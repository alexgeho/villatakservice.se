#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kontroll av tjänstehubbar/ortsidor (tjänster v1). Renderar i minnet – skriver inga filer.
Kor:  python3 tools/tj_check.py [--service malare] [--no-byggtorg] [-v]

Schema per sida i PAGES_TJ (tools/tj_*.py):
  kind: "hub" | "district";  service: nyckel i TJ_SERVICES;  ort: (district) t.ex. "Bromma"
  title (<= 60 tecken, ort först för district), description (<= 155), h1, lead, card (kort kortsnitt),
  svc_label: t.ex. "Målare" (rubrik "Målare per område" / "Målare i fler områden"),
  sections: [{id, h2, paras:[html], aside:{title, items} | None, anchor?: "Snabblänktext"}],
  steps_h2, steps:[(rubrik, text)], rot_h2, rot:[html], price_h2, price:[html],
  faq:[(fråga, svar)], sources:[(namn, url)], cta:(rubrik, text),
  img:[(alt_hero, prompt_4_3), (alt_innehåll, prompt_3_2)],
  related: [(href, rubrik, text)]  (hub: 3–4 kort "Relaterade tjänster"; district: valfria extra kort)

Mätt (samma som similarity.py): Jaccard på 5-ords-shingles av <main>, ortnamnet -> "ORT".
  - parvis inom tjänsten (hubb + ortsidor) <= 25 %
  - ortsida mot ortens taklaggare-/takrenovering-sida <= 25 %
  - mot byggtorg.se på samma sökord: andel av VÅRA shingles som också finns hos byggtorg <= 15 %
