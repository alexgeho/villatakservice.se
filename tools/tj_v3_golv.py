# -*- coding: utf-8 -*-
"""Golvläggare – ortsidor v3: Bromma, Nacka, Solna, Täby, Lidingö, Huddinge (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade 2026-10-25: Stockholmskällan/Stadsmuseet
(Stockholms spår: Stora mossen, Abrahamsberg, Solna centrum, Näckrosen), Nacka kommun
(kulturmiljöprogram Sommarnöjen vid farleden, anmälan bärande konstruktion), SCB (bostadsbeståndet
2024), Solna stad (guide för lägenhetsinnehavare), Täby kommun (Kulturmiljöer i Täby), Lidingö stad
(kulturmiljöprogram del 2: Tjädervägen, Hersby Gärde), Huddinge kommun (kulturmiljöprogram del 2),
riksdagen.se (bostadsrättslagen 7 kap. 7 och 12 §§), Golvbranschen (uttorkning, limrekommendationer),
Byggkeramikrådet (vanliga frågor), Skatteverket (rotarbeten, så fungerar rotavdraget).
Strukna (ej verifierade): stegljudskrav, golvtyper i originalutförande per område, grundläggning
(platta på mark/krypgrund) per område. Inga priser, garantier, omdömen, case eller cert.
Schema: se tools/tj_check.py."""

_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_GBR_U = ("Golvbranschen – Uttorkning av golvavjämning",
          "https://www.golvbranschen.se/teknik--material/golvavjamning/uttorkning-av-golvavjamning/")
