# -*- coding: utf-8 -*-
"""Plåtslagare – ortsidor v7: Danderyd, Ekerö, Haninge, Sollentuna, Tyresö, Värmdö (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
Danderyds kommun (Så sköter du dina egna VA-ledningar, VA-folder hösten 2022; Dagvattenplan 2021–2027;
Nya regler för bygglov från 1 december 2025), Ekerö kommun (Dagvatten; Solceller; Vad vill du bygga?),
Haninge kommun (Haninges karaktärsmiljöer, WSP 2019, uppdaterad nov 2020; Fasadändring), Sollentuna kommun
(Fasadändring en- eller tvåbostadshus; Tilläggsisolera; Dagvattenpolicy KF 2016; Teknisk handbok kap 6
Dagvatten), Tyresö kommun (Översvämningsrisker och åtgärder; Förändringar i PBL från 1 december 2025),
Värmdö kommun (Bygglov vid fasadändring; Bygga i kulturmiljöer; Kulturmiljö och byggnadsvård; Fritidshus-
område i förändring del 1, jan 2023), Boverket (Ändra fasad eller tak, 2026; Risker med vatten som läcker
genom tak; Risker med avvattning från låglutande tak; Energiguiden: Tilläggsisolera fasaden) och
Skatteverket (Ger arbetet rätt till rotavdrag?; Så fungerar rotavdraget).
Strukna (ej verifierade): att Edsviken påverkas av koppar från villatak, att Roslagsvatten sköter VA i
Danderyd (kommunen är huvudman, Solör kundtjänst), regler om stuprör hos Sollentuna Energi och Miljö
(sidan hittades inte), att Värmdös skärgårdslägen har mer vind än andra orter (bara Boverkets generella
skrivning används), plåtmaterial på Dalarös sommarvillor och på Ramundvägen, att fönsterbleck ger rot i
småhus (Skatteverkets lista nämner det bara för ägarlägenhet), att solceller ger rotavdrag (grön teknik).
Inga priser, garantier, omdömen, egna uppdrag eller cert. Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_TAK = ("Boverket – Ändra fasad eller tak (2026)",
           "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/andra-fasad-eller-tak/")
_BV_LACK = ("Boverket – Risker med vatten som läcker genom tak",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttertak/kalla-vindar/vatten-som-lacker-genom-tak/")
_BV_AVV = ("Boverket – Risker med avvattning från låglutande tak",
           "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttertak/takets-ytskikt/avvattning-laglutande-tak/")
_BV_ISOL = ("Boverket – Energiguiden: Tilläggsisolera fasaden",
            "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/tillaggsisolera-fasaden/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ DANDERYD
"platslagare-danderyd.html": {
  "kind": "district", "service": "platslagare", "ort": "Danderyd", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Danderyd – rännor, stuprör och materialval",
  "description": "Plåtslagare i Danderyd: takvatten som inte får gå till spillvattnet, kommunens råd om koppar och zink och lovplikt i kulturmiljöerna. Gratis platsbesök.",
  "h1": "Plåtslagare i Danderyd",
  "lead": "Det mesta regnet som faller på en villa i Danderyd passerar plåt på vägen ner: nockbeslag, ränndalar, hängrännor och stuprör. Var vattnet sedan tar vägen, och vilken metall det har runnit över, är frågor som kommunen har tydliga synpunkter på. Geal Entreprenad AB har egna plåtslagare som arbetar i Djursholm, Stocksund, Enebyberg och övriga Danderyd, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Rännor, stuprör och beslag i Danderyd.",
  "sections": [
    {"id": "takvatten-danderyd", "anchor": "Takvattnet i Danderyd",
     "h2": "Takvattnet får inte gå till spillvattenledningen",
     "paras": [
       "I kommunens VA-folder från hösten 2022, Så sköter du dina egna VA-ledningar, står det rakt ut: takvatten från stuprör får inte ledas till spillvatten- eller avloppsledningen. Kommunen föreslår i stället att du ordnar plats för dagvattnet på tomten, till exempel genom att bygga en stenkista eller låta vattnet rinna ner i regntunnor.",
       "Samma checklista uppmanar villaägare att rensa brunnar och hängrännor för att undvika stora vattensamlingar runt huset. Det är där plåtslagarens arbete och tomtens dränering möts. En ränna som lutar fel, ett skarvat stuprör som läcker eller en utkastare som slutar precis vid sockeln gör att vattnet hamnar på fel ställe även om resten av systemet är rätt byggt.",
       "Vid ett besök följer vi därför vattnet hela vägen: från takfoten, genom rännan och stupröret, ner till marken. Är stupröret i dag anslutet till en ledning i marken frågar vi vart den går. Är du osäker kan kommunens tekniska kontor svara på frågor om anslutningen.",
     ],
     "aside": {"title": "Kommunens VA-checklista om dagvatten", "items": [
       "Stuprör inte till spillvattnet", "Stenkista eller regntunna på tomten",
       "Rensa brunnar och hängrännor", "Plantera mer, hårdgör mindre"]}},
    {"id": "koppar-zink", "h2": "Koppar och zink i kommunens dagvattenplan",
     "paras": [
       "Kommunfullmäktige i Danderyd har antagit en dagvattenplan för 2021–2027. Den ska användas vid all om- och nybyggnation och så långt som möjligt tillämpas på befintliga anläggningar. En av planens tolv målsättningar är att material och ämnen som kan öka spridningen av miljöskadliga ämnen via dagvattnet ska undvikas, och som exempel nämns byggnadsmaterial som koppar och zink vid ny- och tillbyggnation.",
       "För en plåtslagare betyder det att materialvalet blir en fråga redan när en tillbyggnad, en carport eller ett nytt skärmtak planeras. Det finns andra plåtmaterial, till exempel lackerad stålplåt och aluminium, och vi går igenom alternativen innan något beställs. Planen säger också att dagvatten i första hand ska tas om hand lokalt, nära källan, vilket stämmer väl med kommunens råd om stenkista och regntunna.",
       "På ett befintligt hus med kopparbeslag är situationen en annan. Att byta ett skadat beslag mot ett likadant är underhåll. Vill du byta material helt kan det i stället påverka husets utseende, och då kommer kulturmiljöfrågan in.",
     ],
     "aside": None},
    {"id": "lov-danderyd", "h2": "Nytt takmaterial och plåt i kulturmiljöerna",
     "paras": [
       "Boverket skriver att det inte krävs bygglov för att byta taktäckningsmaterial på ett småhus, och att det med byte menas ett tak som ser annorlunda ut eller är av annat material. Innan taket byts behöver du kontrollera att det klarar den nya belastningen. Ändringen ska ändå göras varsamt och anpassas till omgivningen.",
       "Danderyds kommun påpekar att lovplikten är kvar i de känsliga områdena. Inom kulturhistoriskt särskilt värdefulla områden och inom riksintressen för kulturmiljövården krävs bygglov för fasadändringar som nytt tak, och det gäller även om byggnaden i sig är särskilt värdefull. Om fastigheten berörs syns i kommunens kulturmiljökarta, och den som vill ha ett formellt besked kan söka frivilligt bygglov.",
       "Ska plåttaket bytas helt finns mer under " + _L.format("takbyte-danderyd.html", "takbyte i Danderyd") + ". Gäller det bara beslag, rännor och bleck kan arbetet oftast planeras utan kontakt med kommunen, men vi tittar på kartan innan kulör eller profil ändras.",
     ],
     "aside": {"title": "Före beställning", "items": [
       "Kontrollera kulturmiljökartan", "Läs detaljplanen", "Undvik koppar och zink vid tillbyggnad",
       "Klarar taket ny belastning?"]}},
    {"id": "skarmtak-danderyd", "h2": "Skärmtak och tillbyggnader räknas samman",
     "paras": [
       "Enligt kommunens frågor och svar om de nya reglerna krävs bygglov om ett en- eller tvåbostadshus byggs till med mer än sammantaget 30 kvadratmeter, och då räknas tidigare utförda skärmtak och attefallstillbyggnader in. Kommunen påminner också om att den som ökar bruttoarean utan lov själv ska informera kommunens VA-enhet.",
       "Ett nytt skärmtak över entrén eller altanen behöver en avslutning mot husväggen och oftast en egen ränna, och många får ett litet plåttak. Boverket pekar på att påbyggnader som ökar vattenbelastningen jämfört med vad avvattningen var byggd för kan göra att systemet inte räcker till. När en tillbyggnad leder sitt vatten till en befintlig ränna kontrollerar vi därför att rännan och stupröret klarar mängden.",
       "Läs mer om rännor och stuprör i allmänhet under " + _L.format("hangrannor-stupror.html", "hängrännor och stuprör") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtjobb i Danderyd till",
  "steps": [
    ("Vattnets väg", "Vi följer vattnet från nock till mark: beslag, ränndalar, rännor, stuprör och vart utkastaren leder."),
    ("Karta och plan", "Kulturmiljökartan och detaljplanen kontrolleras innan material eller kulör ändras."),
    ("Materialval", "Vid tillbyggnad väljer vi tillsammans plåt i linje med kommunens dagvattenplan."),
    ("Kostnadsförslag", "Rännor, stuprör, beslag och eventuellt nytt skärmtak prissätts var för sig."),
    ("Montering", "Gammal plåt demonteras, underlaget kontrolleras och ny plåt monteras med rätt fall."),
    ("Kontroll i regn", "Vid genomgången visar vi hur vattnet leds bort och var det tas om hand på tomten."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Danderyd",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör, och att montera och montera ner byggnadsställningar i samband med rotarbetet.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kr per person och år, inom 75 000 kr för rot och rut tillsammans. Plåt och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Danderyd?",
  "price": [
    "Hur långa rännorna är, hur många stuprör och ränndalar huset har, valet av material och kulör, om tillbyggnadens avvattning ska kopplas till befintliga rännor och vilken ställning som behövs på en hög villa. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Får stupröret på vår villa i Danderyd vara kopplat till avloppet?",
     "Nej. Kommunen skriver att takvatten från stuprör inte får ledas till spillvatten- eller avloppsledningen. Vattnet kan i stället tas om hand på tomten, till exempel i en stenkista eller regntunna."),
    ("Ska vi välja bort kopparplåt på tillbyggnaden i Djursholm?",
     "Kommunens dagvattenplan anger att byggnadsmaterial som koppar och zink ska undvikas vid ny- och tillbyggnation. Vi föreslår därför andra plåtmaterial till tillbyggnaden och går igenom kulörerna med dig."),
    ("Kan ni byta ett trasigt kopparbeslag mot ett nytt i koppar?",
     "Ja, att ersätta ett skadat beslag med samma material och utförande är underhåll. Planens råd om koppar och zink gäller ny- och tillbyggnation."),
    ("Räknas vårt nya skärmtak in i de 30 kvadratmetrarna?",
     "Ja. Danderyds kommun skriver att tidigare utförda skärmtak och attefallstillbyggnader räknas in när det sammanlagda måttet för lovfria tillbyggnader bedöms."),
    ("Var ser jag om villan ligger i ett kulturhistoriskt värdefullt område?",
     "I Danderyds kulturmiljökarta. Ligger fastigheten där krävs bygglov för nytt tak och andra fasadändringar, och kommunen ger rådgivning om du är osäker."),
  ],
  "sources": [
    ("Danderyds kommun – Så sköter du dina egna VA-ledningar (VA-folder hösten 2022, pdf)",
     "https://www.danderyd.se/contentassets/751fb19789854742aeec443c9ffb4fb1/a5-danderyd_sep-2022_korr3.pdf"),
    ("Danderyds kommun – Dagvattenplan 2021–2027 (pdf)",
     "https://www.danderyd.se/contentassets/00f7f9d961964d459147d4659ee94463/dagvattenplan-2021-2027.pdf"),
    ("Danderyds kommun – Nya regler för bygglov från 1 december 2025",
     "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/"),
    _BV_TAK, _BV_AVV, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver rännor och stuprör ses över i Danderyd?", "Boka ett gratis platsbesök så följer vi vattnet från taket till tomten tillsammans."),
  "img": [
    ("Stor ljus villa i Danderyd med mörkt falsat plåttak, hängrännor och stuprör",
     "large early 1900s Swedish villa with light yellow rendered facade and a dark grey standing-seam metal roof, matching dark grey half-round gutters and round downpipes ending in a gravel bed, big oak trees and lawn, Djursholm Danderyd, overcast autumn daylight, no people, no text"),
    ("Hängränna och stuprör i plåt vid hörnet av en gul trävilla med regntunna",
     "corner of a light yellow painted wooden Swedish villa with white corner boards, a dark grey metal half-round gutter at the eaves turning into a round dark grey metal downpipe that runs down the corner and ends just above a green rain barrel standing on flat stones, lawn and autumn leaves, overcast day, no plastic pipes, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ EKERÖ
"platslagare-ekero.html": {
  "kind": "district", "service": "platslagare", "ort": "Ekerö", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Ekerö – takvatten, solceller och skärmtak",
  "description": "Plåtslagare i Ekerö: takvatten som tas om hand på tomten, solceller på plåttak och Lovö, skärmtak och förråd med plåt. Gratis platsbesök.",
  "h1": "Plåtslagare i Ekerö",
  "lead": "På Mälaröarna rinner dagvattnet ut i vattendrag som också används för dricksvatten och bad, och kommunen är inte skyldig att ta emot dagvatten från fastigheterna. Det gör takets plåt och avvattning till mer än en detalj. Geal Entreprenad AB har egna plåtslagare som lagar och byter rännor, stuprör, beslag och plåttak på Ekerö, Färingsö och öarna runt omkring, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Takvatten, solceller och plåttak i Ekerö.",
  "sections": [
    {"id": "lod-ekero", "anchor": "Takvattnet på Ekerö",
     "h2": "Takvattnet tas om hand på tomten",
     "paras": [
       "Ekerö kommun förklarar att dagvatten är regn- och smältvatten som rinner över gräs, asfalt och tak, och att det kan ledas bort via diken eller ledningar eller tas om hand direkt på fastigheten. Det senare kallas lokalt omhändertagande av dagvatten, LOD. Kommunen skriver också att den inte är skyldig att ta emot dagvatten från fastigheter och att LOD är ett bra sätt att ta hand om vattnet.",
       "Kommunen påminner om att dagvattnet går direkt ut i vattendrag som vi sedan tar dricksvatten från eller badar i. När det blir stopp i en brunn ute på gatan är det vägföreningen som ansvarar för underhållet, inte kommunen.",
       "För ett hus på Ekerö betyder det att stuprörens nedre del är lika viktig som rännan på taket. Vi ser till att varje stuprör slutar i en utkastare, ett ränndalsstycke ut på marken eller en regntunna, och att vattnet leds bort från grunden och inte mot grannens tomt.",
     ],
     "aside": {"title": "Vem ansvarar för vad på Ekerö?", "items": [
       "Rännor och stuprör: fastighetsägaren", "LOD på tomten: fastighetsägaren",
       "Gatans dagvattenbrunnar: vägföreningen", "Kommunalt dagvatten: Roslagsvatten"]}},
    {"id": "solceller-ekero", "h2": "Solceller på plåttaket – och undantaget på Lovö",
     "paras": [
       "Kommunen skriver att solenergi är bra att planera för när du bygger nytt eller lägger om taket, och att solceller på taket vanligtvis inte kräver bygglov. Bygglov krävs om detaljplanen anger det, och om fastigheten ligger inom detaljplan i ett område för totalförsvarets riksintressen eller i särskilt värdefulla byggnader och områden. Påverkar anläggningen bärande konstruktion eller brandskydd väsentligt krävs en bygganmälan. För Lovö skriver kommunen att Försvarsmakten tillfrågas i bygglovsärenden och ofta är negativ till solceller.",
       "Boverket nämner otäta infästningar för solceller som en av orsakerna till att regn läcker in genom tak, och skriver att du behöver kontrollera att taket klarar den nya belastningen. På ett falsat plåttak fästs panelerna ofta med klämmor i falsarna, medan andra lösningar kräver hål genom plåten. Vi bedömer vilket som passar taket, och om plåten ändå ska bytas är det klokt att göra det innan panelerna monteras. Läs mer under " + _L.format("solceller-tak.html", "solceller på taket") + ".",
     ],
     "aside": None},
    {"id": "skarmtak-ekero", "h2": "Skärmtak, förråd och låga plåttak",
     "paras": [
       "Efter ändringarna i plan- och bygglagen räknar Ekerö kommun skärmtak till den bygglovsbefriade potten för tillbyggnader. En lovfri komplementbyggnad får enligt kommunen ha en taknockshöjd på högst 4 meter inom detaljplan och 4,5 meter utanför. Det ger förråd, garage och carportar med låga tak, och plåt är ett av de material som fungerar på låg lutning.",
       "Låga tak ställer egna krav. Boverket skriver att utvändig takavvattning kan få problem med att det fryser i rännor och stuprör, och att stuprör som går ner till marken kan skadas av fordon och liknande. Vid en carport placerar vi därför stupröret där det inte är i vägen för bilen, och på ett förråd ser vi till att plåten har tillräckligt fall och en droppkant som släpper vattnet utanför väggen.",
       "Komplementbyggnader och tillbyggnader närmare gränsen än 4,5 meter kräver skriftligt medgivande från grannarna, annars behövs bygglov.",
     ],
     "aside": {"title": "Lovfritt komplement på Ekerö", "items": [
       "Taknock högst 4 m inom detaljplan", "Högst 4,5 m utanför detaljplan",
       "Skärmtak räknas till tillbyggnadspotten", "Grannemedgivande närmare än 4,5 m"]}},
    {"id": "karta-ekero", "h2": "Ekerökartan visar de nya undantagsområdena",
     "paras": [
       "Kommunen har gjort en ny bedömning av sina särskilt värdefulla byggnader och områden och visar dem i Ekerökartan. Där kan du inte tillämpa de ändrade byggreglerna. För fasadändringar på villa och fritidshus, som byte av taktäckning, krävs bygglov om fastigheten ligger i ett område som bedömts som särskilt värdefullt.",
       "Boverket beskriver samma sak från andra hållet: det krävs i regel varken bygglov eller anmälan för att ändra fasad eller tak på ett småhus, men utökad lovplikt kan gälla inom särskilt värdefulla områden och inom område för totalförsvaret. Ändringen ska alltså vara varsam även där den är lovfri. Mer om tak på Mälaröarna finns under " + _L.format("taklaggare-ekero.html", "takläggare i Ekerö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången för plåtarbeten i Ekerö",
  "steps": [
    ("Platsbesök", "Vi tittar på tak, rännor och stuprör och på var vattnet tar vägen på tomten."),
    ("Kartan", "Ekerökartan visar om fastigheten ligger i ett särskilt värdefullt område eller nära totalförsvarets riksintresse."),
    ("Förslag", "Plåt, rännor, stuprör och eventuella solcellsförberedelser står var för sig i ett skriftligt kostnadsförslag."),
    ("Leverans", "Material och ställning planeras efter vägen fram till huset."),
    ("Montering", "Plåten bockas och monteras med fall, droppkanter och utkastare som leder vattnet bort från grunden."),
    ("Genomgång", "Vi går runt huset tillsammans och visar var vattnet hamnar."),
  ],
  "rot_h2": "Rotavdrag för plåtslageri i Ekerö",
  "rot": [
    "Att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör ger rotavdrag i ett småhus enligt Skatteverket, och det gäller även ett fritidshus som du äger och använder som bostad. Ställning som monteras i samband med arbetet ingår.",
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ingår inte. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här styr priset i Ekerö",
  "price": [
    "Takets storlek och form, antalet stuprör och hur vattnet ska tas om hand på tomten, om plåten ska förberedas för solceller och hur lätt det är att komma fram med material och ställning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi koppla stupröret till kommunens dagvattennät på Ekerö?",
     "Kommunen skriver att den inte är skyldig att ta emot dagvatten från fastigheter. Om din fastighet kan anslutas får du svar på hos Roslagsvatten, som besvarar frågor om kommunalt dagvatten."),
    ("Vem ska vi ringa när brunnen på gatan är full av vatten?",
     "Din vägförening. Ekerö kommun skriver att det är vägföreningen som ansvarar för underhållet av dagvattenbrunnarna på gatan."),
    ("Kan vi sätta solceller på plåttaket på Lovö?",
     "Kommunen skriver att Försvarsmakten tillfrågas i bygglovsärenden inom detaljplan och områdesbestämmelser på Lovö och ofta är negativ till solceller. Kontrollera Ekerökartan och fråga kommunen innan något beställs."),
    ("Behöver plåttaket bytas innan solcellerna monteras?",
     "Det beror på plåtens skick, men panelerna sitter länge. Är plåten sliten är det enklare att byta den först än att montera ner panelerna senare. Taket ska också klara den nya belastningen."),
    ("Får carporten ha plåttak utan bygglov?",
     "En lovfri komplementbyggnad får ha taknock på högst 4 meter inom detaljplan och 4,5 meter utanför, och närmare gränsen än 4,5 meter krävs grannemedgivande. Takmaterialet i sig avgör inte lovplikten."),
  ],
  "sources": [
    ("Ekerö kommun – Dagvatten", "https://www.ekero.se/bygga-bo-miljo/vatten-och-avlopp/dagvatten"),
    ("Ekerö kommun – Solceller", "https://www.ekero.se/bygga-bo-miljo/energi-och-uppvarmning/solceller"),
    ("Ekerö kommun – Vad vill du bygga?", "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/vad-vill-du-bygga"),
    _BV_TAK, _BV_LACK, _BV_AVV, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska plåten på huset i Ekerö ses över?", "Boka ett gratis platsbesök så går vi igenom rännor, stuprör och tak tillsammans."),
  "img": [
    ("Rödmålad villa i Ekerö med svart falsat plåttak och solpaneler",
     "red painted Swedish wooden villa with white corners and a black standing-seam metal roof with a row of black solar panels mounted on clamps along the seams, black gutters and downpipes, birch trees and a glimpse of lake Mälaren, Ekerö, summer daylight, no people, no text"),
    ("Carport med lågt plåttak, hängränna och stuprör vid en grusad uppfart",
     "empty small open Swedish wooden carport on four posts with no walls at the front, a low-pitched grey corrugated metal roof without any chimney or flue, a slim grey metal gutter along the eave and one round downpipe at the back corner, gravel driveway, pine and birch trees, rural Ekerö, overcast day, completely empty carport, no vehicles, no chimney, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HANINGE
"platslagare-haninge.html": {
  "kind": "district", "service": "platslagare", "ort": "Haninge", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Haninge – gårdar, sjöbodar och falsad plåt",
  "description": "Plåtslagare i Haninge: falsad plåt på gårdar, korrugerad plåt på sjöbodar, brutna tak och lov nära totalförsvarets riksintresse. Gratis platsbesök.",
  "h1": "Plåtslagare i Haninge",
  "lead": "Haninge rymmer stationsnära samhällen, slottsmiljöer och en skärgård med gårdar, fiskebodar och sommarnöjen. Plåten på husen följer samma variation, från falsade tak på gårdarnas huvudbyggnader till enkla korrugerade skivor på sjöbodarna. Geal Entreprenad AB har egna plåtslagare som arbetar i Handen, Västerhaninge, Tungelsta, Dalarö och övriga Haninge, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Falsad plåt, sjöbodar och beslag i Haninge.",
  "sections": [
    {"id": "falsad-haninge", "anchor": "Falsad plåt i Haninge",
     "h2": "Falsad plåt hör till landsbygdens byggnadstradition",
     "paras": [
       "Kommunens dokument Haninges karaktärsmiljöer, framtaget av WSP 2019 och uppdaterat 2020, är en del av kulturmiljöprogrammet och ska stödja bygglov och förvaltning. Om landsbygden skriver det att de äldsta byggnaderna har timmerstomme och tak som vanligen täcktes med torv, brädor eller vass, material som senare ersattes av tegel.",
       "I råden för ny bebyggelse på landsbygden beskrivs sadeltaket som den vanligaste takformen. Tegel är ett vanligt material på huvudbyggnaden, och som annat material att föredra nämns falsad plåt. På förråd och sjöbodar anges trapetskorrugerad plåt som ett alternativ.",
       "Råden gäller nya hus, men de säger mycket om vad som passar på de gamla. När en gård har haft falsad plåt på taket lägger vi gärna ny plåt med samma bandbredd och kulör, så att taket fortsätter att se ut som det har gjort. Mer om tekniken finns under " + _L.format("falsat-plattak.html", "falsat plåttak") + ".",
     ],
     "aside": {"title": "Taken på Haninges landsbygd", "items": [
       "Torv, brädor och vass på de äldsta husen", "Tegel på många huvudbyggnader",
       "Falsad plåt som alternativ till tegel", "Korrugerad plåt på förråd och sjöbodar"]}},
    {"id": "sjobodar", "h2": "Sjöbodar och båthus vid vattnet",
     "paras": [
       "För sjöbodar och båthus ger karaktärsmiljöerna egna råd. Befintliga sjöbodsmiljöer ska bevaras, och nya bodar ska ha en enkel form med sadeltak och gaveln mot vattnet, stående träpanel målad i faluröd slamfärg och vara oisolerade och ouppvärmda. Användningen ska vara förvaring av båtar, båtutrustning och fiskeredskap.",
       "En sjöbod står ofta precis vid stranden och tar emot både regn och vind från vattnet. Det korrugerade plåttaket behöver därför sitta fast ordentligt vid gavlarna och längs takfoten, där vinden får tag. Vi byter gärna enstaka skivor och kompletterar fästdon i stället för att byta hela taket, om resten håller.",
       "Dokumentet skriver också att tegel och senare tillägg med plåtfasader är främmande material på landsbygden. Vi föreslår därför inte plåt som fasadbeklädnad på en sjöbod eller ett uthus, utan håller plåten på taket och i detaljerna.",
     ],
     "aside": None},
    {"id": "brutna-tak", "h2": "Brutna tak och mansardtak",
     "paras": [
       "Ett exempel i dokumentet är Tungelsta gamla skola från 1912, med brutet mansardtak täckt med falsad takplåt. Bland karaktärsdragen för sommarnöjena på Dalarö och Smådalarö, med villor från 1860- till 1920-talet, nämns träpanel, spröjsade fönster, torn och brutna tak.",
       "På ett brutet tak möts två lutningar i en brytlinje, och där är plåten svårast att göra rätt. Övergången måste tas upp av den övre plåten och föras över den undre så att vattnet inte kan tränga in i skarven. Kring tornhuvar, takkupor och skorstenar bockas beslagen för hand. Boverket skriver att tak med många vinklar, kupor och takfönster får fler skarvar och anslutningar, och att det ökar sannolikheten för läckage.",
       "Karaktärsmiljöerna anger att byggnaders ursprungliga arkitektoniska uttryck ska bevaras och vara vägledande vid om- och tillbyggnad i sommarnöjesområdena. Vi mäter därför upp befintliga beslag innan de rivs.",
     ],
     "aside": {"title": "Svåra punkter på ett brutet tak", "items": [
       "Brytlinjen mellan lutningarna", "Kupornas sidor och tak", "Tornhuvar och spiror",
       "Anslutning mot skorstenen"]}},
    {"id": "lov-haninge", "h2": "Lov i Haninge – och solceller nära totalförsvaret",
     "paras": [
       "Haninge kommun räknar byte av taktäckningsmaterial, takkupor och solceller till fasadändringarna. Bygglov krävs om fasaden ändras på en byggnad eller i ett område som är särskilt värdefullt. Kommunen anger också att solenergianläggningar kräver lov i ett detaljplanelagt område som ligger inom eller nära ett riksintresse för totalförsvaret, oavsett byggnadstyp.",
       "Ändringar ska enligt kommunen utföras varsamt även när de är lovfria, och karaktärsmiljöerna påpekar att deras råd kan tillämpas på alla sommarnöjesområden i kommunen, även de som inte är utpekade som särskilt värdefulla. Vill du veta mer om taken i kommunen i stort, se " + _L.format("taklaggare-haninge.html", "takläggare i Haninge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går plåtarbetet till i Haninge",
  "steps": [
    ("Besök på gården eller tomten", "Vi tittar på huvudbyggnad, uthus och sjöbod och noterar vilka plåttyper som finns."),
    ("Kulturmiljö och lov", "Vi kontrollerar om området är särskilt värdefullt och om solceller berörs av totalförsvarets riksintresse."),
    ("Uppmätning", "Befintliga beslag, falsar och skivor mäts upp innan något rivs."),
    ("Kostnadsförslag", "Varje byggnad och varje del av arbetet prissätts var för sig."),
    ("Plåtarbete", "Ny plåt bockas och monteras, och brytlinjer, kupor och genomföringar görs om noggrant."),
    ("Genomgång", "Vi visar arbetet och hur plåten ansluter mot de delar som har behållits."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Haninge",
  "rot": [
    "Rotavdrag gäller för att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör på ett småhus som du äger och bor i, också ett fritidshus. Arbete på en fristående sjöbod eller ett uthus på samma tomt bör stämmas av mot Skatteverkets regler innan.",
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år, inom 75 000 kr för rot och rut tillsammans. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Haninge?",
  "price": [
    "Hur många byggnader som ingår, om taken är raka eller brutna, mängden beslag kring kupor och torn, om plåten ska tillverkas efter förlaga och hur lätt det är att nå tomten med material. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Passar falsad plåt på en gammal gård i Österhaninge?",
     "Kommunens karaktärsmiljöer nämner falsad plåt som ett material att föredra vid sidan av tegel på landsbygdens huvudbyggnader. Har gården haft plåt tidigare passar det oftast att fortsätta med samma utförande."),
    ("Kan vi lägga korrugerad plåt på vår sjöbod på Dalarö?",
     "Trapetskorrugerad plåt anges som ett alternativ på förråd och sjöbodar. Ligger boden i ett särskilt värdefullt område eller en detaljplan med bestämmelser bör du stämma av med kommunen först."),
    ("Kan ni lägga ny plåt på ett mansardtak?",
     "Ja. Det kräver mer handarbete än ett rakt tak eftersom brytlinjen, kuporna och anslutningarna bockas på plats. Vi mäter upp de gamla beslagen så att det nya taket får samma linjer."),
    ("Kräver solceller bygglov i Haninge?",
     "Det beror på var huset ligger. Kommunen anger lovplikt i särskilt värdefulla områden och för solenergianläggningar i detaljplanelagda områden inom eller nära riksintresse för totalförsvaret."),
    ("Kan vi klä uthuset med plåt i stället för panel?",
     "Haninges karaktärsmiljöer beskriver plåtfasader som främmande på landsbygden. Vi rekommenderar plåt på taket och i detaljerna och trä på väggarna."),
  ],
  "sources": [
    ("Haninge kommun – Haninges karaktärsmiljöer, kulturmiljöprogram (WSP 2019, uppdaterad 2020, pdf)",
     "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf"),
    ("Haninge kommun – Fasadändring",
     "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/fasadandring/"),
    _BV_LACK, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver plåten på gården eller sjöboden ses över?", "Boka ett gratis platsbesök så går vi igenom tak, beslag och rännor på alla byggnader."),
  "img": [
    ("Faluröd gård i Haninge med svart falsat plåttak och vita knutar i ett odlingslandskap",
     "falu red Swedish farmhouse with white corner boards and window frames and a black standing-seam metal gable roof, a smaller red barn with corrugated metal roof beside it, open fields and a forest edge, Österhaninge countryside, summer daylight, no people, no text"),
    ("Röd sjöbod med korrugerat plåttak och gaveln mot vattnet",
     "small falu red wooden boathouse with vertical board and batten panelling and a grey trapezoidal corrugated metal gable roof, gable facing the calm sea, wooden jetty, granite rocks and pines, Stockholm archipelago near Dalarö, soft evening light, no boats, no people, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SOLLENTUNA
"platslagare-sollentuna.html": {
  "kind": "district", "service": "platslagare", "ort": "Sollentuna", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Sollentuna – radhus, isolering och materialval",
  "description": "Plåtslagare i Sollentuna: plåt längs radhuslängans takfot, bleck och vindskivor vid tilläggsisolering och kommunens dagvattenpolicy om materialval.",
  "h1": "Plåtslagare i Sollentuna",
  "lead": "I ett radhus delar grannarna takfot, ränna och nockplåt, och på en villa som tilläggsisoleras flyttas plötsligt både fönsterbleck och vindskivor. Det är två vanliga skäl att ta in en plåtslagare. Geal Entreprenad AB har egna plåtslagare som arbetar i Tureberg, Edsberg, Rotebro, Häggvik och övriga Sollentuna, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Radhusplåt, bleck och rännor i Sollentuna.",
  "sections": [
    {"id": "radhus-sollentuna", "anchor": "Plåt på radhus",
     "h2": "Radhuslängan har en gemensam takfot",
     "paras": [
       "Sollentuna kommun skriver att det oftast inte krävs bygglov för en fasadändring på ett en- eller tvåbostadshus, och räknar dit byte av kulör, fasadbeklädnad och taktäckningsmaterial. För radhus, kedjehus och andra sammanbyggda småhus gäller däremot olika möjligheter att ändra fasaden utan lov beroende på hur bebyggelsen är utformad, och kommunen ber dig kontakta kontaktcenter för vägledning.",
       "För plåten på ett radhus är det just sammanbyggnaden som ställer till det. Fotplåten och hängrännan löper ofta över flera hus, och nockplåten och vindskivorna ska se likadana ut längs hela längan. Byter ett hus till en annan profil eller kulör syns det tydligt, och en ränna som skarvas mot grannens måste ha samma fall så att vattnet inte blir stående i skarven.",
       "Kommunen påpekar att vissa detaljplaner har bestämmelser om hur fasad- och takmaterial ska vara utförda. Planerar flera grannar att byta plåt kan det löna sig att samordna och göra hela längan i samma etapp.",
     ],
     "aside": {"title": "Plåt som delas i en radhuslänga", "items": [
       "Fotplåt och hängränna", "Nockplåt", "Vindskivor på gavlarna", "Skarvar mellan husen"]}},
    {"id": "isolering-sollentuna", "h2": "Tilläggsisolering flyttar plåten",
     "paras": [
       "Kommunen skriver att en tilläggsisolering kan räknas som en fasadändring eftersom den kan ändra husets yttre utseende. Boverkets energiguide beskriver vad som händer: fönster och dörrar hamnar längre in i fasaden, takfoten skjuter inte ut lika mycket som tidigare och fasaden kan hänga ut över sockeln. För att behålla proportionerna kan fönster behöva flyttas ut och sockel och takfot byggas på.",
       "Varje sådan ändring är ett plåtjobb. Fönsterblecken måste bli djupare eller göras om när fönstret flyttas ut, vindskivor och fotplåt måste förlängas när takfoten byggs på och en sockelplåt kan behövas där väggen blir tjockare än grunden. Boverket nämner också att vind- och slagregnsutsatta detaljer som fönster och dörrar kan behöva en extra fuktsäker utformning.",
       "Vi samordnar gärna plåten med fasadarbetet, se " + _L.format("fasadrenovering-sollentuna.html", "fasadrenovering i Sollentuna") + ", så att blecken mäts upp mot den nya väggen och inte mot den gamla.",
     ],
     "aside": None},
    {"id": "dagvatten-sollentuna", "h2": "Materialval enligt dagvattenpolicyn",
     "paras": [
       "Sollentunas dagvattenpolicy antogs av kommunfullmäktige 2016 och är framtagen inom Oxunda Vattensamverkan, ett samarbete mellan Järfälla, Sigtuna, Sollentuna, Vallentuna, Täby och Upplands Väsby. Den gäller hela kommunen, även Edsvikens avrinningsområde. Policyn säger att förorening av dagvatten ska begränsas vid källan genom goda materialval och lokala lösningar, och att särskild hänsyn behöver tas till Mälaren som är dricksvattentäkt.",
       "Kommunens tekniska handbok för dagvatten pekar ut tät bebyggelse där en betydande andel hus har förzinkade byggnadsmaterial eller material som innehåller koppar som en områdestyp där rening av dagvattnet bör övervägas.",
       "För en villaägare är det ett skäl att fundera på materialet när rännor, stuprör eller beslag ska bytas. Vi går igenom vilka plåtmaterial och ytbehandlingar som finns och vad de innebär för husets utseende.",
     ],
     "aside": {"title": "Dagvattenpolicyn i korthet", "items": [
       "Minska konsekvenser vid översvämning", "Bevara en naturlig vattenbalans",
       "Goda materialval vid källan", "Fördröj flöden även på privat mark"]}},
    {"id": "lov-sollentuna", "h2": "Värdefullt område? Kommunen vill se huset från alla håll",
     "paras": [
       "Bygglov krävs för en fasadändring om fastigheten ligger inom ett kulturhistoriskt värdefullt område eller om byggnaden i sig är kulturhistoriskt värdefull. För att avgöra det ber kommunen om foton på fastigheten från samtliga väderstreck tillsammans med en beskrivning av åtgärden, och återkommer sedan med en bedömning.",
       "För åtgärder som inte kräver lov går det att söka frivilligt bygglov för att få ett beslut på att det planerade arbetet uppfyller lagens krav. Kommunen påminner om att du som byggherre ansvarar för att reglerna följs även när inget lov behövs. För byte av själva taket, se " + _L.format("takbyte-sollentuna.html", "takbyte i Sollentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången för plåten i Sollentuna",
  "steps": [
    ("Besök", "Vi tittar på takfot, rännor, bleck och skarvar och, i ett radhus, på hur plåten ansluter mot grannarna."),
    ("Detaljplan", "Vi kontrollerar om planen har bestämmelser om takmaterial och om huset kan ligga i ett värdefullt område."),
    ("Samordning", "Ska fasaden isoleras planeras plåten efter de nya måtten."),
    ("Kostnadsförslag", "Varje del prissätts för sig, och i en radhuslänga kan förslaget delas upp per hus."),
    ("Montering", "Plåten monteras med samma profil och kulör som längan i övrigt och med rätt fall i skarvarna."),
    ("Genomgång", "Vi visar arbetet och hur rännan leder vattnet förbi grannens del."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete i Sollentuna",
  "rot": [
    "Skatteverket godkänner rotavdrag för att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör på ett småhus, och ett radhus räknas som småhus. Bor du i en bostadsrätt ger samma arbete inte rotavdrag.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kr per person och år, inom ett gemensamt tak på 75 000 kr för rot och rut. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här påverkar priset i Sollentuna",
  "price": [
    "Längden på takfot och rännor, antalet fönsterbleck som ska göras om vid en isolering, om flera hus i en länga görs samtidigt och vilken ställning som behövs. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Kan vi byta hängränna på vårt radhus utan att grannen gör det?",
     "Ja, men rännan måste anslutas till grannens med rätt fall och tät skarv. Ändras kulör eller profil bör du kontakta kommunen, eftersom radhus bedöms utifrån hur bebyggelsen är utformad."),
    ("Behöver fönsterblecken bytas när vi tilläggsisolerar?",
     "Oftast. När väggen blir tjockare hamnar fönstret längre in eller flyttas ut, och blecket måste nå förbi den nya fasaden med droppkant och fall."),
    ("Kräver en tilläggsisolering bygglov i Sollentuna?",
     "Kommunen skriver att den kan räknas som en fasadändring. På ett en- eller tvåbostadshus krävs oftast inget lov, men i kulturhistoriskt värdefulla områden behövs bygglov."),
    ("Vilka foton vill kommunen ha för att bedöma om huset är värdefullt?",
     "Foton på fastigheten från samtliga väderstreck och en beskrivning av vad du vill göra. Kommunen återkommer sedan med en bedömning."),
    ("Spelar det någon roll vilken plåt vi väljer till rännorna?",
     "Dagvattenpolicyn säger att föroreningar ska begränsas genom goda materialval. Vi går igenom alternativen och vad de innebär innan du bestämmer dig."),
  ],
  "sources": [
    ("Sollentuna kommun – Fasadändring en- eller tvåbostadshus",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/fasadandring-for-en--eller-tvabostadshus/"),
    ("Sollentuna kommun – Tilläggsisolera",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/tillaggsisolera/"),
    ("Sollentuna kommun – Dagvattenpolicy för Sollentuna kommun (KF 2016, pdf)",
     "https://www.sollentuna.se/globalassets/kommun-och-politik/sa-styrs-sollentuna/sollentuna-forfattningssamling-sfs/miljo-och-halsoskydd/dagvattenpolicy-2.pdf"),
    ("Sollentuna kommun – Teknisk handbok, kap 6 Dagvatten (pdf)",
     "https://www.sollentuna.se/globalassets/trafik--resor/teknisk-handbok/kap-6-dagvatten.pdf"),
    _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska plåten på huset i Sollentuna bytas?", "Boka ett gratis platsbesök så går vi igenom takfot, rännor och bleck tillsammans."),
  "img": [
    ("Radhuslänga i Sollentuna med gemensam takfot, hängrännor och stuprör i plåt",
     "long row of 1970s Swedish two-storey terraced houses with vertical wooden panelling painted in muted ochre and brown, low-pitched dark grey concrete tile gable roof shared by the whole row, a continuous black metal fascia flashing and black half-round gutter running the full length of the row, black round downpipes between the houses, small front gardens, no window shutters, Sollentuna suburb, overcast day, no people, no cars, no text"),
    ("Nytt djupt fönsterbleck under ett fönster i en nyisolerad fasad",
     "close-up of a white wooden window set in a newly insulated thick light grey panelled facade, with a new deep folded dark grey metal window sill flashing with drip edge and upturned side ends, daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TYRESÖ
"platslagare-tyreso.html": {
  "kind": "district", "service": "platslagare", "ort": "Tyresö", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Tyresö – stuprör, källare och barr i rännorna",
  "description": "Plåtslagare i Tyresö: rostiga stuprör vid källaren, utkastare som leder vattnet bort, rännor under tallarna och råd vid skyfall. Gratis platsbesök.",
  "h1": "Plåtslagare i Tyresö",
  "lead": "Tyresö kommun ger villaägare ett konkret råd mot fukt i källaren: se till att stuprören är hela och rätt monterade. Det låter enkelt, men stupröret är ofta den mest bortglömda plåten på huset. Geal Entreprenad AB har egna plåtslagare som byter rännor, stuprör och beslag i Tyresö centrum, Trollbäcken, Krusboda och övriga Tyresö, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Stuprör, rännor och beslag i Tyresö.",
  "sections": [
    {"id": "stupror-tyreso", "anchor": "Stuprör och källare",
     "h2": "Rostiga järnstuprör och fukt i källaren",
     "paras": [
       "På sidan om översvämningsrisker skriver kommunen att dåligt fungerande stuprör och mark som lutar in mot huset hör till orsakerna till fuktproblem i källare. Problem med stuprör uppkommer enligt kommunen oftast när äldre stuprör av järn rostar sönder nere vid källaren. Vatten som rinner ut där hamnar precis intill grunden.",
       "Kommunens råd till fastighetsägare är att se till att stuprören är i bra skick och rätt monterade och att använda utkastare från stuprören. Det första vi gör vid ett besök är därför att gå runt huset och titta på stuprörens nedre meter: rost, sprickor, lösa skarvar och var vattnet faktiskt hamnar.",
       "Ett nytt stuprör behöver inte betyda nya rännor. Är rännan hel och har rätt fall kan stupröret bytas för sig, med en ny utkastare som leder vattnet ut på marken en bit från grunden.",
     ],
     "aside": {"title": "Kommunens råd mot fukt i källaren", "items": [
       "Hela och rätt monterade stuprör", "Utkastare från stuprören",
       "Mark som lutar bort från huset", "Rensad dagvattenbrunn"]}},
    {"id": "takytan", "h2": "Takets storlek avgör hur mycket vatten som kommer",
     "paras": [
       "Kommunen räknar upp vad som avgör hur mycket dagvatten en fastighet lämnar ifrån sig: tomtens storlek, hur mycket som är hårdgjort, jordarten, markens lutning, storleken på taket och hur mycket och hur länge det regnar. Som jämförelse anger kommunen att en nylagd dagvattenservis i plast med 160 millimeters ytterdiameter och 1 procents lutning klarar cirka 22 liter i sekunden.",
       "Rännor och stuprör ska klara samma sak i mindre skala. På ett stort tak med få stuprör blir varje stuprör hårt belastat vid häftiga regn, och rännan svämmar över innan vattnet hinner ner. När vi byter avvattning räknar vi därför på takytan som varje stuprör tar emot, och ibland föreslår vi ett extra stuprör i stället för en större ränna.",
       "Kommunen har också gjort en skyfallskartering som visar var vatten riskerar att samlas vid ett så kallat 100-årsregn, men påpekar att den inte bör användas för att förutsäga risken för enskilda byggnader.",
     ],
     "aside": None},
    {"id": "tallar-tyreso", "h2": "Barr, löv och is i rännorna",
     "paras": [
       "Boverket skriver att utvändig takavvattning kan få problem med att det fryser i rännor och stuprör, att stuprör som går ner till marken kan skadas mekaniskt och att renssilen och anslutningen mot dagvattnet kan lossna. Boverket nämner också att träd runt huset ökar risken för att avvattningen sätts igen.",
       "På en tomt med tallar och björkar fylls rännorna med barr och löv, och vattnet blir stående i rännan i stället för att rinna mot stupröret. Det fryser på vintern och kan bända upp skarvar. Vi ser till att rännan har jämnt fall mot varje stuprör, sätter lövsil i rännans utlopp där det behövs och placerar en rensbar del i stupröret ovanför marken.",
       "Hur ofta rännorna ska rensas beror på träden, men en kontroll varje höst efter lövfällningen är en bra vana. Läs mer under " + _L.format("hangrannor-stupror.html", "hängrännor och stuprör") + ".",
     ],
     "aside": {"title": "Före vintern", "items": [
       "Rensa barr och löv", "Kontrollera fallet i rännan", "Lövsil vid utloppet",
       "Se till att utkastaren är fri"]}},
    {"id": "va-tyreso", "h2": "Duplikatsystem, separering och lov",
     "paras": [
       "När kommunen bygger om en kombinerad avloppsledning i gatan till ett duplikatsystem, med separata ledningar för spillvatten och dagvatten, informerar den berörda fastighetsägare, som då ska separera sitt avlopp inom fastigheten. Kommunen skriver att den inte betalar ersättning för översvämningsskador om fastigheten efter uppmaning inte har separerat avloppet. Stuprör som i dag går till en gemensam ledning kan då behöva kopplas om, så att takvattnet går till dagvattnet eller tas om hand på tomten.",
       "Själva plåtbytet kräver sällan lov. Tyresö kommun skriver att det sedan 1 december 2025 inte krävs bygglov för nytt tak på ett en- eller tvåbostadshus, men påpekar att lov behövs i kulturhistoriskt särskilt värdefulla områden och att uppdaterad information inte finns för alla områden, så det är klokt att fråga kommunen. Mer om taken i kommunen finns under " + _L.format("taklaggare-tyreso.html", "takläggare i Tyresö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett plåtjobb till i Tyresö",
  "steps": [
    ("Runt huset", "Vi börjar nerifrån: stuprörens skick, utkastare, markens lutning och dagvattenbrunnen."),
    ("Upp på taket", "Rännornas fall, skarvar, beslag och hur mycket barr och löv som samlas kontrolleras."),
    ("Dimensionering", "Vi räknar på takytan per stuprör och föreslår eventuella extra stuprör."),
    ("Kostnadsförslag", "Stuprör, rännor och beslag prissätts var för sig så att du kan välja i vilken ordning."),
    ("Byte", "Gamla järnstuprör och rännor tas ner och ny plåt monteras med utkastare och rensdel."),
    ("Avslutning", "Vi visar arbetet och hur rännorna sköts inför vintern."),
  ],
  "rot_h2": "ROT-avdrag för stuprör och rännor i Tyresö",
  "rot": [
    "Att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör ger rotavdrag på ett småhus som du äger och bor i. Att dränera husgrunden finns också med i Skatteverkets lista över godkända arbeten.",
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rut. Material och resor ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Tyresö?",
  "price": [
    "Antalet stuprör och hur långa rännorna är, om bara stuprören eller hela avvattningen ska bytas, hur högt huset är och om det behövs ställning på en sluttande tomt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför rostar stupröret sönder längst ner?",
     "Där samlas vatten, smuts och is, och äldre stuprör av järn tål det sämst. Tyresö kommun skriver att problem med stuprör oftast uppkommer när äldre järnstuprör rostar sönder nere vid källaren."),
    ("Hur långt från huset ska vattnet från stupröret hamna?",
     "Så långt ut att det inte rinner tillbaka mot grunden. Kommunen råder fastighetsägare att använda utkastare och att se till att marken lutar bort från huset."),
    ("Kan vi byta bara stuprören och behålla rännorna?",
     "Ja, om rännorna är hela och har rätt fall. Vi kontrollerar dem vid besöket innan vi föreslår något."),
    ("Hjälper en lövsil mot barr från tallarna?",
     "Den hindrar barr och löv från att följa med ner i stupröret, men rännan behöver ändå rensas. Vi brukar kombinera lövsil med en rensbar del i stupröret."),
    ("Vad ska vi göra när kommunen bygger duplikatsystem i vår gata?",
     "Kommunen informerar berörda fastighetsägare, som då ska separera avloppet inom fastigheten. Stuprören ska då inte gå till spillvattnet. Vi kan göra om stuprören, medan ledningar i mark görs av en VA-entreprenör."),
  ],
  "sources": [
    ("Tyresö kommun – Översvämningsrisker och åtgärder",
     "https://www.tyreso.se/boende--miljo/vatten-och-avlopp/oversvamningsrisker-och-atgarder.html"),
    ("Tyresö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
     "https://www.tyreso.se/boende--miljo/bygga/bygga-riva-eller-andra/forandringar-i-plan--och-bygglagen-fran-1-december-2025.html"),
    _BV_AVV, _BV_TAK, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Läcker stupröret vid källaren?", "Boka ett gratis platsbesök så går vi igenom stuprör, rännor och vattnets väg runt huset."),
  "img": [
    ("Villa i Tyresö bland tallar med nya hängrännor och stuprör i plåt",
     "1960s Swedish single-storey villa with light wooden facade and grey concrete tile roof among tall pine trees on a sloping granite plot, new dark grey half-round gutters and round downpipes ending in curved outlet spouts, Tyresö, early autumn, no people, no text"),
    ("Hängränna med tallbarr och löv vid takfoten på en villa",
     "view along a grey metal half-round gutter hung below the eaves of a grey concrete tile roof on a Swedish villa, the inside of the gutter holding a layer of brown pine needles and a few yellow birch leaves, gutter brackets visible, pine branches and a pine forest blurred in the background, daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VÄRMDÖ
"platslagare-varmdo.html": {
  "kind": "district", "service": "platslagare", "ort": "Värmdö", "svc_label": "Plåtslagare",
  "title": "Plåtslagare på Värmdö – skärgårdsbyar, vind och takfönster",
  "description": "Plåtslagare på Värmdö: plåttak i riksintressen och kulturmiljöområden, anmälan vid underhåll av skyddade hus och beslag i blåsiga lägen.",
  "h1": "Plåtslagare på Värmdö",
  "lead": "Värmdö kommun har fjorton riksintressen för kulturmiljövården och ett 55-tal utpekade kulturmiljöområden, från Gustavsbergs brukssamhälle till fiskarmiljöerna på Möja och skärgårdsbyn Harö. Där krävs bygglov även för ett nytt tak. Geal Entreprenad AB har egna plåtslagare som arbetar i Gustavsberg, Hemmesta, på Ingarö, Djurö och i övriga Värmdö, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Plåttak och beslag på Värmdö.",
  "sections": [
    {"id": "riksintressen", "anchor": "Kulturmiljöer på Värmdö",
     "h2": "Fjorton riksintressen och ett 55-tal kulturmiljöområden",
     "paras": [
       "Kommunen skriver att Värmdö har 14 områden av riksintresse och cirka 55 utpekade kulturmiljöområden, och att alla räknas som särskilt värdefulla. Riksintressena är utpekade av länsstyrelsen, länsmuseet och Riksantikvarieämbetet och omfattar bland annat Gustavsbergs brukssamhälle, skärgårdsbyarna på Harö, Husarö, Ingmarsö, Svartsö, Gällnö och Hjälmö, fiskarmiljöerna på Möja, Bockö och Lökaön, sommarnöjesmiljön på Grinda och Sandhamn med Grönskär.",
       "Bland de lokala kulturmiljöerna i programmet Skärgårdsbygd, framtaget av Stockholms läns museum och kommunen, nämns Norra Lagnö, Stavsnäs by och Säby på Ingarö. Kommunen ber den som ska bygga i en kulturmiljö att fundera särskilt på material och byggnadssätt, färger, fönster och dörrar och takets form och lutning.",
       "För en plåtslagare innebär det att ett tak i en skärgårdsby inte bara ska vara tätt. Bandbredd, falsens höjd, kulör och hur plåten avslutas vid gavel och takfot är en del av det som ska passa in.",
     ],
     "aside": {"title": "Några av Värmdös riksintressen", "items": [
       "Gustavsberg – brukssamhälle", "Harö – skärgårdsby", "Möja, Bockö, Lökaön – fiskarmiljöer",
       "Sandhamn och Grönskär", "Grinda – sommarnöjesmiljö"]}},
    {"id": "lov-varmdo", "h2": "Nytt tak, takfönster och solceller kräver lov i kulturmiljöerna",
     "paras": [
       "Enligt kommunens sida om fasadändring krävs inget bygglov för fasadändring, nytt tak eller nya fönster på ett en- eller tvåbostadshus eller en komplementbyggnad. Men om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område, eller om byggnaden är särskilt värdefull, krävs bygglov för åtgärder som ommålning, nytt tak, nya fönster, solceller och takfönster.",
       "Kommunen skriver också att du behöver göra en anmälan och få startbesked för att underhålla en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde. Byggnadsminnen och kyrkliga kulturminnen kräver tillstånd från länsstyrelsen. Ligger fastigheten inom strandskyddat område kan dispens behövas.",
       "Kommunantikvarien hjälper gärna till. Kommunen föreslår att du tar en promenad i området, fotograferar fastigheten och mejlar kommunantikvarien innan arbetet planeras. Ska ett takfönster sättas in samtidigt, se " + _L.format("takfonster.html", "takfönster") + ".",
     ],
     "aside": None},
    {"id": "vind-varmdo", "h2": "Där det regnar och blåser mycket",
     "paras": [
       "Boverket skriver att regn i kombination med vind ökar sannolikheten för att vatten pressas eller sugs in i springor och skarvar, och att risken därför är större där det regnar och blåser mycket. Tak med många vinklar, kupor och takfönster får fler skarvar och anslutningar. Otäta infästningar för solceller, taksäkerhetsutrustning, luckor och huvar nämns som vanliga orsaker till läckage.",
       "Ett hus på en udde eller en klippa ut mot fjärden tar emot väder från flera håll. Där lägger vi extra vikt vid vindskivornas infästning, vid nockens och gavelns beslag och vid att plåten vid takfoten sitter fast även när vinden lyfter underifrån. Genomföringar placeras med tillräckligt avstånd så att de går att täta ordentligt.",
       "Läs mer om skärgårdens tak i stort under " + _L.format("takrenovering-varmdo.html", "takrenovering på Värmdö") + ".",
     ],
     "aside": {"title": "Utsatta punkter i blåsiga lägen", "items": [
       "Vindskivor och gavelbeslag", "Nockplåt", "Fotplåt som vinden lyfter",
       "Infästningar för stegar och solceller"]}},
    {"id": "pfo-varmdo", "h2": "När fritidshusområdet blir ett villaområde",
     "paras": [
       "Kommunens broschyr Fritidshusområde i förändring från 2023 beskriver hur tusentals fastigheter i prioriterade förändringsområden ska planläggas och få kommunalt vatten och avlopp. I utredningsskedet kartlägger kommunen bland annat dagvattenflöden. När detaljplanen har vunnit laga kraft och vatten och avlopp är utbyggt kan man söka bygglov.",
       "Det är ofta då ett sommarhus byggs till eller om till helårsbostad, och takets plåt och avvattning behöver räcka för ett större hus. Riktlinjerna säger att områdenas karaktär ska bibehållas och att ny bebyggelse ska anpassas till befintlig bebyggelse och kulturmiljö. Vi planerar därför rännor och stuprör för den nya takytan och väljer plåt som passar det befintliga huset.",
       "En tillbyggnad får ofta ett eget takfall som möter det gamla taket i en vinkel. Där bildas en ränndal eller en anslutning mot väggen, och det är just sådana möten som Boverket pekar ut som känsliga för läckage. Vi bockar plåten i ränndalen och i väggens uppvik så att vattnet leds förbi skarven mellan det gamla och det nya, och ser till att den nya rännan ansluter till stupröret med rätt fall.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med plåten på Värmdö",
  "steps": [
    ("Var ligger huset?", "Vi kontrollerar i Värmdökartan om fastigheten ligger i ett riksintresse eller kulturmiljöområde."),
    ("Besök", "Tak, beslag, rännor och genomföringar granskas, med särskild uppmärksamhet på de vindutsatta sidorna."),
    ("Lov eller anmälan", "Behövs bygglov eller anmälan tar vi fram underlag om plåtens utförande och kulör."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där varje del av plåtarbetet står för sig."),
    ("Montering", "Plåten monteras med extra infästning vid gavlar, nock och takfot."),
    ("Genomgång", "Vi visar arbetet och vad som är bra att kontrollera efter en storm."),
  ],
  "rot_h2": "Rotavdrag för plåtarbete på Värmdö",
  "rot": [
    "Skatteverket räknar ett fritidshus som småhus, och att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör ger rotavdrag om du äger huset och använder det som bostad. Byggnadsställning i samband med arbetet ingår.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kr per person och år, inom 75 000 kr för rot och rut tillsammans. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Värmdö?",
  "price": [
    "Takets form och antalet genomföringar, om plåten ska tillverkas efter förlaga i en kulturmiljö och hur mycket extra infästning ett utsatt läge kräver. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för nytt plåttak i en skärgårdsby på Värmdö?",
     "Ligger fastigheten i ett av kommunens riksintressen eller kulturmiljöområden räknas den som särskilt värdefull, och då krävs bygglov för nytt tak. Utanför de områdena krävs normalt inget lov."),
    ("Måste vi göra en anmälan för att laga plåten på ett skyddat hus?",
     "Kommunen skriver att underhåll av en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde kräver anmälan och startbesked."),
    ("Kan kommunantikvarien hjälpa oss att välja plåt och kulör?",
     "Kommunen skriver att kommunantikvarien gärna ger tips och råd. Fotografera fastigheten och mejla kommunantikvarien innan arbetet planeras."),
    ("Hur sätter ni fast plåten på ett hus som står ute på en klippa?",
     "Med tätare infästning vid gavlar, nock och takfot, där vinden får tag, och med genomföringar placerade så att de går att täta ordentligt."),
    ("Var ser vi om fastigheten ligger i ett kulturmiljöområde på Värmdö?",
     "I Värmdökartan, där kommunens kulturmiljöområden är utmärkta. Är du osäker kan du fråga kommunantikvarien."),
  ],
  "sources": [
    ("Värmdö kommun – Bygglov vid fasadändring",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/bygglovvidfasadandring.4.1a14d9c818e5a4c406a626d.html"),
    ("Värmdö kommun – Bygga i kulturmiljöer",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/byggaikulturmiljoer.4.57b4a3ba16e6b961dbf10429.html"),
    ("Värmdö kommun – Kulturmiljö och byggnadsvård",
     "https://www.varmdo.se/upplevaochgora/turist/kulturmiljoochbyggnadsvard.4.50cc920016fa8c77c58edccd.html"),
    ("Värmdö kommun – Fritidshusområde i förändring, del 1 Planering (2023, pdf)",
     "https://www.varmdo.se/download/18.52346f71869c9938611c2df/1678200543391/Broschyr%20PFO%20del%201%20-%20uppdaterad%202023.pdf"),
    _BV_LACK, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver plåten på huset på Värmdö ses över?", "Boka ett gratis platsbesök så går vi igenom tak, beslag och lovfrågan tillsammans."),
  "img": [
    ("Rött trähus med svart falsat plåttak på en klippa i Värmdös skärgård",
     "traditional falu red Swedish archipelago wooden house with white trim and a black standing-seam metal roof with neat gable flashings, on granite rocks by the sea with windswept pines, Stockholm archipelago Värmdö, clear breezy day with small waves, no boats, no people, no text"),
    ("Vindskiva i plåt vid gaveln på ett skärgårdshus med havet i bakgrunden",
     "close-up of the corner where a black standing-seam metal roof with straight vertical seams meets the gable, a neat black folded metal ridge cap along the top and a black metal-clad barge board along the gable edge, falu red vertical board wall below, blurred Baltic archipelago sea and low rocky islands in the background, daylight, no people, no hands, no text"),
  ],
  "related": [],
},

}
