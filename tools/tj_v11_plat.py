# -*- coding: utf-8 -*-
"""Plåtslagare – ortsidor v11: Norrtälje, Botkyrka, Järfälla, Vallentuna, Sigtuna, Upplands Väsby (2026-10-25).
Orterna valda efter antal bostäder i småhus 2025 (SCB BO0104T04): Norrtälje 19 171, Botkyrka 12 582,
Järfälla 11 489, Vallentuna 9 300, Sigtuna 7 571, Upplands Väsby 7 065.
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
  Norrtälje kommun / Räddningstjänsten (Taksäkerhet, granskad 2025-09-11; Brandskyddskontroll av eldstad),
  Boverket (PBL kunskapsbanken: Taksäkerhet, BFS 2024:9 2 kap. 15–24 §§),
  Botkyrka kommun (Dagvatten, uppd. 2025-12-03; Strategi och riktlinjer för dagvatten, folder; Vattenskydds-
  områden, uppd. 2026-06-24; Anslutning av ett attefallshus (komplementbyggnad); Solceller, solfångare och
  solpaneler – energisidan och bygglov A–Ö),
  Järfälla kommun (Dagvatten och länshållningsvatten; Rekommendationer för dag- och dränvattenhantering, VA- &
  avfallsavdelningen feb 2017; Miljö- och hälsoskyddsenhetens faktablad nr 16 Dagvatten, rev. sep 2025),
  Vallentuna kommun (Dagvatten; Dagvattenstrategi KF 2024-12-02 § 172; Landsbygd; Fasadändring; Nybyggnad av
  komplementbyggnad),
  Sigtuna kommun (Riktlinjer för bebyggelseutveckling i dalgången mellan Odensala och Hova, BTN 2020-12-15 § 163;
  Tak – ändra befintlig byggnad), Sigtuna Vatten & Renhållning (Dagvatten; broschyren Dagvatten på din fastighet,
  Oxunda vattensamverkan 2018),
  Upplands Väsby kommun (Vattentjänstplan KF 2024-11-11; Dagvatten; Ledningsnät, anslutning till fastighet;
  Vattenskyddsområde),
  SCB (BO0104T04) och Skatteverket (Ger arbetet rätt till rotavdrag? – privat; Så fungerar rotavdraget).
Strukna (ej verifierade eller oklara i källan): Norrtäljes sotningsintervall (redan på köksrenoveringssidan,
inte upprepat), krav på snörasskydd för befintliga villor (Boverket 24 § gäller entréer vid nybyggnad och får
anpassas vid ändring – texten säger bara det), att glidskydd och takstegar ger rotavdrag (Skatteverkets lista
nämner dem inte), Botkyrkas skyddsföreskrifter för Tullinge och Segersjö i detalj (föreskrifterna ej öppnade –
bara kommunsidans sammanfattning används), att Botkyrkas solcellsregler är aktuella efter 1 december 2025
(kommunen varnar själv att informationen kan vara inaktuell – texten säger det), Järfällas nuvarande nivå på
reducerad dagvattenavgift (bara rekommendationsskriftens hänvisning till taxan), innehållet i Järfällas faktablad
nr 09 om högtryckstvätt (hittades inte), plåttak på Vallentunas gårdar och kulturmiljöprogram (ingen källa
öppnad – inga påståenden om lokala tak), Lindholmens kulturmiljöanalys (pdf gick inte att hämta), flygbuller och
Arlanda i Sigtuna (finns redan på takrenoverings-/takläggarsidan och rör inte plåten), att Väsbys broschyr är
identisk med Oxundas (används bara för Sigtuna), skyddsföreskrifterna för Hammarby reservvattentäkt i detalj,
VA-taxornas belopp. Inga priser, garantier, omdömen, egna uppdrag eller cert.
Kritikpass 2026-10-25: Norrtälje-ingressens 'flest småhus i länet' struken (bara sex orters SCB-tal kontrollerade),
radhus/kedjehus/souterräng som beskrivning av Järfällas och Väsbys bestånd struket ur ingresserna (ingen öppnad källa),
Botkyrkas 'gäller även ombyggd komplementbyggnad' rättat till 'kontakta VA-enheten', solcellsundantagen tillskrivna
bygglovssidan (inte energisidan), slutsatsen 'därför vill kommunen ha mer vatten på tomten' ersatt med kommunens egen
formulering, rotavdragets undantag för lantbruksbyggnader i Sigtuna struket (Skatteverket säger det inte).
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py."""

_L = '<a class="text-link" href="{0}">{1}</a>'

_SCB = ("SCB – Antal lägenheter efter region, hustyp och upplåtelseform (BO0104), 2025",
        "https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BO__BO0104__BO0104D/BO0104T04/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_BV_TAKSAK = ("Boverket – Taksäkerhet (PBL kunskapsbanken)",
              "https://www.boverket.se/sv/PBL-kunskapsbanken/regler-om-byggande/sakerhet-anvandning/taksakerhet/")
_NT = "https://www.norrtalje.se/info/trygghet-sakerhet/raddningstjansten/"
_BK = "https://www.botkyrka.se/boende-och-narmiljo/"
_JF = "https://www.jarfalla.se/"
_VT = "https://vallentuna.se/bygga-bo-och-miljo/"
_SG = "https://www.sigtuna.se/"
_UV = "https://www.upplandsvasby.se/bygga-bo-och-miljo/vatten-och-avlopp/"

