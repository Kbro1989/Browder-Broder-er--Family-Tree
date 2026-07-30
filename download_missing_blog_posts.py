import os
import re
import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')

archive_dir = r"c:\Users\krist\Desktop\Family-Tree-Research\downloaded_source_pages"
os.makedirs(archive_dir, exist_ok=True)

missing_urls = [
    "https://genealogyproofs.wordpress.com/2021/03/08/correcting-hopeless-errors-concerning-browder-family-genealogy/",
    "https://genealogyproofs.wordpress.com/2021/07/20/false-browder-ancestry/",
    "https://genealogyproofs.wordpress.com/2021/10/04/the-ancestry-of-isham-browder-1762-1830-solved-at-last/",
    "https://genealogyproofs.wordpress.com/2023/02/11/parthenia-theney-browder-bailey-never-existed-and-heres-proof/",
    "https://genealogyproofs.wordpress.com/2023/09/28/thrasher-john-sen-to-john-thrasher-jr-17-feb-1788/",
    "https://genealogyproofs.wordpress.com/2023/10/18/browder-as-opposed-to-broderbund/",
    "https://genealogyproofs.wordpress.com/2023/12/20/clearing-up-some-early-browder-family-research/",
    "https://genealogyproofs.wordpress.com/2025/01/04/jones-browder-estate-case/",
    "https://genealogyproofs.wordpress.com/2025/02/23/origins-of-the-south-carolina-browder-family/"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print(f"=== DOWNLOADING {len(missing_urls)} MISSING BLOG POST ARTICLES FROM GENEALOGYPROOFS ===")

downloaded_count = 0

for url in missing_urls:
    clean_slug = re.sub(r'https://genealogyproofs\.wordpress\.com/\d{4}/\d{2}/\d{2}/', '', url).strip('/')
    clean_slug = clean_slug.replace('-', '_')
    filename = f"genealogyproofs_wordpress_com_{clean_slug}.html"
    dest_path = os.path.join(archive_dir, filename)
    
    print(f"Fetching: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
        with open(dest_path, "w", encoding="utf-8") as out:
            out.write(html)
            
        size_kb = os.path.getsize(dest_path) / 1024
        print(f" ✓ Saved: '{filename}' ({size_kb:.1f} KB)")
        downloaded_count += 1
    except Exception as e:
        print(f" ❌ Failed fetching '{url}': {e}")

print(f"\nSuccessfully downloaded {downloaded_count}/{len(missing_urls)} missing blog posts!")

