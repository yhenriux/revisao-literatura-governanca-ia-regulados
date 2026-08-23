# Exportação textual — Artigo_original_v0

Origem: `C:/Users/yhenr/OneDrive/Documentos/ChatGPT/Revisão de Literatura • Governança Conversacional em Sistemas Baseados em Modelos de Linguagem de Grande Escala em Ambientes  Regulados_ uma revisão sistemática da literatura/Artigo/Artigo_original_v0.docx`

Governança Conversacional em Sistemas Baseados em Modelos de Linguagem de Grande Escala em Ambientes Regulados: uma revisão sistemática da literatura

Conversational Governance in Large Language Model-Based Systems in Regulated Environments: A Systematic Literature Review

Resumo

Sistemas baseados em Modelos de Linguagem de Grande Escala vêm ampliando o uso de interfaces conversacionais em domínios críticos, como saúde, finanças, governo, jurídico, seguros, educação regulada e telecomunicações. Embora esses sistemas ofereçam novas possibilidades de automação, atendimento, recuperação de conhecimento e suporte à decisão, também introduzem riscos associados à alucinação, opacidade, vieses, rastreabilidade limitada, supervisão humana insuficiente, explicabilidade, conformidade regulatória e responsabilização. Este artigo apresenta uma Revisão Sistemática da Literatura sobre governança conversacional em sistemas baseados em LLMs aplicados a ambientes regulados. A revisão foi orientada pelo PRISMA 2020 e combinou busca sistemática, consolidação de corpus, deduplicação, recuperação de texto completo, triagem determinística, adjudicação assistida por LLM, avaliação de qualidade, validação de evidências e síntese temática. A revisão avaliou 407 estudos únicos em texto completo. Após a aplicação dos critérios de elegibilidade e a adjudicação das evidências, 177 estudos compuseram o corpus analítico, 112 referências foram mantidas como fundacionais ou contextuais e 118 estudos foram excluídos. Os resultados mostram predominância de compliance e gestão de risco, identificados em 88,7% do corpus, de controles técnicos e avaliação, em 61,0%, e de accountability e auditoria, em 54,2%. Contestabilidade e reparo apareceram em apenas 2,8% dos estudos, enquanto saúde e medicina concentraram 44,1% do corpus analítico. A principal contribuição do artigo é propor um Modelo Conceitual Integrado de Governança Conversacional, organizado em cinco camadas interdependentes: técnica, interacional, organizacional, regulatória e evolutiva. O modelo indica que a governança de sistemas conversacionais baseados em LLMs não pode ser reduzida ao controle do modelo, devendo abranger também a resposta, a interação, a fonte de conhecimento, o escalonamento, os registros de auditoria, a contestação, o reparo e a aprendizagem operacional.

Palavras-chave: governança conversacional; modelos de linguagem de grande escala; LLMs; IA generativa; ambientes regulados; accountability; auditoria algorítmica; supervisão humana; RAG; guardrails.

Abstract

Large Language Model-based systems have expanded the use of conversational interfaces in critical domains such as healthcare, finance, government, law, insurance, regulated education, and telecommunications. Although these systems create new opportunities for automation, service delivery, knowledge retrieval, and decision support, they also introduce risks related to hallucination, opacity, bias, limited traceability, insufficient human oversight, explainability, regulatory compliance, and accountability. This article presents a Systematic Literature Review on conversational governance in LLM-based systems deployed in regulated environments. The review was guided by PRISMA 2020 and combined systematic search, corpus consolidation, deduplication, full-text retrieval, deterministic screening, LLM-assisted adjudication, quality appraisal, evidence validation, and thematic synthesis. The review assessed 407 unique full-text studies. Following the application of the eligibility criteria and evidence adjudication, 177 studies formed the analytical corpus, 112 references were retained as foundational or contextual sources, and 118 studies were excluded. The results show a predominance of compliance and risk management, identified in 88.7% of the corpus, technical controls and evaluation, in 61.0%, and accountability and auditing, in 54.2%. Contestability and repair appeared in only 2.8% of the studies, while healthcare and medicine accounted for 44.1% of the analytical corpus. The main contribution of the article is the proposal of an Integrated Conceptual Model of Conversational Governance, organized into five interdependent layers: technical, interactional, organizational, regulatory, and evolutionary. The model suggests that governance of LLM-based conversational systems cannot be reduced to model control alone; it must also encompass the response, interaction, knowledge source, escalation, audit records, contestability, repair, and operational learning.

Keywords: conversational governance; large language models; LLMs; generative AI; regulated environments; accountability; algorithmic auditing; human oversight; retrieval-augmented generation; guardrails.

## 1. Introdução

Modelos de Linguagem de Grande Escala passaram a ocupar um papel central na mediação de interações digitais, especialmente em assistentes virtuais, chatbots, agentes conversacionais, sistemas de atendimento, mecanismos de busca aumentada por geração e interfaces de suporte à decisão. Diferentemente de sistemas conversacionais baseados apenas em regras ou classificação de intenção, sistemas baseados em LLMs operam com geração aberta de linguagem natural, uso dinâmico de contexto, possibilidade de integração com ferramentas externas e capacidade de produzir respostas fluentes, adaptativas e persuasivas. Essas características ampliam o potencial de uso, mas também introduzem novos desafios de governança.

A literatura sobre modelos fundacionais tem destacado riscos associados à escala, opacidade, viés, alucinação, uso indevido, instabilidade comportamental e dificuldade de avaliação sistemática (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022). No caso de sistemas conversacionais, esses riscos são intensificados pela forma de interação. A resposta do sistema não aparece como uma saída técnica isolada, mas como parte de uma conversa com usuários que podem atribuir ao agente competência, intenção, autoridade ou confiabilidade maior do que a efetivamente sustentada pelo sistema (Luger & Sellen, 2016; Rapp et al., 2021).

Em ambientes regulados, esses desafios tornam-se mais críticos. Saúde, finanças, governo, jurídico, seguros, educação regulada e telecomunicações envolvem requisitos de conformidade, privacidade, segurança, auditabilidade, explicabilidade, dever de cuidado e proteção de direitos. Uma resposta conversacional inadequada nesses domínios pode produzir consequências práticas: orientação clínica indevida, aconselhamento financeiro inadequado, falha de acesso a serviço público, interpretação jurídica equivocada, discriminação, violação de dados ou impossibilidade de contestação. Por isso, a governança de sistemas baseados em LLMs não pode ser reduzida à avaliação de desempenho do modelo.

A literatura de governança de IA e Responsible AI consolidou princípios como justiça, transparência, explicabilidade, privacidade, segurança, robustez e accountability (Floridi et al., 2018; Jobin et al., 2019). Entretanto, estudos críticos indicam que princípios gerais não garantem, por si só, implementação responsável, pois sua efetividade depende de mecanismos institucionais, processos organizacionais, práticas de auditoria e responsabilidades claramente atribuídas (Mittelstadt, 2019). Essa lacuna entre princípio e operacionalização é particularmente relevante para sistemas conversacionais baseados em LLMs, nos quais a governança precisa alcançar não apenas o modelo, mas também a interação, a base de conhecimento, os prompts, os guardrails, os logs, os fluxos de escalonamento e os processos de reparo.

A accountability algorítmica oferece uma base conceitual importante para essa discussão. Accountability envolve a obrigação de explicar e justificar condutas diante de uma instância avaliadora, com possibilidade de julgamento e consequências (Bovens, 2007). Em sistemas de IA, essa relação torna-se distribuída entre atores humanos, componentes técnicos, fornecedores, organizações e instituições reguladoras (Wieringa, 2020). Em sistemas conversacionais baseados em LLMs, a responsabilização precisa considerar a cadeia completa de produção da resposta: modelo fundacional, instruções de sistema, prompt do usuário, documentos recuperados, ferramentas acionadas, políticas de segurança, intervenção humana e contexto organizacional.

A literatura de interação humano-IA acrescenta que sistemas inteligentes precisam comunicar capacidades, limites, incertezas e possibilidades de correção de forma compreensível (Amershi et al., 2019; Shneiderman, 2020). Em interfaces conversacionais, essa exigência adquire uma dimensão específica: parte da governança ocorre no próprio diálogo. O sistema pode governar riscos ao recusar uma solicitação, indicar fonte, solicitar confirmação, reconhecer incerteza, escalar para atendimento humano ou permitir contestação. Assim, a governança conversacional envolve simultaneamente infraestrutura técnica, desenho de interação, política organizacional, conformidade regulatória e aprendizagem operacional.

Apesar da relevância crescente do tema, a literatura permanece fragmentada. Estudos sobre governança de IA discutem princípios e frameworks de risco; estudos sobre accountability algorítmica tratam responsabilização, auditoria e explicabilidade; estudos sobre LLMs abordam riscos de modelos fundacionais, alucinação e avaliação; estudos de interação humano-IA investigam confiança, transparência e experiência; e estudos sobre ambientes regulados enfatizam conformidade, segurança e impacto institucional. Ainda há necessidade de uma síntese específica sobre como esses elementos se combinam em mecanismos de governança conversacional para sistemas baseados em LLMs.

Este estudo apresenta uma Revisão Sistemática da Literatura sobre governança conversacional em sistemas baseados em LLMs aplicados a ambientes regulados. O objetivo é identificar, organizar e sintetizar mecanismos técnicos, interacionais, organizacionais, regulatórios e evolutivos que orientam, controlam, monitoram, justificam e corrigem o comportamento desses sistemas em interações mediadas por linguagem natural.

A revisão é guiada pelas seguintes questões de pesquisa: quais mecanismos de governança são relatados para sistemas conversacionais baseados em LLMs em ambientes regulados; como esses mecanismos endereçam risco, accountability, supervisão humana, auditoria, explicabilidade e conformidade; quais capacidades técnicas, interacionais, organizacionais e regulatórias aparecem associadas à governança conversacional; quais lacunas metodológicas, setoriais e operacionais persistem na literatura; e como a literatura articula explicabilidade, contestabilidade, reparo e aprendizagem operacional em sistemas baseados em LLMs.

A contribuição do artigo é tripla. Primeiro, a revisão consolida uma literatura dispersa sobre governança de IA, LLMs, sistemas conversacionais, accountability, auditoria, interação humano-IA e ambientes regulados. Segundo, organiza os mecanismos identificados em famílias analíticas: mecanismos técnicos e operacionais; supervisão humana, escalonamento e contestabilidade; accountability, auditoria e compliance; e aplicações em domínios regulados. Terceiro, propõe um Modelo Conceitual Integrado de Governança Conversacional, composto por cinco camadas: técnica, interacional, organizacional, regulatória e evolutiva.

O restante do artigo está organizado da seguinte forma. A Seção 2 apresenta os trabalhos relacionados e delimita a lacuna da revisão. A Seção 3 descreve o método, incluindo construção do corpus, critérios de elegibilidade, recuperação de texto completo, adjudicação assistida, avaliação de qualidade, validação de evidências e estratégia de síntese. A Seção 4 sintetiza os mecanismos de governança conversacional identificados na literatura. A Seção 5 apresenta os principais achados e oportunidades de pesquisa. A Seção 6 propõe o Modelo Conceitual Integrado de Governança Conversacional. Por fim, a Seção 7 apresenta as conclusões, limitações e direções para pesquisas futuras.

## 2. Trabalhos relacionados

A literatura sobre governança conversacional em sistemas baseados em LLMs se distribui em campos parcialmente sobrepostos: governança de IA, Responsible AI, accountability algorítmica, explicabilidade, interação humano-IA, operação de modelos generativos, avaliação de LLMs e implantação de IA em ambientes regulados. Esta seção organiza esses campos para explicitar a lacuna que motiva a revisão: a ausência de uma síntese específica sobre mecanismos de governança conversacional aplicáveis a sistemas baseados em LLMs em contextos regulados.

## 2.1. Governança de IA e Responsible AI

A literatura de governança de IA consolidou princípios como justiça, transparência, explicabilidade, privacidade, segurança, robustez e accountability. Revisões comparativas de diretrizes éticas mostram convergência em torno desses valores, mas também apontam variações significativas na forma como são operacionalizados em práticas, processos e instituições (Jobin et al., 2019). Essa tensão entre princípios gerais e mecanismos concretos é recorrente na literatura de Responsible AI, especialmente quando sistemas de IA são inseridos em organizações complexas e ambientes de risco elevado.

Floridi et al. (2018) propuseram um enquadramento ético para IA baseado em princípios como beneficência, não maleficência, autonomia, justiça e explicabilidade. Mittelstadt (2019), por sua vez, argumentou que princípios éticos isolados tendem a ser insuficientes para garantir conduta responsável, pois sua efetividade depende de arranjos institucionais, mecanismos de responsabilização e formas concretas de implementação. Essa discussão é relevante para sistemas conversacionais baseados em LLMs, nos quais a governança precisa lidar simultaneamente com comportamento probabilístico, interação com usuários, dependência de dados e decisões organizacionais.

A emergência de frameworks institucionais amplia essa discussão. O NIST AI Risk Management Framework, por exemplo, organiza a gestão de risco em funções como governar, mapear, medir e gerenciar, oferecendo uma estrutura operacional para a gestão de riscos de IA ao longo do ciclo de vida (National Institute of Standards and Technology, 2023). Em paralelo, instrumentos normativos como o AI Act europeu reforçam a centralidade de uma abordagem baseada em risco para sistemas de IA, especialmente em contextos de alto impacto social, econômico ou jurídico (European Parliament & Council of the European Union, 2024). Esses referenciais fornecem uma base importante, mas ainda tratam sistemas conversacionais e LLMs em um nível amplo, sem detalhar suficientemente os mecanismos interacionais de governança.

## 2.2. Accountability algorítmica, auditoria e explicabilidade

A noção de accountability oferece uma base conceitual central para compreender como decisões automatizadas podem ser justificadas, contestadas e atribuídas a atores responsáveis. Bovens (2007) define accountability como uma relação na qual um ator deve explicar e justificar sua conduta diante de uma instância avaliadora, que pode formular julgamento e impor consequências. Essa formulação é particularmente útil para sistemas de IA porque desloca a análise de atributos puramente técnicos para relações sociotécnicas entre sistemas, organizações, usuários, reguladores e públicos afetados.

No campo da accountability algorítmica, Wieringa (2020) mostra que a literatura trata diferentes objetos de responsabilização, como dados, modelos, decisões, efeitos e instituições. Raji et al. (2020) avançam essa discussão ao propor práticas de auditoria interna para sistemas de IA, destacando a necessidade de documentação, avaliação, rastreabilidade e mecanismos de revisão. Em sistemas baseados em LLMs, esses elementos ganham relevância porque a resposta final apresentada ao usuário pode depender de múltiplos componentes: modelo fundacional, prompt, contexto recuperado, base de conhecimento, guardrails, memória, ferramentas externas e regras de orquestração.

