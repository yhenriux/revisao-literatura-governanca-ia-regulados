#!/usr/bin/env python3
"""Gera o catálogo bibliográfico digital a partir dos inventários versionados."""
from __future__ import annotations
import csv, json
from pathlib import Path

ROOT = Path.cwd()
OUT = ROOT / "catalogo_virtual"
OUT.mkdir(exist_ok=True)

def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def compact(value: str, limit: int = 600) -> str:
    value = " ".join((value or "").split())
    return value if len(value) <= limit else value[:limit].rstrip() + "…"

def build():
    unified_path = next(ROOT.rglob("CORPUS_UNICO_TRATADO_V2.1.csv"))
    unified = read_csv(unified_path)
    items = []
    for r in unified:
        status = {"incluir_historico": "incluido", "central": "central", "apoio": "apoio", "incerto": "incerto", "excluir_ou_contextual": "contextual"}.get(r.get("decisao_final", ""), "incerto")
        secoes = {"titulo": r.get("titulo", "não informado no registro"), "resumo_abstract": "não informado no registro", "palavras_chave": "não informado no registro", "introducao": "não informado no registro", "referencial_teorico_background": "não informado no registro", "metodo": "desenho e procedimentos: não informado no registro", "resultados": "não informado no registro", "discussao": "não informado no registro", "conclusao": "não informado no registro", "referencias": "identificação bibliográfica disponível no registro"}
        items.append({
            "id": r.get("id_estudo", ""), "titulo": r.get("titulo", ""), "autores": r.get("autores", ""), "ano": r.get("ano", ""), "veiculo": "",
            "doi_url": r.get("doi", ""), "fonte": "corpus analítico único tratado", "status": status,
            "classificacao": r.get("classificacao", ""), "setor": "não informado no registro", "temas": "não informado no registro",
            "camadas": "não informado no registro", "pagina_evidencia": r.get("pagina_evidencia", ""),
            "arquivo_pdf": r.get("arquivo_pdf", ""), "hash_pdf": "", "qualidade": "não informado no registro",
            "observacao": "Registro bibliográfico do corpus analítico único tratado.", "proveniencia": r.get("proveniencia_tecnica", ""), "secoes_artigo": secoes
        })
    payload = {"catalogo": "Catálogo bibliográfico digital — Corpus analítico único tratado", "versao": "v2.1", "gerado_em": "2026-08-22", "total_registros": len(items), "fonte_de_verdade": ["CORPUS_UNICO_TRATADO_V2.1.csv"], "estrutura_artigo": list(next(iter(items))["secoes_artigo"].keys()), "registros": items}
    (OUT / "catalogo.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = {}
    for item in items: counts[item["status"]] = counts.get(item["status"], 0) + 1
    return len(items), counts

if __name__ == "__main__":
    total, counts = build()
    print(f"catalogo={total}")
    for k, v in sorted(counts.items()): print(f"{k}={v}")
