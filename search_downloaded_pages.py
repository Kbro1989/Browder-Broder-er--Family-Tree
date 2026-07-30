import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

archive_dir = "downloaded_source_pages"

search_patterns = {
    "Browder": r'\bBrowder\b',
    "Browderer": r'\bBrowderer\b',
    "Broderer": r'\bBroderer\b',
    "Broder": r'\bBroder\b',
    "Browdere": r'\bBrowdere\b',
    "Brouder": r'\bBrouder\b',
    "Brodeur": r'\bBrodeur\b',
    "Brodator": r'\bBrodator\b',
    "Embrowder": r'\bEmbrowder\b',
    "Hulme": r'\bHulme\b',
    "Parsons": r'\bParsons\b',
    "Eppes": r'\bEppes\b'
}

print(f"=== SEARCHING ALL LOCAL HTML SOURCE PAGES IN '{archive_dir}/' FOR NAME & CRAFT PATTERNS ===")

for filename in sorted(os.listdir(archive_dir)):
    filepath = os.path.join(archive_dir, filename)
    if not os.path.isfile(filepath) or os.path.getsize(filepath) < 100:
        continue
    
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    
    # Strip HTML tags
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text)
    
    print(f"\n📄 Inspecting file: {filename} ({len(text)} chars)")
    
    for label, pattern in search_patterns.items():
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        if matches:
            print(f"   ✓ Pattern '{label}': {len(matches)} matches")
            for m in matches[:5]:
                st = max(0, m.start() - 60)
                en = min(len(text), m.end() + 60)
                snip = text[st:en].strip()
                print(f"       snippet: ... {snip} ...")

