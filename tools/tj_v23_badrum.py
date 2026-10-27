# -*- coding: utf-8 -*-
"""Badrumsrenovering – ortsidor v23: Hägersten, Kista, Skärholmen, Sundbyberg, Vällingby, Älvsjö (2026-10-26).
Hubb: badrumsrenovering.html (TJ_HUB["badrumsrenovering"]). Tre bilder per sida: img[0] hero 4:3, img[1]–[2] 3:2.

Lokal vinkel per sida (en huvudfråga per sida):
Hägersten – bostadsrätten: bostadsrätterna i Midsommarkransen, Hägerstensåsen och Hägersten (områdesfakta 2025),
  styrelsens tillstånd (BRL 7 kap. 7 §), anmälan vid ny stam i nytt schakt, ROT-gränsen byta/flytta golvbrunn,
  golvlutning enligt GVK.
Kista – radhus i bostadsrättsförening i Kista och Akalla (områdesfakta), storskaliga stadsdelens småhus (Varsam),
  föreningens ledningar (BRL 7 kap. 12 §), ventilationen efter byggår (F 1961–1975, FTX från 1976), elgenomföringar.
Skärholmen – småhusen i Sätra, Vårberg, Skärholmen och Bredäng (områdesfakta), souterrängvåningen (Varsam),
  backventil och översvämning (Stockholm Vatten och Avfall), asbest i kakelfix och fog (Boverket), golvbrunnar
  före 1990 (GVK).
Sundbyberg – badrum i flerbostadshus och OVK (Sundbyberg), tillstånd för ventilation i bostadsrätt, Duvbo:
  ventilationshuv som fasadändring, kontrollplan.
Vällingby – radhus i riksintresset Vällingby–Råcksta, Atlantis och Omega (Varsam), vad som kräver lov utvändigt
  (ventilation), våtzoner (GVK).
Älvsjö – villastaden (Varsam, municipalsamhälle, Hallman), småhusen i Långbro, Långsjö, Liseberg och Solberga,
  badrum på övervåningen i trähus: förstärka träbjälklag (GVK), bärande konstruktion och ofullständiga ritningar,
  vattenburen golvvärme, dörröppningen.

Fakta endast från källorna i respektive 'sources', öppnade med curl/urllib (Mozilla-UA) 2026-10-26, alla 200;
pdf:erna (Varsam, riksintressen, områdesfakta) har textlager.
Strukna / ej använda: Herrängen (stadsdelsområdet inte belagt i källan), byggår för enskilda radhusområden i Kista
och Skärholmen (bara Bredäng 1962 och Sätra därefter finns i källan), avgifter och handläggningstider, alla priser,
garantier, omdömen och cert. GVK nämns som branschregler, inte som egen auktorisation.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no text, no letters"

_SI = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/"
_STH_FLYTTA = ("Stockholms stad – Flytta kök eller badrum", _SI + "flytta-kok-eller-badrum/")
_STH_VA = ("Stockholms stad – Installation eller ändring av vatten och avlopp", _SI + "installation-eller-andring-av-vatten-och-avlopp-va/")
_STH_STAM = ("Stockholms stad – Stambyte", _SI + "stambyte/")
_STH_BAR = ("Stockholms stad – Ändra i bärande konstruktion", _SI + "andra-i-barande-konstruktion/")
_STH_VENT = ("Stockholms stad – Ventilation", _SI + "ventilation/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
           "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 och 12 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_GVK = "https://www.gvk.se/branschregler/"
_GVK_BRUNN = ("GVK – Gamla golvbrunnar", _GVK + "golvbrunn/gamla-golvbrunnar/")
_GVK_LUT = ("GVK – Golvlutning", _GVK + "golv/golvlutning/")
_GVK_ZON = ("GVK – Våtzoner", _GVK + "vatzoner/")
_GVK_EL = ("GVK – Elgenomföring i badrum", _GVK + "elgenomforing-i-badrum/")
_GVK_TRA = ("GVK – Förstärka träbjälklag", _GVK + "golv/forstarka-trabjalklag/")
_GVK_GV = ("GVK – Vattenburen golvvärme", _GVK + "golv/golvvarme/vattenburen-golvvarme/")
_GVK_DORR = ("GVK – Dörröppning", _GVK + "golv/dorroppning/")
_SVOA_BACK = ("Stockholm Vatten och Avfall – Backventiler", "https://www.svoa.se/artiklar-listsida/oversvamning---hantera-och-forebygg/backventiler/")
_SVOA_FOR = ("Stockholm Vatten och Avfall – Förebygg översvämningar",
             "https://www.svoa.se/villa-och-radhus/vatten-och-avlopp/hantera-oversvamning/nar-det-regnar-mycket/")
_BV_ASB = ("Boverket – Risker med hantering av asbest i byggnader",
           "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_SUN_OVK = ("Sundbybergs stad – Obligatorisk ventilationskontroll (OVK)",
            "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/obligatorisk-ventilationskontroll-ovk")
_SUN_FAS = ("Sundbybergs stad – Fasadändring",
            "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/fasadandring")
_SUN_KP = ("Sundbybergs stad – Kontrollplan",
           "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/kontrollplan")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

PAGES_TJ = {

# ------------------------------------------------------------------ HÄGERSTEN
"badrumsrenovering-hagersten.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Hägersten", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Hägersten – bostadsrätten och brunnen",
  "description": "Badrumsrenovering i Hägersten: styrelsens tillstånd i bostadsrätt, när en ny stam ska anmälas, ROT för att byta men inte flytta golvbrunnen och rätt fall.",
  "h1": "Badrumsrenovering i Hägersten",
  "lead": "I Midsommarkransen och på Hägerstensåsen är de flesta bostäder bostadsrätter, och där avgör styrelsen och stadgarna en stor del av badrumsrenoveringen. Geal Entreprenad AB renoverar badrum i lägenheter och villor i Hägersten och går igenom vad som är ditt och vad som är föreningens innan rivningen börjar.",
  "card": "Bostadsrätten, golvbrunnen och fallet.",
  "sections": [
    {"id": "bostadsratten-hagersten", "anchor": "Bostadsrätten",
     "h2": "Bostadsrätterna i Hägersten",
     "paras": [
       "Stadens områdesfakta för 2025 visar 4 363 bostadsrätter i flerbostadshus i Midsommarkransen, 2 031 på Hägerstensåsen och 1 775 i stadsdelen Hägersten. Samtidigt finns 955 småhus med äganderätt i Hägersten. Badrummet i en lägenhet och badrummet i en villa följer därför olika regler, och vi börjar med att reda ut vilket som gäller.",
       "Bostadsrättslagen kräver styrelsens tillstånd för åtgärder i lägenheten som innefattar ingrepp i bärande konstruktion, installation eller ändring av ledningar för avlopp, värme, gas eller vatten och installation eller ändring av ventilation. Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet för föreningen. Stockholms stad råder dig att kontakta styrelsen innan du börjar planera att flytta badrummet.",
     ],
     "aside": {"title": "Kräver styrelsens tillstånd", "items": [
       "Ingrepp i bärande konstruktion", "Ändrade ledningar för vatten och avlopp", "Ändrad ventilation", "Påverkan på brandskyddet"]}},
    {"id": "anmalan-hagersten", "h2": "När badrummet behöver anmälas",
     "paras": [
       "Du behöver inte bygglov för att flytta ett badrum, skriver Stockholms stad. Men en anmälan och ett startbesked krävs om flytten påverkar bärande konstruktion eller brandskydd, om ventilationen ändras väsentligt eller om en ny VA-stam tillkommer i ett nytt schakt. Vid ett stambyte där installationerna byts i samma läge behövs normalt ingen anmälan.",
       "Oavsett anmälan ska arbetet uppfylla de tekniska egenskapskraven, och vid ett stambyte får tillgängligheten inte försämras, till exempel genom att golvet i badrummet höjs eller att dörröppningen blir för smal. Vi planerar höjderna så att tröskel och golv fungerar mot hallen.",
     ],
     "aside": None},
    {"id": "golvbrunnen-hagersten", "h2": "Byta golvbrunnen ger ROT, flytta den gör det inte",
     "paras": [
       "I en bostadsrätt ger Skatteverket rotavdrag för arbete innanför bostadens tak, väggar och golv som du ansvarar för enligt stadgarna, bland annat att byta golvbrunn, sätta kakel och klinker, installera dusch och toalett och dra vatten- och avloppsledningar som tjänar lägenheten. Inget avdrag ges däremot för att utföra stambyten, flytta eller byta ut avloppsrör eller flytta golvbrunnen.",
       "Det påverkar planeringen. Står golvbrunnen kvar på samma plats blir ROT-frågan enkel, medan en ny planlösning med flyttad brunn och nytt avloppsrör blir dyrare efter avdrag. Vi visar båda alternativen i kostnadsförslaget så att du kan jämföra.",
     ],
     "aside": {"title": "ROT i bostadsrätt", "items": [
       "Byta golvbrunn: ja", "Kakel och klinker: ja", "Flytta golvbrunn: nej", "Stambyte: nej"]}},
    {"id": "fallet-hagersten", "h2": "Rätt fall mot brunnen",
     "paras": [
       "GVK:s branschregler anger att golvet i duschplatsen ska ha ett fall mot golvbrunnen inom 1:150 till 1:50, det vill säga 7–30 millimeter per meter, och att övrig golvyta ska luta 2–10 millimeter per meter. Bakfall får inte förekomma, och tätskiktets uppvik vid dörröppningen ska ligga minst 20 millimeter över golvbrunnens fläns i duschplatsen.",
       "Stora klinkerplattor kräver normalt mindre lutning för att inte ge stora nivåskillnader mellan plattorna. Vi mäter fallet på det spacklade undergolvet innan tätskiktet läggs. Om köket i samma lägenhet kan du läsa under " + _L.format("koksrenovering-hagersten.html", "köksrenovering i Hägersten") + ", och om tjänsten i stort under " + _L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
    {"id": 'kanalen-hagersten', "h2": 'Badrumskanalen och köket',
     "paras": [
       'Vill du flytta köket och badrummet samtidigt påminner Stockholms stad om att ventilationskanalens sammanlagda mått måste vara tillräckligt stort innan badrumskanalen används som kombinerad imkanal för köket och frånluftskanal för badrummet. Köket behöver tillräcklig frånluft och ska uppfylla kraven för imkanal.',
       'Staden råder dig att rådgöra tidigt med skorstensfejarmästaren om förutsättningarna för en ny eller ändrad ventilationskanal. I en bostadsrätt är kanalerna dessutom ofta gemensamma för flera lägenheter, och då är det föreningens sak.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Hägersten",
  "steps": [
    ("Platsbesök", "Vi ser badrummet, golvbrunnen och stammarna och frågar efter stadgarna."),
    ("Styrelsen", "Du får en beskrivning av ändringarna att lämna till styrelsen."),
    ("Skriftligt kostnadsförslag", "Alternativ med kvarstående och flyttad golvbrunn står var för sig."),
    ("Rivning och underlag", "Gamla skikt rivs och golvet byggs upp med rätt fall."),
    ("Tätskikt och ytskikt", "Tätskikt enligt branschreglerna, sedan kakel, klinker och porslin."),
    ("Genomgång", "Vi går igenom badrummet och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Hägersten",
  "rot": [
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material och resor ger inget avdrag.",
    "Äger du en villa i Hägersten gäller småhusreglerna, där bland annat installation av dusch, toalett, kakel- och klinkersättning och indragning av vatten- och avloppsledningar ger avdrag.",
  ],
  "price_h2": "Vad påverkar priset för badrummet i Hägersten?",
  "price": [
    "Om golvbrunnen och toaletten står kvar, vad som döljer sig under det gamla golvet, rummets storlek, ytskikt och porslin och vad föreningen redan gör i sitt stambyte. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag styrelsens tillstånd för att renovera badrummet i Midsommarkransen?",
     "Ja, om du ändrar ledningar för vatten och avlopp, ventilationen eller bärande konstruktion. Det kräver bostadsrättslagen."),
    ("Behöver badrumsflytten i Hägersten anmälas till staden?",
     "Bara om den påverkar bärande konstruktion, brandskydd eller ventilationen väsentligt, eller om en ny VA-stam tillkommer i ett nytt schakt."),
    ("Får jag rotavdrag för att flytta golvbrunnen i bostadsrätten?",
     "Nej. Skatteverket ger inget avdrag för att flytta golvbrunn eller avloppsrör i en bostadsrätt, men för att byta golvbrunnen."),
    ("Hur mycket ska duschgolvet luta mot brunnen?",
     "Enligt GVK mellan 1:150 och 1:50, alltså 7–30 millimeter per meter. Övrig golvyta ska luta 2–10 millimeter per meter."),
    ("Kan golvet i badrummet bli högre efter renoveringen?",
     "Det bör undvikas. Vid stambyte får tillgängligheten inte försämras, och Stockholms stad nämner just höjda golv i badrum som exempel."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Midsommarkransen (pdf)", _OF + "soderort/hagersten/midsommarkransen.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hägerstensåsen (pdf)", _OF + "soderort/hagersten/hagerstensasen.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hägersten (pdf)", _OF + "soderort/hagersten/hagersten.pdf"),
              _BRL, _STH_FLYTTA, _STH_STAM, _GVK_LUT, _SKV, _SKV2],
  "cta": ("Ska badrummet i Hägersten göras om?", "Boka ett gratis platsbesök, så går vi igenom badrummet, stadgarna och golvbrunnen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Bostadshus från mitten av 1900-talet i ljus puts bland tallar",
     "mid 20th century Swedish three-storey apartment buildings in light yellow plaster with simple windows and small balconies, pine trees and lawns on a gentle slope, southern Stockholm suburb, autumn daylight" + _IMG_END),
    ("Badrum med badkar och stor kakelvägg",
     "newly renovated small Swedish apartment bathroom with light grey floor tiles sloping toward a new square stainless floor drain, white wall tiles, glass shower screen, wall-hung toilet, soft daylight" + _IMG_END),
    ("Badrumsgolv under arbete med spacklat underlag och ny golvbrunn",
     "small empty bathroom under renovation, smooth grey levelled screed floor with a new square stainless floor drain near the corner, walls with grey primer, no tiles yet, clean and tidy, soft construction light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ KISTA
"badrumsrenovering-kista.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Kista", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Kista – radhusen i föreningarna",
  "description": "Badrumsrenovering i Kista och Akalla: radhus i bostadsrättsförening, vad föreningen ansvarar för, ventilationen efter byggår och el genom tätskiktet.",
  "h1": "Badrumsrenovering i Kista",
  "lead": "I Kista och Akalla finns hundratals radhus och villor som ägs i bostadsrättsförening, och där gäller föreningens regler även om huset är ditt eget. Geal Entreprenad AB renoverar badrum i radhus och lägenheter i Kista och reder ut ansvaret innan arbetet börjar.",
  "card": "Radhusen, föreningen och ventilationen.",
  "sections": [
    {"id": "radhusen-kista", "anchor": "Radhusen",
     "h2": "Småhus i bostadsrättsförening",
     "paras": [
       "Enligt stadens områdesfakta för 2025 finns 404 småhus med bostadsrätt och 482 med äganderätt i Kista, och i Akalla 493 småhus med bostadsrätt och 170 med äganderätt. Stadens strategi för småhus- och villaområden beskriver att småhusen i de storskaliga stadsdelarna främst var radhus och kedjehus, men att det också förekom villor och atriumhus, till exempel i Akalla.",
       "Husen byggdes industriellt och rationellt, i enhetliga grupper med en blandning av tegel, trä och skivor i fasaderna och oftast med platta tak eller svagt lutande pulpettak. Omsorgen om planlösningarna var stor, och goda ljusförhållanden och funktionalitet var ledord, skriver staden.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Kista: 404 bostadsrätt, 482 äganderätt", "Akalla: 493 bostadsrätt, 170 äganderätt"]}},
    {"id": "ansvaret-kista", "h2": "Vad är ditt och vad är föreningens?",
     "paras": [
       "Bostadsrättslagen lägger ansvaret för lägenhetens skick på bostadsrättshavaren om inte stadgarna säger något annat. Men bostadsrättshavaren svarar inte för reparationer av ledningar för avlopp, värme, gas, el och vatten eller ventilationskanaler som föreningen har försett lägenheten med och som tjänar fler än en lägenhet.",
       "Ett radhus räknas också som bostadsrätt hos Skatteverket, och rotavdrag ges för arbete som du ansvarar för enligt stadgarna. För att installera eller ändra ledningar för vatten och avlopp eller ventilation krävs styrelsens tillstånd. Vi läser stadgarna med dig och tar fram en beskrivning som styrelsen kan ta ställning till.",
     ],
     "aside": None},
    {"id": "ventilation-kista", "h2": "Ventilationen följer husets byggår",
     "paras": [
       "Stockholms stad beskriver frånluftsventilation som vanlig i hus byggda mellan 1961 och 1975, med centrala fläktar som drar ut luften via don i kök, badrum och toalett. Från- och tilluftsventilation, med eller utan värmeåtervinning, är vanlig i hus byggda från 1976 och framåt. Badrummets frånluftsdon är därför en del av husets system, inte bara rummets.",
       "Installation eller väsentlig ändring av ventilationen kräver anmälan och startbesked, till exempel byte av aggregat, fläkt, kanaler eller värmeväxlare som påverkar flöden eller luftkvalitet. Monteras något utvändigt kan det bedömas som en ändring av byggnadens yttre utseende och kräva bygglov. Vi behåller donets läge och flöde och stämmer av med föreningen innan något ändras.",
     ],
     "aside": {"title": "Vanligt enligt staden", "items": [
       "Självdrag i äldre hus", "Frånluft 1961–1975", "Från- och tilluft från 1976"]}},
    {"id": "el-kista", "h2": "El genom tätskiktet",
     "paras": [
       "GVK:s branschregler säger att el i våtrum ska installeras i samråd med ett elinstallationsföretag. Genomföringar som bryter väggens tätskikt ska vara monterade och fixerade innan tätskiktet läggs, installationsrören ska vara minst 16 millimeter och monteras vinkelrätt mot väggen, och mellanrummet mot väggskivan får vara högst 2 millimeter.",
       "I platsen för bad eller dusch får det inte finnas flexibel slang eller ventilationsrör, och genomföringar för el ska om möjligt placeras i våtzon 2. Om köket kan du läsa under " + _L.format("koksrenovering-kista.html", "köksrenovering i Kista") + ", och om tjänsten i stort under " + _L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
    {"id": 'tillganglighet-kista', "h2": 'Ett badrum som håller när behoven ändras',
     "paras": [
       'GVK påminner om att minst ett hygienrum i bostaden ska vara tillgängligt och användbart för personer med nedsatt rörelseförmåga enligt byggreglerna. Branschorganisationen tipsar om att tänka på om tätskiktslösningen tål ändringar i efterhand och om väggarna bör förstärkas med kortlingar eller 15 millimeter konstruktionsplywood där stödhandtag kan komma att sitta.',
       'Fallet mot golvbrunnen kan ge stora nivåskillnader mot intilliggande rum om man inte väljer en lämplig lösning, till exempel att bila bort en bruksläggning eller välja en lågbyggande förstärkning av underlaget. I ett radhus där man vill kunna bo kvar länge planerar vi det från början.',
     ],
     "aside": {"title": 'Att tänka på', "items": ['Förstärkta väggar för stödhandtag', 'Låg tröskel eller ingen', 'Tätskikt som tål ändringar']}},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Kista",
  "steps": [
    ("Platsbesök", "Vi ser badrummet, ventilationsdonet och stammarna i huset."),
    ("Stadgar och styrelse", "Vi går igenom ansvaret och tar fram underlag till styrelsen."),
    ("Skriftligt kostnadsförslag", "Rivning, VVS, el, tätskikt och ytskikt står var för sig."),
    ("Installationer", "VVS och elgenomföringar monteras och fixeras före tätskiktet."),
    ("Tätskikt och ytskikt", "Tätskikt enligt branschreglerna, sedan kakel och klinker."),
    ("Genomgång", "Vi går igenom badrummet och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Kista",
  "rot": [
    "I en bostadsrätt, även ett radhus i förening, ger arbetet innanför bostadens tak, väggar och golv rotavdrag när du ansvarar för det enligt stadgarna, till exempel kakel- och klinkersättning, dusch, toalett, handfat och att byta golvbrunn. Inget avdrag ges för stambyten eller för att flytta golvbrunnen.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor ger inget avdrag.",
  ],
  "price_h2": "Vad påverkar priset för badrummet i Kista?",
  "price": [
    "Rummets storlek, om något ska flyttas, vad som finns under golvet, el och ventilation, ytskikt och porslin och vad föreningen ansvarar för. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag styrelsens tillstånd för badrummet i radhuset i Akalla?",
     "Ja, om du installerar eller ändrar ledningar för vatten och avlopp eller ventilation. Det gäller även radhus som ägs med bostadsrätt."),
    ("Vem betalar om avloppsstammen i vårt radhusområde i Kista behöver lagas?",
     "Ledningar som föreningen har försett husen med och som tjänar fler än en bostad ansvarar föreningen för, enligt bostadsrättslagen."),
    ("Får jag byta frånluftsfläkten i badrummet?",
     "Byte av fläkt som påverkar flöden kräver anmälan till staden, och i en bostadsrätt även styrelsens tillstånd."),
    ("Hur ska elen dras in i ett badrum med tätskikt?",
     "Via installationsrör på minst 16 millimeter, monterade vinkelrätt och fixerade innan tätskiktet läggs, helst i våtzon 2."),
    ("Ger badrummet i radhuset i Kista rotavdrag?",
     "Ja, för arbete som du ansvarar för enligt stadgarna. Skatteverket räknar radhus i bostadsrättsförening som bostadsrätt."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Kista (pdf)", _OF + "vasterort/jarva/kista.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Akalla (pdf)", _OF + "vasterort/jarva/akalla.pdf"),
              _VARSAM, _BRL, _STH_VENT, _GVK_EL, _SKV, _SKV2],
  "cta": ("Ska badrummet i Kista göras om?", "Boka ett gratis platsbesök, så går vi igenom badrummet och föreningens regler innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhuslänga i tegel och trä med platta tak och små förgårdar",
     "row of 1970s Swedish terraced houses with dark brick and wooden panel facades, flat roofs, small front gardens with hedges and a car-free footpath with young trees, northwestern Stockholm suburb, overcast daylight" + _IMG_END),
    ("Renoverat radhusbadrum med kakel, dusch och frånluftsdon i taket",
     "renovated small bathroom in a Swedish terraced house with white wall tiles, dark grey floor tiles, walk-in shower with glass screen, round white exhaust air valve in the ceiling, soft daylight" + _IMG_END),
    ("Våtrumsvägg med nydragna rör och genomföringar innan tätskiktet läggs",
     "bathroom wall under renovation with gypsum boards, electrical conduit pipes coming out at right angles and fixed pipe penetrations, ready for waterproofing membrane, construction light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"badrumsrenovering-skarholmen.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Skärholmen", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Skärholmen – radhusen och källaren",
  "description": "Badrumsrenovering i Skärholmen, Sätra, Vårberg och Bredäng: badrum i souterräng, backventil, asbest i kakelfix och golvbrunnar som ska bytas.",
  "h1": "Badrumsrenovering i Skärholmen",
  "lead": "I Sätra, Vårberg, Skärholmen och Bredäng finns nästan 2 000 småhus med äganderätt, och i de här områdena tas nivåskillnader ofta upp med en souterrängvåning. Geal Entreprenad AB renoverar badrum i radhus och villor i Skärholmen och börjar med golvbrunnen och det som finns under kaklet.",
  "card": "Radhusen, källarplanet och golvbrunnen.",
  "sections": [
    {"id": "husen-skarholmen", "anchor": "Radhusen",
     "h2": "Småhusen i Skärholmens stadsdelsområde",
     "paras": [
       "Stadens områdesfakta för 2025 visar 1 976 småhus med äganderätt i Skärholmens stadsdelsområde: 577 i Vårberg, 543 i Skärholmen, 536 i Sätra och 320 i Bredäng. Stadens strategi för småhus- och villaområden berättar att Bredäng var den första stadsdelen som planerades i stor skala och började byggas 1962, följd av Sätra.",
       "Strategin beskriver också att nivåskillnader i de här områdena ofta tas upp med en souterrängvåning, att tomterna är små och att husen är radhus, kedjehus, villor och atriumhus. Ligger badrummet i en souterrängvåning är det delvis under mark, och det påverkar hur vi planerar avlopp och golv.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Vårberg: 577", "Skärholmen: 543", "Sätra: 536", "Bredäng: 320"]}},
    {"id": "kallaren-skarholmen", "h2": "Badrum i nedre planet och backventilen",
     "paras": [
       "Stockholm Vatten och Avfall förklarar att en backventil installeras på servisledningen för att hindra att avloppsvatten från ledningen i gatan tränger in i källaren genom golvbrunnar och andra avlopp. Du kan installera en på eget initiativ, men den kräver ingrepp i ledningssystemet, kan inte sättas in i alla anläggningar och är ditt ansvar att sköta.",
       "Innan en backventil monteras måste du säkerställa att inga egna dagvattenanslutningar finns på ledningen, annars blir dagvattnet kvar i huset när ventilen stänger. Bolaget råder också att golvet i källaren bör vara av ett material som tål vatten och att takvatten från stuprör inte bör ledas till avloppsledningen.",
     ],
     "aside": {"title": "Före en backventil", "items": [
       "Inga dagvattenanslutningar på ledningen", "Plan för regelbunden tillsyn", "Golv som tål vatten"]}},
    {"id": "asbest-skarholmen", "h2": "Asbest i kakelfix och fog",
     "paras": [
       "Boverket skriver att det främst är byggnader uppförda mellan 1940 och 1970 som innehåller asbest, men att asbest användes i byggnader in på 1980-talet och att ett hus från perioden 1940–1980 sannolikt har asbest någonstans. Bland platserna nämns kakel- och klinkerfix och fog, socklar i badrum, mattor, lim under mattor och plattor och golvmassor.",
       "Så länge asbesten är bunden är den ingen fara, men den frigörs när materialet sågas, slipas, borras eller skrapas. Provtagning och analys är det enda säkra sättet att veta, och därför tar vi prov innan vi river i ett badrum från den här tiden. Rotavdrag ges för att sanera asbest i samband med byggarbete men inte för att mäta den.",
     ],
     "aside": None},
    {"id": "brunnen-skarholmen", "h2": "Golvbrunnar från före 1990 byts",
     "paras": [
       "Enligt GVK:s branschregler ska en golvbrunn som är äldre än 1990 bytas ut vid renovering. GVK tar ett hus byggt 1978 som exempel: har våtrummet inte renoverats sedan dess saknar golvbrunnen antagligen klämring för att fixera en plastmatta och ska definitivt bytas.",
       "Är åldern oklar finns ofta ett RSK-nummer, fabrikat eller modellnamn i själva brunnen, och vid tveksamhet rekommenderar GVK att byta. Om husens tak kan du läsa under " + _L.format("taklaggare-skarholmen.html", "takläggare i Skärholmen") + ", och om tjänsten i stort under " + _L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
    {"id": 'vatten-skarholmen', "h2": 'Om källaren redan har haft vatten',
     "paras": [
       'Har källaren drabbats av översvämning råder Stockholm Vatten och Avfall dig att först anmäla skadan till försäkringsbolaget och sedan rapportera händelsen till bolaget via dess formulär, eftersom det hjälper till att kartlägga ledningsnätet. Som fastighetsägare ansvarar du själv för att skydda din egendom mot översvämningar.',
       'Bolagets checklista tar upp att rensa hängrännor, stuprör och brunnar, att ha tunga tättslutande föremål som sandsäckar redo att lägga över golvbrunnar och toaletter i källaren, att se över dräneringen och fuktskyddet på väggar under mark och att marken ska luta från huset. Vi går igenom det innan ett nytt badrum byggs i nedre planet.',
     ],
     "aside": {"title": 'Checklista före bygget', "items": ['Rensade hängrännor och brunnar', 'Dränering och fuktskydd', 'Marken lutar från huset']}},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Skärholmen",
  "steps": [
    ("Platsbesök", "Vi ser badrummet, golvbrunnen, avloppet och hur rummet ligger mot mark."),
    ("Provtagning", "Kakelfix, fog och golvskikt provas för asbest när huset är från rätt tid."),
    ("Skriftligt kostnadsförslag", "Rivning, eventuell sanering, VVS och ytskikt står var för sig."),
    ("Rivning och brunn", "Gamla skikt rivs och golvbrunnen byts."),
    ("Tätskikt och ytskikt", "Tätskikt enligt branschreglerna, sedan kakel och klinker."),
    ("Genomgång", "Vi går igenom badrummet och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Skärholmen",
  "rot": [
    "För ett småhus räknar Skatteverket bland annat installation av dusch, toalett och handfat, kakel- och klinkersättning och att dra och reparera vatten- och avloppsledningar som rotarbete. Asbestsanering i samband med byggarbetet ger också avdrag, men inte mätning av asbest.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år, och tillsammans med rutavdrag högst 75 000 kronor.",
  ],
  "price_h2": "Vad påverkar priset för badrummet i Skärholmen?",
  "price": [
    "Rummets storlek, om asbest måste saneras, golvbrunnens och avloppets skick, om rummet ligger i nedre planet mot mark och vilka ytskikt du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad gör en backventil?",
     "Den sitter på servisledningen och hindrar att avloppsvatten från ledningen i gatan tränger in i källaren genom golvbrunnar och andra avlopp."),
    ("Vem ansvarar för att skydda huset i Skärholmen mot översvämning?",
     "Du som fastighetsägare. Stockholm Vatten och Avfall skriver att fastighetsägaren har ansvar för att skydda sin egendom och kan minska risken med förebyggande åtgärder."),
    ("Måste golvbrunnen bytas när vi renoverar badrummet i Sätra?",
     "Ja, om den är äldre än 1990. GVK:s branschregler kräver att sådana golvbrunnar byts vid renovering."),
    ("Kan det finnas asbest i badrummet i vårt radhus i Vårberg?",
     "Det kan det. Boverket nämner kakel- och klinkerfix, fog och socklar i badrum, och hus från 1940–1980 innehåller sannolikt asbest någonstans."),
    ("Får vi rotavdrag för asbestprovet?",
     "Nej. Skatteverket ger avdrag för att sanera asbest i samband med byggarbete, men inte för att mäta asbest."),
    ("Kan vi sätta in en backventil själva?",
     "Ja, enligt Stockholm Vatten och Avfall kan du installera en på eget initiativ, men du ansvarar för den och den passar inte alla anläggningar."),
    ("Vad ska vi tänka på innan backventilen monteras?",
     "Att inga egna dagvattenanslutningar finns på ledningen, och att ventilen behöver regelbunden tillsyn och skötsel."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Skärholmens stadsdelsområde (pdf)", _OF + "soderort/skarholmen/skarholmen-stadsdelsomrade.pdf"),
              _VARSAM, _SVOA_BACK, _SVOA_FOR, _BV_ASB, _GVK_BRUNN, _SKV, _SKV2],
  "cta": ("Ska badrummet i Skärholmen göras om?", "Boka ett gratis platsbesök, så går vi igenom badrummet, golvbrunnen och avloppet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhuslänga i tegel med ljus träpanel och små förgårdar",
     "1960s Swedish split-level terraced houses on a slope, lower level partly below ground, brick and painted wood facades, low-pitched roofs, small gardens with shrubs, southwestern Stockholm suburb, daylight" + _IMG_END),
    ("Ljust badrum med grått klinkergolv, golvbrunn och duschhörna",
     "renovated basement-level bathroom in a Swedish house with grey floor tiles, square floor drain, white wall tiles, a small high window near the ceiling, shower area with glass screen, soft light" + _IMG_END),
    ("Uppbrutet badrumsgolv med gammal golvbrunn och rivna klinkerplattor",
     "bathroom floor during demolition: old tiles removed, exposed concrete and an old round floor drain in the middle, dust sheets and tools neatly set aside, construction light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SUNDBYBERG
"badrumsrenovering-sundbyberg.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Sundbyberg", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Sundbyberg – ventilation och OVK",
  "description": "Badrumsrenovering i Sundbyberg: badrumsventilationen i flerbostadshus och OVK, styrelsens tillstånd, ventilationshuvar i Duvbo och kontrollplanen.",
  "h1": "Badrumsrenovering i Sundbyberg",
  "lead": "Badrummet är det rum där husets ventilation syns tydligast, och i ett flerbostadshus i Sundbyberg ska den fungera för alla lägenheter när du är klar. Geal Entreprenad AB renoverar badrum i lägenheter och villor i Sundbyberg och tar hänsyn till ventilationen från början.",
  "card": "Ventilationen, OVK och Duvbo.",
  "sections": [
    {"id": "ovk-sundbyberg", "anchor": "OVK",
     "h2": "Badrummet och husets ventilationskontroll",
     "paras": [
       "Sundbybergs stad förklarar att fastighetsägaren regelbundet ska kontrollera ventilationen genom en obligatorisk ventilationskontroll, OVK. Kontrollen ska göras innan ett nytt system tas i bruk, när ett befintligt system byggs om och regelbundet därefter: var sjätte år för flerbostadshus med F-, FX- eller S-ventilation och var tredje år för flerbostadshus med FT- eller FTX-ventilation.",
       "Kravet gäller inte en- och tvåbostadshus. Kontrollen görs av en sakkunnig kontrollant, och brister ska åtgärdas senast inom sex månader. För dig som renoverar betyder det att badrummets frånluftsdon och flöde är en del av husets kontroll, och att donet inte ska bytas eller flyttas utan att föreningen vet om det.",
     ],
     "aside": {"title": "OVK i flerbostadshus", "items": [
       "F, FX och S: var sjätte år", "FT och FTX: var tredje år", "Även när systemet byggs om"]}},
    {"id": "tillstand-sundbyberg", "h2": "Styrelsens tillstånd i bostadsrätten",
     "paras": [
       "Bostadsrättslagen kräver styrelsens tillstånd för installation eller ändring av anordning för ventilation, för installation eller ändring av ledningar för avlopp, värme, gas eller vatten och för ingrepp i bärande konstruktion. Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet för föreningen, och den kan förena ett tillstånd med villkor.",
       "För reparationer av ledningar och ventilationskanaler som föreningen har försett lägenheten med och som tjänar fler än en lägenhet svarar inte bostadsrättshavaren. Vi tar fram en beskrivning av vad som ändras i badrummet, så att styrelsen kan ta ställning innan arbetet börjar.",
     ],
     "aside": None},
    {"id": "duvbo-sundbyberg", "h2": "Villor i Duvbo: ventilationshuven är en fasadändring",
     "paras": [
       "I villan krävs ingen OVK, men det som syns utvändigt kan kräva lov. Sundbybergs stad räknar antenner, ventilationshuvar och skorstenar, liksom ventilationsaggregat, som fasadändringar. I Duvbo och för kulturhistoriskt värdefulla byggnader är lovplikten utökad, och där krävs för det mesta bygglov för fasadändringar.",
       "Ska badrummet i en Duvbovilla få en ny frånluftskanal som mynnar över taket planerar vi därför placeringen tidigt och tar fram underlag till en ansökan. Utanför Duvbo krävs inte längre bygglov för fasadändringar på en- eller tvåbostadshus som inte är kulturhistoriskt värdefulla.",
     ],
     "aside": {"title": "Fasadändring i Sundbyberg", "items": [
       "Ventilationshuvar", "Ventilationsaggregat", "Skorstenar och antenner"]}},
    {"id": "kontrollplan-sundbyberg", "h2": "Kontrollplanen när anmälan krävs",
     "paras": [
       "Påverkar badrumsrenoveringen bärande delar eller brandskydd väsentligt kan en anmälan krävas, och då ska startbeskedet ha kommit innan arbetet börjar. Staden beskriver kontrollplanen som en förteckning över vad som ska kontrolleras, vem som kontrollerar, hur och när det görs, mot vad resultatet jämförs och hur det redovisas.",
       "Kontrollerna kan göras av dig, av entreprenören, av en sakkunnig eller av en annan anlitad kontrollant. Vi fyller i våra kontroller löpande. Om köket kan du läsa under " + _L.format("koksrenovering-sundbyberg.html", "köksrenovering i Sundbyberg") + ", och om tjänsten i stort under " + _L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
    {"id": 'vattenskada-sundbyberg', "h2": 'Om vattnet läcker ut till grannen',
     "paras": [
       'Bostadsrättslagen säger att bostadsrättshavaren svarar för reparationer på grund av vattenledningsskada bara om skadan har uppkommit genom vårdslöshet eller försummelse, till exempel av någon som för hans eller hennes räkning utför arbete i lägenheten. Den som anlitar en hantverkare tar alltså ett ansvar för hur arbetet görs.',
       'Om bostadsrättshavaren försummar sitt ansvar så att någon annans egendom riskerar omfattande skador får föreningen enligt lagen avhjälpa bristen på bostadsrättshavarens bekostnad. Vi lägger därför tätskiktet enligt branschreglerna och dokumenterar det med foton innan kaklet sätts, så att det går att visa hur badrummet är byggt.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Sundbyberg",
  "steps": [
    ("Platsbesök", "Vi ser badrummet, frånluftsdonet och husets ventilationssystem."),
    ("Föreningen", "Beskrivning av ändringarna till styrelsen när det behövs."),
    ("Skriftligt kostnadsförslag", "Rivning, VVS, ventilation, tätskikt och ytskikt står var för sig."),
    ("Installationer", "VVS och el monteras och donet behåller sitt läge och flöde."),
    ("Tätskikt och ytskikt", "Tätskikt enligt branschreglerna, sedan kakel och klinker."),
    ("Genomgång", "Vi går igenom badrummet och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Sundbyberg",
  "rot": [
    "I en bostadsrätt ger Skatteverket rotavdrag för arbete på delar av ventilationskanal som finns innanför bostadens tak, väggar och golv, och för kakel- och klinkersättning, dusch, toalett och att byta golvbrunn, när du ansvarar för det enligt stadgarna.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor ger inget avdrag.",
  ],
  "price_h2": "Vad påverkar priset för badrummet i Sundbyberg?",
  "price": [
    "Rummets storlek, om något ska flyttas, ventilationen, vad som finns under golvet och vilka ytskikt och vilket porslin du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur snabbt ska brister från OVK åtgärdas i Sundbyberg?",
     "Så snart som möjligt och senast inom sex månader från besiktningen. Därefter ska ett godkänt protokoll från ombesiktningen skickas in."),
    ("Vem ansvarar om hantverkaren orsakar en vattenskada i bostadsrätten?",
     "Enligt bostadsrättslagen svarar bostadsrättshavaren för en vattenledningsskada som har uppkommit genom vårdslöshet av någon som utför arbete i lägenheten för hans eller hennes räkning."),
    ("Hur ofta görs OVK i vårt flerbostadshus i Sundbyberg?",
     "Var sjätte år med F-, FX- eller S-ventilation och var tredje år med FT- eller FTX-ventilation, enligt staden."),
    ("Behöver min villa i Sundbyberg OVK?",
     "Nej. Kravet på obligatorisk ventilationskontroll gäller inte en- och tvåbostadshus."),
    ("Får jag flytta frånluftsdonet i badrummet i bostadsrätten?",
     "Inte utan styrelsens tillstånd. Bostadsrättslagen kräver tillstånd för installation eller ändring av anordning för ventilation."),
    ("Behövs bygglov för en ny ventilationshuv på villan i Duvbo?",
     "För det mesta. Staden räknar ventilationshuvar som fasadändring, och i Duvbo krävs för det mesta bygglov för fasadändringar."),
    ("Ger arbete på ventilationen i badrummet rotavdrag?",
     "Ja, i en bostadsrätt för delar av ventilationskanalen som finns innanför bostadens tak, väggar och golv."),
  ],
  "sources": [_SUN_OVK, _SUN_FAS, _SUN_KP, _BRL, _SKV, _SKV2],
  "cta": ("Ska badrummet i Sundbyberg göras om?", "Boka ett gratis platsbesök, så går vi igenom badrummet och ventilationen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Flerbostadshus i tegel och puts längs en gata med träd",
     "1940s Swedish apartment buildings with brick and light plaster facades, regular windows and small balconies, tree-lined street, Sundbyberg, soft daylight" + _IMG_END),
    ("Nytt badrum med frånluftsdon i taket ovanför duschen",
     "newly renovated Swedish apartment bathroom with white wall tiles, grey floor tiles, shower with glass screen and a round white exhaust air valve in the ceiling above, soft light" + _IMG_END),
    ("Äldre trähus med tak av rött lertegel, skorsten och takkupa",
     "old Swedish wooden villa from around 1900 with red clay tile roof and a small metal ventilation cap on the roof, decorative carpentry, large trees, quiet daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"badrumsrenovering-vallingby.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Vällingby", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Vällingby – radhus i riksintresset",
  "description": "Badrumsrenovering i Vällingby: radhusen i riksintresset Vällingby–Råcksta, vad som får göras inomhus, när ventilation utvändigt kräver lov och våtzonerna.",
  "h1": "Badrumsrenovering i Vällingby",
  "lead": "Radhusen i Vällingby ligger i ett riksintresse för kulturmiljövården, men badrummet inne i huset kan renoveras utan bygglov. Det som syns på fasaden är en annan sak. Geal Entreprenad AB renoverar badrum i radhus och villor i Vällingby och Råcksta och vet var gränsen går.",
  "card": "Riksintresset, radhusen och våtzonerna.",
  "sections": [
    {"id": "riksintresset-vallingby", "anchor": "Riksintresset",
     "h2": "Radhusen i ABC-staden",
     "paras": [
       "Vällingby–Råcksta planerades som landets första ABC-stad, med arbete, bostäder och centrum och tunnelbana in till stan, och ingen skulle ha längre än 900 meters gångväg till tunnelbanan. Området byggdes ut under 1950-talet med högre hus närmast centrum och längst ut områden med radhus och småhus, och det är riksintresse för kulturmiljövården.",
       "Stadens strategi för småhusområden lyfter fram flera väl gestaltade radhus- och villaområden i Vällingby, bland dem de kulturhistoriskt synnerligen värdefulla Atlantis i nordost och Omega i nordväst. Bland riksintressets karaktärsdrag nämns de ursprungliga husens gestaltning och byggnadsdetaljer som fönster, entrépartier, balkonger och räcken.",
     ],
     "aside": {"title": "Utpekat i Vällingby", "items": [
       "Riksintresset Vällingby–Råcksta", "Atlantis i nordost", "Omega i nordväst"]}},
    {"id": "inomhus-vallingby", "h2": "Inomhus: inget bygglov, men anmälan i vissa fall",
     "paras": [
       "Stockholms stad skriver att du inte behöver bygglov för att flytta kök eller badrum. En anmälan och ett startbesked krävs om flytten påverkar bärande konstruktion eller brandskydd, om ventilationen ändras väsentligt eller om en ny VA-stam tillkommer i ett nytt schakt. Vid alla ändringar ska du ta hänsyn till byggnadens kulturhistoriska värden.",
       "Enligt stadens områdesfakta för 2025 finns 220 småhus med äganderätt och 228 med bostadsrätt i Vällingby, och i Råcksta 299 med äganderätt och 91 med bostadsrätt. Är huset en bostadsrätt kan du också behöva tillstånd från föreningen, som staden påpekar. Staden råder dessutom att du tidigt rådgör med skorstensfejarmästaren om förutsättningarna för en ny eller ändrad ventilationskanal.",
     ],
     "aside": None},
    {"id": "utvandigt-vallingby", "h2": "Utvändigt: ventilation kan kräva lov",
     "paras": [
       "Monteras ett aggregat, ventilationskanaler eller annan anordning utvändigt kan det bedömas som en ändring av byggnadens yttre utseende, och då behövs bygglov, skriver staden. Inom ett riksintresse för kulturmiljövården, och för byggnader som är markerade blå eller gröna i Stadsmuseets karta, krävs bygglov även för åtgärder som annars kan vara lovfria.",
       "Ett nytt badrum i ett Vällingbyradhus planerar vi därför så att ventilationen går genom de befintliga kanalerna och att inget nytt syns på fasaden eller taket. Behövs en utvändig ändring tar vi fram underlag till en ansökan innan arbetet börjar.",
     ],
     "aside": {"title": "Kan kräva bygglov här", "items": [
       "Aggregat på fasaden", "Nya kanaler eller huvar utvändigt", "Ändrade fönster eller dörrar"]}},
    {"id": "vatzoner-vallingby", "h2": "Våtzonerna i ett litet radhusbadrum",
     "paras": [
       "GVK delar in våtrummet i plats för bad eller dusch, våtzon 1 och våtzon 2. Våtzon 1 är väggarna vid duschen och en meter utanför den, och hela golvytan, och platsen för bad eller dusch omfattar golv och väggar upp till 2,0 meter över färdigt golv. Den del av väggytan som inte är våtzon 1 är våtzon 2 och ska också ha ett vattentätt skikt.",
       "GVK påpekar att ett badkar som installeras i ett rum som var anpassat för dusch kan göra att våtzon 2 klassas om till våtzon 1. I ett litet radhusbadrum ligger därför ofta större delen av väggarna i våtzon 1. Om husens tak kan du läsa under " + _L.format("taklaggare-vallingby.html", "takläggare i Vällingby") + ", och om tjänsten i stort under " + _L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Vällingby",
  "steps": [
    ("Platsbesök", "Vi ser badrummet, ventilationen och vad som syns utvändigt."),
    ("Kartan", "Riksintresset och Stadsmuseets karta kontrolleras om något ändras utvändigt."),
    ("Skriftligt kostnadsförslag", "Rivning, VVS, el, tätskikt och ytskikt står var för sig."),
    ("Rivning och underlag", "Gamla skikt rivs och väggar och golv byggs upp."),
    ("Tätskikt och ytskikt", "Tätskikt efter våtzonerna, sedan kakel, klinker och porslin."),
    ("Genomgång", "Vi går igenom badrummet och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Vällingby",
  "rot": [
    "För ett småhus med äganderätt ger installation av dusch, toalett och handfat, kakel- och klinkersättning och vatten- och avloppsledningar rotavdrag. Är huset en bostadsrätt gäller avdraget arbete innanför tak, väggar och golv som du ansvarar för enligt stadgarna.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för badrummet i Vällingby?",
  "price": [
    "Rummets storlek, om något ska flyttas, vad som finns under golvet, ventilationen, ytskikt och porslin och om något måste ändras utvändigt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem ska vi fråga om badrummets ventilationskanal i Vällingby?",
     "Stockholms stad råder dig att rådgöra tidigt med skorstensfejarmästaren om förutsättningarna för en ny eller ändrad ventilationskanal."),
    ("Behöver jag bygglov för att renovera badrummet i ett radhus i Atlantis?",
     "Inte för arbetet inomhus. Bygglov kan krävas om något ändras utvändigt, eftersom området ligger i riksintresset Vällingby–Råcksta."),
    ("Behövs bygglov för ett nytt ventilationsaggregat på fasaden?",
     "Det kan behövas. Stockholms stad skriver att utvändigt monterade aggregat och kanaler kan bedömas som ändring av byggnadens yttre utseende."),
    ("När behöver badrumsrenoveringen anmälas i Vällingby?",
     "Om den påverkar bärande konstruktion eller brandskydd, ändrar ventilationen väsentligt eller om en ny VA-stam tillkommer i ett nytt schakt."),
    ("Hur högt ska tätskiktet gå i duschen?",
     "Platsen för bad eller dusch omfattar golv och väggar upp till 2,0 meter över färdigt golv, och hela väggen i höjdled i våtzon 1 behandlas med tätskikt."),
    ("Ändras våtzonerna om vi sätter in ett badkar?",
     "Det kan de. GVK påpekar att ett badkar i ett rum som var anpassat för dusch kan göra att våtzon 2 klassas om till våtzon 1."),
  ],
  "sources": [_RIKS, _VARSAM, ("Stockholms stad – Områdesfakta 2025: Vällingby (pdf)", _OF + "vasterort/hasselby-vallingby/vallingby.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Råcksta (pdf)", _OF + "vasterort/hasselby-vallingby/racksta.pdf"),
              _STH_FLYTTA, _STH_VENT, _STH_KL, _GVK_ZON, _SKV, _SKV2],
  "cta": ("Ska badrummet i Vällingby göras om?", "Boka ett gratis platsbesök, så går vi igenom badrummet och vad som får ändras innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus från 1950-talet i tegel och puts längs en gångväg med träd",
     "1950s Swedish terraced houses with red brick and light plaster facades, regular windows, small front gardens, footpath with mature trees and lawns in between, western Stockholm suburb, summer daylight" + _IMG_END),
    ("Litet radhusbadrum med kakel på alla väggar och dusch i hörnet",
     "small renovated bathroom in a Swedish 1950s terraced house, white tiles on all walls, light grey floor, corner shower with glass screen, compact washbasin, soft daylight" + _IMG_END),
    ("Duschhörna med tätskikt på väggarna innan kakel sätts",
     "corner of a bathroom during renovation with a blue liquid waterproofing membrane on walls up to the ceiling and on the floor around a new floor drain, before tiling, construction light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"badrumsrenovering-alvsjo.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Älvsjö", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Älvsjö – badrum i villans övervåning",
  "description": "Badrumsrenovering i Älvsjö: villastaden, badrum på övervåningen i trähus, förstärka träbjälklaget, bärande konstruktion, golvvärme och dörröppningen.",
  "h1": "Badrumsrenovering i Älvsjö",
  "lead": "Ett badrum på övervåningen i en äldre trävilla ligger på ett träbjälklag, och ska det få klinker måste golvet först klara det. Geal Entreprenad AB renoverar badrum i villor i Älvsjö, Långbro, Långsjö och Liseberg och börjar med det som bär.",
  "card": "Villorna, träbjälklaget och golvvärmen.",
  "sections": [
    {"id": "villastaden-alvsjo", "anchor": "Villastaden",
     "h2": "Villorna kring Älvsjö",
     "paras": [
       "Stadens strategi för småhus- och villaområden berättar att stationssamhällena längs järnvägen på 1910-talet växte till större samhällen och att några, som Älvsjö, fick status som municipalsamhällen. Stadsplanen för Älvsjö villastad togs fram av Per Olof Hallman, och trä var det dominerande fasadmaterialet i villastäderna.",
       "Enligt stadens områdesfakta för 2025 finns 1 377 småhus med äganderätt i Långbro, 839 i Långsjö, 264 i Solberga, 255 i Liseberg och 191 i stadsdelen Älvsjö. I strategins tabell är del av Älvsjö markerad som kulturhistoriskt värdefull miljö med generösa byggrätter.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Långbro: 1 377", "Långsjö: 839", "Solberga: 264", "Liseberg: 255", "Älvsjö: 191"]}},
    {"id": "bjalklaget-alvsjo", "h2": "Klinker på ett träbjälklag",
     "paras": [
       "GVK:s branschregler kräver att ett golv som ska få kakel, klinker eller natursten förstärks för att bli tillräckligt stabilt. Det kan göras med en formstabil skiva som limmas och skruvas fast, till exempel 22 millimeter spånskiva kompletterad med minst 12 millimeter formstabil avjämningsmassa eller en 13 millimeter skiva, eller med lättfyllnadsmassa mellan bjälkarna och armerad avjämningsmassa.",
       "GVK:s anvisning utgår från ett bjälklag med högst 600 millimeter mellan bjälkarna, och med bjälkar 45 x 220 millimeter i virkeskvalitet C24 får avståndet mellan stöden vara högst 3,4 meter vid 600 millimeters centrumavstånd. Vi öppnar golvet och mäter bjälkarna innan vi bestämmer metod.",
     ],
     "aside": {"title": "GVK:s två metoder", "items": [
       "Formstabil skiva, limmad och skruvad", "Lättfyllnadsmassa mellan bjälkarna"]}},
    {"id": "barande-alvsjo", "h2": "Badrum på övervåningen och det som bär",
     "paras": [
       "Påverkar flytten av badrummet bärande konstruktion krävs anmälan och startbesked, skriver Stockholms stad. Du kan titta på ritningar för att se husets principiella konstruktion, men staden påpekar att ritningar kan vara ofullständiga och att det inte är säkert att de som byggde följde dem. Staden kan inte bedöma åt dig om det du vill göra påverkar bärande konstruktion.",
       "I ett äldre trähus anlitar vi därför en konstruktör när bjälklaget ska bära ett nytt badrum eller en vägg ska öppnas. Ändras ventilationen väsentligt eller tillkommer en ny stam i ett nytt schakt krävs också anmälan.",
     ],
     "aside": None},
    {"id": "golvvarme-alvsjo", "h2": "Golvvärme och dörröppningen",
     "paras": [
       "I ett hus med radiatorer kan badrummet få en lokal vattenburen golvvärmeslinga, ofta med en shunt som blandar ner radiatorvattnet. GVK skriver att rör på 12, 10 och 8 millimeter mest används vid renovering där bygghöjden ska vara låg, att inkopplingen mot värmesystemet bör göras av en VVS-montör och att elarbetet, som inkoppling av cirkulationspump och rumsreglering, ska göras av en elektriker.",
       "Det finns inget krav på tröskel i ett våtrum, men saknas tröskel ska fuktkänsligt material vid dörren skyddas och golvbrunnens fläns ligga minst 20 millimeter under tätskiktets översta punkt vid dörröppningen. Om villans kök kan du läsa under " + _L.format("koksrenovering-alvsjo.html", "köksrenovering i Älvsjö") + ", och om tjänsten i stort under " + _L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Älvsjö",
  "steps": [
    ("Platsbesök", "Vi ser badrummet, bjälklaget och var stammar och värme går."),
    ("Konstruktion", "Bjälkarna mäts och en konstruktör kopplas in när något ska bära mer."),
    ("Skriftligt kostnadsförslag", "Förstärkning, VVS, golvvärme, tätskikt och ytskikt står var för sig."),
    ("Anmälan", "Anmälan och kontrollplan när bärande delar eller stammar ändras."),
    ("Bygget", "Golvet förstärks, installationer dras och tätskikt och ytskikt läggs."),
    ("Genomgång", "Vi går igenom badrummet och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Älvsjö",
  "rot": [
    "För en villa räknar Skatteverket installation och reparation av dusch, toalett, handfat, element och kakel- och klinkersättning som rotarbete, liksom att dra och reparera vatten- och avloppsledningar. Är bostaden yngre än fem år får arbetet bara återställa det ursprungliga skicket.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor ger inget avdrag.",
  ],
  "price_h2": "Vad påverkar priset för badrummet i Älvsjö?",
  "price": [
    "Bjälklagets skick och om det behöver förstärkas, om badrummet flyttas, golvvärme, avstånd till stammar och vilka ytskikt du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur stora var tomterna i villastäderna från början?",
     "Enligt stadens strategi var tomter på 1 500–3 000 kvadratmeter typiska för villastäderna. När nya planer togs fram för delar av dem på 1930-talet blev tomterna 700–1 000 kvadratmeter."),
    ("Måste träbjälklaget förstärkas om vi vill ha klinker i badrummet?",
     "Ja. GVK kräver förstärkning av golv som ska få kakel, klinker, natursten eller liknande ytskikt."),
    ("Behöver vi anmäla ett nytt badrum på övervåningen i villan i Långbro?",
     "Om det påverkar bärande konstruktion eller brandskydd, ändrar ventilationen väsentligt eller kräver en ny stam i nytt schakt, ja."),
    ("Kan vi lita på husets gamla ritningar?",
     "Inte helt. Stockholms stad påpekar att ritningar kan vara ofullständiga och att det inte är säkert att de som byggde följde dem."),
    ("Går det att få golvvärme i badrummet om huset har radiatorer?",
     "Ja, med en lokal vattenburen slinga, ofta med shunt. GVK nämner rör på 12, 10 och 8 millimeter vid renovering med låg bygghöjd."),
    ("Måste badrummet ha tröskel?",
     "Nej, men då ska fuktkänsligt material vid dörren skyddas och golvbrunnens fläns ligga minst 20 millimeter under tätskiktets översta punkt vid dörren."),
  ],
  "sources": [_VARSAM, ("Stockholms stad – Områdesfakta 2025: Långbro (pdf)", _OF + "soderort/hagersten/langbro.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Långsjö (pdf)", _OF + "soderort/hagersten/langsjo.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Liseberg (pdf)", _OF + "soderort/hagersten/liseberg.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Solberga (pdf)", _OF + "soderort/hagersten/solberga.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Älvsjö (pdf)", _OF + "soderort/hagersten/alvsjo.pdf"),
              _GVK_TRA, _STH_BAR, _STH_FLYTTA, _GVK_GV, _GVK_DORR, _SKV, _SKV2],
  "cta": ("Ska badrummet i villan i Älvsjö göras om?", "Boka ett gratis platsbesök, så går vi igenom badrummet och bjälklaget innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre trävilla i två plan med tegeltak i en stor trädgård",
     "1910s Swedish two-storey wooden villa painted light green with white trim, red clay tile roof, glazed porch, large garden with apple trees and lilacs, quiet villa street, southern Stockholm, summer" + _IMG_END),
    ("Badrum med badkar, grått kakel och handdukstork",
     "renovated upstairs bathroom in an old Swedish wooden villa with sloping ceiling, roof window, light stone-look floor tiles, freestanding bathtub and walk-in shower, soft daylight" + _IMG_END),
    ("Uppbrutet golv med träbjälkar och nya golvskivor i ett badrum",
     "bathroom floor in an old wooden house during renovation: exposed timber floor joists, new particle board sheets partly screwed down, levelling tools on the floor, empty room without figurines or ornaments, construction light" + _IMG_END),
  ],
},
}
