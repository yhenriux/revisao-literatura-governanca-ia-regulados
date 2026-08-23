#!/usr/bin/env python3
"""Resolve e arquiva textos completos abertos dos candidatos prospectivos v2.1.

Não contorna paywalls. Só persiste respostas que sejam PDFs válidos e registra
proveniência, licença informada, URL final, tamanho e SHA-256.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


ROOT = Path(os.environ.get("REV_LIT_ROOT", Path.cwd()))
INPUT = ROOT / "Documentacao_do_projeto/v2.1/triagem_assistida/TRIAGEM_ASSISTIDA_DOS_REGISTROS_V2.1.csv"
BASE = ROOT / "arquivos_tratados_aigovernanca/ft_v21"
PDF_DIR = BASE / "pdfs"
MANIFEST = BASE / "MANIFESTO_TEXTOS_COMPLETOS_V2.1.csv"
REPORT = BASE / "LEIA_ME.md"
TARGET_CLASSES = {
    "candidata_evidencia_central",
    "candidata_evidencia_apoio",
    "incerta_exige_texto_completo",
}
UA = "GovernancaConversacionalReview/2.1 (open-access full-text audit)"


def request_json(url: str, timeout: int = 25) -> dict[str, Any] | None:
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8", errors="replace"))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return None


def safe_name(text: str, limit: int = 78) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")
    return (text[:limit].rstrip("_") or "sem_titulo")


def candidates_from_openalex(doi: str) -> list[dict[str, str]]:
    if not doi:
        return []
    endpoint = "https://api.openalex.org/works/https://doi.org/" + quote(doi, safe="")
    data = request_json(endpoint)
    if not data:
        return []
    locations = []
    if data.get("best_oa_location"):
        locations.append(data["best_oa_location"])
    locations.extend(data.get("locations") or [])
    seen: set[str] = set()
    out = []
    for loc in locations:
        pdf_url = (loc or {}).get("pdf_url")
        if not pdf_url or pdf_url in seen:
            continue
        seen.add(pdf_url)
        out.append({
            "url": pdf_url,
            "resolver": "OpenAlex",
            "license": (loc or {}).get("license") or "não informada",
            "oa_status": (data.get("open_access") or {}).get("oa_status") or "não informado",
        })
    return out


def candidates_from_europe_pmc(doi: str) -> list[dict[str, str]]:
    if not doi:
        return []
    query = quote(f'DOI:"{doi}"')
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={query}&format=json&resultType=core&pageSize=5"
    data = request_json(url)
    out = []
    for result in ((data or {}).get("resultList") or {}).get("result", []):
        pmcid = result.get("pmcid")
        if pmcid:
            out.append({
                "url": f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextPDF",
                "resolver": "Europe PMC",
                "license": result.get("license") or "não informada",
                "oa_status": "repositório Europe PMC",
            })
        for item in ((result.get("fullTextUrlList") or {}).get("fullTextUrl") or []):
            if item.get("documentStyle") == "pdf" and item.get("url"):
                out.append({
                    "url": item["url"],
                    "resolver": "Europe PMC",
                    "license": result.get("license") or "não informada",
                    "oa_status": "link aberto informado",
                })
    return out


def candidates_from_arxiv(doi: str, source_url: str, source_id: str) -> list[dict[str, str]]:
    values = " ".join([doi or "", source_url or "", source_id or ""])
    match = re.search(r"(?:arxiv[:./]|abs/)(\d{4}\.\d{4,5})(?:v\d+)?", values, flags=re.I)
    if not match:
        return []
    return [{
        "url": f"https://arxiv.org/pdf/{match.group(1)}",
        "resolver": "arXiv",
        "license": "licença declarada no registro arXiv",
        "oa_status": "repositório aberto",
    }]


def download_pdf(url: str, destination: Path) -> tuple[bool, str, int, str]:
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/pdf"})
    try:
        with urlopen(req, timeout=50) as response:
            final_url = response.geturl()
            data = response.read(40 * 1024 * 1024 + 1)
    except HTTPError as exc:
        return False, f"http_{exc.code}", 0, url
    except (URLError, TimeoutError) as exc:
        return False, type(exc).__name__.lower(), 0, url
    if len(data) > 40 * 1024 * 1024:
        return False, "arquivo_maior_que_40_mb", len(data), final_url
    if len(data) < 1024 or not data.lstrip().startswith(b"%PDF-"):
        return False, "resposta_nao_pdf", len(data), final_url
    destination.write_bytes(data)
    return True, hashlib.sha256(data).hexdigest(), len(data), final_url


def process(record: dict[str, str]) -> dict[str, str]:
    sid = record["id_v21"]
    doi = (record.get("doi") or "").strip().lower().removeprefix("https://doi.org/")
    title = record.get("titulo") or "sem título"
    # O caminho raiz do projeto já se aproxima do limite legado do Windows.
    # O manifesto mantém o título humano; o arquivo usa apenas o ID estável.
    destination = PDF_DIR / f"{sid}.pdf"
    base = {
        "id_v21": sid,
        "classe_triagem": record.get("decisao_assistida", ""),
        "titulo": title,
        "autores": record.get("autores", ""),
        "ano": record.get("ano", ""),
        "doi": doi,
        "fonte_recuperacao": record.get("fonte", ""),
        "posicao": record.get("posicao", ""),
        "faixa_posicao": record.get("faixa_posicao", ""),
        "status_pdf": "não_obtido",
        "resolver_pdf": "",
        "licenca_informada": "",
        "status_acesso_aberto": "",
        "url_pdf_origem": "",
        "url_pdf_final": "",
        "arquivo_pdf": "",
        "bytes": "0",
        "sha256": "",
        "motivo_nao_obtido": "nenhum_link_pdf_aberto_localizado",
    }
    links = []
    links.extend(candidates_from_arxiv(doi, record.get("url", ""), record.get("identificador_fonte", "")))
    links.extend(candidates_from_europe_pmc(doi))
    links.extend(candidates_from_openalex(doi))
    unique = []
    seen = set()
    for item in links:
        if item["url"] not in seen:
            seen.add(item["url"])
            unique.append(item)
    failures = []
    for item in unique:
        ok, result, size, final_url = download_pdf(item["url"], destination)
        if ok:
            base.update({
                "status_pdf": "obtido_pdf_aberto",
                "resolver_pdf": item["resolver"],
                "licenca_informada": item["license"],
                "status_acesso_aberto": item["oa_status"],
                "url_pdf_origem": item["url"],
                "url_pdf_final": final_url,
                "arquivo_pdf": destination.relative_to(ROOT).as_posix(),
                "bytes": str(size),
                "sha256": result,
                "motivo_nao_obtido": "",
            })
            return base
        failures.append(f"{item['resolver']}:{result}")
    if failures:
        base["motivo_nao_obtido"] = " | ".join(failures)[:500]
    return base


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    with INPUT.open(encoding="utf-8-sig", newline="") as handle:
        source = [row for row in csv.DictReader(handle) if row.get("decisao_assistida") in TARGET_CLASSES]
    unique: dict[str, dict[str, str]] = {}
    for row in source:
        key = row.get("chave_deduplicacao") or (row.get("titulo") or "").casefold()
        unique.setdefault(key, row)
    rows = list(unique.values())
    for index, row in enumerate(rows, 1):
        row["id_v21"] = f"NEW-{index:04d}"
    print(f"Registros únicos para resolução: {len(rows)}", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(process, row): row for row in rows}
        for done, future in enumerate(as_completed(futures), 1):
            try:
                results.append(future.result())
            except Exception as exc:  # mantém auditoria mesmo diante de uma falha isolada
                row = futures[future]
                results.append({
                    "id_v21": row["id_v21"], "classe_triagem": row.get("decisao_assistida", ""),
                    "titulo": row.get("titulo", ""), "autores": row.get("autores", ""),
                    "ano": row.get("ano", ""), "doi": row.get("doi", ""),
                    "fonte_recuperacao": row.get("fonte", ""), "posicao": row.get("posicao", ""),
                    "faixa_posicao": row.get("faixa_posicao", ""), "status_pdf": "erro_resolucao",
                    "resolver_pdf": "", "licenca_informada": "", "status_acesso_aberto": "",
                    "url_pdf_origem": "", "url_pdf_final": "", "arquivo_pdf": "", "bytes": "0",
                    "sha256": "", "motivo_nao_obtido": f"{type(exc).__name__}: {exc}"[:500],
                })
            if done % 25 == 0 or done == len(rows):
                obtained = sum(r["status_pdf"] == "obtido_pdf_aberto" for r in results)
                print(f"Processados {done}/{len(rows)}; PDFs abertos obtidos: {obtained}", flush=True)
    results.sort(key=lambda row: row["id_v21"])
    fields = list(results[0].keys())
    with MANIFEST.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)
    obtained = [r for r in results if r["status_pdf"] == "obtido_pdf_aberto"]
    total_bytes = sum(int(r["bytes"]) for r in obtained)
    by_class: dict[str, list[int]] = {}
    for row in results:
        bucket = by_class.setdefault(row["classe_triagem"], [0, 0])
        bucket[0] += 1
        bucket[1] += row["status_pdf"] == "obtido_pdf_aberto"
    lines = [
        "# Acervo prospectivo de textos completos — v2.1", "",
        "Este diretório contém somente PDFs recuperados de endpoints de acesso aberto. Nenhum paywall foi contornado.", "",
        f"- Registros únicos submetidos à resolução: {len(results)}.",
        f"- PDFs abertos obtidos e validados: {len(obtained)}.",
        f"- Não obtidos: {len(results) - len(obtained)}.",
        f"- Volume total: {total_bytes / 1024 / 1024:.1f} MiB.", "",
        "| Classe de triagem | Registros | PDFs obtidos |", "|---|---:|---:|",
    ]
    for key, values in sorted(by_class.items()):
        lines.append(f"| {key} | {values[0]} | {values[1]} |")
    lines.extend(["", "O manifesto registra DOI, origem, licença informada, URL final, tamanho e SHA-256. A disponibilidade do PDF não determina elegibilidade científica."])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Concluído: {len(obtained)} PDFs, {total_bytes / 1024 / 1024:.1f} MiB", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
