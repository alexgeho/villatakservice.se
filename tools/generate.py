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
import os, re, json, datetime

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
GEO_LAT = "59.3328"
GEO_LON = "17.9514"
IMG     = DOMAIN + "/assets/images/1.webp"
TODAY   = "2026-09-06"                          # stabilt datePublished för artiklar
BUILD_DATE = datetime.date.today().isoformat()  # dynamisk sitemap-lastmod (freshness)
ORGNR   = "559303-7566"
VATNR   = "SE559303756601"

AREAS = ["Sundbyberg","Solna","Bromma","Spånga","Sollentuna",
         "Järfälla","Täby","Danderyd","Lidingö","Nacka"]
# Resten av Storstockholm (2026-10-08) – innehåll i tools/omraden_stockholm.py.
from omraden_stockholm import (AREAS_NEW, STOCKHOLM_STAD, NEIGHBORS_NEW,
    NEIGHBORS_ADD, LOC_NEW, LOC_EXTRA_NEW, ORT_IMG_NEW)
AREAS = AREAS + AREAS_NEW
# Norrtälje, Södertälje, Sigtuna (2026-10-25, ägaren bekräftar uppdrag där) – tools/omraden_extra.py.
from omraden_extra import (AREAS_X, NEIGHBORS_X, NEIGHBORS_ADD_X, LOC_X, LOC_EXTRA_X,
    ORT_SEO_X, ORT_SRC_X)
AREAS = AREAS + AREAS_X
# Innerstaden (v30, 2026-10-27): Kungsholmen, Södermalm, Vasastan, Östermalm – tools/omraden_v30.py.
from omraden_v30 import (AREAS_V30, NEIGHBORS_V30, NEIGHBORS_ADD_V30, LOC_V30, LOC_EXTRA_V30,
    ORT_SEO_V30, ORT_SRC_V30, ORT_HERO_ALT_V30, ORT_IMG3_V30, ORT_TRUST_V30)
AREAS = AREAS + AREAS_V30
STOCKHOLM_STAD = STOCKHOLM_STAD + AREAS_V30

# Dalarna: Geal Entreprenad AB samordnar/förmedlar takprojekt och utför via lokal
# samarbetspartner på plats i Dalarna. Ingen egen adress i regionen anges.
DALARNA_AREAS = ["Borlänge","Falun","Ludvika","Avesta","Hedemora",
                 "Säter","Mora","Leksand","Rättvik","Smedjebacken"]

# Geografiska grannar för "Närliggande områden". Tidigare länkade varje ortsida
# till de tre FÖRSTA orterna i listan, så Sundbyberg/Solna/Bromma fick ~74 inlänkar
# och t.ex. Täby/Nacka/Mora bara 1–2 (→ "Discovered – not indexed").
NEIGHBORS = {
  "Sundbyberg": ["Solna","Bromma","Spånga","Järfälla"],
  "Solna":      ["Sundbyberg","Bromma","Danderyd","Sollentuna"],
  "Bromma":     ["Sundbyberg","Spånga","Solna","Järfälla"],
  "Spånga":     ["Bromma","Järfälla","Sundbyberg","Sollentuna"],
  "Sollentuna": ["Järfälla","Täby","Danderyd","Solna"],
  "Järfälla":   ["Spånga","Sollentuna","Bromma","Sundbyberg"],
  "Täby":       ["Danderyd","Sollentuna","Lidingö","Solna"],
  "Danderyd":   ["Täby","Solna","Lidingö","Sollentuna"],
  "Lidingö":    ["Danderyd","Nacka","Täby","Solna"],
  "Nacka":      ["Lidingö","Danderyd","Täby","Solna"],
  "Borlänge":   ["Falun","Säter","Ludvika","Smedjebacken"],
  "Falun":      ["Borlänge","Rättvik","Säter","Leksand"],
  "Ludvika":    ["Smedjebacken","Borlänge","Säter"],
  "Avesta":     ["Hedemora","Säter","Borlänge"],
  "Hedemora":   ["Avesta","Säter","Borlänge"],
  "Säter":      ["Hedemora","Borlänge","Falun","Avesta"],
  "Mora":       ["Rättvik","Leksand","Falun"],
  "Leksand":    ["Rättvik","Mora","Falun","Borlänge"],
  "Rättvik":    ["Leksand","Mora","Falun"],
  "Smedjebacken": ["Ludvika","Borlänge","Säter"],
}
NEIGHBORS.update(NEIGHBORS_NEW)
NEIGHBORS.update(NEIGHBORS_X)
NEIGHBORS.update(NEIGHBORS_V30)
for _o, _add in list(NEIGHBORS_ADD.items()) + list(NEIGHBORS_ADD_X.items()) + list(NEIGHBORS_ADD_V30.items()):
    NEIGHBORS[_o] = NEIGHBORS[_o] + [x for x in _add if x not in NEIGHBORS[_o]]

def slug(name):
    return (name.lower().replace("ä","a").replace("å","a").replace("ö","o")
            .replace(" ","-"))

# Takrenovering per ort (2026-10-25): Keyword Planner "takrenovering <ort>" 10–100/mån.
# Egen lång sida per ort (takrenovering-<slug>.html); innehåll + källor i tools/takreno_orter.py.
from takreno_orter import TRP
TRP_ORTER = ["Bromma","Solna","Nacka","Täby","Danderyd","Lidingö","Huddinge","Järfälla",
             "Sollentuna","Vallentuna","Upplands Väsby","Värmdö","Tyresö","Haninge",
             "Enskede","Älvsjö","Norrtälje","Södertälje"]
# v8 (2026-10-25): orter med spår "<10" men många småhus; läggs till när innehållet finns i TRP.
TRP_ORTER += [o for o in ["Österåker", "Ekerö", "Botkyrka", "Sigtuna", "Hässelby", "Spånga"] if o in TRP]
# v29 (2026-10-27): resterande stadsdelar (spår "<10"); tre bilder per sida.
TRP_ORTER += [o for o in ["Farsta", "Hägersten", "Kista", "Kungsholmen", "Skärholmen", "Sundbyberg",
                          "Södermalm", "Vasastan", "Vällingby", "Östermalm"] if o in TRP]
TRP_FILES = {o: f"takrenovering-{slug(o)}.html" for o in TRP_ORTER}
TRP_NEIGHBORS = {
  "Bromma": ["Solna","Älvsjö","Järfälla"], "Solna": ["Bromma","Danderyd","Sollentuna"],
  "Nacka": ["Värmdö","Tyresö","Lidingö"], "Täby": ["Danderyd","Vallentuna","Sollentuna"],
  "Danderyd": ["Täby","Lidingö","Solna"], "Lidingö": ["Danderyd","Nacka","Täby"],
  "Huddinge": ["Älvsjö","Haninge","Södertälje"], "Järfälla": ["Sollentuna","Upplands Väsby","Bromma"],
  "Sollentuna": ["Järfälla","Täby","Upplands Väsby"], "Vallentuna": ["Täby","Upplands Väsby","Norrtälje"],
  "Upplands Väsby": ["Sollentuna","Vallentuna","Järfälla"], "Värmdö": ["Nacka","Tyresö","Haninge"],
  "Tyresö": ["Haninge","Nacka","Huddinge"], "Haninge": ["Tyresö","Huddinge","Värmdö"],
  "Enskede": ["Älvsjö","Huddinge","Nacka"], "Älvsjö": ["Enskede","Huddinge","Bromma"],
  "Norrtälje": ["Vallentuna","Täby","Upplands Väsby"], "Södertälje": ["Huddinge","Älvsjö","Haninge"],
  # v8
  "Österåker": ["Vallentuna","Täby","Norrtälje"], "Ekerö": ["Bromma","Hässelby","Spånga"],
  "Botkyrka": ["Huddinge","Södertälje","Älvsjö"], "Sigtuna": ["Upplands Väsby","Vallentuna","Sollentuna"],
  "Hässelby": ["Spånga","Bromma","Järfälla"], "Spånga": ["Hässelby","Bromma","Sollentuna"],
  # v29
  "Farsta": ["Enskede","Huddinge","Tyresö"], "Hägersten": ["Älvsjö","Skärholmen","Bromma"],
  "Kista": ["Spånga","Sollentuna","Järfälla"], "Kungsholmen": ["Vasastan","Bromma","Solna"],
  "Skärholmen": ["Hägersten","Botkyrka","Huddinge"], "Sundbyberg": ["Solna","Bromma","Spånga"],
  "Södermalm": ["Enskede","Hägersten","Nacka"], "Vasastan": ["Östermalm","Kungsholmen","Solna"],
  "Vällingby": ["Hässelby","Spånga","Bromma"], "Östermalm": ["Vasastan","Lidingö","Danderyd"],
}
TRP_NEIGHBORS = {o: [n for n in v if n in TRP] for o, v in TRP_NEIGHBORS.items()}
# Bilder (tools/gen_images_flux.py): <sida>-1 = hero, <sida>-2 = i innehållet.
# Alt-texten beskriver motivet – aldrig som eget utfört projekt.
TRP_IMG_ALT = {
 "Bromma": ("Putsad villa med brant tegeltak och skorsten i en trädgårdsstad i Bromma", "Takfall med svarta betongpannor och vinkelränna"),
 "Solna": ("Mindre putsad villa med valmat tegeltak i Råsunda", "Radhustak med betongpannor, skorstenar och takfönster"),
 "Nacka": ("Sekelskiftesvilla i trä med rött plåttak på en klippa vid vattnet i Nacka", "Villa i trädgård med ställning vid taket"),
 "Täby": ("Villa med bruna betongpannor och träfasad i Täby", "Radhuslänga med mörka betongpannor och takfönster"),
 "Danderyd": ("Stor villa med brant tegeltak, takkupor och hög skorsten i Djursholm", "Svarta betongpannor med nockpannor längs taket"),
 "Lidingö": ("Sekelskiftesvilla i trä med glasveranda och tegeltak på Lidingö", "Villa med ställning runt taket under renovering"),
 "Huddinge": ("Gul trävilla med tegeltak och snickarglädje i Huddinge", "Kedjehus med mörka takpannor vid skogskanten i Huddinge"),
 "Järfälla": ("Radhus från 1970-talet med bruna betongpannor i Järfälla", "Takfot med betongpannor, hängränna och stuprör"),
 "Sollentuna": ("Tegelvilla med grå betongpannor bland höga tallar i Sollentuna", "Barr och mossa i hängrännan på ett tak med betongpannor"),
 "Vallentuna": ("Villa med röda takpannor i Vallentuna", "Faluröd lada med plåttak i odlingslandskapet kring Vallentuna"),
 "Upplands Väsby": ("Villagata med likartade hus och mörka tak i Upplands Väsby", "Takfot med takpannor, hängränna och stuprör"),
 "Värmdö": ("Permanentat fritidshus med plåttak i skogen på Värmdö", "Hus på en klippa vid havet i Värmdös skärgård"),
 "Tyresö": ("Rött fritidshus med tillbyggd flygel och två takhöjder vid en vik i Tyresö", "Villa med mossa på taket under höga granar i Tyresö"),
 "Haninge": ("Sekelskiftesvilla med snickarglädje och rött plåttak vid en vik i skärgården kring Dalarö", "Villa med mörka takpannor och träfasad bland björkar i Haninge"),
 "Enskede": ("Trähus med brant tegeltak och staket i Gamla Enskede", "Svart betongpannetak runt en takkupa"),
 "Älvsjö": ("Trävilla med tegeltak och glasveranda i Älvsjö", "Svart betongpannetak vid skorstenen efter renovering"),
 "Norrtälje": ("Rött trähus med svart tak på klipporna vid vattnet i Roslagen", "Timrat hus med rött tak"),
 "Södertälje": ("Putsad villa med tegeltak i en sluttning ovanför en sjö i Södertälje", "Villa med grå takpannor vid skogskanten i Södertälje"),
}
# v8: nya orters alt-texter ligger i TRP[ort]["img"] (samma schema som PAGES_TJ).
for _o, _t in TRP.items():
    if "img" in _t:
        TRP_IMG_ALT.setdefault(_o, (_t["img"][0][0], _t["img"][1][0]))
ORT_HERO_ALT = {
 "Norrtälje": ("Faluröd gård med tegeltak i odlingslandskapet kring Norrtälje", "Röda trähus längs en stenig strand i Roslagen"),
 "Södertälje": ("Rött trähus med svart plåttak på landet i Järna", "Tegelvilla med mörka betongpannor i Södertälje"),
 "Sigtuna": ("Låga trähus med tegeltak längs en smal gata i Sigtuna", "Villor med bruna takpannor i Märsta"),
}

def trp_list_html(title, muted=False, sid=""):
    # Lista "Takrenovering per område" – två kolumner (area-columns), staplas på mobil.
    names = sorted(TRP_ORTER, key=lambda n: n.replace("Ä","A~").replace("Ö","O~"))
    half = (len(names) + 1) // 2
    cols = "\n".join("              <ul class=\"area-list\">\n" + "\n".join(
        f'                <li><a href="{TRP_FILES[n]}">Takrenovering i {n}</a></li>' for n in part)
        + "\n              </ul>" for part in (names[:half], names[half:]))
    cls = "section section-muted seo-section" if muted else "section seo-section"
    idattr = f' id="{sid}"' if sid else ""
    return f"""      <section class="{cls}"{idattr}>
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">{title}</h2>
            <div class="area-columns">
{cols}
            </div>
          </div>
        </div>
      </section>"""

# ---- shared markup --------------------------------------------------------
def a(href, text):
    return f'<a class="text-link" href="{href}">{text}</a>'

# Inline Consent Mode v2 default (DENIED) – körs i <head> FÖRE main.js.
# Future-proof för GTM; main.js gör bara consent-update efter samtycke.
CONSENT_INLINE = """    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      window.gtag = gtag;
      gtag('consent','default',{
        ad_storage:'denied', ad_user_data:'denied', ad_personalization:'denied',
        analytics_storage:'denied', functionality_storage:'granted',
        security_storage:'granted', wait_for_update:500
      });
      window.__vtsConsentDefault = true;
    </script>"""

NAV = """      <div class="container header-inner">
        <a class="logo" href="/">Geal Entreprenad AB</a>
        <nav class="site-nav" id="site-nav" aria-label="Huvudnavigation">
          <ul>
            <li><a data-nav href="/">Hem</a></li>
            <li><a data-nav href="tjanster.html">Tjänster</a></li>
            <li><a data-nav href="bygg.html">Bygg</a></li>
            <li><a data-nav href="omraden.html">Områden</a></li>
            <li><a data-nav href="artiklar.html">Artiklar</a></li>
            <li><a data-nav href="om-oss.html">Om oss</a></li>
            <li><a data-nav href="kontakt.html">Kontakt</a></li>
            <li><a data-nav href="sok.html">Sök</a></li>
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
            <li><a href="badrumsrenovering.html">Badrumsrenovering</a></li>
            <li><a href="koksrenovering.html">Köksrenovering</a></li>
            <li><a href="malare.html">Målare</a></li>
            <li><a href="snickare.html">Snickare</a></li>
            <li><a href="golvlaggning.html">Golvläggning</a></li>
            <li><a href="fasadrenovering.html">Fasadrenovering</a></li>
            <li><a href="fonsterbyte.html">Fönsterbyte</a></li>
            <li><a href="platslagare.html">Plåtslagare</a></li>
            <li><a href="bygg.html">Bygg &amp; Renovering</a></li>
          </ul>
        </div>
        <div>
          <h3>Områden</h3>
          <ul>
            <li><a href="taklaggare-sundbyberg.html">Sundbyberg</a></li>
            <li><a href="taklaggare-solna.html">Solna</a></li>
            <li><a href="taklaggare-bromma.html">Bromma</a></li>
            <li><a href="dalarna.html">Dalarna</a></li>
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
        &copy; <span data-year>2026</span> {BRAND} &middot; Org.nr {ORGNR} &middot;
        <a href="sok.html">Sök</a> &middot;
        <a href="integritetspolicy.html">Integritetspolicy</a> &middot;
        <a href="villkor.html">Villkor</a> &middot;
        <a href="faq.html">Vanliga frågor</a>. Alla rättigheter förbehållna.
      </div>
    </footer>"""

def local_business_schema():
    return {
        "@context":"https://schema.org","@type":"RoofingContractor",
        "@id":DOMAIN+"/#foretag","name":BRAND,"image":IMG,"url":DOMAIN+"/","telephone":PHONE_T,
        "email":EMAIL,"priceRange":"$$",
        "identifier":ORGNR,"vatID":VATNR,
        "address":{"@type":"PostalAddress","streetAddress":STREET,
            "postalCode":ZIP,"addressLocality":CITY,
            "addressRegion":"Stockholms län","addressCountry":"SE"},
        "geo":{"@type":"GeoCoordinates","latitude":GEO_LAT,"longitude":GEO_LON},
        "areaServed":[{"@type":"City","name":n} for n in ["Stockholm"]+AREAS],
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification",
            "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],
            "opens":"08:00","closes":"17:00"}]
    }

def breadcrumb_schema(crumbs):
    return {"@context":"https://schema.org","@type":"BreadcrumbList",
        "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,
            "item":DOMAIN+"/"+("" if u in ("/","index.html") else u)} for i,(n,u) in enumerate(crumbs)]}

def faq_schema(faq):
    return {"@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":q,
            "acceptedAnswer":{"@type":"Answer","text":re.sub(r"<[^>]+>","",x)}} for q,x in faq]}

def article_schema(p):
    return {"@context":"https://schema.org","@type":"Article",
        "headline":p["h1"],"image":IMG,"datePublished":TODAY,"dateModified":TODAY,
        "author":{"@type":"Organization","name":BRAND},
        "publisher":{"@type":"Organization","name":BRAND,
            "logo":{"@type":"ImageObject","url":IMG}},
        "mainEntityOfPage":DOMAIN+"/"+p["file"]}

def service_schema(p):
    areas = p.get("area_served") or ["Stockholm"]+AREAS
    return {"@context":"https://schema.org","@type":"Service",
        "serviceType":p.get("service_type",p["h1"]),
        "provider":{"@type":"RoofingContractor","@id":DOMAIN+"/#foretag","name":BRAND,"url":DOMAIN+"/"},
        "areaServed":[{"@type":"City","name":n} for n in areas],
        "name":p["h1"],"description":p["description"]}

def howto_schema(p):
    name, steps = p["howto"]
    return {"@context":"https://schema.org","@type":"HowTo","name":name,
        "step":[{"@type":"HowToStep","position":i+1,"name":h,"text":t}
                for i,(h,t) in enumerate(steps)]}

def jsonld(obj):
    return ('    <script type="application/ld+json">\n' +
            json.dumps(obj, ensure_ascii=False, indent=6) + "\n    </script>")

