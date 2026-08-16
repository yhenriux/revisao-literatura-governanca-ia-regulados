# Centro de documentação do projeto

Este diretório reúne a documentação técnica, metodológica e editorial da revisão sistemática sobre governança conversacional em sistemas baseados em LLMs em ambientes regulados.

## Organização

- `project/`: visão geral, arquitetura documental, política de versionamento e decisões.
- `editorial/`: parecer, checklist, matriz de resposta e relatório comparativo da v1.
- `methodology/`: suplemento metodológico e guia de reprodução/manutenção.

## Princípios de governança

1. Nenhuma versão publicada de um artefato é sobrescrita ou excluída.
2. A v0 é a fonte de verdade para números e resultados da revisão editorial v1.
3. Mudanças editoriais não podem alterar evidências ou conclusões sem decisão registrada.
4. Dados ativos, derivados, documentação e manuscritos têm funções distintas e devem permanecer identificáveis.
5. Todo marco editorial recebe versão de arquivo, commit e tag Git.

## Artefatos principais

- Manuscrito integral original: `01_ARTIGO__VERSOES/ARTIGO__T-v0__FONTE.docx`.
- Manuscrito revisado limpo: `01_ARTIGO__VERSOES/ARTIGO__T-v1__EDICAO.docx`.
- Manuscrito revisado e comentado: `01_ARTIGO__VERSOES/ARTIGO__T-v1__REDLINE.docx`.
- PDF revisado: `01_ARTIGO__VERSOES/ARTIGO__T-v1__LEITURA.pdf`.
- Estado original da v1 antes da auditoria: arquivos `01_ARTIGO__VERSOES/ARTIGO__T-v1-pre-auditoria__*`.

A tag `article-v1` preserva o primeiro fechamento. A tag `article-v1-final` identifica a correção definitiva dos próprios artefatos da v1, sem criação de v2.

## Rotas rápidas

- Para enviar o artigo: `../01_ARTIGO__VERSOES/ARTIGO__T-v1__LEITURA.pdf`.
- Para entender o histórico: `editorial/QA_REPORT_V1.md` e `project/CHANGELOG.md`.
- Para reproduzir ou manter o corpus: `methodology/REPRODUCIBILITY_GUIDE.md`.
- Para registrar uma nova decisão: `project/DECISION_LOG.md`.

## Índices de controle

- [Inventário de artefatos](project/ARTIFACT_INVENTORY.md)
- [Relatório de verificação da v1](editorial/QA_REPORT_V1.md)
- [Arquitetura facetada PMEST](project/RANGANATHAN_FACETED_ARCHITECTURE.md)