A explicabilidade também é recorrente nesse debate. Estudos em explicabilidade e interação humano-IA indicam que a utilidade de uma explicação depende do contexto de uso, da tarefa, da capacidade do usuário de interpretar a informação e dos efeitos práticos da explicação sobre decisão, confiança e contestação (Amershi et al., 2019; Shneiderman, 2020). Em sistemas conversacionais, a explicação opera em paralelo com diálogo, reparo, escalonamento e encaminhamento para supervisão humana. Assim, a explicabilidade deixa de ser apenas uma propriedade informacional do modelo e passa a compor a arquitetura da interação.

## 2.3. Governança de LLMs, modelos fundacionais e IA generativa

A literatura sobre modelos fundacionais e Modelos de Linguagem de Grande Escala destaca que esses sistemas diferem de modelos tradicionais de aprendizado de máquina por sua escala, generalidade e capacidade de adaptação a múltiplas aplicações downstream. Em vez de serem desenvolvidos exclusivamente para uma tarefa delimitada, modelos fundacionais podem sustentar diferentes sistemas, produtos e contextos de uso, fazendo com que riscos presentes no modelo de base sejam propagados ou transformados ao longo de sua cadeia de aplicação (Bommasani et al., 2021). Essa característica amplia a necessidade de governança para além do treinamento do modelo, abrangendo também adaptação, integração, implantação e uso organizacional.

Entre os principais riscos associados a esses sistemas, a literatura identifica opacidade, vieses, produção de conteúdo nocivo, concentração de poder, uso indevido e geração de respostas linguisticamente plausíveis sem garantia de correção factual (Bender et al., 2021; Weidinger et al., 2022). O problema da alucinação é particularmente relevante porque LLMs podem produzir informações inconsistentes, não verificáveis ou incompatíveis com as evidências disponíveis, mantendo elevado grau de fluência e coerência textual. Essa combinação pode dificultar a identificação do erro por usuários não especialistas e comprometer a confiabilidade de aplicações utilizadas em contextos sensíveis (Ji et al., 2023).

A recuperação aumentada por geração tem sido apresentada como uma resposta arquitetural parcial a esses problemas. Sistemas baseados em RAG conectam o modelo generativo a fontes externas de conhecimento, permitindo recuperar informações atualizadas ou específicas do domínio antes da geração da resposta. Essa arquitetura pode melhorar a ancoragem da resposta em fontes externas, a factualidade e a rastreabilidade das saídas, mas não elimina os riscos de governança. Seu desempenho depende da qualidade das fontes, da estratégia de recuperação, do ranqueamento, da atualização dos documentos e da maneira como o conteúdo recuperado é incorporado à geração (Gao et al., 2023). Dessa forma, RAG desloca parte do problema da governança do modelo para a governança da informação e da infraestrutura de recuperação.

A avaliação de LLMs também apresenta desafios distintos daqueles encontrados em sistemas determinísticos. Além de métricas de desempenho, torna-se necessário examinar segurança, robustez, privacidade, viés, transparência, utilidade, integração ao fluxo de trabalho e comportamento em situações de incerteza. Em revisão sistemática sobre avaliação de chatbots de saúde, Hua et al. (2025) identificaram que a rápida adoção de IA generativa supera a consolidação dos padrões avaliativos existentes. Como resposta, os autores propuseram um framework hierárquico que integra dimensões de segurança, privacidade, equidade, confiabilidade, utilidade e efetividade operacional. Embora formulado para o domínio da saúde, o estudo demonstra que a avaliação de sistemas conversacionais baseados em IA generativa precisa combinar critérios técnicos, humanos e institucionais.

A auditoria constitui outra resposta relevante às características dos LLMs. Mökander et al. (2023) propõem uma abordagem em três camadas, composta por auditorias de governança dos provedores, auditorias do modelo antes de sua liberação e auditorias das aplicações construídas sobre o modelo. Essa estrutura reconhece que a avaliação isolada do modelo não é suficiente, pois riscos podem surgir ou se modificar durante a adaptação, a integração e o uso em aplicações específicas. A proposta também evidencia que a accountability de sistemas baseados em LLMs precisa alcançar diferentes atores e estágios do ciclo de vida, ainda que a auditoria, por si só, não resolva todos os desafios associados à governança desses sistemas.

Esses trabalhos fornecem bases importantes para compreender riscos, ancoragem da resposta em fontes externas, avaliação e auditoria de LLMs. Entretanto, permanecem parcialmente fragmentados. A literatura sobre riscos concentra-se predominantemente nas propriedades e impactos dos modelos; os estudos sobre RAG enfatizam arquiteturas de recuperação e geração; e os frameworks de avaliação e auditoria tratam controles técnicos ou institucionais específicos. Ainda é limitada a integração desses elementos com mecanismos que operam no próprio diálogo, como comunicação de incerteza, confirmação, escalonamento, supervisão humana, contestação e reparo. Essa lacuna sustenta a necessidade de analisar a governança conversacional como uma configuração sociotécnica que articula modelo, aplicação, interação, organização e ambiente regulatório.

## 2.4. Sistemas conversacionais, chatbots e interação humano-IA

A literatura de sistemas conversacionais antecede a popularização dos LLMs e oferece contribuições importantes sobre experiência do usuário, expectativas, confiança, reparo conversacional, transparência e limites da automação. Luger e Sellen (2016) mostram que usuários tendem a projetar expectativas humanas sobre agentes conversacionais, o que pode gerar frustração quando as capacidades reais do sistema são limitadas. Følstad e Brandtzaeg (2020) indicam que a experiência com chatbots depende de fatores como utilidade percebida, qualidade da interação, confiança e capacidade de resolução.

Revisões sobre interação humano-chatbot também apontam que sistemas conversacionais precisam ser avaliados por dimensões que excedem acurácia ou intenção reconhecida, incluindo compreensão contextual, satisfação, reparo, continuidade, transparência e adequação ao domínio (Rapp et al., 2021). Com LLMs, essas dimensões se tornam mais complexas, pois o sistema pode produzir respostas fluidas, personalizadas e contextualmente plausíveis, mesmo quando há incerteza, erro factual ou lacuna de governança.

A literatura de interação humano-IA contribui com diretrizes para projetar sistemas que comuniquem capacidade, incerteza, estado, limitações e possibilidades de correção (Amershi et al., 2019). Para governança conversacional, essas diretrizes apontam a necessidade de mecanismos como confirmação, explicitação de limites, escalonamento, contestação, revisão humana e registro de eventos críticos. Dessa forma, a governança não se restringe ao backend técnico, pois envolve também a forma como o sistema se apresenta, negocia incertezas e permite intervenção humana.

## 2.5. IA em ambientes regulados

Ambientes regulados adicionam camadas específicas de exigência à governança de sistemas baseados em LLMs. Saúde, finanças, governo, jurídico, seguros, telecomunicações e educação regulada envolvem assimetrias de informação, deveres de cuidado, privacidade, rastreabilidade, normas setoriais e impactos potenciais sobre direitos dos usuários. Nesses contextos, a adoção de IA exige mecanismos que conectem desempenho técnico, conformidade, documentação, supervisão e accountability.

Na saúde, por exemplo, a literatura de machine learning clínico tem enfatizado que modelos precisam ser avaliados em termos de segurança, generalização, integração ao fluxo de trabalho, monitoramento e impacto real na prática clínica (Wiens et al., 2019). Em administração pública, a accountability algorítmica demanda que decisões automatizadas possam ser justificadas e contestadas em relação a valores públicos, legitimidade institucional e responsabilidade administrativa (Busuioc, 2021). Em finanças e serviços regulados, a governança de IA precisa lidar com explicabilidade, discriminação, compliance, auditoria e rastreabilidade de decisões automatizadas.

Esses debates indicam que a governança conversacional em LLMs precisa articular requisitos técnicos e institucionais. Um assistente baseado em LLM em ambiente regulado não apenas responde perguntas; ele participa de fluxos de atendimento, orientação, triagem, recomendação ou suporte à decisão. Isso envolve também design de canais de escalonamento, registro de interações, políticas de base de conhecimento, limites de automação, revisão humana e mecanismos de reparo.

## 2.6. Síntese da lacuna da revisão

Os trabalhos relacionados oferecem fundamentos robustos, mas permanecem distribuídos em campos que raramente se integram em uma estrutura única. A literatura de governança de IA oferece princípios e frameworks de risco. A accountability algorítmica aprofunda responsabilidade, auditoria e explicabilidade. A literatura de LLMs descreve riscos de modelos fundacionais, alucinação, viés e avaliação. Os estudos de interação humano-IA e chatbots tratam experiência, confiança, transparência e reparo. A literatura sobre ambientes regulados explicita requisitos setoriais de conformidade, documentação e supervisão.

A lacuna central desta revisão está na articulação dessas dimensões em torno da governança conversacional. Sistemas baseados em LLMs operam por meio de interação contínua, linguagem natural, contexto dinâmico, componentes técnicos distribuídos e relações organizacionais de responsabilidade. Por isso, sua governança tende a depender de capacidades combinadas: mecanismos técnicos de controle e observabilidade, mecanismos interacionais de supervisão e reparo, mecanismos organizacionais de accountability, mecanismos regulatórios de conformidade e mecanismos evolutivos de aprendizagem operacional.

Para delimitar a contribuição específica desta revisão, a Tabela 1 compara os principais campos que sustentam o objeto investigado, indicando a contribuição de cada tradição e o limite que permanece quando sistemas conversacionais baseados em LLMs são analisados em ambientes regulados.

Tabela 1. Campos relacionados, contribuições e limites para o objeto da revisão

Nota. Os campos são apresentados como tradições parcialmente sobrepostas, e não como categorias mutuamente exclusivas.

Fonte. Elaboração própria com base na literatura discutida na Seção 2.

A comparação evidencia que governança de IA, accountability algorítmica, explicabilidade, interação humano-IA e operação de LLMs fornecem fundamentos necessários, mas permanecem fragmentadas quando consideradas isoladamente. A governança conversacional constitui o ponto de integração entre essas tradições.

## 3. Método de pesquisa

Este estudo foi conduzido como uma Revisão Sistemática da Literatura, orientada pelas diretrizes PRISMA 2020, com o objetivo de identificar, organizar e sintetizar criticamente evidências sobre mecanismos de governança conversacional em sistemas baseados em Modelos de Linguagem de Grande Escala aplicados a ambientes regulados. O delineamento metodológico combinou procedimentos de busca sistemática, consolidação de corpus, deduplicação, triagem automatizada, recuperação de texto completo, avaliação assistida por LLM, validação determinística de evidências e síntese temática.

A adoção do PRISMA 2020 fornece uma estrutura para transparência na identificação, triagem, elegibilidade e inclusão de estudos em revisões sistemáticas (Page et al., 2021). Como o tema investigado se aproxima de sistemas computacionais, engenharia de software, governança de IA e operação de sistemas digitais, a revisão também incorporou recomendações metodológicas para revisões sistemáticas em engenharia de software, especialmente quanto à definição de protocolo, critérios de elegibilidade, extração de dados e rastreabilidade das decisões (Kitchenham & Charters, 2007). Procedimentos de snowballing foram empregados como estratégia complementar de expansão e verificação do corpus, em linha com recomendações específicas para estudos sistemáticos de literatura (Wohlin, 2014).

## 3.1. Desenho da revisão

A revisão foi delineada para mapear mecanismos de governança aplicáveis a sistemas conversacionais baseados em LLMs em contextos nos quais risco, rastreabilidade, accountability, conformidade regulatória e supervisão humana ganham relevância operacional. O escopo inclui sistemas de IA generativa, assistentes virtuais, chatbots, agentes conversacionais, arquiteturas baseadas em RAG, mecanismos de guardrails, observabilidade, auditoria, logs, tracing, monitoramento pós-implantação, governança do conhecimento, escalonamento, contestação, reparo e aprendizagem operacional.

O delineamento foi organizado em três camadas complementares. A primeira camada é sistemática e trata da identificação, consolidação, deduplicação e rastreabilidade do corpus. A segunda camada é avaliativa e abrange elegibilidade, qualidade metodológica, confiança nas evidências e aderência ao escopo. A terceira camada é sintética e organiza os achados por mecanismos de governança, domínios regulados e capacidades sociotécnicas.

Esse desenho permite articular a lógica de uma revisão sistemática com uma síntese temática orientada à construção de um modelo conceitual. A revisão, portanto, opera em paralelo como mapeamento do estado da arte, análise crítica de mecanismos e base para proposição conceitual.

## 3.2. Fontes de informação e estratégia de busca

A estratégia de busca foi estruturada para cobrir a natureza interdisciplinar da governança conversacional, situada na interseção entre ciência da computação, sistemas de informação, interação humano-computador, governança de inteligência artificial, gestão de risco e aplicações em ambientes regulados. A busca combinou um corpus-semente previamente reunido, consultas automatizadas em fontes bibliográficas públicas e expansão bibliográfica por snowballing. O processo foi conduzido de forma estruturada e rastreável, em consonância com as recomendações do PRISMA 2020 e com orientações para revisões sistemáticas em engenharia de software (Kitchenham & Charters, 2007; Page et al., 2021).

As consultas automatizadas foram executadas em oito fontes de informação: OpenAlex, Crossref, Semantic Scholar, PubMed, Europe PMC, CORE, arXiv e Directory of Open Access Journals. A seleção dessas fontes buscou combinar cobertura interdisciplinar, literatura biomédica, publicações em ciência da computação, preprints, metadados bibliográficos e documentos disponíveis em acesso aberto.

O OpenAlex foi utilizado como índice acadêmico multidisciplinar e como infraestrutura principal para expansão bibliográfica. O Crossref foi empregado para recuperação e normalização de metadados bibliográficos e identificadores DOI. O Semantic Scholar ampliou a cobertura de ciência da computação, inteligência artificial e áreas correlatas. PubMed e Europe PMC foram incluídos para recuperar estudos de saúde, medicina, bioética e sistemas clínicos. O CORE e o DOAJ contribuíram para a recuperação de publicações em acesso aberto. O arXiv foi utilizado para identificar preprints e produção técnica recente relacionada a LLMs, IA generativa, avaliação e segurança.

As fontes proprietárias inicialmente consideradas no planejamento, incluindo Scopus, Web of Science, ACM Digital Library, IEEE Xplore, ScienceDirect e SpringerLink, não foram incorporadas à execução automatizada nem ao corpus consolidado. Por essa razão, não são reportadas como fontes efetivamente consultadas nesta revisão.

