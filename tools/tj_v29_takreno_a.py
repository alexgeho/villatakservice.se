# -*- coding: utf-8 -*-
"""Takrenovering i Farsta, Hägersten, Kista, Skärholmen, Sundbyberg och Vällingby (v29, 2026-10-27).
Samma schema som TRP i tools/takreno_orter.py (sections, steps, rot, price, faq, sources, img).
Lokala fakta är kontrollerade mot källorna i "sources" (öppnade 2026-10-27).
Inga priser, garantier, recensioner, kundcase eller certifieringar."""

SKV_ROT = ("https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/"
           "safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
SKV_RATT = ("https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/"
            "gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
VARSAM = "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf"
OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
BL_FASAD = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/"
BL_KLASS = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/"
BOV_UTANLOV = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/andra-fasad-eller-tak/"
BOV_LAG = ("https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/"
           "fuktrisker-yttertak/takets-ytskikt/avvattning-laglutande-tak/")
BOV_YTSKIKT = ("https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/"
               "fuktrisker-yttertak/takets-ytskikt/")
SSM = "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/"
NO_PEOPLE = ", empty scene, no people, no hands, no text, no signs"


def _rot_smahus(extra=""):
    return [
        "Skatteverket räknar reparation och byte av takpannor, underlagspapp och hängrännor på ett småhus som "
        "rotarbete när du äger huset och bor i det eller har det som fritidshus. Avdraget är 30 procent av "
        "arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. "
        "Material och resor ger inget avdrag, enligt "
        f'<a class="text-link" href="{SKV_ROT}" rel="noopener">Skatteverket</a>.',
        "Geal drar avdraget direkt på fakturan. Är ni flera ägare har var och en sitt eget tak för avdraget. "
        + extra + 'Läs mer under <a class="text-link" href="rot-avdrag-takarbete.html">rotavdrag för takarbete</a>.',
    ]


TRP29A = {}

# ---------------------------------------------------------------- FARSTA
TRP29A["Farsta"] = {
    "title": "Takrenovering i Farsta – Tallkrogens tegel och villorna",
    "description": "Takrenovering i Farsta: omläggning av lertegel på småstugorna i Tallkrogen, "
                   "typritningarna från stadens småstugebyrå och äldre villor längs Magelungen.",
    "lead": "Farsta stadsdelsområde har drygt 4 700 småhus, och drygt 3 800 av dem ägs med äganderätt. "
            "En stor grupp är småstugorna i Tallkrogen med tak av rött lertegel, en annan är "
            "sekelskiftesvillorna och sommarnöjena längs Magelungen. En takrenovering i Farsta handlar "
            "därför oftast om att lägga om ett gammalt tegeltak på ny papp och läkt, inte om att byta material.",
    "card": "Tallkrogens småstugor och villorna vid Magelungen.",
    "sections": [
        {"id": "hus", "h2": "Tallkrogen byggdes av sina ägare",
         "paras": [
             "I början av 1920-talet tog Stockholm fram ett system där familjer med små inkomster kunde bygga "
             "sitt eget egnahem. Staden organiserade arbetet, ritade typhus och skrev utförliga byggbeskrivningar. "
             "De första stugorna stod klara 1927 i Pungpinan och Olovslund, och därefter följde bland annat "
             "Norra Ängby, Enskedefältet och Tallkrogen.",
             "Tallkrogen fick en egen plan. Gatorna lades ut i ellipser, som löparbanor på en idrottsarena, och "
             "husen i varje kvarter fick samma storlek, höjd och avstånd till gatan. Det är därför ett tak i "
             "Tallkrogen syns så tydligt: när en stuga får ett tak som avviker märks det längs hela gatan.",
             "Stadens statistik för 2024 visar 945 småhus i Tallkrogen. Nästan alla, 941 stycken, ägs med "
             "äganderätt. Det betyder att det är du som ägare, inte en förening, som bestämmer när taket ska "
             "renoveras och hur."],
         "aside": {"title": "Tallkrogen i stadens underlag",
                   "items": ["945 småhus, 941 med äganderätt (2024)",
                             "Kulturhistoriskt värdefull miljö enligt staden",
                             "Äldre miljöprogram för småstugeområdet",
                             "Typritningar från 1927–1957"]}},
        {"id": "ritningar", "h2": "Typritningarna visar hur taket såg ut",
         "paras": [
             "Småstugorna skulle vara billiga och lätta att bygga. Småstugebyrån gav därför ut kataloger med ett "
             "begränsat antal hustyper i ett, ett och ett halvt eller två plan. Husen var av trä med stående panel, "
             "och taken täcktes med enkupigt eller tvåkupigt rött lertegel. Stadens vägledning visar som exempel "
             "ett ett och ett halvplanshus med mansardtak klätt i tegel.",
             "I slutet av 1970-talet samlade Stadsbyggnadskontoret alla typritningar från 1927 till 1957 för att "
             "ge underlag till den som vill ändra sin stuga. För oss är ritningen ett bra stöd före en omläggning: "
             "den visar ursprunglig takvinkel, takfotens utsprång och var kuporna satt. Har taket fått en ny kupa "
             "eller ett annat utsprång genom åren ser vi det direkt."]},
        {"id": "tegel", "h2": "Teglet får ofta ligga kvar",
         "paras": [
             "Lertegel håller länge. Det som är slut på en stuga från 1930- eller 1940-talet är oftast det "
             "som ligger under: läkten, underlagspappen och plåten runt skorsten och kupor. En takrenovering i "
             "Tallkrogen börjar därför med att pannorna tas ner och sorteras. Hela pannor läggs åt sidan, spruckna "
             "byts ut.",
             "Sedan läggs ny papp och ny läkt, och de gamla pannorna kommer tillbaka upp. Räcker de inte till "
             "kompletterar vi med begagnade eller nya pannor av samma modell. På ett mansardtak läggs de nya "
             "pannorna gärna på den del som syns minst, så att gatufasaden behåller sitt gamla tegel.",
             "Stadens vägledning för småstugeområdena rekommenderar att karaktärsskapande material, kulörer och "
             "byggnadsdelar tas till vara eller återskapas vid renoveringar. Rött tegel på ett rött tegeltak "
             "är det enklaste sättet att följa den."],
         "aside": {"title": "Det vi brukar byta",
                   "items": ["Läkt och ströläkt", "Underlagspapp", "Beslag runt skorsten och kupor",
                             "Spruckna pannor och nockpannor"]}},
        {"id": "magelungen", "h2": "Villorna längs Magelungen",
         "paras": [
             "Farsta har också en äldre historia. Kring sekelskiftet 1900 lockade AB Södertörns villastad med frisk "
             "luft och natur, och när Nynäsbanan öppnade 1901 blev det lättare att ta sig till staden. Längs "
             "Magelungens strand ligger flera hus från den tiden, bland annat grosshandlare Elliots gulmålade villa "
             "från 1910 och sekelskiftesvillan Dagaborg. I backen ner mot sjön finns fler sommarnöjen, några med "
             "snickarglädje.",
             "Sådana hus har mer att hålla reda på än en småstuga: vindskivor med profiler, kupor, burspråk och "
             "ibland ett tak som byggts om i flera omgångar. Vid en omläggning mäter vi upp detaljerna innan de "
             "tas ner, så att nya vindskivor och plåtdetaljer får samma form som de gamla."]},
        {"id": "lov", "h2": "När behövs bygglov?",
         "paras": [
             "Lägger du om taket med samma material behövs inget lov. På ett en- eller tvåbostadshus behövs enligt "
             f'<a class="text-link" href="{BOV_UTANLOV}" rel="noopener">Boverket</a> i regel inte heller '
             "bygglov för att byta till ett annat taktäckningsmaterial, men ändringen ska vara varsam och "
             "anpassad till omgivningen.",
             "Undantaget är byggnader och områden som är särskilt kulturhistoriskt värdefulla. Där gäller "
             "utökad lovplikt, och då krävs bygglov även för sådant som annars är lovfritt. Staden räknar "
             "Tallkrogen som kulturhistoriskt värdefull miljö, och "
             f'<a class="text-link" href="{BL_KLASS}" rel="noopener">Stadsmuseets klassificeringskarta</a> '
             "ger en första bild av hur just ditt hus är klassat. Vill du byta material eller ändra takformen "
             "tittar vi på kartan och detaljplanen tillsammans innan något beställs."]},
    ],
    "steps": [
        ("Karta och ritning", "Vi kollar Stadsmuseets karta och tar gärna fram husets typritning."),
        ("Vinden", "Papp, läkt och ventilation kontrolleras inifrån."),
        ("Nedtagning", "Pannorna tas ner, sorteras och staplas på tomten."),
        ("Underlag", "Ny underlagspapp, ströläkt och bärläkt monteras."),
        ("Läggning", "Gamla pannor läggs tillbaka och kompletteras med samma modell."),
        ("Plåt", "Beslag kring skorsten och kupor görs om, rännor rensas."),
    ],
    "rot": _rot_smahus(),
    "price": [
        "Kostnaden i Farsta styrs av takets yta och lutning, om det är ett mansardtak, hur många pannor som "
        "går att återanvända, antalet kupor och hur mycket plåt som ska göras om. Läs mer om "
        '<a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a> eller räkna '
        'på ditt tak i <a class="text-link" href="kalkylator-takbyte.html">kalkylatorn för takbyte</a>.'],
    "faq": [
        ("Kan vi återanvända teglet på vår stuga i Tallkrogen?",
         "Ofta ja. Lertegel har lång livslängd, så vi plockar ner, sorterar och lägger tillbaka hela pannor på "
         "ny papp och läkt. Det som saknas kompletteras med pannor av samma modell."),
        ("Var hittar jag ritningen till min småstuga?",
         "Stadsbyggnadskontoret samlade typritningarna för småstugorna från 1927–1957 i slutet av 1970-talet. "
         "Har du inte husets ritning hjälper vi dig att ta reda på vilken typ huset är byggt efter."),
        ("Behöver jag bygglov för att lägga betongpannor i Tallkrogen?",
         "Det beror på husets klassning. Tallkrogen räknas som kulturhistoriskt värdefull miljö, och är huset "
         "särskilt värdefullt gäller utökad lovplikt. Kontrollera Stadsmuseets karta och detaljplanen först."),
        ("Vår villa vid Magelungen har snickarglädje på vindskivorna – byts den?",
         "Nej, inte om den går att laga. Vi mäter upp profilerna före omläggningen och tar ner, lagar och "
         "sätter tillbaka det som håller. Det som är ruttet görs nytt med samma form."),
    ],
    "sources": [
        ("Stockholms stad – Varsam utveckling av småhus- och villaområden", VARSAM),
        ("Stockholms stad – Områdesfakta Tallkrogen (2025)", OF + "soderort/farsta/tallkrogen.pdf"),
        ("Stockholms stad – Områdesfakta Farsta stadsdelsområde (2025)", OF + "soderort/farsta/farsta-stadsdelsomrade.pdf"),
        ("Stockholms stadsmuseum – Stockholms spår: Farsta strand", SSM + "SSM_DOK_000014.pdf"),
        ("Boverket – Ändra fasad eller tak", BOV_UTANLOV),
        ("Stockholms stad – Fasadändring", BL_FASAD),
        ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", BL_KLASS),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "img": [
        ("Småstuga i trä med mansardtak av rött lertegel längs en svängd gata",
         "small Swedish 1930s wooden cottage of one and a half storeys with vertical light grey-green board facade, "
         "a mansard roof covered with red single-roll clay tiles, a small brick chimney, a clipped hedge and fruit "
         "trees, part of a row of similar cottages along a gently curving suburban street, Tallkrogen Stockholm, "
         "late summer" + NO_PEOPLE),
        ("Nylagt svart pannat tak sett från nocken, grönska runt huset",
         "stack of old red clay roof tiles neatly sorted on a wooden pallet in a garden, next to bundles of new "
         "pale wooden roof battens and a roll of black roofing underlay, an older wooden cottage wall in soft focus "
         "behind, daylight" + NO_PEOPLE),
        ("Gul sekelskiftesvilla i trä med tegeltak bland lövträd vid en sjö",
         "yellow painted Swedish wooden villa from about 1910 with decorative white fretwork on the gables, a steep "
         "red clay tile roof with a small dormer, standing among tall deciduous trees on a slope above a calm lake "
         "shore, early autumn light" + NO_PEOPLE),
    ],
}

# ---------------------------------------------------------------- HÄGERSTEN
TRP29A["Hägersten"] = {
    "title": "Takrenovering i Hägersten – villor från tre epoker",
    "description": "Takrenovering i Hägersten: trävillor, funkishus och kataloghus i Mälarhöjden, villorna på "
                   "Hägerstensåsen och takformen när huset byggs till.",
    "lead": "I stadsdelen Hägersten finns knappt 1 000 småhus, och nästan alla ägs av de boende. I "
            "grannstadsdelen Mälarhöjden, längs Mälarstranden, står utsirade trävillor från 1800-talets andra hälft bredvid "
            "vita funkishus från 1930-talet och dagens kataloghus. En takrenovering i Hägersten börjar därför "
            "med frågan vilken epok huset tillhör – för det avgör vad som ska ligga på taket.",
    "card": "Mälarhöjden, Hägerstensåsen och tre epoker av villor.",
    "sections": [
        {"id": "hus", "h2": "Från sommarnöjen till villastad",
         "paras": [
             "Stranden mellan Klubbensborg och Lyran var länge en plats för sommarnöjen. Från mitten av 1800-talet "
             "tog sommargästerna ångbåten från staden, och flera av de stora, utsirade trävillorna står kvar. "
             "Villa Sagatun, ett landmärke för sjöfarande sedan 1881, kom monteringsfärdig från Ekmans snickeri.",
             "När Fridhems villastad fick spårvagn till staden 1913 blev det populärt att bo här året runt. "
             "Området planlades 1923 och fick 1926 namnet Mälarhöjden. Sedan dess har varje årtionde lagt till "
             "sina hus: strama vita funkisvillor från 1930-talet längs Pettersbergsvägen och kataloghus från "
             "senare tid.",
             "Stadens statistik för 2024 visar 994 småhus i stadsdelen Hägersten, varav 955 med äganderätt. "
             "Det är alltså oftast du som ägare som bestämmer över taket."],
         "aside": {"title": "Hägersten i siffror (2024)",
                   "items": ["994 småhus i stadsdelen", "955 av dem med äganderätt",
                             "Mälarhöjden: kulturhistoriskt värdefull miljö",
                             "Mälarhöjden: generösa byggrätter"]}},
        {"id": "epoker", "h2": "Tre tak som behöver olika renovering",
         "paras": [
             "En trävilla från 1800-talets slut kan ha ett brant tak med takfall åt flera håll, kupor och "
             "vindskivor med snickarglädje. Här är det detaljerna som tar tid: varje kupa behöver nya beslag, "
             "och vindskivorna ska helst lagas och sitta kvar.",
             "Ett funkishus från 1930-talet kan ha ett låglutande eller nästan platt tak med plåt eller papp. "
             "Där handlar renoveringen om tätskiktet, skarvarna och hur vattnet leds bort, eftersom Boverket "
             "skriver att låglutande tak belastas mer av nederbörd.",
             "Ett kataloghus från 1970- eller 1980-talet kan ha betongpannor. Pannorna kan vara hela medan "
             "papp och läkt under är slut, och då räcker det ofta med en omläggning."]},
        {"id": "asen", "h2": "Hägerstensåsen – villorna på den norra delen",
         "paras": [
             "Före 1938 var Hägerstensåsen en skogsklädd bergsrygg. När området byggdes ut blev det mest trevånings "
             "smalhus på stadens mark, men på den norra delen byggdes även punkthus och villor. De första husen "
             "var klara 1939 och de sista 1948.",
             "Åsen ligger högt, och på ett hus i ett utsatt läge tittar vi vid en omläggning "
             "särskilt på nock, vindskivor och infästningen av pannorna i takfoten, eftersom det är där vinden "
             "tar tag först."]},
        {"id": "tillbyggnad", "h2": "Renovera taket eller bygga på?",
         "paras": [
             "Mälarhöjden har enligt stadens vägledning generösa byggrätter, och många villor har byggts till. "
             "Står en tillbyggnad på tur är det klokt att planera taket samtidigt: det är dyrt att lägga om ett "
             "tak som rivs några år senare.",
             "Stadens vägledning för villastäderna räknar volym, proportioner och takform till det som har stor "
             "påverkan på områdets karaktär – både för huvudbyggnaden och för till- och komplementbyggnader. Det gäller "
             "också ett nytt tak: samma lutning och samma typ av material som grannhusen gör att huset fortsätter "
             "att höra till gatan. Läs mer om tillbyggnader i vår guide om "
             '<a class="text-link" href="tillbyggnad.html">tillbyggnad</a>.']},
        {"id": "lov", "h2": "Klassning och bygglov",
         "paras": [
             "Staden räknar Mälarhöjden som en kulturhistoriskt värdefull miljö. Ligger ditt hus i ett område eller "
             "är en byggnad som är särskilt värdefull gäller utökad lovplikt, och då behövs bygglov även för att "
             "byta takmaterial. "
             f'<a class="text-link" href="{BL_KLASS}" rel="noopener">Stadsmuseets klassificeringskarta</a> ger en '
             "första indikation, men ibland behöver Stadsmuseet göra en bedömning.",
             "Lägger du om taket med samma material krävs inget lov. Ändringen ska ändå göras varsamt, så att "
             "husets särdrag tas till vara."]},
    ],
    "steps": [
        ("Epok och klassning", "Vi tittar på husets ålder, Stadsmuseets karta och eventuella tillbyggnadsplaner."),
        ("Vinden", "Papp, läkt, råspont och ventilation kontrolleras inifrån."),
        ("Förslag", "Omläggning, nytt tätskikt eller nytt material – beskrivet med foton."),
        ("Nedtagning", "Pannor eller plåt tas ner och detaljer mäts upp."),
        ("Nytt underlag", "Papp och läkt, eller nytt tätskikt på låglutande tak."),
        ("Detaljer", "Kupor, vindskivor, nock och rännor görs klart."),
    ],
    "rot": _rot_smahus(),
    "price": [
        "Kostnaden i Hägersten påverkas av takets form och lutning, antalet kupor och takfall, om det är plåt, "
        "papp, tegel eller betong, hur mycket underlag som behöver bytas och om en tillbyggnad ska anslutas. Läs "
        'mer om <a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a>.'],
    "faq": [
        ("Vårt funkishus i Mälarhöjden har ett nästan platt tak – kan det läggas om med pannor?",
         "Pannor kräver en viss lutning, och ett funkistak är byggt för plåt eller papp. Vi renoverar det därför "
         "med nytt tätskikt eller ny plåt. Att ändra takformen påverkar husets karaktär och kan kräva bygglov."),
        ("Ska vi renovera taket nu eller vänta tills vi byggt på?",
         "Om tillbyggnaden ligger nära i tid är det oftast bäst att göra båda samtidigt, så att det nya och gamla "
         "taket får samma underlag och material. Annars kan vi laga det som läcker och vänta med resten."),
        ("Är vår trävilla från 1890-talet skyddad?",
         "Det framgår av Stadsmuseets klassificeringskarta och detaljplanen. Mälarhöjden som helhet räknas som "
         "kulturhistoriskt värdefull miljö, men klassningen av varje hus ser du på kartan."),
        ("Varför blåser det in under pannorna på vår villa på Hägerstensåsen?",
         "Ofta sitter pannorna vid nock och takfot för löst, eller så har underlagspappen gått sönder. Vi tittar "
         "inifrån vinden och på taket och åtgärdar infästningen när taket läggs om."),
    ],
    "sources": [
        ("Stockholms stadsmuseum – Stockholms spår: Mälarhöjden", SSM + "SSM_DOK_000069.pdf"),
        ("Stockholms stadsmuseum – Stockholms spår: Hägerstensåsen", SSM + "SSM_DOK_000088.pdf"),
        ("Stockholms stad – Varsam utveckling av småhus- och villaområden", VARSAM),
        ("Stockholms stad – Områdesfakta Hägersten (2025)", OF + "soderort/hagersten/hagersten.pdf"),
        ("Boverket – Risker med avvattning från låglutande tak", BOV_LAG),
        ("Stockholms stad – Fasadändring", BL_FASAD),
        ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", BL_KLASS),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "img": [
        ("Trävilla med snickarglädje och brant tegeltak i en sluttning ovanför sjön",
         "modest two-storey Swedish wooden villa from about 1890 with light yellow horizontal panel, white "
         "fretwork on the gable and a small glazed veranda, steep red clay tile roof with one dormer, set among "
         "pine trees on a slope above a lake, Stockholm suburb, summer" + NO_PEOPLE),
        ("Svarta betongpannor längs takfoten med hängränna",
         "white rendered Swedish functionalist villa from the 1930s with a low-pitched standing-seam metal roof and "
         "a thin roof edge, horizontal windows, pine trees and rocks around, clear daylight" + NO_PEOPLE),
        ("Takkupa med nya plåtbeslag på ett tegeltak",
         "close view of a small dormer on an older red clay tile roof with new grey metal flashings around the "
         "dormer cheeks and front, neat tile cuts, wooden window frame painted white, soft daylight" + NO_PEOPLE),
    ],
}

# ---------------------------------------------------------------- KISTA
TRP29A["Kista"] = {
    "title": "Takrenovering i Kista – tätskikt på låga tak",
    "description": "Takrenovering i Kista: nytt tätskikt på platta och låglutande tak från 1975–80, takbrunnar, "
                   "bräddavlopp och radhus i förening.",
    "lead": "Kista byggdes ut på bara fem år, 1975–1980, och fick både flerbostadshus och omkring 780 småhus. "
            "I dag finns knappt 1 000 småhus i stadsdelen. Många har platta eller låglutande tak, och på dem "
            "är det tätskiktet och avvattningen som avgör hur länge taket håller. En takrenovering i Kista "
            "handlar därför oftare om papp, duk och brunnar än om pannor.",
    "card": "Låga tak, tätskikt och takbrunnar från 1970-talet.",
    "sections": [
        {"id": "hus", "h2": "En stadsdel med friare former",
         "paras": [
             "Stockholms stad köpte marken på Järvafältet 1966, och mellan 1975 och 1980 byggdes Kista ut. Enligt "
             "Stadsmuseet tillämpade staden här betydligt friare former för arkitekturen än i de andra "
             "stadsdelarna på Järvafältet. Bebyggelsen fick 2 500 lägenheter i flerbostadshus och omkring 780 "
             "småhus.",
             "Stadens statistik för 2024 visar 971 småhus i Kista. 482 ägs med äganderätt och 404 är "
             "bostadsrätter. Husen är alltså nästan 50 år gamla, och många tak har nått den ålder då tätskiktet "
             "behöver bytas för första eller andra gången."],
         "aside": {"title": "Kistas småhus (2024)",
                   "items": ["971 småhus", "482 med äganderätt", "404 bostadsrätter",
                             "Byggda 1975–1980"]}},
        {"id": "tatskikt", "h2": "Tätskiktet gör jobbet på ett lågt tak",
         "paras": [
             "På ett brant tegeltak rinner vattnet av innan det hinner göra skada. På ett platt eller låglutande "
             "tak blir det kvar längre, och Boverket skriver att låglutande tak belastas mer av nederbörd. Då "
             "är tätskiktet – papp eller duk – det enda som skiljer regnvattnet från takkonstruktionen.",
             "Enligt Boverket läcker vatten oftast in vid genomföringar, skarvar, ränndalar och infästningar. Det "
             "är också där vi börjar när vi besiktar ett lågt tak i Kista: runt ventilationshuvar, skorstenar, "
             "takfönster och anslutningen mot fasaden."]},
        {"id": "brunnar", "h2": "Brunnar, silar och bräddavlopp",
         "paras": [
             "Större låglutande tak har ofta brunnar i ränndalarna som leder vattnet till invändiga stuprör. Boverket "
             "varnar för att silarna på brunnarna kan sättas igen av löv och mossa. Då blir vattnet stående, kan "
             "frysa och skada tätskiktet – och i värsta fall rinna in vid låga trösklar.",
             "Därför ska ett sådant tak ha ett bräddavlopp som leder bort vattnet om brunnarna sätter igen. Vid en "
             "renovering kontrollerar vi att det finns, att det sitter lägre än trösklar och krön och att det "
             "klarar ett skyfall. Saknas det föreslår vi var det kan placeras."],
         "aside": {"title": "Det vi kontrollerar på låga tak",
                   "items": ["Skarvar och genomföringar", "Silar och brunnar", "Bräddavlopp",
                             "Anslutning mot fasad och takfot"]}},
        {"id": "forening", "h2": "Äganderätt eller förening?",
         "paras": [
             "Äger du ditt radhus beställer du själv. I de radhusområden där husen är bostadsrätter är det "
             "föreningens stadgar som avgör vem som ansvarar för taket. Ligger ansvaret på föreningen är det "
             "styrelsen som beställer, och då brukar det vara klokt att göra hela längan på en gång.",
             "Även med äganderätt kan grannarna vara berörda, eftersom radhus har sammanbyggda tak. Vi visar "
             "hur skarven mot grannens tak löses innan arbetet börjar, så att det nya och det gamla tätskiktet "
             "möts på ett säkert sätt."]},
        {"id": "renovera", "h2": "Laga, lägga på nytt eller bygga om?",
         "paras": [
             "Är det gamla tätskiktet torrt och fast kan ett nytt ofta läggas ovanpå. Har fukt kommit in under "
             "behöver det gamla rivas så att underlaget kan torka eller bytas. Vi tar därför prov på flera ställen "
             "innan vi föreslår en metod.",
             "Radhusen i en länga är byggda lika. Ändrar du takets material eller färg på ett av dem "
             "påverkar det helheten, så vi föreslår samma utförande om du inte uttryckligen vill något annat. "
             "Läs mer om hur vi arbetar med "
             '<a class="text-link" href="plattak.html">plåttak</a> och '
             '<a class="text-link" href="takbesiktning.html">takbesiktning</a>.']},
    ],
    "steps": [
        ("Besiktning", "Vi går upp på taket och kontrollerar skarvar, genomföringar och brunnar."),
        ("Prov", "Vi undersöker om underlaget är torrt innan metoden väljs."),
        ("Förslag", "Lagning, nytt tätskikt ovanpå eller rivning – beskrivet med foton."),
        ("Grannar och förening", "Skarven mot grannens tak och vem som beställer klaras ut."),
        ("Utförande", "Nytt tätskikt, nya brunnar och bräddavlopp vid behov."),
        ("Kontroll", "Avrinningen testas och allt dokumenteras."),
    ],
    "rot": _rot_smahus("Är radhuset en bostadsrätt och taket föreningens ansvar ger arbetet inget rotavdrag för dig "
                       "som medlem. "),
    "price": [
        "Kostnaden i Kista påverkas av takets yta, om det gamla tätskiktet kan ligga kvar, antalet genomföringar och "
        "brunnar, om bräddavlopp saknas och om flera hus görs samtidigt. Läs mer om "
        '<a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a>.'],
    "faq": [
        ("Kan nytt tätskikt läggas ovanpå det gamla på vårt radhus i Kista?",
         "Ja, om det gamla är torrt och sitter fast. Har fukt kommit in under måste det rivas. Vi tar prov på "
         "flera ställen innan vi föreslår en metod."),
        ("Behöver ett platt radhustak i Kista ett bräddavlopp?",
         "Det är en utloppsväg som leder bort vattnet om takbrunnarna sätter igen. Boverket skriver att låglutande "
         "tak med brunnar behöver en sådan överfyllnadsfunktion."),
        ("Vem betalar taket i vår bostadsrättsförening med radhus?",
         "Det står i föreningens stadgar. Ansvarar föreningen för taket är det styrelsen som beställer och "
         "betalar, och då ger arbetet inget rotavdrag för medlemmarna."),
        ("Hur ofta ska brunnarna på taket rensas?",
         "Minst en gång om året, gärna efter lövfällningen. Silar som sätts igen av löv och mossa är en vanlig "
         "orsak till stående vatten på låga tak."),
    ],
    "sources": [
        ("Stockholms stadsmuseum – Stockholms spår: Kista", SSM + "SSM_DOK_000080.pdf"),
        ("Stockholms stad – Områdesfakta Kista (2025)", OF + "vasterort/jarva/kista.pdf"),
        ("Boverket – Risker med avvattning från låglutande tak", BOV_LAG),
        ("Boverket – Fuktrisker med takets ytskikt", BOV_YTSKIKT),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "img": [
        ("Radhus från 1970-talet med låglutande tak och träfasader",
         "row of simple one-storey Swedish terraced houses from the late 1970s with almost flat roofs and a thin "
         "dark roof edge, vertical brown stained wooden facades, small fenced front yards, a car-free paved "
         "footpath with young trees, Scandinavian suburb, overcast summer day" + NO_PEOPLE),
        ("Takbrunn med sil på ett platt tak med papptäckning",
         "close view of a roof drain with a round metal leaf guard on a flat roof covered with dark bitumen roofing "
         "felt, a few leaves nearby, a small overflow outlet at the roof edge in the background, daylight" + NO_PEOPLE),
        ("Ventilationshuv och nya anslutningar på ett låglutande tak",
         "close view of new dark bitumen roofing membrane with neat welded seams around a metal ventilation hood on "
         "a low-sloped roof, clean edges, clear sky" + NO_PEOPLE),
    ],
}

# ---------------------------------------------------------------- SKÄRHOLMEN
TRP29A["Skärholmen"] = {
    "title": "Takrenovering i Skärholmen – radhusen i husgrupperna",
    "description": "Takrenovering i Skärholmen: radhus och kedjehus från 1960- och 70-talen i Bredäng, "
                   "Sätra och Vårberg och låga tak i husgrupper.",
    "lead": "Skärholmens stadsdelsområde har knappt 2 000 småhus, och nästan alla ägs av de boende. De flesta är "
            "radhus och kedjehus byggda i grupper under 1960- och 1970-talen i Bredäng, Sätra och Vårberg. "
            "Husen i en grupp är lika varandra, och taket är en del av den likheten. En takrenovering i "
            "Skärholmen handlar därför både om det egna taket och om hur det passar in i längan.",
    "card": "Radhus i grupper i Bredäng, Sätra och Vårberg.",
    "sections": [
        {"id": "hus", "h2": "Småhusen i den storskaliga stadsdelen",
         "paras": [
             "I början av 1960-talet köpte staden stora markområden i sydvästra Stockholm. Bredäng var den första "
             "stadsdelen som planerades i stor skala och började byggas 1962, följd av Sätra. Byggandet blev alltmer "
             "industriellt, och en stor del av miljonprogrammets bebyggelse blev gruppbyggda småhus och radhus.",
             "Stadens statistik för 2024 visar 1 991 småhus i Skärholmens stadsdelsområde, varav 1 976 med "
             "äganderätt. I Vårberg finns 580 småhus och i Sätra 538. Nästan alla ägs alltså av dem som bor där."],
         "aside": {"title": "Skärholmens småhus (2024)",
                   "items": ["1 991 småhus i stadsdelsområdet", "1 976 med äganderätt",
                             "Vårberg 580, Sätra 538, Bredäng 322",
                             "Bredäng: kulturhistoriskt värdefull miljö"]}},
        {"id": "grupper", "h2": "Taket är en del av husgruppen",
         "paras": [
             "Stadens vägledning beskriver småhusen i de storskaliga stadsdelarna som strikt grupperade, med enkel och "
             "stram gestaltning. Fasaderna kunde blanda tegel, trä och skivor, men inom varje husgrupp var "
             "enhetligheten mycket stor och färgsättningen noga komponerad. Taken var ofta platta eller svagt "
             "lutande pulpettak.",
             "Det får betydelse när ett tak ska renoveras. Ett radhus som får ett annat taktäckningsmaterial eller "
             "en annan kulör än grannarna bryter mönstret längs hela längan. Vi föreslår därför samma utförande som "
             "grannhusen om du inte har bestämt dig för något annat – och då pratar vi gärna med grannarna först."]},
        {"id": "lag", "h2": "Låga tak tål mindre slarv",
         "paras": [
             "Ett pulpettak med svag lutning leder bort vattnet långsammare än ett brant sadeltak. Boverket skriver "
             "att låglutande tak belastas mer av nederbörd, och att vatten oftast läcker in vid skarvar, "
             "genomföringar, ränndalar och infästningar.",
             "På radhusen i Skärholmen är det därför ofta anslutningarna som är slut: där taket möter grannens tak, "
             "där det möter den högre fasaden och runt ventilationen. En renovering kan vara allt från att göra om "
             "de anslutningarna till att lägga ett helt nytt tätskikt."],
         "aside": {"title": "Vanliga läckställen",
                   "items": ["Skarven mot grannens tak", "Anslutningen mot högre fasad",
                             "Ventilationshuvar", "Takfot och hängränna"]}},
        {"id": "langan", "h2": "Ett hus i taget eller hela längan?",
         "paras": [
             "Eftersom husen äger var sitt tak kan varje ägare renovera när det passar. Ofta är det ändå smart att "
             "flera grannar gör det samtidigt: ställning, container och etablering delas, och skarvarna mellan "
             "husen blir nya på en gång.",
             "Gör bara ett hus behöver vi ansluta det nya taket till grannens gamla på ett sätt som håller. Vi "
             "dokumenterar skarven med foton, så att både du och grannen vet hur den är gjord."]},
        {"id": "bredang", "h2": "Bredäng – värdefull miljö",
         "paras": [
             "Staden räknar Bredäng som en kulturhistoriskt värdefull miljö. Stadens vägledning säger att "
             "förändringar i sådana områden ska visa hänsyn till helheten, och att karaktärsskapande material och "
             "kulörer ska tas till vara när husen renoveras.",
             "Att lägga om taket med samma material kräver inget lov. Är ditt hus eller område klassat som särskilt "
             "kulturhistoriskt värdefullt gäller dock utökad lovplikt för materialbyten. Titta på "
             f'<a class="text-link" href="{BL_KLASS}" rel="noopener">Stadsmuseets klassificeringskarta</a> '
             "innan du bestämmer dig för något nytt."]},
    ],
    "steps": [
        ("Besiktning", "Vi kontrollerar tätskikt, skarvar och anslutningar mot grannar och fasad."),
        ("Grannar", "Vi visar hur skarven löses och om flera hus kan göras samtidigt."),
        ("Förslag", "Samma utförande som husgruppen, beskrivet med foton."),
        ("Etablering", "Ställning och container planeras på den smala tomten."),
        ("Utförande", "Nytt tätskikt eller ny täckning, nya anslutningar."),
        ("Dokumentation", "Foton av skarvarna till dig och grannen."),
    ],
    "rot": _rot_smahus(),
    "price": [
        "Kostnaden i Skärholmen påverkas av takets yta, om det är ett pulpettak eller sadeltak, hur många "
        "anslutningar mot grannar och fasad som ska göras om och om flera hus görs samtidigt. Läs mer om "
        '<a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a>.'],
    "faq": [
        ("Måste hela radhuslängan i Sätra renoveras samtidigt?",
         "Nej, varje ägare kan renovera sitt tak. Det blir ofta billigare och skarvarna bättre om flera grannar "
         "gör det samtidigt, men det är inget krav."),
        ("Får vi välja en annan färg på taket än grannarna i Vårberg?",
         "Ett tak med annan kulör bryter husgruppens enhetliga karaktär. Ligger huset i ett område som är "
         "särskilt kulturhistoriskt värdefullt kan bygglov krävas. Vi rekommenderar samma utförande som grannarna."),
        ("Var läcker radhustak oftast?",
         "Vid skarvar, genomföringar och anslutningar – till exempel där taket möter grannens tak eller en högre "
         "fasad. Det är också där vi börjar besiktningen."),
        ("Är Bredäng skyddat?",
         "Staden räknar Bredäng som kulturhistoriskt värdefull miljö. Vad som gäller för ditt hus ser du på "
         "Stadsmuseets klassificeringskarta och i detaljplanen."),
    ],
    "sources": [
        ("Stockholms stad – Varsam utveckling av småhus- och villaområden", VARSAM),
        ("Stockholms stad – Områdesfakta Skärholmens stadsdelsområde (2025)",
         OF + "soderort/skarholmen/skarholmen-stadsdelsomrade.pdf"),
        ("Stockholms stad – Områdesfakta Vårberg (2025)", OF + "soderort/skarholmen/varberg.pdf"),
        ("Stockholms stad – Områdesfakta Sätra (2025)", OF + "soderort/skarholmen/satra.pdf"),
        ("Stockholms stad – Områdesfakta Bredäng (2025)", OF + "soderort/skarholmen/bredang.pdf"),
        ("Boverket – Fuktrisker med takets ytskikt", BOV_YTSKIKT),
        ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", BL_KLASS),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "img": [
        ("Radhuslänga från 1960-talet med låglutande tak och tegelfasad",
         "long row of Swedish 1960s terraced houses with low-pitched roofs, red brick lower facades and dark "
         "stained wooden panels above, identical small front gardens with hedges, a footpath with lawn and birch "
         "trees, south-western Stockholm suburb, summer" + NO_PEOPLE),
        ("Skarv mellan två radhustak med nya och gamla takpannor",
         "close view of the joint between two terraced house roofs, one side with new black roofing felt and one "
         "side with older weathered felt, a neat metal capping over the joint, low-sloped roof, daylight" + NO_PEOPLE),
        ("Småhus i trä med likadana sadeltak",
         "group of Swedish 1970s link-detached houses with identical shallow gable roofs in dark concrete tiles, "
         "uniform light wooden facades and carports between the houses, trees in the background, overcast light"
         + NO_PEOPLE + ", no cars"),
    ],
}

# ---------------------------------------------------------------- SUNDBYBERG
TRP29A["Sundbyberg"] = {
    "title": "Takrenovering i Sundbyberg – Duvbos tegel och taktassar",
    "description": "Takrenovering i Sundbyberg: rött lertegel och synliga taktassar på Duvbos villor från "
                   "tre epoker och utökad lovplikt för takmaterial.",
    "lead": "I Duvbo i Sundbyberg ligger villor från sekelskiftet 1900, 1920-talet och 1930–40-talen. "
            "Kommunens miljöprogram beskriver vilket tak som hör till varje epok, och oftast är svaret "
            "rött lertegel med synliga taktassar. En takrenovering i Sundbyberg handlar därför om att lägga om "
            "taket utan att tappa de detaljer som gör husen till Duvbohus.",
    "card": "Rött lertegel och synliga taktassar i Duvbo.",
    "sections": [
        {"id": "hus", "h2": "Ett av de första egnahemsområdena",
         "paras": [
             "Riksantikvarieämbetet pekade 1987 ut Duvbo som riksintresse för kulturmiljövården. Motiveringen var att "
             "Duvbo är ett av de första exemplen på en välorganiserad egnahemsförstad i Stockholmstrakten.",
             "Husen är framför allt byggda kring sekelskiftet 1900 och under 1920-talet. Sekelskiftesvillorna byggdes "
             "ofta av ägarna själva och visar en rik provkarta på tidens smak. Senare, på 1930- och 1940-talen, "
             "tillkom enkla slätputsade hus i ljusa kulörer.",
             "Kommunen skriver att det inte i första hand är de enskilda husen som är värdefulla, utan området som "
             "helhet. Ett tak som avviker påverkar alltså mer än det egna huset."]},
        {"id": "epoker", "h2": "Tre epoker, nästan samma tak",
         "paras": [
             "Miljöprogrammet för Duvbo har en tabell över material och utförande för varje epok. Sekelskiftesvillan "
             "i schweizerstil hade rött lertegel, falsad slätplåt eller ibland papp, och synliga kontursågade "
             "taktassar. Taken var ofta oregelbundna och hade ibland torn och kupoler.",
             "1920-talsvillan fick enkla eller brutna sadeltak med rött lertegel och synliga taktassar. Husen från "
             "1930- och 40-talen fick flacka tak, även de täckta med rött lertegel och med synliga taktassar."],
         "aside": {"title": "Duvbos tak enligt miljöprogrammet",
                   "items": ["Sekelskifte: rött tegel, falsad plåt, ev. papp",
                             "1920-tal: rött lertegel",
                             "1930–40-tal: flacka tak med rött tegel",
                             "Alla epoker: synliga taktassar"]}},
        {"id": "taktassar", "h2": "Taktassarna ska synas",
         "paras": [
             "Taktassar är de utstickande ändarna av takstolarna under takfoten. På sekelskiftesvillorna är de "
             "kontursågade – utskurna i en dekorativ form. När ett tak läggs om är det lätt att de byggs in bakom en "
             "ny takfotsbräda eller sågas av för att det går snabbare.",
             "Vi gör tvärtom. Taktassarna mäts upp och fotograferas innan arbetet börjar. De som är ruttna i änden "
             "skarvas eller ersätts med nya i samma form, och takfoten byggs så att de syns som förut. Samma gäller "
             "vindskivor och lister med profiler."]},
        {"id": "lov", "h2": "Utökad lovplikt i Duvbo",
         "paras": [
             "I samband med en planändring utökades bygglovsplikten i Duvbo. Den omfattar bland annat utbyte av "
             "takläggningsmaterial, och enligt miljöprogrammet är åtgärder inom den utökade lovplikten kostnadsfria.",
             "En omläggning med samma tegel kräver inget nytt lov. Vill du byta från tegel till ett annat material "
             "behöver du alltså söka bygglov – och miljöprogrammet säger att husets tidstypiska uttryck inte får "
             "förvanskas genom byte av takmaterial. Hus som byggts senare och avviker bör anpassas i takmaterial och "
             "färg till omgivningen när de ändå renoveras."]},
        {"id": "ovriga", "h2": "Övriga Sundbyberg",
         "paras": [
             "Utanför Duvbo gäller de vanliga reglerna. På ett en- eller tvåbostadshus behövs i regel inte bygglov "
             "för att byta taktäckningsmaterial, men ändringen ska vara varsam och passa omgivningen, och "
             "detaljplanen ska följas. Kontrollera med "
             f'<a class="text-link" href="https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/fasadandring" rel="noopener">Sundbybergs stad</a> '
             "om du är osäker.",
             "Vi har nära till Sundbyberg från Bromma. Även utanför Duvbo är det ofta läkt och papp under ett "
             "tegel som fortfarande håller som behöver bytas. Läs mer om "
             '<a class="text-link" href="takrenovering.html">takrenovering och takomläggning</a>.']},
    ],
    "steps": [
        ("Epok och lov", "Vi bestämmer husets epok och om utökad lovplikt berör arbetet."),
        ("Dokumentation", "Taktassar, vindskivor och lister mäts upp och fotograferas."),
        ("Nedtagning", "Teglet tas ner och sorteras, hela pannor sparas."),
        ("Underlag", "Ny papp och läkt, lagning av råspont där det behövs."),
        ("Läggning", "Teglet läggs tillbaka och kompletteras med samma modell."),
        ("Takfot", "Taktassarna lagas och takfoten byggs så att de syns."),
    ],
    "rot": _rot_smahus(),
    "price": [
        "Kostnaden i Sundbyberg påverkas av takets form, hur många pannor som går att återanvända, hur mycket "
        "råspont som behöver bytas och hur många taktassar och profilerade detaljer som ska lagas. Läs mer om "
        '<a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a>.'],
    "faq": [
        ("Måste vi söka bygglov för att lägga om teglet på vår villa i Duvbo?",
         "Nej, inte om samma material läggs tillbaka. Den utökade lovplikten i Duvbo gäller bland annat utbyte "
         "av takläggningsmaterial, alltså om du vill byta till något annat."),
        ("Vad är kontursågade taktassar?",
         "Det är takstolarnas ändar under takfoten, utsågade i en dekorativ form. Miljöprogrammet för Duvbo nämner "
         "dem som ett typiskt drag hos sekelskiftesvillorna."),
        ("Kan vi få plåttak i Duvbo?",
         "På sekelskiftesvillorna förekom falsad slätplåt enligt miljöprogrammet. Ett byte från tegel till plåt "
         "kräver ändå bygglov, och kommunen bedömer om det passar husets epok."),
        ("Kostar bygglovet något i Duvbo?",
         "Enligt kommunens miljöprogram är åtgärder inom den utökade lovplikten kostnadsfria. Kontrollera med "
         "bygglovsenheten vad som gäller för ditt ärende."),
    ],
    "sources": [
        ("Sundbybergs stad – Miljöprogram för Duvbo (2024)",
         "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/"
         "Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf"),
        ("Sundbybergs stad – Duvbo", "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/duvbo"),
        ("Sundbybergs stad – Fasadändring",
         "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/fasadandring"),
        ("Boverket – Ändra fasad eller tak", BOV_UTANLOV),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "img": [
        ("Sekelskiftesvilla i trä med rött tegeltak och snickarglädje bakom ett spjälstaket",
         "Swedish wooden villa from about 1900 in Swiss chalet style with facade panels in alternating vertical and "
         "horizontal boards, decorative fretwork, an irregular red clay tile roof with a small turret, a simple "
         "picket fence and a leafy hedge in front, large old trees, Duvbo Sundbyberg, summer" + NO_PEOPLE),
        ("Takfot med lövsågade detaljer under ett tegeltak",
         "close view from below of the eaves of an old Swedish wooden villa showing exposed decoratively cut rafter "
         "tails painted white, red clay roof tiles above, a half-round metal gutter, soft daylight" + NO_PEOPLE),
        ("Ljust putsat hus från 1940-talet med flackt tegeltak",
         "simple light rendered Swedish house from the 1940s with a low-pitched red clay tile roof and visible "
         "rafter tails, small windows, a garden with fruit trees and a hedge, quiet residential street" + NO_PEOPLE),
    ],
}

# ---------------------------------------------------------------- VÄLLINGBY
TRP29A["Vällingby"] = {
    "title": "Takrenovering i Vällingby – radhusen i ABC-staden",
    "description": "Takrenovering i Vällingby: radhus i riksintresset Vällingby–Råcksta, Langendals radhus "
                   "i Råcksta och omläggning som behåller husgruppens uttryck.",
    "lead": "Vällingby byggdes på 1950-talet som Sveriges första ABC-stad, med höga hus närmast centrum och "
            "radhus och småhus längst ut. Hela Vällingby–Råcksta är riksintresse för kulturmiljövården, och "
            "staden nämner de ursprungliga husens gestaltning och detaljer bland det som är värdebärande. En "
            "takrenovering i Vällingby görs därför så att taket ser ut som förut när det är klart.",
    "card": "Radhusen i riksintresset Vällingby–Råcksta.",
    "sections": [
        {"id": "hus", "h2": "Radhusen längst ut från centrum",
         "paras": [
             "Vällingby–Råcksta planerades som en självförsörjande förort med arbete, bostäder och centrum. Ingen "
             "skulle ha längre än 900 meter till tunnelbanan. Kring centrum byggdes höga punkthus, sedan lägre "
             "flerbostadshus, och längst ut områden med radhus och småhus.",
             "Stadens statistik för 2024 visar 449 småhus i stadsdelen Vällingby. 228 är bostadsrätter och 220 "
             "ägs med äganderätt – alltså ungefär hälften var. Vem som beställer en takrenovering beror därför på "
             "vilken sorts hus du bor i."],
         "aside": {"title": "Vällingby i siffror (2024)",
                   "items": ["449 småhus i stadsdelen", "228 bostadsrätter", "220 med äganderätt",
                             "Riksintresse Vällingby (AB 120)"]}},
        {"id": "racksta", "h2": "Langendals radhus i Råcksta",
         "paras": [
             "Råcksta planerades samtidigt som Vällingby, och de första bostäderna var klara 1952. Stadsmuseet "
             "beskriver husen som mycket välplanerade, ofta grupperade kring skyddade innergårdar och med mycket "
             "sparad natur.",
             "Särskilt uppmärksammade är radhusen vid Långseleringen och Ramselegatan, ritade av arkitekten Adrian "
             "Langendal och klara 1953. De är kända för sin livfulla färgsättning och omväxlande detaljer, som de "
             "dekorativa räckena vid de franska fönstren. På hus med så tydlig gestaltning är takfot, vindskivor och "
             "plåtdetaljer en del av helheten, och de ska få tillbaka samma form och kulör efter en omläggning."]},
        {"id": "grimsta", "h2": "Grimsta och de andra husgrupperna",
         "paras": [
             "Staden räknar Grimsta som kulturhistoriskt värdefull miljö, och Råcksta både som riksintresse och "
             "värdefull miljö. I Vällingby finns också radhusområdena Atlantis och Omega, som stadens vägledning "
             "kallar kulturhistoriskt synnerligen värdefulla.",
             "I stadens beskrivning av riksintresset har Vällingby–Råcksta bebyggelse i tydligt definierade grupper "
             "med enhetlig karaktär. Ett tak som får ett annat material eller en "
             "annan kulör än grannarnas syns därför tydligt."]},
        {"id": "riks", "h2": "Vad riksintresset betyder för taket",
         "paras": [
             "I stadens beskrivning av riksintresset nämns de ursprungliga husens gestaltning och byggnadsdetaljer "
             "som värdebärande, liksom bebyggelsens indelning i tydliga grupper med enhetlig karaktär. Riksintresset "
             "i sig ger inga detaljerade regler för ditt tak, men det påverkar hur staden bedömer en bygglovsansökan.",
             "Lägger du om taket med samma material krävs inget lov. Vill du byta material eller kulör ska du först "
             "titta på Stadsmuseets klassificeringskarta och detaljplanen: är huset eller området särskilt "
             "kulturhistoriskt värdefullt gäller utökad lovplikt."]},
        {"id": "forening", "h2": "Brf-radhus och egna hus",
         "paras": [
             "Bor du i ett radhus som är bostadsrätt avgör stadgarna vem som ansvarar för taket. Är det föreningen "
             "beställer styrelsen, och då görs ofta en hel länga eller ett helt område i taget.",
             "Äger du huset själv beställer du, men taket hänger ofta ihop med grannarnas. Vi löser skarvarna mot "
             "grannhusen och visar hur de är gjorda, så att nästa granne som renoverar kan ansluta på samma sätt. "
             'Läs mer om <a class="text-link" href="takbesiktning.html">takbesiktning</a> innan du bestämmer dig.']},
    ],
    "steps": [
        ("Klassning", "Vi tittar på riksintresset, Stadsmuseets karta och detaljplanen."),
        ("Besiktning", "Pannor, papp, läkt och plåtdetaljer kontrolleras."),
        ("Dokumentation", "Takfot, vindskivor och kulörer mäts och fotograferas."),
        ("Beställare", "Vi klarar ut om föreningen eller du beställer."),
        ("Omläggning", "Nytt underlag och samma täckning som husgruppen."),
        ("Detaljer", "Plåt och vindskivor i samma form och kulör som förut."),
    ],
    "rot": _rot_smahus("Är radhuset en bostadsrätt och taket föreningens ansvar ger arbetet inget rotavdrag för dig "
                       "som medlem. "),
    "price": [
        "Kostnaden i Vällingby påverkas av takets yta och form, om flera hus i längan görs samtidigt, hur mycket "
        "underlag som behöver bytas och hur många plåt- och snickeridetaljer som ska återskapas. Läs mer om "
        '<a class="text-link" href="vad-kostar-takrenovering.html">vad en takrenovering kostar</a>.'],
    "faq": [
        ("Vårt radhus ligger i riksintresset Vällingby–Råcksta – behöver vi bygglov för att lägga om taket?",
         "Inte för en omläggning med samma material. Vill ni byta material eller kulör ska ni kontrollera "
         "Stadsmuseets karta och detaljplanen, eftersom utökad lovplikt kan gälla."),
        ("Vem beställer taket i vår brf med radhus i Vällingby?",
         "Det står i stadgarna. Ansvarar föreningen för taket är det styrelsen som beställer, och då ger arbetet "
         "inget rotavdrag för medlemmarna."),
        ("Kan vi lägga om bara vårt eget tak i längan?",
         "Ja, om du äger huset. Vi ansluter mot grannarnas tak och dokumenterar skarvarna. Ofta blir det enklare "
         "och billigare om flera grannar gör det samtidigt."),
        ("Vad är speciellt med Langendals radhus i Råcksta?",
         "Stadsmuseet lyfter fram deras livfulla färgsättning och omväxlande detaljer. Vid en renovering är det "
         "viktigt att takfot, vindskivor och plåt får tillbaka samma form och kulör."),
    ],
    "sources": [
        ("Stockholms stad – Riksintressen i översiktsplanen (Vällingby AB 120)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf"),
        ("Stockholms stadsmuseum – Stockholms spår: Råcksta", SSM + "SSM_DOK_000072.pdf"),
        ("Stockholms stad – Varsam utveckling av småhus- och villaområden", VARSAM),
        ("Stockholms stad – Områdesfakta Vällingby (2025)", OF + "vasterort/hasselby-vallingby/vallingby.pdf"),
        ("Stockholms stad – Fasadändring", BL_FASAD),
        ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", BL_KLASS),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "img": [
        ("Radhus från 1950-talet med färgglada fasader och sadeltak",
         "low two-storey Swedish 1950s terraced houses in a simple modernist style, plain rendered facades in "
         "muted ochre and pale green, a long shallow gable roof with dark concrete tiles running over the whole "
         "row, small balconies with thin metal railings, lawns and tall pine trees, Vällingby Stockholm, early autumn" + NO_PEOPLE),
        ("Takfot med vindskiva och plåtbeslag på ett radhus",
         "close view of the eaves and gable end of a 1950s Swedish terraced house: painted wooden barge board, "
         "neat grey metal edge flashing, dark roof tiles and a half-round gutter, soft daylight" + NO_PEOPLE),
        ("Radhusgrupp i tegel bland höga tallar",
         "group of low Swedish 1950s terraced houses with red brick facades and identical dark tiled roofs set into "
         "natural terrain with rocks and tall pine trees, a gravel footpath between the houses, summer light"
         + NO_PEOPLE),
    ],
}
