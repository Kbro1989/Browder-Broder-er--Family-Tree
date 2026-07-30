import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

remaining_ids = [
    "lancashireparis11socigoog",
    "lancashireparis12socigoog",
    "lancashireparis13socigoog",
    "lancashireparis14socigoog",
    "lancashireparis15socigoog",
    "lancashireparis16socigoog",
    "lancashireparis17socigoog",
    "lancashireparis18socigoog",
    "lancashireparis19socigoog",
    "lancashireparis20socigoog",
    "lancashireparis21socigoog",
    "lancashireparis22socigoog",
    "lancashireparis23socigoog"
]

print("=== SCANNING LPRS VOLUMES 11 TO 23 ON ARCHIVE.ORG FOR 'BROWDERER' & 'BROWDER' ===")

for item_id in remaining_ids:
    txt_url = f"https://archive.org/download/{item_id}/{item_id}_djvu.txt"
    try:
        req = urllib.request.Request(txt_url, headers={'User-Agent': 'AntigravityGenealogyBot/1.0'})
        with urllib.request.urlopen(req) as resp:
            vol_text = resp.read().decode('utf-8', errors='ignore')
        
        matches = list(re.finditer(r'\b(browderer|broderer|browder|broder|browdere)\b', vol_text, re.IGNORECASE))
        if matches:
            print(f"\n[!] MATCH IN {item_id} ({len(vol_text)} chars): {len(matches)} matches!")
            for m in matches[:10]:
                st = max(0, m.start() - 50)
                en = min(len(vol_text), m.end() + 50)
                snip = vol_text[st:en].replace('\n', ' ')
                print(f"    - match='{m.group(0)}': ... {snip} ...")
        else:
            print(f"  Item {item_id}: 0 matches")
    except Exception as e:
        print(f"  Item {item_id}: Error fetching - {e}")

