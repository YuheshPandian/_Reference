import os

# Folders and files to exclude from listings
SKIP_DIRS = {".git", ".github", "__pycache__"}
SKIP_FILES = {"generate_file_indexes.py", "index.html"}


def should_skip(name, full_path):
    """Return True if the file or folder should be skipped."""
    return (
        name in SKIP_FILES
        or name in SKIP_DIRS
        or os.path.basename(full_path) in SKIP_DIRS
    )


def generate_index_html(folder):
    """Generate an index.html for a folder."""
    items = []
    for name in sorted(os.listdir(folder)):
        full_path = os.path.join(folder, name)
        if should_skip(name, full_path):
            continue
        display_name = name + "/" if os.path.isdir(full_path) else name
        items.append(f'<li><a href="{name}">{display_name}</a></li>')

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Index of {folder}</title>
</head>
<body>
  <h1>Location: {folder}</h1>
  <ul>
    {"".join(items)}
  </ul>
</body>
</html>"""

    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def is_dir_skipped(path):
    """Skip directory if any part of its path is in SKIP_DIRS."""
    return any(part in SKIP_DIRS for part in path.split(os.sep))


# Walk the folder tree and generate index.html where needed
for root, dirs, files in os.walk("."):
    if is_dir_skipped(root):
        continue
    generate_index_html(root)