## 3.2.1. Construção das estratégias de busca

As estratégias foram organizadas em cinco famílias conceituais derivadas das questões de pesquisa e da terminologia identificada no corpus-semente. A Tabela 2 apresenta a lógica de cada estratégia e as fontes em que foi aplicada. As strings canônicas e suas adaptações técnicas são documentadas integralmente no Apêndice A.

Tabela 2. Famílias conceituais e operacionalização da estratégia de busca

Nota. As consultas foram adaptadas às regras de sintaxe, indexação e processamento de cada fonte. As versões completas e executadas são apresentadas nas Tabelas A1 e A2.

Fonte. Elaboração própria com base nos registros de execução da busca.

A combinação das cinco famílias buscou reduzir a dependência de uma única terminologia. As estratégias cobriram tanto formulações amplas de governança de IA quanto mecanismos mais específicos, como observabilidade, supervisão humana, contestabilidade e operação de sistemas conversacionais.

As versões simplificadas empregadas no OpenAlex, Semantic Scholar e arXiv, bem como as consultas compactas utilizadas no DOAJ, são apresentadas no Apêndice A. Essa separação preserva, no corpo do artigo, as strings canônicas que orientaram conceitualmente a busca, mantendo as adaptações técnicas por fonte disponíveis para reprodução integral do procedimento.

## 3.2.2. Parâmetros de execução

As consultas foram executadas em julho de 2026. Para assegurar uma execução padronizada entre fontes com diferentes mecanismos de paginação, limites de acesso e políticas de requisição, foi definido um limite de até 25 resultados armazenados por combinação entre estratégia e fonte. Cada chamada registrou a fonte, o endpoint, a data, o identificador da estratégia, a consulta efetivamente enviada, a quantidade total de resultados informada pela fonte, a quantidade armazenada e o status da execução.

Esse limite torna o procedimento reproduzível, mas caracteriza a busca como uma busca sistemática delimitada, e não como recuperação exaustiva de todos os resultados disponíveis em cada fonte. Quando a fonte retornava mais de 25 resultados, foram preservados os registros apresentados segundo o mecanismo nativo de relevância da própria plataforma.

Não foram aplicados filtros temporais ou linguísticos diretamente nas consultas às APIs. O recorte principal de publicação, compreendido entre 2020 e 2026, foi aplicado nas etapas de triagem e elegibilidade. Estudos anteriores a 2020 foram preservados somente quando apresentavam função teórica, conceitual ou metodológica diretamente relevante para a revisão. Foram considerados estudos em inglês e português, sem exclusão automática por idioma na etapa de recuperação.

A cobertura do Semantic Scholar foi parcial em razão de limitações de taxa de requisição, mesmo após tentativas sucessivas com intervalos progressivos. A consulta ao arXiv também apresentou cobertura parcial devido a falhas de tempo de resposta. Essas ocorrências foram registradas nos logs de execução e consideradas entre as limitações da revisão.

## 3.2.3. Expansão por snowballing

A busca nas fontes bibliográficas foi complementada por snowballing, de acordo com os princípios apresentados por Wohlin (2014). O procedimento foi iniciado a partir dos estudos do corpus-semente que possuíam DOI válido e registro correspondente no OpenAlex.

Foram empregados cinco mecanismos de expansão:

Backward snowballing, mediante recuperação dos trabalhos referenciados pelos estudos-semente. Os identificadores das referências foram coletados no OpenAlex, e uma amostra de até 200 registros únicos foi resolvida para obtenção de metadados completos.

Forward snowballing, por meio da identificação de publicações que citavam os estudos-semente. As consultas foram realizadas em lotes de até 25 identificadores do OpenAlex, com recuperação de até 50 resultados por lote.

Trabalhos relacionados, utilizando o campo related_works do OpenAlex, limitado a até três registros relacionados por estudo-semente.

Expansão por autoria, por meio da recuperação de até cinco publicações recentes dos primeiros autores dos estudos-semente, limitada aos 15 primeiros autores identificados e às publicações a partir de 2024.

Expansão por veículo de publicação, considerando os oito periódicos ou veículos mais recorrentes entre os estudos-semente e recuperando até dez trabalhos publicados a partir de 2023, mediante a consulta large language model OR generative AI OR LLM OR chatbot OR governance.

Os registros provenientes do snowballing foram submetidos aos mesmos procedimentos de consolidação, deduplicação e elegibilidade aplicados aos registros recuperados pelas consultas principais. A origem de cada estudo foi preservada para permitir rastreabilidade entre busca direta, corpus-semente e expansão bibliográfica.

## 3.2.4. Consolidação e congelamento da busca

Os resultados das diferentes fontes foram integrados em uma base única. A deduplicação considerou DOI normalizado, correspondência exata de títulos e similaridade textual entre títulos. Grupos formados automaticamente foram submetidos a uma validação posterior, de modo que registros com títulos semelhantes, mas DOIs distintos, fossem preservados como estudos separados.

Após a consolidação, deduplicação, triagem e disponibilidade de texto completo, 407 estudos únicos constituíram o universo avaliado nesta revisão. A busca foi então congelada, impedindo a inclusão posterior de registros sem repetição formal do procedimento. Para cada estudo foram preservados metadados bibliográficos, origem, decisão de elegibilidade, justificativa, evidências textuais, classificação temática e informações necessárias à auditoria do processo.

## 3.3. Construção e consolidação do corpus

O corpus de elegibilidade foi composto por 407 estudos únicos com texto completo disponível, selecionados após procedimentos de busca, consolidação bibliográfica, deduplicação e triagem inicial. Esses estudos foram submetidos à extração textual, avaliação assistida, validação determinística das evidências e classificação quanto à aderência ao objeto da revisão.

Após a adjudicação, 177 estudos formaram o corpus analítico da revisão, dos quais 23 foram classificados como evidência central e 154 como evidência de apoio. Outras 112 referências foram mantidas como fundacionais ou contextuais, por contribuírem para a fundamentação teórica, normativa ou metodológica, sem serem tratadas como evidência equivalente aos estudos diretamente aderentes ao objeto. Foram excluídos 118 estudos por insuficiência de aderência aos critérios definidos.

Essa distinção permitiu separar os estudos utilizados diretamente na síntese dos mecanismos de governança conversacional das referências empregadas apenas para contextualização conceitual e metodológica. As análises temáticas, as frequências e a construção dos achados foram baseadas no corpus analítico de 177 estudos.

## 3.4. Questões de pesquisa

A revisão foi orientada pelas seguintes questões de pesquisa:

RQ1. Quais mecanismos de governança são relatados para sistemas conversacionais baseados em LLMs em ambientes regulados?

RQ2. Como esses mecanismos endereçam risco, accountability, supervisão humana, auditoria, explicabilidade e conformidade?

RQ3. Quais capacidades técnicas, interacionais, organizacionais e regulatórias aparecem associadas à governança conversacional?

RQ4. Quais lacunas metodológicas, setoriais e operacionais persistem na literatura?

RQ5. Como a literatura articula explicabilidade, contestabilidade, reparo e aprendizagem operacional em sistemas baseados em LLMs?

Essas questões foram formuladas para permitir uma síntese em múltiplas camadas. A camada técnica cobre mecanismos como RAG, logs, tracing, guardrails, observabilidade e avaliação contínua. A camada interacional contempla supervisão humana, contestação, reparo, escalonamento e handoff. A camada organizacional envolve accountability, papéis, políticas, governança do conhecimento e documentação. A camada regulatória inclui compliance, auditoria, risco, privacidade e evidência documental. A camada evolutiva abrange aprendizagem operacional, feedback loops, atualização de bases e melhoria contínua.

## 3.5. Critérios de elegibilidade

Os critérios de inclusão foram definidos para selecionar estudos com aderência substantiva à governança conversacional em sistemas baseados em LLMs ou a literaturas fundacionais diretamente relevantes para esse objeto. Foram considerados elegíveis estudos que abordassem uma ou mais das seguintes dimensões: governança de IA generativa, sistemas conversacionais, accountability, supervisão humana, auditoria, observabilidade, risco, conformidade, explicabilidade, contestabilidade, RAG, guardrails, operação de sistemas de IA ou implantação em ambientes regulados.

Referências anteriores à consolidação recente dos LLMs foram mantidas quando desempenhavam função fundacional, teórica ou metodológica para a revisão. Essa categoria inclui literatura sobre accountability algorítmica, governança de IA, Responsible AI, interação humano-computador, avaliação crítica de evidências, revisão sistemática e síntese temática. Esse critério permite incorporar bases conceituais necessárias para interpretar a governança conversacional como fenômeno sociotécnico.

Foram excluídos estudos sem relação substantiva com IA, governança, sistemas conversacionais, ambientes regulados ou mecanismos de accountability. Também foram excluídos documentos duplicados, registros sem metadados mínimos recuperáveis, textos sem acesso ao conteúdo necessário para avaliação e materiais internos do próprio projeto identificados como manuscritos prévios ou documentos de trabalho.

Os critérios foram operacionalizados por códigos explícitos para aumentar a consistência da triagem e permitir a rastreabilidade das decisões de elegibilidade.

Tabela 3. Critérios de inclusão e exclusão

Nota. O critério I7 permite a manutenção de referências anteriores a 2020 apenas quando apresentam função fundacional, teórica ou metodológica diretamente relacionada à revisão.

Fonte. Protocolo metodológico da revisão.

A aplicação dos critérios distinguiu estudos diretamente aderentes ao objeto, evidências de apoio, referências fundacionais ou contextuais e estudos excluídos. A disponibilidade de texto completo foi tratada como condição operacional de avaliação, e não como indicador de qualidade científica.

## 3.6. Recuperação de texto completo e extração automatizada

A recuperação de texto completo foi conduzida sobre os candidatos elegíveis com disponibilidade de PDF. Para cada arquivo, o pipeline realizou leitura do PDF, extração textual por página, geração de hash do arquivo, geração de hash do texto extraído, identificação de número de páginas, detecção de possível PDF escaneado, remoção da seção de referências e seleção de trechos relevantes para análise.

A remoção da seção de referências foi adotada como salvaguarda contra contaminação bibliográfica. Em artigos de revisão, relatórios técnicos e estudos conceituais, listas de referências podem conter autores, títulos e conceitos que pertencem a estudos citados, e não ao estudo avaliado. A separação entre corpo do texto e bibliografia reduz o risco de capturar uma referência citada como se fosse evidência substantiva do artigo.

A extração automatizada também produziu indicadores operacionais de qualidade do texto, como extensão do conteúdo extraído, presença de tabelas e figuras, status de extração e possíveis limitações associadas a PDFs escaneados ou parciais. Esses indicadores foram utilizados como apoio à auditoria e à priorização de revisão.

## 3.7. Triagem determinística em Python

Antes da avaliação assistida por LLM, cada estudo foi submetido a uma triagem determinística em Python. Essa etapa utilizou uma taxonomia controlada e bilíngue composta por termos fortes e fracos associados a oito dimensões: LLMs e IA generativa; IA conversacional e agentes; governança e accountability; ambientes regulados e de alto risco; supervisão humana, reparo e contestação; risco, auditoria e compliance; governança operacional e técnica; e valor fundacional.

A triagem determinística produziu um score preliminar de aderência ao escopo, termos encontrados, evidências literais, página de ocorrência e seção provável. Essa etapa operou como mecanismo de rastreabilidade e priorização. A pontuação automatizada foi interpretada como apoio à avaliação, preservando a necessidade de adjudicação posterior para decisões de elegibilidade e síntese.

## 3.8. Adjudicação assistida por LLM

A avaliação assistida por LLM foi conduzida sobre os 407 estudos únicos do corpus de elegibilidade. O pipeline utilizou um modelo de linguagem, combinado com procedimentos determinísticos em Python, para apoiar tarefas de classificação bibliográfica, elegibilidade, avaliação metodológica, extração temática, síntese das contribuições e decisão assistida.

Cada avaliação recebeu como entrada os metadados extraídos por Python, o resultado da triagem determinística, trechos iniciais do artigo, evidências lexicais selecionadas, trechos intermediários e trechos finais anteriores às referências. O modelo foi instruído a responder em JSON estruturado, usar apenas o texto fornecido, evitar inferências sem base textual e registrar “unclear” quando a informação estivesse ausente.

O uso de LLM foi tratado como adjudicação assistida e auditável. A decisão final do corpus foi estabelecida por meio da reconciliação entre os resultados automatizados, a validação das evidências, os critérios de elegibilidade e a consistência metodológica. Essa abordagem permite ganho de escala na leitura operacional dos estudos, preservando mecanismos de auditoria para reduzir risco de extrapolação indevida.

O procedimento não correspondeu a uma revisão humana independente em duplicata. A triagem e a avaliação foram conduzidas em um único fluxo assistido por LLM, combinado com procedimentos determinísticos em Python e validação textual das evidências. As decisões automatizadas foram tratadas como apoio à classificação e à síntese, mantendo-se rastreabilidade entre decisão, justificativa e evidência recuperada.

## 3.9. Avaliação de qualidade e confiança das evidências

A avaliação de qualidade metodológica foi operacionalizada por meio de um instrumento CASP/JBI adaptado ao tipo de estudo. O CASP oferece checklists para apoiar avaliação crítica de diferentes desenhos de pesquisa, enquanto o JBI Manual for Evidence Synthesis sistematiza procedimentos de síntese e avaliação de evidências em revisões (Aromataris et al., 2024; Critical Appraisal Skills Programme, n.d.). Os critérios avaliados incluíram clareza do objetivo, adequação metodológica, suficiência da amostra ou corpus, transparência da coleta de dados, rigor analítico, reflexividade ou aspectos éticos, clareza dos resultados, transparência das limitações, suporte das evidências e transferibilidade.

Além disso, foi incorporada uma camada CERQual para avaliar confiança em achados qualitativos. O CERQual considera limitações metodológicas, coerência, adequação dos dados e relevância para estimar confiança em achados de sínteses qualitativas (Lewin et al., 2018). Nesta revisão, essa camada foi utilizada como indicador de confiança analítica associado aos estudos e aos achados temáticos.

Como a avaliação de qualidade foi assistida por LLM e aplicada a estudos com desenhos heterogêneos, os scores foram utilizados como indicadores de priorização e cautela analítica, e não como critérios automáticos de inclusão ou exclusão. Estudos empíricos, conceituais, normativos, técnicos e de revisão foram interpretados de acordo com seus respectivos desenhos metodológicos, evitando comparações diretas entre estruturas de evidência distintas.

## 3.10. Validação determinística de evidências

