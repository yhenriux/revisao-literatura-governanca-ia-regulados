const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const source = path.join(root, 'Artigo', 'texto_exportado', 'Artigo_v2.2_para_editar.md');
const out = path.join(root, 'Artigo', 'v2.2_render.html');
const imageRoot = path.join(root, 'Recursos_do_artigo', 'v2.1', 'imagens');
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const inline = s => esc(s).replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/\*([^*]+)\*/g, '<em>$1</em>').replace(/`([^`]+)`/g, '<code>$1</code>');
const images = {
  'Figure 1': 'Grafico_1_composicao_do_corpus.png',
  'Figure 2': 'Grafico_2_familias_de_mecanismos.png',
  'Figure 3': 'Grafico_3_camadas_do_modelo.png',
  'Figure 4': 'Grafico_4_distribuicao_setorial.png',
  'Figure 5': 'Grafico_5_cobertura_dos_achados.png',
  'Figure 6': 'Grafico_6_coocorrencia_mecanismos_camadas.png',
  'Figure 7': 'Figura_1_modelo_de_cinco_camadas.png'
};
const lines = fs.readFileSync(source, 'utf8').split(/\r?\n/);
const tableBlocks = {};
for (let t = 1; t <= 3; t++) {
  const start = lines.findIndex(x => x.trim() === `## Table ${t}`);
  if (start < 0) continue;
  const block = [];
  for (let k = start + 1; k < lines.length && !/^##\s+Table\s+\d+/.test(lines[k].trim()); k++) block.push(lines[k]);
  tableBlocks[t] = block;
}
function renderTable(block = []) {
  const rows=[];
  for (const raw of block) {
    if (!/^\|/.test(raw.trim())) continue;
    const cells=raw.trim().replace(/^\||\|$/g,'').split('|').map(x=>inline(x.trim()));
    if (!cells.every(x=>/^:?-+$/.test(x.replace(/<[^>]+>/g,'')))) rows.push(cells);
  }
  return rows.length ? '<table><thead><tr>'+rows[0].map(x=>`<th>${x}</th>`).join('')+'</tr></thead><tbody>'+rows.slice(1).map(r=>'<tr>'+r.map(x=>`<td>${x}</td>`).join('')+'</tr>').join('')+'</tbody></table>' : '';
}
let html=[], i=0, inAppendix=false, inReferences=false;
while (i < lines.length) {
  const line=lines[i].trim();
  if (!line) {i++; continue;}
  if (/^##\s+Table\s+1$/.test(line)) {inAppendix=true;i++;continue;}
  if (inAppendix) {i++;continue;}
  const heading=line.match(/^(#{1,6})\s+(.+)$/);
  if (heading) {inReferences=/^References$/i.test(heading[2]); html.push(`<h${heading[1].length}>${inline(heading[2])}</h${heading[1].length}>`);i++;continue;}
  if (/^\|/.test(line) && i+1<lines.length && /^\|?\s*:?-+/.test(lines[i+1].trim())) {const b=[];while(i<lines.length&&/^\|/.test(lines[i].trim()))b.push(lines[i++]);html.push(renderTable(b));continue;}
  const caption=line.match(/^\*\*(Table\s+(1|2|3)|Figure\s+[1-7])\./);
  if (caption) {const label=caption[1]; if(label.startsWith('Table')) html.push(`<h3>${inline(line)}</h3>${renderTable(tableBlocks[Number(caption[2])])}`); else {const file=images[label];const data='data:image/png;base64,'+fs.readFileSync(path.join(imageRoot,file)).toString('base64');html.push(`<h3>${inline(line)}</h3><figure><img src="${data}" alt="${esc(line)}"></figure>`);}i++;continue;}
  if (/^(Note|Source)\./.test(line)) {html.push(`<p class="${line.startsWith('Note.')?'note':'source'}">${inline(line)}</p>`);i++;continue;}
  let p=[line];i++;while(i<lines.length&&lines[i].trim()&&!/^#/.test(lines[i])&&!/^\|/.test(lines[i].trim())&&!/^(\*\*)?(Note|Source|Table\s+[1-3]|Figure\s+[1-7])\./.test(lines[i].trim()))p.push(lines[i++].trim());
  html.push(`<p${inReferences?' class="reference"':''}>${inline(p.join(' '))}</p>`);
}
const css=`@page{size:A4;margin:17mm 18mm 17mm 20mm}body{font-family:Arial,Helvetica,sans-serif;color:#172033;font-size:9.6pt;line-height:1.3}h1{text-align:center;font-size:17pt;margin:0 0 13pt}h2{font-size:13pt;margin:14pt 0 6pt;border-bottom:1px solid #9aa7b7;padding-bottom:2pt}h3{font-size:10.8pt;margin:9pt 0 4pt}p{margin:0 0 5pt;text-align:justify}.reference{margin-left:12.7mm;text-indent:-12.7mm}table{width:100%;border-collapse:collapse;margin:7pt 0 9pt;font-size:8.5pt}th{background:#eaf0f4;font-weight:bold;text-align:left;border-top:1px solid #637789;border-bottom:1px solid #bcc9d2;padding:3.5pt}td{border-bottom:1px solid #d6dee5;padding:3.5pt;vertical-align:top}.note,.source{font-size:8pt;font-style:italic;text-align:left;margin:2pt 0 3pt}.source{font-style:normal}figure{margin:5pt auto 7pt;text-align:center;page-break-inside:avoid}figure img{max-width:100%;max-height:90mm;display:block;margin:0 auto}code{font-family:Consolas,monospace;font-size:8pt}@media print{h2,h3{break-after:avoid}table,figure{break-inside:avoid}}`;
fs.writeFileSync(out,`<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Conversational Governance in LLM-Based Systems</title><style>${css}</style></head><body>${html.join('\n')}</body></html>`,'utf8');
console.log(out);
