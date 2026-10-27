# -*- coding: utf-8 -*-
"""Fasadrenovering – ortsidor v12: Sigtuna, Solna, Spånga, Älvsjö, Farsta, Hägersten (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25: Sigtuna kommun (Bevarande-
och förnyelseplan för Sigtuna stad, antagen 2019: ombyggnad, putsat hus, dropplist/sockel, tilläggsisolering,
q/k, ca 60 detaljplaner, stadsplan C4, kv Koppardosan; Riktlinjer för bebyggelseutveckling i dalgången mellan
Odensala och Hova, antagen 2020-12-15: fasad, sekelskiftesvillor, gavelspetsar; Bygga i kulturmiljö), Solna stad
(Planbeskrivning detaljplan Fjället 8, P24/2, laga kraft 2024-02-29: norra Råsunda, ambitionsnivå C, grönklassad
villa 1927–28; Tilläggsplan vindsinredning i Råsunda P09/3; Fasadändring; Kulturmiljöer i Solna), Stockholms stad
(Varsam utveckling av småhus- och villaområden: villastad, småstugeområden, tunnelbanestad, storskalig stadsdel,
eternit-bildtext; bygglov.stockholm: Fasadändring, Stadsmuseets kulturhistoriska klassificering; Områdesfakta 2025
för Tensta, Älvsjö, Liseberg, Fagersjö, Farsta strand, Farsta, Hökarängen; Rådet till skydd för Stockholms skönhet,
yttrande Kopplingsboxen 26, 2022), Stockholmskällan (Stockholms spår: Tensta, Farsta, Hägerstensåsen; S. Lindhagen,
Älvsjö villastad – ett exempel på förortsinventering), Boverket (PBL kunskapsbanken: fasadändring; energiguiden:
tilläggsisolera fasaden; fuktrisker med fasadmaterial och ytskikt; risker med enstegstätning; asbest),
Arbetsmiljöverket (tillstånd för rivning av asbest) och Skatteverket (rotavdrag, lista och så fungerar det).
Strukna (ej verifierade eller oklara i källan): Sigtunas kulturminnesvårdsprogram 1985 (inte online), särskilda
fasadregler för Märsta/Rosersberg/Valsta (ingen källa), Sigtunas egen sida om fasadändring (404), Rödingarna vid
Ulriksdal (ingen gällande fasadbestämmelse hittad), kv Fyrväpplingen (byggnadsminne, redan på snickare-solna),
"panel på förvandring" och Hem på landets färgkrav i Älvsjö (redan på andra Älvsjösidor), Stadsmuseets inventering
av Herrängen/Solberga (ej hittad), Hökmossens exakta stadsdel och byggår (bara mäklarsidor), årtal då Fagersjö
byggdes, att enstegstätade hus är från viss tid, att tegelfasader "sällan behöver bytas", datum för PBL-ändringen
(källan anger lag 2025:974, inte datum), Solna stads villkor om fasad mot allmän plats för villor (oklart återgivet).
Kritikpass 2026-10-25: alla siffror kontrollerade mot källtext – Koppardosan (Ljungberg/Riksbyggen 1940-tal, Romare
1950-tal, röd/gul puts), ca 60 detaljplaner, C4 1925, Odensala–Hova dec. 2020; Fjället 8 1927–1928, laga kraft
februari 2024, ambitionsnivå C, grönklassad; Solna handläggning högst tio veckor, överklagande fyra veckor; Tensta
123 småhus varav 119 äganderätter, inflyttning 1967; Älvsjö 214 småhus/191 äganderätter, Liseberg 255, tomtförsäljning
december 1908, inventering från sommaren 1977; Fagersjö 198/191, Farsta strand 291, Farsta 418, Hökarängen 232
bostadsrätter i småhus, Farsta centrum oktober 1960, 16 våningar; typritningar 1927–1957, Hägerstensåsen 1938/1939/
1948; asbest 1940–1980 (Boverket FAQ), åtta veckor (AV). "Nästan alltid" (putsbortfall) återges som "i de allra
flesta fall". Inga priser, garantier, omdömen, egna uppdrag eller cert. Korslänkar via V4_MODULES i tjanster_v1.py.
Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_FASAD = ("Boverket – PBL kunskapsbanken: Bygglov för fasadändring",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_BV_ISOL = ("Boverket – Energiguiden: Tilläggsisolera fasaden",
            "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/tillaggsisolera-fasaden/")
_BV_FMAT = ("Boverket – Fuktrisker med fasadens material och ytskikt",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/")
_BV_ENST = ("Boverket – Risker med enstegstätning",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/risker-enstegstatning/")
_BV_ASB = ("Boverket – Asbest", "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_AV_ASB = ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest",
           "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_STH_FASAD = ("Stockholms stad – Fasadändring (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_STH_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
               "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ SIGTUNA
"fasadrenovering-sigtuna.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Sigtuna", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Sigtuna – puts, panel och sockel",
  "description": "Fasadrenovering i Sigtuna: putsade hus i stadskärnan, sockel och dropplist vid isolering, q och k i planen och panelen i dalgången. Gratis platsbesök.",
  "h1": "Fasadrenovering i Sigtuna",
  "lead": "I Sigtuna stad ska ett putsat hus enligt kommunens bevarande- och förnyelseplan få förbli putsat, och den som vill isolera utvändigt får en tydlig varning om sockeln. I dalgången mellan Odensala och Hova finns egna riktlinjer, och i villaområdena kring Märsta gäller detaljplanen och lagens krav på varsamhet. Geal Entreprenad AB renoverar fasader i hela Sigtuna kommun, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Puts i stadskärnan, panel i dalgången.",
  "sections": [
    {"id": "putsade-hus", "anchor": "Putsade hus i stadskärnan",
     "h2": "Ett putsat hus ska få förbli putsat",
     "paras": [
       "Bevarande- och förnyelseplanen för Sigtuna stad, antagen 2019, utgår från att ett hus vid ombyggnad och renovering ska behålla det utseende det har i dag. Planen skriver uttryckligen att ett putsat hus bör få vara putsat även i fortsättningen, om inte särskilda skäl talar för en förändring. Samtidigt öppnar den för att rätta till olämpliga detaljer som tillkommit senare, till exempel en olämplig fasadyta eller felaktig färgsättning.",
       "Stadskärnan består inte bara av trähus. I kvarteret Koppardosan vid Stora gatan beskriver planen två putsade tegelbyggnader i två våningar från 1940-talet, ritade av S. L. Ljungberg vid Riksbyggens arkitektkontor, och två putsade bostadshus från 1950-talet ritade av Bengt Romare. Det ena 50-talshuset har rödfärgad och det andra gulfärgad puts, båda med vita fönsteromfattningar.",
       "Boverket förklarar varför putsen behöver skötas med omsorg. Kalkputs kan suga upp, transportera och avge fukt utan att skada stommen, men vid för stor fuktbelastning uppstår skador, och putsbortfall beror i de allra flesta fall på fukt. Vi letar därför först efter var vattnet kommer in och lagar sedan med ett bruk som liknar det som redan sitter på väggen.",
     ],
     "aside": {"title": "Kvarteret Koppardosan", "items": [
       "Putsat tegel från 1940-talet", "Putsade hus från 1950-talet",
       "Röd och gul puts", "Vita fönsteromfattningar"]}},
    {"id": "sockeln", "h2": "Sockeln och dropplisten avgör isoleringen",
     "paras": [
       "Planen pekar ut en detalj som lätt försvinner vid en renovering. Stensockeln på de äldre husen är ofta bredare än själva väggen, och i anslutningen mellan panel och sockel sitter därför en dropplist. Den förändras kraftigt vid utvändig tilläggsisolering om inga särskilda åtgärder vidtas, och planens slutsats är att utvändig isolering bör undvikas och att invändig isolering är att föredra.",
       "Blir det ändå en utvändig isolering ska den nya fasadbeklädnaden enligt planen utformas i princip lika som den gamla, med oförändrat taksprång, utflyttade fönster och anpassad sockel. Boverket beskriver vad som annars händer: fönster och dörrar hamnar längre in, takfoten skjuter ut mindre och fasaden kan hänga ut över sockeln. Utåtgående fönster kan dessutom bli omöjliga att haka av när de ska renoveras.",
       "Invändig isolering gör i sin tur väggens utsida kallare, och Boverket nämner frostsprängning i tegel och sten och röta i trä. Vi bedömer därför väggen innan isoleringen väljs. Ska taket läggas om samtidigt finns mer under " + _L.format("takrenovering-sigtuna.html", "takrenovering i Sigtuna") + ".",
     ],
     "aside": None},
    {"id": "q-och-k", "h2": "q, k och bygglov inom riksintresset",
     "paras": [
       "Inom planens område finns ungefär 60 gällande detaljplaner, och kommunen fattar fortfarande bygglovsbeslut med hjälp av stadens äldsta stadsplan C4 från 1925. Planen förklarar de vanligaste skydden. En skyddsbestämmelse, q, kan omfatta både utformning, material, teknik och underhåll. En varsamhetsbestämmelse, k, beskriver vilka egenskaper byggnaden ska ha, exempelvis färg och fasad- eller taktäckningsmaterial.",
       "Inom riksintresset för kulturmiljövården i Sigtuna stad gäller inte de bygglovsbefriade åtgärderna, och fasadförändringar kräver därför bygglov. Oavsett lovplikt ska ändringar enligt plan- och bygglagen utföras varsamt, så att byggnadens värden inte går förlorade.",
       "Där en q-bestämmelse styr underhållet lagar vi hellre än byter. Färgen på samma fasad beskrivs på sidan om " + _L.format("malare-sigtuna.html", "målare i Sigtuna") + ".",
     ],
     "aside": {"title": "I stadskärnan", "items": [
       "Läs detaljplanen", "Finns q eller k?",
       "Bygglov inom riksintresset", "Varsamhet oavsett lov"]}},
    {"id": "utanfor-staden", "h2": "Dalgången, Märsta och Rosersberg",
     "paras": [
       "Riktlinjerna för dalgången mellan Odensala och Hova antogs i december 2020. De konstaterar att fasadmaterialet på landsbygden nästan uteslutande har varit trä. Sekelskiftesvillorna har fasader av locklistpanel eller spontad panel, och för nya hus rekommenderas stående träpanel, locklistpanel, lockpanel eller spontad panel. Gavelspetsar och partier mellan fönstren bör inte utföras i avvikande material eller färg, eftersom fasaden ska uppfattas som en enhet.",
       "För villorna och radhusen kring Märsta och Rosersberg finns inget motsvarande program. Kommunen skriver ändå att byggnader som inte är utpekade kan vara så värdefulla att de behöver särskild hänsyn, och att ursprungliga material och detaljer i första hand bör behållas eller ersättas med samma material.",
       "Enligt plan- och bygglagen krävs i dag inget bygglov för att byta kulör eller material på fasaden på ett en- eller tvåbostadshus. Undantagen är hus som är särskilt värdefulla, ligger i ett särskilt värdefullt område eller omfattas av utökad lovplikt i detaljplanen. Mer om material och metoder finns på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Sigtuna till",
  "steps": [
    ("Var ligger huset?", "Vi tar reda på om fastigheten ligger i stadskärnan, i dalgången eller i ett villaområde och vad som gäller där."),
    ("Platsbesök", "Puts, panel, sockel och dropplist gås igenom, och vi markerar var fukten tar sig in."),
    ("Val av isolering", "Ska huset isoleras jämför vi in- och utvändig lösning med hänsyn till sockel och fönster."),
    ("Skriftligt kostnadsförslag", "Lagning, omputsning, panelbyte och isolering prissätts som separata poster."),
    ("Lov vid behov", "Inom riksintresset tar vi fram material- och kulörbeskrivning till din ansökan."),
    ("Utförande och genomgång", "Arbetet görs i torrt väder, och vi går igenom fasaden tillsammans efteråt."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Sigtuna",
  "rot": [
    "Skatteverket räknar att byta, reparera och mura fasader, tilläggsisolera och måla fasader som rotarbete i ett småhus, liksom att montera och montera ner ställningar i samband med arbetet. Är huset yngre än fem år får arbetet bara återställa det till ursprungligt skick.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag, och du ska äga bostaden när arbetet utförs. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Sigtuna?",
  "price": [
    "Hur stora partier av putsen som har släppt, om sockel och dropplist måste byggas om, om isoleringen görs in- eller utvändigt och om en bygglovsansökan behöver förberedas. Ett trähus i dalgången och ett putsat hus i stadskärnan kräver olika material. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag byta puts mot träpanel på ett hus i Sigtuna stad?",
     "Bevarande- och förnyelseplanen säger att ett putsat hus bör få vara putsat även i fortsättningen, om inte särskilda skäl talar för en förändring. Inom riksintresset krävs dessutom bygglov för fasadförändringar."),
    ("Varför avråder Sigtunas bevarandeplan från utvändig tilläggsisolering?",
     "Eftersom dropplisten mellan panelen och den breda stensockeln förändras kraftigt. Planen föredrar invändig isolering, och isolerar man ändå utvändigt ska taksprång, fönster och sockel anpassas så att huset ser ut som förut."),
    ("Vad är skillnaden mellan q och k i en detaljplan i Sigtuna?",
     "En q-bestämmelse skyddar byggnaden och kan reglera utformning, material, teknik och underhåll. En k-bestämmelse är en varsamhetsbestämmelse som beskriver egenskaper, till exempel färg och fasadmaterial."),
    ("Vilken panel passar en sekelskiftesvilla i dalgången mellan Odensala och Hova?",
     "Riktlinjerna beskriver locklistpanel eller spontad panel på sekelskiftesvillorna och rekommenderar stående träpanel i någon traditionell form. Gavelspetsar bör inte få ett avvikande material."),
    ("Kan kommunen bedöma om mitt hus i Märsta är kulturhistoriskt värdefullt?",
     "Ja. Skicka adress eller fastighetsbeteckning, foton från husets alla fyra sidor och en beskrivning av vad du vill göra, så gör kommunen en bedömning. Riksantikvarieämbetets bebyggelseregister kan också ge information."),
  ],
  "sources": [
    ("Sigtuna kommun – Bevarande- och förnyelseplan för Sigtuna stad, antagen 2019 (pdf)",
     "https://www.sigtuna.se/download/18.6ed4dd301706254f993282/1582201854957/Bevarande-%20och%20f%C3%B6rnyelseplan%20f%C3%B6r%20Sigtuna%20stad,%20antagen%202019.pdf"),
    ("Sigtuna kommun – Riktlinjer för bebyggelseutveckling i dalgången mellan Odensala och Hova (pdf)",
     "https://www.sigtuna.se/download/18.2b81151517d4919beb8c692e/1638798200988/Riktlinjer%20f%C3%B6r%20bebyggelseutveckling%20i%20dalg%C3%A5ngen%20mellan%20Odensala%20och%20Hova.pdf"),
    ("Sigtuna kommun – Bygga i kulturmiljö",
     "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html"),
    _BV_FASAD, _BV_ISOL, _BV_FMAT, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset i Sigtuna renoveras?", "Boka ett gratis platsbesök så går vi igenom puts, panel och sockel och vad planen säger om huset."),
  "img": [
    ("Putsat hus i två våningar med gul puts, vita fönsteromfattningar och tegeltak i Sigtuna stad",
     "small 1950s two-storey Swedish house with smooth yellow render, white window surrounds, small-paned wooden windows, red clay tile gable roof, on a narrow old town street with a low wooden picket fence and lilac bushes, Sigtuna, summer daylight, no people"),
    ("Rödmålad stående panel som slutar i en dropplist ovanför en sockel av natursten",
     "close-up of the base of an old Swedish wooden house: red painted vertical board-and-batten panel ending in a horizontal wooden drip moulding above a wider grey natural stone plinth, grass in front, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SOLNA
"fasadrenovering-solna.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Solna", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Solna – villorna i norra Råsunda",
  "description": "Fasadrenovering i Solna: putsade villor i norra Råsunda, krav på färg, form och material, fukt i puts och vad en lovansökan behöver. Gratis platsbesök.",
  "h1": "Fasadrenovering i Solna",
  "lead": "Råsunda är mest känt för sina flerfamiljshus längs Råsundavägen, men i norr mot Råstasjön finns ett villaområde som Solna stad pekar ut som en sammanhängande kulturhistoriskt värdefull miljö. Där gäller anpassningskrav för både färg och material. Geal Entreprenad AB renoverar fasader på villor och radhus i Råsunda, Bergshamra, Ulriksdal och övriga Solna, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Putsade villor och krav på material.",
  "sections": [
    {"id": "norra-rasunda", "anchor": "Villorna i norra Råsunda",
     "h2": "Ett villaområde som ska bevaras till sin karaktär",
     "paras": [
       "Stadens tilläggsplan för vindsinredning i Råsunda beskriver ett äldre bostadsområde där många hus uppfördes i början av 1900-talet. Bebyggelsen är blandad eftersom utbyggnaden skedde successivt: flerfamiljshus i fem våningar längs Råsundavägen, lägre hus längre bort och villaområden i norr mot Råstasjön och söderut mot Ekensbergsvägen. Råsunda var i stort sett färdigbyggt på 1950-talet.",
       "Villabebyggelsen i norra Råsunda är i översiktsplanen utpekad som en sammanhängande kulturhistoriskt värdefull miljö som i huvudsak ska bevaras till sin karaktär. Den finns också med i kulturminnesvårdsprogrammet, där Råsunda villastad har ambitionsnivå C. Enligt stadens planbeskrivning för fastigheten Fjället 8 innebär det en miljö som kan sakna homogen karaktär men ändå har kulturhistoriskt eller miljömässigt värde, och anpassningskraven gäller läge, färg, form och material.",
       "För en fasadrenovering betyder det att materialvalet inte är fritt, även när huset saknar skyddsbestämmelse i detaljplanen. Vi utgår från det material huset har i dag och från husen runt omkring, och tar reda på vad som är original innan något byts.",
     ],
     "aside": {"title": "Norra Råsunda", "items": [
       "Villor mot Råstasjön", "Värdefull miljö i översiktsplanen",
       "Ambitionsnivå C", "Krav på färg, form och material"]}},
    {"id": "fjallet-8", "h2": "Villan på Fjället 8: puts, valmat tak och småspröjsade fönster",
     "paras": [
       "Planbeskrivningen för Fjället 8, som vann laga kraft i februari 2024, ger en bild av en typisk villa i området. Huset uppfördes 1927–1928 och har drag från jugend och 1910-talets villaarkitektur, men också nationalromantiska drag från Danmark och Nordtyskland: ett högt valmat tak med två symmetriskt placerade kupor och småspröjsade fönster. Huvudbyggnaden bedöms ha stort kulturhistoriskt värde och är grönklassad.",
       "Planen gällde ett nytt garage. Det antikvariska utlåtandet lyfte fram att garaget ansluter till villan genom putsade fasader och ett valmat tak med lertegel, och placeringen valdes så att huvudbyggnadens fasader kan upplevas i sin helhet från gatorna. Samma tanke gäller vid en renovering: det är villans fasad mot gatan som bär miljön.",
       "Boverket påpekar att en ändring av färgtyp, till exempel från linoljefärg till plastfärg, kan påverka byggnadens yttre karaktärsdrag, medan ommålning i samma kulör normalt räknas som underhåll. På en putsad villa från 1920-talet lagar vi därför sprickor med ett bruk som passar den befintliga putsen och väljer en avfärgning som fungerar på underlaget. Om kulörerna finns mer under " + _L.format("malare-solna.html", "målare i Solna") + ".",
     ],
     "aside": None},
    {"id": "fukt-puts", "h2": "Därför släpper putsen",
     "paras": [
       "Boverket konstaterar att putsbortfall i de allra flesta fall beror på fukt. Kalkputs kan ta upp och avge fukt utan att stommen skadas, men blir belastningen för stor uppstår skador, och fuktig puts kan frysa sönder om fukten sitter kvar över vintern. Myndigheten pekar också på att tjockare isolering gör väggens yttre delar kallare, vilket kan hindra en putsad fasad från att torka ut.",
       "De svaga punkterna är anslutningarna mot fönster och dörrar, stuprörens infästningar och skarvarna. Där behövs tvåstegstätning, så att vatten som kommer förbi det yttre skiktet kan ledas ut igen. Boverket noterar att en enstegstätning med mjukfog kan ha relativt kort livslängd även när den är väl utförd, och att det vid fönster ofta saknas vattenavledning mellan karm och omfattning.",
       "Vid besöket knackar vi på putsen för att hitta partier som har släppt, tittar på fönsterblecken och sockeln och följer stuprören ner till marken. Ska takfoten och taket ses över samtidigt finns mer under " + _L.format("takrenovering-solna.html", "takrenovering i Solna") + ".",
     ],
     "aside": {"title": "På en putsad villa", "items": [
       "Bom puts vid hörnen", "Sprickor under fönsterbleck",
       "Fogar mot karmarna", "Stuprörens fästen"]}},
    {"id": "lov-solna", "h2": "Bygglov för fasaden i Solna",
     "paras": [
       "Solna stad skriver att bygglov krävs om fasadändringen gäller en särskilt värdefull byggnad eller ett särskilt värdefullt område, eller om detaljplanen säger att åtgärden kräver lov. Som fasadändring räknar staden bland annat byte av fasadfärg, fasadmaterial eller taktäckning. I Solnakartan ser du gällande detaljplan och vilka byggnader och områden som är kulturhistoriskt värdefulla.",
       "Till en ansökan behövs normalt situationsplan, fasadritning, planritning och en material- och kulörbeskrivning, och ibland foton där grannhusen syns eller en antikvarisk förundersökning. Omfattar arbetet även tilläggsisolering eller nya fönster kräver staden dessutom en kontrollansvarig. Handläggningstiden är högst tio veckor från komplett ansökan, och grannar har sedan fyra veckor på sig att överklaga. Mer om puts och panel finns på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Solna till",
  "steps": [
    ("Solnakartan", "Vi kontrollerar detaljplan, klassning och om fastigheten ligger i en utpekad miljö."),
    ("Platsbesök", "Putsen knackas av, och fönsteranslutningar, sockel och stuprör gås igenom."),
    ("Skriftligt kostnadsförslag", "Lagning, omputsning och avfärgning redovisas var för sig med bruk och färg angivna."),
    ("Underlag till ansökan", "Behövs bygglov tar vi fram material- och kulörbeskrivning till ansökan."),
    ("Utförande", "Puts och avfärgning görs i lämpligt väder, och anslutningarna tätas i två steg."),
    ("Genomgång", "Vi går runt huset tillsammans och visar vad som har lagats."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Solna",
  "rot": [
    "På ett småhus ger det rotavdrag att reparera och mura fasader, måla fasader och tilläggsisolera, liksom att sätta upp ställningar som behövs för arbetet. I en bostadsrätt räknas fasaden som gemensam yta, och då ger arbetet inget avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Solna?",
  "price": [
    "Hur stor del av putsen som har släppt, om hela fasaden behöver putsas om, vilken avfärgning som passar underlaget, hur många fönsteranslutningar som ska göras om och om ett bygglov behöver förberedas. Tomtens terräng påverkar också hur ställningen ställs upp. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Vad innebär ambitionsnivå C för en villa i Råsunda?",
     "Att miljön bedöms ha kulturhistoriskt eller miljömässigt värde även om den inte är helt enhetlig. Enligt Solna stad gäller anpassningskraven läge, färg, form och material."),
    ("Behöver jag bygglov för att putsa om villan i norra Råsunda?",
     "Byts putsen mot samma material och utförande räknas det enligt Boverket som underhåll. Byter du fasadmaterial eller kulör i en kulturhistoriskt värdefull miljö krävs bygglov enligt Solna stad."),
    ("Vilka handlingar behövs för en fasadändring i Solna?",
     "Normalt situationsplan, fasadritning, planritning och en material- och kulörbeskrivning. Ibland begär staden fotografier där grannhusen syns eller en antikvarisk förundersökning."),
    ("Hur lång tid tar ett bygglov för fasaden i Solna?",
     "Handläggningstiden är högst tio veckor från att ansökan är komplett. Efter beslutet har grannar och andra sakägare fyra veckor på sig att överklaga."),
    ("Varför spricker putsen under fönstren på vår villa i Solna?",
     "Ofta tar vatten sig in där karm, bleck och puts möts. Boverket rekommenderar tvåstegstätning vid sådana anslutningar, så att vatten som kommer förbi kan ledas ut igen."),
  ],
  "sources": [
    ("Solna stad – Planbeskrivning, detaljplan för Fjället 8 i Råsunda, laga kraft 2024 (pdf)",
     "https://www.solna.se/download/18.d9b843718dfa99e174dfd7/1709812406982/Planbeskrivning_LAGAKRAFT.pdf"),
    ("Solna stad – Tilläggsplan för vindsinredning i Råsunda, plan- och genomförandebeskrivning (pdf)",
     "https://www.solna.se/download/18.6ce5045216a58f96d2f451b0/1560347652584/P09_3%20Till%C3%A4ggsplan,%20vindsinredning%20i%20R%C3%A5sunda_Plan-%20och%20genomf%C3%B6randebeskrivning.pdf"),
    ("Solna stad – Fasadändring", "https://www.solna.se/bygga-bo--miljo/bygga/guide/vanliga-byggatgarder/fasadandring"),
    ("Solna stad – Kulturmiljöer i Solna", "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna"),
    _BV_FASAD, _BV_FMAT, _BV_ENST, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på villan i Solna renoveras?", "Boka ett gratis platsbesök så går vi igenom putsen, anslutningarna och vad som gäller för din fastighet."),
  "img": [
    ("Ljusputsad villa med brant tegeltak, takkupor och småspröjsade fönster bakom en klippt häck i Solna",
     "late 1920s Swedish villa with light smooth render, tall steep hipped red clay tile roof with two small symmetrical dormers, small-paned white wooden windows, mature oak trees and a hedge, quiet villa street in Råsunda Solna, autumn daylight, no people"),
    ("Ljus putsfasad under ett vitt fönster med plåtbleck",
     "close-up of a masonry villa wall finished with rough light beige lime render plaster (stucco texture, no wooden boards), below a white wooden window with a grey metal sill flashing, two short cracks in the render filled with fresh slightly lighter plaster patches, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SPÅNGA
"fasadrenovering-spanga.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Spånga", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Spånga – villastäder och radhus i Tensta",
  "description": "Fasadrenovering i Spånga: trävillor i Bromsten, Flysta och Sundby, hus från flera epoker, radhus med skivor i Tensta och lovfrågan. Gratis platsbesök.",
  "h1": "Fasadrenovering i Spånga",
  "lead": "Spånga rymmer både villastäderna som växte upp kring järnvägen och miljonprogrammets Tensta med sina gruppbyggda småhus. Fasaderna skiljer sig därefter: trä och puts i villastäderna, tegel, trä och skivor i radhusen. Geal Entreprenad AB renoverar fasader i Bromsten, Flysta, Solhem, Sundby, Tensta och övriga Spånga, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Trävillor och gruppbyggda radhus.",
  "sections": [
    {"id": "villastaden", "anchor": "Villastäderna",
     "h2": "Trä, puts och glasverandor i villastäderna",
     "paras": [
       "Stockholms stads strategi Varsam utveckling av småhus- och villaområden räknar Bromsten, Solhem, Flysta och Sundby till typen villastad. Den beskriver hur små stationssamhällen uppstod när järnvägen byggdes ut, och hur några av dem på 1910-talet blev municipalsamhällen med egen administration och beskattningsrätt, till exempel Spånga. Villastäderna var privat organiserade och fick en brokigare bebyggelse än de egnahemsområden som staden planerade.",
       "Enligt strategin var trä det dominerande fasadmaterialet, även om puts förekom. Glasverandor, takkupor, snickarglädje och färgsättning gav husen den variation som syns än i dag. En av stadens vägledningar gäller direkt fasaden: karaktärsskapande material, kulörer, byggnadsdelar och detaljer ska tas tillvara eller återskapas i så stor utsträckning som möjligt vid ombyggnader och renoveringar.",
       "Vi börjar därför med att ta reda på vad som är original. Under en senare beklädnad kan den gamla panelen finnas kvar, och snickerierna kring en veranda kan ofta lagas i stället för att bytas. Om kulörerna finns mer under " + _L.format("malare-spanga.html", "målare i Spånga") + ".",
     ],
     "aside": {"title": "Villastaden enligt staden", "items": [
       "Trä som huvudmaterial", "Puts på en del hus",
       "Glasverandor och takkupor", "Ta tillvara detaljerna"]}},
    {"id": "epoker", "h2": "Hus från olika årtionden på samma gata",
     "paras": [
       "Strategin beskriver hur villastäderna har förtätats genom att tomter delats av, så att nya hus på tomter kring 600 kvadratmeter har kompletterat eller ersatt den äldre bebyggelsen. Radhus, parhus och mindre flerfamiljshus har tillkommit, och därför finns flera tidsepoker representerade längs samma gata.",
       "Det påverkar renoveringen, eftersom ett yngre hus på en avstyckad tomt kan ha en helt annan vägg än grannens villa. Boverket varnar för träregelväggar som byggts med enstegstätade putssystem, där regn har tagit sig in och orsakat omfattande fuktskador. På en enstegstätad fasad finns bara en tätningsnivå mot regn, och vatten som kommer innanför kan bara torka ut genom långsamma processer.",
       "På en äldre trävilla handlar det oftare om panel som har fuktats upp. Boverket påpekar att akrylatfärg på träpanel kräver en alkydoljegrundfärg, och att panel som målats utan den kunde fuktas upp kraftigt av regn. Vi gör därför ett skrapprov och bestämmer färgsystem innan panelen lagas. Taket på samma hus beskrivs under " + _L.format("takrenovering-spanga.html", "takrenovering i Spånga") + ".",
     ],
     "aside": None},
    {"id": "tensta", "h2": "Radhusen i Tensta: tegel, trä och skivor",
     "paras": [
       "Tensta byggdes inom miljonprogrammet, och den första inflyttningen skedde 1967 enligt Stadsmuseets skrift om stadsdelen. Strategin räknar Tensta till de storskaliga stadsdelarna, där de gruppbyggda småhusen ofta har en blandning av fasadmaterial som tegel, trä och skivor, platta tak eller pulpettak och en färgsättning som är enhetlig inom varje husgrupp. Stadens områdesfakta för 2025 räknar 123 bostäder i småhus i Tensta, varav 119 äganderätter.",
       "I många områden från den här tiden användes asbestcement, mer känt som eternit. Strategin konstaterar att skivorna i många fall har bytts ut och att det i dag finns fasadskivor utan asbest, så att radhusens uttryck kan behållas. Boverket bedömer att asbest sannolikt finns någonstans i hus byggda 1940–1980, och att bara provtagning och analys ger ett säkert svar.",
       "Visar provet asbest ska skivorna rivas av ett företag som har tillstånd från Arbetsmiljöverket, och ansökan görs åtta veckor innan arbetet börjar. Eftersom färgsättningen är gemensam för husgruppen är det klokt att stämma av material och kulör med grannarna innan den nya fasaden beställs.",
     ],
     "aside": {"title": "Radhus i Tensta", "items": [
       "Tegel, trä och skivor", "Samma färg i husgruppen",
       "Prov på äldre skivor", "Nya skivor utan asbest"]}},
    {"id": "lov-spanga", "h2": "Stadsmuseets karta och lov i Spånga",
     "paras": [
       "Stockholms stad räknar byte av kulör eller material på fasaden och tilläggsisolering som fasadändringar. För en- och tvåbostadshus krävs inte längre bygglov om vissa förutsättningar är uppfyllda, men utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla byggnader och områden. Stadsmuseets klassificeringskarta ger en första indikation, och blå eller grön markering betyder att lov behövs.",
       "Ligger huset på en streckad yta som ännu inte är inventerad kan lov ändå krävas. Stadsmuseet brukar svara inom tre veckor om du mejlar adress, byggnadsår, tidigare ombyggnader och foton av fasaderna. Hos staden kan man också beställa äldre miljöprogram och typritningssamlingar, som saknar juridisk status men beskriver områdets karaktär. Läs mer om material på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Spånga till",
  "steps": [
    ("Husets historia", "Vi tar reda på byggår, senare ombyggnader och hur väggen är uppbyggd."),
    ("Platsbesök", "Panel, puts eller skivor gås igenom, och vi gör skrapprov på färgen."),
    ("Prov vid behov", "Äldre fasadskivor provas innan de tas ner."),
    ("Skriftligt kostnadsförslag", "Rivning, ny beklädnad, målning och anslutningar redovisas som egna poster."),
    ("Utförande", "Ny panel eller nya skivor monteras med luftspalt och tvåstegstätning vid fönstren."),
    ("Genomgång", "Vi går runt huset tillsammans när arbetet är klart."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Spånga",
  "rot": [
    "För ett småhus ger byte och reparation av fasader, fasadmålning och tilläggsisolering rotavdrag. Sanering av asbest i samband med byggarbetet ger också avdrag, men inte en mätning som görs för sig.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Spånga?",
  "price": [
    "Vilken beklädnad huset har i dag, om asbest måste saneras, hur mycket panel eller hur många skivor som ska bytas och om husgruppen ska ha samma material. En trävilla med glasveranda kräver mer snickeri än ett radhus. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilket fasadmaterial hade villorna i Spångas villastäder från början?",
     "Enligt Stockholms stads strategi var trä det dominerande materialet, men puts förekom. Det enskilda huset kan ha bytt beklädnad, så det är klokt att öppna på ett dolt ställe."),
    ("Får vi byta fasadskivor på vårt radhus i Tensta till ett annat material?",
     "Kontrollera först Stadsmuseets karta och detaljplanen. Staden råder att förändringar i sammanhållna husgrupper utformas utifrån helheten, och det finns asbestfria skivor som behåller radhusens uttryck."),
    ("Varför flagnar och ruttnar panelen på vår villa i Bromsten?",
     "En möjlig orsak är tät plastfärg utan rätt grundfärg. Boverket skriver att akrylatfärg kräver alkydoljegrundfärg och att panelen annars kan fuktas upp kraftigt av regn."),
    ("Hur får jag Stadsmuseets bedömning av mitt hus i Spånga?",
     "Mejla adress, fastighetsbeteckning, stadsdel, byggnadsår, tidigare ombyggnader och foton av fasaderna. Museet brukar svara inom tre veckor efter att ha fått alla uppgifter."),
    ("Kan en fasad med bara en tätningsnivå ge fuktskador?",
     "Ja. Boverket beskriver enstegstätade putssystem på träregelväggar som känsliga, eftersom vatten som kommer innanför bara torkar ut långsamt. Anslutningar bör tätas i två steg."),
  ],
  "sources": [
    _STH_VARSAM,
    ("Stockholms stad – Områdesfakta Tensta (2025, pdf)", _OF + "vasterort/jarva/tensta.pdf"),
    ("Stockholmskällan / Stadsmuseet – Stockholms spår: Tensta (pdf)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000034.pdf"),
    _STH_FASAD, _STH_KLASS, _BV_FMAT, _BV_ENST, _BV_ASB, _AV_ASB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset i Spånga renoveras?", "Boka ett gratis platsbesök så tar vi reda på vad väggen består av och vad som bör sparas."),
  "img": [
    ("Äldre ljusgul trävilla med takkupa och fönsterluckor bakom en klippt häck i Spånga",
     "early 1900s Swedish wooden villa painted pale yellow with white trim, a glazed veranda and a small dormer, red clay tile roof, behind a clipped hedge with fruit trees in the garden, quiet villa street in Bromsten Spånga Stockholm, autumn daylight, no people"),
    ("Radhusvägg med släta grå fasadskivor bredvid brunmålad stående träpanel",
     "close-up of a 1970s Swedish terraced house wall: left half clad with dark brown painted vertical wooden board panel, right half clad with large smooth flat grey fibre cement facade sheets fixed with small visible screws and narrow vertical joints, a white window with metal sill flashing in the grey part, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"fasadrenovering-alvsjo.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Älvsjö", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Älvsjö – villastad och nya grannhus",
  "description": "Fasadrenovering i Älvsjö: Hallmans villastad, Stadsmuseets inventering, nya hus på delade tomter och skarven mellan puts och trä. Gratis platsbesök.",
  "h1": "Fasadrenovering i Älvsjö",
  "lead": "I Älvsjö villastad står villor från 1910-talet sida vid sida med hus från senare årtionden. Stockholms stad räknar Älvsjö till de villastäder där äldre stadsplaner tillåter generösa byggrätter, och där varsamheten därför behöver vara stor. Geal Entreprenad AB renoverar fasader i Älvsjö, Långbro, Liseberg, Solberga och övriga Älvsjö, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villastad, nya grannhus och puts på trä.",
  "sections": [
    {"id": "villastaden-alvsjo", "anchor": "Villastaden",
     "h2": "En villastad planerad efter trädgårdsstadens principer",
     "paras": [
       "Stadens strategi Varsam utveckling av småhus- och villaområden nämner Älvsjö som ett av de stationssamhällen som på 1910-talet fick status som municipalsamhälle. Stadsplanen för Älvsjö villastad togs fram av Per Olof Hallman efter samma grundprinciper som hans planer för den tidiga trädgårdsstaden. Strategin beskriver villastäderna som privat organiserade, med individuellt utformade hus där trä var det dominerande fasadmaterialet och puts förekom.",
       "Stadens områdesfakta för 2025 räknar 214 bostäder i småhus i stadsdelen Älvsjö, och 191 av dem är äganderätter. I grannstadsdelen Liseberg finns ytterligare 255 småhus som äganderätter. Det är alltså främst enskilda husägare som bestämmer över fasaderna här, hus för hus.",
       "Strategins vägledning för villastaden är att karaktärsskapande material, kulörer, byggnadsdelar och detaljer ska tas tillvara eller återskapas så långt som möjligt. För en villa som har klätts in under senare år kan en fasadrenovering vara ett tillfälle att föra tillbaka det ursprungliga materialet.",
     ],
     "aside": {"title": "Villastaden Älvsjö", "items": [
       "Municipalsamhälle på 1910-talet", "Stadsplan av P. O. Hallman",
       "Trä och puts", "214 småhus i stadsdelen"]}},
    {"id": "inventeringen", "h2": "Stadsmuseets inventering som förlaga",
     "paras": [
       "Sommaren 1977 började Stockholms stadsmuseum inventera stadens förorter, och Älvsjö var en av de fjorton första stadsdelarna. Suzanne Lindhagens redogörelse beskriver metoden: inventerarna tog sig runt på cykel, besiktade exteriörerna, markerade bebyggelse från tiden före omkring 1930 som behållit sin karaktär och fotograferade samtliga inventerade fastigheter. Materialet skulle bland annat fungera som underlag i plan- och byggärenden.",
       "För en fasadrenovering är det användbart. Fotona och kartorna kan visa hur ett hus såg ut innan senare förändringar, och när ett listverk, en foderbräda eller en panel saknas kan de ge en förlaga att arbeta efter. Redogörelsen berättar också att tomtförsäljningen i villastaden började i december 1908 och att en stadsplan fastställdes redan 1921.",
       "Vi frågar därför gärna efter gamla foton eller ritningar till huset och jämför med det som syns när vi öppnar beklädnaden på ett dolt ställe. Taket på samma villa beskrivs under " + _L.format("takrenovering-alvsjo.html", "takrenovering i Älvsjö") + ".",
     ],
     "aside": None},
    {"id": "nya-grannar", "h2": "När grannhuset är nytt",
     "paras": [
       "Strategin konstaterar att äldre stadsplaner med generösa byggrätter finns bland annat i Älvsjö, och att förtätningen av villastadsdelarna tog ny fart under 2010-talet. Fastigheter har köpts upp och styckats av, och på samma yta har flera en- och tvåbostadshus eller flerbostadshus byggts. Staden skriver att en sådan utveckling ställer stora krav på varsamhet.",
       "Den som renoverar en äldre villa bredvid ett nybygge kan frestas att välja samma moderna material som grannen. Strategin pekar åt ett annat håll. Material, färgsättning och byggnadsdelar räknas till de aspekter som har stor påverkan på områdets karaktär och värde, och det är den äldre villan som bär sambandet med villastadens historia.",
       "Vi föreslår därför material efter husets egen ålder, inte efter gatans yngsta hus. På en villa från 1920-talet blir det ofta träpanel med samma profil som tidigare, eller puts som lagas med ett liknande bruk. Om kulörerna finns mer under " + _L.format("malare-alvsjo.html", "målare i Älvsjö") + ".",
     ],
     "aside": {"title": "Inför valet av material", "items": [
       "Husets byggår", "Gamla foton och ritningar",
       "Original under beklädnaden", "Grannarnas äldre hus"]}},
    {"id": "puts-tra", "h2": "Puts, trä och lovfrågan",
     "paras": [
       "Många villor kombinerar puts och trä. Boverket beskriver hur timmerhusen under 1800-talet fick träpanel som skydd för stommen, och hur puts senare användes på murade hus men även på hus med trästomme. Där två material möts uppstår skarvar som behöver tätas i två steg, så att vatten som tar sig förbi det yttre skiktet kan rinna ut. På panelen är nederkanten mot sockeln och partierna under fönsterbleck mest utsatta.",
       "Putsbortfall beror enligt Boverket i de allra flesta fall på fukt, och fuktig puts kan frysa sönder om fukten sitter kvar över vintern. Vi letar därför efter orsaken innan något lagas och byter bara de delar som är skadade.",
       "Lovfrågan avgörs av Stadsmuseets klassificering och detaljplanen. Hus som är markerade med gult eller grått i kartan behöver inte lov om inget annat gäller, medan blå eller grön markering eller skyddsbestämmelser i planen betyder att lov krävs. Läs mer om metoderna på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Älvsjö till",
  "steps": [
    ("Foton och ritningar", "Vi går igenom gamla bilder, ritningar och Stadsmuseets klassning för huset."),
    ("Platsbesök", "Puts, panel, skarvar och sockel undersöks, och vi öppnar på ett dolt ställe vid behov."),
    ("Materialval", "Material och profil väljs efter husets ålder och det som finns kvar av originalet."),
    ("Skriftligt kostnadsförslag", "Lagning, byte och avfärgning redovisas som separata poster."),
    ("Utförande", "Skarvar mellan puts och trä tätas i två steg, och arbetet görs i torrt väder."),
    ("Genomgång", "Vi går igenom fasaden tillsammans och visar vad som har bytts."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Älvsjö",
  "rot": [
    "Skatteverket räknar fasadrengöring, reparation och byte av fasader, fasadmålning och tilläggsisolering som rotarbete i ett småhus. Byggnadsställningar som monteras för arbetet ingår också.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Du behöver äga huset när arbetet utförs. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Älvsjö?",
  "price": [
    "Hur mycket av den ursprungliga fasaden som finns kvar, om både puts och panel behöver lagas, om en senare inklädnad ska tas bort och om profiler måste specialbeställas. Även ställningen kring ett hus i två våningar påverkar. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem ritade stadsplanen för Älvsjö villastad?",
     "Per Olof Hallman, enligt Stockholms stads strategi för småhus- och villaområden. Han använde samma grundprinciper som i sina planer för den tidiga trädgårdsstaden."),
    ("Finns det gamla bilder på min villa i Älvsjö?",
     "Stockholms stadsmuseum inventerade Älvsjö i slutet av 1970-talet och fotograferade då samtliga inventerade fastigheter. Kontakta Stadsmuseet för att se om ditt hus finns med."),
    ("Ska vi välja samma fasad som det nya huset bredvid?",
     "Stadens strategi räknar material, färgsättning och byggnadsdelar till det som påverkar villastadens karaktär mest. För en äldre villa är det oftast bättre att utgå från husets egen ålder och originalmaterial."),
    ("Behöver jag bygglov för ny fasad på en gulmarkerad villa i Älvsjö?",
     "Är huset gult eller grått i Stadsmuseets karta, och varken detaljplanen eller ett särskilt värdefullt område kräver det, behövs normalt inget bygglov. Kontrollera ändå detaljplanen först."),
    ("Hur många småhus finns det i Älvsjö?",
     "Stadens områdesfakta för 2025 räknar 214 bostäder i småhus i stadsdelen Älvsjö, varav 191 äganderätter. I Liseberg finns ytterligare 255 småhus som äganderätter."),
  ],
  "sources": [
    _STH_VARSAM,
    ("Stockholmskällan / Stadsmuseet – S. Lindhagen: Älvsjö villastad, ett exempel på förortsinventering (pdf)",
     "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf"),
    ("Stockholms stad – Områdesfakta Älvsjö (2025, pdf)", _OF + "soderort/hagersten/alvsjo.pdf"),
    ("Stockholms stad – Områdesfakta Liseberg (2025, pdf)", _OF + "soderort/hagersten/liseberg.pdf"),
    _STH_KLASS, _STH_FASAD, _BV_FMAT, _BV_ENST, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på villan i Älvsjö renoveras?", "Boka ett gratis platsbesök så går vi igenom puts, panel och vad som finns kvar av originalet."),
  "img": [
    ("Villa med vitputsad bottenvåning och brun liggande träpanel i gaveln i Älvsjö",
     "1910s Swedish villa with smooth white rendered ground floor and dark brown painted horizontal wooden panel in the upper gable, small-paned windows with shutters, steep red clay tile roof, next door a modern light grey two-storey house, garden with apple trees and a hedge, Älvsjö Stockholm, autumn daylight, no people"),
    ("Vit fasad och rött pannat tak på en villa",
     "close-up of the junction between a smooth white rendered lower wall and dark brown painted horizontal wooden panel above on an old Swedish villa, a new metal drip flashing along the joint, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ FARSTA
"fasadrenovering-farsta.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Farsta", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Farsta – radhus i tegel, puts och skivor",
  "description": "Fasadrenovering i Farsta: radhus i ABC-staden, Fagersjös grupphus, fibercementskivor och asbest, och hur husgruppen hålls ihop. Gratis platsbesök.",
  "h1": "Fasadrenovering i Farsta",
  "lead": "När Farsta centrum invigdes 1960 lades flera stora radhusområden i stadsdelens utkanter, och i Fagersjö finns gruppbyggda småhus från de storskaliga stadsdelarnas tid. Fasaderna är av tegel, puts, trä och fibercementskivor, och varje husgrupp har sin gemensamma färgsättning. Geal Entreprenad AB renoverar fasader i Farsta, Farsta strand, Fagersjö, Sköndal och övriga Farsta, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Radhus, grupphus och fasadskivor.",
  "sections": [
    {"id": "abc-staden", "anchor": "Radhusen i ABC-staden",
     "h2": "Radhusen i utkanten av ABC-staden",
     "paras": [
       "Farsta centrum invigdes i oktober 1960 som den första ABC-staden i Söderort, där bokstäverna stod för arbetsplatser, bostäder och centrum. Stadsmuseets skrift om stadsdelen beskriver de 16 våningar höga punkthusen intill centrum, en lägre bebyggelse ju längre ut man kommer och flera stora radhusområden i utkanterna.",
       "Stadens strategi Varsam utveckling av småhus- och villaområden räknar Farsta, Farsta strand och delar av Sköndal till de gruppbyggda småhusområdena i tunnelbanestäderna. Även i Farsta präglades gestaltningen enligt strategin av höga ambitioner. Fasader i rött tegel var vanliga, men det förekom även puts och skivor i fibercement.",
       "Stadens områdesfakta för 2025 räknar 291 äganderätter i småhus i Farsta strand och 418 i stadsdelen Farsta. Varje husägare ansvarar alltså för sin egen fasad, men husen ingår i grupper där ett avvikande material syns tydligt.",
     ],
     "aside": {"title": "Farstas radhus", "items": [
       "Rött tegel", "Puts på en del hus",
       "Skivor i fibercement", "Samma färg i husgruppen"]}},
    {"id": "fagersjo", "h2": "Fagersjö: grupphus med blandade material",
     "paras": [
       "Fagersjö hör enligt strategin till de gruppbyggda småhusområdena i storskaliga stadsdelar, tillsammans med bland annat Bredäng, Sätra och Skärholmen. Småhusen där var huvudsakligen radhus och kedjehus, ofta med en blandning av fasadmaterial som tegel, trä och skivor, men med mycket stor enhetlighet inom husgrupperna. Färgsättningen var noga komponerad, och taken var ofta platta eller svagt lutande pulpettak.",
       "Enligt områdesfakta för 2025 finns 198 bostäder i småhus i Fagersjö, och 191 av dem är äganderätter. Strategin påpekar att de gruppbyggda husen står på små tomter, vilket gör utrymmet för större förändringar av det enskilda huset begränsat.",
       "För fasaden innebär det att renoveringen bör utgå från husgruppens material och kulör. Strategins råd till fastighetsägare är att följa de andra byggnaderna i kvarteret och undvika förändringar mot gatan som påverkar den enhetliga bebyggelsen. Om målningen finns mer under " + _L.format("malare-farsta.html", "målare i Farsta") + ".",
     ],
     "aside": None},
    {"id": "skivor", "h2": "Fibercementskivor, eternit och asbest",
     "paras": [
       "Strategin beskriver asbestcement, mer känt som eternit, som ett populärt material i många av tidens områden, och konstaterar att skivorna ofta har bytts mot annat. Boverket skriver att många fasader redan under 1940- och 1950-talen kläddes med cementfiberplattor som innehöll asbest, och att plattorna förbjöds på 1970-talet. De är nästan underhållsfria så länge de är hela, men fibrer kan frigöras om man borrar i dem.",
       "Boverket bedömer att asbest sannolikt finns någonstans i byggnader uppförda 1940–1980, och att provtagning och analys är det enda säkra sättet att veta. Uppgifter kan också finnas i bygglovshandlingarna. Att riva asbesthaltigt material på en fasad kräver enligt Arbetsmiljöverket ett företag med tillstånd, och ansökan ska lämnas åtta veckor innan arbetet börjar.",
       "Efter saneringen byggs fasaden upp igen. Strategin noterar att det i dag finns fasadskivor utan asbest, vilket gör det möjligt att behålla radhusens uttryck. Vi föreslår skivor med liknande format och fogbild, så att huset inte sticker ut i raden.",
     ],
     "aside": {"title": "Före rivning av skivor", "items": [
       "Byggt 1940–1980?", "Prov och analys",
       "Rivning med tillstånd", "Liknande format och fogar"]}},
    {"id": "tegel-lov", "h2": "Tegel, puts och lovfrågan i Farsta",
     "paras": [
       "På en tegelfasad handlar renoveringen främst om fogar och anslutningar. Boverket pekar på att anslutningar mot fönster, dörrar och stuprör behöver tvåstegstätning, och att en enstegstätning med mjukfog kan ha relativt kort livslängd även när den är väl utförd. På putsade partier beror putsbortfall i de allra flesta fall på fukt.",
       "Stockholms stad räknar byte av kulör eller material på fasaden och tilläggsisolering som fasadändringar. För ett en- eller tvåbostadshus krävs normalt inget bygglov, men utökad lovplikt gäller där huset eller området är särskilt kulturhistoriskt värdefullt eller detaljplanen har skyddsbestämmelser. Stadsmuseets klassificeringskarta ger en första indikation, och museet kan göra en bedömning.",
       "I Hökarängen räknar områdesfakta 232 småhus som bostadsrätter. I en bostadsrätt räknar Skatteverket fasaden som gemensam yta, och arbetet ger då inget rotavdrag. Läs mer på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Farsta till",
  "steps": [
    ("Husgruppen först", "Vi tittar på grannhusen och tar reda på husgruppens ursprungliga material och kulör."),
    ("Platsbesök", "Tegel, fogar, puts, skivor och anslutningar gås igenom."),
    ("Prov på skivor", "Äldre fasadskivor provas innan något tas ner."),
    ("Skriftligt kostnadsförslag", "Sanering, ny beklädnad, fogning och bleck redovisas som egna poster."),
    ("Utförande", "Arbetet planeras så att väggen inte står öppen längre än nödvändigt."),
    ("Genomgång", "Vi går runt huset tillsammans och visar vad som har bytts."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Farsta",
  "rot": [
    "I ett småhus ger byte och reparation av fasader, fasadmålning och tilläggsisolering rotavdrag. Asbestsanering i samband med byggarbetet ger också avdrag, medan provtagning och mätning av asbest inte gör det.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Farsta?",
  "price": [
    "Om skivorna innehåller asbest, hur stor yta som ska bytas, vilket skivformat som passar husgruppen och hur många fönsteranslutningar som ska göras om. Ett gavelhus har mer fasad än ett mellanhus. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste vårt radhus i Fagersjö ha samma fasadfärg som grannarnas?",
     "Det beror på detaljplanen och klassningen, men stadens strategi råder att följa de andra byggnaderna i kvarteret och undvika förändringar som påverkar husgruppens enhetliga uttryck."),
    ("Vilket material hade radhusen i Farsta från början?",
     "Enligt Stockholms stads strategi var rött tegel vanligt, men det förekom även puts och skivor i fibercement. Husgrupperna skiljer sig åt, så det är bäst att utgå från ditt eget hus."),
    ("Kan eternitskivor på fasaden bytas mot skivor som ser likadana ut?",
     "Ja, strategin noterar att det i dag finns fasadskivor utan asbest som gör det möjligt att behålla radhusens uttryck. Rivningen av de gamla skivorna kräver ett företag med tillstånd."),
    ("Får vi rotavdrag för fasaden om radhuset i Hökarängen är en bostadsrätt?",
     "Nej. Skatteverket räknar fasader som gemensamma ytor i en bostadsrätt, och arbete på dem ger inget avdrag."),
    ("Hur lång tid innan arbetet ska asbesttillståndet sökas?",
     "Arbetsmiljöverket anger att ansökan ska göras åtta veckor innan arbetet är tänkt att börja. Tillståndet söks av företaget som river."),
  ],
  "sources": [
    ("Stockholmskällan / Stadsmuseet – Stockholms spår: Farsta (pdf)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000015.pdf"),
    _STH_VARSAM,
    ("Stockholms stad – Områdesfakta Fagersjö (2025, pdf)", _OF + "soderort/farsta/fagersjo.pdf"),
    ("Stockholms stad – Områdesfakta Farsta strand (2025, pdf)", _OF + "soderort/farsta/farsta-strand.pdf"),
    ("Stockholms stad – Områdesfakta Farsta (2025, pdf)", _OF + "soderort/farsta/farsta.pdf"),
    ("Stockholms stad – Områdesfakta Hökarängen (2025, pdf)", _OF + "soderort/farsta/hokarangen.pdf"),
    _BV_FMAT, _BV_ENST, _BV_ASB, _AV_ASB, _STH_FASAD, _STH_KLASS, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på radhuset i Farsta renoveras?", "Boka ett gratis platsbesök så går vi igenom tegel, skivor och fogar och vad som passar husgruppen."),
  "img": [
    ("Radhus från 1960-talet i rött tegel med platta tak längs en gångväg i Farsta",
     "Swedish modernist 1960s terraced houses in Stockholm suburb: long low row of two-storey houses with red brick walls, flat roofs with a thin dark wooden fascia, large plain windows with teak-brown frames, no chimneys, small front gardens with low hedges along a car-free pedestrian path, pine trees and rocky ground, Farsta, autumn daylight, no people"),
    ("Radhusvägg med nya grå fasadskivor bredvid en tegelvägg och ett fönster",
     "close-up of the gable end of a 1960s Swedish terraced house clad with new flat grey fibre cement facade boards in a regular grid with visible joints, next to a red brick wall section and a window with a metal sill, no downpipe, no pipes, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HÄGERSTEN
"fasadrenovering-hagersten.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Hägersten", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Hägersten – småstugor i Hökmossen",
  "description": "Fasadrenovering i Hägersten: småstugorna i Hökmossen, panel med lockläkt, typritningar, isolering och fönster i fasadliv. Gratis platsbesök.",
  "h1": "Fasadrenovering i Hägersten",
  "lead": "Hökmossen i Hägersten är ett av Stockholms småstugeområden, med enkla trähus som står i grupper längs gatorna. Stadens strategi för småhusområden ger tydliga råd om hur sådana fasader ska behandlas vid renovering. Geal Entreprenad AB renoverar fasader i Hökmossen, Hägerstensåsen, Mälarhöjden och övriga Hägersten, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Småstugor, typritningar och panel.",
  "sections": [
    {"id": "hokmossen", "anchor": "Småstugorna i Hökmossen",
     "h2": "Hökmossen – ett av stadens småstugeområden",
     "paras": [
       "Strategin Varsam utveckling av småhus- och villaområden räknar Hökmossen till småstugeområdena, tillsammans med bland annat Tallkrogen, Norra Ängby och Enskedefältet. Bakgrunden var ett system för självbyggeri som utformades i början av 1920-talet för att familjer med låga inkomster skulle kunna bygga egna hem. Staden tog över projektet, organiserade byggandet och tog fram typritningar med utförliga bygginstruktioner.",
       "Rådet till skydd för Stockholms skönhet beskriver i ett yttrande från 2022 Hökmossen som ett småstugeområde enligt Stockholms byggnadsordning. Yttrandet gällde sex nya radhus vid Mejselvägen och Korpmossevägen, och rådet ansåg att de borde anpassas mer efter småstugorna än efter flerbostadshusen. Det säger något om hur staden ser på området: det är stugornas skala och utformning som ska styra.",
       "Vid en fasadrenovering är husets ursprungliga typ därför utgångspunkten. Det gäller även när stugan har byggts till mot trädgården, vilket strategin beskriver som det vanliga sättet att utöka småstugorna.",
     ],
     "aside": {"title": "Hökmossen", "items": [
       "Småstugeområde", "Hus efter typritningar",
       "Enhetliga husgrupper", "Tillbyggnader mot trädgården"]}},
    {"id": "panel-locklakt", "h2": "Stående panel med tunn lockläkt",
     "paras": [
       "Strategin beskriver småstugorna som enkla volymer, uteslutande i trä och med fönstren placerade i fasadliv. Fasadmaterialet var stående träpanel med tunn lockläkt, och taken var täckta med enkupigt eller tvåkupigt rött lertegel. I några områden förekommer även putsfasader. Färgsättningen var från början strikt reglerad till ett fåtal ljusa nyanser av grått, grönt och gult, och rödfärg fick användas efter särskild ansökan.",
       "Lockläktens dimension är en av de detaljer som syns mest. Byts panelen mot en lockpanel med grövre lock eller mot liggande panel förändras hela stugans uttryck, och eftersom husen står i grupper syns skillnaden längs gatan. Vi mäter därför befintlig panel och läkt innan nytt virke beställs, och byter bara de bräder som är skadade.",
       "Strategins vägledning för småstugeområden är att utgå från de ursprungliga husens volym, proportioner och takform vid renoveringar, och att ta tillvara eller återskapa karaktärsskapande material, kulörer, byggnadsdelar och detaljer så långt som möjligt. Om färgerna finns mer under " + _L.format("malare-hagersten.html", "målare i Hägersten") + ".",
     ],
     "aside": None},
    {"id": "isolering-fasadliv", "h2": "Isolering när fönstren sitter i fasadliv",
     "paras": [
       "På en småstuga sitter fönstren i samma liv som panelen. En utvändig tilläggsisolering gör väggen tjockare, och Boverket beskriver hur fönster och dörrar då hamnar längre in i fasaden, hur takfoten skjuter ut mindre och hur fasaden kan hänga ut över sockeln. Huset får lätt ett överjäst uttryck.",
       "Boverket visar också att det går att göra annorlunda. På vissa putsade funkishus har takfot, sockel och skärmtak byggts på samtidigt som fönster och dörrar flyttats ut, så att utseendet är oförvanskat. Invändig isolering lämnar fasaden orörd men gör väggens utsida kallare, och risken för röta och mögel i väggen ökar ju tjockare man isolerar.",
       "Enligt Boverket lönar det sig bäst att tilläggsisolera när fasaden ändå görs om, till exempel när panelen byts. Ska stugan få ny panel ser vi därför över om isoleringen bakom kan kompletteras utan att fönstren hamnar djupt i väggen. Om taket ska ses över samtidigt finns mer under " + _L.format("taklaggare-hagersten.html", "takläggare i Hägersten") + ".",
     ],
     "aside": {"title": "Före isoleringen", "items": [
       "Fönster i fasadliv", "Takfotens utsprång",
       "Sockelns bredd", "Torrt väder"]}},
    {"id": "typritningar-lov", "h2": "Typritningar, Hägerstensåsen och lovfrågan",
     "paras": [
       "Stadsbyggnadskontoret samlade i slutet av 1970-talet alla typritningar för småstugor från 1927 till 1957 i en sammanställning, så att den som ville ändra sin stuga skulle ha ett lättillgängligt underlag. Enligt strategin finns sammanställningen hos stadsbyggnadskontoret och på Stockholmskällan, och via bygglov.stockholm går det att beställa äldre miljöprogram och typritningssamlingar.",
       "Grannområdet Hägerstensåsen har en annan historia. Enligt Stadsmuseets skrift var åsen en skogsklädd bergsrygg före 1938. De första husen blev färdiga 1939 och de sista var inflyttningsklara 1948, och på den norra delen byggdes förutom smalhus och punkthus även villor. Där gäller alltså andra material och epoker.",
       "För en- och tvåbostadshus krävs inte längre bygglov för fasadändringar om vissa förutsättningar är uppfyllda. Lov behövs däremot i särskilt kulturhistoriskt värdefulla miljöer och där detaljplanen har skyddsbestämmelser, och Stadsmuseets klassificeringskarta ger en första indikation. Mer om panel och puts finns på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Hägersten till",
  "steps": [
    ("Typritningen", "Vi tar reda på vilken stugtyp huset byggdes efter och hur fasaden såg ut från början."),
    ("Platsbesök", "Panel, lockläkt, sockel och fönsteranslutningar gås igenom och mäts."),
    ("Isolering eller inte", "Vi bedömer om väggen kan isoleras utan att fönster och takfot får fel proportioner."),
    ("Skriftligt kostnadsförslag", "Panelbyte, isolering, bleck och målning redovisas som egna poster."),
    ("Utförande", "Ny panel med samma dimension monteras i torrt väder, med luftspalt bakom."),
    ("Genomgång", "Vi går runt stugan tillsammans när arbetet är klart."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Hägersten",
  "rot": [
    "Att byta och reparera fasader, tilläggsisolera och måla fasader räknas av Skatteverket som rotarbete i ett småhus. Även att montera och montera ner byggnadsställningar i samband med arbetet ger avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Hägersten?",
  "price": [
    "Hur mycket panel som är skadad, om lockläkten måste specialbeställas, om stugan ska isoleras och om fönstren då ska flyttas ut. En tillbyggnad mot trädgården gör fasadytan större. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Var hittar jag typritningen till min småstuga i Hökmossen?",
     "Stadsbyggnadskontoret sammanställde typritningarna för småstugor från 1927–1957 i slutet av 1970-talet. Enligt staden finns de hos stadsbyggnadskontoret och på Stockholmskällan."),
    ("Får jag byta till liggande panel på en småstuga i Hägersten?",
     "Stadens strategi råder att karaktärsskapande material tas tillvara eller återskapas. Småstugornas panel är stående med tunn lockläkt, och ett byte syns i hela husgruppen. Kontrollera också Stadsmuseets karta och detaljplanen."),
    ("Vilka kulörer fick småstugorna i Hökmossen ha från början?",
     "Enligt strategin var färgsättningen strikt reglerad till ett fåtal ljusa nyanser av grått, grönt och gult. Rödfärg fick användas efter särskild ansökan."),
    ("Kan en småstuga tilläggsisoleras utan att fönstren hamnar djupt i väggen?",
     "Ja, om fönstren flyttas ut och takfot och sockel anpassas samtidigt. Boverket beskriver exempel där utseendet har blivit oförvanskat på det sättet."),
    ("När byggdes husen på Hägerstensåsen?",
     "Enligt Stadsmuseet blev de första husen färdiga 1939 och de sista var inflyttningsklara 1948. Före 1938 var åsen en skogsklädd bergsrygg."),
  ],
  "sources": [
    _STH_VARSAM,
    ("Rådet till skydd för Stockholms skönhet – Kopplingsboxen 26, förslag till detaljplan, remissyttrande 2022 (pdf)",
     "https://skonhetsradet.stockholm/wp-content/uploads/sites/16/2022/02/Signerad-Kopplingsboxen-26-forslag-till-detaljplan-2020-08919652735-2_TMP.pdf"),
    ("Stockholmskällan / Stadsmuseet – Stockholms spår: Hägerstensåsen (pdf)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000088.pdf"),
    _STH_FASAD, _STH_KLASS, _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på stugan i Hägersten renoveras?", "Boka ett gratis platsbesök så går vi igenom panel, lockläkt och isolering och vad som passar stugtypen."),
  "img": [
    ("Småstuga i trä med ljus stående panel och rött tegeltak bakom en häck i Hägersten",
     "small 1930s Swedish timber cottage, one and a half storeys, light grey-green painted vertical board panel with thin cover battens, white window frames flush with the wall, steep red clay tile roof, a row of similar cottages behind hedges along a straight street, Hägersten Stockholm, autumn daylight, no people"),
    ("Ljusgrå stående träpanel med tunn lockläkt ovanför en putsad sockel",
     "close-up of light grey painted vertical wooden board panel with thin cover battens on a Swedish cottage, a few new primed boards and battens fitted near the concrete plinth, a window corner visible, daylight, no people, no hands"),
  ],
  "related": [],
},

}
