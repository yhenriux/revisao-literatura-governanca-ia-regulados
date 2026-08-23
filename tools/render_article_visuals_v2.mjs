/** Gera os seis gráficos acadêmicos da v2 em SVG e PNG (360 dpi).
 * A Figura 1 é o PNG histórico restaurado do marco article-v2-final e não é regenerada.
 */
import { createRequire } from "node:module";
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";

const require = createRequire(import.meta.url);
const sharp = require("sharp");
const ROOT = path.resolve(process.env.REV_LIT_ROOT || process.cwd());
const VERSION = process.env.ARTICLE_VISUAL_VERSION || "v2";
const DATA_NAME = VERSION === "v2" ? "dados_figuras_v2.csv" : `dados_figuras_${VERSION.replaceAll(".", "")}.csv`;
const DATA = path.join(ROOT, "Recursos_do_artigo", VERSION, DATA_NAME);
const PNG_DIR = path.join(ROOT, "Recursos_do_artigo", VERSION, "imagens");
const SVG_DIR = path.join(ROOT, "Recursos_do_artigo", VERSION, "fontes_vetoriais");

const C = {
  blue: "#176B87", dark: "#124B61", light: "#B9D4DE", orange: "#D97706",
  gray: "#A7B0B7", pale: "#E7ECEF", grid: "#D7E0E5", text: "#24343D", white: "#FFFFFF",
};

const files = [
  ["Grafico_1_composicao_do_corpus", 443, 130],
  ["Grafico_2_familias_de_mecanismos", 443, 248],
  ["Grafico_3_camadas_do_modelo", 443, 198],
  ["Grafico_4_distribuicao_setorial", 443, 234],
  ["Grafico_5_cobertura_dos_achados", 443, 198],
  ["Grafico_6_coocorrencia_mecanismos_camadas", 443, 256],
];

const esc = (s) => String(s).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
const attrs = (o) => Object.entries(o).map(([k,v]) => `${k}="${esc(v)}"`).join(" ");
const line = (x1,y1,x2,y2,stroke=C.grid,width=1,extra={}) => `<line ${attrs({x1,y1,x2,y2,stroke,"stroke-width":width,...extra})}/>`;
const rect = (x,y,w,h,fill,rx=0,stroke="none",sw=0) => `<rect ${attrs({x,y,width:w,height:h,fill,rx,stroke,"stroke-width":sw})}/>`;
const circle = (cx,cy,r,fill,stroke=C.white,sw=0.8) => `<circle ${attrs({cx,cy,r,fill,stroke,"stroke-width":sw})}/>`;
const diamond = (cx,cy,r,fill) => `<polygon ${attrs({points:`${cx},${cy-r} ${cx+r},${cy} ${cx},${cy+r} ${cx-r},${cy}`,fill,stroke:C.white,"stroke-width":0.8})}/>`;
function text(x,y,value,size=8.5,anchor="start",fill=C.text,weight=400,extra={}) {
  return `<text ${attrs({x,y,"font-size":size,"text-anchor":anchor,fill,"font-weight":weight,...extra})}>${esc(value)}</text>`;
}
function multiline(x,y,value,size=8.5,anchor="start",fill=C.text,weight=400,lineHeight=10) {
  const rows=String(value).split("\n");
  const start=y-((rows.length-1)*lineHeight)/2;
  return `<text ${attrs({x,y:start,"font-size":size,"text-anchor":anchor,fill,"font-weight":weight})}>${rows.map((r,i)=>`<tspan x="${x}" dy="${i?lineHeight:0}">${esc(r)}</tspan>`).join("")}</text>`;
}
function svg(w,h,body,defs="") {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}"><defs>${defs}</defs><style>text{font-family:Arial,Helvetica,sans-serif} .axis{shape-rendering:crispEdges}</style><rect width="100%" height="100%" fill="#fff"/>${body}</svg>`;
}
function parseCsv(raw) {
  raw=raw.replace(/^\uFEFF/,"");
  const records=[];let record=[],field="",quoted=false;
  for(let i=0;i<raw.length;i++){
    const ch=raw[i];
    if(ch==='"'){
      if(quoted&&raw[i+1]==='"'){field+='"';i++;}else quoted=!quoted;
    }else if(ch===','&&!quoted){record.push(field);field="";
    }else if((ch==='\n'||ch==='\r')&&!quoted){
      if(ch==='\r'&&raw[i+1]==='\n')i++;
      record.push(field);field="";if(record.some(v=>v!==""))records.push(record);record=[];
    }else field+=ch;
  }
  if(field||record.length){record.push(field);records.push(record);}
  const [keys,...rows]=records;
  return rows.map(values=>Object.fromEntries(values.map((value,index)=>[
    keys[index], index===1||index===4?Number(value):value
  ])));
}
const group=(rows,id)=>rows.filter(r=>r.figura===id).sort((a,b)=>a.ordem-b.ordem);
const categories=(rows)=>[...new Map(rows.map(r=>[r.ordem,r.categoria])).entries()].sort((a,b)=>a[0]-b[0]).map(x=>x[1]);
const lookup=(rows,cat,serie)=>rows.find(r=>r.categoria===cat&&r.serie===serie)?.valor ?? 0;
const niceMax=(value)=>{const step=value>300?100:value>160?50:value>80?20:10;return Math.max(step,Math.ceil(value/step)*step);};
const ticksFor=(max)=>[0,Math.round(max*.25),Math.round(max*.5),Math.round(max*.75),max];
function wrap(value,max=28){const words=value.split(" ");let lines=[""];for(const word of words){const last=lines.length-1;if((lines[last]+" "+word).trim().length>max&&lines[last])lines.push(word);else lines[last]=(lines[last]+" "+word).trim();}return lines.join("\n");}
function axisGrid(left,right,top,bottom,ticks,max){let b="";for(const tick of ticks){const x=left+(right-left)*tick/max;b+=line(x,top,x,bottom,C.grid,0.6,{class:"axis"})+text(x,bottom+14,String(tick),8.5,"middle");}return b;}
function legend(x,y,items){let b="";items.forEach((it,i)=>{const xx=x+i*92;b+=it.shape==="diamond"?diamond(xx,y-2,4,it.color):circle(xx,y-2,4,it.color);b+=text(xx+8,y+1,it.label,8.5);});return b;}

