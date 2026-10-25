# -*- coding: utf-8 -*-
"""Snickare – ortsidor v10: Botkyrka, Enskede, Hässelby, Spånga, Upplands Väsby, Sigtuna (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25: Botkyrka kommun
(Kulturmiljöprogram antaget 2014: Västra stambanan, Tullinge station 1903, Uttran station 1908 och riktlinjer;
Bygglov A–Ö: Altan, Plank, Komplementbyggnad – uppdaterade juni 2026), Stockholms stad (Varsam utveckling av
småhus- och villaområden; bygglov.stockholm: Mur, plank, altan; Komplementbyggnad (bygglovsbefriad);
Tillbyggnad (bygglovsbefriad); Stadsmuseets kulturhistoriska klassificering; Fönster och dörrar; Häckar och
träd; Ändra i bärande konstruktion; Ny bostad i enbostadshus (bygglovsbefriad); Områdesfakta 2025 Hässelby
villastad, Solhem, Bromsten), Upplands Väsby kommun (Kunskapsunderlag för kulturmiljö: radhus och kedjehus
1960–70-tal, Oxundavägen; Altan; Mur och plank; Nybyggnad – komplementbyggnad; Kulturhistoriska byggnader,
kulturmiljöer), Sigtuna kommun (Bevarande- och förnyelseplan för Sigtuna stad 2019; Riktlinjer för
bebyggelseutveckling i dalgången mellan Odensala och Hova 2020; Staket, mur och plank; Bygga i kulturmiljö),
Boverket (Mur, plank, altan och annat; Bygga en ny byggnad; Ingrepp i husets bärande delar) och Skatteverket
(Ger arbetet rätt till rotavdrag?; Så fungerar rotavdraget).
Strukna (ej verifierade eller oklara i källan): Botkyrkas regel om staket med mer än 50 procent
genomsiktlighet och att carport alltid kräver bygglov (sidorna märkta "kan vara inaktuell" efter 1 dec 2025);
Sigtunas höjdgränser för plank på kommunens sida (omvända mot Boverket – Boverkets mått används);
Odensala–Hova-riktlinjens "i sammanhållen bebyggelse krävs bygglov även för tillbyggnader och
komplementbyggnader" (skriven 2020, oklart efter PBL-ändringen); Stockholms sida Inreda vinden ("bygglov för
ytterligare en bostad") som strider mot sidan Ny bostad i enbostadshus – bara den senare används; Varsams
vägledning om skärmtak/bod gäller typen storskalig stadsdel, inte Hässelbys tunnelbanestad – används inte för
Hässelby; om Hässelby strand/gård och Enskededalen är klassade eller ingår i riksintresset (inte kontrollerat);
områdesfakta för Gamla Enskede/Enskededalen (sidan saknades); rotavdragets femårsregel. Inga priser,
garantier, omdömen, egna uppdrag eller cert. Korslänkar via V4_MODULES i tjanster_v1.py.
Schema: se tools/tj_check.py."""

_BOV_MUR = ("Boverket – Mur, plank, altan och annat",
            "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/mur-plank-altan-och-annat/")
_BOV_NY = ("Boverket – Bygga en ny byggnad",
           "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/bygga-en-ny-byggnad/")
_BOV_BAR = ("Boverket – Ingrepp i husets bärande delar",
            "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/ingrepp-i-husets-barande-delar/")
