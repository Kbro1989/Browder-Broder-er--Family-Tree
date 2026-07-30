import os
import sys
import re
import urllib.request
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    ("https://broderers.co.uk/history-broderers", "broderers_co_uk_history.html"),
    ("https://broderers.co.uk/twenty-questions", "broderers_co_uk_twenty_questions.html"),
    ("https://en.wikipedia.org/wiki/Worshipful_Company_of_Broderers", "wikipedia_worshipful_company_of_broderers.html"),
    ("https://atom.aim25.com/index.php/worshipful-company-of-broderers-2", "aim25_worshipful_company_of_broderers.html"),
    ("https://www.gutenberg.org/cache/epub/20990/pg20990-images.html", "gutenberg_20990_london_and_the_kingdom_vol3.html"),
    ("https://www.familysearch.org/en/wiki/London_Business_and_Occupations", "familysearch_london_business_and_occupations.html"),
    ("https://www.british-history.ac.uk/london-record-soc/vol29", "bho_london_record_soc_vol29.html"),
    ("https://genealogyproofs.wordpress.com/blog-feed/page/3/", "genealogyproofs_wordpress_page3.html"),
    ("https://www.weavers.org.uk/about/history/1300-2/", "weavers_org_uk_history.html"),
    ("https://durham-repository.worktribe.com/OutputFile/1454276", "lambert_edward_iii_flemings.html"),
    ("https://www.englandsimmigrants.com/page/individual-studies/fourteenth-century-england-a-place-flemish-rebels-called-home", "englands_immigrants_flemish_rebels.html")
]

output_dir = "downloaded_source_pages"
os.makedirs(output_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 AntigravityGenealogyBot/1.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9'
}

print(f"=== FETCHING ALL {len(urls)} PROVIDED SOURCE URLS TO LOCAL DIRECTORY '{output_dir}/' ===")

results = []

for url, filename in urls:
    filepath = os.path.join(output_dir, filename)
    print(f"\n[+] Downloading: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()
            # Decode HTML
            try:
                html_text = content.decode('utf-8')
            except UnicodeDecodeError:
                html_text = content.decode('latin-1', errors='ignore')
            
            with open(filepath, "w", encoding="utf-8") as out:
                out.write(html_text)
            
            size_kb = len(content) / 1024
            print(f"    ✓ Saved to '{filepath}' ({size_kb:.1f} KB)")
            results.append((url, filepath, True, size_kb, None))
    except Exception as e:
        print(f"    ❌ Error fetching: {e}")
        results.append((url, filepath, False, 0, str(e)))

print("\n==========================================================================================")
print("                                 DOWNLOAD SUMMARY REPORT                                  ")
print("==========================================================================================")
for url, filepath, success, size_kb, err in results:
    status_str = f"SUCCESS ({size_kb:.1f} KB)" if success else f"FAILED ({err})"
    print(f" - {filename:<50} | {status_str}")

