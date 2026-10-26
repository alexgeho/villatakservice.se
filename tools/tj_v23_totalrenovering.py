# -*- coding: utf-8 -*-
"""Totalrenovering – ortsidor v23: Farsta, Hässelby, Spånga, Tyresö, Värmdö, Österåker (2026-10-26).
Tjänst under villarenovering.html (TJ_HUB["totalrenovering"]). Intent: renovera hela huset på en gång – skild från
ortens byggforetag-<ort>.html och från enskilda rum (badrumsrenovering-/koksrenovering-<ort>.html), som länkas.
Skild från v18/v21 (Bromma, Danderyd, Enskede, Huddinge, Kungsholmen, Lidingö, Nacka, Sollentuna, Solna, Södermalm,
Täby, Vasastan). Tre bilder per sida: img[0] hero 4:3, img[1]–[2] 3:2.

Lokal vinkel per sida (en huvudfråga per sida):
Farsta – småstugorna i Tallkrogen, Svedmyra och Sköndal (Varsam: självbyggeri, typritningar 1927–1957, Tallkrogens
  elliptiska plan, små bostäder, tillbyggnader mot trädgården), kulturhistoriskt värdefull miljö och lovplikten.
Hässelby – 1960- och 70-talens grupphus i Hässelby villastad (Varsam), eternit och asbest (Varsam, Boverket),
  frånluftsventilation 1961–1975 och anmälan, ROT för sanering men inte mätning.
Spånga – villastäderna Solhem, Bromsten, Flysta och Sundby (Varsam, områdesfakta), bärande konstruktion och
  ofullständiga ritningar, självdrag i äldre hus och anmälan vid ny ventilation.
Tyresö – bygg- och rivningsavfallet (sex fraktioner, dispens, asbest och asfalt till Kovik), bygglovsarkivet
  (ritningar som inte stämmer, VA-ritningar), eldstaden (anmälan, undantag, bygglov i särskilt värdefullt område).
Värmdö – nya byggregler (BBR och EKS ersatta, övergången slut 30 juni 2026, kontrollplanen anger regelverk),
  förbindelsepunkten och ledningarna på tomten, legionella och varmvattentemperaturer, vattnets hårdhet per vattenverk.
Österåker – fritidshusområden som blir permanentboende (Roslagsvatten, eget avlopp och egen brunn, VA-plan),
  anmälningspliktiga åtgärder i en ombyggnad och handlingarna, värmepump (anmälan, grundvattenvärme ej tillåten,
  Normbrunn 16), ansvaret efter 1 december 2025.

Fakta endast från källorna i respektive 'sources', öppnade med curl/urllib (Mozilla-UA) 2026-10-26, alla 200;
pdf:erna (Varsam, områdesfakta) har textlager.
Strukna / ej använda: Tyresös avgifter och mottagningspriser på Kovik, Tyresös datum för de fyra entreprenörerna
(året framgår inte), avgifter och handläggningstider i alla kommuner, att ett fritidshus som görs om till
permanentbostad i sig kräver lov (ingen källa), alla priser, garantier, omdömen och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no text, no letters"

_SI = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/"
_STH_BAR = ("Stockholms stad – Ändra i bärande konstruktion", _SI + "andra-i-barande-konstruktion/")
_STH_VENT = ("Stockholms stad – Ventilation", _SI + "ventilation/")
_STH_PLAN = ("Stockholms stad – Ändra planlösningen i en byggnad", _SI + "andra-planlosningen-i-en-byggnad/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
           "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_STH_FD = ("Stockholms stad – Fönster och dörrar (miljöprogram och typritningssamlingar)",
           "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fonster-och-dorrar/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_BV_ASB = ("Boverket – Risker med hantering av asbest i byggnader",
           "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_TY = "https://www.tyreso.se/boende--miljo/"
_TY_AVF = ("Tyresö kommun – Bygg- och rivningsavfall", _TY + "avfall-och-atervinning/bygg--och-rivningsavfall.html")
_TY_ARK = ("Tyresö kommun – Beställa handlingar från bygglovsarkivet", _TY + "bygga/bestalla-handlingar-fran-bygglovsarkivet.html")
_TY_ELD = ("Tyresö kommun – Eldstad, installera eller ändra", _TY + "bygga/bygglovswebben/eldstad-installera-eller-andra.html")
_VA = "https://www.varmdo.se/byggabomiljo/"
_VA_NYA = ("Värmdö kommun – Nya byggregler från 1 juli 2025", _VA + "bygganyttandraellerriva/nyabyggreglerfran1juli2025.4.74383e6b197a1b2c7e8317c.html")
_VA_KVA = ("Värmdö kommun – Kommunalt vatten och avlopp", _VA + "vattenochavlopp/kommunaltvattenochavlopp.4.1a82111d16e6c321a3693781.html")
_VA_LEG = ("Värmdö kommun – Legionella", _VA + "boendemiljo/legionella.4.21baa0f21900c48123d18028.html")
_OS = "https://www.osteraker.se/byggabomiljo/"
_OS_VA = ("Österåkers kommun – Vatten och avlopp", _OS + "vattenochavlopp.4.367d658917909e8fc2b3a4.html")
_OS_ANM = ("Österåkers kommun – Anmälan", _OS + "bygganyttandraellerriva/anmalan.4.367d658917909e8fc2bad6.html")
_OS_EN = ("Österåkers kommun – Energi och uppvärmning", _OS + "energiochuppvarmning.4.367d658917909e8fc2b629.html")
_OS_HUS = ("Österåkers kommun – Hus (bygglovsguiden)", _OS + "bygganyttandraellerriva/bygglovsguiden/hus.4.24daed7e19aff7a0474eef.html")

PAGES_TJ = {

# ------------------------------------------------------------------ FARSTA
"totalrenovering-farsta.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Farsta", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Farsta – småstugorna i Tallkrogen",
  "description": "Totalrenovering i Farsta: småstugorna i Tallkrogen, Svedmyra och Sköndal, stadens typritningar, små bostäder som byggs om och lovplikten i värdefull miljö.",
  "h1": "Totalrenovering i Farsta",
  "lead": "Småstugorna i Tallkrogen, Svedmyra och Sköndal byggdes efter stadens typritningar, ofta av ägarna själva, och de är små efter dagens mått. Geal Entreprenad AB totalrenoverar småstugor och villor i Farsta och börjar med husets egen typritning.",
  "card": "Småstugorna och typritningarna.",
  "sections": [
    {"id": "smastugorna-farsta", "anchor": "Småstugorna",
     "h2": "Småstugeområdena i Farsta",
     "paras": [
       "Stadens strategi för småhus- och villaområden räknar Tallkrogen, del av Svedmyra och del av Sköndal till småstugeområdena. Systemet med självbyggeri utformades i början av 1920-talet för att familjer med låga inkomster skulle kunna bygga egnahem. Staden tog över, organiserade byggandet och upprättade typritningar med utförliga bygginstruktioner, och de första stugorna stod klara 1927.",
       "Tallkrogen utmärker sig med sin elliptiska planstruktur där gatorna är utlagda som löparbanor på en idrottsarena. Enligt stadens områdesfakta för 2025 finns 941 småhus med äganderätt i Tallkrogen, 1 194 i Sköndal och 327 i Svedmyra, och 3 806 i hela Farsta stadsdelsområde.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Sköndal: 1 194", "Tallkrogen: 941", "Svedmyra: 327", "Farsta stadsdelsområde: 3 806"]}},
    {"id": "typritningar-farsta", "h2": "Börja med husets typritning",
     "paras": [
       "Småstugebyrån gav ut kataloger anpassade för de olika områdena, och i slutet av 1970-talet samlade stadsbyggnadskontoret alla typritningar från 1927 till 1957 i en sammanställning för dem som ville ändra sina stugor. Den finns hos stadsbyggnadskontoret eller på Stockholmskällan, och för Tallkrogen finns dessutom ett äldre miljöprogram.",
       "Husen är fristående i ett, ett och ett halvt eller två plan, byggda uteslutande i trä med fönster i fasadliv, stående panel med tunn lockläkt och tak av enkupigt eller tvåkupigt rött lertegel. Med typritningen vet vi redan före platsbesöket var bärande väggar, skorsten och trappa bör sitta, och vi stämmer av det mot huset när vi öppnar.",
     ],
     "aside": {"title": "Typritningarna", "items": [
       "Stugor uppförda 1927–1957", "Sammanställda av stadsbyggnadskontoret", "Finns även på Stockholmskällan"]}},
    {"id": "smabostader-farsta", "h2": "Små bostäder som ska räcka längre",
     "paras": [
       "Strategin konstaterar att bostäderna i småstugeområdena ofta är små och inte motsvarar dagens önskemål om standard, att trycket på att förändra husen har ökat och att många hus har byggts till, huvudsakligen mot trädgården. Därför är gaturummets ursprungliga karaktär relativt välbevarad.",
       "En totalrenovering i en småstuga handlar därför ofta om att få ut mer av samma yta: en ny planlösning, ett nytt badrum och kök och en tillbyggnad på baksidan. Ingrepp i bärande konstruktion kräver anmälan och startbesked, och Stockholms stad råder dig att anlita en konstruktör om du är osäker.",
     ],
     "aside": None},
    {"id": "lovplikt-farsta", "h2": "Kulturhistoriskt värdefulla miljöer",
     "paras": [
       "Strategin beskriver småstugeområdena som kulturhistoriskt värdefulla miljöer, och i dess tabell är Tallkrogen, del av Svedmyra och del av Sköndal markerade som kulturhistoriskt värdefull miljö. Ligger huset inom ett område som översiktsplanen pekar ut som särskilt kulturhistoriskt värdefullt, grön ring i Stadsmuseets karta, eller är det markerat blått eller grönt, behöver du bygglov för åtgärder som annars kan vara lovfria, till exempel nya fönster eller annat fasadmaterial.",
       "Inomhus är friheten större, men allt utvändigt i en totalrenovering prövar vi mot kartan först. Staden påpekar att de äldre miljöprogrammen inte har juridisk status men ger kunskap om områdets karaktär. Om badrummet kan du läsa under " + _L.format("badrumsrenovering-farsta.html", "badrumsrenovering i Farsta") + ", och om tjänsten i stort under " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
    {"id": 'fargen-farsta', "h2": 'Fasaden och färgen',
     "paras": [
       'Strategin berättar att färgsättningen i småstugeområdena från början var strikt reglerad och begränsad till ett fåtal kulörer, ofta i ljusa nyanser av grått, grönt och gult, och att rödfärg bara fick användas efter särskild ansökan. Den sammanhållna färgsättningen bidrar fortfarande till områdenas enhetliga karaktär.',
       'Ingår fasaden i totalrenoveringen föreslår vi därför kulörer som passar gatan och kontrollerar om byte av kulör eller fasadmaterial kräver lov för just ert hus.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Farsta till",
  "steps": [
    ("Typritning och karta", "Husets typritning, miljöprogram och Stadsmuseets karta tas fram."),
    ("Platsbesök", "Stomme, installationer och önskemål går vi igenom i huset."),
    ("Skriftligt kostnadsförslag", "Rivning, stomme, installationer och ytskikt står var för sig."),
    ("Anmälan och lov", "Anmälan vid bärande ändringar och bygglov för utvändiga ändringar när det krävs."),
    ("Ombyggnad", "Rivning, stomme, el, VVS, isolering och ytskikt i rätt ordning."),
    ("Genomgång", "Vi går igenom huset och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Farsta",
  "rot": [
    "För ett småhus räknar Skatteverket bland annat att riva väggar och bygga om planlösningen, arbeta med tilläggsisolering, sätta kakel och klinker och göra förbättringsarbeten som rotarbete. Att bygga ett helt nytt hus eller riva ett hus ger inget avdrag, och större delen av den ursprungliga stommen ska behållas vid en ombyggnad.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år, och äger ni huset två kan båda göra avdrag. Material och resor ger inget avdrag.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Farsta?",
  "price": [
    "Husets storlek och skick, hur mycket av stommen som ändras, om en tillbyggnad ingår, el och VVS och vilka ytskikt du väljer. Läs mer om helrenoveringar under " + _L.format("villarenovering.html", "villarenovering") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Var hittar vi typritningen till vår småstuga i Tallkrogen?",
     "Stadsbyggnadskontoret sammanställde alla typritningar från 1927 till 1957, och sammanställningen finns hos stadsbyggnadskontoret eller på Stockholmskällan."),
    ("Behövs bygglov för nya fönster på en småstuga i Farsta?",
     "Det kan behövas. Småstugeområdena är kulturhistoriskt värdefulla miljöer, och ligger huset inom grön ring i Stadsmuseets karta eller är markerat blått eller grönt krävs bygglov för åtgärder som annars kan vara lovfria."),
    ("Behöver vi anmäla en ny planlösning?",
     "Om ändringen påverkar bärande konstruktion, ja. Då krävs anmälan och startbesked innan arbetet börjar."),
    ("Har äldre miljöprogram någon juridisk betydelse?",
     "Nej, enligt Stockholms stad har de ingen juridisk status i bygglovsprövningen, men de ger kunskap om områdets karaktär."),
    ("Ger totalrenoveringen av småstugan rotavdrag?",
     "Ja, för arbetskostnaden. Att riva väggar, bygga om planlösningen och tilläggsisolera räknas som rotarbete på småhus."),
  ],
  "sources": [_VARSAM, ("Stockholms stad – Områdesfakta 2025: Tallkrogen (pdf)", _OF + "soderort/farsta/tallkrogen.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Sköndal (pdf)", _OF + "soderort/farsta/skondal.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Svedmyra (pdf)", _OF + "soderort/farsta/svedmyra.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Farsta stadsdelsområde (pdf)", _OF + "soderort/farsta/farsta-stadsdelsomrade.pdf"),
              _STH_BAR, _STH_KL, _STH_FD, _SKV, _SKV2],
  "cta": ("Ska småstugan i Farsta byggas om?", "Boka ett gratis platsbesök, så går vi igenom huset och typritningen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Småstuga i trä med tak av rött lertegel och häck mot gatan",
     "small 1930s Swedish wooden cottage in one and a half storeys with mansard roof of red clay tiles, light grey vertical board-and-batten facade, windows flush with the facade, hedge and fruit trees, gently curving residential street, summer" + _IMG_END),
    ("Rad av likadana småstugor i ljusa kulörer med häckar mot gatan",
     "row of identical small Swedish wooden cottages painted in pale grey, green and yellow, red tile roofs, clipped hedges along the street, quiet suburban street in southern Stockholm, daylight" + _IMG_END),
    ("Interiör under renovering med öppnade väggar och ny stomme",
     "interior of a small old wooden house during full renovation: walls opened to the studs, new timber framing, new electrical conduits and insulation, plank floor covered with protective board, construction light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HÄSSELBY
"totalrenovering-hasselby.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Hässelby", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Hässelby – grupphus från 60- och 70-tal",
  "description": "Totalrenovering i Hässelby: 1960- och 70-talens grupphus, eternit och asbest, frånluften och anmälan, och ROT för sanering men inte provtagning.",
  "h1": "Totalrenovering i Hässelby",
  "lead": "I Hässelby villastad ersattes många villor på 1960- och 1970-talen av täta grupper av likadana småhus, och när ett sådant hus renoveras lönar det sig ofta att göra allt i en följd. Geal Entreprenad AB totalrenoverar radhus, kedjehus och villor i Hässelby och börjar med det som kan vara farligt att riva.",
  "card": "Grupphusen, eterniten och ventilationen.",
  "sections": [
    {"id": "grupphusen-hasselby", "anchor": "Grupphusen",
     "h2": "Grupphusen i Hässelby villastad",
     "paras": [
       "Stadens strategi för småhus- och villaområden beskriver hur många villor i Hässelby villastad på 1960- och 1970-talen ersattes av täta, stora sammanhållna grupper av enhetlig småhusbebyggelse. Med mindre tomter och samlade parkeringsytor kunde marken utnyttjas bättre, och villastäderna utvecklades till stor del till renodlade villaområden.",
       "Enligt stadens områdesfakta för 2025 finns 4 757 småhus med äganderätt i Hässelby villastad och 9 216 i hela Hässelby-Vällingby stadsdelsområde. Husen i en grupp är ofta byggda likadant, så det vi hittar när vi öppnar ett hus säger mycket om grannhusen också.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Hässelby villastad: 4 757", "Hässelby-Vällingby: 9 216"]}},
    {"id": "eterniten-hasselby", "h2": "Eternit och annan asbest",
     "paras": [
       "Strategin skriver om Hässelby att man i många områden prövade nya material, och att ett populärt material var asbestcement, mer känt som eternit. Eterniten har i många fall bytts ut, och i dag finns fasadskivor utan asbest som gör det möjligt att behålla radhusens uttryck.",
       "Boverket skriver att byggnader från perioden 1940–1980 sannolikt innehåller asbest någonstans och nämner bland annat kakelfix och fog, golvmattor och lim, rörisolering, fasadskivor, ventilationskanaler och fönsterkitt. Provtagning och analys är det enda säkra sättet att veta, och asbesthaltigt material som tagits ner får inte säljas eller överlåtas. Vi tar prov innan rivningen planeras.",
     ],
     "aside": {"title": "Asbest kan finnas i", "items": [
       "Fasadskivor av eternit", "Kakelfix och fog", "Golvmattor och lim", "Rörisolering", "Ventilationskanaler"]}},
    {"id": "ventilationen-hasselby", "h2": "Frånluften från 1960- och 70-talen",
     "paras": [
       "Stockholms stad beskriver frånluftsventilation som vanlig i hus byggda mellan 1961 och 1975. Centrala fläktar drar ut luften via don i kök, badrum och toalett, och tilluften kommer in via uteluftsdon i ytterväggarna och via otätheter. Systemet ger vissa möjligheter att rena tilluften och under vissa förutsättningar värmeåtervinning.",
       "När ett hus från den tiden tätas med nya fönster och ny isolering behöver ventilationen ses över samtidigt. Installation eller väsentlig ändring av ventilationen, till exempel ett nytt aggregat, ny fläkt eller värmeväxlare som påverkar flöden, kräver anmälan och startbesked, och monteras något utvändigt kan det kräva bygglov.",
     ],
     "aside": None},
    {"id": "ordningen-hasselby", "h2": "Ordningen i en totalrenovering",
     "paras": [
       "Vi börjar med provtagning och, om det behövs, sanering. Därefter kommer stommen, sedan el och VVS, isolering och ventilation, och sist ytskikten. Ingrepp i bärande konstruktion kräver anmälan, och staden påpekar att ritningar kan vara ofullständiga.",
       "Rotavdrag ges för att sanera asbest i samband med byggarbete, men inte för att mäta asbest. Om badrummet kan du läsa under " + _L.format("badrumsrenovering-hasselby.html", "badrumsrenovering i Hässelby") + ", om fasaden under " + _L.format("fasadrenovering-hasselby.html", "fasadrenovering i Hässelby") + " och om tjänsten i stort under " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
    {"id": 'tunnelbanestaden-hasselby', "h2": 'Hässelby gård och Hässelby strand',
     "paras": [
       'Utanför villastaden ligger Hässelby gård och Hässelby strand, som stadens strategi räknar till tunnelbanestadens gruppbyggda småhusområden. Rad- och kedjehus placerades längst ut från centrum och tunnelbanestationen, med en successiv nedtrappning av skalan, och båda områdena är markerade som kulturhistoriskt värdefull miljö.',
       'Strategin beskriver arkitekturen som en blandning av för tiden moderna idéer och folkhemsidealet, med fasader i rött tegel men också puts och skivor i fibercement. Enligt områdesfakta 2025 finns 324 småhus med äganderätt i Hässelby gård. När något ska ändras på fasaden i en sådan grupp kontrollerar vi först vad som gäller för området.',
     ],
     "aside": {"title": 'Tunnelbanestad i Hässelby', "items": ['Hässelby gård', 'Hässelby strand', 'Kulturhistoriskt värdefull miljö']}},
  ],
  "steps_h2": "Så går en totalrenovering i Hässelby till",
  "steps": [
    ("Platsbesök", "Stomme, installationer, ventilation och ytskikt går vi igenom."),
    ("Provtagning", "Misstänkta material provas för asbest före rivningen."),
    ("Skriftligt kostnadsförslag", "Sanering, rivning, installationer och ytskikt står var för sig."),
    ("Anmälan", "Anmälan vid bärande ändringar och ny ventilation."),
    ("Ombyggnad", "Sanering, stomme, el, VVS, isolering, ventilation och ytskikt."),
    ("Genomgång", "Vi går igenom huset och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Hässelby",
  "rot": [
    "Skatteverket räknar asbestsanering i samband med byggarbete som rotarbete på småhus, liksom att riva väggar, bygga om planlösningen och tilläggsisolera. Att mäta fukt, radon eller asbest ger däremot inget avdrag.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Hässelby?",
  "price": [
    "Om asbest måste saneras, husets storlek, hur mycket av stommen och installationerna som byts, ventilationen och vilka ytskikt du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken ventilation har ett radhus från 1960-talet i Hässelby?",
     "Ofta frånluft. Stockholms stad beskriver frånluftsventilation som vanlig i hus byggda mellan 1961 och 1975, med fläktar som drar ut luften via don i kök och badrum."),
    ("Får vi sälja eller ge bort eternitskivor som har tagits ner?",
     "Nej. Boverket påpekar att EU:s kemikalieregler innebär att asbesthaltiga material som tagits ner vid rivning inte får säljas eller överlåtas."),
    ("Är Hässelby gård och Hässelby strand kulturhistoriskt värdefulla?",
     "Ja, i stadens strategi för småhusområden är båda markerade som kulturhistoriskt värdefull miljö bland tunnelbanestäderna."),
    ("Kan vårt radhus i Hässelby ha eternitskivor på fasaden?",
     "Det är möjligt. Stadens strategi skriver att asbestcement, eternit, var ett populärt material i området och att det i många fall har bytts ut."),
    ("Hur vet vi om det finns asbest i huset?",
     "Bara genom provtagning och analys, enligt Boverket. Hus från 1940–1980 innehåller sannolikt asbest någonstans."),
    ("Får vi rotavdrag för asbestsaneringen?",
     "Ja, när saneringen görs i samband med byggarbete. För själva provtagningen ges inget avdrag."),
    ("Behöver vi anmäla ett nytt ventilationsaggregat i huset?",
     "Ja. Installation eller väsentlig ändring av ventilationen kräver anmälan och startbesked enligt Stockholms stad."),
    ("Kan vi behålla radhusets utseende om eterniten byts?",
     "Strategin påpekar att det i dag finns fasadskivor utan asbest som gör det möjligt att behålla uttrycket på radhusen."),
  ],
  "sources": [_VARSAM, ("Stockholms stad – Områdesfakta 2025: Hässelby villastad (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-villastad.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hässelby-Vällingby stadsdelsområde (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-vallingby-stadsdelsomrade.pdf"),
              _BV_ASB, _STH_VENT, _STH_BAR, _SKV, _SKV2],
  "cta": ("Ska huset i Hässelby totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom huset och vad som behöver provtas innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Kedjehus från 1970-talet med likadana fasader längs en återvändsgata",
     "group of identical 1970s Swedish link houses with dark wood and grey fibre-cement panel facades, low-pitched roofs, carports, cul-de-sac with young trees, western Stockholm suburb, overcast daylight" + _IMG_END),
    ("Grå panelfasad med ett enkelt vitt fönster på ett radhus",
     "close-up of a 1960s Swedish terraced house facade clad in grey fibre-cement boards with aluminium trims and a simple window, daylight, slight weathering" + _IMG_END),
    ("Rum under totalrenovering med blottad stomme och nya installationer",
     "room in a 1970s Swedish house during total renovation: walls stripped to timber studs, new ventilation ducts and electrical conduits installed, plastic dust protection, construction light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"totalrenovering-spanga.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Spånga", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Spånga – villorna i Solhem och Bromsten",
  "description": "Totalrenovering i Spånga: villastäderna Solhem, Bromsten, Flysta och Sundby, bärande väggar och ofullständiga ritningar, självdrag och ny ventilation.",
  "h1": "Totalrenovering i Spånga",
  "lead": "Villorna i Solhem, Bromsten, Flysta och Sundby är från många olika decennier, och i en äldre villa kan stommen se annorlunda ut än ritningarna. Geal Entreprenad AB totalrenoverar villor i Spånga och tar reda på vad som bär innan någon vägg rivs.",
  "card": "Villastäderna, stommen och ventilationen.",
  "sections": [
    {"id": "villastaderna-spanga", "anchor": "Villastäderna",
     "h2": "Villastäderna i Spånga",
     "paras": [
       "Stadens strategi för småhus- och villaområden berättar att stationssamhällena vid järnvägen på 1910-talet växte till större samhällen, och att Spånga var ett av dem som fick status som municipalsamhälle. Solhem, Bromsten, Flysta och Sundby räknas till villastäderna. I Solhem fanns stora tomter där bara en tiondel av tomten fick bebyggas, och Solhem är i strategins tabell markerat som kulturhistoriskt värdefull miljö.",
       "Enligt stadens områdesfakta för 2025 finns 1 946 småhus med äganderätt i Solhem, 916 i Bromsten, 657 i Flysta och 525 i Sundby. Villastäderna har förtätats successivt genom tomtdelningar. När nya planer togs fram för delar av dem på 1930-talet blev tomterna 700–1 000 kvadratmeter, och senare har hus tillkommit på tomter kring 600 kvadratmeter, så hus från olika tider står sida vid sida.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Solhem: 1 946", "Bromsten: 916", "Flysta: 657", "Sundby: 525"]}},
    {"id": "barande-spanga", "h2": "Väggarna som bär",
     "paras": [
       "Stockholms stad kräver anmälan och startbesked för ändringar som påverkar byggnadens bärande konstruktion. Du kan logga in med bank-id och se husets ritningar för att förstå dess principiella konstruktion, men staden påpekar att ritningar kan vara ofullständiga och att det inte är säkert att de som byggde följde dem. Staden kan inte bedöma åt dig om ändringen påverkar bärande konstruktion och råder dig att kontakta en konstruktör.",
       "I en villa som byggts om flera gånger är det just där överraskningarna finns. Vi öppnar på några ställen innan planlösningen bestäms och tar in en konstruktör när en bärande vägg ska bort eller ett bjälklag ska bära mer.",
     ],
     "aside": {"title": "Kräver anmälan", "items": [
       "Ingrepp i bärande konstruktion", "Väsentlig ändring av ventilation", "Ändring som påverkar brandskyddet"]}},
    {"id": "sjalvdrag-spanga", "h2": "Självdrag i äldre villor",
     "paras": [
       "Stockholms stad beskriver hur äldre hus ofta har självdragsventilation, med en panna i källaren och en skorsten genom huset som mynnar över taknocken. På vintern sugs luften in genom ventiler, vädringsfönster och otätheter och ut via skorstenskanalen i kök och badrum, och problem uppstår ofta på sommaren när temperaturen ute och inne är densamma och draget uteblir.",
       "Systemet medger ingen rening av tilluften och ingen värmeåtervinning. När huset tätas i en totalrenovering ändras förutsättningarna för självdraget, och installation eller väsentlig ändring av ventilationen kräver anmälan. Vi planerar ventilationen tillsammans med fönster och isolering.",
     ],
     "aside": None},
    {"id": "planen-spanga", "h2": "Planlösningen och arbetsordningen",
     "paras": [
       "Staden skriver att ändringar av planlösningen kan kräva anmälan när de påverkar tekniska egenskapskrav som bärförmåga, brandskydd, ventilation eller vatten och avlopp, och att du behöver kontakta en konsult om du är osäker.",
       "Vi gör arbetet i ordningen stomme, el och VVS, isolering och ventilation, ytskikt. Om villans badrum kan du läsa under " + _L.format("badrumsrenovering-spanga.html", "badrumsrenovering i Spånga") + ", om köket under " + _L.format("koksrenovering-spanga.html", "köksrenovering i Spånga") + " och om tjänsten i stort under " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
    {"id": 'karaktaren-spanga', "h2": 'Villastadens karaktär utvändigt',
     "paras": [
       'Strategin beskriver villastäderna som privat organiserade, med en brokigare bebyggelse än i stadens egnahemsområden och hus som är individuellt utformade. Trä var det dominerande fasadmaterialet, även om puts förekom, och glasverandor, takkupor, snickarglädje och färgsättning gav variationen som syns än i dag. Husen var som regel indragna från gatan med en grön förgård.',
       'Ändras något utvändigt i en totalrenovering, som fönster, takkupor eller fasadmaterial, kontrollerar vi Stadsmuseets karta och detaljplanen först. Solhem är markerat som kulturhistoriskt värdefull miljö i strategins tabell.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Spånga till",
  "steps": [
    ("Ritningar", "Husets ritningar hämtas och jämförs med huset."),
    ("Platsbesök och provöppningar", "Stomme, bjälklag, skorsten och installationer undersöks."),
    ("Skriftligt kostnadsförslag", "Stomme, installationer, ventilation och ytskikt står var för sig."),
    ("Konstruktör och anmälan", "Beräkningar och anmälan vid bärande ändringar och ny ventilation."),
    ("Ombyggnad", "Stomme, el, VVS, isolering, ventilation och ytskikt i rätt ordning."),
    ("Genomgång", "Vi går igenom huset och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Spånga",
  "rot": [
    "Att riva väggar och bygga om planlösningen i ett hus, arbeta med tilläggsisolering och installera och rengöra ventilation räknas som rotarbete på småhus enligt Skatteverket. Är bostaden yngre än fem år får arbetet bara återställa det ursprungliga skicket.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor ger inget avdrag.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Spånga?",
  "price": [
    "Husets storlek och ålder, hur mycket av stommen som ändras, ventilationslösningen, el och VVS och vilka ytskikt du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur stora var tomterna i Solhem?",
     "Stora. Enligt stadens strategi fanns det i Solhem stora tomter där bara en tiondel av tomten fick bebyggas."),
    ("Vilket ventilationssystem har en äldre villa i Spånga?",
     "Ofta självdrag, enligt Stockholms stad, med luft som sugs ut via skorstenskanalen i kök och badrum. Systemet ger ingen rening av tilluften och ingen värmeåtervinning."),
    ("Är Solhem en kulturhistoriskt värdefull miljö?",
     "Ja, i stadens strategi för småhus- och villaområden är Solhem markerat som kulturhistoriskt värdefull miljö."),
    ("Kan vi lita på ritningarna till vår villa i Solhem?",
     "Inte helt. Stockholms stad påpekar att ritningar kan vara ofullständiga och att det inte är säkert att de som byggde följde dem."),
    ("Hjälper staden oss att avgöra om en vägg är bärande?",
     "Nej. Staden skriver att den inte kan bedöma det och råder dig att kontakta en konstruktör."),
    ("Behöver vi anmäla en ny ventilation i villan i Bromsten?",
     "Ja, installation eller väsentlig ändring av ventilationen kräver anmälan och startbesked."),
    ("Varför fungerar självdraget sämre på sommaren?",
     "För att draget bygger på temperaturskillnaden mellan ute och inne. När den är liten uteblir drageffekten, skriver staden."),
    ("Ger totalrenoveringen av villan rotavdrag?",
     "Ja, för arbetskostnaden, till exempel att riva väggar, bygga om planlösningen och tilläggsisolera."),
  ],
  "sources": [_VARSAM, ("Stockholms stad – Områdesfakta 2025: Solhem (pdf)", _OF + "vasterort/jarva/solhem.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Bromsten (pdf)", _OF + "vasterort/jarva/bromsten.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Flysta (pdf)", _OF + "vasterort/jarva/flysta.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Sundby (pdf)", _OF + "vasterort/jarva/sundby.pdf"),
              _STH_BAR, _STH_VENT, _STH_PLAN, _SKV, _SKV2],
  "cta": ("Ska villan i Spånga totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom huset och stommen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre villa i puts och trä med glasveranda på en stor tomt",
     "1920s Swedish villa with light plaster and wooden details, glazed veranda, red clay tile roof and a chimney, large garden with old fruit trees, quiet villa street in northwestern Stockholm, early autumn" + _IMG_END),
    ("Villagata med hus från flera tidsperioder och mogna trädgårdar",
     "Swedish villa street with houses from different periods: a 1910s wooden villa, a 1950s plastered house and a 1990s house, mature gardens and hedges, summer daylight" + _IMG_END),
    ("Rum under renovering med gammal murad eldstad och nedriven väggbeklädnad",
     "interior of an old Swedish villa during renovation: a wall opened to reveal timber studs next to an old plastered brick chimney stack, floor protected, construction light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ TYRESÖ
"totalrenovering-tyreso.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Tyresö", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Tyresö – avfallet, ritningar och eldstad",
  "description": "Totalrenovering i Tyresö: sortering av bygg- och rivningsavfall, asbest och asfalt, husets handlingar i bygglovsarkivet och regler för eldstaden.",
  "h1": "Totalrenovering i Tyresö",
  "lead": "En totalrenovering börjar med rivning, och i Tyresö ska rivningsavfallet sorteras redan på plats. Geal Entreprenad AB totalrenoverar villor och fritidshus i Tyresö och planerar rivningen, ritningarna och eldstaden innan arbetet börjar.",
  "card": "Rivningsavfallet, arkivet och eldstaden.",
  "sections": [
    {"id": "avfallet-tyreso", "anchor": "Rivningsavfallet",
     "h2": "Sortera rivningsavfallet på plats",
     "paras": [
       "Tyresö kommun skriver att bygg- och rivningsavfall ska sorteras där det uppstår, och att det gäller både privatpersoner och yrkesmässiga verksamheter. Minst trä, mineral av betong, tegel, klinker, keramik eller sten, metall, glas, plast och gips ska sorteras ut, och även andra avfallsslag om det ger bättre behandling.",
       "Är avfallet förorenat eller går inte att separera kan du ansöka om undantag, och den som anser att undantag gäller bör dokumentera det så att det kan visas vid ett tillsynsbesök. Vi ställer upp behållare för varje fraktion och planerar rivningen så att materialen hålls isär från början.",
     ],
     "aside": {"title": "Ska sorteras ut", "items": [
       "Trä", "Betong, tegel, klinker, keramik, sten", "Metall", "Glas", "Plast", "Gips"]}},
    {"id": "asbest-tyreso", "h2": "Asbest och asfalt går till Kovik",
     "paras": [
       "Asfalt och asbest kan inte lämnas på kretsloppscentralen. Tyresö kommun har avtal med Koviks återvinningsanläggning i Gustavsberg på Värmdö, dit hushåll kan lämna dem. Asbest ska vara väl förpackad i tätslutande emballage och lämnas med en ifylld blankett för grundläggande karakterisering.",
       "Uppbruten asfalt måste först analyseras på ett ackrediterat laboratorium för PAH-16, eftersom den kan innehålla stenkolstjära. Kommunen har också avtal med fyra godkända entreprenörer som mot kostnad kan hämta bygg- och rivningsavfall hos privatpersoner.",
     ],
     "aside": None},
    {"id": "arkivet-tyreso", "h2": "Husets handlingar i bygglovsarkivet",
     "paras": [
       "Handlingar beställs i kommunens e-tjänst och skickas via e-post. De flesta av Tyresös bygglovshandlingar finns digitalt, men vissa äldre finns bara i det fysiska arkivet, och för de allra äldsta byggnaderna kan det vara svårt att få fram dokumentation. Vanligast är situationsplan och plan-, fasad- och sektionsritningar, ibland också konstruktionsritningar.",
       "Kommunen påpekar att ritningarna inte behöver stämma med hur det ser ut i dag och att du bör kontrollmäta inför egna byggprojekt. Ritningar över vatten och avlopp finns bara om de någon gång har skickats in, annars vet kommunen inget om ledningarna på fastigheten. Vi mäter därför upp huset och letar upp ledningarna själva.",
     ],
     "aside": {"title": "Vanliga handlingar i arkivet", "items": [
       "Situationsplan", "Plan-, fasad- och sektionsritningar", "Ibland konstruktionsritningar"]}},
    {"id": "eldstaden-tyreso", "h2": "Eldstaden i en totalrenovering",
     "paras": [
       "Att installera eller ändra en eldstad kräver inte bygglov i sig, men en anmälan och ett startbesked, skriver Tyresö kommun. Det gäller en ny eldstad, braskamin, öppen spis, skorsten eller rökkanal, en braskassett eller spisinsats som ändrar eldningsförhållandena och byte till en tyngre eldstad. För en ny skorsten eller utvändig rökkanal kan bygglov behövas.",
       "Byter du till en likvärdig eldstad, byter eldstadsplan eller sätter insatsrör i befintlig skorsten behövs ingen anmälan. Bygglov krävs för en ny kamin med utvändig skorsten inom ett område som är utpekat som särskilt värdefullt. Om badrummet kan du läsa under " + _L.format("badrumsrenovering-tyreso.html", "badrumsrenovering i Tyresö") + ", och om tjänsten i stort under " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
    {"id": 'kontrollplanen-tyreso', "h2": 'Kontrollplanen i Tyresö',
     "paras": [
       'Tyresö kommun beskriver kontrollplanen som det samlade dokument som visar de kontroller byggherren ska göra. Den som bygger upprättar förslaget, ibland med hjälp av kontrollansvarig eller entreprenör, och där anges vad som ska kontrolleras, vilka anmälningar som ska göras och vilka intyg som ska lämnas in. Kommunen ska godkänna planen innan startbesked ges.',
       'När arbetet är klart ska kontrollplanen signeras och lämnas in med begäran om slutbesked. Kommunen påminner om att Boverkets nya byggregler, som gäller från 1 juli 2025, bygger på funktionskrav, och att byggherren behöver kunna visa hur kraven uppfylls och kontrolleras.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Tyresö till",
  "steps": [
    ("Handlingar", "Husets ritningar beställs från bygglovsarkivet och jämförs med huset."),
    ("Platsbesök", "Stomme, installationer, eldstad och material som ska rivas går vi igenom."),
    ("Skriftligt kostnadsförslag", "Rivning, avfall, stomme, installationer och ytskikt står var för sig."),
    ("Rivning och sortering", "Materialen sorteras på plats; asbest förpackas och lämnas separat."),
    ("Ombyggnad", "Stomme, el, VVS, isolering och ytskikt; anmälan för eldstaden vid behov."),
    ("Genomgång", "Vi går igenom huset och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Tyresö",
  "rot": [
    "Skatteverket räknar att riva väggar och bygga om planlösningen, tilläggsisolera, sanera asbest i samband med byggarbete och byggstäda efter rotarbetet som rotarbete på småhus. Att mura och reparera skorstenar, murstockar, öppna spisar och kakelugnar ger också avdrag, men inte att kontrollera eldstäder och skorstenar.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor ger inget avdrag.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Tyresö?",
  "price": [
    "Husets storlek, hur mycket som rivs, om asbest måste hanteras, hur mycket av stommen och installationerna som byts, eldstaden och vilka ytskikt du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka material ska sorteras ut vid rivningen i Tyresö?",
     "Minst trä, mineral av betong, tegel, klinker, keramik eller sten, metall, glas, plast och gips, enligt kommunen."),
    ("Kan vi lämna asbest på kretsloppscentralen i Tyresö?",
     "Nej. Asbest och asfalt lämnas på Koviks återvinningsanläggning, väl förpackat och med en blankett för grundläggande karakterisering."),
    ("Stämmer ritningarna från Tyresös bygglovsarkiv med huset?",
     "Inte nödvändigtvis. Kommunen påpekar att de inte behöver överensstämma med hur det ser ut i dag och att du bör kontrollmäta."),
    ("Måste vi anmäla en ny braskamin i Tyresö?",
     "Ja. En ny eldstad eller braskamin kräver anmälan och startbesked, men inte bygglov i sig."),
    ("Behöver vi anmäla insatsrör i den gamla skorstenen?",
     "Nej. Tyresö kommun räknar insatsrör och glidgjutning som underhåll som inte kräver anmälan."),
  ],
  "sources": [_TY_AVF, _TY_ARK, _TY_ELD, _SKV, _SKV2],
  "cta": ("Ska huset i Tyresö totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom huset, rivningen och handlingarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa i trä bland tallar och stora stenblock",
     "1960s Swedish wooden villa among pine trees and granite outcrops with scaffolding along one gable during renovation, gravel driveway, Stockholm archipelago suburb, daylight" + _IMG_END),
    ("Containrar med rivningsmaterial utanför ett hus under renovering",
     "several construction waste skips on a gravel driveway next to a house under renovation, separately filled with timber offcuts, scrap metal and broken plasterboard, neat and sorted, daylight" + _IMG_END),
    ("Ny kamin med golvplåt framför en putsad skorstensmur",
     "living room in a Swedish house under renovation with a newly installed black cast iron wood stove in front of a plastered chimney, fireproof floor plate, walls primed, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VÄRMDÖ
"totalrenovering-varmdo.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Värmdö", "svc_label": "Totalrenovering",
  "title": "Totalrenovering på Värmdö – VVS, varmvatten och nya regler",
  "description": "Totalrenovering på Värmdö: Boverkets nya byggregler, ledningarna från förbindelsepunkten, legionella och varmvattentemperaturer och vattnets hårdhet.",
  "h1": "Totalrenovering på Värmdö",
  "lead": "När ett hus på Värmdö totalrenoveras och rören byts gäller nya byggregler, regler för ledningarna på tomten och regler för varmvattnet. Geal Entreprenad AB totalrenoverar villor och fritidshus på Värmdö och planerar VVS:en för hela huset på en gång.",
  "card": "VVS, varmvattnet och byggreglerna.",
  "sections": [
    {"id": "reglerna-varmdo", "anchor": "Byggreglerna",
     "h2": "Boverkets nya byggregler gäller nu fullt ut",
     "paras": [
       "Värmdö kommun förklarar att Boverkets nya byggregler trädde i kraft den 1 juli 2025 och ersatte Boverkets byggregler, BBR, och de europeiska konstruktionsstandarderna, EKS. Under en övergångsperiod till och med den 30 juni 2026 kunde man välja gamla eller nya regler, och efter den 1 juli 2026 gäller bara de nya.",
       "Reglerna utgår från funktionskrav för säkerhet, energi, hälsa och tillgänglighet, och byggherren måste kunna visa att lösningarna uppfyller dem genom dokumentation, beräkningar eller branschstandarder. Kontrollplanen ska redovisa vilket regelverk som tillämpas, hur de tekniska kraven uppfylls och vilka riskmoment och kontrollpunkter som finns.",
     ],
     "aside": {"title": "Datumen", "items": [
       "1 juli 2025: nya regler i kraft", "Till 30 juni 2026: valfritt", "Från 1 juli 2026: bara nya regler"]}},
    {"id": "ledningarna-varmdo", "h2": "Ledningarna från förbindelsepunkten",
     "paras": [
       "När kommunen bygger ut vatten och avlopp görs en förbindelsepunkt till varje fastighet, normalt omkring en halvmeter från fastighetsgränsen. Kommunen ansvarar för ledningarna fram till förbindelsepunkten och fastighetsägaren för ledningarna därifrån fram till huset, och kostnaden för ledningsdragningen på fastigheten tillkommer.",
       "Inom ett verksamhetsområde för kommunalt vatten och avlopp är fastighetsägaren skyldig att betala avgifter, och när förbindelsepunkten är upprättad ska anläggningsavgiften betalas. Ansluts huset i samband med totalrenoveringen planerar vi de nya ledningarna inomhus så att de möter servisen på rätt ställe.",
     ],
     "aside": None},
    {"id": "varmvattnet-varmdo", "h2": "Varmvattnet och legionella",
     "paras": [
       "Värmdö kommun skriver att legionellabakterier växer i temperaturer mellan 20 och 45 grader, främst i vattenledningar, och särskilt i blindledningar, termostatblandare och duschslangar. I varmvattenberedaren ska temperaturen vara minst 60 grader, vid tappstället minst 50 och högst 65 grader, och kallvattnet ska hålla högst 18 grader.",
       "Kommunen råder att blindledningar tas bort, att varm- och kallvattenledningar isoleras så att de inte påverkar varandra och att handdukstorkare, golvvärme och andra värmare inte kopplas på cirkulationsledningar för tappvarmvatten. När alla rör ändå byts är det rätt tillfälle att bygga bort gamla blindledningar.",
     ],
     "aside": {"title": "Temperaturer enligt kommunen", "items": [
       "Varmvattenberedare: minst 60 °C", "Tappställe: 50–65 °C", "Kallvatten: högst 18 °C"]}},
    {"id": "vattnet-varmdo", "h2": "Vattnet skiljer sig åt på Värmdö",
     "paras": [
       "Dricksvattnet på Värmdö kommer från kommunens vattenverk och från Stockholm vatten via Nacka, och kommunen köper ungefär hälften av behovet från Stockholm vatten. Vattnet från Ingarö vattenverk beskrivs som mellanhårt till hårt, ungefär 9–11 °dH, medan Stockholm vattens vatten är mjukt, kring 4,5–5 °dH.",
       "Vi frågar därför var husets vatten kommer ifrån när blandare, beredare och rör väljs. Om badrummet kan du läsa under " + _L.format("badrumsrenovering-varmdo.html", "badrumsrenovering på Värmdö") + ", om köket under " + _L.format("koksrenovering-varmdo.html", "köksrenovering på Värmdö") + " och om tjänsten i stort under " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
    {"id": 'deklarationen-varmdo', "h2": 'Energideklarationen efter ombyggnaden',
     "paras": [
       'Värmdö kommun beskriver energideklarationen som en redovisning av husets energianvändning, med uppgifter om energiprestanda, ventilationskontroll och eventuell radonmätning. Den görs av en oberoende expert och gäller i tio år. När en bostad säljs eller hyrs ut ska energiprestandan anges i annonsen, och saknas deklaration får köparen låta upprätta en på säljarens bekostnad senast sex månader efter tillträdet.',
       'En totalrenovering ändrar ofta husets energiprestanda. Vi sparar uppgifter om isolering, fönster, ventilation och värme så att en ny deklaration blir enkel att göra.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering på Värmdö till",
  "steps": [
    ("Platsbesök", "Stomme, rör, beredare, avlopp och vattenkälla går vi igenom."),
    ("Regelverk och kontrollplan", "Kontrollplanen tas fram enligt de nya byggreglerna."),
    ("Skriftligt kostnadsförslag", "Rivning, stomme, VVS, el och ytskikt står var för sig."),
    ("Rivning", "Gamla rör och blindledningar rivs ut och materialen sorteras."),
    ("Ombyggnad", "Nya ledningar, beredare, el, isolering och ytskikt."),
    ("Genomgång", "Vi går igenom huset, temperaturerna och dokumentationen med dig."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen på Värmdö",
  "rot": [
    "För ett småhus ger Skatteverket rotavdrag för att dra in och reparera el-, vatten- och avloppsledningar, också vid indragning av kommunalt vatten och avlopp, och för att installera blandare, toalett, dusch och element. Rotavdrag ges för en bostad som du äger och bor i eller använder som fritidsbostad.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor ger inget avdrag.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen på Värmdö?",
  "price": [
    "Husets storlek, hur mycket av stommen som ändras, om alla rör byts, anslutning till kommunalt vatten och avlopp, el och vilka ytskikt du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Var kommer vattnet från på Ingarö?",
     "Från grundvattentäkter vid Brunn och Fågelvik via Ingarö vattenverk, där vattnet luftas och behandlas med UV-ljus, enligt Värmdö kommun."),
    ("Hur länge gäller en energideklaration?",
     "I tio år, enligt Värmdö kommun. Den görs av en oberoende expert och innehåller bland annat husets energiprestanda."),
    ("Kan vi välja de gamla byggreglerna för vår ombyggnad på Värmdö?",
     "Inte längre. Övergångsperioden löpte till och med den 30 juni 2026, och efter den 1 juli 2026 gäller bara Boverkets nya byggregler."),
    ("Var går gränsen för vårt ansvar för vatten och avlopp?",
     "Vid förbindelsepunkten, normalt omkring en halvmeter från fastighetsgränsen. Därifrån till huset ansvarar fastighetsägaren."),
    ("Vilken temperatur ska varmvattnet ha?",
     "Minst 60 grader i beredaren och minst 50 grader vid tappstället, men högst 65 grader på grund av skållningsrisken, enligt kommunen."),
    ("Får golvvärmen i badrummet kopplas på varmvattencirkulationen?",
     "Nej, kommunen råder att handdukstorkare, golvvärme och andra värmare inte kopplas på cirkulationsledningar för tappvarmvatten."),
    ("Ger nya vattenledningar i huset rotavdrag?",
     "Ja, för arbetskostnaden. Skatteverket räknar indragning och reparation av vatten- och avloppsledningar som rotarbete på småhus."),
  ],
  "sources": [_VA_NYA, _VA_KVA, _VA_LEG, _SKV, _SKV2],
  "cta": ("Ska huset på Värmdö totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom huset och VVS:en innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa i trä bland tallar nära vattnet i skärgården",
     "Swedish wooden villa painted dark red with white trim among pine trees on a rocky plot with a glimpse of the archipelago sea, gravel path, late summer daylight" + _IMG_END),
    ("Varmvattenberedare och nydragna kopparrör i ett teknikutrymme",
     "neat utility room in a Swedish house with a new stainless steel water heater, insulated copper and PEX pipes running along the wall, new shut-off valves, clean concrete floor, bright light" + _IMG_END),
    ("Badrumsvägg under renovering med en öppen nisch för rörinstallationer",
     "bathroom wall under renovation with newly installed water pipes in protective conduits and a recessed distribution box, before boarding, construction light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"totalrenovering-osteraker.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Österåker", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Österåker – fritidshuset blir året runt",
  "description": "Totalrenovering i Österåker: fritidshusområden som blir permanentboende, eget avlopp och brunn, anmälningspliktiga åtgärder, värmepump och ditt ansvar.",
  "h1": "Totalrenovering i Österåker",
  "lead": "Utanför tätorten i Österåker blir fritidshusområden permanentboende, och hus som byggdes för sommaren ska fungera året runt. Geal Entreprenad AB totalrenoverar villor och fritidshus i Österåker och planerar vatten, avlopp och värme från början.",
  "card": "Fritidshuset, värmen och anmälan.",
  "sections": [
    {"id": "fritidshusen-osteraker", "anchor": "Fritidshusen",
     "h2": "Från fritidshus till permanentboende",
     "paras": [
       "Österåkers kommun beskriver sig som en kommun som expanderar snabbt, där flera områden utanför tätorten utvecklas från fritidshusområden till mer permanent boende. I vissa av dem finns ännu inget kommunalt vatten och avlopp, och då måste de boende ha eget avlopp och egen brunn.",
       "Roslagsvatten har hand om det kommunala vattnet och avloppet och utökar antalet anslutna områden. Kommunens VA-plan innehåller en gemensam utbyggnadsplan för det allmänna nätet och en strategi för de enskilda anläggningarna, och i mars 2025 antog kommunfullmäktige kommunens första vattentjänstplan.",
     ],
     "aside": {"title": "Frågor att ställa först", "items": [
       "Kommunalt VA eller eget avlopp?", "Egen brunn?", "Detaljplan, kulturmiljö, strandskydd?"]}},
    {"id": "anmalan-osteraker", "h2": "Det som ska anmälas i en ombyggnad",
     "paras": [
       "Österåkers kommun listar åtgärder som kräver anmälan även när de inte kräver lov: installation av kamin eller eldstad, installation eller väsentlig ändring av vatten och avlopp i en byggnad, ändring av bärande väggar och balkar, nya eller förändrade rördragningar inne i bjälklag, ändring som väsentligt påverkar brandskyddet, ny eller ändrad ventilation och stambyte.",
       "Till anmälan hör ett förslag till kontrollplan och de handlingar som behövs, till exempel VA-situationsplan, konstruktionsritningar, planritning, VVS-ritning och brandskyddsdokumentation. Arbetet får inte börja förrän startbeskedet har kommit. I en totalrenovering hamnar ofta flera av punkterna i samma anmälan.",
     ],
     "aside": {"title": "Kräver anmälan i Österåker", "items": [
       "Kamin eller eldstad", "Ändrat vatten och avlopp", "Bärande väggar och balkar", "Rör i bjälklag",
       "Ventilation", "Stambyte"]}},
    {"id": "varmen-osteraker", "h2": "Värmepump i ett hus som ska bo året runt",
     "paras": [
       "En värmepump som hämtar värme från berg, jord, sjövatten eller havsvatten måste först anmälas till kommunen, medan luftvärmepumpar inte är anmälningspliktiga. Inom ett vattenskyddsområde krävs tillstånd, ska borrhålet ligga nära en kommunal dagvattenledning ska det anmälas till Roslagsvatten, och värmeutvinning ur grundvatten är inte tillåtet i Österåker.",
       "Borrvatten och borrkax får inte ledas till avloppsnätet utan rening. Vid borrning ska SGU:s standard Normbrunn 16 följas, och normen anger också regler om avstånd till andra brunnar. Vi dimensionerar värmesystemet efter det renoverade huset, inte efter fritidshuset det var, och planerar borrhål och ledningar så att de passar husets nya planlösning och värmesystem.",
     ],
     "aside": None},
    {"id": "ansvaret-osteraker", "h2": "Mer frihet, mer eget ansvar",
     "paras": [
       "Från den 1 december 2025 gäller nya regler i plan- och bygglagen. Fler åtgärder är bygglovsbefriade, men kommunen granskar inte dina planer innan du börjar bygga, och du ansvarar själv för att det du bygger uppfyller kraven. Bygger du fel kan kommunen ingripa i efterhand med byggsanktionsavgift eller krav på rivning.",
       "Kommunen råder dig att först kontrollera detaljplan, kulturmiljö och strandskydd, och den som är osäker kan söka frivilligt bygglov. Om badrummet kan du läsa under " + _L.format("badrumsrenovering-osteraker.html", "badrumsrenovering i Österåker") + ", och om tjänsten i stort under " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
    {"id": 'solen-osteraker', "h2": 'Energideklaration och solceller',
     "paras": [
       'Alla småhus som säljs ska ha en energideklaration, och den innehåller förslag på åtgärder som sänker energianvändningen utan att försämra inomhusmiljön, skriver Österåkers kommun. Deklarationen gäller i tio år, och husägaren ansvarar för att den görs och godkänns.',
       'Solceller på fasaden eller taket kan kräva bygglov. Kommunen råder dig att kontakta elnätsägaren, i Österåker E.ON, innan du tar in offerter, och påpekar att solceller kan ge skattereduktion för grön teknik. Ska taket ändå göras om i totalrenoveringen planerar vi infästningar och kabelvägar samtidigt.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Österåker till",
  "steps": [
    ("Platsbesök", "Stomme, vatten, avlopp, värme och detaljplan går vi igenom."),
    ("Anmälan", "Anmälan och kontrollplan för VA, bärande delar, ventilation och eldstad."),
    ("Skriftligt kostnadsförslag", "Stomme, VVS, värme, el och ytskikt står var för sig."),
    ("Rivning", "Det gamla rivs och materialen sorteras."),
    ("Ombyggnad", "Stomme, isolering, VVS, värme, el och ytskikt i rätt ordning."),
    ("Slutbesked", "Kontrollplanen fylls i så att slutbesked kan ges."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Österåker",
  "rot": [
    "Rotavdrag ges för en bostad som du äger och bor i eller använder som fritidsbostad. På småhus räknar Skatteverket bland annat ombyggnad av planlösningen, tilläggsisolering, vatten- och avloppsledningar och installation av värmepumpar som rotarbete, men rotavdrag och skattereduktion för grön teknik kan inte ges för samma arbete.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Österåker?",
  "price": [
    "Husets storlek och skick, isolering, om vatten och avlopp ska dras om, värmesystemet, el och vilka ytskikt du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka handlingar behövs till en anmälan i Österåker?",
     "Förslag till kontrollplan och de handlingar som projektet kräver, till exempel VA-situationsplan, konstruktionsritningar, planritning, VVS-ritning och brandskyddsdokumentation."),
    ("Vem har hand om det kommunala vattnet i Österåker?",
     "Roslagsvatten. Gäller frågan enskilt vatten och avlopp vänder du dig i stället till kommunens miljö- och hälsoskyddsavdelning."),
    ("Vem ska vi kontakta innan vi skaffar solceller i Österåker?",
     "Elnätsägaren, som i Österåker är E.ON, enligt kommunen. Solceller på fasad eller tak kan också kräva bygglov."),
    ("Måste vi anmäla nya rör i bjälklaget när fritidshuset i Österåker byggs om?",
     "Ja. Kommunen listar nya eller förändrade rördragningar inne i bjälklag bland de åtgärder som kräver anmälan."),
    ("Får vi borra för bergvärme i Österåker?",
     "Ja, efter anmälan till kommunen. Inom vattenskyddsområde krävs tillstånd, och värmeutvinning ur grundvatten är inte tillåtet."),
    ("Behöver en luftvärmepump anmälas i Österåker?",
     "Nej. Anmälningsplikten gäller inte värmepumpar som har luft som värmekälla."),
    ("Vem granskar ombyggnaden om den inte kräver lov?",
     "Ingen i förväg. Sedan den 1 december 2025 ansvarar du själv för att kraven uppfylls, och kommunen kan ingripa i efterhand."),
    ("Ger totalrenoveringen av fritidshuset rotavdrag?",
     "Ja, Skatteverket ger rotavdrag även för en bostad som du använder som fritidsbostad, för arbetskostnaden."),
  ],
  "sources": [_OS_VA, _OS_ANM, _OS_EN, _OS_HUS, _SKV, _SKV2],
  "cta": ("Ska huset i Österåker byggas om för året runt?", "Boka ett gratis platsbesök, så går vi igenom huset, vattnet och värmen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Fritidshus i trä bland tallar som byggs om till året runt-bostad",
     "small red Swedish wooden summer house among pine trees in Roslagen being renovated into a year-round home, new windows installed, insulation boards stacked on the porch, scaffolding at one side, daylight" + _IMG_END),
    ("Uppgrävt schakt med ny ledning fram till ett trähus i skogen",
     "geothermal borehole cap with new collector hoses running toward the foundation of a Swedish wooden house, freshly dug gravel trench, pine trees, daylight" + _IMG_END),
    ("Bjälklag med nydragna rör och isolering under ett nytt golv",
     "opened timber floor structure in an old Swedish house with newly installed water and drain pipes running between the joists and fresh mineral wool insulation, construction light" + _IMG_END),
  ],
},
}
