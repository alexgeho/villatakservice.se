# -*- coding: utf-8 -*-
"""Ortsidor för snickare (tjänster v1, 2026-10-25): Nacka, Södermalm, Tyresö, Täby, Norrtälje.
Schema: se tools/tj_check.py. Fakta endast från källorna i respektive sidas "sources"
(öppnade 2026-10-25). Inga priser, case, cert eller garantier utöver lag."""

L = 'class="text-link"'
BV_ALTAN = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/mur-plank-altan-och-annat/"
BV_TILLB = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/gora-en-tillbyggnad/"
BV_BAR = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/ingrepp-i-husets-barande-delar/"
BV_FASAD = "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/"
BV_LISTA = "https://www.boverket.se/sv/samhallsplanering/uppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/"
SKV_ROT = "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html"
SKV_ARB = "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html"
BRL = "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/"

NACKA_JVG = "https://www.nacka.se/499626/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-jarnvagen.pdf"
NACKA_SOM = "https://www.nacka.se/499628/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-sommarnojen.pdf"
NACKA_FAS = "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/lovfria-atgarder/fasadandringar/"
NACKA_PBL = "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/nyheter-om-nya-lagandringen/2025/10/nya-pbl-regler-ger-mer-frihet-och-storre-ansvar-for-nackas-fastighetsagare/"
TYR_PBL = "https://www.tyreso.se/boende--miljo/bygga/bygga-riva-eller-andra/forandringar-i-plan--och-bygglagen-fran-1-december-2025.html"
TYR_SLM = "https://insynsverige.se/documentHandler.ashx?did=20437"
TABY_KM = "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"
TABY_FAS = "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/fasadandring"
NT_LOV = "https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/lovbefriade-atgarder/"
NT_STR = "https://www.norrtalje.se/sjalvservice/bygga-bo-miljo/strandskyddsdispens/"
NT_FAKTA = "https://www.norrtalje.se/info/bygga-bo-miljo/norrtalje-vaxer/landsbygd-skargard/fakta-och-statistik/"
SCB_FRIT = "https://www.scb.se/hitta-statistik/artiklar/2026/fritidshus-vart-finns-de/"
SSM_INV = ("https://stockholmskallan.stockholm.se/postfiles/KUL/"
           "SSM_Sodermalm__Sodra_Maria,_del_av_Hogalid__1978_00.pdf")
SR_KLASS = ("https://skonhetsradet.stockholm/wp-content/uploads/sites/16/2026/03/"
            "Signerad-Oklassificerade-byggnader-i-nya-detaljplanerSR-2025_234-4.1-0.pdf")
NACKA_ALTA = ("https://www.nacka.se/49b6e2/globalassets/uppleva-gora/bilder/kultur/kulturhistoria/"
              "kulturpromenader/vandring-alta.pdf")


def a(href, text):
    return f'<a {L} href="{href}">{text}</a>'


def ext(href, text):
    return f'<a {L} href="{href}" rel="noopener">{text}</a>'


