# -*- coding: utf-8 -*-
"""Plåtslagare – hubb (platslagare.html) + ortsidor v4: Bromma, Nacka, Täby, Solna, Huddinge, Lidingö
(2026-10-25). Fakta endast från källorna i respektive 'sources', öppnade 2026-10-25: Boverket (PBL
kunskapsbanken: fasadändring, lydelse efter 1 december 2025; risker med fönster och dörrar), Skatteverket
(rotarbete, rotavdragets belopp), Stockholms stad (fasadändring på bygglov.stockholm; Varsam utveckling av
småhus- och villaområden), Nacka kommun (fasadändringar; kulturmiljöprogram Sommarnöjen vid farleden och
Villasamhällen vid järnvägen), Täby kommun (fasadändring; Kulturmiljöer i Täby), Solna stad (bygglovsfria
åtgärder; kulturmiljöer i Solna), Huddinge kommun (ändra fasad eller tak; dagvattenbroschyr;
kulturmiljöprogram del 2), Lidingö stad (ändrade regler; frågor och svar om kulturmiljöprogrammet) och SMHI
(salt i haven). Inga priser, garantier, omdömen, egna uppdrag eller cert. Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_FASAD = ("Boverket – PBL kunskapsbanken: Bygglov för fasadändring",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_BV_FONST = ("Boverket – Risker med fönster och dörrar",
             "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/risker-fonster-dorrar/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_STH_FASAD = ("Stockholms stad – Fasadändring (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_HUD_DAG = ("Huddinge kommun – Hur tar jag hand om mitt dagvatten? (broschyr, pdf)",
            "https://www.huddinge.se/globalassets/huddinge.se/bostad-och-miljo/din-bostad-och-tomt/vatten-och-avlopp/dagvattenbroschyr")
_HUD_FASAD = ("Huddinge kommun – Ändra fasad eller tak",
              "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/fasadandring")
_HUD_KMP = ("Huddinge kommun – Kulturmiljöprogram del 2 (pdf)",
            "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf")
_TABY_KMP = ("Täby kommun – Kulturmiljöer i Täby, riktlinjer (pdf)",
             "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf")
_SMHI = ("SMHI – Salt i haven runt Sverige",
         "https://www.smhi.se/kunskapsbanken/oceanografi/haven-runt-sverige/salt-i-haven-runt-sverige-")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ HUBB
"platslagare.html": {
  "kind": "hub", "service": "platslagare", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Stockholm – tak, rännor, bleck och beslag",
  "description": "Plåtslagare i Stockholm för villa: plåttak, hängrännor och stuprör, fönsterbleck, "
                 "skorstensbeslag och plåtfasad. Lov sedan 1 december 2025 och ROT-avdrag.",
  "h1": "Plåtslagare i Stockholm",
  "lead": "Plåten på ett hus sitter där vattnet tar sig in om något är fel: i falsar, ränndalar, runt "
          "skorstenen, under fönstren och längs takfoten. Geal Entreprenad AB har egna plåtslagare och tar "
          "hand om allt från ett läckande skorstensbeslag till ett nytt plåttak, med gratis platsbesök, "
          "skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Plåttak, hängrännor och beslag.",
  "sections": [
    {"id": "platarbeten", "anchor": "Plåtarbetena",
     "h2": "Fem delar av huset där plåten gör jobbet",
     "paras": [
       "En plåtslagare arbetar sällan bara med taket. På en villa handlar uppdraget lika ofta om detaljerna "
       "som binder ihop tak och vägg: fotplåt och vindskivor, ränndalar mellan två takfall, beslag kring "
       "skorsten och ventilationshuvar, fönsterbleck och sockelplåt. De är små ytor, men de leder bort "
       "vatten från de mest utsatta punkterna i klimatskalet.",
       "Vi delar in arbetet i fem områden. Plåttaket som helhet, takavvattningen med hängrännor och "
       "stuprör, fönsterbleck och andra fasadbleck, beslagen kring skorstenen och plåt som fasadmaterial. "
       "Samma hantverk ligger bakom alla fem – att bocka, falsa och fästa plåt så att den rör sig med "
       "temperaturen utan att släppa in vatten.",
       "Varje område har en egen fördjupning på sajten, och här samlar vi det som binder ihop dem: hur "
       "skadorna hänger samman, vad lagen säger om materialbyten och vad som ger rotavdrag.",
     ],
     "aside": {"title": "Plåtslagarens arbetsfält", "items": [
       "Plåttak: falsat eller profilerat", "Hängrännor, stuprör och utkastare",
       "Fönsterbleck och sockelplåt", "Skorstensbeslag och intäckning", "Plåt som fasadbeklädnad"]}},
    {"id": "tak-och-detaljer", "h2": "Plåttaket – och plåten på andra tak",
     "paras": [
       "Ett plåttak läggs antingen som bandtäckning med falsade skarvar eller som profilerade skivor som "
       "skruvas fast. Skillnaderna mellan metoderna, och när taket kan tätas i stället för att bytas, går vi "
       "igenom på sidan om " + _L.format("plattak.html", "plåttak") + " och i artikeln om "
       + _L.format("falsat-plattak.html", "falsat plåttak och bandtäckning") + ". Ska ett befintligt plåttak "
       "få nytt ytskikt finns mer under " + _L.format("mala-plattak.html", "måla plåttak") + ".",
       "Även ett tegel- eller betongpannetak är beroende av plåt. Ränndalen mellan två takfall, fotplåten "
       "som leder vattnet ner i rännan och nockens avslutning är plåtarbeten, och på ett äldre tak är det "
       "ofta de som har gett upp först. Därför ser vi över plåtdetaljerna vid varje "
       + _L.format("takbesiktning.html", "takbesiktning") + " och föreslår åtgärder del för del.",
       "Vid ett takbyte görs plåtarbetet om i samma etapp, eftersom ställningen redan står. Gäller det "
       "bara en ränndal eller en takfot kan det ofta göras separat med en mindre ställning.",
     ],
     "aside": None},
    {"id": "avvattning", "h2": "Takavvattning: från rännan till marken",
     "paras": [
       "Hängrännor och stuprör ska ta emot allt vatten som rinner av taket och lämna det på rätt ställe. "
       "När rännan lutar fel, skarvarna glappar eller rören är igensatta rinner vattnet längs fasaden eller "
       "ner mot grunden. Rensning, byte och justering beskriver vi på sidan om "
       + _L.format("hangrannor-stupror.html", "hängrännor och stuprör") + ".",
       "Kommunerna har dessutom åsikter om vart vattnet tar vägen. Huddinge kommun beskriver i sin "
       "dagvattenbroschyr hur stuprör kan förses med utkastare och ränndalsplattor, och att utkastaren bör "
       "vara minst 20 centimeter lång för att undvika vattenstänk på fasaden. Närmast huset bör marken luta "
       "minst 1:20 på en sträcka av minst tre meter, och vattnet får inte ledas ut på gatan eller till "
       "grannen. Vilka regler som gäller där du bor avgörs av detaljplanen och VA-huvudmannen.",
       "Avvattningen hänger också ihop med vintern. Smältvatten som fryser i rännan bildar istappar och "
       "kan trycka isen bakåt in under fotplåten. Mer om det under "
       + _L.format("istappar-isbildning.html", "istappar och isbildning") + ".",
     ],
     "aside": {"title": "Kontrollera själv efter regn", "items": [
       "Rinner vatten över rännkanten?", "Droppar det från skarvarna?",
       "Stänker vatten upp på sockeln?", "Står vatten kvar vid grunden?"]}},
    {"id": "bleck-och-beslag", "h2": "Fönsterbleck och skorstensbeslag",
     "paras": [
       "Boverket räknar bleckens lutning och om blecken inte sluter tätt mot väggen till de faktorer som "
       "avgör risken för fuktskador vid fönster och dörrar. Myndigheten pekar också på att det ska finnas en "
       "dränerande och ventilerande spalt under fönsterblecket, så att vatten som ändå tar sig in kan torka "
       "ut. Ett nytt bleck mäts därför upp efter fönstret och fasaden och bockas med uppvik mot karmen och "
       "en droppkant som släpper vattnet utanför väggen. Byts fönstren samtidigt, se "
       + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
       "Kring skorstenen möts murverk och tak, och rörelserna mellan dem gör beslaget till en av takets "
       "vanligaste läckpunkter. Intäckningen ska ha rätt överlapp mot pannorna och en anslutning mot "
       "murverket som tål att skorstenen och taket rör sig olika. Hur beslag och murning åtgärdas beskriver "
       "vi i " + _L.format("skorstensrenovering.html", "skorstensrenovering och skorstensbeslag") + ".",
     ],
     "aside": {"title": "Bleck som ofta behöver bytas", "items": [
       "Fönsterbleck utan uppvik", "Sockelplåt som släppt", "Skorstensbeslag med spruckna fogar",
       "Vindskivor och nockplåt efter storm"]}},
    {"id": "platfasad-lov", "h2": "Plåtfasad, materialval och lov sedan 1 december 2025",
     "paras": [
       "Plåt används även som fasadbeklädnad, till exempel på tillbyggnader, garage och kring kupor. Enligt "
       "Boverket är byte till ett annat material på fasad eller tak – som från tegeltak till plåttak eller "
       "från puts till panel – en fasadändring. Att byta mot samma material och utförande räknas däremot som "
       "underhåll.",
       "Sedan 1 december 2025 krävs inget bygglov för fasadändringar på en- och tvåbostadshus. Undantagen "
       "är byggnader och områden som är särskilt värdefulla, hus med skyddsbestämmelser i detaljplan eller "
       "områdesbestämmelser och planer med utökad lovplikt. På andra byggnader, som flerbostadshus, krävs "
       "fortfarande lov inom detaljplan när ändringen görs på en fasad eller ett tak mot allmän plats. "
       "Läs mer i " + _L.format("bygglov-takbyte.html", "bygglov vid takbyte") + ".",
       "Materialet påverkar också dagvattnet. Huddinge kommun råder villaägare att vid om- och nybyggnad "
       "välja tak- och fasadmaterial som inte förorenar dagvattnet, och nämner kopparbleck och omålade "
       "zinkytor som exempel att undvika. På ett hus där koppar är en del av originalet kan det ändå vara "
       "rätt att fortsätta i koppar, och det reder vi ut med kommunen innan materialet beställs.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtarbete till",
  "steps": [
    ("Platsbesök", "Vi går igenom tak, rännor, bleck och beslag och letar efter var vattnet faktiskt tar vägen."),
    ("Lov och material", "Vi kontrollerar om huset ligger i ett värdefullt område och om materialvalet kräver lov."),
    ("Skriftligt förslag", "Varje del – tak, avvattning, bleck och beslag – prissätts för sig så att du kan välja."),
    ("Mått och bockning", "Bleck och beslag mäts upp på plats och bockas efter huset, inte efter standardmått."),
    ("Montering", "Plåten fästs så att den kan röra sig med temperaturen, med täta skarvar och rätt överlapp."),
    ("Kontroll och avslut", "Vi går igenom avvattningen tillsammans och tar med oss allt överblivet material."),
  ],
  "rot_h2": "ROT-avdrag för plåtarbeten",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att reparera, rengöra eller byta ut plåttak, "
    "hängrännor och stuprör, att byta och reparera fönsterbleck, att mura och reparera skorstenar och att "
    "montera och montera ner byggnadsställningar i samband med rotarbetet. Avdraget är högst 30 procent av "
    "arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med "
    "rutavdrag. Material och resekostnader ger inget avdrag.",
    "I en bostadsrätt ger plåt- och glasarbeten utanför den egna bostaden inte rotavdrag. Geal drar "
    "avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden för plåtarbetet",
  "price": [
    "Hur mycket plåt som byts, om detaljerna kan bockas av standardplåt eller behöver tillverkas efter "
    "förlaga, vilket material och vilken kulör som väljs, hur många genomföringar och kupor taket har och "
    "hur hög ställning som krävs. Ett arbete som görs samtidigt med ett takbyte delar ställning med det. "
    "Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan en plåtslagare byta bara ränndalen på ett tegeltak?",
     "Ja. Pannorna närmast ränndalen lyfts av, den gamla ränndalsplåten tas bort och underlaget kontrolleras "
     "innan ny plåt läggs in och pannorna läggs tillbaka."),
    ("Hur långt ut ska stuprörets utkastare gå?",
     "Huddinge kommun anger att utkastaren bör vara minst 20 centimeter lång för att undvika stänk på fasaden, "
     "och att marken närmast huset ska luta bort från det."),
    ("Behövs bygglov för att klä en tillbyggnad med plåt?",
     "På ett en- eller tvåbostadshus normalt inte sedan 1 december 2025, om huset inte är särskilt värdefullt, "
     "har skyddsbestämmelser eller ligger i ett område med utökad lovplikt."),
    ("Varför ska det finnas en spalt under fönsterblecket?",
     "Boverket beskriver spalten som ett sätt att låta fönstret dränera och torka ut, så att vatten som tagit "
     "sig in under blecket inte blir stående mot karm och vägg."),
    ("Ger byte av fönsterbleck rotavdrag?",
     "Ja. Skatteverket räknar byte och reparation av fönsterbleck i småhus som rotarbete. Själva plåten räknas "
     "som material och ger inget avdrag."),
    ("Ska jag undvika kopparbleck på huset?",
     "Huddinge kommun nämner kopparbleck och omålade zinkytor som material att undvika med hänsyn till "
     "dagvattnet. Är koppar en del av husets ursprungliga utförande stämmer vi av med kommunen först."),
  ],
  "sources": [_BV_FASAD, _BV_FONST, _HUD_DAG, _SKV_LISTA, _SKV_ROT],
  "cta": ("Läcker det vid plåten?", "Boka ett gratis platsbesök så går vi igenom tak, rännor, bleck och beslag."),
  "img": [
    ("Villa med nytt svart falsat plåttak, hängrännor och stuprör i plåt",
     "Swedish 1930s white rendered villa with a new black standing-seam metal roof, matching black half-round "
     "gutters and downpipes, metal chimney flashing, suburban Stockholm garden, clear autumn day"),
    ("Nytt bockat fönsterbleck med droppkant under ett träfönster",
     "close-up of a newly fitted folded metal window sill flashing with drip edge under a white wooden window "
     "on a painted wooden facade, soft daylight"),
  ],
  "related": [
    ("plattak.html", "Plåttak", "Nytt plåttak, bandtäckning och reparationer."),
    ("falsat-plattak.html", "Falsat plåttak och bandtäckning", "Klassiskt plåttak för låga lutningar."),
    ("hangrannor-stupror.html", "Hängrännor och stuprör", "Rensa, renovera eller byta."),
    ("skorstensrenovering.html", "Skorstensrenovering och beslag", "Täta och renovera kring skorstenen."),
  ],
},

# ------------------------------------------------------------------ BROMMA
"platslagare-bromma.html": {
  "kind": "district", "service": "platslagare", "ort": "Bromma", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Bromma – kupor, låga tak och fönsterbleck",
  "description": "Plåtslagare i Bromma: plåt kring takkupor i trädgårdsstäderna, låga tak i Södra Ängby, "
                 "fönsterbleck på puts och panel och stadens regler för fasadändring.",
  "h1": "Plåtslagare i Bromma",
  "lead": "I Bromma sitter plåten ofta på ställen som är lätta att glömma: kring de små takkuporna mitt på "
          "trädgårdsstädernas långsidor, längs takfoten på funkisvillornas låga tak och under fönstren. "
          "Geal Entreprenad AB har egna plåtslagare som lagar och byter beslag, rännor och bleck i hela "
          "Bromma, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Kupor, låga tak och bleck i Bromma.",
  "sections": [
    {"id": "kupor", "anchor": "Takkupor i Bromma",
     "h2": "Små takkupor på branta tegeltak",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur 1920-talets klassiska "
       "formspråk tog över i Nockeby, Höglandet, Ålsten, Smedslätten och Ulvsunda. Husen var enkla volymer i "
       "ett och ett halvt plan, de branta sadeltaken i rött tegel gav stadsdelarna en enhetlig karaktär, och "
       "små konstfulla takkupor mitt på långsidorna gav varje hus en egen identitet.",
       "För en plåtslagare är kupan det mest krävande stället på ett sådant tak. Kupans tak, dess sidor och "
       "anslutningen mot pannorna består av plåt som ska ta emot vattnet från ett brant takfall och leda det "
       "runt kupan. Där plåten har spruckit, lagats med fogmassa eller lagts om utan rätt överlapp brukar "
       "fukten synas inne på vinden innan den syns utifrån.",
       "Vägledningen råder ägarna att ta tillvara eller återskapa karaktärsskapande material och byggnadsdelar. "
       "När vi gör om plåten kring en kupa utgår vi därför från de profiler och den kulör som finns, så att "
       "kupan behåller sitt utseende från gatan.",
     ],
     "aside": {"title": "Plåten kring en takkupa", "items": [
       "Kupans eget tak", "Sidobeslag mot pannorna", "Ränndal eller nackskiva bakom kupan",
       "Fotplåt och ränna under fönstret"]}},
    {"id": "sodra-angby", "h2": "Låga tak och tunna takfötter i Södra Ängby",
     "paras": [
       "Södra Ängby blev enligt vägledningen den sista stadsdelen som planerades efter trädgårdsstadens "
       "principer, men husen fick ett modernistiskt formspråk: kubiska volymer, oftast i två våningar, med "
       "svagt lutande tak och brutet vita eller ljust grå fasader i slätputs eller liggande träpanel. Staden "
       "beskriver området som ett av Europas största sammanhängande områden av villor från 1930-talet i "
       "modernistisk stil.",
       "På ett svagt lutande tak rinner vattnet långsamt, och därför blir skarvar, genomföringar och "
       "takfotens plåt avgörande för tätheten. På de här husen är takkanten dessutom en del av arkitekturen. "
       "En grov fotplåt eller en vindskiva som är bredare än originalet syns direkt mot den släta fasaden.",
       "Vi mäter upp befintliga profiler innan något rivs och bockar ny plåt efter dem. Är taket i så dåligt "
       "skick att hela tätskiktet behöver göras om finns mer under "
       + _L.format("takrenovering-bromma.html", "takrenovering i Bromma") + ".",
     ],
     "aside": None},
    {"id": "bleck-bromma", "h2": "Fönsterbleck på putsade och panelklädda villor",
     "paras": [
       "Bromma har både putsade fasader och stående eller liggande träpanel, och på båda är fönsterblecket "
       "en svag punkt. Boverket nämner bleckens lutning och om blecken sluter tätt mot väggen som faktorer "
       "som påverkar risken för fuktskador vid fönster, och att det behövs en dränerande och ventilerande "
       "spalt under blecket.",
       "På en putsad funkisvilla ska blecket gå in under putsens kant eller ha ett uppvik som tätas mot "
       "fasaden, och droppkanten ska släppa vattnet så långt ut att putsen under fönstret inte blir "
       "randig. På en panelfasad ska blecket ligga över bröstningsbrädan och släppa vattnet utanför "
       "panelen. I båda fallen kontrollerar vi karmens nederkant när det gamla blecket är borta.",
       "Ska fasaden renoveras samtidigt är det klokt att göra blecken i samma etapp, se "
       + _L.format("fasadrenovering-bromma.html", "fasadrenovering i Bromma") + ".",
     ],
     "aside": {"title": "Tecken på att blecket har gjort sitt", "items": [
       "Randig puts under fönstret", "Flagnande färg på bröstningen",
       "Blecket lutar in mot karmen", "Rost längs vikningen"]}},
    {"id": "lov-bromma", "h2": "Materialbyte, kupor och stadens klassificering",
     "paras": [
       "Stockholms stad räknar byte av kulör eller material på fasad eller tak, nya fönster och dörrar samt "
       "balkonger och mindre takkupor som fasadändringar. För en- och tvåbostadshus krävs normalt inget "
       "bygglov för dem sedan 1 december 2025, men lov behövs om huset är särskilt värdefullt, ligger i ett "
       "särskilt värdefullt område eller om detaljplanen har skyddsbestämmelser.",
       "Stadsmuseets klassificeringskarta ger en första indikation, men staden påpekar att alla byggnader och "
       "områden ännu inte är inventerade och att man kan behöva kontakta Stadsmuseet för en bedömning. "
       "Vägledningen pekar dessutom ut Ålstensgatan och Södra Ängby som riksintressen.",
       "Att byta plåt mot samma material och utförande räknas enligt Boverket som underhåll. Att gå från "
       "tegel till plåt på ett tak, eller att bygga en ny kupa, är däremot ändringar som kan kräva lov i de "
       "värdefulla områdena. Lokala takarbeten i stort hittar du under "
       + _L.format("taklaggare-bromma.html", "takläggare i Bromma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med plåten på en Brommavilla",
  "steps": [
    ("Besök med stege och kikare", "Vi tittar på kupor, ränndalar, takfot och bleck och på vinden där fukt brukar synas först."),
    ("Klassning och plan", "Stadsmuseets karta och detaljplanen stäms av innan material och kulör bestäms."),
    ("Förslag del för del", "Kupor, rännor och bleck prissätts var för sig i ett skriftligt kostnadsförslag."),
    ("Uppmätning", "Befintliga profiler mäts så att ny plåt får samma mått och vikningar."),
    ("Byte och anslutningar", "Gammal plåt tas bort, underlaget kontrolleras och ny plåt monteras med rätt överlapp."),
    ("Genomgång", "Vi går igenom arbetet tillsammans och visar var vattnet tar vägen."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Bromma",
  "rot": [
    "För ett småhus ger det rotavdrag att reparera eller byta plåttak, hängrännor och stuprör och att byta "
    "fönsterbleck, enligt Skatteverket. Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kr "
    "per person och år, inom ett gemensamt tak på 75 000 kr för rot och rut.",
    "Plåten och resorna ger inget avdrag. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här påverkar priset i Bromma",
  "price": [
    "Antalet kupor och ränndalar, om profilerna behöver tillverkas efter förlaga, hur mycket av takfoten och "
    "blecken som byts och vilken ställning som behövs för att nå kuporna på ett brant tak. Efter ett "
    "kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Läcker det ofta kring takkuporna på 1920-talsvillorna i Ålsten?",
     "Kupan är en vanlig läckpunkt eftersom plåten där tar emot vatten från ett brant takfall. Spruckna "
     "beslag och lagningar med fogmassa är tecken på att plåten behöver göras om."),
    ("Kan plåten på ett lågt tak i Södra Ängby bytas utan bygglov?",
     "Byts plåten mot samma material och utförande räknas det som underhåll. Ändras material, kulör eller "
     "takkantens utformning i riksintresset bör du räkna med att lov kan krävas och stämma av med staden."),
    ("Räknas en ny takkupa som fasadändring i Stockholm?",
     "Ja, staden räknar mindre takkupor till fasadändringarna. På ett en- eller tvåbostadshus utanför de "
     "värdefulla områdena krävs normalt inget lov för dem sedan 1 december 2025."),
    ("Hur ska ett fönsterbleck sitta på en slätputsad funkisvilla?",
     "Med uppvik mot fasaden och en droppkant som släpper vattnet utanför putsen, och med en spalt under "
     "blecket så att fönstret kan torka ut."),
    ("Vad gör vi om Stadsmuseets karta inte visar något för vårt hus i Bromma?",
     "Staden påpekar att alla byggnader ännu inte är inventerade. Ligger huset i en trädgårdsstad eller nära "
     "ett riksintresse är det klokt att fråga Stadsmuseet innan material eller kulör ändras."),
  ],
  "sources": [_STH_FASAD, _VARSAM, _BV_FASAD, _BV_FONST, _SKV_LISTA, _SKV_ROT],
  "cta": ("Behöver plåten på Brommavillan ses över?", "Boka ett gratis platsbesök så går vi igenom kupor, rännor och bleck."),
  "img": [
    ("Trävilla i Bromma med brant rött tegeltak och liten takkupa klädd med plåt",
     "1920s Swedish one-and-a-half storey wooden villa with steep red clay tile roof and a small centred dormer "
     "clad in dark grey standing-seam metal, black metal flashings around the dormer, hedge and fruit trees, "
     "garden city suburb Bromma Stockholm, summer daylight, no people, no text"),
    ("Låg takfot med smal plåtavslutning på en vit funkisvilla",
     "close-up of the low-pitched roof edge of a white rendered 1930s Swedish functionalist villa, thin dark "
     "metal fascia flashing and slim half-round gutter, pine branches, soft daylight, no people, no text"),
  ],
},

# ------------------------------------------------------------------ NACKA
"platslagare-nacka.html": {
  "kind": "district", "service": "platslagare", "ort": "Nacka", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Nacka – plåttak vid farleden och havsluft",
  "description": "Plåtslagare i Nacka: plåttak på sommarvillor och stugor vid farleden, kupor i Saltsjöbaden, "
                 "fästdon i havsnära lägen och kommunens kulturmiljökarta.",
  "h1": "Plåtslagare i Nacka",
  "lead": "Längs farleden i Nacka har plåt legat på taken sedan de första sommarvillorna byggdes, och i "
          "villasamhällena längs Saltsjöbanan är takets form en del av det kommunen vill bevara. Geal "
          "Entreprenad AB har egna plåtslagare som lagar och byter plåttak, beslag och rännor i hela Nacka, "
          "med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Farledens plåttak och Saltsjöbadens villor.",
  "sections": [
    {"id": "farleden-plat", "anchor": "Plåt vid farleden",
     "h2": "Från schweizervillornas plåttak till tegel – och tillbaka",
     "paras": [
       "Kommunens kulturmiljöprogram för sommarnöjena vid farleden beskriver hur de tidiga sommarvillorna "
       "byggdes i en friare trähusarkitektur med snickeridetaljer från ångsågarna. När de nationalromantiska "
       "idéerna slog igenom i början av 1900-talet försvann schweizerutsmyckningarna till förmån för "
       "stramare detaljer, och plåttaken ersattes av tegeltak.",
       "Därför ser taken olika ut från villa till villa. I flera av områdena som programmet beskriver – "
       "bland annat i Vikingshill och på Grävlingsberg – ligger plåt eller tegel på sadeltaken, och "
       "utskjutande taksprång räknas till de karaktärsdrag som bör bevaras. Taksprånget är också det ställe "
       "där plåten möter vind och regn först.",
       "Ett gammalt plåttak på en sommarvilla har ofta lagats många gånger. Innan vi föreslår ett byte "
       "undersöker vi om falsarna går att efterfalsa och om skadorna sitter i plåten eller i anslutningarna "
       "kring skorsten och kupor.",
     ],
     "aside": {"title": "Det programmet lyfter fram", "items": [
       "Plåt eller tegel på sadeltaken", "Utskjutande taksprång", "Ljusmålad panel", "Rejäla stensocklar"]}},
    {"id": "stugor-plat", "h2": "Röd korrugerad plåt på låga stugtak",
     "paras": [
       "Programmet beskriver också de enklare stugorna vid farleden. Om semesteranläggningen Visborgs minne "
       "skriver kommunen att det på de låga sadeltaken oftast ligger röd korrugerad plåt, att takutsprången "
       "är små och att nuvarande materialtyper bör användas vid underhåll och förnyelse. De röda plåttaken "
       "nämns som en del av det som gör stuggrupperna enhetliga.",
       "Har du en före detta sportstuga med samma typ av tak, som numera bebos året runt, gäller samma sak. "
       "En korrugerad plåt som har rostat i överlappen kan ofta bytas skiva för skiva, men då ska "
       "profil, kulör och fästdon stämma med resten av taket.",
       "När en stuga får isolerad vind blir taket kallare utvändigt och snön ligger kvar längre. Då behöver "
       "vi se över takfot, ränna och nock samtidigt, så att smältvatten inte fryser fast vid kanten. Mer om "
       "lokala tak i stort finns under " + _L.format("taklaggare-nacka.html", "takläggare i Nacka") + ".",
     ],
     "aside": None},
    {"id": "havsluft", "h2": "Havsluft, fästdon och utsatta lägen",
     "paras": [
       "Östersjön är bräckt. Enligt SMHI är salthalten i Egentliga Östersjön 6–9 gram per kilo havsvatten, "
       "mot ungefär 35 gram i världshaven. Ändå gör fukt och vind från sjön att plåt, skruv och spik på "
       "strandtomter i Nacka utsätts för mer än på ett hus inne i skogen.",
       "Vi väljer därför fästdon och plåt med ytskydd som passar läget, och undviker att blanda metaller som "
       "inte ska ligga mot varandra. På hus med fritt läge mot farleden kontrollerar vi särskilt vindskivor, "
       "nockplåt och fotplåt, eftersom det är där en storm brukar få fäste.",
       "På branta tomter med berg i dagen planeras ställning och materialhantering redan vid platsbesöket. "
       "Mer om omläggning av hela taket finns under "
       + _L.format("takrenovering-nacka.html", "takrenovering i Nacka") + ".",
     ],
     "aside": {"title": "Extra kontroll vid sjötomt", "items": [
       "Fästdon i nock och vindskivor", "Rost i överlapp och falsar",
       "Fotplåt mot förhärskande vind", "Beslag kring skorstenen"]}},
    {"id": "lov-nacka", "h2": "Saltsjöbadens tak och kommunens lila markering",
     "paras": [
       "I programmet för villasamhällena vid järnvägen skriver kommunen att man i Saltsjöbaden eftersträvar "
       "att bevara befintliga tak, fasader, fönster och entréer, och att takkupor, terrasser och balkonger "
       "helst ska göras mot baksidan med ett utförande som underordnas huset. Tidstypisk utformning av "
       "bland annat tak ska behållas även i övriga villasamhällen längs banan.",
       "Nacka kommun räknar byte av färg eller material på fasad eller tak och mindre takkupor som "
       "fasadändringar. Inom detaljplan krävs inte längre bygglov för dem på en- eller tvåbostadshus, men "
       "åtgärden får inte strida mot planen. Ligger fastigheten i ett område som är särskilt värdefullt "
       "enligt 8 kap. 13 § PBL krävs lov för alla fasadändringar som påverkar områdets karaktär eller "
       "husets yttre.",
       "I kommunens karta visar lila markering särskilt höga kulturvärden, och orange att en bedömning kan "
       "pågå. Att gå från tegel till plåt, eller tvärtom, är just en sådan ändring som prövas där.",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången för plåtarbeten i Nacka",
  "steps": [
    ("Besök på tomten", "Vi bedömer tak, taksprång, rännor och beslag och hur ställningen kan stå i terrängen."),
    ("Karta och plan", "Kulturmiljökartan och detaljplanen kontrolleras innan material eller kulör ändras."),
    ("Kostnadsförslag", "Lagning, delbyte och nytt tak redovisas var för sig i ett skriftligt förslag."),
    ("Val av plåt och fästdon", "Material och skruv väljs efter läget, särskilt på tomter nära vattnet."),
    ("Montering", "Plåten läggs med samma profil och kulör som tidigare där huset kräver det."),
    ("Avslut", "Rännor rensas, vi går igenom arbetet med dig och tar med allt spill."),
  ],
  "rot_h2": "ROT-avdrag för plåtslageri i Nacka",
  "rot": [
    "Skatteverket godkänner rotavdrag för att reparera, rengöra eller byta plåttak, hängrännor och stuprör "
    "på ett småhus, och för ställningen som behövs för arbetet. Avdraget är högst 30 procent av "
    "arbetskostnaden, med 50 000 kr per person och år som tak och 75 000 kr för rot och rut sammanlagt.",
    "Materialet ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Nacka?",
  "price": [
    "Om plåten kan lagas eller behöver bytas, takets form med kupor och taksprång, materialvalet i utsatta "
    "lägen och hur svår tomten är att ställa ställning på. Efter ett gratis platsbesök får du ett skriftligt "
    "kostnadsförslag.",
  ],
  "faq": [
    ("Får vi byta tegeltaket mot plåt på en sommarvilla i Vikingshill?",
     "Utanför de värdefulla områdena krävs normalt inget lov på en villa, men varsamhetskravet gäller. Ligger "
     "huset inom lila markering krävs bygglov för materialbytet."),
    ("Kan en rostig korrugerad plåt på stugtaket bytas skiva för skiva?",
     "Ofta ja, om resten av taket är i gott skick. Profil, kulör och fästdon ska då stämma med de skivor som "
     "sitter kvar."),
    ("Rostar plåt snabbare på en sjötomt i Saltsjöbaden?",
     "Fukt och vind från sjön påfrestar plåt och fästdon mer än i ett skyddat läge, även om Östersjön är "
     "bräckt. Därför väljer vi ytskydd och skruv efter läget."),
    ("Var ska en ny takkupa sitta på en villa i Saltsjöbaden?",
     "Kommunens program anger att takkupor helst görs mot baksidan och underordnas huset. Stäm av med "
     "kommunen tidigt, eftersom lov kan krävas i området."),
    ("Vad gör vi om fastigheten är orange i Nackas karta?",
     "Orange betyder att en bedömning av kulturvärdena kan pågå. Kontakta stadsbyggnadsservice innan "
     "material eller kulör på taket ändras."),
  ],
  "sources": [
    ("Nacka kommun – Fasadändringar",
     "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/lovfria-atgarder/fasadandringar/"),
    ("Nacka kommun – Kulturmiljöprogram: Sommarnöjen vid farleden (pdf)",
     "https://www.nacka.se/499628/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-sommarnojen.pdf"),
    ("Nacka kommun – Kulturmiljöprogram: Villasamhällen vid järnvägen (pdf)",
     "https://www.nacka.se/499626/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-jarnvagen.pdf"),
    _SMHI, _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska plåttaket i Nacka ses över?", "Boka ett gratis platsbesök så bedömer vi om plåten ska lagas eller bytas."),
  "img": [
    ("Sekelskiftesvilla vid vattnet i Nacka med rött plåttak och långa taksprång",
     "late 1800s Swedish wooden summer villa painted pale yellow with white carpentry details, red "
     "standing-seam metal roof with wide overhanging eaves, on a granite slope above a calm Baltic inlet, "
     "pine trees, Nacka Stockholm, summer, no people, no text"),
    ("Liten röd stuga med lågt tak av röd korrugerad plåt bland tallar",
     "small Swedish falu red wooden cottage with a low-pitched gable roof of red corrugated metal sheets and "
     "small eaves, standing on a rocky pine slope near the sea, overcast daylight, no people, no text"),
  ],
},

# ------------------------------------------------------------------ TÄBY
"platslagare-taby.html": {
  "kind": "district", "service": "platslagare", "ort": "Täby", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Täby – takfot, takband och grupphus",
  "description": "Plåtslagare i Täby: plåt på stationsvillornas tak, smala vindskivor i Näsbypark, "
                 "takband på platta tak och bockad plåt i grupphusområden.",
  "h1": "Plåtslagare i Täby",
  "lead": "I Täby skiljer sig plåtarbetet mycket mellan husen: tegel eller plåt på de äldre villorna vid "
          "Roslagsbanan, smala vindskivor på funkisvillorna i Näsbypark och platta tak med takband i "
          "grupphusområdena. Geal Entreprenad AB har egna plåtslagare som arbetar i hela Täby, med gratis "
          "platsbesök och skriftligt kostnadsförslag.",
  "card": "Stationsvillor, funkis och grupphus i Täby.",
  "sections": [
    {"id": "aldre-villor", "anchor": "Täbys villor",
     "h2": "Stationsvillornas tak: tegel eller plåt",
     "paras": [
       "Kommunens kunskapsunderlag Kulturmiljöer i Täby beskriver den äldre villabebyggelsen vid "
       "Roslagsbanans stationer, bland annat längs Sågtorpsvägen i Roslags-Näsby där flera av Täbys äldsta "
       "villor ligger. Husen har sadeltak eller brutna tak, ibland utkragande nedtill, och taken är oftast "
       "täckta med tegelpannor eller plåt.",
       "Ett brutet tak har en knäck där takfallet byter lutning, och ett utkragat nedre takfall kräver att "
       "fotplåten följer svängen. Båda ställena är svåra att få täta med standarddetaljer. Där plåten ligger "
       "på hela taket är det falsarna, skarvarna mot skorstenen och övergången vid knäcken som brukar släppa "
       "först.",
       "Kommunens generella riktlinjer för småhusområden säger att befintliga takformer, takmaterial och "
       "takfotens utformning bör behållas på befintliga hus. Riktlinjerna är inte juridiskt bindande men "
       "används som vägledning i kommunens arbete.",
     ],
     "aside": {"title": "Detaljer på de äldre villorna", "items": [
       "Brutna tak med knäck", "Utkragande nedre takfall", "Tegel eller plåt på taket",
       "Kraftiga socklar mot sluttningen"]}},
    {"id": "nasbypark", "h2": "Funkis i Näsbypark: smala vindskivor och koppar",
     "paras": [
       "I samma underlag lyfter kommunen fram flera villor i Näsbypark. En funkisvilla från 1940 har låga "
       "takfall som inte syns från gatan, och en villa från 1946 beskrivs med ett tak som ger ett lätt "
       "intryck och smala vindskivor. En villa från 1939 har en kopparbaldakin över entrén.",
       "Det är just den sortens detaljer som försvinner om takkanten görs om med grövre plåt. En vindskiva "
       "som är några centimeter högre, eller en fotplåt med annan bockning, ändrar hur hela huset uppfattas. "
       "Vi mäter därför upp profilerna innan något tas bort och bockar ny plåt efter dem.",
       "På de låga taken är det dessutom tätheten som avgör. Vatten rinner långsamt och skarvar, "
       "genomföringar och anslutningar mot vägg måste vara utförda för låg lutning. Mer om det under "
       + _L.format("takrenovering-taby.html", "takrenovering i Täby") + ".",
     ],
     "aside": None},
    {"id": "grupphus", "h2": "Platta tak, takband och bockad plåt i grupphusen",
     "paras": [
       "Underlaget visar två hus från 1968 där envåningshusen ofta har platt tak med brett träpanelat "
       "takband, och parhusen i Erikslund som har enkla, raka former utan takfot – bara en bockad plåt vid "
       "övergången mellan tak och vägg. Om en villa från 1959 skriver kommunen att takfot och stuprännor är "
       "integrerade i byggnaden.",
       "På sådana hus är plåten inte en detalj utan själva gränsen mellan tak och fasad. Byts den mot en "
       "standardprofil ändras hela gatubilden, och på ett platt tak leder en felaktig avslutning vatten in "
       "i takbandet. Därför börjar vi med att dokumentera den befintliga plåten.",
       "I ett grupphusområde är det dessutom praktiskt om flera grannar gör plåtarbetet samtidigt. Då blir "
       "kulör och profil lika på hela längan. Söker du oss för lokala takarbeten finns mer under "
       + _L.format("taklaggare-taby.html", "takläggare i Täby") + ".",
     ],
     "aside": {"title": "Grupphusens plåtdetaljer", "items": [
       "Takband på platta tak", "Bockad plåt utan takfot", "Integrerade stuprännor",
       "Lika kulör längs hela längan"]}},
    {"id": "lov-taby", "h2": "Vad Täby kommun säger om plåt och fasadändring",
     "paras": [
       "Täby kommun skriver att det inte behövs bygglov för fasadändringar på en- och tvåbostadshus om "
       "byggnaden inte är särskilt värdefull, inte ligger i ett särskilt värdefullt område och inte har "
       "utökad lovplikt i detaljplanen. Är du osäker ber kommunen dig kontakta den för rådgivning.",
       "Plåt används också på fasader i Täby. I underlaget nämns punkthusen i kvarteret Höstfibblan, som "
       "ursprungligen hade putsade fasader men som har tilläggsisolerats och fått ljust gula plåtfasader. "
       "Enligt Boverket räknas ett byte till annat fasadmaterial som fasadändring, medan byte mot samma "
       "material och utförande är underhåll.",
       "Kommunen råder också den som ska förändra ett hus att ta fram äldre ritningar, eftersom många hus "
       "har byggts till. Ritningarna visar ofta hur takfot och plåtdetaljer var tänkta från början.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtarbete till i Täby",
  "steps": [
    ("Besök och dokumentation", "Vi fotograferar och mäter takfot, vindskivor och takband innan något rörs."),
    ("Riktlinjer och plan", "Kommunens riktlinjer och detaljplanen kontrolleras inför val av material."),
    ("Skriftligt kostnadsförslag", "Tak, takfot, avvattning och bleck redovisas var för sig."),
    ("Bockning efter förlaga", "Ny plåt bockas efter de profiler som finns på huset."),
    ("Montering och täthet", "Anslutningar mot vägg och genomföringar görs för takets lutning."),
    ("Slutkontroll", "Vi provar avvattningen och går igenom arbetet med dig."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Täby",
  "rot": [
    "Enligt Skatteverket ger det rotavdrag att reparera eller byta plåttak, hängrännor och stuprör och att "
    "byta och reparera fönsterbleck på ett småhus. Avdraget är högst 30 procent av arbetskostnaden och högst "
    "50 000 kr per person och år, och rot och rut får tillsammans uppgå till 75 000 kr.",
    "Material och resor ingår inte. Avdraget dras direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden i Täby",
  "price": [
    "Om plåten kan bockas av standardplåt eller måste tillverkas efter förlaga, hur lång takfoten och "
    "takbandet är, antalet genomföringar och om flera hus i samma länga görs samtidigt. Efter ett gratis "
    "platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan takbandet på ett platt tak från 1968 göras om i plåt?",
     "Det går, men takbandet är en del av husets uttryck. Vi utgår från befintlig höjd och kulör och "
     "kontrollerar först om området har riktlinjer eller planbestämmelser för utformningen."),
    ("Hur bevarar man de smala vindskivorna på en funkisvilla i Näsbypark?",
     "Genom att mäta upp befintlig plåt och bocka ny efter samma mått. En standardprofil blir ofta för "
     "grov för husets lätta takkant."),
    ("Behöver alla parhus i Erikslund byta plåt samtidigt?",
     "Det är inget krav, men om grannarna gör arbetet tillsammans blir profil och kulör lika och "
     "anslutningarna mellan husen görs i samma etapp."),
    ("Är Täbys riktlinjer för takmaterial bindande?",
     "Nej. Kulturmiljöer i Täby är ett kunskapsunderlag med råd, men det används som vägledning, och i "
     "områden med utökad lovplikt eller skyddsbestämmelser krävs lov."),
    ("Var hittar vi äldre ritningar på vår villa i Roslags-Näsby?",
     "Kommunen råder dig att kontakta den för att se om det finns äldre ritningar. De visar ofta takfot "
     "och plåtdetaljer som de var från början."),
  ],
  "sources": [
    ("Täby kommun – Fasadändring",
     "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/fasadandring"),
    _TABY_KMP, _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver plåten på huset i Täby bytas?", "Boka ett gratis platsbesök så går vi igenom takfot, takband och rännor."),
  "img": [
    ("Funkisvilla i Täby med ljus puts, lågt tak och smala plåtvindskivor",
     "1940s Swedish functionalist villa with smooth white render, low-pitched roof hidden behind a thin metal "
     "fascia, slim metal barge boards, large garden with birch trees, Näsbypark Täby, clear day, no people, no text"),
    ("Lågt radhus med brett takband i trä och plåtavtäckning",
     "low single-storey 1960s Swedish terraced houses with completely flat roofs, the roof edge finished with "
     "a broad horizontal band of dark brown painted wooden boards topped by a thin dark metal coping, yellow "
     "brick facades, close view of two houses from the front garden, one storey only, no pitched roofs, empty scene, daylight, "
     "no people, no text"),
  ],
},

# ------------------------------------------------------------------ SOLNA
"platslagare-solna.html": {
  "kind": "district", "service": "platslagare", "ort": "Solna", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Solna – underhåll i skyddade miljöer",
  "description": "Plåtslagare i Solna: plåtarbete som underhåll i stadens kulturmiljöer, lov för "
                 "materialbyte, plåt mot gata på flerbostadshus och ROT-avdrag.",
  "h1": "Plåtslagare i Solna",
  "lead": "I Solna avgör kulturmiljön ofta hur ett plåtarbete får göras. Staden skriver att de lovbefriade "
          "åtgärderna i många fall inte kan användas, eftersom stora delar av Solna är kulturhistoriskt "
          "värdefulla. Geal Entreprenad AB har egna plåtslagare som lagar och byter plåt på villor, radhus "
          "och flerbostadshus i Solna, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Plåt i Solnas kulturmiljöer.",
  "sections": [
    {"id": "kulturmiljo-solna", "anchor": "Solnas miljöer",
     "h2": "Var de lovbefriade åtgärderna inte gäller",
     "paras": [
       "På sidan om bygglovsfria åtgärder räknar Solna stad upp var undantagen från bygglov inte kan "
       "användas. Det gäller i de kulturhistoriskt värdefulla miljöerna i Solnakartan, i riksintressena "
       "Karlberg, Solna kyrkby- och radhusbebyggelse, Ulriksdal och Hagaparken, i nationalstadsparken och i "
       "de sammanhängande miljöer som översiktsplanen pekar ut.",
       "Till de senare hör Råsunda villastad, villabebyggelsen i norra Råsunda, Råsta egnahem, Alnäs och "
       "Stocksundstorp och 1950-talsbebyggelsen i Råsunda. Därtill kommer en- och tvåbostadshus med "
       "varsamhets- eller skyddsbestämmelser i detaljplanen, bland annat kring Sjövägen, i Bergshamra by "
       "och i Stocksundstorp.",
       "För en villaägare i Solna innebär det att frågan om lov behöver ställas tidigare än i många andra "
       "kommuner – och att det lönar sig att skilja på underhåll och ändring redan i offerten.",
     ],
     "aside": {"title": "Exempel på utpekade miljöer", "items": [
       "Råsunda villastad", "Villorna i norra Råsunda", "Råsta egnahem",
       "Alnäs och Stocksundstorp", "Solna kyrkby och radhusen"]}},
    {"id": "underhall", "h2": "Samma material och utförande – det som räknas som underhåll",
     "paras": [
       "Boverket skriver att det inte är en fasadändring att byta fasadbeklädnad eller taktäckningsmaterial "
       "mot samma material och utförande, utan underhåll. För ett plåtarbete i Solna är det en viktig "
       "gräns. Att byta en rostig fotplåt, en sprucken ränndal eller ett skorstensbeslag mot nya delar i "
       "samma utförande ändrar inte husets utseende.",
       "Därför börjar vi med att dokumentera det som finns: profiler, falsarnas typ, kulör och hur "
       "vindskivor och takfot är utformade. Med det som underlag kan plåten bytas utan att husets "
       "karaktärsdrag påverkas, och du har något att visa staden om frågan kommer upp.",
       "Ska taket i stället läggas om eller få nytt material är det en annan sak. Hur vi arbetar med "
       "hela tak i kommunen beskriver vi under "
       + _L.format("takrenovering-solna.html", "takrenovering i Solna") + ".",
     ],
     "aside": None},
    {"id": "materialbyte", "h2": "När plåten ska bytas mot något annat",
     "paras": [
       "På frågan om man får byta tak eller ändra takmaterial utan bygglov svarar Solna stad nej, och "
       "skriver att de flesta områden i staden har en detaljplan. Fastigheter utanför detaljplan har ofta "
       "stora kulturvärden och är skyddade på annat sätt.",
       "Enligt Boverkets vägledning efter den 1 december 2025 krävs inget bygglov för att byta material på "
       "tak eller fasad på ett en- eller tvåbostadshus, om huset inte är särskilt värdefullt, ligger i ett "
       "värdefullt område eller har utökad lovplikt. Eftersom så stora delar av Solna omfattas av "
       "undantagen utgår vi från att ett materialbyte – till exempel från tegel till plåt eller från "
       "plåt till papp – behöver stämmas av med staden innan något beställs.",
       "Vill du ha ett skriftligt besked kan du kontakta stadens kontaktcenter. Mer om lovfrågan vid "
       "takarbeten finns under " + _L.format("bygglov-takbyte.html", "bygglov vid takbyte") + ".",
     ],
     "aside": {"title": "Underhåll eller ändring?", "items": [
       "Ny fotplåt i samma profil: underhåll", "Nytt skorstensbeslag lika det gamla: underhåll",
       "Tegel byts mot plåt: ändring", "Ny kulör på plåttaket: ändring"]}},
    {"id": "flerbostad", "h2": "Plåt mot gata på radhus och flerbostadshus",
     "paras": [
       "För byggnader som inte är en- eller tvåbostadshus gäller andra regler. Enligt Boverket krävs bygglov "
       "för en fasadändring inom detaljplan när den görs på en fasad eller ett tak som vetter mot en allmän "
       "plats, som gata eller park. För en bostadsrättsförening med plåttak eller plåtfasad mot gatan blir "
       "materialvalet därför en lovfråga oavsett kulturmiljö.",
       "Rotavdraget skiljer sig också. Skatteverket räknar inte plåt- och glasarbeten utanför den egna "
       "bostaden som rotarbete för en bostadsrätt, så plåtarbetet på ett flerbostadshus faktureras "
       "föreningen. För dig med villa eller ägt radhus gäller vanligt rotavdrag.",
       "Ett flerbostadshus har dessutom ofta större plåtytor än en villa: fönsterbleck på många våningar, "
       "plåtavtäckningar på brandväggar och takfötter som bara nås med hög ställning eller skylift. Vi går "
       "igenom dem med föreningens förvaltare och delar gärna upp arbetet i etapper. Söker du en lokal firma "
       "för hela taket finns mer under " + _L.format("taklaggare-solna.html", "takläggare i Solna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går plåtarbetet till i Solna",
  "steps": [
    ("Platsbesök", "Vi går igenom plåten på tak, rännor och bleck och noterar vad som är original."),
    ("Kulturmiljö och plan", "Solnakartan och detaljplanen kontrolleras innan vi föreslår material."),
    ("Underhåll eller ändring", "I förslaget skiljer vi på delar som byts i samma utförande och sådant som kräver lov."),
    ("Skriftligt kostnadsförslag", "Varje del redovisas för sig, med rotavdraget där det gäller."),
    ("Utförande", "Plåten bockas efter befintliga profiler och monteras med samma kulör."),
    ("Dokumentation", "Du får en genomgång av vad som har bytts och hur det är utfört."),
  ],
  "rot_h2": "ROT-avdrag för plåtarbete i Solna",
  "rot": [
    "På ett småhus ger det rotavdrag att reparera, rengöra eller byta plåttak, hängrännor och stuprör, enligt "
    "Skatteverket. Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och "
    "högst 75 000 kr tillsammans med rut. Material och resor ger inget avdrag.",
    "Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Solna?",
  "price": [
    "Om plåten kan bytas i samma utförande eller ska tillverkas efter förlaga, hur många detaljer som byts, "
    "hur ställningen kan stå på tomten eller mot gatan och om arbetet kräver underlag för en lovansökan. "
    "Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi byta en rostig fotplåt på vår villa i Råsunda utan lov?",
     "Byts plåten mot samma material och utförande räknas det som underhåll och inte som fasadändring. "
     "Ändras profil eller kulör bör du stämma av med Solna stad först."),
    ("Vad säger Solna stad om att byta takmaterial?",
     "Staden svarar nej på frågan om takmaterial får bytas utan bygglov inom detaljplan, och de flesta "
     "områden i Solna har en detaljplan. Kontakta stadens kontaktcenter för besked om just ditt hus."),
    ("Behöver vår bostadsrättsförening bygglov för ny plåt på taket mot gatan?",
     "Ja, om materialet eller kulören ändras. För andra byggnader än en- och tvåbostadshus krävs lov för "
     "fasadändring inom detaljplan när taket vetter mot allmän plats."),
    ("Får jag rotavdrag för plåtarbete på huset där jag har bostadsrätt?",
     "Nej. Skatteverket räknar inte plåt- och glasarbeten utanför den egna bostaden som rotarbete. "
     "Arbetet beställs i stället av föreningen."),
    ("Gäller Solnas begränsningar även i Bergshamra by?",
     "Ja. Staden nämner en- och tvåbostadshus med varsamhets- eller skyddsbestämmelser i Bergshamra by bland "
     "de byggnader där lovbefriade åtgärder inte kan användas."),
  ],
  "sources": [
    ("Solna stad – Bygglovsfria åtgärder",
     "https://www.solna.se/bygga-bo--miljo/bygga/bygglov/bygglovsfria-atgarder"),
    ("Solna stad – Kulturmiljöer i Solna",
     "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna"),
    _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska plåten på huset i Solna bytas?", "Boka ett gratis platsbesök så reder vi ut vad som är underhåll och vad som kräver lov."),
  "img": [
    ("1920-talsvilla i Solna med tegeltak, plåtbeslag och hängrännor",
     "1920s Swedish plastered villa with red clay tile roof, dark metal chimney flashing, black half-round "
     "gutters and downpipes, on a hilly residential street with lilac and birch, Råsunda Solna, spring, "
     "no people, no text"),
    ("Ny fotplåt och hängränna längs takfoten på ett tegeltak",
     "close-up of the eaves of a Swedish villa roof covered with regular rows of red clay pantiles, clean new "
     "dark grey metal eaves flashing under the lowest tile row and a new half-round gutter on brackets, white "
     "painted wooden fascia board, daylight, no people, no text"),
  ],
},

# ------------------------------------------------------------------ HUDDINGE
"platslagare-huddinge.html": {
  "kind": "district", "service": "platslagare", "ort": "Huddinge", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Huddinge – stuprör, dagvatten och bleck",
  "description": "Plåtslagare i Huddinge: hängrännor och stuprör efter kommunens dagvattenråd, val av "
                 "plåt utan koppar och zink, brutna tegeltak och fasadändring utan lov.",
  "h1": "Plåtslagare i Huddinge",
  "lead": "Huddinge kommun vill att regnvattnet från taken tas om hand på tomten. Det gör hängrännor, "
          "stuprör och utkastare till mer än en detalj – de är början på husets dagvattenhantering. Geal "
          "Entreprenad AB har egna plåtslagare som byter rännor, bleck och beslag i hela Huddinge, med "
          "gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Rännor, dagvatten och brutna tak.",
  "sections": [
    {"id": "dagvatten", "anchor": "Dagvatten i Huddinge",
     "h2": "Kommunens dagvattenstrategi börjar vid stupröret",
     "paras": [
       "I broschyren om dagvatten skriver Huddinge kommun att ambitionen är att ta hand om dagvattnet lokalt "
       "genom att låta regnvattnet infiltrera på tomten. Saknas förutsättningar för det ska flödet i stället "
       "fördröjas inom tomten. Som fastighetsägare ansvarar du för att hanteringen följer detaljplanen och, "
       "där det finns allmänt ledningsnät, VA-huvudmannens bestämmelser.",
       "Kommunen beskriver flera sätt att göra det. Stuprör kan förses med utkastare och ränndalsplattor som "
       "leder vattnet ut på gräsmattan, och vattnet kan samlas i regnvattentunnor. En tunna fylls relativt "
       "snabbt, så den bör ha ett överfyllnadsskydd som leder överskottet vidare till en grönyta.",
       "Vattnet får inte ledas ut på gatan eller till andra fastigheter. Därför planerar vi var stupröret "
       "ska sitta tillsammans med dig, så att det mynnar där marken kan ta emot vattnet.",
     ],
     "aside": {"title": "Kommunens råd i korthet", "items": [
       "Låt vattnet infiltrera på tomten", "Utkastare minst 20 cm", "Mark som lutar 1:20 bort från huset",
       "Inget vatten till gata eller granne"]}},
    {"id": "utkastare", "h2": "Utkastare, marklutning och stänk på fasaden",
     "paras": [
       "Broschyren anger att utkastaren – böjen längst ner på stupröret – bör vara minst 20 centimeter lång "
       "för att undvika vattenstänk på fasaden. Närmast huset bör marken luta minst 1:20, det vill säga "
       "minst 15 centimeter nivåskillnad på en sträcka av minst tre meter från byggnaden.",
       "En kort eller avbruten utkastare syns ofta som fuktfläckar och avflagnad färg nederst på sockeln. "
       "När vi byter stuprör ser vi därför till att röret slutar i rätt höjd och riktning, och vi påpekar "
       "om marken lutar mot huset så att du kan åtgärda det.",
       "Hängrännorna ska ha jämnt fall mot stupröret och sitta så att vattnet från takfoten hamnar i rännan "
       "och inte bakom den. I skogsnära lägen med mycket barr kan lövsilar minska igensättningen. Mer om "
       "rännorna i allmänhet finns på sidan om "
       + _L.format("hangrannor-stupror.html", "hängrännor och stuprör") + ".",
     ],
     "aside": None},
    {"id": "material-huddinge", "h2": "Plåt som inte förorenar dagvattnet",
     "paras": [
       "Kommunen påminner om att dagvatten ofta når närmaste sjö eller vattendrag utan rening, och att "
       "metaller från byggnader är en av föroreningarna. Vid om- och nybyggnad råder den därför villaägare "
       "att välja tak- och fasadmaterial som inte förorenar dagvattnet, och nämner kopparbleck och omålade "
       "zinkytor som exempel att undvika.",
       "För plåtarbetet betyder det att vi i första hand föreslår belagd plåt för rännor, bleck och beslag. "
       "För landsbygden anger kulturmiljöprogrammet att tegeltäckta tak är vanligast, men att plåt och "
       "sedum också kan vara aktuellt i vissa miljöer. Samtidigt skriver kommunen att plåtfasader har "
       "svårare att passa in i landsbygdens bebyggelse.",
       "Ska taket bytas helt hänger materialvalet ihop med resten av taket, se "
       + _L.format("takrenovering-huddinge.html", "takrenovering i Huddinge") + ".",
     ],
     "aside": {"title": "Vid val av plåt", "items": [
       "Belagd plåt framför omålad zink", "Undvik nya kopparbleck", "Samma kulör på ränna och stuprör",
       "Fästdon som passar plåten"]}},
    {"id": "tak-huddinge", "h2": "Brutna tegeltak och frivilligt bygglov",
     "paras": [
       "Kulturmiljöprogrammet beskriver småhusområdena från 1910–40-talet med träpanel, enkelt spröjsade "
       "fönster och sadeltak eller brutna tak täckta med tegel. På 1960–80-talets grupphus varierar "
       "takformerna från kraftigt lutande sadeltak till flacka valmade tak och pulpettak. På ett brutet tak "
       "är knäcken och ränndalarna plåtslagarens viktigaste ställen, och på ett pulpettak är det takfoten "
       "och anslutningen mot väggen.",
       "Huddinge kommun skriver att du inte behöver bygglov för att renovera fasaden eller byta tak om du "
       "byter befintligt material mot samma sorts material med samma färg, och att utseendet på ett en- "
       "eller tvåbostadshus får ändras utan lov om huset eller området inte är kulturhistoriskt värdefullt. "
       "Vill du ha ett skriftligt besked kan du söka frivilligt bygglov.",
       "Mer om oss som lokal firma finns under "
       + _L.format("taklaggare-huddinge.html", "takläggare i Huddinge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi rännor och plåt i Huddinge",
  "steps": [
    ("Besök i regnväder eller torka", "Vi ser var vattnet rinner av taket och var det hamnar på tomten."),
    ("Plan för avvattningen", "Stuprörens placering och utkastare bestäms efter hur marken kan ta emot vattnet."),
    ("Kostnadsförslag", "Rännor, stuprör, bleck och beslag redovisas var för sig i skrift."),
    ("Materialval", "Vi föreslår plåt och kulör efter huset och kommunens råd om dagvatten."),
    ("Montering", "Rännor monteras med fall mot stupröret och utkastare i rätt höjd."),
    ("Kontroll", "Vi går igenom avvattningen med dig och visar var vattnet tar vägen."),
  ],
  "rot_h2": "ROT-avdrag för rännor och plåt i Huddinge",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att reparera, rengöra eller byta hängrännor, stuprör "
    "och plåttak och att byta fönsterbleck. Avdraget är högst 30 procent av arbetskostnaden och högst "
    "50 000 kr per person och år, med 75 000 kr som gemensamt tak för rot och rut.",
    "Regnvattentunnor och ränndalsplattor räknas som material. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset i Huddinge?",
  "price": [
    "Längden på rännor och stuprör, hur många hörn och utkastare som behövs, om bleck och beslag byts "
    "samtidigt och hur ställningen kan stå på en sluttande tomt. Efter ett gratis platsbesök får du ett "
    "skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi leda stuprörets vatten ut mot gatan i Huddinge?",
     "Nej. Kommunen skriver att avledningen inte får ske till gata eller till andra fastigheter, utan att "
     "vattnet i första hand ska infiltrera på den egna tomten."),
    ("Hur lång ska utkastaren vara enligt Huddinge kommun?",
     "Minst 20 centimeter, för att undvika vattenstänk på fasaden. Marken närmast huset bör samtidigt luta "
     "bort från byggnaden."),
    ("Ska vi undvika kopparbleck på vår villa i Huddinge?",
     "Kommunen nämner kopparbleck och omålade zinkytor som material att undvika vid om- och nybyggnad, "
     "eftersom metaller följer med dagvattnet."),
    ("Behövs bygglov för nya plåtrännor i annan kulör på ett radhus i Huddinge?",
     "Utanför kulturhistoriskt värdefulla områden får ett en- eller tvåbostadshus ändras utan lov. Ligger "
     "huset i ett värdefullt område behövs lov, och då kan du också söka frivilligt bygglov för besked."),
    ("Kan stupröret kopplas till en regnvattentunna?",
     "Ja, kommunen nämner tunnan som det enklaste sättet att återanvända dagvatten. Den bör ha lock och ett "
     "överfyllnadsskydd som leder överskottet till en grönyta."),
  ],
  "sources": [_HUD_DAG, _HUD_FASAD, _HUD_KMP, _BV_FASAD, _SKV_LISTA, _SKV_ROT],
  "cta": ("Behöver rännor och stuprör bytas i Huddinge?", "Boka ett gratis platsbesök så planerar vi avvattningen tillsammans."),
  "img": [
    ("Villa i Huddinge med tegeltak, nya hängrännor och stuprör",
     "1920s Swedish wooden villa with a red clay tile gambrel roof, new dark grey half-round gutters and "
     "downpipes, mature garden with pine trees on a sloping lot, Huddinge, summer daylight, no people, no text"),
    ("Stuprör med utkastare som leder vatten till en ränndalsplatta på gräsmattan",
     "a single dark grey round metal downpipe running straight down a wooden house wall ending in one outlet bend about 20 cm above "
     "the ground, rainwater flowing out onto a long concrete splash block lying on the lawn that leads the "
     "water away from the house plinth, grass sloping away from the house, after rain, daylight, no people, no text"),
  ],
},

# ------------------------------------------------------------------ LIDINGÖ
"platslagare-lidingo.html": {
  "kind": "district", "service": "platslagare", "ort": "Lidingö", "svc_label": "Plåtslagare",
  "title": "Plåtslagare på Lidingö – plåt i vind och blå markering",
  "description": "Plåtslagare på Lidingö: plåttak och beslag i utsatta lägen mot fjärdarna, stadens "
                 "utökade lovplikt, byggnadsinventeringar och rotavdrag. Gratis platsbesök.",
  "h1": "Plåtslagare på Lidingö",
  "lead": "På Lidingö tar vinden från fjärdarna i plåten på hus som står högt eller nära vattnet, och flera "
          "områden på ön är utpekade som kulturhistoriskt värdefulla. Geal Entreprenad AB har egna plåtslagare som "
          "lagar och byter plåttak, rännor, bleck och beslag på hela Lidingö, med gratis platsbesök och "
          "skriftligt kostnadsförslag.",
  "card": "Plåt i vind och värdefulla miljöer.",
  "sections": [
    {"id": "vind-lidingo", "anchor": "Plåt på Lidingö",
     "h2": "När vinden tar i takfoten",
     "paras": [
       "Ett hus som står fritt mot vattnet får mer vind och slagregn än ett hus i en skyddad dalgång. Det "
       "märks först på plåten i takets kanter: vindskivor, nockplåt och fotplåt. Är plåten fäst med för få "
       "eller för korta fästdon börjar den röra sig, och då nöts hålen upp tills plåten släpper.",
       "Östersjön är bräckt – SMHI anger 6–9 gram salt per kilo i Egentliga Östersjön mot ungefär 35 gram "
       "i världshaven – men fukt och vind från fjärdarna gör ändå att ytskydd och fästdon slits snabbare på "
       "strandnära tomter. Vi väljer därför plåt och skruv efter läget och kontrollerar infästningen i "
       "kanterna särskilt noga.",
       "Efter en storm är det ofta en enskild vindskiva eller en bit nockplåt som har lossnat. Det kan "
       "åtgärdas separat, men vi ser också över resten av kanten när vi ändå är uppe.",
     ],
     "aside": {"title": "Utsatta delar på ett sjönära tak", "items": [
       "Vindskivor på gaveln", "Nockplåt", "Fotplåt mot förhärskande vind", "Beslag kring skorstenen"]}},
    {"id": "bla-markering", "h2": "Den blå markeringen i stadens karta",
     "paras": [
       "Lidingö stad skriver att det inom områden som är särskilt kulturhistoriskt värdefulla gäller utökad "
       "lovplikt för de flesta byggnadsåtgärder. I stadens webbkarta syns det som ett blått lager, och "
       "klickar du på fastigheten får du veta om den omfattas. Är fastigheten gulmarkerad kan det finnas "
       "värden som behöver bedömas, och då ska du kontakta kundcenter.",
       "Utanför de värdefulla områdena har lättnaderna sedan 1 december 2025 blivit stora. Staden räknar "
       "upp att bygglov för fasadändringar på en- och tvåbostadshus har slopats – målning, byte av fasad- "
       "eller taktäckningsmaterial, takfönster och mer.",
       "För ett plåtarbete betyder det att ett byte till samma material och utförande sällan är någon "
       "lovfråga, medan ett byte från tegel eller skiffer till plåt i ett blått område kräver lov. Mer om "
       "lokala takarbeten finns under " + _L.format("taklaggare-lidingo.html", "takläggare på Lidingö") + ".",
     ],
     "aside": None},
    {"id": "kmp-lidingo", "h2": "Kulturmiljöprogrammet och husets egen historia",
     "paras": [
       "Stadens kulturmiljöprogram antogs av kommunfullmäktige den 16 december 2024. Enligt staden är det "
       "ett kunskapsunderlag och inte juridiskt bindande, men det är ett stöd vid beslut i bygglovs- och "
       "planärenden. Programmet pekar ut och avgränsar värdefulla miljöer, inte varje enskild byggnad.",
       "Staden har också äldre inventeringar av enskilda byggnader, dels från 1970- och 1980-talen, dels "
       "från 2013–2015. Genom att kontakta kundcenter på miljö- och stadsbyggnadskontoret kan du be att få "
       "ta del av de beskrivningar som finns för din fastighet. Där framgår ibland vilka material taket och "
       "plåtdetaljerna hade från början.",
       "Begreppet K-märkt finns inte i juridisk mening, skriver staden. Det som brukar menas är att huset är "
       "byggnadsminne, har skyddsbestämmelser i detaljplan eller är utpekat i kulturmiljöprogrammet. För "
       "de nio byggnadsminnena på ön, bland dem radhusen på Canadastigen, är det länsstyrelsen som prövar "
       "ändringar.",
     ],
     "aside": {"title": "Ta reda på före plåtarbetet", "items": [
       "Blå eller gul markering i kartan?", "Skyddsbestämmelser i detaljplanen?",
       "Finns en äldre byggnadsinventering?", "Är huset byggnadsminne?"]}},
    {"id": "arbete-lidingo", "h2": "Rännor, bleck och beslag på kuperade tomter",
     "paras": [
       "På en kuperad tomt med stödmurar, terrasser eller ett hus i souterräng påverkar terrängen var "
       "ställningen kan stå och hur långa stuprören blir, och på en terrasserad tomt behöver vattnet från "
       "stupröret ledas så att det inte rinner mot nästa mur eller mot grannen.",
       "Fönsterblecken på husets utsatta sidor tar också mycket vatten. Boverket pekar på bleckens lutning, "
       "att blecken sluter tätt mot väggen och en dränerande spalt under blecket som avgörande för att "
       "undvika fuktskador vid fönster. Byter vi bleck gör vi det med uppvik mot karmen och en droppkant som "
       "håller vattnet borta från fasaden.",
       "Ska hela taket läggas om samtidigt beskriver vi arbetsgången under "
       + _L.format("takrenovering-lidingo.html", "takrenovering på Lidingö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtarbete till på Lidingö",
  "steps": [
    ("Besök på tomten", "Vi går igenom takets kanter, rännor, bleck och beslag och hur ställningen kan stå."),
    ("Karta och inventering", "Blå eller gul markering och eventuella byggnadsinventeringar kontrolleras."),
    ("Kostnadsförslag", "Lagning, delbyte och nytt utförande redovisas var för sig i skrift."),
    ("Plåt och fästdon", "Material, ytskydd och skruv väljs efter hur utsatt huset står."),
    ("Montering", "Kanterna fästs extra noga och bleck bockas efter fönster och fasad."),
    ("Genomgång", "Vi går igenom arbetet med dig och rensar rännorna innan vi lämnar."),
  ],
  "rot_h2": "Rotavdrag för plåtarbeten på Lidingö",
  "rot": [
    "Skatteverket godkänner rotavdrag i småhus för att reparera, rengöra eller byta plåttak, hängrännor och "
    "stuprör och för att byta fönsterbleck, liksom för ställningen som behövs. Avdraget är högst 30 procent "
    "av arbetskostnaden, 50 000 kr per person och år och 75 000 kr sammanlagt för rot och rut.",
    "Material och resor ger inget avdrag. Avdraget görs direkt på fakturan.",
  ],
  "price_h2": "Det här påverkar priset på Lidingö",
  "price": [
    "Hur mycket plåt som byts, om husets läge kräver kraftigare fästdon och ytskydd, hur många bleck och "
    "beslag som görs om och hur svår tomten är att ställa ställning på. Efter ett gratis platsbesök får du "
    "ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vindskivan blåste loss i stormen – kan bara den bytas?",
     "Ja, en enskild vindskiva eller nockplåt kan bytas separat. Vi kontrollerar samtidigt infästningen längs "
     "resten av kanten, eftersom den ofta har samma ålder."),
    ("Vad betyder blått lager i Lidingös webbkarta?",
     "Att fastigheten omfattas av utökad lovplikt. Då krävs bygglov för bland annat fasadändring, som att "
     "byta till ett annat takmaterial."),
    ("Kan vi få veta vilket material taket hade från början?",
     "Lidingö stad har byggnadsinventeringar från 1970–80-talen och 2013–2015. Kontakta kundcenter på miljö- "
     "och stadsbyggnadskontoret och be att få ta del av det som finns för fastigheten."),
    ("Är vårt hus K-märkt om det ingår i kulturmiljöprogrammet?",
     "K-märkt finns inte som juridiskt begrepp. Programmet är ett kunskapsunderlag, men det används vid "
     "bygglov, och skyddsbestämmelser i detaljplan är bindande."),
    ("Behöver plåten på ett sjönära hus på Lidingö andra fästdon?",
     "Ofta ja. Vind och fukt från fjärdarna sliter på ytskydd och infästning, så vi väljer fästdon och plåt "
     "efter läget och kontrollerar kanterna extra noga."),
  ],
  "sources": [
    ("Lidingö stad – Ändrade lagar och regler för byggande",
     "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/"),
    ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet",
     "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/"),
    _SMHI, _BV_FASAD, _BV_FONST, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver plåten på huset på Lidingö ses över?", "Boka ett gratis platsbesök så går vi igenom takets kanter, rännor och bleck."),
  "img": [
    ("Villa på en höjd på Lidingö med mörkt plåttak och utsikt mot fjärden",
     "early 1900s Swedish wooden villa painted white on a rocky hill with pines, dark grey standing-seam metal "
     "roof with metal barge boards and ridge flashing, glimpse of the sea between the trees, Lidingö "
     "Stockholm, windy autumn day, no people, no text"),
    ("Gavel med ny vindskiva och nockplåt i plåt på ett tak",
     "close-up of a house gable with new dark metal barge board flashing and ridge cap on a clay tile roof, "
     "visible screw fixings, blue sky with clouds, no people, no text"),
  ],
},
}
