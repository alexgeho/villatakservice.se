#!/usr/bin/env python3
"""Landing v1 (07.11.2026): gör alla tjänst×ort-sidor (hero-grid--page) till landningssidor.

- Offertformulär i hero (ersätter hero-bilden), id="offert".
- Sidans bilder samlas i ett galleri direkt under hero (fristående figure-sektioner tas bort).
- Block "Därför väljer kunder oss" med verkliga fakta före FAQ.
- "Få offert"-knappar på sidan pekar på #offert.

Idempotent: sidor som redan har id="offert" hoppas över.
Körs efter generate.py (anropas i slutet av generate.main()).
Användning: python3 tools/landing_v1.py [fil.html ...]
"""
import os, re, sys, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHONE_T, PHONE_D = "+46812410276", "08 12 410 276"

HERO_FIG = re.compile(r'\s*<figure class="hero-side-visual">\s*(<img [^>]*?/>)\s*</figure>', re.S)
FIG_SEC = re.compile(r'\s*<section class="section(?: section-muted)? seo-section figure-section">\s*<div class="container">\s*'
                     r'<figure class="content-figure">\s*(<img [^>]*?/>)\s*(?:<figcaption>.*?</figcaption>\s*)?</figure>\s*</div>\s*</section>', re.S)
H1 = re.compile(r'<h1 class="hero-title">(.*?)</h1>', re.S)


def attr(img, name):
    m = re.search(rf'\b{name}="([^"]*)"', img)
    return m.group(1) if m else ""


def form_html(file, tjanst, ort):
    t = H.escape(tjanst, quote=True); o = H.escape(ort, quote=True)
    low = tjanst[0].lower() + tjanst[1:] if tjanst else ""
    prof = {"snickare", "målare", "plåtslagare", "takläggare", "golvläggare", "byggföretag"}
    rubrik = (f"Få offert från {low}" if low in prof else f"Få offert på {low}") if low else "Få offert"
    return f"""
          <div class="form-box hero-form" id="offert">
            <h2>{rubrik}</h2>
            <p class="form-note">Beskriv jobbet och ange adress eller ort.</p>
            <p class="form-alert" data-form-fel role="alert" hidden>Något blev fel. Kontrollera uppgifterna eller ring <a href="tel:{PHONE_T}">{PHONE_D}</a>.</p>
            <form action="sendmail.php" method="post">
              <div class="hp-field" aria-hidden="true"><label for="website">Lämna detta fält tomt</label><input id="website" name="website" type="text" tabindex="-1" autocomplete="off" /></div>
              <input type="hidden" name="tjanst" value="{t}" />
              <input type="hidden" name="ort" value="{o}" />
              <input type="hidden" name="retur" value="{file}" />
              <input type="hidden" name="gdpr" value="1" />
              <div class="field"><label for="namn">Namn</label><input id="namn" name="namn" type="text" autocomplete="name" required /></div>
              <div class="field"><label for="epost">E-post</label><input id="epost" name="epost" type="email" autocomplete="email" required /></div>
              <div class="field"><label for="telefon">Telefon</label><input id="telefon" name="telefon" type="tel" autocomplete="tel" /></div>
              <div class="field"><label for="meddelande">Beskriv jobbet</label><textarea id="meddelande" name="meddelande" rows="3" required></textarea></div>
              <button class="btn btn-primary btn-block" type="submit">Skicka förfrågan</button>
              <p class="form-legal">Genom att skicka godkänner du vår <a class="text-link" href="integritetspolicy.html">integritetspolicy</a>.</p>
            </form>
          </div>"""


def gallery_html(imgs):
    items = []
    for img in imgs:
        src, alt = attr(img, "src"), attr(img, "alt")
        srcset = attr(img, "srcset")
        ss = f' srcset="{srcset}" sizes="(max-width: 700px) 100vw, 33vw"' if srcset else ""
        items.append(f'            <figure><img src="{src}"{ss} width="{attr(img, "width")}" height="{attr(img, "height")}" alt="{alt}" loading="lazy" decoding="async" /></figure>')
    cls = "page-gallery" if len(imgs) > 1 else "page-gallery page-gallery--one"
    return f"""
      <section class="section gallery-section">
        <div class="container">
          <div class="{cls}">
{chr(10).join(items)}
          </div>
          <p class="gallery-note">Illustrationer</p>
        </div>
      </section>"""