PAGES_TJ = {

# ---------------------------------------------------------------- NACKA
"snickare-nacka.html": {
  "kind": "district", "service": "snickare", "ort": "Nacka", "svc_label": "Snickare",
  "title": "Snickare i Nacka – verandor, panel och altaner",
  "description": "Snickare i Nacka: verandor och lövsågerier i Saltsjöbaden och Boo, altaner mot "
                 "baksidan, inredning i Ältas radhus. Lovregler från 1 december 2025 och ROT.",
  "h1": "Snickare i Nacka",
  "lead": "Som snickare i Nacka arbetar man med tre helt olika sorters hus: panelvillor längs "
          "Saltsjöbanan, sommarvillor med verandor vid farleden i Boo och radhus i Älta. Vi lagar "
          "och bygger nytt i trä – verandor, panel, foder, altaner, väggar och förvaring – och "
          "kontrollerar först vad kommunens kulturmiljökarta och detaljplanen säger om just din tomt.",
  "card": "Verandor, panel och altaner.",
  "sections": [
    {"id": "hus", "anchor": "Husen i Nacka",
     "h2": "Panelarkitektur, sommarnöjen och radhuslängor",
     "paras": [
       "De så kallade Sjuvillorna i Saltsjöbaden byggdes 1896 efter ritningar av arkitekten Eric "
       "Lundroth och hör till ortens äldsta hus. Kommunens " + ext(NACKA_JVG, "kulturmiljöprogram "
       "för villasamhällena vid järnvägen") + " beskriver 1890-talets panelarkitektur som "
       "fantasirik och varierande, och på Neglingehalvön var samtliga 120 tomter sålda i början "
       "av 1900-talet.",
       "Vid farleden i Boo är det sommarnöjena som präglar snickeriet. Enligt " + ext(NACKA_SOM,
       "programmet för sommarnöjena") + " massproducerade ångsågarna hyvlat virke och "
       "snickeridetaljer, och vissa snickerifabriker tillverkade hela hus som skeppades ut till "
       "tomterna. Schweizervillorna fick långt utskjutande tak, lövsågningsornament och "
       "verandor. Efter sekelskiftet blev foder och detaljer stramare, och från 1930-talet kom "
       "funkisbetonade stugor med ospröjsade fönster.",
       "Älta började som egnahems- och sommarstugeort, och enligt kommunens " + ext(NACKA_ALTA, "kulturvandring i Älta") +
       " byggdes det första radhusområdet, 25 radhus söder om Erstaviksvägen, 1968–1969. Där handlar snickeriet mer om planlösning, förvaring och uteplatser "
       "än om ornament."],
     "aside": {"title": "Vad husen brukar behöva",
               "items": ["Saltsjöbaden, Neglinge: foder, panel och entréer",
                         "Boo: verandor, räcken och lövsågerier",
                         "Solsidan, Storängen: fönster- och dörrsnickerier",
                         "Älta: väggar, förvaring och altan"]}},
    {"id": "veranda",
     "h2": "Verandor, räcken och foder på sekelskiftesvillorna",
     "paras": [
       "En veranda på en sommarvilla från 1880-talet har ofta lagats många gånger med virke som "
       "inte riktigt passar. Vi tar ner det som är ruttet, mäter upp de ursprungliga profilerna "
       "och tillverkar nya stolpar, räcken, foder och lövsågade detaljer efter dem. På Eolsudde "
       "noterar kommunens program att en av de större schweizervillornas veranda fortfarande är "
       "öppen, medan andra tidigt glasades in.",
       "Kulturmiljöprogrammen ger samma råd för både villastäderna och sommarnöjena: respektera "
       "husens proportioner, fasadfärg och tak samt detaljer som fönster, panel, utsmyckningar, "
       "entréer och räcken. För ett snickeriarbete betyder det att ny panel ska ha samma profil "
       "och dimension som den gamla, att foder och knutbrädor byts bit för bit i stället för i "
       "klump, och att entrépartiet lagas hellre än ersätts med en standarddörr.",
       "Är målningen också sliten samordnar vi gärna snickeri och " + a("malare.html", "målning") +
       " i samma etapp, så att träet hinner grundas innan det står ute en vinter."],
     "aside": None},
    {"id": "altan",
     "h2": "Altan och tillbyggnad – helst mot baksidan",
     "paras": [
       "För villorna längs Saltsjöbanan skriver kommunen att tillbyggnader ska underordnas "
       "huvudbyggnaden i placering, höjd och volym, och att takkupor, terrasser, balkonger och "
       "altaner helst ska läggas mot baksidan. Programmet avråder också från stora utfyllnader, "
       "stödmurar och hårdgjorda ytor. På en bergig tomt i Solsidan eller Saltsjö-Duvnäs är en "
       "altan på plintar som följer terrängen därför ofta lättare att få att passa in än ett "
       "högt trädäck på en gjuten mur.",
       "Själva altanen kräver normalt inget bygglov inom detaljplan så länge den håller sig under "
       "1,8 meter över marken inom 3,6 meter från huset, eller 1,2 meter längre ut, enligt " + ext(BV_ALTAN,
       "Boverket") + ". Ska den få tak och väggar blir det en " + a("tillbyggnad.html",
       "tillbyggnad") + ", och då räknas tidigare lovfria tillbyggnader och skärmtak in i de 30 "
       "kvadratmeter som får byggas till utan lov."],
     "aside": None},
    {"id": "lov",
     "h2": "Vad Nacka kommun kräver sedan 1 december 2025",
     "paras": [
       "Nacka kommun skriver på sin sida om " + ext(NACKA_FAS, "fasadändringar") + " att nya "
       "fönster och dörrar, ändringar av befintliga, balkonger och mindre takkupor räknas som "
       "fasadändringar. På ett en- eller tvåbostadshus inom detaljplan krävs inte längre bygglov "
       "för dem, men åtgärden får inte strida mot detaljplanen. Ingrepp i den bärande "
       "konstruktionen kräver en anmälan.",
       "Ligger fastigheten i ett område som kommunen bedömt som särskilt värdefullt enligt 8 kap. "
       "13 § PBL krävs lov för samtliga fasadändringar som påverkar områdets karaktär eller "
       "husets yttre. I " + ext(NACKA_PBL, "kommunens genomgång av de nya PBL-reglerna") +
       " nämns att även en friggebod då kräver lov.",
       "Ett råd från kommunens kundrådgivare är att prata med grannarna tidigt. Många "
       "tillsynsanmälningar kommer från grannar som inte visste vad som skulle byggas, och "
       "eftersom kommunen inte längre granskar många lovfria åtgärder i förväg ligger ansvaret "
       "på fastighetsägaren."],
     "aside": {"title": "Före beställning",
               "items": ["Sök fastigheten i Nackas webbkarta",
                         "Läs detaljplanen för tomten",
                         "Påverkas något bärande? Då krävs anmälan",
                         "Berätta för grannarna vad som ska byggas"]}},
    {"id": "radhus",
     "h2": "Inredningssnickeri i Ältas radhus",
     "paras": [
       "I ett radhus från slutet av 1960-talet är ytan given, så snickeriet handlar om att få ut "
       "mer av den: en vägg som flyttas för att ge ett extra sovrum, en trappa som byggs om, "
       "platsbyggda garderober under snedtak eller en bänk med förvaring i hallen. Innan en vägg "
       "rivs tar vi reda på om den är bärande – är den det behövs en konstruktör, en anmälan och "
       "startbesked innan arbetet börjar, enligt " + ext(BV_BAR, "Boverket") + ".",
       "Har samfälligheten egna riktlinjer för altaner, plank och förråd följer vi dem, så att "
       "längan behåller sitt uttryck. Ligger altanen närmare tomtgränsen än 4,5 meter behövs "
       "dessutom grannens skriftliga medgivande för att slippa bygglov."],
     "aside": None}],
  "steps_h2": "Så lägger vi upp ett snickeriarbete i Nacka",
  "steps": [
    ("Karta och plan först", "Vi slår upp fastigheten i kommunens webbkarta och läser detaljplanen, "
     "så att du vet om arbetet är lovfritt eller kräver lov eller anmälan."),
    ("Platsbesök", "Vi tittar på husets epok, mäter upp profiler på panel, foder och räcken och "
     "noterar fukt och röta."),
    ("Förslag i husets stil", "Du får ett skriftligt förslag där nytt virke och nya detaljer matchar "
     "det som finns, eller en enkel modern lösning när det passar bättre."),
    ("Material och tillverkning", "Specialprofiler och lövsågade delar tas fram i förväg, så att "
     "huset står öppet så kort tid som möjligt."),
    ("Utförande", "Vi byter och bygger etappvis och samordnar med målare, elektriker eller VVS när "
     "det behövs."),
    ("Genomgång", "Vi går igenom arbetet med dig och lämnar en sammanställning av vad som är gjort.")],
  "rot_h2": "ROT för snickeri på villan eller sommarhuset",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och rot och "
    "rut får tillsammans vara högst 75 000 kr. Material och resor ger inget avdrag. Vi drar av "
    "beloppet direkt på fakturan.",
    "Enligt " + ext(SKV_ARB, "Skatteverket") + " ger det avdrag att bygga en altan som sitter ihop "
    "med huset och att reparera fasaden, men inte att bygga en fristående friggebod. Ett "
    "sommarhus i Boo som du äger och använder räknas också. För om- och tillbyggnad gäller att "
    "huset ska vara äldre än fem år räknat från värdeåret."],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "Mest betyder hur mycket av det gamla som går att spara, om profiler och ornament måste "
    "specialtillverkas, hur tomten lutar och hur långt materialet ska bäras. En rak altan på plan "
    "mark i Älta är ett annat jobb än en veranda med lövsågerier på en sluttning i Boo. Efter ett "
    "kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag."],
  "faq": [
    ("Får jag glasa in verandan på min sommarvilla i Boo?",
     "Det beror på om villan ligger inom ett område som kommunen pekat ut som särskilt värdefullt. "
     "Där krävs lov för ändringar som påverkar husets yttre, och en inglasning gör det. "
     "Utanför sådana områden kan den vara lovfri på ett en- eller tvåbostadshus, men den får inte "
     "strida mot detaljplanen och ska göras varsamt. Hur just din inglasning bedöms kan "
     "Stadsbyggnadsservice svara på innan du beställer."),
    ("Kan ni tillverka lövsågade detaljer som matchar de gamla?",
     "Ja. Vi tar mall från en hel detalj eller från gamla foton och låter tillverka nya i samma "
     "form och dimension, så att lagningen inte syns på håll."),
    ("Varför rekommenderar kommunen att altanen läggs på baksidan?",
     "Kulturmiljöprogrammet för villasamhällena vid järnvägen vill att gatubilden behålls. En "
     "altan mot baksidan påverkar inte husets fasad mot gatan, och det gör den lättare att få "
     "att passa in."),
    ("Vår vägg i radhuset i Älta – kan den rivas utan anmälan?",
     "Om väggen inte bär och ingreppet inte påverkar de bärande delarna väsentligt krävs ingen "
     "anmälan. Är den bärande behöver en konstruktör räkna på en ersättning, och då krävs anmälan "
     "och startbesked innan rivningen."),
    ("Kartan visar ingen kulturmiljö för vår villa i Björknäs – betyder det att allt är fritt?",
     "Inte säkert. Kommunen skriver att kulturmiljölagret håller på att uppdateras och att det "
     "inte tänds för vissa utpekade delar av Björknäs–Eknäs. Fråga Stadsbyggnadsservice innan du "
     "ändrar fasad, fönster eller entré.")],
  "sources": [
    ("Nacka kommun – Kulturmiljöprogram: Villasamhällen vid järnvägen", NACKA_JVG),
    ("Nacka kommun – Kulturmiljöprogram: Sommarnöjen vid farleden", NACKA_SOM),
    ("Nacka kommun – Kulturvandring i Älta", NACKA_ALTA),
    ("Nacka kommun – Fasadändringar", NACKA_FAS),
    ("Nacka kommun – Nya PBL-regler ger mer frihet och större ansvar för Nackas fastighetsägare", NACKA_PBL),
    ("Boverket – Mur, plank, altan och annat", BV_ALTAN),
    ("Boverket – Göra en tillbyggnad", BV_TILLB),
    ("Boverket – Ingrepp i husets bärande delar", BV_BAR),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska verandan eller altanen göras om?", "Berätta om huset så bokar vi ett kostnadsfritt "
          "platsbesök i Nacka."),
  "img": [("Ljusmålad schweizervilla med veranda och lövsågerier vid vattnet i Boo, Nacka",
           "light painted 1880s Swiss-style wooden summer villa with open veranda, fretwork "
           "ornaments and long roof overhangs, pine trees and rocky shore, Baltic archipelago, Nacka"),
          ("Nytillverkade verandastolpar och räcke i trä mot en äldre panelvägg",
           "close-up of newly crafted white painted wooden veranda posts and railing with fretwork "
           "details next to old painted wooden panel facade, carpentry repair, summer light")],
},

