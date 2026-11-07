#!/usr/bin/env python3
"""Bilder för landningssidor utan bilder (07.11.2026): 3 per sida via flux (gen_images_flux.run).
-1 hero-bild 4:3 (typiskt hus/tak), -2 detalj 3:2, -3 färdigt resultat 3:2. Inga personer/text.
Kör: REPLICATE_API_TOKEN=... python3 tools/gen_images_landing.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import gen_images_flux as g

ORT = {
 "botkyrka": "1970s Swedish villa area with brown concrete tile roofs, Tullinge, birch trees",
 "enskede": "1910s Swedish wooden garden-city house with steep red clay tile roof, Gamla Enskede",
 "borlange": "1950s Swedish villa with red clay tile roof in Dalarna, Borlänge, pines",
 "hagersten": "1940s Swedish functionalist plastered villa with red clay tile roof, Hägersten",
 "ekero": "red Swedish wooden villa with black standing-seam metal roof near lake Mälaren, Ekerö",
 "huddinge": "yellow 1910s Swedish wooden villa with red clay tile roof, Huddinge",
 "farsta": "1950s Swedish brick villa with gray concrete tile roof, Farsta Strand",
 "ludvika": "red wooden Swedish house with red metal roof by a lake in Ludvika, Dalarna",
 "hedemora": "old yellow Swedish wooden house with red clay tile roof in Hedemora, Dalarna",
 "osteraker": "Swedish coastal villa with dark concrete tile roof among pines, Åkersberga",
 "lidingo": "early 1900s Swedish wooden villa with red clay tile roof among pines, Lidingö",
 "solna": "1930s Swedish plastered villa with red clay tile hipped roof, Solna",
 "avesta": "falu red Swedish house with black metal roof in Avesta, Dalarna",
 "tyreso": "1960s Swedish villa with gray concrete tile roof among pines and granite, Tyresö",
 "danderyd": "large 1910s Swedish national romantic villa with steep red clay tile roof, Djursholm",
 "sollentuna": "1960s Swedish brick villa with gray concrete tile roof among tall pines, Sollentuna",
 "varmdo": "red Swedish wooden house with dark standing-seam metal roof in archipelago pine forest, Värmdö",
 "hasselby": "1930s Swedish villa with red clay tile roof near lake Mälaren, Hässelby Villastad",
 "taby": "1970s Swedish villa with brown concrete tile gable roof and wooden facade, Täby",
 "alvsjo": "1920s Swedish wooden villa with brown-red clay tile roof, Älvsjö",
 "kista": "1970s Swedish terraced houses with dark concrete tile roofs, Kista area",
 "vallingby": "1950s Swedish terraced houses with red clay tile roofs, Vällingby",
 "leksand": "falu red Swedish wooden house with black metal roof by lake Siljan, Leksand",
 "bromma": "1920s plastered Swedish villa with steep red clay tile roof and chimney, Bromma",
 "nacka": "early 1900s Swedish wooden villa with red standing-seam metal roof on a granite slope, Nacka",
 "falun": "old falu red wooden house with black metal roof, Falun, Dalarna",
 "rattvik": "falu red Swedish wooden house with grass meadow and black metal roof, Rättvik",
 "haninge": "1970s Swedish villa with dark brown concrete tile roof, Haninge, birches",
 "smedjebacken": "red wooden Swedish house with red metal roof near a lake, Smedjebacken",
 "jarfalla": "1970s Swedish terraced houses with brown concrete tile roofs, Järfälla",
 "sundbyberg": "1930s Swedish villa with red clay tile roof, Sundbyberg",
 "mora": "falu red Swedish wooden house with black metal roof in Mora, Dalarna, snow-free autumn",
 "vallentuna": "1980s Swedish villa with red concrete tile roof, Vallentuna",
 "sater": "old yellow Swedish wooden house with red clay tile roof in Säter, Dalarna",
 "skarholmen": "1960s Swedish brick terraced houses with gray concrete tile roofs, Skärholmen",
 "spanga": "1940s Swedish wooden villa with red clay tile roof, Spånga",
 "upplands-vasby": "1970s Swedish villas with dark concrete tile roofs, Upplands Väsby",
}
TOPIC = {
 "attefallshus-regler": ["small modern Swedish attefallshus guest house 30 m2 with black metal roof in a villa garden"],
 "attefallshus": ["small modern Swedish attefallshus with dark wooden facade and black metal roof in a garden"],
 "byggfirma": ["Swedish villa extension under construction with scaffolding and new roof trusses, safety railings"],
 "energieffektivt-tak": ["Swedish attic with thick new loose-fill insulation between joists, clean and safe"],
 "bygglov-takbyte": ["Swedish 1930s villa with newly replaced black standing-seam metal roof, quiet street"],
 "dalarna": ["falu red Swedish wooden house with black metal roof by a lake in Dalarna"],
 "falsat-plattak": ["close-up of a new black standing-seam metal roof on a Swedish villa"],
 "friggebod": ["small Swedish friggebod garden shed with red wooden facade and black metal roof"],
 "fritidshus": ["new Swedish summer house with wooden facade and black metal roof among pines by the sea"],
 "fuktskada-mogel-vind": ["Swedish attic with roof boards showing old moisture stains, ventilation openings at eaves"],
 "hangrannor-stupror": ["new black metal half-round gutter and downpipe on a Swedish villa roof edge"],
 "istappar-isbildning": ["Swedish villa roof edge in winter with icicles hanging from the gutter, snow on roof"],
 "hyra-taklaggare": ["Swedish villa with scaffolding and roof safety railing during roof replacement, new battens"],
 "mala-plattak": ["freshly painted red corrugated metal roof on an old Swedish wooden house"],
 "nybyggnad-villa": ["new modern Swedish villa with black metal roof and light wooden facade"],
 "nar-ska-taket-bytas": ["worn old concrete tile roof with moss, cracked tiles and rusty flashing on a Swedish villa"],
 "mossa-pa-taket": ["concrete tile roof partly covered with green moss on a Swedish villa under spruce trees"],
 "papptak": ["new black bitumen felt roof on a low-pitched Swedish garage roof"],
 "rot-avdrag-takarbete": ["Swedish villa with a freshly replaced red clay tile roof, sunny day"],
 "plattak": ["new red standing-seam metal roof on a Swedish wooden villa"],
 "skorstensrenovering": ["renovated brick chimney with new black metal flashing on a red tile roof"],
 "sa-valjer-du-taklaggare": ["Swedish villa with scaffolding, roof safety railing and stacked new roof tiles on the roof"],
 "takarbete-vintern": ["Swedish villa with scaffolding and weather protection tarp over the roof in light snow"],
 "takbyte-eller-takrenovering": ["half of a Swedish villa roof with new black tiles and half with old weathered tiles"],
 "solceller-tak": ["solar panels mounted on a black metal roof of a Swedish villa"],
 "taklackage": ["water stain on a ceiling under an attic in a Swedish house, bucket on the floor"],
 "takbesiktning": ["detailed view of a concrete tile roof with flashing around a chimney, inspection perspective"],
 "takfonster": ["new roof window installed in a red tile roof of a Swedish villa"],
 "takbyte": ["Swedish villa during roof replacement: scaffolding with safety railing, new battens and underlay"],
 "takmaterial-livslangd": ["samples of red clay tiles, gray concrete tiles and black metal roofing side by side"],
 "takmalning": ["old Swedish wooden house with freshly painted red metal roof"],
 "takrenovering": ["Swedish villa with freshly renovated gray concrete tile roof and new flashings"],
 "taktvatt": ["clean concrete tile roof on a Swedish villa after roof washing, half still mossy"],
 "tegel-betong-plattak": ["three Swedish villas side by side with red clay tile, gray concrete tile and black metal roofs"],
 "taksakerhet-snorasskydd": ["black snow guard and roof ladder on a black metal roof of a Swedish villa"],
 "tillbyggnad": ["Swedish 1960s villa with a new modern extension with flat black roof"],
 "vad-kostar-bygga-hus": ["new Swedish villa under construction with roof trusses and scaffolding"],
 "var-checklista-tak": ["Swedish villa roof in spring sunshine, clean gutters, blooming tree"],
 "villarenovering": ["renovated Swedish 1950s villa with new roof and fresh facade paint"],
 "vindsisolering": ["Swedish attic with new insulation and walkway boards, clean"],
 "vad-kostar-takrenovering": ["Swedish villa with renovated roof and new metal flashings around the chimney"],
 "vad-kostar-takbyte": ["Swedish villa with newly replaced black concrete tile roof"],
 "villatak": ["Swedish villa street with several houses with different roof types"],
}
DETAIL = "close-up detail of new roof battens, underlay and neatly stacked roof tiles on scaffolding with safety railing"
DONE = "finished new roof with clean ridge, flashings and gutters"

jobs = {}
for o, d in ORT.items():
    b = f"taklaggare-{o}"
    jobs[b + "-1"] = ("4:3", d)
    jobs[b + "-2"] = ("3:2", DETAIL + ", " + d.split(",")[0])
    jobs[b + "-3"] = ("3:2", DONE + " on a " + d.split(",")[0])
for t, (d,) in TOPIC.items():
    jobs[t + "-1"] = ("4:3", d)
    jobs[t + "-2"] = ("3:2", "detail view: " + d)
    jobs[t + "-3"] = ("3:2", DONE + ", Swedish villa, context: " + d)
g.JOBS = jobs
if __name__ == "__main__":
    names = sys.argv[1:] or list(jobs)
    for n in names:
        print(g.run(n), flush=True)
