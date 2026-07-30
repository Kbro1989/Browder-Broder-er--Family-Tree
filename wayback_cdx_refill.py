import os
import urllib.request
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")

targets = [
    ("englandsimmigrants_com_page_individual_studies_fourteenth_century_england_a_place_f.html", "https://www.englandsimmigrants.com/page/individual-studies/fourteenth-century-england-a-place-for-aliens"),
    ("englands_immigrants_flemish_rebels.html", "https://www.englandsimmigrants.com/page/individual-studies/flemish-rebels"),
    ("genealogyproofs_wordpress_com_2019_09_03_proofs_that_martha_browder_c1774_c1811_who_marrie.html", "https://genealogyproofs.wordpress.com/2019/09/03/proofs-that-martha-browder-c1774-c1811-who-married-william-bailey-was-the-daughter-of-edmund-browder-jr-c1734-1785-of-rockingham-county-north-carolina"),
    ("genealogyproofs_wordpress_com_2019_09_04_mary_eppes_randolph_step_daughter_of_dr_james_tho.html", "https://genealogyproofs.wordpress.com/2019/09/04/mary-eppes-randolph-step-daughter-of-dr-james-thomas-of-dinwiddie-county-virginia-was-the-wife-of-edmund-browder-jr-c1734-1785-of-rockingham-county-north-carolina"),
    ("genealogyproofs_wordpress_com_2019_09_05_earliest_known_descendants_of_john_and_elizabeth_.html", "https://genealogyproofs.wordpress.com/2019/09/05/earliest-known-descendants-of-john-and-elizabeth-browder-of-dinwiddie-county-virginia"),
    ("genealogyproofs_wordpress_com_2019_09_05_edmund_browder_i_and_elizabeth_probably_bolling_a.html", "https://genealogyproofs.wordpress.com/2019/09/05/edmund-browder-i-and-elizabeth-probably-bolling-and-their-children")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("=== SEARCHING WAYBACK MACHINE CDX API FOR REMAINING 6 STUB PAGES ===")

for fname, orig_url in targets:
    cdx_url = f"http://web.archive.org/cdx/search/cdx?url={orig_url}*&output=json&limit=5"
    print(f"Querying CDX for: {orig_url}")
    try:
        req = urllib.request.Request(cdx_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            cdx_data = json.loads(resp.read().decode('utf-8'))
            
        if len(cdx_data) > 1:
            timestamp = cdx_data[1][1]
            archived_url = cdx_data[1][2]
            wayback_snapshot = f"http://web.archive.org/web/{timestamp}/{archived_url}"
            print(f"  Found Snapshot: {wayback_snapshot}")
            
            # Fetch snapshot
            sreq = urllib.request.Request(wayback_snapshot, headers=headers)
            with urllib.request.urlopen(sreq, timeout=20) as sresp:
                html = sresp.read().decode('utf-8', errors='ignore')
                
            dest = os.path.join(archive_dir, fname)
            with open(dest, "w", encoding="utf-8") as out:
                out.write(html)
            print(f"  ✓ REFILLED VIA WAYBACK: '{fname}' ({os.path.getsize(dest)/1024:.1f} KB)")
        else:
            print(f"  ❌ No Wayback snapshot found for '{orig_url}'")
    except Exception as e:
        print(f"  ❌ CDX Query error for '{orig_url}': {e}")

print("\n==========================================================================================")
print("WAYBACK MACHINE CDX REFILL COMPLETE!")
print("==========================================================================================")

