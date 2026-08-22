# Relatório de qualidade da triagem assistida — v2.1

## Unidade e finalidade

A unidade é o registro bibliográfico único não localizado automaticamente entre os 407 registros históricos. A finalidade desta etapa é priorizar título/resumo e identificar quais registros exigem texto completo; não é substituir a decisão científica final do autor.

## Resultado do segundo passe

| Classe | Registros | Interpretação |
|---|---:|---|
| Candidata a evidência central | 56 | C1, C2 e C3 presentes por título/resumo; exige texto completo |
| Candidata a evidência de apoio | 182 | pertinente, mas sem confirmação de todos os critérios centrais; exige texto completo |
| Incerta | 337 | metadados insuficientes ou aderência ambígua; exige texto completo antes de excluir |
| Referência contextual | 35 | útil para enquadramento, fora das frequências do corpus |
| Duplicata histórica provável | 9 | semelhança de título ≥ 0,94 com registro histórico |
| Duplicata na nova execução | 35 | mesmo título recuperado com fonte ou identificador distinto |
| Exclusão por título/resumo | 338 | não demonstra simultaneamente objeto tecnológico e mecanismo de governança |
| **Total** | **992** |  |

## Verificações de qualidade

- completude: 300 registros brutos não tinham resumo, mas nenhum foi incluído automaticamente por essa ausência;
- unicidade: além da deduplicação por DOI, 35 duplicatas adicionais foram identificadas por título normalizado;
- integridade histórica: nove registros exigem reconciliação com o universo anterior por semelhança aproximada;
- validade: as classificações usam campos explícitos C1, C2 e C3 e preservam termos acionadores e justificativa;
- rastreabilidade: fonte, consulta, posição, DOI, URL, título, resumo e decisão assistida permanecem na mesma linha;
- temporalidade: o arquivo derivado preserva o ano, mas não a data exata de publicação, impedindo separar com segurança publicações posteriores à execução histórica ocorridas ainda em julho de 2026.

## Riscos analíticos

### Alto — texto completo ainda necessário

575 registros permanecem nas classes central, apoio ou incerta. Incorporá-los diretamente alteraria o corpus com base apenas em título/resumo e quebraria a equivalência com o protocolo histórico de avaliação em texto completo.

### Alto — sensibilidade não isolada ao truncamento

A busca prospectiva ocorreu depois da busca histórica. Sem data exata por registro, parte da diferença pode refletir publicações novas dentro do corte de julho, além do efeito das posições 26–100.

### Médio — precisão da classificação automática

Termos como segurança, privacidade, ética e risco aparecem em estudos de aplicação que não têm governança como objeto principal. Por isso, as classes são candidaturas, não inclusões definitivas.

### Médio — heterogeneidade de fontes

Crossref, Europe PMC, OpenAlex e arXiv possuem coberturas e metadados diferentes. PubMed, CORE e Semantic Scholar foram retirados desta análise prospectiva por decisão do autor após falha operacional; essa delimitação deve aparecer no suplemento.

## Critério operacional refinado

- **Evidência central:** estudo diretamente dedicado a governança, supervisão, risco, accountability ou operação controlada de LLM/sistema conversacional; relação explícita com ambiente regulado, de alto impacto ou mecanismo transferível; e contribuição substantiva para ao menos uma pergunta da revisão.
- **Evidência de apoio:** estudo elegível que informa riscos, controles, avaliação, interação ou contexto setorial, mas trata a governança de forma secundária, parcial ou transferível.
- **Referência contextual:** material útil ao enquadramento teórico, normativo ou metodológico, sem participação nas frequências do corpus.
- **Exclusão:** registro que não satisfaz a elegibilidade após a etapa apropriada de avaliação.

## Decisão de uso

Os 56 e 182 registros não devem ser somados ao corpus antes da verificação de texto completo. Os 337 incertos também não devem ser excluídos automaticamente. O arquivo de triagem é adequado para priorização e auditoria, mas ainda não sustenta novos números de PRISMA ou gráficos.
