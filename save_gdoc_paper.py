import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

gdoc_content_path = r"C:\Users\krist\.gemini\antigravity\brain\f59bef92-7fda-4f56-81e6-b12686cba557\.system_generated\steps\259\content.md"
target_txt_path = r"c:\Users\krist\Desktop\Family-Tree-Research\john_mark_browder_origins_paper.txt"

with open(gdoc_content_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Clean metadata header from read_url_content output
if "---" in text:
    clean_paper = text.split("---", 1)[1].strip()
else:
    clean_paper = text

with open(target_txt_path, "w", encoding="utf-8") as out:
    out.write(clean_paper)

print(f"=== SAVED COMPLETE JOHN MARK BROWDER PAPER ===")
print(f"File Path: {target_txt_path}")
print(f"File Size: {len(clean_paper)} bytes ({len(clean_paper.splitlines())} lines)")

