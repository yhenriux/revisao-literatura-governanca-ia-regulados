# Relatório técnico de preparação — v2.1

Data: 22 de agosto de 2026.

## Resultado

O pacote de validação foi gerado e verificado. Ele ainda não constitui a versão final do artigo porque as decisões científicas reservadas a Yago permanecem pendentes.

## Planilha

- oito abas presentes;
- 177 registros históricos em `Validacao_177`;
- 23 linhas iniciais em `Avaliacao_JBI`, correspondentes às evidências centrais publicadas na v2 e sujeitas a atualização após validação;
- cinco achados em `CERQual_achados`;
- 1.342 ocorrências da busca em `Triagem_novos`, das quais 992 são únicas e pendentes;
- listas de seleção presentes nas células de decisão;
- rótulos históricos do LLM separados da primeira decisão humana;
- fórmula de fechamento exige 177 confirmações, zero pendências históricas, JBI para todas as centrais humanas, cinco decisões CERQual e zero triagens novas pendentes;
- seis pré-visualizações inspecionadas sem cortes ou sobreposições.

## Busca

- 40 combinações registradas;
- 25 respostas brutas correspondem exatamente a 25 hashes não vazios no log;
- nenhuma resposta bruta órfã permaneceu no pacote;
- 15 combinações bloqueadas ou falhas permanecem explicitamente registradas;
- comparação executada contra os 407 registros históricos, e não apenas contra o corpus analítico de 177;
- nenhum registro novo foi incluído automaticamente.

## Scripts

- `search_sensitivity_v21.py` compilado sem erro de sintaxe;
- `build_validation_workbook_v21.mjs` executado até a exportação XLSX;
- planilha reaberta estruturalmente: oito abas e 37 regras de validação de dados;
- varredura de fórmulas sem `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?` ou `#N/A`.

## Bloqueadores científicos remanescentes

1. confirmação e assinatura da origem das camadas;
2. validação humana dos 177 estudos;
3. triagem dos 992 registros únicos e complementação das fontes bloqueadas;
4. JBI das evidências centrais confirmadas;
5. CERQual dos achados compatíveis;
6. reconciliação do corpus e atualização do artigo.

Até esses bloqueadores serem resolvidos, não devem ser gerados PDF final, redline final ou tag `article-v2.1`.
