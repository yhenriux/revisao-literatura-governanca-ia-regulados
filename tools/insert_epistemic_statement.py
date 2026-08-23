"""Replaces the model-status paragraph in the v2.1 DOCX deliverables."""
from pathlib import Path
import sys
from docx import Document

TEXT = (
    "Este artigo apresenta uma primeira proposição conceitual derivada da síntese sistemática da literatura. "
    "As cinco camadas organizam padrões recorrentes identificados no corpus, mas sua presença nas publicações "
    "analisadas não constitui validação empírica do modelo. O modelo não pretende funcionar como escala de "
    "maturidade, norma ou certificação; sua validade externa e utilidade operacional ainda deverão ser examinadas "
    "em estudos de caso, avaliações com especialistas e aplicações em sistemas reais de ambientes regulados."
)

def update(path: Path) -> None:
    doc = Document(path)
    for p in doc.paragraphs:
        if p.text.startswith("O Modelo Conceitual Integrado é uma proposição analítica derivada"):
            p.text = TEXT
            doc.save(path)
            return
    raise RuntimeError(f"parágrafo do status epistemológico não encontrado: {path}")

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        update(Path(arg))
