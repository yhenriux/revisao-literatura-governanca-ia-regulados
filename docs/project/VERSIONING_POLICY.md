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
- Não criar uma nova versão apenas para corrigir formatação, atualizar documentação ou regenerar um artefato equivalente. Essas mudanças devem ser registradas no histórico do marco corrente, quando autorizadas.
- Não usar nomes como `final_final`, `novo`, `corrigido2` ou equivalentes ambíguos.

## Mensagens de commit

Use mensagens curtas, orientadas ao efeito da mudança:

- `article:` para manuscritos e PDFs;
- `docs:` para documentação editorial ou técnica;
- `audit:` para verificações e relatórios de QA;
- `corpus:` para dados e inventários do corpus;
- `build:` para artefatos regenerados por ferramentas.

Exemplos: `docs: atualizar matriz de resposta ao parecer` e `audit: registrar verificação de acessibilidade`.

## Política de limpeza

O Git deve conter versões oficiais, documentação necessária à proveniência, corpus/derivados necessários à reprodução e ferramentas usadas para gerar ou verificar artefatos. Renders PNG temporários, caches, logs locais, cópias de download e intermediários não reproduzíveis devem permanecer fora do repositório.