Para reduzir risco de alucinação, paráfrase excessiva ou extrapolação indevida, o pipeline validou se os trechos de evidência citados pela LLM estavam presentes no texto extraído do PDF. Cada evidência foi checada por correspondência textual, com tolerância para cortes, reticências e variações decorrentes da extração automatizada.

A validação produziu contagens de evidências localizadas e não localizadas por estudo, além de indicadores de atenção. A ausência de correspondência literal não foi interpretada automaticamente como ausência de suporte, pois diferenças de extração, hifenização, segmentação ou normalização textual podem impedir a localização exata de um trecho.

Foram tratados como críticos os casos sem evidência válida ou com conflito entre a decisão assistida e o conjunto de evidências recuperadas. Esses casos foram considerados durante a adjudicação e a consolidação do corpus. A validação determinística funcionou, portanto, como uma camada de controle entre a avaliação assistida por LLM e a classificação final dos estudos.

## 3.11. Codificação temática e estratégia de síntese

A codificação temática foi orientada pelas questões de pesquisa e pelas camadas esperadas do modelo conceitual. Foram extraídos códigos abertos, códigos axiais, temas, subtemas, conceitos, camadas de modelo e alinhamento com as RQs. A síntese temática seguiu a lógica de identificação, organização e refinamento de padrões recorrentes no corpus, em consonância com abordagens consolidadas de análise temática (Braun & Clarke, 2006).

A síntese foi conduzida em dois movimentos. O primeiro organizou os estudos por famílias de mecanismos: mecanismos técnicos e operacionais; supervisão humana, escalonamento e contestabilidade; accountability, auditoria e compliance; e domínios regulados e aplicações. O segundo integrou os achados em um modelo conceitual de governança conversacional, articulando as camadas técnica, interacional, organizacional, regulatória e evolutiva.

Antes da quantificação dos resultados, os campos de codificação temática foram submetidos a uma normalização terminológica. A unidade de contagem foi o estudo, após a deduplicação e a consolidação das decisões de elegibilidade. Foram considerados exclusivamente os 177 estudos do corpus analítico, compostos por 23 evidências centrais e 154 evidências de apoio. As referências fundacionais ou contextuais e os estudos excluídos não foram incorporados às frequências.

A normalização utilizou um vocabulário controlado aplicado aos temas, subtemas, códigos abertos, códigos axiais, conceitos, camadas do modelo, sínteses das contribuições e setores de aplicação. Os campos de alinhamento às questões de pesquisa e de justificativa da decisão automatizada não foram utilizados nas contagens, de modo a reduzir circularidade entre o escopo fornecido ao modelo e os resultados da síntese. Casos sem correspondência direta ou com classificação setorial ambígua foram submetidos a adjudicação pontual.

As famílias de mecanismos, as camadas conceituais e os achados foram codificados de maneira multirrótulo, permitindo que um mesmo estudo contribuísse para mais de uma categoria. Consequentemente, os totais dessas dimensões não são mutuamente exclusivos e podem superar o número de estudos do corpus. Para a distribuição setorial, cada estudo recebeu um único domínio primário, definido a partir do título, do setor declarado e do objeto central da investigação.

## 3.12. Governança dos dados e consolidação do corpus

A base consolidada da revisão reuniu 407 estudos únicos avaliados em texto completo. Após a reconciliação das decisões assistidas, das evidências validadas e dos critérios de elegibilidade, 177 estudos foram incluídos no corpus analítico: 23 classificados como evidência central e 154 como evidência de apoio.

Outras 112 referências foram mantidas como fundacionais ou contextuais. Essas obras contribuíram para a fundamentação teórica, normativa ou metodológica, mas não foram incorporadas às frequências ou tratadas como evidência equivalente aos estudos do corpus analítico. Foram excluídos 118 estudos por ausência de aderência suficiente ao objeto, ausência de LLM ou IA generativa como foco, ausência de dimensão conversacional ou ausência de mecanismos substantivos de governança.

Os artefatos de revisão preservam, para cada estudo, metadados bibliográficos, decisão de elegibilidade, justificativa, evidências textuais, avaliação de qualidade, confiança analítica, códigos temáticos e uso previsto na síntese. Essa estrutura assegura rastreabilidade entre as fontes, os achados e o modelo conceitual proposto.

Gráfico 1. Composição dos 407 estudos avaliados em texto completo

Nota. As três categorias somam os 407 estudos únicos avaliados em texto completo.

Fonte. Elaboração própria com base na base consolidada da revisão.

O corpus analítico reuniu 177 estudos, equivalentes a 43,5% do universo avaliado. As referências fundacionais ou contextuais representaram 27,5%, enquanto 29,0% dos estudos foram excluídos. Essa separação impediu que literatura conceitual ou metodológica fosse contabilizada como evidência equivalente aos estudos diretamente aderentes ao objeto.

A Tabela 4 consolida as principais decisões metodológicas e sua operacionalização ao longo da revisão.

Tabela 4. Síntese do protocolo metodológico da revisão

Nota. A avaliação assistida não correspondeu a revisão humana independente em duplicata.

Fonte. Elaboração própria com base no protocolo e nos artefatos do pipeline.

A combinação entre triagem determinística, avaliação assistida, validação textual e auditoria buscou equilibrar escala, rastreabilidade e cautela analítica.

## 4. Mecanismos de Governança Conversacional em Sistemas Baseados em LLMs

A síntese temática foi conduzida sobre os 177 estudos do corpus analítico, composto por 23 evidências centrais e 154 evidências de apoio. As 112 referências fundacionais ou contextuais foram empregadas para fundamentação e interpretação, sem serem contabilizadas nas frequências dos mecanismos identificados.

As famílias de mecanismos e as camadas conceituais foram codificadas de maneira multirrótulo. Desse modo, um mesmo estudo pôde contribuir para diferentes categorias, e a soma das ocorrências pode superar o total de 177 estudos. As quantidades apresentadas representam incidência temática no corpus, não necessariamente implementação ou validação empírica dos mecanismos.

O Gráfico 2 compara a incidência das oito famílias normalizadas de mecanismos e a quantidade de evidências centrais em cada uma. A posição do marcador final representa o total de estudos, enquanto o marcador inicial indica o subconjunto classificado como evidência central.

Gráfico 2. Incidência das famílias de mecanismos e presença de evidência central

Nota. As famílias são multirrótulos. Um estudo pode contribuir para mais de uma categoria. A distância entre os marcadores corresponde às evidências de apoio.

Fonte. Elaboração própria com base nos 177 estudos do corpus analítico.

Compliance e gestão de risco apresentaram a maior cobertura, com 157 estudos e todas as 23 evidências centrais. Controles técnicos e avaliação apareceram em 108 estudos, enquanto accountability e auditoria foram identificadas em 96. Contestabilidade e reparo apresentaram incidência residual, com apenas cinco estudos e uma evidência central. A distribuição indica maior maturidade em prevenção, controle e conformidade do que em recurso, correção e reparação. Os valores completos são apresentados na Tabela B1, no Apêndice B.

A reorganização dos códigos pelas cinco camadas do modelo conceitual permite observar o grau de consolidação de cada dimensão. O Gráfico 3 compara evidências centrais e de apoio nas camadas técnica, interacional, organizacional, regulatória e evolutiva.

Gráfico 3. Distribuição dos estudos pelas camadas do modelo conceitual

Nota. As camadas são multirrótulo. Um mesmo estudo pode contribuir para diferentes dimensões do modelo.

Fonte. Elaboração própria com base nos 177 estudos do corpus analítico.

A camada técnica foi identificada em 147 estudos e a organizacional em 122, indicando predominância de controles instrumentais, políticas, documentação e atribuição de responsabilidades. A camada regulatória apareceu em 85 estudos. Em contraste, as camadas interacional e evolutiva foram identificadas em 49 e 36 estudos, respectivamente. Essa diferença mostra que a literatura está mais consolidada na governança do sistema e da organização do que na governança do diálogo e da aprendizagem pós-implantação. Os valores completos são apresentados na Tabela B2, no Apêndice B.

## 4.1. Mecanismos técnicos e operacionais de governança

A primeira família de mecanismos reúne componentes técnicos que permitem controlar, observar, restringir, avaliar ou corrigir o comportamento de sistemas baseados em LLMs. Esses mecanismos incluem RAG, guardrails, logs, tracing, observabilidade, red teaming, avaliação contínua, monitoramento pós-implantação, versionamento, documentação técnica e governança de bases de conhecimento.

No corpus analítico, controles técnicos e avaliação foram identificados em 108 estudos, dos quais 18 foram classificados como evidências centrais e 90 como evidências de apoio. Aprendizagem operacional e monitoramento apareceram em 81 estudos, enquanto mecanismos específicos de governança do conhecimento foram identificados em 44. Como as categorias são multirrótulo, esses grupos se sobrepõem em estudos que combinam avaliação, observabilidade, RAG, guardrails e monitoramento pós-implantação. Essa concentração também pode ser observada no Gráfico 2, especialmente na predominância de controles técnicos e avaliação e na presença mais limitada de governança do conhecimento.

A literatura sobre modelos fundacionais aponta que LLMs introduzem riscos específicos de opacidade, alucinação, viés, produção de conteúdo nocivo e dificuldade de avaliação em larga escala (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022). Em razão disso, a governança técnica passa a exigir mais que métricas tradicionais de desempenho. Ela precisa registrar o contexto de uso, rastrear entradas e saídas, monitorar falhas, controlar fontes de conhecimento e avaliar o comportamento do sistema em situações ordinárias e excepcionais.

A recuperação aumentada por geração, ou RAG, aparece como um mecanismo relevante porque conecta o modelo generativo a fontes externas de conhecimento. Esse arranjo pode reduzir a dependência exclusiva da memória paramétrica do modelo e permitir maior controle sobre atualidade, rastreabilidade e domínio das respostas (Gao et al., 2023). Contudo, RAG não resolve por si só o problema da governança. A qualidade das respostas passa a depender também da curadoria da base de conhecimento, da estratégia de recuperação, do ranqueamento dos documentos, da atualização das fontes e da forma como evidências são apresentadas ao usuário.

Guardrails também ocupam papel central na literatura recente. Eles podem operar como regras de bloqueio, filtros de segurança, classificadores de risco, limites de escopo, validações de formato, restrições de conteúdo ou políticas de resposta. Em sistemas conversacionais, esses mecanismos ajudam a reduzir respostas perigosas, juridicamente sensíveis, discriminatórias ou fora do domínio autorizado. Entretanto, guardrails podem falhar quando são tratados apenas como filtros técnicos, sem integração com processos de revisão humana, monitoramento de incidentes, auditoria e atualização contínua.

Logs, tracing e observabilidade ampliam a governança ao registrar o comportamento do sistema em produção. A observabilidade permite examinar prompts, respostas, fontes recuperadas, ferramentas chamadas, latência, erros, taxas de escalonamento, avaliações de segurança, feedback do usuário e eventos críticos. Em ambientes regulados, esses registros são relevantes para auditoria, investigação de incidentes, melhoria contínua e prestação de contas. A literatura de auditoria algorítmica reforça que mecanismos de documentação e rastreabilidade precisam cobrir o ciclo de vida do sistema, não apenas o momento de modelagem (Raji et al., 2020).

A avaliação contínua é outro mecanismo técnico-operacional. Ela inclui testes antes da implantação, red teaming, avaliação com datasets de referência, monitoramento pós-implantação e análise de regressão quando prompts, modelos, bases de conhecimento ou políticas são alterados. Em LLMs, a avaliação precisa contemplar factualidade, segurança, robustez, aderência ao domínio, consistência, privacidade, viés, toxicidade, capacidade de recusa, rastreabilidade de fontes e comportamento diante de incerteza. Essa lógica aproxima a governança técnica da gestão de risco, pois os testes deixam de ser apenas indicadores de qualidade e passam a funcionar como evidências de controle.

Em síntese, os mecanismos técnicos e operacionais oferecem a camada de controle instrumental da governança conversacional. Eles tornam possível observar, restringir e corrigir o comportamento do sistema. Ainda assim, sua efetividade depende da conexão com mecanismos humanos, organizacionais e regulatórios.

## 4.2. Supervisão humana, escalonamento e contestabilidade

A segunda família de mecanismos trata da relação entre automação e intervenção humana. Em sistemas baseados em LLMs, a supervisão humana pode aparecer em diferentes pontos do ciclo de vida: desenho do sistema, curadoria de conhecimento, validação de respostas, monitoramento de incidentes, revisão de casos sensíveis, escalonamento durante a interação e avaliação pós-uso.

Mecanismos de supervisão humana e escalonamento foram identificados em 76 estudos, incluindo 12 evidências centrais e 64 de apoio. Contestabilidade e reparo, entretanto, apareceram em apenas cinco estudos, dos quais um central e quatro de apoio. Essa diferença indica que a literatura aborda com maior frequência a presença de supervisão ou encaminhamento humano do que a existência de mecanismos formais para questionar, revisar ou reparar uma resposta produzida pelo sistema. O contraste entre supervisão humana e contestabilidade também reforça uma das assimetrias mais relevantes da revisão, já indicada no Gráfico 2: a literatura discute com frequência a presença de intervenção humana, mas ainda oferece cobertura limitada para mecanismos formais de recurso, revisão e reparação.

A literatura de interação humano-IA demonstra que a qualidade da automação depende da forma como o sistema comunica suas capacidades, limitações, incertezas e possibilidades de correção (Amershi et al., 2019). Em sistemas conversacionais, essa comunicação não ocorre apenas em painéis administrativos ou documentos técnicos. Ela ocorre também no próprio diálogo, quando o sistema reconhece limites, solicita confirmação, orienta o usuário, encaminha para atendimento humano ou explica por que não pode executar determinada ação.

A supervisão humana pode assumir formatos distintos. O modelo human-in-the-loop envolve intervenção humana direta em etapas críticas da operação. O modelo human-on-the-loop envolve monitoramento e capacidade de intervenção sem participação em todas as decisões. O modelo human-in-command enfatiza que atores humanos preservam autoridade sobre objetivos, políticas, limites de uso e consequências organizacionais. Em ambientes regulados, a escolha entre esses formatos deve considerar risco, reversibilidade da decisão, impacto sobre direitos, sensibilidade dos dados e grau de autonomia concedido ao sistema.

O escalonamento é um mecanismo interacional central. Ele define quando e como o sistema deve transferir a interação para uma pessoa, equipe, canal especializado ou processo de revisão. Em atendimento, saúde, finanças e setor público, escalonamento não é apenas uma conveniência de UX. Ele funciona como salvaguarda contra erro, incerteza, ambiguidade, sofrimento do usuário, risco jurídico, falha de compreensão ou necessidade de julgamento contextual. A literatura sobre chatbots mostra que a experiência do usuário é prejudicada quando agentes conversacionais excedem suas capacidades percebidas ou não oferecem caminhos claros de reparo (Følstad & Brandtzaeg, 2020; Luger & Sellen, 2016).

