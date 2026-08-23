# Protocolo metodológico da v2.1

## Objetivo

Responder aos seis pontos do terceiro parecer sem reestruturar o artigo: abrangência da recuperação, origem das cinco camadas, regra de evidência central, validação da adjudicação assistida por LLM, papel de JBI/CERQual e rastreabilidade do corpus.

## Governança da revisão

- Revisor humano: Yago Henrique.
- Não houve e não é alegada dupla revisão humana independente.
- O LLM é instrumento auxiliar; não é revisor científico nem árbitro da decisão final.
- A decisão humana foi registrada por estudo, com data, justificativa e evidência localizada.
- Divergências entre sugestão do LLM e decisão humana foram reexaminadas no texto integral. A decisão humana fundamentada prevaleceu.

## Evidência central

Um estudo será classificado como `evidência central` somente quando os três critérios forem confirmados:

1. **Objeto direto:** governança, supervisão, risco, accountability, auditoria, compliance ou operação controlada de LLMs, IA generativa ou sistemas conversacionais.
2. **Contexto:** relação explícita com ambiente regulado, de alto impacto ou mecanismo demonstravelmente transferível para esse contexto.
3. **Contribuição substantiva:** resultado empírico, síntese sistemática, mecanismo avaliado ou arquitetura conceitual relevante para pelo menos uma questão da revisão.

Um estudo elegível será `evidência de apoio` quando contribuir de modo periférico, contextual ou transferível, sem cumprir simultaneamente os três critérios. Confiança do LLM e escores automatizados não determinam essa classificação.

## Origem das cinco camadas

O relato metodológico adotará um processo híbrido e iterativo, condicionado à confirmação factual do autor:

1. perguntas de pesquisa e dimensões sensibilizadoras;
2. codificação aberta;
3. agrupamento axial;
4. comparação e refinamento iterativos;
5. consolidação das cinco camadas;
6. aplicação do vocabulário normalizado ao corpus;
7. contabilização descritiva.

As frequências caracterizam a incidência dos mecanismos no esquema consolidado. Elas não validam empiricamente o modelo.

## Adjudicação assistida por LLM

Fluxo documentado:

`triagem determinística → sugestão do LLM → localização automática de evidência → validação humana por Yago → decisão final`

A correspondência literal automática comprova apenas que um trecho foi localizado. Ela não comprova, isoladamente, que o trecho sustenta uma inferência científica. A planilha de validação separa essas duas operações.

## Avaliação crítica

- CASP/JBI foram usados como apoio crítico para identificar limitações metodológicas e qualificar a interpretação.
- Esses instrumentos não determinaram elegibilidade nem a distinção entre evidência central e de apoio.
- Não haverá escore agregado entre desenhos heterogêneos.
- As dimensões CERQual orientaram a reflexão sobre coerência, adequação, relevância e limitações dos achados qualitativos compatíveis.
- Não foram atribuídos níveis formais de confiança a contagens quantitativas ou achados incompatíveis.

## Recuperação ampliada e análise de sensibilidade

A v2.1 relata no corpo do artigo o procedimento final consolidado de recuperação, e não parâmetros transitórios de implementações anteriores. A recuperação foi realizada em múltiplas fontes e famílias de consulta, ampliada por faixas de resultados e complementada por rastreamento de referências, citações, autoria e veículos. Os registros foram deduplicados por DOI e, subsidiariamente, por título normalizado, ano e autoria.

A abrangência foi examinada por análise de sensibilidade, explicitamente datada e com corte de publicação em 31 de julho de 2026. Ela documenta o comportamento das fontes, a contribuição das posições posteriores e a cobertura do corpus tratado. Detalhes operacionais permanecem no suplemento e no registro técnico para preservar a proveniência sem sobrecarregar a narrativa científica.

- Fontes utilizadas na recuperação ampliada: OpenAlex, Crossref, Europe PMC, arXiv e DOAJ. Fontes sem execução utilizável não serão apresentadas como componentes efetivos da busca final; suas tentativas e falhas permanecem no log técnico.
- Famílias: governança de LLMs; LLMOps e observabilidade; governança conversacional; ambientes regulados; supervisão humana e contestabilidade.
- Faixas sucessivas examinadas até a centésima posição por combinação.
- Deduplicação: DOI normalizado; subsidiariamente título normalizado, ano e autoria.
- Todo registro incorporado recebeu decisão final do autor antes de integrar o corpus.

### Redação autorizada para o corpo do artigo

> A recuperação bibliográfica foi realizada em múltiplas fontes e famílias de consulta, com posterior ampliação por faixas de resultados e rastreamento de referências, citações, autoria e veículos. Os registros foram deduplicados por identificadores persistentes e, subsidiariamente, por título normalizado, autoria e ano. A abrangência foi examinada por análise de sensibilidade das posições recuperadas e pelo confronto entre fontes, mantendo-se no corpus apenas estudos elegíveis segundo os critérios definidos.

### Redação autorizada para as limitações

> Mecanismos de ordenação, indexação e disponibilidade das fontes podem influenciar a recuperação. A combinação de buscas em múltiplas bases, expansão por rastreamento bibliográfico, análise de posições posteriores e deduplicação reduziu a dependência de uma única fonte ou ordenação. O corpus deve ser interpretado como síntese sistemática de registros documentados, e não como enumeração exaustiva de toda a literatura existente.

## Critério de encerramento

A v2.1 possui 358 estudos incluídos, 30 evidências centrais e 328 de apoio. Não há campos científicos pendentes; as contagens são reproduzíveis pela matriz longa. A publicação depende apenas do fechamento operacional de hashes, commit, tag e sincronização.
