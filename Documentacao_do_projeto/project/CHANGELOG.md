# Changelog

## v2.1 — ciclo metodológico em validação humana (2026-08-22)

### Preparado

- Protocolo metodológico para responder aos seis pontos do terceiro parecer.
- Declaração verificável sobre a origem híbrida e iterativa das cinco camadas.
- Critério operacional de evidência central em três condições cumulativas.
- Fluxo explícito de adjudicação assistida por LLM com decisão final do autor.
- Planilha controlada para validar 177 estudos, JBI por desenho, CERQual por achado e busca complementar.
- Registro de 40 combinações prospectivas, posições e hashes de respostas.

### Resultado provisório da busca

- 1.342 ocorrências recuperadas nas fontes que responderam.
- 992 registros únicos não localizados entre os 407 registros históricos e ainda pendentes de decisão humana.
- PubMed e CORE bloqueados por configuração ausente; Semantic Scholar limitado por HTTP 429.

### Estado

- `aguardando_validacao_humana`.
- Nenhum DOCX, redline ou PDF final v2.1 foi publicado.
- Nenhuma tag `article-v2.1` foi criada.
- A v2 permanece o último marco científico fechado.

## v1 final — correção pós-auditoria

### Preservado

- Estado originalmente publicado da v1 em arquivos `pre_auditoria` e na tag imutável `article-v1`.
- V0 como autoridade científica e numérica.
- Sete figuras, três tabelas, 29 referências, achados e conclusões científicas.

### Corrigido

- Total reduzido de 8.095 para 7.906 palavras sem criar uma v2.
- Resultados condensados apenas por remoção de recapitulações e transcrições de gráficos.
- Fontes dos gráficos normalizadas para “corpus analítico”.
- Resumo e abstract simplificados e semanticamente equivalentes.
- Discussão ampliada de 323 para 734 palavras.
- Conclusão ampliada para 182 palavras.
- Distinção explícita entre evidência sintetizada e contribuição autoral.
- Trade-offs e implicações proporcionais ao risco desenvolvidos por setor.
- Redline reconstruída com 33 inserções, 33 exclusões e quatro comentários editoriais.
- Página final vazia da redline eliminada.

### Verificado

- Versão limpa com 16 páginas e redline com 19, todas inspecionadas.
- Sete textos alternativos e zero achados de acessibilidade.
- Equivalência de texto, tabelas e mídia após aceitação da redline.
- Ocorrências numéricas e construções defensivas dentro dos limites definidos.

### Controle de versão

- Preservação pré-auditoria: commit `1c71e1e`.
- Artefatos finais e geradores: commit `905d692`.
- Marco final: tag `article-v1-final`.

## v1 — revisão pós-parecer

### Adicionado

- Centro de documentação técnica, metodológica e editorial.
- Matriz de resposta ao parecer.
- Política de versionamento e registro de decisões.
- Suplemento metodológico e guia de reprodução.
- Manuscrito limpo, redline comentada e PDF da v1.

### Alterado em relação à v0

- Introdução condensada e orientada à contribuição.
- Trabalhos relacionados integrados pela lacuna.
- Método reduzido aos elementos de validade científica.
- Resultados aproximados do modelo conceitual.
- Discussão criada como seção autônoma.
- Conclusão reescrita sem recontagem metodológica.
- Repetições numéricas e justificativas defensivas reduzidas.

### Preservado

- Números oficiais e resultados da v0.
- Sete figuras utilizadas na narrativa científica.
- Referências bibliográficas.
- Arquivos integrais da v0.

# v2 — revisão metodológica após segundo parecer (2026-08-17)

- Criado inventário auditável dos 177 estudos e documento de reconciliação.
- Explicitado o status epistemológico do modelo de cinco camadas.
- Documentadas limitações da recuperação, da cobertura de fontes e da adjudicação assistida por LLM.
- Reconciliadas 408 linhas operacionais com 407 estudos publicados mediante documentação de uma duplicata exata.
- Readjudicados os 17 casos de fronteira em nove evidências de apoio, cinco referências contextuais e três exclusões.
- Condensada a Tabela 3 em quatro categorias de inclusão e quatro de exclusão, com as sete regras completas de cada tipo preservadas no suplemento.
- Reduzidas repetições entre resultados, síntese e discussão, sem alterar achados ou referências.
- Gerados DOCX final, DOCX editável, redline e PDF final de 15 páginas.
- Confirmadas três tabelas, sete figuras, 29 referências e equivalência da redline após aceitação.
- Auditoria de acessibilidade concluída sem achados; todas as páginas do PDF foram inspecionadas.
- Artefatos da v1 permanecem imutáveis e o estado anterior à correção foi marcado por tag própria.

## v2 final — redesign visual acadêmico (2026-08-18)

### Melhorado