TRUST = """
      <section class="section section-muted" id="varfor-oss">
        <div class="container">
          <h2 class="section-title">Därför väljer kunder oss</h2>
          <div class="trust-cards">
            <div class="trust-card"><h3>Gratis besök</h3><p>Vi tittar på jobbet på plats innan du får offert.</p></div>
            <div class="trust-card"><h3>Tydlig offert</h3><p>Du ser vad som ingår och vad det kostar.</p></div>
            <div class="trust-card"><h3>ROT-avdrag på fakturan</h3><p>Vi drar av ROT direkt och sköter ansökan.</p></div>
            <div class="trust-card"><h3>Lokalt företag</h3><p>Geal Entreprenad AB, Bromma. Org.nr 559303-7566.</p></div>
          </div>
        </div>
      </section>"""


def transform(path):
    s = open(path, encoding="utf-8").read()
    if 'id="offert"' in s or 'hero-grid--page' not in s:
        return False
    m = HERO_FIG.search(s)
    if not m:
        return False
    file = os.path.basename(path)
    h1 = re.sub(r"<[^>]+>", "", H.unescape(H1.search(s).group(1))).strip()
    sep = " i " if " i " in h1 else (" på " if " på " in h1 else None)
    tjanst, ort = h1.rsplit(sep, 1) if sep else (h1, "")
    imgs = [m.group(1)]
    s = s[:m.start()] + form_html(file, tjanst.strip(), ort.strip()) + s[m.end():]
    imgs += FIG_SEC.findall(s)
    s = FIG_SEC.sub("", s)
    # galleri direkt efter hero
    end = s.index("</section>", s.index('<section class="page-hero">')) + len("</section>")
    s = s[:end] + gallery_html(imgs) + s[end:]
    # förtroendeblock före FAQ (annars före CTA)
    for anchor in ('      <section class="section seo-section" id="faq">', '      <section class="section cta-strip">'):
        if anchor in s:
            s = s.replace(anchor, TRUST.lstrip("\n") + "\n" + anchor, 1)
            break
    s = s.replace('href="kontakt.html#form"', 'href="#offert"')
    open(path, "w", encoding="utf-8").write(s)
    return True


def main(files=None):
    files = files or sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    n = sum(transform(os.path.join(ROOT, f)) for f in files)
    print(f"landing_v1: {n} sidor uppdaterade")


if __name__ == "__main__" and sys.argv[1:]:
    main(sys.argv[1:])


# ---- Sidor utan hero-bild (takläggare-orter, tak-tjänster, guider) ---------
SKIP = {"404.html", "artiklar.html", "faq.html", "integritetspolicy.html", "kontakt.html", "om-oss.html",
        "omraden.html", "sok.html", "tack.html", "tjanster.html", "villkor.html", "kalkylator-takbyte.html",
        "offert-dalarna.html", "index.html", "bygg.html"}
KEYS = [("takbyte", "Takbyte"), ("takrenovering", "Takrenovering"), ("takmalning", "Takmålning"),
        ("mala-plattak", "Takmålning"), ("taktvatt", "Taktvätt"), ("mossa", "Taktvätt"),
        ("takbesiktning", "Takbesiktning"), ("plattak", "Plåttak"), ("papptak", "Papptak"),
        ("takfonster", "Takfönster"), ("skorsten", "Skorstensrenovering"), ("hangrannor", "Hängrännor"),
        ("taksakerhet", "Taksäkerhet"), ("vindsisolering", "Vindsisolering"), ("energieffektivt", "Vindsisolering"),
        ("fuktskada", "Takbesiktning"), ("taklackage", "Takreparation"), ("attefallshus", "Attefallshus"),
        ("friggebod", "Friggebod"), ("fritidshus", "Fritidshus"), ("nybyggnad", "Nybyggnad"),
        ("bygga-hus", "Nybyggnad"), ("byggfirma", "Byggföretag"), ("tillbyggnad", "Tillbyggnad"),
        ("villarenovering", "Villarenovering")]
