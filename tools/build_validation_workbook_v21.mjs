import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const root = process.env.REV_LIT_ROOT || path.resolve(scriptDir, "..");
const inventoryPath = path.join(root, "Documentacao_do_projeto", "methodology", "CORPUS_ANALYTIC_177_INVENTORY.csv");
const checkpointPath = path.join(root, "arquivos_tratados_aigovernanca", "metagrade_llm_output", "checkpoint_results.jsonl");
const searchQueuePath = path.join(root, "Documentacao_do_projeto", "v2.1", "busca_de_sensibilidade", "Resultados_recuperados_v2.1.csv");
const outputPath = path.join(root, "Documentacao_do_projeto", "v2.1", "Validacao_humana_do_corpus_v2.1.xlsx");

function parseCsv(source) {
  const text = source.replace(/^\uFEFF/, "");
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    if (quoted) {
      if (char === '"' && text[i + 1] === '"') { field += '"'; i += 1; }
      else if (char === '"') quoted = false;
      else field += char;
    } else if (char === '"') quoted = true;
    else if (char === ',') { row.push(field); field = ""; }
    else if (char === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += char;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  const [headers, ...data] = rows.filter((r) => r.some((value) => value !== ""));
  return data.map((values) => Object.fromEntries(headers.map((header, index) => [header, values[index] ?? ""])));
}

const inventory = parseCsv(await fs.readFile(inventoryPath, "utf8"));
const checkpointRows = (await fs.readFile(checkpointPath, "utf8"))
  .split(/\r?\n/).filter(Boolean).map((line) => JSON.parse(line));
const checkpoint = new Map(checkpointRows.map((row) => [String(row.raw_file_name || "").replace(/\.pdf$/i, ""), row]));

let searchQueue = [];
try {
  searchQueue = parseCsv(await fs.readFile(searchQueuePath, "utf8"));
} catch {
  searchQueue = [];
}

const wb = Workbook.create();
const navy = "#173B57";
const blue = "#DCEAF3";
const pale = "#FFF4CC";
const green = "#DDEFE3";
const red = "#F7D9D9";
const gray = "#EEF1F3";
const white = "#FFFFFF";
const text = "#1F2933";

function colName(index) {
  let n = index + 1;
  let out = "";
  while (n > 0) {
    const rem = (n - 1) % 26;
    out = String.fromCharCode(65 + rem) + out;
    n = Math.floor((n - 1) / 26);
  }
  return out;
}

function headerStyle(range) {
  range.format = {
    fill: navy,
    font: { name: "Arial", size: 10, bold: true, color: white },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "outside", style: "thin", color: "#9FB2BF" },
  };
}

function titleBlock(sheet, title, subtitle, width) {
  const last = colName(width - 1);
  sheet.getRange(`A1:${last}1`).merge();
  sheet.getRange("A1").values = [[title]];
  sheet.getRange("A1").format = { fill: navy, font: { name: "Arial", bold: true, color: white, size: 16 }, rowHeight: 30 };
  sheet.getRange(`A2:${last}2`).merge();
  sheet.getRange("A2").values = [[subtitle]];
  sheet.getRange("A2").format = { fill: blue, font: { name: "Arial", size: 10, color: text, italic: true }, wrapText: true, rowHeight: 32 };
}

function writeTable(sheet, startRow, headers, rows, widths = []) {
  const start = startRow;
  const lastCol = colName(headers.length - 1);
  sheet.getRange(`A${start}:${lastCol}${start}`).values = [headers];
  headerStyle(sheet.getRange(`A${start}:${lastCol}${start}`));
  if (rows.length) {
    sheet.getRange(`A${start + 1}:${lastCol}${start + rows.length}`).values = rows;
    sheet.getRange(`A${start + 1}:${lastCol}${start + rows.length}`).format = {
      font: { name: "Arial", size: 10, color: text },
      verticalAlignment: "top",
      wrapText: true,
      borders: { insideHorizontal: { style: "thin", color: "#D9E1E6" } },
    };
  }
  widths.forEach((width, i) => { sheet.getRange(`${colName(i)}:${colName(i)}`).format.columnWidth = width; });
  return { firstDataRow: start + 1, lastDataRow: start + rows.length, lastCol };
}

