# -*- coding: utf-8 -*-
"""Pilot 2026-11-18 (SEO-plan 18.11, avsnitt 4 och 4a): alla 32 golvslipning-<ort>.html efter EN mall.
Körs från tjanster_v1.py efter att modulerna har lästs in och skriver om posterna i TJ (innehållet i
tj_v*_golvslipning.py är orört – mallen väljer ur det). Övriga tjänsters ortsidor väntar på ägarens «ok».

Mall (700–900 ord redaktionell text: lead + sektioner + steg + tid + ROT + pris + FAQ):
  1. title: «Golvslipning <Ort> – <vinkel>, <fördel>» (≤ 60 tecken). H1 «Golvslipning <Ort> – gratis besök och
     kostnadsförslag» sätts i tools/seo_overrides.py (H1_OVERRIDES) – generatorns h1 «Golvslipning i <Ort>»
     används fortfarande för kort, listor och formulärets dolda fält.
  2. Ortens hus och golv (sektion 1, med källa) + sidans sakfråga (sektion 2). Sektion 3–4 utgår.
  3. Steg (oförändrade) + «Hur lång tid tar golvslipning i <Ort>?».
  4. ROT (oförändrad).
  5. «Vad påverkar priset på golvslipning i <Ort>?» med länk i texten till hubben golvslipning.html.
  6. FAQ: pris (mall, med orten) och upp till tre av sidans egna frågor. Orten står bara i frågor om pris, ROT och
     boendeform. Tiden står i sektion 3 och upprepas inte i FAQ.
  7. Källor: bara de som den synliga texten använder (EVIDENCE), LACK 22 på alla sidor (mallstycket om tid).
Inga nya priser eller siffror; tidsuppgifterna är Golvbranschens (LACK 22), som redan citeras på sajten.
Lokala fakta är bara de som redan fanns på sidan med källa."""
import html as _H, re as _re

HUB = '<a class="text-link" href="golvslipning.html">golvslipning i Stockholm</a>'

# Sidor med GSC-styrd title i seo_overrides.py (Bromma, Danderyd, Huddinge, Lidingö, Solna, Täby, Vallentuna)
# behåller den; här står övriga 25.
TITLES = {
 "alvsjo": "Golvslipning Älvsjö – ny kulör på trägolvet, gratis offert",
 "botkyrka": "Golvslipning Botkyrka – furugolv och parkett, gratis offert",
 "ekero": "Golvslipning Ekerö – trägolv med golvvärme, gratis offert",
 "enskede": "Golvslipning Enskede – gamla brädgolv, gratis platsbesök",
 "farsta": "Golvslipning Farsta – parkett i lägenhet och radhus, ROT",
 "hagersten": "Golvslipning Hägersten – parkett från 1940-talet, ROT",
 "haninge": "Golvslipning Haninge – lagning och slipning, gratis offert",
 "hasselby": "Golvslipning Hässelby – trägolv under mattan, gratis offert",
 "jarfalla": "Golvslipning Järfälla – golv och trappa, gratis offert",
 "kista": "Golvslipning Kista – parkett i bostadsrätt, ROT på fakturan",
 "kungsholmen": "Golvslipning Kungsholmen – parkett i bostadsrätt, ROT",
 "nacka": "Golvslipning Nacka – slipa och olja trägolv, gratis offert",
 "norrtalje": "Golvslipning Norrtälje – golv i fritidshus, gratis offert",
 "osteraker": "Golvslipning Österåker – golv i villa och stuga, ROT",
 "ostermalm": "Golvslipning Östermalm – slipa parkett, ROT på fakturan",
 "sigtuna": "Golvslipning Sigtuna – gamla plankgolv, gratis platsbesök",
 "skarholmen": "Golvslipning Skärholmen – parkett i lägenhet, gratis offert",
 "sodermalm": "Golvslipning Södermalm – slipa före inflyttning, ROT",
 "sollentuna": "Golvslipning Sollentuna – slipa trägolv i villa och radhus",
 "spanga": "Golvslipning Spånga – breda brädgolv i villa, gratis offert",
 "sundbyberg": "Golvslipning Sundbyberg – målade och fernissade golv, ROT",
 "tyreso": "Golvslipning Tyresö – gamla brädgolv, gratis platsbesök",
 "upplands-vasby": "Golvslipning Upplands Väsby – radhus och villor, ROT",
 "vallingby": "Golvslipning Vällingby – lamellgolv från 1950-talet, ROT",
 "varmdo": "Golvslipning Värmdö – gamla brädgolv, gratis platsbesök",
 "vasastan": "Golvslipning Vasastan – stavparkett och fiskben, ROT",
}

