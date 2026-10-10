from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
files = list(root.rglob('*.md'))
keys = {p.relative_to(root).with_suffix('').as_posix() for p in files}
issues = []
for p in files:
    content = p.read_text(encoding='utf-8')
    for raw in re.findall(r'\[\[([^\]]+)\]\]', content):
        target = raw.split('|',1)[0].split('#',1)[0].strip().removesuffix('.md').lstrip('/')
        if not target or target == '...': continue
        parent = p.relative_to(root).parent.as_posix()
        local = (parent + '/' + target).lstrip('./')
        if not (target in keys or local in keys or sum(k.split('/')[-1] == target for k in keys) == 1):
            issues.append(f'{p.relative_to(root)} -> [[{raw}]]')
if issues:
    print('Links invalidos:', *issues, sep='\n - ')
    sys.exit(1)
print(f'OK: {len(files)} Markdown, links resolvidos')