Exit 1 vid fel.
"""
import html as H, itertools, os, re, sys, tempfile, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import generate as G  # noqa: E402
from tjanster_v1 import TJ, TJ_SERVICES, TJ_HUB  # noqa: E402

ARGS = sys.argv[1:]
ONLY = ARGS[ARGS.index("--service") + 1] if "--service" in ARGS else None
VERB = "-v" in ARGS
CACHE = os.path.join(tempfile.gettempdir(), "byggtorg_cache")
os.makedirs(CACHE, exist_ok=True)
errors, warns = [], []

def words_of(s):
    m = re.search(r"<main\b.*?</main>", s, re.S)
    s = m.group(0) if m else s
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S)
    s = H.unescape(re.sub(r"<[^>]+>", " ", s)).lower()
    return re.findall(r"[a-zåäöéü0-9]+", s)

def sh(words, ort=None, k=5):
    o = ort.lower().split() if ort else []
    w = ["ORT" if x in o else x for x in words]
    return {" ".join(w[i:i + k]) for i in range(len(w) - k + 1)}

def jac(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0

def byggtorg(slug):
    fp = os.path.join(CACHE, slug + ".html")
    if not os.path.exists(fp):
        try:
            req = urllib.request.Request(f"https://byggtorg.se/{slug}/", headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
        except Exception:
            data = ""
        open(fp, "w", encoding="utf-8").write(data)
    s = open(fp, encoding="utf-8").read()
    if not s or "<main" not in s:  # 404 (HTTPError) sparas som tom fil
        return None
    return words_of(s)

BT_HUB = {"malare": ["malare"], "badrumsrenovering": ["badrumsrenovering"],
          "koksrenovering": ["koksrenovering", "koksrenovering-nacka"], "golvlaggning": ["golvlaggning", "vad-kostar-golvslipning"],
          "fasadrenovering": ["fasadrenovering"], "fonsterbyte": ["fonsterbyte"], "snickare": [],
          "byggforetag": ["byggforetag-stockholm"]}

pages = {p["file"]: p for p in G.PAGES if p["file"] in TJ}
# Sidor som skrivs parallellt (andra moduler) – länkar dit räknas inte som trasiga.
PLANNED = set(TJ_HUB.values()) | {f"malare-{o}.html" for o in "bromma solna huddinge sollentuna vallentuna norrtalje nacka taby".split()} \
    | {f"badrumsrenovering-{o}.html" for o in "bromma taby jarfalla".split()} \
    | {f"snickare-{o}.html" for o in "nacka sodermalm tyreso taby norrtalje".split()} | {"byggforetag-taby.html", "byggforetag-lidingo.html"}
sel = {f: d for f, d in TJ.items() if not ONLY or d["service"] == ONLY}
CYR = re.compile(r"[Ѐ-ӿ]")
BAD = [(r"\d[\d  ]*\s?(kr|kronor|:-)", "prisuppgift?"), (r"garanti", "garanti (bara 'enligt lag/konsumenttjänstlagen')"),
       (r"certifi|auktoriser|behörig", "cert/behörighet – bara om sajten redan anger det"),
       (r"omdöme|recension|betyg|nöjda kunder|stjärn", "omdömen"), (r"vi har (gjort|utfört|renoverat|målat|byggt)", "påstått eget uppdrag"),
       (r"alltid|aldrig", "absolut löfte?"), (r"inom 24|samma dag|snabbast", "svarstid?")]
existing_faq = set()
for p in G.PAGES:
    if p["file"] not in TJ:
        for q, _ in p.get("faq") or []:
            existing_faq.add(q.strip().lower())
seen_q = {}

def text_fields(d):
    out = [d["title"], d["description"], d["h1"], d["lead"], d.get("card", ""), d["steps_h2"], d["rot_h2"], d["price_h2"]]
    for s in d["sections"]:
        out += [s["h2"]] + s["paras"] + ([s["aside"]["title"]] + s["aside"]["items"] if s.get("aside") else [])
    out += [x for st in d["steps"] for x in st] + d["rot"] + d["price"] + [x for f in d["faq"] for x in f]
    out += [x[0] for x in d["img"]] + list(d["cta"]) + [x for r in d.get("related", []) for x in r[1:]]
    return out

wc = {}
for f, d in sel.items():
    p = pages.get(f)
    if not p:
        errors.append(f"{f}: inte renderad"); continue
    html = G.render(p)
    w = words_of(html)
    wc[f] = len(w)
    lo, hi = (1200, 1800) if d["kind"] == "hub" else (1200, 1500)
    if not lo <= len(w) <= hi + 150:
        (errors if len(w) < lo - 50 else warns).append(f"{f}: {len(w)} ord (mål {lo}–{hi})")
    t = G.short_title(d["title"])
    if len(t) > 60: warns.append(f"{f}: title {len(t)} tecken")
    if len(d["description"]) > 155: errors.append(f"{f}: description {len(d['description'])} tecken")
    if d["kind"] == "district":
        if not d["h1"].split(" i ")[-1].startswith(d["ort"]) and not d["title"].startswith(d["h1"].split(" – ")[0]):
            warns.append(f"{f}: H1/title ska börja med '<Tjänst> i {d['ort']}'")
    for x in text_fields(d):
        if CYR.search(x): errors.append(f"{f}: kyrilliska tecken i: {x[:60]}")
        plain = re.sub(r"<[^>]+>", " ", x)
        for rx, why in BAD:
            for m in re.finditer(rx, plain, re.I):
                ctx = plain[max(0, m.start() - 40):m.end() + 40]
                if why.startswith("pris") and re.search(r"50 000|75 000|30 procent|30 %", ctx): continue
                if why.startswith("garanti") and re.search(r"enligt lag|konsumenttjänstlag", ctx, re.I): continue
                warns.append(f"{f}: {why}: …{ctx.strip()}…")
    for href in re.findall(r'href="(?!https?:)([^"#]+\.html)', html):
        if not os.path.exists(os.path.join(ROOT, href)) and href not in TJ and href not in PLANNED:
            errors.append(f"{f}: trasig länk {href}")
    for q, _ in d["faq"]:
        k = q.strip().lower()
        if k in existing_faq: errors.append(f"{f}: FAQ finns redan på sajten: {q}")
        if k in seen_q: errors.append(f"{f}: FAQ dubblett med {seen_q[k]}: {q}")
        seen_q[k] = f
    if len(d["sources"]) < 3: warns.append(f"{f}: få källor ({len(d['sources'])})")
    for n in (f[:-5] + "-1", f[:-5] + "-2"):
        if not os.path.exists(os.path.join(ROOT, "assets", "images", n + ".webp")):
            warns.append(f"{f}: bild saknas {n}.webp") if VERB else None

# Likhet inom tjänst
shs = {f: sh(words_of(G.render(pages[f])), TJ[f].get("ort")) for f in sel if f in pages}
maxin, maxloc, maxbt = (0, "", ""), (0, ""), (0, "", "")
bysvc = {}
for f in shs: bysvc.setdefault(TJ[f]["service"], []).append(f)
for svc, fs in bysvc.items():
    for x, y in itertools.combinations(fs, 2):
        # hubben har inget ort-namn: jämför med ortsidans ord ersatta
        a = shs[x] if TJ[x].get("ort") else sh(words_of(G.render(pages[x])), TJ[y].get("ort"))
        b = shs[y] if TJ[y].get("ort") else sh(words_of(G.render(pages[y])), TJ[x].get("ort"))
        j = jac(a, b)
        if j > maxin[0]: maxin = (j, x, y)
        if j > 0.25: errors.append(f"likhet {j:.1%} {x} – {y} (> 25 %)")
        elif VERB: print(f"  {j:.1%} {x} – {y}")
# Mot ortens takläggar-/takrenoveringssida
for f in shs:
    o = TJ[f].get("ort")
    if not o: continue
    for other in (f"taklaggare-{G.slug(o)}.html", f"takrenovering-{G.slug(o)}.html"):
        fp = os.path.join(ROOT, other)
        if os.path.exists(fp):
            j = jac(shs[f], sh(words_of(open(fp, encoding="utf-8").read()), o))
            if j > maxloc[0]: maxloc = (j, f"{f} – {other}")
            if j > 0.25: errors.append(f"likhet {j:.1%} {f} – {other} (> 25 %)")
# Mot byggtorg.se
if "--no-byggtorg" not in ARGS:
    for f in shs:
        d = TJ[f]
        slugs = ([f[:-5]] if d["kind"] == "district" else []) + BT_HUB.get(d["service"], [])
        if d["kind"] == "hub" and d["service"] in BT_HUB: pass
        ours = sh(words_of(G.render(pages[f])))
        for s_ in slugs:
            bw = byggtorg(s_)
            if not bw: continue
            c = len(ours & sh(bw)) / len(ours)
            if c > maxbt[0]: maxbt = (c, f, s_)
            if c > 0.15: errors.append(f"byggtorg {c:.1%} {f} – byggtorg.se/{s_}/ (> 15 %)")
            elif VERB: print(f"  byggtorg {c:.1%} {f} – {s_}")

for f in sorted(wc): print(f"{wc[f]:5d} ord  {f}  | {G.short_title(TJ[f]['title'])}")
print(f"Parvis max inom tjänst: {maxin[0]:.1%} {maxin[1]} – {maxin[2]}")
print(f"Mot ortens tak-sidor: max {maxloc[0]:.1%} {maxloc[1]}")
print(f"Mot byggtorg (andel av våra shingles): max {maxbt[0]:.1%} {maxbt[1]} – {maxbt[2]}")
for w_ in warns: print("  WARN:", w_)
for e in errors: print("  FEL:", e)
sys.exit(1 if errors else 0)
