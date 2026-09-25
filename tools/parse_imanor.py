import re, json, sys
lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
sec_re = re.compile(r'^[#*\s]*(4\.(\d+)(?:\.(\d+))?)\**\s*\**\s*(?:Lots?\s*N\s*°\s*\d+\s*:\s*)?(.+?)\**\s*$')
lot = sub = None; lotname = subname = ''
recs = []; cur = None; lastkey = None
def keyof(k):
    k = k.lower().replace('’',"'").strip(' :-')
    if k.startswith('code'): return 'nm'
    if k.startswith('equival'): return 'eq'
    if k.startswith('intitul'): return 'titre'
    if k.startswith('domain'): return 'domaine'
    if k == '': return 'cont'
    return None
for i, l in enumerate(lines):
    if i < 400: continue
    s = l.strip()
    if not s.startswith('|'):
        m = sec_re.match(s)
        if m and len(m.group(4)) < 140 and not re.search(r'\.{4}', s):
            name = re.sub(r'[*#]', '', m.group(4)).strip()
            name = re.sub(r'^Lots?\s*N\s*°\s*\d+\s*:\s*', '', name)
            if m.group(3) is None:
                lot = int(m.group(2)); lotname = name; sub = None; subname = ''
            else:
                sub = m.group(1); subname = name
        continue
    cells = [c.strip() for c in s.strip('|').split('|')]
    if len(cells) < 2 or set(cells[0]) <= set('- ') and cells[0] != '': continue
    k = keyof(cells[0]); v = ' '.join(c for c in cells[1:] if c).strip()
    if k is None: continue
    if k == 'nm':
        if not v: continue
        cur = dict(nm=v, eq='', titre='', domaine='', lot=lot, lotname=lotname, sub=sub, subname=subname)
        recs.append(cur); lastkey = 'nm'
    elif cur is None: continue
    elif k == 'cont':
        if v and lastkey in ('domaine', 'titre'): cur[lastkey] += ' ' + v
    else:
        if cur[k] and k=='domaine': cur[k] += ' ' + v
        elif not cur[k]: cur[k] = v
        lastkey = k
for r in recs:
    for k in ('nm','eq','titre','domaine'):
        r[k] = re.sub(r'\s+', ' ', r[k].replace('\\-', '-').replace('\\', '')).strip(' ;')
json.dump(recs, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
from collections import Counter
print(len(recs))
print(Counter((r['lot'], r['lotname'][:50]) for r in recs))
print(Counter((r['sub'], r['subname'][:50]) for r in recs))
print('no eq', sum(1 for r in recs if not r['eq']), 'no titre', sum(1 for r in recs if not r['titre']), 'no dom', sum(1 for r in recs if not r['domaine']))
