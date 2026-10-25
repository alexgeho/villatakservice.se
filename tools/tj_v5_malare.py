# -*- coding: utf-8 -*-
"""Målare – ortsidor v5: Ekerö, Upplands Väsby, Enskede, Älvsjö, Hässelby, Sigtuna (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade 2026-10-25: Ekerö kommun (Vad vill du bygga?;
Kulturmiljöprogram 2015), Upplands Väsby kommun (Fasadändring; Kunskapsunderlag för kulturmiljö 2025),
Stockholms stad (bygglov.stockholm: Fasadändring, Stadsmuseets kulturhistoriska klassificering; vägledningen
Varsam utveckling av småhus- och villaområden), Stadsmuseet via Stockholmskällan (Gamla Enskede
byggnadsinventering 1974; Sockenplan; S. Lindhagen: Älvsjö villastad), Sigtuna kommun (Bevarande- och
förnyelseplan för Sigtuna stad 2019; Bygga i kulturmiljö), Boverket (PBL kunskapsbanken: fasadändring),
Riksantikvarieämbetet (Byggnadsmåleri med traditionella färgtyper) och Skatteverket (rotavdrag).
Inga priser, garantier, omdömen, egna uppdrag eller cert. Schema: se tools/tj_check.py."""

_BOV = ("Boverket – Bygglov för fasadändring (PBL kunskapsbanken)",
        "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_RAA = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf)",
        "https://www.raa.se/publicerat/9789172095830.pdf")
