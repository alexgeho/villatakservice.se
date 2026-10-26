# -*- coding: utf-8 -*-
"""Golvslipning – ortsidor v27: Vasastan, Vällingby, Värmdö, Hässelby, Spånga, Österåker (2026-10-26).
Deltjänst under golvlaggning.html (TJ_HUB["golvslipning"]). Intent: slipa och ytbehandla ett BEFINTLIGT trägolv – inte
lägga nytt (det är golvlaggare-<ort>.html, som varje sida länkar till). Tre bilder per sida.

Lokal vinkel per sida (en huvudfråga per sida, skild från v15/v17/v18/v19-sidorna och från varandra):
Vasastan – stav- och fiskbensparkett i stenstadens lägenheter: slipriktning (diagonalt först), slitskiktet, hur mycket
  en slipning tar (0,5–1 mm, lamellparkett 2–4 gånger), P3 och ekdamm, bostadsrätternas stadgar (områdesfakta).
Vällingby – 1950-talets lamellgolv på sandbädd och lösa reglar (flytande golv från mitten av 1940-talet), svikt och
  ondulering, risk för stavsläpp, holländsk parkett i björk, tunnelbanestaden 1954 (riksintresse), ägarformer.
Värmdö – gamla brädgolv i äldre hus (SCB: småhus byggda före 1950), förvanskningsförbudet gäller även interiört,
  Värmdös 14 riksintressen och cirka 55 kulturmiljöområden, grangolv som åldras till silvergrått – slipa eller inte.
Hässelby – golvet under mattan i hus från 1940–1970-talen: asbest (Boverket, utjämningsmassor), spikar efter masonit
  och linoleum, gnistor och dammexplosion (GBR), villastaden och grupphusen (Varsam, områdesfakta).
Spånga – breda originalgolv i villastädernas äldre villor: lyfta, vända och slå ihop, springor efter årstid, hyvling
  mot slipning, sickling som kompromiss (Byggnadsvårdsföreningen), Solhems villor (Varsam, områdesfakta).
Österåker – sommarvillor och sportstugor som blivit åretruntboenden (Svinninge 2008), tjärpappens färg i golv under
  gamla mattor, liten excenterslip, breda springor i sommarhus, SCB:s småhus efter byggår, fritidshus och ROT.

Fakta endast från källorna i respektive 'sources', öppnade 2026-10-26: curl (UA Mozilla) för kommunernas, stadens,
Boverkets och Golvbranschens sidor (alla 200), byggnadsvard.se via webbplatsens WP-API (/wp-json/wp/v2/posts/<id>),
SCB via PxWeb-API (BO0104T02, BO0104T04, 2025), Skatteverket via curl med webbläsar-UA. Alla pdf:er har textlager.
Strukna / ej använda: vilka golv som faktiskt ligger i husen i respektive ort (skrivet som villkor "har du …"),
ordningsregler och arbetstider i föreningar, om styrelsens tillstånd krävs för golvslipning (skrivet "läs stadgarna"),
tillverkar- och varumärkesnamn i källorna (utom AB Gustaf Kähr, som källan nämner som historisk uppgift), priser,
avgifter, tidsåtgång. Inga garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_BV = "https://byggnadsvard.se/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


def _sbf(titel, slug):
    return (f"Svenska Byggnadsvårdsföreningen – {titel}", _BV + slug + "/")


_GBR = ("Golvbranschen – Branschriktlinjer SLIP 22, slipning av trägolv (pdf)",
        "https://www.golvbranschen.se/siteassets/dokument/branschriktlinjer/branschriktlinjer---slipning-av-tragolv---slip-22.pdf")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_BOV_ASB = ("Boverket – Risker med hantering av asbest i byggnader",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_BOV_FORV = ("Boverket – PBL kunskapsbanken: Förvanskningsförbudet",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/teman/kulturvarden/kulturvarden-i-plan---och-bygglagen/krav-pa-byggnadsverk-och-tomter/forvanskningsforbudet/")
_VAR_KULT = ("Värmdö kommun – Bygga i kulturmiljöer",
             "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/byggaikulturmiljoer.4.57b4a3ba16e6b961dbf10429.html")
_OST_SVIN = ("Österåkers kommun – Råd och riktlinjer för byggande i Svinninge (pdf)",
             "https://www.osteraker.se/download/18.5bb0400617c11d33b5536/1632390824156/rad_och_vagledning_svinninge.pdf")
_SCB_PER = ("SCB – Antal lägenheter efter region, hustyp och byggnadsperiod (BO0104T02)",
            "https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BO__BO0104__BO0104D/BO0104T02/")
_SCB_UPPL = ("SCB – Antal lägenheter efter region, hustyp och upplåtelseform (BO0104T04)",
             "https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BO__BO0104__BO0104D/BO0104T04/")

_SBF_PARKETT = _sbf("Materialhörnan – Parkettgolv", "materialhornan-parkettgolv")
_SBF_GAMPARK = _sbf("Gammalt parkettgolv?", "gammalt-parkettgolv-2")
_SBF_1943 = _sbf("Parkett från 1943", "parkett-fran-1943")
_SBF_VAD = _sbf("Vad göra?", "vad-goera")
_SBF_TRAGOLV = _sbf("Trägolv", "tragolv")
_SBF_FISKBEN = _sbf("Lägga ny fiskbensparkett så traditionellt som möjligt", "lagga-ny-fiskbensparkett-sa-traditionellt-som-mojligt")
_SBF_BUCKL = _sbf("Hur renovera buckliga originalgolv från början av 1900-talet?",
                  "hur-renovera-buckliga-originalgolv-fran-borjan-av-1900-talet")
_SBF_SEKEL = _sbf("Golv i sekelskifteshus", "golv-i-sekelskifteshus")
_SBF_TJARA = _sbf("Tjärat trägolv?", "tjarat-tragolv")
_SBF_SPRING = _sbf("Breda golvspringor", "breda-golvspringor")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden, som mest 50 000 kronor per person och år, och rot och rut får "
            "tillsammans vara högst 75 000 kronor. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ VASASTAN
"golvslipning-vasastan.html": {
  "kind": "district", "service": "golvslipning", "ort": "Vasastan", "svc_label": "Golvslipning",
  "title": "Golvslipning i Vasastan – stavparkett och fiskben",
  "description": "Golvslipning i Vasastan: stav- och fiskbensparkett i stenstadens lägenheter, slipriktning, hur mycket slitskikt som finns kvar och rotavdrag i bostadsrätt.",
  "h1": "Golvslipning i Vasastan",
  "lead": "I stenstadens lägenheter i Vasastan ligger ofta stav- eller fiskbensparkett som har slipats förut. Frågan är därför inte bara hur golvet ska se ut, utan hur mycket trä som finns kvar att slipa. Geal Entreprenad AB slipar och ytbehandlar parkett i Vasastan och kontrollerar slitskiktet innan arbetet börjar.",
  "card": "Stav- och fiskbensparkett.",
  "sections": [
    {"id": "lagenheter-vasastan", "anchor": "Lägenheterna",
     "h2": "Bostadsrätter i stenstaden",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 8 532 lägenheter i flerbostadshus i Gustav Vasa församling. 1 467 av dem är ettor, 2 328 tvåor, 1 955 treor och 1 673 har fyra rum eller fler. I Västra Matteus finns 11 913 lägenheter i flerbostadshus, och 8 990 av församlingens bostäder är bostadsrätter. Det är alltså oftast du själv som beställer golvslipningen, men inom ramen för föreningens stadgar. Läs dem innan du bokar, så att du vet vad föreningen säger om golv, buller och arbetstider.",
       "Vasastan hör till den klassiska stenstaden, som översiktsplanens riksintressedel beskriver som tät kvartersstad med bebyggelse från 1870 till 1930. Parketten har en egen historia under samma tid. Enligt Nordiska museet, i Byggnadsvårdsföreningens Materialhörnan, fick stavparketten sitt stora genombrott under 1900-talet, och på 1920-talet började man klistra fast specialhyvlade parkettstavar med asfalt direkt på betong.",
     ],
     "aside": {"title": "Gustav Vasa enligt områdesfakta", "items": [
       "8 532 lägenheter i flerbostadshus", "5 707 bostadsrätter", "1 107 lägenheter utan kök", "636 med fem rum eller fler"]}},
    {"id": "slitskikt-vasastan", "h2": "Hur mycket finns kvar att slipa?",
     "paras": [
       "Golvbranschens riktlinjer SLIP 22 säger att golvet ska inspekteras före slipningen. Laminat, golv med ett slitskikt tunnare än en millimeter och vissa fabrikslackerade golv går inte att slipa, och är man osäker kan man kontrollera med en kniv i en springa i ett hörn av rummet. Har slitskiktet lossnat på något ställe ska det limmas ner först.",
       "Byggnadsvårdsföreningen skriver i ett svar att en slipning med golvslipmaskin tar bort ungefär en halv till en millimeter av parketten, så djupare märken än så kan synas även efteråt. En lamellparkett brukar enligt samma svar kunna slipas två till fyra gånger. I en äldre lägenhet där golvet slipats flera gånger förut är det därför värt att titta noga innan maskinen kopplas in.",
     ],
     "aside": {"title": "Kontrollera före slipning", "items": [
       "Att golvet går att slipa", "Slitskiktets tjocklek", "Lösa stavar", "Fuktkvot och luftfuktighet"]}},
    {"id": "fiskben-vasastan", "h2": "Fiskben slipas diagonalt först",
     "paras": [
       "Enligt riktlinjerna ska rutmönster, fiskben och andra mönster där träet ligger åt olika håll normalt slipas först diagonalt och sedan i rummets längdriktning, eller från det håll ljuset kommer. Grovslipningen görs normalt med korn 36–50, mellanslipningen med korn 60–80, och slutresultatet ska motsvara korn 120 för lövträ som ek. Efter färdigslipningen får det inte finnas slipränder kvar, och det är extra viktigt om golvet ska pigmenteras.",
       "Kanterna slipas med en något grövre kornstorlek än resten av golvet, och hörn som sicklas putsas med samma papper som den sista slipningen, så att strukturen blir densamma överallt. Vill du byta golv i ett rum i stället för att slipa finns mer under " + _L.format("golvlaggare-vasastan.html", "golvläggare i Vasastan") + ".",
     ],
     "aside": None},
    {"id": "damm-vasastan", "h2": "Damm, brand och grannarna",
     "paras": [
       "SLIP 22 anger att slipdamm från bland annat ek och bok är cancerframkallande, och att slipning bör göras med en partikelseparator eller cyklondammsugare med HEPA-filter och med andningsskydd av klass P3. Slipdamm som blandats med lack eller oljerester kan självantända, så dammpåsen ska tömmas och förvaras utomhus eller på en brandsäker plats.",
       "I ett flerbostadshus påverkar det också trapphuset. Vi täcker dörrar och ventiler, bär ut dammet i slutna säckar och berättar för dig när det blir ljud, så att du kan informera grannarna. Golvet ska enligt riktlinjerna inte ytbehandlas när luftfuktigheten inomhus ligger utanför 30–60 procent eller fuktkvoten i trät utanför 6–10 procent. Läs mer om tjänsten under " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipningen till i Vasastan",
  "steps": [
    ("Platsbesök", "Vi ser på mönstret, slitskiktet och tidigare slipningar."),
    ("Skriftligt kostnadsförslag", "Slipning, lagning och ytbehandling var för sig."),
    ("Förberedelse", "Möbler ut, lister lossas och trapphuset skyddas."),
    ("Slipning", "Diagonalt först i mönstret, sedan i längdriktningen."),
    ("Ytbehandling", "Lack, olja eller såpa när fuktvärdena är rätt."),
    ("Genomgång", "Skötselråd för golvet de första veckorna."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i bostadsrätt",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete även i en bostadsrätt, när arbetet görs innanför lägenhetens väggar, tak och golv och du har underhållsansvaret enligt föreningens stadgar.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för golvslipning i Vasastan?",
  "price": [
    "Golvytan, mönstret, hur många gånger golvet slipats förut, lagning av lösa stavar, vilken ytbehandling du väljer och hur dammet kan bäras ut. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur slipas fiskbensparkett i en lägenhet i Vasastan?",
     "Enligt Golvbranschens riktlinjer slipas mönsterlagd parkett normalt först diagonalt och sedan i rummets längdriktning eller från det håll ljuset kommer."),
    ("Hur många gånger kan parketten i vår lägenhet i Vasastan slipas?",
     "Det beror på slitskiktet. Byggnadsvårdsföreningen skriver att en slipning tar ungefär en halv till en millimeter och att lamellparkett brukar klara två till fyra slipningar."),
    ("Är slipdammet från ekparkett farligt?",
     "Golvbranschen anger att damm från ek och bok är cancerframkallande. Slipningen görs med dammavskiljare med HEPA-filter och andningsskydd av klass P3."),
    ("Får jag rotavdrag för golvslipning i min bostadsrätt i Vasastan?",
     "Ja, om arbetet görs innanför lägenhetens väggar, tak och golv och du har underhållsansvaret enligt stadgarna."),
  ],
  "sources": [_of("Gustav Vasa", "inre-staden/norra-innerstaden/gustav-vasa"),
              _of("Västra Matteus", "inre-staden/norra-innerstaden/vastra-matteus"), _RIKS, _SBF_PARKETT, _SBF_GAMPARK, _GBR, _SKV],
  "cta": ("Ska parketten i Vasastan slipas?", "Boka ett gratis platsbesök, så kontrollerar vi slitskiktet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipad fiskbensparkett i ek i en äldre stadslägenhet",
     "freshly sanded and lacquered oak herringbone parquet floor in an empty early 1900s Stockholm apartment, tall window with deep sill, white panelled walls, soft daylight across the floor" + _SFX),
    ("Golvslipmaskin på en delvis slipad stavparkett",
     "drum floor sanding machine standing on a partly sanded oak strip parquet floor, the sanded area pale and the unsanded area darker with old lacquer, empty room, daylight" + _SFX),
    ("Hörn av ett parkettgolv där kanten slipats",
     "close view of the corner of an oak herringbone parquet floor where the edge has been sanded smooth along a white skirting board, fine dust-free surface, soft light" + _SFX),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"golvslipning-vallingby.html": {
  "kind": "district", "service": "golvslipning", "ort": "Vällingby", "svc_label": "Golvslipning",
  "title": "Golvslipning i Vällingby – 1950-talets lamellgolv",
  "description": "Golvslipning i Vällingby: lamellgolv på sandbädd i tunnelbanestadens lägenheter, svikt och ondulering, risken för stavsläpp och rotavdrag.",
  "h1": "Golvslipning i Vällingby",
  "lead": "Vällingby byggdes under 1950-talet, och i den tidens flerbostadshus låg golven ofta flytande på sand och reglar. Ett sådant golv går att slipa, men det fjädrar och kan bli vågigt om det inte förbereds. Geal Entreprenad AB slipar golv i lägenheter och radhus i Vällingby och berättar om riskerna innan vi börjar.",
  "card": "Lamellgolv, svikt och slitskikt.",
  "sections": [
    {"id": "stadsdelen-vallingby", "anchor": "Stadsdelen",
     "h2": "Tunnelbanestaden från 1950-talet",
     "paras": [
       "Enligt stadens vägledning Varsam utveckling av småhus- och villaområden var Vällingby den första tunnelbanestaden och invigdes 1954. Översiktsplanens riksintressedel beskriver Vällingby–Råcksta som landets första så kallade ABC-stad, utbyggd under 1950-talet och ett sammanhållet uttryck för det årtiondet. Ingen skulle ha längre än 900 meters gångväg till tunnelbanan.",
       "Stadens områdesfakta för 2025 räknar 3 891 lägenheter i flerbostadshus i Vällingby. Bostadsrätterna är 2 076, allmännyttans lägenheter 1 498 och de övriga hyresrätterna 597. Till det kommer 449 småhus, varav 228 bostadsrätter och 220 med äganderätt – radhus och kedjehus längst ut från centrum.",
     ],
     "aside": {"title": "Vällingby enligt områdesfakta", "items": [
       "3 891 lägenheter i flerbostadshus", "2 076 bostadsrätter", "1 498 i allmännyttan", "449 småhus"]}},
    {"id": "flytande-vallingby", "h2": "Golv på sandbädd och reglar",
     "paras": [
       "Nordiska museet beskriver i Byggnadsvårdsföreningens Materialhörnan hur metoden att lägga flytande golv infördes vid mitten av 1940-talet och snabbt blev populär, bland annat i hyreshus. På betongbjälklaget lades en sandbädd som jämnades ut, och på den lösa träreglar som lamellbrädorna fästes på. Det gav bättre ljudisolering och ett något fjädrande golv. Lamellbrädan, med krysslimmade furulameller och en slityta av lövträ, hade lanserats på 1930-talet.",
       "Har ditt golv lagts så finns det inget att göra åt fjädringen i sig – den hör till konstruktionen. Men den påverkar slipningen, och vi trycker därför på golvet rum för rum innan vi föreslår något. Enligt samma text måste trämaterialet vara absolut torrt för att det inte ska uppstå torksprickor mellan stavarna, och förr hyvlades och handsicklades nylagda golv för att få en perfekt yta. I dag handsicklas golv bara i hörnen där golvslipmaskinen inte kommer åt.",
     ],
     "aside": {"title": "Flytande golv från 1940-talet", "items": [
       "Sandbädd på betongbjälklaget", "Lösa träreglar", "Lamellbrädor ovanpå", "Bättre ljudisolering"]}},
    {"id": "svikt-vallingby", "h2": "Svikt, ondulering och stavsläpp",
     "paras": [
       "Golvbranschens riktlinjer SLIP 22 säger att undergolvet ska vara stabilt utan svikt. Sviktar golvkonstruktionen kan resultatet bli så kallad ondulering, alltså en vågig yta. Kan svikten inte åtgärdas före slipningen ska kunden informeras om risken innan arbetet börjar, och det gör vi skriftligt.",
       "När golvet är en lamellkonstruktion finns enligt riktlinjerna en generell risk för stavsläpp, alltså att slitskiktet lossnar vid eller efter slipningen. Golventreprenören ska upplysa konsumenten om det. Finns misstanke om stavsläpp, till exempel när golvet har varit vattenskadat, bör man avråda från omslipning. Vi kontrollerar därför slitskiktet med en kniv i en springa i ett hörn och väljer ytbehandling efter risken.",
     ],
     "aside": None},
    {"id": "bjork-vallingby", "h2": "Ljusa golv av björk",
     "paras": [
       "I ett svar om en lägenhet från 1943 i Stockholms närförort skriver Byggnadsvårdsföreningen att läggningsmönstret holländsk parkett och ljusa träslag som björk, ask eller lönn passade bra efter att lamellbrädan lanserats. Har du ett sådant golv vill du sannolikt behålla den ljusa tonen som golvet hade när det var nytt. Då väljer vi slippapper och ytbehandling så att träet inte gulnar mer än nödvändigt.",
       "Riksintressedelen räknar de ursprungliga husens byggnadsdetaljer till det som är värdebärande i Vällingby–Råcksta. Golven inne i lägenheterna nämns inte, men ett välbevarat golv från byggåret är ändå värt att vara rädd om. Ska golvet bytas i stället finns mer under " + _L.format("golvlaggare-vallingby.html", "golvläggare i Vällingby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipningen till i Vällingby",
  "steps": [
    ("Platsbesök", "Vi trycker på golvet och kontrollerar slitskiktet."),
    ("Skriftligt kostnadsförslag", "Med information om svikt och stavsläpp."),
    ("Förberedelse", "Lösa partier limmas och lister lossas."),
    ("Slipning", "Med lågt tryck i finslipningen för att undvika vågor."),
    ("Ytbehandling", "Lack eller olja som passar träslaget."),
    ("Genomgång", "Skötselråd och första rengöringen."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i Vällingby",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete. I en bostadsrätt ska arbetet göras innanför bostadens väggar, tak och golv och avse sådant du ansvarar för enligt stadgarna, och i ett radhus eller kedjehus med äganderätt ska du äga huset och bo i det.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för golvslipning i Vällingby?",
  "price": [
    "Golvytan, golvets konstruktion och skick, lagning av lösa partier, träslag och ytbehandling, om möbler ska bäras ut och om flera rum slipas samtidigt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför fjädrar golvet i min lägenhet i Vällingby?",
     "Om golvet är ett flytande golv på sandbädd och lösa reglar, som infördes vid mitten av 1940-talet, är en viss fjädring en del av konstruktionen."),
    ("Kan ett golv som sviktar slipas utan att bli vågigt?",
     "Golvbranschen varnar för ondulering när undergolvet sviktar. Kan svikten inte åtgärdas ska du informeras om risken innan arbetet börjar."),
    ("Vad är stavsläpp vid slipning av lamellgolv?",
     "Att slitskiktet lossnar vid eller efter slipningen. Golvbranschen anger att risken finns vid lamellkonstruktioner och att golventreprenören ska informera om den."),
    ("Går det att behålla den ljusa tonen i ett björkgolv i Vällingby?",
     "Ja, med rätt slippapper och en ytbehandling som inte gulnar för mycket. Vi visar prov innan hela golvet behandlas."),
  ],
  "sources": [_VARSAM, _RIKS, _of("Vällingby", "vasterort/hasselby-vallingby/vallingby"), _SBF_PARKETT, _SBF_1943, _GBR, _SKV],
  "cta": ("Ska golvet i Vällingby slipas?", "Boka ett gratis platsbesök, så trycker vi på golvet, kontrollerar svikt och slitskikt och berättar om riskerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat ljust björkgolv i en lägenhet från 1950-talet",
     "freshly sanded light birch parquet floor in an empty 1950s Swedish apartment, large window with simple frame, white walls, radiator under the window, soft daylight" + _SFX),
    ("Genomskärning av ett golv med sandbädd och lösa reglar",
     "cutaway view of a floor construction in an empty apartment: concrete slab, a smooth levelled layer of dry sand, loose wooden battens lying on the sand, and wooden floor boards on top with one row removed, clean and dry, daylight" + _SFX),
    ("Ljust trägolv efter slipning",
     "close view of light-coloured Dutch pattern parquet floor after sanding, smooth matte surface, soft window light, empty room" + _SFX),
  ],
},

# ------------------------------------------------------------------ VÄRMDÖ
"golvslipning-varmdo.html": {
  "kind": "district", "service": "golvslipning", "ort": "Värmdö", "svc_label": "Golvslipning",
  "title": "Golvslipning på Värmdö – gamla brädgolv i äldre hus",
  "description": "Golvslipning på Värmdö: gamla brädgolv i hus byggda före 1950, när slipning är rätt och fel, förvanskningsförbudet inomhus och rotavdrag.",
  "h1": "Golvslipning på Värmdö",
  "lead": "På Värmdö finns många äldre hus med breda brädgolv som har skurats, oljats eller målats i generationer. Ett sådant golv kan bli fint av en slipning, men det kan också förlora det som gör det värt att behålla. Geal Entreprenad AB slipar och behandlar trägolv på Värmdö och hjälper dig att välja hur hårt golvet ska tas.",
  "card": "Gamla brädgolv och skonsam slipning.",
  "sections": [
    {"id": "husen-varmdo", "anchor": "Husen",
     "h2": "Äldre småhus på Värmdö",
     "paras": [
       "SCB:s bostadsstatistik för 2025 räknar 12 789 lägenheter i småhus i Värmdö kommun. 945 av dem finns i hus byggda före 1931, 441 i hus från 1931–1940 och 670 i hus från 1941–1950. Lägg till 861 från 1950-talet, så finns drygt 2 900 småhusbostäder på Värmdö i hus byggda före 1961.",
       "Värmdö kommun skriver att det finns 14 områden av riksintresse för kulturmiljövården i kommunen och cirka 55 utpekade kulturmiljöområden, och att alla dessa räknas som särskilt värdefulla. Kommunantikvarien hjälper gärna till med råd, och kommunen rekommenderar att man fotograferar sin fastighet och hör av sig via mejl.",
     ],
     "aside": {"title": "Småhus på Värmdö enligt SCB", "items": [
       "945 byggda före 1931", "441 från 1931–1940", "670 från 1941–1950", "861 från 1951–1960"]}},
    {"id": "inomhus-varmdo", "h2": "Förvanskningsförbudet gäller även inomhus",
     "paras": [
       "Värmdö kommun skriver att särskilt värdefulla byggnader och områden inte får förvanskas enligt plan- och bygglagen, oavsett om åtgärden kräver bygglov eller inte. Boverket förklarar att förvanskningsförbudet gäller vid alla ändringar, såväl exteriört som interiört. Det är de egenskaper som gör byggnaden särskilt värdefull som skyddas, och förbudet är inget förändringsförbud.",
       "Kommunen skriver också att du behöver göra en anmälan och få startbesked om du ska underhålla en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde. Bor du i ett sådant hus tar vi reda på vad som gäller innan vi slipar ett golv som kan vara en del av husets värde.",
     ],
     "aside": {"title": "Värmdö kommun", "items": [
       "14 områden av riksintresse", "Cirka 55 kulturmiljöområden", "Kommunantikvarie för rådgivning", "Anmälan vid underhåll av skyddade hus"]}},
    {"id": "silvergratt-varmdo", "h2": "Silvergrått golv – slipa eller låta bli?",
     "paras": [
       "En läsare skrev till Svenska Byggnadsvårdsföreningen om ett grangolv från 1890-talet som en gång varit skurgolv och sedan oljats, och som nu var grått och trist. Svaret var att ett grangolv åldras till silvergrått, och att en slipning förstör det smutsavvisande skiktet och ger ett dött golv utan slitage. Föreningen föreslog att leva med golvhistorien och fortsätta med såpa, med kallt vatten. Är ytan uppsprucken så att det blir stickor i fötterna är en slipning däremot befogad.",
       "Det är ungefär så vi resonerar på Värmdö också. Är golvet friskt men grått föreslår vi rengöring och skurning i stället för slipning. Är det skadat, flagnande eller fullt av gammal lack slipar vi så skonsamt som möjligt och tar bara bort det som behövs.",
     ],
     "aside": None},
    {"id": "skonsamt-varmdo", "h2": "Så skonsamt som golvet tillåter",
     "paras": [
       "Golvbranschens riktlinjer SLIP 22 säger att eventuella spikar ska tas bort före slipning, eftersom de kan förstöra pappret och ge gnistor med risk för dammexplosion i slipdammpåsen. Sticker spikhuvuden upp i ett gammalt brädgolv går vi över hela ytan och sänker eller drar dem innan vi börjar.",
       "Grovslipningen ska enligt riktlinjerna ta bort all tidigare ytbehandling och jämna till golvet, och kornstorleken på startpappret avgörs av golvets skick. Ett brett furu- eller grangolv som bara ska fräschas upp behöver inte nödvändigtvis det grövsta pappret. Vill du hellre lägga ett nytt golv finns mer under " + _L.format("golvlaggare-varmdo.html", "golvläggare på Värmdö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipningen till på Värmdö",
  "steps": [
    ("Platsbesök", "Vi ser på golvets skick och vad det har behandlats med."),
    ("Kulturvärden", "Vi tar reda på om huset är skyddat eller särskilt värdefullt."),
    ("Skriftligt kostnadsförslag", "Rengöring, slipning och ytbehandling var för sig."),
    ("Förberedelse", "Spikar sänks eller dras och lister lossas."),
    ("Slipning", "Så lite som golvet kräver, med rätt papper."),
    ("Ytbehandling", "Såpa, olja, linoljefärg eller lack efter ditt val."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning på Värmdö",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete i ett småhus, och till småhus räknas enligt Skatteverket också fritidshus. Huset ska användas som bostad och ägas av dig. Är bostaden yngre än fem år får arbetet bara återställa det ursprungliga skicket.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för golvslipning på Värmdö?",
  "price": [
    "Golvytan, golvets skick och tidigare behandling, hur många spikar som behöver tas om hand, vilken ytbehandling du väljer och var på Värmdö huset ligger. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Ska ett gammalt grått grangolv på Värmdö slipas?",
     "Inte nödvändigtvis. Byggnadsvårdsföreningen skriver att grangolv åldras till silvergrått och att slipning förstör det smutsavvisande skiktet, men att slipning är befogad om ytan spricker upp."),
    ("Gäller förvanskningsförbudet golven inne i ett gammalt hus på Värmdö?",
     "Ja, om huset är särskilt värdefullt. Boverket skriver att förbudet gäller både exteriört och interiört."),
    ("Behöver jag göra en anmälan för att slipa golv i ett skyddat hus på Värmdö?",
     "Värmdö kommun skriver att underhåll av en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde kräver anmälan och startbesked. Fråga kommunen innan."),
    ("Varför tas spikarna bort innan golvet slipas?",
     "Golvbranschen skriver att spikar kan förstöra slippappret och ge gnistor med risk för dammexplosion i dammpåsen."),
  ],
  "sources": [_SCB_PER, _VAR_KULT, _BOV_FORV, _SBF_VAD, _GBR, _SKV],
  "cta": ("Har du ett gammalt golv på Värmdö som behöver fräschas upp?", "Boka ett gratis platsbesök, så går vi igenom golvet och kulturvärdena innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Brett grangolv med silvergrå patina i ett äldre trähus",
     "interior of an old Swedish wooden house in the archipelago, wide spruce floorboards with a silvery grey soap-scrubbed patina, white painted wooden walls, small paned window with sea light, simple wooden chair, soft daylight" + _SFX),
    ("Spikhuvuden som sänkts i ett gammalt brädgolv före slipning",
     "close view of old wide pine floorboards with nail heads punched below the surface before sanding, a nail punch lying on the boards, daylight" + _SFX),
    ("Breda brädor i olika nyanser efter slipning",
     "old wide plank floor partly sanded, one half with worn brown floor paint and the other half bare pale pine, empty room in an old wooden house, soft light" + _SFX),
  ],
},

# ------------------------------------------------------------------ HÄSSELBY
"golvslipning-hasselby.html": {
  "kind": "district", "service": "golvslipning", "ort": "Hässelby", "svc_label": "Golvslipning",
  "title": "Golvslipning i Hässelby – golvet under den gamla mattan",
  "description": "Golvslipning i Hässelby: trägolv under gamla mattor i villor och radhus från 1940–1970-talen, asbest i utjämningsmassor, spikar och rotavdrag.",
  "h1": "Golvslipning i Hässelby",
  "lead": "När en gammal plastmatta eller linoleummatta rivs i en villa i Hässelby ligger det ibland ett trägolv under som går att slipa fram. Men i hus från mitten av 1900-talet kan det också finnas asbest i underlaget. Geal Entreprenad AB slipar golv i Hässelby och tar reda på vad som ligger under innan vi river eller slipar.",
  "card": "Golvet under mattan.",
  "sections": [
    {"id": "villastad-hasselby", "anchor": "Husen i Hässelby",
     "h2": "Villastaden och grupphusen",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 7 029 bostäder i Hässelby villastad, varav 4 757 småhus med äganderätt. Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur många villor i Hässelby villastad på 1960- och 1970-talen ersattes av täta, stora grupper av enhetlig småhusbebyggelse, och hur tillkommande hus på tomter kring 600 kvadratmeter har kompletterat eller ersatt den äldre bebyggelsen.",
       "Det gör att Hässelby har hus från många decennier sida vid sida. En villa från 1920-talet, ett radhus från 1960-talet och ett hus från 2000-talet har helt olika golv och underlag. Vi frågar därför efter byggåret och efter tidigare renoveringar innan vi föreslår något.",
     ],
     "aside": {"title": "Hässelby villastad enligt områdesfakta", "items": [
       "7 029 bostäder", "4 757 småhus med äganderätt", "1 705 lägenheter i flerbostadshus", "794 bostadsrätter"]}},
    {"id": "asbest-hasselby", "h2": "Asbest i hus från 1940 till 1980",
     "paras": [
       "Boverket skriver att det främst är byggnader uppförda mellan 1940 och 1970 som innehåller asbest, och att det är sannolikt att det finns asbest någonstans i en byggnad från perioden 1940–1980. Asbest användes i byggnader främst från 1940-talet och en bit in på 1980-talet och förbjöds inom byggsektorn 1982. Provtagning och analys är enligt Boverket det enda säkra sättet att veta.",
       "Svenska Byggnadsvårdsföreningen skriver i ett svar att det under mitten av 1900-talet ibland användes asbesthaltiga utjämningsmassor, och att man bör vara försiktig och använda andningsmask och skyddskläder om man behöver riva i sådant material. Hittar vi en okänd utjämningsmassa under en matta i ett hus från den tiden tar vi prov innan vi slipar eller river.",
     ],
     "aside": {"title": "Boverket om asbest", "items": [
       "Förbjuden i byggsektorn 1982", "Främst hus från 1940–1970", "Ofarlig i bunden form", "Prov är enda säkra sättet"]}},
    {"id": "spik-hasselby", "h2": "Spikarna efter masonit och linoleum",
     "paras": [
       "En läsare skrev till Byggnadsvårdsföreningen om en villa från 1920 där en linoleummatta från 1943 hade tagits bort, och där golvet under var spikat med mängder av spik. Svaret var att golvet förmodligen varit täckt med masonit och linoleummatta, och att alla spikar bör tas ur innan golvet slipas.",
       "Golvbranschens riktlinjer SLIP 22 förklarar varför: spikar kan förstöra slippappret och ge gnistor med risk för dammexplosion i slipdammpåsen. Vi drar spikarna, fyller hålen där det behövs och ser efter om brädorna under mattan är hela nog att slipas. Är de inte det kan golvet behöva läggas om, och då finns mer under " + _L.format("golvlaggare-hasselby.html", "golvläggare i Hässelby") + ".",
     ],
     "aside": None},
    {"id": "under-hasselby", "h2": "Om det inte finns något trägolv under",
     "paras": [
       "Det är inte säkert att det finns ett trägolv under mattan. I ett annat svar berättar Byggnadsvårdsföreningen om en lägenhet i ett hus från 1913 där plastmattorna revs och inget trägolv fanns under. Golvet kan också vara ett trägolv av en kvalitet som inte var tänkt att synas, eller vara lagat med skivor.",
       "Därför lyfter vi en bit av mattan i ett hörn innan vi lovar något. Finns det ett golv som går att slipa gör vi det. Finns det inte föreslår vi ett nytt golv i stället för att försöka slipa fram något som inte håller. Mer om tjänsten finns under " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipningen till i Hässelby",
  "steps": [
    ("Platsbesök", "Vi frågar efter byggår och lyfter mattan i ett hörn."),
    ("Asbestprov", "Prov tas på okända underlag i hus från 1940–1980."),
    ("Skriftligt kostnadsförslag", "Rivning, spikdragning och slipning var för sig."),
    ("Rivning", "Mattan tas bort och spikarna dras."),
    ("Slipning", "Grov-, mellan- och finslipning efter golvets skick."),
    ("Ytbehandling", "Lack, olja eller såpa efter ditt val."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i Hässelby",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete i ett småhus som du äger och bor i, och det gäller också att sanera asbest i samband med byggarbete. Att mäta asbest ger däremot inget rotavdrag.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för golvslipning i Hässelby?",
  "price": [
    "Golvytan, om mattan ska rivas, hur många spikar som ska dras, om asbestprov behövs, golvets skick och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan det finnas asbest under plastmattan i min villa i Hässelby?",
     "I hus från 1940–1980 är det enligt Boverket sannolikt att asbest finns någonstans, och asbesthaltiga utjämningsmassor användes ibland. Bara ett prov ger svar."),
    ("Varför är golvet under linoleummattan fullt av spik?",
     "Byggnadsvårdsföreningen skriver att golvet förmodligen varit täckt med masonit och linoleum, och att alla spikar ska tas ur före slipning."),
    ("Ger asbestsanering rotavdrag i Hässelby?",
     "Skatteverket ger rotavdrag för att sanera asbest i samband med byggarbete, men inte för att mäta asbest."),
    ("Vad händer om det inte finns något trägolv under mattan?",
     "Då föreslår vi ett nytt golv i stället. Vi lyfter mattan i ett hörn redan vid platsbesöket, så att du vet innan något rivs."),
  ],
  "sources": [_of("Hässelby villastad", "vasterort/hasselby-vallingby/hasselby-villastad"), _VARSAM, _BOV_ASB,
              _SBF_FISKBEN, _SBF_TRAGOLV, _GBR, _SKV],
  "cta": ("Har du ett golv under en gammal matta i Hässelby?", "Boka ett gratis platsbesök, så lyfter vi mattan i ett hörn och tar reda på vad som finns under innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat furugolv i en villa från mitten av 1900-talet",
     "freshly sanded and oiled pine floorboards in an empty living room of a mid-20th century Swedish villa, large window to a garden, white walls, soft daylight" + _SFX),
    ("Gammal linoleummatta som lyfts i ett hörn så att brädgolvet syns",
     "close view of the corner of a room where an old patterned linoleum floor covering has been peeled back, revealing old wooden floorboards with many small nails, daylight" + _SFX),
    ("Slipat furugolv med kvistar och smala springor",
     "close view of old pine floorboards after nail removal, small filled nail holes in rows, ready for sanding, soft daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"golvslipning-spanga.html": {
  "kind": "district", "service": "golvslipning", "ort": "Spånga", "svc_label": "Golvslipning",
  "title": "Golvslipning i Spånga – villornas breda originalgolv",
  "description": "Golvslipning i Spånga: breda originalgolv i villastädernas äldre villor, springor som växlar med årstiderna, hyvling mot slipning och sickling.",
  "h1": "Golvslipning i Spånga",
  "lead": "I Spångas äldre villor ligger ibland de breda brädgolven kvar från byggåret, bucklig efter hundra år och med springor som växlar med årstiderna. Geal Entreprenad AB slipar, sicklar och lagar golv i villorna i Solhem, Bromsten och Flysta och hjälper dig att välja hur mycket av patinan som ska vara kvar.",
  "card": "Breda originalgolv och patina.",
  "sections": [
    {"id": "villorna-spanga", "anchor": "Villorna",
     "h2": "Villastädernas äldre hus",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur Spånga på 1910-talet fick status som municipalsamhälle, och hur villastäderna fick fritt liggande hus på stora trädgårdstomter om 1 500–3 000 kvadratmeter. När nya planer togs fram under 1930-talet gjordes tomterna mindre, 700–1 000 kvadratmeter. I Solhem fick bara en tiondel av tomten bebyggas.",
       "Villastäderna var privat organiserade och bebyggelsen består enligt vägledningen i huvudsak av individuellt utformade enfamiljshus med trä som dominerande fasadmaterial. Stadens områdesfakta för 2025 räknar 1 946 småhus med äganderätt i Solhem. Vägledningen beskriver hur villastäderna successivt har förtätats med nya hus, men i de äldre husen kan originalgolven finnas kvar under senare mattor eller lager av färg.",
     ],
     "aside": {"title": "Villastaden enligt vägledningen", "items": [
       "Municipalsamhälle på 1910-talet", "Tomter 1 500–3 000 m²", "1930-talets tomter 700–1 000 m²", "Trä som dominerande material"]}},
    {"id": "buckliga-spanga", "h2": "Buckliga golv med stora springor",
     "paras": [
       "En läsare frågade Svenska Byggnadsvårdsföreningen hur man renoverar buckliga originalgolv från början av 1900-talet med stora springor och rester av färg och fernissa. Svaret var att golvet sannolikt är av hög kvalitet och bör sparas. Med ett brytjärn för golv går det ofta att demontera brädorna försiktigt, och ibland kan de vändas och läggas tillbaka, helst med kärnsidan uppåt. Vid omläggningen kan brädorna bankas ihop så att springorna minskar, och då kan det behövas en bräda i samma tjocklek i ytterkanten.",
       "Föreningen varnar för att lägga golvet för tajt, eftersom träet rör sig med årstiderna: springorna är stora på senvintern och små på sensommaren. Ett enklare alternativ är att limma i smala lister i springorna och handhyvla dem till golvnivå. Ska golvet läggas om helt finns mer under " + _L.format("golvlaggare-spanga.html", "golvläggare i Spånga") + ".",
     ],
     "aside": {"title": "Ett buckligt golv kan", "items": [
       "Lyftas med brytjärn", "Vändas med kärnsidan upp", "Bankas ihop", "Kompletteras med en bräda i kanten"]}},
    {"id": "patina-spanga", "h2": "Slipa, hyvla eller sickla?",
     "paras": [
       "Gammal färg och fernissa kan enligt Byggnadsvårdsföreningen normalt sicklas bort. Är tiljorna tjocka går det att slipa, men då försvinner patinan och en del av historien. Hyvling ger enligt föreningen en vackrare och mer motståndskraftig yta, men handhyvling är ett grannlaga arbete.",
       "I ett annat svar, om lackade och slitna furugolv i ett trähus från 1904, föreslår föreningen att en slipning eller helst en sickling kan vara en kompromiss, och att hantverksmässigt lagade skador kan ge en extra dimension. Vi lägger fram alternativen för dig och provar på en mindre yta innan hela rummet tas.",
     ],
     "aside": None},
    {"id": "fukt-spanga", "h2": "Rätt fukt innan ytbehandlingen",
     "paras": [
       "Golvbranschens riktlinjer SLIP 22 säger att golvet inte ska ytbehandlas när luftfuktigheten inomhus ligger utanför 30–60 procent eller när fuktkvoten i trät ligger utanför 6–10 procent. Problemet är enligt riktlinjerna inte luftfuktigheten i sig utan variationerna, som kan ge sprickor i spacklade fogar.",
       "I en gammal villa med stora springor tar vi därför hänsyn till årstiden. Lagar vi springor med lister gör vi det när golvet varken är som mest hopkrympt eller som mest svällt, och vi mäter fukten innan lack, olja eller såpa kommer på. Mer om tjänsten finns under " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipningen till i Spånga",
  "steps": [
    ("Platsbesök", "Vi ser på brädorna, springorna och tidigare behandling."),
    ("Prov", "Sickling eller slipning provas på en liten yta."),
    ("Skriftligt kostnadsförslag", "Lyftning, lagning och slipning var för sig."),
    ("Lagning", "Brädor lyfts, vänds eller bankas ihop där det behövs."),
    ("Slipning eller sickling", "Så skonsamt som golvet tillåter."),
    ("Ytbehandling", "Efter fuktmätning, med såpa, olja eller lack."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i Spånga",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete i ett småhus som du äger och använder som bostad. Är huset yngre än fem år får arbetet bara återställa det ursprungliga skicket.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för golvslipning i Spånga?",
  "price": [
    "Golvytan, om brädorna ska lyftas och läggas om, springor och lagningar, om färg eller fernissa ska sicklas bort och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan ett buckligt originalgolv i en villa i Spånga räddas?",
     "Ofta ja. Byggnadsvårdsföreningen beskriver hur brädorna kan lyftas med brytjärn, vändas med kärnsidan uppåt och bankas ihop."),
    ("Varför är springorna i mitt gamla golv i Spånga större på vintern?",
     "Träet rör sig med årstiderna. Enligt Byggnadsvårdsföreningen är springorna stora på senvintern och små på sensommaren."),
    ("Är hyvling bättre än slipning för ett gammalt brädgolv?",
     "Byggnadsvårdsföreningen skriver att hyvling ger en vackrare och mer motståndskraftig yta, men att handhyvling är ett grannlaga arbete."),
    ("Kan gammal fernissa tas bort utan att golvet slipas?",
     "Ja, Byggnadsvårdsföreningen skriver att gammal färg och fernissa normalt kan sicklas bort."),
  ],
  "sources": [_VARSAM, _of("Solhem", "vasterort/jarva/solhem"), _SBF_BUCKL, _SBF_SEKEL, _GBR, _SKV],
  "cta": ("Har du ett gammalt golv i Spånga som du vill spara?", "Boka ett gratis platsbesök, så provar vi sickling eller slipning på en liten yta innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Brett brädgolv i en äldre trävilla efter skonsam slipning",
     "wide old pine floorboards after gentle sanding in an early 1900s Swedish wooden villa, warm honey tone with visible knots and patina, white panelled walls, tall window with garden view, soft daylight" + _SFX),
    ("Golvbrädor som lyfts så att bjälklaget syns",
     "a flooring pry bar lying on wide old pine floorboards where two boards have been carefully lifted, exposing the joists below, daylight" + _SFX),
    ("Breda furubrädor efter skonsam slipning",
     "close view of thin wooden slivers glued into the gaps between old wide pine floorboards and planed flush, soft daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"golvslipning-osteraker.html": {
  "kind": "district", "service": "golvslipning", "ort": "Österåker", "svc_label": "Golvslipning",
  "title": "Golvslipning i Österåker – sommarhus som blivit bostad",
  "description": "Golvslipning i Österåker: golv i sommarvillor och stugor som byggts om för åretruntboende, mörka golv under gamla mattor, springor och rotavdrag.",
  "h1": "Golvslipning i Österåker",
  "lead": "I Österåker har många sommarhus och stugor byggts om för att gå att bo i året runt. Golven från sommartiden ligger ofta kvar, ibland under mattor från senare decennier. Geal Entreprenad AB slipar och behandlar golv i Åkersberga, Svinninge och resten av kommunen och börjar med att ta reda på vad golvet har varit med om.",
  "card": "Golv i sommarhus som blivit bostad.",
  "sections": [
    {"id": "sommarhus-osteraker", "anchor": "Sommarhusen",
     "h2": "Från sommarvilla till permanentbostad",
     "paras": [
       "Österåkers kommuns råd och riktlinjer för byggande i Svinninge, från 2008, beskriver området som ett blandområde med permanent- och fritidsboende där åretruntboendet successivt ökat. Fritidshusen byggs om och till för att passa dagens krav på permanentbostäder, och många hus ersätts av nya villor. Svinningeudd och Nantes beskrivs som kommunens äldsta och bäst bevarade sommarhusbebyggelse.",
       "Riktlinjerna berättar också om sportstugorna från 1930-talet: enkla, ändamålsenliga envåningshus med den timrade enkelstugan som förebild, ofta uppförda som typhus och vinterbonade för att kunna användas på vintern. Efter sekelskiftet 1900 blev den röda stugan med vita knutar populär som sommarvilla eller egnahem.",
     ],
     "aside": {"title": "Svinninge enligt riktlinjerna", "items": [
       "Blandat permanent- och fritidsboende", "Sommarvillor från sekelskiftet", "Vinterbonade sportstugor från 1930-talet", "Många hus byggs om och till"]}},
    {"id": "scb-osteraker", "h2": "Småhusen i kommunen",
     "paras": [
       "SCB:s bostadsstatistik för 2025 räknar 13 635 lägenheter i småhus i Österåkers kommun, och 11 981 av dem är äganderätter. 814 finns i hus byggda före 1931 och 330 i hus från 1931–1940, medan flest tillkom på 1960- och 1970-talen, 5 215 tillsammans. Golven i huset beror alltså mycket på när det byggdes och hur det har använts.",
       "Ett hus som stått kallt på vintern och nu värms året runt utsätter golvet för andra förhållanden än förr. Byggnadsvårdsföreningen påminner i ett svar om att golvet rör sig och att ett torrt klimat ger hoptorkade plankor. När en läsare hittade ett furugolv med upp till 5 millimeter breda springor under korkmattan i ett sommarhus från omkring 1900 var svaret att det inte är så mycket på så breda tiljor, och att det snyggaste är att lägga om golvet och slå ihop brädorna.",
     ],
     "aside": {"title": "Småhus i Österåker enligt SCB", "items": [
       "13 635 lägenheter i småhus", "11 981 äganderätter", "814 byggda före 1931", "330 från 1931–1940"]}},
    {"id": "morkt-osteraker", "h2": "Mörkt och klibbigt golv under mattan",
     "paras": [
       "En läsare skrev till Byggnadsvårdsföreningen om ett torp där plastmattan i köket hade rivits och golvet under verkade tjärat, mörkt och lite klibbigt. Svaret var att golvet antagligen tagit färg av tjärpapp som lagts som underlag till linoleummattor. Föreningen föreslog att prova att lösa upp det med T-sprit eller balsamterpentin och att använda mask, och varnade för att det kan bli kladd av att slipa på tjäran.",
       "Föreningen skriver också att man helst bör undvika golvslip på sådana golv, eftersom den tar ganska mycket av brädornas tjocklek och lämnar en slät och trist yta, och att man i första hand kan slipa med en liten excenterslip på 125–150 millimeter. Vi provar oss fram på en liten yta innan vi väljer metod för hela rummet.",
     ],
     "aside": None},
    {"id": "behandling-osteraker", "h2": "Ytbehandling för ett hus som används året runt",
     "paras": [
       "När golvet är slipat ska det behandlas efter hur huset används nu. Golvbranschens riktlinjer SLIP 22 säger att ytbehandling inte ska göras när luftfuktigheten inomhus ligger utanför 30–60 procent eller fuktkvoten i trät utanför 6–10 procent. I ett hus som nyss börjat värmas året runt mäter vi därför innan vi lackar eller oljar.",
       "Efter tjärpapp kan föreningen rekommendera linoljefärg, med reservationen att tjäran kan slå igenom. Ett såpat eller oljat golv är enklare att bättra på i ett hus där det går in och ut mycket. Ska golvet bytas i stället finns mer under " + _L.format("golvlaggare-osteraker.html", "golvläggare i Österåker") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipningen till i Österåker",
  "steps": [
    ("Platsbesök", "Vi ser på golvet och frågar hur huset har använts."),
    ("Prov", "Rengöring eller slipning provas på en liten yta."),
    ("Skriftligt kostnadsförslag", "Rivning, slipning och ytbehandling var för sig."),
    ("Förberedelse", "Mattor rivs, lister lossas och spikar tas om hand."),
    ("Slipning", "Så skonsamt som golvet tillåter."),
    ("Ytbehandling", "Efter fuktmätning, med det du valt."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i Österåker",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete i ett småhus, och till småhus räknas enligt Skatteverket både villor, radhus och fritidshus. Huset ska användas som bostad och ägas av dig.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för golvslipning i Österåker?",
  "price": [
    "Golvytan, om mattor ska rivas, golvets tidigare behandling, hur mycket springor och lagningar som behövs och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför är golvet under plastmattan i min stuga i Österåker mörkt och klibbigt?",
     "Byggnadsvårdsföreningen skriver att golvet antagligen tagit färg av tjärpapp som låg under linoleummattor."),
    ("Ska ett tjärfärgat golv slipas med golvslip?",
     "Helst inte. Byggnadsvårdsföreningen råder att i första hand använda en liten excenterslip på 125–150 millimeter, eftersom golvslipen tar mycket av brädornas tjocklek."),
    ("Är 5 millimeters springor i ett gammalt sommarhusgolv i Österåker mycket?",
     "Inte på breda tiljor, enligt Byggnadsvårdsföreningen. Vill du få bort dem är det snyggaste att lägga om golvet och slå ihop brädorna."),
    ("Ger golvslipning i ett fritidshus i Österåker rotavdrag?",
     "Ja, Skatteverket räknar fritidshus som småhus. Du ska äga huset och använda det som bostad."),
  ],
  "sources": [_OST_SVIN, _SCB_PER, _SCB_UPPL, _SBF_SPRING, _SBF_TJARA, _GBR, _SKV],
  "cta": ("Har du ett gammalt golv i ett hus i Österåker?", "Boka ett gratis platsbesök, så provar vi metoden på en liten yta innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Slipat furugolv i en äldre röd stuga med vita knutar",
     "interior of an old red Swedish cottage with white corners, freshly sanded wide pine floorboards with a soft oiled finish, white painted wood walls, small paned window with view of pine trees, soft daylight" + _SFX),
    ("Mörkt fläckigt golv där en gammal matta tagits bort",
     "close view of old wooden floorboards with dark tar-like stains in a pattern left after an old floor covering was removed, small orbital sander lying on the floor, daylight" + _SFX),
    ("Breda furubrädor med springor i ett gammalt sommarhus",
     "close view of wide old pine floor planks with gaps of a few millimetres between them in an old summer house, soft light from a window" + _SFX),
  ],
},
}
