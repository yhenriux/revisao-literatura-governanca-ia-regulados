#!/usr/bin/env python3
"""Constrói matriz integral assistida a partir das filas JSONL por página.

As recomendações são pré-adjudicação: não substituem a decisão final do autor,
nem afirmam avaliação JBI/CASP/CERQual concluída.
"""
from __future__ import annotations
import csv, json, re
from pathlib import Path

ROOT = Path.cwd()
SRC = ROOT / "Documentacao_do_projeto/v2.1/triagem_texto_completo"
OUT = SRC / "MATRIZ_DECISAO_INTEGRAL_APOIO_INCERTOS_V2.1.csv"
REPORT = SRC / "RELATORIO_DA_MATRIZ_INTEGRAL_APOIO_INCERTOS_V2.1.md"
FILES = [SRC / "FILA_DE_TRIAGEM_INTEGRAL_APOIO_V2.1.jsonl", SRC / "FILA_DE_TRIAGEM_INTEGRAL_INCERTOS_V2.1.jsonl"]

PATTERNS = {
    "llm": r"large language model|\bLLM\b|generative AI|ChatGPT|chatbot|conversational AI|AI agent",
    "technical": r"RAG|retrieval augmented|guardrail|monitoring|observability|logging|evaluation|robustness|hallucination|privacy",
    "interactional": r"human oversight|human-in-the-loop|supervision|escalation|handoff|explainab|transparen|contestab|redress|appeal|user experience",
    "organizational": r"governance|accountability|workflow|role|responsib|incident|organization|organizational|institution",
    "regulatory": r"regulat|compliance|legal|liability|GDPR|AI Act|FDA|clinical|healthcare|financial|finance|public sector|government",
    "evolutionary": r"continuous|feedback|learning|adapt|post-market|lifecycle|drift|updat|monitoring|surveillance",
    "empirical": r"\bmethod(s)?\b|\bdata\b|experiment|evaluation|study|results|participants|sample|audit",
    "review": r"systematic review|scoping review|survey|literature review|evidence synthesis|meta-analysis",
    "conceptual": r"framework|conceptual|propos|model|taxonomy|guideline|policy",
}

SECTOR_PATTERNS = {
    "saúde": r"health|clinical|medical|hospital|mental health|patient|physician|healthcare",
    "finanças": r"bank|financial|finance|insurance|credit|AML|Basel",
    "governo": r"government|public sector|public service|policy|municipal|civil infrastructure",
    "jurídico/regulatório": r"legal|law|liability|regulat|compliance|AI Act",
    "educação": r"education|university|student|academic|scholarship|school",
    "organizacional transversal": r"organization|enterprise|corporate|workplace|business",
}

def first_evidence(item: dict, families: list[str]) -> tuple[str, str]:
    for family in families:
        values = item.get("evidencias_por_familia", {}).get(family, [])
        if values:
            return values[0].get("pagina", ""), values[0].get("trecho", "")
    return "", ""

def match(pattern: str, text: str) -> bool:
    return bool(re.search(pattern, text or "", re.I))

def main() -> int:
    rows = []
    for source in FILES:
        with source.open(encoding="utf-8") as handle:
            rows.extend(json.loads(line) for line in handle if line.strip())
    output = []
    for item in sorted(rows, key=lambda x: x["id_v21"]):
        text = " ".join([item.get("titulo", ""), item.get("autores", ""), json.dumps(item.get("evidencias_por_familia", {}), ensure_ascii=False)])
        flags = {name: match(pattern, text) for name, pattern in PATTERNS.items()}
        sectors = [name for name, pattern in SECTOR_PATTERNS.items() if match(pattern, text)]
        layers = []
        if flags["technical"]: layers.append("técnica")
        if flags["interactional"]: layers.append("interacional")
        if flags["organizational"]: layers.append("organizacional")
        if flags["regulatory"]: layers.append("regulatória")
        if flags["evolutionary"]: layers.append("evolutiva")
        mechanisms = []
        for label, flag in [("observabilidade/monitoramento", flags["technical"]), ("supervisão/escalonamento", flags["interactional"]), ("accountability/roles", flags["organizational"]), ("compliance/auditoria", flags["regulatory"]), ("feedback/ciclo de vida", flags["evolutionary"])]:
            if flag: mechanisms.append(label)
        if flags["review"]: design = "revisão/survey"
        elif flags["empirical"]: design = "estudo empírico (confirmar desenho)"
        elif flags["conceptual"]: design = "framework/política conceitual"
        else: design = "não determinado pela extração"
        title = item.get("titulo", "")
        title_llm = match(PATTERNS["llm"], title)
        title_governance = match(r"governance|accountability|oversight|audit|compliance|risk|safety|regulat|supervision|guardrail", title)
        title_regulated = match(r"health|clinical|medical|bank|financial|finance|legal|government|public|education|regulated", title)
        original = item.get("classe_triagem", "")
        if title_llm and title_governance and title_regulated and flags["regulatory"]:
            suggested = "candidata a evidência central — confirmar critérios"
        elif title_llm and (title_governance or flags["organizational"] or flags["interactional"]):
            suggested = "candidata a evidência de apoio — confirmar critérios"
        elif original == "candidata_evidencia_apoio" and flags["llm"]:
            suggested = "apoio contextual — verificar contribuição substantiva"
        else:
            suggested = "incerta/excluir ou contextualizar — confirmar texto completo"
        page, excerpt = first_evidence(item, ["governanca", "regulacao", "supervisao", "llm"])
        output.append({
            "id_v21": item["id_v21"], "classe_triagem_original": item.get("classe_triagem", ""),
            "titulo": item.get("titulo", ""), "autores": item.get("autores", ""), "ano": item.get("ano", ""),
            "doi": item.get("doi", ""), "arquivo_pdf": item.get("arquivo_pdf", ""), "sha256_pdf": item.get("sha256_pdf", ""),
            "paginas_pdf": item.get("paginas_pdf", ""), "desenho_assistido": design,
            "setor_assistido": "; ".join(sectors) or "não determinado", "mecanismos_assistidos": "; ".join(mechanisms) or "não determinado",
            "camadas_assistidas": "; ".join(layers) or "não determinado", "pagina_evidencia_assistida": page,
            "trecho_evidencia_assistida": excerpt[:1200], "decisao_assistida_integral": suggested,
            "justificativa_assistida": "A sugestão combina objeto LLM/conversacional e mecanismos de governança localizados no texto extraído; requer conferência humana.",
            "qualidade_jbi_casp": "pendente de avaliação design-específica pelo autor",
            "cerqual": "pendente no nível do achado; não aplicar automaticamente ao artigo",
            "limitacoes_assistidas": "Extração textual e padrões lexicais podem perder contexto, tabelas, figuras ou negações; verificar PDF.",
            "decisao_final_autor": "", "justificativa_final_autor": "", "pagina_decisao_final": "", "data_validacao_autor": "",
        })
    fields = list(output[0].keys())
    with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader(); writer.writerows(output)
    counts = {}
    for row in output: counts[row["decisao_assistida_integral"]] = counts.get(row["decisao_assistida_integral"], 0) + 1
    lines = ["# Matriz integral assistida — apoio e incertos v2.1", "", f"Registros processados: {len(output)}.", "", "| Sugestão assistida | Registros |", "|---|---:|"]
    lines.extend(f"| {key} | {value} |" for key, value in sorted(counts.items()))
    lines.extend(["", "Os campos de decisão final do autor estão vazios por desenho. A matriz não incorpora estudos ao corpus e não apresenta a extração assistida como avaliação metodológica concluída."])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__": raise SystemExit(main())