# Tre av sidans egna frågor: (index i sidans faq, ny fråga | None = sidans egen formulering).
# Regel (granskning 18.11): orten står bara i frågor om pris, ROT och boendeform – hantverksfrågor står utan ort.
_N = None
FAQ = {
 "alvsjo": [(0, _N), (1, _N), (2, _N)], "botkyrka": [(0, _N), (1, _N), (2, _N)], "bromma": [(0, _N), (1, _N), (2, _N)],
 "danderyd": [(0, _N), (1, _N), (2, _N)], "ekero": [(0, _N), (1, _N), (2, _N)], "enskede": [(0, _N), (1, _N), (2, _N)],
 "farsta": [(0, _N), (1, _N), (2, _N)],
 "hagersten": [(0, "Hur ser man om parketten i en lägenhet från 1940-talet i Hägersten tål en slipning till?"), (1, _N), (2, _N)],
 "haninge": [(0, _N), (1, _N), (2, _N)], "hasselby": [(0, _N), (1, _N), (2, _N)], "huddinge": [(0, _N), (1, _N), (2, _N)],
 "jarfalla": [(0, "Kan trappan slipas samtidigt som golven i radhuset i Järfälla?"), (1, _N), (2, _N)],
 "kista": [(0, _N), (1, "Behöver styrelsen godkänna att parketten slipas i en bostadsrätt i Kista?"), (2, _N)],
 "kungsholmen": [(0, _N), (1, _N), (2, _N)], "lidingo": [(0, _N), (1, _N), (2, _N)],
 # nacka: frågan om första underhållet (UNDERHÅLL 22) hörde till en struken sektion
 "nacka": [(0, _N), (1, _N), (4, _N)],
 "norrtalje": [(0, _N), (1, _N), (4, "Ger golvslipning i fritidshuset i Norrtälje rotavdrag?")],
 "osteraker": [(0, _N), (1, _N), (3, _N)], "ostermalm": [(0, _N), (2, _N), (4, _N)], "sigtuna": [(0, _N), (1, _N), (2, _N)],
 "skarholmen": [(0, _N), (2, _N), (3, _N)],
 # sodermalm: frågan om parkett på sand (index 2) tas bara med om sektionen "Parkett som ligger på sand" är kvar
 "sodermalm": [(0, "Kan jag få rotavdrag för golvslipning innan jag har flyttat in i bostadsrätten på Södermalm?"), (1, _N), (2, _N)],
 "sollentuna": [(0, _N), (1, _N), (4, _N)], "solna": [(0, _N), (1, _N), (4, _N)], "spanga": [(0, _N), (1, _N), (2, _N)],
 "sundbyberg": [(0, _N), (1, _N), (4, _N)],
 "taby": [(0, _N), (1, "Behövs en anmälan för att riva en vägg i radhuset i Täby?"),
          (4, "Ger rivning av en vägg och slipning av golvet rotavdrag i Täby?")],
 "tyreso": [(0, _N), (1, _N), (3, _N)],
 "upplands-vasby": [(0, _N), (2, _N), (4, "Gäller rotavdraget för golvslipning i ett radhus i Upplands Väsby som är bostadsrätt?")],
 "vallentuna": [(0, _N), (1, _N), (4, "Ger reparation av ett insektsskadat golv i Vallentuna rotavdrag?")],
 "vallingby": [(0, _N), (1, _N), (3, _N)], "varmdo": [(0, _N), (1, _N), (2, _N)], "vasastan": [(0, _N), (1, _N), (3, _N)],
}
# Egen fråga som kräver att en viss sektion finns kvar: (ort, index) -> sektionens id.
FAQ_NEEDS = {("sodermalm", 2): "sand-sodermalm"}
# Sektionsordning när ingressens fortsättning (hamnar överst i första blocket) hör till sektion 2.
ORDER = {"lidingo": [1, 0, 2, 3]}
# Hänvisningar till sektioner som inte längre finns på en annan ortsida -> hubben.
REWRITE = {
 "bromma": (r' Hur det kontrolleras beskrivs på sidan om <a class="text-link" href="golvslipning-sollentuna.html">[^<]*</a>\.',
            " Hur det går till beskriver vi på sidan om " + HUB + "."),
 "huddinge": (r' Hur det går till beskrivs på sidan om <a class="text-link" href="golvslipning-nacka.html">[^<]*</a>\.',
              " Hur det går till beskriver vi på sidan om " + HUB + "."),
}