_SKV = ("Skatteverket – Så fungerar rotavdraget",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV2 = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/"
_STH_MPA = ("Stockholms stad – Mur, plank, altan (bygglov.stockholm)", _SB + "bygga-nytt-och-bygga-till/mur-plank-altan/")
_STH_KOMP = ("Stockholms stad – Komplementbyggnad, bygglovsbefriad (bygglov.stockholm)",
             _SB + "bygga-nytt-och-bygga-till/komplementbyggnad-bygglovsbefriad/")
_STH_TILL = ("Stockholms stad – Tillbyggnad, bygglovsbefriad (bygglov.stockholm)",
             _SB + "bygga-nytt-och-bygga-till/tillbyggnad-bygglovsbefriad/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov.stockholm)",
              _SB + "bygga-nytt-och-bygga-till/stadsmuseets-kulturhistoriska-klassificering/")
_STH_FD = ("Stockholms stad – Fönster och dörrar (bygglov.stockholm)", _SB + "andra-byggnads-yttre-utseende/fonster-och-dorrar/")
_STH_HACK = ("Stockholms stad – Häckar och träd (bygglov.stockholm)", _SB + "andra-mark/hackar-och-trad/")
_STH_BAR = ("Stockholms stad – Ändra i bärande konstruktion (bygglov.stockholm)", _SB + "andra-inomhus/andra-i-barande-konstruktion/")
_STH_BOST = ("Stockholms stad – Ny bostad i enbostadshus, bygglovsbefriad (bygglov.stockholm)",
             _SB + "andra-inomhus/ny-bostad-i-enbostadshus-bygglovsbefriad/")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_BK = "https://botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/"
_UV = "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/"

_L = '<a class="text-link" href="{0}">{1}</a>'

_ROT_SUM = ("Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
            "tillsammans med rutavdrag. Material och resor ingår inte, och Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ BOTKYRKA
"snickare-botkyrka.html": {
  "kind": "district", "service": "snickare", "ort": "Botkyrka", "svc_label": "Snickare",
  "title": "Snickare i Botkyrka – altan, plank och förråd nära spåret",
  "description": "Snickare i Botkyrka: altan, plank och förråd i villaområdena längs Västra stambanan, 30-metersregeln vid spåret och hur höjden mäts.",
  "h1": "Snickare i Botkyrka",
  "lead": "Tumba, Rönninge, Tullinge och Uttran växte fram kring stationerna på Västra stambanan, och villaområdena ligger fortfarande längs järnvägen. För en altan, ett plank eller ett förråd kan avståndet till spåret avgöra om bygglov behövs. Geal Entreprenad AB bygger altaner, plank, förråd och carportar i hela Botkyrka, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Altan, plank och förråd i villaområdena vid järnvägen.",
  "sections": [
    {"id": "stambanan", "anchor": "Villorna längs järnvägen",
     "h2": "Villasamhällen som växte längs Västra stambanan",
     "paras": [
       "Botkyrkas kulturmiljöprogram beskriver utbyggnaden av Västra stambanan under tidigt 1860-tal som en av de faktorer som fick avgörande betydelse för kommunens utveckling. Längs linjen uppstod tidigt små stationssamhällen, till exempel i Tumba och Rönninge, och kring sekelskiftet 1900 växte mer renodlade villaområden fram längs järnvägssträckningen.",
       "Tullinge järnvägsstation öppnade 1903 och blev starten för villasamhället där. I Uttran började bebyggelsen när en ny station öppnade 1908. Programmet beskriver Uttran som en brokig blandning av stilar och volymer från drygt hundra års villabyggande, där de äldre delarna har svängda gator, bevarade naturpartier och stora tomter med husen placerade på höjdpartier.",
       "För snickeriet på tomten får det två följder. Marken är ofta kuperad, så en altan som är låg vid husväggen kan bli hög ute vid kanten. Och ligger tomten nära spåret kan ett bygge som annars är lovfritt ändå kräva bygglov eller ett skriftligt medgivande.",
     ],
     "aside": {"title": "Ur kulturmiljöprogrammet", "items": [
       "Stambanan byggs tidigt 1860-tal", "Tullinge station öppnar 1903",
       "Uttran station öppnar 1908", "Villor på höjdpartier"]}},
    {"id": "trettio-meter", "h2": "Trettio meter från spårets mitt",
     "paras": [
       "På sina sidor om altan, plank och komplementbyggnad räknar Botkyrka kommun upp när utökad lovplikt gäller. Första punkten är att åtgärden görs närmare än 30 meter från ett järnvägsspårs mitt. Då krävs bygglov även för sådant som annars är lovfritt på grund av sin begränsade storlek eller enkla utformning.",
       "Boverket anger för lovfria komplementbyggnader att de ska stå minst 30 meter från mitten av en järnväg, om inte infrastrukturförvaltaren har lämnat sitt skriftliga medgivande. Övriga punkter i kommunens lista är placering närmare en gräns än 4,5 meter utan grannarnas medgivande, åtgärder inom eller intill riksintresse för totalförsvaret och åtgärder vid byggnader eller i områden som är särskilt värdefulla från historisk, kulturhistorisk, miljömässig eller konstnärlig synpunkt.",
       "Vid platsbesöket mäter vi därför avståndet från den tänkta altanen eller boden till spårets mitt och till tomtgränsen innan något ritas. För kulturvärdena hänvisar kommunen till sin webbkarta, till detaljplanen och till översiktsplanen.",
     ],
     "aside": {"title": "Utökad lovplikt i Botkyrka", "items": [
       "Under 30 m från spårets mitt", "Under 4,5 m från gräns utan medgivande",
       "Nära riksintresse för totalförsvaret", "Särskilt värdefull miljö"]}},
    {"id": "altan-plank", "h2": "Altan och plank: så mäter kommunen höjden",
     "paras": [
       "Inom detaljplan krävs bygglov för en altan som är högre än 1,8 meter och ligger inom 3,6 meter från en byggnad, eller som är högre än 1,2 meter och ligger längre bort. Samma gränser gäller för plank. Kommunen mäter altanens höjd från markens lägsta nivå till ovansidan av altangolvet, och har marken ändrats i samband med bygget räknas höjden från den nya nivån.",
       "Ett vanligt räcke räknas inte in. Utformas altanräcket däremot som ett tätt plank ingår det i höjden. Kombineras ett plank med en mur mäts hela konstruktionen som en helhet, så två delar som var för sig ligger under gränsen kan tillsammans kräva lov.",
       "Kommunen påpekar också att altaner på tomten som sammanlagt är större än 50 kvadratmeter ska följa detaljplanen eller områdesbestämmelserna. En hög altan som byggs ihop med huset kan bedömas som en tillbyggnad, och en större fristående altan som en byggnad. Mer om altaner och trall finns på " + _L.format("snickare.html", "sidan om snickare") + ".",
     ],
     "aside": None},
    {"id": "forrad-carport", "h2": "Förråd och carport i villaträdgården",
     "paras": [
       "Kommunen nämner garage, carport, förråd, gäststuga, växthus och bastu som exempel på komplementbyggnader. Inom detaljplan krävs bygglov om byggnaden får en byggnadsarea över 30 kvadratmeter eller en taknock högre än 4,0 meter, eller om alla lovfria komplementbyggnader och komplementbostadshus på tomten tillsammans blir större än 45 kvadratmeter. Utanför detaljplan går gränserna vid 50 kvadratmeter, 4,5 meter och 65 kvadratmeter.",
       "Byggnaden måste vara fristående och mindre än huset den kompletterar. Inreds den som en självständig bostad räknas den i stället som komplementbostadshus.",
       "För Uttran säger kulturmiljöprogrammets riktlinjer att komplementbyggnader ska placeras så att gatubildens helhetsverkan med friliggande hus på uppvuxna trädgårdstomter bibehålls, och att höjd, volym och utförande ska underordnas huvudbyggnaden. Omfattande utfyllnader, stödmurar och hårdgjorda ytor ska undvikas. Ska villans tak ses över samtidigt finns mer under " + _L.format("takrenovering-botkyrka.html", "takrenovering i Botkyrka") + ".",
     ],
     "aside": {"title": "Lovfritt inom detaljplan", "items": [
       "Högst 30 m² byggnadsarea", "Sammanlagt högst 45 m²",
       "Taknock högst 4,0 m", "Mindre än huvudbyggnaden"]}},
  ],
  "steps_h2": "Så bygger vi altan eller förråd i Botkyrka",
  "steps": [
    ("Platsbesök", "Vi mäter marknivåer, avstånd till tomtgräns och, där det är aktuellt, avståndet till järnvägsspårets mitt."),
    ("Plan och karta", "Detaljplan, kulturmiljöprogram och tidigare lovfria byggnader på tomten gås igenom."),
    ("Skriftligt kostnadsförslag", "Grund, stomme, trall eller panel, räcken och trappor redovisas var för sig."),
    ("Medgivanden", "Behövs grannens eller infrastrukturförvaltarens skriftliga medgivande tar vi fram en ritning som underlag."),
    ("Bygget", "Plintar, stomme och beklädnad byggs enligt ritningen, med höjden kontrollerad mot gränserna."),
    ("Genomgång", "Vi går igenom resultatet med dig och lämnar mått och ritning att spara."),
  ],
  "rot_h2": "ROT-avdrag för snickeri i Botkyrka",
  "rot": [
    "Skatteverket ger rotavdrag för att bygga en altan till ett småhus om den byggs ihop med huset, och för att reparera entrétrappor, altaner och räcken. Att bygga en ny fristående byggnad, som ett garage eller en friggebod, ger inget avdrag, och inte heller att bygga staket och murar.",
    "En tillbyggnad av ett förråd, ett garage eller en carport kan däremot ge avdrag om någon av tillbyggnadens sidor sitter ihop med den befintliga byggnadens yttervägg till minst 75 procent, eller om det finns en dörr emellan. " + _ROT_SUM,
  ],
  "price_h2": "Vad styr kostnaden i Botkyrka?",
  "price": [
    "Altanens yta och höjd över marken, hur mycket tomten sluttar och om det behövs trappor och räcken väger tyngst. För en bod eller carport avgör grunden och taket mest. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Gäller 30-metersregeln vid järnvägen även för en altan i Tullinge?",
     "Ja. Botkyrka kommun räknar placering närmare än 30 meter från ett järnvägsspårs mitt som ett skäl för utökad lovplikt även för altaner och plank. Då krävs bygglov fast altanen annars hade varit lovfri."),
    ("Räknas räcket på altanen in i höjden i Botkyrka?",
     "Ett vanligt räcke gör det inte. Utformas räcket som ett tätt plank räknar kommunen in det i altanens höjd."),
    ("Hur stora altaner får vi ha i Botkyrka utan att följa detaljplanen?",
     "Enligt kommunen får lovfria altaner avvika från detaljplanen så länge den sammanlagda altanarean på tomten inte är större än 50 kvadratmeter."),
    ("Får förrådet bakom villan i Uttran vara lika stort som huset?",
     "Nej. Kommunen kräver bygglov om en komplementbyggnad får lika stor eller större byggnadsarea än huvudbyggnaden. Inom detaljplan går gränsen för lovfrihet dessutom vid 30 kvadratmeter."),
    ("Ger en carport som byggs mot villans vägg rotavdrag?",
     "Det beror på hur den ansluter. Skatteverket ger avdrag för en tillbyggnad om någon av dess sidor sitter ihop med den befintliga byggnadens yttervägg till minst 75 procent, eller om det finns en dörr emellan. En fristående carport ger inget avdrag."),
  ],
  "sources": [
    ("Botkyrka kommun – Kulturmiljöprogram, antaget 2014 (pdf)",
     "https://www.botkyrka.se/download/18.1fbbaae6170bff9469deb7f/1602575505534/Kulturmilj%C3%B6program.pdf"),
    ("Botkyrka kommun – Altan (Bygglov A–Ö)", _BK + "altan"),
    ("Botkyrka kommun – Plank (Bygglov A–Ö)", _BK + "plank"),
    ("Botkyrka kommun – Komplementbyggnad (Bygglov A–Ö)", _BK + "komplementbyggnad"),
    _BOV_NY, _SKV2, _SKV,
  ],
  "cta": ("Ska altanen eller förrådet byggas i Botkyrka?",
          "Boka ett gratis platsbesök så mäter vi höjder och avstånd och går igenom vad som gäller för tomten."),
  "img": [
    ("Ny trätrall i två nivåer vid en äldre villa på en kuperad tomt i Tullinge",
     "newly built wooden deck terrace in two levels with short wooden steps on a sloping rocky garden plot, attached to an early 1900s Swedish wooden villa painted pale yellow with white trim, pine and birch trees, granite outcrop, Tullinge Botkyrka suburb, summer afternoon, no people"),
    ("Fristående förråd i trä med stående panel under uppbyggnad i en villaträdgård",
     "small freestanding wooden garden shed under construction behind a Swedish villa, vertical board-and-batten cladding partly mounted on a light timber frame, concrete plinth foundation, stacked boards and sawhorses, mature apple tree, Botkyrka, overcast day, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ENSKEDE
"snickare-enskede.html": {
  "kind": "district", "service": "snickare", "ort": "Enskede", "svc_label": "Snickare",
  "title": "Snickare i Enskede – verandor, entréer och förråd",
  "description": "Snickare i Enskede: verandor och entrédörrar i Gamla Enskede, altan mot trädgårdssidan och varför en ny bod kräver bygglov i riksintresset.",
  "h1": "Snickare i Enskede",
  "lead": "I Gamla Enskede har många villor en veranda vid entrén, och trädgårdarna mellan husen är en del av helheten. Det påverkar både hur snickerierna lagas och var en ny altan eller bod kan stå. Geal Entreprenad AB arbetar med verandor, dörrar, altaner, förråd och inredningssnickeri i Gamla Enskede, Enskededalen och Enskede gård, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Verandor, entréer och bodar i trädgårdsstaden.",
  "sections": [
    {"id": "veranda", "anchor": "Verandan och entrén",
     "h2": "Verandan vid entrén i Gamla Enskede",
     "paras": [
       "Stockholms stads vägledning Varsam utveckling av småhus- och villaområden beskriver Gamla Enskede som stadens första trädgårdsstad. Villorna byggdes i nationalromantisk stil, och brant takfall, liggande panel och en veranda vid entrén är vanligt. Typritningar togs fram för ett enhetligt uttryck, och den mest kända är den så kallade Enskedestugan.",
       "Vägledningen räknar ursprungliga byggnadsdetaljer som fönster, entrédörrar och räcken till trädgårdsstadens karaktärsdrag. Fönstren sitter grunt i fasaden, är oftast två- eller treluftsfönster med stående proportioner och har i många fall småspröjsade rutor ovanför tvärposten. Rådet är att ta tillvara eller återskapa karaktärsskapande material, byggnadsdelar och detaljer så långt det går.",
       "För en snickare betyder det att en rötskadad verandastolpe, ett trappsteg eller en räckesdetalj i första hand lagas eller kopieras i samma profil. Ska en dörr eller ett fönster bytas listar staden ändringar som kan kräva bygglov: nytt material eller ny kulör, ändrad storlek, ändrade profiler på karmar, bågar och spröjsar, annan upphängning eller ny indelning.",
     ],
     "aside": {"title": "Detaljer att spara", "items": [
       "Verandans stolpar och räcken", "Entrédörren",
       "Småspröjsade fönster", "Gavelrösten"]}},
    {"id": "riksintresse", "h2": "En ny bod kräver bygglov i riksintresset",
     "paras": [
       "Gamla Enskede är, tillsammans med Ålstensgatan och Södra Ängby, utpekat som riksintresse för kulturmiljövården, enligt stadens vägledning. Stadsmuseets klassificeringskarta visar riksintressena med en blå ring, och staden skriver att du behöver söka bygglov för åtgärder som annars kan vara bygglovsbefriade om fastigheten ligger inom ett sådant område.",
       "Det gäller också det som byggs i trädgården. Stadens sida om lovfria komplementbyggnader påpekar att den utökade lovplikten gäller alla typer av komplementbyggnader, även sådana som tidigare kallades friggebod. På samma sätt kan en mur, ett plank eller en altan som är lovfri i andra stadsdelar kräva lov här.",
       "Utanför riksintresset avgör kartans färger och detaljplanen, och Stadsmuseet kan ge besked om enskilda fastigheter. Vi tar gärna fram måttsatta skisser som du kan bifoga en ansökan.",
     ],
     "aside": {"title": "Kan kräva lov i Gamla Enskede", "items": [
       "Bod eller förråd", "Plank och mur", "Altan", "Byte av dörr eller fönster"]}},
    {"id": "tradgardssidan", "h2": "Altan och terrass mot trädgårdssidan",
     "paras": [
       "Vägledningen beskriver trädgårdsstädernas öppna kvarter med vyer över trädgårdarna som ett viktigt karaktärsdrag. Tillbyggnader, takkupor, terrasser och andra mer påtagliga förändringar ska i första hand göras mot trädgårdssidan, och tillbyggnader mot gatan bör undvikas.",
       "Där ingen utökad lovplikt gäller krävs bygglov för en altan, en mur eller ett plank som är högre än 1,8 meter inom 3,6 meter från en byggnad, eller högre än 1,2 meter längre bort. Bygger du ett plank ovanpå altanen avgör den sammanlagda höjden, medan ett lovbefriat räcke inte räknas in. Får altanen tak eller väggar kan den i stället bli en tillbyggnad.",
       "Staden anger att när förutsättningarna för lovbefrielse inte är uppfyllda krävs bygglov för en mur eller altan som är högre än 0,5 meter och för ett plank högre än 1,1 meter, och att även lägre konstruktioner kan kräva lov om de bedöms påverka områdets karaktär. Läs mer om altaner och trall på " + _L.format("snickare.html", "sidan om snickare") + ".",
     ],
     "aside": None},
    {"id": "enskededalen", "h2": "Enskededalen och Enskede gård",
     "paras": [
       "I Enskededalen blev 1920-talets klassiska formspråk rådande, enligt vägledningen. Husen är enkla volymer i ett och ett halvt plan med symmetriska fasader, stående träpanel med tunn lockläkt och små takkupor mitt på långsidorna. Färgskalan gick i ljusa dämpade toner av grönt, gult eller grått.",
       "Vägledningen nämner att garage, carportar och förråd har byggts på tomterna i trädgårdsstäderna, och att det i Enskede gård också har skett förtätning inom den ursprungliga strukturen. Rådet är att utgå från de ursprungliga husens volym, proportioner och takform, även när det gäller komplementbyggnader.",
       "Vid platsbesöket tittar vi därför på panelens dimension och lockläktens bredd, så att en ny bod eller en lagad vägg passar huset. Ska taket ses över samtidigt finns mer under " + _L.format("takrenovering-enskede.html", "takrenovering i Enskede") + ", och för större utbyggnader under " + _L.format("tillbyggnad-enskede.html", "tillbyggnad i Enskede") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett snickeriarbete i Enskede till",
  "steps": [
    ("Platsbesök", "Vi tittar på veranda, dörrar, fönster och tomt och noterar profiler, panel och mått."),
    ("Kartan", "Fastigheten kontrolleras i Stadsmuseets klassificeringskarta och i detaljplanen."),
    ("Skriftligt kostnadsförslag", "Lagning, kopiering av detaljer och nya delar redovisas var för sig."),
    ("Underlag till lov", "Där lov behövs tar vi fram måttsatta skisser som du kan bifoga ansökan."),
    ("Snickeriet", "Det som kan lagas lagas, och nya delar tillverkas i samma profil som originalet."),
    ("Genomgång", "Vi går igenom arbetet tillsammans innan vi lämnar platsen."),
  ],
  "rot_h2": "ROT-avdrag för snickeri i Enskede",
  "rot": [
    "För en villa ger Skatteverket rotavdrag för att reparera och underhålla entrétrappor, balkonger och altaner med räcken, för att byta och reparera dörrar och för att bygga en altan som byggs ihop med huset. Att bygga ett nytt fristående förråd eller garage ger inget avdrag, och inte heller att bygga staket.",
    "Om material byts ska det nya vara likvärdigt med det gamla. " + _ROT_SUM,
  ],
  "price_h2": "Vad påverkar kostnaden i Enskede?",
  "price": [
    "Hur mycket av verandan eller entrén som kan sparas avgör mest: en lagning går fortare än en kopia av en svarvad stolpe eller en profilerad list. För en altan eller bod väger storlek, grund och eventuella lovhandlingar tyngst. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver en ny bod på tomten i Gamla Enskede bygglov?",
     "Ja, i regel. Gamla Enskede är riksintresse för kulturmiljövården, och Stockholms stad skriver att åtgärder som annars är lovfria då kräver bygglov. Det gäller alla typer av komplementbyggnader, även sådana som tidigare kallades friggebod."),
    ("Kan verandan på en Enskedevilla lagas i stället för att byggas om?",
     "Ofta. Stadens vägledning råder att ta tillvara eller återskapa ursprungliga detaljer som räcken och entrédörrar, och skadade delar kan bytas i samma profil medan resten sparas."),
    ("Var ska en ny altan placeras på en tomt i Enskede?",
     "Stadens vägledning för trädgårdsstäderna säger att terrasser och tillbyggnader i första hand ska placeras mot trädgårdssidan och inte mot gatan."),
    ("Behöver vi bygglov för att byta entrédörr på en villa i Gamla Enskede?",
     "Det kan krävas. Staden räknar bland annat byte av material, kulör, storlek och profiler på dörrar som ändringar som kan vara bygglovspliktiga, och i riksintresset krävs lov för åtgärder som annars är lovfria."),
    ("Hur skiljer sig husen i Enskededalen från dem i Gamla Enskede?",
     "Enskededalen byggdes i 1920-talets klassiska formspråk med enkla volymer, stående panel med tunn lockläkt och små takkupor. Gamla Enskede präglas av nationalromantik med branta tak och liggande panel."),
  ],
  "sources": [
    _VARSAM, _STH_KLASS, _STH_KOMP, _STH_MPA, _STH_FD, _SKV2, _SKV,
  ],
  "cta": ("Ska verandan, entrén eller boden i Enskede göras om?",
          "Boka ett gratis platsbesök så går vi igenom detaljerna, kartan och vad som behöver sökas."),
  "img": [
    ("Röd trävilla med vit veranda vid entrén i Gamla Enskede",
     "early 1900s Swedish national romantic wooden villa with horizontal panelling painted falu red, white window frames with small panes in the upper sash, steep red clay tile roof, small white wooden entrance veranda with turned posts and railing, garden with fruit trees and a clipped hedge, Gamla Enskede Stockholm, spring daylight, no people"),
    ("Ny svarvad verandastolpe och lagat trappsteg vid en äldre villa",
     "close-up of a repaired white painted wooden entrance porch on an old Swedish villa, one newly turned wooden post and a replaced step in fresh primed wood among the original weathered parts, carpentry tools on a cloth, garden behind, soft daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HÄSSELBY
"snickare-hasselby.html": {
  "kind": "district", "service": "snickare", "ort": "Hässelby", "svc_label": "Snickare",
  "title": "Snickare i Hässelby – altan, bod och plank på villatomten",
  "description": "Snickare i Hässelby: altan, bod och plank i villastaden och radhusområdena, grannemedgivande vid gränsen, skärmtak och ROT. Gratis platsbesök.",
  "h1": "Snickare i Hässelby",
  "lead": "I Hässelby villastad är nästan alla småhus äganderätter, och i stadens villastäder har tomter delats genom åren. Därför kan en ny altan, bod eller ett plank hamna nära en grannegräns som inte fanns när huset byggdes. Geal Entreprenad AB bygger altaner, förråd, plank, staket och skärmtak i Hässelby villastad, Hässelby gård och Hässelby strand, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Altan, bod och plank i villastaden och radhusen.",
  "sections": [
    {"id": "villastaden", "anchor": "Villastaden",
     "h2": "Villastad med tomter som delats",
     "paras": [
       "Stockholms stads områdesfakta för 2025 räknar 5 009 bostäder i småhus i stadsdelen Hässelby villastad. Av dem är 4 757 äganderätter och 204 bostadsrätter. För de flesta småhusägare här kan rotavdraget alltså gälla även arbete på husets utsida, till exempel en altan som byggs ihop med huset.",
       "Stadens vägledning Varsam utveckling av småhus- och villaområden räknar Hässelby villastad till typen villastad. Där är villorna fritt placerade på tomterna, en successiv delning av tomter har skett genom åren och bebyggelsen kommer från flera tidsepoker. Husen är som regel indragna från gatan med en grön förgård, och gatorna kantades av klippta häckar eller staket.",
       "När en tomt har delats kan grannens gräns ligga närmare huset än förr. Det spelar roll, eftersom det är avståndet 4,5 meter till gränsen som avgör om en bod eller ett högt plank kan byggas utan bygglov.",
     ],
     "aside": {"title": "Hässelby villastad 2025", "items": [
       "5 009 bostäder i småhus", "4 757 småhus med äganderätt",
       "204 småhus i bostadsrätt", "Successiv tomtdelning"]}},
    {"id": "grans", "h2": "Bod och plank nära grannens gräns",
     "paras": [
       "Enligt Stockholms stad ska en lovfri komplementbyggnad placeras 4,5 meter från gränsen mot granne, samfällighet eller allmän plats, och detsamma gäller murar och plank som är högre än 1,2 meter. Vill du bygga närmare behöver du skriftliga medgivanden från de berörda grannarna.",
       "Staden anger vad ett medgivande ska innehålla: fastighetsbeteckning, vilken typ av åtgärd det gäller, en situationsplan där åtgärden och avståndet till gränsen är inritade, och underskrifter från berörda grannar. Medgivandet bör kunna visas upp för byggnadsnämnden om ett tillsynsärende uppstår. Får du inget medgivande behöver du söka bygglov.",
       "Gränsar tomten mot en park eller gata är det oftast kommunen som är huvudman, och då behöver du stadens medgivande innan du bygger. Förfrågan skickas till stadsbyggnadskontoret.",
     ],
     "aside": {"title": "Medgivandet ska innehålla", "items": [
       "Fastighetsbeteckning", "Typ av åtgärd",
       "Situationsplan med avstånd", "Grannarnas underskrifter"]}},
    {"id": "altan-bod", "h2": "Altan och bod – mått att hålla",
     "paras": [
       "En komplementbyggnad, som ett förråd, en gäststuga, ett garage eller en bastu, kräver inte bygglov om den är högst 30 kvadratmeter byggnadsarea, mindre än huset den kompletterar och högst 4,0 meter till taknocken. Alla lovfria komplementbyggnader och komplementbostadshus på tomten får tillsammans vara högst 45 kvadratmeter, och där räknas tidigare friggebodar och attefallshus in.",
       "För altaner gäller samma höjdgränser som för plank och murar: högst 1,8 meter inom 3,6 meter från en byggnad och högst 1,2 meter längre bort. Lovfria altaner får avvika från detaljplanen så länge den totala ytan inte är större än 50 kvadratmeter. Byggs altanen in med väggar, även under golvet, kan den kräva bygglov som tillbyggnad.",
       "Stadens vägledning råder att tillbyggnader i villastaden i första hand orienteras mot trädgårdssidan. Ligger huset fritt med trädgården mot gatan kan en tillbyggnad mot gatan fungera, om gaturummet inte påverkas negativt. Mer om altaner och trall finns på " + _L.format("snickare.html", "sidan om snickare") + ".",
     ],
     "aside": None},
    {"id": "skarmtak", "h2": "Skärmtak och uterum vid radhusen",
     "paras": [
       "Hässelby strand och Hässelby gård räknas i stadens vägledning till de gruppbyggda småhusområdena i tunnelbanestaden. Rad- och kedjehusen ligger ofta på bryn och platåer, och nivåskillnaderna tas ofta upp med en suterrängvåning.",
       "Ett skärmtak över uteplatsen eller ett uterum räknas som tillbyggnad. Staden anger att en lovfri tillbyggnad får vara högst 30 kvadratmeter bruttoarea eller öppenarea och inte högre än husets taknock, och att tidigare friggebodsskärmtak, attefallstillbyggnader och attefallstakkupor räknas in i samma yta. Påverkar tillbyggnaden bärande konstruktion eller brandskydd krävs anmälan och startbesked.",
       "I ett radhus kan gränsen mot grannen gå direkt vid uteplatsen, och då behövs ett skriftligt medgivande för det som hamnar närmare än 4,5 meter. Är fastigheten kulturhistoriskt värdefull enligt Stadsmuseets karta krävs bygglov även för det som annars är lovfritt. Ska skärmtaket anslutas mot husets tak finns mer under " + _L.format("takrenovering-hasselby.html", "takrenovering i Hässelby") + ".",
     ],
     "aside": {"title": "Räknas in i 30 m² tillbyggnad", "items": [
       "Uterum", "Skärmtak", "Tidigare attefallstillbyggnad", "Attefallstakkupor"]}},
  ],
  "steps_h2": "Så bygger vi i Hässelby",
  "steps": [
    ("Platsbesök", "Vi mäter avstånd till alla gränser och ser vad som redan har byggts lovfritt på tomten."),
    ("Karta och plan", "Stadsmuseets karta och detaljplanen kontrolleras, liksom var gränserna går efter tidigare tomtdelningar."),
    ("Situationsplan", "Vi ritar in bod, altan eller plank med avstånd, så att grannarna har ett underlag att skriva under."),
    ("Skriftligt kostnadsförslag", "Grund, stomme, beklädnad och tak står som separata poster."),
    ("Bygget", "Bygget utförs efter ritningen, med höjder och avstånd kontrollerade."),
    ("Genomgång", "Vi går igenom arbetet med dig och lämnar situationsplanen att spara."),
  ],
  "rot_h2": "ROT i Hässelby – altan ja, fristående bod nej",
  "rot": [
    "Skatteverket ger rotavdrag för att bygga en altan till ett småhus om den byggs ihop med huset, och för att reparera altaner, entrétrappor och räcken. Ett helt nytt fristående förråd, en friggebod eller ett garage ger inget avdrag, och inte heller att bygga staket och murar.",
    "Bor du i ett radhus med bostadsrätt gäller avdraget bara arbete inne i bostaden, innanför väggar, tak och golv, och att bygga en altan ger då inget avdrag. " + _ROT_SUM,
  ],
  "price_h2": "Vad styr kostnaden i Hässelby?",
  "price": [
    "Altanens storlek och höjd, hur boden grundläggs och om planket ska stå på en mur påverkar mest. Behövs bygglov tillkommer handlingar och handläggningstid. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad ska ett grannemedgivande för en bod i Hässelby innehålla?",
     "Stockholms stad anger fastighetsbeteckning, vilken åtgärd det gäller, en situationsplan med åtgärden och avståndet till gränsen inritade samt underskrifter från berörda grannar."),
    ("Hur nära gatan får en bod i Hässelby villastad stå?",
     "Gränsen mot gata eller park räknas som gräns mot allmän plats, och en lovfri komplementbyggnad ska stå 4,5 meter därifrån. Närmare krävs stadens medgivande, eftersom kommunen oftast är huvudman."),
    ("Får vi bygga ett skärmtak över uteplatsen vid vårt radhus i Hässelby gård?",
     "Ett skärmtak räknas som tillbyggnad och kan vara lovfritt upp till 30 kvadratmeter tillsammans med tidigare lovfria tillbyggnader, om fastigheten inte är kulturhistoriskt värdefull. Närmare gränsen än 4,5 meter behövs grannens skriftliga medgivande."),
    ("Kan vi sätta ett plank vid utfarten mot gatan i Hässelby?",
     "Planket får inte skymma sikten för trafiken, vilket Boverket påpekar är särskilt viktigt vid hörntomter och utfarter. Stockholms stad anger att häckar där bör vara högst 70 centimeter, och ett plank över 1,2 meter ska stå 4,5 meter från gränsen om du inte har medgivande."),
    ("Ger en altan till ett radhus med bostadsrätt i Hässelby rotavdrag?",
     "Nej. Skatteverket ger inte rotavdrag för att bygga en altan till en bostadsrätt, eftersom avdraget där bara gäller arbete inne i bostaden."),
  ],
  "sources": [
    ("Stockholms stad – Områdesfakta Hässelby villastad (2025, pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-villastad.pdf"),
    _VARSAM, _STH_KOMP, _STH_MPA, _STH_TILL, _STH_HACK, _BOV_MUR, _SKV2, _SKV,
  ],
  "cta": ("Ska altanen, boden eller planket byggas i Hässelby?",
          "Boka ett gratis platsbesök så mäter vi avstånden och ritar en situationsplan för grannarna."),
  "img": [
    ("Ny låg trall och ett kort plank vid en villa i Hässelby villastad",
     "newly built low wooden deck with a short privacy screen of vertical boards behind a 1940s Swedish one-and-a-half storey wooden villa painted light grey, lawn, clipped hedge and fruit trees, neighbouring houses close by, Hässelby villastad Stockholm, late summer afternoon, no people"),
    ("Förråd i trä med pulpettak under uppbyggnad nära tomtgränsen",
     "small Swedish wooden storage shed with a single-pitch roof under construction near a garden boundary hedge, light timber frame, horizontal wooden cladding partly mounted, gravel and concrete plinths, folding ruler lying on a board, Stockholm suburb garden, overcast day, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SPÅNGA
"snickare-spanga.html": {
  "kind": "district", "service": "snickare", "ort": "Spånga", "svc_label": "Snickare",
  "title": "Snickare i Spånga – väggar, vind och verandor i villan",
  "description": "Snickare i Spånga: öppna en bärande vägg, inred vinden eller en ny bostad och laga glasverandan i villastäderna Solhem, Bromsten och Flysta.",
  "h1": "Snickare i Spånga",
  "lead": "Villastäderna i Spånga byggdes med individuellt utformade hus, de flesta i trä. När en vägg ska öppnas, vinden inredas eller en del av huset bli en egen bostad behövs både snickeri och rätt underlag till kommunen. Geal Entreprenad AB gör inredningssnickeri, väggar, trappor och verandor i Solhem, Bromsten, Flysta och Sundby, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Väggar, vindar och verandor i villastäderna.",
  "sections": [
    {"id": "villastaden", "anchor": "Villastäderna",
     "h2": "Stora tomter och individuella hus",
     "paras": [
       "Stockholms stads vägledning Varsam utveckling av småhus- och villaområden räknar Solhem, Bromsten, Flysta och Sundby till typen villastad. När järnvägen byggdes ut uppstod stationssamhällen utanför stadens dåvarande gränser, och på 1910-talet fick några av dem status som municipalsamhällen med egen administration och beskattningsrätt, till exempel Spånga.",
       "Villastäderna var privat organiserade, och bebyggelsen blev därför brokigare än i stadens egna egnahemsområden. Fritt liggande hus på tomter om 1 500–3 000 kvadratmeter blev karakteristiskt, och i Solhem fick bara en tiondel av tomten bebyggas. När nya planer togs fram på 1930-talet blev tomterna mindre, 700–1 000 kvadratmeter.",
       "Enligt stadens områdesfakta för 2025 finns 1 946 småhus med äganderätt i Solhem och 916 i Bromsten. I ett äldre hus av det slaget är det ofta väggarna, vinden och verandan som berörs när huset ska anpassas till ett nytt sätt att bo.",
     ],
     "aside": {"title": "Spånga i vägledningen", "items": [
       "Villastad, privat organiserad", "Tomter om 1 500–3 000 m²",
       "Solhem: en tiondel bebyggd", "1930-talet: 700–1 000 m²"]}},
    {"id": "barande", "h2": "Öppna en vägg mellan kök och vardagsrum",
     "paras": [
       "Boverket skriver att det inte krävs anmälan för att riva en vägg som inte är bärande, eller en vägg där man redan när huset byggdes förberedde för en öppning. Påverkas de bärande delarna väsentligt, till exempel en bärande innervägg, en balk, en pelare eller ett bjälklag, krävs en anmälan till byggnadsnämnden och ett startbesked innan arbetet börjar.",
       "Stockholms stad påpekar att du kan logga in med bank-id i Bygg- och plantjänsten och se ritningarna för fastigheten, men att ritningarna kan vara ofullständiga och att det inte är säkert att de som byggde följde dem. Staden kan inte bedöma om ändringen berör den bärande konstruktionen, utan hänvisar till en konstruktör.",
       "Därför öppnar vi gärna en liten inspektionslucka i tak eller vägg innan något rivs, så att konstruktören ser hur bjälkarna faktiskt ligger. Är väggen bärande dimensioneras en balk, och vi bygger in den och lagar väggar, tak och golv runt öppningen.",
     ],
     "aside": {"title": "Bärande delar enligt Boverket", "items": [
       "Bärande ytter- och innerväggar", "Balkar och pelare",
       "Bjälklag", "Takstolar och takbjälkar"]}},
    {"id": "vind-bostad", "h2": "Vind, trappa och en andra bostad",
     "paras": [
       "Stockholms stad skriver att du kan inreda ytterligare en bostad i ett enbostadshus utan bygglov, även om det inte följer detaljplanen, så länge huset eller området inte är särskilt kulturhistoriskt värdefullt. Ändras brandskydd eller bärande konstruktion, eller installeras vatten, avlopp eller en eldstad, krävs anmälan och startbesked. Fasadändringar i samband med den nya bostaden kräver inte heller bygglov under samma förutsättning.",
       "Att inreda vinden som en del av den egna bostaden handlar mer om bjälklag, trappa och väggar. Boverket nämner att ett takfönster som sätts mellan två takstolar, utan att någon av dem behöver kapas, normalt inte påverkar den bärande konstruktionen väsentligt.",
       "En trappa upp till vinden tar plats på planet under, och ett nytt hål i bjälklaget kan påverka bärigheten. Vi går igenom placeringen med dig och konstruktören innan bjälklaget öppnas, och bygger trappa, väggar och platsbyggda förvaringar när underlaget är klart.",
     ],
     "aside": None},
    {"id": "veranda", "h2": "Glasverandan och entrén",
     "paras": [
       "Vägledningen nämner glasverandor, takkupor och snickarglädje som det som gav villastäderna deras variation, och råder att karaktärsskapande material, kulörer, byggnadsdelar och detaljer tas tillvara eller återskapas vid ombyggnad och renovering.",
       "På en glasveranda är det de delar som tar emot vatten, som bottenstycken, fönsterbänkar och trappsteg, som brukar behöva lagas först. Vi lagar med nytt trä i samma profil, och där en del är för skadad tillverkar vi en kopia. Fler exempel på snickeri ute och inne finns på " + _L.format("snickare.html", "sidan om snickare") + ".",
       "Ska fönster eller dörrar i verandan bytas eller ändras kan det krävas bygglov, till exempel vid ändrad indelning, nya profiler eller annan upphängning. Är huset blå- eller grönmarkerat i Stadsmuseets karta krävs lov även för det som annars är lovfritt. Mer om färgen finns under " + _L.format("malare-spanga.html", "målare i Spånga") + " och om taket under " + _L.format("takrenovering-spanga.html", "takrenovering i Spånga") + ".",
     ],
     "aside": {"title": "Kan kräva bygglov", "items": [
       "Ny spröjsindelning", "Ändrade profiler",
       "Annan upphängning", "Större eller mindre öppning"]}},
  ],
  "steps_h2": "Så går ett snickeriuppdrag i Spånga till",
  "steps": [
    ("Platsbesök", "Vi tittar på väggar, bjälklag, vind och veranda och tar mått."),
    ("Ritningarna", "Vi går igenom ritningarna från Bygg- och plantjänsten med dig och jämför dem med huset."),
    ("Konstruktör vid behov", "Berörs bärande delar tar en konstruktör fram underlag till anmälan."),
    ("Skriftligt kostnadsförslag", "Rivning, stomme, ytskikt och lagningar redovisas var för sig."),
    ("Arbetet", "Vi börjar efter startbesked när sådant krävs och skyddar det som ska stå kvar."),
    ("Genomgång", "Vi går igenom resultatet och lämnar över det underlag som hör till anmälan."),
  ],
  "rot_h2": "ROT-avdrag för snickeri i Spånga",
  "rot": [
    "I ett småhus ger Skatteverket rotavdrag för att byta och reparera dörrar, för att montera platsbyggda fasta möbler som garderober och bokhyllor och för att reparera entrétrappor, altaner och räcken. Att montera fristående möbler ger inget avdrag.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset i Spånga?",
  "price": [
    "Om väggen är bärande avgör mest, eftersom en balk, en konstruktör och en anmälan då tillkommer. Vid vindsinredning väger bjälklaget och trappan tyngst. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Var hittar vi gamla ritningar på vår villa i Spånga?",
     "Stockholms stad har äldre handlingar för fastigheter i e-tjänsten Bygg- och plantjänsten, där du loggar in med bank-id. Staden påpekar att ritningarna kan vara ofullständiga."),
    ("Behöver vi anmäla att vi river en vägg i en villa i Solhem?",
     "Bara om de bärande delarna påverkas väsentligt. Då krävs anmälan och startbesked innan arbetet börjar. En vägg som inte är bärande kan rivas utan anmälan."),
    ("Kan vi inreda en egen lägenhet i vår villa i Bromsten utan bygglov?",
     "I ett enbostadshus går det att inreda ytterligare en bostad utan bygglov, om huset eller området inte är särskilt kulturhistoriskt värdefullt. Ändras bärande konstruktion eller brandskydd, eller installeras vatten och avlopp, krävs anmälan."),
    ("Hur stor del av tomten fick bebyggas i Solhem?",
     "Enligt stadens vägledning fick bara en tiondel av tomten bebyggas i Solhem, där tomterna var stora."),
    ("Ger platsbyggda garderober i vindsrummet rotavdrag?",
     "Ja, i ett småhus ger Skatteverket rotavdrag för att montera platsbyggda fasta möbler som garderober och bokhyllor. Fristående möbler ger inget avdrag."),
  ],
  "sources": [
    _VARSAM,
    ("Stockholms stad – Områdesfakta Solhem (2025, pdf)", _OF + "vasterort/jarva/solhem.pdf"),
    ("Stockholms stad – Områdesfakta Bromsten (2025, pdf)", _OF + "vasterort/jarva/bromsten.pdf"),
    _BOV_BAR, _STH_BAR, _STH_BOST, _STH_FD, _STH_KLASS, _SKV2, _SKV,
  ],
  "cta": ("Ska en vägg, vinden eller verandan i Spånga göras om?",
          "Boka ett gratis platsbesök så går vi igenom huset, ritningarna och vad som behöver anmälas."),
  "img": [
    ("Äldre trävilla med glasveranda och snickarglädje i Solhem",
     "early 1900s Swedish wooden villa painted pale green with white carved gingerbread trim, a two-storey glazed veranda with small-paned windows, steep red tile roof with a dormer, large garden with old apple trees and a lilac hedge, Solhem Spånga Stockholm, late spring daylight, no people"),
    ("Ny öppning med limträbalk mellan kök och vardagsrum i en äldre villa",
     "interior of an old Swedish wooden villa under renovation, a new wide opening in an interior wall between kitchen and living room with a new laminated timber beam installed above, temporary support posts, protected wooden floor, paper on the floor, daylight from windows, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"snickare-upplands-vasby.html": {
  "kind": "district", "service": "snickare", "ort": "Upplands Väsby", "svc_label": "Snickare",
  "title": "Snickare i Upplands Väsby – altan och plank i radhusområden",
  "description": "Snickare i Upplands Väsby: altan, plank och förråd i radhusområdena, ekdörrar längs Oxundavägen och kommunens mått för lovfritt bygge.",
  "h1": "Snickare i Upplands Väsby",
  "lead": "I flera delar av Upplands Väsby byggdes radhus, kedjehus och atriumhus i grupper på 1960- och 70-talen, ofta med små trädgårdar avgränsade av plank. När uteplatsen ska byggas om eller ett förråd byggas till gäller både kommunens mått och hänsynen till husgruppen. Geal Entreprenad AB bygger altaner, plank, förråd, carportar och entréer i hela kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Altan, plank och förråd vid radhus och kedjehus.",
  "sections": [
    {"id": "radhusen", "anchor": "Radhusområdena",
     "h2": "Plankomgärdade gårdar från 1960- och 70-talen",
     "paras": [
       "Kommunens Kunskapsunderlag för kulturmiljö i Upplands Väsby beskriver radhus- och kedjehusområdena från 1960- och 70-talen som enhetligt uppförda bebyggelsegrupper med låg höjdskala och platta eller flacka tak. Bostäderna har förgårdsmark och små trädgårdar eller atriumgårdar med uteplatser, ofta avgränsade av plank. Exempel finns i Sjukyrkoberget, Skälby, Fresta och Odenslunda och i centrala Apoteksskogen.",
       "Underlaget räknar små trädgårdar med uteplatser eller plankomgärdade gårdsrum med tydlig gräns mot allmänna ytor till områdenas karaktärsdrag, liksom enhetlig färgsättning och utformning av detaljer som balkongfronter och entrépartier inom varje bebyggelsegrupp. Vägledningen är att undvika tillbyggnader som bryter ursprungsvolymen och att inte hårdgöra ytor eller privatisera förgårdsmarken.",
       "För ett nytt plank eller en ny altan är det därför klokt att utgå från grannarnas. Samma höjd, samma bräddimension och samma kulör gör att längan fortsätter att se ut som en helhet, så vi tittar på resten av raden innan vi föreslår något.",
     ],
     "aside": {"title": "Karaktärsdrag i radhusområdena", "items": [
       "Plank runt uteplatsen", "Enhetliga entrépartier",
       "Kontrast mellan tegel och trä", "Grön förgårdsmark"]}},
    {"id": "matt", "h2": "Kommunens mått för altan, plank och staket",
     "paras": [
       "Upplands Väsby kommun skriver att en altan eller ett trädäck inom detaljplanerat område är lovfritt om det är lägre än 1,8 meter och ligger inom 3,6 meter från en byggnad, eller är högst 1,2 meter högt, och inte byggs på en byggnad eller i ett område som är kulturhistoriskt värdefullt. Ett räcke räknas bara in i höjden om det är tätt som ett plank.",
       "Detaljplanen kan ha prickmark där marken inte får bebyggas, men altaner får strida mot detaljplanen upp till 50 kvadratmeter. Utanför detaljplan krävs normalt inget lov för en altan, men kommunen påpekar att en altan som är högre än cirka 1,7 meter till altangolvet kan betraktas som en byggnad.",
       "För murar och plank gäller 1,8 meter inom 3,6 meter från byggnaden och 1,2 meter längre bort, och närmare tomtgränsen än 4,5 meter krävs grannens skriftliga medgivande. Kommunen beskriver ett staket som en inhägnad med en högsta höjd på 1,2 meter. En högre inhägnad räknas bara som staket om den går att se igenom från alla håll. Höjden räknas från befintlig marknivå där marken är som lägst.",
     ],
     "aside": {"title": "Lovfritt i Upplands Väsby", "items": [
       "Altan upp till 50 m² på prickmark", "Plank 1,8 m nära huset",
       "Staket högst 1,2 m", "Mät där marken är lägst"]}},
    {"id": "forrad", "h2": "Förråd och carport – en pott på 45 kvadratmeter",
     "paras": [
       "Kommunen räknar garage, carport och förråd som komplementbyggnader, och efter ändringarna i plan- och bygglagen används inte längre begreppen friggebod och attefallshus. Inom detaljplan får alla lovfria komplementbyggnader på tomten tillsammans vara högst 45 kvadratmeter, och den största högst 30. Utanför detaljplan är gränserna 65 och 50 kvadratmeter.",
       "Kommunen ger ett räkneexempel: har du tidigare byggt en friggebod på 15 kvadratmeter och ett attefallshus på 20 har du bara 10 kvadratmeter kvar att bygga lovfritt. Ett garage på 35 kvadratmeter kräver bygglov inom detaljplan även om potten inte är utnyttjad. Taknocken får vara högst 4,0 meter inom detaljplan, och byggnaden ska stå 4,5 meter från tomtgränsen om grannen inte har gett sitt skriftliga medgivande.",
       "Ska förrådet få vatten eller avlopp behöver du betala en VA-avgift, även om du kopplar på från den befintliga anslutningen på tomten. Mer om förråd och snickeri finns på " + _L.format("snickare.html", "sidan om snickare") + ".",
     ],
     "aside": None},
    {"id": "oxundavagen", "h2": "Ekdörrar och entrétrappor längs Oxundavägen",
     "paras": [
       "Oxundavägen bedöms i kunskapsunderlaget utgöra ett särskilt värdefullt bebyggelseområde enligt plan- och bygglagen. Längs Vinkelvägen har radhusen ytterdörrar av ek med spröjsat fönsterglas, omfattade av en vit putsad portik, och grusgångar leder fram till en entrétrappa med tre steg och ett enkelt smidesräcke. Längs Radhusvägen sitter ekdörrarna infällda i fasaden.",
       "Vägledningen för området är att respektera kvarterens entrélösningar med dörrar, fasadförskjutningar och trappor och att undvika nya fönster- och dörrupptagningar. Kommunen skriver att det krävs bygglov för mur, plank och komplementbyggnader inom ett kulturhistoriskt särskilt värdefullt område, även när de annars hade varit lovfria.",
       "En sliten ekdörr kan ofta slipas, oljas och få nya tätningslister i stället för att bytas. Mer om husen i området finns under " + _L.format("malare-upplands-vasby.html", "målare i Upplands Väsby") + " och " + _L.format("takrenovering-upplands-vasby.html", "takrenovering i Upplands Väsby") + ".",
     ],
     "aside": {"title": "Vinkelvägen och Radhusvägen", "items": [
       "Ekdörrar med spröjsat glas", "Vit putsad portik",
       "Trappa med tre steg", "Enkelt smidesräcke"]}},
  ],
  "steps_h2": "Så går ett snickeriuppdrag i Upplands Väsby till",
  "steps": [
    ("Platsbesök", "Vi mäter uteplats, marknivåer och avstånd till gränser och tittar på grannarnas plank och förråd."),
    ("Plan och underlag", "Detaljplanen, prickmarken och kunskapsunderlaget för kulturmiljö kontrolleras."),
    ("Potten räknas", "Tidigare friggebodar, attefallshus och förråd på tomten läggs ihop."),
    ("Skriftligt kostnadsförslag", "Trall, plank, förråd och dörrarbete redovisas som egna poster."),
    ("Bygget", "Vi bygger efter ritningen och följer grannarnas plank i höjd och linje där det passar."),
    ("Genomgång", "Vi går igenom resultatet tillsammans."),
  ],
  "rot_h2": "ROT-avdrag för snickeri i Upplands Väsby",
  "rot": [
    "Skatteverket ger rotavdrag för att bygga en altan till ett småhus om den byggs ihop med huset och för att byta och reparera dörrar och dörrlås. Att bygga ett fristående förråd eller garage ger inget avdrag, och inte heller att bygga staket och murar.",
    "Är radhuset en bostadsrätt ger varken altan eller byte av ytterdörr avdrag. Där gäller avdraget bara arbete inne i bostaden, som innerdörrar och insidan av ytterdörren. " + _ROT_SUM,
  ],
  "price_h2": "Vad styr kostnaden i Upplands Väsby?",
  "price": [
    "Uteplatsens storlek, om den gamla trallen och planket kan rivas utan att grunden behöver göras om och hur många meter plank som ska bytas påverkar mest. För ett förråd väger grund och tak tyngst. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får altanen ligga på prickmark i Upplands Väsby?",
     "Ja. Enligt kommunen får altaner strida mot detaljplanen upp till 50 kvadratmeter, vilket innebär att en sådan altan kan placeras på prickmark."),
    ("Hur högt får ett staket vara i Upplands Väsby utan att räknas som plank?",
     "Kommunen anger högst 1,2 meter. En högre inhägnad räknas bara som staket om den har hög genomsläpplighet, som ett smidesstaket eller ett trådnätstängsel."),
    ("Hur mycket förråd kan vi bygga lovfritt i Väsby om vi redan har en friggebod på 15 kvadratmeter?",
     "Inom detaljplan är potten 45 kvadratmeter, så 30 återstår, och ingen enskild byggnad får vara större än 30. Finns även ett attefallshus på 20 kvadratmeter återstår bara 10."),
    ("Kan vi byta ekdörren på vårt radhus vid Oxundavägen?",
     "Området bedöms som särskilt värdefullt, och kunskapsunderlaget råder att entrélösningarna med dörrar och trappor respekteras. Ofta går dörren att renovera. Fråga kommunen före ett byte, eftersom kraven på bygglov är högre i särskilt värdefulla områden."),
    ("Kostar det något att dra in vatten i förrådet i Upplands Väsby?",
     "Ja. Kommunen tar ut en VA-avgift om komplementbyggnaden får vatten eller avlopp, även om du kopplar på från den befintliga anslutningen på tomten."),
  ],
  "sources": [
    ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö i Upplands Väsby (pdf)",
     "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf"),
    ("Upplands Väsby kommun – Altan", _UV + "altan"),
    ("Upplands Väsby kommun – Mur och plank", _UV + "mur-och-plank"),
    ("Upplands Väsby kommun – Nybyggnad, komplementbyggnad", _UV + "nybyggnad---komplementbyggnad"),
    ("Upplands Väsby kommun – Kulturhistoriska byggnader, kulturmiljöer", _UV + "kulturhistoriska-byggnader-kulturmiljoer"),
    _SKV2, _SKV,
  ],
  "cta": ("Ska uteplatsen, planket eller förrådet göras om i Upplands Väsby?",
          "Boka ett gratis platsbesök så mäter vi upp och går igenom vad som gäller för tomten och husgruppen."),
  "img": [
    ("Radhus i tegel och trä med plankomgärdade uteplatser och ny trall i Upplands Väsby",
     "row of 1970s Swedish single-storey terraced houses with red brick and dark stained vertical timber cladding, flat roofs with deep fascia, small back gardens each enclosed by a wooden privacy fence, one with a newly built light wooden deck, birch trees, Upplands Väsby, summer afternoon, no people"),
    ("Oljad ekdörr med spröjsat glas och smidesräcke vid ett putsat radhus",
     "close-up of an oiled oak front door with a small-paned glass window set in a white rendered portico of a Swedish terraced house with earth-toned render, three steps with a simple black wrought iron railing, gravel path, daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SIGTUNA
"snickare-sigtuna.html": {
  "kind": "district", "service": "snickare", "ort": "Sigtuna", "svc_label": "Snickare",
  "title": "Snickare i Sigtuna – staket, dörrar och gårdshus",
  "description": "Snickare i Sigtuna: spjälstaket och plank i stadens gränder, dörrar och gårdshus i dalgången Odensala–Hova och reglerna för plank och mur.",
  "h1": "Snickare i Sigtuna",
  "lead": "I Sigtuna stad följer planken och spjälstaketen gränderna ner mot Mälaren, och i dalgången mellan Odensala och Hova står små uthus kvar från månghussystemets tid. Båda miljöerna har kommunala riktlinjer som berör snickerierna. Geal Entreprenad AB bygger och lagar staket, plank, dörrar, trappor och uthus i Sigtuna stad, Märsta och övriga kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Staket, dörrar och gårdshus i stad och dalgång.",
  "sections": [
    {"id": "granderna", "anchor": "Gränderna i Sigtuna stad",
     "h2": "Plank och spjälstaket som följer marken",
     "paras": [
       "Bevarande- och förnyelseplanen för Sigtuna stad, antagen 2019, beskriver gränderna som 2–4 meter breda och sluttande ner mot sjön. Byggnaderna är låga, putsade eller panelade, och ligger längs tomtgränserna eller indragna i trädgårdarna, som inhägnas av plank eller spjälstaket som följer markens lutning.",
       "För flera av stadens miljöer anger planen att inhägnader ska utföras som plank, häckar eller spjälstaket av traditionell typ. I gräns mot granne eller gata, där ingen byggnad markerar gränsen, uppförs staket eller plank av trä i traditionellt utförande, alternativt lövhäckar.",
       "Ett spjälstaket i sluttning byggs med stolparna i lod och spjälorna i jämn höjd över marken. Vi mäter upp lutningen före bygget och ser hur grannarnas staket är gjorda, så att det nya följer gränden på samma sätt.",
     ],
     "aside": {"title": "Inhägnader enligt planen", "items": [
       "Plank av trä", "Spjälstaket av traditionell typ",
       "Lövhäckar", "Följer markens lutning"]}},
    {"id": "aterbruk", "h2": "Spegeldörrar, trappräcken och återbruk",
     "paras": [
       "Planen visar spegeldörrar mot Stora gatan, en port i ett plank och snickarglädje på en veranda som exempel på detaljer i den äldre bebyggelsen. Utgångspunkten vid ombyggnad och renovering är att huset ska behålla det utseende det har, och byggnadsdetaljer som dörrar, dörr- och fönsteromfattningar och trapp- och balkongräcken bör tas tillvara och återanvändas i största möjliga utsträckning.",
       "Planen konstaterar också att byggnader med riktigt gammal träpanel är en sällsynthet som bör värnas, och att gamla panelbrädor ofta har olika bredder. Det bör behållas vid byte, eftersom en ny panel med exakta mått ger ett mer stereotypt intryck. Ett gammalt fönster bör i första hand repareras, till exempel genom att det dåliga bottenstycket byts ut.",
       "Det passar ett snickeri som lagar i stället för att byta: en ny nedre del på en spegeldörr, en ilagning i en dörromfattning eller en kopia av en trasig räckesdetalj. Mer om snickeriet finns på " + _L.format("snickare.html", "sidan om snickare") + " och om färgen på samma detaljer under " + _L.format("malare-sigtuna.html", "målare i Sigtuna") + ".",
     ],
     "aside": None},
    {"id": "odensala", "h2": "Dalgången mellan Odensala och Hova",
     "paras": [
       "Kommunens riktlinjer för bebyggelseutveckling i dalgången mellan Odensala och Hova antogs av bygg- och trafiknämnden i december 2020. De beskriver ett landskap där storskaliga moderna ekonomibyggnader står sida vid sida med ålderdomliga små uthus från månghussystemets tid, då det fanns ett hus för varje funktion på gården, som hönshus, vedbod och fäbod.",
       "För ombyggnader är rådet att förändra så lite som möjligt i de äldsta husen, att behålla de gamla gårdshusen och försöka finna användning för dem, och att låta trähus förbli trähus. En tillbyggnad görs helst på längden, så att gavelproportionerna och takvinkeln behålls.",
       "Riktlinjerna ger också råd om detaljer. En ytterdörr bör vara enkel och målad, utan onödiga och överdrivna detaljer, och ädelträ bör undvikas. Överljus, ett fönster ovanför dörren, är ett bra sätt att få ljus i hallen. Tomten behöver inte inhägnas, men vill man ha staket är ett enkelt rödfärgat trästaket lämpligt. Allt för låga staket är främmande på landsbygden, och ibland passar en gärdesgård i trä eller sten.",
     ],
     "aside": {"title": "Dörrar i dalgången", "items": [
       "Förr ofta dubbeldörrar", "Målade i gul ockra eller brun umbra",
       "Överljus från 1800-talet", "Undvik ädelträ"]}},
    {"id": "regler-sigtuna", "h2": "Regler för staket, plank och mur",
     "paras": [
       "Inom detaljplan krävs bygglov för ett plank eller en mur som är högre än 1,8 meter inom 3,6 meter från en byggnad, eller högre än 1,2 meter längre bort, enligt Boverket. Sigtuna kommun påpekar att lov också kan krävas om byggnaden eller området är särskilt kulturhistoriskt värdefullt, och att det finns många sådana områden i kommunen. För ett staket behövs oftast inget bygglov, men det beror på höjd, täthet, längd och utformning.",
       "Ska ett plank stå närmare grannens gräns än 4,5 meter behöver du ett skriftligt medgivande med en beskrivning av åtgärden, en situationsplan och underskrifter från alla berörda grannar. Mot gata eller park behövs kommunens medgivande, och närmare ett järnvägsspår än 30 meter krävs godkännande från infrastrukturförvaltaren. Även ett gammalt staket eller plank som är särskilt kulturhistoriskt värdefullt kan kräva lov för att rivas.",
       "Är du osäker på om huset ligger i ett kulturhistoriskt särskilt värdefullt område kan du skicka foton från samtliga väderstreck till kommunen, som återkommer med en bedömning. Om taken i samma miljöer finns mer under " + _L.format("takrenovering-sigtuna.html", "takrenovering i Sigtuna") + ".",
     ],
     "aside": {"title": "Inför ett nytt plank", "items": [
       "Kontrollera detaljplanen", "Grannens skriftliga medgivande",
       "30 m till järnvägsspår", "Foton till kommunen vid osäkerhet"]}},
  ],
  "steps_h2": "Så går ett snickeriuppdrag i Sigtuna till",
  "steps": [
    ("Platsbesök", "Vi tittar på staket, dörrar, trappor och uthus och mäter upp lutning och gränser."),
    ("Riktlinjerna", "Vi går igenom vad bevarandeplanen eller riktlinjerna för dalgången säger om fastigheten."),
    ("Skriftligt kostnadsförslag", "Lagning, kopior och nya delar redovisas var för sig."),
    ("Medgivanden och lov", "Vi tar fram situationsplan och beskrivning för grannemedgivande eller ansökan."),
    ("Snickeriet", "Gamla delar som kan sparas lagas, och nya tillverkas efter förlagan."),
    ("Genomgång", "Vi går igenom arbetet tillsammans när det är klart."),
  ],
  "rot_h2": "ROT-avdrag för snickeri i Sigtuna",
  "rot": [
    "I ett småhus ger Skatteverket rotavdrag för att byta och reparera dörrar, dörrlås och dörrhandtag och för att reparera entrétrappor med räcken. Om material byts ska det nya vara likvärdigt med det gamla. Att bygga eller reparera staket och murar ger inget avdrag, och inte heller att bygga en ny fristående byggnad.",
    "En tillbyggnad av ett förråd eller en gäststuga kan ge avdrag om någon av tillbyggnadens sidor sitter ihop med den befintliga byggnadens yttervägg till minst 75 procent, eller om det finns en dörr emellan. " + _ROT_SUM,
  ],
  "price_h2": "Vad styr kostnaden i Sigtuna?",
  "price": [
    "Hur mycket av det gamla som går att spara avgör mest. Ett spjälstaket i sluttning tar längre tid än ett på plan mark, och en kopia av en profilerad dörromfattning tar längre tid än en lagning. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken sorts staket passar i Sigtuna stads gränder?",
     "Bevarande- och förnyelseplanen anger plank, häckar eller spjälstaket av traditionell typ, och i gränderna följer inhägnaderna markens lutning."),
    ("Behöver vi bygglov för ett nytt staket vid huset i Sigtuna stad?",
     "Oftast inte för ett staket, men det beror på höjd, täthet, längd och utformning. För plank och murar kan lov krävas i kulturhistoriskt värdefulla områden, och kommunen skriver att det finns många sådana i Sigtuna."),
    ("Vilken ytterdörr rekommenderar kommunen i dalgången mellan Odensala och Hova?",
     "En enkel, målad dörr utan överdrivna detaljer. Riktlinjerna avråder från ädelträ och från långsmala sidofönster med färgat glas och lyfter fram överljus som ett bra sätt att få ljus i hallen."),
    ("Får vi riva det gamla uthuset på gården i Odensala?",
     "Riktlinjerna råder att behålla de gamla gårdshusen och finna användning för dem. Kommunen påpekar att rivning av en byggnad eller byggnadsdel kan kräva lov om miljön är särskilt värdefull."),
    ("Hur får vi veta om vårt hus i Sigtuna ligger i ett kulturhistoriskt värdefullt område?",
     "Skicka foton av fastigheten från samtliga väderstreck och en beskrivning av vad du vill göra via kommunens formulär, så återkommer kommunen med en bedömning."),
  ],
  "sources": [
    ("Sigtuna kommun – Bevarande- och förnyelseplan för Sigtuna stad, antagen 2019 (pdf)",
     "https://www.sigtuna.se/download/18.6ed4dd301706254f993282/1582201854957/Bevarande-%20och%20f%C3%B6rnyelseplan%20f%C3%B6r%20Sigtuna%20stad,%20antagen%202019.pdf"),
    ("Sigtuna kommun – Riktlinjer för bebyggelseutveckling i dalgången mellan Odensala och Hova (pdf)",
     "https://www.sigtuna.se/download/18.2b81151517d4919beb8c692e/1638798200988/Riktlinjer%20f%C3%B6r%20bebyggelseutveckling%20i%20dalg%C3%A5ngen%20mellan%20Odensala%20och%20Hova.pdf"),
    ("Sigtuna kommun – Staket, mur och plank",
     "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/staket-mur-och-plank.html"),
    ("Sigtuna kommun – Bygga i kulturmiljö",
     "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html"),
    _BOV_MUR, _SKV2, _SKV,
  ],
  "cta": ("Ska staketet, dörren eller uthuset i Sigtuna lagas?",
          "Boka ett gratis platsbesök så går vi igenom vad som kan sparas och vad riktlinjerna säger om fastigheten."),
  "img": [
    ("Rödfärgat spjälstaket som följer en sluttande gränd i Sigtuna stad",
     "narrow sloping lane in an old Swedish small town leading down towards a lake, low red and yellow painted wooden houses, traditional wooden picket fence painted falu red with white posts following the slope of the ground, lush gardens with lilacs and old trees behind the fence, Sigtuna, summer morning, no people"),
    ("Rödfärgat timrat uthus med målad dubbeldörr och överljus på en gård i Odensala",
     "old small timbered outbuilding painted falu red with a simple painted wooden double door in yellow ochre and a small transom window above, stone foundation, gravel farmyard, open fields and forest edge behind, Uppland countryside near Sigtuna, overcast day, no people, no text"),
  ],
  "related": [],
},

}