// LEIA-ME
{
  const sheet = wb.worksheets.add("LEIA-ME");
  titleBlock(sheet, "Validação humana do corpus — v2.1", "Instrumento exclusivo para decisões científicas de Yago Henrique. Os rótulos históricos do LLM estão separados na aba Referencia_LLM para reduzir ancoragem.", 6);
  const sections = [
    ["1", "Valide a declaração autoral", "Confirme primeiro se o relato híbrido e iterativo corresponde ao processo real de construção das cinco camadas."],
    ["2", "Preencha Validacao_177", "Trabalhe em lotes de 25. Examine título, metadados, evidência e, quando necessário, o PDF. Não consulte Referencia_LLM antes da primeira decisão."],
    ["3", "Aplique a regra central", "Evidência central exige C1, C2 e C3 = Sim. Caso contrário, classifique como apoio ou exclua, com justificativa."],
    ["4", "Reexamine divergências", "Depois da primeira decisão, compare com Referencia_LLM. Toda divergência deve voltar ao texto integral e receber justificativa final."],
    ["5", "Complete JBI e CERQual", "Use o checklist JBI correspondente ao desenho. CERQual é avaliado por achado qualitativo, não por estudo."],
    ["6", "Não altere fórmulas", "Preencha somente as células amarelas. A aba Resumo calcula pendências e bloqueia o fechamento enquanto houver campos obrigatórios vazios."],
  ];
  writeTable(sheet, 4, ["Etapa", "Ação", "Como fazer"], sections, [9, 28, 78]);
  sheet.getRange("A12:F12").merge();
  sheet.getRange("A12").values = [["Critério de encerramento: a v2.1 não pode ser chamada de final enquanto a aba Resumo indicar pendências humanas."]];
  sheet.getRange("A12").format = { fill: red, font: { bold: true, color: "#7A1F1F" }, wrapText: true, rowHeight: 32 };
  sheet.showGridLines = false;
}

// RESUMO
{
  const sheet = wb.worksheets.add("Resumo");
  titleBlock(sheet, "Painel de fechamento", "Os indicadores são calculados a partir das abas de validação e qualidade.", 4);
  const rows = [
    ["Estudos históricos", "=COUNTA('Validacao_177'!$B$5:$B$181)", 177, "deve permanecer 177 até a busca complementar ser julgada"],
    ["Validações confirmadas", "=COUNTIF('Validacao_177'!$X$5:$X$181,\"confirmado\")", 177, "bloqueador principal"],
    ["Validações pendentes", "=COUNTIF('Validacao_177'!$X$5:$X$181,\"pendente\")", 0, "deve chegar a zero"],
    ["Evidências centrais humanas", "=COUNTIF('Validacao_177'!$M$5:$M$181,\"evidencia_central\")", "informativo", "pode divergir de 23 após validação"],
    ["Evidências de apoio humanas", "=COUNTIF('Validacao_177'!$M$5:$M$181,\"evidencia_apoio\")", "informativo", "pode divergir de 154 após validação"],
    ["Avaliações JBI concluídas", "=COUNTIF('Avaliacao_JBI'!$V$5:$V$27,\"confirmado\")", "todas as centrais", "atualizar lista se a classificação mudar"],
    ["Achados CERQual concluídos/N.A.", "=COUNTIF('CERQual_achados'!$I$5:$I$9,\"confirmado\")+COUNTIF('CERQual_achados'!$I$5:$I$9,\"nao_aplicavel\")", 5, "avaliação no nível do achado"],
    ["Novos registros aguardando decisão", searchQueue.length ? `=COUNTIF('Triagem_novos'!$R$5:$R$${4 + searchQueue.length},\"pendente\")` : 0, 0, "não incluir automaticamente"],
  ];
  writeTable(sheet, 4, ["Indicador", "Valor atual", "Meta", "Observação"], rows, [36, 20, 18, 60]);
  sheet.getRange("A14:D14").merge();
  sheet.getRange("A14").formulas = [["=IF(AND(B6=177,B7=0,B10=B8,B11=5,B12=0),\"PRONTO PARA RECONCILIAÇÃO\",\"AGUARDANDO VALIDAÇÃO HUMANA\")"]];
  sheet.getRange("A14").format = { fill: pale, font: { bold: true, color: "#6B4F00", size: 13 }, horizontalAlignment: "center", rowHeight: 28 };
  sheet.showGridLines = false;
}

