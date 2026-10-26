# -*- coding: utf-8 -*-
"""Snickare – ortsidor v3: Bromma, Solna, Huddinge, Sollentuna, Lidingö, Danderyd (2026-10-25).
Schema: se tools/tj_check.py. Fakta endast från källorna i respektive sidas "sources"
(öppnade 2026-10-25): kommunernas bygglovssidor och kulturmiljöprogram/riktlinjer, Stockholms stad,
Stadsmuseet, Boverket, Skatteverket och riksdagen.se. Inga priser, case, cert eller garantier."""

L = 'class="text-link"'

# Gemensamma källor
BV_ALTAN = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/mur-plank-altan-och-annat/"
BV_TILLB = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/gora-en-tillbyggnad/"
BV_NY = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/bygga-en-ny-byggnad/"
SKV_ROT = "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html"
SKV_ARB = "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html"
BRL = "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/"

# Bromma / Stockholms stad
STH_VARSAM = "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf"
STH_ALT = "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/mur-plank-altan/"
STH_TILL = "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/tillbyggnad-bygglovsbefriad/"
STH_FD = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fonster-och-dorrar/"
SSM_KLASS = "https://stadsmuseet.stockholm/kunskap-och-samlingar/kulturmiljo/klassificering/"

# Solna
S_LAG = "https://www.solna.se/bygga-bo--miljo/bygga/guide-till-lov-och-anmalan/for-lagenhetsinnehavare"
S_VILLA = "https://www.solna.se/bygga-bo--miljo/bygga/guide/villaagare"
S_FRI = "https://www.solna.se/bygga-bo--miljo/bygga/bygglov/bygglovsfria-atgarder"
S_KM = "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna"

# Huddinge
H_PBL = "https://www.huddinge.se/bostad-och-miljo/bygglov/forandringar-i-pbl"
H_KM2 = ("https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/"
         "kulturmiljoprogram/kulturmiljoprogram--del-2.pdf")

# Sollentuna
SOL_ALT = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/altan/"
SOL_TILL = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/tillbyggnad-en--och-tvabostadshus/"
SOL_KM = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/kulturmiljoer/"
SOL_STR = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/strandskydd"
SOL_GR = ("https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/oversiktsplan/"
          "granskningsutlatande-till-oversiktsplan-sollentuna-2040.pdf")

# Lidingö
L_GRON = "https://share.mediaflow.com/sv/?WHCCZ16EAN"
L_NASET = "https://share.mediaflow.com/sv/?4OCCV1BE7N"
L_DEL1 = "https://share.mediaflow.com/sv/?7ZCCF1REBX"
L_NYA = "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/"
L_FAQ = "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/"

# Danderyd
D_RIKT = ("https://www.danderyd.se/globalassets/globala-filer/kommun-och-politik/ovriga-styrdokument-ny/"
          "styrande-dokument---samhallsbyggnad-miljo-och-exploatering/"
          "riktlinjer-for-kulturmiljohistoriska-byggnader-och-miljoer-i-danderyd-2024.pdf")
D_NYA = "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/"


def a(href, text):
    return f'<a {L} href="{href}">{text}</a>'


def ext(href, text):
    return f'<a {L} href="{href}" rel="noopener">{text}</a>'


PAGES_TJ = {

# ---------------------------------------------------------------- BROMMA
"snickare-bromma.html": {
  "kind": "district", "service": "snickare", "ort": "Bromma", "svc_label": "Snickare",
  "title": "Snickare i Bromma – glasverandor, entréer och altaner",
  "description": "Snickare i Bromma: glasverandor och entréer i villastaden, altaner och uterum mot "
                 "trädgården. Stockholms regler för altan och tillbyggnad samt ROT.",
  "h1": "Snickare i Bromma",
  "lead": "I Bromma är det mesta som ger villan dess karaktär gjort av trä: glasverandan, entrédörren, "
          "räckena och fönstrens bågar och spröjs. Vi lagar och bygger nytt – verandor, entréer, altaner "
          "och tillbyggnader mot trädgården – och tar först reda på vad Stadsmuseets klassificering och "
          "Stockholms stads lovregler säger om just din fastighet.",
  "card": "Verandor, entréer och altaner.",
  "sections": [
    {"id": "villastad", "anchor": "Husen i Bromma",
     "h2": "Villastad och trädgårdsstad – två sorters snickeri",
     "paras": [
       "Stadens strategi " + ext(STH_VARSAM, "Varsam utveckling av småhus- och villaområden") + " skiljer "
       "mellan villastäderna och trädgårdsstäderna. Villastäderna, som den kring Bromma kyrka, växte fram "
       "efter privata initiativ och fick en brokigare bebyggelse med individuellt utformade hus. Trä var "
       "det vanligaste fasadmaterialet, och det var glasverandor, takkupor och snickarglädje som gav "
       "stadsdelarna den variation som syns än i dag.",
       "Trädgårdsstäderna i Äppelviken, Ålsten och Smedslätten tillkom på 1920-talet, och många av "
       "husen där ritades av arkitekten Edvin Engström. I Äppelviken blev det "
       "nationalromantiska draget tydligt, med branta tak och småspröjsade fönster. I Smedslätten, "
       "Nockeby och Höglandet är husen enklare och symmetriska. I Smedslätten är det små detaljer som "
       "takkupor och hörnpilastrar som ger varje hus en egen identitet.",
       "Strategin räknar ursprungliga byggnadsdetaljer som fönster, entrédörrar och räcken till det som "
       "bär trädgårdsstadens värden. För oss betyder det att en entré eller ett räcke i första hand "
       "lagas eller kopieras, och att en ny del får samma profil som den gamla i stället för att bytas "
       "mot en standardvara."],
     "aside": {"title": "Vad husen brukar behöva",
               "items": ["Bromma kyrka, Mariehäll: glasverandor och räcken",
                         "Äppelviken: entréer och småspröjsade bågar",
                         "Smedslätten, Ålsten: kupor, foder och lister",
                         "Hela Bromma: altan och uterum mot trädgården"]}},
    {"id": "veranda",
     "h2": "Glasverandan och entrén – laga, kopiera, komplettera",
     "paras": [
       "En glasveranda från villastadens första årtionden har ofta byggts om flera gånger. Vi tar bort "
       "det som är ruttet, mäter upp bågar, spröjs, foder och räcken och tillverkar nya delar efter de "
       "bevarade.",
       "Stockholms stad räknar mycket som en ändring av " + ext(STH_FD, "fönster och dörrar") + ": att "
       "ändra dimensioner, proportioner eller profilering på karmar, bågar och spröjs, att byta "
       "upphängning och att ändra indelningen, till exempel lägga till spröjs eller ta bort en mittpost. "
       "Om det kräver bygglov beror på byggnaden och fasaden.",
       "Har en veranda eller entré försvunnit kan stadens äldre miljöprogram och typritningssamlingar "
       "visa hur husen såg ut. De har ingen juridisk status vid bygglov men ger kunskap om områdets "
       "karaktär. Ska verandan också målas om samordnar vi arbetet med " + a("malare-bromma.html",
       "målare i Bromma") + ", så att nytt trä grundas innan vintern."],
     "aside": None},
    {"id": "altan",
     "h2": "Altanen: höjden, planket och det som byggs in",
     "paras": [
       "Enligt stadens sida om " + ext(STH_ALT, "mur, plank och altan") + " krävs bygglov för en altan "
       "som blir högre än 1,8 meter över marken inom 3,6 meter från en byggnad, eller högre än 1,2 meter "
       "längre bort. Ett plank som byggs ovanpå altanen räknas in i höjden, liksom en mur under den. Ett "
       "lovbefriat staket eller räcke på altanen räknas däremot inte.",
       "Får altanen tak eller väggar kan den bli en tillbyggnad, och staden skriver att det kan gälla "
       "även om bara undersidan byggs in. Altaner som inte kräver bygglov får avvika från detaljplanen "
       "så länge den totala ytan inte överstiger 50 kvadratmeter. Ändras markens höjd mer än en halv "
       "meter inom detaljplan behövs marklov.",
       "Var altanen hamnar spelar också roll. Strategin för trädgårdsstäderna säger att tillbyggnader, "
       "takkupor och terrasser i första hand ska göras mot trädgårdssidan och att utblicken från gatan "
       "in i kvarteret ska hållas öppen."],
     "aside": {"title": "Räknas in i altanens höjd",
               "items": ["Plank ovanpå altanen: ja",
                         "Mur under altanen: ja",
                         "Lovfritt räcke eller staket: nej",
                         "Inbyggd undersida: kan bli tillbyggnad"]}},
    {"id": "uterum",
     "h2": "Uterum och tillbyggnad – 30 kvadratmeter sammanlagt",
     "paras": [
       "Staden ger uterum, skärmtak, större takkupor och lågt sittande balkonger som exempel på "
       + ext(STH_TILL, "tillbyggnader") + ". En sådan behöver inte bygglov om den inte är större än 30 "
       "kvadratmeter och inte högre än husets taknock, men i de 30 kvadratmetrarna ingår allt som redan "
       "byggts till lovfritt, till exempel skärmtak, attefallstillbyggnader och attefallskupor. Mer om "
       "planeringen finns på sidan om " + a("tillbyggnad.html", "tillbyggnad") + ".",
       "På ett en- eller tvåbostadshus får den lovfria tillbyggnaden strida mot detaljplanen och till "
       "exempel placeras på prickmark. Den ska ligga minst 4,5 meter från tomtgränsen om inte grannen "
       "skriftligen medger annat; mot gata eller park är det oftast staden som ska ge medgivandet. "
       "Påverkas bärande delar eller brandskydd krävs anmälan och startbesked.",
       "Ligger fastigheten i ett område eller är huset klassat som särskilt kulturhistoriskt värdefullt "
       "gäller utökad lovplikt. Stadsmuseet beskriver sin " + ext(SSM_KLASS, "klassificering") + " som "
       "ett kunskapsunderlag som används vid bygglovsprövning. Kartan ger en första indikation, men "
       "alla byggnader är ännu inte inventerade."],
     "aside": {"title": "Före beställning",
               "items": ["Slå upp huset i Stadsmuseets karta",
                         "Läs detaljplanen i Bygg- och plantjänsten",
                         "Räkna ihop tidigare lovfria tillbyggnader",
                         "Mät avståndet till tomtgränsen"]}}],
  "steps_h2": "Så går ett snickeriuppdrag i Bromma till",
  "steps": [
    ("Klassning och plan", "Vi slår upp Stadsmuseets karta och detaljplanen i stadens e-tjänst innan något "
     "ritas, så att du vet om arbetet kräver lov."),
    ("Besök vid huset", "Vi mäter upp verandan, entrén eller altanläget och noterar röta, sättningar och "
     "äldre lagningar."),
    ("Mallar och profiler", "Saknade detaljer ritas av från bevarade delar eller gamla foton och tas fram i "
     "samma profil."),
    ("Skriftligt förslag", "Du får en beskrivning av arbetet, i vilken ordning det görs och vad som "
     "eventuellt ska sökas eller anmälas."),
    ("Bygget", "Vi arbetar etappvis och samordnar med målare och plåtslagare så att nytt trä skyddas i tid."),
    ("Överlämning", "När allt är klart går vi igenom resultatet och lämnar en sammanställning av det som "
     "gjorts.")],
  "rot_h2": "ROT-avdrag för veranda, altan och entré",
  "rot": [
    "Enligt " + ext(SKV_ARB, "Skatteverket") + " ger det rotavdrag att bygga eller reparera en altan eller "
    "balkong som sitter ihop med huset, att glasa in en altan och att reparera eller byta dörrar och "
    "fönster. En ny fristående byggnad eller en ny friggebod ger inget avdrag, och inte heller ett staket.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och rot och rut får "
    "tillsammans uppgå till högst 75 000 kr. Material, resor och maskiner betalar du fullt ut. För om- och "
    "tillbyggnad ska huset vara äldre än fem år räknat från värdeåret, medan reparation och underhåll ger "
    "avdrag oavsett ålder. Vi drar av beloppet direkt på fakturan."],
  "price_h2": "Vad avgör kostnaden i Bromma?",
  "price": [
    "Mest väger hur mycket av verandan eller entrén som går att spara, om bågar och profiler måste "
    "specialtillverkas och om arbetet kräver lov eller anmälan. En altan på en plan gräsmatta är ett annat "
    "jobb än en veranda på en villa där grunden har satt sig. Vi kommer ut kostnadsfritt, tittar på huset "
    "och lämnar sedan ett skriftligt kostnadsförslag."],
  "faq": [
    ("Räknas planket på vår altan i Bromma in i höjden för bygglov?",
     "Ja. Stockholms stad räknar den sammanlagda höjden när ett plank byggs på en altan eller en altan på "
     "en mur. Ett lovbefriat staket eller räcke på altanen räknas däremot inte in."),
    ("Kan vi bygga in undersidan av altanen till ett förråd?",
     "Det går, men staden skriver att även en altan där bara undersidan byggs in med väggar kan bedömas "
     "som en tillbyggnad. Då gäller reglerna för tillbyggnad, och ytan räknas in i de 30 kvadratmeter som "
     "får byggas till lovfritt."),
    ("Var hittar vi hur glasverandan på vår Brommavilla såg ut från början?",
     "Äldre handlingar för fastigheten går att söka fram i stadens e-tjänst Bygg- och plantjänsten. Staden "
     "har också äldre miljöprogram och typritningssamlingar som går att beställa."),
    ("Behöver vi lov för att ta bort spröjsen i glasverandan?",
     "Det kan krävas. Staden räknar ändrad indelning av fönster, som att ta bort spröjs eller en mittpost, "
     "som en ändring av fönster, och om lov krävs beror på byggnaden. Är huset klassat som särskilt "
     "värdefullt gäller utökad lovplikt."),
    ("Får en tillbyggnad på vår villa i Äppelviken placeras på prickmark?",
     "Ja, en lovfri tillbyggnad på ett en- eller tvåbostadshus får strida mot detaljplanen. Är huset eller "
     "området särskilt kulturhistoriskt värdefullt krävs däremot bygglov.")],
  "sources": [
    ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)", STH_VARSAM),
    ("Stockholms stad – Fönster och dörrar", STH_FD),
    ("Stockholms stad – Mur, plank, altan", STH_ALT),
    ("Stockholms stad – Tillbyggnad (bygglovsbefriad)", STH_TILL),
    ("Stadsmuseet – Kulturhistorisk klassificering", SSM_KLASS),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Har glasverandan sett bättre dagar?", "Berätta om huset så kommer vi ut till Bromma och tittar – "
          "platsbesöket är gratis."),
  "img": [("Trävilla med spröjsad glasveranda och äppelträd i Bromma",
           "1920s Swedish wooden villa with white small-paned glazed veranda and panelled entrance door, "
           "pale green vertical board facade, red tile roof, mature pine and apple trees, garden city suburb "
           "Bromma Stockholm, summer daylight, no people, no text"),
          ("Nya spröjsade bågar och foder på en äldre glasveranda i trä",
           "close-up of newly made white painted wooden window sashes with small glazing bars and moulded "
           "casings on an old glazed wooden veranda, carpentry repair, soft daylight, no people, no hands, "
           "no text")],
  "related": [("malare-bromma.html", "Målare i Bromma", "Fasader i trädgårdsstäderna."),
              ("koksrenovering-bromma.html", "Köksrenovering i Bromma", "Kök i villa och bostadsrätt."),
              ("badrumsrenovering-bromma.html", "Badrumsrenovering i Bromma", "Badrum i trävillor och småstugor.")],
},

