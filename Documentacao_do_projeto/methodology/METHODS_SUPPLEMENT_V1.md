# Suplemento metodológico da v1

Este documento preserva detalhes retirados do corpo principal para melhorar fluidez sem reduzir rastreabilidade.

## Fontes e estratégias

A busca automatizada utilizou OpenAlex, Crossref, Semantic Scholar, PubMed, Europe PMC, CORE, arXiv e DOAJ. Cinco famílias conceituais cobriram governança de LLMs, LLMOps/observabilidade, governança conversacional, ambientes regulados e supervisão humana/contestabilidade.

As consultas foram executadas em julho de 2026. Foi definido limite de até 25 resultados armazenados por combinação entre estratégia e fonte. Semantic Scholar apresentou restrições de taxa e o arXiv teve falhas de tempo de resposta. Essas limitações fazem parte da interpretação de cobertura.

## Expansão bibliográfica

O snowballing incluiu:

1. referências citadas;
2. trabalhos citantes;
3. trabalhos relacionados no OpenAlex;
4. expansão controlada por autoria;
5. expansão controlada por veículo.

## Processamento técnico

Os artefatos registram origem, endpoint, consulta, data, quantidade informada pela fonte, quantidade armazenada e status. A consolidação empregou DOI normalizado, título exato e similaridade textual, seguida de validação para evitar fusões indevidas.

A extração de PDF registrou texto por página, hashes do arquivo e do texto, extensão, status e indicadores de digitalização. A bibliografia foi separada do corpo para reduzir contaminação por referências citadas.

## Avaliação assistida

A triagem determinística usou taxonomia bilíngue e registrou termos, páginas e evidências literais. A adjudicação assistida por LLM recebeu metadados e trechos selecionados, respondeu em JSON e foi instruída a não inferir informações ausentes. Evidências foram verificadas contra o texto extraído.

O fluxo não constituiu revisão humana independente em duplicata. CASP/JBI e CERQual foram adaptados à heterogeneidade dos desenhos e usados como indicadores de cautela, não como medidas uniformes ou exclusão automática.

## Artefatos auditáveis no repositório

- corpus textual consolidado;
- PDFs recuperados;
- saídas JSON da adjudicação;
- planilha de metagrade;
- checkpoint e backup de erros;
- script de adjudicação;
- hashes e metadados incorporados aos artefatos de processamento.

