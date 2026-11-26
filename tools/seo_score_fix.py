#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-poäng ≥ 80 (Rank Math-stil, ~/nordkod/scripts/seo-score.mjs), ägaren 26.11.2026.

Körs SIST i generate.py (efter seo_overrides.py). Idempotent. Gäller alla sidor, även de
handgjorda (index, tjanster, om-oss, kontakt, artiklar, takbyte).

Fokussökord = titelns första del (före « – », « | », «: », «, »), max 6 ord – samma regel som
poängskriptet – eller FOCUS nedan när titelns början inte är sökordet (frågetitlar).

Vad skriptet gör (bara där det saknas):
  0. H1 enligt H1-tabellen nedan (sidor där H1 och titel hade olika fraser).
  1. Dekorativa bilder (alt="") får aria-hidden="true" (ikoner, logga).
  2. Sökordet i en bild-alt: hero-bilden (annars första innehållsbilden) får « – <sökord>» sist.
  3. Sökordet i en H2: rubriken «Vanliga frågor» blir «<Sökord> – vanliga frågor».
  4. Sökordet i meta description: «Fönsterrenovering i Bromma: …» → «Fönsterrenovering Bromma: …»
     när titeln/H1 använder formen utan preposition (samma text i og:description och JSON-LD).
  5. Extern källa saknas: första «ROT-avdrag» i ett stycke länkas till Skatteverkets sida om rotavdraget,
     annars första «bygglov»/«inget lov» till Boverkets PBL-kunskapsbank om fasadändring.