_SKV = ("Skatteverket – Så fungerar rotavdraget",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV2 = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
         "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_STH_FASAD = ("Stockholms stad – Fasadändring (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ EKERÖ
"malare-ekero.html": {
  "kind": "district", "service": "malare", "ort": "Ekerö", "svc_label": "Målare",
  "title": "Målare i Ekerö – sommarvillor, stugor och villagator",
  "description": "Målare i Ekerö: sommarvillor med rik panel, rödfärgade stugor, permanentade fritidshus och villorna i östra Ekerö, kommunens karta och lovfrågan.",
  "h1": "Målare i Ekerö",
  "lead": "På Mälaröarna kan en sommarvilla från 1800-talet, en rödmålad stuga och en villagata från 1970-talet ligga nära varandra, och de tre husen behöver helt olika färg och förarbete. Geal Entreprenad AB målar fasader, fönster och snickerier ute och inne i hela Ekerö kommun, tar reda på vilken färg som sitter på huset innan något beställs och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Sommarvillor, stugor och villor på Mälaröarna.",
  "sections": [
    {"id": "husen-ekero", "anchor": "Husen på Mälaröarna",
     "h2": "Från sommarnöjen till villagator",
     "paras": [
       "Ekerö kommuns kulturmiljöprogram från 2015 beskriver hur närheten till Stockholm tidigt gjorde öarna populära som sommarnöje. När ångbåtar började trafikera Mälaröarna i mitten av 1800-talet blev resan enklare, och sommarvillor uppfördes åt välbärgade stockholmare. Under 1900-talet tillkom fler områden med fritidshus.",
       "På Kungshatt finns enligt programmet ett femtiotal sommarvillor från tiden kring sekelskiftet 1900, med rikt dekorerad panelarkitektur och öppna eller inglasade verandor. Ett sådant hus har mycket snickerier i förhållande till fasadytan: listverk, foder, räcken och spröjsade fönster som skrapas, lagas och målas för hand.",
       "Östra Ekerö domineras i stället av villor och radhus från andra halvan av 1900-talet. Programmet nämner Väsby, med enhetlig bebyggelse från tidigt 1970-tal, och Närlunda, där villor från 1960-talet dominerar. I Älvnäs, Gällstaö och Erikssten har sommarbostäder permanentats och förtätats, och sommarvillor och sportstugor från 1900-talet har byggts om eller rivits.",
     ],
     "aside": {"title": "Husen i korthet", "items": [
       "Kungshatt: sommarvillor kring 1900", "Väsby: enhetligt tidigt 1970-tal",
       "Närlunda: villor från 1960-talet", "Älvnäs, Gällstaö, Erikssten: permanentade sommarhus"]}},
    {"id": "lov-ekero", "h2": "Kommunens karta visar var kulören prövas",
     "paras": [
       "Ekerö kommun skriver att fasadändringar inte kräver bygglov på ett en- eller tvåbostadshus, om inte fastigheten ligger i ett område som bedömts som särskilt värdefullt. Efter ändringarna i plan- och bygglagen, som trädde i kraft den 1 december 2025, har kommunen gjort en ny bedömning av sina särskilt värdefulla byggnader och områden. De visas som undantagsområden i Ekerökartan, och där kan de lovbefriade reglerna inte användas.",
       "Boverket räknar ett byte av kulör, till exempel från rött till vitt, som en fasadändring, medan ommålning i samma kulör normalt räknas som underhåll. Att gå från slamfärg till en annan färgtyp är inget kulörbyte, men det kan bedömas påverka husets yttre karaktärsdrag. En lovfri fasadändring får heller inte strida mot detaljplanen.",
       "Är du osäker ger kommunen ett enkelt råd: mejla ett foto på huset till info@ekero.se och beskriv vilken ändring du vill göra, så avgör kommunen om bygglov behövs. Kulturmiljöprogrammet är rådgivande, men för tätorten i östra Ekerö skriver det att befintliga byggnader bör respekteras när det gäller proportioner, fasadfärg, fönster, panel, entréer och räcken, och det gäller enligt programmet även villor och sportstugor.",
     ],
     "aside": {"title": "Innan en ny kulör", "items": [
       "Sök fastigheten i Ekerökartan", "Läs detaljplanen för tomten",
       "Mejla foto till kommunen vid tvekan", "Samma kulör räknas som underhåll"]}},
    {"id": "slamfarg-ekero", "h2": "Rödfärgade stugor, uthus och gårdar",
     "paras": [
       "Röd slamfärg finns på allt från uthus till hela miljöer. I barnbyn Skå på Färingsö, som Stockholms stad byggde upp på 1940-talet kring Skå gård, uppfördes tolv rödmålade små stugor. För västra Ekerö skriver kulturmiljöprogrammet att torpens och gårdarnas skala, färgsättning och gestaltning bör respekteras.",
       "Riksantikvarieämbetets handbok om traditionella färgtyper beskriver slamfärgen som den i särklass mest underhållsvänliga. Vid ommålning borstas fasaden med stål- eller rotborste tills lös färg och lavar är borta, spikar som rest sig slås i och rötskadat ändträ lagas med friskt virke. Därefter räcker normalt en strykning.",
       "Handboken är lika tydlig om begränsningen: en slamfärgad yta ska bara målas om med slamfärg, eftersom det inte går att återvända när en annan färgtyp väl har strukits på, ens om den gamla färgen tas bort. Den varnar också för färger som säljs med namn som påminner om rödfärg men har andra bindemedel, till exempel latextillsatser. Ska taket på en gammal bod eller lada ses över samtidigt, läs mer under " + _L.format("taklaggare-ekero.html", "takläggare i Ekerö") + ".",
     ],
     "aside": None},
    {"id": "fritidshus-ekero", "h2": "När sommarstugan har blivit villa",
     "paras": [
       "En sommarstuga som byggts om till åretruntbostad har ofta fått nya delar i omgångar: en tillbyggnad med annan panel, nya fönster på en sida och färg från flera decennier. Riksantikvarieämbetet påpekar att linoljefärg, slamfärg och kalkfärg ännu på 1950-talet hörde till de vanligaste färgerna, så även ett hus från 1900-talets mitt kan ha en traditionell färg under de senare lagren.",
       "Därför gör vi skrapprov på flera ställen innan färgtypen bestäms. Efter tvätt och skrapning avgör skadornas omfattning hur mycket som ska grundas. Enligt handboken räcker det att grunda de skadade partierna om ungefär en tiondel av färgskiktet är skadat, medan hela ytan bör grundas när 30–40 procent är skadat. Grått och luddigt trä skrapas och slipas bort först.",
       "Inomhus målar vi väggar, tak, snickerier och dörrar och tapetserar, och i en stuga som värms året runt först på senare år tittar vi efter fuktfläckar innan väggarna målas. Är vinden kall och dragig kan " + _L.format("vindsisolering.html", "vindsisolering") + " vara värt att göra innan rummen under målas om.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Ekerö till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, snickerier, fönster och uthus och gör skrapprov för att se vilken färgtyp som sitter på."),
    ("Kartan och planen", "Fastigheten kontrolleras i Ekerökartan och detaljplanen, och vid tvekan frågar vi kommunen."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, förarbete och antal strykningar står med, och snickerierna redovisas för sig."),
    ("Förarbete", "Tvätt eller borstning, skrapning, lagning av trä och kittning av fönster. Rabatter och bryggor skyddas."),
    ("Målning", "Grundning och strykningar i lämpligt väder, med de torktider färgtypen kräver."),
    ("Genomgång", "Vi går igenom huset tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Ekerö",
  "rot": [
    "Rotavdraget gäller både villan du bor i och ett fritidshus som du äger och använder. Skatteverket räknar fasadmålning, målning av fönster, väggar och tak och även rengöring av fasader som rotarbete i ett småhus, men inte målning av staket och murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Garage, förråd och andra mindre byggnader kan enligt Skatteverket höra till småhuset. Färg, material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden i Ekerö",
  "price": [
    "Mest avgör vilken sorts hus det är. En sommarvilla med rik panel och inglasad veranda kräver mycket handarbete, en rödfärgad stuga eller lada går fortare per kvadratmeter, och på en villa från 1960- eller 70-talet är det oftast panelens och fönstrens skick som styr. Kuperade strandtomter kan också påverka hur ställningen kan stå. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för att måla villan i Ekerö i en ny kulör?",
     "Normalt inte för ett en- eller tvåbostadshus. Ligger fastigheten i ett av undantagsområdena i Ekerökartan, eller har detaljplanen utökad lovplikt, krävs lov. Kommunen svarar om du mejlar ett foto och en beskrivning av ändringen."),
    ("Kan vi gå över från rödfärg till täckande färg på stugan?",
     "Tekniskt går det, men Riksantikvarieämbetet avråder eftersom det inte går att återgå till slamfärg efteråt. Det kan också räknas som en påverkan på husets karaktärsdrag om stugan ligger i ett värdefullt område."),
    ("Får vi rotavdrag för att måla fritidshuset på Mälaröarna?",
     "Ja, om du äger huset och använder det som fritidsbostad. Avdraget gäller arbetskostnaden, inte färgen."),
    ("Hur mycket av den gamla färgen måste bort innan fasaden målas om?",
     "All lös och flagnande färg. Fast sittande färg kan ligga kvar, och är bara en mindre del av ytan skadad räcker det att grunda de partierna innan hela fasaden stryks."),
    ("Hur målar man en sommarvilla med mycket snickarglädje?",
     "Listverk, foder och räcken skrapas, lagas och grundas för sig innan fasaden målas. Det tar tid, och därför redovisar vi snickerierna separat i kostnadsförslaget."),
  ],
  "sources": [
    ("Ekerö kommun – Kulturmiljöprogram 2015 (pdf)",
     "https://www.ekero.se/download/18.553838ea17305720c321ec82/1597925412772/Eker%C3%B6%20kulturmilj%C3%B6program.pdf"),
    ("Ekerö kommun – Vad vill du bygga? (fasadändring och undantagsområden)",
     "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/vad-vill-du-bygga"),
    _BOV, _RAA, _SKV, _SKV2,
  ],
  "cta": ("Ska huset på Mälaröarna målas om?", "Boka ett gratis platsbesök så går vi igenom färglager, kulör och lovfrågan på plats."),
  "img": [
    ("Sekelskiftesvilla med inglasad veranda och rik panel vid Mälaren på Ekerö",
     "late 1800s Swedish wooden summer villa with richly decorated carpentry, glazed veranda, pale yellow painted wooden panel and white trims, on a rocky lakeshore plot by lake Mälaren, Ekerö, pines and birches, calm water, summer daylight, no people"),
    ("Rödfärgad brädvägg på en lada med borstar inför ommålning med slamfärg",
     "close-up of an old Swedish wooden barn wall with vertical boards painted entirely in traditional matte falu red slurry paint, the left part faded and slightly worn, the right part freshly repainted in the same deep matte falu red, a wide paint brush and a wire brush resting on a small wooden trestle in the grass, rural island farm by lake Mälaren, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"malare-upplands-vasby.html": {
  "kind": "district", "service": "malare", "ort": "Upplands Väsby", "svc_label": "Målare",
  "title": "Målare i Upplands Väsby – puts, tegel och radhus",
  "description": "Målare i Upplands Väsby: jordfärgad puts vid Oxundavägen, vitmålat tegel i Ägget, mörk panel i Skälby och kommunens regler om ny kulör. Gratis platsbesök.",
  "h1": "Målare i Upplands Väsby",
  "lead": "I Upplands Väsby är det ofta en hel länga eller ett helt kvarter som delar samma färgskala. Kommunens kunskapsunderlag för kulturmiljö från 2025 beskriver kulörerna område för område, från de faluröda villorna i Väsby villastad till 1960-talets vita tegel i Skälby. Geal Entreprenad AB målar ute och inne i hela kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Radhus, kedjehus och villor i Väsby.",
  "sections": [
    {"id": "oxundavagen", "anchor": "Färgskalorna",
     "h2": "Jordpigment i putsen längs Oxundavägen",
     "paras": [
       "Radhusen och villorna längs Oxundavägen byggdes 1947 och 1958. På Vinkelvägen har radhusen grovputsade fasader där jordpigmenten skiftar mot gult, grönt, brunt och beige. Fönsterbågar och karmar av trä är vitmålade och flankeras av luckor i vitt, blått eller brunt, och entréerna har ekdörrar i en vit putsad portik.",
       "På Radhusvägen är uttrycket mer modernistiskt. Vita band delar in putsen i fält, och fasaderna går i grönt, vitt och beige. Längs Lagmansvägen återkommer de vita linjerna i putsen. Kunskapsunderlaget räknar områdets sammanhållna färgskala och jordpigmenten i putsen till de karaktärsdrag som ska bevaras, och vägledningen är att underhålla och behålla färgskalorna.",
       "För en målare betyder det att kulören sällan väljs hus för hus. Ska en putsfasad i en länga målas om tar vi först fram den kulör som sitter på i dag, och det är klokt att stämma av med grannarna så att längan behåller sin helhet även när husen målas vid olika tillfällen.",
     ],
     "aside": {"title": "Oxundavägen i korthet", "items": [
       "Vinkelvägen: puts i gult, grönt, brunt och beige", "Vita fönster, luckor i vitt, blått eller brunt",
       "Radhusvägen: vita band i putsen", "Färgskalan räknas som bevarandevärd"]}},
    {"id": "agget-skalby", "h2": "Vitmålat tegel i Ägget, mörk panel i Skälby",
     "paras": [
       "Kedjehusområdet Ägget i Runby uppfördes 1957–61 och består av omkring 100 kedjehus av fyra olika typer. Underlaget beskriver en blandning av rött tegel, trä och vitmålat rödtegel. De låga husen i mitten har fasader av vitmålat rödtegel eller puts, och den enkla träpanelen som kröner gavlarna har en kontrasterande kulör, som svart, blått, gult eller brunt. Garagen mellan de mindre kedjehusen har en duvblå kulör.",
       "Skälby har vinkelradhus i en våning med fasader av vitt mexitegel. Sockeln är mörkmålad, och där fasaden möter taket sitter en mörkmålad liggande träpanel. Enligt underlaget ger de svarta detaljerna i trä tyngd och kontrast mot det vita teglet, och planken kring atriumgårdarna har samma liggande panel som fasaden.",
       "Målat tegel och målad panel åldras olika. Panel och plank av trä är de delar som målas om, medan teglet står kvar orört, och när bara de mörka detaljerna målas om gäller det att träffa samma kulör och glans som hos grannarna. Ska takfot eller vindskivor bytas samtidigt kan det samordnas med en " + _L.format("takrenovering-upplands-vasby.html", "takrenovering i Upplands Väsby") + ".",
     ],
     "aside": {"title": "Kulörer i underlaget", "items": [
       "Ägget: vitmålat rödtegel", "Ägget: gavelpanel i kontrastkulör",
       "Ägget: duvblå garage", "Skälby: vitt tegel och mörk panel"]}},
    {"id": "lov-vasby", "h2": "Ny färg är lovfri – utom i de utpekade områdena",
     "paras": [
       "Upplands Väsby kommun skriver att du i normala fall inte behöver bygglov för fasadändringar på ett en- eller tvåbostadshus, och att det betyder att du kan måla om i en ny färg utan lov. Undantaget är om byggnaden är särskilt värdefull eller ligger inom ett särskilt värdefullt område och ändringen påverkar karaktären, eller om detaljplan eller områdesbestämmelser har utökad lovplikt.",
       "Oxundavägen, Ägget, Skälby och Väsby villastad bedöms i kunskapsunderlaget som särskilt värdefulla bebyggelseområden enligt PBL 8 kap. 13 §. Bor du i något av dem är det därför klokt att fråga kommunen innan en ny kulör beställs. Kommunen påpekar också att ändringar ska göras med hänsyn till byggnadens karaktär och omgivande miljö, oavsett om lov krävs.",
       "Boverket gör en skillnad som spelar roll i radhusområdena. Att måla om i samma kulör räknas normalt som underhåll. Att byta färgtyp, till exempel från linoljefärg till plastfärg, är inget kulörbyte men kan bedömas påverka husets yttre karaktärsdrag.",
     ],
     "aside": None},
    {"id": "puts-vasby", "h2": "Puts från 1940- och 50-talen kräver rätt färg",
     "paras": [
       "Riksantikvarieämbetet beskriver hur man vid mitten av 1900-talet alltmer gick över från kalkbruk till kalkcementbruk när hus putsades, och samtidigt till andra färger än kalkfärg. Kalkfärg fäster bra på ren kalkputs men dåligt på förgipsade och cementrika underlag. Innan putsfasaderna längs Oxundavägen målas om behöver vi därför veta vad putsen och den gamla färgen består av.",
       "Förarbetet tar ofta mest tid: tvätt, borttagning av lös färg och lagning av sprickor med ett bruk som liknar det befintliga. Handboken påpekar att den som högtryckstvättar en fasad måste vara väl förtrogen med tekniken, så att väggen inte får vattenskador. Större putsskador hör hemma under " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
       "I Väsby villastad är det trä som gäller. Kunskapsunderlaget beskriver de ursprungliga villorna från sekelskiftet 1900 och 1910 som faluröda, i nationalromantisk stil, med vita knutar och småspröjsade fönster. Där handlar arbetet om rödfärgad panel, knutbrädor och fönsterbågar som skrapas, kittas och målas. Mer om husen i kommunen finns under " + _L.format("taklaggare-upplands-vasby.html", "takläggare i Upplands Väsby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Upplands Väsby till",
  "steps": [
    ("Platsbesök", "Vi tittar på puts, tegel, panel och fönster och tar reda på vilken färg och kulör som sitter på."),
    ("Område och regler", "Vi kontrollerar om huset ligger i ett av de särskilt värdefulla områdena och vad detaljplanen säger."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, förarbete och antal strykningar skrivs ut, gärna för flera hus i samma länga."),
    ("Förarbete", "Tvätt, skrapning, lagning av puts och trä och kittning av fönster."),
    ("Målning", "Strykningarna görs i lämpligt väder och med de torktider färgen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Upplands Väsby",
  "rot": [
    "För radhus, kedjehus och villor med äganderätt räknar Skatteverket målning av fasader, fönster, väggar och tak som rotarbete, men inte målning av staket och murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och tillsammans med rutavdrag högst 75 000 kr. Färg och material ger inget avdrag.",
    "Du behöver äga bostaden medan arbetet utförs och bo i den. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "På putsfasaderna är det mängden sprickor och lös färg som styr, på tegelhusen hur mycket målad panel, plank och vindskivor det finns och på trävillorna panelens och fönstrens skick. Målas flera hus i en länga samtidigt kan ställning och etablering samordnas. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag måla mitt radhus vid Vinkelvägen i en annan kulör än grannarnas?",
     "Området är utpekat som särskilt värdefullt och färgskalan räknas som bevarandevärd, så fråga kommunen innan. Ett kulörbyte som påverkar områdets karaktär kan kräva bygglov där."),
    ("Vilken kulör ska gavelpanelen ha på ett kedjehus i Ägget?",
     "Underlaget beskriver gavelpanel i kontrasterande kulörer som svart, blått, gult eller brunt. Utgå från den kulör din hustyp har i dag och stäm av med kommunen om du vill byta."),
    ("Gäller lovfriheten för ny kulör även i Väsby villastad?",
     "Kommunen skriver att lov kan krävas i särskilt värdefulla områden när ändringen påverkar karaktären, och villastaden är utpekad i kunskapsunderlaget. Kontakta kommunen innan du byter kulör."),
    ("Varför spelar putsens ålder roll för vilken färg som används?",
     "Puts från 1900-talets mitt innehåller ofta cement, och kalkfärg fäster dåligt på cementrika underlag. Därför tar vi reda på vad putsen och den gamla färgen består av innan färg väljs."),
    ("Kan flera grannar i samma radhuslänga beställa målning tillsammans?",
     "Ja. Vi kan ta fram ett gemensamt kostnadsförslag där varje hus redovisas för sig, och ställningen kan flyttas mellan husen."),
  ],
  "sources": [
    ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö i Upplands Väsby 2025 (pdf)",
     "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf"),
    ("Upplands Väsby kommun – Fasadändring",
     "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/fasadandring"),
    _BOV, _RAA, _SKV, _SKV2,
  ],
  "cta": ("Ska huset i Väsby målas om?", "Boka ett gratis platsbesök så går vi igenom puts, panel och kulör på plats."),
  "img": [
    ("Putsade radhus i jordfärger med spröjsade fönster, tegeltak och små takkupor",
     "a long low 1940s Swedish folkhem terraced house row (radhuslänga) in Upplands Väsby, simple Scandinavian style like Stockholm suburbs, one and a half storeys, flat facades without bay windows or arches, rough rendered facades in muted earth pigments, ochre, sage green and beige, small white painted wooden windows with glazing bars, each window flanked by a pair of painted wooden window shutters in blue or brown, steep red clay tile roof with a row of small sheet metal dormers and a few plain chimneys, simple wooden front doors, gravel paths, birch trees and low hedges, Upplands Väsby Sweden, not British, not Dutch, autumn daylight, no people"),
    ("Radhus från 1960-talet med vitt tegel, mörk liggande panel och mörka plank",
     "1960s Swedish single-storey terraced houses with white brick facades, dark painted horizontal wooden fascia panel under a low roof, dark painted plinth, dark wooden horizontal board fences around small courtyards, lawn in front, Upplands Väsby, overcast day, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ENSKEDE
"malare-enskede.html": {
  "kind": "district", "service": "malare", "ort": "Enskede", "svc_label": "Målare",
  "title": "Målare i Enskede – rödfärg, gul puts och småstugor",
  "description": "Målare i Enskede: rödfärgad panel och gul kalkputs i Gamla Enskede, ljusa kulörer i Enskededalen och på småstugorna och lovplikten i riksintresset.",
  "h1": "Målare i Enskede",
  "lead": "Gamla Enskede byggdes för att hänga ihop, och färgen var en del av helheten. När Stadsmuseet inventerade området 1974 konstaterade museet att alla hustyper från början hade enhetliga fasad- och takmaterial och en samstämmig färgsättning. Geal Entreprenad AB målar fasader, fönster och snickerier ute och inne i Enskede, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Trädgårdsstad, egnahem och småstugor i Enskede.",
  "sections": [
    {"id": "gamla-enskede", "anchor": "Gamla Enskede",
     "h2": "Tjära, rödfärg och gul kalkputs",
     "paras": [
       "Gamla Enskede blev Stockholms första trädgårdsstad, anlagd efter stadsplanedirektören Per Olof Hallmans plan. Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur det nationalromantiska blev tydligt här, med branta takfall och småspröjsade fönster. Fasaderna var ofta av liggande träpanel eller spån som tjärades eller målades med röd slamfärg, men även puts förekom.",
       "Stadsmuseets inventering ger detaljerna typhus för typhus. Ett friliggande enfamiljshus beskrivs med rödfärgad, liggande fasspontpanel och vita foder och lister, ett annat med kalkputsad fasad i sprit- och slätputs, avfärgad i en gul färgton. Stockholmskällans text om Sockenplan sammanfattar att arkitekterna ofta arbetade om den röda stugan med vita knutar, och att putsade hus oftast avfärgades i ljusa kulörer.",
       "Samma inventering beskriver hur området förändrades. Trähus som länge underhållits med traditionella material och metoder och målats om då och då försvann ibland bakom en fasad av eternit eller plåt. Museet noterade också motsatsen: husägare som bytte gammal panel mot ny av samma typ, och eternit från 1950-talet som plockats bort så att huset åter framstod som ett trähus.",
     ],
     "aside": {"title": "Ur inventeringen", "items": [
       "Rödfärgad liggande fasspontpanel", "Vita foder och lister",
       "Kalkputs avfärgad i gul färgton", "Från början samstämmig färgsättning"]}},
    {"id": "dalen-faltet", "h2": "Enskededalen och Enskedefältet: ljusa toner i få kulörer",
     "paras": [
       "Söder om kärnan blev formspråket ett annat. I Enskededalen blev 1920-talets klassiska stil rådande, enligt vägledningen: enkla volymer i ett och ett halvt plan, symmetriska fasader, stående träpanel med tunn lockläkt och en färgskala i ljusa, dämpade toner av grönt, gult eller grått.",
       "Mellan 1930 och 1932 restes över 400 småstugor på Enskedefältet av självbyggare, med fasader av oljemålad träpanel. I stadens småstugeområden var färgsättningen från början strikt reglerad och begränsad till ett fåtal kulörer, ofta ljusa nyanser av grått, grönt och gult. Rödfärg fick användas efter särskild ansökan.",
       "Den som vill veta hur en småstuga såg ut från början har ett bra underlag. Stadsbyggnadskontoret samlade i slutet av 1970-talet alla typritningar för småstugorna mellan 1927 och 1957 i en sammanställning, just för att ge underlag till dem som ville ändra sina stugor. Ritningen visar fönster, panel och detaljer som är lätta att tappa bort vid en ommålning.",
     ],
     "aside": {"title": "Färgskalan", "items": [
       "Enskededalen: ljusa, dämpade toner", "Småstugor: få kulörer i grått, grönt, gult",
       "Rödfärg efter särskild ansökan", "Typritningar 1927–1957 finns samlade"]}},
    {"id": "lov-enskede", "h2": "Riksintresset gör kulörbytet lovpliktigt",
     "paras": [
       "Gamla Enskede är utpekat som riksintresse för kulturmiljövården. Sedan 1 december 2025 är kulörbyten på en- och tvåbostadshus i regel lovfria, men Stockholms stad skriver att du behöver söka bygglov för annars lovbefriade åtgärder om fastigheten ligger inom ett riksintresse för kulturmiljövården, i ett område som är utpekat som särskilt kulturhistoriskt värdefullt eller är blå- eller grönmarkerad i Stadsmuseets karta.",
       "Utanför riksintresset avgör kartan och detaljplanen. Gult eller grått utan andra skydd betyder normalt inget lov, medan streckade ytor är miljöer som ännu inte inventerats och kan kräva lov. Stadsmuseet ger rådgivning om du mejlar adress, fastighetsbeteckning, byggnadsår, ombyggnader och foton av fasaderna, och museet brukar svara inom tre veckor.",
       "Boverket räknar ommålning i samma kulör som underhåll. Att byta färgtyp är inget kulörbyte, men det kan påverka husets karaktärsdrag, och i ett område där inventeringen beskriver oljemålad panel och kalkavfärgad puts hör frågan till samma bedömning.",
     ],
     "aside": {"title": "Kontrollera före beställning", "items": [
       "Riksintresse: lov för ny kulör", "Blått eller grönt i kartan: lov",
       "Streckat: inte inventerat ännu", "Gult eller grått: normalt lovfritt"]}},
    {"id": "kalkputs-enskede", "h2": "Gul kalkputs och oljemålad panel",
     "paras": [
       "Den gula tonen på en kalkputsad Enskedevilla kan komma från järnvitriol. Riksantikvarieämbetet skriver att järnvitriol inte är ett pigment utan reagerar med kalken och ger en gulröd verkan, och att den nya kalkfärgen ofta också behöver lite järnvitriol när den gamla avfärgningen innehåller det. Skador lagas med kalkputs lik den befintliga, och putsen ska ha karbonatiserat i minst tre till fyra veckor innan den målas.",
       "På panelen är förarbetet avgörande. Fasaden tvättas, avflagnad färg skrapas bort och grått, luddigt trä slipas fram till friskt virke. Rötskadat ändträ lagas med nytt trä innan något grundas. I parhusen och radhusen är det extra viktigt att båda halvorna får samma kulör och glans.",
       "Ska teglet läggas om medan ställningen ändå står uppe, läs mer om " + _L.format("takrenovering-enskede.html", "takrenovering i Enskede") + " eller " + _L.format("taklaggare-enskede.html", "takläggare i Enskede") + ". Inomhus målar vi väggar, tak och snickerier och tapetserar.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Enskede till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, puts, fönster och snickerier och gör skrapprov för att se färgtyp och äldre kulörer."),
    ("Riksintresse och karta", "Vi kontrollerar om huset ligger i riksintresset, hur det är klassat och vad detaljplanen säger."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, förarbete och antal strykningar står med, så att förslaget kan bifogas en ansökan."),
    ("Förarbete", "Tvätt, skrapning, lagning av trä och puts, kittning av fönster och skydd av trädgården."),
    ("Målning", "Grundning och strykningar i lämpligt väder, med de torktider färgtypen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Enskede",
  "rot": [
    "Skatteverket räknar målning av fasader, fönster, väggar och tak och tapetsering som rotarbete i ett småhus. Målning av staket och murar ger inget avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Färg, material och resor ger inget avdrag. Är ni två som äger huset kan ni båda använda ert utrymme. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "I Gamla Enskede väger snickerier, spröjsade fönster och verandor tungt, och kalkputs kräver lagning och väntetid innan den kan målas. På småstugorna är det oftare panelens skick och mängden skrapning som styr. Tomterna är små och gatorna smala, så ställningen planeras vid besöket. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi måla om vår rödfärgade villa i Gamla Enskede i en ljusare kulör?",
     "Inom riksintresset krävs bygglov för ett kulörbyte. Inventeringen visar att färgsättningen var samstämmig från början, så räkna med att staden väger in områdets helhet."),
    ("Var hittar man den ursprungliga ritningen till en småstuga på Enskedefältet?",
     "Typritningarna för småstugorna 1927–1957 finns samlade, och stadens äldre typritningssamlingar och miljöprogram går att beställa. Ritningen är ett bra stöd när fönster, panel och detaljer ska målas."),
    ("Varför blir kalkfärgen lite flammig på vår gula puts?",
     "Det är en egenskap hos kalkfärg. Riksantikvarieämbetet beskriver dess levande, något flammiga yta som en av de mest uppskattade egenskaperna."),
    ("Hur länge måste en putslagning vänta innan den kan målas?",
     "Kalkputsen ska ha karbonatiserat, vilket tar minst tre till fyra veckor. Därför planerar vi lagningar i god tid före målningen."),
    ("Måste båda halvorna av ett parhus i Enskede målas samtidigt?",
     "Nej, men de bör få samma kulör och glans. Vill någon av er byta kulör inom riksintresset krävs dessutom bygglov."),
  ],
  "sources": [
    ("Stockholmskällan / Stadsmuseet – Gamla Enskede, byggnadsinventering 1974 (pdf)",
     "https://stockholmskallan.stockholm.se/postfiles/KUL/SSM_Gamla_Enskede__byggnadsinventering_1974_1977_00.pdf"),
    ("Stockholmskällan – Stockholms spår: Sockenplan (pdf)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000049.pdf"),
    _VARSAM, _STH_KLASS, _STH_FASAD, _BOV, _RAA, _SKV2,
  ],
  "cta": ("Ska huset i Enskede målas om?", "Boka ett gratis platsbesök så går vi igenom färglager, kulör och riksintresset på plats."),
  "img": [
    ("Röd trävilla med vita knutar och brant tegeltak i Gamla Enskede",
     "1910s Swedish national romantic wooden garden-city house with horizontal panel painted falu red, white corner boards and window trims, small-paned windows, steep red clay tile roof with a dormer, small front veranda, white picket fence and fruit trees, narrow curving street, Gamla Enskede Stockholm, spring daylight, no people"),
    ("Gul putsad fasad bredvid ett vitt fönster på en äldre villa",
     "close-up of a yellow ochre lime-washed rendered wall of an old Swedish villa with a slightly mottled lime paint texture, a freshly patched area of lime render that is still lighter, edge of a white painted wooden window frame, soft daylight, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"malare-alvsjo.html": {
  "kind": "district", "service": "malare", "ort": "Älvsjö", "svc_label": "Målare",
  "title": "Målare i Älvsjö – villastadens färgton och snickerier",
  "description": "Målare i Älvsjö: villastadens godkända färgtoner, vit puts och mörkbrun panel, faluröda hus med vita snickerier och villorna i Långbro och Herrängen.",
  "h1": "Målare i Älvsjö",
  "lead": "När AB Hem på landet sålde tomterna i Älvsjö villastad stod det i köpekontrakten att husets yttre färgton skulle godkännas av bolaget. Det är en del av förklaringen till att villastaden fortfarande hänger ihop. Geal Entreprenad AB målar ute och inne i Älvsjö, Långbro, Herrängen, Solberga och Örby, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villastad, egnahem och småstugor i Älvsjö.",
  "sections": [
    {"id": "villastaden", "anchor": "Villastadens hus",
     "h2": "Två hustyper och en godkänd färgton",
     "paras": [
       "Stadsmuseets förortsinventering av Älvsjö villastad, beskriven av Suzanne Lindhagen, visar hur området byggdes ut efter 1908. Bolaget ställde krav i kontrakten: tomterna fick inte styckas, varje tomt skulle bebyggas inom två år med en enda byggnad efter en ritning som bolaget godkänt, och färgtonen skulle godkännas för att undvika färger som inte harmonierade med grannhusen.",
       "Inventeringen beskriver två vanliga hustyper. Den ena hade vit slätputsad bottenvåning, gavelspetsar klädda med mörkbrunmålad panel på förvandring och småspröjsade fönster med luckor. Den andra hade falurödfärgad träpanel och vitmålade snickerier, ibland med utsågade hjärtan som dekor. Båda fanns kvar i nästan ursprungligt skick när museet gjorde sin genomgång.",
       "Samma text konstaterar att många hus från 1910- och 20-talen hade byggts om eller till i flera omgångar, och att nya fasad- och takmaterial, nya färgtyper och tilläggsisolering hade bidragit till att husens ursprungliga karaktär gått mer eller mindre förlorad.",
     ],
     "aside": {"title": "Hustyperna", "items": [
       "Vit slätputs i bottenvåningen", "Mörkbrun panel i gavelspetsarna",
       "Faluröd panel med vita snickerier", "Småspröjsade fönster med luckor"]}},
    {"id": "langbro-herrangen", "h2": "Långbro, Herrängen och Örby: variation i trä",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden räknar delar av Långbro och Herrängen, Liseberg, Örby, Långsjö och delar av Älvsjö till typen villastad. Villastäderna var privat organiserade och fick en brokigare bebyggelse än stadens egnahemsområden. Trä var det dominerande fasadmaterialet, även om puts förekom, och glasverandor, takkupor, snickarglädje och färgsättning gav stadsdelarna en variation som fortfarande syns.",
       "Vägledningen ger samma råd för alla villastäder: ta tillvara eller återskapa karaktärsskapande material, kulörer, byggnadsdelar och detaljer så långt det går vid ombyggnader och renoveringar. Material och färgsättning räknas dessutom till de aspekter som har stor påverkan på områdets karaktär.",
       "Andra delar av Långbro och Herrängen byggdes som småstugeområden. Där är husen typritade, uteslutande i trä med fönster i fasadliv och stående lockläktpanel, och kulörerna hölls från början till ett fåtal ljusa. På sådana hus är det snarare enhetligheten med grannhusen än det individuella uttrycket som ska bevaras.",
     ],
     "aside": {"title": "Typiska detaljer", "items": [
       "Glasverandor med många spröjs", "Takkupor och snickarglädje",
       "Fönsterluckor och dekorbrädor", "Lockläktpanel på småstugorna"]}},
    {"id": "lov-alvsjo", "h2": "Detaljplanen och kartan avgör",
     "paras": [
       "Stockholms stad skriver att det inte längre krävs bygglov för fasadändringar på en- eller tvåbostadshus om vissa förutsättningar är uppfyllda. Utökad lovplikt gäller bland annat om huset är en särskilt kulturhistoriskt värdefull byggnad eller ligger i ett särskilt kulturhistoriskt värdefullt område, och Stadsmuseets klassificeringskarta ger en första indikation. Byte av kulör räknas uttryckligen som en fasadändring.",
       "En fasadändring som inte kräver lov ska ändå stämma överens med detaljplanen, och detaljplanen kan innehålla bestämmelser som skyddar en byggnad eller kräver lov även när lagen inte gör det. Planen för din fastighet hittar du i stadens e-tjänst Bygg- och plantjänsten.",
       "Vill du veta mer om ditt område går det att beställa stadens äldre miljöprogram och typritningssamlingar. De har ingen juridisk status vid bygglovsprövningen, men staden beskriver dem som ett bra underlag för att förstå områdets karaktär. Mer om husen och taken i stadsdelen finns under " + _L.format("takrenovering-alvsjo.html", "takrenovering i Älvsjö") + ".",
     ],
     "aside": None},
    {"id": "snickerier-alvsjo", "h2": "Luckor, dekorbrädor och glasverandor",
     "paras": [
       "Det är snickerierna som slits först. Riksantikvarieämbetet skriver att ommålning behöver göras oftare på utsatta delar som fönstersnickerier, vindskivor och sydfasader, och att mild rengöring och bättring av skadade partier är ett utmärkt sätt att förlänga livslängden på oljefärg som i övrigt är intakt. En rätt sammansatt linoljefärg har enligt handboken en livslängd på cirka 15–20 år.",
       "Fönsterluckor, dekorbrädor med utsågade hjärtan och verandornas spröjs målas bäst nedtagna eller i lugn takt på plats: skrapning, lagning av trä, grundning, mellanstrykning och slutstrykning. Linoljefärg är övermålningsbar efter ungefär ett till tre dygn i varmt och torrt väder, och för långa uppehåll mellan strykningarna bör undvikas.",
       "Den vita slätputsen i bottenvåningen kräver en annan färg än panelen ovanför. Handboken skriver att kalkfärg fäster bra på kalkputs men dåligt på cementrika underlag, så vi tar reda på vad putsen består av innan färgen väljs. Ska taket ses över samtidigt, läs om " + _L.format("taklaggare-alvsjo.html", "takläggare i Älvsjö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Älvsjö till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, puts, luckor och verandor och gör skrapprov för att se färgtyp och äldre kulörer."),
    ("Karta och detaljplan", "Klassningen i Stadsmuseets karta och detaljplanen kontrolleras innan en ny kulör beställs."),
    ("Skriftligt kostnadsförslag", "Fasad, snickerier och fönster redovisas för sig, med färgtyp, kulör och antal strykningar."),
    ("Förarbete", "Tvätt, skrapning, lagning av trä och puts och kittning av fönster."),
    ("Målning", "Puts och panel målas med var sin lämplig färg, i lämpligt väder."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Älvsjö",
  "rot": [
    "I en villa eller ett radhus med äganderätt räknar Skatteverket fasadmålning, fönstermålning och invändig målning som rotarbete, liksom rengöring av fasader. Att måla staket och murar ger inget avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och tillsammans med rutavdrag högst 75 000 kr.",
    "Färgen räknas som material och ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset?",
  "price": [
    "I Älvsjö styrs kostnaden ofta mer av snickerierna än av fasadytan: antalet fönster med spröjs och luckor, glasverandor, dekorbrädor och vindskivor. Hus som byggts till i flera omgångar kan ha olika underlag på olika delar. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Gäller Hem på landets regler om färgton fortfarande i Älvsjö villastad?",
     "Nej, kravet stod i de gamla köpekontrakten. I dag är det plan- och bygglagen, detaljplanen och husets klassning som avgör om en ny kulör kräver lov."),
    ("Kan man bättringsmåla bara de mest utsatta delarna av villan?",
     "Ja. Fönster, vindskivor och söderfasad slits fortare, och en bättring av dem kan skjuta upp en hel ommålning några år."),
    ("Vilken färg passar på den vita slätputsen i bottenvåningen?",
     "Det beror på putsen. Kalkfärg fungerar på kalkputs men fäster dåligt på cementrik puts, så vi undersöker underlaget först."),
    ("Hur målar ni om fönsterluckor och dekorsnickerier?",
     "Helst nedtagna. De skrapas, lagas, grundas och målas i lugn takt och sätts sedan tillbaka, så att även kanter och baksidor får färg."),
    ("Behöver vi bygglov för ny kulör på villan i Örby?",
     "Kontrollera Stadsmuseets klassificeringskarta och detaljplanen. Är huset blå- eller grönmarkerat eller har planen skyddsbestämmelser krävs lov."),
  ],
  "sources": [
    ("Stockholmskällan / Stadsmuseet – Suzanne Lindhagen: Älvsjö villastad, ett exempel på förortsinventering (pdf)",
     "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf"),
    _VARSAM, _STH_FASAD, _STH_KLASS, _RAA, _SKV, _SKV2,
  ],
  "cta": ("Ska villan i Älvsjö målas om?", "Boka ett gratis platsbesök så går vi igenom snickerier, puts och kulör på plats."),
  "img": [
    ("Villa i Älvsjö med vit putsad bottenvåning och mörkbrun panel i gavelspetsen",
     "1910s Swedish villa with smooth white rendered ground floor and dark brown painted wooden panel in the upper gable, small-paned white windows with wooden shutters, steep red clay tile roof, lilac bushes and apple trees in the garden, quiet villa street, Älvsjö Stockholm, early summer, no people"),
    ("Faluröd panel med vita fönsterfoder och en vit dekorbräda med utsågade hjärtan",
     "detail of a falu red painted wooden house facade with white painted window trim and a white decorative fretwork board with cut-out heart shapes under the eaves, old Swedish villa, soft daylight, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HÄSSELBY
"malare-hasselby.html": {
  "kind": "district", "service": "malare", "ort": "Hässelby", "svc_label": "Målare",
  "title": "Målare i Hässelby – villastad, grupphus och radhus",
  "description": "Målare i Hässelby: trävillor med glasverandor i villastaden, grupphus med gemensam färgsättning, tegelradhus i Hässelby strand och gamla fasadskivor.",
  "h1": "Målare i Hässelby",
  "lead": "I Hässelby kan en trävilla med glasveranda från villastadens första tid ligga granne med ett grupphusområde där alla hus har samma kulör. Det som är rätt färgsättning på det ena huset är sällan rätt på det andra. Geal Entreprenad AB målar ute och inne i Hässelby villastad, Hässelby gård och Hässelby strand, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villastad, grupphus och radhus i Hässelby.",
  "sections": [
    {"id": "villastaden-hasselby", "anchor": "Villastaden",
     "h2": "Villastaden: individuella hus i trä",
     "paras": [
       "Hässelby villastad hör enligt stadens vägledning Varsam utveckling av småhus- och villaområden till typen villastad. Villastäderna var privat organiserade, och bebyggelsen blev därför brokigare än i de egnahemsområden som staden planerade. Trä var det dominerande fasadmaterialet, även om puts förekom, och glasverandor, takkupor, snickarglädje och färgsättning gav husen en variation som fortfarande syns.",
       "Stadsmuseet inventerade Hässelby villastad med Lambarön under sina förortsinventeringar i slutet av 1970-talet. Inventeringarna skulle bland annat fungera som underlag vid plan- och rivningsärenden och visa vad som fanns kvar av den äldsta bebyggelsen.",
       "För en målare innebär villastaden att varje hus behöver bedömas för sig. En villa med glasveranda och profilerade foder har ofta haft en annan färgsättning än grannhuset från 1940-talet, och skrapprov på skyddade ställen visar vilka kulörer som har suttit på. Vägledningen råder att ta tillvara eller återskapa karaktärsskapande material, kulörer och detaljer så långt det går.",
     ],
     "aside": {"title": "Villastaden i korthet", "items": [
       "Privat organiserad bebyggelse", "Trä dominerar, puts förekommer",
       "Glasverandor och snickarglädje", "Varje hus bedöms för sig"]}},
    {"id": "grupphus-hasselby", "h2": "Grupphusen: en färgskala för hela gruppen",
     "paras": [
       "Under 1960- och 1970-talen ersattes många villor i Hässelby villastad av täta, sammanhållna grupper av enhetlig småhusbebyggelse, enligt vägledningen. Marken kunde utnyttjas bättre med mindre tomter och gemensamma parkeringsytor, och stadsdelen fick delvis en helt annan karaktär.",
       "I sådana grupper är det helheten som räknas. Vägledningen nämner grupphusområdenas sammanhållna karaktär, med exempelvis enhetlig skala, färgsättning och byggnadsmaterial, som ett karaktärsdrag, och råder att förändringar i sammanhållna grupper av villor, radhus och kedjehus utformas utifrån ett helhetsperspektiv.",
       "I praktiken betyder det att kulör, glans och kulörsättning på dörrar, vindskivor och plank bör vara densamma hus för hus. Planerar flera grannar att måla samma sommar kan ställning och förarbete samordnas, och en gemensam kulörlista gör det lättare att hålla ihop gruppen när husen målas vid olika tillfällen.",
     ],
     "aside": None},
    {"id": "strand-gard", "h2": "Hässelby strand och gård: tegel, puts och fasadskivor",
     "paras": [
       "Hässelby strand och Hässelby gård hör i vägledningen till de gruppbyggda småhusområdena i tunnelbanestaden. Hässelby gård planerades samtidigt som Råcksta och ingick i Vällingby centrums omland, och i tunnelbanestäderna trappades skalan ner från högre hus vid centrum till grupper av rad- och kedjehus längst ut. Fasader i rött tegel var vanliga, men det förekom även puts och skivor i fibercement.",
       "Vägledningen nämner just Hässelby som exempel på att nya material prövades. Ett populärt material var asbestcement, mer känt som eternit, som innehöll asbest och i många fall har bytts ut. Det finns numera fasadskivor utan asbest, vilket enligt vägledningen gör det möjligt att behålla radhusens uttryck.",
       "På ett tegelradhus är det sällan teglet som målas, utan fönster, dörrar, plank, vindskivor och panelpartier. Sitter det kvar äldre fasadskivor behöver vi veta vad de består av innan de tvättas eller slipas, och skivor som ska bytas hör hemma under " + _L.format("fasadrenovering.html", "fasadrenovering") + " snarare än målning.",
     ],
     "aside": {"title": "Vanliga fasader", "items": [
       "Rött tegel med målade träpartier", "Puts på delar av husen",
       "Fibercementskivor, ibland utbytta", "Målade dörrar, plank och vindskivor"]}},
    {"id": "lov-hasselby", "h2": "Kulör, detaljplan och samma färgtyp som förut",
     "paras": [
       "Stockholms stad skriver att bygglov för fasadändringar på en- och tvåbostadshus inte längre krävs om vissa förutsättningar är uppfyllda, men att utökad lovplikt bland annat gäller i särskilt kulturhistoriskt värdefulla byggnader och områden. Stadsmuseets klassificeringskarta ger en första indikation, och lovfria fasadändringar ska ändå stämma överens med detaljplanen eller kunna ses som en liten avvikelse från den.",
       "Riksantikvarieämbetet råder att i de flesta fall hålla sig till samma färgtyp som tidigare vid ommålning, särskilt utomhus på ytor som har målats med linoljefärg, slamfärg, trätjära eller kalkfärg. Att måla över äldre färgtyper med moderna material innebär en teknisk risk, och nästa underhåll kan bli komplicerat. Boverket påpekar på sin sida att ett byte av färgtyp kan bedömas påverka husets karaktärsdrag.",
       "Mer om husen och taken i stadsdelen finns under " + _L.format("taklaggare-hasselby.html", "takläggare i Hässelby") + ". Inomhus målar vi väggar, tak, snickerier och dörrar och tapetserar.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Hässelby till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, puts, tegelhusets träpartier och fönster och gör skrapprov där det behövs."),
    ("Klassning och plan", "Stadsmuseets karta och detaljplanen kontrolleras, och i grupphusområden stämmer vi av den gemensamma kulören."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, förarbete och antal strykningar står med, även för flera hus i samma grupp."),
    ("Förarbete", "Tvätt, skrapning, lagning av trä och kittning av fönster."),
    ("Målning", "Grundning och strykningar i lämpligt väder, med de torktider färgen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Hässelby",
  "rot": [
    "För villor och radhus med äganderätt räknar Skatteverket målning av fasader, fönster, väggar, tak och golv som rotarbete, men inte målning av staket och murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "I en bostadsrätt ger målning av fönster och ytterdörrar bara avdrag för insidan. Färg och material räknas inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "På villastadens trähus är det snickerierna, verandorna och mängden skrapning som styr. På tegelradhusen är ytorna mindre men detaljerna många: dörrar, plank, vindskivor och fönster. Målas flera hus i en grupp samtidigt kan etableringen delas. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi välja egen kulör på vårt hus i ett grupphusområde i Hässelby?",
     "Är huset inte klassat eller skyddat i detaljplanen är kulörbytet normalt lovfritt. Stadens vägledning lyfter ändå fram den enhetliga färgsättningen, så stäm av med grannarna och samfälligheten först."),
    ("Kan ni måla de gamla fasadskivorna på vårt radhus?",
     "Först behöver vi veta vad skivorna består av. Eternit innehöll asbest, så äldre skivor ska inte bearbetas förrän materialet är utrett, och ska de bytas är det ett fasadarbete snarare än målning."),
    ("Vi har en villa med glasveranda i Hässelby villastad – vad ska vi tänka på?",
     "Verandan har många spröjs och smala delar som slits fort. Planera den som en egen del i arbetet och behåll den färgtyp som sitter på."),
    ("Varför ska vi inte stryka modern färg över den gamla linoljefärgen?",
     "Riksantikvarieämbetet varnar för att det innebär en teknisk risk och kan göra nästa underhåll svårt. Det går inte heller enkelt att gå tillbaka utan att ta bort all färg."),
    ("Hur vet jag om huset i Hässelby är klassat?",
     "Sök adressen i Stadsmuseets klassificeringskarta. Är du osäker kan du mejla museet med adress, byggnadsår och foton och få en bedömning."),
  ],
  "sources": [
    _VARSAM,
    ("Stockholmskällan / Stadsmuseet – Suzanne Lindhagen: Älvsjö villastad, ett exempel på förortsinventering (pdf)",
     "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf"),
    _STH_FASAD, _STH_KLASS, _BOV, _RAA, _SKV2,
  ],
  "cta": ("Ska huset i Hässelby målas om?", "Boka ett gratis platsbesök så går vi igenom fasad, färgtyp och kulör på plats."),
  "img": [
    ("Trävilla med glasveranda och snickarglädje i Hässelby villastad",
     "1910s Swedish wooden villa with a glazed veranda and decorative carpentry, light grey-green painted wooden panel, white trims, steep red clay tile roof with a dormer, large garden with fruit trees, villa street, Hässelby villastad Stockholm, early autumn daylight, no people"),
    ("Radhuslänga från 1960-talet med rött tegel och målade dörrar och träpartier",
     "row of 1960s Scandinavian modernist terraced houses in a Stockholm suburb, two storeys, red brick facades combined with painted wooden panel sections in muted green, simple windows without glazing bars, low pitched roof with dark concrete tiles and no chimneys, painted wooden front doors, small front gardens with low hedges and birch trees, pedestrian path in front, Hässelby strand Stockholm, overcast day, no people, no antennas, no dishes, no chimney pots"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SIGTUNA
"malare-sigtuna.html": {
  "kind": "district", "service": "malare", "ort": "Sigtuna", "svc_label": "Målare",
  "title": "Målare i Sigtuna – stadens färgsättningstradition",
  "description": "Målare i Sigtuna: bevarandeplanens kulörer och färgtyper, lov för kulörbyte i riksintresset, fönster och kitt och villorna i Märsta. Gratis platsbesök.",
  "h1": "Målare i Sigtuna",
  "lead": "Få småstäder har sin färghistoria så noga beskriven som Sigtuna. Kommunens bevarande- och förnyelseplan går igenom stadens fasadkulörer från 1700-talet fram till i dag och ger råd om färgtyper för både gamla och yngre hus. Geal Entreprenad AB målar ute och inne i Sigtuna stad, Märsta och resten av kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Stadskärnan, Märsta och Rosersberg.",
  "sections": [
    {"id": "fargtradition", "anchor": "Färgtraditionen",
     "h2": "Från gul slamfärg till trefärgade fasader",
     "paras": [
       "Bevarande- och förnyelseplanen för Sigtuna stad antogs av kommunfullmäktige den 28 november 2019 och är enligt planen tungt vägledande för planarbete och bygglov. Kapitlet om färgsättning är hämtat från den tidigare planen från 1986, där arkitekten Peter von Knorring analyserade panelarkitekturens fasadfärger från 1850 till 1930. Underlaget bygger på provtagningar på ett tjugotal äldre fasader, brandförsäkringar och äldre målningar.",
       "Planen beskriver Sigtuna under 1700-talet som en gul stad, med gult slamfärgade timmerväggar och oljemålade snickerier på de viktigare husen, medan den enklare bebyggelsen troligen var rödfärgad. Kring 1850–60-talet målades de nypanelade husen oftast med rödfärg. Omkring 1870 kom ljusa pastellfärger, rosa eller ljusgrönt, ofta med vita knutar, och vid sekelskiftet dominerade ljusgult och gröngrått.",
       "Under 1920-talet slog en murrig färgskala igenom vid restaureringar, med olivgrönt, mörkgult och brunt och gröna eller bruna fönster, medan Malmen höll fast vid pastellerna. Sedan slutet av 1990-talet har man enligt planen ofta återskapat äldre husens kraftigare kulörer, gärna med olika färg på fasad, listverk och detaljer, och trefärgade fasader med kulörta fönsterbågar är vanliga.",
     ],
     "aside": {"title": "Epoker i korthet", "items": [
       "1700-tal: gul slamfärg på timmer", "1850–60-tal: rödfärgad panel",
       "Sekelskiftet: ljusgult och gröngrått", "1920-tal: olivgrönt och mörkgult"]}},
    {"id": "lov-sigtuna", "h2": "Kulörbyte i stadskärnan kräver bygglov",
     "paras": [
       "Planen är tydlig: inom riksintresset för kulturmiljövården för Sigtuna stad gäller inte de bygglovsbefriade åtgärderna. Vid fasadförändringar som kulörbyte ska fastighetsägaren därför ansöka om bygglov. Planen påminner också om att ändringar ska utföras varsamt oavsett om en byggnad är särskilt värdefull eller inte, så att dess värden inte går förlorade.",
       "Boverket räknar ommålning i samma kulör som underhåll, medan byte av färgtyp, till exempel från linoljefärg till plastfärg, kan bedömas påverka husets yttre karaktärsdrag. Planen råder till försiktighet med nya kulörer som helvitt, grått och svart i den historiska miljön, men skriver att de kan fungera utmärkt i ett nutida sammanhang.",
       "Utanför stadskärnan finns andra underlag. På sin sida om att bygga i kulturmiljö skriver kommunen att även byggnader och områden som inte är utpekade i något program kan vara så värdefulla att särskild hänsyn behövs, och att dalgången Odensala–Hova har särskilda riktlinjer. Kommunen uppmanar den som är osäker att höra av sig.",
     ],
     "aside": {"title": "I riksintresset", "items": [
       "Kulörbyte: sök bygglov", "Planen är tungt vägledande",
       "Samma kulör: normalt underhåll", "Odensala–Hova: egna riktlinjer"]}},
    {"id": "fargtyper-sigtuna", "h2": "Linolja, slamfärg och mineralisk färg",
     "paras": [
       "Planen rekommenderar traditionella material och metoder för utvändig målning även på hus som byggdes så sent som på 1950-talet, till exempel slamfärg på ohyvlad panel på enklare byggnader och oljefärg på utsatta partier som fönster. Väljer man ändå en modern färgtyp rekommenderas att obehandlat trävirke grundas med traditionell linoljefärg, eftersom den tränger in bättre och ökar virkets livslängd.",
       "Moderna färger kan ge traditionella kulörer, men planen påpekar att de åldras på ett främmande sätt och har en annan glans och struktur. För nya hus i stadskärnan anger riktlinjerna att hyvlade träfasader målas med täckande oljefärg, ohyvlade bräder med falu rödfärg och putsfasader med mineralisk färg utan organiska inslag som akrylharts. Vid ombyggnad ska ett hus som målats med falu rödfärg få behålla samma ytbehandling.",
       "Tillgången är god. Planen skriver att det i dag finns provsamlingar med ett tjugotal traditionella pigment, att Riksantikvarieämbetet har tagit fram provsamlingar för linoljefärg och kalkfärg och att de traditionella kulörerna finns översatta till NCS-systemet. Linoljefärg säljs även i vanliga välsorterade måleributiker.",
     ],
     "aside": None},
    {"id": "fonster-sigtuna", "h2": "Fönster, dörrar och husen i Märsta",
     "paras": [
       "Om fönstren ger planen konkreta råd. Nya fönster ska vara trogna kopior av de befintliga, fönsterkittet ska vara övermålningsbart och även gångjärnen ska målas i fönstrens kulör. Ett gammalt fönster bör enligt planen i första hand repareras, och glasrutorna spelar en viktig roll för husets uttryck: de äldsta glasen är munblåsta med små blåsor, mellan 1915 och 1960 är de flesta glasen maskindragna, och sedan 1970-talet används floatglas som kan uppfattas som mörka hål i fasaden. Det är ett skäl att kitta om och behålla gamla rutor.",
       "Märsta, Rosersberg och Steninge ligger utanför bevarandeplanens område, och där gäller i regel plan- och bygglagens lovfrihet för kulörbyte på en- och tvåbostadshus, så länge huset inte är särskilt värdefullt och detaljplanen inte säger annat. Där handlar uppdragen oftare om villor och radhus där panel, vindskivor och fönster målas om.",
       "Ska taket ses över när ställningen ändå står uppe, läs mer under " + _L.format("taklaggare-sigtuna.html", "takläggare i Sigtuna") + ". Inomhus målar vi väggar, tak, snickerier och dörrar och tapetserar i hela kommunen.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Sigtuna till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, puts, fönster och snickerier och gör skrapprov för att se färgtyp och äldre kulörer."),
    ("Plan och lov", "Vi kontrollerar om huset ligger i riksintresset och vad bevarandeplanen säger, och om ny kulör kräver bygglov."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, förarbete och antal strykningar skrivs ut, så att förslaget kan bifogas en ansökan."),
    ("Förarbete", "Tvätt, skrapning, lagning av trä, kittning med övermålningsbart kitt och grundning."),
    ("Målning", "Strykningarna görs i lämpligt väder och med de torktider färgtypen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och noterar vilka färger som använts."),
  ],
  "rot_h2": "ROT-avdrag för målning i Sigtuna",
  "rot": [
    "Skatteverket räknar målning av fasader, fönster, väggar, tak och element som rotarbete i ett småhus, medan målning av staket och murar inte ger avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Du behöver äga huset när arbetet görs och bo i det, året runt eller som fritidsbostad. Färg och resor räknas inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "I stadskärnan väger traditionella färgtyper, flerfärgade fasader och fönster som kittas om tungt, och en eventuell bygglovsansökan behöver räknas in i tidplanen. I Märsta och Rosersberg är det oftare panelens skick och husets storlek som styr. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi måla om vårt hus vid Stora gatan i samma kulör utan bygglov?",
     "Ommålning i samma kulör räknas enligt Boverket normalt som underhåll. Ska kulören eller färgtypen ändras inom riksintresset krävs bygglov enligt bevarandeplanen."),
    ("Vilken färg rekommenderar kommunen på ett 1950-talshus i Sigtuna stad?",
     "Planen rekommenderar traditionella färgtyper även för hus från 1950-talet, till exempel slamfärg på ohyvlad panel och oljefärg på fönster."),
    ("Vad menas med en trefärgad fasad i Sigtuna?",
     "Att fasad, listverk och detaljer har olika kulörer, ofta med kulörta fönsterbågar. Planen beskriver det som vanligt sedan slutet av 1990-talet, när äldre husens kraftigare kulörer började återskapas."),
    ("Kan vi använda modern färg om vi grundar med linolja?",
     "Planen rekommenderar just det om man väljer en modern färgtyp, men påpekar att moderna färger åldras annorlunda och får en annan glans och struktur."),
    ("Gäller bevarandeplanen även vårt radhus i Märsta?",
     "Nej, planen gäller Sigtuna stad. I Märsta avgör detaljplanen och husets värde om ny kulör kräver lov, och kommunen svarar om du är osäker."),
  ],
  "sources": [
    ("Sigtuna kommun – Bevarande- och förnyelseplan för Sigtuna stad, antagen 2019 (pdf)",
     "https://www.sigtuna.se/download/18.6ed4dd301706254f993282/1582201854957/Bevarande-%20och%20f%C3%B6rnyelseplan%20f%C3%B6r%20Sigtuna%20stad,%20antagen%202019.pdf"),
    ("Sigtuna kommun – Bygga i kulturmiljö",
     "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html"),
    _BOV, _SKV, _SKV2,
  ],
  "cta": ("Ska huset i Sigtuna målas om?", "Boka ett gratis platsbesök så går vi igenom färgtyp, kulör och lovfrågan på plats."),
  "img": [
    ("Panelade trähus i olika kulörer längs en gata i Sigtunas stadskärna",
     "row of small 19th century Swedish wooden town houses with painted panel facades in pale yellow, grey-pink and sage green, contrasting window frames, white and green trims, red clay tile roofs, narrow cobbled street sloping down toward a lake, historic small town Sigtuna by lake Mälaren, summer, empty street, no people"),
    ("Grönmålad fönsterbåge och fönsterbleck mot gulmålad panel",
     "close-up of a well maintained old wooden casement window on a Swedish wooden town house, sash freshly painted glossy dark green, neat new linseed putty along small panes of slightly wavy old glass, the small iron hinge painted in the same dark green as the sash, smooth ochre yellow painted wooden panel around the window, clean, daylight, no people"),
  ],
  "related": [],
},

}
