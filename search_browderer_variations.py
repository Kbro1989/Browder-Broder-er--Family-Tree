import urllib.request
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

local_file = "lancashireparis03socigoog_djvu.txt"

if not os.path.exists(local_file):
    url = "https://archive.org/download/lancashireparis03socigoog/lancashireparis03socigoog_djvu.txt"
    print(f"Downloading {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'AntigravityGenealogyBot/1.0'})
    with urllib.request.urlopen(req) as resp, open(local_file, 'wb') as f:
        f.write(resp.read())

with open(local_file, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print(f"=== DEEP SUBSTRING & OCR NOISE SEARCH: BROWDERER IN VOL 31 ({len(text)} chars) ===")

patterns = [
    ("Exact substring 'browderer'", r'browderer'),
    ("Exact substring 'broderer'", r'broderer'),
    ("Exact substring 'browder'", r'browder'),
    ("Exact substring 'broder'", r'broder'),
    ("OCR fuzzy 'br*w*d*r*r'", r'b[r\s]*[o0uvw]*[w\s]*[d\s]*[e3]*[r\s]*[e3]*[r\s]*'),
    ("Flemish/French variant 'brodeur'", r'brodeur'),
    ("Late Latin/Norman 'brodator'", r'brodator'),
    ("Embroidery craft 'embrowder'", r'embrowder')
]

for label, pattern in patterns:
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    print(f"\n--- {label} (Pattern: '{pattern}') ---")
    print(f"Total matches found: {len(matches)}")
    if matches and label != "OCR fuzzy 'br*w*d*r*r'":
        for i, m in enumerate(matches[:20]):
            start = max(0, m.start() - 60)
            end = min(len(text), m.end() + 60)
            snippet = text[start:end].replace('\n', ' ')
            print(f"  {i+1}. match='{m.group(0)}' @ char {m.start()}: ... {snippet} ...")

print("\n=== SCANNING OTHER LPRS VOLUMES ON ARCHIVE.ORG FOR 'BROWDERER' ===")
lprs_ids = [
    "lancashireparis01socigoog",
    "lancashireparis02socigoog",
    "lancashireparis04socigoog",
    "lancashireparis05socigoog",
    "lancashireparis06socigoog",
    "lancashireparis07socigoog",
    "lancashireparis08socigoog",
    "lancashireparis09socigoog",
    "lancashireparis10socigoog"
]

for item_id in lprs_ids:
    txt_url = f"https://archive.org/download/{item_id}/{item_id}_djvu.txt"
    try:
        req = urllib.request.Request(txt_url, headers={'User-Agent': 'AntigravityGenealogyBot/1.0'})
        with urllib.request.urlopen(req) as resp:
            vol_text = resp.read().decode('utf-8', errors='ignore')
        
        matches = list(re.finditer(r'browderer|broderer|browder|broder', vol_text, re.IGNORECASE))
        if matches:
            print(f"\n[!] MATCH IN {item_id} ({len(vol_text)} chars): {len(matches)} matches!")
            for m in matches[:10]:
                st = max(0, m.start() - 50)
                en = min(len(vol_text), m.end() + 50)
                snip = vol_text[st:en].replace('\n', ' ')
                print(f"    - match='{m.group(0)}': ... {snip} ...")
        else:
            print(f"  Item {item_id}: 0 matches for browderer/broderer/browder/broder")
    except Exception as e:
        print(f"  Item {item_id}: Error fetching - {e}")

