# Suplemento metodológico da v2

## Abrangência da recuperação

A busca utilizou OpenAlex, Crossref, Semantic Scholar, PubMed, Europe PMC, CORE, arXiv e DOAJ, com cinco famílias conceituais: governança de LLMs, LLMOps e observabilidade, governança conversacional, ambientes regulados e supervisão humana/contestabilidade. As consultas foram executadas em julho de 2026.

O limite de até 25 resultados por combinação entre estratégia e fonte foi uma decisão operacional de auditabilidade: com oito fontes e cinco famílias, permitiu registrar, deduplicar, obter texto completo e validar individualmente um conjunto heterogêneo sem tratar a ordenação das APIs como amostragem probabilística. O limite reduz redundância e viabiliza conferência, mas pode truncar consultas produtivas e não demonstra exaustividade.

| Fonte | Cobertura operacional preservada | Limitação conhecida | Compensação aplicada |
|---|---|---|---|
| OpenAlex | consultas executadas | ordenação e limite por combinação | deduplicação e expansão bibliográfica |
| Crossref | consultas executadas | metadados e ordenação variáveis | validação por DOI, título e texto completo |
| Semantic Scholar | parcial | restrições de taxa | snowballing por citações, referências, autoria e veículo |
| PubMed | consultas executadas | concentração biomédica | triangulação com fontes multidisciplinares |
| Europe PMC | consultas executadas | sobreposição com PubMed | deduplicação por DOI, título e similaridade |
| CORE | consultas executadas | heterogeneidade de repositórios | validação de texto completo e metadados |
| arXiv | parcial | falhas de tempo de resposta | recuperação por fontes alternativas e snowballing |
| DOAJ | consultas executadas | cobertura apenas de acesso aberto | triangulação com as demais fontes |

Os logs preservados não permitem atribuir retrospectivamente, estudo a estudo, a fonte e a família de consulta que originaram cada registro. Por isso, nenhuma proveniência individual foi inferida. APIs e mecanismos de ordenação podem favorecer relevância, recência ou popularidade. O snowballing por referências, citações, trabalhos relacionados, autoria e veículo reduz, mas não elimina, o risco de perda. A revisão deve ser interpretada como síntese sistemática de um corpus documentado, não como enumeração exaustiva de toda a literatura existente.

O arquivo `SEARCH_COVERAGE_AUDIT_V2.csv` explicita as 40 combinações entre oito fontes e cinco famílias de consulta. Os campos de total reportado pela API, resultados retornados, armazenados, deduplicados, obtidos em texto completo e incorporados ao corpus estão marcados como `não preservado` ou `não atribuível` quando os logs históricos não os sustentam. Essa ausência impede uma análise quantitativa retrospectiva do efeito do limite de 25; ela não foi preenchida por estimativa nem por nova busca apresentada como reprodução histórica.

## Critérios operacionais completos

| Código | Tipo | Formulação operacional |
|---|---|---|
| I1 | Inclusão | Estudo sobre LLMs, IA generativa ou sistemas conversacionais. |
| I2 | Inclusão | Presença de mecanismo técnico, interacional, organizacional, regulatório ou evolutivo de governança. |
| I3 | Inclusão | Aplicação ou implicação relevante para ambiente regulado ou de alto impacto. |
| I4 | Inclusão | Texto completo suficiente para avaliação. |
| I5 | Inclusão | Publicação entre 2020 e 2026. |
| I6 | Inclusão | Estudo empírico, técnico, conceitual, normativo ou revisão aderente ao objeto. |
| I7 | Inclusão | Referência anterior a 2020 com função fundacional, teórica ou metodológica. |
| E1 | Exclusão | Ausência de LLM, IA generativa ou sistema conversacional como objeto substantivo. |
| E2 | Exclusão | Ausência de mecanismo técnico, interacional, organizacional, regulatório ou evolutivo de governança. |
| E3 | Exclusão | Ausência de aplicação, implicação ou transferibilidade para ambiente regulado ou de alto impacto. |
| E4 | Exclusão | Texto completo insuficiente para responder às questões da revisão. |
| E5 | Exclusão | Publicação anterior a 2020 sem função fundacional, teórica ou metodológica. |
| E6 | Exclusão | Registro duplicado, manuscrito interno ou versão redundante de estudo já representado. |
| E7 | Exclusão | Metadados insuficientes ou conteúdo sem evidência substantiva para classificação. |

No corpo do artigo, a Tabela 3 consolida esses critérios em quatro grupos de inclusão e quatro de exclusão. Casos de fronteira exigem decisão registrada, evidência literal e justificativa; a readjudicação dos 17 casos da v2 está em `CORPUS_BORDERLINE_ADJUDICATION_V2.csv`.

