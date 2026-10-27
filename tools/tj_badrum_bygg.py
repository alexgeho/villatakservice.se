# -*- coding: utf-8 -*-
"""Tjänster v1 – ortsidor: badrumsrenovering i Bromma, Täby, Järfälla och byggföretag i Täby,
Lidingö (2026-10-25). Schema: se tools/tj_check.py. Lokala fakta om bebyggelsen är omformulerade
från tools/takreno_orter.py (TRP, med källor) och kontrollerade mot kommunernas sidor; regler från
Boverket, riksdagen.se (bostadsrättslagen), Skatteverket och branschorganen GVK, BKR och Säker Vatten."""

L = '<a class="text-link" href="{0}">{1}</a>'
X = '<a class="text-link" href="{0}" rel="noopener">{1}</a>'

# Gemensamma källor
S_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
         "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
S_GVK = ("GVK – Säkra Våtrum, kvalitetsdokument och kontroll av badrum", "https://www.gvk.se/")
S_BKR = ("Byggkeramikrådet – branschregler för våtrum (BBV)", "https://www.bkr.se/")
S_SV = ("Säker Vatten – Branschregler Säker Vatteninstallation", "https://www.sakervatten.se/")
S_ROT = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
S_ROTJOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
S_PBL = ("Boverket – Lista med PBL-ändringar som trädde i kraft 1 december 2025",
         "https://www.boverket.se/sv/samhallsplanering/uppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/")
S_FAS = ("Boverket – Fasadändring, PBL kunskapsbanken",
         "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")

