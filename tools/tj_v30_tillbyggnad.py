# -*- coding: utf-8 -*-
"""Tillbyggnad – ortsidor v30: Farsta, Spånga, Vällingby, Skärholmen (2026-10-27).
Hubb: tillbyggnad.html (TJ_HUB["tillbyggnad"]). Struktur som tj_v26_tillbyggnad.py. Tre bilder per sida.

Lokal vinkel per sida:
Farsta – småstugeområdena (Tallkrogen, Svedmyra, Sköndal): bygg mot trädgården, håll siktvyerna öppna, lägre nock
  och samma takfot (Varsam); kulturhistoriskt värdefull miljö = lov; tidigare lovfria tillbyggnader räknas in.
Spånga – villastäderna Solhem, Bromsten, Flysta och Sundby: stora tomter, Solhems tiondel, lovfri tillbyggnad får
  strida mot detaljplanen (en- och tvåbostadshus) men inte i värdefull miljö; mot gatan bara när huset står fritt.
Vällingby – radhus och kedjehus i riksintresset Vällingby–Råcksta: uterum, skärmtak, takkupor och balkonger som
  tillbyggnad, riksintresse = lov, bostadsrättsradhus och föreningen, suterränghusen.
Skärholmen – storskalig stadsdel (Bredäng 1962, Sätra): "som regel inget utrymme", skärmtak, uterum eller bod mot
  trädgården, volym efter kvarteret, platta tak och pulpettak; 4,5 meter till gräns på små tomter.

Fakta endast från källorna i respektive 'sources', öppnade med curl (Mozilla-UA) 2026-10-27, alla svarade 200; pdf:erna
har textlager. Skatteverket återställde anslutningen härifrån – samma URL och ROT-formulering som v26.
Strukna: avgifter, handläggningstider, enskilda hus- och kvartersnamn som inte står i källorna. Inga priser, garantier,
omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_STH_TB = ("Stockholms stad – Tillbyggnad (bygglovsbefriad)",
           "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/tillbyggnad-bygglovsbefriad/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_BV_TB = ("Boverket – Göra en tillbyggnad",
          "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/gora-en-tillbyggnad/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_RIKS = ("Stockholms stad – Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_PLAN = ("Stockholms stad – Ändra planlösningen i en byggnad",
         "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/andra-planlosningen-i-en-byggnad/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")

_ROT1 = ("Rotavdraget gäller arbetskostnaden, inte material. Skatteverket räknar en tillbyggnad av ett bostadshus som "
         "rotarbete om någon av dess sidor sitter ihop med husets yttervägg till minst 75 procent eller om en dörr "
         "förbinder de två delarna.")
_ROT2 = ("Bostaden ska vara äldre än fem år och större delen av den ursprungliga stommen ska behållas. Där avdraget "
         "gäller drar Geal det direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ FARSTA
"tillbyggnad-farsta.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Farsta", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Farsta – småstugan och trädgårdssidan",
  "description": "Tillbyggnad i Farsta: småstugeområdena i Tallkrogen, Svedmyra och Sköndal, bygga mot trädgården, "
                 "lägre nock och samma takfot, och de 30 kvadratmetrarna.",
  "h1": "Tillbyggnad i Farsta",
  "lead": "I Farsta står tusentals småhus, många av dem små stugor i Tallkrogen, Svedmyra och Sköndal som har vuxit "
          "med familjerna. Geal Entreprenad AB ritar och bygger tillbyggnader som följer stadens vägledning för "
          "småstugeområdena och tar hand om lov eller anmälan.",
  "card": "Småstugorna och trädgårdssidan.",
  "sections": [
    {"id": "smahusen-farsta", "anchor": "Småhusen",
     "h2": "Småhusen i Farsta",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 4 713 småhus i Farsta stadsdelsområde, och 3 806 av dem ägs med "
       "äganderätt. I Tallkrogen fanns 941 småhus med äganderätt och i Svedmyra 327. Det är alltså många "
       "fastighetsägare som själva bestämmer över sina hus – och många som funderar på mer plats.",
       "Stadens vägledning Varsam utveckling av småhus- och villaområden räknar Tallkrogen, del av Svedmyra och "
       "del av Sköndal till småstugeområdena. Tallkrogen står där som kulturhistoriskt värdefull miljö med ett "
       "äldre miljöprogram, och delar av Svedmyra och Sköndal som kulturhistoriskt värdefulla. Där kan bygglov "
       "krävas även för en tillbyggnad som annars hade varit lovfri.",
     ],
     "aside": {"title": "Områdesfakta 2025", "items": [
       "4 713 småhus i Farsta", "941 ägda småhus i Tallkrogen", "327 ägda småhus i Svedmyra"]}},
    {"id": "tradgardssidan", "h2": "Bygg mot trädgårdssidan",
     "paras": [
       "Vägledningen beskriver småstugeområdenas enhetliga kvarter som ett viktigt karaktärsdrag. Det vanligaste är "
       "att tillbyggnader läggs in mot tomten, i den privata zonen på trädgårdssidan, och att man undviker att "
       "bygga mot gatan. Tillbyggnader mot gården bör placeras så att siktvyerna från gatan in mot trädgårdarna "
       "hålls öppna.",
       "Vägledningen konstaterar också att många hus har byggts till genom åren, och att förändringarna "
       "huvudsakligen har gjorts mot trädgården. Det är därför områdena fortfarande känns sammanhållna. Vi ritar "
       "tillbyggnaden så att den syns så lite som möjligt från gatan och så att ljuset i huset blir bättre.",
     ],
     "aside": {"title": "Vägledningens råd", "items": [
       "Bygg mot trädgårdssidan", "Undvik tillbyggnad mot gatan", "Håll siktvyerna öppna"]}},
    {"id": "nock-takfot", "h2": "Lägre nock, samma takfot",
     "paras": [
       "Vägledningen ber fastighetsägaren utgå från det ursprungliga husets volym, proportioner och takform. I ett "
       "av exemplen underordnar sig tillbyggnaden huvudbyggnaden: taknocken på tillbyggnaden ligger lägre än "
       "husets nock, medan takfoten ligger på samma nivå. Husets ursprungliga form ska fortfarande gå att läsa ut.",
       "För en liten stuga med sadeltak blir det ofta en tillbyggnad med samma takvinkel och samma takfot, men "
       "med lägre nock. Vi ritar sektioner som visar hur takfallen möts, så att anslutningen går att bygga tät "
       "och snön inte blir liggande i vinkeln.",
     ],
     "aside": None},
    {"id": "potten-farsta", "h2": "De 30 kvadratmetrarna och tidigare tillbyggnader",
     "paras": [
       "Stockholms stad skriver att en lovfri tillbyggnad får vara högst 30,0 kvadratmeter bruttoarea eller "
       "öppenarea och inte högre än husets taknock, och att alla lovfria tillbyggnader på huset räknas ihop. "
       "Boverket ger ett exempel: har du redan byggt en attefallstillbyggnad på 15 kvadratmeter och ett skärmtak på "
       "15 kvadratmeter kan du inte bygga till mer utan bygglov.",
       "Tillbyggnaden ska stå minst 4,5 meter från gräns, annars krävs grannens skriftliga medgivande, och minst "
       "30 meter från en järnvägs mitt. Påverkas husets bärande delar eller brandskydd, eller ska tillbyggnaden få "
       "vatten och avlopp eller eldstad, krävs anmälan och startbesked. Läs mer om " +
       _L.format("attefallshus-farsta.html", "attefallshus i Farsta") + " om du väger en tillbyggnad mot ett "
       "eget gårdshus, och om utbyggnader i allmänhet under " + _L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": {"title": "Lovfritt – om inget annat gäller", "items": [
       "Högst 30,0 m² sammanlagt", "Inte över husets nock", "4,5 m till gräns eller medgivande"]}},
  ],
  "steps_h2": "Så bygger vi till ett hus i Farsta",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter stugan och tidigare tillbyggnader."),
    ("Kartan", "Stadsmuseets karta och detaljplanen kontrolleras."),
    ("Ritningar", "Tillbyggnad mot trädgården med lägre nock."),
    ("Lov eller anmälan", "Bygglov i värdefull miljö, annars anmälan där det krävs."),
    ("Bygget", "Grund, stomme, tak och anslutning mot huset."),
    ("Slutbesked", "Den nya delen tas i bruk efter slutbesked."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Farsta",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Farsta?",
  "price": [
    "Storlek och grundläggning, hur takfallen ska mötas, om bärande väggar öppnas, våtrum och installationer, "
    "och om bygglov och ritningar för en kulturmiljö behövs. Efter ett gratis platsbesök får du ett skriftligt "
    "kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga till mot gatan i Tallkrogen?",
     "Stadens vägledning för småstugeområdena råder att tillbyggnader läggs mot trädgårdssidan och att man undviker "
     "att bygga mot gatan, eftersom de enhetliga kvarteren är ett viktigt karaktärsdrag."),
    ("Krävs bygglov för en tillbyggnad i Tallkrogen?",
     "Tallkrogen står som kulturhistoriskt värdefull miljö i stadens vägledning. Visar Stadsmuseets karta att "
     "fastigheten ligger i en sådan miljö krävs bygglov även för en tillbyggnad som annars är lovfri."),
    ("Hur högt får taket på tillbyggnaden vara i Farsta?",
     "En lovfri tillbyggnad får inte gå över husets taknock. Vägledningen visar exempel där nocken på "
     "tillbyggnaden är lägre än husets och takfoten ligger på samma nivå."),
    ("Räknas vårt skärmtak in när vi bygger till i Farsta?",
     "Ja. Boverket skriver att tidigare lovfria tillbyggnader som skärmtak, altaner och attefallstillbyggnader "
     "räknas in i de 30 kvadratmetrarna."),
    ("Behövs anmälan om tillbyggnaden får ett badrum i Farsta?",
     "Ja. Installeras vatten och avlopp, ventilation eller eldstad i tillbyggnaden krävs anmälan och startbesked."),
  ],
  "sources": [_of("Farsta stadsdelsområde", "soderort/farsta/farsta-stadsdelsomrade"), _of("Tallkrogen", "soderort/farsta/tallkrogen"),
              _of("Svedmyra", "soderort/farsta/svedmyra"), _VARSAM, _STH_TB, _STH_KLASS, _BV_TB, _SKV],
  "cta": ("Funderar du på att bygga till i Farsta?",
          "Boka ett gratis platsbesök, så går vi igenom huset, kartan och tidigare tillbyggnader innan du får ett "
          "skriftligt kostnadsförslag."),
  "img": [
    ("Liten stuga med sadeltak och en lägre tillbyggnad mot trädgården",
     "small 1930s Swedish cottage with a red clay tile gable roof and light yellow wooden panel, with a lower new "
     "extension on the garden side using the same roof angle and eaves height, lawn, apple tree and berry bushes, "
     "summer daylight" + _SFX),
    ("Gata i ett småstugeområde med likadana hus och häckar",
     "empty quiet street in a Swedish 1930s small cottage area with rows of similar small one-and-a-half storey "
     "wooden houses painted in pale colours with gable roofs, low hedges and gardens, no cars, nobody on the street, soft morning light" + _SFX),
    ("Takfall från en tillbyggnad som möter huvudhusets tak",
     "close view of where the roof of a new single-storey extension meets the wall and roof of an older small "
     "wooden house, metal flashing along the joint, red clay tiles, blue sky" + _SFX),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"tillbyggnad-spanga.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Spånga", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Spånga – villastäderna och tomterna",
  "description": "Tillbyggnad i Spånga: villastäderna Solhem, Bromsten, Flysta och Sundby, stora tomter, detaljplanen "
                 "och när det går att bygga mot gatan.",
  "h1": "Tillbyggnad i Spånga",
  "lead": "Spångas villastäder växte fram runt järnvägen, med fritt liggande villor på stora tomter. Där finns ofta "
          "plats att bygga till – men också en kulturmiljö att ta hänsyn till. Geal Entreprenad AB reder ut "
          "reglerna för din tomt och bygger till huset med total entreprenad.",
  "card": "Villastäderna, tomterna och gatan.",
  "sections": [
    {"id": "villastaderna-spanga", "anchor": "Villastäderna",
     "h2": "Villastäderna i Spånga",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden räknar Solhem, Bromsten, Flysta och Sundby "
       "till villastäderna. Vägledningen berättar att små stationssamhällen uppstod när järnvägen byggdes ut och "
       "att Spånga på 1910-talet blev ett municipalsamhälle med egen administration och beskattningsrätt. I "
       "vägledningens tabell står Solhem som kulturhistoriskt värdefull miljö.",
       "Enligt områdesfakta för 2025 fanns 1 946 småhus med äganderätt i Solhem, 916 i Bromsten, 657 i Flysta "
       "och 525 i Sundby. De flesta småhusen i de fyra områdena ägs alltså med äganderätt.",
     ],
     "aside": {"title": "Ägda småhus 2025", "items": [
       "Solhem 1 946", "Bromsten 916", "Flysta 657", "Sundby 525"]}},
    {"id": "tomterna-spanga", "h2": "Stora tomter och små byggrätter",
     "paras": [
       "Villastäderna fick stora tomter. Vägledningen anger tomter på 1 500–3 000 kvadratmeter som typiska, och "
       "när nya planer togs fram för delar av villastäderna på 1930-talet blev tomterna 700–1 000 kvadratmeter. "
       "I Solhem fick enligt vägledningen bara en tiondel av tomten bebyggas.",
       "En äldre plan kan alltså sätta en snäv gräns för hur mycket huset får växa. Stockholms stad skriver att "
       "en lovfri tillbyggnad på ett en- eller tvåbostadshus får strida mot detaljplanen, till exempel stå på mark "
       "som inte får bebyggas. Men det gäller bara om ingen utökad lovplikt finns – i en särskilt värdefull miljö "
       "krävs bygglov, och då prövas tillbyggnaden mot planen.",
     ],
     "aside": {"title": "Villastadens tomter", "items": [
       "Ofta 1 500–3 000 m²", "700–1 000 m² i 1930-talsplaner", "Solhem: en tiondel fick bebyggas"]}},
    {"id": "gatan-spanga", "h2": "Mot trädgården – eller mot gatan",
     "paras": [
       "För villastäderna skriver vägledningen att det vanligaste är att tillbyggnader läggs mot trädgårdssidan och "
       "att man undviker att bygga mot gatan. Men den gör ett undantag: ligger huvudbyggnaden fritt på tomten med "
       "trädgården mot gatan kan en tillbyggnad mot gaturummet fungera, utan att gaturummet påverkas negativt.",
       "Vägledningen ber också fastighetsägaren fundera på hur huset förhåller sig till grannarna – är det en "
       "blandning av hus från olika tider, och finns det något gemensamt uttryck att fånga upp? Vi börjar därför "
       "med att titta på gatan, inte bara på huset, när vi föreslår var tillbyggnaden ska ligga.",
     ],
     "aside": None},
    {"id": "regler-spanga", "h2": "Lovfritt, anmälan och grannarna",
     "paras": [
       "Utan utökad lovplikt får en tillbyggnad vara högst 30,0 kvadratmeter sammanlagt och inte gå över husets "
       "nock. Den ska stå minst 4,5 meter från gränsen mot granne, samfällighet eller allmän plats, annars krävs "
       "skriftligt medgivande. För gatu- och parkmark är det oftast staden som ska ge medgivandet, och förfrågan "
       "skickas till stadsbyggnadskontoret.",
       "Påverkas bärande delar eller brandskydd, eller ska tillbyggnaden få vatten, avlopp eller eldstad, krävs "
       "anmälan och startbesked. Vill du hellre bygga fristående finns " +
       _L.format("attefallshus-spanga.html", "attefallshus i Spånga") + ", och totalrenoveringar beskriver vi "
       "under " + _L.format("totalrenovering-spanga.html", "totalrenovering i Spånga") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi till ett hus i Spånga",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter huset, tomten och avstånden."),
    ("Planen och kartan", "Detaljplanen och Stadsmuseets karta kontrolleras."),
    ("Placering", "Trädgårdssidan eller gatan – efter hur huset står."),
    ("Lov eller anmälan", "Bygglov där miljön kräver det, annars anmälan."),
    ("Bygget", "Grund, stomme, tak och anslutning mot huset."),
    ("Slutbesked", "Den nya delen tas i bruk efter slutbesked."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Spånga",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Spånga?",
  "price": [
    "Storlek, grundläggning på en kuperad eller plan tomt, hur fasad och tak ska anslutas, om väggar öppnas och "
    "om bygglov behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur mycket fick man bygga på en tomt i Solhem?",
     "Enligt stadens vägledning fick bara en tiondel av tomten bebyggas i Solhem. Vad som gäller i dag står i "
     "detaljplanen för fastigheten."),
    ("Får en lovfri tillbyggnad i Spånga strida mot detaljplanen?",
     "För ett en- eller tvåbostadshus, ja, enligt Stockholms stad – till exempel på mark som inte får bebyggas. "
     "Men inte om utökad lovplikt gäller, som i en särskilt värdefull miljö."),
    ("Kan vi bygga till mot gatan i Spånga?",
     "Vägledningen för villastäderna säger att det kan fungera när huset ligger fritt på tomten med trädgården "
     "mot gatan och gaturummet inte påverkas negativt."),
    ("Vem ger medgivande om tillbyggnaden hamnar nära gatan i Spånga?",
     "För gatu- och parkmark är det oftast staden. Förfrågan skickas till stadsbyggnadskontoret, och medgivandet "
     "ska vara skriftligt."),
    ("Behövs anmälan för en tillbyggnad med badrum i Spånga?",
     "Ja. Ska tillbyggnaden få vatten och avlopp, ventilation eller eldstad krävs anmälan och startbesked, även om "
     "själva tillbyggnaden är lovfri."),
    ("Är Solhem en kulturmiljö?",
     "Ja. Stadens vägledning listar Solhem som kulturhistoriskt värdefull miljö."),
  ],
  "sources": [_VARSAM, _of("Solhem", "vasterort/jarva/solhem"), _of("Bromsten", "vasterort/jarva/bromsten"),
              _of("Flysta", "vasterort/jarva/flysta"), _of("Sundby", "vasterort/jarva/sundby"), _STH_TB, _BV_TB, _SKV],
  "cta": ("Funderar du på att bygga till i Spånga?",
          "Boka ett gratis platsbesök, så går vi igenom tomten, planen och gatan innan du får ett skriftligt "
          "kostnadsförslag."),
  "img": [
    ("Villa från 1920-talet på en stor tomt med en ny tillbyggnad mot trädgården",
     "1920s Swedish wooden villa with a hipped red tile roof and light green panel on a large garden plot, with a "
     "new single-storey extension with large windows on the garden side, old apple trees, summer daylight" + _SFX),
    ("Villagata med fritt liggande hus och stora trädgårdar",
     "quiet Swedish villa street with individually designed detached houses set back on large garden plots, "
     "hedges and old trees along the street, early 20th century villa town, soft daylight" + _SFX),
    ("Nygjuten grund för en tillbyggnad intill en äldre villa",
     "newly cast concrete foundation slab with insulation edge for a house extension next to the wall of an older "
     "wooden villa, garden around it, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"tillbyggnad-vallingby.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Vällingby", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Vällingby – radhus i riksintresset",
  "description": "Tillbyggnad i Vällingby: radhus och kedjehus i riksintresset Vällingby–Råcksta, uterum, skärmtak och "
                 "takkupor, bygglov och föreningens tillstånd.",
  "h1": "Tillbyggnad i Vällingby",
  "lead": "I Vällingby och Råcksta ligger radhus och kedjehus från 1950-talet i enhetliga grupper, och stora "
          "delar av stadsdelen ingår i riksintresset Vällingby–Råcksta. Ett uterum eller en större takkupa är fullt möjligt, men kräver ofta bygglov. Geal "
          "Entreprenad AB ritar tillbyggnaden efter husgruppen och sköter ansökan och bygget.",
  "card": "Radhusen, riksintresset och lovet.",
  "sections": [
    {"id": "riksintresset-vallingby", "anchor": "Riksintresset",
     "h2": "Radhusen i riksintresset",
     "paras": [
       "Stadens beskrivning av riksintressena berättar att Vällingby–Råcksta planerades som landets första ABC-stad, "
       "med högre hus närmast centrum och en successiv nedtrappning av skalan, och längst ut områden med radhus och "
       "småhus. Bland karaktärsdragen nämns bebyggelsens anpassning till naturen och terrängen och de ursprungliga "
       "husens gestaltning och detaljer.",
       "Stockholms stad skriver att bygglov krävs för åtgärder inom ett riksintresse för kulturmiljövården, som "
       "visas med en blå ring i Stadsmuseets karta – även för sådant som annars är lovfritt. En tillbyggnad på ett "
       "radhus inom riksintresset prövas därför av byggnadsnämnden.",
     ],
     "aside": {"title": "Riksintresset", "items": [
       "Vällingby–Råcksta", "Radhus längst ut från centrum", "Lov även för lovfria åtgärder"]}},
    {"id": "vad-ar-tillbyggnad-vallingby", "h2": "Uterum, skärmtak och takkupor",
     "paras": [
       "Stockholms stad beskriver en tillbyggnad som något som byggs direkt mot huset och ökar dess volym. Som "
       "exempel nämns uterum, skärmtak, större takkupor och lågt sittande balkonger. Utanför riksintresset kan en "
       "sådan tillbyggnad vara lovfri upp till 30,0 kvadratmeter sammanlagt, men i Vällingby–Råcksta behövs lov.",
       "Stadens vägledning för tunnelbanestäderna beskriver radhusområdena som enhetligt utformade husgrupper, "
       "och flera av dem har höga kulturmiljö- och stadsbildsmässiga värden. Ett uterum som ska godkännas ritas därför med samma "
       "takvinkel, material och kulörer som huset, och helst likadant som grannarnas om flera i raden har byggt.",
     ],
     "aside": {"title": "Exempel på tillbyggnad", "items": [
       "Uterum", "Skärmtak", "Större takkupa", "Lågt sittande balkong"]}},
    {"id": "suterrang-vallingby", "h2": "Suterränghusen på bryn och platåer",
     "paras": [
       "Vägledningen beskriver hur bryn och platåer utanför centrum användes till radhus, med mjuk anpassning till "
       "terrängen och nivåskillnader som tas upp med en suterrängvåning. Det påverkar tillbyggnaden: mot trädgården "
       "kan marken ligga en våning lägre än mot gatan.",
       "Ett uterum på suterrängsidan kan behöva stå på pelare eller en egen grund, och ansluta mot husets bjälklag. "
       "Vi tar fram konstruktionsunderlag för grunden och anslutningen, och om bärande delar påverkas väsentligt "
       "krävs anmälan och startbesked utöver lovet.",
     ],
     "aside": None},
    {"id": "foreningen-tillbyggnad", "h2": "När radhuset är en bostadsrätt",
     "paras": [
       "Enligt stadens områdesfakta för 2025 var 228 av de 449 småhusen i Vällingby bostadsrätter, och i Råcksta "
       "91 av 390. I ett radhus med bostadsrätt är det föreningen som äger huset, och en tillbyggnad kräver "
       "föreningens tillstånd innan något annat. Staden påminner om att du som bor i en bostadsrätt behöver "
       "föreningens tillstånd för ändringar som påverkar bärande delar, ventilation eller vatten och avlopp.",
       "Vi tar fram ritningar som både styrelsen och byggnadsnämnden kan ta ställning till. Vill du hellre bygga "
       "fristående på tomten beskriver vi det under " + _L.format("attefallshus-vallingby.html", "attefallshus i "
       "Vällingby") + ", och utbyggnader i allmänhet under " + _L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Vällingby: 228 av 449 bostadsrätter", "Råcksta: 91 av 390 bostadsrätter"]}},
  ],
  "steps_h2": "Så bygger vi till ett radhus i Vällingby",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter huset och nivåerna mot trädgården."),
    ("Föreningen", "Tillstånd från föreningen om radhuset är en bostadsrätt."),
    ("Ritningar", "Tillbyggnad efter husgruppens form, material och kulörer."),
    ("Bygglov", "Ansökan till byggnadsnämnden inom riksintresset."),
    ("Bygget", "Grund, stomme, tak och anslutning mot huset."),
    ("Slutbesked", "Den nya delen tas i bruk efter slutbesked."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Vällingby",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Vällingby?",
  "price": [
    "Storlek, grundläggning på suterrängsidan, hur taket ansluts, material som ska matcha husgruppen och "
    "bygglovshandlingarna. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för ett uterum på vårt radhus i Vällingby?",
     "Om huset ligger inom riksintresset Vällingby–Råcksta, ja. Stockholms stad skriver att bygglov krävs inom "
     "ett riksintresse för kulturmiljövården även för åtgärder som annars är lovfria."),
    ("Räknas en större takkupa som tillbyggnad i Vällingby?",
     "Ja. Stockholms stad nämner större takkupor bland exemplen på tillbyggnader."),
    ("Hur långt från gränsen får tillbyggnaden stå i Vällingby?",
     "En lovfri tillbyggnad ska stå minst 4,5 meter från gräns, annars krävs skriftligt medgivande. Inom "
     "riksintresset söks bygglov ändå, och då prövas placeringen i ansökan."),
    ("Vårt radhus i Vällingby är en bostadsrätt – vem bestämmer?",
     "Föreningen äger huset. Börja med att fråga styrelsen om tillstånd innan ni söker bygglov."),
    ("Kan vi bygga en balkong på radhuset i Vällingby?",
     "En lågt sittande balkong räknas som tillbyggnad enligt Stockholms stad. Inom riksintresset krävs bygglov, "
     "och i en bostadsrätt även föreningens tillstånd."),
    ("Hur bygger man ett uterum på suterrängsidan?",
     "Ofta på pelare eller egen grund med anslutning mot husets bjälklag. Påverkas bärande delar väsentligt krävs "
     "anmälan och startbesked."),
    ("Måste uterummet se ut som grannarnas i Vällingby?",
     "Det är inget krav i sig, men husgrupperna är enhetligt utformade enligt stadens vägledning. Vi ritar därför "
     "gärna uterummet likt grannarnas och efter husets form."),
  ],
  "sources": [_RIKS, _VARSAM, _STH_TB, _STH_KLASS, _PLAN, _of("Vällingby", "vasterort/hasselby-vallingby/vallingby"),
              _of("Råcksta", "vasterort/hasselby-vallingby/racksta"), _SKV],
  "cta": ("Funderar du på att bygga till radhuset i Vällingby?",
          "Boka ett gratis platsbesök, så går vi igenom huset, föreningen och lovet innan du får ett skriftligt "
          "kostnadsförslag."),
  "img": [
    ("Ljust putsat radhus med ett inglasat uterum vid gaveln",
     "Swedish 1950s two-storey row house terrace with light plastered facade, simple gable roof with black concrete "
     "tiles and small square windows, one house with a newly built glazed sunroom on the garden side, small lawn, "
     "pine trees behind, Stockholm suburb, summer daylight" + _SFX),
    ("Radhus i suterräng på ett bryn med gångväg nedanför",
     "1950s Swedish row houses built on the edge of a slope with a lower ground floor facing a garden, footpath "
     "and lawn below, birch and pine trees, soft daylight" + _SFX),
    ("Takkupa på ett radhustak med svarta betongpannor",
     "newly built small dormer with dark metal cladding on the black concrete tile roof of a 1950s Swedish row "
     "house, neighbouring roofs in a row, blue sky" + _SFX),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"tillbyggnad-skarholmen.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Skärholmen", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Skärholmen – radhus, uterum och skärmtak",
  "description": "Tillbyggnad i Skärholmen: gruppbyggda radhus i Bredäng och Sätra, skärmtak, uterum eller bod mot "
                 "trädgården, platta tak och 4,5 meter till gräns.",
  "h1": "Tillbyggnad i Skärholmen",
  "lead": "Radhusen och kedjehusen i Bredäng, Sätra och Vårberg står på små tomter i enhetliga grupper. Stadens "
          "vägledning säger rakt ut att utrymmet för tillbyggnader ofta är litet – men ett skärmtak, ett uterum "
          "eller en bod kan få plats. Geal Entreprenad AB ritar och bygger det som passar huset och tomten.",
  "card": "Radhusen, uterum och skärmtak.",
  "sections": [
    {"id": "storskalig-stadsdel", "anchor": "Radhusen",
     "h2": "Radhusen i den storskaliga stadsdelen",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden räknar Bredäng, Sätra, Skärholmen och "
       "Vårberg till de storskaliga stadsdelarna. Bredäng var den första stadsdelen som planerades i stor skala och "
       "började byggas 1962, följt av Sätra. Småhusen där är främst radhus och kedjehus, men det finns även villor "
       "och atriumhus.",
       "Enligt områdesfakta för 2025 fanns 1 991 småhus i Skärholmens stadsdelsområde, och 1 976 av dem ägdes med "
       "äganderätt. I Sätra fanns 536 ägda småhus och i Bredäng 320. Bredäng står i vägledningens tabell som "
       "kulturhistoriskt värdefull miljö.",
     ],
     "aside": {"title": "Områdesfakta 2025", "items": [
       "1 991 småhus i stadsdelsområdet", "536 ägda småhus i Sätra", "320 ägda småhus i Bredäng"]}},
    {"id": "litet-utrymme", "h2": "Som regel litet utrymme – men inte inget",
     "paras": [
       "Vägledningen skriver att de gruppbyggda småhusen står på små tomter och att möjligheterna till större "
       "förändringar därför är begränsade. Som regel finns inget utrymme för tillbyggnad, eftersom de enhetliga "
       "kvarteren och relationen till gatan är viktiga att behålla. I vissa fall kan ett mindre skärmtak, ett "
       "inglasat uterum eller en bod rymmas, och vägledningen konstaterar att just inglasade uterum är vanliga.",
       "Det vanligaste är att lägga dem mot tomtens privata del, trädgårdssidan, och att undvika förändringar mot "
       "gatan. Vi börjar därför med att se vad grannarna i samma grupp redan har byggt och hur trädgården ligger.",
     ],
     "aside": {"title": "Kan ofta rymmas", "items": [
       "Mindre skärmtak", "Inglasat uterum", "En bod"]}},
    {"id": "tak-och-volym", "h2": "Platta tak och husgruppens form",
     "paras": [
       "Enligt vägledningen har småhusen i de storskaliga stadsdelarna huvudsakligen platta tak eller pulpettak, "
       "även om branta sadeltak förekommer. Fasaderna blandar tegel, trä och skivor, och färgsättningen är enhetlig "
       "inom varje husgrupp. Vägledningen ber fastighetsägaren utgå från husets volym, proportioner och takform och "
       "påpekar att det gäller även för ett skärmtak, ett inglasat uterum eller en bod.",
       "Ett uterum mot ett radhus med platt tak får därför ofta ett platt eller svagt lutande tak, och dess "
       "takavvattning behöver lösas så att vattnet inte rinner mot grannens tomt. Vi ritar anslutningen mot husets "
       "fasad och tak så att den blir tät.",
     ],
     "aside": None},
    {"id": "grans-skarholmen", "h2": "Små tomter och 4,5 meter till gräns",
     "paras": [
       "En lovfri tillbyggnad ska enligt Stockholms stad stå minst 4,5 meter från gräns mot granne, samfällighet "
       "eller allmän plats, annars krävs ett skriftligt medgivande. På ett radhus ligger huset ofta i gräns mot "
       "båda grannarna, så ett uterum på baksidan kräver i regel medgivanden – eller bygglov. Medgivandet ska "
       "innehålla fastighetsbeteckning, vilken åtgärd det gäller, en situationsplan med avstånden och grannarnas "
       "underskrifter.",
       "Ligger huset i en särskilt värdefull miljö, som Bredäng, krävs bygglov ändå. Läs mer om " +
       _L.format("takbyte-skarholmen.html", "takbyte i Skärholmen") + " om taket ska bytas samtidigt, och om "
       "utbyggnader i allmänhet under " + _L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": {"title": "Medgivandet ska innehålla", "items": [
       "Fastighetsbeteckning", "Vilken åtgärd det gäller", "Situationsplan med avstånd", "Grannarnas underskrifter"]}},
  ],
  "steps_h2": "Så bygger vi till ett radhus i Skärholmen",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter tomten och ser vad grannarna har byggt."),
    ("Kartan", "Stadsmuseets karta och detaljplanen kontrolleras."),
    ("Medgivanden", "Skriftliga medgivanden från grannarna, eller bygglov."),
    ("Ritningar", "Uterum eller skärmtak efter husgruppens form."),
    ("Bygget", "Grund, stomme, tak och tät anslutning mot huset."),
    ("Slutbesked", "Slutbesked där lov eller anmälan har krävts."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Skärholmen",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Skärholmen?",
  "price": [
    "Storlek, glas och tak, grundläggning, anslutning mot husets fasad och takavvattning, och om bygglov behövs. "
    "Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi bygga ett uterum på vårt radhus i Sätra?",
     "Ofta ja. Stadens vägledning skriver att ett inglasat uterum, ett mindre skärmtak eller en bod i vissa fall "
     "kan rymmas, helst mot trädgårdssidan."),
    ("Räknas ett skärmtak som tillbyggnad i Skärholmen?",
     "Ja. Stockholms stad nämner skärmtak bland exemplen på tillbyggnader, och det räknas in i de 30 "
     "kvadratmetrarna."),
    ("Behöver vi grannarnas medgivande för ett uterum i Skärholmen?",
     "Om uterummet hamnar närmare gränsen än 4,5 meter, ja – och på ett radhus gör det oftast det. Utan skriftliga "
     "medgivanden krävs bygglov."),
    ("Vilket tak ska uterummet ha i Bredäng?",
     "Vägledningen ber att man utgår från husets takform. Har radhuset platt tak eller pulpettak blir uterummets "
     "tak ofta platt eller svagt lutande."),
    ("Kan vi bygga en bod i stället för ett uterum i Skärholmen?",
     "Ja. Stadens vägledning nämner en bod bland det som i vissa fall kan rymmas på tomterna. Den ska följa "
     "husets volym och takform precis som ett uterum."),
    ("Behöver ett uterum i Skärholmen anmälas?",
     "Bara om det påverkar husets bärande delar eller brandskydd väsentligt, eller får vatten, avlopp, "
     "ventilation eller eldstad. Annars räcker lovfriheten eller bygglovet."),
    ("När började Bredäng byggas?",
     "1962, enligt stadens vägledning. Bredäng var den första stadsdelen som planerades i stor skala, följt av "
     "Sätra."),
    ("Är Bredäng en kulturmiljö?",
     "Ja. Stadens vägledning listar Bredäng som kulturhistoriskt värdefull miljö, och där krävs bygglov för "
     "tillbyggnader som annars kunde ha varit lovfria."),
  ],
  "sources": [_VARSAM, _of("Skärholmens stadsdelsområde", "soderort/skarholmen/skarholmen-stadsdelsomrade"),
              _of("Sätra", "soderort/skarholmen/satra"), _of("Bredäng", "soderort/skarholmen/bredang"),
              _STH_TB, _STH_KLASS, _BV_TB, _SKV],
  "cta": ("Funderar du på ett uterum eller skärmtak i Skärholmen?",
          "Boka ett gratis platsbesök, så går vi igenom tomten, grannarna och lovet innan du får ett skriftligt "
          "kostnadsförslag."),
  "img": [
    ("Radhus med platta tak och ett inglasat uterum mot en liten trädgård",
     "1960s Swedish flat-roofed row houses with facades of brick and dark wooden panel, one house with a small "
     "glazed sunroom with a flat roof on the garden side, small lawn and a low fence, summer daylight" + _SFX),
    ("Rad med likadana radhus längs en gångväg",
     "row of identical 1960s Swedish two-storey row houses with flat roofs and a broad wooden fascia, facades of "
     "red brick and dark brown vertical wooden panel, along a car-free footpath, small front gardens, no gables, soft daylight" + _SFX),
    ("Skärmtak över en uteplats vid ett radhus",
     "simple wooden canopy with a low-pitched roof over a patio at the back of a 1960s Swedish row house, wooden "
     "decking, potted plants, overcast daylight" + _SFX),
  ],
},
}
