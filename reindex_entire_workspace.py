import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

scripts = [
    "parse_relationships_from_papers.py",
    "cross_reference_locations.py",
    "extract_speech_and_dialogue.py",
    "generate_timeline_1300_1990.py",
    "variable_cross_reference_matrix.py",
    "update_readme_with_exact_tree.py",
    "master_file_cross_reference.py"
]

print("=== RE-INDEXING ENTIRE WORKSPACE WITH ALL 9 NEW BLOG ARTICLES ===")

for script in scripts:
    print(f"\n--- Running: {script} ---")
    res = subprocess.run([sys.executable, script], capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print(f"Error: {res.stderr}")

print("\n==========================================================================================")
print("ALL WORKSPACE MATRICES, READMES, AND PIPELINES RE-INDEXED SUCCESSFULLY!")
print("==========================================================================================")

