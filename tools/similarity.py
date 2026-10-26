#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Likhet mellan ortsidor (mot mallkloner).
Kor:  python3 tools/similarity.py [--max 0.25] [--takreno] [--tjanster]
Mattet: Jaccard pa 5-ords-shingles av sidans <main>-text (utan header/footer),
ortnamnet ersatt med "ORT" sa att bara ortbytet inte gor sidor olika.
Visar max-/snittlikhet och de mest lika paren. Exit 1 om max > --max.
"""
import glob, html, itertools, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
LIMIT = float(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 0.25

if "--tjanster" in sys.argv:
    # Tjänstehubbar + ortsidor (2026-10-25): parvis inom tjänst, mot ortens taksidor och mot byggtorg.se.
    import subprocess
    sys.exit(subprocess.call([sys.executable, os.path.join(ROOT, "tools", "tj_check.py")]
                             + [x for x in sys.argv[1:] if x != "--tjanster"]))

from generate import AREAS, slug  # noqa: E402  (Stockholmsorter)

def text_of(path):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"<main\b.*?</main>", s, re.S)
    s = m.group(0) if m else s
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s)).lower()
    return re.findall(r"[a-zåäö0-9]+", s)

def shingles(words, ort, k=5):
    o = ort.lower().split()
    w = ["ORT" if x in o else x for x in words]
    return {" ".join(w[i:i + k]) for i in range(len(w) - k + 1)}

pages = {}
for ort in AREAS:
    p = os.path.join(ROOT, f"taklaggare-{slug(ort)}.html")
    if os.path.exists(p):
        pages[ort] = shingles(text_of(p), ort)

if "--takreno" in sys.argv:
    # Takrenovering-ortsidor: parvis (<= 25 %) och mot ortens takläggarsida (<= 30 %).
    from generate import TRP_ORTER, TRP_FILES
    tr = {o: shingles(text_of(os.path.join(ROOT, TRP_FILES[o])), o) for o in TRP_ORTER}
    pp = sorted(((len(tr[x] & tr[y]) / len(tr[x] | tr[y]), x, y)
                 for x, y in itertools.combinations(tr, 2)), reverse=True)
    vs = sorted(((len(tr[o] & pages[o]) / len(tr[o] | pages[o]), o) for o in tr if o in pages), reverse=True)  # v29: innerstaden saknar takläggarsida
    print(f"Takrenovering: {len(tr)} sidor. Parvis max {pp[0][0]:.1%}, snitt {sum(p[0] for p in pp)/len(pp):.1%}.")
    for s_, x, y in pp[:5]:
        print(f"  {s_:.1%}  {x} – {y}")
    print(f"Mot takläggarsidan: max {vs[0][0]:.1%}.")
    for s_, o in vs:
        print(f"  {s_:.1%}  {o}")
    sys.exit(1 if pp[0][0] > 0.25 or vs[0][0] > 0.30 else 0)

pairs = []
for x, y in itertools.combinations(pages, 2):
    a, b = pages[x], pages[y]
    pairs.append((len(a & b) / len(a | b), x, y))
pairs.sort(reverse=True)
mx = pairs[0][0] if pairs else 0
avg = sum(p[0] for p in pairs) / len(pairs) if pairs else 0
print(f"{len(pages)} ortsidor, {len(pairs)} par. Max {mx:.1%}, snitt {avg:.1%}.")
for s, x, y in pairs[:8]:
    print(f"  {s:.1%}  {x} – {y}")
sys.exit(1 if mx > LIMIT else 0)
