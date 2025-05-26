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
  <a class="download-btn" href="{name}" download>Download</a>
</li>
''')

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Index of {folder}</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');

    body {{
      background-color: #f9f9f9;
      padding: 20px;
    }}
    h1 {{
      font-size: 2.2rem;
      font-family: Poppins, sans-serif;
      color: #222;
      font-weight: 300;
    }}
    ul {{
      list-style-type: none;
      padding-left: 0;
    }}
    li {{
      padding-block: 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid #3333338b;
    }}
    a {{
      text-decoration: none;
      color: #005a9b;
      font-family: Inter, sans-serif;
      font-size: 1.35rem;
      transition: 200ms ease;
    }}
    a:hover {{
      color: #00216d;
    }}
    .download-btn {{
      margin-left: 12px;
      background-color: rgb(168, 255, 168);
      font-size: 0.9em;
      padding: 4px;
      color: rgb(68, 68, 68);
      border-radius: 8px;
      box-shadow: 0px 4px 0px #63be45;
      font-family: Roboto, sans-serif;
      transition: 200ms ease;
    }}
    .download-btn:hover {{
      background-color: rgb(159, 255, 159);
      box-shadow: 0px 4px 0px #3a8e1e;
    }}
    .download-btn:active {{
      box-shadow: 0px 2px 0px #3a8e1e;
      transform: translateY(2px);
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
