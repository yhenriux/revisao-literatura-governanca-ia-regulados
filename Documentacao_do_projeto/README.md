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

- Manuscrito integral original: `../Artigo/Artigo_original_v0.docx`.
- Manuscrito revisado limpo: `../Artigo/Artigo_para_editar.docx`.
- Manuscrito revisado e comentado: `../Artigo/Artigo_com_alteracoes.docx`.
- PDF revisado: `../Artigo/Artigo_final.pdf`.
- Estado original da v1 antes da auditoria: arquivos `../Artigo/Artigo_pre_auditoria_*`.

A tag `article-v1` preserva o primeiro fechamento. A tag `article-v1-final` identifica a correção definitiva dos próprios artefatos da v1, sem criação de v2.

## Rotas rápidas

- Para enviar o artigo: `../Artigo/Artigo_final.pdf`.
- Para entender o histórico: `editorial/QA_REPORT_V1.md` e `project/CHANGELOG.md`.
- Para reproduzir ou manter o corpus: `methodology/REPRODUCIBILITY_GUIDE.md`.
- Para registrar uma nova decisão: `project/DECISION_LOG.md`.

## Índices de controle

- [Inventário de artefatos](project/ARTIFACT_INVENTORY.md)
- [Relatório de verificação da v1](editorial/QA_REPORT_V1.md)
- [Arquitetura facetada PMEST](project/RANGANATHAN_FACETED_ARCHITECTURE.md)
