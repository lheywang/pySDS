from  pathlib import Path
import tqdm
import subprocess

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
        sorted.append(file.split(".")[0] + ".md")

for index, file in enumerate(sorted):
    with open(file, "w") as f:
        print(["pydoc-markdown", "-p", file[:-2], file])
        # subprocess.run(["pydoc-markdown", "-p", file[:-2], "--render-toc", ">", file])