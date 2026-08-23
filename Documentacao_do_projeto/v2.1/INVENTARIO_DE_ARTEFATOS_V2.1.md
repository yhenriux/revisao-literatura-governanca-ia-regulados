# Inventário de artefatos — v2.1 final

Data de fechamento: 23 de agosto de 2026.

Este inventário identifica os artefatos correntes da v2.1. Arquivos de processo permanecem versionados em suas pastas de origem, mas não substituem as fontes científicas de verdade indicadas abaixo.

## Manuscrito

| Artefato | Função | Bytes | SHA-256 |
|---|---|---:|---|
| `../../Artigo/Artigo_v2.1_para_editar.docx` | manuscrito limpo e editável | 2.213.068 | `397c2cf8caffa981df5e24b13a3d7771e1953ba6e782be43cb9ed41e37b8bb55` |
| `../../Artigo/Artigo_v2.1_para_leitura.pdf` | versão final para leitura e avaliação | 1.026.590 | `991ec09fd990ac76dc9bdee8b84fb0e61e87666e4f3f83a2cec41e9876233fc1` |
| `../../Artigo/Artigo_v2.1_com_alteracoes.docx` | comparação rastreável entre v2 e v2.1 | 2.216.854 | `e084f7c2769cab99e848c754b7506cbded63c08e19a7ecfb79a9311c9f671fbf` |

## Corpus e decisões

| Artefato | Função | Bytes | SHA-256 |
|---|---|---:|---|
| `triagem_texto_completo/CORPUS_ANALITICO_FINAL_V2.1.csv` | fonte de verdade dos 358 estudos incluídos | 509.797 | `cb0f008bab664af2a2fbae6c3ed44b03756f72f03441e7181d735cf21657abf5` |
| `triagem_texto_completo/REGISTRO_DECISOES_CORPUS_V2.1.csv` | 383 decisões finais documentadas | 552.900 | `6fcd60d8da12213d5917a20b35cd837b486adee6911bc405f67b04b6b48f4997` |
| `triagem_texto_completo/MATRIZ_ESTUDO_MECANISMO_CAMADA_V2.1.csv` | matriz longa que reproduz as contagens | 5.172.455 | `67afe6a61e789d559a9c3ab2a412c6b899323f5b168aa02cceff7a927d4a2370` |
| `triagem_texto_completo/RECONCILIACAO_CONTAGENS_CORPUS_V2.1.md` | resumo de reconciliação do corpus | 833 | `e70ddda65d97793d79cab0e9c9e6dbb71bf5128b4938ad47d5aa122bdd16cf03` |

O corpus final contém 358 estudos únicos: 30 evidências centrais e 328 evidências de apoio. Cada registro possui identificação, classificação, setor, mecanismos, camadas, PDF, hash, página e trecho de evidência.

## Recuperação e recursos analíticos

| Artefato | Função | Bytes | SHA-256 |
|---|---|---:|---|
| `busca_de_sensibilidade/Resultados_recuperados_v2.1.csv` | resultados posicionais preservados | 2.703.046 | `92923c48ed85f3d56ce4cab7b8573336eb737cf187e7116f66575937e9a14a1f` |
| `busca_de_sensibilidade/Log_de_execucao_das_consultas_v2.1.csv` | execução, parâmetros, falhas e hashes | 13.559 | `aaedc1232833c218afefae4fe28229d5fa71e7e1b0afb2391b71342417575255` |
| `../../Recursos_do_artigo/v2.1/dados_figuras_v21.csv` | dados versionados das sete figuras | 10.779 | `3906a9f07e6288ceae3f31d998a019bf6ccbadd17fe2b95c461d3b702273dc65` |
| `../../catalogo_virtual/catalogo.json` | catálogo público do corpus analítico | 1.196.352 | `c952deee882e020dae4bdcb657eb9e0cc3aa8e50acebce42e0c193c5f3c7e3bf` |

## Verificação

| Artefato | Função | Bytes | SHA-256 |
|---|---|---:|---|
| `RELATORIO_DE_QUALIDADE_V2.1.md` | auditoria automatizada e editorial | 2.214 | `84cc0749b9805bbfd22ed06a4213bf3ad0724a6d2beb5c9185c39b51e29d02f0` |
| `MATRIZ_DE_RESPOSTA_AO_PARECER_V2.1.md` | parecer → ação → evidência | — | recalculado no commit final |
| `CHECKLIST_DE_FECHAMENTO_V2.1.md` | portão de publicação | — | recalculado no commit final |

## Controle de versão

- Versão preservada de comparação: `article-v2`.
- Branch de preparação: `codex/article-v2-1`.
- Marco de entrega: `article-v2.1`.
- Commit científico: `4d3f2e3`.
- Catálogo verificado com 358 estudos em `https://yhenriux.github.io/revisao-literatura-governanca-ia-regulados/`.
- Pasta do artigo no Drive: `https://drive.google.com/drive/folders/1mBMhIJ2HTfZ1y6AxrsVWJoB2W7VvBmX7`.
- Pacote documental v2.1 no Drive: `https://drive.google.com/drive/folders/1ZAwQC4rwraOsXgjy-T2B4_thyyMlHL4u`.

Nenhum arquivo da v2 foi sobrescrito. A v2.1 possui nomes próprios e permanece reproduzível pelos scripts versionados em `tools/`.