## Adjudicação assistida por LLM

A triagem determinística registrou termos, páginas e evidências literais. A adjudicação assistida recebeu metadados e trechos selecionados, produziu saída estruturada em JSON e foi instruída a não inferir informação ausente. O LLM foi um instrumento auxiliar, não um avaliador autônomo.

| Etapa | Controle aplicado | Risco residual |
|---|---|---|
| Triagem determinística | termos, regras e evidências literais | falsos positivos ou negativos por vocabulário |
| Adjudicação assistida | JSON estruturado e prompt restritivo | interpretação contextual, enquadramento e alucinação |
| Validação | confronto de citações com o texto extraído | falha de extração, hifenização ou localização |
| Readjudicação documentada | critérios explícitos, justificativa e evidência por caso de fronteira | ausência de segundo revisor humano independente |
| Síntese | distinção entre central, apoio, contextual e exclusão | dependência das decisões anteriores |

Não houve dupla revisão humana independente. A confiança numérica do LLM não é probabilidade calibrada. Persistem dependências de versão, prompt, configuração e disponibilidade do serviço. A readjudicação documentada dos 17 casos de fronteira corrige a seleção posicional anteriormente usada, mas não transforma o fluxo em dupla codificação independente.

A auditoria final dos 177 estudos examinou os 105 alertas históricos de localização de evidência. Noventa e quatro âncoras foram confirmadas no texto integral após normalização de Unicode, diacríticos, espaços e pontuação; nos 11 casos restantes, a âncora foi substituída por evidência alternativa já registrada na matriz e literalmente localizada no texto integral. O arquivo `CORPUS_EVIDENCE_VERIFICATION_177.csv` preserva o alerta original, o método de confirmação, o trecho final, a página e o estado da verificação. Não restaram casos sem evidência literal verificável. Essa conferência demonstra existência do trecho, não concordância temática entre revisores humanos independentes.

## Reconciliação do universo e do corpus

O checkpoint possui 408 linhas. Uma duplicata exata (`CAND-000510__2939b340`, duplicata de `CAND-000509__2939b340`) foi removida por igualdade de hash de PDF, hash de texto, `record_id` e `study_id`, resultando em 407 estudos únicos.

Os 17 registros `borderline` foram readjudicados em nove evidências de apoio, cinco referências contextuais e três exclusões. O resultado reproduz as contagens publicadas: 23 evidências centrais, 154 de apoio, 112 contextuais e 118 exclusões.

## Inventário e reprodução

- `CORPUS_ANALYTIC_177_INVENTORY.csv`: composição integral do corpus analítico.
- `CORPUS_EVIDENCE_VERIFICATION_177.csv`: fechamento auditável dos 105 alertas históricos e verificação dos 177 estudos.
- `CORPUS_THEME_RECONCILIATION_177.xlsx`: ligação direta entre estudo, classificação, codificação original, evidência, arquivo e hash.
- `SEARCH_COVERAGE_AUDIT_V2.csv`: matriz fonte × família de consulta, incluindo indisponibilidades históricas explicitadas.
- `LLM_ADJUDICATION_AUDIT_V2.md`: controles, resultados empíricos e riscos residuais da adjudicação assistida.
- `CORPUS_UNIVERSE_RECONCILIATION.csv`: reconciliação das 408 linhas operacionais com o universo de 407 estudos únicos.
- `CORPUS_BORDERLINE_ADJUDICATION_V2.csv`: decisões humanas dos 17 casos de fronteira.
- `CORPUS_RECONCILIATION_177.md`: explicação e testes de invariantes.
- `arquivos_tratados_aigovernanca/metagrade_llm_output/metagrade_python_llm_workbook.xlsx`: codificação temática e matriz de evidências.
- `tools/build_v2_inventory.ps1`: gerador reprodutível que falha se as contagens ou hashes obrigatórios divergirem.

PDFs, hashes, saídas JSON, checkpoint e planilha permanecem preservados. A rastreabilidade demonstrada cobre identidade, pertencimento ao corpus, decisão, arquivo, hash e evidência-âncora. A proveniência bibliográfica individual não preservada permanece registrada como limitação, sem reconstrução retroativa não verificável.

As frequências temáticas publicadas permanecem preservadas em `Recursos_do_artigo/v2/dados_figuras_v2.csv`. A matriz final de rótulos normalizados por estudo que originou essas frequências não foi preservada como artefato independente; por isso, `CORPUS_THEME_RECONCILIATION_177.xlsx` não fabrica retroativamente marcações individuais para forçar a reprodução dos totais. A planilha separa o que é diretamente reconciliável do que permanece como valor publicado, tornando esse limite auditável.
