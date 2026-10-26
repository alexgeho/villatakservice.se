# -*- coding: utf-8 -*-
"""Tillbyggnad – ortsidor v26: Botkyrka, Järfälla, Sigtuna, Solna, Sundbyberg, Hässelby (2026-10-26).
Hubb: tillbyggnad.html (TJ_HUB["tillbyggnad"]). Struktur som tj_v22_tillbyggnad.py. Tre bilder per sida.

Fakta endast från källorna i respektive 'sources', öppnade med curl (UA Mozilla) 2026-10-26, alla svarade 200:
  Boverket – Göra en tillbyggnad (30,0 m² sammanlagt, 30 m från järnvägs mitt, anmälan vid ventilation, eldstad,
    vatten, avlopp och väsentlig påverkan på bärande delar eller brandskydd).
  Botkyrka kommun – Tillbyggnad (uppdaterad 1 juni 2026): volymökning i vilken riktning som helst, praxis, 30,0 m²
    BTA/OPA, under taknock, tidigare skärmtak och attefallstillbyggnad räknas in, utökad lovplikt (järnväg 30 m,
    4,5 m till gräns, totalförsvar, särskilt värdefullt), webbkartans lager, gestaltningsprogram, allmän väg utanför
    plan, strandskydd, frivilligt bygglov. Kulturmiljöprogram (pdf, textlager, antaget 2014): Tullinge station 1903,
    Separator, Hamra egnahem 1920-talet, kataloghus (Boros Björkhamra), Uttran villaområde 1910–2010-tal, riktlinje
    att tillbyggnader underordnas huvudbyggnaden.
  Järfälla kommun – Bygglovsbefriade åtgärder (från 1 december 2025, liten avvikelse, skyddsbestämmelser om mark-
    förorening/olyckor/översvämning/erosion, anmälan). Kulturmiljöplan Kallhäll (pdf, textlager): Stålringen tidigt
    1960-tal, Widmark & Platzer, arkitekt Lars Henschen, stadsplan S800212 max byggnadsyta 200 m², remsa mot gatan
    får inte bebyggas, tillbyggnader bör läggas mot trädgårdssidan, takkupor harmoniera; Bolinderbyn radhus från 1945
    (bostadsrätt) och privatägda villor.
  Sigtuna kommun – Generella regler för tillbyggnad (påbyggnad, källarutgrävning och takkupor räknas, handlingar:
    situationsplan, fasad-, plan-, sektions- och konstruktionsritningar, kontrollplan; totalförsvar vid flygplats för
    tillbyggnad av komplementbostadshus), Inglasning av uterum, Flygbuller (Arlanda riksintresse, Swedavia yttrar sig
    vid tillbyggnad inom influensområdet), Bygga i kulturmiljö.
  Solna stad – Bygglovsfria åtgärder (stora delar KV, lista över riksintressen och sammanhängande miljöer, k och q
    kring Sjövägen, Bergshamra by, Stocksundstorp; fastighetsägarens tillstånd; frivilligt bygglov), Kulturmiljöer i
    Solna, Ändra bärande konstruktion (utlåtande från konstruktör m.m.).
  Sundbybergs stad – Tillbyggnad bygglovsbefriad (gäller inte KV-byggnader och Duvbo, frivilligt bygglov kostar som
    vanligt bygglov), Tillbyggnad av en- och tvåbostadshus (underordna, hörn fria, handlingar, ofta kontrollansvarig,
    uterum kan räcka med kontrollplan), Trädfällning i Duvbo (marklov > 20 cm på 1,3 m), Miljöprogram Duvbo (pdf,
    textlager; Egna Hem 1898, 325 tomter, 1924 ytterligare 98, riksintresse 1987, tillbyggnadsriktlinjer).
  Stockholms stad – Tillbyggnad (bygglovsbefriad); Stockholmskällan/Stockholmshem – Västra Smedshagen, Hässelby
    Villastad (pdf, OCR-textlager, läsbart): arbetare arrenderade tomter 1893, försäljning utan styckningsplan,
    municipalsamhälle 1914, stadsplan 1926, köping 1926, ett hundratal sommarstugor på 1920-talet; Områdesfakta 2025
    Hässelby villastad; Varsam utveckling (1960–70-tal, tomter kring 600 m²).
  Skatteverket – Ger arbetet rätt till rotavdrag? (WebFetch): tillbyggnad där en sida sitter ihop med ytterväggen till
    minst 75 % eller dörr emellan, bostaden äldre än fem år, större delen av stommen behålls; 30 % i exemplen.
Strukna: avgifter, handläggningstider, vilka orter i Botkyrka som ligger inom totalförsvarets intresseområden (ingen
källa – bara att kartlagret finns), radonvärden.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"

_BV_TB = ("Boverket – Göra en tillbyggnad",
          "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/gora-en-tillbyggnad/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")

_ROT1 = ("Rotavdraget gäller arbetskostnaden, inte material. Skatteverket räknar en tillbyggnad av ett bostadshus som "
         "rotarbete om någon av dess sidor sitter ihop med husets yttervägg till minst 75 procent eller om en dörr "
         "förbinder de två delarna.")
_ROT2 = ("Bostaden ska vara äldre än fem år och större delen av den ursprungliga stommen ska behållas. Där avdraget "
         "gäller drar Geal det direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ BOTKYRKA
"tillbyggnad-botkyrka.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Botkyrka", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Botkyrka – Tullinge, Uttran och kartan",
  "description": "Tillbyggnad i Botkyrka: vad som räknas som tillbyggnad, potten på 30 kvadratmeter, webbkartans lager och kulturmiljöprogrammet för Tullinge och Uttran.",
  "h1": "Tillbyggnad i Botkyrka",
  "lead": "Ett uterum, en större takkupa eller ett nytt sovrum på husets baksida – i Botkyrka kan en tillbyggnad vara lovfri eller kräva bygglov beroende på var huset står. Geal Entreprenad AB går igenom kommunens regler och kartan för din tomt och bygger sedan till huset med total entreprenad.",
  "card": "Villorna i Tullinge, Uttran och kartan.",
  "sections": [
    {"id": "vad-ar-tillbyggnad-botkyrka", "anchor": "Vad som räknas",
     "h2": "Vad räknas som en tillbyggnad?",
     "paras": [
       "Botkyrka kommun förklarar att en tillbyggnad är en ändring som ökar byggnadens volym, och att det inte spelar någon roll åt vilket håll ökningen sker. Det kan alltså vara en utbyggnad mot trädgården, en påbyggnad på taket eller en större takkupa. Kommunen skriver också att det finns en utvecklad praxis för vad som bedöms som tillbyggnad, där flera faktorer vägs in.",
       "Huvudregeln är att en tillbyggnad kräver bygglov. Men på ett hus som inte är en komplementbyggnad krävs inget lov om tillbyggnaden är högst 30,0 kvadratmeter bruttoarea eller öppenarea och inte går över husets taknock. Tidigare lovfria tillbyggnader på huset – till exempel ett skärmtak eller en attefallstillbyggnad – räknas in i samma 30 kvadratmeter.",
     ],
     "aside": {"title": "Lovfri tillbyggnad", "items": [
       "Högst 30,0 m² BTA eller OPA", "Inte över husets taknock", "Tidigare lovfria tillbyggnader räknas in"]}},
    {"id": "kartan-botkyrka", "h2": "Webbkartan visar var lov ändå krävs",
     "paras": [
       "Kommunen listar flera lägen där utökad lovplikt gäller: närmare än 30 meter från ett järnvägsspårs mitt, närmare än 4,5 meter från gränsen utan grannarnas medgivande, inom eller intill områden av riksintresse för totalförsvaret och på särskilt värdefulla byggnader eller i särskilt värdefulla områden. För att se vad som gäller hänvisar kommunen till sin webbkarta, med lager för kulturmiljöprogrammet, detaljplaner och riksintressen för kulturmiljövård och totalförsvar.",
       "Vi går igenom lagren för din fastighet innan vi ritar. Kommunen påminner också om att översiktsplanen och eventuella gestaltningsprogram kan peka ut värdefulla miljöer, att strandskydd kan kräva dispens och att åtgärder nära allmän väg utanför detaljplan kan kräva särskilt tillstånd.",
     ],
     "aside": None},
    {"id": "tullinge-uttran", "h2": "Villorna i Tullinge och Uttran",
     "paras": [
       "Botkyrkas kulturmiljöprogram beskriver hur Tullinge växte till ett villasamhälle sedan järnvägsstationen öppnat 1903, och hur egnahemsområdet Hamra egnahem planlades på 1920-talet söder om järnvägen. Där dominerar kataloghus från 1920- och 1940-talen, bland annat Boros villa Björkhamra. Uttran beskrivs som ett villaområde som byggts från 1910-talet fram till 2010-talet, med nationalromantiska villor, 1920-talsklassicism, funkis och senare hustyper.",
       "Programmets riktlinjer är tydliga: tillbyggnader ska underordnas huvudbyggnaden och få en placering, höjd, volym och utformning som är anpassad till den ursprungliga byggnadens karaktär. För ett kataloghus med symmetrisk fasad betyder det ofta en lägre tillbyggnad på baksidan i stället för en ny volym mot gatan. Programmet säger också att grundstrukturen i gatunät och tomtindelning ska respekteras och att omfattande utfyllnader, stödmurar och hårdgjorda ytor ska undvikas – något att tänka på när en tillbyggnad ska grundläggas på de kuperade tomterna vid Tullingesjön.",
     ],
     "aside": {"title": "Riktlinjen för tillbyggnader", "items": [
       "Underordnas huvudbyggnaden", "Anpassad placering och höjd", "Volym och form efter husets karaktär"]}},
    {"id": "anmalan-botkyrka", "h2": "Anmälan och frivilligt bygglov",
     "paras": [
       "Även en lovfri tillbyggnad kan kräva anmälan och startbesked, till exempel när husets bärande delar eller brandskydd påverkas väsentligt eller när ett nytt badrum får vatten och avlopp. Då tar vi fram konstruktionsunderlag och ett förslag till kontrollplan innan arbetet börjar.",
       "Vill du ha ett bindande beslut kan du söka frivilligt bygglov. Kommunen skriver att det ger trygghet inför bygget och minskar risken att åtgärden ifrågasätts senare, men att prövningen kostar en bygglovsavgift. Står det redan ett attefallshus på tomten och funderar du på mer boyta där beskriver vi det under " + _L.format("attefallshus-botkyrka.html", "attefallshus i Botkyrka") + ". Allmänt om utbyggnader finns under " + _L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi till ett hus i Botkyrka",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter huset och tidigare tillbyggnader."),
    ("Kartan", "Webbkartans lager och detaljplanen kontrolleras för fastigheten."),
    ("Ritningar", "Förslag som underordnar sig huset, med konstruktionsunderlag."),
    ("Lov eller anmälan", "Bygglov, anmälan eller frivilligt bygglov – efter vad som gäller."),
    ("Bygget", "Grund, stomme, tak, anslutning mot huset och invändigt."),
    ("Slutbesked", "Den nya delen används när slutbeskedet har kommit."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Botkyrka",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Botkyrka?",
  "price": [
    "Storlek och grundläggning, hur den nya delen ansluter till tak och fasad, om bärande väggar öppnas, våtrum och installationer samt om bygglov och ritningar för en kulturmiljö behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Räknas en takkupa som tillbyggnad i Botkyrka?",
     "Ja, om den ökar husets volym. Kommunen skriver att det inte spelar någon roll åt vilket håll volymen ökar."),
    ("Vilka lager i Botkyrkas webbkarta ska vi titta på före en tillbyggnad?",
     "Kulturmiljöprogrammet, detaljplanerna och riksintressena för kulturmiljövård och totalförsvar. Kommunen anger dem som de viktigaste för utökad lovplikt."),
    ("Hur ska en tillbyggnad på ett kataloghus i Tullinge se ut?",
     "Enligt kulturmiljöprogrammet ska den underordnas huvudbyggnaden och anpassas i placering, höjd och volym. Ofta blir det en lägre del på baksidan."),
    ("Kan vi få ett beslut på en lovfri tillbyggnad i Botkyrka?",
     "Ja, genom frivilligt bygglov. Kommunen prövar då åtgärden och tar ut en bygglovsavgift."),
    ("Räknas vårt gamla skärmtak in när vi bygger till i Botkyrka?",
     "Ja. Kommunen skriver att redan utförda lovfria åtgärder som skärmtak och attefallstillbyggnad ska läggas ihop med den nya tillbyggnaden i de 30 kvadratmetrarna."),
  ],
  "sources": [("Botkyrka kommun – Tillbyggnad", "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/tillbyggnad"),
              ("Botkyrka kommun – Kulturmiljöprogram, antaget 2014 (pdf)", "https://www.botkyrka.se/download/18.1fbbaae6170bff9469deb7f/1602575505534/Kulturmilj%C3%B6program.pdf"),
              _BV_TB, _SKV],
  "cta": ("Funderar du på att bygga till i Botkyrka?", "Boka ett gratis platsbesök, så går vi igenom kartan och huset innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Kataloghus från 1920-talet med en lägre tillbyggnad på baksidan mot trädgården",
     "1920s Swedish catalogue house with symmetrical facade, light yellow wooden panel and a hipped red tile roof, with a lower new single-storey extension with large windows on the garden side, lawn and birch trees, summer daylight" + _SFX),
    ("Nationalromantisk trävilla på en höjd i ett villaområde",
     "early 1900s Swedish national romantic wooden villa with steep roof, dark brown panel and white window frames set on a wooded hill above a winding road, pine trees, late summer light" + _SFX),
    ("Ny takkupa på ett sadeltak med rött tegel",
     "newly built dormer with white trim on a red clay tile gable roof of an older Swedish house, scaffolding partly visible, blue sky, no workers" + _SFX),
  ],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"tillbyggnad-jarfalla.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Järfälla", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Järfälla – lovfritt och kulturmiljöplanen",
  "description": "Tillbyggnad i Järfälla: lovfria tillbyggnader sedan december 2025, liten avvikelse, skyddsbestämmelser och kulturmiljöplanens råd för villorna i Kallhäll.",
  "h1": "Tillbyggnad i Järfälla",
  "lead": "Sedan 1 december 2025 kan fler tillbyggnader göras utan bygglov i Järfälla, men kommunen påminner om att reglerna för gränser, kulturmiljö och skydd mot översvämning fortfarande gäller. Geal Entreprenad AB reder ut vad som gäller för ditt hus och bygger till med total entreprenad.",
  "card": "Lovfritt, avvikelser och Kallhälls villor.",
  "sections": [
    {"id": "lovfritt-jarfalla", "anchor": "Lovfritt",
     "h2": "Lovfritt sedan december 2025 – med villkor",
     "paras": [
       "Järfälla kommun skriver att flera åtgärder som tidigare krävde bygglov blev lovbefriade den 1 december 2025, och tillbyggnad är en av dem. Det som avgör är bland annat avståndet till tomtgränsen, byggnadsarea och höjd, skriftligt grannemedgivande, närheten till järnväg, om byggnaden eller området är särskilt värdefullt och vad detaljplanen säger.",
       "Enligt Boverket får en lovfri tillbyggnad vara högst 30,0 kvadratmeter sammanlagt, och tidigare lovfria tillbyggnader räknas in. Den ska stå minst 30 meter från en järnvägs mitt om infrastrukturförvaltaren inte har gett sitt skriftliga medgivande. Kommunen påpekar dessutom att du måste hålla dig inom den totalt tillåtna arean för komplementbyggnader, komplementbostadshus och tillbyggnader.",
     ],
     "aside": {"title": "Järfälla listar", "items": [
       "Avstånd till tomtgräns", "Area och nockhöjd", "Skriftligt grannemedgivande", "Järnväg, totalförsvar, kulturmiljö"]}},
    {"id": "skydd-jarfalla", "h2": "Skyddsbestämmelser och liten avvikelse",
     "paras": [
       "Två saker i kommunens text är lätta att missa. Lovbefriade åtgärder får inte strida mot skyddsbestämmelser om markförorening, olyckor, översvämning eller erosion. Och de lovbefriade åtgärder som inte är undantagna från detaljplanen får bara avvika från planen om avvikelsen är liten och inte motverkar planens syfte.",
       "Vi läser därför detaljplanen för fastigheten innan vi ritar, och vi ser efter om det finns planbestämmelser om exempelvis översvämning. Grannemedgivanden ska vara skriftliga, och om tillbyggnaden väsentligt påverkar brandskydd, bärande konstruktion, vatten, avlopp eller ventilation krävs anmälan och startbesked.",
     ],
     "aside": None},
    {"id": "stalringen", "h2": "Stålringen i Kallhäll – bygg mot trädgården",
     "paras": [
       "Järfällas kulturmiljöplan beskriver villaområdet vid Stålringen och Tennringen i Kallhäll, som byggdes i början av 1960-talet av Widmark & Platzer med Lars Henschen som arkitekt. Husen ligger med gavlarna mot gatan, har beige spritputs och branta sadeltak med rött lertegel. Stadsplanen tillåter en byggnadsyta på högst 200 kvadratmeter, så det finns byggrätt kvar, men en smal remsa närmast gatan får inte bebyggas.",
       "Planen ger rådet att tillbyggnader bör läggas mot trädgårdssidan och att nya takkupor bör harmoniera med husens utformning. Den konstaterar samtidigt att det inte finns något särskilt skydd för de kulturhistoriska värdena där. Vi ritar ändå gärna efter rådet, eftersom gatubilden med gavlarna är det som gör området enhetligt. Planen beskriver också hur gatan lagts som en slinga på sluttande mark och hur delar av den ursprungliga barrskogen har sparats i områdets utkanter.",
     ],
     "aside": {"title": "Kallhäll, Stålringen", "items": [
       "Villor från tidigt 1960-tal", "Byggnadsyta högst 200 m²", "Remsan mot gatan får inte bebyggas",
       "Tillbyggnad mot trädgården"]}},
    {"id": "bolinderbyn", "h2": "Radhusen i Bolinderbyn",
     "paras": [
       "I Bolinderbyn byggde Bolinders radhus och villor åt sina anställda. Kulturmiljöplanen berättar att radhuslängorna längs Bolindervägen började byggas 1945 och att det sammanlagt blev 21 längor. Radhusen upplåts med bostadsrätt, medan villorna är privatägda.",
       "Den skillnaden är viktig för en tillbyggnad. I ett radhus med bostadsrätt är det föreningen som äger huset, och en utbyggnad kräver föreningens tillstånd innan något annat. I en villa är det du som fastighetsägare som ansvarar för att lagen följs. Läs gärna även om " + _L.format("attefallshus-jarfalla.html", "attefallshus i Järfälla") + " om du väger en utbyggnad mot ett eget gårdshus, och om utbyggnader i allmänhet under " + _L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi till ett hus i Järfälla",
  "steps": [
    ("Platsbesök", "Vi mäter huset, tidigare tillbyggnader och avstånden till gränserna."),
    ("Detaljplanen", "Planbestämmelser, skyddsbestämmelser och kulturmiljö kontrolleras."),
    ("Ritningar", "Förslag mot trädgårdssidan med konstruktionsunderlag."),
    ("Anmälan", "Anmälan och startbesked där bärande delar eller installationer berörs."),
    ("Bygget", "Grund, stomme, tak och anslutning till befintligt hus."),
    ("Slutbesked", "Den nya delen tas i bruk efter slutbesked."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Järfälla",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Järfälla?",
  "price": [
    "Storlek, grundläggning, hur takfall och fasad ska mötas, om väggar mot befintligt hus öppnas, våtrum och installationer samt om det behövs bygglov eller anmälan. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga till mot gatan på Stålringen i Kallhäll?",
     "Enligt kulturmiljöplanen får en smal remsa närmast gatan inte bebyggas. Villor som ligger längre in på tomten kan byggas till även mot gatan, men planen rekommenderar trädgårdssidan."),
    ("Vad är en liten avvikelse för en lovfri tillbyggnad i Järfälla?",
     "Kommunen skriver att lovbefriade åtgärder som inte är undantagna från planen får avvika om avvikelsen är liten och inte motverkar planens syfte."),
    ("Kan vi bygga ut vårt radhus i Bolinderbyn?",
     "Radhusen där upplåts med bostadsrätt, så det är föreningen som äger huset. Börja med att fråga styrelsen."),
    ("Gäller lovfriheten om tomten har skyddsbestämmelser mot översvämning i Järfälla?",
     "Nej. Kommunen skriver att lovbefriade åtgärder inte får strida mot skyddsbestämmelser om markförorening, olyckor, översvämning eller erosion."),
    ("Måste grannens medgivande vara skriftligt i Järfälla?",
     "Ja. Kommunen skriver uttryckligen att grannemedgivanden måste vara skriftliga."),
  ],
  "sources": [("Järfälla kommun – Bygglovsbefriade åtgärder", "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/bygglovsbefriadeatgarder.4.a41712119a05132defe8bb3.html"),
              ("Järfälla kommun – Kulturmiljöplan, Kallhäll (pdf)", "https://www.jarfalla.se/download/18.68e7a727168e12dd179a407f/1550245859848/kulturmiljoplan-kallhall.pdf"),
              _BV_TB, _SKV],
  "cta": ("Vill du bygga till ditt hus i Järfälla?", "Boka ett gratis platsbesök, så läser vi detaljplanen och mäter huset innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Putsad villa från 1960-talet med brant sadeltak och en ny tillbyggnad mot trädgården",
     "1960s Swedish villa with beige spray plaster facade and steep red clay tile gable roof, gable end facing the street, a new low extension with wooden cladding and large windows on the garden side, lawn and pine trees, summer daylight" + _SFX),
    ("Villagata som slingrar sig i en sluttning med gavlar mot gatan",
     "curving suburban street on a gentle slope with 1960s Swedish plastered villas placed with their gables facing the street, steep red tile roofs, pine forest at the edge, overcast daylight" + _SFX),
    ("Radhuslängor i två våningar med små trädgårdar",
     "1940s Swedish two-storey terraced house rows with light plastered facades and gable roofs, small front gardens with hedges, quiet street, summer daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SIGTUNA
"tillbyggnad-sigtuna.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Sigtuna", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Sigtuna – Arlanda, uterum och handlingar",
  "description": "Tillbyggnad i Sigtuna: Swedavias yttrande inom flygbullrets influensområde, inom och utanför plan, uterum och takkupor och kommunens handlingar.",
  "h1": "Tillbyggnad i Sigtuna",
  "lead": "I Sigtuna kommun ligger Arlanda, och det påverkar även den som vill bygga till sitt hus. Inom flygbullrets influensområde begär kommunen ett yttrande från Swedavia innan bygglov ges. Geal Entreprenad AB tar fram handlingarna och bygger tillbyggnaden med total entreprenad.",
  "card": "Arlanda, uterum och handlingarna.",
  "sections": [
    {"id": "arlanda-sigtuna", "anchor": "Arlanda",
     "h2": "Inom flygbullrets influensområde",
     "paras": [
       "Sigtuna kommun beskriver Arlanda som ett riksintresse enligt miljöbalken, både för dagens verksamhet och för framtida utbyggnad. Det område som påverkas av flygbullret kallas influensområdet. Vill du bygga nytt eller göra en tillbyggnad där kontaktar kommunen Swedavia för ett utlåtande innan beslutet fattas.",
       "Bygg- och miljönämnden väger bland annat in bullersituationen, hur avloppet löses och markens radonhalt. Kommunen skriver att den ibland kan acceptera byggnation om man vidtar bullerbegränsande åtgärder, till exempel avskärmning eller isolering av byggnaden. För en tillbyggnad med sovrum kan det alltså påverka både fönster och väggar.",
     ],
     "aside": {"title": "Kommunen väger in", "items": [
       "Bullersituationen", "Hur avloppet ska lösas", "Markens radonhalt", "Bullerdämpande åtgärder"]}},
    {"id": "plan-sigtuna", "h2": "Inom och utanför detaljplan",
     "paras": [
       "Kommunen skriver att huvudregeln är bygglov för tillbyggnader, men att det finns undantag. Både inom och utanför detaljplan är en tillbyggnad lovfri om den är högst 30 kvadratmeter, inte går över husets taknock och tillsammans med tidigare lovfria tillbyggnader inte blir större än 30 kvadratmeter. Lovfriheten gäller alla typer av byggnader, inte bara en- och tvåbostadshus.",
       "Lov krävs ändå om huset ligger närmare gränsen än 4,5 meter utan grannens medgivande, inom 30 meter från ett järnvägsspårs mitt utan medgivande, eller i ett kulturhistoriskt särskilt värdefullt område. Kommunen nämner också att den som vill bygga till ett komplementbostadshus nära en flygplats som är riksintresse för totalförsvaret behöver bygglov.",
     ],
     "aside": None},
    {"id": "uterum-sigtuna", "h2": "Uterum, takkupor och källare",
     "paras": [
       "Enligt kommunen räknas alla åtgärder som ökar en byggnads volym som tillbyggnad – påbyggnader, källarutgrävningar och takkupor som ökar volymen. Ett inglasat uterum eller en inglasad uteplats kan också vara en tillbyggnad, och om den inte ryms i den lovfria potten behövs bygglov. Till en sådan ansökan vill kommunen ha situationsplan, planritning, fasadritningar, en teknisk beskrivning av inglasningen och förslag till kontrollplan.",
       "Situationsplanen ska göras på kommunens karta. Sigtuna låter dig ladda ned tomtkartan som pdf utan inloggning och utan kostnad, och sedan markeras tillbyggnaden på den. Vi tar fram ritningarna och kontrollplanen åt dig. Kontrollplanen ska enligt kommunen ange vilken fastighet det gäller och vem som är byggherre, vad som ska kontrolleras, vem som gör kontrollerna, hur de görs och dokumenteras, när i processen de görs och ha plats för datum och signatur. Den som har fått startbesked får sedan påbörja arbetet.",
     ],
     "aside": {"title": "Handlingar till bygglov", "items": [
       "Situationsplan på tomtkartan", "Fasad-, plan- och sektionsritning", "Konstruktionsritningar", "Förslag till kontrollplan"]}},
    {"id": "kulturmiljo-sigtuna", "h2": "Sigtuna stad och kulturmiljöerna",
     "paras": [
       "Kommunen skriver att tillbyggnader i en kulturmiljö ska utföras varsamt och att vissa byggnader och områden är så värdefulla att de inte får förvanskas. Där kan bygglov krävas även för tillbyggnader som annars är lovfria. För Sigtuna stad finns en bevarande- och förnyelseplan, och för dalgången mellan Odensala och Hova finns egna riktlinjer.",
       "Kommunens råd är att behålla formspråk, proportioner och karaktärsdrag, att ge akt på fasader, tak, fönster och entréer och att bevara ursprungliga material eller byta mot samma material. Om tillbyggnaden påverkar husets bärande konstruktion, brandskydd eller ventilation väsentligt krävs anmälan, och arbetet får börja först efter startbesked. Vill du hellre bygga ett fristående hus beskriver vi det under " + _L.format("attefallshus-sigtuna.html", "attefallshus i Sigtuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi till ett hus i Sigtuna",
  "steps": [
    ("Läget", "Vi ser om fastigheten ligger inom influensområdet, en detaljplan eller en kulturmiljö."),
    ("Platsbesök", "Huset och tidigare tillbyggnader mäts vid ett gratis besök."),
    ("Handlingar", "Tomtkarta, ritningar, konstruktion och kontrollplan tas fram."),
    ("Lov eller anmälan", "Ansökan eller anmälan skickas via kommunens e-tjänst."),
    ("Bygget", "Grund, stomme, tak och anslutning, med bulleråtgärder där det behövs."),
    ("Slutbesked", "Den nya delen tas i bruk efter slutbesked."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Sigtuna",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Sigtuna?",
  "price": [
    "Storlek och grundläggning, bullerdämpande fönster och väggar där det krävs, anslutningen mot befintligt tak och fasad, installationer och omfattningen av handlingarna. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför vill Sigtuna kommun ha Swedavias yttrande om vår tillbyggnad?",
     "Om fastigheten ligger inom Arlandas influensområde för flygbuller kontaktar kommunen Swedavia innan den beslutar om nybyggnad eller tillbyggnad."),
    ("Räknas en källarutgrävning som tillbyggnad i Sigtuna?",
     "Ja, om den ökar husets volym. Kommunen nämner påbyggnader, källarutgrävningar och takkupor som exempel."),
    ("Var får vi tomtkartan till situationsplanen i Sigtuna?",
     "Kommunen låter dig ladda ned tomtkartan som pdf utan inloggning och utan kostnad."),
    ("Kan bullret stoppa en tillbyggnad med sovrum nära Arlanda?",
     "Det kan begränsa möjligheten. Kommunen skriver att bygget ibland kan accepteras om man vidtar bullerdämpande åtgärder som avskärmning eller isolering."),
    ("Gäller lovfriheten även utanför detaljplan i Sigtuna?",
     "Ja, för tillbyggnader på upp till 30 kvadratmeter som inte går över taknocken. Kulturmiljö, gränser och järnväg kan ändå kräva lov."),
  ],
  "sources": [("Sigtuna kommun – Generella regler för tillbyggnad", "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/bygga-till/generella-regler-for-tillbyggnad.html"),
              ("Sigtuna kommun – Inglasning av uterum", "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/bygga-till/inglasning-av-uterum.html"),
              ("Sigtuna kommun – Flygbuller", "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/flygbuller.html"),
              ("Sigtuna kommun – Bygga i kulturmiljö", "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html"),
              _BV_TB, _SKV],
  "cta": ("Planerar du en tillbyggnad i Sigtuna?", "Boka ett gratis platsbesök, så går vi igenom läget, bullret och handlingarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa med ett nybyggt inglasat uterum mot en gräsmatta",
     "1980s Swedish wooden villa painted dark red with white trim and a newly built glazed sunroom extension with a slim black frame on the garden side, lawn and flowering shrubs, flat countryside in the distance, summer daylight" + _SFX),
    ("Tomtkarta och ritningar på ett bord bredvid en tumstock",
     "printed site map and architectural drawings without readable text spread on a wooden table next to a folding ruler, soft daylight from a window" + _SFX),
    ("Låga trähus längs en gata i en gammal småstad",
     "row of small old wooden houses with red clay tile roofs along a narrow street in a small historic Swedish lakeside town, lake glimpsed at the end of the street, summer morning light" + _SFX),
  ],
},

# ------------------------------------------------------------------ SOLNA
"tillbyggnad-solna.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Solna", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Solna – när kulturmiljön kräver lov",
  "description": "Tillbyggnad i Solna: varför lovfriheten ofta inte gäller, Råsunda, Råsta egnahem och Bergshamra by, bärande konstruktion och fastighetsägarens tillstånd.",
  "h1": "Tillbyggnad i Solna",
  "lead": "Solna stad skriver rakt ut att undantagen från bygglov ofta inte kan användas i Solna, eftersom stora delar av staden är kulturhistoriskt värdefulla. För en tillbyggnad betyder det att kartan och planen måste läsas först. Geal Entreprenad AB tar fram underlaget och bygger till huset med total entreprenad.",
  "card": "Kulturmiljöerna och lovet.",
  "sections": [
    {"id": "kulturmiljo-solna", "anchor": "Kulturmiljön",
     "h2": "Stora delar av Solna är kulturmiljö",
     "paras": [
       "På stadens sida om bygglovsfria åtgärder står att en lovfri tillbyggnad på ett en- eller tvåbostadshus får vara högst 30 kvadratmeter brutto- eller öppenarea, och att tidigare skärmtak och attefallstillbyggnader räknas in. Men staden skriver också att dessa åtgärder oftast inte kan utföras i Solna, eftersom de inte får göras på en byggnad eller i ett bebyggelseområde som är särskilt kulturhistoriskt värdefullt.",
       "Staden räknar upp riksintressena för kulturmiljövården – Karlberg, Solna kyrkby- och radhusbebyggelse, Ulriksdal och Hagaparken – och de sammanhängande värdefulla miljöerna i översiktsplanen, bland andra Råsunda villastad, villabebyggelsen i norra Råsunda, Råsta egnahem och Alnäs och Stocksundstorp.",
     ],
     "aside": {"title": "Exempel på utpekade miljöer", "items": [
       "Råsunda villastad", "Villorna i norra Råsunda", "Råsta egnahem", "Alnäs och Stocksundstorp"]}},
    {"id": "k-och-q-solna", "h2": "k- och q-bestämmelser i planen",
     "paras": [
       "Utöver de utpekade miljöerna nämner staden en- och tvåbostadshus som är klassade som kulturhistoriskt värdefulla i översiktsplanen eller i Solnas kulturminnesvårdsprogram, och hus inom detaljplaner med varsamhets- eller skyddsbestämmelser, så kallade k och q. Det gäller bland annat områdena kring Sjövägen, Bergshamra by och Stocksundstorp.",
       "Står ditt hus i en sådan miljö räknar vi med en bygglovsansökan från början. Då blir gestaltningen viktig: tillbyggnaden ska anpassas till husets ursprungliga karaktär och inte förvanska det. Staden hänvisar till Solnakartan för att se vilka byggnader och miljöer som är utpekade.",
     ],
     "aside": None},
    {"id": "barande-solna", "h2": "När väggen mot det gamla huset öppnas",
     "paras": [
       "En tillbyggnad blir oftast meningsfull först när den öppnas mot resten av huset. Solna stad skriver att invändiga ändringar som påverkar bärande delar kräver anmälan och startbesked, till exempel avväxling av en bärande vägg eller håltagning i ett bärande bjälklag. Till anmälan hör ett utlåtande från konstruktör, konstruktionsritning, planritning och sektionsritning.",
       "Ibland krävs dessutom en kontrollansvarig. Vi tar fram konstruktionsunderlaget tillsammans med en konstruktör och ser till att anmälan är komplett innan väggen rörs. Staden skriver också att de flesta områden i Solna har en detaljplan, och att fastigheter utanför plan ofta har stora kulturvärden och skyddas på annat sätt – till exempel slottsområdena Haga och Ulriksdal, som är statliga byggnadsminnen.",
     ],
     "aside": {"title": "Anmälan om bärande delar", "items": [
       "Utlåtande från konstruktör", "Konstruktionsritning", "Plan- och sektionsritning", "Ibland kontrollansvarig"]}},
    {"id": "tillstand-solna", "h2": "Fastighetsägaren, strandskydd och frivilligt lov",
     "paras": [
       "Staden påminner om att fastighetsägarens tillstånd behövs även när åtgärden inte kräver lov eller anmälan – något att tänka på för den som äger ett radhus i en förening eller hyr. Ligger fastigheten inom strandskyddat område kan det krävas dispens, och i vissa lägen tillstånd från andra myndigheter.",
       "Är tillbyggnaden lovfri kan du söka frivilligt bygglov för att få stadens bedömning av att den är lagenlig. Då betalar du bygglovsavgift som vanligt. Den som bygger utan startbesked när ett sådant krävs riskerar en byggsanktionsavgift. Mer om utbyggnader finns under " + _L.format("tillbyggnad.html", "tillbyggnad") + ", och om husets helhet under " + _L.format("byggforetag-solna.html", "byggföretag i Solna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi till ett hus i Solna",
  "steps": [
    ("Solnakartan", "Vi kontrollerar om huset eller miljön är utpekad och vilka planbestämmelser som gäller."),
    ("Platsbesök", "Gratis besök där huset och tidigare tillbyggnader mäts."),
    ("Ritningar", "Förslag anpassat till husets karaktär, med konstruktionsunderlag."),
    ("Lov och anmälan", "Bygglovsansökan och anmälan för bärande delar."),
    ("Bygget", "Grund, stomme, tak och öppning mot befintligt hus."),
    ("Slutbesked", "Den nya delen tas i bruk efter slutbesked."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Solna",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Solna?",
  "price": [
    "Om bygglov och anpassade ritningar behövs, storlek och grundläggning, hur bärande väggar öppnas, material som ska matcha huset och installationer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför gäller inte lovfriheten för tillbyggnader i stora delar av Solna?",
     "Staden skriver att de lovfria åtgärderna inte får göras på byggnader eller i områden som är särskilt kulturhistoriskt värdefulla, och att stora delar av Solna är det."),
    ("Krävs bygglov för en tillbyggnad i Råsta egnahem?",
     "Råsta egnahem är utpekat som sammanhängande kulturhistoriskt värdefull miljö i översiktsplanen. Räkna med bygglov och kontrollera Solnakartan för ditt hus."),
    ("Vilka handlingar behövs för att öppna en bärande vägg mot tillbyggnaden i Solna?",
     "Staden nämner anmälan, utlåtande från konstruktör, konstruktionsritning, planritning och sektionsritning. Ibland krävs kontrollansvarig."),
    ("Behövs tillstånd även för en lovfri tillbyggnad i Solna?",
     "Ja, fastighetsägarens tillstånd behövs även då. Strandskyddsdispens eller andra tillstånd kan också krävas beroende på läget."),
    ("Vad händer om vi börjar bygga till i Solna utan startbesked?",
     "Staden skriver att den som påbörjar en åtgärd utan startbesked får betala en byggsanktionsavgift, och att den som bygger utan lov kan behöva söka lov i efterhand eller rätta felen."),
    ("Var ser vi om vårt hus i Solna är kulturklassat?",
     "I Solnakartan, där staden visar kulturhistoriskt klassade byggnader och värdefulla miljöer. Vid osäkerhet kan du kontakta stadens kontaktcenter."),
  ],
  "sources": [("Solna stad – Bygglovsfria åtgärder", "https://www.solna.se/bygga-bo--miljo/bygga/bygglov/bygglovsfria-atgarder"),
              ("Solna stad – Kulturmiljöer i Solna", "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna"),
              ("Solna stad – Ändra bärande konstruktion", "https://www.solna.se/bygga-bo--miljo/bygga/anmalan/andra-barande-konstruktion"),
              _BV_TB, _SKV],
  "cta": ("Vill du bygga till i Solna?", "Boka ett gratis platsbesök, så kontrollerar vi kartan och planen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre villa i puts med en anpassad tillbyggnad i samma färg mot trädgården",
     "1920s Swedish villa with light ochre plaster facade and a hipped dark tile roof, with a carefully matched lower plastered extension with small-paned windows on the garden side, mature trees and hedge, summer daylight" + _SFX),
    ("Avväxlingsbalk i en öppning i en bärande vägg under ombyggnad",
     "interior renovation: new steel beam and timber posts supporting a newly cut wide opening in a load-bearing wall between an old room and a new extension, dust sheets on the floor, no workers, daylight" + _SFX),
    ("Villagata med träd, häckar och äldre villor i en villastad",
     "quiet street in an early 1900s Swedish villa town with plastered and wooden villas behind hedges and old trees, autumn colours, soft light" + _SFX),
  ],
},

# ------------------------------------------------------------------ SUNDBYBERG
"tillbyggnad-sundbyberg.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Sundbyberg", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Sundbyberg – Duvbo och reglerna",
  "description": "Tillbyggnad i Sundbyberg: varför lovfriheten inte gäller i Duvbo, miljöprogrammets riktlinjer, träden och marklovet, handlingar och kontrollansvarig.",
  "h1": "Tillbyggnad i Sundbyberg",
  "lead": "I Sundbyberg gäller de lovfria tillbyggnaderna inte i Duvbo eller på kulturhistoriskt värdefulla byggnader. I villastaden krävs alltså bygglov, och staden har tydliga riktlinjer för hur en tillbyggnad ska se ut. Geal Entreprenad AB ritar efter dem och bygger till huset med total entreprenad.",
  "card": "Duvbo, träden och riktlinjerna.",
  "sections": [
    {"id": "duvbo-lov", "anchor": "Duvbo",
     "h2": "I Duvbo krävs bygglov",
     "paras": [
       "Sundbybergs stad skriver att lättnaden för bygglovsbefriade tillbyggnader inte gäller för kulturhistoriskt värdefulla byggnader eller i riksintresset Duvbo. Utanför dem får en tillbyggnad vara högst 30,0 kvadratmeter brutto- eller öppenarea och ska vara lägre än husets taknock, och tidigare attefallstillbyggnader, attefallstakkupor och lovfria skärmtak räknas in.",
       "Enligt stadens miljöprogram bildades föreningen Egna Hem 1898 och köpte året därpå egendomen Dufvebol, där en stadsplan med 325 tomter togs fram. Området utökades 1924 med ytterligare 98 villatomter, och 1987 pekade Riksantikvarieämbetet ut Duvbo som riksintresse för kulturmiljövården – som ett av de första exemplen på en välorganiserad egnahemsförstad i Stockholmstrakten.",
     ],
     "aside": {"title": "Duvbo i korthet", "items": [
       "Egna Hem bildades 1898", "325 tomter i första planen", "98 tomter till 1924", "Riksintresse sedan 1987"]}},
    {"id": "riktlinjer-sundbyberg", "h2": "Miljöprogrammets riktlinjer",
     "paras": [
       "Miljöprogrammet säger att en tillbyggnad inte får vara så stor eller placeras så att den dominerar över den ursprungliga huskroppen eller påverkar gatubilden. Husets ursprungliga volym ska gå att urskilja även efter tillbyggnaden. Tillbyggnaden ska ansluta till husets form, material och färg, och programmet skriver att plana tak inte hör hemma bland egnahemsbebyggelsen från 1900–1920-talen. Förgårdsmarken ska bevaras, och tillbyggnader och uthus ska läggas så att områdets öppenhet behålls.",
       "Stadens allmänna råd för tillbyggnader pekar åt samma håll: tillbyggnaden ska underordna sig husets volym, till exempel genom en lägre volym som håller avstånd till taknocken och lämnar husets hörn fria med tydliga indrag. I praktiken blir det ofta en tillbyggnad mot trädgården med sadeltak och samma panel som huset. Miljöprogrammet beskriver att husen från sekelskiftet och 1920-talet ofta står i två våningar på höga socklar och att träfasaderna ursprungligen målades med linoljefärg eller slamfärg i jordnära kulörer. Det är bra att utgå från när kulören på den nya delen ska bestämmas.",
     ],
     "aside": None},
    {"id": "trad-sundbyberg", "h2": "Träden och marklovet",
     "paras": [
       "Träden i Duvbo är skyddade i detaljplanen. Staden skriver att det krävs marklov för att fälla ett träd med en stamdiameter större än 20 centimeter på 1,3 meters höjd, och att den är restriktiv med att bevilja det. Till ansökan hör foton, en situationsplan med träden utmärkta och skälet till fällningen.",
       "En tillbyggnad som kräver att ett större träd tas ned blir därför två prövningar. Vi placerar hellre tillbyggnaden så att rotsystemen klarar sig, och om ett träd ändå står i vägen tar vi med marklovet i planeringen från början. Programmet nämner också att den utökade lovplikten i Duvbo omfattar bland annat fasadmaterial, omfärgning och byte av fönster.",
     ],
     "aside": {"title": "Marklov för träd i Duvbo", "items": [
       "Stam över 20 cm på 1,3 m höjd", "Foton på träden", "Situationsplan med träden", "Skäl till fällningen"]}},
    {"id": "handlingar-sundbyberg", "h2": "Handlingar och kontrollansvarig",
     "paras": [
       "Till en bygglovsansökan för tillbyggnad brukar staden vilja ha plan-, fasad- och sektionsritningar, en förenklad nybyggnadskarta, en material- och kulörbeskrivning samt kontrollansvarig eller kontrollplan. Staden skriver att det ofta krävs en kontrollansvarig vid en tillbyggnad, men att en kontrollplan kan räcka vid enklare tillbyggnader som ett uterum. Ritningarna ska vara skalenliga och ha måtten i millimeter.",
       "Utanför Duvbo kan en lovfri tillbyggnad ändå kräva anmälan om den påverkar konstruktion eller brandskydd väsentligt, eller om en eldstad eller vatten och avlopp installeras. Vill du ha ett beslut i förväg kan du söka frivilligt bygglov, som enligt staden kostar lika mycket som ett vanligt bygglov. Mer om större projekt finns under " + _L.format("byggforetag-sundbyberg.html", "byggföretag i Sundbyberg") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi till ett hus i Sundbyberg",
  "steps": [
    ("Läget", "Vi ser om huset ligger i Duvbo eller är kulturhistoriskt värdefullt."),
    ("Platsbesök", "Huset, träden och förgårdsmarken mäts in vid ett gratis besök."),
    ("Ritningar", "Tillbyggnad som underordnar sig huset, med material- och kulörbeskrivning."),
    ("Lov", "Bygglov, och marklov om ett större träd berörs."),
    ("Bygget", "Grund, stomme, tak och anslutning mot huset, med kontroll enligt planen."),
    ("Slutbesked", "Den nya delen används när slutbeskedet har kommit."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Sundbyberg",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Sundbyberg?",
  "price": [
    "Storlek och grundläggning, anpassning av tak, panel och fönster till ett äldre hus, eventuell kontrollansvarig, hänsyn till träd och rötter samt installationer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi göra en attefallstillbyggnad i Duvbo?",
     "Nej. Sundbybergs stad skriver att lättnaden för bygglovsbefriade tillbyggnader inte gäller i riksintresset Duvbo, så bygglov krävs."),
    ("Får tillbyggnaden ha platt tak i Duvbo?",
     "Miljöprogrammet skriver att tillbyggnader med plana tak inte hör hemma bland egnahemsbebyggelsen från 1900–1920-talen."),
    ("Måste vi ha kontrollansvarig för en tillbyggnad i Sundbyberg?",
     "Ofta ja, enligt staden. Vid enklare tillbyggnader som ett uterum kan en kontrollplan räcka."),
    ("Behövs marklov för att fälla en björk vid tillbyggnaden i Duvbo?",
     "Ja, om stammen är större än 20 centimeter i diameter på 1,3 meters höjd. Staden är restriktiv med sådana lov."),
    ("Vilka handlingar vill Sundbyberg ha för en tillbyggnad?",
     "Plan-, fasad- och sektionsritningar, en förenklad nybyggnadskarta, material- och kulörbeskrivning samt kontrollansvarig eller kontrollplan."),
  ],
  "sources": [("Sundbybergs stad – Tillbyggnad, bygglovsbefriad", "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/tillbyggnad---bygglovsbefriad"),
              ("Sundbybergs stad – Tillbyggnad av en- och tvåbostadshus", "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/tillbyggnad-av-en--och-tvabostadshus"),
              ("Sundbybergs stad – Trädfällning i Duvbo", "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/tradfallning-i-duvbo"),
              ("Sundbybergs stad – Miljöprogram Duvbo (pdf)", "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf"),
              _BV_TB, _SKV],
  "cta": ("Vill du bygga till ett hus i Duvbo eller Sundbyberg?", "Boka ett gratis platsbesök, så går vi igenom riktlinjerna och träden innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla i trä med en lägre tillbyggnad med sadeltak mot trädgården",
     "early 1900s Swedish two-storey wooden villa on a high stone plinth with ochre board cladding and red tile roof, with a lower new extension with matching panel and a pitched roof on the garden side, large old trees and fruit trees, summer daylight" + _SFX),
    ("Stora gamla träd och spjälstaket längs en villagata",
     "Swedish early 1900s villa street with large old deciduous trees dominating the street, simple white picket fences and leafy hedges, wooden villas behind, summer light" + _SFX),
    ("Gavel med nymålad gul träpanel och vita vindskivor",
     "close-up of a house corner where new painted wooden board cladding of an extension meets the older original panel of a villa, clear recess between them, same ochre colour, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ HÄSSELBY
"tillbyggnad-hasselby.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Hässelby", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Hässelby – från sommarstuga till villa",
  "description": "Tillbyggnad i Hässelby: villastadens hus som vuxit i omgångar, potten på 30 kvadratmeter, gränser och medgivanden, prickmark och anmälan i Stockholms stad.",
  "h1": "Tillbyggnad i Hässelby",
  "lead": "Många hus i Hässelby villastad har vuxit i omgångar – från en enkel stuga till en villa för hela året. Nästa tillbyggnad behöver därför räkna med det som redan har byggts. Geal Entreprenad AB mäter huset, går igenom reglerna och bygger till med total entreprenad.",
  "card": "Hus som vuxit i omgångar.",
  "sections": [
    {"id": "historien-hasselby", "anchor": "Villastaden",
     "h2": "En villastad som byggdes bit för bit",
     "paras": [
       "En skrift om Västra Smedshagen från Stockholmshem och KTH berättar hur några arbetare 1893 fick arrendera tomter på godsets mark för att bygga egna bostäder, och hur tomtförsäljningen sedan pågick utan någon egentlig styckningsplan – storlekar och lägen bestämdes allt eftersom. Hässelby blev municipalsamhälle 1914 med namnet Hässelby Villastad, och 1926 fastställdes en stadsplan. På 1920-talet byggdes också ett hundratal sommarstugor.",
       "Den historien syns i husen. Många villor har byggts till flera gånger, och tomterna är olika stora. Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver dessutom hur villor ersattes på 1960- och 1970-talen och hur tomter kring 600 kvadratmeter har tillkommit genom avstyckning.",
     ],
     "aside": {"title": "Hässelby villastad 2025", "items": [
       "7 029 bostäder", "5 009 i småhus", "4 757 med äganderätt"]}},
    {"id": "potten-hasselby", "h2": "Tidigare tillbyggnader räknas in",
     "paras": [
       "Stockholms stad skriver att en lovfri tillbyggnad får vara högst 30,0 kvadratmeter bruttoarea eller öppenarea, inte gå över husets taknock och tillsammans med andra lovfria tillbyggnader inte bli större än 30,0 kvadratmeter. Tidigare tillbyggnader som inte har krävt lov – till exempel friggebodsskärmtak, attefallstillbyggnader och attefallstakkupor – ska räknas in.",
       "På ett hus som redan har byggts ut utan lov kan potten alltså vara förbrukad. Vi går igenom gamla ritningar och vad som har byggts till innan vi föreslår något. Stadens äldre handlingar för fastigheten kan du själv ta fram via e-tjänsten Bygg- och plantjänsten.",
     ],
     "aside": {"title": "Räknas in i 30 m²", "items": [
       "Friggebodsskärmtak", "Attefallstillbyggnad", "Attefallstakkupor", "Den nya tillbyggnaden"]}},
    {"id": "granser-hasselby", "h2": "Gränser, prickmark och medgivanden",
     "paras": [
       "För en- och tvåbostadshus får en lovfri tillbyggnad strida mot detaljplanen, skriver staden, och den får till exempel placeras på prickmark. Den ska däremot stå 4,5 meter från gränsen mot granne, samfällighet och allmän plats, om inte berörda har gett ett skriftligt medgivande. Mot gatu- och parkmark är det oftast staden som ska ge medgivandet, och förfrågan skickas till stadsbyggnadskontoret.",
       "På de avstyckade tomterna i villastaden ligger husen ofta nära flera gränser. Medgivandet ska innehålla fastighetsbeteckning, vilken åtgärd det gäller, en situationsplan med avståndet inritat och grannarnas underskrifter. Tillbyggnaden ska också stå minst 30 meter från ett järnvägsspår om inte infrastrukturförvaltaren har godkänt annat.",
     ],
     "aside": None},
    {"id": "anmalan-hasselby", "h2": "Anmälan, kartan och utförandet",
     "paras": [
       "Påverkar tillbyggnaden husets bärande konstruktion eller brandskydd behövs en anmälan och ett startbesked, och det gäller också om tillbyggnaden får en eldstad eller vatten och avlopp. Ligger fastigheten i ett särskilt kulturhistoriskt värdefullt område, eller är huset blå- eller grönmarkerat i Stadsmuseets karta, krävs bygglov. Hässelby villastad är inte markerad i vägledningens tabell, men Hässelby strand och Hässelby gård är det.",
       "När ett äldre hus byggs till är anslutningen mellan nytt och gammalt det svåra: takfall som ska mötas, grunder på olika nivåer och fukt i övergången. Vi ritar detaljerna innan vi bygger, och vi tar reda på hur den befintliga grunden ser ut innan den nya grunden dimensioneras. Vill du hellre bygga ett fristående hus beskriver vi det under " + _L.format("attefallshus-hasselby.html", "attefallshus i Hässelby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi till ett hus i Hässelby",
  "steps": [
    ("Historiken", "Gamla ritningar och tidigare tillbyggnader gås igenom."),
    ("Platsbesök", "Huset, gränserna och marken mäts vid ett gratis besök."),
    ("Ritningar", "Förslag med anslutningsdetaljer mellan nytt och gammalt."),
    ("Lov eller anmälan", "Medgivanden, anmälan eller bygglov efter vad som krävs."),
    ("Bygget", "Grund, stomme, tak och öppning mot befintligt hus."),
    ("Slutbesked", "Den nya delen används när slutbeskedet har kommit."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Hässelby",
  "rot": [_ROT1, _ROT2],
  "price_h2": "Vad påverkar kostnaden för en tillbyggnad i Hässelby?",
  "price": [
    "Storlek och grundläggning, hur takfall och grund ska anslutas till ett hus som redan byggts till, om bärande väggar öppnas, våtrum och installationer samt om lov behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Räknas en gammal attefallstakkupa in när vi bygger till i Hässelby?",
     "Ja. Stockholms stad skriver att tidigare lovfria tillbyggnader, som attefallstakkupor och attefallstillbyggnader, ingår i de 30 kvadratmetrarna."),
    ("Får tillbyggnaden stå på prickmark i Hässelby villastad?",
     "För ett en- eller tvåbostadshus får en lovfri tillbyggnad strida mot detaljplanen, till exempel stå på prickmark. Gränsavståndet gäller ändå."),
    ("Var hittar vi gamla ritningar på vårt hus i Hässelby?",
     "Stadens äldre handlingar för fastigheten finns i e-tjänsten Bygg- och plantjänsten, där du själv kan ta fram och skriva ut dem."),
    ("Behöver vi bygglov för tillbyggnad i Hässelby strand?",
     "Hässelby strand står som kulturhistoriskt värdefull miljö i stadens vägledning. Ligger huset inom en grön eller blå ring i Stadsmuseets karta krävs bygglov."),
    ("Vem ger medgivande när tillbyggnaden hamnar nära gatan i Hässelby?",
     "För gatu- och parkmark är det oftast staden som är huvudman. Förfrågan skickas skriftligt till stadsbyggnadskontoret."),
  ],
  "sources": [("Stockholms stad – Tillbyggnad (bygglovsbefriad)", "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/tillbyggnad-bygglovsbefriad/"),
              ("Stockholmskällan / Stockholmshem – Västra Smedshagen, Hässelby Villastad (BOOM-gruppen KTH, 1996, pdf)",
               "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0006397_01_ocr.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hässelby villastad (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-villastad.pdf"),
              ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
               "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf"),
              _BV_TB, _SKV],
  "cta": ("Funderar du på att bygga till i Hässelby?", "Boka ett gratis platsbesök, så går vi igenom vad som redan är byggt innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Liten äldre trävilla som byggts ut i flera omgångar med en ny del mot trädgården",
     "small old Swedish wooden house that has been extended in several stages, original 1920s cottage part with gable roof and a newer larger wing, plus a new single-storey extension with large windows on the garden side, fruit trees and lawn, summer daylight" + _SFX),
    ("Två takfall som möts där en ny tillbyggnad ansluter till ett äldre hus",
     "roof detail where the gable roof of a new extension meets the older roof of a Swedish wooden villa, new flashing and gutter at the valley, red concrete tiles, blue sky, no workers" + _SFX),
    ("Villagata med hus av olika storlek och ålder bakom häckar",
     "Swedish suburban villa street with houses of different sizes and ages behind hedges and low fences, mature birch trees, summer daylight" + _SFX),
  ],
},
}
