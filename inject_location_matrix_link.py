import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_file = "browder_broderers_family_tree.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

print("=== INJECTING LOCATION CROSS-REFERENCE MATRIX LINKS INTO HTML FAMILY TREE ===")

location_footer_link = """
<div style="margin-top: 20px; text-align: center; padding: 20px; background: rgba(59,130,246,0.08); border: 1px solid #3b82f6; border-radius: 8px;">
    <p style="color: #60a5fa; font-size: 1.1em; font-weight: bold; margin-bottom: 6px;">📍 GEOGRAPHIC LOCATION CROSS-REFERENCE MATRIX</p>
    <p style="color: #d0c0a0; font-size: 0.9em;">Cross-referenced historical locations (London, Manchester, Saffron Walden, Suffolk, Cornwall, Tipperary, Dublin, Virginia, North Carolina, Tennessee) across all source files:</p>
    <p style="margin-top: 10px;">
        <a href="./location_cross_reference_matrix.md" target="_blank" style="color: #60a5fa; font-weight: bold; font-size: 1.05em; text-decoration: underline;">📄 View Geographic Location Matrix Markdown Report</a> | 
        <a href="./location_cross_reference_matrix.json" target="_blank" style="color: #93c5fd; font-size: 0.95em;">📊 View Location Cross-Reference JSON Matrix</a>
    </p>
</div>
"""

if "GEOGRAPHIC LOCATION CROSS-REFERENCE MATRIX" not in html:
    html = html.replace('<!-- SOURCED LINEAGE: Every Link Tagged -->', '<!-- SOURCED LINEAGE: Every Link Tagged -->' + location_footer_link)
    print(" ✓ Injected Location Cross-Reference Matrix block into HTML Sourced Lineage section.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print("✓ HTML Family tree updated with direct links to Geographic Location Matrix!")

