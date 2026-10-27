# -*- coding: utf-8 -*-
"""Tjänster v2 – ortsidor köksrenovering i Bromma, Nacka, Solna, Täby, Lidingö och Danderyd
(2026-10-25). Schema: se tools/tj_check.py. Bebyggelsefakta är omformulerade från tools/takreno_orter.py
(TRP, kontrollerade mot källorna där). Nya fakta kontrollerade 2026-10-25 mot: Stockholms stad
(bygglov.stockholm: flytta kök, ventilation, bärande konstruktion), Nacka kommun (eldstad, nya PBL-regler),
Solna stad (lägenhetsinnehavare, bärande konstruktion, VA, anmälan, OVK), Täby kommun (avlopp, fett,
fasadändring), Lidingö stad (ändrade regler), Danderyds kommun (avfallskvarn, nya regler, OVK),
Skatteverket (rotarbete i småhus och bostadsrätt) och riksdagen.se (bostadsrättslagen 7 kap. 7 §)."""

L = '<a class="text-link" href="{0}">{1}</a>'
X = '<a class="text-link" href="{0}" rel="noopener">{1}</a>'

S_ROT = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
S_ROTJOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
S_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
         "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
S_PBF = ("Riksdagen – Plan- och byggförordning (2011:338), 6 kap. 1 §",
         "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-byggforordning-2011338_sfs-2011-338/")
S_STH_FLYTT = ("Stockholms stad – Flytta kök eller badrum",
               "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/flytta-kok-eller-badrum/")
