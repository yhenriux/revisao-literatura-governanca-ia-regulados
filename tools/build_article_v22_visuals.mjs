/** Builds English visual resources for the international v2.2 manuscript.
 * Counts are copied from the v2.1 data contract; labels alone are translated.
 */
import { readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const source = path.join(root, "Recursos_do_artigo", "v2.1", "dados_figuras_v21.csv");
const destinationDir = path.join(root, "Recursos_do_artigo", "v2.2");
const destination = path.join(destinationDir, "dados_figuras_v22.csv");

const labels = new Map([
  ["Estudos incluídos", "Included studies"],
  ["Fora do escopo analítico", "Outside analytical scope"],
  ["Versão redundante", "Redundant version"],
  ["Compliance e gestão de risco", "Compliance and risk management"],
  ["Controles técnicos e avaliação", "Technical controls and evaluation"],
  ["Accountability e auditoria", "Accountability and auditing"],
  ["Explicabilidade, confiança e limites", "Explainability, trust and limits"],
  ["Aprendizagem operacional e monitoramento", "Operational learning and monitoring"],
  ["Supervisão humana e escalonamento", "Human oversight and escalation"],
  ["Governança do conhecimento", "Knowledge governance"],
  ["Contestabilidade e reparo", "Contestability and redress"],
  ["Técnica", "Technical"],
  ["Interacional", "Interactional"],
  ["Organizacional", "Organizational"],
  ["Regulatória", "Regulatory"],
  ["Evolutiva", "Evolutionary"],
  ["Evidência central", "Central evidence"],
  ["Evidência de apoio", "Supporting evidence"],
  ["Saúde e medicina", "Health care and medicine"],
  ["Multissetorial", "Multi-sector"],
  ["Tecnologia e operações empresariais", "Technology and business operations"],
  ["Educação", "Education"],
  ["Finanças e seguros", "Finance and insurance"],
  ["Infraestrutura crítica e cibersegurança", "Critical infrastructure and cybersecurity"],
  ["Jurídico e judiciário", "Legal and judicial"],
  ["Governo e setor público", "Government and public sector"],
  ["Avaliação, riscos e qualidade", "Evaluation, risk and quality"],
  ["Supervisão humana e accountability", "Human oversight and accountability"],
  ["Observabilidade, auditoria e monitoramento", "Observability, auditing and monitoring"],
  ["Conhecimento, RAG e guardrails", "Knowledge, RAG and guardrails"],
  ["Confiança, explicabilidade e orientação", "Trust, explainability and guidance"],
  ["Estudos", "Studies"],
  ["Total", "Total"],
]);

let csv = await readFile(source, "utf8");
for (const [from, to] of labels) csv = csv.replaceAll(from, to);
csv = csv.replaceAll("Registro de decisões do corpus analítico único tratado — v2.1", "Normalized corpus decision register — v2.2")
  .replaceAll("Matriz estudo–mecanismo–camada — v2.1", "Study–mechanism–layer matrix — v2.2")
  .replaceAll("Classificação setorial primária reproduzível — v2.1", "Reproducible primary sector classification — v2.2")
  .replaceAll("Síntese de achados derivada das famílias de mecanismos — v2.1", "Findings synthesis derived from mechanism families — v2.2")
  .replaceAll("Coocorrência por estudo na matriz normalizada — v2.1", "Study-level co-occurrence in normalized matrix — v2.2");
await mkdir(destinationDir, { recursive: true });
await writeFile(destination, csv, "utf8");
console.log(destination);