# ---------------------------------------------------------------- SOLNA
"snickare-solna.html": {
  "kind": "district", "service": "snickare", "ort": "Solna", "svc_label": "Snickare",
  "title": "Snickare i Solna – lägenhet, balkong och radhus",
  "description": "Snickare i Solna: innerväggar, lägenhetsdörrar och förvaring i bostadsrätt, inglasade "
                 "balkonger och radhus där lovfriheten sällan gäller. Regler och ROT.",
  "h1": "Snickare i Solna",
  "lead": "De flesta snickeriuppdrag i Solna görs i lägenheter: en ny innervägg, en lägenhetsdörr, "
          "platsbyggd förvaring eller en balkong som ska glasas in. Hos villa- och radhusägare gäller det "
          "oftare altan, förråd eller tillbyggnad, i en stad där stora delar räknas som kulturhistoriskt "
          "värdefulla. Vi reder ut vem som ska godkänna arbetet innan det planeras.",
  "card": "Väggar, dörrar, balkong och radhus.",
  "sections": [
    {"id": "miljoer", "anchor": "Husen i Solna",
     "h2": "35 utpekade miljöer – många av dem bostadsområden",
     "paras": [
       "Solna stad beskriver en kulturhistoria som präglas av mångfald och kontraster, och på stadens sida "
       "om " + ext(S_KM, "kulturmiljöer i Solna") + " räknas 35 sammanhängande kulturhistoriskt värdefulla "
       "miljöer upp. Bland bostadsområdena finns Vasalund, Gamla Hagalund, Brahelund, 1950-talshusen vid "
       "Förvaltarvägen och i kvarteren Fjorden och Nordan, och arbetarbostäderna vid Ulriksdals station, "
       "som kallas Rödingarna.",
       "Staden skriver att byggnader med jämna mellanrum behöver anpassas till nya behov och att det då är "
       "viktigt att ta hänsyn till husens ursprungliga karaktär, så att deras historiska värde inte går "
       "förlorat. Bland de enskilda byggnadsminnena finns radhus i kvarteret Fyrväpplingen.",
       "För en snickare innebär det att samma sorts uppdrag kan hanteras helt olika. En ny vägg i en "
       "50-talslägenhet i Huvudsta är i första hand en fråga för föreningen, medan ett förråd vid ett "
       "radhus i en utpekad miljö kan kräva bygglov."],
     "aside": {"title": "Bostadsmiljöer på stadens lista (urval)",
               "items": ["Vasalund",
                         "Gamla Hagalund och Brahelund",
                         "Rödingarna vid Ulriksdals station",
                         "Radhus i kv. Fyrväpplingen (byggnadsminne)"]}},
    {"id": "brf",
     "h2": "Lägenhetsdörren, väggen och styrelsens tillstånd",
     "paras": [
       "Solna stads sida " + ext(S_LAG, "för lägenhetsinnehavare") + " är kortfattad: som boende i "
       "bostadsrätt behöver du fastighetsägarens medgivande för byggåtgärder, alltså föreningens. Att riva "
       "en vägg kräver föreningens godkännande men inte bygglov. Är väggen bärande krävs dessutom en "
       "anmälan om ändring av bärande konstruktion, en process som staden beskriver som lik en "
       "bygglovsansökan.",
       "I 7 kap. 7 § " + ext(BRL, "bostadsrättslagen") + " räknas de åtgärder upp som kräver styrelsens "
       "tillstånd. En av dem är det som påverkar brandskyddet, och den som byter lägenhetsdörren mot "
       "trapphuset bör därför stämma av med styrelsen innan dörren beställs. Staden påpekar på sin "
       "villaägarsida att flera ändringar kan påverka brandskyddet och att en sakkunnig brandkonsult kan "
       "hjälpa till att bedöma dem.",
       "Har lägenheten särskilda kulturhistoriska värden krävs tillstånd för varje åtgärd som påverkar "
       "dem. Styrelsen får säga nej bara om åtgärden är till påtaglig skada eller olägenhet för "
       "föreningen, och ett tillstånd kan förenas med villkor."],
     "aside": {"title": "Underlag som styrelsen brukar vilja se",
               "items": ["Ritning med väggens placering",
                         "Uppgift om väggen är bärande",
                         "Dörrens utförande mot trapphuset",
                         "Arbetstider för bullrande moment"]}},
    {"id": "balkong",
     "h2": "Inglasad balkong kräver bygglov",
     "paras": [
       "Enligt Solna stad kräver inglasning av balkong bygglov för fasadändring. På vissa platser är det "
       "inte tillåtet alls, antingen på grund av byggnadens kulturvärden eller på grund av "
       "detaljplanen. Om man också vill bygga ett skärmtak över balkongen räknas det som en tillbyggnad, "
       "och det är enligt staden ofta inte tillåtet.",
       "Balkongen hör till huset, och därför är det föreningen som fastighetsägare som ska stå bakom "
       "ansökan. Staden råder den som beställer att ställa krav på att leverantören bygger enligt "
       "bygglovet, följer kontrollplanen och dokumenterar bygget, och att begära slutbesked när allt är "
       "klart.",
       "Ekonomiskt skiljer sig balkongen från resten av lägenheten. Skatteverket ger inget rotavdrag för "
       "att bygga, reparera eller glasa in en balkong i en bostadsrätt, medan arbete inne i lägenheten "
       "ger det."],
     "aside": None},
    {"id": "radhus",
     "h2": "Altan, förråd och tillbyggnad vid villor och radhus",
     "paras": [
       "På sidan om " + ext(S_FRI, "bygglovsfria åtgärder") + " skriver staden att undantagen från "
       "bygglov i många fall inte kan tillämpas i Solna, eftersom stora delar av staden är "
       "kulturhistoriskt värdefulla. På " + ext(S_VILLA, "villaägarsidan") + " står att friggebodar inte "
       "längre får byggas utan bygglov i stora delar av Solna, och att de vanligaste skälen är särskilt "
       "värdefulla kulturmiljöer och riksintressen. Områdena syns i Solnakartan.",
       "Där undantagen gäller, inom detaljplan, finns en gemensam pott på 45 kvadratmeter byggnadsarea "
       "för lovfria komplementbyggnader och komplementbostadshus. En enskild byggnad får vara högst 30 "
       "kvadratmeter, inte större än huset den kompletterar och högst 4 meter till nock. För "
       "tillbyggnader finns en egen pott på 30 kvadratmeter, och tidigare friggebodar, " +
       a("attefallshus.html", "attefallshus") + " och skärmtak räknas in.",
       "Staden räknar också upp lägen där lov krävs: närmare tomtgräns än 4,5 meter utan grannens "
       "skriftliga medgivande, närmare än 30 meter från ett järnvägsspårs mitt och vid riksintressen för "
       "totalförsvaret. Ligger tomten inom strandskydd kan även dispens behövas."],
     "aside": {"title": "Lov krävs i Solna om",
               "items": ["Fastigheten ligger i en utpekad kulturmiljö",
                         "Huset har k- eller q-bestämmelse i planen",
                         "Bygget hamnar inom 30 m från spårmitt",
                         "Det står närmare gräns än 4,5 m utan medgivande"]}},
    {"id": "inredning",
     "h2": "Förvaring och innerväggar som passar huset",
     "paras": [
       "Inne i lägenheten är platsbyggd förvaring det vanligaste önskemålet: garderober i en hall, "
       "bokhyllor runt en dörr eller skåp i en nisch. Vi anpassar luckor, lister och foder till lägenhetens "
       "ålder, så att det nya ser ut att höra till. En ny lätt vägg byggs med reglar, ljudisolering och "
       "skivor och får en dörr som passar resten av lägenheten.",
       "Ska köket göras om samtidigt samordnar vi snickeriet med " + a("koksrenovering-solna.html",
       "köksrenoveringen i Solna") + ", så att föreningen får ett samlat underlag och arbetet kan "
       "planeras i en följd."],
     "aside": None}],
  "steps_h2": "Arbetsgång för snickeri i Solna",
  "steps": [
    ("Vem godkänner?", "Vi reder ut om arbetet behöver föreningens tillstånd, en anmälan till staden eller "
     "bygglov – eller inget av dem."),
    ("Uppmätning", "Vid besöket mäter vi rum, dörröppningar och nischer och letar efter tecken på bärande "
     "väggar."),
    ("Handlingar", "Du får ritning och beskrivning att lämna till styrelsen och, när det behövs, underlag "
     "för anmälan."),
    ("Material i rätt mått", "Dörrar, skivor och virke beställs i storlekar som går in genom porten och upp "
     "i trapphuset."),
    ("Montering", "Väggar, dörrar och förvaring byggs med skyddat trapphus och efter föreningens tider för "
     "bullrande arbete."),
    ("Slutgenomgång", "Vi går igenom arbetet med dig och lämnar dokumentation som kan sparas eller lämnas "
     "till föreningen.")],
  "rot_h2": "Vad ger ROT i en bostadsrätt i Solna?",
  "rot": [
    "I en bostadsrätt räknar " + ext(SKV_ARB, "Skatteverket") + " bara arbete inne i lägenheten. Att byta "
    "innerdörrar, riva innerväggar och bygga om planlösningen eller montera platsbyggda garderober ger "
    "avdrag. Att byta själva ytterdörren gör det inte, men arbete på dörrens insida gör det. Balkong och "
    "inglasning ligger utanför.",
    "Avdraget motsvarar 30 procent av arbetskostnaden inklusive moms. Per person och år kan rot ge högst "
    "50 000 kr, inom ett gemensamt tak på 75 000 kr för rot och rut. Material och resor räknas inte in. "
    "Vi drar av beloppet på vår faktura."],
  "price_h2": "Det här styr priset",
  "price": [
    "I en lägenhet påverkas priset mest av om något bärande berörs, vilka dörrar och skivor som behövs och "
    "hur lätt det är att få upp material i huset. Vid ett radhus spelar marken och en eventuell "
    "lovansökan in. Efter ett kostnadsfritt besök får du ett skriftligt kostnadsförslag."],
  "faq": [
    ("Får jag byta lägenhetsdörren i min bostadsrätt i Solna utan att fråga styrelsen?",
     "Räkna med att styrelsen ska tillfrågas. Bostadsrättslagen kräver styrelsens tillstånd för åtgärder "
     "som påverkar brandskyddet, och dörren mot trapphuset är en del av det. Att byta ytterdörren ger "
     "dessutom inget rotavdrag i en bostadsrätt."),
    ("Kan vi glasa in balkongen i Solna utan bygglov?",
     "Nej. Solna stad skriver att inglasning av balkong kräver bygglov för fasadändring, och att det på "
     "vissa platser inte är tillåtet. Det är föreningen som fastighetsägare som behöver stå bakom ansökan."),
    ("Får vi bygga en friggebod vid vårt radhus i Solna?",
     "I stora delar av Solna krävs bygglov även för en friggebod, eftersom områdena är kulturhistoriskt "
     "värdefulla eller ligger inom riksintressen. Kontrollera fastigheten i Solnakartan innan något "
     "beställs."),
    ("Behöver ett förråd nära järnvägen i Solna bygglov?",
     "Ja, om det placeras närmare än 30 meter från ett järnvägsspårs mitt. Undantaget från bygglov gäller "
     "då bara med infrastrukturförvaltarens skriftliga medgivande."),
    ("Vem ansvarar om inglasningen av vår balkong inte följer bygglovet?",
     "Den som låter utföra arbetet är byggherre och ansvarar, även när en leverantör gör jobbet. Staden "
     "råder därför föreningen att ställa krav på att bygget följer lovet och kontrollplanen och att begära "
     "slutbesked.")],
  "sources": [
    ("Solna stad – För lägenhetsinnehavare", S_LAG),
    ("Solna stad – För villaägare", S_VILLA),
    ("Solna stad – Bygglovsfria åtgärder", S_FRI),
    ("Solna stad – Kulturmiljöer i Solna", S_KM),
    ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §", BRL),
    ("Boverket – Bygga en ny byggnad", BV_NY),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska lägenheten få en ny vägg eller mer förvaring?", "Berätta vad du planerar så kommer vi till "
          "Solna och mäter upp, utan kostnad."),
  "img": [("Ljus bostadsrätt i Solna med platsbyggd garderob och vit innerdörr",
           "bright 1950s Scandinavian apartment interior, white built-in wardrobe with panelled doors, white "
           "interior door with simple casing, oak parquet floor, large window and balcony door, Solna "
           "Stockholm, no people, no text"),
          ("Nybyggd innervägg med dörr i en lägenhet från 1950-talet",
           "newly built interior partition wall with white flush interior door and simple painted casings "
           "in a 1950s Scandinavian apartment, freshly finished carpentry, tools neatly on the floor, no "
           "people, no hands, no text")],
  "related": [("malare-solna.html", "Målare i Solna", "Snickerier, kulör och bygglov."),
              ("koksrenovering-solna.html", "Köksrenovering i Solna", "Kök i bostadsrätt och villa."),
              ("badrumsrenovering-solna.html", "Badrumsrenovering i Solna", "Badrum vid stambyte och i villa.")],
},

