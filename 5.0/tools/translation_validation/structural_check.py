# This script validates that a translated ASVS file maintains the same structural format as the original file.
# It compares the positions of blank lines between the original and translated files to ensure consistency.
# Usage:
#   python structural_check.py --og <original_file> --tr <translated_file>
# Arguments:
#   --og : Path to the original ASVS file
#   --tr : Path to the translated ASVS file

import argparse
import sys


parser = argparse.ArgumentParser(
    description="Validate that translation has the same structure as the original"
)
parser.add_argument("--og", required=True, help="Path to original ASVS file")
parser.add_argument("--tr", required=True, help="Path to translated ASVS file")
args = parser.parse_args()

def extract_newlines(text: str):
    """Return list of line numbers that are blank."""
    return [i for i, line in enumerate(text.splitlines(), start=1) if line.strip() == ""]

def check_newlines(orig, trans):
    """Compare newline positions and return mismatch info"""
    min_len = min(len(orig), len(trans))
    for idx in range(min_len):
        if orig[idx] != trans[idx]:
            # Report the index and the actual line numbers
            return (
                False,
                f"Mismatch at newline {idx+1}: original blank line at {orig[idx]}, translated blank line at {trans[idx]}",
                len(orig),
                len(trans)
            )
    if len(orig) != len(trans):
        # One list is longer
        return (
            False,
            f"Extra blank lines in one of the files, starting at newline {min_len+1}",
            len(orig),
            len(trans)
        )
    return (True, None, len(orig), len(trans))

def main():
    with open(args.og, encoding="utf-8") as f:
        original_text = f.read()
    with open(args.tr, encoding="utf-8") as f:
        translation_text = f.read()

    orig_newlines = extract_newlines(original_text)
    trans_newlines = extract_newlines(translation_text)

    ok, msg, o_count, t_count = check_newlines(orig_newlines, trans_newlines)

    if not ok:
        print(f"❌ Newline mismatch detected at file {args.og}")
        print(f"   - Original count: {o_count}, Translation count: {t_count}")
        print(f"   - First issue: {msg}")
        print(" To see the other mismatched newline positions, solve the first issue and re-run.")
        sys.exit(1)
    else:
        print(f"✅ Newlines match exactly (count={o_count})")
        sys.exit(0)

if __name__ == "__main__":
    main()
