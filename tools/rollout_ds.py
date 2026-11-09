#!/usr/bin/env python3
"""Utrullning av pilot takbyte.html (ägarens «ok» 09.11.2026) till alla landningssidor.
DS taklia (ds-taklia.css + body.ds-taklia), header med logga 5A, hero som pilot (lead 1 mening,
«Det här ingår» + bockar), formulär v3, block: H2 ovanför; foto+text (sidans bilder) / bara text,
>2 stycken → resten under «Läs mer»; bullet-list → bockar; cta-strip → «Begär offert» med formulär.
Idempotent (markör data-ds). Körs efter landing_v1/v2 i generate.py.
Användning: python3 tools/rollout_ds.py [fil.html ...]"""
import os, re, sys, html as H, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PILOT = os.path.join(ROOT, "takbyte.html")
PHONE_T, PHONE_D = "+46812410276", "08 12 410 276"

INGAR = {
 "Takbyte": ["Rivning och bortforsling", "Ny underlagspapp och läkt", "Tegel, betongpannor eller plåt", "Plåt kring skorsten", "Hängrännor och stuprör", "Slutkontroll med dig"],
 "Takläggare": ["Takbyte och takrenovering", "Underlagspapp och läkt", "Tegel, betong och plåt", "Plåtdetaljer och skorsten", "Hängrännor och snörasskydd", "Slutkontroll med dig"],
 "Takrenovering": ["Besiktning av taket", "Byte av trasiga pannor", "Tätning kring skorsten", "Nya plåtdetaljer", "Rengöring och behandling", "Slutkontroll med dig"],
 "Takarbete": ["Besiktning av taket", "Tydlig offert", "Material och plåtdetaljer", "Ställning och skydd", "Städning efter jobbet", "Slutkontroll med dig"],
 "Plåtslagare": ["Plåttak och falsning", "Skorstensbeslag", "Hängrännor och stuprör", "Fönsterbleck", "Snörasskydd och takstegar", "Slutkontroll med dig"],
 "Plåttak": ["Rivning av gammalt tak", "Nytt underlag", "Falsad plåt", "Skorstensbeslag", "Hängrännor och stuprör", "Slutkontroll med dig"],
 "Snickare": ["Platsbesök och offert", "Altaner och trall", "Dörrar och fönster", "Lister och foder", "Inbyggnader och förråd", "Städning efter jobbet"],
 "Målare": ["Skydd av golv och möbler", "Spackling och slipning", "Grundning", "Två strykningar", "Tak, väggar och snickerier", "Städning efter jobbet"],
 "Tapetsering": ["Skydd av golv och möbler", "Nedtagning av gammal tapet", "Spackling och slipning", "Grundning", "Uppsättning av ny tapet", "Städning efter jobbet"],
 "Köksrenovering": ["Rivning och bortforsling", "El och VVS med behörighet", "Skåp, bänkskivor och vitvaror", "Kakel och stänkskydd", "Golv och målning", "Slutkontroll med dig"],
 "Badrumsrenovering": ["Rivning och bortforsling", "Tätskikt enligt branschregler", "VVS och el med behörighet", "Kakel och klinker", "Porslin och inredning", "Våtrumsintyg"],
 "Totalrenovering": ["Rivning och bortforsling", "El och VVS med behörighet", "Kök och badrum", "Väggar och golv", "Målning och snickerier", "Slutkontroll med dig"],
 "Villarenovering": ["Rivning och bortforsling", "El och VVS med behörighet", "Kök och badrum", "Väggar och golv", "Målning och snickerier", "Slutkontroll med dig"],
 "Fönsterbyte": ["Mätning på plats", "Demontering av gamla fönster", "Montage och drevning", "Fönsterbleck", "Foder och lister", "Bortforsling"],
 "Fönsterrenovering": ["Skrapning av gammal färg", "Kittning", "Byte av trasigt glas", "Linoljefärg", "Tätningslister", "Justering av beslag"],
 "Fasadrenovering": ["Besiktning av fasaden", "Ställning och skydd", "Lagning av skador", "Ny puts eller panel", "Målning", "Slutkontroll med dig"],
 "Fasadmålning": ["Ställning och skydd", "Tvätt av fasaden", "Skrapning och lagning", "Grundning", "Två strykningar", "Slutkontroll med dig"],
 "Golvslipning": ["Flytt av möbler", "Slipning i flera steg", "Lagning av skador", "Lack, olja eller lut", "Lister vid behov", "Städning efter jobbet"],
 "Golvläggare": ["Bortforsling av gammalt golv", "Avjämning av underlaget", "Stegljudsskydd", "Parkett, laminat eller vinyl", "Trösklar och lister", "Städning efter jobbet"],
 "Golvläggning": ["Bortforsling av gammalt golv", "Avjämning av underlaget", "Stegljudsskydd", "Parkett, laminat eller vinyl", "Trösklar och lister", "Städning efter jobbet"],
 "Byggföretag": ["Platsbesök och offert", "Bygglov och anmälan vid behov", "Grund och stomme", "Tak och fasad", "El och VVS med behörighet", "Slutkontroll med dig"],
 "Attefallshus": ["Anmälan och ritningar", "Grund", "Stomme och tak", "Fönster och dörrar", "Isolering och invändigt", "Slutkontroll med dig"],
 "Tillbyggnad": ["Bygglov och ritningar", "Grund", "Stomme och tak", "Anslutning till huset", "El och VVS med behörighet", "Slutkontroll med dig"],
 "Nybyggnad": ["Bygglov och ritningar", "Grund", "Stomme och tak", "Fasad och fönster", "El och VVS med behörighet", "Slutkontroll med dig"],
}
NOTE = {"Takbyte": "Skicka gärna en bild på taket.", "Takläggare": "Skicka gärna en bild på taket.",
        "Takrenovering": "Skicka gärna en bild på taket.", "Takarbete": "Skicka gärna en bild på taket.",
        "Plåtslagare": "Skicka gärna en bild på taket.", "Plåttak": "Skicka gärna en bild på taket."}
