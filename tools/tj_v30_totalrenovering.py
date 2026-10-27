# -*- coding: utf-8 -*-
"""Totalrenovering – ortsidor v30: Hägersten, Sigtuna, Sundbyberg, Upplands Väsby, Vällingby, Älvsjö (2026-10-27).
Tjänst under villarenovering.html (TJ_HUB["totalrenovering"]). Intent: renovera hela huset eller lägenheten på en gång –
skild från ortens byggforetag-/tillbyggnad-sidor och från enskilda rum (badrums-/köksrenovering), som länkas.
Tre bilder per sida: img[0] hero 4:3, img[1]–[2] 3:2.

Lokal vinkel per sida:
Hägersten – två sorters hem: villorna i Mälarhöjden (villastad, privat initiativ, kulturhistoriskt värdefull miljö
  enligt Varsam) och lägenheterna på Hägerstensåsen (planlösning, anmälan, föreningens tillstånd), asbest 1940–1970.
Sigtuna – ventilation (anmälan och handlingar), VA (när en ändring är väsentlig, SIVAB, enskilt avlopp), Sigtuna stads
  kulturmiljö (ursprungliga material), när renoveringen blir en tillbyggnad inom Arlandas influensområde.
Sundbyberg – Duvbos villor inifrån (riksintresse 1987, utökad lovplikt för yttre utseende och solceller, gratis
  konsultationsmöte), fasadernas material enligt miljöprogrammet, kamin och skorsten, byggetablering på stadens mark.
Upplands Väsby – kunskapsunderlaget för kulturmiljö: äldre villaområden före 1960 och radhus/kedjehus 1960–70,
  varsamhetskravet gäller även invändigt, dagvatten och dränering får inte kopplas till spillvattnet.
Vällingby – riksintresset AB 120 (ABC-staden, ursprungliga detaljer), bostäderna i Vällingby enligt områdesfakta,
  eternit och asbest, bostadsrätten och föreningens tillstånd.
Älvsjö – Älvsjö villastad (Hallmans stadsplan, municipalsamhälle, Stadsmuseets inventering av exteriörer), elen
  (Elsäkerhetsverket), kök och ventilation, det som syns från gatan.

Fakta endast från källorna i respektive 'sources', öppnade med curl (Mozilla-UA) 2026-10-27, alla 200; pdf:erna har
textlager (Älvsjö-inventeringen är OCR men läsbar i de använda styckena). Skatteverkets sidor återställde
anslutningen härifrån – samma URL:er och ROT-formuleringar som v23–v29.
Strukna / ej använda: avgifter, handläggningstider, byggår för enskilda kvarter som inte står i källorna,
alla priser, garantier, omdömen och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_S = "https://bygglov.stockholm/nar-behovs-bygglov/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_RIKS = ("Stockholms stad – Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_PLAN = ("Stockholms stad – Ändra planlösningen i en byggnad", _S + "andra-inomhus/andra-planlosningen-i-en-byggnad/")
_FLYTTA = ("Stockholms stad – Flytta kök eller badrum", _S + "andra-inomhus/flytta-kok-eller-badrum/")
_FASAD = ("Stockholms stad – Fasadändring", _S + "andra-byggnads-yttre-utseende/fasadandring/")
_ASB = ("Boverket – Asbest", "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_EL = ("Elsäkerhetsverket – Bygga och renovera", "https://www.elsakerhetsverket.se/privatpersoner/din-elanlaggning/bygga-och-renovera")
_ALVINV = ("Stadsmuseet – Älvsjö villastad, ett exempel på förortsinventering (Stockholmskällan, pdf)",
           "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf")
_SIG = "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/"
_SIG_VENT = ("Sigtuna kommun – Installation eller ändring av ventilation",
             _SIG + "vad-ska-du-bygga/andra-befintlig-byggnad/installation-eller-andring-av-ventilation.html")
_SIG_VA = ("Sigtuna kommun – Vatten och avlopp", _SIG + "vad-ska-du-bygga/andra-befintlig-byggnad/vatten-och-avlopp.html")
_SIG_KULT = ("Sigtuna kommun – Bygga i kulturmiljö", _SIG + "var-far-du-bygga/bygga-i-kulturmiljo.html")
_SIG_FLYG = ("Sigtuna kommun – Flygbuller", _SIG + "var-far-du-bygga/flygbuller.html")
_SBG = "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/"
_SBG_DUVBO = ("Sundbybergs stad – Duvbo", _SBG + "duvbo")
_SBG_PROG = ("Sundbybergs stad – Miljöprogram Duvbo (pdf)",
             "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf")
_SBG_KAMIN = ("Sundbybergs stad – Kaminer, eldstäder och skorsten", _SBG + "bygglovsguide/kaminer-eldstader-och-skorsten")
_SBG_ETABL = ("Sundbybergs stad – Byggetablering", _SBG + "bygglovsguide/byggetablering")
_VASBY_KU = ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö (pdf)",
             "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf")
_VASBY_KULT = ("Upplands Väsby kommun – Kulturhistoriska byggnader, kulturmiljöer",
               "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/kulturhistoriska-byggnader-kulturmiljoer")
_VASBY_VA = ("Upplands Väsby kommun – Ledningsnät, anslutning till fastighet",
             "https://www.upplandsvasby.se/bygga-bo-och-miljo/vatten-och-avlopp/ledningsnat-anslutning-till-fastighet")

_ROT_SMAHUS = ("I ett småhus räknar Skatteverket bland annat rivning av väggar, ny planlösning, tilläggsisolering, "
               "kakel och klinker och andra förbättringsarbeten som rotarbete. Avdraget gäller arbetskostnaden, inte "
               "material och resor.")
_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Äger ni "
            "bostaden två kan båda göra avdrag. Där avdraget gäller drar Geal det direkt på fakturan.")
_ROT_BRF = ("I en bostadsrätt ger Skatteverket rotavdrag för arbete innanför lägenhetens tak, väggar och golv som du "
            "ansvarar för enligt stadgarna. Stambyten och arbete på gemensamma ytor som tak, fasader och trapphus ger "
            "inget avdrag för dig som bostadsrättshavare.")

PAGES_TJ = {

# ------------------------------------------------------------------ HÄGERSTEN
"totalrenovering-hagersten.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Hägersten", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Hägersten – villa eller bostadsrätt",
  "description": "Totalrenovering i Hägersten: villorna i Mälarhöjden, lägenheterna på Hägerstensåsen, anmälan, "
                 "föreningens tillstånd och asbest i hus från 1940–1970.",
  "h1": "Totalrenovering i Hägersten",
  "lead": "I Hägersten ligger villastaden Mälarhöjden och flerbostadshusen på Hägerstensåsen nära varandra, och en "
          "totalrenovering ser helt olika ut i de två. Geal Entreprenad AB renoverar hela villan eller lägenheten "
          "i en sammanhållen entreprenad och reder ut vad som kräver anmälan, lov eller föreningens tillstånd.",
  "card": "Villan i Mälarhöjden eller lägenheten.",
  "sections": [
    {"id": "tva-sorters-hem", "anchor": "Två sorters hem",
     "h2": "Två sorters hem i samma stadsdel",
     "paras": [
       "Stadens områdesfakta för 2025 visar skillnaden tydligt. I Mälarhöjden fanns 1 507 bostäder, och 1 086 av "
       "dem låg i småhus – 988 med äganderätt. På Hägerstensåsen fanns 4 904 bostäder, nästan alla i "
       "flerbostadshus: 2 034 bostadsrätter och 2 657 hyresrätter hos privata värdar.",
       "För en totalrenovering betyder det att två grannområden har helt olika regler att förhålla sig till. I "
       "villan är det du som fastighetsägare som ansvarar för att lagens krav uppfylls. I bostadsrätten är det "
       "föreningen som äger huset, och mycket av det du vill göra kräver styrelsens tillstånd innan något annat.",
     ],
     "aside": {"title": "Områdesfakta 2025", "items": [
       "Mälarhöjden: 1 086 småhus av 1 507 bostäder", "Hägerstensåsen: 4 904 bostäder",
       "Hägerstensåsen: 2 034 bostadsrätter"]}},
    {"id": "malarhojden", "h2": "Villan i Mälarhöjden",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur villasamhällen som Mälarhöjden "
       "växte fram efter privata initiativ genom större markförvärv. Husen är individuellt utformade, trä är det "
       "vanligaste fasadmaterialet, och glasverandor, takkupor och snickarglädje ger området dess variation. I "
       "vägledningens tabell står Mälarhöjden som kulturhistoriskt värdefull miljö.",
       "En totalrenovering inomhus kräver sällan bygglov, men varsamhetskravet gäller ändå. Ska fönster, "
       "verandor eller fasadmaterial bytas samtidigt räcker det inte att åtgärden är lovfri på ett vanligt småhus: "
       "i en miljö som Stadsmuseets karta markerar som värdefull kan bygglov krävas ändå. Vi slår upp fastigheten "
       "innan vi planerar det som syns utifrån.",
     ],
     "aside": {"title": "Villastaden enligt Varsam", "items": [
       "Privat initiativ och större markförvärv", "Individuellt utformade hus", "Trä, glasverandor och takkupor"]}},
    {"id": "hagerstensasen", "h2": "Lägenheten på Hägerstensåsen",
     "paras": [
       "Stockholms stad skriver att du inte behöver göra någon anmälan om du ändrar planlösningen inom en lägenhet "
       "och inga tekniska egenskapskrav påverkas – till exempel om du flyttar eller bygger ut kök eller badrum. "
       "Påverkas bärande konstruktion, brandskydd eller ventilation, eller tillkommer en ny VA-stam i ett nytt "
       "schakt, krävs anmälan och startbesked.",
       "Staden påminner också om att en hyresgäst normalt inte får göra sådana ändringar, och att du i en "
       "bostadsrätt behöver föreningens tillstånd. Ska köket flyttas och badrummets kanal användas som kombinerad "
       "imkanal måste kanalens mått räcka, och staden råder dig att tidigt rådgöra med sotaren. Vi tar fram det "
       "underlag som styrelsen behöver innan vi bokar in arbetet.",
     ],
     "aside": None},
    {"id": "asbest-hagersten", "h2": "Asbest i hus från 1940–1970",
     "paras": [
       "Boverket skriver att asbest förbjöds inom byggsektorn 1982, men att stora mängder finns kvar i byggnader. "
       "Det är främst hus som byggdes mellan 1940 och 1970 som innehåller asbest, men den kan finnas även i äldre "
       "hus. Så länge den är inkapslad är den ingen fara – det är när materialet bearbetas och dammar som fibrerna "
       "blir farliga.",
       "Inför en totalrenovering i Hägersten tar vi därför reda på husets byggår och tidigare renoveringar och "
       "låter ta prover på de material som kan innehålla asbest. Det som innehåller asbest saneras innan "
       "rivningen fortsätter. Läs mer om enskilda rum under " +
       _L.format("badrumsrenovering-hagersten.html", "badrumsrenovering i Hägersten") + " och " +
       _L.format("koksrenovering-hagersten.html", "köksrenovering i Hägersten") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Hägersten till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi går igenom hela villan eller lägenheten."),
    ("Tillstånd och anmälan", "Föreningens tillstånd, anmälan och eventuellt lov reds ut."),
    ("Provtagning", "Misstänkt asbest provas innan något rivs."),
    ("Rivning", "Sanering och rivning i rätt ordning."),
    ("Installationer", "El, VVS och ventilation byggs om."),
    ("Ytskikt och slutkontroll", "Golv, väggar, kök och bad, sedan gemensam besiktning."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Hägersten",
  "rot": [_ROT_SMAHUS, _ROT_BRF, _ROT_SUM],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Hägersten?",
  "price": [
    "Hur mycket som rivs, om asbest behöver saneras, om kök och badrum flyttas, el- och VVS-arbetets omfattning, "
    "ytskikt och hur material kan bäras in. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi göra en anmälan för att flytta köket i vår bostadsrätt på Hägerstensåsen?",
     "Inte om inga tekniska egenskapskrav påverkas. Påverkas bärande delar, brandskydd eller ventilation, eller "
     "behövs en ny VA-stam, krävs anmälan och startbesked. Föreningens tillstånd behövs i båda fallen."),
    ("Krävs bygglov för att byta fönster på en villa i Mälarhöjden?",
     "På ett vanligt småhus är många fasadändringar lovfria, men Mälarhöjden står som kulturhistoriskt värdefull "
     "miljö. Om Stadsmuseets karta visar att fastigheten är särskilt värdefull krävs lov ändå."),
    ("Hur vet vi om det finns asbest i huset i Hägersten?",
     "Boverket råder att börja med byggåret och tidigare renoveringar. I hus från 1940–1970 finns det sannolikt "
     "asbest, och misstänkta material behöver provas innan rivning."),
    ("Kan badrummets ventilationskanal användas för köket i Hägersten?",
     "Bara om kanalens sammanlagda mått räcker, enligt Stockholms stad. Köket ska ha tillräcklig frånluft och "
     "uppfylla kraven för imkanal."),
    ("Får vi renovera vår hyreslägenhet i Hägersten?",
     "Stockholms stad skriver att du som hyresgäst normalt inte får göra ändringar som påverkar bärande delar, "
     "ventilation eller VA. Tala med hyresvärden först."),
  ],
  "sources": [_of("Mälarhöjden", "soderort/hagersten/malarhojden"), _of("Hägerstensåsen", "soderort/hagersten/hagerstensasen"),
              _VARSAM, _PLAN, _FLYTTA, _ASB, _SKV, _SKV2],
  "cta": ("Funderar du på att renovera hela bostaden i Hägersten?",
          "Boka ett gratis platsbesök, så går vi igenom huset eller lägenheten och vad som behöver anmälas innan du "
          "får ett skriftligt kostnadsförslag."),
  "img": [
    ("Trävilla med glasveranda och takkupa i en lummig villastad",
     "1910s Swedish wooden villa with light yellow panel, white glazed veranda, a dormer on a red tile roof and "
     "carpentry details, set in a lush garden with old fruit trees on a hilly street, summer daylight" + _SFX),
    ("Lägenhet under renovering med nya väggreglar och kök som flyttas",
     "interior of a 1950s Swedish apartment under total renovation, new timber studs for a moved kitchen wall, "
     "exposed concrete floor, plastic covered windows, tools on the floor, daylight" + _SFX),
    ("Gammal golvmatta och fix som friläggs inför provtagning",
     "close view of an old patterned vinyl floor tile partly lifted from a concrete subfloor showing black "
     "adhesive underneath, a sealed sample bag lying beside it, renovation site, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SIGTUNA
"totalrenovering-sigtuna.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Sigtuna", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Sigtuna – ventilation, VA och kulturmiljö",
  "description": "Totalrenovering i Sigtuna: anmälan för ny ventilation, när en VA-ändring är väsentlig, varsamhet i "
                 "Sigtuna stads kulturmiljö och tillbyggnad nära Arlanda.",
  "h1": "Totalrenovering i Sigtuna",
  "lead": "En totalrenovering i Märsta, Sigtuna stad eller Rosersberg handlar ofta lika mycket om installationerna "
          "som om ytorna. Geal Entreprenad AB renoverar hela huset, tar fram handlingarna som Sigtuna kommun vill "
          "ha och planerar arbetet så att anmälan och startbesked finns innan vi börjar.",
  "card": "Ventilation, VA och kulturmiljö.",
  "sections": [
    {"id": "ventilation-sigtuna", "anchor": "Ventilation",
     "h2": "Ny ventilation kräver anmälan",
     "paras": [
       "Sigtuna kommun skriver att du måste göra en anmälan och invänta startbesked innan du installerar ett nytt "
       "ventilationssystem, och att samma sak gäller om du ändrar ett befintligt. Innebär åtgärden en stor "
       "förändring av byggnadens utsida – till exempel ett aggregat eller kanaler på fasaden – behövs bygglov "
       "i stället för anmälan.",
       "Till anmälan vill kommunen ha situationsplan, planritning, fasadritningar, förslag till kontrollplan, "
       "konstruktionsritning och utlåtande från konstruktör. Tomtkartan för situationsplanen laddas ner gratis från "
       "kommunen. Byts ventilationen vid en totalrenovering, medan tak, väggar och golv ändå är öppna, ska anmälan "
       "vara klar innan rivningen börjar.",
     ],
     "aside": {"title": "Kommunen vill se", "items": [
       "Situationsplan och planritning", "Fasadritningar", "Förslag till kontrollplan",
       "Konstruktionsritning och utlåtande"]}},
    {"id": "va-sigtuna", "h2": "Vatten och avlopp – när en ändring är väsentlig",
     "paras": [
       "Enligt kommunen krävs anmälan om du väsentligt ändrar eller gör en ny installation för vatten eller avlopp. "
       "En ändring räknas som väsentlig när installationen påverkar byggnadens bärande konstruktion eller när ett "
       "stambyte påverkar VA-stammarna. Till anmälan hör en redovisning av vatten- och avloppsanordningarna, plan- "
       "och sektionsritning och förslag till kontrollplan, och vid omfattande arbeten en kontrollansvarig.",
       "Ska huset anslutas till kommunens nät görs anmälan till Sigtuna Vatten och renhållning, SIVAB. Har fastigheten "
       "eget avlopp är det något annat: att anlägga eller ändra ett enskilt avlopp är tillståndspliktigt enligt "
       "miljöbalken. Ska ett nytt badrum kopplas till ett enskilt avlopp tar vi därför upp frågan tidigt.",
     ],
     "aside": None},
    {"id": "kulturmiljo-sigtuna", "h2": "Hus i Sigtunas kulturmiljöer",
     "paras": [
       "Sigtuna kommun påminner om att alla ändringar ska göras varsamt och att särskilt värdefulla byggnader inte "
       "får förvanskas. Kommunen ber fastighetsägare behålla formspråk, proportioner och karaktärsdrag som är typiska "
       "för byggnaden och tiden, och att bevara ursprungliga material och detaljer – eller ersätta dem med samma "
       "material när de måste bytas.",
       "För Sigtuna stad finns en bevarande- och förnyelseplan och för dalgången mellan Odensala och Hova särskilda "
       "riktlinjer. Är huset särskilt värdefullt kan bygglov krävas för sådant som annars är lovfritt, till exempel "
       "fasadändring, rivning av en byggnadsdel eller solceller. Vid en totalrenovering av ett äldre hus i Sigtuna "
       "stad lägger vi därför upp arbetet inifrån och behåller fönster, dörrar och fasad om inget annat är bestämt.",
     ],
     "aside": {"title": "Kommunens råd", "items": [
       "Behåll formspråk och proportioner", "Bevara ursprungliga material", "Byt till samma material"]}},
    {"id": "arlanda", "h2": "När renoveringen blir en tillbyggnad nära Arlanda",
     "paras": [
       "Arlanda flygplats är riksintresse enligt miljöbalken, och flygbullret påverkar stora delar av kommunen. "
       "Kommunen skriver att den kontaktar Swedavia för ett utlåtande innan den beslutar om en nybyggnad eller "
       "tillbyggnad inom flygplatsens influensområde. Det gäller alltså inte en ren invändig renovering, men "
       "väl om huset byggs ut samtidigt.",
       "I bygglovsbedömningen väger kommunen bland annat in bullersituationen, hur avloppet ska lösas och markens "
       "radonhalt. Ibland kan bygget godtas om bullret begränsas, till exempel genom avskärmning eller isolering. "
       "Vill du bygga till i samma veva beskriver vi reglerna under " +
       _L.format("tillbyggnad-sigtuna.html", "tillbyggnad i Sigtuna") + ". Badrummet för sig finns under " +
       _L.format("badrumsrenovering-sigtuna.html", "badrumsrenovering i Sigtuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Sigtuna till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi går igenom huset, ventilation och avlopp."),
    ("Handlingar", "Ritningar, kontrollplan och utlåtanden tas fram."),
    ("Anmälan", "Anmälan eller lov – startbesked innan arbetet börjar."),
    ("Rivning", "Det som ska bort rivs i rätt ordning."),
    ("Installationer", "Ventilation, VA och el byggs om."),
    ("Ytskikt och slutbesked", "Golv, väggar, kök och bad, sedan slutbesked där det krävs."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Sigtuna",
  "rot": [_ROT_SMAHUS, _ROT_SUM],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Sigtuna?",
  "price": [
    "Om ventilationen byts, om VA-stammar påverkas, om huset har enskilt avlopp, hur mycket som rivs och om "
    "ursprungliga material ska bevaras. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi göra en anmälan för ny ventilation i huset i Sigtuna?",
     "Ja. Sigtuna kommun skriver att både nya ventilationssystem och ändringar i befintliga kräver anmälan och "
     "startbesked. Sitter aggregat eller kanaler på fasaden kan det i stället krävas bygglov."),
    ("När är en VA-ändring väsentlig i Sigtuna?",
     "När installationen påverkar byggnadens bärande konstruktion eller när ett stambyte påverkar VA-stammarna, "
     "enligt kommunen. Då krävs anmälan."),
    ("Vi har eget avlopp i Sigtuna – vad gäller när vi bygger nytt badrum?",
     "Att anlägga eller ändra ett enskilt avlopp är tillståndspliktigt enligt miljöbalken. Ansökan görs hos "
     "kommunen i dess e-tjänst."),
    ("Måste Swedavia yttra sig när vi renoverar vårt hus i Märsta?",
     "Inte vid en invändig renovering. Kommunen kontaktar Swedavia när det gäller nybyggnad eller tillbyggnad "
     "inom Arlandas influensområde."),
    ("Kan vi byta till nya material på ett äldre hus i Sigtuna stad?",
     "Kommunen ber att ursprungliga material bevaras eller ersätts med samma material. På särskilt värdefulla hus "
     "kan bygglov krävas även för åtgärder som annars är lovfria."),
  ],
  "sources": [_SIG_VENT, _SIG_VA, _SIG_KULT, _SIG_FLYG, _SKV, _SKV2],
  "cta": ("Vill du renovera hela huset i Sigtuna?",
          "Boka ett gratis platsbesök, så går vi igenom ventilation, avlopp och kulturmiljö innan du får ett "
          "skriftligt kostnadsförslag."),
  "img": [
    ("Villa med betongpannor och en skottkärra på tomten en vinterdag",
     "1970s Swedish suburban villa with brown concrete tile roof and light wooden panel, windows covered with "
     "protective plastic during renovation, a skip container on the driveway, birch trees, overcast daylight" + _SFX),
    ("Nytt ventilationsaggregat och isolerade kanaler på en vind",
     "new white residential ventilation unit with heat recovery and insulated grey ducts installed on a wooden "
     "attic floor under roof trusses, mineral wool insulation, daylight from a small window" + _SFX),
    ("Äldre trähus med originalfönster längs en gata i en småstad",
     "old low Swedish wooden houses painted in red and ochre with original small-paned windows along a narrow "
     "street in a historic small town, clay tile roofs, calm summer morning" + _SFX),
  ],
},

# ------------------------------------------------------------------ SUNDBYBERG
"totalrenovering-sundbyberg.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Sundbyberg", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Sundbyberg – Duvbos villor inifrån",
  "description": "Totalrenovering i Sundbyberg: Duvbos utökade lovplikt, fasader och material enligt miljöprogrammet, "
                 "kamin och skorsten, och container på stadens mark.",
  "h1": "Totalrenovering i Sundbyberg",
  "lead": "I Sundbyberg ligger Duvbo, Sveriges första egnahemsområde, där allt som syns utifrån har särskilda "
          "regler. Geal Entreprenad AB renoverar hela huset inifrån, håller det yttre som det är och "
          "tar hand om anmälan, lov och etablering.",
  "card": "Duvbos villor, kaminer och etablering.",
  "sections": [
    {"id": "duvbo", "anchor": "Duvbo",
     "h2": "Duvbo – riksintresse sedan 1987",
     "paras": [
       "Sundbybergs stad beskriver Duvbo som Sveriges första egnahemsområde. Riksantikvarieämbetet utsåg det till "
       "riksintresse 1987. Enligt stadens miljöprogram bildades föreningen Egna Hem 1898, köpte egendomen Dufvebol "
       "året därpå och lade ut en stadsplan med 325 tomter. 1924 utökades området västerut med ytterligare 98 "
       "villatomter.",
       "Staden har särskilda regler för området och erbjuder ett kostnadsfritt konsultationsmöte med någon av "
       "stadens arkitekter inför större åtgärder som nybyggnad eller tillbyggnad. Planerar du en totalrenovering "
       "som också ändrar huset utvändigt är det ett bra första steg.",
     ],
     "aside": {"title": "Duvbo i korthet", "items": [
       "Egna Hem bildades 1898", "Stadsplan med 325 tomter", "98 tomter till 1924", "Riksintresse 1987"]}},
    {"id": "fasader-duvbo", "h2": "Det yttre ändras inte i förbifarten",
     "paras": [
       "Detaljplanen för Duvbo har utökad lovplikt: bygglov krävs för åtgärder som påverkar byggnadens yttre "
       "utseende, och staden skriver att även solcellspaneler kräver lov. Byts fönster, dörrar, panel eller "
       "takmaterial i samband med renoveringen på ett sätt som påverkar utseendet behövs alltså bygglov.",
       "Miljöprogrammet beskriver vad som ska tas hänsyn till. Sekelskiftesvillorna har fasader indelade i fält med "
       "stående och liggande spontpanel och snickarglädje, och tak i rött lertegel eller falsad plåt. 1920-talets "
       "villor har locklistpanel och enkla eller brutna sadeltak med rött lertegel, och husen från 1930- och "
       "40-talen är slätputsade i ljusa kulörer. Träfasaderna målades ursprungligen med linoljefärg eller slamfärg. "
       "Vid en totalrenovering behåller vi därför det yttre och lägger kraften på planlösning, installationer och "
       "ytskikt inne.",
     ],
     "aside": {"title": "Kräver lov i Duvbo", "items": [
       "Ändringar av yttre utseende", "Solcellspaneler", "Träd över 20 cm i diameter"]}},
    {"id": "kamin-sundbyberg", "h2": "Kamin, insats och skorsten",
     "paras": [
       "Ska eldstaden användas igen efter renoveringen gäller stadens regler för eldstäder. Sundbybergs stad "
       "skriver att det krävs anmälan och startbesked för att installera eldstad, skorsten eller rökkanal, för att byta en insats "
       "om eldningsförhållandena ändras och för att byta eldstad om det innebär en ny anslutning till rökkanalen "
       "eller ett annat bränsle. En tyngre eldstad som kräver förstärkning av bärande delar kräver också anmälan.",
       "En ny eller ändrad skorsten kan dessutom kräva bygglov som fasadändring, och i Duvbo påverkar den "
       "husets utseende. Staden råder att utformning och placering bestäms i samråd med skorstensfejarmästaren. "
       "Till ansökan hör fasad- och planritning, produktblad och kontrollplan.",
     ],
     "aside": None},
    {"id": "etablering-sundbyberg", "h2": "Container och byggbod på gatan",
     "paras": [
       "En totalrenovering kräver plats för container och material. Staden skriver att byggetableringen bör stå "
       "på den egna fastigheten om det går. På någon annans mark behövs fastighetsägarens tillstånd, och ska den stå "
       "på stadens mark, till exempel gatu- eller parkmark, behövs tillstånd från polisen. Byggbodar, plank och i "
       "vissa fall containrar kan också kräva bygglov.",
       "I Duvbo är tomterna stora och förgårdarna breda, så vi försöker placera containern på tomten. Där det inte "
       "går söker vi tillstånden i god tid. Enskilda rum beskriver vi under " +
       _L.format("badrumsrenovering-sundbyberg.html", "badrumsrenovering i Sundbyberg") + " och " +
       _L.format("koksrenovering-sundbyberg.html", "köksrenovering i Sundbyberg") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Sundbyberg till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi går igenom huset och tomten."),
    ("Konsultation", "Vid utvändiga ändringar i Duvbo bokas stadens konsultationsmöte."),
    ("Lov och anmälan", "Bygglov för det yttre, anmälan för eldstad och installationer."),
    ("Etablering", "Container och bodar på tomten eller med polisens tillstånd."),
    ("Renovering", "Rivning, installationer och ytskikt i rätt ordning."),
    ("Slutkontroll", "Gemensam genomgång och slutbesked där det krävs."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Sundbyberg",
  "rot": [_ROT_SMAHUS, _ROT_SUM],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Sundbyberg?",
  "price": [
    "Hur mycket som byggs om inne, om eldstaden ska återställas, om det yttre kräver lov och särskilda material, "
    "och var containern kan stå. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för nya fönster på vår villa i Duvbo?",
     "Ja. Detaljplanen för Duvbo har utökad lovplikt för åtgärder som påverkar byggnadens yttre utseende."),
    ("Kan vi få hjälp av staden innan vi renoverar i Duvbo?",
     "Ja. Sundbybergs stad erbjuder ett kostnadsfritt konsultationsmöte med en av stadens arkitekter inför större "
     "åtgärder som nybyggnad eller tillbyggnad. Där får du veta vad som är möjligt på fastigheten."),
    ("Behövs anmälan för att byta kamininsats i Sundbyberg?",
     "Ja, om bytet ändrar eldningsförhållandena, till exempel rökgastemperaturen. Då krävs anmälan och startbesked "
     "enligt staden."),
    ("Får containern stå på gatan i Sundbyberg?",
     "Bara med tillstånd från polisen, eftersom gatumarken ägs av staden. Staden råder att etableringen placeras "
     "på den egna fastigheten om det går."),
    ("Behöver vi bygglov för solceller på villan i Duvbo?",
     "Ja. Sundbybergs stad skriver att även solcellspaneler kräver bygglov i Duvbo, eftersom detaljplanen har "
     "utökad lovplikt för åtgärder som påverkar husets yttre utseende."),
    ("Vilken färg använde man på Duvbos trävillor från början?",
     "Enligt stadens miljöprogram målades träfasaderna ursprungligen med linoljefärg eller slamfärg i tidstypiska, "
     "jordnära färgskalor."),
  ],
  "sources": [_SBG_DUVBO, _SBG_PROG, _SBG_KAMIN, _SBG_ETABL, _SKV, _SKV2],
  "cta": ("Vill du renovera hela villan i Sundbyberg?",
          "Boka ett gratis platsbesök, så går vi igenom huset, reglerna i Duvbo och etableringen innan du får ett "
          "skriftligt kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla med snickarglädje och tegeltak på en höjd bland stora träd",
     "Swedish wooden villa from around 1900 with panel in alternating vertical and horizontal fields, carpentry "
     "decorations, red clay tile roof and a high plastered base, on a hill among large old trees and fruit trees, "
     "picket fence, summer daylight" + _SFX),
    ("Liten vedkamin vid en kaklad vägg i ett rum under renovering",
     "old white tiled stove standing in a room of an old wooden villa under renovation, walls stripped to boards, "
     "floor covered with protective paper, daylight from small-paned windows" + _SFX),
    ("Container på uppfarten till en villa med bred förgård",
     "green skip container standing on the gravel driveway of an old Swedish villa with a wide front garden, "
     "hedge and picket fence along the street, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"totalrenovering-upplands-vasby.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Upplands Väsby", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Upplands Väsby – villor och radhus",
  "description": "Totalrenovering i Upplands Väsby: äldre villor före 1960, radhus och kedjehus från 1960–70-talen, "
                 "varsamhet även inomhus och dagvattnet vid renoveringen.",
  "h1": "Totalrenovering i Upplands Väsby",
  "lead": "Upplands Väsby har både äldre villor från tiden före 1960 och stora grupper av radhus och kedjehus "
          "från 1960- och 70-talen. Geal Entreprenad AB renoverar hela huset med kommunens "
          "kunskapsunderlag för kulturmiljö som stöd, så att det som gör husen typiska finns kvar.",
  "card": "Äldre villor, radhus och varsamhet.",
  "sections": [
    {"id": "villor-fore-1960", "anchor": "Villor före 1960",
     "h2": "De äldre villorna",
     "paras": [
       "Kommunens kunskapsunderlag för kulturmiljö beskriver de äldre villaområdena som friliggande hus i stora "
       "trädgårdar, ofta i 1,5–2 våningar med sadeltak eller brutet sadeltak och fasader i träpanel. Spröjsade "
       "fönster, verandor, utanpåliggande trappor och snickarglädje är återkommande, och i egnahemsområdena låg "
       "ofta standardiserade ritningar till grund. Som exempel nämns Runby egnahemsområde, Åsvägen–Lövvägen och "
       "villaområdena kring Sandavägen.",
       "Underlaget ger också råd: undvik förhöjda väggliv, frontespiser och större takkupor som bryter mot villans "
       "ursprungliga volym. För en totalrenovering betyder det att mer boyta oftast får hittas inne i huset – i en "
       "omdisponerad planlösning eller en bättre utnyttjad vind – snarare än genom att lyfta taket.",
     ],
     "aside": {"title": "Äldre villor före 1960", "items": [
       "1,5–2 våningar, sadeltak", "Träpanel och spröjsade fönster", "Verandor och snickarglädje"]}},
    {"id": "radhus-1960-70", "h2": "Radhus och kedjehus från 1960–70-talen",
     "paras": [
       "De östra kommundelarna har enligt underlaget vuxit fram med många småhus och radhus i separata enklaver "
       "längs säckgator. Husen har enkla volymer i en eller två våningar, platta eller flacka tak, enluftsfönster "
       "utan spröjs och infällda balkonger. Rött tegel, vitt kalkcementtegel och målad träpanel i starka kulörer är "
       "de vanligaste materialen. Exempel finns i Sjukyrkoberget, Skälby, Fresta och Odenslunda.",
       "Underlaget betonar att grupperna är enhetligt utförda och råder fastighetsägare att undvika tillbyggnader "
       "som bryter ursprungsvolymen. En totalrenovering av ett radhus börjar därför inifrån: badrum, kök, "
       "installationer och planlösning. Fönster, fasadmaterial och kulörer håller vi lika med grannarnas.",
     ],
     "aside": None},
    {"id": "varsamhet-inomhus", "h2": "Varsamheten gäller även inomhus",
     "paras": [
       "Upplands Väsby kommun påpekar att varsamhetskravet och förvanskningsförbudet i plan- och bygglagen alltid "
       "gäller, inom och utom detaljplan, och att kraven gäller invändiga och utvändiga åtgärder – även sådana som "
       "inte kräver lov eller anmälan. En byggnad behöver inte vara utpekad i förväg för att vara värdefull. "
       "Kommunen nämner till exempel hus som är byggda före 1920 och har kvar sin karaktär.",
       "I praktiken betyder det att vi dokumenterar fasta inredningar, dörrar, lister och trappor i ett äldre hus "
       "innan rivningen och föreslår vad som kan sparas. Är du osäker på om huset är särskilt värdefullt kan "
       "kommunen svara på vad som gäller för fastigheten.",
     ],
     "aside": {"title": "Kan vara värdefullt", "items": [
       "Utpekat i en inventering", "Skyddat i detaljplan", "Byggt före 1920 med bibehållen karaktär"]}},
    {"id": "dagvatten-vasby", "h2": "Dagvatten och dränering vid renoveringen",
     "paras": [
       "Görs dräneringen om i samband med renoveringen gäller kommunens regler för ledningsnätet. Dagvatten och "
       "dräneringsvatten får inte kopplas till spillvattenservisen, och eget vatten får inte kopplas ihop med "
       "kommunens. Förbindelsepunkten mot det allmänna nätet ligger vanligtvis ungefär en halv meter utanför "
       "fastighetsgränsen, och var ledningarna går utanför tomten kan beställas via Ledningskollen.",
       "Vi kontrollerar hur husets avlopp och dagvatten är kopplade innan vi bygger om badrum och tvättstuga. "
       "Badrummet för sig beskriver vi under " +
       _L.format("badrumsrenovering-upplands-vasby.html", "badrumsrenovering i Upplands Väsby") + " och köket "
       "under " + _L.format("koksrenovering-upplands-vasby.html", "köksrenovering i Upplands Väsby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Upplands Väsby till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi går igenom huset och dess ursprungliga detaljer."),
    ("Dokumentation", "Det som ska sparas fotograferas och märks."),
    ("Planering", "Planlösning, installationer och eventuell anmälan."),
    ("Rivning", "Varsam rivning av det som ska bort."),
    ("Installationer", "El, VVS och ventilation byggs om."),
    ("Ytskikt och slutkontroll", "Golv, väggar, kök och bad, sedan gemensam besiktning."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Upplands Väsby",
  "rot": [_ROT_SMAHUS, _ROT_SUM],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Upplands Väsby?",
  "price": [
    "Husets ålder och storlek, hur mycket av inredningen som ska sparas, om planlösningen ändras, el- och "
    "VVS-arbetets omfattning och om dräneringen görs om. Efter ett gratis platsbesök får du ett skriftligt "
    "kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga en större takkupa när vi renoverar vår äldre villa i Upplands Väsby?",
     "Kommunens kunskapsunderlag råder att undvika större takkupor, frontespiser och förhöjda väggliv som bryter "
     "mot villornas ursprungliga volym. Det kan också krävas lov."),
    ("Gäller varsamhetskravet även när vi river inomhus i Upplands Väsby?",
     "Ja. Kommunen skriver att varsamhetskravet och förvanskningsförbudet gäller invändiga åtgärder också, även "
     "när inget lov eller anmälan krävs."),
    ("Får dräneringen kopplas till avloppet i Upplands Väsby?",
     "Nej. Dagvatten och dräneringsvatten får inte kopplas till spillvattenservisen enligt kommunen."),
    ("Hur vet vi om vårt hus i Upplands Väsby är kulturhistoriskt värdefullt?",
     "Det kan vara utpekat i kommunens kunskapsunderlag, skyddat i detaljplan eller byggt före 1920 med bevarad "
     "karaktär. Kommunen kan svara på vad som gäller för fastigheten."),
    ("Kan vi byta fönster i radhuset i Upplands Väsby?",
     "Ja, men kunskapsunderlaget betonar att radhusgrupperna är enhetligt utförda. Vi föreslår fönster som "
     "liknar de ursprungliga enluftsfönstren och stämmer av med grannar och förening."),
  ],
  "sources": [_VASBY_KU, _VASBY_KULT, _VASBY_VA, _SKV, _SKV2],
  "cta": ("Vill du renovera hela huset i Upplands Väsby?",
          "Boka ett gratis platsbesök, så går vi igenom huset och dess detaljer innan du får ett skriftligt "
          "kostnadsförslag."),
  "img": [
    ("Äldre trävilla med veranda och snickarglädje i en stor trädgård",
     "1920s Swedish wooden villa with a gambrel roof, light panel, small-paned windows and a veranda with "
     "carpentry details, large garden with old apple trees and pines on a slope, summer daylight" + _SFX),
    ("Radhuslänga från 1970-talet med tegel och målad träpanel",
     "1970s Swedish row houses with flat roofs, facades combining red brick and dark green painted wooden panel, "
     "single-pane windows without glazing bars, small front gardens along a cul-de-sac, daylight" + _SFX),
    ("Sparad innerdörr och lister märkta inför renovering",
     "old panelled wooden interior door with brass handle and old mouldings leaning against a wall in a house "
     "under renovation, protected with cardboard corners, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"totalrenovering-vallingby.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Vällingby", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Vällingby – 1950-talshus i riksintresset",
  "description": "Totalrenovering i Vällingby: ABC-staden som riksintresse, husens ursprungliga detaljer, eternit och "
                 "asbest, och vad som gäller i en bostadsrätt.",
  "h1": "Totalrenovering i Vällingby",
  "lead": "Vällingby byggdes ut under 1950-talet som landets första ABC-stad och är riksintresse för "
          "kulturmiljövården. Geal Entreprenad AB renoverar hela radhuset, kedjehuset eller lägenheten och utgår "
          "från det som gör husen typiska för sin tid.",
  "card": "ABC-staden, eternit och föreningen.",
  "sections": [
    {"id": "abc-staden", "anchor": "ABC-staden",
     "h2": "ABC-staden som riksintresse",
     "paras": [
       "Stadens beskrivning av riksintressena berättar att Vällingby–Råcksta planerades som en självförsörjande "
       "förort, landets första så kallade ABC-stad – Arbete, Bostad, Centrum. Ingen skulle ha längre än 900 meters "
       "gångväg från bostaden till tunnelbanan. Området byggdes ut under 1950-talet och ses som ett sammanhållet "
       "uttryck för det årtiondet.",
       "Bland de värdebärande karaktärsdragen nämns de ursprungliga husens gestaltning och byggnadsdetaljer som "
       "fönster, entrépartier, balkonger och räcken. Det är just de delarna som ofta byts vid en renovering. Vi "
       "försöker därför renovera dem i stället för att byta, och där byte är nödvändigt välja utförande som liknar "
       "originalet.",
     ],
     "aside": {"title": "Värdebärande detaljer", "items": [
       "Fönster", "Entrépartier", "Balkonger och räcken"]}},
    {"id": "bostader-vallingby", "h2": "Radhus, kedjehus och lägenheter",
     "paras": [
       "Enligt stadens områdesfakta för 2025 fanns 4 391 bostäder i Vällingby. 3 891 låg i flerbostadshus, och av "
       "de 449 småhusen var 228 bostadsrätter och 220 ägda. I flerbostadshusen fanns 1 848 bostadsrätter och "
       "1 498 hyresrätter i allmännyttan. Även ett radhus kan alltså ägas av en förening.",
       "Stadens vägledning för småhusområden beskriver hur tunnelbanestädernas radhus lades på bryn och platåer "
       "utanför centrum, mjukt anpassade till terrängen och ofta med en suterrängvåning. Den nedre våningen i ett "
       "suterränghus ligger delvis mot marken, och där behöver fukt och ventilation ses över innan nya ytskikt "
       "läggs.",
     ],
     "aside": {"title": "Vällingby 2025", "items": [
       "4 391 bostäder", "449 småhus", "228 småhus med bostadsrätt"]}},
    {"id": "eternit-vallingby", "h2": "Eternit och annan asbest",
     "paras": [
       "Vägledningen nämner att många områden från tiden prövade nya material, och att asbestcement – mer känt som "
       "eternit – var populärt. Eterniten har i många fall bytts mot andra material, och i dag finns fasadskivor "
       "utan asbest som gör det möjligt att behålla husens uttryck.",
       "Boverket skriver att asbest förbjöds i byggsektorn 1982 och att det främst är hus från 1940–1970 som "
       "innehåller den. Inkapslad asbest är ofarlig, men när materialet bearbetas frigörs fibrer. Inför en "
       "totalrenovering i Vällingby inventerar vi därför fasadskivor, golv, fix och rörisolering och låter "
       "sanera det som innehåller asbest innan rivningen börjar.",
     ],
     "aside": None},
    {"id": "foreningen-vallingby", "h2": "Bostadsrätten och föreningen",
     "paras": [
       "I en bostadsrätt är det föreningen som äger huset. Stockholms stad skriver att du behöver föreningens "
       "tillstånd för ändringar som påverkar bärande konstruktion, brandskydd, ventilation eller vatten och avlopp, "
       "och att anmälan och startbesked krävs när de tekniska egenskapskraven påverkas. Att flytta eller bygga ut "
       "kök och badrum inom lägenheten kräver ingen anmälan om inga sådana krav berörs.",
       "Vi tar fram ritningar och en beskrivning av arbetet till styrelsen och planerar in renoveringen först när "
       "tillståndet finns. Enskilda rum beskriver vi under " +
       _L.format("badrumsrenovering-vallingby.html", "badrumsrenovering i Vällingby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Vällingby till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi går igenom bostaden och dess ursprungliga detaljer."),
    ("Inventering", "Misstänkt asbest provas innan något rivs."),
    ("Tillstånd", "Föreningens tillstånd och anmälan där det krävs."),
    ("Sanering och rivning", "Asbest saneras först, sedan rivs resten."),
    ("Installationer", "El, VVS och ventilation byggs om."),
    ("Ytskikt och slutkontroll", "Golv, väggar, kök och bad, sedan gemensam besiktning."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Vällingby",
  "rot": [_ROT_SMAHUS, _ROT_BRF, _ROT_SUM],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Vällingby?",
  "price": [
    "Om asbest behöver saneras, hur mycket som rivs, om detaljer som fönster och entré ska renoveras, el- och "
    "VVS-arbetets omfattning och fukt i en suterrängvåning. Efter ett gratis platsbesök får du ett skriftligt "
    "kostnadsförslag.",
  ],
  "faq": [
    ("Är Vällingby ett riksintresse?",
     "Ja. Vällingby–Råcksta är riksintresse för kulturmiljövården, och stadens beskrivning nämner de ursprungliga "
     "husens fönster, entrépartier, balkonger och räcken bland karaktärsdragen."),
    ("Finns det eternit på vårt radhus i Vällingby?",
     "Det kan det göra. Stadens vägledning nämner att asbestcement, eternit, var ett populärt material i området. "
     "Prover visar säkert om skivorna innehåller asbest."),
    ("Kan vi byta eternitskivorna mot något som ser likadant ut?",
     "Ja. Vägledningen skriver att det i dag finns fasadskivor utan asbest som gör det möjligt att behålla "
     "radhusens uttryck. Kan bytet kräva lov stämmer vi av det först."),
    ("Behöver vi föreningens tillstånd för att renovera vårt radhus i Vällingby?",
     "Om radhuset är en bostadsrätt, ja, för ändringar av bärande delar, ventilation och VA. Enligt områdesfakta "
     "var 228 av småhusen i Vällingby bostadsrätter 2025."),
    ("Måste vi spara originalfönstren i vårt radhus i Vällingby?",
     "Fönster nämns bland de ursprungliga detaljer som bär riksintresset. Vi renoverar dem hellre än byter, och "
     "ett byte inom riksintresset kan kräva bygglov."),
    ("Vad är en suterrängvåning?",
     "En våning som delvis ligger mot marken i en sluttning. Stadens vägledning beskriver att radhusen i "
     "tunnelbanestäderna ofta tar upp nivåskillnader med en sådan våning."),
  ],
  "sources": [_RIKS, _of("Vällingby", "vasterort/hasselby-vallingby/vallingby"), _VARSAM, _ASB, _PLAN, _SKV, _SKV2],
  "cta": ("Vill du renovera hela bostaden i Vällingby?",
          "Boka ett gratis platsbesök, så går vi igenom huset, detaljerna och föreningens krav innan du får ett "
          "skriftligt kostnadsförslag."),
  "img": [
    ("Radhus från 1950-talet i tegel på en höjd med gräsytor och tallar",
     "1950s Swedish two-storey row houses in red brick with white window frames and simple entrance canopies, "
     "set on a gentle slope with lawns and pine trees, footpath in front, summer daylight" + _SFX),
    ("Suterrängvåning i ett radhus under renovering med frilagd vägg",
     "lower ground floor room of a 1950s Swedish row house under renovation, one wall partly against the slope "
     "stripped to concrete, new insulation boards stacked, a small window high up, daylight" + _SFX),
    ("Grå fasad och vita stuprör på en radhusgavel",
     "close view of grey fibre cement facade boards on the gable of a 1950s Swedish row house, a white window "
     "frame and a downpipe, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"totalrenovering-alvsjo.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Älvsjö", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Älvsjö – villastaden, elen och köket",
  "description": "Totalrenovering i Älvsjö: Hallmans villastad, Stadsmuseets inventering, gammal elanläggning som "
                 "byggs om, kök och ventilation, och det som syns från gatan.",
  "h1": "Totalrenovering i Älvsjö",
  "lead": "I Älvsjö villastad står äldre trävillor på stora trädgårdstomter. När ett sådant "
          "hus renoveras från grunden är det ofta elen, köket och badrummet som behöver göras om, medan fasaden "
          "ska få vara kvar. Geal Entreprenad AB renoverar hela huset i en sammanhållen entreprenad.",
  "card": "Villastaden, elen och köket.",
  "sections": [
    {"id": "villastaden-alvsjo", "anchor": "Villastaden",
     "h2": "Älvsjö villastad",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden berättar att små stationssamhällen växte "
       "fram när järnvägen byggdes ut, och att några av dem – Spånga och Älvsjö – blev municipalsamhällen på "
       "1910-talet med egen administration och beskattningsrätt. Stadsplanen för Älvsjö villastad togs fram av Per "
       "Olof Hallman enligt samma principer som hans planer för den tidiga trädgårdsstaden.",
       "I vägledningens tabell står del av Älvsjö som kulturhistoriskt värdefull miljö med generösa byggrätter. "
       "Enligt stadens områdesfakta för 2025 fanns 730 bostäder i Älvsjö, varav 214 i småhus och 191 med "
       "äganderätt.",
     ],
     "aside": {"title": "Villastaden", "items": [
       "Municipalsamhälle på 1910-talet", "Stadsplan av Per Olof Hallman", "Kulturhistoriskt värdefull miljö"]}},
    {"id": "inventeringen", "h2": "Stadsmuseets inventering och husens exteriörer",
     "paras": [
       "Stadsmuseet började sommaren 1977 inventera Stockholms förorter, och Älvsjö var en av de fjorton första "
       "stadsdelarna. I "
       "museets redogörelse framgår att inventeringen gällde bebyggelse från tiden före omkring 1930 som hade kvar "
       "sin ursprungliga karaktär, och att det endast var exteriörerna som besiktigades.",
       "För en totalrenovering betyder det att fasaden, fönstren och verandan är det som andra har dokumenterat och "
       "bedömt. Interiören har större frihet, men varsamhetskravet gäller ändå. Vi gör om planlösning och "
       "installationer inifrån och låter det som syns från gatan vara kvar om inget annat är bestämt.",
     ],
     "aside": None},
    {"id": "elen-alvsjo", "h2": "Elen i ett gammalt hus",
     "paras": [
       "Elsäkerhetsverket skriver att det inte finns några regler som tvingar dig att uppgradera en befintlig "
       "elanläggning när nya krav införs, så länge den är i gott skick och används som tidigare. Men om du bygger "
       "om eller utvidgar anläggningen ska ombyggnaden följa de nya kraven. Görs ett sovrum om till badrum eller "
       "byggs huset ut behöver elen oftast ändras.",
       "Allt elinstallationsarbete ska göras av ett elinstallationsföretag som är registrerat hos Elsäkerhetsverket "
       "för verksamhetstypen Bostäder, och det går att kontrollera i myndighetens tjänst Kolla elföretaget. I en "
       "totalrenovering samordnar vi elarbetet med rivning och ytskikt, så att nya ledningar dras innan väggarna "
       "stängs.",
     ],
     "aside": {"title": "Elsäkerhetsverket", "items": [
       "Gammal anläggning får vara kvar om den är i gott skick", "Ombyggnad följer nya krav",
       "Registrerat elföretag för Bostäder"]}},
    {"id": "kok-alvsjo", "h2": "Köket och ventilationen",
     "paras": [
       "Att flytta köket kräver inte bygglov, men Stockholms stad skriver att anmälan behövs om flytten påverkar "
       "bärande konstruktion, brandskydd eller ventilation, eller om en ny VA-stam dras i ett nytt schakt. Köket "
       "ska ha tillräcklig frånluft och uppfylla kraven för imkanal, och staden råder att tidigt rådgöra med "
       "sotaren om nya eller ändrade kanaler.",
       "Går köksfläkten till en murad kanal i skorstensstocken kontrollerar vi kanalen innan köket planeras. Fasaden behåller vi: på ett småhus kan många fasadändringar göras utan lov, men inte om "
       "huset eller området är särskilt värdefullt. Läs mer under " +
       _L.format("koksrenovering-alvsjo.html", "köksrenovering i Älvsjö") + " och " +
       _L.format("badrumsrenovering-alvsjo.html", "badrumsrenovering i Älvsjö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Älvsjö till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi går igenom huset, elen och kanalerna."),
    ("Planering", "Planlösning, kök, bad och eventuell anmälan."),
    ("Rivning", "Det som ska bort rivs, det som ska sparas skyddas."),
    ("El och VVS", "Registrerad elinstallatör och VVS före stängda väggar."),
    ("Ytskikt", "Golv, väggar, kök och bad."),
    ("Slutkontroll", "Gemensam genomgång och dokumentation av elen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Älvsjö",
  "rot": [_ROT_SMAHUS, _ROT_SUM],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Älvsjö?",
  "price": [
    "Husets storlek och skick, hur mycket av elen som byggs om, om köket flyttas och kanaler behöver göras om, "
    "och hur mycket av den ursprungliga inredningen som ska sparas. Efter ett gratis platsbesök får du ett "
    "skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste vi byta all el när vi renoverar villan i Älvsjö?",
     "Inte nödvändigtvis. Elsäkerhetsverket skriver att en äldre anläggning får vara kvar om den är i gott skick, "
     "men att det som byggs om eller utvidgas ska följa de nya kraven."),
    ("Hur kontrollerar vi att elfirman får arbeta i vårt hus i Älvsjö?",
     "I Elsäkerhetsverkets tjänst Kolla elföretaget. Företaget ska vara registrerat för verksamhetstypen Bostäder."),
    ("Vem gjorde stadsplanen för Älvsjö villastad?",
     "Per Olof Hallman, enligt stadens vägledning Varsam utveckling av småhus- och villaområden."),
    ("Behöver vi anmälan för att flytta köket i Älvsjö?",
     "Bara om flytten påverkar bärande konstruktion, brandskydd eller ventilation, eller om en ny VA-stam dras i "
     "ett nytt schakt, enligt Stockholms stad."),
    ("Får vi flytta badrummet till övervåningen i villan i Älvsjö?",
     "Ja, men det kräver anmälan om det påverkar bärande delar, ventilation eller kräver en ny VA-stam i nytt "
     "schakt. Elen ska då byggas om enligt dagens krav."),
    ("Inventerade Stadsmuseet även husens interiörer i Älvsjö?",
     "Nej. Museets redogörelse säger att det endast var exteriörerna som besiktigades, med undantag i enstaka fall."),
  ],
  "sources": [_VARSAM, _ALVINV, _of("Älvsjö", "soderort/hagersten/alvsjo"), _EL, _FLYTTA, _FASAD, _SKV, _SKV2],
  "cta": ("Vill du renovera hela villan i Älvsjö?",
          "Boka ett gratis platsbesök, så går vi igenom huset, elen och köket innan du får ett skriftligt "
          "kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla i trä med veranda på en stor trädgårdstomt",
     "Swedish wooden villa from around 1905 with a glazed veranda, white trim and a steep red tile roof on a large "
     "garden plot with old fruit trees and a clipped hedge, quiet villa street, early summer" + _SFX),
    ("Ljus hall med vita väggar och trägolv",
     "new grey residential electrical distribution board mounted on a wall in an old wooden villa under "
     "renovation, new cables running in conduits along exposed studs, daylight" + _SFX),
    ("Kök i en äldre villa under ombyggnad med skorstensstock i hörnet",
     "kitchen in an old Swedish wooden villa under reconstruction, cabinets removed, a plastered chimney breast in "
     "the corner, new water pipes on the wall, wooden floor protected with board, daylight" + _SFX),
  ],
},
}
