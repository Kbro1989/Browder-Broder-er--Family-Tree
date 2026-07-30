import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("browder_broderers_lineage.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)

with open("browder_broderers_family_tree.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Extract data-name from HTML person-cards
html_card_names = re.findall(r'data-name="([^"]+)"', html_content)
html_card_set = set(h.strip() for h in html_card_names)

# Extract nodes from JSON
nodes = json_data.get('nodes', {})
print(f"=== TOTAL NODES IN JSON: {len(nodes)} ===")

json_nodes_dict = {}
for node_id, node in nodes.items():
    name = node.get('name', '')
    json_nodes_dict[node_id] = {
        'name': name,
        'dates': node.get('dates'),
        'location': node.get('location'),
        'parents': node.get('parents', []),
        'children': node.get('children', []),
        'uncertainty': node.get('uncertainty')
    }

print("\n--- NODES IN JSON BUT MISSING / DIFFERENT IN HTML ---")
missing_in_html = []
for node_id, info in json_nodes_dict.items():
    name = info['name']
    # Check if name or substring exists in HTML card names
    found = any(name.lower() in h.lower() or h.lower() in name.lower() for h in html_card_set)
    if not found:
        missing_in_html.append((node_id, name, info))
        print(f" ❌ [JSON Node ID: {node_id}] '{name}' -> NOT in HTML timeline cards!")
    else:
        print(f" ✓ [JSON Node ID: {node_id}] '{name}' -> Present in HTML")

print(f"\nTotal JSON nodes missing in HTML: {len(missing_in_html)}")

# Now check SVG connector lines in HTML vs JSON linkages
print("\n--- CHECKING SVG CONNECTOR LINES IN HTML ---")
svg_lines = re.findall(r'<line [^>]+>', html_content)
print(f"Total SVG connector lines in HTML: {len(svg_lines)}")

# Extract Complete Chain from HTML
complete_chain_items = re.findall(r'<p><span style="color:[^"]+">(0[a-h]|\d+[a-z]?).*?<\/p>', html_content, re.DOTALL)
print(f"\nTotal items in COMPLETE CHAIN SUMMARY: {len(complete_chain_items)}")
for item in complete_chain_items:
    clean_item = re.sub(r'<[^>]+>', '', item).strip()
    print(f"  - {clean_item}")

