import os
import re
import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
archive_dir = os.path.join(workspace_dir, "downloaded_source_pages")
pdf_dir = os.path.join(workspace_dir, "harvested_pdfs")
os.makedirs(archive_dir, exist_ok=True)
os.makedirs(pdf_dir, exist_ok=True)

gutenberg_files = [
    ("gutenberg_51885_trade_signs_of_essex.txt", "https://www.gutenberg.org/files/51885/51885-0.txt"),
    ("gutenberg_55862_industrial_history_of_england.txt", "https://www.gutenberg.org/files/55862/55862-0.txt"),
    ("gutenberg_70140_early_english_cotton_industry.txt", "https://www.gutenberg.org/files/70140/70140-0.txt")
]

archive_org_ocr_files = [
    ("archive_org_gilds_and_companies_of_london_ocr.txt", "https://archive.org/stream/gildscompaniesof00unwiuoft/gildscompaniesof00unwiuoft_djvu.txt"),
    ("archive_org_yorkshire_woollen_industry_ocr.txt", "https://archive.org/stream/yorkshirewoollen00heatuoft/yorkshirewoollen00heatuoft_djvu.txt"),
    ("archive_org_annals_of_manchester_ocr.txt", "https://archive.org/stream/annalsofmanchest00axon/annalsofmanchest00axon_djvu.txt")
]

archive_org_pdfs = [
    ("gildscompaniesof00unwiuoft.pdf", "https://archive.org/download/gildscompaniesof00unwiuoft/gildscompaniesof00unwiuoft.pdf"),
    ("yorkshirewoollen00heatuoft.pdf", "https://archive.org/download/yorkshirewoollen00heatuoft/yorkshirewoollen00heatuoft.pdf"),
    ("annalsofmanchest00axon.pdf", "https://archive.org/download/annalsofmanchest00axon/annalsofmanchest00axon.pdf"),
    ("returnsofaliensd1031hugu.pdf", "https://archive.org/download/returnsofaliensd1031hugu/returnsofaliensd1031hugu.pdf"),
    ("returnsofaliensd02kirk.pdf", "https://archive.org/download/returnsofaliensd02kirk/returnsofaliensd02kirk.pdf")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("=== BATCH HARVESTING DIRECT DOWNLOAD PACK SOURCES ===")

# Download Gutenberg Text Files
for fname, url in gutenberg_files:
    dest = os.path.join(archive_dir, fname)
    print(f"Fetching Gutenberg text: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
        with open(dest, "w", encoding="utf-8") as out:
            out.write(text)
        print(f" ✓ Saved: '{fname}' ({os.path.getsize(dest)/1024:.1f} KB)")
    except Exception as e:
        print(f" ❌ Failed fetching '{url}': {e}")

# Download Archive.org OCR Text Files
for fname, url in archive_org_ocr_files:
    dest = os.path.join(archive_dir, fname)
    print(f"Fetching Archive.org OCR text: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=25) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
        with open(dest, "w", encoding="utf-8") as out:
            out.write(text)
        print(f" ✓ Saved: '{fname}' ({os.path.getsize(dest)/1024:.1f} KB)")
    except Exception as e:
        print(f" ❌ Failed fetching '{url}': {e}")

# Download Archive.org PDFs
for fname, url in archive_org_pdfs:
    dest = os.path.join(pdf_dir, fname)
    print(f"Fetching Archive.org PDF: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=40) as resp:
            data = resp.read()
        with open(dest, "wb") as out:
            out.write(data)
        print(f" ✓ Saved PDF: '{fname}' ({os.path.getsize(dest)/(1024*1024):.2f} MB)")
    except Exception as e:
        print(f" ❌ Failed fetching PDF '{url}': {e}")

print("\n==========================================================================================")
print("DOWNLOAD PACK HARVESTING COMPLETED!")
print("==========================================================================================")

