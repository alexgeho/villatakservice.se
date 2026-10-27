# -*- coding: utf-8 -*-
"""Takrenovering på Kungsholmen, Södermalm, Vasastan och Östermalm (v29, 2026-10-27).
Innerstaden: oftast bostadsrättsföreningens tak – egen trust-rad utan ROT-löfte i hero.
Lokala fakta är kontrollerade mot källorna i "sources" (öppnade 2026-10-27).
Inga priser, garantier, recensioner, kundcase eller certifieringar."""
from tj_v29_takreno_a import SKV_ROT, SKV_RATT, OF, BL_FASAD, BL_KLASS, BOV_YTSKIKT, NO_PEOPLE

RIKS = "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf"
BL_FLERBO = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/flerbostadshus/"
BL_KULT = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/kulturhistorisk-vardefull-byggnad-och-omrade/"
TRUST_BRF = ["Gratis besök och kostnadsförslag", "Underlag till föreningen"]


def _rot_brf(ort_pa, smahus_text):
    return [
        "Bor du i bostadsrätt ger arbete på husets tak inget rotavdrag enligt "
        f'<a class="text-link" href="{SKV_ROT}" rel="noopener">Skatteverket</a>. Avdraget i en bostadsrätt '
        "gäller arbete inne i lägenheten som du själv ansvarar för enligt stadgarna, och taket är föreningens sak. "
        "Det är föreningen som beställer och betalar.",
        f"{smahus_text} Äger du ett småhus {ort_pa} räknar Skatteverket däremot reparation och byte av takpannor och "
        "hängrännor som rotarbete. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år, "
        "och Geal drar det direkt på fakturan. Läs mer under "
        '<a class="text-link" href="rot-avdrag-takarbete.html">rotavdrag för takarbete</a>.',
    ]


TRP29B = {}

