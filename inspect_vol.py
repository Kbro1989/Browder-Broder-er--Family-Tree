import urllib.request
import json

url = "https://archive.org/metadata/lancashireparis03socigoog"
req = urllib.request.Request(url, headers={'User-Agent': 'AntigravityGenealogyBot/1.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    meta = data.get('metadata', {})
    print("=== METADATA FOR lancashireparis03socigoog ===")
    print("Title:", meta.get('title'))
    print("Publisher:", meta.get('publisher'))
    print("Year/Date:", meta.get('year') or meta.get('date'))
    print("Creator:", meta.get('creator'))
    print("Description:", meta.get('description', '')[:400])

    print("\n=== KEY DOWNLOADABLE FILES ===")
    for f in data.get('files', []):
        fname = f.get('name', '')
        if fname.endswith(('.pdf', '.txt', '_djvu.txt', '.epub')):
            size = f.get('size', '0')
            fmt = f.get('format', '')
            print(" -", fname, f"({size} bytes, format: {fmt})")
except Exception as e:
    print("Error:", e)
