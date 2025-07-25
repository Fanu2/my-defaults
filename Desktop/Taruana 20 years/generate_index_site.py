import os
from pathlib import Path

BASE_DIR = Path(".")

def scan_directory(base_path):
    tree = {}
    for root, dirs, files in os.walk(base_path):
        rel_root = os.path.relpath(root, base_path)
        if rel_root == ".":
            rel_root = ""
        tree[rel_root] = sorted(files)
    return tree

def generate_html(tree):
    html = [
        "<html>",
        "<head>",
        "<meta charset='UTF-8'>",
        "<title>📁 Taruana Archives</title>",
        "<style>",
        "body { font-family: sans-serif; margin: 2rem; background: var(--bg, #f9f9f9); color: var(--text, #000); transition: background 0.3s, color 0.3s; }",
        "h2 { color: #1f4b99; }",
        "details { margin-bottom: 1rem; }",
        "a { text-decoration: none; color: inherit; display: block; padding: 2px; }",
        "a:hover { background: #e0e0e0; }",
        ".toggle { position: fixed; top: 10px; right: 10px; padding: 0.5rem 1rem; background: #444; color: #fff; border: none; cursor: pointer; border-radius: 5px; }",
        "</style>",
        "<script>",
        "function toggleMode() {",
        "  const root = document.documentElement;",
        "  if (root.style.getPropertyValue('--bg') === '#121212') {",
        "    root.style.setProperty('--bg', '#f9f9f9');",
        "    root.style.setProperty('--text', '#000');",
        "  } else {",
        "    root.style.setProperty('--bg', '#121212');",
        "    root.style.setProperty('--text', '#f0f0f0');",
        "  }",
        "}",
        "</script>",
        "</head>",
        "<body>",
        "<button class='toggle' onclick='toggleMode()'>🌓 Toggle Dark Mode</button>",
        "<h1>📁 Taruana Document Archive</h1>"
    ]

    for folder, files in sorted(tree.items()):
        if not files:
            continue
        folder_display = folder or "Root"
        html.append(f"<details><summary><h2>{folder_display}</h2></summary><ul>")
        for file in files:
            filepath = os.path.join(folder, file) if folder else file
            icon = "📄" if file.endswith(".pdf") else "🌐" if file.endswith(".htm") else "🧾"
            # Simple clickable link opening in a new tab
            link = f"<a href='{filepath}' target='_blank'>{icon} {file}</a>"
            html.append(f"<li>{link}</li>")
        html.append("</ul></details>")

    html.append("</body></html>")
    return "\n".join(html)

if __name__ == "__main__":
    structure = scan_directory(BASE_DIR)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generate_html(structure))
    print("✅ index.html generated successfully.")