Contestabilidade e reparo ampliam a supervisão humana para além do momento da resposta. Contestabilidade refere-se à possibilidade de questionar, revisar ou disputar uma saída, recomendação ou decisão mediada por IA. Reparo refere-se aos mecanismos pelos quais erros são reconhecidos, corrigidos e incorporados a melhorias futuras. Em sistemas baseados em LLMs, esses mecanismos são especialmente importantes porque erros podem ser expressos em linguagem fluida e persuasiva, dificultando a percepção imediata de incerteza ou inconsistência.

A supervisão humana efetiva exige definição de papéis e critérios. Não basta afirmar que há “humano no loop” se não estiver claro quem intervém, em que momento, com qual autoridade, com quais evidências e sob quais responsabilidades. Esse ponto conecta supervisão humana à accountability organizacional. Uma intervenção humana meramente simbólica pode criar aparência de controle sem produzir responsabilização real.

## 4.3. Accountability, auditoria e compliance

A terceira família de mecanismos reúne práticas de responsabilização, documentação, auditoria, conformidade e governança institucional. Esses mecanismos respondem à pergunta sobre quem deve explicar, justificar, monitorar e corrigir o comportamento de sistemas conversacionais baseados em LLMs.

Accountability e auditoria foram identificadas em 96 estudos, dos quais 17 centrais e 79 de apoio. Compliance e gestão de risco apresentaram a maior incidência de todo o corpus, com 157 estudos, incluindo os 23 estudos classificados como evidência central. Essa concentração mostra que a literatura mais aderente ao objeto reconhece amplamente risco e conformidade, ainda que a operacionalização desses princípios varie entre documentação, auditoria, controles técnicos e estruturas organizacionais. Visualmente, essa concentração é expressa no Gráfico 2, no qual compliance e gestão de risco ocupam a posição mais recorrente de toda a taxonomia de mecanismos.

A accountability algorítmica desloca a discussão da performance técnica para relações de responsabilidade. Bovens (2007) define accountability como uma relação em que um ator deve explicar e justificar sua conduta diante de uma instância avaliadora. Em sistemas de IA, essa relação se torna distribuída, pois decisões e respostas podem envolver desenvolvedores, fornecedores de modelo, equipes de produto, curadores de conhecimento, gestores de risco, áreas jurídicas, operadores humanos e organizações usuárias. Wieringa (2020) mostra que a accountability algorítmica pode incidir sobre dados, modelos, decisões, efeitos e instituições, o que reforça sua natureza sociotécnica.

A auditoria é o mecanismo que operacionaliza parte dessa accountability. Ela pode ocorrer antes da implantação, durante o ciclo de desenvolvimento, em produção ou após incidentes. Auditorias de IA podem examinar dados, documentação, modelos, métricas, processos decisórios, riscos, impactos e mecanismos de mitigação (Raji et al., 2020). Para LLMs, a auditoria precisa incluir também prompts, políticas de sistema, bases recuperadas, ferramentas conectadas, guardrails, logs conversacionais, registros de escalonamento e respostas geradas em contextos sensíveis.

A conformidade regulatória adiciona critérios externos à governança. Em setores regulados, sistemas de IA precisam observar normas de proteção de dados, segurança, direitos do consumidor, regras setoriais, deveres profissionais e requisitos de documentação. O AI Risk Management Framework do NIST propõe funções de governança, mapeamento, medição e gestão de riscos, oferecendo uma estrutura operacional para organizar responsabilidades ao longo do ciclo de vida de sistemas de IA (National Institute of Standards and Technology, 2023). A abordagem baseada em risco também aparece no AI Act europeu, que diferencia obrigações conforme o potencial de dano e o contexto de aplicação (European Parliament & Council of the European Union, 2024).

Em sistemas conversacionais, compliance não pode ser tratado apenas como checagem documental. A conformidade precisa aparecer no comportamento do sistema, nas respostas dadas, nos limites de escopo, nas recusas, no registro das interações, na proteção de dados, na forma de recuperar conhecimento e nos mecanismos de contestação. Um assistente financeiro, clínico ou governamental pode estar formalmente documentado, mas ainda assim falhar se orientar usuários de modo inadequado, ocultar incerteza, não escalar casos críticos ou não preservar trilhas de auditoria.

A documentação também é parte da accountability. Model cards, system cards, relatórios de avaliação, registros de mudanças, matrizes de risco, políticas de uso e descrições de arquitetura permitem que atores internos e externos compreendam limites, pressupostos e responsabilidades do sistema. No caso de LLMs, a documentação precisa acompanhar não apenas o modelo, mas o sistema conversacional como um todo: orquestração, prompts, dados, ferramentas, canais, métricas, mecanismos de segurança e processos humanos associados.

## 4.4. Aplicações e domínios regulados

A quarta família de mecanismos observa como a governança conversacional se manifesta em domínios regulados. A literatura analisada concentra parte relevante das discussões em saúde, finanças, setor público, jurídico, educação, seguros, segurança da informação e serviços digitais. Esses domínios diferem entre si, mas compartilham características que aumentam a exigência de governança: assimetria de informação, impacto sobre direitos, sensibilidade de dados, necessidade de rastreabilidade e dependência de normas externas.

Na saúde, sistemas baseados em LLMs podem apoiar orientação ao paciente, triagem, educação em saúde, documentação clínica, suporte à decisão, pesquisa e acompanhamento. A literatura sobre IA responsável em saúde reforça que modelos precisam ser avaliados em termos de segurança, generalização, integração ao fluxo de trabalho, monitoramento e impacto real na prática (Wiens et al., 2019). Em sistemas conversacionais de saúde, essa exigência é ampliada pela relação direta com pacientes, que podem interpretar respostas como orientação médica, mesmo quando o sistema deveria atuar apenas como apoio informacional.

No setor financeiro, LLMs podem ser aplicados em atendimento, análise de documentos, orientação sobre produtos, suporte a compliance, detecção de risco, relatórios e automação de processos. Esses usos demandam explicabilidade, rastreabilidade, controle de privacidade, mitigação de viés e documentação de decisões. Uma resposta conversacional inadequada pode gerar risco de aconselhamento indevido, discriminação, violação regulatória ou dano econômico ao usuário.

No setor público, sistemas conversacionais podem mediar acesso a serviços, benefícios, informações legais, canais de reclamação e orientação administrativa. A governança nesse domínio envolve legitimidade, transparência, contestabilidade e preservação de direitos. Busuioc (2021) argumenta que a accountability da IA no setor público exige capacidade de responsabilizar algoritmos e organizações por decisões e efeitos. Em interfaces conversacionais, essa responsabilização precisa incluir não apenas decisões automatizadas formais, mas também respostas, encaminhamentos e omissões que afetam a experiência do cidadão.

Em educação, jurídico e seguros, os riscos variam conforme o tipo de interação. Sistemas educacionais podem afetar avaliação, orientação e aprendizagem. Sistemas jurídicos podem influenciar compreensão de direitos, estratégias processuais ou acesso à justiça. Sistemas de seguros podem impactar elegibilidade, indenização, precificação e comunicação de cobertura. Nesses contextos, a governança conversacional deve definir limites claros entre informação, recomendação, decisão e aconselhamento especializado.

A classificação por domínio primário revelou concentração expressiva na saúde e na medicina, que reuniram 78 estudos, equivalentes a 44,1% do corpus analítico. Outros 42 estudos, ou 23,7%, apresentaram natureza multissetorial ou transversal, enquanto 17, ou 9,6%, concentraram-se em tecnologia e operações empresariais.

Os demais ambientes regulados apresentaram cobertura consideravelmente menor. A educação reuniu 13 estudos, ou 7,3%; os serviços financeiros e de seguros, nove, ou 5,1%; o jurídico e o judiciário, sete, ou 4,0%; infraestrutura crítica, telecomunicações e cibersegurança, seis, ou 3,4%; e o setor público e governo, cinco, ou 2,8%.

A concentração é ainda mais acentuada entre as evidências centrais. Dos 23 estudos centrais, 12 pertencem à saúde e à medicina, cinco são multissetoriais, cinco tratam de tecnologia e operações empresariais e apenas um se concentra no setor público. Educação, finanças, seguros, jurídico, telecomunicações e infraestrutura crítica apresentam estudos de apoio, mas nenhum estudo classificado como evidência central.

A distribuição por domínio primário é apresentada no Gráfico 4. Como os domínios são mutuamente exclusivos, a área ocupada por cada categoria representa sua participação no corpus analítico.

Gráfico 4. Composição setorial do corpus analítico

Nota. A área de cada bloco é proporcional ao total de estudos. O número de evidências centrais é indicado em cada domínio.

Fonte. Elaboração própria com base nos 177 estudos do corpus analítico.

Saúde e medicina concentraram 78 estudos, equivalentes a 44,1% do corpus, incluindo 12 das 23 evidências centrais. Estudos multissetoriais representaram 23,7%, e tecnologia e operações empresariais, 9,6%. Educação, finanças, seguros, jurídico, infraestrutura crítica, telecomunicações e setor público apresentaram cobertura comparativamente menor. A concentração setorial limita a transferência direta dos achados e reforça a necessidade de validação do modelo em diferentes ambientes regulados. Os valores completos são apresentados na Tabela B3, no Apêndice B.

## 5. Achados da revisão e oportunidades de pesquisa

A síntese dos 177 estudos do corpus analítico resultou em cinco achados principais. O achado mais recorrente foi qualidade das evidências, avaliação e benchmarks, sustentado por 118 estudos, dos quais 18 centrais e 100 de apoio. Supervisão humana e accountability operacional foram identificadas em 111 estudos. Confiança, explicabilidade e governança orientada ao usuário apareceram em 101 estudos; observabilidade, auditoria e monitoramento pós-implantação, em 94; e governança do conhecimento, RAG e guardrails, em 58.

Como os achados foram codificados de maneira multirrótulo, essas quantidades representam incidência temática e não categorias mutuamente exclusivas. A identificação de determinado mecanismo também não significa necessariamente sua implementação ou validação empírica, pois parte da literatura o apresenta como princípio normativo, requisito arquitetural, recomendação ou agenda de pesquisa.

A seção organiza a interpretação desses resultados em cinco eixos: qualidade das evidências e avaliação; supervisão humana e accountability operacional; observabilidade, auditoria e monitoramento pós-implantação; governança do conhecimento, RAG e guardrails; e confiança, explicabilidade e governança orientada ao usuário.

Os cinco achados diferem tanto em cobertura temática quanto na quantidade de evidências centrais que os sustentam. O Gráfico 5 combina essas duas dimensões: a posição da bolha representa o total de estudos, e sua área indica o número de evidências centrais.

Gráfico 5. Cobertura temática e densidade de evidência central por achado

Nota. Os achados são multirrótulo. A posição horizontal representa o total de estudos e a área da bolha representa a quantidade de evidências centrais.

Fonte. Elaboração própria com base nos 177 estudos do corpus analítico.

Qualidade das evidências, avaliação e benchmarks constituíram o achado mais recorrente, com 118 estudos e 18 evidências centrais. Supervisão humana e accountability operacional apareceram em 111 estudos e apresentaram 19 evidências centrais, o maior valor desse estrato. Governança do conhecimento, RAG e guardrails apresentaram a menor cobertura entre os cinco eixos, com 58 estudos e nove evidências centrais.

## 5.1. Qualidade das evidências, avaliação e benchmarks

O primeiro achado foi sustentado por 118 estudos, correspondentes a 66,7% do corpus analítico, incluindo 18 evidências centrais e 100 de apoio. Trata-se do achado com maior cobertura quantitativa, refletindo a atenção dedicada a métricas, benchmarks, factualidade, alucinação, robustez, segurança e validação de sistemas baseados em LLMs. Apesar dessa frequência, a literatura permanece fragmentada na conversão dos riscos de modelos fundacionais em protocolos uniformes de avaliação e critérios de aceitação para sistemas conversacionais implantados em produção (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022). O Gráfico 5 mostra que esse é o achado com maior incidência temática no corpus, o que reforça a centralidade da avaliação e da qualidade das evidências na literatura analisada.

Em sistemas baseados em LLMs, métricas tradicionais de desempenho são insuficientes para avaliar governança. Acurácia, cobertura de intenção, taxa de resposta correta ou satisfação do usuário não capturam integralmente riscos como respostas não rastreáveis, uso de fontes inadequadas, ausência de escalonamento, opacidade decisória, violação de política institucional ou falha em comunicar incerteza. A avaliação precisa incorporar dimensões como factualidade, segurança, robustez, rastreabilidade, consistência, explicabilidade, privacidade, aderência ao domínio e capacidade de recusa.

A literatura sobre alucinação em geração de linguagem natural reforça que a fluidez textual dos modelos pode mascarar erros factuais ou inferências sem suporte documental (Ji et al., 2023). Em ambientes regulados, esse problema é agravado porque usuários podem interpretar respostas conversacionais como orientação autorizada, recomendação técnica ou decisão institucional. Por isso, uma agenda de pesquisa relevante consiste em desenvolver benchmarks específicos para governança conversacional, com cenários de risco, casos-limite, testes de escalonamento, avaliação de fontes, análise de contestabilidade e medição de comportamento sob incerteza.

Outro ponto crítico é a qualidade metodológica dos estudos. Parte da literatura é conceitual, normativa ou técnica, enquanto outra parte é empírica, experimental ou aplicada a domínios específicos. Essa heterogeneidade dificulta comparações diretas e exige instrumentos flexíveis de avaliação crítica. O uso combinado de appraisal metodológico, análise temática e avaliação de confiança das evidências permite diferenciar estudos com forte suporte empírico, contribuições conceituais fundacionais e propostas técnicas ainda pouco validadas.

## 5.2. Supervisão humana e accountability operacional

Supervisão humana e accountability operacional foram identificadas em 111 estudos, equivalentes a 62,7% do corpus, incluindo 19 evidências centrais e 92 de apoio. Entretanto, apenas 76 estudos apresentaram mecanismos explícitos de supervisão ou escalonamento. A diferença entre o achado amplo e os mecanismos operacionalizados indica que accountability, oversight e controle humano são frequentemente defendidos em nível normativo, sem detalhamento equivalente sobre quem intervém, quando intervém, com quais evidências, com qual autoridade e sob qual responsabilidade. A comparação entre o total do achado e a incidência mais restrita de mecanismos explicitamente operacionalizados sugere uma distância entre formulações normativas e desenho efetivo de dispositivos de supervisão.

