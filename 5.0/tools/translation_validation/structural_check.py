import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(
        description="Validate that translation has the same structure as the original"
    )
    parser.add_argument("--og", required=True, help="Path to original ASVS file")
    parser.add_argument("--tr", required=True, help="Path to translated ASVS file")
    return parser.parse_args()

def extract_newlines(text: str):
    """Return list of line numbers that are blank."""
    return [i for i, line in enumerate(text.splitlines(), start=1) if line.strip() == ""]

def check_newlines(orig, trans):
    """Compare newline positions and return mismatch info"""
    if len(orig) != len(trans):
        # Find first mismatch
        for i, (o, t) in enumerate(zip(orig, trans), start=1):
            if o != t:
                return (False, f"Mismatch at original line {o} vs translated line {t}", len(orig), len(trans))
        # One list is longer
        return (False, f"Extra newlines starting at line {min(len(orig), len(trans))}", len(orig), len(trans))
    else:
        for o, t in zip(orig, trans):
            if o != t:
                return (False, f"Mismatch at original line {o} vs translated line {t}", len(orig), len(trans))
    return (True, None, len(orig), len(trans))

def main():
    args = get_args()

    with open(args.og, encoding="utf-8") as f:
        original_text = f.read()
    with open(args.tr, encoding="utf-8") as f:
        translation_text = f.read()

    orig_newlines = extract_newlines(original_text)
    trans_newlines = extract_newlines(translation_text)

    ok, msg, o_count, t_count = check_newlines(orig_newlines, trans_newlines)

    if not ok:
        print("❌ Newline mismatch detected")
        print(f"   - Original count: {o_count}, Translation count: {t_count}")
        print(f"   - First issue: {msg}")
        print(" To see the other mismatched newline positions, solve the first issue and re-run.")
        sys.exit(1)
    else:
        print(f"✅ Newlines match exactly (count={o_count})")
        sys.exit(0)

if __name__ == "__main__":
    main()
