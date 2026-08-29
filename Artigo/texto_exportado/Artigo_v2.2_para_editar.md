# Conversational Governance in Large Language Model-Based Systems in Regulated Environments: A Systematic Literature Review

## Abstract

**Importance.** Conversational systems based on large language models (LLMs) are increasingly used in health care, finance, government, legal services, insurance, and regulated education, where a generated response may affect clinical guidance, financial advice, access to public services, or the exercise of rights. **Problem.** Relevant research is fragmented across AI governance, Responsible AI, algorithmic accountability, foundation-model risk, human-AI interaction, and sector-specific studies. **Methods.** This PRISMA 2020-guided systematic review combined five conceptual search families across OpenAlex, Crossref, Europe PMC, arXiv, and the Directory of Open Access Journals (DOAJ), with successive retrieval rounds, deduplication, and citation, reference, author, and venue tracing. Decisions were documented for 383 full texts, resulting in 358 unique included studies: 30 central evidence studies and 328 supporting evidence studies. **Results.** Compliance and risk management, accountability and auditing, and monitoring predominate, whereas contestability and repair remain weakly operationalized. The review synthesizes these patterns into a five-layer model—technical, interactional, organizational, regulatory, and evolutionary—that frames conversational governance as a socio-technical system. The model is an analytical proposition derived from the review and requires empirical validation in real regulated settings.

Keywords: conversational governance; large language models; regulated environments; accountability; auditing; human oversight.

## 1. Introduction

Large language models (LLMs) have expanded the use of conversational interfaces in health care, finance, government, legal services, insurance, regulated education, and telecommunications. Open-ended language generation, integration with external sources, and the ability to invoke tools increase the value of such systems, but also introduce risks of hallucination, opacity, bias, misuse, and behavioral instability (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022).

In regulated environments, a conversational response may influence clinical guidance, financial advice, access to public services, legal interpretation, or the exercise of rights. Governance therefore cannot be restricted to model performance. It must cover the chain that produces the response, including prompts, knowledge sources, guardrails, tools, records, human oversight, and the organizational context.

In this article, LLM-based conversational systems are understood as **socio-technical configurations**: arrangements in which models, data, interfaces, guardrails, records, and monitoring mechanisms operate together with people, organizational roles, procedures, rules, and institutional responsibilities. This perspective is adopted because the regulatory effects of a response arise from the interaction of technology, users, organizations, and normative context, rather than from model behavior alone. It enables the joint analysis of the technical, interactional, organizational, regulatory, and evolutionary dimensions identified in the review.

The literature offers important but fragmented foundations. AI governance and Responsible AI establish principles; algorithmic accountability addresses justification, auditing, and responsibility; LLM research examines risk and evaluation; human-AI interaction investigates trust, transparency, and correction; and sectoral work emphasizes compliance and safety. What is missing is a synthesis that integrates these perspectives into mechanisms specific to conversational interaction.

This systematic review identifies and organizes technical, interactional, organizational, regulatory, and evolutionary mechanisms that guide, control, monitor, justify, and correct LLM-based conversational systems in regulated environments. Its main contribution is the Integrated Conceptual Model of Conversational Governance, which presents these mechanisms as five interdependent layers: technical, interactional, organizational, regulatory, and evolutionary.

The review is guided by the following research questions:

**RQ1.** Which conversational-governance mechanisms are reported in the literature on LLM-based systems in regulated environments?

**RQ2.** How do those mechanisms address risk, accountability, human oversight, auditing, explainability, and compliance?

**RQ3.** Which technical, interactional, organizational, regulatory, and evolutionary capabilities are associated with conversational governance?

**RQ4.** Which methodological, sectoral, and operational gaps persist in the literature?

**RQ5.** How does the literature articulate explainability, contestability, repair, and operational learning in LLM-based systems?

The article consolidates dispersed research, organizes mechanisms into analytical families, and proposes a conceptual architecture applicable to research, evaluation, and organizational practice. The next section positions this contribution in relation to the relevant literature.

## 2. Related Work

The relevant literature converges in five streams. First, AI governance and Responsible AI have consolidated principles such as fairness, transparency, privacy, safety, robustness, and accountability, but have also shown that isolated principles do not guarantee responsible implementation (Floridi et al., 2018; Jobin et al., 2019; Mittelstadt, 2019). Frameworks such as the NIST AI Risk Management Framework and the European AI Act connect these principles to risk management, without fully detailing the governance that takes place during conversation (National Institute of Standards and Technology, 2023; European Parliament & Council of the European Union, 2024).

Second, accountability, auditing, and explainability concern the ability of actors to explain and justify their conduct to an evaluative forum, with the possibility of judgment and consequences (Bovens, 2007; Busuioc, 2021). In AI systems, responsibility is distributed across data, models, decisions, effects, and institutions, requiring documentation, traceability, and auditing throughout the lifecycle (Mökander et al., 2023; Raji et al., 2020; Wieringa, 2020).

Third, work on foundation models and generative AI shows that the scale and generality of LLMs propagate risks across applications, while plausible responses can conceal factual errors (Bommasani et al., 2021; Ji et al., 2023). Retrieval-augmented generation (RAG), guardrails, evaluation, and observability mitigate part of these risks but transfer new responsibilities to sources, retrieval, integration, and operations (Gao et al., 2023).

Fourth, human-AI interaction research shows that users need to understand capabilities, limits, uncertainty, and available routes to correction (Amershi et al., 2019; Shneiderman, 2020). In a conversational interface, explanation, confirmation, refusal, escalation, and repair are both design choices and governance controls; linguistic fluency can raise trust beyond the system’s actual competence (Luger & Sellen, 2016; Rapp et al., 2021).

