#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Statisk sidgenerator for villatakservice.se (Geal Entreprenad AB).
Kor:  python3 tools/generate.py
Skriver statiska .html-filer i repo-roten. Ingen runtime-dep.
Gemensam header/footer/head/schema har; sidinnehall i PAGES + kluster-listor.
De 6 ursprungssidorna (index/tjanster/om-oss/kontakt/artiklar/artikel)
redigeras direkt i sina filer och genereras INTE har (delad nav/footer maste matcha).
"""
import os, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- NAP / brand ----------------------------------------------------------
BRAND   = "Geal Entreprenad AB"
DOMAIN  = "https://villatakservice.se"
PHONE_D = "08 12 410 276"
PHONE_T = "+46812410276"
EMAIL   = "info@villatakservice.se"
STREET  = "Byggmästarvägen 18"
ZIP     = "168 32"
CITY    = "Bromma"
GEO_LAT = "59.3566"
GEO_LON = "17.9540"
IMG     = DOMAIN + "/assets/images/1.webp"
TODAY   = "2026-09-06"
ORGNR   = "559303-7566"
VATNR   = "SE559303756601"

AREAS = ["Sundbyberg","Solna","Bromma","Spånga","Sollentuna",
         "Järfälla","Täby","Danderyd","Lidingö","Nacka"]

# ---- shared markup --------------------------------------------------------
def a(href, text):
    return f'<a class="text-link" href="{href}">{text}</a>'

NAV = """      <div class="container header-inner">
        <a class="logo" href="index.html">Geal Entreprenad AB</a>
        <nav class="site-nav" id="site-nav" aria-label="Huvudnavigation">
          <ul>
            <li><a data-nav href="index.html">Hem</a></li>
            <li><a data-nav href="tjanster.html">Tjänster</a></li>
            <li><a data-nav href="bygg.html">Bygg</a></li>
            <li><a data-nav href="omraden.html">Områden</a></li>
            <li><a data-nav href="artiklar.html">Artiklar</a></li>
            <li><a data-nav href="om-oss.html">Om oss</a></li>
            <li><a data-nav href="kontakt.html">Kontakt</a></li>
          </ul>
        </nav>
        <a class="btn btn-primary header-cta" href="kontakt.html#form">Offert</a>
        <button class="menu-toggle" type="button" aria-controls="site-nav"
          aria-expanded="false" aria-label="Oppna meny">Meny</button>
      </div>"""

FOOTER = f"""    <footer class="footer">
      <div class="container footer-top">
        <div>
          <h3>{BRAND}</h3>
          <p>Vi utför takbyte, takrenovering och takservice för villaägare, BRF och
            företag i Sundbyberg och Stockholm.</p>
        </div>
        <div>
          <h3>Tjänster</h3>
          <ul>
            <li><a href="takbyte.html">Takbyte</a></li>
            <li><a href="takrenovering.html">Takrenovering</a></li>
            <li><a href="takbesiktning.html">Takbesiktning</a></li>
            <li><a href="plattak.html">Plåttak</a></li>
            <li><a href="bygg.html">Bygg &amp; Renovering</a></li>
          </ul>
        </div>
        <div>
          <h3>Områden</h3>
          <ul>
            <li><a href="taklaggare-sundbyberg.html">Sundbyberg</a></li>
            <li><a href="taklaggare-solna.html">Solna</a></li>
            <li><a href="taklaggare-bromma.html">Bromma</a></li>
            <li><a href="omraden.html">Alla områden</a></li>
          </ul>
        </div>
        <div>
          <h3>Kontakt</h3>
          <ul>
            <li><a href="tel:{PHONE_T}">{PHONE_D}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>{STREET}, {CITY}</li>
          </ul>
        </div>
      </div>
      <div class="container footer-bottom">
        &copy; <span data-year></span> {BRAND} &middot; Org.nr {ORGNR} &middot;
        <a href="integritetspolicy.html">Integritetspolicy</a> &middot;
        <a href="faq.html">Vanliga frågor</a>. Alla rättigheter förbehållna.
      </div>
    </footer>"""

def local_business_schema():
    return {
        "@context":"https://schema.org","@type":"RoofingContractor",
        "name":BRAND,"image":IMG,"url":DOMAIN+"/","telephone":PHONE_T,
        "email":EMAIL,"priceRange":"$$",
        "identifier":ORGNR,"vatID":VATNR,
        "address":{"@type":"PostalAddress","streetAddress":STREET,
            "postalCode":ZIP,"addressLocality":CITY,
            "addressRegion":"Stockholms län","addressCountry":"SE"},
        "geo":{"@type":"GeoCoordinates","latitude":GEO_LAT,"longitude":GEO_LON},
        "areaServed":[{"@type":"City","name":n} for n in ["Stockholm"]+AREAS],
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification",
            "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],
            "opens":"08:00","closes":"17:00"}],
        "sameAs":[]
    }

def breadcrumb_schema(crumbs):
    return {"@context":"https://schema.org","@type":"BreadcrumbList",
        "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,
            "item":DOMAIN+"/"+u} for i,(n,u) in enumerate(crumbs)]}

def faq_schema(faq):
    return {"@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":q,
            "acceptedAnswer":{"@type":"Answer","text":x}} for q,x in faq]}

def article_schema(p):
    return {"@context":"https://schema.org","@type":"Article",
        "headline":p["h1"],"image":IMG,"datePublished":TODAY,"dateModified":TODAY,
        "author":{"@type":"Organization","name":BRAND},
        "publisher":{"@type":"Organization","name":BRAND,
            "logo":{"@type":"ImageObject","url":IMG}},
        "mainEntityOfPage":DOMAIN+"/"+p["file"]}

def service_schema(p):
    return {"@context":"https://schema.org","@type":"Service",
        "serviceType":p.get("service_type",p["h1"]),
        "provider":{"@type":"RoofingContractor","name":BRAND,"url":DOMAIN+"/"},
        "areaServed":[{"@type":"City","name":n} for n in ["Stockholm"]+AREAS],
        "name":p["h1"],"description":p["description"]}

def jsonld(obj):
    return ('    <script type="application/ld+json">\n' +
            json.dumps(obj, ensure_ascii=False, indent=6) + "\n    </script>")

def render(p):
    robots_meta = '\n    <meta name="robots" content="noindex, follow" />' if p.get("noindex") else ""
    schemas = [local_business_schema() if p.get("localbiz") else None,
               breadcrumb_schema(p["crumbs"]),
               faq_schema(p["faq"]) if p.get("faq") else None,
               article_schema(p) if p.get("article") else None,
               service_schema(p) if p.get("service") else None]
    blocks = "\n".join(jsonld(s) for s in schemas if s)
    canon = f"{DOMAIN}/{p['file']}"
    faq_html = ""
    if p.get("faq"):
        items = "\n".join(f"""            <article class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">{q}
                <span data-sign>+</span>
              </button>
              <div class="faq-answer" hidden>{x}</div>
            </article>""" for q,x in p["faq"])
        faq_html = f"""
      <section class="section seo-section" id="faq">
        <div class="container">
          <h2 class="section-title">Vanliga frågor</h2>
          <div class="faq-wrap" data-accordion>
{items}
          </div>
        </div>
      </section>"""
    cta = p.get("cta", ("Behöver du hjälp med taket?",
        "Kontakta oss så återkommer vi med en tydlig bedömning och offert för ditt tak."))
    cta_html = "" if p.get("no_cta") else f"""
      <section class="section cta-strip">
        <div class="container">
          <h2>{cta[0]}</h2>
          <p>{cta[1]}</p>
          <div class="hero-actions" style="justify-content: center">
            <a class="btn btn-light" href="kontakt.html#form">Få offert</a>
            <a class="btn btn-outline-light" href="tel:{PHONE_T}">Ring oss</a>
          </div>
        </div>
      </section>"""
    return f"""<!doctype html>
<html lang="sv">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{p['title']}</title>
    <meta name="description" content="{p['description']}" />
    <link rel="canonical" href="{canon}" />
    <meta name="geo.region" content="SE-AB" />
    <meta name="geo.placename" content="Bromma, Stockholm" />
    <meta property="og:title" content="{p['title']}" />
    <meta property="og:description" content="{p['description']}" />
    <meta property="og:type" content="{p.get('og_type','website')}" />
    <meta property="og:url" content="{canon}" />
    <meta property="og:image" content="{IMG}" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="theme-color" content="#1f2f46" />{robots_meta}
    <link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
    <link rel="stylesheet" href="assets/css/style.css" />
    <script src="assets/js/main.js" defer></script>
{blocks}
  </head>
  <body>
    <a class="skip-link" href="#content">Hoppa till innehåll</a>
    <header class="site-header">
{NAV}
    </header>

    <main id="content">
{p['body']}
{faq_html}
{cta_html}
    </main>

{FOOTER}
  </body>
