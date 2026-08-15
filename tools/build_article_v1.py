"""Constrói a v1 a partir da v0, preservando o pacote, estilos e figuras originais."""

from __future__ import annotations

import copy
import sys
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


INTRO = [
    "Modelos de Linguagem de Grande Escala (LLMs) ampliaram o uso de interfaces conversacionais em serviços de saúde, finanças, governo, jurídico, seguros, educação regulada e telecomunicações. A geração aberta de linguagem, a integração com fontes externas e a capacidade de acionar ferramentas aumentam o valor desses sistemas, mas também introduzem riscos de alucinação, opacidade, viés, uso indevido e instabilidade comportamental (Bender et al., 2021; Bommasani et al., 2021; Weidinger et al., 2022).",
    "Em ambientes regulados, uma resposta conversacional pode influenciar orientação clínica, aconselhamento financeiro, acesso a serviços públicos, interpretação jurídica ou exercício de direitos. A governança, portanto, não pode se restringir ao desempenho do modelo: precisa abranger a cadeia que produz a resposta, incluindo prompts, fontes de conhecimento, guardrails, ferramentas, registros, supervisão humana e contexto organizacional.",
    "A literatura oferece bases importantes, porém fragmentadas. Governança de IA e Responsible AI estabelecem princípios; accountability algorítmica trata de justificação, auditoria e responsabilização; estudos de LLMs examinam riscos e avaliação; interação humano-IA investiga confiança, transparência e correção; e trabalhos setoriais enfatizam conformidade e segurança. Falta uma síntese que integre essas perspectivas em mecanismos próprios da interação conversacional.",
    "Esta revisão sistemática identifica e organiza mecanismos técnicos, interacionais, organizacionais, regulatórios e evolutivos que orientam, controlam, monitoram, justificam e corrigem sistemas conversacionais baseados em LLMs em ambientes regulados. As questões de pesquisa examinam os mecanismos relatados, sua relação com risco e accountability, as capacidades associadas, as lacunas metodológicas e setoriais e o papel de explicabilidade, contestabilidade, reparo e aprendizagem operacional.",
    "A principal contribuição é o Modelo Conceitual Integrado de Governança Conversacional, apresentado desde o início como síntese dos resultados. Suas cinco camadas - técnica, interacional, organizacional, regulatória e evolutiva - mostram que governar a conversa requer coordenar controles do sistema, desenho da interação, responsabilidades institucionais, obrigações externas e aprendizagem em produção.",
    "O artigo contribui ao consolidar uma literatura dispersa, organizar os mecanismos em famílias analíticas e propor uma arquitetura conceitual aplicável à pesquisa, à avaliação e à prática organizacional. A narrativa segue do posicionamento da lacuna ao método, aos resultados, ao modelo e às suas implicações.",
]

RELATED = [
    "A literatura relevante converge em cinco vertentes. A primeira, governança de IA e Responsible AI, consolidou princípios como justiça, transparência, privacidade, segurança, robustez e accountability, mas também demonstrou que princípios isolados não garantem implementação responsável (Floridi et al., 2018; Jobin et al., 2019; Mittelstadt, 2019). Frameworks como o NIST AI RMF e o AI Act europeu aproximam esses princípios da gestão de risco, sem detalhar plenamente a governança que ocorre durante a conversa (National Institute of Standards and Technology, 2023; European Parliament & Council of the European Union, 2024).",
    "A segunda vertente trata de accountability, auditoria e explicabilidade. Accountability pressupõe atores capazes de explicar e justificar condutas diante de uma instância avaliadora, com possibilidade de julgamento e consequências (Bovens, 2007). Em sistemas de IA, o objeto dessa responsabilização se distribui entre dados, modelos, decisões, efeitos e instituições, exigindo documentação, rastreabilidade e auditoria ao longo do ciclo de vida (Raji et al., 2020; Wieringa, 2020).",
    "A terceira vertente examina modelos fundacionais e IA generativa. A escala e a generalidade dos LLMs propagam riscos por diferentes aplicações, enquanto respostas plausíveis podem ocultar erros factuais (Bommasani et al., 2021; Ji et al., 2023). RAG, guardrails, avaliação e observabilidade mitigam parte desses riscos, mas transferem novas responsabilidades para fontes, recuperação, integração e operação (Gao et al., 2023).",
    "A quarta vertente, interação humano-IA, mostra que usuários precisam compreender capacidades, limites, incertezas e caminhos de correção (Amershi et al., 2019; Shneiderman, 2020). Em uma interface conversacional, explicação, confirmação, recusa, escalonamento e reparo são simultaneamente escolhas de design e controles de governança; a fluência linguística pode elevar confiança além da competência real do sistema (Luger & Sellen, 2016; Rapp et al., 2021).",
    "A quinta vertente discute a adoção de IA em setores regulados. Saúde, finanças, governo, jurídico e seguros compartilham exigências de segurança, privacidade, auditabilidade, dever de cuidado e contestação, embora variem em risco e obrigação setorial. A lacuna não é ausência de princípios ou controles isolados, mas falta de integração entre o que controla o sistema, governa a interação, atribui responsabilidades, demonstra conformidade e aprende com o uso real. Essa lacuna fundamenta o modelo de cinco camadas.",
]

