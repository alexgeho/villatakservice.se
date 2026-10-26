# -*- coding: utf-8 -*-
"""Tapetsering – ortsidor v31: Hägersten, Kista, Vällingby (2026-10-27).
Hubb: malare.html (deltjänst, TJ_SERVICES["tapetsering"]). Intent: tapetsera väggar inomhus. Tre bilder per sida:
img[0] hero 4:3, img[1] och img[2] 3:2.

Lokal vinkel per sida:
Hägersten – områdesfakta 2025 för Mälarhöjden (villor med äganderätt), Hägerstensåsen, Västertorp och Fruängen (hyresrätter
  och bostadsrätter), Varsam om Mälarhöjden som villasamhälle, Byggnadsvårdsföreningen om underlag (puts, spänd papp och
  väv i äldre hus, kridering 1920–1950-tal, bronstryck), jordabalken 12 kap. 24 a § om hyresgästens rätt att tapetsera.
Kista – Stockholms spår (utbyggd 1975–1980), områdesfakta 2025 (bostadsrätter, hyresrätter, specialbostäder, lägenheter
  utan kök), Byggnadsvårdsföreningen om betongväggar i en 70-talslägenhet och om underlag i nya hus (gips, betong,
  puts), bostadsrättslagen 7 kap. 12 §.
Vällingby – riksintressedelen AB 120 (utbyggd under 1950-talet), områdesfakta 2025 för Vällingby, Råcksta och Grimsta,
  Byggnadsvårdsföreningen om kridering och sandspackel från mitten av 1950-talet, bostadsrättslagen 7 kap. 7 §
  (lägenheter med kulturhistoriska värden).

Fakta endast från källorna i respektive 'sources', öppnade med curl (webbläsar-UA) 2026-10-27, alla svarade 200; pdf:erna
har textlager. Skatteverket 2026-10-27: tapetsera räknas som rotarbete (målning och tapetsering) i småhus och, innanför
lägenhetens tak, väggar och golv, i bostadsrätt; arbetet ska utföras i bostad som köparen äger.
Strukna / ej använda: vilka tapeter enskilda hus i orterna har, tapetpriser, Stadsmuseets klassning av interiörer.
Inga garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_BV = "https://byggnadsvard.se/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


def _sbf(titel, slug):
    return (f"Svenska Byggnadsvårdsföreningen – {titel}", _BV + slug + "/")


_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_JB = ("Riksdagen – Jordabalk (1970:994), 12 kap. 24 a §",
       "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/jordabalk-1970994_sfs-1970-994/")
_BRL12 = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 12 §",
          "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_BRL7 = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
         "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_SPAR_KISTA = ("Stockholms stadsmuseum – Stockholms spår: Kista (pdf)",
               "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000080.pdf")
_SBF_UNDERLAG = _sbf("Underlag för tapetsering", "underlag-for-tapetsering")
_SBF_BETONG = _sbf("Inomhus betongvägg", "inomhus-betongvaegg")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Tapeter och annat "
            "material ger inget avdrag, och Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ HÄGERSTEN
"tapetsering-hagersten.html": {
  "kind": "district", "service": "tapetsering", "ort": "Hägersten", "svc_label": "Tapetsering",
  "title": "Tapetsering i Hägersten – villor och lägenheter",
  "description": "Tapetsering i Hägersten: villorna i Mälarhöjden och lägenheterna i Hägerstensåsen och Fruängen, gamla väggar som släpper, hyresrätt och rotavdrag.",
  "h1": "Tapetsering i Hägersten",
  "lead": "I Hägersten ligger villastaden Mälarhöjden granne med lägenhetsområden som Hägerstensåsen, Västertorp och Fruängen. Väggarna i ett hus från 1920-talet och i en lägenhet från 1960-talet behöver olika underarbete innan tapeten sätts upp. Geal Entreprenad AB tapetserar i villor, radhus och lägenheter i Hägersten och börjar med att ta reda på vad väggen är gjord av.",
  "card": "Villor och lägenheter i samma stadsdel.",
  "sections": [
    {"id": "stadsdelen-hagersten", "anchor": "Stadsdelen",
     "h2": "Villastad och lägenhetsområden",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden berättar att villasamhällen växte upp i bland annat Mälarhöjden efter privata initiativ genom större markförvärv. Stadens områdesfakta för 2025 räknar 1 086 småhus i Mälarhöjden, varav 988 med äganderätt. Bara drygt 400 bostäder där ligger i flerbostadshus.",
       "I grannstadsdelarna är det tvärtom. Hägerstensåsen har 2 657 hyresrätter hos privata värdar och 2 034 bostadsrätter, men bara 36 småhus med äganderätt. Fruängen har 3 495 bostadsrätter och Västertorp 1 627 bostadsrätter och 1 524 lägenheter i allmännyttan. Vem som får och vill tapetsera, och vem som betalar, skiljer sig därför mycket åt inom samma stadsdelsområde.",
     ],
     "aside": {"title": "Hägersten 2025", "items": [
       "Mälarhöjden: 988 villor med äganderätt", "Hägerstensåsen: 2 034 bostadsrätter", "Fruängen: 3 495 bostadsrätter", "Västertorp: 1 524 i allmännyttan"]}},
    {"id": "aldre-hagersten", "h2": "Väggar i hus från 1920–1950-talen",
     "paras": [
       "Byggnadsvårdsföreningen skriver att dålig vidhäftning kan befaras i hus från 1920–1950-talen, då väggarna underbehandlades med lim och krita, så kallad kridering. Vid mitten av 1950-talet började sandspackel användas som underlag i stället. I en villa i Mälarhöjden från den perioden provar vi därför hur väggen tar emot innan vi sätter upp en ny tapet.",
       "Föreningen skriver också att det oftast går bra att tapetsera på gamla tapeter, men att bronstryck kan slå igenom de nya. Då grundar vi med alkydfärg eller shellack först. Lämpliga underlag i gamla hus är enligt föreningen puts, timmer, spänd papp och spänd väv, och på spänd papp kan det bildas veck i hörnen som efter några år behöver justeras.",
     ],
     "aside": {"title": "Äldre väggar", "items": [
       "Kridering 1920–1950-tal", "Sandspackel från mitten av 1950-talet", "Bronstryck kan slå igenom", "Grundning med alkyd eller shellack"]}},
    {"id": "hyresgast-hagersten", "h2": "Hyresgästens rätt att tapetsera",
     "paras": [
       "Jordabalken ger bostadshyresgäster rätt att på egen bekostnad utföra målning, tapetsering och därmed jämförliga åtgärder i lägenheten. Minskar lägenhetens bruksvärde genom arbetet har hyresvärden rätt till ersättning för skadan. Det betyder att en hyresgäst i Hägerstensåsen eller Västertorp kan tapetsera utan att fråga hyresvärden, men att hyresvärden kan få ersättning om arbetet minskar bruksvärdet.",
       "Rotavdrag får du däremot bara för arbete i en bostad du äger. Hyresgäster betalar alltså hela arbetskostnaden själva. Vi går igenom väggarna, föreslår en tapet som passar rummet och gör underarbetet så att väggen inte skadas.",
     ],
     "aside": None},
    {"id": "fukt-hagersten", "h2": "Kök, badrum och oeldade rum",
     "paras": [
       "Byggnadsvårdsföreningen skriver att tapeter kan användas på många underlag, så länge luftfuktigheten inte blir för hög, som den kan bli i kök och badrum. Hög fuktighet i äldre hus och oeldade sommarhus skadar papperstapeter långsamt, vilket syns som lösa skarvar, fuktfläckar och svarta prickar.",
       "Föreningen råder också att man köper en extra rulle av en äldre tapettyp som kan försvinna ur sortimentet, så att den går att laga senare. Vi är noga med underarbetet, eftersom vassa korn och toppar från dålig slipning eller orent klister syns mer genom tapeten än ojämnheter. Mer om tjänsten finns under " + _L.format("malare-hagersten.html", "målare i Hägersten") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så tapetserar vi i Hägersten",
  "steps": [
    ("Platsbesök", "Gratis besök där vi provar väggarna."),
    ("Val av tapet", "Mönster, papper eller non-woven och antal rullar."),
    ("Underarbete", "Gammal tapet, spackling och slipning."),
    ("Grundning", "Vid bronstryck eller sugande väggar."),
    ("Uppsättning", "Våd för våd med mönsterpassning."),
    ("Avslut", "Lister tillbaka och genomgång."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Hägersten",
  "rot": [
    "Skatteverket räknar tapetsering som rotarbete, både i villor och radhus och i bostadsrätter. I en bostadsrätt ska arbetet göras innanför lägenhetens tak, väggar och golv och gälla något du ansvarar för enligt stadgarna. Hyresgäster får inget avdrag, eftersom avdraget gäller bostäder som köparen äger.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för tapetseringen i Hägersten?",
  "price": [
    "Väggytan, hur mycket gammal tapet och spackel som ska åtgärdas, om väggen behöver grundas, tapetens typ och mönsterpassning och antalet hörn och fönster i rummet. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag tapetsera min hyreslägenhet i Hägerstensåsen utan att fråga hyresvärden?",
     "Ja. Jordabalken ger hyresgäster rätt att tapetsera på egen bekostnad, men hyresvärden kan få ersättning om bruksvärdet minskar."),
    ("Varför släpper tapeten i min villa från 1930-talet i Mälarhöjden?",
     "Byggnadsvårdsföreningen skriver att väggar i hus från 1920–1950-talen underbehandlades med lim och krita, vilket kan ge dålig vidhäftning."),
    ("Kan ny tapet sättas på den gamla?",
     "Oftast ja, men bronstryck i den gamla tapeten kan slå igenom. Då grundas väggen med alkydfärg eller shellack först."),
    ("Får hyresgäster rotavdrag för tapetsering?",
     "Nej. Rotavdraget gäller arbete i en bostad som köparen äger."),
  ],
  "sources": [_VARSAM, _of("Mälarhöjden", "soderort/hagersten/malarhojden"), _of("Hägerstensåsen", "soderort/hagersten/hagerstensasen"),
              _of("Fruängen", "soderort/hagersten/fruangen"), _of("Västertorp", "soderort/hagersten/vastertorp"), _SBF_UNDERLAG, _JB, _SKV],
  "cta": ("Vill du tapetsera i Hägersten?", "Boka ett gratis platsbesök, så provar vi väggarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nytapetserat rum i en äldre villa med mönstrad tapet",
     "bedroom in a 1930s Swedish villa with newly hung pale green patterned wallpaper, white painted window with deep sill, wooden floor, empty room, soft daylight" + _SFX),
    ("Tapetrullar och verktyg på ett bord",
     "two rolls of patterned wallpaper, a wallpaper brush, a seam roller and a smoothing tool laid out on a pasting table in an empty room, daylight" + _SFX),
    ("Ljust flerfamiljshus med tegeltak bland tallar",
     "three-storey 1940s Swedish apartment buildings in light plaster with pitched tile roofs, set among pine trees on a hillside, footpath, summer daylight, no people" + _SFX),
  ],
},

# ------------------------------------------------------------------ KISTA
"tapetsering-kista.html": {
  "kind": "district", "service": "tapetsering", "ort": "Kista", "svc_label": "Tapetsering",
  "title": "Tapetsering i Kista – betongväggar och gips",
  "description": "Tapetsering i Kista: lägenheter och radhus från 1975–1980, betong- och gipsväggar, bostadsrätt eller hyresrätt, underarbete och rotavdrag.",
  "h1": "Tapetsering i Kista",
  "lead": "Kista byggdes 1975–1980. I hus från den tiden kan väggarna vara av betong, gips eller puts, som Byggnadsvårdsföreningen räknar till de lämpliga underlagen för tapet, men gamla tapetlager och hål behöver åtgärdas först. Geal Entreprenad AB tapetserar i lägenheter och radhus i Kista och anpassar underarbetet efter väggen.",
  "card": "Lägenheter och radhus från 1970-talet.",
  "sections": [
    {"id": "stadsdelen-kista", "anchor": "Stadsdelen",
     "h2": "En stadsdel med många lägenheter",
     "paras": [
       "Stadsmuseets Stockholms spår om Kista berättar att stadsdelen byggdes ut 1975–1980 på det gamla militära övningsområdet Järvafältet, med 2 500 lägenheter i flerbostadshus och omkring 780 småhus från början. Stadens områdesfakta för 2025 räknar i dag 7 893 bostäder i Kista: 3 981 bostadsrätter, 2 801 hyresrätter hos privata värdar och 629 i allmännyttan.",
       "Områdesfakta räknar också 1 604 specialbostäder och 721 lägenheter i flerbostadshus utan kök. Det är alltså en stadsdel med många mindre bostäder. Bland lägenheterna i flerbostadshus finns 1 391 tvåor, 1 761 treor och 854 fyror. Stockholms spår nämner också att Kista centrum invigdes 1977. Vi planerar arbetet så att du kan bo kvar under tiden.",
     ],
     "aside": {"title": "Kista 2025", "items": [
       "7 893 bostäder", "3 981 bostadsrätter", "2 801 privata hyresrätter", "721 lägenheter utan kök"]}},
    {"id": "underlag-kista", "h2": "Betong och gips som underlag",
     "paras": [
       "Byggnadsvårdsföreningen skriver att lämpliga underlag för tapeter i nya hus är gipsskivor, betong och puts, medan puts, timmer, spänd papp och spänd väv nämns för äldre hus. Väggar av de materialen går alltså bra att tapetsera på, men de behöver vara rena, släta och torra. Vassa korn och toppar från dålig slipning eller orent klister syns mer genom tapeten än åsar och fördjupningar, så underarbetet är det viktigaste.",
       "I ett svar om en 70-talslägenhet där den boende ville ta bort tapeten och låta betongen vara synlig skriver föreningen att betongväggarna inte självklart är så vackra som man tror, och att en opigmenterad silikatfärg kan strykas på så att betongen inte dammar. Vill du tvärtom tapetsera över en vägg som tidigare varit omålad betong spacklar och grundar vi först. Föreningen påpekar också att tapeter kan bukta sig vid uppsättningen, så vi låter varje våd vila och trycker ut luften innan nästa sätts upp.",
     ],
     "aside": {"title": "Underlag i nya hus", "items": [
       "Gipsskivor", "Betong", "Puts", "Rent, slätt och torrt"]}},
    {"id": "agarform-kista", "h2": "Bostadsrätt eller hyresrätt",
     "paras": [
       "I en bostadsrätt säger bostadsrättslagen att medlemmen håller lägenheten i gott skick om inte stadgarna säger något annat. Det är alltså stadgarna som avgör vem som ansvarar för väggarnas ytskikt. Tapetsering finns inte bland de åtgärder som lagen kräver styrelsens tillstånd för, så länge den inte är en väsentlig förändring eller påverkar särskilda kulturvärden.",
       "Bor du i hyresrätt ger jordabalken dig rätt att tapetsera på egen bekostnad. Försämrar arbetet lägenhetens bruksvärde kan hyresvärden kräva ersättning, så vi väljer underarbete och tapet som går att ta bort utan att väggen skadas.",
     ],
     "aside": None},
    {"id": "radhus-kista", "h2": "Radhusen i Kista och Akalla",
     "paras": [
       "Kista har 971 småhus enligt områdesfakta, varav 482 med äganderätt och 404 bostadsrätter. I ett radhus är det du som ägare eller föreningen enligt stadgarna som bestämmer, och arbetet kan omfatta flera rum och våningsplan.",
       "Byggnadsvårdsföreningen skriver att tapeter klarar många underlag, så länge luftfuktigheten inte blir för hög som i kök och badrum. I radhusens kök och badrum föreslår vi därför andra ytskikt än papperstapet. Mer om tjänsten finns under " + _L.format("malare-kista.html", "målare i Kista") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så tapetserar vi i Kista",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på väggarna."),
    ("Tapetval", "Typ, mönster och antal rullar."),
    ("Underarbete", "Gammal tapet bort, spackling och slipning."),
    ("Grundning", "Där väggen suger ojämnt."),
    ("Uppsättning", "Våd för våd, skarvarna rullas."),
    ("Avslut", "Eluttag och lister tillbaka."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Kista",
  "rot": [
    "Skatteverket räknar tapetsering som rotarbete i både småhus och bostadsrätter. I en bostadsrätt ska arbetet göras innanför lägenhetens tak, väggar och golv och gälla något du ansvarar för enligt stadgarna. Bor du i hyresrätt får du inget avdrag, eftersom det bara gäller bostäder som köparen äger.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för tapetseringen i Kista?",
  "price": [
    "Antal rum och väggytor, hur mycket som ska flyttas undan, hur många lager gammal tapet som ska bort, spackling av hål och skarvar, grundning, tapetens typ och mönster. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Går det att tapetsera direkt på betongväggarna i min lägenhet i Kista?",
     "Betong är ett lämpligt underlag enligt Byggnadsvårdsföreningen, men väggen ska vara ren, slät och torr, och ofta behöver den spacklas och grundas först."),
    ("Behöver jag styrelsens tillstånd för att tapetsera min bostadsrätt i Kista?",
     "Normalt inte. Tapetsering finns inte bland de åtgärder som bostadsrättslagen kräver tillstånd för, om den inte påverkar särskilda kulturvärden."),
    ("Hur många bostadsrätter finns det i Kista?",
     "Stadens områdesfakta räknar 3 981 bostadsrätter av 7 893 bostäder 2025, och 2 801 hyresrätter hos privata värdar."),
    ("Passar papperstapet i köket?",
     "Byggnadsvårdsföreningen skriver att luftfuktigheten kan bli för hög för tapet i kök och badrum."),
  ],
  "sources": [_SPAR_KISTA, _of("Kista", "vasterort/jarva/kista"), _SBF_UNDERLAG, _SBF_BETONG, _BRL12, _BRL7, _JB, _SKV],
  "cta": ("Vill du tapetsera i Kista?", "Boka ett gratis platsbesök, så tittar vi på väggarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nytapetserad vägg i en lägenhet från 1970-talet",
     "living room in a 1970s Swedish apartment with one wall newly covered in a subtle grey geometric wallpaper, white painted other walls, large window, parquet floor, empty room, daylight" + _SFX),
    ("Spacklad och slipad betongvägg före tapetsering",
     "close view of a smooth freshly filled and sanded concrete wall with pale grey filler patches, a wide filling knife resting on a step ladder, empty room, daylight" + _SFX),
    ("Radhus från slutet av 1970-talet",
     "late 1970s Scandinavian modernist terraced houses in a Stockholm suburb, dark brown vertical wood panel facades, low mono-pitch roofs, large plain white windows without bay windows, small front yards with bushes, car-free footpath, overcast daylight, no people" + _SFX),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"tapetsering-vallingby.html": {
  "kind": "district", "service": "tapetsering", "ort": "Vällingby", "svc_label": "Tapetsering",
  "title": "Tapetsering i Vällingby – väggar från 1950-talet",
  "description": "Tapetsering i Vällingby: väggar från 1950-talet med kridering eller sandspackel, gamla tapetlager, föreningens regler, hyresrätt och rotavdrag.",
  "h1": "Tapetsering i Vällingby",
  "lead": "Vällingby byggdes under 1950-talet, just när väggarna i nya hus började behandlas på ett annat sätt. Därför kan två lägenheter i samma stadsdel kräva helt olika underarbete. Geal Entreprenad AB tapetserar i lägenheter, radhus och kedjehus i Vällingby, Råcksta och Grimsta och provar väggen innan tapeten sätts upp.",
  "card": "Väggar från 1950-talet.",
  "sections": [
    {"id": "femtiotal-vallingby", "anchor": "1950-talet",
     "h2": "Byggt under 1950-talet",
     "paras": [
       "Översiktsplanens riksintressedel beskriver Vällingby–Råcksta som landets första ABC-stad, utbyggd under 1950-talet och ett sammanhållet uttryck för det årtiondet. Byggnadsvårdsföreningen skriver att dålig vidhäftning kan befaras i hus från 1920–1950-talen, då väggarna underbehandlades med lim och krita, så kallad kridering, och att sandspackel började användas som underlag vid mitten av 1950-talet.",
       "Stadens vägledning Varsam utveckling av småhus- och villaområden berättar att Vällingby invigdes 1954 och lyfter fram radhusområdena Atlantis och Omega som kulturhistoriskt synnerligen värdefulla. Ett hus från början av årtiondet kan alltså ha krita under tapeten, medan ett hus från slutet har sandspackel. Vi tar ner en bit av den gamla tapeten och provar ytan innan vi föreslår underarbete. Släpper väggen behöver den förbehandlas, annars kan den nya tapeten lossna.",
     ],
     "aside": {"title": "Väggarna enligt Byggnadsvårdsföreningen", "items": [
       "Kridering 1920–1950-tal", "Sandspackel från mitten av 1950-talet", "Prov innan tapetsering", "Förbehandling vid behov"]}},
    {"id": "boende-vallingby", "h2": "Bostadsrätt, hyresrätt eller radhus",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 2 076 bostadsrätter i Vällingby, 1 498 lägenheter i allmännyttan och 597 hos privata hyresvärdar, och 220 småhus med äganderätt. I Råcksta finns 1 551 bostadsrätter och över 3 000 hyresrätter, och i Grimsta är 1 525 av 2 338 bostäder allmännyttiga.",
       "Hyresgäster har enligt jordabalken rätt att tapetsera på egen bekostnad, men hyresvärden kan kräva ersättning om lägenhetens bruksvärde minskar. I en bostadsrätt är det stadgarna som avgör vem som ansvarar för väggarnas ytskikt. I småhusen med äganderätt bestämmer du själv, och där kan arbetet omfatta hela huset.",
     ],
     "aside": {"title": "Vällingby, Råcksta, Grimsta 2025", "items": [
       "Vällingby: 2 076 bostadsrätter", "Råcksta: 1 551 bostadsrätter", "Grimsta: 1 525 i allmännyttan", "Vällingby: 220 småhus med äganderätt"]}},
    {"id": "kultur-vallingby", "h2": "När lägenheten har kulturvärden",
     "paras": [
       "Bostadsrättslagen säger att det för en lägenhet med särskilda historiska, kulturhistoriska, miljömässiga eller konstnärliga värden krävs styrelsens tillstånd för varje åtgärd som påverkar ett sådant värde. Riksintressedelen för Vällingby–Råcksta räknar upp detaljer på husens utsida, men en lägenhet kan ha till exempel en bevarad tapet eller fast inredning som föreningen vill behålla.",
       "Finns en äldre tapet kvar som kan vara värdefull frågar vi föreningen innan den tas ner. Ibland går det att låta den sitta kvar under den nya, eftersom Byggnadsvårdsföreningen skriver att det oftast går bra att tapetsera på gamla tapeter. Bronstryck kan dock slå igenom, och då grundas väggen med alkydfärg eller shellack.",
     ],
     "aside": None},
    {"id": "underarbete-vallingby", "h2": "Underarbetet avgör resultatet",
     "paras": [
       "Byggnadsvårdsföreningen påpekar att vassa korn och toppar från dålig slipning eller orent klister syns mer genom tapeten än åsar och fördjupningar. Vi slipar därför varje spacklad yta och torkar av väggen innan klistret stryks. Tapeten kan bukta sig vid uppsättningen, och därför låter vi varje våd vila enligt tillverkarens anvisning.",
       "Föreningen rekommenderar också att man köper en extra rulle om tapeten är av en äldre typ som kan försvinna ur sortimentet. Mer om tjänsten finns under " + _L.format("malare-vallingby.html", "målare i Vällingby") + ", och för golven finns " + _L.format("golvslipning-vallingby.html", "golvslipning i Vällingby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så tapetserar vi i Vällingby",
  "steps": [
    ("Platsbesök", "Gratis besök, prov av väggen under tapeten."),
    ("Föreningen", "Vid äldre tapeter eller fast inredning."),
    ("Underarbete", "Nedtagning, spackling och slipning."),
    ("Förbehandling", "Där väggen kriderats eller bronstryck finns."),
    ("Uppsättning", "Våd för våd med mönsterpassning."),
    ("Avslut", "Lister och eluttag tillbaka."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Vällingby",
  "rot": [
    "Skatteverket räknar tapetsering som rotarbete i villor, radhus och bostadsrätter. I en bostadsrätt ska arbetet göras innanför lägenhetens tak, väggar och golv och gälla något du ansvarar för enligt stadgarna. Hyresgäster får inget rotavdrag.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för tapetseringen i Vällingby?",
  "price": [
    "Väggytan och antalet rum, hur många lager tapet som ska bort, om väggen behöver förbehandlas efter kridering, spackling, tapetens typ och mönsterpassning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför fäster inte ny tapet på väggen i min lägenhet från 1950-talet i Vällingby?",
     "Byggnadsvårdsföreningen skriver att väggar från 1920–1950-talen ofta behandlades med lim och krita, som ger dålig vidhäftning."),
    ("Måste styrelsen godkänna att jag tapetserar om i Råcksta?",
     "Normalt inte, men har lägenheten särskilda kulturhistoriska värden krävs tillstånd för åtgärder som påverkar dem."),
    ("Får jag tapetsera min hyreslägenhet i Grimsta?",
     "Ja, jordabalken ger hyresgäster rätt att tapetsera på egen bekostnad. Hyresvärden kan få ersättning om bruksvärdet minskar."),
    ("När började man använda sandspackel på väggarna?",
     "Enligt Byggnadsvårdsföreningen vid mitten av 1950-talet, alltså under samma årtionde som Vällingby byggdes."),
  ],
  "sources": [_RIKS, _VARSAM, _of("Vällingby", "vasterort/hasselby-vallingby/vallingby"), _of("Råcksta", "vasterort/hasselby-vallingby/racksta"),
              _of("Grimsta", "vasterort/hasselby-vallingby/grimsta"), _SBF_UNDERLAG, _BRL7, _JB, _SKV],
  "cta": ("Vill du tapetsera i Vällingby?", "Boka ett gratis platsbesök, så provar vi väggen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Rum i en 1950-talslägenhet med ny tapet",
     "room in a 1950s Swedish apartment with newly hung wallpaper in a small mid-century pattern in warm yellow tones, white painted door and window, light wooden floor, empty room, daylight" + _SFX),
    ("Gammal tapet som tagits ner i en remsa",
     "close view of a wall where a strip of old faded floral wallpaper has been peeled away revealing a chalky white surface underneath, a scraper resting on the skirting, daylight" + _SFX),
    ("Punkthus och lamellhus från 1950-talet",
     "1950s Swedish suburban housing with a tall brick point block and lower light plastered apartment buildings among lawns and birch trees, footpath, overcast daylight, no people" + _SFX),
  ],
},
}