Fifth, studies of AI adoption in regulated sectors show that health care, finance, government, legal services, and insurance share requirements for safety, privacy, auditability, duty of care, and contestability, despite differing in risk and sectoral obligations. In health care, chatbot-evaluation proposals show why safety, user experience, and performance criteria must be assessed together (Hua et al., 2025; Wiens et al., 2019). The gap is therefore not the absence of principles or isolated controls, but the lack of integration between what controls the system, governs the interaction, assigns responsibility, demonstrates compliance, and learns from real use. This gap grounds the five-layer model and motivates the method described next.

## 3. Method

The review followed PRISMA 2020 and recommendations for systematic reviews in software engineering and evidence synthesis (Aromataris et al., 2024; Kitchenham & Charters, 2007; Page et al., 2021; Wohlin, 2014). The protocol combined corpus identification and consolidation, eligibility and quality assessment, evidence validation, and thematic synthesis for conceptual development.

The search combined structured queries and bibliographic expansion. The final retrieval used five sources and services—**OpenAlex, Crossref, Europe PMC, arXiv, and the Directory of Open Access Journals (DOAJ)**—across five conceptual families: LLM governance; LLMOps and observability; conversational governance; regulated environments; and human oversight and contestability. References, citing works, authors, and publication venues were traced to broaden coverage.

**Table 1. Conceptual families and operationalization of the search strategy**

Note. Queries were adapted to the syntax and indexing rules of each source and service.

Source. Authors’ own elaboration based on search-execution records.

The bibliographic retrieval was performed in successive rounds, combining the five conceptual families, the five sources and services, and complementary strategies for tracing references, citations, authorship, and venues. In each round, results were expanded progressively to the hundredth position for each query–source combination and deduplicated using persistent identifiers and, secondarily, normalized title, authorship, and year. Retrieval stability was assessed through sensitivity analysis, examining whether later rounds added eligible studies not found in earlier rounds. This procedure assessed search breadth without assuming that the first results were necessarily the most relevant.

Snowballing included cited references, citing works, related works, and controlled expansions by author and venue. All records were consolidated and deduplicated by DOI, exact title, and textual similarity, with ambiguous groups checked manually. The expanded execution recorded 1,342 occurrences and 1,074 unique records after internal deduplication; selection decisions were documented for 383 full texts.

Studies were included when they addressed LLMs, generative AI, or conversational systems and reported governance mechanisms relevant to regulated or high-impact environments. The final analytical corpus contains 358 unique studies: 30 central evidence studies and 328 supporting evidence studies. Twenty-four additional records were outside the review scope.

All 358 studies are individually identified in the project’s open-source virtual bibliographic catalog.[^1] The catalog provides the reference, classification, sector, mechanism family, normalized layer, PDF, hash, evidence page, and supporting excerpt. The study–mechanism–layer matrix is the source used to recalculate tables and figures, while the traced PDFs are the source of full text.

[^1]: Bibliographic catalog of the research: *Conversational governance in LLM-based systems*. GitHub Pages. https://yhenriux.github.io/revisao-literatura-governanca-ia-regulados/

**Table 2. Consolidated inclusion and exclusion criteria**

Note. The table summarizes the criteria used to select the studies.

Source. Review methodological protocol.

Full-text extraction recorded pages, extraction quality, and relevant excerpts. Thematic synthesis combined open coding, axial grouping, and iterative comparison, following Braun and Clarke (2006). A deterministic screening step located terms and literal evidence; the LLM then received metadata and selected excerpts, produced structured fields, and was instructed not to infer missing information. The model suggested eligibility, classification, and codes, but did not make the final scientific decision.

Classifications suggested by the LLM from full texts were validated through human assessment by checking the corresponding excerpts and pages in the original evidence. Any divergence was resolved through reading of the primary source.

Adapted CASP/JBI instruments were used to identify methodological limitations and qualify interpretation (Aromataris et al., 2024; Critical Appraisal Skills Programme, n.d.), without determining eligibility or the distinction between central and supporting evidence. CERQual dimensions informed reflection on coherence, adequacy, relevance, and limitations of qualitative findings, following Lewin et al. (2018); no formal confidence ratings were assigned to findings incompatible with that approach.

A study was classified as central evidence only when it simultaneously met three conditions: direct treatment of governance, supervision, risk, accountability, auditing, compliance, or controlled operation of LLMs or conversational systems; an explicit relationship with a regulated or high-impact environment, or a demonstrably transferable mechanism; and a substantive contribution to at least one review question through an empirical result, systematic synthesis, evaluated mechanism, or conceptual architecture. Eligible studies with a peripheral, contextual, or only transferable contribution were classified as supporting evidence.

The research questions and initial literature supplied sensitizing dimensions rather than a closed final scheme. Analysis combined open coding, axial grouping, constant comparison, and iterative refinement. Consolidation of these patterns produced the five layers, which were then applied as a normalized vocabulary to the corpus. Frequencies were calculated from application of that scheme to included studies, following the criteria and procedures described above.

The analytical categories follow a multi-label coding rule: a study may be associated with more than one mechanism family, sector, finding, or layer when the text provides corresponding evidence. Counts represent coding occurrences rather than necessarily distinct studies; category totals should therefore not be summed to reconstruct corpus size. In co-occurrence tables, each cell reports the number of studies coded simultaneously in the row category and the column category.

Figure 1 shows the documented composition of the corpus, from identification through full-text selection and inclusion.

**Figure 1. Composition of documented decisions in the full selection**

Source. Authors’ own elaboration based on the consolidated review database.