Användning: python3 tools/seo_score_fix.py [--check]
"""
import os, re, sys, glob, unicodedata, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Sida → fokussökord när titelns början är en fråga/jämförelse (speglas i
# ~/nordkod/scripts/seo-focus-keywords.json så att poängskriptet räknar på samma ord).
FOCUS = {
    "mala-plattak.html": "måla om plåttaket",
    "tegel-betong-plattak.html": "betongpannor",
    "takmaterial-livslangd.html": "livslängd",
    "vad-kostar-takrenovering.html": "vad kostar takrenovering",
    "vad-kostar-takbyte.html": "vad kostar ett takbyte",
    "rot-avdrag-takarbete.html": "ROT-avdrag",
}

ROT_URL = ("https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/"
           "safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

PBL_URL = "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/"

# H1 som ska bära sökordet. Sätts här (efter landing_v1/rollout_ds) och inte i generatorn, eftersom
# generatorns H1 används för formulärets dolda fält tjanst/ort (samma skäl som h1_overrides i seo_overrides.py).
H1 = {
    "takrenovering.html": "Takrenovering i Stockholm – takomläggning och reparation",
    "takbesiktning.html": "Besikta tak i Stockholm – takbesiktning på villan",
    "taklaggare-sollentuna.html": "Takläggare Sollentuna – gratis besök och kostnadsförslag",
    "byggforetag-hagersten.html": "Byggföretag Hägersten – gratis besök och kostnadsförslag",
}

def fold(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def has(hay, kw):
    return f" {kw} " in f" {fold(hay)} "


def strip(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def keyword(fn, title):
    if fn in FOCUS:
        return FOCUS[fn]
    base = re.split(r"\s[–|—-]\s|\s\|\s|:\s|,\s", title)[0]
    return " ".join(re.sub(r"\s+", " ", base).strip().split(" ")[:6])


def lcfirst(s):
    w = s.split(" ")[0]
    if len(w) > 1 and w[1:2].isupper():  # ROT-avdrag, PBL …
        return s
    return s[:1].lower() + s[1:]


def main_region(s):
    m = re.search(r"<main\b[^>]*>(.*)</main>", s, re.S)
    r = m.group(1) if m else s
    for t in ("script", "style", "nav", "header", "footer", "form", "aside"):
        r = re.sub(rf"<{t}\b.*?</{t}>", " ", r, flags=re.S)
    return r


def fix(fn, s):
    if re.search(r'<meta name="robots" content="[^"]*noindex', s):
        return s, []
    tm = re.search(r"<title>(.*?)</title>", s, re.S)
    if not tm:
        return s, []
    title = H.unescape(tm.group(1)).strip()
    if fn in H1:
        s = re.sub(r'(<h1 class="hero-title">)(.*?)(</h1>)', lambda g: g.group(1) + H.escape(H1[fn], quote=False) + g.group(3),
                   s, count=1, flags=re.S)
    kw = keyword(fn, title)
    k = fold(kw)
    notes = []

    # 1. dekorativa bilder
    s = re.sub(r'<img\b(?![^>]*aria-hidden)([^>]*?) alt=""', r'<img\1 alt="" aria-hidden="true"', s)

    # 2. sökordet i en alt-text
    alts = [H.unescape(a) for a in re.findall(r'<img\b[^>]*\balt="([^"]*)"', s)]
    if not any(has(a, k) for a in alts):
        reg = main_region(s)
        cand = re.search(r'<img class="hero-bg"[^>]*\balt="([^"]+)"', s) or \
            re.search(r'<img\b(?![^>]*aria-hidden)[^>]*\balt="([^"]+)"', reg)
        if cand:
            old = cand.group(0)
            new = old.replace(f'alt="{cand.group(1)}"', f'alt="{cand.group(1)} – {H.escape(lcfirst(kw), quote=True)}"')
            s = s.replace(old, new, 1)
        else:
            notes.append("alt")

    # 3. sökordet i en H2/H3
    subs = [strip(h) for h in re.findall(r"<h[23]\b[^>]*>(.*?)</h[23]>", main_region(s), re.S)]
    if not any(has(h, k) for h in subs):
        faq = re.search(r'(<h2 class="section-title">)Vanliga (?:<em>)?frågor(?:</em>)?(</h2>)', s)
        if faq and not k.startswith("vanliga fragor"):
            s = s.replace(faq.group(0), faq.group(1) + f"{kw[:1].upper() + kw[1:]} – vanliga <em>frågor</em>" + faq.group(2), 1)
        else:
            notes.append("h2")

    # 4. sökordet i meta description
    dm = re.search(r'<meta name="description" content="([^"]*)"', s)
    if dm and not has(H.unescape(dm.group(1)), k):
        old = dm.group(1)
        new = None
        for prep in (" i ", " på "):
            i = old.find(prep)
            if 0 < i <= len(kw) + 2:
                c = old[:i] + " " + old[i + len(prep):]
                if fold(c).startswith(k + " "):
                    new = c
                    break
        if new:
            s = s.replace(f'content="{old}"', f'content="{new}"')
            s = s.replace(f'"description": "{H.unescape(old)}"', f'"description": "{H.unescape(new)}"')
        else:
            notes.append("meta")
    # 5. en extern källa: första «ROT-avdrag» i ett stycke länkas till Skatteverket
    reg = main_region(s)
    if not re.search(r'<a\b[^>]*href="https?://(?!(?:www\.)?villatakservice\.se)', reg):
        reg = re.sub(r'<section[^>]*id="varfor-oss".*?</section>', " ", reg, flags=re.S)  # fördelskorten
        done = False
        for pat, url in ((r"ROT-avdrag(?:et)?|\bROT\b", ROT_URL), (r"\binget (?:bygg)?lov\b", PBL_URL), (r"\bbygglov\b", PBL_URL)):
            for para in re.findall(r"<p\b[^>]*>.*?</p>", reg, re.S):
                m = re.search(pat, para)
                if not m or para[:m.start()].count("<a ") != para[:m.start()].count("</a>") or para not in s:
                    continue
                new_p = para[:m.start()] + f'<a class="text-link" href="{url}" rel="noopener">{m.group(0)}</a>' + para[m.end():]
                s = s.replace(para, new_p, 1)
                done = True
                break
            if done:
                break
        if not done:
            notes.append("extern")
    return s, notes


def main():
    check = "--check" in sys.argv
    changed, todo = [], []
    for fp in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        fn = os.path.basename(fp)
        src = open(fp, encoding="utf-8").read()
        out, notes = fix(fn, src)
        if notes:
            todo.append(f"{fn}: {','.join(notes)}")
        if out != src:
            changed.append(fn)
            if not check:
                open(fp, "w", encoding="utf-8").write(out)
    if "-v" in sys.argv and todo:
        print("Manuellt (saknar FAQ-rubrik/hero-bild/description i formen «Tjänst i Ort:»):\n  " + "\n  ".join(todo))
    if check and changed:
        print("seo_score_fix saknas på:", ", ".join(changed[:20]))
        sys.exit(1)
    print(f"seo_score_fix: {len(changed)} sidor ändrade, {len(todo)} med manuella punkter.")


if __name__ == "__main__":
    main()
