# Guia de reprodução e manutenção

## Pré-condições

- Trabalhar em branch própria para mudanças metodológicas.
- Registrar a versão do Python, dependências, modelo e configuração de execução.
- Usar credenciais apenas por variável de ambiente; nunca versioná-las.
- Preservar os arquivos originais e registrar SHA-256 de novos insumos.

## Fluxo controlado

1. Inventariar e identificar a proveniência dos insumos.
2. Executar consolidação e deduplicação com logs.
3. Congelar o universo antes da avaliação.
4. Registrar critérios e decisões de elegibilidade.
5. Executar extração e guardar indicadores de qualidade.
6. Executar triagem e adjudicação com saída estruturada.
7. Validar evidências contra o texto-fonte.
8. Normalizar códigos antes de quantificar.
9. Separar corpus analítico, referências contextuais e exclusões.
10. Gerar relatório de execução e versão do manuscrito correspondente.

## Controles de integridade

- Não modificar uma versão editorial fechada para refletir nova execução.
- Não misturar resultados de universos diferentes.
- Não interpretar frequência multirrótulo como categorias mutuamente exclusivas.
- Não tratar saída de LLM como decisão humana independente.
- Não remover PDFs ou logs históricos; classificar e preservar.

## Publicação

Cada marco deve incluir: artefatos, documentação, changelog, hash, commit, tag e verificação de correspondência entre local e remoto.

