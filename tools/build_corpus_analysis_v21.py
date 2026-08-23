#!/usr/bin/env python3
"""Normaliza códigos e recalcula as contagens analíticas da v2.1.

Cada número publicado nos gráficos é derivado do corpus analítico final. A
matriz longa preserva a ligação entre estudo, classificação, setor, família de
mecanismos, camada e evidência textual.
"""

from __future__ import annotations

import csv
import os
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Documentacao_do_projeto/v2.1/triagem_texto_completo"
SOURCE = BASE / "CORPUS_ANALITICO_FINAL_V2.1.csv"
DECISIONS = BASE / "REGISTRO_DECISOES_CORPUS_V2.1.csv"
OUTPUT_MATRIX = BASE / "MATRIZ_ESTUDO_MECANISMO_CAMADA_V2.1.csv"
OUTPUT_RECONCILIATION = BASE / "RECONCILIACAO_CONTAGENS_CORPUS_V2.1.md"
OUTPUT_DATA = ROOT / "Recursos_do_artigo/v2.1/dados_figuras_v21.csv"

MECHANISMS = {
    "Compliance e gestão de risco": (
        r"compliance|risk|risco|regulat|governan|governance|policy|politica|standard|norma|"
        r"legal|law|privacy|privacidade|ethic|etica|safety|seguranca"
    ),
    "Controles técnicos e avaliação": (
        r"evaluat|avaliac|benchmark|technical control|controle tecnic|guardrail|security control|"
        r"robust|accuracy|validation|validac|testing|red.?team|architecture|arquitet|model monitoring|"
        r"model performance|desempenho do modelo"
    ),
    "Accountability e auditoria": (
        r"accountab|audit|trace|rastre|provenance|proveniencia|responsib|papel|role|incident|"
        r"record|registro|logging|\blog\b|documenta"
    ),
    "Explicabilidade, confiança e limites": (
        r"explain|explic|transparen|trust|confianc|limit|uncertain|incerteza|disclos|"
        r"interpret|bias|vies|fairness|equidade"
    ),
    "Aprendizagem operacional e monitoramento": (
        r"monitor|observab|feedback|lifecycle|ciclo de vida|drift|continuous|continu|update|"
        r"atualiz|learning|aprendiz|adapt"
    ),
    "Supervisão humana e escalonamento": (
        r"human|humana|humano|oversight|supervis|escalat|human.in.the.loop|reviewer|revisor"
    ),
    "Governança do conhecimento": (
        r"knowledge|conhecimento|retrieval|\brag\b|prompt|grounding|memory|memoria|knowledge source|"
        r"fonte de conhecimento|source citation|citacao de fonte"
    ),
    "Contestabilidade e reparo": (
        r"contest|redress|appeal|recurso|repair|reparo|remedy|remedi|complaint|queixa|recourse"
    ),
}

LAYERS = ["Técnica", "Interacional", "Organizacional", "Regulatória", "Evolutiva"]

FINDINGS = {
    "Avaliação, riscos e qualidade": {
        "Compliance e gestão de risco", "Controles técnicos e avaliação"
    },
    "Supervisão humana e accountability": {
        "Supervisão humana e escalonamento", "Accountability e auditoria"
    },
    "Observabilidade, auditoria e monitoramento": {
        "Aprendizagem operacional e monitoramento", "Accountability e auditoria"
    },
    "Conhecimento, RAG e guardrails": {
        "Governança do conhecimento", "Controles técnicos e avaliação"
    },
    "Confiança, explicabilidade e orientação": {
        "Explicabilidade, confiança e limites", "Supervisão humana e escalonamento"
    },
}


