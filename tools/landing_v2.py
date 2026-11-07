#!/usr/bin/env python3
"""Landing v2 (07.11.2026, ägaren): bakgrundsbild i hero, fördelar direkt under hero, sedan galleri.
Körs efter landing_v1.py. Idempotent (hoppar över sidor med page-hero--bg)."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAL = re.compile(r'\n      <section class="section gallery-section">.*?</section>', re.S)
FIG = re.compile(r'\s*<figure><img [^>]*?/></figure>')
TRUST = re.compile(r'      <section class="section section-muted" id="varfor-oss">.*?</section>\n', re.S)


def transform(path):
    s = open(path, encoding="utf-8").read()
    if 'id="offert"' not in s or "page-hero--bg" in s:
        return False
    g = GAL.search(s)
    if not g:
        return False
    gal = g.group(0)
    figs = FIG.findall(gal)
    first = figs[0]
    src = re.search(r'src="([^"]+)"', first).group(1)
    ss = re.search(r'srcset="([^"]+)"', first)
    ss = f' srcset="{ss.group(1)}" sizes="100vw"' if ss else ""
    # bort med första bilden ur galleriet
    rest = figs[1:]
    if rest:
        gal2 = gal.replace(first, "", 1)
        cls = {1: "page-gallery page-gallery--one", 2: "page-gallery page-gallery--two"}.get(len(rest), "page-gallery")
        gal2 = re.sub(r'<div class="page-gallery[^"]*">', f'<div class="{cls}">', gal2)
    else:
        gal2 = ""
    s = s.replace(gal, "", 1)
    # hero med bakgrundsbild
    s = s.replace('<section class="page-hero">',
                  f'<section class="page-hero page-hero--bg">\n        <img class="hero-bg" src="{src}"{ss} alt="" fetchpriority="high" decoding="async" />', 1)
    # fördelar flyttas direkt under hero, galleriet efter
    t = TRUST.search(s)
    trust = t.group(0) if t else ""
    if t:
        s = s.replace(trust, "", 1)
    end = s.index("</section>", s.index('<section class="page-hero page-hero--bg">')) + len("</section>")
    s = s[:end] + "\n" + trust.rstrip("\n") + gal2 + s[end:]
    open(path, "w", encoding="utf-8").write(s)
    return True


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    print("landing_v2:", sum(transform(os.path.join(ROOT, f)) for f in files))
