# Exportação textual — Artigo_v2.1_para_editar

Origem: `C:/Users/yhenr/OneDrive/Documentos/ChatGPT/Revisão de Literatura • Governança Conversacional em Sistemas Baseados em Modelos de Linguagem de Grande Escala em Ambientes  Regulados_ uma revisão sistemática da literatura/Artigo/Artigo_v2.1_para_editar.docx`

Governança Conversacional em Sistemas Baseados em Modelos de Linguagem de Grande Escala em Ambientes Regulados: uma revisão sistemática da literatura

Conversational Governance in Large Language Model-Based Systems in Regulated Environments: A Systematic Literature Review

Resumo

Esta revisão sistemática investiga mecanismos de governança conversacional em sistemas baseados em LLMs aplicados a ambientes regulados. Orientada pelo PRISMA 2020, documentou decisões sobre 383 textos completos e consolidou 358 estudos únicos no corpus analítico, sendo 30 evidências centrais e 328 de apoio. Os resultados mostram predominância de compliance, gestão de risco, accountability e monitoramento, enquanto contestabilidade e reparo permanecem pouco consolidados. A principal contribuição é um modelo integrado de cinco camadas - técnica, interacional, organizacional, regulatória e evolutiva - derivado da síntese e ainda dependente de validação empírica.

Palavras-chave: governança conversacional; LLMs; ambientes regulados; accountability; auditoria; supervisão humana.

Abstract

This systematic review investigates conversational governance mechanisms in LLM-based systems deployed in regulated environments. Guided by PRISMA 2020, it documented decisions for 383 full texts and consolidated 358 unique studies in the analytical corpus, including 30 central and 328 supporting evidence studies. Results show a predominance of compliance, risk management, accountability, and monitoring, whereas contestability and repair remain underdeveloped. The main contribution is an integrated five-layer model - technical, interactional, organizational, regulatory, and evolutionary - derived from the synthesis and still requiring empirical validation.

Keywords: conversational governance; LLMs; regulated environments; accountability; auditing; human oversight.

## 1. Introdução

Modelos de Linguagem de Grande Escala (LLMs) ampliaram o uso de interfaces conversacionais em serviços de saúde, finanças, governo, jurídico, seguros, educação regulada e telecomunicações. A geração aberta de linguagem, a integração com fontes externas e a capacidade de acionar ferramentas aumentam o valor desses sistemas, mas também introduzem riscos de alucinação, opacidade, viés, uso indevido e instabilidade comportamental (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022).

Em ambientes regulados, uma resposta conversacional pode influenciar orientação clínica, aconselhamento financeiro, acesso a serviços públicos, interpretação jurídica ou exercício de direitos. A governança, portanto, não pode se restringir ao desempenho do modelo: precisa abranger a cadeia que produz a resposta, incluindo prompts, fontes de conhecimento, guardrails, ferramentas, registros, supervisão humana e contexto organizacional.

Neste artigo, sistemas conversacionais baseados em LLMs são entendidos como **configurações sociotécnicas**: arranjos nos quais modelos, dados, interfaces, guardrails, registros e mecanismos de monitoramento funcionam em conjunto com pessoas, papéis organizacionais, procedimentos, normas e responsabilidades institucionais. Essa perspectiva foi adotada porque os efeitos regulatórios de uma resposta resultam da interação entre tecnologia, usuários, organizações e contexto normativo, e não apenas do comportamento do modelo. Ela permite analisar conjuntamente as dimensões técnica, interacional, organizacional, regulatória e evolutiva identificadas na revisão.

A literatura oferece bases importantes, porém fragmentadas. Governança de IA e Responsible AI estabelecem princípios; accountability algorítmica trata de justificação, auditoria e responsabilização; estudos de LLMs examinam riscos e avaliação; interação humano-IA investiga confiança, transparência e correção; e trabalhos setoriais enfatizam conformidade e segurança. Falta uma síntese que integre essas perspectivas em mecanismos próprios da interação conversacional.

Esta revisão sistemática identifica e organiza mecanismos técnicos, interacionais, organizacionais, regulatórios e evolutivos que orientam, controlam, monitoram, justificam e corrigem sistemas conversacionais baseados em LLMs em ambientes regulados. As questões de pesquisa examinam os mecanismos relatados, sua relação com risco e accountability, as capacidades associadas, as lacunas metodológicas e setoriais e o papel de explicabilidade, contestabilidade, reparo e aprendizagem operacional.

A principal contribuição é o Modelo Conceitual Integrado de Governança Conversacional, apresentado desde o início como síntese dos resultados. Suas cinco camadas - técnica, interacional, organizacional, regulatória e evolutiva - mostram que governar a conversa requer coordenar controles do sistema, desenho da interação, responsabilidades institucionais, obrigações externas e aprendizagem em produção.

O artigo contribui ao consolidar uma literatura dispersa, organizar os mecanismos em famílias analíticas e propor uma arquitetura conceitual aplicável à pesquisa, à avaliação e à prática organizacional. A narrativa segue do posicionamento da lacuna ao método, aos resultados, ao modelo e às suas implicações. Essa lacuna orienta a revisão das abordagens existentes na seção seguinte.

## 2. Trabalhos relacionados

A literatura relevante converge em cinco vertentes. A primeira, governança de IA e Responsible AI, consolidou princípios como justiça, transparência, privacidade, segurança, robustez e accountability, mas também demonstrou que princípios isolados não garantem implementação responsável (Floridi et al., 2018; Jobin et al., 2019; Mittelstadt, 2019). Frameworks como o NIST AI RMF e o AI Act europeu aproximam esses princípios da gestão de risco, sem detalhar plenamente a governança que ocorre durante a conversa (National Institute of Standards and Technology, 2023; European Parliament & Council of the European Union, 2024).

A segunda vertente trata de accountability, auditoria e explicabilidade. Accountability pressupõe atores capazes de explicar e justificar condutas diante de uma instância avaliadora, com possibilidade de julgamento e consequências (Bovens, 2007; Busuioc, 2021). Em sistemas de IA, o objeto dessa responsabilização se distribui entre dados, modelos, decisões, efeitos e instituições, exigindo documentação, rastreabilidade e auditoria ao longo do ciclo de vida (Mökander et al., 2023; Raji et al., 2020; Wieringa, 2020).

