# Suplemento metodológico da v2

## Abrangência da recuperação

A busca utilizou OpenAlex, Crossref, Semantic Scholar, PubMed, Europe PMC, CORE, arXiv e DOAJ, com cinco famílias conceituais. As consultas foram executadas em julho de 2026. O limite de até 25 resultados por combinação entre estratégia e fonte foi operacional: reduziu volume redundante e tornou possível registrar e validar cada item. Não deve ser interpretado como prova de exaustividade.

Semantic Scholar apresentou restrições de taxa e o arXiv teve falhas de tempo de resposta. APIs e ordenações podem privilegiar relevância, recência ou popularidade. O snowballing por referências, citações, trabalhos relacionados, autoria e veículo reduziu o risco de perda, sem eliminá-lo. A cobertura é, portanto, sistemática e documentada, mas não exaustiva.

## Critérios de elegibilidade

Os sete critérios de inclusão e sete de exclusão usados operacionalmente na v1 são preservados neste suplemento. No corpo da v2, a Tabela 3 apresenta categorias consolidadas; este documento mantém a formulação completa, exemplos de fronteira e regras de aplicação.

## Adjudicação assistida por LLM

A triagem determinística registrou termos, páginas e evidências literais. A adjudicação recebeu metadados e trechos selecionados, respondeu em JSON e foi instruída a não inferir informação ausente. Evidências foram confrontadas com o texto extraído e casos sem correspondência receberam atenção.

| Etapa | Controle | Risco residual |
|---|---|---|
| Triagem determinística | termos, regras e evidências literais | falsos positivos/negativos por vocabulário |
| Adjudicação LLM | JSON estruturado e prompt restritivo | interpretação contextual incorreta |
| Validação | confronto com texto extraído | falhas de extração ou localização |
| Síntese | normalização e distinção central/apoio | dependência das decisões anteriores |

O procedimento não constituiu revisão humana independente em duplicata. A confiança numérica do LLM não é probabilidade calibrada. Persistem riscos de alucinação, enquadramento, erro de extração, dependência de versão, prompt e disponibilidade do serviço. O LLM ampliou escala e estrutura, mas não substituiu julgamento humano.

## Inventário e reprodução

O inventário completo dos 177 estudos está em `CORPUS_ANALYTIC_177_INVENTORY.csv`. PDFs, hashes, saídas JSON, checkpoint, planilha e script permanecem preservados em `arquivos_tratados_aigovernanca/`.
