import os
import re
import sys
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
html_file = os.path.join(workspace_dir, "browder_broderers_family_tree.html")
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Get map of downloaded files in archive_dir
downloaded_files = os.listdir(archive_dir)

# Helper function to match URL to file slug
def find_matching_file(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc.replace("www.", "").replace(".", "_")
    path_slug = re.sub(r'[^a-zA-Z0-9]', '_', parsed.path).strip('_')
    if not path_slug:
        path_slug = "index"
    expected_prefix = f"{domain}_{path_slug[:40]}"
    
    for f in downloaded_files:
        if f.startswith(expected_prefix) or expected_prefix in f:
            if os.path.getsize(os.path.join(archive_dir, f)) > 100:
                return f
    return None

# Find all web links in HTML
urls = set(re.findall(r'href="(https?://[^"]+)"', html))

print(f"=== LINKING {len(urls)} WEB URLS TO LOCAL DOWNLOADED FILES IN HTML ===")

replacements_count = 0
for u in sorted(urls):
    matched_file = find_matching_file(u)
    if matched_file:
        local_rel_path = f"downloaded_source_pages/{matched_file}"
        # Inject local archive link if not already present
        # Look for pattern: <a href="URL"...>TEXT</a>
        pattern = re.escape(u)
        
        # Replace occurrences in HTML
        def tag_replacer(m):
            href_val = m.group(0)
            return href_val # match handled via regex substitution
        
        # Exact replacement of anchor tags containing this URL
        tag_regex = r'<a [^>]*href="' + re.escape(u) + r'"[^>]*>(.*?)<\/a>'
        
        def link_sub(match):
            inner_text = match.group(1)
            # Avoid double local links
            if "[📁 Local Archive]" in inner_text or "Local Archive" in inner_text:
                return match.group(0)
            return f'<a href="{u}" target="_blank" style="color: #a89070;">{inner_text}</a> [<a href="./{local_rel_path}" target="_blank" style="color: #c9a84c; font-weight: bold;">📁 Local Archive</a>]'
        
        html, cnt = re.subn(tag_regex, link_sub, html)
        if cnt > 0:
            replacements_count += cnt
            print(f" ✓ Linked '{u[:50]}...' -> '{matched_file}' ({cnt} times)")

with open(html_file, "w", encoding="utf-8") as out:
    out.write(html)

print(f"\n==========================================================================================")
print(f"LINK INTEGRATION FINISHED: {replacements_count} ANCHOR TAGS UPDATED WITH LOCAL ARCHIVE LINKS")
print("==========================================================================================")

