#!/usr/bin/env python3
"""Landing v3 (07.11.2026, ägaren: «taklia som förlaga»).
- Formulär som taklia: Namn | E-post, Telefon | Ort, Beskriv jobbet, Bifoga bild (valfritt).
- Sidans bilder bredvid texten (bild vänster/höger växelvis) i stället för separat galleri.
- Sista blocket "Begär offert" med formulär (ersätter cta-strip).
Körs efter landing_v2.py. Idempotent (markör data-v3)."""
import os, re, sys, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHONE_T, PHONE_D = "+46812410276", "08 12 410 276"
OLD_FORM = re.compile(r'<div class="form-box hero-form" id="offert">.*?</form>\s*</div>', re.S)
GAL = re.compile(r'\n      <section class="section gallery-section">.*?</section>', re.S)
FIG = re.compile(r'<figure>(<img [^>]*?/>)</figure>')
TEXT_SEC = re.compile(r'(<section class="section(?: section-muted)? seo-section"[^>]*>\s*<div class=")container(">\s*)'
                      r'<div class="section-copy section-copy--wide">(.*?)</div>(\s*</div>\s*</section>)', re.S)
CTA = re.compile(r'\n      <section class="section cta-strip">.*?</section>', re.S)


def val(s, name):
    m = re.search(rf'name="{name}" value="([^"]*)"', s)
    return m.group(1) if m else ""


def form(rubrik, tjanst, ort, retur, sfx="", hero=True):
    i = lambda x: x + sfx
    cls = "form-box hero-form" if hero else "form-box hero-form offer-form"
    idattr = ' id="offert"' if hero else ""
    h = "h2"
    return f"""<div class="{cls}"{idattr} data-v3>
            <{h}>{rubrik}</{h}>
            <p class="form-note">Beskriv jobbet så återkommer vi och bokar ett kostnadsfritt besök.</p>
            <p class="form-alert" data-form-fel role="alert" hidden>Något blev fel. Kontrollera uppgifterna eller ring <a href="tel:{PHONE_T}">{PHONE_D}</a>.</p>
            <form action="sendmail.php" method="post" enctype="multipart/form-data">
              <div class="hp-field" aria-hidden="true"><label for="{i('website')}">Lämna detta fält tomt</label><input id="{i('website')}" name="website" type="text" tabindex="-1" autocomplete="off" /></div>
              <input type="hidden" name="tjanst" value="{tjanst}" />
              <input type="hidden" name="retur" value="{retur}" />
              <input type="hidden" name="gdpr" value="1" />
              <div class="field-row">
                <div class="field"><label for="{i('namn')}">Namn</label><input id="{i('namn')}" name="namn" type="text" autocomplete="name" required /></div>
                <div class="field"><label for="{i('epost')}">E-post</label><input id="{i('epost')}" name="epost" type="email" autocomplete="email" required /></div>
              </div>
              <div class="field-row">
                <div class="field"><label for="{i('telefon')}">Telefon</label><input id="{i('telefon')}" name="telefon" type="tel" autocomplete="tel" /></div>
                <div class="field"><label for="{i('ort')}">Ort</label><input id="{i('ort')}" name="ort" type="text" value="{ort}" autocomplete="address-level2" /></div>
              </div>
              <div class="field"><label for="{i('meddelande')}">Beskriv jobbet – typ och ungefärlig yta</label><textarea id="{i('meddelande')}" name="meddelande" rows="3" required></textarea></div>
              <div class="field field-file"><label for="{i('bild')}">Bifoga bild (valfritt)</label><input id="{i('bild')}" name="bild" type="file" accept="image/*,.heic,.pdf" /></div>
              <button class="btn btn-primary btn-block" type="submit">Skicka förfrågan</button>
              <p class="form-legal">Genom att skicka godkänner du vår <a class="text-link" href="integritetspolicy.html">integritetspolicy</a>.</p>
            </form>
          </div>"""


def transform(path):
    s = open(path, encoding="utf-8").read()
    if "data-v3" in s or 'id="offert"' not in s:
        return False
    m = OLD_FORM.search(s)
    if not m:
        return False
    old = m.group(0)
    rubrik = re.search(r"<h2>(.*?)</h2>", old).group(1)
    tjanst, ort, retur = val(old, "tjanst"), val(old, "ort"), val(old, "retur")
    s = s.replace(old, form(rubrik, tjanst, ort, retur), 1)
    # bilder bredvid text
    g = GAL.search(s)
    if g:
        imgs = FIG.findall(g.group(0))
        secs = list(TEXT_SEC.finditer(s))
        k = min(len(imgs), len(secs))
        for n in range(k - 1, -1, -1):
            sm, img = secs[n], imgs[n]
            img = re.sub(r'sizes="[^"]*"', 'sizes="(max-width: 900px) 100vw, 560px"', img)
            side = " split-media--flip" if n % 2 else ""
            rep = (sm.group(1) + "container split-media" + side + sm.group(2)
                   + f'<figure class="split-figure">{img}</figure>\n          <div class="section-copy">'
                   + sm.group(3) + "</div>" + sm.group(4))
            s = s[:sm.start()] + rep + s[sm.end():]
        g = GAL.search(s)
        left = imgs[k:]
        if not left:
            s = s.replace(g.group(0), "", 1)
        else:
            new = g.group(0)
            for img in imgs[:k]:
                new = new.replace(f"<figure>{img}</figure>", "", 1)
            new = re.sub(r"\n\s*\n", "\n", new)
            cls = {1: "page-gallery page-gallery--one", 2: "page-gallery page-gallery--two"}.get(len(left), "page-gallery")
            new = re.sub(r'<div class="page-gallery[^"]*">', f'<div class="{cls}">', new)
            s = s.replace(g.group(0), new, 1)
    # Begär offert längst ner
    end = f"""
      <section class="section offer-section" id="begar-offert">
        <div class="container offer-grid">
          <div class="section-copy">
            <h2 class="section-title">Begär offert</h2>
            <p>Gratis besök och fast offert. Ring <a class="text-link" href="tel:{PHONE_T}">{PHONE_D}</a> eller skicka en förfrågan.</p>
          </div>
          {form("Få offert", tjanst, ort, retur, sfx="-2", hero=False)}
        </div>
      </section>"""
    c = CTA.search(s)
    s = s[:c.start()] + end + s[c.end():] if c else s.replace("\n    </main>", end + "\n    </main>", 1)
    open(path, "w", encoding="utf-8").write(s)
    return True


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    print("landing_v3:", sum(transform(os.path.join(ROOT, f)) for f in files))
