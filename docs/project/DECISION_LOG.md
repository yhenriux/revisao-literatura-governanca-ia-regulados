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
- Resultado: 16.201 palavras na v0 e 8.095 na v1 completa, redução de 50,0%.

## ADR-004 — Separação artigo/suplemento

- Status: aceito.
- Decisão: manter no artigo apenas o necessário para avaliar rigor, validade e reprodutibilidade científica; mover detalhes de APIs, paginação, hashes, logs e implementação para o GitHub/suplemento.

## ADR-005 — Arquitetura narrativa

- Status: aceito.
- Decisão: reorganizar a v1 em Introdução, Trabalhos relacionados, Método, Resultados e modelo, Discussão e Conclusão.

## ADR-006 — Redline editorial

- Status: aceito.
- Decisão: produzir redline com alterações rastreadas nos marcos seccionais e comentários ancorados que explicam cada transformação estrutural; a matriz editorial oferece rastreabilidade detalhada.