# ---------------------------------------------------------------- SÖDERMALM
"snickare-sodermalm.html": {
  "kind": "district", "service": "snickare", "ort": "Södermalm", "svc_label": "Snickare",
  "title": "Snickare på Södermalm – snickeri i lägenheten",
  "description": "Snickare på Södermalm: innerväggar, dörrar, listverk och platsbyggd förvaring i "
                 "bostadsrätt. Styrelsens tillstånd, fasadregler och ROT i lägenheten.",
  "h1": "Snickare på Södermalm",
  "lead": "En snickare på Södermalm arbetar oftast inomhus: nya eller flyttade innerväggar, "
          "dörrar och karmar, listverk och platsbyggda garderober i lägenheter från 1880-talets "
          "hyreshus till 1930-talets lamellhus. I en bostadsrätt behövs ofta styrelsens tillstånd, och "
          "det tar vi med i planeringen från början.",
  "card": "Väggar, dörrar och förvaring i lägenhet.",
  "sections": [
    {"id": "kvarter", "anchor": "Husen på Söder",
     "h2": "Från 1880-talets hyreshus till 1930-talets lamellhus",
     "paras": [
       "Stadsmuseets " + ext(SSM_INV, "byggnadsinventering av Södra Maria och del av Högalid") +
       " beskriver hur Södermalm förändrades när stadsplanerna efter Albert Lindhagens kommitté "
       "fastställdes kring 1880. Då förnyades bostadsbeståndet snabbt, och det som byggdes var "
       "nästan uteslutande hyreshus. Många av de nya invånarna var arbetare, och de som inte hade "
       "råd med hyrorna i de nya husen bodde kvar i gårdshus och trähus i områdets utkanter.",
       "På 1920-talet byggdes fortfarande slutna kvarter, men gårdarna började öppnas till så "
       "kallade storgårdskvarter, och stilen präglades av 20-talsklassicismen. På 1930-talet kom "
       "de friliggande lamellhusen på bergstomter som tidigare ansetts svåra att bebygga. Under "
       "1920- och 1930-talen byggdes enligt inventeringen nästan bara lägenheter på ett rum och "
       "kök eller ett rum med pentry.",
       "Inventeringen noterar också att inredningen i de flesta äldre lägenheter består av "
       "profilerade standardsnickerier, taklister i stuck och kakelugnar. För en snickare betyder "
       "det att samma uppdrag ser olika ut beroende på huset: i ett sekelskifteshus är dörrar, "
       "foder och lister värda att laga och kopiera, och en vägg som ser lätt ut kan ändå vara "
       "bärande. I en liten 30-talslägenhet handlar det oftare om att få plats med förvaring."],
     "aside": {"title": "Epoker på Söder",
               "items": ["Kring 1880: nya stadsplaner, snabb förnyelse",
                         "1880–1900: hyreshus i slutna kvarter",
                         "1920-talet: storgårdskvarter och 20-talsklassicism",
                         "1930-talet: lamellhus på bergstomterna"]}},
    {"id": "brf",
     "h2": "Styrelsens tillstånd enligt bostadsrättslagen",
     "paras": [
       "Enligt 7 kap. 7 § " + ext(BRL, "bostadsrättslagen") + " får du inte utan styrelsens "
       "tillstånd göra ingrepp i en bärande konstruktion, ändra ledningar för avlopp, värme, gas "
       "eller vatten, ändra ventilation, eldstad eller rökkanal eller påverka brandskyddet. Samma "
       "sak gäller annan väsentlig förändring av lägenheten. Har lägenheten särskilda historiska "
       "eller kulturhistoriska värden krävs tillstånd för varje åtgärd som påverkar dem.",
       "Styrelsen får säga nej bara om åtgärden är till påtaglig skada eller olägenhet för "
       "föreningen, och tillståndet kan förenas med villkor. Den som är missnöjd kan begära att "
       "hyresnämnden prövar frågan. Föreningens stadgar avgör dessutom vad du själv ansvarar för "
       "att underhålla, så läs dem innan du beställer.",
       "I praktiken lönar det sig att skicka en enkel ritning och en beskrivning till styrelsen "
       "innan arbetet bokas. Vi tar fram underlaget: vilka väggar som berörs, hur de byggs och om "
       "något bärande eller brandskyddet påverkas."],
     "aside": {"title": "Tillstånd behövs bland annat för",
               "items": ["Ingrepp i bärande vägg eller bjälklag",
                         "Flyttad ventilation eller rökkanal",
                         "Ändrat brandskydd, t.ex. ny dörr mot trapphuset",
                         "Annan väsentlig förändring av planlösningen"]}},
    {"id": "inredning",
     "h2": "Väggar, dörrar, listverk och förvaring",
     "paras": [
       "En ny innervägg i en lägenhet byggs med reglar, ljudisolering och skivor och får dörr, "
       "foder och lister som matchar resten av lägenheten. Att riva en vägg som inte bär kräver "
       "enligt " + ext(BV_BAR, "Boverket") + " ingen anmälan, men påverkas de bärande delarna "
       "väsentligt ska anmälan göras och startbesked finnas innan arbetet börjar. I äldre stenhus "
       "är det därför klokt att låta en konstruktör titta på ritningarna först.",
       "I lägenheter från sekelskiftet är listverket ofta det som binder ihop rummen. När en vägg "
       "flyttas eller en dörröppning sätts igen kompletterar vi golvlister, foder och taklister "
       "med samma profil, så att ändringen inte syns. Gamla innerdörrar går ofta att justera och "
       "renovera i stället för att bytas.",
       "Platsbyggd förvaring är det vanligaste önskemålet: garderober i nischer, bokhyllor kring "
       "en dörr, bänkar i ett burspråk eller skåp under en sovloftstrappa. Ska samtidigt köket "
       "eller golven göras om samordnar vi det med " + a("koksrenovering.html",
       "köksrenoveringen") + " och " + a("golvlaggning.html", "golvläggningen") + "."],
     "aside": None},
    {"id": "fasad",
     "h2": "Fönster, balkong och trapphus är föreningens fråga",
     "paras": [
       "Ytterfönster, balkonger och fasad hör till huset, inte till lägenheten. Enligt reglerna "
       "från 1 december 2025 behövs bygglov för fasadändringar på ett flerbostadshus inom detaljplan när ändringen "
       "görs på en fasad eller ett tak som vetter mot allmän plats, till exempel en gata, ett torg "
       "eller en park, enligt " + ext(BV_FASAD, "Boverkets PBL kunskapsbank") + ". Mot gården kan "
       "samma ändring vara lovfri, om inte detaljplanen eller ett särskilt värdefullt område ger "
       "utökad lovplikt, men det är föreningen som beslutar och söker.",
       "Stadsmuseet har klassificerat bebyggelsen i innerstaden i blått, grönt och gult efter hur "
       "höga kulturhistoriska värden den har. Enligt " + ext(SR_KLASS, "Skönhetsrådet") + " är "
       "grundprincipen att blå- och grönklassade byggnader remitteras till Stadsmuseet och "
       "Skönhetsrådet när bygglov söks. Rör ett arbete trapphus, entréportar eller fönster i ett sådant hus bör "
       "föreningen ta reda på husets klassning innan något beställs.",
       "Inne i lägenheten är det annorlunda. Arbete på insidan av befintliga fönster ger enligt "
       "Skatteverket rotavdrag i bostadsrätt, men vad du själv får göra med fönstren framgår av "
       "föreningens stadgar."],
     "aside": None},
    {"id": "logistik",
     "h2": "Arbete i ett bebott hus",
     "paras": [
       "Ett snickeriarbete på femte våningen utan rymlig hiss kräver planering. Skivor och virke "
       "beställs i längder som går att bära upp i trapphuset, kapning görs så långt det går inne i "
       "lägenheten och trapphuset skyddas där materialet bärs. Leveranser bokas till tider då "
       "bilen kan stå nära porten.",
       "Enligt 7 kap. 9 § bostadsrättslagen ska du rätta dig efter de särskilda regler som "
       "föreningen meddelar. Många föreningar har regler om tider för bullrande arbeten och om var "
       "byggavfall får ställas. Vi går igenom dem med dig innan start och anpassar arbetsdagarna "
       "efter dem."],
     "aside": None}],
  "steps_h2": "Från idé till färdig lägenhet",
  "steps": [
    ("Besök och mätning", "Vi mäter upp lägenheten, ser vilka väggar som kan vara bärande och "
     "noterar vilka originalsnickerier som finns kvar."),
    ("Underlag till styrelsen", "Du får en ritning och en beskrivning av arbetet att skicka till "
     "föreningen när tillstånd behövs."),
    ("Konstruktör vid behov", "Berörs något bärande tar en konstruktör fram lösningen, och anmälan "
     "lämnas till stadsbyggnadskontoret."),
    ("Planering av transporter", "Leveranser, bärning och skydd av trapphuset planeras efter huset "
     "och föreningens regler."),
    ("Snickeri på plats", "Väggar, dörrar, listverk och förvaring byggs i en ordning som håller "
     "lägenheten så användbar som möjligt."),
    ("Avslut", "Vi städar, går igenom resultatet med dig och lämnar en sammanställning till dig och "
     "föreningen.")],
  "rot_h2": "ROT i bostadsrätt – bara innanför väggarna",
  "rot": [
    "I en bostadsrätt ger enligt " + ext(SKV_ROT, "Skatteverket") + " bara arbete inne i "
    "bostaden rätt till rotavdrag. Skatteverkets " + ext(SKV_ARB, "lista över rotarbeten") +
    " nämner till exempel att riva innerväggar och ändra planlösningen, byta innerdörrar och "
    "montera platsbyggda garderober och bokhyllor. Att bygga om en balkong, glasa in den eller "
    "byta ytterdörr ger inget avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst "
    "75 000 kr tillsammans med rut. Äger ni lägenheten tillsammans kan ni båda använda ert "
    "utrymme, och vi drar av beloppet direkt på fakturan."],
  "price_h2": "Vad påverkar priset i en lägenhet?",
  "price": [
    "Det som styr mest är om något bärande berörs, hur mycket originalsnickeri som ska lagas eller "
    "kopieras, om förvaringen ska specialbyggas och hur lätt det är att få upp material i huset. "
    "Vi kommer gärna förbi utan kostnad och lämnar sedan ett skriftligt kostnadsförslag."],
  "faq": [
    ("Behöver jag styrelsens tillstånd för att bygga en ny innervägg i bostadsrätten?",
     "Om väggen ändrar planlösningen väsentligt, påverkar ventilation eller brandskydd eller innebär "
     "ingrepp i något bärande behövs tillstånd enligt bostadsrättslagen. En lätt vägg som bara delar ett "
     "stort rum kan vara en mindre ändring, men fråga styrelsen innan arbetet bokas."),
    ("Kan ni bygga ett sovloft i en lägenhet med hög takhöjd?",
     "Ja, om takhöjden räcker och bjälklaget klarar infästningen. Ett loft kan räknas som en "
     "väsentlig förändring, så räkna med att föreningen vill se ritningar innan det byggs."),
    ("Vem bestämmer om fönstren mot gatan i vårt hus på Söder?",
     "Föreningen. Ytterfönstren hör till huset, och mot en gata krävs bygglov för en fasadändring "
     "på ett flerbostadshus inom detaljplan. Vad du som medlem själv får göra med fönstren, "
     "till exempel på insidan, framgår av stadgarna."),
    ("Får jag rotavdrag för en platsbyggd garderob i min bostadsrätt?",
     "Ja. Skatteverket räknar montering av platsbyggda fasta möbler, som garderober och bokhyllor, "
     "till arbeten som ger rotavdrag i bostadsrätt. Själva skåpmaterialet ger inget avdrag."),
    ("Hur får ni upp långa skivor till en vindsvåning utan hiss?",
     "Vi beställer material i längder som går runt trapphusets vändplan och skarvar där det inte "
     "syns. Ibland går det att lyfta in material genom ett fönster, men det kräver föreningens "
     "godkännande.")],
  "sources": [
    ("Riksdagen – Bostadsrättslag (1991:614), 7 kap.", BRL),
    ("Boverket – Fasadändring (PBL kunskapsbanken)", BV_FASAD),
    ("Boverket – Ingrepp i husets bärande delar", BV_BAR),
    ("Boverket – Lista med PBL-ändringar 1 december 2025", BV_LISTA),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Stockholms stadsmuseum – Södermalm: Södra Maria, del av Högalid. Byggnadshistorisk "
     "inventering 1974–75 (Stockholmskällan)", SSM_INV),
    ("Skönhetsrådet, Stockholms stad – Oklassificerade byggnader i nya detaljplaner (2025)", SR_KLASS)],
  "cta": ("Planerar du om lägenheten?", "Berätta vad du vill ändra så kommer vi förbi och mäter "
          "upp – utan kostnad."),
  "img": [("Ljus lägenhet på Södermalm med platsbyggd bokhylla och vita innerdörrar",
           "bright turn-of-the-century Stockholm apartment interior, Södermalm, white panelled "
           "interior doors with moulded casings, built-in white bookcase around a doorway, "
           "herringbone oak floor, tall windows, no people"),
          ("Nyuppsatt innervägg med dörr och foder i en äldre stadslägenhet",
           "new interior partition wall with white panelled door and classic moulded casings and "
           "skirting boards in an older Stockholm city apartment, carpentry just finished, tools "
           "neatly on floor")],
},

