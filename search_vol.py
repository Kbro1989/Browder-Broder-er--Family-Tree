import urllib.request
import re
import sys

url = "https://archive.org/download/lancashireparis03socigoog/lancashireparis03socigoog_djvu.txt"
txt_filename = "lancashireparis03socigoog_djvu.txt"

print(f"Downloading {url} ...")
req = urllib.request.Request(url, headers={'User-Agent': 'AntigravityGenealogyBot/1.0'})
with urllib.request.urlopen(req) as resp, open(txt_filename, 'wb') as f:
    f.write(resp.read())

print("[+] Download complete. Reading text file...")
with open(txt_filename, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

print(f"Total characters: {len(text)}")

search_patterns = [
    r'\bBrowder\b',
    r'\bBrowderer\b',
    r'\bBroderer\b',
    r'\bBroder\b',
    r'\bBrowdere\b',
    r'\bHulme\b',
    r'\bSancre\b',
    r'\bDeloney\b'
]

print("\n=== REGEX SEARCH RESULTS IN LANCASHIREPARIS03SOCIGOOG ===")
for pattern in search_patterns:
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    print(f"\nPattern: '{pattern}' -> Found {len(matches)} matches:")
    for i, match in enumerate(matches[:15]):
        start = max(0, match.start() - 100)
        end = min(len(text), match.end() + 100)
        snippet = text[start:end].replace('\n', ' ')
        print(f"  {i+1}. ... {snippet} ...")