PAGES_TJ = {

# =============================== BADRUM BROMMA ===============================
"badrumsrenovering-bromma.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Bromma", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Bromma – trävillor, småstugor och funkis",
  "description": "Badrumsrenovering i Bromma: träbjälklag i trädgårdsstädernas villor, små badrum i småstugorna, "
                 "lov i riksintressena och styrelsens tillstånd i bostadsrätt.",
  "h1": "Badrumsrenovering i Bromma",
  "lead": "En badrumsrenovering i Bromma börjar med frågan vilket hus badrummet sitter i – en trävilla från "
          "trädgårdsstäderna, en småstuga i Ängby eller Olovslund eller en funkisvilla. Vi river ner till "
          "underlaget, bygger upp golv och väggar för ett tätskikt enligt branschreglerna och låter behöriga "
          "installatörer sköta VVS och el. ROT-avdraget drar vi direkt på fakturan.",
  "card": "Trävillor, småstugor och funkisvillor.",
  "sections": [
    {"id": "husen", "anchor": "Husen i Bromma",
     "h2": "Brommas villor gömmer tre olika sorters badrum",
     "paras": [
       "I Alvik och Äppelviken, som staden köpte 1908, började villorna byggas på 1910-talet. På "
       "1920-talet växte trädgårdsstäderna fram i Ålsten, Smedslätten, Nockeby, Höglandet och Ulvsunda, med "
       "trähus i ett och ett halvt plan under branta sadeltak. Badrummet i ett sådant hus har ofta flyttats "
       "eller byggts om under årens lopp och kan i dag ligga i källaren, i ett hörn av "
       "bottenvåningen eller under snedtaket på övervåningen. Var det ligger avgör hur golvet är byggt och "
       "hur avloppet går.",
       "Småstugorna är en egen kategori. I Olovslund byggde familjerna själva sina hus, de flesta 1927–28, och "
       "i Norra Ängby uppfördes 1 200 småstugor 1931–38 av element som tillverkades i fabrik. Husen är "
       "små och planlösningen tät, och många har byggts till genom åren. Ett nytt eller större badrum hamnar "
       "därför ofta i skarven mellan den gamla stommen och en tillbyggnad.",
       "Funkisvillorna i Södra Ängby, drygt 500 hus från 1934–39, och de 94 radhusen längs Ålstensgatan, som "
       "började byggas 1932, är ritade med genomtänkta och snåla planer. Där är det sällan läge att flytta badrummet; "
       "bättre att arbeta inom det befintliga rummet och lägga krutet på tätskikt, ventilation och nya ytskikt.",
     ],
     "aside": {"title": "Bra att veta före besöket", "items": [
       "Ligger badrummet på övervåningen, i källaren eller i en tillbyggnad?",
       "Finns det en golvbrunn i dag, och hur gammal är den?",
       "Ska rummet flyttas eller bli större?",
       "Ligger huset i Ängby, Olovslund eller längs Ålstensgatan?"]}},
    {"id": "bjalklag",
     "h2": "Träbjälklag, snedtak och gamla stammar",
     "paras": [
       "I trädgårdsstädernas trähus vilar badrumsgolvet på ett bjälklag av trä. Trä rör sig med fukt och "
       "belastning, och ett golv med klinker och ett tätskikt tål inte att svikta. Därför river vi ner till "
       "bjälkarna, kontrollerar dem och förstärker eller kompletterar där det behövs innan nytt golv byggs "
       "upp. Samtidigt byggs fallet mot golvbrunnen in i golvet, och det är lättare att få till rätt när "
       "underlaget är öppet.",
       "Under snedtak blir rummet lågt längs ena väggen. Det påverkar var duschen kan stå och hur frånluften "
       "dras, och i en uppvärmd övervåning måste ventilationen fungera för att fukten inte ska gå vidare upp i "
       "takkonstruktionen. I källarbadrum är frågan i stället hur avloppet ligger i förhållande till "
       "husets servis och om golvet ligger mot mark.",
       "Avloppsrör i äldre hus kan ha bytts helt, delvis eller inte alls. Vi går igenom vad som syns när "
       "golvet är rivet och föreslår åtgärder utifrån det, i stället för att gissa i förväg. Hur tätskikt, "
       "fall och brunn ska utföras beskrivs mer generellt under " + L.format("badrumsrenovering.html", "badrumsrenovering i Stockholm") + ".",
     ],
     "aside": None},
    {"id": "riksintresse",
     "h2": "Inget bygglov för badrummet – men titta på fasaden",
     "paras": [
       "Stockholms stad skriver att det inte behövs bygglov för att flytta ett badrum. Däremot krävs anmälan "
       "och startbesked om arbetet ändrar bärande konstruktion eller brandskydd, om ventilationen installeras "
       "eller ändras väsentligt eller om det dras en ny VA-stam i ett nytt schakt. Det är vanligast när "
       "badrummet flyttas mellan våningar eller när ett nytt badrum byggs i en tillbyggnad.",
       "Det som syns utifrån är en annan fråga. Norra och Södra Ängby, Ålstensgatan och Olovslund är riksintressen "
       "för kulturmiljövården, och enligt staden kan lov krävas där även för åtgärder som annars är lovfria. En "
       "ny fläkthuv på taket, ett galler i fasaden eller ett nytt badrumsfönster kan alltså behöva prövas. "
       "Utanför riksintressena ger " + X.format("https://stadsmuseet.stockholm/kunskap-och-samlingar/kulturmiljo/klassificering/", "Stadsmuseets kulturhistoriska klassificering") +
       " en första bild av hur värdefullt huset bedöms vara.",
       "Ska frånluften gå genom taket samordnar vi genomföringen med tätningen av taket. Mer om takets "
       "detaljer finns hos " + L.format("taklaggare-bromma.html", "takläggare i Bromma") + ".",
     ],
     "aside": {"title": "Kan kräva anmälan eller lov", "items": [
       "Ny VA-stam i nytt schakt",
       "Väsentligt ändrad ventilation",
       "Ingrepp i bärande bjälklag eller vägg",
       "Nytt fönster eller galler i riksintresseområde"]}},
    {"id": "boendeform",
     "h2": "Villa i Nockeby eller bostadsrätt i Alvik",
     "paras": [
       "Bor du i en bostadsrätt, till exempel i Alvik, Traneberg eller Abrahamsberg, gäller "
       "bostadsrättslagen. Enligt 7 kap. 7 § får du inte utan styrelsens tillstånd göra ingrepp i bärande "
       "konstruktion, installera eller ändra ledningar för avlopp, värme, gas eller vatten eller ändra "
       "ventilationen – precis det en badrumsrenovering brukar innehålla. Styrelsen får säga nej bara om "
       "åtgärden är till påtaglig skada eller olägenhet för föreningen, och den som är missnöjd kan begära "
       "att hyresnämnden prövar frågan.",
       "I en villa eller ett eget radhus fattar du besluten själv, men du bär också hela ansvaret för att "
       "våtrummet blir tätt. Be om att få tätskiktets egenkontroll och monteringsanvisning när arbetet är klart "
       "och spara dem med husets handlingar. Ska badrummet ingå i en större ombyggnad av huset finns mer under "
       + L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en badrumsrenovering i Bromma till",
  "steps": [
    ("Besök i huset", "Vi tittar på badrummet, bjälklaget där det går att se och var avlopp och frånluft går."),
    ("Kartan och reglerna", "Vi kontrollerar om huset ligger i ett riksintresse och om något ska ändras i fasad eller tak."),
    ("Skriftligt kostnadsförslag", "Du får ett förslag där rivning, underlag, tätskikt, VVS, el och ytskikt står var för sig."),
    ("Rivning till bjälkarna", "Gamla ytskikt och golv tas bort, och vi bedömer stommen och rören innan något byggs upp igen."),
    ("Underlag, rör och el", "Bjälklag förstärks vid behov, golvet byggs med fall och installatörerna drar rör och el."),
    ("Tätskikt och slutdokument", "Tätskikt, kakel och porslin monteras, och du får egenkontroll och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Bromma",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år, och tillsammans med "
    "rutavdrag högst 75 000 kronor. Skatteverket räknar bland annat rivning av väggar, plattsättning, att dra "
    "vatten och avlopp och att montera toalett, dusch och handfat som rotarbete i ett småhus. Material och resor "
    "ger inget avdrag. Vi drar avdraget direkt på fakturan.",
    "I bostadsrätt gäller avdraget bara arbete inne i lägenheten. Stambyte, att flytta golvbrunnen eller att "
    "byta avloppsrör räknas där inte som rotarbete enligt Skatteverket.",
  ],
  "price_h2": "Vad styr priset på ett badrum i Bromma?",
  "price": [
    "Det som oftast avgör är vad som finns under det gamla golvet: hur mycket bjälklaget behöver förstärkas, "
    "om golvbrunn och avlopp kan ligga kvar och om rummet ska flyttas eller göras större. Därefter spelar "
    "storlek, val av kakel och klinker, golvvärme och nya fönster eller genomföringar in. Platsbesöket är "
    "gratis och du får ett skriftligt kostnadsförslag innan något beställs.",
  ],
  "faq": [
    ("Klarar träbjälklaget i en 1920-talsvilla i Bromma ett klinkergolv?",
     "Ofta, men inte utan kontroll. Golvet rivs ner till bjälkarna, och där de sviktar eller har fuktskador förstärks "
     "eller byts de innan golvet byggs upp med fall mot brunnen."),
    ("Kan badrummet i en småstuga i Norra Ängby göras större?",
     "Ibland, genom att ta yta från ett angränsande rum eller en tillbyggnad. Rör det bärande delar eller nya stammar "
     "krävs anmälan och startbesked, och ändras fasaden i riksintresset kan lov behövas."),
    ("Behövs lov för en ny fläkthuv på taket i Södra Ängby?",
     "Räkna med att fråga stadsbyggnadskontoret. Södra Ängby är riksintresse för kulturmiljövården och har en detaljplan "
     "med skyddsbestämmelser, så synliga ändringar på tak och fasad kan kräva lov."),
    ("Vad ska vi spara för papper efter badrummet i vår Brommavilla?",
     "Egenkontrollen för tätskiktet, monteringsanvisningen för tätskiktssystemet, skötselråd för ytskikten och "
     "eventuellt startbesked och slutbesked från staden."),
    ("Måste vi ha styrelsens ja för badrummet i en bostadsrätt i Traneberg?",
     "Ja, om arbetet ändrar avlopp, vatten, ventilation eller bärande delar, enligt bostadsrättslagen 7 kap. 7 §. "
     "Ta med en beskrivning av arbetet när du söker tillstånd."),
  ],
  "sources": [
    ("Stockholms stad – Flytta kök eller badrum", "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/flytta-kok-eller-badrum/"),
    ("Stockholms stad – Installation eller ändring av vatten och avlopp", "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/installation-eller-andring-av-vatten-och-avlopp-va/"),
    ("Stockholms stad – Översiktsplan, Riksintressen enligt miljöbalken", "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf"),
    ("Stockholms stad – Varsam utveckling av småhus- och villaområden", "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf"),
    ("Stockholmskällan / Stadsmuseet – Ängbyplan", "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000106.pdf"),
    ("Stockholmskällan / Stadsmuseet – Alvik (ytterstadsprojektet)", "https://stockholmskallan.stockholm.se/postfiles/SMF/ytterstadsprojektet/Alvik.pdf"),
    ("Stadsmuseet – Kulturhistorisk klassificering", "https://stadsmuseet.stockholm/kunskap-och-samlingar/kulturmiljo/klassificering/"),
    ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov)", "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/"),
    S_BRL, S_GVK, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i Bromma göras om?", "Boka ett gratis besök, så går vi igenom huset och badrummet på plats."),
  "img": [
    ("Renoverat badrum under snedtak i en äldre trävilla i Bromma",
     "renovated bathroom under a sloping attic ceiling in a 1920s Swedish wooden villa, white tiles, light grey floor tiles, "
     "small roof window, walk-in shower with glass screen, Bromma garden city"),
    ("Ljust badrum med vägghängd toalett och spotlights i taket",
     "bathroom under renovation in an old Swedish wooden house, floor opened to wooden joists, new plastic drain pipes, "
     "stacked wet-room boards, natural light"),
  ],
},

# =============================== BADRUM TÄBY ===============================
"badrumsrenovering-taby.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Täby", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Täby – radhuslängor, villor och gästhus",
  "description": "Badrumsrenovering i Täby: våtrum i grupphus och radhus från 60- och 70-talen, äldre villor "
                 "vid Roslagsbanan och badrum i tillbyggnad eller gästhus.",
  "h1": "Badrumsrenovering i Täby",
  "lead": "En badrumsrenovering i Täby handlar oftast om ett våtrum i ett radhus eller grupphus från efterkrigstiden, "
          "eller om ett badrum som ska in i en äldre villa längs Roslagsbanan. Vi river, bygger upp underlaget, "
          "lägger tätskikt och ytskikt och samordnar VVS och el med behöriga installatörer – en kontakt för hela jobbet.",
  "card": "Radhuslängor, villor och nya gästhus.",
  "sections": [
    {"id": "epoker", "anchor": "Husen i Täby",
     "h2": "Från stationsvilla till grupphus – vad det betyder för våtrummet",
     "paras": [
       "Täbys villor kom i vågor längs Roslagsbanan. I Roslags-Näsby byggdes ett åttiotal villor mellan 1907 och "
       "1920, i Viggbyholm började tomter styckas av när hållplatsen öppnade 1903 och i Täby villastad vid kyrkbyn "
       "stod omkring 250 villor klara fram till första världskriget. I de husen var badrummet inte en del av ursprungsplanen. "
       "Det har byggts in senare, ibland flera gånger, och varje omgång kan ha lämnat ett nytt lager golv eller "
       "en ny rördragning efter sig.",
       "Efter kriget kom grupphusen. Norskogen i Näsbypark byggdes 1957–59, och i Täby kyrkby uppfördes "
       "radhusområdena Midgård 1972–73 och Miklagård 1975–76. Gribbylund, där marken först styckades till sommarstugetomter, "
       "består i dag mest av typhus från 1970- och 1980-talen. Här är huset byggt med badrum från början, och "
       "ett våtrum som inte gjorts om kan vara lika gammalt som huset. Då är det tätskiktet, inte kaklet, "
       "som avgör om det är dags.",
     ],
     "aside": {"title": "Täbys hus i korthet", "items": [
       "Roslags-Näsby och Viggbyholm: villor från 1900-talets början",
       "Näsbypark: villor från 1920-talet och framåt",
       "Norskogen: grupphus 1957–59",
       "Midgård och Miklagård: radhus 1972–76",
       "Gribbylund: typhus från 70- och 80-talen"]}},
    {"id": "langan",
     "h2": "Badrum vägg i vägg med grannen",
     "paras": [
       "I en radhuslänga kan ditt badrum ligga vägg i vägg med grannens, med bara den skiljande väggen emellan. "
       "Det ställer två krav. Tätskiktet på den väggen måste vara helt, eftersom en läcka där kan bli grannens "
       "problem. Och rivning, bilning och kapning hörs genom hela längan, så det är klokt att prata med "
       "grannarna i förväg om när de bullriga dagarna kommer.",
       "Samma planlösning i hela längan har en fördel: vet vi var avlopp och frånluft går i ett hus är det ofta "
       "likadant i nästa. Ett nytt duschhörn eller en flyttad toalett ska ändå anslutas till de ledningar som "
       "finns, och ligger huset i en samfällighet eller en förening behöver du ta reda på vem som äger vilka "
       "delar innan något ändras.",
       "Är radhuset en bostadsrätt gäller bostadsrättslagen. Styrelsen ska ge tillstånd innan ledningar för "
       "vatten och avlopp eller ventilationen ändras, och innan någon gör ingrepp i bärande konstruktion.",
     ],
     "aside": {"title": "Före start i längan", "items": [
       "Vem äger ledningarna – du, samfälligheten eller föreningen?",
       "Behövs styrelsens tillstånd?",
       "Vilka dagar blir det bullrigt?",
       "Var går frånluften ut?"]}},
    {"id": "villa",
     "h2": "När den äldre villan ska ha ett riktigt badrum",
     "paras": [
       "I en villa från Täbys första villaepok sitter badrummet ofta på en plats som inte var tänkt för vatten. "
       "Vi river ner till stommen för att se bjälklag, väggar och rör, och bygger sedan upp ett underlag som "
       "tål tätskikt och klinker. Golvet får fall mot en golvbrunn, och väggarna kläs med skivor som är gjorda "
       "för våtrum.",
       "Branschorganisationen GVK uppdaterade sina regler för tätskikt, Säkra Våtrum, den 1 januari 2026, och "
       "Byggkeramikrådet har motsvarande regler för plattsatta våtrum. Fråga vilka regler arbetet utförs efter och "
       "be att få egenkontrollen för tätskiktet när det är klart. Vad du i övrigt bör få på papper står på "
       + L.format("badrumsrenovering.html", "sidan om badrumsrenovering") + ".",
     ],
     "aside": None},
    {"id": "nytt",
     "h2": "Ett extra badrum i tillbyggnad eller gästhus",
     "paras": [
       "Många i Täby vill ha ett andra badrum, och det kan hamna i en tillbyggnad eller i ett komplementbostadshus "
       "på tomten. Sedan den 1 december 2025 är ett sådant hus bygglovsbefriat om det är högst 30 kvadratmeter och "
       "4 meter högt inom detaljplan, och alla lovfria komplementbyggnader på tomten får tillsammans vara högst "
       "45 kvadratmeter. Täby kommun påpekar att en anmälan och ett startbesked kan krävas när vatten och avlopp "
       "installeras i byggnaden, och Boverket beskriver samma sak: själva huset kräver ingen anmälan, men "
       "installationerna gör det.",
       "Ligger fastigheten i ett kulturhistoriskt särskilt värdefullt område krävs bygglov även för det som "
       "annars är lovfritt. Mer om reglerna finns under " + L.format("attefallshus.html", "attefallshus") +
       " och " + L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi ett badrum i Täby",
  "steps": [
    ("Genomgång på plats", "Vi ser badrummet, var rören och frånluften går och vad grannväggen är byggd av."),
    ("Ägarfrågan", "I bostadsrätt eller samfällighet tar vi reda på vad som behöver godkännas innan start."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med arbete och material på egna rader, så ROT-avdraget syns."),
    ("Rivning och kontroll", "Rummet rivs ner till stommen, och rör, golvbrunn och bjälklag bedöms med golvet öppet."),
    ("Uppbyggnad och tätskikt", "Golv med fall, våtrumsskivor och tätskikt monteras; installatörerna drar rör och el."),
    ("Ytskikt och överlämning", "Kakel, klinker och porslin på plats, och du får dokumentationen över tätskiktet."),
  ],
  "rot_h2": "ROT-avdraget när du renoverar badrummet i Täby",
  "rot": [
    "Du kan få rotavdrag med 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst "
    "75 000 kronor tillsammans med rutavdrag. Avdraget gäller arbetet, inte materialet, och vi drar det direkt på "
    "fakturan. Äger ni huset tillsammans har var och en sitt eget utrymme.",
    "Ett badrum i ett nytt fristående gästhus ger enligt Skatteverket inget rotavdrag, eftersom avdraget inte gäller "
    "nybyggnad av en fristående byggnad. Ett badrum i en tillbyggnad som sitter ihop med huset kan däremot "
    "omfattas, om huset är äldre än fem år.",
  ],
  "price_h2": "Vad styr priset på badrummet i Täby?",
  "price": [
    "Storleken på rummet spelar mindre roll än man tror. Det som brukar avgöra är om toalett, dusch och golvbrunn "
    "ligger kvar eller flyttas, hur mycket av underlaget som behöver byggas om och vilka ytskikt du väljer. I ett "
    "nytt gästhus tillkommer dragning av vatten och avlopp från huvudbyggnaden. Besöket är gratis och du får ett "
    "skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan jag flytta duschen i ett radhus i Miklagård utan att störa grannen?",
     "Oftast går det att flytta duschen inom rummet, men ledningar och väggar delas med längan. Vi kontrollerar var "
     "avloppet går och hur grannväggen är byggd innan vi föreslår en ny placering."),
    ("Behöver jag anmäla ett nytt badrum i ett gästhus i Täby?",
     "Räkna med det. Huset kan vara lovfritt, men Täby kommun anger att anmälan och startbesked kan krävas när vatten "
     "och avlopp installeras i byggnaden."),
    ("Är det värt att renovera badrummet i ett hus från 70-talet om det ser helt ut?",
     "Det beror på tätskiktets ålder och skick, inte på hur kaklet ser ut. Ett badrum som är original från "
     "husets byggår bör undersökas, särskilt runt golvbrunnen och duschen."),
    ("Vem äger avloppet i ett grupphus i Norskogen?",
     "Det beror på hur området förvaltas. I en samfällighet eller förening kan delar av ledningarna vara gemensamma, "
     "så kontrollera det innan avloppet ändras."),
    ("Kan en villa i Roslags-Näsby få golvvärme i badrummet?",
     "Ja, i de flesta fall. Elektrisk golvvärme läggs i samband med att golvet byggs upp och kopplas in av en behörig "
     "elinstallatör."),
  ],
  "sources": [
    ("Täby kommun – Kulturmiljöer i Täby, riktlinjer (pdf)", "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"),
    ("Täby kommun – Bygga, riva och förändra", "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra"),
    ("Täby kommun – Kulturmiljöer i Täby", "https://taby.se/huvudsajter/kulturmiljoer"),
    S_PBL, S_BRL, S_GVK, S_BKR, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i Täby renoveras?", "Boka ett gratis platsbesök, så går vi igenom rummet och ledningarna."),
  "img": [
    ("Nyrenoverat badrum i ett radhus från 1970-talet i Täby",
     "newly renovated bathroom in a Swedish 1970s terraced house, large light grey wall tiles, dark floor tiles, "
     "wall-hung toilet, walk-in shower, small window with daylight, Täby"),
    ("Grupphusområde med radhuslängor i Täby",
     "row of Swedish 1970s terraced houses with red concrete roof tiles and small dormers, wooden facades, "
     "green lawns and birch trees, Täby suburb, summer"),
  ],
},

# =============================== BADRUM JÄRFÄLLA ===============================
"badrumsrenovering-jarfalla.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Järfälla", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Järfälla – radhus och souterränghus",
  "description": "Badrumsrenovering i Järfälla: våtrum i radhus och kedjehus i Kallhäll, Jakobsberg och Viksjö, "
                 "VA-anmälan, ansvar för ledningar och styrelsens tillstånd.",
  "h1": "Badrumsrenovering i Järfälla",
  "lead": "Badrumsrenovering i Järfälla gäller ofta radhus och kedjehus som byggfirmorna uppförde i serier från "
          "1945 och in på 1960-talet. Vi river, kontrollerar avlopp och underlag, bygger upp tätskikt och "
          "ytskikt och låter behöriga installatörer göra VVS och el – med ROT-avdraget direkt på fakturan.",
  "card": "Radhus, kedjehus och souterränghus.",
  "sections": [
    {"id": "serier", "anchor": "Husen i Järfälla",
     "h2": "Hus byggda i serier – och badrum därefter",
     "paras": [
       "Järfällas kulturmiljöplan beskriver många småhusområden som byggdes i ett svep av en och samma firma. I "
       "Kallhäll lät Bolinders uppföra radhus åt sina anställda längs Bolindervägen från 1945. I Jakobsberg "
       "började Widmark & Platzer bygga Ekedalsområdet 1958, och samma firma står bakom kedjehusen vid "
       "Dressyrvägen och villorna vid Stålringen. Grändvillorna vid Hovvägen, "
       "byggda i souterräng, kom omkring 1960.",
       "För badrummet betyder det att husen i ett område ofta är byggda med samma planlösning och samma "
       "material. Ett badrum från 1960- eller 70-talet som inte byggts om har i regel både tätskikt, "
       "golvbrunn och rör från samma tid. Har det renoverats en gång kan det ändå finnas gamla delar kvar under "
       "det nya, till exempel en äldre brunn under ny klinker.",
       "Det finns också undantag. Lund vid Mälaren är kommunens äldsta fritidshusområde, med enkla trähus från "
       "1900-talets början. Där kan ett badrum behöva byggas upp från grunden i ett hus som inte var tänkt för "
       "åretruntboende.",
     ],
     "aside": {"title": "Ur kulturmiljöplanen", "items": [
       "Bolinderbyn, Kallhäll: radhus från 1945",
       "Ekedal, Jakobsberg: från 1958",
       "Dressyrvägen och Stålringen: 1960-tal",
       "Hovvägen: grändvillor kring 1960",
       "Lund vid Mälaren: fritidshus från tidigt 1900-tal"]}},
    {"id": "suterrang",
     "h2": "Souterränghus och badrum mot mark",
     "paras": [
       "I Ekedal finns souterrängradhus, där nedre planet ligger delvis i backen. Ett badrum i det planet har ofta "
       "golv direkt på betong mot mark och en eller flera väggar mot jord. Där räcker det inte att bara tänka på "
       "vattnet från duschen; fukt kan också komma från marken. Innan nytt tätskikt läggs undersöker vi därför "
       "underlaget och om det finns tecken på markfukt.",
       "Ligger badrummet på övervåningen i ett tvåplans radhus är frågan i stället bjälklaget och hur frånluften "
       "går ut. I kedjehusen kan garaget mellan husen ge möjlighet till en ny dragning, men det avgörs av hur "
       "huset faktiskt är byggt.",
       "Terrängen spelar in även på andra håll. I Bolinderbyn i Kallhäll står radhusen i 21 längor, och i Ekedal "
       "ligger radhuslängorna i den lägre delen och villorna högre upp i backen. Hur huset ligger i slänten avgör "
       "var badrummet kan placeras och hur avloppet når ut. Ska badrummet flyttas upp eller ner en våning påverkar "
       "det både fallet på avloppet och var frånluften kan dras, och det är ofta där en ytskiktsrenovering blir "
       "ett större projekt som kan behöva anmälas.",
     ],
     "aside": None},
    {"id": "ledningar",
     "h2": "Var dina ledningar börjar – och när kommunen vill veta",
     "paras": [
       "I en villa eller ett eget radhus i Järfälla äger du ledningarna från förbindelsepunkten, som enligt kommunen "
       "normalt ligger vid eller strax utanför tomtgränsen. Det betyder att reparationer vid läckor, åtgärder vid "
       "avloppsstopp och underhåll av ledningar och ventiler inne på tomten är ditt ansvar. När badrummet ändå är "
       "rivet är det ett bra tillfälle att se över avloppet ut mot gatan.",
       "Järfälla kommun kräver anmälan om du installerar eller väsentligt ändrar vatten och avlopp, till exempel "
       "när stammar dras i nya lägen. Du måste vänta på startbesked innan arbetet börjar, och en kontrollplan ska "
       "lämnas in. Kommunen räknar med beslut inom fyra veckor efter att alla handlingar kommit in. Är du osäker på om "
       "ändringen är tillräckligt stor vill kommunen att du hör av dig innan arbetet börjar.",
     ],
     "aside": {"title": "Kan behöva anmälas", "items": [
       "Stammar i nya lägen",
       "Nytt badrum med egen VA-anslutning",
       "Ingrepp i bärande vägg",
       "Väsentligt ändrad ventilation"]}},
    {"id": "forening",
     "h2": "Bostadsrätt i Jakobsberg eller Barkarby",
     "paras": [
       "Bor du i en bostadsrätt, till exempel i ett flerbostadshus i Jakobsberg eller Barkarby, är det "
       "bostadsrättslagen som styr: utan styrelsens tillstånd får du inte ändra ledningar för vatten och avlopp, ändra ventilationen "
       "eller göra ingrepp i bärande konstruktion. Ta reda på föreningens regler för våtrum innan du begär "
       "kostnadsförslag, och om stammarna nyligen bytts eller ska bytas.",
       "Tätskiktet ska utföras enligt branschregler, som GVK:s Säkra Våtrum eller Byggkeramikrådets regler, och "
       "VVS-arbetet enligt Säker Vattens branschregler. Det är dokumentationen därifrån som föreningen brukar vilja "
       "se. Mer om helheten finns under " + L.format("badrumsrenovering.html", "badrumsrenovering i Stockholm") +
       ", och om taket också behöver ses över finns " + L.format("takrenovering-jarfalla.html", "takrenovering i Järfälla") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Badrummet i Järfälla steg för steg",
  "steps": [
    ("Platsbesök", "Vi ser badrummet, golvbrunnen och var huset ansluter till kommunens ledningar."),
    ("Anmälan eller inte", "Flyttas stammar eller ändras ventilationen hjälper vi dig att ta fram underlag till kommunen."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där arbete och material står separat."),
    ("Rivning och fuktkontroll", "Rummet rivs, och i souterrängplan kontrolleras golv och väggar mot mark."),
    ("Rör, el och tätskikt", "Installatörerna drar nytt, golvet byggs med fall och tätskiktet läggs enligt branschregler."),
    ("Klart och dokumenterat", "Kakel, klinker och porslin monteras, och du får egenkontroll och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för badrum i Järfälla",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 "
    "kronor ihop med rutavdrag. I ett småhus räknar Skatteverket bland annat plattsättning, rivning av väggar och "
    "dragning av vatten- och avloppsledningar som rotarbete. Material och resor ingår inte, och vi drar "
    "avdraget direkt på fakturan.",
    "I bostadsrätt gäller avdraget bara arbete inne i lägenheten, och enligt Skatteverket inte stambyte eller "
    "flytt av golvbrunn.",
  ],
  "price_h2": "Vad påverkar priset på badrummet i Järfälla?",
  "price": [
    "Det som oftast styr är skicket på underlaget och avloppet, om något ska flyttas och om rummet ligger mot mark "
    "i ett souterrängplan. Ytskikt, golvvärme och inredning kommer sedan. Besöket är kostnadsfritt och du får ett "
    "skriftligt kostnadsförslag innan något beställs.",
  ],
  "faq": [
    ("Hur lång tid tar Järfälla kommun på sig med en VA-anmälan för badrummet?",
     "Kommunen anger att du kan räkna med beslut inom fyra veckor från att alla handlingar kommit in. Arbetet får "
     "börja först när startbeskedet finns."),
    ("Vem ansvarar för avloppet mellan mitt radhus i Viksjö och gatan?",
     "Kommunen äger ledningarna fram till förbindelsepunkten, som normalt ligger vid eller strax utanför tomtgränsen. "
     "Därifrån och in i huset är det fastighetsägaren, eller samfälligheten om ledningarna är gemensamma."),
    ("Kan vi bygga ett badrum i nedre planet i ett souterränghus i Ekedal?",
     "Ofta, men golv och väggar mot mark måste undersökas först. Avloppet måste också kunna ledas ut med tillräckligt "
     "fall."),
    ("Går det att få ett riktigt badrum i ett gammalt fritidshus i Lund?",
     "Det går, men räkna med att bygga upp golv, väggar och ventilation från grunden och att kontrollera hur huset "
     "får vatten och blir av med avloppet."),
    ("Behöver kedjehusgrannen tillfrågas när jag gör om badrummet?",
     "Inte för själva renoveringen, men det är klokt att berätta när rivningen pågår. Delar ni ledningar eller vägg "
     "behöver ni vara överens om hur anslutningen görs."),
  ],
  "sources": [
    ("Järfälla kommun – Installation eller ändring av vatten och avlopp", "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/installationellerandringavvattenochavloppva.4.69a1b161151015104f4bd741.html"),
    ("Järfälla kommun – Ansvarsgränser mellan ledningar", "https://www.jarfalla.se/byggaboochmiljo/vavattenochavlopp/ansvarsgransermellanledningar.4.503309051349ea61989800014995.html"),
    ("Järfälla kommun – Kulturmiljöplan, inledning", "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4052/1550245824984/kulturmiljoplan-inledning.pdf"),
    ("Järfälla kommun – Kulturmiljöplan, Jakobsberg", "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4080/1550245872956/kulturmiljoplan-jakobsberg.pdf"),
    ("Järfälla kommun – Kulturmiljöplan, Kallhäll", "https://www.jarfalla.se/download/18.68e7a727168e12dd179a407f/1550245859848/kulturmiljoplan-kallhall.pdf"),
    ("Järfälla kommun – Kulturmiljöplan, Stäket", "https://www.jarfalla.se/download/18.68e7a727168e12dd179a407e/1550245842779/kulturmiljoplan-staket.pdf"),
    S_BRL, S_GVK, S_BKR, S_SV, S_ROT, S_ROTJOB,
  ],
  "cta": ("Dags för nytt badrum i Järfälla?", "Boka ett gratis besök, så tittar vi på rummet och ledningarna."),
  "img": [
    ("Renoverat badrum i ett kedjehus i Järfälla",
     "renovated bathroom in a Swedish 1960s link house, white subway tiles, terrazzo-look floor tiles, wooden vanity, "
     "shower niche, warm daylight, Järfälla"),
    ("Radhus i souterräng med tegeltak i Järfälla",
     "Swedish 1960s split-level terraced houses on a slope with red clay tile roofs and light brick facades, "
     "pine trees, Jakobsberg Järfälla, autumn"),
  ],
},

# =============================== BYGGFÖRETAG TÄBY ===============================
"byggforetag-taby.html": {
  "kind": "district", "service": "byggforetag", "ort": "Täby", "svc_label": "Byggföretag",
  "title": "Byggföretag i Täby – tillbyggnad, gästhus och renovering",
  "description": "Byggföretag i Täby: tillbyggnad, gästhus och renovering av villor och grupphus som total "
                 "entreprenad, med kommunens kulturmiljöråd och nya PBL.",
  "h1": "Byggföretag i Täby",
  "lead": "Som byggföretag i Täby bygger vi till, bygger nytt på tomten och renoverar villor och radhus som total "
          "entreprenad, med en kontakt från ritning till slutbesiktning. I Täby styrs mycket av vilken epok huset "
          "tillhör och av kommunens råd för kulturmiljöer, så vi börjar med huset och reglerna innan något ritas.",
  "card": "Tillbyggnad, gästhus och renovering.",
  "sections": [
    {"id": "uppdrag", "anchor": "Vad vi bygger i Täby",
     "h2": "Det villaägare i Täby oftast vill bygga",
     "paras": [
       "De flesta byggprojekt på Täbys villatomter handlar om mer yta eller om att förnya ett hus som börjar bli "
       "gammalt. Det kan vara en " + L.format("tillbyggnad.html", "tillbyggnad") + " mot trädgården, ett gästhus "
       "eller " + L.format("attefallshus.html", "attefallshus") + " för en vuxen son eller dotter, en inredd vind "
       "eller en " + L.format("villarenovering.html", "renovering av hela villan") + " med nytt kök, badrum och "
       "ytskikt. Ofta blir det en kombination, och då är det en fördel att ett företag håller ihop helheten.",
       "Vi arbetar som total entreprenad: du har en kontakt, vi samordnar snickare, plattsättare, målare och "
       "behöriga installatörer för el och VVS, och vi ansvarar för att delarna passar ihop. Vill du veta mer om "
       "hur det fungerar, se " + L.format("byggfirma.html", "byggfirma i Stockholm") + ".",
     ],
     "aside": {"title": "Vanliga projekt", "items": [
       "Tillbyggnad på upp till 30 kvadratmeter",
       "Komplementbostadshus på tomten",
       "Renovering av hela villan eller radhuset",
       "Ombyggnad av kök och badrum"]}},
    {"id": "epoker",
     "h2": "Husets ålder avgör hur det byggs till",
     "paras": [
       "Täby har villor från alla epoker. I Roslags-Näsby och Viggbyholm står villor från 1900-talets första "
       "decennier med sadeltak eller brutna tak, i Näsbypark finns villor från 1920-talet och funkishus från "
       "1940-talet med låga takfall, och i kyrkbyn till exempel en villa från 1962 med svarta "
       "betongpannor. Radhusområdena Midgård och Miklagård byggdes 1972–76 och Norskogen 1957–59.",
       "En tillbyggnad på en trävilla från 1910-talet ställer andra krav än en på ett radhus från 1970-talet. I "
       "den äldre villan ska ny stomme anslutas till gammal, ofta med en takfot och en panel som ska se ut som "
       "originalet. I grupphuset är frågan i stället hur tillägget passar in i en hel länga som ritades som en "
       "enhet.",
     ],
     "aside": None},
    {"id": "riktlinjer",
     "h2": "Täby kommuns råd: underordnat, mot trädgården, samma tak",
     "paras": [
       "Täby kommun har antagit Kulturmiljöer i Täby, med råd och riktlinjer som enligt kommunen gäller för alla "
       "områden som underlaget tar upp. För småhusområden skriver kommunen att tillbyggnader bör vara underordnade "
       "huvudbyggnaden, att husets ursprungliga uttryck och färgsättning bör vara vägledande och att befintliga "
       "takformer, takmaterial och takfotens utformning bör behållas och väljas även för det som byggs till. Inom "
       "kulturhistoriskt värdefulla områden bör tillbyggnaden hamna mot trädgårdssidan.",
       "För grupphusområden går råden ett steg längre. Carport och altan ska anpassas till husens formspråk, utan "
       "avvikande takvinklar, för stora volymer eller kraftiga kontraster i material och färg, och ursprungliga "
       "fönsterformat bör behållas. Kommunen vill också att markarbeten som sprängning, fyllning och schaktning "
       "hålls nere och att tomterna får behålla sin naturliga topografi.",
       "Riktlinjerna är kommunens styrdokument för kulturmiljöerna. Vi läser dem för ditt "
       "område innan vi skissar, så att förslaget går att genomföra.",
     ],
     "aside": {"title": "Kontrollera tidigt", "items": [
       "Finns området med i Kulturmiljöer i Täby?",
       "Vad säger detaljplanen om byggrätt och placering?",
       "Är tomten särskilt värdefull med utökad lovplikt?",
       "Ändras marknivån mer än en halv meter?"]}},
    {"id": "lov",
     "h2": "Lovfritt sedan december 2025 – med undantag",
     "paras": [
       "Sedan den 1 december 2025 får ett en- eller tvåbostadshus byggas till med sammanlagt högst 30 "
       "kvadratmeter utan bygglov, så länge tillbyggnaden inte går över taknocken. Placeras den närmare "
       "fastighetsgränsen än 4,5 meter krävs grannens skriftliga medgivande. Ett komplementbostadshus är "
       "lovfritt upp till 30 kvadratmeter och 4 meters höjd inom detaljplan, och de lovfria komplementbyggnaderna "
       "på tomten får tillsammans vara högst 45 kvadratmeter. Friggebod och attefallshus finns inte längre som "
       "begrepp i lagen.",
       "Täby kommun påpekar att bygglov krävs även för sådant om fastigheten ligger i ett kulturhistoriskt "
       "särskilt värdefullt område. Lovfritt betyder heller inte anmälningsfritt: väsentliga ingrepp i bärande "
       "konstruktion och installation av vatten, avlopp eller ventilation kan kräva anmälan och startbesked. Ändras markens "
       "höjd mer än en halv meter inom detaljplan krävs marklov. Kommunen granskar inte lovfria åtgärder i "
       "förväg, så ansvaret för att reglerna följs ligger på dig som byggherre – och på oss som bygger.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så driver vi ett byggprojekt i Täby",
  "steps": [
    ("Besök på tomten", "Vi ser huset, tomten och terrängen och går igenom vad du vill bygga."),
    ("Regler för just din fastighet", "Detaljplan, Täbys kulturmiljöråd och lov- eller anmälningsplikt kontrolleras."),
    ("Skiss och kostnadsförslag", "Du får ett skriftligt kostnadsförslag som visar vad som ingår och vad som är ROT-arbete."),
    ("Lov, anmälan och startbesked", "Där det krävs tar vi fram underlag, och bygget startar när besked finns."),
    ("Bygget", "Grund, stomme, tak och installationer samordnas av oss, med behöriga installatörer för el och VVS."),
    ("Slutbesiktning", "Vi går igenom arbetet tillsammans med dig och lämnar över dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för byggprojekt i Täby",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 "
    "kronor ihop med rutavdrag. Det gäller reparation och underhåll samt om- och tillbyggnad, det senare bara "
    "om huset är äldre än fem år. Material, bygglovshandlingar, arkitekt och besiktningsman ger inget avdrag.",
    "En tillbyggnad ger avdrag om någon av dess sidor sitter ihop med husets yttervägg till minst 75 procent. "
    "Ett helt nytt fristående hus på tomten, som ett gästhus eller garage, ger enligt Skatteverket inget "
    "rotavdrag. Vi drar avdraget direkt på fakturan där det gäller.",
  ],
  "price_h2": "Vad styr kostnaden för att bygga i Täby?",
  "price": [
    "Storlek, grundläggning och hur mycket som ska anslutas till det befintliga huset styr mest. På kuperade "
    "tomter i Näsbypark och Viggbyholm påverkar terrängen grunden, och i ett grupphusområde kan kommunens råd "
    "styra materialval och utformning. Installationer för badrum eller kök i en tillbyggnad tillkommer. "
    "Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga ett komplementbostadshus i trädgården i Näsbypark utan bygglov?",
     "Ofta, om det ryms inom 30 kvadratmeter och 4 meter, följer detaljplanen och tomtens sammanlagda gräns på "
     "45 kvadratmeter. Ligger fastigheten i ett kulturhistoriskt särskilt värdefullt område krävs bygglov."),
    ("Varför vill Täby kommun att tillbyggnaden placeras mot trädgården?",
     "I kulturhistoriskt värdefulla områden vill kommunen att gatubilden ska påverkas så lite som möjligt. Därför "
     "rekommenderar riktlinjerna att tillbyggnader läggs mot trädgårdssidan."),
    ("Kan vi bygga en carport vid vårt radhus i Midgård?",
     "Ofta ja, men kommunens råd för grupphusområden säger att den ska anpassas till husens formspråk, utan avvikande "
     "takvinkel eller stora kontraster i material och färg. Kontrollera också detaljplanen."),
    ("Ger ett nytt gästhus på tomten i Täby rotavdrag?",
     "Nej, inte för själva bygget. Skatteverket ger inte rotavdrag för en helt ny fristående byggnad. En tillbyggnad "
     "som sitter ihop med huset kan däremot ge avdrag."),
    ("Måste vi spränga för att bygga till på en bergig tomt i Täby?",
     "Inte nödvändigtvis. Kommunen vill att markarbeten hålls nere, och ofta går det att anpassa grunden efter "
     "berget. Ändras marknivån mer än en halv meter inom detaljplan krävs marklov."),
  ],
  "sources": [
    ("Täby kommun – Bygga, riva och förändra", "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra"),
    ("Täby kommun – Råd och riktlinjer, småhusområden", "https://taby.se/huvudsajter/kulturmiljoer/rad-och-riktlinjer/smahusomraden"),
    ("Täby kommun – Råd och riktlinjer, grupphusområden", "https://taby.se/huvudsajter/kulturmiljoer/rad-och-riktlinjer/grupphusomraden"),
    ("Täby kommun – Kulturmiljöer i Täby, riktlinjer (pdf)", "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"),
    S_PBL, S_ROT, S_ROTJOB,
  ],
  "cta": ("Planerar du att bygga i Täby?", "Boka ett gratis besök, så går vi igenom tomten, huset och reglerna."),
  "img": [
    ("Villa i Täby med nybyggd tillbyggnad mot trädgården",
     "Swedish 1940s functionalist white rendered villa with a new single-storey timber extension facing the garden, "
     "matching low-pitched roof, large windows, pine trees and lawn, Täby"),
    ("Nybyggt litet gästhus på en villatomt i Täby",
     "small newly built Swedish guest house of about 30 square meters with red wooden cladding and white trim, "
     "pitched roof, in a garden next to an older villa, rocky terrain with pines"),
  ],
},

# =============================== BYGGFÖRETAG LIDINGÖ ===============================
"byggforetag-lidingo.html": {
  "kind": "district", "service": "byggforetag", "ort": "Lidingö", "svc_label": "Byggföretag",
  "title": "Byggföretag på Lidingö – villastäder, berg och kulturmiljö",
  "description": "Byggföretag på Lidingö: tillbyggnad och renovering i villastäder och radhusbyar, med "
                 "utökad lovplikt, kulturmiljöprogrammet och kuperade tomter.",
  "h1": "Byggföretag på Lidingö",
  "lead": "Som byggföretag på Lidingö bygger vi till, renoverar och bygger nytt på villatomter, med en kontakt för "
          "hela projektet. På ön avgör kulturmiljöprogrammet, stadens markering för utökad lovplikt och den "
          "kuperade terrängen ofta mer än storleken på det du vill bygga.",
  "card": "Villastäder, radhusbyar och berg.",
  "sections": [
    {"id": "on", "anchor": "Att bygga på Lidingö",
     "h2": "Villastäder från 1906 och radhusbyar från efterkrigstiden",
     "paras": [
       "Villabyggandet på Lidingö tog fart 1906, när ingenjören Hjalmar Arwin bildade AB Lidingö Villastad. Fyra år "
       "senare stod 293 villor klara, och Per Olof Hallmans stadsplan antogs 1913. Samma år som Arwin startade köpte "
       "Allan Abenius Brevik, där villastaden växte fram parallellt. Kärnan i de här områdena är hus från ungefär "
       "1905–1930, och i Brevik har villastaden sedan kompletterats med villor, framför allt på 1940–60-talen.",
       "Efterkrigstiden gav radhusbyarna. Mölna radhusby, ritad av Nils Tesch, byggdes 1960–62 med fyrtio "
       "radhuslägenheter i sju längor. I västra Käppala tillkom närmare hundra radhus och kedjehus 1979, och "
       "Gåshaga förvandlades mellan 1999 och 2009 från varv och fritidshus till ett bostadsområde. Varje område har "
       "sina egna material – rött lertegel, skiffer, kopparplåt eller betongpannor – och det är dem en tillbyggnad "
       "ska möta.",
     ],
     "aside": {"title": "Lidingös byggepoker", "items": [
       "Lidingö villastad och Brevik: från 1906",
       "Kompletteringar i Brevik: 1940–60-tal",
       "Mölna radhusby: 1960–62",
       "Käppala: radhus och kedjehus 1979",
       "Gåshaga: 1999–2009"]}},
    {"id": "lovplikt",
     "h2": "Blått på kartan betyder bygglov",
     "paras": [
       "Sedan den 1 december 2025 får ett en- eller tvåbostadshus byggas till med högst 30 kvadratmeter utan bygglov, "
       "och ett komplementbostadshus på upp till 30 kvadratmeter och 4 meter är lovfritt inom detaljplan, med en "
       "gemensam gräns på 45 kvadratmeter för tomtens lovfria komplementbyggnader. På Lidingö är undantagen ovanligt "
       "viktiga. Lidingö stad skriver att utökad lovplikt gäller för de flesta byggnadsåtgärder inom särskilt "
       "kulturhistoriskt värdefulla områden, och att de syns som ett blått lager i stadens webbkarta. Är fastigheten "
       "gulmarkerad kan det finnas värden som behöver bedömas.",
       "Stadens kulturmiljöprogram antogs av kommunfullmäktige den 16 december 2024. Det är ett kunskapsunderlag "
       "och inte juridiskt bindande, men det används vid bygglovsprövningen. För byggnadsminnen, som radhusen på "
       "Canadastigen, är det Länsstyrelsen som prövar ändringar.",
       "Lovfritt är inte detsamma som fritt fram. Även en tillbyggnad utan lov kan kräva anmälan och startbesked om "
       "den påverkar bärande konstruktion eller får vatten, avlopp eller ventilation. För åtgärder som inte kräver "
       "lov går det dessutom att söka ett frivilligt bygglov och få besked i förväg om att projektet följer reglerna.",
     ],
     "aside": {"title": "Läs kartan först", "items": [
       "Blått lager: utökad lovplikt",
       "Gul markering: värden kan behöva bedömas",
       "Skyddsbestämmelse i detaljplanen",
       "Byggnadsminne: Länsstyrelsen prövar"]}},
    {"id": "terrang",
     "h2": "Berg, branter och stödmurar",
     "paras": [
       "Lidingö är kuperat, med stora bergsryggar och tydlig skärgårdsterräng kring Gåshaga, Killinge och Käppala. "
       "Mölna radhusby ligger på en högplatå, flera villor i Brevik står i souterräng och många tomter i villastäderna "
       "har stödmurar och terrasser. För en tillbyggnad betyder det att grunden ofta är den största frågan: ska huset "
       "stå på berg, på plintar eller på en platta som kräver schaktning?",
       "Inom detaljplan krävs marklov om markens höjd ändras mer än en halv meter. Vi planerar därför grunden efter terrängen och undviker stora ingrepp där det går. "
       "Branta tomter påverkar också hur material och ställning kommer fram, något vi bedömer vid besöket.",
     ],
     "aside": None},
    {"id": "material",
     "h2": "Bygga till så att det ser ut att höra till",
     "paras": [
       "I Lidingö villastad har de äldre villorna höga tak med rött lertegel, i Brevik ligger tegel, skiffer eller "
       "plåt på sadeltaken och i Mölna radhusby är tak- och gavelsprången avtäckta med koppar. En tillbyggnad som "
       "ska bli godkänd, och som ska se ut att ha funnits där länge, behöver därför ofta samma takmaterial, samma "
       "takfot och en fasad som möter originalet.",
       "Vi tar fram förslag där tillbyggnaden underordnar sig huset och där material och detaljer går att motivera i en "
       "ansökan. Ska huset också renoveras i samma veva samordnar vi det i en och samma entreprenad, se "
       + L.format("villarenovering.html", "villarenovering") + ". Mer om ytan du kan vinna finns under "
       + L.format("tillbyggnad.html", "tillbyggnad") + " och " + L.format("attefallshus.html", "attefallshus") +
       ", och om hur total entreprenad fungerar under " + L.format("byggfirma.html", "byggfirma i Stockholm") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi på Lidingö",
  "steps": [
    ("Tomt och karta", "Vi besöker tomten och kontrollerar stadens karta, detaljplanen och kulturmiljöprogrammet."),
    ("Förslag som håller", "Skiss med material och placering som passar huset och området."),
    ("Skriftligt kostnadsförslag", "Arbete, material och vad som ger ROT-avdrag redovisas tydligt."),
    ("Lov, anmälan eller frivilligt lov", "Vi tar fram underlag och väntar in startbesked där det krävs."),
    ("Grund efter terrängen", "Grundläggning anpassas till berg och lutning, sedan stomme, tak och installationer."),
    ("Överlämning", "Gemensam slutgenomgång och dokumentation av det som byggts."),
  ],
  "rot_h2": "ROT-avdrag när du bygger på Lidingö",
  "rot": [
    "Du kan få rotavdrag med 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 "
    "kronor tillsammans med rutavdrag. Avdraget gäller reparation och underhåll samt om- och tillbyggnad, det "
    "senare bara på ett hus som är äldre än fem år. Material, arkitekt, bygglovshandlingar och besiktningsman ingår inte.",
    "En tillbyggnad räknas om någon sida sitter ihop med husets yttervägg till minst 75 procent, medan ett nytt "
    "fristående hus på tomten inte ger avdrag. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för att bygga på Lidingö?",
  "price": [
    "Grunden på kuperade tomter, krav på material som skiffer, lertegel eller koppar och hur svårt det är att få fram "
    "material och ställning brukar påverka mest. Därefter kommer storlek, installationer och ytskikt. Vi kommer ut "
    "gratis och lämnar ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur ser jag om min fastighet på Lidingö har utökad lovplikt?",
     "Lidingö stad visar det som ett blått lager i webbkartan. Är fastigheten gulmarkerad kan det finnas värden som "
     "behöver bedömas, och då är det klokt att kontakta stadens kundcenter."),
    ("Kan en tillbyggnad på en villa i Brevik få skiffertak som huset?",
     "Ja, och det är ofta det som gör att tillbyggnaden smälter in. Skiffer finns på flera av Breviks sadeltak, och "
     "samma material på tillbyggnaden gör det lättare att motivera förslaget."),
    ("Är det värt att söka frivilligt bygglov för en lovfri tillbyggnad på Lidingö?",
     "Det kan vara det vid ett större eller dyrt projekt, eftersom du då får besked i förväg om att "
     "tillbyggnaden följer reglerna. Lidingö stad nämner möjligheten på sin sida om de ändrade reglerna."),
    ("Vilka regler gäller för radhusen i Mölna radhusby?",
     "Kulturmiljöprogrammet rekommenderar att de slammade tegelfasaderna, det enkupiga lerteglet och kopparplåten "
     "bevaras. Kontrollera stadens karta och detaljplanen innan något ändras utvändigt."),
    ("Hur påverkar berget på tomten en tillbyggnad på Lidingö?",
     "Grunden får anpassas efter berget, ibland med plintar eller gjuten platta på berg. Ändras markens höjd mer än en "
     "halv meter inom detaljplan krävs marklov."),
  ],
  "sources": [
    ("Lidingö stad – Ändrade lagar och regler för byggande", "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/"),
    ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet", "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Lidingö villastad (pdf)", "https://share.mediaflow.com/sv/?9OCCB1KE1L"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Breviks villastad (pdf)", "https://share.mediaflow.com/sv/?70CCS1CE0X"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Mölna radhusby (pdf)", "https://share.mediaflow.com/sv/?3ZCCS1LEFX"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Gåshaga, Killinge och Käppala (pdf)", "https://share.mediaflow.com/sv/?P7CCT1JEFN"),
    S_PBL, S_ROT, S_ROTJOB,
  ],
  "cta": ("Vill du bygga på Lidingö?", "Boka ett gratis besök, så går vi igenom tomten, kartan och vad som går att bygga."),
  "img": [
    ("Sekelskiftesvilla med tillbyggnad på en kuperad tomt på Lidingö",
     "Swedish early 1900s wooden villa with red clay tile roof and a new matching extension, on a hilly rocky plot "
     "with stone retaining walls and old oak trees, Lidingö"),
    ("Grund för tillbyggnad på berg vid en villa på Lidingö",
     "construction site for a house extension on bare granite bedrock next to an old Swedish villa, concrete "
     "footings and timber frame, retaining wall, trees, overcast day"),
  ],
},
}
