# -*- coding: utf-8 -*-
"""Fönsterbyte – ortsidor v27: Enskede, Farsta, Hässelby, Spånga, Vällingby, Älvsjö (2026-10-26).
Hubb: fonsterbyte.html (TJ_HUB["fonsterbyte"]). Intent: byta fönster – skild från ortens fonsterrenovering-<ort>.html
(renovera befintliga bågar), som länkas där den finns. Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.
Vällingby har egen trust-rad (sidnyckel "trust"): rotavdrag ges inte för fönsterbyte i bostadsrätt.

Lokal vinkel per sida:
Enskede – Gamla Enskede som riksintresse (AB 112, 1908, landets första radhus, fönster som värdebärande detalj),
  villorna med äganderätt och bostadsrätterna i de två- och trevånings husen längs de breda gatorna (områdesfakta),
  stadens lista över ändringar som räknas som fönsterbyte, Enskede gård och Enskededalen.
Farsta – Tallkrogens småstugor (1933, närmare 1 000 stugor, mer än 10 hustyper, fabrikstillverkade byggnadsdelar),
  fönster i fasadliv enligt Varsam, typritningssamlingen 1927–1957, att flytta fönster från fasadliv till indraget,
  Farsta stadsdelsområdes radhus och småhus (områdesfakta, Stockholms spår).
Hässelby – villastaden utan markering i Varsam-tabellen men med detaljplan och varsamhetskrav, Hässelby strand och
  Hässelby gård som kulturhistoriskt värdefulla tunnelbanestäder, MÖD 2019:25 om vad som avsevärt påverkar
  utseendet, grupphusen och helhetsperspektivet.
Spånga – villastäderna och glasverandorna, en ny fönsteröppning (Boverket: inget lov, ingen anmälan om inte bärande
  delar påverkas väsentligt; staden: insyn, förstärkning), Solhem som kulturhistoriskt värdefull miljö.
Vällingby – riksintresset Vällingby–Råcksta (AB 120) med fönster som värdebärande detalj, Atlantis och Omega,
  kedjehus med regelbunden fönstersättning, radhus med bostadsrätt (stadgarna avgör, Skatteverket: inget rot för
  fönsterbyte i bostadsrätt), områdesfakta för Vällingby och Råcksta.
Älvsjö – villastaden enligt Stadsmuseets inventering (Hem på landet 1908, ett hundratal tomter 1915, stadsplan 1921,
  nya fasad- och takmaterial och tilläggsisolering som förändrat husen), fönstrets läge i fasaden när huset
  tilläggsisoleras (stadens lista), del av Älvsjö som kulturhistoriskt värdefull miljö med generösa byggrätter.

Fakta endast från källorna i respektive 'sources', öppnade med curl (UA Mozilla) 2026-10-26, alla svarade 200;
pdf:erna (riksintressen, Varsam, områdesfakta, Stockholms spår, Älvsjö-inventeringen) har textlager. Skatteverket
lästes med curl (webbläsar-UA): småhus – reparera eller byta ut fönster, montera bullerglas och isolerglas, byta
fönsterbleck, femårsregeln; bostadsrätt – byta fönster och arbeta mellan eller på utsidan av fönster ger inget
avdrag, arbete på insidan (glas i inre båge, tätningslist, innerfönster och fönsterfoder) ger avdrag.
Strukna / ej använda: Stadsmuseets svarstid, handläggningstider och avgifter, BBR:s U-värden, vilka fönster enskilda
hus i orterna har (skrivet som villkor), att Tallkrogens stugor har en viss fönstertyp utöver Varsams beskrivning av
småstugeområdena, Hem på landet som grundare av Duvbo (motsägelse mellan källor). Inga priser, garantier, omdömen,
egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_TRUST_BRF = ["Gratis besök och kostnadsförslag", "Underlag till bygglov och förening"]
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"

_STH_FD = ("Stockholms stad – Fönster och dörrar", _SB + "fonster-och-dorrar/")
_STH_FAS = ("Stockholms stad – Fasadändring", _SB + "fasadandring/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_BV_TAK = ("Boverket – Ändra fasad eller tak",
           "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/andra-fasad-eller-tak/")
_BV_MOD = ("Boverket – Fönsterbyten: bygglovsplikt och förvanskningsförbudet (MÖD 2019:25)",
           "https://www.boverket.se/sv/PBL-kunskapsbanken/teman/kulturvarden/kulturvarden-i-teori-och-praktik/rattsfall/fonsterbyten/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 12 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_TALLK = ("Stockholms stadsmuseum – Stockholms spår: Tallkrogen (pdf)",
          "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000041.pdf")
_FARSTA = ("Stockholms stadsmuseum – Stockholms spår: Farsta (pdf)",
           "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000015.pdf")
_ALV_INV = ("Stadsmuseet – Inventering av Älvsjö villastad (Stockholmskällan, pdf)",
            "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf")


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_ROT_HUS = ("I ett småhus räknar Skatteverket det som rotarbete att reparera eller byta ut fönster, att montera bullerglas "
            "och isolerglas och att byta fönsterbleck. Är bostaden yngre än fem år får arbetet bara återställa det "
            "ursprungliga skicket, och nytt material ska vara likvärdigt med det gamla.")
_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor "
            "ger inget avdrag, och Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ ENSKEDE
"fonsterbyte-enskede.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Enskede", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Enskede – villor och hus i riksintresset",
  "description": "Fönsterbyte i Enskede: varför nya fönster i Gamla Enskede kräver bygglov, vad som räknas som en ändring, villor och bostadsrätter och rotavdrag.",
  "h1": "Fönsterbyte i Enskede",
  "lead": "Gamla Enskede är riksintresse för kulturmiljövården, och fönstren räknas uttryckligen till det som gör området värdefullt. Därför kräver ett fönsterbyte där bygglov även på en villa. Geal Entreprenad AB byter fönster i Enskede och tar fram ritningar och beskrivning så att de nya fönstren håller samma indelning och proportioner som de gamla.",
  "card": "Fönster i riksintresset.",
  "sections": [
    {"id": "riksintresse-enskede", "anchor": "Riksintresset",
     "h2": "Stockholms första trädgårdsstad",
     "paras": [
       "Översiktsplanens riksintressedel beskriver Gamla Enskede som Stockholms första trädgårdsstad, påbörjad 1908 och en föregångare på det bostadssociala området med landets första radhus. Stadsdelen har cirka 10 000 invånare och omfattar nära 300 hektar. Bland de värdebärande karaktärsdragen räknas de enskilda husens ursprungliga byggnadsdetaljer, som fönster, entrédörrar och räcken.",
       "Stockholms stad skriver att bygglov krävs för åtgärder som annars kan vara lovbefriade när huset ligger inom ett riksintresse för kulturmiljövården, som visas med blå ring på Stadsmuseets karta. För en villa i Gamla Enskede betyder det att även ett fönsterbyte som skulle ha varit lovfritt i ett annat område behöver prövas.",
     ],
     "aside": {"title": "Gamla Enskede enligt översiktsplanen", "items": [
       "Riksintresse AB 112", "Påbörjad 1908", "Landets första radhus", "Fönster räknas som värdebärande"]}},
    {"id": "andring-enskede", "h2": "Vad staden räknar som en ändring",
     "paras": [
       "På stadens sida om fönster och dörrar räknas bland annat dessa ändringar upp: att byta material eller kulör, att ändra storlek eller placering, att ändra dimensioner, proportioner eller profilering på karmar, bågar och spröjs, att byta upphängning, till exempel från sidohängda fönster till vippfönster, och att ändra indelningen genom att lägga till spröjs eller ta bort en mittpost. Staden påpekar att en byggnad kan ha karaktäristiska fönster eller en tidstypisk indelning där ändringen påverkar både fasaden och husets karaktär.",
       "Vi mäter därför upp de befintliga fönstren noggrant och ritar de nya med samma luftindelning, spröjs och profiler. Beskrivningen av material och kulör bifogas ansökan. Är fönstren i så gott skick att de kan räddas finns alternativet " + _L.format("fonsterrenovering-enskede.html", "fönsterrenovering i Enskede") + ".",
     ],
     "aside": {"title": "Räknas som ändring av fönster", "items": [
       "Nytt material eller ny kulör", "Annan storlek eller placering", "Andra profiler eller spröjs", "Annan upphängning eller indelning"]}},
    {"id": "hustyper-enskede", "h2": "Villor och bostadsrätter i samma stadsdel",
     "paras": [
       "Riksintressedelen beskriver bebyggelsen som två- och trevånings affärs- och bostadshus längs de breda gatorna i områdets ytterkanter, och nationalromantisk egnahemsbebyggelse vid de smalare gatorna inne i området. Stadens områdesfakta för 2025 räknar 5 117 bostäder i Gamla Enskede. 898 av dem är småhus med äganderätt, 2 360 är bostadsrätter och 1 331 hör till allmännyttan.",
       "Det gör att två grannar i Enskede kan stå inför helt olika fönsterbyten. Villaägaren beställer själv och söker bygglov. I ett flerbostadshus är det föreningen eller fastighetsägaren som beställer, och då krävs bygglov för ändringar på fasader mot allmän plats även utanför riksintresset. Vi tar fram underlaget i båda fallen.",
     ],
     "aside": None},
    {"id": "grannar-enskede", "h2": "Enskede gård och Enskededalen",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden markerar också Enskede gård och Enskededalen som kulturhistoriskt värdefulla miljöer, och för Enskededalen finns ett äldre miljöprogram. Vägledningen beskriver att 1920-talets klassiska formspråk blev rådande i bland annat Enskededalen, med enkla volymer i ett och ett halvt plan och symmetriskt uppbyggda fasader.",
       "Staden skriver att äldre miljöprogram och typritningssamlingar inte har någon juridisk status i bygglovsprövningen, men att de är ett bra underlag för att förstå områdets karaktär. Vi använder dem när vi ritar nya fönster, så att de passar huset de sitter i. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Enskede",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter och fotograferar fönstren."),
    ("Kartan", "Vi kontrollerar riksintresset och Stadsmuseets klassning."),
    ("Ritningar", "Fasadritning och detaljritning med samma indelning."),
    ("Bygglov", "Du söker lov med vårt underlag."),
    ("Tillverkning", "Fönstren tillverkas efter uppmätning."),
    ("Montage", "Byte, drevning, tätning, foder och bleck."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Enskede",
  "rot": [_ROT_HUS, _ROT_SUM],
  "price_h2": "Vad påverkar priset för fönsterbytet i Enskede?",
  "price": [
    "Antal och storlek på fönstren, spröjs och luftindelning, profiler och glas, om fönstren tillverkas efter uppmätning, bleck och foder och om bygglovsritningar behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag bygglov för att byta fönster på min villa i Gamla Enskede?",
     "Ja. Gamla Enskede är riksintresse för kulturmiljövården, och där kräver staden bygglov även för åtgärder som annars är lovbefriade."),
    ("Räknas det som en ändring att byta till fönster med annan spröjs i Enskede?",
     "Ja. Staden räknar ändrade profiler och ändrad indelning, som tillagd spröjs eller borttagen mittpost, som ändring av fönster."),
    ("Hur många småhus finns det i Gamla Enskede?",
     "Stadens områdesfakta för 2025 räknar 898 småhus med äganderätt av områdets 5 117 bostäder."),
    ("Har miljöprogrammet för Enskededalen någon juridisk betydelse?",
     "Nej, enligt staden har äldre miljöprogram ingen juridisk status i bygglovsprövningen, men de är ett bra underlag."),
  ],
  "sources": [_RIKS, _STH_KL, _STH_FD, _of("Gamla Enskede", "soderort/enskede/gamla-enskede"), _VARSAM, _SKV],
  "cta": ("Ska fönstren bytas i Enskede?", "Boka ett gratis platsbesök, så mäter vi upp fönstren och tar fram underlaget till bygglovet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nationalromantisk trävilla med småspröjsade fönster i en trädgårdsstad",
     "early 1900s Swedish national romantic wooden villa painted falu red with white window frames, small-paned upper sashes, steep red tile roof, front garden with hedge, curving street in a garden suburb, summer" + _SFX),
    ("Uppmätning av ett äldre fönster med spröjs",
     "close view of an old white painted wooden window with small panes above a transom, a wooden folding ruler lying on the window sill, daylight" + _SFX),
    ("Bostadshus med butiker i bottenvåningen längs en bred gata",
     "two and three storey plastered residential buildings with small shop windows on the ground floor along a broad tree-lined street in an early 1900s Stockholm garden suburb, white windows, empty street, no cyclists, no cars, summer" + _SFX),
  ],
},

# ------------------------------------------------------------------ FARSTA
"fonsterbyte-farsta.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Farsta", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Farsta – småstugorna i Tallkrogen",
  "description": "Fönsterbyte i Farsta: småstugorna i Tallkrogen med fönster i fasadliv, typritningarna, när nya fönster kräver bygglov och rotavdrag för radhus och villor.",
  "h1": "Fönsterbyte i Farsta",
  "lead": "I Tallkrogen står närmare tusen småstugor byggda efter ett fåtal typritningar, med fönstren placerade i fasadens liv. Ett fönsterbyte där handlar om att behålla det läget och den indelningen. Geal Entreprenad AB byter fönster på småstugor, radhus och villor i Farsta och tar fram underlaget om bygglov behövs.",
  "card": "Småstugor och radhus.",
  "sections": [
    {"id": "tallkrogen-farsta", "anchor": "Tallkrogen",
     "h2": "Tallkrogens småstugor",
     "paras": [
       "Stadsmuseets Stockholms spår om Tallkrogen berättar att utbyggnaden påbörjades 1933 och att området blev det största småstugeområdet i Söderort. Närmare 1 000 småstugor växte upp på den flacka åkermarken under det närmaste decenniet. Vid en första anblick kan det se ut som samma stuga upprepad i det oändliga, men området rymmer mer än tio olika hustyper, och byggnadsdelarna levererades färdiga från fabriken.",
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver småstugeområdenas hus som enkla volymer, uteslutande i trä med fönster placerade i fasadliv, med stående träpanel med tunn lockläkt och tak av enkupigt eller tvåkupigt rött lertegel. Tallkrogen är i vägledningens tabell markerat som kulturhistoriskt värdefull miljö med ett äldre miljöprogram.",
     ],
     "aside": {"title": "Tallkrogen", "items": [
       "Utbyggt från 1933", "Närmare 1 000 småstugor", "Mer än tio hustyper", "Fönster i fasadliv"]}},
    {"id": "fasadliv-farsta", "h2": "Fönstret ska sitta kvar i fasadlivet",
     "paras": [
       "På stadens lista över ändringar av fönster finns just exemplet att ett fönster flyttas från placering i fasadliv till att bli indraget från fasadlivet. Det räknas som en ändring, liksom att ändra storlek, profiler, upphängning och indelning. För en småstuga där fönstren sitter i fasadens liv är det därför viktigt att det nya fönstret monteras i samma läge och inte flyttas in.",
       "Vi mäter karm och foder på det gamla fönstret och beställer det nya efter de måtten. Bleck och foder sätts tillbaka så att stugans fasad ser ut som förut. Är fönstren friska nog att renoveras i stället kan det vara ett bättre val, och då går vi igenom båda alternativen på platsbesöket.",
     ],
     "aside": {"title": "Vid byte i en småstuga", "items": [
       "Samma läge i fasaden", "Samma luftindelning", "Foder och bleck tillbaka", "Kontroll av kartan först"]}},
    {"id": "typritningar-farsta", "h2": "Typritningarna som underlag",
     "paras": [
       "Enligt vägledningen samlade stadsbyggnadskontoret i slutet av 1970-talet alla typritningar från 1927 till 1957 i en sammanställning, för att den som ville ändra sin stuga skulle ha ett enkelt åtkomligt underlag. Staden skriver att äldre miljöprogram och typritningssamlingar kan beställas, och att de inte har juridisk status i bygglovsprövningen men är ett bra underlag för att förstå områdets karaktär.",
       "Vi tar gärna hjälp av typritningen för din hustyp när vi ritar nya fönster. Ligger huset i ett område som är utpekat som särskilt värdefullt, eller är det blå- eller grönmarkerat på Stadsmuseets karta, behövs bygglov, och då är ritningen ett bra stöd i ansökan.",
     ],
     "aside": None},
    {"id": "radhus-farsta", "h2": "Radhus och villor i resten av Farsta",
     "paras": [
       "Farsta byggdes enligt Stockholms spår som Söderorts första ABC-stad, och i stadsdelens utkanter lades flera stora radhusområden. Stadens områdesfakta för 2025 räknar 3 806 småhus med äganderätt och 639 småhus med bostadsrätt i Farsta stadsdelsområde, varav 941 äganderätter i Tallkrogen och 327 i Svedmyra.",
       "I ett radhusområde är det klokt att tänka på grannarna. Vägledningen råder att förändringar i sammanhållna grupper av villor, radhus och kedjehus utformas utifrån ett helhetsperspektiv. Byter du fönster i en länga ser vi gärna att de nya liknar grannarnas. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Farsta",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter fönstren och tittar på fasaden."),
    ("Kartan", "Vi kontrollerar Stadsmuseets klassning för huset."),
    ("Förslag", "Nya fönster med samma läge, indelning och profiler."),
    ("Lov", "Ritningar och beskrivning när bygglov krävs."),
    ("Montage", "Fönstren monteras i fasadlivet och tätas."),
    ("Avslut", "Foder och bleck tillbaka och genomgång med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Farsta",
  "rot": [_ROT_HUS,
          "Är radhuset en bostadsrätt ger Skatteverket inget rotavdrag för att byta fönster eller arbeta på deras utsida, men för arbete på insidan som du ansvarar för enligt stadgarna. " + _ROT_SUM],
  "price_h2": "Vad påverkar priset för fönsterbytet i Farsta?",
  "price": [
    "Antal och storlek på fönstren, om de tillverkas efter mått, luftindelning och spröjs, foder och bleck, åtkomst och om bygglovsunderlag behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag flytta in fönstret från fasadlivet på min småstuga i Tallkrogen?",
     "Staden räknar en sådan flytt som en ändring av fönstret. Där bygglov krävs prövas den, och i en småstuga med fönster i fasadliv påverkar den karaktären."),
    ("Hur många olika hustyper finns det i Tallkrogen?",
     "Enligt Stadsmuseets Stockholms spår rymmer området mer än tio olika hustyper, trots att stugorna kan se lika ut."),
    ("Var hittar jag typritningen för min småstuga i Farsta?",
     "Staden skriver att äldre miljöprogram och typritningssamlingar kan beställas från staden."),
    ("Ska fönstren i vårt radhus i Farsta se ut som grannarnas?",
     "Stadens vägledning råder att förändringar i sammanhållna grupper av radhus utformas utifrån ett helhetsperspektiv, så det är oftast bäst."),
  ],
  "sources": [_TALLK, _FARSTA, _VARSAM, _STH_FD, _STH_KL, _of("Farsta stadsdelsområde", "soderort/farsta/farsta-stadsdelsomrade"),
              _of("Tallkrogen", "soderort/farsta/tallkrogen"), _of("Svedmyra", "soderort/farsta/svedmyra"), _SKV],
  "cta": ("Ska fönstren bytas i Farsta?", "Boka ett gratis platsbesök, så mäter vi upp fönstren och kontrollerar kartan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Småstuga i trä med fönster i fasadliv och rött tegeltak",
     "small 1930s Swedish wooden cottage with vertical board-and-batten siding painted pale yellow, white windows set flush with the facade, red clay tile roof, small garden with fruit trees and hedge, quiet street, summer" + _SFX),
    ("Nytt träfönster monterat i liv med en panelfasad",
     "close view of a new white wooden window mounted flush with vertical board-and-batten siding on a small wooden house, neat trim boards and a metal sill flashing, daylight" + _SFX),
    ("Rad av likadana småstugor längs en gata",
     "row of identical small 1930s Swedish wooden cottages along a gently curving street, pale grey and green painted facades, red tile roofs, hedges and street trees, summer afternoon" + _SFX),
  ],
},

# ------------------------------------------------------------------ HÄSSELBY
"fonsterbyte-hasselby.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Hässelby", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Hässelby – villastaden och grupphusen",
  "description": "Fönsterbyte i Hässelby: när nya fönster på en villa är lovfria, detaljplan och varsamhetskrav, grupphusen, Hässelby strand och gård och rotavdrag.",
  "h1": "Fönsterbyte i Hässelby",
  "lead": "I Hässelby villastad kräver ett fönsterbyte på en villa i regel inte bygglov, men det betyder inte att vilka fönster som helst passar. Detaljplanen och varsamhetskravet gäller ändå. Geal Entreprenad AB byter fönster på villor, radhus och kedjehus i Hässelby och hjälper dig att välja fönster som passar huset och grannarnas.",
  "card": "Villor, radhus och grupphus.",
  "sections": [
    {"id": "villastaden-hasselby", "anchor": "Villastaden",
     "h2": "Villastaden med hus från många årtionden",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 7 029 bostäder i Hässelby villastad, och 4 757 av dem är småhus med äganderätt. Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur många villor där på 1960- och 1970-talen ersattes av täta, sammanhållna grupper av enhetlig småhusbebyggelse, och hur hus på tomter kring 600 kvadratmeter har kompletterat den äldre bebyggelsen.",
       "I vägledningens tabell saknar Hässelby villastad markering som kulturhistoriskt värdefull miljö. Hässelby strand och Hässelby gård, som hör till tunnelbanestäderna, är däremot markerade. Stadsmuseets karta visar vad som gäller för det enskilda huset, och staden påpekar att det finns områden som ännu inte är inventerade.",
     ],
     "aside": {"title": "Hässelby i vägledningen", "items": [
       "Hässelby villastad – villastad", "Hässelby strand – värdefull miljö", "Hässelby gård – värdefull miljö", "Grupphus från 1960–70-talen"]}},
    {"id": "lovfritt-hasselby", "h2": "Lovfritt – men inte fritt",
     "paras": [
       "Stockholms stad skriver att det inte längre krävs bygglov för fasadändringar på en- och tvåbostadshus om vissa förutsättningar är uppfyllda. Fasadändringar som inte kräver lov ska ändå stämma med detaljplanen eller vara en liten avvikelse som inte motverkar planens syfte. Boverket påminner om att ändringen ska göras varsamt och anpassas till omgivningen, och att den inte får innebära en betydande olägenhet för grannarna.",
       "Staden skriver också att bygglov kan behövas om huset omfattas av varsamhetsbestämmelser i detaljplanen, även utanför riksintressen och särskilt värdefulla områden. Vi tittar därför på detaljplanen för fastigheten i stadens e-tjänst innan vi beställer fönster, så att du inte bygger fel utan att veta om det.",
     ],
     "aside": {"title": "Kontrollera före beställning", "items": [
       "Stadsmuseets karta", "Detaljplanens bestämmelser", "Varsamhetsbestämmelser", "Grannarnas fönster"]}},
    {"id": "domen-hasselby", "h2": "När ändras utseendet avsevärt?",
     "paras": [
       "Boverket redovisar två domar från Mark- och miljööverdomstolen om fönsterbyten i 1920-talsklassicerande flerbostadshus, där den ena är vägledande som MÖD 2019:25. Trä hade ersatts av aluminiumklätt trä, profilerna var kantigare och fast spröjs hade ersatts av löstagbar. Domstolen ansåg att skillnaderna var tydliga för en fackman på nära håll men knappt märkbara för den som färdas på gatan, och att bytet därför inte krävde bygglov.",
       "Boverket understryker att domarna bara säger att fönsterbytena inte krävde lov i just de fallen, inte att det gäller alla fönsterbyten. För en bostadsrättsförening i Hässelby strand eller Hässelby gård, där husen ligger i kulturhistoriskt värdefulla miljöer, är det därför klokt att ta fram ett underlag och fråga staden innan man beställer.",
     ],
     "aside": None},
    {"id": "grupper-hasselby", "h2": "Fönster i en grupp av likadana hus",
     "paras": [
       "Vägledningen råder att förändringar i sammanhållna grupper av villor, radhus och kedjehus utformas utifrån ett helhetsperspektiv. I ett grupphusområde från 1960-talet är det fönstren som mest syns när husen jämförs med varandra, så ett byte som ser annorlunda ut än grannarnas märks. Vägledningen nämner också att eternit, som innehöll asbest, var ett populärt fasadmaterial i Hässelby och i många fall har bytts ut. Byts fasadskivorna samtidigt som fönstren bör båda planeras ihop.",
       "Vi föreslår fönster med samma indelning, kulör och proportioner som de ursprungliga, och tar gärna fram ett gemensamt förslag om flera grannar vill byta samtidigt. Ska fasaden också åtgärdas finns mer under " + _L.format("fasadrenovering-hasselby.html", "fasadrenovering i Hässelby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Hässelby",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter fönstren."),
    ("Plan och karta", "Detaljplanen och Stadsmuseets klassning kontrolleras."),
    ("Förslag", "Fönster som passar huset och gruppen."),
    ("Beställning", "Tillverkning efter uppmätta mått."),
    ("Montage", "Byte, drevning, tätning, foder och bleck."),
    ("Genomgång", "Vi går igenom fönstren och skötseln med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Hässelby",
  "rot": [_ROT_HUS, _ROT_SUM],
  "price_h2": "Vad påverkar priset för fönsterbytet i Hässelby?",
  "price": [
    "Antal och storlek på fönstren, indelning och glas, foder och bleck, om fönstren beställs för flera hus samtidigt och om underlag till staden behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag bygglov för att byta fönster på min villa i Hässelby villastad?",
     "Normalt inte, eftersom fasadändringar på en- och tvåbostadshus är lovfria under vissa förutsättningar. Detaljplanen och varsamhetsbestämmelser kan ändå kräva lov."),
    ("Krävde bytet till aluminiumklädda fönster bygglov i MÖD 2019:25?",
     "Nej, domstolen ansåg att ändringen inte avsevärt påverkade utseendet i det fallet. Boverket påpekar att det inte gäller alla fönsterbyten."),
    ("Är Hässelby strand ett kulturhistoriskt värdefullt område?",
     "I stadens vägledning Varsam utveckling är Hässelby strand markerat som kulturhistoriskt värdefull miljö."),
    ("Kan flera grannar i ett radhusområde i Hässelby byta fönster tillsammans?",
     "Ja, och det gör det lättare att hålla ihop utseendet. Vi tar fram ett gemensamt förslag."),
  ],
  "sources": [_of("Hässelby villastad", "vasterort/hasselby-vallingby/hasselby-villastad"), _VARSAM, _STH_FAS, _STH_KL,
              _BV_TAK, _BV_MOD, _SKV],
  "cta": ("Ska fönstren bytas i Hässelby?", "Boka ett gratis platsbesök, så kontrollerar vi detaljplanen och mäter fönstren innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus från 1960-talet med regelbundna fönster i en grupp",
     "row of 1960s Swedish terraced houses with dark brown wooden facades and white window frames in a regular pattern, small front gardens, footpath, birch trees, summer" + _SFX),
    ("Nytt fönster i en villa med träfasad",
     "close view of a newly installed white wooden window in a light grey painted wooden facade of a Swedish villa, neat trim and metal sill, daylight" + _SFX),
    ("Flerbostadshus från 1950-talet i en tunnelbanestad",
     "1950s Swedish three-storey apartment buildings with light rendered facades and regular windows, surrounded by lawns and pine trees, summer daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"fonsterbyte-spanga.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Spånga", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Spånga – villastäderna och nya öppningar",
  "description": "Fönsterbyte i Spånga: nya fönster i villastädernas hus, när en ny fönsteröppning kräver anmälan, glasverandor, Solhem och rotavdrag.",
  "h1": "Fönsterbyte i Spånga",
  "lead": "Spångas villastäder består av individuellt utformade hus från olika tider, ofta med glasverandor och kupor. Ett fönsterbyte där kan vara att ersätta gamla fönster, men också att ta upp ett nytt. Geal Entreprenad AB byter och sätter in fönster i villor i Solhem, Bromsten, Flysta och Sundby och ser till att konstruktionen och grannarna är med i planeringen.",
  "card": "Villor, verandor och nya öppningar.",
  "sections": [
    {"id": "villastad-spanga", "anchor": "Villastäderna",
     "h2": "Villastäder med individuella hus",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur villastäderna var privat organiserade, vilket gav en brokigare bebyggelse än i stadens egnahemsområden. Trä var det dominerande fasadmaterialet, och glasverandor, takkupor och snickarglädje gav stadsdelarna en variation som är tydlig än i dag. I tabellen är Solhem markerat som kulturhistoriskt värdefull miljö, medan Bromsten, Flysta och Sundby saknar sådan markering.",
       "Stadsmuseets inventering av Älvsjö villastad nämner att fastighetsbolaget AB Hem på landet hade anlagt Solhem innan bolaget började sälja tomter i Älvsjö 1908. Stadens områdesfakta för 2025 räknar 1 946 småhus med äganderätt i Solhem och 916 i Bromsten.",
     ],
     "aside": {"title": "Villastäder i Spånga", "items": [
       "Solhem – kulturhistoriskt värdefull", "Bromsten", "Flysta", "Sundby"]}},
    {"id": "oppning-spanga", "h2": "Ett nytt fönster där det inte fanns något",
     "paras": [
       "Boverket skriver att det inte krävs bygglov för att ta upp en ny öppning för ett fönster eller en dörr i ett småhus, och inte heller någon anmälan, så länge du inte gör något som påverkar konstruktionen av byggnadens bärande delar väsentligt. Ändringen ska ändå anpassas till omgivningen och vara varsam mot byggnaden, och ibland krävs bygglov ändå, till exempel nära eller inom särskilt värdefulla byggnader och områden.",
       "Stockholms stad påminner om att nya fönster kan ge ökad insyn som blir en olägenhet för grannarna, och att nya öppningar kan påverka den bärande konstruktionen så att den behöver förstärkas. Vi ser därför på väggen innan vi lovar något. Behövs en förstärkning ritas den, och påverkas bärande delar väsentligt görs en anmälan.",
     ],
     "aside": {"title": "Före en ny fönsteröppning", "items": [
       "Är väggen bärande?", "Behövs förstärkning?", "Insyn mot grannen", "Stadsmuseets karta"]}},
    {"id": "veranda-spanga", "h2": "Glasverandornas fönster",
     "paras": [
       "En glasveranda har ofta fler och mindre rutor än huset i övrigt, och fönstren är en stor del av dess uttryck. Byts de mot fönster med annan indelning ändras verandans karaktär mer än när ett enstaka fönster byts på fasaden. På stadens lista över ändringar av fönster står just att lägga till spröjs eller ta bort en mittpost.",
       "Vi mäter verandans fönster och föreslår nya med samma indelning, eller renovering där det går. För villor i Solhem, som är kulturhistoriskt värdefull miljö, kontrollerar vi kartan innan vi beställer. Mer om att renovera befintliga fönster finns under " + _L.format("fonsterrenovering-spanga.html", "fönsterrenovering i Spånga") + ".",
     ],
     "aside": None},
    {"id": "epoker-spanga", "h2": "Hus från olika tider på samma gata",
     "paras": [
       "Vägledningen beskriver villastäderna som områden med en mångfald av hustyper från olika epoker, där utbyggnadsfaserna och den successiva kompletteringen speglas i bebyggelsen. Den råder att karaktärsskapande material, kulörer, byggnadsdelar och detaljer tas tillvara eller återskapas i så stor utsträckning som möjligt vid ombyggnader och renoveringar.",
       "För fönsterbytet betyder det att vi utgår från husets egen tid. En villa från 1910-talet och en från 1970-talet på samma gata behöver olika fönster, och båda kan bli rätt. Vi tittar på fönstrens proportioner, bågarnas antal och hur de öppnas, och på hur fodren är profilerade, innan vi föreslår något nytt. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Spånga",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter fönstren och ser på väggarna."),
    ("Kartan", "Vi kontrollerar Stadsmuseets klassning för huset."),
    ("Konstruktion", "Förstärkning ritas när en ny öppning tas upp."),
    ("Förslag", "Fönster efter husets tid och indelning."),
    ("Montage", "Byte eller ny öppning, drevning och tätning."),
    ("Avslut", "Foder, bleck och genomgång med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Spånga",
  "rot": [_ROT_HUS, _ROT_SUM],
  "price_h2": "Vad påverkar priset för fönsterbytet i Spånga?",
  "price": [
    "Antal och storlek på fönstren, om en ny öppning tas upp och behöver förstärkas, verandans fönster, indelning och glas, foder och bleck. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag bygglov för att ta upp ett nytt fönster i min villa i Spånga?",
     "Normalt inte, enligt Boverket, och inte heller anmälan så länge bärande delar inte påverkas väsentligt. I särskilt värdefulla områden kan lov krävas."),
    ("Är Solhem i Spånga kulturhistoriskt värdefullt?",
     "Ja, i stadens vägledning Varsam utveckling är Solhem markerat som kulturhistoriskt värdefull miljö."),
    ("Kan ett nytt fönster störa grannen i Spånga?",
     "Staden påpekar att nya fönster kan ge ökad insyn, och råder att informera grannen om planerna."),
    ("Kan fönstren i en glasveranda bytas utan att verandan ändrar karaktär?",
     "Ja, om de nya fönstren får samma indelning och proportioner som de gamla."),
  ],
  "sources": [_VARSAM, _ALV_INV, _of("Solhem", "vasterort/jarva/solhem"), _of("Bromsten", "vasterort/jarva/bromsten"),
              _BV_TAK, _STH_FD, _SKV],
  "cta": ("Ska fönster bytas eller sättas in i Spånga?", "Boka ett gratis platsbesök, så ser vi på fönstren, verandan och väggarna och kontrollerar kartan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre trävilla med glasveranda och spröjsade fönster",
     "early 1900s Swedish wooden villa painted light green with a white glazed veranda with many small window panes, small dormer, mature garden with apple trees, summer" + _SFX),
    ("Ny fönsteröppning i en trävägg med förstärkt överliggare",
     "interior of a Swedish wooden villa under renovation where a new window opening has been cut in a wall, new timber header above the opening, sawdust on protective floor covering, no workers, daylight" + _SFX),
    ("Glasveranda med nya fönster med samma indelning",
     "close view of a glazed wooden veranda with newly installed white windows divided into small panes, matching the old style, garden reflected softly, summer light" + _SFX),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"fonsterbyte-vallingby.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Vällingby", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Vällingby – radhusen i riksintresset",
  "description": "Fönsterbyte i Vällingby: fönstren som värdebärande detalj i riksintresset, Atlantis och Omega, radhus med bostadsrätt och vem som får byta fönstren.",
  "h1": "Fönsterbyte i Vällingby",
  "lead": "I Vällingby–Råcksta räknas de ursprungliga husens fönster till det som gör riksintresset värdefullt. För radhus och kedjehus där är ett fönsterbyte därför både en fråga om bygglov och om föreningen. Geal Entreprenad AB byter fönster i Vällingby och tar fram underlaget till staden och styrelsen.",
  "card": "Radhus och kedjehus i riksintresset.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "riksintresse-vallingby", "anchor": "Riksintresset",
     "h2": "Fönstren i riksintresset",
     "paras": [
       "Översiktsplanens riksintressedel beskriver Vällingby–Råcksta som landets första ABC-stad, utbyggd under 1950-talet med radhus och småhus längst ut från centrum. Bland de värdebärande karaktärsdragen räknas de ursprungliga husens gestaltning och byggnadsdetaljer, som fönster, entrépartier, balkonger och räcken.",
       "Stockholms stad kräver bygglov för åtgärder som annars kan vara lovbefriade när huset ligger inom ett riksintresse för kulturmiljövården. Ett fönsterbyte på ett radhus i Vällingby behöver därför prövas, även om det skulle ha varit lovfritt på en villa i ett annat område.",
     ],
     "aside": {"title": "Värdebärande i Vällingby–Råcksta", "items": [
       "Husens ursprungliga gestaltning", "Fönster och entrépartier", "Balkonger och räcken", "Anpassning till terrängen"]}},
    {"id": "atlantis-vallingby", "h2": "Atlantis, Omega och kedjehusen",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden nämner flera mycket väl gestaltade radhus- och villaområden i Vällingby, bland dem de kulturhistoriskt synnerligen värdefulla Atlantis i nordost och Omega i nordväst. Om Vällingbys kedjehus skriver vägledningen att de kombinerar moderna volymer med asymmetriska gavlar och en mer traditionell fasadutformning med regelbunden fönstersättning och material som tegel och puts.",
       "Riksintressedelen beskriver också det sociala programmet bakom stadsdelen, med tankar om en blandad befolkning och lättillgänglighet, och dokumentet konstaterar att folkmängden i Vällingby–Råcksta efter 1960-talet har minskat kraftigt till knappt 15 000 invånare. Staden vill att stadsdelen ska utvecklas med fler invånare, men nya tillägg ska ha samma höga kvalitet på utformningen som ursprungsbebyggelsen. Den regelbundna fönstersättningen är det som syns när man går längs en gata med likadana hus. Vi föreslår därför fönster som behåller samma indelning, kulör och läge i fasaden, och tar gärna fram ett gemensamt förslag för hela längan, så att husen fortsätter att se ut som en helhet.",
     ],
     "aside": None},
    {"id": "foreningen-vallingby", "h2": "Vem får byta fönstren i radhuset?",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 449 småhus i Vällingby, varav 228 med bostadsrätt och 220 med äganderätt. I Råcksta är 91 småhus bostadsrätter och 299 äganderätter. Bor du i ett radhus med bostadsrätt avgör föreningens stadgar enligt bostadsrättslagen om fönstren är ditt eller föreningens ansvar.",
       "Skatteverket ger inget rotavdrag för att byta fönster i en bostadsrätt, men för arbete på insidan av befintliga fönster, som att byta glaset i den inre bågen, montera tätningslist eller byta innerfönster och fönsterfoder, när det är sådant du ansvarar för enligt stadgarna. Vi hjälper styrelsen med ett förslag som gäller alla hus i föreningen. Vill du hellre renovera fönstren finns mer under " + _L.format("fonsterrenovering-vallingby.html", "fönsterrenovering i Vällingby") + ".",
     ],
     "aside": {"title": "Småhus i Vällingby enligt områdesfakta", "items": [
       "449 småhus", "228 bostadsrätter", "220 äganderätter", "Råcksta: 299 äganderätter"]}},
    {"id": "underlag-vallingby", "h2": "Underlag till bygglovet",
     "paras": [
       "En ansökan om att byta fönster behöver visa hur de nya fönstren ser ut. Staden beskriver fasadritningen i skala 1:100 och detaljritningen, som visar byggnadsdetaljer som fönster i skala 1:10, 1:20 eller 1:50. Vid enkla ändringar kan ett fotomontage räcka i stället för en fasadritning.",
       "Vi mäter upp de befintliga fönstren, fotograferar fasaden och ritar de nya fönstren med profiler och indelning. Äldre handlingar som stadsbyggnadskontoret har för fastigheten, till exempel ritningar från byggåret, kan enligt staden letas fram och skrivas ut via e-tjänsten Bygg- och plantjänsten, och dem använder vi som utgångspunkt. Underlaget kan användas både i föreningens beslut och i ansökan. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Vällingby",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter och fotograferar fönstren."),
    ("Föreningen", "Vi går igenom stadgarna och ansvaret med styrelsen."),
    ("Ritningar", "Fasad- och detaljritning till bygglovet."),
    ("Bygglov", "Ansökan med vårt underlag."),
    ("Montage", "Fönstren byts hus för hus i längan."),
    ("Genomgång", "Skötselråd till föreningen och de boende."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Vällingby",
  "rot": [
    "För ett radhus eller kedjehus med äganderätt räknar Skatteverket det som rotarbete att reparera eller byta ut fönster och att montera isolerglas. " + _ROT_SUM,
    "I en bostadsrätt ger själva fönsterbytet inget rotavdrag, men arbete på insidan av fönstren kan ge avdrag om det är ditt ansvar enligt stadgarna.",
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet i Vällingby?",
  "price": [
    "Antal hus och fönster, om fönstren tillverkas efter mått, indelning och glas, foder och bleck, ritningar till bygglovet och om hela längan byts samtidigt. Efter ett gratis platsbesök får du eller föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för att byta fönster på ett radhus i Vällingby?",
     "Ja, i riksintresset Vällingby–Råcksta kräver staden bygglov även för åtgärder som annars är lovbefriade, och fönstren räknas som värdebärande."),
    ("Vem ansvarar för fönstren i ett radhus med bostadsrätt i Vällingby?",
     "Det avgör föreningens stadgar enligt bostadsrättslagen. Läs stadgarna eller fråga styrelsen."),
    ("Får jag rotavdrag för fönsterbyte i min bostadsrätt i Vällingby?",
     "Nej, inte för själva bytet. Skatteverket ger avdrag för arbete på insidan av fönstren om det är ditt ansvar enligt stadgarna."),
    ("Vilka radhusområden i Vällingby är synnerligen värdefulla?",
     "Stadens vägledning nämner Atlantis i nordost och Omega i nordväst som kulturhistoriskt synnerligen värdefulla."),
  ],
  "sources": [_RIKS, _VARSAM, _STH_KL, _of("Vällingby", "vasterort/hasselby-vallingby/vallingby"),
              _of("Råcksta", "vasterort/hasselby-vallingby/racksta"), _BRL, _SKV],
  "cta": ("Ska fönstren i radhusen bytas i Vällingby?", "Boka ett gratis platsbesök, så mäter vi upp fönstren och tar fram underlaget till staden och föreningen innan ni får ett skriftligt kostnadsförslag."),
  "img": [
    ("Kedjehus i tegel och puts med regelbundna fönster",
     "1950s Swedish link houses with red brick and light rendered facades, asymmetric gables, regular rows of white windows, small front gardens and footpaths, pine trees, summer" + _SFX),
    ("Nytt fönster i en tegelfasad på ett radhus",
     "close view of a newly installed white wooden window in a red brick facade of a 1950s terraced house, neat metal sill and white trim, daylight" + _SFX),
    ("Radhuslänga från 1950-talet i en grön förort",
     "long low row of 1950s Swedish terraced houses in yellow-brown brick with flat simple facades, low-pitched roofs, identical plain white windows without bay windows, small lawns and pine and birch trees, Scandinavian modernist suburb, soft afternoon light" + _SFX),
  ],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"fonsterbyte-alvsjo.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Älvsjö", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Älvsjö – villastaden och tilläggsisoleringen",
  "description": "Fönsterbyte i Älvsjö: villastadens hus från 1910- och 1920-talen, fönstrets läge när fasaden tilläggsisoleras, när lov krävs och rotavdrag.",
  "h1": "Fönsterbyte i Älvsjö",
  "lead": "I Älvsjö villastad står många hus från 1910- och 1920-talen kvar, men de flesta har byggts om i flera omgångar. När fönster byts i samband med att fasaden tilläggsisoleras är det lätt att fönstret hamnar djupare i väggen än förut. Geal Entreprenad AB byter fönster i Älvsjö och planerar fönstrets läge innan fasaden byggs ut.",
  "card": "Fönster och tilläggsisolering.",
  "sections": [
    {"id": "villastaden-alvsjo", "anchor": "Villastaden",
     "h2": "Villastaden som Hem på landet byggde",
     "paras": [
       "Stadsmuseets inventering av Älvsjö villastad berättar att fastighetsbolaget AB Hem på landet köpte två markområden från Älvsjö säteri 1908 och 1911, och att tomtförsäljningen började i december 1908. Omkring 1915 var uppåt hundra tomter bebyggda, ungefär hälften av alla i området. Villastaden fick tidigt vatten, avlopp och ordnade vägar, och en stadsplan fastställdes redan 1921.",
       "Villorna var enligt inventeringen i allmänhet på två, tre eller fyra rum och kök, och ibland rymde husen flera lägenheter där den minsta var avsedd för uthyrning. Stadens vägledning Varsam utveckling av småhus- och villaområden markerar del av Älvsjö som kulturhistoriskt värdefull miljö med generösa byggrätter.",
     ],
     "aside": {"title": "Älvsjö villastad", "items": [
       "Tomtförsäljning från 1908", "Ett hundratal tomter bebyggda 1915", "Stadsplan 1921", "Villor på 2–4 rum och kök"]}},
    {"id": "forandringar-alvsjo", "h2": "Hus som har byggts om",
     "paras": [
       "Inventeringen beskriver att en påfallande stor del av den äldsta bebyggelsen har bevarats, men att många fastigheter från 1910- och 1920-talen har byggts om eller till, ibland i flera omgångar, ofta så att den ursprungliga karaktären gått mer eller mindre förlorad. Nya fasad- och takmaterial, nya färgtyper och tilläggsisoleringar hade enligt inventeringen bidragit till utvecklingen, och endast ett tiotal av de äldre husen hade behållit sitt ursprungliga utseende så gott som helt.",
       "Inventeringen är gjord efter 1977, och mycket har hänt sedan dess. Men frågan är densamma i dag: ett fönsterbyte är ett tillfälle att antingen ta huset närmare sitt ursprung eller att förändra det ytterligare. Vi visar båda vägarna på platsbesöket.",
     ],
     "aside": None},
    {"id": "lage-alvsjo", "h2": "Fönstrets läge när fasaden blir tjockare",
     "paras": [
       "Stockholms stad räknar tilläggsisolering som en fasadändring. På stadens lista över ändringar av fönster finns dessutom exemplet att ett fönster flyttas från placering i fasadliv till att bli indraget från fasadlivet. Byggs väggen ut utan att fönstret flyttas ut med den hamnar fönstret längre in, och då ändras husets uttryck, med djupare smygar och större skuggor.",
       "Vi planerar därför fönsterbytet och tilläggsisoleringen samtidigt. Antingen flyttas fönstret ut så att det behåller sitt läge i förhållande till fasaden, eller så väljer vi en lösning där karm, foder och bleck gör övergången så lik den gamla som möjligt. Hur fasaden i övrigt kan renoveras beskriver vi under " + _L.format("fasadrenovering-alvsjo.html", "fasadrenovering i Älvsjö") + ".",
     ],
     "aside": {"title": "Vid tilläggsisolering", "items": [
       "Fönstret flyttas ut med fasaden", "Samma läge i fasadlivet", "Nya foder och bleck", "Smygarna anpassas"]}},
    {"id": "lov-alvsjo", "h2": "Bygglov eller inte?",
     "paras": [
       "För en- och tvåbostadshus krävs inte längre bygglov för fasadändringar om vissa förutsättningar är uppfyllda, skriver staden. Men om huset ligger i ett område som är utpekat som särskilt kulturhistoriskt värdefullt i översiktsplanen, visat med grön ring på Stadsmuseets karta, eller om huset är blå- eller grönmarkerat, krävs bygglov även för sådant som annars är lovfritt.",
       "Vi tittar på kartan för ditt hus innan vi ritar något. Behövs lov tar vi fram fasadritning och beskrivning av fönster och fasad. Vill du hellre renovera de gamla fönstren finns mer under " + _L.format("fonsterrenovering-alvsjo.html", "fönsterrenovering i Älvsjö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Älvsjö",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter fönstren och väggens tjocklek."),
    ("Kartan", "Vi kontrollerar Stadsmuseets klassning för huset."),
    ("Planering", "Fönstrets läge bestäms tillsammans med fasaden."),
    ("Lov", "Ritningar och beskrivning när lov krävs."),
    ("Montage", "Fönstren sätts i rätt läge och tätas."),
    ("Avslut", "Foder, bleck och genomgång med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Älvsjö",
  "rot": [_ROT_HUS,
          "Skatteverket ger också rotavdrag för tilläggsisolering i samband med ombyggnad, om huset är äldre än fem år och större delen av stommen behålls. " + _ROT_SUM],
  "price_h2": "Vad påverkar priset för fönsterbytet i Älvsjö?",
  "price": [
    "Antal och storlek på fönstren, om de flyttas ut i samband med tilläggsisolering, indelning och spröjs, foder och bleck och om bygglovsunderlag behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad händer med fönstren när fasaden tilläggsisoleras i Älvsjö?",
     "Utan åtgärd hamnar de djupare i väggen. Staden räknar en flytt från fasadliv till indraget som en ändring av fönstret, så läget bör planeras."),
    ("Behöver jag bygglov för nya fönster på min villa i Älvsjö?",
     "Inte om fasadändringen är lovfri för huset, men i särskilt värdefulla områden och för blå- eller grönmarkerade hus krävs lov."),
    ("När byggdes Älvsjö villastad?",
     "Enligt Stadsmuseets inventering började tomterna säljas 1908, och omkring 1915 var ett hundratal tomter bebyggda."),
    ("Ger tilläggsisolering rotavdrag i Älvsjö?",
     "Ja, Skatteverket räknar tilläggsisolering som rotarbete när huset är äldre än fem år och större delen av stommen behålls."),
  ],
  "sources": [_ALV_INV, _VARSAM, _STH_FAS, _STH_FD, _STH_KL, _SKV],
  "cta": ("Ska fönster bytas eller fasaden isoleras i Älvsjö?", "Boka ett gratis platsbesök, så planerar vi fönstrens läge innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa från 1910-talet med putsad bottenvåning och panel i gaveln",
     "1910s Swedish villa with white smooth-rendered ground floor, dark brown wooden panel in the gable, small-paned windows with shutters, steep red tile roof, garden with fruit trees, summer" + _SFX),
    ("Nytt träfönster med foder i en ljus fasad",
     "close view of a white wooden window in a thickened insulated house wall with a deep reveal, new wooden trim and metal sill, renovation in progress, no workers, daylight" + _SFX),
    ("Gata i en villastad med äldre hus och trädgårdar",
     "quiet street in an early 1900s Stockholm villa suburb with varied old wooden and rendered villas, hedges, fruit trees and picket fences, summer afternoon" + _SFX),
  ],
},
}
