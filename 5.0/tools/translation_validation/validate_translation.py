"""
Driver script to validate ASVS translations.

Replicates the logic previously embedded in the GitHub Actions bash step:
- Verifies the translated folder exists
- Iterates over all markdown files in the original directory
- Ensures each has a corresponding translated file
- Runs requirement and structural checks for each file

Usage:
    python 5.0/tools/translation_validation/validate_translation.py \
        --translated-folder <folder_inside_5.0>

Example:
    python 5.0/tools/translation_validation/validate_translation.py --translated-folder tr
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Ensure we can import sibling modules when running as a script
_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

import req_check as req_validator  # type: ignore
import structural_check as struct_validator  # type: ignore


APPENDIX_C = "0x92-Appendix-C_Cryptography.md"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ASVS translation against originals")
    parser.add_argument(
        "--translated-folder",
        required=True,
        help="Name of the folder inside 5.0/ that contains translated files (e.g. 'tr' or 'he')",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    original_dir = repo_root / "5.0" / "en"
    translated_dir = repo_root / "5.0" / args.translated_folder

    if not translated_dir.is_dir():
        print(f"❌ Translated directory not found: {translated_dir}")
        return 1

    if not original_dir.is_dir():
        print(f"❌ Original directory not found: {original_dir}")
        return 1

    md_files = sorted(original_dir.glob("*.md"))

    # Collect per-file results for summary
    results = []  # each item: {file, missing, req, struct}

    for original_file in md_files:
        fname = original_file.name
        translated_file = translated_dir / fname

        if not translated_file.is_file():
            print(f"❌ Missing translation for {fname}")
            results.append({
                "file": fname,
                "missing": True,
                "req": None,
                "struct": None,
            })
            continue

        print(f"🔍 Validating {fname} ...")

        req_status: object
        struct_status: bool

        # Run requirement check for all but Appendix C
        if fname != APPENDIX_C:
            req_status = req_validator.validate_files(str(original_file), str(translated_file))
        else:
            req_status = "skipped"

        # Run structural check
        struct_status = struct_validator.validate_files(str(original_file), str(translated_file))

        results.append({
            "file": fname,
            "missing": False,
            "req": req_status,
            "struct": struct_status,
        })

    # Per-file summary
    print("\n----- Per-file summary -----")
    for r in results:
        if r["missing"]:
            print(f"❌ {r['file']} — missing translation")
            continue
        req_txt = (
            "ok" if r["req"] is True else ("skipped" if r["req"] == "skipped" else "fail")
        )
        struct_txt = "ok" if r["struct"] is True else "fail"
        passed = ((r["req"] is True) or (r["req"] == "skipped")) and (r["struct"] is True)
        prefix = "✅" if passed else "❌"
        print(f"{prefix} {r['file']} — req: {req_txt}, struct: {struct_txt}")

    # Overall summary
    total = len(md_files)
    missing = sum(1 for r in results if r["missing"])
    translated_count = total - missing
    req_failures = sum(1 for r in results if (not r["missing"]) and (r["req"] is False))
    struct_failures = sum(1 for r in results if (not r["missing"]) and (r["struct"] is False))
    passes = sum(
        1
        for r in results
        if (not r["missing"]) and ((r["req"] is True) or (r["req"] == "skipped")) and (r["struct"] is True)
    )
    overall_ok = missing == 0 and req_failures == 0 and struct_failures == 0

    print("\n----- Summary -----")
    ok_emoji = "✅"
    fail_emoji = "❌"
    def mark(cond: bool) -> str:
        return ok_emoji if cond else fail_emoji

    print(f"Total files: {total}")
    print(f"{mark(translated_count == total)} Translated found: {translated_count}")
    print(f"{mark(missing == 0)} Missing translations: {missing}")
    print(f"{mark(req_failures == 0)} Requirement check failures: {req_failures}")
    print(f"{mark(struct_failures == 0)} Structural check failures: {struct_failures}")
    print(f"{mark(passes == translated_count)} Fully passed: {passes}")
    print(f"{ok_emoji if overall_ok else fail_emoji} Overall: {'PASS' if overall_ok else 'FAIL'}")

    return 0 if overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
