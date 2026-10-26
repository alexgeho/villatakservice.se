# -*- coding: utf-8 -*-
"""Tillbyggnad – ortsidor v22: Älvsjö, Hägersten, Ekerö, Haninge, Norrtälje, Vallentuna (2026-10-26).
Hubb: tillbyggnad.html (TJ_HUB["tillbyggnad"]). Struktur som tj_v14_tillbyggnad.py, tre bilder per sida.

Rättslig ram (riksdagen.se, lydelse lag 2025:974, läst 2026-10-26): PBL 9 kap. 9–10 §§ (lovfri tillbyggnad på en
byggnad som inte är en komplementbyggnad: högst 30,0 m² BTA/OPA, inte över taknocken, sammanlagt 30,0 m² med tidigare
lovfria tillbyggnader), 11–12 §§ (tillbyggnad av komplementbyggnad), 34–35 §§ (4,5 m, 30,0 m från järnväg,
grannmedgivande), 37 § (särskilt värdefulla byggnader och områden). Boverket – Göra en tillbyggnad: tidigare lovfria
åtgärder som räknas in (attefallstillbyggnad, attefallstakkupa, liten tillbyggnad utanför plan och tätbebyggt
område, skärmtak, altan, balkong eller burspråk), anmälan vid ventilation/eldstad/VA och när bärande delar eller
brandskydd påverkas väsentligt, lovfri tillbyggnad får strida mot detaljplan utom skyddsbestämmelser.

Lokal vinkel per sida (skild från v8/v14-orterna och från ortens byggföretags-, snickar- och taksidor):
Älvsjö – villastadens planer med stora byggrätter kontra den lovfria 30 m²-potten, utbyggnadsriktning mot
  trädgårdssidan, volym och takform, nya tillägg i annat material, marknivå, stödmurar och dagvatten (Varsam
  utveckling, villastad) och stadens sida om bygglovsbefriad tillbyggnad (prickmark, anmälan, allmän plats).
Hägersten – två slags småhusområden: Mälarhöjden (villastad, kulturhistoriskt värdefull miljö och generösa byggrätter
  enligt tabellen) och Fruängen (tunnelbanestad, gruppbyggda rad- och kedjehus), Stadsmuseets klassificering,
  anmälan när brandskyddet påverkas, grannmedgivande i radhuslängan, vad som räknas in i 30 m².
Ekerö – kommunens nya bedömning av särskilt värdefulla byggnader och områden i Ekerökartan, totalförsvarets områden,
  skyddsbestämmelser (markförorening, olyckor, översvämning, erosion), skärmtak i potten, inglasad altan kräver lov,
  lägenhetsregistret när boarean ändras, Roslagsvatten och eget avlopp.
Haninge – när lov krävs (ej lovfri, eller ihopbyggd komplementbyggnad), lovfri 30 m², frivilligt lov när villan är
  ny, situationsplanen (nybyggnadskarta 1:400, minst tre mått i rät vinkel), fasader med NCS och marklinjer och
  kommunens exempel på kontrollplan för tillbyggnad (SBF89 2026-10-06, 19 punkter med BFS 2024-hänvisningar).
Norrtälje – tidigare lovfria åtgärder före 2025-12-01 som räknas in (anmäld tillbyggnad 15 m², skärmtak 15 m²,
  takkupa), tillbyggnad på enbostadshus eller fritidshus får strida mot planen, strandskydd (förbud mot tillbyggnader,
  100/300 m, dispens även för lovfritt, landskapsbildsskydd – Länsstyrelsen, Arholma), riksintressen och VA utanför
  plan, ingen bedömning via e-post – frivilligt lov.
Vallentuna – kommunens krav: inte högre än taknocken, 4,5 m mot granne/samfällighet/allmän plats, handlingarna
  (situationsplan 1:500, sektion genom befintligt hus och tillbyggnad, ramp eller hiss vid höjdskillnad, NCS),
  handlingar som kan behövas (bullerutredning, antikvarisk utredning), bygglovsarkivet (1950–2024, cirka 75 %).

Fakta endast från källorna i respektive 'sources', öppnade med curl (UA Mozilla) 2026-10-26, alla svarade 200
(Skatteverket först timeout, 200 vid nytt försök); pdf:erna (Varsam utveckling, Haninges kontrollplan) har textlager.
Strukna / ej använda: alla avgifter och handläggningstider (Norrtäljes tio/20 veckor, Länsstyrelsens tre veckor),
Vallentunas "kontrollansvarig, kopia på certifikat" (cert – utelämnat), Haninges uppgift om staket 80 cm (ej relevant),
om Mälarhöjden är "särskilt värdefullt" enligt PBL 8:13 (tabellen anger kulturhistoriskt värdefull miljö – texten säger
att Stadsmuseets karta ska kontrolleras), om Fruängens radhus är klassificerade (tabellen har inget kryss för Fruängen –
ingen klassificering påstås), Varsams vägledning för storskaliga stadsdelar (gäller inte Fruängen – inte använd).
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no text, no letters"

_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 9 kap. 9–14 och 34–37 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_BV_TB = ("Boverket – Göra en tillbyggnad",
          "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/gora-en-tillbyggnad/")
_SKV_JOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_STH_TB = ("Stockholms stad – Tillbyggnad (bygglovsbefriad)",
           "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/tillbyggnad-bygglovsbefriad/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_EKE_VAD = ("Ekerö kommun – Vad vill du bygga?", "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/vad-vill-du-bygga")
_EKE_STR = ("Ekerö kommun – Strandskydd, bryggor och sjöbodar",
            "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/strandskydd-bryggor-och-sjobodar")
_HN = "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/"
_HAN_TB = ("Haninge kommun – Tillbyggnad av en- och tvåbostadshus", _HN + "tillbyggnad-en-och-tvabostadshus/")
_HAN_BEF = ("Haninge kommun – Bygglovsbefriad ny och tillbyggnad", _HN + "bygglovsbefriad-ny-och-tillbyggnad/")
_HAN_KP = ("Haninge kommun – Kontrollplan tillbyggnad, exempel (pdf)",
           "https://www.haninge.se/4a900c/contentassets/d035506cb89f4eb382de69277d4f42e0/blankett-sbf89-kontrollplan-tillbyggnad-pbl-bfs.pdf")
_NOR_LOV = ("Norrtälje kommun – Lovbefriade åtgärder", "https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/lovbefriade-atgarder/")
_NOR_SKI = ("Norrtälje kommun – Skillnad mellan bygglovspliktiga, anmälningspliktiga och bygglovsbefriade åtgärder",
            "https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/skillnad-mellan-atgarder/")
_NOR_STR = ("Norrtälje kommun – Strandskyddsdispens", "https://www.norrtalje.se/sjalvservice/bygga-bo-miljo/strandskyddsdispens/")
_VB = "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/"
_VAL_TB = ("Vallentuna kommun – Tillbyggnad av en- och tvåbostadshus", _VB + "behover-jag-bygglov/tillbyggnad-av-en--och-tvabostadshus")
_VAL_ARK = ("Vallentuna kommun – Bygglovsarkivet", _VB + "bygglovsarkivet")

_ROT_BASE = ("Rotavdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 "
             "kronor tillsammans med rutavdrag. Material och resor ger inget avdrag.")
_ROT_TB = ("Skatteverket godkänner en tillbyggnad av ett småhus om någon av tillbyggnadens sidor sitter ihop med husets "
           "yttervägg till minst 75 procent, eller om det finns en dörr emellan. Bostaden ska vara äldre än fem år och större "
           "delen av den ursprungliga stommen ska behållas. Bygglovshandlingar och arkitekt ger inget avdrag. Geal drar "
           "avdraget direkt på fakturan där det gäller.")

PAGES_TJ = {

# ------------------------------------------------------------------ ÄLVSJÖ
"tillbyggnad-alvsjo.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Älvsjö", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Älvsjö – trädgårdssidan och villans volym",
  "description": "Tillbyggnad i Älvsjö: planens byggrätt eller lovfria 30 m², varför staden vill se tillbyggnaden mot trädgården, volym och takform, material och marknivåer.",
  "h1": "Tillbyggnad i Älvsjö",
  "lead": "I Älvsjös villastäder finns äldre planer som ger stora byggrätter, men också en grön karaktär som staden vill behålla. En tillbyggnad som passar in handlar därför lika mycket om var och hur den placeras som om hur stor den blir. Geal Entreprenad AB bygger till villor i hela Älvsjö och börjar med planen och tomten.",
  "card": "Byggrätt, trädgårdssida och volym.",
  "sections": [
    {"id": "byggratt-alvsjo", "anchor": "Planen eller 30 m²",
     "h2": "Detaljplanens byggrätt eller lovfria 30 kvadratmeter",
     "paras": [
       "Stadens skrift Varsam utveckling av småhus- och villaområden nämner Älvsjö, Herrängen, Långsjö och Långbro bland villastäderna med äldre stadsplaner som tillåter generösa byggrätter. Den påpekar att det i regel finns en detaljplan som reglerar hur mycket du får bygga, var och hur högt, och att ett första steg är att stämma av det du vill göra mot den. Ryms tillbyggnaden i planen söker du bygglov enligt planen.",
       "Vill du bygga till utan bygglov gäller lagens regel: högst 30,0 kvadratmeter bruttoarea eller öppenarea, inte högre än husets taknock och sammanlagt 30,0 kvadratmeter med tidigare lovfria tillbyggnader. Staden räknar upp friggebodsskärmtak, attefallstillbyggnader och attefallstakkupor som exempel på sådant som ska räknas in. För ett en- eller tvåbostadshus får den lovfria tillbyggnaden strida mot detaljplanen och alltså placeras på prickmark.",
     ],
     "aside": {"title": "Räknas in i 30 m²", "items": [
       "Friggebodsskärmtak", "Attefallstillbyggnad", "Attefallstakkupor", "Den nya tillbyggnaden"]}},
    {"id": "riktning-alvsjo", "h2": "Mot trädgården – och undantagen",
     "paras": [
       "För villastäderna skriver staden att det vanligaste är att orientera tillbyggnader in mot tomten, i den privata zonen på trädgårdssidan, och att undvika tillbyggnader mot gatan. Ligger huset fritt på tomten med trädgården mot gatan kan en tillbyggnad mot gaturummet fungera utan att gatan påverkas negativt.",
       "Skriften visar båda fallen: en villa långt in på tomten där tillbyggnaden mot gatan samspelar med huset, och en villa nära gatan där tillbyggnaden mot trädgården underordnar sig huvudbyggnaden. Villastäderna planerades med husen indragna från gatan och en grön förgård mellan hus och gata, och gatorna kantades av klippta häckar eller staket. Staden vill också att flera utfarter intill varandra och stora sammanhängande parkeringsytor undviks. Vi tittar på hur ditt hus och grannarnas står mot gatan innan vi föreslår en placering.",
     ],
     "aside": None},
    {"id": "volym-alvsjo", "h2": "Volym, takform och material",
     "paras": [
       "Staden råder dig att utgå från de ursprungliga husens volym, proportioner och takformer när du bygger till. Ett nytt tillägg behöver inte kopiera huset. Det kan ha samma volym och form som området men ett nytt, väl gestaltat material, eller avvika i form men ha de karaktärsskapande materialen, kulörerna och detaljerna. Skriften påpekar att det många gånger är klokt att ta hjälp av en sakkunnig, till exempel arkitekt eller byggnadsantikvarie.",
       "Påverkar tillbyggnaden husets bärande konstruktion eller brandskydd behöver du göra en anmälan och vänta på startbesked, skriver staden. Detsamma gäller om du installerar eldstad, vatten eller avlopp i tillbyggnaden. Vi ser till att anslutningen mot det befintliga taket och stommen är utredd innan något rivs upp.",
     ],
     "aside": {"title": "Utgå från huset", "items": [
       "Ursprunglig volym", "Proportioner", "Takform", "Karaktärsskapande material"]}},
    {"id": "mark-alvsjo", "h2": "Marken, träden och dagvattnet",
     "paras": [
       "Villastadens gröna karaktär är det som håller ihop områdena, enligt staden. Förändringar av marknivån behöver göras med omsorg om befintlig vegetation, berghällar och stödmurar, och gröna ytor bör inte hårdgöras så att dagvattenhanteringen försämras. Dagvattnet ska tas om hand inom den egna fastigheten.",
       "Därför ritar vi tillbyggnadens grund efter tomtens nivåer och planerar var regnvattnet från det nya taket ska ta vägen. Ska tillbyggnaden närmare gränsen än 4,5 meter behövs grannens skriftliga medgivande. Mot gata och park är kommunen oftast huvudman, och då går förfrågan skriftligt till stadsbyggnadskontoret. Om större byggprojekt i Älvsjö kan du läsa under " + _L.format("byggforetag-alvsjo.html", "byggföretag i Älvsjö") + " och om altaner och snickeri under " + _L.format("snickare-alvsjo.html", "snickare i Älvsjö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad i Älvsjö",
  "steps": [
    ("Planen", "Detaljplanens byggrätt och Stadsmuseets klassificering för fastigheten."),
    ("Platsbesök", "Husets placering, trädgårdssidan, marknivåer och träd."),
    ("Skiss", "Volym, takform och material utgår från huset."),
    ("Kostnadsförslag", "Arbete, material och lovhandlingar står var för sig."),
    ("Lov eller anmälan", "Bygglov enligt planen, lovfritt med anmälan eller frivilligt lov."),
    ("Byggnation", "Grund, stomme, tak och anslutningen mot huset."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Älvsjö",
  "rot": [_ROT_BASE, _ROT_TB],
  "price_h2": "Vad påverkar kostnaden i Älvsjö?",
  "price": [
    "Tillbyggnadens storlek, grunden på en kuperad tomt, hur taket ska anslutas, valet av material och om bygglov behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga till mot gatan i Älvsjös villastad?",
     "Staden avråder i regel och föredrar trädgårdssidan. Ligger huset långt in på tomten med trädgården mot gatan kan det fungera, om gatan inte påverkas negativt."),
    ("Räknas vårt gamla skärmtak när vi bygger till lovfritt i Älvsjö?",
     "Ja. Staden nämner friggebodsskärmtak, attefallstillbyggnader och attefallstakkupor som tidigare lovfria tillbyggnader som ska räknas in i 30,0 kvadratmeter."),
    ("Måste tillbyggnaden se likadan ut som villan i Älvsjö?",
     "Nej. Staden skriver att det nya ska ta tillvara karaktärsskapande material, kulör, byggnadsdelar och former men inte nödvändigtvis kopiera."),
    ("Gäller avståndet till järnvägen för en lovfri tillbyggnad i Älvsjö?",
     "Ja. Staden skriver att tillbyggnaden ska placeras minst 30 meter från järnvägsspår, och att det krävs medgivande från infrastrukturförvaltaren för att placera den närmare."),
    ("Vem ger medgivande om tillbyggnaden hamnar nära gatan i Älvsjö?",
     "Mot allmän plats som gata och park är kommunen oftast huvudman. Staden vill ha förfrågan skriftligt till stadsbyggnadskontoret."),
  ],
  "sources": [_STH_TB, _VARSAM, _BV_TB, _PBL, _SKV_JOB, _SKV_ROT],
  "cta": ("Vill ni bygga till villan i Älvsjö?", "Boka ett gratis platsbesök, så går vi igenom planen och var tillbyggnaden passar bäst."),
  "img": [
    ("Äldre trävilla med en lägre tillbyggnad med glaspartier mot en lummig trädgård",
     "early 1900s Swedish two-storey wooden villa with light yellow board cladding and a red clay tile roof, with a lower new single-storey extension with large glass doors and a pitched roof attached on the garden side, mature apple trees and lawn, Stockholm villa suburb, summer daylight" + _SFX),
    ("Villa långt in på tomten med en tillbyggnad som följer husets takform",
     "Swedish villa set far back on a large leafy plot with a front garden toward a narrow winding street, a new side extension with the same roof pitch and similar wooden cladding, clipped hedge along the street, daylight" + _SFX),
    ("Berghäll och låg stödmur av natursten i en villaträdgård",
     "garden of a Swedish villa with a smooth granite outcrop, a low natural stone retaining wall and lawn next to a freshly cast concrete foundation slab for a small extension, trees left standing, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ HÄGERSTEN
"tillbyggnad-hagersten.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Hägersten", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Hägersten – villastad och radhus i Fruängen",
  "description": "Tillbyggnad i Hägersten: Mälarhöjdens villastad och Fruängens gruppbyggda radhus, Stadsmuseets karta, brandskyddet mot grannen och medgivandet i längan.",
  "h1": "Tillbyggnad i Hägersten",
  "lead": "I Hägersten ligger två helt olika slags småhusområden nära varandra: villastaden i Mälarhöjden och de gruppbyggda rad- och kedjehusen i Fruängen. Vad som är rimligt att bygga till skiljer sig mycket mellan dem. Geal Entreprenad AB bygger till villor och radhus i hela Hägersten och utgår från vilket område huset ligger i.",
  "card": "Villastad, radhuslänga och brandskydd.",
  "sections": [
    {"id": "tva-omraden-hagersten", "anchor": "Två slags områden",
     "h2": "Villastad och tunnelbanestad",
     "paras": [
       "Stadens skrift Varsam utveckling av småhus- och villaområden delar in småhusen efter karaktär. Mälarhöjden är en villastad, där villasamhällen växte upp efter privata initiativ genom större markförvärv. I tabellen över stadens småhusområden är Mälarhöjden markerad både som kulturhistoriskt värdefull miljö och som område med detaljplaner med generösa byggrätter. Fruängen räknas till tunnelbanestäderna med gruppbyggda småhus.",
       "För tunnelbanestäderna beskriver skriften radhus och kedjehus i enhetligt utformade husgrupper, ofta anpassade till terrängen med en suterrängvåning, och planer byggda på ABC-stadens tankar. Där är husgruppen själva karaktären. I villastaden är bebyggelsen i stället brokig, med hus från olika tider, och skriften visar en tillbyggd villa i Mälarhöjden som exempel.",
     ],
     "aside": {"title": "Enligt stadens tabell", "items": [
       "Mälarhöjden – villastad", "Kulturhistoriskt värdefull miljö", "Generösa byggrätter",
       "Fruängen – tunnelbanestad"]}},
    {"id": "malarhojden-hagersten", "h2": "Mälarhöjden: kontrollera klassificeringen först",
     "paras": [
       "En tillbyggnad på högst 30,0 kvadratmeter som inte går över taknocken kräver normalt inget bygglov. Men staden skriver att utökad lovplikt gäller om du bor i en särskilt kulturhistoriskt värdefull byggnad eller ett särskilt kulturhistoriskt värdefullt område, och då krävs bygglov även för en tillbyggnad som annars är lovfri. Stadsmuseets klassificeringskarta ger en första indikation, men du kan behöva kontakta Stadsmuseet för en bedömning.",
       "I villastäderna råder staden dig att utgå från de ursprungliga husens volym, proportioner och takform och att ta tillvara karaktärsskapande material, kulörer och detaljer. I Mälarhöjden, där tabellen anger detaljplaner med generösa byggrätter, kan en större tillbyggnad prövas mot planen i ett bygglov. Vi tar fram ritningar för båda vägarna och visar vad skillnaden innebär.",
     ],
     "aside": None},
    {"id": "fruangen-hagersten", "h2": "Fruängen: radhuset och grannarna",
     "paras": [
       "Ett radhus delar vägg med grannen. Staden skriver att du behöver göra en anmälan och vänta på startbesked om tillbyggnaden påverkar byggnadens bärande konstruktion eller brandskydd. I en radhuslänga kan brandskyddet mot grannhuset påverka hur en tillbyggnad mot trädgården kan göras. Vi utreder det innan ritningarna är klara.",
       "Ska tillbyggnaden närmare gränsen än 4,5 meter behövs ett skriftligt medgivande från berörda grannar. Det ska enligt staden innehålla fastighetsbeteckning, vilken typ av åtgärd det gäller, en situationsplan med åtgärden och avståndet till gränsen inritat och grannarnas underskrifter. Medgivandet bör du kunna visa för byggnadsnämnden om ett tillsynsärende uppstår. Finns det en samfällighet mellan husen räknas gränsen mot den också.",
       "Skriften beskriver tunnelbanestädernas radhus som anlagda på bryn och platåer utanför centrum, med mjuk anpassning till terrängen och tidstypisk färgsättning, och utformning och materialval som varierar mellan områdena. Vi ritar tillbyggnaden efter husgruppens takfall och fasadmaterial, så att den följer längan i stället för att bryta den.",
     ],
     "aside": {"title": "Medgivandet ska ha", "items": [
       "Fastighetsbeteckning", "Typ av åtgärd", "Situationsplan med avstånd", "Grannarnas underskrifter"]}},
    {"id": "potten-hagersten", "h2": "Det som redan är byggt räknas in",
     "paras": [
       "Lovfriheten gäller sammanlagt 30,0 kvadratmeter per hus. Boverket räknar upp vad som ska inkluderas om det redan har byggts lovfritt enligt tidigare regler: attefallstillbyggnad, attefallstakkupa, skärmtak, altan, balkong eller burspråk. Har huset redan en attefallstillbyggnad på 15 kvadratmeter och ett skärmtak på 15 kvadratmeter går det inte att bygga mer utan lov.",
       "En lovfri tillbyggnad får strida mot detaljplanen, men inte mot regler om skyddsåtgärder och skyddsanordningar. Den ska också göras varsamt, anpassas till omgivningen och får inte innebära en betydande olägenhet för grannarna. Om större ombyggnader i området kan du läsa under " + _L.format("byggforetag-hagersten.html", "byggföretag i Hägersten") + ", och om fasaderna under " + _L.format("fasadrenovering-hagersten.html", "fasadrenovering i Hägersten") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad i Hägersten",
  "steps": [
    ("Området", "Villastad eller gruppbyggt radhusområde och Stadsmuseets klassificering."),
    ("Platsbesök", "Stomme, brandskydd mot grannen och tidigare tillbyggnader mäts in."),
    ("Skiss", "Tillbyggnaden utgår från husets volym och takform."),
    ("Medgivande", "Situationsplan till grannarna när avståndet är mindre än 4,5 meter."),
    ("Lov eller anmälan", "Bygglov, frivilligt lov eller anmälan för bärande delar och brandskydd."),
    ("Byggnation", "Grund, stomme, tak och anslutningen mot huset."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Hägersten",
  "rot": [_ROT_BASE, _ROT_TB],
  "price_h2": "Vad påverkar kostnaden i Hägersten?",
  "price": [
    "Tillbyggnadens storlek, grunden i sluttande terräng, brandskyddet mot grannhuset, anslutningen mot taket och om bygglov behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Krävs bygglov för en tillbyggnad i Mälarhöjden?",
     "Det beror på klassificeringen. Är byggnaden eller området särskilt kulturhistoriskt värdefullt krävs bygglov även för en tillbyggnad som annars är lovfri. Stadsmuseets karta ger en första indikation."),
    ("Måste vi göra en anmälan för en tillbyggnad på vårt radhus i Fruängen?",
     "Ja, om tillbyggnaden påverkar husets bärande konstruktion eller brandskydd. Då krävs anmälan och startbesked innan arbetet börjar."),
    ("Vår balkong byggdes utan lov – påverkar den hur mycket vi får bygga till?",
     "Ja. Boverket räknar upp balkong, altan, skärmtak och attefallstillbyggnad bland de tidigare lovfria åtgärder som räknas in i 30 kvadratmeter."),
    ("Vem lämnar medgivande om tillbyggnaden hamnar nära en park i Hägersten?",
     "Mot allmän platsmark som park och gata är kommunen oftast huvudman. Staden vill att du skickar förfrågan skriftligt till stadsbyggnadskontoret."),
    ("Vad räknas som tunnelbanestad i Hägersten?",
     "I stadens skrift Varsam utveckling hör Fruängen till de gruppbyggda småhusområdena i tunnelbanestaden."),
  ],
  "sources": [_STH_TB, _VARSAM, _BV_TB, _PBL, _SKV_JOB, _SKV_ROT],
  "cta": ("Vill ni bygga till i Hägersten?", "Boka ett gratis platsbesök, så går vi igenom området, huset och grannarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhuslänga från efterkrigstiden med en låg inglasad tillbyggnad mot trädgården",
     "1950s Swedish terraced houses in a uniform row with brick facades and low pitched roofs, one house with a new low glazed garden room extension on the back that keeps the same roof line, small rear gardens separated by hedges, Stockholm suburb, summer daylight" + _SFX),
    ("Trävilla på en kuperad tomt med berg i dagen och tallar",
     "1920s Swedish wooden villa on a hilly leafy plot in an old Stockholm villa suburb, with a new one-storey extension on the gable end in matching board cladding and roof tiles, rock outcrop and pine trees, daylight" + _SFX),
    ("Brandskyddande vägg mellan två radhus under ombyggnad",
     "empty construction site between two white Swedish terraced houses during the build of a rear extension, a tall fire-rated gypsum board party wall section and a sheet metal flashing at the roof edge, timber framing visible, nobody present, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ EKERÖ
"tillbyggnad-ekero.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Ekerö", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad på Ekerö – kartan, glasade altaner och registret",
  "description": "Tillbyggnad på Ekerö: Ekerökartan över värdefulla områden, skärmtak i potten, inglasad altan, lägenhetsregistret, strandskyddet och vatten och avlopp.",
  "h1": "Tillbyggnad på Ekerö",
  "lead": "Ekerö kommun gjorde en ny bedömning av sina särskilt värdefulla byggnader och områden när de nya byggreglerna kom. Det betyder att en tillbyggnad som är lovfri på en ö kan kräva bygglov på nästa. Geal Entreprenad AB bygger till villor och fritidshus på Mälaröarna och börjar med kartan.",
  "card": "Kartan, inglasningen och registret.",
  "sections": [
    {"id": "kartan-ekero", "anchor": "Ekerökartan",
     "h2": "Börja i Ekerökartan",
     "paras": [
       "När plan- och bygglagen ändrades gjorde kommunen en ny bedömning av sina särskilt värdefulla byggnader och områden. De finns nu i Ekerökartan tillsammans med totalförsvarets riksintressen, och kommunen ber dig börja med att kontrollera om din fastighet berörs. Inom de särskilt värdefulla områdena går det inte att använda de nya lovfria reglerna.",
       "Kommunen nämner två undantag till. Ska tillbyggnaden närmare gränsen än 4,5 meter krävs grannarnas skriftliga medgivande, annars bygglov. Och lovfria åtgärder får inte strida mot skyddsbestämmelser i detaljplanen om markförorening, olyckor, översvämning och erosion. Vi läser kartan och planen för din fastighet innan vi föreslår en lösning.",
     ],
     "aside": {"title": "Lovfriheten gäller inte", "items": [
       "I särskilt värdefulla områden", "Under 4,5 m utan medgivande",
       "Mot planens skyddsbestämmelser"]}},
    {"id": "potten-ekero", "h2": "Skärmtak i potten – och altanen som glasas in",
     "paras": [
       "En tillbyggnad av ett hus som inte är en komplementbyggnad får vara högst 30 kvadratmeter bruttoarea eller öppenarea tillsammans med tidigare lovfria tillbyggnader, och den får inte gå över husets taknock. Ekerö kommun påpekar att skärmtak nu räknas in i den potten. Ett skärmtak över uteplatsen och ett uterum delar alltså på samma 30 kvadratmeter.",
       "Altaner lägre än 1,2 meter kräver inget bygglov, och utanför detaljplanelagt område krävs inget bygglov för altan alls. Men kommunen skriver att en altan behöver bygglov om du bygger in den, till exempel med inglasning, eller om du bygger ett rum under den. Det gäller både fristående altaner och altaner som byggs ihop med huset. Vill du glasa in en befintlig altan räknar vi därför på den som en tillbyggnad.",
     ],
     "aside": None},
    {"id": "registret-ekero", "h2": "Meddela kommunen när boarean ändras",
     "paras": [
       "En regel som ofta glöms: om du bygger ett komplementbostadshus, inreder ytterligare en bostad eller ändrar boarean i ditt bostadshus ska du meddela kommunen när bostaden står klar, oavsett vad de nya byggreglerna säger. Kommunen behöver uppgiften för att uppdatera lägenhetsregistret. En tillbyggnad som blir ett nytt sovrum eller ett större vardagsrum ändrar boarean.",
       "Tillbyggnader av befintliga komplementbyggnader har egna mått: högst 30 kvadratmeter byggnadsarea inom detaljplan och 50 utanför, högst 4 meter i nock inom plan och 4,5 utanför, mindre än huvudbyggnaden och inom tomtens sammanlagda 45 respektive 65 kvadratmeter. Om nya fristående hus på tomten kan du läsa under " + _L.format("attefallshus-ekero.html", "attefallshus på Ekerö") + ".",
     ],
     "aside": {"title": "Meddela kommunen vid", "items": [
       "Nytt komplementbostadshus", "Ytterligare en bostad", "Ändrad boarea"]}},
    {"id": "vatten-ekero", "h2": "Strand, vatten och avlopp",
     "paras": [
       "Många tomter på Ekerö ligger nära vatten. Kommunen ber dig sätta dig in i reglerna om strandskydd innan du bygger i närheten av vatten. Vi mäter in avståndet till strandlinjen tidigt, eftersom placeringen kan avgöra om en dispens behövs.",
       "Får tillbyggnaden badrum eller kök gäller två saker. Ska den anslutas till kommunalt vatten och avlopp skickar du en anmälan till Roslagsvatten i god tid före byggstart. Har fastigheten eget avlopp och tillbyggnaden ger mer avloppsvatten kan du behöva söka tillstånd eller anmäla ändringen av den enskilda avloppsanläggningen. Om större byggprojekt på öarna kan du läsa under " + _L.format("byggforetag-ekero.html", "byggföretag på Ekerö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad på Ekerö",
  "steps": [
    ("Ekerökartan", "Särskilt värdefulla områden, totalförsvaret och detaljplanens skyddsbestämmelser."),
    ("Platsbesök", "Tidigare skärmtak och tillbyggnader mäts in och avståndet till vatten kontrolleras."),
    ("Skiss", "Tillbyggnaden ritas efter huset och tomten."),
    ("Lov eller anmälan", "Bygglov, frivilligt lov eller anmälan för installationer."),
    ("Byggnation", "Grund, stomme, tak och anslutningen mot huset."),
    ("Klart", "Ändrad boarea meddelas kommunen för lägenhetsregistret."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad på Ekerö",
  "rot": [_ROT_BASE, _ROT_TB],
  "price_h2": "Vad påverkar kostnaden på Ekerö?",
  "price": [
    "Tillbyggnadens storlek, grund på berg, lera eller i sluttning, om badrum och avlopp ska in, hur material kan köras fram och om bygglov behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kräver en inglasad altan bygglov på Ekerö?",
     "Ja. Kommunen skriver att en altan behöver bygglov om du bygger in den, till exempel med inglasning, oavsett om den står fritt eller är ihopbyggd med huset."),
    ("Räknas skärmtak in i de lovfria 30 kvadratmetrarna på Ekerö?",
     "Ja. Kommunen påpekar att skärmtak nu ingår i den lovfria potten för tillbyggnader."),
    ("Varför ska vi meddela Ekerö kommun när tillbyggnaden är klar?",
     "Om boarean ändras ska kommunen få veta det när bostaden står klar, så att lägenhetsregistret kan uppdateras. Det gäller oavsett om tillbyggnaden krävde lov."),
    ("Vi har eget avlopp på Ekerö – påverkar det tillbyggnaden?",
     "Det kan göra det. Ger tillbyggnaden mer avloppsvatten kan du behöva söka tillstånd eller anmäla ändring av den enskilda avloppsanläggningen, skriver kommunen."),
    ("Var ser vi om vår fastighet på Ekerö är särskilt värdefull?",
     "I Ekerökartan. Kommunen har gjort en ny bedömning av särskilt värdefulla byggnader och områden och visar dem där tillsammans med totalförsvarets riksintressen."),
  ],
  "sources": [_EKE_VAD, _EKE_STR, _BV_TB, _PBL, _SKV_JOB, _SKV_ROT],
  "cta": ("Vill ni bygga till på Ekerö?", "Boka ett gratis platsbesök, så går vi igenom kartan och tomten innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Rödmålad villa med en nybyggd inglasad tillbyggnad mot en sjöutsikt mellan träd",
     "falu red Swedish wooden villa with white trims on a sloping lakeside plot, a new glazed garden room extension with a low pitched roof attached on the side facing the water, birches and pines, calm Lake Mälaren glimpsed between trees, summer evening light" + _SFX),
    ("Altan med skärmtak av trä och glas på baksidan av en villa",
     "wooden deck at the back of a Swedish villa covered by a timber framed canopy with clear glass roof panels, outdoor furniture removed, lawn and trees beyond, daylight" + _SFX),
    ("Grund och stomme till en tillbyggnad vid en villa nära en strand",
     "timber frame and floor joists of a new extension under construction next to a Swedish lakeside villa, gravel and stone around, water and reeds visible in the background, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ HANINGE
"tillbyggnad-haninge.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Haninge", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Haninge – lov, mått och kontrollplanen",
  "description": "Tillbyggnad i Haninge: när bygglov krävs, ihopbyggda förråd, lovfria 30 m², situationsplanen med tre mått och kommunens exempel på kontrollplan.",
  "h1": "Tillbyggnad i Haninge",
  "lead": "Ett uterum, en takkupa, en påbyggnad eller ett förråd som byggs ihop med huset – Haninge kommun räknar allt det som tillbyggnader. Vad som kräver bygglov och vilka handlingar som behövs har kommunen beskrivit noga. Geal Entreprenad AB bygger till villor och fritidshus i hela Haninge och tar fram underlaget.",
  "card": "Lov, situationsplan och kontrollplan.",
  "sections": [
    {"id": "lov-haninge", "anchor": "När lov krävs",
     "h2": "När tillbyggnaden behöver bygglov",
     "paras": [
       "Haninge kommun ger uterum, skärmtak, takkupa och påbyggnad som exempel på tillbyggnader. Du behöver söka bygglov om tillbyggnaden inte omfattas av reglerna för bygglovsbefriad tillbyggnad, och om du bygger ihop en befintlig komplementbyggnad med bostadshuset. Ett garage eller förråd som ska bli en del av huset kräver alltså lov.",
       "Utan bygglov får du bygga högst 30 kvadratmeter, om du inte tidigare har använt möjligheten och tillbyggnaden uppfyller kraven: brutto- eller öppenarea på högst 30 kvadratmeter sammanlagt, inte högre än husets taknock och minst 4,5 meter från tomtgränsen och 30 meter från järnvägsspårets mitt, om grannen inte skriftligen har godkänt något annat. Ligger tomten i ett område som är utpekat som särskilt värdefullt krävs bygglov ändå.",
     ],
     "aside": {"title": "Bygglov krävs", "items": [
       "Över 30 m² sammanlagt", "Ihopbyggd komplementbyggnad",
       "Särskilt värdefullt område", "Närmare än 4,5 m utan medgivande"]}},
    {"id": "nyttus-haninge", "h2": "Nytt hus och tillbyggnad samtidigt",
     "paras": [
       "Bygger du ett nytt en- eller tvåbostadshus och vill använda den lovfria tillbyggnaden direkt för att få en större yta, skriver kommunen att du då måste söka ett frivilligt bygglov för tillbyggnaden samtidigt som du söker bygglov för huset. Om du redan har byggt lovfria tillbyggnader, till exempel en attefallstillbyggnad eller ett skärmtak, räknas deras yta in.",
       "Kommunen påpekar också att en överprövande myndighet kan bedöma att en åtgärd faktiskt är bygglovspliktig om någon klagar, trots kommunens riktlinjer, och att du har rätt att få åtgärden prövad i ett frivilligt lov. Strandskyddet gäller vanligtvis mellan 100 och 300 meter från kustlinjen, sjöar och större vattendrag, och där kan dispens behövas.",
     ],
     "aside": None},
    {"id": "handlingar-haninge", "h2": "Situationsplanen och ritningarna",
     "paras": [
       "Situationsplanen ska göras på en nybyggnadskarta i skala 1:400, som beställs via kommunens e-tjänst. Tillbyggnadens placering ska låsas med minst tre avstånd i rät vinkel från närmaste fastighetsgränser, varav två mått ska utgå från ett hushörn till två olika gränser. Avståndet till befintliga byggnader ska också anges, och nybyggnadskartan eller dess text får inte ändras.",
       "Fasadritningen i 1:100 ska visa berörda fasader med väderstreck, vad som är befintligt och vad som är nytt, marklinjer kring tillbyggnaden och material och kulör med NCS-koder. Sektionen ska visa rumshöjder, färdiga golvnivåer, takvinkel och tillbyggnadens byggnads- och nockhöjd. Planritningen visar berörda plan och var sektionerna är tagna.",
     ],
     "aside": {"title": "Situationsplanen", "items": [
       "Nybyggnadskarta 1:400", "Minst tre mått i rät vinkel",
       "Två mått från ett hushörn", "Avstånd till andra byggnader"]}},
    {"id": "kontrollplan-haninge", "h2": "Kommunens exempel på kontrollplan",
     "paras": [
       "Du som byggherre ansvarar för en riskanalys och för en kontrollplan som visar vilka kontroller som görs, hur, mot vad och av vem. Haninge har lagt ut ett exempel på kontrollplan för tillbyggnad med 19 punkter. Där finns bland annat placering, mått och höjdläge före grundläggning, befintlig byggnad och lastöverföring, fuktsäker anslutning, brandskydd mellan tillbyggnad och befintlig byggnad, genomföringar, ventilation och att ändringar görs varsamt med foto innan arbetet börjar.",
       "Exemplet hänvisar till Boverkets föreskrifter i serien BFS 2024 för bland annat bärförmåga, brandskydd, fukt och säkerhet vid användning, och det påpekar att kontrollplanen ska anpassas efter tillbyggnadens omfattning och det befintliga husets förutsättningar. De punkter som gäller själva bygget kontrollerar och signerar vi. Om husets tak och plåt kan du läsa under " + _L.format("takbyte-haninge.html", "takbyte i Haninge") + ", och om nya fristående hus under " + _L.format("attefallshus-haninge.html", "attefallshus i Haninge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad i Haninge",
  "steps": [
    ("Platsbesök", "Huset, tidigare tillbyggnader, avstånd och marknivåer."),
    ("Lovfrågan", "Lovfritt, bygglov eller frivilligt lov – och om tomten är särskilt värdefull."),
    ("Ritningar", "Situationsplan på nybyggnadskarta, fasader, plan och sektion."),
    ("Kontrollplan", "Riskanalys och kontrollpunkter utifrån kommunens exempel."),
    ("Byggnation", "Grund, stomme, tak och anslutning med signerade kontroller."),
    ("Slutbesked", "Tillbyggnaden används när slutbeskedet har kommit."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Haninge",
  "rot": [_ROT_BASE, _ROT_TB],
  "price_h2": "Vad påverkar kostnaden i Haninge?",
  "price": [
    "Tillbyggnadens storlek, grunden, anslutningen mot det befintliga taket och stommen, brandskyddet och om bygglov och nybyggnadskarta behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för att bygga ihop garaget med huset i Haninge?",
     "Ja. Haninge kommun skriver att det krävs bygglov när en befintlig komplementbyggnad byggs ihop med ett befintligt bostadshus."),
    ("Hur många mått ska situationsplanen ha för en tillbyggnad i Haninge?",
     "Minst tre avstånd i rät vinkel från närmaste fastighetsgränser, varav två ska utgå från ett hushörn till två olika gränser."),
    ("Kan vi bygga ett nytt hus och en lovfri tillbyggnad samtidigt i Haninge?",
     "Bara om du söker frivilligt bygglov för tillbyggnaden samtidigt med bygglovet för huset, enligt kommunen."),
    ("Vad tar Haninges exempel på kontrollplan upp om brandskydd?",
     "En egen punkt för brandskyddet mellan tillbyggnaden och den befintliga byggnaden, som kontrolleras mot brandskyddsprojekteringen före inklädnad."),
  ],
  "sources": [_HAN_TB, _HAN_BEF, _HAN_KP, _BV_TB, _PBL, _SKV_JOB, _SKV_ROT],
  "cta": ("Vill ni bygga till i Haninge?", "Boka ett gratis platsbesök, så går vi igenom lovfrågan och underlaget innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa med en ny påbyggd takkupa och ett uterum på gaveln",
     "1970s Swedish one-and-a-half storey villa with dark wooden cladding and a new large dormer on the roof plus a new glazed garden room on the gable end, rocky garden with pines, Stockholm southern suburb, clear daylight" + _SFX),
    ("Garage och villa som byggs ihop med en ny mellandel",
     "Swedish villa and a detached wooden garage being joined by a new connecting section under construction, timber frame and roof trusses in place, scaffolding, gravel driveway, overcast daylight" + _SFX),
    ("Fuktsäker anslutning mellan gammal och ny vägg under byggnation",
     "close-up of the joint between an existing painted wooden house wall and a new timber framed extension wall with wind barrier membrane and taped seams, before cladding, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ NORRTÄLJE
"tillbyggnad-norrtalje.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Norrtälje", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Norrtälje – gamla attefallsytor och strand",
  "description": "Tillbyggnad i Norrtälje: tidigare lovfria tillbyggnader som räknas in, fritidshus och detaljplan, strandskyddet och landskapsbildsskyddet, frivilligt lov.",
  "h1": "Tillbyggnad i Norrtälje",
  "lead": "Många hus i Norrtälje har redan byggts till i omgångar – en attefallstillbyggnad, ett skärmtak, en takkupa. Sedan december 2025 räknas allt det in när du vill bygga mer utan lov, och nära vattnet gäller dessutom strandskyddet. Geal Entreprenad AB bygger till villor och fritidshus i hela kommunen och börjar med det som redan finns.",
  "card": "Tidigare tillbyggnader, strand och frivilligt lov.",
  "sections": [
    {"id": "tidigare-norrtalje", "anchor": "Det som redan finns",
     "h2": "Det som byggdes före december 2025 räknas in",
     "paras": [
       "En tillbyggnad kräver inte bygglov om den har en brutto- eller öppenarea på högst 30 kvadratmeter, inte går över husets taknock och tillsammans med andra genomförda tillbyggnader håller sig inom 30 kvadratmeter. Norrtälje kommun påpekar att även sådant som var lovbefriat enligt äldre regler, före 2025-12-01, ska tas med när arean räknas ihop.",
       "Kommunen ger exempel: en anmäld tillbyggnad på 15 kvadratmeter enligt attefallsreglerna, ett bygglovsbefriat skärmtak på 15 kvadratmeter som skyddad uteplats och en takkupa enligt attefallsreglerna. Har huset både attefallstillbyggnaden och skärmtaket är de 30 kvadratmetrarna redan använda. Vid platsbesöket mäter vi upp allt som har byggts till och går igenom husets äldre handlingar.",
     ],
     "aside": {"title": "Räknas in enligt kommunen", "items": [
       "Anmäld tillbyggnad 15 m²", "Skärmtak 15 m²", "Takkupa enligt attefall"]}},
    {"id": "plan-norrtalje", "h2": "Fritidshuset och detaljplanen",
     "paras": [
       "En lovfri tillbyggnad på ett enbostadshus eller fritidshus får strida mot detaljplanen, skriver kommunen. Gäller tillbyggnaden en annan typ av byggnad måste den följa planen. Bygglov krävs om fastigheten ligger inom ett särskilt värdefullt område, och om tillbyggnaden placeras närmare än 4,5 meter från gränsen utan att grannen skriftligen har medgett det. Mot allmän plats inom detaljplan är det huvudmannen för platsen som kan lämna medgivandet.",
       "När en tillbyggnad kräver bygglov prövas den olika beroende på var fastigheten ligger. Inom detaljplan prövas om åtgärden stämmer med planen. Utanför detaljplan kan riksintressen för kulturmiljövård, naturvård, friluftsliv, åkermark eller buller påverka prövningen, och kommunen behöver utreda att vatten och avlopp går att lösa. I kommunens karta finns lager för detaljplan, totalförsvar, särskilt värdefulla områden och strandskydd.",
     ],
     "aside": None},
    {"id": "strand-norrtalje", "h2": "Strandskyddet gäller även lovfritt",
     "paras": [
       "Strandskyddet förbjuder bland annat att uppföra byggnader eller tillbyggnader, ändra användningen av byggnader, fälla träd och schakta eller fylla ut inom det skyddade området. Det gäller generellt 100 meter från strandlinjen, och i vissa områden i Stockholms län är det utökat till 300 meter. Norrtälje kommun påpekar att även bygglovsfria åtgärder kan kräva strandskyddsdispens.",
       "Ligger fastigheten inom ett område med landskapsbildsskydd, vanligast kring kyrkor, till exempel på Arholma, prövar Länsstyrelsen dispensen och du ansöker direkt där. Till en dispensansökan vill kommunen ha fotografier på platsen och från platsen mot huvudbyggnaden. Vi tar fram ritningarna och bilderna samtidigt, så att båda ansökningarna kan skickas tillsammans.",
     ],
     "aside": {"title": "Inom strandskyddet", "items": [
       "Dispens även för lovfritt", "100 m, ibland 300 m",
       "Landskapsbildsskydd – Länsstyrelsen", "Foton på och från platsen"]}},
    {"id": "besked-norrtalje", "h2": "Bindande besked kräver frivilligt lov",
     "paras": [
       "Kommunen ger allmän rådgivning om bygglov och regler, men skriver att den inte kan bedöma enskilda åtgärder via e-post eller telefon. Vill du ha ett bindande besked om att just din tillbyggnad inte kräver lov behöver du söka frivilligt bygglov, så att byggnadsnämnden gör en formell prövning.",
       "Anmälan kan krävas även när lov inte behövs, till exempel för installation eller ändring av eldstad, rökkanal, ventilation eller hiss och vid ändring i byggnadens brandskydd. Om nya fristående hus på tomten kan du läsa under " + _L.format("attefallshus-norrtalje.html", "attefallshus i Norrtälje") + ", och om nya hus och större projekt under " + _L.format("byggforetag-norrtalje.html", "byggföretag i Norrtälje") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad i Norrtälje",
  "steps": [
    ("Platsbesök", "Tidigare tillbyggnader, skärmtak och takkupor mäts upp."),
    ("Kartan", "Detaljplan, särskilt värdefulla områden, totalförsvar och strandskydd."),
    ("Skiss", "Tillbyggnaden ritas efter huset och tomten."),
    ("Ansökningar", "Frivilligt lov, bygglov och strandskyddsdispens vid behov."),
    ("Byggnation", "Grund, stomme, tak och anslutningen mot huset."),
    ("Slutbesked", "Tillbyggnaden används när slutbeskedet har kommit."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Norrtälje",
  "rot": [_ROT_BASE, _ROT_TB],
  "price_h2": "Vad påverkar kostnaden i Norrtälje?",
  "price": [
    "Tillbyggnadens storlek, grund på berg eller lera, transporter till en ö eller en tomt utan väg, anslutningen mot taket och om lov eller dispens behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Räknas vår attefallstillbyggnad från 2018 när vi bygger till i Norrtälje?",
     "Ja. Kommunen skriver att alla tidigare bygglovsfria åtgärder ska tas med, även sådana som var lovbefriade enligt äldre regler före 2025-12-01."),
    ("Kan Norrtälje kommun svara per e-post om vår tillbyggnad kräver lov?",
     "Kommunen ger allmän rådgivning men bedömer inte enskilda åtgärder via e-post eller telefon. Ett bindande besked kräver frivilligt bygglov."),
    ("Vem prövar strandskyddsdispens på Arholma?",
     "Inom områden med landskapsbildsskydd, som på Arholma, är det Länsstyrelsen som prövar ansökan om strandskyddsdispens."),
    ("Får en lovfri tillbyggnad på fritidshuset strida mot detaljplanen i Norrtälje?",
     "Ja, för ett enbostadshus eller fritidshus. Gäller tillbyggnaden en annan typ av byggnad måste den följa detaljplanen."),
  ],
  "sources": [_NOR_LOV, _NOR_SKI, _NOR_STR, _BV_TB, _PBL, _SKV_JOB, _SKV_ROT],
  "cta": ("Vill ni bygga till i Norrtälje?", "Boka ett gratis platsbesök, så går vi igenom det som redan är byggt och vad som gäller för tomten."),
  "img": [
    ("Rödmålat fritidshus med vita knutar och en ny tillbyggnad nära en havsvik",
     "falu red Swedish wooden summer house with white corner boards and a new single-storey extension in matching cladding, on a rocky plot near a Baltic sea inlet with pines and junipers, Roslagen archipelago, summer daylight" + _SFX),
    ("Äldre skärmtak och en tidigare tillbyggnad på baksidan av ett trähus",
     "back side of a Swedish wooden house with an older small extension and a timber roof canopy over a patio, measuring tape and folding ruler on the deck, overcast daylight" + _SFX),
    ("Strandlinje med vass och klippor nedanför en tomt med ett trähus",
     "shoreline with reeds and smooth granite rocks below a sloping plot with a red wooden house among pines, calm sea, Roslagen coast, soft evening light" + _SFX),
  ],
},

# ------------------------------------------------------------------ VALLENTUNA
"tillbyggnad-vallentuna.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Vallentuna", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Vallentuna – ritningar, nivåer och arkivet",
  "description": "Tillbyggnad i Vallentuna: regler för lovfri tillbyggnad, sektion genom hus och tillbyggnad, ramp eller hiss vid nivåskillnad och ritningar ur arkivet.",
  "h1": "Tillbyggnad i Vallentuna",
  "lead": "Vallentuna kommun beskriver en tillbyggnad som att du ökar byggnadens volym uppåt, nedåt eller åt sidan. Kommunen har också tydliga krav på hur ritningarna ska se ut, och de flesta villors gamla ritningar finns i ett digitalt arkiv. Geal Entreprenad AB bygger till villor i hela Vallentuna och börjar med husets egna handlingar.",
  "card": "Ritningar, nivåer och arkivet.",
  "sections": [
    {"id": "regler-vallentuna", "anchor": "Lovfritt",
     "h2": "Kommunens regler för en lovfri tillbyggnad",
     "paras": [
       "Enligt kommunen får en lovfri tillbyggnad vara högst 30,0 kvadratmeter i bruttoarea eller öppenarea, och alla tidigare och nya bygglovsbefriade tillbyggnader på huset får tillsammans inte överstiga 30 kvadratmeter. Tillbyggnaden får inte vara högre än den befintliga byggnadens taknock och ska ligga minst 4,5 meter från tomtgränsen mot granne, samfällighet eller allmän platsmark som gata och park. Vill du bygga närmare krävs skriftligt medgivande från berörda grannar.",
       "Kommunen skriver också att bygglov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område, och att anmälan och startbesked krävs om vatten och avlopp eller ventilation installeras samtidigt som tillbyggnaden görs. Enligt Boverket kan anmälan även krävas om husets bärande delar eller brandskydd påverkas väsentligt.",
     ],
     "aside": {"title": "Lovfritt i Vallentuna", "items": [
       "Högst 30 m² sammanlagt", "Inte över taknocken",
       "Minst 4,5 m från gräns", "Ej i särskilt värdefullt område"]}},
    {"id": "ritningar-vallentuna", "h2": "Ritningarna kommunen vill se",
     "paras": [
       "Behövs bygglov ska ansökan ha en situationsplan i skala 1:500 och plan-, fasad- och sektionsritningar i 1:100. Fasadritningarna visar berörda fasader och vad som är befintligt och vad som är nytt. Sektionen ska gå genom både det befintliga huset och tillbyggnaden. Material och kulörer redovisas med NCS-koder, och en kontrollplan ska följa med.",
       "Kommunen ställer krav på kvaliteten: ritningsnummer och datum så att versioner kan skiljas åt, alla mått i millimeter, norrpil på situationsplanen och ritningar som är fackmannamässigt utförda på vitt olinjerat papper. Planritningarna ska vara möblerade så att tillgängligheten kan granskas. Vi tar fram hela ritningsunderlaget och följer kommunens krav.",
     ],
     "aside": None},
    {"id": "nivaer-vallentuna", "h2": "Nivåskillnader, buller och kulturvärden",
     "paras": [
       "En detalj i kommunens krav är lätt att missa: finns det höjdskillnader mellan det befintliga huset och tillbyggnaden ska ramp eller hiss finnas. På en sluttande tomt, eller när golvet i tillbyggnaden hamnar lägre än i huset, avgör det hur grunden och golvnivåerna ska planeras. Vi mäter nivåerna vid platsbesöket och ritar golvet efter dem.",
       "Kommunen beskriver också handlingar som kan behövas efter en första granskning. En bullerutredning behövs om gällande bullerriktvärden överskrids på fastigheten. En antikvarisk utredning behövs om byggnaden har höga kulturhistoriska värden. Uppgifter om kontrollansvarig gäller främst större tillbyggnader.",
     ],
     "aside": {"title": "Kan behövas", "items": [
       "Bullerutredning", "Antikvarisk utredning", "Kontrollansvarig vid större projekt"]}},
    {"id": "arkivet-vallentuna", "h2": "Husets gamla ritningar i bygglovsarkivet",
     "paras": [
       "I Vallentunas digitala bygglovsarkiv finns ritningar över byggnader uppförda ungefär mellan 1950 och 2024, och cirka 75 procent av handlingarna är digitaliserade. Där finns fasad-, plan- och sektionsritningar och situationsplaner, alla i skala 1:100. Du söker på adress eller fastighetsbeteckning. Fastighetsbeteckningen hittar du i kommunkartan under Bygga, bo och miljö. Ritningar som inte finns digitalt kan beställas: ärenden äldre än fem år från arkivet, pågående och nyare ärenden från bygglovsavdelningen. Observera att arkivet bara visar avslutade och arkiverade ärenden.",
       "Sektionsritningen visar bland annat våningshöjder och takfall, och det gör det lättare att planera hur tillbyggnaden ska anslutas till huset. Om villans tak och fönster kan du läsa under " + _L.format("takrenovering-vallentuna.html", "takrenovering i Vallentuna") + " och " + _L.format("fonsterrenovering-vallentuna.html", "fönsterrenovering i Vallentuna") + ", och om större byggprojekt under " + _L.format("byggforetag-vallentuna.html", "byggföretag i Vallentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras en tillbyggnad i Vallentuna",
  "steps": [
    ("Arkivet", "Husets gamla ritningar hämtas från bygglovsarkivet."),
    ("Platsbesök", "Nivåer, avstånd och tidigare tillbyggnader mäts in."),
    ("Skiss", "Golvnivåer, takanslutning och placering ritas."),
    ("Ritningar", "Situationsplan 1:500 och plan, fasad och sektion 1:100."),
    ("Lov eller anmälan", "Bygglov, frivilligt lov eller anmälan för installationer."),
    ("Byggnation", "Grund, stomme, tak och anslutningen mot huset."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Vallentuna",
  "rot": [_ROT_BASE, _ROT_TB],
  "price_h2": "Vad påverkar kostnaden i Vallentuna?",
  "price": [
    "Tillbyggnadens storlek, grunden och golvnivåerna, en ramp eller annan lösning för nivåskillnader, anslutningen mot taket och om bygglov behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför kräver Vallentuna kommun ramp i tillbyggnaden?",
     "Kommunen skriver att ramp eller hiss ska finnas om det finns höjdskillnader mellan det befintliga huset och tillbyggnaden."),
    ("Var hittar vi ritningar till vår villa i Vallentuna?",
     "I kommunens digitala bygglovsarkiv, som har ritningar för byggnader från ungefär 1950–2024. Det som inte är digitaliserat kan beställas från arkivet."),
    ("När behövs en bullerutredning för en tillbyggnad i Vallentuna?",
     "Om gällande bullerriktvärden överskrids på fastigheten. Behovet avgörs vid kommunens första granskning av ärendet."),
    ("Vad gäller om ritningarna till Vallentuna är större än A3?",
     "Då ska en extra omgång av samtliga ritningar skickas in i A3-format, och handlingar i större format ska vara nedvikta till A4."),
    ("Vilken skala ska situationsplanen ha i Vallentuna?",
     "Skala 1:500. Plan-, fasad- och sektionsritningar görs i 1:100, och situationsplanen ska ha norrpil."),
  ],
  "sources": [_VAL_TB, _VAL_ARK, _BV_TB, _PBL, _SKV_JOB, _SKV_ROT],
  "cta": ("Vill ni bygga till i Vallentuna?", "Boka ett gratis platsbesök, så går vi igenom ritningarna och nivåerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Vit villa med en lägre tillbyggnad på en gräsbevuxen tomt med björkar",
     "1980s Swedish wooden villa with light grey board cladding on a gently sloping lawn, a new single-storey extension stepping slightly down with the terrain, large windows, birch trees, Uppland suburb, clear daylight" + _SFX),
    ("Gamla ritningar och en tumstock på ett bord",
     "old architectural paper drawings of a house section and floor plan spread on a wooden table with a folding ruler and pencil, soft window light, no readable text" + _SFX),
    ("Ljus tillbyggnad med nivåskillnad mellan golven mot det befintliga huset",
     "interior of a bright new Swedish house extension with light oak flooring and a short gentle wooden ramp connecting it to the slightly higher floor level of the existing house, white walls, daylight from large windows" + _SFX),
  ],
},
}