// VALIDACAO 177 — sem classificação LLM visível
{
  const sheet = wb.worksheets.add("Validacao_177");
  const headers = ["Lote", "Identificador", "Título", "Autores", "Ano", "Veículo", "Arquivo PDF", "Setor sugerido", "Elegível?", "C1 objeto direto", "C2 contexto regulado", "C3 contribuição substantiva", "Classificação de Yago", "Justificativa humana", "Evidência confirmada", "Página", "Camada técnica", "Camada interacional", "Camada organizacional", "Camada regulatória", "Camada evolutiva", "Mecanismos principais", "Observações", "Status validação", "Validador", "Data"];
  titleBlock(sheet, "Validação cega dos 177 estudos", "Preencha as células amarelas antes de consultar a aba Referencia_LLM. Evidência central somente quando C1, C2 e C3 forem Sim.", headers.length);
  const rows = inventory.map((row, i) => [
    Math.floor(i / 25) + 1, row.identificador, row.titulo, row.autores, row.ano, row.veiculo,
    `arquivos_tratados_aigovernanca/fulltext_repository/pdfs/${row.arquivo_pdf}`, row.setor,
    "", "", "", "", "", "", row.evidencia_ancora || "", row.pagina_evidencia || "",
    "", "", "", "", "", "", "", "pendente", "Yago Henrique", "",
  ]);
  const table = writeTable(sheet, 4, headers, rows, [8, 25, 48, 30, 9, 28, 45, 24, 12, 14, 16, 18, 22, 48, 55, 9, 14, 16, 18, 16, 15, 35, 35, 16, 20, 13]);
  sheet.freezePanes.freezeRows(4);
  sheet.freezePanes.freezeColumns(2);
  sheet.getRange(`I5:N${table.lastDataRow}`).format.fill = pale;
  sheet.getRange(`Q5:X${table.lastDataRow}`).format.fill = pale;
  sheet.getRange(`Z5:Z${table.lastDataRow}`).format.fill = pale;
  for (const col of ["I", "J", "K", "L"]) sheet.getRange(`${col}5:${col}${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["sim", "nao", "incerto"] } };
  for (const col of ["Q", "R", "S", "T", "U"]) sheet.getRange(`${col}5:${col}${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["sim", "nao", "incerto"] } };
  sheet.getRange(`M5:M${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["evidencia_central", "evidencia_apoio", "excluir", "incerto"] } };
  sheet.getRange(`X5:X${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["pendente", "em_revisao", "confirmado"] } };
  sheet.getRange(`A5:A${table.lastDataRow}`).format.numberFormat = "0";
  sheet.getRange(`P5:P${table.lastDataRow}`).format.numberFormat = "0";
  sheet.showGridLines = false;
}

