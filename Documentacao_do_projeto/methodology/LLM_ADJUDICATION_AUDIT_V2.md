# Auditoria do procedimento de adjudicação assistida por LLM — v2

## Escopo e resultado empírico

A auditoria cobre 408 linhas operacionais do workbook do pipeline. O processamento registrou 3601 evidências validadas e 627 evidências rejeitadas; 259 registros tiveram ao menos uma evidência inválida. 301 registros foram sinalizados pelo próprio fluxo para verificação manual e 149 aparecem com estado de auditoria `checked`. Esses números descrevem controles do pipeline e não demonstram concordância entre revisores humanos independentes.

## Controles e riscos residuais

| Etapa | Controle observado | Risco residual |
|---|---|---|
| Triagem determinística | termos, regras, páginas e trechos candidatos | falsos positivos e negativos por vocabulário ou extração |
| Adjudicação assistida | saída JSON estruturada, decisão e justificativa | interpretação contextual, enquadramento e dependência do modelo |
| Validação de evidência | confronto literal com o texto extraído e contagem de evidências inválidas | hifenização, Unicode, falhas de OCR e localização |
| Auditoria final da v2 | 177 estudos confrontados com texto integral; 105 alertas históricos examinados, sendo 94 âncoras confirmadas por normalização e 11 substituídas por evidência literal alternativa | não equivale a dupla codificação humana independente |
| Síntese | separação entre evidência central, apoio, contextual e exclusão | dependência das decisões anteriores e da taxonomia adotada |

## Interpretação permitida

O LLM foi um instrumento auxiliar de escala e estruturação. Sua confiança numérica não é probabilidade calibrada, e o fluxo não deve ser descrito como revisão humana independente em duplicata. A confirmação literal demonstra que o trecho existe no texto integral; não prova, isoladamente, que a interpretação temática seja a única possível.

## Proveniência

Fonte: abas `records_flat` e `evidence_matrix` de `metagrade_python_llm_workbook.xlsx`, inventário dos 177 estudos e repositório de texto integral. Gerado em 2026-08-19.
