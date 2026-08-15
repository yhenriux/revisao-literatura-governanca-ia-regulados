# Revisao de Literatura - Governanca Conversacional em LLMs (Ambientes Regulados)

**Agente 1 - Busca Sistematica, Expansao e Consolidacao do Corpus**
**+ Governanca e Correcao do Corpus**
**+ Consolidacao Final em Base Unica**
**+ Agente 2 - Triagem Automatizada de Titulo/Resumo**
**+ Agente 3A - Recuperacao de PDF, Extracao de Texto Completo, Scores NLP e Clusterizacao**

Este diretorio contem toda a rastreabilidade da reconstrucao do processo de busca e
consolidacao do corpus, usando os PDFs previamente reunidos como **corpus-semente**
(nao corpus final). A busca esta **congelada**: nao se adicionam novos registros a
partir daqui. A triagem de titulo/resumo (Agente 2) e a etapa de recuperacao de PDF,
extracao de texto completo, scores de aderencia tematica (NLP) e clusterizacao
(Agente 3A) **ja foram concluidas de forma automatizada** (regras/heuristicas
aplicadas por script, sem julgamento humano) sobre toda a base elegivel de
`corpus_master.csv`. A leitura humana do texto completo, a decisao final de
elegibilidade, a avaliacao de qualidade CASP/JBI, a codificacao tematica
(RQ/CAP/eixo), a sintese dos achados e o fluxograma PRISMA **ainda nao ocorreram**;
nenhuma analise/figura/tabela final do artigo foi gerada nesta etapa.

## Regra de governanca (fixa, vale para todos os agentes futuros)

> Os unicos arquivos de dados ativos deste projeto sao os 4 listados abaixo. E
> **proibido** criar CSVs paralelos, arquivos derivados com sufixos de versao
> (`_corrected`, `_final`, `_v2`, `_v3`, `_revised`, `_new`, `_backup`, `_temp`,
> `_1B`, `_ok`, `_limpo` etc.) ou pastas paralelas de output. Se um arquivo
> canonico estiver errado, incompleto ou obsoleto, ele deve ser **corrigido
> sobrescrevendo o mesmo caminho**, nunca duplicado. PDFs originais nunca sao
> apagados.

## Arquivos de dados ativos (`data/`)

```
data/
├── search_queries.csv      # Fase 2 - strings de busca canonicas e por API (congeladas)
├── raw_records_log.csv     # rastreabilidade bruta PRISMA (1.423 registros, nada excluido)
├── corpus_master.csv       # UNICA base viva da revisao (1.229 candidatos)
└── PIPELINE_STATUS.md      # resumo numerico curto, sempre recalculado a partir dos 3 acima
```

- **`raw_records_log.csv`**: log bruto e imutavel de tudo que foi coletado (PDFs seed,
  busca em API, snowballing), com `source_origin`, `source_api`, `query_id/query_string`,
  `raw_status` (inclui `project_document_previous_manuscript` e `out_of_scope` para os
  PDFs seed) e `notes`. Existe apenas para auditoria/rastreabilidade PRISMA; nao e usado
  para decisoes.
- **`corpus_master.csv`**: **unica base viva** da revisao a partir de agora. Um candidato
  deduplicado por linha (documentos do proprio projeto ja excluidos). Contem as colunas
  de identificacao/prioridade e as colunas de triagem (Agente 2) e de recuperacao/
  extracao/NLP/clustering de texto completo (Agente 3A) ja preenchidas de forma
  automatizada; as colunas de decisao final de elegibilidade, qualidade CASP/JBI,
  codificacao tematica RQ/CAP e status final seguem vazias, para serem preenchidas
  nos proprios Agentes 3B-6 **sem criar nenhum arquivo novo**.
- **`scripts/`**: documenta e reproduz o metodo (um arquivo por fase), mas **nao e fonte
  de dados**. Apos a consolidacao final, os scripts intermediarios (`05_06` a `09`) nao
  sao mais re-executaveis isoladamente porque seus CSVs de entrada/saida intermediarios
  foram removidos (ver secao abaixo). Reproduzir do zero exige rodar toda a cadeia
  `01 -> 03 -> 03b -> 04 -> 05_06 -> 07 -> 08_09 -> 09 -> 11 -> 12 -> 10` numa sessao so.