# ---------------------------------------------------------------- TYRESÖ
"snickare-tyreso.html": {
  "kind": "district", "service": "snickare", "ort": "Tyresö", "svc_label": "Snickare",
  "title": "Snickare i Tyresö – stugor som blir helårshus",
  "description": "Snickare i Tyresö: panel, fönster, förstukvistar och altaner på fritidshus som "
                 "permanentas i Solberga och Raksta. Lovregler efter december 2025 och ROT.",
  "h1": "Snickare i Tyresö",
  "lead": "I Tyresö är det vanligaste snickeriuppdraget ett hus som började som sommarstuga och nu "
          "ska fungera året runt. Det kan gälla panel och fönster, en ny förstukvist, en altan "
          "mot skogen eller en tillbyggnad – och då behöver både husets historia och kommunens "
          "lovregler vägas in.",
  "card": "Stugor, altaner och tillbyggnader.",
  "sections": [
    {"id": "hus", "anchor": "Husen i Tyresö",
     "h2": "Från godsmark till fritidshus och villor",
     "paras": [
       "På 1600-talet sträckte sig Tyresögodset från dagens Bollmora till Dalarö. När godsägaren Claes Lagergren dog "
       "1930 började marken styckas, och i slutet av 1950-talet var nästan halva godset bebyggt "
       "med fritidshus, enligt ett " + ext(TYR_SLM, "kulturmiljöunderlag från Stockholms läns "
       "museum") + ". Solberga fick byggnadsplan 1952 och Raksta 1958.",
       "Underlaget beskriver ett välbevarat fritidshus från 1950-talet med röd stockpanel, gröna "
       "lister och foder och tvåkupigt tegeltak. Men samma underlag konstaterar att "
       "permanentningen pågår och att en del hus är helt ombyggda eller nybyggda. Fler har bosatt "
       "sig permanent i området, och den nya detaljplanen ska ge större byggrätter.",
       "För snickaren innebär det hus med flera lager: en ursprunglig stuga, en eller två "
       "tillbyggnader från olika årtionden och detaljer som bytts efter hand. Innan vi föreslår "
       "något tar vi reda på vilka delar som är original och vilka som är senare tillägg."],
     "aside": {"title": "Typiska hus",
               "items": ["1950-talsstugor med stock- eller locklistpanel",
                         "Stugor som byggts till i flera etapper",
                         "Äldre torp och arbetarbostäder från godstiden",
                         "Villor och fritidshus i Gamla Tyresö"]}},
    {"id": "stuga",
     "h2": "Panel, fönster och förstukvist när stugan blir bostad",
     "paras": [
       "Ett gott exempel på varsam ombyggnad finns i samma underlag: huvudbyggnaden på Solberga "
       "gård renoverades för att få permanentstandard med de gamla detaljerna kvar. Stommen och "
       "panelen lagades i nödvändig omfattning, förstukvisten och entrédörren tillverkades nya, "
       "och inne kompletterades foder och lister med samma utseende som de befintliga. Det är "
       "samma arbetssätt vi föreslår på en 1950-talsstuga.",
       "Konkret betyder det att rötskadad panel byts bit för bit mot ny i samma profil, att äldre "
       "fönsterbågar med sina beslag lagas och tätas när det går, och att nya fönster i en "
       "tillbyggnad väljs så att de inte bryter mot stugans. Är fönstren uttjänta kan du läsa mer "
       "om " + a("fonsterbyte.html", "fönsterbyte") + ".",
       "Inne handlar det ofta om att göra en sommarplanlösning beboelig året runt: en vägg som "
       "flyttas för att ge plats åt ett badrum, en ny trappa till vinden eller förvaring där det "
       "förut stod en kamin. Berör ändringen något bärande krävs anmälan innan arbetet börjar."],
     "aside": None},
    {"id": "altan",
     "h2": "Altan och veranda på skogstomten",
     "paras": [
       "Tomterna i Solberga och Raksta är i huvudsak stora, med husen inpassade i naturmark. En "
       "altan där byggs bäst på plintar som följer berget, med luft under trallen så att virket "
       "torkar efter regn under tallarna. Kulturmiljöunderlaget visar också att verandor har "
       "byggts till i efterhand, som på huset Telegrafen där en veranda mot vattnet tillkom 1994 "
       "med vitmålade utsågade dekorationer.",
       "Tyresö kommun skriver att en altan får byggas utan bygglov upp till 1,8 meter över marken "
       "inom 3,6 meter från huset och upp till 1,2 meter längre ut. Får altanen tak blir den en "
       "tillbyggnad, och för ett en- eller tvåbostadshus krävs lov när tillbyggnaderna "
       "sammanlagt blir större än 30 kvadratmeter. Då räknas tidigare skärmtak och "
       "attefallstillbyggnader in. Läs mer om " + a("tillbyggnad.html", "tillbyggnad") + "."],
     "aside": {"title": "Räknas in i 30 m²",
               "items": ["Attefallstillbyggnad och attefallstakkupa", "Skärmtak",
                         "Altan, balkong eller burspråk enligt äldre regler",
                         "Den nya tillbyggnaden"]}},
    {"id": "lov",
     "h2": "Tyresö kommuns regler efter 1 december 2025",
     "paras": [
       "På sidan om " + ext(TYR_PBL, "förändringarna i plan- och bygglagen") + " skriver kommunen "
       "att ommålning, nytt tak och nya fönster inte kräver bygglov på ett en- eller "
       "tvåbostadshus. Undantaget är fastigheter i ett kulturhistoriskt särskilt värdefullt område "
       "och byggnader som själva är det – där krävs lov, även för altan, plank och mur. Sådana "
       "områden kan vara utpekade i översiktsplanen, i kulturmiljöprogrammet eller i "
       "detaljplanen, och kommunen ber dig höra av dig om du är osäker.",
       "Tyresö slott och kyrka med omgivande område är riksintresse för kulturmiljövården, och "
       "enligt underlaget ingår en del av planområdet Solberga/Raksta i riksintresset. Där kontrollerar vi planen extra noga innan något byggs utvändigt.",
       "Lovfritt betyder inte att kommunen granskar arbetet i förväg. Ansvaret för att reglerna "
       "följs ligger på dig som fastighetsägare, och den som vill ha ett säkert besked kan söka ett "
       "frivilligt bygglov."],
     "aside": None},
    {"id": "komplement",
     "h2": "Gäststuga, förråd och komplementbostadshus",
     "paras": [
       "Friggebod och attefallshus heter numera komplementbyggnad och komplementbostadshus. Inom "
       "detaljplan krävs lov om byggnaden blir större än 30 kvadratmeter eller högre än 4 meter "
       "till nock, och sammanlagt får de lovfria byggnaderna på tomten vara högst 45 "
       "kvadratmeter. Ska byggnaden få vatten och avlopp eller en eldstad krävs anmälan och "
       "startbesked, enligt kommunen.",
       "Vi bygger stomme, panel, fönster och inredning och samordnar installationerna. Mer om "
       "sådana hus finns på sidan om " + a("attefallshus.html", "attefallshus") + "."],
     "aside": None}],
  "steps_h2": "Så går ett snickeriuppdrag till i Tyresö",
  "steps": [
    ("Husets historia", "Vi tar reda på vilka delar som är ursprungliga och vilka som är senare "
     "tillbyggnader, gärna med hjälp av gamla ritningar."),
    ("Planläge och lov", "Vi kontrollerar om fastigheten ligger i ett omvandlingsområde eller ett "
     "kulturhistoriskt värdefullt område."),
    ("Besiktning", "Panel, syllar, fönster och bjälklag undersöks för fukt och röta, särskilt där "
     "olika husdelar möts."),
    ("Förslag och kostnad", "Du får ett skriftligt förslag där vi skiljer på vad som bör lagas och "
     "vad som lönar sig att byta."),
    ("Etablering i terrängen", "Material och avfall planeras efter berg, träd och smala vägar."),
    ("Bygge och genomgång", "Arbetet görs i etapper, och vi går igenom resultatet med dig på plats.")],
  "rot_h2": "ROT för snickeri på helårshus och fritidshus",
  "rot": [
    "Rotavdraget gäller både permanentbostad och fritidshus som du äger och använder. Det är 30 "
    "procent av arbetskostnaden, högst 50 000 kr per person och år, och rot och rut får "
    "tillsammans vara högst 75 000 kr. Vi drar av beloppet direkt på fakturan.",
    "Enligt " + ext(SKV_ARB, "Skatteverket") + " ger en tillbyggnad av bostadshuset rätt till avdrag, även "
    "ett förråd eller en gäststuga som byggs ihop med huset. Detsamma gäller en altan som byggs ihop med huset. Att bygga en ny "
    "fristående byggnad, till exempel en friggebod eller ett garage, ger däremot inget avdrag."],
  "price_h2": "Vad styr priset?",
  "price": [
    "Kostnaden beror mest på hur mycket röta som finns i panel och syllar, hur många husdelar och "
    "anslutningar huset har efter tidigare tillbyggnader, om detaljer måste specialtillverkas och "
    "hur lätt tomten är att arbeta på. Platsbesöket är kostnadsfritt, och du får ett skriftligt "
    "kostnadsförslag."],
  "faq": [
    ("Ska vi byta all panel på 1950-talsstugan eller laga den?",
     "Oftast räcker det att byta de skadade partierna, särskilt nertill och kring fönster. Ny "
     "panel i samma profil smälter in när den målats. Är det mesta ruttet kan ett helt byte löna "
     "sig, men det avgör vi efter besiktningen."),
    ("Räknas vår gamla attefallstillbyggnad in när vi bygger en ny altan med tak?",
     "Ja. Kommunen skriver att alla bygglovsbefriade tillbyggnader på huvudbyggnaden ska räknas "
     "ihop, även skärmtak och attefallstillbyggnader. Blir summan större än 30 kvadratmeter krävs "
     "bygglov."),
    ("Behöver vi bygglov för en altan i Solberga?",
     "Inte om altanen håller sig inom höjdmåtten och fastigheten inte ligger i ett kulturhistoriskt "
     "särskilt värdefullt område. Ligger huset nära slottsmiljön är det klokt att fråga kommunen "
     "först."),
    ("Kan ni tillverka en ny förstukvist som liknar den gamla?",
     "Ja. Vi mäter upp och fotograferar det som finns kvar, eller utgår från gamla bilder, och "
     "bygger en ny i samma form med foder och detaljer som passar huset."),
    ("Kan vi bo kvar i huset medan ni bygger om?",
     "Ofta ja, om arbetet delas upp i etapper. Vi planerar så att kök och badrum går att använda "
     "så länge som möjligt.")],
  "sources": [
    ("Tyresö kommun – Förändringar i plan- och bygglagen från 1 december 2025", TYR_PBL),
    ("Stockholms läns museum – Solberga/del av Raksta, kulturmiljöunderlag (2008:31)", TYR_SLM),
    ("Boverket – Göra en tillbyggnad", BV_TILLB),
    ("Boverket – Mur, plank, altan och annat", BV_ALTAN),
    ("Boverket – Ingrepp i husets bärande delar", BV_BAR),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Ska stugan bli helårshus?", "Beskriv huset så kommer vi ut till Tyresö och tittar – "
          "utan kostnad."),
  "img": [("Rödmålad 1950-talsstuga med stockpanel och gröna foder på en skogstomt i Tyresö",
           "1950s Swedish summer cottage with red log-style wooden cladding, green trim and window "
           "casings, double-curved clay tile roof, set among pine trees and granite outcrops, Tyresö"),
          ("Ny altan på plintar som följer berget vid en äldre stuga",
           "new pressure treated wooden deck on concrete piers following sloping granite rock "
           "beside an older red wooden cottage, pine forest, Stockholm archipelago")],
},

