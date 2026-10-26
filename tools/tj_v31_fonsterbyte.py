# -*- coding: utf-8 -*-
"""Fönsterbyte – ortsidor v31: Kista, Skärholmen, Södermalm (2026-10-27).
Hubb: fonsterbyte.html (TJ_HUB["fonsterbyte"]). Intent: byta fönster – skild från ortens fonsterrenovering-<ort>.html
(renovera befintliga bågar), som länkas där den finns. Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.
Södermalm har egen trust-rad (sidnyckel "trust"): rotavdrag ges inte för fönsterbyte i bostadsrätt.

Lokal vinkel per sida:
Kista – stadsdelen byggd 1975–1980 på Järvafältet (Stockholms spår: 2 500 lägenheter och omkring 780 småhus),
  områdesfakta 2025 för Kista och Akalla (radhus med äganderätt och bostadsrätt), vem som beställer bytet i ett
  bostadsrättsradhus (stadgarna, brl 7:12), stadens lista över ändringar av fönster.
Skärholmen – storskalig stadsdel enligt Varsam (Bredäng 1962, sedan Sätra; radhus, kedjehus, villor och atriumhus på
  små tomter, enhetlig gestaltning och färgsättning inom husgrupperna), Bredäng som kulturhistoriskt värdefull
  miljö i Varsam-tabellen, områdesfakta 2025 för Skärholmen, Sätra, Bredäng och Vårberg.
Södermalm – områdesfakta 2025 (77 525 bostäder, 43 680 bostadsrätter, 13 äganderätter), riksintressedelens tidiga
  bebyggelse på malmarna (omkring 300 hus kvar, fönster som karaktärsdrag) och stenstaden 1870–1930 med enklare
  gårdsfasader, bygglov för flerbostadshus mot allmän plats, Skatteverkets regel för fönster i bostadsrätt.

Fakta endast från källorna i respektive 'sources', öppnade med curl (webbläsar-UA) 2026-10-27, alla svarade 200;
pdf:erna (Stockholms spår, Varsam, riksintressen, områdesfakta) har textlager. Skatteverket lästes 2026-10-27:
småhus – reparera eller byta ut fönster; bostadsrätt – byta fönster och arbeta mellan eller på utsidan ger inget
avdrag, arbete på insidan av befintliga fönster (glaset i inre bågen, tätningslist) ger avdrag; högst 30 procent av
arbetskostnaden och högst 50 000 kronor per person och år.
Strukna / ej använda: vilka fönster enskilda hus i Kista har, att Kista finns i Varsam-tabellen (det gör det inte),
handläggningstider och avgifter, U-värden, egna uppdrag i orterna. Inga priser, garantier, omdömen eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_TRUST_BRF = ["Gratis besök och kostnadsförslag", "Underlag till föreningens styrelse"]
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"

_STH_FD = ("Stockholms stad – Fönster och dörrar", _SB + "fonster-och-dorrar/")
_STH_FAS = ("Stockholms stad – Fasadändring", _SB + "fasadandring/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 och 12 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SPAR_KISTA = ("Stockholms stadsmuseum – Stockholms spår: Kista (pdf)",
               "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000080.pdf")


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor "
            "ger inget avdrag, och Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ KISTA
"fonsterbyte-kista.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Kista", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Kista – radhusen från 1975–1980",
  "description": "Fönsterbyte i Kista: radhus och villor från 1975–1980, vem som beställer i ett bostadsrättsradhus, när det räknas som ändring och rotavdrag.",
  "h1": "Fönsterbyte i Kista",
  "lead": "Kista byggdes ut mellan 1975 och 1980, och i småhusen sitter i många fall fortfarande de fönster som monterades när husen var nya. Geal Entreprenad AB byter fönster i radhus, kedjehus och villor i Kista och Akalla och hjälper till att reda ut vem som ska beställa när huset ägs av en förening.",
  "card": "Radhus och villor från 1970-talet.",
  "sections": [
    {"id": "jarvafaltet-kista", "anchor": "Stadsdelen",
     "h2": "En stadsdel från slutet av 1970-talet",
     "paras": [
       "Stadsmuseets Stockholms spår om Kista berättar att stadsdelen ligger på det gamla militära övningsområdet Järvafältet. Staden köpte marken 1966 och byggde ut Kista åren 1975–1980. Staden tillämpade betydligt friare former för den arkitektoniska utformningen här än i de andra stadsdelarna på Järvafältet. Bebyggelsen beskrivs som 2 500 lägenheter i flerbostadshus och omkring 780 småhus.",
       "Är fönstren original har de alltså suttit i snart femtio år. Bågar, beslag och tätningar från den tiden kan vara slitna även om karmen är frisk, och då är det värt att jämföra ett byte med en " + _L.format("fonsterrenovering-kista.html", "fönsterrenovering i Kista") + " innan du bestämmer dig. Vi går igenom båda vägarna på platsbesöket och visar var bågarna är slitna.",
     ],
     "aside": {"title": "Kista enligt Stockholms spår", "items": [
       "Marken köptes 1966", "Utbyggd 1975–1980", "2 500 lägenheter", "Omkring 780 småhus"]}},
    {"id": "agarform-kista", "h2": "Äganderätt eller bostadsrätt i radhuset",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 971 småhus i Kista. 482 av dem ägs med äganderätt och 404 är bostadsrätter. I grannstadsdelen Akalla finns 671 småhus, där 493 är bostadsrätter och 170 har äganderätt. I de två stadsdelarna tillsammans är alltså ungefär vartannat småhus en bostadsrätt, där ägaren inte äger själva huset.",
       "Bostadsrättslagen säger att bostadsrättshavaren håller lägenheten i gott skick om inte något annat bestämts i stadgarna. Därför är det stadgarna som avgör om fönstren är ditt eller föreningens ansvar. Ligger ansvaret på föreningen kan den välja att byta i en hel husgrupp på en gång. Vi läser stadgarna med dig och tar fram underlag till styrelsen om föreningen ska fatta beslut.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Kista: 971 småhus", "Varav 482 med äganderätt", "Akalla: 671 småhus", "Varav 493 bostadsrätter"]}},
    {"id": "andring-kista", "h2": "Samma utseende eller ett nytt",
     "paras": [
       "Stockholms stad skriver att du ofta behöver bygglov för att ändra befintliga fönster i fasaden, och att det beror på vilken byggnad och fasad det gäller. Som ändring räknar staden bland annat en ny placering, andra dimensioner, proportioner eller profiler på karm och båge, en annan upphängning och en ändrad indelning, till exempel en borttagen mittpost.",
       "Ett byte till fönster som ser ut som de gamla är därför enklast. Vill du ändra något kontrollerar vi först detaljplanen och Stadsmuseets klassificeringskarta. Staden påpekar också att nya fönster kan öka insynen hos grannarna. I en radhuslänga där husen sitter ihop är det klokt att prata med grannarna innan nya öppningar görs.",
     ],
     "aside": None},
    {"id": "akalla-kista", "h2": "Villor och atriumhus i Akalla",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver småhusen i de storskaliga stadsdelarna som i huvudsak radhus och kedjehus, men nämner Akalla som exempel där det också finns villor och atriumhus. Fasaderna blandar tegel, trä och skivor, och husen i en grupp är mycket lika varandra.",
       "I ett atriumhus vetter många fönster mot den inre gården och syns knappt från gatan, medan fönstren mot gatan är det grannarna ser. Vi tar hänsyn till båda när vi föreslår nya fönster, så att husgruppen behåller sitt gemensamma uttryck. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Kista",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter karmar och bågar."),
    ("Stadgar och karta", "Vem ansvarar, och gäller någon särskild regel?"),
    ("Förslag", "Fönster med samma indelning som grannhusen."),
    ("Beställning", "Fönstren tillverkas efter uppmätning."),
    ("Byte", "Ny karm, drevning, tätning och foder."),
    ("Avslut", "Bleck på plats och genomgång med dig."),
  ],
  "rot_h2": "ROT-avdrag för nya fönster i Kista",
  "rot": [
    "Äger du radhuset eller villan räknar Skatteverket det som rotarbete att reparera eller byta ut fönster och att montera isolerglas. Är huset en bostadsrätt ger själva fönsterbytet inget avdrag, men arbete på insidan av befintliga fönster gör det, till exempel att byta glaset i den inre bågen eller sätta tätningslist.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet i Kista?",
  "price": [
    "Antal och storlek på fönstren, om de tillverkas efter uppmätning, glas och beslag, foder och bleck, och om flera hus i samma grupp byts samtidigt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem bestämmer om fönsterbytet i mitt bostadsrättsradhus i Kista?",
     "Det beror på föreningens stadgar. Bostadsrättslagen låter stadgarna bestämma vad medlemmen själv ska hålla i gott skick."),
    ("När byggdes radhusen i Kista?",
     "Enligt Stadsmuseet byggdes Kista ut åren 1975–1980, med omkring 780 småhus och 2 500 lägenheter i flerbostadshus."),
    ("Får jag rotavdrag för nya fönster i ett radhus med äganderätt i Kista?",
     "Ja, Skatteverket godkänner byte och reparation av fönster i småhus. För en bostadsrätt gäller bara arbete på insidan av fönstren."),
    ("Behöver jag bygglov för att ta bort mittposten i fönstren i Akalla?",
     "Det kan behövas. Staden räknar en ändrad indelning som ändring av fönster, och lovplikten beror på huset och fasaden."),
  ],
  "sources": [_SPAR_KISTA, _of("Kista", "vasterort/jarva/kista"), _of("Akalla", "vasterort/jarva/akalla"), _VARSAM, _STH_FD, _BRL, _SKV],
  "cta": ("Ska fönstren bytas i Kista?", "Boka ett gratis platsbesök, så mäter vi upp fönstren och går igenom stadgarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhuslänga i tegel och trä med låga tak",
     "row of 1970s Swedish terraced houses with dark brown wooden panels and red brick, low pitched roofs, white framed windows, small front gardens with shrubs, paved footpath, summer daylight" + _SFX),
    ("Nytt fönster med vit karm i en träfasad",
     "close view of a new white wooden window with two side-hung sashes fitted in a dark brown vertical wood panel facade of a 1970s terraced house, clean sheet metal sill, daylight" + _SFX),
    ("Atriumhus med fönster mot en inre gård",
     "small enclosed inner courtyard of a 1970s Swedish single-storey atrium house, large windows and a glazed door facing the courtyard, paving stones and a small tree, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"fonsterbyte-skarholmen.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Skärholmen", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Skärholmen – radhusen i husgrupperna",
  "description": "Fönsterbyte i Skärholmen: radhus och kedjehus från 1960- och 70-talen i Sätra, Bredäng och Vårberg, husgruppens helhet, karta och rotavdrag.",
  "h1": "Fönsterbyte i Skärholmen",
  "lead": "Radhusen i Sätra, Bredäng, Vårberg och Skärholmen byggdes i grupper där husen var nästan identiska. När ett hus i gruppen får nya fönster märks det direkt. Geal Entreprenad AB byter fönster i småhus i Skärholmens stadsdelsområde och föreslår fönster som passar både huset och grannhusen.",
  "card": "Radhus i sammanhållna husgrupper.",
  "sections": [
    {"id": "storskalig-skarholmen", "anchor": "Husgrupperna",
     "h2": "Småhus i de storskaliga stadsdelarna",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden berättar att Bredäng var den första stadsdelen som planerades i stor skala. Bygget började 1962, och sedan följde Sätra. En stor andel av miljonprogrammets bebyggelse bestod av gruppbyggda småhus och radhus. Vägledningen beskriver dem som radhus, kedjehus, villor och atriumhus, uppförda på små tomter och med mycket enhetlig utformning inom varje grupp.",
       "Fasaderna blandade tegel, trä och skivor, och färgsättningen var noga komponerad och lika inom husgruppen. För ett fönsterbyte betyder det att karmens kulör, bågarnas indelning och blecken helst ska stämma med grannhusens. Det är också det första vi tittar på vid platsbesöket. Vägledningen nämner dessutom att nivåskillnader ofta tas upp med en souterrängvåning, så ett radhus kan ha fönster på olika höjd mot gatan och mot trädgården. Vi mäter därför varje fasad för sig.",
     ],
     "aside": {"title": "Gruppbyggda småhus enligt Varsam", "items": [
       "Bredäng påbörjades 1962", "Radhus och kedjehus", "Små tomter", "Enhetlig färgsättning i gruppen"]}},
    {"id": "smahus-skarholmen", "h2": "Hur många småhus som finns",
     "paras": [
       "Stadens områdesfakta för 2025 visar att småhusen i stadsdelsområdet till största delen ägs med äganderätt. Vårberg har 580 småhus, varav 577 med äganderätt. I Skärholmen är det 543 av 551, i Sätra 536 av 538 och i Bredäng 320 av 322. Flerbostadshusen domineras i stället av hyresrätter: i Bredäng finns till exempel 3 037 hyresrätter hos privata värdar och 973 i allmännyttan, men bara 722 bostadsrätter.",
       "Eftersom nästan alla radhusägare äger sitt hus beställer de också fönsterbytet själva. Ibland vill flera grannar byta samtidigt, och då kan vi mäta upp hela längan på en gång så att fönstren blir likadana. Den som hellre vill rusta de gamla bågarna kan läsa om " + _L.format("fonsterrenovering-skarholmen.html", "fönsterrenovering i Skärholmen") + ".",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Vårberg: 577", "Skärholmen: 543", "Sätra: 536", "Bredäng: 320"]}},
    {"id": "bredang-skarholmen", "h2": "Bredäng är utpekat som värdefull miljö",
     "paras": [
       "I tabellen i slutet av vägledningen är Bredäng markerat som kulturhistoriskt värdefull miljö. Skärholmen, Sätra och Vårberg har ingen sådan markering. Vägledningen skriver att några av de storskaliga stadsdelarna är klassificerade som kulturhistoriskt värdefulla och att förändringar där behöver visa hänsyn till de värdena.",
       "Stockholms stad skriver att du behöver söka bygglov för åtgärder som annars är lovbefriade om huset ligger i ett område som är utpekat som särskilt kulturhistoriskt värdefullt. Vi kontrollerar därför Stadsmuseets klassificeringskarta och detaljplanen för ditt hus innan vi föreslår nya fönster med en annan indelning eller färg. Vägledningen skriver också att mindre tillbyggnader, till exempel inglasade uterum, är vanliga i de här områdena, och glaspartiet i ett sådant uterum kan bytas i samma veva.",
     ],
     "aside": None},
    {"id": "valja-skarholmen", "h2": "Vad som räknas som en ändring",
     "paras": [
       "Staden räknar bland annat nytt material eller ny kulör, en annan storlek eller placering, andra profiler på karm, båge och spröjs, en annan upphängning och en ändrad indelning som ändringar av fönster. För ett radhus där grannarnas fönster är likadana syns sådana ändringar tydligt i längan.",
       "Vi brukar därför föreslå fönster som har samma luftindelning och upphängning som originalen, men med nyare glas. Vill du ändra mer går vi igenom vad det kan kräva innan något beställs. Staden påpekar också att nya fönster kan ge ökad insyn hos grannarna och att nya öppningar kan påverka den bärande konstruktionen. I ett radhus med tunna mellanväggar mot grannen är det två skäl att planera noga. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Skärholmen",
  "steps": [
    ("Platsbesök", "Vi mäter fönstren och fotograferar grannhusen."),
    ("Kontroll", "Detaljplan och Stadsmuseets karta."),
    ("Förslag", "Samma indelning och kulör som husgruppen."),
    ("Tillverkning", "Fönster efter uppmätning."),
    ("Montage", "Byte, tätning, foder och nya bleck."),
    ("Slutgenomgång", "Vi går igenom fönstren och skötseln."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Skärholmen",
  "rot": [
    "För ett radhus eller en villa med äganderätt räknar Skatteverket det som rotarbete att reparera eller byta ut fönster, montera isolerglas och byta fönsterbleck. Är huset yngre än fem år får arbetet bara återställa det ursprungliga skicket.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet i Skärholmen?",
  "price": [
    "Antal fönster och fönsterdörrar, storlek och indelning, glas och beslag, nya bleck och foder och om flera hus i längan byter samtidigt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kräver ett fönsterbyte i Bredäng bygglov?",
     "Det kan göra det. Bredäng är markerat som kulturhistoriskt värdefull miljö i stadens vägledning, och då kan lov krävas även för annars lovfria åtgärder."),
    ("Måste mina nya fönster i Sätra se ut som grannarnas?",
     "Ändringen ska göras varsamt och anpassas till omgivningen. Varsam-vägledningen beskriver husgrupper med enhetlig gestaltning och färgsättning."),
    ("Kan flera grannar i Vårberg byta fönster samtidigt?",
     "Ja. Vi kan mäta upp hela längan på en gång så att fönstren blir likadana, och varje ägare får sitt eget kostnadsförslag."),
    ("När byggdes radhusen i Bredäng?",
     "Bredäng började byggas 1962 och var enligt staden den första stadsdelen som planerades i stor skala."),
  ],
  "sources": [_VARSAM, _of("Skärholmen", "soderort/skarholmen/skarholmen"), _of("Sätra", "soderort/skarholmen/satra"),
              _of("Bredäng", "soderort/skarholmen/bredang"), _of("Vårberg", "soderort/skarholmen/varberg"), _STH_FD, _STH_KL, _SKV],
  "cta": ("Ska fönstren bytas i Skärholmen?", "Boka ett gratis platsbesök, så mäter vi upp fönstren och jämför med husgruppen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Kedjehus från 1960-talet med tegel och träpanel",
     "row of 1960s Swedish linked houses with yellow brick ground floors and light grey wooden panel upper parts, identical white windows, small front gardens, footpath with young trees, summer" + _SFX),
    ("Två grannhus med likadana fönster",
     "full-bleed photo filling the whole frame without borders, garden side of two adjoining single-storey Swedish 1960s terraced houses in a Stockholm suburb, light grey horizontal wood panel and yellow brick, identical wide white windows with dark sheet metal sills, low flat roof, small lawn plots divided by a low hedge, Scandinavian modernist architecture, daylight" + _SFX),
    ("Nytt fönster monterat i en tegelfasad",
     "close view of a newly installed white wooden window in a yellow brick wall, fresh sealant joint, new grey sheet metal window sill, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SÖDERMALM
"fonsterbyte-sodermalm.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Södermalm", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte på Södermalm – gatufasad och gårdsfasad",
  "description": "Fönsterbyte på Södermalm: föreningens beslut, bygglov för fasader mot gatan, malmarnas äldre hus, stenstaden och rotavdrag i bostadsrätt.",
  "h1": "Fönsterbyte på Södermalm",
  "lead": "På Södermalm är nästan alla bostäder lägenheter, och ett fönsterbyte beslutas därför oftast av en bostadsrättsförening. Om fasaden vetter mot gatan eller gården gör skillnad för lovet. Geal Entreprenad AB tar fram underlaget till styrelsen och bygglovet och byter fönster i flerbostadshus och de få småhusen på Södermalm.",
  "card": "Föreningar, gatufasad och gårdsfasad.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "foreningen-sodermalm", "anchor": "Föreningen",
     "h2": "Föreningen beställer",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 77 525 bostäder i Södermalms stadsdelsområde. 43 680 av dem är bostadsrätter, 23 361 är hyresrätter hos privata värdar och 10 471 hör till allmännyttan. Bara 13 bostäder ägs med äganderätt. Nästan varje fönsterbyte på Södermalm är alltså en fråga för en förening eller en fastighetsägare.",
       "Bostadsrättslagen säger att medlemmen håller lägenheten i gott skick om inte stadgarna säger något annat. Vem som ansvarar för fönstren avgörs alltså av stadgarna. Vi tar fram ett underlag som styrelsen kan fatta beslut på, med uppmätning, förslag och tidsplan. Har lägenheten särskilda kulturhistoriska värden krävs enligt samma lag styrelsens tillstånd för åtgärder som påverkar de värdena, även på insidan.",
     ],
     "aside": {"title": "Bostäder 2025", "items": [
       "77 525 bostäder", "43 680 bostadsrätter", "33 832 hyresrätter", "13 med äganderätt"]}},
    {"id": "lov-sodermalm", "h2": "Mot gatan krävs bygglov",
     "paras": [
       "Stockholms stad skriver att det för byggnader som inte är en- eller tvåbostadshus, till exempel flerbostadshus, krävs bygglov om ändringen görs på en fasad eller ett tak som vetter mot allmän plats. Ändringar på sidor som inte vetter mot allmän plats kan göras utan lov om vissa förutsättningar är uppfyllda. Ligger huset i ett särskilt kulturhistoriskt värdefullt område krävs lov ändå.",
       "Som ändring av fönster räknar staden bland annat nytt material eller ny kulör, andra profiler och spröjs, en annan upphängning och en ändrad indelning. Ett byte mot fönster med samma utseende är därför ofta det enklaste. Staden skriver att bygglovsplikten också beror på byggnaden, eftersom ett hus kan ha karaktäristiska fönster eller en tidstypisk indelning där en ändring påverkar både fasaden och husets karaktär. Vi kontrollerar Stadsmuseets klassificeringskarta och detaljplanen för just ert hus innan förslaget lämnas.",
     ],
     "aside": {"title": "Flerbostadshus på Södermalm", "items": [
       "Fasad mot gatan: bygglov", "Mot gården: ofta utan lov", "Värdefullt område: lov", "Kontroll av kartan först"]}},
    {"id": "stenstaden-sodermalm", "h2": "Stenstaden och gårdsfasaderna",
     "paras": [
       "Översiktsplanens riksintressedel beskriver den klassiska stenstaden från 1870–1930 med utbredning på bland annat Södermalm. Gatufasaderna är tydligt uppdelade i sockelvåning och huvudfasad, medan gårdsfasaderna är enklare. När gatufasaden är rikare utformad än gårdsfasaden kan även fönstren skilja sig åt, och det kontrollerar vi på plats.",
       "Vill föreningen byta alla fönster samtidigt brukar vi därför föreslå två typer: en mot gatan som följer de ursprungliga profilerna och en enklare mot gården. Riksintressedelen nämner också att mer begränsade förändringar som inre modernisering prövas enligt plan- och bygglagens varsamhetskrav.",
     ],
     "aside": None},
    {"id": "malmarna-sodermalm", "h2": "De äldre husen på malmarna",
     "paras": [
       "Från bebyggelsen på malmarna före stenstaden återstår enligt riksintressedelen omkring 300 hus, mestadels på Södermalm. Värdekärnorna är Fjällgatan, Katarinaberget, Vita bergen, Åsöberget och Östra Mariaberget. Till karaktärsdragen räknas byggnadsdetaljer som fönster, entréportar och ornamentik, som tillsammans bildar en karaktäristisk helhetsbild.",
       "I de här husen är ett byte sällan förstahandsvalet. Där brukar det vara bättre att laga och komplettera de befintliga bågarna, och då finns " + _L.format("fonsterrenovering-sodermalm.html", "fönsterrenovering på Södermalm") + ". Måste ett fönster ändå bytas tillverkas det nya efter det gamla. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster på Södermalm",
  "steps": [
    ("Besiktning", "Gratis besök där vi mäter och bedömer fönstren."),
    ("Underlag", "Förslag och tidsplan till styrelsen."),
    ("Bygglov", "Ritningar för fasaden mot gatan."),
    ("Tillverkning", "Fönster efter uppmätning, gata och gård."),
    ("Byte", "Ett fönster i taget, med skydd i lägenheterna."),
    ("Avslut", "Foder, bleck och genomgång med föreningen."),
  ],
  "rot_h2": "ROT-avdrag vid fönsterbyte i bostadsrätt",
  "rot": [
    "Skatteverket ger inget rotavdrag för att byta fönster i en bostadsrätt, och inte heller för arbete mellan eller på utsidan av fönstren. Arbete på insidan av befintliga fönster ger avdrag, till exempel att byta glaset i den inre bågen eller montera tätningslist, om det är något du som medlem ansvarar för enligt stadgarna.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet på Södermalm?",
  "price": [
    "Antal fönster, profiler mot gatan och gården, om bleck och foder också ska bytas, bygglovsritningar, ställning eller skylift mot innergården, och hur bytet planeras för att störa de boende så lite som möjligt. Efter besiktningen får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vår förening bygglov för att byta fönster mot gatan på Södermalm?",
     "Oftast ja. För flerbostadshus krävs bygglov när fasaden vetter mot allmän plats, och i värdefulla områden krävs lov även mot gården."),
    ("Får jag rotavdrag när föreningen byter fönster i min bostadsrätt på Södermalm?",
     "Nej. Fönsterbyte i bostadsrätt ger inget rotavdrag. Arbete på insidan av befintliga fönster kan däremot ge avdrag."),
    ("Kan fönstren mot gården se annorlunda ut än mot gatan?",
     "Ja. Gårdsfasaderna i stenstaden är enklare, och ett byte mot gården kräver ofta inget lov om förutsättningarna är uppfyllda."),
    ("Hur många av de äldre husen på malmarna finns kvar?",
     "Översiktsplanen räknar med omkring 300 hus från perioden, mestadels på Södermalm."),
  ],
  "sources": [_of("Södermalms stadsdelsområde", "inre-staden/sodermalm/sodermalm-stadsdelsomrade"), _STH_FAS, _STH_FD, _STH_KL, _RIKS, _BRL, _SKV],
  "cta": ("Ska föreningen byta fönster på Södermalm?", "Boka en gratis besiktning, så mäter vi upp fönstren och tar fram underlaget till styrelsen innan föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Stenstadshus med rad av fönster mot gatan",
     "upper floors of a late 1800s plastered Stockholm apartment building seen from across the street, rows of tall white two-sash windows with ornamented surrounds and a copper roof above, no ground floor visible, no signs, soft daylight" + _SFX),
    ("Enklare gårdsfasad med vita fönster",
     "plain plastered courtyard facade of an early 1900s Stockholm apartment building, simple white windows in rows, a small inner courtyard with a tree and paving, overcast daylight" + _SFX),
    ("Äldre trähus med små fönster på en bergsluttning",
     "small 1700s wooden house painted ochre on a steep cobbled lane in old Stockholm, small-paned white windows, wooden fence and garden, no people, summer daylight" + _SFX),
  ],
},
}
