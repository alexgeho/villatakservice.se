# -*- coding: utf-8 -*-
"""Attefallshus – ortsidor v30: Solna, Sundbyberg, Upplands Väsby, Skärholmen (2026-10-27).
Hubb: attefallshus.html (TJ_HUB["attefallshus"]). Struktur som tj_v26_attefallshus.py. Tre bilder per sida.
Nybyggnad – inget rotavdrag; hero-punkterna kommer från TJ_SERVICES["attefallshus"]["trust"].

Lokal vinkel per sida:
Solna – "stora delar av Solna är kulturhistoriskt särskilt värdefulla": lov alltid i värdefull miljö, de utpekade
  miljöerna (Råsta egnahem, Råsunda villastad, norra Råsunda, Gamla Hagalund, Bergshamra by m.fl.), Solnakartan,
  handlingarna (nybyggnadskarta typ C, NCS-koder), kontrollplan utan certifierad KA, skyddsbestämmelser.
Sundbyberg – Duvbo: inget lovfritt komplementbostadshus och ingen ny friggebod sedan 1 december 2025, uthusen inne
  på tomterna (miljöprogrammet), gratis konsultationsmöte; utanför Duvbo: potten, prickmark och störningsskydd,
  medgivande från kommunstyrelsen för allmän plats, frivilligt bygglov kostar som vanligt lov.
Upplands Väsby – kommunen använder inte längre ordet attefallshus: 45/65 m², 30/50 m², 4,0/4,5 m, räkneexemplet
  15 + 20 = 10 kvar, VA-avgift även vid inkoppling på befintlig servis; Bollstanäs–Gamla vägen särskilt värdefullt.
Skärholmen – radhustomterna i den storskaliga stadsdelen: husgruppens form gäller även en bod, 4,5 meter och
  medgivandets innehåll, mindre än huset det kompletterar, prickmark, servisanmälan och bostadsenhetsavgift.

Fakta endast från källorna i respektive 'sources', öppnade med curl (Mozilla-UA) 2026-10-27, alla svarade 200; pdf:erna
har textlager. Skatteverket återställde anslutningen härifrån – samma URL och formulering som v22–v26.
Strukna: avgiftsbelopp, handläggningstider utöver Solnas uppgift om tio veckor, namn på enskilda fastigheter.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_REG = _L.format("attefallshus-regler.html", "reglerna för attefallshus")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_ROT_NY = ("Skatteverket skriver att det inte går att få rotavdrag för att bygga en helt ny bostad, och inte heller "
           "för ett nytt hus, en friggebod, ett garage eller en liknande fristående byggnad. Ett komplementbostadshus "
           "står fritt på tomten, så kostnadsförslaget för huset räknas utan avdrag.")
_SOLNA_K = ("Solna stad – Komplementbyggnad", "https://www.solna.se/bygga-bo--miljo/bygga/guide/vanliga-byggatgarder/komplementbyggnad")
_SOLNA_KULT = ("Solna stad – Kulturmiljöer i Solna", "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna")
_SOLNA_FRI = ("Solna stad – Bygglovsfria åtgärder", "https://www.solna.se/bygga-bo--miljo/bygga/bygglov/bygglovsfria-atgarder")
_SBG = "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/"
_SBG_KBH = ("Sundbybergs stad – Komplementbostadshus, bygglovsbefriat", _SBG + "bygglovsguide/komplementbostadshus---bygglovsbefriat")
_SBG_DUVBO = ("Sundbybergs stad – Duvbo", _SBG + "duvbo")
_SBG_PROG = ("Sundbybergs stad – Miljöprogram Duvbo (pdf)",
             "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf")
_VASBY_K = ("Upplands Väsby kommun – Nybyggnad, komplementbyggnad",
            "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/nybyggnad---komplementbyggnad")
_VASBY_KU = ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö (pdf)",
             "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf")
_VASBY_KULT = ("Upplands Väsby kommun – Kulturhistoriska byggnader, kulturmiljöer",
               "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/kulturhistoriska-byggnader-kulturmiljoer")
_STH_KBH = ("Stockholms stad – Komplementbostadshus (bygglovsbefriad)",
            "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/komplementbostadshus-bygglovsbefriad/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_SVOA = ("Stockholm Vatten och Avfall – Koppla in vatten och avlopp till nybyggd villa eller attefallshus",
         "https://www.svoa.se/villa-och-radhus/vatten-och-avlopp/bygga-om/")

PAGES_TJ = {

# ------------------------------------------------------------------ SOLNA
"attefallshus-solna.html": {
  "kind": "district", "service": "attefallshus", "ort": "Solna", "svc_label": "Attefallshus",
  "title": "Attefallshus i Solna – kulturmiljöerna och lovet",
  "description": "Attefallshus i Solna: när bygglov krävs, de utpekade miljöerna i Råsunda, Råsta och Bergshamra, "
                 "Solnakartan, handlingarna och kontrollplanen.",
  "h1": "Attefallshus i Solna",
  "lead": "Solna stad skriver att stora delar av staden är kulturhistoriskt särskilt värdefulla, och där krävs alltid "
          "bygglov för ett komplementbostadshus. Geal Entreprenad AB kontrollerar din fastighet i Solnakartan, tar "
          "fram handlingarna och bygger huset nyckelfärdigt.",
  "card": "Kulturmiljöerna, kartan och lovet.",
  "sections": [
    {"id": "alltid-lov-solna", "anchor": "När lov krävs",
     "h2": "När bygglov krävs i Solna",
     "paras": [
       "Solna stad skriver att du alltid behöver söka bygglov för en komplementbyggnad eller ett "
       "komplementbostadshus inom ett kulturhistoriskt värdefullt område eller till en kulturhistoriskt värdefull "
       "byggnad. Staden lägger till att stora delar av Solna är kulturhistoriskt särskilt värdefulla.",
       "Bygglov krävs också om huset placeras närmare tomtgräns än 4,5 meter utan grannens skriftliga medgivande, "
       "närmare än 30 meter från ett järnvägsspårs mitt, utanför tomten eller om det blir större än vad lagen "
       "tillåter. Inom detaljplan är gränserna 30 kvadratmeter byggnadsarea, 4,0 meter i nock och 45 "
       "kvadratmeter sammanlagt för alla komplementbyggnader på tomten. Huset får inte heller vara större än "
       "bostadshuset det kompletterar.",
     ],
     "aside": {"title": "Lov krävs bland annat", "items": [
       "I kulturhistoriskt värdefull miljö", "Närmare gräns än 4,5 m utan medgivande",
       "Närmare järnväg än 30 m", "Över 30 m² eller 4,0 m inom plan"]}},
    {"id": "miljoerna-solna", "h2": "Miljöerna med villor och egnahem",
     "paras": [
       "Solna stad listar ett stort antal sammanhängande kulturhistoriskt värdefulla miljöer, där helhetsintrycket "
       "är det viktiga. Bland dem finns flera villa- och småhusområden: Råsta egnahem, villabebyggelsen i norra "
       "Råsunda, Råsunda villastad, Gamla Hagalund, Bergshamra by, Alnäs och Stocksundstorp samt Solna kyrkby med "
       "radhusbebyggelse. Listan bygger på skriften Kulturmiljöer i Solna från 1988.",
       "Står villan i någon av de miljöerna behöver ett nytt gårdshus anpassas till helheten – i placering, storlek, "
       "takform och material. Staden har också en karta över kulturhistoriskt klassade byggnader. Är själva villan "
       "utpekad krävs lov även om tomten ligger utanför en sammanhängande miljö.",
     ],
     "aside": {"title": "Exempel på utpekade miljöer", "items": [
       "Råsta egnahem", "Råsunda villastad", "Norra Råsunda", "Gamla Hagalund", "Bergshamra by"]}},
    {"id": "handlingar-solna", "h2": "Handlingarna till ansökan",
     "paras": [
       "Till en bygglovsansökan vill Solna stad ha en situationsplan baserad på nybyggnadskarta typ C, plan-, fasad- "
       "och sektionsritningar, en arearedovisning, en översiktlig beskrivning och en material- och "
       "kulörbeskrivning med NCS-koder. Ibland behövs fler underlag, till exempel markplaneringsritningar med "
       "befintliga och nya marknivåer om tomten lutar.",
       "Staden skriver att en kontrollplan ska skickas in och fastställas innan startbeskedet. Bygger du som "
       "privatperson en komplementbyggnad till ett en- eller tvåbostadshus behöver du ingen certifierad "
       "kontrollansvarig. Enligt staden är handläggningstiden högst tio veckor, och en komplett ansökan kortar den.",
     ],
     "aside": None},
    {"id": "skydd-solna", "h2": "Kartan, planen och skyddsbestämmelserna",
     "paras": [
       "Stora delar av Solna har detaljplan, och i Solnakartan går det att söka på fastigheten för att se både "
       "planen och om byggnaden eller området är kulturhistoriskt värdefullt. Ett lovfritt komplementbostadshus till "
       "en villa får strida mot detaljplanen, men inte mot skyddsbestämmelser om markförorening, olyckor eller "
       "översvämning.",
       "Ligger tomten nära en strand kan strandskyddsdispens behövas. Vi kontrollerar allt det här innan vi ritar, "
       "så att du vet om det blir lov eller inte innan du bestämmer dig. Måtten och paragraferna finns samlade i " +
       _REG + ", och vill du hellre bygga ihop med huset finns " +
       _L.format("tillbyggnad-solna.html", "tillbyggnad i Solna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Solna",
  "steps": [
    ("Solnakartan", "Detaljplan, kulturmiljö och strandskydd kontrolleras."),
    ("Platsbesök", "Vi mäter befintliga byggnader, gränser och marknivåer."),
    ("Handlingar", "Ritningar, arearedovisning och kulörbeskrivning med NCS-koder."),
    ("Lov eller anmälan", "Bygglov i värdefull miljö, annars anmälan för installationerna."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset tas i bruk när slutbeskedet har kommit."),
  ],
  "rot_h2": "Inget rotavdrag för ett nytt gårdshus",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Solna?",
  "price": [
    "Om bygglov och kulturmiljöanpassade ritningar behövs, husets storlek och planlösning, kök och badrum, "
    "grundläggning och marknivåer, och hur långt ledningarna ska dras. Efter ett gratis platsbesök får du ett "
    "skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för ett attefallshus i Råsunda villastad?",
     "Råsunda villastad finns med bland Solnas sammanhängande kulturhistoriskt värdefulla miljöer. Solna stad skriver "
     "att bygglov alltid krävs för ett komplementbostadshus i ett sådant område."),
    ("Behövs en kontrollansvarig för ett gårdshus i Solna?",
     "Inte en certifierad, om du som privatperson bygger till ett en- eller tvåbostadshus. En kontrollplan ska ändå "
     "skickas in och fastställas."),
    ("Vad händer om vår villa i Solna ligger utanför detaljplan?",
     "Då är gränserna större: 50 kvadratmeter byggnadsarea och 4,5 meter i nock, enligt Solna stad. I en "
     "kulturhistoriskt värdefull miljö krävs ändå bygglov."),
    ("Hur lång tid tar ett bygglov i Solna?",
     "Solna stad anger en handläggningstid på högst tio veckor och skriver att en komplett ansökan kortar tiden."),
    ("Var ser vi om vår villa i Solna är kulturhistoriskt värdefull?",
     "I Solnakartan, där du söker på fastigheten. Där visas både detaljplan och kulturhistoriskt värdefulla "
     "byggnader och områden."),
    ("Får gårdshuset i Solna stå närmare tomtgränsen än 4,5 meter?",
     "Ja, om berörd granne ger sitt skriftliga medgivande. Utan medgivande krävs bygglov enligt Solna stad, och "
     "för gatu- eller parkmark är det oftast staden som ska tillfrågas."),
    ("Vilken karta behövs till situationsplanen i Solna?",
     "Staden vill ha en situationsplan baserad på nybyggnadskarta typ C för nybyggnad. Kartunderlaget kostar pengar."),
  ],
  "sources": [_SOLNA_K, _SOLNA_KULT, _SOLNA_FRI, _SKV],
  "cta": ("Vill du bygga ett gårdshus i Solna?",
          "Boka ett gratis platsbesök, så går vi igenom kartan, kulturmiljön och handlingarna innan du får ett "
          "skriftligt kostnadsförslag."),
  "img": [
    ("Litet gårdshus med stående panel bakom en äldre villa i en villastad",
     "small new Swedish garden cottage with vertical light grey wooden cladding and a gable roof with black "
     "concrete tiles, placed at the back of a garden behind a 1920s plastered villa with a hipped roof, mature "
     "trees, early summer daylight" + _SFX),
    ("Villagata med äldre egnahem och staket",
     "quiet Swedish street with small 1910s and 1920s wooden owner-built houses behind white picket fences, "
     "lilac bushes and fruit trees, gravel pavement, soft morning light" + _SFX),
    ("Ritningsrulle och kulörprover på ett bord i en trädgård",
     "rolled architectural drawings tied with a band and a small fan of paint colour samples lying on a wooden "
     "garden table in front of a lawn, blank paper, no readable text, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SUNDBYBERG
"attefallshus-sundbyberg.html": {
  "kind": "district", "service": "attefallshus", "ort": "Sundbyberg", "svc_label": "Attefallshus",
  "title": "Attefallshus i Sundbyberg – Duvbo och resten av staden",
  "description": "Attefallshus i Sundbyberg: varför Duvbo inte tillåter lovfria gårdshus, potten på 45 kvadratmeter, "
                 "medgivanden, störningsskydd och frivilligt bygglov.",
  "h1": "Attefallshus i Sundbyberg",
  "lead": "I Sundbyberg går skiljelinjen vid Duvbo. Där går det inte att bygga ett lovfritt komplementbostadshus, "
          "medan villatomter på andra håll i staden följer de vanliga reglerna. Geal Entreprenad AB reder ut vad "
          "som gäller för din tomt och bygger huset nyckelfärdigt.",
  "card": "Duvbo, potten och medgivandena.",
  "sections": [
    {"id": "duvbo-attefall", "anchor": "Duvbo",
     "h2": "Inga lovfria gårdshus i Duvbo",
     "paras": [
       "Sundbybergs stad skriver att bygglovslättnaden för komplementbostadshus inte gäller för kulturhistoriskt "
       "värdefulla byggnader, och att det i riksintresset Duvbo inte är möjligt att uppföra ett bygglovsbefriat "
       "komplementbostadshus. Sedan den 1 december 2025 får du inte heller uppföra, flytta eller bygga till en "
       "friggebod i Duvbo. River du en friggebod kan du inte bygga den på nytt.",
       "Planerar du en nybyggnad i Duvbo erbjuder staden ett kostnadsfritt konsultationsmöte med någon av stadens "
       "arkitekter. Där får du veta vad som är möjligt på fastigheten och vilka krav som kan ställas på gestaltning "
       "och utformning. Det är dit vi råder dig att gå först, innan några ritningar beställs.",
     ],
     "aside": {"title": "I Duvbo", "items": [
       "Inget lovfritt komplementbostadshus", "Ingen ny friggebod sedan 1 december 2025",
       "Gratis konsultationsmöte med stadens arkitekt"]}},
    {"id": "uthusen-duvbo", "h2": "Uthusen i Duvbos trädgårdar",
     "paras": [
       "Stadens miljöprogram för Duvbo beskriver hur de gamla uthusen står inne på tomterna, ofta dolda av "
       "växtlighet, och hur husen ligger på tomtens högsta punkt med breda förgårdar mot gatan. Programmet räknar "
       "den glesa bebyggelsen och den karaktäristiska förgårdsmarken till områdets kulturmiljövärden, och ber "
       "fastighetsägare lägga tillbyggnader och uthus så att öppenheten bevaras och gatubilden förändras så lite som "
       "möjligt.",
       "Om staden efter en prövning kan godta ett nytt gårdshus på en tomt i Duvbo blir det alltså ett hus långt "
       "in på tomten, lågt och enkelt, i trä och med ett tak som passar villans. Vi ritar förslaget efter "
       "programmet och tar med det till konsultationsmötet.",
     ],
     "aside": None},
    {"id": "potten-sundbyberg", "h2": "Utanför Duvbo – potten och planen",
     "paras": [
       "Utanför Duvbo kan ett komplementbostadshus vara lovfritt om det är högst 30,0 kvadratmeter byggnadsarea, "
       "mindre än huset det kompletterar och högst 4,0 meter i nock. Varje tomt inom detaljplan har en sammanlagd "
       "pott på 45 kvadratmeter för sådana byggnader, och staden påpekar att tidigare attefallshus, friggebodar och "
       "lovfria skärmtak räknas in.",
       "Huset får strida mot detaljplanen, utom där planen har bestämmelser om skydd mot störningar. Vill du ha ett "
       "bindande besked kan du söka frivilligt bygglov – staden skriver att det kostar lika mycket som ett vanligt "
       "bygglov. Installeras vatten, avlopp, ventilation eller eldstad krävs anmälan och startbesked innan bygget "
       "börjar.",
     ],
     "aside": {"title": "Utan lov – om inget annat gäller", "items": [
       "Högst 30,0 m² byggnadsarea", "Högst 4,0 m i nock", "Pott 45,0 m² på tomten"]}},
    {"id": "medgivande-sundbyberg", "h2": "Medgivanden från grannar och staden",
     "paras": [
       "Huset ska stå minst 4,5 meter från gränsen mot granne, samfällighet eller allmän plats, som gatu- och "
       "parkmark. Står det närmare behövs skriftligt medgivande. För allmän platsmark är det oftast staden som är "
       "huvudman, och i Sundbyberg skickas förfrågan skriftligt till kommunstyrelsen.",
       "Grannemedgivandet ska vara underskrivet av berörda grannar, och avståndet till gränsen ska vara inritat på "
       "situationsplanen. Huset ska också stå minst 30 meter från ett järnvägsspår om inte infrastrukturförvaltaren "
       "har gett sitt medgivande. Måtten finns samlade i " + _REG + ", och om du hellre bygger ihop med villan "
       "finns " + _L.format("tillbyggnad-sundbyberg.html", "tillbyggnad i Sundbyberg") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Sundbyberg",
  "steps": [
    ("Läget", "Duvbo, kulturvärden och detaljplan kontrolleras först."),
    ("Platsbesök", "Vi mäter tomten, befintliga byggnader och avstånden."),
    ("Medgivanden", "Grannar och, vid allmän plats, kommunstyrelsen."),
    ("Lov eller anmälan", "Bygglov, frivilligt bygglov eller anmälan för installationerna."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset tas i bruk när slutbeskedet har kommit."),
  ],
  "rot_h2": "Inget rotavdrag för ett nytt gårdshus",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Sundbyberg?",
  "price": [
    "Om huset kräver bygglov, storlek och planlösning, kök och badrum, grundläggning, ledningsdragning och hur "
    "material kan bäras in på tomten. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi bygga ett attefallshus i Duvbo?",
     "Inte utan bygglov. Sundbybergs stad skriver att det inte är möjligt att uppföra ett bygglovsbefriat "
     "komplementbostadshus i riksintresset Duvbo."),
    ("Får vi bygga om vår gamla friggebod i Duvbo?",
     "Nej. Sedan den 1 december 2025 får du inte uppföra, flytta eller bygga till en friggebod i Duvbo, och en "
     "friggebod som rivs kan inte byggas upp igen."),
    ("Hur långt från järnvägen måste gårdshuset stå i Sundbyberg?",
     "Minst 30 meter från spåret, om inte infrastrukturförvaltaren har gett sitt medgivande. Annars krävs bygglov."),
    ("Vem ger medgivande om gårdshuset hamnar nära gatan i Sundbyberg?",
     "För allmän platsmark är det oftast staden. I Sundbyberg skickas förfrågan skriftligt till kommunstyrelsen."),
    ("Vad kostar ett frivilligt bygglov i Sundbyberg?",
     "Staden skriver att ett frivilligt bygglov kostar lika mycket som ett vanligt bygglov."),
    ("Får ett gårdshus i Sundbyberg stå på prickmark?",
     "Ett lovfritt komplementbostadshus får strida mot detaljplanen, enligt staden, utom där planen har "
     "bestämmelser om skydd mot störningar. I Duvbo gäller det inte, eftersom lovfriheten inte gäller där."),
    ("Räknas vårt skärmtak in i potten i Sundbyberg?",
     "Ja, om det är byggt utan lov. Staden räknar tidigare attefallshus, friggebodar och lovfria skärmtak in i de "
     "45 kvadratmetrarna."),
  ],
  "sources": [_SBG_KBH, _SBG_DUVBO, _SBG_PROG, _SKV],
  "cta": ("Vill du bygga ett gårdshus i Sundbyberg?",
          "Boka ett gratis platsbesök, så går vi igenom läget, potten och medgivandena innan du får ett skriftligt "
          "kostnadsförslag."),
  "img": [
    ("Litet gårdshus i trä långt in på en lummig tomt bakom en äldre villa",
     "small new Swedish timber garden house painted dark red with white trim and a low gable roof, placed far back "
     "in a lush garden behind an old wooden villa with carpentry details, fruit trees and lilac, summer daylight"
     + _SFX),
    ("Gammalt uthus som skymtar bakom fruktträd och buskar",
     "old small red wooden outbuilding partly hidden behind apple trees and bushes in a large old villa garden, "
     "grass and stone path, soft afternoon light" + _SFX),
    ("Spjälstaket och häck mot en grusväg i ett villaområde",
     "white wooden picket fence and leafy hedge along a winding gravel road in an old Swedish villa area on a "
     "hill, pine trees, summer daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"attefallshus-upplands-vasby.html": {
  "kind": "district", "service": "attefallshus", "ort": "Upplands Väsby", "svc_label": "Attefallshus",
  "title": "Attefallshus i Upplands Väsby – potten och Bollstanäs",
  "description": "Attefallshus i Upplands Väsby: lovfri komplementbyggnad inom och utanför plan, potten, VA-avgiften "
                 "och villorna vid Gamla vägen i Bollstanäs.",
  "h1": "Attefallshus i Upplands Väsby",
  "lead": "Upplands Väsby kommun använder inte längre orden friggebod och attefallshus – allt kallas lovfri "
          "komplementbyggnad. Reglerna är desamma i grunden, men kommunen förklarar dem med egna exempel. Geal "
          "Entreprenad AB räknar på din tomt och bygger komplementbostadshuset nyckelfärdigt.",
  "card": "Potten, VA-avgiften och Bollstanäs.",
  "sections": [
    {"id": "begreppen-vasby", "anchor": "Reglerna",
     "h2": "Lovfri komplementbyggnad – kommunens ord",
     "paras": [
       "Kommunen skriver att termerna friggebod och attefallshus inte längre gäller efter ändringarna i plan- och "
       "bygglagen. I stället används begreppet lovfri komplementbyggnad, och i det ingår komplementbostadshus – en "
       "komplementbyggnad avsedd för permanentboende. En komplementbyggnad ska vara fristående och inte sitta ihop "
       "med huvudbyggnaden.",
       "Inom detaljplan får alla komplementbyggnader på tomten tillsammans vara högst 45,0 kvadratmeter, och den "
       "största högst 30,0 kvadratmeter. Utanför detaljplan är gränserna 65,0 och 50,0 kvadratmeter. Nockhöjden får "
       "vara högst 4,0 meter inom plan och 4,5 meter utanför, och byggnaden ska vara mindre än huvudbyggnaden.",
     ],
     "aside": {"title": "Inom / utanför plan", "items": [
       "Sammanlagt 45,0 / 65,0 m²", "Största byggnaden 30,0 / 50,0 m²", "Nock 4,0 / 4,5 m"]}},
    {"id": "rakneexempel", "h2": "Räkneexemplet med potten",
     "paras": [
       "Kommunen ger ett tydligt exempel. Har du inom detaljplan redan byggt en friggebod på 15 kvadratmeter och ett "
       "attefallshus på 20 kvadratmeter utan lov, har du bara 10 kvadratmeter kvar att bygga lovfritt. Ett annat "
       "exempel: ett garage på 35 kvadratmeter kan inte byggas lovfritt inom plan, även om potten inte är "
       "utnyttjad, eftersom den största byggnaden får vara högst 30 kvadratmeter.",
       "Vi börjar därför varje projekt i Upplands Väsby med att mäta allt som redan står på tomten. Det avgör om ett "
       "komplementbostadshus kan byggas utan lov, om det behöver bli mindre eller om det är bättre att söka bygglov "
       "direkt.",
     ],
     "aside": {"title": "Exemplet inom plan", "items": [
       "Friggebod 15 m²", "Attefallshus 20 m²", "Kvar: 10 m²"]}},
    {"id": "va-vasby", "h2": "VA-avgift även utan ny servis",
     "paras": [
       "Ska komplementbyggnaden ha vatten eller avlopp skriver kommunen att du behöver betala en VA-avgift, och att "
       "det gäller även om du inte gör några nya anslutningar utan kopplar på den befintliga anslutningen på tomten. "
       "Installation eller väsentlig ändring av VA, eldstad, rökkanal eller ventilation kan dessutom kräva anmälan.",
       "Kommunen påminner också om att en lovfri komplementbyggnad inte får vara en betydande olägenhet för "
       "omgivningen, och att samma krav på utformning, gestaltning och tekniska egenskaper gäller som för en "
       "lovpliktig byggnad. Det är alltså inte enklare att bygga – bara att slippa ansökan.",
     ],
     "aside": None},
    {"id": "bollstanas", "h2": "Villorna vid Gamla vägen i Bollstanäs",
     "paras": [
       "Kommunens kunskapsunderlag för kulturmiljö pekar ut Bollstanäs–Gamla vägen som särskilt värdefullt "
       "bebyggelseområde enligt plan- och bygglagen. Där finns villor från sekelskiftet 1900 på stora tomter i en "
       "sluttning ner mot Norrviken, med grusvägar som följer terrängen. Enligt kommunen krävs bygglov för en "
       "komplementbyggnad inom ett kulturhistoriskt särskilt värdefullt område.",
       "Underlaget räknar enkla, äldre uthus byggda i anslutning till huvudbyggnaden till områdets bevarandevärda "
       "karaktärsdrag, och ger råd om att ny bebyggelse ska vara mindre volymer med bevarad öppenhet mellan tomterna. "
       "Större volymer, schaktning och höga stödmurar bör undvikas. Ett gårdshus här ritar vi därför lågt och enkelt, "
       "anpassat till marken. Måtten finns samlade i " + _REG + ".",
     ],
     "aside": {"title": "Bollstanäs–Gamla vägen", "items": [
       "Särskilt värdefullt område", "Villor från sekelskiftet 1900", "Mindre volymer, ingen schaktning"]}},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Upplands Väsby",
  "steps": [
    ("Platsbesök", "Vi mäter allt som redan står på tomten och räknar potten."),
    ("Planen och kulturmiljön", "Detaljplan och kunskapsunderlaget kontrolleras."),
    ("Ritningar", "Ett hus som ryms i potten och passar platsen."),
    ("Lov eller anmälan", "Bygglov där det krävs, annars anmälan för installationerna."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset tas i bruk när slutbeskedet har kommit."),
  ],
  "rot_h2": "Inget rotavdrag för ett nytt gårdshus",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Upplands Väsby?",
  "price": [
    "Husets storlek och planlösning, om bygglov behövs, kök och badrum, grundläggning i sluttning, VA-avgiften och "
    "ledningsdragningen. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Heter det fortfarande attefallshus i Upplands Väsby?",
     "Kommunen skriver att termerna friggebod och attefallshus inte längre gäller. I stället används lovfri "
     "komplementbyggnad, där komplementbostadshus ingår."),
    ("Hur stort gårdshus får vi bygga utanför detaljplan i Upplands Väsby?",
     "Den största byggnaden får vara högst 50,0 kvadratmeter och alla komplementbyggnader tillsammans högst 65,0. "
     "Nocken får vara högst 4,5 meter."),
    ("Måste vi betala VA-avgift om gårdshuset kopplas på villans ledningar i Upplands Väsby?",
     "Ja. Kommunen skriver att VA-avgift ska betalas även om du kopplar på den befintliga anslutningen på tomten."),
    ("Behöver vi bygglov för ett gårdshus vid Gamla vägen i Bollstanäs?",
     "Bollstanäs–Gamla vägen är utpekat som särskilt värdefullt område. Kommunen skriver att bygglov krävs för en "
     "komplementbyggnad i ett sådant område."),
    ("Kan vi bygga ett garage på 35 kvadratmeter utan lov i Upplands Väsby?",
     "Inte inom detaljplan. Kommunen skriver att den största byggnaden får vara högst 30,0 kvadratmeter, även om "
     "potten inte är använd."),
  ],
  "sources": [_VASBY_K, _VASBY_KU, _VASBY_KULT, _SKV],
  "cta": ("Vill du bygga ett gårdshus i Upplands Väsby?",
          "Boka ett gratis platsbesök, så räknar vi på potten och platsen innan du får ett skriftligt "
          "kostnadsförslag."),
  "img": [
    ("Nytt gårdshus med pulpettak på en tomt bredvid ett äldre uthus",
     "small new Swedish guest house with light wooden cladding and a mono-pitch roof on a sloping garden plot, an "
     "old red wooden outbuilding beside it and a large 1900s wooden villa in the background, pines and oaks, "
     "summer daylight" + _SFX),
    ("Grusväg längs en sluttning med äldre villor och höga tallar",
     "narrow gravel road following a slope with old Swedish wooden villas on large plots, tall pine and oak trees, "
     "glimpse of a lake below, quiet late afternoon" + _SFX),
    ("Rensbrunn och nya rör i ett schakt mellan villa och gårdshus",
     "short open trench in a lawn with new grey plastic drain pipes leading to an inspection chamber between an "
     "older villa and a new small garden house, spade lying beside, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"attefallshus-skarholmen.html": {
  "kind": "district", "service": "attefallshus", "ort": "Skärholmen", "svc_label": "Attefallshus",
  "title": "Attefallshus i Skärholmen – små radhustomter",
  "description": "Attefallshus i Skärholmen: radhus- och kedjehustomter i Sätra och Bredäng, husgruppens form, 4,5 "
                 "meter och medgivanden, prickmark och servisanmälan.",
  "h1": "Attefallshus i Skärholmen",
  "lead": "I Sätra, Bredäng och Vårberg står de flesta småhus i gruppbyggda rader på små tomter. Ett "
          "komplementbostadshus kan ändå vara möjligt, men tomtens mått och grannarna avgör mycket. Geal "
          "Entreprenad AB mäter upp tomten, räknar på reglerna och bygger huset nyckelfärdigt.",
  "card": "Radhustomterna och grannarna.",
  "sections": [
    {"id": "tomterna-skarholmen", "anchor": "Tomterna",
     "h2": "Gruppbyggda hus på små tomter",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver småhusen i de storskaliga "
       "stadsdelarna – Bredäng, Sätra, Skärholmen och Vårberg – som strikt grupperade radhus, kedjehus, villor och "
       "atriumhus på små tomter. Färgsättningen är enhetlig inom husgrupperna, och taken är oftast platta eller "
       "pulpettak.",
       "Enligt områdesfakta för 2025 fanns 1 991 småhus i Skärholmens stadsdelsområde, nästan alla med äganderätt. "
       "I Sätra fanns 536 ägda småhus och i Bredäng 320. Det betyder att det är du som fastighetsägare som "
       "ansvarar för att ett lovfritt hus uppfyller kraven.",
     ],
     "aside": {"title": "Områdesfakta 2025", "items": [
       "1 991 småhus i stadsdelsområdet", "536 i Sätra", "320 i Bredäng"]}},
    {"id": "husgruppen", "h2": "Även ett gårdshus ska följa husgruppen",
     "paras": [
       "Vägledningen skriver att tillbyggnadsmöjligheterna i grupphusområdena ofta är mycket begränsade, men att en "
       "bod i vissa fall kan rymmas. Den ber fastighetsägaren utgå från husets volym, proportioner och takform och "
       "betonar att det gäller även om du bygger ett skärmtak, ett inglasat uterum eller en bod. Det vanligaste är "
       "att placera sådant mot trädgårdssidan och undvika förändringar mot gatan.",
       "Ett komplementbostadshus vid ett radhus med platt tak blir därför ofta en enkel låg volym med platt eller "
       "svagt lutande tak, i material och kulörer som går igen i husgruppen. Bredäng står i vägledningens tabell som "
       "kulturhistoriskt värdefull miljö, och där krävs bygglov även för ett hus som annars är lovfritt.",
     ],
     "aside": None},
    {"id": "grans-medgivande", "h2": "4,5 meter och grannarnas medgivande",
     "paras": [
       "Stockholms stad skriver att ett lovfritt komplementbostadshus ska stå 4,5 meter från gränsen mot granne, "
       "samfällighet eller allmän plats. På en smal radhustomt är det sällan möjligt, och då behövs skriftliga "
       "medgivanden. Medgivandet ska innehålla fastighetsbeteckning, vilken åtgärd det gäller, en situationsplan med "
       "avståndet till gränsen och underskrifter från berörda grannar. Får du inte medgivandena krävs bygglov.",
       "Två andra regler hjälper på en liten tomt. Huset får strida mot detaljplanen, till exempel stå på prickmark "
       "som annars inte får bebyggas. Men det ska ha en mindre byggnadsarea än radhuset det kompletterar, och "
       "alla lovfria komplementbyggnader på tomten får tillsammans vara högst 45,0 kvadratmeter.",
     ],
     "aside": {"title": "Utan lov – om inget annat gäller", "items": [
       "Högst 30,0 m² byggnadsarea", "Mindre än radhuset", "4,5 m till gräns eller medgivande", "Pott 45,0 m²"]}},
    {"id": "va-skarholmen", "h2": "Vatten och avlopp till gårdshuset",
     "paras": [
       "Stockholm Vatten och Avfall vill ha en servisanmälan i god tid före byggstart när en komplementbyggnad byggs "
       "om eller får ny användning, och en ritning över ledningsdragningen måste bifogas. Den nya vattenledningen "
       "ska kopplas efter vattenmätaren i huset, och spillvattnet till den befintliga spillvattenledningen på tomten, "
       "gärna via en rensbrunn. Dag- och dräneringsvatten får inte kopplas till spillvattnet.",
       "Har gårdshuset både kök eller pentry och toalett räknas det som en egen bostad i VA-taxan, och då tillkommer "
       "en bostadsenhetsavgift som ska vara betald innan inkoppling. Installationerna kräver också anmälan och "
       "startbesked. Om du hellre vill bygga ihop med huset beskriver vi det under " +
       _L.format("tillbyggnad-skarholmen.html", "tillbyggnad i Skärholmen") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Skärholmen",
  "steps": [
    ("Platsbesök", "Vi mäter tomten, radhuset och avstånden till gränserna."),
    ("Kartan", "Stadsmuseets karta och detaljplanen kontrolleras."),
    ("Medgivanden", "Skriftliga medgivanden från grannarna, eller bygglov."),
    ("Servisanmälan", "Ritning över ledningarna till Stockholm Vatten och Avfall."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset tas i bruk när slutbeskedet har kommit."),
  ],
  "rot_h2": "Inget rotavdrag för ett nytt gårdshus",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Skärholmen?",
  "price": [
    "Husets storlek och planlösning, om bygglov behövs, kök och badrum, grundläggning, ledningsdragning och hur "
    "material kan bäras in på en tomt som ofta saknar bilväg fram till huset. Efter ett gratis platsbesök får du ett skriftligt "
    "kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi bygga ett attefallshus vid vårt radhus i Sätra?",
     "Ofta, om måtten ryms och grannarna ger skriftliga medgivanden när huset hamnar närmare gränsen än 4,5 meter. "
     "Huset ska ha en mindre byggnadsarea än radhuset."),
    ("Får gårdshuset stå på prickmark i Skärholmen?",
     "Ja, om det är lovfritt. Stockholms stad skriver att ett komplementbostadshus som inte kräver lov får strida "
     "mot detaljplanen, till exempel stå på prickmark."),
    ("Hur stort får gårdshuset vara vid ett radhus i Skärholmen?",
     "Högst 30,0 kvadratmeter byggnadsarea och mindre än radhuset det kompletterar, om inget lov krävs. Alla "
     "lovfria komplementbyggnader på tomten får tillsammans vara högst 45,0 kvadratmeter."),
    ("Vad ska grannens medgivande innehålla?",
     "Fastighetsbeteckning, vilken åtgärd det gäller, en situationsplan med avståndet till gränsen och "
     "underskrifter från berörda grannar."),
    ("Behöver vi bygglov för ett gårdshus i Bredäng?",
     "Bredäng står som kulturhistoriskt värdefull miljö i stadens vägledning. Visar Stadsmuseets karta att "
     "fastigheten berörs krävs bygglov."),
    ("Får dagvattnet från gårdshusets tak ledas till avloppet i Skärholmen?",
     "Nej. Stockholm Vatten och Avfall skriver att dag- och dräneringsvatten inte får kopplas till "
     "spillvattenledningen."),
    ("Vad kostar det extra i VA om gårdshuset får kök och toalett?",
     "Då räknas huset som en egen bostad i VA-taxan och en bostadsenhetsavgift tillkommer enligt Stockholm Vatten "
     "och Avfall. Den ska vara betald innan inkoppling."),
  ],
  "sources": [_VARSAM, _of("Skärholmens stadsdelsområde", "soderort/skarholmen/skarholmen-stadsdelsomrade"),
              _of("Sätra", "soderort/skarholmen/satra"), _of("Bredäng", "soderort/skarholmen/bredang"), _STH_KBH, _SVOA, _SKV],
  "cta": ("Vill du bygga ett gårdshus i Skärholmen?",
          "Boka ett gratis platsbesök, så går vi igenom tomten, grannarna och ledningarna innan du får ett skriftligt "
          "kostnadsförslag."),
  "img": [
    ("Litet gårdshus med platt tak längst bak på en radhustomt",
     "small new Swedish garden house with a flat roof and dark wooden cladding at the back of a narrow garden "
     "behind a 1960s flat-roofed row house with brick and wood facade, low fence to neighbours, summer daylight"
     + _SFX),
    ("Radhus med pulpettak i en enhetlig husgrupp",
     "group of identical 1960s Swedish one-storey row houses with flat roofs and a broad dark fascia, facades of "
     "white lime brick and dark painted wood, small front gardens with low fences along a car-free footpath, soft daylight" + _SFX),
    ("Måttband och käppar som markerar ett hörn på en liten tomt",
     "wooden stakes with string marking the corner of a planned small building on a lawn next to a low fence in a "
     "narrow row house garden, a folding ruler lying in the grass, overcast daylight" + _SFX),
  ],
},
}
