import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

failed_targets = [
    ("https://atom.aim25.com/index.php/worshipful-company-of-broderers-2", "downloaded_source_pages/aim25_worshipful_company_of_broderers.html"),
    ("https://www.familysearch.org/en/wiki/London_Business_and_Occupations", "downloaded_source_pages/familysearch_london_business_and_occupations.html"),
    ("https://www.british-history.ac.uk/london-record-soc/vol29", "downloaded_source_pages/bho_london_record_soc_vol29.html"),
    ("https://durham-repository.worktribe.com/OutputFile/1454276", "downloaded_source_pages/lambert_edward_iii_flemings.html"),
    ("https://www.englandsimmigrants.com/page/individual-studies/fourteenth-century-england-a-place-flemish-rebels-called-home", "downloaded_source_pages/englands_immigrants_flemish_rebels.html")
]

print("=== RETRYING FAILED URLS USING CURL WITH BROWSER HEADERS ===")

for url, outfile in failed_targets:
    print(f"\n[+] Fetching via curl: {url}")
    cmd = [
        "curl", "-s", "-L",
        "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "-H", "Accept-Language: en-US,en;q=0.5",
        "--connect-timeout", "20",
        "--max-time", "60",
        "-o", outfile,
        url
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if os.path.exists(outfile) and os.path.getsize(outfile) > 100:
            size_kb = os.path.getsize(outfile) / 1024
            print(f"    ✓ Successfully saved '{outfile}' ({size_kb:.1f} KB)")
        else:
            print(f"    ⚠️ Warning: File '{outfile}' is empty or very small ({os.path.getsize(outfile) if os.path.exists(outfile) else 0} bytes)")
    except Exception as e:
        print(f"    ❌ Error executing curl: {e}")

