import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_file = "browder_broderers_family_tree.html"
json_file = "browder_broderers_lineage.json"

print("=== ADDING IN-LAWS, SPOUSES, NEIGHBORS AND ACQUAINTANCES CARDS ===")

with open(json_file, "r", encoding="utf-8") as f:
    lineage = json.load(f)

nodes = lineage.get("nodes", {})

new_nodes = {
    "adam_hulme_1575": {
        "id": "adam_hulme_1575",
        "name": "Adam Hulme",
        "type": "individual",
        "dates": {"birth": 1575, "death": None},
        "location": "Manchester Cathedral Parish, Lancashire, England",
        "notes": "Father of Marye Hulme (christened Feb 4, 1601). Native Manchester parishioner whose daughter married Robert Browder on Dec 26, 1623.",
        "uncertainty": "certain",
        "sources": [{"url": "https://archive.org/details/lancashireparis03socigoog", "label": "Manchester Cathedral Registers (LPRS Vol 31)"}]
    },
    "elizabeth_parsons_1655": {
        "id": "elizabeth_parsons_1655",
        "name": "Elizabeth Parsons",
        "type": "individual",
        "dates": {"birth": 1655, "death": None},
        "location": "Surry County, Virginia",
        "notes": "Wife of Edmund Browder I. Documented in Surry County court records and land transactions.",
        "uncertainty": "probable",
        "sources": [{"url": "https://genealogyproofs.wordpress.com/blog-feed/page/3/", "label": "J.M. Browder Research"}]
    },
    "lt_arthur_jones_1660": {
        "id": "lt_arthur_jones_1660",
        "name": "Lt. Arthur Jones",
        "type": "individual",
        "dates": {"birth": 1660, "death": None},
        "location": "Prince George County, Virginia",
        "notes": "Father of Elizabeth Jones (who married John Browder Sr. in 1715). Landowner on Gravelly Run.",
        "uncertainty": "certain",
        "sources": [{"url": "https://genealogyproofs.wordpress.com/blog-feed/page/3/", "label": "Prince George Co. Deeds"}]
    },
    "susanna_king_1665": {
        "id": "susanna_king_1665",
        "name": "Susanna King",
        "type": "individual",
        "dates": {"birth": 1665, "death": None},
        "location": "Prince George County, Virginia",
        "notes": "Wife of Lt. Arthur Jones and mother of Elizabeth Jones.",
        "uncertainty": "certain",
        "sources": [{"url": "https://genealogyproofs.wordpress.com/blog-feed/page/3/", "label": "Prince George Co. Records"}]
    },
    "col_robert_bolling_1646": {
        "id": "col_robert_bolling_1646",
        "name": "Col. Robert Bolling",
        "type": "individual",
        "dates": {"birth": 1646, "death": 1709},
        "location": "Prince George County, Virginia",
        "notes": "Prominent Virginia planter, merchant, and justice. Father of Elizabeth Bolling (wife of Edmund I).",
        "uncertainty": "probable",
        "sources": [{"url": "https://genealogyproofs.wordpress.com/blog-feed/page/3/", "label": "Virginia Historical Records"}]
    },
    "william_havercomb_1630": {
        "id": "william_havercomb_1630",
        "name": "William Havercomb",
        "type": "individual",
        "dates": {"birth": 1630, "death": None},
        "location": "Lower Norfolk County, Virginia",
        "notes": "Virginia planter who transported John Broadar [Browder] in 1674 (950-acre headright grant on Elizabeth River, VA Land Patents Bk 6 p. 526).",
        "uncertainty": "certain",
        "sources": [{"url": "https://docs.google.com/document/d/11JGUzWvoXJACDSofp-JVpTQJpD_eDOpYCMye2ge7cuk/edit", "label": "VA Land Patents Bk 6 p. 526"}]
    },
    "james_jopling_1635": {
        "id": "james_jopling_1635",
        "name": "James Jopling",
        "type": "individual",
        "dates": {"birth": 1635, "death": None},
        "location": "Lower Norfolk County, Virginia",
        "notes": "Neighboring landowner on Elizabeth River, VA (marked gum tree bound to Havercomb/Browder 1674 grant).",
        "uncertainty": "certain",
        "sources": [{"url": "https://docs.google.com/document/d/11JGUzWvoXJACDSofp-JVpTQJpD_eDOpYCMye2ge7cuk/edit", "label": "VA Land Patents Bk 6 p. 526"}]
    },
    "baron_hungerford_1404": {
        "id": "baron_hungerford_1404",
        "name": "Baron Robert Hungerford",
        "type": "individual",
        "dates": {"birth": 1404, "death": 1459},
        "location": "London / Wiltshire, England",
        "notes": "Second Baron Hungerford. Bequeathed a legacy of 53s 4d to William Browderer in his 1459 Will.",
        "uncertainty": "certain",
        "sources": [{"url": "https://docs.google.com/document/d/11JGUzWvoXJACDSofp-JVpTQJpD_eDOpYCMye2ge7cuk/edit", "label": "Will of Baron Hungerford 1459"}]
    }
}