## O que foi removido nesta consolidacao e por que

Os seguintes CSVs intermediarios existiam apenas para produzir `raw_records_log.csv` e
`corpus_master.csv` e foram removidos por terem funcao duplicada (eram bases concorrentes
do mesmo dado em estagios diferentes do pipeline):

`seed_pdfs_inventory.csv`, `raw_search_results_all_sources.csv`,
`snowballing_raw_results.csv`, `all_candidate_records_raw.csv`,
`deduplicated_candidate_records.csv`, `enriched_candidate_records.csv`,
`pre_screened_candidates.csv`, `candidate_corpus_ready_for_screening.csv`.

Todo o conteudo relevante desses arquivos foi migrado para `raw_records_log.csv`
(rastreabilidade bruta) e `corpus_master.csv` (base de decisao) antes da remocao.

## Correcoes de qualidade de dados aplicadas ate aqui

- Titulo/autores/ano/veiculo dos 80 PDFs seed candidatos foram corrigidos via resolucao
  real de DOI em Crossref (fallback OpenAlex), substituindo heuristicas de posicao de
  texto que capturavam cabecalhos genericos e anos incorretos.
- Os dois manuscritos do proprio artigo (`Artigo1_IJIM_Final`,
  `Artigo1_IJIM_Revisao_PT-BR`) tiveram o DOI espurio removido, ficam registrados em
  `raw_records_log.csv` com `raw_status=project_document_previous_manuscript` para
  rastreabilidade, mas **nao aparecem** em `corpus_master.csv`.
- A deduplicacao aplicou validacao pos-agrupamento: qualquer grupo automatico (por
  titulo identico/fuzzy) com 2+ DOIs distintos foi dividido de volta em candidatos
  separados, corrigindo fusoes falsas entre artigos diferentes com cabecalhos de
  template identicos.

## Numeros-chave (ver `data/PIPELINE_STATUS.md` para o resumo sempre atualizado)

- PDFs seed inventariados: **85** (80 estudos candidatos, 2 documentos do proprio
  projeto, 3 fora de escopo)
- Total bruto em `raw_records_log.csv`: **1.423** (85 seed + 803 API + 535 snowballing)
- Base mestre `corpus_master.csv`: **1.229** candidatos (`ready_for_title_abstract_screening`:
  829 yes, 18 needs_review, 382 no)

## Parecer PRISMA — status metodologico

Objetivo da revisao: analisar como a governanca conversacional e operacionalizada em
sistemas baseados em LLMs implantados em ambientes regulados (saude, financas, governo,
seguros, telecom, juridico), cobrindo mecanismos de accountability, supervisao humana,
auditoria, observabilidade (LLMOps) e conformidade regulatoria. RQs herdadas do artigo
anterior (a formalizar em protocolo proprio antes da sintese final): RQ1 - quais
mecanismos de governanca sao relatados para sistemas conversacionais baseados em LLM em
ambientes regulados; RQ2 - como esses mecanismos endereçam risco, supervisao humana e
accountability; RQ3 - quais lacunas metodologicas/setoriais persistem na literatura.

