# -*- coding: utf-8 -*-
"""Byggföretag – ortsidor v8: Danderyd, Sollentuna, Järfälla, Haninge, Värmdö, Tyresö (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
Riksdagen (plan- och bygglagen 9 kap. 10 och 17 §§, 10 kap. 3, 4, 5 och 26 §§; arbetsmiljölagen 3 kap. 6 och
7 c §§), Skatteverket (Så fungerar rotavdraget; Ger arbetet rätt till rotavdrag? – tillbyggnad 75 procent,
fristående byggnad, bygglovshandlingar, hus yngre än fem år), Boverket (Strandskydd; Energiguiden: När du ska
anlita ett företag), Danderyds kommun (Nya regler för bygglov från 1 december 2025 med frågor och svar;
Riktlinjer för kulturhistoriska byggnader och miljöer i Danderyd 2024), Sollentuna kommun (Tillbyggnad en- eller
tvåbostadshus; Översiktsplan med sikte på 2040), Järfälla kommun (Bygglovsbefriade åtgärder; tjänsteskrivelse
Planuppdrag för Hjälmvägen 13A och 13C, Skälby, 2020), Haninge kommun (Omvandlingsområden, webbsida och folder),
Värmdö kommun (Förändringar i PBL från 1 december 2025; broschyren Fritidshusområde i förändring, del 1
Planering, 2023) och Tyresö kommun (Förändringar i PBL från 1 december 2025; Tillsyn enligt PBL; Mätuppdrag och
kartor; Avstyckning och servitut; Översvämningsrisker och åtgärder).
Strukna (ej verifierade eller medvetet utelämnade): kommunala avgifter och taxor i kronor (bygglovsavgift,
planavgift, handläggningstid), kontrollansvarig och byggbedömare (lagändring 2026:712 – oklart vilka regler som
gäller för villor vid publicering), utökat strandskydd för enskilda områden på Värmdö, vilka PFO-områden som är
planlagda i dag, Järfällas nya översiktsplan 2050 (bara granskningsskede), Tyresö-specifika regler för
sprängning, ABS 18 och konsumenttjänstlagens 15-procentsregel (ingen primärkälla öppnad).
Inga priser, garantier, omdömen, egna uppdrag eller cert. Schema: se tools/tj_check.py."""

_L = '<a class="text-link" href="{0}">{1}</a>'

# ------------------------------------------------------------------ gemensamma källor
_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 9 kap. 10 och 17 §§ samt 10 kap. 3–5 och 26 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_AML = ("Riksdagen – Arbetsmiljölag (1977:1160), 3 kap. 6 och 7 c §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arbetsmiljolag-19771160_sfs-1977-1160/")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV_JOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_BV_AVTAL = ("Boverket – Energiguiden: När du ska anlita ett företag",
             "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/6.upphandling")
_BV_STRAND = ("Boverket – Strandskydd",
              "https://www.boverket.se/sv/samhallsplanering/sa-planeras-sverige/planeringsfragor/strandskydd/")

