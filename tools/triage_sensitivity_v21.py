"""Triagem assistida e reproduzível da busca prospectiva da v2.1.

O script organiza decisões por título/resumo. Ele não se apresenta como segundo
revisor humano e não altera automaticamente o corpus publicado.
"""

from __future__ import annotations

import csv
import html
import json
import os
import re
import unicodedata
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(os.environ.get("REV_LIT_ROOT", Path(__file__).resolve().parents[1]))
SOURCE = ROOT / "Documentacao_do_projeto" / "v2.1" / "busca_de_sensibilidade" / "Resultados_recuperados_v2.1.csv"
UNIVERSE = ROOT / "Documentacao_do_projeto" / "methodology" / "CORPUS_UNIVERSE_RECONCILIATION.csv"
OUT = ROOT / "Documentacao_do_projeto" / "v2.1" / "triagem_assistida"


LLM_TERMS = (
    "large language model", "large-language model", " llm ", "llms", "chatgpt",
    "generative ai", "generative artificial intelligence", "foundation model",
    "conversational ai", "conversational agent", "chatbot", "ai assistant",
    "artificial intelligence assistant", "ai agent", "retrieval augmented generation",
    "retrieval-augmented generation", " rag ",
)
GENERIC_AI_TERMS = ("artificial intelligence", " ai ", "machine learning", "algorithmic")
GOVERNANCE_TERMS = (
    "governance", "govern", "accountability", "accountable", "audit", "compliance",
    "regulat", "oversight", "risk management", "risk assessment", "guardrail",
    "monitoring", "observability", "responsible ai", "responsible artificial intelligence",
    "transparen", "explainab", "human oversight", "human-in-the-loop", "human in the loop",
    "contestab", "redress", "appeal", "incident", "safety", "security", "privacy",
    "bias", "fairness", "ethical", "ethics", "quality assurance", "validation",
)
STRONG_GOVERNANCE_TERMS = (
    "governance", "governing", "accountability", "accountable", "audit", "compliance",
    "regulat", "oversight", "risk management", "guardrail", "responsible use",
    "responsible ai", "safety", "observability", "human-in-the-loop", "human oversight",
    "contestab", "redress", "liability", "traceability",
)
REGULATED_TERMS = (
    "health", "medical", "medicine", "clinical", "patient", "hospital", "pharma",
    "finance", "financial", "bank", "credit", "insurance", "fintech",
    "legal", "law ", "judicial", "justice", "court", "lawyer",
    "government", "public sector", "public administration", "public service",
    "education", "school", "university", "critical infrastructure", "telecom",
    "high-stakes", "high stakes", "regulated", "regulatory", "compliance",
    "gdpr", "hipaa", "data protection", "consumer protection", "employment", "hiring",
)
SUBSTANTIVE_TERMS = (
    "framework", "model", "method", "evaluation", "evaluat", "empirical", "experiment",
    "systematic review", "scoping review", "literature review", "architecture", "protocol",
    "implementation", "case study", "dataset", "benchmark", "guideline", "policy",
    "taxonomy", "assessment", "analysis", "survey", "interview", "design", "mechanism",
)
EXCLUSION_SIGNALS = (
    "course syllabus", "student assignment", "editorial introduction", "book review",
    "conference program", "call for papers", "correction to", "erratum",
)


