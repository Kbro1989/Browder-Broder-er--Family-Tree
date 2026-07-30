import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

gdoc_raw_path = r"C:\Users\krist\.gemini\antigravity\brain\f59bef92-7fda-4f56-81e6-b12686cba557\.system_generated\steps\244\content.md"

with open(gdoc_raw_path, "r", encoding="utf-8", errors="ignore") as f:
    raw_content = f.read()

# Remove script and style tags
no_script = re.sub(r'<script[^>]*>.*?</script>', ' ', raw_content, flags=re.DOTALL)
no_style = re.sub(r'<style[^>]*>.*?</style>', ' ', no_script, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', '\n', no_style)

lines = [line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith('%') and not line.strip().startswith('DOCS_')]
clean_doc_text = '\n'.join(lines)

out_path = "c:/Users/krist/Desktop/Family-Tree-Research/john_mark_browder_gdoc_extracted.txt"
with open(out_path, "w", encoding="utf-8") as out:
    out.write(clean_doc_text)

print(f"=== EXTRACTED GOOGLE DOC TEXT ({len(clean_doc_text)} chars, {len(lines)} lines) ===")
print(f"Saved extracted text to: {out_path}")
print("\n--- FIRST 2500 CHARACTERS PREVIEW ---")
print(clean_doc_text[:2500])