## 4. Results and Integrated Conceptual Model

Mechanism families and conceptual layers were coded in a multi-label manner, so a study could contribute to different categories. Frequencies represent thematic incidence, not necessarily implementation or empirical validation.

Figure 2 compares the incidence of the eight normalized mechanism families and the number of central evidence studies in each. The final marker represents the total number of studies, whereas the initial marker represents the subset classified as central evidence.

**Figure 2. Incidence of mechanism families and presence of central evidence**

Source. Authors’ own elaboration based on the analytical corpus.

Compliance and risk management had the greatest coverage, with 339 studies (94.7% of the corpus) and 29 of the 30 central evidence studies (96.7%). Accountability and auditing appeared in 250 studies (69.8%), human oversight and escalation in 243 (67.9%), and operational learning and monitoring in 232 (64.8%). Contestability and repair had residual incidence, with three studies (0.8%) and no central evidence. The main gap thus shifts from risk identification to the capacity for recourse, correction, and repair.

Reorganizing the codes across the five conceptual layers makes it possible to observe the consolidation of each dimension. Figure 3 compares central and supporting evidence across the technical, interactional, organizational, regulatory, and evolutionary layers.

**Figure 3. Distribution of studies across the conceptual-model layers**

Source. Authors’ own elaboration based on the analytical corpus.

The regulatory layer was identified in 339 studies (94.7% of the corpus) and the organizational layer in 324 (90.5%), followed by the technical layer with 284 (79.3%). The interactional and evolutionary dimensions accounted for 248 (69.3%) and 233 studies (65.1%), respectively. Differences in incidence across layers are moderate, but the rarity of contestation mechanisms shows that interactional codes do not by themselves amount to effective user agency.

## 4.1. Technical and Operational Mechanisms

The first mechanism family comprises technical components that make it possible to control, observe, constrain, evaluate, or correct the behavior of LLM-based systems. These mechanisms include RAG, guardrails, logs, tracing, observability, red teaming, continuous evaluation, post-deployment monitoring, versioning, technical documentation, and knowledge-base governance.

The foundation-model literature indicates that LLMs introduce specific risks of opacity, hallucination, bias, harmful-content generation, and difficulty of evaluation at scale (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022). Technical governance consequently demands more than traditional performance metrics. It must record the context of use, trace inputs and outputs, monitor failures, control knowledge sources, and assess system behavior in ordinary and exceptional situations.

Retrieval-augmented generation (RAG) is relevant because it connects the generative model to external knowledge sources. This arrangement can reduce exclusive reliance on parametric memory and allow greater control over recency, traceability, and the domain of responses (Gao et al., 2023). RAG alone, however, does not solve governance. Response quality also depends on knowledge-base curation, retrieval strategy, document ranking, source updating, and how evidence is presented to the user.

Guardrails also have a central role in recent literature. They may operate as blocking rules, safety filters, risk classifiers, scope limits, format validation, content restrictions, or response policies. In conversational systems, these mechanisms help reduce dangerous, legally sensitive, discriminatory, or out-of-domain responses. Yet guardrails may fail when they are treated only as technical filters rather than integrated with human-review processes, incident monitoring, auditing, and continuous updating.

Logs, tracing, and observability extend governance by recording system behavior in production. Observability makes it possible to inspect prompts, responses, retrieved sources, invoked tools, latency, errors, escalation rates, safety evaluations, user feedback, and critical events. In regulated environments, such records matter for auditing, incident investigation, continuous improvement, and accountability. Algorithmic-audit research emphasizes that documentation and traceability must cover the system lifecycle, not only the modeling phase (Raji et al., 2020).

Continuous evaluation is another technical-operational mechanism. It includes pre-deployment testing, red teaming, evaluation with reference datasets, post-deployment monitoring, and regression analysis when prompts, models, knowledge bases, or policies change. For LLMs, evaluation must address factuality, safety, robustness, domain fit, consistency, privacy, bias, toxicity, refusal capability, source traceability, and behavior under uncertainty. This logic connects technical governance to risk management because testing becomes evidence of control rather than merely an indicator of quality.

Taken together, the evidence indicates that technical and operational mechanisms provide the instrumental-control layer of conversational governance. They make system behavior observable, constrainable, and correctable; their effectiveness depends on their connection to the human, organizational, and regulatory mechanisms considered in the following sections.

## 4.2. Human Oversight, Escalation, and Contestability

Human-oversight and escalation mechanisms were identified in 243 studies (67.9% of the corpus), including 14 central evidence studies (46.7% of central evidence); contestability and repair appeared in only three studies (0.8%), with no central evidence. This difference indicates broad attention to human intervention but limited operationalization of formal mechanisms for questioning, reviewing, or repairing responses.

Human-AI interaction research shows that automation quality depends on how a system communicates its capabilities, limitations, uncertainties, and possibilities for correction (Amershi et al., 2019). In conversational systems, this communication occurs not only in administrative dashboards or technical documents, but in the dialogue itself, when a system acknowledges limits, requests confirmation, guides a user, transfers them to human assistance, or explains why it cannot carry out an action.

Escalation is a central interactional mechanism. It defines when and how the system transfers an interaction to a person, team, specialized channel, or review process. In customer service, health care, finance, and the public sector, escalation is not merely a UX convenience. It acts as a safeguard against error, uncertainty, ambiguity, user distress, legal risk, misunderstanding, or the need for contextual judgment. Chatbot research shows that user experience deteriorates when conversational agents exceed their perceived capabilities or fail to offer clear paths to repair (Følstad & Brandtzaeg, 2020; Luger & Sellen, 2016).

