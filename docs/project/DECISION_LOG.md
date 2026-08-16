# Registro de decisões

## ADR-001 — Imutabilidade da v0

- Status: aceito.
- Decisão: preservar DOCX e PDF da v0 sem qualquer modificação.
- Justificativa: garantir proveniência, comparação editorial e integridade científica.

## ADR-002 — Autoridade numérica

- Status: aceito.
- Decisão: usar os números da v0 como fonte de verdade da revisão v1.
- Consequência: divergências com documentos operacionais são registradas como diferença de estado/escopo, não corrigidas silenciosamente.

## ADR-003 — Redução estrutural

- Status: aceito.
- Decisão: reduzir o manuscrito aproximadamente à metade, preservando resultados, modelo, discussão e contribuição.
- Resultado: o primeiro fechamento alcançou 8.095 palavras; a correção pós-auditoria encerrou a v1 com 7.906 palavras, redução de 51,2% em relação às 16.201 da v0.

## ADR-004 — Separação artigo/suplemento

- Status: aceito.
- Decisão: manter no artigo apenas o necessário para avaliar rigor, validade e reprodutibilidade científica; mover detalhes de APIs, paginação, hashes, logs e implementação para o GitHub/suplemento.

## ADR-005 — Arquitetura narrativa

- Status: aceito.
- Decisão: reorganizar a v1 em Introdução, Trabalhos relacionados, Método, Resultados e modelo, Discussão e Conclusão.

## ADR-006 — Redline editorial

- Status: aceito.
- Decisão: produzir redline com alterações rastreadas nos marcos seccionais e comentários ancorados que explicam cada transformação estrutural; a matriz editorial oferece rastreabilidade detalhada.

## ADR-007 — Correção interna da v1

- Status: aceito.
- Decisão: corrigir os artefatos oficiais da v1 sem criar v2.
- Justificativa: os desvios foram introduzidos na própria elaboração da v1 e não representam novo corpus, nova busca ou nova contribuição científica.
- Consequência: a versão antes publicada permanece recuperável como `pre_auditoria` e pela tag `article-v1`; a corrente recebe a tag `article-v1-final`.

## ADR-008 — Regra de evidência e proposição

- Status: aceito.
- Decisão: reservar formulações como “a revisão identificou” para a síntese da literatura e “o modelo propõe” para a contribuição autoral.
- Consequência: o modelo é apresentado como estrutura analítica sujeita a validação empírica, não como escala de maturidade, evidência de efetividade ou substituto de normas setoriais.

## ADR-009 — Critério de equivalência da redline

- Status: aceito.
- Decisão: considerar equivalentes a versão limpa e a redline aceita quando coincidirem os parágrafos não vazios, as tabelas e os objetos de mídia.
- Resultado: equivalência confirmada em 183 parágrafos não vazios, três tabelas e sete imagens; 33 inserções e 33 exclusões permaneceram rastreáveis antes da aceitação.
