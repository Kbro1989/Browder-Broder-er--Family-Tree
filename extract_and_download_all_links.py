import os
import re
import sys
import subprocess
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
output_dir = os.path.join(workspace_dir, "downloaded_source_pages")
os.makedirs(output_dir, exist_ok=True)

# Scan files for URLs
files_to_scan = [
    "browder_broderers_family_tree.html",
    "browder_broderers_lineage.json",
    "browder_mining_summary.txt",
    "browder_research_brief.md",
    "browder_archive_pipeline_results.json"
]

all_urls = set()

url_regex = r'https?://[^\s"\'\)\>\<\,\]\[]+'

for fname in files_to_scan:
    fpath = os.path.join(workspace_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        matches = re.findall(url_regex, content)
        for u in matches:
            clean_u = u.rstrip(".;,")
            # Exclude local relative links
            if not clean_u.startswith("http://localhost") and not "downloaded_source_pages" in clean_u:
                all_urls.add(clean_u)

print(f"=== FOUND {len(all_urls)} UNIQUE WEB SOURCE URLS ACROSS ALL RESEARCH FILES ===")

# Generate clean filename for each URL
def url_to_filename(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc.replace("www.", "").replace(".", "_")
    path_slug = re.sub(r'[^a-zA-Z0-9]', '_', parsed.path).strip('_')
    if not path_slug:
        path_slug = "index"
    fname = f"{domain}_{path_slug[:60]}.html"
    return fname

url_map = {}
for u in sorted(all_urls):
    fname = url_to_filename(u)
    url_map[u] = fname
    print(f" - {u} -> {fname}")

print("\n=== STARTING COMPREHENSIVE BATCH DOWNLOAD OF ALL SOURCE URLS ===")

success_count = 0
fail_count = 0

for idx, (url, fname) in enumerate(sorted(url_map.items()), 1):
    outfile = os.path.join(output_dir, fname)
    if os.path.exists(outfile) and os.path.getsize(outfile) > 500:
        print(f"[{idx:2d}/{len(url_map)}] Already downloaded: {fname} ({os.path.getsize(outfile)/1024:.1f} KB)")
        success_count += 1
        continue
    
    print(f"[{idx:2d}/{len(url_map)}] Downloading: {url}")
    cmd = [
        "curl", "-s", "-L",
        "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "-H", "Accept-Language: en-US,en;q=0.5",
        "--connect-timeout", "15",
        "--max-time", "45",
        "-o", outfile,
        url
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if os.path.exists(outfile) and os.path.getsize(outfile) > 100:
            size_kb = os.path.getsize(outfile) / 1024
            print(f"       ✓ Saved '{fname}' ({size_kb:.1f} KB)")
            success_count += 1
        else:
            print(f"       ⚠️ Failed or empty response: {url}")
            fail_count += 1
    except Exception as e:
        print(f"       ❌ Error: {e}")
        fail_count += 1

print("\n==========================================================================================")
print(f"COMPLETE BATCH DOWNLOAD FINISHED: {success_count} SUCCESSFUL, {fail_count} FAILED / EMPTY")
print("==========================================================================================")

