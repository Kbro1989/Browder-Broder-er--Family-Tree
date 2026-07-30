import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
remote_url = "git@github.com:Kbro1989/Browder-Broder-er--Family-Tree.git"

print("=== SETTING UP GIT REPOSITORY & PUSHING TO GITHUB ===")

# Create .gitignore if not exists
gitignore_path = os.path.join(workspace_dir, ".gitignore")
gitignore_content = """# Git Ignore Rules
harvested_pdfs/*.pdf
*.pyc
__pycache__/
"""

with open(gitignore_path, "w", encoding="utf-8") as out:
    out.write(gitignore_content)

print(" ✓ Created .gitignore")

# Helper runner
def run_git(args):
    print(f"Running: git {' '.join(args)}")
    res = subprocess.run(["git"] + args, cwd=workspace_dir, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print(f"Stderr: {res.stderr}")
    return res

run_git(["init"])
run_git(["branch", "-M", "main"])
run_git(["remote", "remove", "origin"])
run_git(["remote", "add", "origin", remote_url])

run_git(["add", "."])
run_git(["commit", "-m", "Initial commit: Complete 700-Year Browder & Worshipful Company of Broderers Lineage Corpus, HTML Tree, and Matrix Reports"])

print("\n--- PUSHING TO REMOTE REPOSITORY ---")
run_git(["push", "-u", "origin", "main", "--force"])

print("✓ Git repository setup and push attempt completed!")