# ---------------------------------------------------------------- HUDDINGE
"snickare-huddinge.html": {
  "kind": "district", "service": "snickare", "ort": "Huddinge", "svc_label": "Snickare",
  "title": "Snickare i Huddinge – altan, förråd och gäststuga",
  "description": "Snickare i Huddinge: altaner, förråd, gäststugor och tillbyggnader vid egnahem, "
                 "50-talsvillor och sportstugor. Potten för lovfria byggnader och ROT.",
  "h1": "Snickare i Huddinge",
  "lead": "I Huddinge handlar många snickeriuppdrag om det som byggs vid sidan av huset: en altan, ett "
          "förråd, en gäststuga eller en tillbyggnad. Sedan december 2025 delar sådana byggnader på en "
          "gemensam pott, och kommunens kulturmiljöprogram ger råd om var på tomten de passar. Vi hjälper "
          "dig att se vad som får plats innan något byggs.",
  "card": "Altaner, förråd och gäststugor.",
  "sections": [
    {"id": "tomten", "anchor": "Tomterna i Huddinge",
     "h2": "Förgården, baksidan och skogstomten",
     "paras": [
       "Del 2 av kommunens " + ext(H_KM2, "kulturmiljöprogram") + " beskriver egnahemsområdena från "
       "1910–40-talet med villor indragna från vägen och en stor förgårdsmark med äldre fruktträd och "
       "buskar, avskärmad med häck eller staket. Där råder programmet att garage inte placeras vid gatan, "
       "eftersom förgårdens öppna rum då sluts, och att plank bara sätts upp där det är bullerstört.",
       "För småhusområdena från 1940–50-talet avråder programmet från tillbyggnader, större skärmtak och "
       "inglasade uteplatser mot gatan, och från stora altandäck och höga stödmurar på kuperade tomter. I "
       "områdena från 1960–80-talet bör carport, garage och andra komplementbyggnader inte stå på "
       "förgårdsmarken, och burspråk och större skärmtak mot gatan bör undvikas.",
       "Råden för 1940–50-talets och 1960–80-talets områden gäller enligt programmet alla sådana "
       "småhusområden i kommunen, även de som inte ingår i ett utpekat kulturmiljöområde. All bebyggelse "
       "omfattas dessutom av varsamhetskravet i plan- och bygglagen."],
     "aside": {"title": "Programmets råd i korthet",
               "items": ["Egnahem 1910–40-tal: garage inte vid gatan",
                         "1940–50-tal: undvik stora altandäck i slänt",
                         "1960–80-tal: carport inte på förgårdsmarken",
                         "Plank bara där det är bullerstört"]}},
    {"id": "pott",
     "h2": "En pott för förråd, gäststuga och komplementbostadshus",
     "paras": [
       "Huddinge kommun skriver i sin genomgång av " + ext(H_PBL, "förändringarna i PBL") + " att attefalls- "
       "och friggebodsreglerna har slopats och ersatts av regler med en pott för lovbefriade åtgärder. "
       "Enligt " + ext(BV_NY, "Boverket") + " får den största byggnaden inom detaljplan vara 30 "
       "kvadratmeter och alla tillsammans 45 kvadratmeter, med högst 4 meter till nock. Byggnaden ska vara "
       "mindre än bostadshuset och stå minst 4,5 meter från tomtgränsen om grannen inte skriftligen "
       "medger något annat. Utanför detaljplan är gränserna 50 och 65 kvadratmeter.",
       "Det som redan står på tomten räknas in. Har du ett attefallshus på 30 kvadratmeter och en "
       "friggebod på 15 kvadratmeter går det inte att bygga mer lovfritt inom detaljplan. Ska byggnaden "
       "få vatten, avlopp, eldstad eller ventilation krävs en anmälan.",
       "Ett komplementbostadshus är en fristående bostad som ska uppfylla kraven för bostäder, med kök, "
       "toalett och dusch, och kunna användas utan att vara beroende av huvudbyggnaden. Mer om reglerna "
       "finns i guiden om " + a("attefallshus.html", "attefallshus") + "."],
     "aside": {"title": "Inom detaljplan, utan lov",
               "items": ["Största byggnaden: 30 kvm",
                         "Sammanlagt på tomten: 45 kvm",
                         "Nockhöjd: högst 4 meter",
                         "Minst 4,5 m till gräns eller medgivande"]}},
    {"id": "stugor",
     "h2": "Sportstugor och sommarvillor vid sjöarna",
     "paras": [
       "Enligt kulturmiljöprogrammet tog byggandet av sportstugor fart i Huddinge under 1930- och "
       "40-talet, främst vid Orlången, Ådran, Kvarnsjön och Magelugnen, och på tidigare jordbruksmark vid "
       "Vårby, Glömsta och Länna gårdar. Semesterlagen 1938 gav alla arbetare rätt till två veckors "
       "semester. Stugorna är små och enkla, ofta röda med vita knutar, och har komplementbyggnader som "
       "gäststuga, vedbod, utedass och jordkällare.",
       "För sportstugeområdena råder programmet att huvudbyggnaden hålls i en mindre volym och att "
       "komplementbyggnader uppförs fristående, en bit in på tomten. I praktiken passar en ny gäststuga "
       "eller vedbod ofta bättre än en stor tillbyggnad på själva stugan.",
       "Äldre än stugorna är sommarvillorna i Masmo vid Albysjöns strand. Programmet beskriver sommarnöjena från "
       "1880–1920-talet som stora trävillor med glasverandor, snickarglädje och spröjsade fönster. Ligger "
       "tomten nära vatten gäller strandskyddet, som enligt Boverket omfattar 0–300 meter från "
       "strandlinjen."],
     "aside": None},
    {"id": "regler",
     "h2": "Nya byggregler och kontrollplan",
     "paras": [
       "Från den 1 juli 2025 gäller nya byggregler som ersätter Boverkets byggregler, BBR. Kommunen "
       "förklarar att de nya reglerna beskriver vad som ska uppnås, till exempel att byggnaden ska vara "
       "energisnål och säker, i stället för exakt hur det ska göras. Övergångstiden löpte till den 30 juni "
       "2026, och för ansökningar som kommer in efter den 1 juli 2026 gäller bara de nya reglerna.",
       "För byggherren betyder det mer dokumentation. Kontrollplanen ska visa vilket regelverk som följs "
       "och hur kraven kontrolleras, och den ska vara anpassad till projektet. Kommunen råder att man "
       "identifierar de mest riskfyllda momenten och lägger kontrollerna där. Vid en " +
       a("tillbyggnad.html", "tillbyggnad") + " är det ofta anslutningen mot befintligt tak och vägg.",
       "Kommunen påminner också om att fler åtgärder kräver bygglov i områden med riksintressen, i "
       "kulturhistoriskt värdefulla miljöer och nära totalförsvarets anläggningar, och att lovbefrielsen "
       "där ofta inte gäller. Den som är osäker kan boka tid med en bygglovshandläggare."],
     "aside": {"title": "Inför ett lovfritt bygge",
               "items": ["Räkna ihop friggebodar och attefallshus",
                         "Mät avståndet till tomtgränsen",
                         "Ska vatten eller ventilation in? Anmälan",
                         "Spara ritningar och kontrollpunkter"]}}],
  "steps_h2": "Från idé till färdigt bygge i Huddinge",
  "steps": [
    ("Tomten och potten", "Vi går igenom vad som redan står på tomten och hur mycket som återstår av den "
     "lovfria ytan."),
    ("Läge på tomten", "Vi föreslår en placering som fungerar med terrängen, grannarna och kommunens råd för "
     "husets epok."),
    ("Ritning och kontrollplan", "Du får ritningar och, när det behövs, ett förslag till kontrollplan enligt "
     "de nya byggreglerna."),
    ("Grund och stomme", "Plintar eller platta anpassas till marken, och stommen reses med skydd mot väder."),
    ("Panel, fönster och trall", "Utvändiga delar monteras, och vi samordnar el och VVS om sådant ingår."),
    ("Avslut och papper", "Vi går igenom bygget med dig och lämnar en sammanställning att spara.")],
  "rot_h2": "ROT för altan och tillbyggnad – inte för fristående förråd",
  "rot": [
    "Rotavdraget gäller arbete på eller i anslutning till bostaden. " + ext(SKV_ARB, "Skatteverket") +
    " godtar altaner och balkonger som är ihopbyggda med huset, och en tillbyggnad av förråd eller "
    "gäststuga som sitter ihop med huset kan också ge avdrag. En ny fristående byggnad, till exempel ett "
    "garage, eller en ny friggebod ger däremot inget avdrag.",
    "Avdraget är 30 procent av arbetskostnaden och kan bli högst 50 000 kr per person och år; rot och rut "
    "har ett gemensamt tak på 75 000 kr. Vid om- och tillbyggnad ska det ha gått fem år från husets "
    "värdeår. En möblerad stuga som du äger och använder som fritidshus räknas också. Vi drar avdraget på "
    "fakturan."],
  "price_h2": "Vad påverkar kostnaden för bygget?",
  "price": [
    "Storlek, grundläggning och hur kuperad tomten är väger tyngst, liksom om byggnaden ska isoleras och "
    "få vatten och avlopp eller bara vara ett kallt förråd. En gäststuga på en sluttande skogstomt kräver "
    "mer markarbete än ett förråd på en plan egnahemstomt. Platsbesöket kostar inget, och därefter får du "
    "ett skriftligt kostnadsförslag."],
  "faq": [
    ("Hur mycket mer får vi bygga på tomten i Stuvsta om vi redan har en friggebod?",
     "Inom detaljplan är potten 45 kvadratmeter, och friggeboden räknas in. Har den 15 kvadratmeter "
     "återstår 30, vilket också är maxstorleken för en enskild byggnad. Ligger fastigheten i ett "
     "kulturhistoriskt värdefullt område krävs bygglov oavsett."),
    ("Kan sportstugan vid Orlången få en tillbyggnad?",
     "Det beror på planen och strandskyddet. Kulturmiljöprogrammet råder att huvudbyggnaden hålls liten "
     "och att nya byggnader uppförs fristående, så en separat gäststuga kan vara en bättre lösning."),
    ("Får carporten stå mot gatan i vårt 70-talsområde i Huddinge?",
     "Kulturmiljöprogrammet råder att inga komplementbyggnader, som carport eller garage, placeras på "
     "förgårdsmarken i områden från 1960–80-talet. Rådet gäller även områden som inte är utpekade."),
    ("Vilka byggregler gäller om vi söker bygglov för en tillbyggnad i Huddinge nu?",
     "För ansökningar som kommer in efter den 1 juli 2026 gäller bara de nya byggreglerna, och "
     "kontrollplanen ska vara gjord enligt dem."),
    ("Måste gäststugan anmälas om den får dusch och toalett?",
     "Ja. Även om byggnaden ryms i den lovfria potten krävs en anmälan till byggnadsnämnden när vatten och "
     "avlopp eller ventilation installeras, och du behöver vänta på startbesked.")],
  "sources": [
    ("Huddinge kommun – Kulturmiljöprogram del 2 (småhus och semesterbostäder, pdf)", H_KM2),
    ("Huddinge kommun – Förändringar i byggregler samt plan- och bygglagen", H_PBL),
    ("Boverket – Bygga en ny byggnad", BV_NY),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Funderar du på en gäststuga eller altan?", "Berätta vad som redan står på tomten så kommer vi ut "
          "till Huddinge och tittar – utan kostnad."),
  "img": [("Röd sportstuga med vita knutar och en liten gäststuga på en skogstomt i Huddinge",
           "small red wooden Swedish cottage with white corner boards and a separate small guest cabin on a "
           "hilly forest plot with pine trees and rock outcrops near a lake, Huddinge south of Stockholm, "
           "summer, no people, no text"),
          ("Nybyggd altan i trä på baksidan av ett egnahem med fruktträd",
           "newly built wooden deck with simple railing at the garden side of a 1930s Swedish wooden house, "
           "old apple trees and lawn, carpentry just finished, no people, no hands, no text")],
  "related": [("malare-huddinge.html", "Målare i Huddinge", "Egnahem, tegelvillor och stugor."),
              ("badrumsrenovering-huddinge.html", "Badrumsrenovering i Huddinge", "Från sportstuga till grupphus.")],
},

