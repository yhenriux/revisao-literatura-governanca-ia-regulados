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

- Manuscrito integral original: `versoes_artigo/Governanca_Conversacional_v0.docx`.
- Manuscrito revisado limpo: `versoes_artigo/Governanca_Conversacional_v1.docx`.
- Manuscrito revisado e comentado: `versoes_artigo/Governanca_Conversacional_v1_redline.docx`.
- PDF revisado: `versoes_artigo/Governanca_Conversacional_v1.pdf`.
- Estado original da v1 antes da auditoria: arquivos `versoes_artigo/*_pre_auditoria.*`.

A tag `article-v1` preserva o primeiro fechamento. A tag `article-v1-final` identifica a correção definitiva dos próprios artefatos da v1, sem criação de v2.

## Índices de controle

- [Inventário de artefatos](project/ARTIFACT_INVENTORY.md)
- [Relatório de verificação da v1](editorial/QA_REPORT_V1.md)
