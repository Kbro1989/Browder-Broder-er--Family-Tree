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

# Extract all person nodes
nodes = lineage.get("nodes", {})
person_list = []
for nid, nd in nodes.items():
    pname = nd.get("name", "")
    if pname and len(pname) > 3 and not pname.startswith("Worshipful") and not pname.startswith("Flemish"):
        clean_name = re.sub(r'\[.*?\]', '', pname).strip()
        person_list.append((nid, clean_name))

# Add extra key historical figures
person_list.extend([
    ("mary_hulme", "Mary Hulme"),
    ("elizabeth_parsons", "Elizabeth Parsons"),
    ("elizabeth_jones", "Elizabeth Jones"),
    ("peter_eppes", "Peter Eppes"),
    ("john_broadar", "John Broadar"),
    ("john_parr", "John Parr"),
    ("edmund_harrison", "Edmund Harrison")
])

# Collect all files in workspace
all_files = []

for item in os.listdir(workspace_dir):
    fpath = os.path.join(workspace_dir, item)
    if os.path.isfile(fpath) and not item.startswith("."):
        all_files.append((item, fpath, "root"))

for item in os.listdir(archive_dir):
    fpath = os.path.join(archive_dir, item)
    if os.path.isfile(fpath) and not item.startswith("."):
        all_files.append((f"downloaded_source_pages/{item}", fpath, "archive"))

print(f"=== MASTER FILE CROSS-REFERENCE ANALYSIS ACROSS {len(all_files)} WORKSPACE FILES ===")

file_matrix = {}

keywords_dict = {
    "Livery & Guilds": ["Broderer", "Broderers", "Weaver", "Weavers", "Livery", "Company of Broderers"],
    "Historical Eras": ["1327", "1394", "1419", "1459", "1541", "1604", "1611", "1623", "1664", "1674", "1682", "1739"],
    "Primary Record Types": ["Will", "Headright", "Deed", "Hearth Money", "Subsidy Roll", "Patent", "Register", "Chancery"],
    "Key Regions": ["London", "Manchester", "Lancashire", "Essex", "Suffolk", "Cornwall", "Tipperary", "Virginia", "Tennessee"]
}

for fname, fpath, fcategory in all_files:
    size_bytes = os.path.getsize(fpath)
    
    # Read file content safely
    try:
        with open(fpath, "r", encoding="utf-8", errors="ignore") as sf:
            raw_text = sf.read()
        
        text = re.sub(r'<[^>]+>', ' ', raw_text) if fname.endswith('.html') else raw_text
        text = re.sub(r'\s+', ' ', text)
        line_count = len(raw_text.splitlines())
    except Exception:
        text = ""
        line_count = 0

    matched_persons = []
    for nid, pname in person_list:
        first_n = pname.split()[0]
        last_n = pname.split()[-1] if len(pname.split()) > 1 else ""
        if last_n:
            if re.search(rf'\b{re.escape(first_n)}\s+(?:\w+\s+)?{re.escape(last_n)}\b', text, re.IGNORECASE):
                matched_persons.append(pname)
        else:
            if re.search(rf'\b{re.escape(pname)}\b', text, re.IGNORECASE):
                matched_persons.append(pname)

    matched_keywords = {}
    for cat, kws in keywords_dict.items():
        found_kws = [kw for kw in kws if re.search(rf'\b{re.escape(kw)}\b', text, re.IGNORECASE)]
        if found_kws:
            matched_keywords[cat] = found_kws

    file_matrix[fname] = {
        "file_name": fname,
        "category": fcategory,
        "size_bytes": size_bytes,
        "line_count": line_count,
        "persons_count": len(matched_persons),
        "persons_matched": matched_persons,
        "keywords_matched": matched_keywords
    }

# Save JSON Matrix
json_out = os.path.join(workspace_dir, "MASTER_FILE_CROSS_REFERENCE_MATRIX.json")
with open(json_out, "w", encoding="utf-8") as jout:
    json.dump(file_matrix, jout, indent=2, ensure_ascii=False)

# Build Markdown Report
md_out = os.path.join(workspace_dir, "MASTER_FILE_CROSS_REFERENCE_MATRIX.md")
with open(md_out, "w", encoding="utf-8") as mout:
    mout.write("# 🌐 MASTER WORKSPACE FILE CROSS-REFERENCE MATRIX\n\n")
    mout.write(f"Complete cross-reference of all **{len(all_files)} files** in the Family-Tree-Research repository.\n\n")
    
    mout.write("## 📁 Workspace Summary Statistics\n\n")
    mout.write(f"- **Total Files Analyzed:** `{len(all_files)}`  \n")
    mout.write(f"- **Primary Core Files (Root):** `{len([f for f in all_files if f[2] == 'root'])}`  \n")
    mout.write(f"- **Harvested Source Pages (Archive):** `{len([f for f in all_files if f[2] == 'archive'])}`  \n\n")
    
    mout.write("## 📄 Master File Cross-Reference Table\n\n")
    mout.write("| File Path | Size | Lines | Persons Matched | Key Guilds / Regions / Eras |\n")
    mout.write("|---|:---:|:---:|---|---|\n")
    
    for fname, data in sorted(file_matrix.items(), key=lambda x: x[1]["size_bytes"], reverse=True):
        size_str = f"{data['size_bytes']/1024:.1f} KB" if data['size_bytes'] < 1024*1024 else f"{data['size_bytes']/(1024*1024):.2f} MB"
        p_str = ", ".join(data['persons_matched'][:4]) + (f" (+{len(data['persons_matched'])-4} more)" if len(data['persons_matched']) > 4 else "") if data['persons_matched'] else "None"
        
        kw_flat = []
        for c, klist in data['keywords_matched'].items():
            kw_flat.extend(klist[:2])
        kw_str = ", ".join(kw_flat[:4]) if kw_flat else "None"
        
        file_url = os.path.join(workspace_dir, fname).replace('\\', '/')
        mout.write(f"| [`{fname}`](file:///{file_url}) | {size_str} | {data['line_count']} | {p_str} | {kw_str} |\n")
        
    mout.write("\n---\n\n")
    mout.write("## 🔍 Deep Entity Cross-Citations\n\n")
    
    for fname, data in file_matrix.items():
        if data['persons_matched']:
            file_url = os.path.join(workspace_dir, fname).replace('\\', '/')
            mout.write(f"### 📜 [`{fname}`](file:///{file_url})\n")
            mout.write(f"• **Persons Referenced:** {', '.join(data['persons_matched'])}\n")
            for c, klist in data['keywords_matched'].items():
                mout.write(f"• **{c}:** {', '.join(klist)}\n")
            mout.write("\n")

print(f"✓ Master File Cross-Reference Matrix saved to '{json_out}' and '{md_out}'!")