Contestability and repair extend human oversight beyond the moment of response. Contestability is the possibility of questioning, reviewing, or disputing an AI-mediated output, recommendation, or decision. Repair refers to mechanisms through which errors are recognized, corrected, and incorporated into future improvements. In LLM-based systems, these mechanisms are especially important because errors may be expressed in fluent and persuasive language, making uncertainty or inconsistency harder to detect immediately.

Effective human oversight requires clearly defined roles and criteria. It is not enough to claim that a human is in the loop if it is unclear who intervenes, when, with what authority, based on what evidence, and under what responsibility. This point connects human oversight to organizational accountability: merely symbolic intervention can create an appearance of control without producing real responsibility.

## 4.3. Accountability, Auditing, and Compliance

The incidence of accountability, auditing, compliance, and risk-management mechanisms indicates broad recognition of responsibilities and obligations, although their operationalization varies across documentation, technical controls, audits, and organizational structures.

Algorithmic accountability shifts the discussion from technical performance to relationships of responsibility. Bovens (2007) defines accountability as a relationship in which an actor must explain and justify conduct before an evaluative forum. In AI systems, this relationship becomes distributed because decisions and responses may involve developers, model providers, product teams, knowledge curators, risk managers, legal functions, human operators, and user organizations. Wieringa (2020) shows that algorithmic accountability may concern data, models, decisions, effects, and institutions, reinforcing its socio-technical nature.

Auditing operationalizes part of that accountability. It may occur before deployment, during development, in production, or after incidents. AI audits can examine data, documentation, models, metrics, decision processes, risks, impacts, and mitigation mechanisms (Raji et al., 2020). For LLMs, auditing also needs to include prompts, system policies, retrieved knowledge bases, connected tools, guardrails, conversational logs, escalation records, and responses generated in sensitive contexts.

Regulatory compliance adds external criteria to governance. In regulated sectors, AI systems must observe data-protection rules, safety requirements, consumer rights, sectoral rules, professional duties, and documentation requirements. The NIST AI Risk Management Framework proposes governance, mapping, measurement, and risk-management functions that organize responsibilities across the AI lifecycle (National Institute of Standards and Technology, 2023). A risk-based approach also appears in the European AI Act, which differentiates obligations according to the potential for harm and the application context (European Parliament & Council of the European Union, 2024).

In conversational systems, compliance cannot be treated only as a documentation check. It must be reflected in system behavior, the answers given, scope limits, refusals, interaction records, data protection, knowledge-retrieval practice, and contestation mechanisms. A financial, clinical, or governmental assistant may be formally documented yet still fail if it guides users inappropriately, conceals uncertainty, does not escalate critical cases, or does not preserve audit trails.

Documentation is likewise part of accountability. Model cards, system cards, evaluation reports, change records, risk matrices, use policies, and architecture descriptions allow internal and external actors to understand the system’s limits, assumptions, and responsibilities. For LLMs, documentation must accompany not only the model but the conversational system as a whole: orchestration, prompts, data, tools, channels, metrics, safety mechanisms, and associated human processes.

## 4.4. Applications and Regulated Domains

Classification by primary domain revealed concentration in health care and medicine, with 150 studies (41.9% of the corpus). A further 112 studies (31.3%) were multisectoral or cross-cutting, while 47 (13.1%) focused on technology and business operations.

Other regulated environments had lower coverage: education included 17 studies (4.7%); finance and insurance, 14 (3.9%); critical infrastructure and cybersecurity, 10 (2.8%); legal and judicial settings, four (1.1%); and government and the public sector, four (1.1%).

Of the 30 central evidence studies, 19 belong to health care and medicine, six to technology and business operations, four are multisectoral, and one focuses on finance and insurance. The remaining domains have supporting studies but no study classified as central evidence.

Figure 4 presents the distribution by primary domain. Because domains are mutually exclusive, bar length represents their share of the analytical corpus.

**Figure 4. Sectoral composition of the analytical corpus**

Source. Authors’ own elaboration based on the analytical corpus.

Health care and medicine account for 41.9% of the corpus, contrasting with the limited coverage of the remaining specific domains. This distribution constrains direct transfer of findings and calls for model validation in environments with different obligations, risks, users, consequences, and professional practices.

## 4.5. Review Findings

Because findings were coded in a multi-label manner, these quantities represent thematic incidence rather than mutually exclusive categories. Identifying a mechanism does not necessarily mean that it has been implemented or empirically validated, since part of the literature presents it as a normative principle, architectural requirement, recommendation, or research agenda.

The five findings differ both in thematic coverage and in the number of central evidence studies that support them. Figure 5 combines these dimensions: the final marker represents the total number of studies, and the initial marker indicates the central-evidence subset.

**Figure 5. Thematic coverage and central-evidence density by finding**

Source. Authors’ own elaboration based on the analytical corpus.

The predominance of the first finding reflects the attention devoted to metrics, benchmarks, factuality, hallucination, robustness, safety, and validation. Despite this coverage, the literature remains fragmented in translating foundation-model risks into consistent evaluation protocols and acceptance criteria for conversational systems in production (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022).

For LLM-based systems, traditional performance metrics are insufficient to evaluate governance. Accuracy, intent coverage, correct-response rate, or user satisfaction do not fully capture risks such as untraceable responses, inappropriate sources, absent escalation, decision opacity, breaches of institutional policy, or failures to communicate uncertainty. Evaluation needs to include factuality, safety, robustness, traceability, consistency, explainability, privacy, domain fit, and refusal capability.

