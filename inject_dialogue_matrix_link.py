import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_file = "browder_broderers_family_tree.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

print("=== INJECTING DIALOGUE & COMMUNICATION MATRIX LINKS INTO HTML FAMILY TREE ===")

dialogue_footer_link = """
<div style="margin-top: 20px; text-align: center; padding: 20px; background: rgba(234,179,8,0.08); border: 1px solid #eab308; border-radius: 8px;">
    <p style="color: #facc15; font-size: 1.1em; font-weight: bold; margin-bottom: 6px;">🗣️ INTERPERSONAL DIALOGUE & ORAL COMMUNICATION MATRIX</p>
    <p style="color: #d0c0a0; font-size: 0.9em;">Cross-reference of who spoke to whom, about what, and when across all emails, oral traditions, depositions, and guild songs:</p>
    <p style="margin-top: 10px;">
        <a href="./INTERPERSONAL_DIALOGUE_COMMUNICATION_MATRIX.md" target="_blank" style="color: #facc15; font-weight: bold; font-size: 1.05em; text-decoration: underline;">📄 View Dialogue & Oral Communication Matrix Report</a> | 
        <a href="./INTERPERSONAL_DIALOGUE_COMMUNICATION_MATRIX.json" target="_blank" style="color: #fef08a; font-size: 0.95em;">📊 View Dialogue Events JSON Matrix</a>
    </p>
</div>
"""

if "INTERPERSONAL DIALOGUE & ORAL COMMUNICATION MATRIX" not in html:
    html = html.replace('<!-- SOURCED LINEAGE: Every Link Tagged -->', '<!-- SOURCED LINEAGE: Every Link Tagged -->' + dialogue_footer_link)
    print(" ✓ Injected Dialogue & Communication Matrix block into HTML Sourced Lineage section.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print("✓ HTML Family tree updated with direct links to Interpersonal Dialogue & Communication Matrix!")

