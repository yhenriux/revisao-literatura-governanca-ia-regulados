#!/usr/bin/env python3
"""Extrai texto por página dos PDFs prospectivos e prepara uma fila auditável."""
from __future__ import annotations
import csv, hashlib, json, os, re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(os.environ.get("REV_LIT_ROOT", Path.cwd()))
MANIFEST = ROOT / "arquivos_tratados_aigovernanca/ft_v21/MANIFESTO_TEXTOS_COMPLETOS_V2.1.csv"
OUT = ROOT / "Documentacao_do_projeto/v2.1/triagem_texto_completo"
PDF_ROOT = ROOT / "arquivos_tratados_aigovernanca/ft_v21/pdfs"
TERMS = {
    "governanca": r"governance|governança|accountability|oversight|audit|compliance|risk",
    "regulacao": r"regulated|regulatory|regulation|healthcare|clinical|financial|finance|legal|public sector|government",
    "llm": r"large language model|\bLLM\b|generative AI|chatbot|conversational AI|AI agent",
    "supervisao": r"human oversight|human-in-the-loop|supervision|escalation|contestability|redress|appeal|audit",
}

def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()

def evidence_pages(pages: list[str], pattern: str) -> list[dict[str, str]]:
    rx = re.compile(pattern, re.I)
    found = []
    for number, text in enumerate(pages, 1):
        match = rx.search(text or "")
        if match:
            start = max(0, match.start() - 240)
            end = min(len(text), match.end() + 420)
            found.append({"pagina": str(number), "trecho": norm(text[start:end])})
    return found[:5]

def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open(encoding="utf-8-sig", newline="") as handle:
        records = list(csv.DictReader(handle))
    target = [r for r in records if r.get("status_pdf") == "obtido_pdf_aberto" and r.get("classe_triagem") == "candidata_evidencia_central"]
    output = OUT / "FILA_DE_TRIAGEM_INTEGRAL_CENTRAIS_V2.1.jsonl"
    summary = []
    with output.open("w", encoding="utf-8") as handle:
        for record in sorted(target, key=lambda r: r["id_v21"]):
            path = ROOT / record["arquivo_pdf"]
            reader = PdfReader(str(path), strict=False)
            pages = [(page.extract_text() or "") for page in reader.pages]
            joined = "\n".join(pages)
            item = {
                "id_v21": record["id_v21"], "titulo": record["titulo"], "autores": record["autores"],
                "ano": record["ano"], "doi": record["doi"], "arquivo_pdf": record["arquivo_pdf"],
                "sha256_pdf": record["sha256"], "paginas_pdf": len(pages), "caracteres_extraidos": len(joined),
                "texto_extraido_completo": True,
                "presenca_termos": {name: bool(re.search(pattern, joined, re.I)) for name, pattern in TERMS.items()},
                "evidencias_por_familia": {name: evidence_pages(pages, pattern) for name, pattern in TERMS.items()},
                "decisao_final_autor": "", "justificativa_final_autor": "", "pagina_evidencia_decisao": "",
                "qualidade_jbi_casp": "", "cerqual": "", "observacoes": "",
            }
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
            summary.append(item)
    md = OUT / "RELATORIO_DA_EXTRAÇÃO_INTEGRAL_CENTRAIS_V2.1.md"
    lines = ["# Extração integral — candidatos a evidência central v2.1", "", f"- PDFs processados: {len(summary)}.", f"- Páginas processadas: {sum(x['paginas_pdf'] for x in summary)}.", f"- Itens com extração textual: {sum(x['texto_extraido_completo'] for x in summary)}.", "", "A extração localiza evidências e páginas; não substitui a decisão científica final do autor.", "", "| ID | Páginas | Caracteres | LLM/governança/regulação/supervisão |", "|---|---:|---:|---|"]
    for item in summary:
        pres = item["presenca_termos"]
        lines.append(f"| {item['id_v21']} | {item['paginas_pdf']} | {item['caracteres_extraidos']} | {pres['llm']}/{pres['governanca']}/{pres['regulacao']}/{pres['supervisao']} |")
    md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
