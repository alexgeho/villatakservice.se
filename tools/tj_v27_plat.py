# -*- coding: utf-8 -*-
"""Plåtslagare – ortsidor v27: Kungsholmen, Södermalm, Östermalm, Vasastan, Sundbyberg, Spånga (2026-10-26).
Hubb: platslagare.html (TJ_HUB["platslagare"]). Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.
Innerstadssidorna har egen trust-rad (sidnyckel "trust"): plåtarbeten på husets tak ger inget rotavdrag i bostadsrätt.

Lokal vinkel per sida:
Kungsholmen – huvar, kanaler och skorstenar på stenstadens plåttak (ventilationshuv kräver oftast bygglov, aggregat
  under 80 x 60 x 30 cm, skorsten/rökkanal med sotaren), föreningen som beställare (områdesfakta).
Södermalm – två slags tak: malmarnas tidiga bebyggelse (omkring 300 hus, värdekärnorna) och stenstadens hyreshus;
  takkupor och vindsinredning (mindre takkupa lovpliktig i flerbostadshus, större = tillbyggnad, stadens vägledning),
  kalla vindar och fukt (Boverket).
Östermalm – taklandskapet i stadssiluetten (Norrmalm och Östermalm, 1800-talets senare del), plåttäckta tak upp till
  45 grader, Stadsmuseets klassning och ringar, balkongplåt och räcke 1,1 m (balkongvägledningen ej uppdaterad efter
  1 december 2025).
Vasastan – takfönster (stadens fönstersida), vindsinredning, Motorn och Vingen (slutet av 1910-talet, kooperativt med
  kommunalt stöd) och Observatoriekullen, bostadsrätterna i Gustav Vasa och Västra Matteus.
Sundbyberg – Duvbo: Egna Hem 1898, 325 tomter, 98 till 1924, riksintresse 1987, sekelskiftesvillornas tak i rött
  lertegel eller falsad slätplåt, utökad lovplikt för byte av takläggningsmaterial (kostnadsfri), stadens regler för
  övriga Sundbyberg (flerbostadshus mot allmän plats, solceller).
Spånga – villastäderna Solhem (kulturhistoriskt värdefull, Hem på landet), Bromsten, Flysta, Sundby; byte av
  taktäckning utan lov på villa (Boverket), belastning, utökad lovplikt; hängrännor, stuprör och dagvatten (SVOA).

Fakta endast från källorna i respektive 'sources', öppnade med curl (UA Mozilla) 2026-10-26, alla svarade 200;
pdf:erna (riksintressen, Varsam, områdesfakta, Duvbo, Älvsjö-inventeringen) har textlager och lästes med pdftotext.
Skatteverket lästes med curl (webbläsar-UA): småhus – reparera, rengöra eller byta ut plåttak, hängrännor och
stuprör, byta fönsterbleck, ställning i samband med rotarbete; bostadsrätt – reparera eller byta plåttak, hängrännor
och stuprör ger inget avdrag.
Strukna / ej använda: Stadsmuseets svarstid, avgifter och handläggningstider, vem som anlade Duvbo utöver
föreningen Egna Hem (Älvsjö-inventeringen nämner Hem på landet – motsägelse, inte använd för Duvbo), takvinklar på
enskilda hus, vilka hus på Södermalm som har vilka tak. Inga priser, garantier, omdömen, egna uppdrag eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_TRUST_BRF = ["Gratis besök och kostnadsförslag", "Underlag till föreningen"]
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"

_STH_FAS = ("Stockholms stad – Fasadändring", _SB + "fasadandring/")
_STH_FBH = ("Stockholms stad – Flerbostadshus", _SB + "flerbostadshus/")
_STH_HUV = ("Stockholms stad – Luftvärmepump, ventilationsaggregat och ventilationshuv",
            _SB + "luftvarmepump-ventilationsaggregat-och-ventilationshuv/")
_STH_SKO = ("Stockholms stad – Eldstad, braskamin och skorsten", _SB + "eldstad-braskamin-och-skorsten/")
_STH_BALK = ("Stockholms stad – Balkong", _SB + "balkong/")
_STH_FD = ("Stockholms stad – Fönster och dörrar", _SB + "fonster-och-dorrar/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_BV_TAK = ("Boverket – Ändra fasad eller tak",
           "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/andra-fasad-eller-tak/")
_BV_FUKT = ("Boverket – Fuktrisker i yttertak",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttertak/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SUN_FAS = ("Sundbybergs stad – Fasadändring",
            "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/fasadandring")
_SUN_DUVBO = ("Sundbybergs stad – Miljöprogram Duvbo (pdf)",
              "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf")
_ALV_INV = ("Stadsmuseet – Inventering av Älvsjö villastad (Stockholmskällan, pdf)",
            "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf")
_SVOA = ("Stockholm Vatten och Avfall – Bygga om: vatten och avlopp",
         "https://www.svoa.se/villa-och-radhus/vatten-och-avlopp/bygga-om/")


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_ROT_BRF = ("Bor du i bostadsrätt ger plåtarbeten på husets tak, hängrännor och stuprör inget rotavdrag enligt "
            "Skatteverket. Avdraget i en bostadsrätt gäller arbete innanför lägenhetens väggar, tak och golv som du själv "
            "ansvarar för enligt stadgarna, och taket är föreningens sak.")
_ROT_HUS = ("Äger du ett småhus räknar Skatteverket det som rotarbete att reparera, rengöra eller byta ut plåttak, "
            "hängrännor och stuprör, att byta fönsterbleck och att montera och montera ner byggnadsställningar i samband "
            "med arbetet. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år, och material "
            "och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ KUNGSHOLMEN
"platslagare-kungsholmen.html": {
  "kind": "district", "service": "platslagare", "ort": "Kungsholmen", "svc_label": "Plåtslagare",
  "title": "Plåtslagare på Kungsholmen – huvar, kanaler och skorstenar",
  "description": "Plåtslagare på Kungsholmen: plåt kring ventilationshuvar och skorstenar på stenstadens tak, när en ny huv kräver bygglov och hur föreningen beställer.",
  "h1": "Plåtslagare på Kungsholmen",
  "lead": "Ett plåttak på Kungsholmen är sällan bara plåt. Där sticker huvar, kanaler, skorstenar och stegar upp genom taket, och det är runt dem det oftast läcker. Geal Entreprenad AB har egna plåtslagare som byter och tätar plåt kring genomföringar, lägger om takplåt och tar fram underlaget som föreningen behöver.",
  "card": "Huvar, skorstenar och genomföringar.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "foreningen-kungsholmen", "anchor": "Föreningen",
     "h2": "Föreningen är oftast beställaren",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 44 554 bostäder i Kungsholmens stadsdelsområde. 30 598 av dem är bostadsrätter, 10 828 är övriga hyresrätter och 2 791 hör till allmännyttan, medan småhusen bara är några hundra. Det betyder att ett plåtjobb på taket i de flesta fall beställs av en bostadsrättsförening eller en fastighetsägare, inte av den som bor högst upp.",
       "Kungsholmen ingår i den klassiska stenstaden, som översiktsplanens riksintressedel beskriver som tät kvartersstad med bebyggelse från 1870 till 1930. Ett av karaktärsdragen som räknas upp är de sluttande taken, oftast plåttäckta och med en lutning upp till 45 grader från fasaden. Taket syns alltså från gatan, och därför bryr sig både staden och föreningen om hur plåten ser ut.",
     ],
     "aside": {"title": "Stenstadens tak enligt staden", "items": [
       "Sluttande, oftast plåttäckta", "Lutning upp till 45 grader", "Markerad takfot mot gatan", "Del av ett taklandskap"]}},
    {"id": "huvar-kungsholmen", "h2": "Nya huvar och kanaler – ofta bygglov",
     "paras": [
       "När en förening ser över ventilationen, till exempel i samband med stambyte, blir taket en del av projektet. Stockholms stad skriver att den som ska sätta upp en ny ventilationshuv på taket eller dra en ventilationskanal på fasaden oftast behöver bygglov, eftersom det kan påverka byggnadens utseende. Ett enstaka aggregat som är mindre än 80 x 60 x 30 centimeter och inte syns från gatan klarar sig däremot normalt utan lov.",
       "För flerbostadshus gäller dessutom att ändringar på fasad eller tak som vetter mot allmän plats kräver bygglov. Staden räknar byte av kulör eller material på taket som en fasadändring, liksom antenner, huvar och skorstenar. Vi ritar därför in nya huvar och deras plåtinklädnad redan i förslaget, så att föreningen kan söka lov med rätt underlag.",
     ],
     "aside": {"title": "Räknas som fasadändring", "items": [
       "Nytt material eller ny kulör på taket", "Ventilationshuv på taket", "Kanal på fasaden", "Ny skorsten"]}},
    {"id": "skorsten-kungsholmen", "h2": "Skorstenar och rökkanaler",
     "paras": [
       "En ny utvändig skorsten kan kräva bygglov och ska redovisas på fasadritningar, och den som installerar eller väsentligt ändrar en eldstad eller rökkanal ska göra en anmälan och vänta på startbesked. Staden råder fastighetsägaren att planera skorstenens utformning och placering tillsammans med skorstensfejarmästaren. Plåtslagaren kommer in när skorstenen är bestämd: med beslag, krage och anslutning mot takplåten.",
       "Läckor vid en skorsten eller en huv syns ofta först som en fläck i taket på våningen under. Vi går upp, öppnar plåten runt genomföringen och ser om felet sitter i själva anslutningen, i en skadad fals eller i underlaget. Hör fasaden också till projektet beskriver vi helheten under " + _L.format("fasadrenovering-kungsholmen.html", "fasadrenovering på Kungsholmen") + ".",
     ],
     "aside": None},
    {"id": "tillgang-kungsholmen", "h2": "Arbete på taket i ett flerbostadshus",
     "paras": [
       "På ett stenhus med flera våningar mot gatan behövs säkra vägar upp, skyddsräcken och ibland en ställning mot gården. Vi går igenom med föreningen var materialet kan tas upp, hur trapphuset skyddas och vilka lägenheter som behöver få veta när det bullrar. Stadens sida om flerbostadshus påminner också om att det är bra att informera grannar och styrelsen om det som planeras.",
       "När arbetet är klart lämnar vi en beskrivning av vad som har bytts och var, med foton från taket. Det är underlag som en styrelse har nytta av när nästa takinspektion görs eller när en ny styrelse tar över. Läs mer om tjänsten under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med plåttak på Kungsholmen",
  "steps": [
    ("Platsbesök", "Gratis besök på taket och på vinden där läckan syns."),
    ("Förslag", "Beskrivning av plåt, huvar och genomföringar med foton."),
    ("Bygglov", "Ritningar när huvar, kanaler eller material ändras mot gatan."),
    ("Planering", "Tillträde, ställning och information till de boende."),
    ("Utförande", "Byte och tätning av plåt kring varje genomföring."),
    ("Dokumentation", "Foton och beskrivning till styrelsen."),
  ],
  "rot_h2": "ROT-avdrag för plåtarbeten på Kungsholmen",
  "rot": [_ROT_BRF,
          "Äger du ett av de få småhusen i stadsdelen räknar Skatteverket däremot plåttak, hängrännor och stuprör som rotarbete, och då drar Geal avdraget direkt på fakturan."],
  "price_h2": "Vad påverkar priset för plåtarbeten på Kungsholmen?",
  "price": [
    "Takets yta och lutning, antalet huvar, skorstenar och genomföringar, om takplåten ska läggas om eller bara lagas, ställning och skydd samt om bygglovshandlingar behövs. Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver föreningen bygglov för en ny ventilationshuv på taket på Kungsholmen?",
     "Oftast ja. Stockholms stad skriver att en ny huv på taket eller en kanal på fasaden i regel kräver bygglov eftersom den påverkar husets utseende."),
    ("Får vi byta takplåten till en annan kulör på vårt hus på Kungsholmen?",
     "Byte av kulör eller material på taket räknas som fasadändring, och på ett flerbostadshus kräver det bygglov när taket vetter mot allmän plats."),
    ("Varför läcker det vid skorstenen på vårt tak på Kungsholmen?",
     "Ofta sitter felet i anslutningen mellan skorstenens plåtkrage och takplåten. Vi öppnar plåten och ser efter innan vi föreslår åtgärd."),
    ("Vem ska kontaktas innan en ny skorsten byggs på Kungsholmen?",
     "Staden råder att placering och utformning planeras med skorstensfejarmästaren, och en ny eldstad eller rökkanal ska anmälas."),
  ],
  "sources": [_of("Kungsholmens stadsdelsområde", "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade"), _RIKS,
              _STH_HUV, _STH_FAS, _STH_SKO, _STH_FBH, _SKV],
  "cta": ("Läcker det vid en huv eller skorsten på Kungsholmen?", "Boka ett gratis platsbesök, så går vi upp på taket och föreslår åtgärd innan föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Plåttak på ett stenhus med ventilationshuvar och skorstenar",
     "grey standing-seam metal roof of an early 1900s stone apartment building in Stockholm, several sheet metal ventilation hoods and brick chimneys with metal collars, roof safety ladder, overcast sky" + _SFX),
    ("Plåtkrage runt en skorsten på ett plåttak",
     "close view of a new sheet metal flashing collar around a plastered chimney on a grey standing-seam metal roof, neat folded seams, daylight" + _SFX),
    ("Ny ventilationshuv i plåt på ett tak",
     "new galvanised sheet metal ventilation hood on a pitched standing-seam metal roof of an apartment building, city rooftops in the background, clear sky" + _SFX),
  ],
},

# ------------------------------------------------------------------ SÖDERMALM
"platslagare-sodermalm.html": {
  "kind": "district", "service": "platslagare", "ort": "Södermalm", "svc_label": "Plåtslagare",
  "title": "Plåtslagare på Södermalm – takkupor, vindar och malmarna",
  "description": "Plåtslagare på Södermalm: plåt på takkupor vid vindsinredning, kalla vindar och fukt, stenstadens hyreshus och de äldre husen på malmarna.",
  "h1": "Plåtslagare på Södermalm",
  "lead": "På Södermalm möts två sorters tak: stenstadens hyreshus vid de breda gatorna och de äldre, låga husen uppe på bergen. Geal Entreprenad AB har egna plåtslagare som lägger plåt på takkupor, byter takplåt och lagar rännor på båda sorterna, och som hjälper föreningen med underlaget när vinden ska byggas om.",
  "card": "Takkupor, vindar och äldre tak.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "tva-tak-sodermalm", "anchor": "Två slags tak",
     "h2": "Stenstaden och malmarnas äldsta hus",
     "paras": [
       "Översiktsplanens riksintressedel beskriver hur stenstadens hyreshus präglar stora delar av malmarna, normalt fem våningar höga vid 18 meter breda gator. Samtidigt finns det enligt samma dokument omkring 300 hus kvar från den tidiga bebyggelsen på malmarna, mestadels på Södermalm. Fjällgatan, Katarinaberget, Vita bergen, Åsöberget och Östra Mariaberget pekas ut som värdekärnor.",
       "Dokumentet påpekar att de flesta äldre byggnaderna har byggts om och till under århundradena, så att det är svårt att tala om ett originalutförande. För en plåtslagare betyder det att varje tak i de miljöerna behöver ses för sig: vilka lager som finns, vilken plåt som ligger och vad som är värt att behålla.",
       "Bland karaktärsdragen för malmarnas tidiga bebyggelse nämner dokumentet den småskaliga bebyggelsen som en markant kontrast till den täta stenstaden runt omkring, och att byggnadsdetaljer som fönster, entréportar och ornamentik tillsammans bildar en karaktäristisk helhet. Plåt på tak, kupor och bleck hör till den helheten, och vi föreslår hellre lagning än byte där det går.",
     ],
     "aside": {"title": "Värdekärnor på malmarna", "items": [
       "Fjällgatan", "Katarinaberget", "Vita bergen", "Åsöberget", "Östra Mariaberget"]}},
    {"id": "kupor-sodermalm", "h2": "Takkupor när vinden byggs om",
     "paras": [
       "Riksintressedelen nämner vindsinredningar bland de mer begränsade förändringar som kan prövas enligt plan- och bygglagens varsamhetskrav, med stadsbyggnadskontorets vägledningar för vindsinredningar och balkonger som underlag. På stadens sida om flerbostadshus räknas mindre takkupor till de lovpliktiga fasadändringarna, medan en större takkupa räknas som en tillbyggnad.",
       "En takkupa i plåt har många detaljer som ska fungera ihop: kupans tak, sidor och fönsterbleck, anslutningen mot takfallet och avvattningen nedanför. Vi tar fram kupans plåtdetaljer tillsammans med föreningens arkitekt, så att de stämmer med bygglovsritningarna, och lägger plåten när stommen är klar. Inredningen av själva vinden beskriver vi under " + _L.format("totalrenovering-sodermalm.html", "totalrenovering på Södermalm") + ".",
     ],
     "aside": {"title": "Kupans plåtdetaljer", "items": [
       "Kupans tak och sidor", "Fönsterbleck", "Anslutning mot takfallet", "Ränna och stuprör"]}},
    {"id": "vind-sodermalm", "h2": "Kalla vindar och fukt",
     "paras": [
       "Boverket skriver att kalla vindar ofta drabbas av fuktskador, och att låglutande tak ofta drabbas av läckage. Fukten kan komma både ovanifrån och inifrån huset. På en vind som fortfarande är kall och används som förråd börjar vi därför med att titta på undersidan av taket: på fläckar, rost på spik och fukt i virket.",
       "Hittar vi läckor vid falsar, kupor eller genomföringar lagar vi plåten där. Är skadorna spridda över stora delar av taket föreslår vi i stället att plåten läggs om i etapper, så att föreningen kan planera kostnaden över flera år. Hela underlaget redovisas med foton, så att styrelsen ser samma sak som vi.",
     ],
     "aside": None},
    {"id": "foreningen-sodermalm", "h2": "Föreningen och de boende",
     "paras": [
       "Södermalms stadsdelsområde har enligt stadens områdesfakta för 2025 hela 77 525 bostäder, varav 43 680 bostadsrätter och 23 361 övriga hyresrätter. Det är alltså i regel en förening eller en fastighetsägare som beställer ett plåttak, och styrelsen som behöver underlag för beslutet.",
       "Vi beskriver arbetet så att styrelsen kan informera de boende: när det blir ljud från taket, om ställning eller skydd behövs mot gården och hur länge vinden är otillgänglig. Mer om tjänsten finns under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med plåttak på Södermalm",
  "steps": [
    ("Platsbesök", "Gratis besök på taket och på vinden."),
    ("Inventering", "Foton av plåt, kupor, falsar och genomföringar."),
    ("Förslag", "Lagning, omläggning i etapper eller plåt till nya kupor."),
    ("Lov", "Plåtdetaljer till föreningens bygglovsritningar vid nya kupor."),
    ("Utförande", "Plåtarbetet med skydd för gård och trapphus."),
    ("Överlämning", "Genomgång och dokumentation till styrelsen."),
  ],
  "rot_h2": "ROT-avdrag för plåtarbeten på Södermalm",
  "rot": [_ROT_BRF,
          "Bor du i ett av de få småhusen på Södermalm och äger det själv ger plåttak, hängrännor och stuprör rotavdrag enligt Skatteverket, och Geal drar avdraget direkt på fakturan."],
  "price_h2": "Vad påverkar priset för plåtarbeten på Södermalm?",
  "price": [
    "Om plåten lagas eller läggs om, takets yta och lutning, antalet kupor och genomföringar, ställning mot gata eller gård, hur material kan tas upp till taket och om plåtdetaljer ska tas fram till ett bygglov. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för takkupor när vinden byggs om på Södermalm?",
     "Ja, på ett flerbostadshus räknar staden mindre takkupor som lovpliktig fasadändring, och en större kupa räknas som tillbyggnad."),
    ("Varför blir det fuktskador på vår kalla vind på Södermalm?",
     "Boverket skriver att kalla vindar ofta drabbas av fuktskador. Fukten kan komma från läckor i taket men också inifrån huset, så båda behöver kontrolleras."),
    ("Finns det en vägledning för vindsinredning i stenhusen på Södermalm?",
     "Ja, översiktsplanens riksintressedel hänvisar till stadsbyggnadskontorets vägledningar för vindsinredningar och balkonger som underlag för prövningen."),
    ("Kan plåttaket läggas om i etapper på vårt hus på Södermalm?",
     "Ja, när skadorna är spridda kan omläggningen delas upp, så att föreningen kan fördela kostnaden över flera år."),
    ("Hur många av de äldsta husen på malmarna finns kvar på Södermalm?",
     "Enligt översiktsplanens riksintressedel återstår omkring 300 hus från den tidiga bebyggelsen på malmarna, mestadels på Södermalm."),
  ],
  "sources": [_RIKS, _STH_FBH, _STH_FAS, _BV_FUKT,
              _of("Södermalms stadsdelsområde", "inre-staden/sodermalm/sodermalm-stadsdelsomrade"), _SKV],
  "cta": ("Ska vinden byggas om eller taket ses över på Södermalm?", "Boka ett gratis platsbesök, så inventerar vi taket, kuporna och vinden och föreslår åtgärder innan föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Plåttak med takkupor på ett stenhus på en höjd",
     "early 1900s plastered apartment building on a hill in Stockholm with a dark grey standing-seam metal roof and several small metal-clad dormers, view over rooftops, late afternoon light" + _SFX),
    ("Takkupa klädd i falsad plåt",
     "close view of a dormer window clad in grey folded standing-seam sheet metal, metal window sill flashing and small gutter below, pitched metal roof around it, daylight" + _SFX),
    ("Kall vind under ett plåttak med synliga takstolar",
     "interior of a cold unheated attic under a metal roof in an old apartment building, wooden rafters and roof boards, small skylight, storage cages, soft daylight, empty" + _SFX),
  ],
},

# ------------------------------------------------------------------ ÖSTERMALM
"platslagare-ostermalm.html": {
  "kind": "district", "service": "platslagare", "ort": "Östermalm", "svc_label": "Plåtslagare",
  "title": "Plåtslagare på Östermalm – taklandskap och balkongplåt",
  "description": "Plåtslagare på Östermalm: plåttak som syns i stadssiluetten, Stadsmuseets klassning, bygglov för nytt material eller ny kulör och plåt på balkonger.",
  "h1": "Plåtslagare på Östermalm",
  "lead": "Östermalms tak är en del av den stadssiluett som syns från vattnet och från höjderna runt innerstaden. Det gör att även ett rent underhållsjobb på plåten kan bli en fråga om utseende. Geal Entreprenad AB har egna plåtslagare som lagar och lägger om takplåt, byter plåt på balkonger och tar fram underlaget till föreningen och Stadsmuseet.",
  "card": "Taklandskapet och balkongerna.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "siluett-ostermalm", "anchor": "Taklandskapet",
     "h2": "En del av stadens siluett",
     "paras": [
       "Översiktsplanens riksintressedel beskriver att grundanslaget i dagens stadssiluett utgörs av stenstadens stora, sammanhållna bebyggelsemassa på Norrmalm och Östermalm, som till största delen uppfördes under 1800-talets senare del. Bebyggelsen är enligt dokumentet också fonden mot Gamla stan och innerstadens stadsfronter.",
       "Stenstadens tak beskrivs som sluttande, oftast plåttäckta och med en lutning upp till 45 grader från fasaden. När taklandskapet nämns som karaktärsdrag handlar det om helheten – hur taken samspelar kvarter för kvarter. En omlagd plåt i fel kulör eller med fel falsning kan därför märkas även om resten av huset är orört.",
       "Dokumentet skriver också att siluetten i stadens centrala delar är känslig och att byggnader från tiden före andra världskriget ofta har en viktig roll för upplevelsen av Stockholm som historisk stadsmiljö, vilket gör att påbyggnader i regel är olämpliga. För plåtslagaren betyder det att vi i första hand behåller takets form och arbetar med det material som redan ligger.",
     ],
     "aside": {"title": "Stenstaden på Östermalm", "items": [
       "Byggd mest under 1800-talets senare del", "Plåttäckta, sluttande tak", "Del av siluetten", "Fond mot Gamla stan"]}},
    {"id": "klass-ostermalm", "h2": "Stadsmuseets karta och bygglovet",
     "paras": [
       "Stockholms stad räknar byte av kulör eller material på taket som en fasadändring, och på ett flerbostadshus krävs bygglov när taket vetter mot allmän plats. Därtill kräver staden bygglov för åtgärder som annars kan vara lovbefriade om huset ligger inom riksintresse för kulturmiljövården, som visas med blå ring på Stadsmuseets karta, eller om huset är blå- eller grönmarkerat.",
       "Vi börjar därför varje uppdrag på Östermalm med att titta på kartan tillsammans med föreningen. Ska plåten bara lagas med samma material och utförande blir frågan en annan än om taket ska få en ny kulör eller en ny typ av plåt. Staden påpekar att det också finns hus som ännu inte är inventerade, och då kan museet behöva göra en bedömning.",
     ],
     "aside": {"title": "Bygglov krävs enligt staden om huset", "items": [
       "Ligger inom riksintresse (blå ring)", "Ligger i särskilt värdefullt område (grön ring)", "Är blå- eller grönmarkerat", "Har skydd i detaljplanen"]}},
    {"id": "balkong-ostermalm", "h2": "Plåt på balkonger och detaljer",
     "paras": [
       "Har balkongerna plåt på ovansidan och på listerna under är det plåten som skyddar plattan. När plåten rostar eller lossnar rinner vatten in i plattan, och då är det dags att byta. Staden skriver att en balkong är en viktig del av byggnadens arkitektur, och att ett räcke ska vara minst 1,1 meter högt när nya balkonger byggs. Stadens balkongvägledning är enligt staden inte uppdaterad efter lagändringarna den 1 december 2025.",
       "Vi byter balkongplåt och plåt på lister, gesimser och fönsterbleck så att utformningen stämmer med det som fanns. Där fasaden också behöver åtgärdas samordnar vi med " + _L.format("fasadrenovering-ostermalm.html", "fasadrenovering på Östermalm") + ", så att ställningen bara behöver stå uppe en gång.",
     ],
     "aside": None},
    {"id": "underlag-ostermalm", "h2": "Underlag till styrelsen",
     "paras": [
       "I Hedvig Eleonora församling finns enligt stadens områdesfakta för 2025 7 344 bostäder, varav 5 164 bostadsrätter och 2 110 övriga hyresrätter. Allmännyttan har bara 68 lägenheter där. Plåttaket är alltså i de flesta fall en fråga för en bostadsrättsförening.",
       "Vi lämnar en beskrivning med foton av taket, en lista över vad som behöver göras nu och vad som kan vänta, och plåtdetaljer som kan användas i en bygglovsansökan. Mer om tjänsten finns under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med plåttak på Östermalm",
  "steps": [
    ("Platsbesök", "Gratis besök på taket, på vinden och på balkongerna."),
    ("Kartan", "Vi går igenom Stadsmuseets klassning med föreningen."),
    ("Förslag", "Lagning eller omläggning med samma material och utförande."),
    ("Bygglov", "Underlag när material eller kulör ska ändras."),
    ("Utförande", "Takplåt, balkongplåt, lister och bleck."),
    ("Dokumentation", "Foton och beskrivning till styrelsen."),
  ],
  "rot_h2": "ROT-avdrag för plåtarbeten på Östermalm",
  "rot": [_ROT_BRF,
          "Äger du ett småhus räknar Skatteverket däremot plåttak, hängrännor och stuprör som rotarbete, och Geal drar då avdraget direkt på fakturan."],
  "price_h2": "Vad påverkar priset för plåtarbeten på Östermalm?",
  "price": [
    "Takets yta och form, om plåten lagas eller läggs om, balkonger, lister och bleck, ställning mot gatan, skydd för entréer och trottoar och om bygglovsunderlag behövs. Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för att byta takplåt på Östermalm?",
     "Ska materialet eller kulören ändras krävs bygglov när taket vetter mot allmän plats, och inom riksintresset kan lov krävas även för åtgärder som annars är lovbefriade."),
    ("Hur ser vi om vårt hus på Östermalm är klassat av Stadsmuseet?",
     "Stadsmuseets karta visar klassningen med färger och ringar. Är huset inte inventerat kan museet behöva göra en bedömning."),
    ("När behöver balkongplåten bytas på ett stenhus på Östermalm?",
     "När plåten rostar, spricker eller lossnar så att vatten kan rinna in i balkongplattan."),
    ("Vad gäller om vårt hus på Östermalm inte är inventerat av Stadsmuseet?",
     "Staden skriver att streckade ytor på kartan ännu inte är inventerade. Utanför riksintresse och särskilt värdefulla områden kan bygglov ändå behövas, och museet kan göra en bedömning."),
    ("Kan plåtbytet samordnas med fasadrenoveringen på Östermalm?",
     "Ja, då behöver ställningen bara stå uppe en gång och plåtdetaljerna anpassas till fasaden."),
  ],
  "sources": [_RIKS, _STH_FAS, _STH_KL, _STH_BALK,
              _of("Hedvig Eleonora", "inre-staden/norra-innerstaden/hedvig-eleonora"), _SKV],
  "cta": ("Behöver taket eller balkongerna ses över på Östermalm?", "Boka ett gratis platsbesök, så går vi igenom taket, balkongerna och Stadsmuseets karta med styrelsen innan föreningen får ett skriftligt kostnadsförslag med det som behöver göras nu och det som kan vänta."),
  "img": [
    ("Plåttak på stenhus från sent 1800-tal i innerstaden",
     "late 1800s ornate stone apartment buildings in Stockholm with steep dark grey standing-seam metal roofs, decorative cornices and small round dormers, roofscape seen from slightly above, soft morning light" + _SFX),
    ("Balkong med ny plåt på ovansidan",
     "close view of an old stone building balcony with new grey sheet metal flashing on top and on the edge profile, ornate cast iron railing, daylight" + _SFX),
    ("Falsat plåttak med takfot och hängränna",
     "detail of a dark grey standing-seam metal roof edge with gutter and decorative cornice on an old city apartment building, clear sky" + _SFX),
  ],
},

# ------------------------------------------------------------------ VASASTAN
"platslagare-vasastan.html": {
  "kind": "district", "service": "platslagare", "ort": "Vasastan", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Vasastan – takfönster och vindar",
  "description": "Plåtslagare i Vasastan: plåt kring nya takfönster, när takfönster kräver bygglov, vindsinredning i stenstaden och kvarteren Motorn och Vingen.",
  "h1": "Plåtslagare i Vasastan",
  "lead": "När en vind i Vasastan ska bli bostad blir takfönstren i regel en del av projektet, och varje takfönster är ett nytt hål i plåten. Geal Entreprenad AB har egna plåtslagare som tar upp och kläder in takfönster, lägger om plåt runt dem och tar fram detaljerna som föreningen behöver till bygglovet.",
  "card": "Takfönster, vindar och plåt.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "takfonster-vasastan", "anchor": "Takfönster",
     "h2": "Nya takfönster kräver ofta lov",
     "paras": [
       "Stockholms stad skriver att man ofta behöver bygglov för att ta upp nya eller ändra befintliga fönster och dörrar, eller för att sätta in nya takfönster. Det beror på vilken byggnad och vilken fasad det gäller, och en ny öppning kan också påverka den bärande konstruktionen så att den behöver förstärkas.",
       "För flerbostadshus gäller att ändringar på tak som vetter mot allmän plats kräver bygglov. Takfönster mot gården bedöms enligt samma regler men med andra förutsättningar. Vi ritar plåtdetaljerna kring varje takfönster – karmens inklädnad, anslutningen ovanför och nedanför och avledningen av vatten – så att de kan bifogas föreningens ansökan.",
       "Staden påminner om att nya öppningar kan ge ökad insyn för grannarna och att alla ändringar ska göras varsamt med hänsyn till byggnadens karaktär. På stadens sida om flerbostadshus beskrivs detaljritningen, i skala 1:10, 1:20 eller 1:50, som den ritning som visar byggnadsdetaljer som fönster, räcken och balkonger. Det är där plåtdetaljerna kring takfönstren hör hemma.",
     ],
     "aside": {"title": "Plåt runt ett takfönster", "items": [
       "Inklädnad av karmen", "Anslutning ovanför fönstret", "Plåt nedanför mot takfallet", "Avledning av vatten"]}},
    {"id": "vind-vasastan", "h2": "Vindsinredning i stenstaden",
     "paras": [
       "Vasastan hör till den klassiska stenstaden, som enligt översiktsplanens riksintressedel har en utbredning på Östermalm, Södermalm, Kungsholmen och Norrmalm. Dokumentet nämner vindsinredningar bland de begränsade förändringar som kan prövas enligt varsamhetskraven, med stadsbyggnadskontorets vägledningar som underlag, och beskriver taken som sluttande och oftast plåttäckta.",
       "En vindsinredning ändrar mer än takfönstren. Ventilation, rökkanaler och ibland balkonger påverkar också taket. Vi samordnar plåtarbetet med byggföretaget och arkitekten, så att taket blir tätt i varje etapp och inte öppnas mer än nödvändigt. Före varje helg och inför väntat regn täcker vi det som är öppet, så att vinden och lägenheterna under inte tar skada. Hur ett större ombyggnadsprojekt i stadsdelen kan läggas upp beskriver vi under " + _L.format("byggforetag-vasastan.html", "byggföretag i Vasastan") + ".",
     ],
     "aside": None},
    {"id": "kvarter-vasastan", "h2": "Motorn och Vingen och Observatoriekullen",
     "paras": [
       "Riksintressedelen lyfter fram kvarteren Motorn och Vingen i norra Vasastaden, uppförda i slutet av 1910-talet som ett tidigt exempel på kooperativt byggande med kommunalt stöd. Dokumentet skriver att bebyggelsen med gårdar och allmänna platser har stort kulturvärde att bevara. Runt Observatoriekullen ligger Stockholms ursprungliga högskoleområde, med bland annat Stockholms observatorium från 1753, den första Tekniska högskolan från sent 1800-tal, Handelshögskolan från mitten av 1920-talet och Stadsbiblioteket från 1928. Området karaktäriseras enligt dokumentet av grönska och luftighet, i tydlig kontrast till den omgivande stenstaden.",
       "I sådana miljöer är frågan om takets utseende ännu viktigare. Vi föreslår plåt och falsning som stämmer med det befintliga taket och tittar på Stadsmuseets karta innan något material eller någon kulör ändras. Där huset har kvar äldre plåtdetaljer, som bleck och lister, tar vi mått och gör nya delar efter samma form i stället för att byta till standardprofiler.",
     ],
     "aside": None},
    {"id": "foreningar-vasastan", "h2": "Bostadsrättsföreningarna",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 8 889 bostäder i Gustav Vasa församling, varav 5 707 bostadsrätter, och 12 579 i Västra Matteus, varav 8 990 bostadsrätter. Plåttak och takfönster beställs därför i de flesta fall av en förening, till exempel när föreningen bestämmer sig för att bygga om vinden.",
       "Vi lämnar ett underlag som styrelsen kan använda både för beslutet och för bygglovet: beskrivning, plåtdetaljer och foton av taket före arbetet. Mer om tjänsten finns under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med takfönster och plåt i Vasastan",
  "steps": [
    ("Platsbesök", "Gratis besök på vinden och taket."),
    ("Detaljer", "Plåtdetaljer för takfönster och anslutningar."),
    ("Bygglov", "Underlag till föreningens ansökan."),
    ("Etapper", "Taket öppnas bara så mycket som behövs."),
    ("Utförande", "Inklädnad, omläggning och tätning."),
    ("Genomgång", "Kontroll av tätheten och dokumentation."),
  ],
  "rot_h2": "ROT-avdrag för plåtarbeten i Vasastan",
  "rot": [_ROT_BRF,
          "Vid en vindsinredning är det oftast föreningen eller den som köper vinden som beställer, och reglerna för rotavdrag beror då på vem som äger bostaden och vad stadgarna säger."],
  "price_h2": "Vad påverkar priset för takfönster och plåt i Vasastan?",
  "price": [
    "Antal och storlek på takfönstren, takets lutning och plåttyp, om plåten runt omkring behöver läggas om, ställning och skydd samt om bygglovsunderlag ska tas fram. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för nya takfönster i Vasastan?",
     "Ofta. Stockholms stad skriver att nya takfönster ofta kräver bygglov, beroende på byggnad och fasad, och på flerbostadshus gäller lovplikt för tak mot allmän plats."),
    ("Vad gör plåtslagaren när ett takfönster sätts in i Vasastan?",
     "Kläder in karmen, ansluter plåten ovanför och nedanför fönstret och ser till att vattnet leds förbi öppningen."),
    ("Vilken ritning visar plåten runt takfönstren i Vasastan?",
     "Detaljritningen, som staden anger i skala 1:10, 1:20 eller 1:50 och som visar byggnadsdetaljer som fönster, räcken och balkonger."),
    ("Kan taket hållas tätt under en vindsinredning i Vasastan?",
     "Ja, vi öppnar taket i etapper och tätar varje del innan nästa öppnas."),
    ("När byggdes kvarteren Motorn och Vingen i Vasastan?",
     "I slutet av 1910-talet, som ett tidigt exempel på kooperativt byggande med kommunalt stöd enligt översiktsplanens riksintressedel."),
  ],
  "sources": [_STH_FD, _STH_FBH, _RIKS, _of("Gustav Vasa", "inre-staden/norra-innerstaden/gustav-vasa"),
              _of("Västra Matteus", "inre-staden/norra-innerstaden/vastra-matteus"), _SKV],
  "cta": ("Ska vinden byggas om i Vasastan?", "Boka ett gratis platsbesök, så går vi igenom vinden och tar fram plåtdetaljerna för takfönstren innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Plåttak med takfönster på ett stenhus i innerstaden",
     "pitched dark grey standing-seam metal roof of an early 1900s Stockholm apartment building with several new skylight windows in a row, rooftops and a church tower in the distance, clear sky" + _SFX),
    ("Takfönster med inklädnad i plåt",
     "close view of a skylight window in a grey standing-seam metal roof with neat folded sheet metal flashing around the frame, daylight, no reflections of people" + _SFX),
    ("Inredd vind med takfönster och synliga bjälkar",
     "newly converted attic apartment under a sloping roof with two skylight windows, exposed wooden beams, white walls, oak floor, empty room, soft daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SUNDBYBERG
"platslagare-sundbyberg.html": {
  "kind": "district", "service": "platslagare", "ort": "Sundbyberg", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Sundbyberg – Duvbos tak och lovplikten",
  "description": "Plåtslagare i Sundbyberg: falsad plåt och lertegel på Duvbos villor, utökad lovplikt för nytt takmaterial, flerbostadshus mot allmän plats och ROT.",
  "h1": "Plåtslagare i Sundbyberg",
  "lead": "I Duvbo har sekelskiftesvillorna ofta tak av falsad slätplåt eller rött lertegel, och där är lovplikten utökad så att även ett byte av takmaterial kräver bygglov. Geal Entreprenad AB har egna plåtslagare som lägger falsad plåt, byter hängrännor och stuprör och hjälper dig med underlaget till Sundbybergs stad.",
  "card": "Duvbos tak, rännor och lov.",
  "sections": [
    {"id": "duvbo-sundbyberg", "anchor": "Duvbo",
     "h2": "Duvbo – en av landets första egnahemsmiljöer",
     "paras": [
       "Sundbybergs miljöprogram för Duvbo berättar att föreningen Egna Hem bildades 1898 för att skapa egna hem för arbetare. Året därpå köpte föreningen egendomen Dufvebol och gjorde en stadsplan med 325 tomter, och 1924 utökades området västerut med ytterligare 98 villatomter. Riksantikvarieämbetet pekade 1987 ut Duvbo som riksintresse för kulturmiljövården.",
       "Husen är enligt programmet framför allt byggda vid sekelskiftet 1900 och under 1920-talet. Sekelskiftesvillornas tak i rött lertegel eller falsad plåt är ofta oregelbundna och har ibland torn och kupoler. För sekelskiftet anger programmet rött lertegel, falsad slätplåt och eventuellt papp, med synliga kontursågade taktassar.",
     ],
     "aside": {"title": "Taken i Duvbo enligt programmet", "items": [
       "Sekelskiftet: lertegel, falsad slätplåt, ev. papp", "1920-talet: rött lertegel", "1930–40-talen: flacka tak med lertegel", "Synliga taktassar"]}},
    {"id": "lov-sundbyberg", "h2": "Utökad lovplikt för takmaterial",
     "paras": [
       "I samband med en planändring för Duvbo har bygglovsplikten utökats. Den omfattar bland annat utbyte av fasadbeklädnad och takläggningsmaterial, omfärgning av fasaden och utbyte, flyttning eller igensättning av fönster och dörrar. Programmet anger att åtgärder inom ramen för den utökade lovplikten är kostnadsfria.",
       "Programmet säger också att byggnadens tidstypiska uttryck inte får förvanskas genom byte av takmaterial, och att material vid underhåll om möjligt ska väljas i överensstämmelse med originalet eller byggnadens tillkomsttid. För ett plåttak betyder det falsad plåt som liknar den som låg, inte en annan profil. Vi tar fram en beskrivning av material och utförande som kan bifogas ansökan.",
       "Programmet har också råd för hus som inte ser ut som originalen. Äldre hus som kraftigt förändrats bör om möjligt anpassas bättre till omgivningen i samband med andra åtgärder, och hus som tillkommit senare och avviker från den äldre stilen ska anpassas till omgivningen när det gäller takmaterial och färgsättning. Ett nytt plåttak kan alltså vara ett tillfälle att ta huset närmare Duvbos karaktär.",
     ],
     "aside": None},
    {"id": "ovriga-sundbyberg", "h2": "Övriga Sundbyberg",
     "paras": [
       "Utanför Duvbo gäller Sundbybergs stads vanliga regler. För en- och tvåbostadshus krävs inte längre bygglov för fasadändringar, så länge huset inte är kulturhistoriskt värdefullt eller ligger i ett särskilt värdefullt område. För flerbostadshus och kontorshus krävs bygglov om ändringen görs på fasad eller tak som vetter mot allmän plats.",
       "Staden skriver också att solcellspaneler kräver bygglov oavsett hustyp, och att det går att söka frivilligt bygglov om du vill vara säker på att en åtgärd följer lagens krav. Ska taket bytas helt beskriver vi den delen under " + _L.format("taklaggare-sundbyberg.html", "takläggare i Sundbyberg") + ".",
     ],
     "aside": {"title": "Bygglov i Sundbyberg", "items": [
       "Duvbo: utökad lovplikt", "Villa utanför värdefulla områden: inget lov för fasadändring", "Flerbostadshus mot allmän plats: lov", "Solceller: lov"]}},
    {"id": "rannor-sundbyberg", "h2": "Rännor, stuprör och detaljer",
     "paras": [
       "På en sekelskiftesvilla sitter plåten inte bara på taket. Hängrännor, stuprör, fönsterbleck, plåt på verandatak och beslag runt torn och kupoler hör till samma helhet. Vi byter det som är skadat och anpassar nya delar efter det som finns kvar, så att huset behåller sitt uttryck. Runda hängrännor och stuprör i plåt passar de flesta äldre villor, och vi målar dem gärna i en kulör som stämmer med huset.",
       "Innan vi lägger om någon plåt kontrollerar vi underlaget och takassarna. Programmet räknar de synliga, kontursågade taktassarna till sekelskiftesvillornas karaktär, så vi skyddar dem under arbetet. Programmet påminner också om plan- och bygglagens krav på att ändringar ska utföras varsamt, så att byggnadens särdrag beaktas och dess byggnadstekniska, historiska och kulturhistoriska värden tas till vara. Mer om tjänsten finns under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med plåttak i Sundbyberg",
  "steps": [
    ("Platsbesök", "Gratis besök där vi ser på tak, rännor och detaljer."),
    ("Lovfrågan", "Vi kontrollerar om huset ligger i Duvbo eller är värdefullt."),
    ("Beskrivning", "Material och utförande till ansökan."),
    ("Ansökan", "Du söker lov med vårt underlag när det krävs."),
    ("Utförande", "Falsad plåt, rännor, stuprör och bleck."),
    ("Genomgång", "Kontroll av avvattning och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för plåtslagare i Sundbyberg",
  "rot": [_ROT_HUS,
          "Bor du i en bostadsrätt i ett flerbostadshus ger plåtarbeten på husets tak inget rotavdrag."],
  "price_h2": "Vad påverkar priset för plåtarbeten i Sundbyberg?",
  "price": [
    "Takets yta och form, torn och kupoler, om plåten lagas eller läggs om, rännor och stuprör, ställning och om en beskrivning till bygglovet behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för att byta takplåt på en villa i Duvbo?",
     "Ja. I Duvbo omfattar den utökade lovplikten byte av takläggningsmaterial, och enligt miljöprogrammet är sådana ansökningar kostnadsfria."),
    ("Vilket takmaterial hade sekelskiftesvillorna i Duvbo?",
     "Miljöprogrammet anger rött lertegel, falsad slätplåt och eventuellt papp, med synliga kontursågade taktassar."),
    ("Behöver jag bygglov för plåtarbeten på en villa utanför Duvbo i Sundbyberg?",
     "Inte för fasadändringar på en- och tvåbostadshus, så länge huset inte är kulturhistoriskt värdefullt eller ligger i ett särskilt värdefullt område."),
    ("Vilket takmaterial ska ett nyare hus i Duvbo ha?",
     "Miljöprogrammet säger att hus som tillkommit senare och avviker från äldre stil ska anpassas till omgivningen när det gäller takmaterial och färgsättning."),
    ("Kräver solceller bygglov i Sundbyberg?",
     "Ja, Sundbybergs stad skriver att solcellspaneler kräver bygglov."),
  ],
  "sources": [_SUN_DUVBO, _SUN_FAS, _SKV],
  "cta": ("Ska taket eller rännorna ses över i Sundbyberg?", "Boka ett gratis platsbesök, så går vi igenom taket och lovfrågan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla med falsat plåttak och torn",
     "Swedish wooden villa from around 1900 with a dark red folded standing-seam metal roof, a small tower with a pointed metal roof, ornate carved wooden details, lush garden with fruit trees, picket fence, summer" + _SFX),
    ("Hängränna och stuprör på ett äldre trähus",
     "simple view of the eaves corner of an old red painted wooden villa, one straight half-round grey metal gutter along the eaves connected to one vertical round downpipe running down the wall, decorative rafter tails, green garden, daylight" + _SFX),
    ("Falsat plåttak på en kupa",
     "detail of a small dormer with a folded standing-seam metal roof on an old wooden villa, red clay tile roof around it, clear sky" + _SFX),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"platslagare-spanga.html": {
  "kind": "district", "service": "platslagare", "ort": "Spånga", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Spånga – villastädernas tak och rännor",
  "description": "Plåtslagare i Spånga: plåttak, rännor och stuprör i Solhem, Bromsten och Flysta, när byte av takmaterial är lovfritt och dagvatten från stuprören.",
  "h1": "Plåtslagare i Spånga",
  "lead": "Spångas villastäder växte fram kring järnvägen och består av individuellt utformade hus med glasverandor, kupor och snickarglädje. Geal Entreprenad AB har egna plåtslagare som lägger plåttak, byter hängrännor och stuprör och kläder in kupor och verandatak på villorna i Solhem, Bromsten och Flysta.",
  "card": "Villatak, rännor och stuprör.",
  "sections": [
    {"id": "villastad-spanga", "anchor": "Villastäderna",
     "h2": "Villastäderna kring järnvägen",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur små stationssamhällen uppstod när järnvägen byggdes ut och hur några av dem, till exempel Spånga, på 1910-talet fick status som municipalsamhällen. Hässelby villastad, Bromsten, Nälsta, Solhem, Flysta och Sundby räknas till typen villastad, och i Solhem fick bara en tiondel av de stora tomterna bebyggas.",
       "Stadsmuseets inventering av Älvsjö villastad nämner att fastighetsbolaget AB Hem på landet redan hade anlagt Solhem innan bolaget köpte mark i Älvsjö 1908. Villastäderna var privat organiserade och fick enligt vägledningen en brokigare bebyggelse än stadens egnahemsområden, med trä som dominerande fasadmaterial och glasverandor, takkupor och snickarglädje som gav variation.",
     ],
     "aside": {"title": "Villastäder i Spånga", "items": [
       "Solhem – kulturhistoriskt värdefull miljö", "Bromsten", "Flysta", "Sundby"]}},
    {"id": "lov-spanga", "h2": "Nytt takmaterial utan bygglov – med undantag",
     "paras": [
       "Boverket skriver att du inte behöver bygglov för att byta taktäckningsmaterial på ditt småhus, även till ett tak som ser annorlunda ut. Ändringen ska ändå göras varsamt och anpassas till omgivningen, och innan du byter ska du kontrollera att taket klarar den nya belastningen. Undantagen gäller inte där utökad lovplikt gäller, till exempel nära eller inom särskilt värdefulla byggnader och områden.",
       "I vägledningens tabell är Solhem markerat som kulturhistoriskt värdefull miljö, medan Bromsten, Flysta och Sundby saknar sådan markering. Stadsmuseets karta visar vad som gäller för det enskilda huset. Vi tittar på kartan innan vi föreslår ett nytt material, och väljer hellre plåt och falsning som passar husets tid.",
       "Vägledningen påminner också om att många villor på 1960- och 1970-talen ersattes av grupper av enhetliga småhus, och den råder att förändringar i sammanhållna grupper av villor, radhus och kedjehus utformas utifrån ett helhetsperspektiv. Byter du plåt på ett radhus i en sådan grupp är det därför bra att prata med grannarna om material och kulör.",
     ],
     "aside": None},
    {"id": "rannor-spanga", "h2": "Hängrännor, stuprör och dagvatten",
     "paras": [
       "På de stora villatomterna i Spånga leds vattnet från taket via rännor och stuprör ut på tomten. Stockholm Vatten och Avfall skriver att dag- och dräneringsvatten inte får kopplas till kommunens spillvattenledning, och att du som fastighetsägare ansvarar för ledningarna på din egen tomt. Byter vi stuprör kontrollerar vi därför vart vattnet tar vägen.",
       "Rännor som har sjunkit, läcker i skarvarna eller rinner över vid kraftigt regn byter vi, och vi anpassar storleken efter takytan. På kupor och verandatak lägger vi ny plåt och nya bleck. Ska hela taket bytas finns mer under " + _L.format("taklaggare-spanga.html", "takläggare i Spånga") + ".",
     ],
     "aside": {"title": "Kontrollera vid nya stuprör", "items": [
       "Att dagvattnet inte går till spillvattnet", "Var vattnet leds ut på tomten", "Rännans storlek mot takytan", "Fall mot stupröret"]}},
    {"id": "agarform-spanga", "h2": "Vem äger husen?",
     "paras": [
       "Stadens områdesfakta för 2025 visar att 1 946 av 3 470 bostäder i Solhem är småhus med äganderätt. I Bromsten är 916 av 3 826 bostäder småhus med äganderätt och i Flysta 657 av 833. Det är alltså oftast villaägaren själv som beställer plåtarbetet, och då gäller rotavdraget för småhus.",
       "Vi kommer på ett gratis platsbesök, ser på tak, rännor och detaljer och lämnar ett skriftligt kostnadsförslag med det som behöver göras. Mer om tjänsten finns under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med villatak i Spånga",
  "steps": [
    ("Platsbesök", "Gratis besök där vi ser på tak, kupor och rännor."),
    ("Kartan", "Vi kontrollerar Stadsmuseets klassning av huset."),
    ("Belastning", "Vi ser över att taket klarar ett nytt material."),
    ("Förslag", "Plåt, rännor och stuprör anpassade efter huset."),
    ("Utförande", "Omläggning, bleck, rännor och stuprör."),
    ("Avslut", "Kontroll av avvattningen och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för plåtslagare i Spånga",
  "rot": [_ROT_HUS],
  "price_h2": "Vad påverkar priset för plåtarbeten i Spånga?",
  "price": [
    "Takets yta, lutning och antal kupor, om plåten läggs om eller lagas, rännornas och stuprörens längd, verandatak och bleck samt ställning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag bygglov för att byta till plåttak på min villa i Spånga?",
     "Normalt inte. Boverket skriver att byte av taktäckningsmaterial på ett småhus är lovfritt, men utökad lovplikt kan gälla i särskilt värdefulla områden."),
    ("Är Solhem i Spånga ett kulturhistoriskt värdefullt område?",
     "Ja, i stadens vägledning Varsam utveckling är Solhem markerat som kulturhistoriskt värdefull miljö."),
    ("Får stuprören på min villa i Spånga kopplas till avloppet?",
     "Nej, Stockholm Vatten och Avfall skriver att dag- och dräneringsvatten inte får kopplas till spillvattenledningen."),
    ("Ska plåttaket på mitt radhus i Spånga se ut som grannarnas?",
     "Stadens vägledning råder att förändringar i sammanhållna grupper av radhus och kedjehus görs utifrån ett helhetsperspektiv, så samma material och kulör är oftast det bästa valet."),
    ("Klarar mitt tak i Spånga ett tyngre takmaterial?",
     "Det behöver kontrolleras före bytet. Boverket påpekar att taket ska klara den nya belastningen."),
  ],
  "sources": [_VARSAM, _ALV_INV, _BV_TAK, _SVOA,
              _of("Solhem", "vasterort/jarva/solhem"), _of("Bromsten", "vasterort/jarva/bromsten"),
              _of("Flysta", "vasterort/jarva/flysta"), _SKV],
  "cta": ("Ska taket eller rännorna bytas i Spånga?", "Boka ett gratis platsbesök, så ser vi på taket och avvattningen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre trävilla med plåttak och glasveranda i en villastad",
     "early 1900s Swedish wooden villa painted light yellow with a dark grey standing-seam metal roof, glazed veranda and small dormer, large garden with apple trees and hedge, quiet suburban street, summer" + _SFX),
    ("Ny hängränna och stuprör vid takfoten på en villa",
     "close view of a new grey metal half-round gutter and downpipe on the eaves of an old wooden villa, painted fascia board, lawn below, daylight" + _SFX),
    ("Verandatak klätt med falsad plåt",
     "glazed wooden veranda of an old Swedish villa with a low-pitched folded sheet metal roof and neat metal flashings, garden in the background, summer light" + _SFX),
  ],
},
}
