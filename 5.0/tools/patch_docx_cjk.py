#!/usr/bin/env python3
"""Patch a Pandoc DOCX so Chinese text uses the East Asian font theme.

Pandoc's DOCX writer uses a shared reference document. Its default language
is English, which makes some readers resolve the theme to a Latin font even
when a run contains Han characters. This script makes the document's East
Asian language explicit and removes the Times New Roman East Asian override
from the legacy Normal (Web) style.
"""

from __future__ import annotations

import argparse
import os
import tempfile
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace("w", W_NS)


def qname(name: str) -> str:
    return f"{{{W_NS}}}{name}"


def patch_styles(data: bytes) -> bytes:
    root = ET.fromstring(data)

    # The document defaults apply to unstyled content and to styles that only
    # specify a Latin font. zh-CN selects the Hans entry in the theme.
    for lang in root.findall(f".//{qname('lang')}"):
        lang.set(qname("eastAsia"), "zh-CN")

    for style in root.findall(qname("style")):
        if style.get(qname("styleId")) != "NormalWeb":
            continue
        fonts = style.find(f".//{qname('rFonts')}")
        if fonts is not None:
            fonts.attrib.pop(qname("eastAsia"), None)
            fonts.set(qname("eastAsiaTheme"), "minorEastAsia")
        lang = style.find(f".//{qname('lang')}")
        if lang is None:
            rpr = style.find(qname("rPr"))
            if rpr is None:
                rpr = ET.SubElement(style, qname("rPr"))
            lang = ET.SubElement(rpr, qname("lang"))
        lang.set(qname("eastAsia"), "zh-CN")

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def patch_settings(data: bytes) -> bytes:
    root = ET.fromstring(data)
    theme_lang = root.find(qname("themeFontLang"))
    if theme_lang is None:
        theme_lang = ET.Element(qname("themeFontLang"))
        root.insert(0, theme_lang)
    theme_lang.set(qname("eastAsia"), "zh-CN")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def patch_docx(source: Path, destination: Path) -> None:
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as temp:
        temp_path = Path(temp.name)
    try:
        with zipfile.ZipFile(source) as input_docx, zipfile.ZipFile(
            temp_path, "w", compression=zipfile.ZIP_DEFLATED
        ) as output_docx:
            for item in input_docx.infolist():
                content = input_docx.read(item.filename)
                if item.filename == "word/styles.xml":
                    content = patch_styles(content)
                elif item.filename == "word/settings.xml":
                    content = patch_settings(content)
                output_docx.writestr(item, content)
        destination.parent.mkdir(parents=True, exist_ok=True)
        os.replace(temp_path, destination)
    finally:
        temp_path.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    patch_docx(args.source, args.destination)


if __name__ == "__main__":
    main()
