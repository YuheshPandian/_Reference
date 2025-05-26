import os

EXCLUDED_DIRS = {".git", ".github", "__pycache__"}


def generate_index(folder):
    files = os.listdir(folder)
    items = []

    for file in sorted(files):
        # Skip the index itself
        if file == "index.html":
            continue
        path = os.path.join(folder, file)
        display_name = file + "/" if os.path.isdir(path) else file
        items.append(f'<li><a href="{file}">{display_name}</a></li>')

    html_content = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Index of {folder}</title></head>
<body>
<h1>Index of {folder}</h1>
<ul>
{"".join(items)}
</ul>
</body>
</html>"""

    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)


def should_skip(path):
    return any(excluded in path.split(os.sep) for excluded in EXCLUDED_DIRS)


# Walk through all folders
for root, dirs, files in os.walk("."):
    if should_skip(root):
        continue
    generate_index(root)