def _asset_version(rel):
    import hashlib
    with open(os.path.join(ROOT, rel), "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()[:8]

# CSS/JS cachas 1 år (.htaccess) – versionera URL:en så en deploy syns direkt.
CSS_URL = "assets/css/style.css?v=" + _asset_version("assets/css/style.css")
JS_URL  = "assets/js/main.js?v=" + _asset_version("assets/js/main.js")

def short_title(t):
    # Google kortar vid ~60 tecken – offra varumärkessuffixet först.
    return t.replace(" | Geal Entreprenad AB", "") if len(t) > 60 else t

def render(p):
    robots_meta = '\n    <meta name="robots" content="noindex, follow" />' if p.get("noindex") else ""
    schemas = [local_business_schema() if p.get("localbiz") else None,
               breadcrumb_schema(p["crumbs"]),
               faq_schema(p["faq"]) if p.get("faq") else None,
               article_schema(p) if p.get("article") else None,
               service_schema(p) if p.get("service") else None,
               howto_schema(p) if p.get("howto") else None]
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
    # Offert-CTA-mål: standard kontakt.html, men regionsidor (Dalarna) pekar
    # på en enkel offertformulär-sida utan Stockholmsadress/karta.
    contact_url = p.get("contact_url", "kontakt.html")
    cta = p.get("cta", ("Behöver du hjälp med taket?",
        "Kontakta oss så återkommer vi med en tydlig bedömning och offert för ditt tak."))
    cta_html = "" if p.get("no_cta") else f"""
      <section class="section cta-strip">
        <div class="container">
          <h2>{cta[0]}</h2>
          <p>{cta[1]}</p>
          <div class="hero-actions" style="justify-content: center">
            <a class="btn btn-light" href="{contact_url}#form">Få offert</a>
            <a class="btn btn-outline-light" href="tel:{PHONE_T}">Ring oss</a>
          </div>
        </div>
      </section>"""
    return f"""<!doctype html>
<html lang="sv">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{short_title(p['title'])}</title>
    <meta name="description" content="{p['description']}" />
    <link rel="canonical" href="{canon}" />
    <meta name="geo.region" content="{p.get('geo_region','SE-AB')}" />
    <meta name="geo.placename" content="{p.get('geo_placename','Bromma, Stockholm')}" />
    <meta property="og:title" content="{short_title(p['title'])}" />
    <meta property="og:description" content="{p['description']}" />
    <meta property="og:type" content="{p.get('og_type','website')}" />
    <meta property="og:url" content="{canon}" />
    <meta property="og:image" content="{IMG}" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="theme-color" content="#1f2f46" />{robots_meta}
    <link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
    <link rel="stylesheet" href="{CSS_URL}" />
{CONSENT_INLINE}
    <script src="{JS_URL}" defer></script>
{blocks}
  </head>
  <body>
    <a class="skip-link" href="#content">Hoppa till innehåll</a>
    <header class="site-header">
{NAV.replace('href="kontakt.html#form"', f'href="{contact_url}#form"')}
    </header>

    <main id="content">
{p['body']}
{faq_html}{p.get('after_faq', '')}
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
def _img_attrs(name, sizes):
    # src + srcset (1200/640) + verkliga mått från filen.
    from PIL import Image
    fp = os.path.join(ROOT, "assets", "images", name + ".webp")
    if not os.path.exists(fp):  # bild ännu inte genererad (tj_check renderar i minnet)
        return f'src="assets/images/{name}.webp" width="1200" height="800"'
    w, h = Image.open(fp).size
    ss = ""
    if os.path.exists(os.path.join(ROOT, "assets", "images", name + "-640.webp")):
        ss = f' srcset="assets/images/{name}-640.webp 640w, assets/images/{name}.webp {w}w" sizes="{sizes}"'
    return f'src="assets/images/{name}.webp"{ss} width="{w}" height="{h}"'

def hero(h1, lead, crumbs, anchors=None, trust=None, img=None):
    # img=(namn, alt): fotorealistisk illustration bredvid rubriken (hero-grid--page som om-oss).
    if img:
        return _hero_img(h1, lead, crumbs, anchors, trust, img)
    # trust: egna bockpunkter (t.ex. B2B-sidor där ROT/besök inte gäller).
    trust = trust or ["Gratis besök och kostnadsförslag", "ROT-avdrag direkt på fakturan"]
    trust_li = "\n".join(f"              <li>{t}</li>" for t in trust)
    an = ""
    if anchors:
        links = "\n".join(f'            <a href="{h}">{t}</a>' for h,t in anchors)
        an = f'\n          <div class="anchor-nav" aria-label="Snabblänkar">\n{links}\n          </div>'
    return f"""      <section class="page-hero">
        <div class="container">
          {breadcrumb_html(crumbs)}
          <h1 class="hero-title">{h1}</h1>
          <p class="section-lead">{lead}</p>
          <div class="trust-strip">
            <ul>
{trust_li}
            </ul>
            <a class="btn btn-primary" href="tel:{PHONE_T}">Ring {PHONE_D}</a>
          </div>{an}
        </div>
      </section>"""

def _hero_img(h1, lead, crumbs, anchors, trust, img):
    trust = trust or ["Gratis besök och kostnadsförslag", "ROT-avdrag direkt på fakturan"]
    trust_li = "\n".join(f"                <li>{t}</li>" for t in trust)
    an = ""
    if anchors:
        links = "\n".join(f'              <a href="{h}">{t}</a>' for h,t in anchors)
        an = f'\n            <div class="anchor-nav" aria-label="Snabblänkar">\n{links}\n            </div>'
    return f"""      <section class="page-hero">
        <div class="container hero-grid hero-grid--page">
          <div class="hero-copy">
            {breadcrumb_html(crumbs)}
            <h1 class="hero-title">{h1}</h1>
            <p class="section-lead">{lead}</p>
            <div class="trust-strip">
              <ul>
{trust_li}
              </ul>
              <a class="btn btn-primary" href="tel:{PHONE_T}">Ring {PHONE_D}</a>
            </div>{an}
          </div>
          <figure class="hero-side-visual">
            <img {_img_attrs(img[0], "(max-width: 900px) 100vw, 430px")} alt="{img[1]}" fetchpriority="high" decoding="async" />
          </figure>
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

def sec_process(title, steps, muted=False, sid="", grid="process-grid"):
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
          <div class="{grid}">
{cards}
          </div>
        </div>
      </section>"""

def fig(name, alt, muted=False):
    # AI-genererad illustration (Recraft) – märkt "Illustration", aldrig som eget projektfoto.
    cls = "section section-muted seo-section" if muted else "section seo-section"
    # Bilder med 640-variant (flux-bilderna 2026-10-25) får srcset och verkliga mått.
    if os.path.exists(os.path.join(ROOT, "assets", "images", name + "-640.webp")):
        img = f'<img {_img_attrs(name, "(max-width: 900px) 100vw, 860px")} alt="{alt}" loading="lazy" decoding="async" />'
    else:
        img = f'<img src="assets/images/{name}.webp" alt="{alt}" width="1600" height="1067" loading="lazy" decoding="async" />'
    return f"""      <section class="{cls} figure-section">
        <div class="container">
          <figure class="content-figure">
            {img}
            <figcaption>Illustration</figcaption>
          </figure>
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
              <a class="text-link" href="{href}">{h} &rarr;</a>
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
SVC_CRUMB = [("Hem","/"),("Tjänster","tjanster.html")]

# Tjänster v1–v5: register över tjänstehubbar/ortsidor (tools/tjanster_v1.py).
from tjanster_v1 import TJ, TJ_SERVICES, TJ_HUB, TJ_DISTRICTS

def tj_list_html(title, files, muted=False, sid=""):
    # Kompakt lista med länkar i två kolumner (samma mönster som trp_list_html).
    items = sorted(files, key=lambda f: TJ[f]["h1"].replace("Ä","A~").replace("Ö","O~").replace("Å","A}"))
    half = (len(items) + 1) // 2
    cols = "\n".join("              <ul class=\"area-list\">\n" + "\n".join(
        f'                <li><a href="{f}">{TJ[f]["h1"]}</a></li>' for f in part)
        + "\n              </ul>" for part in (items[:half], items[half:]) if part)
    cls = "section section-muted seo-section" if muted else "section seo-section"
    idattr = f' id="{sid}"' if sid else ""
    return f"""      <section class="{cls}"{idattr}>
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">{title}</h2>
            <div class="area-columns">
{cols}
            </div>
          </div>
        </div>
      </section>"""


page(file="takbyte.html",
  title="Takbyte på villa i Stockholm – fast pris & ROT | Geal Entreprenad AB",
  description="Takbyte på villa i Sundbyberg och Stockholm. Vi byter tegel-, betong- och plåttak med tydlig offert, ROT-avdrag och slutkontroll. Begär kostnadsfri offert.",
  h1="Takbyte på villa i Stockholm",
  service=True, service_type="Takbyte", localbiz=False,
  howto=("Så går ett takbyte till", [
    ("Förfrågan","Du kontaktar oss med kort info om huset och taket."),
    ("Besiktning & offert","Vi bedömer taket och lämnar tydlig offert med material och tidplan."),
    ("Utförande","Vi river, förbereder underlag och lägger nytt tak enligt plan."),
    ("Slutkontroll","Vi går igenom resultatet med dig och dokumenterar arbetet.")]),
  crumbs=SVC_CRUMB+[("Takbyte","takbyte.html")],
  cta=("Dags för takbyte?","Begär en kostnadsfri offert på ditt takbyte – vi bedömer taket och ger tydligt pris med ROT-avdrag."),
  body=hero("Takbyte på villa i Stockholm",
    "Ett takbyte är en av villans större investeringar. Vi byter tegeltak, betongpannor och plåttak med tydlig offert, fast pris och slutbesiktning – i hela Storstockholm.",
    SVC_CRUMB+[("Takbyte","takbyte.html")],
    [("#nar","När behövs takbyte"),("#ingar","Vad ingår"),("#pris","Pris & ROT"),("#faq","Vanliga frågor")])
    + sec("När är det dags för ett takbyte?", [
        "Ett takbyte blir aktuellt när taket nått slutet av sin tekniska livslängd eller när skadorna är så omfattande att löpande reparationer inte längre lönar sig. Vanliga tecken är återkommande läckage, spruckna eller frostskadade pannor, fuktfläckar på vinden och underlagspapp som blivit spröd.",
        f"Är du osäker på om taket behöver bytas eller om en renovering räcker? Börja med en {a('takbesiktning.html','takbesiktning')} – då får du ett tydligt underlag innan du beslutar. Vi går också igenom skillnaden i vår guide {a('takbyte-eller-takrenovering.html','takbyte eller takrenovering')}."], sid="nar")
    + fig("takbyte-lager", "Nytt tak läggs på en villa – ny underlagspapp och läkt överst, nya betongpannor nederst")
    + sec_split("Vad ingår i ett takbyte?", [
        "Vid ett takbyte ser vi till hela takets konstruktion, inte bara ytskiktet. Vi river det gamla taket, kontrollerar och byter läkt och underlagspapp vid behov, och åtgärdar detaljer runt skorsten, takfönster och genomföringar.",
        f"Vi byter även utsatta plåtdetaljer och ser över {a('hangrannor-stupror.html','hängrännor och stuprör')} samt {a('taksakerhet-snorasskydd.html','taksäkerhet som snörasskydd och takstege')} så att taket blir komplett och godkänt."],
        "Det här ingår normalt", [
        "Rivning och bortforsling av befintligt tak.","Ny underlagspapp och kontroll av läkt.",
        "Nytt ytskikt: tegel, betongpannor eller plåt.","Plåtarbeten kring skorsten och genomföringar.",
        "Ny hängränna och stuprör vid behov.","Slutkontroll och genomgång med dig som kund."], sid="ingar")
    + sec_split("Tecken på att taket behöver bytas", [
        "Ett tak slits sällan ut på en gång. Oftast är det underlagspappen under pannorna som tar slut först, och då syns problemen på vinden innan de syns från gatan. Det lönar sig att gå upp på vinden en gång om året, gärna efter ett kraftigt regn eller när snön smälter.",
        "Är pannorna dessutom porösa, frostsprängda eller av en modell som inte längre tillverkas är ett helt nytt tak oftast mer lönsamt än att lägga om."],
        "Vanliga tecken", [
        "Fuktfläckar eller mögel på råsponten.","Dagsljus genom taket från vinden.",
        "Spröd underlagspapp vid takfoten.","Många spruckna eller vittrade pannor.",
        "Återkommande läckage trots reparationer.","Taket är 40–50 år eller äldre."], muted=False, sid="tecken")
    + sec("Takbyte på villor i Stockholm – olika epoker, olika tak", [
        "I trädgårdsstäderna i Bromma, Danderyd och Sundbyberg är många villor från 1920–40-talet med branta tegeltak, kupor och detaljrika vindskivor. Vid takbyte på de husen väljer vi pannor och plåt som behåller husets karaktär och förnyar samtidigt underlaget helt.",
        f"Villorna från 1960–70-talet i bland annat Sollentuna, Spånga, Täby och Järfälla har oftast betongpannor och originalunderlag som nu är 50 år gammalt. Där är takbyte eller takomläggning det vanligaste uppdraget. Funkishus och radhus med låg lutning får ofta nytt plåt- eller {a('papptak.html','papptak')}.",
        f"Vi arbetar i hela Storstockholm – se {a('omraden.html','alla områden')}."], muted=True, sid="epoker")
    + fig("takmaterial-jamforelse", "Takmaterial sida vid sida: tegelpannor, betongpannor, plåt och takpapp")
    + sec("Passa på vid takbytet", [
        f"Ett takbyte är rätt tillfälle att göra allt som annars kräver ställning: byta {a('hangrannor-stupror.html','hängrännor och stuprör')}, montera snörasskydd och takstege, byta takfönster och se över ventilationen vid takfoten.",
        "Funderar du på solceller är det klokt att planera dem samtidigt. Ett nytt tak håller i 40–60 år, medan solcellerna har en livslängd på runt 25–30 år – därför ska de monteras på ett tak som inte behöver bytas inom kort. Infästningarna för solcellerna kan förberedas redan när taket läggs.",
        "Vill du tilläggsisolera vinden kan även det samordnas, men ventilationen måste fungera så att det inte blir fukt under taket."])
    + sec("Bästa tiden för takbyte", [
        "Takbyten görs i Stockholm från tidig vår till sen höst. Huset hålls tätt varje kväll med presenning eller nytt underlag, så ett kort regn är inget problem. Under vintern utför vi främst akuta reparationer.",
        "Våren och sommaren bokas snabbt. Begär besiktning och offert redan under vintern om du vill ha taket klart till sommaren."])
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
    + (tj_list_html("Takbyte per område", TJ_DISTRICTS["takbyte"], muted=True, sid="omraden") if TJ_DISTRICTS.get("takbyte") else "")
    + links_block("Relaterat", [
        ("kalkylator-takbyte.html","Takbyte-kalkylator","Uppskatta priset direkt – area, material och ROT."),
        ("villatak.html","Tak på villa – komplett guide","Allt om tak på villa: material, kostnad och underhåll."),
        ("taklaggare-sundbyberg.html","Takbyte i Sundbyberg","Vi är lokala takläggare i Sundbyberg och närområdet."),
        ("bygglov-takbyte.html","Behövs bygglov för takbyte?","När takbyte kräver bygglov eller anmälan.")]),
  faq=[
    ("Hur lång tid tar ett takbyte på en villa?","De flesta villatakbyten tar ungefär 1–2 veckor beroende på takets storlek, väder och eventuella underliggande skador. Vi ger en preliminär tidplan i offerten."),
    ("Kan jag använda ROT-avdrag för takbyte?","Ja, arbetskostnaden för takbyte på villa ger normalt rätt till ROT-avdrag. Vi drar av det direkt på fakturan. Exakt nivå för 2026 anges i offerten."),
    ("Måste jag byta hela taket eller räcker en renovering?","Det beror på skicket. Om grundkonstruktionen är sund kan en takrenovering räcka. En takbesiktning ger svar innan du beslutar."),
    ("Vilket takmaterial är bäst?","Det beror på husets lutning, stil och budget. Tegel och betong är vanligast, plåt passar låga lutningar. Vi går igenom alternativen med dig."),
    ("Kan man bo kvar i huset under takbytet?","Ja. Huset hålls tätt varje kväll och du kan bo kvar som vanligt under arbetet."),
    ("Ska man byta tak innan man sätter solceller?","Ja, om taket är äldre än 25–30 år. Solcellerna håller länge, och det blir dyrt att ta ner dem för att byta tak senare."),
    ("Behövs bygglov för takbyte?","Normalt inte för villa eller radhus: sedan 1 december 2025 krävs inget bygglov för att byta takmaterial eller kulör på en- och tvåbostadshus. Undantaget är särskilt kulturhistoriskt värdefulla hus och områden. Höjs taket över befintlig nock krävs bygglov.")])

page(file="takrenovering.html",
  title="Takrenovering i Stockholm – takomläggning & reparation | Geal Entreprenad AB",
  description="Takrenovering och takomläggning på villa i Stockholm: ny underlagspapp och läkt, omlagda pannor och tät plåt – utan nytt tak. Gratis besök och ROT.",
  h1="Takrenovering och takomläggning i Stockholm",
  service=True, service_type="Takrenovering", localbiz=False,
  howto=("Så går en takomläggning till", [
    ("Besiktning","Vi kontrollerar pannor, underlagspapp, läkt, råspont och plåt och lämnar en åtgärdsplan."),
    ("Ställning & skydd","Ställning och fallskydd sätts upp, fasad och tomt skyddas."),
    ("Nedplockning","Pannorna plockas ner och sorteras; hela pannor sparas för återläggning."),
    ("Nytt underlag","Ny underlagspapp, ströläkt och bärläkt monteras; skadad råspont byts."),
    ("Återläggning","Pannorna läggs tillbaka och kompletteras med nya där det behövs."),
    ("Plåt & slutkontroll","Plåt runt skorsten, nock och genomföringar görs om och arbetet kontrolleras.")]),
  crumbs=SVC_CRUMB+[("Takrenovering","takrenovering.html")],
  cta=("Behöver taket renoveras?","Vi kommer ut gratis, visar vad som behöver göras och lämnar ett skriftligt kostnadsförslag."),
  body=hero("Takrenovering och takomläggning i Stockholm",
    "Är pannorna fortfarande hela men underlaget slitet? Då kan en takomläggning ge taket 30–40 år till – för en lägre kostnad än ett helt nytt tak. Vi renoverar villatak i hela Storstockholm.",
    SVC_CRUMB+[("Takrenovering","takrenovering.html")],
    [("#nar","När passar det"),("#omlaggning","Takomläggning"),("#ingar","Så går det till"),("#pris","Kostnad & ROT"),("#faq","Vanliga frågor")])
    + sec("När passar takrenovering?", [
        "Takrenovering är rätt när takets bärande delar är sunda men skikten under eller runt pannorna har gjort sitt. Det vanligaste exemplet är ett betong- eller tegeltak från 1960–80-talet där pannorna fortfarande är hela, men där underlagspappen har blivit spröd, läkten har börjat ruttna eller plåten runt skorstenen läcker.",
        "Ytan på taket ser ofta bra ut från gatan. Problemen syns i stället på vinden: fuktfläckar på råsponten, mögellukt, droppmärken på isoleringen eller dagsljus genom taket. Det är tecken på att vatten tar sig förbi pannorna och att underlaget inte längre är tätt.",
        f"Vi hjälper dig välja rätt nivå efter en {a('takbesiktning.html','takbesiktning')}: punktvis reparation, takomläggning eller {a('takbyte.html','takbyte')}. Jämförelsen finns också i guiden {a('takbyte-eller-takrenovering.html','takbyte eller takrenovering')}."], sid="nar")
    + fig("takrenovering-omlaggning", "Takomläggning på villa: pannorna plockade ner, ny underlagspapp och läkt monterad")
    + sec_split("Tecken på att taket behöver renoveras", [
        "Underlagspapp från 60- och 70-talet var ofta tunn och har efter 40–50 år förlorat sin täthet. Pannorna kan ha flera decennier kvar, men utan ett tätt underlag blir taket bara så bra som sitt svagaste skikt.",
        "Vänta inte tills läckaget syns i taket inomhus. Fukt som får verka i flera år kan skada råspont och takstolar, och då blir en renovering snabbt ett byte."],
        "Vanliga tecken", [
        "Fuktfläckar eller mögel på vinden.","Spröd eller trasig underlagspapp vid takfoten.",
        "Sneda, spruckna eller lösa pannor.","Läckage vid skorsten eller takfönster.",
        "Mossa som lyfter pannorna.","Taket är över 40 år och aldrig omlagt."], sid="tecken")
    + sec("Takomläggning – vad innebär det?", [
        "Vid en takomläggning plockar vi ner alla pannor, byter underlagspapp och läkt och lägger sedan tillbaka samma pannor. Trasiga pannor ersätts med nya eller begagnade av samma modell. Resultatet är ett tak med helt nytt tätskikt men med husets ursprungliga karaktär kvar.",
        "Takomläggning lönar sig när pannorna är i gott skick. Betongpannor håller ofta 40–60 år och tegelpannor betydligt längre. Är pannorna däremot porösa, frostsprängda eller av en modell som inte längre tillverkas kan nya pannor vara ett bättre val.",
        "Vid omläggningen passar vi på att åtgärda allt som är svårt att komma åt annars: ventilation av takfoten, infästning av nock, plåtdetaljer, vindskivor och genomföringar."], muted=True, sid="omlaggning")
    + sec_process("Så går takrenoveringen till", [
        ("Besiktning","Vi går igenom pannor, papp, läkt, råspont och plåt och lämnar en skriftlig åtgärdsplan."),
        ("Ställning & skydd","Ställning och fallskydd sätts upp och tomten skyddas."),
        ("Nedplockning","Pannorna plockas ner och hela pannor sparas för återläggning."),
        ("Nytt underlag","Ny underlagspapp och läkt; skadad råspont byts."),
        ("Återläggning","Pannorna läggs tillbaka och kompletteras där det behövs."),
        ("Plåt & kontroll","Plåt runt skorsten, nock och genomföringar görs om och vi gör slutkontroll.")], sid="ingar")
    + sec_split("Mindre reparationer", [
        f"Alla tak behöver inte omläggning. Ofta räcker det att byta några spruckna pannor, laga plåten runt skorstenen eller täta ett takfönster. Vi gör även takreparationer och åtgärder vid akut {a('taklackage.html','takläckage')}.",
        "En liten reparation i tid förhindrar en stor skada senare. Vid besiktningen får du veta vad som är bråttom och vad som kan vänta."],
        "Typiska reparationer", [
        "Byte av enstaka pannor.","Plåtarbeten runt skorsten.",
        "Tätning av takfönster och genomföringar.","Ny nockpanna och nockbruk.",
        "Byte av vindskivor och takfotsbrädor."])
    + sec("Vad kostar en takrenovering?", [
        "Kostnaden styrs av takets storlek och lutning, hur många pannor som kan återanvändas, hur mycket råspont som måste bytas, plåtarbeten och ställningsbehov. Därför kan två villor med samma yta få olika pris.",
        f"Vi publicerar inga fasta priser. Vi kommer ut gratis, tittar på taket och lämnar ett skriftligt kostnadsförslag där varje moment står med. Faktorerna som påverkar priset går vi igenom i {a('vad-kostar-takrenovering.html','vad kostar en takrenovering')}.",
        "Arbetet kan också delas upp i etapper – till exempel den mest utsatta takfallet först och resten året efter."], sid="pris")
    + rot_box("Takrenovering och takomläggning på villa ger ROT-avdrag på arbetskostnaden. Vi gör avdraget direkt på fakturan.")
    + trp_list_html("Takrenovering i ditt område", muted=True, sid="orter")
    + links_block("Relaterat", [
        ("takbyte-eller-takrenovering.html","Takbyte eller takrenovering?","Så väljer du rätt åtgärd för ditt tak."),
        ("vad-kostar-takrenovering.html","Vad kostar en takrenovering?","Vad som påverkar kostnaden."),
        ("takmaterial-livslangd.html","Livslängd per takmaterial","Hur länge pannor och papp håller.")]),
  faq=[
    ("Vad är skillnaden mellan takrenovering och takomläggning?","Takomläggning innebär att befintliga pannor läggs om med ny underlagspapp och läkt. Takrenovering är ett bredare begrepp som även omfattar reparationer av plåt, pannor och enskilda skador."),
    ("Hur länge håller en takomläggning?","Med ny underlagspapp och läkt håller taket normalt 30–40 år till, så länge pannorna är i gott skick."),
    ("Kan man återanvända gamla betongpannor?","Ja, om de är hela och inte porösa. Trasiga pannor ersätts med nya eller begagnade av samma modell."),
    ("Hur vet jag om det räcker med renovering?","En takbesiktning visar om stommen och pannorna är sunda. Är de det räcker ofta renovering, annars rekommenderar vi takbyte."),
    ("Hur lång tid tar en takomläggning?","För en normal villa oftast en till två veckor beroende på storlek, väder och hur mycket råspont som behöver bytas."),
    ("Kan arbetet delas upp i etapper?","Ja, vi kan börja med de mest utsatta delarna och planera resten senare."),
    ("Ger takrenovering ROT-avdrag?","Ja, arbetskostnaden ger ROT-avdrag. Vi gör avdraget direkt på fakturan.")])

page(file="takbesiktning.html",
  title="Besikta tak i Stockholm – takbesiktning av villatak",
  description="Besikta taket före husköp, efter storm eller inför takbyte. Vi kontrollerar pannor, plåt, underlag och vind och dokumenterar med foton. Stockholm.",
  h1="Takbesiktning i Stockholm – besikta taket på villan",
  service=True, service_type="Takbesiktning", localbiz=False,
  crumbs=SVC_CRUMB+[("Takbesiktning","takbesiktning.html")],
  cta=("Vill du besikta taket?","Boka en takbesiktning så får du ett tydligt underlag inför beslut och offert."),
  body=hero("Takbesiktning i Stockholm – besikta taket på villan",
    "Att besikta taket är ofta det bästa första steget. Vi går igenom takets skick, riskpunkter och avvattning och ger dig ett tydligt underlag – innan du beslutar om renovering eller takbyte.",
    SVC_CRUMB+[("Takbesiktning","takbesiktning.html")],
    [("#varfor","Varför besikta"),("#nar","När besikta"),("#ingar","Vad kontrolleras"),("#huskop","Vid husköp"),("#sjalv","Kolla själv"),("#faq","Vanliga frågor")])
    + sec("Varför besiktning av tak lönar sig", [
        "Utan en korrekt bedömning är det svårt att veta om ett problem kräver akut insats eller kan planeras längre fram. Många hör av sig efter att ha sett en missfärgning i undertaket, lösa pannor eller mossa på utsatta ytor.",
        f"En besiktning ger svar på om det är ett isolerat problem eller ett tecken på större belastning – och är ett bra underlag inför {a('takbyte.html','takbyte')} eller {a('takrenovering.html','takrenovering')}."], sid="varfor")
    + fig("takbesiktning-checklista", "Kontrollpunkter vid takbesiktning: nock, skorsten, ränndal, hängrännor, takfönster och takfot")
    + sec_split("Vad kontrolleras vid en takbesiktning?", [
        "Vi gör en samlad bedömning av skick, funktion och rekommenderad åtgärdsnivå, och dokumenterar fynden så att du kan prioritera rätt.",
        f"Vanliga fynd är otäta anslutningar, {a('taklackage.html','takläckage')}, begynnande {a('fuktskada-mogel-vind.html','fuktskador på vinden')} och slitna beslag."],
        "Vi ser bland annat på", [
        "Takytor, pannor och plåtdetaljer.","Anslutningar mot skorsten och genomföringar.",
        "Hängrännor, stuprör och avvattning.","Tecken på fukt i undertak och på vind.",
        "Taksäkerhet och infästningar.","Rekommendation: service, renovering eller byte."], sid="ingar")
    + sec_split("När ska du besikta taket?", [
        "Det bästa tillfället är innan problemen syns inomhus. En besiktning är särskilt värdefull i några lägen:",
        f"Är du osäker på hur gammalt taket är kan du jämföra med normal livslängd för olika material i vår guide om {a('takmaterial-livslangd.html','takmaterial och livslängd')}."],
        "Boka besiktning när", [
        "Du köper eller säljer villa och vill veta takets skick.",
        "Det har stormat eller varit en snötung vinter.",
        "Du ser fuktfläckar i taket, droppar på vinden eller mögellukt.",
        "Du funderar på takbyte eller renovering och vill ha rätt underlag.",
        "Taket närmar sig slutet av sin livslängd.",
        "Det har gått 5–10 år sedan senaste genomgången."], muted=False, sid="nar")
    + sec_process("Så går en takbesiktning till", [
        ("Bokning","Du berättar kort om huset, taket och vad du har sett. Vi bokar en tid som passar."),
        ("Besiktning på plats","Vi går igenom takytan, plåtdetaljer, anslutningar, avvattning och – om det går – vinden."),
        ("Bedömning","Vi dokumenterar fynden med foton och bedömer vad som är akut och vad som kan planeras."),
        ("Rekommendation","Du får en tydlig rekommendation: service, renovering eller takbyte – och offert om du vill.")], muted=True)
    + sec("Vad vi tittar extra på – per takmaterial", [
        f"<strong>Tegel- och betongpannor:</strong> spruckna eller förskjutna pannor, frostskador, lösa nockpannor, mossa och påväxt samt skicket på underlagspappen där den syns. Läs mer om {a('tegel-betong-plattak.html','tegel, betong och plåttak')}.",
        f"<strong>Plåttak:</strong> rost, lösa eller otäta falsar, infästningar och skruvar, färgskikt och skarvar. Se även {a('mala-plattak.html','måla plåttak')} och {a('falsat-plattak.html','falsat plåttak')}.",
        f"<strong>Detaljer på alla tak:</strong> skorstenens beslag och fogar, genomföringar, takfönster, {a('hangrannor-stupror.html','hängrännor och stuprör')} samt taksäkerhet som stegar och snörasskydd."])
    + sec("Besikta taket vid husköp – takbesiktning eller överlåtelsebesiktning?", [
        "Inför ett husköp görs ofta en överlåtelsebesiktning av hela huset. Den är okulär, och taket bedöms då i regel från marken och från vinden. Det räcker för att hitta tydliga brister, men säger mindre om hur länge pannor och underlagspapp håller och vad en åtgärd skulle innebära.",
        "Vill du veta mer om just taket kan du komplettera med en takbesiktning. Då tittar en takläggare närmare på takytan, plåtdetaljerna och underlaget där det syns, och du får besked om taket behöver underhåll, omläggning eller byte inom överskådlig tid.",
        "Var medveten om skillnaden: vi är takläggare, inte oberoende besiktningsmän. Vår bedömning är ett underlag för åtgärd och offert. Behöver du ett formellt protokoll till ett köpeavtal eller en tvist ska du anlita en certifierad besiktningsman."], muted=True, sid="huskop")
    + sec("Efter storm, snötung vinter eller läckage", [
        f"Efter en storm eller en vinter med mycket snö och is är det klokt att besikta taket innan vårregnen. Lösa nockpannor, skadade plåtdetaljer och igensatta rännor upptäcks då innan de orsakar {a('taklackage.html','läckage')}.",
        "Har skadan redan skett dokumenterar vi den med foton och beskriver vad som behöver åtgärdas. Underlaget kan du använda i kontakten med ditt försäkringsbolag – kontrollera alltid med bolaget vad de kräver."])
    + sec_split("Vad händer efter besiktningen?", [
        "Besiktningen slutar med en rekommendation. Den kan peka på någon av tre nivåer – och du bestämmer själv om och när du vill gå vidare.",
        f"ROT-avdraget gäller arbetet med själva åtgärden, till exempel omläggning eller takbyte. Läs mer om {a('rot-avdrag-takarbete.html','ROT-avdrag för takarbete')}."],
        "Vanliga utfall", [
        f"Underhåll: {a('taktvatt.html','taktvätt')}, rensning av rännor eller {a('takmalning.html','takmålning')}.",
        f"{a('takrenovering.html','Takrenovering eller takomläggning')}: nytt underlag, samma pannor.",
        f"{a('takbyte.html','Takbyte')}: nya pannor eller plåt och nytt underlag.",
        f"Osäker på priset? Läs {a('vad-kostar-takbyte.html','vad ett takbyte kostar')}."])
    + sec_split("Kolla taket själv – enkel checklista", [
        "Mellan besiktningarna kan du själv hålla koll på det mesta från marken och från vinden. Gå inte upp på taket själv – ett halt tak är farligt, och trampade pannor kan börja läcka.",
        f"Ser du något av punkterna i listan är det dags att låta en takläggare titta närmare. Läs mer om {a('nar-ska-taket-bytas.html','tecken på att taket behöver bytas')}."],
        "Titta efter", [
        "Pannor som saknas, har spruckit eller glidit (använd gärna kikare).",
        "Mossa och påväxt på de skuggiga takfallen.",
        "Hängrännor som svämmar över eller hänger snett.",
        "Fuktfläckar, mörka partier eller dagsljus på vinden.",
        "Mögellukt eller kondens på vinden efter kalla nätter."], muted=False, sid="sjalv")
    + sec("Takbesiktning i Stockholm och närområdet", [
        f"Vi har kontor i Bromma och besiktar tak i hela Stockholm – bland annat i {a('taklaggare-bromma.html','Bromma')}, {a('taklaggare-sundbyberg.html','Sundbyberg')}, {a('taklaggare-solna.html','Solna')}, {a('taklaggare-sollentuna.html','Sollentuna')}, {a('taklaggare-danderyd.html','Danderyd')}, {a('taklaggare-taby.html','Täby')}, {a('taklaggare-nacka.html','Nacka')}, {a('taklaggare-lidingo.html','Lidingö')} och {a('taklaggare-jarfalla.html','Järfälla')}. Besiktningen är ett bra första steg innan du tar in offerter på {a('takbyte.html','takbyte')} eller {a('takrenovering.html','takrenovering')}.",
        f"Bor du i Dalarna? Där besiktar vi tak via vår lokala partner – se {a('dalarna.html','takbesiktning och takbyte i Dalarna')}."], muted=True)
    + links_block("Relaterat", [
        ("nar-ska-taket-bytas.html","Tecken på att taket behöver bytas","Vanliga signaler att hålla koll på."),
        ("fuktskada-mogel-vind.html","Fuktskada och mögel på vinden","Orsaker, symptom och åtgärder."),
        ("taklaggare-bromma.html","Takbesiktning i Bromma","Lokala takläggare i Bromma och västerort.")]),
  faq=[
    ("Vad kostar en takbesiktning?","Vi erbjuder alltid gratis platsbesök och kostnadsförslag inför ett takprojekt. Kontakta oss så bokar vi en tid som passar."),
    ("Hur ofta bör man besikta taket?","En översiktlig kontroll två gånger per år (vår och höst) är en bra grund. En professionell besiktning är klok vart 5–10:e år eller vid tecken på problem."),
    ("Får jag en rapport?","Ja, du får en tydlig bedömning av skick, riskpunkter och rekommenderad åtgärd som underlag för offert."),
    ("Kan man besikta taket på vintern?","Snötäckta takytor går inte att bedöma ordentligt, men vind, genomföringar och avvattning kan kontrolleras. En fullständig bedömning av takytan görs när taket är snöfritt."),
    ("Är det farligt att kontrollera taket själv?","Ja, gå inte upp på taket själv. Kontrollera i stället från marken, gärna med kikare, och från vinden. Det räcker för att upptäcka de flesta varningstecken."),
    ("Vad är skillnaden mellan takbesiktning och överlåtelsebesiktning?","En överlåtelsebesiktning gäller hela huset inför köp och är okulär – taket bedöms oftast från marken och vinden. En takbesiktning gäller bara taket och ger besked om vilken åtgärd som behövs."),
    ("Gör ni oberoende takbesiktning?","Nej, vi är takläggare och vår bedömning är underlag för åtgärd och offert. Behöver du ett oberoende protokoll, till exempel vid tvist, anlitar du en certifierad besiktningsman."),
    ("Besiktar ni tak i Dalarna?","Ja, via vår lokala partner i Dalarna, bland annat i Borlänge, Falun och Säter.")])

page(file="plattak.html",
  title="Plåttak i Stockholm – nytt plåttak & plåtarbeten | Geal Entreprenad AB",
  description="Plåttak i Stockholm och Sundbyberg: nytt plåttak, bandtäckning och plåtarbeten med fokus på täthet och avvattning. Gratis offert från lokala takläggare.",
  h1="Plåttak i Stockholm",
  service=True, service_type="Plåttak", localbiz=False,
  crumbs=SVC_CRUMB+[("Plåttak","plattak.html")],
  cta=("Funderar du på plåttak?","Vi hjälper dig med nytt plåttak eller plåtarbeten – begär en offert."),
  body=hero("Plåttak i Stockholm",
    "Plåttak är ett populärt val i Stockholm tack vare låg vikt, lång livslängd och rent uttryck. Vi utför nytt plåttak, bandtäckning och plåtdetaljer med precision i skarvar, beslag och avvattning.",
    SVC_CRUMB+[("Plåttak","plattak.html")],
    [("#fordelar","Fördelar"),("#typer","Bandtäckning eller profil"),("#tata","Täta plåttak"),("#pris","Kostnad & ROT"),("#faq","Vanliga frågor")])
    + sec("Fördelar med plåttak", [
        "Plåttak har låg vikt, tål temperaturväxlingar bra och passar även på lägre taklutningar där pannor inte fungerar. Rätt utfört ger det en tät konstruktion som är enkel att underhålla.",
        f"Samtidigt ställer plåtarbeten höga krav på precision – små fel i infästning eller skarvar kan ge läckage eller korrosion över tid. Jämför material i {a('tegel-betong-plattak.html','tegel vs betong vs plåt')}."], sid="fordelar")
    + fig("plattak-falsat", "Svart falsat plåttak på en vit funkisvilla")
    + sec_split("Vad vi gör inom plåttak", [
        "Vi hjälper både dig som vill installera nytt plåttak och fastighetsägare som behöver renovera ett befintligt system. I varje projekt tittar vi på taklutning, avvattning och detaljlösningar.",
        f"Har plåttaket börjat rosta kan {a('takmalning.html','takmålning')} vara ett alternativ när konstruktionen fortfarande är sund."],
        "Vi arbetar med", [
        "Nytt plåttak och bandtäckning (falsat plåt).","Beslag och anslutningar runt genomföringar.",
        "Plåtdetaljer: vindskivor, fotplåt, ståndskivor.","Avvattning och skydd mot korrosion.",
        "Reparation av befintliga plåttak.","Råd om skötsel och underhåll."], sid="ingar")
    + sec("Bandtäckning eller profilplåt?", [
        "Bandtäckning, även kallad falsat plåttak, är den klassiska metoden: långa plåtband som fogas ihop med dubbelfals direkt på råsponten. Den ger ett slätt, stilrent tak, fungerar ner till mycket låga lutningar och passar äldre hus och funkisvillor. Bandtäckning läggs av plåtslagare och tar längre tid, men håller mycket länge.",
        "Profilplåt (till exempel trapetsprofil eller pannprofil) levereras i färdiga skivor som skruvas fast. Den är snabbare att montera och oftast billigare, och passar många villor och komplementbyggnader. Skruvarnas gummibrickor behöver ses över med åren.",
        f"Vilket som passar beror på husets stil, lutning och budget. Mer om den klassiska metoden finns i {a('falsat-plattak.html','falsat plåttak och bandtäckning')}."], muted=True, sid="typer")
    + sec_split("Täta och reparera falsat plåttak", [
        "Äldre falsade plåttak från 1950–70-talet läcker oftast vid falsarna, vid skorstenen och vid genomföringar. Plåten kan vara frisk men falsarna ha öppnat sig av rörelser och frost. Då kan taket tätas genom att falsarna efterfalsas och tätas och skadade partier byts.",
        f"Är plåten frisk men färgen sliten är {a('takmalning.html','takmålning')} ett bra nästa steg efter tätningen. Är plåten genomrostad på flera ställen blir nytt plåttak mer lönsamt."],
        "Vanliga läckagepunkter", [
        "Öppna eller rostiga falsar.","Plåt runt skorsten.",
        "Ventilationshuvar och genomföringar.","Ränndalar och takfot.","Skarvar mot vägg och kupor."], muted=False, sid="tata")
    + sec("Byta från pannor till plåt", [
        "Många väljer att gå från betong- eller tegelpannor till plåt vid takbyte, eftersom plåt är lättare och kräver mindre underhåll. Lägre vikt avlastar takstolarna på äldre hus.",
        f"Sedan 1 december 2025 kräver byte av takmaterial på villa och radhus normalt inget bygglov. Undantaget är hus med skyddsbestämmelser och särskilt värdefulla miljöer – där krävs lov, så stäm av med kommunen – läs mer i {a('bygglov-takbyte.html','bygglov för takbyte')}."], muted=True)
    + sec("Vad kostar ett plåttak?", [
        "Priset beror på takets yta och form, valet mellan bandtäckning och profilplåt, plåtkvalitet och kulör, antal genomföringar och kupor samt ställningsbehov. Bandtäckning kostar mer än profilplåt men har lång livslängd.",
        "Vi publicerar inga fasta priser. Vi kommer ut gratis och lämnar ett skriftligt kostnadsförslag där alternativen står sida vid sida."], sid="pris")
    + rot_box("Arbetskostnaden för plåttak och plåtarbeten på villa ger ROT-avdrag. Vi gör avdraget direkt på fakturan.")
    + links_block("Plåttak i ditt område", [
        ("taklaggare-bromma.html","Bromma","Funkisvillor med låga plåttak."),
        ("taklaggare-danderyd.html","Danderyd","Stora villor med falsad plåt."),
        ("taklaggare-lidingo.html","Lidingö","Havsnära tak och korrosionsskydd."),
        ("taklaggare-nacka.html","Nacka","Kustnära tak i Saltsjöbaden."),
        ("taklaggare-solna.html","Solna","Villatak i Råsunda och Råsta."),
        ("taklaggare-sundbyberg.html","Sundbyberg","Plåtdetaljer på radhus och villor.")], muted=False, sid="orter")
    + links_block("Relaterat", [
        ("falsat-plattak.html","Falsat plåttak & bandtäckning","Klassiskt plåttak för låga lutningar."),
        ("mala-plattak.html","Måla plåttak","Underhåll och nytt ytskydd."),
        ("papptak.html","Papptak","Byta eller lägga nytt papptak."),
        ("takmaterial-livslangd.html","Livslängd per takmaterial","Så länge håller plåt, tegel och betong."),
        ("taklaggare-lidingo.html","Plåttak på Lidingö","Salt havsluft ställer extra krav på plåt.")]),
  faq=[
    ("Hur länge håller ett plåttak?","Ett väl utfört plåttak håller ofta 40–50 år eller mer med rätt underhåll och eventuell ommålning."),
    ("Kan man lägga plåttak på låg lutning?","Ja, plåt (särskilt bandtäckning) fungerar på lägre lutningar där tegel- och betongpannor inte är lämpliga."),
    ("Är plåttak bullrigt vid regn?","Med korrekt underlag och isolering är ljudnivån normalt inget problem i bostadshus."),
    ("Kan man täta ett gammalt falsat plåttak?","Ja, om plåten är frisk kan falsarna efterfalsas och tätas och skadade partier bytas. Därefter kan taket målas."),
    ("Vad är skillnaden mellan bandtäckning och profilplåt?","Bandtäckning är falsade plåtband som läggs på plats av plåtslagare. Profilplåt är färdiga skivor som skruvas fast – snabbare och oftast billigare."),
    ("Behövs bygglov för att byta till plåttak?","Normalt inte för villa eller radhus: sedan 1 december 2025 krävs inget bygglov för att byta takmaterial eller kulör på en- och tvåbostadshus. Undantaget är särskilt kulturhistoriskt värdefulla hus och områden."),
    ("Ger plåttak ROT-avdrag?","Ja, arbetskostnaden ger ROT-avdrag. Vi gör avdraget direkt på fakturan.")])

page(file="papptak.html",
  title="Papptak i Stockholm – byta & lägga papptak | Geal Entreprenad AB",
  description="Byta eller lägga nytt papptak på villa, radhus och funkishus i Stockholm. Ny underlagspapp och ytpapp, täta detaljer och ROT. Gratis besök och fast pris.",
  h1="Papptak i Stockholm",
  service=True, service_type="Papptak", localbiz=False,
  howto=("Så lägger vi nytt papptak", [
    ("Besiktning","Vi går upp på taket och vinden, bedömer pappen, råsponten och detaljerna och avgör om taket ska lagas eller läggas om."),
    ("Rivning","Den gamla pappen tas bort och forslas bort, så att underlaget kan kontrolleras."),
    ("Underlag","Råsponten kontrolleras och skadade eller fuktskadade partier byts."),
    ("Underlagspapp","Ett första lager papp läggs över hela takytan med täta skarvar."),
    ("Ytpapp","Ytpappen läggs ovanpå och skyddar mot sol, regn och slitage."),
    ("Detaljer och slutkontroll","Fotplåt, vindskivor, genomföringar och avvattning görs täta, och vi går igenom taket tillsammans med dig.")]),
  crumbs=SVC_CRUMB+[("Papptak","papptak.html")],
  cta=("Dags att byta papptaket?","Vi kommer ut gratis, bedömer taket och lämnar ett skriftligt kostnadsförslag med fast pris."),
  body=hero("Papptak i Stockholm",
    "Vi byter och lägger nytt papptak på villor, radhus och funkishus med låg taklutning. Ett papptak brukar hålla 20–30 år, och när det är slut lägger vi ny underlagspapp och ytpapp och gör alla detaljer täta. Du får fast pris efter ett gratis besök.",
    SVC_CRUMB+[("Papptak","papptak.html")],
    [("#nar","När byta"),("#ingar","Så går det till"),("#plat","Papp eller plåt"),("#pris","Kostnad & ROT"),("#faq","Vanliga frågor")])
    + sec_split("När behöver papptaket bytas?", [
        "Papptak brukar hålla 20–30 år, kortare på låglutande tak där vatten blir stående. Papp är vanligt på funkisvillor, radhus och hus med nästan platta tak, där pannor inte fungerar.",
        f"Ett gammalt papptak kan ofta lagas punktvis så länge pappen är hel i övrigt. Är den spröd över hela ytan, eller har fukt nått råsponten, är det dags att lägga om. Osäker? En {a('takbesiktning.html','takbesiktning')} ger besked."],
        "Tecken på att pappen är slut", [
        "Blåsor och sprickor i ytan.","Lösa eller öppna skarvar.",
        "Stående vatten efter regn.","Granulat som spolas ner i hängrännorna.",
        "Fuktfläckar i tak eller på vinden.","Mossa och påväxt som håller fukt."], sid="nar")
    + sec_process("Så går ett byte av papptak till", [
        ("Besiktning","Vi går upp på taket och vinden, bedömer pappen, råsponten och detaljerna och avgör om taket ska lagas eller läggas om."),
        ("Rivning","Den gamla pappen tas bort och forslas bort, så att underlaget kan kontrolleras."),
        ("Underlag","Råsponten kontrolleras och skadade eller fuktskadade partier byts."),
        ("Underlagspapp","Ett första lager papp läggs över hela takytan med täta skarvar."),
        ("Ytpapp","Ytpappen läggs ovanpå och skyddar mot sol, regn och slitage."),
        ("Detaljer och slutkontroll","Fotplåt, vindskivor, genomföringar och avvattning görs täta, och vi går igenom taket tillsammans med dig.")], muted=True, sid="ingar")
    + sec("Det mesta läckaget sitter i detaljerna", [
        "På ett låglutande tak rinner vattnet långsamt, så skarvar, takfot och anslutningar måste vara helt täta. De vanligaste läckagepunkterna är runt skorsten, ventilation och andra genomföringar, vid takfoten och där taket möter en vägg.",
        f"Därför byter vi plåtdetaljer som fotplåt och vindskivor när de är slitna, och ser över {a('hangrannor-stupror.html','hängrännor och stuprör')} i samma omgång."])
    + sec("Papp eller plåt på låg lutning?", [
        f"Både papp och plåt fungerar på låga taklutningar. Papp har kortare livslängd, 20–30 år, medan ett {a('plattak.html','plåttak')} brukar hålla 40–50 år. Falsad plåt är det klassiska alternativet på funkishus, se {a('falsat-plattak.html','falsat plåttak och bandtäckning')}.",
        f"Vill du byta från papp till plåt bedömer vi underlaget och lutningen vid besöket. Sedan 1 december 2025 kräver byte av takmaterial på villa och radhus normalt inget bygglov, utom i skyddade miljöer – läs mer i {a('bygglov-takbyte.html','bygglov för takbyte')}. Jämför fler material i {a('takmaterial-livslangd.html','livslängd per takmaterial')}."], muted=True, sid="plat")
    + sec("Vad kostar ett papptak?", [
        "Priset beror på takets yta, lutning och form, om råsponten behöver bytas, antal genomföringar och plåtdetaljer samt ställning och åtkomst. Rivning och bortforsling av den gamla pappen ingår i ett komplett byte.",
        f"Vi publicerar inga fasta priser. Vi kommer ut gratis och lämnar ett skriftligt kostnadsförslag med fast pris. Vill du ha en första uppskattning per kvadratmeter kan du {a('https://takbytepris.nu/','räkna på papptak på takbytepris.nu')}. Mer om vad som styr priset finns i {a('vad-kostar-takbyte.html','vad kostar ett takbyte')}."], sid="pris")
    + rot_box("Arbetskostnaden för att byta papptak på villa ger ROT-avdrag. Vi gör avdraget direkt på fakturan.")
    + links_block("Papptak i ditt område", [
        ("taklaggare-bromma.html","Bromma","Funkisvillor med låga tak."),
        ("taklaggare-solna.html","Solna","Villatak i Råsunda och Råsta."),
        ("taklaggare-jarfalla.html","Järfälla","Radhus med låglutande tak."),
        ("taklaggare-taby.html","Täby","Villor och radhus från 60–70-talet."),
        ("taklaggare-sundbyberg.html","Sundbyberg","Plåt- och papptak i Rissne.")], muted=False, sid="orter")
    + links_block("Relaterat", [
        ("plattak.html","Plåttak","Nytt plåttak på låg lutning."),
        ("takmaterial-livslangd.html","Livslängd per takmaterial","Så länge håller papp, plåt och pannor."),
        ("takbyte.html","Takbyte","Komplett takbyte på villa."),
        ("vad-kostar-takbyte.html","Vad kostar ett takbyte?","Pris per kvm och ROT.")]),
  faq=[
    ("Hur länge håller ett papptak?","Ett papptak brukar hålla 20–30 år, kortare på låglutande tak där vatten blir stående."),
    ("Hur vet jag att papptaket behöver bytas?","Blåsor, sprickor, lösa skarvar, stående vatten och fuktfläckar på vinden är vanliga tecken. Vi bedömer taket vid ett gratis besök."),
    ("Kan man laga ett papptak i stället för att byta?","Ja, om pappen är hel i övrigt kan enstaka skador lagas. Är den spröd över hela ytan eller har fukt nått råsponten lönar sig en omläggning."),
    ("Vad kostar det att byta papptak?","Det beror på yta, lutning, underlagets skick och detaljer. Vi lämnar fast pris efter ett gratis besök. Arbetskostnaden ger ROT-avdrag."),
    ("Kan man lägga papptak själv?","Det går, men arbete på tak innebär fallrisk och på ett bostadshus avgör täta skarvar och detaljer om taket håller. ROT-avdrag får du bara när ett företag utför arbetet."),
    ("Vad är tjärpapp?","Tjärpapp är det vardagliga namnet på takpapp. Modern takpapp är bitumenbaserad, inte tjärbaserad."),
    ("Kan man byta från papptak till plåttak?","Ja, plåt fungerar också på låg lutning och håller längre. Vi bedömer underlaget och lutningen vid besöket."),
    ("Behövs bygglov för att byta papptak?","Normalt inte för villa eller radhus: sedan 1 december 2025 krävs inget bygglov för att byta takmaterial på en- och tvåbostadshus. Undantaget är särskilt kulturhistoriskt värdefulla hus och områden.")])

page(file="takmalning.html",
  title="Takmålning i Stockholm – målning av plåttak med ROT | Geal Entreprenad AB",
  description="Takmålning av plåttak och falsade tak i Stockholm. Tvätt, rostskydd och rätt färgsystem – så går det till, när det lönar sig och vad ROT ger. Gratis besök.",
  h1="Takmålning i Stockholm",
  service=True, service_type="Takmålning", localbiz=False,
  howto=("Så går en takmålning till", [
    ("Besiktning","Vi går upp på taket, bedömer rost, färgskikt, falsar och detaljer och avgör om målning är rätt åtgärd."),
    ("Tvätt","Taket tvättas med lågtryck och rengöringsmedel så att smuts, påväxt och krita försvinner."),
    ("Rostbehandling","Rost skrapas eller borstas ner till fast underlag och punktgrundas med rostskyddsgrund."),
    ("Tätning","Falsar, skarvar och genomföringar ses över och tätas där det behövs."),
    ("Målning","Grundfärg och täckfärg läggs i rätt skikttjocklek enligt färgtillverkarens system."),
    ("Slutkontroll","Vi kontrollerar resultatet tillsammans med dig och ger råd om underhåll.")]),
  crumbs=SVC_CRUMB+[("Takmålning","takmalning.html")],
  cta=("Dags att måla taket?","Vi kommer ut gratis, bedömer om målning räcker och lämnar ett skriftligt kostnadsförslag."),
  body=hero("Takmålning i Stockholm",
    "Ett plåttak som har börjat blekna, krita eller rosta behöver inte alltid bytas. Rätt utförd takmålning – tvätt, rostskydd och ett färgsystem för plåt – ger taket ett nytt skydd för många år framåt.",
    SVC_CRUMB+[("Takmålning","takmalning.html")],
    [("#nar","När passar det"),("#ingar","Så går det till"),("#farg","Färgsystem"),("#pris","Kostnad & ROT"),("#faq","Vanliga frågor")])
    + sec("När är takmålning rätt åtgärd?", [
        "Takmålning passar när plåttakets ytskikt har slitits men själva plåten fortfarande är hel. Typiska tecken är att färgen har mattats och kritar (det blir vitt på fingret när du drar över ytan), att kulören har bleknat ojämnt, eller att det har uppstått rostprickar vid skruvar, falsar, nockar och vid takfoten. I det läget skyddar en ny färgfilm plåten innan rosten hinner äta sig igenom.",
        "Målning är däremot fel åtgärd när plåten är genomrostad, när läckage redan har skadat underlagspapp och råspont, eller när taket ändå närmar sig slutet av sin livslängd. Då blir resultatet kortlivat och pengarna gör mer nytta i ett nytt tak. Därför börjar vi alltid med att gå upp på taket och titta – inte med att räkna kvadratmeter.",
        f"Osäker på skicket? En {a('takbesiktning.html','takbesiktning')} ger ett skriftligt underlag. Är taket uttjänt läser du mer om {a('plattak.html','nytt plåttak')}."], sid="nar")
    + fig("takmalning-plattak-process", "Plåttak som målas om – sliten rostig plåt till vänster, nymålad grafitgrå plåt till höger")
    + sec_split("Tecken på att plåttaket behöver målas", [
        "Ett plåttak på en villa i Stockholmsområdet målas vanligen om med 10–20 års mellanrum, beroende på färgsystem, väderstreck och hur mycket träd som står runt huset. Söderläge och mycket sol bryter ner färgen snabbare, medan skuggiga tak under björk och tall får mer påväxt och fukt.",
        "Vänta inte tills rosten syns från gatan. Ytrost som åtgärdas tidigt kostar lite, medan rost som har gått igenom plåten kräver lagning eller byte av hela plåtar."],
        "Kontrollera själv från marken", [
        "Kulören har bleknat eller blivit flammig.","Färgen kritar eller flagnar.",
        "Rostprickar vid skruvar, falsar eller nock.","Rost i hängrännor och vid takfot.",
        "Påväxt och mossa i skuggiga partier."], sid="tecken")
    + sec_process("Så går takmålningen till", [
        ("Besiktning","Vi bedömer rost, färgskikt, falsar och detaljer och berättar ärligt om målning räcker."),
        ("Skydd & tvätt","Vi skyddar fasad, rabatter och fönster och tvättar taket med lågtryck och rengöringsmedel."),
        ("Rostbehandling","Rost borstas ner till fast underlag och grundas med rostskyddsgrund."),
        ("Tätning","Falsar, skarvar och genomföringar ses över och tätas vid behov."),
        ("Målning","Grund- och täckfärg i rätt skikttjocklek enligt tillverkarens system."),
        ("Slutkontroll","Vi går igenom resultatet med dig och dokumenterar arbetet.")], muted=True, sid="ingar")
    + sec("Färgsystem för plåttak", [
        "Det finns ingen färg som passar alla tak. Valet beror på vilken plåt taket är gjort av och hur det är behandlat sedan tidigare. Varmförzinkad plåt, plastbelagd plåt (till exempel polyester eller PVC-belagd profilplåt) och äldre målad plåt kräver olika förbehandling och grundfärg för att färgen ska fästa.",
        "Vi följer alltid färgtillverkarens system – samma tvättmedel, grund och täckfärg som är provade ihop – och lägger färgen i rätt skikttjocklek. Det är den vanligaste orsaken till att en takmålning håller i 5 år i stället för 15: för tunt lager eller fel grund på fel plåt.",
        "Vill du byta kulör går det bra. Mörka kulörer som svart och grafit är vanligast på villor i Bromma, Spånga och Sollentuna, men tegelröd och grön förekommer också – särskilt på äldre hus där kulören bör passa husets epok."], sid="farg")
    + sec_split("Falsat plåttak, profilplåt och detaljer", [
        "Falsade plåttak (bandtäckning) har ofta trettio, fyrtio år på nacken på villor från 1950–70-talen. De går i regel utmärkt att måla, men falsarna måste kontrolleras. Är en fals öppen eller rostig tätas den innan målning – annars kan vatten tränga in under färgen.",
        f"Profilplåt (trapetsprofil) har skruvar med gummibricka som torkar ut med åren. Vid målning byter vi skruvar och brickor där de har släppt. Vi ser också över {a('hangrannor-stupror.html','hängrännor och stuprör')}, ventilationshuvar och plåt runt skorstenen, eftersom det är där läckage oftast börjar."],
        "Vi kontrollerar alltid", [
        "Falsar och skarvar.","Skruvar och gummibrickor.",
        "Plåt runt skorsten och ventilation.","Nockplåt och vindskivor.","Hängrännor och takavvattning."])
    + sec("Kan man måla betongpannor eller tegel?", [
        "Betongpannor kan behandlas med en särskild takfärg för betong, men det förlänger främst utseendet – inte pannornas tekniska livslängd. Är pannorna porösa eller underlagspappen gammal hjälper inte färg mot läckage. Tegeltak målar vi inte: teglet behöver kunna andas, och färg kan göra att fukt stängs inne och att pannorna fryser sönder.",
        f"Har du betong- eller tegeltak med mossa och smuts räcker det oftast med {a('taktvatt.html','taktvätt')} och behandling mot påväxt. Läs mer i guiden {a('mossa-pa-taket.html','mossa på taket')}."], muted=True, sid="betong")
    + fig("takmalning-betongpannor", "Betongpannor där halva ytan är rengjord och målad med svart takfärg")
    + sec("Vad kostar takmålning?", [
        "Kostnaden beror på takets storlek och lutning, hur mycket rost som måste åtgärdas, om falsar behöver tätas, vilken färg som används och hur lätt det är att komma åt taket med ställning eller lift. Två tak med samma yta kan därför få helt olika pris.",
        "Vi publicerar inga fasta priser. I stället kommer vi ut gratis, tittar på taket och lämnar ett skriftligt kostnadsförslag med vad som ingår – tvätt, rostbehandling, antal färgskikt, kulör och ställning. Då kan du jämföra offerter på lika villkor.",
        "Jämfört med ett nytt plåttak är målning i regel en bråkdel av kostnaden, förutsatt att plåten är frisk. Det är därför det lönar sig att måla i tid."], sid="pris")
    + rot_box("Arbetskostnaden för takmålning på din villa ger ROT-avdrag. Vi gör avdraget direkt på fakturan, så du betalar bara din del.")
    + sec("Bästa tiden att måla taket i Stockholm", [
        "Takfärg behöver torr plåt och plusgrader för att härda rätt. I Stockholmsområdet målar vi normalt från maj till och med september. Vi planerar efter väderprognosen och väntar hellre en dag än målar på fuktig plåt.",
        "Planera gärna under vintern och våren – då hinner vi göra besiktningen och boka in arbetet innan högsäsongen."])
    + links_block("Vi målar plåttak i hela Stockholm", [
        ("taklaggare-bromma.html","Bromma","Funkisvillor och 50-talshus med falsade plåttak."),
        ("taklaggare-sundbyberg.html","Sundbyberg","Villor i Duvbo, Lilla Alby och Ör."),
        ("taklaggare-spanga.html","Spånga","Villaområden från 50- till 70-talet."),
        ("taklaggare-danderyd.html","Danderyd","Större villor med svart bandtäckt plåt."),
        ("taklaggare-sollentuna.html","Sollentuna","Plåt och betong på 60–70-talsvillor."),
        ("taklaggare-lidingo.html","Lidingö","Havsnära tak som utsätts för saltluft.")], sid="orter")
    + links_block("Relaterat", [
        ("taktvatt.html","Taktvätt","Rengöring innan målning eller som eget underhåll."),
        ("plattak.html","Plåttak","Nytt plåttak när målning inte räcker."),
        ("takbesiktning.html","Takbesiktning","Skriftligt underlag innan du bestämmer dig."),
        ("takmaterial-livslangd.html","Livslängd per takmaterial","Hur länge plåt, betong och tegel håller."),
        ("mala-plattak.html","Måla om eller byta plåttaket?","Så avgör du om målning räcker.")]),
  faq=[
    ("Hur ofta behöver ett plåttak målas?","Vanligen var 10–20:e år beroende på färgsystem, väderstreck och påväxt. Kritar färgen eller syns rost är det dags att planera."),
    ("Hur länge håller en takmålning?","Med rätt tvätt, rostbehandling och färgsystem håller en takmålning normalt 10–15 år, ofta längre på skyddade tak."),
    ("Kan man måla ett falsat plåttak?","Ja. Falsade plåttak går bra att måla, men falsar och skarvar måste kontrolleras och tätas innan målning."),
    ("Kan man måla betongpannor?","Det går med särskild betongfärg, men det förbättrar främst utseendet. Tegeltak målar vi inte eftersom färgen kan stänga inne fukt."),
    ("Vilken tid på året målar man tak?","Från maj till september, på torr plåt och vid plusgrader. Boka gärna besiktning redan under våren."),
    ("Kan man byta färg på taket?","Ja, med rätt grundfärg kan du byta kulör. Vi hjälper dig välja en kulör som passar husets stil."),
    ("Ger takmålning ROT-avdrag?","Ja, arbetskostnaden ger ROT-avdrag. Vi gör avdraget direkt på fakturan."),
    ("Vad kostar takmålning?","Det beror på yta, lutning, rost och åtkomst. Vi kommer ut gratis och lämnar ett skriftligt kostnadsförslag.")])

page(file="taktvatt.html",
  title="Taktvätt i Stockholm – ta bort mossa skonsamt | Geal Entreprenad AB",
  description="Taktvätt i Stockholm: skonsam lågtryckstvätt av betong-, tegel- och plåttak, mossbehandling och rensning av hängrännor. Gratis besök och ROT-avdrag.",
  h1="Taktvätt i Stockholm",
  service=True, service_type="Taktvätt", localbiz=False,
  howto=("Så går en taktvätt till", [
    ("Bedömning","Vi kontrollerar taktyp, skick och mängd påväxt och väljer metod."),
    ("Skydd","Fasad, fönster, rabatter och hängrännor skyddas."),
    ("Mekanisk rengöring","Grov mossa tas bort försiktigt för hand eller med borste."),
    ("Lågtryckstvätt","Taket tvättas med lågtryck och rengöringsmedel anpassat för materialet."),
    ("Behandling","Taket behandlas mot ny påväxt."),
    ("Rännor & kontroll","Hängrännor och stuprör rensas och vi rapporterar skador vi har sett.")]),
  crumbs=SVC_CRUMB+[("Taktvätt","taktvatt.html")],
  cta=("Behöver taket tvättas?","Vi kommer ut gratis, bedömer taket och lämnar ett skriftligt kostnadsförslag."),
  body=hero("Taktvätt i Stockholm",
    "Mossa och påväxt håller kvar fukt, lyfter pannor och sätter igen hängrännorna. En skonsam taktvätt med rätt metod för din taktyp förlänger takets liv – utan högtryck som sliter på ytan.",
    SVC_CRUMB+[("Taktvätt","taktvatt.html")],
    [("#varfor","Varför taktvätt"),("#metod","Metod per taktyp"),("#ingar","Så går det till"),("#pris","Kostnad & ROT"),("#faq","Vanliga frågor")])
    + sec("Varför ska man tvätta taket?", [
        "Mossa fungerar som en svamp. Den suger upp regnvatten och håller taket fuktigt långt efter att det har slutat regna. På vintern fryser fukten, och när mossan växer in under pannornas överlapp kan den lyfta dem så att vatten blåser in under. Samtidigt spolas mossa och smuts ner i hängrännorna, som sätts igen och svämmar över.",
        "I Stockholmsområdet är påväxt särskilt vanlig på villor med mycket träd runt huset – tall, gran och björk ger skugga och barr som håller kvar fukten. Norrsidan av taket drabbas nästan alltid först.",
        f"Regelbunden taktvätt är därför underhåll, inte bara utseende. Läs mer om orsaker och förebyggande i guiden {a('mossa-pa-taket.html','mossa på taket')}."], sid="varfor")
    + fig("taktvatt-mossa", "Lågtryckstvätt av mossbeväxt betongtak")
    + sec_split("Metod efter taktyp", [
        "Fel metod kan göra mer skada än mossan. Högtryckstvätt nära ytan blåser bort betongpannornas ytskikt, gör dem porösa och tar sig in under pannorna. Därför arbetar vi med lågtryck och rengöringsmedel som är anpassade för materialet.",
        f"Betongpannor tvättas skonsamt och behandlas mot ny påväxt. Tegelpannor är känsligare för hårda metoder och rengörs försiktigt. Plåttak tvättas fritt från smuts och krita – ofta som första steg inför {a('takmalning.html','takmålning')}."],
        "Vi anpassar metoden till", [
        "Betongpannor.","Tegelpannor.","Plåttak och falsat plåttak.",
        "Papptak och shingel.","Takets lutning och åtkomst."], sid="metod")
    + sec_process("Så går taktvätten till", [
        ("Bedömning","Vi kontrollerar taktyp, skick och mängd påväxt och väljer metod."),
        ("Skydd","Fasad, fönster, rabatter och rännor skyddas."),
        ("Mekanisk rengöring","Grov mossa tas bort försiktigt för hand eller med borste."),
        ("Lågtryckstvätt","Taket tvättas med lågtryck och anpassat rengöringsmedel."),
        ("Behandling","Taket behandlas mot ny påväxt."),
        ("Rännor & rapport","Hängrännor rensas och vi berättar om skador vi har sett.")], muted=True, sid="ingar")
    + sec_split("Taktvätt är också en kontroll", [
        f"När vi ändå är uppe på taket ser vi allt som är svårt att se från marken: spruckna pannor, lös nockpanna, dålig plåt runt skorstenen eller underlagspapp som syns vid takfoten. Du får veta vad vi har hittat, och om något bör åtgärdas kan det ofta göras samtidigt. Vill du ha ett skriftligt utlåtande gör vi en {a('takbesiktning.html','takbesiktning')}.",
        f"Vi rensar även {a('hangrannor-stupror.html','hängrännor och stuprör')} som en del av tvätten, så att mossan inte bara flyttar från taket till rännan."],
        "Vi tittar efter", [
        "Spruckna eller lösa pannor.","Plåt runt skorsten och ventilation.",
        "Nockpannor och nockbruk.","Underlagspapp vid takfoten.","Hängrännor och stuprör."])
    + sec("Hur ofta ska taket tvättas?", [
        "Det beror på läge. Ett tak i öppet, soligt läge klarar sig ofta 8–10 år mellan tvättarna, medan ett tak under höga träd kan behöva tvättas var 3–5:e år. En behandling mot påväxt efter tvätten gör att intervallet blir längre.",
        "Bästa tiden för taktvätt är vår och höst, när det är plusgrader och mossan är fuktig och lätt att få bort. Vi tvättar inte vid frost."])
    + sec("Vad kostar taktvätt?", [
        "Priset beror på takets storlek och lutning, taktyp, mängden mossa och hur lätt det är att komma åt taket. Rensning av hängrännor och behandling mot påväxt ingår ofta i samma arbete.",
        "Vi publicerar inga fasta priser. Vi kommer ut gratis och lämnar ett skriftligt kostnadsförslag med vad som ingår."], sid="pris")
    + rot_box("Arbetskostnaden för taktvätt på villa ger ROT-avdrag. Vi gör avdraget direkt på fakturan.")
    + links_block("Taktvätt i ditt område", [
        ("taklaggare-sollentuna.html","Sollentuna","Villor under tall och björk med mycket påväxt."),
        ("taklaggare-bromma.html","Bromma","Äldre villaträdgårdar och skuggiga tak."),
        ("taklaggare-danderyd.html","Danderyd","Stora tomter med hög växtlighet."),
        ("taklaggare-taby.html","Täby","Radhus och villor från 70-talet."),
        ("taklaggare-spanga.html","Spånga","Betongtak på 60-talsvillor."),
        ("taklaggare-nacka.html","Nacka","Skuggiga tomter i skog och vid vatten.")], sid="orter")
    + links_block("Relaterat", [
        ("mossa-pa-taket.html","Mossa på taket – behandling","Orsaker, metoder och förebyggande."),
        ("hangrannor-stupror.html","Hängrännor & stuprör","Rensning och byte för god avvattning."),
        ("takmalning.html","Takmålning","Nytt ytskydd på plåttak efter tvätt.")]),
  faq=[
    ("Skadar högtryckstvätt taket?","Ja, högtryck nära ytan kan skada pannornas ytskikt och tränga in under pannorna. Vi använder lågtryck och metoder anpassade efter taktyp."),
    ("Hur ofta bör taket tvättas?","Var 3–5:e år under träd och var 8–10:e år i öppet läge. Behandling mot påväxt förlänger intervallet."),
    ("När på året tvättar man taket?","Vår och höst vid plusgrader, när mossan är fuktig och lätt att få bort. Inte vid frost."),
    ("Kan ni behandla mot ny mossa?","Ja, efter tvätten behandlar vi taket mot ny påväxt med medel anpassat för taktypen."),
    ("Rensar ni hängrännorna samtidigt?","Ja, rensning av hängrännor och stuprör ingår normalt i taktvätten."),
    ("Ger taktvätt ROT-avdrag?","Ja, arbetskostnaden ger ROT-avdrag. Vi gör avdraget direkt på fakturan.")])


# ====================== VILLA PILLAR ======================================
page(file="villatak.html", localbiz=True,
  title="Tak på villa – komplett guide till villatak i Stockholm | Geal Entreprenad AB",
  description="Villatak i Stockholm: allt om takbyte, material, kostnad, ROT och underhåll för tak på villa. Guide och lokala takläggare för ditt villatak.",
  h1="Tak på villa – komplett guide till villatak",
  crumbs=[("Hem","/"),("Villatak","villatak.html")],
  cta=("Ska du åtgärda ditt villatak?","Vi är takläggare specialiserade på villatak i Stockholm – begär en kostnadsfri offert."),
  body=hero("Tak på villa – komplett guide till villatak",
    "Villatak har egna förutsättningar: taklutning, material och detaljer skiljer sig från större fastigheter. Här samlar vi allt om takbyte, renovering, material, kostnad och underhåll för tak på villa i Stockholm.",
    [("Hem","/"),("Villatak","villatak.html")],
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
_area_files = {n: f"taklaggare-{slug(n)}.html" for n in AREAS}
def _cards(names):
    return "\n".join(f"""            <article class="service-snippet">
              <h3>{n}</h3>
              <p>Takläggare i {n} – takbyte, renovering och besiktning.</p>
              <a class="text-link" href="{_area_files[n]}">Takläggare i {n}</a>
            </article>""" for n in names)
def _area_section(title, names, muted):
    cls = "section section-muted seo-section" if muted else "section seo-section"
    return f"""      <section class="{cls}">
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">{title}</h2>
          </div>
          <div class="service-grid">
{_cards(names)}
          </div>
        </div>
      </section>"""
_stad = [n for n in AREAS if n in STOCKHOLM_STAD]
_kommuner = [n for n in AREAS if n not in STOCKHOLM_STAD]
page(file="omraden.html",
  title="Områden – takläggare i hela Stockholm | Geal Entreprenad AB",
  description="Takläggare i alla Stockholms stadsdelar och kranskommuner – från Bromma, Hässelby och Enskede till Täby, Värmdö och Haninge. Välj ditt område.",
  h1="Områden vi arbetar i",
  crumbs=[("Hem","/"),("Områden","omraden.html")],
  cta=("Finns ditt område inte med?","Skicka en förfrågan – vi tar uppdrag i hela Storstockholm."),
  body=hero("Områden vi arbetar i",
    "Vi utgår från Bromma och arbetar i alla stadsdelar i Stockholm och i kranskommunerna runt omkring.",
    [("Hem","/"),("Områden","omraden.html")])
    + _area_section("Stadsdelar i Stockholm", _stad, True)
    + _area_section("Kommuner runt Stockholm", _kommuner, False)
    + trp_list_html("Takrenovering per område", muted=True, sid="takrenovering")
    + f"""      <section class="section seo-section">
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">Vi arbetar även i Dalarna</h2>
            <p>Utöver Storstockholm tar vi takuppdrag i Dalarna – {a('taklaggare-borlange.html','Borlänge')}, {a('taklaggare-falun.html','Falun')}, {a('taklaggare-ludvika.html','Ludvika')}, {a('taklaggare-mora.html','Mora')}, {a('taklaggare-leksand.html','Leksand')} med flera. Där samordnar vi projektet och utför arbetet via vår lokala samarbetspartner på plats. {a('dalarna.html','Se takläggare i Dalarna')}.</p>
          </div>
        </div>
      </section>""")

SRCA = '<a class="text-link" href="https://www.boverket.se/sv/samhallsplanering/uppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/" rel="noopener">Boverket – PBL-ändringar från 1 december 2025</a>'
# ====================== LOCATION PAGES ====================================
# Per ort: dict med intro (hero-lead), paras (>=3 unika lokala stycken),
# items (aside-punkter) och faq (unik lokal FAQ). [OWNER] Riktiga lokala
# priser/kundcase kan tillföras senare för ännu starkare E-E-A-T.
LOC = {
 "Sundbyberg": {
   "intro": "Sundbyberg är ett av våra närmaste arbetsområden – vi finns precis intill i Bromma. Här känner vi husen, taken och de lokala förutsättningarna, från äldre villor i Duvbo och Storskogen till nyare bebyggelse. Vi är takläggare i Sundbyberg för takbyte, takrenovering och takbesiktning.",
   "paras": [
     "Sundbyberg är en av Sveriges till ytan minsta men tätaste kommuner, och bebyggelsen växlar snabbt mellan äldre trävillor och nyare flerbostadshus. I villaområden som Duvbo, Storskogen och Lilla Alby dominerar branta sadeltak med tegel- eller betongpannor, ofta från tidigt 1900-tal, där underlagspapp och läkt hunnit bli spröda.",
     "Duvbos kulturhistoriska trähusmiljö ställer särskilda krav – här är det viktigt att bevara takets uttryck och detaljer vid ett takbyte, samtidigt som vi moderniserar underlag, plåt och avvattning. Närmare centrum och Rissne finns fler flerbostadshus med plåt- och papptak, där vi arbetar med tätskikt och plåtdetaljer.",
     "Eftersom vår bas ligger i Bromma, bara minuter från Sundbyberg, har vi kort inställelsetid för besiktning och kan snabbt vara på plats vid akuta läckage. Vi känner de lokala förutsättningarna – från smala gator i Duvbo som påverkar ställning och etablering till snölaster på norrvända tak.",
   ],
   "items": ["Grannområde till vår bas i Bromma – kort inställelsetid.","Erfarenhet av Duvbos äldre trävillor och kulturmiljö.","Takbyte, renovering, besiktning och plåtarbeten."],
   "faq": [
     ("Hur snabbt kan ni vara på plats i Sundbyberg?","Eftersom vi utgår från Bromma, granne med Sundbyberg, har vi mycket kort inställelsetid och kan oftast boka en besiktning inom några dagar – och rycka ut snabbare vid akuta läckage."),
     ("Får jag byta tak i Duvbo utan tillstånd?","Duvbo är en kulturhistoriskt värdefull trähusmiljö. Fasadändringar på villor är sedan 1 december 2025 i regel lovfria, men för särskilt värdefulla byggnader och områden krävs fortfarande bygglov. Stäm av med Sundbybergs stad innan du byter material eller kulör."),
     ("Arbetar ni med både villor och flerbostadshus i Sundbyberg?","Ja. Vi byter och renoverar villatak i Duvbo och Storskogen och utför plåt- och tätskiktsarbeten på flerbostadshus närmare centrum och Rissne."),
   ]},
 "Solna": {
   "intro": "Solna gränsar till Sundbyberg och är ett av våra vanligaste arbetsområden. Vi hjälper villaägare i bland annat Råsunda, Råsta och Stocksundstorp med takbyte, takrenovering och plåtarbeten.",
   "paras": [
     "Solna gränsar direkt till både Sundbyberg och Bromma, och villabebyggelsen är koncentrerad till områden som Råsunda villastad, Råsta egnahem, Stocksundstorp och Bergshamra by. Många villor är byggda mellan 1920- och 1960-talet, och en stor andel av taken närmar sig nu slutet av sin tekniska livslängd.",
     "I Råsunda villastad ser vi ofta klassiska tegeltak där pannorna är hela men underlagspapp och läkt är uttjänta – då räcker det ibland med en takomläggning istället för fullt byte. I Stocksundstorp, där villorna är från olika tider och flera har lägre lutning, är plåt- och papptak vanligare.",
     "Solnas blandning av epoker gör att vi nästan alltid börjar med en besiktning för att avgöra rätt åtgärdsnivå. Vår närhet till Solna innebär att vi kan hålla tät kontakt genom hela projektet och snabbt komma ut på uppföljning.",
   ],
   "items": ["Granne med vår bas – snabb service i hela Solna.","Erfarenhet av 1920–60-talsvillor.","Villatak i Råsunda, Råsta, Stocksundstorp."],
   "faq": [
     ("Vilka delar av Solna arbetar ni i?","Vi tar takuppdrag i hela Solna, bland annat Råsunda, Råsta, Stocksundstorp, Bergshamra by och Järvastaden – både villor och mindre fastigheter."),
     ("Räcker det med takomläggning på mitt Solna-hus?","På många äldre tegeltak i Råsunda villastad är pannorna hela medan underlaget är slitet – då kan en omläggning räcka. En besiktning ger säkert svar."),
     ("Hur nära ligger ni Solna?","Vi utgår från Bromma, som gränsar till Solna, vilket ger korta restider och snabb service."),
   ]},
 "Bromma": {
   "why": "Med vår bas i Abrahamsberg har vi nära till villorna i Ängby, Nockeby, Äppelviken och Ålsten. Det gör att vi kan komma ut på besiktning utan långa väntetider och hålla nära kontakt genom hela projektet.",
   "intro": "Bromma i västerort är vårt hemmaområde – vi utgår härifrån (Abrahamsberg) och känner västerorts villor väl. Vi är takläggare i Bromma för villor i bland annat Ängby, Nockeby, Äppelviken och Bromma Kyrka.",
   "paras": [
     "Bromma i västra Stockholm är vårt hemmaområde – vi utgår från Abrahamsberg och känner västerorts villor in i minsta detalj. I klassiska trädgårdsstäder som Ängby, Äppelviken, Nockeby och Smedslätten är många hus från 1920–40-talet, ofta med branta tegeltak och karaktärsfulla takdetaljer som vi är vana att bevara.",
     "Äppelviken och Ålsten har en enhetlig villakaraktär där husens uttryck värnas; vid takbyte här är det avgörande att välja pannor och plåtkulörer som passar områdets stil. I nyare delar och radhusområden förekommer också låglutande tak och plåtlösningar.",
     "Som lokal takfirma med bas mitt i Bromma har vi mycket korta avstånd till jobben, vilket gör etablering, ställning och uppföljning enkla. Vi känner de lokala förutsättningarna – från stora lövträd som fyller hängrännor till snölaster på norrsidor.",
   ],
   "items": ["Lokal takfirma med bas mitt i Bromma.","Varsamt takbyte i trädgårdsstäderna Ängby/Äppelviken.","Tegel-, betong- och plåttak."],
   "faq": [
     ("Ni utgår från Bromma – vad betyder det för mig?","Att vi har hemmaplan: kort inställelsetid, enkel etablering och snabb uppföljning eftersom våra jobb ofta ligger bara minuter bort."),
     ("Kan ni bevara husets stil vid takbyte i Äppelviken eller Ängby?","Ja, det är en av våra specialiteter. Vi väljer pannor, plåt och detaljer som bevarar trädgårdsstadens uttryck och moderniserar samtidigt underlag och avvattning."),
     ("Vilka takmaterial passar Brommas villor?","Tegel och betong dominerar på de branta sadeltaken, medan plåt passar lägre lutningar. Vi anpassar valet efter husets ålder och områdets karaktär."),
   ]},
 "Spånga": {
   "intro": "Spånga och Tensta–Spånga är ett stort villaområde i nordvästra Stockholm. Vi hjälper villaägare i Spånga, Bromsten och Solhem med takbyte, takrenovering och takbesiktning.",
   "paras": [
     "Spånga i nordvästra Stockholm är ett stort och blandat villaområde som omfattar bland annat Bromsten, Solhem, Sundby och Flysta. Bebyggelsen spänner från äldre trävillor till 1960- och 70-talshus, och många av taken från efterkrigstiden är nu mogna för omläggning eller byte.",
     "I Solhem och Flysta ser vi ofta betongpannor från 60–70-talet som börjat vittra, tillsammans med underlagspapp som passerat sin livslängd. I sådana projekt byter vi gärna hängrännor, stuprör och taksäkerhet i samma omgång för ett komplett resultat.",
     "Spånga ligger nära vår bas i Bromma, vilket gör det enkelt för oss att komma ut på besiktning och hålla tempo i projekten. Vi anpassar alltid åtgärderna efter husets ålder och det aktuella takets skick.",
   ],
   "items": ["Villatak i Spånga, Bromsten, Solhem, Flysta.","Erfarenhet av 60–70-talens betongpannetak.","Takbyte med ny avvattning och taksäkerhet."],
   "faq": [
     ("Vilka områden i Spånga arbetar ni i?","Vi tar takuppdrag i hela Spånga, bland annat Bromsten, Solhem, Sundby och Flysta."),
     ("Mina betongpannor från 70-talet vittrar – måste jag byta hela taket?","Ofta ja, om både pannor och underlag är uttjänta. Men en besiktning avgör – ibland räcker en omläggning med nytt underlag."),
     ("Byter ni hängrännor samtidigt som taket i Spånga?","Ja, vi rekommenderar ofta att byta avvattning och taksäkerhet i samma projekt för ett komplett och långsiktigt resultat."),
   ]},
 "Sollentuna": {
   "intro": "Sollentuna norr om Stockholm har omfattande villabebyggelse. Vi är takläggare i Sollentuna för villor i bland annat Edsberg, Helenelund, Tureberg och Viby.",
   "paras": [
     "Sollentuna norr om Stockholm har omfattande villabebyggelse i områden som Edsberg, Helenelund, Tureberg, Viby och Norrviken. Husen varierar från äldre villor till moderna, och de trädnära, ibland kuperade lägena påverkar hur taken slits.",
     "Många villor i Sollentuna ligger nära skog och stora träd, vilket ger mer mossa, löv i hängrännor och skuggiga takytor som håller kvar fukt. Här är taktvätt, rensning av avvattning och kontroll av norrvända ytor ofta lika viktigt som själva takbytet.",
     "Snölaster är också en faktor i Sollentuna, särskilt på större tak, och vi ser gärna över taksäkerhet och snörasskydd i samband med ett byte. Vi når Sollentuna smidigt och planerar projekten efter husets läge och exponering.",
   ],
   "items": ["Villatak i Edsberg, Helenelund, Tureberg, Viby.","Taktvätt och avvattning för trädnära, skuggiga tak.","Snörasskydd och taksäkerhet vid snölaster."],
   "faq": [
     ("Mitt tak i Sollentuna är mossigt och skuggigt – vad gör ni?","Skuggiga, trädnära tak håller kvar fukt och drar åt sig mossa. Vi tvättar skonsamt, rensar avvattningen och kan förebygga ny påväxt – och bedömer om taket samtidigt behöver åtgärdas."),
     ("Behöver jag snörasskydd i Sollentuna?","På många tak, särskilt över entréer och gångytor, är snörasskydd klokt med tanke på snölasterna. Vi ser över taksäkerheten vid besiktning."),
     ("Vilka delar av Sollentuna arbetar ni i?","Hela kommunen – bland annat Edsberg, Helenelund, Tureberg, Viby och Norrviken."),
   ]},
 "Järfälla": {
   "intro": "Järfälla med Jakobsberg, Kallhäll och Viksjö är ett växande villaområde nordväst om Stockholm. Vi hjälper villaägare i Järfälla med takbyte, takrenovering och plåtarbeten.",
   "paras": [
     "Järfälla nordväst om Stockholm växer snabbt och har stora villaområden i Jakobsberg, Kallhäll, Viksjö och Barkarby. Särskilt Viksjö byggdes ut kraftigt under 1970- och 80-talet, och många av dessa tak når nu en ålder där byte eller omläggning är aktuellt.",
     "I Viksjö och Kallhäll ser vi ofta slitna betongpannor och uttjänt underlagspapp på hus av liknande årgång – ibland hela gaturader med samma behov. Det gör att vi kan planera effektivt och ge tydliga besked om vad som behöver göras.",
     "Vi hjälper Järfällas villaägare med allt från punktinsatser mot läckage till kompletta takbyten med ny avvattning och taksäkerhet. Barkarbys expansion innebär också nyare bebyggelse där vi utför plåtarbeten och detaljlösningar.",
   ],
   "items": ["Villatak i Jakobsberg, Kallhäll, Viksjö, Barkarby.","Byte av mogna 70–80-talstak.","Betongpannor, plåt och ny avvattning."],
   "faq": [
     ("Många hus i Viksjö har samma ålder – kan ni ge pris snabbt?","Ofta går det snabbt. Eftersom bebyggelsen är enhetlig känner vi igen konstruktionerna väl, men vi ger alltid fast pris efter ett platsbesök."),
     ("Vilka områden i Järfälla arbetar ni i?","Hela Järfälla, bland annat Jakobsberg, Kallhäll, Viksjö och Barkarby."),
     ("Mina betongpannor i Kallhäll är från 80-talet – hur länge håller de?","Betongpannor håller ofta 30–50 år, men underlagspappen har kortare liv. Efter 40 år är det klokt att låta besikta både pannor och underlag."),
   ]},
 "Täby": {
   "intro": "Täby nordost om Stockholm är ett av regionens största villaområden. Vi är takläggare i Täby för villor i bland annat Näsbypark, Gribbylund, Viggbyholm och Roslags-Näsby.",
   "paras": [
     "Täby nordost om Stockholm är ett av regionens största villaområden, med stadsdelar som Näsbypark, Gribbylund, Viggbyholm, Roslags-Näsby och Skarpäng. Bebyggelsen spänner från äldre, påkostade villor till moderna hus, vilket ställer olika krav på takarbetet.",
     "I Näsbypark och Viggbyholm finns många större, arkitektoniskt påkostade villor där takets uttryck och detaljer är viktiga – valmade tak, takkupor och synlig plåt kräver erfarenhet och noggrant hantverk. I nyare områden som Gribbylund och Arninge är taken ofta enklare men med moderna materialkrav.",
     "Vi anpassar alltid material och lösningar efter husets karaktär och ålder, och lägger stor vikt vid täta anslutningar och snygga plåtdetaljer. Täby når vi smidigt och vi planerar projekten efter husets stil och läge.",
   ],
   "items": ["Villatak i Näsbypark, Gribbylund, Viggbyholm.","Varsamt takbyte på påkostade villor med valmade tak.","Anpassat materialval och detaljerade plåtarbeten."],
   "faq": [
     ("Kan ni hantera påkostade villatak i Näsbypark?","Ja, vi är vana vid större villor med valmade tak, kupor och detaljerade plåtarbeten där både täthet och utseende måste bli rätt."),
     ("Vilka delar av Täby arbetar ni i?","Hela Täby, bland annat Näsbypark, Gribbylund, Viggbyholm, Roslags-Näsby och Skarpäng."),
     ("Vi har ett modernt hus i Gribbylund – tar ni mindre takjobb också?","Ja, allt från punktinsatser och plåtdetaljer till kompletta byten – oavsett husets ålder."),
   ]},
 "Danderyd": {
   "intro": "Danderyd med Djursholm, Stocksund och Enebyberg har några av regionens mest påkostade villor. Vi är takläggare i Danderyd för takbyte, takrenovering och plåtarbeten på villatak.",
   "paras": [
     "Danderyd med Djursholm, Stocksund, Enebyberg och Danderyds villastad har några av Stockholmsregionens mest påkostade villor. Här är taken ofta stora och komplexa, med torn, valmar, kupor och detaljerade plåtarbeten som kräver van hand.",
     "Djursholms sekelskiftesvillor har ofta kulturhistoriskt värde där husets uttryck måste bevaras vid takbyte – rätt val av tegel eller plåt och ett varsamt utförande är avgörande. Samtidigt moderniserar vi underlag, tätskikt och avvattning så att taket blir tätt för lång tid framåt.",
     "Komplexa tak innebär fler anslutningar och riskpunkter, och vi lägger särskild vikt vid plåt kring skorstenar, takfönster och genomföringar. Vi arbetar noggrant och dokumenterat, vilket passar den här typen av fastigheter.",
   ],
   "items": ["Villatak i Djursholm, Stocksund, Enebyberg.","Erfarenhet av komplexa tak med torn, valmar och kupor.","Detaljerade, dokumenterade plåtarbeten."],
   "faq": [
     ("Har ni erfarenhet av Djursholms äldre, komplexa villatak?","Ja. Vi arbetar med torn, valmar, kupor och detaljerad plåt, och kombinerar bevarat uttryck med moderna, täta lösningar."),
     ("Kan husets karaktär bevaras vid takbyte i Djursholm?","Absolut – vi väljer material och kulörer som bevarar sekelskiftesvillans stil och utför arbetet varsamt."),
     ("Vilka områden i Danderyd arbetar ni i?","Hela Danderyd, bland annat Djursholm, Stocksund, Enebyberg och Danderyds villastad."),
   ]},
 "Lidingö": {
   "intro": "Lidingö är en ö öster om Stockholm med stor villabebyggelse. Vi hjälper villaägare på Lidingö i bland annat Lidingö villastad, Brevik, Sticklinge och Käppala med takbyte och plåtarbeten.",
   "paras": [
     "Lidingö är en ö öster om Stockholm med stor och varierad villabebyggelse i områden som Lidingö villastad, Mölna, Sticklinge, Käppala och Brevik. Det havsnära läget präglar både husen och deras tak.",
     "Den salta, fuktiga havsluften ställer extra krav på plåt, beslag och infästningar – korrosion är betydligt vanligare här än inåt land. Vi väljer material, ytbehandling och rostskydd som klarar Lidingös kustklimat och ser noga över plåtdetaljer och avvattning.",
     "Många villor på Lidingö har utsatta lägen med både vind och sol, vilket sliter på ytskikt. Vid takbyte och plåtarbeten här prioriterar vi korrosionsbeständiga lösningar och täta anslutningar för lång livslängd.",
   ],
   "items": ["Villatak i Lidingö villastad, Brevik, Käppala.","Materialval och rostskydd för salt havsluft.","Plåttak och korrosionsbeständiga lösningar."],
   "faq": [
     ("Varför är plåt extra utsatt på Lidingö?","Den salta havsluften påskyndar korrosion. Vi väljer korrosionsbeständig plåt och rätt ytbehandling så att taket håller trots kustklimatet."),
     ("Vilka delar av Lidingö arbetar ni i?","Hela Lidingö, bland annat Lidingö villastad, Mölna, Sticklinge, Käppala och Brevik."),
     ("Kan ni rostskydda och måla befintligt plåttak på Lidingö?","Ja, om konstruktionen är sund kan tvätt, rostskydd och målning förlänga takets liv – ett kostnadseffektivt alternativ till byte."),
   ]},
 "Nacka": {
   "intro": "Nacka öster om Stockholm har omfattande villabebyggelse i bland annat Saltsjöbaden, Boo, Älta och Fisksätra. Vi är takläggare i Nacka för takbyte, takrenovering och takbesiktning.",
   "paras": [
     "Nacka öster om Stockholm har omfattande villabebyggelse i bland annat Saltsjöbaden, Boo, Älta, Fisksätra och Nacka strand. Terrängen är ofta kuperad och kustnära, vilket påverkar både hus och tak.",
     "Saltsjöbadens äldre, ofta stora villor har varierade tak med både tegel och plåt, och det kustnära läget innebär salt luft och väderexponering som sliter på ytskikt och plåt. I Boo och Älta finns en blandning av äldre och nyare hus med skiftande takbehov.",
     "Vi anpassar åtgärder efter husets ålder, läge och exponering, och lägger vikt vid korrosionsbeständiga plåtlösningar och god avvattning på de kustnära taken. Nacka når vi via goda förbindelser och planerar projekten efter tomtens förutsättningar.",
   ],
   "items": ["Villatak i Saltsjöbaden, Boo, Älta, Fisksätra.","Erfarenhet av stora, äldre villatak i tegel och plåt.","Kustnära, korrosionsbeständigt materialval."],
   "faq": [
     ("Har ni erfarenhet av stora villatak i Saltsjöbaden?","Ja, vi arbetar med äldre, stora villor som ofta har komplexa tak i både tegel och plåt, och anpassar lösningarna efter det kustnära läget."),
     ("Vilka delar av Nacka arbetar ni i?","Hela Nacka, bland annat Saltsjöbaden, Boo, Älta, Fisksätra och Nacka strand."),
     ("Påverkar det kustnära läget mitt tak i Nacka?","Ja, salt luft och väder sliter mer på plåt och ytskikt. Vi väljer korrosionsbeständiga material och ser extra noga över avvattning."),
   ]},
}
# Fördjupning per ort (2026-10-05): 2 unika sektioner + 3 extra FAQ.
# Håll texten lokal och specifik – inga mallade stycken där bara ortnamnet byts.
LOC_EXTRA = {
 "Sundbyberg": {
   "secs": [
     ("Vanliga tak och problem i Sundbyberg", [
       "I Duvbo och Storskogen är de flesta villor byggda mellan 1910- och 1940-talet. Typiskt är branta sadel- och brutna tak med lertegel, ofta med takkupor och detaljrika vindskivor. Teglet håller länge, men underlagspappen från förra omläggningen – ofta på 1960–70-talet – är nu spröd. Vanliga skador är läckage vid kupornas anslutningar och vid skorstenar som murats om i omgångar.",
       "Lilla Alby och Ör har fler hus från 1940–60-talet med betongpannor och enklare takformer. Här ser vi ofta vittrade pannor på norrsidan, mossa som lyfter pannorna och hängrännor som sätts igen av de stora träden i villaträdgårdarna. På radhus och parhus är plåtdetaljerna mellan husen en återkommande läckagepunkt."]),
     ("Planera takprojektet i Sundbyberg", [
       "Gatorna i Duvbo är smala och tomterna ofta trånga, så ställning, container och materialleveranser behöver planeras i förväg. Vi lägger upp etableringen så att grannar och infarter störs så lite som möjligt.",
       "Ett takbyte på villa kräver normalt inget bygglov sedan 1 december 2025. Duvbo är däremot utpekat som kulturhistoriskt värdefullt, där lovplikten kan finnas kvar – vill du byta material eller kulör, stäm av med Sundbybergs stad först. Vi hjälper dig ta fram underlag om det behövs."]),
   ],
   "faq": [
     ("Vilka tak är vanligast i Duvbo?","Branta tak med lertegel på villor från 1910–40-talet, ofta med takkupor. Teglet är ofta i gott skick medan underlagspappen behöver bytas."),
     ("Kan ni ställa ställning på smala gator i Duvbo?","Ja, vi planerar ställning och leveranser efter tomten och gatan så att grannar och infarter påverkas minimalt."),
     ("Gör ni takbesiktning i Sundbyberg?","Ja, och eftersom vi utgår från Bromma kan vi oftast komma ut inom några dagar."),
   ]},
 "Solna": {
   "secs": [
     ("Vanliga tak och problem i Solna", [
       "I Råsunda villastad finns många villor och mindre flerfamiljshus från 1920–40-talet med tegeltak. Pannorna har ofta lång livslängd kvar, men läkten och underlagspappen är uttjänta – ett typiskt fall för takomläggning snarare än nytt tak.",
       "I Bergshamra by och Stocksundstorp finns villor från olika tider, flera med lägre taklutning där plåt och papp är vanligare. Låglutande tak är känsligare för läckage i skarvar och genomföringar, och här lönar det sig att regelbundet kontrollera plåtdetaljer och avvattning. Närheten till Brunnsviken och Ulriksdals grönområden ger också mer löv och påväxt på taken."]),
     ("Planera takprojektet i Solna", [
       "Solna har en blandning av äldre villor och tät stadsbebyggelse. På tomter nära gata planerar vi ställning och avspärrning så att arbetet går säkert, och vid behov hjälper vi till med tillstånd för att ställa container på allmän mark.",
       "I Solna krävs bygglov för att byta takmaterial inom detaljplan, och de flesta områden har detaljplan, enligt <a class=\"text-link\" href=\"https://www.solna.se/bygga-bo--miljo/bygga/bygglov/bygglovsfria-atgarder\" rel=\"noopener\">Solna stad</a>. Samma pannor på nytt underlag ändrar inte utseendet – stäm av med Solna stad innan arbetet planeras."]),
   ],
   "faq": [
     ("Är takomläggning vanligt i Råsunda?","Ja. Många tegeltak i Råsunda villastad har hela pannor men slitet underlag, och då är omläggning ofta det mest lönsamma."),
     ("Hur ofta ska ett låglutande tak i Stocksundstorp kontrolleras?","Minst en gång per år, helst efter vintern. Skarvar, genomföringar och avvattning är de vanligaste läckagepunkterna."),
     ("Behöver jag bygglov för att byta från tegel till plåt i Solna?","Ja, i regel. Solna stad kräver bygglov för byte av takmaterial inom detaljplan, och det gäller de flesta områden i Solna."),
   ]},
 "Bromma": {
   "secs": [
     ("Vanliga tak och problem i Bromma", [
       "Bromma har några av Stockholms mest välbevarade villaområden. I trädgårdsstäderna Ängby, Äppelviken, Ålsten och Smedslätten är många hus från 1920–40-talet, ofta med branta tak i lertegel eller med falsad plåt. Funkisvillorna från 1930-talet i Södra Ängby har låga, ibland nästan platta tak med papp eller plåt, som kräver noggrant tätskikt och bra avvattning.",
       "De stora, gamla trädgårdarna är Brommas charm men också en utmaning för taken: löv och barr sätter igen hängrännor, och skuggiga takfall får mossa som håller kvar fukt. Vi ser ofta att läckage börjar vid ränndalar och skorstenar där löv har samlats."]),
     ("Planera takprojektet i Bromma", [
       "Sedan 1 december 2025 är byte av takmaterial och kulör på villor i regel lovfritt. I riksintressena Ängby, Olovslund och Ålstensgatan, för blå- eller grönmärkta hus och vid skyddsbestämmelser krävs dock fortfarande bygglov, enligt <a class=\"text-link\" href=\"https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/\" rel=\"noopener\">Stockholms stad</a>. Höjs taket kan det räknas som tillbyggnad. Stäm av med stadsbyggnadskontoret i Stockholm – vi hjälper dig med underlag och materialval som passar området.",
       "Eftersom vi utgår från Abrahamsberg i Bromma kan vi göra besiktning med kort varsel och följa projektet på plats varje dag. Det gör det enkelt att stämma av detaljer under arbetets gång."]),
   ],
   "faq": [
     ("Lägger ni plåttak på funkisvillor i Bromma?","Ja, falsad plåt och papptak på låglutande funkistak hör till våra vanliga uppdrag. Rätt tätskikt och avvattning är avgörande på låga taklutningar."),
     ("Behöver jag bygglov för takbyte i Äppelviken?","Normalt inte. Är huset blå- eller grönmärkt hos Stadsmuseet eller har skyddsbestämmelser i detaljplanen krävs lov – stäm av med Stockholms stad."),
     ("Rensar ni hängrännor samtidigt som ni byter tak?","Ja, och vi rekommenderar ofta lövskydd eller större rännor i Brommas trädrika områden."),
   ]},
 "Spånga": {
   "secs": [
     ("Vanliga tak och problem i Spånga", [
       "Bromsten och Solhem byggdes till stor del ut under 1900-talets första hälft och har många äldre trävillor med tegel- eller betongtak. I Sundby och Flysta dominerar villor från 1950–70-talet med betongpannor, där pannornas yta har vittrat och underlagspappen är i slutet av sin livslängd.",
       "Typiska problem är porösa betongpannor som suger vatten, mossa på norrsidan och läckage vid skorstenar och ventilationshuvar. Många hus har också fått tilläggsisolering på vinden, vilket kan göra taket kallare och mer känsligt för fukt om ventilationen vid takfoten inte fungerar."]),
     ("Planera takprojektet i Spånga", [
       "Spångas villatomter är oftast rymliga, vilket gör det enkelt att ställa ställning och container. Det håller nere kostnaden för etablering jämfört med tätare områden.",
       "Vid takbyte på ett 60–70-talshus passar det bra att samtidigt se över hängrännor, stuprör, snörasskydd och takstege. Då blir taket komplett och godkänt för sotare och framtida underhåll."]),
   ],
   "faq": [
     ("Är betongpannorna på mitt 60-talshus i Spånga slut?","Inte nödvändigtvis. Är de porösa eller frostskadade bör de bytas, annars kan en omläggning med nytt underlag räcka. En besiktning ger svar."),
     ("Ska man tilläggsisolera vinden samtidigt som taket byts?","Det kan vara klokt, men ventilationen vid takfoten måste fungera. Vi ser över det i samband med takbytet."),
     ("Arbetar ni i Tensta och Hässelby också?","Ja, vi arbetar i hela västerort, inklusive Hässelby, Vällingby och Tensta."),
   ]},
 "Sollentuna": {
   "secs": [
     ("Vanliga tak och problem i Sollentuna", [
       "Sollentuna har stora villaområden från 1960–70-talet i bland annat Edsberg, Helenelund och Häggvik, medan Tureberg är en villastad från 1910. Många av dessa hus har betongpannor och underlagspapp som nu är 50 år gamla – den vanligaste orsaken till att vi kommer till Sollentuna är just takbyte eller takomläggning på hus från den här epoken.",
       "Rotebro och Vaxmora har fler äldre villor och sekelskifteshus med branta tegeltak. Sollentuna är också trädrikt, och skuggiga tak under tall och gran får ofta kraftig mossa som lyfter pannorna och sätter igen hängrännorna."]),
     ("Planera takprojektet i Sollentuna", [
       "Har flera hus i samma område samma ålder är det vanligt att grannar byter tak inom några år. Planerar ni samtidigt kan etablering och ställning samordnas.",
       "Att byta från betong till plåt eller byta kulör kräver normalt inget bygglov för villor sedan 1 december 2025. Har ditt område skyddsbestämmelser i detaljplanen gäller lovplikt – kontrollera med Sollentuna kommun."]),
   ],
   "faq": [
     ("Hur gamla är taken i Edsberg och Häggvik?","Många är från 1960–70-talet med originalunderlag. Efter 50 år är det oftast dags för omläggning eller byte."),
     ("Kan flera grannar byta tak samtidigt?","Ja, och det kan spara på etablering och planering. Hör av er så tittar vi på husen samtidigt."),
     ("Tvättar ni tak i Sollentuna?","Ja, taktvätt och mossbehandling är vanligt i Sollentunas trädrika områden."),
   ]},
 "Järfälla": {
   "secs": [
     ("Vanliga tak och problem i Järfälla", [
       "Järfälla har stora villa- och radhusområden från 1960–80-talet i Jakobsberg, Viksjö, Barkarby och Kallhäll. Radhusen har ofta låglutande tak med papp eller betongpannor, och de gemensamma plåtdetaljerna mellan husen är en vanlig läckagepunkt.",
       "I Viksjö och Kallhäll ligger många hus nära skog, vilket ger mer påväxt och fuktiga tak. Vi ser ofta att takfoten har för dålig ventilation, vilket ger fukt och mögel på vinden även när själva taket är tätt."]),
     ("Planera takprojektet i Järfälla", [
       "Byter flera hus samtidigt blir resultatet enhetligt och anslutningarna mellan husen kan göras om ordentligt.",
       "Material- och kulörbyte på radhus och villor kräver normalt inget bygglov. Skyddade hus kräver lov – stäm av med Järfälla kommun vid osäkerhet."]),
   ],
   "faq": [
     ("Byter ni tak på radhus i Järfälla?","Ja, både enskilda radhus och hela längor. Anslutningarna mellan husen är viktiga att göra rätt."),
     ("Varför luktar det mögel på vinden fast taket är tätt?","Ofta på grund av dålig ventilation vid takfoten. Vi kan se över ventilationen i samband med besiktning."),
     ("Arbetar ni i Kallhäll och Viksjö?","Ja, i hela Järfälla kommun."),
   ]},
 "Täby": {
   "secs": [
     ("Vanliga tak och problem i Täby", [
       "Täby växte snabbt under 1960–70-talet, och många villor och radhus i Näsby Park, Ensta och Hägernäs är från den tiden, medan Gribbylund mest byggdes ut på 1970- och 80-talet. Betongpannor och papptak dominerar, och underlagspappen är nu ofta i slutet av sin livslängd.",
       "Näsby Park har även äldre villor från 1920-talet med tegeltak. Nära Stora Värtan i Hägernäs och Näsby Park är taken mer utsatta för vind, vilket ställer krav på infästning av pannor, nock och plåtdetaljer."]),
     ("Planera takprojektet i Täby", [
       "Många radhusområden i Täby förvaltas av samfälligheter med egna regler för tak och kulör. Kontrollera vad som gäller innan du väljer material – vi hjälper dig med underlag till föreningen.",
       "Även byte till plåt eller ny kulör kräver normalt inget bygglov för villor och radhus sedan 1 december 2025. Undantag är hus med skyddsbestämmelser – stäm av med Täby kommun om du är osäker."]),
   ],
   "faq": [
     ("Är betongtaken i Gribbylund dags att byta?","Många är från 1970–80-talet med originalunderlag. En besiktning visar om omläggning räcker eller om pannorna också behöver bytas."),
     ("Hjälper ni samfälligheter i Täby?","Ja, vi lämnar offert och underlag för hela radhuslängor eller områden."),
     ("Klarar taket vinden nära Stora Värtan?","Med rätt infästning av pannor, nock och plåt ja. Vi anpassar infästningen efter läget."),
   ]},
 "Danderyd": {
   "secs": [
     ("Vanliga tak och problem i Danderyd", [
       "Djursholm, Stocksund och Enebyberg har många större villor från tidigt 1900-tal med komplexa tak: flera takfall, kupor, torn och ränndalar. Lertegel och falsad plåt är vanligast. Komplexa tak har fler anslutningar – och fler ställen där läckage kan uppstå, särskilt i ränndalar och vid kupor.",
       "Danderyds stora tomter med gamla ekar och tallar ger mycket löv och barr i rännorna och skuggiga takfall med påväxt. Kopparplåt och zink förekommer på äldre hus och kräver plåtslagare med erfarenhet av traditionella material."]),
     ("Planera takprojektet i Danderyd", [
       "Delar av Djursholm och Stocksund har detaljplaner med skyddsbestämmelser. Där krävs bygglov även för material-, kulör- och detaljändringar, trots att fasadändringar på villor annars blev lovfria 1 december 2025. Stäm av med Danderyds kommun först.",
       "Stora villor kräver ofta mer ställning och längre byggtid. Vi lägger upp en tidplan med etapper så att huset är tätt varje kväll och arbetet störs så lite som möjligt av väder."]),
   ],
   "faq": [
     ("Kan ni lägga tak på stora villor med många takfall i Djursholm?","Ja, komplexa tak med kupor, ränndalar och flera takfall är en vanlig typ av uppdrag."),
     ("Behöver jag bygglov för takbyte i Djursholm?","Inte vid byte till samma material och utseende. Har huset skyddsbestämmelser krävs lov vid ändringar – stäm av med Danderyds kommun."),
     ("Hur lång tid tar ett takbyte på en större villa?","Ofta två till fyra veckor beroende på storlek, takets form och väder."),
   ]},
 "Lidingö": {
   "secs": [
     ("Vanliga tak och problem på Lidingö", [
       "Lidingö har allt från villor från 1905–1930 i Lidingö villastad och Brevik till nybyggda hus i Gåshaga från 2000-talet. Äldre hus har ofta tegel eller falsad plåt, medan nyare villor har betongpannor eller plåt.",
       "Läget vid vattnet påverkar taken. Salt luft från Saltsjön och Lilla Värtan påskyndar korrosion på plåt, skruvar och beslag, och vinden från vattnet ställer krav på infästning. Vi väljer korrosionsbeständig plåt och fästelement för havsnära hus."]),
     ("Planera takprojektet på Lidingö", [
       "Många tomter på Lidingö är kuperade och ligger i slänt, vilket påverkar hur ställning och lift kan placeras. Vi gör alltid ett platsbesök innan vi planerar etableringen.",
       "Takbyte på villa kräver normalt inget bygglov, även med nytt material. Delar av Lidingö är dock värdefulla kulturmiljöer där lovplikten finns kvar – stäm av med Lidingö stad."]),
   ],
   "faq": [
     ("Rostar plåttak snabbare på Lidingö?","Havsnära hus utsätts för mer salt och fukt. Med rätt plåt, ytbeläggning och underhåll håller ett plåttak ändå länge."),
     ("Kan ni arbeta på kuperade tomter?","Ja, vi planerar ställning eller lift efter tomten vid ett platsbesök."),
     ("Arbetar ni på hela Lidingö?","Ja, bland annat i Käppala, Lidingö villastad, Brevik, Gåshaga och Mölna."),
   ]},
 "Nacka": {
   "secs": [
     ("Vanliga tak och problem i Nacka", [
       "Saltsjöbaden har många stora villor från tidigt 1900-tal med komplexa tak i tegel och plåt, medan Boo har sommarvillor från 1860-talet och framåt och Älta egnahem från tidigt 1900-tal och radhus från slutet av 1960-talet. Fisksätra och Nacka strand har mer flerbostadshus.",
       "Det kustnära läget med salt luft och hård vind sliter på plåtdetaljer, skruvar och infästningar. I skogsnära delar av Boo och Älta får taken mycket barr och påväxt. Vi ser ofta läckage vid skorstenar och genomföringar där plåten har korroderat."]),
     ("Planera takprojektet i Nacka", [
       "Många tomter i Nacka ligger i kuperad terräng och på berg, vilket påverkar ställning och materialhantering. Vi gör alltid platsbesök innan vi lämnar kostnadsförslag.",
       "Material- och kulörbyte på villatak är normalt lovfritt. Saltsjöbaden har delvis skyddsbestämmelser för äldre villor, och där krävs lov – stäm av med Nacka kommun."]),
   ],
   "faq": [
     ("Vilken plåt passar havsnära hus i Saltsjöbaden?","Korrosionsbeständig plåt med kraftig ytbeläggning och rostfria fästelement. Vi anpassar valet efter läget."),
     ("Tvättar ni tak i Boo och Älta?","Ja, taktvätt och mossbehandling är vanligt i skogsnära delar av Nacka."),
     ("Kan ni byta tak på hus i brant terräng?","Ja, vi planerar ställning och lift efter tomten vid ett platsbesök."),
   ]},
}

ORT_IMG = {
 "Bromma": ("ort-bromma-villa","Villa med rött tegeltak i en av Brommas trädgårdsstäder"),
 "Sundbyberg": ("ort-sundbyberg-villa","Äldre trävilla med brant tegeltak och takkupa, typisk för Duvbo"),
 "Danderyd": ("ort-danderyd-villa","Stor stenvilla med svart plåttak, kupor och torn, typisk för Djursholm"),
 "Sollentuna": ("ort-sollentuna-villa","70-talsvilla med betongpannor och mossa på norrsidan bland tallar"),
 "Solna": ("ort-solna-villa","Mindre 40-talsvilla med tegeltak i Solna"),
 "Täby": ("ort-taby-radhus","Radhuslänga från 70-talet med låglutande svarta tak"),
 "Spånga": ("ort-spanga-villa","60-talsvilla i tegel med bruna betongpannor"),
 "Nacka": ("ort-nacka-villa","Havsnära villa på berg med plåttak, typisk för Saltsjöbaden"),
}
LOC.update(LOC_NEW)
LOC_EXTRA.update(LOC_EXTRA_NEW)
LOC.update(LOC_X)
LOC_EXTRA.update(LOC_EXTRA_X)
LOC.update(LOC_V30)
LOC_EXTRA.update(LOC_EXTRA_V30)
ORT_IMG.update({k: v for k, v in ORT_IMG_NEW.items()
                if os.path.exists(os.path.join(ROOT, "assets", "images", v[0] + ".webp"))})
# GSC near-miss (28 d t.o.m. 2026-10-11): egna title/description + en tjänstesektion
# för orter där tjänstesökord (takbyte/takrenovering/omläggning + ort) ligger på pos 15–30.
# title <= 65, description <= 155 tecken. Övriga orter använder mallen nedan.
ORT_SEO = {
 "Danderyd": {
   "title": "Takläggare i Danderyd & Djursholm – takbyte, takrenovering",
   "desc": "Takbyte, takrenovering och takreparation i Danderyd, Djursholm och Stocksund. Gratis besök, fast pris och ROT-avdrag direkt på fakturan.",
   "svc": ("Takbyte och takrenovering i Danderyd", [
     f"De flesta som hör av sig från Danderyd står inför samma val: räcker det att renovera taket, eller är det dags att byta? På äldre villor i Djursholm och Stocksund är teglet ofta i gott skick medan underlagspappen är uttjänt. Då kan en {a('takrenovering.html','takrenovering eller takomläggning')} räcka – pannorna tas ner, nytt underlag läggs och samma pannor läggs tillbaka.",
     f"Är både pannor och underlag slut blir ett {a('takbyte.html','takbyte på villan')} mer lönsamt i längden. Läcker det redan? Läs vad du gör vid {a('taklackage.html','takläckage')}."]),
   "faq": [("Gör ni takreparationer och lagar läckage i Danderyd?","Ja. Vi lagar läckage kring skorstenar, kupor och ränndalar och byter enstaka pannor och plåtdetaljer. Vid besöket bedömer vi om en reparation räcker eller om taket behöver renoveras.")]},
 "Sundbyberg": {
   "title": "Takläggare i Sundbyberg – takbyte, takrenovering & plåt",
   "desc": "Takläggare i Sundbyberg: takbyte, takrenovering och plåtarbeten i Duvbo och Storskogen. Granne med vår bas i Bromma. Gratis besök och fast pris.",
   "svc": ("Takbyte, takrenovering och plåtarbeten i Sundbyberg", [
     f"I Duvbo och Storskogen handlar många uppdrag om {a('takrenovering.html','takrenovering')}: det gamla lertegelet sitter kvar, men underlagspapp och läkt byts. Är pannorna spruckna eller porösa gör vi i stället ett komplett {a('takbyte.html','takbyte')} med nytt underlag, nya pannor och nya plåtdetaljer.",
     f"Plåtarbeten är en stor del av jobben i Sundbyberg – skorstensbeslag, vindskivor, fotplåt och anslutningar mellan radhus och parhus. Vi lägger även nya {a('plattak.html','plåttak')} på låglutande tak och byter {a('hangrannor-stupror.html','hängrännor och stuprör')} i samma omgång."])},
 "Spånga": {
   "title": "Takläggare i Spånga – takbyte, takrenovering & omläggning",
   "desc": "Takläggare i Spånga, Bromsten och Solhem: takbyte, takrenovering och takomläggning på villa. Gratis besök, fast pris och ROT-avdrag på fakturan.",
   "svc": ("Takrenovering och takomläggning i Spånga", [
     f"Är pannorna fortfarande hela räcker ofta en takomläggning: pannorna lyfts av, ny underlagspapp och ny läkt läggs och hela pannor läggs tillbaka. Det är en form av {a('takrenovering.html','takrenovering')} som ger ett tätt tak för lång tid framåt till lägre kostnad än ett nytt tak.",
     f"Är betongpannorna porösa eller frostskadade räcker inte en omläggning – då gör vi ett {a('takbyte.html','takbyte')}. Osäker på vilket som gäller ditt hus? Läs {a('takbyte-eller-takrenovering.html','takbyte eller takrenovering')} eller boka en {a('takbesiktning.html','takbesiktning')}."])},
 "Solna": {
   "title": "Takläggare i Solna – takrenovering & takbyte på villa",
   "desc": "Takläggare i Solna: takrenovering, takomläggning och takbyte i Råsunda, Råsta och Stocksundstorp. Gratis besök, fast pris och ROT-avdrag.",
   "svc": ("Takrenovering i Solna", [
     f"Vid en {a('takrenovering.html','takrenovering')} byter vi underlagspapp och läkt och lägger tillbaka samma pannor. Samtidigt ser vi över plåtdetaljer, vindskivor och genomföringar, så att hela taket håller lika länge.",
     f"Är pannorna slut gör vi ett {a('takbyte.html','takbyte')} med nya pannor, nytt underlag och nya plåtdetaljer. Vi börjar alltid med ett gratis besök och ger fast pris på den åtgärd taket faktiskt behöver."])},
 "Sollentuna": {
   "title": "Takläggare i Sollentuna – takbyte, takrenovering & taktvätt",
   "desc": "Takfirma i Sollentuna: byta tak, takrenovering, takomläggning och taktvätt i Edsberg, Tureberg och Rotebro. Gratis besök, fast pris och ROT.",
   "svc": ("Byta tak eller lägga om taket i Sollentuna", [
     f"När ett 60- eller 70-talstak i Sollentuna börjar läcka är frågan oftast om det räcker att lägga om eller om det är dags att byta tak. Är betongpannorna hela och har inte sugit fukt kan en {a('takrenovering.html','takomläggning')} ge ett tätt tak för lång tid: pannorna tas ner, ny underlagspapp och läkt läggs och pannorna läggs tillbaka.",
     f"Har pannorna vittrat eller spruckit i frost gör vi i stället ett komplett {a('takbyte.html','takbyte')}, med nya pannor eller plåt. Är taket bara mossigt men i övrigt helt räcker ofta en {a('taktvatt.html','taktvätt med mossbehandling')}. Vid besöket får du besked om vilken nivå ditt tak behöver."]),
   "faq": [("Vad är skillnaden på att byta tak och lägga om taket?","Vid en takomläggning återanvänds pannorna och underlagspapp och läkt byts. Vid ett takbyte byts även pannorna, eller så går du över till plåt.")]},
 "Täby": {
   "title": "Takläggare i Täby – takbyte, takomläggning & takrenovering",
   "desc": "Takläggare i Täby: byta tak, takomläggning och takrenovering på villor och radhus i Näsby Park, Gribbylund och Ensta. Gratis besök och ROT-avdrag.",
   "svc": ("Takbyte och takomläggning i Täby", [
     f"På villor med betongpannor där pannorna fortfarande är hela räcker ofta en {a('takrenovering.html','takomläggning')}: nytt underlag och ny läkt, samma pannor. Har pannorna börjat vittra blir ett {a('takbyte.html','takbyte')} med nya pannor eller ett {a('plattak.html','plåttak')} mer lönsamt i längden.",
     f"För radhus lämnar vi offert per hus eller för hela längan, så att plåt och anslutningar mellan husen görs om i samma omgång. Vill du först veta vad taket behöver bokar du en {a('takbesiktning.html','takbesiktning')}, och vad ett nytt tak kan kosta går vi igenom i {a('vad-kostar-takbyte.html','vad kostar ett takbyte')}."]),
   "faq": [("Vad kostar det att byta tak i Täby?","Det beror på takets storlek, material, lutning och underlagets skick. Vi kommer ut gratis och ger ett fast pris med ROT-avdraget uträknat.")]},
 "Bromma": {
   "title": "Takläggare i Bromma – takbyte i Mariehäll, Nockeby & Ängby",
   "desc": "Takbyte och takrenovering i Brommas villaområden: Mariehäll, Nockeby, Ängby, Äppelviken och Ålsten. Vår bas ligger i Bromma. Gratis besök.",
 },
}

# Keyword Planner 2025-10..2026-09: "takrenovering <ort>" 10–100/mån. Sedan 2026-10-25 har
# varje ort en egen lång sida (TRP_FILES); här står bara 1–2 meningar + länk, så att texten
# inte dupliceras. Solna: sektionen "Takrenovering i Solna" (ORT_SEO) får bara denna text.
# Danderyd: texten läggs in i "Takbyte och takrenovering i Danderyd".
_TR, _TK = "takrenovering.html", "vad-kostar-takrenovering.html"
def _trl(o, t): return a(TRP_FILES[o], t)
TAKRENO_MERGE = {"Danderyd"}
TAKRENO = {
 "Bromma": [f"Trädgårdsstädernas tegeltak och funkisvillornas låga tak kräver olika slags renovering. Hur vi går tillväga, vilka regler som gäller och hur ROT räknas läser du på sidan om {_trl('Bromma','takrenovering i Bromma')}."],
 "Solna": [f"Villaområdena i Solna är få men kulturhistoriskt känsliga, från Råsunda till Stocksundstorp – vad en renovering omfattar där och vilka regler som gäller går vi igenom under {_trl('Solna','takrenovering i Solna')}."],
 "Nacka": [f"Saltluft, berg och skog ställer olika krav på taken i Nacka. Läs mer om material, arbetsgång och bygglovsfrågor under {_trl('Nacka','takrenovering i Nacka')}."],
 "Täby": [f"Från villorna i Näsbypark och Viggbyholm till typhusen i Gribbylund – så planerar du en renovering av taket i Täby, steg för steg, på sidan om {_trl('Täby','takrenovering i Täby')}."],
 "Danderyd": [f"Hur en renovering av Djursholms och Stocksunds tak går till, med kulturmiljö och regler, beskriver vi under {_trl('Danderyd','takrenovering i Danderyd')}."],
 "Lidingö": [f"Villastäder som Brevik och radhusbyar som Mölna behöver olika åtgärder. Vad som gäller för ditt hus läser du om under {_trl('Lidingö','takrenovering i Lidingö')}."],
 "Huddinge": [f"Från Stuvstas villastad till radhusen i Östra Skogås: arbetsgång, material och ROT finns samlat på sidan om {_trl('Huddinge','takrenovering i Huddinge')}."],
 "Järfälla": [f"Radhusområden och villor i Järfälla har ofta jämngamla tak. Läs hur en omläggning planeras på sidan om {_trl('Järfälla','takrenovering i Järfälla')}."],
 "Sollentuna": [f"Från villastäderna i Tureberg och Norrviken till radhusen från 1960–80-talet – så går en renovering till i Sollentuna, läs mer under {_trl('Sollentuna','takrenovering i Sollentuna')}."],
 "Vallentuna": [f"Villaområden i tätorten och gårdar på landsbygden har helt olika tak. Mer om det under {_trl('Vallentuna','takrenovering i Vallentuna')}."],
 "Upplands Väsby": [f"När flera hus i samma område har lika gamla tak kan arbetet samordnas. Hur det går till beskriver vi under {_trl('Upplands Väsby','takrenovering i Upplands Väsby')}."],
 "Värmdö": [f"Skärgårdsläge, vind och permanentade fritidshus ger egna frågor vid en renovering. Läs mer under {_trl('Värmdö','takrenovering i Värmdö')}."],
 "Tyresö": [f"Tak som byggts på i etapper och 60–70-talstak under skog – arbetsgången för Tyresö finns på sidan om {_trl('Tyresö','takrenovering i Tyresö')}."],
 "Haninge": [f"Från Dalarös sekelskiftesvillor till 60–80-talshusen i Brandbergen: vad en renovering omfattar läser du under {_trl('Haninge','takrenovering i Haninge')}."],
 "Enskede": [f"Hur lertegel återanvänds i trädgårdsstaden och vad som gäller vid parhus beskriver vi under {_trl('Enskede','takrenovering i Enskede')}."],
 "Älvsjö": [f"Originaltegel i Långbro och Herrängen och små takytor på verandor och burspråk – läs mer under {_trl('Älvsjö','takrenovering i Älvsjö')}."],
}

def _trp_sources(srcs, muted):
    li = "\n".join(f'              <li><a class="text-link" href="{u}" rel="noopener">{t}</a></li>'
                   for t, u in srcs)
    cls = "section section-muted seo-section" if muted else "section seo-section"
    return f"""
      <section class="{cls}" id="kallor">
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">Källor</h2>
            <ul class="bullet-list">
{li}
            </ul>
          </div>
        </div>
      </section>"""

# Hero-bild (fotorealistisk illustration, Replicate flux) för orter som har en.
ORT_SEO.update(ORT_SEO_X)
ORT_SEO.update(ORT_SEO_V30)
ORT_HERO_ALT.update(ORT_HERO_ALT_V30)
ORT_SRC_X.update(ORT_SRC_V30)
ORT_HERO = {o: (f"taklaggare-{slug(o)}-1", alt) for o, (alt, _alt2) in ORT_HERO_ALT.items()}
for _o, (_alt1, _alt2) in ORT_HERO_ALT.items():
    ORT_IMG[_o] = (f"taklaggare-{slug(_o)}-2", _alt2)

for _ort, _d in LOC.items():
    intro = _d["intro"]; paras = _d["paras"]; items = _d["items"]
    _x = LOC_EXTRA.get(_ort, {"secs": [], "faq": []})
    _seo = ORT_SEO.get(_ort, {})
    cityfaq = _d["faq"] + _x["faq"] + _seo.get("faq", [])
    extra_html = "".join(sec(t, ps, muted=(i % 2 == 0)) for i,(t,ps) in enumerate(_x["secs"]))
    if _ort in ORT_IMG3_V30 and len(_x["secs"]) >= 3:
        # v30: tredje bild mellan andra och tredje extrasektionen; bilden räknas som en sektion i grå/vit-växlingen.
        _xs = _x["secs"]
        extra_html = ("".join(sec(t, ps, muted=(i % 2 == 0)) for i, (t, ps) in enumerate(_xs[:2]))
                      + fig(f"taklaggare-{slug(_ort)}-3", ORT_IMG3_V30[_ort], muted=True)
                      + "".join(sec(t, ps, muted=(j % 2 == 1)) for j, (t, ps) in enumerate(_xs[2:])))
    _tr = TAKRENO.get(_ort, [])
    _trt = f"Takrenovering i {_ort}"
    _nsec = len(_x["secs"])
    if _seo.get("svc"):
        _merge = _seo["svc"][0] == _trt or _ort in TAKRENO_MERGE
        # Samma rubrik som den nya ortsidan (Solna): bara kort text + länk.
        _svc_ps = (_tr if _seo["svc"][0] == _trt else _seo["svc"][1] + (_tr if _merge else []))
        extra_html += sec(_seo["svc"][0], _svc_ps, muted=(_nsec % 2 == 0), sid="takbyte-takrenovering")
        _nsec += 1
        if _merge: _tr = []
    # Hamnar den nya sektionen vit (Täby, Sollentuna) blir "Våra tjänster" grå och
    # "Varför välja oss" vit, så att vit/grå-växlingen behålls.
    _flip = False
    if _tr:
        extra_html += sec(_trt, _tr, muted=(_nsec % 2 == 0), sid="takrenovering")
        _flip = (_nsec % 2 == 1)
    f = _area_files[_ort]
    others = NEIGHBORS[_ort]
    page(file=f,
      title=_seo.get("title") or f"Takläggare i {_ort} – takbyte & takrenovering | Geal Entreprenad AB",
      description=_seo.get("desc") or f"Takläggare i {_ort}: takbyte, takrenovering och takbesiktning på villa. Gratis besök, fast pris och ROT-avdrag direkt på fakturan.",
      h1=f"Takläggare i {_ort}",
      service=True, service_type="Takläggning", area_served=[_ort],
      crumbs=[("Hem","/"),("Områden","omraden.html"),(_ort,f)],
      cta=(f"Behöver du takläggare i {_ort}?", f"Vi är lokala takläggare i {_ort} – begär en kostnadsfri offert på ditt takprojekt."),
      body=hero(f"Takläggare i {_ort}", intro,
        [("Hem","/"),("Områden","omraden.html"),(_ort,f)],
        [("#tjanster","Tjänster"),("#lokalt","Lokalt"),("#faq","Vanliga frågor")], img=ORT_HERO.get(_ort),
        trust=ORT_TRUST_V30.get(_ort))
        + sec(f"Takläggare i {_ort} – lokalt och nära", paras + [
            f"Oavsett om du behöver ett komplett takbyte eller en riktad renovering ger vi en tydlig bedömning och offert. Vi arbetar även i grannområden – se alla {a('omraden.html','områden vi arbetar i')}."], sid="lokalt")
        + (fig(*ORT_IMG[_ort]) if _ort in ORT_IMG else "")
        + extra_html
        + links_block(f"Våra tjänster i {_ort}", [
            (f"takbyte-{slug(_ort)}.html" if f"takbyte-{slug(_ort)}.html" in TJ else "takbyte.html", f"Takbyte i {_ort}", "Byte av tegel-, betong- och plåttak."),
            (TRP_FILES.get(_ort, "takrenovering.html"), f"Takrenovering i {_ort}", "Riktade åtgärder som förlänger takets liv."),
            ("takbesiktning.html", f"Takbesiktning i {_ort}", "Bedömning av skick inför beslut."),
            ("takmalning.html", f"Takmålning i {_ort}", "Nytt ytskydd på plåttak."),
            ("taktvatt.html", f"Taktvätt i {_ort}", "Skonsam tvätt och mossbehandling."),
            ("plattak.html", f"Plåttak i {_ort}", "Nytt plåttak och plåtarbeten.")], muted=_flip, sid="tjanster")
        + sec_split(f"Varför välja oss i {_ort}?", [
            _d.get("why") or f"Vi utgår från Bromma och når {_ort} snabbt. Det gör att vi kan komma ut på besiktning utan långa väntetider och hålla nära kontakt genom hela projektet.",
            f"Läs mer om {a('villatak.html','tak på villa')} eller jämför {a('takbyte-eller-takrenovering.html','takbyte och takrenovering')} innan du bestämmer dig."],
            f"Takläggare i {_ort}", items, muted=not _flip)
        + links_block("Närliggande områden", [
            (_area_files[o], f"Takläggare i {o}", f"Vi arbetar även i {o}.") for o in others]),
      faq=cityfaq,
      after_faq=_trp_sources(ORT_SRC_X[_ort], muted=True) if _ort in ORT_SRC_X else "")

# ====================== TAKRENOVERING PER ORT =============================
# 16 långa ortsidor "Takrenovering i <ort>" (Keyword Planner 10–100/mån per ort).
# Innehåll, lokala fakta och källor (sidor som faktiskt öppnats) i tools/takreno_orter.py.
# Priser: bara länk till vad-kostar-takrenovering.html. FAQPage-schema bara för ortens frågor.
TRP_CRUMB = SVC_CRUMB + [("Takrenovering", "takrenovering.html")]

for _ort in TRP_ORTER:
    _d = TRP[_ort]
    _f = TRP_FILES[_ort]
    _crumbs = TRP_CRUMB + [(_ort, _f)]
    # Sektionerna byggs som funktioner av muted; färgen sätts bakifrån så att sista
    # blocket före FAQ (vit) blir grått och vit/grå-växlingen håller hela vägen.
    _parts = []
    for _i, _s in enumerate(_d["sections"]):
        if _s.get("aside"):
            _parts.append(lambda m, s=_s: sec_split(s["h2"], s["paras"], s["aside"]["title"],
                                                    s["aside"]["items"], muted=m, sid=s["id"]))
        else:
            _parts.append(lambda m, s=_s: sec(s["h2"], s["paras"], muted=m, sid=s["id"]))
        if _i == 0:
            _parts.append(lambda m, o=_ort: fig(f"takrenovering-{slug(o)}-2", TRP_IMG_ALT[o][1], muted=m))
        # v29: valfri tredje bild (img[2]) efter sista textsektionen.
        if _i == len(_d["sections"]) - 1 and _i > 0 and len(_d.get("img", [])) > 2:
            _parts.append(lambda m, o=_ort, d=_d: fig(f"takrenovering-{slug(o)}-3", d["img"][2][0], muted=m))
    _parts.append(lambda m, o=_ort, d=_d: sec_process(f"Så går takrenoveringen till i {o}", d["steps"], muted=m, sid="process"))
    _parts.append(lambda m, o=_ort, d=_d: sec(f"ROT-avdrag för takrenovering i {o}", d["rot"], muted=m, sid="rot"))
    _parts.append(lambda m, o=_ort, d=_d: sec(f"Vad kostar en takrenovering i {o}?", d["price"], muted=m, sid="pris"))
    _parts.append(lambda m, o=_ort: links_block(f"Mer om tak i {o}", (
        [(_area_files[o], f"Takläggare i {o}", "Takbyte, besiktning och plåtarbeten.")] if o in _area_files else []) + [
        ("takrenovering.html", "Takrenovering och takomläggning", "Så fungerar en omläggning."),
        ("vad-kostar-takrenovering.html", "Vad kostar en takrenovering?", "Det här styr priset."),
        ("kalkylator-takbyte.html", "Takbyte-kalkylator", "Räkna på takytan och ROT.")], muted=m, sid="lankar"))
    _parts.append(lambda m, o=_ort: links_block("Takrenovering i närliggande orter", [
        (TRP_FILES[n], f"Takrenovering i {n}", TRP[n]["card"]) for n in TRP_NEIGHBORS[o]], muted=m))
    _n = len(_parts)
    _html = "\n".join(fn((_n - 1 - i) % 2 == 0) for i, fn in enumerate(_parts))
    page(file=_f, title=_d["title"], description=_d["description"],
      h1=f"Takrenovering i {_ort}",
      service=True, service_type="Takrenovering", area_served=[_ort],
      geo_placename=f"{_ort}, Stockholm",
      crumbs=_crumbs,
      cta=(f"Ska taket renoveras i {_ort}?", "Vi kommer ut gratis, går igenom taket och lämnar ett skriftligt kostnadsförslag."),
      body=hero(f"Takrenovering i {_ort}", _d["lead"], _crumbs,
        [("#hus", "Husen"), ("#process", "Så går det till"), ("#rot", "ROT"), ("#faq", "Vanliga frågor"), ("#kallor", "Källor")],
        trust=_d.get("trust"), img=(f"takrenovering-{slug(_ort)}-1", TRP_IMG_ALT[_ort][0]))
        + _html,
      faq=_d["faq"],
      after_faq=_trp_sources(_d["sources"], muted=True))

# ====================== TJÄNSTER V1 (2026-10-25) ==========================
# Ägarbeslut 25.10: sajten täcker alla Geals byggtjänster. Tjänstehubbar (badrum, kök,
# målare, golv, snickare, fasad, fönster) + ortsidor "<tjänst> i <ort>" (Keyword Planner
# 100–1 000/mån). Innehåll + källor i tools/tj_*.py (PAGES_TJ), registreras i tools/tjanster_v1.py.
# Inga priser, garantier utöver lag, omdömen, case eller cert som sajten inte redan anger.
TJ_CRUMB = SVC_CRUMB
# (TJ-importen och tj_list_html ligger före tjänstesidorna – takbyte.html listar ortsidorna, v5)

def _tj_parts(d):
    parts = []
    for i, s in enumerate(d["sections"]):
        if s.get("aside"):
            parts.append(lambda m, s=s: sec_split(s["h2"], s["paras"], s["aside"]["title"],
                                                  s["aside"]["items"], muted=m, sid=s["id"]))
        else:
            parts.append(lambda m, s=s: sec(s["h2"], s["paras"], muted=m, sid=s["id"]))
        if i == 0:
            parts.append(lambda m, d=d: fig(d["file"][:-5] + "-2", d["img"][1][0], muted=m))
        # v20: valfri tredje bild (img[2]) efter sista textsektionen – sidor med två bilder oförändrade.
        if i == len(d["sections"]) - 1 and i > 0 and len(d["img"]) > 2:
            parts.append(lambda m, d=d: fig(d["file"][:-5] + "-3", d["img"][2][0], muted=m))
    parts.append(lambda m, d=d: sec_process(d["steps_h2"], d["steps"], muted=m, sid="process"))
    parts.append(lambda m, d=d: sec(d["rot_h2"], d["rot"], muted=m, sid="rot"))
    parts.append(lambda m, d=d: sec(d["price_h2"], d["price"], muted=m, sid="pris"))
    return parts

for _f, _d in TJ.items():
    _svc = TJ_SERVICES[_d["service"]]
    _hubf = TJ_HUB.get(_d["service"])
    if _d["kind"] == "hub":
        _crumbs = TJ_CRUMB + [(_svc["crumb"], _f)]
    else:
        _crumbs = TJ_CRUMB + ([(_svc["crumb"], _hubf)] if _hubf else []) + [(_d["ort"], _f)]
    _parts = _tj_parts(_d)
    _others = [x for x in TJ_DISTRICTS.get(_d["service"], []) if x != _f]
    if _d["kind"] == "hub":
        if _others:
            _parts.append(lambda m, d=_d, o=_others: tj_list_html(f"{d['svc_label']} per område", o, muted=m, sid="omraden"))
        # v15: deltjänster med samma hubb (t.ex. fasadmålning och tapetsering under malare.html).
        for _s2 in sorted(s for s, h in TJ_HUB.items() if h == _f and s != _d["service"] and TJ_DISTRICTS.get(s)):
            _fs2 = TJ_DISTRICTS[_s2]
            _parts.append(lambda m, fs=_fs2, s2=_s2: tj_list_html(f"{TJ[fs[0]]['svc_label']} per område", fs, muted=m, sid=f"omraden-{s2}"))
        _parts.append(lambda m, d=_d: links_block("Relaterade tjänster", d["related"], muted=m, sid="lankar"))
    else:
        _ort = _d["ort"]
        _cards = [(_hubf, TJ[_hubf]["h1"] if _hubf in TJ else _svc["crumb"], (TJ[_hubf]["card"] if _hubf in TJ else _svc["card"]))] if _hubf else []
        if _ort in _area_files:
            _cards.append((_area_files[_ort], f"Takläggare i {_ort}", "Takbyte, takbesiktning och plåtarbeten."))
        if _ort in TRP_FILES:
            _cards.append((TRP_FILES[_ort], f"Takrenovering i {_ort}", TRP[_ort]["card"]))
        _cards += _d.get("related", [])
        _parts.append(lambda m, c=_cards, o=_ort: links_block(f"Fler tjänster {'på' if o in ('Lidingö', 'Södermalm', 'Värmdö') else 'i'} {o}", c, muted=m, sid="lankar"))
        if _others:
            _parts.append(lambda m, d=_d, o=_others: tj_list_html(f"{d['svc_label']} i fler områden", o, muted=m))
    _n = len(_parts)
    _html = "\n".join(fn((_n - 1 - i) % 2 == 0) for i, fn in enumerate(_parts))
    _anchors = [(f"#{_d['sections'][0]['id']}", _d["sections"][0].get("anchor", "Översikt")),
                ("#process", "Så går det till"), ("#rot", "ROT"), ("#faq", "Vanliga frågor"), ("#kallor", "Källor")]
    page(file=_f, title=_d["title"], description=_d["description"], h1=_d["h1"],
      service=True, service_type=_svc["service_type"],
      area_served=([_d["ort"]] if _d["kind"] == "district" else None),
      geo_placename=(f"{_d['ort']}, Stockholm" if _d["kind"] == "district" else "Bromma, Stockholm"),
      crumbs=_crumbs, cta=_d["cta"],
      body=hero(_d["h1"], _d["lead"], _crumbs, _anchors, trust=_d.get("trust") or _svc.get("trust"), img=(_f[:-5] + "-1", _d["img"][0][0])) + _html,
      faq=_d["faq"], after_faq=_trp_sources(_d["sources"], muted=True))

# ====================== DALARNA (Borlänge + regionen) =====================
# Geal Entreprenad AB förmedlar/samordnar och utför via lokal samarbetspartner på plats i
# Dalarna. Egen adress i regionen anges INTE (NAP-ärlighet). Gemensamma
# lokala vinklar: tunga snölaster, frys–tö, istappar, äldre trä-/faluröda
# villor och fritidshus. geo.region = SE-W (Dalarna).
DAL = {
 "Borlänge": {
   "intro": "Borlänge är Dalarnas industri- och handelscentrum vid Dalälven, och en av de orter där vi är mest aktiva i regionen. Vi hjälper villaägare i bland annat Tjärna, Jakobsgårdarna, Kvarnsveden och Torsång med takbyte, takrenovering och takbesiktning – med takläggare på plats i Borlänge.",
   "paras": [
     "Borlänge växte fram kring Domnarvets järnverk och pappersbruket i Kvarnsveden, och bebyggelsen speglar det: villaområden från 1940–70-talet blandas med äldre trähus och nyare områden. Många av dessa efterkrigstak har betongpannor och underlagspapp som passerat sin tekniska livslängd och är mogna för byte eller omläggning.",
     "Klimatet i Borlänge ställer hårdare krav än i Stockholmstrakten. Rejäla snölaster vintertid, återkommande tö och köldperioder sliter på tätskikt och plåt och skapar istappar och isbildning vid takfot och hängrännor. Vid takarbeten här lägger vi stor vikt vid snörasskydd, taksäkerhet och genomtänkt avvattning som klarar snösmältning.",
     "I villaområden nära Dalälven och skogen, som Torsång och Kvarnsveden, är fukt och mossa på norrvända, skuggiga takytor vanligt. Vi bedömer alltid om det räcker med taktvätt och riktade åtgärder eller om taket behöver läggas om helt, och anpassar materialvalet efter husets ålder och läge.",
   ],
   "items": ["Takläggare på plats i Borlänge, Tjärna, Kvarnsveden, Torsång.","Snörasskydd och taksäkerhet för Dalarnas snölaster.","Byte av mogna 40–70-talstak i betong och plåt."],
   "faq": [
     ("Arbetar ni verkligen i Borlänge?","Ja. Geal Entreprenad AB tar takuppdrag i Borlänge tillsammans med vår lokala samarbetspartner i Dalarna – du får kontakt och offert av oss, och arbetet utförs av takläggare på plats."),
     ("Hur påverkar snölasten mitt tak i Borlänge?","Tunga snölaster och återkommande tö belastar både konstruktion och tätskikt och ger istappar vid takfoten. Vi ser över snörasskydd, infästningar och avvattning så att taket klarar vintern."),
     ("Måste jag byta hela taket eller räcker en renovering?","Det avgörs av en besiktning. Är pannorna hela men underlagspappen slut kan en omläggning räcka; är både pannor och underlag uttjänta rekommenderar vi byte."),
   ]},
 "Falun": {
   "intro": "Falun är Dalarnas residensstad, känd för koppargruvan och den faluröda färgen, med gott om äldre trähus och kulturhistoriskt värdefulla miljöer. Vi hjälper villaägare i bland annat Britsarvet, Källviken, Herrhagen och Främby med takbyte och takrenovering.",
   "paras": [
     "Falu koppargruva och trähusbebyggelsen i Elsborg och Östanfors är världsarv, och stora delar av Falun präglas av äldre trävillor med branta sadeltak. På sådana hus är det avgörande att bevara takets uttryck och proportioner vid ett byte, samtidigt som vi förnyar underlag, plåt och avvattning.",
     "Faluns läge i Dalarna innebär kalla, snörika vintrar. Tegel- och betongpannor utsätts för upprepade frys- och töcykler som kan spränga sprickor, och snötryck belastar konstruktionen. Vi prioriterar täta anslutningar, rätt underlagspapp och snörasskydd som skyddar entréer och gångytor.",
     "I områden som Britsarvet, Herrhagen och Hälsinggården finns villor från olika epoker, medan Främby och Källviken har inslag av nyare hus. Vi anpassar åtgärder och material efter husets ålder – från varsam omläggning på äldre trävillor till moderna plåtlösningar på lägre lutningar.",
   ],
   "items": ["Varsamt takbyte på Faluns äldre trävillor.","Material som tål frys–tö och snötryck.","Villatak i Britsarvet, Källviken, Herrhagen, Främby."],
   "faq": [
     ("Kan ni bevara husets stil vid takbyte i Faluns trähuskvarter?","Ja. På äldre trävillor väljer vi pannor, plåt och kulörer som bevarar husets och områdets karaktär, och moderniserar samtidigt underlag och tätskikt."),
     ("Behöver jag bygglov för takbyte i Falun?","Normalt inte för villor, inte heller vid material- eller kulörbyte (gäller från 1 december 2025). I kulturhistoriskt värdefulla miljöer krävs lov – stäm av med Falu kommun."),
     ("Vilka delar av Falun arbetar ni i?","Hela Falun med omnejd, bland annat Britsarvet, Källviken, Herrhagen, Främby och Hälsinggården."),
   ]},
 "Ludvika": {
   "intro": "Ludvika i sydvästra Dalarna har en stark industrihistoria med kraftteknik och gruvdrift. Vi hjälper villaägare i Ludvika, Grängesberg, Håksberg och Sunnansjö med takbyte, takrenovering och besiktning.",
   "paras": [
     "Ludvika växte kring gruvnäringen och kraftindustrin, och villabebyggelsen består till stor del av hus från 1900-talets mitt tillsammans med äldre trähus i Grängesberg och de mindre orterna. Många av dessa tak närmar sig nu slutet på sin livslängd.",
     "Det sjörika, skogsnära landskapet och de snörika vintrarna sätter tydliga spår på taken: mossa och löv på skuggiga ytor, tunga snölaster och isbildning vid takfot. Vi ser gärna över avvattning, snörasskydd och taksäkerhet i samband med byte eller renovering.",
     "I Grängesberg och Sunnansjö finns äldre trävillor där utseendet är viktigt, medan centrala Ludvika och Marnäs har mer blandad bebyggelse. Vi bedömer varje tak individuellt och föreslår rätt åtgärdsnivå – från punktinsats mot läckage till komplett takbyte.",
   ],
   "items": ["Villatak i Ludvika, Grängesberg, Håksberg, Sunnansjö.","Åtgärder för mossa, snölast och isbildning.","Allt från läckagelagning till komplett takbyte."],
   "faq": [
     ("Tar ni takuppdrag i hela Ludvika kommun?","Ja, i Ludvika tätort och kringliggande orter som Grängesberg, Håksberg, Sunnansjö och Nyhammar, via vår lokala samarbetspartner i Dalarna."),
     ("Mitt tak är mossigt och skuggigt – vad gör ni?","Skuggiga, trädnära tak håller kvar fukt och drar åt sig mossa. Vi tvättar skonsamt, rensar avvattningen och bedömer om taket behöver ytterligare åtgärder."),
     ("Hur snabbt kan jag få en offert?","Vi bokar ett platsbesök och lämnar en tydlig, fast offert efter besiktning av takets skick."),
   ]},
 "Avesta": {
   "intro": "Avesta vid Dalälven i sydöstra Dalarna har en lång järnbrukshistoria. Vi hjälper villaägare i Avesta, Krylbo, Horndal och Fors med takbyte, takrenovering och plåtarbeten.",
   "paras": [
     "Avesta präglas av järn- och stålindustrin, från de gamla bruken till dagens rostfria stål i Koppardalen. Villabebyggelsen består av allt från äldre bruksbostäder och trävillor till efterkrigstidens småhus, där många tak nu är mogna för åtgärd.",
     "Läget vid Dalälven och de kalla vintrarna innebär fukt, snölast och frys–töväxlingar som sliter på tätskikt och pannor. Vi lägger vikt vid rätt underlagspapp, täta plåtdetaljer och snörasskydd som klarar regionens klimat.",
     "I Krylbo och Horndal finns äldre bebyggelse där vi arbetar varsamt, medan centrala Avesta och Skogsbo har en blandning av hustyper. Vi anpassar material och metod efter husets ålder och takets skick.",
   ],
   "items": ["Villatak i Avesta, Krylbo, Horndal, Fors.","Tätskikt och plåt som tål fukt och frys–tö.","Snörasskydd och komplett avvattning."],
   "faq": [
     ("Arbetar ni i Krylbo och de mindre orterna kring Avesta?","Ja, i hela Avesta kommun inklusive Krylbo, Horndal, Fors och By, via vår lokala partner i Dalarna."),
     ("Räcker en takomläggning på mitt äldre hus?","Om pannorna är hela men underlaget slitet kan en omläggning räcka. En besiktning ger säkert besked."),
     ("Byter ni hängrännor och stuprör samtidigt?","Ja, vi rekommenderar ofta att förnya avvattning och taksäkerhet i samma projekt för ett komplett resultat."),
   ]},
 "Hedemora": {
   "intro": "Hedemora är Dalarnas äldsta stad med medeltida anor och välbevarad trähusbebyggelse. Vi hjälper villaägare i Hedemora, Långshyttan, Vikmanshyttan och Stjärnsund med takbyte och takrenovering.",
   "paras": [
     "Som Dalarnas äldsta stad har Hedemora en värdefull trästadskärna och gott om äldre trävillor. På dessa hus är varsamhet vid takbyte avgörande – vi bevarar takets uttryck och detaljer och moderniserar samtidigt underlag och tätskikt.",
     "Snörika vintrar och stora temperaturväxlingar belastar taken hårt. Snötryck, istappar och frys–töcykler kräver robusta lösningar; vi ser över snörasskydd, infästningar och avvattning vid varje projekt.",
     "I bruksorter som Långshyttan och Vikmanshyttan finns äldre bebyggelse med egen karaktär, medan centrala Hedemora blandar epoker. Vi bedömer varje tak för sig och föreslår rätt åtgärd.",
   ],
   "items": ["Varsamt takarbete i Hedemoras trästad.","Villatak i Långshyttan, Vikmanshyttan, Stjärnsund.","Snörasskydd och robusta vinterlösningar."],
   "faq": [
     ("Kan husets karaktär bevaras vid takbyte i Hedemora?","Ja, särskilt viktigt i trästaden. Vi väljer material och kulörer som bevarar husets stil och utför arbetet varsamt."),
     ("Vilka orter kring Hedemora arbetar ni i?","Hela kommunen, bland annat Långshyttan, Vikmanshyttan, Stjärnsund och Garpenberg."),
     ("Hur ofta bör taket kontrolleras i Dalarnas klimat?","En översyn vår och höst är klokt, särskilt efter snörika vintrar då snötryck och istappar kan ha skadat plåt och tätskikt."),
   ]},
 "Säter": {
   "intro": "Säter är känt för sin välbevarade trästad och den natursköna Säterdalen. Vi hjälper villaägare i Säter, Gustafs och Stora Skedvi med takbyte, takrenovering och takbesiktning.",
   "paras": [
     "Säters trästad är en av landets bäst bevarade, och orten har många äldre trävillor med branta tak. Här är det viktigt att bevara husens uttryck vid takbyte samtidigt som underlag och plåt förnyas för lång livslängd.",
     "Det inlandsklimat som råder i Säter ger kalla, snörika vintrar. Snölast, isbildning och frys–töväxlingar sliter på tätskikt och pannor, och vi prioriterar snörasskydd och genomtänkt avvattning.",
     "I Gustafs och Stora Skedvi finns lantligt belägna villor och gårdar, ofta trädnära, där mossa och fukt på skuggiga takytor är vanligt. Vi anpassar åtgärderna efter husets läge och takets skick.",
   ],
   "items": ["Varsamt takarbete i Säters trästad.","Villatak i Gustafs och Stora Skedvi.","Snörasskydd och avvattning för snörika vintrar."],
   "faq": [
     ("Arbetar ni med äldre trävillor i Säter?","Ja. Vi är vana vid varsamt takarbete där husets och trästadens karaktär ska bevaras."),
     ("Tar ni uppdrag i Gustafs och Stora Skedvi?","Ja, i hela Säters kommun via vår lokala samarbetspartner i Dalarna."),
     ("Behöver mitt trädnära tak taktvätt?","Skuggiga, trädnära tak samlar mossa och fukt. Vi tvättar skonsamt och bedömer om taket behöver ytterligare åtgärder."),
   ]},
 "Mora": {
   "intro": "Mora vid Siljan är norra Dalarnas centrum, känt för Vasaloppet och dalahästarna i Nusnäs. Vi hjälper villa- och fritidshusägare i Mora, Noret, Färnäs och Sollerön med takbyte och takrenovering.",
   "paras": [
     "Kring Mora och Siljan finns både åretruntvillor och många fritidshus, ofta äldre timmerhus och trävillor. På dessa tak är varsamhet och rätt materialval viktigt, och för fritidshus lägger vi vikt vid lösningar som tål att stå oövervakade under vintern.",
     "Norra Dalarnas klimat är kärvt med långa, snörika vintrar. Tunga snölaster och isbildning ställer höga krav på konstruktion, snörasskydd och avvattning – något vi alltid ser över vid takarbeten i Moratrakten.",
     "I Noret och Färnäs finns tätare villabebyggelse, medan Sollerön och byarna runt Siljan har mer utspridda hus. Vi anpassar planering och material efter läget och takets skick, och samordnar arbetet via vår lokala partner.",
   ],
   "items": ["Villor och fritidshus i Mora, Noret, Färnäs, Sollerön.","Robusta lösningar för tunga snölaster.","Varsamt arbete på äldre timmer- och trähus."],
   "faq": [
     ("Tar ni takuppdrag på fritidshus kring Siljan?","Ja. Vi hjälper både åretruntboende och fritidshusägare, och väljer lösningar som klarar snörika vintrar även när huset står oövervakat."),
     ("Hur påverkar snön taket i Mora?","Norra Dalarna har tunga snölaster. Vi kontrollerar konstruktion, snörasskydd och infästningar så att taket klarar belastningen."),
     ("Vilka orter kring Mora arbetar ni i?","Mora tätort samt Noret, Färnäs, Vika, Nusnäs och Sollerön, via vår lokala samarbetspartner."),
   ]},
 "Leksand": {
   "intro": "Leksand vid Siljan är känt för midsommar, dalahästkultur och timmerhus. Vi hjälper villa- och fritidshusägare i Leksand, Insjön, Tällberg och Siljansnäs med takbyte och takrenovering.",
   "paras": [
     "Leksandsbygden har gott om äldre timmerhus, faluröda trävillor och fritidshus, särskilt i Tällberg och längs Siljan. Här är det viktigt att bevara husens traditionella uttryck vid takbyte samtidigt som underlag och plåt förnyas.",
     "De snörika vintrarna vid Siljan innebär tunga snölaster, isbildning och frys–töväxlingar. Vi prioriterar snörasskydd, robusta infästningar och avvattning som klarar snösmältning och skyddar entréer och gångytor.",
     "I Insjön och centrala Leksand finns tätare villabebyggelse, medan Tällberg och Siljansnäs har många fritidshus i natursköna lägen. Vi anpassar material och metod efter husets karaktär och läge.",
   ],
   "items": ["Villor och fritidshus i Leksand, Insjön, Tällberg, Siljansnäs.","Varsamt arbete på timmerhus och faluröda villor.","Snörasskydd och avvattning för Siljansklimatet."],
   "faq": [
     ("Arbetar ni med timmerhus och fritidshus i Leksand?","Ja. Vi är vana vid varsamt takarbete på timmer- och trähus, och väljer lösningar som klarar vintern även på oövervakade fritidshus."),
     ("Tar ni uppdrag i Tällberg och Siljansnäs?","Ja, i hela Leksands kommun via vår lokala partner i Dalarna."),
     ("Behöver jag snörasskydd i Leksand?","På de flesta tak, särskilt över entréer och gångytor, är snörasskydd klokt med tanke på snölasterna vid Siljan."),
   ]},
 "Rättvik": {
   "intro": "Rättvik vid Siljan är känt för sin långa kyrkbrygga, kalkstenen och natursköna byar. Vi hjälper villa- och fritidshusägare i Rättvik, Vikarbyn, Boda och Furudal med takbyte och takrenovering.",
   "paras": [
     "Rättviksbygden har många äldre trävillor, timmerhus och fritidshus, ofta i sluttningar mot Siljan. På dessa tak är varsamhet och rätt materialval viktigt, och vi förnyar underlag och plåt utan att förändra husets uttryck.",
     "Klimatet vid Siljan är snörikt med kalla vintrar. Snölast, isbildning och frys–töcykler sliter på tätskikt och pannor; vi lägger vikt vid snörasskydd, infästningar och avvattning som klarar snösmältning.",
     "I Vikarbyn, Boda och Furudal finns utspridd bebyggelse i natursköna lägen, medan centrala Rättvik har tätare villaområden. Vi planerar projekten efter läge och tillgänglighet och samordnar arbetet lokalt.",
   ],
   "items": ["Villor och fritidshus i Rättvik, Vikarbyn, Boda, Furudal.","Varsamt arbete på timmer- och trähus.","Snörasskydd och avvattning för snörika vintrar."],
   "faq": [
     ("Tar ni takuppdrag i byarna kring Rättvik?","Ja, i hela Rättviks kommun inklusive Vikarbyn, Boda och Furudal, via vår lokala samarbetspartner."),
     ("Hur hanterar ni sluttande, svåråtkomliga tomter?","Vi planerar etablering, ställning och säkerhet efter tomtens förutsättningar och takets tillgänglighet."),
     ("Kan ni arbeta på fritidshus vintertid?","Vi bedömer varje projekt; vissa arbeten planeras till barmarkssäsong, medan akuta läckage åtgärdas när det behövs."),
   ]},
 "Smedjebacken": {
   "intro": "Smedjebacken vid Norra Barken i södra Dalarna har en stark bruks- och stålhistoria. Vi hjälper villaägare i Smedjebacken, Söderbärke och Vad med takbyte, takrenovering och besiktning.",
   "paras": [
     "Smedjebacken präglas av järn- och stålindustrin och det sjönära läget vid Norra Barken. Villabebyggelsen består av allt från äldre trähus och bruksbostäder till efterkrigstidens småhus, där många tak nu är mogna för byte eller omläggning.",
     "Det sjörika, skogsnära landskapet och de snörika vintrarna ger fukt, mossa på skuggiga ytor samt tunga snölaster och isbildning. Vi ser över taktvätt, avvattning, snörasskydd och taksäkerhet i samband med takarbeten.",
     "I Söderbärke och Vad finns lantligt belägna villor, medan centrala Smedjebacken har tätare bebyggelse. Vi bedömer varje tak individuellt och föreslår rätt åtgärdsnivå efter husets ålder och skick.",
   ],
   "items": ["Villatak i Smedjebacken, Söderbärke, Vad.","Åtgärder mot mossa, snölast och isbildning.","Från läckagelagning till komplett takbyte."],
   "faq": [
     ("Arbetar ni i hela Smedjebackens kommun?","Ja, i Smedjebacken, Söderbärke, Vad och kringliggande byar, via vår lokala partner i Dalarna."),
     ("Mitt sjönära tak är mossigt – vad gör ni?","Fuktiga, skuggiga lägen ger mer mossa. Vi tvättar skonsamt, rensar avvattningen och bedömer takets skick."),
     ("Hur får jag en offert?","Vi bokar ett platsbesök och lämnar en tydlig, fast offert efter besiktning."),
   ]},
}
_dal_files = {n: f"taklaggare-{slug(n)}.html" for n in DALARNA_AREAS}

# ---- Dalarna hub (dalarna.html) ------------------------------------------
_dal_cards = "\n".join(f"""            <article class="service-snippet">
              <h3>{n}</h3>
              <p>Takläggare i {n} – takbyte, takrenovering och besiktning.</p>
              <a class="text-link" href="{_dal_files[n]}">Takläggare i {n}</a>
            </article>""" for n in DALARNA_AREAS)
page(file="dalarna.html",
  geo_region="SE-W", geo_placename="Borlänge, Dalarna",
  contact_url="offert-dalarna.html",
  title="Takläggare i Dalarna – Borlänge, Falun & hela regionen | Geal Entreprenad AB",
  description="Takbyte, takrenovering och takbesiktning i Dalarna – Borlänge, Falun, Säter, Ludvika, Mora m.fl. Takläggare på plats via vår lokala partner.",
  h1="Takläggare i Dalarna",
  crumbs=[("Hem","/"),("Områden","omraden.html"),("Dalarna","dalarna.html")],
  cta=("Behöver du takläggare i Dalarna?","Skicka en förfrågan – vi samordnar ditt takprojekt med erfarna takläggare på plats i Dalarna."),
  body=hero("Takläggare i Dalarna",
    "Geal Entreprenad AB tar takuppdrag i hela Dalarna. Vi samordnar projektet och lämnar offert, medan arbetet på taket utförs av vår lokala samarbetspartner med takläggare på plats – från Borlänge och Falun till orterna runt Siljan.",
    [("Hem","/"),("Områden","omraden.html"),("Dalarna","dalarna.html")],
    [("#orter","Orter"),("#klimat","Dalarnas klimat"),("#tjanster","Tjänster")])
    + sec("Tak i Dalarnas klimat – snölast, is och frys–tö", [
        "Dalarna har ett kärvare klimat än Stockholmsregionen: tunga snölaster, långa köldperioder och återkommande töväxlingar. Det sätter hård press på taket – snötryck belastar konstruktionen, medan frys–töcykler spränger sprickor i pannor och tätskikt.",
        "Vid takfot och hängrännor bildas istappar och isvallar när smältvatten fryser om, vilket kan tvinga in vatten under tätskiktet. Därför är snörasskydd, robust infästning, rätt underlagspapp och genomtänkt avvattning extra viktigt på dalatak.",
        "Regionen har också gott om äldre trä- och faluröda villor samt fritidshus, där vi arbetar varsamt för att bevara husets uttryck. Se alla orter nedan eller jämför "
        + a('takbyte-eller-takrenovering.html','takbyte och takrenovering') + " innan du bestämmer dig."], sid="klimat")
    + f"""      <section class="section section-muted seo-section" id="orter">
        <div class="container">
          <div class="section-copy section-copy--wide">
            <h2 class="section-title">Orter vi arbetar i – Dalarna</h2>
            <p>Välj din ort för lokal information om takbyte, takrenovering och takbesiktning – till exempel {a(_dal_files['Borlänge'],'takbyte i Borlänge')}, {a(_dal_files['Falun'],'takläggare i Falun')} eller {a(_dal_files['Säter'],'takbyte i Säter och Stora Skedvi')}.</p>
          </div>
          <div class="service-grid">
{_dal_cards}
          </div>
        </div>
      </section>"""
    + links_block("Våra tjänster i Dalarna", [
        ("takbyte.html","Takbyte","Byte av tegel-, betong- och plåttak."),
        ("takrenovering.html","Takrenovering","Riktade åtgärder som förlänger takets liv."),
        ("takbesiktning.html","Takbesiktning","Bedömning av skick inför beslut."),
        ("taksakerhet-snorasskydd.html","Snörasskydd & taksäkerhet","Extra viktigt i Dalarnas snöklimat."),
        ("taktvatt.html","Taktvätt","Mot mossa på skuggiga, trädnära tak."),
        ("hangrannor-stupror.html","Hängrännor & stuprör","Avvattning som klarar snösmältning.")],
        muted=False, sid="tjanster"),
  faq=[
    ("Har ni egen personal i Dalarna?","Vi samordnar och lämnar offert centralt, medan takarbetet utförs av vår lokala samarbetspartner med erfarna takläggare på plats i Dalarna. Du har en tydlig kontakt genom hela projektet."),
    ("Vilka orter i Dalarna arbetar ni i?","Bland annat Borlänge, Falun, Ludvika, Avesta, Hedemora, Säter, Mora, Leksand, Rättvik och Smedjebacken – hör av dig även om din ort inte står med."),
    ("Vad kostar ett takbyte i Dalarna?","Priset beror på takets storlek, material och skick. Vi lämnar alltid en tydlig offert efter besiktning; ROT-avdrag kan sänka arbetskostnaden."),
  ])

# ---- Dalarna ort-sidor ---------------------------------------------------
# GSC 28 d: "takläggare säter" pos 19,8, "takbyte säter" 24,6, "takbyte stora skedvi" 2,1.
DAL_SEO = {
 "Säter": {
   "title": "Takläggare i Säter & Stora Skedvi – takbyte i Dalarna",
   "desc": "Takbyte och takrenovering i Säter, Gustafs och Stora Skedvi – varsamt på trästadens villor, via vår lokala partner i Dalarna. Fast pris efter besök.",
 },
}
for _ort, _d in DAL.items():
    intro = _d["intro"]; paras = _d["paras"]; items = _d["items"]; cityfaq = _d["faq"]
    f = _dal_files[_ort]
    others = NEIGHBORS[_ort]
    page(file=f,
      geo_region="SE-W", geo_placename=f"{_ort}, Dalarna",
      contact_url="offert-dalarna.html",
      title=DAL_SEO.get(_ort, {}).get("title") or f"Takläggare i {_ort} – takbyte & takrenovering i Dalarna | Geal Entreprenad AB",
      description=DAL_SEO.get(_ort, {}).get("desc") or f"Takläggare i {_ort}: takbyte, takrenovering och takbesiktning på villa via vår lokala partner i Dalarna. Fast pris efter besök.",
      h1=f"Takläggare i {_ort}",
      service=True, service_type="Takläggning", area_served=[_ort],
      crumbs=[("Hem","/"),("Områden","omraden.html"),("Dalarna","dalarna.html"),(_ort,f)],
      cta=(f"Behöver du takläggare i {_ort}?", f"Begär en kostnadsfri offert – vi samordnar ditt takprojekt i {_ort} med takläggare på plats i Dalarna."),
      body=hero(f"Takläggare i {_ort}", intro,
        [("Hem","/"),("Områden","omraden.html"),("Dalarna","dalarna.html"),(_ort,f)],
        [("#tjanster","Tjänster"),("#lokalt","Lokalt"),("#faq","Vanliga frågor")])
        + sec(f"Takläggare i {_ort} – lokalt och nära", paras + [
            f"Oavsett om du behöver ett komplett takbyte eller en riktad renovering ger vi en tydlig bedömning och offert. Vi arbetar i hela {a('dalarna.html','Dalarna')} – se fler orter nedan."], sid="lokalt")
        + links_block(f"Våra tjänster i {_ort}", [
            ("takbyte.html", f"Takbyte i {_ort}", "Byte av tegel-, betong- och plåttak."),
            ("takrenovering.html", f"Takrenovering i {_ort}", "Riktade åtgärder som förlänger takets liv."),
            ("takbesiktning.html", f"Takbesiktning i {_ort}", "Bedömning av skick inför beslut.")], muted=False, sid="tjanster")
        + sec_split(f"Så arbetar vi i {_ort}", [
            f"Geal Entreprenad AB samordnar ditt takprojekt i {_ort} och lämnar offert, medan arbetet på taket utförs av vår lokala samarbetspartner med erfarna takläggare på plats i Dalarna. Du har en tydlig kontakt genom hela projektet.",
            f"Vi anpassar alltid material och metod efter Dalarnas klimat med tunga snölaster och frys–tö. Läs mer om {a('taksakerhet-snorasskydd.html','snörasskydd och taksäkerhet')} eller {a('villatak.html','tak på villa')}."],
            f"Takläggare i {_ort}", items)
        + links_block("Fler orter i Dalarna", [
            (_dal_files[o], f"Takläggare i {o}", f"Vi arbetar även i {o}.") for o in others]),
      faq=cityfaq)

# ---- Enkel offertformulär-sida för Dalarna (utan Stockholmsadress/karta) --
_offert_form = """      <section class="section section-muted" id="form">
        <div class="container">
          <div class="form-box" style="max-width:720px;margin:0 auto">
            <h2>Begär offert – Dalarna</h2>
            <p class="section-lead">Fyll i formuläret så återkommer vi med en tydlig
              bedömning och offert. Du kan också ringa
              <a class="text-link" href="tel:%s">%s</a> eller mejla
              <a class="text-link" href="mailto:%s">%s</a>.</p>
            <p id="form-fel" class="form-alert" role="alert" hidden>
              Något blev fel när meddelandet skulle skickas. Kontrollera uppgifterna och
              försök igen, eller ring oss på <a href="tel:%s">%s</a>.
            </p>
            <form action="sendmail.php" method="post">
              <div class="hp-field" aria-hidden="true">
                <label for="website">Lämna detta fält tomt</label>
                <input id="website" name="website" type="text" tabindex="-1" autocomplete="off" />
              </div>
              <input type="hidden" name="retur" value="offert-dalarna.html" />
              <div class="field">
                <label for="namn">Namn</label>
                <input id="namn" name="namn" type="text" placeholder="Ange namn" required />
              </div>
              <div class="field">
                <label for="ort">Ort i Dalarna</label>
                <input id="ort" name="ort" type="text" placeholder="T.ex. Borlänge" />
              </div>
              <div class="field">
                <label for="telefon">Telefon</label>
                <input id="telefon" name="telefon" type="tel" placeholder="Ange telefonnummer" required />
              </div>
              <div class="field">
                <label for="epost">E-post</label>
                <input id="epost" name="epost" type="email" placeholder="Ange e-postadress" required />
              </div>
              <div class="field">
                <label for="tjanst">Tjänst</label>
                <select id="tjanst" name="tjanst" required>
                  <option value="">Välj tjänst</option>
                  <option>Takbyte</option>
                  <option>Takrenovering</option>
                  <option>Plåttak</option>
                  <option>Takmålning</option>
                  <option>Takbesiktning</option>
                  <option>Taktvätt</option>
                </select>
              </div>
              <div class="field">
                <label for="meddelande">Meddelande</label>
                <textarea id="meddelande" name="meddelande"
                  placeholder="Beskriv kort vad du vill ha hjälp med" required></textarea>
              </div>
              <label class="checkbox-row">
                <input type="checkbox" name="gdpr" required />
                Jag godkänner att mina uppgifter behandlas enligt <a class="text-link" href="integritetspolicy.html">integritetspolicyn</a>.
              </label>
              <button class="btn btn-primary" type="submit">Skicka</button>
            </form>
            <script>
              (function () {
                var p = new URLSearchParams(location.search);
                if (p.get("fel")) {
                  var el = document.getElementById("form-fel");
                  if (el) { el.hidden = false; }
                }
              })();
            </script>
          </div>
        </div>
      </section>""" % (PHONE_T, PHONE_D, EMAIL, EMAIL, PHONE_T, PHONE_D)
page(file="offert-dalarna.html",
  geo_region="SE-W", geo_placename="Dalarna",
  noindex=True, nolist=True, no_cta=True, contact_url="offert-dalarna.html",
  title="Begär offert – takläggare i Dalarna | Geal Entreprenad AB",
  description="Begär kostnadsfri offert på takbyte, takrenovering eller takbesiktning i Dalarna. Fyll i formuläret så återkommer vi.",
  h1="Begär offert – Dalarna",
  crumbs=[("Hem","/"),("Dalarna","dalarna.html"),("Begär offert","offert-dalarna.html")],
  body=hero("Begär offert – Dalarna",
    "Berätta kort om ditt takprojekt i Dalarna så återkommer vi med en tydlig bedömning och offert. Arbetet utförs av vår lokala samarbetspartner på plats.",
    [("Hem","/"),("Dalarna","dalarna.html"),("Begär offert","offert-dalarna.html")])
    + _offert_form)

# ====================== ARTICLES (cluster) ================================
ART_CRUMB = [("Hem","/"),("Artiklar","artiklar.html")]

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
        elif kind=="html": out.append(val)
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

PLANNJA_FAQ = '<a class="text-link" href="https://www.plannja.se/konsument/support/faq" rel="noopener">Plannja – vanliga frågor</a>'
SKV_ROT = '<a class="text-link" href="https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete.4.2e56d4ba1202f95012080002966.html" rel="noopener">Skatteverket – rot- och rutarbete</a>'

# ROT-räknare: ren Skatteverket-matematik (30 %, max 50 000 kr/person/år 2026), inga priser.
ROT_TOOL = """          <div class="calc-wrap" id="rot-raknare">
            <form class="calc-form" data-rot-form novalidate>
              <div class="field">
                <label for="rot-arbete">Arbetskostnad i offerten (kr inkl. moms)</label>
                <input id="rot-arbete" name="arbete" type="number" min="0" step="1000" inputmode="numeric" placeholder="t.ex. 120000" />
              </div>
              <div class="field">
                <label for="rot-agare">Ägare som delar avdraget</label>
                <select id="rot-agare" name="agare">
                  <option value="1">1 person</option>
                  <option value="2">2 personer</option>
                </select>
              </div>
            </form>
            <aside class="calc-result" data-rot-result hidden aria-live="polite">
              <p class="calc-result__label">ROT-avdrag</p>
              <p class="calc-result__figure"><span data-rot-avdrag>–</span> kr</p>
              <div class="calc-result__rot">
                <p class="calc-result__label">Du betalar för arbetet</p>
                <p class="calc-result__figure"><span data-rot-betala>–</span> kr</p>
              </div>
              <p class="calc-disclaimer">30 % av arbetskostnaden, högst 50 000 kr per person och år (2026). Material ingår inte. Har du redan använt ROT i år blir utrymmet mindre.</p>
            </aside>
          </div>"""

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
  "Vad kostar ett takbyte? Pris per kvm, arbete & ROT 2026",
  "Vad kostar ett takbyte på villa – totalt och per kvm? Så styr takyta, material och underlag priset, så mäter du taket och räknar ROT 2026.",
  "Vad kostar ett takbyte – totalt och per kvm?",
  "Priset för ett takbyte räknas oftast per kvadratmeter takyta, men kvm-priset varierar mycket med material, lutning och underlag. Här går vi igenom vad som driver kostnaden, hur du mäter takytan, hur du jämför offerter och hur ROT-avdraget räknas – och varför vi alltid ger pris först efter ett gratis besök.",
  [("p","En av de vanligaste frågorna vi får är vad ett takbyte kostar. Det ärliga svaret är att det beror på taket – två villor med samma yta kan landa långt ifrån varandra. Kostnaden styrs framför allt av takets area och form, val av material, taklutning, tillgänglighet och underlagets skick. Därför lämnar vi inga schablonpriser, utan kommer ut gratis, tittar på taket och ger ett kostnadsförslag med fast pris."),
   ("h2","Vad påverkar priset på ett takbyte?"),
   ("ul",["<strong>Takarea och form</strong> – fler kvadratmeter kostar mer, och ett tak med många vinklar, kupor och ränndalar tar längre tid än ett enkelt sadeltak.",
          f"<strong>Material</strong> – betongpannor, tegel, plåt och {a('papptak.html','papp')} skiljer sig i både materialpris, vikt och läggningstid. Materialet påverkar också livslängd och underhåll, se {a('takmaterial-livslangd.html','takmaterial och livslängd')}.",
          "<strong>Underlagets skick</strong> – om råspont, läkt eller underlagspapp behöver bytas ökar omfattningen. Det syns ofta först när det gamla taket rivs, därför bedömer vi det redan vid besöket.",
          "<strong>Taklutning och höjd</strong> – branta och höga tak kräver mer säkerhetsutrustning och ställning.",
          "<strong>Tillgänglighet</strong> – plats för ställning, container och materialleverans påverkar arbetet.",
          f"<strong>Detaljer</strong> – skorstensbeslag, genomföringar, {a('takfonster.html','takfönster')}, {a('hangrannor-stupror.html','hängrännor och stuprör')} och {a('taksakerhet-snorasskydd.html','taksäkerhet')} kan ingå eller tillkomma."]),
   ("h2","Takbyte pris per kvm – så räknar du"),
   ("p","Kvm-priset för ett takbyte gäller takets yta, inte husets boyta. Takytan är större än ytan under taket, eftersom taket lutar och sticker ut vid takfoten. Ju brantare tak, desto större skillnad."),
   ("p","Så räknar du ut takytan ungefärligt: ta ytan under taket inklusive takutsprång och dela med cosinus för taklutningen. Det motsvarar att multiplicera med omkring:"),
   ("ul",["<strong>1,12</strong> vid 27 graders lutning.",
          "<strong>1,27</strong> vid 38 graders lutning.",
          "<strong>1,41</strong> vid 45 graders lutning."]),
   ("p","Exempel: ett hus med 150 kvm under taket och 27 graders lutning har omkring 170 kvm takyta. Ett tak på 100, 150 eller 200 kvm takyta får alltså olika totalpris, men kvm-priset är sällan detsamma. Ställning, container, skorstensbeslag och andra plåtdetaljer kostar ungefär lika mycket oavsett yta, och kupor och ränndalar ökar arbetet."),
   ("p",f"Vill du räkna på din egen takyta kan du använda vår {a('kalkylator-takbyte.html','takbyte-kalkylator')} eller räkna pris per kvm för betong, tegel, plåt och papp på {a('https://takbytepris.nu/','takbytepris.nu')}. Det ger ett spann – det fasta priset får du efter besöket."),
   ("h2","Därför får du pris först efter ett gratis besök"),
   ("p","Siffror i olika prisguider varierar kraftigt och säger lite om just ditt tak. Ett pris som ges utan att någon sett taket blir antingen för högt för att täcka osäkerheten, eller för lågt och följs av tilläggsarbeten. Vi gör därför alltid ett kostnadsfritt besök och ger ett skriftligt kostnadsförslag med fast pris – så vet du vad takbytet kostar innan du bestämmer dig."),
   ("h2","Så jämför du offerter på takbyte"),
   ("p","Ett lågt totalpris är inte alltid billigast. Kontrollera att offerterna du jämför omfattar samma sak:"),
   ("ul",["Rivning och bortforsling av det gamla taket.",
          "Ny underlagspapp, och om läkt eller råspont byts.",
          "Plåtdetaljer: nock, vindskivor, skorsten och genomföringar.",
          "Ställning och skydd under arbetet.",
          "Hängrännor, stuprör och taksäkerhet – ingår de eller inte?",
          "Garanti på arbetet och vem som står för den.",
          "Tidplan och vad som händer vid dåligt väder.",
          "Att ROT-avdraget är uträknat och att firman sköter ansökan."]),
   ("tips","Be om en specificerad offert där arbete och material står var för sig. Det gör det lättare att jämföra – och det är arbetskostnaden som ger ROT-avdrag."),
   ("h2","Arbetskostnad vid takbyte – vad räknas som arbete?"),
   ("p","Arbetskostnaden är det som takläggarna gör på plats: rivning av det gamla taket, ny underlagspapp, läkt, läggning av pannor eller plåt och plåtarbeten kring nock, skorsten och genomföringar. Material, utrustning och resor räknas inte som arbete och ger inget ROT-avdrag, enligt Skatteverket."),
   ("p","Hur stor del av totalpriset som är arbete varierar mellan tak. Ett brant tak med många kupor och ränndalar tar fler arbetstimmar än ett enkelt sadeltak av samma storlek, och plåttak har en annan fördelning än pannor. Därför ska arbete och material alltid stå på egna rader i offerten – annars går det varken att jämföra offerter eller räkna ROT rätt."),
   ("h2","Så räknas ROT-avdraget på ett takbyte"),
   ("p",f"Som villaägare får du normalt ROT-avdrag på <strong>arbetskostnaden</strong> – inte på material, utrustning eller resor. Under 2026 är avdraget 30 % av arbetskostnaden, med ett tak på 50 000 kr per person och år. Äger ni huset två kan ni alltså få upp till 100 000 kr tillsammans. Avdraget görs direkt på fakturan. Läs mer i {a('rot-avdrag-takarbete.html','ROT-avdrag för takarbete')}."),
   ("p","Räkneexempel: är arbetskostnaden i offerten 120 000 kr blir ROT-avdraget 30 % av det, alltså 36 000 kr – under taket på 50 000 kr för en ägare. Du betalar då 84 000 kr för arbetet, plus material och övriga kostnader."),
   ("h3","Räkna ut ditt ROT-avdrag"),
   ("html",ROT_TOOL),
   ("p",f"Den tillfälliga höjningen till 50 % gällde bara arbeten som betalades mellan 12 maj och 31 december 2025. Från 1 januari 2026 gäller 30 % igen. ROT och RUT delar dessutom ett tak på 75 000 kr per person och år. Källa: {SKV_ROT}."),
   ("h2","Behövs ett helt takbyte – eller räcker en renovering?"),
   ("p",f"Är stommen sund och skadorna begränsade kan en {a('takrenovering.html','takrenovering')} eller omläggning räcka, och den kostar oftast mindre än ett fullt byte. Är taket i slutet av sin livslängd blir ett {a('takbyte.html','takbyte')} bättre på sikt. En {a('takbesiktning.html','takbesiktning')} ger svar, och vi går igenom skillnaden i {a('takbyte-eller-takrenovering.html','takbyte eller takrenovering')}."),
   ("cta",("Gratis besök och kostnadsförslag","Vi tittar på ditt tak och ger ett skriftligt kostnadsförslag med fast pris – ROT-avdraget uträknat."))],
  [("takbyte.html","Takbyte","Vår tjänst för komplett takbyte."),
   ("takbyte-eller-takrenovering.html","Takbyte eller takrenovering?","Så avgör du vilket som lönar sig."),
   ("rot-avdrag-takarbete.html","ROT-avdrag för takarbete","Så mycket kan du dra av."),
   ("takbesiktning.html","Takbesiktning","Få takets skick bedömt först."),
   ("https://takbytepris.nu/","Takbyte pris","Räkna på din takyta – pris per m² för betong, tegel och plåt.")],
  faq=[("Vad kostar ett takbyte?","Det beror på takets area och form, material, lutning, tillgänglighet och underlagets skick. Vi kommer ut gratis och ger ett kostnadsförslag med fast pris för just ditt tak."),
       ("Är takbyte dyrare med tegel eller plåt?","Det varierar. Materialen skiljer sig i pris, vikt och läggningstid, och valet påverkar även livslängd och underhåll. Vi går igenom alternativen vid besöket."),
       ("Ingår rivning i priset?","I en komplett offert från oss ingår rivning och bortforsling av det gamla taket. Kontrollera alltid att det ingår när du jämför offerter."),
       ("Hur mycket ROT-avdrag får man på ett takbyte?","Under 2026 är ROT-avdraget 30 % av arbetskostnaden, högst 50 000 kr per person och år. Material ger inget avdrag. Avdraget görs direkt på fakturan."),
       ("Vad räknas som arbetskostnad vid ett takbyte?","Rivning, läggning av underlagspapp, läkt och pannor eller plåt samt plåtarbeten. Material, utrustning och resor räknas inte som arbetskostnad och ger inget ROT-avdrag."),
       ("Vad kostar ett takbyte per kvm?","Kvm-priset beror på material, lutning, underlagets skick och detaljer som kupor och skorsten. Räkna med takytan, inte husets boyta – takytan är större ju brantare taket är. Vi ger fast pris efter ett gratis besök."),
       ("Gäller 50 % ROT fortfarande?","Nej. Den tillfälliga höjningen till 50 % gällde betalningar mellan 12 maj och 31 december 2025. Från 2026 är ROT-avdraget 30 % av arbetskostnaden.")],
  badge="Kostnad", read="7 min")

article("vad-kostar-takrenovering.html",
  "Vad kostar takrenovering och takomläggning? Det styr priset",
  "Vad kostar en takrenovering eller takomläggning på villa? Så påverkar omfattning, underlag, plåt och ställning priset – och så räknar du ROT-avdraget.",
  "Vad kostar en takrenovering?",
  "En takrenovering kostar oftast mindre än ett fullt takbyte, men spannet är stort beroende på omfattning. Här går vi igenom vad som styr priset – från byte av enstaka pannor till en hel takomläggning.",
  [("p","Takrenovering omfattar allt från byte av enstaka pannor till full omläggning med ny underlagspapp. Därför varierar priset kraftigt. Kostnaden avgörs av hur stor del av taket som åtgärdas, materialet och hur utsatta detaljerna är. Vi lämnar inga schablonpriser – du får ett fast pris efter ett gratis besök."),
   ("h2","Tre nivåer av takrenovering"),
   ("ul",["<strong>Punktinsats</strong> – byte av spruckna pannor, en lös nockpanna eller ett otätt skorstensbeslag. Liten omfattning, men ställning eller lift kan ändå behövas.",
          f"<strong>Takomläggning</strong> – pannorna lyfts av, ny underlagspapp och ny läkt läggs och hela pannor läggs tillbaka. Läs mer om {a('takrenovering.html','takrenovering och takomläggning')}.",
          f"<strong>Plåt- och detaljarbeten</strong> – nya vindskivor, fotplåt, ränndalar, {a('hangrannor-stupror.html','hängrännor och stuprör')}, ofta i samma omgång som omläggningen."]),
   ("h2","Vad påverkar priset?"),
   ("ul",["Omfattning – punktinsats eller omläggning av hela takytan.",
          "Om underlagspapp och läkt behöver bytas, och om råsponten är skadad under pappen.",
          "Hur många pannor som är trasiga och måste ersättas med nya.",
          "Antal plåtdetaljer och anslutningar: skorsten, takfönster, kupor och ränndalar.",
          "Taklutning, höjd och behov av ställning.",
          "Tillgänglighet för material, container och ställning på tomten."]),
   ("h2","Takomläggning eller takbyte – vad blir billigast?"),
   ("p",f"Vid en omläggning återanvänds pannorna, så materialkostnaden blir lägre än vid ett nytt tak. Men om många pannor är porösa eller frostskadade och ändå måste bytas, krymper skillnaden. Då kan ett {a('takbyte.html','takbyte')} bli bättre på sikt. Jämför i {a('vad-kostar-takbyte.html','vad ett takbyte kostar')} och {a('takbyte-eller-takrenovering.html','takbyte eller takrenovering')}."),
   ("h2","Platsbesök och kostnadsförslag"),
   ("p",f"Inför en takrenovering gör vi alltid ett gratis platsbesök och lämnar kostnadsförslag. Vid besöket bedömer vi pannor, underlag och plåt och föreslår rätt nivå. Läs mer om {a('takbesiktning.html','takbesiktning')}."),
   ("h2","ROT-avdrag på takrenovering"),
   ("p",f"Takrenovering och takomläggning räknas som reparation och underhåll och ger ROT-avdrag på arbetskostnaden: 30 % under 2026, högst 50 000 kr per person och år. Material ger inget avdrag. Räkna på ditt fall i guiden om {a('rot-avdrag-takarbete.html','ROT-avdrag för takarbete')}."),
   ("h2","Så jämför du offerter på takrenovering"),
   ("ul",["Står det vilken nivå som ingår – punktinsats, omläggning eller båda?",
          "Ingår ny underlagspapp och läkt, och vad händer om råsponten är skadad?",
          "Hur många nya pannor räknar offerten med?",
          "Ingår ställning, rivning och bortforsling?",
          "Står arbete och material på separata rader så att ROT kan räknas?"]),
   ("cta",("Vill du veta vad din takrenovering kostar?","Vi tittar på taket gratis och ger ett fast pris med ROT-avdraget uträknat."))],
  [("takrenovering.html","Takrenovering","Vår tjänst för takrenovering och omläggning."),
   ("vad-kostar-takbyte.html","Vad kostar ett takbyte?","Jämför med kostnaden för byte."),
   ("rot-avdrag-takarbete.html","ROT-avdrag","Sänk kostnaden med ROT.")],
  faq=[("Vad kostar en takomläggning?","Det beror på takets storlek, hur många pannor som måste bytas, underlagets skick och plåtdetaljerna. Vi ger fast pris efter ett gratis besök."),
       ("Är takomläggning billigare än takbyte?","Oftast, eftersom pannorna återanvänds. Är många pannor skadade krymper skillnaden och ett takbyte kan bli bättre på sikt."),
       ("Får man ROT-avdrag på takrenovering?","Ja, på arbetskostnaden: 30 % under 2026, högst 50 000 kr per person och år."),
       ("Kostar det något att få ett kostnadsförslag?","Nej. Inför ett takprojekt gör vi ett gratis platsbesök och lämnar kostnadsförslag med fast pris.")],
  badge="Kostnad", read="6 min")

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
  "ROT-avdrag för takbyte och takomläggning 2026 – räkna själv",
  "ROT-avdrag 2026 för takbyte, takomläggning och takrenovering: 30 % av arbetskostnaden, max 50 000 kr per person. Villkor, exempel och ROT-räknare.",
  "ROT-avdrag för takarbete",
  "Takarbete på villa ger normalt rätt till ROT-avdrag på arbetskostnaden. Här förklarar vi hur det fungerar och vad du behöver tänka på.",
  [("p","ROT-avdraget gör att du får dra av en del av arbetskostnaden för renovering och underhåll av din bostad. Takbyte, takrenovering och de flesta takarbeten på villa omfattas, förutsatt att du äger bostaden och uppfyller villkoren."),
   ("h2","Hur mycket är ROT-avdraget?"),
   ("p","Avdraget gäller arbetskostnaden – inte material, resor eller administration. För 2026 är ROT-avdraget 30 % av arbetskostnaden, med ett tak på 50 000 kr per person och år. ROT och RUT delar dessutom ett gemensamt tak på 75 000 kr per person och år (Skatteverket)."),
   ("p","Den tillfälliga höjningen till 50 % gällde bara arbeten som betalades mellan 12 maj och 31 december 2025. Får du en offert under 2026 är det alltså 30 % som gäller."),
   ("h2","Räkna ut ROT-avdraget"),
   ("html",ROT_TOOL),
   ("h2","Vilka takarbeten ger ROT-avdrag?"),
   ("p","ROT gäller reparation, underhåll, ombyggnad och tillbyggnad av din bostad. På ett villatak omfattar det normalt arbetet vid:"),
   ("ul",[f"{a('takbyte.html','Takbyte')} – rivning, nytt underlag och nya pannor eller plåt.",
          f"{a('takrenovering.html','Takomläggning och takrenovering')} – samma pannor läggs tillbaka på nytt underlag.",
          f"Plåtarbeten, {a('hangrannor-stupror.html','hängrännor och stuprör')} och {a('skorstensrenovering.html','skorstensrenovering')}.",
          f"{a('takmalning.html','Målning av plåttak')} och reparation av läckage."]),
   ("p","Avdraget gäller bara arbetet. Pannor, plåt, papp, container och resor betalar du fullt för."),
   ("h2","Villkor för ROT-avdrag på taket"),
   ("ul",["Du äger bostaden och bor i den eller använder den som fritidshus.",
          "Arbetet utförs av ett företag med F-skatt.",
          "Arbetskostnaden står separat på fakturan.",
          "Du har tillräckligt med skatt att reducera och har inte redan använt hela ditt utrymme för året.",
          "Är huset nybyggt kan särskilda regler gälla – kontrollera med Skatteverket."]),
   ("p",f"Källa: {SKV_ROT}. Vi har F-skatt och sköter ansökan om utbetalning åt dig."),
   ("h2","Så fungerar det i praktiken"),
   ("ol",["Vi bedömer taket och lämnar offert.","Arbetskostnaden specificeras separat.",
          "Avdraget dras direkt på fakturan.","Vi begär utbetalning från Skatteverket."]),
   ("tips","ROT-avdraget är personligt och delas på antal ägare. Bor ni två som äger huset kan avdraget ofta bli högre totalt."),
   ("cta",("Vi hjälper dig med ROT","Vi drar av ROT direkt på fakturan – du ser din slutkostnad tydligt i offerten."))],
  [("takbyte.html","Takbyte","ROT gäller normalt vid takbyte."),
   ("vad-kostar-takbyte.html","Vad kostar ett takbyte?","Se hur ROT påverkar slutpriset."),
   ("bygglov-takbyte.html","Bygglov för takbyte","Vad som gäller kring tillstånd.")],
  faq=[("Gäller ROT för materialkostnaden?","Nej, ROT-avdraget gäller endast arbetskostnaden, inte material eller resekostnader."),
       ("Får man ROT-avdrag för takomläggning?","Ja. Takomläggning är reparation och underhåll av bostaden, så arbetskostnaden ger ROT-avdrag på 30 % under 2026, högst 50 000 kr per person och år."),
       ("Är ROT-avdraget 50 % 2026?","Nej. 50 % gällde tillfälligt för betalningar mellan 12 maj och 31 december 2025. Från 2026 är det 30 % av arbetskostnaden."),
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
   ("tips","Var vaksam på ovanligt låga priser och krav på stora förskott. Seriösa företag ger tydliga, jämförbara offerter. Vill du jämföra fler kan du <a href=\"https://byggtorg.se/takarbeten/\">få offerter på takarbeten</a> via Byggtorg."),
   ("cta",("Begär en tydlig offert av oss","Vi ger en specificerad offert med omfattning, material och tidplan – enkel att jämföra."))],
  [("takbesiktning.html","Takbesiktning","Bra underlag inför offertjämförelse."),
   ("om-oss.html","Om oss","Så arbetar vi."),
   ("villatak.html","Tak på villa","Komplett guide till villatak.")],
  faq=[("Ska jag välja billigaste offerten?","Inte automatiskt. Jämför vad som ingår. En billig offert som saknar underlagsbyte eller plåtarbeten kan bli dyrare totalt.")],
  badge="Checklista", read="4 min")

article("bygglov-takbyte.html",
  "Bygglov för takbyte – regler från 1 december 2025 | Geal Entreprenad AB",
  "Sedan 1 december 2025 krävs normalt inget bygglov för att byta takmaterial eller kulör på villa och radhus. Här är undantagen som fortfarande gäller.",
  "Behövs bygglov för takbyte?",
  "Plan- och bygglagen ändrades 1 december 2025. För villor och radhus blev takbyte enklare – men inte helt regelfritt.",
  [("p","Med de nya reglerna i 9 kap. plan- och bygglagen (PBL) krävs inte längre bygglov för fasadändringar på en- och tvåbostadshus – villor, parhus och radhus. Det gäller även taket: att byta takmaterial, till exempel från betongpannor till plåt, eller att byta kulör kräver normalt inget bygglov."),
   ("h2","När krävs ändå bygglov?"),
   ("ul",["Huset eller området är särskilt värdefullt ur historisk, kulturhistorisk, miljömässig eller konstnärlig synpunkt – då gäller utökad lovplikt för fasadändringar.",
          "Det är ett flerbostadshus eller en annan byggnad inom detaljplan, och taket vetter mot gata eller annan allmän plats.",
          "Taket höjs över befintlig taknock – då räknas det som en tillbyggnad som kräver bygglov."]),
   ("h2","När krävs anmälan?"),
   ("p","Även utan bygglov kräver vissa takarbeten anmälan och startbesked enligt plan- och byggförordningen (PBF 6 kap. 1 §): när bärande delar som takstolar ändras väsentligt, och vid installation eller väsentlig ändring av eldstad, rökkanal eller ventilation – till exempel om skorstenen byggs om."),
   ("h2","Lovfritt är inte regelfritt"),
   ("p","Varsamhetskravet och förbudet mot att förvanska byggnader i 8 kap. PBL gäller fortfarande. Ett nytt tak ska passa husets karaktär, och kommunen kan ingripa i efterhand om en lovfri åtgärd förvanskar ett värdefullt hus. Tekniska krav gäller också – till exempel att takstolarna klarar vikten när ett lätt plåttak byts mot tegel."),
   ("p",'Källa: <a class="text-link" href="https://www.boverket.se/sv/samhallsplanering/uppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/" rel="noopener">Boverket – PBL-ändringar från 1 december 2025</a>. Lagtext: <a class="text-link" href="https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/" rel="noopener">PBL 9 kap. 15 och 37 §§</a> och <a class="text-link" href="https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-byggforordning-2011338_sfs-2011-338/" rel="noopener">PBF 6 kap. 1 §</a> (riksdagen.se). Gäller från 1 december 2025.'),
   ("tips","Osäker på om ditt hus räknas som särskilt värdefullt? Fråga kommunens bygglovsenhet. Du kan också söka frivilligt bygglov för att få besked i förväg."),
   ("cta",("Planerar du ett takbyte?","Vi hjälper dig bedöma materialval och vad som gäller – begär en offert."))],
  [("takbyte.html","Takbyte","Vår tjänst för takbyte."),
   ("tegel-betong-plattak.html","Tegel vs betong vs plåt","Jämför material inför takbytet."),
   ("rot-avdrag-takarbete.html","ROT-avdrag","Ekonomin kring takbyte.")],
  faq=[("Krävs bygglov för att byta från tegel till plåt på en villa?","Normalt inte sedan 1 december 2025. Undantaget är särskilt värdefulla byggnader och områden, där bygglov fortfarande krävs."),
       ("Krävs bygglov om jag byter tegel mot likadant tegel?","Nej."),
       ("Vem ansvarar för att reglerna följs?","Fastighetsägaren. Vi hjälper dig bedöma materialval och om huset kan räknas som särskilt värdefullt.")],
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
  "Plåttak eller betongpannor? Jämför tegel, betong och plåt",
  "Plåttak, betongpannor eller tegeltak? Vi jämför livslängd, vikt, lutning, underhåll och utseende så att du väljer rätt takmaterial vid takbytet.",
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
   ("h2","Plåttak eller betongpannor – vad passar ditt hus?"),
   ("ul",["<strong>Taklutning:</strong> pannor kräver en minsta lutning enligt tillverkarens anvisningar. Låglutande tak blir oftast plåt.",
          "<strong>Vikt:</strong> plåt är betydligt lättare än pannor. Ska du gå från plåt till pannor måste takstolarna klara den högre vikten.",
          "<strong>Ljud:</strong> regn hörs mer på plåt, särskilt om vinden är oisolerad.",
          "<strong>Snö:</strong> snön glider lättare av plåt, så snörasskydd över entréer och gångar är extra viktigt.",
          "<strong>Utseende:</strong> husets stil och grannskapet väger tungt – i äldre områden passar ofta tegel eller falsad plåt bäst."]),
   ("h2","Tegeltak eller plåttak?"),
   ("p",f"Tegel ger lång livslängd och ett klassiskt uttryck men är tungt. Plåt är lätt, klarar låga lutningar och kan målas om, men kräver noggranna plåtarbeten för att bli tätt. På äldre hus med tegeltak är en {a('takrenovering.html','takomläggning')} där teglet läggs tillbaka ofta ett alternativ till att byta material."),
   ("h2","Underhåll per material"),
   ("ul",[f"Betongpannor: {a('taktvatt.html','taktvätt')} och mossbehandling när påväxten tar fart.",
          f"Plåt: {a('takmalning.html','ommålning')} när färgskiktet släpper, kontroll av falsar och skruvar.",
          "Tegel: byte av enstaka spruckna pannor och kontroll av nock och anslutningar."]),
   ("p",f"Se hur länge materialen håller i {a('takmaterial-livslangd.html','livslängd per takmaterial')}. Vill du ha plåt hjälper vi dig med {a('plattak.html','plåttak')}, och byte sköts via {a('takbyte.html','takbyte')}."),
   ("tips","Byter du från plåt till pannor – kontrollera att takstolarna klarar den högre vikten. Bygglov krävs normalt inte för villor sedan 1 december 2025, se guiden om bygglov för takbyte.")],
  [("takmaterial-livslangd.html","Livslängd per material","Så länge håller taken."),
   ("plattak.html","Plåttak","Vår tjänst för plåttak."),
   ("bygglov-takbyte.html","Bygglov för takbyte","Vid byte av material.")],
  faq=[("Vilket takmaterial är billigast?","Betongpannor har oftast lägst materialkostnad. Totalkostnaden beror dock även på tak, underlag och arbete."),
       ("Är plåttak bättre än tegel?","Inget är objektivt bäst. Plåt passar låga lutningar och ger låg vikt; tegel ger lång livslängd och klassiskt utseende."),
       ("Kan man byta från betongpannor till plåttak?","Ja. Plåt är lättare än pannor, så takstolarna klarar normalt vikten. Bygglov krävs normalt inte för villor sedan 1 december 2025, utom där detaljplanen har skyddsbestämmelser."),
       ("Låter plåttak mer när det regnar?","Ja, regn hörs mer på plåt än på pannor, särskilt med oisolerad vind.")],
  badge="Material", read="6 min")

