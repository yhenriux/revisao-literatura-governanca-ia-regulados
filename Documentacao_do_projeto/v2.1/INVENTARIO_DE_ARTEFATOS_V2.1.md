# Inventário de artefatos — v2.1 em validação

Data do inventário: 22 de agosto de 2026.

Os hashes abaixo identificam o pacote entregue para validação humana. Eles deverão ser atualizados quando Yago devolver a planilha preenchida.

| Artefato | Função | Bytes | SHA-256 |
|---|---|---:|---|
| `Validacao_humana_do_corpus_v2.1.xlsx` | decisões humanas, JBI, CERQual e triagem prospectiva | 970.747 | `699de67031d560b4d4fb030e11bd4c0d04019e3b7059d41c4f2317cc8f152d72` |
| `PROTOCOLO_METODOLOGICO_V2.1.md` | regras científicas do ciclo | 4.407 | `fd7cced033c6257538a35cac4fdbec9bdd0e722eb63fbb68ced8b03af7699786` |
| `GUIA_DE_VALIDACAO_PARA_YAGO_V2.1.md` | instrução operacional ao único validador | 2.744 | `9752e6d6898da3dad3545b982bfadcf9cdfb9cc99c6d1bd009364318d9e26de2` |
| `DECLARACAO_ORIGEM_DAS_CAMADAS_V2.1.md` | confirmação factual do processo de codificação | 1.171 | `c0fdcdacb53508c1648417df21c51aa60ce62f46bc19b23520665d7530e2ba10` |
| `MATRIZ_DE_RESPOSTA_AO_PARECER_V2.1.md` | parecer → ação → evidência | 1.344 | `872dc72db751f278664b044d0f6a31a3182906546d320a0cbdec09b56de39bf9` |
| `CHECKLIST_DE_FECHAMENTO_V2.1.md` | portão de publicação | 1.483 | `62f9b7ec7376dcd381c538a34580246c98ae392db3db00b725d4c624f7570995` |
| `busca_de_sensibilidade/Registro_das_40_consultas_v2.1.csv` | contrato e estado das consultas | 18.322 | `a51366d712191abc1d126ecc5630f14d997c841d2c70a5b3a7f54e96b0eb0e26` |
| `busca_de_sensibilidade/Resultados_recuperados_v2.1.csv` | fila posicional completa | 2.703.046 | `92923c48ed85f3d56ce4cab7b8573336eb737cf187e7116f66575937e9a14a1f` |
| `busca_de_sensibilidade/Log_de_execucao_das_consultas_v2.1.csv` | execução, falhas e hashes por fonte/família | 13.559 | `aaedc1232833c218afefae4fe28229d5fa71e7e1b0afb2391b71342417575255` |
| `busca_de_sensibilidade/RELATORIO_DE_QUALIDADE_DA_BUSCA_V2.1.md` | diagnóstico de completude e riscos | 3.462 | `12d8f30cb31614466f42f4655ca6f997531edf998ee7eb066bcade7ebe5d7810` |
| `../../tools/search_sensitivity_v21.py` | reprodução da busca prospectiva | 25.446 | `e67fca75821c3adbafed14504dbad83d3d79e0ed40a29e7a101f2baa3d6bd0f6` |
| `../../tools/build_validation_workbook_v21.mjs` | reprodução da planilha | 21.710 | `882151bc63ca0a49670ad5efadf496199f6012cc45c76ad7cd0d4794dc1423ff` |

## Respostas brutas

As respostas brutas ficam em `busca_de_sensibilidade/respostas_brutas/`. Cada arquivo é identificado pelo hash registrado na linha correspondente de `Log_de_execucao_das_consultas_v2.1.csv`. Fontes bloqueadas ou falhas não possuem resposta bruta inventada.

## Triagem assistida de título e resumo

Esta etapa classifica prioridades de leitura, não incorpora estudos ao corpus. Os campos de decisão final do autor permanecem vazios nos 992 registros prospectivos.

| Artefato | Função | Bytes | SHA-256 |
|---|---|---:|---|
| `DECLARACAO_DO_AUTOR_SOBRE_CURADORIA_V2.1.md` | declaração do autor sobre a curadoria humana do corpus histórico | 1.008 | `c81c68a4725968de318ae9a13262f4509e1a09022fc85e9c72f56018fa587596` |
| `triagem_assistida/TRIAGEM_ASSISTIDA_DOS_REGISTROS_V2.1.csv` | decisões assistidas, critérios e fila de texto completo dos 992 registros | 2.147.283 | `abc007db24dcd8a3c172d39b9f341467945c307e335a06efca31e2c2280637ef` |
| `triagem_assistida/RELATORIO_DA_TRIAGEM_ASSISTIDA_V2.1.md` | síntese quantitativa da triagem | 1.031 | `5f1138703a0c16ea8db8989ba9cc3ffe3f29f836eefd618f5ef6aaf7be1b11ee` |
| `triagem_assistida/RELATORIO_DE_QUALIDADE_DA_TRIAGEM_V2.1.md` | controles, riscos e limites de interpretação | 4.287 | `040f93b4e28aeeb93ee09d08b7e527e1815ca748407c035f987c3ae865acaa3c` |
| `../../tools/triage_sensitivity_v21.py` | reprodução das regras de triagem assistida | 11.975 | `355dde4e5e8551d255b07b06066d165071d3d0c63020fc4905917a79be09177f` |