PROF = {"Snickare", "Målare", "Plåtslagare", "Takläggare", "Golvläggare", "Byggföretag"}
PRIS = {"Takbyte": "från 1 400 kr/m² inkl. material, före ROT-avdrag"}


def pilot_parts():
    p = open(PILOT, encoding="utf-8").read()
    header = re.search(r'<header class="site-header">.*?</header>', p, re.S).group(0)
    form = re.search(r'<div class="form-box hero-form" id="offert" data-v3>.*?</form>\s*</div>', p, re.S).group(0)
    offer = re.search(r'      <section class="section(?: section-muted)? offer-section" id="begar-offert">.*?</section>', p, re.S).group(0)
    css = re.search(r'<link rel="stylesheet" href="assets/css/ds-taklia.css\?v=[^"]*" />', p).group(0)
    return header, form, offer, css


def em_last(h2):
    if "<em>" in h2:
        return h2
    m = re.search(r'([A-Za-zÅÄÖåäöÉé0-9–-]+)([?!.:]?)\s*$', h2)
    if not m or "<" in h2[m.start():]:
        return h2
    return h2[:m.start()] + f"<em>{m.group(1)}</em>{m.group(2)}"


def set_form(form, tjanst, ort, retur, note, rubrik):
    f = re.sub(r'name="tjanst" value="[^"]*"', f'name="tjanst" value="{tjanst}"', form)
    f = re.sub(r'name="retur" value="[^"]*"', f'name="retur" value="{retur}"', f)
    f = re.sub(r'(name="ort" type="text" value=")[^"]*"', rf'\g<1>{ort}"', f)
    f = re.sub(r'<p class="form-note">[^<]*</p>', f'<p class="form-note">{note}</p>', f)
    if rubrik is not None:
        f = re.sub(r'<h3>[^<]*</h3>', f'<h3>{rubrik}</h3>', f, count=1)
    return f


def first_sentence(t):
    m = re.match(r'(.+?[.!?])(\s+[A-ZÅÄÖ0-9].*)?$', t, re.S)
    return (m.group(1), (m.group(2) or "").strip()) if m else (t, "")


SEC = re.compile(r'      <section class="section(?: section-muted)? seo-section"([^>]*)>(.*?)</section>', re.S)
WRAP = re.compile(r'\s*<div class="(?:container(?: section-layout[^"]*)?|section-copy(?: section-copy--wide)?)">')


