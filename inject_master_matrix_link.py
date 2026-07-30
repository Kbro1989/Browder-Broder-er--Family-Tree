import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_file = "browder_broderers_family_tree.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

print("=== INJECTING MASTER CROSS-REFERENCE MATRIX LINKS INTO HTML FAMILY TREE ===")

master_footer_link = """
<div style="margin-top: 20px; text-align: center; padding: 20px; background: rgba(16,185,129,0.08); border: 1px solid #10b981; border-radius: 8px;">
    <p style="color: #34d399; font-size: 1.1em; font-weight: bold; margin-bottom: 6px;">🌐 MASTER REPOSITORY FILE CROSS-REFERENCE MATRIX</p>
    <p style="color: #d0c0a0; font-size: 0.9em;">N-to-N cross-reference of all 94 workspace files, research papers, local source pages, JSON nodes, and location/relationship matrices:</p>
    <p style="margin-top: 10px;">
        <a href="./MASTER_FILE_CROSS_REFERENCE_MATRIX.md" target="_blank" style="color: #34d399; font-weight: bold; font-size: 1.05em; text-decoration: underline;">📄 View Master File Cross-Reference Matrix Report (94 Files)</a> | 
        <a href="./MASTER_FILE_CROSS_REFERENCE_MATRIX.json" target="_blank" style="color: #6ee7b7; font-size: 0.95em;">📊 View Master Cross-Reference JSON Matrix</a>
    </p>
</div>
"""

if "MASTER REPOSITORY FILE CROSS-REFERENCE MATRIX" not in html:
    html = html.replace('<!-- SOURCED LINEAGE: Every Link Tagged -->', '<!-- SOURCED LINEAGE: Every Link Tagged -->' + master_footer_link)
    print(" ✓ Injected Master File Cross-Reference Matrix block into HTML Sourced Lineage section.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print("✓ HTML Family tree updated with direct links to Master File Cross-Reference Matrix!")