Essa lacuna é especialmente importante em sistemas conversacionais. Em uma interface baseada em linguagem natural, a supervisão humana não ocorre apenas no treinamento ou na validação do modelo. Ela pode ocorrer durante o atendimento, em fluxos de escalonamento, na revisão de respostas sensíveis, na curadoria de bases de conhecimento, na análise de incidentes e na atualização de políticas. A governança conversacional exige, portanto, uma arquitetura de supervisão distribuída ao longo do ciclo de vida do sistema.

A literatura de interação humano-IA mostra que sistemas devem comunicar capacidades, limitações, incertezas e possibilidades de correção de forma clara ao usuário (Amershi et al., 2019). No caso de LLMs, essa exigência se torna mais forte porque o sistema pode parecer mais competente do que realmente é. A aparência de fluência, coerência e personalização pode aumentar a confiança do usuário mesmo quando a resposta contém erro, extrapolação ou ausência de base documental.

A accountability operacional depende da transformação da supervisão humana em processo institucional. Isso envolve definir papéis, critérios de escalonamento, níveis de risco, evidências exigidas para revisão, mecanismos de contestação, responsabilidades de equipes e consequências de falhas. Sem essa estrutura, a supervisão humana pode se tornar uma salvaguarda apenas declaratória, incapaz de produzir prestação de contas real.

A literatura de accountability algorítmica reforça que responsabilização exige relações identificáveis entre atores, decisões, justificativas, instâncias de avaliação e consequências (Bovens, 2007; Wieringa, 2020). Para LLMs conversacionais, essa relação deve incluir a cadeia completa de produção da resposta: modelo, prompt, contexto recuperado, ferramentas, guardrails, base de conhecimento, política organizacional e intervenção humana.

## 5.3. Observabilidade, auditoria e monitoramento pós-implantação

Observabilidade, auditoria e monitoramento pós-implantação foram identificados em 94 estudos, correspondentes a 53,1% do corpus analítico, dos quais 18 centrais e 76 de apoio. Os estudos abordam auditoria, logs, tracing, telemetria, documentação, monitoramento contínuo e investigação de incidentes ao longo do ciclo de vida dos sistemas baseados em LLMs.

Observabilidade não deve ser tratada apenas como capacidade técnica de monitoramento. Ela é uma condição para investigação, aprendizagem e responsabilização. Sem logs e tracing adequados, torna-se difícil reconstruir por que determinada resposta foi produzida, quais fontes foram usadas, quais regras foram aplicadas, se houve tentativa de escalonamento e quais componentes contribuíram para a falha.

O monitoramento pós-implantação também é essencial porque LLMs operam em ambientes dinâmicos. Mudanças em modelos, prompts, bases de conhecimento, políticas internas, requisitos regulatórios e padrões de uso podem alterar o comportamento do sistema. Assim, a governança precisa incluir avaliação contínua, testes de regressão, análise de incidentes, revisão de métricas e atualização controlada de componentes.

Embora o achado amplo tenha aparecido em 94 estudos, a camada evolutiva foi identificada em apenas 36. Essa diferença mostra que monitoramento e auditoria são frequentemente tratados como instrumentos de rastreabilidade ou conformidade, mas menos frequentemente conectados a processos sistemáticos de aprendizagem, atualização e adaptação após incidentes. O contraste entre a incidência do achado e a menor presença da camada evolutiva pode ser visualizado pela leitura combinada do Gráfico 5 com o Gráfico 3.

A literatura de gestão de risco em IA reforça a necessidade de governar, mapear, medir e gerenciar riscos durante o ciclo de vida do sistema (National Institute of Standards and Technology, 2023). Essa abordagem é compatível com a governança conversacional porque permite tratar cada interação como evento observável, avaliável e potencialmente auditável. Em ambientes regulados, essa capacidade é particularmente relevante para demonstrar conformidade, investigar danos e sustentar decisões organizacionais.

## 5.4. Governança do conhecimento, RAG e guardrails

Governança do conhecimento, RAG e guardrails constituíram o achado de menor cobertura entre os cinco eixos principais, sendo identificados em 58 estudos, equivalentes a 32,8% do corpus. Nove estudos foram classificados como evidências centrais e 49 como evidências de apoio. Quando considerada apenas a família específica de governança do conhecimento, foram identificados 44 estudos, indicando que nem todos os trabalhos sobre RAG ou guardrails abordam explicitamente curadoria, proveniência, validade, autoridade e versionamento das fontes. O posicionamento desse achado no Gráfico 5 mostra que, embora relevante, essa agenda ainda apresenta cobertura comparativamente menor que avaliação, supervisão e observabilidade.

Esse achado desloca parte da governança do modelo para a governança da informação. Em ambientes regulados, bases de conhecimento precisam ter autoria, versão, validade, data de atualização, escopo, fonte autorizada e critérios de uso. Uma resposta conversacional incorreta pode decorrer de falha do modelo, mas também de documento desatualizado, fonte inadequada, chunk mal segmentado, recuperação irrelevante ou ausência de regra de prioridade entre fontes.

Guardrails complementam essa governança ao impor limites de escopo, segurança e conformidade. Eles podem bloquear perguntas proibidas, impedir aconselhamento indevido, exigir escalonamento, forçar citação de fontes, recusar respostas inseguras ou validar formatos. Contudo, guardrails isolados não garantem governança. Eles precisam ser testados, versionados, monitorados e conectados a processos de revisão e accountability.

A oportunidade de pesquisa está em desenvolver modelos de governança que integrem RAG, curadoria de conhecimento, guardrails e supervisão humana. Essa integração deve contemplar tanto a qualidade da informação quanto a qualidade da interação. Em sistemas conversacionais, não basta recuperar a fonte correta; é necessário apresentar a resposta de modo adequado ao risco, ao perfil do usuário, ao grau de incerteza e às responsabilidades institucionais envolvidas.

## 5.5. Confiança, explicabilidade e governança orientada ao usuário

Confiança, explicabilidade e governança orientada ao usuário foram identificadas em 101 estudos, correspondentes a 57,1% do corpus analítico. Esse conjunto inclui 17 evidências centrais e 84 de apoio, demonstrando que transparência, confiança calibrada, comunicação de incerteza e experiência do usuário ocupam posição relevante na literatura.

Isso implica diferenciar explicabilidade interna, voltada a desenvolvedores e auditores, de explicabilidade orientada ao usuário, voltada a compreensão, contestação e reparo. A primeira pode envolver logs, métricas, traces, documentos técnicos e análise de componentes. A segunda precisa aparecer como resposta compreensível, indicação de fonte, aviso de incerteza, justificativa de recusa, explicitação de limite ou encaminhamento para suporte humano.

A confiança em sistemas conversacionais pode ser indevidamente ampliada pela naturalidade da linguagem. Usuários tendem a atribuir competência, intencionalidade ou compreensão a agentes conversacionais mesmo quando suas capacidades são limitadas (Luger & Sellen, 2016). Com LLMs, esse risco aumenta porque a interação se torna mais fluida, adaptativa e persuasiva. Portanto, a governança orientada ao usuário deve incluir mecanismos para calibrar confiança, evitar antropomorfização excessiva e comunicar limites de forma explícita.

A análise dos mecanismos específicos revela, entretanto, uma assimetria substantiva. Explicabilidade, confiança e comunicação de limites apareceram em 84 estudos, enquanto contestabilidade e reparo foram identificados em apenas cinco. A literatura oferece, portanto, cobertura muito maior para mecanismos que informam ou explicam o comportamento do sistema do que para mecanismos que permitem ao usuário agir sobre uma resposta inadequada, obter revisão ou buscar reparação. A leitura combinada do Gráfico 5 com o Gráfico 2 evidencia que mecanismos voltados à comunicação e à explicação aparecem com frequência considerável, enquanto contestabilidade e reparo permanecem residuais.

Contestabilidade e reparo são extensões práticas da explicabilidade. Uma explicação que não permite ação posterior pode ter valor limitado em ambientes regulados. A governança conversacional deve permitir que usuários questionem respostas, solicitem revisão, corrijam informações, acionem suporte humano e compreendam os caminhos disponíveis para contestação. Essa dimensão aproxima governança, UX conversacional e accountability.

## 5.6. Síntese dos achados

A síntese quantitativa e temática demonstra que a literatura se concentra em risco, compliance, avaliação e controles técnicos, enquanto dedica menor atenção às dimensões interacional e evolutiva da governança. A camada técnica apareceu em 83,1% dos estudos e a camada organizacional em 68,9%, em comparação com 27,7% para a camada interacional e 20,3% para a evolutiva. Essa assimetria é sintetizada pelos Gráficos 2 e 3, que mostram maior densidade nas dimensões técnicas, organizacionais e regulatórias e menor incidência nas dimensões interacional e evolutiva.

Os resultados também revelam concentração setorial na saúde e na medicina, responsáveis por 44,1% do corpus analítico e por 12 das 23 evidências centrais. Finanças, seguros, educação, jurídico, telecomunicações e infraestrutura crítica apresentam contribuições de apoio, mas não possuem estudos classificados como evidência central na taxonomia adotada. O Gráfico 4 complementa essa leitura ao evidenciar a concentração setorial na saúde e na medicina.

As capacidades identificadas não funcionam de forma isolada. RAG sem curadoria pode amplificar informação inadequada; guardrails sem monitoramento podem falhar silenciosamente; supervisão humana sem papéis definidos pode se tornar simbólica; logs sem processo de auditoria podem não gerar accountability; e explicabilidade sem contestação pode não produzir reparo. A contribuição analítica da revisão está, portanto, em demonstrar que a governança conversacional depende da integração de mecanismos técnicos, interacionais, organizacionais, regulatórios e evolutivos.

Em conjunto, os dados indicam que a literatura não apresenta apenas uma lacuna de integração. Há também lacunas de operacionalização, equilíbrio entre camadas e maturidade setorial. Risco, avaliação e conformidade possuem ampla cobertura, enquanto contestabilidade, reparo, aprendizagem operacional e manifestação da governança no próprio diálogo permanecem menos consolidados.

Para examinar como os mecanismos se distribuem entre as cinco camadas, foi calculada a coocorrência dos códigos no nível do estudo. O Gráfico 6 apresenta a quantidade de estudos simultaneamente associados a cada família de mecanismos e a cada camada conceitual.

Gráfico 6. Coocorrência entre famílias de mecanismos e camadas de governança

Nota. Cada célula representa o número de estudos simultaneamente codificados na família da linha e na camada da coluna. As categorias são multirrótulo.

Fonte. Elaboração própria com base nos códigos normalizados dos 177 estudos do corpus analítico.

As maiores coocorrências ocorreram entre compliance e gestão de risco e a camada técnica, com 131 estudos, e entre a mesma família e a camada organizacional, com 111. Controles técnicos e avaliação apresentaram 98 ocorrências na camada técnica. Accountability e auditoria apareceram em 82 estudos associados à camada técnica e em 77 ligados à camada organizacional. Contestabilidade e reparo permaneceram pouco representados em todas as camadas. A matriz reforça que o modelo precisa integrar dimensões amplamente consolidadas a capacidades ainda pouco desenvolvidas.

A combinação entre incidência temática, força das evidências e lacunas de coocorrência permite derivar implicações para pesquisa e desenvolvimento. A Tabela 5 sintetiza essas implicações e as oportunidades correspondentes.

Tabela 5. Implicações e oportunidades de pesquisa derivadas dos achados

Nota. As oportunidades foram derivadas da síntese quantitativa e temática e não representam apenas a frequência isolada dos códigos.

Fonte. Elaboração própria com base nos achados da revisão.

As oportunidades convergem para a necessidade de avaliações específicas para contextos regulados, supervisão proporcional ao risco, observabilidade de ponta a ponta, governança das fontes de conhecimento e mecanismos interacionais de contestação e reparo.

## 6. Modelo Conceitual Integrado de Governança Conversacional

Com base nos achados da revisão, esta seção propõe um Modelo Conceitual Integrado de Governança Conversacional para sistemas baseados em LLMs implantados em ambientes regulados. O modelo organiza a governança conversacional como uma configuração sociotécnica composta por cinco camadas interdependentes: técnica, interacional, organizacional, regulatória e evolutiva.

A proposição parte do reconhecimento de que sistemas baseados em LLMs não são governados apenas pelo modelo fundacional. Sua operação envolve prompts, bases de conhecimento, mecanismos de recuperação, ferramentas externas, guardrails, interfaces conversacionais, políticas organizacionais, supervisão humana, registros de auditoria e requisitos regulatórios. Por isso, a governança precisa abranger o sistema conversacional completo, e não apenas o componente algorítmico isolado.

## 6.1. Fundamentos do modelo

A literatura sobre modelos fundacionais aponta que LLMs ampliam a escala e a complexidade dos riscos associados a sistemas de IA, incluindo opacidade, alucinação, viés, uso indevido, dificuldade de avaliação e impactos sociais distribuídos (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022). Esses riscos tornam insuficiente uma abordagem de governança centrada apenas em acurácia ou desempenho técnico.

A literatura de accountability algorítmica, por sua vez, mostra que responsabilização exige relações claras entre atores, decisões, justificativas, mecanismos de avaliação e consequências (Bovens, 2007; Wieringa, 2020). Em sistemas conversacionais baseados em LLMs, essa relação se torna distribuída, pois uma resposta pode depender de múltiplos componentes técnicos e decisões organizacionais. A accountability precisa, portanto, abranger a cadeia completa de produção, validação, entrega e correção da resposta.

A literatura de interação humano-IA acrescenta que sistemas inteligentes devem comunicar capacidades, limitações, incertezas e caminhos de correção de forma compreensível para usuários (Amershi et al., 2019; Shneiderman, 2020). Esse ponto é central para a governança conversacional, pois parte da governança ocorre no próprio diálogo: quando o sistema informa limites, recusa uma solicitação, cita fontes, pede confirmação, escala para atendimento humano ou permite contestação.

Por fim, frameworks de gestão de risco em IA reforçam a necessidade de mapear, medir, governar e gerenciar riscos ao longo do ciclo de vida do sistema (National Institute of Standards and Technology, 2023). Em ambientes regulados, essa orientação precisa ser combinada a requisitos setoriais, documentação, auditoria, proteção de dados, supervisão humana e evidências de conformidade.

## 6.2. Camadas do modelo conceitual

O modelo propõe cinco camadas integradas.

A camada técnica reúne mecanismos de controle, observabilidade e segurança operacional. Inclui RAG, guardrails, logs, tracing, monitoramento, red teaming, avaliação contínua, versionamento e testes de regressão. Essa camada responde à necessidade de tornar o comportamento do sistema observável, avaliável e tecnicamente controlável.

