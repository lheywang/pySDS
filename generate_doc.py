from pathlib import Path
import os

files = []
folder = Path("SDSPy")
for item in folder.iterdir():
    if item.is_file():
        files.append(str(item))

    if item.is_dir() and item.name != "__pycache__":
        folder2 = Path(item)
        for item2 in folder2.iterdir():
            if item2.is_file():
                files.append(str(item2))

sorted = []
for index, file in enumerate(files):
    if not (file.endswith("__init__.py") or file.endswith("main.py")):
        print(f"pydoc-markdown -p . --render-toc >.\{file[:-3]+".md"}")
