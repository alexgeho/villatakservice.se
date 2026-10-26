# -*- coding: utf-8 -*-
"""Köksrenovering – ortsidor v31: Hässelby, Sigtuna, Vällingby (2026-10-27).
Hubb: koksrenovering.html (TJ_HUB["koksrenovering"]). Intent: renovera eller flytta kök. Tre bilder per sida:
img[0] hero 4:3, img[1] och img[2] 3:2.

Lokal vinkel per sida:
Hässelby – områdesfakta 2025 för Hässelby villastad (7 029 bostäder, 5 009 småhus, 4 757 med äganderätt), Hässelby gård och
  Hässelby strand (bostadsrätter och hyresrätter), Varsam om villastaden (villor ersatta av gruppbyggda småhus på
  1960–70-talen, styckade tomter kring 600 kvadratmeter), stadens regler för att flytta kök, ventilationssystem efter
  byggår, elarbeten enligt Elsäkerhetsverket.
Sigtuna – kommunens sidor om ventilation (anmälan och startbesked vid nytt eller ändrat system, bygglov vid aggregat på
  fasaden) och vatten och avlopp (anmälan vid väsentlig ändring, tillstånd för enskilt avlopp enligt miljöbalken,
  kontrollplan), bevarande- och förnyelseplanen (q-bestämmelser som kan omfatta interiör).
Vällingby – riksintressedelen AB 120 (ABC-staden, utbyggd under 1950-talet, socialt program med en rationell vardag),
  områdesfakta 2025 för Vällingby och Råcksta, bostadsrättslagen 7 kap. 7 § (styrelsens tillstånd för ledningar och
  ventilation), stadens råd om imkanal och sotaren, hyresrätt.

Fakta endast från källorna i respektive 'sources', öppnade med curl (webbläsar-UA) 2026-10-27, alla svarade 200; pdf:erna
har textlager. Skatteverket 2026-10-27: småhus – montera fast köksinredning och installera vitvaror i samband med
omfattande byggarbete eller renovering, byta och reparera köksluckor; bostadsrätt – samma i samband med byggarbetet,
innanför lägenhetens tak, väggar och golv; 30 procent och högst 50 000 kronor.
Strukna / ej använda: vilken ventilation enskilda hus i orterna har, handläggningstider och avgifter, priser på kök.
Inga garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SI = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_STH_KOK = ("Stockholms stad – Flytta kök eller badrum", _SI + "flytta-kok-eller-badrum/")
_STH_VENT = ("Stockholms stad – Ventilation", _SI + "ventilation/")
_ELSAK = ("Elsäkerhetsverket – Vad får jag göra själv med el?",
          "https://www.elsakerhetsverket.se/privatpersoner/detta-far-du-gora-sjalv-med-el/vad-far-jag-gora-sjalv-med-el")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SIG_VENT = ("Sigtuna kommun – Installation eller ändring av ventilation",
             "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/andra-befintlig-byggnad/installation-eller-andring-av-ventilation.html")
_SIG_VA = ("Sigtuna kommun – Vatten och avlopp (ändra befintlig byggnad)",
           "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/andra-befintlig-byggnad/vatten-och-avlopp.html")
_SIG_BEV = ("Sigtuna kommun – Bevarande- och förnyelseplan för Sigtuna stad, antagen 2019 (pdf)",
            "https://www.sigtuna.se/download/18.6ed4dd301706254f993282/1582201854957/Bevarande-%20och%20f%C3%B6rnyelseplan%20f%C3%B6r%20Sigtuna%20stad,%20antagen%202019.pdf")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material, "
            "skåp och vitvaror ger inget avdrag, och Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ HÄSSELBY
"koksrenovering-hasselby.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Hässelby", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Hässelby – villastaden och radhusen",
  "description": "Köksrenovering i Hässelby: villor och gruppbyggda småhus i Hässelby villastad, flytt av kök, ventilation efter byggår, el och rotavdrag.",
  "h1": "Köksrenovering i Hässelby",
  "lead": "I Hässelby villastad finns över 5 000 småhus, med villor från olika årtionden och grupper av radhus från 1960- och 70-talen. Köket i ett sådant hus har ofta byggts om flera gånger. Geal Entreprenad AB renoverar och flyttar kök i villor, radhus och lägenheter i Hässelby och tar hand om el, vatten och ventilation.",
  "card": "Kök i villor och radhus.",
  "sections": [
    {"id": "villastaden-hasselby", "anchor": "Villastaden",
     "h2": "Över 5 000 småhus i villastaden",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 7 029 bostäder i Hässelby villastad, varav 5 009 i småhus. 4 757 av småhusen ägs med äganderätt och 204 är bostadsrätter. I grannstadsdelarna ser det annorlunda ut: Hässelby gård har 324 småhus med äganderätt men över 5 000 lägenheter i flerbostadshus, och i Hässelby strand finns nästan bara lägenheter i flerbostadshus.",
       "Stadens vägledning Varsam utveckling av småhus- och villaområden berättar att många villor i Hässelby villastad ersattes av täta grupper av enhetlig småhusbebyggelse på 1960- och 1970-talen. Genom att tomter successivt styckats av har villastäderna förtätats, och nya hus på tomter kring 600 kvadratmeter har kompletterat eller ersatt den äldre bebyggelsen. Köken i området är alltså från alla tider.",
     ],
     "aside": {"title": "Hässelby villastad 2025", "items": [
       "7 029 bostäder", "5 009 småhus", "4 757 med äganderätt", "Tomter kring 600 m² efter styckning"]}},
    {"id": "flytta-hasselby", "h2": "När köket ska flyttas",
     "paras": [
       "Stockholms stad skriver att du behöver göra en anmälan och invänta startbesked om flytten av ett kök innebär ändring av husets bärande konstruktion eller brandskydd, eller installation eller väsentlig ändring av ventilationen. Oavsett om anmälan krävs ska arbetet uppfylla de tekniska egenskapskraven i plan- och bygglagen.",
       "I en villa där köket ska öppnas mot vardagsrummet är det ofta en vägg som ska bort. Är väggen bärande tar vi in en konstruktör och gör anmälan innan vi river. Staden råder också att man tidigt pratar med skorstensfejarmästaren om förutsättningarna för en ny eller ändrad imkanal.",
     ],
     "aside": {"title": "Anmälan och startbesked när", "items": [
       "Bärande konstruktion ändras", "Brandskyddet påverkas", "Ventilationen ändras väsentligt", "Annars: tekniska krav ändå"]}},
    {"id": "ventilation-hasselby", "h2": "Ventilationen efter husets ålder",
     "paras": [
       "Staden beskriver tre vanliga system. I äldre hus finns ofta självdrag, där använd luft sugs ut via skorstenskanalen i kök och badrum; på sommaren kan drageffekten utebli. Frånluftsventilation med centrala fläktar är enligt staden vanlig i hus byggda 1961–1975, och från 1976 och framåt är från- och tilluft, ofta med värmeåtervinning, vanligt.",
       "Eftersom Hässelbys småhus är byggda under så olika perioder tar vi reda på vilket system ditt hus har innan köksfläkten väljs. Fläkten ska passa det system som finns, och ändras ventilationen väsentligt krävs anmälan.",
     ],
     "aside": None},
    {"id": "el-hasselby", "h2": "El och vatten i det nya köket",
     "paras": [
       "Elsäkerhetsverket skriver att förändringar i den fasta elinstallationen, till exempel ett uttag i köket och elledningar i väggar, ska göras av ett registrerat elinstallationsföretag. Själv får du bara göra enklare saker, som att byta en befintlig strömbrytare på högst 16 ampere, och bara om du har kunskapen. Vi samordnar elinstallatören så att uttag för spis, ugn och diskmaskin hamnar rätt i ritningen.",
       "Flyttas diskbänken drar vi nya vatten- och avloppsledningar och kontrollerar fallet till stammen. I ett radhus i en husgrupp kan ledningarna vara gemensamma, och då stämmer vi av med föreningen eller grannarna. Mer om tjänsten finns under " + _L.format("koksrenovering.html", "köksrenovering") + ", och för badrummet finns " + _L.format("badrumsrenovering-hasselby.html", "badrumsrenovering i Hässelby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi kök i Hässelby",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter och tittar på ventilationen."),
    ("Ritning", "Planlösning, el och vatten i ett förslag."),
    ("Anmälan", "Om väggar, brandskydd eller ventilation ändras."),
    ("Rivning", "Gamla skåp, ytskikt och installationer bort."),
    ("Installationer", "El, vatten, avlopp och imkanal."),
    ("Montage", "Skåp, bänkskivor och vitvaror på plats."),
  ],
  "rot_h2": "ROT-avdrag för köket i Hässelby",
  "rot": [
    "I ett småhus räknar Skatteverket det som rotarbete att montera fast köksinredning och installera vitvaror i samband med omfattande byggarbete eller renovering, att riva väggar och bygga om planlösningen och att byta köksluckor. Huset ska vara äldre än fem år.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset på ett kök i Hässelby?",
  "price": [
    "Storleken på köket, om det flyttas eller öppnas mot ett annat rum, nya el-, vatten- och avloppsdragningar, ventilationen, skåp, bänkskivor och vitvaror. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag göra en anmälan för att flytta köket i min villa i Hässelby?",
     "Ja, om flytten påverkar bärande konstruktion, brandskydd eller innebär en väsentlig ändring av ventilationen. Annars krävs ingen anmälan."),
    ("Vilken ventilation har ett radhus från 1960-talet?",
     "Enligt Stockholms stad är frånluftsventilation med centrala fläktar vanlig i hus byggda 1961–1975. Vi kontrollerar vad just ditt hus har."),
    ("Får jag dra ett nytt eluttag i köket själv?",
     "Nej. Elsäkerhetsverket skriver att ett uttag i köket och ledningar i väggar ska installeras av ett registrerat elinstallationsföretag."),
    ("Hur många villor finns det i Hässelby villastad?",
     "Stadens områdesfakta räknar 5 009 småhus 2025, varav 4 757 med äganderätt."),
  ],
  "sources": [_of("Hässelby villastad", "vasterort/hasselby-vallingby/hasselby-villastad"),
              _of("Hässelby gård", "vasterort/hasselby-vallingby/hasselby-gard"),
              _of("Hässelby strand", "vasterort/hasselby-vallingby/hasselby-strand"), _VARSAM, _STH_KOK, _STH_VENT, _ELSAK, _SKV],
  "cta": ("Planerar du ett nytt kök i Hässelby?", "Boka ett gratis platsbesök, så tittar vi på ventilation, el och vatten innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust villakök med vita luckor och träbänkskiva",
     "bright modern kitchen in a Swedish suburban villa with white flat cabinet doors, oak worktop, induction hob, window over the sink facing a garden, empty room, daylight" + _SFX),
    ("Öppning mellan kök och vardagsrum under ombyggnad",
     "renovation in progress in a Swedish house: a wide new opening between kitchen and living room with a laminated wooden beam above, bare studs and protective floor paper, tools on the floor, daylight" + _SFX),
    ("Köksfläkt och imkanal ovanför en spis",
     "close view of a stainless steel kitchen hood mounted on a white wall above a hob, with a white painted duct casing going up to the ceiling, plain wall tiles, soft light" + _SFX),
  ],
},

# ------------------------------------------------------------------ SIGTUNA
"koksrenovering-sigtuna.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Sigtuna", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Sigtuna – ventilation, avlopp och anmälan",
  "description": "Köksrenovering i Sigtuna: när ny ventilation kräver anmälan, ändrade avlopp och enskilda avlopp, kök i äldre trähus och rotavdrag.",
  "h1": "Köksrenovering i Sigtuna",
  "lead": "I Sigtuna kommun krävs en anmälan och ett startbesked innan du installerar eller ändrar ett ventilationssystem, och samma sak gäller när vatten och avlopp ändras väsentligt. Geal Entreprenad AB renoverar kök i Märsta, Sigtuna stad och kommunens övriga orter och tar fram underlaget när anmälan behövs.",
  "card": "Ventilation, avlopp och anmälan.",
  "sections": [
    {"id": "ventilation-sigtuna", "anchor": "Ventilation",
     "h2": "Ny eller ändrad ventilation",
     "paras": [
       "Sigtuna kommun skriver att du måste göra en anmälan och invänta startbesked om du ska installera ett nytt ventilationssystem, och att det också gäller om du ska ändra ett befintligt system. Innebär åtgärden en stor förändring av husets utsida, till exempel ett aggregat eller ventilationskanaler på fasaden, behöver du söka bygglov i stället.",
       "Till anmälan hör en situationsplan, som visar placering och läge sett ovanifrån och görs på kommunens tomtkarta, som enligt kommunen går att ladda ner gratis utan inloggning. Kommunen skriver också att ett förslag på kontrollplan ska lämnas in både vid bygglov och vid anmälan. Om det sker ändringar i den bärande konstruktionen ska de markeras på ritningarna, och en konstruktör ska intyga att kraven på bärförmåga uppfylls.",
     ],
     "aside": {"title": "Anmälan om ventilation", "items": [
       "Nytt ventilationssystem", "Ändrat befintligt system", "Bygglov vid aggregat på fasaden", "Kontrollplan krävs"]}},
    {"id": "avlopp-sigtuna", "h2": "Vatten och avlopp till köket",
     "paras": [
       "Om du väsentligt ändrar eller gör en ny installation för vatten eller avlopp behöver du enligt kommunen göra en anmälan. Ska byggnaden anslutas till det kommunala nätet anmäler du det i stället till Sigtuna Vatten och Renhållning. Att anlägga ett nytt eller ändra ett befintligt enskilt avlopp är en tillståndspliktig åtgärd enligt miljöbalken.",
       "För ett kök i en villa med eget avlopp betyder det att en ny diskmaskin eller en flyttad diskbänk inte bara är en fråga om rör i väggen. Vi går igenom om ändringen påverkar avloppsanläggningen och tar fram konstruktionsritningar om bärande delar berörs. Är ändringen omfattande behöver du enligt kommunen också anlita en kontrollansvarig.",
     ],
     "aside": {"title": "Vatten och avlopp i Sigtuna", "items": [
       "Anmälan vid väsentlig ändring", "Kommunalt nät: anmälan till SIVAB", "Enskilt avlopp: tillstånd", "Kontrollansvarig vid stora ändringar"]}},
    {"id": "trahus-sigtuna", "h2": "Kök i ett äldre trähus",
     "paras": [
       "Bevarande- och förnyelseplanen för Sigtuna stad berättar att kulturvärden kan skyddas med skydds- och varsamhetsbestämmelser i detaljplanen, och att en skyddsbestämmelse kan omfatta både exteriör och interiör och gälla utformning, material, teknik och underhåll. Inom planens område finns ungefär 60 gällande detaljplaner.",
       "I ett äldre hus i stadskärnan kontrollerar vi därför detaljplanen innan köket ritas. Det kan finnas en gammal spisplats, skorsten eller snickerier som ska vara kvar, och då planerar vi köket runt dem. En ny imkanal i ett sådant hus stämmer vi av med sotaren innan arbetet börjar.",
     ],
     "aside": None},
    {"id": "planering-sigtuna", "h2": "Planeringen i praktiken",
     "paras": [
       "Ett nytt kök börjar med en ritning där skåp, vitvaror, el, vatten och ventilation hänger ihop. När vi vet om anmälan krävs lägger vi in tiden för startbeskedet i tidsplanen, så att rivningen inte börjar för tidigt. Kommunens handläggare kan begära fler handlingar, och den tiden räknar vi med.",
       "Under bygget hålls köket avstängt men resten av huset går att använda. Vatten stängs bara av under de timmar som rören kopplas om. Mer om tjänsten finns under " + _L.format("koksrenovering.html", "köksrenovering") + ", och för badrummet finns " + _L.format("badrumsrenovering-sigtuna.html", "badrumsrenovering i Sigtuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi kök i Sigtuna",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter och går igenom installationerna."),
    ("Ritning", "Kök, el, vatten och ventilation i ett förslag."),
    ("Anmälan", "Situationsplan, ritningar och kontrollplan."),
    ("Startbesked", "Arbetet börjar när kommunen gett klartecken."),
    ("Bygget", "Rivning, installationer och ytskikt."),
    ("Slutskede", "Montage, kontroll och genomgång."),
  ],
  "rot_h2": "ROT-avdrag för köket i Sigtuna",
  "rot": [
    "Skatteverket räknar det som rotarbete att montera fast köksinredning och installera vitvaror i samband med en omfattande renovering, liksom att byta köksluckor och bygga om planlösningen. Avdraget gäller i villor, radhus och fritidshus som är äldre än fem år och i bostadsrätter i samband med byggarbetet.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset på ett kök i Sigtuna?",
  "price": [
    "Kökets storlek och utrustning, om ventilationen ändras och en anmälan med kontrollplan krävs, avloppets typ och nya dragningar, bärande väggar och hänsyn till ett äldre hus. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag anmäla en ny köksventilation i Sigtuna?",
     "Ja, om du installerar ett nytt ventilationssystem eller ändrar ett befintligt. Då krävs anmälan och startbesked från kommunen."),
    ("Krävs tillstånd om jag ändrar mitt enskilda avlopp när köket flyttas i Sigtuna?",
     "Ja. Kommunen skriver att det är tillståndspliktigt enligt miljöbalken att anlägga eller ändra ett enskilt avlopp."),
    ("Kan detaljplanen påverka köksrenoveringen i ett gammalt hus i Sigtuna stad?",
     "Ja, en skyddsbestämmelse kan enligt bevarande- och förnyelseplanen omfatta även interiören."),
    ("Var hittar jag tomtkartan till min anmälan i Sigtuna?",
     "Kommunen har en länk där du söker på adressen och laddar ner tomtkartan som pdf, utan inloggning och utan kostnad."),
  ],
  "sources": [_SIG_VENT, _SIG_VA, _SIG_BEV, _SKV],
  "cta": ("Vill du renovera köket i Sigtuna?", "Boka ett gratis platsbesök, så går vi igenom ventilation och avlopp innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Kök i ett äldre trähus med gamla snickerier",
     "renovated kitchen in an old Swedish timber house with new light grey cabinets, a wooden worktop and an old preserved panelled door and window trim, wide plank floor, daylight" + _SFX),
    ("Nya vatten- och avloppsrör vid en köksvägg",
     "close view of new copper water pipes and a grey plastic drain pipe mounted on a bare kitchen wall before cabinets are installed, studs and pipe clamps visible, daylight" + _SFX),
    ("Villa i Märsta med sadeltak",
     "full-bleed photo filling the whole frame, 1970s Swedish suburban single-storey villa with brown wooden panel facade, low pitched concrete tile roof, small lawn and hedge, quiet residential street, summer, no borders" + _SFX),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"koksrenovering-vallingby.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Vällingby", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Vällingby – kök i 1950-talets ABC-stad",
  "description": "Köksrenovering i Vällingby: kök i lägenheter och radhus från 1950-talet, styrelsens tillstånd, imkanal och sotare, hyresrätt och rotavdrag.",
  "h1": "Köksrenovering i Vällingby",
  "lead": "Vällingby byggdes under 1950-talet som en ABC-stad, där vardagen skulle vara rationell och nära till allt. I bostadsrätterna krävs styrelsens tillstånd när ledningar och ventilation ändras. Geal Entreprenad AB renoverar kök i lägenheter och radhus i Vällingby och tar fram underlaget till föreningen.",
  "card": "Kök i lägenheter och radhus.",
  "sections": [
    {"id": "abc-vallingby", "anchor": "ABC-staden",
     "h2": "Landets första ABC-stad",
     "paras": [
       "Översiktsplanens riksintressedel beskriver Vällingby–Råcksta som landets första ABC-stad, med arbete, bostäder och centrum. Ingen skulle ha längre än 900 meters gångväg från bostaden till tunnelbanan. I det sociala programmet ingick tankar om en blandad befolkning och lättillgänglighet, som också skulle skapa en rationell vardag för arbetande kvinnor. Området byggdes ut under 1950-talet. Stadens vägledning Varsam utveckling av småhus- och villaområden berättar att Vällingby invigdes 1954 och att bostäderna placerades i fallande skala runt centrum, med högre hus närmast och grupper av rad- och kedjehus längst ut.",
       "Till det värdebärande räknar riksintressedelen de ursprungliga husens gestaltning och detaljer som fönster, entrépartier, balkonger och räcken – alltså exteriören. Köken inne i lägenheterna nämns inte, men en lägenhet kan ändå ha kulturhistoriska värden som föreningen behöver ta hänsyn till.",
     ],
     "aside": {"title": "Vällingby–Råcksta (AB 120)", "items": [
       "Landets första ABC-stad", "Byggd under 1950-talet", "Högst 900 m till tunnelbanan", "Riksintresse för kulturmiljövården"]}},
    {"id": "foreningen-vallingby", "h2": "Styrelsens tillstånd",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 2 076 bostadsrätter i Vällingby, varav 228 i småhus, och 1 551 i Råcksta. Bostadsrättslagen säger att bostadsrättshavaren inte får utföra vissa åtgärder utan styrelsens tillstånd: ingrepp i en bärande konstruktion, installation eller ändring av ledningar för avlopp, värme, gas eller vatten, installation eller ändring av ventilation, ändring av eldstad eller rökkanal och annan väsentlig förändring av lägenheten.",
       "Har lägenheten särskilda kulturhistoriska värden krävs dessutom tillstånd för varje åtgärd som påverkar de värdena. Ett kök där diskbänken flyttas eller ventilationen ändras kan beröra flera av punkterna. Vi tar fram en ritning och en skriftlig beskrivning som styrelsen kan ta ställning till innan vi börjar.",
     ],
     "aside": {"title": "Kräver styrelsens tillstånd", "items": [
       "Ingrepp i bärande konstruktion", "Ändrade vatten- och avloppsledningar", "Ändrad ventilation", "Annan väsentlig förändring"]}},
    {"id": "imkanal-vallingby", "h2": "Imkanalen och sotaren",
     "paras": [
       "Stockholms stad påminner om att ventilationskanalens sammanlagda mått måste räcka om badrumskanalen ska användas som kombinerad imkanal för köket och frånluftskanal för badrummet. Ett kök behöver tillräcklig frånluft och ska uppfylla kraven för imkanal. Staden råder att man tidigt pratar med skorstensfejarmästaren om en ny eller ändrad kanal.",
       "Staden beskriver också att äldre hus ofta har självdrag, där luften sugs ut genom skorstenskanalen i kök och badrum, medan frånluft med centrala fläktar blev vanlig i hus byggda 1961–1975. I ett hus från 1950-talet tar vi därför reda på vilket system som finns innan fläkten väljs.",
     ],
     "aside": None},
    {"id": "hyresratt-vallingby", "h2": "Hyresrätt, bostadsrätt eller radhus",
     "paras": [
       "Vällingby har också 1 498 lägenheter i allmännyttan och 597 hos privata hyresvärdar. Staden skriver att du som hyresgäst normalt inte får flytta kök eller badrum. Bor du i bostadsrätt behöver du kontakta styrelsen innan du planerar en flytt.",
       "I de 220 småhusen med äganderätt bestämmer du själv, men en anmälan kan behövas om bärande väggar, brandskydd eller ventilationen ändras. Mer om tjänsten finns under " + _L.format("koksrenovering.html", "köksrenovering") + ", och om golven finns " + _L.format("golvslipning-vallingby.html", "golvslipning i Vällingby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi kök i Vällingby",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter och tittar på kanaler och stammar."),
    ("Underlag", "Ritning och beskrivning till styrelsen."),
    ("Tillstånd", "Styrelsen eller kommunen ger klartecken."),
    ("Rivning", "Skåp, ytskikt och gamla installationer bort."),
    ("Installationer", "El, vatten, avlopp och imkanal."),
    ("Montage", "Skåp, bänkskiva och vitvaror."),
  ],
  "rot_h2": "ROT-avdrag för kök i Vällingby",
  "rot": [
    "I en bostadsrätt ger Skatteverket rotavdrag för att montera fast köksinredning och installera vitvaror i samband med byggarbetet, för att riva innerväggar och bygga om planlösningen och för att byta köksluckor. Arbetet ska göras innanför lägenhetens tak, väggar och golv och gälla något du ansvarar för enligt stadgarna. I ett radhus med äganderätt gäller motsvarande regler för småhus.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset på ett kök i Vällingby?",
  "price": [
    "Kökets storlek och planlösning, om diskbänk eller spis flyttas, nya ledningar och kanaler, underlag till föreningen, skåp, bänkskivor och vitvaror. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste styrelsen godkänna min köksrenovering i Vällingby?",
     "Ja, om du ändrar vatten- eller avloppsledningar, ventilationen eller bärande delar. Det följer av bostadsrättslagen 7 kap. 7 §."),
    ("Får jag flytta köket i min hyreslägenhet i Råcksta?",
     "Normalt inte. Stockholms stad skriver att hyresgäster normalt inte får göra den typen av ändringar."),
    ("Kan köksfläkten kopplas till badrummets ventilationskanal?",
     "Bara om kanalens sammanlagda mått räcker och kraven på imkanal uppfylls. Staden råder att man pratar med sotaren först."),
    ("Är köken i Vällingby skyddade av riksintresset?",
     "Riksintressedelen räknar upp exteriöra detaljer som fönster och entréer. Föreningen kan ändå behöva ta hänsyn till kulturvärden i lägenheten."),
  ],
  "sources": [_RIKS, _VARSAM, _of("Vällingby", "vasterort/hasselby-vallingby/vallingby"), _of("Råcksta", "vasterort/hasselby-vallingby/racksta"),
              _BRL, _STH_KOK, _STH_VENT, _SKV],
  "cta": ("Planerar du ett nytt kök i Vällingby?", "Boka ett gratis platsbesök, så tar vi fram underlaget till styrelsen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Kök i en 1950-talslägenhet med ljusa luckor",
     "renovated kitchen in a 1950s Swedish apartment with pale green flat cabinet doors, light wooden worktop, small window above the sink, original proportions, empty room, daylight" + _SFX),
    ("Lamellhus från 1950-talet i en grön förort",
     "three-storey 1950s Swedish apartment buildings in light plaster with small balconies, set among lawns and pine trees in a planned suburb, footpath, overcast daylight, no people" + _SFX),
    ("Kökshörna med nya ledningar inför montage",
     "kitchen corner during renovation with new water and drain connections for a dishwasher and sink coming out of a freshly painted wall, cabinets not yet installed, protective floor covering, daylight" + _SFX),
  ],
},
}
