# Inventário de artefatos — v2 final

## Manuscrito

| Artefato | Função | SHA-256 |
|---|---|---|
| `Artigo/Artigo_v2_final.docx` | Manuscrito final com redesign visual | `936B4838C80746075745CEB6ECE19AF5452C5CD8C5A5F9B92CEAA038BA7E2781` |
| `Artigo/Artigo_v2_para_editar.docx` | Versão editável preservada, sem o redesign visual final | `E03C4DD19DB4BEA0640D12E86797E3EEA8E9052C93C01A19AD2D6093C8FD5540` |
| `Artigo/Artigo_v2_com_alteracoes.docx` | Redline da v1 para a v2 | `BB2EEEF0F168045693199B9B179607BBD6F26F7C30C5616553BA6104A0D1614B` |
| `Artigo/Artigo_v2_final.pdf` | PDF final redesenhado, 15 páginas | `977FC0CB76D90494A3B8FAE52B72E86D32FEACC35A8257464A62CF40BC1C5588` |

## Recursos visuais reprodutíveis

| Artefato | Função | SHA-256 |
|---|---|---|
| `Recursos_do_artigo/v2/dados_figuras_v2.csv` | Dados longos congelados dos Gráficos 1–6 | `AF11FD28867BB360DD865C9CB413CE503DCC8035E450483E0439F7BB52885B10` |
| `tools/render_article_visuals_v2.mjs` | Gerador das fontes SVG e PNGs dos seis gráficos quantitativos | `C2E5592868BB214DBD66BD53E56E9C3B8C3D005236CD854ACFCAD4DF49737AAF` |
| `tools/redesign_article_v2.py` | Aplicação reprodutível do redesign ao DOCX final | `3273B1E144EEE8E2CD60B756CD971578FF26D45F6014DCD0A4CB9E74EDB4DAF0` |
| `Recursos_do_artigo/v2/fontes_vetoriais/` | Seis fontes SVG dos gráficos quantitativos | ver hashes individuais no histórico Git |
| `Recursos_do_artigo/v2/imagens/` | Sete PNGs efetivamente incorporados | ver hashes individuais no histórico Git |
| `Recursos_do_artigo/v2/imagens/Figura_1_modelo_de_cinco_camadas.png` | Figura 1 histórica restaurada de `article-v2-final` | `A160B7C68DD7F78DC910AB497C1AF51F91FDBF5EF4F22B0F47D292ABFF14930D` |

### Ajuste de contraste do Gráfico 6

| Artefato | SHA-256 |
|---|---|
| `Recursos_do_artigo/v2/fontes_vetoriais/Grafico_6_coocorrencia_mecanismos_camadas.svg` | `271DEC1C9123F795A0430D1BCDF361F47337C0B181C2498F3E21494C14118F8E` |
| `Recursos_do_artigo/v2/imagens/Grafico_6_coocorrencia_mecanismos_camadas.png` | `890F911469EDDA24B297FBD060171D02C67B2A837C9FA32210782B209FC35115` |

## Rastreabilidade metodológica

| Artefato | Função | SHA-256 |
|---|---|---|
| `CORPUS_ANALYTIC_177_INVENTORY.csv` | Inventário individual do corpus analítico | `3D80BE7EA8C4078D085AC3ADDE4C684DFCDF40CCC8AE3BE0CF594B3A218EF7EB` |
| `CORPUS_UNIVERSE_RECONCILIATION.csv` | Reconciliação das 408 linhas operacionais com 407 estudos publicados | `5AB47969E045625545421265D0E1E1C4F2BA308AA33AC4BF624B1A4DE7B77363` |
| `CORPUS_BORDERLINE_ADJUDICATION_V2.csv` | Readjudicação dos 17 casos de fronteira | `7E73EF73F5D15A75EC6AB51BF57B23D8E87A7EDA408FE2C8928319462DFBEC7E` |
| `CORPUS_RECONCILIATION_177.md` | Explicação auditável da reconciliação | `0064197DB5FFA396D676515239BEF29F67F808668AB9011C47F333CE7A5AE340` |
| `METHODS_SUPPLEMENT_V2.md` | Critérios completos, cobertura e controles metodológicos | `A88E613DD2E2D248420F1F175C61EF718EE61E6B3E214C0D9AE414CA3BB95C57` |

## Marcos de versão

- Estado anterior à auditoria final: `article-v2-pre-final-audit`.
- Marco metodológico original: `article-v2`, mantido sem movimentação.
- Marco desta entrega: `article-v2-final`.
- Marco visual, sem movimentar as tags anteriores: `article-v2-final-visual`.
- Marco do ajuste de contraste: `article-v2-final-visual-white-labels`.
- Marco da restauração da Figura 1: `article-v2-final-figure-restored`.
- Commit de conteúdo científico e artefatos: `11c06c2`.
- Commit do redesign visual e dos recursos reprodutíveis: `2325db1`.

## Cópias correntes no Google Drive

- PDF final: ID `1KXQchTmWKICS-p6JkgxT8kFIZ7siVAnY`.
- DOCX final: ID `1kLWQhY_qVN2iZONIrEi9Y9ERdeMAwiRU`.
- DOCX editável: ID `1qGDfndeHw3Gdrge7klZ2XK3TnRnhZ5-U`.
- DOCX com alterações: ID `1CVc3DJW1k03Fwltap369IFdJdpHiO2BS`.
- Os IDs foram preservados e os bytes substituídos, mantendo o histórico de revisões do Drive.
