import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
pdf_path = os.path.join(workspace_dir, "harvested_pdfs", "Baptisms-1558-1814-St.Marys-sorted-2025.pdf")
output_dir = os.path.join(workspace_dir, "agent_outputs")

print("=== DEEP SEARCHING SAFFRON WALDEN BAPTISM PDF (1558-1814) ===")

pdf_matches = []

try:
    import pypdf
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total Pages in SWHS PDF: {total_pages}")
    
    for idx, page in enumerate(reader.pages):
        text = page.extract_text()
        if "1575" in text or "Browd" in text or "Brod" in text or "Katherine" in text:
            lines = text.split("\n")
            for line in lines:
                if re.search(r'\b(1575|Browd|Brod|Broau|Katherine)\b', line, re.IGNORECASE):
                    pdf_matches.append({"page": idx+1, "line": line.strip()})
except Exception as e:
    print(f"pypdf not available or error: {e}, using string buffer scan...")
    with open(pdf_path, "rb") as pf:
        raw_pdf = pf.read()
    strings = re.findall(b"[a-zA-Z0-9\s\.,\-\/]{4,}", raw_pdf)
    for s in strings:
        st_str = s.decode('utf-8', errors='ignore')
        if "1575" in st_str or "Browd" in st_str or "Katherine" in st_str:
            pdf_matches.append({"page": 0, "line": st_str.strip()})

print(f"\nMatches for 1575: {sum(1 for m in pdf_matches if '1575' in m['line'])}")
print(f"Matches for Katherine: {sum(1 for m in pdf_matches if 'Katherine' in m['line'])}")
print(f"Matches for Browd/Brod/Broau: {sum(1 for m in pdf_matches if 'Browd' in m['line'] or 'Brod' in m['line'] or 'Broau' in m['line'])}")

print("\n--- SAMPLE 1575 MATCHES ---")
for m in pdf_matches[:10]:
    print(f"Page {m['page']}: {m['line']}")

print("\n--- SAMPLE BROWD/BROD MATCHES ---")
for m in pdf_matches:
    if "Browd" in m['line'] or "Brod" in m['line']:
        print(f"Page {m['page']}: {m['line']}")

# Save PDF Audit JSON
json_out = os.path.join(output_dir, "22_saffron_walden_deep_search.json")
with open(json_out, "w", encoding="utf-8") as out:
    json.dump(pdf_matches[:100], out, indent=2, ensure_ascii=False)

print(f"\n✓ Saved deep search to '{json_out}'!")