A terceira vertente examina modelos fundacionais e IA generativa. A escala e a generalidade dos LLMs propagam riscos por diferentes aplicações, enquanto respostas plausíveis podem ocultar erros factuais (Bommasani et al., 2021; Ji et al., 2023). RAG, guardrails, avaliação e observabilidade mitigam parte desses riscos, mas transferem novas responsabilidades para fontes, recuperação, integração e operação (Gao et al., 2023).

A quarta vertente, interação humano-IA, mostra que usuários precisam compreender capacidades, limites, incertezas e caminhos de correção (Amershi et al., 2019; Shneiderman, 2020). Em uma interface conversacional, explicação, confirmação, recusa, escalonamento e reparo são simultaneamente escolhas de design e controles de governança; a fluência linguística pode elevar confiança além da competência real do sistema (Luger & Sellen, 2016; Rapp et al., 2021).

A quinta vertente discute a adoção de IA em setores regulados. Saúde, finanças, governo, jurídico e seguros compartilham exigências de segurança, privacidade, auditabilidade, dever de cuidado e contestação, embora variem em risco e obrigação setorial. Na saúde, propostas de avaliação de chatbots mostram como segurança, experiência do usuário e critérios de desempenho precisam ser analisados conjuntamente (Hua et al., 2025; Wiens et al., 2019). A lacuna não é ausência de princípios ou controles isolados, mas falta de integração entre o que controla o sistema, governa a interação, atribui responsabilidades, demonstra conformidade e aprende com o uso real. Essa lacuna fundamenta o modelo de cinco camadas e orienta o método de busca e análise apresentado a seguir.

## 3. Método

A revisão seguiu o PRISMA 2020 e recomendações para revisões sistemáticas em engenharia de software e síntese de evidências (Aromataris et al., 2024; Kitchenham & Charters, 2007; Page et al., 2021; Wohlin, 2014). O protocolo articulou identificação e consolidação do corpus, avaliação de elegibilidade e qualidade, validação de evidências e síntese temática orientada à construção conceitual.

A busca combinou consultas estruturadas e expansão bibliográfica. A recuperação ampliada utilizou múltiplas bases e serviços em cinco famílias: governança de LLMs, LLMOps e observabilidade, governança conversacional, ambientes regulados e supervisão humana/contestabilidade. Referências, citações, autoria e veículos foram rastreados para ampliar a cobertura.

Tabela 1. Famílias conceituais e operacionalização da estratégia de busca

Nota. As consultas foram adaptadas à sintaxe de cada base e serviço de busca.

Fonte. Elaboração própria com base nos registros de execução da busca.

A recuperação bibliográfica foi realizada em rodadas sucessivas, combinando cinco famílias conceituais, múltiplas bases e serviços de busca e estratégias complementares de rastreamento de referências, citações, autoria e veículos. Em cada rodada, os resultados foram ampliados progressivamente até a centésima posição por combinação de consulta e fonte, deduplicados por identificadores persistentes e, subsidiariamente, por título normalizado, autoria e ano. A estabilidade da recuperação foi examinada por análise de sensibilidade, verificando-se se as rodadas posteriores acrescentavam estudos elegíveis não identificados nas etapas anteriores. Esse procedimento permitiu avaliar a abrangência da busca sem assumir que os primeiros resultados fossem necessariamente os mais relevantes.

O snowballing incluiu referências citadas, trabalhos citantes, relacionados e expansões controladas por autoria e veículo. Todos os registros foram consolidados e deduplicados por DOI, título exato e similaridade textual, com validação de grupos potencialmente ambíguos. Como verificação de abrangência, a execução ampliada registrou 1.342 ocorrências e 1.074 registros únicos após deduplicação interna, distribuídos por todas as faixas examinadas até a centésima posição. A seleção integral documentou decisões sobre 383 textos completos.

Foram incluídos estudos sobre LLMs, IA generativa ou sistemas conversacionais que apresentassem mecanismos de governança relacionados a ambientes regulados ou de alto impacto. O corpus analítico final reuniu 358 estudos únicos, dos quais 30 foram classificados como evidências centrais e 328 como evidências de apoio. Outros 24 registros foram considerados fora do escopo da revisão.

Os 358 estudos estão identificados individualmente no catálogo virtual da pesquisa, objeto digital de documentação desenvolvido em código aberto para esta revisão.[^1] O catálogo permite consultar referência, classificação, setor, família de mecanismos, camada normalizada, PDF, hash, página e trecho de evidência. A matriz estudo–mecanismo–camada é a fonte para recalcular tabelas e figuras, enquanto os PDFs rastreados constituem a fonte do texto integral.

[^1]: Catálogo bibliográfico da pesquisa: *Governança conversacional em sistemas baseados em LLMs*. GitHub Pages. https://yhenriux.github.io/revisao-literatura-governanca-ia-regulados/

Tabela 2. Critérios consolidados de inclusão e exclusão

Nota. A tabela resume os critérios aplicados na seleção dos estudos.

Fonte. Protocolo metodológico da revisão.

A extração de texto completo registrou páginas, qualidade da extração e trechos relevantes. A síntese temática combinou codificação aberta, agrupamento axial e comparação iterativa, conforme a abordagem de Braun e Clarke (2006). Uma triagem determinística localizou termos e evidências literais; em seguida, o LLM recebeu metadados e trechos selecionados, produziu campos estruturados e foi instruído a não inferir informação ausente. O modelo sugeriu elegibilidade, classificação e códigos, mas não tomou a decisão científica final.

As classificações sugeridas pelo LLM a partir dos textos integrais foram validadas por avaliação humana, mediante verificação dos trechos e das páginas correspondentes na evidência original. Eventuais divergências foram resolvidas com base na leitura da fonte primária.

Os instrumentos CASP/JBI adaptados foram usados como apoio para identificar limitações metodológicas e qualificar a interpretação (Aromataris et al., 2024; Critical Appraisal Skills Programme, n.d.), sem determinar elegibilidade ou a distinção entre evidência central e de apoio. As dimensões do CERQual orientaram a reflexão sobre coerência, adequação, relevância e limitações dos achados qualitativos, conforme a orientação de Lewin et al. (2018); não foram atribuídos níveis formais de confiança a achados incompatíveis com essa abordagem.

A classificação como evidência central exigiu simultaneamente três condições: tratamento direto de governança, supervisão, risco, accountability, auditoria, compliance ou operação controlada de LLMs ou sistemas conversacionais; relação explícita com ambiente regulado, de alto impacto ou mecanismo demonstravelmente transferível; e contribuição substantiva para pelo menos uma questão da revisão, por resultado empírico, síntese sistemática, mecanismo avaliado ou arquitetura conceitual. Estudos elegíveis com contribuição periférica, contextual ou apenas transferível foram classificados como evidência de apoio.

