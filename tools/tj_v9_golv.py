# -*- coding: utf-8 -*-
"""Golvläggare – ortsidor v9: Järfälla, Vallentuna, Norrtälje, Österåker, Botkyrka, Upplands Väsby (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
Järfälla kommun (Kulturmiljöplan: Jakobsberg – Skogsvägen–Toppvägen och Jakobsbergs gård; Radon; Ändra i bärande
konstruktion), Vallentuna kommun (Radon), Norrtälje kommun (Kulturmiljöutredning nr 1 Arholma 2016; Inomhus- och
boendemiljö), Österåkers kommun (Bostadsanpassning), Botkyrka kommun (Kulturmiljöprogram 2014:
Tullinge, Segersjö, villaarkitektur; Radon), Upplands Väsby kommun (Kunskapsunderlag för kulturmiljö: Radhus och
kedjehus 1960–70-tal, Väsby villastad; Radon), Boverket (Risker med asbest i byggnader; Betongplatta på mark; Risker
med fukttransport från mark; Krypgrund – fördjupning om torpargrunden; Källare; Energiguiden Golvvärme;
Bostadsanpassningsbidraget – handboken), Golvbranschen (Massiva trägolv; Lamellparkett; Linoleumgolv; PVC-golv),
SCB (BO0104T04, bostäder i småhus 2024: Järfälla 11 492, Vallentuna 9 194, Norrtälje 19 110, Österåker 13 488,
Botkyrka 12 555, Upplands Väsby 7 053) och Skatteverket (rotavdrag; inget rotavdrag när arbetet får bidrag).
Strukna (ej verifierade eller motsägelsefulla): Tunanäs och 1960-talets småhusbygge i Åkersberga
(Kulturmiljöprogrammet I Roslagen 1998 finns bara som inskannad pdf utan textlager), radonbidrag (Norrtälje anger att man kan söka, Botkyrka att bidraget
inte längre finns i statens budget – nämns därför inte), golvmaterial i originalutförande per område/epok,
grundläggningstyp per område, andel hus med asbest per område, Golvbranschens temperaturgräns för trägolv på
golvvärme (bara hänvisning), gamla kommunala radonkartor per tomt (kommunerna avråder från att dra slutsatser per tomt).
Inga priser, garantier, omdömen, egna uppdrag i orterna eller certifikat. Korslänkar via V4_MODULES i tjanster_v1.py.
Schema: se tools/tj_check.py."""

_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SCB = ("SCB – Antal lägenheter efter region och hustyp (BO0104), 2024",
        "https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BO__BO0104__BO0104D/BO0104T04/")
