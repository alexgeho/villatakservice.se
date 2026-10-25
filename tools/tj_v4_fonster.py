# -*- coding: utf-8 -*-
"""Fönsterbyte – ortsidor v4: Bromma, Nacka, Täby, Huddinge, Sollentuna, Lidingö (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade 2026-10-25: Stockholms stad (bygglov.stockholm:
Fönster och dörrar, Fasadändring; vägledningen Varsam utveckling av småhus- och villaområden), Nacka kommun
(Fasadändringar; kulturmiljöprogrammet Villasamhällen vid järnvägen), Täby kommun (Fasadändring; Kulturmiljöer
i Täby), Huddinge kommun (Fasadändring; kulturmiljöprogram del 2), Sollentuna kommun (Ändra fönster eller
dörrar; Kulturhistoriska byggnader och kulturmiljöer; Bidrag för bullerdämpning i bostad), Lidingö stad
(Ändrade lagar och regler; kulturmiljöprogram del 1 och områdesbeskrivningarna Lidingö villastad och Breviks
villastad), Boverket (energiguiden: fönster och dörrar; PBL kunskapsbanken: fasadändring) och Skatteverket
(rotavdrag). Inga priser, garantier, omdömen, egna uppdrag eller cert. Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_FONSTER = ("Boverket – Energiguiden: Energirenovera eller byta fönster och dörrar",
               "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/fonster_dorrar/")
_BV_FASAD = ("Boverket – PBL kunskapsbanken: Bygglov för fasadändring",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"fonsterbyte-bromma.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Bromma", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Bromma – spröjs, mittpost och stadens regler",
  "description": "Fönsterbyte i Bromma: småspröjs i Äppelviken, tvåluftsfönster på småstugorna, stadens regler om spröjs och mittpost och när bågarna kan behållas.",
  "h1": "Fönsterbyte i Bromma",
  "lead": "I Bromma är det ofta fönstren som avslöjar husets ålder: småspröjsade rutor i Äppelviken, tvåluftsfönster i liv med panelen på småstugorna och en fri fönstersättning på funkisvillorna i Södra Ängby. Geal Entreprenad AB byter och renoverar fönster i hela Bromma, mäter upp profiler och indelning innan något beställs och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Småspröjs, småstugor och funkis i Bromma.",
  "sections": [
    {"id": "fonstren-bromma", "anchor": "Fönstren i Bromma",
     "h2": "Småspröjs, tvåluftsfönster och fri fönstersättning",
     "paras": [
       "Stockholms stads vägledning Varsam utveckling av småhus- och villaområden beskriver hur Brommas trädgårdsstäder fick olika stilideal. I Äppelviken blev det nationalromantiska inslaget tydligt, med branta takfall, stor formrikedom och fönster med småspröjsade rutor. I 1920-talets trädgårdsstäder, som Nockeby, Höglandet, Ålsten och Smedslätten, blev husen enklare och fasaderna symmetriskt uppbyggda.",
       "Småstugorna i Norra Ängby och Olovslund byggdes efter typritningar som enligt vägledningen styrde utformningen på en detaljerad nivå, även fönstren. I de tidiga utbyggnadsfaserna dominerar tvåluftsfönster med en spröjs. Senare blev tvåluftsfönster utan spröjs vanliga, men även andra fönstertyper förekommer, och fönstren sitter placerade i fasadliv.",
       "Södra Ängby skiljer sig från båda. Där fick villorna modernismens formspråk med kubiska volymer och en oregelbunden fönstersättning. Södra Ängby och Ålstensgatan är utpekade som riksintressen, och vägledningen räknar ursprungliga byggnadsdetaljer som fönster, entrédörrar och räcken till det som bär trädgårdsstädernas karaktär.",
     ],
     "aside": {"title": "Fönstren i korthet", "items": [
       "Äppelviken: småspröjsade rutor", "Småstugor: tvåluftsfönster, med eller utan spröjs",
       "Småstugor: fönster i fasadliv", "Södra Ängby: oregelbunden fönstersättning"]}},
    {"id": "andring-bromma", "h2": "Det här räknar staden som en ändring av fönstret",
     "paras": [
       "På stadens sida om fönster och dörrar står det att lovfrågan beror på vilken byggnad och fasad ändringen gäller. Som exempel på ändringar nämns att byta material eller kulör på fönster, att ändra dimensioner, proportioner eller profilering på karmar, bågar och spröjsar och att lägga till spröjs eller ta bort mittposten. Staden påpekar att ett hus kan ha karaktäristiska fönster eller en tidstypisk fönsterindelning.",
       "Sedan 1 december 2025 krävs normalt inget bygglov för fasadändringar på en- och tvåbostadshus. Utökad lovplikt gäller däremot om huset är särskilt kulturhistoriskt värdefullt, ligger i ett värdefullt område eller om detaljplanen skyddar särskilda värden. Stadsmuseets klassificeringskarta ger en första indikation, men alla byggnader är ännu inte inventerade, och detaljplanen går att läsa i Bygg- och plantjänsten.",
       "För en Brommavilla blir det konkret. Att ersätta en småspröjsad båge med helt glas, ta bort mittposten i ett tvåluftsfönster eller byta trä mot ett annat material är just de ändringar staden räknar upp. Även när bytet är lovfritt ska varsamhetskravet följas.",
     ],
     "aside": {"title": "Exempel på ändringar", "items": [
       "Annat material eller annan kulör", "Andra profiler på karm och båge",
       "Spröjs som läggs till eller tas bort", "Mittpost som tas bort"]}},
    {"id": "underlag-bromma", "h2": "Uppmätning och detaljritning när lov krävs",
     "paras": [
       "Krävs bygglov vill staden ha en fasadritning i skala 1:100 där material och kulörer framgår, eller en separat material- och kulörbeskrivning med NCS-koder. En detaljritning i skala 1:10, 1:20 eller 1:50 behövs när en detalj påverkar utformningen, och staden nämner fönster som exempel. Fotografier av huset och fönstren som ska ändras ska också bifogas.",
       "Därför mäter vi upp varje fönster vid besöket: karmens mått, bågarnas och spröjsens bredd, glasindelningen och hur djupt fönstret sitter i väggen. Med de måtten går det att beställa ett nytt fönster som har samma proportioner, och samma uppgifter blir underlag för en detaljritning.",
       "Staden ger också två praktiska råd. Ett nytt eller större fönster kan öka insynen hos grannen, så det är bra att berätta om planerna i förväg, och en ny öppning kan påverka husets bärande konstruktion. Ska även en takkupa eller ett takfönster ses över finns mer under " + _L.format("taklaggare-bromma.html", "takläggare i Bromma") + ".",
     ],
     "aside": None},
    {"id": "behalla-bromma", "h2": "Behålla bågarna och förbättra dem inifrån",
     "paras": [
       "Enligt Boverkets energiguide ger det oftast en mindre energibesparing att förbättra befintliga fönster än att byta, men det kostar oftast mindre och kan ge en bättre totalkalkyl när fönstren är i gott skick. Vägledningen råder dessutom att ta tillvara karaktärsskapande material och detaljer så långt det går, och i Bromma sitter mycket av husets karaktär i bågarna.",
       "Boverket listar vad som brukar behövas förutom nytt glas: att byta tätningslist, rikta upp bågar som inte hänger rakt, förbättra drevningen, kitta om och måla samt reparera fuktskador i karmar och bågar. Får innerbågen ett energiglas eller en tvåglaskassett behöver bågen klara den extra tyngden, och gångjärn och beslag kan behöva förstärkas.",
       "Många äldre villor har självdrag, och då kan luften som läcker in kring fönstren vara en del av tilluften. Blir huset tätare behöver tilluften ordnas på annat sätt, till exempel med spaltventiler i bågen eller karmen. Ska fönstren målas om utvändigt samtidigt, läs mer under " + _L.format("malare-bromma.html", "målare i Bromma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett fönsterbyte i Bromma till",
  "steps": [
    ("Platsbesök", "Vi bedömer karm, bågar och glas, mäter upp varje fönster och noterar spröjs, mittpost och fasadliv."),
    ("Klassning och plan", "Stadsmuseets karta och detaljplanen kontrolleras, så att du vet om bytet kräver lov."),
    ("Byte eller renovering", "Fönster för fönster bedömer vi vad som kan renoveras och vad som behöver bytas."),
    ("Kostnadsförslag", "Fönster, glas, montage, foder och bleck står var för sig i ett skriftligt förslag."),
    ("Montage", "Gamla fönster tas ur, nya monteras med drevning och tätning, och ventilationen ses över."),
    ("Genomgång", "Foder och bleck görs klart och vi går igenom varje fönster tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för nya fönster i Bromma",
  "rot": [
    "För ett småhus räknar Skatteverket det som rotarbete att reparera eller byta ut fönster, montera bullerglas och isolerglas, byta fönsterbleck och måla fönster. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Själva fönstren och resorna räknas inte.",
    "Du behöver äga villan medan arbetet pågår och bo i den. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden i Bromma",
  "price": [
    "Antalet fönster och deras storlek, om spröjs och profiler ska tillverkas efter förlaga, om bågarna kan renoveras och få energiglas i stället för att bytas, hur mycket foder och bleck som behöver göras om och om övervåningen kräver ställning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi ta bort spröjsen i fönstren på vår villa i Äppelviken?",
     "Ligger huset i ett område med utökad lovplikt krävs bygglov, eftersom staden räknar en ändrad spröjsindelning som en fasadändring. Kontrollera Stadsmuseets karta och detaljplanen innan något beställs."),
    ("Vilka fönster satt från början på småstugorna i Norra Ängby?",
     "Enligt stadens vägledning dominerade tvåluftsfönster med en spröjs i de tidiga utbyggnadsfaserna, medan tvåluftsfönster utan spröjs blev vanligare senare. Fönstren sitter i fasadliv."),
    ("Behövs en detaljritning för nya fönster i Bromma?",
     "Bara om bytet kräver lov och detaljen påverkar utformningen. Då kan staden vilja se en detaljritning av fönstret i skala 1:10, 1:20 eller 1:50."),
    ("Klarar de gamla bågarna ett energiglas på insidan?",
     "Det beror på om bågen tål den extra tyngden och om det finns djup nog för glaset. Gångjärn och beslag kan behöva förstärkas, vilket vi bedömer vid besöket."),
    ("Måste vi tänka på ventilationen när fönstren byts i en äldre Brommavilla?",
     "Ja, om huset har självdrag. Luften som läckt in kring de gamla fönstren behöver då ersättas, till exempel med spaltventiler i bågen eller karmen."),
  ],
  "sources": [
    ("Stockholms stad – Fönster och dörrar (bygglov.stockholm)",
     "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fonster-och-dorrar/"),
    ("Stockholms stad – Fasadändring (bygglov.stockholm)",
     "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/"),
    _VARSAM, _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren på Brommavillan bytas?", "Boka ett gratis platsbesök så mäter vi upp fönstren och går igenom vad som kan sparas."),
  "img": [
    ("Trävilla i Bromma med vita tvåluftsfönster med spröjs och rött tegeltak",
     "1920s Swedish one-and-a-half storey wooden villa with vertical board-and-batten panel painted pale yellow, white two-pane casement windows with a single horizontal glazing bar set flush with the facade, steep red clay tile roof, hedge and apple trees, garden suburb Bromma Stockholm, late summer daylight, no people, no text"),
    ("Uppmätning av en äldre fönsterbåge med spröjs inför fönsterbyte",
     "close-up of an old white painted wooden window sash with small glazing bars and slightly wavy old glass, a folding wooden ruler laid across the frame, soft daylight on a Swedish wooden house wall, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ NACKA
"fonsterbyte-nacka.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Nacka", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Nacka – villorna längs Saltsjöbanan",
  "description": "Fönsterbyte i Nacka: småspröjsade fönster i Saltsjö-Duvnäs och på Solsidan, panoramafönster från 1900-talets mitt, kommunens kulturmiljökarta och slagregn.",
  "h1": "Fönsterbyte i Nacka",
  "lead": "Längs Saltsjöbanan står villor från sekelskiftet med småspröjsade fönster, tegelvillor i nationalromantik och hus från 1900-talets mitt med stora panoramafönster. Geal Entreprenad AB byter och renoverar fönster i hela Nacka, går igenom kommunens kulturmiljöunderlag innan något beställs och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Villasamhällena vid Saltsjöbanan.",
  "sections": [
    {"id": "saltsjobanan", "anchor": "Villorna vid banan",
     "h2": "Villasamhällena vid Saltsjöbanan och deras fönster",
     "paras": [
       "Kommunens kulturmiljöprogram Villasamhällen vid järnvägen beskriver sekelskiftets villasamhällen som terränganpassade, med svängda gator, stora tomter och påkostade villor i tidstypisk panelarkitektur. Programmet konstaterar att här finns exempel på landets främsta villaarkitektur från olika perioder.",
       "Fönstren skiljer sig mellan epokerna. På Solsidan visar programmet en tegelvilla i nationalromantisk stil från 1913, ritad av Ferdinand Boberg, där småspröjsade fönster och mycket muryta hör till stilen. I Saltsjö-Duvnäs nämns en stenvilla från 1910-talet med småspröjsade fönster och högt tegeltak. Programmet visar också en villa från 1900-talets mitt med stora panoramafönster och olika material i fasaden.",
       "Även de yngre husen har sina detaljer. Radhusområdet Vita Raden i Saltsjö-Duvnäs från 1967 beskrivs som 1960-talsmodernism med vita betongelement och tunna fönsterprofiler. Ett nytt fönster med grövre profiler syns på ett sådant hus lika tydligt som på en sekelskiftesvilla.",
     ],
     "aside": {"title": "Fönster i programmet", "items": [
       "Småspröjs på nationalromantiska villor", "Panoramafönster från 1900-talets mitt",
       "Tunna profiler på Vita Raden", "Fönsteromfattningar som ska behållas"]}},
    {"id": "forhallningssatt", "h2": "Fönster och fönsteromfattningar ska behållas",
     "paras": [
       "För Tattby, Solsidan och de andra villasamhällena återkommer samma förhållningssätt i programmet: tidstypisk utformning av grundmurar, fasader, tak, fönster, fönsteromfattningar, entrépartier, räcken och staket behålls. På Solsidan och i Tattby finns många välbevarade villor som programmet beskriver som känsliga för förändringar, och där eftersträvas att befintliga tak, fasader och fönster bevaras.",
       "Programmet skriver också att antikvarisk medverkan kan krävas inför en bygglovsprövning, och att planläggning med skydd av kulturvärden ska eftersträvas i områden med äldre detaljplaner. Den som planerar ett fönsterbyte i ett av de här områdena bör därför räkna med att utformningen kan behöva redovisas noga.",
       "I praktiken betyder det att fönstren ska ha samma indelning och liknande profiler som de gamla, och att omfattningarna runt fönstren får sitta kvar eller göras om i samma utförande. Boverket lyfter också fram material, proportioner, indelning och profilering som det som ger ett fönster dess uttryck.",
     ],
     "aside": None},
    {"id": "lov-nacka", "h2": "Lila eller orange i kommunens karta",
     "paras": [
       "Nacka kommun räknar nya fönster eller dörrar, och ändringar av befintliga, som fasadändringar. Inom detaljplan krävs inte längre bygglov för fasadändringar på en- eller tvåbostadshus, men bytet måste stämma med detaljplanen.",
       "Ligger fastigheten i ett område som enligt 8 kap. 13 § PBL är särskilt värdefullt gäller utökad lovplikt för fasadändringar som påverkar områdets karaktär. I kommunens webbkarta visar lila markering byggnader och områden med särskilt höga kulturvärden, och orange att kulturvärdena kan vara under bedömning. Stadsbyggnadsservice kan svara på frågor om de orange områdena. Påverkar arbetet den bärande konstruktionen, till exempel när en öppning görs större, krävs en anmälan.",
       "Utanför de markerade områdena är ett byte till fönster med samma utseende normalt en enkel åtgärd, men varsamhetskravet gäller fortfarande. Boverket nämner fönster bland de åtgärder som kan påverka en byggnads karaktärsdrag, och på en villa från sekelskiftet är det svårt att byta fönster utan att det syns från gatan. Därför stämmer vi av indelning och profiler med dig innan beställningen.",
     ],
     "aside": {"title": "Före beställningen", "items": [
       "Lila eller orange markering?", "Vad säger detaljplanen?",
       "Ska någon öppning ändras?", "Finns omfattningar att bevara?"]}},
    {"id": "vind-nacka", "h2": "Vindutsatta lägen och vatten under fönstren",
     "paras": [
       "Boverkets energiguide påpekar att gamla fönstertätningar ofta släpper igenom vatten under fönstren, särskilt där väggen utsätts för slagregn i vindutsatta lägen. Innan ett fönster byts bör man därför undersöka om det finns fuktskador i väggen och om fönstret behöver kompletteras med fuktskydd.",
       "På de branta tomterna mot vattnet tar vissa fasader mycket vind. Där kontrollerar vi särskilt bröstningen under fönstret, fönsterbänkens anslutning och att fönsterblecket leder vattnet ut från väggen. Behöver fasaden lagas runt fönstren, läs mer under " + _L.format("fasadrenovering-nacka.html", "fasadrenovering i Nacka") + ".",
       "Boverket nämner också solavskärmning, eftersom bättre isolerade fönster ökar risken för övertemperatur inomhus. På stora panoramafönster mot söder eller väster är det värt att tänka på glasval och solskydd redan när fönstren beställs.",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången vid fönsterbyte i Nacka",
  "steps": [
    ("Inventering", "Vi går igenom fönster, omfattningar och bröstningar och letar fukt där slagregnet tar."),
    ("Karta och plan", "Kulturmiljökartan och detaljplanen stäms av innan fönstertyp väljs."),
    ("Val av fönster", "Indelning, profiler och glas väljs så att de passar husets ålder och läge."),
    ("Skriftligt förslag", "Fönster, montage, omfattningar och bleck redovisas var för sig."),
    ("Montage", "Fönstren byts ett i taget, med drevning, tätning och fuktskydd under fönstret."),
    ("Genomgång", "Vi går igenom varje fönster tillsammans med dig och visar hur de sköts."),
  ],
  "rot_h2": "Rotavdrag för fönsterarbete i Nacka",
  "rot": [
    "Skatteverket godkänner rotavdrag i småhus för att reparera eller byta ut fönster, montera isolerglas och bullerglas och byta fönsterbleck. Solfilm, myggnät och markiser ger inget avdrag. Det är arbetskostnaden som ger avdrag: 30 procent av den, med högst 50 000 kr per person och år och 75 000 kr som tak för rot och rut tillsammans.",
    "Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Nacka?",
  "price": [
    "Antal och storlek på fönstren, om indelning och profiler ska anpassas till en äldre villa, om omfattningarna ska göras om, om väggen under fönstren behöver lagas och om stora glaspartier kräver särskilt glas eller lyft. Branta tomter kan kräva mer ställning. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi byta de småspröjsade fönstren på en villa på Solsidan?",
     "Det går, men kulturmiljöprogrammet räknar fönster och fönsteromfattningar till det som ska behållas. Ligger huset i ett lila område krävs bygglov, och nya fönster bör få samma indelning som de gamla."),
    ("Vad är antikvarisk medverkan vid ett fönsterbyte i Nacka?",
     "Att en sakkunnig inom kulturmiljö deltar i planeringen. Kulturmiljöprogrammet skriver att det kan krävas inför en bygglovsprövning i villasamhällena vid Saltsjöbanan."),
    ("Behöver vi anmäla om ett fönster görs större i Nacka?",
     "Påverkar ändringen den bärande konstruktionen kräver kommunen en anmälan, även när själva fasadändringen är lovfri."),
    ("Varför blir det fuktigt under fönstret på vår villa mot vattnet?",
     "Boverket skriver att gamla fönstertätningar ofta släpper in vatten under fönstren i lägen med slagregn. Bröstningen bör undersökas innan det nya fönstret sätts in."),
    ("Blir det varmare inne med nya panoramafönster?",
     "Bättre isolerade fönster kan öka risken för övertemperatur, och Boverket föreslår solavskärmning som åtgärd. Glasval och solskydd bör därför bestämmas samtidigt."),
  ],
  "sources": [
    ("Nacka kommun – Fasadändringar",
     "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/lovfria-atgarder/fasadandringar/"),
    ("Nacka kommun – Kulturmiljöprogram: Villasamhällen vid järnvägen (pdf)",
     "https://www.nacka.se/499626/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-jarnvagen.pdf"),
    _BV_FONSTER, _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren i Nackavillan bytas?", "Boka ett gratis platsbesök så går vi igenom fönster, omfattningar och lovfrågor."),
  "img": [
    ("Nationalromantisk villa i Nacka med småspröjsade fönster och högt tegeltak",
     "early 1910s Swedish national romantic villa with light plastered facade and dark red brick details, many small-paned white wooden windows, tall steep red clay tile roof, pine trees and granite rocks on a hillside, Saltsjöbaden Nacka, autumn daylight, no people, no text"),
    ("Fönsterbröstning och nytt fönsterbleck under ett träfönster",
     "close-up of the lower part of a white wooden window in a light painted wooden facade, new grey metal window sill flashing with drip edge, freshly sealed joint, rain drops on the glass, overcast Nordic daylight, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TÄBY
"fonsterbyte-taby.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Täby", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Täby – trä, originalformat och grupphus",
  "description": "Fönsterbyte i Täby: fönster i trä i Roslags-Näsby och Byle, originalformat i grupphusen, fönster i liv i Norskogen och kommunens råd om energiglas.",
  "h1": "Fönsterbyte i Täby",
  "lead": "Täby har spröjsade fönster i villastäderna kring järnvägen, grupphus från 1950–70-talen med enhetliga fönster och elementhus där fönstren sitter i liv med plåtfasaden. Kommunens kulturmiljöunderlag ger råd för många av områdena. Geal Entreprenad AB byter och renoverar fönster i hela Täby, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villastäder och grupphus i Täby.",
  "sections": [
    {"id": "villastader-taby", "anchor": "Fönstren i Täby",
     "h2": "Spröjsade fönster i trä i de äldre villastäderna",
     "paras": [
       "Kommunens underlag Kulturmiljöer i Täby beskriver den äldre villabebyggelsen i Roslags-Näsby och Norra Viggbyholm med träfasader i ljusa kulörer eller falurött, fönsterfoder i kontrasterande färg och putsade fasader i milda pastellfärger. Fönstren är ofta spröjsade, och verandor och burspråk ger variation i fasaderna.",
       "I Täby kyrkby och Byle växte villastäderna fram efter planer från 1907. Där är det vanligt med branta, ofta brutna tak, glasverandor och spröjsade fönster, och foder, vindbrädor och knutar är oftast vita. För alla fyra områdena ger underlaget samma råd: fönster bör utformas i trä och i likhet med originalutformningen.",
       "Rådet gäller även när fönstren byts av energiskäl. Ett nytt träfönster kan få moderna glas och tätningar men ändå behålla spröjsindelning, proportioner och foder. Det är den kombinationen vi utgår från när vi föreslår fönster till ett äldre hus i Täby.",
     ],
     "aside": {"title": "Råd för de äldre villorna", "items": [
       "Fönster i trä", "Utformning som originalet",
       "Ofta spröjsade fönster", "Foder i kontrastfärg eller vitt"]}},
    {"id": "grupphus-taby", "h2": "Grupphusen – originalformat och bruna snickerier",
     "paras": [
       "För grupphusområdena är råden ännu tydligare. Underlaget säger att ursprunglig färgsättning och ursprungliga fönsterformat ska behållas. Kvarteret Kammaren, ett välbevarat kedjehuskvarter från 1976 med bottenvåningar i fasadtegel och bruna fönstersnickerier, har rådet att originalformatet på fönstren ska behållas. I kvarteret Knäpparen, med villor från 1978–1979 i rödbrunt eller sandfärgat tegel, gäller att de bruna fönstersnickerierna ska behållas.",
       "Norskogen i Näsbypark är ett grupphusområde med 197 bostäder i villor, parhus och radhus från 1957–1959. Fasaderna har finprofilerad fabrikslackad aluminiumplåt och fönster utan spröjs och foder som sitter i liv med fasaden. Där är det just avsaknaden av detaljer som ska bevaras, och ett fönster med grov karm eller påsatta foder skulle bryta mot det.",
       "Byts fönstren i ett grupphusområde är det klokt att utgå från de ursprungliga måtten och kulören. Boverket påpekar dessutom att nya fönster med grövre snickerier släpper in mindre dagsljus, vilket märks i små rum.",
     ],
     "aside": {"title": "I grupphusen", "items": [
       "Behåll ursprungligt fönsterformat", "Behåll ursprunglig kulör på snickerierna",
       "Norskogen: fönster i liv, utan foder", "Undvik grövre profiler"]}},
    {"id": "energi-taby", "h2": "Kommunens råd: underhåll och invändigt energiglas",
     "paras": [
       "I de generella råden skriver kommunen att äldre fönster kan vara av hög kvalitet, ofta är värda att underhållas och eventuellt kan kompletteras med invändigt energiglas. Boverkets energiguide pekar åt samma håll: tätning och energiglas på insidan är ofta det som lönar sig först, medan ett byte kan behöva göras tillsammans med andra renoveringar för att bli lönsamt.",
       "Byts fönstren ändå bör de nya väljas med lågt U-värde för hela fönstret och med ett glas som passar läget. Boverket påpekar att olika glas ger olika solavskärmning, bullerdämpning och dagsljusinsläpp. Kontrollera märkningen när fönstren levereras, så att rätt U-värde sitter i rätt hål.",
       "Ska fasaden tilläggsisoleras råder kommunen att fönstren flyttas ut, så att de sitter i samma förhållande till fasaden som tidigare. Planeras både fönster och isolering lönar det sig att göra arbetena i samma etapp, se " + _L.format("fasadrenovering-taby.html", "fasadrenovering i Täby") + ".",
     ],
     "aside": None},
    {"id": "lov-taby", "h2": "Lovfritt – med undantag för de värdefulla miljöerna",
     "paras": [
       "Täby kommun skriver att det inte behövs bygglov för fasadändringar på en- och tvåbostadshus, om byggnaden inte är särskilt värdefull, inte ligger i ett särskilt värdefullt område och inte har utökad lovplikt i detaljplanen. Andra ändringar som påverkar byggnadens karaktärsdrag kan också kräva lov, och den som är osäker kan få rådgivning av kommunen.",
       "Kommunen råder också fastighetsägare att ta fram ritningarna på huset och fråga efter äldre handlingar, eftersom många hus har byggts till. Originalritningen visar hur fönstren var tänkta från början, och det blir ett bra underlag när nya fönster ska väljas. Ska takfönster eller kupor ses över samtidigt finns mer under " + _L.format("taklaggare-taby.html", "takläggare i Täby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Täby",
  "steps": [
    ("Besök och mätning", "Vi mäter upp fönstren, noterar indelning, kulör och foder och bedömer skicket."),
    ("Ritningar och råd", "Originalritningar och kulturmiljöunderlaget för området gås igenom."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag med fönster, glas, montage och ROT-avdrag."),
    ("Beställning", "Fönstren beställs i trä och med samma format som originalet där råden säger så."),
    ("Montage", "Fönstren monteras ett i taget, med drevning, tätning och nya bleck vid behov."),
    ("Avslut", "Vi kontrollerar märkning och funktion och går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Täby",
  "rot": [
    "Att reparera eller byta ut fönster och att montera isolerglas eller bullerglas i ett småhus är rotarbete enligt Skatteverket. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag.",
    "Äger ni huset tillsammans har var och en sitt avdragsutrymme. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset i Täby?",
  "price": [
    "Antal och storlek på fönstren, om de ska tillverkas i trä med spröjs efter förlaga, vilket glas som väljs, om foder och bleck behöver göras om och om fönstren ska flyttas ut i samband med en tilläggsisolering. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste nya fönster vara av trä i Roslags-Näsby?",
     "Kommunens kulturmiljöunderlag rekommenderar fönster i trä som liknar originalet. Kräver detaljplanen lov prövas utformningen, annars är rådet vägledande."),
    ("Får vi byta till vita fönster i kvarteret Knäpparen?",
     "Kommunens råd för kvarteret är att de bruna fönstersnickerierna ska behållas. Kontrollera detaljplanen och fråga kommunen om fastigheten har utökad lovplikt."),
    ("Kan fönstren i Norskogen bytas mot fönster med foder?",
     "Det skulle bryta mot områdets karaktär. Underlaget beskriver fönster utan spröjs och foder som sitter i liv med plåtfasaden, och nya fönster bör följa det."),
    ("Är det bättre att sätta energiglas i de gamla fönstren än att byta?",
     "Ofta, om fönstren är i gott skick. Kommunen skriver att äldre fönster kan kompletteras med invändigt energiglas, och Boverket menar att det kan ge en bättre totalkalkyl."),
    ("Var hittar jag originalritningarna till mitt hus i Täby?",
     "Kommunen råder dig att ta fram ritningarna och fråga efter äldre handlingar. De visar hur fönstren var utformade när huset byggdes."),
  ],
  "sources": [
    ("Täby kommun – Fasadändring",
     "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/fasadandring"),
    ("Täby kommun – Kulturmiljöer i Täby (pdf)",
     "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Funderar du på nya fönster i Täby?", "Boka ett gratis platsbesök så går vi igenom fönstren och kommunens råd för ditt område."),
  "img": [
    ("Kedjehus i Täby med fasadtegel och bruna fönstersnickerier",
     "row of modest 1970s Swedish one-and-a-half storey linked houses with ground floor in red-brown facing brick, upper part in brown stained vertical wood panel, plain dark brown wooden window frames without glazing bars, low-pitched roofs with dark concrete tiles, carports between the houses, low hedges, Täby suburb, clear autumn day, no people, no text"),
    ("Spröjsat träfönster med vita foder på en äldre villa",
     "close-up of a white painted wooden two-pane window with glazing bars and white trim boards on a light yellow wooden villa facade, early 1900s Swedish style, soft daylight, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HUDDINGE
"fonsterbyte-huddinge.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Huddinge", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Huddinge – egnahem, teak och mittposter",
  "description": "Fönsterbyte i Huddinge: enkelt spröjsade fönster i egnahemsområdena, teakfönster från 1970-talet, kommunens regler och fukt under fönstren.",
  "h1": "Fönsterbyte i Huddinge",
  "lead": "Huddinges villor har fönster från helt olika tider: enkelt spröjsade fönster i egnahemsområdena, enhetliga fönsterrader i folkhemmets grupphus och påkostade fönster i teak på 1970-talets arkitektritade villor. Geal Entreprenad AB byter och renoverar fönster i hela Huddinge och börjar med ett gratis platsbesök och ett skriftligt kostnadsförslag.",
  "card": "Egnahem, grupphus och 70-talsvillor.",
  "sections": [
    {"id": "epoker-huddinge", "anchor": "Fönstren i Huddinge",
     "h2": "Fyra epoker – fyra sorters fönster",
     "paras": [
       "Kommunens kulturmiljöprogram beskriver egnahemsområdena från 1910–1940-talen med villor i jugend, nationalromantik, klassicism och tidig funkis. Träpanel, enkelt spröjsade fönster och tegeltäckta sadel- eller brutna tak är de tongivande dragen. I sommarnöjena från 1880–1920-talen är villorna större, med glasverandor, snickarglädje och spröjsade fönster.",
       "Folkhemsbygget från 1940–1960-talen gav små enhetliga villor, kedjehus och radhus i trä, puts eller fasadtegel. Programmet beskriver fönstersättningen i 1940-talets områden som enhetlig. På 1970-talet blev villorna större, och arkitektritade hus fick enligt programmet påkostade material som portar och fönster i teak och stora glasade partier.",
       "Den spridningen gör att ett fönsterbyte i Huddinge sällan går att göra efter mall. Ett teakfönster från 1970-talet, en spröjsad båge från 1920-talet och ett fönster i en radhuslänga där alla grannar har likadana kräver olika lösningar.",
     ],
     "aside": {"title": "Fönster per epok", "items": [
       "Sommarnöjen: spröjs och glasverandor", "Egnahem: enkelt spröjsade fönster",
       "Folkhem: enhetlig fönstersättning", "1970-tal: teak och stora glaspartier"]}},
    {"id": "mittpost", "h2": "Mittposten och de stående formaten",
     "paras": [
       "I avsnittet om landsbygdens bebyggelse skriver programmet att fönster är byggnadernas ögon och har en starkt karaktärsbärande effekt på hur en byggnad uppfattas. I äldre byggnadstradition placeras fönstren symmetriskt och har kvadratiska eller stående rektangulära format, och mittposten är en viktig del av fönstrets uttryck.",
       "Därför avråder vi från att ersätta ett tvåluftsfönster med en stor fast ruta på ett äldre hus, även när det är lovfritt. Ett nytt fönster kan ha samma mittpost och samma proportioner men moderna glas och tätningar. Boverket framhåller också att material, proportioner, indelning och profilering är det som ger ett fönster dess uttryck.",
       "På 1970-talets villor är det i stället ofta de stora glaspartierna och träslaget som bär arkitekturen. Är teakkarmarna friska kan bågar och glas förbättras, och byts fönstren bör de nya ha liknande indelning och ett ytskikt som passar huset. Mer om ytskikt på trä finns under " + _L.format("malare-huddinge.html", "målare i Huddinge") + ".",
     ],
     "aside": None},
    {"id": "lov-huddinge", "h2": "Kommunens regler för nya fönster",
     "paras": [
       "Huddinge kommun skriver att det inte krävs bygglov för att ändra utseendet på en- eller tvåbostadshus, om inte byggnaden eller området är kulturhistoriskt värdefullt. Att sätta in nya dörrar och fönster räknas som en fasadändring, och i värdefulla miljöer krävs därför bygglov. Kommunens webbkarta visar om en byggnad ligger inom ett kulturmiljöområde.",
       "Krävs lov för ett nytt fönster behöver ansökan bara ha med en planritning, enligt kommunen. Är du osäker kan du söka bygglov frivilligt. Även en lovfri ändring ska vara anpassad till hur området ser ut, och påverkas byggnadens bärande delar väsentligt, till exempel när en ny öppning tas upp, krävs anmälan och startbesked.",
       "I folkhemmets kedjehus och radhus är fönstersättningen en del av helheten i hela längan. Byts fönstren i ett hus åt gången är det klokt att välja samma indelning och kulör som grannarna har, så att raden fortsätter att hänga ihop. Det gör det också lättare för nästa granne som vill byta.",
     ],
     "aside": {"title": "Kontrollera först", "items": [
       "Kulturmiljöområde i webbkartan?", "Nytt fönster eller samma öppning?",
       "Påverkas bärande delar?", "Hur ser grannhusen ut?"]}},
    {"id": "fukt-huddinge", "h2": "Fukt under fönstret och byte på vintern",
     "paras": [
       "Boverket skriver att det är vanligt att gamla fönstertätningar släpper igenom vatten under fönstren, särskilt där fasaden utsätts för slagregn. Innan ett nytt fönster sätts in bör man därför undersöka om väggen har fuktskador och om fönstret behöver kompletteras med fuktskydd. Vi kontrollerar bröstningen under det gamla fönstret när det tas ut.",
       "Fönster kan bytas året runt, men byts de på vintern råder Boverket att göra det stegvis, så att huset inte kyls ned. Planera också för inbrottsskyddet om ett fönsterhål behöver stå öppet en tid i väntan på det nya fönstret.",
       "När fönstren är på plats behöver värmesystemet ofta justeras, eftersom huset tappar mindre värme. Har huset mekanisk ventilation ska även luftflödena justeras in. Ska fasaden runt fönstren också ses över, se " + _L.format("fasadrenovering-huddinge.html", "fasadrenovering i Huddinge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går fönsterbytet till i Huddinge",
  "steps": [
    ("Besök", "Vi går igenom fönstren, mäter upp dem och noterar mittposter, indelning och träslag."),
    ("Kulturmiljö och lov", "Webbkartan och detaljplanen kontrolleras, och vi ser om någon öppning ändras."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag med fönster, montage, bleck och ROT."),
    ("Etappindelning", "Bytet planeras rum för rum, så att huset hålls varmt och stängt."),
    ("Montage", "Bröstningen kontrolleras, fönstret monteras och drevning och fuktskydd görs klart."),
    ("Avslut", "Foder och bleck kommer på plats och vi går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönster i Huddinge",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att reparera eller byta ut fönster, montera isolerglas och bullerglas, byta fönsterbleck och montera ställning i samband med arbetet. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och 75 000 kr tillsammans med rutavdrag.",
    "Fönstren i sig räknas som material och ger inget avdrag. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Huddinge?",
  "price": [
    "Antalet fönster, deras storlek och träslag, om mittposter och spröjs ska tillverkas efter förlaga, om bröstningen under fönstren behöver lagas, om foder och bleck görs om och om arbetet kräver ställning. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi behålla teakfönstren i vår 70-talsvilla i Huddinge?",
     "Ofta, om karmarna är friska. Bågar, tätningar och glas kan förbättras, och kulturmiljöprogrammet lyfter fram teakfönstren som ett tidstypiskt drag för 1970-talets arkitektritade villor."),
    ("Behövs bygglov för ett nytt fönster i ett kulturmiljöområde i Huddinge?",
     "Ja. Att sätta in nya fönster räknas som en fasadändring, och i kulturhistoriskt värdefulla miljöer krävs bygglov. Ansökan behöver då en planritning."),
    ("Varför ska mittposten behållas när fönstret byts?",
     "Kulturmiljöprogrammet beskriver mittposten som en viktig del av fönstrets uttryck i äldre byggnadstradition. Utan den ser ett äldre hus ombyggt ut."),
    ("Hur undviker vi att huset blir kallt när fönstren byts på vintern?",
     "Boverket råder att byta stegvis. Vi tar ett eller ett par fönster i taget, så att bara en liten del av huset står öppen under arbetet."),
    ("Behöver värmen justeras efter fönsterbytet?",
     "Ja, enligt Boverket behöver värmesystemet ofta justeras in, och i hus med mekanisk ventilation även luftflödena."),
  ],
  "sources": [
    ("Huddinge kommun – Fasadändring",
     "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/fasadandring"),
    ("Huddinge kommun – Kulturmiljöprogram del 2 (pdf)",
     "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren bytas i Huddinge?", "Boka ett gratis platsbesök så går vi igenom fönstren och vad som kan sparas."),
  "img": [
    ("Egnahemsvilla i Huddinge med träpanel och enkelt spröjsade fönster",
     "1920s Swedish wooden villa with light grey horizontal wood panel, white two-pane windows with a single glazing bar and a central mullion, red clay tile gable roof, fruit trees in a large front garden set back from a narrow road, Huddinge Stockholm, early autumn, no people, no text"),
    ("Stort fönsterparti med karmar i teak på en villa från 1970-talet",
     "1970s Swedish architect-designed villa with large floor-to-ceiling window sections in natural teak frames, dark stained wooden facade, birch trees reflected in the glass, soft overcast daylight, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SOLLENTUNA
"fonsterbyte-sollentuna.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Sollentuna", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Sollentuna – buller, ljudglas och lov",
  "description": "Fönsterbyte i Sollentuna: bullerglas mot E4, järnvägen och kommunala gator, kommunens bidrag för bullerdämpning, radhus, kulturmiljöer och ROT.",
  "h1": "Fönsterbyte i Sollentuna",
  "lead": "I Sollentuna är det ofta trafiken som får villaägare att se över fönstren. Kommunen konstaterar att en stor del av bullret kommer från E4, järnvägen och flygtrafiken, och för hus vid kommunala gator finns ett bidrag för bullerdämpning. Geal Entreprenad AB byter och renoverar fönster i hela Sollentuna, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Buller, ljudglas och radhus i Sollentuna.",
  "sections": [
    {"id": "buller", "anchor": "Buller och fönster",
     "h2": "E4, järnvägen och flyget – varifrån bullret kommer",
     "paras": [
       "Kommunens regler för bidrag till bulleråtgärder beskriver samhällsbuller som den störning som berör flest människor i Stockholms län. En stor del av Sollentunas bullerproblem kommer enligt kommunen från statens anläggningar: E4, järnvägen och flygrörelserna till och från Arlanda. Dessutom finns flera genomfartsleder, både statliga och kommunala, med betydande vägtrafikbuller.",
       "Kommunen skriver också att skärmar och vallar är väl utbyggda i Sollentuna och att buller ständigt diskuteras i detaljplanearbetet. För den som redan bor nära en trafikled är det ändå fönstren som avgör hur mycket som hörs inomhus, eftersom de är fasadens svagaste del även mot ljud.",
       "Boverkets energiguide påpekar att olika glas och glaskombinationer ger olika mycket bullerdämpning, solavskärmning och dagsljusinsläpp. Ett fönster mot en trafikerad gata kan därför behöva ett annat glas än fönstren mot trädgården.",
     ],
     "aside": {"title": "Bullerkällor enligt kommunen", "items": [
       "E4", "Järnvägen", "Flyget till och från Arlanda", "Statliga och kommunala genomfartsleder"]}},
    {"id": "bullerbidrag", "h2": "Kommunens bidrag för bullerdämpning i bostaden",
     "paras": [
       "Den som störs av buller från kommunala vägar kan söka bidrag hos kommunen. Bidraget kan gälla komplettering av befintliga fönster med en tillsatsruta, byte av fönster eller installation och byte av friskluftsdon. Det kan ges för rum mot och vinkelrätt mot den bullerutsatta sidan, och fönsterytan får vara högst 30 procent av den berörda fasadytan.",
       "Villkoren är att bullret överstiger 55 dBA ekvivalent nivå enligt kommunens bullerkartläggning, att huset är ett en- eller tvåbostadshus som ägaren bor i permanent, att det är byggt före 1997 och att fastigheten inte fått bullerbidrag tidigare. För buller från E4 och järnvägen hänvisar kommunen till Trafikverket, och för flygbuller till Luftfartsverket eller Swedavia.",
       "Bidraget ska sökas och beviljas innan arbetet börjar, och det betalas inte ut i efterhand. Ansökningar tas emot hela året men behandlas i april och maj, ett avtal tecknas innan arbetet startar och åtgärderna ska vara klara och redovisade inom ett år från beslutet. Planerar du att byta fönster mot en kommunal gata är det därför värt att kontrollera bidraget innan beställningen görs.",
     ],
     "aside": {"title": "Villkor i korthet", "items": [
       "Över 55 dBA enligt kartläggningen", "En- eller tvåbostadshus, eget permanent boende",
       "Byggt före 1997", "Ansökan beviljad före start"]}},
    {"id": "tyst-fonster", "h2": "Tillsatsruta, nytt fönster eller nytt friskluftsdon",
     "paras": [
       "En tillsatsruta på insidan av ett befintligt fönster ger en extra glasning utan att fasaden ändras. Boverket beskriver samma princip för energin: en extra båge med energiglas eller en tvåglaskassett på insidan, förutsatt att bågen klarar tyngden och att det finns djup för kompletteringen.",
       "Byts fönstret helt behöver anslutningen mot väggen vara tät, eftersom ljud tar sig igenom springor lika lätt som luft. Boverket påpekar att drevningen och isoleringen mellan karm och vägg ska göras fackmässigt och gärna fotodokumenteras. Ett tätare hus behöver samtidigt tilluft, och ett ljuddämpande friskluftsdon är då en del av lösningen snarare än ett tillägg.",
       "När fönstren och huset blir tätare ändras också ventilationen. I hus med självdrag kan läckage kring de gamla fönstren ha varit en del av tilluften. Ska vinden isoleras samtidigt, eller taket ses över mot vägsidan, se " + _L.format("takrenovering-sollentuna.html", "takrenovering i Sollentuna") + ".",
     ],
     "aside": None},
    {"id": "lov-sollentuna", "h2": "Fönster, radhus och kulturmiljöplanen",
     "paras": [
       "Sollentuna kommun räknar att ändra fönster och dörrar som en fasadändring, och för en- och tvåbostadshus krävs det oftast inget bygglov. I radhus, kedjehus och andra sammanbyggda småhus gäller olika möjligheter beroende på hur bebyggelsen är utformad, och kommunen ber dig då kontakta kontaktcenter. Påverkar ändringen husets bärande stomme kan en konstruktionsritning behövas.",
       "För byggnader och områden som är kulturhistoriskt särskilt värdefulla går de lovbefriade åtgärderna inte att använda. I kommunens karta med gällande detaljplaner finns ett lager som visar områdena i kulturmiljöplanen, men en byggnad kan vara värdefull även om den inte syns där. Vill du ha ett beslut på att bytet uppfyller kraven kan du söka frivilligt bygglov. Läs mer om fasaden runt fönstren under " + _L.format("fasadrenovering-sollentuna.html", "fasadrenovering i Sollentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Sollentuna",
  "steps": [
    ("Besök", "Vi går igenom fönstren, ser vilka rum som vetter mot trafiken och mäter upp varje fönster."),
    ("Bidrag och lov", "Vi ser om huset kan omfattas av bullerbidraget och om kulturmiljöplanen berör fastigheten."),
    ("Förslag per sida", "Glas och åtgärd väljs per fasad, och allt redovisas i ett skriftligt kostnadsförslag."),
    ("Tilluft", "Friskluftsdon eller spaltventiler planeras så att ventilationen fungerar i det tätare huset."),
    ("Montage", "Fönster eller tillsatsrutor monteras med tät drevning, och anslutningarna fotograferas."),
    ("Avslut", "Vi går igenom resultatet och lämnar underlag som kan behövas för kvitton och bidrag."),
  ],
  "rot_h2": "ROT-avdrag för bullerglas och fönster i Sollentuna",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att reparera eller byta ut fönster och att montera bullerglas och isolerglas. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag.",
    "Du behöver äga huset medan arbetet görs och bo i det. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här påverkar priset i Sollentuna",
  "price": [
    "Hur många fönster som vetter mot trafiken, om det räcker med tillsatsrutor eller om fönstren ska bytas, vilket glas som krävs för bullret, hur många friskluftsdon som behövs och hur mycket foder och bleck som görs om. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi få bidrag från Sollentuna kommun för nya fönster mot gatan?",
     "Om bullret kommer från en kommunal väg och överstiger 55 dBA ekvivalent nivå, huset är byggt före 1997 och ni bor där permanent kan ni söka kommunens bidrag. Det ska beviljas innan arbetet börjar."),
    ("Gäller bullerbidraget även buller från E4?",
     "Nej. Kommunens bidrag gäller kommunala gator och vägar. För buller från E4 och järnvägen hänvisar kommunen till Trafikverket."),
    ("Räcker det med en tillsatsruta mot trafikbullret?",
     "Ofta gör det skillnad, och kommunens bidrag kan gälla just tillsatsrutor. Det avgörs av fönstrets skick och hur mycket djup bågen har för ett extra glas."),
    ("Behövs bygglov för att byta fönster i ett radhus i Sollentuna?",
     "Det beror på hur radhusområdet är utformat, och kommunen ber dig kontakta kontaktcenter. Ligger huset inom kulturmiljöplanen krävs lov."),
    ("Varför behövs friskluftsdon när fönstren blir tätare?",
     "Utan läckaget kring de gamla fönstren kan tilluften bli för liten. Ett ljuddämpande friskluftsdon ger frisk luft utan att släppa in bullret."),
  ],
  "sources": [
    ("Sollentuna kommun – Bidrag för bullerdämpning i bostad",
     "https://sollentuna.se/trafik--gator/trafikbuller-och-bullerbidrag/"),
    ("Sollentuna kommun – Information om och regler för bidrag för bulleråtgärder (pdf)",
     "https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/buller/regler-for-bullerbidrag_ny-logga_ny-lank.pdf"),
    ("Sollentuna kommun – Ändra fönster eller dörrar på en- eller tvåbostadshus",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/andra-fonster-eller-dorrar-pa-hus/"),
    ("Sollentuna kommun – Kulturhistoriska byggnader och kulturmiljöer",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/kulturmiljoer/"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Hörs trafiken genom fönstren?", "Boka ett gratis platsbesök så går vi igenom glas, tilluft och kommunens bidrag."),
  "img": [
    ("Villa i Sollentuna med nya vita fönster mot en villagata",
     "1960s Swedish single-storey brick villa with new white wooden windows facing a residential street, low wooden fence and hedge, tall pine trees behind, Sollentuna suburb, soft natural colour, light overcast autumn daylight, green lawn, no people, no cars, no text"),
    ("Tillsatsruta och friskluftsdon på insidan av ett fönster",
     "interior close-up of a white wooden window in a Swedish house with an added inner glass pane mounted on the sash and a small white fresh-air vent above the frame, calm room, soft daylight, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ LIDINGÖ
"fonsterbyte-lidingo.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Lidingö", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte på Lidingö – villastäderna och lovplikten",
  "description": "Fönsterbyte på Lidingö: jugend, tätspröjs och tvåluftsfönster i villastäderna, Breviks villor, stadens blå lager och fönster i originalutförande.",
  "h1": "Fönsterbyte på Lidingö",
  "lead": "I Lidingö villastad och Brevik går det att läsa husens ålder i fönstren: höga helglasade bågar på jugendvillorna, tätt sittande spröjs på nationalromantiken och tvåluftsfönster i fasadliv på 1930- och 40-talens villor. Geal Entreprenad AB byter och renoverar fönster på hela Lidingö, kontrollerar stadens lovplikt innan något beställs och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Villastäderna och Brevik på Lidingö.",
  "sections": [
    {"id": "villastaden", "anchor": "Fönstren på Lidingö",
     "h2": "Från helglasade bågar till tvåluftsfönster i fasadliv",
     "paras": [
       "Kulturmiljöprogrammets beskrivning av Lidingö villastad följer stilarna decennium för decennium. De äldre villorna är främst byggda i jugend, med höga tak i rött lertegel, tunga socklar i natursten och höga fönster med helglasade bågar och burspråk. Från omkring 1910 skiftade stilen mot nationalromantik, med fönster med tätt sittande spröjs, fönsterluckor, loggior och burspråk.",
       "Under 1920-talet byggdes villorna i klassicerande form. Fönstren blev större än tidigare, med tvåluftsfönster som hade tre rutor per båge i bottenplanet och två rutor per båge i övre planet. Villorna från 1930- och 1940-talen har en försiktig modernism, slätputsade fasader och främst tvåluftsfönster placerade i fasadlivet.",
       "Skillnaden mellan våningarna på 1920-talsvillorna är värd att lägga märke till. Byts fönstren mot ett och samma format på båda planen försvinner en detalj som arkitekten avsiktligt ritade in.",
     ],
     "aside": {"title": "Fönstren i villastaden", "items": [
       "Jugend: höga, helglasade bågar", "Från 1910: tätt sittande spröjs",
       "1920-tal: tre rutor nere, två uppe", "1930–40-tal: tvåluftsfönster i fasadliv"]}},
    {"id": "brevik", "h2": "Brevik – tätspröjs, souterräng och en- och tvåluftsfönster",
     "paras": [
       "I Breviks villastad beskriver programmet två parvillor från 1912 i kvarteret Trädgården med ljusa slätputsade fasader och tätspröjsade fönster, och en villa i kvarteret Rapsen med drag av italiensk klassicism och jugend, symmetrisk fasad och tätspröjsade fönster. De äldre villorna står i ett och ett halvt till två våningar under branta sadeltak med tegel, skiffer eller plåt.",
       "Villorna från 1940- och 1950-talen är ofta byggda i ett och ett halvt plan i souterräng, med ljusa putsfasader, tidstypiskt smide och en- och tvåluftsfönster. På ett souterränghus sitter fönstren i nedre planet nära marken, och där behöver anslutningen mot sockeln och fönsterblecket särskild omsorg.",
       "För både villastaden och Brevik ger programmet rådet att äldre byggnadsdetaljer ska värnas, till exempel fönster och dörrar i originalutförande, och att byggnaderna ska underhållas med väl anpassade material och metoder.",
     ],
     "aside": None},
    {"id": "lov-lidingo", "h2": "Stadens blå lager och skyddsbestämmelserna",
     "paras": [
       "Lidingö stad skriver att bygglov för fasadändringar på en- och tvåbostadshus har slopats utanför de värdefulla områdena, men att utökad lovplikt gäller för de flesta byggnadsåtgärder inom särskilt kulturhistoriskt värdefulla områden. I stadens webbkarta visas de områdena som ett blått lager. Är fastigheten gulmarkerad kan det finnas värden som behöver bedömas, och då hänvisar staden till sitt kundcenter.",
       "Kulturmiljöprogrammets första del, en handbok för fastighetsägare, förklarar hur en detaljplan kan styra fönstren. En utformningsbestämmelse kan ange hur fönstren ska utformas för att passa befintlig bebyggelse, och en skyddsbestämmelse kan skydda det faktiska materialet och reglera hur underhållet ska utföras och med vilken teknik.",
       "Handboken beskriver också varsamhetskravet, som gäller även utan lov, som ett förhållningssätt där varje ändring utgår från byggnadens karaktärsdrag – till exempel fönstrens utformning. Råden i områdesbeskrivningarna är inte juridiskt bindande, men staden använder dem som stöd i bygglovsärenden.",
     ],
     "aside": {"title": "Kontrollera i detaljplanen", "items": [
       "Blått eller gult i webbkartan?", "Utformningsbestämmelse om fönster?",
       "Skyddsbestämmelse för materialet?", "Krav på hur underhåll görs?"]}},
    {"id": "renovera-lidingo", "h2": "Renovera originalfönstren eller byta",
     "paras": [
       "Eftersom programmet vill att fönster i originalutförande värnas börjar vi med att bedöma om de befintliga fönstren kan renoveras. Boverket skriver att det ofta är mer lönsamt att förbättra fönster i gott skick än att byta, och att det kräver mindre naturresurser. Tätningslister, drevning, kittning och målning, och ett energiglas i innerbågen, kan göra stor skillnad.",
       "Är fönstren i så dåligt skick att de behöver bytas bör de nya anpassas till husets ålder och karaktär, med samma indelning och liknande profiler. Boverket påminner om att grövre fönstersnickerier släpper in mindre dagsljus och att nya fönster ofta blir tyngre, så att gångjärn och beslag behöver kontrolleras.",
       "Fönstersnickerierna behöver målas oftare än resten av fasaden, se " + _L.format("malare-lidingo.html", "målare på Lidingö") + ". Ska fasaden eller taket runt fönstren också ses över finns mer under " + _L.format("fasadrenovering-lidingo.html", "fasadrenovering på Lidingö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett fönsterbyte på Lidingö till",
  "steps": [
    ("Platsbesök", "Vi bedömer varje fönster, mäter upp det och noterar indelning, spröjs och profiler."),
    ("Webbkarta och plan", "Stadens blå och gula markeringar och detaljplanens bestämmelser kontrolleras."),
    ("Renovera eller byta", "Fönster för fönster avgör vi vad som kan renoveras och vad som behöver bytas."),
    ("Skriftligt förslag", "Renovering, nya fönster, glas och montage står var för sig i förslaget."),
    ("Utförande", "Bågar renoveras eller nya fönster monteras med drevning, tätning och bleck."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och visar hur fönstren sköts."),
  ],
  "rot_h2": "ROT-avdrag för fönster på Lidingö",
  "rot": [
    "För ett småhus räknar Skatteverket det som rotarbete att reparera eller byta ut fönster, montera isolerglas, byta fönsterbleck och måla fönster. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Solfilm och myggnät ger inget avdrag.",
    "Material och resor räknas inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden på Lidingö",
  "price": [
    "Hur många fönster som kan renoveras och hur många som måste bytas, om spröjs och profiler ska tillverkas efter förlaga, vilket glas som väljs, om fönster i souterrängplanet kräver nya bleck och anslutningar och om arbetet kräver ställning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Krävs bygglov för nya fönster i Lidingö villastad?",
     "Ligger fastigheten i stadens blå lager gäller utökad lovplikt för de flesta åtgärder, och då kan ett fönsterbyte kräva lov. Är fastigheten gulmarkerad bör du kontakta stadens kundcenter."),
    ("Hur var fönstren indelade på Lidingös villor från 1920-talet?",
     "Enligt kulturmiljöprogrammet hade de tvåluftsfönster med tre rutor per båge i bottenplanet och två rutor per båge i övre planet."),
    ("Kan en skyddsbestämmelse styra hur fönstren underhålls?",
     "Ja. Stadens handbok beskriver att en skyddsbestämmelse kan skydda materialet och reglera hur underhållet ska utföras och med vilken teknik."),
    ("Är råden i Lidingös kulturmiljöprogram bindande?",
     "Nej, råden i områdesbeskrivningarna är inte juridiskt bindande. Staden använder dem som stöd vid bygglov och planärenden, och varsamhetskravet i lagen gäller även när inget lov krävs."),
    ("Vad behöver vi tänka på med fönstren i ett souterränghus i Brevik?",
     "Fönstren i nedre planet sitter nära marken, så sockelns anslutning, fönsterblecket och fuktskyddet under fönstret behöver kontrolleras särskilt."),
  ],
  "sources": [
    ("Lidingö stad – Ändrade lagar och regler för byggande",
     "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/"),
    ("Lidingö stad – Kulturmiljöprogram del 1: Handbok för fastighetsägare (pdf)",
     "https://share.mediaflow.com/sv/?7ZCCF1REBX"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Lidingö villastad (pdf)",
     "https://share.mediaflow.com/sv/?9OCCB1KE1L"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Breviks villastad (pdf)",
     "https://share.mediaflow.com/sv/?70CCS1CE0X"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren på Lidingövillan bytas?", "Boka ett gratis platsbesök så bedömer vi vilka fönster som kan renoveras och vilka som behöver bytas."),
  "img": [
    ("Jugendvilla på Lidingö med höga fönster och rött tegeltak",
     "two-storey early 1900s Swedish Art Nouveau villa of moderate size with light plastered facade, tall white wooden windows with large undivided glass panes, one bay window, high red clay tile roof, heavy grey natural stone plinth, plain facade without plaques or inscriptions, mature oak and pine trees, Lidingö Stockholm, spring daylight, no people, no text"),
    ("Tätspröjsat fönster på en putsad villa från 1910-talet",
     "close-up of a small-paned white wooden window with many glazing bars and green wooden shutters on a light smooth plastered wall of a 1910s Swedish national romantic villa, full-bleed photo filling the whole frame, soft daylight, no people, no text"),
  ],
  "related": [],
},
}
