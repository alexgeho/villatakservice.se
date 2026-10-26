# -*- coding: utf-8 -*-
"""Attefallshus – ortsidor v22: Lidingö, Vallentuna, Järfälla, Botkyrka, Älvsjö, Sigtuna (2026-10-26).
Hubb: attefallshus.html (TJ_HUB["attefallshus"]). Regelartikel: attefallshus-regler.html.
Struktur som tj_v20_attefallshus.py. Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.

Rättslig ram (riksdagen.se, lydelse lag 2025:974, läst 2026-10-26): PBL 9 kap. 4 § (inom detaljplan 30,0 m² /
mindre än huvudbyggnaden / 4,0 m / inom tomten / 45,0 m²), 5 § (utanför 50,0 / 4,5 / 65,0), 16 § p. 2 (ändra en
komplementbyggnad till ett komplementbostadshus som enligt 4 eller 5 § inte kräver lov – inget bygglov), 34–35 §§
(4,5 m från gräns, 30,0 m från järnvägsspårs mitt, skriftligt grannmedgivande; 34 § p. 2 omfattar ändringen enligt
16 §), 36 § p. 1 (totalförsvarets flygplatser och övnings- eller skjutfält), 37 § (särskilt värdefulla byggnader och
områden).

Lokal vinkel per sida (skild från v16/v20-orterna och från ortens övriga tjänstesidor):
Lidingö – potten med gamla friggebodar och attefallshus, anmälan för ventilation/VA/eldstad/rökkanal/imkanal, stadens
  avloppsnät till Käppalaverket och LTA-enheten (villkor för drift, 1,5 m fri yta, bara spillvatten), cirka 7 150 småhus
  och cirka 50 fastigheter med eget avlopp, kulturmiljöprogrammet som kunskapsunderlag.
Vallentuna – inom/utanför plan, gäststuga (komplementbyggnad) kontra komplementbostadshus, Roslagsvatten och kommunens
  VA-anmälan med startbesked även för grävarbetet, cirka 2 800 enskilda avlopp och vad situationsplanen för avloppet
  ska visa, egen brunn (inget tillstånd för husbehov, Normbrunn 16, prov minst vart tredje år).
Järfälla – förrådet som blir bostad (PBL 9:16 p. 2), 4,5 m-regeln för ändringen (9:34 p. 2), kommunens lista över
  lovbefriade åtgärder och skyddsbestämmelser (markförorening, olyckor, översvämning, erosion), liten avvikelse,
  ansvarsgräns och förbindelsepunkt, samfällighet och ledningsservitut.
Botkyrka – webbkartans flikar och lager (Kulturmiljöprogram, Detaljplaner, Kulturmiljövård, Totalförsvaret, MSB),
  översiktsplan och gestaltningsprogram, allmän väg utanför plan, kommunens checklista för anmälan (situationsplan
  1:400 med två mått i rät vinkel, grannens påskrift av alla delägare, fasad/plan/sektion 1:100, möblerat och
  tillgängligt entréplan, tekniskt samråd, utstakning), VA-enhetens servisanmälan och mätarregeln.
Älvsjö – villastadens tomter (Hallmans plan, 1 500–3 000 m², 700–1 000 m² på 1930-talet, tomtdelning kring 600 m²),
  stadens regler för komplementbostadshus (prickmark, tillbyggnad av huset, friggebod räknas in, medgivandets
  innehåll, stadsbyggnadskontoret för allmän plats), dagvatten inom egen fastighet, SVOA:s servisanmälan.
Sigtuna – kommunens exempel på den gemensamma potten, Arlanda som riksintresse och influensområdet (Swedavia yttrar
  sig vid bygglov för nybyggnad och tillbyggnad), bedömningen av buller, avlopp och markradon, kommunens checklista
  (gratis tomtkarta, ritningar, konstruktionsritningar, teknisk beskrivning), dalgången Odensala–Hova (gårdshus).

Fakta endast från källorna i respektive 'sources', öppnade med curl (UA Mozilla) 2026-10-26, alla svarade 200
(Skatteverket först timeout, 200 vid nytt försök); pdf:erna (Varsam utveckling, Odensala–Hova) har textlager.
Motstridiga källor: Botkyrkas anmälningssida (uppdaterad 25 maj 2026) säger att ett komplementbostadshus för permanent
boende kräver anmälan, tekniskt samråd och startbesked, medan Lidingö stad skriver att själva uppförandet av ett lovfritt
komplementbostadshus inte ska anmälas (bara installationerna). Texten påstår därför inte att huset i sig kräver anmälan
i Botkyrka – den återger kommunens påminnelse om anmälan för installationer och att checklistan finns på anmälningssidan.
Strukna / ej använda: alla avgifter, taxor och handläggningstider (Vallentunas timtaxa och handläggningstimmar,
Lidingös elkostnad för LTA, Sigtunas tio veckor), Botkyrkas krav på kontrollansvarig (kommunens ord om certifiering –
utelämnat), Sigtunas riktlinje om bygglov i sammanhållen bebyggelse (skriven 2020, före lagändringen – utelämnad),
att Lidingöbanan skulle räknas som järnväg (ingen källa – utelämnat), vilka järnvägar som går genom Botkyrka och
Järfälla (ingen källa på sidorna – ingen ortsuppgift), om ett attefallshus på en LTA-fastighet kan anslutas (ingen
källa – skrivet som att vi frågar staden), Örbys och Sturebys stadsdelstillhörighet (inte nämnt i Älvsjö-texten).
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert. Rotavdrag: Skatteverket – nytt hus eller liknande
fristående byggnad och bygglovshandlingar/arkitekt ger inget avdrag.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no text, no letters"
_REG = _L.format("attefallshus-regler.html", "reglerna för attefallshus")

_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 9 kap. 4–5, 16 och 34–37 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")

_LID_VAD = ("Lidingö stad – Vad vill du göra?", "https://lidingo.se/bygga-bo/bygglov/vad-vill-du-gora/")
_LID_LAG = ("Lidingö stad – Ändrade lagar och regler för byggande", "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/")
_LID_VA = ("Lidingö stad – Spillvatten och avlopp", "https://lidingo.se/bygga-bo/mitt-boende/vatten-och-avlopp/spillvatten-avlopp/")
_LID_KMP = ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet",
            "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/")

_VB = "https://vallentuna.se/bygga-bo-och-miljo/"
_VAL_KB = ("Vallentuna kommun – Nybyggnad av komplementbyggnad", _VB + "bygglov-och-anmalan/behover-jag-bygglov/nybyggnad-av-komplementbyggnad")
_VAL_VA = ("Vallentuna kommun – Anslut kommunalt VA", _VB + "vatten-och-avlopp/anslut-kommunalt-va")
_VAL_AVL = ("Vallentuna kommun – Enskilt avlopp", _VB + "vatten-och-avlopp/enskilt-avlopp")
_VAL_BR = ("Vallentuna kommun – Egen brunn", _VB + "vatten-och-avlopp/egen-brunn")
_ROS = ("Roslagsvatten – Regler för komplementbyggnad med inkoppling till kommunalt VA",
        "https://roslagsvatten.se/anslutning-regler-f%C3%B6r-komplementbostad")

_JAR_BEF = ("Järfälla kommun – Bygglovsbefriade åtgärder",
            "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/bygglovsbefriadeatgarder.4.a41712119a05132defe8bb3.html")
_JAR_VA = ("Järfälla kommun – Ansvarsgränser mellan ledningar",
           "https://www.jarfalla.se/byggaboochmiljo/vavattenochavlopp/ansvarsgransermellanledningar.4.503309051349ea61989800014995.html")

_BB = "https://botkyrka.se/boende-och-narmiljo/"
_BOT_KBH = ("Botkyrka kommun – Komplementbostadshus (bygglov A–Ö)", _BB + "bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/komplementbostadshus")
_BOT_ANM = ("Botkyrka kommun – Komplementbostadshus (förändringar som kräver anmälan)",
            _BB + "bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-eller-anmalan/forandringar-som-kraver-anmalan/komplementbostadshus")
_BOT_VA = ("Botkyrka kommun – Anslutning av ett attefallshus (komplementbyggnad)",
           _BB + "vatten-och-avlopp/anslut-till-vatten-och-avlopp/anslutning-av-ett-attefallshus-komplementbyggnad")

_STH_KBH = ("Stockholms stad – Komplementbostadshus (bygglovsbefriad)",
            "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/komplementbostadshus-bygglovsbefriad/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_SVOA = ("Stockholm Vatten och Avfall – Koppla in vatten och avlopp till nybyggd villa eller attefallshus",
         "https://www.svoa.se/villa-och-radhus/vatten-och-avlopp/bygga-om/")

_SIG_KBH = ("Sigtuna kommun – Komplementbostadshus",
            "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/bygga-nytt/komplementbostadshus.html")
_SIG_FLYG = ("Sigtuna kommun – Flygbuller", "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/flygbuller.html")
_SIG_KULT = ("Sigtuna kommun – Bygga i kulturmiljö", "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html")
_SIG_OH = ("Sigtuna kommun – Riktlinjer för bebyggelseutveckling i dalgången mellan Odensala och Hova (pdf)",
           "https://www.sigtuna.se/download/18.2b81151517d4919beb8c692e/1638798200988/Riktlinjer%20f%C3%B6r%20bebyggelseutveckling%20i%20dalg%C3%A5ngen%20mellan%20Odensala%20och%20Hova.pdf")

_ROT_NEW = ("Skatteverket räknar upp arbeten som inte ger rotavdrag på ett småhus, bland annat att bygga ett helt nytt hus, "
            "en friggebod, ett garage eller en liknande fristående byggnad, och att skriva bygglovshandlingar eller anlita en "
            "arkitekt. Ett komplementbostadshus är en ny fristående byggnad, så kostnadsförslaget räknas utan avdrag.")

PAGES_TJ = {

# ------------------------------------------------------------------ LIDINGÖ
"attefallshus-lidingo.html": {
  "kind": "district", "service": "attefallshus", "ort": "Lidingö", "svc_label": "Attefallshus",
  "title": "Attefallshus på Lidingö – potten, avloppet och kartan",
  "description": "Attefallshus på Lidingö: den gemensamma potten med gamla friggebodar, anmälan för vatten, avlopp och imkanal, LTA-pumpen och stadens kulturmiljöer.",
  "h1": "Attefallshus på Lidingö",
  "lead": "Ett gästhus i trädgården, en bostad åt en vuxen son eller dotter eller ett hus att hyra ut – på Lidingö börjar frågan ofta med vad som redan står på tomten och hur avloppet går. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och går igenom tomten med dig innan något ritas.",
  "card": "Potten, avloppet och kulturmiljöerna.",
  "sections": [
    {"id": "potten-lidingo", "anchor": "Potten",
     "h2": "Det som redan står på tomten räknas in",
     "paras": [
       "Lidingö stad beskriver en gemensam ”pott” för lovfria komplementbyggnader och komplementbostadshus på varje tomt: 45 kvadratmeter inom detaljplan och 65 kvadratmeter utanför. Tidigare uppförda attefallshus och friggebodar räknas in i potten. Ett nytt hus får dessutom vara högst 30 kvadratmeter och fyra meter i nock inom detaljplan, och det ska vara mindre än det hus det kompletterar. Ett komplementbostadshus får bara byggas till ett en- eller tvåbostadshus.",
       "På många tomter står redan ett förråd, en gäststuga eller ett garage. Vi mäter deras byggnadsarea vid platsbesöket och räknar fram hur stort det nya huset kan bli utan bygglov. Står huset närmare gränsen än 4,5 meter behövs grannens skriftliga medgivande. Staden påpekar också att det är viktigt att ett lovfritt hus placeras rätt i förhållande till tomtgränserna och har rätt storlek och höjd.",
     ],
     "aside": {"title": "Räknas in i potten", "items": [
       "Tidigare attefallshus", "Friggebodar", "Garage och förråd utan lov", "Det nya huset"]}},
    {"id": "anmalan-lidingo", "h2": "Inget lov – men anmälan för installationerna",
     "paras": [
       "Själva uppförandet av ett lovfritt komplementbostadshus ska inte anmälas till byggnadsnämnden, skriver staden. Men ska huset få ventilation, vatten, avlopp, eldstad, rökkanal eller imkanal ska det anmälas innan installationen görs. I praktiken gäller det nästan varje hus som ska bli en riktig bostad med kök och badrum.",
       "Vi tar fram planritning, VA-ritning och förslag till kontrollplan till anmälan, och vi börjar inte med installationerna förrän startbeskedet har kommit. Vill du ha ett beslut på hela huset kan du i stället söka frivilligt bygglov. Staden beskriver det som ett sätt att vara säker på att det som byggs uppfyller lagens krav.",
     ],
     "aside": None},
    {"id": "avlopp-lidingo", "h2": "Avloppet: självfall, LTA-pump eller eget",
     "paras": [
       "På Lidingö finns enligt staden cirka 7 150 småhus. De allra flesta är anslutna till det kommunala nätet, och avloppsvattnet går till Käppalaverket. Cirka 50 fastigheter har fortfarande eget vatten och avlopp. Staden ansvarar för avloppsnätet fram till tomtgränsen. Innanför gränsen är ledningarna fastighetsägarens.",
       "Där marken ligger lågt eller ledningarna inte kan grävas tillräckligt djupt trycks avloppet fram av en LTA-pump. Staden sköter pumpen om det finns ett gällande avtal, ett larm med separat säkring, en isolerad lucka och minst 1,5 meter fri yta runt enheten. Ledningarna klarar bara spillvatten, och avfallskvarnar får inte anslutas. Har din fastighet en LTA-enhet frågar vi staden hur det nya huset ska kopplas in innan avloppet ritas.",
     ],
     "aside": {"title": "Vid LTA-pump", "items": [
       "Gällande avtal med staden", "Larm med separat säkring",
       "1,5 m fri yta runt enheten", "Bara spillvatten"]}},
    {"id": "kulturmiljo-lidingo", "h2": "Kulturmiljöerna och bygglovet",
     "paras": [
       "Ligger fastigheten inom ett kulturhistoriskt värdefullt område krävs bygglov för att uppföra, flytta eller utöka en komplementbyggnad eller ett komplementbostadshus. Lidingös kulturmiljöprogram från 2024 pekar ut områden, inte enskilda hus, och alla utpekade områden finns i stadens webbkarta. Programmet är ett kunskapsunderlag och påverkar inte byggrätten i detaljplanen.",
       "Staden har också äldre byggnadsinventeringar, från 1970- och 1980-talen och från 2013–2015, och via kundcenter kan du be att få ta del av beskrivningar som finns för din fastighet. De är bra att ha när huset ska ritas så att det passar till villan. Hur större ombyggnader och tillbyggnader prövas beskrivs under " + _L.format("tillbyggnad-lidingo.html", "tillbyggnad på Lidingö") + ", och byggprojekt i stort under " + _L.format("byggforetag-lidingo.html", "byggföretag på Lidingö") + ". Måtten och paragraferna finns i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus på Lidingö",
  "steps": [
    ("Platsbesök", "Vi mäter befintliga byggnader och räknar ut vad som är kvar i potten."),
    ("Kartan", "Detaljplan, kulturmiljö och avståndet till gränserna kontrolleras."),
    ("Avloppet", "Vi tar reda på om fastigheten har självfall, LTA-pump eller eget avlopp."),
    ("Anmälan", "Ventilation, vatten, avlopp och imkanal anmäls innan installationerna görs."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset används först när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag gäller inte det nya huset",
  "rot": [_ROT_NEW],
  "price_h2": "Vad påverkar priset på ett attefallshus på Lidingö?",
  "price": [
    "Husets storlek och planlösning, kök och badrum, grund på berg eller i en sluttning, hur avloppet ska kopplas in och hur material kan köras fram på en kuperad tomt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Räknas vår gamla friggebod in när vi bygger attefallshus på Lidingö?",
     "Ja. Staden skriver att tidigare uppförda friggebodar och attefallshus ingår i potten på 45 kvadratmeter inom detaljplan och 65 kvadratmeter utanför."),
    ("Måste ett attefallshus med pentry anmälas på Lidingö?",
     "Installationerna ska anmälas. Staden kräver anmälan innan ventilation, vatten och avlopp, eldstad, rökkanal eller imkanal installeras."),
    ("Kan vi koppla ett nytt hus till vår LTA-pump på Lidingö?",
     "Det får staden svara på för den enskilda fastigheten. Ledningarna klarar bara spillvatten, och staden ställer villkor för att sköta pumpen. Vi frågar innan avloppet ritas."),
    ("Hur mycket fri yta ska finnas runt en LTA-enhet på Lidingö?",
     "Minst 1,5 meter. Staden tar inget ansvar för skador på föremål eller växtlighet inom den gränsen, och vägen fram ska vara halkfri och snöröjd vintertid."),
    ("Ändrar kulturmiljöprogrammet hur mycket vi får bygga på Lidingö?",
     "Nej, programmet påverkar inte byggrätten. Men inom ett kulturhistoriskt värdefullt område krävs bygglov även för ett hus som annars är lovfritt."),
  ],
  "sources": [_PBL, _LID_VAD, _LID_LAG, _LID_VA, _LID_KMP, _SKV],
  "cta": ("Funderar du på ett attefallshus på Lidingö?", "Boka ett gratis platsbesök, så räknar vi på potten och avloppet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet nybyggt trähus med vit panel och grått plåttak i en kuperad trädgård med tallar och berg i dagen",
     "small newly built Swedish timber guest house with white vertical board cladding, black window frames and a grey standing seam metal roof on a sloping garden with granite outcrops and pine trees, a larger older wooden villa partly visible uphill, sea glimpsed between trunks in the distance, late summer daylight" + _SFX),
    ("Grön lucka till en avloppspumpbrunn i en gräsmatta med fri yta runt omkring",
     "green round plastic lid of a small sewage pump well set flush in a lawn next to a gravel path of a Swedish villa garden, a clear open area around it, birch and pine trees behind, overcast daylight" + _SFX),
    ("Äldre rött förråd och ett nybyggt gästhus bredvid varandra på en villatomt",
     "an older small red wooden storage shed and a newly built light grey timber guest house of similar height standing side by side on a mossy lawn of a hilly Swedish villa plot, stone steps and pine trees around, soft afternoon light" + _SFX),
  ],
},

# ------------------------------------------------------------------ VALLENTUNA
"attefallshus-vallentuna.html": {
  "kind": "district", "service": "attefallshus", "ort": "Vallentuna", "svc_label": "Attefallshus",
  "title": "Attefallshus i Vallentuna – plan, avlopp och brunn",
  "description": "Attefallshus i Vallentuna: mått inom och utanför detaljplan, gäststuga eller bostad, anmälan till kommunen och Roslagsvatten, eget avlopp och brunn.",
  "h1": "Attefallshus i Vallentuna",
  "lead": "I Vallentuna kan tomten ligga i en villagata i tätorten eller på landet med egen brunn och eget avlopp. Det avgör både hur stort huset får bli och hur vattnet ska lösas. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och reder ut båda frågorna innan ritningarna görs.",
  "card": "Inom eller utanför plan, avlopp och brunn.",
  "sections": [
    {"id": "plan-vallentuna", "anchor": "Inom eller utanför plan",
     "h2": "Inom eller utanför detaljplan",
     "paras": [
       "Plan- och bygglagen ger olika mått beroende på var tomten ligger. Inom detaljplan får ett lovfritt komplementbostadshus vara högst 30,0 kvadratmeter och 4,0 meter till nocken, och alla lovfria komplementbyggnader på tomten får tillsammans vara högst 45,0 kvadratmeter. Utanför detaljplan är gränserna 50,0 kvadratmeter, 4,5 meter och 65,0 kvadratmeter. I båda fallen ska huset ligga inom tomten och vara mindre än huset det kompletterar.",
       "Vallentuna kommun skriver att bygglov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område. Kommunen påminner också om att lovfriheten inte tar bort kravet på anmälan och startbesked när vatten och avlopp installeras i byggnaden eller inom tomten, eller när huset får ventilation.",
     ],
     "aside": {"title": "Lagens mått", "items": [
       "Inom plan: 30 m², 4,0 m, pott 45 m²", "Utanför plan: 50 m², 4,5 m, pott 65 m²",
       "Mindre än huvudbyggnaden", "Inom tomten"]}},
    {"id": "gaststuga-vallentuna", "h2": "Gäststuga eller egen bostad",
     "paras": [
       "Kommunen räknar gäststugan som en komplementbyggnad, liksom garage, förråd, vedbod och bastu. En lovfri komplementbyggnad kan inte användas som självständig bostad, skriver kommunen, eftersom den då inte längre är bara ett komplement till bostadshuset. Ska någon bo i huset är det ett komplementbostadshus, och då ska det uppfylla de tekniska kraven för en bostad.",
       "Skillnaden märks i allt från planlösning till isolering och installationer. Därför bestämmer vi användningen tillsammans med dig först. Kommunens krav på handlingar är tydliga: ritningar i skala 1:100, situationsplan i 1:500 med norrpil, mått i millimeter, kulörer med NCS-koder och en planritning som är möblerad så att tillgängligheten kan granskas.",
     ],
     "aside": None},
    {"id": "va-vallentuna", "h2": "Kommunalt VA via Roslagsvatten",
     "paras": [
       "Roslagsvatten AB ansvarar för vatten och avlopp i Vallentuna. Innan nytt VA installeras ska en anmälan göras till kommunens bygglovsenhet, och startbeskedet gäller även grävarbetet för ledningarna. Anmälan ska ha en VA-situationsplan där ledningar och brunnar ritas från förbindelsepunkten fram till byggnaden, och en kontrollplan. Efter startbeskedet anmäls arbetet till Roslagsvatten, som synar installationen, medger anslutning och sätter upp vattenmätare. Därefter söks slutbesked.",
       "Enligt Roslagsvatten ska vattenledningen till ett komplementhus kopplas efter vattenmätaren i det befintliga huset och spillvattnet på befintlig spillvattenledning inom tomten, gärna via en rensbrunn. Dag- och dräneringsvatten får inte kopplas till spillvattnet. Har huset kök eller pentry och toalett räknas det som en egen bostad i VA-taxan.",
     ],
     "aside": {"title": "Ordningen för VA", "items": [
       "Anmälan till kommunen", "Startbesked, även för grävningen",
       "Anmälan till Roslagsvatten", "Syn och vattenmätare", "Slutbesked"]}},
    {"id": "eget-vallentuna", "h2": "Eget avlopp och egen brunn",
     "paras": [
       "I Vallentuna finns ungefär 2 800 enskilda avloppsanläggningar. Den som anlägger en ny eller ändrar en befintlig anläggning ska först söka tillstånd eller göra en anmälan till Bygg- och miljötillsynsnämnden, annars kan det bli en miljösanktionsavgift. Situationsplanen ska visa vilka hus som kopplas på, varje del av anläggningen, platsen för slamtömningsbilen, egen och grannarnas dricksvattentäkt med avstånd i meter och eventuella borrhål för bergvärme. För en infiltration krävs också en jordprovsanalys.",
       "För en egen brunn till husbehov behövs i de flesta fall inget tillstånd. Kommunen hänvisar till SGU:s Normbrunn 16 och till Livsmedelsverkets råd att ta prov minst vart tredje år, och minst en gång per år om fler än två fastigheter delar brunn. Innan en ny brunn borras ska du ta reda på var grannarnas avlopp finns och berätta det för brunnsborraren. Om villan och tomten beskrivs under " + _L.format("takrenovering-vallentuna.html", "takrenovering i Vallentuna") + " och " + _L.format("byggforetag-vallentuna.html", "byggföretag i Vallentuna") + ". Lagens mått finns samlade i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Vallentuna",
  "steps": [
    ("Platsbesök", "Detaljplan, befintliga byggnader och hur vatten och avlopp löses i dag."),
    ("Användning", "Gäststuga eller bostad – det styr kraven på huset."),
    ("Ritningar", "Plan med möblering, fasader, situationsplan och VA-ritning."),
    ("Anmälan", "VA och ventilation anmäls och vi väntar på startbesked."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Efter Roslagsvattens syn eller avloppsbeslutet söks slutbesked."),
  ],
  "rot_h2": "Rotavdrag gäller inte det nya huset",
  "rot": [_ROT_NEW],
  "price_h2": "Vad påverkar priset på ett attefallshus i Vallentuna?",
  "price": [
    "Husets storlek och planlösning, kök och badrum, grunden, avståndet till förbindelsepunkten eller om ett eget avlopp behöver byggas eller utökas. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga ett större attefallshus på landet i Vallentuna?",
     "Utanför detaljplan får ett lovfritt komplementbostadshus vara högst 50,0 kvadratmeter och 4,5 meter i nock, med en pott på 65,0 kvadratmeter. Inom plan gäller 30,0, 4,0 och 45,0."),
    ("Kan vår gäststuga i Vallentuna hyras ut som bostad?",
     "Inte som lovfri komplementbyggnad. Kommunen skriver att en sådan byggnad inte kan användas som självständig bostad. Ett komplementbostadshus ska byggas för att vara en bostad."),
    ("Behöver grävningen för vattenledningen startbesked i Vallentuna?",
     "Ja. Kommunen skriver att startbeskedet för VA-installationen även gäller de grävarbeten som behövs."),
    ("Vad ska situationsplanen för ett nytt enskilt avlopp i Vallentuna visa?",
     "Bland annat husen som kopplas på, anläggningens delar, platsen för slamtömningsbilen, brunnar med avstånd i meter, borrhål för bergvärme och avståndet till fastighetsgränsen."),
  ],
  "sources": [_PBL, _VAL_KB, _VAL_VA, _ROS, _VAL_AVL, _VAL_BR, _SKV],
  "cta": ("Funderar du på ett attefallshus i Vallentuna?", "Boka ett gratis platsbesök, så går vi igenom tomten, vattnet och avloppet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet rödmålat trähus med vita knutar och svart plåttak på en gårdstomt intill en åker",
     "small newly built Swedish timber guest house painted falu red with white corner boards and a black metal roof on a farm plot next to an open field, an older red farmhouse partly visible, a few birches, Roslagen countryside, early autumn daylight" + _SFX),
    ("Grävt dike med vattenrör och avloppsrör mellan ett bostadshus och ett nytt litet hus",
     "open shallow trench across a lawn between a Swedish villa and a small new guest house, blue water pipe and orange sewer pipe laid on sand bedding, an inspection chamber at one end, wooden stakes, overcast daylight" + _SFX),
    ("Brunnslock av betong och en markbädd med luftningsrör på en lantlig tomt",
     "concrete well cover with a metal lid on a rural Swedish plot and, further away, a grassed septic soil bed with two white ventilation pipes sticking up, a red outbuilding and forest edge behind, soft light" + _SFX),
  ],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"attefallshus-jarfalla.html": {
  "kind": "district", "service": "attefallshus", "ort": "Järfälla", "svc_label": "Attefallshus",
  "title": "Attefallshus i Järfälla – när förrådet blir en bostad",
  "description": "Attefallshus i Järfälla: göra om ett förråd till bostad utan lov, 4,5 meter till gränsen, skyddsbestämmelser i planen och vem som äger VA-ledningarna.",
  "h1": "Attefallshus i Järfälla",
  "lead": "Många tomter har redan ett garage, en ateljé eller ett stort förråd som skulle kunna bli en bostad. I Järfälla, liksom i resten av landet, går det sedan december 2025 att göra om en sådan byggnad till ett komplementbostadshus utan bygglov – om vissa villkor är uppfyllda. Geal Entreprenad AB bygger nytt och bygger om, och börjar med att mäta det som redan står där.",
  "card": "Förråd, garage och ateljé som blir bostad.",
  "sections": [
    {"id": "andrad-anvandning-jarfalla", "anchor": "Förrådet blir bostad",
     "h2": "Ändrad användning utan bygglov",
     "paras": [
       "Plan- och bygglagen kräver normalt bygglov när en byggnad tas i anspråk för ett väsentligen annat ändamål. Men enligt 9 kap. 16 § krävs inget bygglov för att ändra en komplementbyggnad till ett komplementbostadshus, om det färdiga huset uppfyller måtten för ett lovfritt komplementbostadshus. Järfälla kommun har med åtgärden i sin lista över vad som kan vara bygglovsbefriat.",
       "Måtten är desamma som för ett nytt hus: inom detaljplan högst 30,0 kvadratmeter byggnadsarea och 4,0 meter till nocken, mindre än villan och inom en gemensam pott på 45,0 kvadratmeter för tomtens lovfria komplementbyggnader. Ett garage på 35 kvadratmeter kan alltså inte bli en lovfri bostad som det står. Vid platsbesöket mäter vi byggnaden utvändigt och går igenom stommen, grunden och taket, eftersom en bostad ska klara krav som ett förråd inte behöver uppfylla.",
     ],
     "aside": {"title": "Villkoren inom detaljplan", "items": [
       "Högst 30,0 m² byggnadsarea", "Högst 4,0 m till nocken",
       "Mindre än villan", "Pott 45,0 m² för hela tomten"]}},
    {"id": "grans-jarfalla", "h2": "Står förrådet nära gränsen?",
     "paras": [
       "Gamla förråd och garage står ofta nära tomtgränsen. Det spelar roll när användningen ändras. Enligt 9 kap. 34 § krävs bygglov närmare gränsen än 4,5 meter, eller inom 30,0 meter från ett järnvägsspårs mitt, även för en sådan ändring som avses i 16 §. Bygglovet behövs inte om de berörda grannarna skriftligen har medgett åtgärden.",
       "Järfälla kommun skriver att grannemedgivanden måste vara skriftliga och påminner om att närhet till gräns, järnväg, totalförsvar eller kulturmiljö kan kräva bygglov även för annars lovfria åtgärder. Vi ritar in avstånden på en situationsplan som grannen kan skriva under, och den sparar du tillsammans med husets övriga papper.",
     ],
     "aside": None},
    {"id": "plan-jarfalla", "h2": "Planens skyddsbestämmelser och små avvikelser",
     "paras": [
       "Kommunen lyfter två saker som är lätta att missa. Lovfria åtgärder får inte strida mot skyddsbestämmelser i detaljplanen som gäller markförorening, olyckor, översvämning eller erosion. Och åtgärder som inte är undantagna från att följa planen får göras med en avvikelse bara om den är liten och inte motverkar planens syfte.",
       "Kommunen skriver också att du som fastighetsägare själv ansvarar för att följa lagstiftningen och alla förutsättningar för din fastighet, och att anmälan och startbesked kan krävas om åtgärden innebär väsentliga ändringar av brandskydd, bärande konstruktion, vatten, avlopp eller ventilation. För en ombyggnad till bostad gäller det ofta flera av dem. Vill du ha ett beslut i förväg kan du söka frivilligt lov, vilket kommunen beskriver som en trygghet inför en större investering.",
     ],
     "aside": {"title": "Anmälan kan krävas för", "items": [
       "Brandskydd", "Bärande konstruktion", "Vatten och avlopp", "Ventilation"]}},
    {"id": "va-jarfalla", "h2": "Vem äger ledningarna på tomten?",
     "paras": [
       "Kommunen äger normalt VA-ledningarna i allmän mark fram till förbindelsepunkten, som brukar ligga vid eller strax utanför fastighetsgränsen. Därefter ansvarar fastighetsägaren för ledningarna, för läckor och stopp och för att vattenmätarplatsen uppfyller kommunens krav. I vissa områden ägs ledningarna efter förbindelsepunkten av en samfällighet, och ibland går en grannes ledningar över tomten med ett servitut.",
       "Innan vi drar nya ledningar till det blivande komplementbostadshuset tar vi reda på vilket av fallen som gäller. Det avgör var ledningarna kan anslutas och vem som behöver tillfrågas. Om villornas tak i kommunen kan du läsa under " + _L.format("takbyte-jarfalla.html", "takbyte i Järfälla") + ", och om större byggprojekt under " + _L.format("byggforetag-jarfalla.html", "byggföretag i Järfälla") + ". Lagens mått finns i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så gör vi om ett förråd till bostad i Järfälla",
  "steps": [
    ("Mätning", "Byggnadsarea, nockhöjd, avstånd till gräns och övriga byggnader på tomten."),
    ("Skick", "Grund, stomme och tak bedöms mot kraven för en bostad."),
    ("Planen", "Skyddsbestämmelser och eventuella avvikelser i detaljplanen kontrolleras."),
    ("Anmälan", "Brandskydd, bärande delar, VA och ventilation anmäls vid behov."),
    ("Ombyggnad", "Isolering, installationer, kök och badrum fram till nyckelfärdigt."),
    ("Slutbesked", "Bostaden används när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag för ombyggnad och nytt hus",
  "rot": [
    "Skatteverket ger inget rotavdrag för att bygga ett helt nytt hus, en friggebod, ett garage eller en liknande fristående byggnad, och inte för bygglovshandlingar eller arkitekt. Samtidigt skriver Skatteverket att komplementhus som garage och förråd kan höra till småhuset, och för att bygga om ska bostaden vara äldre än fem år och större delen av den ursprungliga stommen behållas.",
    "Vilka delar av just din ombyggnad som kan ge avdrag reder vi ut innan kostnadsförslaget skrivs. Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år.",
  ],
  "price_h2": "Vad påverkar priset i Järfälla?",
  "price": [
    "Om den befintliga byggnaden kan behållas eller behöver nya delar, isolering och fönster, kök och badrum, avståndet till ledningarna och om brandskyddet mot villan behöver förstärkas. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för att göra om vårt förråd i Järfälla till bostad?",
     "Inte om det färdiga huset håller måtten för ett lovfritt komplementbostadshus och inget annat gör att lov krävs, till exempel kulturvärden eller avståndet till gränsen."),
    ("Vårt garage står två meter från grannens tomt – kan det bli bostad utan lov?",
     "Bara om grannen skriftligen medger det. Närmare gränsen än 4,5 meter krävs annars bygglov även för den ändrade användningen."),
    ("Vem lagar en läcka på ledningen till attefallshuset i Järfälla?",
     "Efter förbindelsepunkten är ledningarna fastighetsägarens, eller samfällighetens i vissa områden. Kommunen ansvarar fram till förbindelsepunkten."),
    ("Vad menar Järfälla kommun med en liten avvikelse?",
     "Att en lovfri åtgärd som ska följa planen ändå får avvika något, om avvikelsen är liten och inte motverkar planens syfte eller bestämmelser."),
  ],
  "sources": [_PBL, _JAR_BEF, _JAR_VA, _SKV],
  "cta": ("Vill du göra om förrådet till en bostad i Järfälla?", "Boka ett gratis platsbesök, så mäter vi byggnaden och går igenom villkoren innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Fristående garage med träpanel som byggs om till bostad, med nya fönster och dörr",
     "detached Swedish wooden garage with grey painted vertical board cladding being converted into a small dwelling, the old garage door opening replaced by a new glazed door and two new windows, scaffolding on one side, villa garden with lawn and apple tree, overcast daylight" + _SFX),
    ("Mätband och tumstock vid hörnet av ett förråd nära en häck mot grannen",
     "a yellow folding ruler and a measuring tape laid out on the grass from the corner of a small wooden outbuilding towards a trimmed hedge marking the neighbour boundary on a Swedish villa plot, close view, soft daylight" + _SFX),
    ("Öppen schakt med avloppsrör fram till en rensbrunn vid ett litet hus",
     "open trench in a villa garden with an orange sewer pipe leading to a new plastic inspection chamber next to a small converted wooden outbuilding, gravel and sand heaps beside, Swedish suburban garden, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ BOTKYRKA
"attefallshus-botkyrka.html": {
  "kind": "district", "service": "attefallshus", "ort": "Botkyrka", "svc_label": "Attefallshus",
  "title": "Attefallshus i Botkyrka – webbkartan och anmälan",
  "description": "Attefallshus i Botkyrka: kartlagren som visar utökad lovplikt, kommunens checklista med ritningar och grannens påskrift och VA-enhetens servisanmälan.",
  "h1": "Attefallshus i Botkyrka",
  "lead": "Botkyrka kommun har en konkret vägledning för den som vill bygga ett komplementbostadshus: vilka lager i webbkartan du ska tända, vilka ritningar anmälan ska ha och hur vattnet ska dras. Geal Entreprenad AB bygger attefallshus nyckelfärdigt och följer den ordningen från första kartkollen till slutbeskedet.",
  "card": "Kartlagren, checklistan och vattnet.",
  "sections": [
    {"id": "kartan-botkyrka", "anchor": "Webbkartan",
     "h2": "Lagren i webbkartan som avgör lovplikten",
     "paras": [
       "Ett komplementbostadshus är enligt kommunen en fristående byggnad som kompletterar ett en- eller tvåbostadshus och är inredd med en självständig bostad. Det kan användas som fritidshus eller permanentbostad. Lovfritt blir det bara om måtten håller och ingen utökad lovplikt gäller. För att se det hänvisar kommunen till webbkartan: under den blå fliken Bibliotek och kultur finns lagret Kulturmiljöprogram, under Bygga och bo lagret Detaljplaner och under Riksintressen lagren Kulturmiljövård, Totalförsvaret och MSB, Försvarsmaktens civila del.",
       "Kommunen skriver också att översiktsplanen kan visa vilka områden och byggnader som är särskilt värdefulla, att detaljplanen ska granskas för skyddsbestämmelser och att det bör kontrolleras om området har ett gestaltningsprogram. Vi går igenom alla lagren för din fastighet vid platsbesöket och skriver ner vad vi har sett, så att du har det samlat inför valet av plats och storlek på huset.",
     ],
     "aside": {"title": "Tänd lagren", "items": [
       "Kulturmiljöprogram", "Detaljplaner", "Riksintressen: Kulturmiljövård",
       "Riksintressen: Totalförsvaret", "Riksintressen: MSB"]}},
    {"id": "utokad-botkyrka", "h2": "När ett litet hus ändå kräver lov",
     "paras": [
       "För ett lovfritt komplementbostadshus räknar kommunen upp när den utökade lovplikten slår till: inom 30 meter från ett järnvägsspårs mitt utan medgivande från huvudmannen eller infrastrukturförvaltaren, närmare en gräns än 4,5 meter utan grannarnas medgivande, inom eller i anslutning till totalförsvarets flygplatser, övningsfält eller skjutfält och vid eller inom särskilt värdefulla byggnader, tomter och bebyggelseområden.",
       "Andra lagar kan också gälla. Kommunen nämner strandskyddsdispens inom strandskyddat område och särskilt tillstånd för åtgärder nära allmän väg utanför detaljplanelagt område. Även ett lovfritt hus ska uppfylla kraven i plan- och bygglagen, plan- och byggförordningen och Boverkets föreskrifter, påpekar kommunen. Vill du ha ett formellt och bindande beslut kan du söka frivilligt bygglov och startbesked. Syftet kan vara att skapa trygghet och minska risken för att huset ifrågasätts senare, men prövningen kostar en bygglovsavgift.",
     ],
     "aside": None},
    {"id": "checklista-botkyrka", "h2": "Kommunens checklista för anmälan",
     "paras": [
       "Kommunen påminner om att det oftast krävs en anmälan för tekniska installationer som ventilation, eldstad, vatten eller avlopp, även om byggnaden i sig kan vara lovfri. På kommunens sida om anmälan av komplementbostadshus finns en checklista för handlingarna, och där beskrivs tekniskt samråd, startbesked innan bygget och slutbesked innan huset används. Ritningarna ska vara fackmannamässiga, skalenliga och högst i A3. Situationsplanen i skala 1:400 ska måttsätta huset med minst två avstånd i rät vinkel till tomtgränser och visa alla byggnader på tomten. Ligger huset närmare grannens gräns än 4,5 meter ska grannen skriva under på situationsplanen, och alla delägare till grannfastigheten måste godkänna.",
       "Fasadritningen i 1:100 ska visa alla fasader med nya och befintliga marknivåer, material och kulörer. Planritningen ska ha möblerat entréplan som är tillgängligt för personer med nedsatt rörelseförmåga, och sektionen ska visa våningshöjd, golvnivåer, takvinkel och marknivå vid entréerna. Till det kommer konstruktionsritning och kontrollplan. Kommunen skriver att utstakning och lägeskontroll kan krävas.",
     ],
     "aside": {"title": "Till anmälan", "items": [
       "Situationsplan 1:400", "Fasader, plan och sektion 1:100",
       "Konstruktionsritning", "Kontrollplan", "Grannens påskrift vid behov"]}},
    {"id": "vatten-botkyrka", "h2": "Servisanmälan till VA-enheten",
     "paras": [
       "Får huset kök, pentry eller toalett räknas det som en egen bostad ur VA-synpunkt, och då tillkommer en anslutningsavgift enligt VA-taxan. För att dra in vatten och avlopp skickar du en servisanmälan till kommunens VA-enhet. Vattenledningen ska dras efter den befintliga vattenmätaren i huset, och den nya spillvattenledningen kopplas på den befintliga inom tomten. Görs det inte så monterar VA-enheten en egen mätare i attefallshuset.",
       "Dag- och dräneringsvatten får inte kopplas till spillvattenledningen. Ska en befintlig komplementbyggnad byggas om eller få ändrad användning ska du kontakta VA-enheten. Om villornas tak och plåt i kommunen kan du läsa under " + _L.format("takrenovering-botkyrka.html", "takrenovering i Botkyrka") + " och " + _L.format("platslagare-botkyrka.html", "plåtslagare i Botkyrka") + ". Lagens mått finns i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Botkyrka",
  "steps": [
    ("Kartkoll", "Alla kartlager, detaljplan och eventuellt gestaltningsprogram för tomten."),
    ("Platsbesök", "Placering, avstånd i rät vinkel och befintliga byggnader mäts in."),
    ("Handlingar", "Situationsplan, fasader, plan, sektion, konstruktion och kontrollplan."),
    ("Anmälan", "Installationerna anmäls och vi väntar på startbesked innan de görs."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset används när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag gäller inte det nya huset",
  "rot": [_ROT_NEW],
  "price_h2": "Vad påverkar priset på ett attefallshus i Botkyrka?",
  "price": [
    "Husets storlek och planlösning, kök och badrum, grunden, ledningsdragningen fram till befintlig mätare och spillvattenledning och om utstakning behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka kartlager ska vi titta på innan vi bygger attefallshus i Botkyrka?",
     "Kommunen pekar ut Kulturmiljöprogram, Detaljplaner och under Riksintressen lagren Kulturmiljövård, Totalförsvaret och MSB."),
    ("Hur många av grannens ägare måste skriva under i Botkyrka?",
     "Alla delägare till fastigheten måste godkänna. Påskriften görs daterad med namnförtydligande direkt på situationsplanen."),
    ("Måste attefallshuset i Botkyrka ha egen vattenmätare?",
     "Inte om vattenledningen dras efter husets befintliga mätare. Annars monterar kommunens VA-enhet en mätare i attefallshuset."),
    ("Får dagvattnet från attefallshusets tak kopplas till avloppet i Botkyrka?",
     "Nej. Kommunen skriver att dag- och dräneringsvatten inte får kopplas till kommunens spillvattenledning."),
    ("Kan ett attefallshus i Botkyrka användas som fritidshus?",
     "Ja. Kommunen skriver att ett komplementbostadshus kan användas antingen som fritidshus eller som permanentbostad."),
    ("Vilka ritningar vill Botkyrka kommun se för ett attefallshus?",
     "Situationsplan i 1:400, fasad-, plan- och sektionsritningar i 1:100, konstruktionsritning och kontrollplan. Ritningarna får vara högst A3."),
  ],
  "sources": [_PBL, _BOT_KBH, _BOT_ANM, _BOT_VA, _SKV],
  "cta": ("Funderar du på ett attefallshus i Botkyrka?", "Boka ett gratis platsbesök, så går vi igenom kartan och handlingarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nybyggt litet hus med mörkgrå träpanel och pulpettak på en villatomt med gräsmatta",
     "newly built small Swedish timber dwelling with dark grey vertical board cladding, large windows and a low mono-pitch roof with black metal sheeting, standing on a lawn behind a 1970s brick villa, birch trees and a wooden fence, south Stockholm suburb, clear afternoon light" + _SFX),
    ("Utskriven situationsplan och tumstock på ett bord med en trädgård i bakgrunden",
     "printed architectural site plan drawing with dimension lines lying on an outdoor wooden garden table, a folding ruler and a pencil on top, blurred villa garden in the background, no readable text, daylight" + _SFX),
    ("Vattenmätare och rör i ett tekniskt utrymme i ett litet trähus",
     "small technical cupboard inside a new Swedish timber guest house with a water meter, shut-off valves and white PEX pipes neatly mounted on a plywood board, clean and bright interior light" + _SFX),
  ],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"attefallshus-alvsjo.html": {
  "kind": "district", "service": "attefallshus", "ort": "Älvsjö", "svc_label": "Attefallshus",
  "title": "Attefallshus i Älvsjö – villatomten, stadens regler och VA",
  "description": "Attefallshus i Älvsjö: villastadens tomter, stadens regler för komplementbostadshus på prickmark och nära gräns, grannens medgivande och vatten från SVOA.",
  "h1": "Attefallshus i Älvsjö",
  "lead": "Villastäderna i Älvsjö planerades för stora trädgårdar, och många tomter har sedan dess delats. Det gör att förutsättningarna för ett komplementbostadshus kan skilja sig mycket mellan två grannar. Geal Entreprenad AB bygger attefallshus nyckelfärdigt och börjar med detaljplanen, klassificeringskartan och tomtens mått.",
  "card": "Villatomten, prickmarken och vattnet.",
  "sections": [
    {"id": "tomten-alvsjo", "anchor": "Villatomten",
     "h2": "Villastadens tomter i Älvsjö",
     "paras": [
       "Stadens skrift Varsam utveckling av småhus- och villaområden beskriver villastäderna som fritt liggande hus i trädgårdslandskap på tomter om 1 500–3 000 kvadratmeter. I Älvsjö villastad togs stadsplanen fram av Per Olof Hallman. När nya planer gjordes för delar av villastäderna på 1930-talet blev tomterna mindre, 700–1 000 kvadratmeter, och genom successiv tomtdelning har hus kommit till på tomter kring 600 kvadratmeter.",
       "Skriften pekar ut villastadens gröna karaktär som det som håller ihop områdena. Bland de aspekter som har stor påverkan vid förändring nämns volym, proportioner och takform, även för komplementbyggnader. Den påminner också om att dagvatten ska tas om hand inom den egna fastigheten och att gröna ytor inte bör hårdgöras. Vi placerar därför huset så att träd och gräsytor sparas så långt det går.",
     ],
     "aside": {"title": "Tomterna enligt staden", "items": [
       "1 500–3 000 m² i de första planerna", "700–1 000 m² på 1930-talet",
       "Kring 600 m² efter tomtdelning"]}},
    {"id": "regler-alvsjo", "h2": "Stadens regler för ett lovfritt hus",
     "paras": [
       "Stockholms stad beskriver ett komplementbostadshus som en självständig bostad som ska stå fristående och vara ett komplement till ett en- eller tvåbostadshus som redan finns. Utan bygglov får det vara högst 30,0 kvadratmeter byggnadsarea och 4,0 meter i nock, mindre än villan och rymmas i en sammanlagd area på 45,0 kvadratmeter. Attefallshus och friggebodar som redan står på tomten räknas in. Ett lovfritt komplementbostadshus får strida mot detaljplanen och kan alltså placeras på prickmark.",
       "Ett befintligt komplementbostadshus kan byggas till utan lov så länge det efter tillbyggnaden inte blir större än 30,0 kvadratmeter eller högre än 4,0 meter. Bor du i en särskilt kulturhistoriskt värdefull byggnad eller ett sådant område gäller utökad lovplikt. Staden hänvisar till Stadsmuseets klassificeringskarta som en första indikation. Staden påminner också om att det du bygger inte får orsaka en betydande olägenhet för omgivningen och att varsamhetskrav och tekniska egenskapskrav gäller även utan lov. Detaljplanen för fastigheten hittar du i e-tjänsten Bygg- och plantjänsten.",
     ],
     "aside": None},
    {"id": "medgivande-alvsjo", "h2": "Medgivandet när huset står nära gränsen",
     "paras": [
       "Huset ska placeras 4,5 meter från gränsen mot granne, samfällighet eller allmän plats, och minst 30 meter från järnvägsspår om inte infrastrukturförvaltaren medger det. Vill du bygga närmare en granne behövs ett skriftligt medgivande som enligt staden ska innehålla fastighetsbeteckning, vilken typ av åtgärd det gäller, en situationsplan med åtgärden och avståndet till gränsen och underskrifter från berörda grannar.",
       "Mot gata och park är det oftast kommunen som är huvudman, och då skickar du förfrågan skriftligt till stadsbyggnadskontoret. Staden råder dig att kunna visa medgivandet för byggnadsnämnden om ett tillsynsärende uppstår. Vi ritar situationsplanen så att den kan användas direkt i medgivandet.",
     ],
     "aside": {"title": "Medgivandet ska ha", "items": [
       "Fastighetsbeteckning", "Typ av åtgärd",
       "Situationsplan med avstånd", "Grannarnas underskrifter"]}},
    {"id": "va-alvsjo", "h2": "Vatten och avlopp från villan",
     "paras": [
       "Ska huset få vatten och avlopp krävs en anmälan och startbesked innan installationen börjar, och detsamma gäller ventilation och eldstad. Stockholm Vatten och Avfall vill ha en servisanmälan i god tid före byggstart, med en ritning över ledningsdragningen. Utan ritningen kan ansökan inte behandlas. Vattenledningen kopplas efter vattenmätaren i det befintliga huset och spillvattnet på den befintliga spillvattenledningen inom tomten, gärna via en rensbrunn.",
       "Dag- och dräneringsvatten får inte kopplas till spillvattnet. Ligger det nya huset högre upp och längre från förbindelsepunkten kan vattentrycket bli sämre, skriver SVOA. Har huset kök eller pentry och toalett räknas det som en egen bostad och en bostadsenhetsavgift tillkommer. Om villornas tak och fasader i Älvsjö kan du läsa under " + _L.format("takrenovering-alvsjo.html", "takrenovering i Älvsjö") + " och " + _L.format("fasadrenovering-alvsjo.html", "fasadrenovering i Älvsjö") + ". Lagens mått finns i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Älvsjö",
  "steps": [
    ("Planen", "Detaljplan, prickmark och Stadsmuseets klassificering för tomten."),
    ("Platsbesök", "Befintliga byggnader, träd, marknivåer och avstånd till gränserna."),
    ("Medgivande", "Situationsplan till grannen eller stadsbyggnadskontoret vid behov."),
    ("Anmälan och servis", "Anmälan för VA och ventilation och servisanmälan till SVOA."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset används när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag gäller inte det nya huset",
  "rot": [_ROT_NEW],
  "price_h2": "Vad påverkar priset på ett attefallshus i Älvsjö?",
  "price": [
    "Husets storlek och planlösning, kök och badrum, grund i sluttning eller på berg, ledningarnas längd från villan och hur material kan bäras in på en tomt med träd och häckar. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får ett attefallshus i Älvsjö stå på prickmark?",
     "Ja. Stockholms stad skriver att ett komplementbostadshus som inte kräver lov får strida mot detaljplanen och därmed placeras på mark som inte får bebyggas."),
    ("Kan vi bygga till vårt befintliga attefallshus i Älvsjö?",
     "Ja, utan lov så länge huset efter tillbyggnaden högst är 30,0 kvadratmeter och 4,0 meter högt, mindre än villan och ryms i tomtens sammanlagda 45,0 kvadratmeter."),
    ("Vad ska grannens medgivande innehålla i Stockholm?",
     "Fastighetsbeteckning, typ av åtgärd, en situationsplan med åtgärden och avståndet till gränsen inritat och underskrifter från de berörda grannarna."),
    ("Gäller utökad lovplikt i Älvsjö även för en vanlig bod?",
     "Ja. Staden skriver att lovplikten i kulturhistoriskt värdefulla miljöer gäller alla typer av komplementbyggnader, även sådana som tidigare kallades friggebod."),
    ("Varför kan vattentrycket bli sämre i ett attefallshus?",
     "Enligt SVOA kan trycket försämras om den nya byggnaden ligger högre upp och längre från förbindelsepunkten vid tomtgränsen."),
  ],
  "sources": [_PBL, _STH_KBH, _VARSAM, _SVOA, _SKV],
  "cta": ("Funderar du på ett attefallshus i Älvsjö?", "Boka ett gratis platsbesök, så går vi igenom planen och tomten innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet trähus med ljusgul panel och sadeltak bakom en äldre villa i en lummig trädgård",
     "small newly built Swedish timber guest house with pale yellow horizontal board cladding, white trims and a pitched red clay tile roof at the back of a large leafy garden behind an early 1900s wooden villa, old fruit trees and a clipped hedge, Stockholm villa suburb, summer daylight" + _SFX),
    ("Snören och käppar som markerar ett litet hus mellan fruktträd på en gräsmatta",
     "wooden stakes and white string marking the rectangular footprint of a small house on a lawn between old apple trees in a Swedish villa garden, a wheelbarrow nearby, soft overcast light" + _SFX),
    ("Rensbrunn och nya rör i en grävd ränna mellan en villa och ett litet hus",
     "open trench across a garden lawn with a new grey plastic inspection chamber, a blue water pipe and an orange sewer pipe running from an older villa towards a small new timber house, Stockholm suburb garden, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SIGTUNA
"attefallshus-sigtuna.html": {
  "kind": "district", "service": "attefallshus", "ort": "Sigtuna", "svc_label": "Attefallshus",
  "title": "Attefallshus i Sigtuna – potten, flygbullret och ritningarna",
  "description": "Attefallshus i Sigtuna: kommunens exempel på potten, Arlanda och flygbullret när lov krävs, checklistan för ritningar och gårdshusen i Odensala–Hova.",
  "h1": "Attefallshus i Sigtuna",
  "lead": "Från villagatorna i Märsta och Rosersberg till gårdarna i dalgången mellan Odensala och Hova – i Sigtuna styr både Arlanda och kulturmiljöerna vad som kan byggas. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och tar reda på vad som gäller för din tomt innan huset ritas.",
  "card": "Potten, Arlanda och gårdshusen.",
  "sections": [
    {"id": "potten-sigtuna", "anchor": "Den gemensamma potten",
     "h2": "Kommunens räkneexempel på potten",
     "paras": [
       "Sigtuna kommun förklarar den gemensamma potten med två exempel. Inom detaljplan: står det redan en friggebod på 15 kvadratmeter och ett attefallshus på 30 kvadratmeter på tomten kan du inte bygga något mer utan bygglov. Utanför detaljplan: står det en friggebod på 15 kvadratmeter och ett garage på 50 kvadratmeter är potten också full. Gränserna är 45 kvadratmeter inom plan och 65 utanför.",
       "Därtill ska huset vara högst 30 kvadratmeter och 4 meter i nock inom detaljplan eller 50 kvadratmeter och 4,5 meter utanför, vara mindre än huset det kompletterar och stå inom tomten. Närmare tomtgränsen än 4,5 meter krävs grannens skriftliga medgivande. Kommunen påminner om att en anmälan behövs när vatten, avlopp eller ventilation installeras eller när brandskyddet påverkas, även när bygglov inte krävs.",
     ],
     "aside": {"title": "Potten är full när", "items": [
       "Inom plan: friggebod 15 + attefallshus 30", "Utanför plan: friggebod 15 + garage 50"]}},
    {"id": "arlanda-sigtuna", "h2": "Arlanda och flygbullret",
     "paras": [
       "Arlanda flygplats ligger i Sigtuna kommun och är ett riksintresse enligt miljöbalken, både för dagens verksamhet och för möjligheten att utöka den. Det område som påverkas av flygbullret kallas influensområdet. Om du vill bygga nytt eller göra en tillbyggnad där tar kommunen kontakt med Swedavia för ett utlåtande innan den fattar beslut om bygglov.",
       "När bygg- och miljönämnden yttrar sig på ansökningar om bygglov och förhandsbesked bedömer den bland annat bullersituationen, hur avloppet ska lösas och markens radonhalt enligt en markradonutredning. Kommunen skriver att närhet till en stor väg, järnväg eller flygbuller kan begränsa möjligheten att bygga, men att byggnation i vissa fall kan accepteras med bullerbegränsande åtgärder som avskärmning eller isolering. Behöver ditt hus bygglov tar vi med de frågorna från början.",
     ],
     "aside": None},
    {"id": "ritningar-sigtuna", "h2": "Ritningarna enligt kommunens checklista",
     "paras": [
       "Kommunen har en checklista i sex steg. Tomtkartan till situationsplanen laddar du ner gratis som pdf utan inloggning. Fasadritningen ska visa alla fasader med nya och befintliga marknivåer, material, kulörer och väderstreck. Planritningen ska ha möblerat entréplan som är tillgängligt för personer med nedsatt rörelseförmåga och vara måttsatt så att arean kan räknas ut. Sektionen visar våningshöjd, golvnivåer, takvinkel och marknivå vid entréer.",
       "Konstruktionsritningar ska redovisas för grund, stomme och takkonstruktion, med tekniska snitt genom bjälklag, väggar och yttertak. En teknisk beskrivning förklarar brandskydd, uppvärmning, ventilation, energi och säkerhet. Förslag till kontrollplan lämnas in både vid bygglov och anmälan. Vi tar fram hela underlaget, så att det är klart när ärendet skickas.",
     ],
     "aside": {"title": "Kommunen vill se", "items": [
       "Situationsplan på tomtkartan", "Fasader, plan och sektion",
       "Konstruktionsritningar", "Teknisk beskrivning", "Förslag till kontrollplan"]}},
    {"id": "odensala-sigtuna", "h2": "Gårdshus i dalgången mellan Odensala och Hova",
     "paras": [
       "Dalgången mellan Odensala och Hova har enligt kommunens riktlinjer spår av mänsklig aktivitet i mer än 1 500 år. Riktlinjerna, antagna i december 2020, använder ordet gårdshus som samlingsnamn för uthus, ekonomibyggnader och komplementbyggnader som hör till en gård, och beskriver bevarade rödmålade uthus, knuttimrade uthus från 1800-talets andra hälft och gårds- och uthus placerade vinkelrätt mot varandra.",
       "Kommunen skriver att du kan behöva bygglov för komplementbyggnader inom ett kulturhistoriskt värdefullt område och tar emot foton från samtliga väderstreck för att göra en bedömning av fastigheten. Dalgången är inte planlagd med detaljplan, utom Herresta by med planer från 2011 och 2013, och när marken inte är planlagd föregås bygglov vanligen av ett förhandsbesked. Ett nytt hus på en sådan gård ritar vi så att det inordnar sig bland de befintliga. Om villornas tak och fasader i kommunen kan du läsa under " + _L.format("takrenovering-sigtuna.html", "takrenovering i Sigtuna") + " och " + _L.format("byggforetag-sigtuna.html", "byggföretag i Sigtuna") + ". Lagens mått finns i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Sigtuna",
  "steps": [
    ("Platsbesök", "Befintliga byggnader mäts och potten räknas ut."),
    ("Förutsättningar", "Detaljplan, kulturmiljö och om tomten ligger i Arlandas influensområde."),
    ("Ritningar", "Situationsplan, fasader, plan, sektion och konstruktion enligt checklistan."),
    ("Anmälan", "VA, ventilation och brandskydd anmäls och vi väntar på startbesked."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset används när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag gäller inte det nya huset",
  "rot": [_ROT_NEW],
  "price_h2": "Vad påverkar priset på ett attefallshus i Sigtuna?",
  "price": [
    "Husets storlek och planlösning, kök och badrum, grunden, avloppslösningen och om huset behöver extra ljudisolering eller anpassning till en gårdsmiljö. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vi har en friggebod och ett attefallshus i Märsta – får vi bygga ett hus till?",
     "Inte utan bygglov om de tillsammans är 45 kvadratmeter inom detaljplan. Sigtuna kommun använder just friggebod 15 och attefallshus 30 som exempel på en full pott."),
    ("Vad innebär Arlandas influensområde för ett bygglov i Sigtuna?",
     "Vid ny- och tillbyggnad inom influensområdet tar kommunen kontakt med Swedavia för ett utlåtande innan beslut fattas om bygglov."),
    ("Hur får vi veta om vår gård i Sigtuna ligger i en värdefull kulturmiljö?",
     "Kommunen tar emot foton från samtliga väderstreck och en beskrivning av vad du vill göra, och återkommer med en bedömning."),
    ("Kostar tomtkartan till situationsplanen något i Sigtuna?",
     "Nej. Kommunen skriver att du kan söka på din adress och ladda ner tomtkartan som pdf utan inloggning och utan kostnad."),
    ("Vad ska konstruktionsritningarna för ett attefallshus i Sigtuna visa?",
     "Grund, stomme och takkonstruktion, med tekniska snitt som förklarar hur bjälklag, väggar och yttertak är uppbyggda."),
  ],
  "sources": [_PBL, _SIG_KBH, _SIG_FLYG, _SIG_KULT, _SIG_OH, _SKV],
  "cta": ("Funderar du på ett attefallshus i Sigtuna?", "Boka ett gratis platsbesök, så går vi igenom tomten och förutsättningarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet rödmålat gårdshus med vita knutar bredvid äldre uthus i ett öppet odlingslandskap",
     "small newly built falu red timber guest house with white corner boards and a red clay tile roof placed at a right angle to older red wooden outbuildings on a farm courtyard in an open Uppland agricultural valley, gravel yard, big old ash tree, early autumn light" + _SFX),
    ("Villagata med tvåvåningshus av tegel och trä under en klar himmel",
     "quiet Swedish suburban street with 1970s single-storey brick and wood villas with concrete tile roofs, small front lawns and young trees, wide clear sky above, Märsta Uppland, daylight" + _SFX),
    ("Rödmålade knuttimrade uthus på en gammal gårdstomt",
     "close view of old falu red log outbuildings with dovetailed corner joints and small doors on an old Swedish farmstead, grass and gravel in front, soft late afternoon light" + _SFX),
  ],
},
}
