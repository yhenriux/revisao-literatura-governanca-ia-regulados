# Relatório de qualidade da busca prospectiva de sensibilidade — v2.1

## Conclusão executiva

A execução de 22 de agosto de 2026 é auditável, mas ainda não está completa. Das 40 combinações planejadas, 25 produziram respostas utilizáveis, dez foram bloqueadas por configuração ausente e cinco falharam por limitação de taxa. Portanto, os resultados atuais servem como fila de validação e diagnóstico de cobertura, não como prova de estabilidade do corpus.

Esta execução não reproduz retrospectivamente a busca histórica de julho de 2026. Ela é uma análise prospectiva própria, com corte de publicação em 31 de julho de 2026.

## Cobertura por fonte

| Fonte | Combinações executadas | Bloqueadas ou falhas | Registros retornados | Interpretação |
|---|---:|---:|---:|---|
| OpenAlex | 5 | 0 | 341 | resposta utilizável |
| Crossref | 5 | 0 | 500 | resposta utilizável |
| Europe PMC | 5 | 0 | 500 | resposta utilizável |
| arXiv | 5 | 0 | 1 | resposta utilizável, recuperação muito restrita |
| DOAJ | 5 | 0 | 0 | execução válida sem resultados |
| Semantic Scholar | 0 | 5 | 0 | falha HTTP 429; requer nova tentativa controlada |
| PubMed | 0 | 5 | 0 | bloqueada por ausência de `NCBI_EMAIL` |
| CORE | 0 | 5 | 0 | bloqueada por ausência de `CORE_API_KEY` |

## Reconciliação dos resultados

- Registros retornados, com sobreposições: 1.342.
- Correspondências com o universo histórico: 139 ocorrências.
- Duplicatas dentro da execução: 268 ocorrências.
- Registros únicos não localizados entre os 407 históricos: 992.
- Prioridade automática alta entre os novos únicos: 314.
- Prioridade automática regular entre os novos únicos: 678.
- Registros novos nas posições 1–25: 203.
- Registros novos nas posições 26–50: 250.
- Registros novos nas posições 51–75: 263.
- Registros novos nas posições 76–100: 276.

Nenhum dos 992 registros é considerado elegível antes da decisão humana. A concentração de candidatos após a posição 25 impede concluir, neste momento, que o truncamento histórico foi inócuo; essa inferência só será possível após a triagem humana.

## Controles de qualidade aplicados

- corte temporal aplicado antes da inclusão na fila;
- deduplicação primária por DOI e subsidiária por título normalizado;
- comparação com todo o universo histórico de 407 registros, incluindo excluídos e contextuais;
- preservação de fonte, família, consulta, posição, faixa, horário, URL sem credencial, hash e resposta bruta;
- separação entre prioridade automática e decisão humana;
- ausência de inclusão automática no corpus.

## Pendências necessárias

1. configurar `NCBI_EMAIL` e, quando disponível, `NCBI_API_KEY`;
2. configurar `CORE_API_KEY`;
3. configurar `SEMANTIC_SCHOLAR_API_KEY` ou executar exportação manual documentada;
4. repetir somente as combinações bloqueadas ou falhas;
5. Yago triar todos os registros únicos pendentes;
6. estender em blocos de 100 qualquer combinação com estudo elegível exclusivo nas posições 76–100;
7. reconciliar os estudos elegíveis com o corpus, PRISMA, tabelas, gráficos e conclusões.

## Limitação de interpretação

Os mecanismos de ranking das fontes podem privilegiar relevância, recência, citação ou popularidade. A sensibilidade por posição mede a consequência operacional desse ranking na execução documentada, mas não demonstra exaustividade da literatura.
