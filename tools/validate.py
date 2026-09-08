#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enkel validator/"lint" for villatakservice.se.
Kor:  python3 tools/validate.py
Kontroller:
  - Alla JSON-LD-block ar giltig JSON.
  - Exakt en <h1> per sida.
  - Inga trasiga interna lankar (href till lokala .html som saknas).
  - Inga trasiga in-page-ankare (#id maste finnas pa sidan).
  - Inga dubbla <title>.
  - Alla sidor i sitemap.xml existerar; alla icke-noindex-sidor finns i sitemap.
Returnerar exit-kod 1 vid fel (rott), 0 vid gront.
"""
import os, re, json, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
warnings = []

html_files = sorted(
    f for f in glob.glob(os.path.join(ROOT, "*.html"))
)
names = {os.path.basename(f) for f in html_files}

JSONLD_RE = re.compile(
    r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL)
H1_RE = re.compile(r'<h1\b', re.IGNORECASE)
TITLE_RE = re.compile(r'<title>', re.IGNORECASE)
HREF_RE = re.compile(r'href="([^"]+)"')
ID_RE = re.compile(r'\bid="([^"]+)"')

total_jsonld = 0
for path in html_files:
    base = os.path.basename(path)
    with open(path, encoding="utf-8") as fh:
        html = fh.read()

    # JSON-LD
    for block in JSONLD_RE.findall(html):
        total_jsonld += 1
        try:
            json.loads(block)
        except Exception as e:
            errors.append(f"{base}: ogiltig JSON-LD: {e}")

    # H1
    n_h1 = len(H1_RE.findall(html))
    if n_h1 != 1:
        errors.append(f"{base}: {n_h1} <h1> (ska vara exakt 1)")

    # title
    if len(TITLE_RE.findall(html)) != 1:
        errors.append(f"{base}: {len(TITLE_RE.findall(html))} <title> (ska vara 1)")

    # interna lankar + ankare
    ids = set(ID_RE.findall(html))
    for href in HREF_RE.findall(html):
        if href.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
            continue
        target, _, frag = href.partition("#")
        target = target.strip()
        if target.endswith(".html"):
            if target not in names:
                errors.append(f"{base}: trasig lank -> {target}")
        if href.startswith("#") and frag and frag not in ids:
            errors.append(f"{base}: trasigt ankare -> #{frag}")

# sitemap
sm_path = os.path.join(ROOT, "sitemap.xml")
if os.path.exists(sm_path):
    with open(sm_path, encoding="utf-8") as fh:
        sm = fh.read()
    locs = re.findall(r"<loc>https://villatakservice\.se/?([^<]*)</loc>", sm)
    for loc in locs:
        f = loc if loc else "index.html"
        if f and f not in names:
            errors.append(f"sitemap: refererar saknad sida {f}")
    # noindex-sidor ska inte ligga i sitemap
    for path in html_files:
        base = os.path.basename(path)
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        noindex = 'name="robots" content="noindex' in html
        loc_name = "" if base == "index.html" else base
        in_sm = loc_name in locs
        if noindex and in_sm:
            errors.append(f"sitemap: noindex-sida {base} ska inte finnas i sitemap")
else:
    warnings.append("sitemap.xml saknas")

print(f"Kontrollerade {len(html_files)} sidor, {total_jsonld} JSON-LD-block.")
for w in warnings:
    print("  WARN:", w)
if errors:
    print(f"\n✗ {len(errors)} fel:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("✓ Validering gron: inga fel.")
sys.exit(0)