# ---------------------------------------------------------------- SOLLENTUNA
"snickare-sollentuna.html": {
  "kind": "district", "service": "snickare", "ort": "Sollentuna", "svc_label": "Snickare",
  "title": "Snickare i Sollentuna – altan, uterum och brygga",
  "description": "Snickare i Sollentuna: altaner, uterum och tillbyggnader vid villor och radhus, bryggor "
                 "och trädäck nära Edsviken. Kommunens regler, strandskydd och ROT.",
  "h1": "Snickare i Sollentuna",
  "lead": "Som snickare i Sollentuna bygger man ofta utomhus: en altan, ett uterum, ett skärmtak över "
          "entrén eller en brygga vid vattnet. Kommunen har egna sidor för varje åtgärd, och strandskyddet "
          "gör att samma trädäck kan bedömas olika beroende på var tomten ligger. Därför börjar vi med "
          "detaljplanen och mäter innan något ritas.",
  "card": "Altaner, uterum och bryggor.",
  "sections": [
    {"id": "altan", "anchor": "Altan i Sollentuna",
     "h2": "När altanen blir en tillbyggnad",
     "paras": [
       "Sollentuna kommun skriver på sin sida om " + ext(SOL_ALT, "altan") + " att ett vanligt trädäck "
       "direkt på marken oftast inte kräver bygglov. Innehåller konstruktionen ett utrymme under altanen "
       "kan den i stället bedömas som en tillbyggnad. Inom detaljplan krävs lov om altanen blir högre än "
       "1,8 meter över marken inom 3,6 meter från en byggnad, eller högre än 1,2 meter längre ut.",
       "En lovbefriad altan som tillsammans med tomtens övriga altaner har en yta under 50 kvadratmeter får "
       "strida mot detaljplanen. Den får dock inte placeras eller utformas så att trafiksäkerheten "
       "påverkas.",
       "På en sluttande tomt blir altanen lätt hög på baksidan även när den är låg vid husväggen. Vi mäter "
       "därför höjden både vid huset och vid ytterkanten innan vi föreslår ett utförande, och vi räknar "
       "med att ett förråd under altanen kan göra den till en tillbyggnad."],
     "aside": {"title": "Kontrollera före bygget",
               "items": ["Höjd över mark vid huset och ytterkanten",
                         "Avstånd till byggnaden: 3,6 meter",
                         "Altanytan på hela tomten",
                         "Blir det ett utrymme under?"]}},
    {"id": "tillbyggnad",
     "h2": "Uterum, skärmtak och kupor delar på 30 kvadratmeter",
     "paras": [
       "Med " + ext(SOL_TILL, "tillbyggnad") + " menar kommunen alla åtgärder som ökar byggnadens volym, "
       "oavsett om det sker uppåt, åt sidan eller nedåt. På ett en- eller tvåbostadshus får tillbyggnader "
       "göras utan lov upp till sammanlagt 30 kvadratmeter brutto- eller öppenarea, och de får inte bli "
       "högre än husets taknock. De tidigare undantagen för attefallstillbyggnad, takkupor och skärmtak "
       "har tagits bort, men det som byggts med stöd av dem räknas in i de 30 kvadratmetrarna. Lovbefriade "
       "tillbyggnader får strida mot gällande detaljplan.",
       "För radhus, kedjehus och andra sammanbyggda småhus skriver kommunen att möjligheterna varierar "
       "med hur bebyggelsen är utformad, och hänvisar till Kontaktcenter. En anmälan krävs om tillbyggnaden "
       "påverkar bärande konstruktion eller brandskyddet, till exempel skyddet mot brandspridning till "
       "andra byggnader. Det kan bli aktuellt i en radhuslänga.",
       "Inför en större utbyggnad finns mer om planering och ytor på sidan om " +
       a("tillbyggnad.html", "tillbyggnad") + "."],
     "aside": None},
    {"id": "kulturvarde",
     "h2": "Kulturvärden bedöms utifrån foton",
     "paras": [
       "Inom kulturhistoriskt särskilt värdefulla områden går de bygglovsbefriade åtgärderna inte att "
       "använda, enligt kommunens sida om " + ext(SOL_KM, "kulturhistoriska byggnader och områden") + ". I "
       "kartan med gällande detaljplaner finns ett lager med kulturmiljöplanen, men kommunen påpekar att en "
       "byggnad kan vara särskilt värdefull även om den inte finns med där.",
       "Är man osäker kan man be kommunen om en bedömning. Den vill då ha adress eller "
       "fastighetsbeteckning, foton på huset från samtliga väderstreck och en beskrivning av det man vill "
       "göra. Den som vill vara säker på att en lovfri åtgärd uppfyller lagens krav kan också söka ett "
       "frivilligt bygglov.",
       "Krävs bygglov för altanen anger kommunen en handläggningstid på ungefär 4–10 veckor. Ansökan görs "
       "via e-tjänst och ska innehålla situationsplan och plan-, fasad- och sektionsritningar."],
     "aside": None},
    {"id": "strand",
     "h2": "Brygga och trädäck nära Edsviken",
     "paras": [
       "Inom strandskyddat område krävs dispens för att bygga nytt, ändra byggnader eller deras "
       "användning, utöka den privata hemfridszonen, gräva inför ett bygge och sätta upp bryggor. På sidan "
       "om " + ext(SOL_STR, "strandskydd") + " skriver kommunen att den är mycket restriktiv till nya "
       "bryggor och att en befintlig brygga ska byggas om varsamt och inte bli större än den som finns. "
       "Arbete i vatten kräver dessutom tillstånd för vattenverksamhet hos länsstyrelsen.",
       "Dispens behövs inte om strandskyddet är upphävt i detaljplanen. Beviljas dispens granskar "
       "länsstyrelsen beslutet inom högst tre veckor, och arbetet bör inte påbörjas förrän beslutet har "
       "vunnit laga kraft. Kommunen anger en handläggningstid på ungefär 10–52 veckor. Ansökan ska "
       "innehålla situationsplan, ritningar, fotografier och en beskrivning av växtlighet, arter och den "
       "allemansrättsliga tillgängligheten på platsen.",
       "I " + ext(SOL_GR, "granskningsutlåtandet till översiktsplanen") + " skriver kommunen att den generellt "
       "vill minska antalet bryggor i Edsviken. Planerar du en brygga är det alltså klokt att utgå från "
       "den som redan finns."],
     "aside": {"title": "Dispens krävs inom strandskydd för",
               "items": ["Nytt trädäck eller ny byggnad",
                         "Utökad hemfridszon",
                         "Ny eller större brygga",
                         "Grävning inför ett bygge"]}}],
  "steps_h2": "Arbetsgången i Sollentuna",
  "steps": [
    ("Detaljplan och strandskydd", "Vi läser planen för fastigheten och ser om strandskyddet är upphävt "
     "eller om dispens behövs."),
    ("Mått på plats", "Höjder, avstånd till hus och tomtgräns och tidigare lovfria tillbyggnader mäts upp."),
    ("Underlag om kulturvärde", "Är det oklart om huset är särskilt värdefullt skickas foton och en "
     "beskrivning till kommunen först."),
    ("Förslag och kostnad", "Du får ett skriftligt förslag med material, utförande och vad som eventuellt "
     "ska sökas."),
    ("Byggstart", "Plintar, stomme och trall eller väggar byggs i den ordning väder och mark tillåter."),
    ("Kontroll och genomgång", "Vi kontrollerar höjder och infästningar och går igenom arbetet med dig.")],
  "rot_h2": "ROT i Sollentuna – altan ja, brygga nej",
  "rot": [
    ext(SKV_ARB, "Skatteverket") + " räknar bygge och reparation av en altan som sitter ihop med huset som "
    "rotarbete, liksom inglasning av altanen och en tillbyggnad som byggs ihop med bostaden. Att reparera "
    "en båtbrygga ger däremot inget avdrag, och inte heller ett nytt fristående garage.",
    "Du kan få tillbaka 30 procent av arbetskostnaden, med ett tak på 50 000 kr i rotavdrag per person och "
    "år och 75 000 kr för rot och rut sammanlagt. Är huset yngre än fem år från värdeåret ger om- och "
    "tillbyggnad inget avdrag. Materialet betalas fullt ut, och avdraget görs på fakturan."],
  "price_h2": "Vad kostar altanen eller uterummet?",
  "price": [
    "Det avgörs främst av storlek, höjd över marken, grundläggning och materialval, och av om bygget kräver "
    "lov, anmälan eller strandskyddsdispens. En låg altan på plan mark är enklare än ett högt trädäck i en "
    "slänt mot vattnet. Vi kommer ut gratis, mäter och lämnar sedan ett skriftligt kostnadsförslag."],
  "faq": [
    ("Blir altanen i Sollentuna en tillbyggnad om vi bygger ett förråd under den?",
     "Det kan den bli. Kommunen skriver att en altan med ett utrymme under kan bedömas som en tillbyggnad, "
     "och då räknas ytan in i de 30 kvadratmeter som får byggas till lovfritt."),
    ("Får vi bygga om vår gamla brygga vid Edsviken?",
     "Det kräver strandskyddsdispens om strandskyddet inte är upphävt. Kommunen vill att ombyggnaden görs "
     "varsamt och att bryggan inte blir större än i dag, och arbete i vattnet kräver tillstånd från "
     "länsstyrelsen."),
    ("Vad ska vi skicka till kommunen för att få veta om huset har kulturvärde?",
     "Adress eller fastighetsbeteckning, foton på huset från samtliga väderstreck och en beskrivning av "
     "vad ni vill göra. Kommunen återkommer sedan med en bedömning."),
    ("Har varje radhus i en länga i Sollentuna egna 30 kvadratmeter för tillbyggnad?",
     "Kommunen skriver att möjligheterna för radhus och kedjehus beror på hur bebyggelsen är utformad och "
     "ber dig kontakta Kontaktcenter. Påverkar tillbyggnaden skyddet mot brandspridning till grannen krävs "
     "en anmälan."),
    ("När får vi börja bygga efter en beviljad strandskyddsdispens?",
     "Först när beslutet har vunnit laga kraft. Länsstyrelsen granskar alla dispenser och kan överpröva "
     "beslutet, och du ansvarar själv för att kontrollera att det inte har överprövats eller överklagats.")],
  "sources": [
    ("Sollentuna kommun – Altan", SOL_ALT),
    ("Sollentuna kommun – Tillbyggnad en- eller tvåbostadshus", SOL_TILL),
    ("Sollentuna kommun – Kulturhistoriska byggnader och områden", SOL_KM),
    ("Sollentuna kommun – Strandskydd", SOL_STR),
    ("Sollentuna kommun – Granskningsutlåtande till översiktsplan Sollentuna 2040 (pdf)", SOL_GR),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Planerar ni en altan eller ett uterum?", "Berätta om tomten så kommer vi ut till Sollentuna och "
          "mäter – platsbesöket kostar inget."),
  "img": [("Trädäck på en sluttande villatomt ner mot en vik i Sollentuna",
           "wooden deck terrace on a sloping garden of a Swedish villa leading down to a calm lake bay with "
           "reeds and a small old wooden jetty, birch and pine trees, Sollentuna north of Stockholm, summer "
           "evening light, no people, no text"),
          ("Ny altan på stolpar med räcke vid ett radhus i slänt",
           "close-up of a new wooden deck on posts with simple railing at the back of a Swedish 1970s "
           "terraced house on sloping ground, carpentry just completed, no people, no hands, no text")],
  "related": [("malare-sollentuna.html", "Målare i Sollentuna", "Villastad och radhuslängor."),
              ("badrumsrenovering-sollentuna.html", "Badrumsrenovering i Sollentuna", "Ventilation och stammar.")],
},