article("takmaterial-livslangd.html",
  "Hur länge håller ett tak? Livslängd för tegel, plåt & papp",
  "Hur länge håller ett tak? Riktvärden för tegelpannor, betongpannor, plåttak och papptak – och varför underlagspappen ofta avgör när taket måste bytas.",
  "Livslängd per takmaterial",
  "Hur länge ett tak håller beror på material, utförande och underhåll. Här är typiska livslängder och vad som förlänger dem.",
  [("p","Att känna till takets förväntade livslängd hjälper dig planera ekonomiskt. Siffrorna nedan är riktvärden – läge, lutning och underhåll påverkar utfallet mycket."),
   ("h2","Typisk livslängd"),
   ("ul",["<strong>Tegelpannor:</strong> 50+ år.","<strong>Betongpannor:</strong> 30–50 år.",
          "<strong>Plåttak:</strong> 40–50 år, kan ommålas.","<strong>Papptak:</strong> 20–30 år.",
          "<strong>Underlagspapp:</strong> 30–40 år (ofta takets svaga länk)."]),
   ("h2","Hur länge håller ett tegeltak?"),
   ("p","Lertegel är det mest långlivade pannmaterialet, och livslängden brukar anges till 50 år eller mer. Det är sällan teglet som tar slut först – på äldre tegeltak är det oftast underlagspappen och läkten som är uttjänta. Då räcker en omläggning där samma pannor läggs tillbaka."),
   ("h2","Hur länge håller betongpannor?"),
   ("p","För betongpannor brukar livslängden anges till 30–50 år, beroende på läge, lutning och underhåll. Med åren slits ytskiktet, pannorna suger mer vatten och blir känsligare för frost och mossa. Vittrar pannorna eller spricker de i kyla är det dags för nya pannor, inte bara nytt underlag."),
   ("h2","Hur länge håller ett plåttak?"),
   ("p",f"Ett plåttak brukar hålla 40–50 år, och tillverkare anger att den tekniska livslängden kan nå upp emot 50 år om taket hålls rent från mossa och smuts ({PLANNJA_FAQ}). Livslängden kan förlängas med {a('takmalning.html','takmålning')} när färgskiktet börjat släppa. Rost vid falsar, skruvar och infästningar är tecken på att taket behöver åtgärdas."),
   ("h2","Hur länge håller ett papptak?"),
   ("p",f"Papptak brukar hålla 20–30 år, kortare på låglutande tak där vatten blir stående. Blåsor, sprickor och lösa skarvar är varningstecken – då är det dags att {a('papptak.html','byta papptaket')}. Även under pannor och plåt finns papp – underlagspappen – som ofta håller 30–40 år och därför är takets svaga länk."),
   ("h2","Vad förlänger livslängden?"),
   ("ul",[f"Regelbunden {a('taktvatt.html','taktvätt')} och borttagning av mossa.",
          "Fungerande avvattning och ventilation.","Åtgärd av små skador i tid.",
          "Kontroll vid varje säsongsskifte."]),
   ("p",f"Ofta är det underlagspappen, inte pannorna, som avgör när ett {a('takbyte.html','takbyte')} behövs. En {a('takbesiktning.html','takbesiktning')} visar var ditt tak står."),
   ("tips","Pannor kan se fina ut länge medan underlagspappen under dem är uttjänt – bedöm alltid helheten.")],
  [("tegel-betong-plattak.html","Jämför takmaterial","För- och nackdelar."),
   ("takbesiktning.html","Takbesiktning","Bedöm ditt taks status."),
   ("takbyte.html","Takbyte","När livslängden är nådd.")],
  faq=[("Vilket takmaterial håller längst?","Lertegel brukar ha längst livslängd, ofta 50 år eller mer. Plåt och betongpannor ligger lägre, och papptak har kortast livslängd."),
       ("Hur länge håller underlagspappen?","Underlagspapp brukar hålla 30–40 år. Den är ofta takets svaga länk och avgör när ett tegel- eller betongtak behöver läggas om."),
       ("Kan man förlänga takets livslängd?","Ja. Regelbunden taktvätt, fungerande avvattning och ventilation och att små skador åtgärdas i tid förlänger livslängden. Plåttak kan målas om."),
       ("Hur vet jag att taket är slut?","Spruckna eller vittrande pannor, rost på plåten, blåsor i papp och fukt på vinden är vanliga tecken. En takbesiktning ger besked.")],
  badge="Material", read="5 min")

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
  "Solceller på tak – kolla taket först, sedan montering",
  "Solceller på tak: varför takets skick avgör, när du ska byta tak först och hur infästningarna hålls täta. Vi monterar solceller och byter tak.",
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
  crumbs=[("Hem","/"),("Vanliga frågor","faq.html")],
  cta=("Har du en fråga vi inte besvarat?","Kontakta oss så hjälper vi dig – gratis platsbesök och kostnadsförslag."),
  body=hero("Vanliga frågor om tak",
    "Här har vi samlat de vanligaste frågorna vi får om takbyte, takrenovering, pris, ROT-avdrag och garanti. Hittar du inte svaret är du välkommen att kontakta oss.",
    [("Hem","/"),("Vanliga frågor","faq.html")])
    + links_block("Läs mer om våra tjänster", [
        ("takbyte.html","Takbyte","Komplett byte av tegel-, betong- och plåttak."),
        ("takrenovering.html","Takrenovering","Riktade åtgärder som förlänger takets liv."),
        ("rot-avdrag-takarbete.html","ROT-avdrag","Så mycket kan du dra av 2026.")], muted=False),
  faq=[
    ("Vad kostar ett takbyte?","Priset beror på takets area, material, lutning, tillgänglighet och underlagets skick. Vi erbjuder alltid gratis platsbesök och kostnadsförslag så att du får ett fast pris för just ditt tak."),
    ("Får jag ROT-avdrag för takarbete?","Ja, som villaägare får du normalt ROT-avdrag på arbetskostnaden. För 2026 är avdraget 30 % av arbetskostnaden, med ett tak på 50 000 kr per person och år. Vi drar av det direkt på fakturan."),
    ("Hur lång tid tar ett takbyte?","De flesta villatakbyten tar cirka 1–2 veckor beroende på takets storlek, väder och eventuella underliggande skador. Du får en preliminär tidplan i offerten."),
    ("Behöver jag byta hela taket eller räcker en renovering?","Det beror på skicket. Om grundkonstruktionen är sund kan en takrenovering räcka. En takbesiktning ger svar innan du beslutar."),
    ("Lämnar ni garanti på arbetet?","Ja, vi lämnar garanti enligt lag (konsumenttjänstlagen). Villkoren för ditt projekt står i offert och avtal."),
    ("Är offert och platsbesök kostnadsfritt?","Ja, vi erbjuder gratis platsbesök och kostnadsförslag. Du binder dig inte till något genom att begära offert."),
    ("Vilka områden arbetar ni i?","Vi utgår från Bromma och arbetar i alla stadsdelar i Stockholm och i kranskommunerna – från Sundbyberg, Solna och Hässelby till Huddinge, Värmdö och Österåker."),
    ("Behövs bygglov för takbyte?","Normalt inte för villa eller radhus: sedan 1 december 2025 krävs inget bygglov för att byta takmaterial eller kulör på en- och tvåbostadshus. Undantaget är särskilt kulturhistoriskt värdefulla hus och områden."),
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
  ("p","Nödvändiga funktioner på webbplatsen kräver inga cookies, och typsnitt och bilder laddas från vår egen server. På kontaktsidan visas en inbäddad karta från OpenStreetMap som kan ta emot din IP-adress när kartan laddas."),
  ("p","För statistik och marknadsföring använder vi Google Analytics 4 och Meta-pixel. Dessa laddas <strong>endast om du aktivt samtycker</strong> i vår cookie-banner (Consent Mode v2, standardläge nekat). Väljer du \"Endast nödvändiga\" laddas ingen mät- eller marknadsföringscookie. Du kan när som helst ändra dig genom att rensa webbplatsens lagring i din webbläsare."),
  ("h2","Dina rättigheter"),
  ("ul",["Få tillgång till de uppgifter vi har om dig.","Begära rättelse av felaktiga uppgifter.","Begära radering eller begränsning av behandlingen.","Invända mot behandlingen och begära dataportabilitet.","Lämna klagomål till Integritetsskyddsmyndigheten (IMY)."]),
  ("p","Vill du utöva någon av dina rättigheter kontaktar du oss på <a class=\"text-link\" href=\"mailto:info@villatakservice.se\">info@villatakservice.se</a>."),
]
page(file="integritetspolicy.html", no_cta=True,
  title="Integritetspolicy | Geal Entreprenad AB",
  description="Integritetspolicy för villatakservice.se (Geal Entreprenad AB). Så behandlar vi dina personuppgifter enligt GDPR när du kontaktar oss.",
  h1="Integritetspolicy",
  crumbs=[("Hem","/"),("Integritetspolicy","integritetspolicy.html")],
  body=hero("Integritetspolicy",
    "Vi värnar om din integritet. Här beskriver vi hur Geal Entreprenad AB behandlar dina personuppgifter enligt dataskyddsförordningen (GDPR).",
    [("Hem","/"),("Integritetspolicy","integritetspolicy.html")])
    + '      <section class="section">\n        <article class="container article-shell content-prose">\n'
    + prose(_pol_blocks)
    + '\n        </article>\n      </section>')