Methodological quality is another critical issue. Part of the literature is conceptual, normative, or technical, while another part is empirical, experimental, or applied to specific domains. This heterogeneity makes direct comparisons difficult and requires flexible critical-appraisal tools. Combining methodological appraisal, thematic analysis, and assessment of evidence confidence makes it possible to distinguish studies with strong empirical support, foundational conceptual contributions, and technical proposals that remain lightly validated.

In interpretation, this appraisal was used to calibrate the strength of the language: empirical results and systematic syntheses were distinguished from frameworks, normative principles, and technical proposals. No study was automatically excluded because of quality, and appraisal was not converted into an aggregate score across incompatible designs.

The difference between normative references to oversight and explicit operational mechanisms indicates that accountability, oversight, and human control are frequently advocated without equivalent detail about actors, authority, evidence, and responsibilities.

This gap is especially relevant in conversational systems. In an interface based on natural language, human oversight occurs not only during training or model validation. It can take place during service delivery, in escalation flows, in review of sensitive answers, in knowledge-base curation, in incident analysis, and in policy updates. Conversational governance therefore requires an architecture of distributed oversight throughout the system lifecycle.

Operational accountability depends on turning human oversight into an institutional process. This involves defining roles, escalation criteria, risk levels, evidence required for review, contestation mechanisms, team responsibilities, and consequences of failure. Without such a structure, human oversight can become a merely declaratory safeguard that cannot produce real accountability.

Observability, auditing, and post-deployment monitoring were identified in 276 studies (77.1% of the corpus), of which 23 were central and 253 supporting. These studies address auditing, logs, tracing, telemetry, documentation, continuous monitoring, and incident investigation across the lifecycle.

Observability should not be treated only as a technical monitoring capability. It is a condition for investigation, learning, and accountability. Without adequate logs and tracing, it becomes difficult to reconstruct why a response was produced, which sources were used, which rules were applied, whether escalation was attempted, and which components contributed to a failure.

Comparison with the evolutionary layer shows that monitoring is treated primarily as traceability or compliance and less as a systematic process of learning, updating, and adaptation after incidents.

Knowledge, RAG, and guardrails were associated with 160 studies, including 14 central evidence studies. The narrower knowledge-governance family appeared in 44 studies, indicating that work on RAG or guardrails does not always address curation, provenance, validity, authority, and source versioning.

This finding shifts part of governance from the model to information governance. In regulated environments, knowledge bases need authorship, version, validity, update date, scope, authorized source, and use criteria. An incorrect conversational response can result from model failure, but also from an outdated document, an unsuitable source, poorly segmented chunks, irrelevant retrieval, or the absence of source-priority rules.

The research opportunity lies in developing governance models that integrate RAG, knowledge curation, guardrails, and human oversight. Such integration must address both information quality and interaction quality. In conversational systems, retrieving the correct source is insufficient; the response must be presented appropriately for the risk, user profile, degree of uncertainty, and institutional responsibilities involved.

Trust, explainability, and user-oriented governance were identified in 278 studies (77.7% of the corpus), including 17 central evidence studies and 261 supporting studies. The widespread presence of transparency and communication of limits contrasts with the low incidence of mechanisms that allow a response to be challenged or repaired.

This requires distinguishing internal explainability, directed at developers and auditors, from user-oriented explainability, directed at understanding, contestation, and repair. The former may involve logs, metrics, traces, technical documents, and component analysis. The latter must appear as an understandable response, source indication, uncertainty warning, justified refusal, explicit limit, or referral to human support.

The analysis reveals a substantive asymmetry: the literature favors mechanisms that inform users about capabilities and limits but offers less coverage for mechanisms that allow them to act on an inadequate response, obtain review, or seek repair.

Contestability and repair are practical extensions of explainability. An explanation that does not enable a subsequent action may have limited value in regulated environments. Conversational governance should allow users to question answers, request review, correct information, contact human support, and understand the available routes to contestation. This dimension brings governance, conversational UX, and accountability together.

## 4.6. Synthesis of Findings

The synthesis integrates the results into an uneven configuration: controls that stabilize models and institutional responsibilities are more consolidated than capabilities expressed in dialogue and post-incident learning. This difference guides the model but does not imply a linear sequence or a maturity scale.

The concentration of the literature in health care and medicine, representing 41.9% of the corpus and 19 of the 30 central evidence studies, limits direct transfer of findings. Finance, education, legal, governmental, and critical-infrastructure contexts have fewer central evidence studies and require validation in their own settings.

The identified capabilities do not operate in isolation. RAG without curation can amplify unsuitable information; guardrails without monitoring can fail silently; human oversight without defined roles can become symbolic; logs without an audit process may not produce accountability; and explainability without a user-action mechanism may not produce correction. The analytical contribution of the review is to show that governance depends on integration across the five dimensions, not on isolated controls.

To examine how mechanisms are distributed across the five layers, code co-occurrence was calculated at the study level. Figure 6 presents the number of studies simultaneously associated with each mechanism family and conceptual layer.

**Figure 6. Co-occurrence between mechanism families and governance layers**

Source. Authors’ own elaboration based on normalized corpus codes.

The strongest co-occurrences link compliance and risk management to the regulatory and organizational layers; accountability and auditing are also concentrated in these dimensions. The residual incidence of contestability and repair shows that institutional and technical coverage does not automatically entail user capacity to act.

## 4.7. Five-Layer Model

Based on the review findings, this section proposes an Integrated Conceptual Model of Conversational Governance for LLM-based systems deployed in regulated environments. The model organizes conversational governance as a socio-technical configuration comprising five interdependent layers: technical, interactional, organizational, regulatory, and evolutionary.

