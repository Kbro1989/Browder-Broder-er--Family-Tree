import os
import re
import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")
output_dir = os.path.join(workspace_dir, "agent_outputs")

crawl_json_path = os.path.join(output_dir, "24_blog_feed_crawl_results.json")
with open(crawl_json_path, "r", encoding="utf-8") as jf:
    crawl_data = json.load(jf)

article_urls = crawl_data.get("unique_articles_found", [])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print(f"=== PROCESSING & HARVESTING ALL {len(article_urls)} DISCOVERED ARTICLE URLS ===")

existing_files = os.listdir(archive_dir)

downloaded_count = 0
skipped_count = 0

for url in article_urls:
    clean_slug = re.sub(r'https://genealogyproofs\.wordpress\.com/\d{4}/\d{2}/\d{2}/', '', url).strip('/')
    clean_slug = clean_slug.replace('-', '_')
    filename = f"genealogyproofs_wordpress_com_{clean_slug}.html"
    dest_path = os.path.join(archive_dir, filename)
    
    # If file exists and size > 20KB, skip download
    if filename in existing_files and os.path.getsize(dest_path) > 20000:
        print(f"  ✓ Already Harvested: '{filename}' ({os.path.getsize(dest_path)/1024:.1f} KB)")
        skipped_count += 1
        continue
        
    print(f"Fetching missing article: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
        with open(dest_path, "w", encoding="utf-8") as out:
            out.write(html)
            
        size_kb = os.path.getsize(dest_path) / 1024
        print(f"  ✓ Downloaded: '{filename}' ({size_kb:.1f} KB)")
        downloaded_count += 1
    except Exception as e:
        print(f"  ❌ Failed downloading '{url}': {e}")

print(f"\nProcessing Complete!")
print(f"Already Harvested Articles: {skipped_count}")
print(f"Newly Downloaded Articles: {downloaded_count}")