A camada interacional trata da governança que ocorre na relação entre sistema e usuário. Inclui explicação, comunicação de limites, confirmação, handoff, escalonamento, contestação, reparo e orientação sobre próximos passos. Essa camada é necessária porque sistemas conversacionais governam parte da experiência por meio da própria linguagem.

A camada organizacional define papéis, responsabilidades, políticas, processos, documentação e estruturas internas de decisão. Inclui comitês, matriz de responsabilidade, governança do conhecimento, critérios de escalonamento, fluxos de revisão e processos de auditoria interna. Essa camada evita que a responsabilidade fique dispersa entre modelo, fornecedor, produto, operação e área de negócio.

A camada regulatória conecta o sistema a normas, riscos, evidências e deveres setoriais. Inclui compliance, proteção de dados, avaliação de impacto, trilhas de auditoria, critérios de risco, documentação regulatória e alinhamento com obrigações específicas de cada domínio. Essa camada é especialmente relevante em saúde, finanças, governo, jurídico, seguros, educação regulada e telecomunicações.

A camada evolutiva trata da aprendizagem operacional e da adaptação controlada do sistema. Inclui análise de incidentes, feedback loops, atualização de bases de conhecimento, revisão de prompts, ajustes de guardrails, melhoria contínua e monitoramento pós-implantação. Essa camada reconhece que a governança não termina na implantação; ela precisa acompanhar o comportamento real do sistema em uso.

## 6.3. Estrutura proposta do modelo

A integração dos resultados quantitativos e temáticos permitiu organizar os mecanismos em um modelo sistêmico. A Figura 1 representa as cinco camadas como dimensões interdependentes que atuam sobre o sistema conversacional completo, incluindo modelo, resposta, interação, conhecimento, organização e ambiente regulatório.

Figura 1. Modelo Conceitual Integrado de Governança Conversacional

Nota. As setas representam dependência recíproca e retroalimentação, e não uma sequência temporal rígida.

Fonte. Elaboração própria a partir da síntese da revisão.

A figura evidencia que nenhuma camada produz governança de forma autônoma. A camada regulatória define requisitos e limites; a organizacional os traduz em responsabilidades e processos; a técnica implementa controles e registros; a interacional manifesta a governança no diálogo; e a evolutiva transforma incidentes, uso e feedback em adaptação controlada.

## 6.4. Capacidades do modelo

O modelo não deve ser interpretado como uma sequência linear rígida. As camadas operam de forma interdependente. Um mecanismo técnico, como RAG, depende de governança organizacional da base de conhecimento e pode estar sujeito a requisitos regulatórios de rastreabilidade. Um mecanismo interacional, como handoff, depende de critérios técnicos de detecção de risco e de processos organizacionais de atendimento. Uma auditoria regulatória depende de logs técnicos, documentação organizacional e evidências de interação.

Essa interdependência indica que governança conversacional é uma capacidade sistêmica. Ela exige coordenação entre tecnologia, design conversacional, operação, risco, compliance, jurídico, segurança, dados e áreas de negócio.

## 6.5. Aplicação do modelo em ambientes regulados

Em ambientes regulados, o modelo deve ser aplicado de modo proporcional ao risco da interação. Interações informacionais simples podem demandar controles básicos, como logs, limites de escopo e atualização da base de conhecimento. Interações que envolvem orientação clínica, financeira, jurídica, administrativa ou de acesso a direitos exigem controles mais robustos, incluindo explicação, rastreabilidade de fontes, supervisão humana, contestabilidade, auditoria e documentação regulatória.

Na saúde, por exemplo, a camada interacional precisa diferenciar informação geral, triagem, orientação clínica e suporte à decisão. A camada técnica deve controlar fontes, mitigar alucinação e registrar evidências. A camada organizacional deve definir responsabilidade profissional e critérios de escalonamento. A camada regulatória deve garantir proteção de dados, segurança e documentação. A camada evolutiva deve monitorar incidentes e atualizar protocolos.

No setor financeiro, a governança precisa lidar com risco de aconselhamento indevido, discriminação, privacidade, explicabilidade e conformidade. Em governo, a ênfase recai sobre legitimidade, transparência, contestabilidade e acesso a direitos. Em jurídico e seguros, a distinção entre informação, recomendação e decisão torna-se especialmente sensível. Esses exemplos mostram que o modelo não substitui regras setoriais; ele organiza as capacidades necessárias para que essas regras sejam implementadas em sistemas conversacionais baseados em LLMs.

## 6.6. Contribuição conceitual do modelo

A principal contribuição do modelo é integrar dimensões que aparecem fragmentadas na literatura. A governança de IA oferece princípios e frameworks de risco. A accountability algorítmica oferece uma teoria de responsabilização. A literatura de LLMs descreve riscos técnicos e sociais. A interação humano-IA oferece diretrizes para transparência, confiança e correção. A literatura regulatória define obrigações setoriais e critérios de conformidade. O modelo proposto articula essas contribuições em torno da unidade de análise conversacional.

A governança conversacional é, portanto, definida neste estudo como o conjunto de mecanismos técnicos, interacionais, organizacionais, regulatórios e evolutivos que orientam, controlam, monitoram, justificam e corrigem o comportamento de sistemas baseados em LLMs em interações mediadas por linguagem natural, especialmente quando tais sistemas operam em ambientes regulados ou de alto impacto.

Essa definição amplia a noção de governança para além do controle do modelo. Ela inclui a governança da resposta, da interação, da fonte de conhecimento, do escalonamento, do reparo, da evidência, da responsabilidade e da aprendizagem operacional. Com isso, o modelo oferece uma base para análise de sistemas existentes, desenho de novos sistemas, auditoria de aplicações em produção e desenvolvimento de agendas de pesquisa empírica.

Para converter o modelo conceitual em instrumento de análise organizacional, a Tabela 6 apresenta perguntas verificáveis associadas às camadas e aos controles esperados.

Tabela 6. Perguntas operacionais e exemplos de evidência de controle

Nota. As perguntas e evidências são exemplificativas e devem ser calibradas conforme o risco, o setor e o grau de autonomia do sistema.

Fonte. Elaboração própria com base no Modelo Conceitual Integrado.

A tabela traduz as cinco camadas em critérios que podem orientar revisão de arquitetura, avaliação de risco, auditoria, desenho de interação e monitoramento pós-implantação. Sua aplicação não substitui requisitos regulatórios específicos, mas oferece uma estrutura comum para organizar evidências e responsabilidades.

## 7. Conclusão

Esta revisão sistemática avaliou 407 estudos únicos em texto completo e consolidou um corpus analítico de 177 estudos diretamente relacionados aos mecanismos de governança conversacional em sistemas baseados em Modelos de Linguagem de Grande Escala aplicados a ambientes regulados. O estudo partiu da constatação de que LLMs ampliam as possibilidades de interação em linguagem natural, mas também introduzem riscos relacionados à alucinação, opacidade, vieses, rastreabilidade, supervisão humana, explicabilidade, conformidade e responsabilização. Em setores como saúde, finanças, governo, jurídico, seguros, educação regulada e telecomunicações, esses riscos exigem mecanismos mais robustos do que aqueles tradicionalmente associados a sistemas conversacionais baseados apenas em regras ou classificação de intenção.

A síntese identificou cinco achados principais. Qualidade das evidências, avaliação e benchmarks apresentaram a maior cobertura, com 118 estudos. Supervisão humana e accountability operacional foram identificadas em 111 estudos; confiança, explicabilidade e governança orientada ao usuário, em 101; observabilidade, auditoria e monitoramento pós-implantação, em 94; e governança do conhecimento, RAG e guardrails, em 58.

A distribuição dos mecanismos revela que compliance e gestão de risco predominam no corpus, com 157 estudos, seguidos por controles técnicos e avaliação, com 108, e accountability e auditoria, com 96. Em contraste, contestabilidade e reparo foram identificados em apenas cinco estudos. Essa assimetria indica que a literatura está mais desenvolvida na identificação, prevenção e monitoramento de riscos do que na criação de mecanismos pelos quais usuários possam questionar, revisar ou reparar resultados produzidos por sistemas baseados em LLMs.

A distribuição pelas camadas reforça essa conclusão. A camada técnica apareceu em 147 estudos e a organizacional em 122, enquanto as camadas interacional e evolutiva foram identificadas em 49 e 36 estudos, respectivamente. A concentração de 78 estudos em saúde e medicina também evidencia que a maturidade da literatura não é uniforme entre os diferentes ambientes regulados.

Esses resultados mostram que os mecanismos técnicos são necessários, mas insuficientes quando isolados. RAG, guardrails, logs, tracing, avaliação contínua e monitoramento dependem de curadoria de conhecimento, documentação, processos organizacionais, supervisão humana, critérios de escalonamento e auditoria. Da mesma forma, explicabilidade sem contestação e supervisão sem atribuição clara de responsabilidades podem produzir transparência ou controle apenas aparentes.

A principal contribuição deste artigo é a proposição de um Modelo Conceitual Integrado de Governança Conversacional. O modelo organiza a governança em cinco camadas interdependentes: técnica, interacional, organizacional, regulatória e evolutiva. A camada técnica reúne mecanismos de controle e observabilidade. A camada interacional trata da relação entre sistema, usuário e intervenção humana. A camada organizacional define papéis, políticas, documentação e responsabilidades. A camada regulatória conecta o sistema a normas, riscos e obrigações setoriais. A camada evolutiva contempla aprendizagem operacional, análise de incidentes, atualização de bases, revisão de prompts e melhoria contínua.

Essa contribuição amplia a compreensão de governança em sistemas baseados em LLMs. Em vez de tratar o modelo como único objeto de controle, a revisão mostra que a governança deve abranger a resposta, a interação, a fonte de conhecimento, o fluxo de escalonamento, os registros de auditoria, os mecanismos de reparo, os processos organizacionais e os requisitos regulatórios. Assim, governança conversacional é compreendida como uma capacidade sociotécnica distribuída, sustentada por mecanismos que orientam, controlam, monitoram, justificam e corrigem o comportamento de sistemas baseados em LLMs em interações mediadas por linguagem natural.

## 7.1. Implicações para pesquisa

Para a pesquisa, os resultados indicam a necessidade de avançar em pelo menos cinco frentes. A primeira envolve o desenvolvimento de benchmarks específicos para governança conversacional em ambientes regulados, contemplando factualidade, rastreabilidade, escalonamento, contestabilidade, segurança, privacidade e conformidade. A segunda envolve estudos empíricos sobre supervisão humana, investigando como diferentes arranjos de human-in-the-loop, human-on-the-loop e human-in-command afetam risco, eficiência e accountability. A terceira envolve métodos de auditoria para sistemas conversacionais com RAG, ferramentas externas e guardrails. A quarta envolve modelos de explicabilidade orientados ao usuário, integrados ao fluxo conversacional. A quinta envolve pesquisas longitudinais sobre monitoramento pós-implantação, incidentes e aprendizagem operacional.

## 7.2. Implicações para prática

Para a prática organizacional, a revisão sugere que organizações que implantam LLMs em ambientes regulados precisam evitar uma abordagem centrada apenas em modelo, prompt ou interface. A governança deve ser desenhada como arquitetura operacional. Isso inclui curadoria de conhecimento, logs, tracing, avaliação contínua, guardrails, políticas de escalonamento, documentação, matriz de responsabilidade, processos de auditoria, análise de incidentes e canais de contestação.

Em contextos regulados, também é necessário calibrar mecanismos conforme o risco da interação. Interações informacionais simples podem demandar controles básicos, enquanto interações clínicas, financeiras, jurídicas ou administrativas exigem rastreabilidade mais forte, supervisão humana, documentação formal, proteção de dados e possibilidade de revisão. A adoção responsável de LLMs depende, portanto, da articulação entre design conversacional, governança técnica, compliance, gestão de risco e accountability institucional.

## 7.3. Limitações

Esta revisão apresenta limitações que devem ser consideradas na interpretação dos resultados. Primeiro, a busca foi sistemática, multifuente e delimitada a até 25 resultados armazenados por combinação entre estratégia e fonte. Além disso, a cobertura do Semantic Scholar e do arXiv foi parcial em razão de limitações de taxa e tempo de resposta. Essas condições reduzem a exaustividade potencial da recuperação, embora o corpus-semente e os procedimentos de snowballing tenham ampliado a cobertura.

Segundo, embora o corpus tenha reunido 407 estudos únicos avaliados em texto completo, a disponibilidade e a qualidade da extração textual podem ter afetado a recuperação de informações em documentos com problemas de formatação, digitalização ou estruturação. A validação por correspondência literal reduziu esse risco, mas não elimina integralmente perdas decorrentes da extração automatizada.

Terceiro, o corpus reuniu estudos empíricos, conceituais, técnicos, normativos e de revisão, caracterizados por diferentes desenhos metodológicos e estruturas de evidência. Essa heterogeneidade limita comparações diretas entre os estudos e exige que as avaliações de qualidade e confiança sejam interpretadas como indicadores de cautela analítica, e não como medidas uniformes de desempenho metodológico.

Quarto, a triagem, a extração, a avaliação de qualidade e a codificação foram assistidas por LLM em um único fluxo, e não por revisores humanos independentes em duplicata. Embora o processo tenha incorporado triagem determinística, validação textual e rastreabilidade das decisões, permanece a possibilidade de erros de classificação, interpretação ou extração associados ao uso de modelos de linguagem.

Por fim, as referências fundacionais ou contextuais foram separadas do corpus analítico para evitar que literatura teórica, normativa ou metodológica fosse contabilizada como evidência equivalente aos estudos diretamente aderentes ao objeto. Essa decisão aumenta a clareza da síntese, mas depende da classificação atribuída a cada estudo e pode ser revisada em investigações futuras.

## 7.4. Trabalhos futuros

Pesquisas futuras podem validar o modelo proposto em estudos de caso organizacionais, especialmente em saúde, finanças, governo, jurídico e seguros. Também são necessários estudos empíricos que comparem diferentes arranjos de supervisão humana, avaliem a efetividade de guardrails em produção, investiguem governança de bases RAG e desenvolvam métricas de governança conversacional. Outra direção relevante consiste em explorar padrões de UX conversacional para explicabilidade, contestação, reparo e comunicação de incerteza em sistemas baseados em LLMs.

Por fim, futuras revisões podem aprofundar comparações setoriais e examinar como requisitos regulatórios específicos moldam a governança conversacional em diferentes jurisdições. À medida que LLMs se tornam infraestrutura de interação em serviços críticos, a questão central deixa de ser apenas se esses sistemas respondem corretamente. Passa a ser se suas respostas podem ser controladas, justificadas, auditadas, contestadas e melhoradas de forma responsável.