The proposition recognizes that LLM-based systems are not governed only by the foundation model. Their operation involves prompts, knowledge bases, retrieval mechanisms, external tools, guardrails, conversational interfaces, organizational policies, human oversight, audit records, and regulatory requirements. Governance must therefore cover the full conversational system rather than the isolated algorithmic component.

The model proposes five integrated layers.

The technical layer comprises control, observability, and operational-safety mechanisms. It includes RAG, guardrails, logs, tracing, monitoring, red teaming, continuous evaluation, versioning, and regression testing. This layer addresses the need to make system behavior observable, evaluable, and technically controllable.

The interactional layer addresses governance in the relationship between system and user. It includes explanation, communication of limits, confirmation, handoff, escalation, contestation, repair, and guidance on next steps. This layer is needed because conversational systems govern part of the experience through language itself.

The organizational layer defines roles, responsibilities, policies, processes, documentation, and internal decision structures. It includes committees, responsibility matrices, knowledge governance, escalation criteria, review flows, and internal audit processes. This layer prevents responsibility from being dispersed across the model, provider, product, operations, and business function.

The regulatory layer connects the system to sectoral rules, risks, evidence, and duties. It includes compliance, data protection, impact assessment, audit trails, risk criteria, regulatory documentation, and alignment with domain-specific obligations. It is especially relevant in health care, finance, government, legal services, insurance, regulated education, and telecommunications.

The evolutionary layer concerns operational learning and controlled system adaptation. It includes incident analysis, feedback loops, knowledge-base updating, prompt review, guardrail adjustments, continuous improvement, and post-deployment monitoring. This layer recognizes that governance does not end at deployment: it must follow actual system behavior in use.

Integrating quantitative and thematic results made it possible to organize mechanisms in a systemic model. Figure 7 represents the five layers as interdependent dimensions acting on the full conversational system, including model, response, interaction, knowledge, organization, and regulatory environment.

**Figure 7. Integrated Conceptual Model of Conversational Governance**

Note. Arrows represent reciprocal dependency and feedback, rather than a rigid temporal sequence.

Source. Authors’ own elaboration from the review synthesis.

No layer produces governance autonomously. The regulatory layer defines requirements and limits; the organizational layer translates them into responsibilities and processes; the technical layer implements controls and records; the interactional layer manifests governance in dialogue; and the evolutionary layer turns incidents, use, and feedback into controlled adaptation.

The model is not a rigid linear sequence. Layers operate interdependently. A technical mechanism such as RAG depends on organizational governance of the knowledge base and may be subject to regulatory traceability requirements. An interactional mechanism such as handoff depends on technical criteria for risk detection and organizational service processes. A regulatory audit depends on technical logs, organizational documentation, and interaction evidence.

This interdependence indicates that conversational governance is a systemic capability. It requires coordination across technology, conversational design, operations, risk, compliance, legal, security, data, and business functions.

In regulated environments, the model should be applied proportionately to the risk of the interaction. Simple informational interactions may require basic controls such as logs, scope limits, and knowledge-base updates. Interactions involving clinical, financial, legal, administrative, or rights-related guidance require stronger controls, including explanation, source traceability, human oversight, contestability, auditing, and regulatory documentation.

The model’s principal contribution is to integrate dimensions that appear fragmented in the literature. AI governance provides principles and risk frameworks; algorithmic accountability provides a theory of responsibility; LLM literature describes technical and social risks; human-AI interaction offers guidance for transparency, trust, and correction; and regulatory literature defines sectoral obligations and compliance criteria. The proposed model brings these contributions together around the conversational unit of analysis.

Conversational governance is therefore defined in this study as the set of technical, interactional, organizational, regulatory, and evolutionary mechanisms that guide, control, monitor, justify, and correct the behavior of LLM-based systems in interactions mediated by natural language, especially when such systems operate in regulated or high-impact environments.

This definition extends governance beyond model control. It includes governance of the response, interaction, knowledge source, escalation, repair, evidence, responsibility, and operational learning. It provides a basis for analysis of existing systems, design of new systems, auditing of production applications, and development of empirical research agendas.

**Table 3. Operational questions and examples of control evidence**

Note. The questions synthesize recurring evidence; their organization into five layers and use as a diagnostic structure are propositions of the model and remain subject to empirical validation. Application should be calibrated to system risk, sector, and autonomy.

Source. Authors’ own elaboration based on the Integrated Conceptual Model.

The table translates the five layers into criteria that can guide architecture review, risk assessment, auditing, interaction design, and post-deployment monitoring. It does not replace specific regulatory requirements, but offers a shared structure for organizing evidence and responsibilities.

This article presents a first conceptual proposition derived from systematic literature synthesis. The five layers organize recurring patterns identified in the corpus. The model is not a maturity scale, standard, certification, or regulatory requirement, nor does it replace sectoral standards; its external validity and operational usefulness require examination through case studies, expert evaluation, and applications in real regulated systems.

## 5. Discussion

The observed imbalance suggests that institutionalization of Responsible AI still favors formalizable controls and internal responsibilities, whereas user agency and learning after failures remain less operationalized. This converges with the critique that principles, although established, do not guarantee responsible implementation without institutional and operational mechanisms (Floridi et al., 2018; Jobin et al., 2019; Mittelstadt, 2019).

The risks attributed to foundation models—opacity, hallucination, bias, harmful content, and difficulty of evaluation—explain the centrality of guardrails, testing, and observability (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022). The review also shows that model controls are insufficient. RAG transfers part of the risk to curation, provenance, and source updating; logs produce governance only when they feed auditing; and monitoring produces learning only when incidents lead to controlled change (Gao et al., 2023).

