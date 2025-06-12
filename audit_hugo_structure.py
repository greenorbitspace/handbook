import os
import yaml
from collections import defaultdict

# Paths (adjust if needed)
CONTENT_DIR = "content/en"
LAYOUTS_DIR = "layouts"

def parse_front_matter(file_path):
    """Parse YAML front matter of a markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = yaml.safe_load(parts[1])
                return fm or {}
    except Exception as e:
        print(f"⚠️ Failed to parse {file_path}: {e}")
    return {}

def get_content_types(content_root):
    """Return dict of {type: [list of files]} from front matter in content."""
    types = defaultdict(list)
    for root, _, files in os.walk(content_root):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                fm = parse_front_matter(path)
                ctype = fm.get("type", "undefined")
                types[ctype].append(path)
    return types

def get_template_folders(layouts_root):
    """Return set of top-level template folders and all template files."""
    folders = set()
    templates = set()
    for root, _, files in os.walk(layouts_root):
        rel_root = os.path.relpath(root, layouts_root)
        # Only top-level folders
        top_folder = rel_root.split(os.sep)[0]
        if top_folder != ".":
            folders.add(top_folder)
        for file in files:
            templates.add(os.path.join(rel_root, file))
    return folders, templates

def audit(content_dir, layouts_dir):
    print(f"🔍 Scanning content directory: {content_dir}")
    content_types = get_content_types(content_dir)
    print(f"📄 Found content types and counts:")
    for ctype, files in content_types.items():
        print(f"  - '{ctype}': {len(files)} files")

    print(f"\n🔍 Scanning layouts directory: {layouts_dir}")
    layout_folders, layout_templates = get_template_folders(layouts_dir)
    print(f"📁 Found template folders:")
    for folder in sorted(layout_folders):
        print(f"  - {folder}")

    # Types used in content but no corresponding layout folder
    missing_templates = [ctype for ctype in content_types if ctype not in layout_folders and ctype != "undefined"]
    if missing_templates:
        print(f"\n❌ Content types with NO matching template folder:")
        for mt in missing_templates:
            print(f"  - {mt}")
    else:
        print("\n✅ All content types have corresponding template folders.")

    # Layout folders not matched by any content type
    unused_templates = [folder for folder in layout_folders if folder not in content_types]
    if unused_templates:
        print(f"\n⚠️ Template folders with NO matching content type:")
        for ut in unused_templates:
            print(f"  - {ut}")
    else:
        print("\n✅ All template folders correspond to some content type.")

if __name__ == "__main__":
    audit(CONTENT_DIR, LAYOUTS_DIR)