# ---------------------------------------------------------------- KUNGSHOLMEN
TRP29B["Kungsholmen"] = {
    "title": "Takrenovering på Kungsholmen – plåttak och föreningar",
    "description": "Takrenovering på Kungsholmen: plåttaken i stenstaden, funkishusen i Fredhäll och "
                   "Kristineberg, bygglov för ny kulör mot gatan och underlag till styrelsen.",
    "lead": "På Kungsholmen finns drygt 44 500 bostäder, och nästan sju av tio är bostadsrätter. Den som "
            "beställer en takrenovering här är därför oftast en bostadsrättsförening. Taken i stenstaden är "
            "branta och plåttäckta, och i Fredhäll och Kristineberg står funkishus från 1930-talet. Båda "
            "typerna har sina egna regler när kulör eller material ska ändras.",
    "card": "Plåttak i stenstaden och funkis i Fredhäll.",
    "trust": TRUST_BRF,
    "sections": [
        {"id": "hus", "h2": "En stadsdel av föreningar",
         "paras": [
             "Stadens statistik för 2024 visar 44 554 bostäder i Kungsholmens stadsdelsområde. 30 598 av dem är "
             "bostadsrätter, och bara 337 ligger i småhus. Det betyder att nästan alla tak på Kungsholmen ägs av "
             "en förening eller en fastighetsägare, inte av den som bor under dem.",
             "Kungsholmens kvarter är gamla. När staden beskriver riksintresset nämns bland annat att ett kvarter "
             "omfattas av en stadsplan för hela Kungsholmen från 1880. Staden räknar Kungsholmen till den klassiska "
             "stenstaden: den täta kvartersstaden med bebyggelse från 1870–1930."],
         "aside": {"title": "Kungsholmen i siffror (2024)",
                   "items": ["44 554 bostäder", "30 598 bostadsrätter", "337 bostäder i småhus",
                             "Riksintresse: Stockholms innerstad (AB 115)"]}},
        {"id": "plattak", "h2": "Branta plåttak i stenstaden",
         "paras": [
             "Staden beskriver stenstadens tak som sluttande, oftast plåttäckta och med en lutning på upp till 45 "
             "grader från fasaden. Tillsammans bildar de ett karaktäristiskt taklandskap. Mot gatan har husen ofta "
             "en markerad takfot och ibland en attikavåning.",
             "En takrenovering på ett sådant hus handlar sällan om att byta material. Oftare är det plåten som "
             "behöver målas om, falsarna som behöver tätas eller underlaget under en del av taket som behöver "
             "bytas. Runt huvar, skorstenar och takfönster sitter de detaljer som läcker först."],
         "aside": {"title": "Det vi ofta gör på plåttak",
                   "items": ["Tvätt och ommålning av takplåt", "Tätning av falsar och skarvar",
                             "Byte av plåt där underlaget är skadat", "Nya beslag runt genomföringar"]}},
        {"id": "fredhall", "h2": "Funkishusen i Fredhäll och Kristineberg",
         "paras": [
             "Omkring 1930 började nya stadsdelar byggas efter funktionalismens ideal. I innerstaden var det framför "
             "allt i utkanterna, till exempel i Fredhäll och Kristineberg på Kungsholmen. Fristående huskroppar med "
             "öppna, gröna gårdar blev idealet.",
             "Husen från den tiden har andra tak än stenstaden, och de ska renoveras så att de behåller sin form. "
             "Vi börjar med att ta reda på hur taket är uppbyggt – från vinden och med gamla ritningar om "
             "föreningen har dem – innan vi föreslår en metod."]},
        {"id": "lov", "h2": "Ny kulör mot gatan kräver bygglov",
         "paras": [
             "För flerbostadshus behövs bygglov när en ändring görs på fasad eller tak som vetter mot allmän plats. "
             "Staden räknar byte av kulör eller material på taket som en fasadändring. Ska ett grönt plåttak bli "
             "svart mot gatan behöver föreningen alltså söka bygglov, och kulören ska anges enligt NCS-systemet.",
             "Mot gården kan en ändring vara lovfri om vissa förutsättningar är uppfyllda. Är byggnaden särskilt "
             "kulturhistoriskt värdefull gäller dock utökad lovplikt, och "
             f'<a class="text-link" href="{BL_KLASS}" rel="noopener">Stadsmuseets klassificeringskarta</a> '
             "ger en första indikation. Målas taket om i samma kulör ändras inte utseendet."]},
        {"id": "styrelsen", "h2": "Underlag till styrelsen",
         "paras": [
             "Styrelsen behöver kunna jämföra och förklara beslutet för medlemmarna. Efter ett gratis besök på "
             "taket och vinden får föreningen ett skriftligt kostnadsförslag med foton av skadorna, en beskrivning "
             "av varje moment och vad som kan vänta.",
             "Behövs bygglov tar vi fram en takplan som visar det befintliga taket och det som ska ändras, och "
             "hjälper till med material- och kulörbeskrivningen. Läs mer om "
             '<a class="text-link" href="plattak.html">plåttak</a> och '
             '<a class="text-link" href="takbesiktning.html">takbesiktning</a>.']},
    ],
    "steps": [
        ("Besök", "Gratis besök på taket och på vinden tillsammans med styrelsen."),
        ("Förslag", "Skriftligt kostnadsförslag med foton och beskrivning av varje moment."),
        ("Lov", "Takplan och kulörbeskrivning om kulör eller material ändras mot gatan."),
        ("Planering", "Ställning, tillträde och information till de boende."),
        ("Utförande", "Ommålning, tätning eller byte av plåt och beslag."),
        ("Dokumentation", "Foton och beskrivning till föreningens underhållsplan."),
    ],
    "rot": _rot_brf("på Kungsholmen",
                    "Bara 337 bostäder på Kungsholmen ligger i småhus, de flesta på Stora Essingen."),
    "price": [
        "Kostnaden för en takrenovering på Kungsholmen påverkas av takets yta och lutning, om plåten ska målas "
        "eller bytas, antalet huvar, skorstenar och takfönster, ställning mot gatan och om bygglovshandlingar "
        'behövs. Läs mer om <a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a>.'],
    "faq": [
        ("Behöver vår förening på Kungsholmen bygglov för att måla om plåttaket?",
         "Inte om kulören är densamma. Byter ni kulör eller material på den del av taket som vetter mot gatan "
         "krävs bygglov för ett flerbostadshus."),
        ("Kan vi som bor i lägenheten få rotavdrag för takrenoveringen?",
         "Nej. Taket är föreningens ansvar, och rotavdrag i en bostadsrätt gäller bara arbete inne i lägenheten "
         "som du själv ansvarar för."),
        ("Vad är en takplan?",
         "En måttsatt ritning av taket sett uppifrån, med det som finns och det som ska ändras. Staden kräver den "
         "bland annat när takets utseende ändras."),
        ("Hur vet vi om vårt hus på Kungsholmen är kulturhistoriskt klassat?",
         "Titta i Stadsmuseets klassificeringskarta. Den ger en första indikation, men ibland behöver Stadsmuseet "
         "göra en egen bedömning."),
    ],
    "sources": [
        ("Stockholms stad – Områdesfakta Kungsholmens stadsdelsområde (2025)",
         OF + "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade.pdf"),
        ("Stockholms stad – Riksintressen i översiktsplanen", RIKS),
        ("Stockholms stad – Fasadändring", BL_FASAD),
        ("Stockholms stad – Flerbostadshus", BL_FLERBO),
        ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", BL_KLASS),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "img": [
        ("Stenstadshus med branta plåttak och skorstenar längs en gata",
         "row of Stockholm inner-city stone apartment buildings from around 1900 with rendered facades in ochre and "
         "light grey, steep dark green and black standing-seam metal roofs with chimneys and small dormers, a "
         "marked cornice, seen from across a quiet street, morning light" + NO_PEOPLE + ", no cars"),
        ("Röd länga med ställning och nytt tak under arbete",
         "close view of a freshly painted dark grey standing-seam metal roof on a city apartment building with a "
         "rendered chimney, a roof hatch and a small roof window, safety rails, clear sky" + NO_PEOPLE),
        ("Ljusa lamellhus bland gräsmattor och träd",
         "Swedish 1930s functionalist apartment buildings, narrow lamella blocks with light rendered facades and "
         "shallow roofs, set among lawns and trees on a slope, Stockholm, summer" + NO_PEOPLE + ", no cars"),
    ],
}

