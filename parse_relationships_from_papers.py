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

# Extract person names from JSON nodes
person_names = []
for node_id, node in lineage.get("nodes", {}).items():
    name = node.get("name")
    if name and not name.startswith("Worshipful") and not name.startswith("Flemish"):
        # Clean bracketed text like Gilliam [William] -> Gilliam, William
        clean_name = re.sub(r'\[.*?\]', '', name).strip()
        person_names.append((node_id, clean_name, name))

# Add key historic figures / spouses
extra_names = [
    ("mary_hulme", "Mary Hulme", "Mary Hulme"),
    ("elizabeth_parsons", "Elizabeth Parsons", "Elizabeth Parsons"),
    ("elizabeth_jones", "Elizabeth Jones", "Elizabeth Jones"),
    ("peter_eppes", "Peter Eppes", "Peter Eppes"),
    ("john_parr", "John Parr", "John Parr"),
    ("edmund_harrison", "Edmund Harrison", "Edmund Harrison"),
    ("john_broadar", "John Broadar", "John Broadar")
]

for item in extra_names:
    if item not in person_names:
        person_names.append(item)

print(f"=== PARSING RELATIONSHIPS FOR {len(person_names)} PERSON NAMES ACROSS RESEARCH PAPERS ===")

# Build list of text files to search
sources_to_parse = [
    ("John Mark Browder Origins Paper", paper_file)
]

for fname in os.listdir(archive_dir):
    fpath = os.path.join(archive_dir, fname)
    if os.path.isfile(fpath) and os.path.getsize(fpath) > 100:
        sources_to_parse.append((f"Local HTML Source ({fname})", fpath))

relationship_keywords = [
    "father", "mother", "son", "daughter", "married", "wife", "husband",
    "brother", "sister", "will", "bequeath", "legacy", "headright", "witness",
    "baptized", "christened", "buried", "grant", "deed", "court", "descendant", "ancestor"
]

parsed_results = {}

for node_id, clean_name, full_name in person_names:
    parsed_results[node_id] = {
        "node_id": node_id,
        "full_name": full_name,
        "clean_name": clean_name,
        "matches": []
    }
    
    # Create search patterns (e.g., "John Browder", "John Browderer", "Edmund Browder")
    first_part = clean_name.split()[0]
    last_part = clean_name.split()[-1] if len(clean_name.split()) > 1 else ""
    
    # Simple regex pattern for the person's name
    if last_part:
        pattern = re.compile(rf'\b{re.escape(first_part)}\s+(?:\w+\s+)?{re.escape(last_part)}\b', re.IGNORECASE)
    else:
        pattern = re.compile(rf'\b{re.escape(clean_name)}\b', re.IGNORECASE)
        
    for source_label, src_path in sources_to_parse:
        try:
            with open(src_path, "r", encoding="utf-8", errors="ignore") as sf:
                raw_text = sf.read()
            
            # Clean HTML tags if HTML
            text = re.sub(r'<[^>]+>', ' ', raw_text)
            text = re.sub(r'\s+', ' ', text)
            
            for match in pattern.finditer(text):
                st = max(0, match.start() - 150)
                en = min(len(text), match.end() + 150)
                snippet = text[st:en].strip()
                
                # Check for relationship keywords in snippet
                detected_rel = [kw for kw in relationship_keywords if kw in snippet.lower()]
                
                parsed_results[node_id]["matches"].append({
                    "source": source_label,
                    "file_name": os.path.basename(src_path),
                    "match_text": match.group(0),
                    "snippet": snippet,
                    "relationship_cues": detected_rel
                })
        except Exception:
            pass

# Save JSON results
json_out = os.path.join(workspace_dir, "parsed_name_relationships.json")
with open(json_out, "w", encoding="utf-8") as jout:
    json.dump(parsed_results, jout, indent=2, ensure_ascii=False)

# Build Markdown Report
md_out = os.path.join(workspace_dir, "parsed_name_relationships.md")
with open(md_out, "w", encoding="utf-8") as mout:
    mout.write("# 📜 PARSED NAME RELATIONSHIPS & EVIDENCE MATRIX\n\n")
    mout.write("Extracted relationships and textual snippets across all research papers and downloaded primary sources.\n\n")
    
    for node_id, data in parsed_results.items():
        fname = data["full_name"]
        matches = data["matches"]
        mout.write(f"## 👤 {fname} ({len(matches)} Mentions Found)\n\n")
        
        if not matches:
            mout.write("*No direct textual mentions found in harvested papers.*\n\n")
            continue
            
        for idx, m in enumerate(matches[:8], 1): # Top 8 snippets per person
            cues = ", ".join(m["relationship_cues"]) if m["relationship_cues"] else "general reference"
            mout.write(f"**[{idx}] {m['source']}**  \n")
            mout.write(f"• **Relationship Cues:** `{cues}`  \n")
            mout.write(f"• **Context Snippet:** \"... {m['snippet']} ...\"  \n\n")
        mout.write("---\n\n")

print(f"✓ Parsed relationships saved to '{json_out}' and '{md_out}'!")

