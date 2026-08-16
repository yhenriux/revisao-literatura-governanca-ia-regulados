"""Cria uma redline DOCX real entre duas versões do mesmo manuscrito.

O pacote final é usado como base; blocos alterados recebem parágrafos de
exclusão e inserção rastreadas. Tabelas e desenhos não alterados permanecem
idênticos ao documento final.
"""

from __future__ import annotations

import copy
import difflib
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W, "r": R}


def qn(local: str) -> str:
    return f"{{{W}}}{local}"


def text_of(node) -> str:
    values = node.xpath(".//w:t/text() | .//w:delText/text()", namespaces=NS)
    return "".join(values)


def signature(node) -> str:
    if node.tag == qn("tbl"):
        return "[[TABLE]]" + text_of(node)
    embeds = node.xpath(".//@r:embed", namespaces=NS)
    if embeds:
        return "[[DRAWING]]" + "|".join(embeds)
    return "[[P]]" + text_of(node)


def tracked_paragraph(node, kind: str, change_id: int, author: str, when: str):
    paragraph = copy.deepcopy(node)
    ppr = paragraph.find(qn("pPr"))
    visible = text_of(paragraph)
    for child in list(paragraph):
        if child is not ppr:
            paragraph.remove(child)

    wrapper = etree.Element(qn(kind))
    wrapper.set(qn("id"), str(change_id))
    wrapper.set(qn("author"), author)
    wrapper.set(qn("date"), when)
    run = etree.SubElement(wrapper, qn("r"))
    text_tag = "delText" if kind == "del" else "t"
    text_node = etree.SubElement(run, qn(text_tag))
    text_node.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    text_node.text = visible
    paragraph.append(wrapper)
    return paragraph


def read_xml(docx: Path, member: str):
    with zipfile.ZipFile(docx, "r") as archive:
        return etree.fromstring(archive.read(member))


def build(old_docx: Path, new_docx: Path, out_docx: Path, author: str) -> None:
    old_root = read_xml(old_docx, "word/document.xml")
    new_root = read_xml(new_docx, "word/document.xml")
    old_body = old_root.find(qn("body"))
    new_body = new_root.find(qn("body"))

    old_blocks = [copy.deepcopy(n) for n in old_body if n.tag != qn("sectPr")]
    new_blocks = [copy.deepcopy(n) for n in new_body if n.tag != qn("sectPr")]
    sectpr = copy.deepcopy(new_body.find(qn("sectPr")))

    matcher = difflib.SequenceMatcher(
        a=[signature(n) for n in old_blocks],
        b=[signature(n) for n in new_blocks],
        autojunk=False,
    )
    output = []
    next_id = 1000
    when = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    for opcode, i1, i2, j1, j2 in matcher.get_opcodes():
        if opcode == "equal":
            output.extend(copy.deepcopy(n) for n in new_blocks[j1:j2])
            continue
        for node in old_blocks[i1:i2]:
            if node.tag == qn("p"):
                output.append(tracked_paragraph(node, "del", next_id, author, when))
                next_id += 1
        for node in new_blocks[j1:j2]:
            if node.tag == qn("p"):
                output.append(tracked_paragraph(node, "ins", next_id, author, when))
                next_id += 1
            else:
                output.append(copy.deepcopy(node))

    # Empty terminal paragraphs are visually inert after accepting the changes,
    # but in a long redline they can force an otherwise blank final page.
    while output and output[-1].tag == qn("p") and not text_of(output[-1]).strip():
        output.pop()

    for node in list(new_body):
        new_body.remove(node)
    for node in output:
        new_body.append(node)
    new_body.append(sectpr)

    document_xml = etree.tostring(new_root, xml_declaration=True, encoding="UTF-8", standalone="yes")
    settings_root = read_xml(new_docx, "word/settings.xml")
    if settings_root.find(qn("trackRevisions")) is None:
        settings_root.insert(0, etree.Element(qn("trackRevisions")))
    settings_xml = etree.tostring(settings_root, xml_declaration=True, encoding="UTF-8", standalone="yes")

    with zipfile.ZipFile(new_docx, "r") as source, zipfile.ZipFile(out_docx, "w", zipfile.ZIP_DEFLATED) as target:
        for item in source.infolist():
            if item.filename == "word/document.xml":
                target.writestr(item, document_xml)
            elif item.filename == "word/settings.xml":
                target.writestr(item, settings_xml)
            else:
                target.writestr(item, source.read(item.filename))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("usage: create_tracked_redline.py OLD.docx NEW.docx OUT.docx")
    build(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), "Codex - revisão editorial")