## Artefatos ainda não existentes

O DOCX limpo, a redline, o PDF e a tag `article-v2.1` ainda não existem. Sua criação depende do fechamento humano e da reconciliação científica.

## Acervo prospectivo de textos completos abertos

| Artefato | Função | Bytes | SHA-256 |
|---|---|---:|---|
| `../../arquivos_tratados_aigovernanca/ft_v21/MANIFESTO_TEXTOS_COMPLETOS_V2.1.csv` | reconciliação dos 575 registros com PDFs, URLs, licenças e falhas | 237.293 | `2c29d01d60d9bc2f5e0e09f8e5f652eded6f36abe43d5b72449cb332e6c95125` |
| `../../arquivos_tratados_aigovernanca/ft_v21/LEIA_ME.md` | síntese do acervo e controle estrutural | 980 | `ac3f69fafa6c0b9fef2e58461da0b5c4399390c7e04d7ea9e4da38621c8a6c0d` |
| `../../tools/retrieve_open_fulltexts_v21.py` | resolução reproduzível de cópias abertas | 11.356 | `4cf83b5571034ea1494b9b0d6c8ae9dacb5e749a96fea534fa3f77d955805277` |

Os 223 PDFs totalizam 292.924.414 bytes e possuem hashes individuais no manifesto. Todos foram abertos estruturalmente: 4.439 páginas, zero PDFs inválidos e zero duplicatas binárias.

## Triagem integral — primeira rodada dos candidatos centrais

| Artefato | Função | Bytes | SHA-256 |
|---|---|---:|---|
| `triagem_texto_completo/FILA_DE_TRIAGEM_INTEGRAL_CENTRAIS_V2.1.jsonl` | texto extraído por página e campos estruturados dos 17 PDFs centrais | 220.495 | `92d9180ddf43a0ae372e2a0838beefa06dc5f230d66a8acd2398411d115724ef` |
| `triagem_texto_completo/RELATORIO_DA_EXTRAÇÃO_INTEGRAL_CENTRAIS_V2.1.md` | controle de extração: 17 PDFs, 400 páginas | 1.191 | `00ee3ee47ce128fc8bdb26611627c396270479eb9d3762fa9a53ab8417023ab3` |
| `triagem_texto_completo/DECISOES_ASSISTIDAS_CENTRAIS_V2.1.md` | classificação assistida e justificativas por estudo | 5.253 | `5893def820d66f7ed9c22b9b45ae97a1d364875df1ea2812447b712a9e19613a` |
| `../../tools/extract_fulltext_triage_v21.py` | reprodução da extração por página | 4.278 | `c6fd1e3fd199cc2c83da2701805721f3aa858f063f3e410375953133ac1cbb8b` |

| `triagem_texto_completo/FILA_DE_TRIAGEM_INTEGRAL_APOIO_V2.1.jsonl` | texto extraído por página dos 77 candidatos de apoio | 999.337 | `1121721bbcfc02c32c8496d34a6d16cf8afac8c9886e02885c32f38d6499b090` |
| `triagem_texto_completo/RELATORIO_DA_EXTRAÇÃO_INTEGRAL_APOIO_V2.1.md` | controle da extração dos 77 PDFs e 1.530 páginas | 4.133 | `f57cbc5bf39ca86bd1d9e47d6f0af33fb9a840a280ef55cc30a0fd05165cfb90` |
| `triagem_texto_completo/FILA_DE_TRIAGEM_INTEGRAL_INCERTOS_V2.1.jsonl` | texto extraído por página dos 129 registros incertos | 1.533.382 | `b9adb4e19008d9a2c2a279caa0a5b69edfe08014e28e287292ffe1ffc61635eb` |
| `triagem_texto_completo/RELATORIO_DA_EXTRAÇÃO_INTEGRAL_INCERTOS_V2.1.md` | controle da extração dos 129 PDFs e 2.509 páginas | 6.705 | `477cfbd92d6d961d106e6ab8068261389ab7b1fdf3f5a48a22bcb495cd3c4c9d` |