// Referência histórica LLM
{
  const sheet = wb.worksheets.add("Referencia_LLM");
  const headers = ["Identificador", "Classificação publicada", "Decisão LLM histórica", "Confiança LLM", "Tipo de pesquisa", "Desenho", "Códigos abertos", "Códigos axiais", "Tema", "Camadas históricas", "Racional histórico", "Uso na revisão"];
  titleBlock(sheet, "Referência histórica — consultar depois da primeira decisão", "Esta aba não é validação humana. Serve apenas para reconciliar divergências depois que Yago concluir a primeira avaliação.", headers.length);
  const rows = inventory.map((row) => {
    const cp = checkpoint.get(row.identificador) || {};
    return [row.identificador, row.classificacao_publicada, cp.llm_final_decision || row.decisao_checkpoint, cp.llm_decision_confidence || "", cp.llm_research_type || "", cp.llm_study_design || "", cp.coding_open_codes || "", cp.coding_axial_codes || "", cp.coding_theme || row.tema_codificado, cp.coding_model_layers || row.camadas_codificacao_original, cp.llm_decision_rationale || "", cp.synthesis_use_in_review || ""];
  });
  writeTable(sheet, 4, headers, rows, [25, 22, 24, 13, 20, 24, 42, 42, 38, 38, 60, 55]);
  sheet.freezePanes.freezeRows(4);
  sheet.freezePanes.freezeColumns(1);
  sheet.showGridLines = false;
}

function suggestedJbi(cp) {
  const textValue = `${cp.llm_research_type || ""} ${cp.llm_study_design || ""}`.toLowerCase();
  if (textValue.includes("systematic") || textValue.includes("scoping") || textValue.includes("review")) return "JBI Systematic Reviews and Research Syntheses";
  if (textValue.includes("qualitative") || textValue.includes("interview") || textValue.includes("thematic")) return "JBI Qualitative Research";
  if (textValue.includes("cross-sectional") || textValue.includes("survey")) return "JBI Analytical Cross Sectional Studies";
  if (textValue.includes("random") || textValue.includes("trial")) return "JBI Randomized Controlled Trials";
  if (textValue.includes("quasi") || textValue.includes("experimental")) return "JBI Quasi-Experimental Studies";
  return "JBI Textual Evidence: Narrative/Expert Opinion";
}

