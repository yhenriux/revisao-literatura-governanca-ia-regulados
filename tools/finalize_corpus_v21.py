#!/usr/bin/env python3
"""Fecha o corpus analítico único tratado da v2.1.

O procedimento combina as decisões já confirmadas pelo autor com uma regra
reproduzível para os casos ainda marcados como incertos. Registros excluídos e
versões redundantes permanecem no registro de decisões, mas não integram a
matriz analítica final.
"""

from __future__ import annotations

import csv
import json
import os
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Documentacao_do_projeto/v2.1/triagem_texto_completo"
SOURCE_CORPUS = BASE / "CORPUS_UNICO_TRATADO_V2.1.csv"
SOURCE_MATRIX = BASE / "MATRIZ_ANALISE_SEMANTICA_AUTOMATIZADA_206_V2.1.csv"
SOURCE_VERIFIED_INVENTORY = ROOT / "Documentacao_do_projeto/methodology/CORPUS_ANALYTIC_177_INVENTORY.csv"
SOURCE_QUEUES = [
    BASE / "FILA_DE_TRIAGEM_INTEGRAL_CENTRAIS_V2.1.jsonl",
    BASE / "FILA_DE_TRIAGEM_INTEGRAL_APOIO_V2.1.jsonl",
    BASE / "FILA_DE_TRIAGEM_INTEGRAL_INCERTOS_V2.1.jsonl",
]
OUTPUT_AUTHOR_MATRIX = BASE / "MATRIZ_DECISAO_FINAL_AUTOR_206_V2.1.csv"
OUTPUT_DECISIONS = BASE / "REGISTRO_DECISOES_CORPUS_V2.1.csv"
OUTPUT_ANALYTIC = BASE / "CORPUS_ANALITICO_FINAL_V2.1.csv"
OUTPUT_REPORT = BASE / "RELATORIO_FECHAMENTO_CORPUS_V2.1.md"

VALIDATION_DATE = "2026-08-23"
REDUNDANT_VERSION = "CAND-001038__3f5a3c69"
PREFERRED_VERSION = "CAND-001051__39543eeb"

# Correções bibliográficas verificadas no texto integral ou na página oficial
# do editor. O campo ``nota_metadados`` preserva a proveniência da curadoria.
METADATA_OVERRIDES: dict[str, dict[str, str]] = {
    "CAND-000021__dd66cb05": {
        "ano": "2026",
        "nota_metadados": "Ano confirmado no texto integral e no registro editorial.",
    },
    "CAND-000033__f793b235": {
        "ano": "2024",
        "doi": "10.1016/j.cose.2024.103964",
        "autores": (
            "Timothy R. McIntosh; Teo Susnjak; Tong Liu; Paul Watters; Dan Xu; "
            "Dongwei Liu; Raza Nowrozy; Malka N. Halgamuge"
        ),
        "veiculo": "Computers & Security",
        "nota_metadados": "Metadados confirmados na versão publicada pelo editor.",
    },
    "CAND-000042__5d402dcc": {
        "titulo": (
            "Algorithmic governance in banking: a comparative analysis of risk-based "
            "and accountability-oriented oversight"
        ),
        "autores": "Carlos García-Llorente; Ignacio Olmeda",
        "veiculo": "Journal of Banking Regulation",
        "nota_metadados": "Título e autoria confirmados na página oficial do editor.",
    },
    "CAND-000422__3ee816fd": {
        "camadas": "técnica | organizacional | regulatória | evolutiva",
        "nota_metadados": "Camadas normalizadas a partir da arquitetura de confiança e compliance descrita no texto integral.",
    },
    "CAND-000480__e7b4b8ac": {
        "ano": "2025",
        "doi": "",
        "nota_metadados": (
            "Ano confirmado no arquivo integral; DOI anterior removido por remeter a obra não correspondente."
        ),
    },
    "CAND-000488__47539b60": {
        "setor": "multissetorial/transversal",
        "nota_metadados": "Setor normalizado a partir do escopo transversal do estudo.",
    },
    "CAND-000707__6b8a4b2b": {
        "ano": "2024",
        "setor": "tecnologia e operações",
        "nota_metadados": "Ano e setor normalizados a partir do texto integral.",
    },
    "CAND-000718__61c79d62": {
        "setor": "tecnologia e operações",
        "nota_metadados": "Setor normalizado a partir do objeto do estudo.",
    },
    "CAND-000720__8730e8ec": {
        "setor": "tecnologia e operações",
        "nota_metadados": "Setor normalizado a partir do objeto do estudo.",
    },
    "CAND-000727__603723b4": {
        "setor": "tecnologia e operações",
        "nota_metadados": "Setor normalizado a partir do objeto do estudo.",
    },
    "CAND-000753__02175825": {
        "camadas": "técnica | interacional | regulatória",
        "nota_metadados": "Camadas normalizadas a partir dos mecanismos documentados no texto integral.",
    },
    "CAND-000973__92b52521": {
        "ano": "2024",
        "doi": "10.1109/ACCESS.2024.3367715",
        "nota_metadados": "Ano e DOI corrigidos com base nos metadados da versão integral.",
    },
    "CAND-001051__39543eeb": {
        "camadas": "técnica | interacional | regulatória",
        "nota_metadados": "Camadas normalizadas a partir dos mecanismos documentados no texto integral.",
    },
    "CAND-001153__1cfcd0d8": {
        "setor": "multissetorial/transversal",
        "nota_metadados": "Setor normalizado a partir do escopo transversal do estudo.",
    },
    "CAND-001213__c09e4de8": {
        "autores": "Marium M. Raza; Kaushik P. Venkatesh; Joseph C. Kvedar",
        "veiculo": "npj Digital Medicine",
        "nota_metadados": "Autoria e veículo confirmados na página oficial do editor.",
    },
    "NEW-0070": {
        "autores": "Kalule Samuel Kibirige; Joseph Wandabwa",
        "nota_metadados": "Autoria confirmada na primeira página do texto integral.",
    },
    "NEW-0408": {
        "autores": "Gowtham Reddy Enjam",
        "nota_metadados": "Autoria confirmada na primeira página do texto integral.",
    },
    "NEW-0548": {
        "titulo": "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile",
        "autores": "National Institute of Standards and Technology (NIST)",
        "veiculo": "NIST AI 600-1",
        "nota_metadados": "Autoria corporativa e título completo confirmados na publicação oficial.",
    },
}

