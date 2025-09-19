
# This script validates that requirements in a translated ASVS file maintains the same content and structural format as the original file.
# It compares the positions of blank lines between the original and translated files to ensure consistency.
# Usage:
#   python reg_check.py --og <original_file> --tr <translated_file>
# Arguments:
#   --og : Path to the original ASVS file
#   --tr : Path to the translated ASVS file

import argparse
import re
import sys

# Arguments are processed at the beginning to allow function reuse
parser = argparse.ArgumentParser(
    description="Validate that all ASVS requirements exist correctly in translation"
)
parser.add_argument("--og", required=True, help="Path to original ASVS file")
parser.add_argument("--tr", required=True, help="Path to translated ASVS file")
args = parser.parse_args()



def extract_special_chars(text: str) -> set[str]:
    """
    Extract non-alphanumeric, non-space, non-markdown special characters.
    """
    return set(re.findall(r"[^a-zA-Z0-9\s\|\*\-_#]", text))

def extract_table_rows(text: str) -> list[list[str]]:
    """
    Extracts table rows from markdown, returns as list of column lists.
    """
    rows = []
    for line in text.splitlines():
        if line.strip().startswith("|") and not line.strip().startswith("| :---") and not line.strip().startswith("| #"):
            cols = [c.strip() for c in line.split("|")[1:-1]]  # drop leading/trailing '|'
            rows.append(cols)
    return rows

def extract_requirements(text: str) -> set[str]:
    # Extracts the requirements' numerical value with regex

    return set(re.findall(r"\*\*(\d+\.\d+\.\d+)\*\*", text))


def check_reg_count(original: str, translation: str) -> bool:
    check = True

    original_reqs = extract_requirements(original)
    translation_reqs = extract_requirements(translation)

    # Compare sets
    missing_reqs = original_reqs - translation_reqs
    extra_reqs = translation_reqs - original_reqs

    print("=== Requirement Validation ===")
    print(f"Original count: {len(original_reqs)}")
    print(f"Translation count: {len(translation_reqs)}")
    print()

    if missing_reqs:
        print(f"❌ Missing in translation ({len(missing_reqs)}):")
        for req in sorted(missing_reqs):
            print(f"   - {req} from original file: {args.og}")
        check = False

    if extra_reqs:
        print(f"\n⚠️ Extra in translation ({len(extra_reqs)}):")
        for req in sorted(extra_reqs):
            print(f"   - {req} at translation file: {args.tr}")
        check = False

    if check:
        print("✅ All requirements exist in translation.")

    return check

def compare_rows_columns(original: str, translation: str) -> bool:

    original_rows = extract_table_rows(original)
    translation_rows = extract_table_rows(translation)

    errors = []
    for i, (o_row, t_row) in enumerate(zip(original_rows, translation_rows), start=1):

        # Compare all except description
        for j in range(len(o_row)):
            if j == len(o_row) - 2: 
                continue
            if o_row[j] != t_row[j]:
                errors.append(f"At requirement {o_row[0]}, Column {j+1}: mismatch (Original value:'{o_row[j]}', Translation value:'{t_row[j]}')")

    if errors:
        print("❌ Content mismatches found:")
        for err in errors:
            print("   -", err)
        return False
    else:
        print("✅ All requirement IDs and non-description columns match")
        return True

def main():

    # Read files
    with open(args.og, encoding="utf-8") as f:
        original_text = f.read()
    with open(args.tr, encoding="utf-8") as f:
        translation_text = f.read()

    if not check_reg_count(original_text, translation_text):
        print("Please fix the issues about missing/extra requirements to proceed with other checks.")
        sys.exit(1)

    if not compare_rows_columns(original_text, translation_text):
        print("Please fix the content mismatches for validation.")
        sys.exit(1)

    print("\nAll checks passed successfully.")

    ### Question: I think we shouldn't check special characters, as some languages may not use the same ones but
    ### still be correct. What do you think? Also, the translator may use different characters for parentheses, dashes, etc.
    ### to make it look better in their language.

if __name__ == "__main__":
    main()