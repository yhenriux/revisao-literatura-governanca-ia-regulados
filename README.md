# Governança Conversacional em Sistemas Baseados em LLMs

Revisão sistemática da literatura sobre governança conversacional em sistemas baseados em modelos de linguagem de grande escala implantados em ambientes regulados.

## Comece aqui

- **Artigo para leitura e envio:** [`01_ARTIGO__VERSOES/ARTIGO__T-v1__LEITURA.pdf`](01_ARTIGO__VERSOES/ARTIGO__T-v1__LEITURA.pdf)
- **Versão editável:** [`01_ARTIGO__VERSOES/ARTIGO__T-v1__EDICAO.docx`](01_ARTIGO__VERSOES/ARTIGO__T-v1__EDICAO.docx)
- **Guia dos artefatos:** [`01_ARTIGO__VERSOES/README.md`](01_ARTIGO__VERSOES/README.md)
- **Histórico editorial:** [`04_DOCUMENTACAO__PMEST/editorial/`](04_DOCUMENTACAO__PMEST/editorial/)
- **Método e reprodução:** [`04_DOCUMENTACAO__PMEST/methodology/`](04_DOCUMENTACAO__PMEST/methodology/)
- **Decisões e versionamento:** [`04_DOCUMENTACAO__PMEST/project/`](04_DOCUMENTACAO__PMEST/project/)
- **Arquitetura facetada PMEST:** [`04_DOCUMENTACAO__PMEST/project/RANGANATHAN_FACETED_ARCHITECTURE.md`](04_DOCUMENTACAO__PMEST/project/RANGANATHAN_FACETED_ARCHITECTURE.md)
- **Corpus tratado:** [`arquivos_tratados_aigovernanca/`](arquivos_tratados_aigovernanca/)

## Status atual

| Item | Estado |
|---|---|
| Manuscrito corrente | v1 final fechada |
| Marco Git | `article-v1-final` |
| Arquivo para envio | `01_ARTIGO__VERSOES/ARTIGO__T-v1__LEITURA.pdf` |
| Corpus desta rodada | congelado |
| Nova busca bibliográfica | não prevista |
| Próxima ação | submissão ou avaliação pelos professores |

## Conteúdo do repositório

- `01_ARTIGO__VERSOES/`: versão de trabalho do artigo em DOCX e PDF.
- `03_REFERENCIAS__EXEMPLOS/`: exemplo de survey/review usado como referência de qualidade.
- `arquivos_tratados_aigovernanca/`: corpus tratado, textos completos, PDFs, resultados brutos de avaliação por LLM, planilha de metagrade e utilitário Python de adjudicação.

O detalhamento metodológico, as regras de governança do corpus e o estado do pipeline estão documentados em [`arquivos_tratados_aigovernanca/README.md`](arquivos_tratados_aigovernanca/README.md).

A organização documental segue as facetas PMEST de Ranganathan: personalidade, matéria, energia, espaço e tempo. A classificação é explicada em [`04_DOCUMENTACAO__PMEST/project/RANGANATHAN_FACETED_ARCHITECTURE.md`](04_DOCUMENTACAO__PMEST/project/RANGANATHAN_FACETED_ARCHITECTURE.md).

A documentação técnica, metodológica e editorial do projeto está organizada em [`04_DOCUMENTACAO__PMEST/README.md`](04_DOCUMENTACAO__PMEST/README.md). Esse centro documental registra a arquitetura da informação, a política de versionamento, o parecer editorial, a matriz de resposta, as decisões e o material suplementar.

## Segurança

O utilitário Python aceita credenciais somente por argumento ou pelas variáveis de ambiente `LLM_API_KEY`/`OPENAI_API_KEY`. Nunca adicione chaves, tokens ou arquivos `.env` ao repositório.

## Versionamento do manuscrito

Versões publicadas são imutáveis. A `v0` preserva o manuscrito integral avaliado pelo parecerista; a `v1` representa a revisão estrutural pós-parecer e possui cópia limpa, redline comentada e PDF. A v1 final é o artefato corrente. Qualquer alteração posterior deve preservar este estado e receber nova identificação somente quando representar um novo marco editorial formal, aprovado e documentado.

## Observação sobre direitos autorais

O repositório contém cópias de artigos acadêmicos reunidas para pesquisa. Mantenha o projeto privado e confirme as licenças antes de redistribuir qualquer texto completo.