def unwrap(t):
    """Ta bort container/section-copy/side-panel-omslag; kvar: h2, p, h3, listor, tips-box."""
    n_open = len(WRAP.findall(t))
    t = WRAP.sub("", t)
    n_close = 0
    if 'class="side-panel"' in t:
        t, k = re.subn(r'\s*</div>\s*<aside class="side-panel">', "", t); n_close += k
        t = t.replace("</aside>", "")
    t = t.rstrip()
    for _ in range(n_open - n_close):
        assert t.endswith("</div>"), "omslag"
        t = t[:-6].rstrip()
    return t + "\n"


TOP_P = re.compile(r'\n\s*<p[ >].*?</p>', re.S)


def text_block(attrs, inner, img, flip, intro=""):
    h2m = re.search(r'<h2 class="section-title">(.*?)</h2>', inner, re.S)
    h2 = em_last(h2m.group(1).strip())
    body = inner[h2m.end():]
    if intro:
        body = f'\n            <p>{intro}</p>' + body
    if "Källor" not in h2:
        body = body.replace('class="bullet-list"', 'class="fact-list"')
    # >2 stycken: resten under «Läs mer»
    ps = list(TOP_P.finditer(body))
    if len(ps) > 2:
        cut = ps[1].end()
        body = body[:cut] + '\n            <details class="read-more"><summary>Läs mer</summary>' + body[cut:].rstrip() + '\n            </details>\n          '
    body = body.rstrip() + "\n"
    head = f'        <div class="container block-head-wrap"><div class="block-head"><h2 class="section-title">{h2}</h2></div></div>\n'
    if img:
        fl = " split-media--flip" if flip else ""
        mid = (f'        <div class="container split-media{fl}">\n          <figure class="split-figure">{img}</figure>\n'
               f'          <div class="section-copy">{body}          </div>\n        </div>\n')
        cls = "seo-section media-block"
    else:
        mid = f'        <div class="container text-block">{body}        </div>\n'
        cls = "seo-section media-block"
    return f'      <section class="section {cls}"{attrs}>\n{head}{mid}      </section>'


