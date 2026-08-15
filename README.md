# Governança Conversacional em Sistemas Baseados em LLMs

Repositório de trabalho da revisão sistemática da literatura sobre governança conversacional em sistemas baseados em modelos de linguagem de grande escala implantados em ambientes regulados.

## Conteúdo do repositório

- `versoes_artigo/`: versão de trabalho do artigo em DOCX e PDF.
- `exemplos_qualificados_revisao_literatura/`: exemplo de survey/review usado como referência de qualidade.
- `arquivos_tratados_aigovernanca/`: corpus tratado, textos completos, PDFs, resultados brutos de avaliação por LLM, planilha de metagrade e utilitário Python de adjudicação.

O detalhamento metodológico, as regras de governança do corpus e o estado do pipeline estão documentados em [`arquivos_tratados_aigovernanca/README.md`](arquivos_tratados_aigovernanca/README.md).

## Estado atual

A busca, a consolidação do corpus, a triagem automatizada de título/resumo e a recuperação/extracão automatizada de texto completo foram executadas. A leitura humana integral, a decisão final de elegibilidade, a avaliação CASP/JBI, a codificação temática, a síntese e o fluxograma PRISMA permanecem pendentes.

## Segurança

O utilitário Python aceita credenciais somente por argumento ou pelas variáveis de ambiente `LLM_API_KEY`/`OPENAI_API_KEY`. Nunca adicione chaves, tokens ou arquivos `.env` ao repositório.

## Observação sobre direitos autorais

O repositório contém cópias de artigos acadêmicos reunidas para pesquisa. Mantenha o projeto privado e confirme as licenças antes de redistribuir qualquer texto completo.
