#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-overrides (13.11.2026): title / description / hero-lead per sida, styrt av GSC.

Varför ett eget steg: generatorerna (generate.py + tj_v*.py) skriver om alla sidor, och
handändringar i HTML försvinner vid nästa körning (SEO-rundan 07.11 för golvslipning
Lidingö/Danderyd/Huddinge skrevs över av DS-utrullningen 09.11). Det här skriptet körs SIST
i generate.py och lägger tillbaka texterna. Idempotent.

Regler:
  - bara fakta som redan står på sajten (gratis besök och kostnadsförslag, ROT-avdrag på
    fakturan, takbyte från 1 400 kr/m² före ROT) – inga nya priser, inga nya löften;
  - ROT nämns inte där sidan själv säger att avdraget inte gäller (fasad i bostadsrättshus);
  - lead = EN mening (DS taklia: hero-lead 1 mening);
  - title ≤ 60 tecken, description ≤ 160.

Användning: python3 tools/seo_overrides.py          (skriver)
            python3 tools/seo_overrides.py --check  (exit 1 om någon sida avviker)
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# fil: (title, description, lead eller None = behåll sidans lead)
# Kommentar per rad = GSC-fråga 15.10–11.11.2026 (visningar / position).
OVERRIDES = {
    # byta tak sollentuna 75/8.9, takrenovering sollentuna 71/12.5, takbyte sollentuna 49/8.2
    "takbyte-sollentuna.html": (
        "Takbyte Sollentuna – byta tak från 1 400 kr/m² före ROT",
        "Byta tak i Sollentuna på villa eller radhus: från 1 400 kr/m² inkl. material, före ROT-avdrag. Gratis besök och kostnadsförslag av Geal Entreprenad AB.",
        "Geal Entreprenad AB byter tak på villor och radhus i Sollentuna, från 1 400 kr/m² inklusive material före ROT-avdrag, med gratis besök och kostnadsförslag.",
    ),
    # takläggare sollentuna 158/52 – titeln lämnar takbyte/takrenovering åt takbyte-sollentuna
    "taklaggare-sollentuna.html": (
        "Takläggare Sollentuna – takfirma för villa och radhus",
        None,
        None,
    ),
    # golvslipning danderyd 98/10.7, golvslipning djursholm 12/10.1, parkettslipning djursholm 11/14.6
    "golvslipning-danderyd.html": (
        "Golvslipning Danderyd och Djursholm – parkett, gratis offert",
        "Golvslipning i Danderyd och Djursholm: vi slipar stav- och fiskbensparkett och lackar eller oljar. Gratis platsbesök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB slipar stav- och fiskbensparkett i Danderyd och Djursholm och avslutar med lack eller olja, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # golvslipning lidingö 78/9.5, slipa golv lidingö 13/5.7
    "golvslipning-lidingo.html": (
        "Golvslipning Lidingö – slipa golv, lack eller olja, ROT",
        "Golvslipning på Lidingö: vi slipar parkett och trägolv i villa och radhus och lackar eller oljar. Gratis platsbesök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB slipar parkett och trägolv på Lidingö och ytbehandlar med lack, olja eller lut, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # golvslipning huddinge 107/20.6
    "golvslipning-huddinge.html": (
        "Golvslipning Huddinge – slipa golv, lack eller olja, ROT",
        "Golvslipning i Huddinge: vi slipar parkett och trägolv och lackar eller oljar – även byte från lack till olja. Gratis platsbesök, ROT-avdrag på fakturan.",
        "Geal Entreprenad AB slipar parkett och trägolv i Huddinge och lackar eller oljar efteråt, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # slipa golv solna 46/15.4
    "golvslipning-solna.html": (
        "Golvslipning Solna – slipa golv i lägenhet, gratis offert",
        "Golvslipning i Solna: vi tar fram och slipar trägolvet under gamla mattor och ytbehandlar med lack eller olja. Gratis platsbesök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB slipar trägolv i Solna, också golv som har legat under linoleum eller plastmatta, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # slipa golv bromma 57/15.2 (hamnar i dag på golvlaggare-bromma)
    "golvslipning-bromma.html": (
        "Golvslipning Bromma – slipa golv i villa, gratis offert",
        "Golvslipning i Bromma: vi slipar furugolv och parkett och behandlar med lut och såpa, lack eller olja. Gratis platsbesök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB i Bromma slipar furugolv och parkett och behandlar ytan med lut och såpa, lack eller olja, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # slipa golv täby 22/16.4
    "golvslipning-taby.html": (
        "Golvslipning Täby – slipa golv i villa och radhus, ROT",
        "Golvslipning i Täby: vi slipar trägolv och parkett, lagar in brädor där en vägg har stått och lackar eller oljar. Gratis platsbesök, ROT-avdrag på fakturan.",
        "Geal Entreprenad AB slipar trägolv och parkett i villor och radhus i Täby och lagar in nya brädor där en vägg har stått, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # golvslipning vallentuna 15/6.7
    "golvslipning-vallentuna.html": (
        "Golvslipning Vallentuna – slipa gamla trägolv, gratis offert",
        "Golvslipning i Vallentuna: vi slipar gamla golvplank och parkett i villor, gårdar och fritidshus och lackar eller oljar. Gratis platsbesök och kostnadsförslag.",
        None,
    ),
    # golvläggare solna 66/14.7, golvläggning solna 20/10.7, golvläggning i solna 15/10.3
    "golvlaggare-solna.html": (
        "Golvläggare Solna – golvläggning i lägenhet, gratis offert",
        "Golvläggare i Solna: nytt golv av parkett, laminat eller vinyl och slipning av trägolv i bostadsrätt. Gratis platsbesök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB lägger nya golv och slipar trägolv i Solna, oftast i bostadsrätter, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # golvläggare bromma 25/13.8, ytbehandling golv bromma 12/13.9
    "golvlaggare-bromma.html": (
        "Golvläggare Bromma – golvläggning i villa och lägenhet",
        "Golvläggare i Bromma: vi lägger nytt golv och tar hand om gamla trägolv i villor och smalhusens lägenheter. Gratis platsbesök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB i Bromma lägger nya golv och tar hand om gamla trägolv i villor och smalhusens lägenheter, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # fönsterbyte vallentuna 83/11.3, byta fönster vallentuna 6/15.5
    "fonsterbyte-vallentuna.html": (
        "Fönsterbyte Vallentuna – byta fönster i villa, gratis offert",
        "Fönsterbyte i Vallentuna: vi mäter på plats, monterar nya fönster och går igenom glas som dämpar flygbuller. Gratis besök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB byter fönster i villor i Vallentuna, med glas valt efter flygbullret från Arlanda, gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # fönsterbyte sigtuna 63/17.8 (hamnar i dag på fonsterrenovering-sigtuna)
    "fonsterbyte-sigtuna.html": (
        "Fönsterbyte Sigtuna – byta fönster i villa, gratis offert",
        "Fönsterbyte i Sigtuna: vi mäter på plats, monterar nya fönster och går igenom ljudisoleringen nära Arlanda. Gratis besök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB byter fönster i villor i Sigtuna kommun, där ljudisoleringen mot Arlanda ofta avgör glasvalet, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # fönsterrenovering sigtuna 5/8.6
    "fonsterrenovering-sigtuna.html": (
        "Fönsterrenovering Sigtuna – renovera gamla träfönster",
        "Fönsterrenovering i Sigtuna: vi skrapar, kittar och målar gamla träfönster med linoljefärg i stället för att byta dem. Gratis besök, ROT-avdrag på fakturan.",
        None,
    ),
    # fönsterbyte österåker 26/17.8 + 18/17.7
    "fonsterbyte-osteraker.html": (
        "Fönsterbyte Österåker – byta fönster i villa, gratis offert",
        "Fönsterbyte i Österåker: vi mäter på plats och monterar nya fönster som tål vind och slagregn och passar husets utseende. Gratis besök, ROT-avdrag på fakturan.",
        "Geal Entreprenad AB byter fönster i villor i Österåker, med hänsyn till husets utseende och läget vid kusten, gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    "fonsterrenovering-osteraker.html": (
        "Fönsterrenovering Österåker – renovera gamla träfönster",
        "Fönsterrenovering i Österåker: vi renoverar sommarvillornas bågar och glasverandor – skrapning, kitt, linoljefärg och tätning. Gratis besök, ROT på fakturan.",
        None,
    ),
    # fönsterbyte botkyrka 14/8.5 (hamnar i dag på fonsterrenovering-botkyrka)
    "fonsterbyte-botkyrka.html": (
        "Fönsterbyte Botkyrka – byta fönster i villa, gratis offert",
        "Fönsterbyte i Botkyrka: vi mäter på plats och monterar nya fönster som passar villans epok, från småspröjs till perspektivfönster. Gratis besök, ROT-avdrag.",
        "Geal Entreprenad AB byter fönster i villor i Botkyrka och väljer fönstertyp efter husets epok, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # fönsterrenovering botkyrka 15/11.8
    "fonsterrenovering-botkyrka.html": (
        "Fönsterrenovering Botkyrka – renovera träfönster, ROT",
        "Fönsterrenovering i Botkyrka: vi skrapar, kittar, målar och tätar ursprungliga träfönster, till exempel i radhusen i Tuna. Gratis besök, ROT-avdrag på fakturan.",
        None,
    ),
    # fönsterrenovering täby 95/13.4
    "fonsterrenovering-taby.html": (
        "Fönsterrenovering Täby – kitt, glas och linoljefärg, ROT",
        "Fönsterrenovering i Täby: vi skrapar, kittar om, byter trasigt glas och målar med linoljefärg – även småspröjsade bågar. Gratis besök, ROT-avdrag på fakturan.",
        "Geal Entreprenad AB renoverar träfönster i Täby med skrapning, kittning, nytt glas och linoljefärg, gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # fönsterrenovering solna 60/17.0
    "fonsterrenovering-solna.html": (
        "Fönsterrenovering Solna – kitt, målning och tätning",
        "Fönsterrenovering i Solna: vi kittar om, målar och tätar träfönster i hus från 1950-talet i Råsunda, Skytteholm och Huvudsta. Gratis besök och kostnadsförslag.",
        "Geal Entreprenad AB renoverar träfönster i Solna, bland annat i 1950-talshusen i Råsunda, Skytteholm och Huvudsta, med gratis besök och kostnadsförslag.",
    ),
    # fönsterrenovering stocksund 16/7.1
    "fonsterrenovering-danderyd.html": (
        "Fönsterrenovering Danderyd – Djursholm och Stocksund, ROT",
        "Fönsterrenovering i Danderyd, Djursholm och Stocksund: vi kittar om med linoljekitt, målar och justerar beslag på villans fönster. Gratis besök, ROT-avdrag.",
        None,
    ),
    # målare östermalm 70/18.4
    "malare-ostermalm.html": (
        "Målare Östermalm – tak, väggar och snickerier, gratis offert",
        "Målare på Östermalm: vi målar tak, väggar och snickerier i lägenheter och våningar, även gamla limfärgstak. Gratis platsbesök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB målar tak, väggar och snickerier i lägenheter på Östermalm, även gamla limfärgstak, med gratis platsbesök och ROT-avdrag direkt på fakturan.",
    ),
    # totalentreprenad bromma 143/17.7 (tre sidor delar frågan – den här äger den)
    "byggforetag-bromma.html": (
        "Byggföretag Bromma – totalentreprenad för villa",
        "Byggföretag i Bromma: Geal Entreprenad AB bygger om villor som totalentreprenad – vind, bärande väggar och ny bostad i huset. Gratis besök och kostnadsförslag.",
        "Geal Entreprenad AB är ett byggföretag i Bromma som bygger om villor som totalentreprenad, från vindsinredning till flyttade bärande väggar, med gratis besök och kostnadsförslag.",
    ),
    # totalentreprenad solna 34/17.3
    "byggforetag-solna.html": (
        "Byggföretag Solna – totalentreprenad, gratis offert",
        "Byggföretag i Solna: Geal Entreprenad AB bygger om och bygger till som totalentreprenad och hjälper dig med bygglov och anmälan. Gratis besök och offert.",
        None,
    ),
    # byggfirma ekerö 18/11.2, byggföretag ekerö 11/13
    "byggforetag-ekero.html": (
        "Byggföretag Ekerö – byggfirma för nytt hus, gratis offert",
        "Byggfirma på Ekerö: Geal Entreprenad AB bygger nytt hus på Mälaröarna, med koll på strandskydd och vattenskyddsområdet. Gratis besök och offert.",
        None,
    ),
    # byggfirma hägersten 14/17.9, byggföretag hägersten 10/16.6
    "byggforetag-hagersten.html": (
        "Byggföretag Hägersten – byggfirma för tillbyggnad",
        "Byggfirma i Hägersten: tillbyggnad på Mälarhöjdens kuperade villatomter, med terräng, marklov och ritningar i ordning. Gratis besök och kostnadsförslag.",
        None,
    ),
    # tillbyggnation vallentuna 16/15.6, tillbyggnader vallentuna 11/14
    "tillbyggnad-vallentuna.html": (
        "Tillbyggnad Vallentuna – bygga till villan, gratis offert",
        "Tillbyggnad i Vallentuna: vi bygger till villan med grund, stomme, tak och anslutning till huset och hjälper dig med ritningar och lov. Gratis besök och offert.",
        None,
    ),
    # renoveringsarbete haninge 36/15.7, lägenhetsrenovering haninge 12/19.2
    "totalrenovering-haninge.html": (
        "Totalrenovering Haninge – renovera villan, gratis offert",
        "Totalrenovering i Haninge: kök, badrum, golv och ytskikt i villa och kedjehus med en och samma byggpartner. Gratis besök, ROT-avdrag direkt på fakturan.",
        "Geal Entreprenad AB totalrenoverar villor och kedjehus i Haninge, med kök, badrum, golv och ytskikt i ett och samma projekt, gratis besök och ROT-avdrag direkt på fakturan.",
    ),
    # takrenovering danderyd 30/8.0, plåttak djursholm 6/6.3 (leaden svarar redan)
    "takrenovering-danderyd.html": (
        "Takrenovering Danderyd – tegeltak och plåttak, gratis besök",
        "Takrenovering i Danderyd, Djursholm och Stocksund: vi lägger om tegel- och plåttak med nytt underlag. Gratis besök och kostnadsförslag, ROT-avdrag på fakturan.",
        None,
    ),
    # takrenovering sundbyberg 15/18.3, tegel tak sundbyberg 11/11.9
    "takrenovering-sundbyberg.html": (
        "Takrenovering Sundbyberg – tegeltak i Duvbo, gratis besök",
        "Takrenovering i Sundbyberg och Duvbo: vi lägger om tegeltak och går igenom lovplikten för takmaterial. Gratis besök och kostnadsförslag, ROT på fakturan.",
        None,
    ),
    # plåtslagare sundbyberg 27/16.5, plåtarbeten sundbyberg 9/19.4
    "platslagare-sundbyberg.html": (
        "Plåtslagare Sundbyberg – plåttak och plåtarbeten",
        "Plåtslagare i Sundbyberg och Duvbo: falsade plåttak, skorstensbeslag, hängrännor och fönsterbleck. Gratis besök och kostnadsförslag, ROT-avdrag på fakturan.",
        None,
    ),
    # snickare järfälla 32/19.5
    "snickare-jarfalla.html": (
        "Snickare Järfälla – förråd, dörrar och lister, gratis offert",
        "Snickare i Järfälla: förråd och grindar på förgården, ytterdörrar, lister och foder i radhus och villa. Gratis platsbesök och tydlig offert.",
        "Geal Entreprenad AB är snickare i Järfälla och bygger förråd och grindar på radhusens förgårdar och byter ytterdörrar, med gratis platsbesök och tydlig offert.",
    ),
    # fasadrenovering kungsholmen 31/13.2 (hamnar i dag på fasadmalning-kungsholmen); ingen ROT – sidan säger det
    "fasadrenovering-kungsholmen.html": (
        "Fasadrenovering Kungsholmen – puts på funkishus",
        "Fasadrenovering på Kungsholmen: vi lagar och putsar om slätputsade funkisfasader i Fredhäll och Kristineberg. Gratis besök och kostnadsförslag.",
        "Geal Entreprenad AB renoverar putsade fasader på Kungsholmen, bland annat funkishusen i Fredhäll och Kristineberg, med gratis besök och kostnadsförslag.",
    ),
    # fasadmålning kungsholmen 13/9.8
    "fasadmalning-kungsholmen.html": (
        "Fasadmålning Kungsholmen – måla putsfasad, gratis offert",
        "Fasadmålning på Kungsholmen: vi tvättar, lagar och målar putsade fasader mot gata och gård i Kristineberg och Fredhäll och på Stora Essingen. Gratis besök.",
        None,
    ),
    # puts i lidingö 14/15.9, putsfasad lidingö 9/16.6
    "fasadrenovering-lidingo.html": (
        "Fasadrenovering Lidingö – putsfasad och tegel, gratis offert",
        "Fasadrenovering på Lidingö: vi lagar och putsar om putsfasader och renoverar tegel på radhus, bland annat i Hersby. Gratis besök och kostnadsförslag.",
        None,
    ),
}

TITLE_MAX, DESC_MAX = 60, 160


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


def apply(html, title, desc, lead):
    """Returnerar ny HTML. Hittar gamla värden i sidan och byter på alla ställen."""
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    old_title = m.group(1)
    if title and old_title != esc(title):
        html = html.replace(f"<title>{old_title}</title>", f"<title>{esc(title)}</title>", 1)
        html = re.sub(r'(<meta property="og:title" content=")[^"]*(")',
                      lambda g: g.group(1) + esc(title) + g.group(2), html, count=1)
    if desc:
        m = re.search(r'<meta name="description" content="([^"]*)"', html)
        old_desc = m.group(1)
        if old_desc != esc(desc):
            # meta + og + JSON-LD (Service/WebPage "description" har samma text)
            html = html.replace(f'content="{old_desc}"', f'content="{esc(desc)}"')
            html = html.replace(f'"description": "{old_desc}"', f'"description": "{desc}"')
    if lead:
        hero = re.search(r'<section class="page-hero[^"]*">.*?</section>', html, re.S)
        m = re.search(r'(<p class="section-lead">)(.*?)(</p>)', hero.group(0), re.S)
        if m.group(2) != lead:
            new_hero = hero.group(0).replace(m.group(0), m.group(1) + lead + m.group(3), 1)
            html = html.replace(hero.group(0), new_hero, 1)
    return html


def sibling_links():
    """takrenovering-<ort> → takbyte-<ort>: en mening med länk i kostnadsstycket.
    GSC 13.11: takbyte-sidorna (pris från 1 400 kr/m²) rankar bäst i klustret
    (Sollentuna pos 8–12) men saknade länk från ortens takrenoveringssida (33 orter)."""
    import glob
    out = {}
    for fp in sorted(glob.glob(os.path.join(ROOT, "takrenovering-*.html"))):
        ort = os.path.basename(fp)[len("takrenovering-"):]
        target = "takbyte-" + ort
        tp = os.path.join(ROOT, target)
        if not os.path.exists(tp):
            continue
        html = open(fp, encoding="utf-8").read()
        if f'href="{target}"' in html:
            continue
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", open(tp, encoding="utf-8").read(), re.S).group(1).strip()
        anchor = h1[0].lower() + h1[1:]          # «takbyte i Sollentuna»
        paras = [p for p in re.findall(r"<p>.*?</p>", html, re.S)
                 if 'href="vad-kostar-takrenovering.html"' in p]
        if not paras:
            continue
        old = paras[0]
        new = old[:-4] + f' Ska hela taket bytas, läs om <a class="text-link" href="{target}">{anchor}</a>.</p>'
        out[fp] = html.replace(old, new, 1)
    return out


def main():
    check = "--check" in sys.argv
    bad = []
    for fn, (title, desc, lead) in OVERRIDES.items():
        for label, txt, mx in (("title", title, TITLE_MAX), ("description", desc, DESC_MAX)):
            if txt and len(txt) > mx:
                bad.append(f"{fn}: {label} {len(txt)} tecken (max {mx})")
        for txt in (title, desc, lead):
            if txt and (re.search(r"[Ѐ-ӿ]", txt) or '"' in txt or "<" in txt):
                bad.append(f"{fn}: otillåtet tecken i text")
        if lead and len(re.findall(r"[.!?](?:\s|$)", lead.replace("kr/m²", ""))) != 1:
            bad.append(f"{fn}: lead ska vara exakt en mening")
    if bad:
        print("\n".join(bad))
        sys.exit(1)
    changed = []
    for fn, (title, desc, lead) in OVERRIDES.items():
        fp = os.path.join(ROOT, fn)
        src = open(fp, encoding="utf-8").read()
        out = apply(src, title, desc, lead)
        if out != src:
            changed.append(fn)
            if not check:
                with open(fp, "w", encoding="utf-8") as fh:
                    fh.write(out)
    for fp, out in sibling_links().items():
        changed.append(os.path.basename(fp) + " (länk takbyte)")
        if not check:
            with open(fp, "w", encoding="utf-8") as fh:
                fh.write(out)
    if check:
        if changed:
            print("SEO-overrides saknas på:", ", ".join(changed))
            sys.exit(1)
        print(f"SEO-overrides: {len(OVERRIDES)} sidor OK.")
        return
    print(f"SEO-overrides: {len(changed)} ändringar ({len(OVERRIDES)} sidor med egna texter).")


if __name__ == "__main__":
    main()
