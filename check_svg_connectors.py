import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_file = "browder_broderers_family_tree.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

card_matches = re.findall(r'<div class="person-card ([^"]+)" style="top: (\d+)px; left: (\d+)px;"\s+data-name="([^"]+)"', html)
print(f"=== TOTAL PERSON CARDS IN HTML: {len(card_matches)} ===")

svg_matches = re.findall(r'<line x1="(\d+)" y1="(\d+)" x2="(\d+)" y2="(\d+)"', html)
print(f"=== TOTAL SVG CONNECTOR LINES IN HTML: {len(svg_matches)} ===")

# Generate additional dashed green lines for new associate cards if needed
new_lines = """
        <!-- ASSOCIATE & IN-LAW CONNECTOR LINES -->
        <line x1="1260" y1="230" x2="1380" y2="230" stroke="#5a7a5a" stroke-width="2" stroke-dasharray="4" />
        <line x1="640" y1="140" x2="1380" y2="140" stroke="#5a7a5a" stroke-width="2" stroke-dasharray="4" />
        <line x1="1260" y1="410" x2="1380" y2="410" stroke="#5a7a5a" stroke-width="2" stroke-dasharray="4" />
        <line x1="1260" y1="500" x2="1380" y2="500" stroke="#5a7a5a" stroke-width="2" stroke-dasharray="4" />
"""

if "ASSOCIATE & IN-LAW CONNECTOR LINES" not in html:
    html = html.replace('</svg>', new_lines + '\n    </svg>')
    print(" ✓ Added SVG connector lines for associate and in-law cards.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print("✓ SVG line check finished!")

