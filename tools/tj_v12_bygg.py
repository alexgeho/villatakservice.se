# -*- coding: utf-8 -*-
"""Byggföretag – ortsidor v12: Bromma, Ekerö, Hässelby, Enskede, Sigtuna, Upplands Väsby (2026-10-25).
Lokal vinkel per sida (skild från ortens övriga tjänstesidor): Bromma – vind, bärande väggar och en andra bostad
i villan; Ekerö – förhandsbesked, strandskydd, vattenskyddsområde och bergvärme för nytt hus; Hässelby – riva,
bygga nytt och marken i villastaden; Enskede – byggplatsen på gatan (polistillstånd, container, schakt, gatuträd);
Sigtuna – nytt småhus, komplementbostadshus och att köpa till kommunal mark; Upplands Väsby – nybyggnadskarta,
VA-anslutning, avstyckning och lovfri tillbyggnad. (Flygbuller i Sigtuna/Upplands Väsby och fasad/kulturmiljö i
Sigtuna används inte – de ägs av fönsterbyte- respektive fasadsidorna.)
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
  Skatteverket (Så fungerar rotavdraget; Ger arbetet rätt till rotavdrag? – tillbyggnad 75 procent/dörr, nytt hus
  och fristående byggnad, riva ett hus, riva väggar och bygga om planlösningen, bygglovshandlingar/arkitekt,
  markarbeten för värmeförsörjning),
  Stockholms stad, bygglov.stockholm (Så söker du bygglov – guide; Ändra i bärande konstruktion; Ny bostad i
  enbostadshus (bygglovsbefriad); Inredning av ytterligare bostad; Inreda vinden; Ombyggnad; Villa eller småhus –
  nybyggnad och ändringar; Rivning; Schaktning och fyllning av mark; Fälla eller ta bort träd; Container; Byggbod,
  byggetablering, byggskylt), Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med
  vägledningar (juni 2021, pdf med text), Stockholms stad, tillstand.stockholm (Använda offentlig plats för
  byggverksamhet; Ställa byggsäckar, containrar och fristående bodar på offentlig plats; Mark- och gatuarbeten på
  offentlig mark; Bra att veta för dig som planerar byggprojekt, juni 2019, pdf med text),
  Boverket (PBL kunskapsbanken – Bygglov för att inreda ytterligare bostad),
  Ekerö kommun (Förhandsbesked; Strandskydd, bryggor och sjöbodar; Vattenskyddsområden; Värmepumpar och bergvärme),
  Länsstyrelsen i Stockholms län (Skyddsföreskrifter för Östra Mälarens vattenskyddsområde, 2008-11-25, pdf),
  Sigtuna kommun (Nybyggnation av en- och tvåbostadshus; Komplementbostadshus; Försäljning av små markområden,
  komplettering av småhustomter; Vattentjänstplan),
  Upplands Väsby kommun (Kart- och mättjänster; Ledningsnät, anslutning till fastighet; Förrättningar, avstyckning;
  Kommunalt och statlig lantmäteri; Tillbyggnad; Marklov; Bygglovsprocessen).
Strukna (ej verifierade, oklara i källan eller medvetet utelämnade): alla avgifter i kronor (Stockholms
zonavgifter per kvadratmeter och dygn, bygglovstaxor, Upplands Väsbys geodatataxa, Sigtunas kartavgift), Upplands
Väsbys leveranstid för nybyggnadskarta (sidan anger både "inom 6 veckor" och "normalt inom två veckor" – motsägelse,
struket), vilka myndigheter som prövar tillstånd enligt vattenskyddsföreskrifterna (anges inte i föreskrifterna
som lästes), innehållet i Södra Mälarens föreskrifter (inte lästa – bara att de finns och gäller sedan 1 juni 2024
enligt kommunen), Ekerös avgift för strandskyddsdispens, Skatteverkets 35-procentsschablon för borrning (gäller
fast pris – utelämnad för att inte se ut som en prisuppgift), Stockholms äldre vägledning för vindsinredning
(2013, staden skriver själv att den inte är uppdaterad efter 1 december 2025 – används inte), handläggningstider
för TA-plan (gäller främst evenemang), att "de flesta" husen i Bromma har outnyttjad vind, att tomterna i
Hässelby villastad i dag är ett visst antal kvadratmeter (vägledningen ger bara stadens generella tal för
villastäder), vilka gator i Enskede som saknar trottoar, var Sigtunas VA-verksamhetsområden går, att radhus i
Upplands Väsby har gemensamhetsanläggningar. Inga priser, garantier, omdömen, egna uppdrag eller cert.
Huvudkritik 2026-10-25: 'konstruktör' som egen tjänst struken (Bromma), 'det arbetet gör vi' om
miljöinventering omskrivet (Hässelby), 'många Brommavillor' omskrivet, utsättningspinnar struket ur ekero-1-alt.
Kritikpass 2026-10-25: varje siffra kontrollerad mot källtexten igen – 0,5 meter (marklov, Stockholm och Upplands
Väsby), 50,0 kvadratmeter (rivningsanmälan, Stockholm), tio + tio veckor (Stockholm, Sigtuna; Ekerö max 20 veckor),
två/fem år (Stockholm: påbörja/färdigt), fyra veckor efter kungörelse (Stockholm), 15 kvadratmeter byggskylt,
1,6/2 meter under byggställning, sex veckor och vart femte år (schakt/utbildning, Stockholm), 100/300 meter
strandskydd, 1:10 000 och 1:2000 (Ekerö förhandsbesked), 2008 och 1 juni 2024 (vattenskydd), 50 meter primär
skyddszon, 250 liter brandfarlig vätska, 30/20 meter grannar och två veckor (bergvärme Ekerö), 100 mg/l klorid,
30/50 kvadratmeter, 4/4,5 meter nock, 45/65 kvadratmeter pott, 4,5 meter tomtgräns (Sigtuna), 1 januari 2023
(vattentjänstplan), 0,5 meter förbindelsepunkt, 10 meter förenklad karta, 1:400, 1 april 2009 (ABVA), 30,0
kvadratmeter pott (Upplands Väsby). Strukna i passet: "certifierad" kontrollansvarig och "behörighetsnivå"
(skrivs inte ut), att KA krävs för komplementbostadshus i Sigtuna (kommunen bedömer från fall till fall – så
skrivet), uppgiften att containrar i Stockholm "alltid" kräver bygglov (staden skriver "kan behöva"), att
gatuträd i Enskede skyddas särskilt (källan är stadsövergripande – formulerat så), att projekt i
Hässelby "ofta" gäller nya hus och att varje väggrivning kräver anmälan (bara bärande – så skrivet). Bildalt-texter justerade
efter genererade bilder; omgjorda: hasselby-2 (text på grävmaskinen), enskede-2 (etikett med text på
containern), upplands-vasby-1 (osammanhängande stomme med färdiga fönster), upplands-vasby-2 (ett rör som bytte färg).
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py."""

_L = '<a class="text-link" href="{0}">{1}</a>'

# ------------------------------------------------------------------ gemensamma källor
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV_JOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/"
_SB_GUIDE = ("Stockholms stad – Så söker du bygglov", "https://bygglov.stockholm/guide--bygglov--steg-for-steg/")
_SB_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (2021)",
              "https://bygglov.stockholm/contentassets/8f9f2e84c0524ad6b75eb01a8c9c8995/varsam-utveckling-av-smahus--och-villaomraden-strategi-med-vagledningar_juni-2021_-ta.pdf")