</html>
"""

def breadcrumb_html(crumbs):
    parts = " / ".join(
        (n if i==len(crumbs)-1 else f'<a href="{u}">{n}</a>')
        for i,(n,u) in enumerate(crumbs))
    return f'<p class="breadcrumb">{parts}</p>'

PAGES = []
def page(**kw):
    PAGES.append(kw)

# ---- section helpers ------------------------------------------------------
def hero(h1, lead, crumbs, anchors=None):
    an = ""
    if anchors:
        links = "\n".join(f'            <a href="{h}">{t}</a>' for h,t in anchors)
        an = f'\n          <div class="anchor-nav" aria-label="Snabblänkar">\n{links}\n          </div>'
    return f"""      <section class="page-hero">
        <div class="container">
          {breadcrumb_html(crumbs)}
          <h1 class="hero-title">{h1}</h1>
          <p class="section-lead">{lead}</p>{an}
        </div>
      </section>"""

def sec(title, paras, muted=False, sid=""):
    body = "\n".join(f"            <p>{t}</p>" for t in paras)
    cls = "section section-muted seo-section" if muted else "section seo-section"
    idattr = f' id="{sid}"' if sid else ""
    return f"""      <section class="{cls}"{idattr}>
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">{title}</h2>
{body}
          </div>
        </div>
      </section>"""

def sec_split(title, paras, aside_title, items, muted=True, sid=""):
    body = "\n".join(f"            <p>{t}</p>" for t in paras)
    li = "\n".join(f"              <li>{i}</li>" for i in items)
    cls = "section section-muted seo-section" if muted else "section seo-section"
    idattr = f' id="{sid}"' if sid else ""
    return f"""      <section class="{cls}"{idattr}>
        <div class="container section-layout section-layout--text">
          <div class="section-copy">
            <h2 class="section-title">{title}</h2>
{body}
          </div>
          <aside class="side-panel">
            <h3>{aside_title}</h3>
            <ul class="bullet-list">
{li}
            </ul>
          </aside>
        </div>
      </section>"""

def sec_process(title, steps, muted=False, sid=""):
    cards = "\n".join(f"""            <article class="step-item">
              <span class="step-number">{i+1:02d}</span>
              <h3>{h}</h3>
              <p>{t}</p>
            </article>""" for i,(h,t) in enumerate(steps))
    cls = "section section-muted seo-section" if muted else "section seo-section"
    idattr = f' id="{sid}"' if sid else ""
    return f"""      <section class="{cls}"{idattr}>
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">{title}</h2>
          </div>
          <div class="process-grid">
{cards}
          </div>
        </div>
      </section>"""

def rot_box(text):
    return f"""      <section class="section seo-section">
        <div class="container">
          <div class="tips-box">
            <h3>ROT-avdrag</h3>
            <p>{text} För 2026 är ROT-avdraget 30 % av arbetskostnaden, med ett tak på 50 000 kr per person och år. Läs mer i vår guide om {a('rot-avdrag-takarbete.html','ROT-avdrag för takarbete')}.</p>
          </div>
        </div>
      </section>"""

def links_block(title, cards, muted=True, sid=""):
    # cards: list of (href, heading, text)
    arts = "\n".join(f"""            <article class="service-snippet">
              <h3>{h}</h3>
              <p>{t}</p>
              <a class="text-link" href="{href}">Läs mer</a>
            </article>""" for href,h,t in cards)
    cls = "section section-muted seo-section" if muted else "section seo-section"
    idattr = f' id="{sid}"' if sid else ""
    return f"""      <section class="{cls}"{idattr}>
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">{title}</h2>
          </div>
          <div class="service-grid">
{arts}
          </div>
        </div>
      </section>"""

# ====================== MONEY: SERVICE PAGES ==============================
SVC_CRUMB = [("Hem","index.html"),("Tjänster","tjanster.html")]

page(file="takbyte.html",
  title="Takbyte i Sundbyberg & Stockholm – fast pris & ROT | Geal Entreprenad AB",
  description="Takbyte på villa i Sundbyberg och Stockholm. Vi byter tegel-, betong- och plåttak med tydlig offert, ROT-avdrag och slutkontroll. Begär kostnadsfri offert.",
  h1="Takbyte i Sundbyberg och Stockholm",
  service=True, service_type="Takbyte", localbiz=False,
  crumbs=SVC_CRUMB+[("Takbyte","takbyte.html")],
  cta=("Dags för takbyte?","Begär en kostnadsfri offert på ditt takbyte – vi bedömer taket och ger tydligt pris med ROT-avdrag."),
  body=hero("Takbyte i Sundbyberg och Stockholm",
    "Ett takbyte är en av villans större investeringar. Vi byter tegeltak, betongpannor och plåttak med tydlig offert, fast pris och slutbesiktning – i hela Storstockholm.",
    SVC_CRUMB+[("Takbyte","takbyte.html")],
    [("#nar","När behövs takbyte"),("#ingar","Vad ingår"),("#pris","Pris & ROT"),("#faq","Vanliga frågor")])
    + sec("När är det dags för ett takbyte?", [
        "Ett takbyte blir aktuellt när taket nått slutet av sin tekniska livslängd eller när skadorna är så omfattande att löpande reparationer inte längre lönar sig. Vanliga tecken är återkommande läckage, spruckna eller frostskadade pannor, fuktfläckar på vinden och underlagspapp som blivit spröd.",
        f"Är du osäker på om taket behöver bytas eller om en renovering räcker? Börja med en {a('takbesiktning.html','takbesiktning')} – då får du ett tydligt underlag innan du beslutar. Vi går också igenom skillnaden i vår guide {a('takbyte-eller-takrenovering.html','takbyte eller takrenovering')}."], sid="nar")
    + sec_split("Vad ingår i ett takbyte?", [
        "Vid ett takbyte ser vi till hela takets konstruktion, inte bara ytskiktet. Vi river det gamla taket, kontrollerar och byter läkt och underlagspapp vid behov, och åtgärdar detaljer runt skorsten, takfönster och genomföringar.",
        f"Vi byter även utsatta plåtdetaljer och ser över {a('hangrannor-stupror.html','hängrännor och stuprör')} samt {a('taksakerhet-snorasskydd.html','taksäkerhet som snörasskydd och takstege')} så att taket blir komplett och godkänt."],
        "Det här ingår normalt", [
        "Rivning och bortforsling av befintligt tak.","Ny underlagspapp och kontroll av läkt.",
        "Nytt ytskikt: tegel, betongpannor eller plåt.","Plåtarbeten kring skorsten och genomföringar.",
        "Ny hängränna och stuprör vid behov.","Slutkontroll och genomgång med dig som kund."], sid="ingar")
    + sec("Material: tegel, betong eller plåt?", [
        f"Valet av takmaterial påverkar både livslängd, uttryck och pris. Tegel och betongpannor är vanligast på villor i Stockholm, medan {a('plattak.html','plåttak')} passar bra på lägre lutningar och ger låg vikt. Vi hjälper dig jämföra alternativen utifrån ditt hus.",
        f"En djupare jämförelse hittar du i {a('tegel-betong-plattak.html','tegel vs betong vs plåt')} och i {a('takmaterial-livslangd.html','livslängd per takmaterial')}."], muted=True)
    + sec("Pris för takbyte – vad påverkar kostnaden?", [
        "Priset för ett takbyte beror på takets area och lutning, val av material, tillgänglighet, behov av ställning och underlagets skick. Därför lämnar vi alltid pris efter att ha bedömt taket på plats.",
        f"Vill du förstå kostnadsbilden innan du begär offert? Läs prisguiden {a('vad-kostar-takbyte.html','vad kostar ett takbyte')}. Kostnaden gäller före ROT-avdrag."], sid="pris")
    + rot_box("Arbetskostnaden vid ett takbyte på villa ger normalt rätt till ROT-avdrag, vilket sänker din slutkostnad.")
    + sec_process("Så går ett takbyte till", [
        ("Förfrågan","Du kontaktar oss med kort info om huset och taket."),
        ("Besiktning & offert","Vi bedömer taket och lämnar tydlig offert med material och tidplan."),
        ("Utförande","Vi river, förbereder underlag och lägger nytt tak enligt plan."),
        ("Slutkontroll","Vi går igenom resultatet med dig och dokumenterar arbetet.")], muted=True)
    + links_block("Relaterat", [
        ("villatak.html","Tak på villa – komplett guide","Allt om tak på villa: material, kostnad och underhåll."),
        ("taklaggare-sundbyberg.html","Takbyte i Sundbyberg","Vi är lokala takläggare i Sundbyberg och närområdet."),
        ("bygglov-takbyte.html","Behövs bygglov för takbyte?","När takbyte kräver bygglov eller anmälan.")]),
  faq=[
    ("Hur lång tid tar ett takbyte på en villa?","De flesta villatakbyten tar ungefär 1–2 veckor beroende på takets storlek, väder och eventuella underliggande skador. Vi ger en preliminär tidplan i offerten."),
    ("Kan jag använda ROT-avdrag för takbyte?","Ja, arbetskostnaden för takbyte på villa ger normalt rätt till ROT-avdrag. Vi drar av det direkt på fakturan. Exakt nivå för 2026 anges i offerten."),
    ("Måste jag byta hela taket eller räcker en renovering?","Det beror på skicket. Om grundkonstruktionen är sund kan en takrenovering räcka. En takbesiktning ger svar innan du beslutar."),
    ("Vilket takmaterial är bäst?","Det beror på husets lutning, stil och budget. Tegel och betong är vanligast, plåt passar låga lutningar. Vi går igenom alternativen med dig.")])

page(file="takrenovering.html",
  title="Takrenovering i Stockholm – pris & takomläggning | Geal Entreprenad AB",
  description="Takrenovering och takomläggning i Stockholm och Sundbyberg. Riktade åtgärder som förlänger takets livslängd. Tydlig plan, ROT-avdrag och kostnadsfri offert.",
  h1="Takrenovering och takomläggning i Stockholm",
  service=True, service_type="Takrenovering", localbiz=False,
  crumbs=SVC_CRUMB+[("Takrenovering","takrenovering.html")],
  cta=("Behöver taket renoveras?","Vi bedömer vilka åtgärder som är mest lönsamma och ger en tydlig offert."),
  body=hero("Takrenovering och takomläggning i Stockholm",
    "Takrenovering passar när grundkonstruktionen är sund men delar av taket behöver åtgärdas. Ofta bästa balansen mellan kostnad och livslängd – på villor och äldre fastigheter i Stockholm.",
    SVC_CRUMB+[("Takrenovering","takrenovering.html")],
    [("#nar","När passar det"),("#ingar","Vad ingår"),("#faq","Vanliga frågor")])
    + sec("När passar takrenovering?", [
        "Takrenovering är rätt när takets stomme och stora ytor fortfarande fungerar, men enskilda delar behöver repareras – slitna beslag, spruckna pannor, otäta anslutningar eller begränsade fuktskador.",
        f"Vid en takomläggning lägger vi om befintliga pannor med ny underlagspapp och läkt, vilket kan förlänga takets liv rejält utan ett fullständigt {a('takbyte.html','takbyte')}. Vi hjälper dig välja rätt nivå efter en {a('takbesiktning.html','takbesiktning')}."], sid="nar")
    + sec_split("Vad ingår i en takrenovering?", [
        "Vi börjar med att skilja på kosmetiskt slitage och verkliga riskpunkter, och ger sedan en prioriterad åtgärdsplan. Arbetet kan delas upp i etapper om det passar din budget.",
        f"Vanliga moment är omläggning av pannor, byte av underlagspapp, plåtarbeten och åtgärder mot {a('taklackage.html','takläckage')} och {a('mossa-pa-taket.html','mossa på taket')}."],
        "Typiska åtgärder", [
        "Omläggning av tegel- eller betongpannor.","Byte av underlagspapp och läkt.",
        "Reparation av beslag och anslutningar.","Åtgärd av läckage och enskilda skador.",
        "Byte av utsatta plåtdetaljer.","Prioriterad plan i etapper vid behov."], sid="ingar")
    + rot_box("Även takrenovering på villa ger normalt ROT-avdrag på arbetskostnaden.")
    + links_block("Relaterat", [
        ("takbyte-eller-takrenovering.html","Takbyte eller takrenovering?","Så väljer du rätt åtgärd för ditt tak."),
        ("vad-kostar-takrenovering.html","Vad kostar en takrenovering?","Prisintervall och vad som påverkar kostnaden."),
        ("taklaggare-solna.html","Takrenovering i Solna","Lokala takläggare i Solna och närområdet.")]),
  faq=[
    ("Vad är skillnaden mellan takrenovering och takomläggning?","Takomläggning innebär att befintliga pannor läggs om med ny underlagspapp och läkt. Takrenovering är ett bredare begrepp som även omfattar reparation av beslag, plåt och enskilda skador."),
    ("Hur vet jag om det räcker med renovering?","En takbesiktning visar om stommen är sund. Är den det räcker ofta renovering; annars rekommenderar vi takbyte."),
    ("Kan arbetet delas upp i etapper?","Ja, vi kan prioritera de mest utsatta delarna först och planera resten längre fram efter din budget.")])

page(file="takbesiktning.html",
  title="Takbesiktning i Stockholm – besikta tak | Geal Entreprenad AB",
  description="Takbesiktning i Stockholm och Sundbyberg. Vi besiktar tak, bedömer skick och riskpunkter och ger underlag för offert. Boka en takbesiktning idag.",
  h1="Takbesiktning i Stockholm",
  service=True, service_type="Takbesiktning", localbiz=False,
  crumbs=SVC_CRUMB+[("Takbesiktning","takbesiktning.html")],
  cta=("Vill du besikta taket?","Boka en takbesiktning så får du ett tydligt underlag inför beslut och offert."),
  body=hero("Takbesiktning i Stockholm",
    "Att besikta taket är ofta det bästa första steget. Vi går igenom takets skick, riskpunkter och avvattning och ger dig ett tydligt underlag – innan du beslutar om renovering eller takbyte.",
    SVC_CRUMB+[("Takbesiktning","takbesiktning.html")],
    [("#varfor","Varför besikta"),("#ingar","Vad kontrolleras"),("#faq","Vanliga frågor")])
    + sec("Varför besiktning av tak lönar sig", [
        "Utan en korrekt bedömning är det svårt att veta om ett problem kräver akut insats eller kan planeras längre fram. Många hör av sig efter att ha sett en missfärgning i undertaket, lösa pannor eller mossa på utsatta ytor.",
        f"En besiktning ger svar på om det är ett isolerat problem eller ett tecken på större belastning – och är ett bra underlag inför {a('takbyte.html','takbyte')} eller {a('takrenovering.html','takrenovering')}."], sid="varfor")
    + sec_split("Vad kontrolleras vid en takbesiktning?", [
        "Vi gör en samlad bedömning av skick, funktion och rekommenderad åtgärdsnivå, och dokumenterar fynden så att du kan prioritera rätt.",
        f"Vanliga fynd är otäta anslutningar, {a('taklackage.html','takläckage')}, begynnande {a('fuktskada-mogel-vind.html','fuktskador på vinden')} och slitna beslag."],
        "Vi ser bland annat på", [
        "Takytor, pannor och plåtdetaljer.","Anslutningar mot skorsten och genomföringar.",
        "Hängrännor, stuprör och avvattning.","Tecken på fukt i undertak och på vind.",
        "Taksäkerhet och infästningar.","Rekommendation: service, renovering eller byte."], sid="ingar")
    + links_block("Relaterat", [
        ("nar-ska-taket-bytas.html","Tecken på att taket behöver bytas","Vanliga signaler att hålla koll på."),
        ("fuktskada-mogel-vind.html","Fuktskada och mögel på vinden","Orsaker, symptom och åtgärder."),
        ("taklaggare-bromma.html","Takbesiktning i Bromma","Lokala takläggare i Bromma och västerort.")]),
  faq=[
    ("Vad kostar en takbesiktning?","Vi erbjuder alltid gratis platsbesök och kostnadsförslag inför ett takprojekt. Kontakta oss så bokar vi en tid som passar."),
    ("Hur ofta bör man besikta taket?","En översiktlig kontroll två gånger per år (vår och höst) är en bra grund. En professionell besiktning är klok vart 5–10:e år eller vid tecken på problem."),
    ("Får jag en rapport?","Ja, du får en tydlig bedömning av skick, riskpunkter och rekommenderad åtgärd som underlag för offert.")])

page(file="plattak.html",
  title="Plåttak i Stockholm – nytt plåttak & plåtarbeten | Geal Entreprenad AB",
  description="Plåttak i Stockholm och Sundbyberg: nytt plåttak, bandtäckning och plåtarbeten med fokus på täthet och avvattning. Kostnadsfri offert från lokala takläggare.",
  h1="Plåttak i Stockholm",
  service=True, service_type="Plåttak", localbiz=False,
  crumbs=SVC_CRUMB+[("Plåttak","plattak.html")],
  cta=("Funderar du på plåttak?","Vi hjälper dig med nytt plåttak eller plåtarbeten – begär en offert."),
  body=hero("Plåttak i Stockholm",
    "Plåttak är ett populärt val i Stockholm tack vare låg vikt, lång livslängd och rent uttryck. Vi utför nytt plåttak, bandtäckning och plåtdetaljer med precision i skarvar, beslag och avvattning.",
    SVC_CRUMB+[("Plåttak","plattak.html")],
    [("#fordelar","Fördelar"),("#ingar","Vad vi gör"),("#faq","Vanliga frågor")])
    + sec("Fördelar med plåttak", [
        "Plåttak har låg vikt, tål temperaturväxlingar bra och passar även på lägre taklutningar där pannor inte fungerar. Rätt utfört ger det en tät konstruktion som är enkel att underhålla.",
        f"Samtidigt ställer plåtarbeten höga krav på precision – små fel i infästning eller skarvar kan ge läckage eller korrosion över tid. Jämför material i {a('tegel-betong-plattak.html','tegel vs betong vs plåt')}."], sid="fordelar")
    + sec_split("Vad vi gör inom plåttak", [
        "Vi hjälper både dig som vill installera nytt plåttak och fastighetsägare som behöver renovera ett befintligt system. I varje projekt tittar vi på taklutning, avvattning och detaljlösningar.",
        f"Har plåttaket börjat rosta kan {a('takmalning.html','takmålning')} vara ett alternativ när konstruktionen fortfarande är sund."],
        "Vi arbetar med", [
        "Nytt plåttak och bandtäckning (falsat plåt).","Beslag och anslutningar runt genomföringar.",
        "Plåtdetaljer: vindskivor, fotplåt, ståndskivor.","Avvattning och skydd mot korrosion.",
        "Reparation av befintliga plåttak.","Råd om skötsel och underhåll."], sid="ingar")
    + links_block("Relaterat", [
        ("falsat-plattak.html","Falsat plåttak & bandtäckning","Klassiskt plåttak för låga lutningar."),
        ("mala-plattak.html","Måla plåttak","Underhåll och nytt ytskydd."),
        ("takmaterial-livslangd.html","Livslängd per takmaterial","Så länge håller plåt, tegel och betong."),
        ("taklaggare-lidingo.html","Plåttak på Lidingö","Salt havsluft ställer extra krav på plåt.")]),
  faq=[
    ("Hur länge håller ett plåttak?","Ett väl utfört plåttak håller ofta 40–50 år eller mer med rätt underhåll och eventuell ommålning."),
    ("Kan man lägga plåttak på låg lutning?","Ja, plåt (särskilt bandtäckning) fungerar på lägre lutningar där tegel- och betongpannor inte är lämpliga."),
    ("Är plåttak bullrigt vid regn?","Med korrekt underlag och isolering är ljudnivån normalt inget problem i bostadshus.")])

page(file="takmalning.html",
  title="Takmålning i Stockholm – måla plåttak | Geal Entreprenad AB",
  description="Takmålning av plåttak i Stockholm och Sundbyberg. Tvätt, rostskydd och anpassat målningssystem som ger taket nytt skydd. Begär kostnadsfri offert.",
  h1="Takmålning i Stockholm",
  service=True, service_type="Takmålning", localbiz=False,
  crumbs=SVC_CRUMB+[("Takmålning","takmalning.html")],
  cta=("Dags att måla taket?","Vi bedömer om takmålning är rätt åtgärd och ger dig en tydlig offert."),
  body=hero("Takmålning i Stockholm",
    "För vissa plåttak är målning en kostnadseffektiv åtgärd när ytan behöver nytt skydd men konstruktionen fortfarande är sund. Vi tvättar, rostskyddar och målar med anpassat system.",
    SVC_CRUMB+[("Takmålning","takmalning.html")],
    [("#nar","När passar det"),("#ingar","Så går det till"),("#faq","Vanliga frågor")])
    + sec("När är takmålning rätt åtgärd?", [
        "Takmålning passar när ett plåttak har börjat tappa sitt ytskydd, mattats av eller fått begynnande rost – men där grundkonstruktionen är hel. Då kan målning förlänga takets liv och förbättra utseendet till en lägre kostnad än byte.",
        f"Är rosten eller skadorna mer omfattande kan {a('plattak.html','byte av plåttaket')} vara mer lönsamt. Vi bedömer alltid skicket innan vi rekommenderar målning."], sid="nar")
    + sec_split("Så går takmålningen till", [
        "Vi börjar med rengöring och förbehandling, åtgärdar rost och målar sedan med ett system anpassat för aktuell plåt och miljö. Målning gäller normalt plåttak – tegel- och betongpannor målas sällan med gott resultat.",
        f"Behöver taket först rengöras från påväxt läser du mer under {a('taktvatt.html','taktvätt')}."],
        "Det här ingår", [
        "Tvätt och borttagning av löst material.","Rostskydd och förbehandling där det behövs.",
        "Grund- och täckmålning med anpassat system.","Kontroll av detaljer och avvattning.",
        "Råd om fortsatt underhåll."], sid="ingar")
    + links_block("Relaterat", [
        ("taktvatt.html","Taktvätt","Rengöring innan målning eller som eget underhåll."),
        ("plattak.html","Plåttak","Nytt plåttak när målning inte räcker."),
        ("mossa-pa-taket.html","Mossa på taket","Behandling och förebyggande underhåll.")]),
  faq=[
    ("Kan man måla alla tak?","Nej. Takmålning görs främst på plåttak. Tegel- och betongpannor målas sällan med bra långsiktigt resultat."),
    ("Hur länge håller en takmålning?","Med rätt förbehandling och system håller en takmålning normalt runt 10–15 år beroende på exponering."),
    ("Ger takmålning ROT-avdrag?","Arbetskostnaden för takmålning på villa ger normalt ROT-avdrag. Nivån för 2026 anges i offerten.")])

page(file="taktvatt.html",
  title="Taktvätt i Stockholm – ta bort mossa | Geal Entreprenad AB",
  description="Taktvätt i Stockholm och Sundbyberg. Skonsam rengöring av tak från mossa, smuts och påväxt med rätt metod för din taktyp. Begär kostnadsfri offert.",
  h1="Taktvätt i Stockholm",
  service=True, service_type="Taktvätt", localbiz=False,
  crumbs=SVC_CRUMB+[("Taktvätt","taktvatt.html")],
  cta=("Behöver taket tvättas?","Vi rengör taket skonsamt med rätt metod – begär en offert."),
  body=hero("Taktvätt i Stockholm",
    "Skonsam tvätt av takytor när mossa, smuts och påväxt bör tas bort utan onödigt slitage. Rätt metod för din taktyp förlänger takets liv och förbättrar avvattningen.",
    SVC_CRUMB+[("Taktvätt","taktvatt.html")],
    [("#varfor","Varför taktvätt"),("#ingar","Så går det till"),("#faq","Vanliga frågor")])
    + sec("Varför taktvätt?", [
        "Mossa och påväxt håller kvar fukt, kan lyfta pannor och försämra avvattningen. Regelbunden taktvätt minskar slitage och gör det lättare att upptäcka begynnande skador i tid.",
        f"Vi väljer metod efter taktyp och skick – på känsliga tak används lågtrycksmetoder. Vill du förstå hur mossa uppstår och förebyggs läser du {a('mossa-pa-taket.html','mossa på taket')}."], sid="varfor")
    + sec_split("Så går taktvätten till", [
        "Vi bedömer underlaget innan arbetet startar, väljer rätt metod och rengör taket skonsamt. Efter tvätt kan vi rekommendera ytterligare underhåll som förebygger ny påväxt.",
        f"Är plåttaket samtidigt i behov av nytt ytskydd kan {a('takmalning.html','takmålning')} göras i anslutning."],
        "Det här ingår", [
        "Bedömning av taktyp och skick.","Metod anpassad efter yta (ofta lågtryck).",
        "Borttagning av mossa, smuts och påväxt.","Kontroll av rännor och avvattning.",
        "Råd om fortsatt underhåll."], sid="ingar")
    + links_block("Relaterat", [
        ("mossa-pa-taket.html","Mossa på taket – behandling","Orsaker, metoder och förebyggande."),
        ("hangrannor-stupror.html","Hängrännor & stuprör","Rensning och byte för god avvattning."),
        ("takbesiktning.html","Takbesiktning","Kontrollera skicket samtidigt.")]),
  faq=[
    ("Skadar högtryckstvätt taket?","Högtryck kan skada pannor och ytskikt. Vi använder ofta lågtryck och metoder anpassade efter taktyp för att undvika slitage."),
    ("Hur ofta bör taket tvättas?","Det beror på läge och beskuggning. Tak i skuggiga, trädnära lägen behöver oftare tvätt än öppna, soliga tak."),
    ("Kan ni behandla mot ny mossa?","Ja, vi kan rekommendera och utföra förebyggande behandling efter tvätt. Vi bedömer vad som passar din taktyp.")])


# ====================== VILLA PILLAR ======================================
page(file="villatak.html", localbiz=True,
  title="Tak på villa – komplett guide till villatak i Stockholm | Geal Entreprenad AB",
  description="Villatak i Stockholm: allt om takbyte, material, kostnad, ROT och underhåll för tak på villa. Guide och lokala takläggare för ditt villatak.",
  h1="Tak på villa – komplett guide till villatak",
  crumbs=[("Hem","index.html"),("Villatak","villatak.html")],
  cta=("Ska du åtgärda ditt villatak?","Vi är takläggare specialiserade på villatak i Stockholm – begär en kostnadsfri offert."),
  body=hero("Tak på villa – komplett guide till villatak",
    "Villatak har egna förutsättningar: taklutning, material och detaljer skiljer sig från större fastigheter. Här samlar vi allt om takbyte, renovering, material, kostnad och underhåll för tak på villa i Stockholm.",
    [("Hem","index.html"),("Villatak","villatak.html")],
    [("#material","Material"),("#atgarder","Åtgärder"),("#kostnad","Kostnad & ROT"),("#faq","Vanliga frågor")])
    + sec("Villatak i Stockholm – vad är särskilt?", [
        "De flesta villor i Stockholmsområdet har sadeltak med tegel- eller betongpannor, medan hus med lägre lutning ofta har plåttak. Villans tak är mer utsatt för lokala förhållanden än man tror – vindriktning, beskuggning av träd och snölaster påverkar slitaget.",
        "Som takläggare med villatak som specialitet anpassar vi alltid råd och material efter husets ålder, stil och läge. Den här guiden hjälper dig att förstå helheten innan du beslutar."], sid="material")
    + links_block("Material för villatak", [
        ("tegel-betong-plattak.html","Tegel vs betong vs plåt","För- och nackdelar för villatak."),
        ("takmaterial-livslangd.html","Livslängd per material","Så länge håller olika villatak."),
        ("plattak.html","Plåttak på villa","När plåt passar villans tak.")], muted=False)
    + sec_split("Åtgärder för tak på villa", [
        "Beroende på takets skick kan rätt åtgärd vara allt från tvätt och underhåll till full omläggning. Ofta börjar det med en besiktning som klargör om det räcker med riktade insatser eller om taket behöver bytas.",
        f"De vanligaste tjänsterna för villatak är {a('takbyte.html','takbyte')}, {a('takrenovering.html','takrenovering')}, {a('takbesiktning.html','takbesiktning')}, {a('plattak.html','plåttak')}, {a('takmalning.html','takmålning')} och {a('taktvatt.html','taktvätt')}."],
        "Vanliga villaåtgärder", [
        "Takbyte av tegel-, betong- eller plåttak.","Takomläggning och renovering av utsatta delar.",
        "Byte av hängrännor, stuprör och plåtdetaljer.","Snörasskydd och taksäkerhet.",
        "Taktvätt och behandling mot mossa.","Åtgärd av läckage och fuktskador."], sid="atgarder")
    + sec("Kostnad och ROT för villatak", [
        f"Kostnaden för ett villatak beror på area, material, lutning och skick. Villaägare kan normalt använda {a('rot-avdrag-takarbete.html','ROT-avdrag')} på arbetskostnaden, vilket sänker slutpriset.",
        f"För prisintervall, se {a('vad-kostar-takbyte.html','vad kostar ett takbyte')} och {a('vad-kostar-takrenovering.html','vad kostar en takrenovering')}."], sid="kostnad", muted=True)
    + sec_split("Trygghet och total entreprenad", [
        "Vi är ett registrerat aktiebolag med F-skatt och ansvarsförsäkring, och våra hantverkare är anslutna till ID06. Du får alltid ett skriftligt avtal och en tydlig offert innan arbetet startar.",
        "Utöver taket kan vi ta hand om hela villan som total entreprenad – behöver du samordna takbyte med fasad, fönster eller annan renovering håller vi ihop projektet åt dig."],
        "Därför är du trygg med oss", [
        "Registrerat AB med F-skatt och ansvarsförsäkring.","ID06 på hantverkarna.",
        "Gratis platsbesök och kostnadsförslag.","Skriftligt avtal och tydlig offert.",
        "ROT-avdrag draget direkt på fakturan.","Total entreprenad – hela villan, inte bara taket."], muted=False)
    + links_block("Villatak i ditt område", [
        ("taklaggare-sundbyberg.html","Villatak i Sundbyberg","Lokala takläggare i Sundbyberg."),
        ("taklaggare-bromma.html","Villatak i Bromma","Klassiska villaområden i västerort."),
        ("omraden.html","Alla områden","Se alla orter vi arbetar i.")]),
  faq=[
    ("Vilket tak passar bäst på en villa?","Tegel- och betongpannor är vanligast på villor med sadeltak, medan plåt passar lägre lutningar. Valet beror på husets stil, lutning och budget."),
    ("Kan jag få ROT-avdrag för mitt villatak?","Ja, som villaägare får du normalt ROT-avdrag på arbetskostnaden för takarbete. Nivån för 2026 anges i offerten."),
    ("Hur ofta behöver ett villatak underhållas?","En översiktlig kontroll vår och höst plus taktvätt vid behov räcker långt. Ett komplett tak håller i decennier med rätt underhåll.")])

# ====================== OMRÅDEN HUB =======================================
_area_files = {n: f"taklaggare-{n.lower().replace('ä','a').replace('å','a').replace('ö','o')}.html" for n in AREAS}
_area_cards = "\n".join(f"""            <article class="service-snippet">
              <h3>{n}</h3>
              <p>Takläggare i {n} – takbyte, renovering och besiktning.</p>
              <a class="text-link" href="{_area_files[n]}">Takläggare i {n}</a>
            </article>""" for n in AREAS)
page(file="omraden.html",
  title="Områden – takläggare i Sundbyberg, Solna & Stockholm | Geal Entreprenad AB",
  description="Vi är takläggare i Sundbyberg, Solna, Bromma, Spånga, Sollentuna, Järfälla, Täby, Danderyd, Lidingö och Nacka. Se alla områden vi arbetar i.",
  h1="Områden vi arbetar i",
  crumbs=[("Hem","index.html"),("Områden","omraden.html")],
  cta=("Finns ditt område inte med?","Skicka en förfrågan – vi tar uppdrag i hela Storstockholm."),
  body=hero("Områden vi arbetar i",
    "Vi utgår från Bromma (Mariehäll) och arbetar som takläggare i hela Storstockholm. Lokalkännedom spelar roll – byggnadstyper, taklutningar och vanliga skador skiljer sig mellan områdena.",
    [("Hem","index.html"),("Områden","omraden.html")])
    + f"""      <section class="section section-muted seo-section">
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">Takläggare nära dig</h2>
            <p>Välj ditt område för lokal information om takbyte, takrenovering och takbesiktning.</p>
          </div>
          <div class="service-grid">
{_area_cards}
          </div>
        </div>
      </section>""")

# ====================== LOCATION PAGES ====================================
# Per ort: (intro, lokalt stycke, aside-items)
LOC = {
 "Sundbyberg": (
   "Sundbyberg är ett av våra närmaste arbetsområden – vi finns precis intill i Bromma (Mariehäll). Här känner vi husen, taken och de lokala förutsättningarna, från äldre villor i Duvbo och Storskogen till nyare bebyggelse. Vi är takläggare i Sundbyberg för takbyte, takrenovering och takbesiktning.",
   "Duvbos äldre trävillor har ofta branta tegeltak där underlagspapp och läkt kan behöva bytas, medan flerbostadshus närmare centrum ofta har plåt- eller papptak. Vår närhet gör att vi snabbt kan komma ut på besiktning.",
   ["Grannområde till vår bas i Bromma – kort inställelsetid.","Erfarenhet av Duvbos äldre trävillor.","Takbyte, renovering och besiktning."]),
 "Solna": (
   "Solna gränsar till Sundbyberg och är ett av våra vanligaste arbetsområden. Vi hjälper villaägare i bland annat Bergshamra, Huvudsta och Råsunda med takbyte, takrenovering och plåtarbeten.",
   "Villaområdena i Solna blandar hus från olika epoker, och många tak från mitten av 1900-talet börjar nå slutet av sin livslängd. Det gör att både takomläggning och fullt takbyte är vanligt här.",
   ["Nära Sundbyberg – snabb service.","Erfarenhet av 1900-talsvillor.","Villatak i Bergshamra, Huvudsta, Råsunda."]),
 "Bromma": (
   "Bromma i västerort är vårt hemmaområde – vi utgår härifrån (Mariehäll) och känner västerorts villor väl. Vi är takläggare i Bromma för villor i bland annat Ängby, Nockeby, Äppelviken och Bromma Kyrka.",
   "Många villor i Ängby och Äppelviken är från 1920–40-talet med tegeltak och karaktärsfulla detaljer. Här är det viktigt att bevara husets uttryck vid takbyte, samtidigt som underlag och plåt moderniseras.",
   ["Lokal takfirma med bas i Bromma.","Varsamt takbyte på äldre villor.","Tegel-, betong- och plåttak."]),
 "Spånga": (
   "Spånga och Tensta–Spånga är ett stort villaområde i nordvästra Stockholm. Vi hjälper villaägare i Spånga, Bromsten och Solhem med takbyte, takrenovering och takbesiktning.",
   "Spångas villabebyggelse är blandad, med både äldre trävillor och 1960–70-talshus. Många tak från den perioden är nu mogna för omläggning eller byte, ofta i kombination med nya hängrännor och taksäkerhet.",
   ["Villatak i Spånga, Bromsten, Solhem.","Erfarenhet av 60–70-talshus.","Takbyte med ny avvattning."]),
 "Sollentuna": (
   "Sollentuna norr om Stockholm har omfattande villabebyggelse. Vi är takläggare i Sollentuna för villor i bland annat Edsberg, Helenelund, Tureberg och Viby.",
   "Kupolen av villor i Sollentuna spänner från äldre hus till moderna. Snölaster och trädnära lägen gör att många tak behöver taktvätt och kontroll av avvattning utöver själva takbytet.",
   ["Villatak i Edsberg och Helenelund.","Kontroll av snölast och avvattning.","Takbyte, renovering och taktvätt."]),
 "Järfälla": (
   "Järfälla med Jakobsberg, Kallhäll och Viksjö är ett växande villaområde nordväst om Stockholm. Vi hjälper villaägare i Järfälla med takbyte, takrenovering och plåtarbeten.",
   "Viksjös stora villaområde byggdes till stor del på 1970–80-talet, och många av dessa tak når nu en ålder där byte eller omläggning är aktuellt. Vi ser ofta slitna betongpannor och underlagspapp här.",
   ["Villatak i Jakobsberg, Kallhäll, Viksjö.","Byte av mogna 70–80-talstak.","Betongpannor och plåt."]),
 "Täby": (
   "Täby nordost om Stockholm är ett av regionens största villaområden. Vi är takläggare i Täby för villor i bland annat Näsbypark, Gribbylund, Viggbyholm och Roslags-Näsby.",
   "Näsbypark och Viggbyholm har många äldre, påkostade villor där takets uttryck är viktigt, medan nyare områden har moderna tak. Vi anpassar material och lösningar efter husets karaktär.",
   ["Villatak i Näsbypark och Gribbylund.","Varsamt takbyte på påkostade villor.","Anpassat materialval."]),
 "Danderyd": (
   "Danderyd med Djursholm, Stocksund och Enebyberg har några av regionens mest påkostade villor. Vi är takläggare i Danderyd för takbyte, takrenovering och plåtarbeten på villatak.",
   "Djursholms äldre villor har ofta komplexa tak med torn, valmar och detaljerade plåtarbeten. Här krävs erfarenhet av att kombinera bevarat uttryck med moderna, täta lösningar.",
   ["Villatak i Djursholm och Stocksund.","Erfarenhet av komplexa villatak.","Detaljerade plåtarbeten."]),
 "Lidingö": (
   "Lidingö är en ö öster om Stockholm med stor villabebyggelse. Vi hjälper villaägare på Lidingö i bland annat Bodal, Larsberg, Sticklinge och Käppala med takbyte och plåtarbeten.",
   "Det havsnära läget innebär salt luft som ställer extra krav på plåt och infästningar – korrosion är vanligare här. Vi väljer material och ytbehandling som klarar Lidingös kustklimat.",
   ["Villatak på Lidingö.","Materialval för salt havsluft.","Plåttak och korrosionsskydd."]),
 "Nacka": (
   "Nacka öster om Stockholm har omfattande villabebyggelse i bland annat Saltsjöbaden, Boo, Älta och Fisksätra. Vi är takläggare i Nacka för takbyte, takrenovering och takbesiktning.",
   "Saltsjöbadens äldre, ofta stora villor har varierade tak med både tegel och plåt, och det kustnära läget påverkar slitaget. Vi anpassar åtgärder efter husets ålder och exponering.",
   ["Villatak i Saltsjöbaden och Boo.","Erfarenhet av stora, äldre villor.","Kustnära materialval."]),
}
for _ort,(intro,localp,items) in LOC.items():
    f = _area_files[_ort]
    others = [o for o in AREAS if o!=_ort][:3]
    page(file=f,
      title=f"Takläggare i {_ort} – takbyte & takrenovering | Geal Entreprenad AB",
      description=f"Takläggare i {_ort}. Vi utför takbyte, takrenovering, takbesiktning och plåttak på villa i {_ort} och Stockholm. Lokal takfirma – begär kostnadsfri offert.",
      h1=f"Takläggare i {_ort}",
      crumbs=[("Hem","index.html"),("Områden","omraden.html"),(_ort,f)],
      cta=(f"Behöver du takläggare i {_ort}?", f"Vi är lokala takläggare i {_ort} – begär en kostnadsfri offert på ditt takprojekt."),
      body=hero(f"Takläggare i {_ort}", intro,
        [("Hem","index.html"),("Områden","omraden.html"),(_ort,f)],
        [("#tjanster","Tjänster"),("#lokalt","Lokalt"),("#faq","Vanliga frågor")])
        + sec(f"Takläggare i {_ort} – lokalt och nära", [localp,
            f"Oavsett om du behöver ett komplett takbyte eller en riktad renovering ger vi en tydlig bedömning och offert. Vi arbetar även i grannområden – se alla {a('omraden.html','områden vi arbetar i')}."], sid="lokalt")
        + links_block(f"Våra tjänster i {_ort}", [
            ("takbyte.html", f"Takbyte i {_ort}", "Byte av tegel-, betong- och plåttak."),
            ("takrenovering.html", f"Takrenovering i {_ort}", "Riktade åtgärder som förlänger takets liv."),
            ("takbesiktning.html", f"Takbesiktning i {_ort}", "Bedömning av skick inför beslut.")], muted=False, sid="tjanster")
        + sec_split(f"Varför välja oss i {_ort}?", [
            f"Vi utgår från Bromma (Mariehäll), precis intill Sundbyberg, och når {_ort} snabbt. Det gör att vi kan komma ut på besiktning utan långa väntetider och hålla nära kontakt genom hela projektet.",
            f"Läs mer om {a('villatak.html','tak på villa')} eller jämför {a('takbyte-eller-takrenovering.html','takbyte och takrenovering')} innan du bestämmer dig."],
            f"Takläggare i {_ort}", items)
        + links_block("Närliggande områden", [
            (_area_files[o], f"Takläggare i {o}", f"Vi arbetar även i {o}.") for o in others]),
      faq=[
        (f"Arbetar ni med villatak i {_ort}?", f"Ja, vi är takläggare specialiserade på villatak och arbetar i hela {_ort} med takbyte, takrenovering, besiktning och plåtarbeten."),
        (f"Hur snabbt kan ni komma ut i {_ort}?", f"Eftersom vi utgår från Bromma når vi {_ort} snabbt och kan oftast boka en besiktning inom kort. Kontakta oss så återkommer vi med tid."),
        ("Får jag ROT-avdrag?","Ja, som villaägare får du normalt ROT-avdrag på arbetskostnaden för takarbete. Vi drar av det direkt på fakturan.")])

# ====================== ARTICLES (cluster) ================================
ART_CRUMB = [("Hem","index.html"),("Artiklar","artiklar.html")]

def prose(blocks):
    out=[]
    for kind,val in blocks:
        if kind=="h2": out.append(f"          <h2>{val}</h2>")
        elif kind=="h3": out.append(f"          <h3>{val}</h3>")
        elif kind=="p": out.append(f"          <p>{val}</p>")
        elif kind=="ul":
            out.append("          <ul>\n"+"\n".join(f"            <li>{i}</li>" for i in val)+"\n          </ul>")
        elif kind=="ol":
            out.append("          <ol>\n"+"\n".join(f"            <li>{i}</li>" for i in val)+"\n          </ol>")
        elif kind=="quote": out.append(f"          <blockquote>{val}</blockquote>")
        elif kind=="tips":
            out.append(f'          <div class="tips-box"><h3>Tips</h3><p>{val}</p></div>')
        elif kind=="cta":
            out.append(f'''          <div class="inline-cta">
            <h3>{val[0]}</h3>
            <p>{val[1]}</p>
            <div class="hero-actions" style="justify-content: center">
              <a class="btn btn-primary" href="kontakt.html#form">Få offert</a>
            </div>
          </div>''')
    return "\n".join(out)

def article(file, title, description, h1, lead, blocks, related, faq=None, badge="Guide", read="5 min"):
    body = (hero(h1, lead, ART_CRUMB+[(h1,file)])
        + f"""      <section class="section">
        <article class="container article-shell content-prose">
          <p class="article-meta">Publicerad {TODAY} &middot; {read} läsning &middot; {badge}</p>
{prose(blocks)}
        </article>
      </section>"""
        + links_block("Relaterat", related))
    page(file=file, title=title, description=description, h1=h1, body=body,
         crumbs=ART_CRUMB+[(h1,file)], article=True, og_type="article", faq=faq)

article("vad-kostar-takbyte.html",
  "Vad kostar ett takbyte 2026? Pris & prisexempel | Geal Entreprenad AB",
  "Vad kostar ett takbyte på villa? Vi går igenom prisintervall, vad som påverkar kostnaden och hur ROT-avdrag sänker priset. Guide för dig i Stockholm.",
  "Vad kostar ett takbyte?",
  "Priset för ett takbyte varierar mycket beroende på tak och material. Här förklarar vi vad som driver kostnaden och hur du tolkar en offert – så att du kan jämföra på rätt grunder.",
  [("p","En av de vanligaste frågorna vi får är vad ett takbyte kostar. Det ärliga svaret är att det beror på – men det betyder inte att du är helt utan riktmärken. Kostnaden styrs framför allt av takets area, val av material, taklutning, tillgänglighet och underlagets skick."),
   ("h2","Vad påverkar priset på ett takbyte?"),
   ("ul",["<strong>Takarea och form</strong> – fler kvadratmeter och komplex takform kostar mer.",
          "<strong>Material</strong> – betongpannor är oftast billigast, tegel och plåt dyrare.",
          "<strong>Underlagets skick</strong> – behöver läkt och underlagspapp bytas ökar kostnaden.",
          "<strong>Tillgänglighet och ställning</strong> – höga eller svåråtkomliga tak kräver mer.",
          "<strong>Detaljer</strong> – skorsten, takfönster, hängrännor och taksäkerhet tillkommer."]),
   ("h2","Prisintervall – så mycket kan det landa på"),
   ("p","Exakta priser går inte att ge utan att se taket, och siffror i olika guider varierar kraftigt. Därför erbjuder vi gratis platsbesök och kostnadsförslag – då får du ett fast pris för just ditt tak."),
   ("tips","Jämför alltid offerter på samma omfattning. Ett lågt pris som saknar underlagsbyte eller plåtdetaljer blir ofta dyrare i slutänden."),
   ("h2","ROT-avdrag sänker kostnaden"),
   ("p",f"Som villaägare får du normalt ROT-avdrag på arbetskostnaden, vilket sänker slutpriset. Läs mer i {a('rot-avdrag-takarbete.html','ROT-avdrag för takarbete')}."),
   ("cta",("Få ett fast pris på ditt takbyte","Boka en kostnadsfri besiktning så får du en tydlig offert med ROT-avdrag inräknat."))],
  [("takbyte.html","Takbyte","Vår tjänst för komplett takbyte."),
   ("takbyte-eller-takrenovering.html","Takbyte eller takrenovering?","Så avgör du vilket som lönar sig."),
   ("rot-avdrag-takarbete.html","ROT-avdrag för takarbete","Så mycket kan du dra av.")],
  faq=[("Är takbyte dyrare med tegel eller plåt?","Det varierar. Betongpannor är ofta billigast, medan tegel och kvalitetsplåt kostar mer. Materialvalet påverkar även livslängd och underhåll."),
       ("Ingår rivning i priset?","I en komplett offert från oss ingår rivning och bortforsling av det gamla taket. Kontrollera alltid att det ingår när du jämför offerter.")],
  badge="Kostnad", read="6 min")

article("vad-kostar-takrenovering.html",
  "Vad kostar en takrenovering? Pris & påverkan | Geal Entreprenad AB",
  "Vad kostar en takrenovering på villa? Vi förklarar prisintervall, vad som påverkar kostnaden och när renovering lönar sig jämfört med takbyte.",
  "Vad kostar en takrenovering?",
  "En takrenovering kostar oftast mindre än ett fullt takbyte, men spannet är stort beroende på omfattning. Här går vi igenom vad som styr priset.",
  [("p","Takrenovering omfattar allt från byte av enstaka pannor till full omläggning med ny underlagspapp. Därför varierar priset kraftigt. Kostnaden avgörs av hur stor del av taket som åtgärdas, materialet och hur utsatta detaljerna är."),
   ("h2","Vad påverkar priset?"),
   ("ul",["Omfattning – punktinsats eller omläggning av hela takytan.",
          "Om underlagspapp och läkt behöver bytas.",
          "Antal plåtdetaljer och anslutningar som åtgärdas.",
          "Tillgänglighet och behov av ställning."]),
   ("h2","När lönar sig renovering framför byte?"),
   ("p",f"Om stommen är sund och skadorna är begränsade är renovering oftast mest lönsamt. Är taket vid slutet av sin livslängd blir ett {a('takbyte.html','takbyte')} bättre på sikt. En {a('takbesiktning.html','takbesiktning')} ger svar. Se även {a('takbyte-eller-takrenovering.html','takbyte eller takrenovering')}."),
   ("p","Vi erbjuder gratis platsbesök och kostnadsförslag – du får ett fast pris efter att vi sett taket."),
   ("cta",("Vill du veta vad din takrenovering kostar?","Boka besiktning så får du en tydlig åtgärdsplan och offert."))],
  [("takrenovering.html","Takrenovering","Vår tjänst för takrenovering och omläggning."),
   ("vad-kostar-takbyte.html","Vad kostar ett takbyte?","Jämför med kostnaden för byte."),
   ("rot-avdrag-takarbete.html","ROT-avdrag","Sänk kostnaden med ROT.")],
  badge="Kostnad", read="5 min")

article("takbyte-eller-takrenovering.html",
  "Takbyte eller takrenovering – vad ska jag välja? | Geal Entreprenad AB",
  "Takbyte eller takrenovering? Vi förklarar skillnaden, när respektive alternativ passar och hur du avgör vad som lönar sig för ditt tak.",
  "Takbyte eller takrenovering – vad ska du välja?",
  "Ska du byta hela taket eller räcker en renovering? Svaret avgörs av takets skick och ålder. Här är hur du tänker rätt – och undviker att betala för mycket eller för lite.",
  [("p","Det är lätt att antingen överinvestera i ett byte som inte behövdes, eller att lappa ett tak som egentligen är uttjänt. Nyckeln är att skilja på ytligt slitage och verkliga tekniska brister."),
   ("h2","När räcker en takrenovering?"),
   ("ul",["Stommen och stora ytor är fortfarande sunda.","Skadorna är begränsade till enskilda delar.",
          "Underlagspapp och läkt är i hyfsat skick.","Taket har flera år kvar av sin livslängd."]),
   ("h2","När är det dags för takbyte?"),
   ("ul",["Återkommande läckage på flera ställen.","Spröd eller trasig underlagspapp.",
          "Utbredda frostskador på pannor.","Taket närmar sig slutet av sin tekniska livslängd."]),
   ("h2","Så avgör du"),
   ("p",f"Det säkraste sättet är en {a('takbesiktning.html','takbesiktning')} som bedömer skicket objektivt. Läs även om tecknen i {a('nar-ska-taket-bytas.html','tecken på att taket behöver bytas')}."),
   ("tips","Blanda inte ihop nivåerna: ett underhållsjobb ska inte bära rollen som långsiktig lösning om taket i grunden är uttjänt.")],
  [("takbyte.html","Takbyte","När hela taket behöver bytas."),
   ("takrenovering.html","Takrenovering","När riktade åtgärder räcker."),
   ("takbesiktning.html","Takbesiktning","Få ett objektivt underlag först.")],
  faq=[("Kan ett tak renoveras flera gånger?","Ja, men vid en viss punkt blir upprepade renoveringar dyrare än ett byte. En besiktning hjälper dig se var gränsen går.")],
  badge="Guide", read="5 min")

article("rot-avdrag-takarbete.html",
  "ROT-avdrag för takarbete 2026 – så mycket kan du dra av | Geal Entreprenad AB",
  "ROT-avdrag för takbyte och takrenovering: vad som gäller, hur avdraget fungerar och hur mycket du kan dra av på arbetskostnaden. Guide för villaägare.",
  "ROT-avdrag för takarbete",
  "Takarbete på villa ger normalt rätt till ROT-avdrag på arbetskostnaden. Här förklarar vi hur det fungerar och vad du behöver tänka på.",
  [("p","ROT-avdraget gör att du får dra av en del av arbetskostnaden för renovering och underhåll av din bostad. Takbyte, takrenovering och de flesta takarbeten på villa omfattas, förutsatt att du äger bostaden och uppfyller villkoren."),
   ("h2","Hur mycket är ROT-avdraget?"),
   ("p","Avdraget gäller arbetskostnaden – inte material, resor eller administration. För 2026 är ROT-avdraget 30 % av arbetskostnaden, med ett tak på 50 000 kr per person och år. ROT och RUT delar dessutom ett gemensamt tak på 75 000 kr per person och år (Skatteverket)."),
   ("h2","Så fungerar det i praktiken"),
   ("ol",["Vi bedömer taket och lämnar offert.","Arbetskostnaden specificeras separat.",
          "Avdraget dras direkt på fakturan.","Vi begär utbetalning från Skatteverket."]),
   ("tips","ROT-avdraget är personligt och delas på antal ägare. Bor ni två som äger huset kan avdraget ofta bli högre totalt."),
   ("cta",("Vi hjälper dig med ROT","Vi drar av ROT direkt på fakturan – du ser din slutkostnad tydligt i offerten."))],
  [("takbyte.html","Takbyte","ROT gäller normalt vid takbyte."),
   ("vad-kostar-takbyte.html","Vad kostar ett takbyte?","Se hur ROT påverkar slutpriset."),
   ("bygglov-takbyte.html","Bygglov för takbyte","Vad som gäller kring tillstånd.")],
  faq=[("Gäller ROT för materialkostnaden?","Nej, ROT-avdraget gäller endast arbetskostnaden, inte material eller resekostnader."),
       ("Får jag ROT för takarbete på fritidshus?","ROT kan gälla även fritidshus om du äger det och betalar skatt i Sverige. Villkoren avgör – kontrollera med oss.")],
  badge="ROT & pengar", read="5 min")

article("sa-valjer-du-taklaggare.html",
  "Så väljer du takläggare – checklista | Geal Entreprenad AB",
  "Så väljer du rätt takläggare: checklista med frågor att ställa, vad du ska kontrollera i offerten och varningstecken att undvika.",
  "Så väljer du takläggare – checklista",
  "Att välja rätt takläggare är avgörande för resultatet. Här är en checklista som hjälper dig jämföra företag och undvika de vanligaste fallgroparna.",
  [("p","Ett takprojekt är en stor investering, och skillnaden mellan olika utförare kan vara stor. Använd checklistan nedan när du jämför takläggare."),
   ("h2","Kontrollera det här"),
   ("ul",["<strong>F-skatt och försäkring</strong> – företaget ska ha F-skatt och ansvarsförsäkring.",
          "<strong>Referenser</strong> – be om tidigare projekt, gärna i ditt område.",
          "<strong>Tydlig offert</strong> – omfattning, material och tidplan ska framgå.",
          "<strong>Garanti</strong> – fråga vad garantin omfattar och hur länge den gäller.",
          "<strong>Skriftligt avtal</strong> – muntliga överenskommelser räcker inte."]),
   ("h2","Frågor att ställa"),
   ("ol",["Ingår rivning, underlagsbyte och plåtdetaljer i priset?",
          "Vem ansvarar om något oförutsett upptäcks under arbetet?",
          "Hur hanteras ROT-avdraget?","När kan arbetet påbörjas och hur lång tid tar det?"]),
   ("tips","Var vaksam på ovanligt låga priser och krav på stora förskott. Seriösa företag ger tydliga, jämförbara offerter."),
   ("cta",("Begär en tydlig offert av oss","Vi ger en specificerad offert med omfattning, material och tidplan – enkel att jämföra."))],
  [("takbesiktning.html","Takbesiktning","Bra underlag inför offertjämförelse."),
   ("om-oss.html","Om oss","Så arbetar vi."),
   ("villatak.html","Tak på villa","Komplett guide till villatak.")],
  faq=[("Ska jag välja billigaste offerten?","Inte automatiskt. Jämför vad som ingår. En billig offert som saknar underlagsbyte eller plåtarbeten kan bli dyrare totalt.")],
  badge="Checklista", read="4 min")

article("bygglov-takbyte.html",
  "Behövs bygglov för takbyte? Så gäller reglerna | Geal Entreprenad AB",
  "Behövs bygglov för takbyte? Vi förklarar när takbyte kräver bygglov eller anmälan, och vad som gäller om du byter takmaterial eller färg.",
  "Behövs bygglov för takbyte?",
  "Ett vanligt takbyte med samma material kräver oftast inte bygglov – men det finns undantag. Här är vad som gäller för villor i Stockholmsområdet.",
  [("p","Om du byter tak med samma typ av material och behåller takets utseende krävs normalt inte bygglov. Men om bytet väsentligt ändrar byggnadens yttre utseende kan bygglov eller anmälan behövas."),
   ("h2","När kan bygglov krävas?"),
   ("ul",["Byte till ett takmaterial med tydligt annat utseende (t.ex. tegel till plåt).",
          "Byte av takets färg om det väsentligt ändrar utseendet.",
          "Om huset ligger i ett kulturhistoriskt värdefullt område.",
          "Om du samtidigt ändrar takkonstruktion eller lutning."]),
   ("p","Reglerna tolkas av din kommun, och detaljplaner skiljer sig mellan områden. Kontrollera alltid med kommunens bygglovsenhet innan du byter material eller färg. Vi hjälper dig gärna att bedöma om ditt planerade takbyte kan påverkas."),
   ("tips","Ligger huset inom detaljplan eller i ett känsligt område? Hör med kommunen först – det är billigare än att åtgärda i efterhand."),
   ("cta",("Planerar du ett takbyte?","Vi hjälper dig bedöma materialval och vad som gäller – begär en offert."))],
  [("takbyte.html","Takbyte","Vår tjänst för takbyte."),
   ("tegel-betong-plattak.html","Tegel vs betong vs plåt","Byte av material kan påverka bygglov."),
   ("rot-avdrag-takarbete.html","ROT-avdrag","Ekonomin kring takbyte.")],
  faq=[("Krävs bygglov om jag byter tegel mot likadant tegel?","Nej, normalt inte. Byte till samma typ av material som behåller utseendet är oftast bygglovsfritt, men kontrollera med din kommun."),
       ("Vem ansvarar för att söka bygglov?","Fastighetsägaren ansvarar för att nödvändiga tillstånd finns. Vi kan hjälpa till att bedöma behovet.")],
  badge="Regler", read="4 min")

# ---- problem / symptom ----
article("nar-ska-taket-bytas.html",
  "Tecken på att taket behöver bytas | Geal Entreprenad AB",
  "Vanliga tecken på att taket behöver bytas: läckage, spruckna pannor, fukt på vinden och spröd underlagspapp. Så vet du när det är dags.",
  "Tecken på att taket behöver bytas",
  "Ett tak åldras långsamt och tecknen är lätta att missa. Här är signalerna som visar att det kan vara dags att byta taket – innan skadorna sprider sig.",
  [("p","De flesta tak håller i decennier, men slitaget accelererar mot slutet av livslängden. Ju tidigare du fångar signalerna, desto mer kontrollerad blir åtgärden."),
   ("h2","Signaler att hålla koll på"),
   ("ul",["Återkommande läckage eller fuktfläckar i undertak och på vind.",
          "Spruckna, lösa eller frostskadade pannor.","Mossa och påväxt som håller kvar fukt.",
          "Spröd eller skadad underlagspapp.","Rostiga eller otäta plåtdetaljer.",
          "Genomböjning eller ojämnheter i takytan."]),
   ("h2","Vad du bör göra"),
   ("p",f"Enskilda tecken betyder inte alltid att hela taket måste bytas. När flera signaler uppträder samtidigt bör du dock göra en {a('takbesiktning.html','takbesiktning')}. Den visar om det räcker med {a('takrenovering.html','takrenovering')} eller om ett {a('takbyte.html','takbyte')} är rätt."),
   ("tips","Kontrollera vinden inifrån efter kraftigt regn – fuktfläckar och dagsljus genom taket är tydliga varningstecken.")],
  [("takbesiktning.html","Takbesiktning","Få skicket bedömt."),
   ("taklackage.html","Takläckage","Vad du gör vid läckage."),
   ("takbyte-eller-takrenovering.html","Byte eller renovering?","Så väljer du rätt.")],
  faq=[("Hur gammalt kan ett tak bli?","Det beror på material: betongpannor 30–50 år, tegel 50+ år, plåt 40–50 år. Underhåll och läge påverkar mycket.")],
  badge="Besiktning", read="5 min")

article("taklackage.html",
  "Takläckage – vad göra och vanliga orsaker | Geal Entreprenad AB",
  "Takläckage? Vi förklarar vanliga orsaker, vad du bör göra direkt och hur läckan åtgärdas. Snabb hjälp med tak i Stockholm och Sundbyberg.",
  "Takläckage – orsaker och vad du gör",
  "Ett takläckage bör åtgärdas snabbt innan fukten sprider sig i konstruktionen. Här är de vanligaste orsakerna och vad du bör göra direkt.",
  [("p","Vatten som tar sig in genom taket följer ofta konstruktionen en bit innan det syns inne i huset. Därför är själva läckans källa sällan rakt ovanför fuktfläcken – det kräver erfarenhet att spåra."),
   ("h2","Vanliga orsaker till takläckage"),
   ("ul",["Otäta anslutningar mot skorsten, takfönster och genomföringar.",
          "Trasiga eller förskjutna pannor.","Skadad underlagspapp.",
          "Igensatta eller trasiga hängrännor och stuprör.","Isbildning som tvingar in smältvatten."]),
   ("h2","Vad du bör göra direkt"),
   ("ol",["Placera kärl under läckan och skydda ömtåliga föremål.",
          "Dokumentera med foto.","Undvik att själv klättra på ett vått tak.",
          "Kontakta en takläggare för felsökning och åtgärd."]),
   ("p",f"Vi spårar läckan, åtgärdar orsaken och bedömer om det räcker med reparation eller om en större {a('takrenovering.html','takrenovering')} behövs. Vid utbredda skador kan {a('fuktskada-mogel-vind.html','fukt på vinden')} behöva åtgärdas."),
   ("cta",("Har du ett takläckage?","Kontakta oss för snabb felsökning och åtgärd innan skadan sprider sig."))],
  [("takbesiktning.html","Takbesiktning","Hitta orsaken till läckan."),
   ("hangrannor-stupror.html","Hängrännor & stuprör","Vanlig orsak till fukt."),
   ("fuktskada-mogel-vind.html","Fukt & mögel på vind","När läckan gett följdskador.")],
  faq=[("Hur snabbt bör ett takläckage åtgärdas?","Så snabbt som möjligt. Även små läckor kan ge fukt- och mögelskador i konstruktionen om de får fortsätta."),
       ("Täcker försäkringen takläckage?","Det beror på orsak och villkor. Plötsliga skador täcks oftare än långsamt slitage. Kontrollera med ditt försäkringsbolag.")],
  badge="Problem", read="5 min")

article("fuktskada-mogel-vind.html",
  "Fuktskada och mögel på vinden – orsaker & åtgärd | Geal Entreprenad AB",
  "Fukt och mögel på vinden: vanliga orsaker som dålig ventilation och takläckage, symptom att känna igen och hur problemet åtgärdas.",
  "Fuktskada och mögel på vinden",
  "Fukt på vinden leder ofta till mögel om det får fortsätta. Här går vi igenom orsaker, symptom och hur du åtgärdar problemet vid roten.",
  [("p","Vindsutrymmen är känsliga för fukt eftersom varm, fuktig luft nerifrån möter kalla ytor. I kombination med bristande ventilation eller ett läckande tak skapas grogrund för mögel."),
   ("h2","Vanliga orsaker"),
   ("ul",["Takläckage som fört in vatten i konstruktionen.","Dålig vindsventilation.",
          "Bristfällig isolering och luftläckage nerifrån.","Kondens på undertak vintertid."]),
   ("h2","Symptom att känna igen"),
   ("ul",["Mörka fläckar eller påväxt på undertak och takstolar.","Mögellukt på vinden.",
          "Fuktfläckar och missfärgningar.","Frost eller kondens på undersidan av taket vintertid."]),
   ("p",f"Åtgärden börjar med att hitta källan – ofta ett {a('taklackage.html','takläckage')} eller ventilationsproblem. Vi gör en {a('takbesiktning.html','takbesiktning')} och åtgärdar orsaken. Rätt {a('vindsisolering.html','vindsisolering')} och ventilation minskar risken framåt."),
   ("tips","Måla eller sanera aldrig över mögel utan att åtgärda fuktkällan först – då kommer det tillbaka.")],
  [("takbesiktning.html","Takbesiktning","Hitta fuktkällan."),
   ("vindsisolering.html","Vindsisolering","Rätt isolering och ventilation."),
   ("taklackage.html","Takläckage","Vanlig orsak till vindsfukt.")],
  faq=[("Är mögel på vinden farligt?","Mögel kan påverka inomhusmiljön och byggnaden. Det bör saneras och fuktkällan åtgärdas för att undvika återkommande problem.")],
  badge="Problem", read="5 min")

article("mossa-pa-taket.html",
  "Mossa på taket – behandling och förebyggande | Geal Entreprenad AB",
  "Mossa på taket: varför den uppstår, om den är skadlig och hur du tar bort och förebygger mossa. Skonsam taktvätt i Stockholm.",
  "Mossa på taket – behandling och förebyggande",
  "Mossa på taket är vanligt i skuggiga, trädnära lägen. Här förklarar vi när mossan är ett problem och hur du tar bort den utan att skada taket.",
  [("p","Mossa och alger trivs på fuktiga, beskuggade takytor. Utöver det estetiska håller mossan kvar fukt, kan lyfta pannor och försämra avvattningen – vilket på sikt sliter på taket."),
   ("h2","Är mossa skadligt?"),
   ("p","Måttlig påväxt är sällan akut, men lämnad över tid kan mossan bidra till fuktskador och frostsprängning i pannor. På plåttak kan den påskynda korrosion. Regelbunden kontroll och rengöring lönar sig."),
   ("h2","Så tar du bort mossa"),
   ("ul",["Skonsam borttagning – undvik högtryck som skadar ytskiktet.",
          "Rengör hängrännor och stuprör samtidigt.","Behandling som förebygger ny påväxt.",
          "Kontroll av pannor och detaljer efteråt."]),
   ("p",f"Vi utför {a('taktvatt.html','taktvätt')} med metod anpassad efter taktyp. Vid samtidigt behov av nytt ytskydd på plåttak kan {a('takmalning.html','takmålning')} göras i anslutning."),
   ("tips","Beskär träd som skuggar taket – mer sol och luft minskar återväxten av mossa märkbart.")],
  [("taktvatt.html","Taktvätt","Skonsam rengöring av taket."),
   ("hangrannor-stupror.html","Hängrännor & stuprör","Rensa avvattningen samtidigt."),
   ("takmalning.html","Takmålning","Nytt ytskydd på plåttak.")],
  faq=[("Kan jag ta bort mossa själv?","Enklare rengöring går att göra själv, men undvik högtryck och osäkert klättrande. För större ytor och säkerhet anlitar du en takläggare.")],
  badge="Underhåll", read="4 min")

article("istappar-isbildning.html",
  "Istappar och isbildning på tak – orsaker & åtgärd | Geal Entreprenad AB",
  "Istappar och isbildning på taket: varför det uppstår, riskerna och hur du förebygger med isolering, ventilation och snöskottning.",
  "Istappar och isbildning på tak",
  "Istappar och isvallar vid takfoten är vanligt vintertid och kan skada både tak och avvattning. Här är orsakerna och hur du förebygger problemet.",
  [("p","Isbildning uppstår när värme läcker upp genom taket, smälter snö som sedan fryser vid den kallare takfoten. Resultatet blir isvallar och istappar som kan tvinga in smältvatten under pannorna."),
   ("h2","Varför bildas is och istappar?"),
   ("ul",["Värmeläckage från bostaden upp till vinden.","Bristande isolering och ventilation.",
          "Snö som smälter och återfryser vid takfoten.","Igensatta hängrännor som samlar is."]),
   ("h2","Så förebygger du"),
   ("ul",[f"Förbättra {a('vindsisolering.html','vindsisolering och ventilation')}.",
          "Håll hängrännor och stuprör rena.","Skotta av taket vid stora snömängder.",
          "Montera vid behov snörasskydd och värmekabel."]),
   ("p",f"Istappar är också en säkerhetsrisk för förbipasserande. Läs mer om {a('taksakerhet-snorasskydd.html','taksäkerhet och snörasskydd')}. Har is redan gett läckage, se {a('taklackage.html','takläckage')}."),
   ("tips","Skotta aldrig taket på ett sätt som skadar pannorna eller dig själv – vid stora snömängder anlitar du proffs.")],
  [("vindsisolering.html","Vindsisolering","Minska värmeläckaget."),
   ("taksakerhet-snorasskydd.html","Taksäkerhet & snörasskydd","Skydd mot snö och is."),
   ("hangrannor-stupror.html","Hängrännor & stuprör","Fri avvattning minskar is.")],
  badge="Säsong", read="4 min")

# ---- components ----
article("hangrannor-stupror.html",
  "Hängrännor & stuprör – byte, rensning och renovering | Geal Entreprenad AB",
  "Hängrännor och stuprör: byte, rensning och renovering av takavvattning. Undvik fukt- och fasadskador. Takläggare i Stockholm och Sundbyberg.",
  "Hängrännor och stuprör",
  "Fungerande takavvattning skyddar både tak och fasad. Här går vi igenom när hängrännor och stuprör behöver rensas, renoveras eller bytas.",
  [("p","Hängrännor och stuprör leder bort vatten från taket. Är de igensatta eller trasiga rinner vattnet fel – vilket ger fuktskador på fasad, grund och tak. Avvattning är en billig detalj som förebygger dyra skador."),
   ("h2","När behöver de åtgärdas?"),
   ("ul",["Vatten rinner över kanten vid regn.","Rost, hål eller glapp i skarvar.",
          "Rännor som lutar fel eller lossnat.","Återkommande löv och skräp som täpper igen."]),
   ("h2","Vad vi gör"),
   ("ul",["Rensning av rännor och stuprör.","Byte av trasiga sektioner eller hela systemet.",
          "Justering av lutning och infästning.","Montering av lövsilar vid behov."]),
   ("p",f"Vi byter ofta hängrännor i samband med {a('takbyte.html','takbyte')} eller {a('takrenovering.html','takrenovering')}. Dålig avvattning är också en vanlig orsak till {a('taklackage.html','takläckage')} och {a('istappar-isbildning.html','isbildning')}."),
   ("tips","Rensa rännorna höst och vår, särskilt om du har träd nära huset – det förebygger både fukt och is.")],
  [("takbyte.html","Takbyte","Ny avvattning ingår ofta."),
   ("taktvatt.html","Taktvätt","Rengör rännor samtidigt."),
   ("istappar-isbildning.html","Istappar","Fri avvattning minskar is.")],
  badge="Komponent", read="4 min")

article("takfonster.html",
  "Takfönster – montering och byte | Geal Entreprenad AB",
  "Takfönster: montering av nytt och byte av gammalt takfönster med täta anslutningar. Undvik läckage kring takfönster. Takläggare i Stockholm.",
  "Takfönster – montering och byte",
  "Takfönster ger ljus men är en vanlig källa till läckage om anslutningen är otät. Här är vad som gäller vid montering och byte.",
  [("p","Ett takfönster bryter takets yta och kräver noggranna anslutningar mot pannor eller plåt. De flesta problem med takfönster beror inte på fönstret i sig, utan på hur intäckningen runt det är utförd."),
   ("h2","När byta takfönster?"),
   ("ul",["Kondens mellan glasen eller dålig täthet.","Läckage kring karm och intäckning.",
          "Gammalt fönster med dålig isolering.","I samband med takbyte – passa på att byta."]),
   ("h2","Vad vi gör"),
   ("ul",["Montering av nya takfönster.","Byte av befintliga med ny intäckning.",
          "Täta anslutningar mot tak och underlagspapp.","Åtgärd av läckage kring befintliga fönster."]),
   ("p",f"Vi byter gärna takfönster i samband med {a('takbyte.html','takbyte')}, då intäckningen ändå görs om. Läcker det redan, se {a('taklackage.html','takläckage')}."),
   ("tips","Byt takfönster samtidigt som taket – då blir intäckningen tät och du slipper ett separat ingrepp senare.")],
  [("takbyte.html","Takbyte","Byt fönster samtidigt."),
   ("taklackage.html","Takläckage","Läckage kring fönster."),
   ("villatak.html","Tak på villa","Komplett guide.")],
  badge="Komponent", read="4 min")

article("taksakerhet-snorasskydd.html",
  "Taksäkerhet – snörasskydd, takstege & glidskydd | Geal Entreprenad AB",
  "Taksäkerhet: snörasskydd, takstege, nockräcke och glidskydd. Lagkrav och skydd för sotare, hantverkare och förbipasserande. Montering i Stockholm.",
  "Taksäkerhet – snörasskydd och takstege",
  "Taksäkerhet handlar om att skydda både de som arbetar på taket och de som rör sig runt huset. Här är vad som gäller och vad som ofta krävs.",
  [("p","Det finns krav på taksäkerhet för att sotare och hantverkare ska kunna arbeta säkert, och för att snö och is inte ska rasa ner på människor nedanför. Kraven beror på takets höjd och lutning."),
   ("h2","Vanliga taksäkerhetsdetaljer"),
   ("ul",["<strong>Snörasskydd</strong> – hindrar snö och is från att rasa ner.",
          "<strong>Takstege</strong> – säker väg till skorsten och nock.",
          "<strong>Nockräcke och glidskydd</strong> – hållpunkter vid arbete.",
          "<strong>Fästöglor</strong> för säkerhetslina."]),
   ("h2","När monteras det?"),
   ("p",f"Taksäkerhet ses ofta över i samband med {a('takbyte.html','takbyte')}, men kan även monteras separat. Snörasskydd är extra viktigt över entréer, gångar och parkeringar. Läs även om {a('istappar-isbildning.html','istappar och isbildning')}."),
   ("tips","Har du snörasskydd över dörrar och gångbanor? Det är både ett krav i många fall och ett skydd mot skadeståndsansvar.")],
  [("takbyte.html","Takbyte","Taksäkerhet ses över vid byte."),
   ("istappar-isbildning.html","Istappar & is","Minska risken för ras."),
   ("skorstensrenovering.html","Skorsten","Säker åtkomst för sotare.")],
  badge="Komponent", read="4 min")

article("skorstensrenovering.html",
  "Skorstensrenovering och skorstensbeslag | Geal Entreprenad AB",
  "Skorstensrenovering: tätning, skorstensbeslag och plåtarbeten kring skorsten. Åtgärda läckage och slitage vid skorstenen. Takläggare i Stockholm.",
  "Skorstensrenovering och skorstensbeslag",
  "Skorstenen är en av takets vanligaste läckagepunkter. Här går vi igenom beslag, tätning och renovering av plåtarbetet kring skorstenen.",
  [("p","Anslutningen mellan skorsten och tak är utsatt. Gamla eller dåligt utförda skorstensbeslag släpper in vatten, och murad skorsten kan vittra över tid. Rätt plåtarbete kring skorstenen är avgörande för ett tätt tak."),
   ("h2","Vanliga problem"),
   ("ul",["Otäta eller rostiga skorstensbeslag.","Sprickor i fogar och puts.",
          "Läckage där skorsten möter taket.","Slitna anslutningar efter takets ålder."]),
   ("h2","Vad vi gör"),
   ("ul",["Byte av skorstensbeslag och intäckning.","Tätning av anslutningar mot taket.",
          "Plåtarbeten anpassade efter taktyp.","Åtgärd i samband med takbyte eller renovering."]),
   ("p",f"Vi åtgärdar skorstensbeslag separat eller som del av ett {a('takbyte.html','takbyte')}. Misstänker du läckage vid skorstenen, se {a('taklackage.html','takläckage')}. Vi utför även murning och tätning kring skorstenen vid behov – hela skorstensarbetet på ett ställe."),
   ("tips","Kontrollera skorstensbeslaget vid varje takbesiktning – det är en liten detalj som orsakar många läckor.")],
  [("takbyte.html","Takbyte","Beslag byts vid takbyte."),
   ("taklackage.html","Takläckage","Skorstenen läcker ofta."),
   ("takbesiktning.html","Takbesiktning","Kontroll av anslutningar.")],
  badge="Komponent", read="4 min")

# ---- material / energy ----
article("tegel-betong-plattak.html",
  "Tegeltak vs betongpannor vs plåttak – för- och nackdelar | Geal Entreprenad AB",
  "Tegeltak, betongpannor eller plåttak? Vi jämför pris, livslängd, vikt, underhåll och utseende så att du kan välja rätt takmaterial för din villa.",
  "Tegeltak vs betongpannor vs plåttak",
  "Valet av takmaterial påverkar pris, livslängd och utseende i decennier framåt. Här jämför vi de tre vanligaste materialen för villatak.",
  [("p","Tegel, betong och plåt dominerar villataken i Stockholm. Alla tre fungerar bra – men de har olika styrkor. Rätt val beror på husets lutning, stil, budget och hur mycket underhåll du vill ha."),
   ("h2","Tegelpannor"),
   ("ul",["Lång livslängd, ofta 50 år eller mer.","Klassiskt utseende, färgäkta.",
          "Tyngre – kräver att takstolarna klarar lasten.","Högre materialkostnad."]),
   ("h2","Betongpannor"),
   ("ul",["Oftast lägst materialkostnad.","Bra livslängd, cirka 30–50 år.",
          "Tyngre än plåt, kan behöva mossbehandling.","Vanligast på svenska villor."]),
   ("h2","Plåttak"),
   ("ul",["Låg vikt – passar även låga lutningar.","Livslängd 40–50 år, kan ommålas.",
          "Snabb montering.","Kräver noggranna plåtarbeten för täthet."]),
   ("p",f"Se hur länge materialen håller i {a('takmaterial-livslangd.html','livslängd per takmaterial')}. Vill du ha plåt hjälper vi dig med {a('plattak.html','plåttak')}, och byte sköts via {a('takbyte.html','takbyte')}."),
   ("tips","Byter du från pannor till plåt eller tvärtom – kolla vikt och ev. bygglov, se guiden om bygglov för takbyte.")],
  [("takmaterial-livslangd.html","Livslängd per material","Så länge håller taken."),
   ("plattak.html","Plåttak","Vår tjänst för plåttak."),
   ("bygglov-takbyte.html","Bygglov för takbyte","Vid byte av material.")],
  faq=[("Vilket takmaterial är billigast?","Betongpannor har oftast lägst materialkostnad. Totalkostnaden beror dock även på tak, underlag och arbete."),
       ("Är plåttak bättre än tegel?","Inget är objektivt bäst. Plåt passar låga lutningar och ger låg vikt; tegel ger lång livslängd och klassiskt utseende.")],
  badge="Material", read="6 min")

article("takmaterial-livslangd.html",
  "Livslängd per takmaterial – så länge håller taket | Geal Entreprenad AB",
  "Hur länge håller olika tak? Livslängd för tegel, betongpannor, plåttak och papptak – och vad som påverkar hur länge ditt tak håller.",
  "Livslängd per takmaterial",
  "Hur länge ett tak håller beror på material, utförande och underhåll. Här är typiska livslängder och vad som förlänger dem.",
  [("p","Att känna till takets förväntade livslängd hjälper dig planera ekonomiskt. Siffrorna nedan är riktvärden – läge, lutning och underhåll påverkar utfallet mycket."),
   ("h2","Typisk livslängd"),
   ("ul",["<strong>Tegelpannor:</strong> 50+ år.","<strong>Betongpannor:</strong> 30–50 år.",
          "<strong>Plåttak:</strong> 40–50 år, kan ommålas.","<strong>Papptak:</strong> 20–30 år.",
          "<strong>Underlagspapp:</strong> 30–40 år (ofta takets svaga länk)."]),
   ("h2","Vad förlänger livslängden?"),
   ("ul",[f"Regelbunden {a('taktvatt.html','taktvätt')} och borttagning av mossa.",
          "Fungerande avvattning och ventilation.","Åtgärd av små skador i tid.",
          "Kontroll vid varje säsongsskifte."]),
   ("p",f"Ofta är det underlagspappen, inte pannorna, som avgör när ett {a('takbyte.html','takbyte')} behövs. En {a('takbesiktning.html','takbesiktning')} visar var ditt tak står."),
   ("tips","Pannor kan se fina ut länge medan underlagspappen under dem är uttjänt – bedöm alltid helheten.")],
  [("tegel-betong-plattak.html","Jämför takmaterial","För- och nackdelar."),
   ("takbesiktning.html","Takbesiktning","Bedöm ditt taks status."),
   ("takbyte.html","Takbyte","När livslängden är nådd.")],
  badge="Material", read="4 min")

article("vindsisolering.html",
  "Vindsisolering och tilläggsisolering | Geal Entreprenad AB",
  "Vindsisolering och tilläggsisolering av vind: sänk uppvärmningskostnaden, minska kondens och istappar. Ofta smart att kombinera med takbyte.",
  "Vindsisolering och tilläggsisolering",
  "Att tilläggsisolera vinden är en av de mest lönsamma energiåtgärderna – och passar ofta att göra i samband med takarbete.",
  [("p","En stor del av husets värme försvinner uppåt. Bra vindsisolering sänker uppvärmningskostnaden, jämnar ut inomhusklimatet och minskar problem med kondens och isbildning på taket."),
   ("h2","Fördelar med tilläggsisolering"),
   ("ul",["Lägre uppvärmningskostnad.","Jämnare inomhustemperatur.",
          f"Mindre risk för {a('istappar-isbildning.html','istappar och isbildning')}.",
          f"Minskad risk för {a('fuktskada-mogel-vind.html','kondens och fukt på vinden')}."]),
   ("h2","Tänk på ventilationen"),
   ("p","Isolering utan fungerande ventilation kan öka fuktrisken. Därför ser vi alltid till helheten – isolering och luftning måste fungera ihop. Vid ett takbyte är vinden ofta lätt åtkomlig, vilket gör det till ett bra tillfälle."),
   ("p",f"Vi bedömer isolering och ventilation i samband med {a('takbyte.html','takbyte')} och {a('takbesiktning.html','takbesiktning')}. Vi utför även isolerarbeten, som en del av ett takprojekt eller separat."),
   ("tips","Kombinera tilläggsisolering med takbyte – du sparar etableringskostnad och får både tätt tak och lägre energiförbrukning.")],
  [("takbyte.html","Takbyte","Bra tillfälle att isolera."),
   ("energieffektivt-tak.html","Energieffektivt tak","Fler energiåtgärder."),
   ("fuktskada-mogel-vind.html","Fukt på vind","Ventilation och isolering.")],
  badge="Energi", read="4 min")

article("energieffektivt-tak.html",
  "Energieffektivt tak – så sänker du energiförbrukningen | Geal Entreprenad AB",
  "Energieffektivt tak: isolering, ventilation, ljusa material och solceller. Så påverkar taket husets energiförbrukning och inomhusklimat.",
  "Energieffektivt tak",
  "Taket har stor betydelse för husets energiförbrukning. Här är åtgärderna som gör taket mer energieffektivt – från isolering till solceller.",
  [("p","Ett energieffektivt tak handlar om mer än isolering. Ventilation, material och möjligheten att producera egen el spelar in. Bäst effekt får du genom att se helheten, gärna i samband med ett takbyte."),
   ("h2","Åtgärder som gör skillnad"),
   ("ul",[f"{a('vindsisolering.html','Tilläggsisolering av vinden')} – minskar värmeförlusten.",
          "Rätt vindsventilation – balanserar fukt och temperatur.",
          "Ljusa takmaterial – kan minska värme sommartid.",
          f"{a('solceller-tak.html','Solceller på taket')} – egen elproduktion."]),
   ("h2","Varför göra det vid takbyte?"),
   ("p",f"När taket ändå är öppet är det kostnadseffektivt att förbättra isolering och förbereda för solceller. Se {a('takbyte.html','takbyte')} och planera helheten från start."),
   ("tips","Tänk energismart redan i offertskedet – det är billigare att bygga in åtgärderna än att komplettera senare.")],
  [("vindsisolering.html","Vindsisolering","Störst energieffekt."),
   ("solceller-tak.html","Solceller på tak","Egen elproduktion."),
   ("takbyte.html","Takbyte","Planera energismart.")],
  badge="Energi", read="4 min")

article("solceller-tak.html",
  "Solceller på tak – vad du bör tänka på | Geal Entreprenad AB",
  "Solceller på taket: hur de påverkar taket, varför takets skick är avgörande och varför du bör samordna solceller med takbyte.",
  "Solceller på tak – tänk på detta",
  "Solceller och tak hänger ihop. Här förklarar vi varför takets skick är avgörande innan du monterar solceller – och varför timing spelar roll.",
  [("p","Solceller monteras på taket och sitter där i decennier. Därför är takets skick avgörande: du vill inte upptäcka att taket behöver bytas strax efter att panelerna satts upp."),
   ("h2","Varför takets skick är avgörande"),
   ("ul",["Solceller håller ofta 25–30 år – taket bör hålla minst lika länge.",
          "Att demontera och återmontera paneler vid ett takbyte kostar extra.",
          "Infästningar måste göras täta för att undvika läckage.",
          "Takets bärighet och lutning påverkar installationen."]),
   ("h2","Samordna med takbyte"),
   ("p",f"Är taket nära slutet av sin livslängd är det klokt att göra {a('takbyte.html','takbytet')} först, eller samtidigt. Gör en {a('takbesiktning.html','takbesiktning')} innan du beslutar om solceller."),
   ("p","Vi monterar solceller och ansvarar för att infästningarna blir täta – vi hanterar både tak och solceller i samma projekt."),
   ("tips","Fråga alltid om takets återstående livslängd innan du investerar i solceller – det avgör ordningen.")],
  [("takbyte.html","Takbyte","Gör taket klart först."),
   ("takbesiktning.html","Takbesiktning","Bedöm taket innan solceller."),
   ("energieffektivt-tak.html","Energieffektivt tak","Solceller i sammanhang.")],
  badge="Energi", read="4 min")

# ---- seasonal ----
article("takarbete-vintern.html",
  "Takarbete på vintern – går det? | Geal Entreprenad AB",
  "Går det att göra takarbete på vintern? Vad som fungerar, vad som bör vänta och hur snö och kyla påverkar takbyte och reparationer.",
  "Takarbete på vintern",
  "Går det att byta eller reparera tak på vintern? Kort svar: ofta ja, men med anpassningar. Här är vad som gäller under kalla månader.",
  [("p","Takarbete stannar inte helt vintertid, men kyla, snö och halka ställer krav. Akuta reparationer som läckage måste ofta göras direkt, medan större projekt kan planeras med hänsyn till väder."),
   ("h2","Vad fungerar vintertid?"),
   ("ul",[f"Akut åtgärd av {a('taklackage.html','takläckage')}.","Snöskottning och borttagning av istappar.",
          "Vissa reparationer och plåtarbeten.","Planering och besiktning inför vårens projekt."]),
   ("h2","Vad bör vänta?"),
   ("ul",["Vissa material kräver temperatur över en viss gräns.",
          "Omfattande takbyten planeras ofta till barmarkssäsong.","Arbeten som kräver torrt underlag."]),
   ("p",f"Vintern är ett bra tillfälle att boka {a('takbesiktning.html','takbesiktning')} och planera ett {a('takbyte.html','takbyte')} till våren. Se även {a('istappar-isbildning.html','istappar och isbildning')}."),
   ("tips","Boka besiktning på vintern – då kan arbetet starta tidigt på våren innan kön byggs upp.")],
  [("var-checklista-tak.html","Vår-checklista för taket","Kontrollera efter vintern."),
   ("istappar-isbildning.html","Istappar & is","Vinterns takproblem."),
   ("takbesiktning.html","Takbesiktning","Planera inför våren.")],
  badge="Säsong", read="4 min")

article("var-checklista-tak.html",
  "Vår-checklista för taket – kontrollera efter vintern | Geal Entreprenad AB",
  "Vår-checklista för taket: kontrollera pannor, hängrännor, plåt och vind efter vintern. Upptäck skador i tid innan de växer.",
  "Vår-checklista för taket",
  "Efter vintern är det läge att se över taket. Med den här checklistan upptäcker du vinterskador i tid – innan de blir dyra.",
  [("p","Vintern är hård mot taket: snölast, is och temperaturväxlingar sliter. En enkel genomgång på våren gör att du hinner åtgärda skador innan sommarregnen ställer krav på tätheten."),
   ("h2","Checklista för våren"),
   ("ul",["Kontrollera pannor – spruckna, lösa eller förskjutna.",
          f"Rensa {a('hangrannor-stupror.html','hängrännor och stuprör')} från löv och grus.",
          "Se över plåtdetaljer, beslag och anslutningar.",
          f"Titta efter {a('mossa-pa-taket.html','mossa och påväxt')}.",
          f"Kontrollera vinden efter {a('fuktskada-mogel-vind.html','fukt och kondens')}.",
          "Notera fuktfläckar i undertak."]),
   ("h2","När kalla in proffs?"),
   ("p",f"Ser du flera tecken samtidigt, eller är osäker, boka en {a('takbesiktning.html','takbesiktning')}. Då får du en tydlig bild inför sommaren och kan planera ev. {a('takrenovering.html','renovering')} i god tid."),
   ("tips","Gör vårkontrollen till en rutin – tio minuters översyn kan spara dig ett stort läckage längre fram.")],
  [("takbesiktning.html","Takbesiktning","Boka efter vintern."),
   ("takarbete-vintern.html","Takarbete på vintern","Vad som gäller kalla månader."),
   ("hangrannor-stupror.html","Hängrännor & stuprör","Rensa avvattningen.")],
  badge="Säsong", read="4 min")

# ====================== FAQ + INTEGRITETSPOLICY ==========================
page(file="faq.html",
  title="Vanliga frågor om tak och takarbete | Geal Entreprenad AB",
  description="Vanliga frågor om takbyte, takrenovering, ROT-avdrag, pris, garanti och besiktning. Svar från takläggare i Bromma, Sundbyberg och Stockholm.",
  h1="Vanliga frågor om tak",
  crumbs=[("Hem","index.html"),("Vanliga frågor","faq.html")],
  cta=("Har du en fråga vi inte besvarat?","Kontakta oss så hjälper vi dig – gratis platsbesök och kostnadsförslag."),
  body=hero("Vanliga frågor om tak",
    "Här har vi samlat de vanligaste frågorna vi får om takbyte, takrenovering, pris, ROT-avdrag och garanti. Hittar du inte svaret är du välkommen att kontakta oss.",
    [("Hem","index.html"),("Vanliga frågor","faq.html")])
    + links_block("Läs mer om våra tjänster", [
        ("takbyte.html","Takbyte","Komplett byte av tegel-, betong- och plåttak."),
        ("takrenovering.html","Takrenovering","Riktade åtgärder som förlänger takets liv."),
        ("rot-avdrag-takarbete.html","ROT-avdrag","Så mycket kan du dra av 2026.")], muted=False),
  faq=[
    ("Vad kostar ett takbyte?","Priset beror på takets area, material, lutning, tillgänglighet och underlagets skick. Vi erbjuder alltid gratis platsbesök och kostnadsförslag så att du får ett fast pris för just ditt tak."),
    ("Får jag ROT-avdrag för takarbete?","Ja, som villaägare får du normalt ROT-avdrag på arbetskostnaden. För 2026 är avdraget 30 % av arbetskostnaden, med ett tak på 50 000 kr per person och år. Vi drar av det direkt på fakturan."),
    ("Hur lång tid tar ett takbyte?","De flesta villatakbyten tar cirka 1–2 veckor beroende på takets storlek, väder och eventuella underliggande skador. Du får en preliminär tidplan i offerten."),
    ("Behöver jag byta hela taket eller räcker en renovering?","Det beror på skicket. Om grundkonstruktionen är sund kan en takrenovering räcka. En takbesiktning ger svar innan du beslutar."),
    ("Lämnar ni garanti på arbetet?","Ja, garanti och villkor framgår alltid i offert och avtal så att du vet vad som gäller för just ditt projekt."),
    ("Är offert och platsbesök kostnadsfritt?","Ja, vi erbjuder gratis platsbesök och kostnadsförslag. Du binder dig inte till något genom att begära offert."),
    ("Vilka områden arbetar ni i?","Vi utgår från Bromma (Mariehäll) och arbetar i hela Storstockholm, bland annat Sundbyberg, Solna, Spånga, Sollentuna, Järfälla, Täby, Danderyd, Lidingö och Nacka."),
    ("Behövs bygglov för takbyte?","Ett vanligt takbyte med samma material kräver oftast inte bygglov, men byte av material eller färg kan kräva det. Vi hjälper dig bedöma och du kontrollerar med kommunen."),
    ("Har ni försäkring och F-skatt?","Ja, vi är ett registrerat aktiebolag med F-skatt och ansvarsförsäkring, och våra hantverkare är anslutna till ID06."),
    ("Kan ni ta hand om hela renoveringen?","Ja, vi utför även total entreprenad och kan samordna taket med fasad, fönster och annan renovering av villan.")])

_pol_blocks = [
  ("p", f"<em>Senast uppdaterad {TODAY}.</em>"),
  ("h2","Personuppgiftsansvarig"),
  ("p","Geal Entreprenad AB (org.nr 559303-7566), Byggmästarvägen 18, 168 32 Bromma, är personuppgiftsansvarig för behandlingen av dina personuppgifter. Kontakt: <a class=\"text-link\" href=\"mailto:info@villatakservice.se\">info@villatakservice.se</a>, <a class=\"text-link\" href=\"tel:+46812410276\">08 12 410 276</a>."),
  ("h2","Vilka uppgifter vi samlar in"),
  ("p","När du använder vårt kontaktformulär eller kontaktar oss via telefon eller e-post behandlar vi de uppgifter du lämnar, till exempel namn, telefonnummer, e-postadress, adress/fastighet och det meddelande du skickar."),
  ("h2","Varför vi behandlar uppgifterna"),
  ("ul",["För att besvara din förfrågan och lämna offert.","För att planera och utföra ett eventuellt takprojekt.","För att uppfylla rättsliga skyldigheter, t.ex. bokföring och underlag för ROT-avdrag."]),
  ("p","Den rättsliga grunden är att kunna vidta åtgärder på din begäran inför ett avtal, att fullgöra avtal samt att uppfylla rättsliga förpliktelser."),
  ("h2","Hur länge vi sparar uppgifterna"),
  ("p","Vi sparar dina uppgifter så länge det behövs för ändamålet. Förfrågningar som inte leder till uppdrag gallras när de inte längre är aktuella. Uppgifter kopplade till avtal och fakturor sparas så länge bokföringslagen kräver."),
  ("h2","Vem vi delar uppgifter med"),
  ("p","Vi säljer aldrig dina uppgifter. Vi kan dela uppgifter med Skatteverket (för ROT-avdrag) och med leverantörer som hjälper oss med t.ex. IT och bokföring, vilka då behandlar uppgifterna för vår räkning."),
  ("h2","Cookies och tredjepartstjänster"),
  ("p","Webbplatsen använder inte cookies för spårning eller marknadsföring. Sidan laddar typsnitt från Google Fonts och visar en inbäddad karta från OpenStreetMap på kontaktsidan; dessa tjänster kan ta emot din IP-adress när innehållet laddas."),
  ("h2","Dina rättigheter"),
  ("ul",["Få tillgång till de uppgifter vi har om dig.","Begära rättelse av felaktiga uppgifter.","Begära radering eller begränsning av behandlingen.","Invända mot behandlingen och begära dataportabilitet.","Lämna klagomål till Integritetsskyddsmyndigheten (IMY)."]),
  ("p","Vill du utöva någon av dina rättigheter kontaktar du oss på <a class=\"text-link\" href=\"mailto:info@villatakservice.se\">info@villatakservice.se</a>."),
]
page(file="integritetspolicy.html", no_cta=True,
  title="Integritetspolicy | Geal Entreprenad AB",
  description="Integritetspolicy för villatakservice.se (Geal Entreprenad AB). Så behandlar vi dina personuppgifter enligt GDPR när du kontaktar oss.",
  h1="Integritetspolicy",
  crumbs=[("Hem","index.html"),("Integritetspolicy","integritetspolicy.html")],
  body=hero("Integritetspolicy",
    "Vi värnar om din integritet. Här beskriver vi hur Geal Entreprenad AB behandlar dina personuppgifter enligt dataskyddsförordningen (GDPR).",
    [("Hem","index.html"),("Integritetspolicy","integritetspolicy.html")])
    + '      <section class="section">\n        <article class="container article-shell content-prose">\n'
    + prose(_pol_blocks)
    + '\n        </article>\n      </section>')

# ====================== BYGG & RENOVERING ==============================
BYGG_CRUMB = [("Hem","index.html"),("Bygg & Renovering","bygg.html")]

page(file="bygg.html", localbiz=True,
  title="Bygg & Renovering i Stockholm – total entreprenad | Geal Entreprenad AB",
  description="Vi bygger och renoverar hela villan: total entreprenad, villarenovering, tillbyggnad, attefallshus och nybyggnad i Stockholm. Begär kostnadsfri offert.",
  h1="Bygg & Renovering i Stockholm",
  crumbs=BYGG_CRUMB,
  cta=("Planerar du ett byggprojekt?","Vi tar hela villan – från tak till total entreprenad. Begär en kostnadsfri offert."),
  body=hero("Bygg & Renovering i Stockholm",
    "Geal Entreprenad AB gör mer än tak. Vi tar hela villan som total entreprenad – renovering, tillbyggnad, attefallshus och nybyggnad – med en kontakt genom hela projektet.",
    BYGG_CRUMB)
    + sec("En byggpartner för hela villan", [
        "Att samordna flera hantverkare själv är krävande. Som total entreprenör håller vi ihop planering, hantverk och tidplan åt dig – oavsett om det gäller en renovering, en tillbyggnad eller ett helt nytt hus.",
        f"Vi kombinerar vår takkompetens med bredare byggarbeten, vilket gör att du kan samordna t.ex. {a('takbyte.html','takbyte')} med fasad, fönster och andra åtgärder i samma projekt."])
    + links_block("Våra byggtjänster", [
        ("byggfirma.html","Byggfirma – total entreprenad","En entreprenör för hela projektet."),
        ("villarenovering.html","Villarenovering","Total- och delrenovering av villa."),
        ("tillbyggnad.html","Tillbyggnad","Bygg ut och få mer yta."),
        ("attefallshus.html","Attefallshus","Nyckelfärdigt upp till 30 m²."),
        ("nybyggnad-villa.html","Nybyggnad / nyckelfärdigt hus","Bygg villa från grunden."),
        ("villatak.html","Tak på villa","Vår ursprungliga specialitet.")], muted=False),
  faq=[
    ("Vad betyder total entreprenad?","Att en entreprenör ansvarar för hela projektet – projektering, hantverk och samordning – så att du bara har en kontakt och ett avtal."),
    ("Gör ni både tak och övrig bygg?","Ja. Vi startade med tak och gör i dag även renovering, tillbyggnad, attefallshus och nybyggnad, ofta i samma projekt."),
    ("Kan jag få ROT-avdrag?","ROT gäller arbete på befintlig bostad (t.ex. renovering). Ny- och tillbyggnad ger normalt inte ROT. Vi reder ut vad som gäller i din offert.")])

page(file="byggfirma.html", service=True, service_type="Total entreprenad / byggfirma",
  title="Byggfirma i Stockholm – total entreprenad för villa | Geal Entreprenad AB",
  description="Byggfirma i Stockholm för total entreprenad: en entreprenör för hela villaprojektet – renovering, tillbyggnad och nybyggnad. Kostnadsfri offert.",
  h1="Byggfirma i Stockholm – total entreprenad",
  crumbs=BYGG_CRUMB+[("Byggfirma","byggfirma.html")],
  cta=("Söker du en byggfirma i Stockholm?","Vi tar helheten som total entreprenör – begär en kostnadsfri offert."),
  body=hero("Byggfirma i Stockholm – total entreprenad",
    "Som byggfirma och total entreprenör tar vi ansvar för hela ditt villaprojekt – en kontakt, ett avtal, en tidplan. Du slipper samordna flera hantverkare själv.",
    BYGG_CRUMB+[("Byggfirma","byggfirma.html")],
    [("#vad","Total entreprenad"),("#ingar","Vad ingår"),("#faq","Vanliga frågor")])
    + sec("Vad är total entreprenad?", [
        "Vid total entreprenad ansvarar vi för både projektering och utförande. Vi tar fram lösning, kalkyl och tidplan, anlitar och samordnar rätt yrkespersoner och levererar ett färdigt resultat enligt avtal.",
        f"Det passar allt från {a('villarenovering.html','villarenovering')} och {a('tillbyggnad.html','tillbyggnad')} till {a('nybyggnad-villa.html','nybyggnad')} – och kan självklart inkludera {a('takbyte.html','tak')}."], sid="vad")
    + sec_split("Vad ingår när du anlitar oss", [
        "Du får en tydlig offert med omfattning, material och tidplan innan start, löpande återkoppling under arbetet och en genomgång vid avslut.",
        "Vi arbetar med F-skatt, ansvarsförsäkring och ID06 och lämnar alltid skriftligt avtal."],
        "Det här ingår", [
        "Projektering och kalkyl.","Bygglovsunderlag vid behov.",
        "Samordning av alla hantverkare.","Materialinköp och logistik.",
        "Löpande avstämning och tidplan.","Slutbesiktning och dokumentation."], sid="ingar")
    + f"""      <section class="section seo-section">
        <div class="container"><div class="tips-box">
          <h3>ROT-avdrag</h3>
          <p>ROT gäller arbetskostnaden vid renovering av befintlig bostad (30 % 2026, max 50 000 kr/person/år). Ren nybyggnad och tillbyggnad ger normalt inte ROT – vi särskiljer detta i offerten. Mer i {a('rot-avdrag-takarbete.html','guiden om ROT-avdrag')}.</p>
        </div></div>
      </section>"""
    + links_block("Relaterat", [
        ("villarenovering.html","Villarenovering","Total- och delrenovering."),
        ("tillbyggnad.html","Tillbyggnad","Utöka boytan."),
        ("nybyggnad-villa.html","Nybyggnad","Bygg nytt från grunden.")]),
  faq=[
    ("Vad kostar en byggfirma / total entreprenad?","Det beror helt på projektets omfattning. Vi erbjuder gratis platsbesök och kostnadsförslag och lämnar ett fast pris efter genomgång."),
    ("Tar ni bygglovet?","Vi hjälper till med bygglovsunderlag och ritningar; själva ansökan görs till kommunen och vi guidar dig genom den."),
    ("Har ni försäkring och F-skatt?","Ja, vi är ett registrerat AB med F-skatt och ansvarsförsäkring, och våra hantverkare är anslutna till ID06.")])

page(file="villarenovering.html", service=True, service_type="Villarenovering",
  title="Villarenovering & totalrenovering i Stockholm | Geal Entreprenad AB",
  description="Villarenovering och totalrenovering i Stockholm: kök, badrum, fasad och helhet med ROT-avdrag. Total entreprenad från en byggpartner. Kostnadsfri offert.",
  h1="Villarenovering i Stockholm",
  crumbs=BYGG_CRUMB+[("Villarenovering","villarenovering.html")],
  cta=("Ska du renovera villan?","Vi tar helheten och drar av ROT direkt på fakturan. Begär offert."),
  body=hero("Villarenovering i Stockholm",
    "Från enstaka rum till totalrenovering – vi renoverar villor i hela Stockholm som total entreprenad. En kontakt för hela projektet och ROT-avdrag på arbetet.",
    BYGG_CRUMB+[("Villarenovering","villarenovering.html")],
    [("#nar","När renovera"),("#ingar","Vad vi gör"),("#faq","Vanliga frågor")])
    + sec("Total- eller delrenovering?", [
        "En delrenovering åtgärdar ett utrymme i taget – kök, badrum eller fasad. En totalrenovering tar helheten och passar när fler delar är slitna eller när du vill förnya planlösning och standard samtidigt.",
        f"Ofta kombineras renovering med {a('takrenovering.html','takrenovering')} eller {a('tillbyggnad.html','tillbyggnad')} – vi samordnar allt i ett projekt."], sid="nar")
    + sec_split("Vad vi renoverar", [
        "Vi hjälper dig planera i rätt ordning och prioritera det som ger mest nytta, med tydlig offert och tidplan.",
        f"Behöver taket åtgärdas passar det ofta att göra samtidigt – se {a('takbyte.html','takbyte')}."],
        "Vanliga renoveringar", [
        "Kök och badrum.","Golv, väggar och ytskikt.",
        "Fasad och fönster.","Ny planlösning.",
        "El och VVS (via behöriga).","Energiåtgärder och isolering."], sid="ingar")
    + rot_box("Villarenovering på befintlig bostad ger normalt rätt till ROT-avdrag på arbetskostnaden.")
    + links_block("Relaterat", [
        ("byggfirma.html","Total entreprenad","En entreprenör för hela renoveringen."),
        ("tillbyggnad.html","Tillbyggnad","Kombinera renovering med mer yta."),
        ("takrenovering.html","Takrenovering","Renovera taket samtidigt.")]),
  faq=[
    ("Kan jag bo kvar under renoveringen?","Ofta ja vid delrenovering. Vid totalrenovering planerar vi etapper eller tidplan så att det påverkar dig så lite som möjligt."),
    ("Får jag ROT-avdrag?","Ja, arbete på din befintliga bostad ger normalt ROT (30 % 2026, max 50 000 kr/person/år). Vi drar av det på fakturan."),
    ("Vad kostar en villarenovering?","Det varierar med omfattning och standard. Vi ger gratis platsbesök och ett fast pris efter genomgång.")])

page(file="tillbyggnad.html", service=True, service_type="Tillbyggnad",
  title="Tillbyggnad av villa i Stockholm – bygga till hus | Geal Entreprenad AB",
  description="Tillbyggnad av villa i Stockholm: bygga till eller bygga ut huset för mer boyta. Vi hjälper med bygglov, projektering och byggnation. Kostnadsfri offert.",
  h1="Tillbyggnad av villa i Stockholm",
  crumbs=BYGG_CRUMB+[("Tillbyggnad","tillbyggnad.html")],
  cta=("Vill du bygga till villan?","Vi hjälper dig från idé och bygglov till färdig tillbyggnad. Begär offert."),
  body=hero("Tillbyggnad av villa i Stockholm",
    "Behöver du mer yta? Vi bygger till och bygger ut villor i Stockholm – från extra rum och uterum till hela våningsplan – med hjälp genom bygglov, projektering och byggnation.",
    BYGG_CRUMB+[("Tillbyggnad","tillbyggnad.html")],
    [("#nar","Möjligheter"),("#bygglov","Bygglov"),("#faq","Vanliga frågor")])
    + sec("Fler sätt att få mer yta", [
        "En tillbyggnad ökar husets boyta permanent. Vanliga projekt är att bygga ut vardagsrummet, lägga till ett extra sovrum, bygga uterum/inglasat eller resa ett helt nytt våningsplan.",
        f"Vill du hellre ha en fristående byggnad kan ett {a('attefallshus.html','attefallshus')} vara ett smidigare alternativ utan bygglov."], sid="nar")
    + sec_split("Bygglov och process", [
        "De flesta tillbyggnader kräver bygglov. Vi hjälper till med ritningar och bygglovsunderlag, och planerar sedan grund, stomme, tak och ytskikt så att tillbyggnaden ansluter tätt och snyggt mot befintligt hus.",
        "En välplanerad anslutning mot tak och fasad är avgörande för att undvika framtida fukt- och läckageproblem."],
        "Så går det till", [
        "Behovsgenomgång och förslag.","Ritning och bygglovsunderlag.",
        "Grund och stomme.","Tak, fasad och tät anslutning.",
        "Invändig komplettering.","Slutbesiktning."], sid="bygglov")
    + f"""      <section class="section seo-section">
        <div class="container"><div class="tips-box">
          <h3>ROT och tillbyggnad</h3>
          <p>Observera: ny- och tillbyggnad ger normalt <strong>inte</strong> ROT-avdrag (det gäller renovering av befintlig bostad). Vi är tydliga med vad som gäller i offerten. Läs mer om {a('bygglov-takbyte.html','bygglov')} och {a('rot-avdrag-takarbete.html','ROT')}.</p>
        </div></div>
      </section>"""
    + links_block("Relaterat", [
        ("attefallshus.html","Attefallshus","Fristående yta utan bygglov."),
        ("byggfirma.html","Total entreprenad","Vi tar hela projektet."),
        ("nybyggnad-villa.html","Nybyggnad","Bygga nytt hus.")]),
  faq=[
    ("Behöver jag bygglov för tillbyggnad?","Oftast ja. Vissa mindre åtgärder (t.ex. attefallstillbyggnad) kan räcka med anmälan. Vi hjälper dig bedöma och du kontrollerar med kommunen."),
    ("Hur mycket får jag bygga till?","Det styrs av detaljplan och tomt. Vi går igenom vad som är möjligt vid ett platsbesök."),
    ("Får jag ROT för tillbyggnad?","Normalt nej – ROT gäller renovering av befintlig bostad, inte tillbyggnad av ny yta.")])

page(file="attefallshus.html", service=True, service_type="Attefallshus",
  title="Attefallshus i Stockholm – nyckelfärdigt upp till 30 m² | Geal Entreprenad AB",
  description="Attefallshus i Stockholm, nyckelfärdigt upp till 30 m² – gäststuga, kontor eller uthyrning. Vi bygger och hjälper med anmälan. Kostnadsfri offert.",
  h1="Attefallshus i Stockholm",
  crumbs=BYGG_CRUMB+[("Attefallshus","attefallshus.html")],
  cta=("Funderar du på ett attefallshus?","Vi bygger nyckelfärdigt och hjälper med anmälan. Begär en kostnadsfri offert."),
  body=hero("Attefallshus i Stockholm",
    "Ett attefallshus ger upp till 30 m² extra – som gäststuga, hemmakontor, förråd eller uthyrning – utan bygglov (men med anmälan). Vi bygger nyckelfärdigt i hela Stockholm.",
    BYGG_CRUMB+[("Attefallshus","attefallshus.html")],
    [("#vad","Om attefallshus"),("#regler","Regler"),("#faq","Vanliga frågor")])
    + sec("Vad är ett attefallshus?", [
        "Attefallshus är en fristående komplementbyggnad på upp till 30 m² som får byggas på de flesta villatomter utan bygglov. Det räcker med en anmälan till kommunen och startbesked innan du börjar.",
        "Populära användningar är gäststuga, hemmakontor, gym, förråd eller ett litet hus för uthyrning. Vi bygger nyckelfärdigt – från grund till inflyttningsklart."], sid="vad")
    + sec_split("Regler i korthet", [
        "Reglerna kan ändras och tolkas av din kommun, men i grunden gäller att attefallshuset är fristående, håller sig inom ytan och avstånden nedan samt att du gjort anmälan och fått startbesked.",
        "Vill du placera huset närmare tomtgräns än 4,5 meter krävs grannens medgivande. Vi hjälper dig med underlaget."],
        "Vanliga krav", [
        "Max 30 m² byggnadsarea.","Nockhöjd max 4,0 meter.",
        "Fristående komplementbyggnad.","Minst 4,5 m till tomtgräns (annars grannmedgivande).",
        "Anmälan + startbesked krävs.","Ej inom vissa kulturmiljöer."], sid="regler")
    + f"""      <section class="section seo-section">
        <div class="container"><div class="tips-box">
          <h3>Bra att veta</h3>
          <p>Ett attefallshus är nybyggnad och ger därför normalt <strong>inte</strong> ROT-avdrag. Ska huset hyras ut eller inredas för boende tillkommer krav – vi går igenom det vid platsbesöket. Se även {a('tillbyggnad.html','tillbyggnad')} om du hellre vill bygga ihop med huset.</p>
        </div></div>
      </section>"""
    + links_block("Relaterat", [
        ("nybyggnad-villa.html","Nybyggnad / nyckelfärdigt","Bygga större hus."),
        ("tillbyggnad.html","Tillbyggnad","Bygg ihop med villan."),
        ("byggfirma.html","Total entreprenad","En entreprenör för allt.")]),
  faq=[
    ("Behöver jag bygglov för attefallshus?","Nej, men du måste göra en anmälan till kommunen och få startbesked innan du börjar bygga."),
    ("Hur stort får ett attefallshus vara?","Upp till 30 m² byggnadsarea och max 4,0 meter nockhöjd, som fristående komplementbyggnad."),
    ("Kan man bo eller hyra ut i ett attefallshus?","Ja, ett attefallshus får inredas för boende (komplementbostadshus) – då tillkommer krav på t.ex. VA och isolering som vi tar höjd för.")])

page(file="nybyggnad-villa.html", service=True, service_type="Nybyggnad villa",
  title="Bygga villa i Stockholm – nyckelfärdigt hus | Geal Entreprenad AB",
  description="Bygga villa i Stockholm – nyckelfärdigt hus från grunden. Vi tar helheten som total entreprenör: projektering, bygglov och byggnation. Kostnadsfri offert.",
  h1="Bygga villa i Stockholm – nyckelfärdigt",
  crumbs=BYGG_CRUMB+[("Nybyggnad","nybyggnad-villa.html")],
  cta=("Vill du bygga nytt hus?","Vi bygger villa från grunden som total entreprenör. Begär en kostnadsfri genomgång."),
  body=hero("Bygga villa i Stockholm – nyckelfärdigt",
    "Drömmer du om ett nytt hus? Vi bygger villor från grunden i Stockholm som total entreprenör – från ritning och bygglov till nyckelfärdigt och inflyttningsklart.",
    BYGG_CRUMB+[("Nybyggnad","nybyggnad-villa.html")],
    [("#nyckelfardigt","Nyckelfärdigt"),("#process","Process"),("#faq","Vanliga frågor")])
    + sec("Nyckelfärdigt hus – vad innebär det?", [
        "Nyckelfärdigt betyder att vi ansvarar för hela kedjan och lämnar över ett färdigt hus som du kan flytta in i. Du slipper samordna arkitekt, hantverkare och leverantörer själv.",
        f"Vi hanterar även taket in i minsta detalj tack vare vår takkompetens – se {a('villatak.html','tak på villa')} – vilket ger en tät och hållbar konstruktion från dag ett."], sid="nyckelfardigt")
    + sec_process("Från ritning till inflyttning", [
        ("Genomgång","Vi går igenom dina önskemål, tomt och budget."),
        ("Ritning & bygglov","Vi tar fram ritningar och bygglovsunderlag."),
        ("Grund & stomme","Grundläggning, stomme och tätt hus."),
        ("Nyckelfärdigt","Ytskikt, installationer och slutbesiktning.")], sid="process")
    + f"""      <section class="section seo-section">
        <div class="container"><div class="tips-box">
          <h3>Bra att veta</h3>
          <p>Nybyggnation ger normalt <strong>inte</strong> ROT-avdrag (ROT gäller renovering av befintlig bostad). Vi ger en tydlig kalkyl så att du ser hela kostnadsbilden. Ett mindre projekt? Se {a('attefallshus.html','attefallshus')}.</p>
        </div></div>
      </section>"""
    + links_block("Relaterat", [
        ("attefallshus.html","Attefallshus","Mindre nybyggnad utan bygglov."),
        ("tillbyggnad.html","Tillbyggnad","Utöka befintligt hus."),
        ("byggfirma.html","Total entreprenad","En kontakt för hela bygget.")]),
  faq=[
    ("Bygger ni nyckelfärdigt?","Ja, vi tar helheten som total entreprenör – från ritning och bygglov till inflyttningsklart hus."),
    ("Hur lång tid tar det att bygga en villa?","Det beror på storlek, bygglovstider och markförhållanden. Vi ger en realistisk tidplan i offerten."),
    ("Får jag ROT för att bygga nytt?","Nej, ROT gäller inte nybyggnation. Det gäller renovering och underhåll av befintlig bostad.")])

# ---- Tak-artiklar (near-miss från Keyword Planner) ----
article("mala-plattak.html",
  "Måla plåttak – så gör du, kostnad och när det lönar sig | Geal Entreprenad AB",
  "Måla plåttak: när det lönar sig, hur det går till, vilken färg och vad det kostar. Guide från takläggare i Stockholm.",
  "Måla plåttak – guide",
  "Att måla om plåttaket ger nytt skydd och fräschare uttryck till lägre kostnad än ett byte. Här är när det lönar sig och hur det går till.",
  [("p","Ett plåttak som börjat tappa färg eller fått ytrost kan ofta målas om i stället för att bytas – förutsatt att grundkonstruktionen är hel. Rätt utfört förlänger målningen takets liv med många år."),
   ("h2","När lönar det sig att måla plåttaket?"),
   ("ul",["Ytan är matt, flagnad eller har begynnande rost.","Konstruktionen och infästningarna är hela.",
          "Inga större genomrostningar eller läckage.","Du vill fräscha upp utan ett fullt takbyte."]),
   ("h2","Så går det till"),
   ("ol",["Tvätt och borttagning av löst material och mossa.","Skrapning och rostskydd där det behövs.",
          "Grundfärg anpassad för plåt.","Täckmålning i två skikt."]),
   ("p",f"Är rosten utbredd eller taket uttjänt är det bättre att byta – se {a('plattak.html','plåttak')}. Behöver taket först rengöras, läs om {a('taktvatt.html','taktvätt')}. Vår tjänst för själva målningen: {a('takmalning.html','takmålning')}."),
   ("tips","Måla inte över rost eller smuts – förbehandlingen avgör hur länge resultatet håller."),
   ("cta",("Vill du måla om plåttaket?","Vi bedömer skicket och ger gratis platsbesök och kostnadsförslag."))],
  [("takmalning.html","Takmålning","Vår tjänst för målning av plåttak."),
   ("plattak.html","Plåttak","Nytt plåttak när målning inte räcker."),
   ("taktvatt.html","Taktvätt","Rengöring inför målning.")],
  faq=[("Hur ofta behöver ett plåttak målas om?","Med rätt förbehandling håller en ommålning normalt 10–15 år beroende på exponering."),
       ("Ger takmålning ROT-avdrag?","Ja, arbetskostnaden för att måla plåttak på villa ger normalt ROT-avdrag.")],
  badge="Tak", read="4 min")

article("falsat-plattak.html",
  "Falsat plåttak & bandtäckning – guide och för- och nackdelar | Geal Entreprenad AB",
  "Falsat plåttak (bandtäckning): hur det fungerar, för- och nackdelar, livslängd och när det passar din villa. Guide från takläggare i Stockholm.",
  "Falsat plåttak & bandtäckning",
  "Falsat plåttak – ofta kallat bandtäckning – är ett klassiskt, hållbart plåttak som passar även låga taklutningar. Här är hur det fungerar och när det passar.",
  [("p","Bandtäckning innebär att plåten läggs i banor som falsas ihop i upphöjda skarvar (ståndfalsar). Det ger ett tätt, rent uttryck och fungerar där tegel- och betongpannor inte passar."),
   ("h2","Fördelar och nackdelar"),
   ("ul",["+ Låg vikt och lång livslängd (ofta 40–50 år).","+ Fungerar på låga taklutningar.",
          "+ Rent, tidlöst uttryck.","– Kräver skickligt plåtslageri för täta falsar.",
          "– Högre hantverksmoment än pannor."]),
   ("h2","När passar falsat plåttak?"),
   ("p",f"Det passar villor med lägre lutning, äldre hus där uttrycket ska bevaras, och där man vill ha ett underhållssnålt tak. Jämför material i {a('tegel-betong-plattak.html','tegel vs betong vs plåt')} och se livslängd i {a('takmaterial-livslangd.html','livslängd per takmaterial')}."),
   ("p",f"Vill du installera eller renovera ett falsat plåttak hjälper vi dig – se {a('plattak.html','plåttak')}. Kan målas om vid behov, se {a('mala-plattak.html','måla plåttak')}."),
   ("tips","Täthet i falsar och detaljer runt genomföringar är avgörande – låt ett erfaret plåtslageri utföra arbetet.")],
  [("plattak.html","Plåttak","Vår tjänst för plåttak och bandtäckning."),
   ("tegel-betong-plattak.html","Jämför takmaterial","Tegel vs betong vs plåt."),
   ("mala-plattak.html","Måla plåttak","Underhåll av plåttak.")],
  faq=[("Vad är skillnaden mellan bandtäckning och plåtpannor?","Bandtäckning läggs i hela banor som falsas ihop och ger ett sömlöst uttryck, medan plåtpannor efterliknar tegel i moduler. Bandtäckning passar bättre på låga lutningar."),
       ("Hur länge håller ett falsat plåttak?","Ofta 40–50 år eller mer med rätt underhåll och eventuell ommålning.")],
  badge="Tak", read="5 min")

# ====================== TACK (form success) ============================
page(file="tack.html", no_cta=True, noindex=True, nolist=True,
  title="Tack för din förfrågan | Geal Entreprenad AB",
  description="Tack! Vi har tagit emot din förfrågan och återkommer så snart vi kan.",
  h1="Tack för din förfrågan!",
  crumbs=[("Hem","index.html"),("Tack","tack.html")],
  body=hero("Tack för din förfrågan!",
    "Vi har tagit emot ditt meddelande och återkommer så snart vi kan, oftast inom 24 timmar. Behöver du nå oss direkt är du välkommen att ringa.",
    [("Hem","index.html"),("Tack","tack.html")])
    + f"""      <section class="section seo-section">
        <div class="container">
          <div class="hero-actions">
            <a class="btn btn-primary" href="tel:{PHONE_T}">Ring {PHONE_D}</a>
            <a class="btn btn-secondary" href="index.html">Till startsidan</a>
          </div>
        </div>
      </section>""")

# ====================== 404 =============================================
page(file="404.html", no_cta=True, noindex=True, nolist=True,
  title="Sidan hittades inte (404) | Geal Entreprenad AB",
  description="Sidan kunde inte hittas. Gå till startsidan eller våra tjänster för takbyte, takrenovering och takbesiktning i Stockholm.",
  h1="Sidan hittades inte",
  crumbs=[("Hem","index.html"),("404","404.html")],
  body=hero("Sidan hittades inte (404)",
    "Sidan du letade efter finns inte längre eller har flyttat. Använd länkarna nedan så hittar du rätt.",
    [("Hem","index.html"),("404","404.html")])
    + links_block("Populära sidor", [
        ("index.html","Till startsidan","Takläggare i Sundbyberg och Stockholm."),
        ("tjanster.html","Våra tjänster","Takbyte, renovering, besiktning m.m."),
        ("omraden.html","Områden","Se var vi arbetar."),
        ("artiklar.html","Artiklar","Guider om tak och takarbete."),
        ("faq.html","Vanliga frågor","Svar på det vanligaste."),
        ("kontakt.html","Kontakt","Begär offert eller ställ en fråga.")], muted=False))

# ====================== WRITE FILES + SITEMAP =============================
# Existing hand-maintained pages (regenereras ej men ska med i sitemap)
STATIC_PAGES = ["index.html","tjanster.html","om-oss.html","kontakt.html",
                "artiklar.html"]

def main():
    written = []
    for p in PAGES:
        html = render(p)
        with open(os.path.join(ROOT, p["file"]), "w", encoding="utf-8") as f:
            f.write(html)
        written.append(p["file"])
    # sitemap.xml (exclude noindex/nolist pages such as 404)
    urls = STATIC_PAGES + [p["file"] for p in PAGES if not p.get("nolist")]
    # dedupe, keep order
    seen=set(); ordered=[u for u in urls if not (u in seen or seen.add(u))]
    def loc(u):
        u = "" if u=="index.html" else u
        return f"{DOMAIN}/{u}"
    items = "\n".join(
        f"  <url>\n    <loc>{loc(u)}</loc>\n    <lastmod>{TODAY}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n    <priority>{'1.0' if u=='index.html' else '0.8'}</priority>\n  </url>"
        for u in ordered)
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + items + "\n</urlset>\n")
    with open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8") as f:
        f.write(sitemap)
    # robots.txt
    robots = ("User-agent: *\nAllow: /\n\n"
              f"Sitemap: {DOMAIN}/sitemap.xml\n")
    with open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8") as f:
        f.write(robots)
    print(f"Genererade {len(written)} sidor.")
    print(f"Sitemap: {len(ordered)} URL:er. robots.txt skriven.")
    for w in written: print("  +", w)

if __name__ == "__main__":
    main()
