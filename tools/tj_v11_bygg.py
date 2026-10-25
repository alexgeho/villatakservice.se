# -*- coding: utf-8 -*-
"""Byggföretag – ortsidor v11: Huddinge, Norrtälje, Nacka, Österåker, Botkyrka, Vallentuna (2026-10-25).
Orterna valda efter antal bostäder i småhus 2025 enligt SCB (BO0104T04): Huddinge 20 758, Norrtälje 19 171,
Nacka 16 435, Österåker 13 635, Botkyrka 12 582, Vallentuna 9 300.
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
  SCB (BO0104T04, 2025), Skatteverket (Så fungerar rotavdraget; Ger arbetet rätt till rotavdrag? – nytt hus och
  fristående byggnad, femårsregeln, tillbyggnad 75 procent, markarbeten för vatten och avlopp, sprängarbete),
  Huddinge kommun (Grannemedgivande; Bygglovets olika steg; Boka möte med bygglovsavdelningen; Lantmäterimyndigheten
  – Om lantmäterimyndigheten, Lantmäteriförrättningar och rättsliga uppdrag, Fastighetsgränser),
  Norrtälje kommun (Förhandsbesked; Efter bygglovsbeslutet: startbesked och slutbesked; Skillnad mellan
  bygglovspliktiga, anmälningspliktiga och bygglovsbefriade åtgärder; Enskilt vatten),
  Nacka kommun/Nacka vatten och avfall (Attefallshus och andra komplementbyggnader; Installera LTA; Byggvatten och
  länshållningsvatten; Dagvatten – vägledning för enskilda fastighetsägare),
  Österåkers kommun (Riva, rivningslov; Markarbeten; Gatukostnader),
  Botkyrka kommun (Sök bygglov för nybyggnad en- och tvåbostadshus; APD-plan; Bygga in- och utfart; Tillstånd för
  tunga, långa och breda fordon; Tillstånd för schakt och trafikanordning; Sprängning; Lägeskontroll),
  Vallentuna kommun (Det ska din ansökan eller anmälan innehålla; Marklov och rivningslov; Ditt ansvar som granne;
  Lediga tomter till småhus; Planbesked – ansökan; Landsbygd).
Strukna (ej verifierade, oklara i källan eller medvetet utelämnade): kommunala avgifter i kronor (Nackas
anläggningsavgift för komplementbyggnad, Vallentunas planbeskedsavgift i mPBB, Botkyrkas schaktavgifter),
vilket år Norrtäljes anmälnings-/tillståndsplikt för bergborrade brunnar "från och med 1 april" började gälla
(sidan anger inget år – texten säger bara att plikten finns i utvalda områden), Huddinges handläggningstider
utöver det kommunen själv skriver, om Huddinges sida om grannemedgivande redan är uppdaterad efter PBL 2025
(kommunen skriver att sidorna uppdateras – texten återger bara det som står och hänvisar till kommunens
besked), att kontrollansvarig krävs för varje nytt hus i Botkyrka utöver kommunens checklista, Botkyrkas
A–Ö-sidor som kommunen själv märker "kan vara inaktuell" används bara för sakuppgifter som inte berörs av
lagändringen (APD-plan, sprängning, lägeskontroll), vilka områden i Nacka som har LTA, vilka områden i
Österåker som är förnyelseområden utöver Valsättra del 2, gatukostnader i Nacka (endast äldre handlingar
hittade), Vallentunas tomtpriser och vilka tomter mäklaren har till salu. Inga priser, garantier, omdömen,
egna uppdrag eller cert.
Kritikpass 2026-10-25: alla siffror och regler kontrollerade mot källtexterna igen; "certifierad" kontrollansvarig
(Botkyrka, Österåker) skrivs inte ut, ordet attefallshus används bara där kommunens egen sida använder det,
Norrtäljes 1 april-datum struket, Huddinges uppgift om avgiftsreduktion återges som kommunens egen formulering.
Därtill strukna i kritikpasset (inte belagda i någon öppnad källa): att Huddinge har flest småhus i länet, att
mycket av Norrtäljes mark ligger utanför detaljplan, att Nackas tomter ofta är kuperade, att äldre sommarhus
ofta ersätts i Österåker, ortnamnen Tullinge/Tumba i Botkyrkas ingress, att anmälan "ofta" är vägen vid
ombyggnad i Norrtälje. Bildalt-texter justerade efter genererade bilder (nacka-1 och osteraker-2 omgjorda:
person i bild respektive förvridna containrar).
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py."""

_L = '<a class="text-link" href="{0}">{1}</a>'

# ------------------------------------------------------------------ gemensamma källor
_SCB = ("SCB – Antal lägenheter efter region, hustyp och upplåtelseform (BO0104), 2025",
        "https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BO__BO0104__BO0104D/BO0104T04/")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV_JOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_HU = "https://www.huddinge.se/bostad-och-miljo/"
_NT = "https://www.norrtalje.se/info/bygga-bo-miljo/"
_NA = "https://www.nacka.se/nackavattenavfall/vatten-och-avlopp/anslut-till-kommunalt-va/"
_OS = "https://www.osteraker.se/byggabomiljo/"
_BO = "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/"
_VA = "https://www.vallentuna.se/bygga-bo-och-miljo/"

