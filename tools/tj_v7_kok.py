# -*- coding: utf-8 -*-
"""Tjänster v7 – ortsidor köksrenovering i Enskede, Älvsjö, Spånga, Botkyrka, Upplands Väsby och Vallentuna
(2026-10-25). Schema: se tools/tj_check.py.
Källor öppnade och kontrollerade 2026-10-25:
  Stadsmuseet via Stockholmskällan (Gamla Enskede byggnadsinventering 1974–1977; Stockholms spår: Sockenplan;
  S. Lindhagen, Älvsjö villastad – ett exempel på förortsinventering; J. Ferenius och L. Johannesson, Ur Hem på
  landets arkiv), Stockholms stad (översiktsplanens riksintressen; bygglov.stockholm: flytta kök eller badrum,
  inredning av ytterligare bostad, ny bostad i enbostadshus), Botkyrka kommun (flytt av kök eller badrum, bidrag
  för att anpassa bostaden, Framtid för Tullinge 2010), Södertörns brandförsvarsförbund (radhus), Upplands Väsby
  kommun (kunskapsunderlag för kulturmiljö, nya byggregler från 1 juli 2025, tillbyggnad), Vallentuna kommun
  (tillbyggnad av en- och tvåbostadshus, eldstad, anmälningspliktiga åtgärder, översiktsplan 2040), Boverket
  (lista över PBL-ändringar 1 december 2025; risker med asbest i byggnader), Arbetsmiljöverket (tillstånd för
  rivning av asbest), Elsäkerhetsverket (vad får jag göra själv med el; anlita ett elinstallationsföretag) och
  Skatteverket (så fungerar rotavdraget; ger arbetet rätt till rotavdrag).
Strukna (ej verifierade): att Gamla Enskede som helhet är klassat som särskilt värdefullt enligt PBL 8:13
(bara riksintresset är belagt – texten hänvisar till Stadsmuseets karta), att kökstrappor fortfarande finns kvar,
vilka kök som hade vedspis eller gasspis från början, att Solhemsvillornas uthus i dag är inredda, asbestförekomst
i enskilda områden, andel radhus i Tumba, vilken räddningstjänst som täcker Upplands Väsby och Vallentuna, att
Älvsjövillornas uthyrningslägenheter i dag är sammanslagna. Inga priser, garantier, omdömen, egna uppdrag eller
cert."""

L = '<a class="text-link" href="{0}">{1}</a>'
X = '<a class="text-link" href="{0}" rel="noopener">{1}</a>'

S_ROT = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
S_ROTJOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
U_BV_PBL = "https://www.boverket.se/sv/om-boverket/boverkets-uppdrag/aktuella-regeringsuppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/"
S_BV_PBL = ("Boverket – Lista med PBL-ändringar som trädde i kraft den 1 december 2025", U_BV_PBL)
U_BV_ASB = "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/"
U_AV_ASB = "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/"
U_ELS_SJ = "https://www.elsakerhetsverket.se/privatpersoner/detta-far-du-gora-sjalv-med-el/vad-far-jag-gora-sjalv-med-el"
U_ELS_AN = "https://www.elsakerhetsverket.se/privatpersoner/anlita-ett-elinstallationsforetag"

U_STH_FLYTT = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/flytta-kok-eller-badrum/"
U_STH_YTTR = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/inredning-av-ytterligare-bostad/"
U_STH_NYBO = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/ny-bostad-i-enbostadshus-bygglovsbefriad/"
U_STH_RIKS = "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf"
U_ENS_INV = "https://stockholmskallan.stockholm.se/postfiles/KUL/SSM_Gamla_Enskede__byggnadsinventering_1974_1977_00.pdf"
U_ENS_SOCK = "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000049.pdf"
U_ALV = "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf"
U_SOLHEM = "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005802_01.pdf"

U_BOT_FLYTT = "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/flytt-av-kok-eller-badrum"
U_BOT_BAB = "https://www.botkyrka.se/stod-trygghet-och-familj/aldreomsorg/for-dig-som-bor-hemma/mer-stod-for-dig-som-bor-hemma/bidrag-for-att-anpassa-bostaden"
U_BOT_TUL = "https://botkyrka.se/download/18.1fbbaae6170bff9469deb44/1584093808003/Tullinge%20utvecklingsprogram.pdf"
U_SBFF_OM = "https://www.sbff.se/om-oss/"
U_SBFF_RAD = "https://www.sbff.se/hem--fritid/brandsakerhet-i-hemmet/radhus/"

U_UV_KM = "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf"
U_UV_BBR = "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/nya-byggregler-fran-1-juli-2025"
U_UV_TILL = "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/tillbyggnad"

U_VAL_TILL = "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/behover-jag-bygglov/tillbyggnad-av-en--och-tvabostadshus"
U_VAL_ELD = "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/behover-jag-bygglov/eldstad"
U_VAL_ANM = "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/anmalningspliktiga-atgarder"
U_VAL_OP = "https://vallentuna.se/download/18.63572f8619eeecafce08366/1782478377449/2.11.7%20%C3%96versiktsplan%202040.pdf"

