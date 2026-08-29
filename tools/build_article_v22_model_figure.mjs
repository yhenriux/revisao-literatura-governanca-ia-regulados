/** Generates the English conceptual model figure for v2.2.
 * It localizes labels only; the five-layer model and lifecycle remain unchanged.
 */
import { createRequire } from "node:module";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
const require = createRequire(import.meta.url);
const sharp = require("sharp");

const root = path.resolve(process.env.REV_LIT_ROOT || process.cwd());
const output = path.join(root, "Recursos_do_artigo", "v2.2", "imagens");
await mkdir(output, { recursive: true });

const esc = (value) => String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
const label = (x, y, title, lines, color) => `<g>
  <rect x="${x}" y="${y}" width="230" height="138" rx="22" fill="#ffffff" stroke="${color}" stroke-width="2"/>
  <text x="${x + 115}" y="${y + 48}" text-anchor="middle" font-size="24" font-weight="700" fill="${color}">${esc(title)}</text>
  <line x1="${x + 50}" y1="${y + 61}" x2="${x + 180}" y2="${y + 61}" stroke="${color}" stroke-width="1.5" opacity=".65"/>
  <text x="${x + 115}" y="${y + 88}" text-anchor="middle" font-size="16" fill="#1e293b">${lines.map((line, index) => `<tspan x="${x + 115}" dy="${index ? 22 : 0}">${esc(line)}</tspan>`).join("")}</text>
</g>`;

const svg = `
<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="980" viewBox="0 0 1100 980">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#173b73"/></marker>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#173b73" flood-opacity=".15"/></filter>
  <radialGradient id="core"><stop stop-color="#1f4c98"/><stop offset="1" stop-color="#0c285f"/></radialGradient>
</defs>
<rect width="1100" height="980" fill="#ffffff"/>
<text x="550" y="68" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="40" font-weight="700" fill="#0c285f">Integrated and feedback-driven governance</text>

<!-- lifecycle -->
<path d="M 302 174 C 450 96, 651 96, 798 174" fill="none" stroke="#173b73" stroke-width="3" stroke-dasharray="3 8" marker-end="url(#arrow)"/>
<path d="M 893 286 C 992 400, 992 597, 888 702" fill="none" stroke="#173b73" stroke-width="3" stroke-dasharray="3 8" marker-end="url(#arrow)"/>
<path d="M 796 809 C 650 884, 447 884, 302 809" fill="none" stroke="#173b73" stroke-width="3" stroke-dasharray="3 8" marker-end="url(#arrow)"/>
<path d="M 205 702 C 108 592, 108 392, 207 286" fill="none" stroke="#173b73" stroke-width="3" stroke-dasharray="3 8" marker-end="url(#arrow)"/>

${label(435, 116, "GOVERN", ["set responsibilities", "and direction"], "#173b73")}
${label(835, 284, "EMBED", ["controls in the", "system lifecycle"], "#173b73")}
${label(835, 612, "DEFINE", ["risk boundaries", "and objectives"], "#173b73")}
${label(435, 744, "EVALUATE", ["evidence, outcomes", "and performance"], "#173b73")}
${label(35, 612, "CONSULT", ["users, experts", "and stakeholders"], "#173b73")}
${label(35, 284, "REVIEW", ["monitor, inspect", "and reassess"], "#173b73")}

<!-- layers -->
${label(435, 220, "Technical", ["RAG, guardrails,", "logs and testing"], "#3867c8")}
${label(690, 404, "Interactional", ["limits, handoff,", "contestability, redress"], "#0f766e")}
${label(575, 600, "Organizational", ["roles, policies,", "internal auditing"], "#a16207")}
${label(295, 600, "Regulatory", ["risk, compliance,", "data protection"], "#7c3aed")}
${label(180, 404, "Evolutionary", ["incidents, feedback,", "controlled change"], "#b91c1c")}

<!-- core and connections -->
<g filter="url(#shadow)"><circle cx="550" cy="486" r="126" fill="url(#core)"/><circle cx="550" cy="486" r="126" fill="none" stroke="#0c285f" stroke-width="4"/></g>
<text x="550" y="466" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="26" font-weight="700" fill="#ffffff">LLM-based</text>
<text x="550" y="498" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="26" font-weight="700" fill="#ffffff">conversational</text>
<text x="550" y="530" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="26" font-weight="700" fill="#ffffff">system</text>
<path d="M 550 358 L 550 358" stroke="#173b73"/>
<g stroke="#173b73" stroke-width="3" marker-end="url(#arrow)">
  <line x1="550" y1="360" x2="550" y2="355"/>
  <line x1="676" y1="456" x2="682" y2="454"/>
  <line x1="635" y1="585" x2="642" y2="597"/>
  <line x1="465" y1="585" x2="455" y2="597"/>
  <line x1="424" y1="456" x2="412" y2="454"/>
</g>
<text x="550" y="931" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#526174">The five layers act together: governance is distributed across technology, interaction, organization, regulation and learning.</text>
</svg>`;

const svgFile = path.join(output, "Figura_7_integrated_conversational_governance.svg");
const pngFile = path.join(output, "Figura_1_modelo_de_cinco_camadas.png");
await writeFile(svgFile, svg, "utf8");
await sharp(Buffer.from(svg)).png({ compressionLevel: 9 }).withMetadata({ density: 360 }).toFile(pngFile);
console.log(pngFile);
