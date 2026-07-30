import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
html_file = os.path.join(workspace_dir, "browder_broderers_family_tree.html")

warnings_list = [
    {
        "id": "WARN-01",
        "title": "⚠️ ANCESTRY CONFLATION WARNING — THREE EDMUNDS",
        "severity": "CRITICAL / HIGH HAZARD",
        "affected_nodes": ["Edmund Browder I (c.1651–1739)", "Edmund W. Browder (c.1699–1771)", "Edmund Browder Sr. (c.1716–1759)"],
        "description": "Commercial genealogy databases (Ancestry.com, MyHeritage, Geni, WikiTree user trees) frequently conflate three distinct generations of Edmund Browder into a single person.",
        "empirical_proof": "Primary court records prove: (1) Edmund Browder I died ~1738/39 in Prince George Co. VA; (2) Edmund W. Browder owned Browder's Island and died impoverished in 1771 (1759 Act of Assembly); (3) Edmund Browder Sr. married Elizabeth Jones and died 1759 (Bristol Parish Registers).",
        "examination_action": "Never merge these three individuals. Treat user trees combining them as corrupted."
    },
    {
        "id": "WARN-02",
        "title": "⚠️ FICTITIOUS PERSONA — PARTHENIA 'THENEY' BROWDER BAILEY",
        "severity": "CRITICAL / FALSE PERSONA",
        "affected_nodes": ["Parthenia Browder Bailey (Fictitious)"],
        "description": "Widespread online user trees claim a 'Parthenia Theney Browder' married a Bailey in colonial Virginia/North Carolina.",
        "empirical_proof": "John Mark Browder's 2023 research article ('Parthenia Theney Browder Bailey Never Existed, and Here's Proof') proves this persona was fabricated in 20th-century family notes through misreading of Bailey deed records.",
        "examination_action": "Do NOT include Parthenia Browder Bailey in the direct lineage."
    },
    {
        "id": "WARN-03",
        "title": "⚠️ FALSE IRISH COAT OF ARMS & BRODERICK CONFLATION",
        "severity": "HIGH HAZARD",
        "affected_nodes": ["O'Bruadair / Broderick / Broderbund"],
        "description": "Claims online assert that Browder is an anglicized form of Irish O'Bruadair or Broderick and entitled to the Broderick Coat of Arms.",
        "empirical_proof": "Dr. Benjamin Hudson (Medievalist) and J.M. Browder prove Browder is an Old English occupational contraction of 'browderer' (embroiderer). Broderick derives from Welsh 'ap Rhydderch'. The Broderick Coat of Arms has ZERO historical connection to Browder.",
        "examination_action": "Reject all Irish O'Bruadair heraldry and Broderick coat of arms attachments."
    },
    {
        "id": "WARN-04",
        "title": "⚠️ PRE-1604 GENERATIONAL GAP: 1327 JOHN ➔ 1394 JOHN",
        "severity": "OPEN GAP (67 YEARS)",
        "affected_nodes": ["John Browderer (~1327)", "John Browderer (1394)"],
        "description": "A 67-year gap exists between John Browderer (King's Sergeant, 1327) and John Browderer (Citizen of London, 1394 Papal Letters).",
        "empirical_proof": "Parent-child connection is unproven due to missing 14th-century London Husting Court rolls.",
        "examination_action": "Inspect Papal Letters Vol. IV p. 488 and London Husting Wills for intermediate generation."
    },
    {
        "id": "WARN-05",
        "title": "⚠️ PRE-1604 GENERATIONAL GAP: 1466 RICHARD ➔ 1521 GILLIAM",
        "severity": "OPEN GAP (55 YEARS)",
        "affected_nodes": ["Richard Browderer (~1466)", "Gilliam Browderer (~1521)"],
        "description": "A 55-year gap (2-3 missing generations) exists between Richard Browderer (Coldharbour Cornwall, 1502 record) and Gilliam Browderer (1541 Tudor Subsidy Roll).",
        "empirical_proof": "Only Queenhithe Ward (St. Peter Somerset) of the 1541 Tudor Subsidy Roll has been transcribed; 24 London wards remain un-indexed.",
        "examination_action": "Examine remaining 24 London ward rolls for 1541 Subsidy (TNA E.179/144/120)."
    },
    {
        "id": "WARN-06",
        "title": "⚠️ PRE-1604 GENERATIONAL GAP: 1521 GILLIAM ➔ 1604 ROBERT",
        "severity": "OPEN GAP (83 YEARS)",
        "affected_nodes": ["Gilliam Browderer (~1521)", "Thomas Browder (1575)", "Robert Browder (c. 1604)"],
        "description": "An 83-year gap exists between Gilliam Browderer (London, 1541) and Robert Browder (married Marye Hulme in Manchester, 1623).",
        "empirical_proof": "LPRS Vol 31 scan proved 0 Browders in Manchester Cathedral baptisms 1573-1616. Robert was an immigrant weaver into Manchester.",
        "examination_action": "Inspect Saffron Walden (Essex) and Stoke (Warwickshire) parish registers for Robert's baptism (~1600-1604)."
    },
    {
        "id": "WARN-07",
        "title": "⚠️ VIRGINIA HEADRIGHT GRANT DATE VS ARRIVAL DATE",
        "severity": "RECORD IMPRECISION",
        "affected_nodes": ["John Broadar / Browder (1674)", "William Havercomb"],
        "description": "Virginia Land Patent Book 6, p. 526 is dated Sept 23, 1674. Headright patents were frequently issued years after actual ship arrival.",
        "empirical_proof": "William Havercomb received 950 acres for transporting 18 persons; John Broadar may have arrived in Virginia in the late 1660s.",
        "examination_action": "Treat 1674 as patent grant date, not migration arrival date."
    }
]

