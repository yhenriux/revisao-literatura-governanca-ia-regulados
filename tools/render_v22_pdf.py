"""Deterministic PDF renderer for the PDF-first v2.2 manuscript."""
from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path.cwd()
SOURCE = ROOT / "Artigo/texto_exportado/Artigo_v2.2_para_editar.md"
OUTPUT = ROOT / "Artigo/Artigo_v2.2_final.pdf"
IMAGE_ROOT = ROOT / "Recursos_do_artigo/v2.2/imagens"
IMAGES = {
    "Figure 1": "Grafico_1_composicao_do_corpus.png",
    "Figure 2": "Grafico_2_familias_de_mecanismos.png",
    "Figure 3": "Grafico_3_camadas_do_modelo.png",
    "Figure 4": "Grafico_4_distribuicao_setorial.png",
    "Figure 5": "Grafico_5_cobertura_dos_achados.png",
    "Figure 6": "Grafico_6_coocorrencia_mecanismos_camadas.png",
    "Figure 7": "Figura_1_modelo_de_cinco_camadas.png",
}


def esc(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*", r"<i>\1</i>", text)
    return text.replace("[^1]", "<super>1</super>")


def fs(path: Path) -> str:
    """Use Windows long-path syntax because this workspace exceeds MAX_PATH."""
    value = str(path.resolve())
    return value if value.startswith("\\\\?\\") else "\\\\?\\" + value


def parse_table(lines: list[str]) -> list[list[str]]:
    rows = []
    for line in lines:
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def table_flow(rows: list[list[str]], styles: dict[str, ParagraphStyle]):
    widths = [170 * mm, 0, 0]
    col_count = len(rows[0])
    if col_count == 3:
        widths = [20 * mm, 45 * mm, 105 * mm]
    data = [[Paragraph(esc(cell), styles["table_head"] if r == 0 else styles["table_cell"]) for cell in row] for r, row in enumerate(rows)]
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAF0F4")),
        ("LINEABOVE", (0, 0), (-1, 0), 0.7, colors.HexColor("#637789")),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, colors.HexColor("#B6C4CD")),
        ("LINEBELOW", (0, 1), (-1, -1), 0.25, colors.HexColor("#D6DEE5")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3.5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
    ]))
    return table


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#58677A"))
    canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, str(doc.page))
    canvas.restoreState()


def build() -> None:
    with open(fs(SOURCE), encoding="utf-8") as handle:
        text = handle.read()
    lines = text.splitlines()
    tables: dict[int, list[list[str]]] = {}
    for number in range(1, 4):
        marker = f"## Table {number}"
        start = lines.index(marker)
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## Table ") or lines[i].startswith("## References")), len(lines))
        tables[number] = parse_table(lines[start + 1:end])

    styles0 = getSampleStyleSheet()
    styles = {
        "title": ParagraphStyle("title", parent=styles0["Title"], fontName="Helvetica-Bold", fontSize=16, leading=19, alignment=TA_CENTER, spaceAfter=10),
        "h2": ParagraphStyle("h2", parent=styles0["Heading2"], fontName="Helvetica-Bold", fontSize=11.4, leading=14, textColor=colors.HexColor("#172033"), spaceBefore=9, spaceAfter=4),
        "h3": ParagraphStyle("h3", parent=styles0["Heading3"], fontName="Helvetica-Bold", fontSize=9.8, leading=12, spaceBefore=6, spaceAfter=3),
        "body": ParagraphStyle("body", parent=styles0["BodyText"], fontName="Helvetica", fontSize=8.7, leading=11.2, alignment=TA_JUSTIFY, spaceAfter=4),
        "note": ParagraphStyle("note", parent=styles0["BodyText"], fontName="Helvetica-Oblique", fontSize=7.7, leading=9.2, alignment=TA_LEFT, spaceAfter=2),
        "source": ParagraphStyle("source", parent=styles0["BodyText"], fontName="Helvetica", fontSize=7.7, leading=9.2, alignment=TA_LEFT, spaceAfter=3),
        "reference": ParagraphStyle("reference", parent=styles0["BodyText"], fontName="Helvetica", fontSize=7.35, leading=8.75, leftIndent=10 * mm, firstLineIndent=-10 * mm, spaceAfter=1.2),
        "table_head": ParagraphStyle("table_head", parent=styles0["BodyText"], fontName="Helvetica-Bold", fontSize=7.5, leading=8.6),
        "table_cell": ParagraphStyle("table_cell", parent=styles0["BodyText"], fontName="Helvetica", fontSize=7.4, leading=8.5),
        "footnote": ParagraphStyle("footnote", parent=styles0["BodyText"], fontName="Helvetica", fontSize=7.2, leading=8.6, leftIndent=4 * mm, firstLineIndent=-4 * mm, spaceAfter=3),
    }
    story=[]
    i=0
    in_refs=False
    while i < len(lines):
        raw=lines[i].strip()
        if not raw:
            i+=1; continue
        if raw.startswith("## Table "):
            break
        if raw.startswith("# "):
            story.append(Paragraph(esc(raw[2:]), styles["title"])); i+=1; continue
        if raw.startswith("## "):
            heading=raw[3:]
            in_refs=heading == "References"
            story.append(Paragraph(esc(heading), styles["h2"])); i+=1; continue
        mtable=re.match(r"\*\*Table ([1-3])\.",raw)
        if mtable:
            number=int(mtable.group(1)); story.append(Paragraph(esc(raw), styles["h3"])); story.append(table_flow(tables[number],styles)); story.append(Spacer(1,2)); i+=1;continue
        mfig=re.match(r"\*\*(Figure [1-7])\.",raw)
        if mfig:
            label=mfig.group(1)
            caption = Paragraph(esc(raw), styles["h3"])
            img=Image(fs(IMAGE_ROOT / IMAGES[label]))
            img._restrictSize(165*mm,84*mm)
            # Keep each figure caption with its image; a caption must not be left
            # alone at the end of a page.
            story.append(KeepTogether([caption, img, Spacer(1, 2)]))
            i+=1;continue
        if raw.startswith("Note."):
            story.append(Paragraph(esc(raw),styles["note"]));i+=1;continue
        if raw.startswith("Source."):
            story.append(Paragraph(esc(raw),styles["source"]));i+=1;continue
        if raw.startswith("[^1]:"):
            story.append(Paragraph(esc("1. " + raw[5:].strip()), styles["footnote"])); i+=1;continue
        block=[raw];i+=1
        while i < len(lines):
            nxt=lines[i].strip()
            if not nxt or nxt.startswith("#") or nxt.startswith("**Table ") or nxt.startswith("**Figure ") or nxt.startswith("Note.") or nxt.startswith("Source.") or nxt.startswith("[^1]:"):
                break
            block.append(nxt);i+=1
        story.append(Paragraph(esc(" ".join(block)), styles["reference"] if in_refs else styles["body"]))

    doc=SimpleDocTemplate(fs(OUTPUT),pagesize=A4,leftMargin=20*mm,rightMargin=18*mm,topMargin=17*mm,bottomMargin=17*mm,title="Conversational Governance in LLM-Based Systems in Regulated Environments")
    doc.build(story,onFirstPage=add_page_number,onLaterPages=add_page_number)
    print(OUTPUT)


if __name__ == "__main__":
    build()
