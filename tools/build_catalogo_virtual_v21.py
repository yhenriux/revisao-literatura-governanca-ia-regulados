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
    historical = read_csv(ROOT / "Documentacao_do_projeto/methodology/CORPUS_ANALYTIC_177_INVENTORY.csv")
    prospective = read_csv(ROOT / "Documentacao_do_projeto/v2.1/triagem_assistida/TRIAGEM_ASSISTIDA_DOS_REGISTROS_V2.1.csv")
    matrix_path = ROOT / "Documentacao_do_projeto/v2.1/triagem_texto_completo/MATRIZ_DECISAO_INTEGRAL_APOIO_INCERTOS_V2.1.csv"
    matrix = {r["id_v21"]: r for r in read_csv(matrix_path)} if matrix_path.exists() else {}
    items = []
    for r in historical:
        items.append({
            "id": r.get("identificador", ""), "titulo": r.get("titulo", ""), "autores": r.get("autores", ""), "ano": r.get("ano", ""),
            "veiculo": r.get("veiculo", ""), "doi_url": r.get("doi_ou_url", ""), "fonte": r.get("fonte_bibliografica_individual", ""),
            "status": "corpus_historico", "classificacao": r.get("classificacao_publicada", ""), "setor": r.get("setor", ""),
            "temas": "; ".join(x for x in [r.get("tema_codificado", ""), r.get("subtema_codificado", "")] if x),
            "camadas": r.get("camadas_codificacao_original", ""), "pagina_evidencia": r.get("pagina_evidencia", ""),
            "arquivo_pdf": r.get("arquivo_pdf", ""), "hash_pdf": r.get("hash_pdf", ""), "qualidade": r.get("status_verificacao", ""),
            "observacao": compact(r.get("justificativa_reconciliacao", "")), "proveniencia": r.get("proveniencia_registro", "")
        })
    for r in prospective:
        rid = r.get("identificador_fonte") or r.get("chave_deduplicacao") or ""
        m = matrix.get(rid, {})
        decision = r.get("decisao_assistida", "")
        status = {"candidata_evidencia_central": "candidato_central", "candidata_evidencia_apoio": "candidato_apoio", "incerta_exige_texto_completo": "incerto", "referencia_contextual": "contextual", "duplicata_historica_provavel": "duplicata_historica", "duplicata_nova_execucao": "duplicata_execucao", "excluir": "excluido"}.get(decision, "prospectivo")
        if m:
            status = "candidato_central_assistido" if "central" in m.get("decisao_assistida_integral", "") else ("candidato_apoio_assistido" if "apoio" in m.get("decisao_assistida_integral", "") else "incerto_assistido")
        items.append({
            "id": rid, "titulo": r.get("titulo", ""), "autores": r.get("autores", ""), "ano": r.get("ano", ""), "veiculo": r.get("fonte", ""),
            "doi_url": r.get("doi") or r.get("url", ""), "fonte": r.get("fonte", ""), "status": status,
            "classificacao": decision, "setor": m.get("setor_assistido", ""), "temas": m.get("mecanismos_assistidos", ""),
            "camadas": m.get("camadas_assistidas", ""), "pagina_evidencia": m.get("pagina_evidencia_assistida", ""),
            "arquivo_pdf": m.get("arquivo_pdf", ""), "hash_pdf": m.get("sha256_pdf", ""), "qualidade": m.get("qualidade_jbi_casp", ""),
            "observacao": compact(m.get("limitacoes_assistidas") or r.get("justificativa_assistida", "")), "proveniencia": "busca prospectiva v2.1"
        })
    payload = {"catalogo": "Catálogo bibliográfico digital — Governança conversacional em LLMs", "versao": "v2.1", "gerado_em": "2026-08-22", "total_registros": len(items), "fonte_de_verdade": ["CORPUS_ANALYTIC_177_INVENTORY.csv", "TRIAGEM_ASSISTIDA_DOS_REGISTROS_V2.1.csv", "MATRIZ_DECISAO_INTEGRAL_APOIO_INCERTOS_V2.1.csv"], "registros": items}
    (OUT / "catalogo.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = {}
    for item in items: counts[item["status"]] = counts.get(item["status"], 0) + 1
    return len(items), counts

if __name__ == "__main__":
    total, counts = build()
    print(f"catalogo={total}")
    for k, v in sorted(counts.items()): print(f"{k}={v}")
