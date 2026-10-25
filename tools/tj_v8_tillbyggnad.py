# -*- coding: utf-8 -*-
"""Tillbyggnad – ortsidor v8: Bromma, Täby, Lidingö, Nacka, Huddinge, Enskede (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
Riksdagen (PBL 2010:900 i lydelse från 1 december 2025: 9 kap. 9–10, 14, 34–35, 37 och 52 §§, 10 kap. 2 a §;
PBF 2011:338 6 kap. 1 §), Boverket (Göra en tillbyggnad, publicerad 4 juni 2026), Skatteverket (Ger arbetet rätt
till rotavdrag?: tillbyggnad av småhus ger rotavdrag om någon sida sitter ihop med befintlig yttervägg till minst
75 procent eller om det finns en dörr emellan; större delen av stommen ska behållas; bostaden äldre än fem år;
Så fungerar rotavdraget: 30 procent, högst 50 000 kr rot och 75 000 kr rot + rut), Stockholms stad (Tillbyggnad
(bygglovsbefriad), uppdaterad 2026-10-06; Varsam utveckling av småhus- och villaområden, godkänd 2021-06-16),
Stadsmuseet/Stockholmskällan (Ängbyplan i Stockholms spår; Gamla Enskede, byggnadsinventering 1974–1977),
Täby kommun (Tillbyggnad en- och tvåbostadshus; Kulturmiljöer i Täby, antagen), Lidingö stad (Ändrade lagar och
regler för byggande; Kulturmiljöprogram 2024; Frågor och svar om kulturmiljöprogrammet), Nacka kommun (Nya
PBL-regler ger mer frihet, 24 oktober 2025; Strandskydd; Strandskydd i Nacka; Kulturmiljöprogram: Villasamhällen
vid järnvägen), Huddinge kommun (Lovpliktig tillbyggnad; Förändringar i PBL; Kulturmiljöprogram del 2).
Strukna (ej verifierade): tomträttsavtalens nuvarande villkor för tillbyggnad i Enskede (bara 1908 års kontrakt
enligt Stadsmuseets inventering används, som historik), Stockholms stads underlag "Småstugor 1927–57" (hittades
inte), innehållet i Lidingös områdesbeskrivningar (pdf:erna gick inte att öppna – bara stadens webbsidor används),
hemfridszon i Nacka (ingen kommunkälla), Huddinges bygglovsavgifter (utelämnade), att tilläggsisolering alltid
kräver bygglov (Huddinges formulering är äldre än potten – utelämnad). Inga priser, garantier, omdömen, egna
uppdrag eller cert. Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 9 kap. 9–10, 14, 34–35 och 37 §§, 10 kap. 2 a §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_PBF = ("Riksdagen – Plan- och byggförordning (2011:338), 6 kap. 1 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-byggforordning-2011338_sfs-2011-338/")
_BV_TB = ("Boverket – Göra en tillbyggnad",
          "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/gora-en-tillbyggnad/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_STH_TB = ("Stockholms stad – Tillbyggnad (bygglovsbefriad)",
           "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/tillbyggnad-bygglovsbefriad/")
_STH_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
               "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"tillbyggnad-bromma.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Bromma", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Bromma – småstugor, trädgårdsstad, prickmark",
  "description": "Tillbyggnad i Bromma: lovfria 30 kvadratmeter, prickmark, Stadsmuseets karta och stadens råd för småstugorna i Norra Ängby och för trädgårdsstaden.",
  "h1": "Tillbyggnad i Bromma",
  "lead": "I Bromma handlar en tillbyggnad oftast om att ge ett litet hus mer plats utan att förstöra det som gör gatan fin. Småstugorna i Norra Ängby och Olovslund och villorna i trädgårdsstäderna ritades som enkla volymer, och staden har skrivit ner hur de kan byggas till. Geal Entreprenad AB utgår från Bromma, bygger till villor och småhus som total entreprenad och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Småstugor, trädgårdsstad och prickmark.",
  "sections": [
    {"id": "lovfritt-bromma", "anchor": "Lovfritt eller lov",
     "h2": "30 kvadratmeter utan lov – och vad som räknas in",
     "paras": [
       "Sedan den 1 december 2025 krävs inte bygglov för en tillbyggnad på högst 30,0 kvadratmeter bruttoarea eller öppenarea som inte går över husets taknock (PBL 9 kap. 10 §). Gränsen gäller sammanlagt. Stockholms stad påpekar att tidigare lovfria tillägg ska räknas in, till exempel ett friggebodsskärmtak, en attefallstillbyggnad eller attefallstakkupor.",
       "Staden räknar uterum, skärmtak, större takkupor och lågt sittande balkonger som tillbyggnader. Har huset redan fått en lovfri attefallstillbyggnad på 15 kvadratmeter återstår alltså bara hälften av potten.",
       "För en- och tvåbostadshus får en lovfri tillbyggnad strida mot detaljplanen. Staden ger som exempel att den får hamna på mark som inte får bebyggas, så kallad prickmark. Placeras den närmare gränsen än 4,5 meter behövs ändå ett skriftligt medgivande från de berörda grannarna – och för gatu- och parkmark är det oftast kommunen som ska ge det.",
     ],
     "aside": {"title": "Det här räknas in i potten", "items": [
       "Attefallstillbyggnad och attefallstakkupor", "Friggebodsskärmtak",
       "Altan, balkong eller burspråk", "Skärmtak och uterum"]}},
    {"id": "smastugor-bromma", "h2": "Småstugorna i Norra Ängby och Olovslund",
     "paras": [
       "Enligt Stadsmuseets text om Ängbyplan byggdes 1 200 småstugor i Norra Ängby 1931–38 genom självbyggeri under ledning av stadens fastighetskontor. Byggnadsdelarna tillverkades i element på fabrik, och de blivande ägarna bidrog med arbete motsvarande en tiondel av kostnaden. I stadens vägledning för småhusområden räknas också Olovslund, Bällsta och Eneby som småstugeområden.",
       "Vägledningen konstaterar att många av stugorna har byggts till under åren och att förändringarna främst har gjorts mot trädgårdssidan, vilket har bevarat områdenas karaktär. Det rekommenderade sättet är en tillbyggnad som underordnar sig huvudbyggnaden, där husets ursprungliga form fortfarande går att läsa ut.",
       "Ett av stadens exempel visar en tillbyggnad där nocken ligger lägre än huvudbyggnadens och takfoten på samma nivå. Det är en detalj vi ritar in redan i skissen, eftersom den styr både takets anslutning och hur huset upplevs från gatan.",
     ],
     "aside": {"title": "Stadens råd för småstugor", "items": [
       "Bygg mot trädgårdssidan", "Lägre nock än huvudbyggnaden",
       "Takfot i samma höjd", "Ursprungsformen ska kunna avläsas"]}},
    {"id": "riksintresse-bromma", "h2": "Riksintresse och Stadsmuseets klassificering",
     "paras": [
       "Olovslund, Ålstensgatan och Södra Ängby pekas i stadens vägledning ut som riksintressen för kulturmiljövården. Trädgårdsstäderna, bland dem Äppelviken, Smedslätten, Ålsten, Höglandet och Nockeby, beskrivs som kulturhistoriskt värdefulla miljöer.",
       "Lovbefrielsen gäller inte för en byggnad eller ett område som är särskilt värdefullt (PBL 9 kap. 37 §). Stockholms stad hänvisar till Stadsmuseets klassificeringskarta som en första indikation, men påminner om att alla byggnader och områden ännu inte är inventerade och att museet ibland behöver göra en bedömning.",
       "Därför börjar vi i Bromma med kartan och detaljplanen innan något ritas. Behövs lov tar vi fram underlaget, och behövs det inte vet du ändå att tillbyggnaden går att genomföra.",
     ],
     "aside": None},
    {"id": "tradgardsstad-bromma", "h2": "Trädgårdsstaden: in mot tomten och samma takform",
     "paras": [
       "För trädgårdsstäderna skriver staden att de öppna kvarteren med vyer över trädgårdarna är ett viktigt karaktärsdrag. Tillbyggnader, takkupor och terrasser bör i första hand göras mot trädgårdssidan och placeras så att siktlinjen från gatan in mot trädgårdarna hålls öppen.",
       "Utgångspunkten är de ursprungliga husens volym, proportioner och takformer. I Smedslätten och Ålsten är det ofta en och en halv våning med brant sadeltak i rött tegel, och en tillbyggnad som följer takvinkeln smälter in bättre än en som avviker. Hur den nya takdelen ansluter mot det gamla taket beskriver vi under " + _L.format("takbyte-bromma.html", "takbyte i Bromma") + ".",
       "Ska fasaden på resten av huset göras om samtidigt kan det vara klokt att samordna arbetena, se " + _L.format("fasadrenovering-bromma.html", "fasadrenovering i Bromma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad i Bromma",
  "steps": [
    ("Karta och detaljplan", "Vi kontrollerar Stadsmuseets klassificering, detaljplanen och vad som redan byggts lovfritt på huset."),
    ("Platsbesök", "Vi mäter upp huset, avstånd till gräns och takets höjder och går igenom dina önskemål."),
    ("Skiss mot trädgården", "Ett förslag som underordnar sig huvudbyggnaden och följer stadens vägledning."),
    ("Medgivande eller lov", "Grannarnas skriftliga medgivande, anmälan eller bygglov tas fram innan arbetet börjar."),
    ("Kostnadsförslag", "Ett skriftligt förslag med grund, stomme, tak och invändiga arbeten var för sig."),
    ("Bygge och genomgång", "Vi bygger, ansluter tak och fasad mot det gamla huset och går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Bromma",
  "rot": [
    "Skatteverket godkänner rotavdrag för tillbyggnad av ett småhus om någon av tillbyggnadens sidor sitter ihop med husets befintliga yttervägg till minst 75 procent, eller om det finns en dörr emellan. Större delen av den ursprungliga stommen ska behållas, och huset ska vara äldre än fem år.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Bromma?",
  "price": [
    "Tillbyggnadens storlek och grundläggning, hur taket ska anslutas mot ett befintligt tegeltak, om det behövs bygglov, anmälan eller grannmedgivanden, vilka installationer som ska dras in och hur mycket av det gamla huset som öppnas upp. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga till vår småstuga i Norra Ängby utan bygglov?",
     "Ofta ja, om tillbyggnaden tillsammans med tidigare lovfria tillägg håller sig inom 30 kvadratmeter och inte går över nocken. Är huset eller området särskilt värdefullt krävs bygglov, och det ger Stadsmuseets klassificeringskarta en första indikation på."),
    ("Får en lovfri tillbyggnad hamna på prickmark?",
     "För en- och tvåbostadshus ja. Stockholms stad skriver att en lovfri tillbyggnad får strida mot detaljplanen och till exempel placeras på mark som inte får bebyggas. Reglerna om avstånd till gräns gäller ändå."),
    ("Vem ger medgivande om tillbyggnaden hamnar nära gatan?",
     "För allmän platsmark, som gata och park, är kommunen oftast huvudman. Stockholms stad vill då ha en skriftlig förfrågan till stadsbyggnadskontoret innan något byggs."),
    ("Vilken sida av huset är bäst att bygga till på i en trädgårdsstad?",
     "Enligt stadens vägledning i första hand trädgårdssidan, så att gatubilden och vyn in mot trädgårdarna behålls."),
    ("Räknas vårt gamla skärmtak in i de 30 kvadratmetrarna?",
     "Ja. Tidigare lovfria tillbyggnader, som ett friggebodsskärmtak, ska räknas med när du räknar ut hur mycket som återstår utan bygglov."),
  ],
  "sources": [
    _STH_TB, _STH_VARSAM,
    ("Stadsmuseet/Stockholmskällan – Ängbyplan, Stockholms spår (pdf)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000106.pdf"),
    _PBL, _BV_TB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Vill ni bygga till huset i Bromma?", "Boka ett gratis platsbesök så går vi igenom tomten, potten och vad som gäller för ert hus."),
  "img": [
    ("Liten ljus trävilla med rött tegeltak och en lägre tillbyggnad mot trädgården i Bromma",
     "small 1930s Swedish one-and-a-half storey wooden cottage with light yellow vertical board siding and a steep red clay tile gable roof, with a newer lower single-storey extension on the garden side that has the same siding and a lower red tile roof, lawn and fruit trees, Norra Ängby Bromma Stockholm, summer daylight, empty scene, no people, no text"),
    ("Anslutning där en ny lägre takdel möter en äldre takfot på ett trähus",
     "side view of a small one-storey wooden house extension with a low red clay tile roof built against the gable wall of an older light painted wooden house with a steeper red clay tile roof, the lower roof ends below the eaves of the old house, simple black metal flashing along the wall joint, garden lawn, clear sky, correct roof geometry, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TÄBY
"tillbyggnad-taby.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Täby", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Täby – Byle, kyrkbyn och detaljplanens pott",
  "description": "Tillbyggnad i Täby: lovfria 30 kvadratmeter, när detaljplanen ändå kräver lov och kommunens råd för villorna i Byle, Täby kyrkby och Norra Viggbyholm.",
  "h1": "Tillbyggnad i Täby",
  "lead": "En tillbyggnad på upp till 30 kvadratmeter kan i dag göras utan bygglov, men i Täby är det värt att läsa detaljplanen först. Kommunen påpekar att vissa planer kräver lov även för det som annars är lovfritt, och i de äldre villastäderna finns råd om hur huset bör byggas till. Geal Entreprenad AB bygger till villor och radhus i Täby som total entreprenad och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Byle, kyrkbyn och detaljplanen.",
  "sections": [
    {"id": "potten-taby", "anchor": "Potten",
     "h2": "Den lovfria potten och detaljplanen i Täby",
     "paras": [
       "Täby kommun beskriver tre lägen då en tillbyggnad på ett en- eller tvåbostadshus behöver bygglov: när den inte ryms i den lovfria potten, när byggnaden är särskilt värdefull och när detaljplanen har utökad lovplikt. Kommunen skriver att det i vissa fall står i gällande detaljplan att en annars lovfri tillbyggnad kräver bygglov.",
       "Potten är högst 30,0 kvadratmeter bruttoarea eller öppenarea, sammanlagt för alla tillbyggnader som inte krävt lov, och tillbyggnaden får inte gå över taknocken (PBL 9 kap. 10 §). Boverket räknar upp vad som redan kan ha tagit av den: attefallstillbyggnad, attefallstakkupa, skärmtak, altan, balkong och burspråk.",
       "Vill du veta hur stor byggrätten är kan du enligt kommunen läsa detaljplanen för fastigheten. Är du osäker på kulturvärdena kan du boka ett rådgivningsmöte med en handläggare. Vi tar gärna med oss frågorna dit.",
     ],
     "aside": {"title": "Bygglov i Täby krävs när", "items": [
       "Potten på 30 m² är använd", "Byggnaden är särskilt värdefull",
       "Detaljplanen har utökad lovplikt", "Grannmedgivande saknas inom 4,5 m"]}},
    {"id": "byle-kyrkby", "h2": "Byle och Täby kyrkby – villastaden från 1907",
     "paras": [
       "Enligt Kulturmiljöer i Täby växte en villastad upp runt Täby kyrka med start vid järnvägsstationen, efter en avstyckningsplan från 1907. Byle byggdes enligt en stadsplan från samma år och planerades efter trädgårdsstadens ideal med stora tomter.",
       "Typiskt för villorna från det tidiga 1900-talet är branta, ofta brutna tak med tegel eller målad plåt, takkupor, förstukvistar, burspråk och glasverandor och fönster som ofta är spröjsade. Kommunens råd för området är att fasadmaterial och färg vid om- och tillbyggnader bör anpassas till det befintliga huset om det har kvar sin ursprungliga färgsättning, och att fönster bör utformas i trä som originalen.",
       "I underlaget visas en villa i Byle från 1909 där tillbyggnaden har fått samma färg, fasadmaterial och typ av fönster som det äldre huset och är underordnad huvudbyggnaden. Det är ett bra mått på vad som brukar fungera.",
     ],
     "aside": {"title": "Kännetecken i den äldre villastaden", "items": [
       "Branta eller brutna tak", "Takkupor och glasverandor",
       "Spröjsade träfönster", "Markerad sockel mot sluttningen"]}},
    {"id": "viggbyholm-taby", "h2": "Norra Viggbyholm: från sommarstugor till villor",
     "paras": [
       "Villorna på båda sidor om Roslagsbanan i Norra Viggbyholm har vuxit fram sedan början av 1900-talet. Kommunen beskriver att det först främst byggdes sommarstugor och att villabyggandet tog fart med byggnadsplanen på 1930-talet. I dag finns allt från jugend och 1920-talsklassicism till 1960-talets mörka tegel och kataloghus från senare årtionden.",
       "Här gäller samma råd: särskild vikt vid att anpassa tillbyggnader till platsens kulturvärden och att den ursprungliga färgsättningen får vara vägledande. På ett hus som började som sommarstuga är det ofta stommen och grunden som avgör hur tillbyggnaden kan göras, och det undersöker vi vid platsbesöket.",
     ],
     "aside": None},
    {"id": "mark-taby", "h2": "Sluttande tomter och kommunens generella råd",
     "paras": [
       "Kommunens generella riktlinjer för småhusområden säger att markarbeten som sprängning, fyllning och schaktning bör hållas nere, att tomterna bör präglas av den naturliga topografin och att omfattande terrasseringar ska undvikas. Inom kulturhistoriskt värdefulla områden bör tillbyggnader placeras mot trädgårdssidan och vara underordnade huvudbyggnaden.",
       "För tillbyggnaden innebär det att grunden ofta får anpassas till marken i stället för tvärtom, till exempel med en sockel som tar upp lutningen, som på en villa i Viggbyholm från 1931 som underlaget visar. Taket bör enligt riktlinjerna ha samma form, material och takfot som huset. Hur den nya takdelen läggs beskriver vi under " + _L.format("takbyte-taby.html", "takbyte i Täby") + ", och vill du ha hela projektet samlat, se " + _L.format("byggforetag-taby.html", "byggföretag i Täby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en tillbyggnad i Täby till",
  "steps": [
    ("Detaljplan och byggrätt", "Vi läser planen och tar reda på om den har utökad lovplikt och hur stor byggrätten är."),
    ("Potten", "Vi räknar ihop vad som redan byggts lovfritt på huset, som skärmtak och altan."),
    ("Platsbesök", "Huset, tomtens lutning, avstånd till gräns och anslutningen mot taket gås igenom."),
    ("Förslag och kostnad", "En skiss i samma uttryck som huset och ett skriftligt kostnadsförslag."),
    ("Lov eller anmälan", "Vid behov tas underlag till bygglov eller anmälan fram innan bygget börjar."),
    ("Bygge och avslut", "Grund, stomme, tak och fasad, och en genomgång när allt är klart."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Täby",
  "rot": [
    "En tillbyggnad på en villa eller ett radhus kan ge rotavdrag. Skatteverkets villkor är att en av tillbyggnadens sidor sitter ihop med husets yttervägg till minst 75 procent eller att det finns en dörr mellan delarna, att större delen av den gamla stommen behålls och att huset är äldre än fem år.",
    "Du får 30 procent av arbetskostnaden i avdrag, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Täby?",
  "price": [
    "Tomtens lutning och grundläggning, hur mycket mark som behöver förberedas, om tillbyggnaden ska ha samma takmaterial och fönstertyp som ett äldre hus, om bygglov eller anmälan krävs och vilka installationer som ska in. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan detaljplanen kräva bygglov för en tillbyggnad på under 30 kvadratmeter i Täby?",
     "Ja. Täby kommun skriver att det i vissa detaljplaner står att en annars lovfri tillbyggnad kräver bygglov. Läs planen för fastigheten innan något beställs."),
    ("Hur bör en tillbyggnad på en äldre villa i Byle se ut?",
     "Kommunens råd är att den anpassas i färg, fasadmaterial och fönster till det äldre huset och är underordnad huvudbyggnaden. Fönster bör vara av trä som originalen."),
    ("Får vi spränga för en tillbyggnad på en bergig tomt i Täby?",
     "Kommunens riktlinjer säger att sprängning, fyllning och schaktning bör minimeras och att tomterna bör behålla sin naturliga topografi. Grunden anpassas hellre till marken."),
    ("Var bokar man rådgivning om kulturvärden i Täby?",
     "Kommunen erbjuder rådgivningsmöten med handläggare om du är osäker på om din byggnad eller ditt område har höga kulturvärden."),
    ("Behöver en tillbyggnad i Täby anmälas fast den är lovfri?",
     "Ja, om den innebär ett väsentligt ingrepp i bärande konstruktion eller ventilation, om brandskyddet påverkas eller om en eldstad, rökkanal eller imkanal installeras."),
  ],
  "sources": [
    ("Täby kommun – Tillbyggnad en- och tvåbostadshus",
     "https://www.taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/tillbyggnad-en--och-tvabostadshus"),
    ("Täby kommun – Kulturmiljöer i Täby, antagen (pdf)",
     "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"),
    _PBL, _BV_TB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Funderar ni på att bygga till i Täby?", "Boka ett gratis platsbesök så går vi igenom detaljplanen, potten och tomten."),
  "img": [
    ("Äldre ljusgul trävilla med brant brutet tak och glasveranda bland lövträd i Täby",
     "early 1900s Swedish two-storey wooden villa with light yellow horizontal board siding, white window frames with glazing bars, steep mansard roof with red clay tiles and a dormer, a glazed veranda, large garden with birch and oak trees, Byle Täby, summer, empty scene, no people, no text"),
    ("Ny träsockel och grund för en tillbyggnad på en sluttande villatomt",
     "new concrete foundation and wooden floor framing for a small house extension being built against the side of an existing wooden villa on a gently sloping lawn, stacked timber nearby, natural stone visible in the ground, overcast daylight, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ LIDINGÖ
"tillbyggnad-lidingo.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Lidingö", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad på Lidingö – kartan och kulturmiljöprogrammet",
  "description": "Tillbyggnad på Lidingö: 30 kvadratmeter utan bygglov, stadens webbkarta med utökad lovplikt, kulturmiljöprogrammet från 2024 och frivilligt bygglov.",
  "h1": "Tillbyggnad på Lidingö",
  "lead": "På Lidingö avgörs frågan om bygglov för en tillbyggnad ofta av ett blått lager i stadens webbkarta. Där syns de områden och fastigheter som har utökad lovplikt, och de särskilt värdefulla miljöerna beskrivs i stadens kulturmiljöprogram från 2024. Geal Entreprenad AB bygger till villor och radhus på Lidingö som total entreprenad och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Webbkartan, programmet och frivilligt lov.",
  "sections": [
    {"id": "kartan-lidingo", "anchor": "Webbkartan",
     "h2": "Det blå lagret i stadens webbkarta",
     "paras": [
       "Lidingö stad skriver att utökad lovplikt gäller för de flesta byggnadsåtgärder inom områden som är särskilt kulturhistoriskt värdefulla, och att bygglov då krävs för bland annat nybyggnad, tillbyggnad och fasadändring. Om din fastighet berörs ser du i stadens webbkarta: sök på adress eller fastighetsbeteckning, så visas ett blått lager över de områden och fastigheter som har utökad lovplikt.",
       "Är fastigheten i stället gulmarkerad kan det finnas värden som behöver bedömas, och då ber staden dig kontakta kundcenter för vägledning. Utanför de markerade områdena kan en tillbyggnad på upp till 30 kvadratmeter göras utan bygglov.",
       "Stadens svar på vanliga frågor gör en viktig poäng: inom de utpekade kulturmiljöerna gäller samma regler för alla fastigheter när det gäller de lovfria åtgärderna, även om just ditt hus inte är särskilt värdefullt. Det är alltså området som avgör, inte bara huset.",
     ],
     "aside": {"title": "Så läser du kartan", "items": [
       "Blått: utökad lovplikt", "Gult: värden som kan behöva bedömas",
       "Omarkerat: lovfria regler gäller", "Osäker? Kontakta kundcenter"]}},
    {"id": "program-lidingo", "h2": "Kulturmiljöprogrammet från december 2024",
     "paras": [
       "Kommunfullmäktige antog det nya kulturmiljöprogrammet den 16 december 2024. Det ersatte programmet från 1990, efter att hela Lidingö inventerats. Vissa kvarter som förlorat sina värden togs bort och nya områden lades till. Programmet har två delar: en handbok för fastighetsägare och en bebyggelsehistorisk beskrivning av de särskilt värdefulla områdena, med råd och riktlinjer för varje område.",
       "Bland de utpekade miljöerna finns villastäder som Lidingö villastad, Herseruds villastad och Breviks villastad, men också radhusområden som Mölna radhusby och kolonierna i Dalakolonin och Grönstakolonin. Lidingö har dessutom nio byggnadsminnen, däribland radhusen på Canadastigen, som skyddas enligt kulturmiljölagen och där länsstyrelsen hanterar tillstånd för ändringar.",
       "Staden påpekar att programmet är ett kunskapsunderlag och inte juridiskt bindande, och att det inte påverkar byggrätten enligt detaljplanen. Men det används som stöd när bygglov prövas, så det är de råden vi utgår från när en tillbyggnad ritas i ett utpekat område.",
     ],
     "aside": None},
    {"id": "detaljplan-lidingo", "h2": "Detaljplanens q, k och r",
     "paras": [
       "Om ett hus inte finns med i kulturmiljöprogrammet men omfattas av en detaljplan med skydd av kulturvärden eller rivningsförbud är det enligt staden ändå särskilt kulturhistoriskt värdefullt, eftersom frågan redan är avgjord i planen. I dagens planer används främst tre beteckningar: q för skydd av kulturvärden, k för byggnadens karaktärsdrag och r för rivningsförbud. Äldre planer kan ha andra beteckningar.",
       "I övrigt får de flesta lovfria åtgärder på en- och tvåbostadshus göras även om de strider mot detaljplanen, och staden nämner tillbyggnad som exempel. Staden har också äldre inventeringar av enskilda byggnader från 1970- och 1980-talen och från 2013–2015, som du kan be kundcenter om att få ta del av.",
     ],
     "aside": {"title": "Före ritningen", "items": [
       "Sök fastigheten i webbkartan", "Läs detaljplanen – q, k eller r?",
       "Be om äldre inventeringar", "Läs råden för ditt område"]}},
    {"id": "frivilligt-lidingo", "h2": "Frivilligt bygglov som trygghet",
     "paras": [
       "För åtgärder som normalt inte kräver bygglov kan du på Lidingö ansöka om ett frivilligt bygglov (PBL 9 kap. 52 §). Staden beskriver det som ett beslut som ger dig som byggherre trygghet i att åtgärden uppfyller lagens krav. Det kan vara värt det när tillbyggnaden ligger nära gränsen för potten eller i utkanten av ett utpekat område.",
       "Även lovfritt ska utföras varsamt med hänsyn till husets och områdets karaktär, och en anmälan krävs om ventilation, brandskydd, bärande konstruktion eller vatten och avlopp ändras. Hur den nya takdelen ansluts mot den gamla läser du om under " + _L.format("takrenovering-lidingo.html", "takrenovering på Lidingö") + ", och samordning av hela projektet beskriver vi under " + _L.format("byggforetag-lidingo.html", "byggföretag på Lidingö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad på Lidingö",
  "steps": [
    ("Webbkartan", "Vi söker fram fastigheten och ser om det blå eller gula lagret berör den."),
    ("Plan och program", "Detaljplanens bestämmelser och kulturmiljöprogrammets råd för området läses."),
    ("Platsbesök", "Huset, tomten och takets höjder mäts upp och dina önskemål gås igenom."),
    ("Förslag", "En skiss som passar huset och ett skriftligt kostnadsförslag med delarna var för sig."),
    ("Lov, frivilligt lov eller anmälan", "Det underlag som krävs tas fram innan bygget börjar."),
    ("Bygge och genomgång", "Tillbyggnaden byggs och ansluts tätt mot huset, och vi går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad på Lidingö",
  "rot": [
    "Skatteverket ger rotavdrag för tillbyggnad av ett småhus när tillbyggnaden sitter ihop med husets befintliga yttervägg till minst 75 procent av en sida, eller när det finns en dörr emellan. Huset ska vara äldre än fem år och större delen av stommen ska vara kvar.",
    "Avdraget är 30 procent av arbetskostnaden, upp till 50 000 kr per person och år. Material, resor och utrustning räknas inte. Geal drar av det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden på Lidingö?",
  "price": [
    "Om bygglov eller frivilligt bygglov ska sökas, vilka material och detaljer kulturmiljöprogrammet pekar på, tomtens terräng och grund, hur tillbyggnaden ansluts mot tak och fasad och vilka installationer som ska in. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad betyder blå och gul markering i Lidingö stads webbkarta?",
     "Blått lager betyder utökad lovplikt, och då krävs bygglov även för en tillbyggnad som annars hade varit lovfri. Gul markering betyder att det kan finnas värden som staden behöver bedöma – kontakta kundcenter innan ni ritar. Sök på adressen eller fastighetsbeteckningen."),
    ("Mitt hus är inte värdefullt men ligger i ett utpekat område – gäller lovplikten ändå?",
     "Ja. Lidingö stad skriver att samma regler för de lovfria åtgärderna gäller för alla fastigheter inom de utpekade kulturmiljöerna."),
    ("Är kulturmiljöprogrammet på Lidingö bindande?",
     "Nej, det är ett kunskapsunderlag. Det påverkar inte byggrätten i detaljplanen men används som stöd när bygglov prövas."),
    ("Vad ger ett frivilligt bygglov för tillbyggnaden?",
     "Ett beslut från staden om att åtgärden uppfyller lagens krav, även om den hade kunnat göras utan lov. Det ger trygghet om det finns osäkerhet om reglerna."),
    ("Kan vi få se äldre inventeringar av vårt hus på Lidingö?",
     "Staden har inventeringar av enskilda byggnader från 1970- och 1980-talen och från 2013–2015. Kontakta kundcenter på miljö- och stadsbyggnadskontoret."),
  ],
  "sources": [
    ("Lidingö stad – Ändrade lagar och regler för byggande",
     "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/"),
    ("Lidingö stad – Kulturmiljöprogram",
     "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/"),
    ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet",
     "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/"),
    _PBL, _BV_TB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Vill ni bygga till på Lidingö?", "Boka ett gratis platsbesök så går vi igenom kartan, programmet och huset."),
  "img": [
    ("Vitputsad villa från 1920-talet med valmat tegeltak och en nyare tillbyggnad i trä mot trädgården bland tallar",
     "1920s Swedish white plastered villa with a hipped red clay tile roof, and a newer single-storey extension in dark painted wood with large windows on the garden side, tall pine trees and granite outcrops, Lidingö Stockholm, late summer daylight, empty scene, no people, no text"),
    ("Nyrest stomme till en tillbyggnad intill en äldre putsad villa",
     "small single-storey timber frame of a house extension under construction, open wooden studs and a few roof rafters, built against the side wall of a finished older white plastered 1920s villa with a red clay tile hipped roof, the old villa is complete and intact, pine trees, daylight, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ NACKA
"tillbyggnad-nacka.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Nacka", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Nacka – strandskydd, Storängen, Saltsjöbaden",
  "description": "Tillbyggnad i Nacka: lovfritt upp till 30 kvadratmeter, när strandskyddet kräver dispens och råden för villasamhällena vid Saltsjöbanan.",
  "h1": "Tillbyggnad i Nacka",
  "lead": "I Nacka ligger många villor nära vatten, och då räcker det inte att fråga om bygglov. Strandskyddet är en egen prövning, och kommunen påminner om att dispens kan behövas även när bygglov inte gör det. I villasamhällena längs Saltsjöbanan finns dessutom råd för hur husen ska byggas till. Geal Entreprenad AB bygger till villor i Nacka som total entreprenad och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Strandskydd och villasamhällen.",
  "sections": [
    {"id": "strandskydd-nacka", "anchor": "Strandskyddet",
     "h2": "Strandskyddet – en egen prövning",
     "paras": [
       "Strandskyddet gäller normalt 100 meter från strandkanten, både på land och i vattnet, vid hav, sjöar och vattendrag. I Nacka har det utökats till 300 meter i flera delar av kommunen, bland annat Velamsund, södra delen av Järlasjö, Nyckelviken, delar av Insjön och Kil.",
       "Inom strandskyddat område är det förbjudet att uppföra nya byggnader och att ändra byggnader eller sätta upp anordningar som avhåller allmänheten från att röra sig där. Kommunen skriver att bygglov och strandskyddsdispens är två skilda saker: även om du har fått bygglov kan dispens behövas, och tvärtom. Även när bygglov inte krävs behövs dispens, till exempel för en altan.",
       "För att få dispens krävs ett särskilt skäl enligt 7 kap. 18 c–d § miljöbalken, till exempel att platsen redan är ianspråktagen så att den saknar betydelse för strandskyddets syften. Kommunen påpekar också att strandskyddet återinträder om en detaljplan där det varit upphävt ersätts av en ny plan.",
     ],
     "aside": {"title": "Vid vatten i Nacka", "items": [
       "100 meter, på vissa håll 300", "Bygglov och dispens prövas var för sig",
       "Dispens kräver särskilt skäl", "Brott att bygga utan dispens"]}},
    {"id": "ansokan-nacka", "h2": "Ritningar till en dispensansökan",
     "paras": [
       "Enligt kommunens checklista ska en situationsplan med tydliga mått och total area bifogas till varje ansökan om dispens. Ska du bygga eller bygga om en byggnad ska du också bifoga fasadritningar, helst i skala 1:100, och planritningar som är fackmässigt utförda. Kommunen har ett exempeldokument just för tillbyggnad av enbostadshus.",
       "Miljöenheten och bygglovenheten samordnar sina beslut, och kommunen råder dig att kontakta bygglovenheten samtidigt som du söker dispens. Det är brottsligt att utföra en åtgärd som kräver dispens utan att ha fått den. Vi tar därför fram ritningarna så att de räcker till båda prövningarna.",
     ],
     "aside": None},
    {"id": "villasamhallen-nacka", "h2": "Storängen, Saltsjöbaden och Tattby",
     "paras": [
       "Kulturmiljöprogrammet Villasamhällen vid järnvägen beskriver hur villasamhällen växte fram längs Saltsjöbanan från 1890-talet. Storängen grundades 1904 på enskilt initiativ och är riksintresse för kulturmiljövården. Föreningens byggnadsordning bestämde att villorna inte fick vara högre än två våningar, att avståndet till tomtgräns inte fick vara under sex meter och att grundytan fick vara högst en tiondel av tomten. Den vanliga tomtstorleken var 1 000–1 500 kvadratmeter, men många köpte två eller tre tomter.",
       "För Storängen, Saltsjöbaden och Tattby ger programmet samma förhållningssätt: tillbyggnader ska underordnas huvudbyggnaden och få en placering, höjd, volym och utformning som anpassas till husets karaktär. Takkupor, terrasser, balkonger och altaner görs helst mot baksidan, och omfattande utfyllnader, stödmurar och hårdgjorda ytor undviks.",
       "Programmet skriver också att möjligheten att bygga till beror på den enskilda byggnadens karaktär, dess roll i gatumiljön och dess arkitekturhistoriska värde, och att antikvarisk medverkan kan krävas inför bygglovsprövningen.",
     ],
     "aside": {"title": "Programmets råd", "items": [
       "Underordna tillbyggnaden", "Altaner och kupor mot baksidan",
       "Undvik stödmurar och utfyllnad", "Antikvarie kan behövas"]}},
    {"id": "lov-nacka", "h2": "Lovfritt utanför kulturmiljöerna",
     "paras": [
       "Utanför de särskilt värdefulla områdena kan mindre tillbyggnader oftast göras utan bygglov, skriver Nacka kommun, men krav på anmälan kan finnas kvar. Gränsen är 30 kvadratmeter sammanlagt, under taknocken, och 4,5 meter från gränsen om inte grannarna skriftligen har gått med på placeringen.",
       "Inom ett område som är särskilt värdefullt enligt 8 kap. 13 § PBL ökar lovplikten. Kommunen hänvisar till kulturmiljölagret i webbkartan men påpekar att kartan håller på att uppdateras och inte är helt korrekt överallt. Är du osäker är det Stadsbyggnadsservice som kan svara. Hur den nya takdelen läggs mot det gamla taket beskriver vi under " + _L.format("takrenovering-nacka.html", "takrenovering i Nacka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad i Nacka",
  "steps": [
    ("Strandskydd och plan", "Vi kontrollerar strandskyddet, detaljplanen och kulturmiljölagret i webbkartan."),
    ("Platsbesök", "Huset, berget, avstånd till strand och gräns och takets höjder mäts upp."),
    ("Ritningar", "Situationsplan, fasader och planer som håller för både dispens och bygglov."),
    ("Prövningar", "Dispens, bygglov eller anmälan söks i rätt ordning innan bygget börjar."),
    ("Kostnadsförslag", "Ett skriftligt förslag där grund, stomme, tak och installationer står var för sig."),
    ("Bygge och avslut", "Vi bygger med så lite markingrepp som möjligt och går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Nacka",
  "rot": [
    "Rotavdrag ges för tillbyggnad av ett småhus, enligt Skatteverket, om någon sida av tillbyggnaden sitter ihop med befintlig yttervägg till minst 75 procent eller om det finns en dörr emellan. Skatteverket godkänner också sprängarbete som krävs för en utbyggnad. Huset ska vara äldre än fem år.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och vi gör det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Nacka?",
  "price": [
    "Berg och grundläggning, om strandskyddsdispens eller bygglov behöver sökas, om antikvarisk medverkan krävs, hur tillbyggnaden ansluts mot ett äldre tak och vilka installationer som ska in. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi strandskyddsdispens för en lovfri tillbyggnad i Nacka?",
     "Det kan behövas. Nacka kommun skriver att bygglov och dispens är skilda prövningar och att dispens kan krävas även när bygglov inte gör det."),
    ("Hur långt från vattnet gäller strandskyddet i Nacka?",
     "Normalt 100 meter, men i flera delar av kommunen, bland annat Velamsund, Nyckelviken och Kil, har det utökats till 300 meter."),
    ("Vilka ritningar behövs för att söka dispens för en tillbyggnad?",
     "En situationsplan med mått och area samt fackmässigt utförda fasadritningar, helst i skala 1:100, och planritningar."),
    ("Får vi bygga en altan mot gatan på vår villa i Storängen?",
     "Kulturmiljöprogrammet råder att altaner, terrasser och takkupor helst görs mot baksidan och att tillbyggnader underordnas huvudbyggnaden."),
    ("Stämmer kulturmiljölagret i Nackas webbkarta?",
     "Kommunen skriver att kartan håller på att uppdateras och att lagret inte ligger helt korrekt överallt. Kontakta Stadsbyggnadsservice om du är osäker."),
  ],
  "sources": [
    ("Nacka kommun – Strandskydd",
     "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/jag-vill-gora-ansokan-eller-anmalan/sok-bygglov/strandskydd/"),
    ("Nacka kommun – Strandskydd i Nacka",
     "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/strandskyddsdispens/strandskydd-i-nacka/"),
    ("Nacka kommun – Strandskyddsdispens",
     "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/strandskyddsdispens/"),
    ("Nacka kommun – Nya PBL-regler ger mer frihet och större ansvar för Nackas fastighetsägare",
     "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/nyheter-om-nya-lagandringen/2025/10/nya-pbl-regler-ger-mer-frihet-och-storre-ansvar-for-nackas-fastighetsagare/"),
    ("Nacka kommun – Kulturmiljöprogram: Villasamhällen vid järnvägen (pdf)",
     "https://www.nacka.se/499626/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-jarnvagen.pdf"),
    _PBL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Vill ni bygga till i Nacka?", "Boka ett gratis platsbesök så går vi igenom strandskyddet, planen och huset."),
  "img": [
    ("Sekelskiftesvilla i trä med glasveranda och en lägre tillbyggnad på baksidan på en bergig tomt i Nacka",
     "early 1900s Swedish two-storey wooden villa painted pale green with ornate gables and a glazed veranda, a lower newer single-storey extension at the back with matching siding, granite rock and pine trees on the plot, glimpse of a calm inlet, Saltsjöbaden Nacka, summer daylight, empty scene, no people, no text"),
    ("Grund för en tillbyggnad gjuten mot berg på en villatomt",
     "close-up of a new concrete plinth foundation for a small house extension cast directly against smooth granite bedrock on a residential plot, wooden formwork partly removed, pine needles on the rock, daylight, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HUDDINGE
"tillbyggnad-huddinge.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Huddinge", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Huddinge – egnahem, folkhem och 70-talsvillor",
  "description": "Tillbyggnad i Huddinge: kommunens råd för egnahem, folkhemsvillor och rekordårens hus, lovfria 30 kvadratmeter och handlingarna till bygglov.",
  "h1": "Tillbyggnad i Huddinge",
  "lead": "Huddinge kommun har gett råd för tillbyggnader i småhusområden från tre epoker, och råden gäller även områden som inte är utpekade som kulturmiljö. Ett egnahem från 1920-talet byggs till på ett annat sätt än en kedjehuslänga från 1970-talet. Geal Entreprenad AB bygger till villor och radhus i Huddinge som total entreprenad och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Råd för tre epoker av småhus.",
  "sections": [
    {"id": "epoker-huddinge", "anchor": "Tre epoker",
     "h2": "Råd som gäller alla småhusområden i Huddinge",
     "paras": [
       "Huddinges kulturmiljöprogram delar in småhusen i egnahemsområden från 1910–1940-talen, folkhemsbygget från 1940–1960-talen och rekordårens småhusbebyggelse från 1960–1980-talen. För varje epok finns råd, och programmet skriver uttryckligen att de kan tillämpas på alla småhusområden från perioden i kommunen, även de som inte ingår i ett utpekat kulturmiljöområde.",
       "Programmet påminner också om att all bebyggelse omfattas av varsamhetskraven i plan- och bygglagen. Det betyder att en tillbyggnad som inte kräver lov ändå ska anpassas till huset, och det är de här råden kommunen hänvisar till på sin sida om tillbyggnad, tillsammans med arkitekturstrategin.",
       "Programmet beskriver också hur 1970-talets villor byggdes större och med högre standard än egnahemsrörelsens enkla småhus, och hur arkitektritade villor med portar och fönster i teak och stora glasade partier blev vanligare. Från 1980-talet fick de äldre egnahemsområdena nya tillägg när större tomter styckades av för nya villor. Vilken av de här historierna ditt hus hör till avgör vilka material och proportioner tillbyggnaden bör ha.",
     ],
     "aside": {"title": "Epokerna i programmet", "items": [
       "Egnahem 1910–1940-tal", "Folkhemsbygget 1940–1960-tal",
       "Rekordåren 1960–1980-tal", "Råden gäller även utanför utpekade områden"]}},
    {"id": "egnahem-huddinge", "h2": "Egnahemmen: underordnad volym och lite markarbete",
     "paras": [
       "Egnahemsområdena har smala gator som följer terrängen, stora tomter och villor som ligger en bit in från vägen med förgårdsmark, fruktträd och buskar mot gatan. Programmet visar bland annat egnahemshus från 1920-talet längs Byalagsvägen. Villorna har träpanel, enkelt spröjsade fönster och tegeltäckta sadeltak eller brutna tak.",
       "Råden för tillbyggnad är att husens ursprungliga uttryck ska vara vägledande, att tillbyggnaden ska underordna sig den ursprungliga volymen och att sprängning, fyllning och schaktning hålls nere. Programmet anger också att kvarterens mitt, bakom den befintliga bebyggelsen, är mindre känslig för tillägg.",
     ],
     "aside": None},
    {"id": "folkhem-rekord", "h2": "Folkhemsvillor och kedjehus: inte mot gatan",
     "paras": [
       "Folkhemsbyggets områden består av små, enhetliga villor och kedje- eller radhus, med tomter som ofta skärmas av mot gatan med låg häck, staket eller mur. Programmet visar villor i Fullersta från 1940-talet och i Fridhem från 1950-talet. Råden är att undvika tillbyggnader mot gatan, att undvika större skärmtak och inglasade uteplatser mot gatan och att inte bygga stora altandäck med höga stödmurar på kuperade tomter.",
       "För rekordårens villor, ofta i grupphusområden med upprepade volymer, gäller liknande: större skärmtak, tillbyggnader och burspråk bör undvikas mot gaturummet. Programmet nämner radhusen från 1960-talet i Jacobslund och de senare radhusområdena i Sörskogen och Utsälje som exempel på epoken. I en sammanhållen länga ritar vi därför tillbyggnaden mot trädgården och i husens eget formspråk.",
     ],
     "aside": {"title": "Undvik mot gatan", "items": [
       "Tillbyggnader och burspråk", "Större skärmtak",
       "Inglasade uteplatser", "Höga stödmurar och stora altandäck"]}},
    {"id": "bygglov-huddinge", "h2": "När potten inte räcker: handlingarna till bygglov",
     "paras": [
       "En tillbyggnad på högst 30 kvadratmeter sammanlagt som inte går över nocken kräver inte bygglov, men Huddinge kommun påpekar att lovbefrielsen ofta inte gäller i områden med riksintressen och kulturhistoriskt värdefulla miljöer. Behövs bygglov vill kommunen normalt ha situationsplan på förenklad nybyggnadskarta, fasadritning med marklinjer, planritning och sektionsritning.",
       "Kommunen skriver att konstruktionsritningar kan behövas vid mer komplicerade tillbyggnader men inte vid en enkel, och att en liten enkel tillbyggnad inte kräver kontrollansvarig. Det du bygger behöver inte ha väggar för att räknas som tillbyggnad – skärmtak, uterum, takkupor och balkonger räknas också. Hur taket på tillbyggnaden ansluts beskriver vi under " + _L.format("takbyte-huddinge.html", "takbyte i Huddinge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad i Huddinge",
  "steps": [
    ("Epok och plan", "Vi tar reda på vilken epok huset hör till, vad detaljplanen säger och om området är utpekat."),
    ("Platsbesök", "Huset, tomten, förgårdsmarken och takets höjder mäts upp."),
    ("Skiss", "En tillbyggnad som följer programmets råd och underordnar sig huset."),
    ("Handlingar", "Situationsplan, fasad-, plan- och sektionsritningar när lov eller anmälan krävs."),
    ("Kostnadsförslag", "Ett skriftligt förslag med grund, stomme, tak och invändiga arbeten var för sig."),
    ("Bygge och avslut", "Vi bygger, ansluter mot det gamla huset och går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Huddinge",
  "rot": [
    "Tillbyggnad av en villa, ett radhus eller ett kedjehus kan ge rotavdrag. Skatteverket kräver att någon av tillbyggnadens sidor sitter ihop med befintlig yttervägg till minst 75 procent eller att det finns en dörr emellan, och att huset har passerat sina första fem år.",
    "Avdraget är 30 procent av arbetskostnaden och högst 50 000 kr per person och år. Geal drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Huddinge?",
  "price": [
    "Tomtens terräng och grund, om bygglov och ritningar krävs, hur tillbyggnaden anpassas till husets epok och material, anslutningen mot det befintliga taket och vilka installationer som ska in. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Gäller kulturmiljöprogrammets råd om vårt villaområde i Huddinge inte är utpekat?",
     "Ja. Programmet skriver att råden för respektive epok kan tillämpas på alla småhusområden från perioden i kommunen, även de som inte ingår i ett utpekat område."),
    ("Kan vi bygga ett uterum mot gatan på vårt 50-talshus i Huddinge?",
     "Programmet råder att undvika större skärmtak och inglasade uteplatser mot gatan i folkhemsbyggets områden. Trädgårdssidan är det bättre valet."),
    ("Behövs kontrollansvarig för en liten tillbyggnad i Huddinge?",
     "Inte för en liten enkel tillbyggnad, enligt kommunen. Om du är osäker kan du skicka in ansökan utan, så återkommer kommunen om det behövs."),
    ("Vilka ritningar vill Huddinge kommun ha för bygglov för tillbyggnad?",
     "Normalt situationsplan på förenklad nybyggnadskarta, fasadritning med marklinjer, planritning och sektionsritning, och ibland konstruktionsritning."),
    ("Räknas ett skärmtak som tillbyggnad?",
     "Ja. Huddinge kommun skriver att det du bygger inte behöver ha väggar för att räknas som tillbyggnad, och nämner skärmtak, uterum, takkupor och balkonger."),
  ],
  "sources": [
    ("Huddinge kommun – Lovpliktig tillbyggnad",
     "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/tillbyggnad"),
    ("Huddinge kommun – Förändringar i byggregler samt plan- och bygglagen",
     "https://www.huddinge.se/bostad-och-miljo/bygglov/forandringar-i-pbl"),
    ("Huddinge kommun – Kulturmiljöprogram del 2 (pdf)",
     "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf"),
    _PBL, _BV_TB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Funderar ni på att bygga till i Huddinge?", "Boka ett gratis platsbesök så går vi igenom huset, epoken och reglerna."),
  "img": [
    ("Egnahem från 1920-talet med tegeltak och en mindre tillbyggnad mot trädgården i Huddinge",
     "1920s Swedish wooden owner-built house with light grey horizontal board siding, white window frames, red clay tile gable roof, and a small newer single-storey extension towards the back garden with matching siding, old apple trees and a picket fence, Huddinge, spring daylight, empty scene, no people, no text"),
    ("Rad med kedjehus från 1970-talet med lika fasader mot gatan",
     "row of 1970s Swedish one-and-a-half storey linked houses (kedjehus) with dark brown stained wooden panel facades, identical gable roofs with dark concrete tiles, each house joined to the next by a carport, small front lawns, quiet residential cul-de-sac with birch trees, Stockholm suburb, overcast daylight, empty street, no people, no cars, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ENSKEDE
"tillbyggnad-enskede.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Enskede", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Enskede – små tomträttstomter och riksintresse",
  "description": "Tillbyggnad i Enskede: 1908 års tomträttskontrakt, riksintresset Gamla Enskede, stadens råd för trädgårdsstad och småstugor och vad som är lovfritt i dag.",
  "h1": "Tillbyggnad i Enskede",
  "lead": "Gamla Enskede byggdes på små tomter som staden upplät med tomträtt, och redan 1908 skulle ritningar för en större ombyggnad godkännas av staden. I dag är det plan- och bygglagen och riksintresset som sätter ramarna, men tomternas storlek är densamma. Geal Entreprenad AB bygger till hus i Enskede som total entreprenad och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Små tomter och riksintresse.",
  "sections": [
    {"id": "kontraktet-enskede", "anchor": "1908 års regler",
     "h2": "Tomträttskontraktet som styrde husen",
     "paras": [
       "Enligt Stadsmuseets byggnadsinventering av Gamla Enskede innehöll tomträttskontraktet, som gällde i 60 år, bestämmelser om hur tomten fick bebyggas. Byggnadsrätten angavs i kontraktet, tomten fick bara användas för bostadsändamål och uthus fick inte uppföras. Boningshuset skulle ligga minst tre meter från gatulinjen.",
       "Kontraktet krävde också att ritning och arbetsbeskrivning för nybyggnad och större ombyggnad skulle godkännas av staden, och att träd inte fick fällas utan stadens medgivande. Byggandet började sommaren 1908, och enligt inventeringen var större delen av det första stadsplaneområdet färdigbyggt 1913.",
       "Inventeringen från 1970-talet konstaterade att de små tomterna, upplåtna med tomträtt, inte gav något utrymme för ny bebyggelse. Är ditt hus upplåtet med tomträtt i dag är det därför klokt att läsa avtalet innan en tillbyggnad ritas.",
     ],
     "aside": {"title": "Ur 1908 års kontrakt", "items": [
       "Byggnadsrätten angavs i kontraktet", "Inga uthus på tomten",
       "Minst tre meter till gatulinjen", "Ritningar godkändes av staden"]}},
    {"id": "riksintresse-enskede", "h2": "Gamla Enskede är riksintresse",
     "paras": [
       "Stockholms stads vägledning för småhusområden pekar ut Gamla Enskede som riksintresse för kulturmiljövården, tillsammans med bland annat Pungpinan och Olovslund. Staden skriver att det därmed är av nationellt intresse att bevara området och att det har ett starkt lagskydd. Gamla Enskede var stadens första trädgårdsstad, anlagd efter Per Olof Hallmans stadsplan från 1908, och den mest kända typritningen är den så kallade Enskedestugan.",
       "En lovfri tillbyggnad gäller inte för särskilt värdefulla byggnader och områden (PBL 9 kap. 37 §). Stockholms stad hänvisar till Stadsmuseets klassificeringskarta för en första indikation, och ibland behöver museet göra en bedömning. I Gamla Enskede ska du alltså räkna med att bygglov kan krävas även för en liten tillbyggnad.",
       "Huvuddelen av husen i trädgårdsstäderna var enligt vägledningen friliggande enfamiljshus i ett plan med delvis inredd vind, men även radhus och parhus förekom. I ett parhus delar två ägare på samma huskropp, och en tillbyggnad på ena halvan syns på hela huset. Det är ett skäl att prata med grannen tidigt, även när den andra halvan inte berörs av själva bygget.",
     ],
     "aside": None},
    {"id": "skala-enskede", "h2": "Skala och proportion i typhusområdena",
     "paras": [
       "Redan 1970-talets inventering varnade för att om- och tillbyggnader förryckte skala och proportion, inte minst i områdena med typhus. Den beskrev samtidigt hur husägare började återställa husen, med ny träpanel av samma typ i stället för eternit och med ursprungliga fönster som fick sitta kvar.",
       "Stadens vägledning för trädgårdsstaden säger att tillbyggnader, takkupor och terrasser i första hand ska göras mot trädgårdssidan och att husens ursprungliga volym, proportioner och takformer ska vara utgångspunkten. I Gamla Enskede och Äppelviken beskriver vägledningen ett nationalromantiskt drag med branta takfall och fönster med småspröjsade rutor, och det är de dragen en tillbyggnad behöver förhålla sig till.",
       "Ska taket på huset ses över samtidigt beskriver vi hur äldre tegel tas tillvara under " + _L.format("takrenovering-enskede.html", "takrenovering i Enskede") + ", och om fasaden behöver göras om, se " + _L.format("fasadrenovering-enskede.html", "fasadrenovering i Enskede") + ".",
     ],
     "aside": {"title": "Trädgårdsstadens råd", "items": [
       "Bygg mot trädgårdssidan", "Utgå från husets takform",
       "Behåll vyn in mot trädgårdarna", "Ta tillvara originalmaterial"]}},
    {"id": "smastugor-enskede", "h2": "Småstugorna på Enskedefältet",
     "paras": [
       "Enskedefältet räknas i stadens vägledning som småstugeområde, och där är råden lite annorlunda. Kvarteren är enhetliga, och i småstugeområdena har förändringarna genom åren enligt vägledningen huvudsakligen gjorts mot trädgårdssidan. Ett exempel i vägledningen visar en tillbyggnad med lägre nock än huvudbyggnaden och takfoten på samma nivå.",
       "Utanför de särskilt värdefulla miljöerna gäller den lovfria potten: högst 30 kvadratmeter sammanlagt, inte över nocken och minst 4,5 meter till gräns eller grannarnas skriftliga medgivande. Enligt Stockholms stad räknas tidigare lovfria tillägg som attefallstillbyggnader och skärmtak in. Påverkas bärande konstruktion eller brandskydd, eller installeras eldstad eller vatten och avlopp, krävs anmälan och startbesked.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad i Enskede",
  "steps": [
    ("Klassificering och avtal", "Vi kontrollerar Stadsmuseets karta, detaljplanen och om huset står på tomträtt."),
    ("Platsbesök", "Huset, den lilla tomten, avstånd till gräns och takets höjder mäts upp."),
    ("Skiss i husets skala", "Ett förslag mot trädgården som följer typhusets proportioner."),
    ("Lov eller anmälan", "I riksintresset tas underlag för bygglov fram, annars medgivanden och anmälan."),
    ("Kostnadsförslag", "Ett skriftligt förslag med varje del för sig."),
    ("Bygge och avslut", "Vi bygger med hänsyn till trädgården och går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Enskede",
  "rot": [
    "Skatteverket godkänner rotavdrag för en tillbyggnad av ett småhus om tillbyggnaden sitter ihop med husets yttervägg till minst 75 procent av en sida eller har en dörr mot huset. Större delen av den ursprungliga stommen ska behållas.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och kräver att du äger bostaden när arbetet görs. Geal drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Enskede?",
  "price": [
    "Om bygglov krävs i riksintresset, hur mycket plats det finns för etablering på en liten tomt, hur tillbyggnaden anpassas till typhusets material och takform, anslutningen mot det gamla taket och vilka installationer som ska in. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Krävs bygglov för en liten tillbyggnad i Gamla Enskede?",
     "Det är troligt. Gamla Enskede är riksintresse, och för särskilt värdefulla områden och byggnader gäller inte lovbefrielsen. Stadsmuseets klassificeringskarta ger en första indikation."),
    ("Fick man bygga uthus i Gamla Enskede från början?",
     "Nej. Enligt Stadsmuseets inventering förbjöd tomträttskontraktet från 1908 uthus på tomten och reglerade byggnadsrätten."),
    ("Varför ska tillbyggnaden ligga mot trädgården i Enskede?",
     "Stadens vägledning för trädgårdsstaden och småstugeområdena säger att tillbyggnader i första hand görs mot trädgårdssidan, så att gatubilden och vyn in mot trädgårdarna behålls."),
    ("Behöver vi läsa tomträttsavtalet innan vi bygger till?",
     "Det är klokt. I Gamla Enskede styrde tomträttskontraktet från början både byggnadsrätt och placering, och villkoren i ett nutida avtal kan också påverka."),
    ("Hur gör man en tillbyggnad på en småstuga på Enskedefältet?",
     "Enligt stadens vägledning med lägre nock än huvudbyggnaden, takfot i samma höjd och placering mot trädgården, så att husets ursprungliga form går att läsa ut."),
  ],
  "sources": [
    ("Stadsmuseet/Stockholmskällan – Gamla Enskede, byggnadsinventering 1974–1977 (pdf)",
     "https://stockholmskallan.stockholm.se/postfiles/KUL/SSM_Gamla_Enskede__byggnadsinventering_1974_1977_00.pdf"),
    _STH_VARSAM, _STH_TB, _PBL, _PBF, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Vill ni bygga till huset i Enskede?", "Boka ett gratis platsbesök så går vi igenom tomten, klassificeringen och reglerna."),
  "img": [
    ("Rödfärgat trähus från 1910-talet med brant tegeltak och staket i en trädgårdsstad i Enskede",
     "1910s Swedish wooden garden-city house painted falu red with white trim, steep red clay tile roof, small-paned windows, a low picket fence and lilac and fruit trees on a small plot, narrow curving street, Gamla Enskede Stockholm, spring daylight, empty scene, no people, no text"),
    ("Liten tillbyggnad med lägre tak på baksidan av ett äldre trähus",
     "back garden side of an old Swedish wooden cottage with a small newer single-storey extension that has a lower roof ridge and eaves at the same height as the house, matching red painted boards and clay tiles, small lawn, daylight, no people, no text"),
  ],
  "related": [],
},
}
