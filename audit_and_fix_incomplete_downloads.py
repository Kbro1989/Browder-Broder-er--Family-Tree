import os
import re
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

archive_dir = "c:/Users/krist/Desktop/Family-Tree-Research/downloaded_source_pages"

# Define indicators of incomplete/failed responses
error_indicators = [
    "404 Not Found",
    "403 Forbidden",
    "Access Denied",
    "Just a moment...",
    "Attention Required! | Cloudflare",
    "Page Not Found",
    "502 Bad Gateway",
    "504 Gateway Time-out",
    "Database Error",
    "The requested URL was not found"
]

print("=== AUDITING DOWNLOADED SOURCE PAGES FOR ERRORS & INCOMPLETE CONTENT ===")

incomplete_or_failed = []

for filename in sorted(os.listdir(archive_dir)):
    filepath = os.path.join(archive_dir, filename)
    if not os.path.isfile(filepath):
        continue
    
    size_bytes = os.path.getsize(filepath)
    
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    is_incomplete = False
    reason = ""
    
    if size_bytes < 1500:
        is_incomplete = True
        reason = f"Small file size ({size_bytes} bytes)"
    else:
        for err in error_indicators:
            if err.lower() in content.lower():
                is_incomplete = True
                reason = f"Contains error string '{err}'"
                break
    
    if is_incomplete:
        # Extract URL if saved as comment or attempt to reconstruct from filename
        print(f" ❌ [INCOMPLETE/ERROR] {filename} ({size_bytes} bytes) -> Reason: {reason}")
        incomplete_or_failed.append((filename, filepath, reason))
    else:
        print(f" ✓ [VALID SOURCE] {filename} ({size_bytes/1024:.1f} KB)")

print(f"\nTotal files audited: {len(os.listdir(archive_dir))}")
print(f"Total valid complete files: {len(os.listdir(archive_dir)) - len(incomplete_or_failed)}")
print(f"Total incomplete/failed files requiring deep re-fetch: {len(incomplete_or_failed)}")

