from os import makedirs
from os.path import join as pjoin
from pathlib import Path

import jinja2

def _template_dir(template_group):
    return pjoin('templates', template_group)

def compile(template_name, template_group, data):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(_template_dir(template_group))
    )
    template = env.get_template(template_name)
    outdir = pjoin('output', template_group)
    makedirs(outdir, exist_ok=True)
    with open(pjoin(outdir, template_name), 'w') as f:
        f.write(template.render(**data))

def compile_all(template_group, data):
    path = Path(_template_dir(template_group))
    for p in path.glob('**/[a-z]*.html'):
        compile(str(p.relative_to(path)), template_group, data)