As perguntas de pesquisa e a literatura inicial forneceram dimensões sensibilizadoras, sem constituírem um esquema final fechado. A análise combinou codificação aberta, agrupamento axial, comparação constante e refinamento iterativo. A consolidação desses padrões resultou nas cinco camadas, posteriormente aplicadas como vocabulário normalizado ao corpus. As frequências foram calculadas a partir da aplicação desse esquema aos estudos incluídos, seguindo os critérios e procedimentos descritos nesta seção.

As categorias analíticas seguem uma regra de codificação multirrótulo: um mesmo estudo pode ser associado simultaneamente a mais de uma família de mecanismos, setor, achado ou camada quando o texto apresentar evidência correspondente. As contagens representam ocorrências de codificação e não necessariamente estudos distintos; por isso, os totais entre categorias não devem ser somados para reconstruir o tamanho do corpus. Nas tabelas de coocorrência, cada célula indica o número de estudos codificados simultaneamente na categoria da linha e na categoria da coluna.

O Gráfico 1 apresenta o fluxo de composição do corpus e permite visualizar as etapas de identificação, seleção e inclusão.

Gráfico 1. Composição das decisões documentadas na seleção integral

Fonte. Elaboração própria com base na base consolidada da revisão.

## 4. Resultados e Modelo Conceitual Integrado

As famílias de mecanismos e as camadas conceituais foram codificadas de maneira multirrótulo, de modo que um estudo pôde contribuir para diferentes categorias. As frequências representam incidência temática, e não necessariamente implementação ou validação empírica.

O Gráfico 2 compara a incidência das oito famílias normalizadas de mecanismos e a quantidade de evidências centrais em cada uma. A posição do marcador final representa o total de estudos, enquanto o marcador inicial indica o subconjunto classificado como evidência central.

Gráfico 2. Incidência das famílias de mecanismos e presença de evidência central

Fonte. Elaboração própria com base no corpus analítico.

Compliance e gestão de risco apresentaram a maior cobertura, com 339 estudos (94,7% do corpus) e 29 das 30 evidências centrais (96,7%). Accountability e auditoria apareceram em 250 estudos (69,8%), supervisão humana e escalonamento em 243 (67,9%), e aprendizagem operacional e monitoramento em 232 (64,8%). Contestabilidade e reparo tiveram incidência residual, com três estudos (0,8%) e nenhuma evidência central. O padrão desloca a lacuna principal da identificação de riscos para a capacidade de recurso, correção e reparação.

A reorganização dos códigos pelas cinco camadas do modelo conceitual permite observar o grau de consolidação de cada dimensão. O Gráfico 3 compara evidências centrais e de apoio nas camadas técnica, interacional, organizacional, regulatória e evolutiva.

Gráfico 3. Distribuição dos estudos pelas camadas do modelo conceitual

Fonte. Elaboração própria com base no corpus analítico.

A camada regulatória foi identificada em 339 estudos (94,7% do corpus) e a organizacional em 324 (90,5%), seguidas pela técnica, com 284 (79,3%). As dimensões interacional e evolutiva reuniram 248 (69,3%) e 233 estudos (65,1%), respectivamente. A diferença entre as camadas é menos polarizada que no corpus anterior, mas a raridade de mecanismos de contestação mostra que a presença de códigos interacionais não equivale, por si só, a poder efetivo de ação do usuário.

## 4.1. Mecanismos técnicos e operacionais

A primeira família de mecanismos reúne componentes técnicos que permitem controlar, observar, restringir, avaliar ou corrigir o comportamento de sistemas baseados em LLMs. Esses mecanismos incluem RAG, guardrails, logs, tracing, observabilidade, red teaming, avaliação contínua, monitoramento pós-implantação, versionamento, documentação técnica e governança de bases de conhecimento.

A literatura sobre modelos fundacionais aponta que LLMs introduzem riscos específicos de opacidade, alucinação, viés, produção de conteúdo nocivo e dificuldade de avaliação em larga escala (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022). Em razão disso, a governança técnica passa a exigir mais que métricas tradicionais de desempenho. Ela precisa registrar o contexto de uso, rastrear entradas e saídas, monitorar falhas, controlar fontes de conhecimento e avaliar o comportamento do sistema em situações ordinárias e excepcionais.

A recuperação aumentada por geração, ou RAG, aparece como um mecanismo relevante porque conecta o modelo generativo a fontes externas de conhecimento. Esse arranjo pode reduzir a dependência exclusiva da memória paramétrica do modelo e permitir maior controle sobre atualidade, rastreabilidade e domínio das respostas (Gao et al., 2023). Contudo, RAG não resolve por si só o problema da governança. A qualidade das respostas passa a depender também da curadoria da base de conhecimento, da estratégia de recuperação, do ranqueamento dos documentos, da atualização das fontes e da forma como evidências são apresentadas ao usuário.

Guardrails também ocupam papel central na literatura recente. Eles podem operar como regras de bloqueio, filtros de segurança, classificadores de risco, limites de escopo, validações de formato, restrições de conteúdo ou políticas de resposta. Em sistemas conversacionais, esses mecanismos ajudam a reduzir respostas perigosas, juridicamente sensíveis, discriminatórias ou fora do domínio autorizado. Entretanto, guardrails podem falhar quando são tratados apenas como filtros técnicos, sem integração com processos de revisão humana, monitoramento de incidentes, auditoria e atualização contínua.

Logs, tracing e observabilidade ampliam a governança ao registrar o comportamento do sistema em produção. A observabilidade permite examinar prompts, respostas, fontes recuperadas, ferramentas chamadas, latência, erros, taxas de escalonamento, avaliações de segurança, feedback do usuário e eventos críticos. Em ambientes regulados, esses registros são relevantes para auditoria, investigação de incidentes, melhoria contínua e prestação de contas. A literatura de auditoria algorítmica reforça que mecanismos de documentação e rastreabilidade precisam cobrir o ciclo de vida do sistema, não apenas o momento de modelagem (Raji et al., 2020).

