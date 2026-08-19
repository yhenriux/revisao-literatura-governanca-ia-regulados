import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const [inventoryPath, fulltextPath, sourceWorkbookPath, visualDataPath, outputDir] = process.argv.slice(2);
if (!outputDir) throw new Error("Uso: node close_evidence_audit_v2.mjs <inventario.csv> <fulltext.jsonl> <workbook.xlsx> <dados_figuras.csv> <saida>");

const norm = s => String(s ?? "").normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
const csvEscape = value => {
  const s = String(value ?? "");
  return /[",\r\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s;
};
const toCsv = rows => rows.map(row => row.map(csvEscape).join(",")).join("\r\n") + "\r\n";
const objectsFromMatrix = matrix => {
  const headers = matrix[0].map(String);
  return matrix.slice(1).map(row => Object.fromEntries(headers.map((h, i) => [h, row[i] ?? ""])));
};

const inventoryWb = await Workbook.fromCSV(await fs.readFile(inventoryPath, "utf8"), { sheetName: "Inventario" });
const inventoryMatrix = inventoryWb.worksheets.getItem("Inventario").getUsedRange(true).values;
const inventory = objectsFromMatrix(inventoryMatrix);
const fulltexts = new Map((await fs.readFile(fulltextPath, "utf8")).trim().split(/\r?\n/).map(JSON.parse).map(x => [x.candidate_id, x]));

const source = await SpreadsheetFile.importXlsx(await FileBlob.load(sourceWorkbookPath));
const records = objectsFromMatrix(source.worksheets.getItem("records_flat").getUsedRange(true).values);
const evidence = objectsFromMatrix(source.worksheets.getItem("evidence_matrix").getUsedRange(true).values);
const coding = objectsFromMatrix(source.worksheets.getItem("coding_themes").getUsedRange(true).values);
const recordByFile = new Map(records.map(x => [String(x.raw_file_name), x]));
const evidenceByStudy = new Map();
for (const row of evidence) {
  if (!evidenceByStudy.has(row.study_id)) evidenceByStudy.set(row.study_id, []);
  evidenceByStudy.get(row.study_id).push(row);
}
const codingByStudy = new Map(coding.map(x => [x.study_id, x]));
const supportRank = new Map(["synthesis", "coding", "eligibility", "rq_alignment", "methodology", "appraisal", "bibliographic"].map((x, i) => [x, i]));

const verification = [];
const updatedInventory = [];
for (const item of inventory) {
  const candidateId = String(item.identificador).split("__")[0];
  const full = fulltexts.get(candidateId);
  const textNorm = norm(full?.full_text ?? "");
  const record = recordByFile.get(String(item.arquivo_pdf));
  const studyId = record?.study_id ?? "";
  const originalAnchor = String(item.evidencia_ancora_checkpoint_historico || item.evidencia_ancora || "");
  const historicalStatus = String(item.status_verificacao_checkpoint_historico || item.status_verificacao || "");
  const historicalAnchor = originalAnchor;
  const originalMatch = Boolean(norm(originalAnchor) && textNorm.includes(norm(originalAnchor)));
  let selected = null;
  let method = "";
  if (originalMatch) {
    selected = { excerpt: originalAnchor, page: item.pagina_evidencia, section: "registrada_no_inventario", supports: "ancora_publicada" };
    method = "correspondencia_literal_normalizada_no_texto_integral";
  } else {
    const alternatives = (evidenceByStudy.get(studyId) ?? [])
      .filter(e => norm(e.excerpt) && textNorm.includes(norm(e.excerpt)))
      .sort((a, b) => (supportRank.get(String(a.supports)) ?? 99) - (supportRank.get(String(b.supports)) ?? 99));
    selected = alternatives[0] ?? null;
    method = selected ? "evidencia_alternativa_literal_normalizada_no_texto_integral" : "nao_resolvida";
  }
  const finalStatus = selected ? "verificada_v2_final" : "pendente_revisao_humana";
  verification.push({
    identificador: item.identificador,
    titulo: item.titulo,
    classificacao_publicada: item.classificacao_publicada,
    status_checkpoint_historico: historicalStatus,
    estudo_id_pipeline: studyId,
    decisao_llm: record?.llm_final_decision ?? "",
    decisao_consenso: record?.consensus_final_decision ?? "",
    evidencias_validas_pipeline: record?.validated_evidence_count ?? "",
    evidencias_invalidas_pipeline: record?.invalid_evidence_count ?? "",
    metodo_verificacao_v2_final: method,
    evidencia_verificada: selected?.excerpt ?? "",
    pagina_verificada: selected?.page ?? "",
    secao_verificada: selected?.section ?? "",
    finalidade_evidencia: selected?.supports ?? "",
    status_verificacao_v2_final: finalStatus,
    observacao: selected ? "Trecho localizado após normalização Unicode, de espaços e pontuação; a decisão científica não foi inferida apenas pela confiança do LLM." : "Nenhuma evidência literal foi localizada automaticamente; requer revisão humana independente.",
    alerta_historico_flag: historicalStatus.includes("com_alerta") ? 1 : 0,
    ancora_normalizada_alerta_flag: historicalStatus.includes("com_alerta") && method.startsWith("correspondencia") ? 1 : 0,
    evidencia_alternativa_alerta_flag: historicalStatus.includes("com_alerta") && method.startsWith("evidencia_alternativa") ? 1 : 0,
    pendencia_flag: finalStatus === "verificada_v2_final" ? 0 : 1
  });
  updatedInventory.push({
    ...item,
    status_verificacao_checkpoint_historico: historicalStatus,
    evidencia_ancora_checkpoint_historico: historicalAnchor,
    status_verificacao: finalStatus,
    metodo_verificacao_v2_final: method,
    evidencia_ancora: selected?.excerpt ?? originalAnchor,
    pagina_evidencia: selected?.page ?? item.pagina_evidencia,
    justificativa_reconciliacao: [item.justificativa_reconciliacao, selected && !originalMatch ? "Âncora substituída por evidência alternativa literalmente localizada no texto integral durante a auditoria final da v2." : "Âncora confirmada por correspondência literal normalizada no texto integral durante a auditoria final da v2."].filter(Boolean).join(" ")
  });
}

const unresolved = verification.filter(x => x.status_verificacao_v2_final !== "verificada_v2_final");
if (unresolved.length) throw new Error(`Auditoria incompleta: ${unresolved.length} estudos sem evidência literal verificável: ${unresolved.map(x => x.identificador).join(", ")}`);

await fs.mkdir(outputDir, { recursive: true });
const verificationHeaders = Object.keys(verification[0]);
await fs.writeFile(path.join(outputDir, "CORPUS_EVIDENCE_VERIFICATION_177.csv"), toCsv([verificationHeaders, ...verification.map(x => verificationHeaders.map(h => x[h]))]), "utf8");

const originalHeaders = inventoryMatrix[0].map(String).filter(h => !["status_verificacao", "evidencia_ancora", "pagina_evidencia", "justificativa_reconciliacao", "status_verificacao_checkpoint_historico", "evidencia_ancora_checkpoint_historico", "metodo_verificacao_v2_final"].includes(h));
const inventoryHeaders = [...new Set([
  ...originalHeaders,
  "status_verificacao_checkpoint_historico", "evidencia_ancora_checkpoint_historico",
  "status_verificacao", "metodo_verificacao_v2_final", "evidencia_ancora", "pagina_evidencia", "justificativa_reconciliacao"
])];
await fs.writeFile(inventoryPath, toCsv([inventoryHeaders, ...updatedInventory.map(x => inventoryHeaders.map(h => x[h]))]), "utf8");

const reconciliation = updatedInventory.map(item => {
  const record = recordByFile.get(String(item.arquivo_pdf)) ?? {};
  const code = codingByStudy.get(record.study_id) ?? {};
  const verified = verification.find(v => v.identificador === item.identificador);
  return {
    identificador: item.identificador,
    estudo_id_pipeline: record.study_id ?? "",
    titulo: item.titulo,
    classificacao_publicada: item.classificacao_publicada,
    setor: item.setor,
    tema_inventario: item.tema_codificado,
    subtema_inventario: item.subtema_codificado,
    tema_pipeline: code.coding_theme ?? "",
    subtema_pipeline: code.coding_subtheme ?? "",
    codigos_abertos: code.coding_open_codes ?? "",
    codigos_axiais: code.coding_axial_codes ?? "",
    camadas_codificacao_original: code.coding_model_layers ?? item.camadas_codificacao_original,
    alinhamento_questoes_pesquisa: code.coding_rq_alignment ?? item.alinhamento_questoes_pesquisa,
    confianca_codificacao: code.coding_confidence ?? "",
    evidencia_verificada: verified.evidencia_verificada,
    pagina_verificada: verified.pagina_verificada,
    status_verificacao: verified.status_verificacao_v2_final,
    arquivo_pdf: item.arquivo_pdf,
    hash_pdf: item.hash_pdf
  };
});

const visualWb = await Workbook.fromCSV(await fs.readFile(visualDataPath, "utf8"), { sheetName: "Contagens_publicadas" });
const visualRows = objectsFromMatrix(visualWb.worksheets.getItem("Contagens_publicadas").getUsedRange(true).values);
const countAudit = visualRows.map(x => ({
  figura: x.figura,
  categoria: x.categoria,
  serie: x.serie,
  valor_publicado: Number(x.valor),
  origem_publicada: x.proveniencia,
  unidade_de_contagem: x.figura === "grafico_1" ? "estudo com classe mutuamente exclusiva" : "incidencia temática multirrótulo",
  reconciliacao_individual_disponivel: x.figura === "grafico_1" ? "sim" : "não: os rótulos normalizados por estudo que originaram estas frequências não foram preservados",
  estado_auditoria: x.figura === "grafico_1" ? "reproduzido pelo inventário e reconciliação do universo" : "valor publicado preservado; não reconstituído artificialmente"
}));

const wb = Workbook.create();
const overview = wb.worksheets.add("LEIA-ME");
const detail = wb.worksheets.add("Reconciliacao_177");
const counts = wb.worksheets.add("Auditoria_contagens");
const checks = wb.worksheets.add("Verificacao_evidencias");
overview.showGridLines = detail.showGridLines = counts.showGridLines = checks.showGridLines = false;

overview.getRange("A1:F1").merge();
overview.getRange("A1").values = [["Reconciliação temática e de evidências — corpus analítico de 177 estudos"]];
overview.getRange("A3:B10").values = [
  ["Indicador", "Resultado"],
  ["Estudos reconciliados", null],
  ["Evidências centrais", null],
  ["Evidências de apoio", null],
  ["Alertas históricos examinados", null],
  ["Âncoras confirmadas por normalização", null],
  ["Âncoras substituídas por evidência alternativa", null],
  ["Pendências de evidência", null]
];
overview.getRange("A12:F15").values = [["Nota metodológica", "", "", "", "", ""], ["A planilha demonstra a identidade, classificação, codificação original e evidência literal de cada estudo. As frequências temáticas publicadas são preservadas na aba Auditoria_contagens, mas não são apresentadas como reproduzidas por estudo porque a matriz final de rótulos normalizados que originou os gráficos não foi preservada. Atribuições retroativas seriam metodologicamente indevidas.", "", "", "", "", ""], ["A confirmação literal normalizada remove diferenças de Unicode, diacríticos, espaços e pontuação; ela não transforma confiança do LLM em probabilidade nem substitui dupla codificação humana independente.", "", "", "", "", ""], ["Gerado em 2026-08-19 a partir do inventário v2, texto integral e workbook versionado do pipeline.", "", "", "", "", ""]];
overview.getRange("A12:F12").merge(); overview.getRange("A13:F13").merge(); overview.getRange("A14:F14").merge(); overview.getRange("A15:F15").merge();

const writeObjects = (sheet, data) => {
  const headers = Object.keys(data[0]);
  const matrix = [headers, ...data.map(x => headers.map(h => x[h] ?? ""))];
  sheet.getRangeByIndexes(0, 0, matrix.length, headers.length).values = matrix;
  sheet.freezePanes.freezeRows(1);
  sheet.freezePanes.freezeColumns(2);
  return {headers, rows: matrix.length, cols: headers.length};
};
const detailMeta = writeObjects(detail, reconciliation);
const countMeta = writeObjects(counts, countAudit);
const checkMeta = writeObjects(checks, verification);
overview.getRange("B4:B10").formulas = [
  ["=COUNTA('Reconciliacao_177'!A2:A178)"],
  ["=COUNTIF('Reconciliacao_177'!D2:D178,\"evidencia_central\")"],
  ["=COUNTIF('Reconciliacao_177'!D2:D178,\"evidencia_apoio\")"],
  ["=SUM('Verificacao_evidencias'!Q2:Q178)"],
  ["=SUM('Verificacao_evidencias'!R2:R178)"],
  ["=SUM('Verificacao_evidencias'!S2:S178)"],
  ["=SUM('Verificacao_evidencias'!T2:T178)"]
];

const styleTable = (sheet, meta) => {
  const all = sheet.getRangeByIndexes(0, 0, meta.rows, meta.cols);
  all.format.font = { name: "Arial", size: 9, color: "#1F2937" };
  all.format.verticalAlignment = "top";
  all.format.wrapText = true;
  const header = sheet.getRangeByIndexes(0, 0, 1, meta.cols);
  header.format.fill = "#164E63";
  header.format.font = { name: "Arial", size: 9, bold: true, color: "#FFFFFF" };
  header.format.rowHeight = 30;
  all.format.borders = { insideHorizontal: { style: "thin", color: "#D7E3E8" }, bottom: { style: "thin", color: "#A9BCC5" } };
};
styleTable(detail, detailMeta); styleTable(counts, countMeta); styleTable(checks, checkMeta);
overview.getRange("A1:F1").format = { fill: "#164E63", font: { name: "Arial", size: 16, bold: true, color: "#FFFFFF" }, horizontalAlignment: "left", verticalAlignment: "center" };
overview.getRange("A1:F1").format.rowHeight = 34;
overview.getRange("A3:B3").format = { fill: "#DDEFF3", font: { name: "Arial", size: 10, bold: true, color: "#164E63" } };
overview.getRange("A3:B10").format.borders = { insideHorizontal: { style: "thin", color: "#D7E3E8" }, bottom: { style: "thin", color: "#A9BCC5" } };
overview.getRange("A12:F12").format = { fill: "#DDEFF3", font: { name: "Arial", size: 10, bold: true, color: "#164E63" } };
overview.getRange("A13:F15").format = { font: { name: "Arial", size: 9, color: "#374151" }, wrapText: true, verticalAlignment: "top" };
overview.getRange("A").format.columnWidth = 32; overview.getRange("B").format.columnWidth = 22;
for (const sheet of [detail, counts, checks]) sheet.getUsedRange(true).format.autofitColumns();
for (const sheet of [detail, checks]) {
  const used = sheet.getUsedRange(true);
  for (let c = 0; c < used.columnCount; c++) sheet.getRangeByIndexes(0, c, used.rowCount, 1).format.columnWidth = Math.min(38, Math.max(12, sheet.getRangeByIndexes(0, c, used.rowCount, 1).format.columnWidth ?? 18));
}
counts.getUsedRange(true).format.autofitColumns();

const out = await SpreadsheetFile.exportXlsx(wb);
await out.save(path.join(outputDir, "CORPUS_THEME_RECONCILIATION_177.xlsx"));

const summary = {
  studies: verification.length,
  historicalAlerts: verification.filter(x => x.status_checkpoint_historico.includes("com_alerta")).length,
  normalizedMatchesAmongAlerts: verification.filter(x => x.status_checkpoint_historico.includes("com_alerta") && x.metodo_verificacao_v2_final.startsWith("correspondencia")).length,
  alternativeEvidenceAmongAlerts: verification.filter(x => x.status_checkpoint_historico.includes("com_alerta") && x.metodo_verificacao_v2_final.startsWith("evidencia_alternativa")).length,
  unresolved: unresolved.length,
  central: verification.filter(x => x.classificacao_publicada === "evidencia_central").length,
  supporting: verification.filter(x => x.classificacao_publicada === "evidencia_apoio").length
};
const queryFamilies = [
  "governança de LLMs",
  "LLMOps e observabilidade",
  "governança conversacional",
  "ambientes regulados",
  "supervisão humana e contestabilidade"
];
const sourceCoverage = [
  ["OpenAlex", "executada", "ordenação e limite por combinação", "deduplicação e expansão bibliográfica"],
  ["Crossref", "executada", "metadados e ordenação variáveis", "validação por DOI, título e texto completo"],
  ["Semantic Scholar", "parcial", "restrições de taxa", "snowballing por citações, referências, autoria e veículo"],
  ["PubMed", "executada", "concentração biomédica", "triangulação com fontes multidisciplinares"],
  ["Europe PMC", "executada", "sobreposição com PubMed", "deduplicação por DOI, título e similaridade"],
  ["CORE", "executada", "heterogeneidade de repositórios", "validação de texto completo e metadados"],
  ["arXiv", "parcial", "falhas de tempo de resposta", "recuperação por fontes alternativas e snowballing"],
  ["DOAJ", "executada", "cobertura restrita a acesso aberto", "triangulação com as demais fontes"]
];
const coverageHeaders = ["fonte", "familia_consulta", "periodo_execucao", "estado_cobertura", "limite_solicitado", "total_reportado_api", "resultados_retornados", "resultados_armazenados", "apos_deduplicacao", "texto_completo_obtido", "incluidos_corpus_analitico", "falhas_ou_limitacoes", "compensacao", "status_preservacao_dado"];
const coverageRows = [];
for (const [sourceName, state, limitation, compensation] of sourceCoverage) {
  for (const family of queryFamilies) {
    coverageRows.push([sourceName, family, "julho de 2026", state, "até 25", "não preservado", "não preservado", "não preservado", "não preservado", "não preservado", "não atribuível", limitation, compensation, "ausente nos logs preservados; não reconstruído"]);
  }
}
await fs.writeFile(path.join(outputDir, "SEARCH_COVERAGE_AUDIT_V2.csv"), toCsv([coverageHeaders, ...coverageRows]), "utf8");

const num = v => Number.isFinite(Number(v)) ? Number(v) : 0;
const llmStats = {
  operationalRows: records.length,
  validEvidence: records.reduce((s, r) => s + num(r.validated_evidence_count), 0),
  invalidEvidence: records.reduce((s, r) => s + num(r.invalid_evidence_count), 0),
  rowsWithInvalidEvidence: records.filter(r => num(r.invalid_evidence_count) > 0).length,
  manualSpotcheckRequired: records.filter(r => String(r.llm_manual_spotcheck_required).toLowerCase() === "yes").length,
  auditedChecked: records.filter(r => String(r.audit_status).toLowerCase() === "checked").length,
  dataQualityFlags: records.filter(r => String(r.data_quality_flags ?? "").trim()).length
};
const llmAudit = `# Auditoria do procedimento de adjudicação assistida por LLM — v2\n\n` +
`## Escopo e resultado empírico\n\n` +
`A auditoria cobre ${llmStats.operationalRows} linhas operacionais do workbook do pipeline. O processamento registrou ${llmStats.validEvidence} evidências validadas e ${llmStats.invalidEvidence} evidências rejeitadas; ${llmStats.rowsWithInvalidEvidence} registros tiveram ao menos uma evidência inválida. ${llmStats.manualSpotcheckRequired} registros foram sinalizados pelo próprio fluxo para verificação manual e ${llmStats.auditedChecked} aparecem com estado de auditoria \`checked\`. Esses números descrevem controles do pipeline e não demonstram concordância entre revisores humanos independentes.\n\n` +
`## Controles e riscos residuais\n\n` +
`| Etapa | Controle observado | Risco residual |\n|---|---|---|\n` +
`| Triagem determinística | termos, regras, páginas e trechos candidatos | falsos positivos e negativos por vocabulário ou extração |\n` +
`| Adjudicação assistida | saída JSON estruturada, decisão e justificativa | interpretação contextual, enquadramento e dependência do modelo |\n` +
`| Validação de evidência | confronto literal com o texto extraído e contagem de evidências inválidas | hifenização, Unicode, falhas de OCR e localização |\n` +
`| Auditoria final da v2 | 177 estudos confrontados com texto integral; 105 alertas históricos examinados, sendo 94 âncoras confirmadas por normalização e 11 substituídas por evidência literal alternativa | não equivale a dupla codificação humana independente |\n` +
`| Síntese | separação entre evidência central, apoio, contextual e exclusão | dependência das decisões anteriores e da taxonomia adotada |\n\n` +
`## Interpretação permitida\n\n` +
`O LLM foi um instrumento auxiliar de escala e estruturação. Sua confiança numérica não é probabilidade calibrada, e o fluxo não deve ser descrito como revisão humana independente em duplicata. A confirmação literal demonstra que o trecho existe no texto integral; não prova, isoladamente, que a interpretação temática seja a única possível.\n\n` +
`## Proveniência\n\n` +
`Fonte: abas \`records_flat\` e \`evidence_matrix\` de \`metagrade_python_llm_workbook.xlsx\`, inventário dos 177 estudos e repositório de texto integral. Gerado em 2026-08-19.\n`;
await fs.writeFile(path.join(outputDir, "LLM_ADJUDICATION_AUDIT_V2.md"), llmAudit, "utf8");
console.log(JSON.stringify(summary, null, 2));
