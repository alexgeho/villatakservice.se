#!/usr/bin/env python3
"""Pilot 07.11: takbyte.html utan textväggar — block foto+text i sicksack (DS: «Vägg av text» nej,
intro + 3–4 fakta som lista, en H2 per block, bakgrunder växlar)."""
import os, re
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "takbyte.html")

B = [
 ("nar", "När är det dags för ett takbyte?", "takbyte-4", "Slitet betongpannetak med mossa och spruckna pannor",
  "Ett takbyte blir aktuellt när taket nått slutet av sin livslängd eller när reparationer inte längre lönar sig.",
  ["Återkommande läckage trots reparationer", "Spruckna eller frostskadade pannor", "Fuktfläckar på vinden", "Spröd underlagspapp vid takfoten"],
  'Osäker? Börja med en <a class="text-link" href="takbesiktning.html">takbesiktning</a> eller läs <a class="text-link" href="takbyte-eller-takrenovering.html">takbyte eller takrenovering</a>.'),
 ("ingar", "Vad ingår i ett takbyte?", "takbyte-2", "Nytt underlag och läkt under takbyte",
  "Vi byter hela taket – inte bara ytskiktet.",
  ["Rivning och bortforsling av det gamla taket", "Ny underlagspapp och kontroll av läkt", "Nytt ytskikt: tegel, betongpannor eller plåt", "Plåt kring skorsten och genomföringar, slutkontroll med dig"], ""),
 ("tecken", "Tecken på att taket behöver bytas", "takbyte-5", "Vind med fuktfläckar på råsponten",
  "Underlagspappen tar oftast slut först – därför syns problemen på vinden innan de syns från gatan.",
  ["Fuktfläckar eller mögel på råsponten", "Dagsljus genom taket från vinden", "Vittrade eller frostsprängda pannor", "Taket är 40–50 år eller äldre"], ""),
 ("epoker", "Olika epoker, olika tak", "takbyte-6", "1920-talsvilla med brant tegeltak och kupor",
  "Vi väljer material efter husets ålder och karaktär.",
  ["1920–40-tal i Bromma, Danderyd och Sundbyberg: branta tegeltak med kupor", "1960–70-tal i Sollentuna, Spånga, Täby och Järfälla: betongpannor med 50 år gammalt underlag", "Funkishus och radhus med låg lutning: plåt- eller papptak"],
  'Vi arbetar i hela Storstockholm – se <a class="text-link" href="omraden.html">alla områden</a>.'),
 ("passa-pa", "Passa på vid takbytet", "takbyte-7", "Ny hängränna, snörasskydd och takstege på nytt tak",
  "Ställningen står ändå uppe – gör allt som kräver den samtidigt.",
  ["Hängrännor, stuprör, snörasskydd och takstege", "Takfönster och ventilation vid takfoten", "Infästning för solceller – taket håller 40–60 år, solcellerna 25–30", "Tilläggsisolering av vinden med fungerande ventilation"], ""),
 ("tid", "Bästa tiden för takbyte", "takbyte-8", "Villa med ställning och nytt underlag på våren",
  "Takbyten görs i Stockholm från tidig vår till sen höst.",
  ["Huset hålls tätt varje kväll med presenning eller nytt underlag", "Vintertid gör vi främst akuta reparationer", "Vår och sommar bokas snabbt – begär offert redan på vintern"], ""),
 ("material", "Material: tegel, betong eller plåt?", "takmaterial-jamforelse", "Jämförelse av tegel, betongpannor och plåt",
  "Materialet styr livslängd, uttryck och pris.",
  ["Tegel och betongpannor – vanligast på villor i Stockholm", "Plåt – låg vikt och passar låg lutning", "Vi jämför alternativen för just ditt hus"],
  'Läs mer: <a class="text-link" href="tegel-betong-plattak.html">tegel vs betong vs plåt</a> och <a class="text-link" href="takmaterial-livslangd.html">livslängd per takmaterial</a>.'),
 ("pris", "Pris för takbyte och ROT-avdrag", "takbyte-3", "Färdigt nytt tak med plåtdetaljer och hängrännor",
  "Vi lämnar fast pris efter att ha sett taket på plats.",
  ["Takets area och lutning", "Material och behov av ställning", "Underlagets skick", "ROT-avdrag 2026: 30 % av arbetskostnaden, högst 50 000 kr per person och år"],
  'Räkna själv i <a class="text-link" href="kalkylator-takbyte.html">takbyte-kalkylatorn</a> eller läs <a class="text-link" href="vad-kostar-takbyte.html">vad kostar ett takbyte</a>.'),
]


def img(name, alt):
    fp = os.path.join(ROOT, "assets", "images", name + ".webp")
    w, h = Image.open(fp).size
    ss = f' srcset="assets/images/{name}-640.webp 640w, assets/images/{name}.webp {w}w" sizes="(max-width: 900px) 100vw, 560px"' \
        if os.path.exists(fp.replace(".webp", "-640.webp")) else ""
    return f'<img src="assets/images/{name}.webp"{ss} width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async" />'


def block(i, sid, h2, im, alt, intro, items, extra):
    bg = " section-muted" if i % 2 == 0 else ""
    flip = " split-media--flip" if i % 2 else ""
    li = "\n".join(f"              <li>{x}</li>" for x in items)
    ex = f"\n            <p>{extra}</p>" if extra else ""
    return f"""      <section class="section{bg} seo-section media-block" id="{sid}">
        <div class="container split-media{flip}">
          <figure class="split-figure">{img(im, alt)}</figure>
          <div class="section-copy">
            <h2 class="section-title">{h2}</h2>
            <p>{intro}</p>
            <ul class="fact-list">
{li}
            </ul>{ex}
          </div>
        </div>
      </section>"""


s = open(P, encoding="utf-8").read()
if "media-block" not in s:
    a = s.index('      <section class="section gallery-section">')
    b = s.rindex("<section", 0, s.index(">Så går ett takbyte till<", a))
    b = s.rindex("\n", 0, b) + 1
    s = s[:a] + "\n".join(block(i, *x) for i, x in enumerate(B)) + "\n" + s[b:]
    open(P, "w", encoding="utf-8").write(s)
    print("pilot takbyte: ok")
