import os

# Folders and files to ignore
SKIP_DIRS = {".git", ".github", "__pycache__"}
SKIP_FILES = {"generate_file_indexes.py", "index.html"}


def should_skip_dir(path):
    """Check if the directory should be skipped based on folder names."""
    return any(part in SKIP_DIRS for part in path.split(os.sep))


def generate_index_html(folder):
    """Create an index.html file listing all files and folders inside the given folder."""
    items = []
    for item in sorted(os.listdir(folder)):
        if item in SKIP_FILES:
            continue

        full_path = os.path.join(folder, item)
        display_name = item + "/" if os.path.isdir(full_path) else item
        items.append(f'<li><a href="{item}">{display_name}</a></li>')

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Reference Docs from - {folder}</title>
</head>
<body>
  <h1>Location: <b>{folder}</b></h1>
  <ul>
    {"".join(items)}
  </ul>
</body>
</html>
"""
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


# Walk through each folder and generate index.html if allowed
for root, dirs, files in os.walk("."):
    if should_skip_dir(root):
        continue
    generate_index_html(root)
