# -*- coding: utf-8 -*-
"""Golvslipning – ortsidor v31: Botkyrka, Sigtuna, Skärholmen (2026-10-27).
Hubb: golvlaggning.html (deltjänst, TJ_SERVICES["golvslipning"]). Intent: slipa och ytbehandla befintliga trägolv – skild
från golvlaggare-<ort>.html (nya golv), som länkas där den finns. Tre bilder per sida: img[0] hero 4:3, img[1]–img[2] 3:2.

Lokal vinkel per sida:
Botkyrka – kulturmiljöprogrammet om Tullinge (station 1903, Hamra egnahem på 1920-talet, kataloghusen och Boros villa
  Björkhamra, funkisvillor 1930–40, Folkvillan och Tjänstemannavillan på 1950-talet) och Fittja (cirka 2 500 bostäder
  i början av 1970-talet); spikar i gamla golv (Byggnadsvårdsföreningen, SLIP 22: gnistor och dammexplosion).
Sigtuna – bevarande- och förnyelseplanen för Sigtuna stad 2019 (trähus upp mot nästan 300 år, ungefär 60 detaljplaner,
  q-bestämmelser som kan omfatta interiör, material och teknik), kommunens sida om att bygga i kulturmiljö (bevara
  ursprungliga material), breda plankgolv och springor (Byggnadsvårdsföreningen).
Skärholmen – områdesfakta 2025 (bostadsrätter i flerbostadshus i Skärholmen, Sätra, Bredäng och Vårberg), Varsam om
  Bredäng 1962 och Sätra, parkett från 1960-talet som lamellträ med slitskikt på plywood (Byggnadsvårdsföreningen),
  SLIP 22 om stavsläpp och slitskikt, Arbetsmiljöverket om prov på golvmatta och svartlim.

Fakta endast från källorna i respektive 'sources', öppnade med curl (webbläsar-UA) 2026-10-27, alla svarade 200; pdf:erna
har textlager. SLIP 22: undergolv utan svikt, kontroll av slitskikt med kniv i en springa, slitskikt under 1 mm och
EB-härdade golv går inte att slipa, RF 30–60 % och fuktkvot 6–10 % vid ytbehandling, spikar bort, korn 36–50, 60–80,
100 (barrträ) och 120 (lövträ), P3-skydd, damm från ek och bok cancerframkallande, självantändning.
Strukna / ej använda: vilka golv enskilda hus i orterna har, antal slipningar per golvtyp, SCB-siffror, priser.
Inga garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_BV = "https://byggnadsvard.se/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


def _sbf(titel, slug):
    return (f"Svenska Byggnadsvårdsföreningen – {titel}", _BV + slug + "/")


_GBR = ("Golvbranschen – Branschriktlinjer SLIP 22, slipning av trägolv (pdf)",
        "https://www.golvbranschen.se/siteassets/dokument/branschriktlinjer/branschriktlinjer---slipning-av-tragolv---slip-22.pdf")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_BOT_KMP = ("Botkyrka kommun – Kulturmiljöprogram, antaget 2014 (pdf)",
            "https://www.botkyrka.se/download/18.1fbbaae6170bff9469deb7f/1602575505534/Kulturmilj%C3%B6program.pdf")
_SIG_BEV = ("Sigtuna kommun – Bevarande- och förnyelseplan för Sigtuna stad, antagen 2019 (pdf)",
            "https://www.sigtuna.se/download/18.6ed4dd301706254f993282/1582201854957/Bevarande-%20och%20f%C3%B6rnyelseplan%20f%C3%B6r%20Sigtuna%20stad,%20antagen%202019.pdf")
_SIG_KULT = ("Sigtuna kommun – Bygga i kulturmiljö",
             "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html")
_AV_ASB = ("Arbetsmiljöverket – Förebygg riskerna med asbest",
           "https://www.av.se/halsa-och-sakerhet/kemiska-risker/risker-for-vissa-amnen-produkter-och-verksamheter/asbest/forebygg-riskerna-med-asbest/")
_SKV_SA = ("Skatteverket – Så fungerar rotavdraget",
           "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SBF_TRAGOLV = _sbf("Trägolv", "tragolv")
_SBF_SPRING = _sbf("Breda golvspringor", "breda-golvspringor")
_SBF_ATERST = _sbf("Återställa parkettgolv", "aterstalla-parkettgolv")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor "
            "ger inget avdrag, och Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ BOTKYRKA
"golvslipning-botkyrka.html": {
  "kind": "district", "service": "golvslipning", "ort": "Botkyrka", "svc_label": "Golvslipning",
  "title": "Golvslipning i Botkyrka – kataloghus och funkisvillor",
  "description": "Golvslipning i Botkyrka: furugolv i Tullinges kataloghus från 1920-talet, spikar under gamla mattor, slitskiktet i lägenheternas golv och rotavdrag.",
  "h1": "Golvslipning i Botkyrka",
  "lead": "Villorna i Tullinge byggdes under hela 1900-talets första hälft, från kataloghus på 1920-talet till funkisvillor och folkhemmets typhus. Under gamla mattor och masonit ligger ofta trägolv som går att slipa fram igen. Geal Entreprenad AB slipar och behandlar golv i villor, radhus och lägenheter i Botkyrka.",
  "card": "Furugolv och parkett i villorna.",
  "sections": [
    {"id": "tullinge-botkyrka", "anchor": "Tullinge",
     "h2": "Tullinges villor från 1900-talets första hälft",
     "paras": [
       "Botkyrkas kulturmiljöprogram berättar att AB Separator anlade ett gjuteri vid Tullingesjöns sydspets kring sekelskiftet och att Tullinge järnvägsstation öppnade 1903. Det blev starten för villasamhället. På 1920-talet planlades egnahemsområdet Hamra egnahem söder om järnvägen för tjänstemän och arbetare på Separator, medan villaområdena norr om järnvägen, Tullinge Parkhem och Norra Tullinge Lanthem, byggdes ut vidare.",
       "Under 1920-talet kom kataloghusen, monteringsfärdiga enfamiljshus som köptes direkt från en husleverantör. Boros villa Björkhamra blev populär i Tullinges egnahemsområde och finns väl representerad söder om järnvägen. På 1930- och 40-talen dominerade funkisvillan, och på 1950-talet lanserades Folkvillan och Tjänstemannavillan.",
     ],
     "aside": {"title": "Tullinge i kulturmiljöprogrammet", "items": [
       "Järnvägsstationen öppnade 1903", "Hamra egnahem på 1920-talet", "Kataloghus, bland annat Björkhamra", "Funkis och Folkvillan"]}},
    {"id": "spik-botkyrka", "h2": "Spikar under mattan",
     "paras": [
       "Byggnadsvårdsföreningen svarar i en fråga om en villa från 1920 där en linoleummatta från 1943 togs bort och mörkfernissade trägolv kom fram, med breda tiljor i hallen och smalare brädor i övriga rum. Vissa golv var spikade med mängder av spik, och föreningens förklaring var att golvet förmodligen täckts med masonit och linoleum, därav alla spikar.",
       "Golvbranschens riktlinjer SLIP 22 säger att spikar ska tas bort före slipningen. De kan förstöra slippappret och orsaka gnistor med risk för dammexplosion i slipdammpåsen. Vi drar därför alla spikar och sänker de spikhuvuden som håller brädorna innan maskinen startas. Är golvet för skadat för att slipas finns " + _L.format("golvlaggare-botkyrka.html", "golvläggare i Botkyrka") + ".",
     ],
     "aside": {"title": "Före slipning enligt SLIP 22", "items": [
       "Spikar tas bort", "Lösa partier limmas ner", "Slitskiktet kontrolleras", "Undergolvet ska inte svikta"]}},
    {"id": "fittja-botkyrka", "h2": "Lägenheterna i Fittja och Alby",
     "paras": [
       "Kulturmiljöprogrammet beskriver Fittja som en väl bevarad tunnelbanestadsdel från tidigt 1970-tal. Där uppfördes cirka 2 500 bostäder i början av 1970-talet, både i höghus, låghus och radhus. Programmet lyfter fram de höga punkthusen i 11–12 våningar som ett utmärkande drag.",
       "Golvet i en lägenhet kan vara massivt trä, parkett eller ett lamellgolv, och skillnaden syns inte självklart ovanifrån. SLIP 22 påminner om att golv med ett slitskikt tunnare än 1 millimeter, laminat och fabrikslackerade golv som är EB-härdade inte går att slipa, även om de liknar ett trägolv. Vi kontrollerar därför slitskiktet med en kniv i en springa i ett hörn innan vi lämnar förslag.",
     ],
     "aside": None},
    {"id": "furu-botkyrka", "h2": "Furu eller ek",
     "paras": [
       "Slutslipningen ska enligt SLIP 22 motsvara bandmaskin med korn 100 för barrträ, som furu, och korn 120 för lövträ, som ek och björk. Mönster som fiskben slipas först diagonalt och sedan i rummets längdriktning. Riktlinjerna påpekar också att damm från ek och bok är cancerframkallande, och slipningen görs därför med dammavskiljare och andningsskydd av klass P3.",
       "Före ytbehandlingen mäter vi fukten. Golvet ska inte behandlas när den relativa fuktigheten inomhus ligger utanför 30–60 procent eller när fuktkvoten i träet ligger utanför 6–10 procent. Ett furugolv i ett kataloghus kan få lut, såpa, olja eller lack, beroende på hur huset används. Mer om tjänsten finns under " + _L.format("golvlaggning.html", "golvläggning och golvslipning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så slipar vi golv i Botkyrka",
  "steps": [
    ("Platsbesök", "Gratis besök där vi kontrollerar golv och slitskikt."),
    ("Förberedelse", "Spikar dras, lösa delar limmas, lister lossas."),
    ("Grovslipning", "Korn 36–50 tar bort gammal yta."),
    ("Mellanslipning", "Korn 60–80 tar bort sliprepor."),
    ("Finslipning", "Kanter och yta får samma struktur."),
    ("Ytbehandling", "Lut, såpa, olja eller lack efter fuktmätning."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i Botkyrka",
  "rot": [
    "Skatteverket räknar det som rotarbete att slipa och byta golv i ett småhus. I en bostadsrätt gäller avdraget när arbetet görs innanför lägenhetens tak, väggar och golv och golvet är ditt ansvar enligt stadgarna. Är bostaden yngre än fem år får arbetet bara återställa det ursprungliga skicket.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för golvslipningen i Botkyrka?",
  "price": [
    "Golvytan, hur många spikar och gamla limrester som ska bort, om lösa brädor eller stavar måste limmas, träslag och mönster och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför är det så mycket spik i det gamla trägolvet i min villa i Tullinge?",
     "Byggnadsvårdsföreningen förklarar att golv ofta täcktes med masonit och linoleum, som spikades fast. Spikarna måste bort före slipningen."),
    ("Går det att slipa lamellgolvet i min lägenhet i Fittja?",
     "Det beror på slitskiktet. Golv med slitskikt under 1 millimeter och EB-härdade fabrikslackerade golv går inte att slipa."),
    ("Vilken luftfuktighet behövs för att lacka ett nyslipat golv?",
     "Enligt Golvbranschens SLIP 22 ska den relativa fuktigheten ligga mellan 30 och 60 procent och fuktkvoten i träet mellan 6 och 10 procent."),
    ("Vad är ett kataloghus i Tullinge?",
     "Ett monteringsfärdigt enfamiljshus som köptes från en husleverantör. Boros villa Björkhamra är ett exempel som finns söder om järnvägen."),
  ],
  "sources": [_BOT_KMP, _SBF_TRAGOLV, _GBR, _SKV],
  "cta": ("Ska golven i Botkyrka slipas?", "Boka ett gratis platsbesök, så kontrollerar vi golvet och slitskiktet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat furugolv i ett rum i en äldre villa",
     "freshly sanded and oiled wide pine plank floor in an empty room of a 1920s Swedish wooden villa, white painted panelled walls, tall window with light falling across the boards, summer daylight" + _SFX),
    ("Gammalt trägolv med spikhål efter en borttagen matta",
     "close view of an old dark varnished pine floor with many small nail holes and scattered old nails in rows, after linoleum and hardboard were removed, a claw hammer lying on the boards, daylight" + _SFX),
    ("Golvslipmaskin på ett delvis slipat golv",
     "drum floor sanding machine standing on a partly sanded wooden floor in an empty room, the sanded half pale and the unsanded half darker, dust extraction hose attached, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SIGTUNA
"golvslipning-sigtuna.html": {
  "kind": "district", "service": "golvslipning", "ort": "Sigtuna", "svc_label": "Golvslipning",
  "title": "Golvslipning i Sigtuna – gamla plankgolv i trähusen",
  "description": "Golvslipning i Sigtuna: breda plankgolv i stadens äldre trähus, när detaljplanen skyddar interiören, springor mellan plankorna och rotavdrag.",
  "h1": "Golvslipning i Sigtuna",
  "lead": "I Sigtuna stad finns trähus som är nästan 300 år gamla, och i en del av dem ligger breda plankgolv av furu. Ett sådant golv slipas varsamt, så att inte mer trä än nödvändigt tas bort. Geal Entreprenad AB slipar och behandlar golv i Sigtuna stad, Märsta och kommunens övriga orter.",
  "card": "Plankgolv i äldre trähus.",
  "sections": [
    {"id": "trahus-sigtuna", "anchor": "Trähusen",
     "h2": "Den småskaliga trähusbebyggelsen",
     "paras": [
       "Sigtuna kommuns bevarande- och förnyelseplan för Sigtuna stad, antagen 2019, beskriver den småskaliga trähusbebyggelsen i den centrala staden och på Malmen som ett av stadens starkaste karaktärsdrag. Husen uppfördes före andra halvan av 1800-talet, i huvudsak i timmer med rödfärgad eller oljemålad panel och tegeltak. Kvartersindelningen har på sina håll en hävd på över tusen år, och trots åtskilliga stadsbränder har flera kvarter trähus som är upp mot nästan 300 år gamla.",
       "I sådana hus kan golven vara lika gamla som stommen, eller ha lagts om flera gånger. Vi börjar därför med att ta reda på vad som ligger där: breda plank, smalare brädor eller ett senare golv ovanpå ett äldre. Det avgör hur hårt golvet kan slipas.",
     ],
     "aside": {"title": "Sigtuna stad i planen", "items": [
       "Antagen 2019", "Trähus upp mot nästan 300 år", "Timmer med panel och tegeltak", "Ungefär 60 detaljplaner"]}},
    {"id": "skydd-sigtuna", "h2": "När detaljplanen skyddar interiören",
     "paras": [
       "Planen berättar att det finns ungefär 60 gällande detaljplaner inom området. Kulturvärden kan skyddas med skydds- och varsamhetsbestämmelser. En skyddsbestämmelse, betecknad q, kan enligt planen omfatta både exteriör och interiör och gälla utformning, material, teknik och underhåll, och ibland föreskrivs vissa arbetstekniker.",
       "Sigtuna kommun skriver att ursprungliga material och detaljer om möjligt ska bevaras eller ersättas med samma material om de behöver bytas ut. För ett skyddat golv betyder det att vi slipar så lite som möjligt och väljer en ytbehandling som passar huset. Är du osäker på om huset ligger i ett kulturhistoriskt särskilt värdefullt område kan kommunen bedöma det utifrån bilder på hur huset ser ut i dag.",
     ],
     "aside": {"title": "Skydd i detaljplanen", "items": [
       "q kan omfatta interiör", "Material och teknik", "Vissa arbetstekniker kan föreskrivas", "Kommunen bedömer utifrån bilder"]}},
    {"id": "springor-sigtuna", "h2": "Breda plank och springor",
     "paras": [
       "Byggnadsvårdsföreningen svarar i en fråga om ett furugolv med runt 25 centimeter breda plank i ett sommarhus från omkring 1900, där springorna var upp till 5 millimeter. Föreningen påpekar att plankorna i regel har en kraftig not och spont som är djupare än springan, att golvet rör sig och att plankorna torkar ihop i ett torrt inomhusklimat. Springorna kan fyllas, men det blir sällan vackert; snyggast är enligt svaret om man kan plocka upp plankorna.",
       "Vi slipar därför inte bort springorna, utan bedömer om golvet ska läggas om innan det slipas. Att ta upp plankorna, rengöra noten och lägga dem tätare igen är mer arbete än en slipning, men det gör att golvet behåller sitt material. Ska golvet ersättas helt finns " + _L.format("golvlaggare-sigtuna.html", "golvläggare i Sigtuna") + ".",
     ],
     "aside": None},
    {"id": "ytbehandling-sigtuna", "h2": "Rätt yta och rätt fukt",
     "paras": [
       "Golvbranschens riktlinjer SLIP 22 säger att golvet inte ska ytbehandlas när den relativa fuktigheten inomhus ligger utanför 30–60 procent, eftersom variationerna kan ge sprickor i spacklade fogar. I ett äldre trähus som inte värms upp hela året kan fukten variera mycket, och då väntar vi med ytbehandlingen tills värdena är rätt.",
       "Slutslipningen av furu görs med korn 100. Riktlinjerna varnar också för självantändning: slipdamm som blandats med lack eller olja är brandfarligt, och dammpåsen töms och förvaras utomhus. Mer om tjänsten finns under " + _L.format("golvlaggning.html", "golvläggning och golvslipning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så slipar vi golv i Sigtuna",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på golv och detaljplan."),
    ("Bedömning", "Slipa, lägga om eller laga plankorna."),
    ("Förberedelse", "Spikar bort, lösa plank fästs."),
    ("Slipning", "Så lite trä som möjligt tas bort."),
    ("Fuktmätning", "Rätt luftfuktighet före behandling."),
    ("Ytbehandling", "Såpa, olja eller lack efter husets behov."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i Sigtuna",
  "rot": [
    "Skatteverket räknar slipning av golv i ett småhus som rotarbete, och avdraget gäller även ett fritidshus som du äger och kan använda. I en bostadsrätt gäller avdraget arbete innanför lägenhetens väggar, tak och golv som du ansvarar för enligt stadgarna.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för golvslipningen i Sigtuna?",
  "price": [
    "Golvytan, om plankorna måste läggas om eller fästas, springor och lagningar, hur mycket gammal färg eller fernissa som sitter på och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan detaljplanen skydda golvet i ett gammalt trähus i Sigtuna stad?",
     "Ja. Enligt bevarande- och förnyelseplanen kan en skyddsbestämmelse, q, omfatta både exteriör och interiör och gälla material och teknik."),
    ("Ska breda springor i ett gammalt plankgolv fyllas innan det slipas?",
     "Byggnadsvårdsföreningen skriver att fyllning sällan blir vackert och att det snyggaste är om plankorna kan plockas upp."),
    ("Hur gamla är de äldsta trähusen i Sigtuna stad?",
     "Bevarande- och förnyelseplanen nämner trähus som är upp mot nästan 300 år gamla."),
    ("Varför ska dammpåsen tömmas utomhus efter golvslipningen?",
     "Slipdamm som blandats med lack eller olja kan självantända. Golvbranschen anger att påsen ska tömmas och förvaras utomhus."),
  ],
  "sources": [_SIG_BEV, _SIG_KULT, _SBF_SPRING, _GBR, _SKV, _SKV_SA],
  "cta": ("Ska golven i Sigtuna slipas?", "Boka ett gratis platsbesök, så bedömer vi golvet och detaljplanen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Breda furuplank i ett gammalt timmerhus",
     "wide old pine floor planks freshly sanded and soaped in a low-ceilinged room of an 18th century Swedish timber house, small-paned window, white plastered log wall, soft daylight" + _SFX),
    ("Springa mellan två gamla golvplankor",
     "close view of a narrow gap between two wide old pine floor planks, worn tongue edge visible, warm patina on the wood, daylight from the side" + _SFX),
    ("Röda trähus längs en smal gata",
     "row of small old red-painted timber houses with white trims and clay tile roofs along a narrow cobbled main street in a historic Swedish lakeside town, no people, summer daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"golvslipning-skarholmen.html": {
  "kind": "district", "service": "golvslipning", "ort": "Skärholmen", "svc_label": "Golvslipning",
  "title": "Golvslipning i Skärholmen – parkett i 1960-talshusen",
  "description": "Golvslipning i Skärholmen: parkett och lamellgolv i lägenheter från 1960-talet, slitskikt och stavsläpp, gamla mattor och rotavdrag.",
  "h1": "Golvslipning i Skärholmen",
  "lead": "Bredäng, Sätra, Vårberg och Skärholmen byggdes på 1960- och 70-talen, och i många lägenheter ligger fortfarande golven från byggåret, ibland under en senare matta. Geal Entreprenad AB slipar parkett och trägolv i lägenheter och radhus i Skärholmens stadsdelsområde och kontrollerar först att golvet tål det.",
  "card": "Parkett och lamellgolv från 1960-talet.",
  "sections": [
    {"id": "stadsdelen-skarholmen", "anchor": "Stadsdelarna",
     "h2": "Stadsdelar från miljonprogrammets tid",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden berättar att Bredäng var den första stadsdelen som planerades i stor skala och att bygget började 1962, följt av Sätra. Från 1965 intensifierades bostadsbyggandet i hela landet med målet om en miljon nya lägenheter till och med 1974. Det industrialiserade byggandet fick sitt genombrott i början av 1960-talet. Vägledningen beskriver stadsdelarnas grupper av skivhus i sex till tio våningar, lamellhus i tre till fyra våningar och småhusområden i utkanterna.",
       "Stadens områdesfakta för 2025 visar att lägenheterna i flerbostadshus till stor del är hyresrätter, men att det också finns många bostadsrätter: 960 i Skärholmen, 959 i Sätra, 718 i Bredäng och 678 i Vårberg. Till det kommer nästan 2 000 småhus i stadsdelsområdet, de flesta radhus och kedjehus med äganderätt.",
     ],
     "aside": {"title": "Bostadsrätter i flerbostadshus 2025", "items": [
       "Skärholmen: 960", "Sätra: 959", "Bredäng: 718", "Vårberg: 678"]}},
    {"id": "lamell-skarholmen", "h2": "Parkett som egentligen är lamellträ",
     "paras": [
       "Byggnadsvårdsföreningen svarar i en fråga om en bostadsrätt från 1961 med parkett i original. Föreningen bedömer att golvet sannolikt inte är massiva parkettstavar utan lamellträ, alltså ett slitskikt i holländskt mönster limmat på två meter långa, spontade plywoodbrädor. Slitskiktet är normalt 4 millimeter och går att slipa någon gång.",
       "Golvbranschens riktlinjer SLIP 22 säger att det vid slipning av lamellkonstruktioner finns en generell risk för stavsläpp, alltså att slitskiktet lossnar, och att golventreprenören ska upplysa kunden om det. Vid misstanke om stavsläpp, till exempel efter en vattenskada, bör man avråda från omslipning. Vi kontrollerar slitskiktet med en kniv i en springa i ett hörn och berättar vad vi ser innan något bestäms.",
     ],
     "aside": {"title": "Golv från 1960-talet", "items": [
       "Ofta lamellträ, inte massiv parkett", "Slitskikt normalt 4 mm", "Risk för stavsläpp", "Kontroll med kniv i ett hörn"]}},
    {"id": "mattor-skarholmen", "h2": "Gamla mattor och svart lim",
     "paras": [
       "Ibland har parketten täckts med en plastmatta. Arbetsmiljöverket skriver att man ska göra en asbestanalys om det finns minsta tvekan om ett material innehåller asbest. Provet på en golvmatta ska tas ända ner till undergolvet så att alla lager kommer med, och finns det svartlim ska det också analyseras. Efter provtagningen torkas platsen ren och försluts med tjock grundfärg, primer eller tejp.",
       "Rivning av asbesthaltigt material får enligt Arbetsmiljöverket bara göras av företag som har tillstånd. Visar provet asbest tas mattan därför bort av ett sådant företag innan vi slipar. Är provet fritt tar vi bort mattan och limresterna och bedömer om golvet under går att slipa eller om det behöver ersättas.",
     ],
     "aside": None},
    {"id": "foreningen-skarholmen", "h2": "Föreningen, grannarna och dammet",
     "paras": [
       "I en bostadsrätt avgör stadgarna vem som ansvarar för golvet. Slipningen bullrar och dammar, och Golvbranschens riktlinjer kräver dammavskiljare med HEPA-filter och andningsskydd av klass P3 eftersom damm från bland annat ek och bok är cancerframkallande. Vi stänger av rummet, skyddar ventilationsdonen och informerar grannarna om tiderna.",
       "Grovslipningen görs med högt valstryck och korn 36–50, mellanslipningen med korn 60–80 och finslipningen med lägsta möjliga valstryck. Ett holländskt mönster slipas först diagonalt och sedan i rummets längdriktning. Före lackningen mäter vi luftfuktigheten, som enligt riktlinjerna ska ligga mellan 30 och 60 procent. Är golvet för tunt för att slipas finns " + _L.format("golvlaggning.html", "golvläggning") + " som alternativ.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så slipar vi golv i Skärholmen",
  "steps": [
    ("Platsbesök", "Gratis besök, kontroll av slitskikt och matta."),
    ("Asbestprov", "Vid gamla mattor och svart lim."),
    ("Förberedelse", "Lösa stavar limmas, rummet skärmas av."),
    ("Slipning", "Diagonalt först i mönstrade golv."),
    ("Fuktmätning", "Relativ fuktighet och fuktkvot kontrolleras."),
    ("Ytbehandling", "Lack eller olja efter golvtyp."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i Skärholmen",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete både i småhus och i bostadsrätter. I en bostadsrätt ska arbetet göras innanför lägenhetens tak, väggar och golv och gälla något du ansvarar för enligt föreningens stadgar.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för golvslipningen i Skärholmen?",
  "price": [
    "Golvytan och antalet rum, om en gammal matta och lim ska bort, eventuell asbestanalys, lösa stavar som ska limmas, mönster och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Är parketten i min lägenhet från 1960-talet i Sätra massiv?",
     "Inte säkert. Byggnadsvårdsföreningen beskriver golv från tiden som lamellträ med ett slitskikt på cirka 4 millimeter limmat på plywood."),
    ("Vad är stavsläpp vid golvslipning?",
     "Att slitskiktet på ett lamellgolv lossnar vid eller efter slipningen. Golvbranschen kräver att kunden informeras om risken."),
    ("Måste en gammal golvmatta i Bredäng testas för asbest innan den rivs?",
     "Arbetsmiljöverket säger att prov ska tas vid minsta tvekan, ända ner till undergolvet, och att svartlim också ska analyseras."),
    ("Får jag rotavdrag för golvslipning i min bostadsrätt i Vårberg?",
     "Ja, om golvet är ditt ansvar enligt stadgarna och arbetet görs innanför lägenhetens tak, väggar och golv."),
  ],
  "sources": [_VARSAM, _of("Skärholmen", "soderort/skarholmen/skarholmen"), _of("Sätra", "soderort/skarholmen/satra"),
              _of("Bredäng", "soderort/skarholmen/bredang"), _of("Vårberg", "soderort/skarholmen/varberg"),
              _SBF_ATERST, _GBR, _AV_ASB, _SKV],
  "cta": ("Ska parketten i Skärholmen slipas?", "Boka ett gratis platsbesök, så kontrollerar vi slitskiktet och eventuella mattor innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipad parkett i holländskt mönster i en 1960-talslägenhet",
     "freshly sanded and lacquered oak parquet floor in a Dutch pattern in an empty 1960s Swedish apartment living room, large window, white walls, radiator under the window, daylight" + _SFX),
    ("Hörn av ett parkettgolv där slitskiktet syns i en springa",
     "close view of the corner of an old parquet floor with a thin wear layer visible at a small gap next to the skirting board, a utility knife lying on the floor, daylight" + _SFX),
    ("Flerbostadshus från 1960-talet i en förort",
     "1960s Swedish suburban apartment blocks in light brick with long balconies, lawns and young trees in front, footpath, overcast sky, no people" + _SFX),
  ],
},
}