def fs_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def read_csv(path: Path) -> list[dict[str, str]]:
    with open(fs_path(path), encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    if not path.parent.exists():
        os.makedirs(fs_path(path.parent), exist_ok=True)
    with open(fs_path(path), "w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def fold(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    return "".join(char for char in normalized if not unicodedata.combining(char)).lower()


def primary_sector(row: dict[str, str]) -> str:
    title = fold(row.get("titulo", ""))
    supplied = fold(row.get("setor", ""))
    if re.search(r"health|saude|clinic|medical|patient|hospital|mental health|dementia", title):
        return "Saúde e medicina"
    if re.search(r"bank|financ|insurance|seguro|credit|credito|fintech", title):
        return "Finanças e seguros"
    if re.search(r"judici|court|tribunal|legal profession|legal service|law firm", title):
        return "Jurídico e judiciário"
    if re.search(r"education|educacao|student|university|higher education|teaching|learning analytics", title):
        return "Educação"
    if re.search(r"government|governo|public sector|public service|administracao publica|digital governance", title):
        return "Governo e setor público"
    if re.search(r"cyber|telecom|energy|oil|gas|critical infrastructure|industrial|manufactur", title):
        return "Infraestrutura crítica e cibersegurança"
    if re.search(r"enterprise|software|cloud|llmops|developer|agentic|agent\b|operations|deployment", title):
        return "Tecnologia e operações empresariais"
    if ";" in supplied or "multisset" in supplied or "cross-sector" in supplied or "diverse" in supplied:
        return "Multissetorial"
    if re.search(r"health|saude|clinic|medical", supplied):
        return "Saúde e medicina"
    if re.search(r"bank|financ|insurance|seguro", supplied):
        return "Finanças e seguros"
    if re.search(r"education|educacao|university", supplied):
        return "Educação"
    if re.search(r"judici|legal|law", supplied):
        return "Jurídico e judiciário"
    if re.search(r"government|governo|public", supplied):
        return "Governo e setor público"
    if re.search(r"cyber|telecom|energy|industrial|critical", supplied):
        return "Infraestrutura crítica e cibersegurança"
    if re.search(r"enterprise|software|cloud|operation|technology|tecnologia", supplied):
        return "Tecnologia e operações empresariais"
    return "Multissetorial"


def mechanism_families(row: dict[str, str]) -> list[str]:
    text = fold(" | ".join(
        row.get(field, "")
        for field in ("titulo", "mecanismos", "camadas", "trecho_evidencia")
    ))
    selected = [name for name, pattern in MECHANISMS.items() if re.search(pattern, text)]
    return selected or ["Compliance e gestão de risco"]


def normalized_layers(row: dict[str, str], mechanisms: list[str]) -> list[str]:
    raw = fold(row.get("camadas", ""))
    text = fold(" | ".join((row.get("titulo", ""), row.get("mecanismos", ""), raw)))
    chosen: set[str] = set()
    aliases = {
        "Técnica": r"tecnic|technical|evaluation|avaliac|control|architecture|guardrail|retrieval|\brag\b",
        "Interacional": r"interacion|interaction|interface|user|usuario|explain|explic|trust|confianc|contest|redress",
        "Organizacional": r"organiz|accountab|audit|oversight|supervis|role|papel|incident|workflow|governance",
        "Regulatória": r"regulator|regulat|compliance|legal|law|norma|standard|policy|privacy|risk|risco",
        "Evolutiva": r"evolut|lifecycle|ciclo de vida|monitor|observab|feedback|drift|update|adapt|learning",
    }
    for layer, pattern in aliases.items():
        if re.search(pattern, text):
            chosen.add(layer)
    if "Controles técnicos e avaliação" in mechanisms or "Governança do conhecimento" in mechanisms:
        chosen.add("Técnica")
    if "Explicabilidade, confiança e limites" in mechanisms or "Contestabilidade e reparo" in mechanisms:
        chosen.add("Interacional")
    if "Accountability e auditoria" in mechanisms or "Supervisão humana e escalonamento" in mechanisms:
        chosen.add("Organizacional")
    if "Compliance e gestão de risco" in mechanisms:
        chosen.add("Regulatória")
    if "Aprendizagem operacional e monitoramento" in mechanisms:
        chosen.add("Evolutiva")
    return [layer for layer in LAYERS if layer in chosen] or ["Técnica"]


def add_data(rows: list[dict[str, str]], figure: str, categories: list[str], series: list[str],
             counter: dict[tuple[str, str], int], provenance: str) -> None:
    for order, category in enumerate(categories, 1):
        for item in series:
            rows.append({
                "figura": figure,
                "ordem": str(order),
                "categoria": category,
                "serie": item,
                "valor": str(counter.get((category, item), 0)),
                "proveniencia": provenance,
            })


def main() -> int:
    corpus = read_csv(SOURCE)
    decisions = read_csv(DECISIONS)
    matrix: list[dict[str, str]] = []
    study_codes: dict[str, tuple[str, list[str], list[str], str]] = {}
    for row in corpus:
        sector = primary_sector(row)
        mechanisms = mechanism_families(row)
        layers = normalized_layers(row, mechanisms)
        study_codes[row["id_estudo"]] = (sector, mechanisms, layers, row["classificacao"])
        for mechanism in mechanisms:
            for layer in layers:
                matrix.append({
                    "id_estudo": row["id_estudo"],
                    "titulo": row["titulo"],
                    "classificacao": row["classificacao"],
                    "setor_primario": sector,
                    "familia_mecanismo": mechanism,
                    "camada_normalizada": layer,
                    "pagina_evidencia": row["pagina_evidencia"],
                    "trecho_evidencia": row["trecho_evidencia"],
                    "arquivo_pdf": row["arquivo_pdf"],
                    "hash_pdf": row["hash_pdf"],
                    "status_validacao": row["status_validacao"],
                })
    write_csv(OUTPUT_MATRIX, matrix, list(matrix[0]))

    data: list[dict[str, str]] = []
    decision_counts = Counter(row["decisao_final"] for row in decisions)
    graph1 = {
        ("Estudos incluídos", "Estudos"): len(corpus),
        ("Fora do escopo analítico", "Estudos"): decision_counts["excluir_contextual"],
        ("Versão redundante", "Estudos"): decision_counts["excluir_versao_redundante"],
    }
    add_data(data, "grafico_1", ["Estudos incluídos", "Fora do escopo analítico", "Versão redundante"],
             ["Estudos"], graph1, "Registro de decisões do corpus analítico único tratado — v2.1")

    mechanism_counter: Counter[tuple[str, str]] = Counter()
    layer_counter: Counter[tuple[str, str]] = Counter()
    sector_counter: Counter[tuple[str, str]] = Counter()
    finding_counter: Counter[tuple[str, str]] = Counter()
    cooccurrence: Counter[tuple[str, str]] = Counter()
    for _, (sector, mechanisms, layers, classification) in study_codes.items():
        central = classification == "evidencia_central"
        for mechanism in mechanisms:
            mechanism_counter[(mechanism, "Total")] += 1
            if central:
                mechanism_counter[(mechanism, "Evidência central")] += 1
            for layer in layers:
                cooccurrence[(mechanism, layer)] += 1
        for layer in layers:
            layer_counter[(layer, "Evidência central" if central else "Evidência de apoio")] += 1
        sector_counter[(sector, "Total")] += 1
        if central:
            sector_counter[(sector, "Evidência central")] += 1
        mechanism_set = set(mechanisms)
        for finding, required in FINDINGS.items():
            if mechanism_set & required:
                finding_counter[(finding, "Total")] += 1
                if central:
                    finding_counter[(finding, "Evidência central")] += 1

    mech_order = list(MECHANISMS)
    add_data(data, "grafico_2", mech_order, ["Total", "Evidência central"], mechanism_counter,
             "Matriz estudo–mecanismo–camada — v2.1")
    add_data(data, "grafico_3", LAYERS, ["Evidência central", "Evidência de apoio"], layer_counter,
             "Matriz estudo–mecanismo–camada — v2.1")
    sector_order = [name for name, _ in Counter(v[0] for v in study_codes.values()).most_common()]
    add_data(data, "grafico_4", sector_order, ["Total", "Evidência central"], sector_counter,
             "Classificação setorial primária reproduzível — v2.1")
    add_data(data, "grafico_5", list(FINDINGS), ["Total", "Evidência central"], finding_counter,
             "Síntese de achados derivada das famílias de mecanismos — v2.1")
    add_data(data, "grafico_6", mech_order, LAYERS, cooccurrence,
             "Coocorrência por estudo na matriz normalizada — v2.1")
    write_csv(OUTPUT_DATA, data, ["figura", "ordem", "categoria", "serie", "valor", "proveniencia"])

    layer_totals = {layer: layer_counter[(layer, "Evidência central")] + layer_counter[(layer, "Evidência de apoio")]
                    for layer in LAYERS}
    report = [
        "# Reconciliação das contagens do corpus — v2.1", "",
        "Todas as contagens abaixo são recalculadas a partir do corpus analítico único tratado e da matriz longa versionada.", "",
        "## Invariantes", "",
        f"- Estudos incluídos: {len(corpus)}.",
        f"- Evidências centrais: {sum(1 for row in corpus if row['classificacao'] == 'evidencia_central')}.",
        f"- Evidências de apoio: {sum(1 for row in corpus if row['classificacao'] == 'evidencia_apoio')}.",
        f"- Registros documentados na seleção integral: {len(decisions)}.",
        f"- Registros fora do corpus: {len(decisions) - len(corpus)}.", "",
        "## Cobertura por camada", "",
    ]
    report.extend(f"- {layer}: {layer_totals[layer]} estudos." for layer in LAYERS)
    report += ["", "## Contrato de contagem", "",
               "- A unidade é o estudo único.",
               "- Um estudo pode contribuir para mais de um mecanismo, camada ou achado.",
               "- O setor é uma classificação primária mutuamente exclusiva usada apenas no gráfico setorial.",
               "- As frequências caracterizam a síntese; não validam empiricamente o modelo.", ""]
    with open(fs_path(OUTPUT_RECONCILIATION), "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(report))

    print(f"Estudos: {len(corpus)}")
    print(f"Linhas da matriz longa: {len(matrix)}")
    print(f"Dados de figuras: {len(data)}")
    print("Camadas:", ", ".join(f"{key}={value}" for key, value in layer_totals.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
