# -*- coding: utf-8 -*-
"""Fasadrenovering – ortsidor v6: Danderyd, Ekerö, Tyresö, Enskede, Vallentuna, Österåker (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade 2026-10-25: Danderyds kommun (Riktlinjer för
kulturmiljöhistoriska byggnader och miljöer 2024; Kulturmiljöhandboken: Kvarteret Vale; Nya regler för
bygglov från 1 december 2025), Ekerö kommun (Kulturmiljöprogram 2015, Södra Färingsö/Stenhamra; Vad vill
du bygga?), Stockholms läns museum (Solberga/del av Raksta, rapport 2008:31) och Tyresö kommun (Förändringar
i PBL från 1 december 2025), Stadsmuseet via Stockholmskällan (Gamla Enskede byggnadsinventering 1974–1977;
Stockholms spår: Sockenplan) och Stockholms stad (bygglov.stockholm: Fasadändring, Stadsmuseets
kulturhistoriska klassificering), Vallentuna kommun (Fasadändring; Bygglovsarkivet; Översiktsplan 2040),
Österåkers kommun (Ljusterö planprogram 2010), Boverket (PBL kunskapsbanken: fasadändring; energiguiden:
tilläggsisolera fasaden; fuktrisker med fasadmaterial och ytskikt; risker med enstegstätning) och
Skatteverket (rotavdrag).
Strukna (ej verifierade): fasadmaterial på funkisvillorna i Klingsta/Stocksund och på Ramundvägens villor
(källorna anger inte material), att Vallentunas öppna landskap ger mer slagregn än andra orter, krav på
tillstånd från länsstyrelsen för byggnadsminnet Marum, asbest i Tyresös fritidshus, uppgifter om
grundläggning per område. Inga priser, garantier, omdömen, egna uppdrag eller cert. Schema: se
tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_FASAD = ("Boverket – PBL kunskapsbanken: Bygglov för fasadändring",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_BV_ISOL = ("Boverket – Energiguiden: Tilläggsisolera fasaden",
            "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/tillaggsisolera-fasaden/")
_BV_FMAT = ("Boverket – Fuktrisker med fasadens material och ytskikt",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/")
_BV_ENST = ("Boverket – Risker med enstegstätning",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/risker-enstegstatning/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_STH_FASAD = ("Stockholms stad – Fasadändring (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ DANDERYD
"fasadrenovering-danderyd.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Danderyd", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Danderyd – panel, grund och q-skydd",
  "description": "Fasadrenovering i Danderyd: panel på förvandring, grunder av huggen sten och fasadmaterial i områden med q-bestämmelse. Gratis platsbesök.",
  "h1": "Fasadrenovering i Danderyd",
  "lead": "I Djursholm finns bebyggelse från 1890-talet till 1970-talet, och kommunen vill att alla de årsringarna ska gå att läsa även i framtiden. För en fasadrenovering betyder det att materialet på väggen ofta väger lika tungt som kulören. Geal Entreprenad AB renoverar fasader i Djursholm, Stocksund, Enebyberg och övriga Danderyd, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villastäder, egnahem och grupphus i Danderyd.",
  "sections": [
    {"id": "arsringar", "anchor": "Danderyds årsringar",
     "h2": "Fasadmaterialet räknas till det som ska bevaras",
     "paras": [
       "I kommunens riktlinjer för kulturmiljöhistoriska byggnader och miljöer från 2024 återkommer samma formulering för område efter område: bebyggelsen bör behålla sin utformning mot gatan när det gäller husens placering på tomten, volymverkan och fasadmaterial. Det gäller bland annat funktionalismen i Klingsta, egnahemmen i Klingsta och Enebyberg, de tidiga villastäderna Ekeby och Svalnäs i Djursholm och 1940- och 50-talens bebyggelse i Söderskogen.",
       "Riktlinjerna säger också att byggnadernas ursprungliga arkitektoniska uttryck ska vara vägledande vid om- och tillbyggnad, och att fönster och portar i originalutförande ska värnas. För det moderna Danderyd skriver kommunen att främmande fasaduttryck som inte tillhör periodens stilideal bör undvikas.",
       "Ett byte från puts till panel, eller från en smal profil till en bred, är alltså inte en neutral åtgärd i Danderyd även om själva arbetet är rutin. Vi börjar därför med att ta reda på vilket område huset ligger i och vad som står om just det området.",
     ],
     "aside": {"title": "Ta reda på först", "items": [
       "Ligger huset i kulturmiljökartan?", "Finns q-bestämmelse i detaljplanen?",
       "Vilken årsring hör huset till?", "Vilket fasadmaterial var det från början?"]}},
    {"id": "vale", "h2": "Kvarteret Vale: gul panel på förvandring och huggen sten",
     "paras": [
       "Kulturmiljöhandboken beskriver kvarteret Vale norr om Danderydsvägen som ett exempel på hur fasaden blir en del av skyddet. Köpingen lät 1907 uppföra fyra tvåfamiljshus och två enfamiljshus där för den arbetskraft som behövdes i Djursholm. Husen är enkla trävillor i en och en halv våning med drag av nationalromantik och jugend, och handboken anger materialen punkt för punkt: panel på förvandring, traditionell färgsättning med gul oljefärg, grunder av huggen natursten och tak av tvåkupigt rött lertegel.",
       "Detaljplanen för Vale är från 1985 och alla byggnader omfattas av en q-bestämmelse. När en fasad är beskriven så noga är det rimligt att arbeta på samma sätt: byta skadade brädor mot virke med samma dimension och profil, behålla förvandringen där den håller och se till att panelen slutar på samma avstånd från stengrunden som tidigare.",
       "Samma tänkesätt fungerar i många av Djursholms äldre villor, även där inget q står i planen. Handboken uppmanar till att underhålla varsamt med traditionella material och metoder, och att försöka rätta till olämpliga förändringar som gjorts under senare tid.",
     ],
     "aside": None},
    {"id": "fukt-danderyd", "h2": "Där trä möter sten och fönster",
     "paras": [
       "Boverket beskriver fasadens viktigaste uppgift som att hindra nederbörd från att tränga in i byggnaden. De känsliga punkterna är anslutningarna: mot fönster och dörrar, vid infästningar av stuprör och där olika byggdelar möts. Där behövs enligt Boverket tätning i mer än en nivå, så kallad tvåstegstätning, för att vatten som kommer förbi det yttre skiktet ska kunna rinna ut igen.",
       "På en villa med stengrund och träpanel sitter skadorna därför ofta längst ner, där regnstänk från marken når brädornas ändträ, och under fönsterbleck som har för litet fall. Vid besöket petar vi i panelen med en syl i de lägena och tittar på hur blecken är vinklade. Fönster i originalutförande renoveras hellre än byts, i linje med riktlinjerna, och det kan " + _L.format("malare-danderyd.html", "målare i Danderyd") + " hjälpa till med.",
       "Boverket varnar också för att täta plastfärger på träpanel har gett fuktskador när rätt grundfärg saknats. När vi lagar panel stämmer vi därför av vilken färgtyp som finns på huset innan nytt virke grundas.",
     ],
     "aside": {"title": "Vanliga skadeställen", "items": [
       "Nedersta brädorna mot grunden", "Under fönsterbleck",
       "Kring stuprörens fästen", "Hörnbrädor och vattbrädor"]}},
    {"id": "lov-danderyd", "h2": "Lovfritt för de flesta – men inte i värdefulla områden",
     "paras": [
       "Från den 1 december 2025 gäller att det normalt inte behövs bygglov för att byta kulör eller fasadmaterial på ett en- eller tvåbostadshus. Boverket skriver att det inte heller krävs lov för andra ändringar som påverkar husets karaktärsdrag. Undantaget är utökad lovplikt, bland annat för byggnader som omfattas av skyddsbestämmelser i detaljplan och för särskilt värdefulla byggnader och områden.",
       "Danderyds kommun skriver att bygglov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område, om byggnaden i sig är särskilt värdefull eller om den ligger inom riksintresse för kulturmiljövården. Om fastigheten berörs syns i kommunens kulturmiljökarta, och kommunen erbjuder rådgivning. Den som vill ha ett formellt besked kan söka frivilligt bygglov även för en lovfri åtgärd.",
       "Även utan lov gäller varsamhetskravet. Ett byte av panelprofil eller en utvändig tilläggsisolering på ett hus i ett utpekat område bör därför stämmas av med kommunen innan material beställs.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Danderyd till",
  "steps": [
    ("Kartan först", "Vi tittar i kulturmiljökartan och detaljplanen så att vi vet vilket område och vilka bestämmelser huset omfattas av."),
    ("Besök runt huset", "Panel, förvandring, grund, fönsteranslutningar och bleck kontrolleras, och vi tar mått på befintliga profiler."),
    ("Kostnadsförslag", "Lagning, byte och eventuell isolering prissätts var för sig i ett skriftligt förslag."),
    ("Kontakt med kommunen", "Om huset ligger i ett värdefullt område stämmer vi av lovfrågan innan arbetet planeras."),
    ("Utförande", "Skadat virke byts mot samma dimension, anslutningar och bleck görs om och fasaden förbereds för målning."),
    ("Genomgång", "Vi går runt huset tillsammans och visar vad som har bytts och varför."),
  ],
  "rot_h2": "ROT-avdrag för fasadarbete i Danderyd",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att byta och reparera fasader, tilläggsisolera, måla fasader och reparera eller byta fönster. Även byggnadsställningar som monteras och tas ner i samband med rotarbetet ger avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material, resor och maskiner ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Danderyd?",
  "price": [
    "Hur mycket panel som behöver bytas, om profilen måste specialbeställas för att stämma med den gamla, skicket på förvandring och vattbrädor och hur många fönsteranslutningar som ska göras om. Stora tomter med uppvuxna träd påverkar hur ställningen kan stå. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Får vi byta till en bredare panel på vår villa i Djursholm?",
     "Det beror på var huset ligger. Kommunens riktlinjer säger att fasadmaterialet mot gatan bör bibehållas i flera utpekade områden. Ligger huset i ett kulturhistoriskt särskilt värdefullt område krävs bygglov för fasadändringen. Annars är bytet normalt lovfritt, men varsamhetskravet gäller ändå."),
    ("Vad betyder panel på förvandring?",
     "Att panelen är spikad på liggande reglar som sitter på stommen, i stället för direkt på väggen. Förvandringen ger ett utrymme bakom panelen. Den beskrivs till exempel för husen i kvarteret Vale, och vi kontrollerar den när panel byts."),
    ("Hur vet jag om mitt hus i Danderyd har en q-bestämmelse?",
     "Den står i detaljplanen för fastigheten. Kulturmiljökartan visar om huset ligger i ett kulturhistoriskt värdefullt område, och kommunen ger rådgivning om du är osäker."),
    ("Kan ni laga panelen nere vid stengrunden utan att byta hela väggen?",
     "Ofta ja. De nedersta brädorna tar mest vatten och kan bytas och skarvas in. Vi ser samtidigt till att avståndet mellan panel och grund blir tillräckligt."),
    ("Ska fasadfärgen bytas när panelen lagas?",
     "Inte nödvändigtvis. Vi tar reda på vilken färgtyp som finns och grundar det nya virket så att det fungerar med den. Ett byte av färgtyp kan dessutom påverka husets karaktärsdrag."),
  ],
  "sources": [
    ("Danderyds kommun – Riktlinjer för kulturmiljöhistoriska byggnader och miljöer i Danderyd (2024, pdf)",
     "https://www.danderyd.se/globalassets/globala-filer/kommun-och-politik/ovriga-styrdokument-ny/styrande-dokument---samhallsbyggnad-miljo-och-exploatering/riktlinjer-for-kulturmiljohistoriska-byggnader-och-miljoer-i-danderyd-2024.pdf"),
    ("Danderyds kommun – Kulturmiljöhandboken: Kvarteret Vale (pdf)",
     "https://sync.danderyd.se/globalassets/globala-filer/bygga-bo-och-miljo/bygglov/kulturmiljohandboken/b19-kvarteret-vale.pdf"),
    ("Danderyds kommun – Nya regler för bygglov från 1 december 2025",
     "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/"),
    _BV_FASAD, _BV_FMAT, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på villan i Danderyd ses över?", "Boka ett gratis platsbesök så går vi igenom panel, grund och fönsteranslutningar tillsammans."),
  "img": [
    ("Gulmålad trävilla med vita knutar på stengrund bland lövträd i Djursholm",
     "early 1900s Swedish one-and-a-half storey wooden villa with horizontal and vertical panelling painted ochre yellow with linseed oil paint, white window frames and corner boards, foundation of large hewn granite blocks, steep red two-curved clay tile roof, lawn and large deciduous trees, Djursholm Danderyd, soft daylight, no people, no text"),
    ("Nedre delen av en gulmålad träfasad mot en grund av huggen granit",
     "close-up of the bottom of a yellow painted wooden facade on an old Swedish villa where the lowest boards end a few centimetres above a hewn grey granite foundation, a metal drip flashing between wood and stone, a few new primed boards spliced in among older painted ones, daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ EKERÖ
"fasadrenovering-ekero.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Ekerö", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Ekerö – Stenhamra, egnahem och 60-tal",
  "description": "Fasadrenovering i Ekerö: egnahem kring Stenhuggarbyn, 1960- och 70-talsvillor i Stenhamra och fönsteranslutningar när väggen isoleras. Gratis platsbesök.",
  "h1": "Fasadrenovering i Ekerö",
  "lead": "På Mälaröarna står villor från förra sekelskiftet sida vid sida med hus från 1960- och 1970-talen. Fasaderna har åldrats på olika sätt och behöver olika slags omsorg. Geal Entreprenad AB renoverar fasader i Ekerö, Stenhamra och på öarna runt omkring, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Egnahem, villaområden och äldre gårdar i Ekerö.",
  "sections": [
    {"id": "stenhamra", "anchor": "Stenhamra",
     "h2": "Stenhamra växte ur ett granitbrott",
     "paras": [
       "Ekerö kommuns kulturmiljöprogram från 2015 berättar att Stenhamra på Färingsös sydvästra sida etablerades 1884, när stenbrottet grundades. Stockholms stad köpte granitberget för att säkra tillgången på framför allt gatsten. Intill brottet byggdes Stenhuggarbyn med bostäder för arbetarna och en skola, och några av arbetarlängorna flyttades dit 1889 från stadens gamla stenbrott i Huvudsta. Brottet lades ned 1937.",
       "Under det tidiga 1900-talet började arbetarna bygga egna hem utanför byn. Programmet skriver att de villorna finns kvar men har förändrats och byggts om under årens lopp. I dag domineras Stenhamra av villor från andra halvan av 1900-talet, med många enfamiljshus från 1960- och 1970-talen.",
       "För en fasadrenovering ger det två helt olika utgångslägen i samma tätort: äldre egnahem där flera lager av ombyggnader kan ligga ovanpå varandra, och yngre villor där det ursprungliga utförandet ofta är bättre bevarat men där material och detaljer har nått en ålder då de behöver förnyas.",
     ],
     "aside": {"title": "Fasaderna i Stenhamra", "items": [
       "Stenhuggarbyn: arbetarlängor runt 1900", "Egnahem från tidigt 1900-tal",
       "Villor från 1960- och 70-talen", "Ramundvägen: modernistiskt villaområde"]}},
    {"id": "egnahem-ekero", "h2": "Egnahemmen: leta efter det ursprungliga under senare lager",
     "paras": [
       "När ett hus har byggts om i flera omgångar är det inte säkert att den panel som syns i dag är husets första. Ibland sitter en senare beklädnad direkt på en äldre, ibland har panelen bytts helt. Innan vi föreslår lagning eller byte tar vi därför loss en bräda eller en knutbräda på ett ställe där det inte syns och tittar på vad som finns bakom: äldre panel, vindskydd, luftspalt eller ingenting alls.",
       "Det avgör vad som är rimligt. Finns en hel och torr äldre panel under kan den ibland tas fram igen. Är väggen fuktskadad måste orsaken hittas först; Boverket påpekar att mögel eller röta ska åtgärdas innan någon tilläggsisolering påbörjas. Programmets råd för Stenhamra är att villabebyggelsens gestaltning, skala och färgsättning från 1900-talet bör respekteras, och det är en bra måttstock även för det som inte syns från gatan.",
     ],
     "aside": None},
    {"id": "ramundvagen", "h2": "1960- och 70-talsvillor och Ramundvägen",
     "paras": [
       "Kulturmiljöprogrammet lyfter fram det enhetliga villaområdet längs Ramundvägen som ett av de bästa exemplen på modernistisk arkitektur på Mälaröarna och skriver att det har mycket höga arkitektoniska värden. Programmet föreslår att villorna förses med ytterligare skyddsbestämmelser i detaljplan, och att tillbyggnader i enhetliga villaområden utformas så att områdets karaktär består.",
       "I ett enhetligt område märks avvikelser tydligt. Byter ett hus panelriktning, fönstersättning eller sockelhöjd bryts mönstret längs gatan. Vid en renovering av en villa från den här tiden försöker vi därför behålla indelningen i fasaden och de smala detaljerna kring fönstren, även när själva materialet förnyas.",
       "Är taket på väg att bli lika gammalt som fasaden kan det löna sig att planera båda medan ställningen står. Läs mer under " + _L.format("taklaggare-ekero.html", "takläggare i Ekerö") + ".",
     ],
     "aside": {"title": "Behåll i ett enhetligt område", "items": [
       "Panelens riktning och indelning", "Fönstrens placering och storlek",
       "Sockelns höjd", "Takfotens utsprång"]}},
    {"id": "fonster-ekero", "h2": "Tjockare vägg, större fönster och kommunens krav",
     "paras": [
       "Boverkets energiguide beskriver utvändig tilläggsisolering som ofta bäst för både energi och fukt, men varnar för att fönster och dörrar hamnar längre in i fasaden, att takfoten inte skjuter ut lika mycket och att väggen kan hänga ut över sockeln. Fönster kan behöva flyttas ut, och sockel och takfot byggas på, för att huset ska behålla sina proportioner.",
       "Ekerö kommun skriver att det inte krävs bygglov för fasadändring på ett en- eller tvåbostadshus, utom när fastigheten ligger i ett område som bedömts som särskilt värdefullt. Kommunen påpekar också att en ändring som väsentligt påverkar bärande konstruktion, till exempel nya reglar för ett större fönster, kräver anmälan. Är du osäker kan du mejla ett foto på huset till kommunen och beskriva ändringen, så bedömer de om lov behövs.",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången vid en fasadrenovering i Ekerö",
  "steps": [
    ("Platsbesök", "Vi går runt huset, öppnar panelen på ett undanskymt ställe och ser vad som finns bakom."),
    ("Lov och anmälan", "Vi kontrollerar om huset ligger i ett särskilt värdefullt område och om fönsterändringar kräver anmälan."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där panel, isolering, fönsteranslutningar och bleck står var för sig."),
    ("Ställning och skydd", "Ställningen anpassas efter tomten och fönster och växter skyddas."),
    ("Panel och anslutningar", "Ny eller lagad panel monteras med luftspalt, och anslutningar mot fönster och sockel görs om."),
    ("Avslutning", "Fasaden förbereds för målning och vi går igenom arbetet med dig på plats."),
  ],
  "rot_h2": "Rotavdrag för fasadrenovering i Ekerö",
  "rot": [
    "Att byta och reparera fasader, tilläggsisolera och montera byggnadsställningar i samband med rotarbete ger rotavdrag i ett småhus. Det gäller även ett fritidshus som du äger och använder.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här styr priset i Ekerö",
  "price": [
    "Vad som finns bakom den panel som syns i dag, hur mycket av väggen som är skadad, om fönster ska flyttas ut vid en tilläggsisolering och om sockel och takfot behöver byggas på. Avståndet till tomten och möjligheten att ställa upp ställning påverkar också. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vi har ett gammalt egnahem i Stenhamra – går det att se om panelen är original?",
     "Det syns sällan utifrån. Vi tar loss en bräda på ett undanskymt ställe och ser om det sitter en äldre panel under, vilket vindskydd som finns och hur luftspalten ser ut."),
    ("Kan vi tilläggsisolera en 70-talsvilla i Stenhamra utan att den ser ombyggd ut?",
     "Ofta, om fönstren flyttas ut och sockel och takfot byggs på så att proportionerna behålls. Ligger huset i ett enhetligt område bör indelningen i fasaden också vara densamma efteråt."),
    ("Behöver jag göra en anmälan för ett större fönster i fasaden?",
     "Ekerö kommun skriver att en ändring som väsentligt påverkar bärande konstruktion, till exempel nya reglar för ett större fönster, kräver anmälan. Ligger huset i ett särskilt värdefullt område kan bygglov också krävas."),
    ("Hur får jag besked från Ekerö kommun om min fasadändring kräver lov?",
     "Kommunen tar emot ett foto på huset och en beskrivning av ändringen via e-post och bedömer sedan om bygglov behövs."),
    ("Gäller rotavdrag för fasaden på vårt fritidshus på Färingsö?",
     "Ja, om du äger huset och använder det som fritidsbostad gäller samma regler som för ett permanentboende småhus."),
  ],
  "sources": [
    ("Ekerö kommun – Kulturmiljöprogram 2015 (pdf)",
     "https://www.ekero.se/download/18.553838ea17305720c321ec82/1597925412772/Eker%C3%B6%20kulturmilj%C3%B6program.pdf"),
    ("Ekerö kommun – Vad vill du bygga?",
     "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/vad-vill-du-bygga"),
    _BV_FASAD, _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver fasaden på huset i Ekerö ses över?", "Boka ett gratis platsbesök så öppnar vi panelen och ser vad som finns bakom."),
  "img": [
    ("Enplansvilla från 1960-talet med brunbetsad träpanel i Stenhamra",
     "typical modest Swedish single-storey family house built in 1968, brown stained vertical wooden board-and-batten panelling, white painted wooden window frames with two-pane casement windows, low gable roof with dark brown concrete roof tiles, small brick chimney, short paved driveway with a carport, lawn with birch trees and a granite outcrop, suburban villa street in Stenhamra Ekerö, slightly weathered, late summer daylight, no people, no cars, no text"),
    ("Hörn av ett trähus där den yttre panelen tagits ner och en äldre panel syns under",
     "exterior corner of an old Swedish wooden house during facade renovation: on the left the wall still has light grey painted vertical board-and-batten cladding, on the right the outer cladding has been taken off so that older horizontal weathered wooden boards with traces of old red paint are exposed on the wall, the white corner board removed, a neat stack of removed grey boards lying on the grass, no ladder, daylight, no people, no hands, no tools, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TYRESÖ
"fasadrenovering-tyreso.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Tyresö", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Tyresö – timmerhus, locklist och grund",
  "description": "Fasadrenovering i Tyresö: locklistpanel på timmerhus, äldre panel kvar under isoleringen och putsade naturstensgrunder. Gratis platsbesök.",
  "h1": "Fasadrenovering i Tyresö",
  "lead": "Bakom den röda locklistpanelen på ett äldre hus i Tyresö sitter ofta en timmerstomme, och ibland ytterligare en panel från en tidigare renovering. Den som ska renovera fasaden behöver veta vad som finns i väggen innan något rivs. Geal Entreprenad AB renoverar fasader i hela Tyresö, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Timmerhus, fritidshus och villor i Tyresö.",
  "sections": [
    {"id": "timmer", "anchor": "Timmerhusen",
     "h2": "Timmer, panel och isolering i flera lager",
     "paras": [
       "Boverket beskriver hur husväggar i Sverige länge bestod av liggande omålat timmer som var både stomme och fasad, och hur timmerhusen under 1800-talet fick en fasad av träpanel för att skydda stommen. Stockholms läns museums inventering av Solberga och delar av Raksta från 2008 visar hur den historien fortsätter i Tyresö: flera av de äldre husen har timmerstomme, rödfärgad locklistpanel och vita knutar, lister och foder.",
       "Inventeringen beskriver också hur väggarna har förändrats. Om stugan vid Follbrinksströmmen skrivs att fasaderna troligen är tilläggsisolerade. Om ett annat hus står att det tilläggsisolerades under 1980-talet, och om huset som kallas Telegrafen att den äldre panelen sitter kvar under isoleringen.",
       "En vägg i ett sådant hus kan alltså bestå av timmer, en gammal panel, isolering och en nyare panel. Varje lager påverkar hur väggen torkar ut, och det är därför vi inte river förrän vi vet vad som finns där.",
     ],
     "aside": {"title": "Det kan finnas i väggen", "items": [
       "Timmerstomme", "Äldre panel under den nya",
       "Tilläggsisolering från en senare renovering", "Nyare locklistpanel ytterst"]}},
    {"id": "fukt-tyreso", "h2": "Varför lagren spelar roll för fukten",
     "paras": [
       "Boverket varnar för att invändig isolering gör väggens utsida kallare, så att fukt som kommit in torkar långsammare och risken för röta och mögel ökar. Utvändig isolering håller i stället den befintliga väggen varmare och torrare. Men även en utvändig lösning kräver att ytterpanelen kan torka: myndigheten beskriver hur en ventilerad luftspalt bakom det yttre skiktet låter vatten som kommit förbi rinna ut igen.",
       "När vi öppnar en vägg i ett äldre Tyresöhus kontrollerar vi därför om det finns en luftspalt bakom den yttersta panelen, om vindskyddet är helt och om den äldre panelen är torr. Är den det kan den få sitta kvar, på samma sätt som på Telegrafen. Är den angripen tas den bort, och då ser vi också över timret bakom.",
       "Lagning går ofta före byte. Vid renoveringen av Solberga gård lagades stommen och panelen i den omfattning som behövdes, enligt museets rapport, och det är en arbetsordning vi gärna följer.",
     ],
     "aside": None},
    {"id": "grund-tyreso", "h2": "Naturstensgrunden och de nedersta brädorna",
     "paras": [
       "Flera av husen i inventeringen står på naturstensgrund, en del fogad med bruk och en del putsad och gråmålad. Övergången mellan grund och panel är fasadens mest utsatta del: regn som studsar från marken, snö som ligger kvar mot väggen och vatten som rinner ner bakom ett bleck.",
       "Vi ser till att panelen slutar en bit ovanför grunden och att det finns ett droppbleck som leder vattnet ut. Har grundputsen släppt lagas den med ett bruk som passar underlaget. Dränering av husgrunden är ett eget arbete men hör ihop med fasaden, och ger enligt Skatteverket också rotavdrag.",
       "Är det snickeriet runt fasaden som behöver förnyas, som förstukvist eller fönsterfoder, kan " + _L.format("snickare-tyreso.html", "snickare i Tyresö") + " ta hand om det.",
     ],
     "aside": {"title": "Kontrollera vid grunden", "items": [
       "Avstånd mellan panel och grund", "Droppbleck ovanför grunden",
       "Släppt puts på stengrunden", "Hur vattnet rinner från taket"]}},
    {"id": "lov-tyreso", "h2": "Lovfritt i de flesta fall, men inte i värdefulla miljöer",
     "paras": [
       "Tyresö kommun skriver att det sedan 1 december 2025 inte krävs bygglov för fasadförändringar som ommålning, nytt tak eller nya fönster på en- och tvåbostadshus, men att lov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden i sig är särskilt värdefull. Sådana områden kan vara utpekade i översiktsplan, kulturmiljöprogram eller detaljplan. Kommunen påpekar att uppdaterad information i vissa fall saknas och uppmanar fastighetsägare att höra av sig.",
       "Museets inventering föreslog skyddsbestämmelser som omfattar flera av husens äldre stomme, fasad- och takmaterial och den röda färgsättningen. Om sådana bestämmelser har förts in i detaljplanen gäller utökad lovplikt. Vill du ha ett formellt besked kan du söka frivilligt bygglov.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi en fasad i Tyresö",
  "steps": [
    ("Besök", "Vi går runt huset och öppnar panelen på ett ställe för att se vilka lager väggen består av."),
    ("Plan och skydd", "Detaljplanen kontrolleras och vid behov kontaktar vi kommunen om husets värden."),
    ("Kostnadsförslag", "Lagning, byte, isolering och grundarbeten redovisas var för sig i ett skriftligt förslag."),
    ("Ställning", "Ställningen anpassas efter tomtens berg och träd."),
    ("Panel och anslutningar", "Skadade delar lagas eller byts, luftspalt och bleck görs om och grundputsen lagas."),
    ("Genomgång", "Vi visar vad som gjorts och vad som är bra att hålla koll på framöver."),
  ],
  "rot_h2": "ROT för fasadrenovering i Tyresö",
  "rot": [
    "Skatteverket ger rotavdrag i småhus för att byta och reparera fasader, tilläggsisolera, dränera husgrunder och montera byggnadsställningar i samband med rotarbetet. Avdraget gäller även ett fritidshus som du äger och använder.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Tyresö?",
  "price": [
    "Hur många lager väggen har och i vilket skick de är, om timmer eller äldre panel behöver lagas, om väggen ska isoleras och hur grunden mår. Kuperade tomter med berg och träd kan också påverka ställningen. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan den gamla panelen sitta kvar under en ny fasad på vårt timmerhus i Tyresö?",
     "Om den är hel och torr kan den det, som på huset Telegrafen vid Uddbykvarn. Är den angripen av röta tas den bort och timret bakom kontrolleras."),
    ("Hur ser ni om väggen redan är tilläggsisolerad?",
     "Vi tar loss en bräda på ett undanskymt ställe. Då syns om det finns isolering, vindskydd och luftspalt bakom den yttre panelen."),
    ("Varför ruttnar de nedersta brädorna först på huset?",
     "Det är där regnstänk från marken och snö mot väggen gör mest skada. Panelen ska sluta en bit ovanför grunden, och ett droppbleck leder bort vattnet."),
    ("Krävs bygglov för ny panel på ett hus i Solberga?",
     "Normalt inte för ett en- eller tvåbostadshus. Omfattas huset av skyddsbestämmelser i detaljplanen, eller ligger det i ett särskilt värdefullt område, krävs lov. Fråga kommunen om du är osäker."),
    ("Kan grundputsen på naturstensgrunden lagas samtidigt med fasaden?",
     "Ja. Lösa partier tas bort och lagas med ett bruk som passar underlaget, och sedan målas grunden i samma kulör som tidigare."),
  ],
  "sources": [
    ("Stockholms läns museum – Solberga/del av Raksta, kulturmiljöunderlag, rapport 2008:31 (pdf)",
     "https://insynsverige.se/documentHandler.ashx?did=20437"),
    ("Tyresö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
     "https://www.tyreso.se/boende--miljo/bygga/bygga-riva-eller-andra/forandringar-i-plan--och-bygglagen-fran-1-december-2025.html"),
    _BV_FMAT, _BV_ENST, _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset i Tyresö renoveras?", "Boka ett gratis platsbesök så går vi igenom panel, väggens lager och grunden."),
  "img": [
    ("Rödfärgat timmerhus med locklistpanel och vita knutar på naturstensgrund i Tyresö",
     "old Swedish two-storey timber house clad in falu red vertical board-and-batten panelling with white corner boards, white window frames and trims, standing on a rendered grey natural stone foundation, red clay tile roof, pine trees, granite rocks and a glimpse of a lake bay, Tyresö Stockholm, summer daylight, no people, no text"),
    ("Nedre delen av en röd panelfasad med droppbleck ovanför en grå stengrund",
     "close-up of the lower corner of a falu red board-and-batten facade on an old Swedish wooden house, boards ending above a grey rendered stone plinth with a neat dark metal drip flashing in between, white corner board, some gravel and grass at the base, daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ENSKEDE
"fasadrenovering-enskede.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Enskede", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Enskede – trähus fram ur eternit och plåt",
  "description": "Fasadrenovering i Enskede: ta fram trähuset under eternit eller plåt, laga kalkputs på typhusen och få fasaden rätt i riksintresset. Gratis platsbesök.",
  "h1": "Fasadrenovering i Enskede",
  "lead": "Gamla Enskede byggdes mellan 1908 och 1913 med typhus, och från början hade varje hustyp samma fasad- och takmaterial. Med åren har en del trähus fått nya skal av eternit eller plåt, medan andra har rustats tillbaka. Geal Entreprenad AB renoverar fasader i Gamla Enskede, Enskededalen och Enskedefältet, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Trähus, putsade typhus och småstugor i Enskede.",
  "sections": [
    {"id": "skal", "anchor": "Trähusen under skalet",
     "h2": "När trähuset försvann bakom eternit eller plåt",
     "paras": [
       "Stadsmuseets byggnadsinventering av Gamla Enskede från 1974–1977 beskriver hur området från början var sammanhållet: samtliga byggnadstyper hade enhetliga fasad- och takmaterial, samstämmig färgsättning och likartade staket och grindar. Inventeringen konstaterar sedan att trähus som tidigare underhållits med traditionella material ibland försvann bakom en fasad av eternit eller plåt, och att om- och tillbyggnader ryckte sönder skala och proportioner, särskilt bland typhusen.",
       "Inventeringen ger två förklaringar: nya ägare med andra krav och ambitioner, och byggindustrins stora utbud av nya material och metoder. Men den noterar också motsatsen. Flera husägare hade redan då rustat sina hus genom att byta ut gammal träpanel mot ny av samma typ, eternitfasader från 1950-talet hade plockats bort så att husen åter framstod som trähus, och fler ursprungliga fönster fick sitta kvar.",
       "Det är fortfarande den vanligaste frågan vi får om äldre Enskedehus med skivfasad: går det att ta fram trähuset igen, och vad finns kvar under skivorna?",
     ],
     "aside": {"title": "Ursprungligt i Gamla Enskede", "items": [
       "Trähus med panel", "Stenhus med puts",
       "Samma material inom varje hustyp", "Likartade staket och grindar"]}},
    {"id": "ta-fram", "h2": "Ta fram panelen – så går det till",
     "paras": [
       "Boverket skriver att många fasader under 1940- och 1950-talen kläddes med cementfiberplattor som innehöll asbest, och att fibrerna kan frigöras när plattorna bearbetas, till exempel om man borrar i dem. Innan en sådan fasad tas ner tas därför prover. Enligt Arbetsmiljöverket krävs tillstånd för att riva asbesthaltigt material på tak eller fasad, så den delen görs av ett företag som har det tillståndet. Därefter kan vi bedöma panelen bakom.",
       "Ibland är den gamla panelen hel nog att lagas och målas. Ofta har den spikats sönder när skivorna monterades, eller ruttnat där vatten trängt in bakom plåten. Då byts den mot ny panel av samma typ och dimension, precis som husägarna i inventeringen gjorde. Hörnbrädor, foder och vattbrädor ska ha samma mått som i husets ursprungliga utförande, och äldre ritningar på huset kan sökas fram via stadens e-tjänst Bygg- och plantjänsten.",
     ],
     "aside": None},
    {"id": "puts-enskede", "h2": "Typhusen i kalkputs på Margaretavägen",
     "paras": [
       "Alla hus i Enskede är inte av trä. Inventeringen beskriver typhus I, enfamiljsradhus ritade av arkitekten Viktor Bodin, som stenhus med kalkputsad fasad i slät- och spritputs, avfärgad i gul färgton. Stadens lantegendomsnämnd uppförde 37 sådana radhus 1908–1909, i sex huslängor längs Margaretavägen.",
       "Boverket skriver att kalkputs kan suga upp, transportera och avge fukt utan att skada stommen, men att putsen skadas om fuktbelastningen blir för stor, och att fuktig puts kan frysa sönder om fukten sitter kvar över vinterhalvåret. Enligt myndigheten är fukt nästan undantagslöst orsaken till putsbortfall. Innan vi lagar en putsfasad letar vi därför efter orsaken, oftast vid takfot, fönsterbleck eller sockel.",
       "Lagningar görs med kalkbruk och samma struktur, slät eller sprutad, så att de smälter in. För radhusen innebär det också att samma lösning bör väljas för hela längan. Ska taket ses över samtidigt finns mer under " + _L.format("takrenovering-enskede.html", "takrenovering i Enskede") + ".",
     ],
     "aside": {"title": "Före putslagning", "items": [
       "Var kommer fukten ifrån?", "Slätputs eller spritputs?",
       "Hur fast sitter resten av putsen?", "Vilken avfärgning finns?"]}},
    {"id": "lov-enskede", "h2": "Riksintresse och lovplikt i Enskede",
     "paras": [
       "Byte av material på fasad räknas som fasadändring, och staden räknar också tilläggsisolering hit. För en- och tvåbostadshus krävs normalt inget bygglov sedan 1 december 2025, men inom riksintresse för kulturmiljövården och i områden som utpekats som särskilt kulturhistoriskt värdefulla gäller utökad lovplikt. Stadsmuseets klassificeringskarta visar var de gränserna går.",
       "Att byta en eternitfasad mot panel av husets ursprungliga typ kan därför kräva lov på samma sätt som det omvända. Vid en ansökan vill staden ha fasadritning i skala 1:100 och en material- och kulörbeskrivning med NCS-koder. Vi hjälper dig att ta fram underlaget, och vill du ha ett besked om husets värde kan du vända dig till Stadsmuseet.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går fasadrenoveringen till i Enskede",
  "steps": [
    ("Besök", "Vi tittar på fasaden, letar efter spår av den ursprungliga panelen eller putsen och mäter detaljer."),
    ("Prover och klassning", "Skivfasader provtas för asbest, och vi kontrollerar husets läge i Stadsmuseets karta."),
    ("Kostnadsförslag", "Rivning, ny panel eller putslagning och målning redovisas var för sig i ett skriftligt förslag."),
    ("Rivning av skivor", "Asbesthaltiga skivor tas ner av ett företag med tillstånd innan vårt arbete börjar."),
    ("Panel eller puts", "Panel av samma typ monteras eller putsen lagas med kalkbruk i rätt struktur."),
    ("Avslutning", "Fasaden ytbehandlas och vi går igenom resultatet tillsammans."),
  ],
  "rot_h2": "ROT-avdrag för fasadarbete i Enskede",
  "rot": [
    "Att byta och reparera fasader, mura och reparera putsade fasader och måla fasader är rotarbete i ett småhus enligt Skatteverket, liksom att montera och ta ner byggnadsställningar i samband med arbetet.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset?",
  "price": [
    "Om en skivfasad måste provtas och rivas, hur mycket av den gamla panelen som går att rädda, om detaljer som foder och hörnbrädor måste tillverkas i äldre mått och hur stora putsskador det rör sig om. De smala gatorna och små tomterna påverkar också hur ställningen kan stå. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan eternitplattorna på vårt hus i Gamla Enskede tas bort så att trähuset syns igen?",
     "Det har gjorts i området sedan 1970-talet enligt Stadsmuseets inventering. Plattorna provtas först för asbest och tas ner av ett företag med tillstånd. Sedan bedömer vi panelen bakom."),
    ("Vad gör vi om panelen under plåten är för skadad?",
     "Då byts den mot ny panel av samma typ och dimension, med hörnbrädor och foder i samma mått som husets ursprungliga utförande."),
    ("Hur lagas spritputsen på ett radhus på Margaretavägen?",
     "Lösa partier knackas ner och lagas med kalkbruk som sprutas på så att strukturen blir densamma. Därefter avfärgas ytan så att lagningen inte syns."),
    ("Behöver vi bygglov för att byta skivfasaden mot träpanel i Enskede?",
     "Byte av fasadmaterial är en fasadändring. Inom riksintresset och i områden som är utpekade som särskilt värdefulla krävs bygglov, även om du går tillbaka till husets ursprungliga material."),
    ("Var hittar vi de ursprungliga ritningarna till typhuset?",
     "Stadsbyggnadskontorets äldre handlingar kan sökas fram i e-tjänsten Bygg- och plantjänsten. De visar ofta panelens indelning och fönstrens placering."),
  ],
  "sources": [
    ("Stadsmuseet via Stockholmskällan – Gamla Enskede, byggnadsinventering 1974–1977 (pdf)",
     "https://stockholmskallan.stockholm.se/postfiles/KUL/SSM_Gamla_Enskede__byggnadsinventering_1974_1977_00.pdf"),
    ("Stockholmskällan / Stadsmuseet – Sockenplan (Stockholms spår, pdf)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000049.pdf"),
    ("Stockholms stad – Riksintressen för kulturmiljövården i Stockholm (pdf)",
     "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf"),
    ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest",
     "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/"),
    _STH_FASAD, _STH_KLASS, _BV_FMAT, _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Vill du ta fram trähuset i Enskede igen?", "Boka ett gratis platsbesök så går vi igenom fasaden och vad som finns under ytan."),
  "img": [
    ("Gult trähus med panel och vita fönster bakom ett staket i Gamla Enskede",
     "early 1900s Swedish wooden garden-city house in Gamla Enskede Stockholm with freshly restored vertical wooden panelling painted pale ochre yellow, white window frames with small panes, steep red clay tile roof, low white picket fence and gate, fruit trees and lilac, narrow quiet street, spring daylight, no people, no text"),
    ("Gul spritputsad radhusfasad med släta fönsteromfattningar och ett lagat parti",
     "facade of a 1909 Swedish two-storey rendered terraced house painted pale ochre yellow, the wall surface has coarse rough-cast pebbly spray render texture, with smooth flat render bands framing the windows, old white wooden windows with small panes, dark grey metal sill flashings, one rectangular area under a window has fresh rough-cast render that is slightly paler yellow than the rest, early spring daylight, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VALLENTUNA
"fasadrenovering-vallentuna.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Vallentuna", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Vallentuna – fritidshus och stationsvillor",
  "description": "Fasadrenovering i Vallentuna: omvandlade fritidshus, villor vid Roslagsbanan och ritningar ur bygglovsarkivet som underlag. Gratis platsbesök.",
  "h1": "Fasadrenovering i Vallentuna",
  "lead": "Många hus i Vallentuna byggdes för ett annat liv än det de har i dag: villor vid Roslagsbanans stationer och fritidshus som blivit permanentbostäder. Fasaden är ofta det som först visar att huset används mer än det var tänkt. Geal Entreprenad AB renoverar fasader i hela Vallentuna kommun, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Fritidshus, stationssamhällen och villor i Vallentuna.",
  "sections": [
    {"id": "fritidshus-vtuna", "anchor": "Fritidshusen",
     "h2": "Fritidshus som blivit permanentbostäder",
     "paras": [
       "Vallentunas översiktsplan 2040 beskriver hur gränsen mellan permanent boende och fritidsboende blir allt mer flytande, eftersom allt fler bosätter sig i sitt fritidshus eller använder det en större del av året. Sedan 1990-talet har de flesta fritidshusområden i kommunen omvandlats, framför allt som en del av tätortsutvecklingen.",
       "Utanför tätorterna finns två större områden som är planlagda för fritidsboende. Det största är Garns-Ekskogen i östra delen av kommunen med omkring 500 bebyggda fastigheter, där detaljplanerna till största delen ger en byggrätt på 50 kvadratmeter för huvudbyggnaden. I Lövsättra i södra delen finns en stugby med ett 90-tal bebyggda kolonilotter.",
       "Ett hus som byggdes för sommarbruk har ofta en enkel vägg: panel direkt på regelverket, tunn eller ingen isolering och små takutsprång. När det värms upp hela vintern förändras fuktförhållandena i väggen, och då märks bristerna.",
     ],
     "aside": {"title": "Vanligt i ett sommarbyggt hus", "items": [
       "Panel utan luftspalt", "Tunn eller ingen isolering",
       "Korta takutsprång", "Låg sockel eller plintar"]}},
    {"id": "vagg-vtuna", "h2": "Från sommarvägg till åretruntvägg",
     "paras": [
       "Boverket skriver att utvändig tilläggsisolering ofta är bäst för både energi och fukt, eftersom den befintliga väggen blir varmare och torrare. Myndigheten råder också till att isolera när det är torrt väder för att inte stänga in fukt, och att först åtgärda orsaken om det finns mögel eller röta.",
       "I ett litet hus med begränsad byggrätt är utvändig isolering dessutom ett sätt att behålla rummen som de är. Invändig isolering minskar boytan och gör väggens utsida kallare. En utvändig lösning ändrar i stället husets yttre mått, och Boverket påpekar att ett hus som står nära fastighetsgränsen kan komma att inkräkta på grannens tomt. Det stämmer vi av innan något beställs.",
       "Ny panel monteras med luftspalt bakom, så att vatten som tar sig förbi kan rinna ut. Takfoten kan behöva förlängas när väggen blir tjockare, annars hamnar mer regn på fasaden. Om stuprör och hängrännor ska bytas samtidigt, se " + _L.format("hangrannor-stupror.html", "hängrännor och stuprör") + ".",
     ],
     "aside": None},
    {"id": "stationsvillor", "h2": "Villorna vid Roslagsbanan",
     "paras": [
       "Enligt översiktsplanen började en ny tid 1885 när Roslagsbanan invigdes mellan Stockholm och Rimbo. Banan byggdes för att försörja Stockholm med jordbruksprodukter och andra varor, och kring stationerna växte samhällen fram med villabebyggelse. Planen beskriver hur tidstypiska byggnader, tomtstorlekar och kvartersindelning där ofta bildar tydliga årsringar.",
       "En villa från stationssamhällets tid har ofta snickeridetaljer som är svåra att få tillbaka om de rivs: profilerade foder, knutlådor och vattbrädor. Vid en fasadrenovering tar vi ner dem varsamt, lagar det som går och tillverkar nytt efter mall där det behövs. Översiktsplanen säger att förändringar av kulturmiljöer kräver förståelse för platsens historia, karaktär och funktion.",
       "Boverket skriver att byte av fasadbeklädnad till samma material och utförande är underhåll och inte en fasadändring. Det är oftast den väg vi rekommenderar på de här husen. Panelens bredd, profil och riktning mäts upp innan något rivs, så att det nya virket blir lika.",
     ],
     "aside": {"title": "Detaljer värda att spara", "items": [
       "Profilerade fönsterfoder", "Knutlådor och hörnbrädor",
       "Vattbrädor över sockeln", "Äldre fönsterbågar"]}},
    {"id": "arkiv-vtuna", "h2": "Ritningarna i bygglovsarkivet och lovfrågan",
     "paras": [
       "Vallentuna kommuns digitala bygglovsarkiv innehåller ritningar över byggnader som uppförts ungefär mellan 1950 och 2024. Cirka 75 procent av handlingarna är digitaliserade och resten skannas in löpande. Fasadritningen i skala 1:100 visar hur huset såg ut när det byggdes, och äldre handlingar kan beställas.",
       "Kommunen skriver att det inte krävs bygglov för fasadförändringar som ommålning, nytt tak eller nya fönster på en- och tvåbostadshus, men att lov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden är särskilt värdefull. En ansökan ska då innehålla situationsplan, fasadritning i skala 1:100, redovisning av material och kulörer med NCS-koder och kontrollplan.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Vallentuna till",
  "steps": [
    ("Besök på plats", "Vi går igenom väggens uppbyggnad, sockel, takfot och fönster och öppnar panelen där det behövs."),
    ("Ritningar och plan", "Vi tar fram ritningar ur bygglovsarkivet och kontrollerar detaljplanen och husets placering mot gränsen."),
    ("Kostnadsförslag", "Panel, isolering, takfot och fönsteranslutningar redovisas var för sig i ett skriftligt förslag."),
    ("Ställning", "Ställningen sätts upp och fönster och planteringar skyddas."),
    ("Vägg och panel", "Vindskydd, isolering och ny panel med luftspalt monteras, och detaljer lagas eller tillverkas efter mall."),
    ("Slutgenomgång", "Vi går igenom resultatet med dig på plats."),
  ],
  "rot_h2": "Rotavdrag för fasadarbete i Vallentuna",
  "rot": [
    "Att byta och reparera fasader, tilläggsisolera och montera byggnadsställningar i samband med rotarbete ger rotavdrag i småhus. Det gäller både permanentbostaden och ett fritidshus som du äger och använder.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset i Vallentuna?",
  "price": [
    "Hur väggen är uppbyggd i dag, om den ska isoleras, om takfot och sockel behöver byggas om och hur många snickeridetaljer som ska lagas eller tillverkas på nytt. Även tillgängligheten till tomten och avståndet för materialtransporter påverkar. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Vårt fritidshus i Garns-Ekskogen ska bli åretruntbostad – var börjar man med fasaden?",
     "Med att se hur väggen är uppbyggd. Ett sommarbyggt hus saknar ofta luftspalt och isolering. Utvändig tilläggsisolering med ny panel håller rummen intakta, men kontrollera avståndet till fastighetsgränsen först."),
    ("Kan vi få fram de ursprungliga ritningarna till vårt hus i Vallentuna?",
     "Ritningar över hus byggda ungefär 1950–2024 finns i kommunens digitala bygglovsarkiv, där du söker på adress eller fastighetsbeteckning. Äldre handlingar kan beställas från arkivet."),
    ("Varför ska takfoten förlängas när väggen isoleras?",
     "När väggen blir tjockare skjuter takfoten ut mindre över fasaden och mer regn når panelen. Boverket nämner takfoten som en av detaljerna som påverkas."),
    ("Hur sparar ni snickeridetaljerna på en äldre villa nära Roslagsbanan?",
     "Foder, knutlådor och vattbrädor tas ner varsamt och lagas. Det som inte går att rädda tillverkas efter mall från de gamla delarna."),
    ("Vilka handlingar behövs om fasadändringen kräver bygglov i Vallentuna?",
     "Situationsplan, fasadritning i skala 1:100, redovisning av material och kulörer med NCS-koder och kontrollplan, enligt kommunen."),
  ],
  "sources": [
    ("Vallentuna kommun – Fasadändring", "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/behover-jag-bygglov/fasadandring"),
    ("Vallentuna kommun – Bygglovsarkivet", "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/bygglovsarkivet"),
    ("Vallentuna kommun – Översiktsplan 2040 (pdf)",
     "https://vallentuna.se/download/18.63572f8619eeecafce08366/1782478377449/2.11.7%20%C3%96versiktsplan%202040.pdf"),
    _BV_ISOL, _BV_FASAD, _BV_ENST, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset i Vallentuna förnyas?", "Boka ett gratis platsbesök så går vi igenom väggen, sockeln och takfoten tillsammans."),
  "img": [
    ("Rödmålat fritidshus i trä som byggts om till åretruntbostad i Vallentuna",
     "small Swedish 1960s wooden holiday cottage that has been renovated into a year-round home, new vertical falu red board-and-batten panelling with white window frames, slightly extended eaves, birch and pine trees, rural plot near open fields, Vallentuna Roslagen, autumn daylight, no people, no text"),
    ("Profilerat fönsterfoder på en äldre gulmålad villa med liggande panel",
     "close-up of an old Swedish wooden villa from around 1900 with pale yellow painted horizontal panelling, an old wooden two-pane casement window with traditional putty glazing, a white painted profiled wooden window casing with a decorative carved top piece, a white vertical corner board at the edge, daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"fasadrenovering-osteraker.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Österåker", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Österåker – Ljusterö och skärgårdshus",
  "description": "Fasadrenovering i Österåker: fritidshus från 1950- och 60-talens planer, rödfärgade fiskestugor och slagregn i skärgården. Gratis platsbesök.",
  "h1": "Fasadrenovering i Österåker",
  "lead": "Österåker sträcker sig från Åkersberga ut i skärgården, och fasaderna där har både vind, regn och en lång väg för materialet att hantera. Många hus byggdes som fritidshus och används i dag året runt. Geal Entreprenad AB renoverar fasader i Åkersberga, på Ljusterö och i övriga Österåker, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Skärgårdshus, fritidshus och villor i Österåker.",
  "sections": [
    {"id": "ljustero", "anchor": "Ljusterö",
     "h2": "Ljusterö: 2 000 året runt och över 10 000 på sommaren",
     "paras": [
       "Österåkers planprogram för Ljusterö från 2010 beskriver ön som en av skärgårdens största. Där bor omkring 2 000 personer permanent under vinterhalvåret och uppskattningsvis drygt 10 000 under sommarhalvåret. Ön nås med en statlig färjelinje från Östanå.",
       "Programmet konstaterar att fritidshusbebyggelsen och det moderna skogsbruket har gett de största landskapsförändringarna i kommunen under 1900-talet. Majoriteten av detaljplanerna på Ljusterö är från 1950- och 1960-talen, och i princip alla planer från den perioden är upprättade för fritidshus och fullt utbyggda. Omvandlingen till permanentboende pågår, och i ett mer centralt beläget omvandlingsområde som Svinninge var permanentboendet kring 70 procent.",
       "Ett hus från en fritidshusplan på 1950-talet har ofta en vägg som var tänkt för sommarbruk. Ska det bebos året runt är fasaden en av de delar som behöver ses över, och ofta i samma veva som isoleringen. Boverket påpekar att det blir mest lönsamt att tilläggsisolera när fasaden ändå ska göras om, till exempel när panelen byts.",
     ],
     "aside": {"title": "Ljusterö i siffror", "items": [
       "Cirka 2 000 permanentboende", "Drygt 10 000 under sommaren",
       "Planerna mest från 1950–60-tal", "Färja från Östanå"]}},
    {"id": "fiskebyar", "h2": "Rödfärgade stugor, sommarvillor och en putsad herrgård",
     "paras": [
       "Programmet pekar ut flera miljöer med kulturhistoriska värden. Laggarsvik var en fiskeby som uppfördes i början av 1900-talet, med rödfärgade stugor på geometriskt utlagda tomter runt hamnen. Östra Lagnö by beskrivs som en av kommunens bäst bevarade skärgårdsbyar, och Västra Lagnö har flera stora sommarvillor från tidigt 1900-tal. Bolby och Hummelmora har byggnader främst från sent 1800-tal och tidigt 1900-tal.",
       "Marum är en herrgård uppförd kring 1740, byggd i tegel med putsad fasad i två våningar och förklarad som byggnadsminne. Den visar att det i skärgårdens kulturmiljöer finns putsade fasader, inte bara trä.",
       "I de här miljöerna rekommenderar programmet stor varsamhet vid förändringar. För en fasadrenovering innebär det att behålla panelens typ och de rödfärgade husens karaktär, och att laga hellre än byta där det går.",
     ],
     "aside": None},
    {"id": "vader-osteraker", "h2": "Slagregn och anslutningar på utsatta lägen",
     "paras": [
       "Boverket skriver att sannolikheten för inträngande vatten i en träregelvägg är hög vid slagregn och om det finns hål i fasadens ytskikt där vatten kan sugas eller tryckas in. När det blåser och regnar samtidigt kan en ventilerad luftspalt bakom panelen minska tryckskillnaden över det yttre regnskyddet, så att mindre vatten pressas in.",
       "På ett hus nära vattnet går vi därför igenom fönsteranslutningar, genomföringar och skarvar extra noga. Boverket påpekar att det vid fönster ofta saknas vattenavledning i utrymmet mellan karm och omfattning, men att det i dag finns lösningar och material för att åtgärda det. Fönsterbleck med tillräckligt fall och uppvik mot karmen är en del av samma arbete.",
       "Är det fönstren själva som är slut finns mer om byte under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": {"title": "Kontrollera på utsatta lägen", "items": [
       "Luftspalt bakom panelen", "Tätning mellan karm och omfattning",
       "Fönsterbleckens fall", "Genomföringar för rör och kablar"]}},
    {"id": "logistik", "h2": "Material, färja och lovfrågan",
     "paras": [
       "En fasadrenovering på Ljusterö eller en annan ö kräver mer planering än på fastlandet. Panel, isolering och ställning ska fraktas över, och allt som saknas en dag kostar en extra resa. Vi beställer därför material efter uppmätning på plats och samlar leveranserna. Ställningen planeras efter tomten, som i skärgården ofta är bergig och sluttar mot vattnet, och vi bestämmer i förväg var material kan läggas upp utan att skada mark och växter. Rivningsvirke och spill tas med tillbaka i samma transporter.",
       "Från den 1 december 2025 gäller enligt Boverket att det normalt inte behövs bygglov för att byta kulör eller fasadmaterial på ett en- eller tvåbostadshus. Undantaget är utökad lovplikt, bland annat när detaljplanen har bestämmelser om skydd för särskilda värden eller när byggnaden eller området är särskilt värdefullt. Vi kontrollerar detaljplanen för fastigheten innan arbetet planeras.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går det till i Österåker",
  "steps": [
    ("Platsbesök", "Vi kommer ut till huset, även på ön, och går igenom panel, anslutningar och sockel."),
    ("Plan och värden", "Detaljplanen och eventuella kulturvärden kontrolleras."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med arbete, material och transporter redovisade."),
    ("Leverans och ställning", "Materialet beställs efter uppmätning och fraktas ut i samlade leveranser."),
    ("Fasadarbetet", "Panel lagas eller byts, luftspalt och fönsteranslutningar görs om och bleck förnyas."),
    ("Genomgång", "Vi går igenom fasaden med dig innan ställningen tas ner."),
  ],
  "rot_h2": "Rotavdrag för fasaden i Österåker",
  "rot": [
    "Skatteverket ger rotavdrag för att byta och reparera fasader, tilläggsisolera, reparera eller byta fönster och montera byggnadsställningar i samband med rotarbete i ett småhus. Avdraget gäller också ett fritidshus som du äger och använder. Resekostnader och material ger inget avdrag, vilket är bra att veta på en ö.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här påverkar priset i Österåker",
  "price": [
    "Hur stor del av panelen som behöver bytas, om väggen ska isoleras, hur många fönsteranslutningar som ska göras om och om huset ligger på fastlandet eller på en ö. Transporter med färja och möjligheten att ställa upp ställning på en bergig tomt räknas in. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Tar ni uppdrag på Ljusterö trots att det är färja dit?",
     "Ja. Vi planerar material och ställning så att leveranserna samlas, och transporterna redovisas i kostnadsförslaget."),
    ("Vårt hus på Ljusterö byggdes som fritidshus på 1960-talet – behöver fasaden göras om för att bo där året runt?",
     "Det beror på hur väggen är uppbyggd. Vi öppnar panelen på ett ställe och ser om det finns isolering och luftspalt. Ofta räcker det inte med ny färg för att huset ska fungera året runt."),
    ("Hur skyddar man en fasad nära vattnet mot slagregn?",
     "Med panel som har en ventilerad luftspalt bakom, tät anslutning mellan fönsterkarm och vägg och fönsterbleck med ordentligt fall."),
    ("Ger transporten med färjan rotavdrag?",
     "Nej. Rotavdraget gäller arbetskostnaden. Resekostnader och material ger inget avdrag."),
    ("Kan en rödfärgad stuga i Laggarsvik få ny panel utan att ändra karaktär?",
     "Ja, om panelen byts mot samma typ och dimension och färgsättningen behålls. Ett byte till samma material och utförande räknas som underhåll."),
  ],
  "sources": [
    ("Österåkers kommun – Ljusterö planprogram (april 2010, pdf)",
     "https://www.osteraker.se/download/18.367d658917909e8fc2b5172/1628586891118/Ljuster%C3%B6_planprogram_Hela_L%C3%A5guppl%C3%B6st.pdf"),
    _BV_FASAD, _BV_FMAT, _BV_ENST, _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver fasaden på huset i Österåker ses över?", "Boka ett gratis platsbesök, på fastlandet eller på ön, så går vi igenom fasaden tillsammans."),
  "img": [
    ("Rödfärgade trähus vid en liten hamn i Österåkers skärgård",
     "small group of falu red Swedish wooden cottages with white window frames and corner boards around a small sheltered harbour in the Stockholm archipelago, a wooden jetty, granite rocks and pine trees, Ljusterö Österåker, calm summer evening light, empty scene, no people, no boats with people, no text"),
    ("Fönster i en röd panelvägg med nytt fönsterbleck och tät anslutning mot karmen",
     "close-up of a white wooden window in a falu red horizontal wooden panel wall of a Swedish archipelago house, a new dark grey metal window sill flashing with clear slope and upturned ends against the frame, neat white trim boards, daylight, no people, no hands, no text"),
  ],
  "related": [],
},

}