METHOD = [
    "A revisão seguiu o PRISMA 2020 e recomendações para revisões sistemáticas em engenharia de software, complementadas por snowballing (Kitchenham & Charters, 2007; Page et al., 2021; Wohlin, 2014). O protocolo articulou identificação e consolidação do corpus, avaliação de elegibilidade e qualidade, validação de evidências e síntese temática orientada à construção conceitual.",
    "A busca combinou corpus-semente, consultas automatizadas e expansão bibliográfica. Foram consultadas oito fontes: OpenAlex, Crossref, Semantic Scholar, PubMed, Europe PMC, CORE, arXiv e DOAJ. Cinco famílias de busca cobriram governança de LLMs, LLMOps e observabilidade, governança conversacional, ambientes regulados e supervisão humana/contestabilidade. As strings completas, adaptações por fonte, parâmetros de API, logs e hashes permanecem disponíveis no material suplementar e no repositório do projeto.",
    "As consultas foram executadas em julho de 2026, sem filtros temporais ou linguísticos aplicados diretamente às APIs. O recorte principal de 2020 a 2026 foi aplicado na elegibilidade; trabalhos anteriores foram preservados apenas quando fundacionais. A recuperação foi delimitada a até 25 resultados por combinação entre estratégia e fonte. Semantic Scholar e arXiv tiveram cobertura parcial por limitações de taxa e tempo de resposta.",
    "O snowballing incluiu referências citadas, trabalhos citantes, relacionados e expansões controladas por autoria e veículo. Todos os registros foram consolidados e deduplicados por DOI, título exato e similaridade textual, com validação de grupos potencialmente ambíguos. Após triagem e disponibilidade de texto completo, a busca foi congelada e 407 estudos únicos formaram o universo avaliado.",
    "Os critérios de elegibilidade selecionaram estudos sobre LLMs, IA generativa ou sistemas conversacionais que apresentassem mecanismos de governança e implicação para ambientes regulados ou de alto impacto. A avaliação distinguiu corpus analítico, referências fundacionais/contextuais e exclusões. O corpus analítico reuniu 177 estudos, dos quais 23 constituíram evidências centrais e 154 evidências de apoio; 112 referências foram mantidas para fundamentação e 118 estudos foram excluídos.",
    "A extração de texto completo registrou páginas, qualidade da extração e trechos relevantes, separando referências para reduzir contaminação bibliográfica. Uma triagem determinística em Python identificou termos, páginas e evidências literais. Em seguida, a adjudicação assistida por LLM classificou elegibilidade, qualidade e temas em JSON estruturado, limitada ao texto fornecido. O processo não correspondeu a revisão humana independente em duplicata; essa condição é tratada como limitação.",
    "Para reduzir extrapolações, evidências atribuídas pelo modelo foram verificadas contra o texto extraído. Casos sem correspondência ou em conflito com a decisão receberam atenção na adjudicação. A qualidade foi avaliada por instrumento CASP/JBI adaptado ao desenho dos estudos, e a confiança analítica incorporou dimensões do CERQual (Aromataris et al., 2024; Lewin et al., 2018). Os escores apoiaram priorização e cautela, sem operar como exclusão automática.",
    "A síntese temática identificou mecanismos, domínios e capacidades, normalizados por vocabulário controlado. A unidade de contagem foi o estudo deduplicado. Famílias, camadas e achados foram multirrótulo; por isso, suas frequências podem superar 177. O domínio primário foi mutuamente exclusivo. Somente o corpus analítico alimentou as frequências e o modelo conceitual.",
]

