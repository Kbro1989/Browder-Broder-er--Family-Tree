import os
import re
import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
output_dir = os.path.join(workspace_dir, "agent_outputs")
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")
pdf_dir = os.path.join(workspace_dir, "harvested_pdfs")

os.makedirs(output_dir, exist_ok=True)

print("=== REFILLING CORRUPTED & STUB SOURCE PAGES FROM LIVE / WAYBACK ARCHIVES ===")

url_mapping = {
    "englandsimmigrants_com_page_individual_studies_fourteenth_century_england_a_place_f.html": "https://web.archive.org/web/20210126154500/https://www.englandsimmigrants.com/page/individual-studies/fourteenth-century-england-a-place-for-aliens",
    "englands_immigrants_flemish_rebels.html": "https://web.archive.org/web/20210126154500/https://www.englandsimmigrants.com/page/individual-studies/flemish-rebels",
    "genealogyproofs_wordpress_com_2019_09_03_proofs_that_martha_browder_c1774_c1811_who_marrie.html": "https://genealogyproofs.wordpress.com/2019/09/03/proofs-that-martha-browder-c1774-c1811-who-married-william-bailey-was-the-daughter-of-edmund-browder-jr-c1734-1785-of-rockingham-county-north-carolina/",
    "genealogyproofs_wordpress_com_2019_09_04_mary_eppes_randolph_step_daughter_of_dr_james_tho.html": "https://genealogyproofs.wordpress.com/2019/09/04/mary-eppes-randolph-step-daughter-of-dr-james-thomas-of-dinwiddie-county-virginia-was-the-wife-of-edmund-browder-jr-c1734-1785-of-rockingham-county-north-carolina/",
    "genealogyproofs_wordpress_com_2019_09_04_richard_and_mary_browder_of_dinwiddie_county_virg.html": "https://genealogyproofs.wordpress.com/2019/09/04/richard-and-mary-browder-of-dinwiddie-county-virginia/",
    "genealogyproofs_wordpress_com_2019_09_04_the_earliest_isham_browders_and_other_related_per.html": "https://genealogyproofs.wordpress.com/2019/09/04/the-earliest-isham-browders-and-other-related-persons/",
    "genealogyproofs_wordpress_com_2019_09_05_earliest_known_descendants_of_john_and_elizabeth_.html": "https://genealogyproofs.wordpress.com/2019/09/05/earliest-known-descendants-of-john-and-elizabeth-browder-of-dinwiddie-county-virginia/",
    "genealogyproofs_wordpress_com_2019_09_05_edmund_browder_i_and_elizabeth_probably_bolling_a.html": "https://genealogyproofs.wordpress.com/2019/09/05/edmund-browder-i-and-elizabeth-probably-bolling-and-their-children/",
    "genealogyproofs_wordpress_com_2019_12_02_captain_isham_browder.html": "https://genealogyproofs.wordpress.com/2019/12/02/captain-isham-browder/",
    "genealogyproofs_wordpress_com_2023_02_22_browder_family_traced_to_dublin_ireland.html": "https://genealogyproofs.wordpress.com/2023/02/22/browder-family-traced-to-dublin-ireland/",
    "genealogyproofs_wordpress_com_blog_feed_page_3.html": "https://genealogyproofs.wordpress.com/blog-feed/page/3/",
    "genealogyproofs_wordpress_com_index.html": "https://genealogyproofs.wordpress.com/"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

refilled_summary = []

for fname, url in url_mapping.items():
    fpath = os.path.join(archive_dir, fname)
    print(f"Refilling: '{fname}' from {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            
        with open(fpath, "w", encoding="utf-8") as out:
            out.write(content)
            
        size_kb = os.path.getsize(fpath) / 1024
        print(f" ✓ REFILLED SUCCESSFULLY: '{fname}' ({size_kb:.1f} KB)")
        refilled_summary.append({"file": fname, "status": "REFILLED", "size_kb": size_kb})
    except Exception as e:
        print(f" ❌ Failed refilling '{fname}': {e}")
        refilled_summary.append({"file": fname, "status": "FAILED", "error": str(e)})

# Save Audit JSON
audit_json_path = os.path.join(output_dir, "23_bad_downloads_audit_results.json")
with open(audit_json_path, "w", encoding="utf-8") as out:
    json.dump({
        "refill_action": "REFILLED_STUBS_AND_ERRORS",
        "total_refilled": sum(1 for r in refilled_summary if r["status"] == "REFILLED"),
        "refill_details": refilled_summary
    }, out, indent=2, ensure_ascii=False)

print(f"\n✓ Saved Bad Downloads Refill Results to '{audit_json_path}'!")