PAGES_TJ = {

# =============================== KÖK ENSKEDE ===============================
"koksrenovering-enskede.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Enskede", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Enskede – typhus, småstugor och ett kök",
  "description": "Köksrenovering i Enskede: typhusens små kök, regeln om ett kök per hus från 1908, småstugorna "
                 "på Enskedefältet och vad som gäller för ett andra kök i dag.",
  "h1": "Köksrenovering i Enskede",
  "lead": "När Gamla Enskede byggdes fick varje hus bara ha ett kök. Många av typhusen var på två eller tre rum "
          "och kök, och köket var därefter. I dag vill de flesta ha mer plats och ljus vid spisen, och ibland ett "
          "extra pentry i källaren. Geal Entreprenad AB gör om kök i Enskede med gratis platsbesök, skriftligt "
          "kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Typhus, dubbelhus och småstugor.",
  "sections": [
    {"id": "ett-kok", "anchor": "Ett kök per hus",
     "h2": "Ett kök per hus – en regel från 1908",
     "paras": [
       "Enligt Stadsmuseets " + X.format(U_ENS_INV, "byggnadsinventering av Gamla Enskede") + " uppläts tomterna "
       "med tomträtt från den 1 januari 1908. Kontraktet gällde i 60 år och reglerade bebyggelsen: boningshuset "
       "fick ha högst två våningar utöver källare och vind och skulle bara innehålla ett kök. Regeln var till för "
       "att huset inte skulle bli bostad åt mer än en familj, och den hörde ihop med ett förbud mot inneboende.",
       "Staden åtog sig i samma kontrakt att anlägga vägar och dra fram vatten, avlopp och gas. Inventeringen "
       "beskriver hur en jämförelse omkring 1910 visade att ett eget hem med två rum och kök, källare och "
       "trädgårdstäppa i Enskede kostade lika mycket per år som att hyra en lika stor lägenhet i innerstaden.",
       "Typhusen i inventeringen spänner från två rum och kök till fem rum och kök, och bara några av "
       "planerna har eget bad. Vid platsbesöket börjar vi därför med att ta reda på vilken typ huset hör "
       "till och vad som har ändrats i köket sedan dess.",
     ],
     "aside": {"title": "Typhusen i Gamla Enskede", "items": [
       "Radhus och dubbelhus: 2–3 rum och kök",
       "Friliggande: 2–5 rum och kök",
       "Bad bara i några typer",
       "Kärnan byggd 1908–1913"]}},
    {"id": "andra-koket",
     "h2": "Ett andra kök i källaren – när det räknas som en ny bostad",
     "paras": [
       "Ett pentry i källaren för gäster eller vuxna barn är en vanlig önskan. Blir utrymmet en egen bostad "
       "gäller reglerna för " + X.format(U_STH_NYBO, "ny bostad i enbostadshus") + ": staden skriver att den kan "
       "inredas utan bygglov under vissa förutsättningar, men att utökad lovplikt gäller i en särskilt "
       "kulturhistoriskt värdefull byggnad eller ett sådant område. Då krävs bygglov även för det som annars "
       "är lovfritt.",
       "Gamla Enskede är ett av de fem småhusområden i Stockholm som enligt " + X.format(U_STH_RIKS, "översiktsplanens redovisning")
       + " är av riksintresse för kulturmiljövården. Om just ditt hus omfattas av utökad lovplikt ger "
       "Stadsmuseets klassificeringskarta en första indikation, och ibland behövs museets bedömning.",
       "Oavsett lovfrågan ska en " + X.format(U_STH_YTTR, "ytterligare bostad") + " uppfylla dagens krav på "
       "bland annat tillgänglighet, brandsäkerhet och rumshöjd. Ändras brandskydd eller bärande konstruktion, "
       "eller installeras vatten och avlopp, behövs dessutom en anmälan och ett startbesked innan arbetet "
       "börjar. Vi reder ut vad som gäller innan källarköket ritas.",
     ],
     "aside": None},
    {"id": "flytta-koket",
     "h2": "Flytta köket i ett typhus",
     "paras": [
       "Inventeringen beskriver att friliggande hus ibland har långsidan med veranda mot gatan och ibland "
       "gaveln, oftast med en kökstrappa vänd mot gatan. Köket har alltså ofta legat vid gaveln med egen "
       "ingång. Vill man flytta det till trädgårdssidan eller öppna det mot vardagsrummet är det planlösningen "
       "inne i huset som ändras, och det kräver enligt " + X.format(U_STH_FLYTT, "Stockholms stad") + " inget "
       "bygglov.",
       "En anmälan och ett startbesked behövs däremot om flytten påverkar bärande konstruktion eller "
       "brandskydd, om ventilationen ändras väsentligt eller om en ny VA-stam dras i ett nytt schakt. Staden "
       "påminner om att ett kök behöver tillräcklig frånluft och ska uppfylla kraven för imkanal, och råder dig "
       "att tidigt fråga sotaren om förutsättningarna för en ny eller ändrad kanal.",
       "Staden skriver också att hänsyn till byggnadens kulturhistoriska värden ska tas vid alla ändringar, "
       "även inomhus. Därför sparar vi gärna fasta snickerier som går att återanvända, till exempel "
       "dörrfoder och fönsterbänkar. Ska fasaden eller fönstren mot gatan ändras samtidigt, se "
       + L.format("fasadrenovering-enskede.html", "fasadrenovering i Enskede") + ".",
     ],
     "aside": {"title": "Anmälan när köket flyttas", "items": [
       "Bärande vägg eller bjälklag påverkas",
       "Brandskyddet ändras",
       "Ny fläkt eller kanal som ändrar flödena",
       "Ny VA-stam i nytt schakt"]}},
    {"id": "smastugor",
     "h2": "Småstugorna på Enskedefältet och vid Sockenplan",
     "paras": [
       "Enligt " + X.format(U_ENS_SOCK, "Stockholms spår om Sockenplan") + " fortsatte utbyggnaden efter "
       "trädgårdsstadens kärna ända fram till 1945. Enskedefältet byggdes ut med småstugor 1930–32, och mer än "
       "400 stugor uppfördes genom självbyggeri. Nära Sockenplan byggdes småstugor 1931–40, många efter "
       "arkitekten Edvin Engströms typhusritningar.",
       "Tanken var att familjer med små inkomster skulle kunna skaffa ett eget hem genom eget arbete. I en "
       "självbyggd stuga kan köket ha fått nya rör och ny el i flera omgångar, utförda av olika händer. När vi "
       "river de gamla skåpen tittar vi därför på hur ledningarna faktiskt går innan den nya planen låses.",
       "Stugorna är små, så varje decimeter räknas. Ofta blir lösningen att låta diskbänken stå kvar vid "
       "stammen och i stället vinna plats med högskåp och en smalare ö. Ska tak och väggar målas i samma "
       "veva är det enklast innan inredningen monteras, se " + L.format("malare-enskede.html", "målare i Enskede") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till i Enskede",
  "steps": [
    ("Platsbesök", "Vi mäter köket, ser var stam, frånluft och el finns och går igenom vad som ska behållas."),
    ("Lov och anmälan", "Ska ett andra kök eller en ny bostad inredas kontrollerar vi kartan och om lov eller anmälan behövs."),
    ("Skriftligt kostnadsförslag", "Rivning, installationer, snickeri och montering redovisas var för sig."),
    ("Rivning och ledningar", "Gamla skåp tas bort och rör, el och kanal dras om enligt den nya planen."),
    ("Väggar, golv och stomme", "Ytskikten görs klara och stommen monteras, med bänkskivan inmätt på plats."),
    ("Genomgång", "Vitvaror ansluts och provas och vi går igenom köket tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för köket i Enskede",
  "rot": [
    "Skatteverket räknar det som rotarbete att montera köksinredning och installera vitvaror i samband med en "
    "omfattande renovering, liksom att byta och måla köksluckor, riva väggar och bygga om planlösningen. "
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag.",
    "Du ska äga bostaden när arbetet utförs och bo i den. Material ger inget avdrag, så vi skriver arbete och "
    "material var för sig och drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Enskede?",
  "price": [
    "Mest om köket stannar vid stammen eller flyttas, om en ny kanal behövs och om ett andra kök kräver lov "
    "och anpassning till dagens krav. Små rum med sneda väggar gör också att mer inredning måste anpassas på "
    "plats. Efter ett gratis besök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga ett pentry i källaren på vårt hus i Gamla Enskede?",
     "Så länge det inte blir en egen bostad gäller samma regler som när ett kök byggs om. Blir källaren en egen bostad krävs bygglov om "
     "huset eller området är särskilt kulturhistoriskt värdefullt, och den nya bostaden ska uppfylla dagens krav."),
    ("Varför är köket så litet i många hus i Enskede?",
     "Typhusen ritades ofta som två eller tre rum och kök, och tomträttskontraktet tillät bara ett kök per hus. "
     "Köket var tänkt för en familj och sällan för mer än matlagning."),
    ("Behöver vi bygglov för att flytta köket inne i vårt typhus?",
     "Nej. Stockholms stad kräver däremot anmälan och startbesked om flytten påverkar bärande konstruktion, "
     "brandskydd, ventilationen väsentligt eller kräver en ny VA-stam i nytt schakt."),
    ("Gäller kulturvärdena även när vi bara bygger om inomhus?",
     "Ja. Staden skriver att hänsyn till byggnadens kulturhistoriska värden ska tas vid alla ändringar, även "
     "när ingen anmälan krävs."),
    ("Vem kan bedöma om den gamla kanalen räcker för en ny köksfläkt?",
     "Staden råder dig att tidigt fråga skorstensfejarmästaren, alltså sotaren, om förutsättningarna för en ny "
     "eller ändrad ventilationskanal eller imkanal."),
  ],
  "sources": [
    ("Stadsmuseet – Gamla Enskede, byggnadsinventering 1974–1977 (Stockholmskällan, pdf)", U_ENS_INV),
    ("Stockholms spår – Sockenplan (Stockholmskällan, pdf)", U_ENS_SOCK),
    ("Stockholms stad – Riksintressen i översiktsplanen (pdf)", U_STH_RIKS),
    ("Stockholms stad – Ny bostad i enbostadshus (bygglovsbefriad)", U_STH_NYBO),
    ("Stockholms stad – Inredning av ytterligare bostad", U_STH_YTTR),
    ("Stockholms stad – Flytta kök eller badrum", U_STH_FLYTT),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Enskede bli större?", "Boka ett gratis besök, så går vi igenom planlösning, kanal och lovfrågor på plats."),
  "img": [
    ("Ljust renoverat kök med vita luckor och träbänkskiva i ett äldre trähus i Enskede",
     "renovated small kitchen in a 1910s Swedish wooden garden-city house, white painted shaker cabinet doors, "
     "oak wooden worktop, small-paned old window with white frame looking out on an apple tree, wide pine "
     "floorboards, simple pendant lamp, soft daylight, no people, no text"),
    ("Smalt kök med ljusgröna luckor",
     "small 1930s Swedish self-built cottage with light ochre painted wooden panel, white window frames, "
     "red single-curved clay tile roof, small garden with lilac and a picket fence, quiet street, early summer, "
     "full-bleed photo filling the whole frame, no borders, no people, no text"),
  ],
  "related": [],
},

# =============================== KÖK ÄLVSJÖ ===============================
"koksrenovering-alvsjo.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Älvsjö", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Älvsjö – villastaden och dess två kök",
  "description": "Köksrenovering i Älvsjö: villor med tidigt vatten och avlopp, hus som en gång hade flera "
                 "lägenheter och kök som slås ihop. Anmälan, imkanal och väggar.",
  "h1": "Köksrenovering i Älvsjö",
  "lead": "Älvsjö villastad fick vatten och avlopp ovanligt tidigt, och många villor byggdes med mer än en "
          "lägenhet. I dag betyder det att ett hus kan ha rör från flera epoker och spår av ett andra kök. "
          "Geal Entreprenad AB gör om kök i Älvsjö, Långbro och Herrängen med gratis platsbesök, skriftligt "
          "kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Villastad, flerlägenhetsvillor och kök i lager.",
  "sections": [
    {"id": "villastaden", "anchor": "Älvsjö villastad",
     "h2": "En villastad med vatten och avlopp från början",
     "paras": [
       "Stadsmuseets " + X.format(U_ALV, "förortsinventering av Älvsjö villastad") + " berättar att AB Hem på "
       "landet köpte två markområden från Älvsjö säteri 1908 och 1911, på omkring 13 och 11 hektar. "
       "Tomtförsäljningen började i december 1908, och omkring 1915 var uppåt hundra tomter bebyggda.",
       "En orsak till att området växte så snabbt var att det ovanligt tidigt fick vatten, avlopp och ordnade "
       "vägar. Bolaget lämnade gatumark till Stockholms stad och fick i gengäld vattenledningar framdragna "
       "utan kostnad, och staden medverkade till avloppet. Som jämförelse fick Örby vatten och avlopp först i "
       "slutet av 1930-talet. För Älvsjö fastställdes en stadsplan redan 1921.",
       "För köket betyder det att installationerna i en Älvsjövilla kan ha bytts och byggts på i många "
       "omgångar under mer än hundra år. Innan en ny plan ritas vill vi därför se var stammen går och hur "
       "avloppet är anslutet under golvet.",
     ],
     "aside": {"title": "Älvsjö villastad", "items": [
       "Mark köpt 1908 och 1911",
       "Vatten och avlopp tidigt",
       "Stadsplan 1921",
       "Villor på 2–4 rum och kök"]}},
    {"id": "flera-lagenheter",
     "h2": "När villan hade flera lägenheter",
     "paras": [
       "Inventeringen skriver att villorna i allmänhet var på två, tre eller fyra rum och kök, men att husen "
       "ibland rymde flera lägenheter där den eller de minsta var avsedda för uthyrning. Bland nybyggarna "
       "fanns enligt inventeringen hantverkare och tjänstemän, till exempel snickare, målare och byggmästare.",
       "Ett sådant hus kan i dag ha en övervåning med igensatta anslutningar efter ett kök som inte längre "
       "används. Att " + X.format(U_STH_YTTR, "slå samman lägenheter") + " kräver enligt Stockholms stad inget "
       "bygglov, men du kan behöva göra en anmälan och invänta startbesked. Att dela en lägenhet till två "
       "kräver däremot bygglov.",
       "När ett gammalt kök tas bort ska avloppet och vattnet pluggas där de inte längre behövs, och den "
       "gamla imkanalen antingen användas för det nya rummet eller tas ur bruk på ett sätt som sotaren godtar. "
       "Det är detaljer som är lätta att missa när två kök blir ett.",
     ],
     "aside": None},
    {"id": "kanal-alvsjo",
     "h2": "Imkanalen avgör var spisen kan stå",
     "paras": [
       "Ett kök behöver enligt " + X.format(U_STH_FLYTT, "stadens sida om att flytta kök") + " tillräcklig "
       "frånluft och ska uppfylla kraven för imkanal. Ska spisen flyttas bort från den befintliga kanalen "
       "måste en ny dras, och påverkar den nya fläkten eller kanalen ventilationsflödena räknas det som en "
       "väsentlig ändring som kräver anmälan.",
       "I en villa med inredd vind kan en ny kanal behöva gå genom flera bjälklag och ut genom taket. Ta hål "
       "i bjälklag eller bärande delar kan påverka konstruktionen, och då ska en konsult bedöma det. "
       "Staden råder också till att fråga sotaren tidigt, eftersom en del äldre kanaler inte har de mått som "
       "ett modernt kök kräver.",
       "Ska kanalen ut genom taket samordnar vi genomföringen och plåten runt den med "
       + L.format("taklaggare-alvsjo.html", "takläggare i Älvsjö") + ", så att taket blir tätt igen direkt "
       "efter att hålet tagits upp.",
     ],
     "aside": {"title": "Innan spisen flyttas", "items": [
       "Var går den befintliga imkanalen?",
       "Räcker kanalens mått?",
       "Behövs hål i bjälklaget?",
       "Krävs anmälan för ny fläkt?"]}},
    {"id": "villatyperna",
     "h2": "Puts nere, panel uppe – och väggen mot matsalen",
     "paras": [
       "Inventeringen beskriver två vanliga villatyper från 1910-talet: friliggande hus med vit slätputsad "
       "bottenvåning, gavelspetsar med mörkbrun panel på förvandring och brant tegeltak, och hus med "
       "falurödfärgad träpanel och vita snickerier. Båda finns kvar i nästan ursprungligt skick, och det "
       "var ganska vanligt att ritningar återanvändes från andra områden som bolaget byggde.",
       "I de husen ligger köket ofta intill en matsal eller ett mindre rum. Att öppna väggen mellan dem är "
       "en vanlig önskan. Om väggen bär bjälklaget går inte att se på ytan, och påverkas "
       "den bärande konstruktionen krävs anmälan och startbesked. Därför låter vi en konstruktör titta på "
       "väggen innan något rivs.",
       "Ytskikten i ett gammalt kök kan vara lagda i flera lager, och golvet under de gamla skåpen saknar "
       "ibland ytskikt helt. Det tar vi med i kostnadsförslaget från början.",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången för ett kök i Älvsjö",
  "steps": [
    ("Besök och inventering", "Vi ser var stam, kanal och el finns och om det finns spår av ett äldre andra kök."),
    ("Konstruktör vid behov", "Ska en vägg öppnas eller ett bjälklag få hål bedömer en konstruktör det först."),
    ("Kostnadsförslag", "Rivning, installationer och montering redovisas var för sig, med anmälan om den krävs."),
    ("Rivning och pluggning", "Gamla kök tas bort och anslutningar som inte behövs sätts igen."),
    ("Installationer och stomme", "Ny kanal, rör och el dras, ytskikt görs klara och stommen monteras."),
    ("Genomgång", "Vitvaror och fläkt provas och vi går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för köksrenovering i Älvsjö",
  "rot": [
    "Att riva väggar och bygga om planlösningen räknas som rotarbete hos Skatteverket, liksom att dra in vatten "
    "och avlopp och modernisera elen. Köksinredning och vitvaror ger avdrag för arbetet när de monteras i "
    "samband med en omfattande renovering. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person "
    "och år.",
    "Byggstädning efter arbetet ger avdrag, men bortforsling av byggavfall gör det inte. Vi drar avdraget "
    "direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Älvsjö?",
  "price": [
    "Om en ny imkanal behövs och hur den kan dras, om väggen mot matsalen bär, hur många gamla anslutningar "
    "som ska pluggas och hur många lager golv och väggar har. Efter ett gratis platsbesök får du ett skriftligt "
    "kostnadsförslag.",
  ],
  "faq": [
    ("Vår villa i Älvsjö hade en uthyrningsvåning – behöver vi lov för att slå ihop den med resten?",
     "Stockholms stad kräver inget bygglov för att slå samman lägenheter, men en anmälan och ett startbesked "
     "kan behövas. Att i stället dela ett hus i två bostäder kräver bygglov."),
    ("Vad gör ni med det gamla köket på övervåningen?",
     "Vi tar bort inredningen, sätter igen vatten och avlopp där de inte längre behövs och ser till att den "
     "gamla imkanalen antingen används eller tas ur bruk på ett godtagbart sätt."),
    ("Kan spisen flyttas till köksön i en villa från 1910-talet?",
     "Det kräver en ny imkanal eller en lösning som uppfyller kraven för frånluft. Påverkar den nya fläkten "
     "flödena krävs anmälan, och hål i bjälklag ska bedömas av en konsult."),
    ("Hur gamla är rören i en Älvsjövilla?",
     "Det varierar. Området fick vatten och avlopp redan under villastadens första år, och sedan dess har "
     "installationerna ofta bytts i omgångar. Vi kontrollerar det på plats."),
    ("Ger byggstädningen efter köksrenoveringen rotavdrag?",
     "Ja, enligt Skatteverket räknas byggstädning efter avslutat renoveringsarbete som rotarbete. Att forsla "
     "bort byggavfall ger däremot inget avdrag."),
  ],
  "sources": [
    ("Stadsmuseet – S. Lindhagen: Älvsjö villastad, ett exempel på förortsinventering (Stockholmskällan, pdf)", U_ALV),
    ("Stockholms stad – Flytta kök eller badrum", U_STH_FLYTT),
    ("Stockholms stad – Inredning av ytterligare bostad", U_STH_YTTR),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Älvsjö göras om?", "Boka ett gratis besök, så går vi igenom kanal, rör och väggar på plats."),
  "img": [
    ("Renoverat kök med grågröna luckor i en äldre villa i Älvsjö",
     "renovated kitchen in a 1910s Swedish villa, sage green painted cabinet doors with brass knobs, white "
     "stone-look worktop, white tiled wall, tall old window with small panes and deep window sill, view to a "
     "garden with birch trees, light wooden floor, soft daylight, no people, no text"),
    ("Vitt kök med luckor i rak linje och diskho",
     "1910s Swedish suburban villa with white smooth plastered ground floor, dark brown wooden panelling in "
     "the gable, small-paned windows with shutters, steep red clay tile gable roof with a chimney, lilacs and "
     "an old garden, quiet street, no people, no text"),
  ],
  "related": [],
},

# =============================== KÖK SPÅNGA ===============================
"koksrenovering-spanga.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Spånga", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Spånga – Solhem och 60-talets ombyggnader",
  "description": "Köksrenovering i Spånga: villor i Solhem som byggts om på 1960- och 70-talen, asbest i "
                 "kakelfix och golvmattor och vad som gäller vid rivning av gamla kök.",
  "h1": "Köksrenovering i Spånga",
  "lead": "Många villor i Spånga är äldre än de ser ut. Bakom ett kök från 1960- eller 70-talet kan det sitta "
          "material från en tid då asbest var vanligt i byggprodukter. Därför börjar en köksrenovering här ofta "
          "med ett prov. Geal Entreprenad AB gör om kök i Spånga med gratis platsbesök, skriftligt "
          "kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Solhem, villastäder och kök i flera lager.",
  "sections": [
    {"id": "solhem", "anchor": "Solhem",
     "h2": "Solhem – egna hem med en lägenhet i varje",
     "paras": [
       "Enligt artikeln " + X.format(U_SOLHEM, "Ur Hem på landets arkiv") + " bildades AB "
       "Hem på landet 1899, och 1904 började bolaget bygga egnahemskolonin Solhem nära Spånga station på "
       "Västeråsbanan. Samma år planlades 150 tomter söder om järnvägen i kvarter med 10–12 hus i varje.",
       "Styrelsen bestämde sig, med viss tvekan, för att bara bygga en lägenhet i varje hus för att undvika "
       "spekulationsbyggen med uthyrning. Bolagets ingenjör Gunnar Way-Matthiesen granskade ritningarna och "
       "såg till att husen följde bestämmelserna om stugstil, tegeltak och tilltalande färg. Uthusen byggdes "
       "ihop med boningshusen så att tomterna inte skulle belamras.",
       "Vid årsskiftet 1909–1910 fanns 272 villor i Solhem. Samma år blev samhället municipalsamhälle, och "
       "1949 inkorporerades Spånga med Stockholm.",
     ],
     "aside": {"title": "Solhem i årtal", "items": [
       "1904: de första tomterna planläggs",
       "1909: municipalsamhälle",
       "1949: del av Stockholm",
       "1960–70-tal: många villor byggs om"]}},
    {"id": "ombyggnader",
     "h2": "Kök från 1960- och 70-talens ombyggnader",
     "paras": [
       "Artikeln beskriver hur förändringen tog fart på allvar på 1960-talet. Efterfrågan på tomter ledde "
       "till att flera av de stora tomterna styckades, och många av de äldre villorna förändrades kraftigt "
       "genom om- och tillbyggnader under 1960- och 1970-talen. Av de hus som finns på bolagets tidiga "
       "ritningar och fortfarande står kvar är samtliga förändrade: panel har ersatts av eternit eller "
       "lackpanel, och de tätspröjsade fönstren har bytts.",
       "Ett kök i en Solhemsvilla är därför ofta inte husets första, och inte heller det andra. Det som syns i "
       "dag kan vara från en ombyggnad för femtio år sedan, med golvmatta, kakel och lim från samma tid. "
       "Det är just de lagren som behöver undersökas innan något rivs. Vid besöket frågar vi därför om du vet "
       "när köket senast byggdes om, och om det finns ritningar eller kvitton från den ombyggnaden. Det ger en "
       "första bild av vilka material som kan finnas bakom skåpen.",
     ],
     "aside": None},
    {"id": "asbest",
     "h2": "Asbest i kakelfix, golvmattor och fönsterbänkar",
     "paras": [
       "Boverket skriver att " + X.format(U_BV_ASB, "asbest förbjöds inom byggsektorn 1982") + " men att stora "
       "mängder finns kvar i byggnader. Om huset är uppfört mellan 1940 och 1980 är det sannolikt att det finns "
       "asbest någonstans, och den kan också finnas i produkter från tidigare renoveringar. Bland exemplen Boverket listar finns kakel- och klinkerfix och fog, "
       "golv- och väggmattor, lim och skikt under mattor, golvmassor, fönsterbänkar, ventilationskanaler och "
       "gasspisar.",
       "Asbest i bunden form är inte farlig, men när materialet sågas, slipas, borras eller skrapas frigörs "
       "fibrer som kan sväva i luften i många timmar. Det går sällan att se med blotta ögat, och enligt "
       "Boverket är provtagning och analys det enda säkra sättet att veta.",
       "Visar provet asbest ska rivningen göras av ett företag med tillstånd. " + X.format(U_AV_ASB, "Arbetsmiljöverket")
       + " skriver att företag behöver tillstånd för att riva eller sanera asbesthaltigt material, och att "
       "ansökan ska göras åtta veckor innan arbetet ska börja. Det påverkar tidplanen, och därför tar vi "
       "proverna tidigt.",
     ],
     "aside": {"title": "Vanliga ställen i ett gammalt kök", "items": [
       "Fix och fog bakom kaklet",
       "Golvmatta och limmet under",
       "Fönsterbänkar",
       "Ventilationskanaler"]}},
    {"id": "uthuset",
     "h2": "Köket och det gamla uthuset",
     "paras": [
       "Eftersom uthusen i Solhem byggdes ihop med boningshusen ligger det ibland ett förråd eller en gammal "
       "bod vägg i vägg med köket. Att ta ett sådant utrymme i anspråk för att göra köket större ändrar "
       "planlösningen. Enligt " + X.format(U_STH_FLYTT, "Stockholms stad") + " kräver det inget bygglov, men "
       "en anmälan och ett startbesked behövs om bärande konstruktion eller brandskydd påverkas, om "
       "ventilationen ändras väsentligt eller om en ny VA-stam dras i ett nytt schakt.",
       "Ett förråd är sällan isolerat som ett bostadsrum, så golv, väggar och tak behöver ofta byggas om "
       "innan det kan bli en del av köket. Behöver taket över den delen läggas om samtidigt finns mer under "
       + L.format("taklaggare-spanga.html", "takläggare i Spånga") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går vi till väga i Spånga",
  "steps": [
    ("Platsbesök", "Vi går igenom köket, tittar på golv, kakel och fönsterbänkar och ser var stam och kanal går."),
    ("Prov före rivning", "Misstänkta material provas och analyseras innan något bearbetas."),
    ("Skriftligt kostnadsförslag", "Rivning, eventuell sanering, installationer och montering står var för sig."),
    ("Rivning", "Material utan asbest rivs av oss; asbesthaltigt material tas om hand av ett företag med tillstånd."),
    ("Installationer och ytskikt", "Rör, el och kanal dras, och golv och väggar byggs upp."),
    ("Montering och genomgång", "Skåp, bänkskiva och vitvaror monteras och vi går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för kök och asbestsanering i Spånga",
  "rot": [
    "Skatteverket godkänner rotavdrag för asbestsanering när den görs i samband med byggarbete, och för att "
    "montera köksinredning och vitvaror vid en omfattande renovering. Själva provtagningen för asbest ger "
    "däremot inget avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och 75 000 kr tillsammans "
    "med rut. Material ingår inte. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden för ett kök i Spånga?",
  "price": [
    "Mest om proverna visar asbest och hur mycket material som då måste saneras. Därefter om köket ska byggas "
    "ut i ett angränsande utrymme, om en ny kanal behövs och hur många lager golvet har. Du får ett skriftligt "
    "kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Hur vet vi om det finns asbest i köksgolvet i vår villa i Solhem?",
     "Det går sällan att se. Ett prov som analyseras är det enda säkra sättet, och det tas innan golvmatta, "
     "lim eller golvmassa bearbetas."),
    ("Får vi riva det gamla kakelfixet själva?",
     "Arbetsmiljöverkets regler gäller yrkesmässig hantering, men miljöbalkens hänsynsregler gäller även "
     "privatpersoner. Du måste då skaffa tillräcklig kunskap och skydda dig och andra. Visar provet asbest "
     "rekommenderar vi att ett företag med tillstånd gör rivningen."),
    ("Hur påverkar ett positivt asbestprov tidplanen?",
     "Ett företag som ska riva asbest behöver tillstånd från Arbetsmiljöverket och ska ansöka åtta veckor "
     "innan arbetet börjar. Därför tar vi proverna tidigt."),
    ("Kan köket byggas ut in i förrådet som sitter ihop med huset?",
     "Ofta, men förrådet behöver isoleras som ett bostadsrum, och påverkas bärande delar eller brandskydd krävs "
     "anmälan och startbesked."),
    ("Varför liknar vår villa i Spånga inte originalritningen?",
     "Många äldre villor i Solhem byggdes om kraftigt på 1960- och 70-talen. Panel, fönster och planlösning "
     "har ofta ändrats sedan dess."),
  ],
  "sources": [
    ("Stadsmuseet – J. Ferenius och L. Johannesson: Ur Hem på landets arkiv (Stockholmskällan, pdf)", U_SOLHEM),
    ("Boverket – Risker med hantering av asbest i byggnader", U_BV_ASB),
    ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest", U_AV_ASB),
    ("Stockholms stad – Flytta kök eller badrum", U_STH_FLYTT),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Spånga rivas och göras om?", "Boka ett gratis besök, så går vi igenom material, prover och planlösning på plats."),
  "img": [
    ("Nyrenoverat kök med mörkblå luckor och ljus bänkskiva i en villa i Spånga",
     "newly renovated kitchen in an old Swedish villa, dark blue flat cabinet doors, light grey stone-look "
     "worktop, white square wall tiles, oak floor, window with white frame facing a green garden, built-in "
     "oven in a tall cabinet, soft daylight, no people, no text"),
    ("Gammalt kök från 1970-talet inför rivning, med skyddsplast på den gamla golvmattan",
     "empty old 1970s Swedish villa kitchen after the cabinets have been removed, bare wall with remains of grey "
     "tile adhesive where tiles were taken down, old beige patterned vinyl floor sheet still on the floor, capped "
     "water pipes sticking out of the wall, clean swept room, plastic sheeting over the doorway, daylight from a "
     "window, no tools, no cans, no people, no hands, no text"),
  ],
  "related": [],
},

# =============================== KÖK BOTKYRKA ===============================
"koksrenovering-botkyrka.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Botkyrka", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Botkyrka – kök för att bo kvar i villan",
  "description": "Köksrenovering i Botkyrka: kök för att bo kvar i villan, bostadsanpassningsbidrag och "
                 "spisvakt, imkanal enligt kommunen och fläktrör över radhusvinden.",
  "h1": "Köksrenovering i Botkyrka",
  "lead": "I Tullinge är knappt var tionde bostad en hyresrätt, så den som vill bo kvar när åren går gör det "
          "ofta genom att anpassa sitt eget hus. Köket är ett av de rum där det märks mest. Geal "
          "Entreprenad AB gör om kök i Tullinge, Tumba och övriga Botkyrka, med gratis platsbesök, skriftligt "
          "kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Kök i villor och radhus, för att bo kvar.",
  "sections": [
    {"id": "bo-kvar", "anchor": "Bo kvar i villan",
     "h2": "Ett kök som gör det lättare att bo kvar",
     "paras": [
       "Kommunens utvecklingsprogram " + X.format(U_BOT_TUL, "Framtid för Tullinge") + " från 2010 konstaterar "
       "att bostadsutbudet i Tullinge bara till knappt 10 procent består av hyresrätter. Programmet nämner "
       "äldre som vill flytta från villan till ett bekvämare boende, och att det byggs många bostäder i "
       "stadsdelen, mest spridda enskilda småhus.",
       "När det är ont om andra boendeformer blir det vanligare att man i stället anpassar huset man redan "
       "har. I köket handlar det om arbetshöjder, om att ha det man använder mest mellan höft- och axelhöjd, "
       "om bra belysning över bänken och om utrymme att röra sig mellan skåpen. Det mesta av det är "
       "planering och kostar lite extra om det görs samtidigt med en renovering.",
       "Vi frågar därför tidigt hur länge du räknar med att bo kvar och vem som lagar mat. Ett kök som "
       "fungerar om tjugo år ser ofta likadant ut som ett annat kök, men med skåp, belysning och el placerade "
       "på ett annat sätt.",
     ],
     "aside": {"title": "Planera för att bo kvar", "items": [
       "Diskmaskin och ugn i arbetshöjd",
       "Lådor i stället för djupa skåp",
       "Ljus över hela arbetsytan",
       "Fri yta framför spisen"]}},
    {"id": "anpassning",
     "h2": "Bostadsanpassningsbidrag – och vad det inte täcker",
     "paras": [
       "Botkyrka kommun ger " + X.format(U_BOT_BAB, "bidrag för att anpassa bostaden") + " till den som har "
       "en bestående funktionsnedsättning och behöver anpassa sin permanenta bostad. Behovet ska styrkas med "
       "ett intyg från till exempel en arbetsterapeut, och det ska finnas ett direkt samband mellan "
       "anpassningen och funktionsnedsättningen. Bidraget kan inte användas till normalt underhåll eller "
       "renovering.",
       "Vid enklare anpassningar, som installation av en spisvakt, krävs ingen offert. Vid större åtgärder "
       "ska du vända dig till bostadsanpassningen innan du tar in en offert, så att kommunen kan kontrollera "
       "att företaget är seriöst. Kommunen skriver att bidraget annars riskerar att inte betalas ut. Det är "
       "du som beställer arbetet, och konsumenttjänstlagen gäller mellan dig och entreprenören.",
       "Görs anpassningen samtidigt som köket renoveras behöver de två delarna hållas isär. Skatteverket "
       "skriver att du inte kan få rotavdrag för arbete som du får bidrag eller annat ekonomiskt stöd för från "
       "kommunen. Vi delar därför upp kostnadsförslaget så att det syns vad som är anpassning och vad som är "
       "renovering.",
     ],
     "aside": None},
    {"id": "imkanal-bot",
     "h2": "Imkanal, bjälklag och stam enligt kommunen",
     "paras": [
       "På kommunens sida om " + X.format(U_BOT_FLYTT, "flytt av kök eller badrum") + " står att det ska finnas "
       "en imkanal i ett matlagningsutrymme för att kraven på frånluft ska uppfyllas. Att använda den "
       "befintliga imkanalen i köket ses inte som en väsentlig ändring av ventilationen och kräver ingen "
       "anmälan, men nya aggregat, fläktar eller kanaler som påverkar flöden eller luftkvalitet gör det.",
       "Kommunen tar också upp håltagning i bjälklag: är du osäker på om ett hål påverkar den bärande "
       "konstruktionen ska en konstruktör bedöma det, och berörs bärande delar krävs anmälan. En ny VA-stam i "
       "ett nytt schakt är en väsentlig ändring, medan rördragning för att ansluta till en befintlig stam "
       "normalt inte är anmälningspliktig.",
       "Kommunen påpekar att sidan håller på att uppdateras efter de nya bygglovsreglerna från den 1 december "
       "2025. Vi stämmer därför av med kommunen när ett kök ska flyttas längre bort från stammen.",
     ],
     "aside": {"title": "Kräver anmälan i Botkyrka", "items": [
       "Hål i bärande bjälklag eller vägg",
       "Ny fläkt eller kanal som ändrar flödena",
       "Ny VA-stam i nytt schakt",
       "Två lägenheter som slås ihop"]}},
    {"id": "radhus-bot",
     "h2": "Fläktröret genom radhusvinden",
     "paras": [
       "" + X.format(U_SBFF_OM, "Södertörns brandförsvarsförbund") + ", som ansvarar för räddningstjänsten i Botkyrka, beskriver på sin sida om "
       + X.format(U_SBFF_RAD, "brandskydd i radhus") + " att byggreglerna kräver att en brand inte ska kunna "
       "spridas mellan lägenheter inom 60 minuter, men att många radhus har brister som gör att den sprids "
       "fortare än så. En orsak är genomföringar för antennkablar och ventilationsrör som gjorts i efterhand och "
       "inte tätats rätt.",
       "Förbundet rekommenderar att genomföringar och hål tätas med brandklassad tätningsmassa och påpekar att "
       "det är fastighetsägarens ansvar att se över brandskyddet. När en ny köksfläkt i ett radhus får ett rör "
       "som går över vinden ser vi till att det inte passerar den avskiljande väggen mot grannen och att "
       "genomföringen genom bjälklaget blir tät.",
       "Ska röret ut genom taket görs genomföringen så att taket förblir tätt; läs mer under "
       + L.format("taklaggare-botkyrka.html", "takläggare i Botkyrka") + ". Ska badrummet göras om samtidigt, se "
       + L.format("badrumsrenovering-botkyrka.html", "badrumsrenovering i Botkyrka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till i Botkyrka",
  "steps": [
    ("Platsbesök", "Vi mäter köket, ser var stam och imkanal går och pratar om hur köket ska fungera på sikt."),
    ("Bidrag och anmälan", "Söker du bostadsanpassningsbidrag tar du kontakt med kommunen innan offerten tas fram."),
    ("Skriftligt kostnadsförslag", "Anpassning och renovering redovisas var för sig, liksom arbete och material."),
    ("Rivning och installationer", "Gamla skåp tas bort och rör, el och fläkt dras enligt den nya planen."),
    ("Montering", "Stomme, bänkskiva och vitvaror monteras på de höjder vi bestämt tillsammans."),
    ("Genomgång", "Vi provar fläkt, spis och belysning och går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag och bidrag för köket i Botkyrka",
  "rot": [
    "Att montera köksinredning och vitvaror vid en omfattande renovering, modernisera elen och dra vatten och "
    "avlopp ger rotavdrag i ett småhus. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person "
    "och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Arbete som betalas med bostadsanpassningsbidrag ger inget rotavdrag. Vi skriver anpassning, renovering och "
    "material var för sig och drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Botkyrka?",
  "price": [
    "Om köket stannar vid stammen och den befintliga imkanalen, om skåp och vitvaror ska placeras på nya "
    "höjder, hur mycket ny el som behövs och om en fläktkanal ska dras över vinden i ett radhus. Efter ett "
    "gratis besök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi få bidrag för en spisvakt i Botkyrka?",
     "Har du en bestående funktionsnedsättning kan en spisvakt ingå i bostadsanpassningsbidraget. Kommunen "
     "skriver att en sådan enklare anpassning inte kräver någon offert."),
    ("Täcker bostadsanpassningsbidraget ett helt nytt kök?",
     "Nej. Bidraget gäller åtgärder som behövs på grund av funktionsnedsättningen och kan inte användas till "
     "normalt underhåll eller renovering."),
    ("Får vi rotavdrag för den del av köket som kommunen betalar?",
     "Nej. Skatteverket ger inget rotavdrag för arbete som du får bidrag för från kommunen, men resten av "
     "renoveringen kan ge avdrag."),
    ("Behöver vi göra en anmälan om den nya fläkten kopplas till den gamla imkanalen?",
     "Enligt Botkyrka kommun är det inte en väsentlig ändring att använda befintlig imkanal. Ett nytt aggregat "
     "eller nya kanaler som påverkar flödena kräver däremot anmälan."),
    ("Vad ska vi tänka på när fläktröret dras över vinden i ett radhus i Tumba?",
     "Att röret inte går genom den avskiljande väggen mot grannen och att alla genomföringar tätas med "
     "brandklassad massa, så som Södertörns brandförsvarsförbund rekommenderar."),
  ],
  "sources": [
    ("Botkyrka kommun – Framtid för Tullinge, utvecklingsprogram 2010 (pdf)", U_BOT_TUL),
    ("Botkyrka kommun – Bidrag för att anpassa bostaden", U_BOT_BAB),
    ("Botkyrka kommun – Flytt av kök eller badrum", U_BOT_FLYTT),
    ("Södertörns brandförsvarsförbund – Radhus", U_SBFF_RAD),
    ("Södertörns brandförsvarsförbund – Om oss", U_SBFF_OM),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Botkyrka fungera i många år till?", "Boka ett gratis besök, så går vi igenom höjder, fläkt och el på plats."),
  "img": [
    ("Ljust villakök med ugn i arbetshöjd och lådor under bänken i Botkyrka",
     "bright renovated kitchen in a Swedish 1970s villa, light birch cabinet fronts, wall oven and microwave "
     "built into tall cabinets at waist height, deep drawers under a white worktop, under-cabinet LED lighting, "
     "induction hob, window towards a lawn and pine trees, no people, no text"),
    ("Vitt kök med köksfläkt och fönster över bänken",
     "row of 1970s Swedish two-storey terraced houses with dark brown wooden facades and grey concrete tile "
     "roofs with small metal vent hoods on the roof, small front gardens with hedges, pine forest behind, "
     "overcast day, no people, no text"),
  ],
  "related": [],
},

# =============================== KÖK UPPLANDS VÄSBY ===============================
"koksrenovering-upplands-vasby.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Upplands Väsby", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Upplands Väsby – radhus och nya byggregler",
  "description": "Köksrenovering i Upplands Väsby: radhus, kedjehus och atriumhus från 1960–70-talen, Boverkets "
                 "nya byggregler och vad du själv får göra med elen i köket.",
  "h1": "Köksrenovering i Upplands Väsby",
  "lead": "Väsbys östra delar byggdes med radhus, kedjehus och atriumhus i enhetliga grupper, och många av köken "
          "är nu lika gamla som husen. Sedan sommaren 2026 gäller dessutom bara Boverkets nya byggregler. Geal "
          "Entreprenad AB gör om kök i Upplands Väsby med gratis platsbesök, skriftligt kostnadsförslag och "
          "ROT-avdraget direkt på fakturan.",
  "card": "Radhus, kedjehus och atriumhus.",
  "sections": [
    {"id": "husgrupperna", "anchor": "Radhus och atriumhus",
     "h2": "Radhus, kedjehus och atriumhus i grupper",
     "paras": [
       "Kommunens " + X.format(U_UV_KM, "kunskapsunderlag för kulturmiljö") + " beskriver hur de östra "
       "kommundelarna vuxit fram med en stor andel småhus och radhus, placerade som separata enklaver längs "
       "säckgator. Husen har en eller två våningar, ibland två våningar i suterräng, och platta eller flacka "
       "tak. Exempel finns i Sjukyrkoberget, Skälby, Fresta och Odenslunda, men också i Apoteksskogen.",
       "Underlaget betonar att grupperna är olika sinsemellan men enhetligt utförda inom varje grupp. För ett "
       "kök betyder det ofta att planlösningen är densamma i hela längan: köket ligger på samma ställe, med "
       "samma mått och samma dragning av stam och frånluft. Det gör det lättare att förutse vad som finns "
       "bakom skåpen.",
       "Vägledningen i underlaget säger att tillbyggnader som bryter ursprungsvolymen bör undvikas. Ett större "
       "kök får därför oftast hittas inne i huset, till exempel genom att öppna mot matplatsen eller flytta en "
       "lätt mellanvägg, snarare än genom en utbyggnad mot gatan.",
     ],
     "aside": {"title": "Typiskt för husgrupperna", "items": [
       "En till två våningar",
       "Platta eller flacka tak",
       "Tegel mot målat trä i fasaden",
       "Samma planlösning i hela längan"]}},
    {"id": "byggregler",
     "h2": "Boverkets nya byggregler gäller nu fullt ut",
     "paras": [
       "Upplands Väsby kommun skriver att " + X.format(U_UV_BBR, "Boverkets nya byggregler") + " trädde i kraft "
       "den 1 juli 2025 och ersatte de tidigare byggreglerna BBR och EKS. Under en övergångsperiod till och med "
       "den 30 juni 2026 gick det att välja det gamla eller det nya regelverket. Efter den 1 juli 2026 gäller "
       "bara de nya reglerna.",
       "De nya reglerna är funktionsbaserade. De anger vad byggnaden ska klara, inte hur den ska byggas, och "
       "kommunen påpekar att byggherren ska kunna visa hur kraven uppfylls, till exempel med teknisk "
       "dokumentation, intyg eller beräkningar. I en anmälan ska du ange vilket regelverk du följer.",
       "För ett kök märks det främst när arbetet kräver anmälan, till exempel en ny fläkt som ändrar flödena "
       "eller en ändring i bärande konstruktion. Då samlar vi produktblad och beskrivningar så att du har "
       "underlaget som kommunen kan be om.",
     ],
     "aside": None},
    {"id": "elen-uv",
     "h2": "Elen i köket – vad du får göra själv",
     "paras": [
       "Elsäkerhetsverket skriver att " + X.format(U_ELS_SJ, "de flesta elinstallationsarbeten") + " ska utföras "
       "av ett registrerat elinstallationsföretag, och att förändringar i den fasta installationen, till "
       "exempel ett nytt uttag i köket eller elledningar i väggarna, ska göras av ett sådant företag. Att byta "
       "ett ojordat vägguttag mot ett jordat får du inte heller göra själv.",
       "Det du får göra med rätt kunskap är bland annat att byta glödlampor, lamphållare och en fast ansluten "
       "ljusarmatur i torra utrymmen, och att byta ett befintligt uttag eller en strömbrytare på högst 16 A i "
       "egen dosa. Att fast ansluta en elektrisk produkt till anläggningen, till exempel en fast ansluten spis, räknas däremot som elinstallationsarbete.",
       "Innan du anlitar ett elföretag ska du enligt " + X.format(U_ELS_AN, "Elsäkerhetsverket") + " kontrollera "
       "att det är registrerat hos myndigheten, vilket går att göra i tjänsten Kolla elföretaget. Vi samordnar "
       "elarbetet i köket med snickeri och VVS så att allt görs i rätt ordning.",
     ],
     "aside": {"title": "Elen i köket", "items": [
       "Nya uttag: registrerat elföretag",
       "Fast ansluten spis: registrerat elföretag",
       "Byta lampa eller armatur: får du själv",
       "Kontrollera i Kolla elföretaget"]}},
    {"id": "utbyggnad-uv",
     "h2": "Om köket ändå ska byggas ut",
     "paras": [
       "Enligt kommunens sida om " + X.format(U_UV_TILL, "tillbyggnad") + " krävs inget bygglov för en "
       "tillbyggnad om alla lovfria tillbyggnader på tomten tillsammans är högst 30 kvadratmeter, om den inte "
       "går över taknocken och om den ligger minst 4,5 meter från tomtgränsen. Med grannens skriftliga "
       "medgivande får den ligga närmare.",
       "Bygglov krävs om byggnaden är kulturhistoriskt värdefull eller ligger i ett kulturhistoriskt särskilt "
       "värdefullt område. Kunskapsunderlaget pekar till exempel ut villorna och radhusen längs Oxundavägen "
       "som ett särskilt värdefullt bebyggelseområde. Även när tillbyggnaden är lovfri kan anmälan krävas för "
       "ingrepp i bärande stomme och för nya installationer för vatten, avlopp och ventilation.",
       "För husen med platta tak är det dessutom klokt att planera var köksfläktens kanal ska gå ut innan "
       "tillbyggnaden ritas. Mer om taken finns under " + L.format("taklaggare-upplands-vasby.html", "takläggare i Upplands Väsby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till i Upplands Väsby",
  "steps": [
    ("Platsbesök", "Vi mäter köket och ser var stam, frånluft och el finns i just din hustyp."),
    ("Regler och anmälan", "Vi bedömer om något i planen kräver anmälan och vilket underlag som då behövs."),
    ("Skriftligt kostnadsförslag", "Rivning, el, VVS, snickeri och montering redovisas var för sig."),
    ("Rivning och installationer", "Gamla skåp tas bort och el, rör och fläkt dras enligt den nya planen."),
    ("Ytskikt och stomme", "Golv och väggar görs klara och stommen monteras."),
    ("Inkoppling och genomgång", "Spis och vitvaror ansluts av elföretaget och vi går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för köket i Upplands Väsby",
  "rot": [
    "Skatteverket räknar det som rotarbete att modernisera elen, till exempel att byta och installera vägguttag "
    "och elcentraler och montera inbyggda spotlights. Även köksinredning och vitvaror ger avdrag när de "
    "monteras vid en omfattande renovering. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per "
    "person och år.",
    "Är huset yngre än fem år gäller särskilda regler. Material ger inget avdrag, och vi drar avdraget direkt "
    "på fakturan.",
  ],
  "price_h2": "Vad styr priset i Upplands Väsby?",
  "price": [
    "Om köket stannar på samma plats i planen, hur mycket av elen som behöver förnyas, om en mellanvägg ska "
    "flyttas och om fläktkanalen behöver en ny väg ut genom ett platt tak. Efter ett gratis besök får du ett "
    "skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka byggregler gäller för vår köksrenovering i Upplands Väsby?",
     "Sedan den 1 juli 2026 gäller bara Boverkets nya byggregler. Under övergångsperioden fram till den 30 juni "
     "2026 gick det att välja det gamla regelverket."),
    ("Får jag själv sätta upp den nya taklampan i köket?",
     "Elsäkerhetsverket tillåter att du byter en fast ansluten ljusarmatur i torra utrymmen om du har rätt "
     "kunskap. Nya uttag och ledningar i väggen ska däremot göras av ett registrerat elinstallationsföretag."),
    ("Hur kontrollerar vi att elfirman är registrerad?",
     "Elsäkerhetsverket har tjänsten Kolla elföretaget. Ett företag som inte är registrerat arbetar olagligt "
     "och ska inte anlitas."),
    ("Kan köket i ett atriumhus byggas ut mot gården?",
     "En lovfri tillbyggnad får vara högst 30 kvadratmeter och ligga minst 4,5 meter från tomtgränsen, eller "
     "närmare med grannens skriftliga medgivande. I ett särskilt värdefullt område krävs bygglov."),
    ("Ingår det i rotavdraget att flytta uttagen i köket?",
     "Ja. Skatteverket räknar byte och installation av vägguttag som rotarbete när det gäller modernisering av "
     "elen i bostaden."),
  ],
  "sources": [
    ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö (pdf)", U_UV_KM),
    ("Upplands Väsby kommun – Nya byggregler från 1 juli 2025", U_UV_BBR),
    ("Upplands Väsby kommun – Tillbyggnad", U_UV_TILL),
    ("Elsäkerhetsverket – Vad får jag göra själv med el?", U_ELS_SJ),
    ("Elsäkerhetsverket – Anlita ett elinstallationsföretag", U_ELS_AN),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska radhusköket i Väsby bli nytt?", "Boka ett gratis besök, så går vi igenom el, fläkt och planlösning på plats."),
  "img": [
    ("Modernt kök med vita luckor och ekbänkskiva i ett radhus i Upplands Väsby",
     "modern renovated kitchen in a 1970s Swedish terraced house, white matte handleless cabinets, oak "
     "worktop, black tap, large window without glazing bars towards a small fenced patio, several new wall "
     "sockets above the worktop, pendant lamps over a small dining table, no people, no text"),
    ("Radhus med platta tak och fasad av rött tegel och målat trä i Upplands Väsby",
     "row of low 1970s Swedish single-storey terraced houses with completely flat roofs and a thick dark fascia "
     "along the roof edge, no pitched roofs, no chimneys, facades of red brick combined with horizontal wooden "
     "panelling painted ochre, small gardens behind low wooden fences, car-free gravel footpath in front, "
     "birch trees, no cars, no people, no text"),
  ],
  "related": [],
},

# =============================== KÖK VALLENTUNA ===============================
"koksrenovering-vallentuna.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Vallentuna", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Vallentuna – utbyggt kök och vedspis",
  "description": "Köksrenovering i Vallentuna: bygga ut köket lovfritt enligt reglerna från 1 december 2025, "
                 "närhet till Roslagsbanan och anmälan för vedspis i köket.",
  "h1": "Köksrenovering i Vallentuna",
  "lead": "I Vallentuna är det ofta tomten som ger utrymme, inte huset. Ett större kök blir då en tillbyggnad, "
          "och sedan den 1 december 2025 gäller nya regler för vad som går att bygga utan lov. Geal Entreprenad "
          "AB gör om och bygger ut kök i Vallentuna, med gratis platsbesök, skriftligt kostnadsförslag och "
          "ROT-avdraget direkt på fakturan.",
  "card": "Utbyggda kök, villor och gårdar.",
  "sections": [
    {"id": "bygga-ut", "anchor": "Bygga ut köket",
     "h2": "Bygga ut köket utan bygglov",
     "paras": [
       "Vallentuna kommun beskriver på sidan om " + X.format(U_VAL_TILL, "tillbyggnad av en- och tvåbostadshus")
       + " vad som gäller efter lagändringen. En tillbyggnad får vara högst 30 kvadratmeter i brutto- eller "
       "öppenarea, och då räknas alla tidigare och nya lovfria tillbyggnader på huset ihop. Den får inte vara "
       "högre än husets taknock och ska ligga minst 4,5 meter från tomtgränsen mot granne, samfällighet eller "
       "gata. Vill du bygga närmare krävs skriftligt medgivande från de berörda.",
       "Ligger fastigheten i ett kulturhistoriskt särskilt värdefullt område krävs bygglov oavsett storlek. "
       "Kommunen påpekar också att tillbyggnaden kan kräva anmälan och startbesked trots att den är lovfri, "
       "till exempel om vatten och avlopp eller ventilation installeras i den. För ett kök blir det "
       "aktuellt så snart diskbänken eller fläkten flyttar ut i den nya delen.",
       "Har huset redan en tidigare attefallstillbyggnad eller ett skärmtak räknas de in i de 30 "
       "kvadratmetrarna. Vi mäter därför upp det som redan finns innan vi föreslår hur stor köksdelen kan bli.",
     ],
     "aside": {"title": "Lovfri tillbyggnad", "items": [
       "Högst 30 m² sammanlagt",
       "Inte över taknocken",
       "Minst 4,5 m från tomtgräns",
       "Anmälan för VA och ventilation"]}},
    {"id": "nya-reglerna",
     "h2": "Vad lagändringen 1 december 2025 betyder för köket",
     "paras": [
       "Boverkets " + X.format(U_BV_PBL, "lista över PBL-ändringarna") + " visar att friggebod och attefallshus "
       "har ersatts av bygglovsbefriad komplementbyggnad och komplementbostadshus. Ett komplementbostadshus "
       "kräver bygglov om det är större än 30 kvadratmeter inom detaljplan eller 50 kvadratmeter utanför, och "
       "varje tomt har en gemensam pott på 45 respektive 65 kvadratmeter för sådana byggnader.",
       "Boverket skriver också att många åtgärder som tidigare krävde anmälan, till exempel attefallshus, inte "
       "längre kräver anmälan för själva byggnaden. Men eftersom vatten, avlopp och ventilation fortfarande är "
       "anmälningspliktiga krävs en anmälan för installationerna. Ett kök i ett gästhus på tomten behöver "
       "alltså anmälas även när huset i sig är lovfritt.",
     ],
     "aside": None},
    {"id": "roslagsbanan",
     "h2": "Villor nära Roslagsbanan",
     "paras": [
       "Enligt kommunens " + X.format(U_VAL_OP, "översiktsplan 2040") + " började en ny tid 1885 när "
       "Roslagsbanan invigdes mellan Stockholm och Rimbo. Stationerna blev mötesplatser och stationssamhällen "
       "växte fram med villabebyggelse, och i dag har banan fem stationer i kommunen.",
       "För den som bor nära spåret finns en särskild regel. Boverket skriver att bygglov krävs för en annars "
       "lovfri tillbyggnad om den görs närmare än 30 meter från ett järnvägsspårs mitt. Undantag finns om "
       "infrastrukturförvaltaren skriftligen har medgett åtgärden. En köksutbyggnad på baksidan av en villa vid "
       "en station kan alltså behöva bygglov även om den är liten.",
       "Vi mäter avståndet tidigt, så att du vet om det blir en lovansökan innan ritningarna görs klara. Ska "
       "huset samtidigt få ny fasad där köket byggs till, se " + L.format("fasadrenovering-vallentuna.html", "fasadrenovering i Vallentuna") + ".",
     ],
     "aside": {"title": "Kontrollera före ritning", "items": [
       "Avstånd till tomtgräns",
       "Avstånd till spårets mitt",
       "Tidigare lovfria tillbyggnader",
       "Kulturhistoriskt värdefullt område?"]}},
    {"id": "vedspis",
     "h2": "Vedspis eller spisinsats i köket",
     "paras": [
       "I ett hus på landet vill många ha en vedspis eller en braskamin i köket. Vallentuna kommun skriver att "
       "det krävs " + X.format(U_VAL_ELD, "en anmälan när en eldstad installeras") + ", och att det gäller även "
       "vid byte till en annan typ av eldstad eller från öppen spis till spisinsats. Installationen får inte "
       "börja förrän kommunen gett startbesked.",
       "Innan eldstaden används ska du ha ett slutbesked. Det får du när en ifylld kontrollplan och ett "
       "sotarintyg utan anmärkningar har lämnats in till kommunen. Bygglov krävs om en ny skorsten ska sitta "
       "på fasaden eller om en befintlig utanpåliggande skorsten ska ändras.",
       "Bland de " + X.format(U_VAL_ANM, "anmälningspliktiga åtgärderna") + " räknar kommunen också ändringar som "
       "väsentligt påverkar bärande delar eller brandskydd, och nya eller ändrade installationer för ventilation, "
       "vatten och avlopp. Planerar du både vedspis och köksfläkt tar vi med båda i samma anmälan.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går vi till väga i Vallentuna",
  "steps": [
    ("Platsbesök", "Vi mäter köket, tomten och avstånden och ser vad som redan byggts lovfritt."),
    ("Lov eller anmälan", "Vi bedömer om tillbyggnaden kräver lov och vilka installationer som ska anmälas."),
    ("Skriftligt kostnadsförslag", "Tillbyggnad, kök och eventuell eldstad redovisas var för sig."),
    ("Startbesked", "Arbetet med installationerna börjar när kommunen har gett startbesked."),
    ("Bygge och montering", "Tillbyggnaden byggs, rör, el och fläkt dras och köket monteras."),
    ("Slutbesked och genomgång", "Kontrollplan och sotarintyg lämnas in där det krävs och vi går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för köket i Vallentuna",
  "rot": [
    "Rotavdrag gäller arbete i en bostad du äger och bor i, även en fritidsbostad. Montering av köksinredning "
    "och vitvaror i samband med omfattande byggarbete, liksom ny el och nya avlopp, räknas som rotarbete. "
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år.",
    "Materialet ger inget avdrag. Vi skriver arbete och material var för sig och drar avdraget direkt på "
    "fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Vallentuna?",
  "price": [
    "Om köket stannar i huset eller byggs ut, hur grundläggningen för en tillbyggnad ska göras, om vatten och "
    "avlopp ska förlängas och om en eldstad med skorsten ingår. Efter ett gratis platsbesök får du ett "
    "skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur stor köksutbyggnad får vi göra utan bygglov i Vallentuna?",
     "Högst 30 kvadratmeter sammanlagt med husets tidigare lovfria tillbyggnader, inte över taknocken och minst "
     "4,5 meter från tomtgränsen, om inte grannen skriftligen medgett något annat."),
    ("Vår villa ligger nära Roslagsbanan – påverkar det utbyggnaden?",
     "Ja, om tillbyggnaden hamnar närmare än 30 meter från spårets mitt krävs bygglov, om inte "
     "infrastrukturförvaltaren skriftligen har medgett åtgärden."),
    ("Behöver köket i gästhuset på tomten anmälas?",
     "Själva komplementbostadshuset kräver ingen anmälan om det är lovfritt, men installationer för vatten, "
     "avlopp och ventilation gör det."),
    ("När får vi börja elda i den nya vedspisen?",
     "Först när kommunen har gett slutbesked, vilket kräver en ifylld kontrollplan och ett sotarintyg utan "
     "anmärkningar."),
    ("Räknas vårt gamla skärmtak in i ytan för köksutbyggnaden?",
     "Ja. Alla tidigare och nya lovfria tillbyggnader på huset räknas ihop, och tillsammans får de vara högst "
     "30 kvadratmeter."),
  ],
  "sources": [
    ("Vallentuna kommun – Tillbyggnad av en- och tvåbostadshus", U_VAL_TILL),
    ("Vallentuna kommun – Eldstad", U_VAL_ELD),
    ("Vallentuna kommun – Anmälningspliktiga åtgärder", U_VAL_ANM),
    ("Vallentuna kommun – Översiktsplan 2040 (pdf)", U_VAL_OP),
    S_BV_PBL, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Vallentuna bli större?", "Boka ett gratis besök, så mäter vi upp tomt, avstånd och kök tillsammans."),
  "img": [
    ("Stort kök i en nybyggd tillbyggnad med glaspartier mot trädgården i Vallentuna",
     "spacious new kitchen in a single-storey timber extension of a Swedish villa, light grey cabinets, long "
     "kitchen island with oak top, large windows and a glass door towards a lawn and open fields, black "
     "cast-iron wood-burning cook stove standing on a stone hearth in the corner, soft daylight, no people, no text"),
    ("Tvåvåningsvilla med en ny lägre tillbyggnad med stora fönster i Vallentuna",
     "back side of a 1980s Swedish two-storey light yellow wooden villa with red concrete tile gable roof, and "
     "attached to it a clearly newer low single-storey extension with a flat-pitched dark metal roof and large "
     "windows, the extension is much lower than the main house, lawn and birches, early autumn, "
     "no people, no text"),
  ],
  "related": [],
},

}
