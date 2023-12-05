from pathlib import Path
from sys import exit
import shutil

BUILD_DIR = Path("build/") 
SRC_DIR = Path("src/")
TEMPLATE_DIR = Path("templates/")
TEMPLATE_PREFIX = "$"

FILE_TYPES = ['.html']

parentdir = Path(__file__).resolve().parent
templates = {}

# make build directory
(parentdir / BUILD_DIR).mkdir(parents=True, exist_ok=True)

def src_to_build(filepath):
    return parentdir / BUILD_DIR / filepath.relative_to((parentdir / SRC_DIR))

# make a dictionary of template stuff to replace
for filetype in FILE_TYPES:
    for template_filename in (parentdir / TEMPLATE_DIR).glob('*' + filetype):
        with open(template_filename, 'r') as template_file:
            templates[template_filename.stem] = template_file.read()

# reproduce directory tree from src in build
for directory in (parentdir / SRC_DIR).rglob('*'):
    if (directory.is_dir()):
        print(directory)
        src_to_build(directory).mkdir(parents=True, exist_ok=True)

for filename in (parentdir / SRC_DIR).rglob('*'):
    if (filename.is_file()):
        newfilename = src_to_build(filename)
        shutil.copy(filename, newfilename)
        if (filename.suffix in FILE_TYPES):
            with open(filename, 'r') as web_file:
                s = web_file.read()
            for k, v in templates.items():
                s = s.replace(TEMPLATE_PREFIX + k, v)
            with open(newfilename, 'w') as web_file:
                web_file.write(s)