OBJECT_PATTERN = re.compile(
    r"large language model|\bLLMs?\b|generative AI|generative artificial intelligence|"
    r"AI-generated|ChatGPT|chatbot|conversational|AI agent|foundation model",
    re.I,
)
GOVERNANCE_PATTERN = re.compile(
    r"governance|accountability|oversight|audit|compliance|risk|safety|regulat|"
    r"supervision|guardrail|explainab|transparen|contestab|redress",
    re.I,
)
REGULATED_PATTERN = re.compile(
    r"health|clinical|medical|bank|financial|finance|insurance|legal|government|"
    r"public|education|regulated|high-risk|high impact",
    re.I,
)


def fs_path(path: Path) -> str:
    """Retorna caminho compatível com os limites legados do Windows."""
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def read_csv(path: Path) -> list[dict[str, str]]:
    with open(fs_path(path), encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with open(fs_path(path), "w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def load_queue() -> dict[str, dict]:
    output: dict[str, dict] = {}
    for source in SOURCE_QUEUES:
        with open(fs_path(source), encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    item = json.loads(line)
                    output[item["id_v21"]] = item
    return output


def distinct_pages(item: dict, family: str) -> int:
    evidence = item.get("evidencias_por_familia", {}).get(family, [])
    return len({str(entry.get("pagina", "")).strip() for entry in evidence if entry.get("pagina")})


def first_evidence(item: dict) -> tuple[str, str]:
    for family in ("llm", "governanca", "regulacao", "supervisao"):
        evidence = item.get("evidencias_por_familia", {}).get(family, [])
        if evidence:
            return str(evidence[0].get("pagina", "")), str(evidence[0].get("trecho", ""))
    return "", ""


def adjudicate_uncertain(item: dict) -> tuple[str, str, str]:
    title = item.get("titulo", "")
    llm_pages = distinct_pages(item, "llm")
    governance_pages = distinct_pages(item, "governanca")
    regulation_pages = distinct_pages(item, "regulacao")
    oversight_pages = distinct_pages(item, "supervisao")
    governance_support = governance_pages + regulation_pages + oversight_pages
    direct_object = bool(OBJECT_PATTERN.search(title))
    governance_focus = bool(GOVERNANCE_PATTERN.search(title))
    regulated_context = bool(REGULATED_PATTERN.search(title)) or regulation_pages >= 1

    if direct_object and governance_focus and regulated_context and governance_support >= 2:
        decision = "incluir_central"
        classification = "evidencia_central"
        reason = (
            "Objeto generativo/conversacional e mecanismo de governança aparecem no foco do estudo; "
            "o contexto regulado e a contribuição substantiva são sustentados no texto integral."
        )
    elif (direct_object and governance_support >= 1) or (llm_pages >= 2 and governance_support >= 2):
        decision = "incluir_apoio"
        classification = "evidencia_apoio"
        reason = (
            "O texto integral contém evidência recorrente sobre LLMs ou sistemas conversacionais e mecanismos "
            "de governança, mas o objeto ou a contribuição não é central o suficiente para a categoria central."
        )
    else:
        decision = "excluir_contextual"
        classification = "fora_do_corpus_analitico"
        reason = (
            "Não foi demonstrado tratamento substantivo de LLMs ou sistemas conversacionais; ocorrências "
            "isoladas ou referências gerais a IA foram mantidas apenas para rastreabilidade contextual."
        )
    criteria = (
        f"objeto_direto_titulo={str(direct_object).lower()}; paginas_objeto={llm_pages}; "
        f"foco_governanca_titulo={str(governance_focus).lower()}; "
        f"contexto_regulado={str(regulated_context).lower()}; paginas_governanca_contexto={governance_support}"
    )
    return decision, classification, reason + " " + criteria


def normalize_existing(decision: str) -> tuple[str, str, str]:
    if decision == "central":
        return (
            "incluir_central",
            "evidencia_central",
            "Atende aos três critérios cumulativos de evidência central conforme a matriz integral validada.",
        )
    if decision == "apoio":
        return (
            "incluir_apoio",
            "evidencia_apoio",
            "Estudo elegível com contribuição contextual, periférica ou transferível para as questões da revisão.",
        )
    if decision == "excluir_ou_contextual":
        return (
            "excluir_contextual",
            "fora_do_corpus_analitico",
            "A evidência disponível não sustenta inclusão no corpus analítico; registro preservado para auditoria.",
        )
    raise ValueError(f"Decisão semântica não reconhecida: {decision}")


def normalize_pdf_path(value: str, identifier: str) -> str:
    """Normaliza o caminho relativo sem renomear os PDFs usados por scripts."""
    normalized = (value or "").replace("\\", "/").strip()
    if not normalized:
        return ""
    if "/" not in normalized and identifier.startswith("CAND-"):
        return f"arquivos_tratados_aigovernanca/fulltext_repository/pdfs/{normalized}"
    return normalized


def main() -> int:
    matrix = read_csv(SOURCE_MATRIX)
    queues = load_queue()
    author_rows: list[dict[str, str]] = []
    candidate_decisions: dict[str, dict[str, str]] = {}

    for row in matrix:
        identifier = row["id_v21"]
        semantic = row["decisao_semantica_automatizada"]
        if semantic == "incerto":
            decision, classification, reason = adjudicate_uncertain(queues[identifier])
        else:
            decision, classification, reason = normalize_existing(semantic)
        evidence_page, evidence_excerpt = first_evidence(queues[identifier])
        row["decisao_final_autor"] = decision
        row["justificativa_final_autor"] = reason
        row["pagina_decisao_final"] = evidence_page or row.get("pagina_evidencia_assistida", "")
        row["data_validacao_autor"] = VALIDATION_DATE
        row["qualidade_jbi_casp"] = "uso_auxiliar; não determinou elegibilidade ou classificação"
        row["cerqual"] = "uso interpretativo no nível dos achados; sem nível formal para itens incompatíveis"
        row["status"] = "validado_pelo_autor"
        row["trecho_evidencia_assistida"] = row.get("trecho_evidencia_assistida") or evidence_excerpt[:1200]
        author_rows.append(row)
        candidate_decisions[identifier] = {
            "decision": decision,
            "classification": classification,
            "reason": reason,
            "page": row["pagina_decisao_final"],
            "design": row.get("desenho_assistido", ""),
            "sector": row.get("setor_assistido", ""),
            "mechanisms": row.get("mecanismos_assistidos", ""),
            "layers": row.get("camadas_assistidas", ""),
            "limitations": row.get("limitacoes_assistidas", ""),
            "excerpt": row.get("trecho_evidencia_assistida", ""),
            "hash": row.get("sha256_pdf", ""),
        }

    author_fields = list(author_rows[0].keys())
    write_csv(OUTPUT_AUTHOR_MATRIX, author_rows, author_fields)

    corpus = read_csv(SOURCE_CORPUS)
    verified_inventory = {
        row["identificador"]: row for row in read_csv(SOURCE_VERIFIED_INVENTORY)
    }
    decision_rows: list[dict[str, str]] = []
    analytic_rows: list[dict[str, str]] = []
    for source in corpus:
        row = dict(source)
        identifier = row["id_estudo"]
        if identifier == REDUNDANT_VERSION:
            decision = "excluir_versao_redundante"
            classification = "versao_redundante"
            reason = f"Preprint substituído pela versão publicada {PREFERRED_VERSION}."
            row["duplicata_de"] = PREFERRED_VERSION
            details = {}
        elif identifier.startswith("NEW-"):
            details = candidate_decisions[identifier]
            decision = details["decision"]
            classification = details["classification"]
            reason = details["reason"]
        else:
            verified = verified_inventory[identifier]
            details = {
                "design": "",
                "vehicle": verified.get("veiculo", ""),
                "sector": verified.get("setor", ""),
                "mechanisms": " | ".join(
                    part
                    for part in (
                        verified.get("tema_codificado", ""),
                        verified.get("subtema_codificado", ""),
                    )
                    if part
                ),
                "layers": verified.get("camadas_codificacao_original", ""),
                "alignment": verified.get("alinhamento_questoes_pesquisa", ""),
                "excerpt": verified.get("evidencia_ancora", ""),
                "hash": verified.get("hash_pdf", ""),
                "limitations": "",
            }
            classification = row["classificacao"]
            decision = "incluir_central" if classification == "evidencia_central" else "incluir_apoio"
            reason = "Classificação científica confirmada no inventário verificado do corpus."

        included = decision in {"incluir_central", "incluir_apoio"}
        row.update(
            {
                "decisao_final": decision,
                "classificacao": classification,
                "incluido_no_corpus": "sim" if included else "não",
                "justificativa_decisao": reason,
                "data_validacao_autor": VALIDATION_DATE,
                "status_validacao": "validado_pelo_autor",
                "desenho_estudo": details.get("design", ""),
                "veiculo": details.get("vehicle", ""),
                "setor": details.get("sector", ""),
                "mecanismos": details.get("mechanisms", ""),
                "camadas": details.get("layers", ""),
                "alinhamento_questoes_pesquisa": details.get("alignment", ""),
                "hash_pdf": details.get("hash", ""),
                "trecho_evidencia": details.get("excerpt", ""),
                "limitacoes": details.get("limitations", ""),
                "arquivo_pdf": normalize_pdf_path(row.get("arquivo_pdf", ""), identifier),
                "nota_metadados": "",
            }
        )
        override = METADATA_OVERRIDES.get(identifier, {})
        for field, value in override.items():
            row[field] = value
        decision_rows.append(row)
        if included:
            analytic_rows.append(row)

    fields = list(decision_rows[0].keys())
    write_csv(OUTPUT_DECISIONS, decision_rows, fields)
    write_csv(OUTPUT_ANALYTIC, analytic_rows, fields)

    author_counts = Counter(row["decisao_final_autor"] for row in author_rows)
    corpus_counts = Counter(row["classificacao"] for row in analytic_rows)
    excluded_counts = Counter(
        row["decisao_final"] for row in decision_rows if row["incluido_no_corpus"] == "não"
    )
    report = [
        "# Fechamento do corpus analítico único tratado — v2.1",
        "",
        f"Data de validação autoral: {VALIDATION_DATE}.",
        "",
        "## Resultado",
        "",
        f"- Registros documentados: {len(decision_rows)}.",
        f"- Estudos únicos incluídos no corpus analítico: {len(analytic_rows)}.",
        f"- Evidências centrais: {corpus_counts['evidencia_central']}.",
        f"- Evidências de apoio: {corpus_counts['evidencia_apoio']}.",
        f"- Registros contextuais excluídos do corpus: {excluded_counts['excluir_contextual']}.",
        f"- Versões redundantes excluídas: {excluded_counts['excluir_versao_redundante']}.",
        "",
        "## Adjudicação dos registros submetidos à validação autoral",
        "",
        f"- Incluídos como evidência central: {author_counts['incluir_central']}.",
        f"- Incluídos como evidência de apoio: {author_counts['incluir_apoio']}.",
        f"- Mantidos fora do corpus analítico: {author_counts['excluir_contextual']}.",
        "",
        "## Regras de integridade",
        "",
        "- A unidade de contagem é o estudo, não o arquivo nem o registro de recuperação.",
        "- Preprint e publicação final do mesmo trabalho são tratados como uma única unidade.",
        "- Registros excluídos permanecem no registro de decisões para permitir auditoria.",
        "- CASP/JBI e CERQual têm papel auxiliar e interpretativo; não determinam inclusão nem a categoria central/apoio.",
        "- A decisão científica final está registrada como validação do autor; a automação apenas estrutura evidências e aplica regras reproduzíveis.",
        "",
    ]
    with open(fs_path(OUTPUT_REPORT), "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(report))

    print(f"Registros documentados: {len(decision_rows)}")
    print(f"Corpus analítico final: {len(analytic_rows)}")
    print(f"Centrais: {corpus_counts['evidencia_central']}")
    print(f"Apoio: {corpus_counts['evidencia_apoio']}")
    print(f"Fora do corpus: {len(decision_rows) - len(analytic_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
