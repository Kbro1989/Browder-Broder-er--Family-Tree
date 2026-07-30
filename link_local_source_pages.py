import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("browder_broderers_family_tree.html", "r", encoding="utf-8") as f:
    html = f.read()

# Map of web URLs to local downloaded file paths
url_to_local = {
    "https://www.gutenberg.org/cache/epub/20990/pg20990-images.html": ("downloaded_source_pages/gutenberg_20990_london_and_the_kingdom_vol3.html", "Gutenberg #20990 (Local HTML Archive - 2.28 MB)"),
    "https://genealogyproofs.wordpress.com/blog-feed/page/3/": ("downloaded_source_pages/genealogyproofs_wordpress_page3.html", "J.M. Browder Research (Local HTML Archive - 681 KB)"),
    "https://en.wikipedia.org/wiki/Worshipful_Company_of_Broderers": ("downloaded_source_pages/wikipedia_worshipful_company_of_broderers.html", "Wikipedia: Broderers (Local HTML Archive - 107 KB)"),
    "https://www.weavers.org.uk/about/history/1300-2/": ("downloaded_source_pages/weavers_org_uk_history.html", "Weavers Guild History (Local HTML Archive - 51 KB)"),
    "https://www.british-history.ac.uk/london-record-soc/vol29": ("downloaded_source_pages/bho_london_record_soc_vol29.html", "British History Online 1541 Subsidy (Local HTML Archive - 44 KB)"),
    "https://broderers.co.uk/twenty-questions": ("downloaded_source_pages/broderers_co_uk_twenty_questions.html", "Broderers 20 Questions (Local HTML Archive - 20 KB)"),
    "https://broderers.co.uk/history-broderers": ("downloaded_source_pages/broderers_co_uk_history.html", "Broderers Official History (Local HTML Archive - 15 KB)"),
    "https://www.familysearch.org/en/wiki/London_Business_and_Occupations": ("downloaded_source_pages/familysearch_london_business_and_occupations.html", "FamilySearch Wiki London (Local HTML Archive)")
}

print("=== ADDING DIRECT LOCAL FILE LINKS TO HTML FAMILY TREE ===")

for web_url, (local_path, label) in url_to_local.items():
    # Replace links or append local archive link
    pattern = f'<a href="{re.escape(web_url)}"[^>]*>([^<]+)</a>'
    
    def replacer(match):
        orig_text = match.group(1)
        return f'<a href="{web_url}" target="_blank" style="color: #a89070;">{orig_text}</a> [<a href="./{local_path}" target="_blank" style="color: #c9a84c; font-weight: bold;">📁 Local Archive</a>]'
    
    html, count = re.subn(pattern, replacer, html)
    print(f" - Linked '{local_path}': {count} replacements made.")

with open("browder_broderers_family_tree.html", "w", encoding="utf-8") as out:
    out.write(html)

print("\n✓ HTML Family Tree updated with direct relative local file links!")

