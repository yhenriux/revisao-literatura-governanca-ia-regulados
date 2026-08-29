/* Completes the English v2.2 source with invariant references and tables. */
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const target = path.join(root, 'Artigo', 'texto_exportado', 'Artigo_v2.2_para_editar.md');
const source = path.join(root, 'Artigo', 'texto_exportado', 'Artigo_v2.1_para_editar.md');
const tables = `

## References

__REFERENCES__

## Table 1

| ID | Family | Main conceptual blocks |
| --- | --- | --- |
| A | LLM governance | LLMs and generative AI combined with governance, accountability, compliance, auditing, and risk |
| B | LLMOps and observability | LLMOps, observability, monitoring, and guardrails combined with governance and compliance |
| C | Conversational governance | Conversational AI, chatbots, and agents combined with LLMs, governance, and human oversight |
| D | Regulated environments | LLMs and generative AI combined with regulated sectors, risk, auditing, and compliance |
| E | Human oversight and contestability | Human oversight, human-in-the-loop, contestability, and escalation combined with LLMs and chatbots |

## Table 2

| Code | Type | Criterion |
| --- | --- | --- |
| I1 | Inclusion | Object and mechanism: LLM, generative AI, or conversational system with an identifiable governance mechanism. |
| I2 | Inclusion | Context: application in a regulated or high-impact environment, or demonstrated transferability to that context. |
| I3 | Inclusion | Evidence: sufficient full text, published from 2020 to 2026; earlier studies only when foundational. |
| I4 | Inclusion | Suitable design: empirical, technical, conceptual, normative, or review study with substantive evidence. |
| E1 | Exclusion | Incompatible scope: absence of the relevant system or governance mechanism. |
| E2 | Exclusion | Insufficient context: no application, implication, or transferability to a regulated or high-impact environment. |
| E3 | Exclusion | Insufficient evidence: text or metadata inadequate to answer the review questions. |
| E4 | Exclusion | Redundancy or unsuitable role: duplicate, redundant version, internal manuscript, or pre-2020 study without a foundational role. |

## Table 3

| Governance question | Most directly involved layer | Verifiable evidence or control |
| --- | --- | --- |
| Does the system use authorized and current sources? | Technical and organizational | Versioned RAG base, validated source, update date |
| Can a response be reconstructed afterwards? | Technical and regulatory | Logs, traces, prompt, retrieved source, final response |
| Does the user know when the system has limitations? | Interactional | Uncertainty notice, explanation, justified refusal |
| Is there a route to challenge or correct a response? | Interactional and organizational | Appeal, feedback, human review, repair protocol |
| Who is responsible for a failure? | Organizational | Responsibility matrix, roles, incident process |
| Does the system meet risk and compliance requirements? | Regulatory | Impact assessment, documented controls, audit |
| Does the system improve after incidents? | Evolutionary | Incident analysis, knowledge-base review, prompt adjustment, new test |
`;
let text = fs.readFileSync(target, 'utf8');
if (!text.includes('## References')) {
  const original = fs.readFileSync(source, 'utf8');
  const start = original.indexOf('## Referências');
  const end = original.indexOf('## Tabela 1', start);
  if (start < 0 || end < 0) throw new Error('Could not locate v2.1 references.');
  const references = original.slice(start + '## Referências'.length, end).trim();
  fs.writeFileSync(target, text.trimEnd() + tables.replace('__REFERENCES__', references) + '\n', 'utf8');
}
console.log(target);