from tj_v15_golvslipning import _GBR_LACK  # samma länk som på övriga sidor

# Källa -> uttryck som måste finnas i sidans synliga text för att källan ska stå kvar under «Källor».
# (Regel: varje listad källa används i texten, och varje källa som texten åberopar är listad.)
EVIDENCE = [
 (r"Skatteverket", r"."),
 (r"LACK 22", r"."),  # mallstycket om tid åberopar riktlinjerna för lackering
 (r"SLIP 22", r"SLIP 22|[Rr]iktlinjer(na)? för slipning|slitskikt under en millimeter|6–10 procent|30–60 procent|30 och 60 procent|gnistor|ondulering"),
 (r"OLJA 22", r"OLJA 22|[Rr]iktlinjer(na)? för oljebehandling"),
 (r"LUT 22", r"LUT 22|lutbehandl"),
 (r"UNDERHÅLL 22", r"UNDERHÅLL 22|[Rr]iktlinjer(na)? för underhåll"),
 (r"HÅRDVAXOLJA 22", r"HÅRDVAXOLJA 22"),
 (r"Bedömningsgrunder", r"edömningsgrunder"),
 (r"Trägolv på golvvärme", r"Trägolv på golvvärme|även under mattor|luftfuktare"),
 (r"Golvbranschen – Massiva trägolv", r"[Mm]assiv[at]* trägolv|renoveras i hög utsträckning"),
 (r"Knarr i trägolv", r"[Kk]narr"),
 (r"Golvbranschen – Lamellparkett", r"SS-EN|flerskiktsparkett"),
 (r"Stavar som släpper", r"limfogen"),
 (r"Områdesfakta 2025: Kungsholm", r"Kungsholm"), (r"Områdesfakta 2025: Södermalms", r"Södermalm"),
 (r"Områdesfakta 2025: (.+?) \(pdf\)", None),  # stadsdelens namn ska stå i texten
 (r"Varsam utveckling", r"Varsam"), (r"Riksintressen enligt miljöbalken", r"riksintresse"),
 (r"Boverket – Risker med hantering av asbest", r"Boverket[^.]*asbest|asbest[^.]*Boverket|Provtagning och analys är enligt Boverket"),
 (r"Förvanskningsförbudet", r"örvanskningsförbud"), (r"Ingrepp i husets bärande delar", r"Boverket"),
 (r"Arbetsmiljöverket", r"Arbetsmiljöverket"), (r"Bostadsrättslag", r"ostadsrättslag"), (r"Jordabalk", r"ordabalk"),
 (r"^SCB", r"SCB"),
 # Svenska Byggnadsvårdsföreningen – frågespalt och artiklar (fakta per artikel: se modulernas docstrings)
 (r"– Trägolv( \(spik i golvet\))?$", r"masonit och linoleum"),
 (r"Parkett från 1943", r"holländsk parkett|1943"), (r"Dimension stavparkett", r"1930-talets lamellgolv"),
 (r"Återställa parkettgolv", r"från 1961"), (r"Gammalt parkettgolv", r"halv till en millimeter|0,5 till 1 millimeter"),
 (r"Rädda gammal ekparkett", r"grånar|undanskymd del|rakblad"), (r"60-talsparkett", r"1967"),
 (r"Ytbehandling parkettgolv", r"tidigare behandling först"),
 (r"Lägga ny fiskbensparkett", r"asbesthaltiga utjämningsmassor|hus från 1913"),
 (r"Snygga till trappräcke", r"1969"), (r"Behandling av ny furutrappa", r"gulnar naturligt|linolja fungerar utmärkt"),
 (r"Ytbehandling av handledare", r"fernissa på en handledare"), (r"Val av träslag i ledstång", r"egnahemsvilla från 1940-talet"),
 (r"Material i gammal trapprenovering", r"magnesit"), (r"Renovering av gammal trappa", r"järnskoning"),
 (r"Behandla trägolv i kök", r"disk- och beredningsbänk|linoljefärg"), (r"Behandla massivt obehandlat ekgolv", r"linoljelack|kupa sig"),
 (r"Nytt trägolv i hall", r"grus och skor"), (r"Olja eller slipa ojämnt slitet golv", r"pH-neutralt"),
 (r"Fläckborttagning", r"T-sprit"), (r"Spärrmåla golv", r"schellack"),
 (r"Kan man rädda skurgolven", r"luddigt|några skurningar|skurade golven med sand"),
 (r"Såpa eller skura undergolv", r"mer intakta fibrer"), (r"Göra skurgolv av lackade golv", r"vackrare och mer lättskött"),
 (r"– Lackat$", r"kaustiksoda"), (r"Såpskura nylagt furugolv", r"kallt vatten"),
 (r"Golvbehandling av golv i torp", r"strimmig trägnagare|tidig vårmorgon|skadedjursförsäkring"),
 (r"Täta golvspringor", r"smalast i slutet av sommaren"),
 (r"Breda golvspringor", r"hoptorkade|torkar ihop|sällan vackert|sällan blir vackert"), (r"Tjärat trägolv", r"tjärpapp|excenterslip"),
 (r"Materialhörnan – Parkettgolv", r"Nordiska museet"), (r"1980-talets robusta charm", r"antikvarie"),
 (r"Slipa eller inte slipa golv", r"funktionalismens|omodernt med trägolv"), (r"Hallgolv i lägenhet från 1930", r"lägenhet från 1930"),
 (r"Korkmattan", r"67 procent"), (r"Materialhörnan – Gamla trägolv", r"heltäckande plastmattor|masonitskivor"),
 (r"Måla linoleumgolv", r"rekonditioneras"), (r"Golv och väggar – renovera", r"förhöjd fukthalt|syns tydligare"),
 (r"Parkettgolv \(tejp", r"rödsprit"), (r"Slipa golv från sent 1800-tal", r"sedan 1970-talet|sätter igen slipbanden"),
 (r"Slipa vitmålat plankgolv", r"runnit ned mellan|vit lasur|restlöst"), (r"Renovera fernissat golv", r"såpa under plast|ren såpa i ett dygn"),
 (r"Ta bort fernissa", r"basiska såpan|outspädd flytande såpa"), (r"Måla om flagnat trägolv", r"Inför ommålning"),
 (r"Spikhål i gammalt brädgolv", r"spikhål|randigheten"),
 (r"Hur renovera buckliga originalgolv", r"buckliga originalgolv|kärnsidan|senvintern|sicklas bort|motståndskraftig yta"),
 (r"Är mitt hus angripet", r"byggmästare|ofarliga"), (r"Reparera golvplankor med insektsangrepp", r"linoleummatta ovanpå|ouppvärmt med en linoleummatta"),
 (r"Laga 1700/1800-talsgolv", r"djupa skador|spår av historien|hantverksmässigt utförda"), (r"Vitt pulver", r"mögelpåväxt|ytlig påväxt"),
 (r"Mellanrum mellan golv och sockel", r"kvartsstav|glipan"), (r"Mögellukt", r"mögellukt|jämföra fuktkvoten|jämför med ställen"),
 (r"– Vad göra\?", r"silvergrått"), (r"Hur ska jag gå vidare med detta golv", r"handslipmaskin|oscillerande"),
 (r"Nåta skurgolv", r"1920-talshus"), (r"Finns det någon metod för att lossa golv", r"rundad på undersidan|hur golvet är lagt"),
 (r"Renovera eller nytt", r"varit två rum|undergolv för en linoleummatta"), (r"Golv i sekelskifteshus", r"helst en sickling|1904"),
 (r"Ny vägg sekelskifteslägenhet", r"minimera infästningarna"), (r"Lägga nytt golv på en tredjedel", r"mindre sågverk"),
 (r"Bleka järnvitriol", r"gråna"), (r"– Stavparkett$", r"lekman"),
 # kommunernas och museernas underlag hör till sektion 1 (ortens hus), som alltid är kvar
 (r"kommun –|stad –|stadsmuseum –|läns museum –", r"."),
]