| # | Passo PRISMA | Status | Observacao |
|---|---|---|---|
| 1 | Definir objetivo | partial | Objetivo acima herdado do artigo anterior; falta protocolo formal registrado |
| 2 | Criar RQs | partial | RQs acima herdadas; ainda nao publicadas como protocolo versionado |
| 3 | Escrever protocolo | partial | Elementos do protocolo estao dispersos neste README, nao consolidados em documento unico |
| 4 | Definir bases | complete | APIs publicas e bases sem acesso documentadas (ver `PIPELINE_STATUS.md`) |
| 5 | Criar strings | complete | `data/search_queries.csv` (5 estrategias, blocos tecnologia/governanca/conversacional/ambiente regulado) |
| 6 | Rodar buscas | complete | 803 registros de API + 535 de snowballing + 85 PDFs seed, todos em `raw_records_log.csv` |
| 7 | Consolidar resultados | complete | `raw_records_log.csv` (1.423) e `corpus_master.csv` (1.229) |
| 8 | Remover duplicatas | complete | Deduplicacao com validacao pos-agrupamento (ver secao de correcoes acima) |
| 9 | Triar titulos e resumos | partial | Regras automatizadas aplicadas a todas as 1.229 linhas de `corpus_master.csv`; parte fica em `needs_full_text`/`needs_metadata_review` pendente de leitura humana ou de texto completo — nao e decisao humana final |
| 10 | Ler textos completos | partial | Agente 3A: recuperacao automatizada de PDF (fontes open access), extracao de texto e scores NLP concluidos para os 803 candidatos-alvo; 408 com texto extraido (344 completos + 64 parciais), 395 sem PDF em acesso aberto. Leitura humana do texto completo ainda nao ocorreu |
| 11 | Aplicar criterios | partial | Criterios I1-I7/E1-E7 ja aplicados no nivel titulo/resumo (Passo 9); Agente 3A gera `fulltext_automated_recommendation` (heuristica NLP, nao decisao) para os 408 candidatos com texto extraido; aplicacao/elegibilidade final humana no texto completo ainda pendente |
| 12 | Avaliar qualidade | not_started | CASP/JBI - colunas existem em `corpus_master.csv`, vazias |
| 13 | Extrair dados | not_started | Colunas de codificacao existem em `corpus_master.csv`, vazias |
| 14 | Sintetizar achados | not_started | - |
| 15 | Gerar fluxograma PRISMA | not_started | Depende dos passos 10-13 estarem concluidos |

## Proximos passos (fora do escopo deste agente)

Ja concluidos de forma automatizada (regras/heuristicas, **nao** julgamento humano):
**Agente 1** (busca/consolidacao), **Agente 2** (triagem titulo/resumo - preencheu
`screening_decision`, `screening_reviewer`, `screening_date`,
`inclusion_criteria_met`, `exclusion_criteria_met`, `exclusion_reason`,
`reviewer_notes` para as 1.229 linhas de `data/corpus_master.csv`) e **Agente 3A**
(recuperacao de PDF, extracao de texto completo, scores NLP de aderencia tematica e
clusterizacao - preencheu as colunas `fulltext_*`, `*_relevance_score`,
`fulltext_automated_recommendation`/`fulltext_automated_reason` e
`cluster_id`/`cluster_label`/`cluster_terms` para os 408 candidatos com texto
extraido).

- **Agente 3B** - Leitura humana do texto completo e decisao final de
  elegibilidade: revisa os 408 candidatos com texto extraido (apoiado pelos
  scores e pela `fulltext_automated_recommendation` ja calculados pelo Agente 3A,
  sem substitui-los) e decide sobre os 395 candidatos-alvo sem PDF em acesso
  aberto; preenche `full_text_decision` e `full_text_exclusion_reason`
  diretamente em `data/corpus_master.csv`.
- **Agente 4** - Avaliacao de Qualidade CASP/JBI: preenche `quality_tool`,
  `quality_score`, `bias_risk`, `evidence_strength`, `quality_notes`.
- **Agente 5** - Codificacao RQ/eixo/CAP: preenche `section4_axis`, `rq_mapping`,
  `cap_mapping`, `sector`, `regulated_context`, `study_type`,
  `mechanisms_identified`, `main_finding`, `limitation`, `future_research`.
- **Agente 6** - Sintese, figuras, tabelas e reescrita do artigo: usa
  `final_status`, `included_in_final_corpus`, `used_in_article`, `used_in_figures`,
  `used_in_tables`, `used_in_references`, `reference_apa`.

Nenhum desses agentes deve criar um CSV novo: todas as colunas ja existem em
`data/corpus_master.csv` e devem ser preenchidas no lugar. O "n" final do artigo
(substituindo "baseline n=62"/"corpus n=101"/"79 PDFs" de versoes anteriores) so
sera definido apos a decisao final de elegibilidade (leitura humana de texto
completo) sobre `data/corpus_master.csv`.
