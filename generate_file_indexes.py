# generate_index.py
import os

def generate_index(folder):
    files = os.listdir(folder)
    links = "\n".join([f'<li><a href="{file}">{file}</a></li>' for file in files])
    html = f"<ul>{links}</ul>"

    with open(os.path.join(folder, "index.html"), "w") as f:
        f.write(html)

# Traverse folders
for root, dirs, files in os.walk("."):
    generate_index(root)
