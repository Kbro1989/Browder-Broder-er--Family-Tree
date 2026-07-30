import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"

with open(f"{workspace_dir}/browder_broderers_family_tree.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

print(f"File length: {len(html)} chars")

# Find the persons JS data object - the HTML likely stores person data in a JS object
persons_js = re.search(r"const persons\s*=\s*(\{.*?\});", html, re.DOTALL)
if not persons_js:
    persons_js = re.search(r"var persons\s*=\s*(\{.*?\});", html, re.DOTALL)
if not persons_js:
    persons_js = re.search(r"persons\s*=\s*(\{[^;]{200,}\});", html, re.DOTALL)

if persons_js:
    print("Found persons JS object!")
    print(persons_js.group(1)[:3000])
else:
    print("No persons JS object found. Scanning for person data patterns...")

    # Try onclick handlers
    onclick_ids = re.findall(r"showPerson\(['\"]([^'\"]+)['\"]\)", html)
    print(f"\nshowPerson IDs found: {len(onclick_ids)}")
    for p in onclick_ids[:60]:
        print(f"  {p}")

    # Find person card name spans
    name_spans = re.findall(r'class="card-name"[^>]*>\s*([^<]{3,60})\s*<', html)
    print(f"\ncard-name spans: {len(name_spans)}")
    for n in name_spans[:60]:
        print(f"  {n.strip()}")

    # Find person-name or name class
    pname_spans = re.findall(r'class="person-name"[^>]*>\s*([^<]{3,60})\s*<', html)
    print(f"\nperson-name spans: {len(pname_spans)}")
    for n in pname_spans[:60]:
        print(f"  {n.strip()}")

    # look for strong tags inside cards
    strong_tags = re.findall(r'<strong[^>]*>\s*([A-Z][^<]{3,80})\s*</strong>', html)
    print(f"\nStrong tags: {len(strong_tags)}")
    for s in strong_tags[:40]:
        print(f"  {s.strip()}")

    # Find year spans or date class
    dates = re.findall(r'class="(?:date|birth|years|lifespan)[^"]*"[^>]*>\s*([^<]{3,40})\s*<', html)
    print(f"\nDate/year spans: {len(dates)}")
    for d in dates[:30]:
        print(f"  {d.strip()}")

    # Dump middle section of HTML to see data structure
    mid = len(html) // 2
    print(f"\n--- HTML SAMPLE at position {mid} ---")
    print(html[mid:mid+3000])

