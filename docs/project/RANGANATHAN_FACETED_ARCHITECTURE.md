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
| Enviar o artigo | `versoes_artigo/Governanca_Conversacional_v1.pdf` | P artigo · E publicar · T v1 final |
| Editar o artigo | `versoes_artigo/Governanca_Conversacional_v1.docx` | P artigo · E editar · T v1 final |
| Auditar alterações | `docs/editorial/` e `versoes_artigo/*redline*` | P auditoria · E auditar · T v1 final |
| Consultar decisões | `docs/project/DECISION_LOG.md` | P documentação · E versionar · T corrente |
| Reproduzir o método | `docs/methodology/` e `tools/` | P método/ferramenta · E reproduzir · T corrente |
| Consultar evidências | `arquivos_tratados_aigovernanca/` | P corpus · M evidência · E analisar · T corpus congelado |

## Regra de nomenclatura

Os nomes oficiais do manuscrito permanecem estáveis porque são usados em citações, scripts, hashes, e-mails e instruções de envio. Para novos documentos auxiliares, prefira nomes descritivos com função explícita, por exemplo `RANGANATHAN_FACETED_ARCHITECTURE.md` e `CONTRIBUTING.md`.

Não usar `final_final`, `novo`, `corrigido2` ou nomes que dependam da memória de quem criou o arquivo. A versão e o estado devem aparecer no nome apenas quando forem parte da identidade documental.

## Regra de limpeza

O repositório e a pasta compartilhada devem conter artefatos oficiais, históricos necessários, documentação de proveniência, corpus reproduzível e ferramentas. Renders, caches, logs locais e intermediários permanecem fora das áreas versionadas.
