from pathlib import Path
from sys import exit
BUILD_DIR = Path("build/") 
SRC_DIR = Path("src/")
TEMPLATE_DIR = Path("templates/")
TEMPLATE_PREFIX = "$"

FILE_TYPES = ['*.html', '*.css', '*.js']

parentdir = Path(__file__).resolve().parent
templates = {}

def src_to_build(filepath):
    return parentdir / BUILD_DIR / filepath.relative_to((parentdir / SRC_DIR))

for filetype in FILE_TYPES:
    for template_filename in (parentdir / TEMPLATE_DIR).glob(filetype):
        with open(template_filename, 'r') as template_file:
            templates[template_filename.stem] = template_file.read()

for directory in (parentdir / SRC_DIR).rglob('*'):
    if (directory.is_dir()):
        print(directory)
        src_to_build(directory).mkdir(parents=True, exist_ok=True)

for filetype in FILE_TYPES:
    for filename in (parentdir / SRC_DIR).rglob(filetype):
        with open(filename, 'r') as web_file:
            s = web_file.read()
        for k, v in templates.items():
            s = s.replace(TEMPLATE_PREFIX + k, v)
    with open(src_to_build(filename), 'w') as web_file:
        web_file.write(s)
