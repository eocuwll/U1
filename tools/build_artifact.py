#!/usr/bin/env python3
"""Produit dist/artifact/index.html : version de app/index.html sans <html>/<head>/<body>
(pour publication en page web hébergée), données dans dist/artifact/data/."""
import pathlib, re, shutil
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / 'app/index.html').read_text(encoding='utf-8')
head = s.split('<!--ARTIFACT-START-->')[1].split('<!--HEAD-END-->')[0]
body = s.split('<!--BODY-START-->')[1].split('<!--BODY-END-->')[0]
head = re.sub(r'<link rel="(manifest|icon)"[^>]*>\n?', '', head)
out = root / 'dist/artifact'
(out / 'data').mkdir(parents=True, exist_ok=True)
(out / 'index.html').write_text(head + '<script>window.ARTIFACT=true</script>\n' + body, encoding='utf-8')
for f in (root / 'app/data').glob('*.js'):
    shutil.copy(f, out / 'data' / f.name)
print('ok', out)