def norm(value: str | None) -> str:
    text = html.unescape(html.unescape(value or ""))
    text = re.sub(r"<[^>]+>", " ", text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return f" {re.sub(r'\s+', ' ', text).strip()} "


def hits(text: str, terms: tuple[str, ...]) -> list[str]:
    return sorted({term.strip() for term in terms if term in text})


def historical_titles() -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    with UNIVERSE.open(encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            if row.get("integra_universo_407") == "sim":
                rows.append((row.get("identificador", ""), norm(row.get("titulo"))))
    return rows


def closest_historical(title: str, historical: list[tuple[str, str]]) -> tuple[str, float]:
    if not title.strip():
        return "", 0.0
    best_id, best_score = "", 0.0
    for identifier, candidate in historical:
        score = SequenceMatcher(None, title, candidate).ratio()
        if score > best_score:
            best_id, best_score = identifier, score
    return best_id, best_score


def classify(row: dict[str, str], historical: list[tuple[str, str]]) -> dict[str, str | int | float]:
    title = norm(row.get("titulo"))
    abstract = norm(row.get("resumo"))
    combined = f"{title} {abstract}"
    llm_title = hits(title, LLM_TERMS)
    llm_all = hits(combined, LLM_TERMS)
    ai_all = hits(combined, GENERIC_AI_TERMS)
    gov_title = hits(title, GOVERNANCE_TERMS)
    strong_gov_title = hits(title, STRONG_GOVERNANCE_TERMS)
    gov_all = hits(combined, GOVERNANCE_TERMS)
    regulated = hits(combined, REGULATED_TERMS)
    substantive = hits(combined, SUBSTANTIVE_TERMS)
    negative = hits(combined, EXCLUSION_SIGNALS)
    year_text = (row.get("ano") or "").strip()
    year = int(year_text) if year_text.isdigit() else 0

    c1 = bool(llm_title or len(llm_all) >= 2)
    c2 = bool(regulated)
    c3 = bool(strong_gov_title or len(gov_all) >= 3) and bool(substantive)
    score = min(100, len(llm_title) * 18 + len(llm_all) * 6 + len(gov_title) * 12 + len(gov_all) * 4 + len(regulated) * 3 + len(substantive) * 2)

    near_id, similarity = closest_historical(title, historical)
    near_duplicate = similarity >= 0.94

    if negative:
        decision = "excluir"
        reason = "Tipo documental incompatível com o corpus."
    elif year and year < 2020:
        decision = "referencia_contextual" if (gov_all and (llm_all or ai_all)) else "excluir"
        reason = "Anterior a 2020; preservável apenas como referência fundacional/contextual."
    elif near_duplicate:
        decision = "duplicata_historica_provavel"
        reason = f"Título muito semelhante ao registro histórico {near_id}."
    elif llm_title and strong_gov_title and c2 and c3:
        decision = "candidata_evidencia_central"
        reason = "Atende, por título/resumo, aos três critérios cumulativos de centralidade."
    elif c1 and substantive and (gov_title or len(gov_all) >= 3):
        decision = "candidata_evidencia_apoio"
        reason = "Trata diretamente de LLM/sistema conversacional e oferece contribuição de governança, mas não confirma todos os critérios centrais."
    elif (llm_all and gov_all) or (ai_all and c2 and len(gov_all) >= 2):
        decision = "incerta_exige_texto_completo"
        reason = "Há sinais de tecnologia e governança, porém título/resumo não permitem decisão estável."
    elif gov_all and (llm_all or ai_all):
        decision = "referencia_contextual"
        reason = "Contribuição adjacente ou contextual, sem aderência suficiente ao corpus analítico."
    else:
        decision = "excluir"
        reason = "Título/resumo não demonstram simultaneamente objeto tecnológico e mecanismo de governança pertinente."

    if not abstract.strip() and decision not in {"excluir", "duplicata_historica_provavel"}:
        decision = "incerta_exige_texto_completo"
        reason = "Metadado sem resumo; o título sugere pertinência, mas exige texto completo."

    return {
        "c1_objeto_direto": "sim" if c1 else "nao",
        "c2_contexto_regulado": "sim" if c2 else "nao",
        "c3_contribuicao_substantiva": "sim" if c3 else "nao",
        "pontuacao_priorizacao": score,
        "decisao_assistida": decision,
        "justificativa_assistida": reason,
        "termos_llm": " | ".join(llm_all),
        "termos_governanca": " | ".join(gov_all),
        "termos_governanca_no_titulo": " | ".join(strong_gov_title),
        "termos_contexto": " | ".join(regulated),
        "termos_contribuicao": " | ".join(substantive),
        "duplicata_historica_provavel_de": near_id if near_duplicate else "",
        "duplicata_nova_de": "",
        "similaridade_titulo_historico": round(similarity, 4),
        "necessita_texto_completo": "sim" if decision in {"candidata_evidencia_central", "candidata_evidencia_apoio", "incerta_exige_texto_completo"} else "nao",
        "decisao_final_autor": "",
        "justificativa_final_autor": "",
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    historical = historical_titles()
    source_rows: list[dict[str, str]] = []
    with SOURCE.open(encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            if row.get("status_validacao_humana") == "pendente":
                source_rows.append(row)

    rows = [{**row, **classify(row, historical)} for row in source_rows]

    # DOI divergente não impede duplicidade. Mantém a representação mais completa
    # de cada título normalizado e marca as demais para reconciliação.
    by_title: dict[str, list[dict[str, str | int | float]]] = {}
    for row in rows:
        by_title.setdefault(norm(str(row.get("titulo", ""))), []).append(row)
    for group in by_title.values():
        if len(group) < 2:
            continue
        group.sort(key=lambda row: (bool(row.get("doi")), len(str(row.get("resumo", ""))), int(row["pontuacao_priorizacao"])), reverse=True)
        keeper = group[0]
        keeper_key = str(keeper.get("doi") or keeper.get("identificador_fonte") or keeper.get("titulo"))
        for duplicate in group[1:]:
            duplicate["decisao_assistida"] = "duplicata_nova_execucao"
            duplicate["justificativa_assistida"] = "Mesmo título recuperado em outra fonte ou com outro identificador."
            duplicate["duplicata_nova_de"] = keeper_key
            duplicate["necessita_texto_completo"] = "nao"
    rows.sort(key=lambda row: (-int(row["pontuacao_priorizacao"]), row["decisao_assistida"], row["titulo"]))
    fields = list(rows[0])
    with (OUT / "TRIAGEM_ASSISTIDA_DOS_REGISTROS_V2.1.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(str(row["decisao_assistida"]) for row in rows)
    full_text = sum(row["necessita_texto_completo"] == "sim" for row in rows)
    report = [
        "# Relatório da triagem assistida — v2.1",
        "",
        "A triagem utiliza título, resumo, metadados e regras reproduzíveis. A decisão assistida não substitui a decisão científica final do autor.",
        "",
        "## Resultado",
        "",
        "| Classe assistida | Registros |",
        "|---|---:|",
    ]
    for key in ("candidata_evidencia_central", "candidata_evidencia_apoio", "incerta_exige_texto_completo", "referencia_contextual", "duplicata_historica_provavel", "duplicata_nova_execucao", "excluir"):
        report.append(f"| {key} | {counts.get(key, 0)} |")
    report.extend([
        "",
        f"- Total processado: {len(rows)}.",
        f"- Registros que exigem texto completo antes de inclusão: {full_text}.",
        "- Nenhum registro foi incorporado automaticamente ao corpus.",
        "- PubMed, CORE e Semantic Scholar não integram esta execução prospectiva, por decisão metodológica registrada.",
        "",
        "## Regra de centralidade",
        "",
        "Uma candidata central deve cumprir simultaneamente: objeto direto de governança de LLM/sistema conversacional; relação explícita com ambiente regulado ou de alto impacto; e contribuição substantiva para as perguntas da revisão.",
    ])
    (OUT / "RELATORIO_DA_TRIAGEM_ASSISTIDA_V2.1.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({"processados": len(rows), "classes": counts, "texto_completo": full_text}, ensure_ascii=False, default=dict))


if __name__ == "__main__":
    main()
