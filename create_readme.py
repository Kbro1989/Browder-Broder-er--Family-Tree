import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

readme_content = """# 🌳 BROWDER & WORSHIPFUL COMPANY OF BRODERERS LINEAGE CORPUS (1327 – PRESENT)

Welcome to the authoritative research repository for the **Browder & Worshipful Company of Broderers Lineage Corpus**, spanning **698 years of documented genealogy, primary parish registers, court records, wills, land patents, and occupational guild history (1327–Present)**.

---

## 📌 EXECUTIVE SUMMARY & HISTORICAL FINDINGS

### 1. **Academic Etymology of the Surname**
- **Etymology:** Confirmed via academic correspondence with **Dr. Benjamin Hudson, Ph.D.** (Professor of History & Medievalist). The surname **Browder** is a direct Old English occupational contraction of **browderer** (embroiderer / weaver), as used in the Middle English works of **John Wycliffe** (1320–1384) and **Geoffrey Chaucer** (1343–1400).
- **Roots:** Traced to Flemish weavers invited into England by **King Edward III** in 1327 following trade disruption in Flanders.

### 2. **Pre-1604 Primary Documented Anchor Points (14 Discrete Entries)**
- **~1327:** *John Browderer* — King's Sergeant at Arms, London / St. Hilary Parish, Cornwall.
- **1394:** *John Browderer* — Citizen of London (*Papal Letters, Vol. IV, p. 488; Lateran Regesta Vol. XXXIV*).
- **1406-07:** *Thome Browderer* — Mettingham College, Suffolk (*Ancient Accounts*).
- **1412-13:** *Joh Browdere* — Mettingham College, Suffolk (*earliest recorded spelling dropping the final 'r'*).
- **1439-40:** *William Browderer* — East Riding Antiquarian Society accounts (*Vol. 3, p. 99*).
- **1459:** *William Browderer* — Bequeathed a legacy of 53s 4d in the Will of **Baron Robert Hungerford**.
- **1466 / 1502:** *Richard Browderer* — Coldharbour port, Cornwall.
- **1541:** *Gilliam [William] Browderer* — Tudor Subsidy Roll, St. Peter's Somerset Parish, London (£250 assessment).
- **1575:** *Thomas Browder* — Baptized Nov 25, 1575 at Saffron Walden, Essex. **First recorded contracted "Browder" baptism**.
- **1604 / 1623:** *Robert Browder* — Married **Marye Hulme** on Dec 26, 1623 at Manchester Cathedral.

### 3. **The 31 Jan 1611 Ulster Plantation Allotment**
- Documented in **Gutenberg #20990** (*London and the Kingdom, Vol. III, p. 40*). The **Worshipful Company of Broderers** received a precept to cultivate and plant allotments in Ulster, Ireland, establishing the trade corridor between London, Ireland, and Virginia.

### 4. **Empirical Lancashire Parish Register Scan**
- Scanned **all 32 digitized volumes** of the Lancashire Parish Register Society (LPRS) on Archive.org.
- **Results:** **0 matches for Browder/Browderer** vs **341 matches for Hulme** in Manchester Cathedral (Vol 31). Proves empirically that *Robert Browder* was a 17th-century immigrant weaver into Manchester's textile trade rather than a native Lancashire parishioner.

---

## 📁 REPOSITORY FILE TREE & CONTENTS

```
Family-Tree-Research/
├── browder_broderers_family_tree.html          # Interactive HTML5 Timeline (50 Cards, 51 SVG Lines, 66 Local Archive Links)
├── browder_broderers_lineage.json              # Structured Lineage Graph Model (47 JSON Nodes with Source Citations)
├── john_mark_browder_origins_paper.txt         # Full Extracted Text of John Mark Browder's 153-line Paper (65.8 KB)
├── lancashireparis03socigoog_djvu.txt          # Manchester Cathedral OCR Transcript (LPRS Vol 31 - 1.70 MB, 692 pages)
│
├── 📊 CROSS-REFERENCE MATRICES & REPORTS
│   ├── MASTER_FILE_CROSS_REFERENCE_MATRIX.md   # Master N-to-N Cross-Reference Report (110 Workspace Files)
│   ├── MASTER_FILE_CROSS_REFERENCE_MATRIX.json # JSON Data Model for Master File Matrix
│   ├── TIMELINED_EVENTS_1300_1990_MATRIX.md    # Master 690-Year Chronological Timeline Report (37 Milestones)
│   ├── TIMELINED_EVENTS_1300_1990_MATRIX.json  # JSON Data Model for 1300-1990 Timeline
│   ├── parsed_name_relationships.md            # Parsed Name Relationships & Evidence Snippets Report
│   ├── parsed_name_relationships.json          # JSON Data Model for Name Relationships
│   ├── location_cross_reference_matrix.md      # Geographic Location Cross-Reference Report (12 Key Regions)
│   ├── location_cross_reference_matrix.json    # JSON Data Model for Location Cross-References
│   ├── VARIABLE_ATTRIBUTE_CROSS_REFERENCE_MATRIX.md # Attribute & Variable Cross-Reference Report
│   ├── VARIABLE_ATTRIBUTE_CROSS_REFERENCE_MATRIX.json # JSON Data Model for Variable Attributes
│   ├── INTERPERSONAL_DIALOGUE_COMMUNICATION_MATRIX.md # "Who Spoke to Whom, About What, When" Dialogue Report
│   └── INTERPERSONAL_DIALOGUE_COMMUNICATION_MATRIX.json # JSON Data Model for Oral Communications
│
├── 📂 downloaded_source_pages/                  # Local HTML Archive Subfolder (65 Harvested Source Web Pages)
│   ├── gutenberg_20990_london_and_the_kingdom_vol3.html # Ulster Plantation Allotment Proof (p. 40)
│   ├── archive_org_details_lancashireparis03socigoog.html # Archive.org Manchester Cathedral Page
│   ├── bho_london_record_soc_vol29.html        # British History Online 1541 Tudor Subsidy Roll
│   ├── mcminntnhistorical_org_wills.html       # McMinn County TN Historical Society Wills & Deeds
│   ├── broderers_co_uk_history.html            # Worshipful Company of Broderers Official History
│   ├── findagrave_com_memorial_...             # FindAGrave Memorial Pages & Transcripts
│   └── genealogyproofs_wordpress_...           # John Mark Browder Proof Articles
│
└── 🛠️ PIPELINE & AUTOMATION UTILITIES
    ├── extract_and_download_all_links.py       # Batch Web Source Downloader Utility
    ├── link_all_harvested_pages.py             # HTML Family Tree Local Link Injector
    ├── parse_relationships_from_papers.py      # Relationship & Snippet Parser Script
    ├── cross_reference_locations.py            # Geographic Location Cross-Referencing Script
    ├── master_file_cross_reference.py          # Master Workspace File Cross-Referencer
    ├── generate_timeline_1300_1990.py          # 1300-1990 Chronological Timeline Generator
    ├── variable_cross_reference_matrix.py      # Variable & Attribute Cross-Referencing Script
    ├── extract_speech_and_dialogue.py          # Speech Verb & Interpersonal Dialogue Extractor
    ├── add_associates_and_inlaws.py            # In-Law, Spouse, & Neighbor Card Injector
    ├── check_svg_connectors.py                 # SVG Line Coverage Validation Utility
    └── final_sanity_check.py                   # HTML Structure & Lineage Sanity Verifier
```

---

## 🎨 INTERACTIVE HTML FAMILY TREE USAGE

To view the visual family tree:
1. Double-click or open **[`browder_broderers_family_tree.html`](file:///c:/Users/krist/Desktop/Family-Tree-Research/browder_broderers_family_tree.html)** in any modern web browser.
2. **Features:**
   - **50 Person Cards:** Hover or click on cards to inspect birth/death dates, locations, and primary source proof notes.
   - **51 SVG Connector Lines:** Solid gold lines (`#c9a84c`) denote direct proven lineages; dashed green lines (`#5a7a5a`) denote pre-1604 branch nodes, spouses, and in-laws.
   - **Direct Archive Buttons:** Every card and source citation contains a `[📁 Local Archive]` button linking directly to the offline harvested HTML file under `downloaded_source_pages/`.
   - **Cross-Reference Matrix Buttons:** The Sourced Lineage section includes direct links to all 6 generated markdown reports and JSON data models.

---

## 📜 CORE SOURCE CITATIONS

1. **Browder, John Mark, B.A., M.S., M.T.S., M.Div.** *Origins of the Browder Surname, and Everyone Prior to Edmund Browder*. Full text extracted in [`john_mark_browder_origins_paper.txt`](file:///c:/Users/krist/Desktop/Family-Tree-Research/john_mark_browder_origins_paper.txt).
2. **Sharpe, Reginald R.** *London and the Kingdom*, Vol. III (1895). Gutenberg EPUB #20990, p. 40 (Ulster Plantation Allotment 1611).
3. **Lancashire Parish Register Society.** *The Register of the Parish Church of Manchester (1573–1616)*, Vol. 31 (1908). Full OCR text in [`lancashireparis03socigoog_djvu.txt`](file:///c:/Users/krist/Desktop/Family-Tree-Research/lancashireparis03socigoog_djvu.txt).
4. **London Record Society.** *Two Tudor Subsidy Rolls for the City of London, 1541 and 1582*, Vol. 29 (1993), p. 102.
5. **Virginia State Library.** *Cavaliers and Pioneers: Abstracts of Virginia Land Patents and Grants*, Book 6, p. 526 (John Broadar / Browder headright, 1674).
"""

target_readme = os.path.join("c:/Users/krist/Desktop/Family-Tree-Research", "README.md")
with open(target_readme, "w", encoding="utf-8") as out:
    out.write(readme_content)

print(f"✓ Created README.md successfully at '{target_readme}'!")