# ---------------------------------------------------------------- LIDINGÖ
"snickare-lidingo.html": {
  "kind": "district", "service": "snickare", "ort": "Lidingö", "svc_label": "Snickare",
  "title": "Snickare på Lidingö – verandor, trappor och dörrar",
  "description": "Snickare på Lidingö: glasverandor och trätrappor i Grönstakolonin, entréer i ekpanel på "
                 "Ekorrvägen och fast inredning i äldre villor. Regler och ROT.",
  "h1": "Snickare på Lidingö",
  "lead": "På Lidingö är det ofta detaljerna som ska lagas: en glasveranda som en gång ersatte en "
          "förstukvist, en enkel trätrappa, en entrédörr i ekpanel eller en platsbyggd bokhylla i en äldre "
          "villa. Stadens kulturmiljöprogram från 2024 beskriver många av dem område för område. Vi lagar "
          "hellre än byter och planerar arbetet efter det programmet säger.",
  "card": "Verandor, trappor och dörrar.",
  "sections": [
    {"id": "gronsta", "anchor": "Husen på Lidingö",
     "h2": "Grönstakolonin – förstukvistar som blev glasverandor",
     "paras": [
       ext(L_GRON, "Grönstakolonin") + " tillkom 1910 på initiativ av ingenjören Stig Milles och lär enligt "
       "kulturmiljöprogrammet vara Sveriges äldsta sportstugeområde. De första stugorna byggdes i "
       "plankkonstruktion på stenplintar, med faluröd liggande panel, vita snickerier och branta, "
       "papptäckta sadeltak. Redan på 1920-talet byggdes många ut och förlängdes, och ofta ersattes den "
       "öppna förstukvisten av en glasveranda.",
       "Beskrivningen är full av detaljer som en snickare arbetar med: vita tätspröjsade fönster, gröna "
       "fönsterluckor och trädörrar, enkla utvändiga trätrappor och kryssmönstrade lister som sitter likt "
       "spaljéer mellan fasad och grund. Mot den smala gångvägen, bygatan, avgränsas lotterna med låga "
       "trästaket och en gärdesgård med små grindar. Nästan alla stugor är envåningshus, de flesta med "
       "faluröd fjällpanel.",
       "Programmet råder att tillbyggnader undviks och att äldre byggnadsdetaljer som fönster, dörrar och "
       "farstukvistar i originalutförande ska värnas. Området är dessutom riksintresse för "
       "kulturmiljövården. En sliten veranda lagas därför med samma spröjsindelning, och en trappa byggs "
       "om i samma enkla form."],
     "aside": {"title": "Detaljer i Grönstakolonin",
               "items": ["Glasverandor och öppna förstukvistar",
                         "Enkla utvändiga trätrappor",
                         "Kryssmönstrade lister mot grunden",
                         "Låga trästaket och små grindar"]}},
    {"id": "ekorrvagen",
     "h2": "Ekorrvägen – entréer i liggande ekpanel",
     "paras": [
       "De trettio radhusen på " + ext(L_NASET, "Ekorrvägen") + " nedanför Näset ritades av arkitekten "
       "Ernst Grönwall 1962. De ligger i fem grupper om sex hus, i souterräng med en våning mot gatan och "
       "två mot sluttningen. Ett garage i vinkel ger varje hus en skyddad liten uteplats, och entrén är "
       "indragen där garaget möter bostadsdelen.",
       "Dörrar och garagedörrar är klädda med horisontell ekpanel, och mot sluttningen löper en "
       "loftliknande balkong längs fasaden. Kulturmiljöprogrammet noterar att några entrénischer har "
       "byggts in och att några dörrar och garageportar har bytts. De indragna nischerna med ekpanelade "
       "dörrar räknas som ett av områdets karaktärsdrag.",
       "En ekpanelad dörr går ofta att renovera: skadade ribbor byts mot nya i samma dimension, dörren "
       "justeras i karmen och tätningen förnyas. Då behåller entrén sitt uttryck utan att nischen behöver "
       "byggas om."],
     "aside": None},
    {"id": "inne",
     "h2": "Även snickerier inomhus kan omfattas",
     "paras": [
       "I programmets " + ext(L_DEL1, "handbok för fastighetsägare") + " står att förvanskningsförbudet i "
       "8 kap. 13 § plan- och bygglagen även kan tillämpas på interiörer, som kakelugnar, rumssamband, "
       "snickerier och annan fast inredning som är betydelsefull för byggnadens värde. Förbudet gäller "
       "förvanskning, inte förändring, och bara särskilt värdefulla byggnader och områden.",
       "Innan inbyggda skåp, dörrar eller lister rivs i en äldre villa är det därför värt att ta reda på vad "
       "som finns om huset. Staden har byggnadsinventeringar från 1970- och 80-talet och från 2013–2015, "
       "och äldre bygglovshandlingar i arkivet. Lidingö hembygdsförening har ett stort fotoarkiv.",
       "Handbokens råd är att begränsa ingreppen och bevara och reparera det som fungerar. Den påpekar också "
       "att så kallade underhållsfria material inte kan underhållas utan måste bytas när de har tjänat ut. "
       "För en trätrappa eller ett fönster betyder det att trasiga delar lagas med trä av samma slag och att "
       "resten får sitta kvar."],
     "aside": {"title": "Här finns husets historia",
               "items": ["Stadens byggnadsinventeringar",
                         "Äldre bygglovshandlingar i arkivet",
                         "Hembygdsföreningens fotoarkiv",
                         "Detaljplanens q-, k- och r-bestämmelser"]}},
    {"id": "regler",
     "h2": "Lov, fackmässighet och bidrag",
     "paras": [
       "Utanför de värdefulla områdena kräver fasadändringar på en- och tvåbostadshus inte längre bygglov, "
       "tillbyggnader upp till 30 kvadratmeter är lovfria och komplementbyggnader delar på en pott om 45 "
       "kvadratmeter inom detaljplan. Inom särskilt kulturhistoriskt värdefulla områden gäller utökad "
       "lovplikt för de flesta åtgärder, och stadens webbkarta visar vilka fastigheter som berörs, skriver "
       "staden på sidan om " + ext(L_NYA, "ändrade regler för byggande") + ".",
       "Med de nya byggreglerna lägger staden vikt vid fackmässighet. I handlingarna ska det framgå vilken "
       "lösning eller metod som valts och vilket underlag, till exempel en standard eller handbok, som "
       "använts. En riskbedömning ska bifogas kontrollplanen, och nämnden kan begära komplettering. "
       "Byggherren ansvarar för att arbetet är fackmässigt, oavsett vem som utför det. I detaljplanerna "
       "anger q skydd av kulturvärden, k byggnadens karaktärsdrag och r rivningsförbud.",
       "Är huset kulturhistoriskt särskilt värdefullt kan du enligt stadens " + ext(L_FAQ, "frågor och svar") +
       " söka byggnadsvårdsbidrag hos länsstyrelsen. Gäller arbetet en större tillbyggnad finns mer på sidan "
       "om " + a("byggforetag-lidingo.html", "byggföretag på Lidingö") + "."],
     "aside": None}],
  "steps_h2": "Så arbetar vi med snickeri på Lidingö",
  "steps": [
    ("Husets historia", "Vi tittar på byggår, eventuella inventeringar och vad kulturmiljöprogrammet säger "
     "om området."),
    ("Besiktning av detaljerna", "Veranda, trappa, dörrar och fönster gås igenom del för del, så att det som "
     "håller får sitta kvar."),
    ("Lagning eller kopia", "Skadade delar lagas, och det som inte går att rädda kopieras efter en bevarad "
     "förlaga."),
    ("Handlingar vid lovplikt", "Krävs lov tas ritningar och en kontrollplan med riskbedömning fram."),
    ("Utförande", "Arbetet görs etappvis och samordnas med målare när nytt trä ska grundas."),
    ("Överlämning", "Vi går igenom arbetet med dig och beskriver vilka material och metoder som använts.")],
  "rot_h2": "ROT för trappor, dörrar och verandor",
  "rot": [
    ext(SKV_ARB, "Skatteverket") + " räknar flera av de vanligaste uppdragen här som rotarbete i småhus: att "
    "reparera entrétrappor som är ihopbyggda med huset, att byta och reparera dörrar och fönster och att "
    "bygga eller laga en altan eller balkong som sitter ihop med huset. Staket och nya fristående byggnader "
    "ger inget avdrag.",
    "Avdraget är 30 procent av arbetskostnaden. Taket är 50 000 kr per person och år för rot och 75 000 kr "
    "för rot och rut tillsammans, och bara arbetet räknas, inte material eller resor. Reparation och "
    "underhåll ger avdrag oavsett hur gammalt huset är. Beloppet dras direkt på din faktura."],
  "price_h2": "Vad påverkar priset på Lidingö?",
  "price": [
    "Mest betyder hur mycket av originalet som kan sparas, om dörrar, spröjs eller lister måste "
    "specialtillverkas och om arbetet kräver lov. En glasveranda med tätspröjsade bågar tar längre tid än en "
    "ny trätrappa i enkel form. Vi gör ett kostnadsfritt besök och lämnar sedan ett skriftligt "
    "kostnadsförslag."],
  "faq": [
    ("Får vi glasa in förstukvisten på vår stuga i Grönstakolonin?",
     "Det kräver bygglov eftersom området är särskilt kulturhistoriskt värdefullt. Programmet råder dessutom "
     "att farstukvistar i originalutförande värnas och att tillbyggnader undviks, så ta kontakt med miljö- "
     "och stadsbyggnadskontoret innan något ritas."),
    ("Kan ekpanelen på ytterdörren till ett radhus på Ekorrvägen renoveras?",
     "Oftast ja. Kulturmiljöprogrammet räknar dörrarna i liggande ekpanel till områdets karaktärsdrag, och "
     "skadade ribbor kan bytas mot nya i samma dimension."),
    ("Kan inbyggda skåp i vår villa på Lidingö omfattas av förvanskningsförbudet?",
     "Det kan de, om huset är särskilt värdefullt och den fasta inredningen är betydelsefull för dess värde. "
     "Fråga staden innan skåpen rivs."),
    ("Var hittar vi gamla foton på vårt hus på Lidingö?",
     "Lidingö hembygdsförening har ett stort fotoarkiv, och stadens kundcenter kan ta fram äldre "
     "bygglovshandlingar och eventuella inventeringar av huset."),
    ("Finns det bidrag för att laga verandan på ett kulturhistoriskt värdefullt hus?",
     "Ja, är huset kulturhistoriskt särskilt värdefullt kan du söka byggnadsvårdsbidrag hos länsstyrelsen.")],
  "sources": [
    ("Lidingö stad – Kulturmiljöprogram del 2: Grönstakolonin (pdf)", L_GRON),
    ("Lidingö stad – Kulturmiljöprogram del 2: Näset och Ekorrvägen (pdf)", L_NASET),
    ("Lidingö stad – Kulturmiljöprogram del 1: handbok för fastighetsägare (pdf)", L_DEL1),
    ("Lidingö stad – Ändrade lagar och regler för byggande", L_NYA),
    ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet", L_FAQ),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Behöver verandan eller trappan lagas?", "Berätta om huset så kommer vi ut på Lidingö och tittar, "
          "utan kostnad."),
  "img": [("Faluröd stuga med vit spröjsad glasveranda och trätrappa i Grönstakolonin på Lidingö",
           "small falu red wooden cottage with white small-paned glazed veranda, simple wooden outdoor steps, "
           "green window shutters, tiled gable roof, low wooden picket fence with a small gate, lilac bushes, "
           "rocky slope by a bay, Lidingö Stockholm archipelago, summer, no people, no text"),
          ("Entrédörr i liggande ekpanel i en indragen nisch vid ett radhus",
           "close-up of a 1960s Scandinavian terraced house entrance recessed in a niche, front door clad with "
           "horizontal oak boards, white rendered wall, freshly restored woodwork, no people, no hands, no text")],
  "related": [("malare-lidingo.html", "Målare på Lidingö", "Panel, puts och slamfärg."),
              ("byggforetag-lidingo.html", "Byggföretag på Lidingö", "Tillbyggnad och större projekt."),
              ("koksrenovering-lidingo.html", "Köksrenovering på Lidingö", "Kök i villor och radhus.")],
},