_GBR_MASSIV = ("Golvbranschen – Massiva trägolv", "https://www.golvbranschen.se/teknik--material/tragolv/massiva-tragolv/")
_GBR_LAMELL = ("Golvbranschen – Lamellparkett", "https://www.golvbranschen.se/teknik--material/tragolv/lamellparkett/")
_GBR_LINO = ("Golvbranschen – Linoleumgolv", "https://www.golvbranschen.se/teknik--material/linoleumgolv/")
_GBR_PVC = ("Golvbranschen – PVC-golv", "https://www.golvbranschen.se/teknik--material/plastgolv/plastgolv---pvc/")
_BOV_FG = "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-for-grund/"
_BOV_ASB = ("Boverket – Risker med asbest i byggnader",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_BOV_PLATTA = ("Boverket – Fuktrisker med betongplatta på mark", _BOV_FG + "betongplatta-mark/")
_BOV_MARKFUKT = ("Boverket – Risker med fukttransport från mark till betongplatta och källare",
                 _BOV_FG + "betongplatta-mark/risk-fukttransport-mark/")
_BOV_KRYP = ("Boverket – Fuktrisker med krypgrund", _BOV_FG + "krypgrund/")
_BOV_KALLARE = ("Boverket – Fuktrisker med källare", _BOV_FG + "fuktrisker-med-kallare/")
_BOV_GV = ("Boverket – Energiguiden: Golvvärme",
           "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/golvvarme/")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ JÄRFÄLLA
"golvlaggare-jarfalla.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Järfälla", "svc_label": "Golvläggare",
  "title": "Golvläggare i Järfälla – kedjehus, egnahem och gamla mattor",
  "description": "Golvläggare i Järfälla: nya golv i 60-talets kedjehus, asbest i gamla plattor och lim, egnahemmens trägolv och radon när grunden öppnas. Gratis platsbesök.",
  "h1": "Golvläggare i Järfälla",
  "lead": "Under en plastmatta från 1960-talet kan det ligga både ett fint trägolv och ett lim som inte bör slipas upp i onödan. I Järfälla finns hus från egnahemsåren, tidiga kedjehus och allt som byggts sedan dess. Geal Entreprenad AB lägger nya golv, slipar och lagar trägolv i hela kommunen – från Jakobsberg och Viksjö till Kallhäll och Barkarby – med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Kedjehus, egnahem och gamla golvskikt.",
  "sections": [
    {"id": "toppvagen", "anchor": "Husen i Järfälla",
     "h2": "Kedjehus från flera olika byggfirmor",
     "paras": [
       "Enligt SCB fanns det 11 492 bostäder i småhus i Järfälla 2024. Ett område som kommunens kulturmiljöplan lyfter fram är Skogsvägen–Toppvägen i Jakobsberg. Det exploaterades i början av 1960-talet, och husen uppfördes av flera olika byggfirmor, vilket gav en varierad utformning. Längs Vretstigen och norra delen av Toppvägen står tvåvåningsradhus, medan södra Toppvägen, Skogsvägen och början av Bergsringen har kedjehus.",
       "Planen beskriver bebyggelsen som en god bild av det tidiga 1960-talets småhusbyggande. För den som ska byta golv betyder det att grannens lösning inte säkert passar ditt hus. Två hus på samma gata kan ha olika bjälklag, olika underlag och olika många lager golv. Därför lyfter vi en list eller tittar under en tröskel innan vi föreslår något.",
     ],
     "aside": {"title": "Det vi letar efter", "items": [
       "Underlag av betong eller trä", "Antal gamla golvskikt",
       "Lim och spackel under mattan", "Höjd vid dörrar och trappa"]}},
    {"id": "asbest-golv", "h2": "Gamla plattor och lim kan innehålla asbest",
     "paras": [
       "Boverket skriver att asbest förbjöds inom byggsektorn 1982, men att stora mängder fortfarande finns kvar i husen. Är ett hus byggt mellan 1940 och 1980 är det enligt Boverket sannolikt att det finns asbest någonstans i det. Bland exemplen på var den kan sitta finns golvplattor, mattor, lim under mattor och plattor, skikt under mattor och golvmassor.",
       "Så länge asbesten ligger kvar i bunden form är den ingen fara, men den blir det om materialet slipas, bryts eller dammar. Boverket påpekar att provtagning och analys är det enda säkra sättet att veta. Därför river vi inte upp en gammal matta eller platta förrän vi vet vad som ligger under. Finns det misstanke tas ett prov som skickas till ett laboratorium, och visar det asbest behöver saneringen planeras av ett företag med rätt kompetens innan golvarbetet börjar. Ibland går det att låta det gamla skiktet ligga orört och bygga det nya golvet ovanpå, vilket vi i så fall går igenom med dig.",
     ],
     "aside": {"title": "Innan den gamla mattan rivs", "items": [
       "Ta reda på byggår och tidigare renoveringar", "Leta i bygglovshandlingarna",
       "Låt ett laboratorium analysera ett prov", "Planera saneringen före golvjobbet"]}},
    {"id": "jakobsberg-egnahem", "h2": "Egnahemstomterna från Jakobsbergs gård",
     "paras": [
       "Kulturmiljöplanen berättar att Jakobsbergs gård såldes 1918 till Mälarprovinsernas Egnahem AB. Företaget styckade ägorna till småbruk och trädgårdsmästerimark, och även villatomter styckades av. På de forna ägorna började samhället Jakobsberg växa upp.",
       "I de äldre husen ligger ofta massiva trägolv. Golvbranschen beskriver dem som golv som kan renoveras många gånger, där det som sätter gränsen är hur tjockt träet är mellan ytan och not och spår. Vi mäter det innan vi slipar. Branschen påpekar också att trä krymper och sväller med luftens fuktighet och mår bäst vid 30–60 procent relativ fuktighet, och att våta rengöringsmetoder bör undvikas. Mer om ytbehandling och golvtyper finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "barande-jarfalla", "h2": "När golvbytet rör bjälklaget",
     "paras": [
       "Ett vanligt golvbyte kräver ingen kontakt med kommunen. Annorlunda blir det om bjälkar ska kapas för en ny trappa, ett avlopp eller en golvvärmeslinga. Järfälla kommun skriver att ändringar som påverkar en byggnads bärande konstruktion kräver anmälan och att du ska invänta startbesked innan arbetet börjar.",
       "Kommunen tipsar om att gamla ritningar visar husets principiella konstruktion, men varnar för att de kan vara ofullständiga och att det inte är säkert att husen byggdes som ritningarna visar. Kommunen kan inte själv bedöma om en åtgärd påverkar bärande delar, utan hänvisar till en konstruktör. Vi säger till redan vid platsbesöket om vi ser att golvet kan beröra stommen.",
     ],
     "aside": None},
    {"id": "radon-grund", "h2": "Rör genom grunden och en ny radonmätning",
     "paras": [
       "Enligt kommunen består Järfälla huvudsakligen av normal- och lågriskmark för radon, men med små lokala variationer som gör det olämpligt att generalisera per område. Kommunen rekommenderar en ny mätning om det har gått mer än tio år sedan den förra, om husets ventilation har ändrats eller om man har gjort förändringar i husgrunden, till exempel rörgenomdragningar.",
       "Ska golvet på en platta öppnas för nya rör, till exempel i samband med att " + _L.format("badrumsrenovering-jarfalla.html", "badrummet i Järfälla görs om") + ", är det klokt att planera en långtidsmätning efteråt. Den görs under flera månader mellan 1 oktober och 30 april.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvbytet till i Järfälla",
  "steps": [
    ("Platsbesök", "Vi tittar på golvet, lyfter en list och frågar om husets byggår och tidigare renoveringar."),
    ("Prov vid behov", "Finns gamla plattor eller lim som kan innehålla asbest tas ett prov innan något rivs."),
    ("Kostnadsförslag", "Du får ett skriftligt kostnadsförslag där rivning, underlag och nytt golv redovisas för sig."),
    ("Förberedelse", "Möbler flyttas, trappor och dörrar skyddas och underlaget rensas och riktas."),
    ("Golvläggning", "Det nya golvet läggs, eller det gamla trägolvet slipas och lagas."),
    ("Avslut", "Lister och trösklar sätts tillbaka och du får råd om skötsel av det nya golvet."),
  ],
  "rot_h2": "ROT-avdrag för golv i Järfälla",
  "rot": [
    "Skatteverket godkänner rotavdrag för att slipa och byta golv i ett småhus du äger och bor i, och räknar även byte från plastmatta till trägolv som rotarbete. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och rot och rut får tillsammans vara högst 75 000 kr.",
    "Material och resor ingår inte i avdraget. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Järfälla?",
  "price": [
    "Golvytan, hur många gamla lager som ska bort och om underlaget behöver riktas avgör mest. Behövs asbestprov eller sanering kommer det till som en egen post. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan plastmattan i vårt kedjehus från 1960-talet innehålla asbest?",
     "Det är möjligt. Boverket nämner mattor, golvplattor och lim under mattor bland de material där asbest kan finnas i hus byggda 1940–1980. Bara ett prov som analyseras på laboratorium ger ett säkert svar."),
    ("Måste vi göra en anmälan för att byta golv i Järfälla?",
     "Inte för ett vanligt golvbyte. Kapas eller ändras bjälkar som bär huset kräver kommunen en anmälan och ett startbesked innan arbetet börjar."),
    ("Behöver vi mäta radon efter att golvet i Jakobsberg har öppnats för nya rör?",
     "Järfälla kommun rekommenderar en ny mätning efter förändringar i husgrunden, till exempel rörgenomdragningar. Mätningen görs mellan 1 oktober och 30 april."),
    ("Går det att slipa trägolvet i ett egnahem från 1920-talet?",
     "Ofta, om det finns tillräckligt med trä kvar ovanför not och spår. Vi mäter tjockleken innan vi föreslår slipning eller lagning."),
    ("Kan ett nytt golv läggas ovanpå gamla plattor som kanske innehåller asbest?",
     "Ibland är det ett alternativ, eftersom asbest i bunden form inte är farlig så länge den inte bearbetas. Vi går igenom höjder och underlag med dig innan något bestäms."),
  ],
  "sources": [
    ("Järfälla kommun – Kulturmiljöplan för Järfälla: Jakobsberg (pdf)",
     "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4080/1550245872956/kulturmiljoplan-jakobsberg.pdf"),
    ("Järfälla kommun – Radon",
     "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/inomhusmiljo/radon.4.40b7e74714b9b24883d321c4.html"),
    ("Järfälla kommun – Ändra i bärande konstruktion",
     "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/andraibarandekonstruktion.4.69a1b161151015104f4bca0b.html"),
    _BOV_ASB, _GBR_MASSIV, _SCB, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i huset i Järfälla bytas?", "Boka ett gratis platsbesök så tittar vi på vad som ligger under och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Nylagt ljust trägolv i vardagsrummet i ett kedjehus från 1960-talet",
     "empty bright living room in a Swedish 1960s link house with a newly laid light oak plank floor, white walls, low wide window with a view of a small garden and a wooden fence, simple white skirting boards, soft daylight, no furniture, no people, no text"),
    ("Gamla golvplattor i rutmönster där en platta saknas och limmet syns",
     "close-up of an intact old 1960s vinyl tile floor in a beige and brown checkerboard pattern in a Swedish house, one single square tile missing so that dark old adhesive is visible in its place, a closed small clear plastic sample bag lying next to the gap, white skirting board, natural light, no people, no hands, no tools, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VALLENTUNA
"golvlaggare-vallentuna.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Vallentuna", "svc_label": "Golvläggare",
  "title": "Golvläggare i Vallentuna – golvvärme och golv på platta",
  "description": "Golvläggare i Vallentuna: nytt golv på betongplatta, golvvärme i ett befintligt hus och radonmätning när värmesystemet ändras. Gratis platsbesök.",
  "h1": "Golvläggare i Vallentuna",
  "lead": "Många som byter golv vill samtidigt få varma golv. Men golvvärme i ett hus som inte är byggt för det kan ge både högre elräkning och fukt under golvet. Geal Entreprenad AB lägger nya golv och slipar gamla i hela Vallentuna kommun – i tätorten, i Kårsta, Lindholmen och Brottby – med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Golv på platta och golvvärme i villan.",
  "sections": [
    {"id": "vallentuna-platta", "anchor": "Husen i Vallentuna",
     "h2": "Drygt 9 000 småhusbostäder – och många olika grunder",
     "paras": [
       "SCB räknade 9 194 bostäder i småhus i Vallentuna kommun 2024. De står på allt från stenfoten under en gammal gård till krypgrunder och betongplattor från de senaste decennierna. Vilken grund huset har avgör mer än något annat vilket golv som passar.",
       "Boverket beskriver hur betongplattan på mark kom in i bostadsbyggandet i början av 1960-talet. De första plattorna byggdes huvudsakligen med isoleringen ovanpå betongen och ofta utan ångtätt skikt mot marken. Golven var vanligtvis uppreglade, med isolering mellan reglarna. Har du ett hus från den tiden är det första vi vill veta hur golvet är uppbyggt.",
     ],
     "aside": {"title": "Grunden avgör", "items": [
       "Platta med isolering under eller ovanpå", "Krypgrund med träbjälklag",
       "Källare eller suterräng", "Gammal stenfot under en gård"]}},
    {"id": "uppreglat", "h2": "Uppreglade golv ovanpå kall betong",
     "paras": [
       "När isoleringen ligger ovanpå plattan blir betongens överdel nästan lika kall som marken under huset, och då blir också luftfuktigheten i betongen hög. Boverket skriver att träreglarna och smuts eller byggrester på betongytan då riskerar att bli fuktiga, särskilt där spikreglar har gjutits in eller där reglarna står direkt mot betongen. Det kan ge mikrobiologisk påväxt, dålig lukt och ibland röta. Ingjutna reglar av tryckimpregnerat virke kan lukta särskilt illa.",
       "Boverket konstaterar att den här typen av golv med tiden har fått omfattande fuktskador och att man i dag bygger på andra sätt. För dig som ska byta golv betyder det att vi gärna öppnar en mindre yta vid en vägg innan vi bestämmer något. Ser underlaget friskt ut kan det nya golvet läggas som planerat. Gör det inte det behöver golvkonstruktionen ses över först, annars hamnar det nya golvet på samma problem.",
     ],
     "aside": None},
    {"id": "golvvarme-vallentuna", "h2": "Golvvärme kräver en välisolerad grund",
     "paras": [
       "I Boverkets energiguide står att ett hus med golvvärme avger mer värme till marken än ett hus med annan uppvärmning, eftersom golvet är varmare. Har grunden lite isolering mot mark är risken mycket stor att energianvändningen ökar. Under värmeslingan ska isoleringen vara tjock och ovanför den ska materialet släppa igenom värme.",
       "Därför spelar golvmaterialet roll. Boverket nämner tjocka parkettgolv med isolerande stegljudsisolering och tjocka mattor som exempel på ytor som isolerar, medan plastmattor och klinker lättare släpper igenom värmen. Klinker kan å andra sidan kännas kallt när golvvärmen är avstängd, vilket gör det lätt att förlänga uppvärmningssäsongen. Vi går igenom både grund och golvval innan du bestämmer dig. Mer om golvtyper finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "varmekudde", "h2": "När golvvärmen stängs av på våren",
     "paras": [
       "Är grunden dåligt isolerad värms marken under huset upp under vintern, och det bildas en värmekudde. När golvvärmen slås av på våren blir plattan kall medan marken fortfarande är varm, och då kan markfukt kondensera mot plattan. Boverkets tumregel är att marken behöver vara minst tre grader kallare än konstruktionen för att det ska gå att lägga täta ytor inomhus.",
       "Boverket varnar också för golvvärme i bara en del av grunden. I ett parhus där den ena halvan har golvvärme och den andra radiatorer kan fuktrisken öka i huset utan golvvärme. Och tas radiatorerna under fönstren bort kan kallraset från äldre fönster ge drag längs golvet. Ska fönstren ändå bytas finns mer på sidan om " + _L.format("fonsterbyte-vallentuna.html", "fönsterbyte i Vallentuna") + ".",
     ],
     "aside": {"title": "Fråga dig innan golvvärme", "items": [
       "Hur tjock är isoleringen under plattan?", "Ska hela huset ha golvvärme?",
       "Delar du vägg med en granne?", "Hur gamla är fönstren?"]}},
    {"id": "radon-vallentuna", "h2": "Ny uppvärmning – mät radonhalten igen",
     "paras": [
       "Vallentuna kommun rekommenderar en radonmätning vid ny-, om- och tillbyggnad av småhus, vid förändring av ventilation eller uppvärmningssystem och när det har gått tio år sedan förra mätningen. Att byta radiatorer mot golvvärme är en sådan förändring.",
       "Mätningen görs mellan 1 oktober och 30 april under minst två månader, helst tre. I ett enbostadshus mäts normalt sovrummet och ett rum till, till exempel vardagsrummet. Kommunen visar inskickade mätningar på sin karta, men påpekar att det kan finnas mätningar den inte känner till.",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången för golvet i Vallentuna",
  "steps": [
    ("Genomgång", "Vi går igenom huset, grunden och dina önskemål om golvvärme och golvmaterial."),
    ("Öppning", "Vid behov öppnas en liten yta vid en vägg så att vi ser hur golvet är uppbyggt."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag med golv, underlag och eventuell golvvärme som separata delar."),
    ("Underlag", "Gamla golv tas bort och underlaget torkas, riktas eller byggs om efter behov."),
    ("Nytt golv", "Golvet läggs med rätt fuktspärr och övergångar mot rum som inte görs om."),
    ("Uppföljning", "Du får råd om hur golvet ska skötas och när golvvärmen bör vara igång."),
  ],
  "rot_h2": "Rotavdrag för golvarbete i Vallentuna",
  "rot": [
    "Att slipa och byta golv i ett småhus som du äger och bor i räknas som rotarbete hos Skatteverket. Du får göra avdrag med 30 procent av arbetskostnaden, upp till 50 000 kr per person och år. Rot och rut får sammanlagt bli högst 75 000 kr.",
    "Avdraget gäller bara arbetet, inte material eller resor. Geal drar det direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset i Vallentuna?",
  "price": [
    "Det som påverkar mest är golvytan, skicket på underlaget och om golvkonstruktionen behöver göras om. Golvvärme, nya trösklar och flytt av möbler tillkommer. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi lägga golvvärme på betongplattan i vår villa i Vallentuna?",
     "Det beror på hur mycket isolering som finns under plattan. Boverket varnar för att golvvärme på en dåligt isolerad grund kan öka energianvändningen och ge fuktproblem. Vi tittar på grunden innan vi föreslår något."),
    ("Varför luktar det instängt i nedre planet i vårt hus från 1960-talet?",
     "En möjlig orsak är ett uppreglat golv med isolering ovanpå betongen, där reglarna blir fuktiga. Det är en konstruktion som Boverket beskriver som skadebenägen. Vi öppnar en liten yta och ser efter."),
    ("Är klinker eller parkett bäst ovanpå golvvärme?",
     "Enligt Boverket släpper klinker och plastmatta igenom värmen lättare än tjock parkett med stegljudsisolering. Klinker kan däremot kännas kallt när golvvärmen är av."),
    ("Måste vi mäta radon när vi byter till golvvärme i Vallentuna?",
     "Det finns inget generellt krav för egna hus, men kommunen rekommenderar en mätning när uppvärmningssystemet ändras. Den görs mellan oktober och april."),
    ("Kan golvvärme i vår halva av parhuset påverka grannens halva?",
     "Boverket nämner just parhus där den ena halvan har golvvärme och den andra radiatorer som ett fall där fuktrisken kan öka i huset utan golvvärme. Prata gärna med grannen innan."),
  ],
  "sources": [
    ("Vallentuna kommun – Radon",
     "https://www.vallentuna.se/bygga-bo-och-miljo/miljo-energi-och-halsoskydd/halsoskydd/radon"),
    _BOV_PLATTA, _BOV_MARKFUKT, _BOV_GV, _SCB, _SKV, _SKV2,
  ],
  "cta": ("Funderar du på nytt golv eller golvvärme i Vallentuna?", "Boka ett gratis platsbesök så tittar vi på grunden och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust rum med nytt ekgolv i en villa från 1970-talet i Vallentuna",
     "empty bright room in a Swedish 1970s single-storey villa with a newly laid light oak floor, large window with view of a lawn and birch trees, white walls, white skirting boards, a low white panel radiator under the window, soft daylight, no furniture, no people, no text"),
    ("Uppreglat golv med isolering mellan träreglarna ovanpå en betongplatta",
     "room in a Swedish 1960s house during floor renovation, the old floor boards removed, revealing parallel wooden battens lying on a grey concrete slab with yellow mineral wool insulation between the battens, evenly spaced, white walls, a window with daylight, tidy work site, no people, no hands, no tools, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ NORRTÄLJE
"golvlaggare-norrtalje.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Norrtälje", "svc_label": "Golvläggare",
  "title": "Golvläggare i Norrtälje – golv i gamla gårdar och parstugor",
  "description": "Golvläggare i Norrtälje: breda plankgolv i redargårdar och parstugor, golv på torpargrund och varför en tät matta kan ge fukt. Gratis platsbesök.",
  "h1": "Golvläggare i Norrtälje",
  "lead": "I Roslagen står många gamla gårdar kvar, och i dem ligger ofta golv av breda plank på en grund som byggdes för ett hus som eldades varje dag. Golven går ofta att rädda, men de kräver en annan behandling än golvet i en modern villa. Geal Entreprenad AB slipar, lagar och lägger golv i hela Norrtälje kommun, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Plankgolv i gamla gårdar och parstugor.",
  "sections": [
    {"id": "redargardar", "anchor": "Gårdarna i Roslagen",
     "h2": "Redargårdar och parstugor som byggdes på höjden",
     "paras": [
       "Norrtälje kommun har 19 110 bostäder i småhus enligt SCB:s siffror för 2024, och 26 riksintresseområden för kulturmiljövården. I kommunens kulturmiljöutredning om Arholma från 2016 beskrivs redargårdarna som typiska för Roslagen. Det var större bondgårdar vars ägare också drev rederi, och de tog form under 1800-talet när sjöfarten blev mer storskalig.",
       "Utredningen berättar att flera parstugor byggdes på till två våningar under 1800-talet, när sjöfarten var som mest lönsam. Redargårdarnas huvudbyggnader har ofta timmerstomme inklädd med panel, och interiören inreddes enligt tidens ideal med påkostade paradrum. Mot slutet av 1800-talet kom sommargästerna, och flera gårdar blev pensionat. Ett hus med den historien kan ha golv från flera olika perioder i olika rum.",
     ],
     "aside": {"title": "Vanligt i äldre gårdar", "items": [
       "Breda plank på träbjälkar", "Golv som målats eller lackats om",
       "Mattor ovanpå originalgolvet", "Nivåskillnader mellan rummen"]}},
    {"id": "torpargrund", "h2": "Torpargrunden fungerade – på sitt sätt",
     "paras": [
       "Boverket beskriver den gamla torpargrunden som en grundmur av sten med bärande stenblock som bjälklaget vilade på, och med ventilationsöppningar i muren. På vintern isolerades grundmuren med snö och granris, så att ventilationen minskade och marken under huset inte kyldes ner så mycket.",
       "Huset värmdes med ved, och murstocken i grunden hölls varm hela året. Isoleringen i bjälklaget var tunn, så värme från rummen gick ner i grunden, och fukt från marken kunde vandra upp genom det otäta golvet. Tillsammans gjorde det att grunden fungerade förhållandevis väl ur fuktsynpunkt. Boverket påpekar samtidigt att torpargrunder inte är fria från skador – röta och besvärande lukt förekommer – och att de är betydligt sämre för energi och komfort än en modern krypgrund.",
     ],
     "aside": None},
    {"id": "vedspisen", "h2": "När vedspisen ersattes och golvet tätades",
     "paras": [
       "Boverket listar flera förändringar som har gjort gamla grunder fuktigare. När vedeldningen byttes mot till exempel direktverkande el slutade murstocken värma grunden, skorstensverkan minskade och grunden blev kallare och fuktigare. Tilläggsisolering mellan golvbjälkarna minskade värmen nedåt och gav högre luftfuktighet i grunden.",
       "En förändring rör golvet direkt: en ång- och lufttät golvmatta på golvplanken. Då kunde fukt inte längre torka ut genom bjälklaget, och fuktnivån i grunden ökade. Därför lägger vi inte en tät matta eller ett tätt golv på ett gammalt plankgolv utan att först ha tittat under huset. Ibland är det bättre att slipa fram planken och behandla dem med olja eller såpa än att täcka dem.",
     ],
     "aside": {"title": "Innan golvet täcks", "items": [
       "Titta i grunden under huset", "Känn efter lukt och mjuka partier",
       "Välj ett golv som inte stänger in fukt", "Planera ventilationen i grunden"]}},
    {"id": "plankgolv", "h2": "Breda plank som kan slipas igen",
     "paras": [
       "Golvbranschen skriver att ett massivt trägolv kan renoveras genom omslipning många gånger, så länge det finns en godtagbar tjocklek kvar mellan ytan och not och spår. I gamla plankgolv är planken ofta tjocka, men de kan ha slipats förut och slitits olika mycket. Vi mäter och provslipar en mindre yta innan hela rummet tas.",
       "Branschen påpekar också att trägolv krymper och sväller med luftens fuktighet och trivs bäst vid 15–25 grader och 30–60 procent relativ fuktighet. I ett hus som inte värms hela året blir växlingarna större, och springorna mellan planken öppnar och stänger sig med årstiderna. Det är något att räkna med, inte ett fel som går att slipa bort. Mer om slipning och ytbehandling finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "radon-norrtalje", "h2": "Radon genom sprickor i grunden",
     "paras": [
       "Norrtälje kommun skriver att radon från marken är den vanligaste källan till radon i byggnader och att gasen tar sig in genom sprickor och andra otätheter i grundkonstruktionen. Det enda sättet att veta halten är att mäta, och resultatet av en mätning av inomhusluften ska skickas till kommunens bygg- och miljönämnd.",
       "Mätningen ska pågå i minst två, helst tre månader under eldningssäsongen, oktober till april. Ska golvet i ett äldre hus göras om och grunden ändå ses över är det ett bra tillfälle att planera en mätning. Ska även taket på gården ses över finns mer på sidan om " + _L.format("takbyte-norrtalje.html", "takbyte i Norrtälje") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planerar vi golvjobbet i Norrtälje",
  "steps": [
    ("Besök", "Vi går igenom rummen, tittar under en matta och, om det går, in i grunden under huset."),
    ("Bedömning", "Vi mäter hur mycket trä som finns kvar och ser efter fukt, röta och lukt."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag där slipning, lagning och nytt golv är egna alternativ."),
    ("Material och resor", "Material beställs i god tid så att arbetet kan göras i ett sammanhang, även långt från stan."),
    ("Arbete", "Plank lagas, golvet slipas i flera steg eller ett nytt golv läggs på ett kontrollerat underlag."),
    ("Behandling", "Olja, såpa eller lack väljs efter hur huset används och värms under året."),
  ],
  "rot_h2": "ROT-avdrag för golvet i Norrtälje",
  "rot": [
    "Slipning och byte av golv räknas som rotarbete enligt Skatteverket, både i permanentbostaden och i ett fritidshus som du äger och använder. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, inom ett gemensamt tak på 75 000 kr för rot och rut.",
    "Material och resekostnader ger inget avdrag. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Norrtälje?",
  "price": [
    "Golvets skick, hur många plank som behöver lagas eller bytas och om grunden behöver åtgärdas först avgör mest. Avståndet till huset och om det ligger på en ö påverkar också. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi lägga en plastmatta på det gamla plankgolvet i vår gård i Roslagen?",
     "Det bör övervägas noga. Boverket beskriver hur en ång- och lufttät golvmatta på golvplank hindrar fukt från att torka ut genom bjälklaget så att grunden blir fuktigare."),
    ("Varför har grunden under vår gamla parstuga blivit fuktigare efter att vi bytte till elvärme?",
     "Enligt Boverket värmde murstocken tidigare grunden när huset eldades med ved. När eldningen upphör blir grunden kallare och fuktigare."),
    ("Går det att slipa breda plankgolv som redan har slipats flera gånger?",
     "Det beror på hur mycket trä som finns kvar ovanför not och spår. Vi mäter och gör en provslipning innan vi föreslår en helslipning."),
    ("Vart skickar vi resultatet av radonmätningen i Norrtälje?",
     "Norrtälje kommun anger att resultat från radonmätningar av inomhusluften ska skickas till bygg- och miljönämnden."),
    ("Varför öppnar sig springorna i golvet i vårt fritidshus på vintern?",
     "Trägolv krymper när luften är torr och sväller när den är fuktig. Golvbranschen anger 30–60 procent relativ fuktighet som bäst för trägolv, och i ett hus som inte värms jämnt året om blir växlingarna större."),
  ],
  "sources": [
    ("Norrtälje kommun – Kulturmiljöutredning nr 1: Arholma, 2016 (pdf)",
     "https://www.norrtalje.se/globalassets/dokument/dokument-kultur--fritid/dokument-kultur/dokument-riksintressen-i-norrtalje-kommun/arholma.pdf"),
    ("Norrtälje kommun – Inomhus- och boendemiljö",
     "https://www.norrtalje.se/info/bygga-bo-miljo/miljo-och-halsa/inomhus--och-boendemiljo/"),
    _BOV_KRYP, _GBR_MASSIV, _SCB, _SKV, _SKV2,
  ],
  "cta": ("Har du ett gammalt golv i en gård i Norrtälje?", "Boka ett gratis platsbesök så tittar vi på golvet och grunden och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Slipat brett plankgolv i ett rum i en gammal gård i Roslagen",
     "empty room in an old Swedish Roslagen farmhouse from the 1800s with a freshly sanded and soap-treated floor of very wide pine planks, white painted panelled walls, a small multi-pane window with view of a red barn and meadow, a white tiled stove in the corner, soft daylight, no furniture, no people, no text"),
    ("Stengrund under en gammal träbyggnad med ventilationsöppning",
     "exterior close-up of the low dry-stone foundation of an old falu red Swedish timber farmhouse in Roslagen, a small ventilation opening in the stone wall, wooden sill beam and red painted vertical boards above, grass and a few autumn leaves, natural light, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"golvlaggare-osteraker.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Österåker", "svc_label": "Golvläggare",
  "title": "Golvläggare i Österåker – jämna golv utan höga trösklar",
  "description": "Golvläggare i Österåker: färre trösklar i hus som byggts om i omgångar, bostadsanpassningsbidrag och rotavdrag som inte går ihop med bidrag.",
  "h1": "Golvläggare i Österåker",
  "lead": "En tröskel på några centimeter märks inte förrän någon i familjen börjar använda rullator eller rullstol. Då blir varje nivåskillnad mellan rummen ett hinder. Geal Entreprenad AB lägger nya golv och jämnar ut nivåer i hela Österåker – i Åkersberga, Svinninge och ute i skärgården – med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Jämna golv och färre trösklar.",
  "sections": [
    {"id": "akersberga", "anchor": "Husen i Österåker",
     "h2": "Småhus som har byggts om i omgångar",
     "paras": [
       "Enligt SCB fanns det 13 488 bostäder i småhus i Österåker 2024 – villor och radhus i Åkersberga, äldre sommarhus som i dag är helårsbostäder och hus ute i skärgården. Många av dem har fått nya golv rum för rum under årens lopp, och sällan med samma material eller samma underlag.",
       "Klinker i hallen, parkett i vardagsrummet, en plastmatta kvar i ett sovrum och en tillbyggnad med eget bjälklag: varje lager har sin tjocklek, och skillnaderna samlas vid dörröppningarna. För de flesta är det en skönhetsfråga. För den som har svårt att lyfta fötterna, går med rullator eller sitter i rullstol blir varje kant ett hinder. Därför börjar vi med att kartlägga var nivåerna skiljer sig åt och varför, innan vi föreslår något nytt golv.",
     ],
     "aside": {"title": "Där trösklarna brukar sitta", "items": [
       "Mellan hall och vardagsrum", "In till badrum och tvättstuga",
       "Vid en senare tillbyggnad", "Vid altan- och entrédörrar"]}},
    {"id": "nivaer", "h2": "Nivåskillnader som går att jämna ut",
     "paras": [
       "En tröskel kan finnas där för att täcka en skarv mellan två golvmaterial, för att hålla vatten borta eller för att golven på var sin sida helt enkelt har olika höjd. Den första sorten går ofta att ersätta med en låg övergångslist. Den sista kräver att något av golven byggs upp eller sänks.",
       "Vi mäter höjden i varje rum och ser vad som ligger under. Ibland räcker det att ett nytt golv i det lägre rummet byggs upp några millimeter, ibland behöver ett äldre golv rivas för att det nya ska hamna i samma nivå som grannrummet. Vid badrum och tvättstuga gäller andra regler, eftersom golvet där är en del av tätskiktet. Mer om golvtyper och underlag finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "tunna-golv", "h2": "Tunnare golv ger mindre skillnad i höjd",
     "paras": [
       "Golvets tjocklek avgör hur mycket nivån ändras. Enligt Golvbranschen har lamellparkett oftast en total tjocklek på 12–15 millimeter och läggs normalt flytande, medan självbärande produkter är 20–22 millimeter. Linoleum tillverkas i tjocklekar från 2 till 4 millimeter, och plastmattor av PVC är vanligen 1,4–4 millimeter tjocka.",
       "Ett tunt material gör det lättare att få samma nivå som ett angränsande rum, men det ställer större krav på att underlaget är plant. Linoleum och PVC finns också med stegljudsdämpande baksida. Vi visar vilka alternativ som ger lägst övergång i just ditt hus.",
     ],
     "aside": None},
    {"id": "bostadsanpassning", "h2": "Bostadsanpassningsbidrag för att ta bort trösklar",
     "paras": [
       "Har någon i hushållet en bestående funktionsnedsättning kan ni söka bostadsanpassningsbidrag hos Österåkers kommun. Bidraget gäller fasta funktioner i och i anslutning till bostaden, och borttagning av trösklar är ett av kommunens exempel, liksom ramper. Det ges inte för vanligt underhåll eller för tekniska brister i bostaden, och inte om behovet kan lösas med ett hjälpmedel.",
       "Till ansökan behövs ett intyg från till exempel en arbetsterapeut, sjukgymnast eller läkare, och ett medgivande från den som äger bostaden. Vid större anpassningar vill kommunen också ha ett förslag på hur bostaden ska anpassas, till exempel med ritning och offert. Boverkets handbok om bidraget ger fler exempel, som att höja altanen i nivå med bostadens ingång.",
     ],
     "aside": {"title": "Till ansökan", "items": [
       "Intyg från arbetsterapeut eller läkare", "Medgivande från fastighetsägaren",
       "Förslag med ritning och offert", "Ansökan via kommunens e-tjänst"]}},
    {"id": "rot-eller-bidrag", "h2": "Bidrag eller rotavdrag – inte båda för samma arbete",
     "paras": [
       "Skatteverket skriver att du inte kan få rotavdrag för ett arbete som du får bidrag eller annat ekonomiskt stöd för från stat, kommun eller region. Får ni bostadsanpassningsbidrag för att ta bort trösklarna gäller alltså inte rotavdraget för just det arbetet.",
       "Vill ni samtidigt byta golv i övriga rum kan den delen däremot ge rotavdrag på vanligt sätt. Därför delar vi upp kostnadsförslaget så att det tydligt framgår vilka arbeten som hör till anpassningen och vilka som inte gör det.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvarbetet till i Österåker",
  "steps": [
    ("Mätning", "Vi mäter golvhöjderna i alla rum och noterar var trösklar och nivåskillnader finns."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag där anpassningar och övrigt golvarbete står var för sig."),
    ("Underlag till ansökan", "Söker ni bostadsanpassningsbidrag kan kostnadsförslaget användas som underlag."),
    ("Rivning", "Trösklar och gamla golv tas bort där det behövs, och dörrar justeras."),
    ("Nytt golv", "Golvet läggs så att övergångarna mellan rummen blir så låga som möjligt."),
    ("Kontroll", "Vi går igenom övergångarna tillsammans och ser att dörrarna går fritt."),
  ],
  "rot_h2": "ROT-avdrag för golvarbete i Österåker",
  "rot": [
    "Skatteverket räknar slipning och byte av golv i ett småhus du äger och bor i som rotarbete. Avdraget är 30 procent av arbetskostnaden och högst 50 000 kr per person och år, inom ett gemensamt tak för rot och rut på 75 000 kr. Det gäller inte arbete som betalas med bidrag.",
    "Material och resor ingår inte i avdraget. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Österåker?",
  "price": [
    "Hur många trösklar och nivåskillnader som ska bort, golvytan och vilket material du väljer avgör mest. Om dörrar behöver kortas eller ett golv byggas upp tillkommer det. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi få bidrag för att ta bort trösklarna i vår villa i Åkersberga?",
     "Om någon i hushållet har en bestående funktionsnedsättning kan ni söka bostadsanpassningsbidrag hos Österåkers kommun. Borttagning av trösklar är ett av kommunens exempel på åtgärder."),
    ("Kan vi få rotavdrag för samma tröskelarbete som kommunen ger bidrag till?",
     "Nej. Skatteverket ger inte rotavdrag för arbete som får bidrag från stat, kommun eller region. Övrigt golvarbete i huset kan däremot ge rotavdrag."),
    ("Vilket golv ger lägst övergång mot klinkern i hallen?",
     "Det beror på klinkerns höjd. Tunnare material som linoleum eller plastmatta ger mindre nivåskillnad än parkett, men kräver ett mycket plant underlag. Vi mäter och föreslår."),
    ("Varför ligger golven i vårt hus i Åkersberga på olika höjd?",
     "När rummen har fått nya golv vid olika tillfällen, eller när huset har byggts till, hamnar golven ofta på olika höjd. Vi mäter alla rum och föreslår hur nivåerna kan jämnas ut."),
    ("Kan ert kostnadsförslag användas i ansökan om bostadsanpassning?",
     "Ja, vid större anpassningar vill kommunen ha ett förslag med ritning och offert. Vi delar upp förslaget så att anpassningen syns för sig."),
  ],
  "sources": [
    ("Österåkers kommun – Bostadsanpassning",
     "https://www.osteraker.se/omsorgstod/stodtillaldre/hjalpihemmet/bostadsanpassning.4.367d658917909e8fc2b5dd3.html"),
    ("Boverket – Bostadsanpassningsbidrag för att anpassa och komplettera fasta funktioner",
     "https://www.boverket.se/sv/babhandboken/bostadsanpassningsbidrag/villkor-for-bostadsanpassningsbidrag/anpassa-och-komplettera-fasta-funktioner/"),
    _GBR_LAMELL, _GBR_LINO, _GBR_PVC, _SCB, _SKV, _SKV2,
  ],
  "cta": ("Vill du få bort trösklarna hemma i Österåker?", "Boka ett gratis platsbesök så mäter vi nivåerna och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Hall och vardagsrum med samma golvnivå utan tröskel i en villa",
     "view from a hallway into a living room in a Swedish 1960s villa, light oak floor continuing through a wide open doorway with no threshold, only a thin flush transition, white walls and white door frame, daylight from a large window, empty room, no people, no text"),
    ("Låg övergångslist mellan klinker och trägolv vid en dörröppning",
     "close-up at floor level of a very low flush transition strip in a doorway between grey ceramic floor tiles and a light wooden floor in a Swedish house, white door frame, clean modern finish, natural light, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ BOTKYRKA
"golvlaggare-botkyrka.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Botkyrka", "svc_label": "Golvläggare",
  "title": "Golvläggare i Botkyrka – kataloghus, källare och trägolv",
  "description": "Golvläggare i Botkyrka: trägolv i Tullinges villor och kataloghus, golv i källare som ska bli bostad och radon i hus med blåbetong. Gratis platsbesök.",
  "h1": "Golvläggare i Botkyrka",
  "lead": "En källare som ska bli sovrum eller ett gammalt trägolv i en villa från 1920-talet – båda kräver att man vet vad som finns under. Geal Entreprenad AB lägger nya golv, slipar och lagar trägolv i hela Botkyrka, från Tullinge och Tumba till Vårsta och Norsborg, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Kataloghus, källargolv och trägolv.",
  "sections": [
    {"id": "tullinge", "anchor": "Husen i Botkyrka",
     "h2": "Villasamhället kring Tullinge station",
     "paras": [
       "Botkyrka har 12 555 bostäder i småhus enligt SCB:s siffror för 2024. Kommunens kulturmiljöprogram berättar att AB Separator anlade ett gjuteri vid Tullingesjöns sydspets vid förra sekelskiftet, och att Tullinge järnvägsstation öppnade 1903. Det blev starten för villasamhället. Den tidiga exploateringen sköttes av Tullinge AB, som köpt mark från Tullinge gård.",
       "Programmet beskriver villorna vid Tullingesjöns västra sida och på bergskrönet söder om järnvägen som hantverksmässigt utförda, i nationalromantisk och jugendinspirerad stil, ofta på höjder i landskapet och på stora tomter. Det är bebyggelsen från 1900–1940 som är mest kulturhistoriskt intressant i Tullinge.",
     ],
     "aside": None},
    {"id": "kataloghus", "h2": "Kataloghusen i Hamra egnahem",
     "paras": [
       "På 1920-talet planlades Hamra egnahem söder om järnvägen, för tjänstemän och arbetare på Separator. Samtidigt kom kataloghusen – monteringsfärdiga enfamiljshus som köptes direkt från en husleverantör. Kulturmiljöprogrammet nämner Boros villa Björkhamra som populär i Tullinges egnahemsområde, och kataloghus från 1920- och 40-talen dominerar området.",
       "I ett hus som är nära hundra år gammalt kan det ligga flera generationer golv ovanpå varandra. Är originalgolvet massivt trä kan det enligt Golvbranschen slipas om många gånger, så länge träet ovanför not och spår räcker. Ligger det i stället en senare parkett med tunt slitskikt är marginalen mindre – för lamellparkett är toppskiktet enligt branschens definition minst 2,5 millimeter. Vi tar reda på vilket det är innan vi föreslår slipning. Mer om golvtyper finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": {"title": "Golvskikt i ett äldre hus", "items": [
       "Originalgolv av massivt trä", "Linoleum eller plastmatta ovanpå",
       "Senare parkett eller laminat", "Spånskiva eller board som underlag"]}},
    {"id": "kallare-botkyrka", "h2": "Källaren var byggd för att vara kall",
     "paras": [
       "Har villan källare är det värt att veta hur den var tänkt. Boverket skriver att äldre hus ofta hade oisolerade och ouppvärmda källare. Ibland fanns en panna för ved, kol eller koks som värmde källaren med spillvärme, men generellt var källare kallare förr än i dag, och ventilationen i gamla källare är inte anpassad för bostadsändamål.",
       "Ska källaren bli sovrum eller kontor är golvet ofta det svåraste. Enligt Boverket kan en betongplatta i källare fuktas upp av marken, och ett ångtätt golvmaterial som läggs på betong i kontakt med mark utan skydd mot fukttransport kan ge fuktproblem. Boverket rekommenderar att fuktförhållandena i grunden utreds vid renovering. Vi börjar därför med att mäta fukten i plattan och se hur väggarna mot mark mår innan vi föreslår ett golv.",
     ],
     "aside": {"title": "Innan källargolvet byts", "items": [
       "Mät fukten i betongplattan", "Kontrollera väggarna mot mark",
       "Se över ventilationen", "Välj golv efter fukten, inte tvärtom"]}},
    {"id": "blabetong", "h2": "Blåbetong och radon när rummen görs om",
     "paras": [
       "Botkyrka kommun skriver att radon från marken är den vanligaste källan till radon i byggnader, men att även byggmaterial kan ge ifrån sig radon. Oftast är mängden för liten för att spela roll. Undantaget är blåbetong, som innehåller den uranrika bergarten alunskiffer och användes under perioden 1929–1978.",
       "Som villaägare ansvarar du själv för att ta reda på radonhalten. Kommunen rekommenderar en mätning om ingen har gjorts tidigare, om den senaste är äldre än tio år eller om ventilation eller uppvärmning ändras. Mätningen görs mellan 1 oktober och 30 april under minst två månader, med minst två dosor och minst en per våningsplan, men inte i kök eller badrum. Görs källaren om till sovrum ska den räknas med.",
     ],
     "aside": None},
    {"id": "segersjo", "h2": "Folkvillan, tjänstemannavillan och Segersjö",
     "paras": [
       "Enligt kulturmiljöprogrammet lanserades Folkvillan och Tjänstemannavillan på 1950-talet. Segersjö planerades under 1940-talet på mark som kommunen köpte av Tumba pappersbruk, främst för personalen vid bruket och sanatorierna i Uttran och Tullinge. Planen omfattade ungefär 450 lägenheter, och Segersjö blev det största bostadsområdet som byggdes i kommunen under 1950-talet.",
       "Programmet beskriver femtiotalets villor med friare planformer, stora perspektivfönster och entrédörrar i ek eller teak. I hus från den tiden är det vanligt att golven har bytts minst en gång. Vi lyfter en list och ser vad som finns under innan vi föreslår att slipa, lägga nytt ovanpå eller riva. Ska även taket ses över finns mer om " + _L.format("takrenovering-botkyrka.html", "takrenovering i Botkyrka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Golvjobbet i Botkyrka steg för steg",
  "steps": [
    ("Platsbesök", "Vi tittar på golven, lyfter en list och mäter fukten om golvet ligger mot mark."),
    ("Bedömning", "Vi tar reda på vilka golvskikt som finns och hur mycket trä som finns kvar."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag med slipning, lagning eller nytt golv som separata alternativ."),
    ("Skydd", "Rum som inte berörs skyddas mot damm och möbler flyttas undan."),
    ("Arbete", "Golvet slipas, lagas eller byts mot ett nytt på ett torrt och plant underlag."),
    ("Ytbehandling", "Lack, olja eller såpa läggs på, och du får råd om skötsel."),
  ],
  "rot_h2": "ROT-avdrag för golvarbetet i Botkyrka",
  "rot": [
    "Enligt Skatteverket ger slipning och byte av golv rätt till rotavdrag i ett småhus som du äger och bor i. Avdraget är 30 procent av arbetskostnaden, med ett tak på 50 000 kr per person och år och 75 000 kr för rot och rut tillsammans.",
    "Material och resor räknas inte med. Geal gör avdraget direkt på fakturan, så du betalar bara din del.",
  ],
  "price_h2": "Vad styr priset i Botkyrka?",
  "price": [
    "Golvytan, antalet golvskikt som ska bort och om underlaget måste torkas eller riktas påverkar mest. Ett källargolv kräver ofta mer förarbete än ett golv i bottenvåningen. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilket golv kan vi lägga i källaren i vår villa i Tullinge?",
     "Det beror på hur fuktig betongplattan är. Boverket varnar för att ett ångtätt golv på betong mot mark utan fuktskydd kan ge fuktproblem. Vi mäter fukten först."),
    ("Går det att slipa originalgolvet i ett kataloghus i Hamra egnahem?",
     "Ofta, om det är massivt trä och det finns tillräckligt kvar ovanför not och spår. Ligger det en senare parkett ovanpå tar vi reda på vad som finns under."),
    ("Kan det finnas blåbetong i vår källare i Botkyrka?",
     "Blåbetong användes 1929–1978 och kan ge förhöjd radon. Botkyrka kommun rekommenderar mätning om ingen har gjorts eller om den senaste är äldre än tio år."),
    ("Ska vi mäta radon innan källaren blir sovrum?",
     "Det är klokt. Mätningen görs mellan oktober och april i minst två månader, med minst en dosa per våningsplan som används som bostad."),
    ("Har husen i Segersjö samma golv som när de byggdes på 1950-talet?",
     "Det varierar från hus till hus, och många golv har bytts sedan dess. Vi lyfter en list och ser efter innan vi föreslår något."),
  ],
  "sources": [
    ("Botkyrka kommun – Kulturmiljöprogram (pdf)",
     "https://www.botkyrka.se/download/18.1fbbaae6170bff9469deb7f/1602575505534/Kulturmilj%C3%B6program.pdf"),
    ("Botkyrka kommun – Radon, råd och rekommendationer",
     "https://www.botkyrka.se/boende-och-narmiljo/bostad-och-tradgard/radon"),
    _BOV_KALLARE, _BOV_MARKFUKT, _GBR_MASSIV, _GBR_LAMELL, _SCB, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i huset i Botkyrka göras om?", "Boka ett gratis platsbesök så tittar vi på golvet och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Slipat trägolv i en äldre villa med spröjsade fönster i Tullinge",
     "empty room in a Swedish 1920s wooden catalogue house with a freshly sanded honey-coloured pine floor, white panelled door, small-paned white windows with a view of pine trees on a rocky hill, white skirting boards, soft daylight, no furniture, no people, no text"),
    ("Källarrum med betonggolv som förbereds för ett nytt golv",
     "basement room of an older Swedish villa being prepared for a new floor, bare grey concrete floor, whitewashed walls, small high window letting in daylight, a moisture meter and a roll of floor underlay standing by the wall, clean and tidy, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"golvlaggare-upplands-vasby.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Upplands Väsby", "svc_label": "Golvläggare",
  "title": "Golvläggare i Upplands Väsby – kedjehus, radon och trägolv",
  "description": "Golvläggare i Upplands Väsby: golv i kedjehus och suterränghus, radonmätning före och efter golvbytet och trägolv i villastaden. Gratis platsbesök.",
  "h1": "Golvläggare i Upplands Väsby",
  "lead": "När ett golv mot mark öppnas syns grunden för första gången på länge. I Upplands Väsby, där stora delar av marken räknas som högriskområde för radon, är det ett bra tillfälle att tänka på mer än själva golvet. Geal Entreprenad AB lägger nya golv och slipar gamla i hela kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Kedjehus, suterräng och radon.",
  "sections": [
    {"id": "sackgator", "anchor": "Husen i Upplands Väsby",
     "h2": "Säckgator med hus i samma utförande",
     "paras": [
       "SCB räknade 7 053 bostäder i småhus i Upplands Väsby 2024. Kommunens kunskapsunderlag för kulturmiljö beskriver hur de östra kommundelarna växte fram med en stor andel småhus och radhus under 1960- och 70-talen. Husen ligger i separata grupper längs säckgator, och varje grupp av atriumhus, radhus eller kedjehus är enhetligt utförd. Exempel är Sjukyrkoberget, Skälby, Fresta och Odenslunda.",
       "Underlaget beskriver husen som rationella, i en till två våningar eller i två våningar i suterräng. I ett suterränghus ligger nedre planet delvis mot mark, och där är golvet det som först påverkas av fukt och radon från marken. Ett golvbyte i det planet planerar vi därför annorlunda än i ett rum på övervåningen.",
     ],
     "aside": {"title": "Nedre plan mot mark", "items": [
       "Fukt i betongplattan", "Otätheter vid rör och väggar",
       "Golvval som tål underlaget", "Mätning före och efter"]}},
    {"id": "radonmark", "h2": "Stora delar av kommunen är högriskmark",
     "paras": [
       "Upplands Väsby kommun skriver att det finns stora områden i kommunen som ses som högriskområde för radon i marken, och att det i kommunen finns berggrund med hög halt av uran. Radon från marken kan komma in i huset beroende på markens radonhalt och genomsläpplighet, otätheter i grunden eller källarväggarna och undertryck inomhus.",
       "Kommunen råder den som har radon från marken att börja med att täta mot marken och se över ventilationen, och påpekar att alla åtgärder mot radon måste utföras fackmannamässigt och gärna med hjälp av en radonexpert. När ett golv på platta ändå ska öppnas för ett nytt golv är det rätt tillfälle att låta någon som kan radon titta på grunden, innan det nya golvet stänger igen den.",
     ],
     "aside": None},
    {"id": "matning-vasby", "h2": "Mät före och efter golvbytet",
     "paras": [
       "Mätsäsongen är 1 oktober till 30 april. Kommunen anger att en långtidsmätning ska pågå i minst 60 dagar i följd, och att den därför måste starta senast i slutet av februari. Det krävs minst två dosor och minst en på varje våning med bostadsrum. En korttidsmätning i minst sju dagar kan användas som vägledning, till exempel efter en åtgärd, men ger inget årsmedelvärde.",
       "Strålsäkerhetsmyndigheten rekommenderar enligt kommunen en ny mätning om det har gått mer än tio år, eller om det har gjorts byggnadsåtgärder som kan påverka radonhalten. Kommunen vill gärna ta del av mätprotokollet. Planerar du ett golvbyte i nedre planet kan det vara värt att mäta under vintern före och vintern efter.",
     ],
     "aside": None},
    {"id": "blabetong-bjalklag", "h2": "Blåbetong kan sitta även i bjälklaget",
     "paras": [
       "Kommunen skriver att blåbetong, ett byggmaterial av alunskiffer, innehåller radium och ger ifrån sig radon. Den kan finnas i källarväggar, ytterväggar och innerväggar, och ibland även i bjälklag. Gammamätning är enligt kommunen det bästa och enklaste sättet att ta reda på om huset är byggt med blåbetong.",
       "Kommer radonet bara från byggmaterialet kan bättre ventilation vara lösningen, enligt kommunen. För golvet betyder det att det inte hjälper att täta golvet om källan sitter i väggen. Därför är det bra att veta varifrån radonet kommer innan golvet och underlaget väljs.",
     ],
     "aside": None},
    {"id": "villastaden", "h2": "Sekelskiftesvillorna i Väsby villastad",
     "paras": [
       "Väsby villastad uppstod när industrin växte i början av 1900-talet. En stadsplan togs fram 1910 för ett stort markområde som hörde till Vilunda herrgård, men den genomfördes bara i delar. Typiskt för den ursprungliga bebyggelsen är faluröda villor från tiden kring 1900 och 1910 i nationalromantisk stil, med träfasader, vita knutar och småspröjsade fönster. Området bedöms som särskilt värdefullt enligt plan- och bygglagen.",
       "I de villorna kan originalgolven finnas kvar under senare mattor. Massiva trägolv kan enligt Golvbranschen slipas om flera gånger så länge träet räcker, och vi mäter tjockleken innan vi slipar. Mer om slipning och golvtyper finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ", och om taken på villorna på sidan om " + _L.format("takrenovering-upplands-vasby.html", "takrenovering i Upplands Väsby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi golv i Upplands Väsby",
  "steps": [
    ("Platsbesök", "Vi går igenom rummen och frågar om tidigare radonmätningar och renoveringar."),
    ("Underlag", "Vi tittar på hur golvet är byggt och var rör går genom plattan."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag med golv, underlag och eventuella förberedelser separat."),
    ("Öppning", "Gamla golv tas bort så att grunden kan ses över innan något stängs igen."),
    ("Läggning", "Det nya golvet läggs på ett torrt och plant underlag."),
    ("Efter jobbet", "Du får råd om skötsel och om när en ny radonmätning kan göras."),
  ],
  "rot_h2": "ROT-avdrag för golv i Upplands Väsby",
  "rot": [
    "Skatteverket godkänner rotavdrag för att slipa och byta golv i ett småhus du äger och bor i. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år. Tillsammans med rutavdrag är taket 75 000 kr.",
    "Varken material eller resor ger avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Upplands Väsby?",
  "price": [
    "Golvytan, hur många lager som ska bort och vilket skick underlaget har avgör mest. Rum i nedre plan mot mark kräver ofta mer förarbete. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Ligger vårt kedjehus i Upplands Väsby på högriskmark för radon?",
     "Kommunen skriver att stora områden räknas som högriskområde för radon i marken. Det enda sättet att veta halten i ditt hus är att mäta."),
    ("Hur sent på vintern kan vi börja en radonmätning i Upplands Väsby?",
     "Mätningen ska pågå minst två sammanhängande månader inom perioden 1 oktober–30 april, så den behöver starta senast i slutet av februari."),
    ("Kan blåbetong sitta i golvbjälklaget i vårt hus?",
     "Upplands Väsby kommun skriver att blåbetong ibland finns i bjälklag, inte bara i väggar. En gammamätning visar om huset innehåller blåbetong."),
    ("Är det värt att mäta radon både före och efter golvbytet i suterrängplanet?",
     "Det ger en bild av om arbetet har påverkat halten. Kommunen rekommenderar ny mätning efter byggnadsåtgärder som kan påverka radonhalten."),
    ("Finns originalgolven kvar i villorna i Väsby villastad?",
     "I en del hus ligger de kvar under senare mattor eller golv. Vi lyfter en list och mäter hur mycket trä som finns kvar innan vi föreslår slipning."),
  ],
  "sources": [
    ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö i Upplands Väsby (pdf)",
     "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf"),
    ("Upplands Väsby kommun – Radon",
     "https://www.upplandsvasby.se/bygga-bo-och-miljo/buller-och-luftkvalitet/radon"),
    _GBR_MASSIV, _SCB, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i huset i Upplands Väsby bytas?", "Boka ett gratis platsbesök så går vi igenom golvet och grunden och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Rum i nedre planet i ett suterränghus med nytt ljust golv",
     "empty lower-floor room in a Swedish 1970s split-level link house built into a slope, newly laid light grey oak floor, white walls, a wide window at ground level with view of a small garden and a wooden fence, soft daylight, no furniture, no people, no text"),
    ("Radhuslänga från 1970-talet i rött tegel och mörk träpanel",
     "row of Swedish 1970s split-level link houses built into a gentle wooded slope, lower floor partly below ground on the uphill side, red brick and dark painted wood panel facades, low pitched roofs with wide eaves, small front gardens and a quiet cul-de-sac, pine trees, autumn daylight, no people, no cars, no text"),
  ],
  "related": [],
},

}
