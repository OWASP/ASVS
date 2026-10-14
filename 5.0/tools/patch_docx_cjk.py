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
import re
import tempfile
import zipfile
from pathlib import Path


def set_attribute(tag: str, name: str, value: str) -> str:
    attribute = rf'\s{re.escape(name)}="[^"]*"'
    replacement = f' {name}="{value}"'
    if re.search(attribute, tag):
        return re.sub(attribute, replacement, tag)
    return tag[:-2] + replacement + "/>" if tag.endswith("/>") else tag[:-1] + replacement + ">"


def patch_styles(data: bytes) -> bytes:
    text = data.decode("utf-8")

    # The document defaults apply to unstyled content and to styles that only
    # specify a Latin font. zh-CN selects the Hans entry in the theme.
    text = re.sub(r"<w:lang\b[^>]*>", lambda match: set_attribute(match.group(), "w:eastAsia", "zh-CN"), text)

    def patch_normal_web(match: re.Match[str]) -> str:
        style = match.group()

        def patch_fonts(font_match: re.Match[str]) -> str:
            fonts = re.sub(r'\s+w:eastAsia="[^"]*"', "", font_match.group())
            return set_attribute(fonts, "w:eastAsiaTheme", "minorEastAsia")

        return re.sub(r"<w:rFonts\b[^>]*>", patch_fonts, style, count=1)

    text = re.sub(
        r'<w:style\b(?=[^>]*\bw:styleId="NormalWeb")[\s\S]*?</w:style>',
        patch_normal_web,
        text,
        count=1,
    )
    return text.encode("utf-8")


def patch_settings(data: bytes) -> bytes:
    text = data.decode("utf-8")
    if re.search(r"<w:themeFontLang\b", text):
        text = re.sub(
            r"<w:themeFontLang\b[^>]*>",
            lambda match: set_attribute(match.group(), "w:eastAsia", "zh-CN"),
            text,
            count=1,
        )
    else:
        text = re.sub(r"(<w:settings\b[^>]*>)", r'\1<w:themeFontLang w:eastAsia="zh-CN"/>', text, count=1)
    return text.encode("utf-8")


def patch_footer(data: bytes) -> bytes:
    return data.replace(
        b"OWASP Application Security Verification Standard 4.0",
        b"OWASP Application Security Verification Standard 5.0.0",
    )


def patch_docx(source: Path, destination: Path, patch_cjk: bool, patch_footer_text: bool) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Keep the temporary file on the destination filesystem. The document
    # builder writes outputs to a mounted volume, so /tmp may be a different
    # filesystem and cannot be atomically renamed over the destination.
    with tempfile.NamedTemporaryFile(dir=destination.parent, suffix=".docx", delete=False) as temp:
        temp_path = Path(temp.name)
    try:
        with zipfile.ZipFile(source) as input_docx, zipfile.ZipFile(
            temp_path, "w", compression=zipfile.ZIP_DEFLATED
        ) as output_docx:
            for item in input_docx.infolist():
                content = input_docx.read(item.filename)
                if patch_cjk and item.filename == "word/styles.xml":
                    content = patch_styles(content)
                elif patch_cjk and item.filename == "word/settings.xml":
                    content = patch_settings(content)
                elif patch_footer_text and re.fullmatch(r"word/footer[0-9]+\.xml", item.filename):
                    content = patch_footer(content)
                output_docx.writestr(item, content)
        os.replace(temp_path, destination)
        # NamedTemporaryFile uses mode 0600. Restore normal generated-artifact
        # permissions so the CI artifact uploader can read the DOCX.
        os.chmod(destination, 0o644)
    finally:
        temp_path.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--skip-cjk", action="store_true")
    parser.add_argument("--fix-footer", action="store_true")
    args = parser.parse_args()
    patch_docx(args.source, args.destination, not args.skip_cjk, args.fix_footer)


if __name__ == "__main__":
    main()