// JBI
{
  const central = inventory.filter((row) => row.classificacao_publicada === "evidencia_central");
  const sheet = wb.worksheets.add("Avaliacao_JBI");
  const itemHeaders = Array.from({ length: 13 }, (_, i) => `Item ${i + 1}`);
  const headers = ["Identificador", "Título", "Desenho histórico", "Instrumento sugerido", "Instrumento confirmado por Yago", ...itemHeaders, "Conclusão", "Justificativa", "Data", "Status"];
  titleBlock(sheet, "Avaliação crítica JBI — evidências centrais", "Consulte o checklist oficial correspondente. Registre cada item como Sim, Não, Incerto ou N.A.; itens excedentes do instrumento ficam N.A.", headers.length);
  const rows = central.map((row) => {
    const cp = checkpoint.get(row.identificador) || {};
    return [row.identificador, row.titulo, cp.llm_study_design || cp.llm_research_type || "a confirmar", suggestedJbi(cp), "", ...Array(13).fill(""), "", "", "", "pendente"];
  });
  const table = writeTable(sheet, 4, headers, rows, [25, 48, 25, 38, 38, ...Array(13).fill(10), 26, 48, 13, 15]);
  sheet.freezePanes.freezeRows(4);
  sheet.freezePanes.freezeColumns(2);
  sheet.getRange(`E5:V${table.lastDataRow}`).format.fill = pale;
  for (let i = 5; i < 18; i++) {
    const col = colName(i);
    sheet.getRange(`${col}5:${col}${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["sim", "nao", "incerto", "nao_aplicavel"] } };
  }
  sheet.getRange(`S5:S${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["sem_preocupacoes_relevantes", "preocupacoes_menores", "preocupacoes_importantes"] } };
  sheet.getRange(`V5:V${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["pendente", "em_revisao", "confirmado"] } };
  sheet.showGridLines = false;
}

// CERQual
{
  const sheet = wb.worksheets.add("CERQual_achados");
  const headers = ["Achado", "Compatível com CERQual?", "Limitações metodológicas", "Coerência", "Adequação dos dados", "Relevância", "Confiança global", "Explicação", "Status"];
  titleBlock(sheet, "GRADE-CERQual no nível dos achados", "Não use CERQual para as contagens quantitativas. Avalie somente a componente qualitativa de cada achado e marque Não aplicável quando incompatível.", headers.length);
  const findings = [
    "Avaliação de riscos e qualidade",
    "Supervisão humana e accountability",
    "Observabilidade, auditoria e monitoramento",
    "Governança do conhecimento, RAG e guardrails",
    "Confiança, explicabilidade e orientação ao usuário",
  ];
  const rows = findings.map((f) => [f, "", "", "", "", "", "", "", "pendente"]);
  const table = writeTable(sheet, 4, headers, rows, [42, 22, 28, 24, 26, 24, 20, 60, 18]);
  sheet.getRange(`B5:I${table.lastDataRow}`).format.fill = pale;
  sheet.getRange(`B5:B${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["sim", "nao", "incerto"] } };
  for (const col of ["C", "D", "E", "F"]) sheet.getRange(`${col}5:${col}${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["nenhuma_preocupacao", "preocupacao_menor", "preocupacao_moderada", "preocupacao_grave", "nao_aplicavel"] } };
  sheet.getRange(`G5:G${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["alta", "moderada", "baixa", "muito_baixa", "nao_aplicavel"] } };
  sheet.getRange(`I5:I${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["pendente", "em_revisao", "confirmado", "nao_aplicavel"] } };
  sheet.showGridLines = false;
}

// Triagem dos resultados prospectivos
{
  const sheet = wb.worksheets.add("Triagem_novos");
  const headers = ["Fonte", "Família", "Posição", "Faixa", "Título", "Autores", "Ano", "DOI", "URL", "Resumo", "Presente no corpus histórico", "Duplicata desta execução", "Prioridade automática", "Decisão de Yago", "Justificativa", "Texto completo consultado?", "Classificação final", "Status"];
  titleBlock(sheet, "Triagem da busca prospectiva", "Todo registro novo exige decisão humana. Prioridade automática organiza a fila, mas não exclui nem inclui estudos.", headers.length);
  const rows = searchQueue.map((r) => [r.fonte, r.familia, Number(r.posicao || 0), r.faixa_posicao, r.titulo, r.autores, r.ano, r.doi, r.url, r.resumo, r.presente_no_corpus_historico, r.duplicata_nesta_execucao_de, r.prioridade_triagem_automatica, "", "", "", "", r.status_validacao_humana || "pendente"]);
  const table = writeTable(sheet, 4, headers, rows, [18, 28, 10, 12, 48, 30, 9, 24, 42, 55, 20, 28, 18, 18, 48, 22, 22, 16]);
  if (rows.length) {
    sheet.getRange(`N5:R${table.lastDataRow}`).format.fill = pale;
    sheet.getRange(`N5:N${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["incluir", "excluir", "incerto"] } };
    sheet.getRange(`P5:P${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["sim", "nao", "nao_necessario"] } };
    sheet.getRange(`Q5:Q${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["evidencia_central", "evidencia_apoio", "contextual", "excluir"] } };
    sheet.getRange(`R5:R${table.lastDataRow}`).dataValidation = { rule: { type: "list", values: ["pendente", "em_revisao", "confirmado", "nao_aplicavel"] } };
  }
  sheet.freezePanes.freezeRows(4);
  sheet.freezePanes.freezeColumns(2);
  sheet.showGridLines = false;
}

