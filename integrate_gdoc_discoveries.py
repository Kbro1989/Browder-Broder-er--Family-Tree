import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

json_path = "browder_broderers_lineage.json"

with open(json_path, "r", encoding="utf-8") as f:
    lineage_data = json.load(f)

nodes = lineage_data.get("nodes", {})

# Add new nodes from John Mark Browder paper
new_nodes = {
    "matthew_browder_1610": {
        "id": "matthew_browder_1610",
        "name": "Matthew Browder",
        "type": "individual",
        "dates": {
            "birth": 1610,
            "death": None
        },
        "location": "St. Giles Cripplegate, London, England",
        "notes": "Father of Katherine Browder (bap. Oct 26, 1634, St. Giles Cripplegate, London). Documented 17th-century London Browder cluster.",
        "uncertainty": "certain",
        "sources": [
            {
                "url": "https://docs.google.com/document/d/11JGUzWvoXJACDSofp-JVpTQJpD_eDOpYCMye2ge7cuk/edit",
                "label": "John Mark Browder Paper (p. 101)"
            }
        ]
    },
    "john_broadar_1674": {
        "id": "john_broadar_1674",
        "name": "John Broadar [Browder]",
        "type": "individual",
        "dates": {
            "birth": 1642,
            "death": None
        },
        "location": "Lower Norfolk County, Virginia",
        "notes": "Headright transported by William Havercomb (950-acre grant on Elizabeth River, VA Land Patents Bk 6, p. 526, Sept 23, 1674). Likely father or uncle of Edmund I.",
        "uncertainty": "probable",
        "sources": [
            {
                "url": "https://docs.google.com/document/d/11JGUzWvoXJACDSofp-JVpTQJpD_eDOpYCMye2ge7cuk/edit",
                "label": "John Mark Browder Paper (p. 113-124)"
            }
        ]
    }
}

nodes.update(new_nodes)
lineage_data["nodes"] = nodes

with open(json_path, "w", encoding="utf-8") as out:
    json.dump(lineage_data, out, indent=2, ensure_ascii=False)

print("✓ Updated browder_broderers_lineage.json with Matthew Browder (1610) and John Broadar (1674) nodes!")

