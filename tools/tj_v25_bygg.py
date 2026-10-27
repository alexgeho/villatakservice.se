# -*- coding: utf-8 -*-
"""Byggföretag – ortsidor v25: Farsta, Spånga, Kungsholmen, Södermalm, Vasastan, Östermalm (2026-10-26).
Hör till byggfirma.html (TJ_HUB["byggforetag"]). Intent: anlita ett byggföretag för ett större projekt – lov,
anmälan, byggherrens ansvar – skild från ortens totalrenovering-/badrumsrenovering-sidor (enskilda rum, hela huset)
och från byggföretagssidorna v8–v13 (villor, tillbyggnad, vind i villa, tomt). En huvudfråga per sida.
Tre bilder per sida: img[0] hero 4:3, img[1]–[2] 3:2.

Lokal vinkel per sida:
Farsta – en ny bostad i villan (bygglovsbefriat i enbostadshus, men utökad lovplikt i småstugeområdena Tallkrogen,
  del av Svedmyra och del av Sköndal som Varsam pekar ut som kulturhistoriskt värdefulla), dagens krav på bostaden,
  anmälan vid brandskydd, bärande, VA och eldstad; områdesfakta 2025 (småhus med äganderätt).
Spånga – riva och bygga nytt i villastäderna (Solhem: en tiondel av tomten fick bebyggas, kulturhistoriskt värdefull
  miljö), rivningslov, materialinventering, kontrollansvarig, nybyggnadskarta, klimatdeklaration (undantag för
  privatperson). Ingen ROT för nybyggnad – egen trust-rad.
Kungsholmen – föreningen beställer stambyte: när anmälan krävs, tillgängligheten, IMD vid ombyggnad, ansvaret för
  ledningarna enligt bostadsrättslagen; områdesfakta 2025. Egen trust-rad (föreningen får inget rotavdrag).
Södermalm – inreda vinden till bostäder: bygglov, tillgänglighet och 35-kvm-undantaget, avvikelse från förbud i
  detaljplan, brandskyddet och brandcellsgränser; områdesfakta 2025. Egen trust-rad.
Vasastan – lokal blir bostad: väsentligt ändrad användning, senaste faktiska användningen, dagens krav på bostaden och
  bostadskomplement; områdesfakta 2025 (Gustav Vasa, Västra Matteus). Egen trust-rad.
Östermalm – slå ihop två lägenheter: ingen bygglov men ofta anmälan, bärande väggar och ofullständiga ritningar,
  styrelsens tillstånd enligt bostadsrättslagen 7 kap. 7 §, klassade hus.

Fakta endast från källorna i respektive 'sources', öppnade med urllib (Mozilla-UA) 2026-10-26, alla 200;
områdesfakta-pdf:erna och Varsam har textlager. Skatteverkets sidor svarade inte härifrån (anslutningen bröts) –
samma URL:er och samma ROT-formulering som sajtens tidigare byggföretagssidor.
Strukna / ej använda: avgifter, handläggningstider, Stadsmuseets svarstid, miljösanktionsavgifter, antal våningar
eller byggår för enskilda kvarter, alla priser, garantier, omdömen, egna uppdrag i orterna och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no hands, no text, no letters"

_B = "https://bygglov.stockholm/nar-behovs-bygglov/"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_STH_NYBOST = ("Stockholms stad – Ny bostad i enbostadshus (bygglovsbefriad)", _B + "andra-inomhus/ny-bostad-i-enbostadshus-bygglovsbefriad/")
_STH_YTTERL = ("Stockholms stad – Inredning av ytterligare bostad", _B + "andra-inomhus/inredning-av-ytterligare-bostad/")
_STH_VIND = ("Stockholms stad – Inreda vinden", _B + "andra-inomhus/inreda-vinden/")
_STH_BRAND = ("Stockholms stad – Brandskydd", _B + "andra-inomhus/brandskydd/")
_STH_ANV = ("Stockholms stad – Ändrad användning", _B + "andra-inomhus/andrad-anvandning/")
_STH_STAM = ("Stockholms stad – Stambyte", _B + "andra-inomhus/stambyte/")
_STH_OMB = ("Stockholms stad – Ombyggnad", _B + "andra-inomhus/ombyggnad/")
_STH_PLAN = ("Stockholms stad – Ändra planlösningen i en byggnad", _B + "andra-inomhus/andra-planlosningen-i-en-byggnad/")
_STH_BAR = ("Stockholms stad – Ändra i bärande konstruktion", _B + "andra-inomhus/andra-i-barande-konstruktion/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _B + "andra-inomhus/stadsmuseets-kulturhistoriska-klassificering/")
_STH_RIV = ("Stockholms stad – Rivning", _B + "rivning/rivning/")
_STH_VILLA = ("Stockholms stad – Villa eller småhus, nybyggnad och ändringar", _B + "bygga-nytt-och-bygga-till/villa-eller-smahus-nybyggnad-och-andringar/")
_STH_KLIM = ("Stockholms stad – Klimatdeklaration", "https://bygglov.stockholm/sok-lov-eller-anmalan/klimatdeklaration/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614)",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_BV_FORV = ("Boverket – Förvanskningsförbudet (PBL kunskapsbanken)",
            "https://www.boverket.se/sv/PBL-kunskapsbanken/teman/kulturvarden/kulturvarden-i-plan---och-bygglagen/krav-pa-byggnadsverk-och-tomter/forvanskningsforbudet/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_ROT_BASE = ("Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 "
             "kronor tillsammans med rutavdrag. Material och resor ger inget avdrag, och du ska äga bostaden när arbetet utförs.")
_TRUST_NY = ["Gratis besök och kostnadsförslag", "Nyckelfärdigt från grund till inflyttning"]
_TRUST_BRF = ["Gratis besök och kostnadsförslag", "Underlag till styrelsen och stämman"]

PAGES_TJ = {

# ------------------------------------------------------------------ FARSTA
"byggforetag-farsta.html": {
  "kind": "district", "service": "byggforetag", "ort": "Farsta", "svc_label": "Byggföretag",
  "title": "Byggföretag i Farsta – en ny bostad i villan",
  "description": "Byggföretag i Farsta: inreda en ny bostad i villan, när det är bygglovsbefriat, utökad lovplikt i småstugeområdena och kraven på den nya bostaden.",
  "h1": "Byggföretag i Farsta",
  "lead": "Många villor i Farsta är små, och fler familjer funderar på att inreda en egen bostad i huset för en förälder, ett vuxet barn eller för uthyrning. Geal Entreprenad AB bygger om villor i Farsta som total entreprenad och reder först ut om det räcker med en anmälan eller om bygglov krävs.",
  "card": "En ny bostad i villan.",
  "sections": [
    {"id": "smahusen-farsta", "anchor": "Småhusen i Farsta",
     "h2": "Småhusen i Farsta",
     "paras": [
       "Enligt Stockholms stads områdesfakta fanns det 2024 drygt 5 200 bostäder i småhus i Farsta stadsdelsområde, och 3 806 av dem ägdes med äganderätt. Resten var småhus i bostadsrätt eller hyrda.",
       "En stor del av småhusen ligger i småstugeområdena. Vägledningen Varsam utveckling av småhus- och villaområden nämner Tallkrogen, del av Svedmyra och del av Sköndal. Där byggdes husen efter stadens typritningar, och vägledningen konstaterar att bostäderna ofta är små och inte motsvarar dagens önskemål om standard.",
     ],
     "aside": {"title": "Småhus i Farsta 2024", "items": [
       "Drygt 5 200 bostäder i småhus", "3 806 med äganderätt", "Småstugeområden: Tallkrogen, del av Svedmyra och Sköndal"]}},
    {"id": "lovfritt-farsta", "h2": "När det räcker utan bygglov",
     "paras": [
       "Stockholms stad förklarar att du under vissa förutsättningar kan inreda ytterligare en bostad i ditt enbostadshus utan bygglov. Det gäller även om åtgärden inte följer detaljplanens bestämmelser.",
       "Lovfriheten betyder inte att du kan börja direkt. Ändrar du brandskydd eller bärande konstruktion, installerar vatten och avlopp eller en eldstad behöver du göra en anmälan och vänta på startbesked. I praktiken gäller det de flesta projekt där en ny bostad med kök och badrum inreds.",
     ],
     "aside": {"title": "Anmälan krävs om du", "items": [
       "Ändrar brandskyddet", "Ändrar bärande konstruktion", "Installerar vatten och avlopp", "Installerar en eldstad"]}},
    {"id": "smastugorna-farsta", "anchor": "Utökad lovplikt",
     "h2": "Utökad lovplikt i småstugeområdena",
     "paras": [
       "Varsam beskriver småstugeområdena som kulturhistoriskt värdefulla miljöer, och i tabellen är Tallkrogen, del av Svedmyra och del av Sköndal markerade så. Staden skriver att utökad lovplikt gäller om du bor i en särskilt kulturhistoriskt värdefull byggnad eller ett sådant område. Då behöver du söka bygglov även för det som annars är bygglovsbefriat.",
       "Stadsmuseets klassificeringskarta ger en första indikation, men staden påpekar att du kan behöva kontakta Stadsmuseet för en bedömning. Även fasadändringar i samband med en ny bostad kräver bygglov när huset eller området är särskilt värdefullt.",
     ],
     "aside": None},
    {"id": "kraven-farsta", "h2": "Bostaden ska uppfylla dagens krav",
     "paras": [
       "Staden skriver att en ny bostad ska uppfylla dagens krav, till exempel på tillgänglighet, brandsäkerhet, rumshöjd och bostadsutformning. Till bostaden ska det också finnas bostadskomplement som förråd, tvättstuga och förvaring för barnvagnar och cyklar.",
       "I en liten småstuga kan rumshöjden och brandavskiljningen mellan bostäderna bli de svåraste frågorna. Vi mäter upp huset, tar fram ritningar och går igenom med dig vad som får plats innan något rivs.",
     ],
     "aside": None},
    {"id": "tva-hushall-farsta", "anchor": "Två hushåll",
     "h2": "Planera för två hushåll",
     "paras": [
       "En bostad till i huset fungerar bäst när båda hushållen kan leva sina liv utan att störa varandra. Egen entré, ljudisolering i bjälklag och väggar mellan bostäderna och en tydlig gräns för trädgård och förvaring är frågor som är enklare att lösa på ritbordet än i efterhand.",
       "Vi går också igenom om installationerna ska delas eller vara separata, till exempel varmvatten, ventilation och el. Det påverkar både kostnaden och hur enkelt det blir att hyra ut eller att låta bostaden stå tom en period.",
     ],
     "aside": None},
    {"id": "helheten-farsta", "h2": "Ett projekt med flera delar",
     "paras": [
       "En ny bostad i villan innebär ofta att badrum och kök byggs, att en entré tillkommer och att väggar flyttas. Vi samordnar snickare, el, VVS och ventilation, och du har en kontakt genom hela arbetet. Du får också en tidsplan som visar när huset går att bo i och när det dammar som mest.",
       "Om badrummet i sig kan du läsa under " + _L.format("badrumsrenovering-farsta.html", "badrumsrenovering i Farsta") + ", och om att renovera hela huset under " + _L.format("totalrenovering-farsta.html", "totalrenovering i Farsta") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en ny bostad i en villa i Farsta till",
  "steps": [
    ("Platsbesök", "Vi tittar på huset, rumshöjderna och var en ny entré kan ligga."),
    ("Lov eller anmälan", "Klassning, detaljplan och behov av bygglov kontrolleras."),
    ("Ritningar och kontrollplan", "Underlag för anmälan eller ansökan tas fram."),
    ("Skriftligt kostnadsförslag", "Varje del – bad, kök, väggar och installationer – står för sig."),
    ("Ombyggnad", "Arbetet startar när startbeskedet finns."),
    ("Slutbesked", "Vi samlar intyg och kontrollplan inför slutbeskedet."),
  ],
  "rot_h2": "Rotavdrag när villan byggs om i Farsta",
  "rot": [
    _ROT_BASE,
    "Skatteverket ger rotavdrag för om- och tillbyggnad av ett småhus du äger. För arbete som ger avdrag drar Geal det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Farsta?",
  "price": [
    "Om bygglov krävs, hur mycket som byggs om och om nytt badrum, kök och ventilation behövs. En överblick finns under " + _L.format("byggfirma.html", "byggfirma") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för att inreda en bostad till i vår villa i Farsta?",
     "Det beror på var huset ligger. I ett enbostadshus kan det vara bygglovsbefriat, men i ett särskilt kulturhistoriskt värdefullt område som småstugeområdena krävs bygglov."),
    ("Vi bor i Tallkrogen – gäller utökad lovplikt för oss?",
     "Tallkrogen är utpekat som kulturhistoriskt värdefull miljö i stadens vägledning. Kontrollera Stadsmuseets karta och kontakta museet vid osäkerhet."),
    ("Måste den nya bostaden ha eget förråd och tvätt?",
     "Staden skriver att det ska finnas bostadskomplement som förråd, tvättstuga och förvaring för barnvagnar och cyklar."),
    ("Behövs anmälan även om bygglov inte krävs?",
     "Ja, om du ändrar brandskydd eller bärande konstruktion eller installerar vatten och avlopp eller eldstad."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Farsta stadsdelsområde (pdf)", _OF + "soderort/farsta/farsta-stadsdelsomrade.pdf"),
              _VARSAM, _STH_NYBOST, _STH_YTTERL, _STH_KL, _SKV, _SKV2],
  "cta": ("Vill ni inreda en ny bostad i villan i Farsta?", "Boka ett gratis platsbesök, så går vi igenom huset och reglerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Liten trävilla med tegeltak i ett småstugeområde",
     "small 1930s Swedish one-and-a-half storey wooden cottage with light grey vertical board facade and red clay tile mansard roof, hedge and fruit trees, row of similar cottages along a quiet street, south Stockholm, summer" + _IMG_END),
    ("Nybyggt litet kök i en ombyggd del av en villa",
     "full-frame photo filling the entire image, no borders: small newly built compact kitchen in a converted part of an old Swedish wooden house, white cabinets, light wood worktop, window with view to the garden, freshly painted walls, daylight" + _IMG_END),
    ("En liten husmodell och en rulle ritpapper på ett bord",
     "still life: a small white wooden house model next to a loosely rolled sheet of blank white tracing paper and a pencil on a light wooden table, potted plant, soft daylight from a window, minimal" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"byggforetag-spanga.html": {
  "kind": "district", "service": "byggforetag", "ort": "Spånga", "svc_label": "Byggföretag",
  "title": "Byggföretag i Spånga – riva och bygga nytt hus",
  "description": "Byggföretag i Spånga: riva en villa och bygga nytt i villastäderna, rivningslov, materialinventering, kontrollansvarig och klimatdeklarationen.",
  "h1": "Byggföretag i Spånga",
  "lead": "I Spångas villastäder står hus från olika epoker sida vid sida, och ibland är det ett gammalt hus som ska ersättas med ett nytt. Geal Entreprenad AB bygger nya villor i Spånga som total entreprenad och tar hand om både rivningen och det nya huset.",
  "card": "Riva och bygga nytt hus.",
  "trust": _TRUST_NY,
  "sections": [
    {"id": "villastaden-spanga", "anchor": "Villastäderna",
     "h2": "Villastäderna i Spånga",
     "paras": [
       "Varsam utveckling av småhus- och villaområden berättar att små stationssamhällen uppstod när järnvägen byggdes ut, och att några på 1910-talet blev municipalsamhällen med egen administration och beskattningsrätt. Spånga är ett av exemplen. Solhem, Bromsten, Flysta och Sundby räknas som villastäder.",
       "Villastäderna fick sina egna särdrag. I Solhem fanns stora tomter där endast en tiondel av tomten fick bebyggas. Enligt stadens områdesfakta fanns det 2024 i Solhem 1 946 bostäder i småhus med äganderätt, och i Bromsten 916.",
     ],
     "aside": {"title": "Villastäder i Spånga", "items": [
       "Solhem", "Bromsten", "Flysta", "Sundby"]}},
    {"id": "rivningen-spanga", "h2": "Rivningslov och vad som bevaras",
     "paras": [
       "Inom detaljplanerat område krävs rivningslov för att riva en byggnad eller en del av en byggnad. Staden gör då en sammantagen bedömning av om byggnaden bör bevaras utifrån dess historiska, kulturhistoriska, miljömässiga eller konstnärliga värde, och om rivningen stämmer med detaljplanen.",
       "I vägledningens tabell är Solhem markerat som kulturhistoriskt värdefull miljö. Där kan bedömningen bli strängare, och det lönar sig att titta på Stadsmuseets karta och detaljplanen innan man köper ett hus för att riva det.",
     ],
     "aside": None},
    {"id": "inventering-spanga", "anchor": "Materialinventering",
     "h2": "Materialinventering före rivningen",
     "paras": [
       "När en byggnad ska rivas behöver du ta fram en materialinventering som visar vilka material som finns och redovisar miljöfarligt avfall. Inventeringen ska göras innan rivningen påbörjas, och dokumentationen skickas in.",
       "Rivningen får också en kontrollplan som beskriver vilka kontroller som ska göras och av vem. Vi tar fram inventeringen, sorterar avfallet och lämnar underlaget till kommunen, så att rivningen kan börja när startbeskedet finns.",
     ],
     "aside": {"title": "Inför rivningen", "items": [
       "Rivningslov inom detaljplan", "Materialinventering med miljöfarligt avfall", "Kontrollplan", "Startbesked"]}},
    {"id": "nya-huset-spanga", "h2": "Det nya huset",
     "paras": [
       "Ett nytt hus kräver bygglov. Redan när du söker ska det finnas ett förslag på kontrollansvarig, och den kontrollansvariga ska ha åtagit sig uppdraget. Situationsplanen ritas på en nybyggnadskarta, som visar fastighet, markhöjder, planbestämmelser och anslutningar för vatten och avlopp.",
       "Vägledningen för villastäderna säger att nya byggnader ska utformas inom befintlig struktur, utifrån en samtida tolkning av platsens förutsättningar och den närliggande bebyggelsen. Den råder också att undvika fler utfarter intill varandra och att hårdgöra grönytor, så placeringen av infart och parkering hör till de första frågorna. Befintliga träd och höjdskillnader på tomten påverkar också var huset kan stå.",
     ],
     "aside": None},
    {"id": "tomterna-spanga", "anchor": "Tomterna",
     "h2": "Tomter som delats genom åren",
     "paras": [
       "Varsam beskriver hur villastäderna har förtätats genom att tomter successivt delats. Tillkommande hus på tomter kring 600 kvadratmeter har kompletterat eller ersatt den äldre bebyggelsen, och på 1960- och 70-talen ersattes många villor i villastäderna av grupper av enhetliga småhus.",
       "Den som river ett hus i dag bygger alltså i en miljö som redan har flera årsringar. Det nya huset prövas mot detaljplanen och mot omgivningen, och vägledningen lyfter material, färgsättning, volym och takform som aspekter med stor påverkan på områdets karaktär.",
     ],
     "aside": None},
    {"id": "klimat-spanga", "h2": "Klimatdeklaration – gäller den dig?",
     "paras": [
       "Den som söker bygglov för en ny byggnad kan behöva lämna en klimatdeklaration inför slutbeskedet. Staden listar undantag, och två av dem gäller ofta villor: byggnaden är inte större än 100 kvadratmeter bruttoarea, eller byggherren är en privatperson som uppför byggnaden privat.",
       "Det är vid det tekniska samrådet som staden tar ställning till om byggnaden omfattas. Om tillbyggnad i stället för nytt hus kan du läsa under " + _L.format("byggfirma.html", "byggfirma") + ", och om att renovera det befintliga huset under " + _L.format("totalrenovering-spanga.html", "totalrenovering i Spånga") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går det till att riva och bygga nytt i Spånga",
  "steps": [
    ("Platsbesök", "Vi tittar på huset, tomten och detaljplanen."),
    ("Rivningslov och bygglov", "Ansökningarna tas fram med ritningar och nybyggnadskarta."),
    ("Kontrollansvarig och kontrollplan", "Förslag på kontrollansvarig finns med redan i ansökan."),
    ("Skriftligt kostnadsförslag", "Rivning, grund, stomme och invändigt står för sig."),
    ("Rivning och bygge", "Materialinventering först, sedan rivning och det nya huset."),
    ("Slutbesked", "Vi samlar intyg och kontrollplan inför inflyttningen."),
  ],
  "rot_h2": "Rotavdrag gäller inte nybyggnad",
  "rot": [
    "Skatteverket ger inget rotavdrag för att bygga ett nytt hus. Avdraget gäller reparation, underhåll samt om- och tillbyggnad av en befintlig bostad.",
    "Väljer du att bygga om och bygga till det befintliga huset i stället kan arbetet ge rotavdrag. " + _ROT_BASE,
  ],
  "price_h2": "Vad påverkar kostnaden i Spånga?",
  "price": [
    "Husets storlek, grundläggningen på tomten, rivningen och om miljöfarligt avfall behöver saneras. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi rivningslov för att riva vår villa i Spånga?",
     "Ja, inom detaljplanerat område krävs rivningslov för att riva en byggnad. Staden bedömer då också om huset bör bevaras."),
    ("Måste vi klimatdeklarera vårt nya hus?",
     "Inte om du som privatperson bygger huset privat, eller om det är högst 100 kvadratmeter bruttoarea. Staden tar ställning vid det tekniska samrådet."),
    ("Får vi bygga större än det gamla huset?",
     "Det avgör detaljplanen. I Solhem fick till exempel bara en tiondel av de ursprungliga tomterna bebyggas, så läs planen innan ni ritar."),
    ("Vad är en materialinventering?",
     "En redovisning av vilka material som finns i huset, med miljöfarligt avfall. Den ska göras innan rivningen börjar."),
    ("När ska kontrollansvarig vara utsedd?",
     "Redan när du söker bygglov för nybyggnaden ska det finnas ett förslag på kontrollansvarig."),
  ],
  "sources": [_VARSAM,
              ("Stockholms stad – Områdesfakta 2025: Solhem (pdf)", _OF + "vasterort/jarva/solhem.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Bromsten (pdf)", _OF + "vasterort/jarva/bromsten.pdf"),
              _STH_RIV, _STH_VILLA, _STH_KLIM, _STH_KL, _SKV],
  "cta": ("Ska ni riva och bygga nytt i Spånga?", "Boka ett gratis platsbesök, så går vi igenom tomten och reglerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nybyggd villa i trä på en lummig tomt i en villastad",
     "newly built modern Swedish two-storey wooden villa with light grey vertical panel and black window frames on a green plot with old fruit trees, neighbouring older villas from different eras, quiet curving street, west Stockholm suburb, summer" + _IMG_END),
    ("Grund som gjuts för ett nytt hus på en villatomt",
     "construction site on a suburban villa plot: newly cast concrete slab foundation with formwork and insulation edges, stacked timber under a tarpaulin, mature trees around, overcast daylight" + _IMG_END),
    ("Containrar med rivningsavfall framför ett hus som rivs",
     "several open skips on a villa plot sorted for demolition waste: one with wood, one with metal, one with concrete and brick, part of an old house partly demolished behind, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ KUNGSHOLMEN
"byggforetag-kungsholmen.html": {
  "kind": "district", "service": "byggforetag", "ort": "Kungsholmen", "svc_label": "Byggföretag",
  "title": "Byggföretag på Kungsholmen – föreningens stambyte",
  "description": "Byggföretag på Kungsholmen: föreningens stambyte, när anmälan krävs, tillgängligheten i badrummen, IMD vid ombyggnad och ansvaret för ledningarna.",
  "h1": "Byggföretag på Kungsholmen",
  "lead": "På Kungsholmen är det oftast en bostadsrättsförening som beställer de stora byggprojekten, och stambytet är det största av dem. Geal Entreprenad AB tar på sig stambyten och ombyggnader för föreningar på Kungsholmen och hjälper styrelsen att reda ut vad som kräver anmälan.",
  "card": "Föreningens stambyte.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "foreningarna-kungsholmen", "anchor": "Föreningarna",
     "h2": "En stadsdel av bostadsrättsföreningar",
     "paras": [
       "Stockholms stads områdesfakta visar att det 2024 fanns 44 554 bostäder i Kungsholmens stadsdelsområde. Av dem låg 42 420 i flerbostadshus, och 30 598 var bostadsrätter. Bara 337 bostäder ägdes med äganderätt.",
       "Det betyder att ett stambyte i regel är en fråga för en förening. Styrelsen är beställare, och det är föreningen som behöver ha koll på reglerna, medan medlemmarna påverkas i sina egna badrum och kök.",
     ],
     "aside": {"title": "Kungsholmen 2024", "items": [
       "44 554 bostäder", "42 420 i flerbostadshus", "30 598 bostadsrätter"]}},
    {"id": "anmalan-kungsholmen", "h2": "När stambytet kräver anmälan",
     "paras": [
       "Stockholms stad skriver att ett stambyte oftast innebär att befintliga installationer byts i samma läge, och då behövs ingen anmälan. Anmälan och startbesked krävs däremot om VA-stammar placeras i nya lägen eller om stambytet innebär väsentliga ingrepp i byggnadens bärande konstruktion.",
       "Oavsett om anmälan krävs eller inte ska arbetet utföras enligt gällande regler för våtrum och vatteninstallationer. Är ni osäkra på om ett ingrepp är väsentligt för bärigheten bör en konstruktör bedöma det innan projekteringen är klar.",
     ],
     "aside": {"title": "Anmälan krävs om", "items": [
       "VA-stammar placeras i nya lägen", "Väsentliga ingrepp görs i bärande konstruktion"]}},
    {"id": "tillganglighet-kungsholmen", "anchor": "Tillgängligheten",
     "h2": "Tillgängligheten får inte försämras",
     "paras": [
       "Staden påpekar att tillgängligheten inte får försämras vid ett stambyte. Exempel på försämring är att golven i wc eller badrum höjs, att inredning placeras olämpligt eller att dörröppningar blir för smala.",
       "I ett äldre hus är det lätt att golvet växer när nya fall, tätskikt och klinker läggs ovanpå det gamla. Därför planerar vi golvnivåerna tidigt och tar med dem i underlaget som styrelsen och medlemmarna får se.",
     ],
     "aside": None},
    {"id": "imd-kungsholmen", "h2": "Ombyggnad och individuell mätning",
     "paras": [
       "Ett stambyte kan vara en del av en större ombyggnad. Staden förklarar att en ombyggnad innebär att hela eller en betydande och avgränsbar del av byggnaden förnyas på ett påtagligt sätt, och då gäller ansökan eller anmälan hela byggnaden.",
       "Vid en ombyggnad där tappvarmvattnet installeras nytt eller ändras väsentligt ska individuell mätning och debitering, IMD, av tappvarmvatten installeras i befintliga flerbostadshus. Det är en fråga att ta upp redan när omfattningen bestäms.",
     ],
     "aside": None},
    {"id": "boende-kungsholmen", "anchor": "De boende",
     "h2": "De boende under stambytet",
     "paras": [
       "Ett stambyte berör varje lägenhet i huset, och de boende märker det mest. Vi lägger upp arbetet trappuppgång för trappuppgång, så att varje lägenhet står utan badrum så kort tid som möjligt, och styrelsen får en plan som går att dela med medlemmarna i god tid.",
       "Information är halva arbetet. Vi lämnar besked om när vattnet stängs av, när det låter som mest och hur dammet hålls inne. Medlemmar som behöver tillgång till dusch och toalett under tiden får veta i förväg hur det är ordnat.",
     ],
     "aside": {"title": "Det de boende behöver veta", "items": [
       "När arbetet börjar i deras lägenhet", "När vattnet stängs av", "Var dusch och toalett finns under tiden", "Vem de kontaktar"]}},
    {"id": "ansvaret-kungsholmen", "h2": "Vem ansvarar för vad",
     "paras": [
       "Bostadsrättslagen säger att bostadsrättshavaren inte svarar för reparationer av ledningar för avlopp, värme, gas, elektricitet och vatten om föreningen har försett lägenheten med ledningarna och de tjänar fler än en lägenhet. Stammarna är alltså föreningens sak, medan medlemmen håller lägenheten i övrigt i gott skick om inte stadgarna säger annat.",
       "Många medlemmar vill passa på att göra om badrummet efter egen smak när stammarna ändå byts. Vi hjälper föreningen att skilja grundstandard från tillval, så att det blir tydligt vad föreningen betalar och vad medlemmen betalar. Om enskilda badrum kan du läsa under " + _L.format("badrumsrenovering-kungsholmen.html", "badrumsrenovering på Kungsholmen") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi upp ett stambyte på Kungsholmen",
  "steps": [
    ("Platsbesök", "Vi går igenom stammar, schakt och några typlägenheter med styrelsen."),
    ("Omfattning", "Anmälan, bärighet, tillgänglighet och IMD reds ut."),
    ("Underlag till stämman", "Grundstandard och tillval beskrivs så att medlemmarna kan ta ställning."),
    ("Skriftligt kostnadsförslag", "Varje del och varje tillval står för sig."),
    ("Genomförande", "Trappuppgång för trappuppgång, med information till de boende."),
    ("Slutbesiktning", "Intyg och dokumentation lämnas till föreningen."),
  ],
  "rot_h2": "Rotavdrag vid stambyte på Kungsholmen",
  "rot": [
    "Föreningens arbete på stammar och andra gemensamma delar ger inget rotavdrag. Skatteverket ger avdrag i en bostadsrätt bara för arbete inne i bostaden som medlemmen själv ansvarar för.",
    "Bekostar en medlem tillval i sitt eget badrum kan den delen ge avdrag. " + _ROT_BASE,
  ],
  "price_h2": "Vad påverkar kostnaden för ett stambyte på Kungsholmen?",
  "price": [
    "Antalet lägenheter och stammar, om stammarna kan ligga kvar i samma läge, golvnivåerna och omfattningen av tillval. Efter ett gratis platsbesök får styrelsen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vår förening på Kungsholmen göra en anmälan för stambytet?",
     "Inte om installationerna byts i samma läge. Anmälan krävs om stammar placeras i nya lägen eller om bärande konstruktion påverkas väsentligt."),
    ("Får badrumsgolven bli högre efter stambytet?",
     "Tillgängligheten får inte försämras, och staden nämner höjda golv i wc och badrum som ett exempel på försämring."),
    ("Måste vi installera individuell mätning av varmvatten?",
     "Vid en ombyggnad där tappvarmvattnet installeras nytt eller ändras väsentligt ska IMD installeras i befintliga flerbostadshus."),
    ("Kan medlemmarna välja eget kakel och egen inredning?",
     "Ja, om föreningen erbjuder tillval. Vi hjälper styrelsen att skilja grundstandard från tillval, så att varje medlem vet vad som ingår."),
    ("Vem betalar för nya avloppsledningar i lägenheten?",
     "Ledningar som föreningen försett lägenheten med och som tjänar fler än en lägenhet är föreningens ansvar enligt bostadsrättslagen."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Kungsholmens stadsdelsområde (pdf)", _OF + "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade.pdf"),
              _STH_STAM, _STH_OMB, _BRL, _SKV],
  "cta": ("Planerar föreningen stambyte på Kungsholmen?", "Boka ett gratis platsbesök, så går vi igenom huset med styrelsen och tar fram ett skriftligt kostnadsförslag."),
  "img": [
    ("Flerbostadshus från 1930-talet längs en gata",
     "empty quiet street, no pedestrians, no cars: row of 1930s Stockholm functionalist apartment buildings in light rendered facades with small balconies, street trees, Kungsholmen style, daylight" + _IMG_END),
    ("Öppet schakt med nya avloppsstammar i ett badrum",
     "still life inside a stripped bathroom in an old apartment building during pipe replacement: open vertical shaft with new grey plastic waste pipes and copper water pipes, bare concrete floor, work lamp, daylight" + _IMG_END),
    ("Nyrenoverat badrum med låg tröskel och klinker",
     "newly renovated bathroom in an older Stockholm apartment: light grey floor tiles, white wall tiles, wall-hung toilet, walk-in shower with glass screen, low flush threshold at the door, soft daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SÖDERMALM
"byggforetag-sodermalm.html": {
  "kind": "district", "service": "byggforetag", "ort": "Södermalm", "svc_label": "Byggföretag",
  "title": "Byggföretag på Södermalm – inreda vinden till bostäder",
  "description": "Byggföretag på Södermalm: inreda vinden i ett flerbostadshus, bygglov, tillgänglighet och 35-kvadratsundantaget, brandskydd och detaljplanens förbud.",
  "h1": "Byggföretag på Södermalm",
  "lead": "När en bostadsrättsförening på Södermalm vill bygga nya lägenheter är vinden ofta den enda plats som finns kvar. Geal Entreprenad AB bygger vindslägenheter som total entreprenad och hjälper föreningen genom bygglov, brandskydd och projektering.",
  "card": "Inreda vinden till bostäder.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "foreningarna-sodermalm", "anchor": "Södermalms hus",
     "h2": "Bostadsrätter i stenstaden",
     "paras": [
       "Enligt Stockholms stads områdesfakta fanns det 2024 omkring 77 500 bostäder i Södermalms stadsdelsområde. 43 680 av dem var bostadsrätter, och nästan alla låg i flerbostadshus.",
       "För en förening kan en ny vindslägenhet vara ett sätt att finansiera underhåll, men projektet ställer krav på både styrelsen och huset. Staden skriver att möjligheterna beror på byggnadens placering i stadsbilden, dess kulturhistoriska värde och de tekniska förutsättningarna.",
     ],
     "aside": {"title": "Södermalm 2024", "items": [
       "Omkring 77 500 bostäder", "43 680 bostadsrätter"]}},
    {"id": "bygglovet-sodermalm", "h2": "Bygglov för nya bostäder på vinden",
     "paras": [
       "Du behöver bygglov för att inreda ytterligare en bostad i en befintlig byggnad, till exempel när vinden ska inredas. Ibland hör en tillbyggnad eller fasadändring ihop med projektet, till exempel nya takkupor eller fönster.",
       "Finns ett förbud mot vindsinredning i detaljplanen kan bygglov ändå ges för en eller flera nya bostäder om planens genomförandetid har gått ut och övriga förutsättningar är uppfyllda. Stadsmuseets karta visar om huset är klassat, vilket kan påverka hur taket får ändras.",
     ],
     "aside": {"title": "Det här prövas", "items": [
       "Placeringen i stadsbilden", "Kulturhistoriskt värde", "Tekniska förutsättningar", "Detaljplanens bestämmelser"]}},
    {"id": "tillganglighet-sodermalm", "anchor": "Tillgänglighet",
     "h2": "Tillgänglighet och 35-kvadratsregeln",
     "paras": [
       "Nya lägenheter på vinden ska uppfylla krav på tillgänglighet. Staden skriver att byggnadens befintliga förutsättningar i vissa fall kan göra att anpassningar eller undantag godtas, och att endast mindre lägenheter om högst 35 kvadratmeter som inreds på befintlig vind under vissa förutsättningar kan undantas från tillgänglighetskraven.",
       "Planritningen ska visa fast inredning och möbler, så att tillgänglighet och användbarhet kan bedömas för varje våningsplan. Hissen, trappan och storleken på lägenheterna hänger därför ihop redan i det första skissarbetet. Ett hus utan hiss kan till exempel leda till att föreningen väljer flera små lägenheter i stället för en stor, eller att en hiss byggs samtidigt. Vi tar fram alternativen så att styrelsen kan jämföra dem.",
     ],
     "aside": None},
    {"id": "brandskydd-sodermalm", "h2": "Brandskyddet",
     "paras": [
       "En vindsinredning ändrar i regel brandskyddet. Staden förklarar att ändringar i byggnadens brandcellsindelning alltid påverkar brandskyddet, och att nya dörrar i en brandcellsgräns eller ändrade utrymningsvägar är exempel på ändringar som avsevärt påverkar det. Sådana ändringar kräver anmälan och startbesked.",
       "Vi tar in en brandkonsult tidigt, eftersom utrymningen från den nya lägenheten och avskiljningen mot trapphuset styr planlösningen. Staden rekommenderar själv en sakkunnig brandkonsult när man är osäker.",
     ],
     "aside": {"title": "Påverkar brandskyddet", "items": [
       "Ändrad brandcellsindelning", "Nya dörrar i brandcellsgräns", "Ändrade utrymningsvägar", "Brandtekniska installationer"]}},
    {"id": "konstruktionen-sodermalm", "anchor": "Bjälklag och tak",
     "h2": "Bjälklaget, takstolarna och ljudet",
     "paras": [
       "En vind som byggs om till bostad ska bära möbler, människor och nya väggar, och vindsbjälklaget är inte självklart dimensionerat för det. Takstolarna kan behöva förstärkas eller bytas om nya takkupor tas upp, och ljudet mot lägenheterna under måste hållas nere.",
       "Vi tar in en konstruktör som går igenom bjälklag och takstolar innan ritningarna låses. Staden skriver att en kontrollansvarig i vissa projekt behöver anmälas redan vid ansökan, och att den kontrollansvariga ska ha en självständig ställning i förhållande till den entreprenör som utför arbetet. Därför är det föreningen, inte vi, som anlitar den kontrollansvariga.",
     ],
     "aside": {"title": "Konstruktören går igenom", "items": [
       "Vindsbjälklagets bärighet", "Takstolar vid nya takkupor", "Ljud mot lägenheterna under", "Anslutning mot trapphuset"]}},
    {"id": "projektet-sodermalm", "h2": "Vägledningen och projektet",
     "paras": [
       "Staden har en vägledning för vindsinredning, men påpekar att den inte är uppdaterad efter ändringarna i plan- och bygglagen den 1 december 2025. Viss information kan därför vara inaktuell, och vi stämmer av med staden när något är oklart.",
       "Staden uppmanar också till att informera grannar och styrelse om planerna. Vi tar fram ett underlag som styrelsen kan presentera för medlemmarna. Om renovering av befintliga lägenheter kan du läsa under " + _L.format("totalrenovering-sodermalm.html", "totalrenovering på Södermalm") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi upp en vindsinredning på Södermalm",
  "steps": [
    ("Platsbesök", "Vi tittar på vinden, takstolarna, trapphuset och klassningen."),
    ("Förstudie", "Detaljplan, tillgänglighet och brandskydd reds ut."),
    ("Bygglov och anmälan", "Ritningar, brandskyddsbeskrivning och kontrollansvarig tas fram."),
    ("Skriftligt kostnadsförslag", "Varje del av projektet står för sig, som underlag för stämman."),
    ("Byggnation", "Arbetet planeras så att de boende störs så lite som möjligt."),
    ("Slutbesked", "Intyg och dokumentation lämnas till föreningen."),
  ],
  "rot_h2": "Rotavdrag och vindsinredning",
  "rot": [
    "En vindsinredning som föreningen bekostar ger inget rotavdrag. Skatteverket ger avdrag i en bostadsrätt bara för arbete inne i bostaden som medlemmen själv ansvarar för.",
    "Föreningen planerar därför projektet utan rotavdrag. Den som senare köper lägenheten kan få avdrag för egna arbeten i den.",
  ],
  "price_h2": "Vad påverkar kostnaden på Södermalm?",
  "price": [
    "Antalet lägenheter, takets skick, hiss och trappa, brandskyddet och hur mycket fasad och tak ändras. Efter ett gratis platsbesök får styrelsen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vår förening på Södermalm bygglov för att inreda vinden?",
     "Ja, bygglov krävs för att inreda ytterligare bostäder i en befintlig byggnad, till exempel på en vind."),
    ("Detaljplanen förbjuder vindsinredning – är det kört?",
     "Inte nödvändigtvis. Bygglov kan ges trots förbudet om planens genomförandetid har gått ut och övriga förutsättningar är uppfyllda."),
    ("Måste vindslägenheterna vara tillgängliga?",
     "Ja, som huvudregel. Mindre lägenheter om högst 35 kvadratmeter på befintlig vind kan under vissa förutsättningar undantas."),
    ("Klarar vindsbjälklaget en ny lägenhet?",
     "Det kan bara en konstruktör svara på. Bjälklaget och takstolarna gås igenom innan ritningarna låses, och förstärks där det behövs."),
    ("Kan Geal vara kontrollansvarig för vårt projekt?",
     "Nej. Den kontrollansvariga ska ha en självständig ställning i förhållande till den entreprenör som utför arbetet, så föreningen anlitar en egen."),
    ("Behövs en brandkonsult?",
     "Ändringar i brandcellsindelningen påverkar alltid brandskyddet, och staden rekommenderar en sakkunnig brandkonsult vid osäkerhet."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Södermalms stadsdelsområde (pdf)", _OF + "inre-staden/sodermalm/sodermalm-stadsdelsomrade.pdf"),
              _STH_VIND, _STH_BRAND, _STH_KL, _SKV],
  "cta": ("Vill föreningen bygga på vinden på Södermalm?", "Boka ett gratis platsbesök, så går vi igenom vinden och förutsättningarna med styrelsen."),
  "img": [
    ("Takfall med takkupor på ett stenhus i innerstaden",
     "rooftops of early 1900s Stockholm stone apartment buildings with black sheet metal roofs and new dormer windows, chimneys, view over the city on a clear day, Södermalm" + _IMG_END),
    ("Tom vind med synliga takstolar före ombyggnad",
     "empty old attic in a Stockholm apartment building before conversion: exposed wooden roof trusses, old timber floor, small roof windows letting in daylight, dust in the air" + _IMG_END),
    ("Färdig vindslägenhet med snedtak och takfönster",
     "bright newly converted attic apartment with sloping white ceilings, exposed timber beam, roof windows, light oak floor, simple modern kitchen, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VASASTAN
"byggforetag-vasastan.html": {
  "kind": "district", "service": "byggforetag", "ort": "Vasastan", "svc_label": "Byggföretag",
  "title": "Byggföretag i Vasastan – när en lokal blir bostad",
  "description": "Byggföretag i Vasastan: bygga om en lokal till bostad, bygglov för ändrad användning, den senaste faktiska användningen och kraven på den nya bostaden.",
  "h1": "Byggföretag i Vasastan",
  "lead": "I Vasastans stenhus finns butiker, kontor och lager i gatuplanet och källaren, och ibland vill en förening eller fastighetsägare göra om en sådan lokal till bostad. Geal Entreprenad AB bygger om lokaler till bostäder som total entreprenad och börjar med lovfrågan.",
  "card": "När en lokal blir bostad.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "husen-vasastan", "anchor": "Husen i Vasastan",
     "h2": "Bostadsrätter med lokaler i bottenvåningen",
     "paras": [
       "Stockholms stads områdesfakta för 2024 visar att bostadsrätten dominerar. I församlingsområdet Gustav Vasa var 5 707 av omkring 8 900 bostäder bostadsrätter, och i Västra Matteus 8 990 av omkring 12 600.",
       "I husen finns ofta lokaler som föreningen eller fastighetsägaren hyr ut. När en lokal står tom väcks frågan om den kan bli en bostad, men det är en av de ändringar där lovfrågan avgör allt.",
     ],
     "aside": {"title": "Bostadsrätter 2024", "items": [
       "Gustav Vasa: 5 707", "Västra Matteus: 8 990"]}},
    {"id": "andrad-anvandning-vasastan", "h2": "Bygglov för ändrad användning",
     "paras": [
       "Stockholms stad förklarar att du behöver bygglov för att avsevärt ändra användningen av en byggnad eller en del av den. Kravet hänger ihop med om ändringen räknas som väsentlig, och det är en bedömningsfråga. Bygglov kan behövas även om du inte gör några inredningsåtgärder.",
       "Staden ger exempel som alltid kräver bygglov, bland annat förskola till bostad och bostad till kontor. Ska en lokal bli en eller flera bostäder hänger lovplikten dessutom ihop med reglerna om att inreda ytterligare bostad.",
     ],
     "aside": None},
    {"id": "senaste-vasastan", "anchor": "Senaste användningen",
     "h2": "Den senaste faktiska användningen avgör",
     "paras": [
       "Det är den senaste faktiska användningen som avgör om bygglov behövs. Det kan vara en pågående användning eller den senast kända, oberoende av om det fanns bygglov för den.",
       "När du söker ska både den senaste kända användningen och den nya redovisas. Har lokalen varit kontor i tjugo år, trots att den en gång byggdes som bostad, är det alltså kontoret som är utgångspunkten. Vi tar reda på historiken via stadens ritningsarkiv och tidigare ärenden innan ansökan skrivs.",
     ],
     "aside": {"title": "I ansökan", "items": [
       "Senaste kända användning", "Ny användning", "Ritningar och planlösning"]}},
    {"id": "kraven-vasastan", "h2": "Bostaden ska uppfylla dagens krav",
     "paras": [
       "Staden skriver att en ny bostad ska uppfylla dagens krav, till exempel på tillgänglighet, brandsäkerhet, rumshöjd och bostadsutformning. Till bostaden ska det finnas tillgängliga bostadskomplement som lägenhetsförråd, tvättstuga och förvaring för barnvagnar och cyklar.",
       "I en gatuplanslokal blir ljuset, insynen från gatan och ljudet de stora frågorna, och i en källarlokal rumshöjden och fukten. Vi går igenom sådana förutsättningar innan styrelsen lägger pengar på projektering. Ibland visar det sig att lokalen passar bättre för en annan användning, och då är det bra att veta det innan ansökan skickas. Ibland räcker det med mindre ändringar för att en bostad ska fungera riktigt bra.",
     ],
     "aside": None},
    {"id": "grannarna-vasastan", "anchor": "Brand och ljud",
     "h2": "Brand och ljud mot grannarna",
     "paras": [
       "En lokal och en bostad ställer olika krav på avskiljning. Staden förklarar att lägenheter är egna brandceller, och att ändringar i byggnadens brandcellsindelning påverkar brandskyddet och kräver anmälan. När en lokal blir en eller flera bostäder behöver väggar, bjälklag och dörrar mot trapphuset ses över.",
       "Ljudet är den andra frågan. En lokal under en lägenhet är inte självklart byggd för att ljudet mellan två hem ska hållas nere. Vi låter en sakkunnig bedöma brand och ljud tidigt, eftersom de lösningarna styr både planlösning och kostnad.",
     ],
     "aside": {"title": "Ses över i lokalen", "items": [
       "Väggar och bjälklag mot grannar", "Dörren mot trapphuset", "Utrymningsvägar", "Ljud mellan bostäderna"]}},
    {"id": "foreningen-vasastan", "h2": "Föreningens beslut",
     "paras": [
       "Är det föreningen som äger lokalen fattar styrelsen och stämman besluten enligt stadgarna. Vi tar fram ett underlag med lovfrågan, kraven på bostaden och ett kostnadsförslag som styrelsen kan presentera för medlemmarna.",
       "Om att renovera befintliga lägenheter i Vasastan kan du läsa under " + _L.format("totalrenovering-vasastan.html", "totalrenovering i Vasastan") + ", och om badrum under " + _L.format("badrumsrenovering-vasastan.html", "badrumsrenovering i Vasastan") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi upp en ombyggnad från lokal till bostad i Vasastan",
  "steps": [
    ("Platsbesök", "Vi tittar på lokalen, rumshöjden, ljuset och installationerna."),
    ("Lovfrågan", "Senaste användning, ritningar och detaljplan reds ut."),
    ("Ansökan", "Bygglov för ändrad användning med ritningar och kontrollansvarig."),
    ("Skriftligt kostnadsförslag", "Varje del står för sig, som underlag för styrelsen."),
    ("Ombyggnad", "Arbetet startar när startbeskedet finns."),
    ("Slutbesked", "Intyg och dokumentation lämnas inför inflyttningen."),
  ],
  "rot_h2": "Rotavdrag när en lokal blir bostad",
  "rot": [
    "En ombyggnad som föreningen eller fastighetsägaren bekostar ger inget rotavdrag. Skatteverket ger avdrag till privatpersoner för arbete i deras egen bostad.",
    "Den som sedan bor i lägenheten kan få avdrag för egna arbeten i den. " + _ROT_BASE,
  ],
  "price_h2": "Vad påverkar kostnaden i Vasastan?",
  "price": [
    "Lokalens storlek och skick, nya installationer för kök och badrum, ljud och brand mot grannarna och om fasaden ändras. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för att göra om en lokal i Vasastan till bostad?",
     "I regel ja. En väsentlig ändring av användningen kräver bygglov, och nya bostäder kräver bygglov enligt reglerna om att inreda ytterligare bostad."),
    ("Lokalen var en bostad för länge sedan – räcker det?",
     "Nej. Det är den senaste faktiska användningen som avgör, oberoende av om den hade bygglov."),
    ("Vad ska den nya bostaden uppfylla?",
     "Dagens krav på bland annat tillgänglighet, brandsäkerhet, rumshöjd och bostadsutformning, och det ska finnas bostadskomplement."),
    ("Behöver grannarna i huset informeras?",
     "Det är klokt. Ljud och brand mot grannarna påverkas, och i en förening fattas besluten enligt stadgarna av styrelse och stämma."),
    ("Vad är svårast i en källarlokal?",
     "Oftast rumshöjden, dagsljuset och fukten. Dagens krav på rumshöjd och bostadsutformning gäller även för en bostad i en före detta lokal."),
    ("Kan en del av en bostad bli kontor utan bygglov?",
     "Ja, staden nämner del av bostad till kontor för egen verksamhet som exempel på ändring som inte kräver bygglov."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Gustav Vasa (pdf)", _OF + "inre-staden/norra-innerstaden/gustav-vasa.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Västra Matteus (pdf)", _OF + "inre-staden/norra-innerstaden/vastra-matteus.pdf"),
              _STH_ANV, _STH_YTTERL, _STH_BRAND, _SKV],
  "cta": ("Ska en lokal i Vasastan bli bostad?", "Boka ett gratis platsbesök, så går vi igenom lokalen och lovfrågan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Stenhus med lokaler i gatuplanet i innerstaden",
     "completely empty street at early morning, no pedestrians, no people at all, no cars: early 1900s Stockholm stone apartment building with plain blank shop windows at street level without any signs or lettering, ornate facade above, pavement, Vasastan style, daylight" + _IMG_END),
    ("Lokal under ombyggnad med stålpelare, nya träbjälklag och virke på golvet",
     "empty former shop premises in an old Stockholm building before conversion: large street windows, bare concrete floor, exposed pipes along the ceiling, white walls, daylight" + _IMG_END),
    ("Färdig lägenhet i en ombyggd lokal med högt i tak",
     "bright newly converted apartment in a former street-level shop: high ceiling, large windows with sheer curtains, light wooden floor, small modern kitchen along one wall, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERMALM
"byggforetag-ostermalm.html": {
  "kind": "district", "service": "byggforetag", "ort": "Östermalm", "svc_label": "Byggföretag",
  "title": "Byggföretag på Östermalm – slå ihop två lägenheter",
  "description": "Byggföretag på Östermalm: slå ihop två lägenheter, när anmälan krävs, bärande väggar och ofullständiga ritningar, styrelsens tillstånd och klassade hus.",
  "h1": "Byggföretag på Östermalm",
  "lead": "Att slå ihop två lägenheter till en större våning är ett vanligt önskemål på Östermalm. Geal Entreprenad AB tar sådana projekt som total entreprenad och reder ut vad som kräver anmälan, styrelsens tillstånd och en konstruktörs bedömning.",
  "card": "Slå ihop två lägenheter.",
  "sections": [
    {"id": "sammanslagning-ostermalm", "anchor": "Sammanslagningen",
     "h2": "Ingen bygglov, men ofta anmälan",
     "paras": [
       "Stockholms stad skriver att en sammanslagning av flera lägenheter inte kräver bygglov, men att du kan behöva skicka in en anmälan och invänta startbesked. Att dela en lägenhet i två kräver däremot bygglov, eftersom det tillkommer en bostad.",
       "Anmälan krävs för åtgärder som avsevärt påverkar något av de tekniska egenskapskraven. När två lägenheter blir en gäller det i regel bärande konstruktion och brandskydd, och ofta också ventilation och vatten och avlopp.",
     ],
     "aside": {"title": "Anmälan krävs vid ändring av", "items": [
       "Bärande konstruktion", "Brandskydd", "Ventilation", "Vatten och avlopp"]}},
    {"id": "barande-ostermalm", "h2": "Väggen mellan lägenheterna",
     "paras": [
       "Väggen mellan två lägenheter kan vara bärande, och då kräver en öppning i den anmälan. Staden påpekar att ritningar visar byggnadens principiella konstruktion, men att de kan vara ofullständiga och att det inte är säkert att de som byggde följde dem.",
       "Staden kan inte hjälpa dig att bedöma om ett ingrepp påverkar den bärande konstruktionen, utan hänvisar till en konstruktör. Vi tar in en konstruktör innan något öppnas, och öppningen dimensioneras och redovisas i anmälan.",
     ],
     "aside": None},
    {"id": "brandet-ostermalm", "anchor": "Brandskyddet",
     "h2": "Brandskyddet mellan lägenheterna",
     "paras": [
       "Varje lägenhet är en egen brandcell. När två blir en ändras brandcellsindelningen, och staden skriver att sådana ändringar alltid påverkar brandskyddet. En av de två entrédörrarna blir kanske överflödig, och hur den stängs mot trapphuset avgör om avskiljningen fortfarande fungerar.",
       "Vi låter en brandkonsult beskriva lösningen, så att anmälan och kontrollplan stämmer med det som byggs. Hur den dörr som inte längre används som entré ska hanteras avgörs av brandkonsulten innan styrelsen får underlaget. Brandkonsulten beskriver också hur utrymningen ska fungera från den större våningen.",
     ],
     "aside": None},
    {"id": "installationer-ostermalm", "anchor": "Kök och badrum",
     "h2": "Två kök och två badrum blir ett",
     "paras": [
       "När två lägenheter slås ihop blir det ofta ett kök och ett badrum för mycket. Staden skriver att du inte behöver göra en anmälan om du ändrar planlösningen inom en lägenhet och inga tekniska egenskapskrav påverkas, till exempel om du flyttar eller bygger ut kök eller badrum.",
       "Anmälan krävs däremot vid installation eller väsentlig ändring av ventilationssystem, och när vatten och avlopp ändras väsentligt eller installeras nytt. Ett kök som tas bort betyder att ventilation, avlopp och vatten ska pluggas eller byggas om på rätt sätt, och det behöver planeras tillsammans med föreningen eftersom stammarna är gemensamma.",
     ],
     "aside": {"title": "Ingen anmälan om", "items": [
       "Kök eller badrum flyttas inom lägenheten", "Rummens användning ändras", "Inga tekniska egenskapskrav påverkas"]}},
    {"id": "styrelsen-ostermalm", "h2": "Styrelsens tillstånd",
     "paras": [
       "Bostadsrättslagen säger att bostadsrättshavaren inte får utföra vissa åtgärder utan styrelsens tillstånd. Det gäller ingrepp i bärande konstruktion, installation eller ändring av ledningar för avlopp, värme, gas eller vatten, ändring av ventilation, ändring av eldstad eller rökkanal och annan väsentlig förändring av lägenheten.",
       "En sammanslagning omfattar normalt flera av punkterna. Vi tar fram ett underlag med ritningar, konstruktörens bedömning och brandskyddet, så att styrelsen har något konkret att ta ställning till.",
     ],
     "aside": {"title": "Kräver styrelsens tillstånd", "items": [
       "Ingrepp i bärande konstruktion", "Ändrade ledningar för avlopp, värme, gas eller vatten", "Ändrad ventilation", "Ändrad eldstad eller rökkanal"]}},
    {"id": "klassat-ostermalm", "h2": "Klassade hus",
     "paras": [
       "Stadsmuseets karta visar om huset är blå- eller grönklassat. Boverket förklarar att förvanskningsförbudet gäller vid alla ändringar, såväl exteriört som interiört, och oberoende av om åtgärden kräver lov eller anmälan. Stuckatur, kakelugnar och originalsnickerier i de rum som slås ihop ska därför tas om hand.",
       "Om renovering av rummen efteråt kan du läsa under " + _L.format("badrumsrenovering-ostermalm.html", "badrumsrenovering på Östermalm") + " och " + _L.format("golvslipning-ostermalm.html", "golvslipning på Östermalm") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så slår vi ihop två lägenheter på Östermalm",
  "steps": [
    ("Platsbesök", "Vi tittar på båda lägenheterna, väggen mellan dem och husets klassning."),
    ("Konstruktör och brandkonsult", "Öppningen och brandskyddet bedöms och beskrivs."),
    ("Underlag till styrelsen", "Ritningar och beskrivningar för styrelsens tillstånd."),
    ("Anmälan", "Kontrollplan och handlingar skickas in för startbesked."),
    ("Ombyggnad", "Arbetet startar när tillstånd och startbesked finns."),
    ("Slutbesked", "Intyg och kontrollplan samlas inför slutbeskedet."),
  ],
  "rot_h2": "Rotavdrag när lägenheter slås ihop på Östermalm",
  "rot": [
    _ROT_BASE,
    "Skatteverket ger rotavdrag för att bygga om en bostadsrätt, för arbete inne i bostaden som du ansvarar för. För arbete som ger avdrag drar Geal det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden på Östermalm?",
  "price": [
    "Öppningen i den bärande väggen, brandskyddet, hur mycket installationer som flyttas och hur rummen ska renoveras. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för att slå ihop två lägenheter på Östermalm?",
     "Nej, en sammanslagning kräver inte bygglov, men ofta en anmälan och startbesked eftersom bärande konstruktion och brandskydd påverkas."),
    ("Kan vi lita på de gamla ritningarna?",
     "Inte helt. Ritningar kan vara ofullständiga, och det är inte säkert att de som byggde följde dem. En konstruktör bör bedöma väggen."),
    ("Behöver vi styrelsens tillstånd?",
     "Ja, för bland annat ingrepp i bärande konstruktion och ändrade ledningar och ventilation enligt bostadsrättslagen."),
    ("Hur lång tid tar det innan vi kan börja?",
     "Det beror på när styrelsens tillstånd och startbeskedet finns. Vi tar fram underlagen parallellt så att ingen del väntar i onödan."),
    ("Vad händer med det överflödiga köket?",
     "Det kan rivas eller göras om till ett annat rum. Ändras ventilation eller vatten och avlopp väsentligt krävs anmälan, och styrelsen behöver ge tillstånd."),
    ("Vårt hus är blåklassat – vad betyder det inne i lägenheten?",
     "Förvanskningsförbudet gäller även interiört, så originaldetaljer som stuckatur och snickerier ska tas om hand."),
  ],
  "sources": [_STH_YTTERL, _STH_PLAN, _STH_BAR, _STH_BRAND, _BRL, _STH_KL, _BV_FORV, _SKV],
  "cta": ("Vill ni slå ihop två lägenheter på Östermalm?", "Boka ett gratis platsbesök, så går vi igenom lägenheterna och vad som krävs innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Ståndsmässigt stenhus med burspråk på Östermalm",
     "empty quiet street, no pedestrians, no cars: grand late 1800s Stockholm stone apartment building with bay windows, wrought iron balconies and ornate light facade, tall trees, Östermalm, daylight" + _IMG_END),
    ("Stålbalkar och nya träbjälkar i ett bjälklag under ombyggnad, virke staplat på golvet",
     "still life inside an old apartment during renovation: newly made wide opening in a thick interior wall with a steel beam above and temporary timber props, protective floor covering on parquet, daylight" + _IMG_END),
    ("Sammanslagen våning med öppen dubbeldörr och stuckatur",
     "large bright apartment in an old Stockholm building after two flats were joined: enfilade of rooms with tall double doors open, ornate white plaster ceiling cornices, herringbone parquet, tiled stove in the corner, daylight" + _IMG_END),
  ],
},
}
