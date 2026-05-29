import os
import hashlib

dir1 = "/Users/imac/Desktop/Bastien-Antigravity/obsidian-brain/08-Base-Scripts-old/Role-Prompts"
dir2 = "/Users/imac/Desktop/Bastien-Antigravity/obsidian-brain/08-Base-Scripts/Role-Prompts"

def get_files_and_hashes(base_dir):
    file_hashes = {}
    if not os.path.exists(base_dir):
        return file_hashes
    for root, dirs, files in os.walk(base_dir):
        if "__pycache__" in root or ".git" in root:
            continue
        for file in files:
            if file == ".DS_Store":
                continue
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, base_dir)
            
            hasher = hashlib.sha256()
            try:
                with open(abs_path, 'rb') as f:
                    while chunk := f.read(8192):
                        hasher.update(chunk)
                file_hashes[rel_path] = hasher.hexdigest()
            except Exception as e:
                file_hashes[rel_path] = f"ERROR: {e}"
    return file_hashes

hashes1 = get_files_and_hashes(dir1)
hashes2 = get_files_and_hashes(dir2)

all_rel_paths = sorted(list(set(hashes1.keys()) | set(hashes2.keys())))

# Output in a clean markdown table
print("| Prompt File Path | 08-Base-Scripts-old SHA256 (Prefix) | 08-Base-Scripts SHA256 (Prefix) | Status |")
print("|---|---|---|---|")

for rel in all_rel_paths:
    h1 = hashes1.get(rel)
    h2 = hashes2.get(rel)
    
    if h1 is None:
        status = "Only in 08-Base-Scripts"
        h1_str = "-"
        h2_str = h2[:8] if h2 else "-"
    elif h2 is None:
        status = "Only in 08-Base-Scripts-old"
        h1_str = h1[:8] if h1 else "-"
        h2_str = "-"
    elif h1 == h2:
        status = "Identical"
        h1_str = h1[:8]
        h2_str = h2[:8]
    else:
        status = "**DIFFERENT**"
        h1_str = h1[:8]
        h2_str = h2[:8]
        
    print(f"| {rel} | {h1_str} | {h2_str} | {status} |")
