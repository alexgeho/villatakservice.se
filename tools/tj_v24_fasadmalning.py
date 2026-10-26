# -*- coding: utf-8 -*-
"""Fasadmålning – ortsidor v24: Solna, Haninge, Skärholmen, Hässelby, Enskede, Södermalm (2026-10-26).
Deltjänst under malare.html (TJ_HUB["fasadmalning"]). Intent: måla om fasaden utvändigt – färgtyp, kulör, förarbete
och lov. Skild från ortens malare-<ort>.html och fasadrenovering-<ort>.html (materialbyte, puts och panel) och från
v15/v17/v20-sidorna (Bromma, Danderyd, Ekerö, Farsta, Hägersten, Huddinge, Järfälla, Lidingö, Nacka, Norrtälje,
Sigtuna, Sollentuna, Täby, Tyresö, Upplands Väsby, Vallentuna, Vällingby, Värmdö).

Lokal vinkel per sida:
Solna – en stad av flerbostadshus (ÖP: 99 procent av bostäderna), radhusen och stadsradhusen (Järvastaden, Nya
  Ulriksdal), kulturmiljöerna med småhus i ÖP-listan (Råsta egnahem, Bergshamra by, Solna kyrkby och radhus, kv
  Fyrväpplingen), föreningens ansvar och lovet mot allmän plats (Boverket), ROT bara för småhus.
Haninge – 1940–60-talens folkhemsvillor och kedjehus (tegel med spritputs eller trä i mustiga kulörer) och
  rekordårens grupphus (mustiga färger, 1980-talets pastell), råden i Haninges karaktärsmiljöer, lov och handlingar.
Skärholmen – miljonprogrammets småhus i Bredäng, Sätra, Vårberg och Skärholmen (Varsam: noga komponerad färgsättning,
  tegel, trä och skivor), Bredäng som kulturhistoriskt värdefull miljö, asbest i skivor och målning som exponerat arbete.
Hässelby – villastadens mångfald (trä, glasverandor, snickarglädje, färgsättning), grupphusen från 60- och 70-tal och
  tunnelbanestadens radhus i Hässelby gård och strand (värdefull miljö, tidstypisk färgsättning), färgtypens betydelse
  (slamfärg – byt aldrig färgtyp, RAÄ) och Boverket om färgtyp.
Enskede – Gamla Enskede (första trädgårdsstaden, riksintresse, nationalromantik, tjärad eller rödfärgad panel, puts i
  varma ljusa jordkulörer, kontrast mot snickerier), Enskededalen (ljusa dämpade toner) och Enskedefältet, slamfärg
  med trätjära (RAÄ).
Södermalm – flerbostadshus i bostadsrätt: lov för ny kulör mot gatan (PBL/Boverket), bara fasaden mot allmän plats
  prövas, Stadsmuseets karta, kalkfärg på puts (RAÄ), föreningens beslut och underhållsplan (bostadsrättslagen), inget
  rotavdrag på gemensamma ytor – egen trust-rad.

Fakta endast från källorna i respektive 'sources', öppnade med curl/urllib (Mozilla-UA) 2026-10-26, alla 200;
pdf:erna (Varsam, områdesfakta, Haninges karaktärsmiljöer, Solnas översiktsplan, RAÄ Byggnadsmåleri) har textlager.
Strukna / ej använda: avgifter, handläggningstider, Stadsmuseets svarstid, kulörer för enskilda kvarter (ingen källa),
alla priser, garantier, omdömen, egna uppdrag i orterna och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no text, no letters"

_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"
_STH_FAS = ("Stockholms stad – Fasadändring", _SB + "fasadandring/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_BV_FAS = ("Boverket – Fasadändring (PBL kunskapsbanken)",
           "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_RAA_MAL = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färger (pdf)", "https://www.raa.se/publicerat/9789172095830.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614)",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_AV_FOR = ("Arbetsmiljöverket – Förebygg riskerna med asbest",
           "https://www.av.se/halsa-och-sakerhet/kemiska-risker/risker-for-vissa-amnen-produkter-och-verksamheter/asbest/forebygg-riskerna-med-asbest/")
_BV_ASB = ("Boverket – Risker med hantering av asbest i byggnader",
           "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_SOL_OP = ("Solna stad – Översiktsplan 2030 (pdf)",
           "https://www.solna.se/download/18.d878336172a235b6c417193/1592394620116/Solna%20stads%20%C3%96versiktsplan%202030.pdf")
_SOL_KULT = ("Solna stad – Kulturmiljöer i Solna", "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna")
_SOL_BRF = ("Solna stad – För BRF och hyresvärd", "https://www.solna.se/bygga-bo--miljo/bygga/guide/for-brf-och-hyresvard")
_HAN_FAS = ("Haninge kommun – Fasadändring", "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/fasadandring/")
_HAN_KAR = ("Haninge kommun – Haninges karaktärsmiljöer (pdf)",
            "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
            "tillsammans med rutavdrag. Färg, material och resor ger inget avdrag.")
_TRUST_BRF = ["Gratis besök och kostnadsförslag", "Handlingar till bygglovet"]

PAGES_TJ = {

# ------------------------------------------------------------------ SOLNA
"fasadmalning-solna.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Solna", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Solna – radhusen, föreningen och lovet",
  "description": "Fasadmålning i Solna: radhus och villor i en stad av flerbostadshus, kulturmiljöerna i översiktsplanen, föreningens ansvar och när ny kulör kräver lov.",
  "h1": "Fasadmålning i Solna",
  "lead": "I Solna ligger nästan alla bostäder i flerbostadshus, så den som ska måla om en fasad är ofta en bostadsrättsförening eller en radhusägare med grannar tätt inpå. Geal Entreprenad AB målar fasader på radhus, villor och föreningshus i Solna och börjar med att reda ut vem som beslutar och om den nya kulören kräver lov.",
  "card": "Radhusen, föreningen och lovet.",
  "sections": [
    {"id": "staden-solna", "anchor": "Husen i Solna",
     "h2": "En stad av flerbostadshus",
     "paras": [
       "Enligt Solnas översiktsplan finns 99 procent av stadens bostäder i flerbostadshus, och staden konstaterar att den begränsade marken ger små möjligheter att bygga småhus. I stället har staden arbetat för marknära stadsradhus, som när planen skrevs byggdes i Järvastaden och Nya Ulriksdal.",
       "För fasadmålning betyder det två helt olika uppdrag. Det ena är radhuset eller villan, där ägaren själv bestämmer. Det andra är flerbostadshuset, där föreningen eller fastighetsägaren beslutar och där reglerna för lov är strängare.",
     ],
     "aside": {"title": "Solna enligt översiktsplanen", "items": [
       "99 procent av bostäderna i flerbostadshus", "Stadsradhus i Järvastaden och Nya Ulriksdal"]}},
    {"id": "kulturmiljoer-solna", "h2": "Småhusen i kulturmiljöerna",
     "paras": [
       "Översiktsplanen pekar ut sammanhängande kulturmiljöer där helheten bedöms som viktig. Bland dem finns flera med småhus: Råsta egnahem, Bergshamra by, villabebyggelsen i norra Råsunda, Råsunda villastad och Solna kyrkby med radhusbebyggelse. Radhusen i kvarteret Fyrväpplingen är byggnadsminne.",
       "Staden skriver att det i dessa miljöer ofta är helhetsintrycket som är det viktiga, och att det finns områden och byggnader som skyddas genom bestämmelser i detaljplan. Byter du kulör på ett hus i en sådan miljö kan bygglov krävas även för en villa. Solna stad har en karta över kulturhistoriskt klassade byggnader som ger en första bild.",
     ],
     "aside": {"title": "Kulturmiljöer med småhus", "items": [
       "Råsta egnahem", "Bergshamra by", "Norra Råsunda och Råsunda villastad", "Solna kyrkby med radhus", "Radhus i kv Fyrväpplingen"]}},
    {"id": "lovet-solna", "h2": "Ny kulör eller samma kulör",
     "paras": [
       "Boverket förklarar att byte av kulör betyder en ändring av färgens nyans, ton eller ljushet, till exempel från rött till vitt. Att måla om i samma kulör som förut kräver normalt inte bygglov eftersom det räknas som underhåll. På ett en- eller tvåbostadshus krävs inget bygglov för ny kulör, utom i särskilt värdefulla områden och byggnader.",
       "För andra byggnader, som flerbostadshus, krävs bygglov inom detaljplan om ändringen sker på en fasad som vetter mot en allmän plats, till exempel en gata eller park. Det räcker att en del av fasaden vetter mot allmän plats, och det är bara den fasaden som prövas.",
     ],
     "aside": None},
    {"id": "foreningen-solna", "h2": "När föreningen målar",
     "paras": [
       "Solna stad påminner bostadsrättsföreningar om att de är ansvariga även om en leverantör utför arbetet, och råder dem att göra en ordentlig förstudie av vilka krav som gäller. För en fasadmålning betyder det att föreningen behöver veta om kulören ändras, vilken fasad som vetter mot gatan och om huset är klassat.",
       "Vi tar fram ett underlag som styrelsen kan fatta beslut på: fasadernas skick, nuvarande färgtyp och kulör, förslag på kulör och vilka handlingar ett bygglov kräver. Om husen och kulörerna i Solna i övrigt kan du läsa under " + _L.format("malare-solna.html", "målare i Solna") + ".",
     ],
     "aside": None},
    {"id": "radhuset-solna", "h2": "Radhuset i längan",
     "paras": [
       "På ett radhus i en länga syns en ny kulör i hela gruppen. Även när inget lov krävs lönar det sig att stämma av med grannarna, och ligger radhuset i en samfällighet eller förening kan det finnas gemensamma beslut om färgsättningen.",
       "Vi skrapar fram äldre färglager på en liten yta för att se vilken färgtyp huset har, och väljer en färg som fungerar på det underlaget. Om puts och fasadmaterial i Solna kan du läsa under " + _L.format("fasadrenovering-solna.html", "fasadrenovering i Solna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Solna till",
  "steps": [
    ("Platsbesök", "Fasaderna, färgtypen och vilka sidor som vetter mot gatan går vi igenom."),
    ("Lov och klassning", "Kulturmiljöer, detaljplan och behov av bygglov kontrolleras."),
    ("Skriftligt kostnadsförslag", "Varje fasad och moment står för sig, som underlag för beslut."),
    ("Förarbete", "Tvätt, skrapning och lagning av skadat underlag."),
    ("Målning", "Grundning där det behövs och strykning i rätt färgtyp."),
    ("Genomgång", "Vi går igenom resultatet och skriver ner kulör och färgtyp."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Solna",
  "rot": [
    "Skatteverket räknar målning av fasader på ett småhus som rotarbete. I en bostadsrätt gäller avdraget bara arbete inne i bostaden som du ansvarar för enligt stadgarna, och arbete på gemensamma ytor som fasader ger inget rotavdrag.",
    _ROT_SUM + " För arbete som ger avdrag drar Geal det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fasadmålningen i Solna?",
  "price": [
    "Fasadens yta och höjd, underlagets skick, färgtyp, ställning och om bygglov behöver sökas. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vår förening bygglov för att måla huset i Solna i ny kulör?",
     "Ja, om fasaden vetter mot en allmän plats och huset ligger inom detaljplan. Målar ni i samma kulör som förut räknas det normalt som underhåll."),
    ("Vi bor i Råsta egnahem – behövs lov för ny kulör på villan?",
     "Det kan behövas. Råsta egnahem är en utpekad kulturmiljö i översiktsplanen, och i särskilt värdefulla områden krävs lov även för villor. Kontrollera detaljplanen och stadens karta."),
    ("Ger fasadmålningen av vårt bostadsrättshus rotavdrag?",
     "Nej, Skatteverket ger inget rotavdrag för arbete på gemensamma ytor som fasader i en bostadsrätt."),
    ("Vem ansvarar om målaren gör fel?",
     "Solna stad påpekar att föreningen som byggherre är ansvarig även om en leverantör utför arbetet. Därför är det viktigt att kraven är utredda innan arbetet startar."),
  ],
  "sources": [_SOL_OP, _SOL_KULT, _SOL_BRF, _BV_FAS, _SKV, _SKV2],
  "cta": ("Ska fasaden i Solna målas om?", "Boka ett gratis platsbesök, så går vi igenom fasaderna och reglerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Länga av äldre radhus med nymålade fasader och små förgårdar",
     "row of 1940s Swedish terraced houses with freshly painted light ochre wooden facades and white trim, small front gardens with hedges, quiet street near a park, northern Stockholm suburb, summer" + _IMG_END),
    ("Panel med en provyta där ett äldre ljust färglager syns under den röda färgen",
     "close view of an old painted wooden facade with a small scraped test area revealing several older paint layers in different colours, scraper and brush resting on a ledge, daylight" + _IMG_END),
    ("Putsat flerbostadshus med byggnadsställning mot gatan",
     "empty quiet street, no pedestrians, no cars: 1940s Swedish rendered apartment building with scaffolding and weather protection netting along the street facade during repainting, trees along the street, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HANINGE
"fasadmalning-haninge.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Haninge", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Haninge – mustiga 50-tal och pastell",
  "description": "Fasadmålning i Haninge: folkhemmets villor i mustiga kulörer, rekordårens grupphus och 1980-talets pastell, kommunens råd och när ny kulör kräver lov.",
  "h1": "Fasadmålning i Haninge",
  "lead": "Många småhus i Haninge byggdes mellan 1940- och 1980-talet, och kulören var en del av arkitekturen: mustiga färger på 1950-talet och ljusare pastell när 1980-talet kom. Geal Entreprenad AB målar om fasader på villor, kedjehus och radhus i Haninge och utgår från husets egen tid.",
  "card": "Mustiga 50-tal och pastell.",
  "sections": [
    {"id": "folkhemmet-haninge", "anchor": "Folkhemmets hus",
     "h2": "Folkhemmets villor och kedjehus",
     "paras": [
       "Haninges karaktärsmiljöer beskriver småhusområdena från 1940- till 1960-talet som samlade grupper av små, enhetliga villor, kedjehus eller radhus. 1940-talets hus är enkla en- eller tvåplansvillor i trä, puts eller fasadtegel, med enhetlig fönstersättning och färgsättning i ljusa eller mustiga kulörer.",
       "På 1950-talet blev områdena mer individuellt utformade. Rött eller gult tegel kombinerades med grov spritputs eller trä målat i mustiga kulörer, men det finns också enkla fasader i puts eller trä utan knutar och foder. Exempel på sådana områden finns enligt kommunen i Handen, Jordbro, Vendelsö, Vendelsömalm och Västerhaninge.",
     ],
     "aside": {"title": "Typiskt för 1940–60-tal", "items": [
       "Tegel med spritputs eller trä", "Mustiga kulörer", "Enhetlig fönstersättning", "Små trädgårdstomter"]}},
    {"id": "rekordaren-haninge", "h2": "Rekordårens grupphus",
     "paras": [
       "Villorna från 1960-talet och framåt är oftast byggda i grupp, med enhetlighet inom området och små variationer mot gatan. Enligt kommunen varierar färgsättningen och fasadmaterialen kraftigt, men mustiga färger är vanliga, ofta tegel eller kalksandsten, så kallat mexitegel, i kombination med panel.",
       "Mot 1980-talet blev variationen större inom områdena och husen fick åter dekorativa snickerier. Färgsättningen blev ljusare när pastellfärgerna slog igenom. Exempel på rekordårens småhus finns i Jordbro, Brandbergen, Västerhaninge och Handen.",
     ],
     "aside": None},
    {"id": "raden-haninge", "h2": "Vad kommunen råder",
     "paras": [
       "För 1960–80-talens områden skriver kommunen att husens typiska fasadutformning när det gäller materialval och färgsättning ska värnas, och att mindre åtgärder som fasadändringar kan påverka ett helt kvarter. För 1940–60-talens hus beskriver kommunen dörrar och fönster som en bärande del av husets karaktär, där ursprunglig utformning och färgsättning ska värnas och vara utgångspunkt vid förändring.",
       "Råden kan enligt kommunen tillämpas på alla småhusområden från perioden, även de som inte är utpekade som särskilt värdefulla. All bebyggelse omfattas dessutom av varsamhetskravet i plan- och bygglagen. En ny kulör i en husgrupp bör därför stämmas av mot grannhusen och mot vad gruppen hade från början.",
     ],
     "aside": {"title": "Råd i karaktärsmiljöerna", "items": [
       "Värna materialval och färgsättning", "Fönster och dörrar i ursprunglig färgsättning", "Tänk på hela kvarteret"]}},
    {"id": "lovet-haninge", "h2": "När behövs lov för ny kulör?",
     "paras": [
       "Haninge kommun räknar byte av färg på fasaden som en fasadändring. Bygglov behövs om du ändrar fasaden på en byggnad eller i ett område som är särskilt värdefullt, och för andra byggnader än en- och tvåbostadshus inom detaljplan om fasaden vetter mot allmän plats. Målning i samma kulör räknas enligt Boverket normalt som underhåll.",
       "Krävs lov ska ansökan innehålla en situationsplan på tomtkarta med byggnaden markerad, fotografier av byggnaden och ett förslag till kontrollplan. Vi hjälper till med underlaget. Om fasadmaterialen i kommunen kan du läsa under " + _L.format("fasadrenovering-haninge.html", "fasadrenovering i Haninge") + ".",
     ],
     "aside": None},
    {"id": "underlaget-haninge", "h2": "Panel, puts och tegel",
     "paras": [
       "En fasad från 1950-talet har ofta flera material, och de målas olika. Trä skrapas och tvättas och grundas där färgen släppt, puts rengörs och lagas, och omålat tegel lämnar vi omålat. Kommunen påpekar för 1940–60-talens hus att en fasad i tegel inte ska putsas.",
       "Vi skrapar fram äldre färglager på en liten yta för att se vad huset hade från början. Det hjälper både vid valet av färgtyp och när kulören ska stämmas av mot gruppen. Om kulörer och målning i Haninge i övrigt kan du läsa under " + _L.format("malare-haninge.html", "målare i Haninge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Haninge till",
  "steps": [
    ("Platsbesök", "Fasadmaterial, färgtyp och grannhusens kulörer går vi igenom."),
    ("Skrapprov", "Äldre färglager tas fram för att se husets ursprungliga kulör."),
    ("Skriftligt kostnadsförslag", "Trä, puts och detaljer står var för sig."),
    ("Lov vid behov", "Underlag till bygglov tas fram om huset ligger i ett värdefullt område."),
    ("Målning", "Förarbete, grundning och strykning i rätt färgtyp."),
    ("Genomgång", "Vi går igenom resultatet och skriver ner kulörerna."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Haninge",
  "rot": [
    "Skatteverket räknar målning av fasader på ett småhus som rotarbete, liksom att montera och montera ner byggnadsställningen. Målning av staket och murar ger däremot inget avdrag.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fasadmålningen i Haninge?",
  "price": [
    "Fasadens yta, hur många material den har, underlagets skick, antalet snickerier och om bygglov behövs. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi måla vårt 80-talshus i Brandbergen i en mörkare kulör?",
     "På en villa krävs normalt inget lov, om huset inte ligger i ett särskilt värdefullt område. Kommunens råd är ändå att färgsättningen i rekordårens grupphus ska värnas, så stäm av mot husgruppen."),
    ("Vilka kulörer hade 1950-talets villor i Haninge?",
     "Enligt kommunens karaktärsmiljöer var mustiga kulörer på trä eller spritputs i kombination med rött eller gult tegel tongivande."),
    ("Ska teglet på vårt kedjehus målas samtidigt?",
     "Omålat tegel lämnar vi omålat. Kommunen råder för 1940–60-talens hus att en fasad i tegel inte ska putsas."),
    ("Vad behövs till en ansökan om ny fasadkulör i Haninge?",
     "Situationsplan på tomtkarta med byggnaden markerad, fotografier av byggnaden och ett förslag till kontrollplan."),
  ],
  "sources": [_HAN_KAR, _HAN_FAS, _BV_FAS, _SKV, _SKV2],
  "cta": ("Ska fasaden på huset i Haninge målas om?", "Boka ett gratis platsbesök, så går vi igenom fasaden och kulörerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa från 1950-talet med gult tegel och trädelar i mustig kulör",
     "1950s Swedish single family house combining yellow brick with wooden facade sections painted deep ochre and coarse light render, low hedge and small garden, suburban Haninge, summer" + _IMG_END),
    ("Grupphus från 1980-talet i ljusa pastellkulörer",
     "row of 1980s Swedish group-built houses painted in soft pastel colours with decorative white wooden trim, small front gardens with low hedges, suburban street, daylight" + _IMG_END),
    ("Nymålad panel bredvid omålat tegel på ett kedjehus",
     "close view of a 1960s Swedish linked house where freshly painted wooden panel meets unpainted red brick, crisp paint edge, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"fasadmalning-skarholmen.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Skärholmen", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Skärholmen – radhusen från 60- och 70-tal",
  "description": "Fasadmålning i Skärholmen: radhus och kedjehus i Bredäng, Sätra, Vårberg och Skärholmen, husgruppernas noga komponerade kulörer, asbest i skivor och lovet.",
  "h1": "Fasadmålning i Skärholmen",
  "lead": "Småhusen i Bredäng, Sätra, Vårberg och Skärholmen byggdes i grupp på 1960- och 70-talen, och kulörerna valdes för hela gruppen. Geal Entreprenad AB målar om fasader på radhus, kedjehus och villor i Skärholmen och utgår från husgruppens färgsättning.",
  "card": "Radhusen från 60- och 70-tal.",
  "sections": [
    {"id": "miljonprogrammet-skarholmen", "anchor": "Småhusen",
     "h2": "Småhus i den storskaliga stadsdelen",
     "paras": [
       "Stadens strategi för småhusområden beskriver Bredäng som den första stadsdelen som planerades i stor skala, med byggstart 1962, följd av Sätra. En stor andel av miljonprogrammets bebyggelse bestod av gruppbyggda småhus och radhus. Exempel på villor och atriumhus i de storskaliga stadsdelarna finns enligt strategin bland annat i Sätra.",
       "Enligt stadens områdesfakta för 2025 finns 1 976 småhus med äganderätt i Skärholmens stadsdelsområde: 577 i Vårberg, 543 i Skärholmen, 536 i Sätra och 320 i Bredäng.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Vårberg: 577", "Skärholmen: 543", "Sätra: 536", "Bredäng: 320"]}},
    {"id": "kulorerna-skarholmen", "h2": "Kulörer valda för hela gruppen",
     "paras": [
       "Strategin skriver att småhusen i de storskaliga stadsdelarna ofta hade en blandning av fasadmaterial, som tegel, trä och skivor, men att enhetligheten inom husgrupperna var mycket stor. Färgsättningen var noga komponerad och enhetlig, men kunde variera mellan olika kvarter eller områden.",
       "Bland det som har stor påverkan vid förändringar nämner strategin material, färgsättning, byggnadsdelar och detaljer, och den råder att karaktärsskapande kulörer tas tillvara eller återskapas vid renoveringar. En ny kulör på ett radhus mitt i en länga bryter därför gruppens uttryck, även när det inte krävs lov.",
     ],
     "aside": {"title": "Typiskt för husgrupperna", "items": [
       "Tegel, trä och skivor", "Enhetlig färgsättning inom gruppen", "Variation mellan kvarter"]}},
    {"id": "bredang-skarholmen", "h2": "Bredäng och lovet",
     "paras": [
       "I strategins tabell är Bredäng markerat som kulturhistoriskt värdefull miljö. Stockholms stad påpekar att utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla byggnader och områden, och att du då behöver bygglov även för åtgärder som annars är lovfria. Stadsmuseets klassificeringskarta ger en första indikation på om din fastighet berörs.",
       "Boverket förklarar att en ny kulör, till exempel från rött till vitt, är en fasadändring, medan ommålning i samma kulör normalt är underhåll. På en villa utanför värdefulla miljöer krävs inget lov för ny kulör, men en fasadändring som inte kräver lov ska ändå stämma med detaljplanen.",
     ],
     "aside": None},
    {"id": "skivorna-skarholmen", "h2": "Skivor från 1960- och 70-talen",
     "paras": [
       "Boverket skriver att byggnader från perioden 1940–1980 sannolikt innehåller asbest någonstans, och nämner fasadskivor bland de produkter där den kan finnas. Arbetsmiljöverket räknar målning till de arbeten där man kan utsättas för asbesthaltigt damm, och skriver att det ska vara klarlagt om det finns asbest innan arbetet börjar.",
       "Har radhuset skivor från byggtiden tar vi därför reda på vad de består av innan förarbetet planeras. Analys av ett prov är det enda säkra sättet att veta. Visar provet asbest planeras förarbetet efter det, och delar som ska rivas eller saneras hanteras av ett företag med tillstånd från Arbetsmiljöverket.",
     ],
     "aside": {"title": "Före förarbetet", "items": [
       "Byggår och tidigare renoveringar", "Prov på misstänkta skivor", "Skriftligt besked om resultatet"]}},
    {"id": "tillaggen-skarholmen", "h2": "Uterum och tillbyggnader",
     "paras": [
       "Strategin konstaterar att småhusen i de storskaliga stadsdelarna står på små tomter, vilket begränsar större förändringar, men att påbyggnader förekommer och att mindre tillbyggnader är vanliga, till exempel inglasade uterum. Under 2000-talet har stadsdelarna också kompletterats med nya radhus inom den ursprungliga planstrukturen.",
       "När en fasad ska målas om finns det därför ofta både ursprungliga delar och senare tillägg i samma husgrupp. Vi målar tilläggen så att de ansluter till huvudbyggnaden i kulör och färgtyp, och vi ser över anslutningar mellan uterum och fasad där vatten kan tränga in.",
     ],
     "aside": None},
    {"id": "underlaget-skarholmen", "h2": "Trä, skivor och detaljer",
     "paras": [
       "På ett radhus från den här tiden målas ofta flera material: träpanel och vindskivor, skivor, dörrar och fönsterfoder. Vi skrapar fram äldre färglager på en liten yta för att se färgtyp och ursprunglig kulör och väljer färg som passar varje underlag. Byts en kulör i hela gruppen samtidigt kan ställning och leveranser samordnas mellan husen.",
       "Om tjänsten i stort kan du läsa under " + _L.format("malare.html", "målare") + ", och om stadsdelens tak under " + _L.format("taklaggare-skarholmen.html", "takläggare i Skärholmen") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Skärholmen till",
  "steps": [
    ("Platsbesök", "Fasadmaterial, färgtyp och husgruppens kulörer går vi igenom."),
    ("Provtagning vid behov", "Misstänkta skivor analyseras innan förarbetet planeras."),
    ("Skriftligt kostnadsförslag", "Varje material och moment står för sig."),
    ("Kulör", "Kulören stäms av mot gruppen och mot kartan om huset ligger i Bredäng."),
    ("Målning", "Förarbete, grundning och strykning i rätt färgtyp."),
    ("Genomgång", "Vi går igenom resultatet och skriver ner kulörerna."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Skärholmen",
  "rot": [
    "Skatteverket räknar målning av fasader på ett småhus som rotarbete. Sanering av asbest i samband med byggarbete ger också avdrag, men att mäta asbest gör det inte.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fasadmålningen i Skärholmen?",
  "price": [
    "Fasadens yta, antalet material, underlagets skick, detaljer som vindskivor och foder och om prov behöver tas. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi måla vårt radhus i Sätra i en annan kulör än grannarna?",
     "Utanför värdefulla miljöer krävs normalt inget lov för en villa eller ett radhus, men stadens strategi råder att husgruppernas kulörer tas tillvara."),
    ("Är Bredäng kulturhistoriskt värdefullt?",
     "Ja, Bredäng är markerat som kulturhistoriskt värdefull miljö i stadens strategi för småhusområden. Kontrollera din fastighet i Stadsmuseets karta."),
    ("Kan fasadskivorna på vårt 70-talsradhus innehålla asbest?",
     "Det kan de. Boverket räknar byggnader från 1940–1980 som sannolika att innehålla asbest, och fasadskivor är ett av exemplen. Ett prov ger svaret."),
    ("Ska uterummet målas i samma kulör som huset?",
     "Det är ofta det bästa för helheten. Stadens strategi råder att material och kulörer i husgrupperna tas tillvara, och ett uterum som ansluter i kulör smälter in i gruppen."),
    ("Hur många småhus finns i Skärholmens stadsdelsområde?",
     "Enligt stadens områdesfakta för 2025 finns 1 976 småhus med äganderätt."),
  ],
  "sources": [_VARSAM, ("Stockholms stad – Områdesfakta 2025: Skärholmens stadsdelsområde (pdf)", _OF + "soderort/skarholmen/skarholmen-stadsdelsomrade.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Vårberg (pdf)", _OF + "soderort/skarholmen/varberg.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Sätra (pdf)", _OF + "soderort/skarholmen/satra.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Bredäng (pdf)", _OF + "soderort/skarholmen/bredang.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Skärholmen (pdf)", _OF + "soderort/skarholmen/skarholmen.pdf"),
              _STH_FAS, _STH_KL, _BV_FAS, _BV_ASB, _AV_FOR, _SKV, _SKV2],
  "cta": ("Ska radhuset i Skärholmen målas om?", "Boka ett gratis platsbesök, så går vi igenom fasaden och husgruppen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus från 1960-talet med tegel och målad träpanel i samma kulör",
     "row of late 1960s Swedish terraced houses combining red brick ground floor and upper floor wooden panel painted in a uniform muted green, flat roofs, small front yards, footpath, south-west Stockholm suburb, summer" + _IMG_END),
    ("Husgrupp med kedjehus i enhetlig färgsättning",
     "group of 1970s Swedish linked houses with identical facades in a coordinated colour scheme of brown panel and white trim, small gardens and trees, daylight" + _IMG_END),
    ("Fönsterbleck och träpanel med en pensel inför målning",
     "close view of freshly painted bargeboard and window trim on a 1970s wooden terraced house, masking tape and brush on a ledge, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HÄSSELBY
"fasadmalning-hasselby.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Hässelby", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Hässelby – villastaden och radhusen",
  "description": "Fasadmålning i Hässelby: villastadens trähus med snickarglädje, grupphusen och radhusen i Hässelby gård och strand, färgtypen och när ny kulör kräver lov.",
  "h1": "Fasadmålning i Hässelby",
  "lead": "I Hässelby villastad har nästan varje hus en egen färgsättning, medan radhusen i Hässelby gård och Hässelby strand målades lika i hela gruppen. Geal Entreprenad AB målar om fasader på villor, radhus och kedjehus i Hässelby och börjar med vilket slags område huset står i.",
  "card": "Villastaden och radhusen.",
  "sections": [
    {"id": "villastaden-hasselby", "anchor": "Villastaden",
     "h2": "Villastaden: ett hus i taget",
     "paras": [
       "Stadens strategi för småhusområden räknar Hässelby villastad till villastäderna, som var privat organiserade och därför fick en brokigare bebyggelse än stadens egna egnahemsområden. Trä var det dominerande fasadmaterialet, även om puts förekom, och glasverandor, takkupor, snickarglädje och färgsättning gav variation som syns än i dag.",
       "Enligt stadens områdesfakta för 2025 finns 4 757 småhus med äganderätt i Hässelby villastad. I villastaden väljer vi kulör och färgtyp efter husets egen ålder och stil och tar hänsyn till detaljer som glasverandor och snickarglädje.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Hässelby villastad: 4 757", "Hässelby gård: 324", "Hässelby-Vällingby: 9 216"]}},
    {"id": "grupperna-hasselby", "h2": "Grupphusen från 1960- och 70-talen",
     "paras": [
       "På 1960- och 1970-talen ersattes många villor i Hässelby villastad av täta, sammanhållna grupper av enhetliga småhus, skriver strategin. Bland villastädernas karaktärsdrag nämns grupphusområdenas sammanhållna karaktär, med exempelvis enhetlig skala, färgsättning och byggnadsmaterial.",
       "Här gäller motsatt princip mot den äldre villastaden: kulören väljs för gruppen, inte för det enskilda huset. Har grannarna redan målat om tar vi fram deras kulör, och är gruppen spretig utgår vi från det som syns mest i gruppen och från skrapprov på det egna huset. Strategin råder att förändringar i sammanhållna grupper av villor, radhus och kedjehus utformas utifrån ett helhetsperspektiv.",
     ],
     "aside": None},
    {"id": "tunnelbanestaden-hasselby", "h2": "Hässelby gård och Hässelby strand",
     "paras": [
       "Hässelby gård och Hässelby strand hör till tunnelbanestadens gruppbyggda småhusområden, och båda är markerade som kulturhistoriskt värdefull miljö i strategins tabell. Bland områdenas karaktärsdrag nämner strategin enhetligt utformade husgrupper och tidstypisk färgsättning.",
       "Stockholms stad påpekar att utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla byggnader och områden, och Stadsmuseets klassificeringskarta ger en första indikation på om din fastighet berörs. En ny kulör, till exempel från rött till vitt, är enligt Boverket en fasadändring, medan ommålning i samma kulör normalt räknas som underhåll.",
     ],
     "aside": {"title": "Kontrollera före ny kulör", "items": [
       "Stadsmuseets karta", "Detaljplanen", "Husgruppens kulörer"]}},
    {"id": "fargtypen-hasselby", "h2": "Färgtypen avgör",
     "paras": [
       "Boverket skriver att en ändring av färgtyp, till exempel från slamfärg till silikonhartsfärg eller från linoljefärg till plastfärg, inte räknas som byte av kulör men kan bedömas som påverkan på byggnadens yttre karaktärsdrag. Färgtypen spelar också roll tekniskt.",
       "Riksantikvarieämbetet varnar för att måla om en slamfärgsmålad yta med något annat än slamfärg: har man en gång bytt till latex-, alkyd- eller linoljefärg kan man inte gå tillbaka till slamfärg, ens om den befintliga färgen tas bort. Därför skrapar vi fram ett prov innan färgen väljs. Om villastadens fasader i övrigt kan du läsa under " + _L.format("fasadrenovering-hasselby.html", "fasadrenovering i Hässelby") + ".",
     ],
     "aside": None},
    {"id": "forarbetet-hasselby", "h2": "Förarbetet",
     "paras": [
       "En slamfärgad fasad borstas med stål- eller rotborste så att lös färg och lavar försvinner, dammas av och målas oftast i en strykning. Uppstickande spikskallar slås i och skadad panel lagas med friskt trä. En linoljefärgad fasad sodatvättas och sköljs noga, skrapas där färgen sitter löst, får spikarna islagna och grundas där det behövs. Linoljefärg ska enligt Riksantikvarieämbetet strykas mycket tunt.",
       "Snickerier, vindskivor och foder tar vi i samma arbete. Om målning i stadsdelen i stort kan du läsa under " + _L.format("malare-hasselby.html", "målare i Hässelby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Hässelby till",
  "steps": [
    ("Platsbesök", "Huset, området och grannhusens kulörer går vi igenom."),
    ("Skrapprov", "Färgtyp och äldre kulörer tas fram på en liten yta."),
    ("Skriftligt kostnadsförslag", "Fasad, snickerier och ställning står var för sig."),
    ("Kulör och lov", "Kulören stäms av mot gruppen och kartan kontrolleras."),
    ("Målning", "Förarbete och strykning i samma färgtyp som underlaget."),
    ("Genomgång", "Vi går igenom resultatet och skriver ner färgtyp och kulör."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Hässelby",
  "rot": [
    "Skatteverket räknar målning av fasader på ett småhus som rotarbete, liksom att montera och montera ner byggnadsställningen. Du ska äga huset när arbetet utförs.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fasadmålningen i Hässelby?",
  "price": [
    "Fasadens yta och höjd, färgtyp, underlagets skick, mängden snickerier och glasverandor och om ställning behövs. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi gå från plastfärg tillbaka till rödfärg på villan i Hässelby?",
     "Enligt Riksantikvarieämbetet går det inte att måla om med slamfärg när ytan en gång målats med latex-, alkyd- eller linoljefärg, ens om färgen tas bort."),
    ("Behöver vi lov för ny kulör på radhuset i Hässelby strand?",
     "Hässelby strand är markerat som kulturhistoriskt värdefull miljö i stadens strategi, och där kan lov krävas. Kontrollera Stadsmuseets karta och detaljplanen."),
    ("Måste vi välja samma kulör som grannarna i grupphusområdet?",
     "Det är inget krav i lagen för en villa utanför värdefulla miljöer, men stadens strategi råder att grupper av småhus förändras utifrån helheten."),
    ("Hur målas en rödfärgad fasad om?",
     "Den borstas med stål- eller rotborste så att lös färg och lavar försvinner, dammas av och målas oftast i en strykning, enligt Riksantikvarieämbetet."),
    ("Räknas byte från linoljefärg till plastfärg som ny kulör?",
     "Nej, enligt Boverket är byte av färgtyp inte byte av kulör, men det kan bedömas påverka byggnadens yttre karaktärsdrag."),
  ],
  "sources": [_VARSAM, ("Stockholms stad – Områdesfakta 2025: Hässelby villastad (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-villastad.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hässelby gård (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-gard.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hässelby-Vällingby stadsdelsområde (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-vallingby-stadsdelsomrade.pdf"),
              _STH_FAS, _STH_KL, _BV_FAS, _RAA_MAL, _SKV, _SKV2],
  "cta": ("Ska fasaden på huset i Hässelby målas om?", "Boka ett gratis platsbesök, så går vi igenom fasaden och färgtypen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Trävilla med glasveranda och snickarglädje i kontrasterande kulör",
     "empty garden, nobody present: early 1900s Swedish wooden villa with a glazed veranda and decorative fretwork painted in a contrasting colour, light yellow panel facade, large garden with apple trees, western Stockholm, summer" + _IMG_END),
    ("Radhus i grupp med tidstypisk enhetlig färgsättning",
     "row of 1950s Swedish two storey terraced houses in Hässelby gård style, flat facades of light render and yellow brick, low-pitched roofs without chimneys, no bay windows, Scandinavian modernist, small gardens along a curved path, western Stockholm suburb, daylight" + _IMG_END),
    ("Rödfärgad panel som borstas inför ommålning",
     "close view of weathered falu red painted wooden facade boards with a stiff wire brush resting on a ledge, loose paint flakes, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ENSKEDE
"fasadmalning-enskede.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Enskede", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Enskede – trädgårdsstadens kulörer",
  "description": "Fasadmålning i Enskede: rödfärgade trähus och puts i jordkulörer i Gamla Enskede, Enskededalens dämpade toner, slamfärg med tjära och lovet.",
  "h1": "Fasadmålning i Enskede",
  "lead": "Gamla Enskede var Stockholms första trädgårdsstad, och fasadernas kulörer är en del av det som gör området till riksintresse. Geal Entreprenad AB målar om fasader på villor och radhus i Gamla Enskede, Enskededalen och Enskedefältet och utgår från vad huset hade från början.",
  "card": "Trädgårdsstadens kulörer.",
  "sections": [
    {"id": "tradgardsstaden-enskede", "anchor": "Trädgårdsstaden",
     "h2": "Stockholms första trädgårdsstad",
     "paras": [
       "Gamla Enskede anlades efter stadsplanedirektör Per Olof Hallmans stadsplan från 1908, skriver staden i sin strategi för småhusområden. Typritningar togs fram för ett enhetligt uttryck, och den mest kända är Enskedestugan. I Gamla Enskede blev det nationalromantiska inslaget tydligt, med branta takfall och fönster med småspröjsade rutor.",
       "Fasaderna var ofta liggande träpanel eller spån som tjärades eller målades med röd slamfärg, och även puts förekom. Gamla Enskede är riksintresse för kulturmiljövården, och enligt stadens områdesfakta för 2025 finns där 898 småhus med äganderätt.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Gamla Enskede: 898", "Enskede gård: 417", "Enskedefältet: 405"]}},
    {"id": "kulorerna-enskede", "h2": "Trähus och puts",
     "paras": [
       "Strategins exempel från Gamla Enskede visar trähus som ofta är rödfärgade med vita snickerier. De putsade husen har fasader i varma, ljusa jordkulörer, och färgsättningen bygger på kontrast mellan fasad och snickerier i fönster och byggnadsdetaljer, ofta med fönstersnickerier i en dovare kulör. Slät- och spritputs används som dekor eller för att framhäva en del av byggnaden.",
       "Strategin råder att karaktärsskapande material, kulörer, byggnadsdelar och detaljer tas tillvara eller återskapas så långt det går. Vid en ommålning i Gamla Enskede väljer vi därför kulör för både fasad och snickerier, så att kontrasten finns kvar.",
     ],
     "aside": {"title": "Gamla Enskede enligt strategin", "items": [
       "Rödfärgad panel, vita snickerier", "Puts i varma ljusa jordkulörer", "Kontrast mot snickerierna"]}},
    {"id": "enskededalen-enskede", "h2": "Enskededalen och 1920-talets toner",
     "paras": [
       "I den fortsatta utbyggnaden blev 1920-talets klassiska formspråk rådande, bland annat i Enskededalen. Husen fick enkla volymer i ett och ett halvt plan, och det vanligaste fasadmaterialet var stående träpanel med tunn lockläkt. Färgskalan gick enligt strategin i ljusa, dämpade toner av grönt, gult eller grått.",
       "Enskededalen och Enskede gård är markerade som kulturhistoriskt värdefull miljö i strategins tabell, och för Enskededalen och Enskedefältet finns också äldre miljöprogram. Programmen har ingen juridisk status i bygglovsprövningen, men staden beskriver dem som ett bra underlag för att förstå områdets karaktär.",
     ],
     "aside": None},
    {"id": "lovet-enskede", "h2": "Ny kulör i riksintresset",
     "paras": [
       "Inom ett riksintresse för kulturmiljövården, som visas med blå ring i Stadsmuseets karta, behöver du bygglov för åtgärder som annars är lovfria. Boverket förklarar att en ny kulör, till exempel från rött till vitt, är en fasadändring, medan ommålning i samma kulör normalt räknas som underhåll.",
       "Vill du ändra kulören på ett hus i Gamla Enskede behöver det alltså prövas. Målar du i samma kulör som förut räcker det att vi tar fram rätt nyans. Om fasadmaterialen i Enskede kan du läsa under " + _L.format("fasadrenovering-enskede.html", "fasadrenovering i Enskede") + ".",
     ],
     "aside": None},
    {"id": "slamfargen-enskede", "h2": "Slamfärg, tjära och samma kulör",
     "paras": [
       "Riksantikvarieämbetet beskriver röd slamfärg som en av de bästa utomhusfärgerna för trähus och den mest underhållsvänliga: gammal färg borstas av, fasaden dammas av och målas oftast i en strykning. Har en röd slamfärg fått en tillsats av trätjära behöver tjära normalt tillsättas även vid ommålningen för att färgen ska fästa och kulören bli jämn.",
       "Kulören kan skilja något mellan tillverkare, och det märks särskilt vid bättringsmålning. Vi tar därför fram kulören mot den befintliga fasaden innan vi beställer färgen, och lagningar med nytt trä målas så att de smälter in. Om målning i stadsdelen i stort kan du läsa under " + _L.format("malare-enskede.html", "målare i Enskede") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Enskede till",
  "steps": [
    ("Platsbesök", "Fasaden, snickerierna och färgtypen går vi igenom."),
    ("Skrapprov", "Äldre kulörer och färgtyp tas fram på en liten yta."),
    ("Skriftligt kostnadsförslag", "Fasad och snickerier står var för sig."),
    ("Kulör och lov", "Samma kulör tas fram, eller ny kulör prövas när det krävs."),
    ("Målning", "Borstning, lagning och strykning i rätt färgtyp."),
    ("Genomgång", "Vi går igenom resultatet och skriver ner kulörerna."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Enskede",
  "rot": [
    "Skatteverket räknar målning av fasader på ett småhus som rotarbete, liksom att montera och montera ner byggnadsställningen. Du ska äga huset när arbetet utförs.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fasadmålningen i Enskede?",
  "price": [
    "Fasadens yta, färgtyp, underlagets skick, mängden snickerier och om kulören ska prövas i ett bygglov. En överblick finns under " + _L.format("malare.html", "målare") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för att måla vårt hus i Gamla Enskede i samma röda kulör?",
     "Nej, ommålning i samma kulör räknas normalt som underhåll. En ny kulör är däremot en fasadändring, och i riksintresset krävs då bygglov."),
    ("Vilka kulörer hade husen i Enskededalen?",
     "Enligt stadens strategi gick färgskalan i 1920-talets områden i ljusa, dämpade toner av grönt, gult eller grått."),
    ("Vår rödfärg innehåller tjära – spelar det roll?",
     "Ja, Riksantikvarieämbetet skriver att tjära normalt behöver tillsättas även vid ommålning för att färgen ska fästa och kulören bli jämn."),
    ("Har miljöprogrammet för Enskede juridisk betydelse?",
     "Nej, enligt Stockholms stad har de äldre miljöprogrammen ingen juridisk status i bygglovsprövningen, men de är ett bra underlag om områdets karaktär."),
  ],
  "sources": [_VARSAM, ("Stockholms stad – Områdesfakta 2025: Gamla Enskede (pdf)", _OF + "soderort/enskede/gamla-enskede.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Enskede gård (pdf)", _OF + "soderort/enskede/enskede-gard.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Enskedefältet (pdf)", _OF + "soderort/enskede/enskedefaltet.pdf"),
              _STH_FAS, _STH_KL, _BV_FAS, _RAA_MAL, _SKV, _SKV2],
  "cta": ("Ska fasaden på huset i Enskede målas om?", "Boka ett gratis platsbesök, så går vi igenom fasaden och kulörerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Rödfärgat trähus med vita snickerier och brant tegeltak",
     "1910s Swedish national romantic wooden house painted falu red with white trim and small-paned windows, steep red tile roof, hedge and garden, curving garden city street in southern Stockholm, summer" + _IMG_END),
    ("Putsat hus i varm ljus jordkulör med snickerier i dovare ton",
     "small 1910s Swedish rendered house in warm light ochre with window joinery in a darker muted green, steep red tile roof, garden with lilac, daylight" + _IMG_END),
    ("Villagata med hus i ljusa dämpade kulörer",
     "1920s Swedish garden city street with one and a half storey wooden houses painted in pale muted green, yellow and grey with board-and-batten facades, red tile roofs, hedges, summer" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SÖDERMALM
"fasadmalning-sodermalm.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Södermalm", "svc_label": "Fasadmålning",
  "trust": _TRUST_BRF,
  "title": "Fasadmålning på Södermalm – putsen mot gatan",
  "description": "Fasadmålning på Södermalm: bygglov för ny kulör mot gatan, Stadsmuseets karta, kalkfärg på puts, föreningens beslut och varför ROT inte gäller fasaden.",
  "h1": "Fasadmålning på Södermalm",
  "lead": "På Södermalm är det i regel en bostadsrättsförening eller en fastighetsägare som beställer fasadmålningen, och en ny kulör på gatufasaden kräver bygglov. Geal Entreprenad AB målar fasader på flerbostadshus på Södermalm och tar fram underlaget som föreningen och bygglovet behöver.",
  "card": "Putsen mot gatan.",
  "sections": [
    {"id": "foreningarna-sodermalm", "anchor": "Föreningarna",
     "h2": "Ett stadsdelsområde av föreningar",
     "paras": [
       "Enligt stadens områdesfakta för 2025 finns 43 542 bostadsrätter i flerbostadshus i Södermalms stadsdelsområde, medan småhusen med äganderätt bara är 13. Den som beställer en fasadmålning är därför i regel en bostadsrättsförening, en hyresvärd eller allmännyttan.",
       "I en bostadsrättsförening är fasaden en gemensam del av huset. Enligt bostadsrättslagen ska en förenings ekonomiska plan numera innehålla en teknisk underhållsplan som visar fastighetens underhållsbehov de kommande 50 åren, och en fasadmålning är en av de poster som brukar planeras långt i förväg.",
     ],
     "aside": {"title": "Södermalm 2025", "items": [
       "Bostadsrätter i flerbostadshus: 43 542", "Småhus med äganderätt: 13"]}},
    {"id": "lovet-sodermalm", "h2": "Ny kulör mot gatan kräver lov",
     "paras": [
       "För byggnader som inte är en- eller tvåbostadshus krävs bygglov inom detaljplan för fasadändring på en fasad eller ett tak som vetter mot allmän plats, alltså mot gata, torg eller park. Boverket förklarar att det räcker att en del av fasaden vetter mot allmän plats för att lov ska krävas för hela den fasaden, och att det bara är den fasaden som prövas.",
       "En ny kulör är en fasadändring, medan ommålning i samma kulör normalt räknas som underhåll. Gårdsfasaden kan alltså ofta målas om i ny kulör utan lov, om huset inte är klassat och detaljplanen inte säger något annat. Ett byte av färgtyp är enligt Boverket inget kulörbyte, men kan bedömas påverka byggnadens yttre karaktärsdrag.",
     ],
     "aside": {"title": "Lov för fasadmålning", "items": [
       "Ny kulör mot gatan: bygglov", "Samma kulör: underhåll", "Gårdsfasad: lov om huset är blått eller grönt"]}},
    {"id": "kartan-sodermalm", "h2": "Stadsmuseets klassning",
     "paras": [
       "Stockholms stad hänvisar till Stadsmuseets klassificeringskarta. Är byggnaden markerad med blått eller grönt, eller ligger den inom ett riksintresse eller ett särskilt kulturhistoriskt värdefullt område, behöver du bygglov även för åtgärder som annars är lovfria – då gäller det också gårdsfasaden.",
       "Staden påpekar att en antikvarisk förundersökning kan behövas inför arbeten på särskilt värdefulla byggnader, och att det kan krävas en certifierad sakkunnig inom kulturvärden. Vi tar reda på klassningen innan kulören föreslås. Om fasadmaterial och puts på Södermalm kan du läsa under " + _L.format("fasadrenovering-sodermalm.html", "fasadrenovering på Södermalm") + ".",
     ],
     "aside": None},
    {"id": "kalkfargen-sodermalm", "h2": "Kalkfärg på puts",
     "paras": [
       "Riksantikvarieämbetet beskriver kalkfärg som den färg som i århundraden använts på puts, med en levande, något flammig yta. Vid mitten av 1900-talet gick man alltmer över till kalkcementbruk och andra färger. Kalkfärg släpper igenom fukt, har god vidhäftning på kalkputs men dålig på cementrika underlag, och används i dag främst vid ommålning av fasader som redan är kalkavfärgade och på ny kalkputs på kulturhistoriskt värdefulla hus.",
       "Utomhus målas kalkfärg från senvåren till eftersommaren och i god tid före frost, ett skikt per dag och i 3–7 strykningar. En fasadyta får inte avbrytas mitt i, bara vid hörn eller andra naturliga gränser, och fönsterglas ska skyddas eftersom kalken etsar glas. Därför planeras ställning, väderskydd och arbetslag för hela fasaden på en gång. Kulört kalkfärg bör enligt Riksantikvarieämbetet blandas vid ett och samma tillfälle för hela ytan, eftersom kulören annars lätt avviker.",
     ],
     "aside": {"title": "Kalkfärg enligt RAÄ", "items": [
       "Senvår till eftersommar", "Ett skikt per dag", "3–7 strykningar utomhus", "Skydda fönsterglaset"]}},
    {"id": "underlaget-sodermalm", "h2": "Rätt färg på rätt puts",
     "paras": [
       "Innan färgtypen väljs tar vi reda på vad fasaden är målad med i dag och vilket bruk den är putsad med. En lagning med cementhaltig puts i en kalkputsfasad ska enligt Riksantikvarieämbetet tas bort och putsas om med kalkputs innan fasaden kalkas.",
       "Föreningen får ett skriftligt underlag med fasadernas skick, färgtyp, förslag på kulör och vilka fasader som kräver lov. Om måleri på Södermalm i övrigt kan du läsa under " + _L.format("malare-sodermalm.html", "målare på Södermalm") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning på Södermalm till",
  "steps": [
    ("Platsbesök", "Fasaderna, putsen och färgtypen går vi igenom med styrelsen."),
    ("Klassning och lov", "Stadsmuseets karta och detaljplanen kontrolleras, gata och gård för sig."),
    ("Skriftligt kostnadsförslag", "Varje fasad, ställning och väderskydd står för sig."),
    ("Bygglov", "Ansökan med kulörförslag tas fram när kulören ändras mot gatan."),
    ("Målning", "Putslagning och strykning i rätt färgtyp, fasadyta för fasadyta."),
    ("Genomgång", "Vi går igenom resultatet med styrelsen och lämnar dokumentationen."),
  ],
  "rot_h2": "Rotavdrag gäller inte fasaden",
  "rot": [
    "Skatteverket ger rotavdrag i en bostadsrätt bara för arbete inne i bostaden som bostadsrättshavaren ansvarar för enligt stadgarna. Arbete på gemensamma ytor, till exempel tak, fasader, trapphus och entréer, ger inget rotavdrag.",
    "En fasadmålning på ett föreningshus betalas därför av föreningen utan avdrag, och kostnadsförslaget ställs till föreningen.",
  ],
  "price_h2": "Vad påverkar priset för fasadmålningen på Södermalm?",
  "price": [
    "Fasadernas yta och höjd, putsens skick, färgtyp, ställning och väderskydd mot gatan och om bygglov behövs. Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vår förening på Södermalm bygglov för att måla gårdsfasaden i ny kulör?",
     "Normalt inte, eftersom lovplikten gäller fasader som vetter mot allmän plats. Är huset klassat blått eller grönt i Stadsmuseets karta krävs dock lov även för gårdsfasaden."),
    ("Prövas hela huset om vi byter kulör mot gatan?",
     "Nej, enligt Boverket är det bara fasaden som vetter mot allmän plats som prövas i bygglovet."),
    ("Kan vi använda kalkfärg på vår fasad?",
     "Kalkfärg fäster bra på kalkputs men dåligt på cementrika underlag, enligt Riksantikvarieämbetet. Vi tar reda på vilket bruk fasaden har innan färgtypen väljs."),
    ("När på året kan en kalkfärgad fasad målas?",
     "Utomhus från senvåren till eftersommaren och i god tid före frost, enligt Riksantikvarieämbetet. Undvik starkt solsken."),
    ("Får vi rotavdrag för fasadmålningen?",
     "Nej, arbete på gemensamma ytor som fasader i en bostadsrättsförening ger inget rotavdrag enligt Skatteverket."),
  ],
  "sources": [("Stockholms stad – Områdesfakta 2025: Södermalms stadsdelsområde (pdf)", _OF + "inre-staden/sodermalm/sodermalm-stadsdelsomrade.pdf"),
              _BRL, _BV_FAS, _STH_FAS, _STH_KL,
              ("Stockholms stad – Kulturhistorisk värdefull byggnad och område", _SB + "kulturhistorisk-vardefull-byggnad-och-omrade/"),
              _RAA_MAL, _SKV],
  "cta": ("Ska föreningens fasad på Södermalm målas om?", "Boka ett gratis platsbesök, så går vi igenom fasaderna och lovfrågan innan föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Putsad gatufasad på ett sekelskifteshus i ljus kalkfärg",
     "early 1900s Stockholm stone apartment building with freshly lime-painted rendered street facade in warm light ochre, white window surrounds, cobbled street, Södermalm style, daylight" + _IMG_END),
    ("Byggnadsställning med väderskydd framför en putsfasad",
     "empty street, no pedestrians, no cars: scaffolding with weather protection sheeting covering the rendered facade of a five storey Stockholm apartment building during repainting, street with trees, daylight" + _IMG_END),
    ("Kalkfärgad puts med flammig yta i närbild",
     "close view of a rendered wall freshly painted with lime paint showing a lively slightly mottled surface in pale ochre, window frame masked with paper, daylight" + _IMG_END),
  ],
},
}
