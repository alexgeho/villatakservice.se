# -*- coding: utf-8 -*-
"""Fönsterrenovering – ortsidor v28: Botkyrka, Ekerö, Farsta, Hässelby, Kista, Skärholmen (2026-10-27).
Deltjänst under fonsterbyte.html (TJ_HUB["fonsterrenovering"]). Intent: renovera de befintliga fönstren (kitt,
linoljefärg, bågar, beslag, tätning, tillsatsruta/innerbåge) i stället för att byta dem. Skild från ortens
fonsterbyte-<ort>.html (Botkyrka, Ekerö, Farsta, Hässelby) och från v16/v19/v21/v24-sidorna.

Lokal vinkel per sida:
Botkyrka – radhusen i Tuna (kulturmiljöprogrammet: tidigt 1960-tal, välbevarade radhus söder om Lindhovsvägen med tegel
  och trä och enkelt sakligt formspråk; riktlinjen att ursprungliga dörrar och fönster bibehålls), RAÄ om synliga mått
  och proportioner i modernare hus, Botkyrkas sida om fasadändring (fönster som fasadändring, utökad lovplikt).
Ekerö – Ralph Erskines Ekerö centrum (invigt 1991, billiga material och rationella metoder, variation i skala och färg)
  och kulturmiljöprogrammets råd om att respektera fönster, panel, entréer och räcken i både flerfamiljshus och villa-
  och sportstugebebyggelse; Närlunda med villor från 1960-talet och Väsby från tidigt 1970-tal; RAÄ om besiktning.
Farsta – småstugorna i Svedmyra (Stockholms spår: byggda från 1931–33 av självbyggare med monteringsfärdigt material,
  locklistpanel, ädelputsade stugor på 1950-talet), Svedmyra och Sköndal i Varsam-tabellen, områdesfakta, RAÄ om
  funktionalismens kopplade inåtgående bågar utan spröjs och om okopplade fönster i egnahemmen ännu på 1920-talet.
Hässelby – radhusen vid Astrakangatan och Friherregatan (Småstugebyrån 1957, sidiplattor och invaritplattor,
  Stockholms spår), Hässelby gård som tunnelbanestad och värdefull miljö (Varsam), områdesfakta, RAÄ om att
  linoljefärg ännu på 1950-talet föreskrevs för utvändiga snickerier.
Kista – fönstren i 1970-talets radhus (Kista 1975–80, Stockholms spår; ägarformer i områdesfakta), Stockholms lista över
  fönsterändringar som kan kräva lov (upphängning, indelning, profilering), RAÄ om tätningslister och tillsatsrutor,
  vem som ansvarar i bostadsrätt (bostadsrättslagen) och ROT.
Skärholmen – miljonprogrammets radhus i Sätra, Bredäng och Vårberg (Varsam: rationellt och industriellt byggande,
  enhetliga husgrupper, Bredäng värdefull), alla småhus med äganderätt (områdesfakta), RAÄ om besiktning av varje fönster
  och om att det framför allt är synliga mått och proportioner som ska bevaras i modernare hus.

Fakta endast från källorna i respektive 'sources', öppnade med urllib (Mozilla-UA) 2026-10-27, alla 200 utom
Skatteverket (återställd anslutning – samma adresser och ROT-meningar som v23–v25). Pdf:erna (RAÄ Fönster 1988,
Varsam, områdesfakta, Stockholms spår, Botkyrkas och Ekerös kulturmiljöprogram) har textlager.
Strukna / ej använda: U-värden, vilka fönstertyper som sitter i enskilda Kista- och Skärholmenhus (ingen källa – skrivet
som något vi tar reda på), avgifter, handläggningstider, priser, omdömen, egna uppdrag i orterna och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no hands, no text, no letters"

_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"
_STH_FON = ("Stockholms stad – Fönster och dörrar", _SB + "fonster-och-dorrar/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_RAA_FON = ("Riksantikvarieämbetet – Fönster. Historik och råd vid renovering (pdf)", "https://www.raa.se/publicerat/9789172095892.pdf")
_RAA_MAL = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf)", "https://www.raa.se/publicerat/9789172095830.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 och 12 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_ROT_AMT = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
            "tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.")
_ROT_FON = ("Reparation och målning av fönster på ett småhus som du äger och bor i räknas som rotarbete hos Skatteverket. "
            "Avdraget gäller arbetskostnaden.")

PAGES_TJ = {

# ------------------------------------------------------------------ BOTKYRKA
"fonsterrenovering-botkyrka.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Botkyrka", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Botkyrka – radhusen i Tuna",
  "description": "Fönsterrenovering i Botkyrka: de välbevarade radhusen i Tuna, riktlinjen att ursprungliga fönster ska behållas och hur fönstren görs tätare.",
  "h1": "Fönsterrenovering i Botkyrka",
  "lead": "För radhusen i Tuna skriver Botkyrka kommun i klartext att de ursprungliga dörrarna och fönstren ska behållas. Det gör fönsterrenovering till det naturliga valet när fönstren börjar bli slitna. Geal Entreprenad AB renoverar fönster på radhus och villor i Botkyrka och utgår från de fönster som redan sitter i huset.",
  "card": "Radhusen i Tuna.",
  "sections": [
    {"id": "tuna-botkyrka", "anchor": "Tuna",
     "h2": "Tidigt 1960-tal med hög kvalitet",
     "paras": [
       "Botkyrkas kulturmiljöprogram beskriver Tuna som representativt för det tidiga 1960-talets bebyggelse med hög kvalitet i gestaltning och genomförande. Området planerades under sent 1950-tal och byggdes ut i början av 1960-talet som en grannskapsenhet med villor, radhus, skola, torg och kyrka.",
       "Bland småhusen lyfter programmet fram radhusområdet söder om Lindhovsvägen som välbevarad radhusbebyggelse med hög arkitektonisk kvalitet. Karaktäristiskt är kombinationen av tegel och trä i fasaderna och det enkla, sakliga formspråket.",
     ],
     "aside": {"title": "Radhusen i Tuna", "items": [
       "Söder om Lindhovsvägen", "Tegel och trä i fasaderna", "Enkelt, sakligt formspråk", "Hög arkitektonisk kvalitet"]}},
    {"id": "riktlinjen-botkyrka", "h2": "Ursprungliga fönster bibehålls",
     "paras": [
       "Kulturmiljöprogrammets riktlinje för radhusen i Tuna säger att bebyggelsens tidstypiska karaktär ska värnas, att ursprungliga dörrar och fönster ska bibehållas och att det enkla, sakliga formspråket ska respekteras. I ett område med så tydliga linjer märks ett avvikande fönster direkt.",
       "Riksantikvarieämbetet skriver att det i modernare hus framför allt är fönstrens synliga mått och proportioner som är viktiga att bevara. Vid en renovering behåller vi därför karm, bågar och indelning och lagar det som är skadat, i stället för att ersätta fönstret med något som bara liknar det.",
     ],
     "aside": None},
    {"id": "fasadandring-botkyrka", "h2": "När ett fönsterarbete blir en fasadändring",
     "paras": [
       "Botkyrka kommun skriver att en fasadändring kan vara att byta eller sätta in nya fönster, och att ett byte av kulör också räknas dit. Utökad lovplikt kan gälla för fasadändringar i områden som är särskilt värdefulla, och kommunen hänvisar till webbkartans lager Kulturmiljöprogram för att se vilka områden som berörs.",
       "En renovering där fönstret lagas och målas i samma kulör ändrar inte husets utseende. Ska bågarna få en annan kulör eller ska något i fönstret ändras kontrollerar vi kartan och detaljplanen först. Om fönsterbyten i kommunen kan du läsa under " + _L.format("fonsterbyte-botkyrka.html", "fönsterbyte i Botkyrka") + ".",
     ],
     "aside": {"title": "Kontrollera i webbkartan", "items": [
       "Lagret Kulturmiljöprogram", "Lagret Detaljplaner", "Lagret Kulturmiljövård under Riksintressen"]}},
    {"id": "tatare-botkyrka", "h2": "Tätare utan att byta",
     "paras": [
       "Riksantikvarieämbetet påpekar att två vanliga skäl för att byta gamla fönster är att värme- och ljudisoleringen ska förbättras, men att det finns andra och billigare lösningar. Moderna tätningslister ger en avsevärd förbättring av både ljud- och värmeisolering, och det är innerbågen, inte ytterbågen, som ska tätas.",
       "Fönstret ska målas och justeras innan listerna sätts upp, och en för tjock list gör fönstret svårstängt och kan ge spänningar som skadar båge och glas. Vi mäter springan innan listtypen väljs.",
     ],
     "aside": None},
    {"id": "arbetet-botkyrka", "h2": "Arbetet fönster för fönster",
     "paras": [
       "Riksantikvarieämbetet råder att arbetet inleds med en systematisk besiktning av varje fönster för sig när det är osäkert om fönstren behöver vanligt underhåll eller större reparationer. Utan besiktning är det enligt myndigheten alltför lätt att döma ut fönster som mycket väl går att bevara.",
       "Ofta är det bottenstyckena i karm och båge som skadats, och då går det i regel att byta bara de skadade partierna. Ibland måste en båge nytillverkas, men myndigheten påpekar att ett kontinuerligt underhåll minskar behovet av större ingrepp i framtiden. Om måleri i Botkyrka i övrigt kan du läsa under " + _L.format("malare-botkyrka.html", "målare i Botkyrka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Botkyrka till",
  "steps": [
    ("Besiktning", "Varje fönster bedöms för sig: kitt, färg, trä och beslag."),
    ("Webbkartan", "Kulturmiljöprogram och detaljplan kontrolleras om något ska ändras."),
    ("Skriftligt kostnadsförslag", "Fönster för fönster, med lagningar och tätning för sig."),
    ("Renovering", "Skrapning, lagning av skadade delar, kittning och målning."),
    ("Tätning och justering", "Bågarna justeras och innerbågen tätas."),
    ("Genomgång", "Vi går igenom fönstren och hur de sköts framåt."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Botkyrka",
  "rot": [_ROT_FON, _ROT_AMT],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Botkyrka?",
  "price": [
    "Antal fönster och bågar, hur mycket kitt och färg som behöver tas bort, lagningar av trä, beslag och tätning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste de gamla fönstren i vårt radhus i Tuna behållas?",
     "Botkyrkas kulturmiljöprogram har riktlinjen att ursprungliga dörrar och fönster i Tunas radhus ska bibehållas och att det enkla, sakliga formspråket ska respekteras."),
    ("Var ligger de välbevarade radhusen i Tuna?",
     "Kulturmiljöprogrammet lyfter fram radhusområdet söder om Lindhovsvägen, med fasader i tegel och trä."),
    ("Vad är viktigast att bevara i ett fönster från 1960-talet?",
     "Enligt Riksantikvarieämbetet är det i modernare hus framför allt fönstrens synliga mått och proportioner som är viktiga att bevara."),
    ("Räknas det som fasadändring att måla fönsterbågarna i en ny kulör i Botkyrka?",
     "Ett byte av kulör räknas som fasadändring enligt Botkyrka kommun. I områden med utökad lovplikt kan det kräva lov."),
    ('När byggdes bostadsområdet Tuna?',
     'Enligt Botkyrkas kulturmiljöprogram planerades Tuna under sent 1950-tal och byggdes ut i början av 1960-talet.'),
  ],
  "sources": [("Botkyrka kommun – Kulturmiljöprogram (pdf)", "https://www.botkyrka.se/download/18.1fbbaae6170bff9469deb7f/1602575505534/Kulturmilj%C3%B6program.pdf"),
              ("Botkyrka kommun – Fasadändring", "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/fasadandring"),
              _RAA_FON, _SKV, _SKV2],
  "cta": ("Ska fönstren i Botkyrka renoveras?", "Boka ett gratis platsbesök, så besiktigar vi fönstren ett och ett innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus från tidigt 1960-tal i tegel och trä",
     "row of early 1960s Swedish terraced houses with a combination of brick walls and dark wooden panels, simple clean geometric lines, original wooden windows, small front gardens, suburb south of Stockholm, summer" + _IMG_END),
    ("Gammal fönsterbåge på en arbetsbänk inför renovering",
     "still life in an empty workshop: a 1960s wooden window sash lying on trestles, fresh putty along the glass edge, old paint scraped from the frame, putty knife and paint tin on the bench beside it, daylight" + _IMG_END),
    ("Innerbåge med tätningslist i falsen",
     "close view of the inner sash rebate of an old wooden window with a new dark rubber weatherstrip fitted, freshly painted white frame, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ EKERÖ
"fonsterrenovering-ekero.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Ekerö", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering på Ekerö – Erskines centrum och villorna",
  "description": "Fönsterrenovering på Ekerö: Ralph Erskines Ekerö centrum från 1991, kulturmiljöprogrammets råd om fönster och villorna i Närlunda och Väsby.",
  "h1": "Fönsterrenovering på Ekerö",
  "lead": "Ekerös kulturmiljöprogram ger samma råd för flerfamiljshusen i Ekerö centrum som för villorna och sportstugorna: fönster, panel, entréer och räcken ska respekteras. Geal Entreprenad AB renoverar fönster på villor, radhus och flerbostadshus på Ekerö och lagar det som går att laga innan något byts.",
  "card": "Erskines centrum och villorna.",
  "sections": [
    {"id": "centrum-ekero", "anchor": "Ekerö centrum",
     "h2": "Ett av landets yngsta kommuncentrum",
     "paras": [
       "Enligt Ekerös kulturmiljöprogram gick uppdraget att utforma Ekerö centrum till arkitekten Ralph Erskine, som ville skapa ny god arkitektur med sociala ambitioner: en småstad intill Mälaren med verksamheter i bottenvåningarna och bostäder för alla. Centrum invigdes 1991 och är ett av landets yngsta kommuncentrum.",
       "Programmet beskriver gestaltningen med variation i skala och färgsättning, och skriver att billiga material och rationella byggmetoder användes för att hålla nere kostnaderna. Husen är i varierad höjd med varierande uttryck och kulörer.",
     ],
     "aside": {"title": "Ekerö centrum", "items": [
       "Arkitekt Ralph Erskine", "Invigt 1991", "Variation i skala och färg", "Billiga material, rationella metoder"]}},
    {"id": "radet-ekero", "h2": "Kulturmiljöprogrammets råd om fönstren",
     "paras": [
       "Bland råden för tätorten skriver kulturmiljöprogrammet att byggnaders individuella arkitektur och tidstypiska drag ska respekteras, och att befintliga byggnader bör respekteras när det gäller proportioner, fasadfärg, tak och byggnadsdetaljer som fönster, panel, entréer och räcken. Rådet gäller såväl flerfamiljshusen i Ekerö centrum som villa- och sportstugebebyggelsen.",
       "För en förening eller en villaägare betyder det att ett fönster som renoveras och behåller sina mått, sin indelning och sin kulör ligger i linje med programmet, medan ett byte till en annan typ behöver övervägas noggrannare.",
     ],
     "aside": {"title": "Ska respekteras enligt programmet", "items": [
       "Proportioner", "Fasadfärg och tak", "Fönster och panel", "Entréer och räcken"]}},
    {"id": "villorna-ekero", "h2": "Närlunda, Väsby och de omvandlade sommarhusen",
     "paras": [
       "Kulturmiljöprogrammet beskriver villa- och radhusbebyggelse från andra halvan av 1900-talet som det dominerande inslaget på östra Ekerö, med Väsby och dess enhetliga bebyggelse från tidigt 1970-tal och Närlunda som domineras av villor från 1960-talet. I Älvnäs, Gällstaö och Erikssten har sommarbostäder permanentats, och sommarvillor och sportstugor har byggts om eller rivits.",
       "Fönster från så olika tider kräver olika bedömningar. Ett okopplat fönster i en gammal sommarvilla, ett kopplat fönster i en 60-talsvilla och ett fönster i ett 90-talshus i centrum lagas på olika sätt. Om fönsterbyten på Ekerö kan du läsa under " + _L.format("fonsterbyte-ekero.html", "fönsterbyte på Ekerö") + ".",
     ],
     "aside": None},
    {"id": "besiktning-ekero", "h2": "Besiktning före beslut",
     "paras": [
       "Riksantikvarieämbetet skriver att ett fönster utsätts för påfrestningar som liknar dem en båt utsätts för, och att kitt, målning och beslag fortlöpande måste hållas i gott skick. När det är osäkert om fönstren behöver vanligt underhåll eller större reparationer råder myndigheten att man börjar med att besiktiga och analysera varje fönster för sig.",
       "En sådan inventering ger enligt myndigheten underlag för en mer exakt kostnadsberäkning, och utan den är det lätt att döma ut fönster som går att bevara. För en förening i centrum blir besiktningen också underlaget för styrelsens beslut. Myndigheten beskriver underhåll, reparation, komplettering och nytillverkning som olika nivåer av byggnadsvård, och besiktningen visar vilken nivå varje fönster behöver.",
     ],
     "aside": None},
    {"id": "verkstad-ekero", "h2": "Bågarna kan renoveras i verkstad",
     "paras": [
       "Riksantikvarieämbetet påpekar att målningsarbetet med dagens metoder ofta kan göras i en verkstad. Då kan fönsterrenovering göras även vintertid, och resultatet blir enligt myndigheten av högre och jämnare kvalitet.",
       "När bågarna tas ner sätter vi upp ett tillfälligt skydd i karmen. Om måleri på Ekerö i övrigt kan du läsa under " + _L.format("malare-ekero.html", "målare på Ekerö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering på Ekerö till",
  "steps": [
    ("Besiktning", "Varje fönster bedöms för sig och resultatet sammanställs."),
    ("Skriftligt kostnadsförslag", "Fönster för fönster, med lagningar och målning för sig."),
    ("Planering", "Vi bestämmer om bågarna renoveras på plats eller i verkstad."),
    ("Renovering", "Skrapning, lagning, kittning och målning med samma kulör."),
    ("Tätning och justering", "Bågarna justeras och tätas mot karmen."),
    ("Genomgång", "Vi går igenom fönstren med dig eller styrelsen."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering på Ekerö",
  "rot": [_ROT_FON + " I en bostadsrätt beror avdraget på vad bostadsrättshavaren ansvarar för enligt stadgarna.", _ROT_AMT],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen på Ekerö?",
  "price": [
    "Antal fönster, skador på trä och kitt, om bågarna renoveras i verkstad, beslag och tätning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem ritade Ekerö centrum?",
     "Arkitekten Ralph Erskine, enligt Ekerös kulturmiljöprogram. Centrum invigdes 1991 och är ett av landets yngsta kommuncentrum."),
    ("Gäller kulturmiljöprogrammets råd om fönster även flerfamiljshusen i Ekerö centrum?",
     "Ja, programmet skriver att rådet om att respektera proportioner, fasadfärg, tak och detaljer som fönster gäller såväl flerfamiljshusen i centrum som villa- och sportstugebebyggelsen."),
    ("Från vilket årtionde är villorna i Närlunda?",
     "Kulturmiljöprogrammet beskriver Närlunda som dominerat av villor från 1960-talet."),
    ("Kan föreningens fönster renoveras på vintern?",
     "Ja, om bågarna tas till en verkstad. Riksantikvarieämbetet påpekar att målningsarbetet då kan göras även vintertid."),
    ('Vilka tidigare sommarhusområden på östra Ekerö har blivit åretruntboende?',
     'Kulturmiljöprogrammet nämner Älvnäs, Gällstaö och Erikssten som områden där sommarbostäder har permanentats och förtätats.'),
  ],
  "sources": [("Ekerö kommun – Kulturmiljöprogram 2015 (pdf)", "https://www.ekero.se/download/18.553838ea17305720c321ec82/1597925412772/Eker%C3%B6%20kulturmilj%C3%B6program.pdf"),
              _RAA_FON, _SKV, _SKV2],
  "cta": ("Ska fönstren på Ekerö renoveras?", "Boka ett gratis platsbesök, så besiktigar vi fönstren innan du eller föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Färgglada bostadshus i varierad höjd vid Mälaren",
     "empty street, no pedestrians: late 1980s Scandinavian small town centre with playful postmodern apartment buildings of varied heights, wooden details, varied pastel facade colours, many wooden windows and balconies, lake Mälaren nearby, daylight" + _IMG_END),
    ("Villa från 1960-talet med träfönster",
     "1960s Swedish detached villa with light brick and wooden facade, original wooden casement windows, low pitched roof, lawn and pine trees, island suburb west of Stockholm, summer" + _IMG_END),
    ("Fönsterbågar staplade i en verkstad",
     "still life in an empty joinery workshop: several old wooden window sashes stacked upright on a rack, some stripped of paint and some freshly primed, workbench in the background, soft daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ FARSTA
"fonsterrenovering-farsta.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Farsta", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Farsta – småstugorna i Svedmyra",
  "description": "Fönsterrenovering i Farsta: Svedmyras småstugor från 1930-talet, Svedmyra och Sköndal i stadens strategi, funkisfönster och kopplade bågar.",
  "h1": "Fönsterrenovering i Farsta",
  "lead": "Svedmyras småstugor byggdes på 1930-talet av familjer som själva satte ihop husen av monteringsfärdigt material, och många har kvar fönster från den tiden. De fönstren går ofta att renovera. Geal Entreprenad AB renoverar fönster på småstugor, radhus och villor i Farsta och utgår från de bågar som redan sitter i huset.",
  "card": "Småstugorna i Svedmyra och Sköndal.",
  "sections": [
    {"id": "svedmyra-farsta", "anchor": "Svedmyra",
     "h2": "Småstugor byggda av självbyggare",
     "paras": [
       "Enligt Stadsmuseets skrift om Svedmyra i serien Stockholms spår byggdes stadsdelen ut med småstugor från åren 1931–33. Småstugan var ett alternativ för familjer som inte kunde betala en kontantinsats men kunde bidra med eget arbete, och staden stod för organisation och gav genom Småstugebyrån både instruktioner och byggmaterial.",
       "Materialet var monteringsfärdigt, och väggar och takstolar lyftes på plats i stora element för att hålla nere kostnaderna. Till den tidiga småstugekaraktären hör trähusfasadernas locklistpaneler och de röda tegeltaken, och i områdets östra del kompletterades bebyggelsen på 1950-talet med ädelputsade småstugor i dämpade gråtoner. De enkla en- och tvåvåningsstugorna ligger något indragna från gatorna, på rad efter varandra.",
     ],
     "aside": {"title": "Svedmyra enligt Stockholms spår", "items": [
       "Småstugor från 1931–33", "Monteringsfärdigt material", "Locklistpanel och rött tegel", "Ädelputsade stugor på 1950-talet"]}},
    {"id": "tabellen-farsta", "h2": "Svedmyra och Sköndal i stadens strategi",
     "paras": [
       "I tabellen i stadens strategi Varsam är del av Svedmyra och del av Sköndal markerade som kulturhistoriskt värdefulla småstugeområden, liksom Tallkrogen. Stockholms stad skriver att ändringar av fönster, som ny kulör, ändrad indelning eller andra profiler, kan kräva bygglov beroende på byggnaden, och att utökad lovplikt gäller i särskilt värdefulla områden.",
       "Stadens områdesfakta för 2025 visar 327 småhus med äganderätt i Svedmyra och 1 194 i Sköndal. I hela Farsta stadsdelsområde finns 3 806 småhus med äganderätt.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Svedmyra: 327", "Sköndal: 1 194", "Farsta stadsdelsområde: 3 806"]}},
    {"id": "fonstren-farsta", "h2": "Fönster från funktionalismens början",
     "paras": [
       "Riksantikvarieämbetet beskriver hur funktionalismen introducerades som arkitektonisk stil omkring 1930, och hur de onödiga spröjsarna då försvann ur de nu oftast inåtgående kopplade fönsterbågarna. Det blev vanligt med ett-, två- eller treluftsfönster beroende på rummets storlek, och fönstersnickeriernas profiler förenklades.",
       "Myndigheten påpekar också att de traditionella okopplade fönstren fortfarande var vanliga i förorternas egnahemsbebyggelse vid slutet av 1920-talet. Vilken typ som sitter i just din småstuga tar vi reda på vid besiktningen, eftersom kopplade och okopplade bågar lagas och tätas olika.",
     ],
     "aside": None},
    {"id": "kopplade-farsta", "h2": "Kopplade bågar som kärvar",
     "paras": [
       "Riksantikvarieämbetet skriver att äldre kopplade bågar kan vara besvärligare än okopplade: de är ofta stora och tunga, kan sluta dåligt mot karmen och kan ha igengrodda kopplingsbeslag och skevheter. För att göra fönstren lättare att manövrera kan nya handtag och stängningsbeslag behövas.",
       "Myndigheten råder att gamla fönsterbeslag sparas, eftersom det ofta är svårt att få tag på beslag av äldre typ som passar. Vi rengör och justerar de beslag som finns och sparar de som byts. Om fönsterbyten i Farsta kan du läsa under " + _L.format("fonsterbyte-farsta.html", "fönsterbyte i Farsta") + ".",
     ],
     "aside": {"title": "Vanliga fel enligt RAÄ", "items": [
       "Tunga bågar som inte sluter tätt", "Igengrodda kopplingsbeslag", "Skeva bågar"]}},
    {"id": "linolja-farsta", "h2": "Linoljefärg och kitt",
     "paras": [
       "Riksantikvarieämbetet rekommenderar linoljefärg vid målning av fönster, både vid renovering och nymålning, eftersom den tränger in i virket och fäster bra, medan latexfärger lägger sig som en film på ytan och ofta ger underhållsproblem. Fönstrens underhåll består i första hand av ommålning och kittning.",
       "Om måleri på småstugorna i Farsta kan du läsa under " + _L.format("malare-farsta.html", "målare i Farsta") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Farsta till",
  "steps": [
    ("Besiktning", "Fönstertyp, kitt, färg och beslag bedöms fönster för fönster."),
    ("Kartan", "Stadsmuseets karta kontrolleras om något i fönstret ska ändras."),
    ("Skriftligt kostnadsförslag", "Lagningar, beslag och målning redovisas för sig."),
    ("Renovering", "Skrapning, lagning, kittning och linoljefärg."),
    ("Beslag och tätning", "Beslag rengörs och justeras, innerbågen tätas."),
    ("Genomgång", "Vi går igenom fönstren och visar hur de sköts."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Farsta",
  "rot": [_ROT_FON, _ROT_AMT],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Farsta?",
  "price": [
    "Antal fönster och bågar, om de är kopplade, skador på trä och kitt, beslag och tätning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("När byggdes småstugorna i Svedmyra?",
     "Enligt Stadsmuseets skrift i serien Stockholms spår började Svedmyra byggas ut med småstugor åren 1931–33."),
    ("Är Sköndal ett kulturhistoriskt värdefullt område?",
     "I stadens strategi Varsam är del av Sköndal markerad som kulturhistoriskt värdefullt småstugeområde. Stadsmuseets karta visar vad som gäller för din fastighet."),
    ("Varför saknar fönstren i vår småstuga spröjs?",
     "Riksantikvarieämbetet beskriver hur funktionalismen omkring 1930 tog bort spröjsarna i de nu oftast inåtgående kopplade bågarna."),
    ("Ska vi kasta de gamla fönsterbeslagen när fönstret renoveras?",
     "Nej. Riksantikvarieämbetet råder att gamla fönsterbeslag sparas, eftersom passande beslag av äldre typ ofta är svåra att få tag på."),
    ('Vem hjälpte självbyggarna som byggde småstugorna i Svedmyra?',
     'Staden stod för organisationen och gav genom Småstugebyrån både instruktioner och byggnadsmaterial, enligt Stadsmuseets skrift i serien Stockholms spår.'),
  ],
  "sources": [("Stockholms stadsmuseum – Stockholms spår: Svedmyra (pdf)", "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000043.pdf"),
              _VARSAM,
              ("Stockholms stad – Områdesfakta 2025: Svedmyra (pdf)", _OF + "soderort/farsta/svedmyra.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Sköndal (pdf)", _OF + "soderort/farsta/skondal.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Farsta stadsdelsområde (pdf)", _OF + "soderort/farsta/farsta-stadsdelsomrade.pdf"),
              _STH_FON, _STH_KL, _RAA_FON, _SKV, _SKV2],
  "cta": ("Ska fönstren i Farsta renoveras?", "Boka ett gratis platsbesök, så besiktigar vi fönstren innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Småstuga med locklistpanel och rött tegeltak",
     "1930s Swedish small cottage with vertical board-and-batten wooden facade painted pale yellow, red clay tile roof, simple white wooden windows without glazing bars, small garden with apple tree and hedge, quiet street, Stockholm suburb, summer" + _IMG_END),
    ("Tvåluftsfönster i vitmålat trä på en småstuga",
     "close view of an open pair of old coupled inward-opening wooden window sashes with the coupling hardware between them, white paint, daylight from outside" + _IMG_END),
    ("Gamla fönsterbeslag rengjorda på en arbetsbänk",
     "still life: old window hinges, stays and latches cleaned and laid out in a row on a wooden workbench next to a window sash, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HÄSSELBY
"fonsterrenovering-hasselby.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Hässelby", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Hässelby – radhusen i Hässelby gård",
  "description": "Fönsterrenovering i Hässelby: radhusen i Hässelby gård från 1957, tunnelbanestaden som värdefull miljö, linoljefärg och tätare fönster.",
  "h1": "Fönsterrenovering i Hässelby",
  "lead": "Radhusen vid Astrakangatan och Friherregatan i Hässelby gård ansågs mycket moderna när de byggdes 1957. I dag är tunnelbanestaden utpekad som kulturhistoriskt värdefull miljö, och fönstren är en del av helheten. Geal Entreprenad AB renoverar fönster på radhus och villor i Hässelby och behåller fönstrens utseende.",
  "card": "Radhusen i Hässelby gård.",
  "sections": [
    {"id": "radhusen-hasselby", "anchor": "Radhusen",
     "h2": "Moderna radhus från 1957",
     "paras": [
       "Enligt Stadsmuseets skrift om Hässelby gård i serien Stockholms spår pågick byggandet i stadsdelen som mest 1954 och 1955. Radhusen vid Astrakangatan och Friherregatan uppfördes av Småstugebyrån 1957 och ansågs mycket moderna, med fasader av sidiplattor och tak av nästan svarta invaritplattor, det vill säga korrugerad eternit.",
       "Bostadshusen grupperades med omväxlande höga punkthus och låga hus kring skyddade gårdar. Tunnelbanestationen invigdes 1956.",
     ],
     "aside": {"title": "Hässelby gård", "items": [
       "Byggdes som mest 1954–1955", "Radhus av Småstugebyrån 1957", "Tunnelbanan invigd 1956"]}},
    {"id": "varsam-hasselby", "h2": "Tunnelbanestaden som värdefull miljö",
     "paras": [
       "I tabellen i stadens strategi Varsam är både Hässelby gård och Hässelby strand markerade som kulturhistoriskt värdefulla miljöer av typen tunnelbanestad. Hässelby villastad finns med i samma tabell som villastad, men utan den markeringen.",
       "Stockholms stad räknar upp vilka fönsterändringar som kan kräva bygglov, bland annat att byta material eller kulör, ändra dimensioner, proportioner eller profilering på karmar, bågar och spröjs, byta upphängning och ändra indelning. En renovering som behåller allt det är det säkraste sättet att förnya fönstren i en värdefull miljö.",
     ],
     "aside": {"title": "Kan kräva lov enligt staden", "items": [
       "Nytt material eller ny kulör", "Andra profiler eller proportioner", "Annan upphängning", "Ändrad indelning"]}},
    {"id": "agarna-hasselby", "h2": "Radhus med äganderätt och i förening",
     "paras": [
       "Stadens områdesfakta för 2025 visar 324 småhus med äganderätt i Hässelby gård och 13 i bostadsrätt. I Hässelby villastad är småhusen många fler: 4 757 med äganderätt och 204 i bostadsrätt.",
       "Äger du radhuset bestämmer du själv över fönstren, men eftersom husen i en grupp byggdes likadana är det klokt att behålla samma kulör och utförande som grannarna. Om fönsterbyten i stadsdelen kan du läsa under " + _L.format("fonsterbyte-hasselby.html", "fönsterbyte i Hässelby") + ".",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Hässelby gård: 324 äganderätt, 13 bostadsrätt", "Hässelby villastad: 4 757 äganderätt, 204 bostadsrätt"]}},
    {"id": "femtiotalet-hasselby", "h2": "1950-talets snickerier och linoljefärgen",
     "paras": [
       "Riksantikvarieämbetet skriver att det ännu på 1950-talet var linoljefärg som föreskrevs för utvändig snickerimålning, och att grundning och två strykningar var det minsta som skulle utföras enligt en handbok i måleri från 1953. Fönster från den tiden är alltså ofta målade med linoljefärg från början.",
       "Vid en renovering tar vi reda på vilken färg som sitter på bågarna i dag. Myndigheten varnar för att måla över äldre färgtyper med moderna material, eftersom nästa underhåll då ofta blir mer komplicerat.",
     ],
     "aside": None},
    {"id": "tatning-hasselby", "h2": "Tätningslist eller tillsatsruta",
     "paras": [
       "Riksantikvarieämbetet skriver att komplettering med tätningslist och delvis nya beslag är de åtgärder som oftast utförs, och att ett gammalt fönster med rätt tätningslist och tillsatsruta kan bli lika energisnålt som ett nytt. Tillsatsrutan fästs på innerbågen, och vill man behålla fönstrets profiler är en extra träbåge på insidan ofta den bästa lösningen.",
       "Vi väljer lösning efter hur fönstret ser ut och vad som ska behållas. Springans bredd kan enligt myndigheten mätas genom att fästa små klumpar modellera där listen ska sitta, och samma knep används när gångjärnen justeras. Om måleri i Hässelby i övrigt kan du läsa under " + _L.format("malare-hasselby.html", "målare i Hässelby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Hässelby till",
  "steps": [
    ("Besiktning", "Varje fönster bedöms: färgtyp, kitt, trä och beslag."),
    ("Kartan", "Stadsmuseets karta kontrolleras om något ska ändras."),
    ("Skriftligt kostnadsförslag", "Fönster för fönster, med tätning för sig."),
    ("Renovering", "Skrapning, lagning, kittning och målning i samma färgtyp."),
    ("Tätning", "Tätningslist eller tillsatsruta efter vad fönstret tål."),
    ("Genomgång", "Vi går igenom fönstren och hur de sköts framåt."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Hässelby",
  "rot": [_ROT_FON, _ROT_AMT],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Hässelby?",
  "price": [
    "Antal fönster och bågar, färgtyp och hur mycket som ska skrapas, lagningar, beslag och val av tätning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("När byggdes radhusen vid Astrakangatan i Hässelby gård?",
     "Enligt Stadsmuseets skrift i serien Stockholms spår uppfördes radhusen vid Astrakangatan och Friherregatan av Småstugebyrån 1957."),
    ("Är Hässelby gård ett kulturhistoriskt värdefullt område?",
     "Ja, i stadens strategi Varsam är Hässelby gård markerat som kulturhistoriskt värdefull miljö av typen tunnelbanestad."),
    ("Vilken färg målades fönstren med på 1950-talet?",
     "Riksantikvarieämbetet skriver att det ännu på 1950-talet var linoljefärg som föreskrevs för utvändig snickerimålning."),
    ("Kan ett fönster från 1950-talet bli lika energisnålt som ett nytt?",
     "Enligt Riksantikvarieämbetet kan ett gammalt fönster med rätt tätningslist och tillsatsruta bli lika energisnålt som ett nytt."),
    ('Vad är invaritplattor på radhusen i Hässelby gård?',
     'Enligt Stadsmuseets skrift om Hässelby gård är invaritplattor korrugerad eternit, ett fibercementmaterial som lades på radhusens tak vid Astrakangatan och Friherregatan.'),
  ],
  "sources": [("Stockholms stadsmuseum – Stockholms spår: Hässelby gård (pdf)", "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000086.pdf"),
              _VARSAM,
              ("Stockholms stad – Områdesfakta 2025: Hässelby gård (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-gard.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hässelby villastad (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-villastad.pdf"),
              _STH_FON, _STH_KL, _RAA_FON, _RAA_MAL, _SKV, _SKV2],
  "cta": ("Ska fönstren i Hässelby renoveras?", "Boka ett gratis platsbesök, så besiktigar vi fönstren innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus från 1950-talet med plattfasad och mörkt tak",
     "row of late 1950s Swedish terraced houses with light facade panels, dark corrugated roof sheets, original white wooden windows, small front gardens and a footpath, Stockholm western suburb, summer" + _IMG_END),
    ("Fönsterbåge från 1950-talet med linoljefärg",
     "close view of a 1950s wooden window sash freshly repainted with glossy white linseed oil paint, simple profiles without glazing bars, daylight" + _IMG_END),
    ("Innerbåge med tillsatsruta",
     "close view from inside a room of an old wooden window where an extra thin glass pane has been fitted on the inner sash with discreet hinges, white frame, daylight, plant on sill" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ KISTA
"fonsterrenovering-kista.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Kista", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Kista – 1970-talets radhusfönster",
  "description": "Fönsterrenovering i Kista: radhus från 1975–1980, vem som ansvarar för fönstren, ändringar som kan kräva lov och tätning med list eller tillsatsruta.",
  "h1": "Fönsterrenovering i Kista",
  "lead": "Fönstren i Kistas radhus är snart femtio år gamla. Många av dem går fortfarande att laga, måla om och täta i stället för att bytas. Geal Entreprenad AB renoverar fönster på radhus, kedjehus och villor i Kista och Akalla och börjar med att ta reda på vem som ansvarar för fönstren.",
  "card": "1970-talets radhusfönster.",
  "sections": [
    {"id": "kista-kista", "anchor": "Kista",
     "h2": "Husen från 1975–1980",
     "paras": [
       "Enligt Stadsmuseets skrift om Kista i serien Stockholms spår byggdes stadsdelen ut åren 1975–1980 med omkring 780 småhus och 2 500 lägenheter i flerbostadshus. Staden tillämpade här friare arkitektoniska former än i de andra stadsdelarna på Järvafältet.",
       "Fönstren i husen från den tiden är alltså byggda för ett och samma område under några få år. Det gör att de ofta ser likadana ut inom en husgrupp, och att en renovering kan planeras för flera hus på en gång.",
     ],
     "aside": {"title": "Kista enligt Stockholms spår", "items": [
       "Utbyggt 1975–1980", "Omkring 780 småhus", "2 500 lägenheter"]}},
    {"id": "ansvaret-kista", "h2": "Vem ansvarar för fönstren?",
     "paras": [
       "Stadens områdesfakta för 2025 visar 482 småhus med äganderätt och 404 i bostadsrätt i stadsdelen Kista, och i Akalla 170 med äganderätt och 493 i bostadsrätt. Äger du huset ansvarar du själv för fönstren. I en bostadsrätt avgör stadgarna.",
       "Bostadsrättslagen utgår från att bostadsrättshavaren håller lägenheten i gott skick på egen bekostnad om inte stadgarna säger annat. Därför börjar vi med att läsa vad föreningens stadgar säger om fönstren, innan vi föreslår en renovering för dig eller för hela föreningen.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Kista: 482 äganderätt, 404 bostadsrätt", "Akalla: 170 äganderätt, 493 bostadsrätt"]}},
    {"id": "lov-kista", "h2": "Ändringar som kan kräva lov",
     "paras": [
       "Stockholms stad räknar upp vilka fönsterändringar som kan kräva bygglov: att byta material eller kulör, ändra storlek eller placering, ändra dimensioner, proportioner eller profilering på karmar, bågar och spröjs, byta upphängning, till exempel från sidohängda till vippfönster, och ändra indelning. Det beror också på vilken byggnad det gäller.",
       "En renovering där fönstret behåller material, kulör, mått och upphängning ändrar inget av detta. Det gör renoveringen till ett enkelt val även när huset ligger i en grupp där alla fönster ska se likadana ut.",
     ],
     "aside": None},
    {"id": "tatare-kista", "h2": "Tätare med list eller tillsatsruta",
     "paras": [
       "Riksantikvarieämbetet påpekar att moderna tätningslister ger en avsevärd förbättring av både ljud- och värmeisolering, och att det finns tillsatsrutor som fästs på innerbågen med en profil av plast eller aluminium. Enligt myndigheten ger gummilisterna ett lufttätt utrymme mellan tillsatsruta och båge, och de problem med smuts och kondens som ofta befaras uppstår i regel inte.",
       "Tätningslisterna tillverkas av EPDM-gummi i svart eller brunt och av silikongummi i vitt, i olika profiler för olika springor. Vi mäter springan på varje fönster innan listen väljs.",
     ],
     "aside": {"title": "Tätningslister enligt RAÄ", "items": [
       "Svart eller brun: EPDM-gummi", "Vit: silikongummi", "Silikonlister klistras", "Övriga fästs med häftklammer"]}},
    {"id": "malningen-kista", "h2": "Bottenstycket först",
     "paras": [
       "Riksantikvarieämbetet skriver att det framför allt är bottenstyckena i karm och båge som skadas, och att det oftast går att byta bara de skadade partierna. Sol och väta bryter ner färg och kitt på fönstrens mest utsatta delar, och sydfasader är särskilt utsatta.",
       "Vi börjar därför med fönstren på husets solsida och med nederdelen av varje båge. Myndigheten påpekar också att ett fönster ibland måste justeras med hänsyn till sättningar i huset. En båge som skaver mot karmen slits ojämnt och släpper in fukt, så vi justerar gångjärnen innan bågen målas och tätas. Om måleri och snickerier i Kista i övrigt kan du läsa under " + _L.format("malare-kista.html", "målare i Kista") + " och " + _L.format("snickare-kista.html", "snickare i Kista") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Kista till",
  "steps": [
    ("Ansvaret", "Vi reder ut om du eller föreningen ansvarar för fönstren."),
    ("Besiktning", "Bottenstycken, kitt, färg och beslag bedöms fönster för fönster."),
    ("Skriftligt kostnadsförslag", "Per hus eller per grupp när flera hus renoveras."),
    ("Renovering", "Lagning av skadade delar, kittning och målning i samma kulör."),
    ("Tätning", "Tätningslist eller tillsatsruta på innerbågen."),
    ("Genomgång", "Vi går igenom fönstren med dig eller styrelsen."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Kista",
  "rot": [
    _ROT_FON + " I en bostadsrätt beror avdraget på om fönstren är något du ansvarar för enligt stadgarna; arbete som föreningen ansvarar för ger inget rotavdrag.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Kista?",
  "price": [
    "Antal fönster, skador på bottenstycken, kitt och färg, val av tätning och om flera hus renoveras samtidigt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem ansvarar för fönstren i vårt bostadsrättsradhus i Akalla?",
     "Det avgör föreningens stadgar. Bostadsrättslagen utgår från att du håller lägenheten i gott skick om inte stadgarna säger något annat."),
    ("Får vi byta våra sidohängda fönster i Kista mot vippfönster?",
     "Stockholms stad räknar ett byte av upphängning, till exempel från sidohängda till vippfönster, bland de ändringar som kan kräva bygglov. En renovering ändrar inte upphängningen."),
    ("Blir det kondens mellan tillsatsrutan och bågen?",
     "Riksantikvarieämbetet skriver att de problem med nedsmutsning och kondens som ofta befaras i regel inte förekommer när tillsatsrutan sitter med gummilister."),
    ("Vilken del av fönstret ruttnar först på ett radhus från 1970-talet?",
     "Enligt Riksantikvarieämbetet är det framför allt bottenstyckena i karm och båge som skadas, och ofta räcker det att byta de skadade partierna."),
    ('Vilka tätningslister är svarta och vilka är vita?',
     'Enligt Riksantikvarieämbetet är svarta och bruna lister av EPDM-gummi och vita lister av silikongummi. Silikonlisterna klistras fast, de andra fästs med häftklammer.'),
  ],
  "sources": [("Stockholms stadsmuseum – Stockholms spår: Kista (pdf)", "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000080.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Kista (pdf)", _OF + "vasterort/jarva/kista.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Akalla (pdf)", _OF + "vasterort/jarva/akalla.pdf"),
              _BRL, _STH_FON, _RAA_FON, _SKV, _SKV2],
  "cta": ("Ska fönstren i Kista renoveras?", "Boka ett gratis platsbesök, så går vi igenom fönstren och ansvaret innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus från 1970-talet med stora träfönster",
     "late 1970s Swedish terraced houses with wooden facade panels and large original wooden windows, uniform design within the group, small front gardens and a pedestrian path, northwest Stockholm suburb, summer" + _IMG_END),
    ("Nytt bottenstycke inpassat i en fönsterbåge",
     "still life on a workbench: the lower rail of a wooden window sash with a newly spliced section of fresh pine fitted into the old painted frame, clamps beside it, daylight" + _IMG_END),
    ("Tillsatsruta på insidan av ett radhusfönster",
     "interior view of a 1970s wooden window with a discreet additional glass pane mounted on the inner sash, white frame, light curtains, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"fonsterrenovering-skarholmen.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Skärholmen", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Skärholmen – miljonprogrammets radhus",
  "description": "Fönsterrenovering i Skärholmen: radhusen i Sätra, Bredäng och Vårberg, husgrupperna, Bredäng som värdefull miljö och besiktning före beslut.",
  "h1": "Fönsterrenovering i Skärholmen",
  "lead": "Radhusen i Sätra, Bredäng och Vårberg byggdes rationellt och i stora grupper där husen ser likadana ut. Därför märks det när ett hus får fönster som avviker. Geal Entreprenad AB renoverar fönster på radhus och villor i Skärholmen och behåller fönstrens mått och utseende.",
  "card": "Miljonprogrammets radhus.",
  "sections": [
    {"id": "byggandet-skarholmen", "anchor": "Byggandet",
     "h2": "Ett rationellt och industriellt byggande",
     "paras": [
       "Stadens strategi för småhusområden, Varsam, beskriver hur industrialiseringen av byggtekniken fick sitt genombrott i början av 1960-talet, och hur Bredäng blev den första stadsdelen som planerades i stor skala med byggstart 1962, följd av Sätra. En stor del av miljonprogrammets bebyggelse var gruppbyggda småhus och radhus.",
       "Varsam skriver att det rationella och industriella byggandet avspeglades i arkitekturen genom strikt gruppering av byggnader och en enkel och stram gestaltning. Omsorgen om planlösningarna var stor, och goda ljusförhållanden och funktionalitet var ledord.",
     ],
     "aside": {"title": "Varsam om småhusen", "items": [
       "Strikt gruppering", "Enkel och stram gestaltning", "Goda ljusförhållanden", "Enhetliga husgrupper"]}},
    {"id": "agarna-skarholmen", "h2": "Du äger fönstren själv",
     "paras": [
       "Stadens områdesfakta för 2025 visar att det inte finns några småhus i bostadsrätt i Skärholmens stadsdelsområde. 1 976 småhus ägs med äganderätt, fördelade på Vårberg, Skärholmen, Sätra och Bredäng.",
       "Det betyder att det är du som beslutar om fönstren och som kan få rotavdrag för arbetet. Men eftersom husen i en grupp byggdes likadana lönar det sig att prata med grannarna, både om kulör och om att renovera flera hus samtidigt.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Äganderätt: 1 976", "Bostadsrätt: 0"]}},
    {"id": "bredang-skarholmen", "h2": "Bredäng och de andra stadsdelarna",
     "paras": [
       "I tabellen i Varsam är Bredäng markerat som kulturhistoriskt värdefull miljö, medan Sätra, Skärholmen och Vårberg saknar den markeringen. Stockholms stad skriver att ändringar av fönster, som ny kulör, andra profiler eller ändrad indelning, kan kräva bygglov beroende på byggnaden, och hänvisar till Stadsmuseets klassificeringskarta.",
       "En renovering som behåller fönstrets kulör, mått och indelning ändrar inte husets utseende. Ska något ändras kontrollerar vi kartan för din fastighet först.",
     ],
     "aside": None},
    {"id": "besiktning-skarholmen", "h2": "Besiktiga innan fönstren döms ut",
     "paras": [
       "Riksantikvarieämbetet skriver att det utan besiktning är alltför lätt att döma ut fönster som mycket väl skulle gå att bevara, och råder att arbetet inleds med en systematisk besiktning och analys av varje fönster för sig. Det ger också underlag för en mer exakt kostnadsberäkning.",
       "I modernare hus är det enligt myndigheten framför allt fönstrens synliga mått och proportioner som är viktiga att bevara. På ett radhus från 1960-talet betyder det att karmen och bågarnas bredd ska vara desamma efter renoveringen, så att fönstret fortsätter att se ut som grannarnas.",
     ],
     "aside": {"title": "Vid besiktningen ser vi på", "items": [
       "Bottenstycken i karm och båge", "Kitt och färg", "Beslag och gångjärn", "Hur bågen sluter mot karmen"]}},
    {"id": "fargen-skarholmen", "h2": "Färg och kitt som skyddar träet",
     "paras": [
       "Riksantikvarieämbetet skriver att färgskiktet på ett fönster ska skydda karm och båge mot väta utifrån utan att hindra fukt i virket från att torka ut, ha god beständighet och vara lätt att förnya. Linoljefärg tränger in i virket och fäster bra, medan latexfärger enligt myndigheten snarare lägger sig som en film på ytan och har en tendens att klibba ihop, vilket är en nackdel på fönster.",
       "Lika viktigt är kittet. Myndigheten påpekar att fönsterkittet ska vara helt, så att fukt inte tränger in i träet och orsakar röta, och att sol och väta bryter ner färg och kitt på fönstrens mest utsatta delar. Vi tar därför bort löst kitt och kittar om där det behövs innan bågen målas.",
     ],
     "aside": {"title": "Färgskiktet ska enligt RAÄ", "items": [
       "Skydda mot väta utifrån", "Låta fukt i träet torka ut", "Ha god beständighet", "Vara lätt att förnya"]}},
    {"id": "arbetet-skarholmen", "h2": "Från skrapning till tätning",
     "paras": [
       "Fönstrets underhåll består enligt Riksantikvarieämbetet i första hand av ommålning och kittning. Skadade delar lagas, bågarna justeras och innerbågen tätas med en list som passar falsen. Fönstret ska målas och justeras innan listerna sätts upp.",
       "Om fasader och kulörer i stadsdelen kan du läsa under " + _L.format("fasadmalning-skarholmen.html", "fasadmålning i Skärholmen") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Skärholmen till",
  "steps": [
    ("Besiktning", "Varje fönster bedöms för sig och resultatet sammanställs."),
    ("Kartan", "Stadsmuseets karta kontrolleras, särskilt i Bredäng."),
    ("Skriftligt kostnadsförslag", "Per fönster, och per hus om grannarna är med."),
    ("Renovering", "Skrapning, lagning, kittning och målning i samma kulör."),
    ("Tätning och justering", "Bågarna justeras och innerbågen tätas."),
    ("Genomgång", "Vi går igenom fönstren med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Skärholmen",
  "rot": [_ROT_FON, _ROT_AMT],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Skärholmen?",
  "price": [
    "Antal fönster, skador på trä och kitt, beslag, tätning och om flera hus i gruppen renoveras samtidigt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Finns det radhus i bostadsrätt i Skärholmen?",
     "Enligt stadens områdesfakta för 2025 finns inga småhus i bostadsrätt i Skärholmens stadsdelsområde. 1 976 småhus ägs med äganderätt."),
    ("Är Sätra ett kulturhistoriskt värdefullt område?",
     "Sätra saknar den markeringen i stadens strategi Varsam, där bara Bredäng av stadsdelarna i Skärholmen är markerat som kulturhistoriskt värdefull miljö."),
    ("Hur vet vi om fönstren i vårt radhus i Vårberg går att renovera?",
     "Genom en besiktning av varje fönster för sig. Riksantikvarieämbetet påpekar att det utan besiktning är lätt att döma ut fönster som går att bevara."),
    ("Kan flera grannar i längan renovera fönstren samtidigt?",
     "Ja, och eftersom husen i en grupp byggdes likadana är det ofta praktiskt. Vi gör då kostnadsförslag per hus."),
    ('Varför är det viktigt att fönsterkittet är helt?',
     'Riksantikvarieämbetet påpekar att fukt annars kan tränga in i träet och orsaka röta, särskilt på fönstrens mest utsatta delar.'),
  ],
  "sources": [_VARSAM,
              ("Stockholms stad – Områdesfakta 2025: Skärholmens stadsdelsområde (pdf)", _OF + "soderort/skarholmen/skarholmen-stadsdelsomrade.pdf"),
              _STH_FON, _STH_KL, _RAA_FON, _RAA_MAL, _SKV, _SKV2],
  "cta": ("Ska fönstren i Skärholmen renoveras?", "Boka ett gratis platsbesök, så besiktigar vi fönstren ett och ett innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Grupp av 1960-talsradhus med likadana fönster",
     "group of plain 1960s Swedish million programme terraced houses, two storeys, low-pitched gable roofs without dormers or chimney pots, light yellow brick and dark brown wooden panels, identical white wooden windows, lawns and a concrete footpath, Stockholm suburb, summer" + _IMG_END),
    ("Fönsterbåge där gammal färg skrapats bort",
     "close view of a wooden window sash from the 1960s with old flaking paint partly scraped off the lower rail, bare wood showing, paint scraper lying on the window sill, daylight" + _IMG_END),
    ("Nymålat fönster i en tegelfasad",
     "close view of a freshly repainted white wooden window in a brick facade of a 1960s terraced house, clean glass and new putty lines, daylight" + _IMG_END),
  ],
},
}