PAGES_TJ = {

# ------------------------------------------------------------------ DANDERYD
"byggforetag-danderyd.html": {
  "kind": "district", "service": "byggforetag", "ort": "Danderyd", "svc_label": "Byggföretag",
  "title": "Byggföretag i Danderyd – tillbyggnad, tomt och riktlinjer",
  "description": "Byggföretag i Danderyd: tillbyggnad och nybyggnad på villatomten med kommunens riktlinjer från 2024, fornlämningar, grannmedgivande och lovplikt.",
  "h1": "Byggföretag i Danderyd",
  "lead": "Att bygga till eller bygga nytt på en tomt i Danderyd handlar lika mycket om tomten som om huset. Kommunens riktlinjer för kulturmiljön från 2024 säger något om var garaget får stå, hur mycket marken får sprängas och om stora tomter bör delas. Geal Entreprenad AB tar hand om byggprojektet som total entreprenad, från första skissen till slutbesiktning, och första steget är att läsa vad som gäller för just din fastighet.",
  "card": "Tillbyggnad, tomt och kommunens riktlinjer.",
  "sections": [
    {"id": "riktlinjer-danderyd", "anchor": "Riktlinjerna",
     "h2": "Riktlinjerna från 2024 styr det som byggs till",
     "paras": [
       "Danderyds kommun har tagit fram riktlinjer för kulturhistoriska byggnader och miljöer. Enligt dokumentet ska de användas som vägledning när plan- och lovärenden bedöms, och de riktar sig samtidigt till fastighetsägarna. Riktlinjerna är indelade efter kommundelarna Enebyberg, Danderyd, Djursholm och Stocksund och därefter efter utpekade områden, och för nästan varje område finns ett eget stycke om ny- och tillbyggnad.",
       "Budskapet är ofta detsamma: vid en tillbyggnad ska man utgå från den omgivande bebyggelsen när det gäller husens placering på tomten, utformning och volymverkan. För flera områden står det också att garage och carport inte bör placeras mot gatan. I grupphusområdena ska nya tillägg utformas med stor hänsyn till miljöns kulturhistoriska värden, och i området som kallas Det moderna Danderyd bör fasaduttryck som inte hör till 1950- och 1960-talens stilideal undvikas.",
       "För oss betyder det att skissen börjar med gatan och grannhusen, inte med planlösningen. En " + _L.format("tillbyggnad.html", "tillbyggnad") + " som ligger rätt på tomten och har rätt volym är lättare att få igenom och passar bättre in.",
     ],
     "aside": {"title": "Ur riktlinjerna", "items": [
       "Utgå från grannhusens placering och volym",
       "Garage och carport inte mot gatan",
       "Minimera sprängning, fyllning och schaktning",
       "Undvik att stycka av äldre villatomter"]}},
    {"id": "mark-danderyd", "h2": "Mark, träd och fornlämningar",
     "paras": [
       "Riktlinjerna lägger stor vikt vid trädgården. Äldre träd och buskar, staket, murar och stenlagda gångar kan enligt kommunen ha ett högt kulturhistoriskt värde. I många områden ska markarbeten i form av sprängning, fyllning och schaktning minimeras, och utfyllnad med stödmurar och hårdgjorda ytor undvikas. Ett nytt hus eller en ny flygel bör alltså anpassas efter terrängen snarare än tvärtom.",
       "Riktlinjerna påminner också om fornlämningar. Ska du göra ingrepp i marken eller en tillbyggnad på tomten är det ditt ansvar att ta reda på om det finns fornlämningar i området, och byggherren har skyldighet att undersöka det. Vid frågor, eller om något upptäcks på platsen, är det länsstyrelsens kulturmiljöenhet i Stockholm som ska kontaktas.",
       "Om större villatomter säger dokumentet att äldre villatomter med ursprunglig storlek inte bör styckas av, och att ny bebyggelse ska anpassas till omgivningen i volym, utformning och placering. Den som funderar på att dela tomten och bygga ett nytt hus bör därför räkna med att frågan prövas mot kulturmiljön.",
     ],
     "aside": None},
    {"id": "lov-danderyd", "h2": "30 kvadratmeter utan lov – och när lov ändå krävs",
     "paras": [
       "Sedan den 1 december 2025 får ett en- eller tvåbostadshus byggas till utan bygglov, så länge tillbyggnaden inte går över taknocken och alla lovfria tillbyggnader på huset tillsammans är högst 30,0 kvadratmeter. Danderyds kommun påpekar att tidigare skärmtak och attefallstillbyggnader räknas in. Ligger fastigheten i ett kulturhistoriskt särskilt värdefullt område, eller är byggnaden särskilt värdefull, krävs alltid bygglov. Det framgår av kommunens kulturmiljökarta.",
       "Lovfria tillbyggnader och komplementbyggnader ska ligga minst 4,5 meter från tomtgränsen. Närmare än så krävs skriftligt medgivande från alla berörda grannar, och kommunen påpekar att detaljplanen ibland ändå hindrar en placering nära gränsen. Mot gata, park eller naturmark kan kommunen själv lämna medgivande, och då ska en måttsatt situationsplan skickas in.",
       "En detalj som är lätt att missa: för åtgärder som inte kräver bygglov men som ökar bruttoarean på fastigheten ansvarar fastighetsägaren för att informera kommunens VA-enhet. Berörs husets konstruktion krävs dessutom anmälan och startbesked innan bygget börjar.",
     ],
     "aside": {"title": "Före första spadtaget", "items": [
       "Kulturmiljökartan och detaljplanen",
       "Skriftliga grannmedgivanden",
       "Besked till VA-enheten om bruttoarean ökar",
       "Anmälan om konstruktionen berörs"]}},
    {"id": "helhet-danderyd", "h2": "Ett byggföretag för hela projektet",
     "paras": [
       "Många projekt i Danderyd blir mer än en tillbyggnad. Ett nytt kök i den nya delen, ett badrum på övervåningen eller en ny takfot som ska mötas med den gamla. Vi samordnar snickare, plattsättare, målare och behöriga installatörer för el och VVS, så att du har en kontakt och ett skriftligt avtal. Läs mer om arbetssättet under " + _L.format("byggfirma.html", "byggfirma i Stockholm") + ".",
       "Ska taket på den befintliga delen ses över i samma veva är det klokt att planera det tillsammans med tillbyggnaden. Se " + _L.format("takbyte-danderyd.html", "takbyte i Danderyd") + " för vad kommunen säger om takmaterial.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett byggprojekt i Danderyd till",
  "steps": [
    ("Platsbesök", "Vi går igenom huset, tomten, träden och terrängen och vad du vill bygga."),
    ("Kartan och riktlinjerna", "Kulturmiljökartan, detaljplanen och riktlinjerna för ditt område kontrolleras."),
    ("Skiss och kostnadsförslag", "Du får ett skriftligt kostnadsförslag där ROT-berättigat arbete anges separat."),
    ("Medgivanden och lov", "Grannmedgivanden, bygglov eller anmälan tas fram där det behövs."),
    ("Bygget", "Grund, stomme, tak och installationer samordnas av oss."),
    ("Slutgenomgång", "Vi går igenom resultatet med dig och lämnar över handlingarna."),
  ],
  "rot_h2": "ROT-avdrag när du bygger i Danderyd",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material och resor ger inget avdrag.",
    "En tillbyggnad kan ge avdrag om någon av dess sidor sitter ihop med husets yttervägg till minst 75 procent, eller om det finns en dörr mellan tillbyggnaden och huset. Ett nytt fristående hus eller garage ger inget avdrag, och inte heller bygglovshandlingar eller arkitekt. Vi drar avdraget direkt på fakturan där det gäller.",
  ],
  "price_h2": "Vad påverkar kostnaden i Danderyd?",
  "price": [
    "Storleken, hur grunden kan anpassas till terrängen utan stora markarbeten, hur den nya delen ska anslutas till det befintliga huset och om materialval och utformning styrs av riktlinjerna för området. Installationer för kök eller badrum i den nya delen tillkommer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi placera ett nytt garage mot gatan på vår tomt i Djursholm?",
     "Kommunens riktlinjer för kulturmiljön säger för flera områden att garage och carport inte bör placeras mot gatan. Kontrollera också detaljplanen och om fastigheten ligger i ett särskilt värdefullt område, där bygglov alltid krävs."),
    ("Vem ansvarar för att undersöka fornlämningar när vi bygger till i Danderyd?",
     "Byggherren, det vill säga du som fastighetsägare. Kommunen hänvisar frågor och fynd till länsstyrelsens kulturmiljöenhet i Stockholm."),
    ("Kan kommunen ge medgivande när tillbyggnaden hamnar nära gatan?",
     "Ja, i vissa fall. Danderyds kommun kan lämna medgivande för placering närmare än 4,5 meter mot gata, park eller naturmark, om placeringen inte försämrar sikt, trafiksäkerhet eller kommunens skötsel."),
    ("Måste vi meddela VA-enheten om en lovfri tillbyggnad?",
     "Ja. Ökar åtgärden bruttoarean på fastigheten ansvarar fastighetsägaren enligt kommunen för att informera VA-enheten, även om bygglov inte krävs."),
    ("Går det att stycka av en stor villatomt i Danderyd?",
     "Det prövas i det enskilda fallet, men kommunens riktlinjer säger att äldre villatomter med ursprunglig storlek inte bör styckas av i de utpekade miljöerna."),
  ],
  "sources": [
    ("Danderyds kommun – Nya regler för bygglov från 1 december 2025",
     "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/"),
    ("Danderyds kommun – Riktlinjer för kulturhistoriska byggnader och miljöer i Danderyd (2024, pdf)",
     "https://www.danderyd.se/globalassets/globala-filer/kommun-och-politik/ovriga-styrdokument-ny/styrande-dokument---samhallsbyggnad-miljo-och-exploatering/riktlinjer-for-kulturmiljohistoriska-byggnader-och-miljoer-i-danderyd-2024.pdf"),
    _PBL, _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ni bygga till eller bygga nytt i Danderyd?", "Boka ett gratis platsbesök, så går vi igenom tomten, huset och riktlinjerna."),
  "img": [
    ("Stor ljus villa i Danderyd med en lägre tillbyggnad mot trädgården och höga ekar",
     "large 1920s Swedish light plastered villa with a steep red clay tile roof and a newer lower single-storey wing facing the garden with matching roof pitch and white wooden windows, mature oak trees, lawn, gravel path, Djursholm Danderyd, calm daylight, empty scene"),
    ("Grusgång, stenmur och gamla fruktträd i en trädgård vid en äldre villa",
     "old Swedish villa garden with a low dry stone wall, a gravel path, old apple trees and a white wooden picket fence, corner of a plastered house visible, soft daylight, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SOLLENTUNA
"byggforetag-sollentuna.html": {
  "kind": "district", "service": "byggforetag", "ort": "Sollentuna", "svc_label": "Byggföretag",
  "title": "Byggföretag i Sollentuna – tillbyggnad, tomtdelning och lov",
  "description": "Byggföretag i Sollentuna: tillbyggnad nära järnvägen, minsta tomtstorlek i villastäderna, handlingar till bygglovet och översiktsplanens syn på förtätning.",
  "h1": "Byggföretag i Sollentuna",
  "lead": "Sollentunas villastäder är gamla och lummiga, och kommunen vill att de ska förbli det. Det märks när du vill dela tomten, bygga ett hus till eller bygga ut det du har. Geal Entreprenad AB driver byggprojekt i Sollentuna som total entreprenad, med en kontakt från skiss till slutbesiktning, och vi börjar med vad detaljplanen och översiktsplanen säger om just din tomt.",
  "card": "Tillbyggnad, tomtdelning och lov.",
  "sections": [
    {"id": "villastad", "anchor": "Villastäderna",
     "h2": "Översiktsplanen vill bevara villaområdenas karaktär",
     "paras": [
       "I Översiktsplan för Sollentuna med sikte på 2040 skriver kommunen att även de äldre villaområdena påverkas av ett förändringstryck när marken blir mer begränsad. Många områden har stora tomter som bidrar till grönstrukturen och till att dagvattnet kan tas om hand. Villastadsdelarna växte fram under 1900-talets första hälft, och planen beskriver deras struktur som robust trots senare avstyckningar och förtätningar, men konstaterar att den gröna lummigheten kan förstöras av alltför stark förtätning.",
       "Planen säger också att enbostadstraditionen bör vara norm i villaområdena. Fler bostäder i ett hus ger fler bilplatser och ibland fler lovfria tillägg på tomten, och det kan enligt kommunen påverka lummigheten negativt.",
       "Alla delar av kommunen ser inte ut så. I Sjöberg styckades de första villatomterna av redan på 1920-talet, men området präglades av skog och fritidshus fram till 1960-talet, och den stora utbyggnaden skedde under 1970-, 80- och 90-talen.",
     ],
     "aside": {"title": "Översiktsplanen i korthet", "items": [
       "Enbostadshus som norm i villaområdena",
       "Nya tomter under 800 m² bör inte tillkomma generellt",
       "1 000 m² i kulturmiljöplanens villaområden",
       "Ingen avstyckning i Norrvikens villastad"]}},
    {"id": "tomtdelning", "h2": "Att dela tomten och bygga ett hus till",
     "paras": [
       "Översiktsplanen är tydlig om tomtstorlekar. Tomter under 800 kvadratmeter, räknat utan skaft, bör inte tillkomma generellt. För villaområden som omfattas av kulturmiljöplanen är riktlinjen 1 000 kvadratmeter, utom där gällande detaljplan anger 800. Avstyckningar och förtätningar ska inte tillåtas i Norrvikens villastad, Väderholmen, Skansen och andra områden där kulturmiljöplanen anger att karaktären ska behållas. I Edsvikens villastad bör de bara tillåtas där det går utan att gatumiljöns karaktär förändras.",
       "Beslut som möjliggör förtätning ska enligt planen ta hänsyn till fastighetens storlek och form, terrängen, befintlig växtlighet, var husen placeras och hur stor del av tomten som blir kvar som grönyta för dagvatten. Planen nämner särskilt placeringen av huvudbyggnad, garage, biluppställning och utfart.",
       "Innan vi ritar ett nytt hus på en delad tomt går vi därför igenom detaljplanen och om området finns med i kulturmiljöplanen. Ibland är en tillbyggnad eller ett " + _L.format("attefallshus.html", "attefallshus") + " ett bättre sätt att få mer yta på samma tomt.",
     ],
     "aside": None},
    {"id": "jarnvag", "h2": "Lovfri tillbyggnad – men inte nära spåret",
     "paras": [
       "Sollentuna kommun beskriver en tillbyggnad som varje åtgärd som ökar byggnadens volym, uppåt, åt sidan eller nedåt. Ett en- eller tvåbostadshus får byggas till utan bygglov med sammanlagt högst 30,0 kvadratmeter, om tillbyggnaden inte går över taknocken. Tidigare attefallstillbyggnader, lovfria takkupor och skärmtak räknas in i de 30 kvadratmeterna.",
       "Bygglov krävs om tillbyggnaden hamnar närmare tomtgränsen än 4,5 meter utan grannens skriftliga medgivande, om fastigheten eller huset är kulturhistoriskt värdefullt och, något som berör många i Sollentuna, om den placeras närmare än 30,0 meter från mitten av ett järnvägsspår utan att infrastrukturförvaltaren skriftligen har medgett det. Bor du i radhus eller kedjehus beror möjligheterna på hur husen är byggda ihop, och kommunen hänvisar då till sin vägledning.",
       "Lovfria tillbyggnader får strida mot detaljplanen. Bygger du ett nytt en- eller tvåbostadshus och vill göra en sådan tillbyggnad samtidigt, ska den ingå i bygglovsansökan för det nya huset. Anmälan krävs om tillbyggnaden innebär ingrepp i bärande konstruktion, nya installationer för ventilation, vatten och avlopp eller eldstad, eller om brandskyddet påverkas.",
     ],
     "aside": {"title": "Lov krävs ändå", "items": [
       "Över 30 m² sammanlagt eller över taknocken",
       "Närmare gränsen än 4,5 m utan medgivande",
       "Inom 30 m från järnvägsspårets mitt",
       "Kulturhistoriskt värdefull fastighet"]}},
    {"id": "handlingar", "h2": "Handlingarna till ett bygglov i Sollentuna",
     "paras": [
       "När tillbyggnaden kräver lov ska ansökan enligt kommunen innehålla ett förslag till kontrollplan, en situationsplan på tomtkarta och ritningar i form av plan, fasad och sektion. För enklare åtgärder kan situationsplanen göras på en tomtkarta i skala 1:400. Äldre ritningar på huset kan sökas fram utan kostnad i kommunens bygglovsarkiv, och de är en bra grund för de nya.",
       "Vi tar fram underlaget, skissar tillbyggnaden mot de gamla ritningarna och samordnar sedan bygget med behöriga installatörer för el och VVS. Ska den nya delen få ett eget badrum, läs mer under " + _L.format("badrumsrenovering-sollentuna.html", "badrumsrenovering i Sollentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett byggprojekt i Sollentuna till",
  "steps": [
    ("Platsbesök", "Vi ser huset, tomten och avståndet till grannar, gata och spår."),
    ("Planer och gamla ritningar", "Detaljplan, kulturmiljöplan och husets ritningar från bygglovsarkivet går vi igenom."),
    ("Kostnadsförslag", "Ett skriftligt förslag som skiljer på ROT-berättigat arbete och övrigt."),
    ("Ansökan eller anmälan", "Kontrollplan, situationsplan och ritningar tas fram när lov eller anmälan krävs."),
    ("Bygget", "Vi samordnar alla hantverkare och installatörer."),
    ("Slutgenomgång", "Resultatet gås igenom med dig och handlingarna lämnas över."),
  ],
  "rot_h2": "Rotavdrag för byggprojekt i Sollentuna",
  "rot": [
    "Du kan få rotavdrag med 30 procent av arbetskostnaden, högst 50 000 kronor per person och år. Rot och rut får tillsammans vara högst 75 000 kronor. Du ska äga bostaden när arbetet görs, och material och resor räknas inte.",
    "En tillbyggnad ger avdrag om den sitter ihop med husets yttervägg till minst 75 procent av någon sida, eller om det finns en dörr mellan tillbyggnaden och huset. Ett helt nytt hus på en avstyckad tomt ger aldrig rotavdrag. Är huset yngre än fem år får arbetet bara återställa det till ursprungligt skick. Avdraget dras direkt på vår faktura.",
  ],
  "price_h2": "Vad styr kostnaden i Sollentuna?",
  "price": [
    "Tillbyggnadens storlek och grundläggning, hur den ansluts till huset, om bygglov och kontrollplan behövs och vilka installationer den nya delen ska ha. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga till lovfritt när huset ligger nära järnvägen i Sollentuna?",
     "Inte om tillbyggnaden hamnar närmare än 30,0 meter från mitten av spåret, såvida inte infrastrukturförvaltaren skriftligen har medgett det. Då krävs bygglov."),
    ("Hur liten får en avstyckad tomt vara i Sollentuna?",
     "Enligt översiktsplanen bör tomter under 800 kvadratmeter inte tillkomma generellt. I villaområden som ingår i kulturmiljöplanen är riktlinjen 1 000 kvadratmeter, om inte detaljplanen anger 800."),
    ("Kan vi stycka av tomten i Norrvikens villastad?",
     "Översiktsplanen säger att avstyckningar och förtätningar inte ska tillåtas i Norrvikens villastad, eftersom kulturmiljöplanen anger att karaktären ska behållas."),
    ("Räknas vår gamla takkupa in i de 30 kvadratmeterna?",
     "Ja. Sollentuna kommun skriver att tidigare lovfria takkupor, skärmtak och attefallstillbyggnader ska ingå i beräkningen av den totala arean per byggnad."),
    ("Var hittar vi ritningar på vårt hus inför en tillbyggnad?",
     "I Sollentuna kommuns bygglovsarkiv. Enligt kommunen kostar det ingenting att söka fram äldre ritningar där."),
  ],
  "sources": [
    ("Sollentuna kommun – Tillbyggnad en- eller tvåbostadshus",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/tillbyggnad-en--och-tvabostadshus/"),
    ("Sollentuna kommun – Översiktsplan för Sollentuna med sikte på 2040 (pdf)",
     "https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/oversiktsplan/oversiktsplan-for-sollentuna-med-sikte-pa-2040.pdf"),
    _PBL, _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Planerar ni att bygga i Sollentuna?", "Boka ett gratis platsbesök, så går vi igenom tomten, planerna och vad som är möjligt."),
  "img": [
    ("Äldre villa i Sollentuna med ny tillbyggnad i trä och lummig trädgård",
     "early 1900s Swedish two-storey wooden villa painted pale yellow with a new single-storey timber extension with large windows on the garden side, lush garden with lilac and apple trees, quiet villa street, Sollentuna, summer daylight, empty scene"),
    ("Villatomt med stora träd och gräsmatta mellan två äldre hus",
     "wide view of a large green Swedish villa plot with tall birch and pine trees and a lawn between two older wooden villas, low hedge towards the street, overcast soft light, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"byggforetag-jarfalla.html": {
  "kind": "district", "service": "byggforetag", "ort": "Järfälla", "svc_label": "Byggföretag",
  "title": "Byggföretag i Järfälla – planbesked, extra bostad och ansvar",
  "description": "Byggföretag i Järfälla: tillbyggnad, extra bostad i villan och nytt hus på tomten, planbesked i Skälby, lovfria regler och vem som har arbetsmiljöansvaret.",
  "h1": "Byggföretag i Järfälla",
  "lead": "I Järfälla handlar många byggfrågor om att få plats med fler: en extra bostad i villan, en tillbyggnad för en växande familj eller ett nytt hus på en del av tomten. Geal Entreprenad AB bygger i Järfälla som total entreprenad. Du har en kontakt, ett skriftligt avtal och vi tar ansvar för att delarna passar ihop.",
  "card": "Planbesked, extra bostad och ansvar.",
  "sections": [
    {"id": "skalby", "anchor": "Planbesked",
     "h2": "Skälby och den varsamma förtätningen",
     "paras": [
       "Järfällas gällande översiktsplan, Järfälla – nu till 2030, antogs 2014 och bedömdes som aktuell 2018. Där beskrivs Skälby som ett område med bibehållen karaktär, där en varsam förtätning är möjlig med bostäder som är anpassade till den befintliga bebyggelsen, till exempel med likartad utformning och likartad placering på tomten.",
       "Hur det kan gå till syns i ett planuppdrag från 2020 för två parhus vid Hjälmvägen i Skälby. Ägarna ville dela två fastigheter till fyra och begärde planbesked. Den gällande detaljplanen angav en minsta fastighetsstorlek på 850 kvadratmeter, att huvudbyggnaden inte fick vara större än 140 kvadratmeter och att garage och uthus fick vara högst 30 kvadratmeter. Kommunen påpekade att varje ny fastighet får egna lovfria åtgärder, vilket kan göra att mer av marken hårdgörs och att mer dagvatten rinner till grannarna.",
       "Av samma handling framgår att kommunen kan prioritera planärenden för privata bostadstomter där minst två fastighetsägare samordnar sig och begär planbesked tillsammans, och att kostnaden för detaljplanen bekostas av sökanden genom ett plankostnadsavtal.",
     ],
     "aside": {"title": "Innan tomten delas", "items": [
       "Läs detaljplanens minsta tomtstorlek",
       "Kolla högsta byggnadsarea per hus",
       "Planbesked om planen måste ändras",
       "Räkna med plankostnad och lantmäteri"]}},
    {"id": "extra-bostad", "h2": "En extra bostad i villan – lovfritt men inte regelfritt",
     "paras": [
       "Enligt plan- och bygglagen krävs inte bygglov för att inreda ytterligare en bostad i ett enbostadshus som inte är ett komplementbostadshus. Järfälla kommun räknar upp det bland de lovbefriade åtgärderna, tillsammans med tillbyggnad, komplementbostadshus och att ändra en komplementbyggnad till komplementbostadshus.",
       "Kommunen understryker att lovbefriade åtgärder fortfarande omfattas av Boverkets byggregler och kan kräva anmälan och startbesked, till exempel vid väsentliga ändringar av brandskydd, bärande konstruktion, vatten, avlopp och ventilation. En ny lägenhet i källaren eller på övervåningen innebär nästan alltid något av det.",
       "Ska du bygga ett nytt en- eller tvåbostadshus och samtidigt planera en lovfri tillbyggnad eller en extra bostad, ska de enligt kommunen tas med i bygglovsansökan för huset. Annars måste du vänta med dem tills huset har fått slutbesked.",
     ],
     "aside": None},
    {"id": "dokumentera", "h2": "Spara papperen och anlita rätt kompetens",
     "paras": [
       "Järfälla kommun ger två råd som passar varje byggprojekt. Det första är att dokumentera hur du uppfyller reglerna, till exempel för tillgänglighet och brandskydd, och att spara ritningar och skriftliga grannmedgivanden, eftersom kommunen inte längre arkiverar dem för lovbefriade åtgärder. Det andra är att se till att de du anlitar har rätt kompetens och kan verifiera de tekniska lösningarna, eftersom det är du som byggherre som har det juridiska ansvaret.",
       "Vi lämnar därför över ritningar, beskrivningar och dokumentation när bygget är klart, så att du har dem den dag huset ska säljas eller byggas om. Vill du ha ett formellt beslut kan du söka frivilligt bygglov, något kommunen beskriver som en trygghet inför en större investering.",
     ],
     "aside": {"title": "Det här sparar du", "items": [
       "Ritningar och beskrivningar",
       "Skriftliga grannmedgivanden",
       "Underlag för brandskydd och tillgänglighet",
       "Startbesked och slutbesked"]}},
    {"id": "arbetsmiljo-jarfalla", "h2": "Vem har arbetsmiljöansvaret på din tomt?",
     "paras": [
       "Enligt arbetsmiljölagen är den som låter utföra ett byggarbete byggherre och ska bland annat utse byggarbetsmiljösamordnare för planering och projektering och för utförandet. Anlitar du som privatperson ett företag som självständigt ansvarar för planeringen eller utförandet, och konsumenttjänstlagen gäller för uppdraget, ligger de skyldigheterna i stället på företaget vid arbetets utförande, om ni inte skriftligen har avtalat något annat.",
       "Det är en av fördelarna med en total entreprenad. Du köper hela projektet av ett företag, vi samordnar alla som arbetar på tomten och du slipper hålla ihop flera avtal. Läs mer om hur det fungerar på sidan om " + _L.format("byggfirma.html", "byggfirma i Stockholm") + ", eller om " + _L.format("villarenovering.html", "renovering av hela villan") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så driver vi ett byggprojekt i Järfälla",
  "steps": [
    ("Besök på tomten", "Vi går igenom huset, tomten och vad du vill åstadkomma."),
    ("Detaljplanen", "Tomtstorlek, byggrätt och om planbesked behövs kontrolleras först."),
    ("Kostnadsförslag", "Ett skriftligt förslag där det framgår vad som är ROT-arbete."),
    ("Lov eller anmälan", "Vi tar fram underlag för bygglov, anmälan eller frivilligt lov."),
    ("Bygget", "Vi samordnar stomme, tak, installationer och ytskikt."),
    ("Överlämning", "Du får dokumentationen och vi går igenom arbetet tillsammans."),
  ],
  "rot_h2": "ROT-avdrag för byggprojekt i Järfälla",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, med högst 50 000 kronor per person och år och högst 75 000 kronor inklusive rutavdrag. Material, resor och utrustning ger inget avdrag.",
    "Att riva väggar och göra om planlösningen när en extra bostad inreds kan ge avdrag. Ett helt nytt hus på en avstyckad tomt ger det aldrig, och inte heller ett garage, en friggebod eller annan fristående byggnad. En tillbyggnad ger avdrag om den sitter ihop med husets yttervägg till minst 75 procent av någon sida eller har en dörr in till huset. Vi drar avdraget på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Järfälla?",
  "price": [
    "Om projektet kräver ny detaljplan eller lantmäteriförrättning, hur mycket av huset som berörs när en extra bostad ska få eget kök, badrum och brandskydd, och hur en tillbyggnad grundläggs och ansluts. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för att göra en egen lägenhet i källaren på vår villa i Järfälla?",
     "Nej, att inreda ytterligare en bostad i ett enbostadshus är lovfritt enligt plan- och bygglagen. Men anmälan och startbesked krävs ofta, till exempel när brandskydd, ventilation eller vatten och avlopp ändras."),
    ("Kan vi dela vår tomt i Skälby och bygga ett hus till?",
     "Det beror på detaljplanens minsta fastighetsstorlek. Räcker inte tomten krävs en ny detaljplan, och då börjar det med en begäran om planbesked hos kommunen."),
    ("Varför ska vi spara grannens medgivande när tillbyggnaden är lovfri?",
     "Järfälla kommun arkiverar inte handlingar för lovbefriade åtgärder. Medgivandet och ritningarna är ditt bevis på att åtgärden följer reglerna."),
    ("Har vi arbetsmiljöansvaret när ett byggföretag bygger vår tillbyggnad?",
     "Om företaget självständigt ansvarar för utförandet och uppdraget är en konsumenttjänst, ligger byggherrens skyldigheter vid utförandet på företaget, om ni inte skriftligen har avtalat annat."),
    ("Kan vi vänta med en tillbyggnad tills vårt nya hus är klart?",
     "Ja, men om tillbyggnaden inte finns med i bygglovsansökan för det nya huset får den enligt Järfälla kommun inte göras förrän huset har fått slutbesked."),
  ],
  "sources": [
    ("Järfälla kommun – Bygglovsbefriade åtgärder",
     "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/bygglovsbefriadeatgarder.4.a41712119a05132defe8bb3.html"),
    ("Järfälla kommun – Tjänsteskrivelse: Planuppdrag för Hjälmvägen 13A och 13C, Skälby (2020, pdf)",
     "https://www.jarfalla.se/download/18.55b0b91b174b4fde71d231ed/1601039819229/del-av-hjalmvagen-tjansteskrivelse.pdf"),
    _PBL, _AML, _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Vill ni bygga till eller bygga om i Järfälla?", "Boka ett gratis platsbesök, så går vi igenom huset, tomten och detaljplanen."),
  "img": [
    ("Parhus i Järfälla med trädgård och skaftväg mellan husen",
     "Swedish 1980s semi-detached two-storey house with light wooden panel facade and dark concrete tile roof, small lawn and hedge, a narrow private gravel driveway leading between the houses to a plot behind, suburban street in Skälby Järfälla, daylight, empty scene"),
    ("Källarplan under ombyggnad till egen bostad med nya väggar av gips",
     "interior of a Swedish villa basement under renovation into a small apartment, new gypsum stud walls, a new window opening, electrical conduits on the walls, clean concrete floor, construction lamp, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HANINGE
"byggforetag-haninge.html": {
  "kind": "district", "service": "byggforetag", "ort": "Haninge", "svc_label": "Byggföretag",
  "title": "Byggföretag i Haninge – bygga i omvandlingsområden",
  "description": "Byggföretag i Haninge: nytt hus eller tillbyggnad när fritidshusområdet blir permanentboende, anstånd med bygglov, genomförandetid och VA-anslutning.",
  "h1": "Byggföretag i Haninge",
  "lead": "Haninge har många fritidshusområden där allt fler bor året runt, och kommunen planlägger dem för permanentboende. För den som vill bygga nytt eller bygga ut betyder det att tidpunkten styrs av detaljplanen och av när gator och vatten och avlopp är klara. Geal Entreprenad AB bygger i Haninge som total entreprenad och hjälper dig att planera projektet efter kommunens tidsplan.",
  "card": "Nytt hus och tillbyggnad i omvandlingsområden.",
  "sections": [
    {"id": "omvandling", "anchor": "Omvandlingen",
     "h2": "Från fritidshusområde till permanentboende",
     "paras": [
       "Haninge kommun kallar de fritidshusområden som ska anpassas för permanentboende för omvandlingsområden. Fler som bor året runt innebär enligt kommunen ökade krav på service, större byggrätter, bättre gator och belysning, bra dricksvatten och bättre rening av avloppsvatten. Processen tar avstamp i kommunens VA-plan och pågår ofta under många år.",
       "Först tas en detaljplan fram, sedan bygger kommunen ut vatten, avlopp och gator, och därefter ansluter varje fastighet. Detaljplanen bestämmer var man får bygga och kan också styra hur fastigheter delas och hur husen placeras och utformas. Medan planen tas fram brukar beslut om bygglov skjutas upp, så kallat anstånd, för att underlätta planarbetet.",
       "Du har rätt att lämna synpunkter vid samrådet och granskningen, och kommunen håller i regel också startmöten när planarbetet börjar. Det är ett bra tillfälle att ta upp vad du vill kunna bygga på tomten i framtiden.",
     ],
     "aside": {"title": "Ordningen i Haninge", "items": [
       "VA-planen pekar ut området",
       "Detaljplan med samråd och granskning",
       "Kommunen bygger gator och VA",
       "Därefter egen anslutning och bygglov"]}},
    {"id": "genomforandetid", "h2": "Varför bygglovet får vänta",
     "paras": [
       "När detaljplanen har vunnit laga kraft används ofta en förskjuten genomförandetid. Kommunen skriver att det inte går att få bygglov innan genomförandetiden börjar, för att undvika krockar mellan privata husleveranser och kommunens utbyggnad. Därefter beviljas bygglov enligt den nya planen.",
       "Under utbyggnaden kan det enligt kommunen bli buller, damm, tillfälliga upplag och begränsad framkomlighet när gatorna grävs upp, och finns det mycket berg kan det behöva sprängas. Då görs alltid en riskanalys och vibrationsmätare sätts upp på några byggnader. Varje fastighet får en förbindelsepunkt för vatten och avlopp, och ett frischaktsavtal ger kommunen rätt att schakta på tomten för att skydda anslutningspunkten.",
       "För oss betyder det att projekteringen kan göras i god tid, medan själva bygget planeras till när gator och ledningar är färdiga. Ritningar, kostnadsförslag och val av material kan alltså vara klara när genomförandetiden börjar, så att ansökan om bygglov kan lämnas in direkt.",
     ],
     "aside": None},
    {"id": "egen-utbyggnad", "h2": "När det är din tur att bygga",
     "paras": [
       "När den kommunala utbyggnaden är klar kan du börja dra ledningar och bygga på din egen fastighet. Haninge kommun påpekar att du måste söka bygglov innan du bygger till, bygger nytt eller gör markarbeten, och att anslutningen och ledningsdragningen från förbindelsepunkten till huset kräver anmälan. Ledningarna på tomten bekostar du själv.",
       "Kommunen ger också rådet att välja husleverantör med omsorg, eftersom alla hus inte uppfyller planens bestämmelser om utformning och placering. Det är här ett byggföretag som utgår från planbestämmelserna gör nytta: vi ritar och bygger efter det som planen tillåter på din tomt, i stället för att anpassa planen efter ett färdigt hus. Läs mer om " + _L.format("nybyggnad-villa.html", "nybyggnad av villa") + " och " + _L.format("tillbyggnad.html", "tillbyggnad") + ".",
       "Medger detaljplanen att fastigheten delas ansöker du om avstyckning hos Lantmäteriet, och den förrättningen bekostar fastighetsägaren.",
     ],
     "aside": {"title": "Vid egen utbyggnad", "items": [
       "Bygglov innan du bygger eller gör markarbeten",
       "Anmälan för VA-anslutningen",
       "Hus som följer planbestämmelserna",
       "Avstyckning via Lantmäteriet"]}},
    {"id": "avtal-haninge", "h2": "Ett tydligt avtal från början",
     "paras": [
       "Boverket rekommenderar att alltid göra ett skriftligt avtal när du anlitar hantverkare, och konstaterar att det enklaste juridiskt är att köpa allt från ett och samma företag. I avtalet bör det stå vem som ansvarar för vad, vilka material som ska användas och vem som tätar och återställer efter håltagning. Köper du själv in material till entreprenören är du enligt Boverket ansvarig för produktens funktion.",
       "Hos oss får du ett skriftligt kostnadsförslag och avtal, och vi samordnar alla hantverkare och behöriga installatörer för el och VVS. Gäller projektet ett befintligt fritidshus som ska byggas om, se också " + _L.format("koksrenovering-haninge.html", "köksrenovering i Haninge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett byggprojekt i Haninge till",
  "steps": [
    ("Planläget", "Vi tar reda på om området är under planläggning, har anstånd eller väntar på genomförandetiden."),
    ("Platsbesök", "Tomt, berg, befintligt hus och förbindelsepunkten för VA gås igenom."),
    ("Projektering", "Huset eller tillbyggnaden ritas efter planbestämmelserna."),
    ("Kostnadsförslag och avtal", "Ett skriftligt förslag och avtal med tydlig ansvarsfördelning."),
    ("Bygglov och anmälan", "Ansökan om bygglov och anmälan för VA-anslutningen."),
    ("Bygget och överlämning", "Vi samordnar bygget och går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för byggprojekt i Haninge",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor ihop med rutavdrag. Avdraget gäller även fritidshus som du äger och använder.",
    "Ett helt nytt hus ger aldrig rotavdrag, och inte heller att riva ett gammalt hus, även om det nya byggs på samma stomme. En tillbyggnad på ett befintligt hus kan ge avdrag om den sitter ihop med ytterväggen till minst 75 procent av någon sida eller har en dörr in till huset. Vi drar avdraget direkt på fakturan där det gäller.",
  ],
  "price_h2": "Vad påverkar kostnaden i Haninge?",
  "price": [
    "Om det är ett nytt hus, en ombyggnad av ett fritidshus eller en tillbyggnad, hur tomten ser ut med berg och höjdskillnader, hur långt det är till förbindelsepunkten och vad planbestämmelserna säger om utformningen. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför får vi inte bygglov trots att detaljplanen har vunnit laga kraft i Haninge?",
     "Kommunen använder ofta en förskjuten genomförandetid i omvandlingsområdena. Bygglov ges inte innan den börjar, för att privata byggen inte ska krocka med utbyggnaden av gator och VA."),
    ("Behöver vi anmäla när vi kopplar huset till kommunens VA i Haninge?",
     "Ja. Enligt Haninge kommun kräver anslutning och ledningsdragning från förbindelsepunkten till huset en anmälan, och ledningarna på tomten bekostar du själv."),
    ("Vad är ett frischaktsavtal?",
     "En överenskommelse som ger kommunen rätt att schakta eller spränga innanför fastighetsgränsen när förbindelsepunkten för vatten och avlopp anläggs."),
    ("Kan vi välja vilket hus som helst när vi bygger nytt i ett omvandlingsområde?",
     "Nej, huset måste följa planbestämmelserna om utformning och placering. Haninge kommun påpekar att alla husleverantörer inte har hus som gör det."),
    ("Vem betalar avstyckningen om vi vill dela tomten?",
     "Du som fastighetsägare. Ansökan görs hos Lantmäteriet om detaljplanen medger att fastigheten delas."),
  ],
  "sources": [
    ("Haninge kommun – Omvandlingsområden", "https://www.haninge.se/omvandling"),
    ("Haninge kommun – Folder: Omvandlingsområden, från fritidshusområde till område för permanentboende (pdf)",
     "https://www.haninge.se/siteassets/bygga-bo-och-miljo/oversiktsplanering-och-detaljplaner/detaljplaner/bilder/omvandlingsomraden.pdf"),
    _BV_AVTAL, _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ni bygga i ett omvandlingsområde i Haninge?", "Boka ett gratis platsbesök, så går vi igenom planläget, tomten och tidsplanen."),
  "img": [
    ("Nybyggt trähus bredvid en äldre sommarstuga på en bergig tomt i Haninge",
     "newly built modest Swedish two-storey wooden house with dark grey panel and black metal roof next to an old small red summer cottage on a rocky plot with pine trees, newly paved narrow road in front, Haninge archipelago area, daylight, empty scene"),
    ("Nygrävd gata med nya ledningar i ett fritidshusområde",
     "straight open trench along a gravel road in a Swedish summer house area, two straight grey plastic water and sewer pipes lying neatly at the bottom of the trench on sand bedding, excavated soil heaped beside it, pine trees, granite outcrops, small red wooden cottages in the background, realistic civil works, no people, no machines, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VÄRMDÖ
"byggforetag-varmdo.html": {
  "kind": "district", "service": "byggforetag", "ort": "Värmdö", "svc_label": "Byggföretag",
  "title": "Byggföretag på Värmdö – byggrätt, PFO och strandskydd",
  "description": "Byggföretag på Värmdö: bygga ut eller bygga nytt när fritidshusområdet planläggs, kommunens riktlinjer för PFO-områdena, strandskydd och lovfria regler.",
  "h1": "Byggföretag på Värmdö",
  "lead": "På Värmdö hänger frågan om vad du får bygga ofta ihop med var ditt område befinner sig i kommunens planering. I de prioriterade förändringsområdena ses byggrätterna över, och nära vattnet gäller strandskyddet. Geal Entreprenad AB bygger på Värmdö som total entreprenad, och vi börjar med att reda ut vad som gäller för tomten innan något ritas.",
  "card": "Byggrätt, PFO-områden och strandskydd.",
  "sections": [
    {"id": "pfo", "anchor": "PFO-områdena",
     "h2": "De prioriterade förändringsområdena",
     "paras": [
       "Värmdö kommun har många fritidshusområden där allt fler bor permanent, och enligt kommunens broschyr Fritidshusområde i förändring från 2023 handlar det om tusentals fastigheter som ska planläggas och få kommunalt vatten och avlopp. De områden som ska anpassas först kallas prioriterade förändringsområden, PFO, och är utpekade i översiktsplanen Värmdö 2035. Kommunen skriver också att fler permanentboende leder till ökade krav på större byggrätter.",
       "Planprocessen pågår enligt broschyren normalt i två till tre år fram till antagande. När detaljplanen har fått laga kraft och kommunen har byggt ut vatten och avlopp i området kan man söka bygglov och påbörja eventuell fastighetsbildning. För ett husbygge innebär det att idé och skiss kan vara klara långt innan det är möjligt att bygga.",
     ],
     "aside": {"title": "Planens skeden", "items": [
       "Startskede med start-PM",
       "Samråd och utredningar",
       "Granskning",
       "Antagande och laga kraft"]}},
    {"id": "riktlinjer-varmdo", "h2": "Vad riktlinjerna säger om husen",
     "paras": [
       "Översiktsplanens riktlinjer för PFO-områdena, som broschyren återger, säger att byggrätterna ska ses över generellt och bedömas utifrån områdets karaktär och förutsättningar. Karaktären ska behållas: sprängning, schakt och stora utfyllnader bör undvikas, nya byggnader ska anpassas efter topografin, omfattande förtätning genom avstyckning bör undvikas och äldre och skyddsvärda träd ska bevaras.",
       "Riktlinjerna säger också att det inom fastigheten ska finnas plats för parkering, ett möjligt attefallshus och bergvärme. Det är värt att tänka på redan när huset placeras, så att tomten inte blir låst av ett hus som hamnar mitt i den.",
       "Ett nytt eller ombyggt hus på en bergig skärgårdstomt bör alltså gå med terrängen. Vi föreslår grundläggning och placering som kräver så lite sprängning som möjligt och som sparar de stora träden. Läs mer om att " + _L.format("nybyggnad-villa.html", "bygga nytt hus") + " eller om ett " + _L.format("attefallshus.html", "attefallshus på tomten") + ".",
     ],
     "aside": None},
    {"id": "strandskydd", "h2": "Strandskyddet och 100 meter från stranden",
     "paras": [
       "Strandskyddet gäller enligt Boverket generellt vid hav, insjöar och vattendrag och omfattar normalt 100 meter från strandlinjen, både på land och i vattnet. Länsstyrelsen kan utöka det till upp till 300 meter. Inom strandskyddat område får nya byggnader inte uppföras, och inte heller grävning eller andra förberedelser för dem. Den som vill bygga där, till exempel en komplementbyggnad, behöver dispens, och det kräver ett särskilt skäl enligt miljöbalken.",
       "Värmdö kommun påpekar i sin information om de nya reglerna från den 1 december 2025 att det fortfarande inte är tillåtet att bygga lovfritt inom 100 meter från strand eller närmare tomtgränsen än 4,5 meter. Inom kulturhistoriskt värdefulla områden och riksintressen för kulturmiljövården gäller alltid lovplikt, och kommunens kulturmiljökarta visar om din fastighet berörs. Tidigare lovfria åtgärder som friggebodar, skärmtak och attefallsbyggnader räknas in i de nya möjligheterna.",
       "Som fastighetsägare ansvarar du enligt kommunen för att det som byggs följer lagens krav. Vi kontrollerar strandskydd, kulturmiljö och avstånd innan skissen blir en ritning, och om dispens behövs tar vi fram underlaget till ansökan tillsammans med dig.",
     ],
     "aside": {"title": "Kontrollera tidigt", "items": [
       "Avståndet till stranden",
       "Om strandskyddet är utökat",
       "Kulturmiljökartan",
       "Avståndet till tomtgränsen"]}},
    {"id": "vagar", "h2": "Vägföreningen, dagvattnet och tomten",
     "paras": [
       "I de flesta förändringsområdena föreslås enskilt huvudmannaskap, vilket enligt broschyren innebär att fastighetsägarna genom väg- eller samfällighetsföreningen ansvarar för drift och underhåll av vägar och naturmark. Inom den egna fastigheten är det fastighetsägaren som ska ta hand om dagvattnet. Förbindelsepunkten för vatten och avlopp ligger normalt cirka en halv meter utanför fastighetsgränsen, och ledningarna fram till huset bekostar du själv.",
       "För ett byggprojekt betyder det att tillfart för material, upplag och hårdgjorda ytor behöver planeras med vägarna och dagvattnet i åtanke. Ska ett befintligt fritidshus få nytt badrum när VA kommer, läs mer under " + _L.format("badrumsrenovering-varmdo.html", "badrumsrenovering på Värmdö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett byggprojekt på Värmdö till",
  "steps": [
    ("Planläget", "Vi tar reda på om tomten ligger i ett PFO-område och var planarbetet står."),
    ("Platsbesök", "Berg, träd, avstånd till strand och gräns samt tillfarten gås igenom."),
    ("Skiss och kostnadsförslag", "Huset placeras efter terrängen och du får ett skriftligt förslag."),
    ("Lov och dispens", "Bygglov, anmälan eller strandskyddsdispens tas fram där det krävs."),
    ("Bygget", "Vi samordnar grund, stomme, tak och installationer."),
    ("Slutgenomgång", "Vi går igenom huset med dig och lämnar över handlingarna."),
  ],
  "rot_h2": "ROT-avdrag för byggprojekt på Värmdö",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Det gäller även ett fritidshus som du äger och använder.",
    "Att bygga om ett fritidshus till åretruntbostad, till exempel tilläggsisolera väggar och göra om planlösningen, kan ge avdrag. Ett helt nytt hus ger det aldrig. En tillbyggnad ger avdrag om den sitter ihop med husets yttervägg till minst 75 procent av någon sida eller har en dörr in till huset. Vi drar avdraget på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden på Värmdö?",
  "price": [
    "Terrängen och hur mycket berg som måste hanteras, avståndet till förbindelsepunkten, tillfarten för material på smala vägar och om det befintliga huset ska byggas om eller ersättas. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("När kan vi söka bygglov för ett större hus i vårt PFO-område på Värmdö?",
     "Enligt kommunen när detaljplanen har fått laga kraft och vatten och avlopp har byggts ut i området. Planprocessen fram till antagande tar normalt två till tre år."),
    ("Får vi bygga en gäststuga nära vattnet på Värmdö utan lov?",
     "Inte inom 100 meter från strand, där strandskyddet gäller. Där krävs dispens, och den kräver ett särskilt skäl enligt miljöbalken."),
    ("Varför vill kommunen att vi undviker sprängning på tomten?",
     "Riktlinjerna för PFO-områdena syftar till att behålla områdenas karaktär. Därför bör sprängning, schakt och stora utfyllnader undvikas och nya byggnader anpassas efter topografin."),
    ("Vem ansvarar för vägen till vår tomt när området planläggs?",
     "I de flesta förändringsområdena föreslås enskilt huvudmannaskap. Då ansvarar fastighetsägarna, via väg- eller samfällighetsföreningen, för drift och underhåll av vägarna."),
    ("Räknas vår gamla friggebod in när vi bygger nytt på tomten?",
     "Ja. Värmdö kommun påpekar att tidigare lovfria åtgärder som friggebodar, skärmtak och attefallsbyggnader räknas in i de nya möjligheterna."),
  ],
  "sources": [
    ("Värmdö kommun – Förändringar i PBL från 1 december 2025",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/forandringaripblfrom1december2025.4.18b9914519a768a188a2872.html"),
    ("Värmdö kommun – Fritidshusområde i förändring, del 1 Planering (2023, pdf)",
     "https://www.varmdo.se/download/18.52346f71869c9938611c2df/1678200543391/Broschyr%20PFO%20del%201%20-%20uppdaterad%202023.pdf"),
    _BV_STRAND, _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Ska ni bygga på Värmdö?", "Boka ett gratis platsbesök, så går vi igenom tomten, planläget och strandskyddet."),
  "img": [
    ("Nytt trähus anpassat efter berget på en skogstomt på Värmdö",
     "new Swedish two-storey wooden house with dark stained vertical panel and black standing-seam metal roof built on a granite slope among tall pine trees, foundation following the rock, glimpse of the Baltic sea between the trees, Värmdö, daylight, empty scene"),
    ("Smal grusväg genom ett fritidshusområde med tallar och berghällar",
     "narrow gravel road through a Swedish archipelago summer house area with pine trees, granite outcrops, mailboxes on a wooden post and small red and grey cottages, overcast daylight, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TYRESÖ
"byggforetag-tyreso.html": {
  "kind": "district", "service": "byggforetag", "ort": "Tyresö", "svc_label": "Byggföretag",
  "title": "Byggföretag i Tyresö – från startbesked till slutbesked",
  "description": "Byggföretag i Tyresö: tillbyggnad och nytt hus med startbesked, utstakning och slutbesked, kommunens tillsyn, avstyckning och råd om vatten vid huset.",
  "h1": "Byggföretag i Tyresö",
  "lead": "Ett byggprojekt i Tyresö har flera kontrollpunkter mellan idé och inflyttning: lov eller anmälan, startbesked, utstakning, lägeskontroll och slutbesked. Hoppar man över någon kan det bli ett tillsynsärende. Geal Entreprenad AB driver byggprojekt i Tyresö som total entreprenad och håller ordning på stegen åt dig, med en kontakt genom hela bygget.",
  "card": "Startbesked, utstakning och slutbesked.",
  "sections": [
    {"id": "lov-tyreso", "anchor": "Lov och anmälan",
     "h2": "Lovfritt, lovpliktigt eller anmälan",
     "paras": [
       "Tyresö kommun beskriver de nya reglerna från den 1 december 2025 så här: bygger du till ett en- eller tvåbostadshus med mer än sammantaget 30 kvadratmeter krävs bygglov. Inom kulturhistoriskt särskilt värdefulla områden och riksintressen för kulturmiljövården krävs alltid bygglov. Kommunen påpekar att sådana områden kan finnas i översiktsplanen, kulturmiljöprogrammet eller detaljplanen, men att informationen inte alltid är uppdaterad, och rekommenderar att man hör av sig.",
       "Även en lovfri tillbyggnad kan kräva anmälan och startbesked, till exempel när byggnadens konstruktion berörs eller när vatten och avlopp eller en eldstad installeras. Många åtgärder granskas inte längre av kommunen innan de görs, och då behöver du själv kontrollera att reglerna följs. Den som vill ha ett beslut att luta sig mot kan söka frivilligt bygglov.",
       "Vi går igenom vilken kategori ditt projekt hamnar i innan något beställs, oavsett om det gäller en " + _L.format("tillbyggnad.html", "tillbyggnad") + ", ett " + _L.format("attefallshus.html", "komplementbostadshus") + " eller ett helt nytt hus.",
     ],
     "aside": {"title": "Tre vägar", "items": [
       "Lovfritt – du ansvarar själv",
       "Anmälan och startbesked",
       "Bygglov, startbesked och slutbesked",
       "Frivilligt lov om du vill ha beslut"]}},
    {"id": "startbesked", "h2": "Startbesked, utstakning och slutbesked",
     "paras": [
       "Plan- och bygglagen säger att en åtgärd som kräver bygglov eller anmälan inte får påbörjas innan byggnadsnämnden har gett startbesked. Byggnaden får inte heller tas i bruk innan nämnden har gett slutbesked, om den inte beslutar annat. Byggherren ansvarar för att det som byggs, och projekteringen bakom, uppfyller lagens krav.",
       "Efter startbeskedet ska kommunen enligt lagen låta staka ut byggnaden eller tillbyggnaden och markera höjdläget, om förhållandena på platsen kräver det. Är läget direkt beroende av gränsen mot grannen ska grannen kallas till utstakningen. I Tyresö är det geodataenheten på samhällsbyggnadskontoret som utför utstakning och lägeskontroll och tar fram nybyggnadskartor.",
       "Vi planerar bygget så att utstakningen är gjord innan grunden läggs, och samlar underlaget som behövs inför slutbeskedet. Kontrollerna i kontrollplanen dokumenteras under bygget, så att inget behöver letas fram i efterhand när huset ska tas i bruk.",
     ],
     "aside": None},
    {"id": "tillsyn", "h2": "Tillsyn och olovligt byggande",
     "paras": [
       "Tyresö kommun gör tillsyn på eget initiativ eller efter en anmälan. Enligt kommunen räknas det som olovligt byggande att bygga något som kräver lov utan att ha fått det, men också att börja bygga utan startbesked eller att flytta in utan slutbesked. Vid överträdelser kan byggnads- och tillsynsnämnden besluta om förbud, föreläggande eller rättelseföreläggande, och om någon gjort sig skyldig till olovligheter ska byggsanktionsavgift tas ut.",
       "Kommunen påpekar också att fastighetsägaren alltid är ytterst ansvarig för fastigheten och de ändringar som görs där. Ett rättelseföreläggande kan till exempel bli aktuellt om en byggaktör inte följer det givna bygglovet. Därför bygger vi efter lovet och de ritningar som ligger till grund för det, och tar upp eventuella ändringar med dig innan de görs.",
     ],
     "aside": {"title": "Olovligt enligt kommunen", "items": [
       "Bygga utan lov där lov krävs",
       "Börja utan startbesked",
       "Flytta in utan slutbesked",
       "Inte följa det givna bygglovet"]}},
    {"id": "tomt-tyreso", "h2": "Avstyckning och vattnet runt huset",
     "paras": [
       "Ska tomten delas för ett nytt hus är det Lantmäteriet som beslutar, eftersom Tyresö kommun inte har någon egen lantmäterimyndighet. I detaljplanen kan du se om avstyckning är möjlig och vilken minsta tomtstorlek som gäller, och planen hittar du i kommunens webbkarta.",
       "Kommunen ger också råd om översvämning som är bra att ta med när ett hus eller en tillbyggnad placeras: marken bör luta bort från huset, minst 15 centimeter på de första tre metrarna, och stuprör och hängrännor bör hållas i gott skick. Ändringar av fastighetens vatten- och avloppssystem ska godkännas av tekniska kontoret. Läs mer om takavvattning under " + _L.format("platslagare-tyreso.html", "plåtslagare i Tyresö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så driver vi ett byggprojekt i Tyresö",
  "steps": [
    ("Platsbesök", "Vi går igenom huset, tomten och hur marken lutar."),
    ("Regler och plan", "Detaljplan, kulturmiljö och om lov, anmälan eller frivilligt lov behövs."),
    ("Kostnadsförslag", "Ett skriftligt förslag där ROT-berättigat arbete framgår."),
    ("Startbesked och utstakning", "Bygget börjar först när startbeskedet finns och huset är utstakat."),
    ("Bygget", "Vi samordnar alla hantverkare och behöriga installatörer för el och VVS."),
    ("Slutbesked", "Underlaget lämnas in och vi går igenom arbetet med dig."),
  ],
  "rot_h2": "ROT-avdrag för byggprojekt i Tyresö",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material, resor och administration ger inget avdrag.",
    "En tillbyggnad ger avdrag om den sitter ihop med husets yttervägg till minst 75 procent av någon sida eller har en dörr in till huset. Ett helt nytt hus, en friggebod eller ett garage ger inget avdrag, och inte heller bygglovshandlingar eller besiktningsman. Vi drar avdraget direkt på fakturan där det gäller.",
  ],
  "price_h2": "Vad styr kostnaden i Tyresö?",
  "price": [
    "Projektets storlek, om bygglov och kontrollplan behövs, hur grunden anpassas till berg och lutning, och hur tillbyggnaden ansluts till huset. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi börja bygga vår tillbyggnad i Tyresö när bygglovet är klart?",
     "Inte förrän byggnadsnämnden också har gett startbesked. Enligt Tyresö kommun räknas det som olovligt byggande att börja utan startbesked."),
    ("Vem stakar ut huset i Tyresö?",
     "Kommunens geodataenhet utför utstakning och lägeskontroll. Ligger huset nära gränsen ska grannen enligt plan- och bygglagen kallas till utstakningen."),
    ("Kan vi flytta in i den nya delen innan slutbesked?",
     "Nej, inte i de delar som omfattas av startbeskedet, om inte nämnden beslutar annat. Kommunen räknar inflyttning utan slutbesked som olovligt."),
    ("Vem beslutar om avstyckning av en tomt i Tyresö?",
     "Lantmäteriet. Tyresö kommun har ingen egen lantmäterimyndighet, men i detaljplanen ser du om avstyckning är möjlig och vilken tomtstorlek som gäller."),
    ("Hur ska marken luta runt en ny tillbyggnad?",
     "Tyresö kommun rekommenderar att marken lutar bort från huset med minst 15 centimeter på de första tre metrarna, så att regnvatten inte leds mot grunden."),
  ],
  "sources": [
    ("Tyresö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
     "https://www.tyreso.se/boende--miljo/bygga/bygga-riva-eller-andra/forandringar-i-plan--och-bygglagen-fran-1-december-2025.html"),
    ("Tyresö kommun – Tillsyn enligt plan- och bygglagen",
     "https://www.tyreso.se/boende--miljo/bygga/tillsyn-enligt-plan--och-bygglagen.html"),
    ("Tyresö kommun – Mätuppdrag och kartor", "https://www.tyreso.se/boende--miljo/bygga/matuppdrag-och-kartor.html"),
    ("Tyresö kommun – Avstyckning och servitut", "https://www.tyreso.se/boende--miljo/bygga/avstyckning-och-servitut.html"),
    ("Tyresö kommun – Översvämningsrisker och åtgärder",
     "https://www.tyreso.se/boende--miljo/vatten-och-avlopp/oversvamningsrisker-och-atgarder.html"),
    _PBL, _SKV_ROT, _SKV_JOB,
  ],
  "cta": ("Planerar ni att bygga i Tyresö?", "Boka ett gratis platsbesök, så går vi igenom projektet och vilka besked som behövs."),
  "img": [
    ("Villa i Tyresö med en nybyggd tillbyggnad på berg och tallar runt omkring",
     "Swedish 1960s single-storey villa with grey concrete tile roof and a newly built timber extension with white panel and large windows, built on a gently sloping granite plot among pine trees, lawn sloping away from the house, Tyresö, daylight, empty scene"),
    ("Utstakningspinnar och snören på en tomt där en tillbyggnad ska byggas",
     "thin wooden survey pegs hammered into a grass lawn with taut orange string between them outlining a rectangle next to the wall of a light painted Swedish wooden villa, nothing built yet, only pegs and string on the grass, pine trees and granite in the background, daylight, no people, no text"),
  ],
  "related": [],
},

}
