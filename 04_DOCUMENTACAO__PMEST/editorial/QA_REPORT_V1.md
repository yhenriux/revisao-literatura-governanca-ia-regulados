# Relatório de verificação da v1 final

Data de fechamento: 15 de agosto de 2026.

Este relatório substitui o relatório corrente da v1 pré-auditoria, preservado em `QA_REPORT_V1_PRE_AUDITORIA.md`. A correção não constitui v2: os artefatos oficiais continuam identificados como v1.

## Resultado editorial

| Métrica | v0 | v1 final | Verificação |
|---|---:|---:|---|
| Palavras no corpo textual do DOCX | 16.201 | 7.906 | redução de 51,2% |
| Introdução | — | 338 | foco em problema, lacuna e contribuição |
| Trabalhos relacionados | — | 351 | integração pela lacuna |
| Método | — | 596 | protocolo científico essencial |
| Resultados e modelo | — | 4.427 | preservação prioritária |
| Discussão | — | 734 | meta de 700–800 atendida |
| Conclusão | — | 182 | meta de 180–220 atendida |
| Referências | — | 1.042 | 29 entradas, idênticas à pré-auditoria |
| Parágrafos | 408 | 224 | estrutura condensada |
| Tabelas | 13 | 3 | material operacional transferido |
| Figuras/gráficos | 7 | 7 | preservação integral |
| Páginas da versão limpa | 31 | 16 | todas inspecionadas |
| Páginas da redline | — | 19 | todas inspecionadas |

## Integridade científica

- A v0 permaneceu inalterada; SHA-256: `73E87B454BE1974234275ADAADB7465AB49209183CF79B5496C02353438B4843`.
- Não houve busca adicional, mudança de corpus, inclusão de referência ou modificação de resultado científico.
- As 29 referências da v1 pré-auditoria e da v1 final são textualmente idênticas.
- Permanecem sete figuras, três tabelas e todas as conclusões científicas.
- As ocorrências numéricas autônomas são: `407=4`, `177=5`, `112=1`, `118=3`, `23=5`, `154=1`.
- A discussão distingue evidência sintetizada de proposição autoral e delimita o modelo como estrutura analítica sujeita a validação empírica.

## Equivalência e rastreabilidade

- A redline contém 33 inserções e 33 exclusões rastreadas, sem movimentos artificiais.
- Há quatro comentários editoriais, cobrindo números, figuras/texto, discussão e conclusão.
- Após aceitar as alterações, a redline e a versão limpa apresentam os mesmos 183 parágrafos não vazios, as mesmas três tabelas e os mesmos sete objetos de mídia.
- O manuscrito final foi gerado por `tools/build_article_v1.py`; a redline, por `tools/create_tracked_redline.py`.
- Commit de preservação: `1c71e1e`. Commit dos artefatos finais: `905d692`.
- A tag histórica `article-v1` permanece no estado publicado; o fechamento corrigido recebe `article-v1-final`.

## Verificação técnica, visual e de acessibilidade

- DOCX limpo renderizado em 16 páginas; redline renderizada em 19 páginas.
- Todas as 35 páginas foram inspecionadas individualmente.
- Não foram observados cortes, sobreposições, quebras de tabela, legendas órfãs ou páginas vazias.
- Sete imagens inline possuem texto alternativo descritivo.
- Auditoria automatizada da versão limpa e da redline: zero achados altos, médios ou baixos.
- Estrutura de página: A4, retrato, uma seção, margens preservadas.
- Hierarquia: sete títulos de nível 1 e sete de nível 2.
- Resumo e abstract foram verificados quanto à equivalência semântica.
- As oito construções defensivas especificadas na auditoria ocorreram zero vezes.

## Hashes dos artefatos finais

| Artefato | SHA-256 |
|---|---|
| `Artigo_Governanca_Conversacional_v1_EDITAVEL.docx` | `071F989752E91B9863C17673C93DFEBA137888F5876C38AD03C846E1CD68CFCA` |
| `Artigo_Governanca_Conversacional_v1_COM_ALTERACOES.docx` | `37F6DA33B1C41992DB99749CC6BA1D7439819C29660DC2EB3DA26345A26A54E1` |
| `Artigo_Governanca_Conversacional_v1_FINAL_PARA_LEITURA.pdf` | `C7EBEDFBFAD963E2A1E3F3A6C7A38069383F06F112C6D1BCCE17FFE74317940E` |

## Parecer de aceite interno

Todos os critérios definidos para a correção definitiva da v1 foram atendidos. Não há item parcial ou pendente. O manuscrito permite localizar rapidamente problema, lacuna, método, evidências, modelo de cinco camadas, discussão e contribuição, preservando a rastreabilidade necessária a uma revisão sistemática.
