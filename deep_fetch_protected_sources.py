import os
import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")

wayback_direct_urls = [
    ("englandsimmigrants_com_page_individual_studies_fourteenth_century_england_a_place_f.html", "https://web.archive.org/web/20201026024108/https://www.englandsimmigrants.com/page/individual-studies/fourteenth-century-england-a-place-for-aliens"),
    ("englands_immigrants_flemish_rebels.html", "https://web.archive.org/web/20201026024108/https://www.englandsimmigrants.com/page/individual-studies/flemish-rebels"),
    ("genealogyproofs_wordpress_com_2019_09_03_proofs_that_martha_browder_c1774_c1811_who_marrie.html", "https://web.archive.org/web/20210118000000/https://genealogyproofs.wordpress.com/2019/09/03/proofs-that-martha-browder-c1774-c1811-who-married-william-bailey-was-the-daughter-of-edmund-browder-jr-c1734-1785-of-rockingham-county-north-carolina/"),
    ("genealogyproofs_wordpress_com_2019_09_04_mary_eppes_randolph_step_daughter_of_dr_james_tho.html", "https://web.archive.org/web/20210118000000/https://genealogyproofs.wordpress.com/2019/09/04/mary-eppes-randolph-step-daughter-of-dr-james-thomas-of-dinwiddie-county-virginia-was-the-wife-of-edmund-browder-jr-c1734-1785-of-rockingham-county-north-carolina/"),
    ("genealogyproofs_wordpress_com_2019_09_05_earliest_known_descendants_of_john_and_elizabeth_.html", "https://web.archive.org/web/20210118000000/https://genealogyproofs.wordpress.com/2019/09/05/earliest-known-descendants-of-john-and-elizabeth-browder-of-dinwiddie-county-virginia/"),
    ("genealogyproofs_wordpress_com_2019_09_05_edmund_browder_i_and_elizabeth_probably_bolling_a.html", "https://web.archive.org/web/20210118000000/https://genealogyproofs.wordpress.com/2019/09/05/edmund-browder-i-and-elizabeth-probably-bolling-and-their-children/")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("=== FETCHING DIRECT WAYBACK SNAPSHOTS FOR 6 REMAINING STUBS ===")

success_count = 0

for fname, wb_url in wayback_direct_urls:
    dest = os.path.join(archive_dir, fname)
    print(f"Fetching: {wb_url}")
    try:
        req = urllib.request.Request(wb_url, headers=headers)
        with urllib.request.urlopen(req, timeout=25) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
        with open(dest, "w", encoding="utf-8") as out:
            out.write(html)
            
        size_kb = os.path.getsize(dest) / 1024
        print(f" ✓ Saved: '{fname}' ({size_kb:.1f} KB)")
        success_count += 1
    except Exception as e:
        print(f" ❌ Failed fetching '{fname}': {e}")

print(f"\nSuccessfully fetched {success_count}/{len(wayback_direct_urls)} stub files!")

