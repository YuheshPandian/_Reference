import os

# Directories and files to ignore
SKIP_DIRS = {".git", ".github", "__pycache__"}
SKIP_FILES = {"generate_file_indexes.py", "index.html"}


def should_skip(name, full_path):
    return (
        name in SKIP_FILES
        or name in SKIP_DIRS
        or os.path.basename(full_path) in SKIP_DIRS
    )


def generate_index_html(folder):
    items = []

    for name in sorted(os.listdir(folder)):
        full_path = os.path.join(folder, name)
        if should_skip(name, full_path):
            continue

        if os.path.isdir(full_path):
            items.append(f'<li><a href="{name}/">{name}/</a></li>')
        else:
            items.append(f'''
<li>
  <a href="{name}">{name}</a>
  <a class="download-btn" href="{name}" download>[⬇ Download]</a>
</li>
''')

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Index of {folder}</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      padding: 20px;
    }}
    h1 {{
      font-size: 24px;
      color: #222;
    }}
    ul {{
      list-style-type: none;
      padding-left: 0;
    }}
    li {{
      margin: 8px 0;
    }}
    a {{
      text-decoration: none;
      color: #0077cc;
    }}
    .download-btn {{
      margin-left: 12px;
      color: green;
      font-size: 0.9em;
    }}
    .download-btn:hover {{
      text-decoration: underline;
    }}
  </style>
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
    return any(part in SKIP_DIRS for part in path.split(os.sep))


for root, dirs, files in os.walk("."):
    if is_dir_skipped(root):
        continue
    generate_index_html(root)
