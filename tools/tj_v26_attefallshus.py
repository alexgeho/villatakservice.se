# -*- coding: utf-8 -*-
"""Attefallshus – ortsidor v26: Enskede, Farsta, Hägersten, Hässelby, Spånga, Vällingby (2026-10-26).
Hubb: attefallshus.html (TJ_HUB["attefallshus"]). Regelartikel: attefallshus-regler.html.
Struktur som tj_v22_attefallshus.py. Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.

Fakta endast från källorna i respektive 'sources', öppnade med curl (UA Mozilla) 2026-10-26, alla svarade 200:
  bygglov.stockholm – Komplementbostadshus (bygglovsbefriad), uppdaterad 2026-10-21: 30,0 m² BYA, mindre än
    huvudbyggnaden, nock 4,0 m, inom tomten, pott 45,0 m² där tidigare attefallshus och friggebodar räknas in, får strida
    mot detaljplanen (prickmark), 4,5 m från gräns mot granne/samfällighet/allmän plats, skriftligt medgivande
    (fastighetsbeteckning, åtgärd, situationsplan, underskrifter), 30 m från järnvägsspår, anmälan och startbesked för
    vatten och avlopp/ventilation/eldstad, bygglov vid särskilt kulturhistoriskt värdefull byggnad/tomt/område.
  bygglov.stockholm – Stadsmuseets kulturhistoriska klassificering: bygglov krävs inom riksintresse (blå ring), inom
    särskilt kulturhistoriskt värdefullt område i översiktsplanen (grön ring), om byggnaden är blå- eller grönmarkerad;
    gult/grått kräver inget lov om inget annat gäller; streckade ytor = ännu inte inventerade.
  Varsam utveckling av småhus- och villaområden (pdf, textlager): tabellen s. 85 (Gamla Enskede riksintresse + KV +
    äldre miljöprogram + generösa byggrätter; Enskede gård KV; Enskedefältet KV + miljöprogram; Tallkrogen KV +
    miljöprogram; del av Svedmyra KV; del av Sköndal KV; Mälarhöjden KV + generösa byggrätter; Hässelby villastad,
    Bromsten, Nälsta, Flysta, Sundby utan markering; Solhem KV; Hässelby strand KV; Hässelby gård KV; Vällingby och
    Råcksta riksintresse + KV; Grimsta KV; Kälvesta storskalig stadsdel utan markering), texterna om trädgårdsstad
    (komplementbyggnader, Gamla Enskede första trädgårdsstaden), villastad (stationssamhällen Spånga och Älvsjö, Mälar-
    höjden privat initiativ, Solhem tiondel av tomten, tomter 1 500–3 000 m², 1960–70-talen i Hässelby villastad,
    tomter kring 600 m²), tunnelbanestad (Vällingby 1954, Atlantis och Omega synnerligen värdefulla, Vällingby-Råcksta
    riksintresse) och storskalig stadsdel (Kälvesta egen småhusstadsdel).
  Stockholm Vatten och Avfall – Anslut till vatten och avlopp: servisanmälan med ritning, vattenledning efter mätaren,
    spillvatten till befintlig spillvattenledning inom tomten, gärna via rensbrunn, dag- och dräneringsvatten inte till
    spillvatten, vattentrycket kan bli sämre högre upp och längre bort, kök/pentry + toalett = egen bostad i VA-taxan.
  Stockholms stadsmuseum, Stockholms spår: Tallkrogen (pdf, textlager): utbyggnad från 1933, största småstugeområdet i
    Söderort, närmare 1 000 småstugor, mer än 10 hustyper, flack åkermark; Farsta (pdf): radhusområden i utkanterna.
  Områdesfakta 2025 (pdf, textlager): bostäder i småhus med äganderätt – Gamla Enskede 898, Enskedefältet 405,
    Enskede gård 417, Tallkrogen 941, Sköndal 1 194, Farsta stadsdelsområde 3 806, Mälarhöjden 988, Hässelby villastad
    4 757 (av 7 029 bostäder), Hässelby strand se pdf, Solhem 1 946, Bromsten 916, Flysta 657, Vinsta 826, Nälsta
    1 297, Kälvesta 1 492, Vällingby 220.
  Skatteverket – Ger arbetet rätt till rotavdrag? (läst via WebFetch – curl återställs): aldrig rotavdrag för att
    bygga en helt ny bostad, inte för ett helt nytt hus, friggebod, garage eller liknande fristående byggnad.
Strukna / ej använda: avgifter och taxor (SVOA:s anläggnings- och bostadsenhetsavgift nämns bara som att en avgift
tillkommer), handläggningstider, vilka järnvägar som går genom Spånga (texten säger bara att stationssamhället växte
vid järnvägen och att 30-metersregeln gäller nära spår), om radhus räknas som en- eller tvåbostadshus (ingen källa –
inget sagt), stadsdelstillhörighet utöver områdesfaktas egen indelning.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no text, no letters"
_REG = _L.format("attefallshus-regler.html", "reglerna för attefallshus")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"

_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 9 kap.",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_STH_KBH = ("Stockholms stad – Komplementbostadshus (bygglovsbefriad)",
            "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/komplementbostadshus-bygglovsbefriad/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/stadsmuseets-kulturhistoriska-klassificering/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_SVOA = ("Stockholm Vatten och Avfall – Anslut till vatten och avlopp",
         "https://www.svoa.se/villa-och-radhus/vatten-och-avlopp/bygga-om/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_TALLK = ("Stockholms stadsmuseum – Stockholms spår: Tallkrogen (pdf)",
          "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000041.pdf")
_FARSTA = ("Stockholms stadsmuseum – Stockholms spår: Farsta (pdf)",
           "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000015.pdf")


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_ROT_NY = ("Skatteverket skriver att det inte går att få rotavdrag för att bygga en helt ny bostad, och inte heller "
           "för ett nytt hus, en friggebod, ett garage eller en liknande fristående byggnad. Ett komplementbostadshus "
           "står fritt på tomten, så kostnadsförslaget för huset räknas utan avdrag.")

PAGES_TJ = {

# ------------------------------------------------------------------ ENSKEDE
"attefallshus-enskede.html": {
  "kind": "district", "service": "attefallshus", "ort": "Enskede", "svc_label": "Attefallshus",
  "title": "Attefallshus i Enskede – trädgårdsstaden och lovet",
  "description": "Attefallshus i Enskede: när Gamla Enskede, Enskede gård och Enskedefältet kräver bygglov, Stadsmuseets karta, förgårdsmarken och vattnet till huset.",
  "h1": "Attefallshus i Enskede",
  "lead": "I Enskede avgör kartan mer än måttbandet. Gamla Enskede är riksintresse, och Enskede gård och Enskedefältet är utpekade som kulturhistoriskt värdefulla miljöer – där kan ett hus som annars är lovfritt kräva bygglov. Geal Entreprenad AB kontrollerar tomten först och bygger sedan komplementbostadshuset nyckelfärdigt.",
  "card": "Trädgårdsstaden, kartan och lovet.",
  "sections": [
    {"id": "kartan-enskede", "anchor": "Kartan först",
     "h2": "Börja med Stadsmuseets karta",
     "paras": [
       "Stockholms stad beskriver tydligt när ett komplementbostadshus kräver bygglov trots att måtten håller. Ligger tomten inom ett riksintresse för kulturmiljövården – en blå ring i Stadsmuseets klassificeringskarta – eller inom ett område som översiktsplanen pekar ut som särskilt kulturhistoriskt värdefullt – en grön ring – behövs lov. Samma sak gäller om huset på tomten är markerat med blått eller grönt. Gult eller grått kräver inget lov, om inget annat gäller.",
       "Stadens vägledning Varsam utveckling av småhus- och villaområden listar Gamla Enskede som riksintresse, kulturhistoriskt värdefull miljö och område med äldre miljöprogram. Enskede gård och Enskedefältet står som kulturhistoriskt värdefulla miljöer. Vi slår därför upp just din fastighet innan vi ritar något. Står den på en streckad yta är miljön ännu inte inventerad, och då kan Stadsmuseet behöva göra en bedömning.",
     ],
     "aside": {"title": "Färgerna i kartan", "items": [
       "Blå ring – riksintresse, lov krävs", "Grön ring – särskilt värdefullt område",
       "Blå eller grön byggnad – lov krävs", "Gult eller grått – inget lov i sig"]}},
    {"id": "tradgardsstaden-enskede", "h2": "Ett hus som passar i trädgårdsstaden",
     "paras": [
       "Gamla Enskede var enligt vägledningen Stockholms första trädgårdsstad. Vägledningen ber fastighetsägare i trädgårdsstaden att tänka på gatumönstret – om husen står i gatuliv eller med förgårdsmark – och på områdets gröna karaktär med träd, häckar och trädgårdar. Vägledningen konstaterar att det redan har byggts garage, carportar och förråd på tomterna och att det har skett förtätning, främst i stadsdelarnas utkanter men också inne i den ursprungliga strukturen, till exempel i Enskede gård.",
       "För ett nytt komplementbostadshus betyder det att placeringen på tomten spelar roll. Vi föreslår normalt en plats längre in på tomten, i samma linje som andra gårdshus, och en enkel volym med sadeltak och träpanel som underordnar sig villan. Krävs bygglov blir det byggnadsnämnden som prövar utformningen, och då är det bra att redan från början ha ritat huset med hänsyn till gaturummet och trädgården.",
     ],
     "aside": None},
    {"id": "potten-enskede", "h2": "Måtten och potten på tomten",
     "paras": [
       "Där inget utökat lovkrav gäller får ett komplementbostadshus vara högst 30,0 kvadratmeter byggnadsarea och 4,0 meter i nock. Det ska vara mindre än huset det kompletterar och stå inom tomten. Alla lovfria komplementbyggnader på tomten får tillsammans vara högst 45,0 kvadratmeter, och staden påpekar att äldre attefallshus och friggebodar ska räknas in.",
       "Många tomter i Enskedefältet och Gamla Enskede är små. Avståndet på 4,5 meter till gräns mot granne, gata eller park blir därför ofta svårt att klara, och då behövs skriftliga medgivanden. För gatu- och parkmark är det oftast staden som ska ge medgivandet, och förfrågan skickas till stadsbyggnadskontoret. Får du inte medgivandet blir det i stället en bygglovsansökan. Tänk också på att ett lovfritt hus får stå på prickmark enligt staden, men att det inte hjälper där miljön ändå kräver lov.",
     ],
     "aside": {"title": "Utan lov – om inget annat gäller", "items": [
       "Högst 30,0 m² byggnadsarea", "Högst 4,0 m i nock", "Pott 45,0 m² på tomten",
       "4,5 m till gräns eller medgivande"]}},
    {"id": "va-enskede", "h2": "Vatten och avlopp till gårdshuset",
     "paras": [
       "Ska huset få kök och toalett behövs en anmälan och ett startbesked innan installationerna görs, oavsett om bygglov krävs. Stockholm Vatten och Avfall vill dessutom ha en servisanmälan med en ritning över ledningsdragningen i god tid före byggstart. Den nya vattenledningen ska kopplas efter vattenmätaren i villan, och spillvattnet ska ledas till den befintliga spillvattenledningen inom tomten – gärna via en rensbrunn.",
       "Har gårdshuset både kök eller pentry och toalett räknas det som en egen bostad i VA-taxan, och då tillkommer en avgift som ska vara betald innan huset kopplas in. Dag- och dräneringsvatten från det nya taket får inte ledas till spillvattnet. I Enskede finns enligt områdesfakta 898 småhus med äganderätt i Gamla Enskede, 417 i Enskede gård och 405 i Enskedefältet, så frågan om att dela ledningar med villan kommer upp på många tomter. Vill du hellre bygga ihop med huset beskriver vi det under " + _L.format("tillbyggnad-enskede.html", "tillbyggnad i Enskede") + ". Måtten och paragraferna finns samlade i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Enskede",
  "steps": [
    ("Kartan", "Riksintresse, gröna ringar och husets färg i Stadsmuseets karta kontrolleras först."),
    ("Platsbesök", "Vi mäter befintliga gårdshus, avstånd till gränser och var ledningarna går."),
    ("Lov eller anmälan", "Bygglov där miljön kräver det, annars anmälan för installationerna."),
    ("Servisanmälan", "Ritning över vatten och avlopp skickas till Stockholm Vatten och Avfall."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset tas i bruk när slutbeskedet har kommit."),
  ],
  "rot_h2": "Inget rotavdrag för ett nytt gårdshus",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Enskede?",
  "price": [
    "Om bygglov och ritningar för en kulturmiljö behövs, husets storlek och planlösning, kök och badrum, grundläggning, hur långt ledningarna ska dras och hur material kan bäras in på en tät tomt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för ett attefallshus i Gamla Enskede?",
     "Gamla Enskede är riksintresse för kulturmiljövården. Staden skriver att bygglov krävs för åtgärder inom ett riksintresse, även för sådant som annars är lovfritt."),
    ("Vad betyder en streckad yta i Stadsmuseets karta i Enskede?",
     "Att miljön ännu inte är inventerad. Då kan bygglov ändå krävas, och Stadsmuseet kan göra en bedömning om du skickar adress, byggår och foton."),
    ("Får gårdshuset i Enskede kopplas på villans vattenledning?",
     "Ja, enligt Stockholm Vatten och Avfall ska den nya vattenledningen kopplas efter vattenmätaren och spillvattnet till befintlig spillvattenledning på tomten. En servisanmälan med ritning krävs."),
    ("Räknas vårt gamla garage i Enskede in i de 45 kvadratmetrarna?",
     "Ja, om det är byggt utan lov enligt äldre eller nuvarande regler. Staden skriver att tidigare lovfria komplementbyggnader ska räknas in i den sammanlagda arean."),
  ],
  "sources": [_STH_KBH, _STH_KLASS, _VARSAM, _SVOA, _of("Gamla Enskede", "soderort/enskede/gamla-enskede"),
              _of("Enskede gård", "soderort/enskede/enskede-gard"), _of("Enskedefältet", "soderort/enskede/enskedefaltet"),
              _PBL, _SKV],
  "cta": ("Vill du bygga ett gårdshus i Enskede?", "Boka ett gratis platsbesök, så går vi igenom kartan, måtten och vattnet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet gårdshus med röd träpanel och sadeltak längst in i en lummig trädgård bakom en äldre villa",
     "small new Swedish garden cottage with red vertical wooden cladding, white window frames and a gable roof with red clay tiles at the back of a lush garden behind a 1910s yellow wooden villa with white trim, fruit trees and lilac bushes, Stockholm garden city, early summer daylight" + _SFX),
    ("Rensbrunn i en gräsmatta mellan en villa och ett nybyggt gårdshus",
     "round grey plastic inspection chamber lid for a drain set flush in a lawn on a garden path between an older wooden villa and a newly built small timber guest house, gravel path, garden tools absent, overcast daylight" + _SFX),
    ("Gata i en trädgårdsstad med häckar, förgårdar och träd framför äldre villor",
     "quiet street in a Swedish 1910s garden city with clipped hedges, small front gardens and mature trees in front of individually designed wooden villas in muted colours, no cars, soft morning light" + _SFX),
  ],
},

# ------------------------------------------------------------------ FARSTA
"attefallshus-farsta.html": {
  "kind": "district", "service": "attefallshus", "ort": "Farsta", "svc_label": "Attefallshus",
  "title": "Attefallshus i Farsta – småstugor och radhustomter",
  "description": "Attefallshus i Farsta: när huvudbyggnaden är en liten småstuga i Tallkrogen, kulturmiljöerna i Svedmyra och Sköndal, grannmedgivanden och servisanmälan.",
  "h1": "Attefallshus i Farsta",
  "lead": "I Farsta står många småhus på tomter i Tallkrogen, Sköndal och Svedmyra där huvudbyggnaden själv är ganska liten. Det påverkar hur stort ett attefallshus får bli. Geal Entreprenad AB räknar på villans yta, gränserna och miljön innan vi föreslår ett hus och bygger det sedan nyckelfärdigt.",
  "card": "Småstugor, kulturmiljö och gränser.",
  "sections": [
    {"id": "smastugor-farsta", "anchor": "Småstugorna",
     "h2": "När huvudbyggnaden är en småstuga",
     "paras": [
       "Stadsmuseets skrift om Tallkrogen beskriver hur utbyggnaden började 1933 och hur området blev det största småstugeområdet i Söderort. Närmare 1 000 småstugor växte upp på flack åkermark under ungefär ett decennium. Husen var standardiserade, men skriften räknar mer än tio olika hustyper, och den som byggde kunde ersätta kontantinsatsen med eget arbete.",
       "Lagen säger att ett lovfritt komplementbostadshus ska ha en byggnadsarea som är mindre än det hus det kompletterar. På en tomt med en liten småstuga blir det ofta den regeln – inte 30 kvadratmeter – som sätter gränsen. Vi mäter därför byggnadsarean på stugan och eventuella tillbyggnader innan vi ritar. Ibland är det bättre att " + _L.format("tillbyggnad.html", "bygga till stugan") + " först och komplementbostadshuset sedan.",
     ],
     "aside": {"title": "Två gränser samtidigt", "items": [
       "Högst 30,0 m² byggnadsarea", "Mindre än huset på tomten", "Högst 4,0 m i nock", "Pott 45,0 m²"]}},
    {"id": "kulturmiljo-farsta", "h2": "Tallkrogen, Svedmyra och Sköndal i kartan",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden markerar Tallkrogen som kulturhistoriskt värdefull miljö med ett äldre miljöprogram. Delar av Svedmyra och Sköndal står också som kulturhistoriskt värdefulla. Om din tomt ligger inom en grön eller blå ring i Stadsmuseets klassificeringskarta, eller om huset är markerat med blått eller grönt, krävs bygglov även för ett hus som annars hade varit lovfritt.",
       "I Tallkrogen är gatumönstret speciellt – gatorna lades ut som löparbanor runt en idrottsarena och har namn som Maratonvägen och Olympiavägen. Det gör gaturummen enhetliga, och ett nytt gårdshus syns från gatan om det står fel. Vi placerar det hellre bakom stugan och håller det lågt, med samma takvinkel och färgskala som stugorna.",
     ],
     "aside": None},
    {"id": "radhus-farsta", "h2": "Radhusområdena i utkanterna",
     "paras": [
       "Farsta byggdes som den första ABC-staden i Söderort och invigdes 1960. Enligt Stadsmuseet lades flera stora radhusområden i stadsdelens utkanter. På sådana tomter är friytan mot grannarna liten, och avståndet 4,5 meter till gränsen går sällan att klara. Då behövs skriftliga medgivanden från alla berörda grannar med situationsplan, fastighetsbeteckning och underskrifter, eller en bygglovsansökan.",
       "Områdesfakta för 2025 visar att det finns 3 806 småhus med äganderätt i Farsta stadsdelsområde, varav 941 i Tallkrogen och 1 194 i Sköndal. Hör ditt radhus till en samfällighet räknas även gränsen mot samfälld mark, och då bör samfällighetens styrelse vara med tidigt. Det går också att söka frivilligt bygglov om du vill ha ett beslut på placeringen.",
     ],
     "aside": {"title": "Medgivandet ska innehålla", "items": [
       "Fastighetsbeteckning", "Vilken åtgärd det gäller", "Situationsplan med avstånd", "Underskrifter från grannarna"]}},
    {"id": "va-farsta", "h2": "Vatten, avlopp och installationer",
     "paras": [
       "Ett gårdshus med pentry, dusch och toalett kräver anmälan och startbesked innan vatten, avlopp och ventilation installeras. Till Stockholm Vatten och Avfall skickas en servisanmälan med en ritning över ledningarna. Den nya vattenledningen kopplas efter mätaren i huvudbyggnaden, och spillvattnet ansluts till den befintliga spillvattenledningen inom tomten.",
       "Dagvatten från gårdshusets tak ska inte ledas till spillvattnet. På en flack tomt som i Tallkrogen behöver vi därför planera var vattnet från taket ska ta vägen redan när huset placeras, så att det inte blir stående mot grunden eller rinner över till grannen. Måtten och reglerna i sin helhet beskrivs i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Farsta",
  "steps": [
    ("Mätning", "Byggnadsarean på stugan eller radhuset mäts så att det nya huset blir mindre."),
    ("Kartan", "Kulturmiljöer i Tallkrogen, Svedmyra och Sköndal kontrolleras."),
    ("Grannarna", "Medgivanden tas fram med situationsplan när huset hamnar närmare än 4,5 meter."),
    ("Anmälan", "Installationerna anmäls och servisanmälan skickas innan bygget."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset används när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag och gårdshuset",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Farsta?",
  "price": [
    "Husets storlek i förhållande till stugan, om bygglov behövs, kök och badrum, grund och markförhållanden, avståndet till befintliga ledningar och hur material kan köras in på en smal tomt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur stort attefallshus får vi bygga bredvid en småstuga i Tallkrogen?",
     "Högst 30 kvadratmeter, och dessutom mindre än stugan. Är stugans byggnadsarea liten blir det den som sätter gränsen."),
    ("Krävs bygglov för attefallshus i Tallkrogen?",
     "Tallkrogen är utpekad som kulturhistoriskt värdefull miljö i stadens vägledning. Ligger tomten inom en grön eller blå ring i Stadsmuseets karta krävs bygglov."),
    ("Vem ska godkänna ett gårdshus nära gränsen i ett radhusområde i Farsta?",
     "Alla berörda grannar, och samfälligheten om gränsen går mot samfälld mark. Medgivandet ska vara skriftligt och ha en situationsplan."),
    ("Kan vi få ett beslut i förväg trots att huset är lovfritt i Farsta?",
     "Ja, genom ett frivilligt bygglov. Då prövar byggnadsnämnden huset innan det byggs."),
    ("Var ska regnvattnet från ett gårdshus i Tallkrogen ta vägen?",
     "Inte till spillvattenledningen. Dag- och dräneringsvatten ska enligt Stockholm Vatten och Avfall hållas skilt från spillvattnet, så vi planerar avledningen när huset placeras."),
  ],
  "sources": [_TALLK, _FARSTA, _VARSAM, _STH_KBH, _STH_KLASS, _SVOA,
              _of("Farsta stadsdelsområde", "soderort/farsta/farsta-stadsdelsomrade"),
              _of("Tallkrogen", "soderort/farsta/tallkrogen"), _of("Sköndal", "soderort/farsta/skondal"), _PBL, _SKV],
  "cta": ("Funderar du på ett gårdshus i Farsta?", "Boka ett gratis platsbesök, så mäter vi stugan, gränserna och ledningarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Liten småstuga med brant sadeltak och ett ännu mindre nybyggt gårdshus i trädgården",
     "small 1930s Swedish cottage with steep gable roof and light green wooden panel next to an even smaller newly built light grey timber guest house with a gable roof at the back of the flat garden, picket fence, apple tree, Stockholm suburb, summer afternoon" + _SFX),
    ("Rad av likadana småstugor längs en rak villagata",
     "row of similar small 1930s Swedish cottages with steep gable roofs in pastel colours along a straight flat suburban street with low hedges and picket fences, summer daylight" + _SFX),
    ("Bostadslänga i rött tegel med små trädgårdar mot en gräsyta och björkar",
     "Scandinavian 1960s single-storey and two-storey terraced row houses in Sweden, flat red brick facades with large windows, no door canopies, low pitched roofs, small fenced gardens facing a common lawn with birch trees, Stockholm suburb, soft evening light, full frame photo without borders" + _SFX),
  ],
},

# ------------------------------------------------------------------ HÄGERSTEN
"attefallshus-hagersten.html": {
  "kind": "district", "service": "attefallshus", "ort": "Hägersten", "svc_label": "Attefallshus",
  "title": "Attefallshus i Hägersten – Mälarhöjdens sluttningar",
  "description": "Attefallshus i Hägersten: Mälarhöjdens villastad i stadens karta, kuperade tomter, vattentrycket till ett hus högre upp och reglerna för gränsen.",
  "h1": "Attefallshus i Hägersten",
  "lead": "Mälarhöjden och villorna på Hägerstensåsen ligger på kuperad mark, och det märks när ett gårdshus ska placeras och kopplas till vatten och avlopp. Geal Entreprenad AB börjar med kartan och terrängen och bygger sedan komplementbostadshuset nyckelfärdigt.",
  "card": "Kuperad villastad och vattentryck.",
  "sections": [
    {"id": "malarhojden", "anchor": "Mälarhöjden",
     "h2": "Mälarhöjden – värdefull miljö med stora byggrätter",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur villasamhällen som Mälarhöjden växte upp genom privata initiativ efter större markförvärv. I vägledningens tabell står Mälarhöjden både som kulturhistoriskt värdefull miljö och som område med generösa byggrätter. Områdesfakta för 2025 räknar 988 småhus med äganderätt i Mälarhöjden.",
       "Generösa byggrätter betyder att detaljplanen ofta tillåter mycket, men det säger inget om lovplikten. Om tomten ligger inom en grön eller blå ring i Stadsmuseets klassificeringskarta, eller om villan är markerad med blått eller grönt, krävs bygglov även för ett komplementbostadshus som annars är lovfritt. Vi kontrollerar kartan för just din fastighet först.",
     ],
     "aside": None},
    {"id": "terrangen-hagersten", "h2": "Terrängen styr placeringen",
     "paras": [
       "Vägledningen lyfter fram att villastädernas hus är anpassade till terrängen, ofta med fritt liggande hus i trädgårdar och höjdpartier som lämnats obebyggda. Den nämner också att en tillbyggd villa i Mälarhöjden är ett exempel på hur förändringar kan smälta in. Ett gårdshus på en sluttning behöver därför få en grund som följer marken i stället för stora utfyllnader och stödmurar.",
       "Vi tittar på var berget går i dagen, var marken är lös och hur regnvattnet rinner, och vi räknar med att material kan behöva bäras upp för trappor och branter. Ett hus som placeras högt upp på tomten kan få fin utsikt, men det kräver ofta en längre och dyrare väg för ledningarna. På Hägerstensåsen byggdes enligt Stadsmuseet villor på åsens norra del medan staden byggde smalhus på sin mark, så tomterna där varierar mycket.",
     ],
     "aside": {"title": "Vi kontrollerar", "items": [
       "Berg i dagen och lös mark", "Hur regnvattnet rinner", "Höjden mot förbindelsepunkten",
       "Avstånd till gränser"]}},
    {"id": "vattentryck-hagersten", "h2": "Vatten till ett hus högre upp",
     "paras": [
       "Stockholm Vatten och Avfall påpekar att vattentrycket kan bli sämre om en ny byggnad ligger högre upp och längre bort från förbindelsepunkten vid tomtgränsen. På en kuperad tomt i Mälarhöjden är det en verklig fråga. Den nya vattenledningen ska kopplas efter vattenmätaren i villan, och spillvattnet ska gå till den befintliga spillvattenledningen inom tomten – gärna via en rensbrunn.",
       "Om huset ligger lägre än villans avlopp kan det i stället behövas en pump. Därför ritar vi höjderna innan servisanmälan skickas, och den ska ha en ritning över ledningsdragningen. Har huset både kök eller pentry och toalett räknas det som en egen bostad i VA-taxan, och då tillkommer en avgift innan inkopplingen.",
     ],
     "aside": None},
    {"id": "granser-hagersten", "h2": "Gränser, prickmark och anmälan",
     "paras": [
       "Ett lovfritt komplementbostadshus får enligt staden strida mot detaljplanen och stå på prickmark, men det ska hålla 4,5 meter till gränsen mot granne, samfällighet och allmän plats om inte berörda har gett ett skriftligt medgivande. Mot gatu- och parkmark är det oftast staden som är huvudman. Huset ska också vara högst 30,0 kvadratmeter, 4,0 meter i nock och mindre än villan, och alla lovfria gårdshus på tomten får tillsammans vara högst 45,0 kvadratmeter.",
       "Installationer av vatten, avlopp, ventilation eller eldstad ska anmälas, och arbetet får börja först efter startbesked. Hur större utbyggnader av själva villan prövas beskriver vi under " + _L.format("tillbyggnad-hagersten.html", "tillbyggnad i Hägersten") + ", och lagtexten finns sammanfattad i " + _REG + ".",
     ],
     "aside": {"title": "Utan lov – om inget annat gäller", "items": [
       "Högst 30,0 m² och 4,0 m", "Mindre än villan", "Pott 45,0 m²", "4,5 m till gräns eller medgivande"]}},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Hägersten",
  "steps": [
    ("Kartan", "Vi kontrollerar Stadsmuseets klassificering för fastigheten och villan."),
    ("Terrängen", "Höjder, berg och vattnets väg mäts in vid ett gratis platsbesök."),
    ("Ledningarna", "Vatten och avlopp ritas med höjder och skickas med servisanmälan."),
    ("Anmälan eller lov", "Installationer anmäls; bygglov söks där miljön kräver det."),
    ("Bygget", "Grund anpassad till marken, stomme, tak och installationer."),
    ("Slutbesked", "Huset används när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag gäller inte gårdshuset",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Hägersten?",
  "price": [
    "Grundläggning på berg eller i sluttning, avståndet och höjdskillnaden till ledningarna, eventuell pump, om bygglov behövs, kök och badrum samt hur material kan bäras upp på tomten. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi sämre vattentryck i ett gårdshus högt upp på tomten i Mälarhöjden?",
     "Det kan bli så. Stockholm Vatten och Avfall varnar för att trycket kan försämras om en ny byggnad ligger högre och längre bort från förbindelsepunkten."),
    ("Betyder generösa byggrätter i Mälarhöjden att attefallshuset blir lovfritt?",
     "Nej. Byggrätten handlar om detaljplanen. Ligger tomten i en grön eller blå ring i Stadsmuseets karta krävs bygglov ändå."),
    ("Kan attefallshuset stå på prickmark i Hägersten?",
     "Ett lovfritt komplementbostadshus får enligt staden strida mot detaljplanen, till exempel stå på prickmark. Avståndet till gränser gäller ändå."),
    ("Behövs en pump om gårdshuset ligger lägre än villan i Hägersten?",
     "Det beror på höjderna. Vi mäter in avloppets fall innan servisanmälan så att det framgår om självfall räcker."),
  ],
  "sources": [_VARSAM, _STH_KBH, _STH_KLASS, _SVOA, _of("Mälarhöjden", "soderort/hagersten/malarhojden"),
              ("Stockholms stadsmuseum – Stockholms spår: Hägerstensåsen (pdf)",
               "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000088.pdf"),
              _PBL, _SKV],
  "cta": ("Vill du bygga ett gårdshus i Hägersten?", "Boka ett gratis platsbesök, så mäter vi höjderna och kontrollerar kartan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nybyggt gårdshus med mörk träpanel på en bergig tomt nedanför en äldre villa",
     "newly built small single-storey Swedish guest house with a low gable roof, dark brown vertical wood cladding and a black standing seam roof, one floor only, on a rocky sloping plot below an older white 1920s villa, granite outcrops, pine trees and moss, steps cut into the slope, late summer daylight" + _SFX),
    ("Grundplintar på en sluttande tomt med berg i dagen",
     "concrete pier foundations and timber floor beams for a small house on a sloping garden plot with exposed granite bedrock, pine trees around, overcast daylight, construction site without workers" + _SFX),
    ("Villagata som slingrar sig uppför en höjd med äldre villor i trädgårdar",
     "narrow winding residential street climbing a hill in a Swedish 1920s villa suburb, individually designed wooden villas set back in leafy gardens, pine trees and rock outcrops, morning light" + _SFX),
  ],
},

# ------------------------------------------------------------------ HÄSSELBY
"attefallshus-hasselby.html": {
  "kind": "district", "service": "attefallshus", "ort": "Hässelby", "svc_label": "Attefallshus",
  "title": "Attefallshus i Hässelby – villastadens styckade tomter",
  "description": "Attefallshus i Hässelby: styckade tomter i villastaden, gränser och grannmedgivanden, Hässelby strand och gård i kartan och VA till gårdshuset.",
  "h1": "Attefallshus i Hässelby",
  "lead": "I Hässelby villastad är de flesta bostäder småhus med äganderätt, och många tomter har delats genom åren. Det gör gränserna till den viktigaste frågan för ett attefallshus här. Geal Entreprenad AB mäter tomten, tar fram underlaget för grannarna och bygger huset nyckelfärdigt.",
  "card": "Styckade tomter, gränser och kartan.",
  "sections": [
    {"id": "villastaden-hasselby", "anchor": "Villastaden",
     "h2": "En villastad som har förtätats",
     "paras": [
       "Enligt stadens områdesfakta för 2025 finns 7 029 bostäder i Hässelby villastad, och 4 757 av dem är småhus med äganderätt. Vägledningen Varsam utveckling av småhus- och villaområden beskriver hur många villor i Hässelby villastad ersattes av täta grupper av enhetliga småhus på 1960- och 1970-talen, och hur villastäderna sedan har förtätats genom att tomter styckats av. Nya hus på tomter kring 600 kvadratmeter har kompletterat den äldre bebyggelsen.",
       "På en sådan tomt är det sällan ytan som tar slut först. Det är avståndet till gränserna. Ett lovfritt komplementbostadshus ska stå minst 4,5 meter från gränsen mot granne, samfällighet och allmän plats, och på en avstyckad tomt kan det finnas gränser på flera sidor. Vi ritar in huset på en karta med gränserna innan vi pratar storlek.",
     ],
     "aside": {"title": "Hässelby villastad 2025", "items": [
       "7 029 bostäder", "5 009 i småhus", "4 757 småhus med äganderätt"]}},
    {"id": "medgivande-hasselby", "h2": "Grannmedgivandet i praktiken",
     "paras": [
       "Hamnar huset närmare gränsen än 4,5 meter behövs ett skriftligt medgivande från alla berörda grannar. Staden skriver att det ska innehålla fastighetsbeteckning, vilken åtgärd det gäller, en situationsplan där huset och avståndet är inritat, och underskrifter. Du ska kunna visa upp medgivandet om ett tillsynsärende uppstår. Gäller det gränsen mot en gata eller park är det oftast staden som ska ge sitt medgivande, och förfrågan skickas till stadsbyggnadskontoret.",
       "Vi tar fram situationsplanen och en enkel fasadskiss så att grannen ser vad det gäller. Får du inte medgivandet kan huset flyttas längre in, göras mindre eller prövas med en bygglovsansökan.",
     ],
     "aside": {"title": "Medgivandet ska ha", "items": [
       "Fastighetsbeteckning", "Beskrivning av åtgärden", "Situationsplan med avstånd", "Grannarnas underskrifter"]}},
    {"id": "strand-gard-hasselby", "h2": "Hässelby strand och Hässelby gård",
     "paras": [
       "Hässelby villastad är inte markerad som kulturhistoriskt värdefull miljö i vägledningens tabell. Hässelby strand och Hässelby gård, som byggdes som tunnelbanestäder med grupper av rad- och kedjehus längst ut, står däremot som kulturhistoriskt värdefulla. Om din tomt ligger inom en grön eller blå ring i Stadsmuseets karta, eller om huset är blått eller grönt, krävs bygglov även för ett hus som annars är lovfritt.",
       "I tabellen syns också att flera av områdena i Hässelby saknar äldre miljöprogram. Då är kartan och detaljplanen det viktigaste underlaget, och vi kontrollerar båda innan något ritas.",
     ],
     "aside": None},
    {"id": "va-hasselby", "h2": "Ledningar och anmälan",
     "paras": [
       "Ska gårdshuset få vatten, avlopp och ventilation behövs en anmälan och ett startbesked innan installationerna görs. Stockholm Vatten och Avfall ska ha en servisanmälan med en ritning över ledningarna. Vattenledningen kopplas efter mätaren i huvudbyggnaden och spillvattnet till den befintliga ledningen på tomten. Dag- och dräneringsvatten från gårdshuset får inte gå till spillvattnet.",
       "På en avstyckad tomt kan befintliga servisledningar ligga nära gränsen eller gå över grannens mark. Det behöver vi veta innan grunden placeras. Har gårdshuset både kök eller pentry och toalett räknas det dessutom som en egen bostad i VA-taxan, och då tillkommer en avgift som ska vara betald innan huset kopplas in. Vi tar med det i tidplanen så att inflyttningen inte väntar på inkopplingen. Måtten och reglerna i sin helhet finns i " + _REG + ", och om du hellre vill bygga ut villan beskriver vi det under " + _L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Hässelby",
  "steps": [
    ("Gränserna", "Tomtens gränser och befintliga ledningar ritas in på en karta."),
    ("Placering", "Huset placeras så att 4,5 meter hålls, eller medgivanden tas fram."),
    ("Kartan", "Hässelby strand och gård kontrolleras i Stadsmuseets karta."),
    ("Anmälan", "Installationerna anmäls och servisanmälan skickas."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset används när slutbeskedet har kommit."),
  ],
  "rot_h2": "Inget rotavdrag för det nya huset",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Hässelby?",
  "price": [
    "Husets storlek och planlösning, kök och badrum, grundläggning, hur långt det är till befintliga ledningar och hur material kan köras in på en smal, avstyckad tomt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur nära gränsen får ett attefallshus stå på en avstyckad tomt i Hässelby villastad?",
     "Minst 4,5 meter om inte berörda grannar har gett ett skriftligt medgivande med situationsplan. Med medgivande kan huset stå närmare."),
    ("Krävs bygglov för attefallshus i Hässelby villastad?",
     "Villastaden är inte markerad som kulturhistoriskt värdefull i stadens vägledning, men det är fastighetens läge i Stadsmuseets karta som avgör. Vi kontrollerar den först."),
    ("Vad gäller i Hässelby strand och Hässelby gård?",
     "Båda står som kulturhistoriskt värdefulla miljöer i vägledningen. Ligger tomten inom en grön eller blå ring krävs bygglov."),
    ("Kan gårdshuset kopplas på en servis som går över grannens tomt i Hässelby?",
     "Det får Stockholm Vatten och Avfall och grannen svara på i det enskilda fallet. Vi tar reda på hur ledningarna går innan servisanmälan."),
    ("Vem ger medgivande när gårdshuset i Hässelby hamnar nära gatan?",
     "För gatu- och parkmark är det oftast staden som är huvudman. Förfrågan skickas skriftligt till stadsbyggnadskontoret."),
  ],
  "sources": [_of("Hässelby villastad", "vasterort/hasselby-vallingby/hasselby-villastad"),
              _of("Hässelby strand", "vasterort/hasselby-vallingby/hasselby-strand"),
              _VARSAM, _STH_KBH, _STH_KLASS, _SVOA, _PBL, _SKV],
  "cta": ("Planerar du ett attefallshus i Hässelby?", "Boka ett gratis platsbesök, så ritar vi in gränserna och ledningarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nybyggt gårdshus med ljusgrå panel bakom en villa på en mindre tomt",
     "newly built small Swedish guest house with light grey horizontal wood panel and a low gable roof placed in the corner of a modest suburban garden behind a 1970s brown brick villa, wooden fence to the neighbour, young birch tree, summer daylight" + _SFX),
    ("Situationsplan på ett bord med linjal och penna",
     "architect site plan drawing with property lines and a small rectangle for a new building on a wooden table with a ruler and a pencil, plain lines without readable text, soft daylight" + _SFX),
    ("Villagata med blandade hus från olika årtionden",
     "Swedish suburban street with a mix of houses from different decades, an older wooden villa next to 1970s brick houses and newer white houses, hedges and small lawns, summer daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"attefallshus-spanga.html": {
  "kind": "district", "service": "attefallshus", "ort": "Spånga", "svc_label": "Attefallshus",
  "title": "Attefallshus i Spånga – Solhem, järnvägen och tomterna",
  "description": "Attefallshus i Spånga: Solhem som värdefull miljö, Bromsten, Flysta och Sundby, 30-metersregeln nära spår, potten och vatten och avlopp.",
  "h1": "Attefallshus i Spånga",
  "lead": "Spånga växte upp som stationssamhälle vid järnvägen, och villaområdena Solhem, Bromsten, Flysta och Sundby har stora skillnader i tomter och regler. Geal Entreprenad AB kontrollerar kartan, spåren och gränserna för din tomt och bygger sedan komplementbostadshuset nyckelfärdigt.",
  "card": "Solhem, spåren och de stora tomterna.",
  "sections": [
    {"id": "villastaderna-spanga", "anchor": "Villastäderna",
     "h2": "Villastäderna kring Spånga",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden berättar hur små stationssamhällen uppstod när järnvägen byggdes ut, och hur några av dem, till exempel Spånga, fick status som municipalsamhällen med egen administration. Vägledningen räknar Solhem, Bromsten, Flysta och Sundby till villastäderna. I Solhem fanns stora tomter där bara en tiondel av tomten fick bebyggas.",
       "Områdesfakta för 2025 visar hur mycket småhus det finns: 1 946 småhus med äganderätt i Solhem, 916 i Bromsten, 657 i Flysta och 525 i Sundby. På de stora, äldre tomterna finns ofta plats för ett gårdshus – men platsen måste också klara reglerna för lov och gränser.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Solhem 1 946", "Bromsten 916", "Flysta 657", "Sundby 525"]}},
    {"id": "solhem-spanga", "h2": "Solhem i Stadsmuseets karta",
     "paras": [
       "I vägledningens tabell är Solhem markerat som kulturhistoriskt värdefull miljö, medan Bromsten, Flysta och Sundby saknar markering. Det avgörande är ändå hur just din fastighet är klassad. Ligger den inom en grön eller blå ring i Stadsmuseets klassificeringskarta, eller är villan markerad med blått eller grönt, krävs bygglov även för ett hus som annars hade varit lovfritt. Gul eller grå markering kräver inget lov i sig.",
       "I en värdefull miljö prövar byggnadsnämnden hur huset placeras och ser ut. Vi ritar då ett gårdshus som underordnar sig villan, med enkel form, träpanel och en takvinkel som hör hemma i villastaden. Vägledningen beskriver villastädernas fritt liggande hus i trädgårdslandskap med respektavstånd till tomtgränsen och gröna förgårdar mot gatan – ett gårdshus längst in på tomten, bakom villan, stör den bilden minst. Står fastigheten på en streckad yta i kartan är miljön inte inventerad, och då kan Stadsmuseet behöva göra en bedömning innan vi vet om lov krävs.",
     ],
     "aside": None},
    {"id": "sparen-spanga", "h2": "30 meter från spåret",
     "paras": [
       "Lagen och staden ställer ett krav som många missar: ett lovfritt komplementbostadshus ska stå minst 30 meter från närmaste järnvägsspår. Vill du bygga närmare behövs ett medgivande från infrastrukturförvaltaren, annars blir det en bygglovsansökan. I Spånga, där villaområdena växte upp kring stationen, ligger en del tomter tillräckligt nära spåren för att regeln ska spela roll.",
       "Vi mäter avståndet från husets tänkta läge till spåret innan vi ritar. Samtidigt kontrollerar vi avståndet 4,5 meter till gränserna mot grannar, samfällighet och allmän plats. Där inte heller det går att klara behövs skriftliga medgivanden med situationsplan.",
     ],
     "aside": {"title": "Avstånd att mäta", "items": [
       "30 m till järnvägsspår", "4,5 m till grannens gräns", "4,5 m till gata och park"]}},
    {"id": "potten-spanga", "h2": "Potten, ledningarna och anmälan",
     "paras": [
       "Huset får vara högst 30,0 kvadratmeter byggnadsarea och 4,0 meter i nock, och det ska vara mindre än villan. Alla lovfria komplementbyggnader och komplementbostadshus på tomten får tillsammans vara högst 45,0 kvadratmeter, och gamla friggebodar och attefallshus räknas in. På de stora tomterna i Solhem är det ofta gamla förråd och garage som tar en del av potten.",
       "Vatten, avlopp, ventilation och eldstad ska anmälas, och installationerna får göras först efter startbesked. Stockholm Vatten och Avfall vill ha en servisanmälan med ritning, och den nya vattenledningen ska kopplas efter mätaren i villan. Ett gårdshus långt in på en stor tomt kan få sämre vattentryck, så avståndet till förbindelsepunkten är värt att räkna på. Lagtexten är sammanfattad i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Spånga",
  "steps": [
    ("Kartan", "Fastighetens klassning i Stadsmuseets karta kontrolleras."),
    ("Avstånden", "Spår, gränser och befintliga gårdshus mäts in vid ett gratis platsbesök."),
    ("Potten", "Vi räknar ut hur mycket av de 45 kvadratmetrarna som återstår."),
    ("Anmälan eller lov", "Installationer anmäls; bygglov söks där det krävs."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset tas i bruk när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag och nybyggnad",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Spånga?",
  "price": [
    "Husets storlek, kök och badrum, om bygglov behövs, grundläggning, ledningarnas längd på en stor tomt och om gamla förråd ska rivas för att ge plats i potten. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur långt från järnvägen måste ett attefallshus stå i Spånga?",
     "Minst 30 meter från närmaste spår, om inte infrastrukturförvaltaren har gett sitt medgivande. Annars krävs bygglov."),
    ("Krävs bygglov för attefallshus i Solhem?",
     "Solhem är markerat som kulturhistoriskt värdefull miljö i stadens vägledning. Ligger fastigheten inom en grön eller blå ring i Stadsmuseets karta krävs bygglov."),
    ("Räknas det gamla förrådet in i potten på vår tomt i Bromsten?",
     "Ja, om det är byggt utan lov. Tidigare lovfria komplementbyggnader ingår i de 45 kvadratmetrarna."),
    ("Kan ett gårdshus långt in på tomten i Spånga få dåligt vattentryck?",
     "Det kan hända. Stockholm Vatten och Avfall skriver att trycket kan bli sämre om huset ligger högre och längre från förbindelsepunkten."),
    ("Får bara en tiondel av tomten bebyggas i Solhem?",
     "Det var så de ursprungliga tomterna planerades enligt stadens vägledning. Vad som gäller i dag står i detaljplanen för din fastighet, och vi läser den innan vi ritar."),
  ],
  "sources": [_VARSAM, _STH_KBH, _STH_KLASS, _SVOA, _of("Solhem", "vasterort/jarva/solhem"),
              _of("Bromsten", "vasterort/jarva/bromsten"), _of("Flysta", "vasterort/jarva/flysta"),
              _of("Sundby", "vasterort/jarva/sundby"), _PBL, _SKV],
  "cta": ("Vill du bygga ett attefallshus i Spånga?", "Boka ett gratis platsbesök, så mäter vi avstånden till spår och gränser innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Gårdshus med vit panel och svart plåttak på en stor trädgårdstomt med fruktträd",
     "new small Swedish guest house with white vertical wooden panel, black window frames and black standing seam metal roof on a large old garden plot with apple trees and a lawn, a 1910s wooden villa with glass veranda in the background, summer daylight" + _SFX),
    ("Äldre förråd och garage längst in på en villatomt",
     "old small red wooden storage shed and a detached single garage at the back of a large Swedish villa garden with tall birch trees and overgrown lilac, overcast daylight" + _SFX),
    ("Villaområde med trädgårdar och en järnvägsbank i bakgrunden",
     "Swedish suburban villa area with wooden houses in green gardens, a railway embankment with overhead line masts visible in the background behind trees, no train, summer daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"attefallshus-vallingby.html": {
  "kind": "district", "service": "attefallshus", "ort": "Vällingby", "svc_label": "Attefallshus",
  "title": "Attefallshus i Vällingby – riksintresset och småhusen",
  "description": "Attefallshus i Vällingby: riksintresset Vällingby–Råcksta, Atlantis och Omega, småhusen i Vinsta, Nälsta och Kälvesta – lov, gränser och VA.",
  "h1": "Attefallshus i Vällingby",
  "lead": "Runt Vällingby centrum ligger både ett riksintresse för kulturmiljövården och stora villa- och radhusområden. Reglerna för ett attefallshus skiljer sig därför mycket mellan grannkvarteren. Geal Entreprenad AB tar reda på vad som gäller för din tomt och bygger komplementbostadshuset nyckelfärdigt.",
  "card": "Riksintresset och villaområdena.",
  "sections": [
    {"id": "riksintresset-vallingby", "anchor": "Riksintresset",
     "h2": "Vällingby–Råcksta är riksintresse",
     "paras": [
       "Enligt stadens vägledning Varsam utveckling av småhus- och villaområden var Vällingby den första tunnelbanestaden. Den invigdes 1954 och blev den stadsdel där idén om ABC-staden genomfördes mest konsekvent. Vällingby–Råcksta är utpekat som riksintresse för kulturmiljövården, och Grimsta står som kulturhistoriskt värdefull miljö.",
       "Staden skriver att bygglov krävs för åtgärder inom ett riksintresse, som visas med en blå ring i Stadsmuseets klassificeringskarta – även när åtgärden annars är lovfri. Ligger din tomt inom ringen räknar vi därför med en bygglovsansökan för gårdshuset från början.",
     ],
     "aside": None},
    {"id": "atlantis-omega", "h2": "Radhusen i Atlantis och Omega",
     "paras": [
       "Vägledningen nämner flera mycket väl gestaltade radhus- och villaområden i Vällingby och pekar särskilt ut Atlantis i nordost och Omega i nordväst som kulturhistoriskt synnerligen värdefulla. Atlantis beskrivs med sin låga skala, anpassning till terrängen och sammanhållna utformning. Där är tomterna små och miljön känslig, och ett fristående gårdshus är sällan en enkel fråga.",
       "Bor du i ett av dessa områden börjar vi med Stadsmuseets klassning och detaljplanens bestämmelser. Ibland finns det skydds- eller varsamhetsbestämmelser som styr mer än lagens mått. Vägledningen beskriver också hur tunnelbanestäderna byggdes med högre hus närmast centrum och en nedtrappning mot grupper av rad- och kedjehus längst ut, med gångvägar och naturstråk mellan kvarteren. Ett gårdshus som syns från en sådan gångväg påverkar helheten mer än man tror, och det är en av sakerna byggnadsnämnden tittar på när lov krävs. Vi föreslår därför en placering och en utformning som följer grannhusens skala och material.",
     ],
     "aside": None},
    {"id": "smahusen-vallingby", "h2": "Vinsta, Nälsta och Kälvesta",
     "paras": [
       "Längre ut ligger småhusområden med andra förutsättningar. Områdesfakta för 2025 räknar 826 småhus med äganderätt i Vinsta, 1 297 i Nälsta och 1 492 i Kälvesta, medan Vällingby självt har 220. Nälsta räknas i vägledningen till villastäderna, och Kälvesta beskrivs som en stadsdel som byggdes med enbart småhus när andelen småhus ökade i början av 1970-talet. Ingen av dem är markerad som kulturhistoriskt värdefull i vägledningens tabell.",
       "I de gruppbyggda områdena är tomterna ofta lika stora och husen placerade på samma sätt, så det som fungerar på en tomt fungerar ofta även hos grannen – och tvärtom. Ett komplementbostadshus ska vara högst 30,0 kvadratmeter, 4,0 meter i nock och mindre än huset det hör till. Det ska stå 4,5 meter från gränserna om inte grannarna skriftligt har godkänt något annat, och alla lovfria gårdshus på tomten får tillsammans vara högst 45,0 kvadratmeter.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Kälvesta 1 492", "Nälsta 1 297", "Vinsta 826", "Vällingby 220"]}},
    {"id": "va-vallingby", "h2": "Installationer och anslutning",
     "paras": [
       "Ett gårdshus med pentry och toalett behöver en anmälan och ett startbesked innan vatten, avlopp och ventilation installeras. Stockholm Vatten och Avfall ska få en servisanmälan med en ritning över ledningarna, och den nya vattenledningen kopplas efter mätaren i huset. Spillvattnet ansluts till den befintliga spillvattenledningen på tomten, medan dag- och dräneringsvatten inte får ledas dit.",
       "Har huset både kök eller pentry och toalett räknas det som en egen bostad i VA-taxan, och då tillkommer en avgift som ska vara betald innan inkoppling. Hela regelverket finns i " + _REG + ", och om du hellre vill bygga ut huset beskriver vi det under " + _L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Vällingby",
  "steps": [
    ("Kartan", "Vi ser om tomten ligger inom riksintresset eller en värdefull miljö."),
    ("Detaljplanen", "Skydds- och varsamhetsbestämmelser för radhusområden kontrolleras."),
    ("Platsbesök", "Gränser, befintliga gårdshus och ledningar mäts in."),
    ("Lov eller anmälan", "Bygglov där det krävs, annars anmälan för installationerna."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset används när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag gäller inte nya hus",
  "rot": [_ROT_NY],
  "price_h2": "Vad påverkar priset på ett attefallshus i Vällingby?",
  "price": [
    "Om bygglov behövs, husets storlek, kök och badrum, grundläggning, avståndet till ledningarna och hur material kan köras in i ett gruppbyggt område. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för attefallshus inom riksintresset Vällingby–Råcksta?",
     "Ja. Staden skriver att åtgärder inom ett riksintresse för kulturmiljövården kräver bygglov även om de annars är lovfria."),
    ("Är Kälvesta och Vinsta markerade som kulturmiljö?",
     "Inte i tabellen i stadens vägledning. Det är ändå fastighetens läge i Stadsmuseets karta som avgör, så vi kontrollerar den."),
    ("Går det att bygga gårdshus i Atlantis i Vällingby?",
     "Området är kulturhistoriskt synnerligen värdefullt enligt stadens vägledning, och tomterna är små. Vi börjar med detaljplanen och Stadsmuseets klassning innan något planeras."),
    ("Räknas attefallshuset som en egen bostad i VA-taxan i Vällingby?",
     "Ja, om det har både kök eller pentry och toalett. Då tillkommer en avgift enligt Stockholm Vatten och Avfalls taxa."),
    ("Får gårdshuset stå på prickmark i Kälvesta?",
     "Ett lovfritt komplementbostadshus får enligt staden strida mot detaljplanen, till exempel stå på prickmark. Avståndet 4,5 meter till gränserna gäller ändå."),
  ],
  "sources": [_VARSAM, _STH_KBH, _STH_KLASS, _SVOA, _of("Vällingby", "vasterort/hasselby-vallingby/vallingby"),
              _of("Vinsta", "vasterort/hasselby-vallingby/vinsta"), _of("Nälsta", "vasterort/hasselby-vallingby/nalsta"),
              _of("Kälvesta", "vasterort/hasselby-vallingby/kalvesta"), _PBL, _SKV],
  "cta": ("Vill du bygga ett attefallshus i Vällingby?", "Boka ett gratis platsbesök, så kontrollerar vi riksintresset, gränserna och ledningarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet gårdshus med svart panel bakom ett enplans småhus från 1970-talet",
     "newly built small Swedish guest house with black vertical wooden cladding and a low pitched roof in the back garden of a 1970s single-storey brown brick bungalow in a uniform suburban housing area, lawn and young fruit tree, summer daylight" + _SFX),
    ("Låga radhus i tegel och trä anpassade till en skogig sluttning",
     "low 1950s Swedish terraced houses in brick and wood following the terrain of a wooded slope, pine trees and rocks between the rows, footpath, autumn daylight" + _SFX),
    ("Gata med likadana enplanshus och små trädgårdar",
     "quiet Swedish suburban street with identical 1970s single-storey houses with brown wood panels, small front lawns and low hedges, summer daylight" + _SFX),
  ],
},
}