A avaliação contínua é outro mecanismo técnico-operacional. Ela inclui testes antes da implantação, red teaming, avaliação com datasets de referência, monitoramento pós-implantação e análise de regressão quando prompts, modelos, bases de conhecimento ou políticas são alterados. Em LLMs, a avaliação precisa contemplar factualidade, segurança, robustez, aderência ao domínio, consistência, privacidade, viés, toxicidade, capacidade de recusa, rastreabilidade de fontes e comportamento diante de incerteza. Essa lógica aproxima a governança técnica da gestão de risco, pois os testes deixam de ser apenas indicadores de qualidade e passam a funcionar como evidências de controle.

O conjunto das evidências indica que os mecanismos técnicos e operacionais oferecem a camada de controle instrumental da governança conversacional. Eles tornam possível observar, restringir e corrigir o comportamento do sistema. Sua efetividade depende da conexão com mecanismos humanos, organizacionais e regulatórios, examinados nas subseções seguintes.

## 4.2. Supervisão humana, escalonamento e contestabilidade

Mecanismos de supervisão humana e escalonamento foram identificados em 243 estudos (67,9% do corpus), incluindo 14 evidências centrais (46,7% das evidências centrais); contestabilidade e reparo apareceram em apenas três estudos (0,8%), sem evidência central. A diferença revela atenção ampla à intervenção humana, mas baixa operacionalização de mecanismos formais para questionar, revisar ou reparar respostas.

A literatura de interação humano-IA demonstra que a qualidade da automação depende da forma como o sistema comunica suas capacidades, limitações, incertezas e possibilidades de correção (Amershi et al., 2019). Em sistemas conversacionais, essa comunicação não ocorre apenas em painéis administrativos ou documentos técnicos. Ela ocorre também no próprio diálogo, quando o sistema reconhece limites, solicita confirmação, orienta o usuário, encaminha para atendimento humano ou explica por que não pode executar determinada ação.

O escalonamento é um mecanismo interacional central. Ele define quando e como o sistema deve transferir a interação para uma pessoa, equipe, canal especializado ou processo de revisão. Em atendimento, saúde, finanças e setor público, escalonamento não é apenas uma conveniência de UX. Ele funciona como salvaguarda contra erro, incerteza, ambiguidade, sofrimento do usuário, risco jurídico, falha de compreensão ou necessidade de julgamento contextual. A literatura sobre chatbots mostra que a experiência do usuário é prejudicada quando agentes conversacionais excedem suas capacidades percebidas ou não oferecem caminhos claros de reparo (Følstad & Brandtzaeg, 2020; Luger & Sellen, 2016).

Contestabilidade e reparo ampliam a supervisão humana para além do momento da resposta. Contestabilidade refere-se à possibilidade de questionar, revisar ou disputar uma saída, recomendação ou decisão mediada por IA. Reparo refere-se aos mecanismos pelos quais erros são reconhecidos, corrigidos e incorporados a melhorias futuras. Em sistemas baseados em LLMs, esses mecanismos são especialmente importantes porque erros podem ser expressos em linguagem fluida e persuasiva, dificultando a percepção imediata de incerteza ou inconsistência.

A supervisão humana efetiva exige definição de papéis e critérios. Não basta afirmar que há “humano no loop” se não estiver claro quem intervém, em que momento, com qual autoridade, com quais evidências e sob quais responsabilidades. Esse ponto conecta supervisão humana à accountability organizacional. Uma intervenção humana meramente simbólica pode criar aparência de controle sem produzir responsabilização real.

## 4.3. Accountability, auditoria e compliance

A incidência de accountability, auditoria, compliance e gestão de risco demonstra amplo reconhecimento de responsabilidades e obrigações, embora sua operacionalização varie entre documentação, controles técnicos, auditorias e estruturas organizacionais.

A accountability algorítmica desloca a discussão da performance técnica para relações de responsabilidade. Bovens (2007) define accountability como uma relação em que um ator deve explicar e justificar sua conduta diante de uma instância avaliadora. Em sistemas de IA, essa relação se torna distribuída, pois decisões e respostas podem envolver desenvolvedores, fornecedores de modelo, equipes de produto, curadores de conhecimento, gestores de risco, áreas jurídicas, operadores humanos e organizações usuárias. Wieringa (2020) mostra que a accountability algorítmica pode incidir sobre dados, modelos, decisões, efeitos e instituições, o que reforça sua natureza sociotécnica.

A auditoria é o mecanismo que operacionaliza parte dessa accountability. Ela pode ocorrer antes da implantação, durante o ciclo de desenvolvimento, em produção ou após incidentes. Auditorias de IA podem examinar dados, documentação, modelos, métricas, processos decisórios, riscos, impactos e mecanismos de mitigação (Raji et al., 2020). Para LLMs, a auditoria precisa incluir também prompts, políticas de sistema, bases recuperadas, ferramentas conectadas, guardrails, logs conversacionais, registros de escalonamento e respostas geradas em contextos sensíveis.

A conformidade regulatória adiciona critérios externos à governança. Em setores regulados, sistemas de IA precisam observar normas de proteção de dados, segurança, direitos do consumidor, regras setoriais, deveres profissionais e requisitos de documentação. O AI Risk Management Framework do NIST propõe funções de governança, mapeamento, medição e gestão de riscos, oferecendo uma estrutura operacional para organizar responsabilidades ao longo do ciclo de vida de sistemas de IA (National Institute of Standards and Technology, 2023). A abordagem baseada em risco também aparece no AI Act europeu, que diferencia obrigações conforme o potencial de dano e o contexto de aplicação (European Parliament & Council of the European Union, 2024).

Em sistemas conversacionais, compliance não pode ser tratado apenas como checagem documental. A conformidade precisa aparecer no comportamento do sistema, nas respostas dadas, nos limites de escopo, nas recusas, no registro das interações, na proteção de dados, na forma de recuperar conhecimento e nos mecanismos de contestação. Um assistente financeiro, clínico ou governamental pode estar formalmente documentado, mas ainda assim falhar se orientar usuários de modo inadequado, ocultar incerteza, não escalar casos críticos ou não preservar trilhas de auditoria.

A documentação também é parte da accountability. Model cards, system cards, relatórios de avaliação, registros de mudanças, matrizes de risco, políticas de uso e descrições de arquitetura permitem que atores internos e externos compreendam limites, pressupostos e responsabilidades do sistema. No caso de LLMs, a documentação precisa acompanhar não apenas o modelo, mas o sistema conversacional como um todo: orquestração, prompts, dados, ferramentas, canais, métricas, mecanismos de segurança e processos humanos associados.

