# Versão 2.1 — validação metodológica final

Esta pasta reúne somente os artefatos necessários para responder ao terceiro parecer de Mauricio Almeida. A versão 2 permanece preservada e não será sobrescrita.

## Ordem de trabalho

1. Leia `PROTOCOLO_METODOLOGICO_V2.1.md`.
2. Confirme a declaração autoral em `DECLARACAO_ORIGEM_DAS_CAMADAS_V2.1.md`.
3. Preencha `Validacao_humana_do_corpus_v2.1.xlsx` em lotes de 25 estudos.
4. Complete, na mesma planilha, a avaliação JBI dos estudos centrais e o quadro CERQual dos achados compatíveis.
5. Execute ou examine o relatório da busca prospectiva de sensibilidade.
6. Somente depois dessas etapas, gerar o DOCX limpo, a redline, o PDF e a tag `article-v2.1`.

## Estado da busca prospectiva em 22 de agosto de 2026

- 40 combinações foram registradas: oito fontes × cinco famílias de busca.
- OpenAlex, Crossref, Europe PMC, arXiv e DOAJ responderam e tiveram as respostas preservadas.
- PubMed foi bloqueado porque `NCBI_EMAIL` não estava configurado.
- CORE foi bloqueado porque `CORE_API_KEY` não estava configurada.
- Semantic Scholar devolveu limite HTTP 429 nas cinco combinações; uma chave pode reduzir, mas não elimina, a limitação de taxa.
- Após deduplicação e comparação com os 407 registros históricos, existem 992 registros únicos aguardando triagem humana. Eles **não** integram o corpus enquanto Yago não os julgar.

O relatório completo está em `busca_de_sensibilidade/RELATORIO_DE_QUALIDADE_DA_BUSCA_V2.1.md`. A busca deve ser complementada depois que as configurações locais forem preenchidas em `.env.v2.1.local`, arquivo ignorado pelo Git.

## Estados permitidos

- `em_preparacao`: instrumento ainda sendo produzido;
- `aguardando_validacao_humana`: Yago deve preencher ou confirmar decisões;
- `em_reconciliacao`: decisões humanas estão sendo comparadas aos artefatos históricos;
- `aprovada_para_publicacao`: todos os critérios de aceite passaram.

O estado atual é **aguardando validação humana**. Não utilizar nenhum arquivo desta pasta como manuscrito final antes do fechamento do checklist.