def visible_text(d):
    t = [d["lead"], d["steps_h2"], d.get("time_h2", ""), d["rot_h2"], d["price_h2"]]
    for s in d["sections"]:
        t += [s["h2"]] + s["paras"] + ([s["aside"]["title"]] + s["aside"]["items"] if s.get("aside") else [])
    t += [x for st in d["steps"] for x in st] + d.get("time", []) + d["rot"] + d["price"] + [x for f in d["faq"] for x in f]
    return _H.unescape(_re.sub(r"<[^>]+>", " ", " ".join(t)))


def used_sources(d, sources):
    """Behåll bara källor som den synliga texten använder; okända källor behålls och rapporteras."""
    txt, out, unknown = visible_text(d), [], []
    for name, url in sources:
        for pat, ev in EVIDENCE:
            m = _re.search(pat, name)
            if m:
                ev = ev if ev is not None else _re.escape(m.group(1))
                if _re.search(ev, txt):
                    out.append((name, url))
                break
        else:
            out.append((name, url)); unknown.append(name)
    return out, unknown


def _wc(x):
    return len(_re.findall(r"[a-zåäöéü0-9]+", _H.unescape(_re.sub(r"<[^>]+>", " ", x)).lower()))


def editorial_words(d):
    """Redaktionell text: lead, sektioner (med faktaruta), steg, tid, ROT, pris och FAQ – inte formulär,
    förtroendeblock, kort, ortslistor eller källor."""
    t = [d["lead"], d["steps_h2"], d.get("time_h2", ""), d["rot_h2"], d["price_h2"]]
    for s in d["sections"]:
        t += [s["h2"]] + s["paras"] + ([s["aside"]["title"]] + s["aside"]["items"] if s.get("aside") else [])
    t += [x for st in d["steps"] for x in st] + d.get("time", []) + d["rot"] + d["price"] + [x for f in d["faq"] for x in f]
    return sum(_wc(x) for x in t)


