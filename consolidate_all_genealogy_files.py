import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

app_data_brain = r"C:\Users\krist\.gemini\antigravity\brain\f59bef92-7fda-4f56-81e6-b12686cba557"
target_dir = r"c:\Users\krist\Desktop\Family-Tree-Research"

os.makedirs(target_dir, exist_ok=True)

print(f"=== SEARCHING FOR ANCESTRY & GENEALOGY FILES IN BRAIN DIR '{app_data_brain}' ===")

copied_files = []

for root, dirs, files in os.walk(app_data_brain):
    # Exclude system_generated logs if not relevant, but check steps/tasks for content
    for file in files:
        if file.endswith(".md") or file.endswith(".txt") or file.endswith(".json") or file.endswith(".html"):
            src_path = os.path.join(root, file)
            # Skip system transcript jsonl
            if "transcript" in file or ".system_generated\\logs" in src_path:
                continue
            
            # Check content or name for genealogy relevance
            try:
                with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
                    content_head = f.read(2000)
                
                if any(k in content_head.lower() for k in ["browder", "broderer", "hulme", "genealogy", "gutenberg", "lineage", "family tree"]):
                    # Generate distinct name if needed
                    rel_name = os.path.relpath(src_path, app_data_brain).replace("\\", "_").replace("/", "_")
                    dest_path = os.path.join(target_dir, f"brain_harvested_{rel_name}")
                    shutil.copy2(src_path, dest_path)
                    size_kb = os.path.getsize(dest_path) / 1024
                    copied_files.append((src_path, dest_path, size_kb))
                    print(f" ✓ Copied: '{src_path}' -> '{dest_path}' ({size_kb:.1f} KB)")
            except Exception as e:
                pass

print("\n==========================================================================================")
print(f"CONSOLIDATION FINISHED: COPIED {len(copied_files)} ANCESTRY FILES TO {target_dir}")
print("==========================================================================================")

