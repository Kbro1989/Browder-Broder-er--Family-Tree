import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("lancashireparis03socigoog_djvu.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

patterns = [
    (r'\bBr[ooaudw]+der[e]?r?\b', "Browder/Broderer wildcard variants"),
    (r'\bBrouder\b', "Brouder"),
    (r'\bBrother\b', "Brother (if misread)"),
    (r'\bHulme\b', "Hulme")
]

print("=== DEEP FUZZY OCR SEARCH RESULTS (Manchester Cathedral Registers 1573-1616) ===")

for pat, desc in patterns:
    matches = list(re.finditer(pat, text, re.IGNORECASE))
    print(f"\n[{desc}] Pattern: '{pat}' -> Total matches: {len(matches)}")
    # Print distinct matching words
    distinct_words = set(m.group(0) for m in matches)
    print(f"Distinct matching tokens found: {distinct_words}")