S_STH_VENT = ("Stockholms stad – Ventilation i byggnader",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/ventilation/")
S_STH_BAR = ("Stockholms stad – Ändra i bärande konstruktion",
             "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/andra-i-barande-konstruktion/")
S_STH_PLAN = ("Stockholms stad – Ändra planlösningen i en byggnad",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/andra-planlosningen-i-en-byggnad/")

PAGES_TJ = {

# =============================== KÖK BROMMA ===============================
"koksrenovering-bromma.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Bromma", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Bromma – imkanal, självdrag och småstugor",
  "description": "Köksrenovering i Bromma: imkanal och självdrag i trädgårdsstädernas villor, små kök i "
                 "småstugorna, bärande väggar och stadens regler för att flytta köket.",
  "h1": "Köksrenovering i Bromma",
  "lead": "En köksrenovering i Bromma styrs ofta av sådant som inte syns: en imkanal i en gammal skorsten, "
          "en bärande mellanvägg i en trävilla eller ett kök som är litet för att huset är en småstuga. Vi "
          "går igenom huset först, ritar köket efter det och samordnar snickeri, el och VVS. Platsbesöket är "
          "gratis och ROT-avdraget dras direkt på fakturan.",
  "card": "Imkanal, småstugor och trävillor.",
  "sections": [
    {"id": "villorna", "anchor": "Köken i Bromma",
     "h2": "Trädgårdsstad, småstuga eller funkis – tre olika kök",
     "paras": [
       "Brommas villabebyggelse kom i omgångar. Staden köpte Äppelviken och Alvik 1908, och där byggdes stora "
       "villor från 1910-talet. På 1920-talet följde trädgårdsstäderna i bland annat Ålsten, Smedslätten och "
       "Nockeby med hus i ett och ett halvt plan under branta sadeltak. Ett kök i ett hundraårigt hus har "
       "sällan bara en historia, och det är först när skåpen är nere som det syns hur det har byggts om.",
       "Småstugorna är mindre. I Olovslund byggdes de flesta husen 1927–28 av familjerna själva, och i Norra "
       "Ängby restes 1 200 småstugor 1931–38 av fabrikstillverkade element. När ett kök i ett så litet hus "
       "ska bli större handlar det nästan alltid om att låna yta från ett angränsande rum eller om en "
       "tillbyggnad – och då kommer frågan om väggen mellan rummen bär.",
       "Funkisvillorna i Södra Ängby, drygt 500 hus från 1934–39, är ritade med genomtänkta planer där köket "
       "har en bestämd plats. Där brukar det löna sig att behålla läget och lägga arbetet på stomme, "
       "bänkskiva, belysning och ventilation i stället för att flytta runt funktionerna.",
     ],
     "aside": {"title": "Bra att ta reda på före besöket", "items": [
       "Var går imkanalen – i skorstenen eller i en egen kanal?",
       "Finns gamla ritningar på huset?",
       "Ska köket få mer yta från ett annat rum?",
       "Ligger huset i Ängby, Olovslund eller vid Ålstensgatan?"]}},
    {"id": "imkanal",
     "h2": "Imkanalen bestämmer var spisen kan stå",
     "paras": [
       "Stockholms stad beskriver hur självdrag fungerar i äldre hus: en skorsten går genom huset och mynnar "
       "över nocken, och den använda luften sugs ut via skorstenskanalen i kök och badrum. Drivkraften är "
       "skillnaden mellan inne- och utetemperatur, så på sommaren kan draget nästan utebli. Frånluft med "
       "fläkt blev vanligt i hus byggda 1961–1975, och från 1976 är system med både från- och tilluft vanligare.",
       "För köket betyder det att spisen helst står där en imkanal redan finns. Staden påpekar att ett kök "
       "behöver tillräcklig frånluft och att kanalen ska uppfylla kraven för imkanal. Ska samma kanal användas "
       "både som imkanal för köket och frånluft för badrummet måste det sammanlagda måttet räcka, och staden "
       "rekommenderar att man tidigt rådgör med skorstensfejarmästaren om en ny eller ändrad kanal.",
       "Att byta eller installera en fläkt som påverkar ventilationsflödena räknas som en väsentlig ändring, "
       "och då krävs anmälan och startbesked. Det gäller till exempel om en motordriven köksfläkt ska kopplas "
       "till en kanal som är byggd för självdrag. Monteras en fläkt eller kanal på utsidan av huset kan det "
       "dessutom vara en ändring av yttre utseende som kräver bygglov.",
     ],
     "aside": {"title": "Ventilation efter byggår", "items": [
       "Äldre hus: ofta självdrag via skorstenen",
       "1961–1975: vanligen frånluft med fläkt",
       "Från 1976: ofta från- och tilluft, ibland med återvinning",
       "Ändrade flöden: anmälan och startbesked"]}},
    {"id": "vaggen",
     "h2": "Öppna köket mot vardagsrummet i en trävilla",
     "paras": [
       "Önskan om ett öppnare kök är vanlig i trädgårdsstädernas hus, där rummen ofta är små och avgränsade. "
       "Påverkar ändringen husets bärande konstruktion krävs anmälan och startbesked. Staden tipsar om att man "
       "kan logga in med BankID och se husets äldre ritningar i Bygg- och plantjänsten, men varnar också för "
       "att ritningar kan vara ofullständiga och att de som byggde inte alltid följde dem.",
       "Därför tar vi med en konstruktör när en vägg ska bort eller göras om. Konstruktionsritningen ska "
       "enligt staden upprättas av en sakkunnig konstruktör, och en kontrollplan bestäms i samband med "
       "startbeskedet. Beslutet ska komma inom fyra veckor från att anmälan är komplett, med möjlighet för "
       "staden att förlänga en gång med ytterligare fyra veckor – räkna med det i tidplanen.",
       "Att bara flytta köket inom huset kräver inte bygglov, och har ändringen ingen påverkan på de tekniska "
       "egenskapskraven behövs inte heller någon anmälan. Läs mer om vad som gäller för köket i stort under "
       + L.format("koksrenovering.html", "köksrenovering i Stockholm") + ".",
     ],
     "aside": None},
    {"id": "kulturvarde",
     "h2": "Kulturvärden och det som syns utifrån",
     "paras": [
       "Staden skriver att man vid alla ändringar ska ta hänsyn till byggnadens kulturhistoriska värden. "
       + X.format("https://stadsmuseet.stockholm/kunskap-och-samlingar/kulturmiljo/klassificering/", "Stadsmuseets klassificering") +
       " ger en första bild av hur huset bedöms, och i riksintressena för kulturmiljövården – Norra och Södra "
       "Ängby, Ålstensgatan och Olovslund – kan lov krävas även för sådant som annars är lovfritt.",
       "Inne i huset brukar det röra sig om detaljer som snickerier, dörrar och fönsterbänkar som är värda att "
       "spara när köket byts. Ute är det fläkthuvar, nya fönster och dörrar mot trädgården som kan behöva "
       "prövas. Går en ny kanal genom taket samordnar vi genomföringen med taket – se "
       + L.format("taklaggare-bromma.html", "takläggare i Bromma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en köksrenovering i Bromma till",
  "steps": [
    ("Besök och ritningar", "Vi tittar på köket, kanalerna och väggarna och tar fram husets ritningar om de finns."),
    ("Konstruktör och sotare", "Ska en vägg bort eller en ny imkanal till tar vi in konstruktör och stämmer av med sotaren."),
    ("Kostnadsförslag och anmälan", "Du får ett skriftligt förslag, och vid behov lämnas anmälan in innan arbetet startar."),
    ("Rivning och installationer", "Gamla skåp rivs, och el, vatten, avlopp och fläktkanal dras enligt den nya planen."),
    ("Ytskikt och montering", "Väggar och golv görs klara, stommen monteras och bänkskivan mäts in på plats."),
    ("Inkoppling och överlämning", "Vitvaror och belysning ansluts och provas, och du får handlingarna från arbetet."),
  ],
  "rot_h2": "ROT-avdrag för köket i en Brommavilla",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
    "tillsammans med rut. I ett småhus räknar Skatteverket bland annat att montera fast köksinredning och "
    "installera vitvaror i samband med en omfattande renovering, att byta eller måla köksluckor och att "
    "modernisera el och byta uttag som rotarbete. Rengöring av ventilation och imkanaler ger också rotavdrag i småhus.",
    "Skåp, bänkskiva och vitvaror är material och ger inget avdrag. Vi drar avdraget direkt på fakturan och "
    "skriver arbete och material var för sig.",
  ],
  "price_h2": "Vad styr priset på ett kök i Bromma?",
  "price": [
    "Mest avgör om spis och diskbänk kan stå kvar där kanal och avlopp redan finns. En ny imkanal, en vägg som "
    "ska bort med balk och konstruktionsberäkning eller en el som behöver moderniseras lägger till arbete. "
    "Därefter styr val av stomme, bänkskiva och vitvaror. Efter ett gratis besök får du ett skriftligt "
    "kostnadsförslag.",
  ],
  "faq": [
    ("Kan köksfläkten kopplas till skorstenen i en 1920-talsvilla i Bromma?",
     "Det beror på kanalen. Den ska klara kraven för imkanal, och en motordriven fläkt på en kanal byggd för "
     "självdrag ändrar flödena och kräver då anmälan. Stäm av med sotaren innan köket ritas."),
    ("Var hittar jag gamla ritningar på mitt hus i Bromma?",
     "Stockholms stad har äldre ritningar och handlingar i Bygg- och plantjänsten, där du loggar in med BankID. "
     "Ritningarna kan vara ofullständiga, så en konstruktör bör bedöma bärande väggar på plats."),
    ("Hur kan köket i en småstuga i Norra Ängby bli större?",
     "Oftast genom att ta yta från ett rum intill eller genom en tillbyggnad. Berörs bärande delar krävs anmälan, "
     "och i riksintresset kan ändringar som syns utifrån behöva lov."),
    ("Hur lång tid tar stadens besked om vi river väggen till köket?",
     "Stockholms stad ska besluta inom fyra veckor från att anmälan är komplett och kan förlänga en gång med fyra "
     "veckor. Rivningen får börja först efter startbesked."),
    ("Kan samma kanal ta frånluften från både kök och badrum?",
     "Ibland, men staden påpekar att kanalens sammanlagda mått måste räcka för båda. Kontrollera det innan "
     "badrumskanalen används som imkanal."),
  ],
  "sources": [
    S_STH_FLYTT, S_STH_VENT, S_STH_BAR, S_STH_PLAN,
    ("Stockholms stad – Översiktsplan, Riksintressen enligt miljöbalken", "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf"),
    ("Stockholms stad – Varsam utveckling av småhus- och villaområden", "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf"),
    ("Stockholmskällan / Stadsmuseet – Ängbyplan", "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000106.pdf"),
    ("Stockholmskällan / Stadsmuseet – Alvik (ytterstadsprojektet)", "https://stockholmskallan.stockholm.se/postfiles/SMF/ytterstadsprojektet/Alvik.pdf"),
    ("Stadsmuseet – Kulturhistorisk klassificering", "https://stadsmuseet.stockholm/kunskap-och-samlingar/kulturmiljo/klassificering/"),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Bromma göras om?", "Boka ett gratis besök, så går vi igenom kanaler, väggar och önskemål på plats."),
  "img": [
    ("Renoverat kök med vita luckor och träbänkskiva i en äldre trävilla i Bromma",
     "renovated kitchen in a 1920s Swedish wooden garden-city villa, white shaker cabinets, oak worktop, "
     "small paned windows with white frames facing an apple garden, wide pine floorboards, a chimney breast with "
     "the cooker hood connected to it, calm daylight, Bromma Stockholm"),
    ("Kök med matplats och ugn i högskåp",
     "kitchen under renovation in an old Swedish wooden house, cabinets removed, a wall partly opened with a new "
     "laminated timber beam above the opening, a new galvanized ventilation duct leading to a brick chimney, "
     "protective paper on the floor, tools neatly stacked, daylight"),
  ],
},

# =============================== KÖK NACKA ===============================
"koksrenovering-nacka.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Nacka", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Nacka – radhus i Älta och vedspis i villan",
  "description": "Köksrenovering i Nacka: kök i radhusen i Älta, vedspis eller kamin i sekelskiftesvillan "
                 "med anmälan, ventilation efter byggår och ROT-avdrag.",
  "h1": "Köksrenovering i Nacka",
  "lead": "En köksrenovering i Nacka kan gälla ett radhuskök från slutet av 1960-talet i Älta eller ett kök i en "
          "sekelskiftesvilla i Saltsjöbaden där någon vill ha en vedspis igen. Det är två helt olika jobb. Vi "
          "börjar med huset, tar hand om rivning, snickeri och ytskikt och samordnar el och VVS – med gratis "
          "platsbesök och ROT-avdraget direkt på fakturan.",
  "card": "Radhuskök, sekelskiftesvillor och vedspis.",
  "sections": [
    {"id": "nackahus", "anchor": "Köken i Nacka",
     "h2": "Villastäder vid banan och radhus från 60-talet",
     "paras": [
       "Nackas villabebyggelse har två rötter. Längs Saltsjöbanan växte villasamhällen fram från 1890-talet: "
       "Saltsjöbaden anlades som bad- och villastad, Neglinge byggdes i huvudsak 1895–1910, Storängen grundades "
       "1904 och Saltsjö-Duvnäs 1907. Vid farleden i Boo byggdes sommarvillor från 1860-talet och framåt, och "
       "i Sommarbo, som styckades för fritidshus från 1930-talet, bor allt fler året runt.",
       "Den andra roten är efterkrigstidens småhus. I Älta stod det första radhusområdet, med 25 radhus söder "
       "om Erstaviksvägen, klart 1968–1969, och fler områden följde snabbt. Ett kök i ett sådant radhus har "
       "sin plats bestämd av längans gemensamma stammar och ventilation, och det påverkar vad som går att "
       "flytta.",
       "I en sekelskiftesvilla är förutsättningarna andra. Rummen är fler och större, men el och rör har ofta "
       "kompletterats i flera omgångar, och skorstenen kan rymma både rökkanaler och ventilationskanaler. Vad "
       "den rymmer i just ditt hus är bland det första vi tar reda på.",
     ],
     "aside": {"title": "Vilket hus gäller det?", "items": [
       "Radhus eller kedjehus från 1960–70-talen",
       "Villa längs Saltsjöbanan från 1890–1930",
       "Före detta sommarvilla i Boo",
       "Nyare villa i ett planlagt område"]}},
    {"id": "radhuskok",
     "h2": "Radhusköket: stammar och frånluft sätter ramarna",
     "paras": [
       "I hus byggda mellan 1961 och 1975 var frånluftsventilation vanlig, med fläktar som drar ut luften "
       "via don i kök, badrum och toalett. Uteluften kommer in genom don i ytterväggarna. I ett sådant hus är "
       "köksfläkten en del av ett system, och att ansluta en starkare motordriven fläkt kan rubba balansen "
       "för hela huset. Installation eller väsentlig ändring av ventilation kräver anmälan enligt plan- och "
       "byggförordningen.",
       "Diskbänken ligger nära avloppsstammen, och att flytta den till en köksö betyder nya ledningar i "
       "bjälklag eller platta. En installation eller väsentlig ändring av anläggningen för vatten eller "
       "avlopp i byggnaden är också anmälningspliktig. Ofta är det bättre att behålla diskbänkens läge och i "
       "stället göra om bänkytor, förvaring och belysning.",
       "Bor du i en radhusförening där köken är lika i hela längan är det klokt att höra med grannarna. "
       "Har någon redan bytt kök vet de var stammarna går och vad föreningen har sagt om ventilationen.",
     ],
     "aside": {"title": "Kräver anmälan och startbesked", "items": [
       "Ny eller väsentligt ändrad ventilation",
       "Ny eller väsentligt ändrad VA-installation",
       "Ny eller ändrad eldstad eller rökkanal",
       "Väsentlig påverkan på bärande delar"]}},
    {"id": "vedspis",
     "h2": "Vedspis eller kamin i köket i en äldre villa",
     "paras": [
       "Nacka kommun skriver att den som installerar eller väsentligt ändrar en eldstad ska göra en anmälan, "
       "och kommunen räknar uttryckligen upp kamin, öppen spis, kakelugn och vedspis. Även en tyngre eldstad "
       "eller ett byte av bränsleslag kan vara en väsentlig ändring. En skorsten som byggs utanpå fasaden kan "
       "dessutom kräva bygglov om huset ligger i en kulturmiljö.",
       "Kommunen har automatiserat besluten om eldstäder: en robot granskar anmälan och skickar beslut inom "
       "fem minuter. När installationen är klar ska den besiktigas av en sotare, och eldstaden får inte "
       "användas förrän kommunen gett slutbesked. Planera därför in sotarbesiktningen innan köket ska tas i bruk.",
       "För köksrenoveringen betyder en vedspis mer än själva spisen: golvet ska bära vikten, avstånd till "
       "skåp och bänkar ska hållas och rökkanalen ska vara i skick. Ska skorstenen lagas eller muras om "
       "finns mer under " + L.format("skorstensrenovering.html", "skorstensrenovering") + ".",
     ],
     "aside": None},
    {"id": "kulturmiljo",
     "h2": "Kulturmiljöerna och det som syns utåt",
     "paras": [
       "Nacka kommun påpekar att lättnaderna i de nya PBL-reglerna inte gäller fastigheter i särskilt "
       "värdefulla områden enligt 8 kap. 13 § PBL. Där krävs bygglov för alla fasadändringar – till exempel ett "
       "nytt köksfönster, en dörr mot altanen eller ett nytt galler för frånluften. Kommunens webbkarta visar "
       "kulturmiljöerna, men kommunen skriver själv att lagret uppdateras och inte är helt korrekt överallt.",
       "Saltsjöbaden är riksintresse för kulturmiljövården. Är du osäker rekommenderar kommunen att du "
       "kontaktar Stadsbyggnadsservice tidigt och pratar med grannarna innan arbetet börjar. Se också "
       + L.format("koksrenovering.html", "köksrenovering i Stockholm") + " för planering och val av nivå.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en köksrenovering i Nacka till",
  "steps": [
    ("Platsbesök", "Vi går igenom kök, stammar, ventilation och skorsten och hör vad du vill förändra."),
    ("Kontroll av läget", "Vi tittar i kommunens webbkarta om huset ligger i en kulturmiljö och vad som kan kräva lov."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med rivning, snickeri, el, VVS och eventuell eldstad var för sig."),
    ("Anmälan vid behov", "Ändras ventilation, VA eller eldstad lämnas anmälan in innan arbetet startar."),
    ("Rivning och bygge", "Gamla skåp rivs, installationerna dras och golv, väggar och stomme monteras."),
    ("Besiktning och slutbesked", "Vitvaror ansluts, sotaren besiktar en ny eldstad och du får handlingarna."),
  ],
  "rot_h2": "ROT-avdrag för köket i Nacka",
  "rot": [
    "Du får 30 procent av arbetskostnaden i avdrag, högst 50 000 kronor per person och år, och rot och rut får "
    "tillsammans vara högst 75 000 kronor. Skatteverket godkänner i småhus bland annat att installera och "
    "reparera braskaminer, att mura och reparera skorstenar, öppna spisar och kakelugnar och att installera och "
    "komplettera elcentraler. Att kontrollera eldstäder och skorstenar ger däremot inget rotavdrag.",
    "Material som skåp, bänkskiva, spis och vitvaror ger inget avdrag. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Nacka?",
  "price": [
    "I radhuset är det oftast frågan om diskbänk och fläkt kan stå kvar. I villan tillkommer ibland en eldstad, "
    "en skorsten som behöver åtgärdas eller en el som behöver kompletteras. Storlek, stomme, bänkskiva och "
    "vitvaror styr resten. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Behöver vi anmäla en ny vedspis i köket till Nacka kommun?",
     "Ja. Kommunen kräver anmälan när en eldstad installeras eller ändras väsentligt, och den får användas först "
     "efter sotarens besiktning och kommunens slutbesked."),
    ("Hur snabbt kommer Nacka kommuns beslut om en eldstad?",
     "Kommunen har automatiserat besluten om eldstäder. En robot granskar anmälan och skickar beslut inom fem minuter."),
    ("Kan vi sätta en starkare köksfläkt i vårt radhus från 1960-talet i Älta?",
     "Det beror på husets ventilation. I hus från 1961–1975 är frånluft med fläkt vanlig, och en ny motordriven fläkt "
     "som ändrar flödena kan kräva anmälan. Vi kontrollerar systemet först."),
    ("Krävs bygglov för ett nytt köksfönster i Saltsjöbaden?",
     "Ligger huset i ett särskilt värdefullt område krävs bygglov för alla fasadändringar enligt kommunen. Utanför "
     "sådana områden är fasadändringar på en- och tvåbostadshus normalt lovfria."),
    ("Ger det rotavdrag att få skorstenen kontrollerad inför köksrenoveringen?",
     "Nej, kontroll av eldstäder och skorstenar räknas inte som rotarbete. Att mura och reparera skorstenen gör det."),
  ],
  "sources": [
    ("Nacka kommun – Eldstad eller rökkanal", "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/jag-vill-gora-ansokan-eller-anmalan/bygga-eldstad-eller-rokkanal/"),
    ("Nacka kommun – Nya PBL-regler ger mer frihet och större ansvar för Nackas fastighetsägare", "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/nyheter-om-nya-lagandringen/2025/10/nya-pbl-regler-ger-mer-frihet-och-storre-ansvar-for-nackas-fastighetsagare/"),
    ("Nacka kommun – Kulturmiljöprogram: Villasamhällen vid järnvägen", "https://www.nacka.se/499626/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-jarnvagen.pdf"),
    ("Nacka kommun – Kulturmiljöprogram: Sommarnöjen vid farleden", "https://www.nacka.se/499628/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-sommarnojen.pdf"),
    ("Nacka kommun – Kulturpromenad i Älta", "https://www.nacka.se/49b6e2/globalassets/uppleva-gora/bilder/kultur/kulturhistoria/kulturpromenader/vandring-alta.pdf"),
    S_STH_VENT, S_PBF, S_ROT, S_ROTJOB,
  ],
  "cta": ("Vill du göra om köket i Nacka?", "Boka ett gratis platsbesök, så tittar vi på kök, ventilation och skorsten."),
  "img": [
    ("Renoverat kök med vedspis och vita skåp i en äldre villa i Nacka",
     "renovated kitchen in an early 1900s Swedish wooden villa, black cast-iron wood-burning kitchen stove set in "
     "a white plastered alcove, white painted cabinets, soapstone worktop, tall windows with a view of pine trees "
     "and a glimpse of a sea inlet, wide wooden floorboards, Saltsjöbaden, daylight"),
    ("Ljust kök i ett radhus från 1960-talet efter renovering i Nacka",
     "renovated compact kitchen in a 1960s Swedish terraced house, light grey flat-front cabinets, white "
     "worktop, sink under a window facing a small front garden, ceiling extract vent above the hob, simple "
     "pendant lamp, linoleum-style floor, daylight, Älta Nacka"),
  ],
},

# =============================== KÖK SOLNA ===============================
"koksrenovering-solna.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Solna", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Solna – bostadsrätt, bärande vägg och fläkt",
  "description": "Köksrenovering i Solna: föreningens godkännande, anmälan för bärande vägg och vatten och "
                 "avlopp, köksfläkt och OVK i flerbostadshus och villor i Råsunda.",
  "h1": "Köksrenovering i Solna",
  "lead": "De flesta som gör om köket i Solna bor i en bostadsrätt. Då är det föreningen som först ska säga ja, "
          "och ibland kommunen. Vi hjälper dig att ta fram en tydlig beskrivning av arbetet, river och bygger "
          "nytt och samordnar el och VVS. Bor du i villa i Råsunda eller Stocksundstorp gäller andra frågor, och "
          "dem går vi också igenom vid ett gratis besök.",
  "card": "Bostadsrätter, fläktar och Råsundas villor.",
  "sections": [
    {"id": "solnabostader", "anchor": "Köken i Solna",
     "h2": "En stad av flerbostadshus – med villor runt kanterna",
     "paras": [
       "Solna är i första hand en stad av flerbostadshus. Råsunda planerades kring 1907 med flerfamiljshus i "
       "kärnan, och jugendhusen längs Råsundavägen byggdes 1910–12. Runt omkring växte villaområden fram på "
       "1920-talet, och i norra Solna har nya stadsradhus byggts i Järvastaden och Nya Ulriksdal.",
       "För köket betyder det två helt olika utgångslägen. I lägenheten styr föreningens stammar, "
       "ventilation och stadgar vad som går att göra. I villan bestämmer du själv men ansvarar också för att "
       "allt blir rätt – och stora delar av Solnas villabebyggelse är utpekad som kulturhistoriskt värdefull, "
       "vilket påverkar ändringar som syns utifrån.",
     ],
     "aside": {"title": "Ta med till första mötet", "items": [
       "Föreningens regler för renovering, om sådana finns",
       "Ritning över lägenheten eller huset",
       "Uppgift om vilken ventilation huset har",
       "Önskemål om att flytta kök eller riva vägg"]}},
    {"id": "foreningen",
     "h2": "Föreningens godkännande kommer först",
     "paras": [
       "Solna stad skriver till lägenhetsinnehavare att den som bor i en bostadsrätt alltid behöver "
       "fastighetsägarens medgivande för byggåtgärder. Att flytta köket kräver föreningens godkännande, och i "
       "vissa fall även en anmälan om ändring av vatten och avlopp. Att riva en vägg kräver också föreningens "
       "godkännande, och är väggen bärande krävs dessutom en anmälan om ändring av bärande konstruktion.",
       "Bakom detta ligger bostadsrättslagen. Enligt 7 kap. 7 § får du inte utan styrelsens tillstånd göra "
       "ingrepp i en bärande konstruktion, installera eller ändra ledningar för avlopp, värme, gas eller vatten "
       "eller ändra ventilationen. Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet "
       "för föreningen.",
       "Ju tydligare underlaget är, desto enklare blir beslutet. Vi beskriver vad som rivs, vad som byggs, "
       "vilka installationer som berörs och vem som utför dem, så att styrelsen kan ta ställning utan att "
       "behöva gissa.",
     ],
     "aside": None},
    {"id": "barande",
     "h2": "Bärande vägg och nya rör – så fungerar anmälan i Solna",
     "paras": [
       "Solna stad räknar avväxling av en bärande vägg och håltagning i ett bärande bjälklag som exempel på "
       "åtgärder som kräver anmälan och startbesked. Till anmälan hör bland annat en översiktlig beskrivning, "
       "ett förslag till kontrollplan, ett utlåtande från konstruktör och konstruktionsritning. Enligt staden "
       "kräver enstaka håltagningar i en bärande lägenhetsvägg inte någon certifierad kontrollansvarig.",
       "Samma sak gäller invändiga ändringar som väsentligt påverkar en anläggning för vatten eller avlopp: "
       "anmälan, och sedan vänta på startbesked. Staden meddelar inom tre veckor om handlingar saknas och ska "
       "handlägga anmälan inom fyra veckor från att den är komplett. Ligger byggnaden i en kulturhistoriskt "
       "utpekad miljö och ändringen påverkar fasaden krävs i stället bygglov.",
     ],
     "aside": {"title": "Handlingar vid anmälan", "items": [
       "Översiktlig beskrivning av projektet",
       "Förslag till kontrollplan",
       "Utlåtande från konstruktör",
       "Konstruktions- och planritning"]}},
    {"id": "flakt-ovk",
     "h2": "Köksfläkten och husets ventilationskontroll",
     "paras": [
       "I ett flerbostadshus är köksfläkten kopplad till husets gemensamma ventilation, och den kontrolleras "
       "regelbundet genom obligatorisk ventilationskontroll, OVK. Enligt Solna stad ska flerbostadshus med "
       "självdrag eller frånluft besiktas vart sjätte år och hus med från- och tilluft vart tredje år. Det är "
       "byggnadens ägare – i bostadsrätt föreningen – som ansvarar för att kontrollen görs och att brister åtgärdas.",
       "En fläkt med egen motor som ansluts till fel typ av system kan alltså bli en anmärkning i nästa "
       "protokoll. Fråga styrelsen vilka fläktar som får anslutas innan du väljer modell. I en villa med "
       "självdrag eller frånluft krävs ingen återkommande OVK, men ändras ventilationen väsentligt gäller "
       "anmälningsplikten ändå.",
       "Villorna i Råsunda villastad, Råsta egnahem och Stocksundstorp ingår i områden som staden pekar ut "
       "som kulturhistoriskt värdefulla. Ett nytt köksfönster eller ett fläktgaller på fasaden kan därför "
       "behöva bygglov. Mer om husen finns hos " + L.format("taklaggare-solna.html", "takläggare i Solna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en köksrenovering i Solna till",
  "steps": [
    ("Besök i bostaden", "Vi går igenom köket, väggarna, stammarna och vilken ventilation huset har."),
    ("Underlag till styrelsen", "Du får en beskrivning av arbetet att lämna till föreningen när du söker tillstånd."),
    ("Kostnadsförslag och anmälan", "Du får ett skriftligt förslag, och vid behov lämnas anmälan in till staden."),
    ("Skydd och rivning", "Trapphus och hiss skyddas, och de gamla skåpen rivs och bärs ut."),
    ("Installationer och montering", "El och VVS dras, väggar och golv görs klara och den nya köksinredningen monteras."),
    ("Kontroll och överlämning", "Allt provas, och du får handlingar att spara och lämna till föreningen."),
  ],
  "rot_h2": "ROT-avdrag för köket i en bostadsrätt i Solna",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
    "tillsammans med rut. I bostadsrätt gäller det arbete innanför lägenhetens tak, väggar och golv som du har "
    "underhållsansvar för enligt föreningens stadgar. Skatteverket godkänner där bland annat att montera fast "
    "köksinredning och installera vitvaror i samband med byggarbetet, att byta köksluckor och att dra elledningar "
    "från proppskåpet ut i bostaden.",
    "Rengöring av ventilation och imkanaler ger däremot inget rotavdrag i bostadsrätt, och att färdigställa en "
    "nyproducerad lägenhet ger aldrig avdrag. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Solna?",
  "price": [
    "Den stora skillnaden är om köket byts på samma plats eller flyttas. En flytt, en bärande vägg som ska bort "
    "eller nya avlopp lägger till anmälan, konstruktör och mer installationsarbete. I flerbostadshus påverkar "
    "också skydd av trapphus och hur materialet kommer upp. Du får ett skriftligt kostnadsförslag efter besöket.",
  ],
  "faq": [
    ("Behöver jag kontrollansvarig för att ta upp en öppning i en bärande vägg i min lägenhet i Solna?",
     "Inte för enstaka håltagningar i en bärande lägenhetsvägg, enligt Solna stad. Däremot krävs anmälan, "
     "kontrollplan och konstruktörens underlag, och föreningen måste godkänna arbetet."),
    ("Hur lång tid tar Solna stad på sig att handlägga en anmälan?",
     "Staden meddelar inom tre veckor om något saknas och ska handlägga anmälan inom fyra veckor från att den är komplett."),
    ("Kan vår nya köksfläkt påverka husets OVK i Råsunda?",
     "Ja, om den ändrar flödena i husets gemensamma ventilation. Föreningen ansvarar för OVK, så fråga styrelsen "
     "vilka fläktar som får anslutas."),
    ("Får föreningen säga nej till att vi flyttar köket?",
     "Styrelsen får vägra bara om åtgärden är till påtaglig skada eller olägenhet för föreningen, enligt "
     "bostadsrättslagen 7 kap. 7 §."),
    ("Ger ett nytt kök i en nybyggd bostadsrätt i Järvastaden rotavdrag?",
     "Inte för att färdigställa en nyproducerad lägenhet. När lägenheten är färdigställd kan senare ombyggnad ge "
     "avdrag för arbetet, om du har underhållsansvaret enligt stadgarna."),
  ],
  "sources": [
    ("Solna stad – För lägenhetsinnehavare", "https://www.solna.se/bygga-bo--miljo/bygga/guide-till-lov-och-anmalan/for-lagenhetsinnehavare"),
    ("Solna stad – Ändra bärande konstruktion", "https://www.solna.se/bygga-bo--miljo/bygga/anmalan/andra-barande-konstruktion"),
    ("Solna stad – Ändra vatten och avlopp", "https://www.solna.se/bygga-bo--miljo/bygga/anmalan/andra-vatten-och-avlopp"),
    ("Solna stad – Anmälan", "https://www.solna.se/bygga-bo--miljo/bygga/anmalan"),
    ("Solna stad – Obligatorisk ventilationskontroll, OVK", "https://www.solna.se/bygga-bo--miljo/bygga/tillsyn/obligatorisk-ventilationskontroll-ovk"),
    ("Solna stad – Bygglovsfria åtgärder", "https://www.solna.se/bygga-bo--miljo/bygga/bygglov/bygglovsfria-atgarder"),
    ("Stockholmskällan / Stadsmuseet – Näckrosen (Stockholms spår)", "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000066.pdf"),
    S_BRL, S_ROT, S_ROTJOB,
  ],
  "cta": ("Planerar du ett nytt kök i Solna?", "Boka ett gratis besök, så får du både kostnadsförslag och underlag till föreningen."),
  "img": [
    ("Renoverat kök i en jugendlägenhet i Solna med högt i tak",
     "renovated kitchen in a 1910s Swedish Art Nouveau apartment with high ceilings and ornate ceiling cornice, "
     "deep green flat-front cabinets, white marble-look worktop, brass tap, tall double window with deep sill, "
     "herringbone oak floor, daylight, Råsunda Solna"),
    ("Lägenhetskök under renovering med nya rör och kartonger med ny inredning i Solna",
     "apartment kitchen in an old Swedish building during renovation, old cabinets removed, bare plastered walls, "
     "new water pipes with shut-off valves and electrical boxes roughed in on the wall where the new kitchen will go, "
     "grey protective board on the floor, stacked flat-packed cabinet boxes, tall window with deep sill, daylight"),
  ],
},

# =============================== KÖK TÄBY ===============================
"koksrenovering-taby.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Täby", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Täby – grupphus, radhus och villor",
  "description": "Köksrenovering i Täby: kök i grupphus och radhus från 1950–70-talen, köksutbyggnad i "
                 "grupphusområden, ventilation efter byggår och fett i avloppet.",
  "h1": "Köksrenovering i Täby",
  "lead": "I Täby gör många om köket i ett grupphus eller radhus från 1950-, 60- eller 70-talet, där hela längan "
          "byggdes på en gång och köken från början var lika. Andra har en äldre villa vid Roslagsbanan. Vi river, "
          "bygger nytt och samordnar el och VVS med behöriga installatörer, och ROT-avdraget drar vi direkt på fakturan.",
  "card": "Grupphus, radhus och villor vid banan.",
  "sections": [
    {"id": "tabyhus", "anchor": "Köken i Täby",
     "h2": "Från stationsvillor till grupphusens likadana kök",
     "paras": [
       "Täbys äldsta villor ligger vid Roslagsbanan. I Roslags-Näsby byggdes ett åttiotal villor 1907–1920, i "
       "Viggbyholm styckades tomter av när hållplatsen öppnade 1903 och i Täby villastad vid kyrkbyn stod omkring "
       "250 villor klara före första världskriget. Näsbypark började som ett område för sommarstugor och hade "
       "redan 1933 över 200 bebyggda tomter.",
       "Efter kriget kom grupphusen. Norskogen i Näsbypark byggdes 1957–59, och i Täby kyrkby uppfördes "
       "radhusområdena Midgård 1972–73 och Miklagård 1975–76. Gribbylund består i dag mest av typhus från 1970- "
       "och 1980-talen. I sådana områden har husen samma planlösning, och köket ligger på samma plats i varje hus.",
       "Det är en fördel när köket ska göras om. Har grannen redan bytt kök finns ofta erfarenhet av var "
       "rören går och vad som ryms, och vi kan planera efter samma förutsättningar i hela längan.",
     ],
     "aside": {"title": "Vanliga frågor i grupphusen", "items": [
       "Kan väggen mot vardagsrummet tas bort?",
       "Räcker fläkt och frånluft för en ny köksfläkt?",
       "Kan köket byggas ut mot trädgården?",
       "Vad säger föreningen eller samfälligheten?"]}},
    {"id": "ventilation",
     "h2": "Byggåret visar vilken ventilation köket har",
     "paras": [
       "Ventilationen följer i stort sett husets ålder. I hus byggda 1961–1975 var frånluft med fläkt vanlig, och "
       "från 1976 blev system med både från- och tilluft, ibland med värmeåtervinning, vanligare. Det innebär att "
       "radhusen i Midgård och Miklagård kan ha olika system trots att de byggdes med bara några års mellanrum. "
       "I de äldre stationsvillorna kan ventilationen fortfarande vara självdrag genom skorstenen.",
       "Köksfläkten ska passa systemet. En fläkt med egen motor som ansluts till ett hus med central frånluft "
       "eller till ett FTX-system kan störa balansen, och en installation eller väsentlig ändring av "
       "ventilationen kräver anmälan och startbesked. Vi tar reda på vilket system huset har innan fläkten väljs.",
       "Ska väggen mellan kök och vardagsrum bort och den bär, krävs också anmälan. I grupphus där alla hus är "
       "byggda lika finns det ibland ritningar som visar konstruktionen, men en konstruktör behöver ändå bedöma "
       "just ditt hus.",
     ],
     "aside": None},
    {"id": "utbyggnad",
     "h2": "Bygga ut köket i ett grupphusområde",
     "paras": [
       "Sedan 1 december 2025 får ett hus byggas till med sammanlagt högst 30 kvadratmeter utan bygglov, om "
       "tillbyggnaden inte går över husets taknock. Tidigare lovfria tillbyggnader räknas in. Närmare tomtgränsen "
       "än 4,5 meter krävs bygglov, om inte de berörda grannarna skriftligen har medgett åtgärden – något som "
       "ofta blir aktuellt i en radhuslänga.",
       "Täby kommun har i Kulturmiljöer i Täby antagit riktlinjer som inte är juridiskt bindande men används i "
       "kommunens bedömningar. För grupphusområden anges att det tidstypiska uttrycket ska hållas samman och att "
       "takformer, takmaterial och takfot bör behållas, även vid tillbyggnader. En köksutbyggnad bör därför få "
       "samma tak och detaljer som resten av längan. Mer om att bygga till finns under "
       + L.format("tillbyggnad.html", "tillbyggnad") + ".",
       "Ändringar på fasaden, som ett större köksfönster eller en ny dörr mot uteplatsen, kräver inte bygglov "
       "på ett en- eller tvåbostadshus enligt kommunen – så länge huset inte är särskilt värdefullt, inte ligger "
       "i ett särskilt värdefullt område och detaljplanen inte har utökad lovplikt.",
     ],
     "aside": {"title": "Lovfri tillbyggnad – i korthet", "items": [
       "Högst 30 m² sammanlagt",
       "Inte över husets taknock",
       "Minst 4,5 m till gräns, annars skriftligt medgivande",
       "Bygglov i särskilt värdefulla miljöer"]}},
    {"id": "fett",
     "h2": "Diskbänken och avloppet i Täby",
     "paras": [
       "Avloppsvattnet från Täby går till Käppala avloppsreningsverk på Lidingö, och kommunen ber hushållen att "
       "hålla fett borta från avloppet eftersom det ger stopp i ledningar och problem i pumpstationer. Torka "
       "ur stekpannor och ugnsformar innan disk, och samla upp matolja i en plastflaska. Kommunen delar ut "
       "fettrattar som skruvas på en PET-flaska via sin avfalls- eller VA-enhet.",
       "När köket ändå byggs om är det läge att tänka på det: plats i diskbänksskåpet för sortering och en "
       "flaska för fett, och ett vattenlås som går att komma åt. Gamla avloppsrör under diskbänken byts ofta "
       "i samma veva. Se " + L.format("koksrenovering.html", "köksrenovering i Stockholm") + " för val av nivå "
       "och planering.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en köksrenovering i Täby till",
  "steps": [
    ("Besök i huset", "Vi går igenom köket, väggen mot vardagsrummet, ventilationen och avloppet."),
    ("Regler och grannar", "Vi kontrollerar om något kräver anmälan eller lov och om grannar behöver medge en utbyggnad."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där arbete och material står var för sig."),
    ("Rivning", "Den gamla köksinredningen rivs och vatten och el kopplas bort."),
    ("Installation och montering", "Rör, el och fläktanslutning dras, och golv, väggar och skåp monteras."),
    ("Inkoppling och avslut", "Vitvaror och belysning kopplas in och provas, och du får skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för köket i Täby",
  "rot": [
    "Du får 30 procent av arbetskostnaden i rotavdrag, högst 50 000 kronor per person och år och högst 75 000 kronor "
    "tillsammans med rut. Enligt Skatteverket räknas i småhus bland annat att sätta kakel och klinker, att måla "
    "eller lacka köksluckor, att tapetsera och att montera fast köksinredning och installera vitvaror i samband "
    "med en omfattande renovering.",
    "Att reparera en diskmaskin är inte rotarbete. Är huset yngre än fem år får arbetet bara återställa det skick "
    "det hade från början. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Täby?",
  "price": [
    "I grupphus och radhus är förutsättningarna ofta kända, och det som skiljer är om väggen mot vardagsrummet "
    "ska bort, om ventilationen behöver anpassas och vilken inredning du väljer. En utbyggnad är ett större "
    "projekt med grund, stomme och tak. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi bygga ut köket i vårt radhus i Täby utan bygglov?",
     "Ofta, om tillbyggnaden blir högst 30 kvadratmeter sammanlagt och inte går över taknocken. Närmare gränsen än "
     "4,5 meter krävs skriftligt medgivande från grannarna, annars bygglov."),
    ("Vilken ventilation har ett radhus från 1970-talet i Täby kyrkby?",
     "Hus från 1961–1975 har oftast frånluft med fläkt, och från 1976 är från- och tilluft vanligare. Vi "
     "kontrollerar systemet innan köksfläkten väljs."),
    ("Bör köksutbyggnaden ha samma tak som resten av grupphuset?",
     "Täby kommuns riktlinjer för grupphusområden säger att takformer, takmaterial och takfot bör behållas även vid "
     "tillbyggnader, så att längan behåller sitt uttryck."),
    ("Var får jag tag på en fettratt i Täby?",
     "Täby kommun delar ut fettrattar till PET-flaskor. Kontakta kommunens avfallsenhet eller VA-enhet."),
    ("Krävs bygglov för ett större köksfönster i Täby?",
     "Inte på ett en- eller tvåbostadshus som inte är särskilt värdefullt, inte ligger i ett värdefullt område och "
     "saknar utökad lovplikt i detaljplanen."),
  ],
  "sources": [
    ("Täby kommun – Vad får spolas ned i avloppet", "https://taby.se/bygga-bo-och-miljo/vatten-och-avlopp-va/avloppsvatten/vad-far-spolas-ned-i-avloppet"),
    ("Täby kommun – Avloppsvatten", "https://taby.se/bygga-bo-och-miljo/vatten-och-avlopp-va/avloppsvatten"),
    ("Täby kommun – Fasadändring", "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/fasadandring"),
    ("Täby kommun – Kulturmiljöer i Täby", "https://taby.se/huvudsajter/kulturmiljoer"),
    ("Täby kommun – Kulturmiljöer i Täby, riktlinjer (pdf)", "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"),
    ("Riksdagen – Plan- och bygglag (2010:900), 9 kap. 10 och 34–35 §§",
     "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/"),
    S_STH_VENT, S_PBF, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Täby bytas?", "Boka ett gratis platsbesök, så går vi igenom köket och möjligheterna i huset."),
  "img": [
    ("Renoverat kök med köksö i ett radhus från 1970-talet i Täby",
     "renovated kitchen in a 1970s Swedish terraced house, opened towards the living room, warm white cabinets "
     "with oak handles, oak worktop, small kitchen island, glass door to a wooden deck and garden with birch trees, "
     "light oak floor, daylight, Täby"),
    ("Diskbänksskåp med sorteringskärl och nytt vattenlås i ett renoverat kök",
     "open under-sink cabinet in a newly renovated Scandinavian kitchen, neat new white plastic drain trap and "
     "shut-off valves, pull-out waste sorting bins, a small plastic bottle with a funnel for used cooking oil, "
     "clean and bright, close-up"),
  ],
},

# =============================== KÖK LIDINGÖ ===============================
"koksrenovering-lidingo.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Lidingö", "svc_label": "Köksrenovering",
  "title": "Köksrenovering på Lidingö – villastäder, souterräng och lov",
  "description": "Köksrenovering på Lidingö: kök i villastädernas äldre hus, souterrängvillor i Brevik, "
                 "radhus i Mölna och utökad lovplikt för fönster och tillbyggnad.",
  "h1": "Köksrenovering på Lidingö",
  "lead": "En köksrenovering på Lidingö kan gälla en villa från villastadens första år, ett souterränghus i "
          "Brevik eller ett radhus i Mölna. Ska köket bara bytas inne är reglerna enkla, men ska det få ett nytt "
          "fönster, en dörr mot trädgården eller byggas ut kan stadens utökade lovplikt avgöra. Vi går igenom huset, "
          "bygger köket och samordnar el och VVS – med gratis platsbesök.",
  "card": "Villastäder, souterräng och radhusbyar.",
  "sections": [
    {"id": "lidingohus", "anchor": "Köken på Lidingö",
     "h2": "Husen på Lidingö har sin egen tidslinje",
     "paras": [
       "Villabebyggelsen tog fart 1906, när AB Lidingö Villastad bildades. I slutet av 1910 fanns 293 villor, och "
       "kärnan i villastaden består i dag av hus från ungefär 1905–1930. Samma år som villastaden startade köptes "
       "Brevik, där det 1910 fanns 75 villor. Under 1940- och 50-talen styckades många stora tomter, och nya "
       "villor byggdes mellan de gamla.",
       "Efterkrigstiden gav radhusen. Mölna radhusby ritades av Nils Tesch 1954 och byggdes 1960–62 med fyrtio "
       "radhuslägenheter i sju längor, och i västra Käppala tillkom närmare hundra radhus och kedjehus 1979. I en "
       "äldre villa har köket ofta flyttats eller byggts om flera gånger, medan radhusens kök från början var "
       "likadana i hela området.",
     ],
     "aside": {"title": "Före besöket", "items": [
       "Ligger fastigheten i stadens blå markering?",
       "Ska fönster, dörrar eller fasad ändras?",
       "Står huset i souterräng?",
       "Ska köket få mer yta?"]}},
    {"id": "souterrang",
     "h2": "Kök i ett souterränghus och på branta tomter",
     "paras": [
       "Ön är kuperad, och flera av villorna i Brevik står i souterräng, med en våning delvis under mark på ena "
       "sidan. Ligger köket på entréplanet och avlopp och elcentral i nedre planet, innebär en ny plats för "
       "diskbänken nya ledningar ner genom bjälklaget – och det avgör i praktiken var köket kan hamna.",
       "Branta tomter med stödmurar och terrasser påverkar också själva bygget. Materialet ska bäras in, och gamla "
       "skåp och rivningsmassor ska ut. Vi planerar det vid besöket, så att arbetet går smidigt och utan skador på "
       "trappor och entré.",
       "En installation eller väsentlig ändring av vatten och avlopp eller ventilation i byggnaden kräver anmälan "
       "och startbesked, och detsamma gäller en ändring som väsentligt påverkar bärande delar. Det gäller oavsett "
       "var på Lidingö huset ligger.",
     ],
     "aside": None},
    {"id": "lovplikt",
     "h2": "Den blå markeringen – när köket påverkar fasaden",
     "paras": [
       "Sedan 1 december 2025 krävs inte bygglov för fasadändringar på en- och tvåbostadshus utanför värdefulla "
       "områden, och tillbyggnader på upp till 30 kvadratmeter kan göras utan bygglov. Men Lidingö stad skriver att "
       "utökad lovplikt gäller för de flesta byggnadsåtgärder inom särskilt kulturhistoriskt värdefulla områden. I "
       "stadens webbkarta visas de som ett blått lager, och där krävs bygglov för till exempel tillbyggnad och "
       "fasadändring.",
       "För köket betyder det att ett nytt fönster över diskbänken, en altandörr eller en köksutbyggnad kan behöva "
       "prövas om fastigheten är blåmarkerad. Är den gulmarkerad kan det finnas värden som behöver bedömas, och då "
       "hänvisar staden till sitt kundcenter. Staden påpekar också att lovfria åtgärder ska utföras varsamt med "
       "hänsyn till byggnadens och områdets karaktär.",
       "Underlaget för de värdefulla områdena finns i kulturmiljöprogrammet, som kommunfullmäktige antog den 16 "
       "december 2024. För Mölna radhusby rekommenderar programmet att de slammade tegelfasaderna och "
       "kopparplåtsdetaljerna bevaras, vilket är bra att känna till innan ett köksfönster byts.",
     ],
     "aside": {"title": "Kan behöva bygglov i blå zon", "items": [
       "Nytt eller större köksfönster",
       "Ny dörr från köket mot trädgården",
       "Köksutbyggnad eller burspråk",
       "Fläktgaller eller kanal på fasaden"]}},
    {"id": "radhuskok",
     "h2": "Radhusköket i Mölna och Käppala",
     "paras": [
       "I en radhuslänga byggd på en gång har köken samma läge, och stammarna går på samma sätt i varje hus. Det gör "
       "planeringen förutsägbar. Husen i västra Käppala från 1979 hör till en tid då ventilation med både från- och "
       "tilluft blev vanligare, och då behöver köksfläkten väljas så att den passar husets system. Ändras "
       "ventilationen väsentligt krävs anmälan.",
       "Ingår huset i en samfällighet eller förening kan det finnas egna regler för ändringar som syns utåt. Vi tar "
       "hänsyn till dem i förslaget. Mer om att planera köket finns under "
       + L.format("koksrenovering.html", "köksrenovering i Stockholm") + ", och om husens tak hos "
       + L.format("taklaggare-lidingo.html", "takläggare på Lidingö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en köksrenovering på Lidingö till",
  "steps": [
    ("Besök på plats", "Vi tittar på köket, installationerna i nedre plan och hur materialet kommer in och ut."),
    ("Kartan och reglerna", "Vi kontrollerar stadens webbkarta och om fönster, dörrar eller utbyggnad kräver lov."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med arbete och material var för sig."),
    ("Rivning och installationer", "Gamla skåp rivs, och rör, el och fläktanslutning dras enligt den nya planen."),
    ("Montering", "Golv och väggar görs klara, stommen monteras och bänkskivan sätts på plats."),
    ("Provning och överlämning", "Vitvaror, blandare och belysning kopplas in och provas, och du får handlingarna."),
  ],
  "rot_h2": "ROT-avdrag för köket på Lidingö",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
    "tillsammans med rut. I villa och radhus räknar Skatteverket bland annat att byta köksluckor och dörrar, att "
    "installera och komplettera elcentraler och att montera fast köksinredning och installera vitvaror i samband "
    "med en omfattande renovering som rotarbete.",
    "Att dra el i trädgården ger inget avdrag, och materialet ingår aldrig. Vi drar avdraget direkt på fakturan "
    "och sköter ansökan hos Skatteverket.",
  ],
  "price_h2": "Vad styr priset på ett kök på Lidingö?",
  "price": [
    "Var rören går och om diskbänken kan stå kvar avgör mycket, särskilt i souterränghus. Ett nytt fönster, en "
    "dörr eller en utbyggnad lägger till både arbete och eventuellt bygglov. Därefter styr inredning och "
    "vitvaror. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur ser jag om mitt hus på Lidingö har utökad lovplikt?",
     "Sök på fastigheten i Lidingö stads webbkarta. Ett blått lager visar utökad lovplikt, och en gul markering "
     "betyder att det kan finnas värden som behöver bedömas."),
    ("Behöver vi bygglov för en altandörr från köket i Brevik?",
     "Inte om huset ligger utanför de värdefulla områdena, eftersom fasadändringar på en- och tvåbostadshus är "
     "lovfria. Ligger fastigheten i den blå markeringen krävs bygglov."),
    ("Kan diskbänken flyttas i ett souterränghus?",
     "Oftast, men avloppet ska ledas ner till nedre planet, vilket kan kräva håltagning i bjälklaget. Ändras "
     "VA-installationen väsentligt krävs anmälan."),
    ("Vad säger kulturmiljöprogrammet om fasaderna i Mölna radhusby?",
     "Programmet rekommenderar att de slammade tegelfasaderna, takens enkupiga lertegel och kopparplåtsdetaljerna "
     "bevaras. Det är bra att veta innan fönster eller dörrar ändras."),
    ("Gäller de nya lovreglerna för en köksutbyggnad på Lidingö?",
     "Ja, sedan 1 december 2025 kan tillbyggnader på upp till 30 kvadratmeter göras utan bygglov – utom där "
     "utökad lovplikt gäller."),
  ],
  "sources": [
    ("Lidingö stad – Ändrade lagar och regler för byggande", "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/"),
    ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet", "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Lidingö villastad (pdf)", "https://share.mediaflow.com/sv/?9OCCB1KE1L"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Breviks villastad (pdf)", "https://share.mediaflow.com/sv/?70CCS1CE0X"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Mölna radhusby (pdf)", "https://share.mediaflow.com/sv/?3ZCCS1LEFX"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Gåshaga, Killinge och Käppala (pdf)", "https://share.mediaflow.com/sv/?P7CCT1JEFN"),
    S_STH_VENT, S_PBF, S_ROT, S_ROTJOB,
  ],
  "cta": ("Funderar du på ett nytt kök på Lidingö?", "Boka ett gratis besök, så går vi igenom huset, reglerna och köket."),
  "img": [
    ("Renoverat kök i en äldre villa på Lidingö med utsikt mot trädgård och vatten",
     "renovated kitchen in an early 1900s Swedish villa on a hill, white panelled cabinets, dark stone worktop, "
     "large window above the sink with a view over pine trees and a distant fjord, wooden floor, pendant lamps, "
     "daylight, Lidingö"),
    ("Ny dörr från köket ut mot en terrass på en kuperad tomt",
     "new glazed wooden door from a renovated kitchen opening onto a small stone terrace on a steep rocky garden "
     "plot with old trees, view from inside the kitchen, white cabinets at the edge of the frame, daylight, Sweden"),
  ],
},

# =============================== KÖK DANDERYD ===============================
"koksrenovering-danderyd.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Danderyd", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Danderyd – villor, kvarnförbud, utbyggnad",
  "description": "Köksrenovering i Danderyd: kök i Djursholms och Stocksunds villor, förbudet mot "
                 "avfallskvarn mot avloppet, köksutbyggnad i kulturmiljö och ventilation.",
  "h1": "Köksrenovering i Danderyd",
  "lead": "Köksrenovering i Danderyd handlar ofta om stora villor från 1890–1930 i Djursholm och Stocksund, eller "
          "om egnahem i Enebyberg. Kommunen har några egna regler som är bra att känna till innan köket ritas, "
          "bland annat att en avfallskvarn inte får kopplas till avloppet. Vi tar hela köket, från rivning till "
          "montering, och samordnar el och VVS. Platsbesöket är gratis.",
  "card": "Villastäder, egnahem och kommunens regler.",
  "sections": [
    {"id": "danderydhus", "anchor": "Köken i Danderyd",
     "h2": "Villastäder från sekelskiftet och egnahem i Enebyberg",
     "paras": [
       "Djursholm grundades 1889 och beskrivs i kommunens översiktsplan som landets första villastad anlagd som "
       "förort. Bebyggelsen speglar framför allt 1890–1930, med stora villor på naturtomter. Stocksund växte fram "
       "parallellt, och sedan 1987 är både Djursholms och Stocksunds villastäder riksintressen för "
       "kulturmiljövården. Enebyberg har en annan karaktär, med bebyggelse från 1700-talet till 1970-talet och "
       "utpekade egnahemsområden.",
       "För köket betyder det två saker. Inne i huset bestämmer du i stort sett själv, men allt som syns "
       "utåt – en utbyggnad, ett nytt fönster eller en fläkthuv – prövas hårdare här än i de flesta kommuner. "
       "Och i en villa som är över hundra år gammal behöver el, avlopp och ventilation ses över innan den nya "
       "inredningen planeras.",
     ],
     "aside": {"title": "Bra att veta före besöket", "items": [
       "Ligger huset i en värdekärna eller ett riksintresse?",
       "Finns det en avfallskvarn i dag?",
       "Har huset självdrag, frånluft eller FTX?",
       "Ska köket byggas ut?"]}},
    {"id": "avfallskvarn",
     "h2": "Ingen avfallskvarn kopplad till avloppet",
     "paras": [
       "Danderyds kommun skriver att det inte är tillåtet att installera en avfallskvarn i köket om den är "
       "kopplad till ledningsnätet. Kommunen motiverar det med att både husets egna och de kommunala "
       "ledningarna inte är byggda för matavfall, att fettstopp och giftiga gaser ökar och att näringen i "
       "matavfallet går förlorad. Från 1 januari 2024 är sortering av matavfall med kvarn till ledningsnätet "
       "inte heller längre godkänd enligt regler som regeringen beslutade i december 2022.",
       "En kvarn kopplad till en separat tank är däremot fortsatt ett godkänt system, men enligt kommunen "
       "kräver en sådan anläggning bygglov och samråd med kommunens avfallshämtare. För de flesta blir lösningen "
       "i stället ett genomtänkt sorteringsskåp under diskbänken, med plats för matavfall, förpackningar och "
       "restavfall.",
       "Har köket en gammal kvarn kopplad till avloppet tar vi bort den i samband med rivningen och sätter ett "
       "vanligt vattenlås. Avloppet ses över samtidigt, eftersom det är där matrester och fett brukar ha satt sig.",
     ],
     "aside": None},
    {"id": "utbyggnad",
     "h2": "Bygga ut köket i en villa i riksintresset",
     "paras": [
       "Sedan 1 december 2025 krävs inget bygglov för en tillbyggnad av ett en- eller tvåbostadshus på sammanlagt "
       "högst 30 kvadratmeter, och kommunen påpekar att tidigare skärmtak och attefallstillbyggnader räknas in. "
       "Men Danderyd är tydligt: inom kulturhistoriskt värdefulla områden och riksintressen för kulturmiljövården "
       "gäller alltid lovplikt. Om fastigheten berörs syns i kommunens kulturmiljökarta.",
       "Även en lovfri tillbyggnad kan kräva anmälan och startbesked, till exempel om husets konstruktion berörs, "
       "och ett nytt kök i tillbyggnaden innebär nästan alltid nya installationer för vatten, avlopp och "
       "ventilation. Kommunen påminner också om att den som ökar bruttoarean utan bygglov själv ansvarar för att "
       "informera kommunens VA-enhet.",
       "För egnahemsområdet i Enebyberg anger kommunens riktlinjer att husens ursprungliga arkitektoniska uttryck "
       "ska bevaras och vara vägledande vid om- och tillbyggnad. En köksutbyggnad bör alltså underordna sig huset. "
       "Mer om att bygga till finns under " + L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": {"title": "Köksutbyggnad i Danderyd", "items": [
       "Högst 30 m² lovfritt, äldre tillbyggnader räknas in",
       "Alltid bygglov i kulturmiljö och riksintresse",
       "Anmälan om konstruktion eller installationer berörs",
       "Ökad bruttoarea: meddela VA-enheten"]}},
    {"id": "ventilation",
     "h2": "Köksfläkten och villans ventilation",
     "paras": [
       "Många villor har fått nya ventilationssystem i efterhand. Enligt Danderyds kommun ska en- och "
       "tvåbostadshus med värmeåtervinning få en funktionskontroll när systemet installeras, men någon "
       "återkommande ventilationskontroll krävs inte. Ansluts köksfläkten till ett sådant system behöver den "
       "vara anpassad för det, annars rubbas balansen mellan från- och tilluft.",
       "I hus med självdrag genom en murad skorsten är frågan i stället om kanalen räcker för köket. En "
       "installation eller väsentlig ändring av ventilationen kräver anmälan och startbesked. Vi tar reda på "
       "vilket system huset har innan fläkten väljs. Se också " + L.format("koksrenovering.html", "köksrenovering i Stockholm") +
       " för planering av el, VVS och ventilation.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en köksrenovering i Danderyd till",
  "steps": [
    ("Besök i villan", "Vi går igenom köket, ventilationen, avloppet och om en utbyggnad är aktuell."),
    ("Kulturmiljökartan", "Vi kontrollerar om fastigheten ligger i ett riksintresse eller en värdekärna."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där rivning, installationer och inredning står var för sig."),
    ("Lov eller anmälan", "Behövs bygglov eller anmälan tas underlaget fram innan arbetet startar."),
    ("Rivning och bygge", "Gammal inredning och eventuell kvarn tas bort, rör och el dras och köket monteras."),
    ("Avslut", "Vitvaror och fläkt provas, och du får handlingar och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för köket i Danderyd",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
    "tillsammans med rut. Skatteverket räknar i småhus bland annat att montera fast köksinredning och installera "
    "vitvaror i samband med omfattande byggarbete, att modernisera el och byta vägguttag och att rengöra "
    "ventilation och imkanaler som rotarbete.",
    "Material ger inget avdrag, och är huset yngre än fem år får arbetet bara återställa det ursprungliga skicket. "
    "Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Danderyd?",
  "price": [
    "Storleken på köket och om det flyttas eller byggs ut avgör mest. En tillbyggnad med grund, stomme och tak är "
    "ett eget projekt, och i kulturmiljöerna tillkommer arbetet med bygglov. Ventilation, el och val av inredning "
    "styr resten. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Får vi ha en avfallskvarn i köket i Danderyd?",
     "Inte kopplad till ledningsnätet – det är förbjudet i kommunen. En kvarn kopplad till en separat tank är "
     "godkänd men kräver bygglov och samråd med avfallshämtaren."),
    ("Behöver vi bygglov för att bygga ut köket i Djursholm?",
     "Ja, om fastigheten ligger i ett kulturhistoriskt värdefullt område eller i riksintresset. Där gäller alltid "
     "lovplikt enligt kommunen. Kontrollera i kulturmiljökartan."),
    ("Måste vi meddela kommunen om köksutbyggnaden är lovfri?",
     "Ökar bruttoarean ska du själv informera kommunens VA-enhet, och berörs konstruktion eller installationer "
     "krävs anmälan och startbesked."),
    ("Behövs ventilationskontroll efter att vi bytt köksfläkt i en villa med FTX?",
     "Enligt kommunen krävs en funktionskontroll när ett system med värmeåtervinning installeras i en villa, men "
     "ingen återkommande kontroll. En väsentlig ändring av ventilationen kräver anmälan."),
    ("Räknas vår gamla attefallstillbyggnad in om vi bygger ut köket?",
     "Ja. Danderyds kommun skriver att alla lovfria tillbyggnader på huvudbyggnaden räknas in i de 30 "
     "kvadratmeterna, även tidigare skärmtak och attefallstillbyggnader."),
  ],
  "sources": [
    ("Danderyds kommun – Installation av matavfallskvarn", "https://www.danderyd.se/bygga-bo-och-miljo/vatten-och-avlopp-i-danderyd/avlopp/spillvatten/avfallskvarn/"),
    ("Danderyds kommun – Nya regler för bygglov från 1 december 2025", "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/"),
    ("Danderyds kommun – Obligatorisk ventilationskontroll", "https://www.danderyd.se/bygga-bo-och-miljo/boendemiljo/obligatorisk-ventilationskontroll/"),
    ("Danderyds kommun – Översiktsplan, Riks- och mellankommunala intressen (pdf)", "https://danderyd.se/contentassets/94fc6956dc264c4cab52c0a18ff5bafd/3-riks--och-mellankommunala-intressen.pdf"),
    ("Danderyds kommun – Riktlinjer för kulturmiljöhistoriska byggnader och miljöer 2024 (pdf)", "https://www.danderyd.se/globalassets/globala-filer/kommun-och-politik/ovriga-styrdokument-ny/styrande-dokument---samhallsbyggnad-miljo-och-exploatering/riktlinjer-for-kulturmiljohistoriska-byggnader-och-miljoer-i-danderyd-2024.pdf"),
    S_PBF, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Danderyd göras om?", "Boka ett gratis besök, så går vi igenom köket, huset och reglerna."),
  "img": [
    ("Renoverat kök i en stor sekelskiftesvilla i Danderyd",
     "renovated spacious kitchen in a large early 1900s Swedish national romantic villa, painted pale grey "
     "panelled cabinets, marble worktop, tall paned windows facing a garden with large oak trees, original "
     "wooden ceiling beams, wide plank floor, daylight, Djursholm"),
    ("Kök med vita luckor och mönstrat klinkergolv",
     "pull-out waste sorting drawer with several bins under the sink in a newly renovated Scandinavian kitchen, "
     "one small bin with a brown paper bag for food waste, wooden cabinet front open, clean and bright, close-up"),
  ],
},
}