DISCUSSION = [
    "Os resultados mostram uma literatura mais madura em compliance, risco, controles técnicos e avaliação do que em contestabilidade, reparo e aprendizagem operacional. A assimetria sugere que a governança de LLMs ainda é frequentemente concebida como prevenção e documentação, e menos como capacidade de intervenção durante e após a interação.",
    "A predominância das camadas técnica e organizacional confirma a importância de guardrails, avaliação, logs, políticas e responsabilidades. Contudo, esses mecanismos só produzem governança efetiva quando conectados: RAG depende de curadoria e validade das fontes; supervisão humana depende de autoridade e critérios; logs dependem de processos de auditoria; explicações dependem de canais de contestação; e monitoramento depende de aprendizagem e mudança controlada.",
    "O modelo de cinco camadas explicita essa interdependência. Sua contribuição teórica é deslocar a unidade de análise do modelo isolado para o sistema conversacional sociotécnico. Sua contribuição prática é fornecer uma estrutura para revisar arquitetura, interação, responsabilidade, conformidade e operação sem presumir que um controle único seja suficiente.",
    "A concentração de 44,1% do corpus em saúde e medicina limita a generalização setorial. Finanças, governo, jurídico, seguros, telecomunicações e infraestrutura crítica requerem validação própria. Também é necessário distinguir mecanismos relatados, recomendações normativas e controles empiricamente avaliados; incidência temática não equivale a efetividade comprovada.",
    "A revisão possui limitações. A recuperação por API foi delimitada e parcialmente afetada por restrições de algumas fontes. Estudos heterogêneos foram avaliados em um fluxo único assistido por LLM, sem revisores humanos independentes em duplicata. Extração textual e validação literal reduzem, mas não eliminam, erros de classificação e perda de contexto. Essas limitações recomendam cautela na interpretação de frequências e reforçam a necessidade de replicação e validação empírica.",
    "Pesquisas futuras devem testar o modelo em organizações, comparar arranjos de supervisão, avaliar guardrails e RAG em produção, desenvolver métricas de contestabilidade e investigar longitudinalmente incidentes e aprendizagem operacional. A prioridade não é apenas medir se o sistema responde corretamente, mas verificar se suas respostas podem ser controladas, justificadas, auditadas, contestadas e melhoradas.",
]

CONCLUSION = [
    "A revisão demonstra que governança conversacional em ambientes regulados exige coordenação entre mecanismos técnicos, desenho da interação, responsabilidades organizacionais, obrigações regulatórias e aprendizagem operacional. Os achados respondem às questões de pesquisa ao identificar controles recorrentes e, simultaneamente, lacunas em contestabilidade, reparo, maturidade setorial e monitoramento orientado à melhoria.",
    "O Modelo Conceitual Integrado organiza essa evidência em cinco camadas interdependentes: técnica, interacional, organizacional, regulatória e evolutiva. Sua contribuição consiste em ampliar a governança para além do modelo e incluir resposta, fontes de conhecimento, escalonamento, auditoria, contestação e mudança controlada.",
    "Para a prática, o modelo oferece uma estrutura proporcional ao risco para avaliação de arquitetura e operação. Para a pesquisa, oferece categorias que podem ser validadas, comparadas e convertidas em métricas. Estudos futuros devem examinar sua aplicação em diferentes setores e produzir evidência empírica sobre a efetividade dos mecanismos identificados.",
]


