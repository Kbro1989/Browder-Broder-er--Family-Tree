import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_file = "browder_broderers_family_tree.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

print("=== INJECTING VARIABLE CROSS-REFERENCE MATRIX LINKS INTO HTML FAMILY TREE ===")

variable_footer_link = """
<div style="margin-top: 20px; text-align: center; padding: 20px; background: rgba(236,72,153,0.08); border: 1px solid #ec4899; border-radius: 8px;">
    <p style="color: #f472b6; font-size: 1.1em; font-weight: bold; margin-bottom: 6px;">🔬 VARIABLE & ATTRIBUTE CROSS-REFERENCE MATRIX</p>
    <p style="color: #d0c0a0; font-size: 0.9em;">Exhaustive attribute cross-reference across all 103 repository files, python scripts, JSON models, text transcripts, and HTML dumps:</p>
    <p style="margin-top: 10px;">
        <a href="./VARIABLE_ATTRIBUTE_CROSS_REFERENCE_MATRIX.md" target="_blank" style="color: #f472b6; font-weight: bold; font-size: 1.05em; text-decoration: underline;">📄 View Variable & Attribute Matrix Report (103 Files)</a> | 
        <a href="./VARIABLE_ATTRIBUTE_CROSS_REFERENCE_MATRIX.json" target="_blank" style="color: #fbcfe8; font-size: 0.95em;">📊 View Variable Attributes JSON Matrix</a>
    </p>
</div>
"""

if "VARIABLE & ATTRIBUTE CROSS-REFERENCE MATRIX" not in html:
    html = html.replace('<!-- SOURCED LINEAGE: Every Link Tagged -->', '<!-- SOURCED LINEAGE: Every Link Tagged -->' + variable_footer_link)
    print(" ✓ Injected Variable & Attribute Cross-Reference Matrix block into HTML Sourced Lineage section.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print("✓ HTML Family tree updated with direct links to Variable & Attribute Cross-Reference Matrix!")

