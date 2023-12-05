import pathlib
TEMPLATE_DIR = pathlib.Path("templates/")
TEMPLATE_PREFIX = "$"

parentdir = pathlib.Path(__file__).resolve().parent
templates = {}
for template_filename in (parentdir / TEMPLATE_DIR).glob('*.html'):
    print(template_filename)
    with open(template_filename, 'r') as template_file:
        templates[template_filename.name.replace('.html','')] = template_file.read()

for html_filename in parentdir.rglob('*.html'):
    with open(html_filename, 'w+') as html_file:
        s = html_file.read()
        for k, v in templates.items():
            s.replace(TEMPLATE_PREFIX + k, v)
        html_file.write(s)


