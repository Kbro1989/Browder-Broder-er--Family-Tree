import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
html_file = os.path.join(workspace_dir, "browder_broderers_family_tree.html")

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

print("=== APPLYING SOVEREIGN HTML TREE FIXES & REALIGNMENTS ===")

# Fix 1: Add <base target="_blank"> to <head>
if '<base target="_blank">' not in html:
    html = html.replace('<head>', '<head>\n    <base target="_blank">')
    print(" ✓ Added <base target=\"_blank\"> to <head>")

# Fix 2: Increase timeline container height to 2800px
html = re.sub(r'height:\s*1600px;', 'height: 2800px;', html)
html = re.sub(r'min-height:\s*1600px;', 'min-height: 2800px;', html)
print(" ✓ Increased timeline container height to 2800px")

# Fix 3: Clean duplicate "The Contraction" heading in Doctrine section
if html.count("The Contraction") > 1:
    # Retain the single comprehensive Contraction section
    html = html.replace('<h3>The Contraction</h3>\n        <p>Between 1575 and 1623', '<h3>The Contraction: From Broderer to Browder</h3>\n        <p>Between 1575 and 1623')
    html = html.replace('<h3>The Contraction</h3>', '<!-- Merged Contraction Block -->')
    print(" ✓ Cleaned and merged duplicate 'The Contraction' headers in Doctrine section.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print("✓ HTML Family tree updated with all structural & mechanical fixes!")