- Redesenhadas as sete figuras em sistema visual acadêmico unificado, com rótulos diretos, marcadores redundantes e paleta compatível com leitura em escala de cinza.
- Substituídos o treemap setorial e o gráfico de bolhas por barras ordenadas e dot plot, preservando integralmente os valores publicados.
- Recompostas as três tabelas com larguras explícitas, alinhamento sem recuos indevidos, cabeçalhos discretos e fonte mínima de 8,5 pt.
- Reorganizado o fluxo dos Gráficos 5 e 6 para eliminar vazios excessivos sem fragmentar o conteúdo científico.
- Normalizados os rodapés pares e ímpares e iniciada a lista de referências em página própria.
- Elevada a bibliografia de 8 pt para 10 pt, melhorando a leitura de autoria, títulos e identificadores persistentes.

### Verificado

- PDF final mantido em 15 páginas A4.
- Sete imagens incorporadas a 359–361 dpi, todas com texto alternativo.
- Auditoria de acessibilidade concluída com zero achados altos, médios ou baixos.
- Teste em escala de cinza confirmou distinção por luminosidade, forma e rótulos, sem dependência exclusiva de cor.
- Todas as 15 páginas foram inspecionadas; não há cortes, sobreposições, tabelas quebradas ou paginação incorreta.
- O texto científico foi preservado, exceto por quatro descrições estritamente necessárias para refletir os novos formatos dos Gráficos 4 e 5.

## v2 final — contraste dos rótulos do Gráfico 6 (2026-08-19)

- Alterada exclusivamente a cor dos 40 valores internos do mapa de calor para branco.
- Preservados dados, escala cromática, dimensões, texto científico e todos os demais recursos visuais.
- Regeneradas as fontes SVG e PNG do Gráfico 6 e atualizados somente o DOCX e o PDF finais.
- Confirmadas 15 páginas, sete imagens com texto alternativo e auditoria de acessibilidade sem achados.
- A comparação visual com o marco anterior mostrou alteração somente na página 9.

## v2 final — restauração da Figura 1 histórica (2026-08-19)

- Restaurada a Figura 1 usada no marco `article-v2-final`, conforme preferência editorial do autor.
- Removidos o recorte herdado e a distorção de proporção; a imagem foi incorporada em sua razão original.
- Preservados o texto científico, os seis gráficos redesenhados e os 40 rótulos brancos do Gráfico 6.
- Mantidas 15 páginas, sete imagens com texto alternativo e auditoria de acessibilidade sem achados.
- O SVG da proposta visual substituída foi retirado do estado corrente para não representar falsamente a Figura 1 final; permanece recuperável no histórico Git.

## v2 final — fechamento metodológico dos alertas (2026-08-19)

- Examinados os 105 alertas históricos de localização de evidência: 94 âncoras confirmadas por normalização e 11 substituídas por evidência literal alternativa.
- Criada trilha auditável dos 177 estudos, com preservação do alerta original, método de verificação, trecho, página, arquivo e hash.
- Criada reconciliação em workbook entre identidade, classificação, codificação original e evidência, com fórmulas de controle e zero pendências.
- Explicitados, em matriz fonte × família, os quantitativos de recuperação que não foram preservados nos logs históricos.
- Acrescentada auditoria empírica da adjudicação assistida por LLM, sem equipará-la a dupla revisão humana independente.
- Reduzidas repetições residuais nos resultados e fortalecidas as limitações metodológicas no método e na discussão.
- Preservadas 15 páginas, sete figuras, três tabelas e 29 referências.

## v2.1 — fechamento metodológico e corpus analítico único (2026-08-23)

### Consolidado

- Fechado o corpus analítico único com 358 estudos: 30 evidências centrais e 328 evidências de apoio.
- Registradas 383 decisões integrais: 358 inclusões, 24 exclusões por escopo e uma versão redundante vinculada à publicação final.
- Criada matriz longa estudo–mecanismo–camada–achado para reproduzir todas as contagens do manuscrito e dos gráficos.
- Atualizado o catálogo bibliográfico público para representar somente o corpus analítico final.

### Fortalecido metodologicamente

- Documentada a recuperação ampliada em cinco fontes efetivas, com posições até o centésimo resultado, deduplicação e trilha de execução.
- Explicitada a origem iterativa das cinco camadas e afastada a interpretação circular das frequências.
- Formalizados três critérios cumulativos para evidência central e a distinção em relação à evidência de apoio.
- Descrito o fluxo de adjudicação assistida por LLM com decisão científica final do autor e ausência de dupla revisão independente.
- Delimitado o papel auxiliar de CASP/JBI e o uso interpretativo de CERQual.
- Mantido o modelo como proposição derivada da síntese, ainda dependente de validação empírica.

### Entregue e verificado

- Gerados DOCX limpo, PDF de leitura e redline completa entre v2 e v2.1.
- Preservadas sete figuras, três tabelas e a Figura 1 aprovada.
- PDF final mantido em 16 páginas; todas as páginas da versão limpa e da redline foram renderizadas e inspecionadas.
- Auditoria final concluída sem falhas de corpus, contagens, rastreabilidade, acessibilidade ou equivalência documental.
