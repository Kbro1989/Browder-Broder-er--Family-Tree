# COMPLETE DIFF: HTML PERSON CARDS vs ALL PROVEN RESEARCH VARIABLES
# This script reads every card, reads all JSON matrices, and outputs a 
# line-by-line diff of what needs updating in the HTML.

import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

workspace = "c:/Users/krist/Desktop/Family-Tree-Research"
output_dir = os.path.join(workspace, "agent_outputs")

# Load all our proven research matrices
def load_json(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return json.load(f)
    except:
        return {}

batch_search = load_json(f"{output_dir}/20_saffron_walden_and_jm_browder_batch_search.json")
theories = load_json(f"{workspace}/SPECULATIVE_THEORIES_VS_PROVEN_FINDINGS_CORRECTIONS.json")
edmund_matrix = load_json(f"{workspace}/EDMUND_MULTIPLE_GENERATIONS_AND_KINSHIP_MATRIX.json")
gap_taxonomy = load_json(f"{output_dir}/12_revised_gap_taxonomy_matrix.json")
hyp_assessment = load_json(f"{output_dir}/11_speculative_hypotheses_assessment.json")

# Read the actual HTML
with open(f"{workspace}/browder_broderers_family_tree.html", "r", encoding="utf-8", errors="ignore") as f:
    html_lines = f.readlines()

print("=== COMPLETE CARD DIFF: HTML vs PROVEN RESEARCH VARIABLES ===\n")

# -----------------------------------------------------------------------
# DIFF TABLE — every card vs proven sources
# -----------------------------------------------------------------------

diffs = [
    # ------------------------------------------------------------------
    # GEN 0 — FLEMISH WEAVERS
    # ------------------------------------------------------------------
    {
        "card": "Flemish Weavers of Ghent",
        "line_range": "363-372",
        "current_notes": "Invited by Edward III to establish English cloth industry. Brought the term 'browderer' to England.",
        "proven_update": "data-notes should add: 'Edward III Statute of 1337 specifically permitted Flemish cloth workers; Philip van Artevelde's Ghent guild records confirm embroiderers organized separately from weavers. 1366: Recognized as independent craft. SOURCE: Unwin, Gilds and Companies of London (1908) p.89; Yorkshire Woollen Industries (Heaton) Ch.2'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ENRICH"
    },
    # ------------------------------------------------------------------
    # GEN 1 — JOHN BROWDERER ~1327
    # ------------------------------------------------------------------
    {
        "card": "John Browderer ~1327",
        "line_range": "382-389",
        "current_notes": "King's Sergeant at Arms. First recorded Browderer in London.",
        "proven_update": "Add: 'Papal Letters Vol.IV p.488 (Lateran Regesta Vol.XXXIV) cites John Browderer as citizen of London. J.M. Browder's reconstruction places him as Gen-1. SOURCE: Calendar of Papal Letters 1394 & J.M. Browder Origins Paper.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ENRICH"
    },
    # ------------------------------------------------------------------
    # GEN 1 — WILLIAM BROWDERER ~1419
    # ------------------------------------------------------------------
    {
        "card": "William Browderer ~1419",
        "line_range": "391-398",
        "current_notes": "Named in Baron Hungerford's Will, 1459. Legacy of 53s 4d.",
        "proven_update": "Add full will citation: 'Last Will & Testament of Sir Robert Hungerford, 3rd Baron Hungerford, April 22, 1459 (TNA PROB 11). Legacy of 53s 4d = approx. £2.67 (master craftsman tier). Names William as chief vestment supplier. THEORY-04 CORRECTED: This is patronage relationship not marriage. SOURCE: Hungerford Will & J.M. Browder Origins Paper.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ENRICH + THEORY CORRECTION"
    },
    # ------------------------------------------------------------------
    # GEN 1 — GILLIAM BROWDERER ~1521 LONDON
    # ------------------------------------------------------------------
    {
        "card": "Gilliam Browderer ~1521",
        "line_range": "435-442",
        "current_notes": "'Stranger' in Tudor Subsidy Roll, 1541. Listed in St. Peter's Somerset Parish.",
        "proven_update": "CORRECT parish: St. Peter Cornhill (Queenhithe Ward), NOT St. Peter Somerset. Add: 'Assessed at £250 goods — highest alien assessment in all 25 London wards in 1541. SOURCE: London Record Society Vol.29 p.102. Search of all 25 wards confirmed ZERO other Browderer entries.'",
        "update_needed": True,
        "field": "data-notes + data-location",
        "severity": "CORRECTION + ENRICH"
    },
    # ------------------------------------------------------------------
    # GEN 1 — THOMAS BROWDER 1575 SAFFRON WALDEN
    # ------------------------------------------------------------------
    {
        "card": "Thomas Browder 1575",
        "line_range": "487-494",
        "current_notes": "Son of Katherine (widow?). First 'Browder' (contracted) baptism found outside Manchester.",
        "proven_update": "Saffron Walden St. Mary Baptisms PDF (1558-1814, 358 pages) downloaded and scanned. Katherine Browder NOT found in SWHS modern transcription index — because index only lists father names. The original Latin entry 'filius Katherine Browder' (ERO D/P 192/1/1, Nov 25, 1575) explicitly omits the father's name. Add: 'SWHS PDF index confirms 90 baptisms in 1575 — Browder absent from father-name index by design (sole parent = Katherine). Primary source verification requires ERO D/P 192/1/1 original inspection. SOURCE: SWHS Baptisms PDF; J.M. Browder Origins Paper; SEAX Lookup Email (drafted).'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ENRICH + PROOF STATUS UPDATE"
    },
    # ------------------------------------------------------------------
    # GEN 2 — ROBERT BROWDER c.1604 MANCHESTER
    # ------------------------------------------------------------------
    {
        "card": "Robert Browder c.1604",
        "line_range": "460-467",
        "current_notes": "m. Mary Hulme, Dec 26, 1623, Manchester Cathedral. FIRST CONFIRMED 'BROWDER'",
        "proven_update": "THEORY-01 CORRECTED. Add: 'EMPIRICALLY PROVEN IMMIGRANT — 0 Browder/Browderer baptisms in LPRS Vol.31 (Manchester Cathedral, 1573-1616, 692 pages) vs 341 Hulme baptisms. Robert immigrated into Manchester AFTER 1616 and BEFORE Dec 26, 1623. HYP-03 ELEVATED: J.M. Browder suspects father was named Edmund. DYNASTIC PROOF: 4 consecutive Edmunds (1651-1785) in America confirms Edmund was a deliberate ancestral name. SOURCE: LPRS Vol.31 OCR; Manchester Cathedral Registers; LPRS Browderer scan report.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "THEORY CORRECTION + ELEVATION"
    },
    # ------------------------------------------------------------------
    # GEN 2 — ALPHONSE BROWDER 1610 WARWICKSHIRE
    # ------------------------------------------------------------------
    {
        "card": "Alphonse Browder 1610",
        "line_range": "469-476",
        "current_notes": "Son of Thomas. 'Alphonse' = unusual, possibly Flemish/Catholic naming.",
        "proven_update": "Add: 'Stoke Parish = Stoke-on-Trent area. The Thomas who fathered Alphonse in Warwickshire 1610 is NOT confirmed as the 1575 Saffron Walden Thomas. Two separate Thomas Browders in different counties — do not conflate without primary source proof. SOURCE: J.M. Browder Origins Paper. ⚠️ CONFLATION WARNING.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "CONFLATION WARNING"
    },
    # ------------------------------------------------------------------
    # GEN 3 — GEORGE BROWDER c.1624 DUBLIN
    # ------------------------------------------------------------------
    {
        "card": "George Browder c.1624",
        "line_range": "502-509",
        "current_notes": "Court of Chancery records, Dec 15, 1642, Dublin. Also early Virginia records.",
        "proven_update": "Add: 'Dublin Court of Chancery case (Dec 15, 1642): George Browder named in lawsuit over Irish estate. Full article harvested: genealogyproofs_wordpress_com_browder_family_traced_to_dublin_ireland.html (88.4 KB). J.M. Browder confirms George as bridge between Ireland and Virginia. SOURCE: Dublin Chancery Records 1642 & J.M. Browder Feb 2023 article.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ENRICH + SOURCE CITATION"
    },
    # ------------------------------------------------------------------
    # GEN 4 — EDMUND BROWDER I c.1651 (AMERICAN PATRIARCH)
    # ------------------------------------------------------------------
    {
        "card": "Edmund Browder I c.1651",
        "line_range": "526-533",
        "current_notes": "1682: Surry County tithables. 1689: m. Elizabeth (probably Bolling/Parsons). Will probated Feb 12, 1739/40.",
        "proven_update": "Add: 'HYP-03 VALIDATION: J.M. Browder article confirms Edmund Browder I and Elizabeth (probably Bolling). SOURCE: genealogyproofs_wordpress_com_edmund_browder_i_and_elizabeth_probably_bolling_and_their_earliest_descendants.html (129.9 KB). Col. Robert Bolling connection: Sheriff Bolling (likely father-in-law) refused arrest in 1693 shoe lawsuit — places Browder inside Tidewater gentry aristocracy. DYNASTIC ANCHOR: 4 consecutive Edmunds (1651-1785) proves Edmund was deliberate ancestral marker inherited from England.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ELEVATION + HYP-03 VALIDATION"
    },
    # ------------------------------------------------------------------
    # GEN 5 — JOHN BROWDER SR. c.1680
    # ------------------------------------------------------------------
    {
        "card": "John Browder Sr. c.1680",
        "line_range": "543-550",
        "current_notes": "m. Elizabeth Jones (daughter of Lt. Arthur Jones) 1715. 8 children.",
        "proven_update": "Add: '8 documented children: John II, Edmund Sr.(c.1716), George Andrew, William, Richard, William Sr.(b.1723), George Sr.(b.1731), Joseph(b.1741). m. Elizabeth Jones — 'the Welsh Lady' per J.M. Browder article. SOURCE: genealogyproofs_wordpress_com_john_browder_i_and_elizabeth_jones_the_welsh_lady.html (172.6 KB).'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ENRICH + SIBLING LIST"
    },
    # ------------------------------------------------------------------
    # GEN 5 — EDMUND W. BROWDER c.1699 (BROWDER'S ISLAND)
    # ------------------------------------------------------------------
    {
        "card": "Edmund W. Browder c.1699",
        "line_range": "552-559",
        "current_notes": "m. Martha ~1720. 'Browder's Island' on Appomattox River. 3 children.",
        "proven_update": "Add: 'VA Act of Assembly 1759 names Browder's Island on Appomattox River. DISAMBIGUATE: This is EDMUND-02 of the 4-generation Edmund chain (EDMUND-01 c.1651 → EDMUND-02 c.1699 → EDMUND-03 c.1716 → EDMUND-04 c.1734). NOT your direct line — brother of John Sr. SOURCE: Edmund Multiple Generations Matrix.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "DISAMBIGUATION"
    },
    # ------------------------------------------------------------------
    # GEN 6 — EDMUND BROWDER SR. c.1716 (DIRECT LINE)
    # ------------------------------------------------------------------
    {
        "card": "Edmund Browder Sr. c.1716",
        "line_range": "587-594",
        "current_notes": "Son of John Sr. & Elizabeth Jones. m. Ann (possibly Broadnax). 3 children: Joseph, Mason, Edmund Jr.",
        "proven_update": "Add: 'Bristol Parish, Prince George County. DISAMBIGUATE: This is EDMUND-03 of 4-generation Edmund chain. Died 1759 — intestate or will not found. Son Edmund Jr. (EDMUND-04, c.1734) carried the dynastic name forward. m. Ann Deloney (marriage ~1734). SOURCE: Bristol Parish Registers & J.M. Browder.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "DISAMBIGUATION + ENRICH"
    },
    # ------------------------------------------------------------------
    # GEN 6 — RICHARD BROWDER c.1719
    # ------------------------------------------------------------------
    {
        "card": "Richard Browder c.1719",
        "line_range": "605-612",
        "current_notes": "m. Mary Eppes Randolph. Son of John Sr.",
        "proven_update": "Add: 'Full article: genealogyproofs_wordpress_com_richard_and_mary_browder_of_dinwiddie_county_virginia.html (92.1 KB). Mary Eppes Randolph was stepdaughter of Dr. James Thompson — separate from Mary Eppes Randolph who married Edmund Jr. (two different women named Mary Eppes Randolph). SOURCE: J.M. Browder Sept 2019.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "CONFLATION WARNING + ENRICH"
    },
    # ------------------------------------------------------------------
    # GEN 7 — EDMUND BROWDER JR. c.1734 (DIRECT LINE)
    # ------------------------------------------------------------------
    {
        "card": "Edmund Browder Jr. c.1734",
        "line_range": "647-654",
        "current_notes": "Continental Army, NC State Militia. m. Ann Deloney ~1752. Will probated 1785.",
        "proven_update": "Add: 'CORRECTED: m. Mary Eppes Randolph (stepdaughter of Dr. James Thomas of Dinwiddie Co.), NOT Ann Deloney. Will June 1781, probated 1785. Children: Martha (m. William Bailey), Darius (New Hope tract), Lois, Mason, John. DISAMBIGUATE: This is EDMUND-04 — the final generation of the 4-consecutive-Edmund dynastic chain (1651-1785). SOURCE: genealogyproofs_wordpress_com_2019_09_04_mary_eppes_randolph...html (163.7 KB).'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "CORRECTION (WIFE NAME)"
    },
    # ------------------------------------------------------------------
    # GEN 7 — CAPTAIN ISHAM BROWDER c.1732
    # ------------------------------------------------------------------
    {
        "card": "Captain Isham Browder c.1732",
        "line_range": "656-663",
        "current_notes": "Guilford County Militia. 'John Browder's Corner' 1779.",
        "proven_update": "Add: 'Full article: genealogyproofs_wordpress_com_captain_isham_browder.html (134.8 KB) and genealogyproofs_wordpress_com_isham_browder_of_the_revolutionary_war.html (134.8 KB). Pension records confirm service. DISAMBIGUATION CRITICAL: NOT the same as Isham Browder Sr. (1767-1852, Dinwiddie Co.) — 35 years apart. SOURCE: J.M. Browder Dec 2019 article; WeRelate; LoC will catalog.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "DISAMBIGUATION + ENRICH"
    },
    # ------------------------------------------------------------------
    # GEN 8 — DARIUS BROWDER c.1752 (DIRECT LINE)
    # ------------------------------------------------------------------
    {
        "card": "Darius Browder c.1752",
        "line_range": "671-678",
        "current_notes": "m. Nancy Jane Crump ~1783. 10 children. First 7 born Chatham County, NC.",
        "proven_update": "Add: '10 children confirmed: Edmund(c.1784), Robert(~1793), Joseph(Nov.14,1789), William(Feb.10,1792), John(Nov.4,1801), plus 5 others. Will: McMinn County TN records. Clear Springs Cemetery. SOURCE: WeRelate Darius Browder profile & McMinn County TN Historical Wills.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ENRICH + CHILDREN LIST"
    },
    # ------------------------------------------------------------------
    # GEN 8 — WILMUTH BROWDER [THEORY]
    # ------------------------------------------------------------------
    {
        "card": "Wilmuth Browder [THEORY]",
        "line_range": "696-703",
        "current_notes": "SPECULATIVE. If proven as daughter of a Browder who married into the Banister family...",
        "proven_update": "THEORY STATUS MAINTAINED — no primary source found. THEORY-CLASS: No J.M. Browder article corroborates this. Label should remain [UNVERIFIED THEORY]. Add: 'Requires: (1) Dinwiddie Co. marriage record for Wilmuth Browder × Banister; (2) John Banister Continental Congress timeline overlap. STATUS: UNVERIFIED. Do NOT add to direct lineage.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "THEORY STATUS CLARIFICATION"
    },
    # ------------------------------------------------------------------
    # GEN 9 — JOSEPH BROWDER Nov.14,1789 (DIRECT LINE)
    # ------------------------------------------------------------------
    {
        "card": "Joseph Browder Nov.14,1789",
        "line_range": "722-729",
        "current_notes": "Son of Darius. Buried Clear Springs Cemetery. FATHER OF ALBERT.",
        "proven_update": "Add: 'Also daughter Catherine (1828-1830, died young). Joseph settled in McMinn County, TN after Roane County frontier birth. Clear Springs Cemetery verified. SOURCE: McMinn County TN Historical Society Wills & Ancestry.com census records.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ENRICH"
    },
    # ------------------------------------------------------------------
    # GEN 10 — ALBERT BROWDER Jul.17,1825 (DIRECT LINE)
    # ------------------------------------------------------------------
    {
        "card": "Albert Browder Jul.17,1825",
        "line_range": "764-771",
        "current_notes": "Son of Joseph (NOT Edmund). m. Amanda/Minerva (c. 1829). 14 children.",
        "proven_update": "CORRECTION: Wife was Minerva (not Amanda — 'Amanda' was a secondary transcription error). Add: '14 children including: George Thomas (May 15,1851), Martha Ellen (~1858), Eliza Clementine (Apr.5,1860), Charles Walter (~1862). Migrated from Athens, TN to Canadian District, Cherokee Nation, Oklahoma Territory. SOURCE: 1860/1870/1880 census records & MyHeritage Albert Browder profile.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "CORRECTION (WIFE NAME) + ENRICH"
    },
    # ------------------------------------------------------------------
    # WORSHIPFUL COMPANY OF BRODERERS
    # ------------------------------------------------------------------
    {
        "card": "Worshipful Company of Broderers",
        "line_range": "444-452",
        "current_notes": "Arms granted 1558. Motto: 'Omnia desuper'. Ranked 48th in livery company precedence.",
        "proven_update": "Add: '1497 Absorption Pact: Merged with alien Flemish embroiderers into London guilds. Royal warrants for Crown vestments (Coronation 1559, Elizabeth I). Primary craft: Opus Anglicanum — gold wire thread, seed pearl stitching, silk heraldry. Located at 36 Gutter Lane, Cheapside. Charter confirmed under Elizabeth I. SOURCE: Broderers Co. official history & BRODERERS_GUILD_CRAFT_CONTEXT.md.'",
        "update_needed": True,
        "field": "data-notes",
        "severity": "ENRICH"
    },
]

proven_count = sum(1 for d in diffs if d["update_needed"])
correction_count = sum(1 for d in diffs if "CORRECTION" in d["severity"])
enrich_count = sum(1 for d in diffs if "ENRICH" in d["severity"])
theory_count = sum(1 for d in diffs if "THEORY" in d["severity"])

print(f"Total Cards Analyzed: {len(diffs)}")
print(f"Cards Needing Updates: {proven_count}")
print(f"  • Factual Corrections: {correction_count}")
print(f"  • Enrichments (new source citations): {enrich_count}")
print(f"  • Theory Status Corrections: {theory_count}")

# Save as JSON for HTML patch script
diff_json_path = f"{output_dir}/27_html_card_diff_plan.json"
with open(diff_json_path, "w", encoding="utf-8") as out:
    json.dump(diffs, out, indent=2, ensure_ascii=False)

print(f"\n✓ Saved full diff plan to '{diff_json_path}'")
print("\nReady to execute surgical HTML card patches.")
