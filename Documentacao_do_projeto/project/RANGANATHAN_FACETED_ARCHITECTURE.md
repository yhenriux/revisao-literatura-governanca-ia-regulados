# Arquitetura facetada PMEST do projeto

Esta arquitetura aplica as cinco facetas de S. R. Ranganathan à organização documental do projeto. As facetas funcionam como metadados de navegação e proveniência; não substituem os nomes canônicos dos arquivos usados em scripts, citações ou envio editorial.

## Facetas

| Faceta | Pergunta de navegação | Aplicação no projeto |
|---|---|---|
| **P — Personalidade** | Qual é o objeto? | artigo, corpus, documentação, ferramenta ou referência |
| **M — Matéria** | Qual é o assunto ou conteúdo? | governança conversacional, LLMs, ambientes regulados, método e evidência |
| **E — Energia** | Que operação está sendo realizada? | ler, editar, auditar, reproduzir, versionar ou publicar |
| **S — Espaço** | Em que contexto ou camada se aplica? | saúde, finanças, governo, jurídico, organização, interação e sistema |
| **T — Tempo** | Em que estado histórico? | v0, v1 pré-auditoria, v1 final, corpus congelado ou estado corrente |

## Rotas de uso

| Necessidade | Rota recomendada | Código PMEST |
|---|---|---|
| Enviar o artigo | `Artigo/Artigo_final.pdf` | P artigo · E publicar · T v1 final |
| Editar o artigo | `Artigo/Artigo_para_editar.docx` | P artigo · E editar · T v1 final |
| Auditar alterações | `Documentacao_do_projeto/editorial/` e `Artigo/Artigo_com_alteracoes.docx` | P auditoria · E auditar · T v1 final |
| Consultar decisões | `Documentacao_do_projeto/project/DECISION_LOG.md` | P documentação · E versionar · T corrente |
| Reproduzir o método | `Documentacao_do_projeto/methodology/` e `tools/` | P método/ferramenta · E reproduzir · T corrente |
| Consultar evidências | `arquivos_tratados_aigovernanca/` | P corpus · M evidência · E analisar · T corpus congelado |

O diretório do corpus mantém o identificador técnico `arquivos_tratados_aigovernanca/` para não quebrar o pipeline. Na camada de apresentação do Google Drive, ele é exibido como `Corpus_da_revisao`.

## Regra de nomenclatura

Os nomes técnicos do corpus permanecem estáveis porque são usados em scripts. Para a camada humana, os nomes oficiais do manuscrito usam linguagem simples e função explícita: `Artigo_final.pdf`, `Artigo_para_editar.docx` e `Artigo_com_alteracoes.docx`.

Não usar `final_final`, `novo`, `corrigido2` ou nomes que dependam da memória de quem criou o arquivo. A versão e o estado devem aparecer no nome apenas quando forem parte da identidade documental.

## Regra de limpeza

O repositório e a pasta compartilhada devem conter artefatos oficiais, históricos necessários, documentação de proveniência, corpus reproduzível e ferramentas. Renders, caches, logs locais e intermediários permanecem fora das áreas versionadas.