def transform(path, parts):
    header, pform, offer, css = parts
    s = open(path, encoding="utf-8").read()
    if "data-ds" in s or 'id="offert"' not in s or os.path.basename(path) == "takbyte.html":
        return False
    retur = os.path.basename(path)
    tj = (re.search(r'name="tjanst" value="([^"]*)"', s) or [None, ""])[1]
    ort = (re.search(r'name="ort"[^>]*value="([^"]*)"', s) or [None, ""])[1]
    # head + body
    s = re.sub(r'(<link rel="stylesheet" href="assets/css/style\.css[^"]*" />)', r'\1\n    ' + css, s, count=1)
    s = s.replace("<body>", '<body class="ds-taklia" data-ds>', 1)
    s = re.sub(r'<header class="site-header">.*?</header>', lambda m: header, s, count=1, flags=re.S)
    # hero
    hm = re.search(r'(<div class="container hero-grid hero-grid--page">\s*)<div class="hero-copy">(.*?)\n          </div>\s*<div class="form-box hero-form" id="offert".*?</form>\s*</div>', s, re.S)
    copy = hm.group(2)
    bc = re.search(r'<p class="breadcrumb">.*?</p>', copy, re.S).group(0).replace(" / ", " › ")
    h1 = re.search(r'<h1 class="hero-title">.*?</h1>', copy, re.S).group(0)
    lm = re.search(r'<p class="section-lead">(.*?)</p>', copy, re.S)
    lead, rest = first_sentence(lm.group(1).strip()) if lm else ("", "")
    h1t = re.sub(r"<[^>]+>", "", H.unescape(h1)).strip()
    low = tj[0].lower() + tj[1:] if tj else ""
    rub = (f"Få offert från {low}" if tj in PROF else f"Få offert på {low}") if tj else "Få offert"
    form = set_form(pform, tj, ort, retur, NOTE.get(tj, "Beskriv jobbet kort."), rub)
    rest_html = ""
    if tj in INGAR:
        lis = "\n".join(f"              <li>{x}</li>" for x in INGAR[tj])
        pr = f'\n            <p class="hero-price"><strong>Pris:</strong> {PRIS[tj]}</p>' if tj in PRIS else ""
        rest_html = (f'\n          <div class="hero-copy hero-rest">\n            <h3>Det här ingår</h3>\n'
                     f'            <ul class="hero-checks">\n{lis}\n            </ul>{pr}\n          </div>')
    hero = (hm.group(1) + f'<div class="hero-copy hero-top">\n            {bc}\n            {h1}\n'
            + (f'            <p class="section-lead">{lead}</p>\n' if lead else "") + "          </div>\n          "
            + form + rest_html)
    s = s[:hm.start()] + hero + s[hm.end():]
    # galleri → bilder till block
    imgs = []
    g = re.search(r'\n      <section class="section gallery-section">.*?</section>', s, re.S)
    if g:
        for im in re.findall(r'<figure>(<img [^>]*?/>)</figure>', g.group(0)):
            im = re.sub(r'sizes="[^"]*"', 'sizes="(max-width: 900px) 100vw, 560px"', im)
            imgs.append(im)
        s = s[:g.start()] + s[g.end():]
    # varför oss: accent
    s = s.replace('<h2 class="section-title">Därför väljer kunder oss</h2>', '<h2 class="section-title">Därför väljer kunder <em>oss</em></h2>')
    # textsektioner
    out, pos, k, first = [], 0, 0, True
    for m in SEC.finditer(s):
        inner = m.group(2)
        if '<h2 class="section-title">' in inner and not any(x in inner for x in ("step-item", "service-snippet", "area-list", "faq-")):
            inner = unwrap(inner)
        out.append(s[pos:m.start()]); pos = m.end()
        skip = any(x in inner for x in ("step-item", "service-snippet", "area-list", "faq-")) or '<h2 class="section-title">' not in inner
        if skip:
            out.append(re.sub(r'<h2 class="section-title">(.*?)</h2>', lambda h: f'<h2 class="section-title">{em_last(h.group(1))}</h2>', m.group(0), count=1))
            continue
        nps = len(re.findall(r"<p[ >]", inner))
        img = imgs.pop(0) if imgs and nps >= 2 and "Källor" not in inner else None
        out.append(text_block(m.group(1), inner, img, k % 2 == 1, rest if first else ""))
        if img: k += 1
        if first: rest = ""; first = False
    out.append(s[pos:]); s = "".join(out)
    # övriga H2 (steg, områden, faq, länkar)
    s = re.sub(r'(<section class="section seo-section" id="faq">\s*<div class="container">\s*<h2 class="section-title">)(.*?)(</h2>)',
               lambda m: m.group(1) + em_last(m.group(2)) + m.group(3), s, flags=re.S)
    # cta-strip → Begär offert
    of = offer.replace('name="retur" value="takbyte.html"', f'name="retur" value="{retur}"')
    of = re.sub(r'name="tjanst" value="[^"]*"', f'name="tjanst" value="{tj}"', of)
    of = re.sub(r'(name="ort" type="text" value=")[^"]*"', rf'\g<1>{ort}"', of)
    of = re.sub(r'<p class="form-note">[^<]*</p>', f'<p class="form-note">{NOTE.get(tj, "Beskriv jobbet kort.")}</p>', of)
    s, n = re.subn(r'      <section class="section cta-strip">.*?</section>', lambda m: of, s, count=1, flags=re.S)
    if not n:
        s = s.replace("    </main>", of + "\n    </main>", 1)
    # bakgrunder växlar efter hero
    i = [0]
    def bg(m):
        cls = m.group(1).replace(" section-muted", "")
        r = cls.replace('class="section', 'class="section section-muted', 1) if i[0] % 2 else cls
        i[0] += 1
        return r
    main_a = s.index('</section>', s.index('<section class="page-hero')) + 10
    s = s[:main_a] + re.sub(r'(<section class="section[^"]*")', bg, s[main_a:]) + ""
    # orter: bara ortnamnet (DS §29)
    s = re.sub(r'<ul class="area-list">.*?</ul>', lambda m: re.sub(r'(<a [^>]*>)[^<]*? (?:i|på) ([^<]+)</a>', r'\1\2</a>', m.group(0)), s, flags=re.S)
    s = s.replace('href="kontakt.html#form"', 'href="#offert"')
    open(path, "w", encoding="utf-8").write(s)
    return True


def main(files=None):
    parts = pilot_parts()
    files = files or sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    n = 0
    for f in files:
        try:
            n += transform(os.path.join(ROOT, f), parts)
        except Exception as e:
            print("FEL", f, e)
    print(f"rollout_ds: {n} sidor")


if __name__ == "__main__":
    main(sys.argv[1:] or None)
