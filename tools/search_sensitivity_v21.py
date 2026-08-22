"""Executa a busca prospectiva de sensibilidade da v2.1.

O programa não reconstrói a busca histórica. Ele registra uma execução nova,
datada, com corte de publicação em 2026-07-31, posições, respostas e hashes.
As decisões de elegibilidade permanecem obrigatoriamente humanas.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable


ROOT = Path(os.environ.get("REV_LIT_ROOT") or Path(__file__).resolve().parents[1])
OUT = ROOT / "Documentacao_do_projeto" / "v2.1" / "busca_de_sensibilidade"
RAW = OUT / "respostas_brutas"
CUTOFF = "2026-07-31"


FAMILIES = {
    "A_governanca_de_llms": (
        '("large language model" OR LLM OR "generative AI") AND '
        '(governance OR accountability OR compliance OR audit OR risk)'
    ),
    "B_llmops_e_observabilidade": (
        '(LLMOps OR "LLM observability" OR "large language model monitoring" OR guardrails) AND '
        '(governance OR compliance OR audit)'
    ),
    "C_governanca_conversacional": (
        '("conversational AI" OR chatbot OR "AI agent" OR "conversational agent") AND '
        '("large language model" OR LLM OR "generative AI") AND '
        '(governance OR oversight OR accountability)'
    ),
    "D_ambientes_regulados": (
        '("large language model" OR LLM OR "generative AI") AND '
        '(regulated OR healthcare OR finance OR government OR legal OR insurance) AND '
        '(risk OR audit OR compliance OR governance)'
    ),
    "E_supervisao_e_contestabilidade": (
        '("large language model" OR LLM OR chatbot) AND '
        '("human oversight" OR "human-in-the-loop" OR contestability OR redress OR appeal OR escalation OR handoff)'
    ),
}


PLAIN_QUERIES = {
    "A_governanca_de_llms": "large language model generative AI governance accountability compliance audit risk",
    "B_llmops_e_observabilidade": "LLMOps observability monitoring guardrails governance compliance audit",
    "C_governanca_conversacional": "conversational AI chatbot AI agent large language model governance oversight accountability",
    "D_ambientes_regulados": "large language model generative AI regulated healthcare finance government legal insurance risk compliance governance",
    "E_supervisao_e_contestabilidade": "large language model chatbot human oversight human in the loop contestability redress appeal escalation handoff",
}


SOURCES = ("OpenAlex", "Crossref", "Semantic Scholar", "PubMed", "Europe PMC", "CORE", "arXiv", "DOAJ")


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_doi(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text)
    text = re.sub(r"^doi:\s*", "", text)
    return text.rstrip(" .")


def normalize_title(value: Any) -> str:
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def rank_band(rank: int) -> str:
    if rank <= 25:
        return "1-25"
    if rank <= 50:
        return "26-50"
    if rank <= 75:
        return "51-75"
    if rank <= 100:
        return "76-100"
    start = ((rank - 1) // 100) * 100 + 1
    return f"{start}-{start + 99}"


def request_bytes(url: str, *, headers: dict[str, str] | None = None, timeout: int = 60) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "GovernancaConversacionalReview/2.1 (systematic-review-sensitivity)",
            "Accept": "application/json, application/xml, text/xml, application/atom+xml",
            **(headers or {}),
        },
    )
    last: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last = exc
            if isinstance(exc, urllib.error.HTTPError) and exc.code not in (429, 500, 502, 503, 504):
                raise
            time.sleep(2 ** attempt)
    assert last is not None
    raise last


def decode_abstract(inverted: Any) -> str:
    if not isinstance(inverted, dict):
        return ""
    pairs: list[tuple[int, str]] = []
    for token, positions in inverted.items():
        for position in positions or []:
            pairs.append((int(position), token))
    return " ".join(token for _, token in sorted(pairs))


def common_record(source: str, family: str, query: str, rank: int, raw_hash: str, **fields: Any) -> dict[str, Any]:
    return {
        "fonte": source,
        "familia": family,
        "consulta_canonica": FAMILIES[family],
        "consulta_adaptada": query,
        "posicao": rank,
        "faixa_posicao": rank_band(rank),
        "titulo": fields.get("title") or "",
        "autores": fields.get("authors") or "",
        "ano": fields.get("year") or "",
        "doi": normalize_doi(fields.get("doi")),
        "url": fields.get("url") or "",
        "resumo": fields.get("abstract") or "",
        "identificador_fonte": fields.get("source_id") or "",
        "data_recuperacao_utc": now_utc(),
        "hash_resposta_bruta": raw_hash,
    }


def fetch_openalex(family: str, limit: int) -> tuple[bytes, list[dict[str, Any]], str, int | None]:
    query = PLAIN_QUERIES[family]
    params = {
        "search": query,
        "filter": f"to_publication_date:{CUTOFF}",
        "per-page": min(limit, 100),
        "page": 1,
        "select": "id,doi,title,publication_year,authorships,primary_location,abstract_inverted_index",
    }
    if os.environ.get("OPENALEX_API_KEY"):
        params["api_key"] = os.environ["OPENALEX_API_KEY"]
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = request_bytes(url)
    payload = json.loads(data)
    records = []
    for rank, item in enumerate(payload.get("results", []), 1):
        authors = "; ".join(a.get("author", {}).get("display_name", "") for a in item.get("authorships", []))
        location = item.get("primary_location") or {}
        records.append(common_record("OpenAlex", family, query, rank, sha256(data), title=item.get("title"), authors=authors, year=item.get("publication_year"), doi=item.get("doi"), url=location.get("landing_page_url") or item.get("id"), abstract=decode_abstract(item.get("abstract_inverted_index")), source_id=item.get("id")))
    return data, records, url, (payload.get("meta") or {}).get("count")


def fetch_crossref(family: str, limit: int) -> tuple[bytes, list[dict[str, Any]], str, int | None]:
    query = PLAIN_QUERIES[family]
    params = {"query.bibliographic": query, "filter": f"until-pub-date:{CUTOFF}", "rows": min(limit, 100), "select": "DOI,title,author,published,container-title,URL,abstract"}
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = request_bytes(url)
    payload = json.loads(data).get("message", {})
    records = []
    for rank, item in enumerate(payload.get("items", []), 1):
        authors = "; ".join(" ".join(x for x in (a.get("given"), a.get("family")) if x) for a in item.get("author", []))
        parts = ((item.get("published") or {}).get("date-parts") or [[""]])[0]
        records.append(common_record("Crossref", family, query, rank, sha256(data), title=" ".join(item.get("title") or []), authors=authors, year=parts[0] if parts else "", doi=item.get("DOI"), url=item.get("URL"), abstract=re.sub("<[^>]+>", " ", item.get("abstract") or ""), source_id=item.get("DOI")))
    return data, records, url, payload.get("total-results")


def fetch_semantic_scholar(family: str, limit: int) -> tuple[bytes, list[dict[str, Any]], str, int | None]:
    query = PLAIN_QUERIES[family]
    params = {"query": query, "limit": min(limit, 100), "offset": 0, "fields": "paperId,title,authors,year,abstract,url,externalIds"}
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    headers = {}
    if os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
        headers["x-api-key"] = os.environ["SEMANTIC_SCHOLAR_API_KEY"]
    data = request_bytes(url, headers=headers)
    payload = json.loads(data)
    records = []
    for rank, item in enumerate(payload.get("data", []), 1):
        authors = "; ".join(a.get("name", "") for a in item.get("authors", []))
        external = item.get("externalIds") or {}
        records.append(common_record("Semantic Scholar", family, query, rank, sha256(data), title=item.get("title"), authors=authors, year=item.get("year"), doi=external.get("DOI"), url=item.get("url"), abstract=item.get("abstract"), source_id=item.get("paperId")))
    return data, records, url, payload.get("total")


def fetch_pubmed(family: str, limit: int) -> tuple[bytes, list[dict[str, Any]], str, int | None]:
    email = os.environ.get("NCBI_EMAIL", "").strip()
    if not email:
        raise RuntimeError("NCBI_EMAIL ausente")
    query = f"({FAMILIES[family]}) AND (1900/01/01:{CUTOFF.replace('-', '/')}[pdat])"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": min(limit, 100), "retstart": 0, "sort": "relevance", "tool": "GovernancaConversacionalReview", "email": email}
    if os.environ.get("NCBI_API_KEY"):
        params["api_key"] = os.environ["NCBI_API_KEY"]
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = request_bytes(url)
    search = json.loads(search_data).get("esearchresult", {})
    ids = search.get("idlist", [])
    if not ids:
        return search_data, [], url, int(search.get("count", 0))
    summary_params = {"db": "pubmed", "id": ",".join(ids), "retmode": "json", "version": "2.0", "tool": "GovernancaConversacionalReview", "email": email}
    if os.environ.get("NCBI_API_KEY"):
        summary_params["api_key"] = os.environ["NCBI_API_KEY"]
    summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summary_params)
    summary_data = request_bytes(summary_url)
    payload = json.loads(summary_data).get("result", {})
    combined = search_data + b"\n" + summary_data
    records = []
    for rank, pmid in enumerate(ids, 1):
        item = payload.get(pmid, {})
        article_ids = {x.get("idtype"): x.get("value") for x in item.get("articleids", [])}
        authors = "; ".join(a.get("name", "") for a in item.get("authors", []))
        year_match = re.search(r"\b(19|20)\d{2}\b", item.get("pubdate", ""))
        records.append(common_record("PubMed", family, query, rank, sha256(combined), title=item.get("title"), authors=authors, year=year_match.group(0) if year_match else "", doi=article_ids.get("doi"), url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", abstract="", source_id=pmid))
    return combined, records, summary_url, int(search.get("count", 0))


def fetch_europe_pmc(family: str, limit: int) -> tuple[bytes, list[dict[str, Any]], str, int | None]:
    query = f"({FAMILIES[family]}) AND FIRST_PDATE:[1900-01-01 TO {CUTOFF}]"
    params = {"query": query, "format": "json", "pageSize": min(limit, 100), "resultType": "core"}
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(params)
    data = request_bytes(url)
    payload = json.loads(data)
    records = []
    for rank, item in enumerate((payload.get("resultList") or {}).get("result", []), 1):
        records.append(common_record("Europe PMC", family, query, rank, sha256(data), title=item.get("title"), authors=item.get("authorString"), year=item.get("pubYear"), doi=item.get("doi"), url=f"https://europepmc.org/article/{item.get('source', '')}/{item.get('id', '')}", abstract=item.get("abstractText"), source_id=item.get("id")))
    return data, records, url, payload.get("hitCount")


def fetch_core(family: str, limit: int) -> tuple[bytes, list[dict[str, Any]], str, int | None]:
    key = os.environ.get("CORE_API_KEY", "").strip()
    if not key:
        raise RuntimeError("CORE_API_KEY ausente")
    query = PLAIN_QUERIES[family]
    params = {"q": query, "limit": min(limit, 100), "offset": 0}
    url = "https://api.core.ac.uk/v3/search/works?" + urllib.parse.urlencode(params)
    data = request_bytes(url, headers={"Authorization": f"Bearer {key}"})
    payload = json.loads(data)
    records = []
    for rank, item in enumerate(payload.get("results", []), 1):
        records.append(common_record("CORE", family, query, rank, sha256(data), title=item.get("title"), authors="; ".join(item.get("authors") or []), year=item.get("yearPublished"), doi=item.get("doi"), url=item.get("downloadUrl") or item.get("sourceFulltextUrls", [""])[0] if item.get("sourceFulltextUrls") else "", abstract=item.get("abstract"), source_id=item.get("id")))
    return data, records, url, payload.get("totalHits")


def fetch_arxiv(family: str, limit: int) -> tuple[bytes, list[dict[str, Any]], str, int | None]:
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z-]+", PLAIN_QUERIES[family]) if len(w) > 2][:12]
    query = " AND ".join(f'all:"{word}"' if "-" in word else f"all:{word}" for word in words)
    params = {"search_query": query, "start": 0, "max_results": min(limit, 100), "sortBy": "relevance", "sortOrder": "descending"}
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    data = request_bytes(url)
    root = ET.fromstring(data)
    ns = {"a": "http://www.w3.org/2005/Atom", "op": "http://a9.com/-/spec/opensearch/1.1/"}
    total_node = root.find("op:totalResults", ns)
    records = []
    accepted_rank = 0
    for entry in root.findall("a:entry", ns):
        published = entry.findtext("a:published", default="", namespaces=ns)
        if published[:10] > CUTOFF:
            continue
        accepted_rank += 1
        authors = "; ".join(a.findtext("a:name", default="", namespaces=ns) for a in entry.findall("a:author", ns))
        source_id = entry.findtext("a:id", default="", namespaces=ns)
        doi = entry.findtext("{http://arxiv.org/schemas/atom}doi", default="")
        records.append(common_record("arXiv", family, query, accepted_rank, sha256(data), title=" ".join(entry.findtext("a:title", default="", namespaces=ns).split()), authors=authors, year=published[:4], doi=doi, url=source_id, abstract=" ".join(entry.findtext("a:summary", default="", namespaces=ns).split()), source_id=source_id.rsplit("/", 1)[-1]))
    return data, records, url, int(total_node.text) if total_node is not None and total_node.text else None


def fetch_doaj(family: str, limit: int) -> tuple[bytes, list[dict[str, Any]], str, int | None]:
    query = PLAIN_QUERIES[family]
    encoded = urllib.parse.quote(query, safe="")
    url = f"https://doaj.org/api/search/articles/{encoded}?page=1&pageSize={min(limit, 100)}"
    data = request_bytes(url)
    payload = json.loads(data)
    records = []
    for rank, item in enumerate(payload.get("results", []), 1):
        bib = item.get("bibjson") or {}
        identifiers = {x.get("type"): x.get("id") for x in bib.get("identifier", [])}
        links = bib.get("link") or []
        records.append(common_record("DOAJ", family, query, rank, sha256(data), title=bib.get("title"), authors="; ".join(a.get("name", "") for a in bib.get("author", [])), year=bib.get("year"), doi=identifiers.get("doi"), url=links[0].get("url") if links else "", abstract=bib.get("abstract"), source_id=item.get("id")))
    return data, records, url, payload.get("total")


FETCHERS: dict[str, Callable[[str, int], tuple[bytes, list[dict[str, Any]], str, int | None]]] = {
    "OpenAlex": fetch_openalex,
    "Crossref": fetch_crossref,
    "Semantic Scholar": fetch_semantic_scholar,
    "PubMed": fetch_pubmed,
    "Europe PMC": fetch_europe_pmc,
    "CORE": fetch_core,
    "arXiv": fetch_arxiv,
    "DOAJ": fetch_doaj,
}


def historical_keys() -> tuple[set[str], set[str]]:
    inventory_path = ROOT / "Documentacao_do_projeto" / "methodology" / "CORPUS_ANALYTIC_177_INVENTORY.csv"
    universe_path = ROOT / "Documentacao_do_projeto" / "methodology" / "CORPUS_UNIVERSE_RECONCILIATION.csv"
    checkpoint_path = ROOT / "arquivos_tratados_aigovernanca" / "metagrade_llm_output" / "checkpoint_results.jsonl"
    dois: set[str] = set()
    titles: set[str] = set()

    checkpoint: dict[str, dict[str, Any]] = {}
    with checkpoint_path.open(encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            row = json.loads(line)
            identifier = Path(str(row.get("raw_file_name", ""))).stem
            if identifier:
                checkpoint[identifier] = row

    # O universo histórico de comparação é o conjunto de 407 registros, não apenas
    # os 177 incluídos. Isso impede que registros já excluídos ou contextuais sejam
    # artificialmente apresentados como novas recuperações.
    with universe_path.open(encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            if row.get("integra_universo_407") != "sim":
                continue
            title = normalize_title(row.get("titulo"))
            if title:
                titles.add(title)
            cp = checkpoint.get(str(row.get("identificador", "")), {})
            for field in ("llm_doi", "py_doi"):
                doi = normalize_doi(cp.get(field))
                if doi.startswith("10."):
                    dois.add(doi)

    # Mantém o inventário analítico como salvaguarda para metadados corrigidos que
    # possam não estar completos no checkpoint histórico.
    with inventory_path.open(encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            doi = normalize_doi(row.get("doi_ou_url"))
            title = normalize_title(row.get("titulo"))
            if doi.startswith("10."):
                dois.add(doi)
            if title:
                titles.add(title)
    return dois, titles


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--sources", nargs="*", choices=SOURCES, default=list(SOURCES))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    load_env(ROOT / ".env.v2.1.local")
    OUT.mkdir(parents=True, exist_ok=True)
    RAW.mkdir(parents=True, exist_ok=True)

    registry = []
    for source in SOURCES:
        for family, query in FAMILIES.items():
            registry.append({"fonte": source, "familia": family, "consulta_canonica": query, "consulta_operacional": PLAIN_QUERIES[family], "corte_publicacao": CUTOFF, "limite_inicial": args.limit, "estado": "planejada", "resultados_recuperados": "", "total_reportado": "", "inicio_utc": "", "fim_utc": "", "hash_resposta": "", "erro_ou_limitacao": ""})
    write_csv(OUT / "Registro_das_40_consultas_v2.1.csv", registry, list(registry[0]))
    if args.dry_run:
        print(json.dumps({"consultas": len(registry), "arquivo": str(OUT / 'Registro_das_40_consultas_v2.1.csv')}, ensure_ascii=False))
        return

    all_records: list[dict[str, Any]] = []
    execution: list[dict[str, Any]] = []
    for source in args.sources:
        for family in FAMILIES:
            started = now_utc()
            status = "executada"
            error = ""
            count = None
            records: list[dict[str, Any]] = []
            url = ""
            raw_hash = ""
            try:
                data, records, url, count = FETCHERS[source](family, args.limit)
                raw_hash = sha256(data)
                (RAW / f"{source.replace(' ', '_')}_{family}.bin").write_bytes(data)
                all_records.extend(records)
            except Exception as exc:  # a falha é dado metodológico e deve permanecer no log
                status = "bloqueada" if "ausente" in str(exc).lower() else "falhou"
                error = f"{type(exc).__name__}: {exc}"
            execution.append({"fonte": source, "familia": family, "inicio_utc": started, "fim_utc": now_utc(), "estado": status, "total_reportado": count if count is not None else "não informado", "resultados_recuperados": len(records), "limite_solicitado": args.limit, "url_sem_credenciais": re.sub(r"([?&](?:api_key|key)=)[^&]+", r"\1REDACTED", url), "hash_resposta": raw_hash, "erro_ou_limitacao": error})
            time.sleep(0.4)

    execution_by_query = {(row["fonte"], row["familia"]): row for row in execution}
    for row in registry:
        executed = execution_by_query[(row["fonte"], row["familia"])]
        for field in ("estado", "resultados_recuperados", "total_reportado", "inicio_utc", "fim_utc", "hash_resposta", "erro_ou_limitacao"):
            row[field] = executed[field]
    write_csv(OUT / "Registro_das_40_consultas_v2.1.csv", registry, list(registry[0]))

    historical_dois, historical_titles = historical_keys()
    seen: dict[str, str] = {}
    queue: list[dict[str, Any]] = []
    for item in all_records:
        doi = normalize_doi(item.get("doi"))
        title_key = normalize_title(item.get("titulo"))
        key = f"doi:{doi}" if doi.startswith("10.") else f"title:{title_key}"
        duplicate_of = seen.get(key, "")
        if not duplicate_of:
            seen[key] = f"{item['fonte']}:{item['familia']}:{item['posicao']}"
        historical = doi in historical_dois if doi.startswith("10.") else title_key in historical_titles
        text = normalize_title(f"{item.get('titulo', '')} {item.get('resumo', '')}")
        has_tech = any(x in text for x in ("large language model", " llm ", "generative ai", "chatbot", "conversational ai", "ai agent"))
        has_gov = any(x in text for x in ("govern", "accountab", "compliance", "audit", "risk", "oversight", "guardrail", "contest", "redress"))
        item.update({"chave_deduplicacao": key, "duplicata_nesta_execucao_de": duplicate_of, "presente_no_corpus_historico": "sim" if historical else "não", "prioridade_triagem_automatica": "alta" if has_tech and has_gov else "regular", "decisao_humana": "", "justificativa_humana": "", "status_validacao_humana": "pendente" if not historical and not duplicate_of else "não_aplicável"})
        queue.append(item)

    record_fields = ["fonte", "familia", "consulta_canonica", "consulta_adaptada", "posicao", "faixa_posicao", "titulo", "autores", "ano", "doi", "url", "resumo", "identificador_fonte", "data_recuperacao_utc", "hash_resposta_bruta", "chave_deduplicacao", "duplicata_nesta_execucao_de", "presente_no_corpus_historico", "prioridade_triagem_automatica", "decisao_humana", "justificativa_humana", "status_validacao_humana"]
    write_csv(OUT / "Resultados_recuperados_v2.1.csv", queue, record_fields)
    write_csv(OUT / "Log_de_execucao_das_consultas_v2.1.csv", execution, list(execution[0]))

    summary: dict[tuple[str, str], int] = {}
    for item in queue:
        summary[(item["fonte"], item["faixa_posicao"])] = summary.get((item["fonte"], item["faixa_posicao"]), 0) + 1
    report = ["# Relatório provisório da busca de sensibilidade v2.1", "", f"Execução: {now_utc()}", f"Corte de publicação: {CUTOFF}", "", "## Estado das fontes", "", "| Fonte | Consultas executadas | Consultas bloqueadas/falhas | Resultados |", "|---|---:|---:|---:|"]
    for source in args.sources:
        runs = [x for x in execution if x["fonte"] == source]
        report.append(f"| {source} | {sum(x['estado'] == 'executada' for x in runs)} | {sum(x['estado'] != 'executada' for x in runs)} | {sum(int(x['resultados_recuperados']) for x in runs)} |")
    unique_new = {x["chave_deduplicacao"] for x in queue if x["presente_no_corpus_historico"] == "não" and not x["duplicata_nesta_execucao_de"]}
    report += ["", "## Reconciliação preliminar", "", f"- Registros retornados, incluindo sobreposições: {len(queue)}", f"- Registros únicos não encontrados no corpus histórico: {len(unique_new)}", "- Nenhum registro novo é elegível até receber decisão humana de Yago.", "- Este relatório não reproduz a execução histórica de julho de 2026."]
    (OUT / "RELATORIO_PROVISORIO_DA_BUSCA_V2.1.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({"execucoes": len(execution), "resultados": len(queue), "novos_unicos": len(unique_new), "saida": str(OUT)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
