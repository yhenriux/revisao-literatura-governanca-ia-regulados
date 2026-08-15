# Arquitetura da informação

## Classes documentais

### Manuscritos

Versões intelectuais do artigo. São imutáveis depois de declaradas como marco. Uma nova revisão recebe novo número de versão.

### Documentação editorial

Registra pareceres, decisões, critérios, cortes, migrações e evidências de atendimento. Não substitui o manuscrito.

### Documentação metodológica

Explica protocolo, busca, elegibilidade, extração, avaliação, síntese e limitações. Distingue validade científica de detalhes operacionais.

### Artefatos técnicos

Scripts, logs, hashes, planilhas, JSONs, PDFs e corpus textual que sustentam rastreabilidade e reprodução.

## Relações de proveniência

`v0` → parecer de Mauricio → checklist editorial → decisões registradas → `v1 redline` → `v1 limpa` → `v1 PDF`.

O corpus e os artefatos técnicos sustentam a revisão, mas não alteram automaticamente uma versão editorial já estabelecida. Divergências devem ser reconciliadas em decisão explícita e nova versão.

## Metadados mínimos

Cada novo marco deve registrar: título, versão, data, origem, responsável, finalidade, status, hash SHA-256 e commit Git.