## Apêndice A. Adaptações das consultas por fonte

As versões a seguir documentam as adaptações técnicas aplicadas às strings canônicas para fontes que não processam operadores booleanos, aspas e curingas de maneira uniforme.

Tabela A1. Consultas simplificadas por estratégia

Tabela A2. Consultas compactas empregadas no DOAJ

## Apêndice B. Resultados quantitativos completos

As tabelas deste apêndice apresentam os valores completos utilizados na construção dos Gráficos 2 a 5.

Tabela B1. Distribuição completa por família de mecanismos

Nota. As famílias são multirrótulo; um estudo pode estar representado em mais de uma categoria.

Fonte. Elaboração própria com base no corpus analítico da revisão.

Tabela B2. Distribuição completa pelas camadas do modelo conceitual

Nota. As camadas são multirrótulo; um estudo pode contribuir para diferentes dimensões.

Fonte. Elaboração própria com base no corpus analítico da revisão.

Tabela B3. Distribuição completa por domínio primário

Nota. O domínio primário é mutuamente exclusivo e totaliza os 177 estudos do corpus analítico.

Fonte. Elaboração própria com base no corpus analítico da revisão.

Tabela B4. Evidências centrais e de apoio por achado

Nota. Os achados são multirrótulo; um estudo pode sustentar mais de um achado.

Fonte. Elaboração própria com base no corpus analítico da revisão.

## Apêndice C. Capacidades do modelo conceitual

A Tabela C1 preserva a especificação detalhada das cinco capacidades do modelo, suas funções, mecanismos e evidências esperadas.

Tabela C1. Capacidades do Modelo Conceitual Integrado de Governança Conversacional

Nota. As capacidades são interdependentes e devem ser aplicadas de modo proporcional ao risco e ao contexto organizacional.

Fonte. Elaboração própria a partir da síntese da revisão.

## Referências

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

## Tabela 1

| Campo relacionado | Contribuição principal | Limite para o objeto desta revisão |
| --- | --- | --- |
| Governança de IA e Responsible AI | Define princípios, frameworks de risco e valores normativos | Geralmente opera em nível amplo, com menor detalhamento de mecanismos conversacionais |
| Accountability algorítmica | Explica responsabilidade, auditoria, justificativa e prestação de contas | Nem sempre considera diálogo, reparo, handoff e contestação em interfaces conversacionais |
| Explicabilidade e HCI | Oferece diretrizes para interação humano-IA, confiança e comunicação de limites | Frequentemente trata interação de modo genérico, sem foco em LLMs regulados |
| LLMs e modelos fundacionais | Identifica riscos de escala, alucinação, viés, opacidade e uso indevido | A governança operacional e interacional ainda aparece fragmentada |
| RAG, guardrails e LLMOps | Propõe mecanismos técnicos de controle, avaliação e monitoramento | Requer integração com accountability, supervisão humana e compliance |
| IA em ambientes regulados | Enfatiza risco, conformidade, documentação e impacto institucional | Precisa ser articulada à especificidade conversacional dos LLMs |
| Governança conversacional em LLMs | Integra mecanismos técnicos, interacionais, organizacionais, regulatórios e evolutivos | Objeto específico desta revisão |

## Tabela 2

| ID | Família | Blocos conceituais principais | Fontes de aplicação |
| --- | --- | --- | --- |
| A | Governança de LLMs | LLMs e IA generativa combinados a governança, accountability, compliance, auditoria e risco | Oito fontes, com sintaxe adaptada por API |
| B | LLMOps e observabilidade | LLMOps, observabilidade, monitoramento e guardrails combinados a governança e compliance | Oito fontes, com sintaxe adaptada por API |
| C | Governança conversacional | IA conversacional, chatbots e agentes combinados a LLMs, governança e supervisão humana | Oito fontes, com sintaxe adaptada por API |
| D | Ambientes regulados | LLMs e IA generativa combinados a setores regulados, risco, auditoria e conformidade | Oito fontes, com sintaxe adaptada por API |
| E | Supervisão humana e contestabilidade | Supervisão humana, human-in-the-loop, contestabilidade e escalonamento combinados a LLMs e chatbots | Oito fontes, com sintaxe adaptada por API |

## Tabela 3

| Código | Tipo | Critério |
| --- | --- | --- |
| I1 | Inclusão | Estudo sobre LLMs, IA generativa ou sistemas conversacionais |
| I2 | Inclusão | Presença de mecanismo técnico, interacional, organizacional, regulatório ou evolutivo de governança |
| I3 | Inclusão | Aplicação ou implicação relevante para ambiente regulado ou de alto impacto |
| I4 | Inclusão | Texto completo suficiente para avaliação |
| I5 | Inclusão | Publicação entre 2020 e 2026 |
| I6 | Inclusão | Estudo empírico, técnico, conceitual, normativo ou revisão aderente ao objeto |
| I7 | Inclusão | Referência anterior a 2020 com função fundacional, teórica ou metodológica |
| E1 | Exclusão | Ausência de LLM, IA generativa ou sistema conversacional como objeto substantivo do estudo |
| E2 | Exclusão | Ausência de mecanismo técnico, interacional, organizacional, regulatório ou evolutivo de governança |
| E3 | Exclusão | Ausência de aplicação, implicação ou transferibilidade relevante para ambiente regulado ou de alto impacto |
| E4 | Exclusão | Texto completo insuficiente para avaliação das questões de pesquisa |
| E5 | Exclusão | Publicação anterior a 2020 sem função fundacional, teórica ou metodológica diretamente relacionada à revisão |
| E6 | Exclusão | Registro duplicado, manuscrito interno do projeto ou versão redundante de estudo já representado |
| E7 | Exclusão | Metadados insuficientes ou conteúdo sem evidência substantiva para classificação |

## Tabela 4

| Elemento | Definição no estudo | Operacionalização |
| --- | --- | --- |
| Universo avaliado | 407 estudos únicos | Avaliação em texto completo |
| Corpus analítico | 177 estudos | 23 evidências centrais e 154 de apoio |
| Referências fundacionais/contextuais | 112 | Fundamentação teórica, normativa e metodológica |
| Estudos excluídos | 118 | Insuficiência de aderência aos critérios |
| Casos borderline | 0 | Todos os casos foram adjudicados |
| Triagem inicial | Determinística | Taxonomia controlada e evidências literais |
| Avaliação assistida | Python + LLM | Classificação e extração estruturada |
| Qualidade | CASP/JBI adaptado | Avaliação proporcional ao desenho do estudo |
| Confiança | CERQual adaptado | Coerência, adequação, relevância e limitações |
| Evidência | Validação textual | Conferência contra o texto extraído |
| Síntese | Temática e conceitual | Mecanismos e modelo integrado |

## Tabela 5

| Implicação derivada | Consequência para a governança | Oportunidade de pesquisa |
| --- | --- | --- |
| Métricas tradicionais são insuficientes para avaliar governança conversacional | A avaliação precisa incluir risco, rastreabilidade, segurança, fontes, escalonamento e contestação | Desenvolver benchmarks específicos para LLMs conversacionais em ambientes regulados |
| Supervisão humana é frequentemente tratada de forma genérica | Human-in-the-loop precisa ser operacionalizado com papéis, critérios e autoridade | Investigar modelos de supervisão humana proporcional ao risco da interação |
| Observabilidade é condição para auditoria e accountability | Logs, tracing e registros de decisão precisam cobrir a cadeia completa da resposta | Propor frameworks de observabilidade para sistemas conversacionais com RAG e ferramentas |
| RAG desloca parte da governança para a base de conhecimento | Fonte, validade, versão e curadoria passam a ser dimensões críticas | Desenvolver práticas de governança do conhecimento para LLMs em produção |
| Guardrails são necessários, mas insuficientes quando isolados | Controles técnicos precisam ser conectados a revisão humana, auditoria e monitoramento | Avaliar a efetividade de guardrails em cenários reais de risco regulado |
| Explicabilidade precisa operar no diálogo | O usuário precisa compreender limites, fontes, incertezas e caminhos de contestação | Projetar padrões de explicação, contestação e reparo em UX conversacional |
| Accountability é distribuída entre múltiplos atores e componentes | Responsabilidade precisa cobrir modelo, prompts, dados, ferramentas, políticas e organização | Construir modelos sociotécnicos de responsabilização para sistemas baseados em LLMs |
| Governança precisa continuar após a implantação | Sistemas mudam com uso, atualização de modelo, base e política | Investigar ciclos de aprendizagem operacional e monitoramento pós-implantação |

## Tabela 6

| Pergunta de governança | Camada mais diretamente envolvida | Evidência ou controle verificável |
| --- | --- | --- |
| O sistema usa fontes autorizadas e atualizadas? | Técnica e organizacional | Base RAG versionada, fonte validada, data de atualização |
| A resposta pode ser reconstruída depois? | Técnica e regulatória | Logs, traces, prompt, fonte recuperada, resposta final |
| O usuário sabe quando o sistema tem limitações? | Interacional | Aviso de incerteza, explicação, recusa justificada |
| Há caminho para contestar ou corrigir uma resposta? | Interacional e organizacional | Recurso, feedback, revisão humana, protocolo de reparo |
| Quem é responsável por uma falha? | Organizacional | Matriz de responsabilidade, papéis, processo de incidentes |
| O sistema atende requisitos de risco e compliance? | Regulatória | Avaliação de impacto, controles documentados, auditoria |
| O sistema melhora após incidentes? | Evolutiva | Análise de incidente, revisão de base, ajuste de prompt, novo teste |

## Tabela 7

| ID | Consulta simplificada |
| --- | --- |
| A | large language model governance accountability compliance audit risk management |
| B | LLMOps LLM observability monitoring guardrails governance compliance accountability |
| C | conversational AI chatbot large language model governance accountability human oversight |
| D | large language model generative AI healthcare finance banking insurance government compliance governance risk |
| E | human oversight human-in-the-loop contestability meaningful human control large language model chatbot |

## Tabela 8

| ID | Consulta utilizada no DOAJ |
| --- | --- |
| A | large language model governance |
| B | LLMOps observability governance |
| C | conversational AI large language model governance |
| D | large language model healthcare governance |
| E | human oversight large language model |

## Tabela 9

| Família normalizada | Central | Apoio | Total | % do corpus |
| --- | --- | --- | --- | --- |
| Compliance e gestão de risco | 23 | 134 | 157 | 88,7% |
| Controles técnicos e avaliação | 18 | 90 | 108 | 61,0% |
| Accountability e auditoria | 17 | 79 | 96 | 54,2% |
| Explicabilidade, confiança e comunicação de limites | 13 | 71 | 84 | 47,5% |
| Aprendizagem operacional e monitoramento | 18 | 63 | 81 | 45,8% |
| Supervisão humana e escalonamento | 12 | 64 | 76 | 42,9% |
| Governança do conhecimento | 8 | 36 | 44 | 24,9% |
| Contestabilidade e reparo | 1 | 4 | 5 | 2,8% |

## Tabela 10

| Camada | Central | Apoio | Total | % do corpus |
| --- | --- | --- | --- | --- |
| Técnica | 20 | 127 | 147 | 83,1% |
| Organizacional | 19 | 103 | 122 | 68,9% |
| Regulatória | 9 | 76 | 85 | 48,0% |
| Interacional | 12 | 37 | 49 | 27,7% |
| Evolutiva | 7 | 29 | 36 | 20,3% |

## Tabela 11

| Domínio primário | Central | Apoio | Total | % do corpus |
| --- | --- | --- | --- | --- |
| Saúde e medicina | 12 | 66 | 78 | 44,1% |
| Multissetorial ou transversal | 5 | 37 | 42 | 23,7% |
| Tecnologia e operações empresariais | 5 | 12 | 17 | 9,6% |
| Educação | 0 | 13 | 13 | 7,3% |
| Serviços financeiros e seguros | 0 | 9 | 9 | 5,1% |
| Jurídico e judiciário | 0 | 7 | 7 | 4,0% |
| Infraestrutura crítica, telecom e cibersegurança | 0 | 6 | 6 | 3,4% |
| Setor público e governo | 1 | 4 | 5 | 2,8% |
| Total | 23 | 154 | 177 | 100% |

## Tabela 12

| Achado da revisão | Central | Apoio | Total | % do corpus |
| --- | --- | --- | --- | --- |
| F1. Qualidade das evidências, avaliação e benchmarks | 18 | 100 | 118 | 66,7% |
| F2. Supervisão humana e accountability operacional | 19 | 92 | 111 | 62,7% |
| F3. Observabilidade, auditoria e monitoramento pós-implantação | 18 | 76 | 94 | 53,1% |
| F4. Governança do conhecimento, RAG e guardrails | 9 | 49 | 58 | 32,8% |
| F5. Confiança, explicabilidade e governança orientada ao usuário | 17 | 84 | 101 | 57,1% |

## Tabela 13

| Camada | Capacidade | Mecanismos | Evidência teórica associada | Resultado esperado |
| --- | --- | --- | --- | --- |
| Técnica | Controlar e observar o comportamento do sistema | RAG, guardrails, logs, tracing, red teaming, avaliação contínua | Riscos de modelos fundacionais e necessidade de avaliação contínua (Bommasani et al., 2021; Weidinger et al., 2022) | Sistema monitorável, testável e tecnicamente auditável |
| Interacional | Governar a relação entre usuário, sistema e intervenção humana | Explicação, confirmação, handoff, escalonamento, contestação, reparo | Diretrizes de interação humano-IA e confiança calibrada (Amershi et al., 2019; Shneiderman, 2020) | Usuário informado, possibilidade de correção e redução de automação indevida |
| Organizacional | Atribuir responsabilidades e sustentar processos de governança | Papéis, políticas, comitês, documentação, matriz de responsabilidade | Accountability como relação de justificação e responsabilização (Bovens, 2007; Wieringa, 2020) | Responsabilidade institucional explícita |
| Regulatória | Alinhar o sistema a normas, riscos e obrigações setoriais | Compliance, avaliação de impacto, proteção de dados, auditoria, evidências | Gestão de risco em IA e abordagem baseada em risco (National Institute of Standards and Technology, 2023) | Conformidade demonstrável e proporcionalidade ao risco |
| Evolutiva | Aprender com uso real e adaptar o sistema de modo controlado | Feedback loops, análise de incidentes, atualização de base, revisão de prompts | Monitoramento pós-implantação e auditoria contínua (Raji et al., 2020) | Melhoria contínua governada e redução de reincidência de falhas |
