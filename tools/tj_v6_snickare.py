# -*- coding: utf-8 -*-
"""Snickare – ortsidor v6: Ekerö, Värmdö, Haninge, Vallentuna, Österåker, Järfälla (2026-10-25).
Schema: se tools/tj_check.py. Fakta endast från källorna i respektive sidas "sources", öppnade
2026-10-25: Ekerö kommun (Vad vill du bygga?; Strandskydd, bryggor och sjöbodar), Värmdö kommun
(Förändringar i PBL från 1 december 2025; Fritidshusområde i förändring del 1, 2023), Haninge kommun
(Altan och trädäck; Skärmtak; Staket och spaljéer; Haninges karaktärsmiljöer), Vallentuna kommun
(Altan; Nybyggnad av komplementbyggnad; Inglasat uterum; Översiktsplan 2040), Österåkers kommun
(Bygglovsguiden; Altan; Bryggor och sjöbodar), Järfälla kommun (Bygglovsbefriade åtgärder;
Kulturmiljöplan Jakobsberg), Boverket (Bygga en ny byggnad; Göra en tillbyggnad; Mur, plank, altan
och annat; Ingrepp i husets bärande delar) och Skatteverket (Ger arbetet rätt till rotavdrag?;
Så fungerar rotavdraget).
Strukna (ej verifierade): andel fritidshus/permanentade hus per kommun, antal strandnära tomter,
husens byggår per område (utöver det källorna anger), vanliga altanmaterial lokalt, nockhöjd för
komplementbyggnad utanför detaljplan i Vallentuna (kommunen skriver 4 m, Boverket 4,5 m – utelämnad).
Inga priser, garantier, omdömen, egna uppdrag eller cert."""

L = 'class="text-link"'

# Gemensamma källor
BV_NY = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/bygga-en-ny-byggnad/"
BV_TILL = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/gora-en-tillbyggnad/"
BV_ALTAN = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/mur-plank-altan-och-annat/"
BV_BAR = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/ingrepp-i-husets-barande-delar/"
SKV_ARB = "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html"
SKV_ROT = "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html"

# Ekerö
E_BYGG = "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/vad-vill-du-bygga"
E_STR = "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/strandskydd-bryggor-och-sjobodar"

# Värmdö
V_PBL = "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/forandringaripblfrom1december2025.4.18b9914519a768a188a2872.html"
V_PFO = ("https://www.varmdo.se/download/18.52346f71869c9938611c2df/1678200543391/"
         "Broschyr%20PFO%20del%201%20-%20uppdaterad%202023.pdf")

# Haninge
H_B = "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/"
H_ALT = H_B + "altan-och-tradack/"
H_SKARM = H_B + "skarmtak/"
H_STAKET = H_B + "staket-och-spaljeer/"
H_KAR = "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf"

# Vallentuna
VA_B = "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/behover-jag-bygglov/"
VA_ALT = VA_B + "altan"
VA_KOMP = VA_B + "nybyggnad-av-komplementbyggnad"
VA_UTE = VA_B + "inglasat-uterum"
VA_OP = ("https://vallentuna.se/download/18.63572f8619eeecafce08366/1782478377449/"
         "2.11.7%20%C3%96versiktsplan%202040.pdf")

# Österåker
O_B = "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/"
O_GUIDE = O_B + "bygglovsguiden.4.21374a1619a9c24e54e4acc.html"
O_ALT = O_B + "bygglovsguiden/altan.4.24daed7e19aff7a0474e79.html"
O_BRY = O_B + "bygglovsguiden/bryggorochsjobodar.4.24daed7e19aff7a04749c2.html"
O_UTE = O_B + "bygglovsguiden/uterum.4.24daed7e19aff7a0474ea2.html"

# Järfälla
J_BEFR = ("https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/"
          "bygglovsbefriadeatgarder.4.a41712119a05132defe8bb3.html")
J_JAK = "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4080/1550245872956/kulturmiljoplan-jakobsberg.pdf"


def a(href, text):
    return f'<a {L} href="{href}">{text}</a>'


def ext(href, text):
    return f'<a {L} href="{href}" rel="noopener">{text}</a>'