# ---------------------------------------------------------------- TÄBY
"snickare-taby.html": {
  "kind": "district", "service": "snickare", "ort": "Täby", "svc_label": "Snickare",
  "title": "Snickare i Täby – glasverandor, fönster och carport",
  "description": "Snickare i Täby: glasverandor och fönster i villastäderna vid Roslagsbanan, "
                 "altan och carport i grupphusområden. Kommunens riktlinjer, lov och ROT.",
  "h1": "Snickare i Täby",
  "lead": "Behöver du en snickare i Täby är huset troligen antingen en villa från villastädernas "
          "tid vid Roslagsbanan eller ett grupphus från 1960–80-talen. Vi lagar fönster, dörrar "
          "och glasverandor, bygger altaner och carportar och planerar om invändigt – med "
          "kommunens kulturmiljöriktlinjer som stöd för vad som passar huset.",
  "card": "Verandor, fönster och carport.",
  "sections": [
    {"id": "hus", "anchor": "Husen i Täby",
     "h2": "Villastad från 1907 och grupphus från 60-talet",
     "paras": [
       "Täby villastad vid kyrkbyn växte fram efter en avstyckningsplan från 1907, och Byle "
       "planerades samma år efter trädgårdsstadens ideal med stora tomter. Kommunens underlag "
       + ext(TABY_KM, "Kulturmiljöer i Täby") + " beskriver villorna från tidigt 1900-tal med "
       "branta, ofta brutna tak, och skriver att takkupor, förstukvistar, burspråk och glasverandor "
       "är vanliga och att fönstren ofta är spröjsade. Fasaderna har ofta liggande spontad panel, "
       "målad med Falu rödfärg eller i ljusa toner, med vita foder, vindskivor och knutar.",
       "I Näsbypark står villor från 1920–30-talen, bland annat en vitputsad villa från 1926 med "
       "mörkt gröna fönstersnickerier och en villa från 1939 med snidad entrédörr i mörkt trä. "
       "Efterkrigstiden gav grupphusen, där ett par hus från 1968 har tegel i bottenvåningen och "
       "träpanel under fönstren, och envåningshusen ofta har platt tak med brett panelat takband.",
       "Det är alltså stor skillnad på att byta en dörr i Byle och i ett 1970-talshus i Gribbylund. "
       "Därför börjar vi med husets byggår och ritningar, som kan finnas kvar hos kommunen."],
     "aside": {"title": "Detaljer att vara rädd om",
               "items": ["Glasverandor och förstukvistar",
                         "Spröjsade träfönster med foder",
                         "Entrédörrar i trä",
                         "Panelade takband på grupphusen"]}},
    {"id": "detaljer",
     "h2": "Fönster, dörrar och verandor – kommunens råd",
     "paras": [
       "Kulturmiljöunderlaget ger ovanligt konkreta råd. Äldre fönster kan vara av hög kvalitet "
       "och är ofta värda att underhålla, eventuellt kompletterade med invändigt energiglas. "
       "Tilläggsisoleras fasaden bör fönstren flyttas ut så att de sitter som förut i "
       "förhållande till fasaden, och takfoten kan behöva förlängas. Om dörrar skriver kommunen "
       "att särskilt entrédörrar är viktiga, och att man ska undersöka om en ny dörr passar husets "
       "stil.",
       "För villabebyggelsen kring kyrkbyn och Byle rekommenderas att fönster utformas i trä och "
       "likt originalen. Kommunen föreslår också att den som ska bygga till ett hus med höga "
       "kulturvärden tidigt tar råd av en sakkunnig avseende kulturvärden, till exempel "
       "en byggnadsantikvarie, en arkitekt eller en snickare med kunskap om kulturmiljövård.",
       "För oss betyder det att vi i första hand lagar: byter rötskadade delar i bågar och karmar, "
       "kittar om och justerar beslag, och tillverkar nya verandadelar efter de gamla. Ska "
       "fönstren ändå bytas finns mer att läsa om " + a("fonsterbyte.html", "fönsterbyte") + "."],
     "aside": None},
    {"id": "carport",
     "h2": "Carport, altan och tillbyggnad i grupphusområdena",
     "paras": [
       "I grupphusområdena bygger värdet på helheten. Täbys riktlinjer säger att tillägg som "
       "carport och altan ska anpassas till husets formspråk, utan avvikande takvinklar, för stora "
       "volymer eller kraftiga kontraster i material och färg, och att befintliga takformer och "
       "takfotens utformning bör väljas även för tillbyggnader. En carport på ett platt-taksradhus "
       "får alltså gärna ett lika lågt tak med samma takband.",
       "Tomterna i radhusområdena är smala. Enligt " + ext(BV_TILLB, "Boverket") + " ska en "
       "lovfri tillbyggnad ligga minst 4,5 meter från gränsen eller ha grannens skriftliga "
       "medgivande, och samma gräns gäller för en altan. Det enklaste är att grannarna skriver på "
       "en ritning som visar vad som ska byggas. Större utbyggnader beskriver vi under "
       + a("tillbyggnad.html", "tillbyggnad") + "."],
     "aside": {"title": "Före bygget",
               "items": ["Mät avståndet till tomtgränsen",
                         "Skriftligt medgivande från grannar vid behov",
                         "Kolla samfällighetens riktlinjer",
                         "Samma takform som huset"]}},
    {"id": "lov",
     "h2": "Lov i Täby efter december 2025",
     "paras": [
       "Täby kommun skriver på sidan om " + ext(TABY_FAS, "fasadändring") + " att det inte behövs "
       "bygglov för fasadändringar på en- och tvåbostadshus om byggnaden inte är särskilt "
       "värdefull, inte ligger i ett särskilt värdefullt område och inte har utökad lovplikt i "
       "detaljplanen. Nya fönster eller en ny entrédörr är därför oftast lovfria på en vanlig "
       "villa, men ska fortfarande göras varsamt.",
       "Ligger huset i en värdefull kulturmiljö och har fastigheten bestämmelser i detaljplanen, "
       "som q, Q eller k, rekommenderar kommunen i Kulturmiljöer i Täby att du hör av dig och frågar vad "
       "som gäller. Underlaget är inte juridiskt bindande, men det används när kommunen gör sina "
       "bedömningar. Påverkar arbetet bärande delar, till exempel en ny öppning i en bärande vägg, "
       "krävs anmälan och startbesked."],
     "aside": None},
    {"id": "inne",
     "h2": "Ny planlösning i villa och kedjehus",
     "paras": [
       "I villorna från 1970- och 1980-talen i Gribbylund och Skarpäng önskar många ett "
       "öppnare kök och vardagsrum eller ett extra rum på övervåningen. Vi tar fram om väggen är "
       "bärande, bygger nya väggar med ljudisolering och sätter dörrar, foder och lister som "
       "passar huset. Platsbyggda garderober och trappor anpassas efter de mått som finns.",
       "I en äldre villa i Roslags-Näsby eller Viggbyholm är det tvärtom ofta de gamla "
       "snickerierna som ska bevaras: innerdörrar, trappräcken och foder lagas, och nya delar görs "
       "i samma profil. Hör arbetet ihop med ett större grepp om huset samordnar vi det som en "
       + a("villarenovering.html", "villarenovering") + "."],
     "aside": None}],
  "steps_h2": "Arbetsgång i Täby",
  "steps": [
    ("Byggår och ritningar", "Vi utgår från husets epok och, när det finns, ritningar från "
     "kommunens arkiv."),
    ("Kontroll mot plan och riktlinjer", "Vi läser detaljplanen och ser om huset beskrivs i "
     "Kulturmiljöer i Täby."),
    ("Besök och uppmätning", "Fönster, dörrar, veranda och stomme undersöks, och profiler mäts upp "
     "om något ska kopieras."),
    ("Förslag", "Du får ett skriftligt förslag som skiljer på lagning och byte, med vad det "
     "betyder för husets utseende."),
    ("Grannar och samfällighet", "Vid bygge nära gräns tar vi fram en ritning som grannarna kan "
     "skriva på."),
    ("Utförande och genomgång", "Vi bygger, går igenom arbetet med dig och lämnar en "
     "sammanställning.")],
  "rot_h2": "ROT-avdrag för snickeriet",
  "rot": [
    "Arbetskostnaden ger 30 procent i rotavdrag, högst 50 000 kr per person och år och högst "
    "75 000 kr tillsammans med rut. Materialet räknas inte. Vi drar av beloppet direkt på "
    "fakturan, och äger ni huset tillsammans kan ni dela upp avdraget.",
    "Enligt " + ext(SKV_ARB, "Skatteverket") + " ger det avdrag att reparera eller byta fönster, "
    "glasa in en altan och bygga en altan som sitter ihop med huset. En fristående ny byggnad "
    "ger inget avdrag, och för om- och tillbyggnad ska huset ha passerat fem år från värdeåret."],
  "price_h2": "Det här påverkar kostnaden",
  "price": [
    "Det som styr mest är hur mycket som kan lagas jämfört med att bytas, om fönster- och "
    "dörrdetaljer ska specialtillverkas, hur stor altanen eller carporten blir och om något "
    "bärande berörs. Vi kommer på ett kostnadsfritt besök och lämnar ett skriftligt "
    "kostnadsförslag."],
  "faq": [
    ("Kan glasverandan på vår villa i Täby kyrkby renoveras i stället för att rivas?",
     "Ofta ja. Bågar, spröjs och stolpar med röta byts mot nya delar i samma profil, och resten "
     "lagas och målas. Kommunens riktlinjer pekar ut glasverandor som typiska för villorna från "
     "tidigt 1900-tal."),
    ("Vilken carport passar ett platt-taksradhus från 1960-talet?",
     "En carport med lika lågt tak och samma typ av takband som huset. Täbys riktlinjer avråder "
     "från avvikande takvinklar och stora kontraster i material och färg."),
    ("Måste grannen godkänna vår altan i radhusområdet?",
     "Ligger altanen närmare tomtgränsen än 4,5 meter behövs grannens skriftliga medgivande för "
     "att den ska vara lovfri. Utan medgivande krävs bygglov."),
    ("Kan vi sätta energiglas i de gamla fönstren?",
     "Ja. Kommunens råd är att underhålla äldre fönster och vid behov komplettera med invändigt "
     "energiglas. Det behåller fönstrets utseende utifrån."),
    ("Har kommunen ritningar på vårt hus?",
     "Det kan finnas. Kommunen rekommenderar att man tar fram ritningar inför en ombyggnad, eftersom många "
     "hus byggts till och ritningarna visar konstruktionen. Vi hjälper gärna till att beställa "
     "dem.")],
  "sources": [
    ("Täby kommun – Kulturmiljöer i Täby (antagen)", TABY_KM),
    ("Täby kommun – Fasadändring", TABY_FAS),
    ("Boverket – Göra en tillbyggnad", BV_TILLB),
    ("Boverket – Ingrepp i husets bärande delar", BV_BAR),
    ("Boverket – Lista med PBL-ändringar 1 december 2025", BV_LISTA),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)],
  "cta": ("Vill du laga verandan eller bygga carport?", "Hör av dig så bokar vi ett kostnadsfritt "
          "besök i Täby."),
  "img": [("Gulmålad villa från tidigt 1900-tal med glasveranda och spröjsade fönster i Täby",
           "early 1900s Swedish wooden villa with horizontal yellow painted panel, white trim, "
           "steep mansard roof, glazed veranda with small-paned windows, mature garden, Täby"),
          ("Ny carport med lågt platt tak vid ett radhus från 1960-talet",
           "new timber carport with low flat roof and wide painted fascia matching a 1960s Swedish "
           "terraced house with brick ground floor and wooden panels under windows")],
},