## 4.4. Aplicações e domínios regulados

A classificação por domínio primário revelou concentração na saúde e na medicina, com 150 estudos (41,9% do corpus). Outros 112 (31,3%) apresentaram natureza multissetorial ou transversal, enquanto 47 (13,1%) se concentraram em tecnologia e operações empresariais.

Os demais ambientes regulados apresentaram cobertura menor: educação reuniu 17 estudos (4,7%); finanças e seguros, 14 (3,9%); infraestrutura crítica e cibersegurança, dez (2,8%); jurídico e judiciário, quatro (1,1%); e governo e setor público, quatro (1,1%).

Entre as 30 evidências centrais, 19 pertencem à saúde e à medicina, seis a tecnologia e operações empresariais, quatro são multissetoriais e uma se concentra em finanças e seguros. Os demais domínios possuem estudos de apoio, mas nenhum classificado como evidência central.

A distribuição por domínio primário é apresentada no Gráfico 4. Como os domínios são mutuamente exclusivos, o comprimento das barras representa sua participação no corpus analítico.

Gráfico 4. Composição setorial do corpus analítico

Fonte. Elaboração própria com base no corpus analítico.

A concentração em saúde e medicina, responsável por 41,9% do corpus, contrasta com a cobertura reduzida dos demais domínios específicos. Essa distribuição limita a transferência direta dos achados e exige validação do modelo em ambientes com obrigações, riscos, usuários, consequências e práticas profissionais distintos.

## 4.5. Achados da revisão

Como os achados foram codificados de maneira multirrótulo, essas quantidades representam incidência temática e não categorias mutuamente exclusivas. A identificação de determinado mecanismo também não significa necessariamente sua implementação ou validação empírica, pois parte da literatura o apresenta como princípio normativo, requisito arquitetural, recomendação ou agenda de pesquisa.

Os cinco achados diferem tanto em cobertura temática quanto na quantidade de evidências centrais que os sustentam. O Gráfico 5 combina essas duas dimensões: o marcador final representa o total de estudos, e o marcador inicial indica o subconjunto de evidências centrais.

Gráfico 5. Cobertura temática e densidade de evidência central por achado

Fonte. Elaboração própria com base no corpus analítico.

A predominância do primeiro achado reflete a atenção dedicada a métricas, benchmarks, factualidade, alucinação, robustez, segurança e validação. Apesar dessa cobertura, a literatura permanece fragmentada na conversão dos riscos de modelos fundacionais em protocolos uniformes de avaliação e critérios de aceitação para sistemas conversacionais em produção (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022).

Em sistemas baseados em LLMs, métricas tradicionais de desempenho são insuficientes para avaliar governança. Acurácia, cobertura de intenção, taxa de resposta correta ou satisfação do usuário não capturam integralmente riscos como respostas não rastreáveis, uso de fontes inadequadas, ausência de escalonamento, opacidade decisória, violação de política institucional ou falha em comunicar incerteza. A avaliação precisa incorporar dimensões como factualidade, segurança, robustez, rastreabilidade, consistência, explicabilidade, privacidade, aderência ao domínio e capacidade de recusa.

Outro ponto crítico é a qualidade metodológica dos estudos. Parte da literatura é conceitual, normativa ou técnica, enquanto outra parte é empírica, experimental ou aplicada a domínios específicos. Essa heterogeneidade dificulta comparações diretas e exige instrumentos flexíveis de avaliação crítica. O uso combinado de appraisal metodológico, análise temática e avaliação de confiança das evidências permite diferenciar estudos com forte suporte empírico, contribuições conceituais fundacionais e propostas técnicas ainda pouco validadas.

A diferença entre referências normativas à supervisão e mecanismos operacionais explícitos indica que accountability, oversight e controle humano são frequentemente defendidos sem detalhamento equivalente sobre atores, autoridade, evidências e responsabilidades.

Essa lacuna é especialmente importante em sistemas conversacionais. Em uma interface baseada em linguagem natural, a supervisão humana não ocorre apenas no treinamento ou na validação do modelo. Ela pode ocorrer durante o atendimento, em fluxos de escalonamento, na revisão de respostas sensíveis, na curadoria de bases de conhecimento, na análise de incidentes e na atualização de políticas. A governança conversacional exige, portanto, uma arquitetura de supervisão distribuída ao longo do ciclo de vida do sistema.

A accountability operacional depende da transformação da supervisão humana em processo institucional. Isso envolve definir papéis, critérios de escalonamento, níveis de risco, evidências exigidas para revisão, mecanismos de contestação, responsabilidades de equipes e consequências de falhas. Sem essa estrutura, a supervisão humana pode se tornar uma salvaguarda apenas declaratória, incapaz de produzir prestação de contas real.

Observabilidade, auditoria e monitoramento pós-implantação foram identificados em 276 estudos (77,1% do corpus), dos quais 23 centrais e 253 de apoio. Os estudos abordam auditoria, logs, tracing, telemetria, documentação, monitoramento contínuo e investigação de incidentes ao longo do ciclo de vida.

Observabilidade não deve ser tratada apenas como capacidade técnica de monitoramento. Ela é uma condição para investigação, aprendizagem e responsabilização. Sem logs e tracing adequados, torna-se difícil reconstruir por que determinada resposta foi produzida, quais fontes foram usadas, quais regras foram aplicadas, se houve tentativa de escalonamento e quais componentes contribuíram para a falha.

A comparação com a camada evolutiva mostra que monitoramento é tratado sobretudo como rastreabilidade ou conformidade e menos como processo sistemático de aprendizagem, atualização e adaptação após incidentes.

Conhecimento, RAG e guardrails foram associados a 160 estudos, incluindo 14 evidências centrais. A família mais estrita de governança do conhecimento apareceu em 44, mostrando que trabalhos sobre RAG ou guardrails nem sempre abordam curadoria, proveniência, validade, autoridade e versionamento das fontes.

Esse achado desloca parte da governança do modelo para a governança da informação. Em ambientes regulados, bases de conhecimento precisam ter autoria, versão, validade, data de atualização, escopo, fonte autorizada e critérios de uso. Uma resposta conversacional incorreta pode decorrer de falha do modelo, mas também de documento desatualizado, fonte inadequada, chunk mal segmentado, recuperação irrelevante ou ausência de regra de prioridade entre fontes.