PAGES_TJ = {

# ------------------------------------------------------------------ NORRTÄLJE
"platslagare-norrtalje.html": {
  "kind": "district", "service": "platslagare", "ort": "Norrtälje", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Norrtälje – takstege, glidskydd och skorsten",
  "description": "Plåtslagare i Norrtälje: takskydd som räddningstjänsten kräver vid sotning, glidskydd som inte får sitta i hängrännan och plåten kring skorstenen.",
  "h1": "Plåtslagare i Norrtälje",
  "lead": "Norrtälje kommun har drygt 19 000 bostäder i småhus enligt SCB. Har huset en eldstad ska skorstenen sotas och kontrolleras, och då ska vägen upp på taket vara säker, och den vägen går över plåt: takfot, hängränna, takstege och skorstensbeslag. Geal Entreprenad AB utför plåtarbeten och monterar takskydd på villor och fritidshus i Norrtälje kommun, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Takskydd, rännor och skorstensplåt i Norrtälje.",
  "sections": [
    {"id": "taksakerhet-norrtalje", "anchor": "Taksäkerhet för sotaren",
     "h2": "Kontrollanten går upp på cirka 45 tak i veckan",
     "paras": [
       "I Norrtälje kommun är det räddningstjänsten som gör brandskyddskontrollen av eldstäder. Enligt räddningstjänsten går en brandskyddskontrollant upp på cirka 45 tak varje vecka, och därför behöver det finnas takskyddsanordningar hela vägen från marken till skorstenen. Uppstigningsanordningarna ska vara godkända och monterade enligt produktens installationsanvisning.",
       "Uppfyller takskyddet inte kraven kan räddningstjänsten inte genomföra hela kontrollen. Fastighetsägaren får då en ny tid för att slutföra kontrollen ovan tak. Vilka krav som kan ställas på en fastighet bestäms av Boverkets föreskrifter, skriver räddningstjänsten.",
       "Boverket nämner just skorstenen som exempel på ett fast arbetsställe på taket: den måste sotas regelbundet för att det ska vara tillåtet att elda, och sotaren behöver kunna ta sig upp, förflytta sig till skorstenen och arbeta där på ett säkert sätt. För oss betyder det att takskyddet hör ihop med plåtarbetet. Byts hängrännor, takfotsplåt eller skorstensbeslag är det rätt tillfälle att se över fästpunkterna för stege och glidskydd. Mer om utrustningen finns under " + _L.format("taksakerhet-snorasskydd.html", "taksäkerhet och snörasskydd") + ".",
     ],
     "aside": {"title": "Vägen till skorstenen", "items": [
       "Markstege eller fasadstege", "Glidskydd vid takfoten",
       "Takstege eller taksteg", "Takbrygga vid nocken"]}},
    {"id": "glidskydd", "h2": "Glidskyddet får inte sitta i hängrännan",
     "paras": [
       "Den som går upp på taket från utsidan ska enligt räddningstjänsten alltid ha ett glidskydd fast monterat vid takfoten, så att markstegen inte kan glida åt sidan eller bakåt. Glidskyddet ska sitta i en fast del av byggnaden, helst precis intill takstegen, och vara certifierat enligt standarden SS 831342:2014.",
       "Räddningstjänsten är tydlig på en punkt som rör plåtslagaren direkt: glidskyddet får inte monteras i hängrännan, eftersom rännan inte klarar vikten som krävs, minst 150 kilo. Många fallolyckor sker just där markstegen möter taket. När vi monterar nya rännor placerar vi därför rännkrokarna så att glidskyddet kan fästas i takfoten bredvid, och inte på rännan.",
       "Markstegen ska följa standarden SS-EN 131, vara av lättmetall eller annat lätt material och väga högst 20 kilo. En lös markstege får användas om fasaden är högst 4 meter. Mellan 4 och 8 meter bör det i stället finnas en fast fasadstege eller en taklucka inifrån, och över 8 meter ska uppgången alltid vara invändig via taklucka.",
     ],
     "aside": None},
    {"id": "takstege", "h2": "Takstege, takbrygga och skorstensstege",
     "paras": [
       "Lutar taket mer än 6 grader måste det enligt räddningstjänsten finnas en fast takstege eller separata taksteg mellan uppgången och skorstenen. Takstegen ska sitta fast med minst fyra infästningar, upptill och nedtill, i byggnadens bärande delar. En stege som bara är fäst upptill eller hänger löst över nocken är inte tillåten och måste bytas eller monteras fast innan den används igen.",
       "Lösa taksteg ska ligga i en rak linje och monteras enligt tillverkarens anvisningar. Är det mer än 1 meter i sidled från uppgången till skorstenen ska en takbrygga monteras vid nocken. Står skorstenen mer än 1,2 meter över arbetsstället på taket behövs dessutom en skorstensstege eller en arbetsplattform.",
       "Varje infästning genom taket är en möjlig läckagepunkt. På ett plåttak tätar vi genomföringarna så att vattnet fortsätter att rinna förbi, och på ett tegeltak sätts infästningarna i läkt och underlag enligt tillverkarens anvisning. Ska taket ändå läggas om kan takskyddet planeras samtidigt, se " + _L.format("takbyte-norrtalje.html", "takbyte i Norrtälje") + ".",
     ],
     "aside": {"title": "Räddningstjänstens mått", "items": [
       "Takstege vid mer än 6 graders lutning", "Minst fyra infästningar",
       "Takbrygga över 1 meter i sidled", "Skorstensstege över 1,2 meter"]}},
    {"id": "skorsten-norrtalje", "h2": "Plåten runt skorstenen och snön vid entrén",
     "paras": [
       "Vid brandskyddskontrollen tittar räddningstjänsten bland annat på eldstaden, skorstenen, taket och byggnadsdelar som ligger nära. Inför besöket ber man fastighetsägaren att kontrollera att glidskyddet sitter fast, att vindsluckan går lätt att öppna och att vägen till skorstenen är fri om den går genom vinden.",
       "Skorstensbeslaget, alltså plåten som leder vattnet runt skorstenen och ner på taket, slits av väder och rörelser i taket. Ett beslag som släppt syns ofta som fukt på vinden kring murstocken. Vi byter eller kompletterar beslaget och kan klä in en sliten skorstenskrona i plåt. Behöver själva murstocken lagas finns mer under " + _L.format("skorstensrenovering.html", "skorstensrenovering") + ".",
       "Boverkets föreskrifter kräver också skyddsanordningar mot fallande is och snö vid byggnaders entréer om det finns särskilda risker för personskador. Kraven gäller vid nybyggnad och får anpassas när en befintlig byggnad ändras. Vi tar upp frågan på platsbesöket när taket lutar mot entrén. Allmänt om plåtarbeten finns på sidan " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåt- och takskyddsjobb i Norrtälje till",
  "steps": [
    ("Vägen upp", "Vi går igenom uppgången, glidskyddet, takstegen och vägen till skorstenen enligt räddningstjänstens lista."),
    ("Plåten", "Rännor, takfotsplåt, skorstensbeslag och genomföringar kontrolleras samtidigt."),
    ("Kostnadsförslag", "Plåtarbete och takskydd redovisas som skilda poster i ett skriftligt kostnadsförslag."),
    ("Montering", "Takskyddet fästs i bärande delar och plåten monteras med tätade infästningar."),
    ("Genomgång", "Vi visar var glidskydd och stege sitter, så att du kan förbereda nästa brandskyddskontroll."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Norrtälje",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus, även ett fritidshus, att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör, att mura och reparera skorstenar och att montera och montera ner byggnadsställningar i samband med rotarbetet.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Norrtälje?",
  "price": [
    "Takets höjd och lutning, hur långt det är från uppgången till skorstenen, om takskydd ska nymonteras eller bara kompletteras, skick på rännor och skorstensbeslag och vilken ställning som behövs. Restiden till kust och skärgård räknas in. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får glidskyddet för stegen hakas fast i hängrännan?",
     "Nej. Räddningstjänsten i Norrtälje skriver att glidskyddet inte får monteras i hängrännan, eftersom rännan inte klarar minst 150 kilo. Det ska sitta i en fast del av byggnaden vid takfoten."),
    ("Vad händer om takskyddet inte godkänns vid brandskyddskontrollen?",
     "Då kan räddningstjänsten inte genomföra hela kontrollen. Fastighetsägaren får en ny tid för att slutföra kontrollen ovan tak när takskyddet är åtgärdat."),
    ("När behövs en takbrygga vid nocken?",
     "Enligt räddningstjänsten när det är mer än 1 meter i sidled från uppgången eller takluckan till skorstenen."),
    ("Kan vi använda vår gamla trästege för att komma upp på taket?",
     "Nej. Räddningstjänsten skriver att markstegen inte får vara av trä eller järn, eftersom skador som röta och invändig rost är svåra att se. Den ska vara av lättmetall eller annat lätt material och följa SS-EN 131."),
    ("Kan ni montera takstege samtidigt som ni byter skorstensbeslaget?",
     "Ja. Vi planerar takskydd och plåt i samma uppdrag, så att infästningarna tätas en gång och ställningen bara behövs en gång."),
  ],
  "sources": [
    ("Norrtälje kommun – Räddningstjänsten: Taksäkerhet", _NT + "privatperson/taksakerhet/"),
    ("Norrtälje kommun – Räddningstjänsten: Brandskyddskontroll av eldstad", _NT + "privatperson/din-eldstad/brandskyddskontroll-av-eldstad/"),
    _BV_TAKSAK, _SCB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska takskydd eller skorstensplåt ses över i Norrtälje?", "Boka ett gratis platsbesök så går vi igenom vägen till skorstenen och plåten på taket."),
  "img": [
    ("Röd trävilla i Roslagen med svart plåttak, vit skorsten och stuprör",
     "traditional falu red wooden house in Roslagen near Norrtälje Sweden, black standing-seam metal roof with a black steel roof ladder running from the eaves up to a white rendered brick chimney with a black sheet-metal chimney flashing, black half-round gutter and downpipe, birch and pine trees, overcast autumn daylight, photorealistic, no people, no text"),
    ("Svart takstege på tegeltak ovanför hängrännan vid takfoten",
     "close-up view up a dark grey concrete tile roof on a Swedish house: a black steel roof ladder with flat rungs fixed to the roof runs from the eaves up toward the ridge, at the bottom edge a black metal half-round gutter on gutter hooks, simple realistic construction, overcast daylight, photorealistic detail, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ BOTKYRKA
"platslagare-botkyrka.html": {
  "kind": "district", "service": "platslagare", "ort": "Botkyrka", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Botkyrka – takvatten, vattenskydd, solceller",
  "description": "Plåtslagare i Botkyrka: takvatten som inte får störa grannen, stenkista i Tullinge och Segersjö vattenskyddsområden, rännor på gäststugan och solceller.",
  "h1": "Plåtslagare i Botkyrka",
  "lead": "I Botkyrka finns drygt 12 500 bostäder i småhus enligt SCB. Det vatten som rinner av taken är fastighetsägarens ansvar ända tills det har lämnat tomten, och i stora delar av kommunen ligger tomten dessutom i ett vattenskyddsområde. Geal Entreprenad AB byter hängrännor, stuprör och beslag och lägger plåttak på villor och radhus i Botkyrka, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Rännor, stuprör och plåttak i Botkyrka.",
  "sections": [
    {"id": "takvatten-botkyrka", "anchor": "Takvattnet i Botkyrka",
     "h2": "Ditt takvatten får inte bli grannens problem",
     "paras": [
       "Botkyrka kommun beskriver dagvatten som regn- och smältvatten från tak, vägar och parkeringsplatser, och skriver att vattnet i första hand ska hanteras så nära källan som möjligt. Den som äger fastigheten har ett ansvar för att dagvattnet från den egna tomten inte påverkar närliggande fastigheter.",
       "Kommunen har en strategi och riktlinjer för dagvatten som riktar sig till alla fastighetsägare. Enligt kommunens folder finns 14 dagvattendammar i Botkyrka, där vattnet renas innan det når sjöarna, men vid extremväder hinner vattnet inte stanna i dammarna och belastningen på ledningarna ökar. Åtgärder som fördröjer vattnet är därför viktiga, skriver kommunen.",
       "För plåtslagaren börjar frågan vid stupröret. En ränna som rinner över vid kraftigt regn, ett stuprör som slutar mot grannens tomtgräns eller en utkastare som leder vattnet mot en hårdgjord uppfart skickar vattnet åt fel håll. Vid platsbesöket följer vi vattnet från takfoten till marken och föreslår var det kan ledas ut på gräs eller rabatt. Allmänt om rännor finns under " + _L.format("hangrannor-stupror.html", "hängrännor och stuprör") + ".",
     ],
     "aside": {"title": "Kommunens grundregler", "items": [
       "Ta hand om vattnet nära källan", "Påverka inte grannens tomt",
       "Ny anläggning inom detaljplan anmäls", "Särskild hänsyn i vattenskyddsområde"]}},
    {"id": "vattenskydd-botkyrka", "h2": "Stenkista i Tullinge eller Segersjö vattenskyddsområde",
     "paras": [
       "Botkyrka har sex vattenskyddsområden: Tullinge, Segersjö, Östra Mälaren, Bornsjön, Pålamalm och ett på Näslandet. Kommunen skriver att de största är Tullinge och Segersjö samt Östra Mälarens vattenskyddsområde, som omfattar stora delar av norra Botkyrka. Inom dessa är det särskilt viktigt att förorenat dagvatten hanteras så att yt- och grundvatten inte påverkas.",
       "Vill du leda stuprören till en stenkista eller ett magasin i marken spelar läget roll. Kommunen skriver att mindre grävningsarbeten på tomten är tillåtna, men att större schaktarbeten inom vattenskyddsområdet kräver tillstånd från miljö- och hälsoskyddsnämnden, som är tillståndsmyndighet för Tullinge och Segersjö. För de övriga områdena hänvisar kommunen till Länsstyrelsen respektive SYVAB.",
       "Ska en ny dagvattenanläggning inrättas inom detaljplanelagt område ska den enligt kommunen anmälas, och exempel på en sådan anläggning är en damm, ett anlagt dike eller en dagvattenledning. Vi lägger rännor och stuprör och ser till att vattnet kommer rätt ut från huset. Grävning och anläggning i marken planeras med dig, och vi kontrollerar först om fastigheten ligger i ett skyddsområde.",
     ],
     "aside": None},
    {"id": "gaststuga-botkyrka", "h2": "Ny gäststuga eller tillbyggnad – rännorna räknas också",
     "paras": [
       "Enligt kommunens riktlinjer gäller vid ny- och ombyggnad som ökar byggnadsarean att allt vatten från hårdgjorda ytor på kvartersmark ska ledas till lokala dagvattenanläggningar som kan fördröja de första 20 millimetrarna regn. Ett nytt tak är en sådan hårdgjord yta, även om det är litet.",
       "För en komplementbostad eller ett attefallshus skriver kommunens VA-enhet att dag- och dräneringsvatten inte får kopplas till kommunens spillvattenledning. Den nya spillvattenledningen ska kopplas på befintlig spillvattenledning inom tomten, men vattnet från stugans tak ska alltså ta en annan väg. Bygger du om en befintlig komplementbyggnad ska du enligt kommunen kontakta VA-enheten.",
       "En liten stuga med plåttak får ofta en egen ränna med ett stuprör på ena sidan. Vi placerar stupröret där vattnet kan ledas ut på gräs, långt från både stugans och huvudbyggnadens grund, och väljer ränndimension efter takytan. Läs mer om stommen och lovreglerna på sidan om " + _L.format("attefallshus.html", "attefallshus") + ".",
     ],
     "aside": {"title": "Vid tillbyggnad i Botkyrka", "items": [
       "Fördröj de första 20 mm regn", "Inget takvatten till spillvattnet",
       "Eget stuprör på stugan", "Utkastare mot gräs, inte uppfart"]}},
    {"id": "solceller-botkyrka", "h2": "Solceller på plåttaket – vad kommunen skriver",
     "paras": [
       "På kommunens energisida står att solcellspaneler och solfångare inte kräver bygglov, även om byggnadens utseende påverkas avsevärt, förutsatt att de följer byggnadens form. Enligt kommunens bygglovssidor är undantagen om detaljplanen kräver lov, om byggnaden eller området är särskilt värdefullt från historisk eller kulturhistorisk synpunkt eller om fastigheten ligger i ett område av betydelse för totalförsvaret. Berör anläggningen bärande konstruktion eller brandskydd krävs anmälan. Kommunen påpekar själv att delar av bygglovsinformationen kan vara inaktuell efter lagändringarna den 1 december 2025.",
       "Ett falsat plåttak passar bra för solceller, eftersom fästena kan klämmas på falsen utan att plåten genomborras. Är plåten gammal är det klokt att byta den först, så att panelerna inte behöver demonteras när taket ska läggas om. Mer om plåttak i allmänhet finns under " + _L.format("plattak.html", "plåttak") + ", och om takets skick under " + _L.format("takrenovering-botkyrka.html", "takrenovering i Botkyrka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtjobb i Botkyrka till",
  "steps": [
    ("Vattnets väg", "Vi ser var varje stuprör slutar och om vattnet rinner mot grannen, uppfarten eller en grönyta."),
    ("Skyddsområde", "Vi kontrollerar om tomten ligger i ett vattenskyddsområde innan något grävs."),
    ("Kostnadsförslag", "Rännor, stuprör, plåttak och eventuella solcellsfästen redovisas som egna poster."),
    ("Montering", "Gammal plåt tas ner, underlaget kontrolleras och ny plåt monteras med rätt fall."),
    ("Kontroll", "Vid genomgången visar vi var vattnet leds ut och hur rännorna hålls rena."),
  ],
  "rot_h2": "Rotavdrag för plåtarbetet i Botkyrka",
  "rot": [
    "I ett småhus ger det rotavdrag att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör, och att montera ställning i samband med arbetet. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr för rot och rut sammanlagt.",
    "Bor du i bostadsrätt ger byte av plåttak, hängrännor och stuprör inget rotavdrag enligt Skatteverket. Material ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Botkyrka?",
  "price": [
    "Takytan, hur många stuprör och ränndalar huset har, om plåttaket byts helt eller bara rännor och beslag, vilken ställning som behövs och om en gäststuga eller tillbyggnad ska få egen avvattning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi leda stupröret från gäststugan till avloppet i Botkyrka?",
     "Nej. Kommunens VA-enhet skriver att dag- och dräneringsvatten inte får kopplas till kommunens spillvattenledning. Vattnet från stugans tak behöver tas om hand på annat sätt, till exempel på gräsytan."),
    ("Behöver vi tillstånd för en stenkista i Tullinge vattenskyddsområde?",
     "Mindre grävningsarbeten är tillåtna enligt kommunen, men större schaktarbeten kräver tillstånd från miljö- och hälsoskyddsnämnden. Fråga kommunen innan magasinet planeras."),
    ("Vad menar Botkyrka med att de första 20 millimetrarna regn ska fördröjas?",
     "Det är kommunens riktlinje vid ny- och ombyggnad som ökar byggnadsarean. Vattnet från hårdgjorda ytor ska ledas till en lokal anläggning som kan hålla kvar den första regnmängden."),
    ("Kräver solceller på plåttaket bygglov i Botkyrka?",
     "Kommunen skriver att det normalt inte krävs om panelerna följer byggnadens form, med undantag för bland annat kulturhistoriskt värdefulla miljöer, detaljplaner med krav och totalförsvarets områden."),
    ("Ger byte av stuprör rotavdrag om vi bor i bostadsrätt i Botkyrka?",
     "Nej. Skatteverket anger att byte av plåttak, hängrännor och stuprör inte ger rotavdrag i en bostadsrätt. I ett småhus ger arbetet avdrag."),
  ],
  "sources": [
    ("Botkyrka kommun – Dagvatten", _BK + "vatten-och-avlopp/sa-tar-du-hand-om-vattnet/dagvatten"),
    ("Botkyrka kommun – Strategi och riktlinjer för dagvatten (folder, pdf)",
     "https://www.botkyrka.se/download/18.66a36a071808e5250f7743f/1652862058877/Strategi%20och%20riktlinjer%20f%C3%B6r%20dagvatten.pdf"),
    ("Botkyrka kommun – Vattenskyddsområden", _BK + "utomhusmiljo/vattenskyddsomraden"),
    ("Botkyrka kommun – Anslutning av ett attefallshus (komplementbyggnad)",
     _BK + "vatten-och-avlopp/anslut-till-vatten-och-avlopp/anslutning-av-ett-attefallshus-komplementbyggnad"),
    ("Botkyrka kommun – Solceller, solfångare och solpaneler",
     _BK + "bostad-och-tradgard/energi-och-uppvarmning/solceller-solfangare-och-solpaneler"),
    ("Botkyrka kommun – Bygglov A–Ö: Solceller, solfångare och solpaneler",
     _BK + "bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/solceller"),
    _SCB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska rännor eller plåttak bytas i Botkyrka?", "Boka ett gratis platsbesök så följer vi takvattnet från takfoten till tomten."),
  "img": [
    ("Gult radhus i Tullinge med grått plåttak, hängrännor och stuprör",
     "row of 1970s Swedish terraced houses in Tullinge Botkyrka with light yellow wooden panel facades, grey corrugated-profile metal roofs with matching grey half-round gutters and round downpipes ending on concrete splash blocks onto lawn, small front gardens with low hedges, pine forest behind, overcast autumn daylight, photorealistic, no people, no text"),
    ("Liten röd gäststuga med svart plåttak och eget stuprör mot gräsmattan",
     "small falu red Swedish guest cabin in a villa garden with a black standing-seam metal roof, a black half-round gutter along the eave and one black downpipe at the corner ending in a short outlet over a lawn, white window frames, birch tree, overcast daylight, photorealistic, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"platslagare-jarfalla.html": {
  "kind": "district", "service": "platslagare", "ort": "Järfälla", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Järfälla – stuprör, skärmtak och takvatten",
  "description": "Plåtslagare i Järfälla: om stupröret får gå till kommunens dagvattennät, utkastare som leder vattnet två meter ut och skärmtak över källartrappan.",
  "h1": "Plåtslagare i Järfälla",
  "lead": "Järfälla har knappt 11 500 bostäder i småhus enligt SCB. Där ett hus har källartrappa, garagenedfart eller entré under marknivå hittar regnvattnet lätt dit, och kommunen har skrivit ner hur takvattnet ska tas om hand för att undvika översvämmade källare. Geal Entreprenad AB byter hängrännor och stuprör, bygger skärmtak i plåt och tvättar och målar plåttak i Järfälla, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Stuprör, skärmtak och plåttak i Järfälla.",
  "sections": [
    {"id": "verksamhetsomrade", "anchor": "Får stupröret anslutas?",
     "h2": "Dagvatten gata eller dagvatten fastighet",
     "paras": [
       "I Järfälla är kommunen själv VA-huvudman, genom tekniska nämnden. Kommunens rekommendationer för dag- och dränvattenhantering slår fast att dag- och dräneringsvatten aldrig ska ledas till spillvattennätet. Vattnet ska hanteras inom den egna fastigheten eller ledas till det kommunala dagvattennätet, om ett sådant finns.",
       "Om det finns avgörs av vilket verksamhetsområde fastigheten ligger i. Kommunen har två: Dagvatten gata, där kommunen leder bort vatten från vägar och allmänna ytor, och Dagvatten fastighet, där kommunen också tar hand om dagvatten från privat fastighetsmark. Nästan alla bostäder ligger inom området för dricksvatten och spillvatten, men flera områden ligger utanför det kommunala dagvattenområdet, och där måste fastighetsägaren själv ta hand om dag- och dräneringsvattnet lokalt.",
       "Innan vi kopplar ett nytt stuprör till en ledning i marken frågar vi därför vart ledningen går. Ska fastigheten anslutas till kommunens dagvattennät ska vattnet enligt rekommendationerna först passera en brunn med sandfång, som behöver rensas med jämna mellanrum. Har huset en befintlig LOD-anläggning skriver kommunen att du ska kontakta den innan lösningen byggs bort eller ändras.",
     ],
     "aside": {"title": "Kommunens grundregler", "items": [
       "Inte till spillvattnet", "Dagvatten fastighet eller gata?",
       "Sandfång före anslutning", "Kontakta kommunen före ändring av LOD"]}},
    {"id": "utkastare-jarfalla", "h2": "Två meter ut från husväggen",
     "paras": [
       "Takvattnet bör enligt kommunen ledas bort från huset med utkastare och ränndalsplattor eller med ett rör, till en lämplig infiltrationsyta minst cirka 2 meter från huset där vattnet kan tas upp av växtlighet eller rinna ner i marken. Konstruktionen ska utformas så att vattnet leds bort från byggnaden och inte ger fuktskador.",
       "Marken närmast huset bör luta minst 15 centimeter på de första 3 metrarna ut från ytterväggen. Ytvatten får aldrig ledas till en annan fastighet utan ägarens godkännande, och du ansvarar för att inte leda vatten till grannar eller allmänna gator. Ibland behövs vallar eller rännor vid tomtgränsen. Samlar du takvattnet i en tunna ska vatten som svämmar över tunnans kant inte kunna skada byggnaden.",
       "På radhus och kedjehus sitter stuprören ofta tätt och ibland nära grannens entré. Vi placerar utkastare och nedre stuprörsdelar så att vattnet når en grönyta på den egna tomten, och kontrollerar att rännan har fall mot rätt stuprör. Mer om husen och taken i kommunen finns under " + _L.format("takrenovering-jarfalla.html", "takrenovering i Järfälla") + ".",
     ],
     "aside": None},
    {"id": "skarmtak-jarfalla", "h2": "Skärmtak över källartrappan och garagenedfarten",
     "paras": [
       "Kommunen pekar ut källartrappor och garagenedfarter som lågpunkter där regnvatten inte ska få rinna ner. Ett tak över trappan eller nedfarten hindrar att det regnar ner där, och i vissa fall kan en mindre vall stoppa ytvatten från andra ytor. Kan vattnet hållas borta behövs ingen spygatt, skriver kommunen. Finns det en spygatt ska den alltid vara ansluten till en pump.",
       "Ett skärmtak över en källartrappa är ett typiskt plåtjobb: ett litet tak med plåttäckning, en ränna och en avslutning mot fasaden som inte släpper in vatten bakom. Vattnet från skärmtaket får inte rinna ner i trappan igen, så stupröret leds ut åt sidan och vidare mot gräset, på samma sätt som från huvudtaket.",
       "I souterränghus ligger både entréer och garageportar ofta under marknivån på ena sidan. Kommunen skriver att den bästa lösningen är att inte ha garageportar och dörrar under marknivå. Går det inte att ändra planerar vi skärmtak, ränna och stuprör så att så lite vatten som möjligt når lågpunkten. Om badrum och källarplan i husen läser du under " + _L.format("badrumsrenovering-jarfalla.html", "badrumsrenovering i Järfälla") + ".",
     ],
     "aside": {"title": "Skydda lågpunkterna", "items": [
       "Tak över källartrappan", "Liten vall mot ytvatten",
       "Spygatt kopplad till pump", "Stupröret leds bort från trappan"]}},
    {"id": "tvatt-jarfalla", "h2": "Tvätta plåttaket utan att smutsa ner Bällstaån",
     "paras": [
       "Enligt kommunens faktablad om dagvatten, reviderat i september 2025, rinner en stor del av dagvattnet i Järfälla till Bällstaån, Mälaren, Översjön, Säbysjön eller Igelbäcken. Mälaren är vattentäkt för nästan hela Stockholmsregionen, och delar av kommunen ingår i Östra Mälarens vattenskyddsområde.",
       "Faktabladet tar upp tvätt av tak och fasader särskilt: vid tak- och fasadtvätt ska bästa möjliga teknik och tvättkemikalier användas, eftersom tvätt- och spolvatten annars följer med ner i dagvattenbrunnarna. Dagvatten från byggnader och byggarbetsplatser kan dessutom innehålla höga halter av bland annat metaller.",
       "Ska ett gammalt plåttak tvättas och målas om planerar vi därför var tvättvattnet tar vägen innan arbetet börjar, och rost och färgflagor samlas upp i stället för att spolas ner i rännan. Hur en takmålning går till finns under " + _L.format("takmalning.html", "takmålning") + ", och mer om plåtarbeten i allmänhet under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtjobb i Järfälla till",
  "steps": [
    ("Verksamhetsområde", "Vi tar reda på om fastigheten får ansluta takvattnet till kommunens dagvattennät eller ska ta hand om det själv."),
    ("Lågpunkter", "Källartrappor, garagenedfarter och entréer under mark gås igenom tillsammans med rännorna."),
    ("Kostnadsförslag", "Rännor, stuprör, skärmtak och eventuell tvätt och målning prissätts var för sig."),
    ("Montering", "Ny plåt monteras med fall mot rätt stuprör och utkastare som leder vattnet ut på gräset."),
    ("Kontroll", "Vid genomgången visar vi var vattnet hamnar och vilka brunnar och silar som ska rensas."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Järfälla",
  "rot": [
    "Skatteverket godkänner rotavdrag för att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör i ett småhus, och för att rengöra tak och hängrännor. Ställning som monteras i samband med arbetet räknas också.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år inom 75 000 kr för rot och rut tillsammans. Material ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Järfälla?",
  "price": [
    "Antalet stuprör och hur långt vattnet ska ledas ut, om ett skärmtak ska byggas över trappa eller nedfart, takets höjd på ett souterränghus och om plåttaket ska tvättas och målas. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur vet vi om vår fastighet i Järfälla får ansluta stupröret till kommunens dagvattennät?",
     "Det beror på om fastigheten ligger inom verksamhetsområdet Dagvatten fastighet. Flera områden ligger utanför, och där ska dag- och dräneringsvattnet tas om hand på tomten. Kommunen kan svara för just din fastighet."),
    ("Hur långt från huset ska takvattnet ledas i Järfälla?",
     "Kommunen rekommenderar att vattnet leds med utkastare, ränndalsplattor eller rör till en infiltrationsyta minst cirka 2 meter från huset."),
    ("Kan ett skärmtak hindra vatten i källartrappan?",
     "Ja. Kommunen skriver att tak över källartrappor och garagenedfarter hindrar att det regnar ner i lågpunkterna. Skärmtakets eget vatten måste då ledas bort från trappan."),
    ("Får vi spola av plåttaket med högtryck innan det målas?",
     "Kommunens faktablad om dagvatten anger att bästa möjliga teknik och tvättkemikalier ska användas vid tak- och fasadtvätt, så att föroreningar inte når dagvattnet. Vi planerar tvättvattnets väg innan vi börjar."),
    ("Vad gäller om huset har en stenkista eller annan LOD-anläggning?",
     "Fastighetsägaren ska sköta anläggningen så att den behåller sin funktion, och kommunen vill bli kontaktad innan lösningen byggs bort eller ändras."),
  ],
  "sources": [
    ("Järfälla kommun – Dagvatten och länshållningsvatten",
     _JF + "byggaboochmiljo/naturochmiljo/vattnetijarfalla/dagvatten.4.6f02e66014c5bd408d55babe.html"),
    ("Järfälla kommun – Rekommendationer för dag- och dränvattenhantering (2017, pdf)",
     _JF + "download/18.45afbeb115e342085253b794/1570022197012/rekommendationer-dagvattenhantering-2017-02-06.pdf"),
    ("Järfälla kommun – Faktablad nr 16: Dagvatten (rev. september 2025, pdf)",
     _JF + "download/18.5ca43d07198e5d9c20d68902/1758177095906/faktablad-16-dagvatten.pdf"),
    _SCB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Rinner takvattnet åt fel håll i Järfälla?", "Boka ett gratis platsbesök så går vi igenom rännor, stuprör och lågpunkter runt huset."),
  "img": [
    ("Kedjehus i Järfälla med rött tegeltak, hängrännor och stuprör i plåt",
     "row of 1970s Swedish linked houses (kedjehus) in Järfälla with dark brown wooden panel facades and red clay tile roofs, black metal half-round gutters and downpipes with outlets onto lawns, short driveways, pine trees, overcast autumn daylight, photorealistic, no people, no cars, no text"),
    ("Skärmtak i plåt över entrén och den utvändiga trappan på en tegelvilla",
     "exterior concrete stairs leading down below ground level along the wall of a light brick Swedish villa to a basement door, with a small sloping canopy roof of dark grey standing-seam sheet metal fixed to the wall directly above the stairwell, a small grey gutter on the canopy edge and a short downpipe leading water sideways onto lawn, metal railing around the stairwell opening, overcast day, photorealistic, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VALLENTUNA
"platslagare-vallentuna.html": {
  "kind": "district", "service": "platslagare", "ort": "Vallentuna", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Vallentuna – takvatten, uthus och plåttak",
  "description": "Plåtslagare i Vallentuna: kommunens dagvattenstrategi från 2024, regntunna och ränndal vid stupröret, plåt på uthus och garage och när nytt tak kräver lov.",
  "h1": "Plåtslagare i Vallentuna",
  "lead": "Vallentuna har omkring 9 300 bostäder i småhus enligt SCB, i tätorten och på en stor landsbygd, och på många tomter står också garage, förråd eller vedbod. Kommunfullmäktige antog i december 2024 en dagvattenstrategi som säger hur vatten från tak ska tas om hand. Geal Entreprenad AB byter hängrännor och stuprör, lägger plåttak och monterar beslag i Vallentuna, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Rännor, plåttak och uthus i Vallentuna.",
  "sections": [
    {"id": "strategi-vallentuna", "anchor": "Dagvattenstrategin",
     "h2": "Takvattnet enligt strategin från december 2024",
     "paras": [
       "Vallentunas dagvattenstrategi fastställdes av kommunfullmäktige den 2 december 2024. Den konkretiserar den dagvattenpolicy som gäller för alla kommuner inom Oxundaåns avrinningsområde och som tillämpas i hela Vallentuna. Strategin är skriven för kommunens egen planering, men den visar tydligt hur kommunen ser på vatten från tak.",
       "Tak och andra hårdgjorda ytor ska enligt strategin inte anslutas ofördröjt till allmän dagvattenledning. Takdagvattnet ska ledas ut på genomsläpplig markyta eller infiltreras och fördröjas på annat sätt före anslutning. Öppna lösningar som gräsytor, regnträdgårdar och diken ska väljas i första hand, och stängda lösningar som stenkistor i andra hand.",
       "Strategin skiljer också på olika slags dagvatten. Takdagvatten är inte lämpligt att blanda med orenat dagvatten från vägytor, eftersom vattnet från en väg innehåller mer föroreningar. För en villaägare betyder det att stupröret inte bör ledas mot uppfarten, där vattnet blandas med det som rinner av asfalten, utan mot en gräsyta.",
     ],
     "aside": {"title": "Strategin om takvatten", "items": [
       "Inte ofördröjt till ledningen", "Ut på genomsläpplig mark",
       "Öppna lösningar först", "Blanda inte med vägvatten"]}},
    {"id": "regntunna-vallentuna", "h2": "Regntunna, ränndal eller regnvattenspridare",
     "paras": [
       "På kommunens sida om dagvatten finns konkreta tips för villaägare. Ett enkelt sätt att bidra är att koppla stuprören till en eller flera regntunnor. Då rinner dagvattnet aldrig ner i brunnen och kan inte bidra till översvämning vid skyfall, och vattnet kan användas till bevattning när det är torrt.",
       "Kommunen föreslår också att vattnet från taket leds ut till gräsmatta och rabatter med ränndalar eller regnvattenspridare, och att uppfarter och gångar får genomsläppliga material som grus, singel, hålsten eller marksten med genomsläppliga fogar. En vanlig gräsmatta kan fördröja och rena vatten från taket.",
       "Vid stupröret är det plåtslagarens del som avgör om tipsen fungerar. Ett stuprör med en regnvattenavledare kan fylla tunnan och leda överskottet vidare ner i röret när tunnan är full, och den nedre delen kan avslutas med en utkastare mot en ränndal. Vi anpassar höjden efter tunnan och ser till att röret går att ta isär för rensning. Mer om rännor och stuprör finns under " + _L.format("hangrannor-stupror.html", "hängrännor och stuprör") + ".",
     ],
     "aside": None},
    {"id": "uthus-vallentuna", "h2": "Plåt på uthus, vedbod och garage",
     "paras": [
       "Kommunen beskriver en stor landsbygd med cirka 8 000 boende på landsbygderna och i de mindre orterna Lindholmen, Karby och Brottby, Kårsta, Ekskogen och Frösunda. På tomterna, både där och i tätorten, står ofta flera mindre byggnader. Kommunen räknar garage, carport, förråd, gäststuga, vedbod, växthus, bastu och båthus som komplementbyggnader.",
       "Inom detaljplan krävs bygglov om den sammanlagda ytan överstiger 45 kvadratmeter eller en enskild byggnad överstiger 30 kvadratmeter. Utanför detaljplan är gränserna 65 och 50 kvadratmeter, och nockhöjden får inte vara över 4 meter för att bygga utan lov. Inom ett kulturhistoriskt särskilt värdefullt område krävs alltid bygglov.",
       "Ett litet plåttak på en vedbod eller ett garage lever ofta ett hårdare liv än huvudtaket, med mossa, nedfallna grenar och rännor som ingen rensar. Vi byter plåt och rännor på befintliga komplementbyggnader och kan ge en ny vedbod eller bastu ett falsat eller profilerat plåttak med egen avvattning. Skatteverket skriver att komplementhus som garage och förråd kan höra till småhuset vid rotavdrag, men att det inte ges för att bygga en helt ny fristående byggnad som ett garage. Om snickeriet finns mer under " + _L.format("snickare-vallentuna.html", "snickare i Vallentuna") + ".",
     ],
     "aside": {"title": "Lovfritt komplement i Vallentuna", "items": [
       "Inom plan: 30 m² per byggnad, 45 m² totalt", "Utanför plan: 50 m² och 65 m²",
       "Nockhöjd högst 4 meter", "Lov krävs i värdefullt område"]}},
    {"id": "lov-vallentuna", "h2": "Nytt plåttak utan bygglov – med ett undantag",
     "paras": [
       "Enligt kommunen krävs inte bygglov för fasadförändringar som ommålning, nytt tak eller nya fönster på ett en- eller tvåbostadshus. Ändringen ska ändå göras varsamt och anpassas till byggnadens värden. Ligger fastigheten inom ett kulturhistoriskt särskilt värdefullt område, eller är byggnaden själv särskilt värdefull, krävs alltid bygglov.",
       "Krävs lov ska ansökan bland annat innehålla en fasadritning i skala 1:100 och en redovisning av utvändiga material och kulörer med NCS-koder. Byter du ett tegeltak mot plåt är det alltså bra att veta kulören tidigt. Äldre ritningar kan beställas ur kommunens arkiv. Om takets skick och omläggning i stort läser du under " + _L.format("takrenovering-vallentuna.html", "takrenovering i Vallentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtjobb i Vallentuna till",
  "steps": [
    ("Platsbesök", "Vi går igenom huvudtaket och tomtens mindre byggnader och ser var varje stuprör leder vattnet."),
    ("Vattnet på tomten", "Vi föreslår var takvattnet kan ledas ut på gräs, i regntunna eller mot ränndal."),
    ("Kostnadsförslag", "Hus, garage och uthus prissätts var för sig i ett skriftligt kostnadsförslag."),
    ("Montering", "Ny plåt och nya rännor monteras, med stuprörsdelar anpassade efter tunna eller utkastare."),
    ("Genomgång", "Vi visar hur rännor och avledare rensas inför vintern."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Vallentuna",
  "rot": [
    "Att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör på ett småhus ger rotavdrag. Arbetet ska utföras i bostaden eller på tomten i nära anslutning till den. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Regntunnor, plåt och annat material ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Vallentuna?",
  "price": [
    "Hur stor takytan är på huset och på de mindre byggnaderna, om plåten byts eller bara rännor och beslag, vilka stuprörsdelar som behövs för tunnor och utkastare och hur långt det är till fastigheten. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får stupröret i Vallentuna gå direkt till kommunens dagvattenledning?",
     "Kommunens dagvattenstrategi säger att tak inte ska anslutas ofördröjt till allmän dagvattenledning. Takvattnet ska i första hand ledas ut på genomsläpplig mark eller fördröjas innan det ansluts."),
    ("Kan vi koppla stupröret till en regntunna utan att tunnan svämmar över?",
     "Ja, med en regnvattenavledare på stupröret går överskottet vidare ner i röret när tunnan är full. Kommunen tipsar själv om regntunnor för att minska belastningen vid skyfall."),
    ("Behöver vi bygglov för att byta till plåttak på villan i Vallentuna?",
     "Nej, enligt kommunen krävs inte bygglov för nytt tak på ett en- eller tvåbostadshus, utom om fastigheten ligger i ett kulturhistoriskt särskilt värdefullt område eller byggnaden är särskilt värdefull."),
    ("Hur stor får en vedbod med plåttak vara utan bygglov utanför detaljplan?",
     "Enligt kommunen högst 50 kvadratmeter för en enskild byggnad och 65 kvadratmeter sammanlagt, med en nockhöjd på högst 4 meter."),
    ("Ger byte av plåten på garaget rotavdrag?",
     "Skatteverket skriver att komplementhus som garage och förråd kan höra till småhuset. Reparation och byte av plåt kan då ge avdrag, men inte att bygga ett helt nytt fristående garage."),
  ],
  "sources": [
    ("Vallentuna kommun – Dagvatten", _VT + "vatten-och-avlopp/dagvatten"),
    ("Vallentuna kommun – Dagvattenstrategi, KF 2024-12-02 (pdf)",
     "https://vallentuna.se/download/18.63572f8619eeecafce083a1/1782478399289/2.5.5%20Dagvattenstrategi.pdf"),
    ("Vallentuna kommun – Landsbygd", _VT + "planarbete-och-kartor/landsbygd"),
    ("Vallentuna kommun – Fasadändring", _VT + "bygglov-och-anmalan/behover-jag-bygglov/fasadandring"),
    ("Vallentuna kommun – Nybyggnad av komplementbyggnad", _VT + "bygglov-och-anmalan/behover-jag-bygglov/nybyggnad-av-komplementbyggnad"),
    _SCB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver rännor eller plåttak ses över i Vallentuna?", "Boka ett gratis platsbesök så går vi igenom huset och tomtens mindre byggnader på samma gång."),
  "img": [
    ("Gård i Vallentuna med vit villa, röd vedbod och garage med plåttak",
     "rural property in Vallentuna Uppland Sweden, white wooden villa with black metal roof and black gutters, next to it a small falu red woodshed and a red garage both with dark grey corrugated metal roofs and small gutters, open fields and a line of deciduous trees behind, overcast autumn daylight, photorealistic, no people, no text"),
    ("Stuprör i plåt med avledare till en regntunna vid husknuten",
     "corner of a white painted wooden Swedish house, a dark grey round metal downpipe with a small rainwater diverter fitting at mid height connected by a short pipe into the lid of a plain unbranded dark green rain barrel standing on a concrete slab, lower downpipe section ending in a curved outlet over a concrete splash block onto lawn, autumn leaves, overcast, photorealistic, plain surfaces without any logo or label, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SIGTUNA
"platslagare-sigtuna.html": {
  "kind": "district", "service": "platslagare", "ort": "Sigtuna", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Sigtuna – gårdar, matt plåt och takvatten",
  "description": "Plåtslagare i Sigtuna: kommunens råd om plåt i dalgången Odensala–Hova, matt och mörk plåt på stall och lador, och lövsil och magasin för takvattnet.",
  "h1": "Plåtslagare i Sigtuna",
  "lead": "Sigtuna kommun har drygt 7 500 bostäder i småhus enligt SCB, från villorna i Märsta och Rosersberg till gårdarna i dalgången mellan Odensala och Hova. På landsbygden har kommunen skrivit egna råd om när plåt passar och hur den bör se ut. Geal Entreprenad AB lägger plåttak, byter rännor och stuprör och monterar beslag i Sigtuna kommun, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Plåttak, rännor och beslag i Sigtuna.",
  "sections": [
    {"id": "dalgangen", "anchor": "Plåt i dalgången",
     "h2": "Lertegel och korrugerad plåt i dalgången Odensala–Hova",
     "paras": [
       "Bygg- och trafiknämnden antog i december 2020 riktlinjer för bebyggelseutveckling i dalgången mellan Odensala och Hova. Där beskrivs husen som präglar landskapet: parstugor med rödfärgad locklistpanel och sadeltak täckta med lertegel, sekelskiftesvillor med lertegeltäckta sadeltak som ibland är brutna, och mindre bostadshus på gårdarna med rödfärgad fasad och tegeltak.",
       "De större ekonomibyggnaderna har enligt riktlinjerna ofta en vitputsad ladugårdsdel, fasader av rödfärgad träpanel och sadeltak täckta med tegel eller korrugerad plåt. I inventeringen av enskilda gårdar nämns också en jordkällare med plåttak. Plåten finns alltså redan i dalgången, men främst på byggnader för djur, redskap och förvaring.",
       "På bostadshusen är riktlinjerna försiktigare. Kommunen konstaterar att plåt och plast ofta är oförenliga med äldre naturmaterial och skriver: låt trähus förbli trähus. Plåt som fasadmaterial står sig enligt riktlinjerna inte i tiden, är svår att få fin runt fönster och dörrar, blir lätt repig och bucklig och är svår att byta ut. Vi tar med de råden när vi föreslår material till ett äldre hus, och använder plåten där den hör hemma: på taket, i rännorna och i beslagen.",
     ],
     "aside": {"title": "Taken i dalgången", "items": [
       "Lertegel på parstugor och villor", "Tegel eller korrugerad plåt på ladugårdar",
       "Traditionell takvinkel 30–40 grader", "Trähus ska förbli trähus"]}},
    {"id": "matt-plat", "h2": "Matt plåt – och svart hellre än orange",
     "paras": [
       "Riktlinjerna konstaterar att byggnader för lantbrukets behov är bygglovsbefriade, och att kommunen därför inte kan ställa krav på anpassning till kulturmiljön för lador och liknande byggnader. Rekommendationen till lantbrukaren är ändå att följa riktlinjerna så långt det går med hänsyn till lantbrukets behov.",
       "Hästverksamhet och ridning räknas enligt riktlinjerna som fritidsverksamhet, och då krävs bygglov för stall. För stall och andra större byggnader för fritidsändamål anger kommunen att huset ska ha sadeltak med en takvinkel på inte lägre än cirka 30 grader, och att takbeläggningen bör vara lertegel. Används plåt i stället ska den upplevas matt på avstånd, och svart kulör är då ofta bättre än en klar orange ton. Väggfärgen bör vara matt, särskilt om väggen är klädd med plåt.",
       "Plåt finns i många ytbeläggningar och glansgrader, och skillnaden syns tydligt i ett öppet landskap. Vi tar fram kulörprover och matta alternativ innan något beställs, så att du kan jämföra dem mot kommunens råd och mot gårdens övriga byggnader.",
     ],
     "aside": None},
    {"id": "takvatten-sigtuna", "h2": "Lövsil, magasin och bräddavlopp för takvattnet",
     "paras": [
       "Sigtuna Vatten & Renhållning skriver att dagvattenledningsnätet i kommunen är ungefär 120 kilometer långt, att det finns en dagvattentunnel på nära 4 kilometer och drygt 20 anläggningar för fördröjning och sedimentering, och att allt dagvatten rinner med självfall. Vid all nybyggnation eftersträvas lokalt omhändertagande på fastigheten.",
       "Broschyren Dagvatten på din fastighet, som bolaget länkar till, ger råd som rör stupröret direkt. Leds takvatten till ett magasin eller en stenkista ska det först rensas från löv med en lövsil på stupröret, och silen ska tömmas regelbundet. Anläggningen ska ha ett bräddavlopp för stora regn, och hålrumsvolymen bör motsvara minst 10 millimeter av det regn som faller på tak och hårdgjorda ytor. Den bör kunna rensas och spolas ur, vanligtvis vart tionde år.",
       "Har du en regnvattentunna bör den enligt broschyren ha ett överfyllnadsskydd, så att överskottet leds ut på gräsmattan i stället för mot grunden. Vi monterar lövsil och stuprörsdelar så att de går att nå och rengöra, och leder överskottet bort från huset. Om takets skick i stort läser du under " + _L.format("takrenovering-sigtuna.html", "takrenovering i Sigtuna") + ".",
     ],
     "aside": {"title": "Vid stupröret", "items": [
       "Lövsil före magasinet", "Bräddavlopp för stora regn",
       "Minst 10 mm magasinsvolym", "Överfyllnadsskydd på tunnan"]}},
    {"id": "ritningar-sigtuna", "h2": "Frivilligt bygglov och ritningar till arkivet",
     "paras": [
       "Ska du byta takmaterial, till exempel från tegel till plåt, kan du enligt Sigtuna kommun behöva bygglov beroende på var byggnaden ligger och om den är kulturhistoriskt värdefull. Kommunen erbjuder också frivilligt bygglov, så att du kan få beskedet att åtgärden uppfyller lagens krav innan arbetet börjar. Beslut ska komma inom tio veckor från att ansökan är komplett.",
       "Broschyren om dagvatten påminner om en sak som ofta glöms: lämna in ritningar över den nya VA-anläggningen till bygglovsarkivet, även när ändringen inte kräver bygglov. Det hjälper nästa ägare att hitta stenkistor och ledningar. Mer om plåtarbeten i allmänhet finns på sidan " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtjobb i Sigtuna till",
  "steps": [
    ("Platsbesök", "Vi går igenom tak, rännor och beslag och ser om fastigheten ligger i ett utpekat kulturmiljöområde."),
    ("Kulör och yta", "På gårdar och stall tar vi fram matta kulörprover att jämföra mot kommunens riktlinjer."),
    ("Kostnadsförslag", "Plåttak, rännor, stuprör och lövsilar redovisas som egna poster."),
    ("Montering", "Gammal plåt tas ner och ny plåt monteras med rätt fall och åtkomliga silar."),
    ("Genomgång", "Vi visar var vattnet leds och hur silar och avledare rensas."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Sigtuna",
  "rot": [
    "Skatteverket räknar det som rotarbete att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör på ett småhus, och att montera ställning i samband med arbetet. Arbetet ska utföras i bostaden eller på tomten i nära anslutning till den.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Sigtuna?",
  "price": [
    "Takytan och lutningen, valet av plåt, profil och kulör, antalet rännor och stuprör, om lövsilar och avledare ska monteras och hur hög byggnaden är. En stor ladugård kräver annan ställning än en villa. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi lägga plåt på ladugården i dalgången mellan Odensala och Hova?",
     "Byggnader för lantbrukets behov är bygglovsbefriade enligt kommunens riktlinjer. Kommunen rekommenderar ändå att plåt upplevs matt på avstånd och att svart ofta är bättre än en klar orange ton."),
    ("Kräver ett nytt stall med plåttak bygglov i Sigtuna?",
     "Ja. Riktlinjerna anger att hästverksamhet räknas som fritidsverksamhet och att bygglov därför krävs för stall. Kommunen kan då ställa krav på tak och kulör."),
    ("Varför ska det sitta en lövsil på stupröret till stenkistan?",
     "Broschyren Dagvatten på din fastighet anger att takvatten ska rensas från löv med en lövsil innan det leds till ett magasin, så att anläggningen inte sätts igen."),
    ("Kan vi söka frivilligt bygglov för att byta tegeltaket mot plåt i Sigtuna?",
     "Ja. Kommunen skriver att du kan söka frivilligt bygglov när du byter takmaterial, och få beskedet innan arbetet börjar."),
    ("Rekommenderar kommunen plåt som fasad på ett gammalt trähus?",
     "Nej. I riktlinjerna för dalgången står att trähus ska förbli trähus och att plåt som fasadmaterial är svår att få fin runt fönster och dörrar."),
  ],
  "sources": [
    ("Sigtuna kommun – Riktlinjer för bebyggelseutveckling i dalgången mellan Odensala och Hova (2020, pdf)",
     _SG + "download/18.2b81151517d4919beb8c692e/1638798200988/Riktlinjer%20f%C3%B6r%20bebyggelseutveckling%20i%20dalg%C3%A5ngen%20mellan%20Odensala%20och%20Hova.pdf"),
    ("Sigtuna kommun – Tak (ändra befintlig byggnad)", _SG + "bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/andra-befintlig-byggnad/tak.html"),
    ("Sigtuna Vatten & Renhållning – Dagvatten", "https://sigtunavatten.se/vatten/dagvatten/"),
    ("Sigtuna Vatten & Renhållning – Dagvatten på din fastighet (Oxunda vattensamverkan 2018, pdf)",
     "https://sigtunavatten.se/wp-content/uploads/2019/02/dagvatten-pa-din-fastighet_2018_oxunda_webbversion-a4.pdf"),
    _SCB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska plåten på huset eller gården i Sigtuna bytas?", "Boka ett gratis platsbesök så går vi igenom tak, kulör och takvatten på plats."),
  "img": [
    ("Gård i Odensala med röd ladugård med svart matt plåttak och vit mangårdsbyggnad med tegeltak",
     "farm in the Odensala valley Sigtuna Uppland Sweden, long falu red wooden barn with a white rendered stone lower wall and a simple symmetric gable roof covered with matte black corrugated steel sheets with clearly visible vertical ridges, black gutters, beside it a white wooden two-storey farmhouse with red clay tile roof, open fields and old ash trees, overcast autumn daylight, photorealistic, no people, no animals, no vehicles, no text"),
    ("Stuprör i plåt med lövsil på väg ner mot en stenkista i en villaträdgård",
     "close-up of a dark grey round metal downpipe on a yellow wooden villa wall in Märsta Sweden, with a metal leaf filter section mounted at chest height and the lower pipe continuing into the ground at a cast inspection cover in a lawn, gravel strip along the foundation, overcast, photorealistic, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"platslagare-upplands-vasby.html": {
  "kind": "district", "service": "platslagare", "ort": "Upplands Väsby", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Upplands Väsby – stuprör, radhus och dagvatten",
  "description": "Plåtslagare i Upplands Väsby: stuprör som ger tillskottsvatten i spillvattnet, gemensam dagvattenlösning i radhusområdet och vattenskyddsområdet.",
  "h1": "Plåtslagare i Upplands Väsby",
  "lead": "Upplands Väsby har drygt 7 000 bostäder i småhus enligt SCB. Ungefär hälften av kommunens ledningar i gatorna byggdes mellan 1960 och 1990, och kommunen arbetar med att få bort regnvatten som hamnar i spillvattnet, bland annat från stuprör. Geal Entreprenad AB byter hängrännor, stuprör och plåt på villor och radhus i Upplands Väsby, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Rännor, stuprör och radhusplåt i Väsby.",
  "sections": [
    {"id": "tillskottsvatten", "anchor": "Stuprör och spillvatten",
     "h2": "Stuprör som belastar spillvattnet",
     "paras": [
       "Kommunfullmäktige antog vattentjänstplanen för Upplands Väsby den 11 november 2024. Där förklaras tillskottsvatten som vatten som hamnar i spillvattenledningarna genom till exempel inläckage, stuprör eller dagvattenledningar. Det vattnet behöver inte renas som spillvatten och belastar VA-anläggningen i onödan.",
       "Enligt planen arbetar kommunen systematiskt och områdesvis för att minska tillskottsvattnet, bland annat för att minska risken för bräddning vid höga flöden. Området Övra Runby har utretts och arbetet med att ta bort tillskottsvatten pågår där, och fler områden ska utredas de kommande åren. Kommunen har till största delen ett duplikatsystem med separata ledningar för spill- och dagvatten, men i de äldsta områdena kan det förekomma kombinerade ledningar.",
       "Kommunen skriver också uttryckligen att dagvatten och dräneringsvatten inte får kopplas till spillvattenservisen. När vi byter rännor och stuprör tittar vi därför på var stupröret försvinner ner i marken. Är du osäker på vart ledningen går kan kommunens kontaktcenter Väsby Direkt svara på frågor om din och den allmänna dagvattenanläggningen.",
     ],
     "aside": {"title": "Vattentjänstplanen i korthet", "items": [
       "Tillskottsvatten belastar nätet", "Övra Runby utrett först",
       "Fler områden de kommande åren", "Inget dagvatten till spillvattnet"]}},
    {"id": "ledningsnat-vasby", "h2": "Ledningar och hus från samma årtionden",
     "paras": [
       "Vattentjänstplanen beskriver ett ledningsnät som till stor del byggdes samtidigt som villaområdena. Kommunen har cirka 137 kilometer dagvattenledningar och cirka 153 kilometer spillvattenledningar, och ungefär hälften av näten byggdes mellan 1960 och 1990, merparten på 1970-talet. Ledningarnas ålder gör enligt planen att de inom några år behöver förnyas.",
       "Planen tar också upp skyfall, som enligt SMHI:s definition är minst 50 millimeter regn på en timme eller minst 1 millimeter på en minut. Vid skyfall går dagvattenledningarna fulla och vattnet rinner på markytan. Kommunen tog 2023 fram en skyfallskartering och en skyfallsplan.",
       "Det kommunen gör i gatan och det du gör på tomten hänger ihop. Hängrännor som är rätt dimensionerade för takytan och stuprör som leder vattnet ut på gräset i stället för direkt ner i marken minskar mängden som når ledningarna vid kraftiga regn. Om takens ålder och material i kommunen finns mer under " + _L.format("takrenovering-upplands-vasby.html", "takrenovering i Upplands Väsby") + ".",
     ],
     "aside": None},
    {"id": "radhus-vasby", "h2": "Radhuslängan och den gemensamma lösningen",
     "paras": [
       "I ett radhusområde är det vanligt att rännor, stuprör och ibland ledningarna i marken hör ihop över flera tomter. Kommunen godkänner generellt inte en gemensam förbindelsepunkt för vatten, men kan godkänna det för spill- och dagvatten om det finns särskilda skäl. En förutsättning är att fastigheterna har bildat en gemensamhetsanläggning och vid behov en samfällighetsförening, som då är kommunens motpart.",
       "Ska området bygga en ny gemensam dagvattenanläggning, eller ändra en befintlig, inom detaljplanelagt område ska det enligt kommunen anmälas till bygg- och miljökontoret senast sex veckor före byggstart. Anmälan krävs inte om anläggningen bara avvattnar en enstaka fastighet. Exempel på anläggningar är fördröjningsmagasin, infiltrationsanläggningar och växtbäddar.",
       "För rotavdraget spelar ägarformen roll. Skatteverket skriver att arbeten på samfällighetens gemensamma delar inte ger rätt till rotavdrag, medan plåtarbete på det egna huset i ett småhus gör det. Byter flera grannar rännor samtidigt prissätter vi därför varje hus för sig. Om radhusens fasader och kulörer finns mer under " + _L.format("fasadrenovering-upplands-vasby.html", "fasadrenovering i Upplands Väsby") + ".",
     ],
     "aside": {"title": "När grannarna gör det tillsammans", "items": [
       "Gemensam förbindelsepunkt kräver GA", "Anmälan sex veckor före start",
       "Ingen anmälan för en enstaka tomt", "Ett kostnadsförslag per hus"]}},
    {"id": "vattenskydd-vasby", "h2": "Vattenskyddsområdet kring Hammarby reservvattentäkt",
     "paras": [
       "Stora delar av Upplands Väsby omfattas av vattenskyddsområdet för Hammarby reservvattentäkt, som är norra Stockholms reservdricksvatten och därför extra skyddsvärd. Inom området gäller skyddsföreskrifter från Länsstyrelsen, och kommunen visar gränsen på Väsbykartan. I vissa delar av Väsby leds dagvattnet till kommunala infiltrationsanläggningar där vattnet leds ner i marken.",
       "Kommunen skriver att dagvatten från parkeringar och gator kan innehålla tungmetaller, näringsämnen, partiklar, salter och oljor. Vatten från ett tak är renare, och det är ytterligare ett skäl att låta det rinna ut på gräs i stället för att blandas med vattnet från uppfarten. Mer om plåtarbeten i allmänhet finns på sidan " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtjobb i Upplands Väsby till",
  "steps": [
    ("Platsbesök", "Vi går igenom rännor, stuprör och beslag och ser var varje stuprör leder vattnet."),
    ("Radhus eller villa", "I en radhuslänga reder vi ut vad som är ditt och vad som hör till samfälligheten."),
    ("Kostnadsförslag", "Varje hus får ett eget skriftligt kostnadsförslag, även när grannar beställer samtidigt."),
    ("Montering", "Ny plåt monteras med rätt fall och stuprör som leder ut vattnet på gräset."),
    ("Genomgång", "Vi visar hur rännor och utkastare hålls fria från löv."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Upplands Väsby",
  "rot": [
    "Skatteverket räknar det som rotarbete att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör i ett småhus, och ett radhus räknas som småhus. Arbeten på samfällighetens gemensamma delar ger däremot inget avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Upplands Väsby?",
  "price": [
    "Längden på rännorna, hur många stuprör och ränndalar huset har, om flera hus i en länga görs samtidigt och om stuprören ska kopplas om från en ledning i marken till utkastare. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad är tillskottsvatten och hur hänger det ihop med vårt stuprör?",
     "Enligt Upplands Väsbys vattentjänstplan är det vatten som hamnar i spillvattenledningarna, till exempel från stuprör. Det belastar VA-anläggningen i onödan, och kommunen arbetar områdesvis för att minska det."),
    ("Får två radhus i Upplands Väsby dela förbindelsepunkt för dagvatten?",
     "Det kan godkännas om det finns särskilda skäl och fastigheterna har bildat en gemensamhetsanläggning. För dricksvatten godkänns det generellt inte."),
    ("Behöver vår samfällighet anmäla ett nytt fördröjningsmagasin?",
     "Ja, om anläggningen ligger inom detaljplanelagt område och avvattnar mer än en fastighet. Anmälan ska göras till bygg- och miljökontoret senast sex veckor före byggstart."),
    ("Ger byte av rännor rotavdrag om samfälligheten beställer?",
     "Nej, arbeten på samfällighetens gemensamma delar ger inte rätt till rotavdrag enligt Skatteverket. Plåtarbete på ditt eget radhus ger avdrag."),
    ("Ligger vår villa i Väsby i ett vattenskyddsområde?",
     "Stora delar av kommunen omfattas av vattenskyddsområdet för Hammarby reservvattentäkt. Gränsen syns på Väsbykartan och föreskrifterna finns hos Länsstyrelsen."),
  ],
  "sources": [
    ("Upplands Väsby kommun – Vattentjänstplan, KF 2024-11-11 (pdf)",
     "https://kulturskolan.upplandsvasby.se/download/18.433d62bf19515940f6b4c0/1740661429806/Vattentj%C3%A4nstplan%20Upplands%20V%C3%A4sby%20kommun.pdf"),
    ("Upplands Väsby kommun – Dagvatten", _UV + "dagvatten"),
    ("Upplands Väsby kommun – Ledningsnät, anslutning till fastighet", _UV + "ledningsnat-anslutning-till-fastighet"),
    ("Upplands Väsby kommun – Vattenskyddsområde", _UV + "dricksvatten/vattenskyddsomrade"),
    _SCB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska rännor och stuprör bytas på huset i Väsby?", "Boka ett gratis platsbesök så följer vi takvattnet från rännan till marken."),
  "img": [
    ("Radhuslänga i Upplands Väsby med mörka tak, hängrännor och stuprör",
     "row of 1970s Swedish terraced houses in Upplands Väsby with white painted brick and dark brown wooden panel facades, low-pitched dark grey metal roofs with black half-round gutters and downpipes between each house ending in outlets over small lawns, wooden fences between front yards, autumn birch trees, overcast daylight, photorealistic, no people, no cars, no text"),
    ("Stuprör som går ner i marken vid grunden på ett radhus",
     "close-up of the lower end of a black round metal downpipe on the corner of a Swedish terraced house with dark wooden panel, ending in a curved outlet spout above a concrete splash block that leads water onto a lawn, an old capped ground pipe connection beside it, wet autumn leaves, overcast, photorealistic, no people, no hands, no text"),
  ],
  "related": [],
},
}

