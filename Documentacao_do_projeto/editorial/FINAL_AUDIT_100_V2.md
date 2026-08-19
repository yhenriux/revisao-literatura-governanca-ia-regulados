# Auditoria final de atendimento ao parecer — v2

Data: 2026-08-19.

## Conclusão executiva

A v2 atende integralmente aos pontos acionáveis do parecer de Mauricio Almeida e alcança o máximo atendimento cientificamente defensável com os artefatos históricos disponíveis. A auditoria não atribui `100/100 absoluto`, porque dois dados de proveniência não foram preservados: os quantitativos por consulta/fonte e a matriz final de rótulos temáticos normalizados por estudo que originou parte das frequências gráficas. Preencher essas lacunas retroativamente produziria precisão fictícia.

Avaliação final: **98/100 — pronta para submissão, com limitações metodológicas explicitadas**.

## Matriz de critérios

| Critério derivado do parecer | Evidência verificada | Resultado |
|---|---|---|
| Modelo claramente apresentado como proposição derivada da síntese | Subseção “Status epistemológico do modelo”, nota da Tabela 6, discussão e conclusão | Atendido |
| Modelo ainda dependente de validação empírica | Manuscrito afirma que não é escala, norma ou certificação e propõe estudos de caso, especialistas e validação em sistemas reais | Atendido |
| Identidade inequívoca dos 177 estudos | Inventário individual com referência, classe, PDF, hash e evidência | Atendido |
| Evidência literal dos 177 estudos | `CORPUS_EVIDENCE_VERIFICATION_177.csv`: 177 verificados, zero pendências | Atendido |
| Fechamento dos 105 alertas históricos | 94 confirmações literais normalizadas e 11 evidências alternativas literais | Atendido |
| Reconciliação de 23 centrais e 154 de apoio | Inventário e workbook reproduzem `23 + 154 = 177` | Atendido |
| Limite de 25 resultados justificado | Método explica função operacional, viés de ordenação, truncamento e ausência de amostragem probabilística | Atendido |
| Cobertura parcial de Semantic Scholar e arXiv reconhecida | Método, discussão, suplemento e auditoria fonte × família | Atendido |
| Totais históricos por fonte/consulta | Logs não preservam retornados, armazenados, deduplicados ou incorporados por consulta; campos marcados como indisponíveis | Limitação histórica explicitada |
| Adjudicação por LLM descrita sem linguagem promocional | Auditoria registra entradas, JSON, validação literal, evidências inválidas, riscos e ausência de dupla revisão humana | Atendido |
| Redundância entre resultados, síntese e discussão | Recapitulação geral dos cinco achados removida; números concentrados; síntese integra e discussão interpreta | Atendido |
| Contestabilidade e reparo | Definição principal em 4.2; retomadas posteriores limitadas à interpretação e implicação | Atendido |
| Assimetria entre dimensões | Resultado quantitativo, integração na síntese e implicação na discussão exercem funções distintas | Atendido |
| Tabela 3 condensada | Quatro grupos de inclusão e quatro de exclusão no artigo; sete regras completas de cada tipo no suplemento | Atendido |
| Preservação do conteúdo científico | Sete figuras, três tabelas, 29 referências e números do corpus preservados | Atendido |
| Qualidade visual | PDF de 15 páginas, renderizado integralmente e inspecionado página a página | Atendido |
| Acessibilidade das figuras | Sete imagens com texto alternativo | Atendido |

## Auditoria das evidências

O inventário registra 105 alertas históricos: 101 ocorrências de `llm_evidence_not_found` e quatro combinações de conflito decisório com evidência não localizada. A conferência final adotou normalização Unicode, remoção de diferenças de diacríticos, espaços e pontuação, sem aproximação semântica para declarar correspondência literal.

- 94 âncoras históricas foram localizadas no texto integral após normalização;
- 11 âncoras não localizadas foram substituídas por trechos da matriz de evidências que aparecem literalmente no texto integral;
- nenhum estudo ficou sem evidência verificável;
- o estado histórico foi preservado separadamente do estado final;
- a existência literal do trecho não foi apresentada como concordância temática entre revisores humanos.

## Limites irredutíveis dos artefatos históricos

### Recuperação

Os logs preservados não contêm, por consulta e fonte, totais reportados pela API, retornados, armazenados, deduplicados, obtidos em texto completo ou incorporados ao corpus. A auditoria registra `não preservado` e `não atribuível` em vez de estimar valores.

### Frequências temáticas

O workbook mantém codificação temática original e matriz de evidências por estudo, enquanto `dados_figuras_v2.csv` mantém os totais publicados. Contudo, a matriz intermediária final de rótulos normalizados que liga individualmente cada estudo às oito famílias, às cinco camadas e aos cinco achados não foi preservada. Os totais não foram distribuídos retrospectivamente entre estudos apenas para reproduzir as frequências.

Esses dois limites justificam os dois pontos não atribuídos. Eles não impedem submissão, desde que permaneçam declarados e que os suplementos acompanhem o manuscrito.

## Verificação documental

- DOCX final: 184 parágrafos não vazios, três tabelas, sete imagens e sete textos alternativos.
- PDF final: 15 páginas A4.
- Inspeção visual: sem cortes, sobreposições, páginas vazias, tabelas partidas ou legendas isoladas.
- Workbook de reconciliação: quatro abas renderizadas; fórmulas reproduzem 177 estudos, 23 centrais, 154 de apoio, 105 alertas, 94 confirmações, 11 substituições e zero pendências.
- Varredura de fórmulas: nenhum `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?` ou `#N/A`.

## Recomendação

O artigo pode ser encaminhado aos professores e preparado para submissão. Uma declaração mais forte que `98/100` exigiria nova codificação temática independente dos 177 estudos e reconstrução prospectiva da recuperação bibliográfica; isso constituiria uma nova etapa metodológica, não mero ajuste editorial da v2.
