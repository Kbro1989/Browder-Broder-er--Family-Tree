import os
import urllib.request
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")
pdf_dir = os.path.join(workspace_dir, "harvested_pdfs")
output_dir = os.path.join(workspace_dir, "agent_outputs")

os.makedirs(pdf_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("=== STEP 1: DOWNLOADING SAFFRON WALDEN BAPTISM TRANSCRIPTION PDF (1558-1814) ===")

swhs_pdf_url = "https://saffronwaldenhistory.org.uk/wp-content/uploads/2025/01/Baptisms-1558-1814-St.Marys-sorted-2025.pdf"
swhs_dest = os.path.join(pdf_dir, "Baptisms-1558-1814-St.Marys-sorted-2025.pdf")

try:
    print(f"Downloading PDF from: {swhs_pdf_url}")
    req = urllib.request.Request(swhs_pdf_url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        pdf_data = resp.read()
    with open(swhs_dest, "wb") as out:
        out.write(pdf_data)
    size_mb = os.path.getsize(swhs_dest) / (1024 * 1024)
    print(f" ✓ Saved PDF: 'Baptisms-1558-1814-St.Marys-sorted-2025.pdf' ({size_mb:.2f} MB)")
except Exception as e:
    print(f" ❌ Failed fetching SWHS PDF: {e}")

print("\n=== STEP 2: BATCH SEARCHING ALL HARVESTED J.M. BROWDER POSTS ===")

terms = ["katherine browder", "edmund browder", "robert browder", "1575"]

search_results = {}

for term in terms:
    search_results[term] = []

for fname in os.listdir(archive_dir):
    if fname.startswith("genealogyproofs_wordpress_com_") and fname.endswith(".html"):
        fpath = os.path.join(archive_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as sf:
                text = sf.read()
            text_clean = re.sub(r'<[^>]+>', ' ', text)
            text_clean = re.sub(r'\s+', ' ', text_clean)
            
            for term in terms:
                matches = re.finditer(re.escape(term), text_clean, re.IGNORECASE)
                for match in matches:
                    st = max(0, match.start() - 150)
                    en = min(len(text_clean), match.end() + 150)
                    snippet = text_clean[st:en].strip()
                    search_results[term].append({
                        "file": fname,
                        "matched_term": term,
                        "snippet": snippet
                    })
        except Exception:
            pass

print(f"\nSearch Results Summary:")
for term, hits in search_results.items():
    print(f"  • Term '{term}': {len(hits)} matches found across posts")

# Save JSON
json_out = os.path.join(output_dir, "20_saffron_walden_and_jm_browder_batch_search.json")
with open(json_out, "w", encoding="utf-8") as jout:
    json.dump(search_results, jout, indent=2, ensure_ascii=False)

# Save Markdown Report
md_out = os.path.join(output_dir, "21_saffron_walden_and_jm_browder_batch_search.md")
with open(md_out, "w", encoding="utf-8") as mout:
    mout.write("# 🔍 SAFFRON WALDEN & J.M. BROWDER BATCH SEARCH REPORT\n\n")
    mout.write("Batch search report scanning all 35 harvested John Mark Browder blog posts for key terms: `katherine browder`, `edmund browder`, `robert browder`, `1575`.\n\n")
    
    for term, hits in search_results.items():
        mout.write(f"## 📌 Matches for Term: `{term}` ({len(hits)} Hits)\n\n")
        for idx, hit in enumerate(hits[:15], 1): # Top 15 snippets per term
            mout.write(f"### [{idx}] Source File: `{hit['file']}`\n")
            mout.write(f"• **Verbatim Context Snippet:** \"*{hit['snippet']}*\"  \n\n")
        if len(hits) > 15:
            mout.write(f"*(... plus {len(hits) - 15} additional matches recorded in JSON)*\n\n")
        mout.write("---\n\n")

print(f"✓ Saved Batch Search Report to '{json_out}' and '{md_out}'!")