The predominance of regulatory and organizational layers reinforces the distributed nature of accountability. Explaining and justifying conduct requires identifiable actors, evaluative forums, and consequences (Bovens, 2007), while algorithmic accountability may concern data, models, decisions, effects, and institutions (Wieringa, 2020). For conversational systems, the relevant chain also includes prompts, retrieved bases, tools, policies, and human intervention. The proposed model connects this chain to lifecycle auditing advocated by Raji et al. (2020), linking technical evidence to organizational responsibilities.

Human-AI interaction research helps interpret this gap: users need to understand capabilities and limits and have effective means of correction (Amershi et al., 2019; Shneiderman, 2020). Because linguistic fluency can raise trust without raising competence, user-oriented explainability should enable a subsequent action—correcting information, requesting review, or contacting human support—rather than merely present a justification (Luger & Sellen, 2016; Rapp et al., 2021).

This distinction bounds the contribution: mechanisms and incidence patterns derive from the corpus, whereas their arrangement is an integrative synthesis. Its value lies in making dispersed dependencies explicit and in formulating verifiable categories for empirical studies, audits, and organizational design without pre-empting effectiveness that has not yet been demonstrated.

Applying the model involves trade-offs. Observability improves traceability but must respect privacy and data minimization; transparency may support calibrated trust but should not expose security controls; human oversight reduces risk only when authority, capacity, and time are available, otherwise creating bottlenecks or symbolic safeguards; and standardization facilitates auditing but does not remove the need for domain calibration. These tensions prevent any layer from being maximized in isolation and reinforce risk-proportionate application.

In health care, clinical interactions require validated sources, professional oversight, and escalation; in finance, traceability, prevention of inappropriate advice, and contestation are salient; in government, legitimacy, access to rights, and avenues of recourse matter; and, in legal services, insurance, and regulated education, the distinction between information, recommendation, and decision is central. The NIST AI RMF and the European AI Act support a risk-based approach, but translation into conversation depends on the context and obligations of each sector (National Institute of Standards and Technology, 2023; European Parliament & Council of the European Union, 2024).

Interpretation must take account of sectoral concentration and heterogeneity among empirical, conceptual, normative, and technical studies. Ordering, indexing, and availability mechanisms may influence retrieval; combining multiple sources, later-position analysis, bibliographic tracing, and deduplication reduces that dependence but does not demonstrate exhaustiveness. Validation against full text and decision records supports transparent, reproducible classification.

Future research should validate the model in distinct organizations and sectors, compare oversight arrangements, test guardrails and RAG in production, and develop measures for user action and operational learning. Longitudinal studies can examine whether logs, incidents, and feedback result in controlled improvement. This validation should combine performance, process analysis, user experience, incidents, and compliance evidence, distinguishing the formal presence of controls from their effectiveness.

## 6. Conclusion

**RQ1—Reported mechanisms.** The review identifies eight normalized families of conversational-governance mechanisms, with particularly broad coverage of compliance and risk management, accountability and auditing, human oversight and escalation, and operational monitoring. The evidence shows that governance is distributed across technical controls, interaction design, organizational processes, regulatory obligations, and learning mechanisms.

**RQ2—Risk and accountability.** The mechanisms address risk and accountability only when technical evidence, such as logs, guardrails, retrieved sources, and evaluation records, is connected to roles, escalation processes, auditing, and sectoral obligations. Compliance must therefore be visible in system behavior as well as in documentation.

**RQ3—Associated capabilities.** The review associates conversational governance with the ability to observe and constrain system behavior, communicate limits, transfer high-risk cases, allocate responsibility, preserve audit trails, and adapt after incidents. The five-layer model organizes these interdependent capabilities without treating them as a maturity scale.

**RQ4—Persistent gaps.** The literature is concentrated in health care and medicine and provides less central evidence for finance, education, legal, governmental, and critical-infrastructure contexts. It also offers much stronger coverage of risk identification and institutional control than of formal mechanisms for user contestation, correction, and repair.

**RQ5—Explainability, contestability, repair, and learning.** Explainability is most valuable when it enables subsequent action: users must be able to understand limits, question a response, request review, correct information, or reach human support. Contestability and repair remain weakly operationalized, while operational learning requires incidents and feedback to be translated into controlled system changes.

The Integrated Conceptual Model organizes this evidence into five interdependent layers—technical, interactional, organizational, regulatory, and evolutionary—and shifts the unit of analysis from an isolated model to the socio-technical conversational system that produces, presents, records, and corrects responses. Its theoretical contribution is an integrated account of dispersed governance mechanisms; its practical contribution is a set of verifiable categories for architecture, oversight, auditing, user action, and controlled change. As a proposition derived from systematic synthesis, the model should now be examined through case studies, expert evaluation, and real applications in regulated settings.

## References

Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for human-AI interaction. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (Article 3, pp. 1-13). Association for Computing Machinery. https://doi.org/10.1145/3290605.3300233