A oportunidade de pesquisa está em desenvolver modelos de governança que integrem RAG, curadoria de conhecimento, guardrails e supervisão humana. Essa integração deve contemplar tanto a qualidade da informação quanto a qualidade da interação. Em sistemas conversacionais, não basta recuperar a fonte correta; é necessário apresentar a resposta de modo adequado ao risco, ao perfil do usuário, ao grau de incerteza e às responsabilidades institucionais envolvidas.

Confiança, explicabilidade e orientação ao usuário foram identificadas em 278 estudos (77,7% do corpus), incluindo 17 evidências centrais e 261 de apoio. A ampla presença de transparência e comunicação de limites contrasta com a baixa incidência de mecanismos que permitem contestar ou reparar uma resposta.

Isso implica diferenciar explicabilidade interna, voltada a desenvolvedores e auditores, de explicabilidade orientada ao usuário, voltada a compreensão, contestação e reparo. A primeira pode envolver logs, métricas, traces, documentos técnicos e análise de componentes. A segunda precisa aparecer como resposta compreensível, indicação de fonte, aviso de incerteza, justificativa de recusa, explicitação de limite ou encaminhamento para suporte humano.

A análise revela uma assimetria substantiva: a literatura privilegia mecanismos que informam o usuário sobre capacidades e limites, mas oferece menor cobertura para aqueles que permitem agir sobre uma resposta inadequada, obter revisão ou buscar reparação.

Contestabilidade e reparo são extensões práticas da explicabilidade. Uma explicação que não permite ação posterior pode ter valor limitado em ambientes regulados. A governança conversacional deve permitir que usuários questionem respostas, solicitem revisão, corrijam informações, acionem suporte humano e compreendam os caminhos disponíveis para contestação. Essa dimensão aproxima governança, UX conversacional e accountability.

## 4.6. Síntese dos achados

A síntese integra os resultados em uma configuração desigual: controles que estabilizam modelos e responsabilidades institucionais estão mais consolidados que capacidades manifestadas no diálogo e na aprendizagem pós-incidente. Essa diferença orienta o modelo, mas não implica sequência linear ou escala de maturidade.

A concentração da literatura em saúde e medicina, responsável por 41,9% do corpus e por 19 das 30 evidências centrais, limita a transferência direta dos achados. Finanças, educação, jurídico, governo e infraestrutura crítica têm menor presença de evidências centrais e exigem validação própria.

As capacidades identificadas não funcionam de forma isolada. RAG sem curadoria pode amplificar informação inadequada; guardrails sem monitoramento podem falhar silenciosamente; supervisão humana sem papéis definidos pode se tornar simbólica; logs sem processo de auditoria podem não gerar accountability; e explicabilidade sem um mecanismo de ação do usuário pode não produzir correção. A contribuição analítica da revisão está em demonstrar que a governança depende da integração das cinco dimensões, e não da presença isolada de controles.

Para examinar como os mecanismos se distribuem entre as cinco camadas, foi calculada a coocorrência dos códigos no nível do estudo. O Gráfico 6 apresenta a quantidade de estudos simultaneamente associados a cada família de mecanismos e a cada camada conceitual.

Gráfico 6. Coocorrência entre famílias de mecanismos e camadas de governança

Fonte. Elaboração própria com base nos códigos normalizados do corpus analítico.

As maiores coocorrências ligam compliance e gestão de risco às camadas regulatória e organizacional; accountability e auditoria também se concentram nessas dimensões. A incidência residual de contestabilidade e reparo evidencia que cobertura institucional e técnica não implica, automaticamente, capacidade de ação do usuário.

## 4.7. Modelo de cinco camadas

Com base nos achados da revisão, esta seção propõe um Modelo Conceitual Integrado de Governança Conversacional para sistemas baseados em LLMs implantados em ambientes regulados. O modelo organiza a governança conversacional como uma configuração sociotécnica composta por cinco camadas interdependentes: técnica, interacional, organizacional, regulatória e evolutiva.

A proposição parte do reconhecimento de que sistemas baseados em LLMs não são governados apenas pelo modelo fundacional. Sua operação envolve prompts, bases de conhecimento, mecanismos de recuperação, ferramentas externas, guardrails, interfaces conversacionais, políticas organizacionais, supervisão humana, registros de auditoria e requisitos regulatórios. Por isso, a governança precisa abranger o sistema conversacional completo, e não apenas o componente algorítmico isolado.

O modelo propõe cinco camadas integradas.

A camada técnica reúne mecanismos de controle, observabilidade e segurança operacional. Inclui RAG, guardrails, logs, tracing, monitoramento, red teaming, avaliação contínua, versionamento e testes de regressão. Essa camada responde à necessidade de tornar o comportamento do sistema observável, avaliável e tecnicamente controlável.

A camada interacional trata da governança que ocorre na relação entre sistema e usuário. Inclui explicação, comunicação de limites, confirmação, handoff, escalonamento, contestação, reparo e orientação sobre próximos passos. Essa camada é necessária porque sistemas conversacionais governam parte da experiência por meio da própria linguagem.

A camada organizacional define papéis, responsabilidades, políticas, processos, documentação e estruturas internas de decisão. Inclui comitês, matriz de responsabilidade, governança do conhecimento, critérios de escalonamento, fluxos de revisão e processos de auditoria interna. Essa camada evita que a responsabilidade fique dispersa entre modelo, fornecedor, produto, operação e área de negócio.

A camada regulatória conecta o sistema a normas, riscos, evidências e deveres setoriais. Inclui compliance, proteção de dados, avaliação de impacto, trilhas de auditoria, critérios de risco, documentação regulatória e alinhamento com obrigações específicas de cada domínio. Essa camada é especialmente relevante em saúde, finanças, governo, jurídico, seguros, educação regulada e telecomunicações.

A camada evolutiva trata da aprendizagem operacional e da adaptação controlada do sistema. Inclui análise de incidentes, feedback loops, atualização de bases de conhecimento, revisão de prompts, ajustes de guardrails, melhoria contínua e monitoramento pós-implantação. Essa camada reconhece que a governança não termina na implantação; ela precisa acompanhar o comportamento real do sistema em uso.

A integração dos resultados quantitativos e temáticos permitiu organizar os mecanismos em um modelo sistêmico. A Figura 1 representa as cinco camadas como dimensões interdependentes que atuam sobre o sistema conversacional completo, incluindo modelo, resposta, interação, conhecimento, organização e ambiente regulatório.

Figura 1. Modelo Conceitual Integrado de Governança Conversacional