_villkor_blocks = [
  ("p","<em>Senast uppdaterad 2026-10-24.</em>"),
  ("h2","Offert"),
  ("p","Platsbesök och offert är kostnadsfria, och du binder dig inte till något genom att begära offert. Offerten anger omfattning, material, fast pris och preliminär tidplan."),
  ("h2","Garanti"),
  ("p","Vi lämnar garanti enligt lag, konsumenttjänstlagen (1985:716). Villkoren för ditt projekt står i offert och avtal."),
  ("h2","Betalning och ROT-avdrag"),
  ("p",f"Du betalar mot faktura. ROT-avdraget dras direkt på fakturan, så du betalar bara din del, och vi begär utbetalningen från Skatteverket. Avdraget gäller enligt Skatteverkets regler, se {SKV_ROT} och vår guide om {a('rot-avdrag-takarbete.html','ROT-avdrag för takarbete')}."),
  ("h2","Konsumenttjänstlagen"),
  ("p","Anlitar du oss som privatperson gäller konsumenttjänstlagen (1985:716)."),
  ("h2","Företagsuppgifter"),
  ("p",f"{BRAND}, org.nr {ORGNR}, {STREET}, {ZIP} {CITY}. F-skatt och ansvarsförsäkring. Kontakt: <a class=\"text-link\" href=\"mailto:{EMAIL}\">{EMAIL}</a>, <a class=\"text-link\" href=\"tel:{PHONE_T}\">{PHONE_D}</a>."),
]
page(file="villkor.html", no_cta=True,
  title="Villkor | Geal Entreprenad AB",
  description="Villkor för takarbete hos Geal Entreprenad AB: kostnadsfri offert, betalning mot faktura, ROT-avdrag och konsumenttjänstlagen.",
  h1="Villkor",
  crumbs=[("Hem","/"),("Villkor","villkor.html")],
  body=hero("Villkor",
    "Så fungerar offert, garanti, betalning och ROT-avdrag när du anlitar Geal Entreprenad AB.",
    [("Hem","/"),("Villkor","villkor.html")])
    + '      <section class="section">\n        <article class="container article-shell content-prose">\n'
    + prose(_villkor_blocks)
    + '\n        </article>\n      </section>')

