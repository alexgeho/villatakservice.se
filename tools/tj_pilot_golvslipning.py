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
  6. FAQ: pris + tid (mall) och tre av sidans egna frågor, alla med orten i frågan.
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
 "sollentuna": "Golvslipning Sollentuna – massivt trä och lamell, ROT",
 "spanga": "Golvslipning Spånga – breda brädgolv i villa, gratis offert",
 "sundbyberg": "Golvslipning Sundbyberg – målade och fernissade golv, ROT",
 "tyreso": "Golvslipning Tyresö – gamla brädgolv, gratis platsbesök",
 "upplands-vasby": "Golvslipning Upplands Väsby – radhus och villor, ROT",
 "vallingby": "Golvslipning Vällingby – lamellgolv från 1950-talet, ROT",
 "varmdo": "Golvslipning Värmdö – gamla brädgolv, gratis platsbesök",
 "vasastan": "Golvslipning Vasastan – stavparkett och fiskben, ROT",
}

# Tre av sidans egna frågor: (index i sidans faq, ny fråga med orten | None = frågan nämner redan orten).
FAQ = {
 "alvsjo": [(0, None), (1, "Varför gör ni en provyta innan golvet i Älvsjö pigmenteras?"),
            (2, "Hur länge torkar pigmenterad hårdvaxolja när golvet i Älvsjö har slipats?")],
 "botkyrka": [(0, "Varför är det så mycket spik i det gamla trägolvet i min villa i Tullinge i Botkyrka?"),
              (1, "Går det att slipa lamellgolvet i min lägenhet i Fittja i Botkyrka?"),
              (2, "Vilken luftfuktighet behövs för att lacka ett nyslipat golv i Botkyrka?")],
 "bromma": [(0, None), (1, "Varför ska ett lutat furugolv i Bromma inte lackas?"),
            (2, "Hur många gånger behöver ett lutat golv i Bromma såpas?")],
 "danderyd": [(0, None), (1, "Går det att byta en enstaka skadad stav i parketten i en villa i Danderyd?"),
              (2, "Syns en ny stav bland de gamla i ett parkettgolv i Danderyd?")],
 "ekero": [(0, None), (1, "Hur varmt får ett trägolv med golvvärme på Ekerö bli?"),
           (2, "Varför får golvet på Ekerö springor på vintern när golvvärmen är på?")],
 "enskede": [(0, None), (1, "Varför knarrar det gamla golvet i Enskede bara i gångstråket?"),
             (2, "Kan ett sviktande golv i Enskede slipas jämnt?")],
 "farsta": [(0, None), (1, "Räknas ett fel i det slipade golvet i Farsta om det bara syns i motljus?"),
            (2, "Vad är ondulering på ett slipat golv i Farsta?")],
 "hagersten": [(0, "Hur ser man om parketten i en lägenhet från 1940-talet i Hägersten tål en slipning till?"),
               (1, "Vilket träslag är den ljusa holländska parketten i Hägerstens hus från 1940-talet?"),
               (2, "Kan grå ekparkett i Hägersten få tillbaka färgen utan att slipas?")],
 "haninge": [(0, None), (1, "Hur stor höjdskillnad får det vara mellan två brädor i ett golv i Haninge?"),
             (2, "Kan kupade brädor i en villa i Haninge slipas plana?")],
 "hasselby": [(0, None), (1, "Varför är golvet under linoleummattan i Hässelby fullt av spik?"), (2, None)],
 "huddinge": [(0, None), (1, "Går det att lacka ett oljat golv i Huddinge?"),
              (2, "Kan ett lutat och såpat golv i Huddinge lackas?")],
 "jarfalla": [(0, "Kan trappan slipas samtidigt som golven i radhuset i Järfälla?"),
              (1, "Varför har furutrappan i huset i Järfälla blivit gul?"),
              (2, "Vad ska ledstången i ett radhus i Järfälla behandlas med?")],
 "kista": [(0, None), (1, "Behöver styrelsen godkänna att parketten slipas i en bostadsrätt i Kista?"),
           (2, "Vem betalar ett golv i Kista som skadats av vatten från lägenheten ovanför?")],
 "kungsholmen": [(0, None), (1, "Varför slipar ni med dammavskiljare och andningsskydd i lägenheten på Kungsholmen?"),
                 (2, "Varför får dammsäcken inte stå kvar i lägenheten på Kungsholmen efter slipningen?")],
 "lidingo": [(0, "Vilken yta håller bäst på ett trägolv i köket i en villa på Lidingö?"),
             (1, "Kan man få bort feta fläckar i ett ekgolv på Lidingö utan att slipa?"),
             (2, "Räcker det att olja gångstråken i hallen i huset på Lidingö?")],
 "nacka": [(0, None), (1, "Varför ska oljiga trasor läggas i vatten när golvet i Nacka oljas?"),
           (2, "När ska ett nyoljat golv i Nacka underhållas första gången?")],
 "norrtalje": [(0, "Varför reser sig fibrerna när ett nyslipat skurgolv i Norrtälje skuras?"),
               (1, "Kan ett lackat furugolv i sommarstugan i Norrtälje bli ett skurgolv?"),
               (4, "Ger golvslipning i fritidshuset i Norrtälje rotavdrag?")],
 "osteraker": [(0, None), (1, "Ska ett tjärfärgat golv i Österåker slipas med golvslip?"), (3, None)],
 "ostermalm": [(0, None), (2, "Kan ett vaxat golv på Östermalm lackas över?"),
               (4, "Blir ett fabrikslackat golv på Östermalm bättre av att lackas om på plats?")],
 "sigtuna": [(0, None), (1, "Ska breda springor i ett gammalt plankgolv i Sigtuna fyllas innan det slipas?"), (2, None)],
 "skarholmen": [(0, "Är parketten i min lägenhet från 1960-talet i Sätra i Skärholmen massiv?"),
                (2, "Måste en gammal golvmatta i Bredäng i Skärholmen testas för asbest innan den rivs?"),
                (3, "Får jag rotavdrag för golvslipning i min bostadsrätt i Vårberg i Skärholmen?")],
 "sodermalm": [(0, "Kan jag få rotavdrag för golvslipning innan jag har flyttat in i bostadsrätten på Södermalm?"),
               (1, "Kan slipningen i lägenheten på Södermalm göras före tillträdet?"),
               (2, "Vad betyder det att parketten i ett hus på Södermalm ligger på sand?")],
 "sollentuna": [(0, None), (1, "Hur tunt slitskikt går att slipa på ett lamellgolv i Sollentuna?"),
                (4, "Räcker det att fräscha upp lacken på parketten i Sollentuna i stället för att slipa?")],
 "solna": [(0, "Kan det finnas asbest i limmet under en gammal golvmatta i Solna?"),
           (1, "Går det att slipa undergolvet som låg under linoleummattan i lägenheten i Solna?"),
           (4, "Måste en gammal linoleummatta i Solna rivas?")],
 "spanga": [(0, None), (1, None), (2, "Är hyvling bättre än slipning för ett gammalt brädgolv i Spånga?")],
 "sundbyberg": [(0, "Går det att få bort vit golvfärg ur springorna i ett gammalt golv i Sundbyberg?"),
                (1, "Hur tar man bort gammal fernissa från ett grangolv i Sundbyberg?"),
                (4, "Är det bättre att hyvla än att slipa ett gammalt plankgolv i Sundbyberg?")],
 "taby": [(0, "Hur lagar man golvet där en innervägg har rivits i ett hus i Täby?"),
          (1, "Behövs en anmälan för att riva en vägg i radhuset i Täby?"),
          (4, "Ger rivning av en vägg och slipning av golvet rotavdrag i Täby?")],
 "tyreso": [(0, "Förstör en golvslipmaskin patinan på ett gammalt brädgolv i Tyresö?"),
            (1, "Ska ett silvergrått grangolv i en stuga i Tyresö slipas?"),
            (3, "Varför måste spiken bort innan golvet i Tyresö slipas?")],
 "upplands-vasby": [(0, "Ska glipan mellan golv och sockel tätas efter slipningen i radhuset i Upplands Väsby?"),
                    (2, "Vilken fuktkvot ska trägolvet i Upplands Väsby ha innan det ytbehandlas?"),
                    (4, "Gäller rotavdraget för golvslipning i ett radhus i Upplands Väsby som är bostadsrätt?")],
 "vallentuna": [(0, "Är små runda maskhål i golvplanken i ett gammalt hus i Vallentuna farliga?"),
                (1, "Hur ser man om ett insektsangrepp i golvet i Vallentuna pågår?"),
                (4, "Ger reparation av ett insektsskadat golv i Vallentuna rotavdrag?")],
 "vallingby": [(0, None), (1, "Kan ett golv som sviktar i en lägenhet i Vällingby slipas utan att bli vågigt?"), (3, None)],
 "varmdo": [(0, None), (1, None), (2, None)],
 "vasastan": [(0, None), (1, None), (3, None)],
}


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
        src_sections, src_faq = d["sections"], d["faq"]
        if key in TITLES:
            assert len(TITLES[key]) <= 60 and TITLES[key].startswith(f"Golvslipning {ort} – "), key
            d["title"] = TITLES[key]
        d["time_h2"] = f"Hur lång tid tar golvslipning i {ort}?"
        d["time"] = [
            f"Ett golvjobb i {ort} består av dagar med maskiner och dagar då lacken eller oljan torkar. Hur många "
            "dagar det blir beror på ytan, antalet rum, hur mycket som ska lagas och vilken ytbehandling du väljer. "
            "Enligt Golvbranschens riktlinjer för lackering kan rummet normalt möbleras efter minst ett dygn, medan "
            "mattor bör vänta minst en vecka. Tidplanen står dag för dag i kostnadsförslaget."]
        d["price_h2"] = f"Vad påverkar priset på golvslipning i {ort}?"
        d["price"] = list(d["price"]) + [
            "Vi publicerar inga schablonpriser, eftersom två golv med samma yta kan kräva olika mycket arbete. I "
            "kostnadsförslaget står slipning, lagning och ytbehandling som egna poster, med ROT-avdraget uträknat. "
            f"Hur metoderna och ytbehandlingarna skiljer sig åt, och vad som ingår, beskriver vi på sidan om {HUB}."]
        own = []
        for i, q in FAQ[key]:
            q = q or src_faq[i][0]
            assert ort in q or ort + "s" in q, (f, q)
            own.append((q, src_faq[i][1]))
        tmpl = [
            (f"Vad kostar golvslipning i {ort}?",
             "Det beror på golvytan, golvets skick, hur mycket som ska lagas och vilken ytbehandling du väljer. "
             f"Efter ett gratis platsbesök i {ort} får du ett skriftligt kostnadsförslag, och ROT-avdraget dras direkt på fakturan."),
            (f"Hur lång tid tar en golvslipning i {ort}?",
             "Det beror på ytan och ytbehandlingen. Arbetet består av slipdagar och dagar då lacken eller oljan torkar, "
             "och tidplanen står i kostnadsförslaget."),
        ]
        d["faq"] = tmpl + own
        # sektioner: ortens hus och golv + sidans sakfråga; en tredje bara om texten annars blir för kort
        d["sections"] = src_sections[:2]
        if editorial_words(d) < 700 and len(src_sections) > 2:
            d["sections"] = src_sections[:3]
        n = len(own)
        while editorial_words(d) > 900 and n > 1:
            n -= 1
            d["faq"] = tmpl + own[:n]
        d["pilot_words"] = editorial_words(d)