Nota. As setas representam dependência recíproca e retroalimentação, e não uma sequência temporal rígida.

Fonte. Elaboração própria a partir da síntese da revisão.

A figura evidencia que nenhuma camada produz governança de forma autônoma. A camada regulatória define requisitos e limites; a organizacional os traduz em responsabilidades e processos; a técnica implementa controles e registros; a interacional manifesta a governança no diálogo; e a evolutiva transforma incidentes, uso e feedback em adaptação controlada.

O modelo não deve ser interpretado como uma sequência linear rígida. As camadas operam de forma interdependente. Um mecanismo técnico, como RAG, depende de governança organizacional da base de conhecimento e pode estar sujeito a requisitos regulatórios de rastreabilidade. Um mecanismo interacional, como handoff, depende de critérios técnicos de detecção de risco e de processos organizacionais de atendimento. Uma auditoria regulatória depende de logs técnicos, documentação organizacional e evidências de interação.

Essa interdependência indica que governança conversacional é uma capacidade sistêmica. Ela exige coordenação entre tecnologia, design conversacional, operação, risco, compliance, jurídico, segurança, dados e áreas de negócio.

Em ambientes regulados, o modelo deve ser aplicado de modo proporcional ao risco da interação. Interações informacionais simples podem demandar controles básicos, como logs, limites de escopo e atualização da base de conhecimento. Interações que envolvem orientação clínica, financeira, jurídica, administrativa ou de acesso a direitos exigem controles mais robustos, incluindo explicação, rastreabilidade de fontes, supervisão humana, contestabilidade, auditoria e documentação regulatória.

A principal contribuição do modelo é integrar dimensões que aparecem fragmentadas na literatura. A governança de IA oferece princípios e frameworks de risco. A accountability algorítmica oferece uma teoria de responsabilização. A literatura de LLMs descreve riscos técnicos e sociais. A interação humano-IA oferece diretrizes para transparência, confiança e correção. A literatura regulatória define obrigações setoriais e critérios de conformidade. O modelo proposto articula essas contribuições em torno da unidade de análise conversacional.

A governança conversacional é, portanto, definida neste estudo como o conjunto de mecanismos técnicos, interacionais, organizacionais, regulatórios e evolutivos que orientam, controlam, monitoram, justificam e corrigem o comportamento de sistemas baseados em LLMs em interações mediadas por linguagem natural, especialmente quando tais sistemas operam em ambientes regulados ou de alto impacto.

Essa definição amplia a noção de governança para além do controle do modelo. Ela inclui a governança da resposta, da interação, da fonte de conhecimento, do escalonamento, do reparo, da evidência, da responsabilidade e da aprendizagem operacional. Com isso, o modelo oferece uma base para análise de sistemas existentes, desenho de novos sistemas, auditoria de aplicações em produção e desenvolvimento de agendas de pesquisa empírica.

Para converter o modelo conceitual em instrumento de análise organizacional, a Tabela 3 apresenta perguntas verificáveis associadas às camadas e aos controles esperados.

Tabela 3. Perguntas operacionais e exemplos de evidência de controle

Nota. As perguntas sintetizam evidências recorrentes; sua organização em cinco camadas e seu uso como estrutura diagnóstica são proposições do modelo, ainda sujeitas a validação empírica. A aplicação deve ser calibrada conforme risco, setor e autonomia do sistema.

Fonte. Elaboração própria com base no Modelo Conceitual Integrado.

A tabela traduz as cinco camadas em critérios que podem orientar revisão de arquitetura, avaliação de risco, auditoria, desenho de interação e monitoramento pós-implantação. Sua aplicação não substitui requisitos regulatórios específicos, mas oferece uma estrutura comum para organizar evidências e responsabilidades.

Quanto ao estatuto epistemológico do modelo, este artigo apresenta uma primeira proposição conceitual derivada da síntese sistemática da literatura. As cinco camadas organizam padrões recorrentes identificados no corpus. O modelo não é uma escala de maturidade, norma, certificação ou requisito regulatório, nem substitui normas setoriais; sua validade externa e utilidade operacional dependem de estudos de caso, avaliações com especialistas e aplicações em sistemas reais de ambientes regulados.

## 5. Discussão

O desbalanceamento observado sugere que a institucionalização de Responsible AI ainda privilegia controles formalizáveis e responsabilidades internas, enquanto o poder de ação do usuário e a aprendizagem após falhas permanecem menos operacionalizados. Isso converge com a crítica de que princípios, embora consolidados, não garantem implementação responsável sem mecanismos institucionais e operacionais (Floridi et al., 2018; Jobin et al., 2019; Mittelstadt, 2019).

Os riscos atribuídos a modelos fundacionais - opacidade, alucinação, viés, conteúdo nocivo e dificuldade de avaliação - explicam a centralidade de guardrails, testes e observabilidade (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022). A revisão também mostra, contudo, que controles do modelo não bastam. RAG transfere parte do risco para curadoria, proveniência e atualização das fontes; logs só geram governança quando alimentam auditoria; e monitoramento só produz aprendizagem quando incidentes resultam em mudança controlada (Gao et al., 2023).

A predominância das camadas regulatória e organizacional reforça a natureza distribuída da accountability. Explicar e justificar condutas exige atores, instâncias de avaliação e consequências identificáveis (Bovens, 2007), enquanto a responsabilização algorítmica pode incidir sobre dados, modelos, decisões, efeitos e instituições (Wieringa, 2020). Para sistemas conversacionais, a cadeia relevante inclui ainda prompts, bases recuperadas, ferramentas, políticas e intervenção humana. O modelo proposto aproxima essa cadeia da auditoria de ciclo de vida defendida por Raji et al. (2020), conectando evidências técnicas a responsabilidades organizacionais.

A literatura de interação humano-IA ajuda a interpretar essa lacuna: usuários precisam compreender capacidades e limites e dispor de meios efetivos de correção (Amershi et al., 2019; Shneiderman, 2020). Como a fluência linguística pode elevar confiança sem elevar competência, explicabilidade orientada ao usuário deve permitir ação posterior - corrigir informações, solicitar revisão ou acionar suporte humano - e não apenas apresentar uma justificativa (Luger & Sellen, 2016; Rapp et al., 2021).

Essa distinção delimita a contribuição: os mecanismos e padrões de incidência derivam do corpus, enquanto o arranjo entre eles é uma síntese integradora. Sua utilidade está em tornar explícitas dependências dispersas e formular categorias verificáveis para estudos empíricos, auditorias e desenho organizacional, sem antecipar efetividade ainda não demonstrada.