# ---------------------------------------------------------------- NORRTÄLJE
"snickare-norrtalje.html": {
  "kind": "district", "service": "snickare", "ort": "Norrtälje", "svc_label": "Snickare",
  "title": "Snickare i Norrtälje – fritidshus, altan och strand",
  "description": "Snickare i Norrtälje: permanentning av fritidshus, altaner, gäststugor och "
                 "panel i Roslagen. Strandskydd, lovbefriade åtgärder från december 2025 och ROT.",
  "h1": "Snickare i Norrtälje",
  "lead": "Som snickare i Norrtälje bygger man för Sveriges mest fritidshustäta kommun. Uppdragen "
          "är ofta att göra ett sommarhus beboeligt året runt, bygga en altan eller gäststuga på "
          "landet eller laga panel och fönster – och nära vattnet kan strandskyddet styra mer än "
          "bygglovet.",
  "card": "Fritidshus, altan och gäststuga.",
  "sections": [
    {"id": "roslagen", "anchor": "Husen i Roslagen",
     "h2": "Flest fritidshus i landet",
     "paras": [
       "Enligt " + ext(SCB_FRIT, "SCB") + " har Norrtälje 27 352 fritidshus, fler än någon annan "
       "kommun i Sverige. Kommunen beskriver sig som en av landets största landsbygdskommuner, med "
       "cirka 32 000 invånare på landsbygden, och skriver på sidan " + ext(NT_FAKTA, "fakta och "
       "statistik") + " att ungefär en fjärdedel av fritidshusens brukare vistas i kommunen större "
       "delen av året. Landsbygdsbefolkningen har ökat med cirka 60 procent sedan 1982.",
       "I tätorterna ser det annorlunda ut. Norrtälje stad grundades 1622, och där finns villor "
       "och radhus i bostadsområden som Färsna och Vigelsjö. Rimbo växte runt järnvägsknuten och Hallstavik runt "
       "pappersbruket vid Edeboviken, och båda fick många villor efter andra världskriget.",
       "För snickeriet är det två helt olika vardagar: i Rimbo en villa med uppfart och "
       "byggvaruhus nära, i skärgården ett hus där virket kanske ska fraktas sista biten med båt."],
     "aside": {"title": "Vanliga uppdrag här",
               "items": ["Sommarhus som ska klara vintern",
                         "Altan och trädäck mot sjön",
                         "Gäststuga eller förråd på tomten",
                         "Panel och fönster på äldre hus"]}},
    {"id": "permanent",
     "h2": "När sommarhuset ska bli bostad",
     "paras": [
       "Ett hus byggt för somrarna saknar ofta det som ett helårshus behöver: tät klimatskärm, "
       "isolerade väggar och golv, en entré där man kan ta av sig vinterkläder och förvaring. "
       "Snickeriet är en stor del av ombyggnaden – nya regelväggar och golv, utbytta dörrar och "
       "fönster, ny panel där den gamla är rötskadad och kanske ett vindsrum.",
       "Ofta byggs huset också till. En lovfri tillbyggnad får sammanlagt vara högst 30 "
       "kvadratmeter och inte gå över husets taknock, och tillbyggnader som gjorts lovfritt före "
       "1 december 2025, som attefallstillbyggnad, takkupa och skärmtak, ska räknas in. Det "
       "skriver kommunen på sidan om " + ext(NT_LOV, "lovbefriade åtgärder") + ". Påverkas "
       "bärande delar krävs anmälan, och nya installationer för vatten, avlopp eller eldstad ska "
       "anmälas.",
       "Vi börjar med en genomgång av huset och diskuterar i vilken ordning arbetena bör göras, så "
       "att inget behöver rivas upp igen. Större ombyggnader samordnar vi som en "
       + a("byggfirma.html", "total entreprenad") + "."],
     "aside": None},
    {"id": "strand",
     "h2": "Strandskyddet gäller även lovfria altaner och bryggor",
     "paras": [
       "Strandskyddet gäller i regel 100 meter från strandlinjen, upp på land och ut i vattnet, och "
       "i vissa områden i Stockholms län är det utökat till 300 meter. Inom skyddet är det förbjudet "
       "att bland annat uppföra byggnader och tillbyggnader eller anläggningar utan dispens. "
       "Kommunen skriver på sidan om " + ext(NT_STR, "strandskyddsdispens") + " att även "
       "bygglovsfria åtgärder, som friggebodar, attefallshus, staket och bryggor, kan kräva "
       "dispens.",
       "En altan som är lovfri enligt plan- och bygglagen kan alltså ändå kräva strandskyddsdispens "
       "om den byggs nära vattnet. I områden med landskapsbildsskydd, vanligast kring kyrkor som på "
       "Arholma, prövar Länsstyrelsen ansökan. Kommunens kontaktcenter kan svara på om din "
       "fastighet ligger inom strandskyddat område.",
       "Vi frågar därför tidigt hur långt det är till vattnet. Är dispens nödvändig väntar vi med "
       "att beställa material tills beslutet finns."],
     "aside": {"title": "Kan kräva dispens",
               "items": ["Altan eller trädäck nära stranden",
                         "Gäststuga eller förråd", "Brygga", "Staket mot vattnet"]}},
    {"id": "lov",
     "h2": "Lovbefriat inom och utanför detaljplan",
     "paras": [
       "Stora delar av kommunen saknar detaljplan, och då gäller andra mått. Enligt kommunen får "
       "fristående lovbefriade byggnader inom detaljplan vara högst 30 kvadratmeter var och 45 "
       "sammanlagt, medan gränserna utanför detaljplan är 50 och 65 kvadratmeter. Nockhöjden får "
       "vara högst 4 meter inom detaljplan och 4,5 meter utanför. Begreppet attefallshus togs bort "
       "1 december 2025 och ersattes av komplementbyggnad och komplementbostadshus.",
       "För altaner har Boverket inga höjd- eller placeringsregler utanför detaljplan, så där kan "
       "en större altan byggas friare. Nära gräns, inom ett särskilt värdefullt område eller nära "
       "järnväg kan lov ändå krävas. Kommunen bedömer inte enskilda åtgärder via e-post eller "
       "telefon – den som vill ha ett bindande besked kan söka frivilligt lov. Mer om "
       "komplementbostadshus finns på sidan om " + a("attefallshus.html", "attefallshus") + "."],
     "aside": None},
    {"id": "logistik",
     "h2": "Material och arbetsdagar långt från stan",
     "paras": [
       "På öar utan fast förbindelse når man fastigheten bara med båt eller färja. Då planeras "
       "leveranser av virke och skivor så att allt kommer samtidigt, och rivningsvirke tas med "
       "tillbaka på samma sätt. Ett arbete på ett fritidshus läggs gärna under en period med "
       "stabilt väder, så att huset inte står öppet i höststormarna.",
       "Vi utgår från Bromma och tar uppdrag i hela kommunen, från Rimbo och Hallstavik till "
       "kusten vid Grisslehamn. Längre resor samordnar vi så att besök och arbete samlas i färre "
       "turer."],
     "aside": None}],
  "steps_h2": "Så planerar vi jobbet i Norrtälje",
  "steps": [
    ("Läge och avstånd till vatten", "Vi tar reda på om fastigheten ligger inom detaljplan och "
     "strandskydd innan något ritas."),
    ("Besök på plats", "Vi går igenom huset, mäter upp och noterar fukt, röta och hur huset används "
     "över året."),
    ("Ordning på arbetena", "Vid en permanentning bestämmer vi tillsammans vad som görs först, så "
     "att inget behöver göras om."),
    ("Dispens eller lov vid behov", "Krävs strandskyddsdispens eller lov tar vi fram ritningar och "
     "underlag till ansökan."),
    ("Leveranser och etablering", "Transporter planeras efter väg, färja eller båt."),
    ("Bygge och genomgång", "Vi bygger i etapper och går igenom resultatet med dig på plats.")],
  "rot_h2": "ROT för snickeri på fritidshuset",
  "rot": [
    "Rotavdrag gäller även för fritidshus som du äger och använder. Bor någon annan permanent i "
    "huset räknas det enligt " + ext(SKV_ROT, "Skatteverket") + " inte längre som ditt fritidshus. "
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst "
    "75 000 kr tillsammans med rut. Resor och material ger inget avdrag.",
    "En altan som byggs ihop med huset ger avdrag, liksom en tillbyggnad – även en gäststuga eller "
    "ett förråd som byggs ihop med huset. En "
    "helt ny fristående byggnad, till exempel en friggebod, gör det inte. Vi drar av beloppet "
    "direkt på fakturan."],
  "price_h2": "Vad påverkar priset?",
  "price": [
    "Mest betyder omfattningen – en ny altan eller en hel permanentning – och hur mycket av det "
    "gamla som går att behålla. Avståndet, om material måste fraktas med båt och om dispens eller "
    "lov krävs påverkar också. Platsbesöket är kostnadsfritt och du får ett skriftligt "
    "kostnadsförslag."],
  "faq": [
    ("Behöver vi strandskyddsdispens för en altan vid sjön i Norrtälje?",
     "Det kan behövas, även om altanen inte kräver bygglov. Strandskyddet gäller i regel 100 meter "
     "från stranden och i vissa områden i länet 300 meter. Fråga kommunens kontaktcenter om din "
     "fastighet ligger inom skyddet."),
    ("Hur stor gäststuga får vi bygga utan lov på landet utanför detaljplan?",
     "Utanför detaljplan får en lovbefriad komplementbyggnad vara högst 50 kvadratmeter och 4,5 "
     "meter till nock, och alla lovbefriade byggnader på tomten högst 65 kvadratmeter "
     "sammanlagt. Strandskydd och gränsavstånd kan ändå kräva dispens eller lov."),
    ("Räknas den gamla friggeboden in när vi bygger nytt?",
     "Ja. Kommunen skriver att även byggnader som var lovbefriade enligt äldre regler ska räknas "
     "med när byggnadsarean summeras."),
    ("Kan ni ta uppdrag på en ö utan bilväg?",
     "Ja. Vi planerar transporterna med båt eller färja och samlar leveranserna så att arbetet "
     "kan göras i ett sammanhang."),
    ("Får vi rotavdrag om vi hyr ut stugan några veckor?",
     "Avdraget förutsätter att du äger huset och själv använder det. Bor någon annan permanent i "
     "huset räknas det inte längre som ditt fritidshus. Vid kortare uthyrning – fråga Skatteverket "
     "om just ditt fall.")],
  "sources": [
    ("SCB – Fritidshus, var finns de?", SCB_FRIT),
    ("Norrtälje kommun – Fakta och statistik om landsbygden", NT_FAKTA),
    ("Norrtälje kommun – Lovbefriade åtgärder", NT_LOV),
    ("Norrtälje kommun – Strandskyddsdispens", NT_STR),
    ("Boverket – Lista med PBL-ändringar 1 december 2025", BV_LISTA),
    ("Boverket – Mur, plank, altan och annat", BV_ALTAN),
    ("Boverket – Göra en tillbyggnad", BV_TILLB),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_ARB)],
  "cta": ("Ska fritidshuset byggas om eller få en altan?", "Berätta om huset och läget så planerar "
          "vi ett kostnadsfritt besök i Norrtälje."),
  "img": [("Rödmålat fritidshus i Roslagen med ny altan mot en vik",
           "red painted wooden Swedish summer house with white trim and a new wooden deck facing a "
           "calm sea inlet, rocky shore and pine trees, Roslagen archipelago, Norrtälje"),
          ("Gäststuga i trä under uppbyggnad på en landsbygdstomt",
           "small new timber guest cottage under construction with fresh wooden cladding and "
           "windows installed, rural Swedish plot with birch trees and meadow")],
},
}
