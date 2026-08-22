# Protocolo metodológico da v2.1

## Objetivo

Responder aos seis pontos do terceiro parecer sem reestruturar o artigo: sensibilidade ao limite de 25 resultados, origem das cinco camadas, regra de evidência central, validação da adjudicação assistida por LLM, papel de JBI/CERQual e rastreabilidade do corpus.

## Governança da revisão

- Revisor humano: Yago Henrique.
- Não houve e não será alegada dupla revisão humana independente.
- O LLM é instrumento auxiliar; não é revisor científico nem árbitro da decisão final.
- A decisão humana será registrada por estudo, com data, justificativa e evidência localizada.
- Divergências entre sugestão do LLM e decisão humana serão reexaminadas no texto integral. A decisão humana fundamentada prevalecerá.

## Evidência central

Um estudo será classificado como `evidência central` somente quando os três critérios forem confirmados:

1. **Objeto direto:** governança, supervisão, risco, accountability, auditoria, compliance ou operação controlada de LLMs, IA generativa ou sistemas conversacionais.
2. **Contexto:** relação explícita com ambiente regulado, de alto impacto ou mecanismo demonstravelmente transferível para esse contexto.
3. **Contribuição substantiva:** resultado empírico, síntese sistemática, mecanismo avaliado ou arquitetura conceitual relevante para pelo menos uma questão da revisão.

Um estudo elegível será `evidência de apoio` quando contribuir de modo periférico, contextual ou transferível, sem cumprir simultaneamente os três critérios. Confiança do LLM e escores históricos não determinam essa classificação.

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

- A avaliação automatizada histórica `CASP/JBI adaptada` será tratada apenas como triagem auxiliar.
- A v2.1 utilizará instrumento JBI humano e específico ao desenho para os estudos centrais.
- Não haverá escore agregado entre desenhos heterogêneos.
- A conclusão por estudo será `sem preocupações relevantes`, `preocupações menores` ou `preocupações importantes`, sempre com justificativa.
- CERQual será aplicado somente no nível de achados qualitativos compatíveis, conforme a orientação oficial: <https://www.cerqual.org/official-guidance-for-applying-grade-cerqual/>.
- Contagens quantitativas e achados incompatíveis serão marcados como `não aplicável`.

## Busca prospectiva de sensibilidade

A busca original de julho de 2026 não pode ser reproduzida exatamente porque as strings completas, posições e respostas por consulta não foram preservadas. A v2.1 realizará uma busca prospectiva, explicitamente datada, com corte de publicação em 31 de julho de 2026.

- Fontes: OpenAlex, Crossref, Semantic Scholar, PubMed, Europe PMC, CORE, arXiv e DOAJ.
- Famílias: governança de LLMs; LLMOps e observabilidade; governança conversacional; ambientes regulados; supervisão humana e contestabilidade.
- Faixas iniciais: 1–25, 26–50, 51–75 e 76–100.
- Extensão: blocos adicionais de 100 quando a faixa 76–100 contiver estudo novo elegível.
- Deduplicação: DOI normalizado; subsidiariamente título normalizado, ano e autoria.
- Todo registro novo deverá receber decisão humana antes de alterar o corpus.

## Critério de encerramento

A v2.1 somente será publicada quando não houver campos humanos pendentes, as contagens forem reproduzíveis pela matriz longa e o checklist editorial estiver integralmente atendido.