function graph1(rows){
  const cats=categories(rows), vals=cats.map(c=>lookup(rows,c,"Estudos")), colors=[C.dark,C.light,C.gray];
  const left=176,right=416,total=vals.reduce((a,b)=>a+b,0),max=Math.max(...vals);let b=text(right,15,`Total documentado: ${total}`,8.5,"end",C.text,700);
  cats.forEach((cat,i)=>{const y=34+i*31,w=Math.max(3,(right-left)*vals[i]/max);b+=text(left-8,y+4,cat,8.5,"end",C.text,500);b+=rect(left,y-7,w,15,colors[i]);b+=text(Math.min(left+w+6,432),y+4,String(vals[i]),8.5,"start",C.dark,700);});
  return svg(443,130,b);
}
function graph2(rows){
  const cats=categories(rows), left=190,right=421,top=36,bottom=222,max=niceMax(Math.max(...rows.filter(r=>r.serie==="Total").map(r=>r.valor)));let b=axisGrid(left,right,top,bottom,ticksFor(max),max);b+=legend(270,16,[{shape:"circle",color:C.blue,label:"Total"},{shape:"diamond",color:C.orange,label:"Evidência central"}]);
  cats.forEach((cat,i)=>{const y=top+11+i*(bottom-top-20)/(cats.length-1),t=lookup(rows,cat,"Total"),c=lookup(rows,cat,"Evidência central"),xt=left+(right-left)*t/max,xc=left+(right-left)*c/max;b+=multiline(left-8,y+3,wrap(cat,28),8.5,"end");b+=line(xc,y,xt,y,C.pale,4.5);b+=circle(xt,y,4.1,C.blue);b+=diamond(xc,y,4.3,C.orange);b+=text(xt+6,y+3,String(t),8.5,"start",C.dark,700);b+=text(Math.max(xc-5,left),y-6,String(c),8.5,"end",C.orange,700);});
  b+=text((left+right)/2,244,"Número de estudos",8.5,"middle");return svg(443,248,b);
}
function graph3(rows){
  const cats=categories(rows),left=112,right=420,top=35,bottom=173,max=niceMax(Math.max(...cats.map(c=>lookup(rows,c,"Evidência central")+lookup(rows,c,"Evidência de apoio"))));let b=axisGrid(left,right,top,bottom,ticksFor(max),max);b+=legend(228,16,[{shape:"diamond",color:C.orange,label:"Evidência central"},{shape:"circle",color:C.light,label:"Evidência de apoio"}]);
  cats.forEach((cat,i)=>{const y=top+12+i*27,c=lookup(rows,cat,"Evidência central"),s=lookup(rows,cat,"Evidência de apoio"),wc=(right-left)*c/max,ws=(right-left)*s/max;b+=text(left-8,y+3,cat,8.5,"end");b+=rect(left,y-7,wc,14,C.orange);b+=rect(left+wc,y-7,ws,14,C.light);b+=text(left+wc/2,y+3,String(c),8.5,"middle",C.white,700);b+=text(left+wc+ws+6,y+3,String(c+s),8.5,"start",C.dark,700);});b+=text((left+right)/2,194,"Número de estudos",8.5,"middle");return svg(443,198,b);
}
function graph4(rows){
  const cats=categories(rows),left=194,right=420,top=34,bottom=210,max=niceMax(Math.max(...rows.filter(r=>r.serie==="Total").map(r=>r.valor)));let b=axisGrid(left,right,top,bottom,ticksFor(max),max);b+=legend(270,16,[{shape:"circle",color:C.light,label:"Total"},{shape:"diamond",color:C.orange,label:"Evidência central"}]);
  cats.forEach((cat,i)=>{const y=top+10+i*22,t=lookup(rows,cat,"Total"),c=lookup(rows,cat,"Evidência central"),wt=(right-left)*t/max,wc=(right-left)*c/max;b+=multiline(left-8,y+3,wrap(cat,30),8.5,"end");b+=rect(left,y-6,wt,12,C.light);if(c)b+=rect(left,y-6,wc,12,C.orange);b+=text(left+wt+5,y+3,String(t),8.5,"start",C.dark,700);if(c)b+=text(left+wc/2,y+3,String(c),8.5,"middle",C.white,700);});b+=text((left+right)/2,231,"Número de estudos",8.5,"middle");return svg(443,234,b);
}
function graph5(rows){
  const cats=categories(rows),left=205,right=420,top=36,bottom=169,max=niceMax(Math.max(...rows.filter(r=>r.serie==="Total").map(r=>r.valor)));let b=axisGrid(left,right,top,bottom,ticksFor(max),max);b+=legend(270,16,[{shape:"circle",color:C.blue,label:"Total"},{shape:"diamond",color:C.orange,label:"Evidência central"}]);
  cats.forEach((cat,i)=>{const y=top+12+i*29,t=lookup(rows,cat,"Total"),c=lookup(rows,cat,"Evidência central"),xt=left+(right-left)*t/max,xc=left+(right-left)*c/max;b+=multiline(left-8,y+3,wrap(cat,31),8.5,"end");b+=line(xc,y,xt,y,C.pale,5);b+=circle(xt,y,4.3,C.blue);b+=diamond(xc,y,4.3,C.orange);b+=text(xt+6,y+3,String(t),8.5,"start",C.dark,700);b+=text(xc,y-7,String(c),8.5,"middle",C.orange,700);});b+=text((left+right)/2,194,"Número de estudos",8.5,"middle");return svg(443,198,b);
}
function cividis(v,max){const stops=[[0,"#00204C"],[.25,"#334E6F"],[.5,"#6C6F72"],[.75,"#B59B58"],[1,"#FDE737"]];const t=v/max;let a=stops[0],d=stops.at(-1);for(let i=1;i<stops.length;i++)if(t<=stops[i][0]){a=stops[i-1];d=stops[i];break;}const p=(t-a[0])/(d[0]-a[0]||1),hex=n=>parseInt(n.slice(1),16),A=hex(a[1]),D=hex(d[1]),mix=s=>Math.round(((A>>s)&255)*(1-p)+((D>>s)&255)*p);return `#${[16,8,0].map(s=>mix(s).toString(16).padStart(2,"0")).join("")}`;}
function graph6(rows){
  const cats=categories(rows),cols=["Técnica","Interacional","Organizacional","Regulatória","Evolutiva"],left=181,top=51,cw=48,ch=24,max=Math.max(...rows.map(r=>r.valor));let b="";
  cols.forEach((c,j)=>{const x=left+j*cw+cw/2;b+=text(x,38,c,8.5,"start",C.text,700,{transform:`rotate(-35 ${x} 38)`});});
  cats.forEach((cat,i)=>{b+=multiline(left-8,top+i*ch+ch/2+3,wrap(cat,28),8.5,"end");cols.forEach((col,j)=>{const v=lookup(rows,cat,col),color=cividis(v,max);b+=rect(left+j*cw,top+i*ch,cw,ch,color,0,C.white,1);b+=text(left+j*cw+cw/2,top+i*ch+ch/2+3,String(v),8.5,"middle",C.white,700);});});
  b+=text(left+2.5*cw,253,"Número de estudos por coocorrência",8.5,"middle");return svg(443,256,b);
}
async function save(stem,w,h,content){await writeFile(path.join(SVG_DIR,`${stem}.svg`),content,"utf8");await sharp(Buffer.from(content)).resize(w*5,h*5).png({compressionLevel:9}).withMetadata({density:360}).toFile(path.join(PNG_DIR,`${stem}.png`));}
async function main(){
  await mkdir(PNG_DIR,{recursive:true});await mkdir(SVG_DIR,{recursive:true});const rows=parseCsv(await readFile(DATA,"utf8"));
  const svgs=[graph1(group(rows,"grafico_1")),graph2(group(rows,"grafico_2")),graph3(group(rows,"grafico_3")),graph4(group(rows,"grafico_4")),graph5(group(rows,"grafico_5")),graph6(group(rows,"grafico_6"))];
  for(let i=0;i<files.length;i++)await save(...files[i],svgs[i]);
  console.log(`Gerados ${files.length} gráficos em SVG e PNG a 360 dpi; Figura 1 histórica preservada.`);
}
await main();
