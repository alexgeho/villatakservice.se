# -*- coding: utf-8 -*-
"""Målare – ortsidor del A: Bromma, Solna, Sollentuna, Vallentuna (tjänster v1, 2026-10-25).
Fakta endast från källorna i respektive 'sources'. Lokala uppgifter återanvända och omformulerade
från tools/takreno_orter.py (TRP) där källan redan var verifierad. Schema: se tools/tj_check.py."""

_BOV = ("Boverket – Bygglov för fasadändring (PBL kunskapsbanken)",
        "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_RAA = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf)",
        "https://www.raa.se/publicerat/9789172095830.pdf")
_SKV = ("Skatteverket – Så fungerar rotavdraget",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV2 = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
         "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV3 = ("Skatteverket – Rotavdrag vid målning av fönster i bostadsrätt",
         "https://www.skatteverket.se/privat/etjansterochblanketter/svarpavanligafragor/rotochrutarbete/privatrotochrutarbetefaq/ettforetagskamalaomfonstreniminbostadsrattkanjagfarotavdragforalltmaleriarbete.5.71004e4c133e23bf6db8000116517.html")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"malare-bromma.html": {
  "kind": "district", "service": "malare", "ort": "Bromma", "svc_label": "Målare",
  "title": "Målare i Bromma – fasader i trädgårdsstäderna",
  "description": "Målare i Bromma: lockpanel, slätputs och spån i trädgårdsstäder och småstugeområden. Färgtyp, kulör och lov i riksintressena. Gratis platsbesök.",
  "h1": "Målare i Bromma",
  "lead": "Ska villan i Bromma målas om börjar arbetet med två frågor: vad sitter det för färg på fasaden i dag, och ligger huset i ett riksintresse eller är det blå- eller grönmärkt på Stadsmuseets karta? Svaren styr både färgval och om du behöver söka lov. Geal Entreprenad AB har sin bas i Bromma och tar målningsuppdrag ute och inne, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Fasad och interiör i Brommas villastäder.",
  "sections": [
    {"id": "fasader", "anchor": "Fasaderna i Bromma",
     "h2": "Lockpanel, slätputs och spån – Brommas tre fasadfamiljer",
     "paras": [
       "Den vanligaste ytan en målare möter i Bromma är stående träpanel med smal lockläkt. Så kläddes de flesta hus i 1920-talets trädgårdsstäder – Ålsten, Smedslätten, Nockeby, Höglandet och Ulvsunda – och samma panel användes på småstugorna i Olovslund och Norra Ängby. Stadens vägledning för småhusområden beskriver färgskalan i trädgårdsstäderna som dämpade, ljusa nyanser av grönt, gult och grått. I småstugeområdena var kulörerna från början reglerade till ett fåtal ljusa toner, och den som ville ha traditionell rödfärg fick ansöka särskilt.",
       "I Äppelviken är det nationalromantiska draget tydligare, med branta takfall och småspröjsade fönster. Fasaderna gjordes ofta av liggande panel eller spån som antingen tjärades eller ströks med röd slamfärg.",
       "Södra Ängby, byggd 1933–39, är något helt annat: kubiska funkisvillor med svagt lutande tak och fasader i brutet vitt eller ljusgrått, antingen slätputsade eller klädda med liggande panel. På en putsad fasad handlar målningen om putsens sammansättning, sprickor och vidhäftning, inte om panel och lockläkt. Ska putsen lagas mer omfattande hör det snarare hemma under " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": {"title": "Ta reda på först", "items": [
       "Panel, spån eller puts?", "Vilken färgtyp sitter på i dag?", "Riksintresse eller blå/grön på kartan?",
       "Skyddsbestämmelser i detaljplanen?", "Hur ser fönster och knutar ut?"]}},
    {"id": "fargtyp", "h2": "Färgtypen väger lika tungt som kulören",
     "paras": [
       "Riksantikvarieämbetets handbok om traditionellt byggnadsmåleri ger ett enkelt råd: håll dig i de flesta fall till samma färgtyp som tidigare. Det gäller särskilt utomhus på ytor som har målats med linoljefärg, slamfärg, trätjära eller kalkfärg. Att stryka moderna produkter över äldre färgtyper beskrivs som en teknisk risk, eftersom nästa underhåll kan bli mycket besvärligt och det inte går att återgå till den gamla behandlingen utan att ta bort all färg.",
       "Boverket gör en liknande distinktion i lovfrågan. Ett byte av kulör betyder en ändring av nyans, ton eller ljushet. Att gå från linoljefärg till plastfärg, eller från slamfärg till silikonhartsfärg, räknas inte som kulörbyte – men det kan bedömas som en påverkan på husets yttre karaktärsdrag. I en kulturmiljö som Brommas trädgårdsstäder är det därför klokt att låta färgtypen ingå i samma bedömning som kulören.",
       "För en Brommavilla med äldre panel betyder det att färgprov och skrapprov på flera ställen kommer före offerten. Där huset redan har fått en modern täckfärg är det oftast den som får fortsätta, så länge underlaget är friskt.",
     ],
     "aside": None},
    {"id": "lov-bromma", "h2": "Riksintressen och Stadsmuseets karta avgör lovet",
     "paras": [
       "Sedan 1 december 2025 krävs normalt inget bygglov för att byta kulör på ett en- eller tvåbostadshus, enligt Boverket. Undantagen är byggnader och områden med skyddsbestämmelser i detaljplan eller områdesbestämmelser, särskilt värdefulla byggnader och miljöer enligt plan- och bygglagen samt planer med utökad lovplikt. Att måla om i samma kulör räknas i regel som underhåll.",
       "Stockholms stad skriver att du behöver söka lov för annars lovfria åtgärder om fastigheten ligger inom ett riksintresse för kulturmiljövården. I Bromma gäller det Norra och Södra Ängby, Olovslund och Ålstensgatan med sina 94 funkisradhus från 1932–33. Samma sak gäller om huset är markerat med blått eller grönt på Stadsmuseets klassificeringskarta. Är det gult eller grått och uppfyller inget av de andra kriterierna behövs normalt inget lov. Staden påpekar att kartan bara ger en första indikation och att alla hus ännu inte är inventerade.",
       "För Södra Ängby finns dessutom en detaljplan från 1995 med skyddsbestämmelser för husens utformning. Söker du lov ska kulörerna anges i NCS, och även lovfria ändringar ska uppfylla plan- och bygglagens varsamhetskrav.",
     ],
     "aside": {"title": "Riksintressen i Bromma", "items": [
       "Norra och Södra Ängby (AB 119)", "Olovslund (AB 118)", "Ålstensgatan (AB 117)"]}},
    {"id": "inne", "h2": "Invändigt i småstugor och trädgårdsstadsvillor",
     "paras": [
       "Inomhus är målning sällan en lovfråga, men husens historia syns även här. Småstugorna byggdes billigt och standardiserat efter katalogritningar, och i slutet av 1970-talet samlade Stadsbyggnadskontoret alla typritningar från 1927 till 1957 i en sammanställning för den som ville bygga om sin stuga. Ritningen visar hur huset var tänkt från början, vilket underlättar när man ska avgöra vilka väggar och snickerier som är original.",
       "Där vinden har inretts i efterhand möts ofta nyare skivor, äldre panel och snedtak, och varje yta kräver sin egen förbehandling. I trädgårdsstadsvillorna från 1920-talet kan dörrar, foder och lister bära många lager färg som behöver slipas eller rengöras innan nytt stryks. Ska rummen samtidigt få nya golv eller ändrad planlösning kan målningen ingå i en större " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
    {"id": "lage", "h2": "Tallar och Mälarnära skugga",
     "paras": [
       "Vegetationen i trädgårdsstäderna dominerades från början av tall och ädellövträd, och i Södra Ängby, som gränsar mot Mälaren, har den ursprungliga hällmarkstallskogen till stor del bevarats. Fasader som ligger i skugga större delen av dagen torkar långsamt och får lättare påväxt, så tvätt och torktid behöver planeras in innan första strykningen.",
       "Väljer du linoljefärg anger Riksantikvarieämbetet maj till augusti som bästa period, med en fukthalt i träet på högst omkring 15 procent. Direkt solsken bör undvikas eftersom ytan kan torka för snabbt och bilda blåsor – bättre är att följa solen och stryka de sidor som redan har haft sol.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Bromma till",
  "steps": [
    ("Platsbesök och prover", "Vi tittar på panel, puts, fönster och knutar och gör skrapprov för att se vilken färgtyp som sitter på."),
    ("Karta och plan", "Vi går igenom Stadsmuseets klassificering, riksintressen och detaljplan så att du vet om kulörbytet kräver lov."),
    ("Skriftligt kostnadsförslag", "Underarbete, färgtyp, antal strykningar och ställning står med, så att förslaget går att jämföra."),
    ("Tvätt, skrapning och lagning", "Löst sittande färg tas bort, påväxt tvättas av och skadad panel eller puts lagas."),
    ("Grundning och strykningar", "Färgen läggs i den ordning och med de torktider som färgtypen kräver."),
    ("Genomgång", "Vi går igenom fasaden tillsammans och rättar det som behöver bättras."),
  ],
  "rot_h2": "ROT-avdrag för målning i Bromma",
  "rot": [
    "För en villa ger Skatteverket rotavdrag för att måla fasader, fönster, golv, väggar och tak samt för tapetsering. Att måla staket eller murar ger inget avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och ROT och RUT får tillsammans vara högst 75 000 kr. Färg och annat material ingår inte.",
    "Bor du i bostadsrätt i Bromma gäller avdraget bara arbete inne i lägenheten. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden?",
  "price": [
    "Mest styrs priset av underarbetet: hur mycket gammal färg som måste bort, hur mycket panel eller puts som behöver lagas och hur många fönster med spröjs som ska kittas och målas. Därtill kommer husets höjd och ställningsbehov, färgtypen och antalet strykningar. Vi gör ett gratis platsbesök och lämnar ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Mitt hus i Bromma är gulmarkerat hos Stadsmuseet – behöver jag lov för ny kulör?",
     "Normalt inte, om huset inte heller ligger i ett riksintresse, i ett område som pekats ut som särskilt värdefullt eller har skyddsbestämmelser i detaljplanen. Kartan är bara en första indikation, så kontrollera planen också."),
    ("Kan jag byta från linoljefärg till plastfärg på en trädgårdsstadsvilla?",
     "Det är inget kulörbyte enligt Boverket, men det kan räknas som en påverkan på husets karaktär, och i ett riksintresse kan det bli en lovfråga. Tekniskt avråder Riksantikvarieämbetet från att stryka moderna färger över äldre färgtyper."),
    ("Får jag måla min funkisvilla i Södra Ängby i en annan nyans av vitt?",
     "Södra Ängby är riksintresse och har en detaljplan med skyddsbestämmelser, så en ändrad kulör kräver lov. Samma kulör som tidigare räknas i regel som underhåll."),
    ("Finns det originalritningar till småstugorna i Norra Ängby och Olovslund?",
     "Stadsbyggnadskontoret samlade i slutet av 1970-talet typritningarna från 1927–1957 i en sammanställning. Fråga staden efter ritningen till din hustyp innan du bestämmer färgsättning."),
    ("När på året kan en fasad i Bromma strykas med linoljefärg?",
     "Riksantikvarieämbetet anger maj till augusti, när det är varmt och torrt. I skuggiga lägen under tallarna behöver träet hinna torka efter tvätt innan målningen börjar."),
  ],
  "sources": [
    ("Stockholms stad – Varsam utveckling av småhus- och villaområden",
     "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf"),
    ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov)",
     "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/"),
    ("Stockholms stad – Fasadändring",
     "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/"),
    ("Stockholms stad – Översiktsplan, Riksintressen enligt miljöbalken",
     "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf"),
    ("Stockholmskällan / Stadsmuseet – Ängbyplan (Stockholms spår)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000106.pdf"),
    ("Wikipedia – Södra Ängby", "https://sv.wikipedia.org/wiki/S%C3%B6dra_%C3%84ngby"),
    _RAA, _BOV, _SKV, _SKV2,
  ],
  "cta": ("Ska villan i Bromma målas?", "Boka ett gratis platsbesök så går vi igenom fasad, färgtyp och lovfrågor på plats."),
  "img": [
    ("Nymålad ljusgul trävilla med stående lockpanel och vita fönster i en trädgårdsstad i Bromma",
     "freshly painted pale yellow 1920s wooden villa with vertical board-and-batten siding, white window frames, red clay tile roof, closed front door with small porch, mature pine trees, Bromma garden city Stockholm, summer"),
    ("Vitputsad funkisvilla med svagt lutande tak bland tallar i Södra Ängby",
     "white smooth-rendered 1930s functionalist villa with low-pitched roof and irregular windows among tall pine trees, Södra Ängby Stockholm, painter's scaffolding at one gable, no people"),
  ],
},

# ------------------------------------------------------------------ SOLNA
"malare-solna.html": {
  "kind": "district", "service": "malare", "ort": "Solna", "svc_label": "Målare",
  "title": "Målare i Solna – snickerier, kulör och bygglov",
  "description": "Målare i Solna: villor och radhus i Råsunda, Stocksundstorp och Bergshamra, lovregler för kulör och rotavdrag i bostadsrätt. Gratis platsbesök.",
  "h1": "Målare i Solna",
  "lead": "Stora delar av Solna räknas av staden som kulturhistoriskt värdefulla, och där gäller inte de lovfria reglerna för kulörbyte. Bor du i bostadsrätt är frågan i stället vad du själv ansvarar för och vad som ger rotavdrag. Geal Entreprenad AB tar målningsuppdrag i hela Solna, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villor, radhus och lägenheter i Solna.",
  "sections": [
    {"id": "villor", "anchor": "Villorna i Solna",
     "h2": "Var småhusen finns i en stad av flerbostadshus",
     "paras": [
       "Solna domineras av flerbostadshus, och de egna husen ligger samlade i ett fåtal miljöer. Råsunda planerades kring 1907 med flerfamiljshus i mitten och villor runt om. Villaområdena byggdes ut på 1920-talet, och många av husen byggdes av spårvägare som arbetade vid den stora spårvägsverkstaden. Här möter målaren trävillor med panel, fönster med spröjs och snickerier som har strukits om många gånger.",
       "I Stocksundstorp, på Bergshamras östra udde, finns villor kvar från 1800-talet. Tre större sommarvillor uppfördes vid Stocksundsbron omkring 1892, och Villa Borganäs och Villa Alnäs finns kvar med sitt rika lövsågeri. Udden styckades 1920 i 38 tomter som bebyggdes efter hand, så många villor där är från 1940- till 1970-talen och har sin tids enklare fasader.",
       "Därtill finns Råsta egnahem, Bergshamra by och radhusen vid Solna kyrkby. Färgfrågorna skiljer sig mycket mellan en sommarvilla från 1890-talet och ett egnahem från 1920-talet.",
     ],
     "aside": {"title": "Utpekade småhusmiljöer", "items": [
       "Råsunda villastad", "Villorna i norra Råsunda", "Råsta egnahem", "Alnäs och Stocksundstorp",
       "Solna kyrkby med radhusen", "Bergshamra by"]}},
    {"id": "lov-solna", "h2": "Ny kulör i Solna blir oftast en lovfråga",
     "paras": [
       "Enligt Boverket krävs sedan 1 december 2025 normalt inget bygglov för att byta kulör på ett en- eller tvåbostadshus. Undantag gäller där detaljplan eller områdesbestämmelser har skyddsbestämmelser, för särskilt värdefulla byggnader och områden och där planen har utökad lovplikt. Solna stad räknar upp var de lovbefriade åtgärderna inte kan användas: i de kulturmiljöer som är markerade i Solnakartan, i riksintressena Karlberg, Solna kyrkby med radhusbebyggelsen, Ulriksdal och Hagaparken, i nationalstadsparken och i de sammanhängande kulturmiljöer som översiktsplanen pekar ut, bland annat Råsunda villastad, norra Råsunda, Råsta egnahem samt Alnäs och Stocksundstorp.",
       "Söker du lov för en ny färgsättning vill staden ha en material- och kulörbeskrivning, fasadritning, foton på huset i dag och gärna illustrationer i färg. För en kulturhistoriskt värdefull byggnad kan det krävas en antikvarisk förundersökning eller ett utlåtande från en sakkunnig i kulturvärden (KUL). Stryker du om i samma kulör som tidigare räknas det enligt Boverket normalt som underhåll.",
     ],
     "aside": {"title": "Kolla i Solnakartan", "items": [
       "Lagret kulturhistoriskt värdefull miljö", "Lagret byggnad – kulturhistorisk klassning",
       "Utökad lovplikt", "Detaljplanen för fastigheten"]}},
    {"id": "snickerier", "h2": "Lövsågeri, vindskivor och fönster tar mest tid",
     "paras": [
       "På en villa med rika snickerier är det detaljerna som avgör både tidsåtgång och resultat. Lövsågade gavelspetsar, konsoler och vindskivor har många kanter där färgen släpper först, och de sitter ofta högt. I Solnas värdefulla miljöer är det just sådana detaljer som ska behållas, så skadade delar lagas eller kopieras av en " + _L.format("snickare.html", "snickare") + " innan de målas, i stället för att tas bort.",
       "Riksantikvarieämbetet beskriver hur linoljefärg ska strykas tunt i flera lager – vid nymålning grundning, mellanstrykning och slutstrykning – och att färgen kan strykas över efter ungefär ett till tre dygn om vädret är varmt och torrt. Myndigheten varnar också för att ny färg över mycket fet oljefärg lätt ger blåsor, främst på fasader mot söder, oavsett vilken färgtyp man använder.",
       "Fönstren är ett eget arbete: kitt som har släppt, rötskador i nedre karmdelar och bågar som kärvar. Är fönstren för långt gångna att renovera finns mer under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
    {"id": "brf", "h2": "Bostadsrätt i Solna – vad du själv beställer",
     "paras": [
       "De flesta i Solna bor i lägenhet. Enligt bostadsrättslagen ska bostadsrättshavaren på egen bekostnad hålla lägenheten i gott skick, om inte stadgarna säger något annat. Att måla väggar och tak eller tapetsera inne i lägenheten är därför normalt ditt eget beslut. Har lägenheten särskilda kulturhistoriska värden krävs enligt lagen styrelsens tillstånd för ändringar som påverkar de värdena.",
       "Fasader, trapphus och balkonger är föreningens sak. Det märks också i rotavdraget, som bara gäller arbete inne i lägenheten.",
     ],
     "aside": {"title": "Inne i lägenheten", "items": [
       "Väggar, tak och element", "Tapetsering", "Innerdörrar och köksluckor", "Fönstrens insida"]}},
    {"id": "lage", "h2": "Brunnsviken, Stocksundet och nationalstadsparken",
     "paras": [
       "Stocksundstorp vid Stocksundet ligger inom Kungliga nationalstadsparken, och husen står nära vattnet bland stora träd. Fasader i ett sådant läge får både blåst och skugga, torkar långsamt efter regn och får lätt påväxt. Tvätt, ordentlig torktid och en färgtyp som passar underlaget betyder mer här än på en solig villatomt.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Solna till",
  "steps": [
    ("Platsbesök", "Vi går igenom fasad, snickerier och fönster, eller rummen i lägenheten, och gör skrapprov där det behövs."),
    ("Lov och föreningsregler", "För villan kontrollerar vi Solnakartan och detaljplanen, för bostadsrätten vad stadgarna säger."),
    ("Skriftligt kostnadsförslag", "Underarbete, färgtyp och antal strykningar specificeras, och arbete inne och ute redovisas var för sig."),
    ("Förarbete", "Tvätt, skrapning, lagning av trä och kittning av fönster, eller spackling och slipning inomhus."),
    ("Målning", "Strykningarna görs i den ordning och med de torktider som färgtypen kräver."),
    ("Avslut", "Gemensam genomgång, bättring där det behövs och städning."),
  ],
  "rot_h2": "Rotavdrag för målning i Solna",
  "rot": [
    "I villa och radhus ger både utvändig och invändig målning rotavdrag, men inte målning av staket eller murar. I bostadsrätt gäller avdraget bara arbete inne i lägenheten: väggar, tak, element, dörrar, köksluckor, tapetsering och insidan av fönster och ytterdörr. Skatteverket skriver att arbete som utförs mellan fönstrets in- och utsida inte ger avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och tillsammans med RUT högst 75 000 kr. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset?",
  "price": [
    "På en villa styrs kostnaden av mängden snickerier och fönster, hur mycket gammal färg som behöver bort och om det krävs ställning. I en lägenhet är det väggarnas skick, takhöjd och mängden spackling som avgör. Vi gör ett gratis platsbesök och lämnar ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag måla om min villa i Råsunda i en ny kulör utan bygglov?",
     "Troligen inte. Råsunda villastad och villorna i norra Råsunda hör till de miljöer där Solna stad skriver att de lovbefriade åtgärderna inte kan användas. Samma kulör som tidigare räknas normalt som underhåll."),
    ("Ger målning av fönstren i min bostadsrätt i Solna rotavdrag?",
     "Bara för arbetet på insidan. Enligt Skatteverket ger arbete mellan in- och utsidan inget avdrag, och målning av fönstrens utsida ger inte heller något."),
    ("Behöver jag fråga styrelsen innan jag målar om i lägenheten?",
     "Normalt inte för vanlig målning, eftersom du ansvarar för lägenhetens skick. Läs stadgarna, och har lägenheten särskilda kulturhistoriska värden krävs tillstånd för ändringar som påverkar dem."),
    ("Kan lövsågeriet på en sommarvilla i Stocksundstorp sparas när huset målas om?",
     "Oftast går det. Löst sittande färg tas bort, skadade bitar lagas eller kopieras och detaljerna målas för hand. Det ligger också i linje med att de värdefulla miljöerna ska behålla sin karaktär."),
  ],
  "sources": [
    ("Solna stad – Bygglovsfria åtgärder", "https://www.solna.se/bygga-bo--miljo/bygga/bygglov/bygglovsfria-atgarder"),
    ("Solna stad – Fasadändring", "https://www.solna.se/bygga-bo--miljo/bygga/vanliga-byggatgarder/fasadandring"),
    ("Solna stad – Kulturmiljöer i Solna", "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna"),
    ("Stockholmskällan / Stadsmuseet – Näckrosen (Stockholms spår)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000066.pdf"),
    ("Wikipedia – Stocksundstorp", "https://sv.wikipedia.org/wiki/Stocksundstorp"),
    ("Riksdagen – Bostadsrättslag (1991:614)",
     "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/"),
    _RAA, _BOV, _SKV, _SKV2, _SKV3,
  ],
  "cta": ("Villa eller lägenhet i Solna som ska målas?", "Boka ett gratis platsbesök så går vi igenom arbetet och lovfrågorna."),
  "img": [
    ("Ljusgrön trävilla med lövsågade gavelspetsar och vita snickerier vid vattnet i Solna",
     "freshly painted pale green 1890s Swedish summer villa with ornate white fretwork gables and verandas, large old trees, view of a narrow strait, Stocksundet Solna, summer, no people"),
    ("Ljust målat vardagsrum med spröjsade fönster i en äldre lägenhet i Råsunda",
     "freshly painted light grey living room in a 1910s apartment with tall mullioned windows, white window frames, herringbone parquet, protective paper on floor edges, painter's ladder, Råsunda Solna, no people"),
  ],
},

# ------------------------------------------------------------------ SOLLENTUNA
"malare-sollentuna.html": {
  "kind": "district", "service": "malare", "ort": "Sollentuna", "svc_label": "Målare",
  "title": "Målare i Sollentuna – villastad och radhuslängor",
  "description": "Målare i Sollentuna: sekelskiftesvillor, egnahem och radhuslängor från 60–80-talet. Kulörval i grupp, byggherrens ansvar och rotavdrag. Gratis platsbesök.",
  "h1": "Målare i Sollentuna",
  "lead": "I Sollentuna handlar målning oftast om en av två hustyper: en äldre villa med kupor och snickerier i någon av villastäderna, eller ett radhus i en länga där grannarna har samma fasad. Båda kräver att kulören stäms av innan arbetet börjar – den ena mot kulturmiljön, den andra mot helheten i gruppen. Geal Entreprenad AB tar målningsuppdrag i hela kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villor och radhus i Sollentuna.",
  "sections": [
    {"id": "hustyper", "anchor": "Hustyperna",
     "h2": "Fyra slags hus som målas på olika sätt",
     "paras": [
       "<strong>Villor från seklets början.</strong> Med järnvägen från 1866 och stationerna i Tureberg och Norrviken kom de första villastäderna. AB Norrvikens villastad köpte Kista gårds mark 1906 och styckade den i egnahemstomter, och 1910 delades marken mellan Turebergs station och Edsviken upp i 61 villatomter. På villor från den tiden tar knutbrädor, foder och spröjsade fönster ofta lika mycket tid som själva panelen.",
       "<strong>Egnahem från 1930- och 40-talet.</strong> Under 1930- och 40-talet tillkom egnahemsvillor i södra Norrviken. På dem är det ofta panel som har strukits om i flera omgångar med olika färger, och skrapprov visar vilken färgtyp som ligger överst.",
       "<strong>Radhus från 1960-talet till början av 80-talet.</strong> Större radhusområden byggdes i sydvästra och norra Norrviken. Längorna har samma ålder och oftast samma panel, fönster och kulör. Det gör att flera grannar får samma behov ungefär samtidigt.",
       "<strong>Nyare radhus och villor.</strong> I Edsberg är Kvarnskogen i huvudsak ett radhusområde, och Edsängen blandar radhus och villor mot Täby. På yngre fasader är det ofta skivmaterial, fabriksgrundad panel och moderna täckfärger som gäller.",
     ],
     "aside": {"title": "Var husen finns", "items": [
       "Norrvikens villastad och Tureberg", "Landsnora längs Edsviken", "Södra Norrviken: egnahem",
       "Norrviken: radhus 1960–80", "Kvarnskogen och Edsängen"]}},
    {"id": "radhus", "h2": "Radhuslängan är en enda fasad",
     "paras": [
       "Kommunens översiktsplan säger att radhus och sammanhållna husgrupper får förändras, men att varje förändring ska bidra positivt till helheten. På en länga där alla hus har samma kulör syns ett avvikande hus på långt håll. Det är därför klokt att prata med grannarna, och med samfälligheten om det finns en, innan någon beställer en ny färgsättning.",
       "Kommunen skriver också att reglerna för fasadändring utan lov ser olika ut för radhus, kedjehus och andra sammanbyggda småhus, beroende på hur bebyggelsen är utformad. Kontaktcenter kan vägleda om vad som gäller för just din länga.",
       "Praktiskt finns det fördelar med att flera grannar målar samtidigt. Ställning, tvätt och torktider kan planeras gemensamt, och kulören blir densamma över hela längan i stället för att nyanserna glider isär med åren. Varje hushåll gör sitt eget rotavdrag på sin del av arbetet.",
     ],
     "aside": None},
    {"id": "ansvar", "h2": "Lovfritt betyder inte fritt fram",
     "paras": [
       "Sedan 1 december 2025 krävs normalt inget bygglov för att byta kulör på ett en- eller tvåbostadshus, enligt Boverket. Sollentuna kommun skriver att lov ändå krävs om fastigheten ligger i ett kulturhistoriskt värdefullt område eller om byggnaden i sig är kulturhistoriskt värdefull. Kommunen betonar dessutom att du som byggherre ansvarar för att även en lovfri ändring är anpassad till husets och områdets karaktär och följer detaljplanen, och att vissa detaljplaner har bestämmelser om fasadmaterial.",
       "Osäker på om huset ligger i ett värdefullt område? Kommunen gör en bedömning om du skickar in foton på huset från alla väderstreck och beskriver vad du vill göra. Du kan också söka ett frivilligt bygglov och få ett beslut på att ändringen uppfyller kraven. Äldre ritningar på huset finns i kommunens bygglovsarkiv utan kostnad, och de kan visa hur fasaden var tänkt från början.",
     ],
     "aside": {"title": "Innan du väljer kulör", "items": [
       "Läs detaljplanen för fastigheten", "Skicka foton till kommunen vid osäkerhet",
       "Hämta äldre ritningar ur arkivet", "Stäm av med grannarna i längan"]}},
    {"id": "kulturmiljoplan", "h2": "En ny kulturmiljöplan ska antas våren 2027",
     "paras": [
       "Den kulturmiljöplan Sollentuna använder i dag är från 1993, med tillägg från 2002. Kommunen skriver själv att den inte uppfyller dagens krav och att det är otydligt vilka byggnader och miljöer som är särskilt värdefulla. Därför tas en ny plan fram efter ändringarna i plan- och bygglagen från december 2025. En inventering gjordes under hösten 2025, och målet är att planen ska antas våren 2027.",
       "För den som ska måla en äldre villa betyder det att bedömningen kan ändras. Översiktsplanen hänvisar redan nu till Norrvikens villastad, Väderholmen och Skansen som områden där karaktären ska behållas. Ligger ditt hus där är det säkrast att utgå från husets ursprungliga färgsättning eller att fråga kommunen först.",
     ],
     "aside": None},
    {"id": "lage", "h2": "Lummiga tomter vid Edsviken och Norrviken",
     "paras": [
       "Översiktsplanen lyfter den gröna lummigheten i villastaden som något som ska värnas. Det betyder uppvuxna träd nära husen och fasader som står i skugga stora delar av dagen, särskilt nära Edsviken och sjön Norrviken. Där behöver påväxt tvättas bort och panelen få torka ordentligt innan den målas, och det kan vara läge att se över " + _L.format("takmalning.html", "takmålning") + " eller rännor i samma veva som ställningen ändå står uppe.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går målningen till i Sollentuna",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, snickerier och fönster och gör skrapprov för att se vilken färg som sitter på."),
    ("Kulör och regler", "Vi går igenom detaljplan och kulturmiljö, och på radhus hur kulören förhåller sig till resten av längan."),
    ("Skriftligt kostnadsförslag", "Underarbete, färgtyp, antal strykningar och ställning står med – för flera grannar samordnat om ni vill."),
    ("Förarbete", "Tvätt, skrapning, lagning av skadat trä och kittning av fönster."),
    ("Målning", "Grundning och strykningar med de torktider färgen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "Rotavdrag för målning i Sollentuna",
  "rot": [
    "Skatteverket räknar målning av fasader, fönster, väggar, tak och golv samt tapetsering som rotarbete i småhus, men inte målning av staket eller murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och ROT och RUT får sammanlagt vara högst 75 000 kr. Färgen räknas som material och ger inget avdrag.",
    "I ett radhus gör varje ägare avdrag för arbetet på sitt eget hus. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad avgör priset?",
  "price": [
    "På en sekelskiftesvilla är det mängden snickerier, kupor och spröjsade fönster och husets höjd som väger tyngst. På ett radhus styrs priset mer av panelens skick och hur mycket som behöver skrapas. Om flera grannar målar samtidigt kan ställning och etablering delas. Vi gör ett gratis platsbesök och lämnar ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag måla mitt radhus i Norrviken i en annan kulör än grannarnas?",
     "Det beror på hur längan är utformad och vad detaljplanen säger. Kommunen vill att förändringar i husgrupper bidrar till helheten, så stäm av med kontaktcenter och grannarna först."),
    ("Hur vet jag om min villa i Sollentuna räknas som kulturhistoriskt värdefull?",
     "Skicka foton från alla väderstreck till kommunen via sidan om fasadändring, så gör de en bedömning. Den nya kulturmiljöplanen som ska antas våren 2027 kan ändra vilka hus som pekas ut."),
    ("Är det värt att söka frivilligt bygglov för en ny fasadkulör?",
     "Kommunen erbjuder det för den som vill ha ett beslut på att ändringen uppfyller kraven. Det tar längre tid, men kan vara rimligt på en äldre villa i Norrvikens villastad."),
    ("Kan flera grannar i en radhuslänga i Sollentuna beställa målningen tillsammans?",
     "Ja. Arbetet kan samordnas så att ställning och torktider planeras gemensamt, medan varje ägare får sin egen faktura och sitt eget rotavdrag."),
  ],
  "sources": [
    ("Sollentuna kommun – Fasadändring för en- eller tvåbostadshus",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/mala-om-en--och-tvabostadshus/"),
    ("Sollentuna kommun – Översiktsplan och ny kulturmiljöplan",
     "https://www.sollentuna.se/bygga-bo--miljo/stadsutveckling/oversiktsplan/"),
    ("Sollentuna kommun – Översiktsplan för Sollentuna med sikte på 2040",
     "https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/oversiktsplan/oversiktsplan-for-sollentuna-med-sikte-pa-2040.pdf"),
    ("Sollentuna kommun – Kulturhistoriska byggnader och områden",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/kulturmiljoer/"),
    ("Wikipedia – Norrviken", "https://sv.wikipedia.org/wiki/Norrviken"),
    ("Wikipedia – Tureberg", "https://sv.wikipedia.org/wiki/Tureberg"),
    ("Wikipedia – Edsberg, Sollentuna kommun", "https://sv.wikipedia.org/wiki/Edsberg,_Sollentuna_kommun"),
    _BOV, _SKV, _SKV2,
  ],
  "cta": ("Villa eller radhus i Sollentuna som ska målas?", "Boka ett gratis platsbesök – gärna tillsammans med grannarna i längan."),
  "img": [
    ("Radhuslänga i ljusgrå träpanel med vita fönster och lummiga trädgårdar i Sollentuna",
     "row of 1970s Swedish terraced houses with freshly painted light grey wooden panelling and white window frames, small front gardens with birch trees, Sollentuna Stockholm, early summer, no people"),
    ("Äldre villa med frontespis, spröjsade fönster och ny vit målning på snickerierna i Norrviken",
     "early 1900s Swedish wooden villa with a front gable dormer, mullioned windows, freshly painted white trim on yellow panelling, scaffolding at one side, large leafy trees, Norrviken Sollentuna, no people"),
  ],
},

# ------------------------------------------------------------------ VALLENTUNA
"malare-vallentuna.html": {
  "kind": "district", "service": "malare", "ort": "Vallentuna", "svc_label": "Målare",
  "title": "Målare i Vallentuna – gårdar, slamfärg och villor",
  "description": "Målare i Vallentuna: rödfärg på gårdar och uthus, permanentade fritidshus och villor från utbyggnadsåren. Lov i riksintressena. Gratis platsbesök.",
  "h1": "Målare i Vallentuna",
  "lead": "I Vallentuna kan samma målare ena veckan stryka rödfärg på en gård i odlingslandskapet och nästa vecka måla om ett radhus i Ormsta. Ommålning av ett en- eller tvåbostadshus kräver normalt inget lov här – utom i kommunens kulturhistoriskt särskilt värdefulla miljöer. Geal Entreprenad AB tar målningsuppdrag i hela kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Gårdar, fritidshus och villor i Vallentuna.",
  "sections": [
    {"id": "husen", "anchor": "Husen i Vallentuna",
     "h2": "Tätort, stationssamhällen och landsbygd",
     "paras": [
       "Tätorten fick sin station när järnvägen mellan Stockholm och Rimbo öppnade 1885, men de flesta villorna är betydligt yngre. År 1960 bodde 3 516 personer i tätorten, 1970 var de 8 823 och 1980 hela 18 435. Befolkningen femdubblades alltså på tjugo år, och många villor och radhus i tätorten är från just den perioden. Det betyder ofta liknande panel, liknande fönster och ungefär samma underhållsbehov.",
       "Lindholmen längre norrut på Roslagsbanan har vuxit fram huvudsakligen sedan 1970-talet, med villor och gruppbyggda småhus. I Karby och Brottby vid E18 ligger den äldre bebyggelsen i små grupper på höjderna.",
       "Utanför tätorterna finns gårdar med bostadshus och ekonomibyggnader, och fritidshusområden som enligt översiktsplanen i de flesta fall har omvandlats till permanentboende sedan 1990-talet. Garns-Ekskogen har omkring 500 bebyggda fastigheter, medan Lövsättra stugby ska behålla sin fritidsprägel.",
     ],
     "aside": {"title": "Vad som målas här", "items": [
       "Villor och radhus från 1960–80-talet", "Permanentade fritidshus", "Bostadshus på gårdar",
       "Lador, uthus och garage", "Fönster, knutar och vindskivor"]}},
    {"id": "slamfarg", "h2": "Rödfärg på gården och uthusen",
     "paras": [
       "Riksantikvarieämbetet beskriver hur rödfärgen under 1800-talet blev landsbygdens husfärg och att röd slamfärg fortfarande räknas till de bästa utomhusfärgerna för trähus. Färgen består av mjölklister, vatten, järnvitriol och pigment, ibland med en liten tillsats linolja. Den är matt, släpper igenom fukt och fäster bra på ohyvlat virke men sämre på hyvlat.",
       "Slamfärg beskrivs som den i särklass mest underhållsvänliga färgtypen: det räcker att borsta bort lös färg och stryka på nytt. Men den fungerar bara på sig själv. Enligt myndigheten ska en slamfärgad yta inte målas över med någon annan färgtyp, och har man en gång gått över till exempelvis latex-, alkyd- eller linoljefärg går det inte att återgå till slamfärg ens om den gamla färgen tas bort. Det finns också produkter som påminner om rödfärg men har andra bindemedel, så innehållsförteckningen bör läsas noga.",
       "Kulören kan skilja något mellan olika tillverkare, vilket märks när bara en del av en byggnad målas. På en gård med flera hus är det därför en fördel att stryka allt med samma färg i samma omgång.",
     ],
     "aside": None},
    {"id": "fritidshus", "h2": "Permanentade fritidshus och villor från utbyggnadsåren",
     "paras": [
       "Ett fritidshus som byggts om till helårsbostad har ofta målats i flera omgångar och med olika produkter, och tillbyggnader kan ha fått en annan panel än originalet. Innan något nytt stryks över behöver man veta vad som redan sitter på. Riksantikvarieämbetet påpekar att ny färg över mycket fet oljefärg lätt ger blåsor, särskilt på fasader mot söder. Byggs huset till eller får nya fönster samtidigt kan målningen samordnas med " + _L.format("tillbyggnad.html", "tillbyggnaden") + " så att ställningen bara behöver resas en gång.",
       "Villorna i Ormsta och Bällsta har oftast en modern täckfärg som kan målas över med samma typ, men efter flera decennier kan panelen ha rötskador nertill och vid fönsterbleck. De byts innan målningen börjar. Inomhus är det ofta tak och väggar i ursprungliga rum som ska fräschas upp, i kombination med en " + _L.format("villarenovering.html", "större renovering") + " av kök eller badrum.",
     ],
     "aside": None},
    {"id": "lov-vallentuna", "h2": "Lov och riksintressen i Vallentuna",
     "paras": [
       "Vallentuna kommun skriver att ommålning, nytt tak eller nya fönster på ett en- eller tvåbostadshus inte kräver bygglov, men att ändringar ska göras varsamt och anpassas till byggnadens värden. Lov krävs däremot om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden själv är kulturhistoriskt särskilt värdefull. Det stämmer med Boverkets beskrivning av reglerna från 1 december 2025. Boverket påpekar dessutom att ett byte av färgtyp, till exempel från slamfärg till silikonhartsfärg, inte räknas som kulörbyte men kan bedömas påverka husets yttre karaktärsdrag.",
       "Översiktsplan 2040 räknade upp fem riksintressen för kulturmiljövården. Efter Länsstyrelsens översyn har Kårsta utgått, och kvar finns Skålhamravägen, Markim-Orkesta, Frösunda sockencentrum och Vada-Össeby-Garn längs Långhundraleden, enligt kommunens planeringsstrategi. Kommunens kulturmiljöprogram pekar dessutom ut områden med höga eller mycket höga kulturhistoriska kvaliteter, till exempel delar av Markim, Lingsbergsvägen och Lindholmen.",
       "Krävs lov ska ansökan bland annat innehålla fasadritningar i skala 1:100 och en redovisning av utvändiga material och kulörer med NCS-koder. Äldre ritningar kan beställas från kommunens arkiv om de finns.",
     ],
     "aside": {"title": "Riksintressen för kulturmiljö", "items": [
       "K71 Skålhamravägen", "K74 Markim-Orkesta", "K75 Frösunda sockencentrum", "K77 Vada-Össeby-Garn"]}},
    {"id": "lage", "h2": "Öppna fält och vind",
     "paras": [
       "Gårdarna i Karby och Brottby ligger enligt kommunen i ett småskaligt landskap av skogsklädda kullar och öppen åker- och ängsmark. Ett hus som står fritt i odlingslandskapet är mer utsatt för väder än en villa i tätorten, så det lönar sig att se extra noga på gavlar, vindskivor och fönster mot de öppna fälten. Linoljefärg kräver varmt och torrt väder – Riksantikvarieämbetet anger maj till augusti – medan slamfärg är mer förlåtande men inte bör strykas för tjockt.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Vallentuna till",
  "steps": [
    ("Platsbesök", "Vi tittar på alla byggnader som ska målas och gör skrapprov för att se om det är slamfärg, oljefärg eller modern täckfärg."),
    ("Kulturmiljö", "Ligger fastigheten i ett riksintresse eller ett område med höga kulturhistoriska kvaliteter stämmer vi av med kommunen."),
    ("Skriftligt kostnadsförslag", "Underarbete, färgtyp och antal strykningar per byggnad, så att du kan välja vad som görs först."),
    ("Förarbete", "Borstning eller skrapning, tvätt och byte av rötskadat trä."),
    ("Målning", "Färgen stryks i den ordning och med de torktider som färgtypen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "Rotavdrag för målning i Vallentuna",
  "rot": [
    "På ett småhus räknar Skatteverket målning av fasader, fönster, väggar, tak och golv samt tapetsering som rotarbete. Målning av staket och murar ger inget avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och ROT och RUT får tillsammans vara högst 75 000 kr. Färgen är material och ingår inte.",
    "Ska ekonomibyggnader på en gård målas, fråga om rotavdraget innan arbetet börjar. Geal drar avdraget direkt på fakturan där det gäller.",
  ],
  "price_h2": "Vad styr priset?",
  "price": [
    "Kostnaden beror på hur många byggnader som ingår, hur höga gavlarna är, hur mycket gammal färg som måste bort och hur mycket trä som behöver bytas. På landsbygden spelar även framkomlighet och var ställningen kan stå in. Vi gör ett gratis platsbesök och lämnar ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan en rödfärgad lada i Vallentuna målas om med vanlig täckfärg?",
     "Det går, men Riksantikvarieämbetet avråder. Har slamfärgen en gång täckts med en annan färgtyp går det inte att återgå till slamfärg, och i ett riksintresse kan bytet dessutom påverka byggnadens karaktär."),
    ("Behöver jag lov för att måla om gården i Markim i samma röda kulör?",
     "Samma kulör räknas enligt Boverket normalt som underhåll. Ska kulören eller färgtypen ändras inom riksintresset Markim-Orkesta, stäm av med kommunen först."),
    ("Vad ska anges om jag söker lov för ny fasadkulör i Vallentuna?",
     "Kommunen vill ha fasadritningar i skala 1:100 och en redovisning av utvändiga material och kulörer med NCS-koder, tillsammans med situationsplan och kontrollplan."),
    ("Mitt fritidshus i Garns-Ekskogen har flera lager olika färg – var börjar man?",
     "Med skrapprov på flera ställen för att se vilka färgtyper som ligger på. Därefter avgörs om ytan kan målas över eller om färgen behöver tas bort ner till trä."),
    ("Kan ni måla bostadshus, garage och lada på samma gård i en omgång?",
     "Ja. Det gör det enklare att få samma kulör på alla byggnader och att planera ställning och torktider."),
  ],
  "sources": [
    ("Vallentuna kommun – Fasadändring",
     "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/behover-jag-bygglov/fasadandring"),
    ("Vallentuna kommun – Översiktsplan 2040 (pdf)",
     "https://vallentuna.se/download/18.63572f8619eeecafce08366/1782478377449/2.11.7%20%C3%96versiktsplan%202040.pdf"),
    ("Vallentuna kommun – Fördjupad översiktsplan Norra Vallentuna och Lindholmen (pdf)",
     "https://vallentuna.se/download/18.63572f8619eeecafce08379/1782478384567/2.11.4%20F%C3%B6rdjupad%20%C3%B6versiktsplan%20Norra%20Vallentuna%20och%20Lindholmen.pdf"),
    ("Vallentuna kommun – Fördjupad översiktsplan Karby och Brottby (pdf)",
     "https://vallentuna.se/download/18.63572f8619eeecafce08376/1782478381270/2.11.8%20F%C3%B6rdjupad%20%C3%B6versiktsplan%20Karby%20Brottby.pdf"),
    ("Wikipedia – Vallentuna (tätort)", "https://sv.wikipedia.org/wiki/Vallentuna"),
    _RAA, _BOV, _SKV, _SKV2,
  ],
  "cta": ("Gård, fritidshus eller villa i Vallentuna?", "Boka ett gratis platsbesök så går vi igenom alla byggnader som ska målas."),
  "img": [
    ("Rödfärgat bostadshus med vita knutar och en lada i odlingslandskapet i Vallentuna",
     "freshly painted falu red wooden farmhouse with white corner boards and window frames next to a red barn, open fields and wooded hills, Uppland countryside Vallentuna, summer, no people"),
    ("Nymålad villa från 1970-talet i ljus träpanel i ett villaområde i Vallentuna",
     "freshly painted 1970s Swedish single-storey villa with light beige wooden panelling and dark brown window frames, lawn and birch trees, suburban street, Vallentuna, no people"),
  ],
},
}
