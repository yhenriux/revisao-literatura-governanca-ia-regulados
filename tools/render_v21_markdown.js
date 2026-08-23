const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const source = path.join(root, 'Artigo', 'texto_exportado', 'Artigo_v2.1_para_editar.md');
const out = path.join(root, 'Artigo', 'v2.1_render.html');
const imageRoot = path.join(root, 'Recursos_do_artigo', 'v2.1', 'imagens');
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const inline = s => esc(s).replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/\*([^*]+)\*/g, '<em>$1</em>').replace(/`([^`]+)`/g, '<code>$1</code>');
const imageByLabel = {
  'Gráfico 1': 'Grafico_1_composicao_do_corpus.png',
  'Gráfico 2': 'Grafico_2_familias_de_mecanismos.png',
  'Gráfico 3': 'Grafico_3_camadas_do_modelo.png',
  'Gráfico 4': 'Grafico_4_distribuicao_setorial.png',
  'Gráfico 5': 'Grafico_5_cobertura_dos_achados.png',
  'Gráfico 6': 'Grafico_6_coocorrencia_mecanismos_camadas.png',
  'Figura 1': 'Figura_1_modelo_de_cinco_camadas.png'
};
const lines = fs.readFileSync(source, 'utf8').split(/\r?\n/).slice(3);
// As tabelas são armazenadas no Markdown como blocos finais para facilitar edição.
// Aqui elas são indexadas e reinseridas no ponto editorial de cada chamada.
const tableBlocks = {};
for (let t = 1; t <= 3; t++) {
  const start = lines.findIndex(x => x.trim() === `## Tabela ${t}`);
  if (start < 0) continue;
  const block = [];
  for (let k = start + 1; k < lines.length && !/^##\s+Tabela\s+\d+/.test(lines[k].trim()); k++) block.push(lines[k]);
  tableBlocks[t] = block;
}
let html = [];
let i = 0;
let firstContent = true;
let inTableAppendix = false;
while (i < lines.length) {
  const line = lines[i].trim();
  if (!line) { i++; continue; }
  if (/^##\s+Tabela\s+1$/.test(line)) { inTableAppendix = true; i++; continue; }
  if (inTableAppendix) { i++; continue; }
  if (firstContent) { html.push(`<h1>${inline(line)}</h1>`); firstContent = false; i++; continue; }
  if (/^(Resumo|Abstract)$/.test(line)) { html.push(`<h2>${inline(line)}</h2>`); i++; continue; }
  if (/^\|/.test(line) && i + 1 < lines.length && /^\|?\s*:?-+/.test(lines[i+1].trim())) {
    const rows = [];
    while (i < lines.length && /^\|/.test(lines[i].trim())) {
      const cells = lines[i].trim().replace(/^\||\|$/g, '').split('|').map(x => inline(x.trim()));
      if (!cells.every(x => /^:?-+$/.test(x.replace(/<[^>]+>/g, '')))) rows.push(cells);
      i++;
    }
    html.push('<table><thead><tr>' + rows[0].map(x => `<th>${x}</th>`).join('') + '</tr></thead><tbody>' + rows.slice(1).map(r => '<tr>' + r.map(x => `<td>${x}</td>`).join('') + '</tr>').join('') + '</tbody></table>');
    continue;
  }
  const heading = line.match(/^(#{1,6})\s+(.+)$/);
  if (heading) { const n = heading[1].length; html.push(`<h${n}>${inline(heading[2])}</h${n}>`); i++; continue; }
  const tableCaption = line.match(/^Tabela\s+(2|3|6)\./);
  if (tableCaption) {
    const sourceNumber = ({2: 1, 3: 2, 6: 3})[tableCaption[1]];
    const rows = [];
    const block = tableBlocks[sourceNumber] || [];
    for (const raw of block) {
      if (!/^\|/.test(raw.trim())) continue;
      const cells = raw.trim().replace(/^\||\|$/g, '').split('|').map(x => inline(x.trim()));
      if (!cells.every(x => /^:?-+$/.test(x.replace(/<[^>]+>/g, '')))) rows.push(cells);
    }
    if (rows.length) html.push(`<h3>${inline(line)}</h3><table><thead><tr>${rows[0].map(x => `<th>${x}</th>`).join('')}</tr></thead><tbody>${rows.slice(1).map(r => '<tr>' + r.map(x => `<td>${x}</td>`).join('') + '</tr>').join('')}</tbody></table>`);
    i++; continue;
  }
  const visual = line.match(/^(Gráfico [1-6]|Figura 1)\./);
  if (visual) {
    html.push(`<h3>${inline(line)}</h3>`);
    const img = path.join(imageRoot, imageByLabel[visual[1]]).replace(/\\/g, '/');
    const dataUri = 'data:image/png;base64,' + fs.readFileSync(img).toString('base64');
    html.push(`<figure><img src="${dataUri}" alt="${esc(line)}"></figure>`);
    i++; continue;
  }
  if (/^Nota\./.test(line)) { html.push(`<p class="note">${inline(line)}</p>`); i++; continue; }
  if (/^Fonte\./.test(line)) { html.push(`<p class="source">${inline(line)}</p>`); i++; continue; }
  let para = [line]; i++;
  while (i < lines.length && lines[i].trim() && !/^#/.test(lines[i]) && !/^\|/.test(lines[i].trim()) && !/^(Nota|Fonte|Gráfico [1-6]|Figura 1)\./.test(lines[i].trim())) { para.push(lines[i].trim()); i++; }
  html.push(`<p>${inline(para.join(' '))}</p>`);
}
const css = `@page{size:A4;margin:17mm 18mm 17mm 20mm}body{font-family:Arial,Helvetica,sans-serif;color:#172033;font-size:9.6pt;line-height:1.3}h1{text-align:center;font-size:17pt;margin:0 0 13pt}h2{font-size:13pt;margin:14pt 0 6pt;border-bottom:1px solid #9aa7b7;padding-bottom:2pt}h3{font-size:10.8pt;margin:9pt 0 4pt}p{margin:0 0 5pt;text-align:justify}table{width:100%;border-collapse:collapse;margin:7pt 0 9pt;font-size:8.5pt}th{background:#eaf0f4;font-weight:bold;text-align:left;border-top:1px solid #637789;border-bottom:1px solid #bcc9d2;padding:3.5pt}td{border-bottom:1px solid #d6dee5;padding:3.5pt;vertical-align:top}.note,.source{font-size:8pt;font-style:italic;text-align:left;margin:2pt 0 3pt}.source{font-style:normal}figure{margin:5pt auto 7pt;text-align:center;page-break-inside:avoid}figure img{max-width:100%;max-height:90mm;display:block;margin:0 auto}figcaption{font-size:8.4pt;font-weight:bold;margin-top:2pt}code{font-family:Consolas,monospace;font-size:8pt}@media print{h2,h3{break-after:avoid}table,figure{break-inside:avoid}}`;
const documentTitle = 'Governança Conversacional em Sistemas Baseados em Modelos de Linguagem de Grande Escala em Ambientes Regulados';
fs.writeFileSync(out, `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>${documentTitle}</title><style>${css}</style></head><body>${html.join('\n')}</body></html>`, 'utf8');
console.log(out);
