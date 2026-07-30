import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")
json_model = os.path.join(workspace_dir, "browder_broderers_lineage.json")
paper_file = os.path.join(workspace_dir, "john_mark_browder_origins_paper.txt")

with open(json_model, "r", encoding="utf-8") as f:
    lineage = json.load(f)

# Define target geographic locations
locations_db = {
    "London, England": [
        "London", "Queenhithe", "St. Peter Somerset", "St. Giles", "Cripplegate",
        "St. Botolph", "Aldersgate", "Southwark", "Bermondsey", "Cheapside", "Gutter Lane"
    ],
    "Manchester, Lancashire, England": [
        "Manchester", "Cathedral", "Lancashire", "St. Mary, St. Denys"
    ],
    "Saffron Walden, Essex, England": [
        "Saffron Walden", "Essex", "St. Mary The Virgin"
    ],
    "Suffolk & Norfolk, England": [
        "Suffolk", "Mettingham", "Brockdish", "Norwich", "Norfolk"
    ],
    "Cornwall, England": [
        "Cornwall", "St. Hilary", "Coldharbour", "Trevarthian"
    ],
    "Warwickshire & Yorkshire, England": [
        "Warwickshire", "Stoke Parish", "Yorkshire", "East Riding", "Halifax"
    ],
    "County Tipperary & Cork, Ireland": [
        "Tipperary", "Ballynoran", "Shunraghan", "Iffa and Offa", "Cork", "Clonmel"
    ],
    "Dublin, Ireland": [
        "Dublin", "Chancery Court"
    ],
    "Ulster Plantation, Ireland": [
        "Ulster", "Plantation", "1611"
    ],
    "Lower Norfolk & Surry Co., Virginia": [
        "Lower Norfolk", "Elizabeth River", "Surry County", "Virginia", "James Fort", "Jamestown"
    ],
    "Prince George & Dinwiddie Co., Virginia": [
        "Prince George", "Charles City", "Gravelly Run", "Appomattox", "Blackwater", "Bristol Parish", "Browder's Island"
    ],
    "Chowan & Albemarle, North Carolina": [
        "North Carolina", "Chowan", "Albemarle", "Roanoke"
    ],
    "McMinn County, Tennessee": [
        "McMinn", "Tennessee", "Pond Creek"
    ]
}

# Load source files
sources_to_parse = [
    ("John Mark Browder Origins Paper", paper_file)
]

for fname in os.listdir(archive_dir):
    fpath = os.path.join(archive_dir, fname)
    if os.path.isfile(fpath) and os.path.getsize(fpath) > 100:
        sources_to_parse.append((f"Local HTML Source ({fname})", fpath))

print(f"=== CROSS REFERENCING LOCATIONS ACROSS {len(sources_to_parse)} SOURCE FILES ===")

location_matches = {loc: [] for loc in locations_db}

for loc_name, keywords in locations_db.items():
    kw_pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, keywords)) + r')\b', re.IGNORECASE)
    
    for source_label, src_path in sources_to_parse:
        try:
            with open(src_path, "r", encoding="utf-8", errors="ignore") as sf:
                raw_text = sf.read()
            
            text = re.sub(r'<[^>]+>', ' ', raw_text)
            text = re.sub(r'\s+', ' ', text)
            
            for match in kw_pattern.finditer(text):
                st = max(0, match.start() - 150)
                en = min(len(text), match.end() + 150)
                snippet = text[st:en].strip()
                
                # Identify associated person names in the same snippet
                names_in_snippet = []
                for node_id, node in lineage.get("nodes", {}).items():
                    pname = node.get("name", "")
                    if pname and len(pname) > 3:
                        clean_pname = re.sub(r'\[.*?\]', '', pname).strip()
                        first_n = clean_pname.split()[0]
                        if first_n in snippet and len(first_n) > 2:
                            names_in_snippet.append(clean_pname)
                
                location_matches[loc_name].append({
                    "keyword_matched": match.group(0),
                    "source": source_label,
                    "file_name": os.path.basename(src_path),
                    "snippet": snippet,
                    "associated_persons": list(set(names_in_snippet))
                })
        except Exception:
            pass

# Save JSON matrix
json_out = os.path.join(workspace_dir, "location_cross_reference_matrix.json")
with open(json_out, "w", encoding="utf-8") as jout:
    json.dump(location_matches, jout, indent=2, ensure_ascii=False)

# Build Markdown Report
md_out = os.path.join(workspace_dir, "location_cross_reference_matrix.md")
with open(md_out, "w", encoding="utf-8") as mout:
    mout.write("# 📍 GEOGRAPHIC LOCATION CROSS-REFERENCE MATRIX\n\n")
    mout.write("Mapping of historical geographic locations across primary sources, research papers, and person cards.\n\n")
    
    for loc_name, matches in location_matches.items():
        mout.write(f"## 📍 {loc_name} ({len(matches)} Evidence Snippets Found)\n\n")
        if not matches:
            mout.write("*No direct location snippets found.*\n\n")
            continue
            
        # Group by source file to keep concise
        sources_seen = {}
        for m in matches:
            sf = m["source"]
            if sf not in sources_seen:
                sources_seen[sf] = []
            sources_seen[sf].append(m)
            
        for sf, s_matches in list(sources_seen.items())[:5]: # Top 5 source groups
            mout.write(f"### 📄 {sf}\n")
            for m in s_matches[:3]: # Top 3 snippets per source
                persons_str = ", ".join(m["associated_persons"]) if m["associated_persons"] else "General Parish / Regional Context"
                mout.write(f"• **Keyword:** `{m['keyword_matched']}` | **Persons Mentioned:** *{persons_str}*\n")
                mout.write(f"• **Context:** \"... {m['snippet']} ...\"\n\n")
        mout.write("---\n\n")

print(f"✓ Location cross-reference matrix saved to '{json_out}' and '{md_out}'!")