Aromataris, E., Lockwood, C., Porritt, K., Pilla, B., & Jordan, Z. (Eds.). (2024). JBI manual for evidence synthesis. JBI. https://doi.org/10.46658/JBIMES-24-01

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., Brynjolfsson, E., Buch, S., Card, D., Castellon, R., Chatterji, N., Chen, A., Creel, K., Davis, J. Q., Demszky, D., . . . Liang, P. (2021). On the opportunities and risks of foundation models [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2108.07258

Bovens, M. (2007). Analysing and assessing accountability: A conceptual framework. European Law Journal, 13(4), 447-468. https://doi.org/10.1111/j.1468-0386.2007.00378.x

Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. Qualitative Research in Psychology, 3(2), 77-101. https://doi.org/10.1191/1478088706qp063oa

Busuioc, M. (2021). Accountable artificial intelligence: Holding algorithms to account. Public Administration Review, 81(5), 825-836. https://doi.org/10.1111/puar.13293

Critical Appraisal Skills Programme. (n.d.). CASP checklists. https://casp-uk.net/casp-tools-checklists/

European Parliament, & Council of the European Union. (2024). Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence and amending Regulations and Directives. Official Journal of the European Union. https://eur-lex.europa.eu/eli/reg/2024/1689/oj

Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., Luetge, C., Madelin, R., Pagallo, U., Rossi, F., Schafer, B., Valcke, P., & Vayena, E. (2018). AI4People: An ethical framework for a good AI society. Minds and Machines, 28, 689-707. https://doi.org/10.1007/s11023-018-9482-5

Følstad, A., & Brandtzaeg, P. B. (2020). Users’ experiences with chatbots: Findings from a questionnaire study. Quality and User Experience, 5, Article 3. https://doi.org/10.1007/s41233-020-00033-2

Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., & Wang, H. (2023). Retrieval-augmented generation for large language models: A survey [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2312.10997

Hua, Y., Xia, W., Bates, D., Hartstein, G. L., Kim, H. T., Li, M., Nelson, B. W., Stromeyer, C., IV, King, D., Suh, J., Zhou, L., & Torous, J. (2025). Standardizing and scaffolding health care AI-chatbot evaluation: Systematic review. JMIR AI, 4, Article e69006. https://doi.org/10.2196/69006

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Chen, A., Madotto, A., & Fung, P. (2023). Survey of hallucination in natural language generation. ACM Computing Surveys, 55(12), Article 248. https://doi.org/10.1145/3571730

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. Nature Machine Intelligence, 1, 389-399. https://doi.org/10.1038/s42256-019-0088-2

Kitchenham, B., & Charters, S. (2007). Guidelines for performing systematic literature reviews in software engineering (EBSE Technical Report EBSE-2007-01). Keele University and Durham University.

Lewin, S., Bohren, M., Rashidian, A., Munthe-Kaas, H., Glenton, C., Colvin, C. J., Garside, R., Noyes, J., Booth, A., Tunçalp, Ö., Wainwright, M., Flottorp, S., Tucker, J. D., & Carlsen, B. (2018). Applying GRADE-CERQual to qualitative evidence synthesis findings: Paper 2. How to make an overall CERQual assessment of confidence and create a Summary of Qualitative Findings table. Implementation Science, 13(Suppl. 1), Article 10. https://doi.org/10.1186/s13012-017-0689-2

Luger, E., & Sellen, A. (2016). Like having a really bad PA: The gulf between user expectation and experience of conversational agents. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (pp. 5286-5297). Association for Computing Machinery. https://doi.org/10.1145/2858036.2858288

Mittelstadt, B. (2019). Principles alone cannot guarantee ethical AI. Nature Machine Intelligence, 1, 501-507. https://doi.org/10.1038/s42256-019-0114-4

Mökander, J., Schuett, J., Kirk, H. R., & Floridi, L. (2023). Auditing large language models: A three-layered approach. AI and Ethics, 4, 1085-1115. https://doi.org/10.1007/s43681-023-00289-2

National Institute of Standards and Technology. (2023). Artificial intelligence risk management framework (AI RMF 1.0) (NIST AI 100-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.100-1

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., . . . Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. BMJ, 372, Article n71. https://doi.org/10.1136/bmj.n71

Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., Smith-Loud, J., Theron, D., & Barnes, P. (2020). Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing. In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (pp. 33-44). Association for Computing Machinery. https://doi.org/10.1145/3351095.3372873

Rapp, A., Curti, L., & Boldi, A. (2021). The human side of human-chatbot interaction: A systematic literature review of ten years of research on text-based chatbots. International Journal of Human-Computer Studies, 151, Article 102630. https://doi.org/10.1016/j.ijhcs.2021.102630

Shneiderman, B. (2020). Human-centered artificial intelligence: Reliable, safe & trustworthy. International Journal of Human-Computer Interaction, 36(6), 495-504. https://doi.org/10.1080/10447318.2020.1741118

Weidinger, L., Mellor, J., Rauh, M., Griffin, C., Uesato, J., Huang, P. S., Cheng, M., Glaese, A., Balle, B., Kasirzadeh, A., Biles, C., Brown, S., Kenton, Z., Hawkins, W., Stepleton, T., Birhane, A., Haas, J., Rimell, L., Hendricks, L. A., . . . Gabriel, I. (2022). Taxonomy of risks posed by language models. In Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (pp. 214-229). Association for Computing Machinery. https://doi.org/10.1145/3531146.3533088

Wiens, J., Saria, S., Sendak, M., Ghassemi, M., Liu, V. X., Doshi-Velez, F., Jung, K., Heller, K., Kale, D., Saeed, M., Ossorio, P. N., Thadaney-Israni, S., & Goldenberg, A. (2019). Do no harm: A roadmap for responsible machine learning for health care. Nature Medicine, 25, 1337-1340. https://doi.org/10.1038/s41591-019-0548-6

Wieringa, M. (2020). What to account for when accounting for algorithms: A systematic literature review on algorithmic accountability. In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (pp. 1-18). Association for Computing Machinery. https://doi.org/10.1145/3351095.3372833

Wohlin, C. (2014). Guidelines for snowballing in systematic literature studies and a replication in software engineering. In Proceedings of the 18th International Conference on Evaluation and Assessment in Software Engineering (Article 38). Association for Computing Machinery. https://doi.org/10.1145/2601248.2601268

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