_TS = "https://tillstand.stockholm/tillstand-regler-och-tillsyn/"
_EK = "https://www.ekero.se/bygga-bo-miljo/"
_SI = "https://www.sigtuna.se/bygga-bo-och-miljo/"
_UV = "https://www.upplandsvasby.se/bygga-bo-och-miljo/"

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"byggforetag-bromma.html": {
  "kind": "district", "service": "byggforetag", "ort": "Bromma", "svc_label": "Byggföretag",
  "title": "Byggföretag i Bromma – vind, bärande väggar och ny bostad",
  "description": "Byggföretag i Bromma: inreda vinden, flytta bärande väggar och göra en andra bostad i villan – anmälan, lovplikt och stadens krav.",
  "h1": "Byggföretag i Bromma",
  "lead": "En villa i Bromma kan ha mer yta innanför väggarna än vad som används i dag: en kall vind under det branta taket, en källare eller en planlösning från en annan tid. Geal Entreprenad AB tar sådana ombyggnader som total entreprenad – från ritningar och handlingar till färdiga rum – och här går vi igenom vad Stockholms stad kräver när man bygger om inifrån.",
  "card": "Vind, bärande väggar och en andra bostad.",
  "sections": [
    {"id": "volymen-bromma", "anchor": "Husen och vinden",
     "h2": "Ett och ett halvt plan under brant tegeltak",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur trädgårdsstäderna i Äppelviken, Ålsten och Smedslätten tillkom under 1920-talet. I bland annat Nockeby, Höglandet och Ulvsunda blev husen enkla volymer i ett och ett halvt plan med branta sadeltak i rött tegel och små takkupor mitt på långsidorna. I de tidiga trädgårdsstäderna var huvuddelen friliggande enfamiljshus i ett plan med delvis inredd vind.",
       "Vägledningen konstaterar också att många av husen har förändrats invändigt och byggts till genom åren. För den som vill ha fler rum utan att bygga ut på tomten är det därför ofta vinden, källaren eller väggarna mellan rummen som är frågan. Det är ett annat slags projekt än en tillbyggnad: volymen är densamma, men stommen, brandskyddet och installationerna berörs.",
     ],
     "aside": {"title": "Ytan som redan finns", "items": [
       "Delvis inredd vind",
       "Källare under bottenvåningen",
       "Planlösning från byggåret",
       "Takkupor på långsidorna"]}},
    {"id": "barande-bromma", "h2": "Bärande väggar: anmälan, ritningar och konstruktör",
     "paras": [
       "Ska en bärande vägg tas bort eller ett bärande bjälklag öppnas för en trappa krävs enligt Stockholms stad en anmälan, och arbetet får börja först när startbeskedet har kommit. Staden påpekar att den inte kan hjälpa dig att avgöra om åtgärden påverkar den bärande konstruktionen och hänvisar till en konstruktör när man är osäker.",
       "De äldre ritningarna går att hämta i stadens e-tjänst Bygg- och plantjänsten med bank-id. De visar husets principiella konstruktion, men staden varnar för att de kan vara ofullständiga och att de som byggde inte nödvändigtvis följde dem. Vi börjar därför med att ta fram ritningarna, öppnar på några utvalda ställen och ser till att konstruktionen räknas på det som faktiskt finns innan anmälan lämnas in.",
       "Samma anmälningsplikt gäller om brandskyddet ändras, om vatten och avlopp installeras eller ändras och om en eldstad sätts in. Ett nytt badrum på vinden eller en ny trappa mellan planen kan alltså bli ett ärende hos stadsbyggnadskontoret, även när ingenting syns utifrån.",
     ],
     "aside": {"title": "Kräver anmälan", "items": [
       "Bärande väggar och bjälklag",
       "Ändrat brandskydd",
       "Nytt eller ändrat vatten och avlopp",
       "Ny eldstad"]}},
    {"id": "andra-bostad-bromma", "h2": "En andra bostad i villan",
     "paras": [
       "Att inreda ytterligare en bostad i en byggnad kräver i grunden bygglov, skriver Boverket, eftersom fler bostäder kan påverka behovet av vatten och avlopp, gator och parkering. För ett enbostadshus finns ett undantag: Stockholms stad skriver att du under vissa förutsättningar får inreda en ny bostad utan bygglov, även om det inte följer detaljplanens bestämmelser.",
       "Undantaget faller om huset eller området är särskilt kulturhistoriskt värdefullt, eller om detaljplanen eller områdesbestämmelser har bestämmelser till skydd för särskilda värden. Staden hänvisar till Stadsmuseets klassificeringskarta som en första indikation och skriver att man kan behöva fråga Stadsmuseet om en bedömning. Fasadändringar som görs i samband med den nya bostaden kräver inte heller bygglov så länge huset och området saknar sådant skydd.",
       "Oavsett lovfrågan ska den nya bostaden klara dagens krav på bland annat tillgänglighet, brandsäkerhet, rumshöjd och bostadsutformning. Boverket påpekar att just de kraven kan göra det omöjligt att genomföra åtgärden, särskilt i en källare eller på en vind. Det är därför vi mäter takhöjder och tänker igenom utrymningsvägar innan någon ritar en planlösning.",
     ],
     "aside": None},
    {"id": "takkupa-bromma", "h2": "När vinden växer uppåt",
     "paras": [
       "Räcker inte höjden under taket blir en takkupa ofta lösningen. Stockholms stad räknar en större takkupa som en tillbyggnad, eftersom husets volym ökar, och en tillbyggnad kräver bygglov om den inte ryms i undantagen för lovfria tillbyggnader. Vill man i stället inreda vinden till en helt egen lägenhet krävs bygglov för den nya bostaden. Finns ett förbud mot vindsinredning i detaljplanen kan staden enligt sin egen sida ändå ge lov om planens genomförandetid har gått ut och övriga förutsättningar är uppfyllda.",
       "Blir förändringen så stor att hela eller en betydande och avgränsbar del av huset förnyas räknar staden det som en ombyggnad, och då omfattar ansökan eller anmälan hela byggnaden och inte bara den ändrade delen. För tillbyggnader i Bromma, med småstugornas och trädgårdsstadens särskilda förutsättningar, finns en egen sida om " + _L.format("tillbyggnad-bromma.html", "tillbyggnad i Bromma") + ". Om takets isolering när vinden blir varm, läs mer om " + _L.format("vindsisolering.html", "vindsisolering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi upp en ombyggnad i Bromma",
  "steps": [
    ("Platsbesök", "Vi går igenom vind, källare och väggar och tittar på taket utifrån."),
    ("Ritningar och konstruktör", "Äldre ritningar tas fram och konstruktören bedömer stommen."),
    ("Lovfrågan", "Klassificeringskartan och detaljplanen avgör om det blir anmälan eller bygglov."),
    ("Skriftligt kostnadsförslag", "Rivning, stomme, installationer och ytskikt redovisas var för sig."),
    ("Startbesked och bygge", "Vi bygger först när startbeskedet finns, med en kontakt för alla hantverkare."),
    ("Slutbesked", "Underlaget sammanställs så att rummen får tas i bruk."),
  ],
  "rot_h2": "Rotavdrag för ombyggnad i Bromma",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material och resor ger inget avdrag, och du ska äga bostaden när arbetet utförs.",
    "Skatteverket godkänner att riva väggar och bygga om planlösningen i ett småhus. En tillbyggnad ger avdrag om den sitter ihop med husets yttervägg till minst 75 procent eller har en dörr emellan. Bygglovshandlingar och arkitekt ger inget avdrag. Vi drar av rotavdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Bromma?",
  "price": [
    "Stommens skick, hur mycket som måste förstärkas och om nya våtrum och trappor behövs väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag där varje del står för sig.",
  ],
  "faq": [
    ("Behöver vi anmäla till staden om vi tar bort en vägg i Brommavillan?",
     "Ja, om väggen är bärande. Stockholms stad kräver då en anmälan och ett startbesked innan arbetet börjar. Är du osäker på om väggen bär hänvisar staden till en konstruktör."),
    ("Kan vi göra en lägenhet för föräldrarna i vår villa i Bromma utan bygglov?",
     "Ibland. I ett enbostadshus kan en ny bostad vara lovbefriad, men inte om huset eller området är särskilt kulturhistoriskt värdefullt. Brandskydd, stomme och vatten och avlopp kräver ändå anmälan."),
    ("Var hittar vi de gamla ritningarna till vårt hus i Bromma?",
     "I Stockholms stads e-tjänst Bygg- och plantjänsten, där du loggar in med bank-id. Staden påpekar att ritningarna kan vara ofullständiga."),
    ("Räknas en ny takkupa som tillbyggnad i Stockholms stad?",
     "Ja. Staden nämner en större takkupa som exempel på tillbyggnad, eftersom husets volym ökar. Då krävs bygglov om kupan inte ryms i undantagen för lovfria tillbyggnader."),
    ("Ger det rotavdrag att bygga om planlösningen i villan?",
     "Ja. Skatteverket godkänner att riva väggar och bygga om planlösningen i ett hus. Avdraget gäller arbetskostnaden, inte material eller bygglovshandlingar."),
  ],
  "sources": [
    _SB_VARSAM,
    ("Stockholms stad – Ändra i bärande konstruktion", _SB + "andra-inomhus/andra-i-barande-konstruktion/"),
    ("Stockholms stad – Ny bostad i enbostadshus (bygglovsbefriad)", _SB + "andra-inomhus/ny-bostad-i-enbostadshus-bygglovsbefriad/"),
    ("Stockholms stad – Inredning av ytterligare bostad", _SB + "andra-inomhus/inredning-av-ytterligare-bostad/"),
    ("Stockholms stad – Inreda vinden", _SB + "andra-inomhus/inreda-vinden/"),
    ("Stockholms stad – Ombyggnad", _SB + "andra-inomhus/ombyggnad/"),
    ("Stockholms stad – Villa eller småhus, nybyggnad och ändringar", _SB + "bygga-nytt-och-bygga-till/villa-eller-smahus-nybyggnad-och-andringar/"),
    ("Boverket – Bygglov för att inreda ytterligare bostad",
     "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/ytterligare_bostad/"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Vill ni använda vinden eller källaren i Bromma?", "Boka ett gratis platsbesök, så går vi igenom stommen, lovfrågan och vad som är möjligt."),
  "img": [
    ("Gul trävilla i ett och ett halvt plan med brant rött tegeltak, takkupa och syrener i Bromma",
     "1920s Swedish one-and-a-half storey wooden villa with vertical board-and-batten facade painted pale yellow, steep red clay tile gable roof with one small central dormer on the long side, white windows, lilac bushes and a trimmed hedge, quiet residential street in Bromma Stockholm, early summer, empty scene"),
    ("Oinredd vind med synliga takstolar, brett trägolv, staplade brädor och ett gavelfönster",
     "interior of an empty unfinished attic in an old Swedish wooden house: exposed wooden rafters and roof boards under a steep roof, old wide pine floorboards, a small gable window letting in daylight, a few loose planks stacked neatly, dust in the light, no furniture, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ EKERÖ
"byggforetag-ekero.html": {
  "kind": "district", "service": "byggforetag", "ort": "Ekerö", "svc_label": "Byggföretag",
  "title": "Byggföretag i Ekerö – nytt hus, vattenskydd och bergvärme",
  "description": "Byggföretag på Ekerö: förhandsbesked för nytt hus, strandskydd, vattenskyddsområdet som täcker hela kommunen och tillstånd för bergvärme.",
  "h1": "Byggföretag i Ekerö",
  "lead": "Ett nytt hus på Mälaröarna börjar sällan med ritningarna. Först ska det visa sig om platsen får bebyggas, om strandskyddet berör tomten och hur bygget ska hållas rent i en kommun som i sin helhet ligger inom skyddsområde för dricksvatten. Geal Entreprenad AB bygger nya hus och större tillbyggnader som total entreprenad, och här är de frågor som kommer först i Ekerö kommun.",
  "card": "Nytt hus, vattenskydd och bergvärme.",
  "sections": [
    {"id": "forhandsbesked-ekero", "anchor": "Förhandsbesked",
     "h2": "Förhandsbesked när detaljplan saknas",
     "paras": [
       "Ekerö kommun rekommenderar ett förhandsbesked innan du söker bygglov för ett nytt bostadshus där det inte finns någon detaljplan. Ligger fastigheten inom detaljplan går det inte att söka förhandsbesked, och finns det redan ett hus på tomten kan en tillbyggnad sökas som bygglov direkt. Ekerökartan visar vilket som gäller för din fastighet.",
       "Ansökan är enkel: en karta eller ett flygfoto i skala 1:10 000 med platsen markerad och en situationsplan i skala 1:2000 med den tänkta husplaceringen. Grannarna behöver du inte fråga själv, det gör kommunen. Ibland behövs fler utredningar, till exempel om avloppet. Kommunen använder översiktsplanen som riktlinje och kan komma fram till att området först behöver en detaljplan.",
       "Ett positivt besked betyder att platsen kan bebyggas, men husets storlek, utseende och exakta placering prövas i bygglovet. Ofta kan en tomtplats styckas av, men det beslutar Lantmäteriet. Beskedet gäller i två år från att det vann laga kraft. Kommunen ska besluta inom tio veckor från att ansökan är komplett och kan förlänga med högst tio veckor till, och ansökan räknas som komplett först när remissinstanserna har svarat. De flesta besluten fattas av byggnadsnämnden, som träffas tio gånger per år.",
     ],
     "aside": {"title": "Förhandsbesked på Ekerö", "items": [
       "Bara utanför detaljplan",
       "Karta 1:10 000 och situationsplan 1:2000",
       "Högst 20 veckors handläggning",
       "Gäller i två år"]}},
    {"id": "strand-ekero", "h2": "Strandskyddet före husplaceringen",
     "paras": [
       "Det generella strandskyddet är 100 meter från strandkanten men på vissa ställen upp till 300 meter, skriver kommunen, och det gäller både på land och i vattnet. Inom strandskyddat område är det förbjudet att uppföra en ny byggnad eller att gräva och på annat sätt förbereda för en, och det gäller även komplementbyggnader. Det är också förbjudet att utöka den privata zonen med till exempel gräsmatta, rabatter eller utemöbler.",
       "För att få dispens krävs särskilda skäl. Till ansökan ska bland annat en beskrivning av skälen, situationsplan, planritning och elevationsritning bifogas, liksom en beskrivning av växt- och djurlivet och uppgifter om servitut eller gemensamhetsanläggningar. Vill du bygga inom strandskyddat område rekommenderar kommunen att du söker dispens innan du söker förhandsbesked.",
     ],
     "aside": None},
    {"id": "vattenskydd-ekero", "h2": "Hela kommunen ligger inom vattenskyddsområde",
     "paras": [
       "Ekerö har sedan 2008 varit en del av Östra Mälarens vattenskyddsområde. Sedan Södra Mälarens vattenskyddsområde började gälla 1 juni 2024 ligger hela kommunen inom skyddsområde för vattentäkt, och föreskrifterna gäller även för privatpersoner. För Södra Mälaren finns föreskrifterna hos Länsstyrelsen.",
       "I Länsstyrelsens föreskrifter för Östra Mälaren omfattar den primära skyddszonen bland annat landområdet intill 50 meter från strandlinjen vid medelvattenstånd. Mark- och anläggningsarbeten inom tomtmark får utföras utan tillstånd, men utfyllnad och återfyllnad av schakt får bara göras med rena massor. Ny lagring av mer än 250 liter brandfarlig vätska, som diesel, ska i den primära zonen ha ett sekundärt skydd, och hantering av kemikalier och färger får inte ske om den kan förorena vattnet.",
       "På en byggplats nära stranden påverkar det var maskiner tankas, var färg och lim förvaras och vilka massor som körs in till grunden. Vi går igenom föreskrifterna för just din tomt innan etableringen planeras.",
     ],
     "aside": {"title": "I primär skyddszon", "items": [
       "50 meter från strandlinjen",
       "Bara rena massor vid återfyllnad",
       "Sekundärt skydd över 250 liter bränsle",
       "Tillstånd för ny energianläggning"]}},
    {"id": "bergvarme-ekero", "h2": "Bergvärme till det nya huset",
     "paras": [
       "Ska huset värmas med berg-, jord- eller ytvattenvärme krävs tillstånd från kommunen innan anläggningen installeras. En luftvärmepump kräver inget tillstånd. Till ansökan hör en skalenlig situationsplan med energibrunnarna inritade, gärna i skala 1:400 eller 1:500, och kommunen erbjuder en bergvärmekarta utan kostnad. Enligt Östra Mälarens föreskrifter får nya energianläggningar i den primära skyddszonen inte anläggas utan tillstånd.",
       "Grannarna ska få yttra sig. Där det saknas kommunalt vatten och avlopp räknas alla grannar vars fastighetsgräns ligger närmare än 30 meter från anläggningen som berörda, där alla är anslutna gäller 20 meter. Miljöenheten kontaktar grannarna, som har två veckor på sig. Miljönämnden kräver att energibrunnar anläggs enligt SGU:s Normbrunn 16.",
       "Kommunen påpekar att Ekerö ligger inom ett område som för länge sedan låg under havsytan, så djupt grundvatten kan vara påverkat av salt. Kloridhalten ska mätas under borrningen, och visar den mer än 100 mg/l ska borrhålet tätas. Läs mer om att bygga " + _L.format("nybyggnad-villa.html", "nytt hus") + " och om arbetssättet under " + _L.format("byggfirma.html", "byggfirma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi upp ett nybygge på Ekerö",
  "steps": [
    ("Platsbesök", "Vi tittar på tomten, avståndet till vattnet och var huset kan stå."),
    ("Plan och strandskydd", "Ekerökartan visar detaljplan och vi bedömer om dispens behövs."),
    ("Förhandsbesked", "Karta och situationsplan tas fram för kommunens prövning av platsen."),
    ("Skriftligt kostnadsförslag", "Grund, stomme, värme och installationer redovisas var för sig."),
    ("Bygglov och tillstånd", "Bygglov, avlopp och bergvärme söks i rätt ordning."),
    ("Bygge och slutbesked", "En kontakt för alla hantverkare fram till slutbeskedet."),
  ],
  "rot_h2": "Rotavdrag på Ekerö",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Du ska äga bostaden när arbetet görs, och material och resor ger inget avdrag.",
    "Ett helt nytt hus ger inte rotavdrag. Bygger du i stället till ett befintligt hus ger tillbyggnaden avdrag om den sitter ihop med ytterväggen till minst 75 procent eller har en dörr emellan, och markarbeten för husets värmeförsörjning kan ge avdrag. Vi gör avdraget direkt på fakturan där det gäller.",
  ],
  "price_h2": "Vad påverkar kostnaden på Ekerö?",
  "price": [
    "Grundläggning, avståndet till vatten och avlopp, valet av värmekälla och hur långt material ska transporteras väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi söka förhandsbesked för en tomt inom detaljplan på Ekerö?",
     "Nej. Ekerö kommun skriver att förhandsbesked inte kan sökas inom detaljplanerat område, eftersom planen redan anger hur du får bygga. Då söker du bygglov direkt."),
    ("Hur länge gäller ett positivt förhandsbesked från Ekerö kommun?",
     "I två år från dagen då beslutet vann laga kraft. Inom den tiden behöver du söka bygglov."),
    ("Gäller vattenskyddsföreskrifterna även vår villatomt på Ekerö?",
     "Ja. Kommunen skriver att hela Ekerö ligger inom skyddsområde för vattentäkt sedan 1 juni 2024 och att föreskrifterna även gäller allmänheten."),
    ("Vilka grannar får yttra sig om vår bergvärme på Ekerö?",
     "Där det saknas kommunalt vatten och avlopp räknas grannar med fastighetsgräns närmare än 30 meter, annars 20 meter. Miljöenheten kontaktar dem och de har två veckor på sig."),
    ("Ska vi söka strandskyddsdispens före förhandsbeskedet?",
     "Ekerö kommun rekommenderar det om du vill bygga inom strandskyddat område. Dispens kräver särskilda skäl."),
  ],
  "sources": [
    ("Ekerö kommun – Förhandsbesked", _EK + "bygga-nytt-andra-eller-riva/forhandsbesked"),
    ("Ekerö kommun – Strandskydd, bryggor och sjöbodar", _EK + "bygga-nytt-andra-eller-riva/strandskydd-bryggor-och-sjobodar"),
    ("Ekerö kommun – Vattenskyddsområden", _EK + "sjoar-och-vattendrag/vattenskyddsomraden"),
    ("Länsstyrelsen i Stockholms län – Skyddsföreskrifter för Östra Mälarens vattenskyddsområde (2008)",
     "https://www.ekero.se/download/18.4076f060192ae0f089a8838c/1730368606194/F%C3%B6reskrifter%20f%C3%B6r%20%C3%B6stra%20M%C3%A4larens%20vattenskyddsomr%C3%A5de.pdf"),
    ("Ekerö kommun – Värmepumpar och bergvärme", _EK + "energi-och-uppvarmning/varmepumpar-och-bergvarme"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Funderar ni på att bygga nytt på Ekerö?", "Boka ett gratis platsbesök, så går vi igenom platsen, strandskyddet och värmen innan något ritas."),
  "img": [
    ("Obebyggd mark med högt gräs och tallar ned mot Mälaren",
     "undeveloped Swedish countryside building plot with tall grass, scattered pine trees and smooth granite outcrops sloping gently down towards a calm lake Mälaren bay in the distance, a gravel road along the edge, a few wooden survey stakes in the grass, Ekerö Stockholm, late summer daylight, empty scene"),
    ("Borrigg på en nygjuten grundplatta bredvid ett nytt hus bland tallar",
     "geothermal drilling rig with a vertical mast standing on a construction site plot next to a freshly cast concrete foundation slab of a new Swedish house, gravel, pine trees in the background, overcast daylight, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HÄSSELBY
"byggforetag-hasselby.html": {
  "kind": "district", "service": "byggforetag", "ort": "Hässelby", "svc_label": "Byggföretag",
  "title": "Byggföretag i Hässelby – riva, bygga nytt och delad tomt",
  "description": "Byggföretag i Hässelby: riva ett äldre hus, bygga nytt på en delad tomt i villastaden, marklov, träd och stadens krav före startbesked.",
  "h1": "Byggföretag i Hässelby",
  "lead": "Hässelby villastad har förändrats i omgångar: stora tomter har delats, äldre villor har ersatts och nya hus har byggts mellan de gamla. Står du inför att riva ett uttjänt hus eller bygga på en avstyckad del av tomten är det ett nybygge med allt vad det innebär. Geal Entreprenad AB tar sådana projekt som total entreprenad, och här är ordningen som Stockholms stad kräver.",
  "card": "Riva, bygga nytt och delad tomt.",
  "sections": [
    {"id": "villastad-hasselby", "anchor": "Villastaden",
     "h2": "En villastad som har delats och byggts på",
     "paras": [
       "I Stockholms stads vägledning Varsam utveckling av småhus- och villaområden räknas Hässelby villastad till typen villastad, tillsammans med bland annat Bromsten, Mariehäll och Mälarhöjden. De första planerna gav fritt liggande hus på tomter om 1 500–3 000 kvadratmeter, och när nya planer togs fram under 1930-talet blev tomterna 700–1 000 kvadratmeter.",
       "Vägledningen beskriver hur många villor på 1960- och 1970-talen ersattes av täta, sammanhållna grupper av småhus, bland annat i Hässelby villastad. Genom att tomter successivt har delats har nya hus på tomter kring 600 kvadratmeter kompletterat eller ersatt den äldre bebyggelsen, och förtätningen tog ny fart under 2010-talet. Därför kan ett byggprojekt här lika gärna gälla ett helt nytt hus som en tillbyggnad.",
     ],
     "aside": {"title": "Tomterna enligt vägledningen", "items": [
       "Först 1 500–3 000 kvadratmeter",
       "Från 1930-talet 700–1 000",
       "Nya hus kring 600 kvadratmeter",
       "Ny förtätning på 2010-talet"]}},
    {"id": "riva-hasselby", "h2": "Rivningslov eller rivningsanmälan",
     "paras": [
       "Inom detaljplan krävs rivningslov för att riva en byggnad eller en del av en byggnad. I prövningen gör staden en samlad bedömning av om byggnaden bör bevaras med hänsyn till sitt historiska, kulturhistoriska, miljömässiga eller konstnärliga värde och om rivningen stämmer med detaljplanen. Ska ett hus flyttas krävs rivningslov på den gamla platsen och bygglov på den nya.",
       "En byggnad som får byggas utan bygglov, till exempel en friggebod, kan rivas utan rivningslov om den eller området inte är särskilt kulturhistoriskt värdefullt. Behövs inget rivningslov men byggnadsarean är större än 50,0 kvadratmeter ska rivningen i stället anmälas. Vid det tekniska samrådet går staden bland annat igenom hur förekomsten av farligt avfall har inventerats, och den inventeringen ska vara gjord innan första väggen tas ned.",
     ],
     "aside": None},
    {"id": "nytt-hasselby", "h2": "Det nya huset: karta, kontrollansvarig och tidsgränser",
     "paras": [
       "En ny byggnad kräver bygglov. Redan i ansökan ska det enligt Stockholms stad finnas ett förslag på kontrollansvarig, och den som söker ansvarar för att den föreslagna har åtagit sig uppdraget. Situationsplanen ritas på en nybyggnadskarta, som visar fastigheten, markhöjder, planbestämmelser och anslutningarna för vatten och avlopp.",
       "Staden ska besluta inom tio veckor från att ansökan bedömts komplett och kan förlänga med ytterligare tio veckor. Staden skriver också att det just nu tar längre tid än vanligt att få en handläggare. Även när startbeskedet kommer samtidigt med lovet ska man vänta fyra veckor efter att beslutet kungjorts innan bygget börjar. Bygget ska påbörjas inom två år och vara färdigt inom fem år från beslutsdatum.",
       "Vägledningen för villastaden ger stöd för utformningen. Ett nytt huvudhus ska inordna sig i områdets planstruktur, anpassas till terrängen om tomten är kuperad och ha en volym och proportioner som samspelar med husen intill. Staden vill också undvika fler utfarter bredvid varandra och att grönytor hårdgörs, vilket påverkar var garage och parkering hamnar på en delad tomt.",
     ],
     "aside": {"title": "Med i ansökan", "items": [
       "Situationsplan på nybyggnadskarta",
       "Förslag på kontrollansvarig",
       "Fackmannamässiga ritningar",
       "Utformning efter platsen"]}},
    {"id": "mark-hasselby", "h2": "Mark, dagvatten och träd på tomten",
     "paras": [
       "Inom detaljplan krävs marklov om marknivån höjs eller sänks mer än 0,5 meter. Markändringen får inte leda dagvatten in på en annan fastighet, eftersom dagvattnet ska tas om hand på den egna tomten. Staden tipsar om e-tjänsten Ledningskollen för att få veta var ledningar går innan man gräver, och om berg ska sprängas eller spräckas kan även det kräva marklov.",
       "Detaljplanen kan också kräva marklov för att fälla träd eller förbjuda trädfällning helt, och det gäller oavsett om trädet är levande, sjukt eller dött. Mycket stora, gamla eller grova hålträd räknas som särskilt skyddsvärda, och då ska man samråda med länsstyrelsen innan trädet fälls eller beskärs. Vill du hellre bygga ut det befintliga huset, läs om " + _L.format("tillbyggnad.html", "tillbyggnad") + " och om " + _L.format("nybyggnad-villa.html", "nybyggnad av villa") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi upp ett nybygge i Hässelby",
  "steps": [
    ("Platsbesök", "Vi går igenom huset som ska bort, tomten, träden och grannarnas hus."),
    ("Plan och klassificering", "Detaljplan och Stadsmuseets karta visar vad som får rivas och byggas."),
    ("Skriftligt kostnadsförslag", "Rivning, mark, grund, stomme och installationer redovisas var för sig."),
    ("Rivningslov och bygglov", "Ansökan lämnas med nybyggnadskarta och förslag på kontrollansvarig."),
    ("Tekniskt samråd", "Kontrollplan och inventering av farligt avfall gås igenom med staden."),
    ("Bygge och slutbesked", "En kontakt för hela bygget fram till slutbeskedet."),
  ],
  "rot_h2": "Rotavdrag när du river och bygger nytt",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag, och det gäller bara arbete på en bostad du äger.",
    "Skatteverket godkänner inte att riva ett hus, inte ens om ett nytt byggs upp på den gamla stommen, och ett helt nytt hus ger inte heller avdrag. Bygger du i stället om eller till det hus du har kan arbetet ge rotavdrag. Det redovisar vi tydligt i kostnadsförslaget.",
  ],
  "price_h2": "Vad påverkar kostnaden i Hässelby?",
  "price": [
    "Rivningens omfattning, hur mycket farligt avfall som finns, markförhållandena och husets storlek väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi rivningslov för att riva vårt gamla hus i Hässelby?",
     "Inom detaljplan krävs rivningslov för att riva en byggnad. Staden prövar då om huset bör bevaras och om rivningen stämmer med detaljplanen."),
    ("När räcker det med en rivningsanmälan i Stockholms stad?",
     "När rivningslov inte krävs men byggnadsarean är större än 50,0 kvadratmeter. Mindre lovfria byggnader som en friggebod kan rivas utan lov om de inte är särskilt kulturhistoriskt värdefulla."),
    ("Hur länge gäller ett bygglov för ett nytt hus i Stockholm?",
     "Bygget ska påbörjas inom två år och vara färdigt inom fem år från beslutsdatum, enligt Stockholms stad."),
    ("Får vi fälla träden på tomten innan vi bygger i Hässelby?",
     "Det beror på detaljplanen. Den kan kräva marklov eller förbjuda trädfällning, oavsett om trädet lever. För särskilt skyddsvärda träd ska man samråda med länsstyrelsen."),
    ("Ger det rotavdrag att riva huset innan vi bygger nytt?",
     "Nej. Skatteverket godkänner inte rivning av ett hus, och ett helt nytt hus ger inte heller avdrag."),
  ],
  "sources": [
    _SB_VARSAM,
    ("Stockholms stad – Rivning", _SB + "rivning/rivning/"),
    ("Stockholms stad – Villa eller småhus, nybyggnad och ändringar", _SB + "bygga-nytt-och-bygga-till/villa-eller-smahus-nybyggnad-och-andringar/"),
    _SB_GUIDE,
    ("Stockholms stad – Schaktning och fyllning av mark", _SB + "andra-mark/schaktning-och-fyllning-av-mark/"),
    ("Stockholms stad – Fälla eller ta bort träd", _SB + "andra-mark/tradfallning/"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ni riva och bygga nytt i Hässelby?", "Boka ett gratis platsbesök, så går vi igenom rivningen, tomten och ordningen hos staden."),
  "img": [
    ("Nybyggd vit villa i två plan bredvid en äldre villa bakom klippta häckar i Hässelby",
     "newly built modern Swedish two-storey family house with light grey wooden facade and dark gable roof on a divided garden plot, next to an older 1930s wooden villa with red clay tile roof, both behind low hedges along a narrow residential street, mature birch and apple trees, Hässelby Stockholm, early autumn daylight, empty scene"),
    ("Röjd villatomt med träreglar som markerar det nya husets grund mellan grannvillor",
     "cleared flat Swedish suburban building plot of bare soil and gravel after an old house was demolished, simple wooden batter boards and taut string lines marking the rectangular outline of a new house, a few mature birch trees left standing at the edges, neighbouring villas with tiled roofs behind trimmed hedges, overcast daylight, no machines, no vehicles, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ENSKEDE
"byggforetag-enskede.html": {
  "kind": "district", "service": "byggforetag", "ort": "Enskede", "svc_label": "Byggföretag",
  "title": "Byggföretag i Enskede – byggplatsen, gatan och träden",
  "description": "Byggföretag i Enskede: polistillstånd för container och ställning på gatan, bygglov för bodar, schakt i gatumark och skydd för gatuträd.",
  "h1": "Byggföretag i Enskede",
  "lead": "I Enskedes trädgårdsstad och på småstugegatorna står husen nära gatan, häckarna är täta och utrymmet framför tomten är litet. En tillbyggnad eller större ombyggnad kräver ändå plats för container, material och ibland en ställning. Geal Entreprenad AB tar byggprojekt som total entreprenad, och i Enskede hör planeringen av själva byggplatsen till det första vi gör.",
  "card": "Byggplatsen, gatan och träden.",
  "sections": [
    {"id": "gatorna-enskede", "anchor": "Gatorna",
     "h2": "Smala gator och hus nära tomtgränsen",
     "paras": [
       "Gamla Enskede blev Stockholms första trädgårdsstad och anlades efter Per Olof Hallmans stadsplan från 1908, skriver staden i vägledningen Varsam utveckling av småhus- och villaområden. Gatorna fick ett slingrande mönster som följer terrängen. På Enskedefältet och i de andra småstugeområdena kantas de smalare gatorna oftast av häckar, och husen står i liv med gatan eller med en liten förgårdsmark.",
       "För ett byggprojekt betyder det att tomten sällan räcker till allt. Staden skriver att en byggetablering bör placeras i anslutning till byggarbetsplatsen och på den egna fastigheten om det går. Får containern och materialet inte plats där blir gatan nästa alternativ, och då gäller andra regler.",
     ],
     "aside": None},
    {"id": "tillstand-enskede", "h2": "Polistillstånd för allt som står på gatan",
     "paras": [
       "I områden med detaljplan behövs enligt ordningslagen polistillstånd för att använda offentlig plats till byggbodar, upplag, byggplank, ställningar, mobilkranar och liknande. Staden påpekar att marken utanför en fastighet räknas som offentlig plats om allmänheten har eller har haft tillträde till den, oavsett vem som äger den. Polisen skickar ansökan på remiss till trafikkontoret, och om trafikkontoret avstyrker får polisen inte utfärda tillståndet. Tillstyrker kontoret kan det ställa villkor.",
       "Tillståndet ska vara utfärdat innan platsen används, och där står vilka datum som gäller och vilken yta du får använda. I en container eller byggsäck som allmänheten kommer åt får brandfarliga eller hälsofarliga vätskor inte förvaras. Två avgifter tas ut: en administrationsavgift till polisen och en avgift till staden som beror på vilken avgiftszon platsen ligger i.",
       "Står en ställning över gångbanan ska enligt stadens villkor minst 1,6 meter vara fritt under den eller minst 2 meter finnas kvar för gående. En byggskylt får vara högst 15 kvadratmeter per byggprojekt. Ska en mobilkran ställas upp krävs ett eget polistillstånd.",
     ],
     "aside": {"title": "Kräver polistillstånd", "items": [
       "Container och byggsäck på gatan",
       "Byggbod och upplag",
       "Byggställning över gångbanan",
       "Mobilkran och lift"]}},
    {"id": "bygglov-enskede", "h2": "Bygglov för bod och container",
     "paras": [
       "Utöver polistillståndet kan bygglov behövas. Stockholms stad skriver att tillfälliga byggbodar kräver bygglov och att även byggplank, skyltar, upplag och container kan behöva lov. Om containern används som upplag behövs oftast bygglov, och ska människor vistas i den räknas den som en byggnad. Ett glest byggstängsel kräver däremot inget bygglov.",
       "Kontorsarbetsplatser och besöksutrymmen i byggbodar ska dessutom vara tillgängliga för personer med nedsatt rörelse- eller orienteringsförmåga. Vi planerar därför hellre en mindre etablering på tomten än en större ute på gatan.",
     ],
     "aside": None},
    {"id": "schakt-enskede", "h2": "Gräva i gatan och skydda träden",
     "paras": [
       "Ska något göras i gatu- eller parkmark, som att dra en ny ledning, borra för bergvärme eller bara lyfta bort trottoarplattor framför fasaden, krävs schakt- och öppningstillstånd. För fastighetsägare och byggherrar är handläggningstiden för en komplett ansökan normalt sex veckor, enligt trafikkontoret. En samlingskarta beställs samtidigt, och en godkänd trafikanordningsplan behövs. Den som gräver ska ha gått stadens utbildning Trafikanordningar och markarbeten i offentlig mark, som även gäller underentreprenörer och ska gås om vart femte år.",
       "Träd ska enligt stadens anvisningar för byggprojekt skyddas, och föremål får inte placeras inom trädkronans utbredning, den så kallade droppzonen. Gatuträd får inte beskäras utan trafikkontorets medgivande, och träd på stadens mark får inte fällas. Står ett träd på din tomträtt behöver du inte stadens godkännande för att fälla det, men detaljplanen kan ändå kräva marklov. Mer om att bygga ut ett hus här finns på sidan om " + _L.format("tillbyggnad-enskede.html", "tillbyggnad i Enskede") + ".",
     ],
     "aside": {"title": "Före grävningen", "items": [
       "Schakttillstånd, normalt sex veckor",
       "Samlingskarta",
       "Trafikanordningsplan",
       "Utbildning för den som gräver"]}},
  ],
  "steps_h2": "Så planerar vi byggplatsen i Enskede",
  "steps": [
    ("Platsbesök", "Vi mäter upp tomten, infarten, gatan och träden framför huset."),
    ("Etableringsplan", "Container, material och eventuell bod placeras i första hand på tomten."),
    ("Skriftligt kostnadsförslag", "Etablering, rivning, bygge och återställning redovisas var för sig."),
    ("Tillstånd", "Polistillstånd, bygglov för etableringen och schakttillstånd söks i tid."),
    ("Bygge", "En kontakt för alla hantverkare och för grannarnas frågor."),
    ("Återställning", "Gatan och marken lämnas i ordning när etableringen tas bort."),
  ],
  "rot_h2": "Rotavdrag för byggprojekt i Enskede",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Det gäller arbetet, inte material eller resor.",
    "En tillbyggnad ger avdrag om den sitter ihop med husets yttervägg till minst 75 procent eller har en dörr emellan. Ett nytt hus eller en fristående byggnad som ett garage ger inget avdrag. Vi gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Enskede?",
  "price": [
    "Hur mycket som får plats på tomten, om gatan behöver användas och hur länge etableringen står kvar påverkar kostnaden utöver själva bygget. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi ställa en container på gatan utanför vårt hus i Enskede?",
     "Bara med polistillstånd, som ska vara utfärdat innan containern ställs ut. Polisen frågar trafikkontoret först, och om kontoret säger nej blir det inget tillstånd."),
    ("Behöver en byggbod på tomten bygglov i Stockholm?",
     "Ja. Stockholms stad skriver att tillfälliga byggbodar kräver bygglov. Även upplag, byggplank och container kan behöva lov."),
    ("Hur lång tid tar ett schakttillstånd i Stockholms stad?",
     "För fastighetsägare och byggherrar normalt sex veckor för en komplett ansökan, enligt trafikkontoret. Samlingskarta och trafikanordningsplan behövs också."),
    ("Får vi fälla ett träd på vår tomträtt i Enskede?",
     "Staden skriver att du inte behöver stadens godkännande för ett träd inom en tomträtt. Detaljplanen kan ändå kräva marklov, så kontrollera den först."),
    ("Hur mycket fri höjd ska det vara under en byggställning på trottoaren?",
     "Enligt stadens villkor minst 1,6 meter fritt under ställningen, eller minst 2 meter kvar för gående på gångbanan."),
  ],
  "sources": [
    _SB_VARSAM,
    ("Stockholms stad – Använda offentlig plats för byggverksamhet", _TS + "anvanda-offentlig-plats/anvanda-offentlig-plats-for-byggverksamhet/"),
    ("Stockholms stad – Ställa byggsäckar, containrar och fristående bodar på offentlig plats", _TS + "anvanda-offentlig-plats/stalla-byggsackar-containrar-och-fristaende-bodar-pa-offentlig-plats/"),
    ("Stockholms stad – Mark- och gatuarbeten på offentlig mark", _TS + "mark--och-gatuarbeten/gatuarbeten-pa-offentlig-mark/"),
    ("Stockholms stad – Bra att veta för dig som planerar byggprojekt (2019)",
     "https://tillstand.stockholm/globalassets/foretag-och-organisationer/tillstand-och-regler/tillstand-regler-och-tillsyn/anvanda-offentlig-plats/anvanda-offentlig-plats-for-byggverksamhet/bra-att-veta-for-dig-som-planerar-byggprojekt-20191220.pdf"),
    ("Stockholms stad – Container", _SB + "bygga-nytt-och-bygga-till/container/"),
    ("Stockholms stad – Byggbod, byggetablering, byggskylt", _SB + "bygga-nytt-och-bygga-till/byggbod-byggetablering-byggskylt/"),
    ("Stockholms stad – Fälla eller ta bort träd", _SB + "andra-mark/tradfallning/"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ni bygga i Enskede men har ont om plats?", "Boka ett gratis platsbesök, så planerar vi byggplatsen, tillstånden och tidplanen."),
  "img": [
    ("Smal gata med häckar, gatuträd och trähus med branta tegeltak i Enskede",
     "narrow quiet residential street in an old Swedish garden city with small one-and-a-half storey wooden houses painted in muted red and yellow, steep red clay tile roofs, dense trimmed hedges and picket fences close to the street, street trees, Enskede Stockholm, spring daylight, empty scene, no cars"),
    ("Staplat byggvirke på pallar framför ett rött trähus vid gatan, med ett stort gatuträd",
     "a neatly stacked pile of new timber planks on pallets on the gravel driveway of a small old red Swedish wooden house with steep roof, trimmed hedge along the street, a large leafy tree on the pavement with a simple temporary wooden protective fence around its trunk, plain unmarked surfaces, daylight, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SIGTUNA
"byggforetag-sigtuna.html": {
  "kind": "district", "service": "byggforetag", "ort": "Sigtuna", "svc_label": "Byggföretag",
  "title": "Byggföretag i Sigtuna – nytt hus, gästhus och större tomt",
  "description": "Byggföretag i Sigtuna: bygglov och handlingar för nytt småhus, regler för komplementbostadshus, köpa till kommunal mark och vatten och avlopp.",
  "h1": "Byggföretag i Sigtuna",
  "lead": "I Sigtuna kommun, från Märsta och Rosersberg till Sigtuna stad och landsbygden runt omkring, kan ett större byggprojekt vara ett nytt hus eller ett extra bostadshus på tomten. Geal Entreprenad AB bygger nytt och bygger till som total entreprenad, och här är vad kommunen kräver för ett nytt småhus, när ett gästhus behöver bygglov och hur man gör om tomten är för liten.",
  "card": "Nytt hus, gästhus och större tomt.",
  "sections": [
    {"id": "nytt-sigtuna", "anchor": "Nytt småhus",
     "h2": "Nytt en- eller tvåbostadshus kräver bygglov",
     "paras": [
       "Sigtuna kommun skriver att ett nytt eller flyttat en- eller tvåbostadshus kräver bygglov, oavsett om tomten ligger inom eller utanför detaljplan, och att bygget får börja först efter startbeskedet. Radhus, parhus, kedjehus och fritidshus kan räknas som en- eller tvåbostadshus, kolonistugor gör det inte. Beslut ska komma inom tio veckor från att ansökan är komplett, och tiden kan förlängas en gång med tio veckor för stora eller komplicerade projekt.",
       "Till ansökan hör en anmälan av kontrollansvarig, en situationsplan på nybyggnadskarta, en markplaneringsritning, byggnadsritningar och en exteriörredovisning. Nybyggnadskartan ska vara uppdaterad och beställs från kommunens geodataenhet. Utanför detaljplan kan kommunen behöva ett godkänt avloppstillstånd innan bygglovet prövas, och kommunen rekommenderar att den kontrollansvarige knyts till projektet tidigt.",
       "Ritningarna görs i skala 1:100. Planritningen ska vara möblerad så att tillgängligheten kan bedömas, fasadritningen ska visa befintliga och nya marklinjer fram till gatan och grannfastigheterna, och sektionen ska ha plushöjder för sockel och färdigt golv. Kommunen vill också ha ett färg-PM och ytuppgifter för byggnadsarea, bruttoarea, öppen area och boarea.",
     ],
     "aside": {"title": "Ansökan för nytt hus", "items": [
       "Anmälan av kontrollansvarig",
       "Situationsplan på nybyggnadskarta",
       "Markplaneringsritning",
       "Färg-PM och ytuppgifter"]}},
    {"id": "komplement-sigtuna", "h2": "Ett extra bostadshus på tomten",
     "paras": [
       "Ett komplementbostadshus är en fristående byggnad som är inredd som en egen bostad, till exempel för uthyrning eller som gäststuga. Det kräver bygglov om byggnadsarean är större än 30 kvadratmeter inom detaljplan eller 50 kvadratmeter utanför, om nockhöjden överstiger 4 meter inom plan eller 4,5 meter utanför, om huset är lika stort som eller större än huvudbyggnaden, eller om det placeras närmare tomtgränsen än 4,5 meter utan grannens skriftliga medgivande.",
       "Alla lovbefriade byggnader på tomten delar på en gemensam pott: högst 45 kvadratmeter inom detaljplan och 65 kvadratmeter utanför. Kommunen ger exemplet att en friggebod på 15 kvadratmeter och ett attefallshus på 30 kvadratmeter inom plan tar hela potten. Lov krävs också vid särskilt värdefulla byggnader eller i särskilt värdefulla områden och där detaljplanen eller områdesbestämmelser har utökad lovplikt.",
       "Även utan bygglov ska en anmälan göras om vatten, avlopp eller ventilation installeras eller om brandskyddet påverkas. Till ansökan eller anmälan hör konstruktionsritningar för grund, stomme och tak, en teknisk beskrivning och ett förslag till kontrollplan, och entréplanet ska vara tillgängligt. Kommunen bedömer i varje ärende om en kontrollansvarig behövs. Mer om regelverket finns på sidan om " + _L.format("attefallshus-regler.html", "attefallshus och regler") + ".",
     ],
     "aside": {"title": "Gräns för lovfrihet", "items": [
       "30 kvm inom plan, 50 utanför",
       "Nock 4 eller 4,5 meter",
       "4,5 meter från tomtgränsen",
       "Pott 45 eller 65 kvm"]}},
    {"id": "mark-sigtuna", "h2": "När tomten är för liten",
     "paras": [
       "Räcker inte tomten för det man vill bygga är det ibland kommunens mark som ligger närmast. Sigtuna kommun skriver att en sådan bit inte går att köpa i alla lägen, eftersom detaljplanen kan ange att marken ska vara till för allmänheten, och då får kommunen inte sälja den.",
       "Går det att sälja behöver Lantmäteriet först göra en lantmäteriförrättning, marken värderas, köpehandlingar upprättas och Lantmäteriet gör en marköverföring. Köparen betalar marknadsvärdet för marken och Lantmäteriets handläggningskostnader. Det tar tid, så frågan bör vara utredd innan huset ritas in mot den nya gränsen.",
     ],
     "aside": None},
    {"id": "va-sigtuna", "h2": "Vatten och avlopp i planeringen",
     "paras": [
       "Sedan 1 januari 2023 ska varje kommun ha en aktuell vattentjänstplan för hur behovet och utbyggnaden av allmänt vatten och avlopp ska tillgodoses. Sigtuna kommun och det kommunala VA-bolaget SIVAB har tagit fram en sådan plan, som nu är beslutad i kommunfullmäktige, med en karta över verksamhetsområdena för vatten, avlopp och dagvatten.",
       "Kartan visar om tomten kan anslutas eller om vatten och avlopp behöver lösas på egen hand. Ligger tomten utanför detaljplan kan kommunen dessutom behöva ett godkänt avloppstillstånd för att pröva bygglovet. Sigtunakartan visar dessutom var en detaljplan gäller, är på gång eller utreds. Läs mer om " + _L.format("nybyggnad-villa.html", "nybyggnad av villa") + " och om hela arbetssättet under " + _L.format("byggfirma.html", "byggfirma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi upp ett nybygge i Sigtuna",
  "steps": [
    ("Platsbesök", "Vi tittar på tomten, gränserna och var huset eller gästhuset kan stå."),
    ("Plan och VA", "Sigtunakartan och verksamhetsområdet för vatten och avlopp kontrolleras."),
    ("Kartor och ritningar", "Nybyggnadskarta beställs och ritningarna tas fram i rätt skala."),
    ("Skriftligt kostnadsförslag", "Mark, grund, stomme och installationer redovisas var för sig."),
    ("Ansökan och startbesked", "Bygglov eller anmälan med kontrollplan, sedan tekniskt samråd vid behov."),
    ("Bygge och slutbesked", "En kontakt för alla hantverkare fram till slutbeskedet."),
  ],
  "rot_h2": "Rotavdrag för byggprojekt i Sigtuna",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Du ska äga bostaden när arbetet görs.",
    "Ett helt nytt hus ger inte rotavdrag, och inte heller en fristående byggnad som en gäststuga eller ett komplementbostadshus. En tillbyggnad på befintligt hus ger avdrag om den sitter ihop med ytterväggen till minst 75 procent eller har en dörr emellan. Vi särskiljer det i kostnadsförslaget och gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Sigtuna?",
  "price": [
    "Husets storlek, grundläggningen, om avloppet ska lösas på tomten och hur mycket mark som ska planeras väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för ett nytt hus utanför detaljplan i Sigtuna?",
     "Ja. Sigtuna kommun skriver att ett nytt en- eller tvåbostadshus kräver bygglov både inom och utanför detaljplan. Utanför plan kan kommunen också behöva ett godkänt avloppstillstånd."),
    ("Hur stort gästhus får vi bygga utan bygglov i Sigtuna?",
     "Ett komplementbostadshus får ha högst 30 kvadratmeter byggnadsarea inom detaljplan och 50 utanför, och alla lovfria byggnader delar på en pott om 45 respektive 65 kvadratmeter."),
    ("Kan vi köpa kommunens mark bredvid vår tomt i Sigtuna?",
     "Det beror på detaljplanen. Anger den att marken är till för allmänheten får kommunen inte sälja den. Annars krävs lantmäteriförrättning, värdering och marköverföring."),
    ("Vilka ritningar vill Sigtuna kommun ha för ett nytt småhus?",
     "Plan-, fasad- och sektionsritningar i skala 1:100, situationsplan på nybyggnadskarta, markplaneringsritning, färg-PM och ytuppgifter."),
    ("Ger ett komplementbostadshus rotavdrag?",
     "Nej. Skatteverket godkänner inte avdrag för att bygga en fristående byggnad eller ett helt nytt hus."),
  ],
  "sources": [
    ("Sigtuna kommun – Nybyggnation av en- och tvåbostadshus", _SI + "bygglov/vad-ska-du-bygga/bygga-nytt/nybyggnation-av-en--och-tvabostadshus.html"),
    ("Sigtuna kommun – Komplementbostadshus", _SI + "bygglov/vad-ska-du-bygga/bygga-nytt/komplementbostadshus.html"),
    ("Sigtuna kommun – Försäljning av små markområden, komplettering av småhustomter",
     _SI + "mitt-boende/hitta-bostad-och-lediga-tomter/forsaljning-av-sma-markomraden-komplettering-av-smahustomter.html"),
    ("Sigtuna kommun – Vattentjänstplan", _SI + "mitt-boende/vatten-och-avlopp/vattentjanstplan.html"),
    ("Sigtuna kommun – Bygga nytt", _SI + "bygglov/vad-ska-du-bygga/bygga-nytt.html"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Planerar ni ett nytt hus eller gästhus i Sigtuna?", "Boka ett gratis platsbesök, så går vi igenom tomten, lovfrågan och handlingarna."),
  "img": [
    ("Nybyggt hus i ljust trä med svart plåttak, takkupa och unga björkar på en ny villatomt",
     "newly built Swedish single-storey family house with light natural wood panel facade, black metal roof and large windows on a fresh residential plot, newly laid lawn, young birch saplings, gravel driveway, other modern houses in the background, flat Uppland landscape, Märsta Sigtuna, summer daylight, empty scene"),
    ("Litet svart gästhus i trä med glasdörr och trädäck i trädgården framför en vit villa",
     "small detached single-storey guest cottage with dark painted wooden facade, black pitched roof, a glass door and a small wooden deck, standing in a lawn garden behind a larger light Swedish villa, low hedge and fruit trees, soft summer daylight, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"byggforetag-upplands-vasby.html": {
  "kind": "district", "service": "byggforetag", "ort": "Upplands Väsby", "svc_label": "Byggföretag",
  "title": "Byggföretag i Upplands Väsby – karta, VA och tomtgräns",
  "description": "Byggföretag i Upplands Väsby: rätt karta till bygglovet, anslutning till kommunalt VA, avstyckning och regler för lovfri tillbyggnad på 30 kvm.",
  "h1": "Byggföretag i Upplands Väsby",
  "lead": "Innan ett nytt hus eller en större tillbyggnad i Upplands Väsby kan ritas klart behöver tre saker vara på plats: en karta som håller för bygglovet, en plan för hur huset ansluts till vatten och avlopp och en tydlig bild av var tomtgränsen går. Geal Entreprenad AB bygger nytt, bygger till och bygger om som total entreprenad, och här är hur kommunen hanterar de frågorna.",
  "card": "Karta, VA och tomtgräns.",
  "sections": [
    {"id": "karta-upplands-vasby", "anchor": "Rätt karta",
     "h2": "Nybyggnadskarta, förenklad karta eller kartutdrag",
     "paras": [
       "Situationsplanen ska vara i skala 1:400 och visa fastighetsgränser, alla befintliga byggnader och var det nya ska placeras. Vilken karta den ritas på beror på projektet. Kommunens geodataenhet tar fram en nybyggnadskarta för ny huvud- eller komplementbyggnad som ska anslutas till vatten och avlopp. Den visar fastighetsgränser, detaljplanebestämmelser, nivåkurvor, anslutningspunkten för vatten och avlopp och arbetsfix, och en fältkontroll ingår.",
       "Kommunen skriver att hela nybyggnadskartan ska ingå i situationsplanen och att inga ändringar får göras i den. Detaljplanen bör ha vunnit laga kraft och fastighetsbildningen vara klar innan den slutliga kartan upprättas. Annars märks kartan som preliminär, med texten att tomten är tolkad från ett förslag till detaljplan eller att förrättning pågår.",
       "För mindre tillbyggnader och tillbyggnader mer än 10 meter från fastighetsgränsen räcker en förenklad nybyggnadskarta, som ritas direkt från baskartan utan fältkontroll. För enklare åtgärder som ett uterum, ett skärmtak, en mur eller ett plank kan ett kartutdrag räcka. Det innehåller inga planbestämmelser.",
     ],
     "aside": {"title": "Kartan styrs av projektet", "items": [
       "Nytt hus: nybyggnadskarta",
       "Tillbyggnad långt från gräns: förenklad",
       "Plank eller skärmtak: kartutdrag",
       "Situationsplan i 1:400"]}},
    {"id": "va-upplands-vasby", "h2": "Anslutning till kommunalt vatten och avlopp",
     "paras": [
       "Ett nytt hus ansluts genom en servisansökan till kommunens VA-enhet, via e-tjänst eller blankett. Godkänns ansökan drar VA-enheten fram servisledningarna till fastighetsgränsen, och läget för förbindelsepunkten bestäms efter samråd med fastighetsägaren. Förbindelsepunkten är gränsen mellan den allmänna delen och fastighetens del av ledningen och ligger vanligtvis cirka 0,5 meter utanför fastighetsgränsen.",
       "Dagvatten och dräneringsvatten får inte kopplas till spillvattenservisen, och en egen brunn får inte kopplas ihop med kommunens vatten. Vill två eller flera fastigheter dela förbindelsepunkt godkänns det generellt inte för vatten, men det kan godkännas för spill- och dagvatten om det finns särskilda skäl. Då måste fastigheterna ha bildat en gemensamhetsanläggning, som söks hos Lantmäteriet. Förhållandet mellan fastighetsägaren och kommunen regleras i ABVA, som gäller sedan 1 april 2009.",
     ],
     "aside": None},
    {"id": "grans-upplands-vasby", "h2": "Stycka av och hitta gränsen",
     "paras": [
       "Upplands Väsby har ingen egen lantmäterimyndighet. Fastighetsbildningen sköts av Lantmäteriet i Stockholm, men genom ett avtal kan kommunens geodataenhet göra fältarbetet med mätning och markering vid en förrättning. Avstyckning, överföring av mark mellan fastigheter, bestämning av en gräns och bildande av en gemensamhetsanläggning söks hos Lantmäteriet.",
       "Inom detaljplan ska tomtstorlekarna vara reglerade, och avstyckningen prövas genom ansökan till Lantmäteriet. Utanför detaljplan prövas en avstyckning i stället genom ett förhandsbesked hos kommunens bygglovsenhet. Ett positivt förhandsbesked kan bifogas ansökan till Lantmäteriet, som då inte behöver hämta in kommunens medgivande. En rätt att använda grannens mark, till exempel för en ledning, kan säkras med servitut, antingen genom avtal eller genom beslut i en lantmäteriförrättning.",
     ],
     "aside": {"title": "Vem gör vad", "items": [
       "Lantmäteriet: fastighetsbildning",
       "Geodataenheten: mätning i fält",
       "Bygglovsenheten: förhandsbesked",
       "VA-enheten: servis och förbindelsepunkt"]}},
    {"id": "tillbygg-upplands-vasby", "h2": "Bygga till inom 30 kvadratmeter",
     "paras": [
       "Huvudregeln är bygglov för tillbyggnader, men kommunen beskriver ett undantag: tillbyggnader utan lov får tillsammans omfatta högst 30,0 kvadratmeter brutto- eller öppenarea på tomten. Tidigare attefallstillbyggnader, takkupor och skärmtak som byggts utan lov räknas in. Kommunens exempel är att ett skärmtak och en tillbyggnad på 10 kvadratmeter vardera lämnar 10 kvadratmeter kvar. Tillbyggnaden får inte gå över husets taknock och ska ligga minst 4,5 meter från tomtgränsen om inte grannen skriftligt godkänner något annat.",
       "Bygglov krävs ändå om huset är kulturhistoriskt värdefullt, om tillbyggnaden hamnar på allmän plats eller i ett särskilt värdefullt område, eller om detaljplanen har utökad lovplikt. Påverkas en bärande vägg, eller installeras vatten och avlopp, eldstad eller ventilation, kan det krävas anmälan. Ska marken höjas eller sänkas mer än 0,5 meter inom detaljplan krävs marklov, och då räcker vanligtvis en situationsplan och en marksektion. Mer om " + _L.format("tillbyggnad.html", "tillbyggnad") + " finns på en egen sida.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi upp ett byggprojekt i Upplands Väsby",
  "steps": [
    ("Platsbesök", "Vi tittar på tomten, gränserna och var ledningarna kan gå in."),
    ("Väsbykartan och karta", "Detaljplanen kontrolleras och rätt karta beställs till situationsplanen."),
    ("Skriftligt kostnadsförslag", "Mark, grund, stomme, VA och installationer redovisas var för sig."),
    ("Ansökan", "Bygglov eller anmälan med kontrollplan, och servisansökan till VA-enheten."),
    ("Tekniskt samråd och bygge", "Startbesked, sedan bygget med en kontakt för alla hantverkare."),
    ("Slutsamråd", "Vi förbereder underlaget till slutbeskedet."),
  ],
  "rot_h2": "Rotavdrag i Upplands Väsby",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material och resor ingår inte.",
    "En tillbyggnad ger avdrag om den sitter ihop med husets yttervägg till minst 75 procent eller har en dörr emellan. Markarbeten för att försörja ett befintligt hus med vatten och avlopp kan ge avdrag, men ett helt nytt hus ger inte avdrag. Vi drar av rotavdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Upplands Väsby?",
  "price": [
    "Grundläggning, avståndet till förbindelsepunkten, markens höjdskillnader och husets storlek väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken karta behöver vi för bygglov till ett nytt hus i Upplands Väsby?",
     "En nybyggnadskarta från kommunens geodataenhet. Den visar bland annat gränser, planbestämmelser, nivåer och anslutningspunkt för vatten och avlopp, och hela kartan ska ingå i situationsplanen."),
    ("Var ligger förbindelsepunkten för vatten och avlopp i Upplands Väsby?",
     "Vanligtvis cirka 0,5 meter utanför fastighetsgränsen. Läget bestäms av VA-enheten efter samråd med fastighetsägaren."),
    ("Får två hus i Upplands Väsby dela på samma VA-anslutning?",
     "För vatten godkänns det generellt inte. För spill- och dagvatten kan det godkännas vid särskilda skäl, om fastigheterna har bildat en gemensamhetsanläggning."),
    ("Vem styckar av en tomt i Upplands Väsby?",
     "Lantmäteriet i Stockholm, eftersom kommunen saknar egen lantmäterimyndighet. Utanför detaljplan prövas avstyckningen först genom förhandsbesked hos kommunen."),
    ("Räknas gamla attefallstillbyggnader in i kommunens 30 kvadratmeter?",
     "Ja. Upplands Väsby kommun skriver att tidigare lovfria tillbyggnader, takkupor och skärmtak räknas in i den sammanlagda arean på högst 30,0 kvadratmeter."),
  ],
  "sources": [
    ("Upplands Väsby kommun – Kart- och mättjänster", _UV + "kart--och-mattjanster"),
    ("Upplands Väsby kommun – Ledningsnät, anslutning till fastighet", _UV + "vatten-och-avlopp/ledningsnat-anslutning-till-fastighet"),
    ("Upplands Väsby kommun – Förrättningar, avstyckning", _UV + "fastigheter-och-lantmateri/lantmateri/forrattningar-avstyckning"),
    ("Upplands Väsby kommun – Kommunalt och statlig lantmäteri", _UV + "fastigheter-och-lantmateri/lantmateri/kommunalt-och-statlig-lantmateri"),
    ("Upplands Väsby kommun – Tillbyggnad", _UV + "bygga-nytt-andra-eller-riva/tillbyggnad"),
    ("Upplands Väsby kommun – Marklov", _UV + "bygga-nytt-andra-eller-riva/marklov"),
    ("Upplands Väsby kommun – Bygglovsprocessen", _UV + "bygga-nytt-andra-eller-riva/bygglovsprocessen"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ni bygga nytt eller till i Upplands Väsby?", "Boka ett gratis platsbesök, så reder vi ut kartan, anslutningen och gränsen från början."),
  "img": [
    ("Nytt hus under byggnad med väggstomme i trä på en betongplatta i ett villaområde",
     "simple rectangular new Swedish one-storey house under construction: complete bare wooden wall framing and roof trusses standing on a concrete slab, no cladding and no windows yet, gravel around the slab, neighbouring finished 1970s villas with dark concrete tile roofs behind, birch trees, Upplands Väsby, overcast daylight, no machines, empty scene"),
    ("Öppet schakt i en gräsmatta med ett orange och ett blått rör på sandbädd och utsättningspinnar",
     "straight open trench dug across a lawn of a Swedish villa garden, at the bottom two separate parallel pipes lying side by side on a sand bed: one thick orange plastic sewer pipe and one thin blue plastic water pipe, small wooden marker stakes along the edge, a low hedge in the background, daylight, empty scene"),
  ],
  "related": [],
},
}
