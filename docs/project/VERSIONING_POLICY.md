# Política de versionamento e preservação

## Regra principal

Arquivos históricos nunca são excluídos nem sobrescritos. Correções editoriais geram uma nova versão numerada.

## Convenção

- `v0`: versão integral submetida ao parecer.
- `v1`: revisão estrutural decorrente do parecer de Mauricio B. Almeida.
- `vN_redline`: cópia com alterações rastreadas e comentários editoriais.
- `vN`: cópia limpa do mesmo conteúdo aceito.
- PDF homônimo: representação de leitura verificada da versão limpa.

## Marcos Git

- Um commit para documentação e preparação editorial.
- Um commit para cada versão fechada do manuscrito.
- Tags anotadas `article-v0` e `article-v1`.
- Publicação na branch `main` somente após auditoria.

## Proibições

- Não reutilizar um número de versão para conteúdo diferente.
- Não substituir a v0 por uma versão reduzida.
- Não alterar números, amostras ou conclusões sem registro metodológico.
- Não apagar artefatos técnicos para “limpar” o repositório; classificá-los e documentá-los.