# ---------------------------------------------------------------- SÖDERMALM
TRP29B["Södermalm"] = {
    "title": "Takrenovering på Södermalm – stenstaden och bergen",
    "description": "Takrenovering på Södermalm: plåttak i stenstaden, storgårdskvarteren vid Helgalunden "
                   "och Blecktornsparken och kulturreservaten på bergen.",
    "lead": "Södermalm har över 77 000 bostäder, och mer än hälften är bostadsrätter. De flesta tak tillhör "
            "alltså en förening. Här finns allt från timmerstugor från 1700-talet på Åsöberget till "
            "1920-talets storgårdskvarter och stenstadens branta plåttak. En takrenovering på Södermalm börjar "
            "med att ta reda på vilken av de miljöerna huset hör till.",
    "card": "Stenstad, storgårdskvarter och bergen.",
    "trust": TRUST_BRF,
    "sections": [
        {"id": "hus", "h2": "Föreningarna äger taken",
         "paras": [
             "Stadens statistik för 2024 visar 77 525 bostäder i Södermalms stadsdelsområde. 43 680 är "
             "bostadsrätter och drygt 10 000 tillhör allmännyttan. Endast 211 bostäder ligger i småhus.",
             "För de flesta på Södermalm är taket därför något styrelsen beslutar om. Det påverkar hur arbetet "
             "planeras: medlemmarna ska informeras, ställning och tillträde ska ordnas, och beslutet ska kunna "
             "motiveras i föreningens underhållsplan."],
         "aside": {"title": "Södermalm i siffror (2024)",
                   "items": ["77 525 bostäder", "43 680 bostadsrätter", "211 bostäder i småhus"]}},
        {"id": "stenstad", "h2": "Stenstadens tak",
         "paras": [
             "Staden beskriver den klassiska stenstaden på malmarna med sluttande tak, oftast plåttäckta och med en "
             "lutning på upp till 45 grader, som tillsammans ger ett karaktäristiskt taklandskap. För den tidiga "
             "bebyggelsen på malmarna är stadens huvudfokus att husen inte får förvanskas och att alla ändringar ska "
             "göras varsamt, ofta i samråd med Stadsmuseet.",
             "För en förening betyder det att en takrenovering helst görs med samma material och kulör. Plåten "
             "målas om eller byts där underlaget är skadat, falsar tätas och beslagen runt skorstenar och huvar "
             "görs om. Då ändras inte husets utseende och inget bygglov behövs."]},
        {"id": "storgard", "h2": "Storgårdskvarteren vid Helgalunden och Blecktornsparken",
         "paras": [
             "På 1910- och 1920-talen byggdes nya kvarter kring stora, planterade gårdar. Kvarteret Metern vid "
             "Helgalunden har sin ursprungliga utformning väl bevarad från 1926–27, och kvarteren Draget och Ryssjan "
             "vid Blecktornsparken är välbevarade storgårdskvarter från 1920-talet.",
             "I stadens beskrivning av storgårdskvarteren nämns proportioner, fasadindelning, taklandskap och "
             "färgsättning som delar av en sammanhållen stadsbild. Ett tak i ett sådant kvarter ska därför "
             "renoveras så att det fortsätter att se ut som grannhusens."],
         "aside": {"title": "Storgårdskvarter på Södermalm",
                   "items": ["Metern vid Helgalunden (1926–27)", "Draget vid Blecktornsparken",
                             "Ryssjan vid Blecktornsparken"]}},
        {"id": "bergen", "h2": "Åsöberget, Vita bergen och Mariaberget",
         "paras": [
             "På Åsöberget ligger ett 30-tal små, tätt sammanbyggda timmerstugor, till stor del byggda under "
             "1700-talet för arbetare i hamnen. Vita bergen har småskalig bebyggelse från 1700- och 1800-talen. På "
             "Östra Mariaberget byggdes husen upp efter en stor brand 1759, och taken var brutna och täckta med "
             "tegel.",
             "Det mesta av bebyggelsen inom kulturreservaten på Östra Mariaberget, Skinnarviksberget, Åsöberget och "
             "Vita bergen ägs och förvaltas av Stadsholmen. Där är det alltså inte de boende som beställer taket."]},
        {"id": "lov", "h2": "Bygglov och klassning",
         "paras": [
             "För flerbostadshus krävs bygglov när kulör eller material på taket ändras på en sida som vetter mot "
             "allmän plats. Är byggnaden eller området särskilt kulturhistoriskt värdefullt gäller utökad lovplikt "
             "även för ändringar som annars är lovfria.",
             f'<a class="text-link" href="{BL_KLASS}" rel="noopener">Stadsmuseets klassificeringskarta</a> '
             "ger en första bild av hur huset är klassat. Ska föreningen ändra något på taket hjälper vi till med "
             "takplan och material- och kulörbeskrivning till ansökan."]},
    ],
    "steps": [
        ("Besök", "Gratis besök på taket och vinden tillsammans med styrelsen."),
        ("Klassning", "Vi kontrollerar Stadsmuseets karta och om ändringen vetter mot gatan."),
        ("Förslag", "Skriftligt kostnadsförslag med foton och prioriteringar."),
        ("Information", "Underlag till medlemmarna om ställning och tillträde."),
        ("Utförande", "Ommålning, tätning eller byte av plåt, papp och beslag."),
        ("Dokumentation", "Foton och beskrivning till underhållsplanen."),
    ],
    "rot": _rot_brf("på Södermalm", "Bara 211 bostäder på Södermalm ligger i småhus."),
    "price": [
        "Kostnaden för en takrenovering på Södermalm påverkas av takets yta och lutning, om plåten ska målas eller "
        "bytas, antalet skorstenar, huvar och takfönster, ställning och skydd mot gatan och om bygglov behövs. Läs "
        'mer om <a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a>.'],
    "faq": [
        ("Vem beslutar om taket i vår bostadsrättsförening på Södermalm?",
         "Styrelsen, inom ramen för föreningens stadgar och underhållsplan. Vi lämnar ett skriftligt underlag som "
         "styrelsen kan använda för beslutet."),
        ("Vi bor i ett storgårdskvarter vid Blecktornsparken – får vi byta takkulör?",
         "Staden beskriver taklandskap och färgsättning som en del av storgårdskvarterens helhet. Mot gatan krävs "
         "bygglov för ny kulör, och ändringen ska passa kvarteret."),
        ("Kan Geal renovera taket på en stuga på Åsöberget?",
         "De flesta husen i kulturreservaten på bergen ägs och förvaltas av Stadsholmen, som beställer själva. "
         "Äger du ett äldre hus utanför reservaten kommer vi gärna och tittar."),
        ("Behöver vi bygglov för att måla om plåttaket i samma kulör?",
         "Nej. Ommålning i samma kulör ändrar inte husets utseende och räknas som underhåll."),
    ],
    "sources": [
        ("Stockholms stad – Områdesfakta Södermalms stadsdelsområde (2025)",
         OF + "inre-staden/sodermalm/sodermalm-stadsdelsomrade.pdf"),
        ("Stockholms stad – Riksintressen i översiktsplanen", RIKS),
        ("Stockholms stad – Fasadändring", BL_FASAD),
        ("Stockholms stad – Flerbostadshus", BL_FLERBO),
        ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", BL_KLASS),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "img": [
        ("Taklandskap med plåttak och skorstenar i stenstaden",
         "view over a Stockholm inner-city roofscape on a hill: steep standing-seam metal roofs in dark red, black "
         "and green, many chimneys and small dormers, a church tower in the far distance, soft evening light"
         + NO_PEOPLE),
        ("Storgårdskvarter från 1920-talet runt en planterad gård",
         "Swedish 1920s neoclassical apartment block built around a large planted courtyard with lawn and trees, "
         "rendered facades in warm ochre, steep tiled and metal roofs with dormers, quiet afternoon" + NO_PEOPLE),
        ("Små timmerhus med tegeltak på en sluttning",
         "small 18th-century red-painted timber cottages tightly built together on a rocky slope, low roofs with "
         "red clay tiles, a narrow cobbled lane and a red wooden fence, summer" + NO_PEOPLE),
    ],
}