PLAIN_HERO = re.compile(r'(<section class="page-hero">\s*)<div class="container">(.*?)(\n        </div>\n      </section>)', re.S)


def transform_plain(path):
    file = os.path.basename(path)
    if file in SKIP:
        return False
    s = open(path, encoding="utf-8").read()
    if 'id="offert"' in s or 'hero-grid--page' in s:
        return False
    m = PLAIN_HERO.search(s)
    if not m:
        return False
    h1 = re.sub(r"<[^>]+>", "", H.unescape(H1.search(s).group(1))).strip()
    if file.startswith("taklaggare-"):
        tjanst = "Takläggare"
        sep = " i " if " i " in h1 else " på "
        ort = h1.rsplit(sep, 1)[1] if sep in h1 else ""
    else:
        tjanst = next((v for k, v in KEYS if k in file), "Takarbete")
        ort = ""
    inner = m.group(2).replace("\n          ", "\n            ")
    new = (m.group(1) + '<div class="container hero-grid hero-grid--page">\n          <div class="hero-copy">'
           + inner + "\n          </div>" + form_html(file, tjanst, ort) + m.group(3))
    s = s[:m.start()] + new + s[m.end():]
    for anchor in ('      <section class="section seo-section" id="faq">', '      <section class="section cta-strip">'):
        if anchor in s:
            s = s.replace(anchor, TRUST.lstrip("\n") + "\n" + anchor, 1)
            break
    s = s.replace('href="kontakt.html#form"', 'href="#offert"').replace('href="offert-dalarna.html#form"', 'href="#offert"')
    open(path, "w", encoding="utf-8").write(s)
    return True


def main_all():
    files = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    n = sum(transform(os.path.join(ROOT, f)) for f in files)
    n2 = sum(transform_plain(os.path.join(ROOT, f)) for f in files)
    print(f"landing_v1: {n} + {n2} sidor uppdaterade")


if __name__ == "__main__" and not sys.argv[1:]:
    main_all()


# ---- Galleri för sidor som fick bilder senare (gen_images_landing.py) ------
def add_gallery(path):
    s = open(path, encoding="utf-8").read()
    if 'id="offert"' not in s or "gallery-section" in s or "data-ds" in s or "data-v3" in s:
        return False
    base = os.path.basename(path)[:-5]
    names = [f"{base}-{i}" for i in (1, 2, 3) if os.path.exists(os.path.join(ROOT, "assets", "images", f"{base}-{i}.webp"))]
    if len(names) < 3:
        return False
    h1 = re.sub(r"<[^>]+>", "", H.unescape(H1.search(s).group(1))).strip()
    detalj = "Nytt underlag och läkt vid takarbete" if base.startswith("taklaggare-") else f"{h1} – detalj"
    alts = [h1, detalj, "Färdigt tak med nock, plåtdetaljer och hängrännor"]
    from PIL import Image
    imgs = []
    for n, alt in zip(names, alts):
        w, hgt = Image.open(os.path.join(ROOT, "assets", "images", n + ".webp")).size
        imgs.append(f'<img src="assets/images/{n}.webp" srcset="assets/images/{n}-640.webp 640w, assets/images/{n}.webp {w}w" width="{w}" height="{hgt}" alt="{H.escape(alt, quote=True)}" />')
    end = s.index("</section>", s.index('<section class="page-hero">')) + len("</section>")
    s = s[:end] + gallery_html(imgs) + s[end:]
    open(path, "w", encoding="utf-8").write(s)
    return True


if __name__ == "__main__" and not sys.argv[1:]:
    files = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    print("galleri:", sum(add_gallery(os.path.join(ROOT, f)) for f in files))
