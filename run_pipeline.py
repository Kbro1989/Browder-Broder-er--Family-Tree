import urllib.request
import json
import time
import sys

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'AntigravityGenealogyBot/1.0'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2 * (attempt + 1))
            else:
                return {'error': str(e)}
        except Exception as e:
            return {'error': str(e)}
    return {'error': 'Rate limited (429) after 3 retries'}

def main():
    results = {}

    print("=== 1. ENUMERATING ALL LANCASHIRE PARISH REGISTER SOCIETY VOLUMES ===")
    q2_url = "https://archive.org/advancedsearch.php?q=creator:(Lancashire+Parish+Register+Society)&fl[]=identifier&fl[]=title&fl[]=year&fl[]=description&rows=100&output=json"
    q2 = fetch_json(q2_url)
    
    manchester_volumes = []
    all_lprs = []
    
    if 'response' in q2:
        docs = q2['response']['docs']
        print(f"Total LPRS items found: {len(docs)}")
        for doc in docs:
            ident = doc.get('identifier')
            all_lprs.append(ident)
            
            # Fetch metadata for item to inspect details
            meta_url = f"https://archive.org/metadata/{ident}"
            meta = fetch_json(meta_url)
            title = meta.get('metadata', {}).get('title', '')
            desc = meta.get('metadata', {}).get('description', '')
            subject = str(meta.get('metadata', {}).get('subject', ''))
            
            combined_text = f"{title} {desc} {subject}".lower()
            if 'manchester' in combined_text:
                print(f"[FOUND MANCHESTER MATCH] ID: {ident} | Title: {title[:80]}")
                manchester_volumes.append({
                    'identifier': ident,
                    'title': title,
                    'description': desc[:300],
                    'subject': subject,
                    'files_count': len(meta.get('files', []))
                })
            else:
                print(f"  Processed {ident}...")
            time.sleep(0.3)

    results['manchester_volumes'] = manchester_volumes
    results['all_lprs_ids'] = all_lprs

    print("\n=== 2. WAYBACK CDX (J.M. Browder's Blog) ===")
    q3_url = "https://web.archive.org/cdx/search/cdx?url=genealogyproofs.wordpress.com&matchType=prefix&output=json&limit=50&filter=statuscode:200"
    q3 = fetch_json(q3_url)
    results['q3_wayback_jm_browder'] = q3
    if isinstance(q3, list) and len(q3) > 1:
        print(f"Logged {len(q3)-1} distinct URL captures from genealogyproofs.wordpress.com:")
        for row in q3[1:15]:
            print(f" - Timestamp: {row[1]} | Status: {row[4]} | URL: {row[2]}")

    print("\n=== 3. WAYBACK AVAILABILITY (Lancashire OPC) ===")
    time.sleep(1)
    q4_url = "https://archive.org/wayback/available?url=https://www.lan-opc.org.uk/Manchester/Manchester/cathedral/baptisms.html"
    q4 = fetch_json(q4_url)
    results['q4_lan_opc_availability'] = q4
    print(json.dumps(q4, indent=2))

    output_path = "browder_archive_pipeline_results.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"\n[+] Full structured JSON results saved to {output_path}")

if __name__ == "__main__":
    main()