# ---------------------------------------------------------------- VASASTAN
TRP29B["Vasastan"] = {
    "title": "Takrenovering i Vasastan – Röda Bergen och stenstaden",
    "description": "Takrenovering i Vasastan: plåttak i stenstaden, prydnadsgavlarna i Röda Bergen, "
                   "Motorn och Vingen och bygglov för föreningar när taket ändras mot gatan.",
    "lead": "I Vasastan bor de flesta i bostadsrätt, och det är föreningarnas styrelser som beställer "
            "takrenoveringar. Taken i stenstaden är branta och plåttäckta, och i Röda Bergen reglerade "
            "stadsplanen till och med var prydnadsgavlarna fick sitta. En takrenovering i Vasastan ska därför "
            "laga det som är slut utan att ändra det som gör kvarteret till det det är.",
    "card": "Stenstad, Röda Bergen och föreningarnas tak.",
    "trust": TRUST_BRF,
    "sections": [
        {"id": "hus", "h2": "Bostadsrätter nästan överallt",
         "paras": [
             "Stadens statistik för 2024 visar 12 579 bostäder i Västra Matteus och 8 889 i Gustav Vasa, två av "
             "Vasastans statistikområden. I Västra Matteus är 8 990 bostadsrätter och i Gustav Vasa 5 707. Där "
             "finns inga småhus alls i Västra Matteus och bara 14 i Gustav Vasa.",
             "Taket är därför i regel föreningens. Det är styrelsen som beslutar, och underlaget ska kunna "
             "visas för medlemmarna på en stämma."],
         "aside": {"title": "Två delar av Vasastan (2024)",
                   "items": ["Västra Matteus: 12 579 bostäder", "varav 8 990 bostadsrätter",
                             "Gustav Vasa: 8 889 bostäder", "varav 5 707 bostadsrätter"]}},
        {"id": "rodabergen", "h2": "Röda Bergen – där planen styrde gavlarna",
         "paras": [
             "Röda Bergen är enligt staden innerstadens största miljö som helt präglas av 1910- och 1920-talens "
             "stadsbyggnadsidéer. Husen följer terrängen och gatorna är vinklade för att ge en intim närmiljö. I "
             "planen reglerades var prydnadsgavlar skulle finnas och att gårdarna skulle vara öppna och planterade.",
             "När ett tak i Röda Bergen renoveras ska gavlarna och takfallen alltså behålla den form planen gav "
             "dem. Plåtdetaljer och beslag runt gavlarna görs om med samma profil, och kulören följer det som "
             "finns i dag."],
         "aside": {"title": "1900-talets bostadsområden i Vasastan",
                   "items": ["Röda Bergen (1910–20-tal)", "Motorn och Vingen (slutet av 1910-talet)",
                             "Båda värdekärnor i riksintresset"]}},
        {"id": "motorn", "h2": "Motorn och Vingen",
         "paras": [
             "Kvarteren Motorn och Vingen i norra Vasastaden byggdes i slutet av 1910-talet. De är ett tidigt "
             "exempel på kooperativt byggande med kommunalt stöd, där man ville lösa bostadsbristen med goda "
             "bostäder till rimliga priser i omsorgsfullt gestaltade miljöer.",
             "Staden räknar bebyggelsen och gårdarna som ett stort kulturvärde att bevara. Det betyder inte att "
             "taket inte får renoveras, men att material, kulör och detaljer ska vara desamma när arbetet är klart."]},
        {"id": "stenstad", "h2": "Plåttaken i 1800-talets stenstad",
         "paras": [
             "Stora delar av Vasastan är klassisk stenstad. Staden beskriver taken där som sluttande, oftast "
             "plåttäckta och med en lutning på upp till 45 grader. Mot gatan har husen ofta en markerad takfot.",
             "På sådana tak är det oftast plåten och skarvarna som är slut, inte konstruktionen. En renovering kan "
             "vara tvätt och ommålning, byte av enskilda plåtar där underlaget har tagit skada och nya beslag runt "
             "skorstenar, huvar och takfönster. Läs mer om "
             '<a class="text-link" href="plattak.html">plåttak</a> och '
             '<a class="text-link" href="takmalning.html">takmålning</a>.']},
        {"id": "lov", "h2": "När behöver föreningen bygglov?",
         "paras": [
             "För flerbostadshus krävs bygglov när kulör eller material ändras på en fasad eller ett tak som vetter "
             "mot allmän plats. Kulören ska beskrivas enligt NCS-systemet, och staden kan begära en takplan som "
             "visar taket uppifrån med det befintliga och det nya.",
             "Mot gården kan en ändring vara lovfri om vissa förutsättningar är uppfyllda. Är huset särskilt "
             "kulturhistoriskt värdefullt gäller utökad lovplikt. "
             f'<a class="text-link" href="{BL_KLASS}" rel="noopener">Stadsmuseets klassificeringskarta</a> '
             "ger en första indikation."]},
    ],
    "steps": [
        ("Besök", "Gratis besök på taket och vinden med styrelsen."),
        ("Kartläggning", "Plåt, skarvar, beslag och genomföringar fotograferas."),
        ("Förslag", "Skriftligt kostnadsförslag med det som måste göras nu och det som kan vänta."),
        ("Lov", "Takplan och kulörbeskrivning om något ändras mot gatan."),
        ("Utförande", "Ommålning, tätning eller byte av plåt och beslag."),
        ("Dokumentation", "Foton och beskrivning till underhållsplanen."),
    ],
    "rot": _rot_brf("i Vasastan", "Småhus är mycket ovanliga i Vasastan."),
    "price": [
        "Kostnaden för en takrenovering i Vasastan påverkas av takets yta och lutning, om plåten ska målas eller "
        "bytas, antalet gavlar, skorstenar och takfönster, ställning mot gatan och om bygglov behövs. Läs mer om "
        '<a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a>.'],
    "faq": [
        ("Vårt hus ligger i Röda Bergen – får vi ändra takets form när vi renoverar?",
         "Planen för Röda Bergen reglerade bland annat var prydnadsgavlar skulle finnas, och staden räknar området "
         "som värdekärna i riksintresset. Räkna med att takets form ska behållas och prata med staden först."),
        ("Behöver föreningen bygglov för att byta plåt till samma kulör?",
         "Nej, inte om utseendet inte ändras. Bygglov krävs när kulör eller material ändras på en sida som vetter "
         "mot allmän plats."),
        ("Får medlemmarna rotavdrag när föreningen renoverar taket?",
         "Nej. Taket är föreningens ansvar, och rotavdrag i en bostadsrätt gäller arbete inne i lägenheten som "
         "medlemmen själv ansvarar för."),
        ("Hur lång tid tar en takrenovering på ett stenstadshus?",
         "Det beror på takets storlek och vad som ska göras. Efter besöket får föreningen en tidsplan i "
         "kostnadsförslaget, så att medlemmarna kan informeras i god tid."),
    ],
    "sources": [
        ("Stockholms stad – Riksintressen i översiktsplanen (Röda Bergen, Motorn och Vingen)", RIKS),
        ("Stockholms stad – Områdesfakta Västra Matteus (2025)", OF + "inre-staden/norra-innerstaden/vastra-matteus.pdf"),
        ("Stockholms stad – Områdesfakta Gustav Vasa (2025)", OF + "inre-staden/norra-innerstaden/gustav-vasa.pdf"),
        ("Stockholms stad – Fasadändring", BL_FASAD),
        ("Stockholms stad – Flerbostadshus", BL_FLERBO),
        ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", BL_KLASS),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ],
    "img": [
        ("Bostadshus med gavlar mot gatan längs en trädkantad gata",
         "Swedish 1920s apartment buildings following a hilly curved street, warm red and ochre rendered facades, "
         "steep roofs with decorative gables facing the street, planted front areas, Stockholm, early autumn light"
         + NO_PEOPLE + ", no cars"),
        ("Gavel med nya plåtbeslag mot ett plåttak",
         "close view of a decorative stepped gable on a 1920s Stockholm apartment building with neat new metal "
         "flashings along the gable top and a dark metal roof behind, clear blue sky" + NO_PEOPLE),
        ("Plåttak med takfönster och skorstenar i stenstaden",
         "steep dark grey standing-seam metal roof on an 1890s Stockholm stone apartment building with small roof "
         "windows, rendered chimneys and roof safety rails, other roofs in the background, daylight" + NO_PEOPLE),
    ],
}

# ---------------------------------------------------------------- ÖSTERMALM
TRP29B["Östermalm"] = {
    "title": "Takrenovering på Östermalm – stenstad, villor och funkis",
    "description": "Takrenovering på Östermalm: plåttak i stenstaden, tegelvillorna i Lärkstaden och "
                   "Diplomatstaden, Gärdesstadens funkishus och bygglov för föreningar.",
    "lead": "Östermalm är till största delen stenstad med föreningar som äger taken. Men här finns också "
            "Lärkstaden och Diplomatstaden med tegelhus från 1910- och 1920-talen och Gärdesstaden från "
            "funktionalismens genombrott. En takrenovering på Östermalm ser därför olika ut beroende på i vilken "
            "av de miljöerna huset ligger – och vem som äger det.",
    "card": "Stenstad, Lärkstaden, Diplomatstaden och Gärdet.",
    "trust": TRUST_BRF,
    "sections": [
        {"id": "hus", "h2": "Föreningar och några få villor",
         "paras": [
             "Stadens statistik för 2024 visar 7 344 bostäder i Hedvig Eleonora, en av Östermalms "
             "statistikområden. 5 164 av dem är bostadsrätter och bara 11 ligger i småhus. Så ser det ut i stora "
             "delar av Östermalm: taket ägs av en förening.",
             "Stenstaden på Östermalm uppfördes till största delen under 1800-talets senare del. Tillsammans med "
             "Norrmalm bildar den stadens största samlade årsring och grunden för stadens siluett."],
         "aside": {"title": "Hedvig Eleonora (2024)",
                   "items": ["7 344 bostäder", "5 164 bostadsrätter", "11 bostäder i småhus"]}},
        {"id": "lark", "h2": "Lärkstaden – tegelhus på en oregelbunden plan",
         "paras": [
             "Lärkstaden byggdes 1909–1918 och är ett tidigt exempel på en stadsplan anpassad till terrängen. Staden "
             "beskriver den småskaliga arkitekturen, mängden tegelhus och de planterade förgårdarna som en känsla "
             "av idyllisk, engelsk villastad.",
             "Större delen av Lärkstaden omfattas av en detaljplan från 1952 som reglerar byggrätten. Staden har "
             "skrivit att den vid behov kan komplettera med skyddsbestämmelser. Vid en takrenovering här är det "
             "därför klokt att behålla material, takform och detaljer precis som de är."]},
        {"id": "diplomat", "h2": "Diplomatstaden – villor runt Engelska kyrkan",
         "paras": [
             "Diplomatstaden byggdes på 1910- och 1920-talen med stora enfamiljshus runt Engelska kyrkan, avsedda för "
             "utländska beskickningars residens. Husen är av tegel med ett enhetligt formspråk och stor omsorg om "
             "utformningen. I stadens beskrivning av villaområdena nämns villor i nationalromantisk stil och stor omsorg i "
             "materialbehandlingen som värdebärande.",
             "Området skyddas genom miljöbalkens bestämmelser om nationalstadspark. Ett tak här renoveras med "
             "samma material och detaljer, och alla ändringar stäms av med staden innan arbetet börjar."],
         "aside": {"title": "Villorna på Östermalm",
                   "items": ["Lärkstaden 1909–1918", "Diplomatstaden 1910–20-tal",
                             "Tegel och enhetligt formspråk", "Diplomatstaden: nationalstadspark"]}},
        {"id": "gardet", "h2": "Gärdesstaden och stenstadens plåttak",
         "paras": [
             "Gärdesstaden byggdes 1932–37 på ömse sidor om Tessinparken och är en av Sveriges mest kända miljöer "
             "från funktionalismens genombrottstid. Även den skyddas som en del av nationalstadsparken.",
             "I stenstaden beskriver staden taken som sluttande, oftast plåttäckta och med en lutning på upp till "
             "45 grader. Där handlar renoveringen oftast om ommålning, tätning av falsar och nya beslag runt "
             "skorstenar och huvar. Läs mer om "
             '<a class="text-link" href="plattak.html">plåttak</a>.']},
        {"id": "lov", "h2": "Bygglov för föreningar",
         "paras": [
             "För flerbostadshus krävs bygglov när kulör eller material på taket ändras på en sida som vetter mot "
             "allmän plats. Är huset eller området särskilt kulturhistoriskt värdefullt gäller utökad lovplikt även "
             "för sådant som annars är lovfritt.",
             f'<a class="text-link" href="{BL_KLASS}" rel="noopener">Stadsmuseets klassificeringskarta</a> '
             "ger en första indikation. Behövs bygglov tar vi fram takplan och material- och kulörbeskrivning till "
             "föreningens ansökan."]},
    ],
    "steps": [
        ("Besök", "Gratis besök på taket och vinden med styrelsen eller ägaren."),
        ("Miljö och klassning", "Vi tittar på områdets skydd och Stadsmuseets karta."),
        ("Förslag", "Skriftligt kostnadsförslag med foton och prioriteringar."),
        ("Lov", "Takplan och kulörbeskrivning om något ändras mot gatan."),
        ("Utförande", "Plåt, tegel eller tätskikt med samma material som förut."),
        ("Dokumentation", "Foton och beskrivning till underhållsplanen."),
    ],
    "rot": _rot_brf("på Östermalm", "Villorna i Lärkstaden och Diplomatstaden är få."),
    "price": [
        "Kostnaden för en takrenovering på Östermalm påverkas av takets yta och lutning, om det är plåt, tegel "
        "eller papp, antalet skorstenar, kupor och takfönster, ställning mot gatan och om bygglov behövs. Läs mer om "
        '<a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a>.'],
    "faq": [
        ("Vår villa ligger i Lärkstaden – vad måste vi tänka på när taket läggs om?",
         "Lärkstaden har stora kulturvärden enligt staden. Behåll material, takform och detaljer, och kontrollera "
         "detaljplanen och Stadsmuseets karta innan något ändras."),
        ("Gäller särskilda regler i Diplomatstaden?",
         "Ja, området skyddas genom miljöbalkens bestämmelser om nationalstadspark. Stäm av med staden innan du "
         "ändrar något på huset."),
        ("Behöver vår förening på Östermalm bygglov för att måla om taket?",
         "Inte i samma kulör. Ändras kulör eller material på en sida som vetter mot allmän plats krävs bygglov för "
         "ett flerbostadshus."),
        ("Får vi rotavdrag när föreningen renoverar taket?",
         "Nej. Taket är föreningens ansvar, och rotavdraget i en bostadsrätt gäller arbete inne i lägenheten som "
         "du själv ansvarar för."),
    ],
    "sources": [
        ("Stockholms stad – Riksintressen i översiktsplanen (Lärkstaden, Diplomatstaden, Gärdesstaden)", RIKS),
        ("Stockholms stad – Områdesfakta Hedvig Eleonora (2025)", OF + "inre-staden/norra-innerstaden/hedvig-eleonora.pdf"),
        ("Stockholms stad – Fasadändring", BL_FASAD),
        ("Stockholms stad – Flerbostadshus", BL_FLERBO),
        ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", BL_KLASS),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ],
    "img": [
        ("Stenstadshus med branta plåttak och takkupor",
         "grand Stockholm 1890s stone apartment buildings with richly decorated rendered facades, steep black "
         "standing-seam metal roofs with copper-green dormers and chimneys, a wide tree-lined boulevard, morning "
         "light" + NO_PEOPLE + ", no cars"),
        ("Villa i tegel med brant tak och planterad förgård",
         "Swedish national romantic villa from about 1915 built in dark red brick with a steep red clay tile roof, "
         "tall chimneys and small dormers, a planted front garden behind a low wall, irregular hilly street, "
         "summer" + NO_PEOPLE),
        ("Ljusa bostadshus med platta tak på en bergig höjd",
         "Swedish 1930s functionalist apartment blocks with light rendered facades and flat roofs, placed "
         "dramatically on rocky terrain with lawns and trees, Stockholm, clear day" + NO_PEOPLE + ", no cars"),
    ],
}