# ---------------------------------------------------------------- DANDERYD
"snickare-danderyd.html": {
  "kind": "district", "service": "snickare", "ort": "Danderyd", "svc_label": "Snickare",
  "title": "Snickare i Danderyd – altan, staket och carport",
  "description": "Snickare i Danderyd: altaner, staket, grindar och carport enligt kommunens riktlinjer "
                 "från 2024, lovplikt i värdefulla områden och ROT för arbetet.",
  "h1": "Snickare i Danderyd",
  "lead": "I Danderyd gäller kommunens riktlinjer för kulturmiljöer inte bara huset utan också det som "
          "byggs runt det: altandäck, skärmtak, staket, grindar och carport. I de värdefulla områdena krävs "
          "dessutom bygglov för åtgärder som annars är lovfria. Vi utgår från riktlinjerna och från hur "
          "tomten möter gatan.",
  "card": "Altaner, staket och carport.",
  "sections": [
    {"id": "gatan", "anchor": "Riktlinjerna",
     "h2": "Det som syns från gatan väger tyngst",
     "paras": [
       "Miljö- och stadsbyggnadsnämnden beslutade om " + ext(D_RIKT, "riktlinjerna för kulturmiljöhistoriska "
       "byggnader och miljöer") + " den 11 december 2024. Område efter område – egnahemmen i Enebyberg, de "
       "tidiga villastäderna Ösby och Djursholm, villastäderna Stocksund och Mörby – återkommer samma råd: "
       "undvik stora altandäck, skärmtak och inglasade uteplatser och balkonger mot gatan, och håll häckar "
       "och staket mot gatan låga.",
       "Avskärmande plank bör enligt riktlinjerna bara sättas upp i bullerstörda områden. Garage och carport "
       "bör inte placeras mot gatan. För Stocksund och Mörby förklaras varför: förgårdens öppna rum mot "
       "gatan sluts, och ett dubbelgarage i tomtgräns blir en främmande volym i området.",
       "I kvarteret Yggdrasil går riktlinjerna längre och säger att en tillbyggnad i första hand ska göras "
       "så att den inte syns från gatan. För grupphusen i Djursholm ska tomten avgränsas med en låg häck "
       "eller ett staket, och den öppna förgårdsmarken bör inte bebyggas."],
     "aside": {"title": "Riktlinjernas råd för tomten",
               "items": ["Låga häckar och staket mot gatan",
                         "Plank bara vid buller",
                         "Altandäck och skärmtak inte mot gatan",
                         "Garage och carport inte mot gatan"]}},
    {"id": "staket",
     "h2": "Staket och grindar hör till helheten",
     "paras": [
       "I riktlinjernas allmänna råd till fastighetsägare står att trädgården är en viktig del av en "
       "värdefull miljö, och att detaljer som staket, murar och stenbelagda gångar kan ha ett högt "
       "kulturhistoriskt värde. För Djursholms tidiga villastad, kvarteret Yggdrasil och villastäderna i "
       "Stocksund och Mörby nämns staket, grindar och murar uttryckligen bland det som bör bevaras.",
       "Ett äldre spjälstaket med grind lagas därför helst: ruttna stolpfötter byts, spjälor kompletteras i "
       "samma bredd och avstånd och grindens beslag justeras. Enligt " + ext(BV_ALTAN, "Boverket") + " krävs "
       "inget bygglov för ett vanligt staket, som är lägre och glesare än ett plank. Ett tätt plank har "
       "egna regler.",
       "Ska något som omfattas av avståndsreglerna placeras närmare gatan än 4,5 meter kan kommunen lämna "
       "medgivande mot allmän plats, som gata, park eller naturområde. Placeringen får inte hindra drift och "
       "underhåll eller försämra sikten och trafiksäkerheten, och till förfrågan ska en skalenlig "
       "situationsplan med mått till fastighetsgränsen bifogas."],
     "aside": None},
    {"id": "altan",
     "h2": "Altan, plank och mur – och var lovplikten gäller ändå",
     "paras": [
       "Kommunens sida om " + ext(D_NYA, "nya regler för bygglov") + " anger att altaner, plank och murar "
       "inom 3,6 meter från ett en- eller tvåbostadshus får byggas utan lov upp till 1,8 meter, och längre "
       "bort upp till 1,2 meter. Men ligger fastigheten inom ett kulturhistoriskt särskilt värdefullt område, "
       "eller är byggnaden själv särskilt värdefull, krävs bygglov. Samma lovplikt gäller i områden som är "
       "riksintresse för kulturmiljövården.",
       "Riktlinjerna uppmanar fastighetsägare att söka på sin adress i Kulturmiljökartan för att se om "
       "fastigheten är utpekad. De påminner också om att den som gör ingrepp i marken eller bygger till "
       "själv ansvarar för att ta reda på om det finns fornlämningar på platsen, och att frågor om det ställs "
       "till länsstyrelsens kulturmiljöenhet.",
       "Murar och plank högre än 1,2 meter ska stå minst 4,5 meter från tomtgränsen. Närmare krävs "
       "skriftligt medgivande från samtliga berörda grannar, och kommunen påpekar att detaljplanen ibland "
       "hindrar en placering även när grannen säger ja."],
     "aside": {"title": "Bygglov krävs trots undantagen om",
               "items": ["Fastigheten ligger i ett särskilt värdefullt område",
                         "Byggnaden är särskilt värdefull",
                         "Området är riksintresse för kulturmiljövården",
                         "Grannarnas skriftliga medgivande saknas"]}},
    {"id": "carport",
     "h2": "Uterum, carport och tillbyggnad",
     "paras": [
       "En " + a("tillbyggnad.html", "tillbyggnad") + " av ett en- eller tvåbostadshus kräver bygglov när "
       "den sammanlagda ytan blir större än 30 kvadratmeter, och tidigare skärmtak och "
       "attefallstillbyggnader räknas in. För fristående förråd, garage och gäststugor gäller att ytan "
       "tillsammans inte får överstiga 45 kvadratmeter och en enskild byggnad 30 kvadratmeter, med högst 4 "
       "meter till nock. Berörs husets konstruktion krävs anmälan och startbesked.",
       "Riktlinjerna säger att tillägg ska utgå från omgivande bebyggelse i placering, utformning och "
       "volymverkan. För en carport betyder det oftast ett läge vid sidan av eller bakom huset. Byggs "
       "carporten ihop med huset påverkar det också rotavdraget, se nedan.",
       "Ska köket byggas ut samtidigt som altanen görs om kan arbetena samordnas med " +
       a("koksrenovering-danderyd.html", "köksrenoveringen i Danderyd") + "."],
     "aside": None}],
  "steps_h2": "Arbetsgång för snickeri i Danderyd",
  "steps": [
    ("Kulturmiljökartan", "Vi kontrollerar om fastigheten ligger i ett utpekat område och vilka av "
     "riktlinjernas råd som gäller där."),
    ("Tomten mot gatan", "På plats tittar vi på förgård, staket och grindar och på var en altan eller "
     "carport kan placeras."),
    ("Grannar och gränser", "Hamnar något närmare tomtgräns än 4,5 meter tar vi fram en situationsplan för "
     "grannarnas eller kommunens medgivande."),
    ("Förslag och ansökan", "Du får ett skriftligt förslag och, vid lovplikt, underlag för ansökan."),
    ("Bygge", "Stolpar, stomme och virke anpassas till befintliga staket, grindar och husets detaljer."),
    ("Genomgång", "Vi går igenom resultatet med dig på tomten och lämnar en sammanställning.")],
  "rot_h2": "ROT i Danderyd – carport ja, staket nej",
  "rot": [
    "Ett staket ger inget rotavdrag, enligt " + ext(SKV_ARB, "Skatteverkets") + " genomgång av vilka arbeten "
    "som räknas. En altan eller balkong som är ihopbyggd med huset gör det, liksom en carport eller ett "
    "garage som byggs till huset, om minst 75 procent av väggen är gemensam eller det finns en dörr "
    "emellan. En fristående carport ger inget avdrag.",
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "ihop med rut. Material och resor ingår inte. För tillbyggnad krävs att det har gått fem år efter "
    "husets värdeår. Vi gör avdraget direkt på fakturan."],
  "price_h2": "Kostnaden beror på",
  "price": [
    "Staketets längd, om grindar och stolpar ska tillverkas efter förlaga, altanens storlek och höjd och om "
    "arbetet kräver bygglov påverkar mest. Att laga ett äldre spjälstaket med grind är ett annat uppdrag "
    "än en ny altan på baksidan av ett grupphus. Platsbesöket är gratis, och därefter får du ett "
    "skriftligt kostnadsförslag."],
  "faq": [
    ("Hur högt får staketet mot gatan vara i Djursholm?",
     "Riktlinjerna anger ingen höjd men råder att häckar och staket mot gatan hålls låga. Ett vanligt "
     "staket kräver inte bygglov, men ett tätt plank har egna regler och kräver lov i värdefulla områden."),
    ("Kan kommunen ge medgivande om carporten ska stå nära gatan i Danderyd?",
     "Kommunen kan lämna medgivande för placering närmare än 4,5 meter mot gata eller park, om sikt och "
     "trafiksäkerhet inte försämras. Riktlinjerna avråder dock från carport och garage mot gatan."),
    ("Behöver vi bygglov för en altan i Stocksunds villastad?",
     "Ligger fastigheten inom det särskilt värdefulla området krävs bygglov även för en altan som annars "
     "vore lovfri. Riktlinjerna råder dessutom att stora altandäck inte läggs mot gatan."),
    ("Vem ansvarar för fornlämningar om vi bygger till i Danderyd?",
     "Byggherren, alltså du som fastighetsägare. Riktlinjerna säger att det är ditt ansvar att ta reda på "
     "om det finns fornlämningar, och att frågor ställs till länsstyrelsens kulturmiljöenhet."),
    ("Ger det rotavdrag att bygga en carport vid villan i Danderyd?",
     "Bara om den byggs ihop med huset, med minst 75 procent gemensam vägg eller en dörr emellan. En "
     "fristående carport ger inget avdrag.")],
  "sources": [
    ("Danderyds kommun – Riktlinjer för kulturmiljöhistoriska byggnader och miljöer 2024 (pdf)", D_RIKT),
    ("Danderyds kommun – Nya regler för bygglov från 1 december 2025", D_NYA),
    ("Boverket – Mur, plank, altan och annat", BV_ALTAN),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska staketet, grinden eller altanen göras om?", "Berätta om tomten så kommer vi ut till Danderyd och "
          "tittar – utan kostnad."),
  "img": [("Vit trävilla bakom ett lågt spjälstaket med grind i Djursholm",
           "white painted early 1900s Swedish wooden villa with mullioned windows behind a low white picket "
           "fence with a wooden garden gate, gravel path, mature oak and fruit trees, Djursholm Danderyd, "
           "summer, no people, no text"),
          ("Nytt spjälstaket och grindstolpe i trä vid en äldre villa",
           "close-up of a newly built white painted wooden picket fence and gate post with simple shaped top, "
           "gravel path, garden of an old Swedish villa, carpentry just finished, no people, no hands, no text")],
  "related": [("malare-danderyd.html", "Målare i Danderyd", "Tidstypisk färgsättning."),
              ("koksrenovering-danderyd.html", "Köksrenovering i Danderyd", "Villor och köksutbyggnad."),
              ("badrumsrenovering-danderyd.html", "Badrumsrenovering i Danderyd", "Villor, ritningar och FTX.")],
},
}


# Korslänkar mellan v3-sidorna (golv/snickare/fasad) på samma ort.
_V3 = {"golvlaggare": ("Golvläggare", "Nya golv och slipning.", "bromma nacka solna taby lidingo huddinge"),
       "snickare": ("Snickare", "Altan, dörrar och snickerier.", "bromma solna huddinge sollentuna lidingo danderyd"),
       "fasadrenovering": ("Fasadrenovering", "Panel, puts och isolering.", "bromma nacka taby huddinge sollentuna lidingo")}
for _f, _d in PAGES_TJ.items():
    _pre, _o = _f[:-5].split("-", 1)
    _pa = "på" if _d["ort"] in ("Lidingö", "Södermalm", "Värmdö") else "i"
    for _k, (_lbl, _txt, _orter) in _V3.items():
        if _k != _pre and _o in _orter.split():
            _d.setdefault("related", []).append((f"{_k}-{_o}.html", f"{_lbl} {_pa} {_d['ort']}", _txt))
