import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_file = "browder_broderers_family_tree.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

print("=== INJECTING TIMELINED EVENTS MATRIX LINKS INTO HTML FAMILY TREE ===")

timeline_footer_link = """
<div style="margin-top: 20px; text-align: center; padding: 20px; background: rgba(168,85,247,0.08); border: 1px solid #a855f7; border-radius: 8px;">
    <p style="color: #c084fc; font-size: 1.1em; font-weight: bold; margin-bottom: 6px;">⏳ TIMELINED EVENTS MATRIX (1300 – 1990)</p>
    <p style="color: #d0c0a0; font-size: 0.9em;">Complete 690-year chronological timeline (1300 to 1990) linking all parish records, wills, headrights, battles, and lineage milestones:</p>
    <p style="margin-top: 10px;">
        <a href="./TIMELINED_EVENTS_1300_1990_MATRIX.md" target="_blank" style="color: #c084fc; font-weight: bold; font-size: 1.05em; text-decoration: underline;">📄 View 1300-1990 Timelined Matrix Report (37 Chronological Milestones)</a> | 
        <a href="./TIMELINED_EVENTS_1300_1990_MATRIX.json" target="_blank" style="color: #e9d5ff; font-size: 0.95em;">📊 View Timelined Events JSON Matrix</a>
    </p>
</div>
"""

if "TIMELINED EVENTS MATRIX (1300 – 1990)" not in html:
    html = html.replace('<!-- SOURCED LINEAGE: Every Link Tagged -->', '<!-- SOURCED LINEAGE: Every Link Tagged -->' + timeline_footer_link)
    print(" ✓ Injected 1300-1990 Timelined Events Matrix block into HTML Sourced Lineage section.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print("✓ HTML Family tree updated with direct links to 1300-1990 Timelined Events Matrix!")