_GBR_L = ("Golvbranschen – Samlade limrekommendationer", "https://golvbranschen.se/rad-riktlinjer/limrekommendationer")
_BKR = ("Byggkeramikrådet – Vanliga frågor", "https://www.bkr.se/vanliga-fragor")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 och 12 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"golvlaggare-bromma.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Bromma", "svc_label": "Golvläggare",
  "title": "Golvläggare i Bromma – trägolv i villa och smalhus",
  "description": "Golvläggare i Bromma: slipning av gamla trägolv i 1920-talsvillor, nytt golv i smalhusens lägenheter och fuktkoll i källaren. Gratis platsbesök.",
  "h1": "Golvläggare i Bromma",
  "lead": "Bromma rymmer både trädgårdsstädernas villor från 1920-talet och de gula och röda smalhusen från åren kring andra världskriget. Golvjobben ser olika ut i de två miljöerna: i villan handlar det ofta om att ta fram och slipa det gamla trägolvet, i lägenheten om att lägga nytt utan att störa föreningen. Geal Entreprenad AB lägger och slipar golv i hela Bromma, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villor i trädgårdsstäderna och lägenheter i smalhus.",
  "sections": [
    {"id": "stora-mossen", "anchor": "Villorna i Bromma",
     "h2": "Stora Mossen och de sena 1920-talens villor",
     "paras": [
       "Stadsmuseets text om Stora Mossen beskriver hur planerna för området fastslogs 1926, som en fortsättning på de trädgårdsstäder som funnits i Äppelviken och Ulvsunda sedan 1910-talet. En stor del av husen stod klara 1927–1929. De är nästan identiska: två våningar, flacka sadeltak, enkla rektangulära planer och relativt stora fönster. De flesta ritades av arkitekten Edvin Engström, med klassicistiska villor i den östra delen och funktionalistiska i den västra.",
       "För golvläggaren betyder ett sådant hus att det kan finnas mer under ytan än man tror. Under en heltäckningsmatta eller en senare plastmatta ligger ibland de ursprungliga brädorna kvar. Innan något rivs lyfter vi därför en golvlist eller en tröskel i ett hörn och tittar på vad som finns under – det avgör om rummet ska slipas eller få ett nytt golv.",
     ],
     "aside": {"title": "Titta efter innan du river", "items": [
       "Vad ligger under mattan?", "Är brädorna hela eller kapade?",
       "Rör sig golvet när du går?", "Finns gamla lim- eller spackelrester?"]}},
    {"id": "slipa-bromma", "h2": "Ta fram brädorna eller lägga ett nytt golv",
     "paras": [
       "Ett gammalt trägolv som har legat dolt i årtionden är ofta i bättre skick än det slitna golvet runt omkring, eftersom mattan har skyddat det. Spikhål, missfärgningar efter mattlim och enstaka skadade brädor går att åtgärda: hålen fylls, de sämsta brädorna byts mot likvärdiga och golvet slipas i flera omgångar innan det får sin nya yta.",
       "Ibland är det ändå bättre att lägga nytt. Har brädorna kapats vid en tidigare ombyggnad, saknas stora partier eller sviktar golvet för att bjälklaget har satt sig, blir det ett nytt golv ovanpå ett upprättat underlag. Vilken väg som är rimligast skriver vi in i kostnadsförslaget, så att du kan jämföra. Mer om material och ytbehandlingar finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "smalhus", "h2": "Lägenhet i den gula eller den röda staden",
     "paras": [
       "Abrahamsberg och Åkeslund stadsplanerades i slutet av 1930-talet och byggdes 1937–1945 med smalhus i tre våningar. Enligt Stadsmuseet var idealet hus i park, där varje lägenhet skulle få sol, ljus och luft. Abrahamsberg byggdes av gult tegel och kallades den gula staden, Åkeslund av rött tegel och blev den röda staden.",
       "Bor du i bostadsrätt i ett av husen säger bostadsrättslagen att du på egen bekostnad ska hålla lägenheten i gott skick, och golvet ingår normalt i det ansvaret om stadgarna inte säger annat. Samtidigt kräver lagens 7 kap. 7 § styrelsens tillstånd för bland annat ingrepp i bärande konstruktion och ändring av ledningar för värme eller vatten. Ett vattenburet golvvärmesystem kopplat till husets värme är ett sådant fall. Byts golvet i ett badrum blir det ett våtrumsjobb – se " + _L.format("badrumsrenovering-bromma.html", "badrumsrenovering i Bromma") + ".",
     ],
     "aside": {"title": "Fråga styrelsen om", "items": [
       "Stadgarnas regler för golvbyte", "Krav på underlag eller ljuddämpning",
       "Golvvärme kopplad till husets värme", "Tider för bullrande arbete"]}},
    {"id": "kallare-bromma", "h2": "Golv på betong i villans källare",
     "paras": [
       "Har villan en källare som har gjorts om till tvättstuga, gästrum eller arbetsrum ligger golvet där oftast på betong, och trä tar upp fukt och sväller när den relativa fuktigheten är hög. Golvbranschen rekommenderar att fukten i bjälklaget kontrolleras innan avjämningsmassa läggs, och att mätningen görs av en fuktkontrollant inom RBK.",
       "Branschens limrekommendationer lägger ansvaret för att mätningen blir gjord på beställaren. I praktiken samordnar vi den åt dig, så att resultatet finns innan material beställs och golvtyp väljs.",
     ],
     "aside": None},
    {"id": "yta-bromma", "h2": "Ytan på ett framtaget golv",
     "paras": [
       "Ett golv som har legat under en matta i många år har ofta en annan ton än man väntar sig när det är nyslipat. Därför gör vi en provyta på ett undanskymt ställe, till exempel i en garderob, innan hela rummet behandlas. Där syns hur träet tar emot lack, olja eller såpa och om missfärgningar efter mattlimmet behöver döljas med en pigmenterad behandling.",
       "I hall och kök, där det slits mest, brukar en tålig lack vara det praktiska valet. I sovrum och vardagsrum kan en oljad yta passa bättre, eftersom den går att bättra där den slits utan att hela golvet slipas om.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett golvjobb i Bromma till",
  "steps": [
    ("Besök i huset", "Vi går igenom rummen, lyfter en list där det behövs och ser vad som ligger under nuvarande golv."),
    ("Slipa eller byta", "Du får vårt förslag på om golvet ska tas fram och slipas eller ersättas, och varför."),
    ("Kostnadsförslag", "Arbete och material står på separata rader, liksom förarbeten som rivning och uppriktning."),
    ("Förarbete", "Mattor och lim tas bort, lösa brädor skruvas fast och underlaget rätas upp."),
    ("Slipning eller läggning", "Golvet slipas i flera steg eller läggs nytt, och lister och trösklar anpassas."),
    ("Yta och genomgång", "Lack, olja eller såpa läggs på, och vi går igenom skötseln med dig."),
  ],
  "rot_h2": "ROT-avdrag för golv i Bromma",
  "rot": [
    "Att slipa och byta golv räknas som rotarbete hos Skatteverket, både i småhus och i bostadsrätt. I en bostadsrätt gäller avdraget arbete som utförs inne i bostaden. Att ta bort en plastmatta och lägga trägolv räknas som en förbättring och ger också avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "I en äldre villa avgör golvets skick under mattan och hur mycket bjälklaget behöver rättas upp mest. I en lägenhet väger rivning, bärande av material i trapphuset och föreningens krav på underlaget tyngre. Valet mellan slipning och nytt golv påverkar förstås också. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan det gamla trägolvet i vår villa i Stora Mossen vara kvar under mattan?",
     "Det är möjligt i ett hus från slutet av 1920-talet. Vi lyfter en list eller tröskel vid besöket och ser om brädorna finns kvar och är hela nog att slipa."),
    ("Behöver vi styrelsens tillstånd för nytt parkettgolv i Abrahamsberg?",
     "Ett vanligt golvbyte brukar inte kräva det enligt bostadsrättslagen, men ingrepp i bärande delar eller ledningar för värme och vatten gör det. Läs också stadgarna, föreningen kan ha egna regler."),
    ("Hur gör ni med limrester från en gammal matta på trägolvet?",
     "Resterna skrapas och slipas bort i de första grova stegen. Missfärgningar som sitter djupt kan synas kvar, och då diskuterar vi pigmenterad olja eller byte av enstaka brädor."),
    ("Vem beställer fuktmätningen på betongen i källaren?",
     "Enligt Golvbranschens limrekommendationer är det beställarens ansvar. Vi samordnar mätningen så att den görs innan golvmaterialet köps in."),
    ("Kan ett golv i en funkisvilla i västra Stora Mossen slipas lika mycket som i en äldre villa?",
     "Det beror inte på stilen utan på hur mycket trä som finns över sponten. Vi mäter vid besöket i stället för att gissa utifrån husets ålder."),
  ],
  "sources": [
    ("Stockholmskällan / Stadsmuseet – Stora mossen (Stockholms spår)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000051.pdf"),
    ("Stockholmskällan / Stadsmuseet – Abrahamsberg (Stockholms spår)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000009.pdf"),
    _BRL, _GBR_U, _GBR_L, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i Bromma slipas eller bytas?", "Boka ett gratis platsbesök så tittar vi under ytan och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat brett furugolv i ett ljust rum i en villa från 1920-talet i Bromma",
     "freshly sanded and oiled wide pine floorboards in an empty bright bedroom of a late 1920s Swedish classicist villa in Bromma Stockholm, white painted wooden skirting boards, tall window with white frame, view of garden with pine trees, soft daylight, no people, no text"),
    ("Hörn där heltäckningsmatta är uppvikt och ett äldre trägolv syns under",
     "corner of an empty room in an old Swedish villa where a worn beige wall-to-wall carpet is folded back revealing original wooden floorboards with old paint traces underneath, removed skirting board leaning against the wall, natural light, no people, no hands, no text"),
  ],
  "related": [
    ("malare-bromma.html", "Målare i Bromma", "Väggar och snickerier innan golvet läggs."),
    ("koksrenovering-bromma.html", "Köksrenovering i Bromma", "Nytt kök i villa och småstuga."),
  ],
},

# ------------------------------------------------------------------ NACKA
"golvlaggare-nacka.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Nacka", "svc_label": "Golvläggare",
  "title": "Golvläggare i Nacka – golv i sommarvillor och källarplan",
  "description": "Golvläggare i Nacka: golv i sommarnöjen som bebos året runt, bjälklag som behöver förstärkas och klinker i källarplanet. Gratis platsbesök.",
  "h1": "Golvläggare i Nacka",
  "lead": "Längs farleden i Nacka står villor som byggdes för somrar, med verandor, lusthus och sjöutsikt. I dag bor många där året om, och då ställs andra krav på golven än när huset stängdes på hösten. Geal Entreprenad AB lägger nya golv, slipar gamla och rättar till underlaget i hela Nacka, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Sommarvillor, stugor och hus med källarplan.",
  "sections": [
    {"id": "sommarnojen", "anchor": "Sommarvillorna",
     "h2": "Hus som byggdes för sommaren",
     "paras": [
       "Nacka kommuns kulturmiljöprogram om sommarnöjena vid farleden berättar att det var ångbåten som under senare delen av 1800-talet gjorde den strandnära villabebyggelsen möjlig. Husen kallas ofta grosshandlarvillor, eftersom det var grosshandlare och fabrikörer som hade råd och fritid att bygga dem. Snart kunde även hantverkare och lägre tjänstemän köpa ett eget sommarnöje eller hyra in sig i en större hyresvilla.",
       "Programmet skriver att de ljusa verandorna stod i skarp kontrast till vinterbostadens mörka, mer formella inredning. Sommarhuset var alltså tänkt som något lättare och enklare. Under 1900-talets första årtionden byggdes dessutom mindre sportstugor i skogsbackarna bakom villorna, och från 1930-talet även hus i funkisbetonad stil med lägre tak.",
       "Ett golv som bara användes några månader om året har ofta slitits mindre än man tror, men det har heller inte byggts för ett helt år av vardag. När huset blir permanentbostad är golvet en av de första sakerna som märks – det knarrar, sviktar eller är kallt mot fötterna.",
     ],
     "aside": {"title": "Vanliga frågor i ett gammalt sommarhus", "items": [
       "Sviktar golvet mellan bjälkarna?", "Är brädorna spikade eller skruvade?",
       "Har rummen byggts till i olika etapper?", "Skiljer det i höjd mellan rummen?"]}},
    {"id": "bjalklag-nacka", "h2": "När bjälklaget måste förstärkas",
     "paras": [
       "Ibland räcker det inte att byta ytskikt. Är golvbjälkarna för klena eller skadade behöver de förstärkas eller bytas, och då rör arbetet husets bärande konstruktion. Nacka kommun skriver att ändringar i bärande konstruktioner kräver en anmälan till bygglovenheten och att du, som vid ett bygglov, måste ha fått startbesked innan arbetet får börja.",
       "Därför bedömer vi bjälklaget vid besöket och säger till om ett åtgärdsförslag kräver anmälan. Gäller det bara ytskikt, nya skivor och att skruva fast lösa brädor rör arbetet normalt inte den bärande konstruktionen. Ska golvet i stället ligga kvar och bara få nytt liv kan det slipas – läs mer om " + _L.format("golvlaggning.html", "golvläggning och golvslipning") + ".",
     ],
     "aside": None},
    {"id": "kallarplan-nacka", "h2": "Klinker i källarplanet",
     "paras": [
       "I ett hus som står i en sluttning ligger nedre planet ofta delvis mot marken, och där kan markfukt komma underifrån. Byggkeramikrådet skriver att man i källare med markfukt generellt bör undvika alltför stora plattor och alltför smala fogar, och anger 900 cm² som största rekommenderade plattstorlek. Även flytspackel och spackel behöver väljas i nära samråd med leverantören.",
       "Ska det bli trä eller parkett i stället visar Golvbranschen att trä tar upp fukt och sväller när fuktigheten är hög. Betongen bör därför mätas innan något läggs. Är rummet ett badrum eller en tvättstuga blir det ett tätskiktsjobb, som vi tar inom " + _L.format("badrumsrenovering-nacka.html", "badrumsrenovering i Nacka") + ".",
     ],
     "aside": {"title": "I källarplanet", "items": [
       "Fuktmätning före läggning", "Måttliga plattstorlekar",
       "Spackel valt med leverantören", "Tätskikt i våta rum"]}},
    {"id": "stugor-nacka", "h2": "Små rum i sportstugor och funkishus",
     "paras": [
       "I en mindre stuga är golvytan liten men antalet övergångar stort. Varje rum kan ha sin egen nivå efter tillbyggnader, och dörrarna är sällan anpassade för ett tjockare golv. Vi planerar trösklar och höjder innan materialet väljs, så att dörrar inte behöver kapas i onödan och golvet inte får skarvar mitt i ett rum.",
       "Funkishusen från 1930-talet har ofta enklare och ljusare rum med få detaljer. Där passar ett golv med enkel läggning och en lugn yta, och det är ofta golvet som avgör om ett litet rum upplevs som öppet eller trångt. Vi visar prover på plats, så att du kan se materialet i husets eget ljus innan du bestämmer dig.",
     ],
     "aside": None},
    {"id": "varma-golv-nacka", "h2": "Ett golv som ska vara varmt året om",
     "paras": [
       "I ett hus som bara användes på sommaren var ett kallt golv sällan något problem. Bor man där i januari blir det tydligt. Ofta hänger det ihop med hur bjälklaget under är byggt och isolerat, och då är golvbytet ett bra tillfälle att se över konstruktionen innan det nya golvet läggs ovanpå.",
       "Kulturmiljöprogrammet nämner också äldre villor med en traditionell timmerstomme, som Grundet från 1868 vid Gustavsvik. I sådana hus kan golv och bjälkar ha rört sig under lång tid, och det nya golvet behöver kunna följa med huset i stället för att spricka i skarvarna. Vi väljer därför underlag och golvtyp efter hur huset faktiskt rör sig, inte bara efter utseendet.",
     ],
     "aside": None},
  ],
  "steps_h2": "Steg för steg i Nacka",
  "steps": [
    ("Genomgång på plats", "Vi känner på golvet, tittar på bjälklaget och mäter nivåskillnader mellan rummen."),
    ("Bedömning av underlaget", "Vi säger om det räcker att rikta upp eller om bjälkarna behöver förstärkas, och om det kräver anmälan."),
    ("Skriftligt förslag", "Du ser vad som är arbete, material och förarbete, och vad som ger ROT-avdrag."),
    ("Underlaget först", "Gamla golv tas bort, lösa delar fästs och nya skivor läggs där det behövs."),
    ("Nytt golv eller slipning", "Golvet läggs eller slipas, med trösklar och lister anpassade efter dörrarna."),
    ("Avslut", "Vi städar, går igenom golvet och lämnar råd om skötsel."),
  ],
  "rot_h2": "Rotavdrag för golvarbete i Nacka",
  "rot": [
    "Skatteverket räknar slipning och byte av golv som rotarbete i småhus. Avdraget gäller bara arbetskostnaden och är 30 procent av den, med ett tak på 50 000 kr per person och år och 75 000 kr tillsammans med rut. Golvmaterial och resor ger inget avdrag.",
    "Äger ni huset tillsammans och bor där båda kan avdraget delas, men det blir sammanlagt högst 30 procent av arbetskostnaden. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset?",
  "price": [
    "I ett gammalt sommarhus väger bjälklagets skick och antalet nivåskillnader mellan rummen tyngst, tillsammans med hur mycket som behöver rivas. I källarplanet styr fuktmätning, avjämning och plattval. Vi börjar med ett gratis platsbesök, och du får ett skriftligt kostnadsförslag innan något arbete beställs.",
  ],
  "faq": [
    ("Vårt sommarhus vid farleden i Nacka ska bli permanentbostad – måste golven bytas?",
     "Inte nödvändigtvis. Ofta går det att behålla brädorna och rätta till underlaget. Vi tittar på bjälklaget och golvets skick innan vi föreslår något."),
    ("Krävs anmälan till Nacka kommun om golvbjälkarna ska bytas?",
     "Bjälkarna är en del av den bärande konstruktionen. Nacka kommun kräver anmälan och startbesked för ändringar i bärande konstruktioner, så arbetet får inte börja innan beskedet finns."),
    ("Kan vi lägga stora klinkerplattor i källarplanet i vårt hus i sluttningen?",
     "Byggkeramikrådet avråder från alltför stora plattor i källare med markfukt och rekommenderar högst 900 cm² per platta. Vi mäter fukten och väljer format efter det."),
    ("Rummen i stugan ligger på olika höjd – kan golvet bli jämnt i hela huset?",
     "Ibland går det att jämna ut med nytt underlag, ibland är en tröskel det bästa. Vi mäter höjderna vid besöket och visar alternativen."),
    ("Går det att lägga parkett direkt på betongen i nedre planet?",
     "Det går om betongen är tillräckligt torr. Därför mäts fukten först, och golvet läggs med fuktspärr enligt leverantörens anvisningar."),
  ],
  "sources": [
    ("Nacka kommun – Kulturmiljöprogram: Sommarnöjen vid farleden (pdf)",
     "https://www.nacka.se/499628/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-sommarnojen.pdf"),
    ("Nacka kommun – Ändring av bärande konstruktioner",
     "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/jag-vill-gora-ansokan-eller-anmalan/andring-barande-konstruktioner/"),
    _BKR, _GBR_U, _SKV, _SKV2,
  ],
  "cta": ("Ska golven i huset i Nacka göras om?", "Boka ett gratis platsbesök så går vi igenom bjälklag, nivåer och fukt på plats."),
  "img": [
    ("Ljust målat brädgolv i en äldre sommarvilla med glasveranda och sjöutsikt i Nacka",
     "interior of an old Swedish summer villa from the late 1800s near the water in Nacka, wide light grey painted wooden floorboards, open double doors to a glazed veranda with small window panes, view of pine trees and sea inlet, empty room, summer daylight, no people, no text"),
    ("Nylagt klinkergolv i mellanstort format i ett källarplan med fönster mot trädgården",
     "newly laid medium size grey ceramic floor tiles in a renovated basement room of a Swedish villa built on a slope, small window at ground level showing garden, white walls, empty room, natural light, no people, no hands, no text"),
  ],
  "related": [
    ("snickare-nacka.html", "Snickare i Nacka", "Verandor, panel och altaner."),
    ("malare-nacka.html", "Målare i Nacka", "Sekelskiftesvillor och sommarnöjen."),
  ],
},

# ------------------------------------------------------------------ SOLNA
"golvlaggare-solna.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Solna", "svc_label": "Golvläggare",
  "title": "Golvläggare i Solna – parkett och trägolv i bostadsrätt",
  "description": "Golvläggare i Solna: nytt golv och slipning i bostadsrätt, föreningens regler, äldre lägenheter i Råsunda och plastmatta mot trä. Gratis platsbesök.",
  "h1": "Golvläggare i Solna",
  "lead": "I Solna ligger de flesta golvjobb i en lägenhet, och oftast i en bostadsrätt. Det gör föreningen till en del av planeringen redan innan materialet väljs. Geal Entreprenad AB lägger parkett, trägolv och klinker och slipar gamla golv i hela Solna, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Bostadsrätter i Råsunda, Hagalund och Huvudsta.",
  "sections": [
    {"id": "bostadsratt-solna", "anchor": "Golv i bostadsrätt",
     "h2": "Sju av tio lägenheter i Solnas flerbostadshus är bostadsrätter",
     "paras": [
       "Enligt SCB:s statistik över bostadsbeståndet den 31 december 2024 är 70 procent av lägenheterna i Solnas flerbostadshus bostadsrätter och 29 procent hyresrätter. Solna är därmed en av de tio kommuner i landet med störst andel bostadsrätter. I riket som helhet är andelen 42 procent.",
       "För dig som ska byta golv betyder det två saker. Du ansvarar själv för golvet, eftersom bostadsrättslagen säger att lägenheten ska hållas i gott skick på bostadsrättshavarens bekostnad, om stadgarna inte anger något annat. Och arbetet sker i ett hus där grannarna bor vägg i vägg, över och under, så tider, bärhjälp i trapphuset och skydd av gemensamma ytor behöver planeras.",
     ],
     "aside": {"title": "Före golvbytet i lägenheten", "items": [
       "Läs stadgarna om underhållsansvar", "Fråga om krav på underlag",
       "Boka hiss och skydda trapphuset", "Meddela grannarna om slipdagarna"]}},
    {"id": "foreningen-solna", "h2": "Vad styrelsen ska godkänna",
     "paras": [
       "Bostadsrättslagens 7 kap. 7 § räknar upp åtgärder som kräver styrelsens tillstånd: ingrepp i bärande konstruktion, installation eller ändring av ledningar för avlopp, värme, gas eller vatten, ändring av ventilation, påverkan på brandskyddet och andra väsentliga förändringar av lägenheten. Att byta ett ytskikt hör normalt inte dit. Vattenburen golvvärme som kopplas till husets system gör det.",
       "Solna stad skriver i sin guide för lägenhetsinnehavare att den som bor i en bostadsrättsförening behöver fastighetsägarens medgivande för byggåtgärder, och att en vägg som rivs kräver föreningens godkännande och, om den är bärande, en anmälan till staden. Ska golvbytet göras samtidigt som en vägg tas bort hänger alltså frågorna ihop.",
       "Vår rekommendation är att ta kontakt med styrelsen tidigt och beskriva vad som ska göras, även när golvbytet inte kräver tillstånd. Många föreningar vill veta när det blir buller och hur trapphuset skyddas, och en kort beskrivning av jobbet brukar räcka. Kostnadsförslaget fungerar ofta som en sådan beskrivning.",
     ],
     "aside": None},
    {"id": "rasunda-golv", "h2": "Äldre lägenheter i Råsunda",
     "paras": [
       "Stadsmuseets texter om Råsunda berättar att Stockholms Nya Spårvägs AB köpte marken 1907 och att förorten, till skillnad från andra förorter, bebyggdes med flerbostadshus för medelklassfamiljer. Reklamen från 1909 lovade att man där kunde förena stadens bekvämligheter med lantlivets behag. Längs Råsundavägen växte jugendhusen upp mellan 1910 och 1912, och villaområdena tillkom på 1920-talet.",
       "I en lägenhet från den tiden kan det finnas äldre trägolv eller parkett som går att slipa i stället för att bytas. Lagen innehåller dessutom en särskild regel: har lägenheten ett särskilt kulturhistoriskt eller konstnärligt värde krävs styrelsens tillstånd för en åtgärd som påverkar det värdet. Fråga därför föreningen innan ett originalgolv rivs. Mer om slipning och ytbehandling finns under " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": {"title": "Originalgolv i äldre hus", "items": [
       "Slipa hellre än riv", "Byt enstaka stavar vid skador",
       "Välj yta efter rummets slitage", "Fråga föreningen om kulturvärde"]}},
    {"id": "plastmatta-solna", "h2": "Från plastmatta till trägolv i Hagalund",
     "paras": [
       "Hagalunds gamla trähusbebyggelse revs från 1965 och ersattes av Blåkulla, som stod inflyttningsklart 1973. I lägenheter från den här tiden ligger ofta plastmatta eller ett enkelt golv som har bytts någon gång. Skatteverket räknar att byta plastmatta mot trägolv som ett förbättringsarbete, och det ger rotavdrag även i en bostadsrätt.",
       "Under en gammal matta kan det finnas limrester och ojämnheter som behöver slipas bort eller spacklas innan ett nytt golv läggs. Är underlaget betong följer vi materialleverantörens anvisningar för fuktspärr och lim. Ska köket göras om samtidigt finns mer under " + _L.format("koksrenovering-solna.html", "köksrenovering i Solna") + ".",
     ],
     "aside": None},
    {"id": "slipning-solna", "h2": "Slipa golvet i en lägenhet",
     "paras": [
       "En golvslipning i ett flerbostadshus planeras lite annorlunda än i en villa. Maskinerna låter, dammet ska stanna i lägenheten och material och utrustning ska bäras genom ett gemensamt trapphus. Vi stänger av rummen, använder maskiner med dammsugning och lägger de mest bullriga momenten på tider som föreningens ordningsregler tillåter.",
       "Efter slipningen behöver ytan tid att torka eller härda innan möblerna ställs tillbaka. Hur lång tid beror på om du väljer lack eller olja, och det skriver vi in i tidsplanen så att du vet när lägenheten går att använda igen.",
       "Ska flera rum få nytt golv samtidigt planerar vi i vilken ordning de görs, så att du kan bo kvar under arbetet om du vill. Kök och badrum tas om möjligt sist eller först i ett eget skede, eftersom de är svårast att vara utan. Bärhjälp, skydd och avfall räknas in redan i kostnadsförslaget, så att inget kommer som en överraskning för dig eller föreningen.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi golv i en lägenhet i Solna",
  "steps": [
    ("Besök i lägenheten", "Vi mäter rummen, kontrollerar underlaget och ser hur material kan bäras in."),
    ("Stadgar och tillstånd", "Vi går igenom vad föreningen behöver godkänna och vad som räcker att meddela."),
    ("Kostnadsförslag i skrift", "Arbete, material och skydd av gemensamma ytor redovisas var för sig."),
    ("Skydd och rivning", "Trapphus och hiss skyddas, gammalt golv tas bort och underlaget görs plant."),
    ("Läggning eller slipning", "Det nya golvet läggs eller det gamla slipas, och lister monteras."),
    ("Överlämning", "Vi går igenom golvet med dig och städar efter oss i trapphuset."),
  ],
  "rot_h2": "ROT-avdrag i bostadsrätt i Solna",
  "rot": [
    "I en bostadsrätt ger Skatteverket rotavdrag för arbete inne i bostaden, och dit räknas att slipa och byta golv, sätta klinker och att byta plastmatta mot trägolv. Arbete på fasad eller balkong ger inte avdrag för dig som bostadsrättshavare.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Geal drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i en lägenhet?",
  "price": [
    "Kostnaden styrs av hur många rum och trösklar golvet ska passa mot, hur mycket gammalt golv som ska bort, underlagets skick och om föreningen har krav på ljuddämpning eller viss underlagsduk. Våning, hiss och avstånd till parkering påverkar också tiden. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem ansvarar för parkettgolvet i vår bostadsrätt i Solna?",
     "Bostadsrättslagen lägger underhållet av lägenheten på bostadsrättshavaren om stadgarna inte säger annat. Golvet är därför normalt ditt ansvar."),
    ("Får jag riva originalgolvet i en jugendlägenhet i Råsunda?",
     "Har lägenheten särskilt kulturhistoriskt värde kräver bostadsrättslagen styrelsens tillstånd för åtgärder som påverkar värdet. Fråga föreningen först, och överväg en slipning."),
    ("Ger det rotavdrag att byta plastmattan mot trägolv i en lägenhet i Hagalund?",
     "Ja. Skatteverket räknar bytet som ett förbättringsarbete i bostadsrätt. Avdraget gäller arbetskostnaden, inte materialet."),
    ("Kan vi lägga golvvärme under det nya golvet i bostadsrätten?",
     "Elburen golvvärme är en annan fråga än vattenburen. Ska golvvärme kopplas till husets värmeledningar kräver det styrelsens tillstånd enligt bostadsrättslagen."),
    ("Hur störande är en golvslipning för grannarna i ett flerbostadshus?",
     "Slipmaskinerna låter, så vi lägger slipningen på tider som föreningen tillåter och ser till att grannarna vet om det i förväg."),
  ],
  "sources": [
    ("SCB – Bostadsbeståndet 31 december 2024",
     "https://www.scb.se/hitta-statistik/statistik-efter-amne/boende-bebyggelse-och-mark/bostader-och-boende/bostadsbestand/pong/statistiknyhet/bostadsbestandet-31-december-2024/"),
    ("Solna stad – Guide till lov och anmälan för lägenhetsinnehavare",
     "https://www.solna.se/bygga-bo--miljo/bygga/guide-till-lov-och-anmalan/for-lagenhetsinnehavare"),
    ("Stockholmskällan / Stadsmuseet – Solna centrum (Stockholms spår)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000048.pdf"),
    ("Stockholmskällan / Stadsmuseet – Näckrosen (Stockholms spår)",
     "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000066.pdf"),
    _BRL, _SKV, _SKV2,
  ],
  "cta": ("Nytt golv i lägenheten i Solna?", "Boka ett gratis platsbesök så går vi igenom underlag, föreningens regler och material."),
  "img": [
    ("Nylagd ljus ekparkett i fiskbensmönster i en äldre lägenhet i Råsunda",
     "freshly laid light oak herringbone parquet floor in an empty living room of a 1910s Swedish jugend apartment in Solna, tall white windows, white walls with decorative ceiling cornice, tiled stove in the corner, soft daylight, no people, no text"),
    ("Rum där gammal plastmatta har rivits och betongen är spacklad inför nytt golv",
     "empty room in a 1970s Swedish apartment where an old vinyl floor has been removed, smooth grey patched concrete subfloor ready for new flooring, a roll of underlay and stacked oak floor packages by the wall, natural light, no people, no hands, no text"),
  ],
  "related": [
    ("badrumsrenovering-solna.html", "Badrumsrenovering i Solna", "Bostadsrätt, stambyte och villa."),
    ("malare-solna.html", "Målare i Solna", "Väggar och tak innan golvet läggs."),
  ],
},

# ------------------------------------------------------------------ TÄBY
"golvlaggare-taby.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Täby", "svc_label": "Golvläggare",
  "title": "Golvläggare i Täby – klinker, golvvärme och trägolv",
  "description": "Golvläggare i Täby: golv i villor och radhus från 1970- och 80-talen, klinker med golvvärme, stora plattor och trägolv på betong. Gratis platsbesök.",
  "h1": "Golvläggare i Täby",
  "lead": "Täby är till största delen byggt efter 1970, och många hus har nu sina andra eller tredje golv. Ofta är det hallen och köket som står på tur, gärna med klinker och golvvärme. Geal Entreprenad AB lägger klinker, parkett och trägolv och slipar befintliga golv i hela Täby, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villor, radhus och kedjehus från 1970- och 80-talen.",
  "sections": [
    {"id": "taby-hus", "anchor": "Husen i Täby",
     "h2": "De flesta husen i Täby är byggda efter 1970",
     "paras": [
       "Kommunens riktlinjer Kulturmiljöer i Täby visar åldersfördelningen i byggnadsbeståndet: av de daterade byggnaderna har merparten tillkommit efter 1970, och bebyggelsen från före 1920 utgör bara några få procent. Riktlinjerna jämför med landet som helhet, där 13 procent av bostadsbeståndet är byggt till och med 1920 och 67 procent efter 1960. Under 1970-talet byggdes många radhus och grupphusområden i Täby kyrkby och Byle.",
       "I Skarpäng och Gribbylund bestod områdena så sent som i början av 1970-talet av en blandning av fritidshus och permanentvillor. Därefter växte täta villaområden fram, främst med hus från 1970- och 1980-talen på mindre tomter, ofta i dubbla rader med skafttomter. Kring Gribbylund, Löttingelund och Hästängen är villorna till största delen typhus, och här finns också flera områden med radhus och kedjehus.",
       "Ett typhus från den tiden har ofta fått nya golv i omgångar. Det är vanligt att hitta olika material i olika rum och flera lager på varandra, och det påverkar både höjder vid trösklar och vad som måste rivas.",
     ],
     "aside": {"title": "Vanligt i hus från 70- och 80-talen", "items": [
       "Flera golvlager på varandra", "Olika höjd mellan rummen",
       "Slitna klinkergolv i hallen", "Parkett med tunt slitskikt"]}},
    {"id": "golvvarme-taby", "h2": "Klinker med golvvärme i hall och kök",
     "paras": [
       "En hall där familjen kommer in med snö och grus är ett klassiskt ställe för klinker, och många vill ha golvvärme under. Byggkeramikrådet anger att golvvärmen ska startas försiktigt efter plattsättningen och att temperaturen inte ska höjas med mer än 3 °C per dygn. Slingornas läge ska dessutom dokumenteras, vilket underlättar om till exempel en toalett senare ska monteras.",
       "Där ett tätskikt behövs ska golvvärmesystemet ligga under det. Avjämningsmassan över slingorna läggs i den tjocklek som leverantören anger. Ska golvvärmen ingå i ett nytt badrum blir det en del av en " + _L.format("badrumsrenovering-taby.html", "badrumsrenovering i Täby") + ".",
     ],
     "aside": None},
    {"id": "stora-plattor", "h2": "Stora plattor kräver ett plant underlag",
     "paras": [
       "Plattor i stora format blir allt vanligare även i villor. Ju större platta, desto mer syns ett ojämnt underlag. Byggkeramikrådet anger tillåtna fogsprång – hur mycket en platta får sticka upp över grannen – till 0,7 mm för plattor med en största sida på 10 cm och 2,0 mm för plattor på 60 × 60 cm.",
       "Därför rivs gammalt golv ned till ett stabilt underlag, och svackor jämnas ut innan plattsättningen börjar. Ligger det gamla klinkergolvet fast och plant kan det ibland vara kvar under det nya, men det avgör vi först när vi har kontrollerat det.",
     ],
     "aside": {"title": "Före plattsättning", "items": [
       "Riv ned till stabilt underlag", "Mät planheten med rätskiva",
       "Jämna ut svackor", "Planera fogarna efter rummet"]}},
    {"id": "betong-taby", "h2": "Trägolv på betong",
     "paras": [
       "Ska ett vardagsrum i ett hus på betong få trägolv eller parkett behöver betongen vara tillräckligt torr. Golvbranschen varnar för att fukt som stängs inne mellan betong och golvmaterial kan bryta ned lim och golv, och att det kan ge emissioner som i värsta fall orsakar huvudvärk, yrsel eller astmaliknande besvär.",
       "En mätning av en fuktkontrollant inom RBK visar om golvet kan läggas direkt eller om det behövs annan fuktspärr eller väntetid. Vi samordnar mätningen och följer leverantörens anvisningar för lim. Läs mer om golvtyper under " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "parkett-taby", "h2": "Parkett från 80-talet: slipa eller byta",
     "paras": [
       "Många hus i Täby har fått parkett vid ett tidigare golvbyte. Är det en flerskiktsparkett med tunt toppskikt kan det vara svårt att slipa den mer än lätt, och har den redan slipats en gång finns kanske inte mycket kvar. Massiv parkett eller stavparkett har mer trä att ta av.",
       "Vi tar reda på vilken typ det är genom att lyfta en tröskel eller list. Går golvet att slipa är det ofta det enklaste sättet att få ett fräscht golv utan rivning. Går det inte lägger vi ett nytt golv, flytande eller limmat beroende på underlaget.",
       "I ett kedjehus eller radhus där flera rum ligger i rad kan ett nytt golv läggas genom hela planet utan trösklar, om det tillåts av golvtypen. Ett flytande golv behöver då rörelseutrymme mot väggar och ibland en fog i dörröppningar. Det planerar vi utifrån leverantörens anvisningar.",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgång för golv i Täby",
  "steps": [
    ("Platsbesök", "Vi tittar på golvlagren, mäter höjder vid trösklar och kontrollerar planheten."),
    ("Val av material", "Vi går igenom klinker, parkett eller trägolv utifrån rummets slitage och om golvvärme ska ingå."),
    ("Skriftligt kostnadsförslag", "Rivning, avjämning, eventuell fuktmätning och läggning anges som separata poster."),
    ("Rivning och avjämning", "Gamla lager tas bort, underlaget görs plant och golvvärmen läggs ut."),
    ("Plattsättning eller läggning", "Plattor sätts eller golvet läggs, och fogar, lister och trösklar görs klart."),
    ("Igångsättning", "Vi går igenom hur golvvärmen ska startas och hur golvet sköts."),
  ],
  "rot_h2": "Rotavdrag för golv och klinker i Täby",
  "rot": [
    "Att byta golv räknas som rotarbete i småhus. Byter du en plastmatta mot trägolv räknar Skatteverket det som ett förbättringsarbete, som också ger avdrag. Avdraget gäller arbetet, inte plattor, parkett, lim eller resor.",
    "Du får dra av 30 procent av arbetskostnaden, högst 50 000 kr per person och år. Rot och rut får tillsammans uppgå till högst 75 000 kr. Avdraget görs direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden",
  "price": [
    "Antalet golvlager som ska rivas och hur mycket underlaget behöver jämnas ut väger tungt, särskilt inför stora plattor. Golvvärme, plattformat, mönster och antalet trösklar påverkar också. Vi gör ett gratis platsbesök och lämnar ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vi har tre lager golv i hallen i vårt hus i Gribbylund – måste allt rivas?",
     "Inte nödvändigtvis, men ju fler lager desto större risk för höjdproblem vid dörrar och ett underlag som rör sig. Vi kontrollerar lagren vid besöket och föreslår vad som ska bort."),
    ("Hur snabbt får vi värma upp det nya klinkergolvet i Täby?",
     "Byggkeramikrådet anger att golvvärmen ska höjas långsamt, med högst 3 °C per dygn, och först när plattsättningen har fått stå den tid rådet anger."),
    ("Passar plattor på 60 × 60 cm i ett radhus från 1970-talet i Täby kyrkby?",
     "Ja, om underlaget blir tillräckligt plant. Stora plattor kräver bättre planhet än små, så vi kontrollerar golvet innan vi rekommenderar formatet."),
    ("Varför behöver betongen mätas innan ekparketten läggs?",
     "Fukt som stängs in under golvet kan bryta ned lim och golv och ge emissioner. En mätning visar om golvet kan läggas eller om något behöver göras först."),
    ("Kan ni byta golv i ett kedjehus i Löttingelund medan vi bor kvar?",
     "Oftast ja, rum för rum. Vi planerar ordningen så att ni har tillgång till kök och badrum så mycket som möjligt."),
  ],
  "sources": [
    ("Täby kommun – Kulturmiljöer i Täby, riktlinjer (pdf)",
     "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"),
    _BKR, _GBR_L, _GBR_U, _SKV, _SKV2,
  ],
  "cta": ("Nytt golv i huset i Täby?", "Boka ett gratis platsbesök så tittar vi på golvlager, planhet och golvvärme."),
  "img": [
    ("Hall med nylagt grått klinkergolv i stort format i en villa från 1970-talet i Täby",
     "entrance hall of a renovated 1970s Swedish suburban villa in Taby, newly laid large format light grey ceramic floor tiles with narrow joints, white walls, wooden front door with side window, simple bench, daylight, no people, no text"),
    ("Golvvärmeslingor utlagda på ett rengjort betonggolv inför plattsättning",
     "close-up of white underfloor heating pipes laid in neat loops on a clean concrete floor in an empty Swedish villa hallway before tiling, bucket of levelling compound in the corner, natural light, no people, no hands, no text"),
  ],
  "related": [
    ("koksrenovering-taby.html", "Köksrenovering i Täby", "Grupphus, radhus och villor."),
    ("snickare-taby.html", "Snickare i Täby", "Trösklar, lister och dörrar."),
  ],
},

# ------------------------------------------------------------------ LIDINGÖ
"golvlaggare-lidingo.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Lidingö", "svc_label": "Golvläggare",
  "title": "Golvläggare på Lidingö – souterräng, radhus och trägolv",
  "description": "Golvläggare på Lidingö: golv i 1960-talets souterrängvillor, nedre plan mot berg och mark och radhus från 1940-talets slut. Gratis platsbesök.",
  "h1": "Golvläggare på Lidingö",
  "lead": "Lidingö är kuperat, och många hus har ett nedre plan som delvis ligger i berget eller mot marken. Där ställs andra krav på golvet än i resten av huset. Geal Entreprenad AB lägger parkett, trägolv och klinker och slipar befintliga golv på hela ön, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Souterrängvillor, radhus och äldre villor på Lidingö.",
  "sections": [
    {"id": "tjadervagen", "anchor": "Souterrängvillorna",
     "h2": "Sextiotalsvillor i sluttning vid Tjädervägen",
     "paras": [
       "Lidingö stads kulturmiljöprogram beskriver Tjädervägen i sydvästra Mosstorp som ett exempel på ett mer burget och exklusivt villabyggande från 1960-talet. Området projekterades i början av 1960-talet, och de omkring 20 villorna byggdes mellan 1961 och 1968. De flesta är arkitektritade, och flera är souterrängvillor som har anpassats till nivåskillnaderna på bergskrönet och i sluttningarna.",
       "Programmet lyfter fram äkta material som ett kännetecken för området, bland annat ädelträ, ibland teak, i fönsterpartier och kopparplåt på takfoten. Villorna beskrivs som exteriört ovanligt intakta. I ett hus med så påkostade material passar ett golv som går att slipa om, som massivt trä eller parkett med tjockt slitskikt.",
     ],
     "aside": {"title": "I en souterrängvilla", "items": [
       "Övre plan på träbjälklag eller betong?", "Nedre plan mot berg eller mark?",
       "Trappa och nivåer mellan planen", "Rum med eller utan golvvärme"]}},
    {"id": "nedre-plan", "h2": "Golvet i nedre planet",
     "paras": [
       "Det plan som ligger mot berget eller marken är det känsliga. Byggkeramikrådet skriver att man i källare med markfukt bör undvika alltför stora plattor och alltför smala fogar, och rekommenderar högst 900 cm² per platta. Tätskiktet kan där begränsas till de ytor som verkligen blir blöta, som duschgolvet.",
       "Ska nedre planet få trägolv eller parkett börjar vi med att ta reda på hur fuktigt underlaget är. Golvbranschen påpekar att trä tar upp fukt ur omgivningen och sväller när den relativa fuktigheten är hög, och rekommenderar att bjälklagets fukt kontrolleras av en fuktkontrollant inom RBK. Ska nedre planet också få nytt badrum gör vi det inom " + _L.format("badrumsrenovering-lidingo.html", "badrumsrenovering på Lidingö") + ".",
     ],
     "aside": None},
    {"id": "hersby-garde", "h2": "Radhusen i Hersby Gärde",
     "paras": [
       "En helt annan miljö är Hersby Gärde, där arkitekterna Ancker, Gate & Lindegren ritade radhusen vid Kämpavägen och Laduvägen 1948. Området byggdes 1948–1950 på mark som hört till Hersby gård, och programmet beskriver husen som välbevarade och utförda med goda material och hantverksmässig omsorg. Radhusen har två våningar, några med källare och några i souterräng. Bebyggelsen finns inventerad i Riksantikvarieämbetets bebyggelseregister, och programmet påpekar att radhusbyggandet har tradition på Lidingö.",
       "I ett radhus från den tiden är det vanligt att golven har bytts eller täckts över i omgångar. Vi lyfter en list och tittar på vad som ligger under, och om det finns äldre trägolv som går att slipa föreslår vi det före ett nytt golv. Källaren behandlar vi som nedre planet i en souterrängvilla: fukten mäts först.",
       "Programmet beskriver Hersby Gärde som ett grönt och luftigt område med stora trädgårdar mellan längorna. Med så mycket trädgård runt husen får golvet närmast entrén ta emot mer jord och grus än man kanske räknar med, och där väljer vi en yta som är lätt att hålla ren.",
     ],
     "aside": {"title": "Radhus med två plan och källare", "items": [
       "Se vad som döljs under ytskiktet", "Slipa äldre trägolv där det går",
       "Mät fukten i källaren", "Anpassa trösklar mot trappan"]}},
    {"id": "lidingo-val", "h2": "Parkett eller massivt trä",
     "paras": [
       "Flerskiktsparkett läggs ofta flytande och är snabb att få på plats, vilket passar när ett helt plan ska göras om utan att huset står tomt länge. Massivt trä spikas eller limmas och tål fler slipningar under sin livstid. I ett hus med påkostade material i övrigt är det ofta det senare man väljer. Vi visar alternativen vid besöket – mer om ytbehandlingar finns under " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "trappor-lidingo", "h2": "Trappor och nivåer mellan planen",
     "paras": [
       "I ett hus i flera plan möts golven vid trappan. Ett nytt golv som är tjockare än det gamla ändrar höjden på det översta och nedersta trappsteget, och då kan stegen bli olika höga. Därför mäter vi höjderna innan golvtyp väljs och planerar hur övergången mot trappan ska se ut, med en trappnos eller list som passar golvet.",
       "Samma sak gäller dörrar och trösklar. Ett tjockare golv kan kräva att dörrbladen kortas, och det är bättre att veta före beställningen än att upptäcka det när golvet ligger.",
       "Har nedre planet en egen dörr direkt ut till trädgården kommer det in väta och grus just där. Där kan ett tåligare golv eller en klinkeryta innanför dörren vara klokt, även om resten av planet får trä.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med golv på Lidingö",
  "steps": [
    ("Besök i huset", "Vi går igenom planen ett i taget och noterar vilka rum som ligger mot mark eller berg."),
    ("Fukt och underlag", "I nedre planet bokas en fuktmätning, i övriga rum kontrolleras bjälklag och planhet."),
    ("Förslag i skrift", "Material, förarbeten och läggning redovisas plan för plan."),
    ("Förberedelse", "Gammalt golv tas bort och underlaget rätas upp eller jämnas ut."),
    ("Läggning", "Golvet läggs eller slipas, och trösklar och lister mot trappor och dörrar anpassas."),
    ("Slutkontroll", "Vi går igenom golvet med dig och lämnar skötselråd för vald yta."),
  ],
  "rot_h2": "Rotavdrag för golvläggning på Lidingö",
  "rot": [
    "Slipning och byte av golv i villa eller radhus räknas som rotarbete hos Skatteverket, och det gör även plattsättning. Avdraget är 30 procent av arbetskostnaden och gäller inte material eller resor.",
    "Varje person kan få högst 50 000 kr i rotavdrag per år, och rot och rut får tillsammans bli högst 75 000 kr. Är ni två som äger och bor i huset kan ni dela avdraget. Vi drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden?",
  "price": [
    "I ett hus i flera plan påverkar antalet nivåer, trappor och trösklar mer än ytan i sig. I nedre planet tillkommer fuktmätning och ibland avjämning eller fuktspärr, och valet mellan massivt trä och flerskiktsparkett spelar in. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilket golv passar i nedre planet i en souterrängvilla på Lidingö?",
     "Det beror på hur fuktigt underlaget är. Klinker i måttligt format klarar markfukt bäst, men trä eller parkett kan fungera om mätningen visar att betongen är torr nog."),
    ("Kan golven i vårt radhus i Hersby Gärde slipas i stället för att bytas?",
     "Om det finns äldre trägolv under senare ytskikt och det är helt nog, ja. Vi tittar under en list vid besöket och föreslår slipning där det går."),
    ("Varför avråder Byggkeramikrådet från stora plattor i källaren?",
     "I källare med markfukt rekommenderar rådet högst 900 cm² per platta och inte alltför smala fogar. Vi väljer format efter det."),
    ("Kan ni lägga samma golv i båda planen i vår villa vid Tjädervägen?",
     "Ofta går det i utseende, men konstruktionen kan behöva skilja sig mellan ett plan på bjälklag och ett mot mark. Vi förklarar skillnaden vid besöket."),
    ("Hur lång tid tar det att byta golv i ett helt plan?",
     "Det beror på yta, förarbete och golvtyp. Du får en tidsplan tillsammans med kostnadsförslaget efter platsbesöket."),
  ],
  "sources": [
    ("Lidingö stad – Kulturmiljöprogram del 2: Tjädervägen (pdf)", "https://share.mediaflow.com/sv/?K8CCG1AETN"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Hersby Gärde (pdf)", "https://share.mediaflow.com/sv/?7FCCM1UEIL"),
    ("Lidingö stad – Kulturmiljöprogram", "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/"),
    _BKR, _GBR_U, _SKV, _SKV2,
  ],
  "cta": ("Ska golven i huset på Lidingö bytas?", "Boka ett gratis platsbesök så går vi igenom planen, fukten och materialvalet."),
  "img": [
    ("Vardagsrum med mörkt massivt trägolv och stora fönster i en villa från 1960-talet på Lidingö",
     "spacious living room of an architect designed 1960s Swedish modernist villa on a rocky hillside on Lidingo, wide solid dark oak floorboards, large floor to ceiling teak framed windows overlooking pine trees, minimal furniture, daylight, no people, no text"),
    ("Nedre plan i en souterrängvilla med nylagt klinkergolv i måttligt format",
     "lower ground floor room of a Swedish split-level villa built against bedrock, newly laid medium format beige ceramic floor tiles, white painted walls, a short staircase with wooden treads leading up, small high window, natural light, no people, no hands, no text"),
  ],
  "related": [
    ("koksrenovering-lidingo.html", "Köksrenovering på Lidingö", "Villastäder, souterräng och lov."),
    ("malare-lidingo.html", "Målare på Lidingö", "Väggar och snickerier inne och ute."),
  ],
},

# ------------------------------------------------------------------ HUDDINGE
"golvlaggare-huddinge.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Huddinge", "svc_label": "Golvläggare",
  "title": "Golvläggare i Huddinge – grupphus, radhus och plastmatta",
  "description": "Golvläggare i Huddinge: nya golv i grupphus och radhus från 1960–80-talen, plastmatta som byts mot trägolv och ROT på arbetet. Gratis platsbesök.",
  "h1": "Golvläggare i Huddinge",
  "lead": "Huddinges villaområden domineras av hus från 1960-, 70- och 80-talen, ofta byggda i grupp av samma byggbolag. Golven i dem har nu tjänat länge, och plastmattan i hall och kök är en vanlig kandidat för byte. Geal Entreprenad AB lägger nya golv och slipar befintliga i hela Huddinge, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Grupphus, radhus och kedjehus i Huddinge.",
  "sections": [
    {"id": "grupphus-huddinge", "anchor": "Grupphus och radhus",
     "h2": "Byggt i fabrik, monterat på plats",
     "paras": [
       "Huddinge kommuns kulturmiljöprogram beskriver hur villor under 1960-talet i större omfattning började byggas som grupphusområden, helt uppförda av byggbolag. Konceptet med ett nyckelfärdigt hus hade skapats, och husen byggdes oftast prefabricerat med färdiga byggelement som monterades ihop på plats. Under miljonprogrammets år, 1965–1975, uppfördes i landet som helhet en tredjedel av de nya bostäderna i småhus och grupphus, men i Huddinge blev andelen flerbostadshus större.",
       "Programmet visar också hur bostadsbeståndet förändrades. Fram till 1960-talet var omkring 70 procent av Huddinges bostäder småhus, men mellan 1960 och 1975 sjönk andelen till 33 procent när många flerfamiljshus byggdes. På 1970-talet anpassades villorna enligt programmet för en växande medelklass, med större hus av högre standard än egnahemsrörelsens enkla småhus.",
       "Att husen i ett område är byggda lika gör det lättare att förutse vad som ligger under golvet. Ändå kontrollerar vi varje hus för sig, eftersom ägare genom åren har byggt om på olika sätt.",
     ],
     "aside": {"title": "Typiskt i grupphus från 60–80-talen", "items": [
       "Plastmatta i hall, kök och tvättstuga", "Parkett eller laminat i vardagsrummet",
       "Flera golvlager efter tidigare byten", "Samma planlösning som grannhusen"]}},
    {"id": "plastmatta-huddinge", "h2": "Plastmatta ut, trägolv in",
     "paras": [
       "Skatteverket nämner uttryckligen att byta plastmatta mot trägolv som ett exempel på förbättringsarbete i småhus, och det ger rotavdrag på arbetet. Under den gamla mattan finns ofta lim och spackel som måste bort eller jämnas ut, så att det nya golvet får ett plant och fast underlag.",
       "Ligger mattan på betong vill vi veta hur torr betongen är innan trä läggs. Golvbranschen varnar för att fukt som stängs in mellan betong och golvmaterial kan bryta ned lim och golv och ge emissioner till inomhusluften. Ligger den på träreglar och skivor kontrollerar vi i stället att skivorna sitter fast och inte sviktar.",
     ],
     "aside": None},
    {"id": "radhus-huddinge", "h2": "Radhusen från 1970-talets slut",
     "paras": [
       "Som en motreaktion mot de storskaliga flerbostadshusen byggdes radhus runt om i Huddinge under slutet av 1970-talet och början av 1980-talet. Kulturmiljöprogrammet nämner Sörskogen söder om Huddinge centrum och Utsälje vid Snättringe som exempel. Även Östra Skogås fick terränganpassade småhus, trots att området först var tänkt för flerbostadshus.",
       "I ett radhus på två plan är det ofta smidigast att ta ett plan i taget, så att familjen kan bo kvar. Övergångarna mot trappan och mellan rum med olika golvmaterial planeras innan arbetet börjar. Ska väggarna målas samma gång gör man det före golvet – se " + _L.format("malare-huddinge.html", "målare i Huddinge") + ".",
     ],
     "aside": {"title": "Ett plan i taget", "items": [
       "Övervåningen först eller sist", "Trappnosar och övergångar",
       "Tillgång till kök och badrum", "Skydd av golvet efteråt"]}},
    {"id": "nyare-huddinge", "h2": "Gäller ROT även i ett nyare hus?",
     "paras": [
       "Reparation och underhåll ger rotavdrag oavsett husets ålder. För ombyggnad och förbättring gäller däremot att avdrag inte medges under de första fem åren efter husets värdeår. Skatteverket anger också att material som byts i ett småhus som är yngre än fem år ska ersättas med likvärdigt. Är huset nybyggt kan ett golvbyte alltså hamna utanför avdraget, och det är bra att veta innan offerten jämförs. Mer om golvtyper finns under " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "laminat-huddinge", "h2": "Laminat och tunn parkett från tidigare byten",
     "paras": [
       "Många grupphus har redan bytt golv minst en gång, och då ligger det ofta laminat eller en tunn parkett i vardagsrummet. Laminat går inte att slipa, och en parkett med tunt slitskikt tål sällan mer än en lätt slipning. Är ytan sliten är ett nytt golv därför ofta det rimliga.",
       "Ett flytande golv som ligger på en underlagsduk kan i regel tas bort utan att underlaget skadas. Ligger det nya golvet på samma nivå som det gamla behöver trösklar och dörrar inte ändras. Vi kontrollerar planheten och om underlaget sviktar innan något beställs.",
       "Vill du ha ett golv som kan slipas om i framtiden är massivt trä eller en parkett med tjockt slitskikt ett alternativ till nytt laminat. Materialvalet påverkar både kostnaden och hur många gånger golvet kan fräschas upp, och det är en avvägning vi gärna går igenom vid besöket.",
     ],
     "aside": None},
  ],
  "steps_h2": "Golvbytet steg för steg",
  "steps": [
    ("Hembesök", "Vi tittar på golven, lyfter en list och ser vad som ligger under plastmatta eller laminat."),
    ("Förslag på material", "Vi föreslår golv efter hur rummen används, och om något lager kan ligga kvar."),
    ("Kostnadsförslag", "Du får arbete, material och rivning redovisat var för sig, så att ROT-delen syns."),
    ("Rivning och underlag", "Mattor, lim och gamla lister tas bort och underlaget görs plant och fast."),
    ("Nytt golv", "Golvet läggs, och trösklar, trappnosar och lister monteras."),
    ("Genomgång och städning", "Vi går igenom resultatet och tar med oss spillet."),
  ],
  "rot_h2": "Rotavdrag för nytt golv i Huddinge",
  "rot": [
    "Att slipa och byta golv i ett småhus räknas som rotarbete, och bytet från plastmatta till trägolv räknas som förbättring. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Material, utrustning och resor ingår inte. Betalningen ska göras elektroniskt, till exempel med kort, Swish eller banköverföring, och Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad avgör kostnaden?",
  "price": [
    "Hur många lager som ska rivas, hur mycket lim och spackel som måste bort och om underlaget behöver jämnas ut påverkar mest. Därefter kommer golvmaterial, antalet rum och övergångar, och om trappan ska få nya nosar. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Ger det rotavdrag att byta plastmattan mot ekgolv i vårt radhus i Sörskogen?",
     "Ja. Skatteverket räknar bytet från plastmatta till trägolv som ett förbättringsarbete i småhus. Avdraget gäller arbetskostnaden."),
    ("Vad finns under golven i ett grupphus från 1970-talet i Huddinge?",
     "Det varierar efter hur huset har byggts om. Vi lyfter en list eller tröskel vid besöket och ser vilka lager som finns innan vi föreslår något."),
    ("Vårt hus i Huddinge är bara tre år gammalt – får vi ROT för nytt golv?",
     "Reparation och underhåll ger avdrag, men ombyggnad och förbättring ger inte avdrag de första fem åren efter värdeåret. Byts material ska det nya vara likvärdigt med det gamla."),
    ("Kan ni lägga nytt golv på ett plan i taget i vårt radhus i Utsälje?",
     "Ja, det brukar vara smidigast. Vi planerar ordningen så att ni kan bo kvar och har tillgång till kök och badrum."),
    ("Måste betongen fuktmätas om plastmattan i hallen ska bytas mot trä?",
     "Ligger golvet på betong rekommenderar vi det. Fukt som stängs in under trägolvet kan bryta ned lim och golv."),
  ],
  "sources": [
    ("Huddinge kommun – Kulturmiljöprogram del 2 (pdf)",
     "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf"),
    _SKV, _SKV2, _GBR_L, _GBR_U,
  ],
  "cta": ("Dags att byta golv i huset i Huddinge?", "Boka ett gratis platsbesök så ser vi vad som ligger under och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Kök och matplats med nylagt ljust ekgolv i ett radhus från 1970-talet i Huddinge",
     "kitchen and dining area of a renovated late 1970s Swedish terraced house in Huddinge, newly laid light oak plank floor, simple white kitchen cabinets, large window to a small garden, empty dining table, daylight, no people, no text"),
    ("Hall där gammal plastmatta har rivits och golvet är förberett för trägolv",
     "hallway of a 1970s Swedish row house where an old patterned vinyl floor has been removed, exposed smooth subfloor with patched levelling compound, rolled up old vinyl and new oak floor packages stacked by the wall, natural light, no people, no hands, no text"),
  ],
  "related": [
    ("badrumsrenovering-huddinge.html", "Badrumsrenovering i Huddinge", "Från sportstuga till grupphus."),
  ],
},

}


# Korslänkar mellan v3-sidorna (golv/snickare/fasad) på samma ort.
_V3 = {"golvlaggare": ("Golvläggare", "Nya golv och slipning.", "bromma nacka solna taby lidingo huddinge"),
       "snickare": ("Snickare", "Altan, dörrar och snickerier.", "bromma solna huddinge sollentuna lidingo danderyd"),
       "fasadrenovering": ("Fasadrenovering", "Panel, puts och isolering.", "bromma nacka taby huddinge sollentuna lidingo")}
for _f, _d in PAGES_TJ.items():
    _pre, _o = _f[:-5].split("-", 1)
    _pa = "på" if _d["ort"] in ("Lidingö", "Södermalm", "Värmdö") else "i"
    for _k, (_lbl, _txt, _orter) in _V3.items():
        if _k != _pre and _o in _orter.split():
            _d.setdefault("related", []).append((f"{_k}-{_o}.html", f"{_lbl} {_pa} {_d['ort']}", _txt))
