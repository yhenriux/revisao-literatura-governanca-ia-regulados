# Centro de documentação do projeto

Este diretório reúne a documentação técnica, metodológica e editorial da revisão sistemática sobre governança conversacional em sistemas baseados em LLMs em ambientes regulados.

## Organização

- `project/`: visão geral, arquitetura documental, política de versionamento e decisões.
- `editorial/`: parecer, checklist, matriz de resposta e relatório comparativo da v1.
- `methodology/`: suplemento metodológico e guia de reprodução/manutenção.
- `v2.1/`: protocolo, planilha e busca prospectiva do ciclo metodológico atualmente em validação humana.

## Princípios de governança

1. Nenhuma versão publicada de um artefato é sobrescrita ou excluída.
2. A v0 é a fonte de verdade para números e resultados da revisão editorial v1.
3. Mudanças editoriais não podem alterar evidências ou conclusões sem decisão registrada.
4. Dados ativos, derivados, documentação e manuscritos têm funções distintas e devem permanecer identificáveis.
5. Todo marco editorial recebe versão de arquivo, commit e tag Git.

## Artefatos principais e estado atual

- Manuscrito integral original: `../Artigo/Artigo_original_v0.docx`.
- PDF científico corrente e aprovado antes do novo parecer: `../Artigo/Artigo_v2_final.pdf`.
- DOCX científico corrente: `../Artigo/Artigo_v2_final.docx`.
- Estado original da v1 antes da auditoria: arquivos `../Artigo/Artigo_pre_auditoria_*`.

A v2.1 está em **validação humana**. Ainda não existe PDF final v2.1, pois corpus, JBI, CERQual e busca de sensibilidade dependem de decisões científicas de Yago. O ponto de entrada é `v2.1/LEIA_PRIMEIRO_V2.1.md`.

As tags das versões anteriores permanecem imutáveis. A tag `article-v2.1` só será criada depois do fechamento integral do checklist humano e documental.

## Rotas rápidas

- Para ler o último artigo fechado: `../Artigo/Artigo_v2_final.pdf`.
- Para trabalhar na v2.1: `v2.1/LEIA_PRIMEIRO_V2.1.md` e `v2.1/Validacao_humana_do_corpus_v2.1.xlsx`.
- Para entender o histórico: `editorial/QA_REPORT_V1.md` e `project/CHANGELOG.md`.
- Para reproduzir ou manter o corpus: `methodology/REPRODUCIBILITY_GUIDE.md`.
- Para registrar uma nova decisão: `project/DECISION_LOG.md`.

## Índices de controle

- [Inventário de artefatos](project/ARTIFACT_INVENTORY.md)
- [Relatório de verificação da v1](editorial/QA_REPORT_V1.md)
- [Arquitetura facetada PMEST](project/RANGANATHAN_FACETED_ARCHITECTURE.md)
