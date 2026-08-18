# Reconciliação do corpus analítico de 177 estudos

## Regra editorial

Os números publicados na v2 permanecem invariantes: 407 estudos avaliados em texto completo, 177 estudos no corpus analítico, 23 evidências centrais, 154 evidências de apoio, 112 referências fundacionais/contextuais e 118 exclusões.

## Inventário auditável

O arquivo [`CORPUS_ANALYTIC_177_INVENTORY.csv`](CORPUS_ANALYTIC_177_INVENTORY.csv) identifica individualmente os 177 estudos, com título, autores, ano, veículo, identificador do PDF, hash, decisão de origem e classificação publicada.

O inventário foi construído a partir do checkpoint versionado da adjudicação. Ele reúne os 23 registros classificados como evidência central, 145 classificados como evidência de apoio e nove registros de origem borderline que integram a contagem publicada de apoio. Esses nove registros estão marcados explicitamente para conferência manual; não foram ocultados nem recodificados silenciosamente.

## Procedimento de contagem

1. Selecionar os identificadores presentes no inventário.
2. Deduplicar por identificador do PDF.
3. Contar a coluna `classificacao_publicada` para obter central e apoio.
4. Contar `camadas` e `setor` como campos multirrótulo; suas frequências podem superar 177.
5. Conferir hashes e evidências contra o checkpoint e os PDFs preservados.

## Limite de reconciliação

O checkpoint operacional contém mais registros e decisões intermediárias que o universo publicado no artigo. A diferença entre estados é preservada como diferença entre artefatos; a v2 não altera os números científicos publicados. Uma futura auditoria independente poderá substituir os nove registros marcados como borderline somente mediante decisão registrada e nova versão formal.
