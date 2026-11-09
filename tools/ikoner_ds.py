#!/usr/bin/env python3
"""Ikoner (Recraft, ägaren 09.11.2026) på steg och «Därför väljer kunder oss» på DS-sidor.
Steg: ikon ur nyckelord i H3, annars efter position. Idempotent (data-ikon). Hoppar över om ikonfilen saknas."""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IC = os.path.join(ROOT, "assets", "icons")
RULES = [("rivning", ("riv", "nedtag")), ("tapet", ("tapet", "uppsättning")), ("slipning", ("slip",)),
         ("malning", ("målning", "ytbehandl", "stryk", "lasyr")), ("isolering", ("isoler",)),
         ("forarbete", ("förarbete", "underarbete", "lagning", "förbered", "skydd", "spackl", "kitt", "skrap", "underlag")),
         ("fonster", ("fönster",)), ("golv", ("golv", "läggning")), ("tak", ("tak", "läkt", "pann")),
         ("vvs", ("vvs", "installation", "stam", "el och")), ("montage", ("montage", "monter")),
         ("ritning", ("ritning", "karta", "plan", "skiss", "projekt")),
         ("lov", ("lov", "anmälan", "tillstånd", "ansökan", "slutbesked", "startbesked", "handling", "styrelse", "förening")),
         ("dokument", ("dokument", "intyg")), ("nyckel", ("överlämn", "nyckel", "inflytt")),
         ("kontroll", ("besiktning", "kontroll", "genomgång", "avslut", "prov")),
         ("besok", ("besök", "inventering")), ("offert", ("förslag", "offert", "pris", "avtal", "kalkyl")),
         ("bygg", ("bygg", "utförande", "renovering", "stomme", "grund"))]
FORDEL = {"Gratis besök": "besok", "Tydlig offert": "offert", "ROT-avdrag på fakturan": "rot", "Lokalt företag": "lokal"}


def ok(name):
    return os.path.exists(os.path.join(IC, name + ".svg"))


def pick(title, i, n):
    t = title.lower()
    for icon, keys in RULES:
        if any(k in t for k in keys):
            return icon
    return "besok" if i == 0 else "offert" if i == 1 else "kontroll" if i == n - 1 else "bygg"


def img(name, cls):
    return f'<img class="{cls}" src="assets/icons/{name}.svg" width="56" height="56" alt="" loading="lazy" decoding="async" data-ikon />'


def steps(m):
    out = m.group(0)
    arts = re.findall(r'<article class="step-item">.*?</article>', out, re.S)
    for i, a in enumerate(arts):
        h = re.search(r"<h3>(.*?)</h3>", a, re.S)
        name = "steg-" + pick(h.group(1) if h else "", i, len(arts))
        if not ok(name):
            continue
        b = re.sub(r'\s*<img class="step-img"[^>]*/>', "", a)
        b = b.replace('<article class="step-item">', '<article class="step-item">\n              ' + img(name, "step-icon"), 1)
        out = out.replace(a, b, 1)
    return out


def card(m):
    k = FORDEL.get(m.group(1))
    if not k or not ok("fordel-" + k):
        return m.group(0)
    return m.group(0).replace('<div class="trust-card">', '<div class="trust-card has-icon">' + img("fordel-" + k, "trust-icon"), 1)


def transform(path):
    s = open(path, encoding="utf-8").read()
    if "ds-taklia" not in s or "data-ikon" in s:
        return False
    s2 = re.sub(r'<section\b(?:(?!</section>).)*</section>', lambda m: steps(m) if "step-item" in m.group(0) else m.group(0), s, flags=re.S)
    s2 = re.sub(r'<div class="trust-card"><h3>(.*?)</h3>', card, s2)
    if s2 == s:
        return False
    open(path, "w", encoding="utf-8").write(s2)
    return True


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    print("ikoner:", sum(transform(os.path.join(ROOT, f)) for f in files))
