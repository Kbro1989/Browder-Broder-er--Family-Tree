import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"

with open(f"{workspace_dir}/browder_broderers_family_tree.html", 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Extract all person card blocks - they use class="person-card" or similar
# First find all IDs to understand structure
card_blocks = re.findall(r'<div[^>]*id=["\']([^"\']+)["\'][^>]*class=["\'][^"\']*card[^"\']*["\'][^>]*>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)
if not card_blocks:
    card_blocks = re.findall(r'<div[^>]*class=["\'][^"\']*card[^"\']*["\'][^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)

print(f"Card blocks found: {len(card_blocks)}")

# Extract names/dates from each card using h3/h4 and span tags
persons = []
# Find all person-card like structures
card_pattern = re.findall(
    r'<div[^>]*(?:person|card)[^>]*>(.*?)</div>\s*</div>',
    html, re.DOTALL | re.IGNORECASE
)

# More targeted: find all h3 tags (person names in tree cards)
name_blocks = re.findall(r'<h3[^>]*>(.*?)</h3>', html, re.DOTALL | re.IGNORECASE)
print(f"\nH3 Name Blocks: {len(name_blocks)}")
for n in name_blocks:
    clean = re.sub(r'<[^>]+>', '', n).strip()
    if clean:
        print(f"  {clean}")

h4_blocks = re.findall(r'<h4[^>]*>(.*?)</h4>', html, re.DOTALL | re.IGNORECASE)
print(f"\nH4 Name Blocks: {len(h4_blocks)}")
for n in h4_blocks[:20]:
    clean = re.sub(r'<[^>]+>', '', n).strip()
    if clean:
        print(f"  {clean}")

# Extract tooltip/data-tooltip text for each card
tooltips = re.findall(r'data-tooltip=["\']([^"\']*)["\']', html, re.DOTALL)
print(f"\nTooltip data blocks: {len(tooltips)}")

with open(f"{workspace_dir}/agent_outputs/26_html_card_diff_raw.json", 'w', encoding='utf-8') as out:
    json.dump({
        "h3_name_blocks": [re.sub(r'<[^>]+>', '', n).strip() for n in name_blocks],
        "h4_name_blocks": [re.sub(r'<[^>]+>', '', n).strip() for n in h4_blocks[:40]],
        "tooltip_count": len(tooltips)
    }, out, indent=2, ensure_ascii=False)

print("\nSaved raw card diff to agent_outputs/26_html_card_diff_raw.json")