# ====================== BYGG & RENOVERING ==============================
BYGG_CRUMB = [("Hem","/"),("Bygg & Renovering","bygg.html")]

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
        ("friggebod.html","Friggebod","Komplementbyggnad upp till 30 m²."),
        ("nybyggnad-villa.html","Nybyggnad / nyckelfärdigt hus","Bygg villa från grunden."),
        ("fritidshus.html","Bygga fritidshus","Nyckelfärdigt fritidshus."),
        ("villatak.html","Tak på villa","Vår ursprungliga specialitet."),
        ("vad-kostar-bygga-hus.html","Vad kostar det att bygga hus?","Prisbild och vad som påverkar kostnaden."),
        ("hyra-taklaggare.html","Hyra takläggare","Bemanning bygg: takläggare, plåtslagare och byggarbetare.")]
        + [(f, TJ[f]["h1"], TJ[f]["card"]) for f, d in TJ.items() if d["kind"] == "hub"], muted=False),
  faq=[
    ("Vad betyder total entreprenad?","Att en entreprenör ansvarar för hela projektet – projektering, hantverk och samordning – så att du bara har en kontakt och ett avtal."),
    ("Gör ni både tak och övrig bygg?","Ja. Vi startade med tak och gör i dag även renovering, tillbyggnad, attefallshus och nybyggnad, ofta i samma projekt."),
    ("Kan jag få ROT-avdrag?","ROT gäller arbete på befintlig bostad, till exempel renovering. Nybyggnad ger inte ROT, men en tillbyggnad kan ge det om den sitter ihop med husets yttervägg till minst 75 procent eller har en dörr emellan. Vi reder ut vad som gäller i din offert.")])

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
          <p>ROT gäller arbetskostnaden vid renovering av befintlig bostad (30 % 2026, max 50 000 kr/person/år). Nybyggnad ger inte ROT. En tillbyggnad kan ge ROT om den sitter ihop med husets yttervägg till minst 75 procent eller har en dörr emellan – vi särskiljer detta i offerten. Mer i {a('rot-avdrag-takarbete.html','guiden om ROT-avdrag')}.</p>
        </div></div>
      </section>"""
    + (tj_list_html("Byggföretag per område", TJ_DISTRICTS["byggforetag"], muted=True, sid="omraden") if TJ_DISTRICTS.get("byggforetag") else "")
    + links_block("Relaterat", [
        ("villarenovering.html","Villarenovering","Total- och delrenovering."),
        ("tillbyggnad.html","Tillbyggnad","Utöka boytan."),
        ("nybyggnad-villa.html","Nybyggnad","Bygg nytt från grunden.")], muted=not TJ_DISTRICTS.get("byggforetag")),
  faq=[
    ("Vad kostar en byggfirma / total entreprenad?","Det beror helt på projektets omfattning. Vi erbjuder gratis platsbesök och kostnadsförslag och lämnar ett fast pris efter genomgång."),
    ("Tar ni bygglovet?","Vi hjälper till med bygglovsunderlag och ritningar; själva ansökan görs till kommunen och vi guidar dig genom den."),
    ("Har ni försäkring och F-skatt?","Ja, vi är ett registrerat AB med F-skatt och ansvarsförsäkring, och våra hantverkare är anslutna till ID06.")])

def tiles(title, items, muted=False, sid=""):
    # Enkla rutor utan länk (samma mönster som "Värderingar" på Om oss).
    arts = "\n".join(f"""            <article class="service-snippet">
              <h3>{h}</h3>
              <p>{t}</p>
            </article>""" for h,t in items)
    cls = "section section-muted seo-section" if muted else "section seo-section"
    idattr = f' id="{sid}"' if sid else ""
    return f"""      <section class="{cls}"{idattr}>
        <div class="container">
          <h2 class="section-title">{title}</h2>
          <div class="grid-3">
{arts}
          </div>
        </div>
      </section>"""

HYRA_CRUMB = SVC_CRUMB+[("Hyra takläggare","hyra-taklaggare.html")]
page(file="hyra-taklaggare.html", service=True,
  service_type="Bemanning bygg – uthyrning av takläggare, plåtslagare och byggarbetare",
  title="Hyra takläggare – bemanning bygg i Stockholm | Geal Entreprenad AB",
  description="Hyra takläggare, plåtslagare eller byggarbetare till ert bygge i Stockholm. Bemanning bygg från en takfirma – pris per timme eller per jobb.",
  h1="Hyra takläggare i Stockholm",
  crumbs=HYRA_CRUMB,
  cta=("Behöver ni fler på bygget?","Berätta vad ni behöver – vi lämnar offert."),
  body=hero("Hyra takläggare i Stockholm",
    "Bemanning bygg: vi hyr ut egna takläggare, plåtslagare och byggarbetare till byggföretag och entreprenörer.",
    HYRA_CRUMB,
    trust=["Pris per timme eller per jobb","F-skatt, ansvarsförsäkring och ID06"])
    + tiles("Vilka vi hyr ut", [
        ("Takläggare","Takbyte, takomläggning och nya tak."),
        ("Plåtslagare","Plåttak, beslag, hängrännor och stuprör."),
        ("Byggarbetare","Rivning, tillbyggnad och allmänt bygg.")], muted=True)
    + sec_process("Så går det till", [
        ("Förfrågan","Yrke, antal, plats och period."),
        ("Vi bekräftar","Vilka som kommer och när de börjar."),
        ("På plats","Våra hantverkare börjar på ert bygge.")], grid="grid-3"),
  faq=[
    ("Vad kostar det att hyra takläggare?","Pris per timme eller per jobb – vi lämnar offert."),
    ("Kan vi hyra plåtslagare och byggarbetare också?","Ja. Vi hyr ut takläggare, plåtslagare och byggarbetare – var för sig eller tillsammans. Snickare, betongarbetare och armerare hittar ni på <a href=\"https://gealab.nu/bemanning/\">bemanning bygg hos Geal</a>."),
    ("Har ni F-skatt och ID06?","Ja, vi är ett registrerat AB med F-skatt och ansvarsförsäkring, och våra hantverkare är anslutna till ID06."),
    ("Hur länge kan vi hyra?","Det bestämmer vi tillsammans utifrån ert projekt."),
    ("Var kan ni jobba?","I Stockholm med omnejd. Fråga oss gärna om andra orter.")])

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
    + (tj_list_html("Totalrenovering per område", TJ_DISTRICTS["totalrenovering"], muted=True, sid="omraden") if TJ_DISTRICTS.get("totalrenovering") else "")
    + links_block("Relaterat", [
        ("byggfirma.html","Total entreprenad","En entreprenör för hela renoveringen."),
        ("tillbyggnad.html","Tillbyggnad","Kombinera renovering med mer yta."),
        ("takrenovering.html","Takrenovering","Renovera taket samtidigt.")], muted=not TJ_DISTRICTS.get("totalrenovering")),
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
        "Sedan 1 december 2025 får du bygga till sammanlagt 30 m² utan bygglov, om tillbyggnaden inte går över husets taknock och håller 4,5 meter till tomtgräns eller har grannens skriftliga medgivande. Större tillbyggnader kräver bygglov – vi hjälper till med ritningar och bygglovsunderlag, och planerar sedan grund, stomme, tak och ytskikt så att tillbyggnaden ansluter tätt och snyggt mot befintligt hus.",
        "En välplanerad anslutning mot tak och fasad är avgörande för att undvika framtida fukt- och läckageproblem."],
        "Så går det till", [
        "Behovsgenomgång och förslag.","Ritning och bygglovsunderlag.",
        "Grund och stomme.","Tak, fasad och tät anslutning.",
        "Invändig komplettering.","Slutbesiktning."], sid="bygglov")
    + f"""      <section class="section seo-section">
        <div class="container"><div class="tips-box">
          <h3>ROT och tillbyggnad</h3>
          <p>En tillbyggnad av ett småhus kan ge ROT-avdrag om någon av tillbyggnadens sidor sitter ihop med husets yttervägg till minst 75 procent eller om det finns en dörr emellan, och om huset är äldre än fem år. Nybyggnad av ett fristående hus ger inte ROT. Vi är tydliga med vad som gäller i offerten. Läs mer om {a('bygglov-takbyte.html','bygglov')} och {a('rot-avdrag-takarbete.html','ROT')}.</p>
        </div></div>
      </section>"""
    + (tj_list_html("Tillbyggnad per område", TJ_DISTRICTS["tillbyggnad"], muted=True, sid="omraden") if TJ_DISTRICTS.get("tillbyggnad") else "")
    + links_block("Relaterat", [
        ("attefallshus.html","Attefallshus","Fristående yta utan bygglov."),
        ("byggfirma.html","Total entreprenad","Vi tar hela projektet."),
        ("nybyggnad-villa.html","Nybyggnad","Bygga nytt hus."),
        ("attefallshus-regler.html","Attefallsregler","Vad som gäller utan bygglov.")], muted=not TJ_DISTRICTS.get("tillbyggnad")),
  faq=[
    ("Behöver jag bygglov för tillbyggnad?","Inte för tillbyggnader på sammanlagt högst 30 m² som inte går över taknocken (gäller från 1 december 2025). Närmare än 4,5 m från tomtgräns krävs bygglov, om inte grannen skriftligen medgett det. Större tillbyggnader kräver alltid bygglov."),
    ("Hur mycket får jag bygga till?","Det styrs av detaljplan och tomt. Vi går igenom vad som är möjligt vid ett platsbesök."),
    ("Får jag ROT för tillbyggnad?","Ja, för ett småhus om tillbyggnaden sitter ihop med husets yttervägg till minst 75 procent av en sida eller har en dörr mot huset, och huset är äldre än fem år. Avdraget gäller arbetskostnaden, inte material.")])

# Källor för attefall-/friggebodssidorna (kontrollerade 2026-10-25 mot riksdagen.se och boverket.se).
PBL_URL = "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/"
PBF_URL = "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-byggforordning-2011338_sfs-2011-338/"
BOV_LISTA = "https://www.boverket.se/sv/samhallsplanering/uppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/"
KOMPL_SRC = [("Riksdagen – Plan- och bygglag (2010:900), 1 kap. 4 § och 9 kap. 4–5, 10–12, 16, 34–37 §§", PBL_URL),
             ("Riksdagen – Plan- och byggförordning (2011:338), 6 kap. 1 §", PBF_URL),
             ("Boverket – Lista med PBL-ändringar som trädde i kraft 1 december 2025", BOV_LISTA)]

page(file="attefallshus.html", service=True, service_type="Attefallshus",
  title="Attefallshus i Stockholm – regler från 1 december 2025 | Geal Entreprenad AB",
  description="Attefallshus heter i lagen komplementbostadshus sedan 1 december 2025: 30 m² och 4,0 m inom detaljplan, 45 m² per tomt, ingen anmälan för huset.",
  h1="Attefallshus i Stockholm",
  crumbs=BYGG_CRUMB+[("Attefallshus","attefallshus.html")],
  cta=("Funderar du på ett attefallshus?","Vi bygger nyckelfärdigt och hjälper dig med reglerna. Begär en kostnadsfri offert."),
  body=hero("Attefallshus i Stockholm",
    "Attefallshus är i dag ett vardagsnamn. Sedan 1 december 2025 heter huset komplementbostadshus i plan- och bygglagen, och inom detaljplan får det vara upp till 30 m² utan bygglov och utan anmälan. Vi bygger nyckelfärdigt i hela Stockholm.",
    BYGG_CRUMB+[("Attefallshus","attefallshus.html")],
    [("#vad","Om attefallshus"),("#regler","Regler"),("#anmalan","Anmälan"),("#faq","Vanliga frågor"),("#kallor","Källor")],
    trust=TJ_SERVICES["attefallshus"]["trust"])
    + sec("Attefallshus – namnet som blev kvar", [
        "Ordet attefallshus finns inte längre i lagen. Den 1 december 2025 fick plan- och bygglagen ett nytt 9 kapitel, och de lovfria åtgärderna ”attefallshus” och ”friggebod” togs bort. I stället finns två begrepp: <strong>komplementbostadshus</strong> – en fristående byggnad som kompletterar ett en- eller tvåbostadshus och är inredd med en självständig bostad – och <strong>komplementbyggnad</strong>, som inte är inredd med en självständig bostad.",
        f"De flesta säger fortfarande attefallshus, och det är det ordet man söker på. Därför heter sidan så. Menar du ett förråd, en verkstad eller ett gästrum utan egen bostad är det en komplementbyggnad – se {a('friggebod.html','friggebod')}. Alla mått och paragrafer finns samlade i {a('attefallshus-regler.html','nya regler för attefallshus')}.",
        "Populära användningar är gäststuga, hemmakontor, ett litet hus för en vuxen son eller dotter eller ett hus för uthyrning. Vi bygger nyckelfärdigt – från grund till inflyttningsklart."], sid="vad")
    + sec_split("Regler i korthet", [
        "Inom detaljplan får ett komplementbostadshus byggas utan bygglov om byggnadsarean är högst 30,0 m², taknockshöjden högst 4,0 meter och huset står inom tomten. Utanför detaljplan är gränserna 50,0 m² och 4,5 meter. Byggnadsarean ska också vara mindre än byggnadsarean för huset det kompletterar (PBL 9 kap. 4–5 §§).",
        "Alla lovfria komplementbyggnader och komplementbostadshus på tomten delar på en gemensam pott: högst 45,0 m² inom och 65,0 m² utanför detaljplan. I potten räknas även friggebodar och attefallshus som byggts utan lov enligt de äldre reglerna.",
        "Närmare gränsen än 4,5 meter krävs bygglov, om inte de berörda grannarna skriftligen har medgett placeringen (9 kap. 34–35 §§). Lovfritt är inte regelfritt: tekniska krav och varsamhetskrav gäller, och för särskilt värdefulla byggnader och områden krävs bygglov (9 kap. 37 §)."],
        "Vanliga krav", [
        "Max 30 m² inom detaljplan, 50 m² utanför.","Taknockshöjd max 4,0 m (4,5 m utanför detaljplan).",
        "Högst 45 m² lovfritt per tomt (65 m² utanför) – gamla friggebodar räknas in.","Minst 4,5 m till gräns, annars skriftligt grannmedgivande.",
        "Mindre byggnadsarea än villan, och bara vid en- eller tvåbostadshus.","Bygglov för särskilt värdefulla byggnader och miljöer."], sid="regler")
    + sec("Anmälan och startbesked – för installationerna", [
        "Själva huset kräver ingen anmälan. Men enligt plan- och byggförordningen 6 kap. 1 § krävs anmälan för installation eller väsentlig ändring av anläggning för vattenförsörjning eller avlopp, ventilation, eldstad eller rökkanal. Ett hus att bo i får nästan alltid vatten och avlopp, och då ska kommunen ge startbesked innan de installationerna görs.",
        "Har du redan en lovfri komplementbyggnad kan den göras om till komplementbostadshus utan bygglov, om den håller måtten ovan (PBL 9 kap. 16 §). Ligger den närmare gränsen än 4,5 meter krävs lov även för den ändringen, om inte grannarna skriftligen har medgett den."], sid="anmalan")
    + f"""      <section class="section seo-section">
        <div class="container"><div class="tips-box">
          <h3>Bra att veta</h3>
          <p>Ett attefallshus är nybyggnad och ger därför normalt <strong>inte</strong> ROT-avdrag. Ska huset hyras ut eller inredas för boende tillkommer krav – vi går igenom det vid platsbesöket. Se även {a('tillbyggnad.html','tillbyggnad')} om du hellre vill bygga ihop med huset.</p>
        </div></div>
      </section>"""
    + (tj_list_html("Attefallshus per område", TJ_DISTRICTS["attefallshus"], muted=True, sid="omraden") if TJ_DISTRICTS.get("attefallshus") else "")
    + links_block("Relaterat", [
        ("attefallshus-regler.html","Attefallshus – nya regler","Mått, avstånd och anmälan."),
        ("friggebod.html","Friggebod","Nu komplementbyggnad."),
        ("nybyggnad-villa.html","Nybyggnad / nyckelfärdigt","Bygga större hus."),
        ("tillbyggnad.html","Tillbyggnad","Bygg ihop med villan.")], muted=not TJ_DISTRICTS.get("attefallshus")),
  faq=[
    ("Behöver jag bygglov eller anmälan för attefallshus?","Sedan 1 december 2025 krävs varken bygglov eller anmälan för själva huset om det håller sig inom måtten. Anmälan krävs för vatten, avlopp, ventilation och eldstad eller rökkanal."),
    ("Hur stort får ett attefallshus vara?","Inom detaljplan upp till 30 m² byggnadsarea och 4,0 m taknockshöjd, utanför detaljplan upp till 50 m² och 4,5 m. Alla lovfria komplementbyggnader på tomten får tillsammans vara högst 45 m² respektive 65 m²."),
    ("Kan man bo eller hyra ut i ett attefallshus?","Ja, ett komplementbostadshus är inrett med en självständig bostad. Det får byggas vid en- och tvåbostadshus och ska uppfylla kraven på bostäder, till exempel VA och isolering, som vi tar höjd för."),
    ("Räknas vår gamla friggebod in när vi bygger ett attefallshus?","Ja. Friggebodar och attefallshus som byggts utan lov enligt de äldre reglerna ingår i tomtens gemensamma pott på 45 m² inom detaljplan (65 m² utanför)."),
    ("Varför heter det fortfarande attefallshus?","Det är ett vardagsnamn. I lagen heter huset komplementbostadshus sedan 1 december 2025, men det gamla ordet används fortfarande när man pratar och söker.")],
  after_faq=_trp_sources(KOMPL_SRC, muted=True))

page(file="nybyggnad-villa.html", service=True, service_type="Nybyggnad villa",
  title="Bygga villa i Stockholm – nyckelfärdigt hus | Geal Entreprenad AB",
  description="Bygga villa i Stockholm – nyckelfärdigt hus från grunden. Vi tar helheten som total entreprenör: projektering, bygglov och byggnation. Kostnadsfri offert.",
  h1="Bygga villa i Stockholm – nyckelfärdigt",
  howto=("Från ritning till inflyttning – så bygger vi din villa", [
    ("Genomgång","Vi går igenom dina önskemål, tomt och budget."),
    ("Ritning & bygglov","Vi tar fram ritningar och bygglovsunderlag."),
    ("Grund & stomme","Grundläggning, stomme och tätt hus."),
    ("Nyckelfärdigt","Ytskikt, installationer och slutbesiktning.")]),
  crumbs=BYGG_CRUMB+[("Nybyggnad","nybyggnad-villa.html")],
  cta=("Vill du bygga nytt hus?","Vi bygger villa från grunden som total entreprenör. Begär en kostnadsfri genomgång."),
  body=hero("Bygga villa i Stockholm – nyckelfärdigt",
    "Drömmer du om ett nytt hus? Vi bygger villor från grunden i Stockholm som total entreprenör – från ritning och bygglov till nyckelfärdigt och inflyttningsklart.",
    BYGG_CRUMB+[("Nybyggnad","nybyggnad-villa.html")],
    [("#nyckelfardigt","Nyckelfärdigt"),("#process","Process"),("#faq","Vanliga frågor")], trust=["Gratis besök och kostnadsförslag", "Nyckelfärdigt från grund till inflyttning"])
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
        ("byggfirma.html","Total entreprenad","En kontakt för hela bygget."),
        ("vad-kostar-bygga-hus.html","Vad kostar det att bygga hus?","Vad som påverkar kostnaden."),
        ("fritidshus.html","Fritidshus","Bygga fritidshus.")]),
  faq=[
    ("Bygger ni nyckelfärdigt?","Ja, vi tar helheten som total entreprenör – från ritning och bygglov till inflyttningsklart hus."),
    ("Hur lång tid tar det att bygga en villa?","Det beror på storlek, bygglovstider och markförhållanden. Vi ger en realistisk tidplan i offerten."),
    ("Får jag ROT för att bygga nytt?","Nej, ROT gäller inte nybyggnation. Det gäller renovering och underhåll av befintlig bostad.")])

page(file="friggebod.html", service=True, service_type="Friggebod",
  title="Friggebod i Stockholm – nya regler, upp till 30 m² | Geal Entreprenad AB",
  description="Friggebod heter i lagen komplementbyggnad sedan 1 dec 2025: upp till 30 m² och 4,0 m inom detaljplan, utan bygglov eller anmälan. Vi bygger nyckelfärdigt.",
  h1="Friggebod i Stockholm",
  crumbs=BYGG_CRUMB+[("Friggebod","friggebod.html")],
  cta=("Vill du bygga en friggebod?","Vi bygger nyckelfärdigt. Begär en kostnadsfri offert."),
  body=hero("Friggebod i Stockholm",
    "Friggebod är i dag ett vardagsnamn. Sedan 1 december 2025 heter det komplementbyggnad i lagen – och den får vara större: upp till 30 m² inom detaljplan, utan bygglov och utan anmälan. Vi bygger förråd, växthus och verkstad nyckelfärdigt.",
    BYGG_CRUMB+[("Friggebod","friggebod.html")],
    [("#regler","Regler"),("#skillnad","Friggebod vs attefall"),("#faq","Vanliga frågor"),("#kallor","Källor")], trust=["Gratis besök och kostnadsförslag", "Nyckelfärdigt från grund till inflyttning"])
    + sec_split("Regler för friggebod", [
        "Friggebodsreglerna med 15 m² och 3,0 meter gäller inte längre, och ordet friggebod finns inte kvar i plan- och bygglagen. Det som byggs i dag är en <strong>komplementbyggnad</strong> – en fristående byggnad som kompletterar en byggnad och inte är inredd med en självständig bostad, till exempel förråd, garage, växthus eller verkstad.",
        "Inom detaljplan krävs varken bygglov eller anmälan om byggnadsarean är högst 30,0 m², taknockshöjden högst 4,0 meter, byggnadsarean är mindre än för huset den kompletterar och byggnaden står inom tomten. Utanför detaljplan gäller 50,0 m² och 4,5 meter (PBL 9 kap. 4–5 §§).",
        f"Närmare gränsen än 4,5 meter krävs bygglov, om inte grannarna skriftligen har medgett placeringen. Gäller från 1 december 2025. Källa: {SRCA}."],
        "Vad som gäller", [
        "Max 30 m² inom detaljplan, 50 m² utanför.","Taknockshöjd max 4,0 m (4,5 m utanför detaljplan).",
        "Mindre än huvudbyggnaden, placerad på tomten.","Minst 4,5 m till gräns (annars skriftligt grannmedgivande).",
        "Högst 45 m² lovfritt per tomt inom detaljplan.","Ingen självständig bostad – då är det ett komplementbostadshus."], sid="regler")
    + sec("Friggebod eller attefallshus?", [
        f"Måtten är desamma för båda. Skillnaden är innehållet: en komplementbyggnad är inte inredd med en självständig bostad, medan ett komplementbostadshus – i vardagligt tal {a('attefallshus.html','attefallshus')} – är det och bara får byggas vid en- eller tvåbostadshus. Alla lovfria komplementbyggnader och komplementbostadshus på tomten delar på 45 m² inom detaljplan, och friggebodar som redan står där räknas in.",
        "Vill du senare göra om förrådet till en bostad krävs inget bygglov så länge byggnaden håller måtten och står minst 4,5 meter från gränsen. Däremot krävs anmälan och startbesked när vatten, avlopp, ventilation eller eldstad installeras (plan- och byggförordningen 6 kap. 1 §).",
        f"Vill du i stället bygga ihop med huset, se {a('tillbyggnad.html','tillbyggnad')}."], sid="skillnad")
    + links_block("Relaterat", [
        ("attefallshus.html","Attefallshus","Komplementbostadshus för boende."),
        ("tillbyggnad.html","Tillbyggnad","Bygg ihop med villan."),
        ("bygg.html","Bygg & Renovering","Alla våra byggtjänster.")]),
  faq=[
    ("Behöver jag bygglov för en friggebod?","Nej. Sedan 1 december 2025 gäller reglerna för komplementbyggnad: upp till 30 m² inom detaljplan utan bygglov och utan anmälan, om måtten och avstånden hålls."),
    ("Hur stor får en friggebod vara?","Inom detaljplan max 30 m² byggnadsarea och 4,0 m taknockshöjd, utanför detaljplan max 50 m² och 4,5 m."),
    ("Får man bo i en friggebod?","En komplementbyggnad är inte inredd med en självständig bostad. Ska huset ha en egen bostad är det ett komplementbostadshus (tidigare attefallshus), och då krävs anmälan för vatten och avlopp.")],
  after_faq=_trp_sources(KOMPL_SRC, muted=True))

page(file="fritidshus.html", service=True, service_type="Bygga fritidshus",
  title="Bygga fritidshus i Stockholm – nyckelfärdigt | Geal Entreprenad AB",
  description="Bygga fritidshus i Stockholm och Mälardalen – nyckelfärdigt eller platsbyggt. Vi tar helheten från ritning och bygglov till inflyttning. Gratis offert.",
  h1="Bygga fritidshus i Stockholm",
  crumbs=BYGG_CRUMB+[("Fritidshus","fritidshus.html")],
  cta=("Drömmer du om ett fritidshus?","Vi bygger nyckelfärdigt fritidshus. Begär en kostnadsfri genomgång."),
  body=hero("Bygga fritidshus i Stockholm",
    "Vi bygger fritidshus i Stockholm med omnejd – nyckelfärdigt eller platsbyggt. Från ritning och bygglov till ett inflyttningsklart hus, med en byggpartner genom hela projektet.",
    BYGG_CRUMB+[("Fritidshus","fritidshus.html")],
    [("#nyckelfardigt","Nyckelfärdigt"),("#faq","Vanliga frågor")], trust=["Gratis besök och kostnadsförslag", "Nyckelfärdigt från grund till inflyttning"])
    + sec("Nyckelfärdigt eller platsbyggt fritidshus", [
        "Ett nyckelfärdigt fritidshus levereras helt färdigt att flytta in i – vi ansvarar för hela kedjan. Platsbyggt ger mer frihet i utformningen. Vi hjälper dig välja utifrån tomt, budget och önskemål.",
        f"Ett mindre projekt kan lösas som {a('attefallshus.html','attefallshus')} (upp till 30 m²) eller {a('friggebod.html','friggebod')} – sedan 1 december 2025 upp till 30 m² inom detaljplan utan bygglov."], sid="nyckelfardigt")
    + sec_split("Vi tar helheten", [
        "Från första skiss till slutbesiktning håller vi ihop projektet. Tack vare vår takkompetens blir taket tätt och hållbart från start.",
        "Vi hjälper dig med ritningar och bygglovsunderlag; ansökan görs till kommunen."],
        "Det här ingår", [
        "Genomgång av tomt, önskemål och budget.","Ritning och bygglovsunderlag.",
        "Grund, stomme och tätt hus.","Tak, fasad och installationer.",
        "Ytskikt och inredning.","Slutbesiktning."])
    + f"""      <section class="section seo-section">
        <div class="container"><div class="tips-box">
          <h3>Bra att veta</h3>
          <p>Nybyggnation av fritidshus ger normalt <strong>inte</strong> ROT-avdrag. Renoverar du ett befintligt fritidshus kan ROT gälla. Se även {a('nybyggnad-villa.html','bygga villa')}.</p>
        </div></div>
      </section>"""
    + links_block("Relaterat", [
        ("nybyggnad-villa.html","Bygga villa","Nyckelfärdigt permanenthus."),
        ("attefallshus.html","Attefallshus","Mindre komplementbyggnad."),
        ("byggfirma.html","Total entreprenad","En kontakt för hela bygget.")]),
  faq=[
    ("Bygger ni nyckelfärdiga fritidshus?","Ja, vi bygger nyckelfärdigt – från ritning och bygglov till inflyttningsklart – och även platsbyggt efter dina önskemål."),
    ("Behöver jag bygglov för fritidshus?","Ja, ett fritidshus kräver normalt bygglov. Mindre komplementbyggnader (tidigare attefallshus/friggebod) kan byggas utan bygglov. Vi hjälper dig bedöma."),
    ("Får jag ROT för att bygga fritidshus?","Nej, nybyggnation ger inte ROT. Renovering av ett befintligt fritidshus kan däremot ge ROT-avdrag.")])

# ---- Tak-artiklar (near-miss från Keyword Planner) ----
article("mala-plattak.html",
  "Måla om plåttaket eller byta? Så avgör du | Geal Entreprenad AB",
  "Måla om plåttaket eller byta det? Tecken på att målning räcker, när rosten kräver nytt plåttak och hur förbehandlingen avgör livslängden.",
  "Måla om plåttaket eller byta?",
  "Att måla om plåttaket ger nytt skydd och fräschare uttryck till lägre kostnad än ett byte. Här är när det lönar sig och hur det går till.",
  [("p","Ett plåttak som börjat tappa färg eller fått ytrost kan ofta målas om i stället för att bytas – förutsatt att grundkonstruktionen är hel. Rätt utfört förlänger målningen takets liv med många år."),
   ("h2","När lönar det sig att måla plåttaket?"),
   ("ul",["Ytan är matt, flagnad eller har begynnande rost.","Konstruktionen och infästningarna är hela.",
          "Inga större genomrostningar eller läckage.","Du vill fräscha upp utan ett fullt takbyte."]),
   ("h2","När är det bättre att byta plåttaket?"),
   ("ul",["Rosten har gått igenom plåten och det finns hål eller läckage.",
          "Falsar och skarvar har släppt på flera ställen.",
          "Underlaget under plåten är fuktskadat eller mjukt.",
          "Taket har redan målats om flera gånger och färgen släpper igen."]),
   ("p",f"Då ger ett {a('plattak.html','nytt plåttak')} mer för pengarna än en ommålning. Är du osäker gör vi en {a('takbesiktning.html','takbesiktning')} och ger besked om vilket som gäller ditt tak."),
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

# ---- Bygg-artiklar (near-miss) ----
article("attefallshus-regler.html",
  "Attefallshus – nya regler 2026: mått och avstånd | Geal Entreprenad AB",
  "Sedan 1 december 2025 heter attefallshus komplementbostadshus: 30 m² och 4,0 m inom detaljplan, 50 m² och 4,5 m utanför, 45/65 m² per tomt.",
  "Attefallshus – nya regler 2026",
  "Den 1 december 2025 ersattes attefallsreglerna av regler om komplementbostadshus och komplementbyggnad. Här är måtten, avstånden och vad som fortfarande kräver anmälan – med paragraferna.",
  [("p","Plan- och bygglagen fick ett nytt 9 kapitel den 1 december 2025. De lovfria åtgärderna ”attefallshus” och ”friggebod” togs bort och ersattes av komplementbostadshus och komplementbyggnad. Orden attefallshus, friggebod och attefallstillbyggnad lever kvar som vardagliga namn, men de finns inte längre i lagen. För dig som villaägare innebär ändringen större yta utanför detaljplan, en gemensam pott per tomt och ingen anmälan för själva huset."),
   ("h2","De nya begreppen"),
   ("ul",["<strong>Komplementbostadshus</strong> (vardagligt: attefallshus) – en fristående byggnad som kompletterar ett en- eller tvåbostadshus och är inredd med en självständig bostad.",
          "<strong>Komplementbyggnad</strong> (vardagligt: friggebod) – en fristående byggnad som kompletterar en byggnad och inte är inredd med en självständig bostad, till exempel förråd, garage eller växthus.",
          "Definitionerna står i PBL 1 kap. 4 §."]),
   ("h2","Mått och krav i korthet"),
   ("ul",["<strong>Inom detaljplan:</strong> max 30,0 m² byggnadsarea och 4,0 m taknockshöjd (PBL 9 kap. 4 §).","<strong>Utanför detaljplan:</strong> max 50,0 m² och 4,5 m taknockshöjd (9 kap. 5 §).",
          "Alla lovfria komplementbyggnader och komplementbostadshus på tomten får tillsammans vara högst <strong>45,0 m²</strong> (65,0 m² utanför detaljplan). Friggebodar och attefallshus som byggts utan lov enligt äldre regler räknas in.",
          "Byggnadsarean ska vara mindre än byggnadsarean för huset den kompletterar, och byggnaden ska stå inom tomten.","Ett komplementbostadshus får bara byggas vid en- och tvåbostadshus; en komplementbyggnad vid alla sorters byggnader.",
          "Närmare än <strong>4,5 m från gränsen</strong> krävs bygglov, om inte de berörda grannarna skriftligen medgett åtgärden (9 kap. 34–35 §§). Medgivandet måste numera alltid vara skriftligt."]),
   ("h2","Behövs anmälan och startbesked?"),
   ("p","Inte för själva huset. Men installation eller väsentlig ändring av vatten och avlopp, ventilation, eldstad eller rökkanal kräver fortfarande anmälan och startbesked (<a class=\"text-link\" href=\"https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-byggforordning-2011338_sfs-2011-338/\" rel=\"noopener\">PBF 6 kap. 1 §</a>) innan de görs – och ett hus att bo i behöver i praktiken nästan alltid sådana installationer."),
   ("p","Att göra om en lovfri komplementbyggnad till komplementbostadshus kräver inget bygglov, om den håller måtten (9 kap. 16 §). Står den närmare gränsen än 4,5 meter krävs lov för ändringen, om inte grannarna skriftligen har medgett den."),
   ("h2","Tillbyggnad utan bygglov"),
   ("p",f"Attefallstillbyggnaden på 15 m² finns inte längre. I stället får du bygga till ett hus utan bygglov med högst 30,0 m² bruttoarea eller öppenarea, så länge tillbyggnaden inte går över husets taknock. Gränsen är sammanlagd: tidigare lovfria tillbyggnader på samma byggnad räknas in (9 kap. 10 §), och 4,5-metersregeln mot gränsen gäller även här. Läs mer om {a('tillbyggnad.html','tillbyggnad av villa')}."),
   ("h2","Attefallshus eller friggebod?"),
   ("p",f"Måtten är nu desamma. En {a('friggebod.html','friggebod')} – komplementbyggnad – är inte inredd med en självständig bostad. Ett attefallshus – komplementbostadshus – är inrett som bostad. Se vår tjänst {a('attefallshus.html','attefallshus')}."),
   ("h2","När krävs bygglov ändå?"),
   ("p","Lovfritt är inte regelfritt: tekniska krav, varsamhetskrav och förbudet mot förvanskning gäller fortfarande. Bygglov krävs för byggnader och områden som är särskilt värdefulla eller skyddade i detaljplan (9 kap. 37 §), närmare än 30 meter från ett järnvägsspårs mitt (9 kap. 34 §) och för komplementbostadshus vid flygplatser och övnings- eller skjutfält som är riksintresse för totalförsvaret (9 kap. 36 §)."),
   ("tips","Ligger tomten inom strandskydd eller kulturmiljö kan reglerna vara strängare – hör med kommunen först."),
   ("h2","Källor"),
   ("ul",[f'<a class="text-link" href="{u}" rel="noopener">{t}</a>' for t, u in KOMPL_SRC]),
   ("cta",("Vill du bygga attefallshus?","Vi bygger nyckelfärdigt och hjälper dig med reglerna. Gratis platsbesök och kostnadsförslag."))],
  [("attefallshus.html","Attefallshus","Vi bygger nyckelfärdigt."),
   ("friggebod.html","Friggebod","Nu komplementbyggnad."),
   ("tillbyggnad.html","Tillbyggnad","Bygg ihop med huset.")],
  faq=[("Krävs bygglov eller anmälan för attefallshus 2026?","Nej, inte för själva huset om måtten hålls. Anmälan krävs för vatten och avlopp, ventilation, eldstad och rökkanal."),
       ("Hur nära tomtgränsen får attefallshuset stå?","Närmare än 4,5 meter krävs bygglov, om inte grannarna skriftligen medgett placeringen."),
       ("Hur stort får ett attefallshus vara utanför detaljplan?","Upp till 50 m² byggnadsarea och 4,5 meter taknockshöjd, och högst 65 m² lovfria komplementbyggnader på tomten sammanlagt."),
       ("Finns attefallstillbyggnaden kvar?","Nej. Sedan 1 december 2025 gäller en gemensam gräns på 30 m² för lovfria tillbyggnader på ett hus, och tidigare lovfria tillbyggnader räknas in.")],
  badge="Regler", read="5 min")

article("vad-kostar-bygga-hus.html",
  "Vad kostar det att bygga hus? Prisguide 2026 | Geal Entreprenad AB",
  "Vad kostar det att bygga hus eller ett nyckelfärdigt hus? Vi går igenom vad som driver priset och hur du får ett tillförlitligt kostnadsförslag.",
  "Vad kostar det att bygga hus?",
  "Priset för att bygga hus varierar kraftigt med tomt, storlek och standard. Här är kostnadsdrivarna och hur du får en trygg kalkyl.",
  [("p","Att bygga hus är ett av livets större projekt, och priset beror på många faktorer. Färdiga schablonsiffror blir ofta missvisande eftersom tomt, grundläggning och val av standard påverkar mycket."),
   ("h2","Vad påverkar priset?"),
   ("ul",["<strong>Tomt och grundläggning</strong> – markförhållanden, sprängning, dragningar.",
          "<strong>Storlek och planlösning</strong> – kvadratmeter och komplexitet.",
          "<strong>Nyckelfärdigt vs platsbyggt</strong> – grad av färdigställande.",
          "<strong>Standard och materialval</strong> – kök, bad, ytskikt.",
          "<strong>Anslutningar</strong> – VA, el, fjärrvärme."]),
   ("h2","Så får du ett tillförlitligt pris"),
   ("p",f"Eftersom förutsättningarna skiljer sig ger vi alltid pris efter en genomgång av tomt och önskemål – gratis platsbesök och kostnadsförslag. Se våra tjänster {a('nybyggnad-villa.html','bygga villa (nyckelfärdigt)')} och {a('fritidshus.html','bygga fritidshus')}."),
   ("p","Ett mindre projekt kan bli mer ekonomiskt: ett <a class=\"text-link\" href=\"attefallshus.html\">attefallshus</a> (upp till 30 m²) eller en <a class=\"text-link\" href=\"friggebod.html\">friggebod</a> – båda upp till 30 m² utan bygglov inom detaljplan sedan 1 december 2025."),
   ("tips","Jämför alltid offerter på samma omfattning – vad som ingår (grund, anslutningar, mark) styr slutpriset mer än kvadratmeterpriset."),
   ("cta",("Vill du veta vad ditt husbygge kostar?","Boka en genomgång så får du ett tydligt kostnadsförslag."))],
  [("nybyggnad-villa.html","Bygga villa","Nyckelfärdigt hus från grunden."),
   ("fritidshus.html","Bygga fritidshus","Nyckelfärdigt fritidshus."),
   ("byggfirma.html","Total entreprenad","En entreprenör för hela bygget.")],
  faq=[("Är nyckelfärdigt dyrare än att bygga själv?","Nyckelfärdigt kostar mer i entreprenad men sparar tid, risk och samordning. Att bygga mer själv sänker arbetskostnaden men kräver egen insats och kunskap."),
       ("Får jag ROT när jag bygger nytt?","Nej, ROT gäller inte nybyggnation, bara renovering av befintlig bostad.")],
  badge="Kostnad", read="5 min")

# ====================== KALKYLATOR (lead-magnet) =======================
_kalkyl_tool = """      <section class="section seo-section">
        <div class="container">
          <div class="calc-wrap">
            <form id="kalkyl-form" class="calc-form" novalidate>
              <div class="field">
                <label for="area">Takarea (m²)</label>
                <input id="area" name="area" type="number" min="10" max="1000" step="1"
                  placeholder="t.ex. 130" required />
              </div>
              <div class="field">
                <label for="material">Takmaterial</label>
                <select id="material" name="material" required>
                  <option value="betong">Betongpannor</option>
                  <option value="tegel">Tegelpannor</option>
                  <option value="plat">Plåt (band-/profilplåt)</option>
                </select>
              </div>
              <div class="field">
                <label for="lutning">Taklutning / komplexitet</label>
                <select id="lutning" name="lutning" required>
                  <option value="lag">Låg lutning, enkelt tak</option>
                  <option value="normal" selected>Normalt sadeltak</option>
                  <option value="brant">Brant eller komplext tak</option>
                </select>
              </div>
              <button class="btn btn-primary" type="submit">Beräkna uppskattning</button>
            </form>

            <aside id="kalkyl-result" class="calc-result" hidden aria-live="polite">
              <p class="calc-result__label">Ungefärligt spann (före ROT)</p>
              <p class="calc-result__figure"><span id="kalkyl-low">–</span>–<span id="kalkyl-high">–</span> kr</p>
              <div class="calc-result__rot">
                <p class="calc-result__label">Uppskattat efter ROT-avdrag</p>
                <p class="calc-result__figure"><span id="kalkyl-rot-low">–</span>–<span id="kalkyl-rot-high">–</span> kr</p>
              </div>
              <a id="kalkyl-cta" class="btn btn-primary" href="kontakt.html?tjanst=Takbyte#form">Få en exakt offert</a>
              <p class="calc-disclaimer">Detta är en grov, icke-bindande uppskattning baserad på branschtypiska
                spann – inte en offert. Verkligt pris beror på takets skick, tillgänglighet, plåtdetaljer och
                underlag. Vi lämnar alltid fast pris efter gratis platsbesök. ROT-avdraget är beräknat på
                uppskattad arbetskostnad (30 % 2026, max 50 000 kr/person/år, 1 ägare).</p>
            </aside>
          </div>
        </div>
      </section>"""

page(file="kalkylator-takbyte.html",
  title="Takbyte-kalkylator – uppskatta priset direkt | Geal Entreprenad AB",
  description="Räkna ut ett ungefärligt pris för takbyte på villa: ange area, material och taklutning och få ett prisspann före och efter ROT. Ingen offert.",
  h1="Takbyte-kalkylator – uppskatta priset",
  crumbs=[("Hem","/"),("Tjänster","tjanster.html"),("Takbyte-kalkylator","kalkylator-takbyte.html")],
  cta=("Vill du ha ett exakt pris?","En kalkylator ger ett spann – vi ger ett fast pris efter kostnadsfritt platsbesök. Begär offert."),
  body=hero("Takbyte-kalkylator – uppskatta priset",
    "Få en snabb känsla för vad ett takbyte kan kosta. Ange takets area, material och lutning så visar kalkylatorn ett ungefärligt spann – både före och efter ROT-avdrag. Det är en grov uppskattning, inte en bindande offert.",
    [("Hem","/"),("Tjänster","tjanster.html"),("Takbyte-kalkylator","kalkylator-takbyte.html")])
    + _kalkyl_tool
    + sec("Så fungerar uppskattningen", [
        "Kalkylatorn utgår från branschtypiska kvadratmeterpriser för olika takmaterial och justerar för takets lutning och komplexitet. Priset inkluderar normalt material och arbete, men varje tak är unikt – underlagets skick, plåtdetaljer, ställningsbehov och tillgänglighet påverkar slutpriset mer än kvadratmeterpriset.",
        f"Vill du förstå vad som styr kostnaden i detalj läser du {a('vad-kostar-takbyte.html','vad kostar ett takbyte')}. När du är redo hjälper vi dig med ett fast pris efter ett kostnadsfritt {a('takbesiktning.html','platsbesök och besiktning')}."])
    + links_block("Nästa steg", [
        ("takbyte.html","Takbyte","Så går ett komplett takbyte till."),
        ("vad-kostar-takbyte.html","Vad kostar ett takbyte?","Prisguide och vad som påverkar kostnaden."),
        ("rot-avdrag-takarbete.html","ROT-avdrag","Så mycket kan du dra av 2026."),
        ("https://takbytepris.nu/","Takbyte pris","Detaljerad kalkyl med materiallista och ROT.")]))

# ====================== TACK (form success) ============================
page(file="tack.html", no_cta=True, noindex=True, nolist=True,
  title="Tack för din förfrågan | Geal Entreprenad AB",
  description="Tack! Vi har tagit emot din förfrågan och återkommer så snart vi kan.",
  h1="Tack för din förfrågan!",
  crumbs=[("Hem","/"),("Tack","tack.html")],
  body=hero("Tack för din förfrågan!",
    "Vi har tagit emot ditt meddelande och återkommer så snart vi kan, oftast inom 24 timmar. Behöver du nå oss direkt är du välkommen att ringa.",
    [("Hem","/"),("Tack","tack.html")])
    + f"""      <section class="section seo-section">
        <div class="container">
          <div class="hero-actions">
            <a class="btn btn-primary" href="tel:{PHONE_T}">Ring {PHONE_D}</a>
            <a class="btn btn-secondary" href="/">Till startsidan</a>
          </div>
        </div>
      </section>""")

# ====================== 404 =============================================
page(file="404.html", no_cta=True, noindex=True, nolist=True,
  title="Sidan hittades inte (404) | Geal Entreprenad AB",
  description="Sidan kunde inte hittas. Gå till startsidan eller våra tjänster för takbyte, takrenovering och takbesiktning i Stockholm.",
  h1="Sidan hittades inte",
  crumbs=[("Hem","/"),("404","404.html")],
  body=hero("Sidan hittades inte (404)",
    "Sidan du letade efter finns inte längre eller har flyttat. Använd länkarna nedan så hittar du rätt.",
    [("Hem","/"),("404","404.html")])
    + links_block("Populära sidor", [
        ("/","Till startsidan","Takläggare i Stockholm."),
        ("tjanster.html","Våra tjänster","Takbyte, renovering, besiktning m.m."),
        ("omraden.html","Områden","Se var vi arbetar."),
        ("artiklar.html","Artiklar","Guider om tak och takarbete."),
        ("faq.html","Vanliga frågor","Svar på det vanligaste."),
        ("kontakt.html","Kontakt","Begär offert eller ställ en fråga.")], muted=False))

# ====================== TEMATISK FOKUS (2026-10-15) =====================
# Rena nybygge-/infosidor utan takkoppling: aldrig indexerade av Google (GSC URL-
# inspektion 15.10: "okänd"/"Discovered"), drar crawl och späder ut taktemat.
# noindex,follow + ur sitemap. Sidorna finns kvar för besökare och Ads; kommersiella
# byggsidor (bygg, byggfirma, villarenovering, tillbyggnad, attefallshus,
# nybyggnad-villa) ligger kvar i index.
OFFTOPIC_NOINDEX = {"friggebod.html", "fritidshus.html", "vad-kostar-bygga-hus.html",
                    "attefallshus-regler.html"}
for _p in PAGES:
    if _p["file"] in OFFTOPIC_NOINDEX:
        _p["noindex"] = True
        _p["nolist"] = True

# ====================== SÖK (klientbaserad) ============================
# Metadata för de handunderhållna sidorna (för sökindex).
STATIC_META = {
  "index.html": ("Takläggare i Bromma & Stockholm – takbyte och takrenovering", "Takläggare och takfirma i Bromma. Takbyte, takrenovering, plåttak och totalentreprenad på villa i hela Stockholm. Gratis besök och kostnadsförslag."),
  "tjanster.html": ("Våra tjänster", "Takbyte, takrenovering, takbesiktning, plåttak, takmålning, taktvätt samt badrum, kök, målning, snickeri, golv, fasad och fönster."),
  "om-oss.html": ("Om oss", "Geal Entreprenad AB – takläggare och byggpartner i Stockholm med F-skatt, ansvarsförsäkring och ID06."),
  "kontakt.html": ("Kontakt", "Begär kostnadsfri offert eller ställ en fråga till oss."),
  "artiklar.html": ("Artiklar & guider", "Guider om takbyte, takrenovering, ROT-avdrag, material och underhåll."),
}
# Bygg sökindex av alla indexerbara sidor (PAGES är komplett här).
_search_index = [{"t": t, "u": "/" if u == "index.html" else u, "d": d} for u, (t, d) in STATIC_META.items()]
_search_index += [{"t": p["h1"], "u": p["file"], "d": p["description"]}
                  for p in PAGES if not p.get("noindex") and not p.get("nolist")]
_search_json = json.dumps(_search_index, ensure_ascii=False)

_sok_tool = f"""      <section class="section seo-section">
        <div class="container">
          <form id="sok-form" class="calc-form" role="search" novalidate>
            <div class="field">
              <label for="sok-input">Sök på webbplatsen</label>
              <input id="sok-input" name="q" type="search" autocomplete="off"
                placeholder="t.ex. takbyte, ROT, plåttak, Sundbyberg" />
            </div>
            <button class="btn btn-primary" type="submit">Sök</button>
          </form>
          <div id="sok-results" class="service-grid" aria-live="polite"></div>
        </div>
      </section>
      <script>window.SEARCH_INDEX = {_search_json};</script>"""

page(file="sok.html", noindex=True, nolist=True, no_cta=True,
  title="Sök på villatakservice.se | Geal Entreprenad AB",
  description="Sök bland våra tjänster, orter och guider om tak, takbyte och takrenovering.",
  h1="Sök på webbplatsen",
  crumbs=[("Hem","/"),("Sök","sok.html")],
  body=hero("Sök på webbplatsen",
    "Sök bland våra tjänster, områden och guider om tak, takbyte, takrenovering och ROT.",
    [("Hem","/"),("Sök","sok.html")])
    + _sok_tool)

# ====================== WRITE FILES + SITEMAP =============================
# Existing hand-maintained pages (regenereras ej men ska med i sitemap)
STATIC_PAGES = ["index.html","tjanster.html","om-oss.html","kontakt.html",
                "artiklar.html"]

import re as _re
# Öar och innerstadsdelar tar "på": "på Lidingö", inte "i Lidingö" (men "i Lidingö stad/kommun").
_PA = _re.compile(r'\b([Ii]) (Södermalm|Kungsholmen|Östermalm|Lidingö|Värmdö|Ekerö)\b(?! (?:kommun|stad|stads|centrum))')
def fix_prep(html):
    # Gäller även title/alt/meta; URL:er innehåller inga "i <Ort>" med mellanslag.
    return _PA.sub(lambda m: ("På" if m.group(1) == "I" else "på") + " " + m.group(2), html)

def main():
    written = []
    for p in PAGES:
        html = fix_prep(render(p))
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
    import subprocess
    def lastmod(u):
        # Senaste commit som ändrade filen (ärlig lastmod); ändrad men ej committad = idag.
        fp = os.path.join(ROOT, u)
        try:
            dirty = subprocess.run(["git","status","--porcelain","--",u], cwd=ROOT,
                                   capture_output=True, text=True).stdout.strip()
            d = subprocess.run(["git","log","-1","--format=%cs","--",u], cwd=ROOT,
                               capture_output=True, text=True).stdout.strip()
        except Exception:
            return BUILD_DATE
        return BUILD_DATE if (dirty or not d) else d
    items = "\n".join(
        f"  <url>\n    <loc>{loc(u)}</loc>\n    <lastmod>{lastmod(u)}</lastmod>\n"
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
    # Handunderhållna sidor: samma versionerade asset-URL:er.
    import re
    for fn in STATIC_PAGES + ["artikel.html"]:
        fp = os.path.join(ROOT, fn)
        if not os.path.exists(fp):
            continue
        with open(fp, encoding="utf-8") as fh:
            src = fh.read()
        out = re.sub(r'assets/css/style\.css(\?v=[0-9a-f]+)?', CSS_URL, src)
        out = re.sub(r'assets/js/main\.js(\?v=[0-9a-f]+)?', JS_URL, out)
        if out != src:
            with open(fp, "w", encoding="utf-8") as fh:
                fh.write(out)
    print(f"Genererade {len(written)} sidor.")
    print(f"Sitemap: {len(ordered)} URL:er. robots.txt skriven.")
    for w in written: print("  +", w)

if __name__ == "__main__":
    main()