// Dicionário e genealogia inicial
{
  const sheet = wb.worksheets.add("Dicionario");
  titleBlock(sheet, "Dicionário de decisão e proveniência", "Definições operacionais usadas em todas as abas. Cores nunca substituem os valores textuais.", 4);
  const rows = [
    ["C1 objeto direto", "O objeto principal examina governança, supervisão, risco, accountability, auditoria, compliance ou operação controlada de LLM/IA generativa/sistema conversacional.", "sim | nao | incerto", "Protocolo v2.1"],
    ["C2 contexto", "Há ambiente regulado, de alto impacto ou transferibilidade explícita para esse contexto.", "sim | nao | incerto", "Protocolo v2.1"],
    ["C3 contribuição", "O estudo apresenta resultado, síntese, mecanismo ou arquitetura substantiva para pelo menos uma questão da revisão.", "sim | nao | incerto", "Protocolo v2.1"],
    ["evidencia_central", "C1, C2 e C3 confirmados simultaneamente.", "classificação", "Protocolo v2.1"],
    ["evidencia_apoio", "Estudo elegível, mas com contribuição periférica, contextual ou transferível.", "classificação", "Protocolo v2.1"],
    ["camada técnica", "Controle do modelo, dados, RAG, guardrails, avaliação, segurança e observabilidade técnica.", "sim | nao | incerto", "Modelo de cinco camadas"],
    ["camada interacional", "Limites, explicabilidade, contestação, reparo, handoff e experiência do usuário.", "sim | nao | incerto", "Modelo de cinco camadas"],
    ["camada organizacional", "Papéis, políticas, supervisão, auditoria, incidentes e accountability institucional.", "sim | nao | incerto", "Modelo de cinco camadas"],
    ["camada regulatória", "Risco, conformidade, documentação, direitos e obrigações setoriais.", "sim | nao | incerto", "Modelo de cinco camadas"],
    ["camada evolutiva", "Monitoramento, feedback, aprendizagem pós-incidente e mudança controlada.", "sim | nao | incerto", "Modelo de cinco camadas"],
    ["JBI", "Ferramentas oficiais de avaliação crítica por desenho.", "https://jbi.global/critical-appraisal-tools", "JBI"],
    ["CERQual", "Confiança em achados de sínteses qualitativas; não é escore por estudo.", "https://www.cerqual.org/official-guidance-for-applying-grade-cerqual/", "GRADE-CERQual"],
  ];
  writeTable(sheet, 4, ["Campo", "Definição", "Valores ou link", "Fonte"], rows, [28, 78, 48, 28]);
  sheet.showGridLines = false;
}

// Aplicar apenas alinhamento básico; a tipografia foi definida por bloco para não
// sobrescrever títulos, subtítulos e cabeçalhos.
for (const sheet of wb.worksheets.items) {
  const used = sheet.getUsedRange();
  if (used) {
    used.format.verticalAlignment = "top";
  }
}

await fs.mkdir(path.dirname(outputPath), { recursive: true });
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(outputPath);

const summary = await wb.inspect({ kind: "table", sheetId: "Resumo", range: "A1:D14", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 8, maxChars: 6000 });
const errors = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "final formula error scan", maxChars: 3000 });
console.log(summary.ndjson);
console.log(errors.ndjson);

const previewDir = path.join(process.env.TEMP || root, "codex_v21_workbook_previews");
await fs.mkdir(previewDir, { recursive: true });
for (const [sheetName, range] of [["LEIA-ME", "A1:F12"], ["Resumo", "A1:D14"], ["Validacao_177", "A1:Z15"], ["Avaliacao_JBI", "A1:V12"], ["CERQual_achados", "A1:I9"], ["Triagem_novos", "A1:R14"]]) {
  const preview = await wb.render({ sheetName, range, scale: 1, format: "png" });
  await fs.writeFile(path.join(previewDir, `${sheetName}.png`), new Uint8Array(await preview.arrayBuffer()));
}
console.log(JSON.stringify({ outputPath, previewDir, inventoryRows: inventory.length, searchQueueRows: searchQueue.length }));
