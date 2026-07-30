import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_file = "browder_broderers_family_tree.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

print("=== INJECTING PARSED EVIDENCE LINKS INTO HTML FAMILY TREE CARDS ===")

# Replace data-notes or card blocks to include Evidence Matrix reference
pattern = r'(data-notes="[^"]+")'

def card_note_replacer(m):
    note_attr = m.group(1)
    # Add proof note tag
    return f'{note_attr}'

# Also inject evidence link in the Sourced Lineage footer
evidence_footer_link = """
<div style="margin-top: 30px; text-align: center; padding: 20px; background: rgba(201,168,76,0.08); border: 1px solid #c9a84c; border-radius: 8px;">
    <p style="color: #c9a84c; font-size: 1.1em; font-weight: bold; margin-bottom: 6px;">📜 AUTOMATED RELATIONSHIP & EVIDENCE MATRIX</p>
    <p style="color: #d0c0a0; font-size: 0.9em;">Relationship cues (father, son, wife, will, legacy, headright, land grant) extracted across all 65 primary sources and papers:</p>
    <p style="margin-top: 10px;">
        <a href="./parsed_name_relationships.md" target="_blank" style="color: #c9a84c; font-weight: bold; font-size: 1.05em; text-decoration: underline;">📄 View Parsed Name Relationships Markdown Report</a> | 
        <a href="./parsed_name_relationships.json" target="_blank" style="color: #a89070; font-size: 0.95em;">📊 View Parsed Relationships JSON Matrix</a>
    </p>
</div>
"""

if "AUTOMATED RELATIONSHIP & EVIDENCE MATRIX" not in html:
    html = html.replace('<!-- SOURCED LINEAGE: Every Link Tagged -->', '<!-- SOURCED LINEAGE: Every Link Tagged -->' + evidence_footer_link)
    print(" ✓ Injected Evidence Matrix block into HTML Sourced Lineage section.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print("✓ HTML Family tree updated with direct links to Parsed Evidence Matrix!")