def paragraph_from_template(template, text: str, style: str | None = None):
    node = copy.deepcopy(template)
    texts = node.xpath('.//w:t')
    if texts:
        texts[0].text = text
        for item in texts[1:]:
            item.text = ''
    else:
        run = OxmlElement('w:r')
        txt = OxmlElement('w:t')
        txt.text = text
        run.append(txt)
        node.append(run)
    if style:
        ppr = node.find(qn('w:pPr'))
        if ppr is None:
            ppr = OxmlElement('w:pPr')
            node.insert(0, ppr)
        pstyle = ppr.find(qn('w:pStyle'))
        if pstyle is None:
            pstyle = OxmlElement('w:pStyle')
            ppr.insert(0, pstyle)
        pstyle.set(qn('w:val'), style)
    return node


def build(source: Path, target: Path) -> None:
    doc = Document(source)

    # Normalize regular and even-page footers. The v0 package carries an
    # even-page footer whose justified PAGE field drifts during PDF rendering.
    for section in doc.sections:
        for footer in (section.footer, section.even_page_footer):
            paragraph = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
            paragraph.clear()
            ppr = paragraph._p.get_or_add_pPr()
            jc = ppr.find(qn('w:jc'))
            if jc is None:
                jc = OxmlElement('w:jc')
                ppr.append(jc)
            jc.set(qn('w:val'), 'center')
            paragraph.add_run('Página ')
            run = paragraph.add_run()
            begin = OxmlElement('w:fldChar')
            begin.set(qn('w:fldCharType'), 'begin')
            instruction = OxmlElement('w:instrText')
            instruction.set(qn('xml:space'), 'preserve')
            instruction.text = ' PAGE '
            end = OxmlElement('w:fldChar')
            end.set(qn('w:fldCharType'), 'end')
            run._r.extend((begin, instruction, end))
    body = doc.element.body
    original = [copy.deepcopy(el) for el in body.iterchildren() if el.tag != qn('w:sectPr')]
    sectpr = copy.deepcopy(body.sectPr)
    for el in list(body):
        body.remove(el)

    def original_block(number: int):
        return copy.deepcopy(original[number - 1])

    def add_text(text: str, kind: str = 'body'):
        template_number = {'title': 1, 'subtitle': 2, 'label': 3, 'body': 10, 'keywords': 5, 'h1': 9, 'h2': 23}[kind]
        style = {'h1': 'Heading1', 'h2': 'Heading2'}.get(kind)
        body.append(paragraph_from_template(original[template_number - 1], text, style))

    def add_original(numbers):
        for number in numbers:
            body.append(original_block(number))

    add_text('Governança Conversacional em Sistemas Baseados em Modelos de Linguagem de Grande Escala em Ambientes Regulados: uma revisão sistemática da literatura', 'title')
    add_text('Conversational Governance in Large Language Model-Based Systems in Regulated Environments: A Systematic Literature Review', 'subtitle')
    add_text('Resumo', 'label')
    add_text('Esta revisão sistemática investiga mecanismos de governança conversacional em sistemas baseados em LLMs aplicados a ambientes regulados. Orientada pelo PRISMA 2020, avaliou 407 estudos em texto completo e consolidou 177 no corpus analítico, composto por 23 evidências centrais e 154 de apoio; 112 referências foram mantidas como fundacionais ou contextuais e 118 estudos foram excluídos. Os resultados mostram predominância de compliance e gestão de risco (88,7%), controles técnicos e avaliação (61,0%) e accountability e auditoria (54,2%), enquanto contestabilidade e reparo aparecem em 2,8%. A principal contribuição é um modelo integrado de cinco camadas - técnica, interacional, organizacional, regulatória e evolutiva - que desloca a governança do modelo isolado para o sistema conversacional sociotécnico.', 'body')
    add_text('Palavras-chave: governança conversacional; LLMs; ambientes regulados; accountability; auditoria; supervisão humana.', 'keywords')
    add_text('Abstract', 'label')
    add_text('This systematic review investigates conversational governance mechanisms in LLM-based systems deployed in regulated environments. Guided by PRISMA 2020, it assessed 407 full-text studies and consolidated 177 in the analytical corpus, including 23 central and 154 supporting evidence sources; 112 references were retained as foundational or contextual and 118 studies were excluded. Results show a predominance of compliance and risk management (88.7%), technical controls and evaluation (61.0%), and accountability and auditing (54.2%), whereas contestability and repair appear in 2.8%. The main contribution is an integrated five-layer model - technical, interactional, organizational, regulatory, and evolutionary - that shifts governance from the isolated model to the sociotechnical conversational system.', 'body')
    add_text('Keywords: conversational governance; LLMs; regulated environments; accountability; auditing; human oversight.', 'keywords')

    add_text('1. Introdução', 'h1')
    for paragraph in INTRO:
        add_text(paragraph)

    add_text('2. Trabalhos relacionados', 'h1')
    for paragraph in RELATED:
        add_text(paragraph)

    add_text('3. Método', 'h1')
    for paragraph in METHOD[:2]:
        add_text(paragraph)
    add_original(range(69, 73))
    for paragraph in METHOD[2:5]:
        add_text(paragraph)
    add_original(range(109, 113))
    for paragraph in METHOD[5:]:
        add_text(paragraph)
    add_original(range(144, 148))

    add_text('4. Resultados e Modelo Conceitual Integrado', 'h1')
    add_original(range(156, 172))
    add_text('4.1. Mecanismos técnicos e operacionais', 'h2')
    add_original([173, 175, 176, 177, 178, 179, 180])
    add_text('4.2. Supervisão humana, escalonamento e contestabilidade', 'h2')
    add_original([183, 184, 186, 187, 188])
    add_text('4.3. Accountability, auditoria e compliance', 'h2')
    add_original([191, 192, 193, 194, 195, 196])
    add_text('4.4. Aplicações e domínios regulados', 'h2')
    add_original(range(203, 212))
    add_text('4.5. Achados da revisão', 'h2')
    add_original(range(213, 222))
    add_original([223, 224, 226, 228, 229, 231, 234, 235, 237, 240, 241, 243, 245, 246, 248, 249])
    add_text('4.6. Síntese dos achados', 'h2')
    add_original(range(251, 261))
    add_text('4.7. Modelo de cinco camadas', 'h2')
    add_original([268, 269, 276, 277, 278, 279, 280, 281])
    add_original(range(283, 291))
    add_original([292, 293, 295, 299, 300, 301, 302, 303, 304, 305, 306, 307])

    add_text('5. Discussão', 'h1')
    for paragraph in DISCUSSION:
        add_text(paragraph)

    add_text('6. Conclusão', 'h1')
    for paragraph in CONCLUSION:
        add_text(paragraph)

    add_text('Referências', 'h1')
    add_original(range(363, len(original) + 1))

    body.append(sectpr)
    settings = doc.settings.element
    update_fields = settings.find(qn('w:updateFields'))
    if update_fields is None:
        update_fields = OxmlElement('w:updateFields')
        settings.append(update_fields)
    update_fields.set(qn('w:val'), 'true')
    doc.core_properties.title = 'Governança Conversacional em Sistemas Baseados em LLMs - v1'
    doc.core_properties.subject = 'Versão revisada após parecer editorial de Mauricio B. Almeida'
    doc.core_properties.comments = 'Derivada da v0; números e resultados preservados conforme decisão editorial.'
    doc.core_properties.modified = datetime.now(timezone.utc)

    figure_alts = [
        'Fluxo PRISMA com a composição dos 407 estudos avaliados em texto completo.',
        'Gráfico da incidência das famílias de mecanismos e da presença de evidência central.',
        'Gráfico da distribuição dos estudos pelas cinco camadas do modelo conceitual.',
        'Gráfico da composição setorial do corpus analítico.',
        'Gráfico da cobertura temática e da densidade de evidência central por achado.',
        'Mapa de calor da coocorrência entre famílias de mecanismos e camadas de governança.',
        'Modelo conceitual integrado de governança conversacional com cinco camadas interdependentes.',
    ]
    for shape, alt in zip(doc.inline_shapes, figure_alts):
        shape._inline.docPr.set('descr', alt)
        shape._inline.docPr.set('title', alt)
    doc.save(target)


if __name__ == '__main__':
    build(Path(sys.argv[1]), Path(sys.argv[2]))
