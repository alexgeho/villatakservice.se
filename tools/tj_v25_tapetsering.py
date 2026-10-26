# -*- coding: utf-8 -*-
"""Tapetsering – ortsidor v25: Upplands Väsby, Vallentuna, Värmdö, Älvsjö, Östermalm, Österåker (2026-10-26).
Deltjänst under malare.html (TJ_HUB["tapetsering"]). Intent: tapet inomhus – underlag, gamla lager och tapettyp –
skild från ortens malare-<ort>.html (fasad, kulör, lov) och från v15/v17/v18/v19-sidorna (tapetlager och styrelsen,
kridering, tapettyper, kallställda hus, gips och förlimning, tapet efter epok, tretex/masonit, spara och datera,
pappspänt innertak, timmer och lerklining, snedtak, asbest, laga spännpapp, skivväggar, putsväggar, schablonmålning,
trästaden, fritidshusens kyla, hyresgästens rätt, ett lager till, kant-i-kant, kakelugn, lister och mönsterpassning).
Tre bilder per sida: img[0] hero 4:3, img[1]–[2] 3:2.

Lokal vinkel per sida (en huvudfråga per sida):
Upplands Väsby – 1960–70-talens radhus och kedjehus i de östra kommundelarna (kommunens kunskapsunderlag:
  Sjukyrkoberget, Skälby, Fresta, Odenslunda), strukturtapeter av plast som kan flossas, vävtapet och underlaget,
  varsamhet även invändigt.
Vallentuna – Roslagsbanan 1885 och stationssamhällenas villor (ÖP 2040), spännpapp och makulatur som underlag,
  att klistra våden, non-woven och papperstapet.
Värmdö – skärgårdens gårdar och Beatelunds målade tapeter från 1730-talet (kulturmiljöprogrammet), tapetlagren som
  kulturlager: riva, bygga in, skära ut ett fält, tapetpärm, buckliga tapeter och spännpapp.
Älvsjö – Älvsjö villastad (municipalsamhälle, Hallmans stadsplan, kulturhistoriskt värdefull miljö enligt Varsam),
  bårder och dekor som skrapas fram, linoljefärg som gulnar i mörker, lokala målare och museet.
Östermalm – stenstadens bostadsrätter (områdesfakta Hedvig Eleonora och Oscar), förvanskningsförbudet gäller även
  interiört, bostadsrättshavarens ansvar för det inre (BRL 7 kap. 12 §), ROT i bostadsrätten.
Österåker – Svinninges sommarvillor som blivit åretruntbostäder (kulturmiljöprogrammet: drygt 60 % bebodda året
  runt, grosshandlarvillor i Nantes, 1930-talets fritidshus), täta tapeter och uppvärmning, varsamhetskravet invändigt.

Fakta endast från källorna i respektive 'sources', öppnade med urllib (Mozilla-UA) 2026-10-26, alla 200;
byggnadsvard.se via sajtens WP-API (bara öppen text); pdf:erna har textlager (pdftotext -layout).
Skatteverkets två sidor svarade inte härifrån (anslutningen bröts) – samma URL:er och samma formulering om ROT som på
sajtens tidigare tapetseringssidor.
Strukna / ej använda: företagsnamn för handtryckta tapeter (SBF-svar), priser, tider, garantier, omdömen, egna uppdrag
i orterna, påståenden om vilka tapeter som sitter i enskilda områden (ingen källa).
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no hands, no text, no letters"

_SBF = "https://byggnadsvard.se/"
def _sbf(title, slug):
    return ("Svenska Byggnadsvårdsföreningen – " + title, _SBF + slug + "/")

_SBF_STRUKT = _sbf("Hur gör vi med gamla strukturtapeter av plast?", "hur-gor-vi-med-gamla-strukturtapeter-av-plast")
_SBF_VAV = _sbf("Vävtapet", "vavtapet")
_SBF_MAKUL = _sbf("Vad är makulatur och hur arbetar man med den?", "vad-ar-makulatur-och-hur-arbetar-man-med-den")
_SBF_PAPP = _sbf("Väggytskikt av papp?", "vaggytskikt-av-papp")
_SBF_RIVA = _sbf("Riva ner tapeter eller inte?", "riva-ner-tapeter-eller-inte")
_SBF_BARD = _sbf("Handmålad bård", "handmalade-bard")
_SBF_DEKOR = _sbf("Dekorativ puts i lägenhet?", "dekorativ-puts-i-lagenhet")
_SBF_MODERN = _sbf("Tapetsera med modern tapet i gammalt hus?", "tapetsera-med-modern-tapet-i-gammalt-hus")

_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_VASBY_KU = ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö i Upplands Väsby (pdf)",
             "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf")
_VALL_OP = ("Vallentuna kommun – Översiktsplan 2040 (pdf)",
            "https://vallentuna.se/download/18.63572f8619eeecafce08366/1782478377449/2.11.7%20%C3%96versiktsplan%202040.pdf")
_VARMDO_KMP = ("Värmdö kommun – Värmdö, kulturhistoria i skärgårdsbygd (kulturmiljöprogram, pdf)",
               "https://www.varmdo.se/download/18.7faa473e19913ae5e0f1f12/1757318877718/Kulturmilj%C3%B6v%C3%A5rdsprogrammet%20V%C3%A4rmd%C3%B6_2.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
           "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/stadsmuseets-kulturhistoriska-klassificering/")
_BV_FORV = ("Boverket – Förvanskningsförbudet (PBL kunskapsbanken)",
            "https://www.boverket.se/sv/PBL-kunskapsbanken/teman/kulturvarden/kulturvarden-i-plan---och-bygglagen/krav-pa-byggnadsverk-och-tomter/forvanskningsforbudet/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614)",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_OST_KMP = ("Österåkers kommun – Kulturmiljöprogram för Svinninge (pdf)",
            "https://www.osteraker.se/download/18.367d658917909e8fc2bc760/1632320809578/kulturmiljoprogram_Svinninge.pdf")
_OST_KULT = ("Österåkers kommun – Kulturhistoriska byggnader, kulturmiljöer",
             "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/bygglovsguiden/kulturhistoriskabyggnaderkulturmiljoer.4.367d658917909e8fc2bb42.html")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
            "tillsammans med rutavdrag. Tapet, klister och resor ger inget avdrag.")

PAGES_TJ = {

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"tapetsering-upplands-vasby.html": {
  "kind": "district", "service": "tapetsering", "ort": "Upplands Väsby", "svc_label": "Tapetsering",
  "title": "Tapetsering i Upplands Väsby – radhusen och plasttapeten",
  "description": "Tapetsering i Upplands Väsby: 1960- och 70-talens radhus och kedjehus, strukturtapeter av plast som kan flossas, vävtapet och ett slätt underlag.",
  "h1": "Tapetsering i Upplands Väsby",
  "lead": "En stor del av småhusen i Upplands Väsby är radhus och kedjehus från 1960- och 70-talet, och många av dem har bytt tapet flera gånger sedan dess. Geal Entreprenad AB tapetserar i radhus, kedjehus och villor i Upplands Väsby och börjar med att ta reda på vad som sitter på väggen i dag.",
  "card": "Radhusen och plasttapeten.",
  "sections": [
    {"id": "radhusen-vasby", "anchor": "Radhusen i Väsby",
     "h2": "Radhus och kedjehus från rekordåren",
     "paras": [
       "Kommunens kunskapsunderlag för kulturmiljö beskriver hur de östra kommundelarna växte fram med en stor andel småhus och radhus. Husen ligger i separata grupper längs säckgator, med bilfria gångstråk som binder ihop dem. Som exempel nämns Sjukyrkoberget, Skälby, Fresta och Odenslunda, men också Apoteksskogen i de centrala delarna.",
       "Arkitekturen är rationell: enkla volymer i en eller två våningar, platta eller flacka tak och enluftsfönster utan spröjs. Utvändigt dominerar rött tegel, vitt kalkcementtegel och målad träpanel i färgstarka kulörer. Inomhus kan ett hus från den tiden ha fått ny tapet flera gånger, och väggarna kan då bära spår av flera decenniers val.",
     ],
     "aside": {"title": "Exempel i kunskapsunderlaget", "items": [
       "Sjukyrkoberget", "Skälby", "Fresta", "Odenslunda", "Apoteksskogen"]}},
    {"id": "plasttapeten-vasby", "h2": "Strukturtapet av plast",
     "paras": [
       "Hittar du en strukturtapet av plast på väggen finns det ett enkelt första steg. Svenska Byggnadsvårdsföreningen påpekar att de oftast var flossbara: det yttersta skiktet går att dra loss, och då får man en slätare yta att arbeta vidare med. Går det inte får man försöka få bort så mycket som möjligt.",
       "Nästa fråga är vad tapeten sitter på. Det kan vara skivor som tretex eller masonit, och då avgör skivornas skick hur vi går vidare. Om huset hålls uppvärmt året runt kan plasttapeten enligt föreningen i princip få sitta kvar under ett nytt skikt, även om man gärna undviker plast i äldre hus.",
     ],
     "aside": None},
    {"id": "vavtapet-vasby", "anchor": "Vävtapet",
     "h2": "Väv eller papper över den gamla tapeten",
     "paras": [
       "Många väljer en målningsbar väv för att få en tålig yta i hall och trappa. Byggnadsvårdsföreningen svarar kort på frågan om vad man ska tänka på när väven sätts över en äldre tapet: inget mer än att underlaget är slätt och fast, precis som vid målning eller tapetsering.",
       "Det låter enkelt, men det är just underlaget som tar tiden. Lösa kanter limmas eller skärs bort, skarvar som reser sig slipas ner och hål spacklas. Först när väggen är fast och jämn går vi vidare med väv, papperstapet eller en mönstrad tapet.",
     ],
     "aside": {"title": "Underlaget före ny tapet", "items": [
       "Lösa kanter limmas eller skärs bort", "Upphöjda skarvar slipas", "Hål och sprickor spacklas", "Hela ytan ska vara fast"]}},
    {"id": "varsamt-vasby", "h2": "Varsamt även inomhus",
     "paras": [
       "Kunskapsunderlaget påminner om att varsamhetskravet i plan- och bygglagen gäller vid såväl exteriöra som interiöra ändringar. För de flesta rum i ett radhus betyder det inget mer än att man tänker sig för, men fasta detaljer som originalsnickerier, inbyggda skåp och dörrar är en del av husets karaktär.",
       "Vi tejpar och skyddar sådana delar i stället för att plocka ner dem i onödan. Om husen och kulörerna i Väsby utvändigt kan du läsa under " + _L.format("malare-upplands-vasby.html", "målare i Upplands Väsby") + ".",
     ],
     "aside": None},
    {"id": "tapetvalet-vasby", "h2": "Vilken tapet passar huset?",
     "paras": [
       "I ett radhus från 1960- och 70-talet är rummen ofta ljusa och enkla, med stora fönster mot trädgården. En tapet med lugnt mönster eller en enfärgad väv brukar fungera, men valet är ditt. Vi hjälper till med åtgången och med hur mönstret ska placeras på väggar med fönster och dörrar.",
       "Ska golven göras samtidigt är det bra att tapetsera först och slipa sedan, eller skydda väggarna noga. Om golvslipning i Väsby kan du läsa under " + _L.format("golvslipning-upplands-vasby.html", "golvslipning i Upplands Väsby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen i Upplands Väsby till",
  "steps": [
    ("Platsbesök", "Vi tittar på väggarna och provar om den gamla tapeten går att flossa."),
    ("Skriftligt kostnadsförslag", "Rum för rum, med underarbete och tapetsering var för sig."),
    ("Skydd", "Golv, lister och snickerier täcks innan arbetet börjar."),
    ("Underarbete", "Gamla lager tas ner eller fästs, skarvar slipas och hål spacklas."),
    ("Tapetsering", "Våderna sätts i lod med mönstret passat."),
    ("Genomgång", "Vi går igenom rummen och sparar restbitar för lagning."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Upplands Väsby",
  "rot": [
    "Skatteverket räknar tapetsering inomhus som rotarbete i den bostad du äger och själv använder, både i villa, radhus och bostadsrätt.",
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Upplands Väsby?",
  "price": [
    "Antalet rum, om plasttapeten går att flossa eller måste rivas och hur mycket väggarna behöver jämnas. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi tapetsera direkt på strukturtapeten i vårt radhus i Väsby?",
     "Oftast är det bättre att flossa av det yttersta plastskiktet först. Då blir ytan slätare, och den nya tapeten får ett fastare underlag."),
    ("Gäller kommunens kulturmiljöråd även inne i huset?",
     "Varsamhetskravet i plan- och bygglagen gäller både utvändigt och invändigt, enligt kommunens kunskapsunderlag. Ny tapet kräver inget lov, men fasta originaldetaljer bör tas om hand."),
    ("Vad krävs för att sätta väv på en gammal tapet?",
     "Att underlaget är slätt och fast. Lösa kanter och upphöjda skarvar åtgärdas innan väven sätts upp."),
    ("Får vi rotavdrag för tapetseringen?",
     "Ja, för arbetskostnaden i en bostad du äger och själv använder. Tapet och klister ger inget avdrag."),
  ],
  "sources": [_VASBY_KU, _SBF_STRUKT, _SBF_VAV, _SKV, _SKV2],
  "cta": ("Ska radhuset i Upplands Väsby få ny tapet?", "Boka ett gratis platsbesök, så tittar vi på väggarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Låga radhus i tegel och grönmålad träpanel längs en gångväg",
     "row of low one-storey 1970s Scandinavian terraced houses with completely flat roofs and a thick horizontal fascia board, walls of red brick combined with dark green painted horizontal wooden panel, large single-pane windows without glazing bars, small fenced patios, car-free gravel footpath with birch trees, modernist Swedish suburb, no chimneys, summer" + _IMG_END),
    ("Vägg där det yttersta skiktet av en strukturtapet har dragits loss",
     "close view of an interior wall where the top vinyl layer of an old embossed structure wallpaper has been peeled off in a long strip, revealing a smooth paper backing underneath, scraper resting on a dust sheet, daylight" + _IMG_END),
    ("Nytapetserat vardagsrum med enfärgad väv och stort fönster",
     "bright living room in a 1970s Swedish terraced house with freshly hung plain light textile wallpaper, large window towards a garden, light oak floor, simple furniture, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VALLENTUNA
"tapetsering-vallentuna.html": {
  "kind": "district", "service": "tapetsering", "ort": "Vallentuna", "svc_label": "Tapetsering",
  "title": "Tapetsering i Vallentuna – spännpapp och papperstapet",
  "description": "Tapetsering i Vallentuna: villorna i Roslagsbanans stationssamhällen, spännpapp och makulatur som underlag och valet mellan non-woven och papper.",
  "h1": "Tapetsering i Vallentuna",
  "lead": "När Roslagsbanan öppnade 1885 växte stationssamhällen med villor fram i Vallentuna, och i många av de äldre husen sitter tapeterna på papp i stället för på skivor. Geal Entreprenad AB tapetserar i villor och radhus i Vallentuna och anpassar underlaget efter väggen som finns.",
  "card": "Spännpapp och papperstapet.",
  "sections": [
    {"id": "villorna-vallentuna", "anchor": "Stationsvillorna",
     "h2": "Villorna längs Roslagsbanan",
     "paras": [
       "Vallentunas översiktsplan beskriver hur den nya tiden började 1885 med Roslagsbanans invigning mellan Stockholm och Rimbo. Banan byggdes för att försörja Stockholm med jordbruksprodukter, och kring stationerna växte samhällen med villabebyggelse fram.",
       "I dag är småhusen i majoritet. Enligt översiktsplanen fanns det 2017 drygt 13 000 bostäder i kommunen, och omkring 65 procent av dem var småhus. Spannet är stort, från tidiga stationsvillor till nya hus i tätorterna, och väggarna inomhus ser olika ut beroende på när huset byggdes.",
     ],
     "aside": {"title": "Vallentuna enligt översiktsplanen", "items": [
       "Roslagsbanan invigd 1885", "Drygt 13 000 bostäder 2017", "Omkring 65 procent småhus"]}},
    {"id": "spannpapp-vallentuna", "h2": "Spännpapp och makulatur",
     "paras": [
       "Svenska Byggnadsvårdsföreningen förklarar att makulatur är ett samlingsnamn för restpapper, allt från tidningspapper och enklare förpackningspapper till spännpapp. Spännpapp är ett traditionellt underlag för tapeter som blev vanligt under 1800-talet, och den ger en mer levande yta än gips eller andra moderna skivor.",
       "Pappspänning var ursprungligen ett sätt att få släta väggar och samtidigt täta mot drag, och tidningspapper var en vanlig makulatur eftersom det var billigt. Hittar vi papp och tidningsark längst in under tapetlagren är det alltså inget fel, utan ofta husets ursprungliga lösning.",
     ],
     "aside": {"title": "Underlag i äldre hus", "items": [
       "Spännpapp på panel", "Makulaturpapp under tapeten", "Tidningspapper som makulatur", "Senare skivor som tretex"]}},
    {"id": "nyspann-vallentuna", "h2": "Ny papp eller laga den gamla",
     "paras": [
       "Förr limmade man ihop spännpappsvåderna med benlim i överlappningen, fuktade väggfältet och spikade upp det. Byggnadsvårdsföreningen avråder från att göra så om man inte har erfarenhet, eftersom det är lätt att det blir fel och inte så snyggt.",
       "Därför börjar vi med att se om den befintliga pappen går att behålla. Sitter den fast och väggen är torr lagar vi revor och lösa partier. Är skivor bakom pappen porösa kan det vara tecken på att väggen varit fuktig i perioder, och då vill vi förstå orsaken innan det tapetseras.",
     ],
     "aside": None},
    {"id": "tapettyp-vallentuna", "anchor": "Non-woven eller papper",
     "h2": "Non-woven eller papperstapet",
     "paras": [
       "Non-woven är en tapet med plast i materialet. Byggnadsvårdsföreningen skriver att erfarenheterna är delade: vissa anser att det kan bildas mögel bakom tapeten, medan tillverkarna hävdar att ångmotståndet inte är sämre än för papperstapeter. Oberoende forskning saknas.",
       "Föreningen rekommenderar att man klistrar våderna och inte väggen när man tapetserar på papp. I ett äldre hus med spännpapp väljer vi därför oftast papperstapet. I nyare rum med gipsväggar avgör oftast mönster och tålighet valet.",
     ],
     "aside": None},
    {"id": "rummen-vallentuna", "h2": "Rum för rum",
     "paras": [
       "I en äldre villa skiljer sig rummen ofta åt. Ett rum kan ha papp på panel, ett annat skivor från en senare renovering och köket kakel eller målad vägg. Vi går igenom varje rum för sig och skriver in i kostnadsförslaget vilket underlag som gäller var. Då vet du i förväg vilka väggar som behöver mer förarbete och varför, och kan själv välja var en enklare lösning räcker.",
       "Ska fasaden eller fönstren också ses över kan du läsa om det under " + _L.format("malare-vallentuna.html", "målare i Vallentuna") + " och " + _L.format("fonsterrenovering-vallentuna.html", "fönsterrenovering i Vallentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen i Vallentuna till",
  "steps": [
    ("Platsbesök", "Vi tittar på underlaget i varje rum och lyfter en hörnbit där det går."),
    ("Skriftligt kostnadsförslag", "Underarbete, papp och tapetsering står för sig per rum."),
    ("Skydd", "Golv, lister och fönster täcks."),
    ("Underlaget", "Papp lagas eller kompletteras, skivor fästs och skarvar jämnas."),
    ("Tapetsering", "Våderna klistras och sätts upp i lod."),
    ("Genomgång", "Vi går igenom rummen och lämnar restbitar."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Vallentuna",
  "rot": [
    "Skatteverket räknar tapetsering inomhus som rotarbete i den bostad du äger och själv använder.",
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Vallentuna?",
  "price": [
    "Hur mycket papp och gamla lager som behöver lagas, antalet rum och tapettypen. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vi hittade tidningspapper under tapeterna i vår villa i Vallentuna – är det ett problem?",
     "Nej, tidningspapper var en vanlig makulatur eftersom det var billigt. Sitter det fast kan det ofta vara kvar under den nya tapeten."),
    ("Kan vi spika upp ny spännpapp själva?",
     "Byggnadsvårdsföreningen avråder om man saknar erfarenhet, eftersom det lätt blir fel. Det är oftast enklare att laga den papp som finns."),
    ("Ska vi välja non-woven eller papperstapet?",
     "På spännpapp i ett äldre hus väljer vi oftast papper. Erfarenheterna av non-woven på sådana väggar är delade och oberoende forskning saknas."),
    ("Ska klistret på väggen eller på våden?",
     "Byggnadsvårdsföreningen rekommenderar att klistra våderna och inte väggen när man tapetserar."),
    ("Våra skivor bakom tapeten smular – vad betyder det?",
     "Porösa skivor kan vara ett tecken på att väggen varit fuktig i perioder. Orsaken bör utredas innan det tapetseras."),
  ],
  "sources": [_VALL_OP, _SBF_MAKUL, _SBF_PAPP, _SKV, _SKV2],
  "cta": ("Ska villan i Vallentuna tapetseras?", "Boka ett gratis platsbesök, så går vi igenom underlaget i varje rum innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre gul trävilla med glasveranda och stor trädgård",
     "early 1900s Swedish wooden villa painted light yellow with white trim and a glazed veranda, large garden with old apple trees, small railway line visible in the background, Roslagen countryside, summer" + _IMG_END),
    ("Brun papp som delvis lossnat från en målad panelvägg",
     "close view of an old interior wall where layers of wallpaper have been partly removed, revealing brown stretched paper lining and yellowed newspaper sheets underneath on wooden panel, scraper on the floor, daylight" + _IMG_END),
    ("Papperstapet med blommönster på väggen i ett ljust rum",
     "bright room in an old Swedish villa with freshly hung paper wallpaper with a small floral pattern, white painted window frame and skirting board, wooden floorboards, soft daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VÄRMDÖ
"tapetsering-varmdo.html": {
  "kind": "district", "service": "tapetsering", "ort": "Värmdö", "svc_label": "Tapetsering",
  "title": "Tapetsering på Värmdö – riva eller spara tapetlagren",
  "description": "Tapetsering på Värmdö: skärgårdsgårdarnas tapeter, Beatelunds målade tapeter, att riva eller bygga in gamla lager, tapetpärmen och buckliga väggar.",
  "h1": "Tapetsering på Värmdö",
  "lead": "I skärgårdens gårdar och sommarhus kan det sitta tapetlager från många generationer, och ibland är de det enda som berättar hur rummen en gång såg ut. Geal Entreprenad AB tapetserar i hus på Värmdö och hjälper dig att bestämma vad som ska rivas, sparas eller byggas in.",
  "card": "Riva eller spara tapetlagren.",
  "sections": [
    {"id": "skargarden-varmdo", "anchor": "Skärgårdens hus",
     "h2": "Kulturhistoria i skärgårdsbygd",
     "paras": [
       "Värmdö kommuns kulturmiljöprogram, Värmdö – Kulturhistoria i skärgårdsbygd, beskriver kommunens bästa kulturmiljöer, från förhistoriska gravfält och skärgårdsbyar till bruksmiljöer och villasamhällen. Programmet ges nu ut i en tredje upplaga.",
       "Ett exempel på hur mycket en interiör kan bära är Beatelund. Programmet berättar att gårdens målade tapeter från 1730-talet såldes på auktion 1917 men köptes tillbaka av ägaren Sten Westerberg på 1930-talet, då gården restaurerades. Få hus har sådana tapeter, men principen gäller även ett enklare torp: lagren på väggen är en del av husets historia.",
     ],
     "aside": {"title": "Beatelund enligt programmet", "items": [
       "Herrgårdsbyggnader från 1720-talet", "Målade tapeter från 1730-talet", "Sålda på auktion 1917", "Återköpta på 1930-talet"]}},
    {"id": "kulturlager-varmdo", "h2": "Tapetlagren som kulturlager",
     "paras": [
       "Svenska Byggnadsvårdsföreningen beskriver tapetlagren som en form av kulturlager som kan berätta om husets historia. I ett hus med intressanta kulturhistoriska värden kan många tycka att det är ett ansvar att ta hand om lagren för kommande generationer.",
       "Bygger man in lagren bakom nya skivor kan de i sämsta fall glömmas bort helt och i bästa fall återupptäckas längre fram. Under tiden bidrar de lite till husets isolering. Det är ett val, inte ett fel, och vi tar det tillsammans med dig innan arbetet börjar. Ofta landar det i en blandning: lagren sparas i ett rum och tas ner i ett annat.",
     ],
     "aside": None},
    {"id": "spara-varmdo", "anchor": "Spara ett prov",
     "h2": "Spara ett prov innan du river",
     "paras": [
       "Ett vanligt sätt att ta vara på vackra tapeter är enligt föreningen att skära ut ett fält, lösa upp lagren och rama in dem i kronologisk ordning. Lagren löses med blött tidningspapper runt fältet och en plastpåse runt paketet i ett dygn. Var försiktig, eftersom limfärg är vattenlöslig.",
       "Man kan också samla proverna i en tapetpärm eller lägga några hela våder av tapetpaketet på vinden. Hela våder får med sig bårder, hela mönster och andra spår som kan intressera den som forskar om huset i framtiden.",
     ],
     "aside": {"title": "Sätt att spara lagren", "items": [
       "Inramat fält i kronologisk ordning", "Tapetpärm", "Hela våder på vinden", "Lagren kvar bakom nya skivor"]}},
    {"id": "buckligt-varmdo", "h2": "Buckliga tapeter och spännpapp",
     "paras": [
       "Lite buckliga tapeter kan vara en del av husets karaktär. Föreningen förklarar att det ofta beror på att spännpappen innerst mot väggen har töjts av åratal med växlande fukt och rörelser i huset. Tekniskt är det normalt inget problem, men det kan bli en estetisk fråga.",
       "Väljer du att ta bort allt och börja om finns två vägar enligt föreningen: ny spännpapp eller att limma upp tapeterna. Spännpapp döljer grövre underlag och ger ett skarvlöst underlag utan spackling. Är lerkliningen i gott skick kan den förlimmas, eller så klistras makulaturpapp upp innan papperstapeten sätts.",
     ],
     "aside": None},
    {"id": "vintern-varmdo", "h2": "Huset på vintern",
     "paras": [
       "Används huset bara delar av året är det viktigt att veta. Byggnadsvårdsföreningen avråder från att kallställa ett hus med moderna, täta tapeter eftersom det kan leda till mögel i väggen. En liten grundvärme året om hjälper materialen att hålla sig torra.",
       "Står huset kallt på vintern väljer vi därför papperstapet och undviker täta skikt. Om fasaden och utvändig målning på Värmdö kan du läsa under " + _L.format("malare-varmdo.html", "målare på Värmdö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen på Värmdö till",
  "steps": [
    ("Platsbesök", "Vi tittar på lagren och på hur huset värms under vintern."),
    ("Beslut om lagren", "Riva, spara prover eller bygga in – vi bestämmer det tillsammans."),
    ("Skriftligt kostnadsförslag", "Underarbete och tapetsering står för sig per rum."),
    ("Underlaget", "Papp lagas, ny makulatur sätts upp eller väggen förlimmas."),
    ("Tapetsering", "Papperstapeten sätts upp med mönstret passat."),
    ("Genomgång", "Vi lämnar restbitar och eventuella sparade prover."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering på Värmdö",
  "rot": [
    "Skatteverket räknar tapetsering inomhus som rotarbete, både i permanentbostaden och i ett fritidshus som du äger och själv använder.",
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Värmdö?",
  "price": [
    "Hur många lager som ska ner, om prover ska sparas och vilket underlag väggarna behöver. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur sparar vi de gamla tapeterna i vårt skärgårdshus på Värmdö?",
     "Skär ut ett fält och lös upp lagren med blött tidningspapper och en plastpåse i ett dygn, eller lägg hela våder på vinden. Var försiktig med limfärg, som är vattenlöslig."),
    ("Är det fel att bygga in de gamla tapeterna bakom skivor?",
     "Nej, det är ett val. Lagren finns kvar och bidrar lite till isoleringen, men risken är att de glöms bort."),
    ("Varför är tapeterna buckliga?",
     "Ofta har spännpappen innerst töjts av växlande fukt och rörelser i huset. Det är normalt inget tekniskt problem."),
    ("Vilken tapet passar i ett hus som står kallt på vintern?",
     "Papperstapet. Byggnadsvårdsföreningen avråder från att kallställa ett hus med täta tapeter eftersom det kan leda till mögel i väggen."),
  ],
  "sources": [_VARMDO_KMP, _SBF_RIVA, _SKV, _SKV2],
  "cta": ("Ska huset på Värmdö få ny tapet?", "Boka ett gratis platsbesök, så går vi igenom tapetlagren innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Röd skärgårdsgård med vita knutar vid en vik",
     "old red wooden farmhouse with white corners and a red clay tile roof on a rocky shore by a calm bay in the Stockholm archipelago, pine trees, small wooden jetty, summer evening light" + _IMG_END),
    ("Avriven tapet som visar flera äldre tapetlager i olika mönster",
     "close view of an old plastered interior wall where the newest wallpaper has been torn away in an irregular patch, revealing underneath several older wallpaper layers with different faded floral and striped patterns, edges of each layer visible like steps, brown paper lining at the bottom, soft daylight" + _IMG_END),
    ("Inramade tapetprover i kronologisk ordning på en vägg",
     "row of small wooden frames hanging on a white wall, each containing a sample of a different antique wallpaper pattern arranged from oldest to newest, simple interior of an old Swedish house, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"tapetsering-alvsjo.html": {
  "kind": "district", "service": "tapetsering", "ort": "Älvsjö", "svc_label": "Tapetsering",
  "title": "Tapetsering i Älvsjö – bårder och dekor i villastaden",
  "description": "Tapetsering i Älvsjö: villastaden från municipalsamhällets tid, bårder och målad dekor som skrapas fram och linoljefärg som gulnar i mörker.",
  "h1": "Tapetsering i Älvsjö",
  "lead": "Älvsjö villastad växte fram när Älvsjö var ett eget municipalsamhälle, och i de äldre husen dyker det ibland upp målade bårder och dekor när gamla tapeter tas ner. Geal Entreprenad AB tapetserar i villor och lägenheter i Älvsjö och tar hand om sådana fynd innan något nytt kommer upp.",
  "card": "Bårder och dekor i villastaden.",
  "sections": [
    {"id": "villastaden-alvsjo", "anchor": "Älvsjö villastad",
     "h2": "Villastaden i Älvsjö",
     "paras": [
       "Stockholms stads vägledning Varsam utveckling av småhus- och villaområden berättar att små stationssamhällen uppstod när järnvägen byggdes ut. På 1910-talet blev några av dem municipalsamhällen med egen administration och beskattningsrätt, och Älvsjö är ett av exemplen.",
       "I Älvsjö villastad togs stadsplanen fram av Per Olof Hallman enligt samma grundprinciper som hans planer för den tidiga trädgårdsstaden. I vägledningens tabell är delar av Älvsjö markerade som kulturhistoriskt värdefull miljö. I villastäderna var trä det dominerande fasadmaterialet, och glasverandor, takkupor och snickarglädje gav husen deras variation.",
     ],
     "aside": {"title": "Älvsjö i Varsam", "items": [
       "Municipalsamhälle på 1910-talet", "Stadsplan av Per Olof Hallman", "Del av Älvsjö: kulturhistoriskt värdefull miljö"]}},
    {"id": "barder-alvsjo", "h2": "När en bård dyker upp",
     "paras": [
       "Under tapeterna i en äldre villa kan det finnas en handmålad bård eller ett väggfält. Svenska Byggnadsvårdsföreningen påpekar att målarna ofta var aktiva lokalt och att regionala stilar var vanliga. Den som vill veta mer om en bård kan ta kontakt med länsmuseet eller närmaste hembygdsförening.",
       "Vi stannar upp när vi hittar något sådant. Bården fotograferas och mäts, och du får välja om den ska sparas synlig, byggas in bakom den nya tapeten eller återskapas. Ingenting tas bort innan du har bestämt dig, eftersom en riven bård inte går att få tillbaka.",
     ],
     "aside": {"title": "Om du hittar dekor", "items": [
       "Fotografera och mät", "Skrapa ett litet prov", "Fråga museet eller hembygdsföreningen", "Välj: spara, bygga in eller återskapa"]}},
    {"id": "skrapa-alvsjo", "anchor": "Skrapa fram färgen",
     "h2": "Skrapa fram den gamla färgen",
     "paras": [
       "Byggnadsvårdsföreningen svarar på en fråga om dekor i putsen att det enda sättet att ta reda på hur den såg ut är att provskrapa försiktigt med en skalpell eller vass kniv. Föreningen tipsar också om att fråga grannarna om de har liknande dekor.",
       "Färgen man hittar behöver inte vara den ursprungliga nyansen. Den kan ha blivit sliten eller smutsig, och linoljefärg gulnar i mörker men återfår sin nyans när den får dagsljus en tid. Ett skrapprov ger ändå en god bild av vilka färgskalor det rör sig om.",
     ],
     "aside": None},
    {"id": "ny-tapet-alvsjo", "h2": "Ny tapet i det gamla rummet",
     "paras": [
       "När bården ska vara kvar synlig tapetserar vi fram till den och skär kanten rakt. Ska den byggas in sätter vi ett skikt makulatur över, så att den går att ta fram igen. Ska den återskapas tar du hjälp av en dekorationsmålare med skrapprovet som förlaga.",
       "Valet av tapet styrs av rummet: en lugn tapet låter en bevarad bård synas, medan ett rum utan dekor tål mer mönster. Om målning av väggar och tak i Älvsjö kan du läsa under " + _L.format("malare-alvsjo.html", "målare i Älvsjö") + ".",
     ],
     "aside": None},
    {"id": "klassning-alvsjo", "h2": "Klassade hus och lov",
     "paras": [
       "Ny tapet inomhus kräver inget bygglov. Stadsmuseets klassificeringskarta ger ändå en bild av husets värde, och i ett blått eller grönt klassat hus är det extra viktigt att fasta inredningsdetaljer tas om hand.",
       "Ska golven slipas eller fönstren renoveras samtidigt planerar vi ordningen så att det dammiga arbetet görs först. Läs mer under " + _L.format("golvslipning-alvsjo.html", "golvslipning i Älvsjö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen i Älvsjö till",
  "steps": [
    ("Platsbesök", "Vi tittar på väggarna och lyfter en hörnbit för att se vad som finns under."),
    ("Skriftligt kostnadsförslag", "Underarbete, eventuell dekor och tapetsering står för sig."),
    ("Skydd", "Golv, lister och snickerier täcks."),
    ("Nedtagning", "Gamla lager tas ner, och fynd dokumenteras innan vi går vidare."),
    ("Tapetsering", "Ny tapet sätts upp runt eller över bevarad dekor."),
    ("Genomgång", "Vi lämnar restbitar och bilder på det vi hittade."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Älvsjö",
  "rot": [
    "Skatteverket räknar tapetsering inomhus som rotarbete i den bostad du äger och själv använder. I en bostadsrätt gäller avdraget arbete inne i lägenheten som du ansvarar för.",
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Älvsjö?",
  "price": [
    "Antalet rum, hur många lager som ska ner och om dekor ska sparas eller byggas in. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vi hittade en målad bård under tapeten i vår villa i Älvsjö – vad gör vi?",
     "Fotografera den och skrapa ett litet prov. Länsmuseet eller hembygdsföreningen kan ofta berätta mer, eftersom målarna ofta var verksamma lokalt."),
    ("Varför ser den framskrapade färgen gulare ut än väntat?",
     "Linoljefärg gulnar i mörker men återfår sin nyans när den får dagsljus en tid."),
    ("Går det att tapetsera över dekoren och spara den?",
     "Ja. Ett skikt makulatur över dekoren gör att den går att ta fram igen."),
    ("Kan en bård återskapas om den redan är skadad?",
     "Ja, med ett skrapprov och bilder som förlaga kan en dekorationsmålare måla en ny bård i samma mönster och färger."),
    ("Behövs bygglov för ny tapet i ett klassat hus?",
     "Nej, men fasta inredningsdetaljer i ett blått eller grönt klassat hus bör tas om hand."),
  ],
  "sources": [_VARSAM, _SBF_BARD, _SBF_DEKOR, _STH_KL, _SKV, _SKV2],
  "cta": ("Ska villan i Älvsjö tapetseras?", "Boka ett gratis platsbesök, så tittar vi på väggarna och det som kan finnas under innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre trävilla med snickarglädje i en grönskande villastad",
     "early 1900s Swedish wooden villa painted pale green with white decorative carpentry, glazed veranda and dormer, lush garden with hedge and fruit trees, winding street in a south Stockholm villa suburb, summer" + _IMG_END),
    ("Handmålad bård som kommit fram under en avriven tapet",
     "close view of an old interior wall where wallpaper has been removed near the ceiling, revealing a faded hand-painted decorative border with a simple repeating ornament in ochre and blue on a pale distemper wall, daylight" + _IMG_END),
    ("Litet skrapprov som visar flera färglager på en vägg",
     "macro view of a small scraped test window on an old plastered wall showing several thin paint layers in different colours, a scalpel lying on a cloth below, soft daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERMALM
"tapetsering-ostermalm.html": {
  "kind": "district", "service": "tapetsering", "ort": "Östermalm", "svc_label": "Tapetsering",
  "title": "Tapetsering på Östermalm – klassade våningar",
  "description": "Tapetsering på Östermalm: stenstadens bostadsrätter, förvanskningsförbudet som gäller även interiört, ansvaret för lägenhetens inre och ROT.",
  "h1": "Tapetsering på Östermalm",
  "lead": "De flesta lägenheter på Östermalm är bostadsrätter i äldre stenhus, och många av husen är klassade av Stadsmuseet. Geal Entreprenad AB tapetserar i lägenheter på Östermalm och utgår från att en ny tapet ska passa ett rum som har sin historia.",
  "card": "Klassade våningar och bostadsrätt.",
  "sections": [
    {"id": "bostadsratter-ostermalm", "anchor": "Bostadsrätterna",
     "h2": "Bostadsrätter i stenstaden",
     "paras": [
       "Stockholms stads områdesfakta för 2024 visar hur dominerande bostadsrätten är. I församlingsområdena Hedvig Eleonora och Oscar fanns tillsammans omkring 17 400 bostäder, och nästan 12 900 av dem var bostadsrätter. Bara ett fåtal var småhus.",
       "För tapetsering betyder det att nästan varje uppdrag sker i en lägenhet i ett flerbostadshus. Det påverkar allt från hur material bärs upp i trapphuset till när på dagen det går att arbeta utan att störa grannarna.",
     ],
     "aside": {"title": "Bostäder 2024", "items": [
       "Hedvig Eleonora: 5 164 bostadsrätter", "Oscar: 7 735 bostadsrätter", "Totalt omkring 17 400 bostäder"]}},
    {"id": "klassning-ostermalm", "h2": "Klassade hus och förvanskningsförbudet",
     "paras": [
       "Stadsmuseet klassar byggnader i blått, grönt, gult och grått. Är huset markerat med blått eller grönt i kartan behöver du söka bygglov för åtgärder som annars är bygglovsbefriade.",
       "Boverket förklarar att förvanskningsförbudet gäller vid alla ändringar, såväl exteriört som interiört, och oavsett om åtgärden kräver lov eller anmälan. En ny tapet kräver inget lov, men i ett blått eller grönt hus ska väggfasta detaljer som stuckatur, boaseringar och original­snickerier inte skadas eller tas bort när rummet görs om.",
     ],
     "aside": {"title": "Stadsmuseets karta", "items": [
       "Blått eller grönt: utökad lovplikt", "Gult eller grått: ingen utökad lovplikt i sig", "Ny tapet: inget lov"]}},
    {"id": "ansvaret-ostermalm", "anchor": "Ditt ansvar",
     "h2": "Ditt ansvar för lägenhetens inre",
     "paras": [
       "Enligt bostadsrättslagen ska bostadsrättshavaren på egen bekostnad hålla lägenheten i gott skick, om inte stadgarna säger annat. Väggarnas ytskikt hör till det du själv svarar för, och att byta tapet kräver normalt inte styrelsens tillstånd.",
       "Styrelsens tillstånd behövs däremot för ingrepp i bärande konstruktion och för ändringar av ledningar, ventilation och eldstad. Ska en vägg flyttas i samband med tapetseringen är det därför en annan fråga, och då kontaktar du styrelsen först.",
     ],
     "aside": None},
    {"id": "rummen-ostermalm", "h2": "Höga rum och raka linjer",
     "paras": [
       "I en äldre våning är väggarna ofta höga och rummen sällan helt raka. Vi lägger ut mönstret från rummets viktigaste vägg, oftast den man ser först, och låter skarvar och mönsterbrott hamna i hörn och bakom dörrar.",
       "Där taket har en stuckaturlist tapetserar vi upp till den och skär kanten rakt i stället för att röra listen. Om väggarna i övrigt behöver lagas eller målas kan du läsa under " + _L.format("malare-ostermalm.html", "målare på Östermalm") + ".",
     ],
     "aside": None},
    {"id": "underlaget-ostermalm", "anchor": "Underlaget",
     "h2": "Vad sitter under tapeten?",
     "paras": [
       "I ett stenhus sitter tapeten oftast på puts, men det kan också finnas papp, skivor eller väv från senare renoveringar. Innan vi river lyfter vi en bit i ett hörn eller bakom en dörr och ser hur många lager det finns och hur väl de sitter.",
       "Sitter lagren fast och ytan är jämn kan den nya tapeten ofta sättas direkt efter lagning av skador. Släpper de, eller har de bubblat, tas de ner rum för rum. Putsen under kan då behöva lagas där den spruckit eller lossnat, och sugande partier förlimmas innan tapetseringen.",
     ],
     "aside": {"title": "Före ny tapet", "items": [
       "Lyft en bit och räkna lagren", "Fäst eller ta ner lösa lager", "Laga sprickor i putsen", "Förlim sugande partier"]}},
    {"id": "tapetvalet-ostermalm", "h2": "En tapet som passar våningen",
     "paras": [
       "Många väljer att låta tapeten följa husets tid, med mönster och färger som stämmer med snickerierna och kakelugnarna. Andra vill ha en enkel bakgrund som låter stuckatur och dörrar stå för detaljerna. Båda valen fungerar, så länge de fasta delarna får vara kvar.",
       "Vi tar med provbitar till rummet och sätter upp dem i dagsljus innan du bestämmer dig. En tapet ser ofta annorlunda ut på en hög vägg med ljus från stora fönster än i en provbok.",
     ],
     "aside": None},
    {"id": "grannarna-ostermalm", "h2": "Trapphus och grannar",
     "paras": [
       "Underarbetet är det som låter och dammar. Vi skyddar trapphuset när material bärs in, håller dammet inne i lägenheten och planerar slipning och nedtagning till dagtid.",
       "Ska golven slipas i samma veva lägger vi tapetseringen efter slipningen, eller skyddar väggarna noga. Läs mer under " + _L.format("golvslipning-ostermalm.html", "golvslipning på Östermalm") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen på Östermalm till",
  "steps": [
    ("Platsbesök", "Vi tittar på väggarna, listerna och om huset är klassat."),
    ("Skriftligt kostnadsförslag", "Underarbete och tapetsering står för sig per rum."),
    ("Skydd", "Trapphus, golv, stuckatur och snickerier skyddas."),
    ("Underarbete", "Gamla lager tas ner eller fästs, väggarna jämnas."),
    ("Tapetsering", "Mönstret läggs ut från rummets viktigaste vägg."),
    ("Genomgång", "Vi går igenom rummen och lämnar restbitar."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering på Östermalm",
  "rot": [
    "Skatteverket räknar tapetsering inne i en bostadsrätt som rotarbete när arbetet gäller det du ansvarar för enligt stadgarna. Arbete i föreningens gemensamma utrymmen ger inget avdrag.",
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Östermalm?",
  "price": [
    "Takhöjden, antalet rum, hur mycket väggarna behöver lagas och hur mycket som ska skyddas. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi styrelsens tillstånd för att tapetsera vår bostadsrätt på Östermalm?",
     "Normalt inte. Bostadsrättshavaren svarar för lägenhetens inre. Tillstånd krävs däremot för bland annat ingrepp i bärande konstruktion och ändrade ledningar."),
    ("Vårt hus är blåklassat – får vi byta tapet?",
     "Ja, ny tapet kräver inget lov. Men förvanskningsförbudet gäller även interiört, så väggfasta originaldetaljer ska inte skadas."),
    ("Hur gör ni vid en stuckaturlist i taket?",
     "Vi tapetserar upp till listen och skär kanten rakt, utan att röra listen."),
    ("Får vi rotavdrag i bostadsrätten?",
     "Ja, för arbete inne i lägenheten som du ansvarar för. Tapet och material ger inget avdrag."),
    ("Kan ni tapetsera direkt på de gamla lagren?",
     "Om de sitter fast och ytan är jämn går det ofta. Släpper de tas de ner, och putsen lagas innan den nya tapeten sätts."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Hedvig Eleonora (pdf)", _OF + "inre-staden/norra-innerstaden/hedvig-eleonora.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Oscars kyrka (pdf)", _OF + "inre-staden/norra-innerstaden/oscars-kyrka.pdf"),
              _STH_KL, _BV_FORV, _BRL, _SKV, _SKV2],
  "cta": ("Ska lägenheten på Östermalm tapetseras?", "Boka ett gratis platsbesök, så tittar vi på rummen och husets klassning innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Stenhus från sekelskiftet med burspråk längs en lugn gata",
     "empty quiet street, no pedestrians, no cars: ornate early 1900s Stockholm stone apartment buildings with bay windows, balconies and decorated facades in warm beige and grey, tall street trees, Östermalm style, daylight" + _IMG_END),
    ("Hög vägg med ny tapet upp till en stuckaturlist",
     "tall wall in an old Stockholm apartment freshly hung with an elegant striped paper wallpaper up to an ornate white plaster cornice, tall white double door, herringbone parquet floor, daylight" + _IMG_END),
    ("Skyddspapp och tapetrullar på golvet i ett tomt rum",
     "still life in an empty old apartment room during wallpapering: protective cardboard on the parquet floor, masking tape on a white door frame, rolls of wallpaper, pasting table with brush, daylight from tall windows" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"tapetsering-osteraker.html": {
  "kind": "district", "service": "tapetsering", "ort": "Österåker", "svc_label": "Tapetsering",
  "title": "Tapetsering i Österåker – sommarvillan blir åretruntbostad",
  "description": "Tapetsering i Österåker: sommarvillor och fritidshus som blivit åretruntbostäder, täta tapeter och uppvärmning och varsamhetskravet inomhus.",
  "h1": "Tapetsering i Österåker",
  "lead": "I Österåker har många sommarvillor och fritidshus blivit hus som används året runt, och då förändras också vad väggarna utsätts för. Geal Entreprenad AB tapetserar i villor och fritidshus i Österåker och väljer tapettyp efter hur huset värms och används.",
  "card": "Sommarvillan blir åretruntbostad.",
  "sections": [
    {"id": "svinninge-osteraker", "anchor": "Sommarhusen",
     "h2": "Från sommarnöje till åretruntboende",
     "paras": [
       "Kommunens kulturmiljöprogram för Svinninge beskriver ett blandområde med permanent- och fritidsboende där åretruntboendet successivt ökat. När programmet skrevs var drygt 60 procent av fastigheterna bebodda året runt.",
       "Bebyggelsen är blandad: lantbruksbebyggelse från 1700- och 1800-talet, sommarhus och egnahem från sekelskiftet, sportstugor och fritidshus från 1930–60-talet och nya permanentbostäder. Kring Nantes brygga uppfördes ett trettiotal grosshandlarvillor på stora tomter vid tiden kring sekelskiftet, och på 1930-talet styckades marken för fritidshus.",
     ],
     "aside": {"title": "Svinninge enligt programmet", "items": [
       "Drygt 60 procent bebodda året runt", "Ett trettiotal grosshandlarvillor i Nantes", "Fritidshustomter från 1930-talet"]}},
    {"id": "uppvarmning-osteraker", "h2": "Täta tapeter och uppvärmning",
     "paras": [
       "Svenska Byggnadsvårdsföreningen svarar på en fråga om vanliga, billiga tapeter i ett äldre hus. Om huset värms upp året runt är det inga problem med tätskikt på insidan. Däremot kan det bli problem om huset kallställs på vintern, eftersom fukt då kan anrikas bakom tätskiktet.",
       "Frågan är alltså inte bara vilken tapet du tycker om, utan hur huset ska användas. Ett hus som nu värms hela året ger större frihet i tapetvalet. Ett hus som fortfarande stängs över vintern mår bäst av papperstapet. Är planen att flytta in permanent om några år kan det vara klokt att välja efter hur huset används i dag och byta senare.",
     ],
     "aside": {"title": "Välj tapet efter huset", "items": [
       "Uppvärmt året runt: de flesta tapettyper fungerar", "Kallställt på vintern: välj papperstapet", "Osäkert: välj det öppnare alternativet"]}},
    {"id": "varsamhet-osteraker", "anchor": "Varsamhet inomhus",
     "h2": "Varsamhetskravet gäller inomhus",
     "paras": [
       "Österåkers kommun skriver att varsamhetskravet gäller alla byggnader och alla ändringar, oberoende av husets ålder, och både invändigt och utvändigt. Karaktärsdrag och värden ska tas tillvara när huset ändras.",
       "För tapetseringen betyder det att äldre panel, foder och dörrar i en sekelskiftesvilla inte ska rivas för att det är enklare. I programmet för Svinninge omfattas all bebyggelse av varsamhetskrav, och flera villor lyfts fram som särskilt välbevarade.",
     ],
     "aside": None},
    {"id": "vaggarna-osteraker", "h2": "Väggar som byggts om i omgångar",
     "paras": [
       "Ett fritidshus som blivit permanentbostad har ofta byggts om i omgångar. I ett rum kan det sitta panel, i ett annat skivor från 1970-talet och i ett tredje nya gipsväggar efter en tillbyggnad. Varje underlag kräver sitt förarbete, och skarvarna mellan gammalt och nytt behöver ofta extra omsorg.",
       "Vi börjar med att se var väggarna är torra och fasta och var det har varit fukt. Om tillbyggnader och lov i Österåker kan du läsa under " + _L.format("tillbyggnad-osteraker.html", "tillbyggnad i Österåker") + ", och om fönstren under " + _L.format("fonsterrenovering-osteraker.html", "fönsterrenovering i Österåker") + ".",
     ],
     "aside": None},
    {"id": "fukt-osteraker", "anchor": "Fukt i väggen",
     "h2": "Leta efter fukt innan du tapetserar",
     "paras": [
       "Ett hus som stått ouppvärmt under många vintrar kan ha väggar som tagit upp fukt. Innan vi tapetserar känner vi efter lös tapet, missfärgningar och lukt, särskilt på norrväggar, i hörn mot ytterväggar och bakom stora möbler som stått mot väggen.",
       "Hittar vi tecken på fukt tapetserar vi inte över dem, eftersom en ny tapet bara döljer problemet en tid. Orsaken behöver hittas först, och ibland räcker det att huset nu värms jämnt och ventileras. Då kan väggen få torka en tid innan den nya tapeten kommer upp.",
     ],
     "aside": {"title": "Tecken att se efter", "items": [
       "Tapet som släpper", "Missfärgningar och fläckar", "Unken lukt", "Kalla hörn mot ytterväggar"]}},
    {"id": "valet-osteraker", "h2": "Tapeten i ett sommarhus",
     "paras": [
       "Många vill behålla sommarhusets ljusa och enkla känsla när huset blir ett helårshem. En papperstapet med litet mönster eller en enkel randig tapet brukar passa, men valet är ditt.",
       "Vi hjälper till med åtgången och mönsterpassningen. Om målning inne och ute i Österåker kan du läsa under " + _L.format("malare-osteraker.html", "målare i Österåker") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen i Österåker till",
  "steps": [
    ("Platsbesök", "Vi tittar på väggarna och frågar hur huset värms under vintern."),
    ("Skriftligt kostnadsförslag", "Underarbete och tapetsering står för sig per rum."),
    ("Skydd", "Golv, panel och snickerier täcks."),
    ("Underarbete", "Lösa lager tas ner, skivor fästs och skarvar jämnas."),
    ("Tapetsering", "Tapettypen väljs efter rummet och uppvärmningen."),
    ("Genomgång", "Vi går igenom rummen och lämnar restbitar."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Österåker",
  "rot": [
    "Skatteverket räknar tapetsering inomhus som rotarbete, både i permanentbostaden och i ett fritidshus som du äger och själv använder.",
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Österåker?",
  "price": [
    "Antalet rum, hur många olika underlag väggarna har och hur mycket som behöver lagas. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vårt sommarhus i Österåker värms nu året runt – kan vi välja vilken tapet som helst?",
     "I ett hus som värms året runt är tätare tapeter normalt inget problem, enligt Byggnadsvårdsföreningen. Det är när huset kallställs som fukt kan samlas bakom täta skikt."),
    ("Vilken tapet ska vi ha i ett hus som stängs över vintern?",
     "Papperstapet. Den släpper igenom fukt bättre än täta tapeter."),
    ("Gäller varsamhetskravet även inne i huset?",
     "Ja. Österåkers kommun skriver att det gäller alla byggnader och ändringar, både invändigt och utvändigt."),
    ("Får vi rotavdrag i fritidshuset?",
     "Ja, om du äger huset och själv använder det. Avdraget gäller arbetskostnaden."),
  ],
  "sources": [_OST_KMP, _OST_KULT, _SBF_MODERN, _SKV, _SKV2],
  "cta": ("Ska villan eller fritidshuset i Österåker tapetseras?", "Boka ett gratis platsbesök, så tittar vi på väggarna och uppvärmningen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla med veranda på en sjötomt",
     "large early 1900s Swedish summer villa painted white with ornate wooden veranda and dormers, big lawn sloping down to a calm sound with a wooden jetty and boathouse, pine trees, Roslagen archipelago, summer" + _IMG_END),
    ("Ljust rum med vitmålad bröstpanel i ett äldre hus",
     "bright room in an old Swedish summer house with lower wooden wainscot panel painted white and freshly hung light paper wallpaper with a small pattern above, window with view to the water, wooden floor, daylight" + _IMG_END),
    ("Tapetrullar och klisterbord i ett tomt rum",
     "still life in an empty room of an old wooden house: pasting table with a brush and a bucket of paste, several rolls of light patterned paper wallpaper, plumb line hanging on the wall, soft daylight" + _IMG_END),
  ],
},
}
