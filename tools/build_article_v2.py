"""Aplica as correções metodológicas da v2 sobre a v1, preservando figuras e referências."""
from pathlib import Path
import sys
from docx import Document

TRACE = ("Os 177 estudos do corpus analítico estão identificados individualmente no inventário "
         "suplementar, por identificador estável, referência bibliográfica e arquivo de origem. "
         "As contagens apresentadas nas tabelas e figuras podem ser auditadas a partir desse inventário.")

STATUS = ("O Modelo Conceitual Integrado é uma proposição analítica derivada da síntese dos estudos. "
          "Ele não é uma escala de maturidade, norma, certificação ou requisito regulatório, nem substitui "
          "normas setoriais. Sua validade externa e efetividade ainda dependem de validação empírica em "
          "organizações, sistemas reais e diferentes ambientes regulados.")

THREATS = ("Ameaças à abrangência da recuperação. O limite de até 25 resultados por combinação entre estratégia "
           "e fonte pode sub-representar consultas produtivas. Restrições de taxa do Semantic Scholar e falhas "
           "de tempo de resposta do arXiv produziram cobertura parcial. APIs e ordenações podem privilegiar "
           "relevância, recência ou popularidade. A expansão por referências, citações, autoria e veículo reduz, "
           "mas não elimina, o risco de estudos não recuperados. Assim, os resultados devem ser lidos como síntese "
           "sistemática de um corpus documentado, não como enumeração exaustiva de toda a literatura.")

LLM_LIMITS = ("A adjudicação assistida por LLM foi um instrumento auxiliar, não um avaliador autônomo. O modelo "
              "recebeu metadados e trechos selecionados, produziu campos estruturados e foi instruído a não inferir "
              "informação ausente. Evidências foram confrontadas literalmente com o texto extraído; casos sem "
              "correspondência exigiram atenção. Não houve revisão humana independente em duplicata. Persistem riscos "
              "de interpretação, alucinação, erro de extração, dependência de versão e configuração do modelo. "
              "A confiança numérica não deve ser lida como probabilidade calibrada nem como substituto de julgamento humano.")

def replace_once(doc, old, new):
    for p in doc.paragraphs:
        if old in p.text:
            for r in p.runs:
                r.text = ''
            p.runs[0].text = new if p.runs else new
            return True
    return False

def build(source: Path, target: Path):
    doc = Document(source)
    # Strengthen methodological positioning without changing corpus numbers.
    replace_once(doc, 'O processo não correspondeu a revisão humana independente em duplicata; essa condição é tratada como limitação.',
                 'A adjudicação assistida por LLM foi um instrumento auxiliar, não um avaliador autônomo. O processo não correspondeu a revisão humana independente em duplicata; essa condição é tratada como limitação.')
    replace_once(doc, 'Semantic Scholar e arXiv tiveram cobertura parcial por limitações de taxa e tempo de resposta.',
                 'Semantic Scholar e arXiv tiveram cobertura parcial por limitações de taxa e tempo de resposta. A cobertura operacional não equivale a exaustividade bibliográfica.')
    # Insert traceability and epistemic status immediately before Discussion.
    for i, p in enumerate(doc.paragraphs):
        if p.text.strip() == '5. Discussão':
            p.insert_paragraph_before(TRACE)
            q = p.insert_paragraph_before('Status epistemológico do modelo')
            q.style = 'Heading 2'
            p.insert_paragraph_before(STATUS)
            p.insert_paragraph_before(LLM_LIMITS)
            p.insert_paragraph_before(THREATS)
            break
    doc.core_properties.title = 'Governança Conversacional em Sistemas Baseados em LLMs - v2'
    doc.core_properties.subject = 'Versão metodologicamente revisada após novo parecer editorial'
    doc.core_properties.comments = 'Derivada da v1; corpus, resultados e invariantes factuais preservados.'
    doc.save(target)

if __name__ == '__main__':
    build(Path(sys.argv[1]), Path(sys.argv[2]))