PAGES_TJ = {

# ------------------------------------------------------------------ HUDDINGE
"byggforetag-huddinge.html": {
  "kind": "district", "service": "byggforetag", "ort": "Huddinge", "svc_label": "Byggföretag",
  "title": "Byggföretag i Huddinge – grannar, tomtgräns och lovärendet",
  "description": "Byggföretag i Huddinge: när grannarna hörs i ett bygglov, medgivande nära tomtgränsen, gränsmarkeringar hos lantmäterimyndigheten och tidsplanen.",
  "h1": "Byggföretag i Huddinge",
  "lead": "Huddinge har 20 758 bostäder i småhus enligt SCB:s statistik för 2025. Bygger man till eller bygger nytt på en villatomt hamnar man ofta nära någon av grannarna. Geal Entreprenad AB tar hand om tillbyggnader, nya hus på tomten och större ombyggnader som total entreprenad, och en stor del av förarbetet gäller just grannarna, gränsen och ordningen i kommunens handläggning.",
  "card": "Grannar, tomtgräns och lovärendet.",
  "sections": [
    {"id": "sakagare-huddinge", "anchor": "Grannarna i ärendet",
     "h2": "När grannarna får säga sitt om bygget",
     "paras": [
       "Plan- och bygglagen ger inte grannar en generell rätt att tycka till om allt som byggs, skriver Huddinge kommun. Bygglovsavdelningen skickar ändå ut ett grannehörande i vissa fall: vid förhandsbesked, vid nya hus och större tillbyggnader utanför detaljplanerat område, när ansökan inte följer detaljplanen och när någon vill bygga närmare tomtgränsen än 4,5 meter och detaljplanen saknar bestämmelser om avstånd.",
       "Sakägare är bland andra ägare till fastigheter som gränsar till tomten, innehavare av tomträtt, arrende eller servitut och myndigheter med ett särskilt intresse. Rågrannarna är enligt kommunen sakägare i varje ärende som skickas på hörande. De har oftast två veckor på sig att svara via e-tjänsten. Är det svårt att avgöra vilka som berörs kan kommunen i stället kungöra ärendet i tidningen Mitt i Huddinge och på den digitala anslagstavlan.",
       "Kommer en negativ synpunkt in skickas den till dig som söker, så att du kan bemöta den. Du kan då välja att ändra ritningarna eller gå vidare med förslaget som det är. Följer ansökan detaljplanen helt fattas beslutet utan att sakägarna hörs.",
     ],
     "aside": {"title": "Grannehörande i Huddinge", "items": [
       "Förhandsbesked och bygge utanför plan",
       "Avvikelse från detaljplanen",
       "Närmare än 4,5 meter utan planbestämmelse",
       "Oftast två veckors svarstid"]}},
    {"id": "medgivande-huddinge", "h2": "Medgivande nära tomtgränsen – och mot kommunens mark",
     "paras": [
       "För en del lovfria åtgärder är det grannens godkännande som avgör placeringen. Huddinge kommun nämner friggebod, lovbefriat skärmtak och mur eller plank på högst 1,8 meter inom 3,6 meter från bostadshuset för en skyddad uteplats. Hamnar de närmare tomtgränsen än 4,5 meter ska alla ägare till den berörda grannfastigheten godkänna placeringen innan bygget börjar, och godkännandet gäller även om grannen sedan flyttar. Kommunen rekommenderar ett skriftligt medgivande men vill inte ha det inskickat.",
       "För åtgärder som ska anmälas, som kommunen exemplifierar med attefallshus och attefallstillbyggnad, ska medgivandet vara skriftligt och göras på en situationsplan där det nya är inritat på rätt plats och med rätt mått.",
       "Gränsar tomten mot mark som kommunen äger är det mark- och exploateringssektionen som lämnar medgivande. Kommunen skriver att sektionen utreder hur sådana förfrågningar ska hanteras, att utredningen beräknas bli klar i slutet av januari 2027 och att inga grannemedgivanden lämnas under tiden. En " + _L.format("friggebod.html", "friggebod") + " eller tillbyggnad mot en kommunal parkremsa kan alltså behöva placeras om.",
     ],
     "aside": None},
    {"id": "grans-huddinge", "h2": "Var går gränsen på tomten?",
     "paras": [
       "Innan vi mäter ut ett nytt hus eller en tillbyggnad nära gränsen behöver gränsen vara känd. Huddinge har en egen lantmäterimyndighet, en av 40 kommunala i landet, som har funnits sedan 1997 och arbetar med kommunens cirka 24 000 fastigheter. Finns gränsmarkeringar är det som utgångspunkt de som visar var gränsen går. Saknas de kan förrättningskartan från när fastigheten bildades innehålla mått och uppgifter om markeringarna.",
       "Har markeringarna försvunnit kan de sättas ut på nytt genom särskild gränsutmärkning, om läget kan räknas fram ur förrättningshandlingarna utan oklarheter. Den som ansöker betalar, och markeringen blir rättsligt gällande. Är läget oklart krävs i stället en fastighetsbestämning. En gränsutvisning, där gränsen visas med träpålar eller sprayfärg, är enklare men inte juridiskt bindande. Den beställs hos kommunens mät- och kartenhet.",
       "Ska tomten delas sker det genom avstyckning i en lantmäteriförrättning, och detaljplanen reglerar bland annat hur stor en tomt minst måste vara. Lantmäterimyndigheten ger kostnadsfri rådgivning i upp till 25 minuter om förrättningsåtgärder.",
     ],
     "aside": {"title": "Gränsen i Huddinge", "items": [
       "Befintliga gränsmarkeringar gäller först",
       "Förrättningskartan visar mått",
       "Gränsutvisning är inte bindande",
       "25 minuters gratis rådgivning"]}},
    {"id": "tidsplan-huddinge", "h2": "Tidsplanen: från ansökan till slutsamråd",
     "paras": [
       "Ett ärende granskas oftast av en bygglovshandläggare och en byggnadsinspektör. Behöver de nya handlingar försöker kommunen höra av sig inom tre veckor. Ett lovärende ska enligt kommunen ha ett beslut inom tio veckor och en anmälan inom fyra. Hålls inte tiden reduceras avgiften med en femtedel för varje vecka, men tiden räknas om från den dag ärendet blev komplett. Därför lägger vi tid på att ansökan är fullständig, med skalenliga och måttsatta ritningar.",
       "Efter beslutet bokas inspektören för tekniskt samråd, där kontrollplanen och organisationen av bygget gås igenom. För större byggen görs minst ett arbetsplatsbesök, och när arbetet är klart hålls ett slutsamråd på plats innan slutbesked kan ges. Bokningen kan göras tidigast två veckor före mötet, och den luckan planerar vi in i tidplanen.",
       "Före ansökan kan du boka rådgivning med en handläggare, men kommunen påpekar att den ger generella svar och inget besked om lov. Mer om vad som gäller för " + _L.format("tillbyggnad-huddinge.html", "tillbyggnad i Huddinge") + " finns på en egen sida, och om arbetssättet under " + _L.format("byggfirma.html", "byggfirma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi upp ett byggprojekt i Huddinge",
  "steps": [
    ("Platsbesök", "Vi tittar på huset, tomtgränserna, grannarnas hus och om tomten gränsar mot kommunal mark."),
    ("Gräns och plan", "Gränsmarkeringar, detaljplan och avstånd kontrolleras innan något ritas."),
    ("Skriftligt kostnadsförslag", "Byggdelar, installationer och ROT-berättigat arbete redovisas var för sig."),
    ("Medgivanden och ansökan", "Grannarnas medgivanden tas in där det behövs och ansökan lämnas komplett."),
    ("Samråd och bygge", "Tekniskt samråd, sedan bygget med en kontakt för alla hantverkare."),
    ("Slutsamråd", "Vi förbereder underlaget till slutsamrådet och slutbeskedet."),
  ],
  "rot_h2": "Rotavdrag för byggprojekt i Huddinge",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Det gäller arbete på plats, inte material eller resor, och du ska äga bostaden när arbetet görs.",
    "En tillbyggnad ger avdrag om någon av dess sidor sitter ihop med husets yttervägg till minst 75 procent, eller om det finns en dörr emellan. Ett helt nytt hus eller en fristående byggnad som en friggebod ger inget avdrag, och inte heller bygglovshandlingar. Vi gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Huddinge?",
  "price": [
    "Storlek, grundläggning och hur den nya delen ansluts till huset väger tyngst. Avstånd till gränser och grannars medgivanden kan styra placeringen, och därmed hur mycket mark som behöver göras i ordning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur lång tid har grannarna på sig att yttra sig om vårt bygglov i Huddinge?",
     "Oftast två veckor, enligt kommunen. Synpunkterna lämnas via e-tjänsten, och en negativ synpunkt skickas till dig så att du kan bemöta den."),
    ("Kan Huddinge kommun ge medgivande när vi vill bygga nära kommunens mark?",
     "Inte just nu. Kommunen skriver att mark- och exploateringssektionen utreder frågan till slutet av januari 2027 och inte lämnar grannemedgivanden under tiden."),
    ("Behöver grannens medgivande för vår friggebod skickas in till kommunen?",
     "Nej. Huddinge kommun rekommenderar att det är skriftligt så att det kan bevisas, men det ska inte skickas in. Alla ägare till grannfastigheten ska godkänna placeringen."),
    ("Vem sätter ut en försvunnen gränsmarkering på vår tomt i Huddinge?",
     "Kommunens lantmäterimyndighet, genom särskild gränsutmärkning om läget går att räkna fram ur förrättningshandlingarna. Annars krävs en fastighetsbestämning."),
    ("Vad händer om kommunen inte beslutar om bygglovet inom tio veckor?",
     "Huddinge kommun skriver att avgiften då reduceras med en femtedel för varje vecka som tiden överskrids. Tiden räknas från den dag ärendet är komplett."),
  ],
  "sources": [
    _SCB,
    ("Huddinge kommun – Grannemedgivande", _HU + "bygglov/grannemedgivande"),
    ("Huddinge kommun – Bygglovets olika steg", _HU + "bygglov/bygglovets-olika-steg"),
    ("Huddinge kommun – Boka möte med bygglovsavdelningen", _HU + "bygglov/boka-mote-med-bygglovsavdelningen"),
    ("Huddinge kommun – Om lantmäterimyndigheten", _HU + "lantmaterimyndigheten-huddinge/om-lantmaterimyndigheten"),
    ("Huddinge kommun – Lantmäteriförrättningar och rättsliga uppdrag", _HU + "lantmaterimyndigheten-huddinge/lantmateriforrattningar-och-andra-tjanster"),
    ("Huddinge kommun – Fastighetsgränser", _HU + "lantmaterimyndigheten-huddinge/fastighetsgranser"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ni bygga nära gränsen i Huddinge?", "Boka ett gratis platsbesök, så reder vi ut gränsen, grannarna och lovfrågan."),
  "img": [
    ("Enplansvilla i Huddinge med vitt staket, berghäll och höga tallar",
     "1950s Swedish one-and-a-half storey wooden villa painted light grey with a new single-storey timber extension with large windows on the side, low white picket fence marking the boundary to the neighbouring garden, birch and pine trees, granite outcrop, Huddinge suburb, late summer daylight, empty scene"),
    ("Gränsmarkering i form av ett järnrör vid en tomtgräns i en trädgård",
     "close-up of an old iron boundary marker pipe sticking out of the grass at the corner between two Swedish garden plots, a small wooden survey stake beside it, low hedge and lawn, soft daylight, shallow depth of field, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ NORRTÄLJE
"byggforetag-norrtalje.html": {
  "kind": "district", "service": "byggforetag", "ort": "Norrtälje", "svc_label": "Byggföretag",
  "title": "Byggföretag i Norrtälje – nytt hus, förhandsbesked och brunn",
  "description": "Byggföretag i Norrtälje: förhandsbesked för nytt hus utanför detaljplan, riksintressen, egen brunn nära kusten och vägen från startbesked till inflyttning.",
  "h1": "Byggföretag i Norrtälje",
  "lead": "Norrtälje kommun har 19 171 bostäder i småhus enligt SCB:s statistik för 2025. Den som vill bygga ett nytt hus utanför detaljplan, på landet eller i skärgården, börjar ofta med frågan om platsen alls får bebyggas. Geal Entreprenad AB bygger nya hus, tillbyggnader och större ombyggnader som total entreprenad, och i Norrtälje hör förhandsbeskedet och vattnet till de första punkterna.",
  "card": "Nytt hus, förhandsbesked och egen brunn.",
  "sections": [
    {"id": "forhandsbesked-norrtalje", "anchor": "Förhandsbesked",
     "h2": "Förhandsbeskedet prövar platsen innan ritningarna",
     "paras": [
       "Ett förhandsbesked är enligt Norrtälje kommun en lokaliseringsprövning av om det går att bygga på fastigheten och om vatten och avlopp går att lösa. Det passar när du vill bygga nytt eller stycka av utanför detaljplanerat område och ännu inte har några ritningar. Det räcker med en skiss eller en beskrivning som visar hur byggnaden ska användas.",
       "Syftet är att få ett bindande beslut innan pengar läggs på projektering och bygglovsritningar. Ett positivt besked betyder däremot inte att något får påbörjas. Bygglov krävs, och för ett enskilt avlopp krävs tillstånd. Ska tomten styckas av skickas förhandsbeskedet till Lantmäteriet tillsammans med ansökan om avstyckning.",
       "I prövningen tittar kommunen bland annat på att vatten och avlopp kan lösas på ett tillfredsställande sätt, att brukningsvärd jordbruksmark inte tas i anspråk, att platsen inte strider mot riksintressen och att den inte är bullerutsatt. Det görs också en bedömning av om det behövs en detaljplan, och om huset måste placeras eller utformas på ett visst sätt ska det framgå av beskedet.",
     ],
     "aside": {"title": "Det här prövas", "items": [
       "Vatten och avlopp",
       "Brukningsvärd jordbruksmark",
       "Riksintressen och buller",
       "Behovet av detaljplan"]}},
    {"id": "plan-norrtalje", "h2": "Inom eller utanför detaljplan",
     "paras": [
       "Kommunens karta visar om fastigheten omfattas av en detaljplan. Inom plan prövar bygg- och miljönämnden om åtgärden stämmer med planen och med vissa andra krav i plan- och bygglagen. Utanför plan kan i stället riksintressen för kulturmiljövård, naturvård, friluftsliv eller totalförsvaret påverka prövningen, liksom åkermark och bullernivåer. För Norrtälje stad finns dessutom ett bevarandeprogram i kommunens karta.",
       "En del åtgärder kräver anmälan i stället för lov. Kommunen nämner installation eller ändring av eldstad, rökkanal och ventilation, ändringar i brandskyddet och vissa rivningar. En ombyggnad av ett äldre hus kan alltså kräva anmälan även när inget bygglov behövs.",
     ],
     "aside": None},
    {"id": "brunn-norrtalje", "h2": "Egen brunn nära kusten",
     "paras": [
       "Den som inte har kommunalt vatten ansvarar själv för att brunnen ger tillräckligt med vatten av godkänd kvalitet. Norrtälje kommun påpekar att större delen av kommunen ligger under den så kallade marina gränsen, alltså mark som efter senaste istiden har täckts av salt eller bräckt vatten. Borras en brunn för djupt nära kusten, eller tas för mycket vatten ur den, kan saltvatten tränga in. På sommaren och i tätbebyggda områden kan det vara extra kritiskt.",
       "För att skydda grundvattnet är det anmälnings- eller tillståndspliktigt att borra för dricksvatten inom utvalda områden, bland annat inom 300 meter från kustlinjen, inom detaljplan och på vissa öar. Kommunens karta visar om din fastighet berörs. Kommunen rekommenderar också att brunnen registreras hos SGU och hänvisar till Livsmedelsverkets råd att analysera vattnet minst vart tredje år.",
       "Vattencentrum, som drivs av Norrtälje Vatten och Avfall, ger opartisk och kostnadsfri rådgivning om enskilt vatten och avlopp. För ett nytt hus är det bra att veta tidigt var brunn och avlopp ska ligga, eftersom placeringen påverkar var huset kan stå. Om att göra om ett " + _L.format("fritidshus.html", "fritidshus") + " till åretruntbostad finns mer på en egen sida.",
     ],
     "aside": {"title": "Brunnen i Norrtälje", "items": [
       "Anmälan eller tillstånd i utvalda områden",
       "300 meter från kustlinjen",
       "Risk för saltvatten vid djup borrning",
       "Registrera brunnen hos SGU"]}},
    {"id": "start-slut-norrtalje", "h2": "Från startbesked till inflyttning",
     "paras": [
       "Vid enklare ärenden ges startbeskedet ofta i samma beslut som bygglovet. Vid större byggen krävs ett tekniskt samråd först, bland annat när det behövs en kontrollansvarig. Kommunen avråder från att börja innan lovet har vunnit laga kraft, eftersom det sker på egen risk. En detalj som skiljer sig från tätorten: utanför detaljplan krävs inte marklov, så de markåtgärder som redovisats för nybygget får påbörjas före det tekniska samrådet och startbeskedet. Inom detaljplan kan kommunen ge ett separat startbesked för markarbetet.",
       "Huset ska stakas ut om det framgår av bygglovet. Har det varit tekniskt samråd hålls vanligtvis ett slutsamråd där kontrollplanen, villkoren och den kontrollansvariges utlåtande gås igenom. Huset får inte användas förrän slutbesked finns, annars kan nämnden ta ut en byggsanktionsavgift.",
       "Före inflyttningen ska ett enskilt avlopp anmälas som färdigt med en entreprenörsrapport, och ska huset anslutas till kommunalt vatten och avlopp fylls en servisanmälan i. Norrtälje Vatten och Avfall behöver också veta att huset tas i bruk för att kärl och slamskyltar ska komma ut. Vill du hellre bygga ut det hus du har, läs om " + _L.format("tillbyggnad.html", "tillbyggnad") + " och om hela arbetssättet under " + _L.format("byggfirma.html", "byggfirma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett nytt hus i Norrtälje till",
  "steps": [
    ("Platsbesök", "Vi går över tomten och tittar på terräng, tillfart och var brunn och avlopp kan ligga."),
    ("Kartor och förhandsbesked", "Detaljplan, riksintressen och brunnsområden kontrolleras och förhandsbesked söks vid behov."),
    ("Skriftligt kostnadsförslag", "Mark, grund, stomme och installationer redovisas som egna poster."),
    ("Bygglov och samråd", "Ritningar och kontrollplan tas fram, och tekniskt samråd hålls om det krävs."),
    ("Bygget", "Markarbete, grund, stomme, tak och installationer samordnas av oss."),
    ("Slutbesked och inflyttning", "Slutsamråd, entreprenörsrapport och anmälningar till Norrtälje Vatten och Avfall."),
  ],
  "rot_h2": "Rotavdrag – vad som gäller i Norrtälje",
  "rot": [
    "Ett helt nytt hus ger inget rotavdrag. Det gör däremot en tillbyggnad på ett befintligt hus som sitter ihop med ytterväggen till minst 75 procent på någon sida eller har en dörr emellan, liksom markarbeten för att dra in vatten och avlopp till ett hus du redan äger och bor i eller använder som fritidshus.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material och resor räknas inte. Är huset yngre än fem år ger ombyggnad och tillbyggnad inget avdrag. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Norrtälje?",
  "price": [
    "Terrängen, grundläggningen och hur vatten och avlopp ska lösas betyder mycket, liksom tillfarten för material och maskiner till en tomt på landet eller en ö. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi börja bygga när vi har fått ett positivt förhandsbesked i Norrtälje?",
     "Nej. Förhandsbeskedet prövar bara platsen. Bygglov krävs innan bygget börjar, och ett enskilt avlopp kräver tillstånd."),
    ("Behövs förhandsbesked för att stycka av en tomt utanför detaljplan i Norrtälje?",
     "Kommunen skriver att förhandsbeskedet behövs som underlag i ett ärende om avstyckning. Det skickas till Lantmäteriet tillsammans med ansökan."),
    ("Får vi gräva för grunden innan startbeskedet kommit i Norrtälje?",
     "Utanför detaljplan krävs inte marklov, så de markåtgärder som redovisats för nybyggnaden får påbörjas före startbeskedet. Inom plan krävs ofta marklov och startbesked först."),
    ("Måste vi anmäla en ny borrad brunn nära havet i Norrtälje?",
     "Inom vissa områden, bland annat inom 300 meter från kustlinjen, inom detaljplan och på vissa öar, är det anmälnings- eller tillståndspliktigt. Kommunens karta visar om fastigheten berörs."),
    ("Vad ska anmälas innan vi flyttar in i det nya huset i Norrtälje?",
     "Ett enskilt avlopp anmäls som färdigt med en entreprenörsrapport, kommunalt VA kräver en servisanmälan och Norrtälje Vatten och Avfall ska få veta att huset tas i bruk."),
  ],
  "sources": [
    _SCB,
    ("Norrtälje kommun – Förhandsbesked", _NT + "bygga-andra-riva/forhandsbesked/"),
    ("Norrtälje kommun – Efter bygglovsbeslutet: startbesked och slutbesked", _NT + "bygga-andra-riva/slutsamrad-och-slutbesked/"),
    ("Norrtälje kommun – Skillnad mellan bygglovspliktiga, anmälningspliktiga och bygglovsbefriade åtgärder", _NT + "bygga-andra-riva/skillnad-mellan-atgarder/"),
    ("Norrtälje kommun – Enskilt vatten", _NT + "vatten-och-avlopp/enskilt-vatten/"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Vill ni bygga nytt i Norrtälje kommun?", "Boka ett gratis platsbesök, så går vi igenom tomten, vattnet och vägen till bygglov."),
  "img": [
    ("Nybyggt rödmålat trähus på en tomt med berghällar och tallar i Norrtälje kommun",
     "newly built Swedish one-and-a-half storey house with falu red vertical wooden panel, white window frames and a black metal roof on a rural plot with granite outcrops, pine trees and a gravel drive, Roslagen countryside near the Baltic coast, Norrtälje, summer daylight, empty scene"),
    ("Stensatt brunn på gräsmattan framför ett nytt rödmålat hus på landet",
     "close-up of a round cast-iron cover of a drilled water well on a freshly sown lawn beside the stone plinth of a new red wooden house, granite rocks and pines in the background, Swedish countryside, soft daylight, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ NACKA
"byggforetag-nacka.html": {
  "kind": "district", "service": "byggforetag", "ort": "Nacka", "svc_label": "Byggföretag",
  "title": "Byggföretag i Nacka – VA, LTA och dagvatten när du bygger",
  "description": "Byggföretag i Nacka: vatten och avlopp till en ny bostadsenhet, LTA-pump vid anslutning, byggvatten under bygget och dagvattnet på den egna tomten.",
  "h1": "Byggföretag i Nacka",
  "lead": "Nacka har 16 435 bostäder i småhus enligt SCB:s statistik för 2025. När något nytt byggs på en villatomt blir vatten och avlopp en egen del av projektet: hur ledningarna kopplas, om det krävs en pump och vart regnvattnet tar vägen. Geal Entreprenad AB bygger till, bygger nytt på tomten och gör större ombyggnader som total entreprenad, och här går vi igenom det Nacka vatten och avfall skriver om just det.",
  "card": "VA, LTA och dagvatten på tomten.",
  "sections": [
    {"id": "bostadsenhet-nacka", "anchor": "Ny bostadsenhet",
     "h2": "Ny bostadsenhet på samma VA-anslutning",
     "paras": [
       "Sedan den 1 december 2025 är fler byggåtgärder lovfria, men Nacka vatten och avfall påpekar att det fortfarande krävs anmälan för byggnader med tekniska lösningar som vatten och avlopp. Ändras antalet bostadsenheter på en fastighet som är ansluten till kommunalt VA är fastighetsägaren skyldig att anmäla det. Enligt VA-taxan tas en engångsavgift ut för varje tillkommande bostadsenhet, och anmäls den inte omgående kan dröjsmålsränta tas ut från två månader efter avgiftsskyldigheten.",
       "Med komplementbostadshus menar Nacka vatten och avfall till exempel attefallshus, komplementbostad, kontor, ateljé, gäststuga och liknande. Ledningarna till en sådan byggnad ska kopplas till fastighetens befintliga VA-nät, efter punkten där vattenmätaren sitter i bostadshuset. Därtill tas anläggnings- och brukningsavgift ut enligt den gällande taxan.",
       "För oss betyder det att ledningsdragningen till ett " + _L.format("attefallshus.html", "attefallshus") + " eller en gäststuga ritas tidigt, från mätaren i huvudbyggnaden och ut över tomten, och att anmälan till VA-huvudmannen finns med i tidplanen.",
     ],
     "aside": {"title": "Fler bostäder på tomten", "items": [
       "Anmäl ny bostadsenhet direkt",
       "Engångsavgift enligt VA-taxan",
       "Koppla efter vattenmätaren",
       "Anmälan för VA trots lovfrihet"]}},
    {"id": "lta-nacka", "h2": "När avloppet behöver en LTA-pump",
     "paras": [
       "På vissa platser i Nacka måste det allmänna ledningsnätet trycksättas för att avloppsvattnet ska komma vidare. Då behövs ett LTA-system, lätt trycksatt avlopp, som består av en brunn, en backventil och en larmenhet tillsammans med en pump som fastighetsägaren lånar av Nacka vatten och avfall. Även där det allmänna nätet har självfall kan en tomt behöva LTA om husets egna ledningar inte kan få självfall. Då äger fastighetsägaren pumpen själv.",
       "Backventilen monteras av fastighetsägaren vid fastighetsgränsen, om den inte redan sitter vid huvudledningen. Larmet ska sitta där det hörs väl i bostaden och inte i tvättstuga, pannrum eller annat stängt utrymme, och el ska dras fram till pumpen. Placeringen bestäms i samråd med Nacka vatten och avfall och ska vara lättillgänglig för underhåll.",
       "Ordningen är viktig. Systemet levereras ungefär två veckor efter beställningen. När ledningarna är anslutna och backventilen installerad ska gropen lämnas öppen tills installationen har besiktigats, vilket vanligen sker inom en vecka. Först när allt i färdiganmälan är godkänt kan vattenmätaren och pumpen sättas upp. I anläggningsavgiften ingår en timmes konsultation om placering och ledningsdragning.",
     ],
     "aside": None},
    {"id": "byggvatten-nacka", "h2": "Byggvatten och vatten ur schaktet",
     "paras": [
       "Behövs vatten innan huset är anslutet kan man ansöka om byggvatten, en tillfällig anslutning där förbrukningen mäts med en vattenmätare som hyrs av Nacka vatten och avfall. Ansökan ska göras i god tid innan behovet uppstår.",
       "Vid sprängning, borrning och schaktning samlas ofta regnvatten, inträngande grundvatten och spolvatten i gropen. Det kallas länshållningsvatten, och det är förbjudet att leda bort det till spill- eller dagvattennätet utan samråd med Nacka vatten och avfall. På en bergig tomt där grunden ska sprängas fram tar vi därför upp frågan innan arbetet börjar.",
     ],
     "aside": {"title": "Under byggtiden", "items": [
       "Sök byggvatten i god tid",
       "Hyrd mätare för tillfällig anslutning",
       "Samråd innan länshållningsvatten leds bort"]}},
    {"id": "dagvatten-nacka", "h2": "Regnvattnet stannar på den egna tomten",
     "paras": [
       "I Nacka har fastighetsägaren ansvar för att ta hand om sitt eget dagvatten. Kommunen arbetar med anvisningen att de första 10 millimetrarna regn som rinner av ska tas om hand nära källan, och det är ett minsta mått. Dag- och dräneringsvatten får inte ledas in på grannens tomt eller ut på gatan, och naturliga flöden som rinner över tomten får inte stoppas.",
       "En tumregel i kommunens vägledning är att det behövs en infiltrationsyta på en till två gånger den hårdgjorda ytan. Ett tak på 150 kvadratmeter kan alltså behöva uppemot 300 kvadratmeter mark. På tät lera eller berg, eller där grundvattnet står högt, föreslår kommunen i stället upphöjda planteringar, gröna tak eller underjordiska magasin.",
       "En ny tillbyggnad eller ett nytt hus ökar de hårda ytorna. Kommunen råder att välja grus, singel, hålsten eller marksten med genomsläppliga fogar till uppfarter och gångar, och att uppfarten ska luta mot grönytor utan kantsten. Det planerar vi in i markritningen. Läs mer om " + _L.format("tillbyggnad-nacka.html", "tillbyggnad i Nacka") + " och om hela arbetssättet under " + _L.format("byggfirma.html", "byggfirma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras ett byggprojekt i Nacka",
  "steps": [
    ("Platsbesök", "Vi tittar på huset, tomtens lutning, berg och var vattenmätare och ledningar finns."),
    ("VA-frågan", "Vi reder ut om det blir en ny bostadsenhet, om LTA behövs och vad som ska anmälas."),
    ("Skriftligt kostnadsförslag", "Mark, ledningar, byggnad och ROT-berättigat arbete redovisas var för sig."),
    ("Lov, anmälan och beställning", "Handlingar till kommunen och beställning av LTA eller byggvatten i god tid."),
    ("Bygget", "Schakt, ledningar, grund och byggnad samordnas, med besiktning innan gropen fylls igen."),
    ("Färdiganmälan och genomgång", "Underlaget till färdiganmälan tas fram och vi går igenom resultatet med dig."),
  ],
  "rot_h2": "Rotavdrag för bygge och ledningar i Nacka",
  "rot": [
    "Skatteverket godkänner rotavdrag för markarbeten för att dra in el-, vatten- och avloppsledningar och avloppsbrunnar, även vid indragning av kommunalt VA, och för att dränera husgrunder. En tillbyggnad ger avdrag om den sitter ihop med husets yttervägg till minst 75 procent på någon sida eller har en dörr emellan. Ett helt nytt hus eller en fristående gäststuga ger inget avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material och resor räknas inte, och VA-huvudmannens avgifter ingår inte. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Nacka?",
  "price": [
    "Berg och lutning styr hur mycket som måste sprängas eller schaktas, och om avloppet kan få självfall eller behöver pump. Längden på ledningarna och hur dagvattnet ska tas om hand spelar också in. Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste vi anmäla en gäststuga med vatten och avlopp till Nacka vatten och avfall?",
     "Ja. Förändras antalet bostadsenheter på en fastighet med kommunalt VA är fastighetsägaren skyldig att anmäla det, och en engångsavgift tas ut enligt VA-taxan."),
    ("Var ska ledningarna till ett komplementbostadshus i Nacka kopplas in?",
     "På fastighetens befintliga VA-nät, efter punkten där vattenmätaren sitter i bostadshuset, enligt Nacka vatten och avfall."),
    ("Hur lång tid tar det att få en LTA-pump levererad i Nacka?",
     "Ungefär två veckor efter beställningen, enligt Nacka vatten och avfall. Gropen ska sedan stå öppen tills installationen är besiktigad."),
    ("Var får larmet till LTA-pumpen sitta?",
     "Där det hörs väl i bostaden. Det ska inte placeras i tvättstuga, pannrum eller annat stängt utrymme."),
    ("Hur stor yta behövs för att ta hand om takvattnet på tomten i Nacka?",
     "Kommunens tumregel är en till två gånger den hårdgjorda ytan. Ett tak på 150 kvadratmeter kan behöva uppemot 300 kvadratmeter genomsläpplig mark."),
  ],
  "sources": [
    _SCB,
    ("Nacka vatten och avfall – Attefallshus och andra komplementbyggnader", _NA + "attefallshus/"),
    ("Nacka vatten och avfall – Installera LTA", _NA + "lta/"),
    ("Nacka vatten och avfall – Byggvatten och länshållningsvatten", _NA + "byggvatten-och-lanshallningsvatten/"),
    ("Nacka kommun – Dagvatten: vägledning för enskilda fastighetsägare",
     "https://www.nacka.se/boende-miljo/dagvatten/vagledning-fastighetsagare/"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ni bygga på en bergig tomt i Nacka?", "Boka ett gratis platsbesök, så går vi igenom ledningar, pump och dagvatten på plats."),
  "img": [
    ("Villa på en bergig tomt i Nacka med grusad uppfart som lutar mot gräsmattan",
     "Swedish 1960s single-storey villa with light grey wooden panel and black concrete tile roof on a sloping plot with granite outcrops and tall pine trees, a light gravel driveway sloping towards a lawn without kerbs, neighbouring villas partly visible between the trees, Boo Nacka suburb, summer daylight, completely empty scene with nobody in it"),
    ("Schakt med ny avloppsledning och pumpbrunn vid en villa",
     "open trench in a Swedish villa garden with a new grey plastic sewer pipe and a cylindrical black polyethylene pressure sewer pump well with green lid, coarse gravel bedding, excavated soil and granite rock on the side, house plinth in the background, overcast daylight, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"byggforetag-osteraker.html": {
  "kind": "district", "service": "byggforetag", "ort": "Österåker", "svc_label": "Byggföretag",
  "title": "Byggföretag i Österåker – riva, bygga nytt och gatukostnader",
  "description": "Byggföretag i Österåker: rivningslov och rivningsanmälan, materialinventering, marklov för schakt och fyllning och gatukostnader i förnyelseområden.",
  "h1": "Byggföretag i Österåker",
  "lead": "I Österåker finns 13 635 bostäder i småhus enligt SCB:s statistik för 2025. Ska ett äldre hus ersättas med ett nytt handlar de första stegen om att riva rätt, att ändra marken utan att störa grannarna och att veta vad en ny detaljplan kan kosta i gatukostnader. Geal Entreprenad AB bygger nya hus som total entreprenad, med en kontakt genom hela projektet.",
  "card": "Rivning, markarbete och gatukostnader.",
  "sections": [
    {"id": "rivning-osteraker", "anchor": "Rivningslov",
     "h2": "Rivningslov eller rivningsanmälan",
     "paras": [
       "Österåkers kommun skriver att rivning innebär att ta bort en byggnad helt, eller en del av den tillsammans med dess bärande stomme. Det räknas som rivning även om grunden ska stå kvar och användas till ett nytt hus, och även om man bara tar bort en veranda. Står stommen kvar och bara icke bärande delar tas bort är det inte rivning.",
       "Inom detaljplan krävs rivningslov för hela eller delar av byggnader. Huvudregeln är att en byggnad som en gång fått bygglov också kräver rivningslov, oavsett storlek. Kommunens exempel är ett garage på 25 kvadratmeter med bygglov, som kräver rivningslov, medan en lovfri friggebod inte gör det. Utanför detaljplan krävs rivningslov bara för särskilt värdefulla byggnader eller byggnader i särskilt värdefulla bebyggelseområden, som syns i kommunens karta över kulturmiljöer.",
       "Oberoende av lovplikten krävs rivningsanmälan om byggnaden är större än 50 kvadratmeter, inom och utanför detaljplan. Det är den befintliga byggnadens yta som avgör, inte hur stor del som rivs. Undantaget är ekonomibyggnader utanför detaljplan.",
     ],
     "aside": {"title": "Rivning i Österåker", "items": [
       "Lovgiven byggnad i plan: rivningslov",
       "Över 50 m²: rivningsanmälan",
       "Situationsplan på enkelt kartutdrag",
       "Kontrollplan och materialinventering"]}},
    {"id": "material-osteraker", "h2": "Materialinventering före rivningen",
     "paras": [
       "Till ansökan eller anmälan hör en situationsplan på ett enkelt kartutdrag där det som ska rivas är markerat, ett förslag till kontrollplan och en ifylld materialinventering. Inventeringen ska visa vilka material som är farliga för människor eller miljö och hur de ska tas om hand, hur övrigt rivningsmaterial ska sorteras och om något kan återbrukas eller återvinnas. Det är byggherren som ansvarar för att den görs.",
       "Rivningen får inte börja förrän startbesked finns, och för vissa större rivningar ska byggherren utse en kontrollansvarig som hjälper till med kontrollplanen och med att identifiera material som kan återanvändas. Börjar man innan startbeskedet kan byggnadsnämnden besluta om en sanktionsavgift.",
       "Vi tar fram underlaget, planerar sorteringen och samordnar rivningen med det nya bygget, så att tomten inte står tom längre än nödvändigt. Gäller det i stället en " + _L.format("villarenovering.html", "renovering av villan") + " där stommen står kvar räknas det inte som rivning.",
     ],
     "aside": None},
    {"id": "mark-osteraker", "h2": "Schakt, fyllning och marklov",
     "paras": [
       "Inom detaljplan krävs marklov om markens höjd ändras med mer än 0,5 meter från ursprunglig nivå, och om träd ska fällas där detaljplanen kräver marklov för det. Marklov behövs inte om markåtgärderna ingår i ett bygglov, om marknivån ändras till höjder som planen föreskriver eller om fastigheten ligger utanför detaljplan.",
       "En ansökan om marklov ska innehålla en situationsplan på Nybyggnadskarta C, en markplaneringsritning med släntfot, släntkrön, befintliga och nya höjder och eventuella murar, marksektioner, fasadritningar med gamla och nya marklinjer och ett förslag till kontrollplan.",
       "Kommunen påminner om att du ansvarar för att dagvattnet från din fastighet inte leds över till grannarna, och att olika fyllnadsmassor och ytskikt leder undan vatten olika bra. Ledningar i marken kan kontrolleras via Ledningskollen, och går någon av är det du som ansvarar. Sprängning kräver oftast tillstånd från Polismyndigheten, och hittar man något som kan vara en fornlämning ska arbetet stoppas och Länsstyrelsen kontaktas.",
     ],
     "aside": {"title": "Marklov krävs", "items": [
       "Mer än 0,5 meter höjdändring i plan",
       "Trädfällning där planen kräver det",
       "Inte om marken ingår i bygglovet",
       "Inte utanför detaljplan"]}},
    {"id": "gatukostnad-osteraker", "h2": "Gatukostnader när området får ny detaljplan",
     "paras": [
       "När gator och andra allmänna platser byggs ut i samband med en ny eller ändrad detaljplan kan kommunen ta ut gatukostnader. I så kallade förnyelseområden kan kostnaderna fördelas mellan de berörda fastighetsägarna. En gatukostnadsutredning visar vilka fastigheter som ingår, vilka kostnader som omfattas och hur de fördelas. Den går ut på samråd och granskning, och beslutet fattas av kommunfullmäktige. Just nu pågår en utredning för detaljplanen Valsättra del 2.",
       "Betalningsskyldigheten inträder först när utbyggnaden är klar och den allmänna platsen kan användas, normalt efter slutbesiktning. Anstånd eller avbetalning kan i vissa fall beviljas. Säljs fastigheten efter att betalningsskyldigheten inträtt är det den nya ägaren som ska betala, men inte belopp som förfallit före tillträdet. Fördelningsbeslutet kan laglighetsprövas, och själva kostnaden för en fastighet kan prövas av mark- och miljödomstolen.",
       "För den som planerar ett nytt hus är det värt att känna till, eftersom ett pågående planarbete kan påverka både när ett nytt hus kan byggas och vad det kostar totalt. Om taket på ett befintligt hus, se " + _L.format("takrenovering-osteraker.html", "takrenovering i Österåker") + ", och om arbetssättet under " + _L.format("byggfirma.html", "byggfirma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går riv och nybygge till i Österåker",
  "steps": [
    ("Platsbesök", "Vi går igenom det befintliga huset, tomtens höjder och vad som ska rivas eller sparas."),
    ("Planer och kartor", "Detaljplan, kulturmiljökarta och eventuell gatukostnadsutredning kontrolleras."),
    ("Skriftligt kostnadsförslag", "Rivning, mark och nybygge redovisas var för sig."),
    ("Handlingar", "Rivningsanmälan eller rivningslov, materialinventering och vid behov marklov tas fram."),
    ("Rivning och mark", "Sorterad rivning efter startbesked, sedan schakt och grund."),
    ("Nybygget", "Stomme, tak och installationer, och till sist genomgång med dig."),
  ],
  "rot_h2": "Rotavdrag vid bygge i Österåker",
  "rot": [
    "Ett helt nytt hus ger inget rotavdrag, inte heller om det ersätter ett rivet. För ett befintligt hus kan en tillbyggnad ge avdrag om den sitter ihop med ytterväggen till minst 75 procent på någon sida eller har en dörr emellan. Sprängarbete som krävs för en utbyggnad ger också avdrag, liksom att återställa marken inom sex månader efter ett godkänt gräv- eller markarbete.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material och resor räknas inte. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Österåker?",
  "price": [
    "Hur stort huset som ska rivas är, vilka material inventeringen hittar, hur mycket marken ska ändras och vad det nya huset ska innehålla. Gatukostnader och kommunens avgifter tillkommer utanför vår offert. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi rivningslov för ett gammalt garage på tomten i Österåker?",
     "Ligger tomten inom detaljplan och har garaget en gång fått bygglov krävs som huvudregel rivningslov, oavsett storlek. En lovfri friggebod kräver det inte."),
    ("Räknas det som rivning om vi behåller grunden till det nya huset?",
     "Ja. Österåkers kommun räknar det som rivning när hela byggnaden utom grunden tas bort, till exempel för att grunden ska användas till en ny byggnad."),
    ("Vad ska materialinventeringen inför rivningen visa?",
     "Vilka material som är farliga för människor eller miljö och hur de tas om hand, hur övrigt material ska sorteras och om något kan återbrukas eller återvinnas."),
    ("Behöver vi marklov för att fylla upp tomten en halvmeter i Österåker?",
     "Inom detaljplan krävs marklov om höjden ändras med mer än 0,5 meter från ursprunglig nivå, om inte markåtgärderna ingår i ett bygglov. Utanför detaljplan krävs inget marklov."),
    ("När ska gatukostnaden betalas i ett förnyelseområde i Österåker?",
     "När gatorna och de allmänna platserna är utbyggda och kan användas, normalt efter slutbesiktning. Då faktureras de berörda fastighetsägarna."),
  ],
  "sources": [
    _SCB,
    ("Österåkers kommun – Riva, rivningslov", _OS + "bygganyttandraellerriva/rivarivningslov.4.367d658917909e8fc2bb2a.html"),
    ("Österåkers kommun – Markarbeten", _OS + "bygganyttandraellerriva/markarbeten.4.77c924619b9d91e3e28c6.html"),
    ("Österåkers kommun – Gatukostnader", _OS + "samhallsutveckling/gatukostnader.4.27d4a62417c1135094274af.html"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ett gammalt hus i Österåker ersättas med ett nytt?", "Boka ett gratis platsbesök, så går vi igenom rivning, mark och lovfrågor."),
  "img": [
    ("Nytt trähus bredvid en äldre sommarstuga på en tomt med tallar i Österåker",
     "new two-storey Swedish wooden villa with light grey panel and a black metal roof standing on a pine-covered plot next to a small old falu red summer cottage, gravel area and stacked timber, Roslagen landscape, Åkersberga Österåker, summer daylight, empty scene"),
    ("Container med rivningsvirke på grusplanen vid en äldre stuga som ska rivas",
     "one standard green steel skip container filled with old wooden boards and planks standing on a gravel drive next to a small weathered old Swedish wooden summer cottage with its windows removed, pine trees, Roslagen, overcast daylight, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ BOTKYRKA
"byggforetag-botkyrka.html": {
  "kind": "district", "service": "byggforetag", "ort": "Botkyrka", "svc_label": "Byggföretag",
  "title": "Byggföretag i Botkyrka – nytt hus, utfart och arbetsplats",
  "description": "Byggföretag i Botkyrka: handlingarna till bygglov för ett nytt hus, regler för in- och utfart, APD-plan, tunga transporter och sprängning på tomten.",
  "h1": "Byggföretag i Botkyrka",
  "lead": "Botkyrka har 12 582 bostäder i småhus enligt SCB:s statistik för 2025. Den som bygger ett nytt hus här möter både bygglovets krav och kommunens regler för gatan utanför: utfarten, transporterna och arbetsplatsen. Geal Entreprenad AB bygger nya hus och tillbyggnader som total entreprenad och samordnar allt från ritningar till slutbesked.",
  "card": "Nytt hus, utfart och byggarbetsplats.",
  "sections": [
    {"id": "handlingar-botkyrka", "anchor": "Handlingarna",
     "h2": "Handlingarna till ett nytt en- eller tvåbostadshus",
     "paras": [
       "Ett nytt en- eller tvåbostadshus kräver bygglov i Botkyrka, och innan bygget får börja ska det ha hållits ett tekniskt samråd och getts ett startbesked. Huset får inte tas i bruk förrän slutbesked finns. Kommunens checklista visar vad som ska skickas med, och ritningarna ska vara fackmannamässiga, skalenliga och högst i A3-format.",
       "Situationsplanen görs på en fullständig nybyggnadskarta i skala 1:400. Huset ska vara måttsatt med minst två avstånd i rät vinkel till tomtgränsen, och golvhöjden anges som en plushöjd. Fasad-, plan- och sektionsritningar görs i skala 1:100. Fasaderna ska visa marknivåer, takvinkel i grader, material och kulörer, och planritningen över entréplanet ska vara möblerad och visa att planet är tillgängligt för personer med nedsatt rörelseförmåga.",
       "Till ett nytt hus hör också en markplaneringsritning i 1:400 som visar in- och utfart, parkering, gamla och nya marknivåer, murar, plank, dagvatten och avfallshantering. Kommunen anger att en kontrollansvarig ska anmälas, att utstakning och lägeskontroll krävs och att strandskyddsdispens behövs om tomten ligger inom strandskyddat område.",
     ],
     "aside": {"title": "Checklistan i korthet", "items": [
       "Nybyggnadskarta i skala 1:400",
       "Fasad, plan och sektion i 1:100",
       "Markplanering med utfart och dagvatten",
       "Kontrollansvarig och utstakning"]}},
    {"id": "utfart-botkyrka", "h2": "Utfarten till gatan",
     "paras": [
       "Saknar tomten in- och utfart, eller ska den flyttas, ansöker du om det hos kommunen. Den del som hamnar på gatumark, parkmark eller annan allmän plats byggs som regel av kommunens upphandlade entreprenör, och fastighetsägaren står för kostnaden efter en syn på plats. Vid enklare förutsättningar kan fastighetsägaren få anlägga infarten själv i samråd med kommunens gatuingenjör, som då godkänner den vid en slutbesiktning.",
       "Kraven är konkreta. En fastighet får ha högst en in- och utfart, och murar, plank och häckar intill den får vara högst 0,8 meter för att sikten ska bli god. Det ska finnas sikttrianglar på minst 2,5 gånger 2,5 meter, och avståndet till övergångsställe och korsning ska vara minst 10 meter. Backning över cykelbana eller ut på huvudgata tillåts inte.",
       "På den allmänna platsen får infarten vara högst 3,0 meter bred och ska följa befintliga marknivåer. Ett vägdike får inte fyllas igen. Fastighetsägaren ska lägga en trumma under infarten, som regel 200 millimeter i diameter, och kommunen ska godkänna hur dagvattnet leds bort. Utfarten ritar vi därför in redan i situationsplanen, så att den stämmer med både bygglovet och gatan.",
     ],
     "aside": {"title": "Utfart i Botkyrka", "items": [
       "Högst en utfart per fastighet",
       "Sikttriangel minst 2,5 × 2,5 meter",
       "Högst 3,0 meter bred på allmän plats",
       "Trumma under infarten vid dike"]}},
    {"id": "arbetsplats-botkyrka", "h2": "Arbetsplatsen och transporterna",
     "paras": [
       "En APD-plan, arbetsplatsdispositionsplan, är en ritning som visar var containrar, bodar, upplag, ledningar, första hjälpen, samlingsplats, brandsläckare och brandfarliga varor finns på arbetsplatsen. I Botkyrka ska den även lämnas till Södertörns brandförsvarsförbund.",
       "Transporterna till tomten är en egen fråga. Kommunens gator har oftast bärighetsklass 2, och det finns inga vägar med bärighetsklass 4 i kommunen. Många lokala vägar är inte byggda för stora fordon, och kommunen skriver att även fordon längre än 12 meter kan ha svårt att komma fram. Den planerade färdvägen kan stämmas av med kommunen, och för tunga, långa eller breda transporter krävs dispens. Ska det grävas i gatan för ledningar söks schakttillstånd via e-tjänsten ISY Road, och ärendet går via ledningsägarens projektledare.",
     ],
     "aside": None},
    {"id": "berg-botkyrka", "h2": "Berg, sprängning och lägeskontroll",
     "paras": [
       "Står huset på berg kan grunden behöva sprängas fram. Det kräver tillstånd från polisen, som prövar om den som ska spränga är lämplig och har tillräcklig kunskap. Sprängfirman ska kontakta en besiktningsfirma som avgör vilka hus i närheten som ska besiktigas. Kommunen nämner en rekommendation om att hus inom 50 meter från sprängplatsen bör besiktigas, men vilka som blir aktuella beror på mark, grund och material.",
       "En geoteknisk undersökning fastställer jord-, berg- och grundvattenförhållanden, bland annat genom borrprover, och ger underlag för grundläggningen. När huset står på plats görs en lägeskontroll, en kontrollmätning av att det placerats enligt bygglovet, om startbeskedet kräver det. Den kan göras av kommunens enhet för geografisk information.",
       "Vill du hellre bygga ut det hus du har, läs om " + _L.format("tillbyggnad.html", "tillbyggnad") + " eller om " + _L.format("snickare-botkyrka.html", "snickare i Botkyrka") + " för mindre byggen på tomten. Hela arbetssättet beskrivs under " + _L.format("byggfirma.html", "byggfirma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett nytt hus i Botkyrka till",
  "steps": [
    ("Platsbesök", "Vi tittar på tomten, berget, gatan utanför och var utfarten kan ligga."),
    ("Ritningar och checklista", "Situationsplan, markplanering och ritningar tas fram efter kommunens checklista."),
    ("Skriftligt kostnadsförslag", "Mark, grund, byggnad och installationer redovisas som egna poster."),
    ("Bygglov och samråd", "Ansökan, utfartsansökan och tekniskt samråd före startbeskedet."),
    ("Arbetsplats och bygge", "APD-plan, transporter och eventuell sprängning planeras innan bygget börjar."),
    ("Lägeskontroll och slutbesked", "Kontrollmätning, slutsamråd och genomgång med dig."),
  ],
  "rot_h2": "Rotavdrag – nytt hus eller tillbyggnad i Botkyrka",
  "rot": [
    "Ett helt nytt hus ger inget rotavdrag. En tillbyggnad på ett befintligt hus kan göra det, om den sitter ihop med ytterväggen till minst 75 procent på någon sida eller har en dörr emellan, och sprängarbete som krävs för en utbyggnad räknas också. Är huset yngre än fem år ger ombyggnad och tillbyggnad inget avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material, resor och bygglovshandlingar ger inget avdrag. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Botkyrka?",
  "price": [
    "Berg och markförhållanden, grundläggning, husets storlek och installationer väger tyngst. Utfarten på allmän plats och schakt i gatan debiteras av kommunen och ingår inte i vår offert. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur bred får utfarten vara där den korsar gångbanan i Botkyrka?",
     "Högst 3,0 meter på den del som ligger på allmän plats, och den ska anpassas till befintliga marknivåer. Parkering är inte tillåten på den delen."),
    ("Får vi bygga infarten till vår nya villa själva i Botkyrka?",
     "Som regel bygger kommunens upphandlade entreprenör delen på allmän plats. Vid enklare förutsättningar kan fastighetsägaren få göra det i samråd med gatuingenjören, som godkänner arbetet vid en slutbesiktning."),
    ("Vem ska få APD-planen för bygget i Botkyrka?",
     "Enligt kommunen ska arbetsplatsdispositionsplanen även lämnas till Södertörns brandförsvarsförbund."),
    ("Vilka grannhus ska besiktigas innan vi spränger för grunden?",
     "Det avgör besiktningsfirman som sprängfirman anlitar. Kommunen nämner en rekommendation om att hus inom 50 meter bör besiktigas, men det beror på mark, grund och material."),
    ("Vad är en lägeskontroll vid ett nybygge i Botkyrka?",
     "En kontrollmätning av att huset har placerats enligt bygglovet. Om den krävs anges det i startbeskedet, och den kan göras av kommunens enhet för geografisk information."),
  ],
  "sources": [
    _SCB,
    ("Botkyrka kommun – Sök bygglov för nybyggnad en- och tvåbostadshus",
     _BO + "sa-soker-du-bygglov/bygglov-eller-anmalan/forandringar-som-kraver-bygglov/sok-bygglov-for-nybyggnad-en--och-tvabostadshus"),
    ("Botkyrka kommun – Bygga in- och utfart", _BO + "ovriga-byggrelaterade-tillstand/bygga-in--och-utfart"),
    ("Botkyrka kommun – APD-plan", _BO + "sa-soker-du-bygglov/bygglov-a-o/apd-plan"),
    ("Botkyrka kommun – Tillstånd för tunga, långa och breda fordon", _BO + "ovriga-byggrelaterade-tillstand/ansok-om-tillstand-for-tunga-langa-och-breda-fordon"),
    ("Botkyrka kommun – Tillstånd för schakt och trafikanordning", _BO + "ovriga-byggrelaterade-tillstand/schaktning"),
    ("Botkyrka kommun – Sprängning", _BO + "sa-soker-du-bygglov/bygglov-a-o/sprangning"),
    ("Botkyrka kommun – Lägeskontroll", _BO + "sa-soker-du-bygglov/bygglov-a-o/lageskontroll"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Planerar ni ett nytt hus i Botkyrka?", "Boka ett gratis platsbesök, så går vi igenom tomten, utfarten och vägen till slutbesked."),
  "img": [
    ("Nybyggd vit villa vid en lugn villagata i Botkyrka",
     "newly built Swedish two-storey villa with white wooden panel and dark grey metal roof on a suburban plot, a new single driveway with grey concrete pavers meeting a quiet residential street with a lowered kerb, low hedge, young trees, older villas in the background, Tullinge Botkyrka, summer daylight, empty scene"),
    ("Byggarbetsplats med bod, container och upplag vid ett nytt hus",
     "tidy Swedish residential building site on a villa plot: a small white site hut, a steel skip container, stacked timber under a tarpaulin, a fire extinguisher on a stand and a fenced material storage area, a timber-framed house under construction behind, granite outcrop, overcast daylight, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VALLENTUNA
"byggforetag-vallentuna.html": {
  "kind": "district", "service": "byggforetag", "ort": "Vallentuna", "svc_label": "Byggföretag",
  "title": "Byggföretag i Vallentuna – ritningar, grannar och tomtgräns",
  "description": "Byggföretag i Vallentuna: vad situationsplan och ritningar ska visa, när grannarna hörs, marklov och vad som gäller för kommunens mark intill tomten.",
  "h1": "Byggföretag i Vallentuna",
  "lead": "Vallentuna har 9 300 bostäder i småhus enligt SCB:s statistik för 2025, och omkring 8 000 av kommunens invånare bor på landsbygden och i de mindre orterna som Lindholmen, Karby, Brottby, Kårsta, Ekskogen och Frösunda. Oavsett var huset står går ett byggprojekt fortare när ritningarna är kompletta från början och tomtens gränser mot grannar och kommunal mark är utredda. Geal Entreprenad AB tar hand om tillbyggnader, nya hus och större ombyggnader som total entreprenad.",
  "card": "Ritningar, grannar och kommunens mark.",
  "sections": [
    {"id": "situationsplan-vallentuna", "anchor": "Situationsplanen",
     "h2": "Situationsplanen visar mer än huset",
     "paras": [
       "Vallentuna kommun vill att situationsplanen görs på en nybyggnadskarta som beställs från kommunens kart- och mätavdelning. Den ska visa befintliga och planerade markhöjder mot grannar och väg, stödmurar och slänter, hur infarten ansluter till gatan med plushöjder, parkering, vilka byggnader som ska bevaras eller rivas, nybyggnadens alla yttermått och minst tre mått till fastighetsgränsen.",
       "Utanför kommunalt VA-område ska planen också visa var enskilt avlopp och brunn ska ligga. Dessutom ska tillgängligheten till byggnaderna och plats för utevistelse och avfallshantering redovisas, antingen på situationsplanen eller på en markplaneringsritning.",
       "Kommunen påpekar att dagvattnet ska tas om hand på den egna fastigheten. Normalt innebär det att ny och befintlig marknivå möts ungefär 0,5 meter från tomtgränsen, så att det finns plats för ett dike eller dränering. Ändras marken ska både den befintliga linjen, streckad, och den nya, heldragen, ritas ut ända till gränsen.",
     ],
     "aside": {"title": "På situationsplanen", "items": [
       "Markhöjder mot grannar och väg",
       "Minst tre mått till gränsen",
       "Avlopp och brunn utanför VA-område",
       "Plats för avfall och utevistelse"]}},
    {"id": "ritningar-vallentuna", "h2": "Plan, fasad och sektion",
     "paras": [
       "Planritningen ska visa rummen och deras funktion, väggtjocklekar, fönster, dörrar och trappor, fast inredning som kök, tvätt, wc och dusch, möblering, mått och bruttoarea och boarea för varje plan. I en bostad ska entréplanet enligt kommunen minst rymma hygienrum, en avskiljbar sovplats, matlagning, plats för måltider och sittgrupp samt förvaring och tvätt. För små bostäder på högst 35 kvadratmeter gäller andra regler.",
       "Fasadritningen ska visa takvinklar, fönster, dörrar och skärmtak, blivande och befintlig marknivå fram till tomtgränsen och material och färgsättning. Vid en tillbyggnad ska nytt och befintligt redovisas, och det nya markeras. En sektionsritning krävs vid ny- och tillbyggnad och när konstruktionen påverkas. Den ska visa rumshöjder, golvhöjder på alla plan, bjälklagen med isolering och takvinklar.",
       "Är ansökan komplett får du oftast beslut inom tio veckor. I mer komplicerade fall kan tiden förlängas, men med högst tio veckor. Därför går vi igenom kommunens lista punkt för punkt innan något lämnas in.",
     ],
     "aside": None},
    {"id": "grannar-vallentuna", "h2": "När grannarna hörs – och när de inte gör det",
     "paras": [
       "Grannar får yttra sig om fastigheten ligger inom detaljplan och åtgärden avviker från planen, om den avviker från områdesbestämmelser eller om fastigheten ligger utanför detaljplan och områdesbestämmelser. Utanför plan gäller ett undantag för komplementbyggnader, mindre tillbyggnader och fasadändringar till en- och tvåbostadshus. Vid enskilt avlopp och bergvärme är det kommunens miljöavdelning som bedömer vilka grannar som ska höras.",
       "Följer bygget detaljplanen finns inget krav på att grannarna hörs innan lovet beviljas, och kommunen behöver inte kontakta grannar vid lovfria åtgärder. Efter ett beslut informeras grannarna och beslutet kungörs på kommunens anslagstavla. Den som vill överklaga har normalt tre veckor från att ha tagit del av beslutet, eller fyra veckor från kungörelsen om man inte delgetts. Överklagandet prövas av Länsstyrelsen Stockholm.",
     ],
     "aside": {"title": "Grannyttrande i Vallentuna", "items": [
       "Avvikelse från detaljplan",
       "Bygge utanför plan, med undantag",
       "Tre eller fyra veckor att överklaga"]}},
    {"id": "kommunmark-vallentuna", "h2": "Kommunens mark bredvid tomten",
     "paras": [
       "Ibland visar sig ett staket, en studsmatta eller till och med en byggnad stå på kommunens mark. Kommunen kallar det markannektering, och upptäcks det måste fastighetsägaren ta bort sina saker, även om utökningen funnits länge. Kommunen skriver att den mycket sällan säljer tillskottsmark till privata bostadstomter, eftersom marken oftast är allmän plats i detaljplanen. Då krävs en ändring av planen, och den som vill pröva det kan ansöka om planbesked.",
       "En begäran om planbesked ska vara skriftlig, beskriva vad du vill göra och innehålla en karta. Normalt kommer beskedet inom fyra månader. Det är inte bindande och kan inte överklagas, och den som ansöker betalar handläggningen.",
       "Under ett bygge kan kommunen tillfälligt upplåta mark, till exempel för en container, och i flera fall krävs dessutom polistillstånd. Inom detaljplan krävs marklov för schakt och fyllning som ändrar höjden mer än 0,5 meter. Om mindre byggen på tomten, se " + _L.format("snickare-vallentuna.html", "snickare i Vallentuna") + ", om taket " + _L.format("takrenovering-vallentuna.html", "takrenovering i Vallentuna") + " och om arbetssättet under " + _L.format("byggfirma.html", "byggfirma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett byggprojekt i Vallentuna till",
  "steps": [
    ("Platsbesök", "Vi tittar på huset, tomtens höjder och var gränserna mot grannar och kommunal mark går."),
    ("Nybyggnadskarta och plan", "Karta beställs och detaljplan eller områdesbestämmelser kontrolleras."),
    ("Skriftligt kostnadsförslag", "Byggdelar, mark och ROT-berättigat arbete redovisas var för sig."),
    ("Komplett ansökan", "Situationsplan, plan, fasad och sektion tas fram efter kommunens lista."),
    ("Bygget", "Vi samordnar alla hantverkare och sköter kontakten med kommunen under bygget."),
    ("Slutgenomgång", "Resultatet gås igenom med dig och handlingarna lämnas över."),
  ],
  "rot_h2": "Rotavdrag för bygge i Vallentuna",
  "rot": [
    "En tillbyggnad på ett befintligt hus ger rotavdrag om den sitter ihop med ytterväggen till minst 75 procent på någon sida eller har en dörr emellan. Ett helt nytt hus, ett garage eller en annan fristående byggnad ger inget avdrag, och inte heller ritningar och bygglovshandlingar.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Du ska äga bostaden när arbetet görs, och material och resor räknas inte. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Vallentuna?",
  "price": [
    "Storlek, grundläggning och hur mycket marken ska ändras styr mest, liksom om avlopp och brunn ska ordnas på tomten. Kommunens avgifter för kartor och lov tillkommer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur många mått till tomtgränsen ska situationsplanen ha i Vallentuna?",
     "Minst tre mått från nybyggnaden till fastighetsgränsen, enligt kommunen. Situationsplanen görs på en nybyggnadskarta från kart- och mätavdelningen."),
    ("Varför ska marknivåerna mötas en halvmeter från tomtgränsen?",
     "Vallentuna kommun skriver att dagvattnet ska tas om hand på den egna fastigheten, och att det normalt kräver plats för ett dike eller dränering ungefär 0,5 meter från gränsen."),
    ("Kan vi köpa till en remsa kommunal mark till vår tomt i Vallentuna?",
     "Det är ovanligt. Kommunen säljer mycket sällan tillskottsmark till bostadstomter, eftersom marken oftast är allmän plats i detaljplanen. Det kräver en planändring, och planbesked kan sökas."),
    ("Hur lång tid tar ett planbesked i Vallentuna?",
     "Normalt fyra månader från en komplett begäran. Beskedet är inte bindande och kan inte överklagas."),
    ("Får vi ställa en container på kommunens mark under bygget i Vallentuna?",
     "Kommunen kan upplåta mark tillfälligt, till exempel för en container under ett byggarbete. I flera fall krävs också polistillstånd enligt ordningslagen."),
  ],
  "sources": [
    _SCB,
    ("Vallentuna kommun – Det ska din ansökan eller anmälan innehålla", _VA + "bygglov-och-anmalan/det-ska-din-ansokan-anmalan-innehalla"),
    ("Vallentuna kommun – Marklov och rivningslov", _VA + "bygglov-och-anmalan/marklov-och-rivningslov"),
    ("Vallentuna kommun – Ditt ansvar som granne", _VA + "bostad-tomter-och-fastighetsagare/ditt-ansvar-som-granne"),
    ("Vallentuna kommun – Lediga tomter till småhus", _VA + "bostad-tomter-och-fastighetsagare/lediga-tomter-till-smahus"),
    ("Vallentuna kommun – Planbesked, ansökan", _VA + "planarbete-och-kartor/planbesked---ansokan"),
    ("Vallentuna kommun – Landsbygd", _VA + "planarbete-och-kartor/landsbygd"),
    _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ni bygga i Vallentuna?", "Boka ett gratis platsbesök, så går vi igenom tomten, ritningarna och grannfrågorna."),
  "img": [
    ("Gul enplansvilla med tegeltak mellan åkrar och lövträd i Vallentuna",
     "1980s Swedish one-storey villa with light yellow wooden panel and red concrete tile roof with a new matching timber extension, gently sloping lawn with a shallow grassed drainage swale along the plot boundary, open fields and a small birch grove in the background, Vallentuna, late summer daylight, empty scene"),
    ("Träpålar med snören och ett dike längs tomtgränsen bredvid en villa",
     "wooden survey stakes with taut orange string lines marking out the footprint of a planned extension on a lawn next to the plinth of a light Swedish wooden villa, a small grassed drainage ditch along a low hedge at the plot boundary, open farmland in the distance, Vallentuna, soft daylight, empty scene"),
  ],
  "related": [],
},

}