PAGES_TJ = {

# ---------------------------------------------------------------- EKERÖ
"snickare-ekero.html": {
  "kind": "district", "service": "snickare", "ort": "Ekerö", "svc_label": "Snickare",
  "title": "Snickare i Ekerö – altan, gäststuga och brygga",
  "description": "Snickare i Ekerö: altan efter kommunens höjdregler, gäststuga och förråd enligt PBL "
                 "2025, strandskydd för brygga och sjöbod. Gratis platsbesök.",
  "h1": "Snickare i Ekerö",
  "lead": "På Mälaröarna ligger många tomter nära vatten, och en del ligger inom detaljplan medan andra "
          "inte gör det. Det avgör mer än man tror när en altan, en gäststuga eller en brygga ska byggas. "
          "Geal Entreprenad AB bygger altaner, trappor och mindre byggnader i hela Ekerö kommun och börjar "
          "med att reda ut vilka regler som gäller just din tomt.",
  "card": "Altan, gäststuga och snickeri nära Mälaren.",
  "sections": [
    {"id": "altan-ekero", "anchor": "Altanen",
     "h2": "Altanens höjd avgör – kommunens tre gränser",
     "paras": [
       "Ekerö kommun beskriver en altan som en golvkonstruktion ovanpå mark som används som uteplats. "
       "Enligt " + ext(E_BYGG, "kommunens sida om vanliga byggprojekt") + " krävs inte bygglov för en altan "
       "utanför detaljplanelagt område. Inom detaljplan går gränserna vid två höjder: en altan lägre än 1,2 "
       "meter är lovfri oavsett var den placeras, och en altan mellan 1,2 och 1,8 meter är lovfri om den "
       "ligger inom 3,6 meter från bostadshuset och minst 4,5 meter från tomtgränsen.",
       "Över 1,8 meter krävs bygglov. Det gör det också om du bygger ett rum under altanen, till exempel ett "
       "förråd, eller om altanen byggs in med glas. Kommunen påpekar att det gäller både fristående altaner "
       "och sådana som byggs ihop med huset.",
       "På en sluttande tomt kan samma altan vara låg mot huset och hög ute vid kanten. Därför mäter vi "
       "marken vid platsbesöket innan stommen ritas, så att höjden vid altanens högsta punkt är känd från "
       "början."],
     "aside": {"title": "Inom detaljplan i Ekerö",
               "items": ["Under 1,2 m: lovfri var som helst",
                         "1,2–1,8 m: inom 3,6 m från huset",
                         "Över 1,8 m: bygglov",
                         "Inglasning eller rum under: bygglov"]}},
    {"id": "gaststuga",
     "h2": "Gäststuga och förråd efter 1 december 2025",
     "paras": [
       "Kommunen skriver att det som tidigare kallades attefallsåtgärder och friggebod nu samlas under "
       "bygglovsbefriade komplementbyggnader, komplementbostadshus och tillbyggnader. En komplementbyggnad "
       "får vara högst 30 kvadratmeter inom detaljplan och 50 utanför, med en nockhöjd på högst 4 respektive "
       "4,5 meter. Alla sådana byggnader på tomten får tillsammans vara högst 45 kvadratmeter inom detaljplan "
       "och 65 utanför.",
       "Redan byggda attefallshus och friggebodar räknas in i den potten. Står det en friggebod från 1990-talet "
       "vid tomtgränsen är den alltså en del av räkningen. Mer om de nya reglerna finns på sidan om " +
       a("attefallshus-regler.html", "attefallshus och regler") + ".",
       "Blir gäststugan ett komplementbostadshus, med eget kök, toalett och dusch, behöver du meddela "
       "kommunen när bostaden är klar så att lägenhetsregistret kan uppdateras. Ska den anslutas till "
       "kommunalt vatten och avlopp skickas en anmälan till Roslagsvatten i god tid, och med eget avlopp kan "
       "det behövas tillstånd eller anmälan om mängden avloppsvatten ökar."],
     "aside": None},
    {"id": "brygga-ekero",
     "h2": "Brygga och sjöbod vid Mälaren",
     "paras": [
       "Enligt " + ext(E_STR, "kommunens sida om strandskydd") + " gäller det generella strandskyddet 100 meter "
       "från strandkanten, på vissa ställen upp till 300 meter, och det omfattar både land och vatten. Inom "
       "området är det förbjudet att bygga nya byggnader, även komplementbyggnader, och att bygga bryggor "
       "eller staket som försämrar tillgängligheten. För det krävs dispens, och dispens kräver särskilda skäl.",
       "Ligger vattnet utanför tomten på kommunens mark kan du ansöka om att arrendera vattenområdet för en "
       "brygga. Kommunen understryker att ett arrende inte garanterar dispens, och att en detaljplan kan styra "
       "hur och var bryggan får byggas. En sjöbod kräver dessutom bygglov.",
       "Till en dispensansökan hör bland annat situationsplan, plan- och elevationsritning och en beskrivning "
       "av botten och växt- och djurlivet. Vi kan ta fram ritningsunderlaget för bryggan; själva ansökan "
       "skickar du som fastighetsägare."],
     "aside": {"title": "Inom strandskydd krävs dispens för",
               "items": ["Ny byggnad, även förråd eller gäststuga",
                         "Ändrad användning av en byggnad",
                         "Ny brygga eller nytt staket",
                         "Att utöka den privata zonen"]}},
    {"id": "kartan-ekero",
     "h2": "Ekerökartan före spaden i marken",
     "paras": [
       "I och med lagändringarna har kommunen gjort en ny bedömning av sina särskilt värdefulla byggnader och "
       "områden. Inom dem kan de nya undantagen inte användas, och detsamma gäller om en tillbyggnad eller "
       "komplementbyggnad hamnar närmare gräns än 4,5 meter utan grannarnas skriftliga medgivande.",
       "Kommunen pekar också ut områden för totalförsvarets riksintressen. Där får du inte bygga ett "
       "bygglovsbefriat komplementbostadshus eller inreda ytterligare en bostad i ett enbostadshus. Därför "
       "börjar vi varje snickeriuppdrag i Ekerö med att titta på fastigheten i kommunens karta tillsammans "
       "med dig."],
     "aside": None}],
  "steps_h2": "Så går ett snickeriuppdrag i Ekerö till",
  "steps": [
    ("Kartan först", "Vi ser om tomten ligger inom detaljplan, strandskydd eller ett särskilt värdefullt område."),
    ("Platsbesök", "Vi mäter marknivåer, avstånd till tomtgräns och till vattnet och ser vad som redan finns på tomten."),
    ("Potten räknas", "Tidigare friggebod, attefallshus och skärmtak läggs ihop så att du vet hur mycket som återstår."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med arbete och material på separata rader."),
    ("Bygge", "Grund, stomme och trall eller panel byggs enligt ritningen, med trappor och räcken där höjden kräver det."),
    ("Genomgång", "Vi går igenom resultatet med dig och lämnar underlag du kan spara för fastigheten.")],
  "rot_h2": "ROT för snickeri i Ekerö",
  "rot": [
    "Enligt " + ext(SKV_ARB, "Skatteverket") + " ger en altan till ett småhus rotavdrag om den byggs ihop med "
    "huset. Ett fritidshus räknas också som småhus. Att bygga en helt ny fristående byggnad, som en "
    "friggebod, ett garage eller ett växthus, ger däremot inget avdrag, och inte heller att reparera "
    "båtbryggor eller staket.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag, enligt " + ext(SKV_ROT, "Skatteverkets genomgång") + ". Material och resor "
    "ingår inte. Vi drar avdraget direkt på fakturan."],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "Altanens yta och höjd, hur mycket marken sluttar och om det behövs trappor och räcken påverkar mest. För "
    "en gäststuga väger grunden och om den ska bli bostad tyngst, för en brygga förhållandena i vattnet. "
    "Platsbesöket är gratis och du får ett skriftligt kostnadsförslag."],
  "faq": [
    ("Behöver en altan på 1,5 meters höjd bygglov i Ekerö?",
     "Inom detaljplan inte, om den ligger inom 3,6 meter från bostadshuset och minst 4,5 meter från tomtgränsen. "
     "Utanför detaljplan krävs inget bygglov för altanen."),
    ("Räknas vår gamla friggebod in när vi bygger gäststuga i Ekerö?",
     "Ja. Kommunen skriver att tidigare friggebodar och attefallsåtgärder räknas in i de totala ytor som får "
     "byggas utan bygglov."),
    ("Kan vi arrendera vattnet framför tomten för en brygga i Ekerö?",
     "Om vattenområdet ägs av kommunen kan du ansöka om arrende. Arrendet ger dock ingen dispens från "
     "strandskyddet, den måste sökas separat."),
    ("Måste kommunen få veta när gäststugan i Ekerö blir en bostad?",
     "Ja. När ett komplementbostadshus är klart ska du meddela kommunen så att lägenhetsregistret kan "
     "uppdateras, även om bygget i sig var lovfritt."),
    ("Ger en ny sjöbod i Ekerö rotavdrag?",
     "Nej, en ny fristående byggnad ger inget rotavdrag. En sjöbod kräver dessutom bygglov och inom "
     "strandskyddat område även dispens.")],
  "sources": [
    ("Ekerö kommun – Vad vill du bygga?", E_BYGG),
    ("Ekerö kommun – Strandskydd, bryggor och sjöbodar", E_STR),
    ("Boverket – Bygga en ny byggnad", BV_NY),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska altanen, gäststugan eller bryggan byggas i Ekerö?",
          "Boka ett gratis platsbesök så går vi igenom tomten, kartan och reglerna innan något ritas."),
  "img": [("Ny trätrall vid ett rödmålat trähus med utsikt mot Mälaren i Ekerö",
           "newly built wooden deck terrace with simple wooden railing and a few steps down to the lawn, attached "
           "to a falu red Swedish wooden house with white window frames, lawn sloping down to a calm lake with "
           "reeds, birch and pine trees, Mälaren islands Ekerö Stockholm, late summer afternoon, no people, no text"),
          ("Liten gäststuga i trä under uppbyggnad på en gräsbevuxen tomt",
           "small Swedish wooden guest cabin under construction on a lawn, new light timber frame and partly "
           "mounted vertical wooden panel, concrete plinth foundation, sawhorses and neatly stacked boards, birch "
           "trees, countryside garden, overcast daylight, no people, no hands, no text")],
  "related": [],
},

# ---------------------------------------------------------------- VÄRMDÖ
"snickare-varmdo.html": {
  "kind": "district", "service": "snickare", "ort": "Värmdö", "svc_label": "Snickare",
  "title": "Snickare på Värmdö – när stugan blir helårshus",
  "description": "Snickare på Värmdö: dörrar, fönster och väggar när fritidshuset blir helårshus, altan "
                 "i berg och sluttning, lovfritt efter PBL 2025. Gratis platsbesök.",
  "h1": "Snickare på Värmdö",
  "lead": "Allt fler bor året runt i det som byggdes som sommarhus på Värmdö. Då märks snickeriet: dörrar som "
          "drar, fönster som var tänkta för juli snarare än januari, väggar som delar upp små rum och en trappa till "
          "loftet som bara fungerade på sommaren. Geal Entreprenad AB gör snickeriarbeten på hela Värmdö, inne "
          "och ute, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Fritidshus som blir helårshus.",
  "sections": [
    {"id": "permanent", "anchor": "Helårshuset",
     "h2": "Tusentals fritidshus på väg mot permanentboende",
     "paras": [
       "Värmdö kommuns broschyr " + ext(V_PFO, "Fritidshusområde i förändring") + " beskriver hur fler och fler "
       "väljer att bosätta sig permanent i kommunens fritidshusområden. Många av dem ska planläggas och få "
       "kommunalt vatten och avlopp, och det handlar om tusentals fastigheter. De områden som först ska "
       "anpassas kallas prioriterade förändringsområden och pekas ut i översiktsplanen Värmdö 2035.",
       "Enligt broschyren pågår planprocessen normalt två till tre år fram till antagande, och det är först när "
       "detaljplanen har vunnit laga kraft och vatten och avlopp är utbyggt som man kan söka bygglov i "
       "området. Riktlinjerna säger att byggrätterna ses över och att det inom fastigheten ska finnas plats för "
       "parkering, ett möjligt attefallshus och bergvärme.",
       "För den som väntar på planen finns ändå mycket att göra inne i huset, där lov sällan behövs men där ett "
       "helt år av vardag ställer andra krav än några sommarveckor."],
     "aside": {"title": "Vanligt i ett sommarhus som blir helårshus",
               "items": ["Ytterdörrar som släpper in drag",
                         "Brant trappa eller stege till loftet",
                         "Små rum med lätta mellanväggar",
                         "Fönster och foder som behöver ses över"]}},
    {"id": "vaggar-dorrar",
     "h2": "Väggar, dörrar och fönster – när krävs anmälan?",
     "paras": [
       "Boverket förklarar på sidan om " + ext(BV_BAR, "ingrepp i husets bärande delar") + " att det krävs en "
       "anmälan till byggnadsnämnden och ett startbesked om ändringen påverkar de bärande delarna väsentligt. "
       "Att riva en vägg som inte är bärande, eller göra en befintlig öppning större där en balk klarar "
       "belastningen, kräver ingen anmälan. Boverket rekommenderar att ta hjälp av en konstruktör för att "
       "avgöra vilka delar som bär.",
       "Samma sak gäller för nya fönster och dörrar. Ett fönster eller en dörr med samma bredd som den "
       "tidigare påverkar normalt inte konstruktionen väsentligt, och då behövs varken anmälan eller lov. Ska "
       "öppningen breddas så att en regel eller ett hammarband kapas är det en annan sak.",
       "I ett gammalt sommarhus är mellanväggarna ofta lätta, men en vägg mitt i huset kan bära bjälklaget till "
       "loftet. Vi öppnar en bit av väggen och tittar innan något rivs. Byte av fönster beskrivs närmare på "
       "sidan om " + a("fonsterbyte.html", "fönsterbyte") + "."],
     "aside": None},
    {"id": "berg",
     "h2": "Altan och trappa i berg och sluttning",
     "paras": [
       "Bland riktlinjerna för de prioriterade förändringsområdena står att sprängning, schakt och stora "
       "utfyllnader bör undvikas och att nya byggnader ska anpassas efter topografin. För en altan eller en "
       "entrétrappa på en bergig tomt brukar det betyda plintar eller stolpar som följer berget i stället för "
       "att marken jämnas ut.",
       "Enligt " + ext(BV_ALTAN, "Boverket") + " finns det inom detaljplan ingen bygglovsplikt för en altan "
       "som är högst 1,8 meter och ligger inom 3,6 meter från huset, eller högst 1,2 meter längre ut. Utanför "
       "detaljplan finns inga sådana mått att följa, men altanen ska ändå anpassas till omgivningen och får inte "
       "bli en betydande olägenhet för grannarna."],
     "aside": None},
    {"id": "pott-varmdo",
     "h2": "Lovfritt på Värmdö – men inte nära strand eller gräns",
     "paras": [
       "Kommunens sida om " + ext(V_PBL, "förändringarna i plan- och bygglagen") + " påminner om att det fortsatt "
       "inte är tillåtet att utan tillstånd bygga närmare än 4,5 meter från tomtgränsen eller inom 100 meter "
       "från strand. Har du redan byggt en friggebod, ett skärmtak eller en attefallsåtgärd räknas den in i den "
       "nya potten.",
       "Inom kulturhistoriskt värdefulla områden och områden av riksintresse för kulturmiljövården gäller "
       "alltjämt lovplikt, och kommunen hänvisar till sin kulturmiljökarta. Ansvaret för att bygget följer "
       "lagen ligger på dig som äger fastigheten, därför går vi igenom kartan och det som redan står på tomten "
       "innan vi ritar."],
     "aside": {"title": "Kolla innan du bygger",
               "items": ["Avstånd till tomtgräns",
                         "Avstånd till strandlinjen",
                         "Tidigare friggebod och skärmtak",
                         "Kommunens kulturmiljökarta"]}}],
  "steps_h2": "Så går ett snickeriuppdrag på Värmdö till",
  "steps": [
    ("Besök i huset", "Vi går igenom dörrar, fönster, trappor och väggar och ser vad sommarhuset behöver för vintern."),
    ("Bärande eller inte", "Vi öppnar där det behövs och avgör om en vägg bär, och om en konstruktör ska kopplas in."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med arbete och material på separata rader."),
    ("Anmälan vid behov", "Påverkas bärande delar väsentligt tar vi fram underlag för anmälan och väntar på startbesked."),
    ("Snickeriet", "Väggar, dörrar, foder, trappor eller altan byggs i den ordning som huset kräver."),
    ("Genomgång", "Vi går igenom resultatet med dig och lämnar en sammanställning av vad som gjorts.")],
  "rot_h2": "ROT när fritidshuset byggs om",
  "rot": [
    "Skatteverket räknar ett " + a("fritidshus.html", "fritidshus") + " som småhus, så samma regler gäller som för "
    "en villa. Att byta och reparera dörrar, dörrlås och handtag ger avdrag, liksom att reparera eller byta "
    "fönster och att reparera entrétrappor. Ombyggnad och tillbyggnad kräver att bostaden är äldre än fem år.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag. Material och resor ingår inte, enligt " + ext(SKV_ROT, "Skatteverket") + ". "
    "Vi drar avdraget direkt på fakturan."],
  "price_h2": "Vad påverkar kostnaden?",
  "price": [
    "Om en vägg är bärande, hur många dörrar och fönster som berörs och i vilket skick stommen är under "
    "panelen väger tyngst. Utomhus styr berget och höjden mest hur en altan eller trappa byggs. Platsbesöket är "
    "gratis och du får ett skriftligt kostnadsförslag."],
  "faq": [
    ("Kan vi riva väggen mellan kök och vardagsrum i sommarstugan på Värmdö utan anmälan?",
     "Ja, om väggen inte är bärande eller om en befintlig balk klarar belastningen. Påverkas bärande delar "
     "väsentligt krävs anmälan och startbesked innan arbetet börjar."),
    ("När kan vi söka bygglov i ett förändringsområde på Värmdö?",
     "Enligt kommunens broschyr först när detaljplanen har vunnit laga kraft och vatten och avlopp har byggts "
     "ut i området."),
    ("Kräver en ny ytterdörr i samma storlek anmälan på Värmdö?",
     "Nej, normalt inte. En dörr med samma bredd som den gamla påverkar sällan konstruktionen väsentligt, och "
     "då krävs varken anmälan eller lov."),
    ("Får vi bygga en altan i berget nära vattnet på Värmdö?",
     "Inom 100 meter från strand krävs tillstånd enligt kommunen, även för det som annars är lovfritt. "
     "Utanför strandskyddet styr avståndet till tomtgräns och detaljplanen."),
    ("Räknas fritidshuset på Värmdö som småhus för rotavdrag?",
     "Ja. Skatteverket nämner fritidshus som ett exempel på småhus, så dörrar, fönster och entrétrappor ger "
     "avdrag på samma sätt som i en villa.")],
  "sources": [
    ("Värmdö kommun – Fritidshusområde i förändring, del 1 Planering (pdf, 2023)", V_PFO),
    ("Värmdö kommun – Förändringar i PBL från 1 december 2025", V_PBL),
    ("Boverket – Ingrepp i husets bärande delar", BV_BAR),
    ("Boverket – Mur, plank, altan och annat", BV_ALTAN),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska sommarhuset på Värmdö fungera hela året?",
          "Boka ett gratis platsbesök så går vi igenom väggar, dörrar och trappor och lämnar ett skriftligt förslag."),
  "img": [("Rödmålat fritidshus på en bergknalle med ny trätrappa och liten altan på Värmdö",
           "small falu red Swedish wooden summer cottage with white trim on a granite rock outcrop among pine "
           "trees, a newly built wooden entrance stair and small deck on wooden posts following the uneven rock, "
           "Stockholm archipelago Värmdö, calm sea glimpse between pines, early autumn, no people, no text"),
          ("Ny innerdörr med vitmålade foder i ett ljust fritidshus",
           "interior of a bright Swedish wooden summer house being renovated for year-round living, newly fitted "
           "white panel interior door with simple white painted wooden architraves, light pine floor, wooden "
           "panel walls, narrow steep wooden stair to a loft in the background, daylight, no people, no hands, no text")],
  "related": [],
},

# ---------------------------------------------------------------- HANINGE
"snickare-haninge.html": {
  "kind": "district", "service": "snickare", "ort": "Haninge", "svc_label": "Snickare",
  "title": "Snickare i Haninge – veranda, altan och skärmtak",
  "description": "Snickare i Haninge: verandor och snickarglädje i Dalarö, altan och skärmtak efter "
                 "kommunens regler och karaktärsmiljöerna. Gratis platsbesök.",
  "h1": "Snickare i Haninge",
  "lead": "Haninge rymmer sommarnöjen med glasverandor i Dalarö, gårdar med farstukvistar på landsbygden och "
          "grupphusområden från 1960- och 70-talen. Kommunens dokument Haninges karaktärsmiljöer ger råd om "
          "snickeriet i alla tre. Geal Entreprenad AB bygger och lagar altaner, verandor, trappor och skärmtak "
          "i hela Haninge, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Verandor, altaner och skärmtak.",
  "sections": [
    {"id": "dalaro", "anchor": "Verandorna",
     "h2": "Glasverandor och snickarglädje i Dalarö",
     "paras": [
       "I " + ext(H_KAR, "Haninges karaktärsmiljöer") + " beskrivs sommarnöjena från 1860- till 1920-talet som "
       "områden med stora villor i trä och varierande arkitektur, med bland annat stora glasverandor och "
       "snickarglädje. Dalarö och Smådalarö nämns som exempel. Till de tongivande detaljerna räknas träpanel, "
       "spröjsade fönster, torn och brutna tak.",
       "Dokumentet säger att den ursprungliga fönstersättningen ska vara vägledande, och att lusthus, båthus "
       "och bryggor ska värnas. För en snickare betyder det att en rötskadad verandastolpe eller ett trasigt "
       "lövsågat krön lagas i samma form, och att en spröjsad båge byts mot en likadan och inte mot ett "
       "helglas.",
       "Ett lusthus eller en veranda som har stått i hundra år har ofta skador i nedre delen, där vatten blir "
       "stående. Vi byter de skadade partierna och sparar resten."],
     "aside": {"title": "Detaljer att spara på ett sommarnöje",
               "items": ["Glasverandans spröjsade bågar",
                         "Lövsågade krön och konsoler",
                         "Lusthus och båthus",
                         "Ursprunglig fönstersättning"]}},
    {"id": "farstukvist",
     "h2": "Farstukvist och spegeldörr på landsbygden",
     "paras": [
       "Bland de äldre byggnadstyperna på Haninges landsbygd visar karaktärsmiljöerna dubbelradstugan, med "
       "farstukvist, snickarglädje och spegeldörr, och salsbyggnaden med en markerad veranda. Om fönster och "
       "dörrar säger dokumentet att de har en starkt karaktärsbärande effekt, att ursprungliga fönster i "
       "möjligaste mån bör bevaras och att ursprunglig utformning ska eftersträvas vid byte.",
       "För den agrara miljön ger dokumentet också råd om nya uteplatser. En terrass, altan eller ett inglasat "
       "uterum ska vara i proportion till huvudbyggnaden. Altan i kuperad terräng bör undvikas eftersom höga "
       "pelare ger ett dominerande intryck, och altanens undersida bör inte kläs in, eftersom volymen då "
       "upplevs större.",
       "En ny farstukvist på en gammal gård kan alltså vara rätt val, medan ett stort trädäck på höga stolpar "
       "mot åkern sällan är det."],
     "aside": None},
    {"id": "grupphus",
     "h2": "Altan vid grupphusen i Jordbro, Brandbergen och Handen",
     "paras": [
       "Rekordårens småhus i Haninge finns enligt karaktärsmiljöerna bland annat i Jordbro, Brandbergen, "
       "Västerhaninge och Handen, ofta som grupphus med upprepade volymer mot gatan. Mot 1980-talet fick husen "
       "åter dekorativa snickerier. Råden är att behålla trädgårdskaraktären, skärma av mot gatan med låg häck "
       "eller staket och undvika stora markuppfyllnader och stora altandäck.",
       "Kommunens sida om " + ext(H_ALT, "altan och trädäck") + " anger att ett trädäck i marknivå oftast inte "
       "kräver bygglov, och att en altan är lovfri om den är högst 1,8 meter och ligger inom 3,6 meter från "
       "byggnaden. Täcker altanerna på tomten tillsammans mer än 50 kvadratmeter ska de följa detaljplanen."],
     "aside": {"title": "Kommunens gränser för altan",
               "items": ["Trädäck i marknivå: oftast lovfritt",
                         "Högst 1,8 m inom 3,6 m från huset",
                         "Mer än 50 m² altan: följ detaljplanen",
                         "Närmare gräns än 4,5 m: grannens ja"]}},
    {"id": "skarmtak",
     "h2": "Skärmtak och staket",
     "paras": [
       "Ett skärmtak kräver bygglov i Haninge om det är fristående, sticker ut mer än 50 centimeter från "
       "väggen eller sitter i ett särskilt värdefullt område, enligt " + ext(H_SKARM, "kommunens sida om "
       "skärmtak") + ". Har du inte använt de 30 kvadratmeter som får byggas till ett en- eller tvåbostadshus "
       "utan lov kan skärmtaket rymmas där.",
       "Ett staket med enkel och luftig konstruktion kräver oftast inget lov, men ett tätt staket över 1,2 "
       "meter kan göra det. Vid utfart eller korsning får staket och häck inte vara högre än 80 centimeter. "
       "Kommunen skriver att den uppdaterar kartan över särskilt värdefulla kulturmiljöer, så tills den är "
       "klar ringer vi bygglovsenheten när en fastighet kan vara berörd.",
       "Både altan, skärmtak och staket kan dessutom kräva strandskyddsdispens. Kommunen anger att "
       "strandskyddet vanligtvis gäller 100 till 300 meter från kustlinjen, sjöar och större vattendrag, "
       "och att dispens kan behövas även när bygget inte kräver lov. Varsamhetskravet gäller också: ändringar "
       "och tillägg ska anpassas till byggnaden och miljön runt den, oavsett om de kräver lov eller inte."],
     "aside": None}],
  "steps_h2": "Så går snickeriet i Haninge till",
  "steps": [
    ("Platsbesök", "Vi tittar på huset, tomten och vilken karaktärsmiljö det hör till."),
    ("Laga eller bygga nytt", "Vi föreslår vad som kan lagas i befintlig form och vad som behöver bytas."),
    ("Lov och mått", "Vi kontrollerar höjder, utsprång och avstånd mot kommunens gränser."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med arbete och material på separata rader."),
    ("Utförande", "Stolpar, bågar, krön eller trall tillverkas och monteras efter förlagan."),
    ("Genomgång", "Vi går igenom resultatet med dig och visar vad som behöver underhållas framöver.")],
  "rot_h2": "ROT för veranda, altan och dörrar",
  "rot": [
    "Hos " + ext(SKV_ARB, "Skatteverket") + " ger en altan rotavdrag när den byggs ihop med huset, och att glasa "
    "in balkonger och altaner i ett småhus räknas också. Byte och reparation av dörrar och fönster ger avdrag, "
    "liksom reparation av entrétrappor. Att bygga eller laga staket ger inget avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag. Material och resor ingår inte. Vi drar avdraget direkt på fakturan."],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "Hur mycket av en veranda eller ett snickeri som går att spara, om detaljer måste tillverkas efter förlaga "
    "och hur stor och hög en altan blir påverkar mest. Platsbesöket är gratis och du får ett skriftligt "
    "kostnadsförslag."],
  "faq": [
    ("Får vi byta glasverandans spröjsade fönster mot helglas i Dalarö?",
     "Karaktärsmiljöerna säger att sommarnöjenas ursprungliga fönstersättning ska vara vägledande. Ett byte "
     "bör därför göras med spröjs i samma indelning."),
    ("Hur långt får ett skärmtak sticka ut från väggen i Haninge utan bygglov?",
     "Högst 50 centimeter enligt kommunen, om det inte ryms i de 30 kvadratmeter du får bygga till huset "
     "utan lov. Ett fristående skärmtak kräver bygglov."),
    ("Hur högt får staketet vid utfarten vara i Haninge?",
     "Vid utfart eller korsning högst 80 centimeter för god sikt. Längre in på tomten kräver ett luftigt "
     "staket oftast inget lov."),
    ("Ska vi klä in undersidan på altanen vid vår gård i Haninge?",
     "Karaktärsmiljöerna avråder från det i den agrara miljön, eftersom altanens volym då upplevs större. "
     "Vi bygger hellre en lägre altan som följer marken."),
    ("Kan en rötskadad verandastolpe på ett sommarnöje lagas i stället för att bytas?",
     "Oftast ja. Vi skarvar in nytt virke i den skadade nedre delen och behåller resten av stolpen och "
     "dess profiler.")],
  "sources": [
    ("Haninge kommun – Haninges karaktärsmiljöer (pdf)", H_KAR),
    ("Haninge kommun – Altan och trädäck", H_ALT),
    ("Haninge kommun – Skärmtak", H_SKARM),
    ("Haninge kommun – Staket och spaljéer", H_STAKET),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska verandan, altanen eller skärmtaket göras i Haninge?",
          "Boka ett gratis platsbesök så tittar vi på huset och lämnar ett skriftligt kostnadsförslag."),
  "img": [("Sekelskiftesvilla i trä med glasveranda och snickarglädje i Dalarö",
           "modest two-storey 1890s Swedish wooden summer house with pale yellow horizontal wooden panel, white "
           "corner boards and simple fretwork under the eaves, red metal roof, a glazed veranda on the gable side "
           "with small mullioned window panes, overgrown garden with lilac and old birches, glimpse of a calm "
           "archipelago bay, Dalarö Haninge, summer, empty scene, no people, no text"),
          ("Ny farstukvist med snickarglädje framför en rödmålad gård",
           "close-up of a newly built small wooden entrance porch on a falu red Swedish farmhouse, white painted "
           "posts with simple carved brackets, small gable roof, a few wooden steps and a traditional panelled "
           "front door painted green, gravel yard, daylight, no people, no hands, no text")],
  "related": [],
},

# ---------------------------------------------------------------- VALLENTUNA
"snickare-vallentuna.html": {
  "kind": "district", "service": "snickare", "ort": "Vallentuna", "svc_label": "Snickare",
  "title": "Snickare i Vallentuna – uthus, uterum och fritidshus",
  "description": "Snickare i Vallentuna: vedbod, bastu och förråd enligt PBL 2025, altan, inglasat uterum "
                 "och fritidshus i Garns-Ekskogen. Gratis platsbesök.",
  "h1": "Snickare i Vallentuna",
  "lead": "Vallentuna är både tätort och landsbygd. Enligt översiktsplanen bor ungefär 5 500 personer utanför "
          "tätorterna, i klungor av hus och på enstaka gårdar, och i Garns-Ekskogen finns ett stort område med "
          "fritidshus. Det påverkar vad du får bygga utan lov. Geal Entreprenad AB bygger uthus, altaner och "
          "uterum och gör snickeri inomhus i hela Vallentuna kommun.",
  "card": "Uthus, uterum och fritidshus.",
  "sections": [
    {"id": "uthus", "anchor": "Uthusen",
     "h2": "Vedbod, bastu eller förråd – komplementbyggnader",
     "paras": [
       "Kommunens sida om " + ext(VA_KOMP, "nybyggnad av komplementbyggnad") + " räknar upp garage, carport, "
       "förråd, gäststuga, vedbod, växthus, bastu och båthus. Byggnaden ska vara ett komplement till "
       "bostadshuset och kan inte användas för verksamhet eller som självständig bostad.",
       "Inom detaljplan krävs bygglov om den sammanlagda ytan överstiger 45 kvadratmeter eller en enskild "
       "byggnad 30. Utanför detaljplan går gränsen vid 65 respektive 50 kvadratmeter. I ett kulturhistoriskt "
       "särskilt värdefullt område krävs bygglov. Installeras vatten, avlopp eller ventilation behövs dessutom "
       "anmälan och startbesked, även om byggnaden i sig är lovfri.",
       "En bastu med dusch eller en gäststuga med pentry blir därför oftast ett anmälningsärende, medan en "
       "enkel vedbod inte är det. Tidigare friggebodar och attefallshus räknas in i ytan, enligt " +
       ext(BV_NY, "Boverket") + "."],
     "aside": {"title": "Kommunens exempel på komplementbyggnader",
               "items": ["Vedbod och förråd", "Bastu och gäststuga",
                         "Garage och carport", "Växthus och båthus"]}},
    {"id": "altan-vallentuna",
     "h2": "Altan i tätort och på landet",
     "paras": [
       "Enligt " + ext(VA_ALT, "kommunens altansida") + " behövs varken lov eller anmälan för ett vanligt "
       "trädäck i marknivå. En högre altan till bostadshuset är lovfri om den byggs inom 3,6 meter från huset, "
       "är högst 1,8 meter, ligger minst 4,5 meter från gränsen eller har grannarnas skriftliga medgivande och "
       "inte ligger i ett särskilt värdefullt område.",
       "En altan som ökar byggnadens volym, eller där utrymmet under kan användas som förråd, räknas som "
       "tillbyggnad och kräver bygglov. Är du osäker kan du mejla en måttsatt skiss till kommunen för "
       "bedömning. En sådan skiss ritar vi gärna i samband med platsbesöket."],
     "aside": None},
    {"id": "uterum",
     "h2": "Inglasat uterum med plant golv",
     "paras": [
       "Ett inglasat uterum är enligt kommunen förbundet med ett bostadshus. Det kräver bygglov, men "
       "ett uterum på högst 30 kvadratmeter kan vara bygglovsbefriat. Bland de handlingar kommunen begär för "
       "ett uterum finns sektionsritning genom huset och uterummet, och om det finns höjdskillnad mellan "
       "innergolvet och uterummets golv ska det finnas ramp eller hiss.",
       "Därför lägger vi uterummets golv i samma nivå som rummet innanför när det går, och det styr i sin tur "
       "hur bjälklaget och grunden byggs. Enligt " + ext(BV_TILL, "Boverket") + " räknas tidigare altaner, "
       "skärmtak och attefallstillbyggnader in i de 30 kvadratmetrarna."],
     "aside": {"title": "Underlag till kommunen för uterum",
               "items": ["Situationsplan 1:500", "Plan och fasader 1:100",
                         "Sektion genom hus och uterum", "Material och kulörer (NCS)"]}},
    {"id": "garn",
     "h2": "Fritidshusen i Garns-Ekskogen och Lövsättra",
     "paras": [
       "Översiktsplanen beskriver att gränsen mellan att bo permanent och att bo i fritidshuset blir allt mer "
       "flytande, och att flertalet fritidshusområden har omvandlats sedan 1990-talet. Det största kvarvarande "
       "är Garns-Ekskogen i östra delen av kommunen, med cirka 500 bebyggda fastigheter och detaljplaner med "
       "byggrätt om 50 kvadratmeter för huvudbyggnad och 20 för komplementbyggnad. I Lövsättra stugby är "
       "byggrätten 32 respektive 10 kvadratmeter.",
       "Planen anger att båda områdena ska behålla sin fritidsboendeprägel. Med små byggrätter blir snickeriet "
       "inne i huset viktigare: en bättre trappa till loftet, en vägg som flyttas eller en ny ytterdörr kan göra "
       "mer nytta än en tillbyggnad."],
     "aside": None},
    {"id": "landsbygd-vallentuna",
     "h2": "Bygga på landet – byar, gårdar och kraftledningar",
     "paras": [
       "Landsbygden i Vallentuna kännetecknas enligt översiktsplanen av klungor av bebyggelse och enstaka "
       "gårdar intill skogspartier och träddungar, med åker runt byarna. Riktlinjerna säger att ny bebyggelse i "
       "första hand ska placeras i anslutning till befintlig bebyggelse och att anslutning till lokal "
       "byggnadstradition kan ske med både traditionellt och modernt formspråk. Ett nytt uthus brukar därför "
       "smälta in bäst när det står i gårdens grupp av byggnader och inte ute på åkern.",
       "Planen tar också upp en sak som är lätt att missa: inom 250 meter från stamnätsledningar och stationer "
       "ska samråd hållas med Svenska kraftnät, även för åtgärder som inte kräver bygglov, som friggebodar, "
       "attefallshus och ladugårdar. Ligger tomten nära en stor kraftledning tar vi upp det innan något "
       "beställs."],
     "aside": None}],
  "steps_h2": "Så går ett snickeriuppdrag i Vallentuna till",
  "steps": [
    ("Detaljplan eller inte", "Vi ser om tomten ligger inom detaljplan och vad som redan är byggt lovfritt."),
    ("Platsbesök", "Vi mäter mark, nivåer och avstånd till gräns och går igenom vad du vill bygga."),
    ("Skiss", "Du får en måttsatt skiss som kan skickas till kommunen om bedömning behövs."),
    ("Kostnadsförslag", "Arbete och material redovisas på separata rader i ett skriftligt förslag."),
    ("Bygge", "Grund, stomme, panel och tak eller trall byggs i den ordning ritningen anger."),
    ("Genomgång", "Vi går igenom resultatet med dig och lämnar ritningar och underlag att spara.")],
  "rot_h2": "ROT för uthus, uterum och snickeri",
  "rot": [
    "Hos " + ext(SKV_ARB, "Skatteverket") + " räknas garage, förråd och andra mindre byggnader till småhuset, "
    "men att bygga en ny fristående friggebod, ett garage eller ett växthus ger inget avdrag. En tillbyggnad "
    "som ett uterum kan ge avdrag om minst 75 procent av en sida sitter ihop med husets yttervägg och huset "
    "är äldre än fem år.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag. Material och resor ingår inte. Vi drar avdraget direkt på fakturan."],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "Byggnadens storlek och grund, om den ska ha vatten eller ventilation och hur mycket glas ett uterum får "
    "påverkar mest. På landet spelar också åtkomsten till tomten in. Platsbesöket är gratis och du får ett "
    "skriftligt kostnadsförslag."],
  "faq": [
    ("Behöver vi anmäla en bastu med dusch på tomten i Vallentuna?",
     "Ja. Även om bastun är lovfri kräver kommunen anmälan och startbesked när vatten och avlopp eller "
     "ventilation installeras."),
    ("Hur stor får en vedbod på landet i Vallentuna vara utan bygglov?",
     "Utanför detaljplan högst 50 kvadratmeter för en enskild byggnad och 65 kvadratmeter sammanlagt, där "
     "tidigare lovfria byggnader räknas in."),
    ("Kan kommunen bedöma vår altan i Vallentuna innan vi bygger?",
     "Ja. Kommunen ber om en måttsatt skiss till kommun@vallentuna.se, gärna med placeringen inritad på en "
     "tomtkarta."),
    ("Varför vill Vallentuna kommun ha en ramp till uterummet?",
     "Kommunens krav är att det ska finnas ramp eller hiss om innergolvet och uterummets golv ligger i olika "
     "höjd. Med samma golvnivå behövs ingen."),
    ("Får vi bygga ut fritidshuset i Garns-Ekskogen?",
     "Detaljplanerna där ger byggrätt om 50 kvadratmeter för huvudbyggnad och 20 för komplementbyggnad. Vad "
     "som återstår på din tomt beror på vad som redan är byggt.")],
  "sources": [
    ("Vallentuna kommun – Nybyggnad av komplementbyggnad", VA_KOMP),
    ("Vallentuna kommun – Altan", VA_ALT),
    ("Vallentuna kommun – Inglasat uterum", VA_UTE),
    ("Vallentuna kommun – Översiktsplan 2040 (pdf)", VA_OP),
    ("Boverket – Göra en tillbyggnad", BV_TILL),
    ("Boverket – Bygga en ny byggnad", BV_NY),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska det byggas uthus, altan eller uterum i Vallentuna?",
          "Boka ett gratis platsbesök så mäter vi upp tomten och lämnar ett skriftligt kostnadsförslag."),
  "img": [("Ny vedbod i trä intill en rödmålad gård i det öppna landskapet i Vallentuna",
           "newly built small falu red wooden woodshed with open front and stacked firewood, black metal roof, next "
           "to a traditional red Swedish farmhouse with white corners, open fields and a line of trees, Roslagen "
           "countryside Vallentuna, late summer, no people, no text"),
          ("Uterum i trä med stora glaspartier och golv i samma nivå som huset",
           "exterior view of a small newly built glass sunroom extension with its own low sloping glass roof and "
           "white painted wooden posts and frames, attached to the gable of a falu red Swedish wooden house with "
           "white corners, standing on a low wooden deck at the same level as the house, lawn and apple tree, "
           "countryside, daylight, no people, no hands, no text")],
  "related": [],
},

# ---------------------------------------------------------------- ÖSTERÅKER
"snickare-osteraker.html": {
  "kind": "district", "service": "snickare", "ort": "Österåker", "svc_label": "Snickare",
  "title": "Snickare i Österåker – brygga, altan och äldre hus",
  "description": "Snickare i Österåker: renovera bryggan utan dispens, altan efter PBL 2025 och varsamt "
                 "snickeri i hus byggda före 1920. Gratis platsbesök.",
  "h1": "Snickare i Österåker",
  "lead": "Österåker har enligt kommunen en lång kuststräcka, hundratals öar och många sjöar. Mycket av det "
          "som ska byggas här ligger nära vatten, och mycket av det som ska lagas sitter i äldre hus. Geal "
          "Entreprenad AB gör snickeri i Åkersberga, på öarna och på landsbygden, från bryggor och altaner till "
          "lister, foder och innerdörrar.",
  "card": "Bryggor, altaner och äldre snickerier.",
  "sections": [
    {"id": "brygga-osteraker", "anchor": "Bryggan",
     "h2": "Renovera bryggan – utan att bygga en ny",
     "paras": [
       "Kommunens sida om " + ext(O_BRY, "bryggor och sjöbodar") + " skiljer tydligt på att renovera och att "
       "bygga nytt. Har du en lagligt tillkommen brygga får du renovera den utan strandskyddsdispens, så länge "
       "den inte ändrar utseende, form eller storlek. Att riva en brygga och bygga en ny kräver däremot dispens "
       "först. Arbete i vattnet kan kräva en anmälan om vattenverksamhet.",
       "För en ny, enkel brygga och för flytbryggor krävs strandskyddsdispens. En större brygga med omkring "
       "tio båtplatser räknas som småbåtshamn och kräver både bygglov och dispens. En sjöbod är en "
       "komplementbyggnad som kräver dispens och ofta bygglov.",
       "I praktiken byter vi därför ofta trall, reglar och beslag på en befintlig brygga i samma mått, i stället "
       "för att göra den större. Strandskyddet gäller vanligtvis 100 meter från strandlinjen och på vissa platser "
       "i kommunen 300 meter."],
     "aside": {"title": "Brygga i Österåker",
               "items": ["Renovera i samma form: ingen dispens",
                         "Riva och bygga nytt: dispens först",
                         "Arbete i vattnet: ofta anmälan",
                         "Cirka 10 båtplatser: bygglov och dispens"]}},
    {"id": "fore-1920",
     "h2": "Är ditt hus byggt före 1920?",
     "paras": [
       "I " + ext(O_GUIDE, "kommunens bygglovsguide") + " finns frågor som visar om ett hus kan vara "
       "kulturhistoriskt värdefullt även om det inte är utpekat i kulturmiljökartan. Är huset byggt före 1920? "
       "Har det bevarad planlösning, kakelugnar, lister och foder, innerdörrar och takmålningar? Har det kvar "
       "ursprungliga fönster, dörrar och fasadmaterial? Svarar du ja kan huset vara värdefullt.",
       "Flera av frågorna gäller snickerier. Gamla dörrfoder, golvlister och fyllningsdörrar är just det som "
       "lätt försvinner vid en renovering. Vi tar ner, märker och sätter tillbaka det som går att spara, och "
       "tillverkar nya delar efter de gamla profilerna där något saknas.",
       "Kommunen skriver att alla ändringar ska göras varsamt, oavsett husets ålder och oavsett om åtgärden "
       "kräver lov. Lovfria åtgärder får inte heller utföras på byggnader som har skyddsbestämmelser i "
       "detaljplanen."],
     "aside": None},
    {"id": "altan-osteraker",
     "h2": "Altan efter de nya reglerna",
     "paras": [
       "Kommunens " + ext(O_ALT, "altansida") + " är uppdaterad efter lagändringen den 1 december 2025. Inom "
       "detaljplan krävs inget bygglov för en altan som är högst 1,8 meter och ligger inom 3,6 meter från en "
       "byggnad, eller högst 1,2 meter längre bort. Är altanerna på tomten tillsammans större än 50 "
       "kvadratmeter ska de följa detaljplanens bestämmelser. Utanför detaljplan finns inga mått att följa.",
       "I kulturhistoriskt värdefulla områden och för byggnader som är skyddade i detaljplan kan en altan ändå "
       "kräva bygglov. Då ber kommunen om en beskrivning och ritning till bygglov@osteraker.se för bedömning.",
       "Även en lovfri altan ska enligt kommunen anpassas till omgivningen och vara varsam mot byggnaden, och "
       "dess storlek och placering får inte bli en betydande olägenhet för grannarna. Ska altanen sedan glasas "
       "in blir den ett uterum. Kommunens " + ext(O_UTE, "sida om uterum") + " förklarar att ett uterum som "
       "sitter ihop med bostadshuset räknas som en tillbyggnad, medan ett fristående uterum eller växthus "
       "räknas som en komplementbyggnad. Båda kan byggas utan lov om vissa krav är uppfyllda, och nära vatten "
       "kan strandskyddsdispens behövas."],
     "aside": {"title": "Altan inom detaljplan",
               "items": ["Högst 1,8 m inom 3,6 m från byggnad",
                         "Högst 1,2 m längre bort",
                         "Över 50 m² sammanlagt: följ detaljplanen",
                         "Skyddad byggnad: fråga kommunen"]}},
    {"id": "roslagsbanan",
     "h2": "Roslagsbanan, tomtgränsen och tidigare bygglovfritt",
     "paras": [
       "Bygglovsguiden påminner om att bygglovfria åtgärder ska placeras mer än 30 meter från Roslagsbanans "
       "spårmitt om Trafikförvaltningen inte har godkänt något annat. Den ber dig också räkna med tidigare "
       "friggebodar, attefallsåtgärder, skärmtak och byggnader som saknar bygglov eller startbesked, även äldre "
       "svartbyggen. Allt det påverkar hur mycket du får bygga enligt de nya reglerna.",
       "Är du osäker på tomtgränsen kan kommunens geodataenhet fastställa den och staka ut byggnaden innan du "
       "bygger. För en gäststuga eller ett förråd nära gränsen slipper du då risken att behöva flytta det "
       "efteråt."],
     "aside": None}],
  "steps_h2": "Så går ett snickeriuppdrag i Österåker till",
  "steps": [
    ("Kartor och frågor", "Vi går igenom detaljplan, kulturmiljökarta, strandskydd och avståndet till Roslagsbanan."),
    ("Platsbesök", "Vi tittar på bryggan, altanen eller huset och vad som kan sparas."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med arbete och material på separata rader."),
    ("Ritning vid behov", "Krävs kommunens bedömning tar vi fram beskrivning och ritning."),
    ("Snickeriet", "Trall, stomme, lister, foder eller dörrar byggs och lagas i befintlig form."),
    ("Genomgång", "Vi går igenom arbetet med dig och lämnar en sammanställning.")],
  "rot_h2": "ROT – vad som räknas i Österåker",
  "rot": [
    "Enligt " + ext(SKV_ARB, "Skatteverket") + " ger det inget rotavdrag att reparera och underhålla båtbryggor, "
    "staket eller murar. En altan som byggs ihop med huset ger avdrag, och det gör även byte och reparation av "
    "dörrar, dörrlås och handtag och att reparera eller byta fönster.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag. Material och resor ingår inte. Vi drar avdraget direkt på fakturan."],
  "price_h2": "Vad påverkar kostnaden?",
  "price": [
    "För en brygga styr skicket under trallen och hur svårt det är att arbeta från vattnet. I ett äldre hus "
    "påverkar det hur mycket av listverk och dörrar som går att spara och hur många profiler som måste "
    "tillverkas. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag."],
  "faq": [
    ("Får vi byta trallen på vår brygga i Österåker utan strandskyddsdispens?",
     "Ja, om bryggan är lagligt tillkommen och inte ändrar utseende, form eller storlek. Arbete i vattnet kan "
     "kräva en anmälan om vattenverksamhet."),
    ("Kan vårt hus i Österåker vara kulturhistoriskt värdefullt fast det inte finns i kartan?",
     "Ja. Kommunen skriver att även hus som inte är utpekade kan ha sådana värden, och att hus byggda före "
     "1920 ofta är särskilt värdefulla."),
    ("Hur nära Roslagsbanan får vi bygga ett lovfritt förråd?",
     "Mer än 30 meter från spårmitt, om du inte har Trafikförvaltningens godkännande. Kommunens karta visar "
     "zonen."),
    ("Räknas ett gammalt svartbygge in i det vi får bygga i Österåker?",
     "Ja. Kommunen räknar med byggnader utan bygglov eller startbesked, även äldre preskriberade, när den "
     "bedömer hur mycket som återstår."),
    ("Kan ni tillverka nya dörrfoder efter de gamla i ett hus från 1910-talet?",
     "Ja. Vi tar mått och profil från ett befintligt foder och tillverkar de delar som saknas så att de "
     "matchar.")],
  "sources": [
    ("Österåkers kommun – Bygglovsguiden", O_GUIDE),
    ("Österåkers kommun – Bryggor och sjöbodar", O_BRY),
    ("Österåkers kommun – Altan", O_ALT),
    ("Österåkers kommun – Uterum", O_UTE),
    ("Boverket – Bygga en ny byggnad", BV_NY),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska bryggan, altanen eller snickerierna ses över i Österåker?",
          "Boka ett gratis platsbesök så tittar vi på vad som kan sparas och lämnar ett skriftligt förslag."),
  "img": [("Träbrygga med nylagd trall vid en klippig strand i Österåkers skärgård",
           "wooden jetty with freshly replaced light wooden decking boards on old dark posts, along a granite "
           "shoreline with pine trees, calm Baltic archipelago water, small red boathouse in the background, "
           "Österåker Roslagen, early summer morning, empty scene, no boats with people, no people, no text"),
          ("Gammal fyllningsdörr med profilerade foder i ett hus från tidigt 1900-tal",
           "interior of an early 1900s Swedish wooden house, old white painted four-panel interior door with "
           "profiled wooden architraves and tall skirting boards, one section of architrave newly made in the same "
           "profile with fresh primer, wide pine floorboards, soft daylight, no people, no hands, no text")],
  "related": [],
},

# ---------------------------------------------------------------- JÄRFÄLLA
"snickare-jarfalla.html": {
  "kind": "district", "service": "snickare", "ort": "Järfälla", "svc_label": "Snickare",
  "title": "Snickare i Järfälla – förgård, förråd och ytterdörr",
  "description": "Snickare i Järfälla: förråd och grindar på radhusens förgårdar, ytterdörrar i "
                 "grändvillor och ROT i bostadsrätt. Gratis platsbesök.",
  "h1": "Snickare i Järfälla",
  "lead": "Mycket av Järfällas småhusbebyggelse uppfördes i grupper, där husen gjordes lika för att bilda en "
          "helhet. Kommunens kulturmiljöplan visar hur förgårdar, carportar och förråd ingår i den helheten. "
          "Geal Entreprenad AB bygger och byter förråd, grindar, ytterdörrar och snickerier i hela Järfälla, med "
          "gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Förgårdar, förråd och ytterdörrar.",
  "sections": [
    {"id": "ekedal", "anchor": "Förgårdarna",
     "h2": "Ekedalsvägen – carport, grind och förråd mot gatan",
     "paras": [
       "I " + ext(J_JAK, "kulturmiljöplanen för Jakobsberg") + " beskrivs radhusen vid Ekedalsvägen, uppförda av "
       "Widmark & Platzer. Radhusen är indragna från gatan och förgårdarna är inbyggda genom att varje hus har "
       "carport med grindar och förråd mot gatan. Planen kallar de kringbyggda förgårdarna en alldeles speciell "
       "och värdefull karaktär.",
       "För radhusen säger planen att det är viktigt att värna karaktären mot gatan. Byts ett förråd eller en "
       "carportgrind i en sådan länga är det därför klokt att göra den nya delen lik grannarnas, i samma mått, "
       "samma panel och samma indelning, även om ett lovfritt bygge i sig inte prövas av kommunen.",
       "För villorna längs Fölvägen gäller enligt planen en byggrätt på högst 180 kvadratmeter inklusive uthus, "
       "på tomter om minst 600 kvadratmeter, och eventuella tillbyggnader bör läggas åt baksidan."],
     "aside": {"title": "Detaljer som håller ihop en radhuslänga",
               "items": ["Förrådens mått och placering",
                         "Grindarnas indelning",
                         "Panelens riktning och bredd",
                         "Ytterdörrarnas utformning"]}},
    {"id": "grandvillor",
     "h2": "Grändvillorna vid Hovvägen",
     "paras": [
       "Villorna vid Hovvägens norra del uppfördes kring 1960 av Svenska Industribyggen AB. De är "
       "souterränghus åtskilda av en smal gränd, och därför kallas de grändvillor. Enligt kulturmiljöplanen är "
       "området i stort sett oförändrat sedan byggnadstiden, och bland de mindre förändringar som har skett "
       "nämns byte av garageportar och ytterdörrar.",
       "Planen noterar också att byggnadsplanen tillåter mindre förråd på förgårdsmarken, men att förgårdarna "
       "är så små att ett förråd i praktiken skulle bygga för entréer eller fönster. Ska en ytterdörr eller "
       "garageport bytas i en sådan miljö väljer vi en modell som liknar den ursprungliga, och tittar först på "
       "grannarnas dörrar.",
       "Kring Betselvägen beskriver planen ett mindre område med villor från 1950-talet som inte är "
       "gruppbyggda utan uppförda för varje byggherre. Husen har två plan och hade ursprungligen garage i "
       "bottenvåningen, och låga garagebyggnader har ofta byggts till senare. Där är förutsättningarna för "
       "en ny port, ett förråd eller ett skärmtak andra än i radhuslängorna, eftersom husen redan skiljer sig "
       "åt."],
     "aside": {"title": "Tre miljöer i kulturmiljöplanen",
               "items": ["Ekedalsvägen: radhus med kringbyggda förgårdar",
                         "Hovvägen: grändvillor från omkring 1960",
                         "Betselvägen: 1950-talsvillor för egna byggherrar",
                         "Fölvägen: villor i sluttning"]}},
    {"id": "lovfritt-jarfalla",
     "h2": "Lovfritt med liten avvikelse – och frivilligt lov",
     "paras": [
       "Kommunens sida om " + ext(J_BEFR, "bygglovsbefriade åtgärder") + " räknar upp bland annat "
       "komplementbyggnad, tillbyggnad samt mur, plank och altan. Lovbefriade åtgärder som inte är undantagna "
       "från detaljplanen får göras med en avvikelse om avvikelsen är liten och inte motverkar planens syfte. "
       "Närhet till gräns, järnväg eller kulturmiljö kan ändå kräva bygglov.",
       "Kommunen påminner om att du måste hålla dig inom den totalt tillåtna ytan för komplementbyggnader och "
       "tillbyggnader. Påverkas bärande konstruktion, brandskydd, vatten, avlopp eller ventilation väsentligt "
       "kan anmälan och startbesked krävas, även när bygget är lovfritt.",
       "För alla lovfria åtgärder går det att söka frivilligt lov. Kommunen beskriver det som en trygghet inför "
       "en större investering, till exempel en tillbyggnad på radhusets baksida.",
       "Måtten kommer från " + ext(BV_TILL, "Boverket") + ": en lovfri tillbyggnad av ett småhus får vara högst "
       "30 kvadratmeter sammanlagt och inte högre än husets taknock, och tidigare skärmtak, altaner och "
       "attefallstillbyggnader räknas in. Inom detaljplan får en komplementbyggnad som ett förråd vara högst 30 "
       "kvadratmeter, och alla tillsammans högst 45, med en nockhöjd på högst 4 meter."],
     "aside": None},
    {"id": "brf-jarfalla",
     "h2": "Radhus i bostadsrätt eller äganderätt",
     "paras": [
       "Många radhus i Järfälla ägs som bostadsrätt, och då ser rotavdraget annorlunda ut. Enligt " +
       ext(SKV_ARB, "Skatteverket") + " ger det inget avdrag att bygga eller bygga om en altan eller balkong i en "
       "bostadsrätt, inte heller att glasa in den eller att byta ytterdörr. Att byta och reparera innerdörrar och "
       "deras lås och handtag ger däremot avdrag, liksom arbete på insidan av ytterdörren.",
       "I ett radhus med äganderätt gäller småhusreglerna: dörrar, dörrlås och handtag ger avdrag, och en altan "
       "ger avdrag om den byggs ihop med huset. Fråga också föreningen innan du ändrar något utvändigt."],
     "aside": {"title": "Bostadsrätt – rot eller inte",
               "items": ["Innerdörrar, lås och handtag: ja",
                         "Insidan av ytterdörren: ja",
                         "Byta ytterdörr: nej",
                         "Bygga eller glasa in altan: nej"]}}],
  "steps_h2": "Så går ett snickeriuppdrag i Järfälla till",
  "steps": [
    ("Platsbesök", "Vi tittar på huset, längan och grannarnas förråd, grindar och dörrar."),
    ("Ägandeform", "Vi stämmer av om huset är bostadsrätt eller äganderätt, eftersom det styr rotavdraget."),
    ("Regler och yta", "Vi går igenom detaljplan, tidigare lovfria byggen och om anmälan behövs."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med arbete och material på separata rader."),
    ("Snickeriet", "Förråd, grind, dörr eller altan byggs i mått och utförande som passar längan."),
    ("Genomgång", "Vi går igenom resultatet med dig och lämnar underlag att spara.")],
  "rot_h2": "Så räknas rotavdraget",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag, enligt " + ext(SKV_ROT, "Skatteverket") + ". Material och resor ingår inte.",
    "Att bygga ett nytt fristående förråd eller garage ger inget avdrag, men en tillbyggnad där minst 75 procent "
    "av en sida sitter ihop med husets yttervägg kan göra det. Vi drar avdraget direkt på fakturan."],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "Om förrådet, grinden eller dörren ska matcha resten av längan, hur mycket av det gamla som rivs och om "
    "underlaget håller påverkar mest. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag."],
  "faq": [
    ("Får vi bygga ett eget förråd på förgården vid Ekedalsvägen?",
     "Kulturmiljöplanen säger att karaktären mot gatan ska värnas och att planändringar kan behövas för att ta "
     "bort byggrätter på förgårdsmark. Stäm av med kommunen innan."),
    ("Ger en ny ytterdörr i vårt bostadsrättsradhus i Järfälla rotavdrag?",
     "Nej. Skatteverket undantar byte av ytterdörr i bostadsrätt. Arbete på dörrens insida och byte av "
     "innerdörrar ger däremot avdrag."),
    ("Vad är ett frivilligt lov i Järfälla?",
     "En bygglovsansökan för något som egentligen är lovfritt. Kommunen beskriver det som en trygghet inför "
     "en större investering."),
    ("Måste vi spara ritningar för ett lovfritt förråd i Järfälla?",
     "Kommunen uppmanar dig att spara ritningar och skriftliga grannemedgivanden själv, eftersom de inte "
     "arkiveras hos kommunen vid lovbefriade åtgärder."),
    ("Kan ni göra en carportgrind som matchar grannarnas i radhuslängan?",
     "Ja. Vi tar mått på en befintlig grind i längan och bygger den nya med samma indelning och bredd på "
     "virket.")],
  "sources": [
    ("Järfälla kommun – Kulturmiljöplan, Jakobsberg (pdf)", J_JAK),
    ("Järfälla kommun – Bygglovsbefriade åtgärder", J_BEFR),
    ("Boverket – Göra en tillbyggnad", BV_TILL),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska förrådet, grinden eller dörren bytas i Järfälla?",
          "Boka ett gratis platsbesök så tittar vi på huset och längan och lämnar ett skriftligt kostnadsförslag."),
  "img": [("Putsade radhus från 1960-talet med förråd och carport mot gatan i Jakobsberg",
           "1960s Swedish suburban single-storey terraced houses with flat low roofs and light grey rendered "
           "facades, in front of each house a small enclosed front yard formed by a low wooden storage shed and an "
           "open carport with a wooden gate, all in the same dark brown stained wood, quiet residential street with "
           "birch trees, the carports are empty with no vehicles parked, Stockholm suburb, overcast autumn daylight, no people, no cars, no text"),
          ("Ny carportgrind i trä bredvid ett förråd vid ett radhus",
           "close-up of a newly built low wooden garden gate with vertical boards stained dark brown, hung between "
           "two wooden posts at the opening of an open carport, next to a small wooden storage shed with matching "
           "vertical panel, concrete paving stones, Swedish 1960s terraced house area, daylight, no people, no "
           "hands, no text")],
  "related": [],
},
}
