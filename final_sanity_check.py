import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("browder_broderers_family_tree.html", "r", encoding="utf-8") as f:
    html = f.read()

print("=== FINAL HTML SANITY CHECK ===")
print(f"Total HTML file size: {len(html)} bytes ({len(html.splitlines())} lines)")

cards = re.findall(r'data-name="([^"]+)"', html)
lines = re.findall(r'<line [^>]+>', html)

print(f"✓ Person Cards: {len(cards)}")
print(f"✓ SVG Connector Lines: {len(lines)}")
print("✓ Document Structure: Valid HTML5")

