import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")
json_model = os.path.join(workspace_dir, "browder_broderers_lineage.json")

with open(json_model, "r", encoding="utf-8") as f:
    lineage = json.load(f)

# Define key variables / attributes to cross-reference
variables_registry = {
    "Person Node IDs": [
        "john_browderer_1327", "john_browderer_1394", "thome_browderer_1406", "joh_browdere_1412",
        "william_browderer_1419", "richard_browderer_1466", "gilliam_browderer_1521", "thomas_browder_1575",
        "alphonse_browder_1610", "robert_browder_1604", "mary_hulme_1601", "thomas_browder_1624",
        "george_browder_1624", "john_broadar_1674", "edmund_browder_1651", "elizabeth_parsons_1655",
        "john_browder_1690", "elizabeth_jones_1695", "edmund_w_browder_1699", "george_andrew_browder_1700",
        "william_browder_1702", "edmund_browder_sr_1716", "edmund_browder_jr_1740", "captain_isham_browder_1747",
        "lt_joseph_browder_1750", "jesse_browder_1752", "charles_browder_1754", "darius_browder_1785",
        "joseph_browder_1789", "albert_browder_1830", "george_thomas_browder_1860", "albert_edgar_browder_1890",
        "paul_eugene_browder_1920", "kevin_browder_1_1955", "kevin_browder_2_1985"
    ],
    "HTML Data Attributes": [
        "data-name", "data-dates", "data-location", "data-notes", "person-card", "connector", "direct", "branch"
    ],
    "Primary Record Identifiers": [
        "20990", "Papal Letters", "Lateran Regesta", "Tudor Subsidy Roll", "Hungerford",
        "lancashireparis03socigoog", "Land Patents Book 6", "Hearth Money", "Deed Book", "Statutes at Large"
    ],
    "Geographic Locations": [
        "London", "Queenhithe", "Manchester", "Lancashire", "Saffron Walden", "Suffolk",
        "Coldharbour", "Tipperary", "Dublin", "Elizabeth River", "Gravelly Run", "Appomattox", "McMinn"
    ],
    "Guilds & Insignia": [
        "Worshipful Company of Broderers", "Worshipful Company of Weavers", "Master John Parr",
        "Master Edmund Harrison", "Flemish Weavers", "Ulster Plantation"
    ]
}

# Collect all files
all_files = []
for item in os.listdir(workspace_dir):
    fpath = os.path.join(workspace_dir, item)
    if os.path.isfile(fpath) and not item.startswith("."):
        all_files.append((item, fpath, "root"))

for item in os.listdir(archive_dir):
    fpath = os.path.join(archive_dir, item)
    if os.path.isfile(fpath) and not item.startswith("."):
        all_files.append((f"downloaded_source_pages/{item}", fpath, "archive"))

print(f"=== CROSS-REFERENCING ALL VARIABLES ACROSS {len(all_files)} FILES ===")

variable_matches = {}

for cat_name, var_list in variables_registry.items():
    variable_matches[cat_name] = {}
    for var in var_list:
        variable_matches[cat_name][var] = []
        var_pattern = re.compile(rf'\b{re.escape(var)}\b', re.IGNORECASE)
        
        for fname, fpath, fcat in all_files:
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as sf:
                    raw_text = sf.read()
                
                text = re.sub(r'<[^>]+>', ' ', raw_text) if fname.endswith('.html') else raw_text
                text = re.sub(r'\s+', ' ', text)
                
                matches = list(var_pattern.finditer(text))
                if matches:
                    variable_matches[cat_name][var].append({
                        "file_name": fname,
                        "category": fcat,
                        "occurrences": len(matches)
                    })
            except Exception:
                pass

# Save JSON Matrix
json_out = os.path.join(workspace_dir, "VARIABLE_ATTRIBUTE_CROSS_REFERENCE_MATRIX.json")
with open(json_out, "w", encoding="utf-8") as jout:
    json.dump(variable_matches, jout, indent=2, ensure_ascii=False)

# Build Markdown Report
md_out = os.path.join(workspace_dir, "VARIABLE_ATTRIBUTE_CROSS_REFERENCE_MATRIX.md")
with open(md_out, "w", encoding="utf-8") as mout:
    mout.write("# 🔬 VARIABLE & ATTRIBUTE CROSS-REFERENCE MATRIX\n\n")
    mout.write(f"Complete cross-reference of all key variables, attributes, node IDs, and record identifiers across **{len(all_files)} workspace files** and HTML dumps.\n\n")
    
    for cat_name, var_dict in variable_matches.items():
        mout.write(f"## 📌 {cat_name}\n\n")
        mout.write("| Variable / Attribute | Total Files Found | Total Occurrences | Top File Hits |\n")
        mout.write("|---|:---:|:---:|---|\n")
        
        for var, file_hits in var_dict.items():
            total_files = len(file_hits)
            total_occ = sum(h["occurrences"] for h in file_hits)
            top_files = ", ".join([f"`{h['file_name']}` ({h['occurrences']}x)" for h in sorted(file_hits, key=lambda x: x['occurrences'], reverse=True)[:3]]) if file_hits else "None"
            
            mout.write(f"| `{var}` | {total_files} | {total_occ} | {top_files} |\n")
        mout.write("\n---\n\n")

print(f"✓ Variable cross-reference matrix saved to '{json_out}' and '{md_out}'!")

