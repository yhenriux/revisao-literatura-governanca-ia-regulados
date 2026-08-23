# Relatório final de qualidade da recuperação ampliada — v2.1

## Conclusão executiva

A execução de 22 de agosto de 2026 é auditável e sustenta a estratégia final relatada no artigo. Cinco fontes produziram respostas utilizáveis em 25 combinações. Os resultados foram examinados por faixas sucessivas até a centésima posição, deduplicados e submetidos à triagem e à avaliação de texto integral quando elegíveis.

O corte de publicação foi 31 de julho de 2026. Fontes sem execução utilizável permanecem no log técnico para demonstrar a tentativa, mas não são apresentadas como fontes efetivas do estudo.

## Cobertura por fonte

| Fonte | Combinações executadas | Bloqueadas ou falhas | Registros retornados | Interpretação |
|---|---:|---:|---:|---|
| OpenAlex | 5 | 0 | 341 | resposta utilizável |
| Crossref | 5 | 0 | 500 | resposta utilizável |
| Europe PMC | 5 | 0 | 500 | resposta utilizável |
| arXiv | 5 | 0 | 1 | resposta utilizável, recuperação muito restrita |
| DOAJ | 5 | 0 | 0 | execução válida sem resultados |
| Semantic Scholar | 0 | 5 | 0 | tentativa preservada no log; não integra a busca efetiva |
| PubMed | 0 | 5 | 0 | tentativa preservada no log; não integra a busca efetiva |
| CORE | 0 | 5 | 0 | tentativa preservada no log; não integra a busca efetiva |

## Reconciliação dos resultados

- Registros retornados, com sobreposições: 1.342.
- Sobreposições com registros já identificados no projeto: 139 ocorrências.
- Duplicatas dentro da execução: 268 ocorrências.
- Registros adicionais únicos submetidos à triagem assistida: 992.
- Prioridade automática alta: 314; prioridade regular: 678.
- Registros adicionais ocorreram em todas as faixas examinadas, inclusive nas posições posteriores.

A distribuição posicional confirmou que a recuperação não deveria depender apenas dos primeiros resultados. Por isso, o procedimento final do artigo relata a exploração até a centésima posição e a seleção consolidada, sem manter um truncamento inicial como regra do corpus.

## Controles de qualidade aplicados

- corte temporal aplicado antes da inclusão na fila;
- deduplicação primária por DOI e subsidiária por título normalizado;
- comparação com os registros já identificados no projeto;
- preservação de fonte, família, consulta, posição, faixa, horário, URL sem credencial, hash e resposta bruta;
- separação entre prioridade automática e decisão humana;
- ausência de inclusão automática no corpus.

## Fechamento da seleção

- Registros com texto integral e decisão documentada: 383.
- Estudos únicos incluídos: 358.
- Evidências centrais: 30.
- Evidências de apoio: 328.
- Registros fora do escopo analítico: 24.
- Versões redundantes vinculadas à publicação final: uma.

As decisões estão reconciliadas no registro do corpus e as contagens publicadas são derivadas da matriz longa estudo–mecanismo–camada.

## Limitação de interpretação

Os mecanismos de ranking das fontes podem privilegiar relevância, recência, citação ou popularidade. A análise por posição reduz a dependência dos primeiros resultados, mas não demonstra exaustividade de toda a literatura. O resultado deve ser interpretado como uma síntese sistemática de um corpus documentado e reproduzível.
