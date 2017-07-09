from pathlib import Path

from yaml import load as yaml_load

from . import compile_all

data = {}
for data_path in Path('data').glob('**/*.yml'):
    data.update(yaml_load(data_path.read_text()))

for tgr in Path('templates').iterdir():
    if not tgr.is_dir(): continue
    compile_all(tgr.stem, data)
