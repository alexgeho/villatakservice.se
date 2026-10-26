# -*- coding: utf-8 -*-
"""Takbyte – ortsidor v28: Enskede, Kista, Skärholmen, Solna, Sundbyberg, Kungsholmen (Stora Essingen) (2026-10-27).
Hubb: takbyte.html (TJ_HUB["takbyte"]). Intent som tj_v21/v22/v24_takbyte.py: byte av hela taktäckningen med regler,
kontroll och ROT – skild från ortens takrenovering-<ort>.html, taklaggare-<ort>.html och platslagare-<ort>.html.
Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.

Lokal vinkel per sida:
Enskede – takfallet, höjden och proportionerna i riksintresset Gamla Enskede (AB 112: enhetlig utformning vad gäller
  proportioner, takfall samt tak- och fasadmaterial; olämpligt att bygga på en våning), Boverket om proportioner och
  takkupor som karaktärsdrag och om tillbyggnad som ökad volym, Varsam-tabellen (Gamla Enskede, Enskededalen,
  Enskedefältet), tilläggsisolering utan att ändra takets höjd.
Kista – platta tak och svagt lutande pulpettak i de storskaliga stadsdelarnas småhus (Varsam), Kista byggt 1975–1980
  med omkring 780 småhus (Stockholms spår), ägarformer i Kista och Akalla (områdesfakta 2025), detaljplanen och äldre
  handlingar i Bygg- och plantjänsten, bostadsrätt och ROT för gemensamma ytor.
Skärholmen – egna radhus: alla småhus i stadsdelsområdet ägs med äganderätt (områdesfakta 2025), Bredäng 1962 och
  Sätra (Varsam), Bredäng som kulturhistoriskt värdefull miljö, enhetlig färgsättning och husgrupper, souterräng.
Solna – gatusidan och gårdssidan: Solnas regler för fasadändring (tak som inte vetter mot allmän plats, alltid lov i
  särskilt värdefulla områden och i detaljplan som kräver det), anmälan om åtgärden påverkar konstruktionen (tyngre
  takmaterial), handlingar (material- och kulörbeskrivning, foton där grannfastigheter syns), kulturmiljöerna med
  småhus i Solnas lista (villor i norra Råsunda, Solna kyrkby och radhusbebyggelse, radhus i kv Fyrväpplingen).
Sundbyberg – byggarbetsplatsen: Sundbybergs sida om byggetablering (egen fastighet i första hand, polistillstånd på
  stadens mark, tidsbegränsat bygglov för bodar och upplag), grannar (meddelande vid lov, överklagande inom tre veckor),
  utökad lovplikt i Duvbo och solceller som alltid kräver bygglov.
Kungsholmen – villorna på Stora Essingen: villastad och kulturhistoriskt värdefull miljö (Varsam-tabellen), 314 småhus
  varav 268 med äganderätt (områdesfakta 2025), villastädernas individuella hus med takkupor (Varsam), Stadsmuseets
  karta och samma material som underhåll (Boverket).

Fakta endast från källorna i respektive 'sources', öppnade med urllib (Mozilla-UA) 2026-10-27, alla 200 utom
Skatteverket (återställd anslutning härifrån – samma adresser och samma ROT-meningar som i v23–v25). Pdf:erna
(Varsam, riksintresse-pdf, områdesfakta, Stockholms spår, Duvbos miljöprogram) har textlager.
Strukna / ej använda: avgifter, handläggningstider, vikter för takmaterial (ingen källa – skrivet som fråga för
konstruktör), att en viss förening har taket i stadgarna, priser, garantier, omdömen, egna uppdrag i orterna och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no hands, no text, no letters"

_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_RIKS = ("Stockholms stad – Översiktsplan, riksintressen (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"
_STH_FAS = ("Stockholms stad – Fasadändring", _SB + "fasadandring/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_BV_FAS = ("Boverket – Fasadändring (PBL kunskapsbanken)",
           "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 och 12 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SOL = "https://www.solna.se/bygga-bo--miljo/"
_SBG = "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/"

_ROT_AMT = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
            "tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.")
_ROT_SMAHUS = ("Skatteverket räknar byte och reparation av takpannor och hängrännor på ett småhus som rotarbete, när du "
               "äger och bor i huset eller har det som fritidshus.")

PAGES_TJ = {

# ------------------------------------------------------------------ ENSKEDE
"takbyte-enskede.html": {
  "kind": "district", "service": "takbyte", "ort": "Enskede", "svc_label": "Takbyte",
  "title": "Takbyte i Enskede – takfallet, höjden och riksintresset",
  "description": "Takbyte i Enskede: takfall, höjd och material i riksintresset Gamla Enskede, tilläggsisolering som ändrar proportionerna och Varsams värdefulla miljöer.",
  "h1": "Takbyte i Enskede",
  "lead": "När taket på ett hus i Gamla Enskede ska bytas är det lätt att bara tänka på pannorna. Men i riksintresset räknas också takets lutning, höjd och proportioner, och just de kan ändras om taket byggs upp tjockare än förut. Geal Entreprenad AB byter tak på villor och radhus i Enskede och planerar bytet så att husets form står kvar.",
  "card": "Takfallet, höjden och riksintresset.",
  "sections": [
    {"id": "riksintresset-enskede", "anchor": "Riksintresset",
     "h2": "Vad riksintresset räknar med",
     "paras": [
       "Gamla Enskede började byggas 1908 som Stockholms första trädgårdsstad och är riksintresse för kulturmiljövården (AB 112). I stadens beskrivning av riksintresset räknas bebyggelsens enhetliga utformning vad gäller proportioner, takfall samt tak- och fasadmaterial upp som ett värdebärande karaktärsdrag. De enskilda husens detaljer skapar variationen, men formen och materialen håller ihop gatan.",
       "Staden skriver också att det nästan undantagslöst är olämpligt att bygga på ett hus med en våning till vid en gata som i övrigt präglas av lägre hus, och att tillbyggnader i första hand bör göras mot gården. För ett takbyte betyder det att taket helst ska se ut som förut från gatan, även när allt under pannorna är nytt.",
     ],
     "aside": {"title": "Gamla Enskede (AB 112)", "items": [
       "Började byggas 1908", "Riksintresse för kulturmiljövården", "Takfall och takmaterial räknas"]}},
    {"id": "hojden-enskede", "h2": "När taket blir tjockare",
     "paras": [
       "Många ägare vill passa på att isolera när taket ändå är av. Läggs isoleringen ovanpå råsponten höjs takfoten och nocken, och vindskivor och takutsprång får en annan dimension. Boverket nämner form, storlek och proportioner bland de egenskaper som ger en byggnad dess karaktär, och en ändring som påverkar dem kan kräva bygglov som fasadändring.",
       "Boverket definierar dessutom en tillbyggnad som en ändring som ökar byggnadens volym, och en sådan åtgärd prövas då som tillbyggnad och inte som fasadändring. Vill du isolera bättre går vi därför igenom om det kan göras inifrån, från vinden, så att takets yttre mått blir desamma. Om det inte går tar vi med frågan till staden innan arbetet planeras.",
     ],
     "aside": {"title": "Kan påverka karaktären", "items": [
       "Högre takfot eller nock", "Grövre vindskivor", "Nya takkupor", "Annat takmaterial"]}},
    {"id": "omradena-enskede", "h2": "Enskededalen, Enskedefältet och Enskede gård",
     "paras": [
       "Stadens strategi för småhusområden, Varsam, har en tabell över områdena. Där är Gamla Enskede markerat som riksintresse, kulturhistoriskt värdefull miljö, område med äldre miljöprogram och område med generösa byggrätter. Enskededalen är markerat som kulturhistoriskt värdefull miljö med äldre miljöprogram, och Enskede gård som kulturhistoriskt värdefull miljö.",
       "Enskedefältet finns i samma tabell som småstugeområde, också det kulturhistoriskt värdefullt och med äldre miljöprogram. Stockholms stad påpekar att utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla områden och att Stadsmuseets klassificeringskarta ger en första indikation. Vi tittar på kartan för din fastighet innan materialet bestäms.",
     ],
     "aside": {"title": "I Varsam-tabellen", "items": [
       "Gamla Enskede: riksintresse", "Enskededalen: värdefull miljö", "Enskede gård: värdefull miljö", "Enskedefältet: värdefull miljö"]}},
    {"id": "materialet-enskede", "h2": "Samma material är underhåll",
     "paras": [
       "Boverket skiljer mellan att byta till ett annat taktäckningsmaterial, som räknas som fasadändring, och att lägga samma material och utförande igen, som räknas som underhåll. Ett takbyte där rött lertegel ersätts med rött lertegel i samma utförande är alltså underhåll, och det är också det säkraste valet i en miljö där takmaterialet är ett av karaktärsdragen.",
       "Om ditt tak redan har bytts till ett annat material en gång kan det finnas skäl att gå tillbaka till originalet. Staden skriver att det är av stort värde när kraftigt förändrade byggnader kan återställas så att de smälter in bättre i stadsmiljön. Om tegeltyper och de olika hustyperna i Enskede kan du läsa under " + _L.format("takrenovering-enskede.html", "takrenovering i Enskede") + ".",
     ],
     "aside": None},
    {"id": "underlaget-enskede", "h2": "Från ritning till ny takfot",
     "paras": [
       "Innan det gamla taket rivs mäter och fotograferar vi takfot, vindskivor, nock och plåtdetaljer, så att samma mått och profiler kan läggas tillbaka. Det är ofta vid takfoten som ett nytt tak syns från gatan, och därför ägnar vi den detaljen extra tid.",
       "Under pannorna ser vi över läkt, underlagstäckning och råspont, och skadat trä byts innan det nya taket läggs. Om tjänsten i stort kan du läsa under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Enskede till",
  "steps": [
    ("Kartan och planen", "Riksintresse, klassning och detaljplan kontrolleras för fastigheten."),
    ("Platsbesök", "Takfall, takfot, vindskivor och nuvarande material går vi igenom."),
    ("Isoleringsfrågan", "Vi bedömer om isoleringen kan läggas inifrån utan att takets mått ändras."),
    ("Skriftligt kostnadsförslag", "Material, underlag och plåtarbeten redovisas var för sig."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs med samma profiler."),
    ("Genomgång", "Vi går igenom taket och detaljerna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Enskede",
  "rot": [_ROT_SMAHUS, _ROT_AMT],
  "price_h2": "Vad påverkar priset för takbytet i Enskede?",
  "price": [
    "Takets yta och lutning, val av tegel, hur mycket underlag som behöver bytas, takfotens detaljer och om isoleringen ska förbättras inifrån. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi isolera taket ovanpå råsponten på vårt hus i Gamla Enskede?",
     "Det beror på hur mycket takets höjd och proportioner ändras. Takfall och proportioner räknas som karaktärsdrag i riksintresset, så vi undersöker först om isoleringen kan läggas inifrån och tar frågan till staden om takets mått skulle ändras."),
    ("Kan ett tjockare tak räknas som tillbyggnad?",
     "Boverket definierar tillbyggnad som en ändring som ökar byggnadens volym. Höjs taket så att volymen ökar kan åtgärden därför prövas som tillbyggnad."),
    ("Är Enskededalen också kulturhistoriskt värdefullt?",
     "Ja, i stadens strategi Varsam är Enskededalen markerat som kulturhistoriskt värdefull miljö med äldre miljöprogram."),
    ("Kan vi gå tillbaka till lertegel om taket bytts till plåt tidigare?",
     "Ja, och staden skriver att det är av stort värde när kraftigt förändrade hus återställs så att de smälter in bättre. Eftersom det är ett materialbyte kontrollerar vi lovfrågan först."),
  ],
  "sources": [_RIKS, _VARSAM, _BV_FAS, _STH_FAS, _STH_KL, _SKV, _SKV2],
  "cta": ("Ska taket i Enskede bytas?", "Boka ett gratis platsbesök, så går vi igenom takfall, takfot och isolering innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nationalromantisk villa med brant tegeltak bakom en häck",
     "early 1900s Swedish national romantic garden city villa with steep red clay tile gable roof, small dormer, dark wooden panel and white window frames, clipped hedge in front, curving residential street with mature trees, Stockholm, summer" + _IMG_END),
    ("Takfot och vindskiva på ett tegeltak i närbild",
     "close view of the eaves and bargeboard of an old Swedish villa with red clay roof tiles, painted wooden bargeboard and simple metal gutter, showing the thin roof edge profile, daylight" + _IMG_END),
    ("Vind med ny lösull på bjälklaget under taket",
     "interior of an empty attic of an old wooden house with mineral wool insulation fitted between the rafters under the roof boards, light from a small gable window, tidy and dry, no tools in use" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ KISTA
"takbyte-kista.html": {
  "kind": "district", "service": "takbyte", "ort": "Kista", "svc_label": "Takbyte",
  "title": "Takbyte i Kista – platta tak och pulpettak från 1970-talet",
  "description": "Takbyte i Kista: småhus från 1975–1980 med platta tak och pulpettak, ägarformer i Kista och Akalla och de gamla ritningarna i Bygg- och plantjänsten.",
  "h1": "Takbyte i Kista",
  "lead": "Småhusen i Kista och Akalla har ofta tak som inte syns från gatan: platta tak eller svagt lutande pulpettak. Ett sådant tak byts inte med pannor utan med en tätskiktslösning, och det ställer andra krav än ett vanligt sadeltak. Geal Entreprenad AB byter tak på radhus, kedjehus och villor i Kista och tar reda på hur taket är uppbyggt innan något rivs.",
  "card": "Platta tak och pulpettak.",
  "sections": [
    {"id": "stadsdelen-kista", "anchor": "Stadsdelen",
     "h2": "En stadsdel byggd på fem år",
     "paras": [
       "Staden köpte marken på Järvafältet 1966, och enligt Stadsmuseets skrift i serien Stockholms spår byggdes Kista ut åren 1975–1980. Staden tillämpade här betydligt friare former för den arkitektoniska utformningen än i de övriga stadsdelarna på Järvafältet. Bebyggelsen bestod av 2 500 lägenheter i flerbostadshus och omkring 780 småhus.",
       "I stadens strategi för småhusområden, Varsam, räknas Akalla och Husby till de storskaliga stadsdelarna. Där beskrivs småhusen som huvudsakligen radhus och kedjehus, men också villor och atriumhus, med Akalla som ett av exemplen.",
     ],
     "aside": {"title": "Kista enligt Stockholms spår", "items": [
       "Utbyggt 1975–1980", "Omkring 780 småhus", "Tunnelbanan invigd 1975"]}},
    {"id": "taken-kista", "h2": "Tak som är platta eller svagt lutande",
     "paras": [
       "Varsam skriver att taken på de storskaliga stadsdelarnas småhus ofta var platta eller utformade som svagt lutande pulpettak, även om det också förekommer sadeltak med brant takfall. På ett tak med låg lutning rinner vattnet långsamt, och det är tätskiktet, anslutningarna och avvattningen som avgör hur länge taket håller.",
       "När ett sådant tak byts går vi igenom brunnar, rännor, anslutningar mot uppstickande ventilation och skarvarna mot grannhusen i längan. Varsam påpekar också att färgsättningen var enhetlig inom husgrupperna och att de gruppbyggda husen står på små tomter, så ett tak som syns från gångvägen ska passa in i gruppen.",
     ],
     "aside": {"title": "Varsam om småhusen", "items": [
       "Radhus, kedjehus, villor och atriumhus", "Platta tak eller pulpettak", "Enhetliga husgrupper", "Små tomter"]}},
    {"id": "agarna-kista", "h2": "Äganderätt eller förening",
     "paras": [
       "Stadens områdesfakta för 2025 visar att småhusen i Kista ägs på olika sätt. I stadsdelen Kista finns 482 småhus med äganderätt och 404 i bostadsrätt. I Akalla är fördelningen den omvända: 170 småhus med äganderätt och 493 i bostadsrätt. I Husby finns enligt samma statistik inga småhus alls.",
       "Bor du i ett radhus i bostadsrätt avgör stadgarna vem som svarar för taket. Bostadsrättslagen utgår från att du håller lägenheten i gott skick om inte stadgarna säger annat, och ingrepp i bärande konstruktion kräver styrelsens tillstånd. Därför börjar vi med att reda ut vem som beställer.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Kista: 482 äganderätt, 404 bostadsrätt", "Akalla: 170 äganderätt, 493 bostadsrätt", "Husby: inga småhus"]}},
    {"id": "planen-kista", "h2": "Detaljplanen och de gamla ritningarna",
     "paras": [
       "Stockholms stad påpekar att en fasadändring som inte kräver bygglov ändå ska stämma med detaljplanen, och att detaljplanen kan innehålla bestämmelser som skyddar ett område eller kräver lov för åtgärder som annars är lovfria. Detaljplanen för fastigheten finns i stadens e-tjänst Bygg- och plantjänsten.",
       "I samma e-tjänst kan du själv leta fram äldre handlingar som stadsbyggnadskontoret har för fastigheten. För ett platt tak från 1970-talet är ritningarna värdefulla, eftersom de visar hur takets lutning, isolering och avvattning var tänkta från början. Vi använder dem som underlag när vi beskriver det nya taket.",
     ],
     "aside": None},
    {"id": "materialet-kista", "h2": "Samma utförande eller ett nytt",
     "paras": [
       "Boverket räknar ett byte till annat taktäckningsmaterial som en fasadändring, medan samma material och utförande räknas som underhåll. Ska ett papptäckt pulpettak få en annan beläggning, eller ett platt tak bli ett lutande, är det alltså mer än underhåll och vi kontrollerar plan och lov först.",
       "Om takläggning i stadsdelen i stort kan du läsa under " + _L.format("taklaggare-kista.html", "takläggare i Kista") + ", och om tjänsten under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Kista till",
  "steps": [
    ("Ägarform", "Vi reder ut om du eller föreningen beställer taket."),
    ("Ritningarna", "Äldre handlingar och detaljplan hämtas ur Bygg- och plantjänsten."),
    ("Platsbesök", "Tätskikt, brunnar, rännor och anslutningar mot grannarna går vi igenom."),
    ("Skriftligt kostnadsförslag", "Uppdelat per hus eller etapp när flera tak byts."),
    ("Takbyte", "Gammalt tätskikt rivs, underlaget ses över och det nya taket läggs."),
    ("Genomgång", "Avvattning och anslutningar kontrolleras tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Kista",
  "rot": [
    _ROT_SMAHUS + " I en bostadsrätt ger arbete på gemensamma ytor som tak och fasader inget rotavdrag.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Kista?",
  "price": [
    "Takets yta, typ av tätskikt, antal brunnar och genomföringar, underlagets skick och om flera hus i längan byts samtidigt. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Var hittar jag ritningarna till vårt radhus från 1970-talet i Kista?",
     "I Stockholms stads e-tjänst Bygg- och plantjänsten kan du söka på fastigheten och själv ta fram äldre handlingar som stadsbyggnadskontoret har."),
    ("Vilka tak hade radhusen i Akalla från början?",
     "Stadens strategi Varsam skriver att småhusen i de storskaliga stadsdelarna ofta fick platta tak eller svagt lutande pulpettak, men att även branta sadeltak förekommer."),
    ("Hur många småhus i Akalla ägs av en bostadsrättsförening?",
     "Enligt stadens områdesfakta för 2025 är 493 av småhusen i Akalla bostadsrätter och 170 äganderätter."),
    ("Måste vi följa detaljplanen även om takbytet inte kräver bygglov?",
     "Ja. Stockholms stad påpekar att lovfria fasadändringar ändå ska stämma med detaljplanen eller vara en liten avvikelse som inte motverkar planens syfte."),
  ],
  "sources": [("Stockholms stadsmuseum – Stockholms spår: Kista (pdf)", "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000080.pdf"),
              _VARSAM,
              ("Stockholms stad – Områdesfakta 2025: Kista (pdf)", _OF + "vasterort/jarva/kista.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Akalla (pdf)", _OF + "vasterort/jarva/akalla.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Husby (pdf)", _OF + "vasterort/jarva/husby.pdf"),
              _BRL, _STH_FAS, _BV_FAS, _SKV, _SKV2],
  "cta": ("Ska taket på radhuset i Kista bytas?", "Boka ett gratis platsbesök, så går vi igenom tätskikt, avvattning och anslutningar innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhuslänga från 1970-talet i trä och tegel",
     "row of 1970s Swedish terraced houses with low-pitched mono-pitch roofs, brown wooden panels and yellow brick, small front yards, pedestrian path with young trees, suburban Stockholm, summer" + _IMG_END),
    ("Platt tak med nytt tätskikt och takbrunn sett ovanifrån",
     "view from above of a flat roof on a 1970s Swedish terraced house with new dark bitumen roofing membrane, a roof drain and a ventilation pipe flashing, neat metal edge trim, daylight" + _IMG_END),
    ("Takfot med ny hängränna och stuprör på ett radhus",
     "close view of the low edge of a mono-pitch roof on a 1970s house with new metal edge flashing and gutter, wooden facade panel below, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"takbyte-skarholmen.html": {
  "kind": "district", "service": "takbyte", "ort": "Skärholmen", "svc_label": "Takbyte",
  "title": "Takbyte i Skärholmen – egna radhus i Sätra och Bredäng",
  "description": "Takbyte i Skärholmen: radhus som ägs med äganderätt, Bredäng och Sätra som byggdes först, Bredäng som värdefull miljö och taket som del av husgruppen.",
  "h1": "Takbyte i Skärholmen",
  "lead": "I Skärholmens stadsdelsområde ägs nästan alla småhus med äganderätt, och inget av dem är en bostadsrätt. Det gör att du själv bestämmer över ditt tak, men på ett radhus sitter taket ihop med grannarnas och syns i hela gruppen. Geal Entreprenad AB byter tak på radhus, kedjehus och villor i Sätra, Bredäng, Vårberg och Skärholmen och planerar bytet med längan i tankarna.",
  "card": "Egna radhus i Sätra, Bredäng och Vårberg.",
  "sections": [
    {"id": "agarna-skarholmen", "anchor": "Ägarna",
     "h2": "Småhus som ägs av de boende",
     "paras": [
       "Stadens områdesfakta för 2025 visar 1 976 småhus med äganderätt i Skärholmens stadsdelsområde, 15 hyresrätter och inga småhus i bostadsrätt. Per stadsdel finns 577 småhus med äganderätt i Vårberg, 543 i Skärholmen, 536 i Sätra och 320 i Bredäng.",
       "Det skiljer Skärholmen från många andra stadsdelar med radhus från samma tid, där föreningar ofta äger husen. Här är det du som beställer, betalar och får rotavdraget, men det är ändå klokt att prata med grannarna, eftersom taken i en länga hänger ihop vid nock, takfot och gavlar.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Vårberg: 577", "Skärholmen: 543", "Sätra: 536", "Bredäng: 320"]}},
    {"id": "historien-skarholmen", "h2": "Bredäng först, sedan Sätra",
     "paras": [
       "Enligt stadens strategi för småhusområden, Varsam, var Bredäng den första stadsdelen som planerades i stor skala, med byggstart 1962, följd av Sätra. En stor andel av miljonprogrammets bebyggelse utgjordes av gruppbyggda småhus och radhus, och Sätra nämns som ett av exemplen där det också byggdes villor och atriumhus.",
       "Varsam beskriver hur nivåskillnader ofta togs upp med en souterrängvåning. På ett sådant hus är taket högre upp mot ena sidan än det ser ut från gatan, och vi planerar ställning och materialtransport efter terrängen och gångvägarna i området.",
     ],
     "aside": None},
    {"id": "bredang-skarholmen", "h2": "Bredäng som värdefull miljö",
     "paras": [
       "I Varsam-tabellen är Bredäng markerat som kulturhistoriskt värdefull miljö, medan Sätra, Skärholmen och Vårberg saknar den markeringen. Stockholms stad skriver att utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla områden, och hänvisar till Stadsmuseets klassificeringskarta som en första indikation för den enskilda fastigheten.",
       "Att byta till ett annat taktäckningsmaterial räknas enligt Boverket som fasadändring, medan samma material och utförande räknas som underhåll. I Bredäng kontrollerar vi kartan innan ett nytt material föreslås.",
     ],
     "aside": {"title": "I Varsam-tabellen", "items": [
       "Bredäng: kulturhistoriskt värdefull", "Sätra: ingen markering", "Skärholmen: ingen markering", "Vårberg: ingen markering"]}},
    {"id": "gruppen-skarholmen", "h2": "Taket är en del av husgruppen",
     "paras": [
       "Varsam beskriver de gruppbyggda småhusen som mycket enhetliga inom varje husgrupp, med variation mellan områdena, och påpekar att färgsättningen var enhetlig inom grupperna. Ett nytt tak i en avvikande kulör eller profil syns därför i hela längan.",
       "Vi föreslår material och kulör efter vad grannarna har, och när flera hus byter tak samtidigt kan ställning och avfallshantering delas. Om fasader och kulörer i stadsdelen kan du läsa under " + _L.format("fasadmalning-skarholmen.html", "fasadmålning i Skärholmen") + ".",
     ],
     "aside": None},
    {"id": "uterummet-skarholmen", "h2": "Uterum och påbyggnader mot taket",
     "paras": [
       "Varsam påpekar att de gruppbyggda småhusen står på små tomter, att påbyggnader förekommer och att mindre tillbyggnader, som inglasade uterum, är vanliga. Har ditt hus ett uterum eller en tillbyggnad ansluter dess tak ofta mot huvudtaket eller mot fasaden strax under takfoten.",
       "Den anslutningen är en vanlig plats för läckage, och vid ett takbyte ser vi över den i samma arbete. Ska även uterummets tak bytas går vi igenom det separat i kostnadsförslaget.",
     ],
     "aside": None},
    {"id": "underlaget-skarholmen", "h2": "Det vi ser när pannorna är av",
     "paras": [
       "Under pannorna ser vi över läkt, underlagstäckning och råspont, och plåten vid nock, gavlar och mot grannhuset görs om i samma arbete. Skadat trä byts innan det nya taket läggs.",
       "Om takläggning i stadsdelen i stort finns mer under " + _L.format("taklaggare-skarholmen.html", "takläggare i Skärholmen") + ", och om tjänsten under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Skärholmen till",
  "steps": [
    ("Kartan", "Vi kontrollerar Stadsmuseets karta, särskilt i Bredäng."),
    ("Platsbesök", "Taket, anslutningarna mot grannarna och terrängen runt huset går vi igenom."),
    ("Skriftligt kostnadsförslag", "Med ställning, material och plåtarbeten redovisade."),
    ("Grannarna", "Vi samordnar gärna om flera hus i längan vill byta samtidigt."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Genomgång", "Vi går igenom taket och anslutningarna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Skärholmen",
  "rot": [_ROT_SMAHUS + " Eftersom småhusen i Skärholmen ägs med äganderätt gäller avdraget i regel för den som äger och bor i huset.", _ROT_AMT],
  "price_h2": "Vad påverkar priset för takbytet i Skärholmen?",
  "price": [
    "Takets yta, material, underlagets skick, anslutningar mot grannhusen, terrängen runt huset och om flera hus byts samtidigt. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Äger jag mitt radhus i Sätra själv eller är det en förening?",
     "Enligt stadens områdesfakta för 2025 finns inga småhus i bostadsrätt i Skärholmens stadsdelsområde, och 1 976 ägs med äganderätt. Du beställer alltså i regel själv, men taket hänger ihop med grannarnas."),
    ("Vilken stadsdel i Skärholmen byggdes först?",
     "Bredäng. Stadens strategi Varsam skriver att Bredäng började byggas 1962 och var den första stadsdelen som planerades i stor skala, följd av Sätra."),
    ("Behöver jag tänka på lov om jag byter takmaterial i Vårberg?",
     "Vårberg är inte markerat som kulturhistoriskt värdefullt i Varsam, men ett nytt material är en fasadändring och ska stämma med detaljplanen. Vi kontrollerar Stadsmuseets karta och planen för fastigheten."),
    ("Varför är taket högre på baksidan av vårt hus i Bredäng?",
     "Många hus i de storskaliga stadsdelarna har souterrängvåning där marken sluttar, enligt Varsam. Det påverkar ställningen och hur materialet kommer upp på taket."),
    ('Vilka tillbyggnader är vanliga på radhusen i Skärholmen?',
     'Stadens strategi Varsam nämner mindre tillbyggnader som inglasade uterum som vanliga, och skriver att påbyggnader förekommer.'),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Skärholmens stadsdelsområde (pdf)", _OF + "soderort/skarholmen/skarholmen-stadsdelsomrade.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Vårberg (pdf)", _OF + "soderort/skarholmen/varberg.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Skärholmen (pdf)", _OF + "soderort/skarholmen/skarholmen.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Sätra (pdf)", _OF + "soderort/skarholmen/satra.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Bredäng (pdf)", _OF + "soderort/skarholmen/bredang.pdf"),
              _VARSAM, _STH_FAS, _STH_KL, _BV_FAS, _SKV, _SKV2],
  "cta": ("Ska taket på radhuset i Skärholmen bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och anslutningarna mot grannarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus från 1960-talet i sluttning med sadeltak",
     "row of 1960s Swedish terraced houses built on a slope with a lower souterrain level, gable roofs with dark concrete roof tiles, brick and painted wood facades, footpath and lawns, suburban southwest Stockholm, summer" + _IMG_END),
    ("Radhuslänga från 1960-talet med sadeltak och balkonger",
     "simple 1960s Swedish suburban terraced houses with plain low-pitched gable roofs without chimney pots or dormers, light brick and painted wood facades, metal scaffolding with guard rail along the eaves of one house during re-roofing, that roof partly stripped to the wooden roof boards, lawns and footpath, daylight, no workers, no ladders" + _IMG_END),
    ("Nylagda takpannor på ett radhustak",
     "close view of the ridge of two adjoining terraced house roofs with new dark roof tiles and a neat metal ridge and party wall flashing, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SOLNA
"takbyte-solna.html": {
  "kind": "district", "service": "takbyte", "ort": "Solna", "svc_label": "Takbyte",
  "title": "Takbyte i Solna – gatusidan, gårdssidan och konstruktionen",
  "description": "Takbyte i Solna: när nytt takmaterial kräver lov, varför takfallet mot gatan räknas, anmälan vid tyngre tak och Solnas utpekade småhusmiljöer.",
  "h1": "Takbyte i Solna",
  "lead": "I Solna hänger lovfrågan vid ett takbyte på tre saker: om huset ligger i ett värdefullt område, vad detaljplanen säger och åt vilket håll takfallet vetter. Ett tyngre takmaterial kan dessutom kräva anmälan. Geal Entreprenad AB byter tak på villor och radhus i Solna och tar fram handlingarna innan materialet beställs.",
  "card": "Gatusidan, gårdssidan och konstruktionen.",
  "sections": [
    {"id": "reglerna-solna", "anchor": "Reglerna",
     "h2": "Tre fall där Solna kräver lov",
     "paras": [
       "Solna stad skriver att du kan behöva söka bygglov för byte av taktäckningsmaterial inom detaljplan, i ett kulturhistoriskt värdefullt område eller på en kulturhistoriskt värdefull byggnad. Lov krävs i tre fall: när fasadändringen görs på en särskilt värdefull byggnad eller i ett särskilt värdefullt område, när den gäller solenergi inom detaljplan och inom eller intill riksintresse för totalförsvaret, och när detaljplanen anger att åtgärden kräver lov.",
       "Är inget av det aktuellt behövs inget lov för en fasadändring på ett en- eller tvåbostadshus, om ändringen sker på en fasad eller ett tak som inte vetter mot allmän plats. Staden påpekar också att stora delar av Solna har detaljplan.",
     ],
     "aside": {"title": "Lov krävs i Solna", "items": [
       "Särskilt värdefull byggnad eller område", "Solenergi intill riksintresse för totalförsvaret", "Detaljplanen kräver lov"]}},
    {"id": "takfallet-solna", "h2": "Takfallet mot gatan",
     "paras": [
       "Eftersom Solnas villkor för lovfrihet gäller tak som inte vetter mot allmän plats spelar det roll hur huset ligger. Ett sadeltak har ofta ett takfall mot gatan och ett mot trädgården, och ett nytt material på gatusidan bedöms då annorlunda än samma material på gårdssidan.",
       "Det enklaste är oftast att lägga samma material och utförande som förut, vilket Boverket räknar som underhåll och inte som fasadändring. Ska materialet bytas går vi igenom med dig åt vilket håll takfallen vetter och vad som gäller innan något beställs.",
     ],
     "aside": None},
    {"id": "konstruktionen-solna", "h2": "Ett tyngre tak och anmälan",
     "paras": [
       "Solna stad skriver att du behöver göra en anmälan om byggåtgärd om en fasadändring påverkar byggnadens konstruktion, brandskydd eller tekniska installationer. Ett byte från plåt eller papp till betong- eller lertegel innebär mer vikt på takstolarna, och då kan det behövas en bedömning av konstruktören.",
       "Vid en anmälan som gäller bärande delar räknar staden upp handlingar som utlåtande från konstruktör och intyg om utförd dimensioneringskontroll, och du får inte börja förrän du har fått startbesked. Vi tar upp viktfrågan tidigt, så att den inte dyker upp när materialet redan är beställt.",
     ],
     "aside": {"title": "Anmälan kan krävas", "items": [
       "Påverkad konstruktion", "Påverkat brandskydd", "Påverkade tekniska installationer", "Startbesked före arbetet"]}},
    {"id": "miljoerna-solna", "h2": "Småhusmiljöerna i Solnas lista",
     "paras": [
       "Bland de sammanhängande kulturhistoriskt värdefulla miljöerna i Solna nämner staden villabebyggelsen i norra Råsunda och Solna kyrkby med radhusbebyggelse. Bland de enskilda byggnadsminnena finns radhusen i kvarteret Fyrväpplingen. Staden har också en karta över kulturhistoriskt klassade byggnader.",
       "Om takrenovering och skyddade miljöer i Solna kan du läsa under " + _L.format("takrenovering-solna.html", "takrenovering i Solna") + ". Om tjänsten i stort finns mer under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": {"title": "Exempel ur Solnas lista", "items": [
       "Villabebyggelse i norra Råsunda", "Solna kyrkby och radhusbebyggelse", "Radhus i kv Fyrväpplingen (byggnadsminne)"]}},
    {"id": "handlingarna-solna", "h2": "Handlingarna till en ansökan",
     "paras": [
       "För en fasadändring som kräver lov räknar Solna stad upp bland annat situationsplan, material- och kulörbeskrivning och fotografier av byggnaden där även grannfastigheterna syns. I värdefulla miljöer kan en antikvarisk förundersökning eller ett utlåtande från en sakkunnig inom kulturvärden behövas.",
       "Vi fotograferar taket och grannhusen vid platsbesöket och beskriver det nya materialet och kulören, så att underlaget finns när ansökan ska skrivas.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Solna till",
  "steps": [
    ("Kartan och planen", "Detaljplan, kulturmiljö och klassning kontrolleras för fastigheten."),
    ("Platsbesök", "Takfallen, materialet och takstolarna går vi igenom och fotograferar."),
    ("Vikten", "Vid tyngre material bedöms om konstruktionen påverkas."),
    ("Skriftligt kostnadsförslag", "Material, underlag och eventuella förstärkningar för sig."),
    ("Lov eller anmälan", "Handlingarna tas fram när ändringen kräver det."),
    ("Takbyte och genomgång", "Nytt tak läggs och vi går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Solna",
  "rot": [_ROT_SMAHUS, _ROT_AMT],
  "price_h2": "Vad påverkar priset för takbytet i Solna?",
  "price": [
    "Takets yta, materialval, underlagets skick, om takstolarna behöver förstärkas och om lov eller anmälan behövs. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Spelar det roll åt vilket håll takfallet vetter när vi byter takmaterial i Solna?",
     "Ja. Solnas regel för lovfri fasadändring på villor gäller tak som inte vetter mot allmän plats, så ett takfall mot gatan kan bedömas annorlunda än ett mot trädgården."),
    ("Behöver vi göra en anmälan om vi byter från plåttak till tegel i Solna?",
     "Om bytet påverkar byggnadens konstruktion behövs en anmälan om byggåtgärd enligt Solna stad, och arbetet får inte börja före startbesked."),
    ("Vilka foton vill Solna stad ha med en ansökan om nytt takmaterial?",
     "Staden räknar upp fotografier över den befintliga byggnaden där även grannfastigheterna syns, tillsammans med bland annat material- och kulörbeskrivning."),
    ("Är radhusen i kvarteret Fyrväpplingen skyddade?",
     "Ja, Solna stad listar radhusen i kv Fyrväpplingen bland de enskilda byggnadsminnena i kommunen."),
  ],
  "sources": [("Solna stad – Fasadändring", _SOL + "bygga/guide/vanliga-byggatgarder/fasadandring"),
              ("Solna stad – Ändra bärande konstruktion", _SOL + "bygga/anmalan/andra-barande-konstruktion"),
              ("Solna stad – Kulturmiljöer i Solna", _SOL + "stadsmiljo/kulturmiljoer-i-solna"),
              _BV_FAS, _SKV, _SKV2],
  "cta": ("Ska taket i Solna bytas?", "Boka ett gratis platsbesök, så går vi igenom takfallen, materialet och konstruktionen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa med sadeltak av tegel på en villagata i Solna",
     "1920s Swedish detached villa with red clay tile gable roof facing the street, light rendered facade, white windows, garden with fruit trees and low fence, quiet residential street, Stockholm area, summer" + _IMG_END),
    ("Takstolar och råspont på en vind under ett takbyte",
     "interior view of an old attic during re-roofing, wooden rafters and roof boards visible, daylight coming through a gap where old roofing has been removed, timber stacked neatly, no people" + _IMG_END),
    ("Villa med nytt tak av falsad plåt",
     "view of a Swedish villa from a garden corner showing both slopes of the gable roof, one facing the street and one facing the garden, new metal standing seam roof, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SUNDBYBERG
"takbyte-sundbyberg.html": {
  "kind": "district", "service": "takbyte", "ort": "Sundbyberg", "svc_label": "Takbyte",
  "title": "Takbyte i Sundbyberg – container, ställning och grannar",
  "description": "Takbyte i Sundbyberg: var ställning och container får stå, polisens tillstånd på gatumark, tidsbegränsat bygglov, grannarna och reglerna i Duvbo.",
  "h1": "Takbyte i Sundbyberg",
  "lead": "Ett takbyte kräver plats på marken: ställning längs väggarna, en container för det gamla taket och en yta för det nya materialet. I Sundbyberg, där tomterna ofta är små och gatorna smala, är det just den planeringen som avgör hur smidigt arbetet går. Geal Entreprenad AB byter tak på villor och radhus i Sundbyberg och planerar byggarbetsplatsen innan arbetet startar.",
  "card": "Container, ställning och grannar.",
  "sections": [
    {"id": "etableringen-sundbyberg", "anchor": "Etableringen",
     "h2": "Allt som ska stå på marken",
     "paras": [
       "Sundbybergs stad kallar de tillfälliga funktionerna under byggtiden för byggetablering: byggbodar, containrar för material och verktyg och stängsel eller plank som inhägnar området. Staden skriver att etableringen bör placeras i anslutning till byggarbetsplatsen och på den egna fastigheten om det går.",
       "Vid ett takbyte på en villa räcker det oftast med ställning längs huset och en container på tomten. Vi mäter upp var containern kan stå så att bilen kan tömma den, och var nytt material kan läggas utan att trädgården skadas.",
     ],
     "aside": {"title": "Byggetablering enligt staden", "items": [
       "Byggbodar", "Containrar för material", "Stängsel eller plank", "Helst på egen fastighet"]}},
    {"id": "gatan-sundbyberg", "h2": "När containern måste stå på gatan",
     "paras": [
       "Om etableringen måste stå på någon annans mark behövs fastighetsägarens tillstånd. Ägs marken av Sundbybergs stad, till exempel gatumark eller parkmark, skriver staden att du behöver söka tillstånd från polisen för att placera byggetableringen där. Ska stadens mark användas till något den normalt inte är avsedd för kan det också behövas tillstånd för markupplåtelse.",
       "Byggbodar kräver tidsbegränsat bygglov, och beroende på läge och storlek kan även upplag för byggmaterial kräva lov. Eftersom etableringen ofta strider mot detaljplanen kan staden behöva höra grannarna. Vid ett vanligt villatak försöker vi därför hålla allt på tomten.",
     ],
     "aside": {"title": "Tillstånd som kan behövas", "items": [
       "Polisens tillstånd på stadens mark", "Markupplåtelse", "Tidsbegränsat bygglov för bodar", "Lov för vissa upplag"]}},
    {"id": "grannarna-sundbyberg", "h2": "Vad grannarna får veta",
     "paras": [
       "Sundbybergs stad skriver att det inte finns någon generell rätt för grannar att tycka till om allt som byggs. När staden ger bygglov skickar den däremot ett meddelande till berörda grannar, som då kan överklaga beslutet skriftligt inom tre veckor från den dag de fick det.",
       "Om en ansökan om bygglov inte följer detaljplanen ska grannar och andra berörda enligt staden få lämna synpunkter genom ett grannehörande. Följer ärendet helt detaljplanen fattas beslutet utan att grannarna hörs. Ett takbyte med samma material kräver normalt inget lov, och då får grannarna inget meddelande. Vi tycker ändå att det är bra att berätta när ställningen kommer upp och när containern hämtas, eftersom arbetet hörs och syns.",
     ],
     "aside": None},
    {"id": "duvbo-sundbyberg", "h2": "I Duvbo gäller andra regler",
     "paras": [
       "Sundbybergs stad skriver att lovplikten för fasadändringar är utökad i Duvbo och för kulturhistoriskt värdefulla byggnader, och att det där för det mesta krävs bygglov. Duvbos miljöprogram räknar utbyte av takläggningsmaterial bland de åtgärder som omfattas av den utökade lovplikten. Utanför Duvbo krävs inte längre bygglov för fasadändringar på en- eller tvåbostadshus, så länge byggnaden inte är kulturhistoriskt värdefull.",
       "Solcellspaneler kräver däremot bygglov i hela Sundbyberg, enligt staden. Om tak och plåt i Duvbo kan du läsa mer under " + _L.format("platslagare-sundbyberg.html", "plåtslagare i Sundbyberg") + ".",
     ],
     "aside": {"title": "Lov i Sundbyberg", "items": [
       "Duvbo: utökad lovplikt", "Värdefulla byggnader: utökad lovplikt", "Solceller: kräver bygglov"]}},
    {"id": "arbetet-sundbyberg", "h2": "Arbetet på taket",
     "paras": [
       "När ställningen står och containern är på plats rivs det gamla taket i etapper, så att huset inte står öppet längre än nödvändigt. Läkt, underlagstäckning och råspont ses över, och skadat trä byts innan det nya taket läggs.",
       "Om takläggning i Sundbyberg i stort finns mer under " + _L.format("taklaggare-sundbyberg.html", "takläggare i Sundbyberg") + ", och om tjänsten under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Sundbyberg till",
  "steps": [
    ("Platsbesök", "Taket, tomten och tillfarten går vi igenom tillsammans."),
    ("Etableringen", "Vi planerar var ställning, container och material ska stå."),
    ("Tillstånd", "Behövs gatumark tar vi upp frågan om polisens tillstånd i tid."),
    ("Skriftligt kostnadsförslag", "Etablering, material och arbete redovisas var för sig."),
    ("Takbyte", "Gammalt tak rivs i etapper och nytt tak läggs."),
    ("Genomgång och bortforsling", "Vi går igenom taket och tar bort etableringen."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Sundbyberg",
  "rot": [_ROT_SMAHUS, _ROT_AMT],
  "price_h2": "Vad påverkar priset för takbytet i Sundbyberg?",
  "price": [
    "Takets yta och material, underlagets skick, hur ställning och container kan placeras och om tillstånd för gatumark behövs. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får containern för det gamla taket stå på gatan i Sundbyberg?",
     "Bara med tillstånd. Sundbybergs stad skriver att placering av byggetablering på stadens mark, till exempel gatumark, kräver tillstånd från polisen."),
    ("Behövs bygglov för en byggbod under takbytet?",
     "Ja, enligt Sundbybergs stad kräver tillfälliga byggbodar tidsbegränsat bygglov. Vid ett villatak brukar ingen bod behövas."),
    ("Får grannarna veta att vi byter tak?",
     "Bara om åtgärden kräver lov får grannarna ett meddelande från staden. Ett takbyte med samma material kräver normalt inget lov."),
    ("Hur lång tid har grannarna på sig att överklaga ett bygglov i Sundbyberg?",
     "Tre veckor från den dag de fick beslutet, enligt Sundbybergs stad. Överklagandet ska vara skriftligt."),
    ('När får grannarna lämna synpunkter på ett bygglov i Sundbyberg?',
     'När ansökan inte följer detaljplanen får grannar och andra berörda lämna synpunkter genom ett grannehörande, enligt Sundbybergs stad.'),
  ],
  "sources": [("Sundbybergs stad – Byggetablering", _SBG + "bygglovsguide/byggetablering"),
              ("Sundbybergs stad – Vad gäller för grannar?", _SBG + "vad-galler-for-grannar"),
              ("Sundbybergs stad – Fasadändring", _SBG + "bygglovsguide/fasadandring"),
              ("Sundbybergs stad – Duvbo", _SBG + "duvbo"),
              ("Sundbybergs stad – Miljöprogram Duvbo (pdf)", "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska taket i Sundbyberg bytas?", "Boka ett gratis platsbesök, så planerar vi ställning, container och arbete innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa med ställning runt huset under takbytet",
     "Swedish detached villa with scaffolding around the walls and a large skip container standing on the driveway inside the plot during re-roofing, garden fence and trees, quiet suburban street, daylight, no people, no vehicles moving" + _IMG_END),
    ("Pall med nya takpannor på en uppfart",
     "pallet of new dark roof tiles wrapped in plastic standing on a gravel driveway next to a house with scaffolding, daylight" + _IMG_END),
    ("Halvt avtäckt tak med ny underlagstäckning",
     "roof of a Swedish 1920s villa during re-roofing seen from the garden: the near half covered with new black underlay membrane and neat horizontal wooden battens, the far half still with old red clay tiles, scaffolding with guard rail at the eaves, clear sky, daylight, no workers" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ KUNGSHOLMEN
"takbyte-kungsholmen.html": {
  "kind": "district", "service": "takbyte", "ort": "Kungsholmen", "svc_label": "Takbyte",
  "title": "Takbyte på Kungsholmen – villorna på Stora Essingen",
  "description": "Takbyte på Kungsholmen: villastaden på Stora Essingen som värdefull miljö, småhusen i siffror, takkupor och detaljer och när nytt material kräver lov.",
  "h1": "Takbyte på Kungsholmen",
  "lead": "Kungsholmen är mest känt för stenhus, men på Stora Essingen finns en villastad med egna trädgårdar och tegeltak. Den är utpekad som kulturhistoriskt värdefull miljö, och där är takets material och detaljer en del av helheten. Geal Entreprenad AB byter tak på villor och radhus på Stora Essingen och tar reda på vad som gäller för huset innan materialet väljs.",
  "card": "Villorna på Stora Essingen.",
  "sections": [
    {"id": "villastaden-kungsholmen", "anchor": "Villastaden",
     "h2": "En villastad i innerstadens stadsdelsområde",
     "paras": [
       "Stora Essingen hör till Kungsholmens stadsdelsområde. Stadens områdesfakta för 2025 visar 314 småhus på Stora Essingen, varav 268 med äganderätt, 35 hyresrätter och 11 bostadsrätter. I resten av stadsdelsområdet är småhusen mycket få.",
       "I stadens strategi för småhusområden, Varsam, räknas Stora Essingen till villastäderna, och i strategins tabell är den markerad som kulturhistoriskt värdefull miljö. Det betyder att utökad lovplikt kan gälla för åtgärder som annars är lovfria.",
     ],
     "aside": {"title": "Småhus på Stora Essingen 2025", "items": [
       "Totalt: 314", "Äganderätt: 268", "Hyresrätt: 35", "Bostadsrätt: 11"]}},
    {"id": "husen-kungsholmen", "h2": "Individuella hus med kupor och detaljer",
     "paras": [
       "Varsam beskriver villastäderna som privat organiserade, med en brokigare bebyggelse än i de egnahemsområden som staden planerade. Husen är i huvudsak enfamiljshus och individuellt utformade, och glasverandor, takkupor, snickarglädje och färgsättning ger en variation som är tydlig än i dag.",
       "För ett takbyte betyder det att två grannhus sällan har samma tak. Kupor, frontespiser, skorstenar och takfotens utformning skiljer sig åt, och de detaljerna ska tillbaka på samma sätt när taket är lagt.",
     ],
     "aside": {"title": "Villastaden enligt Varsam", "items": [
       "Individuellt utformade hus", "Takkupor och glasverandor", "Trä vanligast, även puts", "Stora trädgårdar"]}},
    {"id": "lovet-kungsholmen", "h2": "Material, kupor och lov",
     "paras": [
       "Boverket räknar ett byte till annat taktäckningsmaterial som en fasadändring, medan samma material och utförande räknas som underhåll. Boverket nämner också takkupor och frontespiser bland de byggnadsdelar där en ändring kan påverka husets karaktär och därmed kräva lov.",
       "Stockholms stad skriver att du behöver söka bygglov för åtgärder i ett särskilt kulturhistoriskt värdefullt bebyggelseområde även om åtgärden annars är bygglovsbefriad, och hänvisar till Stadsmuseets klassificeringskarta som en första indikation. Vi kontrollerar kartan och detaljplanen innan något annat än samma material föreslås.",
     ],
     "aside": None},
    {"id": "kartan-kungsholmen", "h2": "Vad Stadsmuseets karta visar",
     "paras": [
       "Stadsmuseet klassar byggnader och miljöer för att visa vilka kulturhistoriska värden som finns i staden. På klassificeringskartan är riksintressen för kulturmiljövården markerade med blå ring, områden som översiktsplanen pekar ut som särskilt kulturhistoriskt värdefulla med grön ring, och klassad bebyggelse med blått, grönt, gult eller grått.",
       "Staden skriver att du behöver söka bygglov för åtgärder som annars kan vara lovfria om fastigheten ligger inom ett riksintresse eller ett särskilt värdefullt område, eller om byggnaden är markerad med blått eller grönt. Kartan uppdateras när nya bedömningar görs, så klassningen kan ändras över tid. Vi kontrollerar den aktuella kartan för just ditt hus.",
     ],
     "aside": {"title": "Kartans markeringar", "items": [
       "Blå ring: riksintresse", "Grön ring: särskilt värdefullt område", "Blått eller grönt: lov krävs", "Kartan kan ändras över tid"]}},
    {"id": "detaljerna-kungsholmen", "h2": "Detaljerna före rivningen",
     "paras": [
       "Innan det gamla taket rivs fotograferar och mäter vi kupor, vindskivor, takfot, nock och plåtarbeten runt skorstenar. Det gör det möjligt att lägga tillbaka samma profiler och mått, och det ger ett underlag om staden behöver se hur taket såg ut före bytet.",
       "Under pannorna ser vi över läkt, underlagstäckning och råspont, och plåten i ränndalar och vid kupor görs om i samma arbete. Om plåtarbeten på Kungsholmen kan du läsa under " + _L.format("platslagare-kungsholmen.html", "plåtslagare på Kungsholmen") + ".",
     ],
     "aside": None},
    {"id": "logistiken-kungsholmen", "h2": "Ett tak på en ö",
     "paras": [
       "På en villatomt med uppvuxen trädgård gäller det att skydda växterna under arbetet. Vi planerar var ställning och container kan stå och hur material kommer fram, så att arbetet stör grannarna så lite som möjligt.",
       "Om tjänsten i stort kan du läsa under " + _L.format("takbyte.html", "takbyte") + ", och om skillnaden mot en renovering under " + _L.format("takbyte-eller-takrenovering.html", "takbyte eller takrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte på Stora Essingen till",
  "steps": [
    ("Kartan och planen", "Stadsmuseets karta och detaljplanen kontrolleras för fastigheten."),
    ("Platsbesök", "Taket, kuporna och detaljerna går vi igenom och dokumenterar."),
    ("Skriftligt kostnadsförslag", "Material, plåtarbeten och detaljer redovisas var för sig."),
    ("Lovfrågan", "Ska materialet bytas tas frågan till staden innan beställning."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs med samma detaljer."),
    ("Genomgång", "Vi går igenom taket och detaljerna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte på Kungsholmen",
  "rot": [_ROT_SMAHUS, _ROT_AMT],
  "price_h2": "Vad påverkar priset för takbytet på Stora Essingen?",
  "price": [
    "Takets yta och form, antal kupor och skorstenar, materialval, underlagets skick och hur ställning och material kan placeras. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Är villastaden på Stora Essingen kulturhistoriskt värdefull?",
     "Ja, i stadens strategi Varsam är Stora Essingen markerat som kulturhistoriskt värdefull miljö."),
    ("Hur många villor och radhus finns på Stora Essingen?",
     "Enligt stadens områdesfakta för 2025 finns 314 småhus på Stora Essingen, varav 268 ägs med äganderätt."),
    ("Kan vi ta bort en takkupa när taket ändå byts?",
     "Boverket nämner takkupor bland de delar där en ändring kan påverka husets karaktär och därmed kräva bygglov. I en värdefull miljö tar vi upp frågan med staden innan arbetet planeras."),
    ("Måste vi söka lov om vi lägger samma tegel igen på Stora Essingen?",
     "Samma material och utförande räknas enligt Boverket som underhåll och inte som fasadändring."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Stora Essingen (pdf)", _OF + "inre-staden/kungsholmen/stora-essingen.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Kungsholmens stadsdelsområde (pdf)", _OF + "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade.pdf"),
              _VARSAM, _BV_FAS, _STH_FAS, _STH_KL, _SKV, _SKV2],
  "cta": ("Ska taket på villan på Stora Essingen bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och detaljerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa med tegeltak och takkupa i en lummig trädgård",
     "1920s Swedish detached villa with red clay tile roof, one dormer and a brick chimney, light grey wooden facade with white trim, garden with apple trees and a hedge, quiet villa street, Stockholm, summer, clean image without any watermark or logo" + _IMG_END),
    ("Takkupa med plåtdetaljer på ett tegeltak",
     "close view of a dormer on a red clay tile roof of an old Swedish villa, with painted wooden window, metal flashing around the dormer cheeks and valley, daylight" + _IMG_END),
    ("Villagata med olika tak bakom staket och häckar",
     "quiet villa street on Stora Essingen style island with individually designed old villas with different roofs, clay tiles and metal, behind picket fences and hedges, trees, daylight, empty street" + _IMG_END),
  ],
},
}
