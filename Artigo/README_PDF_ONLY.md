# Área de leitura do artigo

Esta pasta usa PDF como formato operacional de revisão. Os DOCX foram retirados
após exportação textual para `texto_exportado/`.

- `Artigo_v2.1_para_leitura.pdf`: última renderização PDF disponível para leitura e anotações; conferir a data de renderização antes de tratar como cópia final.
- `Artigo_v2_final.pdf`: marco anterior da v2.
- `Artigo_original_v0.pdf`: fonte histórica do estudo.
- `Artigo_pre_auditoria.pdf`: estado preservado antes da auditoria.
- `texto_exportado/Artigo_v2.1_para_editar.md`: fonte textual oficial da consolidação editorial v2.1.
- `texto_exportado/`: memória textual em Markdown dos documentos editáveis e estados históricos.

Alterações futuras devem ser incorporadas ao gerador e renderizadas novamente
para PDF antes da revisão.

## Renderização final da v2.1

1. Executar `node tools/render_v21_markdown.js` para gerar a composição HTML reproduzível em `Artigo/v2.1_render.html`.
2. Imprimir `Artigo/v2.1_render.html` como PDF em `Artigo_v2.1_para_leitura.pdf`.
3. A Figura 1 é carregada de `Recursos_do_artigo/v2.1/imagens/Figura_1_modelo_de_cinco_camadas.png`; as sete figuras são centralizadas pelo CSS do gerador.
4. Conferir visualmente todas as páginas, o número de páginas, as chamadas de figuras/tabelas, o rodapé do catálogo e a equivalência textual com a fonte Markdown.

A renderização local não foi declarada como concluída quando o ambiente não disponibilizou um conversor DOCX/PDF. O PDF deve ser substituído somente após essa verificação visual.