print(f"=== COMPILING {len(warnings_list)} HIGH-PRIORITY LINEAGE WARNINGS & DISCREPANCIES ===")

# Save JSON
json_out = os.path.join(workspace_dir, "FAMILY_TREE_WARNINGS_AND_DISCREPANCIES.json")
with open(json_out, "w", encoding="utf-8") as jout:
    json.dump(warnings_list, jout, indent=2, ensure_ascii=False)

# Save Markdown Report
md_out = os.path.join(workspace_dir, "FAMILY_TREE_WARNINGS_AND_DISCREPANCIES.md")
with open(md_out, "w", encoding="utf-8") as mout:
    mout.write("# ⚠️ FAMILY TREE WARNINGS & DISCREPANCIES EXAMINATION MATRIX\n\n")
    mout.write("Singled-out examination report detailing all critical warnings, conflation hazards, fictitious personas, and open pre-1604 generational gaps across the Browder lineage.\n\n")
    
    for item in warnings_list:
        mout.write(f"## {item['title']}\n")
        mout.write(f"• **Severity Level:** `{item['severity']}`  \n")
        mout.write(f"• **Affected Person Nodes:** *{', '.join(item['affected_nodes'])}*  \n")
        mout.write(f"• **Detailed Description:** {item['description']}  \n")
        mout.write(f"• **Empirical Proof & Evidence:** {item['empirical_proof']}  \n")
        mout.write(f"• **Required Examination Action:** `{item['examination_action']}`  \n\n")
        mout.write("---\n\n")

print(f"✓ Saved warning report to '{json_out}' and '{md_out}'!")

# Inject Warning Matrix link into browder_broderers_family_tree.html
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

warning_footer_block = """
<div style="margin-top: 20px; text-align: center; padding: 20px; background: rgba(239,68,68,0.08); border: 2px solid #ef4444; border-radius: 8px;">
    <p style="color: #fca5a5; font-size: 1.1em; font-weight: bold; margin-bottom: 6px;">⚠️ FAMILY TREE WARNINGS & DISCREPANCIES EXAMINATION MATRIX</p>
    <p style="color: #fca5a5; font-size: 0.9em;">Singled out for examination: 7 critical conflation hazards, fictitious personas, and pre-1604 generational gaps:</p>
    <p style="margin-top: 10px;">
        <a href="./FAMILY_TREE_WARNINGS_AND_DISCREPANCIES.md" target="_blank" style="color: #ef4444; font-weight: bold; font-size: 1.05em; text-decoration: underline;">🚨 View Family Tree Warnings & Discrepancies Markdown Report (7 Examination Points)</a> | 
        <a href="./FAMILY_TREE_WARNINGS_AND_DISCREPANCIES.json" target="_blank" style="color: #fca5a5; font-size: 0.95em;">📊 View Warnings JSON Matrix</a>
    </p>
</div>
"""

if "FAMILY TREE WARNINGS & DISCREPANCIES EXAMINATION MATRIX" not in html:
    html = html.replace('<!-- SOURCED LINEAGE: Every Link Tagged -->', '<!-- SOURCED LINEAGE: Every Link Tagged -->' + warning_footer_block)
    print(" ✓ Injected Warnings Matrix block into HTML Sourced Lineage section.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print("✓ Family Tree Warnings Matrix generated and linked into HTML!")

