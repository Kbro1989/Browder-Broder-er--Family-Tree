import os
import re
import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")
output_dir = os.path.join(workspace_dir, "agent_outputs")

os.makedirs(archive_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("=== SYSTEMATICALLY CRAWLING ALL BLOG-FEED PAGES UNTIL END OF FEED ===")

page_num = 1
crawled_pages = []
discovered_article_urls = set()

while True:
    url = f"https://genealogyproofs.wordpress.com/blog-feed/page/{page_num}/" if page_num > 1 else "https://genealogyproofs.wordpress.com/blog-feed/"
    filename = f"genealogyproofs_wordpress_com_blog_feed_page_{page_num}.html"
    dest_path = os.path.join(archive_dir, filename)
    
    print(f"Crawling Page {page_num}: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
        # Check if page is 404 or empty redirect
        if "404 Not Found" in html or len(html) < 2000:
            print(f"  Reached end of blog feed at page {page_num} (HTTP 404 / empty page). Stopping.")
            break
            
        with open(dest_path, "w", encoding="utf-8") as out:
            out.write(html)
            
        size_kb = os.path.getsize(dest_path) / 1024
        print(f"  ✓ Saved: '{filename}' ({size_kb:.1f} KB)")
        crawled_pages.append((page_num, url, dest_path, size_kb))
        
        # Extract article URLs from this feed page
        matches = re.findall(r'https://genealogyproofs\.wordpress\.com/\d{4}/\d{2}/\d{2}/[^/"\s>]+/', html)
        for m in matches:
            discovered_article_urls.add(m)
            
        page_num += 1
        if page_num > 15: # Safety cap
            print("  Safety cap of 15 pages reached.")
            break
    except Exception as e:
        print(f"  Stopped at page {page_num}: {e}")
        break

print(f"\nCrawled {len(crawled_pages)} total blog feed pages!")
print(f"Extracted {len(discovered_article_urls)} unique article URLs across all feed pages!")

# Save Crawl Results JSON
crawl_json_path = os.path.join(output_dir, "24_blog_feed_crawl_results.json")
with open(crawl_json_path, "w", encoding="utf-8") as out:
    json.dump({
        "total_feed_pages_crawled": len(crawled_pages),
        "crawled_pages": crawled_pages,
        "unique_articles_found": sorted(list(discovered_article_urls))
    }, out, indent=2, ensure_ascii=False)

print(f"✓ Saved Blog Feed Crawl Results to '{crawl_json_path}'!")

