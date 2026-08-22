# Guia de validação humana — Yago

Este é o único trabalho científico que não pode ser delegado a automação. A planilha organiza as decisões, mas não decide por você.

## Antes de abrir a planilha

1. Leia a declaração em `DECLARACAO_ORIGEM_DAS_CAMADAS_V2.1.md`.
2. Se ela reproduzir o processo real, marque a confirmação, informe a data e assine.
3. Se não reproduzir, corrija a declaração antes de validar o corpus.

## Na planilha

Abra `Validacao_humana_do_corpus_v2.1.xlsx` e siga a aba `LEIA-ME`. Preencha somente as células amarelas.

### 1. Validacao_177

Trabalhe em lotes de 25. Para cada estudo:

1. confirme elegibilidade;
2. julgue separadamente C1, C2 e C3;
3. classifique como central, apoio, excluir ou incerto;
4. registre justificativa, trecho e página;
5. confirme setor, mecanismos e incidência nas cinco camadas;
6. marque `confirmado` somente depois de revisar o texto necessário.

Evidência central exige C1, C2 e C3 iguais a `sim`. Não consulte `Referencia_LLM` antes da primeira decisão.

### 2. Referencia_LLM

Depois da primeira decisão humana, compare o seu julgamento ao histórico. Divergências não são erro automático: volte ao texto integral, decida e justifique. A classificação final continua sendo sua.

### 3. Avaliacao_JBI

Avalie os estudos que você confirmar como centrais. Confirme primeiro o desenho e o instrumento; depois preencha os itens do checklist oficial adequado. Não some itens de desenhos distintos em um escore único.

### 4. CERQual_achados

Avalie a confiança no nível de cada achado qualitativo compatível. Se o achado for apenas quantitativo ou incompatível com CERQual, marque `não aplicável` e explique.

### 5. Triagem_novos

Filtre `Status = pendente`. Os registros históricos e as duplicatas já estão marcados como `não_aplicável`.

Para cada registro pendente:

1. julgue título e resumo;
2. para `incluir` ou `incerto`, consulte o texto completo;
3. registre decisão e justificativa;
4. se incluir, classifique como central ou apoio;
5. marque `confirmado` apenas ao concluir a decisão.

Comece pelos 314 registros de prioridade automática alta. A prioridade apenas ordena o trabalho; não autoriza exclusão automática.

## Critério de término

A aba `Resumo` só exibirá `PRONTO PARA RECONCILIAÇÃO` quando houver:

- 177 validações históricas confirmadas;
- nenhuma validação histórica pendente;
- avaliação JBI para todas as evidências humanas centrais;
- cinco decisões CERQual concluídas ou justificadamente não aplicáveis;
- nenhuma triagem nova pendente.

Salve a planilha sem renomeá-la e devolva o mesmo arquivo. A partir dela serão recalculados corpus, PRISMA, gráficos, tabelas e texto da v2.1.
