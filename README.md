# Governança Conversacional em Sistemas Baseados em LLMs

Revisão sistemática da literatura sobre governança conversacional em sistemas baseados em modelos de linguagem de grande escala implantados em ambientes regulados.

## Comece aqui

- **Artigo para leitura e envio:** [`Artigo/Artigo_v2_final.pdf`](Artigo/Artigo_v2_final.pdf)
- **Versão editável:** [`Artigo/Artigo_v2_para_editar.docx`](Artigo/Artigo_v2_para_editar.docx)
- **Guia dos artefatos:** [`Artigo/LEIA_PRIMEIRO.md`](Artigo/LEIA_PRIMEIRO.md)
- **Histórico editorial:** [`Documentacao_do_projeto/editorial/`](Documentacao_do_projeto/editorial/)
- **Método e reprodução:** [`Documentacao_do_projeto/methodology/`](Documentacao_do_projeto/methodology/)
- **Decisões e versionamento:** [`Documentacao_do_projeto/project/`](Documentacao_do_projeto/project/)
- **Arquitetura facetada PMEST:** [`Documentacao_do_projeto/project/RANGANATHAN_FACETED_ARCHITECTURE.md`](Documentacao_do_projeto/project/RANGANATHAN_FACETED_ARCHITECTURE.md)
- **Corpus tratado:** [`arquivos_tratados_aigovernanca/`](arquivos_tratados_aigovernanca/) — nome preservado por compatibilidade com o pipeline; no Drive, aparece como `Corpus_da_revisao`.
- **Catálogo bibliográfico digital:** [`catalogo_virtual/index.html`](catalogo_virtual/index.html) — navegação Swagger-like dos metadados e estados de triagem.

## Status atual

| Item | Estado |
|---|---|
| Manuscrito corrente | v2 em revisão metodológica |
| Marco Git | `article-v1-final` |
| Arquivo para envio | `Artigo/Artigo_v2_final.pdf` |
| Corpus desta rodada | congelado |
| Nova busca bibliográfica | não prevista |
| Próxima ação | submissão ou avaliação pelos professores |

## Conteúdo do repositório

- `Artigo/`: versões oficiais e históricas do artigo em DOCX e PDF.
- `Referencias_da_pesquisa/`: exemplo de survey/review usado como referência de qualidade.
- `arquivos_tratados_aigovernanca/`: corpus tratado, textos completos, PDFs, resultados brutos de avaliação por LLM, planilha de metagrade e utilitário Python de adjudicação.
- `catalogo_virtual/`: catálogo técnico derivado dos inventários, sem duplicar a fonte de verdade científica.

O detalhamento metodológico, as regras de governança do corpus e o estado do pipeline estão documentados em [`arquivos_tratados_aigovernanca/README.md`](arquivos_tratados_aigovernanca/README.md).

A organização documental segue as facetas PMEST de Ranganathan: personalidade, matéria, energia, espaço e tempo. A classificação é explicada em [`Documentacao_do_projeto/project/RANGANATHAN_FACETED_ARCHITECTURE.md`](Documentacao_do_projeto/project/RANGANATHAN_FACETED_ARCHITECTURE.md).

A documentação técnica, metodológica e editorial do projeto está organizada em [`Documentacao_do_projeto/README.md`](Documentacao_do_projeto/README.md). Esse centro documental registra a arquitetura da informação, a política de versionamento, o parecer editorial, a matriz de resposta, as decisões e o material suplementar.

## Segurança

O utilitário Python aceita credenciais somente por argumento ou pelas variáveis de ambiente `LLM_API_KEY`/`OPENAI_API_KEY`. Nunca adicione chaves, tokens ou arquivos `.env` ao repositório.

## Versionamento do manuscrito

Versões publicadas são imutáveis. A `v0` preserva o manuscrito integral avaliado pelo parecerista; a `v1` representa a revisão estrutural pós-parecer; a `v2` incorpora a segunda rodada metodológica, o inventário dos 177 estudos e as limitações documentadas. Cada marco possui cópia limpa, redline, PDF, hash, commit e tag próprios.

## Observação sobre direitos autorais

O repositório contém cópias de artigos acadêmicos reunidas para pesquisa. Mantenha o projeto privado e confirme as licenças antes de redistribuir qualquer texto completo.
