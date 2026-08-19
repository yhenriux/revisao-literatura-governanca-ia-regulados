# Inventário de artefatos — v2 final

## Manuscrito

| Artefato | Função | SHA-256 |
|---|---|---|
| `Artigo/Artigo_v2_final.docx` | Manuscrito final com fechamento metodológico e redesign visual | `3B4A9513B0D87E408CCF2A90311CE53EADC6C611ECD2EAE860DA76BB0E99453A` |
| `Artigo/Artigo_v2_para_editar.docx` | Versão editável com o mesmo conteúdo científico e sem o redesign visual final | `981949C5F34388E671B512E1D7DED93EAE25E472C43A4BE7F575CF71EEABD73D` |
| `Artigo/Artigo_v2_com_alteracoes.docx` | Redline da v1 para a v2 | `BB2EEEF0F168045693199B9B179607BBD6F26F7C30C5616553BA6104A0D1614B` |
| `Artigo/Artigo_v2_final.pdf` | PDF final redesenhado e auditado, 15 páginas | `8F1D228D344933905EA08CFE2BAFCE5E5C58AF720375B85219E004DB3A72D021` |

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
| `CORPUS_ANALYTIC_177_INVENTORY.csv` | Inventário individual do corpus analítico com histórico e estado final da verificação | `886E2453AB2ECCAB6B9C88B30983103EEE24E3EFF2376068A365EF9AA5317269` |
| `CORPUS_EVIDENCE_VERIFICATION_177.csv` | Auditoria das evidências dos 177 estudos e fechamento dos 105 alertas | `F875CF41C48741DE89771BDF25531D2452D7555E2A9896C8BE8F9ACA01EC5669` |
| `CORPUS_THEME_RECONCILIATION_177.xlsx` | Reconciliação estudo, classificação, codificação original, evidência, arquivo e hash | `266047FA4FA8F0725A7E64134FB861447AB382FAF5BC48C3BE06E71F9FDCAC22` |
| `SEARCH_COVERAGE_AUDIT_V2.csv` | Auditoria das 40 combinações fonte × família e dos dados históricos indisponíveis | `D4B7EA6682125FEE6E1D2023B2367D928E32D9E7B4BC47571709F6BD2A6D2F1F` |
| `LLM_ADJUDICATION_AUDIT_V2.md` | Métricas, controles e riscos residuais da adjudicação assistida | `8271FFD75831A893D923F2BC00FE76C184D6A199D8A1188C98BBBE62776578EF` |
| `FINAL_AUDIT_100_V2.md` | Auditoria conclusiva, critérios de atendimento e limites irredutíveis | `886B3535964D27E6126EA8A4595BB63DB7B1799BDAF01D6DB1839C9E06159B30` |
| `CORPUS_UNIVERSE_RECONCILIATION.csv` | Reconciliação das 408 linhas operacionais com 407 estudos publicados | `5AB47969E045625545421265D0E1E1C4F2BA308AA33AC4BF624B1A4DE7B77363` |
| `CORPUS_BORDERLINE_ADJUDICATION_V2.csv` | Readjudicação dos 17 casos de fronteira | `7E73EF73F5D15A75EC6AB51BF57B23D8E87A7EDA408FE2C8928319462DFBEC7E` |
| `CORPUS_RECONCILIATION_177.md` | Explicação auditável da reconciliação | `0064197DB5FFA396D676515239BEF29F67F808668AB9011C47F333CE7A5AE340` |
| `METHODS_SUPPLEMENT_V2.md` | Critérios completos, cobertura, verificação de evidências e controles metodológicos | `50F1231A7D5511FD4FD3CAEEFFAD5123AEDBE6A4ABE9DAF634233740BBE63A3B` |

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
