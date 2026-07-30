import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

feed_content_path = r"C:\Users\krist\.gemini\antigravity\brain\f59bef92-7fda-4f56-81e6-b12686cba557\.system_generated\steps\467\content.md"
archive_dir = r"c:\Users\krist\Desktop\Family-Tree-Research\downloaded_source_pages"

with open(feed_content_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Extract links matching blog posts
urls = re.findall(r'https://genealogyproofs\.wordpress\.com/\d{4}/\d{2}/\d{2}/[^/"\s>]+/', text)
urls = sorted(list(set(urls)))

print(f"=== FOUND {len(urls)} BLOG POST URLS IN FEED ===")

existing_files = os.listdir(archive_dir)

download_audit = []
for url in urls:
    # Build clean local filename
    clean_name = re.sub(r'https://genealogyproofs\.wordpress\.com/', '', url).strip('/')
    clean_name = clean_name.replace('/', '_').replace('-', '_') + ".html"
    
    target_file = f"genealogyproofs_wordpress_com_{clean_name}"
    
    is_downloaded = target_file in existing_files
    download_audit.append((url, target_file, is_downloaded))
    status = "✓ DOWNLOADED & PERSISTED" if is_downloaded else "❌ MISSING"
    print(f"{status}: {url}")

print(f"\nTotal Blog Posts Found: {len(urls)}")
print(f"Already Downloaded: {sum(1 for x in download_audit if x[2])}")
print(f"Missing Posts to Fetch: {sum(1 for x in download_audit if not x[2])}")

# Save audit results to JSON
audit_out = "c:/Users/krist/Desktop/Family-Tree-Research/blog_feed_audit_results.json"
with open(audit_out, "w", encoding="utf-8") as out:
    json.dump(download_audit, out, indent=2)

