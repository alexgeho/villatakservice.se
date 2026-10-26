# -*- coding: utf-8 -*-
"""Golvslipning – ortsidor v17: Bromma, Danderyd, Ekerö, Farsta, Haninge, Huddinge (2026-10-26).
Deltjänst under golvlaggning.html (TJ_HUB["golvslipning"]). Intent: slipa och ytbehandla ett BEFINTLIGT trägolv –
inte lägga nytt eller välja golvmaterial (det är golvlaggare-<ort>.html, som varje sida länkar till i texten).
Lokal vinkel per sida (skild från ortens golvlaggare-sida, från v15-sidorna och från varandra):
Bromma – lut och såpa på furugolv i trädgårdsstäderna (Varsam s. 17–19 och tabellen s. 85–86): lutens kemi,
skyddstäckning, serpentinmetoden, avjämning efter 24 timmar, fuktkvot, såpa 3–4 gånger, lack på lut avråds;
Danderyd – mönsterlagd parkett och stavgolv i villastäderna (ÖP kap. 3): diagonal slipning, kanter, byte av enstaka
stav och färgskillnad, springor i smal stav mot bred bräda, lacktyp och spackling med stålspackel;
Ekerö – golvslipning i hus med golvvärme (kulturmiljöprogrammet: villor från 1960-talet till 2000-talet): yttemperatur
under behandlingen, 27 °C även under mattor, luftfuktighet på vintern, bok och lönn, springor;
Farsta – så bedöms ett färdigslipat golv (GBR:s bedömningsgrunder för massiva trägolv): stående besiktning, klimat
vid besiktningen, slipränder, kantringar, hörn, ondulering, överskottsolja, rödfärgning av furu;
Haninge – laga golvet före slipningen i 1940–1960-talens villor (Haninges karaktärsmiljöer): kantskador, kvisthål,
fogsprång, springor, kupning och skålning, fuktskador och lösa partier;
Huddinge – byta ytbehandling när golvet slipas om i egnahemsområdena (kulturmiljöprogram del 2): från lack till olja
och tvärtom, lut och lack, rester av vax och såpa, olja som ger bärnstenston, UV och rödfärgning, förbjuden lacktyp.

Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-26:
  Golvbranschen GBR (Branschriktlinjer SLIP 22, LACK 22, OLJA 22, LUT 22, UNDERHÅLL 22 – pdf med text; Bedömningsgrunder
  för skönhetsfel, inlagda massiva trägolv, rev. mars 2016 – pdf med text; Trägolv på golvvärme, maj 2022 – pdf med
  text; webbsidan Trägolv på golvvärme), Skatteverket (Ger arbetet rätt till rotavdrag?: slipa och byta golv, småhus
  inkl. fritidshus; Så fungerar rotavdraget: 30 procent, 50 000/75 000 kr, bara arbetad tid på plats, material och
  resor ger inget avdrag), Stockholms stad (Varsam utveckling av småhus- och villaområden, pdf med text: trädgårdsstad
  s. 13–19, tunnelbanestad s. 57–61, tabellen s. 85–86; Områdesfakta 2025, pdf: Södra Ängby, Ålsten, Farsta, Farsta
  strand), Danderyds kommun (Översiktsplan, kap. 3 Riks- och mellankommunala intressen, pdf med text), Ekerö kommun
  (Ekerö kulturmiljöprogram 2015, pdf med text: Mälaröarna s. 42, Östra Ekerö s. 43), Haninge kommun (Haninges
  karaktärsmiljöer, pdf med text: folkhemsbygget 1940–1960-tal, rekordåren 1960–1980-tal), Huddinge kommun
  (Kulturmiljöprogram del 2, småhusen, pdf med text s. 9–11).
Kontrollerade siffror: Södra Ängby 2025: 549 bostäder, 499 i småhus, 495 äganderätter; Ålsten 2025: 1 106 bostäder,
911 i småhus, 811 äganderätter; Farsta 2025: 7 810 bostäder, 545 i småhus, 3 415 bostadsrätter, 3 046 allmännyttan;
Farsta strand 2025: 2 861 bostäder, 328 i småhus; Högdalen 1960, Farsta 1961 (Varsam); Djursholm 1890–1930, landets
första som förort anlagda villastad, Stocksund sekelskiftet och 1900-talets två första decennier, Ringen/Skogsliden
1910-talet (Danderyd ÖP); Ekerö: befolkningen fördubblad sedan 1970, minst 2 475 villor under 1990- och 2000-talet,
Väsby tidigt 1970-tal, Närlunda 1960-tal (kulturmiljöprogrammet); Haninge: folkhemsbygget 1940–1960-tal med exempel
Handen, Jordbro, Vendelsö, Vendelsömalm, Västerhaninge, rekordåren 1960–1980-tal; Huddinge: Västra stambanan 1860,
Hörningsnäs municipalsamhälle 1915, Huddinge/Fullersta/Stuvsta/Segeltorp 1924, Snättringe 1929, stormunicipal 1947,
kataloghus i trä med flacka sadeltak på 1940-talet; LUT 22: natrium- och kaliumhydroxid, avjämning efter 24 timmar,
skurmaskin 150 varv/min och röd rondell, fuktkvot högst 12 % före slutbehandling, åtgång 6–8 m²/liter, såpa 3–4
appliceringar, lack på lut rekommenderas inte, ofärgad olja bärnstensfärgad nyans som ljusnar något; SLIP 22: diagonal
slipning av mönster, kanter med något grövre korn, korn 100 barrträ/120 lövträ, inga slipränder utom efter
slutpapperet, ondulering vid svikt, lossnat slitskikt limmas ner, vattenskadat golv – avrådan vid risk för stavsläpp;
LACK 22: yttemperatur lägre än rumsluften vid golvvärme, 20 ± 2 °C, höjs under 2–3 dagar till högst 27 °C, första
strykningen kan ersättas med 3 spacklingar med rostfri stålspackel, lacktyper efter slitage, lackering på lutade golv
avråds, på oljade golv fungerar det för vissa fabrikat, formaldehydavgivande syrahärdande golvlack förbjuden;
OLJA 22: ytan fri från fett, såpa, vax och lackrester, fuktkvot ≤ 12 % barrträ/≤ 8 % lövträ, yttemperatur 20 ± 2 °C
vid golvvärme och sedan högst 27 °C, trasor i vatten minst 24 timmar; Golvvärmehandboken: 30 % RF vid 20 °C blir ca
20 % vid 27 °C, 27 °C även under mattor och möbler, luftfuktare vintertid, lamellparkett av bok och lönn ska inte
användas på golvvärme, massiva golv rör sig mer, krympning ca 1 % av brädans bredd, smal stav liten springa;
Bedömningsgrunderna: besiktning stående med normal noggrannhet, fel som bara syns i visst ljus eller efter
påpekande räknas inte, klimat 18–25 °C och 30–60 % RF vid besiktning, fogsprång högst ±0,3 mm, springor 1 % av
bredden vid 30 % RF, kupning/skålning högst 1 %, rödfärgning av furu åtgärdas ej, färgskillnad ny/gammal bräda
minskar över tiden, slipränder/kantringar/ej slipade hörn/ondulering/överskottsolja med respektive åtgärd.
Strukna (ej verifierade eller medvetet utelämnade): vilka golv husen i Södra Ängby, Djursholm, Farsta, Vendelsö eller
Stuvsta har från början (furu, fiskben, stavparkett – skrivet som villkor "har huset …"); att golvvärme är vanligt i
Ekerös nyare villor (ingen källa – skrivet som villkor); att lut "skyddar" golvet (källan beskriver bara kulören);
hur ofta ett såpat golv ska såpas om (ingen siffra i LUT 22); att syrahärdande lack finns på äldre golv i Huddinge
(ingen källa – bara att lacktypen är förbjuden i dag); att golvvärmen ska vara avstängd vid slipningen (källorna anger
bara yttemperatur under ytbehandlingen); att bedömningsgrunderna gäller för just renoverade golv i domstol (GBR
skriver bara att de är praxis i domstol och ARN – inte använt); antal mm som slipas bort per slipning (ingen källa);
GBR:s TK-råd 119R (inte öppnat); Byggnadsvårdsföreningens råd om lut och såpa (ej öppnat – bara LUT 22 används);
avgifter, priser, tidsåtgång.
Kritikpass 2026-10-26: alla källor öppnade på nytt (pdf via pdftotext, text i alla); siffror, år och Varsam-tabellen
s. 85–86 (Södra Ängby riks+värdefull+miljöprogram, Ålsten riks+värdefull, Nockeby/Höglandet/Smedslätten/Äppelviken
värdefulla, Farsta värdefull, Farsta strand ingen markering) stämmer. Rättat/struket: Bromma – "som många förknippar
med äldre svenska hus" (ingen källa); Danderyd – "ränderna syns i varannan stav" (ersatt med SLIP 22:s slipordning);
Ekerö – "slipningen är inte svårare" (ingen källa); Farsta – "oftast i en bostadsrätt eller ett radhus" (ersatt med
områdesfaktas 3 415 bostadsrätter), "nylagt" golv, motiveringen "egenskap hos träet/träets egen förändring" för
UV/rödfärgning (bedömningsgrunderna anger bara "åtgärdas ej"); Haninge – "har ofta märken" mjukat, "flera ägare och
lika många sätt" struket, "djupt märke slipas sällan bort" och "kupade brädor kan slipas plana" (ingen källa);
Huddinge – att lutat eller oljat golv kan lackas efter slipning till rent trä (ej i LACK/LUT 22; ersatt med LUT 22:s
slutbehandlingar), motiveringen "hör till träet", "golven har hunnit behandlas" mjukat till "kan ha".
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_DAN_RIKS = ("Danderyds kommun – Översiktsplan, Riks- och mellankommunala intressen (pdf)",
             "https://danderyd.se/contentassets/94fc6956dc264c4cab52c0a18ff5bafd/3-riks--och-mellankommunala-intressen.pdf")
_EKERO_KMP = ("Ekerö kommun – Ekerö kulturmiljöprogram 2015 (pdf)",
              "https://www.ekero.se/download/18.553838ea17305720c321ec82/1597925412772/Eker%C3%B6%20kulturmilj%C3%B6program.pdf")
_HAN_KAR = ("Haninge kommun – Haninges karaktärsmiljöer (pdf)",
            "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf")
_HUD_KMP2 = ("Huddinge kommun – Kulturmiljöprogram del 2, småhusen (pdf)",
             "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf")
_G = "https://www.golvbranschen.se/siteassets/dokument/"
_GBR_SLIP = ("Golvbranschen – Branschriktlinjer SLIP 22, slipning av trägolv (pdf)",
             _G + "branschriktlinjer/branschriktlinjer---slipning-av-tragolv---slip-22.pdf")
_GBR_LACK = ("Golvbranschen – Branschriktlinjer LACK 22, lackering av trägolv (pdf)",
             _G + "branschriktlinjer/branschriktlinjer---lackering-av-tragolv---lack-22.pdf")
_GBR_OLJA = ("Golvbranschen – Branschriktlinjer OLJA 22, oljebehandling av trägolv (pdf)",
             _G + "branschriktlinjer/branschriktlinjer---oljebehandling-av-tragolv---olja-22.pdf")
_GBR_LUT = ("Golvbranschen – Branschriktlinjer LUT 22, lutbehandling av trägolv (pdf)",
            _G + "branschriktlinjer/branschriktlinjer---lutbehandling-av-tragolv---lut-22.pdf")
_GBR_UND = ("Golvbranschen – Branschriktlinjer UNDERHÅLL 22, underhåll av trägolv (pdf)",
            _G + "branschriktlinjer/branschriktlinjer---underhall-av-tragolv---underhall-22.pdf")
_GBR_BED = ("Golvbranschen – Bedömningsgrunder för skönhetsfel, inlagda massiva trägolv (pdf)",
            _G + "bedomningsgrunder/bedomning-massiva-tragolv-1603.pdf.pdf")
_GBR_GV = ("Golvbranschen – Trägolv på golvvärme, maj 2022 (pdf)",
           _G + "tragolv-pa-golvvarme/tragolv-pa-golvvarme-maj-2022.pdf")
_GBR_GVW = ("Golvbranschen – Trägolv på golvvärme",
            "https://www.golvbranschen.se/teknik--material/tragolv/tekniska-tragolvsfragor/tragolv-pa-golvvarme/")

_HUB = _L.format("golvlaggning.html", "golvläggning")
_ROT_SUM = ("Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
            "tillsammans med rutavdrag.")

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"golvslipning-bromma.html": {
  "kind": "district", "service": "golvslipning", "ort": "Bromma", "svc_label": "Golvslipning",
  "title": "Golvslipning i Bromma – lut och såpa på furugolvet",
  "description": "Golvslipning i Bromma: slipa furugolvet i trädgårdsstadens villa och behandla det med lut och såpa – skyddstäckning, arbetsgång, torrt trä och provyta.",
  "h1": "Golvslipning i Bromma",
  "lead": "Ett slipat furugolv som lutas och såpas får en ljus och matt yta. Det är en behandling med egna regler: luten är frätande, den ska läggas i en viss ordning och den passar inte med lack. Geal Entreprenad AB slipar och ytbehandlar trägolv i Bromma, och väljer du lut och såpa går vi igenom hela arbetsgången med dig innan första strykningen.",
  "card": "Slipa furugolvet och behandla med lut och såpa.",
  "sections": [
    {"id": "tradgardsstad-bromma", "anchor": "Trädgårdsstäderna",
     "h2": "Trädgårdsstäder från 1920- och 1930-talen",
     "paras": [
       "Stockholms stads vägledning Varsam utveckling av småhus- och villaområden beskriver hur nya trädgårdsstäder kom till i Äppelviken, Ålsten och Smedslätten under 1920-talet. I Nockeby, Höglandet, Ålsten och Ulvsunda blev 1920-talets klassiska formspråk rådande, med enkla volymer i ett och ett halvt plan. Södra Ängby blev den sista stadsdelen som planerades efter trädgårdsstadens principer och är enligt vägledningen ett av Europas största sammanhängande områden av villor från 1930-talet i modernistisk stil.",
       "I vägledningens tabell på sidorna 85–86 är Södra Ängby både riksintresse och kulturhistoriskt värdefull miljö och har ett äldre miljöprogram. Ålsten är riksintresse och värdefull miljö, och Nockeby, Höglandet, Smedslätten och Äppelviken räknas som värdefulla miljöer. Vägledningen konstaterar samtidigt att många hus har förändrats interiört och byggts till genom åren. Inne i huset handlar det oftast om att välja en yta som passar golvet du har.",
     ],
     "aside": {"title": "Villor i två trädgårdsstäder 2025", "items": [
       "Södra Ängby: 499 av 549 bostäder i småhus", "Södra Ängby: 495 äganderätter", "Ålsten: 911 av 1 106 i småhus", "Ålsten: 811 äganderätter"]}},
    {"id": "luten-bromma", "h2": "Vad luten gör med furun",
     "paras": [
       "Golvbranschens riktlinjer för lutbehandling, LUT 22, beskriver traditionell lutbehandling på homogena golv av fur och gran. För lövträ finns särskilda produkter som riktlinjerna inte går in på, och på lamellgolv ska man vara extra försiktig. Lut består av natrium- och kaliumhydroxid i vattenlösning och är starkt frätande. Ett lutat golv får en djupare och jämnare infärgning när det pigmenteras efteråt.",
       "Riktlinjerna för oljebehandling, OLJA 22, beskriver samma effekt från andra hållet: att luta ett golv av fur eller gran före grundbehandlingen bevarar ljusheten i kombination med vit olja, eller ger en djupare kulör. Vilken av vägarna ditt golv tar visar en provyta. LUT 22 säger att ett mindre prov ska göras innan hela ytan behandlas, så att resultatet blir det du vill ha.",
       "Är du osäker på om golvet är massiv furu eller en lamellparkett med ett tunt slitskikt tar vi reda på det innan vi föreslår lut. Hur det kontrolleras beskrivs på sidan om " + _L.format("golvslipning-sollentuna.html", "golvslipning i Sollentuna") + ".",
     ],
     "aside": {"title": "Lut enligt LUT 22", "items": [
       "Natrium- och kaliumhydroxid", "Starkt frätande", "För fur och gran", "Prov före hela ytan"]}},
    {"id": "arbetsgang-bromma", "h2": "Skyddstäckning och arbetsgång",
     "paras": [
       "Eftersom luten fräter är skyddstäckningen av angränsande ytor mycket viktig. LUT 22 nämner särskilt målade ytor, metall och ytor av lövträ, till exempel en ekparkett i rummet bredvid eller metallbeslag på en tröskel. Den som arbetar använder gummihandskar och skyddsglasögon, och luten blandas i kärl av plast. Borstar och verktyg ska inte ha skaft eller handtag av metall.",
       "Arbetet görs i hela planklängder. Man börjar längst in i ett hörn, lägger lut på ett par plankors bredd, arbetar sig bort till det andra hörnet, vänder och fortsätter rummet ut som en serpentin. Luten läggs vått i vått för att minska risken för skarvar. Hela mängden för ytan hälls upp på en gång och rörs om under arbetet, så att kalk och pigment inte sjunker till botten. Riktlinjerna anger en total åtgång på 6–8 kvadratmeter per liter för färdig yta.",
       "Efter 24 timmar jämnas kalk- och pigmentöverskottet av med skurblock eller en skurmaskin med röd rondell, och golvet dammsugs noga. Då ska dammskydd för näsa och mun användas.",
     ],
     "aside": None},
    {"id": "saapa-bromma", "h2": "Såpa, olja eller hårdvaxolja efter luten",
     "paras": [
       "Ett lutat golv behöver en slutbehandling. LUT 22 beskriver tre: såpa, ofärgad eller med vitt pigment, som i regel kräver 3–4 appliceringar för full mättnad; golvolja som ger en sidenmatt yta; och hårdvaxolja i olika glansgrader. Golvets fuktkvot bör inte överstiga 12 procent före slutbehandlingen, och det mäter vi.",
       "Lack är däremot inget alternativ. Både LUT 22 och riktlinjerna för lackering, LACK 22, avråder från lack på ett lutat golv. Vill du ha ett lackat golv i hallen och ett lutat i vardagsrummet behöver gränsen mellan ytorna planeras före slipningen.",
       "Väljer du olja eller hårdvaxolja gäller samma brandregel som för all olja: trasor och annat organiskt material som varit i kontakt med oljan ska enligt OLJA 22 ligga i vatten i minst 24 timmar eller brännas direkt. Funderar du på att ta fram ett golv som ligger under en matta, eller på att lägga nytt, finns mer under " + _L.format("golvlaggare-bromma.html", "golvläggare i Bromma") + " och på sidan om " + _HUB + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipning med lut till i Bromma",
  "steps": [
    ("Platsbesök", "Vi kontrollerar träslag och golvtyp och mäter fuktkvoten i brädorna."),
    ("Skriftligt kostnadsförslag", "Slipning, lutning och slutbehandling står som egna poster."),
    ("Slipning", "Golvet slipas till rent trä i flera steg, och kanterna slipas för sig."),
    ("Skyddstäckning och prov", "Lister, trösklar och angränsande golv täcks, och en provyta lutas."),
    ("Lutning", "Luten läggs i hela planklängder och jämnas av efter ett dygn."),
    ("Såpa eller olja", "Slutbehandlingen läggs i flera omgångar tills ytan är mättad."),
  ],
  "rot_h2": "ROT-avdrag när golvet i villan slipas",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete i ett småhus. Det är bara arbetad tid på plats hos dig som ger avdrag – lut, såpa och olja räknas som material.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Bromma?",
  "price": [
    "Golvytan, golvets skick, hur mycket som behöver skyddstäckas och hur många omgångar såpa eller olja golvet behöver. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi luta och såpa furugolvet i vår villa i Bromma?",
     "Ja, om golvet är av fur eller gran och går att slipa. Golvbranschens riktlinjer beskriver lut för just de träslagen, följt av såpa, olja eller hårdvaxolja."),
    ("Varför ska golvet inte lackas efter lutningen?",
     "Golvbranschen avråder från lack på lutbehandlade golv. Efter luten används såpa, golvolja eller hårdvaxolja."),
    ("Hur många gånger behöver ett lutat golv såpas?",
     "Enligt Golvbranschen krävs i regel 3–4 appliceringar av såpa för att ytan ska bli mättad."),
    ("Kan luten skada ekparketten i rummet bredvid?",
     "Ja. Luten är starkt frätande, och riktlinjerna pekar särskilt ut lövträ, metall och målade ytor. Därför täcker vi dem innan arbetet börjar."),
    ("Blir ett lutat golv ljust med vit olja?",
     "Golvbranschen skriver att lut före grundbehandlingen bevarar ljusheten på fur och gran i kombination med vit olja. Ett prov på ditt golv visar tonen."),
  ],
  "sources": [
    _VARSAM,
    ("Stockholms stad – Områdesfakta 2025: Södra Ängby (pdf)", _OF + "vasterort/bromma/sodra-angby.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Ålsten (pdf)", _OF + "vasterort/bromma/alsten.pdf"),
    _GBR_LUT, _GBR_OLJA, _GBR_LACK, _SKV, _SKV2,
  ],
  "cta": ("Vill du ge furugolvet i Bromma lut och såpa?", "Boka ett gratis platsbesök, så kontrollerar vi golvet och gör en provyta innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust lutat och såpat furugolv med breda brädor i ett tomt rum i en villa från 1920-talet",
     "empty room in a 1920s Swedish garden-city villa, wide pine floorboards freshly treated with white lye and soap giving a pale matte Scandinavian surface, white painted panelled walls, small-paned window with soft daylight, no furniture, no people, no text"),
    ("Hink av plast, lutborste med träskaft och skurblock på ett nyslipat furugolv",
     "close-up of a plastic bucket, a wide lye brush with a wooden handle and a scrubbing block resting on a freshly sanded bare pine floor, part of the floor already lye-treated paler than the rest, masking paper along a white skirting board, no people, no text"),
  ],
},

# ------------------------------------------------------------------ DANDERYD
"golvslipning-danderyd.html": {
  "kind": "district", "service": "golvslipning", "ort": "Danderyd", "svc_label": "Golvslipning",
  "title": "Golvslipning i Danderyd – parkett och mönster i villan",
  "description": "Golvslipning i Danderyd: slipa fiskbens- och stavparkett i villan – slipriktning, kanter, byte av enstaka stavar, springor och val av lack eller olja.",
  "h1": "Golvslipning i Danderyd",
  "lead": "En fiskbensparkett eller ett golv i rutmönster har stavar som ligger åt olika håll, och det ställer egna krav på hur maskinen förs över golvet. Golvbranschens riktlinjer beskriver därför en särskild slipordning för mönstergolv. Geal Entreprenad AB slipar och ytbehandlar trägolv i Danderyd och planerar slipriktningen efter mönstret och rummets ljus innan arbetet börjar.",
  "card": "Slipa parkett och mönstergolv i villan.",
  "sections": [
    {"id": "villastaderna-danderyd", "anchor": "Villastäderna",
     "h2": "Villastäder med hus från 1890 och framåt",
     "paras": [
       "Danderyds översiktsplan beskriver Djursholm som landets första villastad anlagd som förort, grundad på privat initiativ. Bebyggelsen speglar framför allt perioden 1890–1930, och i villorna kan stilidealen följas från de första enkla trävillorna till nationalromantik, jugend och funktionalism. Stocksund beskrivs som en villastad från sekelskiftet och 1900-talets två första decennier, med villor för ett välbärgat tjänstemannaskikt.",
       "Planen pekar ut värdekärnor där riksintresset preciseras. I området Ringen och Skogsliden är i stort sett samtliga villor byggda på 1910-talet, och i området kring Vasavägen är villorna uppförda mellan 1890 och 1910. Beskrivningarna gäller husen utifrån. Vilket golv som ligger i salongen eller hallen avgörs på plats, och har det ett mönster börjar planeringen där.",
     ],
     "aside": {"title": "Ur Danderyds översiktsplan", "items": [
       "Djursholm: 1890–1930", "Stocksund: 1900-talets början", "Ringen/Skogsliden: 1910-talet", "Vasavägen: 1890–1910"]}},
    {"id": "slipriktning-danderyd", "h2": "Mönstret styr slipriktningen",
     "paras": [
       "Golvbranschens riktlinjer för slipning, SLIP 22, säger att finslipning med bandmaskin ska göras i träets längdriktning. På rutmönster, fiskben och andra mönster där träet ligger åt olika håll går det inte, och då slipas golvet normalt först diagonalt och sedan i rummets längdriktning, eller från det håll ljuset kommer. Efter färdigslipningen får inga slipränder finnas kvar annat än efter slutpappret.",
       "Kanterna längs väggarna slipas med en kantslip och något grövre papper än golvet i övrigt, så att strukturen blir densamma ända ut till listen. Oavsett maskin ska slutresultatet motsvara bandslipning med korn 100 för barrträ och 120 för lövträ, och det får inte finnas skillnader i struktur mellan kanterna och resten av golvet.",
       "I ett rum med stora fönster åt ett håll väljer vi därför slipriktning efter fönstren, så som riktlinjerna beskriver.",
     ],
     "aside": {"title": "Slipning av mönstergolv", "items": [
       "Först diagonalt", "Sedan i rummets längdriktning", "Eller från ljusets håll", "Kanter med något grövre papper"]}},
    {"id": "stavar-danderyd", "h2": "Enstaka stavar som behöver bytas",
     "paras": [
       "I ett gammalt parkettgolv kan någon stav vara skadad, spjälkad eller tydligt mörkare än de andra. Golvbranschens bedömningsgrunder för massiva trägolv anger byte av stav eller bräda som åtgärd för urspjälkning och kantskador, och för en mörk eller ljus stav som sticker ut. Mindre fel kan i stället spacklas och lagas.",
       "En ny stav kan ha en annan ton än de gamla. Bedömningsgrunderna konstaterar att färgskillnader mellan gammal och ny beläggning kan förekomma vid byte, men att skillnaden minskar med tiden. Därför byter vi så få stavar som möjligt och väljer dem så lika det gamla träet som det går.",
       "Springor är en mindre fråga i parkett än i breda brädor. Golvbranschens handbok Trägolv på golvvärme skriver att springornas storlek till stor del beror på stavens eller brädans bredd. Smal stav ger liten springa, och på mindre massiva parkettstavar blir springbildningen mycket liten.",
     ],
     "aside": None},
    {"id": "ytan-danderyd", "h2": "Lack eller olja på parketten",
     "paras": [
       "Riktlinjerna för lackering, LACK 22, delar in golvlack efter slitage. Lack för lätt slitage är avsedd för bostadens rum utom kök och hall, lack för medelslitage för till exempel vardagsrum, och båda stryks tre gånger med mellanslipning efter första strykningen. Den första strykningen kan enligt riktlinjerna ersättas med tre spacklingar med rostfri stålspackel.",
       "Föredrar du olja ska golvet enligt OLJA 22 vara torrt, rent och nyslipat, och fuktkvoten får inte överstiga 8 procent i lövträ som ek eller 12 procent i barrträ.",
       "Hur golvet i en äldre villa bäst lagas, eller när det är rimligare att lägga nytt, beskrivs under " + _L.format("golvlaggare-danderyd.html", "golvläggare i Danderyd") + ". Mer om olika golv finns på sidan om " + _HUB + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går slipningen av ett parkettgolv till i Danderyd",
  "steps": [
    ("Platsbesök", "Vi tittar på mönstret, letar efter skadade stavar och ser varifrån ljuset kommer."),
    ("Skriftligt kostnadsförslag", "Slipning, stavbyten och ytbehandling redovisas var för sig."),
    ("Lagning", "Skadade stavar byts och mindre skador spacklas innan slipningen."),
    ("Diagonal slipning", "Golvet slipas först diagonalt över mönstret och sedan i rummets längdriktning."),
    ("Kanter och hörn", "Kantslip längs väggarna med samma struktur som resten av golvet."),
    ("Lack eller olja", "Ytbehandlingen läggs i rätt antal lager med torktid emellan."),
  ],
  "rot_h2": "ROT-avdrag för slipning av parkett",
  "rot": [
    "Att slipa golv räknas som rotarbete i ett småhus enligt Skatteverket. Avdraget gäller arbetad tid på plats, inte stavar, lack eller olja.",
    _ROT_SUM + " Material och resor ger inget avdrag, och Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Danderyd?",
  "price": [
    "Golvytan, mönstret, hur många stavar som behöver bytas och vilken ytbehandling du väljer betyder mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur slipas en fiskbensparkett i en villa i Danderyd?",
     "Normalt först diagonalt och sedan i rummets längdriktning eller från det håll ljuset kommer, enligt Golvbranschens riktlinjer. Efter slipningen ska inga slipränder synas."),
    ("Går det att byta en enstaka skadad stav i parketten?",
     "Ja. Golvbranschens bedömningsgrunder anger byte av stav vid urspjälkning och kantskador. Mindre skador kan spacklas."),
    ("Syns en ny stav bland de gamla?",
     "Till en början kan tonen skilja sig. Golvbranschen skriver att färgskillnaden mellan ny och gammal beläggning minskar över tiden."),
    ("Varför får parkett mindre springor än breda brädor?",
     "Springornas storlek beror till stor del på stavens bredd. Smal stav ger liten springa, och i massiv parkett blir springbildningen mycket liten."),
    ("Vad betyder spackling med stålspackel vid lackering?",
     "Golvbranschens riktlinjer för lackering anger att den första lackstrykningen kan ersättas med tre spacklingar med rostfri stålspackel, följda av mellanslipning vid behov."),
  ],
  "sources": [
    _DAN_RIKS, _GBR_SLIP, _GBR_BED, _GBR_GV, _GBR_LACK, _GBR_OLJA, _SKV, _SKV2,
  ],
  "cta": ("Ska parketten i villan i Danderyd slipas?", "Boka ett gratis platsbesök, så går vi igenom mönstret, stavarna och ytbehandlingen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipad och lackad fiskbensparkett i ek i en stor salong i en äldre villa",
     "large empty drawing room in an early 1900s Swedish national romantic villa, freshly sanded and lacquered oak herringbone parquet floor glowing in daylight from tall windows, white panelled walls, a white tiled stove in a corner, no furniture, no people, no text"),
    ("Detalj av fiskbensparkett där några stavar är nya och ljusare än de gamla",
     "close-up of an old oak herringbone parquet floor freshly sanded to bare wood, a few newly replaced parquet blocks slightly lighter in tone than the surrounding old ones, an edge sander resting near a white skirting board, no people, no text"),
  ],
},

# ------------------------------------------------------------------ EKERÖ
"golvslipning-ekero.html": {
  "kind": "district", "service": "golvslipning", "ort": "Ekerö", "svc_label": "Golvslipning",
  "title": "Golvslipning på Ekerö – trägolv med golvvärme",
  "description": "Golvslipning på Ekerö: slipa och ytbehandla ett trägolv som ligger på golvvärme – yttemperatur, torr vinterluft, springor och träslag som rör sig mycket.",
  "h1": "Golvslipning på Ekerö",
  "lead": "Ligger trägolvet på golvvärme måste ytbehandlingen göras vid rätt temperatur, och golvet måste få värmas upp igen i lugn takt. Geal Entreprenad AB slipar och ytbehandlar trägolv i villor och fritidshus på Ekerö, och i ett hus med golvvärme går vi igenom värmen med dig innan vi börjar.",
  "card": "Slipa trägolv som ligger på golvvärme.",
  "sections": [
    {"id": "villakommunen-ekero", "anchor": "Villorna",
     "h2": "En villakommun som har vuxit sedan 1970",
     "paras": [
       "Ekerö kulturmiljöprogram från 2015 beskriver hur kommunen har fördubblat sin befolkning sedan 1970 och hur framför allt villabebyggelsen har ökat. Kring östra Ekerö och södra Färingsö dominerar småhus från 1900-talets andra hälft, och under 1990- och 2000-talet tillkom inte mindre än 2 475 villor i kommunen, framför allt i anslutning till befintliga villaområden och byar.",
       "På östra Ekerö nämner programmet Väsby med enhetlig bebyggelse från tidigt 1970-tal och Närlunda, som domineras av villor från 1960-talet. I ett hus från vilket av decennierna som helst kan golvvärmen vara original eller ha kommit till vid en senare ombyggnad. Vi frågar efter värmesystemet redan vid platsbesöket, eftersom det påverkar både tidplanen och valet av ytbehandling.",
     ],
     "aside": {"title": "Ur kulturmiljöprogrammet", "items": [
       "Befolkningen fördubblad sedan 1970", "2 475 villor under 1990- och 2000-talet", "Väsby: tidigt 1970-tal", "Närlunda: 1960-talet"]}},
    {"id": "temperatur-ekero", "h2": "Rätt yttemperatur när lack eller olja stryks",
     "paras": [
       "Golvbranschens riktlinjer för lackering, LACK 22, säger att yttemperaturen på ett golv med golvvärme kontrolleras med en termometer som läggs på golvet. Under behandlingen ska den vara 20 ± 2 grader, och golvets yta ska vara kallare än rumsluften, annars torkar lacken för fort. Efter behandlingen kan temperaturen höjas successivt under 2–3 dagar till normal drift, men inte över 27 grader på golvytan.",
       "Riktlinjerna för oljebehandling, OLJA 22, har samma ordning: 20 ± 2 grader under ytbehandlingen, och därefter en successiv höjning under 2–3 dygn till högst 27 grader. Riktlinjerna påpekar också att man ska vara aktsam vid temperaturer under 15 och över 25 grader och vid starkt solljus, eftersom det påverkar torktiderna.",
       "För dig betyder det att golvvärmen behöver vara så låg att golvets yta håller kring 20 grader när vi stryker, och att den sedan höjs i steg. Har huset flera värmekretsar går vi igenom vilka rum som berörs.",
     ],
     "aside": {"title": "Golvvärme och ytbehandling", "items": [
       "20 ± 2 °C under behandlingen", "Golvet kallare än rumsluften", "Höjs under 2–3 dagar", "Högst 27 °C på golvytan"]}},
    {"id": "vinterluften-ekero", "h2": "Torr vinterluft och springor",
     "paras": [
       "Golvbranschens handbok Trägolv på golvvärme förklarar att golvvärme normalt ger en något lägre luftfuktighet närmast golvet. I ett rum med 30 procents relativ fuktighet vid 20 grader blir fuktigheten ungefär 20 procent vid 27 grader, om luftens fuktinnehåll inte ändras. Vintertid, när inomhusluften är torr, uppstår ofta springor mellan brädorna och skålning, och handboken skriver att det kan vara nödvändigt att använda luftfuktare för att hålla 30–60 procent.",
       "Gränsen på 27 grader gäller enligt handboken även under mattor och möbler, där det normalt blir varmare än på omgivande ytor. En stor matta eller en bokhylla med platt botten räknas som övertäckning om den inte ventileras.",
       "Slipningens riktlinjer, SLIP 22, säger dessutom att golvet inte ska ytbehandlas när luftfuktigheten inomhus ligger utanför 30–60 procent. I ett hus med golvvärme lägger vi därför helst ytbehandlingen utanför den kallaste och torraste delen av året, eller mäter klimatet noga innan vi börjar.",
     ],
     "aside": None},
    {"id": "traslag-ekero", "h2": "Träslag som rör sig mer",
     "paras": [
       "Alla trägolv rör sig inte lika mycket. Handboken anger att lamellparkett av bok och kanadensisk lönn sväller och krymper mer än andra träslag och att de i Skandinavien anses olämpliga tillsammans med golvvärme. Massiva trägolv är mer benägna att röra sig än lamellgolv, och man får räkna med en krympning på ungefär en procent av brädans bredd under normala förhållanden.",
       "Ligger det ett sådant golv på golvvärme i ditt hus kan springorna ha med klimatet att göra snarare än med slitaget, och då är klimatet det första att se över. Vi mäter fuktkvoten och tittar på springorna innan vi föreslår något.",
       "Ska golvet bytas, till exempel i en sommarvilla som har blivit helårshus, finns mer under " + _L.format("golvlaggare-ekero.html", "golvläggare på Ekerö") + ". En översikt över golv och ytbehandlingar finns på sidan om " + _HUB + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipningen till på Ekerö",
  "steps": [
    ("Platsbesök", "Vi tittar på golvet, frågar efter golvvärmen och mäter fuktkvot och luftfuktighet."),
    ("Skriftligt kostnadsförslag", "Slipning, ytbehandling och antal lager står som egna poster."),
    ("Värmen ner", "Golvvärmen sänks så att golvets yta håller 20 ± 2 grader under behandlingen."),
    ("Slipning", "Golvet slipas i tre steg, och kanterna slipas för sig."),
    ("Ytbehandling", "Lack eller olja stryks med termometer på golvet och torktid emellan."),
    ("Värmen upp", "Temperaturen höjs i steg under två till tre dagar, till högst 27 grader."),
  ],
  "rot_h2": "ROT-avdrag i villa och fritidshus",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete i småhus, och till småhus räknas även fritidshus. Det är arbetad tid på plats som ger avdrag, inte material.",
    _ROT_SUM + " Resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Ekerö?",
  "price": [
    "Golvytan, golvets skick, vilken ytbehandling du väljer och hur arbetet behöver delas upp kring golvvärmen. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan trägolvet slipas fast huset på Ekerö har golvvärme?",
     "Ja. Det som skiljer är ytbehandlingen: golvets yta ska hålla 20 ± 2 grader när lack eller olja stryks, och värmen höjs sedan i steg."),
    ("Hur varmt får ett trägolv med golvvärme bli?",
     "Högst 27 grader på golvytan enligt Golvbranschen, och det gäller även under mattor och möbler."),
    ("Varför får golvet springor på vintern när golvvärmen är på?",
     "Golvvärmen sänker luftfuktigheten något närmast golvet, och vinterluften är redan torr. Golvbranschen rekommenderar 30–60 procents luftfuktighet, vid behov med luftfuktare."),
    ("Hur snabbt får golvvärmen sättas på efter lackeringen?",
     "Temperaturen höjs successivt under 2–3 dagar till normal drift, men inte över 27 grader på golvytan."),
    ("Passar bokparkett på golvvärme?",
     "Golvbranschen anser att lamellparkett av bok och kanadensisk lönn är olämplig på golvvärme, eftersom de träslagen sväller och krymper mer än andra."),
  ],
  "sources": [
    _EKERO_KMP, _GBR_GV, _GBR_GVW, _GBR_LACK, _GBR_OLJA, _GBR_SLIP, _SKV, _SKV2,
  ],
  "cta": ("Ligger trägolvet på Ekerö på golvvärme?", "Boka ett gratis platsbesök, så går vi igenom golvet, värmen och klimatet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat och lackat ekgolv i ett ljust vardagsrum i en villa från 1970-talet med fönster mot trädgården",
     "bright empty living room in a 1970s Swedish single-storey villa, a freshly sanded and satin lacquered oak plank floor, large windows facing a green garden with birch trees, white walls, a thin room thermostat on the wall, no furniture, no people, no text"),
    ("Termometer liggande på ett nyslipat trägolv bredvid en golvslipmaskin",
     "close-up of a small digital surface thermometer lying on a freshly sanded bare oak floor, a professional floor sanding machine slightly out of focus in the background, soft daylight, no readable text, no people"),
  ],
},

# ------------------------------------------------------------------ FARSTA
"golvslipning-farsta.html": {
  "kind": "district", "service": "golvslipning", "ort": "Farsta", "svc_label": "Golvslipning",
  "title": "Golvslipning i Farsta – så ska det slipade golvet se ut",
  "description": "Golvslipning i Farsta: vad du kan kräva av ett färdigslipat trägolv i lägenheten eller radhuset – slipränder, kanter, hörn, vågor och blanka partier.",
  "h1": "Golvslipning i Farsta",
  "lead": "När slipmaskinen har gått och lacken eller oljan har torkat ska golvet hålla en viss nivå. Golvbranschen har skrivit ner hur ett trägolv bedöms och vilka fel som ska åtgärdas. Geal Entreprenad AB slipar och ytbehandlar trägolv i lägenheter och radhus i Farsta, och vi går igenom golvet tillsammans med dig efter samma grunder när jobbet är klart.",
  "card": "Slipa trägolvet och gå igenom resultatet.",
  "sections": [
    {"id": "tunnelbanestaden-farsta", "anchor": "Stadsdelen",
     "h2": "Tunnelbanestaden från 1961",
     "paras": [
       "Farsta stod klart 1961, ett år efter Högdalen, skriver Stockholms stad i vägledningen Varsam utveckling av småhus- och villaområden. Farsta planerades i stor utsträckning med bilen som utgångspunkt, med stora parkeringsplatser vid centrum. Gemensamt för tunnelbanestäderna blev att de högre husen placerades närmast centrum och tunnelbanestationen, med grupper av rad- och kedjehus längst ut. I vägledningens tabell räknas Farsta som kulturhistoriskt värdefull miljö.",
       "Det mesta av stadsdelen är lägenheter. Enligt stadens områdesfakta fanns 7 810 bostäder i Farsta 2025, varav 545 i småhus och 3 415 bostadsrätter. I Farsta strand var 328 av 2 861 bostäder småhus. Ett golv som slipas i Farsta ligger alltså ofta i en lägenhet.",
     ],
     "aside": {"title": "Farsta, bostäder 2025", "items": [
       "7 810 bostäder", "3 415 bostadsrätter", "3 046 i allmännyttan", "545 i småhus"]}},
    {"id": "bedomning-farsta", "h2": "Hur ett trägolv bedöms",
     "paras": [
       "Golvbranschens bedömningsgrunder för skönhetsfel i massiva trägolv har en huvudregel: ett mindre skönhetsfel ska vara direkt synligt vid en opartisk bedömning som görs med normal noggrannhet. Besiktningen görs i allmänhet stående. Fel som bara framträder i visst ljus, från vissa delar av rummet eller först efter att någon har pekat på dem räknas inte som fel.",
       "Klimatet spelar in. För fel som hänger ihop med fukt ska rummet vid bedömningen hålla 18–25 grader och 30–60 procents relativ fuktighet. Ligger klimatet utanför det gäller inte toleranserna. Springor mellan brädorna tillåts motsvara en procent av brädans bredd vid den lägsta godtagbara luftfuktigheten, 30 procent, och kupning eller skålning får vara högst en procent av bredden.",
     ],
     "aside": {"title": "Vid bedömningen", "items": [
       "Stående, med normal noggrannhet", "18–25 °C i rummet", "30–60 % relativ fuktighet", "Fel ska synas utan påpekande"]}},
    {"id": "slipfel-farsta", "h2": "Fel som hör till slipningen",
     "paras": [
       "Bedömningsgrunderna har en egen grupp för fel i golvslipningsarbeten. Slipränder efter annat än slutpappret, ringar efter kantslipningen, otillräcklig planslipning, valsslag och ondulering åtgärdas genom omslipning och ny behandling. Hörn som inte har slipats eller skrapats punktslipas och bättras med olja på ett naturoljat golv, medan ett lackat golv slipas om och behandlas på nytt.",
       "Riktlinjerna för slipning, SLIP 22, beskriver hur felen undviks. Ondulering, alltså en vågig yta, kan komma av svikt i golvet men också av fel på maskinen, och det är golvsliparens ansvar att maskinen är rätt inställd och servad. Finslipningen görs i träets längdriktning, och kanterna får samma struktur som resten av golvet.",
       "Ett nyslipat golv visar därför hur noga varje steg gjordes. Vi går över golvet i rummets eget ljus innan ytbehandlingen och åtgärdar det vi ser då, när det fortfarande är enkelt.",
     ],
     "aside": None},
    {"id": "ytbehandling-farsta", "h2": "Ytbehandlingen och det som inte är fel",
     "paras": [
       "Även ytbehandlingen har sina punkter. Överskottsolja som bildar blanka partier torrslipas med hårda rondeller, oljas om och poleras. För lite lack eller olja åtgärdas med mellanslipning och lackering av hela ytan eller med mer olja, och en ojämn lackyta med vallar eller knottror mellanslipas och lackeras om. Flagnar lacken krävs omslipning.",
       "Bedömningsgrunderna påpekar också att golv som utsätts för punktslitage bör skyddas, till exempel med ett underlägg under en kontorsstol med hjul. I en lägenhet med arbetsplats hemma är det värt att tänka på direkt när golvet är nytt.",
       "En sak räknas inte som fel. Färgförändring i trä på grund av UV-ljus, och den rödfärgning som ett furugolv får med tiden, åtgärdas inte enligt bedömningsgrunderna.",
       "Ska golvet i stället bytas, till exempel i hallen eller köket, finns mer under " + _L.format("golvlaggare-farsta.html", "golvläggare i Farsta") + ". Golv och ytbehandlingar beskrivs också på sidan om " + _HUB + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipningen till i Farsta",
  "steps": [
    ("Platsbesök", "Vi tittar på golvet och kontrollerar att det går att slipa och inte sviktar."),
    ("Skriftligt kostnadsförslag", "Slipning, lagning och ytbehandling redovisas var för sig."),
    ("Slipning", "Grov-, mellan- och finslipning, med kantslip längs väggarna."),
    ("Kontroll före ytbehandling", "Vi går över golvet i rummets ljus och åtgärdar ränder och hörn."),
    ("Ytbehandling", "Lack eller olja stryks i rätt mängd med torktid mellan lagren."),
    ("Genomgång", "Vi går igenom golvet stående med dig och lämnar skötselråd."),
  ],
  "rot_h2": "ROT-avdrag i bostadsrätt och radhus",
  "rot": [
    "Golvslipning är rotarbete enligt Skatteverket. I en bostadsrätt krävs att du har underhållsansvaret för golvet enligt stadgarna och att arbetet görs i bostaden, innanför väggar, tak och golv.",
    _ROT_SUM + " Lack, olja och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Farsta?",
  "price": [
    "Golvytan, golvets skick, hur mycket som behöver lagas och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur ska ett nyslipat golv i Farsta se ut när jobbet är klart?",
     "Det ska inte ha slipränder efter annat än slutpappret, inga ringar efter kantslipen, slipade hörn och en jämn yta utan vågor. Golvet bedöms stående och med normal noggrannhet."),
    ("Räknas ett fel som bara syns i motljus?",
     "Enligt Golvbranschens bedömningsgrunder räknas fel som bara framträder i visst ljus eller efter påpekande inte som felaktigheter."),
    ("Vad är ondulering?",
     "En vågig yta efter slipningen. Den kan bero på svikt i golvet eller på en felinställd maskin och åtgärdas med omslipning och ny behandling."),
    ("Vår furu har blivit rödaktig – är det ett slipfel?",
     "Nej. Golvbranschens bedömningsgrunder anger att färgförändring av UV-ljus och rödfärgning av furugolv inte åtgärdas."),
    ("Vilket inomhusklimat ska gälla när golvet bedöms?",
     "18–25 grader och 30–60 procents relativ fuktighet. Utanför det gäller inte toleranserna för fuktrelaterade fel."),
  ],
  "sources": [
    _VARSAM,
    ("Stockholms stad – Områdesfakta 2025: Farsta (pdf)", _OF + "soderort/farsta/farsta.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Farsta strand (pdf)", _OF + "soderort/farsta/farsta-strand.pdf"),
    _GBR_BED, _GBR_SLIP, _SKV, _SKV2,
  ],
  "cta": ("Ska trägolvet i Farsta slipas?", "Boka ett gratis platsbesök, så går vi igenom golvet och vad du kan förvänta dig av resultatet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat och lackat trägolv i ett tomt rum i en lägenhet från 1960-talet med stort fönster",
     "empty living room in a 1960s Stockholm suburban apartment, a freshly sanded and satin lacquered oak strip floor, a wide window with a view of pine trees and red brick buildings, white walls, simple radiator under the window, no furniture, no people, no text"),
    ("Släpljus över ett nyslipat ekgolv som visar en jämn yta utan slipränder",
     "low-angle raking daylight across a freshly sanded bare oak floor showing an even smooth surface without sanding marks, a corner and white skirting board in view, no people, no text"),
  ],
},

# ------------------------------------------------------------------ HANINGE
"golvslipning-haninge.html": {
  "kind": "district", "service": "golvslipning", "ort": "Haninge", "svc_label": "Golvslipning",
  "title": "Golvslipning i Haninge – laga golvet innan det slipas",
  "description": "Golvslipning i Haninge: laga skador före slipningen – kantskador, kvisthål, nivåskillnader, springor, kupade brädor och lösa partier i villans trägolv.",
  "h1": "Golvslipning i Haninge",
  "lead": "Ett trägolv som har legat i många år kan ha märken som en slipning inte tar bort: en spjälkad kant, ett öppet kvisthål, en bräda som står högre än grannen. Sådant lagas innan maskinen startar. Geal Entreprenad AB slipar och ytbehandlar trägolv i Haninge och går igenom golvet bräda för bräda innan vi föreslår vad som ska göras.",
  "card": "Laga och slipa trägolvet i villan.",
  "sections": [
    {"id": "folkhemmet-haninge", "anchor": "Villorna",
     "h2": "Villorna från folkhemmet och rekordåren",
     "paras": [
       "Haninges karaktärsmiljöer beskriver folkhemsbygget 1940–1960-tal som områden med små enhetliga villor, kedjehus eller radhus samlade i grupphusbebyggelse. 1940-talets småhusområden består av enkelt utformade en- eller tvåplansvillor i trä, puts eller fasadtegel, och 1950-talets villa- och kedjehusområden har oftast kombinerade fasadmaterial. Som exempel nämns Handen, Jordbro, Vendelsö, Vendelsömalm och Västerhaninge.",
       "Rekordårens småhus från 1960–1980-tal är enligt samma dokument oftast uppförda som grupphus med enhetlighet inom området, och en- och en halvplansvillor är vanliga. Exempel finns i Jordbro, Brandbergen, Västerhaninge och Handen. Hur golvet i just ditt hus ser ut avgör vi på plats.",
     ],
     "aside": {"title": "Småhus i Haninge", "items": [
       "Folkhemsbygget 1940–1960-tal", "Rekordåren 1960–1980-tal", "Handen, Jordbro, Vendelsö", "Vendelsömalm, Västerhaninge"]}},
    {"id": "skador-haninge", "h2": "Skador som slipningen inte tar bort",
     "paras": [
       "Golvbranschens bedömningsgrunder för massiva trägolv listar lämpliga åtgärder för olika fel. Urspjälkning och kantskador, till exempel efter ett hammarslag, åtgärdas med byte av stav eller bräda, och mindre fel spacklas eller repareras. Öppna kvisthål och kvistsprickor spacklas, och ytan bättras med lack eller olja.",
       "Tryckmärken, repor och skador i ytan kan vid mycket små fel punktförbättras, men i svårare fall byts brädan. Därför går vi igenom märkena innan vi slipar, och en bräda med en svår skada byts före slipningen.",
       "Är en del av slitskiktet lös, till exempel i ett lamellgolv, ska den enligt riktlinjerna för slipning, SLIP 22, limmas fast före slipningen.",
       "Även listerna hör till jobbet. Bedömningsgrunderna anger att hammarslag och andra skador på lister spacklas och ytbehandlas eller att listen byts. En springa mellan golv och sockel bedöms efter tillverkarens krav på expansionsutrymme och kan åtgärdas med en ny sockel eller en kvartstav. Vi går därför igenom listerna samtidigt som brädorna.",
     ],
     "aside": {"title": "Lagas före slipning", "items": [
       "Spjälkade kanter", "Öppna kvisthål", "Djupa tryckmärken", "Lösa partier av slitskiktet"]}},
    {"id": "nivaer-haninge", "h2": "Nivåskillnader, springor och kupade brädor",
     "paras": [
       "Ett fogsprång är när två brädor ligger på olika höjd. Bedömningsgrunderna anger att enstaka fogsprång åtgärdas med byte av bräda, eller på ett oljat golv med punktslipning och omoljning, och att ett bestående fogsprång får vara högst ±0,3 millimeter.",
       "Springor, buktiga brädor och missljud hanteras annorlunda. För dem säger bedömningsgrunderna att orsaken först ska utredas och att åtgärden beror på resultatet. En bräda som har kupat sig, alltså buktat uppåt, eller skålat sig neråt får vara högst en procent av brädans bredd. Golvbranschens handbok Trägolv på golvvärme beskriver att trägolv får springor och skålning när inomhusluften är torr på vintern och kan kupa sig när luften är fuktig på sommaren. En buktighet som kommer av klimatet kan alltså komma tillbaka efter en slipning.",
       "Därför mäter vi fuktkvoten i träet och luftfuktigheten i rummet innan vi föreslår slipning. Riktlinjerna säger att golvet inte ska ytbehandlas när fuktkvoten ligger utanför 6–10 procent eller luftfuktigheten utanför 30–60 procent.",
     ],
     "aside": None},
    {"id": "fukt-haninge", "h2": "När golvet har varit blött",
     "paras": [
       "Fuktskador och svikt står också bland de fel där orsaken ska utredas först. SLIP 22 säger att den som misstänker att slitskiktet kan lossna vid eller efter slipning, till exempel när golvet är vattenskadat, bör avråda från en omslipning. Samma sak gäller när slipningen antas bli orimligt dyr.",
       "Sviktar golvet kan slipningen dessutom ge en vågig yta, ondulering. Går svikten inte att åtgärda före slipningen ska du enligt riktlinjerna få veta risken innan arbetet börjar. I ett hus med källare eller souterräng tittar vi gärna på bjälklaget underifrån när det går.",
       "Är golvet så skadat att det är bättre att lägga nytt beskrivs det under " + _L.format("golvlaggare-haninge.html", "golvläggare i Haninge") + ". Fler golvtyper finns på sidan om " + _HUB + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvslipningen till i Haninge",
  "steps": [
    ("Platsbesök", "Vi går över golvet bräda för bräda och mäter fukten i träet och i rummet."),
    ("Skriftligt kostnadsförslag", "Byten av brädor, spackling, slipning och ytbehandling står som egna poster."),
    ("Lagning", "Skadade brädor byts, lösa partier limmas och kvisthål spacklas."),
    ("Slipning", "Golvet slipas i tre steg till en jämn yta, och kanterna slipas för sig."),
    ("Ytbehandling", "Lack, olja eller hårdvaxolja i det antal lager golvet behöver."),
    ("Genomgång", "Vi visar vad som har lagats och lämnar råd om klimat och skötsel."),
  ],
  "rot_h2": "ROT-avdrag för lagning och slipning",
  "rot": [
    "Skatteverket räknar att slipa och byta golv som rotarbete i småhus. Avdraget gäller arbetad tid på plats.",
    _ROT_SUM + " Brädor, spackel, lack och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Haninge?",
  "price": [
    "Golvytan, hur många brädor som behöver bytas eller lagas, om fuktorsaker behöver utredas och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Försvinner ett djupt hammarmärke i golvet när det slipas i Haninge?",
     "Vi bedömer märket före slipningen. Golvbranschen anger byte av bräda vid kantskador och svårare tryckmärken, medan mindre skador kan spacklas."),
    ("Hur stor höjdskillnad får det vara mellan två brädor?",
     "Ett bestående fogsprång får enligt Golvbranschens bedömningsgrunder vara högst ±0,3 millimeter. Större skillnader åtgärdas, till exempel med byte av bräda."),
    ("Kan kupade brädor slipas plana?",
     "Golvbranschen säger att orsaken ska utredas först och att åtgärden beror på resultatet. Beror kupningen på klimatet kan brädorna röra sig igen."),
    ("Ska ett vattenskadat golv slipas om?",
     "Inte om det finns risk att slitskiktet lossnar. Golvbranschens riktlinjer säger att man då bör avråda från omslipning."),
    ("Vad görs med öppna kvisthål innan golvet lackas?",
     "De spacklas, och ytan punktförbättras med lack eller olja, enligt Golvbranschens bedömningsgrunder."),
  ],
  "sources": [
    _HAN_KAR, _GBR_BED, _GBR_SLIP, _GBR_GV, _SKV, _SKV2,
  ],
  "cta": ("Har trägolvet i Haninge skador som behöver lagas?", "Boka ett gratis platsbesök, så går vi igenom brädorna och fukten innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat brädgolv i ett tomt rum i en villa från 1950-talet med fönster mot trädgården",
     "empty bedroom in a 1950s Swedish suburban villa, a freshly sanded pine plank floor with a light satin finish, a window with white frame looking out to a garden with fruit trees, plain light walls, no furniture, no people, no text"),
    ("Ny furubräda insatt bland gamla brädor i ett golv före slipning, med spackel i ett kvisthål",
     "close-up of an old pine plank floor before sanding: one newly inserted pale pine board among older darker boards, a filled knot hole with wood filler nearby, a putty knife lying on the floor, no people, no text"),
  ],
},

# ------------------------------------------------------------------ HUDDINGE
"golvslipning-huddinge.html": {
  "kind": "district", "service": "golvslipning", "ort": "Huddinge", "svc_label": "Golvslipning",
  "title": "Golvslipning i Huddinge – byta från lack till olja",
  "description": "Golvslipning i Huddinge: byt ytbehandling när trägolvet slipas om – från lack till olja eller tvärtom, lut, rester av vax och såpa och träets egen ton.",
  "h1": "Golvslipning i Huddinge",
  "lead": "När ett trägolv slipas ner till rent trä är det ett bra tillfälle att byta yta, till exempel från en blank lack till en matt olja. Alla byten fungerar inte lika bra, och det gamla medlet måste bort helt. Geal Entreprenad AB slipar och ytbehandlar trägolv i Huddinge, och vill du byta yta går vi igenom vad det gamla golvet har fått tidigare och vad det tål.",
  "card": "Slipa golvet och byt ytbehandling.",
  "sections": [
    {"id": "egnahem-huddinge", "anchor": "Egnahemmen",
     "h2": "Egnahem och villastäder längs järnvägen",
     "paras": [
       "Huddinges kulturmiljöprogram berättar att Västra stambanan med en mellanstation i Huddinge öppnade för trafik 1860 och att villabebyggelsen sedan växte fram på höjderna. Hörningsnäs villastad, Huddinge villastad och Stuvsta egnahemsområde kom till, och områdena blev municipalsamhällen: Hörningsnäs 1915, Huddinge, Fullersta, Stuvsta och Segeltorp 1924 och Snättringe 1929. År 1947 slogs Hörningsnäs, Huddinge, Stuvsta och Snättringe samman till Huddinge stormunicipal.",
       "Under 1940-talet fortsatte egnahemsbygget, och kataloghus uppfördes som enkla träbyggnader med flacka sadeltak. Från 1940–50-talen finns många småhus där tegel och puts är tongivande. I hus med så många år bakom sig kan golven ha behandlats på flera sätt, och det påverkar vad som går att lägga på härnäst.",
     ],
     "aside": {"title": "Municipalsamhällen i Huddinge", "items": [
       "Hörningsnäs 1915", "Huddinge, Fullersta, Stuvsta, Segeltorp 1924", "Snättringe 1929", "Stormunicipal 1947"]}},
    {"id": "lack-till-olja-huddinge", "h2": "Från lack till olja",
     "paras": [
       "Golvbranschens riktlinjer för oljebehandling, OLJA 22, säger att olja ska läggas på ett torrt, rent och nyslipat golv. Ytan ska vara fri från fett, såpa, vax och lackrester. Ett lackat golv som ska oljas måste därför slipas tills all lack är borta, även i hörnen och längs listerna, och slipningen avslutas med korn 100 för barrträ och 120 för lövträ.",
       "Fuktkvoten får inte överstiga 12 procent i barrträ och 8 procent i lövträ, och rummet bör hålla normal rumstemperatur och 30–60 procents luftfuktighet. I riktlinjerna för lutbehandling, LUT 22, står att ofärgad golvolja kan ge träet en bärnstensfärgad nyans som ljusnar något med tiden. Vill du ha ett ljusare eller mörkare golv finns pigmenterad olja.",
       "Ett oljat golv underhålls på ett annat sätt än ett lackat. Hur det går till beskrivs på sidan om " + _L.format("golvslipning-nacka.html", "golvslipning i Nacka") + ".",
     ],
     "aside": {"title": "Före oljning", "items": [
       "All lack bortslipad", "Inga rester av vax eller såpa", "Fuktkvot högst 12 % i barrträ", "Fuktkvot högst 8 % i lövträ"]}},
    {"id": "olja-till-lack-huddinge", "h2": "Från olja eller lut till lack",
     "paras": [
       "Åt andra hållet är det mer begränsat. Riktlinjerna för lackering, LACK 22, skriver att lackering på oljebehandlade golv fungerar för vissa fabrikat och att leverantörernas rekommendationer ska följas. Lackering på lutbehandlade golv avråds helt, och även LUT 22 säger att lack på lut inte rekommenderas.",
       "Har golvet lutats är det alltså såpa, golvolja eller hårdvaxolja som LUT 22 beskriver som slutbehandling. Är det oklart vad golvet har behandlats med gör vi ett prov på en undanskymd yta.",
       "När ny lack väljs finns också en begränsning: LACK 22 anger att formaldehydavgivande syrahärdande golvlack är förbjuden att använda. Riktlinjerna avser vattendispergerade lacker, och olika lacker och fabrikat ska inte blandas.",
     ],
     "aside": None},
    {"id": "tonen-huddinge", "h2": "Träets egen ton",
     "paras": [
       "Ett golv som legat under lack i många år kan ha en annan färg än du väntar dig när det slipats fram. Golvbranschens bedömningsgrunder för massiva trägolv anger att färgförändring i trä på grund av UV-ljus och den rödfärgning som ett furugolv får inte åtgärdas.",
       "Vill du jämna ut tonen är en pigmenterad olja ett sätt. Golvbranschen säger att den som beställer pigmentering ska visa ett prov på önskad kulör, och att den som utför arbetet bör göra ett prov på golvet innan behandlingen startar.",
       "Är golvet för tunt för att slipas, eller vill du byta från plastmatta till trä, finns mer under " + _L.format("golvlaggare-huddinge.html", "golvläggare i Huddinge") + " och på sidan om " + _HUB + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett byte av ytbehandling till i Huddinge",
  "steps": [
    ("Platsbesök", "Vi tar reda på vad golvet har behandlats med och vilket träslag det är."),
    ("Prov", "Är det oklart gör vi ett prov på en undanskymd yta."),
    ("Skriftligt kostnadsförslag", "Slipning, ny ytbehandling och eventuell pigmentering står som egna poster."),
    ("Slipning", "All gammal yta slipas bort, och slipningen avslutas med rätt korn för träslaget."),
    ("Ny yta", "Olja, hårdvaxolja eller lack läggs i det antal lager som behövs."),
    ("Skötselråd", "Du får råd om hur den nya ytan ska städas och underhållas."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i villan",
  "rot": [
    "Att slipa golv i ett småhus räknas som rotarbete enligt Skatteverket. Det är arbetstiden på plats som ger avdrag, inte olja, lack eller pigment.",
    _ROT_SUM + " Resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Huddinge?",
  "price": [
    "Golvytan, hur mycket gammal yta som ska slipas bort, vilket träslag golvet är av och vilken ny ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi byta från lack till olja på trägolvet i Huddinge?",
     "Ja, om golvet slipas tills all lack är borta. Golvbranschen säger att ytan ska vara fri från lackrester, vax och såpa innan den oljas."),
    ("Går det att lacka ett golv som har oljats?",
     "För vissa fabrikat, enligt Golvbranschen, och då ska leverantörens rekommendationer följas."),
    ("Kan ett lutat och såpat golv lackas?",
     "Golvbranschen avråder från lack på lutbehandlade golv. Riktlinjerna beskriver i stället såpa, golvolja eller hårdvaxolja."),
    ("Varför blir det oljade golvet gulaktigt?",
     "Ofärgad olja kan ge träet en bärnstensfärgad nyans som ljusnar något med tiden. En pigmenterad olja ger en annan ton."),
    ("Får man använda syrahärdande lack på golvet i dag?",
     "Nej, inte formaldehydavgivande syrahärdande golvlack. Golvbranschen anger att den är förbjuden att använda."),
  ],
  "sources": [
    _HUD_KMP2, _GBR_OLJA, _GBR_LACK, _GBR_LUT, _GBR_BED, _SKV, _SKV2,
  ],
  "cta": ("Vill du byta yta på trägolvet i Huddinge?", "Boka ett gratis platsbesök, så tar vi reda på vad golvet har i dag och vad det tål innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyoljat ekgolv med matt yta i ett tomt rum i en egnahemsvilla med fönster mot trädgården",
     "empty room in a 1920s Swedish wooden owner-built villa, a freshly sanded oak plank floor with a matte natural oil finish, white painted window with small panes facing a garden, plain light walls, soft daylight, no furniture, no people, no text"),
    ("Golv där ena halvan har blank gammal lack och andra halvan är nyslipad och oljad",
     "close-up of a wooden floor split in two halves: on one side old glossy yellowed varnish, on the other side freshly sanded wood with a matte oil finish, a floor sanding machine edge visible, no people, no text"),
  ],
},

}