def apply(TJ):
    for f, d in TJ.items():
        if d["service"] != "golvslipning" or d["kind"] != "district":
            continue
        key, ort = f[len("golvslipning-"):-5], d["ort"]
        src_sections, src_faq, src_sources = d["sections"], d["faq"], d["sources"]
        d["_all_sections"], d["_all_faq"], d["_all_sources"] = src_sections, src_faq, src_sources  # för kontroll
        if key in ORDER:
            src_sections = [src_sections[i] for i in ORDER[key] if i < len(src_sections)]
        if key in REWRITE:
            pat, new = REWRITE[key]
            hit = [0]
            def _fix(p):
                q, n = _re.subn(pat, lambda m: new, p); hit[0] += n; return q
            src_sections = [dict(s_, paras=[_fix(p) for p in s_["paras"]]) for s_ in src_sections]
            assert hit[0] == 1, (f, "hänvisningen hittades inte")
        if key in TITLES:
            assert len(TITLES[key]) <= 60 and TITLES[key].startswith(f"Golvslipning {ort} – "), key
            d["title"] = TITLES[key]
        d["time_h2"] = f"Hur lång tid tar golvslipning i {ort}?"
        d["time"] = [
            f"Ett golvjobb i {ort} består av dagar med maskiner och dagar då lacken eller oljan torkar. Hur många "
            "dagar det blir beror på ytan, antalet rum, hur mycket som ska lagas och vilken ytbehandling du väljer. "
            "Enligt Golvbranschens riktlinjer för lackering kan rummet normalt möbleras efter minst ett dygn, medan "
            "mattor bör vänta minst en vecka. Tidplanen står i kostnadsförslaget."]
        d["price_h2"] = f"Vad påverkar priset på golvslipning i {ort}?"
        d["price"] = list(d["price"]) + [
            "Vi publicerar inga prislistor, eftersom två golv med samma yta kan kräva olika mycket arbete. I "
            "kostnadsförslaget står slipning, lagning och ytbehandling som egna poster, med ROT-avdraget uträknat. "
            f"Hur metoderna och ytbehandlingarna skiljer sig åt, och vad som ingår, beskriver vi på sidan om {HUB}."]
        tmpl = [
            (f"Vad kostar golvslipning i {ort}?",
             "Det beror på golvytan, golvets skick, hur mycket som ska lagas och vilken ytbehandling du väljer. "
             f"Efter ett gratis platsbesök i {ort} får du ett skriftligt kostnadsförslag, och ROT-avdraget dras direkt på fakturan."),
        ]

        def own_faq(sections):
            ids = {s_["id"] for s_ in sections}
            return [(q or src_faq[i][0], src_faq[i][1]) for i, q in FAQ[key]
                    if FAQ_NEEDS.get((key, i), None) in ids | {None}]

        # sektioner: ortens hus och golv + sidans sakfråga; en tredje bara om texten annars blir för kort
        d["sections"] = src_sections[:2]
        d["faq"] = tmpl + own_faq(d["sections"])
        if editorial_words(d) < 700 and len(src_sections) > 2:
            d["sections"] = src_sections[:3]
            d["faq"] = tmpl + own_faq(d["sections"])
        own = d["faq"][1:]
        n = len(own)
        while editorial_words(d) > 900 and n > 1:
            n -= 1
            d["faq"] = tmpl + own[:n]
        srcs = list(src_sources)
        if not any("LACK 22" in n_ for n_, _ in srcs):
            pos = next((i for i, (n_, _) in enumerate(srcs) if n_.startswith("Skatteverket")), len(srcs))
            srcs.insert(pos, _GBR_LACK)
        d["sources"], d["_unknown_sources"] = used_sources(d, srcs)
        d["pilot_words"] = editorial_words(d)
