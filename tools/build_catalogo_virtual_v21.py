#!/usr/bin/env python3
"""Gera o catálogo bibliográfico digital a partir dos inventários versionados."""
from __future__ import annotations
import csv, json, os
from pathlib import Path

ROOT = Path.cwd()
OUT = ROOT / "catalogo_virtual"
OUT.mkdir(exist_ok=True)
SOURCE = ROOT / "Documentacao_do_projeto/v2.1/triagem_texto_completo/CORPUS_ANALITICO_FINAL_V2.1.csv"

def fs_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved

def read_csv(path: Path):
    with open(fs_path(path), encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def compact(value: str, limit: int = 600) -> str:
    value = " ".join((value or "").split())
    return value if len(value) <= limit else value[:limit].rstrip() + "…"

def build():
    unified = read_csv(SOURCE)
    items = []
    for r in unified:
        status = "central" if r.get("classificacao") == "evidencia_central" else "apoio"
        unavailable = "Conteúdo não transcrito no catálogo; consulte o PDF rastreado."
        reference = " ".join(part for part in (
            r.get("autores", ""), f"({r.get('ano', '')}).", r.get("titulo", ""),
            r.get("veiculo", ""), r.get("doi", "")
        ) if part).strip()
        secoes = {
            "titulo": r.get("titulo") or "Título não registrado",
            "resumo_abstract": unavailable,
            "palavras_chave_keywords": r.get("mecanismos") or "Palavras-chave não extraídas",
            "introducao": unavailable,
            "referencial_teorico_background": r.get("alinhamento_questoes_pesquisa") or unavailable,
            "metodo_metodologia": r.get("desenho_estudo") or "Desenho não classificado no registro",
            "resultados": compact(r.get("trecho_evidencia", ""), 900) or unavailable,
            "discussao": compact(r.get("limitacoes", ""), 700) or "Limitações específicas não registradas",
            "conclusao": compact(r.get("justificativa_decisao", ""), 700) or "Decisão documentada no registro do corpus",
            "referencias": reference or "Referência bibliográfica incompleta",
        }
        items.append({
            "id": r.get("id_estudo", ""), "titulo": r.get("titulo", ""), "autores": r.get("autores", ""), "ano": r.get("ano", ""), "veiculo": r.get("veiculo", ""),
            "doi_url": r.get("doi", ""), "fonte": "corpus analítico único tratado", "status": status,
            "classificacao": r.get("classificacao", ""), "setor": r.get("setor", ""), "temas": r.get("mecanismos", ""),
            "camadas": r.get("camadas", ""), "pagina_evidencia": r.get("pagina_evidencia", ""),
            "trecho_evidencia": compact(r.get("trecho_evidencia", ""), 1200),
            "arquivo_pdf": r.get("arquivo_pdf", ""), "hash_pdf": r.get("hash_pdf", ""),
            "qualidade": r.get("qualidade_jbi_casp", "uso auxiliar na interpretação"),
            "observacao": compact(r.get("justificativa_decisao", ""), 700),
            "proveniencia": "corpus_analitico_final_v2.1", "secoes_artigo": secoes
        })
    payload = {"catalogo": "Catálogo bibliográfico digital — Corpus analítico único tratado", "versao": "v2.1", "gerado_em": "2026-08-23", "total_registros": len(items), "fonte_de_verdade": ["CORPUS_ANALITICO_FINAL_V2.1.csv"], "estrutura_artigo": list(next(iter(items))["secoes_artigo"].keys()), "registros": items}
    with open(fs_path(OUT / "catalogo.json"), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    counts = {}
    for item in items: counts[item["status"]] = counts.get(item["status"], 0) + 1
    return len(items), counts

if __name__ == "__main__":
    total, counts = build()
    print(f"catalogo={total}")
    for k, v in sorted(counts.items()): print(f"{k}={v}")