nodes.update(new_nodes)
lineage["nodes"] = nodes

with open(json_file, "w", encoding="utf-8") as out:
    json.dump(lineage, out, indent=2, ensure_ascii=False)

print(f" ✓ Added {len(new_nodes)} new associate, in-law, and neighbor nodes to JSON model.")

# Now update HTML family tree
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

new_html_cards = """
            <!-- IN-LAWS, SPOUSES, NEIGHBORS & ACQUAINTANCES -->
            <div class="person-card branch" style="top: 230px; left: 1380px;"
                 data-name="Adam Hulme" data-dates="c. 1575" data-location="Manchester Cathedral Parish, Lancashire"
                 data-notes="Father of Marye Hulme (christened Feb 4, 1601). Native Manchester parishioner whose daughter married Robert Browder on Dec 26, 1623.">
                <div class="person-name">Adam Hulme</div>
                <div class="person-dates">c. 1575</div>
                <div class="person-location">Manchester Cathedral, Lancashire</div>
                <div class="person-notes">Father of Marye Hulme (m. 1623 Robert Browder)</div>
            </div>

            <div class="person-card branch" style="top: 140px; left: 1380px;"
                 data-name="Baron Robert Hungerford" data-dates="1404 — 1459" data-location="London / Wiltshire"
                 data-notes="2nd Baron Hungerford. Bequeathed a legacy of 53s 4d to William Browderer in his 1459 Will.">
                <div class="person-name">Baron Robert Hungerford</div>
                <div class="person-dates">1404 — 1459</div>
                <div class="person-location">London / Wiltshire</div>
                <div class="person-notes">Will legacy 53s 4d to William Browderer 1459</div>
            </div>

            <div class="person-card branch" style="top: 410px; left: 1380px;"
                 data-name="William Havercomb" data-dates="c. 1630" data-location="Lower Norfolk County, Virginia"
                 data-notes="Virginia planter who transported John Broadar [Browder] in 1674 (950-acre headright grant on Elizabeth River, VA Land Patents Bk 6 p. 526).">
                <div class="person-name">William Havercomb</div>
                <div class="person-dates">c. 1630</div>
                <div class="person-location">Lower Norfolk Co., VA</div>
                <div class="person-notes">Transported John Broadar 1674 (950-ac grant)</div>
            </div>

            <div class="person-card branch" style="top: 500px; left: 1380px;"
                 data-name="Lt. Arthur Jones & Susanna King" data-dates="c. 1660" data-location="Prince George County, Virginia"
                 data-notes="Parents of Elizabeth Jones (who married John Browder Sr. in 1715). Landowners on Gravelly Run.">
                <div class="person-name">Lt. Arthur Jones & Susanna King</div>
                <div class="person-dates">c. 1660</div>
                <div class="person-location">Prince George Co., VA</div>
                <div class="person-notes">Parents of Elizabeth Jones (m. 1715 John Sr.)</div>
            </div>
"""

if "Adam Hulme" not in html_content:
    html_content = html_content.replace('<!-- REVOLUTIONARY & RECOVERY LINE -->', new_html_cards + '\n            <!-- REVOLUTIONARY & RECOVERY LINE -->')
    print(" ✓ Injected associate & in-law person cards into HTML visual family tree.")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html_content)

print("✓ Associational and marital expansion complete!")