A aplicação do modelo envolve trade-offs. Observabilidade amplia rastreabilidade, mas deve respeitar privacidade e minimização de dados; transparência pode favorecer confiança calibrada, mas não deve expor controles de segurança; supervisão humana reduz riscos apenas quando há autoridade, capacidade e tempo, podendo criar gargalos ou salvaguardas simbólicas; e padronização facilita auditoria, mas não elimina a necessidade de calibração por domínio. Esses conflitos impedem que uma camada seja maximizada isoladamente e reforçam a aplicação proporcional ao risco.

Em saúde, interações clínicas exigem fontes validadas, supervisão profissional e escalonamento; em finanças, destacam-se rastreabilidade, prevenção de aconselhamento indevido e contestação; em governo, legitimidade, acesso a direitos e canais de recurso; e, em jurídico, seguros e educação regulada, a distinção entre informação, recomendação e decisão. O NIST AI RMF e o AI Act europeu sustentam uma abordagem baseada em risco, mas a tradução para a conversa depende do contexto e das obrigações de cada setor (National Institute of Standards and Technology, 2023; European Parliament & Council of the European Union, 2024).

A generalização deve ser cautelosa diante da concentração setorial e da heterogeneidade de estudos empíricos, conceituais, normativos e técnicos. Mecanismos de ordenação, indexação e disponibilidade podem influenciar a recuperação; a combinação de múltiplas fontes, análise de posições posteriores, rastreamento bibliográfico e deduplicação reduz essa dependência, mas não demonstra exaustividade. A revisão por pesquisador único e a adjudicação assistida podem introduzir erro de classificação ou enquadramento. Validação literal, consulta ao texto integral e registro das decisões reduzem esses riscos, sem equivaler a dupla codificação independente.

Pesquisas futuras devem validar o modelo em organizações e setores distintos, comparar arranjos de supervisão, testar guardrails e RAG em produção e desenvolver métricas para ação do usuário e aprendizagem operacional. Estudos longitudinais podem examinar se logs, incidentes e feedback resultam em melhoria controlada. Essa validação deve combinar desempenho, análise de processos, experiência do usuário, incidentes e evidências de conformidade, distinguindo a presença formal de controles de sua efetividade.

## 6. Conclusão

A revisão responde às questões de pesquisa ao mostrar que a governança conversacional depende da coordenação entre controles técnicos, desenho da interação, responsabilidades organizacionais, obrigações regulatórias e aprendizagem operacional. O problema central não é apenas controlar o modelo, mas governar o sistema sociotécnico que produz, apresenta, registra e corrige respostas.

O Modelo Conceitual Integrado organiza essa evidência em cinco camadas interdependentes: técnica, interacional, organizacional, regulatória e evolutiva. Sua contribuição teórica é deslocar a unidade de análise do modelo isolado para o sistema conversacional; sua contribuição prática é oferecer categorias verificáveis para arquitetura, supervisão, auditoria, ação do usuário e mudança controlada.

A interpretação deve considerar a concentração setorial, a heterogeneidade dos estudos e as limitações da recuperação e da adjudicação assistida. O modelo é uma proposição ainda não validada empiricamente e não substitui obrigações setoriais. Estudos futuros devem aplicá-lo em organizações distintas, comparar arranjos de supervisão e testar se guardrails, RAG, observabilidade, revisão humana e aprendizagem após incidentes produzem controle e accountability verificáveis em operação.

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

| ID | Família | Blocos conceituais principais |
| --- | --- | --- |
| A | Governança de LLMs | LLMs e IA generativa combinados a governança, accountability, compliance, auditoria e risco |
| B | LLMOps e observabilidade | LLMOps, observabilidade, monitoramento e guardrails combinados a governança e compliance |
| C | Governança conversacional | IA conversacional, chatbots e agentes combinados a LLMs, governança e supervisão humana |
| D | Ambientes regulados | LLMs e IA generativa combinados a setores regulados, risco, auditoria e conformidade |
| E | Supervisão humana e contestabilidade | Supervisão humana, human-in-the-loop, contestabilidade e escalonamento combinados a LLMs e chatbots |

## Tabela 2

| Código | Tipo | Critério |
| --- | --- | --- |
| I1 | Inclusão | Objeto e mecanismo: LLM, IA generativa ou sistema conversacional com mecanismo de governança identificável. |
| I2 | Inclusão | Contexto: aplicação em ambiente regulado ou de alto impacto, ou transferibilidade demonstrável para esse contexto. |
| I3 | Inclusão | Evidência: texto completo suficiente, publicado entre 2020 e 2026; estudos anteriores somente quando fundacionais. |
| I4 | Inclusão | Desenho aderente: estudo empírico, técnico, conceitual, normativo ou revisão com evidência substantiva. |
| E1 | Exclusão | Escopo incompatível: ausência do sistema relevante ou de mecanismo de governança. |
| E2 | Exclusão | Contexto insuficiente: sem aplicação, implicação ou transferibilidade para ambiente regulado ou de alto impacto. |
| E3 | Exclusão | Evidência insuficiente: texto ou metadados inadequados para responder às questões da revisão. |
| E4 | Exclusão | Redundância ou função inadequada: duplicata, versão redundante, manuscrito interno ou pré-2020 sem função fundacional. |

## Tabela 3

| Pergunta de governança | Camada mais diretamente envolvida | Evidência ou controle verificável |
| --- | --- | --- |
| O sistema usa fontes autorizadas e atualizadas? | Técnica e organizacional | Base RAG versionada, fonte validada, data de atualização |
| A resposta pode ser reconstruída depois? | Técnica e regulatória | Logs, traces, prompt, fonte recuperada, resposta final |
| O usuário sabe quando o sistema tem limitações? | Interacional | Aviso de incerteza, explicação, recusa justificada |
| Há caminho para contestar ou corrigir uma resposta? | Interacional e organizacional | Recurso, feedback, revisão humana, protocolo de reparo |
| Quem é responsável por uma falha? | Organizacional | Matriz de responsabilidade, papéis, processo de incidentes |
| O sistema atende requisitos de risco e compliance? | Regulatória | Avaliação de impacto, controles documentados, auditoria |
| O sistema melhora após incidentes? | Evolutiva | Análise de incidente, revisão de base, ajuste de prompt, novo teste |
