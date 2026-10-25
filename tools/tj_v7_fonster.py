# -*- coding: utf-8 -*-
"""Fönsterbyte – ortsidor v7: Danderyd, Ekerö, Vallentuna, Österåker, Norrtälje, Järfälla (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25: Danderyds kommun (Nya regler
för bygglov från 1 december 2025; Kulturmiljöhandboken B4 Danderyds kyrka/Berga/Ekeby med den allmänna delen
"För samtliga områden gäller följande"), Boverket (rättsfall: Bygglov för fönsterbyte på enbostads-/gatuhus,
MÖD P 169–15; energiguiden: Energirenovera eller byta fönster och dörrar; Bidrag för energieffektivisering i
småhus), Ekerö kommun (Kulturmiljöprogram 2015, Östra Ekerö; Vad vill du bygga?), Vallentuna kommun
(Översiktsplan 2040 med aktualitetsprövning: Arlanda, påverkansområde flygbuller och lågfartsflyg, bullertabell;
Fasadändring), Österåkers kommun (Kulturhistoriska byggnader, kulturmiljöer i bygglovsguiden), Norrtälje kommun
(Kulturmiljöutredning nr 21 Herräng 2016; Bevarandeprogram för Norrtälje stad; Fasadändring), Järfälla kommun
(Kulturmiljöplan: Kallhäll och Jakobsberg; Fasadändring) och Skatteverket (Så fungerar rotavdraget; Ger
arbetet rätt till rotavdrag?).
Strukna (ej verifierade): Swedavias bullerisolering/ersättning för villor i Vallentuna (ingen aktuell källa),
att särskilda Vallentunaområden ligger i dagens påverkansområde, fönstertyper i Österåkers villaområden,
Österåkers kulturmiljöprogram (ingen länk hittad), innehållet i Norrtälje stads bevarandeprogram (bara
kommunens sammanfattning öppnad), fjärrvärmeutbredning i respektive kommun, att 1960–70-talshusen i Järfälla
har treglasfönster i instickskarmar (Boverket säger bara att det är vanligt för 70-talets treglasfönster),
bidragsbelopp i kronor (utelämnade). Inga priser, garantier, omdömen, egna uppdrag eller cert.
Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_FONSTER = ("Boverket – Energiguiden: Energirenovera eller byta fönster och dörrar",
               "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/fonster_dorrar/")
_BV_DOM = ("Boverket – Rättsfall: Bygglov för fönsterbyte på enbostads-/gatuhus (MÖD P 169–15)",
           "https://www.boverket.se/sv/samhallsplanering/arkitektur-och-gestaltad-livsmiljo/arbetssatt/arkitektur-och-pbl/rattsfall/en--och-tvabostadshus/bygglov-for-fonsterbyte-pa-enbostads-gatuhus/")
_BV_BIDRAG = ("Boverket – Bidrag för energieffektivisering i småhus",
              "https://www.boverket.se/sv/bidrag--garantier/bidrag-for-energieffektivisering-i-smahus/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ DANDERYD
"fonsterbyte-danderyd.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Danderyd", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Danderyd – klassade hus, spröjs och lovplikt",
  "description": "Fönsterbyte i Danderyd: när nya fönster kräver bygglov, husens klassning som omistlig, värdefull eller intressant och varför spröjsen kan avgöra.",
  "h1": "Fönsterbyte i Danderyd",
  "lead": "I Danderyd kan samma fönsterbyte vara lovfritt på en gata och kräva bygglov på nästa. Det avgörs av om huset eller området räknas som kulturhistoriskt särskilt värdefullt. Geal Entreprenad AB byter och renoverar fönster i Djursholm, Stocksund, Enebyberg och resten av Danderyd, tar reda på vad som gäller för just ditt hus och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Lovplikt, klassning och spröjs i Danderyd.",
  "sections": [
    {"id": "lov-danderyd", "anchor": "Lovplikten",
     "h2": "Nya fönster är lovfria – utom i de värdefulla miljöerna",
     "paras": [
       "På sin sida om de nya reglerna från den 1 december 2025 svarar Danderyds kommun på frågan om bygglov behövs för ommålning, nytt tak eller fönster. För ett en- eller tvåbostadshus är svaret nej. Kommunen lägger till att ändringar av byggnader ska göras varsamt och på ett sätt som är anpassat till byggnadens värden.",
       "Undantaget väger tungt i Danderyd. Lov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område, om själva byggnaden är kulturhistoriskt särskilt värdefull eller om fastigheten ligger inom ett riksintresse för kulturmiljövården. Vilka fastigheter som berörs går att se i kommunens kulturmiljökarta.",
       "Kommunen påpekar också att många åtgärder inte längre granskas innan arbetet börjar, och att ansvaret för att följa reglerna ligger hos fastighetsägaren. Den som vill ha ett formellt besked kan söka ett frivilligt bygglov. Byggnadsnämnden prövar då att åtgärden uppfyller lagens krav, och du får ett beslut att utgå från.",
     ],
     "aside": {"title": "Innan fönstren beställs", "items": [
       "Titta i kulturmiljökartan", "Läs detaljplanen – finns q eller Q?",
       "Ta hjälp av kommunens rådgivning", "Överväg ett frivilligt bygglov"]}},
    {"id": "klassning", "h2": "Omistlig, värdefull eller intressant",
     "paras": [
       "Danderyds kulturmiljöhandbok delar in husen i de bebyggelseinventeringar som gjorts i tre klasser: omistlig, värdefull och intressant. För de omistliga byggnaderna ska förändringar ske med mycket stor hänsyn till egenarten, för de värdefulla med stor varsamhet. De intressanta byggnaderna anses skyddade genom det som gäller för området i stort. I avsnittet om Danderyds kyrka, Berga och Ekeby räknas till exempel Berga gård och Nybytorp som omistliga.",
       "Handbokens allmänna del, som gäller för alla utpekade områden, säger att stor vikt ska läggas vid att husens ursprungliga exteriör inte förändras genom byte av bland annat fönster, och att ursprungliga material som med sin ålder och patina berättar om äldre hantverk bör bevaras. Nytillskott som fönster, dörrar och burspråk ska anpassas till huset i utformning, placering och materialval.",
       "Därför börjar vi med att ta reda på hur huset är klassat. För ett omistligt eller värdefullt hus är det ofta renovering av de befintliga bågarna som stämmer bäst med handboken, medan ett byte kan vara rimligt på ett hus som redan har fått fönster av senare typ.",
     ],
     "aside": None},
    {"id": "sprojs-danderyd", "h2": "Ett 70-talshus med spröjs – och ett nekat bygglov",
     "paras": [
       "Boverket beskriver ett mål i Mark- och miljööverdomstolen från 2015 (P 169–15) om ett enbostadshus från mitten av 1970-talet. Huset låg i en miljö som Riksantikvarieämbetet bedömt vara av riksintresse, och kommunen hade en varsamhetsbestämmelse i detaljplanen. Ägaren ville byta de spröjsade fönstren mot fönster utan spröjs. Domstolen bedömde att det inte var en varsam ändring, och nekat bygglov stod fast.",
       "Det intressanta är att huset inte var gammalt. Det hade fått spröjsade fönster för att anpassas till den äldre bebyggelsen i kvarteret, och domstolen utgick från just den byggnadens karaktärsdrag, inte från vad som var typiskt för 1970-talet. Domstolen noterade också att det inte hade framkommit några större kostnadsskillnader mellan fönster med och utan spröjs.",
       "Danderyd har gott om yngre hus som har ritats för att passa in bland äldre villor. Därför mäter vi upp och fotograferar spröjsindelningen även på ett hus från 1970- eller 80-talet innan nya fönster beställs. Ska fönstren hellre målas och lagas än bytas, läs mer under " + _L.format("malare-danderyd.html", "målare i Danderyd") + ".",
     ],
     "aside": {"title": "Det domstolen vägde in", "items": [
       "Riksintresse och varsamhetsbestämmelse", "Husets egna karaktärsdrag",
       "Varför huset fick spröjs", "Ingen större kostnadsskillnad"]}},
    {"id": "glas-danderyd", "h2": "Gammalt glas, bågar i verkstad och rotavdraget",
     "paras": [
       "Boverkets energiguide påpekar att äldre glas och invändig profilering kan betyda mycket för hur ett rum upplevs. Om innerbågen får ett energiglas eller en tvåglaskassett vid en renovering kan rutor av äldre munblåst eller valsat glas som blir över användas som ytterrutor på andra bågar, där originalglaset har gått förlorat.",
       "Var arbetet görs har betydelse för rotavdraget. Skatteverket godkänner att reparera eller byta fönster och att montera bullerglas och isolerglas, men inte glas- och plåtarbeten som utförs utanför kundens bostad, till exempel i företagets egna lokaler. Tas bågarna ner för att renoveras på annat håll påverkar det alltså vilken del av arbetet som ger avdrag.",
       "Boverket påminner också om att nya fönster med grövre snickerier släpper in mindre dagsljus, och att bågar, gångjärn och beslag måste klara den extra tyngd som nytt glas ofta innebär. Hör fönsterarbetet ihop med en större översyn av väggarna, se " + _L.format("fasadrenovering-danderyd.html", "fasadrenovering i Danderyd") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras ett fönsterbyte i Danderyd",
  "steps": [
    ("Kartan och planen", "Vi kontrollerar kulturmiljökartan och detaljplanen och tar reda på hur huset är klassat."),
    ("Platsbesök", "Varje fönster mäts upp, spröjs och profiler fotograferas och glaset bedöms."),
    ("Renovera eller byta", "Fönster för fönster avgör vi vad som kan behållas och vad som behöver bytas."),
    ("Kostnadsförslag", "Ett skriftligt förslag där renovering, nya fönster, glas och montage står var för sig."),
    ("Lovfrågan", "Kräver åtgärden lov, eller vill du ha ett frivilligt lov, tas underlaget fram innan beställning."),
    ("Montage och genomgång", "Fönstren sätts in med drevning och tätning, och vi går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Danderyd",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Kostnader för material, resor och utrustning ger inget avdrag, och du ska äga bostaden när arbetet utförs.",
    "Att byta fönsterbleck och måla fönster räknas också som rotarbete. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Danderyd?",
  "price": [
    "Hur många fönster som kan renoveras i stället för att bytas, om spröjs och profiler måste tillverkas efter förlaga, om äldre glas ska tas tillvara och flyttas, om underlag för bygglov behöver tas fram och hur mycket foder och bleck som ska göras om. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för nya fönster på vår villa i Djursholm?",
     "Bara om fastigheten eller huset räknas som kulturhistoriskt särskilt värdefullt eller ligger inom riksintresset för kulturmiljövården. Det framgår av kommunens kulturmiljökarta. Annars är fönsterbytet lovfritt, men det ska göras varsamt."),
    ("Vad betyder det att ett hus i Danderyd är klassat som omistligt?",
     "Att det i kommunens bebyggelseinventeringar räknats till den högsta av tre klasser. Enligt kulturmiljöhandboken ska förändringar av sådana hus göras med mycket stor hänsyn till deras egenart."),
    ("Måste ett hus från 1970-talet behålla sina spröjsade fönster?",
     "Inte generellt, men i ett värdefullt område kan det krävas. Mark- och miljööverdomstolen nekade 2015 bygglov för att ta bort spröjsen på ett 70-talshus, eftersom spröjsen var en del av just det husets karaktär."),
    ("Ger det rotavdrag om bågarna renoveras i en verkstad?",
     "Skatteverket godkänner inte glasarbeten som utförs utanför kundens bostad, till exempel i företagets lokaler. Arbete som görs på plats i huset kan ge avdrag."),
    ("Kan det gamla glaset sparas när fönstren får energiglas?",
     "Ofta ja. Boverket beskriver hur äldre munblåst eller valsat glas som blir över kan sättas in som ytterruta på andra bågar, medan innerbågen får ett modernt energiglas."),
  ],
  "sources": [
    ("Danderyds kommun – Nya regler för bygglov från 1 december 2025",
     "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/"),
    ("Danderyds kommun – Kulturmiljöhandboken: Danderyds kyrka, Berga, Ekeby (pdf)",
     "https://danderyd.se/globalassets/globala-filer/bygga-bo-och-miljo/bygglov/kulturmiljohandboken/b4-danderyds-kyrka---berga---ekeby.pdf"),
    _BV_DOM, _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Funderar ni på nya fönster i Danderyd?", "Boka ett gratis platsbesök så går vi igenom fönstren, husets klassning och lovfrågan."),
  "img": [
    ("Ljusputsad villa i Danderyd med vita spröjsade fönster och rött tegeltak bland ekar",
     "1920s Swedish two-storey light ochre plastered villa with symmetrical facade, white wooden casement windows divided by glazing bars into small panes, white window surrounds, steep red clay tile hipped roof, large oak trees and a lawn, Djursholm Danderyd, calm daylight, empty scene, no people, no text"),
    ("Närbild på en äldre fönsterbåge med spröjs och lätt ojämnt gammalt glas",
     "close-up of an old white painted wooden window sash with a glazing bar and slightly wavy old hand-blown glass reflecting trees, putty lines visible, part of a plastered wall around it, soft daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ EKERÖ
"fonsterbyte-ekero.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Ekerö", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Ekerö – sommarvillor, 60-tal och kallras",
  "description": "Fönsterbyte i Ekerö: permanentade sommarvillor i Älvnäs och Gällstaö, villor från 1960- och 70-talen, kallras, imma på rutan och kommunens lovregler.",
  "h1": "Fönsterbyte i Ekerö",
  "lead": "På östra Ekerö har många sommarhus blivit åretruntbostäder, och bredvid dem ligger villaområden från 1960- och 1970-talen. I båda fallen är fönstren ofta den del av huset som märks mest en kall vinterdag. Geal Entreprenad AB byter och renoverar fönster i Ekerö, Stenhamra och på öarna runt omkring, och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Sommarvillor och 60-talsvillor i Ekerö.",
  "sections": [
    {"id": "ostra-ekero", "anchor": "Östra Ekerö",
     "h2": "Från sommarbostad till villagata på östra Ekerö",
     "paras": [
       "Ekerö kommuns kulturmiljöprogram från 2015 beskriver östra Ekerö som ett område där exploateringstrycket är högt och där det hela tiden sker förtätningar. Områden med sommarbostäder har de senaste decennierna permanentats och förtätats. Som exempel nämns Älvnäs, Gällstaö och Erikssten, där sommarvillor och sportstugor från 1900-talet har byggts om eller rivits.",
       "Det dominerande inslaget är ändå villa- och radhusbebyggelse från andra halvan av 1900-talet. Programmet nämner Väsby med enhetlig bebyggelse från tidigt 1970-tal och Närlunda, som domineras av villor från 1960-talet. På östra Ekerö ligger också Ekerö centrum, ritat av Ralph Erskine och invigt 1991, som ett av landets yngsta kommuncentrum.",
       "Programmets råd för östra Ekerö är att befintliga byggnader bör respekteras när det gäller proportioner, fasadfärg, tak och byggnadsdetaljer som fönster, panel, entréer och räcken. Rådet gäller uttryckligen både flerfamiljshusen i centrum och villa- och sportstugebebyggelsen. Ett fönsterbyte i ett enhetligt område som Väsby bör alltså ge samma intryck från gatan som grannhusens fönster.",
     ],
     "aside": {"title": "Östra Ekerö i programmet", "items": [
       "Älvnäs, Gällstaö, Erikssten: permanentade sommarområden", "Väsby: enhetligt tidigt 1970-tal",
       "Närlunda: villor från 1960-talet", "Ekerö centrum: Ralph Erskine, 1991"]}},
    {"id": "kallras", "h2": "Kallras och U-värde i ett hus som ska värmas hela vintern",
     "paras": [
       "Boverket förklarar att ju lägre värmegenomgångstal, U-värde, ett fönster har, desto mindre kall luft faller ner längs rutan mot golvet. Den kalla luften kallas kallras och känns som drag. Boverkets tumregel är att det inte uppstår något kallras om U-värdet är lägre än 1,0.",
       "Samtidigt isolerar även de bästa fönstren bara ungefär lika bra som fem centimeter vanlig isolering, och ett gammalt fönster kan släppa igenom betydligt mer. I ett hus som en gång byggdes för sommarbruk och som nu ska värmas hela året blir fönstren därför en stor del av värmeförlusten, särskilt om de är många och stora mot sjön.",
       "Boverket råder att välja fönster med lågt U-värde för hela konstruktionen, alltså glas, båge och karm tillsammans, och att kontrollera märkningslappen när fönstren levereras. Det är också värt att dokumentera husets energianvändning före bytet, så att det går att se vad det gav under det första året.",
     ],
     "aside": None},
    {"id": "imma-ekero", "h2": "Imma på insidan eller på utsidan av rutan",
     "paras": [
       "Efter ett fönsterbyte märker en del husägare att rutorna blir immiga på morgonen. Boverket skiljer på två fall. Kondens på insidan är ett tecken på att ventilationen kan behöva förbättras. Kondens på utsidan är däremot inte ett fel utan ett kvitto på att fönstret isolerar bra, eftersom det yttre glaset blir kallare. Den försvinner efter ett par timmar.",
       "Boverket nämner att solavskärmning som skuggar fönstret mot natthimlen kan minska kondensen på utsidan. I ett hus vid Mälaren med fri utsikt mot vattnet går det sällan att undvika helt, och det är bra att veta om innan man väljer det bäst isolerande glaset.",
       "Kondensen på insidan är viktigare att ta på allvar. Har huset självdrag påpekar Boverket att luft som läckt in kring otäta fönster kan ha varit en del av tilluften. När de nya fönstren är täta behöver tilluften ordnas på annat sätt, och vi går igenom det vid besöket.",
     ],
     "aside": {"title": "Imma – vad betyder den?", "items": [
       "Insidan: se över ventilationen", "Utsidan: fönstret isolerar väl",
       "Utvändig imma försvinner efter några timmar", "Solskydd kan minska den utvändiga"]}},
    {"id": "lov-ekero", "h2": "Lov, anmälan och fönster i ny storlek",
     "paras": [
       "Ekerö kommun skriver att fasadändringar på ett en- eller tvåbostadshus inte kräver bygglov, utom när fastigheten ligger i ett område som bedömts som särskilt värdefullt. Ett byte till fönster i samma öppningar är därför i de flesta fall en lovfri åtgärd, men varsamhetskravet gäller.",
       "Ska ett fönster göras större för att få in mer ljus eller utsikt blir det en annan sak. Kräver ändringen nya reglar i väggen räknar kommunen det som en väsentlig ändring av bärande konstruktion, och då ska den anmälas. Kräver åtgärden även bygglov hanteras allt i samma ansökan. Är du osäker kan du skicka ett foto på huset till kommunen och beskriva ändringen.",
       "När fönstren sitter i en fasad som också behöver ses över kan det löna sig att göra båda samtidigt. Mer om det finns under " + _L.format("fasadrenovering-ekero.html", "fasadrenovering i Ekerö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången när fönstren byts i Ekerö",
  "steps": [
    ("Besök och mätning", "Vi mäter upp fönstren, kontrollerar karmar och bröstningar och ser hur huset ventileras."),
    ("Val av fönster", "U-värde, glas, indelning och kulör väljs efter huset och grannhusen i området."),
    ("Lov och anmälan", "Vi kontrollerar om området är särskilt värdefullt och om någon öppning ska ändras."),
    ("Skriftligt förslag", "Fönster, montage, foder, bleck och eventuella ventiler redovisas var för sig."),
    ("Byte", "Fönstren byts i etapper så att huset inte kyls ner, med drevning och tätning runt karmen."),
    ("Uppföljning", "Vi går igenom fönstren med dig och visar hur ventilationen och underhållet fungerar."),
  ],
  "rot_h2": "Rotavdrag för nya fönster i Ekerö",
  "rot": [
    "Skatteverket godkänner rotavdrag för att reparera eller byta ut fönster och för att montera isolerglas och bullerglas. Avdraget gäller även ett fritidshus som du äger. Det är 30 procent av arbetskostnaden, med ett tak på 50 000 kr per person och år och 75 000 kr för rot och rut tillsammans.",
    "Själva fönstren, resor och utrustning räknas inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här styr priset i Ekerö",
  "price": [
    "Antal fönster och deras storlek, vilket U-värde och glas som väljs, om någon öppning ska göras större, hur mycket foder, bleck och bröstningar som behöver göras om och om ventilationen behöver kompletteras. Läget på tomten och avståndet påverkar också. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vår sommarvilla i Älvnäs är nu åretruntbostad – räcker de gamla fönstren?",
     "Det beror på skicket och hur huset ventileras. Gamla fönster kan släppa igenom betydligt mer värme än nya. Vi bedömer vid besöket om bågarna kan förbättras med energiglas eller om ett byte är rimligare."),
    ("Vilket U-värde behövs för att slippa drag vid fönstren?",
     "Boverkets tumregel är att det inte uppstår något kallras om fönstrets U-värde är lägre än 1,0. Värdet ska gälla hela fönstret, inte bara glaset."),
    ("Varför är de nya fönstren immiga på utsidan på morgonen?",
     "Det betyder att det yttre glaset är kallt eftersom fönstret isolerar bra. Boverket beskriver det som normalt, och immen försvinner efter ett par timmar."),
    ("Måste nya fönster i Väsby se ut som grannarnas?",
     "Kulturmiljöprogrammet råder att proportioner och byggnadsdetaljer som fönster respekteras. I ett enhetligt område från 1970-talet bör de nya fönstren därför ha liknande indelning och kulör som de övriga husen."),
    ("Behöver jag anmäla till Ekerö kommun om vi gör ett fönster större?",
     "Ja, om ändringen kräver nya reglar och väsentligt påverkar bärande konstruktion. Ligger huset i ett särskilt värdefullt område kan bygglov också behövas."),
  ],
  "sources": [
    ("Ekerö kommun – Kulturmiljöprogram 2015 (pdf)",
     "https://www.ekero.se/download/18.553838ea17305720c321ec82/1597925412772/Eker%C3%B6%20kulturmilj%C3%B6program.pdf"),
    ("Ekerö kommun – Vad vill du bygga?",
     "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/vad-vill-du-bygga"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren bytas i huset på Ekerö?", "Boka ett gratis platsbesök så går vi igenom fönstren, ventilationen och vad som behöver göras."),
  "img": [
    ("Ombyggd sommarvilla på Ekerö med nya vita fönster och utsikt mot Mälaren",
     "early 1900s Swedish wooden summer villa converted to a year-round home, pale green painted horizontal panel, new white wooden two-pane windows, glazed veranda, red clay tile roof, birch and pine trees, glimpse of lake Mälaren behind, Ekerö, calm autumn daylight, empty scene, no people, no text"),
    ("Utvändig imma på nedre delen av en fönsterruta en kall morgon",
     "close-up of a modern white wooden window on a Swedish house on a cold early morning, light dew condensation on the outside of the glass in the lower half, frosty garden blurred in the reflection, wooden facade around the window, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VALLENTUNA
"fonsterbyte-vallentuna.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Vallentuna", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Vallentuna – flygbuller, glasval och lov",
  "description": "Fönsterbyte i Vallentuna: Arlandas påverkansområden i översiktsplanen, riktvärden för ljud inomhus, glas som dämpar buller och när nya fönster kräver lov.",
  "h1": "Fönsterbyte i Vallentuna",
  "lead": "Vallentuna ligger nära Arlanda, och flygplatsen finns med i nästan varje del av kommunens översiktsplan. För den som bor i ett hus här kan ett fönsterbyte därför handla lika mycket om ljud som om värme. Geal Entreprenad AB byter och renoverar fönster i Vallentuna tätort, Lindholmen, Kårsta och på landsbygden runt omkring och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Flygbuller, glasval och lov i Vallentuna.",
  "sections": [
    {"id": "arlanda", "anchor": "Arlanda och påverkansområdena",
     "h2": "Arlanda och de två påverkansområdena",
     "paras": [
       "Vallentunas översiktsplan beskriver Arlanda som ett riksintresse som ska skyddas mot åtgärder som påtagligt kan försvåra flygplatsens användning. Hela kommunen omfattas av flygplatsens hinderbegränsande yta, som kan innebära höjdrestriktioner för höga byggnader och objekt.",
       "För buller finns ett påverkansområde, tidigare kallat influensområde. Det omfattar dels mark som berörs eller kan beröras av en ekvivalent flygbullernivå på 55 dB(A) eller mer, dels mark där maxnivåer över 70 dB(A) förekommer mer än tre gånger per årsmedeldygn. Enligt planen har påverkansområdet minskat påtagligt inom kommunen och helt utgått från norra Frösunda.",
       "Samtidigt har ett nytt påverkansområde för lågfartsflyg tillkommit. Bakgrunden är ett villkor i flygplatsens miljötillstånd som säger att lågfartstrafik inte får flyga över tätort lägre än 1 000 meter om den maximala ljudnivån på marken överstiger 65 dBA. Områdena styr framför allt var nya bostäder kan byggas, men de visar också hur nära flyget är.",
     ],
     "aside": {"title": "Ur översiktsplanen", "items": [
       "Hela kommunen: hinderbegränsande yta", "Påverkansområde flygbuller har minskat",
       "Nytt påverkansområde för lågfartsflyg", "Norra Frösunda har utgått ur bullerområdet"]}},
    {"id": "riktvarden", "h2": "Riktvärden inomhus och vad fönstret kan göra",
     "paras": [
       "I översiktsplanens tabell över riktvärden för trafikbuller anges 30 dB(A) som ekvivalent nivå inomhus och 45 dB(A) som maximal nivå nattetid. Utomhus vid fasaden anges 60 dB(A) ekvivalent nivå för bostäder större än 35 kvadratmeter. Värdena används när nya bostäder planeras, men de ger också en bild av vad som räknas som en god ljudmiljö inne.",
       "I ett befintligt hus är fönstren ofta den svagaste delen av ytterväggen när det gäller ljud. Boverket påpekar att olika glas och glaskombinationer ger olika mycket bullerdämpning, solavskärmning och dagsljus, och att det därför lönar sig att utreda vilken typ av glas som passar huset. Boverket nämner också mindre buller utifrån som en av de nyttor som kommer när fönster förbättras eller byts på rätt sätt.",
       "Vid besöket frågar vi därför i vilka rum ljudet stör mest och åt vilket håll de vetter. Ett sovrum mot en väg eller mot flygets riktning kan behöva ett annat glas än resten av huset.",
     ],
     "aside": None},
    {"id": "tatt-vallentuna", "h2": "Tätheten avgör lika mycket som glaset",
     "paras": [
       "Ett fönster med bra ljudglas hjälper lite om luft och ljud läcker runt karmen. Boverket lyfter fram drevning och isolering mellan karm och vägg, tätningslister mellan båge och karm och bågar som hänger rakt. När ett fönster inte hänger rätt blir tätningen sämre mot karmen.",
       "Blir huset tätare behöver tilluften ses över, eftersom luft som tidigare läckt in kring fönstren kan ha varit en del av ventilationen. Boverket nämner spaltventiler i bågen eller karmen som en lösning. Ett friskluftsdon är samtidigt en öppning, så placering och typ bör väljas med ljudet i tanke, och i ett hus med mekanisk ventilation bör flödena justeras in efteråt.",
       "Ska fasaden kring fönstren lagas eller målas samtidigt finns mer under " + _L.format("fasadrenovering-vallentuna.html", "fasadrenovering i Vallentuna") + ".",
     ],
     "aside": {"title": "Där ljudet tar sig in", "items": [
       "Glaset", "Fogen mellan karm och vägg",
       "Listen mellan båge och karm", "Friskluftsdon och ventiler"]}},
    {"id": "lov-vallentuna", "h2": "Lovfritt i de flesta fall – och ritningarna i arkivet",
     "paras": [
       "Vallentuna kommun skriver att det inte krävs bygglov för nya fönster på ett en- eller tvåbostadshus, men att ändringar ska göras varsamt och anpassas till byggnadens värden. Lov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden i sig är särskilt värdefull.",
       "Krävs lov vill kommunen ha en situationsplan, fasadritningar i skala 1:100 över de fasader som berörs, en redovisning av utvändiga material och kulörer med NCS-koder och en kontrollplan. Kommunen nämner att äldre ritningar kan beställas om de finns i arkivet, och de är ofta ett bra underlag även när bytet är lovfritt, eftersom de visar fönstrens ursprungliga indelning.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett fönsterbyte i Vallentuna till",
  "steps": [
    ("Platsbesök", "Vi går igenom fönstren rum för rum och noterar var ljud och drag stör mest."),
    ("Glasval", "Ljudglas, energiglas och solskydd väljs efter rummens läge och användning."),
    ("Lovfrågan", "Vi kontrollerar om huset ligger i ett särskilt värdefullt område och beställer äldre ritningar vid behov."),
    ("Kostnadsförslag", "Ett skriftligt förslag där fönster, glas, montage och ventiler står var för sig."),
    ("Montage", "Fönstren sätts in med noggrann drevning och tätning runt karmen."),
    ("Kontroll", "Vi kontrollerar att bågarna sluter tätt och går igenom ventilationen med dig."),
  ],
  "rot_h2": "Rotavdrag för fönster och ljudglas i Vallentuna",
  "rot": [
    "Att montera bullerglas och isolerglas och att reparera eller byta ut fönster i ett småhus är rotarbete enligt Skatteverket. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Solfilm och myggnät ger inget avdrag, och material och resor räknas inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset i Vallentuna?",
  "price": [
    "Antal och storlek på fönstren, vilken ljud- och energiklass glaset ska ha, om bara vissa rum ska få ljudglas, hur mycket foder och bleck som behöver göras om och om ventilationen behöver kompletteras med nya don. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Ligger vårt hus i Vallentuna i Arlandas bullerområde?",
     "Det visar kartorna i kommunens översiktsplan. Enligt planen har påverkansområdet för flygbuller minskat påtagligt, medan ett nytt område för lågfartsflyg har tillkommit."),
    ("Hjälper det att bara byta glas i sovrummet mot flyget?",
     "Det kan göra stor skillnad i det rummet, men glaset är bara en del. Tätningen runt karmen och var friskluften kommer in påverkar också hur mycket ljud som hörs."),
    ("Vilken ljudnivå inomhus räknas som bra?",
     "Översiktsplanens tabell anger 30 dB(A) ekvivalent nivå inomhus och 45 dB(A) maximal nivå nattetid. Värdena gäller planering av nya bostäder men är en bra riktpunkt."),
    ("Ger ljudglas rotavdrag i Vallentuna?",
     "Ja. Skatteverket räknar montering av bullerglas och isolerglas i ett småhus som rotarbete. Avdraget gäller arbetskostnaden."),
    ("Kan vi få ut originalritningarna innan fönstren byts?",
     "Vallentuna kommun skriver att äldre ritningar kan beställas om de finns i arkivet. De visar ofta hur fönstren var indelade från början."),
  ],
  "sources": [
    ("Vallentuna kommun – Översiktsplan 2040 (pdf)",
     "https://vallentuna.se/download/18.63572f8619eeecafce08366/1782478377449/2.11.7%20%C3%96versiktsplan%202040.pdf"),
    ("Vallentuna kommun – Fasadändring",
     "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/behover-jag-bygglov/fasadandring"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Vill ni ha tystare fönster i Vallentuna?", "Boka ett gratis platsbesök så går vi igenom fönstren rum för rum."),
  "img": [
    ("Villa i Vallentuna från 1980-talet med nya vita fönster och rött betongtegeltak",
     "1980s Swedish one-and-a-half storey villa with light grey painted wooden panel, new white windows with narrow frames, red concrete tile gable roof, neat lawn and young birch trees, quiet suburban street, open fields in the far background, Vallentuna, overcast daylight, empty scene, no people, no aircraft, no text"),
    ("Närbild på hörnet av en ny vit fönsterbåge och karm",
     "close-up of the edge of a new white wooden window sash showing a thick triple insulated glass unit with spacer bars and rubber seals, frame corner and sealing strip visible, soft indoor daylight, workshop-clean, no people, no hands, no text, no logos"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"fonsterbyte-osteraker.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Österåker", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Österåker – varsamhet, kulturvärden och kust",
  "description": "Fönsterbyte i Österåker: kommunens frågor om husets värde, varsamhetskravet för alla hus, antikvariskt utlåtande och fönster i vind och slagregn.",
  "h1": "Fönsterbyte i Österåker",
  "lead": "Österåkers kommun skriver att även enkla, vardagliga och yngre hus kan ha kulturvärden, och att fönster hör till de detaljer som kan göra ett hus värdefullt. Samtidigt står husen i skärgården ofta öppet mot vind och regn, som sliter på fönstren. Geal Entreprenad AB byter och renoverar fönster i hela Österåker och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Varsamhet, kulturvärden och kustlägen i Österåker.",
  "sections": [
    {"id": "varsamhet-osteraker", "anchor": "Varsamhetskravet",
     "h2": "Varsamhetskravet gäller även ett hus från 1980-talet",
     "paras": [
       "På sin sida om kulturhistoriska byggnader skriver Österåkers kommun att varsamhetskravet gäller alla byggnader och alla ändringar oberoende av husets ålder. Det gäller både invändigt och utvändigt, och oberoende av om åtgärden kräver bygglov eller anmälan. Varsamheten kan enligt kommunen avse färgsättning, byggnadens proportioner och detaljer.",
       "Kommunen påpekar också att det inte bara är slott och äldre byggnader som har kulturvärden. Även enkla, vardagliga byggnader och yngre bebyggelse kan ha det. För ett fönsterbyte betyder det att frågan om indelning, profiler och kulör finns med även när huset är byggt på 1970- eller 80-talet och bytet i övrigt är lovfritt.",
       "Den som vill ha ett formellt besked kan enligt kommunen söka bygglov frivilligt, även när det inte krävs. Kommunen nämner att det kan vara en fördel om man planerar att sälja fastigheten.",
     ],
     "aside": None},
    {"id": "vardefullt-osteraker", "h2": "Är huset värdefullt? Kommunens frågor",
     "paras": [
       "Kommunen har en lista med frågor för den som vill veta om huset kan vara värdefullt. Finns det en detaljplan med skyddsbestämmelser för huset? Ligger det i eller nära ett kulturmiljöområde i Österåkerskartan? Finns huset med i en inventering eller ett kulturmiljöprogram? Har det en bevarad, tidstypisk karaktär eller bevarade byggnadsdetaljer, till exempel fönster? Svarar man ja på en eller flera frågor kan huset vara värdefullt.",
       "Om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område, eller om byggnaden är särskilt värdefull, behöver du söka bygglov för att ändra fasaden. Kommunen skriver att även små ändringar kan påverka en känslig byggnad och att Bygglovenheten bör kontaktas innan arbetet börjar.",
       "Kommunen förklarar också beteckningarna i detaljplanen: ett litet k innebär att byggnaden ska behandlas varsamt och ett litet q att den inte får rivas. Står någon av dem för huset är det ett tydligt tecken på att fönstren bör behålla sitt utseende.",
     ],
     "aside": {"title": "Kan huset vara värdefullt?", "items": [
       "Skyddsbestämmelse i detaljplanen", "Kulturmiljöområde i Österåkerskartan",
       "Med i en inventering", "Bevarade originalfönster"]}},
    {"id": "antikvarie-osteraker", "h2": "Förvanskningsförbudet och ett antikvariskt utlåtande",
     "paras": [
       "Från den 1 december 2025 skärptes reglerna för särskilt värdefulla byggnader och bebyggelseområden. Österåkers kommun skriver att det i sådana miljöer införs eller behålls en utökad lovplikt, och att förvanskningsförbudet skyddar de egenskaper och karaktärsdrag som gör bebyggelsen särskilt värdefull, både interiört och exteriört.",
       "Inför en bygglovsansökan kan en antikvarisk förundersökning behövas. Den beskriver byggnadens kulturvärden och karaktärsdrag och hur de påverkas av åtgärden. Kommunen skriver att det för mindre åtgärder kan räcka med ett enklare antikvariskt utlåtande, och att en kontrollansvarig för kulturvärden kan behövas i samband med bygglovet.",
       "Ett fönsterbyte på ett värdefullt hus är ofta en sådan mindre åtgärd. Vi tar fram mått, foton och en beskrivning av de befintliga fönstren, så att den antikvariska bedömningen har något konkret att utgå från.",
     ],
     "aside": None},
    {"id": "kust-osteraker", "h2": "Vind, regn och vatten kring fönstret",
     "paras": [
       "Boverkets energiguide råder att man innan fönstren byts utreder om det finns fuktskador i väggarna och om det befintliga eller nya fönstret behöver kompletteras med fuktskydd. På ett hus som står öppet mot en fjärd eller på en udde tittar vi därför särskilt på bröstningen, fönsterbänken och att fönsterblecket har fall ut från väggen.",
       "Boverket påminner också om underhållet: vissa material kräver mer regelbunden skötsel än andra, men framför allt bör man välja material som går att underhålla så att fönstren får lång livslängd. Ett fönster som går att skrapa, laga och måla om håller ofta längre i ett utsatt läge än ett som måste bytas när ytan har gett med sig.",
       "Behöver panelen runt fönstren ses över samtidigt finns mer under " + _L.format("fasadrenovering-osteraker.html", "fasadrenovering i Österåker") + ", och för foder och snickerier inne under " + _L.format("snickare-osteraker.html", "snickare i Österåker") + ".",
     ],
     "aside": {"title": "Vi kontrollerar", "items": [
       "Bröstningen under fönstret", "Fönsterblecket och dess fall",
       "Fogen mellan karm och vägg", "Bågarnas skick och färgsystem"]}},
  ],
  "steps_h2": "Arbetsgången vid fönsterbyte i Österåker",
  "steps": [
    ("Frågor om huset", "Vi går igenom kommunens frågor om husets värde och tittar i Österåkerskartan."),
    ("Platsbesök", "Fönster, bröstningar och bleck kontrolleras och de befintliga fönstren mäts och fotograferas."),
    ("Underlag", "Behövs lov eller ett antikvariskt utlåtande tar vi fram mått och beskrivning av fönstren."),
    ("Kostnadsförslag", "Renovering, nya fönster, glas, bleck och montage står var för sig i ett skriftligt förslag."),
    ("Montage", "Fönstren sätts in med drevning, tätning och fuktskydd under fönstret."),
    ("Genomgång", "Vi visar hur fönstren ska skötas för att klara vind och väder."),
  ],
  "rot_h2": "ROT-avdrag för fönsterarbete i Österåker",
  "rot": [
    "I ett småhus räknar Skatteverket det som rotarbete att reparera eller byta ut fönster, byta fönsterbleck och måla fönster. Avdraget gäller även ett fritidshus som du äger och använder. Det är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Material, resor och utrustning ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här påverkar priset i Österåker",
  "price": [
    "Antal fönster, om de kan renoveras eller behöver bytas, om indelning och profiler ska tillverkas efter förlaga, om underlag för lov eller antikvarisk bedömning behövs och hur mycket bröstningar och bleck som ska lagas. Hus på öarna kräver båt- eller färjeresor. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Gäller varsamhetskravet för vårt radhus från 1980-talet i Åkersberga?",
     "Ja. Österåkers kommun skriver att varsamhetskravet gäller alla byggnader och alla ändringar oberoende av husets ålder, även när bytet inte kräver bygglov."),
    ("Hur vet jag om mitt hus i Österåker räknas som värdefullt?",
     "Kommunen har en lista med frågor, bland annat om skyddsbestämmelser i detaljplanen, om huset finns i Österåkerskartans kulturmiljöområden och om det har bevarade originaldetaljer som fönster."),
    ("Vad är skillnaden mellan k och q i detaljplanen?",
     "Enligt Österåkers kommun innebär ett litet k att byggnaden ska behandlas varsamt och ett litet q att den inte får rivas."),
    ("Behövs en antikvarie för att byta fönster på ett värdefullt hus?",
     "Det kan krävas en antikvarisk förundersökning inför bygglovet. För mindre åtgärder skriver kommunen att ett enklare antikvariskt utlåtande kan räcka."),
    ("Varför ruttnar bröstningen under fönstret på vårt hus vid vattnet?",
     "Boverket råder att undersöka fuktskador i väggen innan fönstret byts och att komplettera med fuktskydd vid behov. I utsatta lägen kontrollerar vi särskilt fönsterblecket och fogarna."),
  ],
  "sources": [
    ("Österåkers kommun – Kulturhistoriska byggnader, kulturmiljöer (bygglovsguiden)",
     "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/bygglovsguiden/kulturhistoriskabyggnaderkulturmiljoer.4.367d658917909e8fc2bb42.html"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren i Österåker renoveras eller bytas?", "Boka ett gratis platsbesök så går vi igenom fönstren och husets förutsättningar."),
  "img": [
    ("Rödfärgad trävilla i Österåker med vita fönsteromfattningar nära vattnet",
     "falu red Swedish wooden villa from the early 1900s with white window surrounds and white two-pane windows with glazing bars, glazed porch, black standing-seam metal roof, pine trees and granite rocks, calm Baltic inlet in the background, Österåker archipelago, soft daylight, empty scene, no people, no text"),
    ("Fönsterbleck och bröstning under ett vitt träfönster i en rödfärgad panel",
     "close-up of the lower part of a white wooden window in a falu red painted vertical board facade, a grey metal window sill flashing sloping outward, the boards under it slightly weathered, water drops on the flashing after rain, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ NORRTÄLJE
"fonsterbyte-norrtalje.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Norrtälje", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Norrtälje – Roslagens hus, bruk och bidrag",
  "description": "Fönsterbyte i Norrtälje: kulturmiljöutredningarna, tvåluftsfönster i Herräng, lov inom och utanför detaljplan och bidrag som inte gäller fritidshus.",
  "h1": "Fönsterbyte i Norrtälje",
  "lead": "Norrtälje kommun har 26 kulturmiljöer av riksintresse, och i kommunens egna utredningar återkommer råden om fönster: behåll de gamla så långt det går. Här finns också drygt 26 000 fritidshus, och det påverkar vilka bidrag som går att få. Geal Entreprenad AB byter och renoverar fönster i Norrtälje stad, Rimbo, Hallstavik och i skärgården och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Roslagens hus, bruksorter och bidrag i Norrtälje.",
  "sections": [
    {"id": "riksintressen-norrtalje", "anchor": "Riksintressen",
     "h2": "26 riksintressen och en utredning för de flesta av dem",
     "paras": [
       "I Norrtälje kommun finns 26 områden som Riksantikvarieämbetet pekat ut som riksintressen för kulturmiljövården. År 2011 beslutade kommunen att göra kulturhistoriska utredningar av 22 av dem, för att få ett bättre beslutsunderlag och för att informera dem som bor där. Utredningarna omfattar skärgårdsmiljöer som Arholma, landsbygd som Länna och Vagnåla och industrimiljöer som Hallstavik, Herräng och Skebobruk. Utredningen för Herräng avslutas med tips och råd för den som bor där.",
       "För Norrtälje stad finns ett eget bevarandeprogram. Kommunfullmäktige fastställde programmet för stadskärnan 1981, och 2008 beslutade bygg- och miljönämnden att det behövde uppdateras. Det är tänkt som vägledning för hur den del av stadskärnan som ligger inom riksintresset ska bevaras och vårdas.",
       "Innan vi föreslår nya fönster på ett hus i ett av de här områdena läser vi därför vad utredningen säger om husen just där.",
     ],
     "aside": {"title": "Exempel på utredningsområden", "items": [
       "Skärgård: Arholma, Backbyn", "Farleder: Grisslehamn, Väddö kanal",
       "Landsbygd: Länna, Vagnåla", "Industri: Hallstavik, Herräng"]}},
    {"id": "herrang", "h2": "Tre rutor i varje luft – fönstren i Herräng",
     "paras": [
       "Kulturmiljöutredningen för Herräng från 2016 beskriver gårdarna väster om Blåkaren, från sent 1800-tal och tidigt 1900-tal, med rödfärgad stående panel och vita snickerier. Fönstren är ofta träspröjsade tvåluftsfönster indelade i tre rutor i varje luft. Om egnahemmen från brukets senare tid skriver utredningen att stilrena tvåluftsfönster hör till bostäderna.",
       "Råden är tydliga. Gamla fönster bör bevaras i så stor utsträckning som möjligt, eftersom ett byte till moderna fönster ofta kan förändra hela fasadens gestaltning, och renovering av befintliga fönster är att föredra. Utredningen konstaterar att äldre fönstersnickerier ofta är utförda av trä med hög kvalitet och att omfattningar och snickerier målas med linoljefärg.",
       "Utredningen visar också hur det kan bli fel. Om en ombyggd ekonomibyggnad skriver den att nya pivåfönster med planglas i de befintliga öppningarna förtar en del av upplevelsen av en autentisk byggnad. Även när öppningarna är kvar kan alltså fönstertypen ändra intrycket.",
     ],
     "aside": {"title": "Råden i korthet", "items": [
       "Bevara gamla fönster så långt det går", "Renovera hellre än byt",
       "Linoljefärg på snickerier och omfattningar", "Ny fönstertyp kan ändra hela fasaden"]}},
    {"id": "lov-norrtalje", "h2": "Lov inom och utanför detaljplan",
     "paras": [
       "Norrtälje kommuns sida om fasadändring skiljer på läget. Inom detaljplan krävs inget bygglov för fasadändringar på ett en- eller tvåbostadshus, utom när detaljplanen har utökad lovplikt. Utanför detaljplan krävs lov om fastigheten ligger inom ett område som är särskilt värdefullt. I kommunens karta går det att kontrollera om fastigheten ligger i ett detaljplanerat område och om den är särskilt värdefull.",
       "Kommunen ger allmän rådgivning men skriver att den inte kan bedöma enskilda åtgärder via e-post eller telefon. Den som vill ha ett bindande besked om ett fönsterbyte kräver lov kan ansöka om frivilligt lov, så att byggnadsnämnden gör en formell prövning.",
       "Är huset ett gammalt sommarhus som ska bli åretruntbostad hör fönstren ofta ihop med tak och väggar. Läs mer under " + _L.format("takbyte-norrtalje.html", "takbyte i Norrtälje") + " och " + _L.format("snickare-norrtalje.html", "snickare i Norrtälje") + ".",
     ],
     "aside": None},
    {"id": "bidrag-norrtalje", "h2": "Bidrag för nya fönster – men inte till fritidshuset",
     "paras": [
       "Boverkets bidrag för energieffektivisering i småhus kan sökas för byte av fönster eller dörrar och för tilläggsglasrutor till befintliga fönster. Det gäller den som äger och stadigvarande bor i ett småhus med värdeår före 1990 som inte är anslutet till fjärrvärme. Bidraget gäller inte ett fritidsboende, och huset ska normalt vara den adress där du är folkbokförd.",
       "Bidraget täcker högst 30 procent av materialkostnaden, och produkterna ska klara kraven på energimärkning. Ansökan ska lämnas inom sex månader från att arbetet påbörjades, och det är länsstyrelsen som handlägger. Eftersom bidraget bara gäller material kan rotavdrag ges för arbetskostnaden i samma jobb.",
       "För fritidshuset finns alltså inget sådant bidrag, men rotavdraget gäller även där. Kommunen räknar med drygt 26 000 fritidshus, så det är en skillnad som är bra att känna till innan fönstren beställs.",
     ],
     "aside": {"title": "Bidraget i korthet", "items": [
       "Permanentbostad, inte fritidshus", "Värdeår före 1990, ingen fjärrvärme",
       "Högst 30 procent av materialet", "Ansökan inom sex månader"]}},
  ],
  "steps_h2": "Så planerar vi ett fönsterbyte i Norrtälje",
  "steps": [
    ("Läget först", "Vi tar reda på om huset ligger inom detaljplan, i ett särskilt värdefullt område eller i ett riksintresse."),
    ("Platsbesök", "Fönstren mäts upp, indelningen dokumenteras och bågarnas skick bedöms."),
    ("Renovera eller byta", "Där bågarna är friska föreslår vi renovering, annars nya fönster med samma indelning."),
    ("Kostnadsförslag", "Material och arbete redovisas var för sig, vilket också behövs för bidrag och rotavdrag."),
    ("Utförande", "Fönstren renoveras eller byts, och snickerierna målas med den färgtyp som passar huset."),
    ("Avslutning", "Vi går igenom arbetet med dig och lämnar de uppgifter som behövs till ansökan."),
  ],
  "rot_h2": "ROT-avdrag för fönster i Norrtälje",
  "rot": [
    "Rotavdraget gäller både villan och fritidshuset, så länge du äger det och använder det som bostad. Att reparera eller byta ut fönster, montera isolerglas och måla fönster räknas som rotarbete. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Geal drar avdraget direkt på fakturan och redovisar material och arbete var för sig.",
  ],
  "price_h2": "Vad påverkar priset i Norrtälje?",
  "price": [
    "Om fönstren kan renoveras eller behöver bytas, om spröjs och indelning ska tillverkas efter förlaga, vilken färgtyp snickerierna ska ha, antal fönster och avståndet till huset. I skärgården påverkar båttransporter och väder planeringen. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur var fönstren indelade på de äldre gårdarna kring Herräng?",
     "Enligt kommunens kulturmiljöutredning är fönstren ofta träspröjsade tvåluftsfönster med tre rutor i varje luft, på hus med rödfärgad stående panel och vita snickerier."),
    ("Kan vi få bidrag för nya fönster i sommarstugan i Roslagen?",
     "Nej, Boverkets bidrag för energieffektivisering gäller bara hus som används som permanentbostad. Rotavdrag för arbetet går däremot att få även för ett fritidshus du äger."),
    ("Behövs bygglov för nya fönster på ett hus utanför detaljplan i Norrtälje?",
     "Bara om fastigheten ligger inom ett område som är särskilt värdefullt. Det kan kontrolleras i kommunens karta."),
    ("Kan Norrtälje kommun svara på mejl om vårt fönsterbyte kräver lov?",
     "Kommunen ger allmän rådgivning men bedömer inte enskilda åtgärder via e-post eller telefon. För ett bindande besked kan du söka frivilligt lov."),
    ("Går det att kombinera energibidraget med rotavdrag?",
     "Ja. Bidraget gäller bara materialkostnaden, så rotavdrag kan ges för arbetskostnaden i samma jobb."),
  ],
  "sources": [
    ("Norrtälje kommun – Kulturmiljöutredning nr 21: Herräng (2016, pdf)",
     "https://www.norrtalje.se/globalassets/dokument/dokument-kultur--fritid/dokument-kultur/dokument-riksintressen-i-norrtalje-kommun/herrang.pdf"),
    ("Norrtälje kommun – Bevarandeprogram för Norrtälje stad",
     "https://www.norrtalje.se/info/trafik-gator-parker/bevarandeprogram-for-norrtalje-stad/"),
    ("Norrtälje kommun – Fasadändring",
     "https://www.norrtalje.se/sjalvservice/bygga-bo-miljo/fasadandring/"),
    ("Norrtälje kommun – Fakta och statistik om landsbygd och skärgård",
     "https://www.norrtalje.se/info/bygga-bo-miljo/norrtalje-vaxer/landsbygd-skargard/fakta-och-statistik/"),
    _BV_BIDRAG, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren i Roslagen renoveras eller bytas?", "Boka ett gratis platsbesök så går vi igenom fönstren, lovfrågan och vad som ger bidrag och avdrag."),
  "img": [
    ("Rödfärgad gård i Roslagen med vita träspröjsade tvåluftsfönster",
     "late 1800s Swedish two-storey farmhouse with falu red vertical board panel, white corner boards and white window surrounds, white wooden two-pane casement windows each sash divided into three panes by glazing bars, low pitched roof with grey standing-seam metal, open meadow and birch trees, Roslagen Norrtälje, summer daylight, empty scene, no people, no text"),
    ("Äldre spröjsad fönsterbåge med flagnande vit färg i en rödfärgad vägg",
     "close-up of a restored old white painted wooden window sash with three small panes divided by glazing bars, fresh linseed putty and paint, set in a falu red painted board wall, soft daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"fonsterbyte-jarfalla.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Järfälla", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Järfälla – brukets villor, radhus och 70-tal",
  "description": "Fönsterbyte i Järfälla: Bolinders arbetarvillor, radhus där varje fönster syns i hela raden, 70-talets treglasfönster, PCB i fogar och inbrottsskydd.",
  "h1": "Fönsterbyte i Järfälla",
  "lead": "I Järfälla står arbetarvillor från Bolinders tid i Kallhäll inte långt från radhuslängor och kedjehus från 1950-, 60- och 70-talen. Fönstren säger mycket om när husen byggdes, och ett byte syns ofta i hela raden. Geal Entreprenad AB byter och renoverar fönster i Jakobsberg, Kallhäll, Viksjö, Barkarby och övriga Järfälla och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Bruksvillor, radhus och 70-talsfönster i Järfälla.",
  "sections": [
    {"id": "kallhall-fonster", "anchor": "Kallhäll",
     "h2": "Glasvillan och de andra arbetarvillorna i Kallhäll",
     "paras": [
       "Järfällas kulturmiljöplan berättar att Bolinders lät bygga de första femton arbetarvillorna i Kallhäll 1907–1913, och att ytterligare sex tillkom under 1920-talet. Villorna låg på båda sidor om järnvägen och varje hus hade fyra eller fler lägenheter. Två av dem finns kvar: Basvillan, där flera förmän bodde, och Glasvillan, som fått sitt namn av de stora fönsterpartierna. Båda är klädda med locklistpanel och har i stort sett kvar sitt ursprungliga utseende.",
       "Planen ger också ett exempel på motsatsen. Kallhälls gamla skola hade stora och höga småspröjsade fönster mot söder för att skolsalarna skulle få så mycket ljus som möjligt. Under 1950-talets senare del förenklades fasaden kraftigt: de spröjsade fönstren gjordes mindre och byttes mot perspektivfönster. Byggnaden har sedan rivits.",
       "Exemplen visar att fönstren kan vara det som ger ett hus dess namn, och att ett byte kan förändra en byggnad mer än någon annan enskild åtgärd.",
     ],
     "aside": None},
    {"id": "radhus-jarfalla", "h2": "Radhus och kedjehus: ett fönster syns i hela raden",
     "paras": [
       "Flera av Järfällas småhusområden är byggda i grupper. Kulturmiljöplanen beskriver till exempel rad- och kedjehusen kring Skogsvägen och Toppvägen i Jakobsberg, som ger en god bild av det tidiga 1960-talets småhusbyggande och där flera olika byggnadsfirmor gav området ett varierat uttryck. Planen skriver att fasad- och takmaterial och färgsättning är viktiga att behålla där, och att lovplikten därför bör utökas vid en eventuell detaljplaneändring.",
       "Järfälla kommun skriver att det inte krävs bygglov för fasadändringar på ett en- eller tvåbostadshus, och nämner nya fönster som exempel på en fasadändring. Undantaget är särskilt värdefulla byggnader och områden och detaljplaner med utökad lovplikt. Lovfria fasadändringar ska ändå stämma överens med detaljplanen eller vara en liten avvikelse som inte motverkar planens syfte, och de ska utföras varsamt.",
       "I en radhuslänga där alla hus har samma fönster blir ett hus med annan indelning eller kulör tydligt. Vi tar därför reda på vilken fönstertyp längan hade från början och föreslår fönster som passar in. Den som vill vara säker kan söka frivilligt bygglov.",
     ],
     "aside": {"title": "I en radhuslänga", "items": [
       "Samma indelning som grannarna", "Samma kulör på karm och båge",
       "Fönstret i samma liv i fasaden", "Kontrollera detaljplanen"]}},
    {"id": "sjuttiotal-jarfalla", "h2": "Treglasfönster från 1970-talet och gamla fogmassor",
     "paras": [
       "Boverket nämner en typ av fönster som ofta behöver bytas: treglasfönster från 1970-talet där glaskassetten har förlorat sin funktion och där monteringen i instickskarmar ger betydande energiförluster. Ett byte kan enligt Boverket också återställa utseendet på en byggnad som har förvanskats.",
       "Innan gamla fönster tas ur bör man enligt Boverket undersöka om fogmassorna innehåller PCB eller asbest, som är saneringspliktiga, och förbereda rätt sanering och avfallshantering. Även kitt kan innehålla asbest och ska då hanteras enligt arbetsmiljöreglerna. För hus från 1950-, 60- och 70-talen är det en fråga som behöver ställas tidigt.",
       "Fönster kan bytas året runt. Boverket nämner fönstertält vid kyla och råder att byta stegvis på vintern så att huset inte kyls ner. Ska fasaden kring fönstren målas om samtidigt, läs mer under " + _L.format("malare-jarfalla.html", "målare i Järfälla") + ".",
     ],
     "aside": None},
    {"id": "sakerhet-jarfalla", "h2": "Inbrottsskydd, brandklass och utrymning",
     "paras": [
       "Boverkets checklista för fönsterbyten handlar inte bara om energi. Den råder att bestämma vilken säkerhetsklassning fönster och dörrar ska ha, eftersom det är en viktig del av inbrottsskyddet, och påpekar att äldre fönster kan behöva förbättras eftersom de inte följer dagens tekniska standarder.",
       "Har huset brandklassade fönster ska den nya lösningen ha minst samma klass. Boverket råder också att tänka igenom hur huset ska utrymmas vid brand, eftersom tekniska detaljer kan göra det lättare eller svårare att ta sig ut genom ett fönster.",
       "Under själva bytet kan ett fönsterhål behöva stå öppet en tid i väntan på det nya fönstret. Boverket föreslår att man planerar inbrottsskyddet även för den tiden. Vi byter därför fönster i den takt som gör att huset kan stängas varje kväll.",
     ],
     "aside": {"title": "Bestäm innan beställning", "items": [
       "Säkerhetsklass mot inbrott", "Brandklass där det behövs",
       "Vilka fönster som är utrymningsväg", "Hur huset stängs under bytet"]}},
  ],
  "steps_h2": "Så går ett fönsterbyte i Järfälla till",
  "steps": [
    ("Platsbesök", "Vi bedömer fönstren, tar reda på fönstertypen i området och kontrollerar fogar och kitt."),
    ("Detaljplan", "Vi kontrollerar om detaljplanen eller områdets värde påverkar vilket fönster som får sättas in."),
    ("Val av fönster", "Indelning, kulör, glas, säkerhetsklass och eventuell brandklass bestäms."),
    ("Kostnadsförslag", "Fönster, montage, sanering av fogmassor och foder redovisas var för sig."),
    ("Byte i etapper", "Fönstren byts i den takt som gör att huset kan stängas och hållas varmt."),
    ("Genomgång", "Vi kontrollerar funktion och tätning och går igenom fönstren med dig."),
  ],
  "rot_h2": "Rotavdrag för fönsterbyte i Järfälla",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att reparera eller byta ut fönster, montera isolerglas och bullerglas och byta fönsterbleck. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Du ska äga bostaden när arbetet utförs. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Järfälla?",
  "price": [
    "Antal och storlek på fönstren, om fönstertypen måste anpassas till resten av radhuslängan, om fogmassor eller kitt behöver saneras, vilken säkerhets- och brandklass som krävs och hur mycket foder och bleck som ska göras om. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför heter Glasvillan i Kallhäll så?",
     "Enligt Järfällas kulturmiljöplan har den fått sitt namn efter de stora fönsterpartierna. Den är en av två kvarvarande arbetarvillor som Bolinders lät bygga."),
    ("Får vi välja en annan fönsterindelning i vårt radhus i Jakobsberg?",
     "Bytet är normalt lovfritt, men det ska stämma med detaljplanen och göras varsamt. I en länga där alla hus har samma fönster syns en annan indelning tydligt, och i särskilt värdefulla områden krävs lov."),
    ("Kan det finnas PCB i fogarna runt våra fönster från 1970-talet?",
     "Det ska undersökas innan fönstren tas ur. Boverket påpekar att gamla fogmassor kan innehålla PCB eller asbest och att även kitt kan innehålla asbest."),
    ("Vilken säkerhetsklass bör nya fönster på bottenvåningen ha?",
     "Boverket råder att bestämma säkerhetsklass innan beställningen, eftersom den är en viktig del av inbrottsskyddet. Vi går igenom vilka fönster som är mest utsatta vid besöket."),
    ("Kan fönstren bytas i Järfälla mitt i vintern?",
     "Ja. Boverket skriver att fönster kan bytas oavsett årstid, till exempel med fönstertält, och att bytet bör göras stegvis så att huset inte kyls ner."),
  ],
  "sources": [
    ("Järfälla kommun – Kulturmiljöplan: Kallhäll (pdf)",
     "https://www.jarfalla.se/download/18.68e7a727168e12dd179a407f/1550245859848/kulturmiljoplan-kallhall.pdf"),
    ("Järfälla kommun – Kulturmiljöplan: Jakobsberg (pdf)",
     "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4080/1550245872956/kulturmiljoplan-jakobsberg.pdf"),
    ("Järfälla kommun – Fasadändring",
     "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/vadvilldubyggaellerandra/fasadandring.4.1966aa14175c8663c9323310.html"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren i Järfälla bytas?", "Boka ett gratis platsbesök så går vi igenom fönstren, detaljplanen och säkerheten."),
  "img": [
    ("Radhuslänga från 1960-talet i Järfälla med ljus locklistpanel och likadana fönster",
     "long row of early 1960s Scandinavian two-storey terraced houses, light grey-white painted vertical wooden board-and-batten facades, identical simple white two-pane windows in the same positions on every unit, low pitched gable roof of red clay tiles without chimneys, small front gardens, a shared open lawn with birch trees in front, Jakobsberg Järfälla Sweden, overcast daylight, empty scene, no people, no cars, no text"),
    ("Ett äldre brunt treglasfönster från 1970-talet med immigt glas mellan rutorna",
     "close-up of an old 1970s brown wooden triple-glazed window with a worn inset frame and fogged glass between the panes, mounted in a light rendered wall, daylight, no people, no hands, no text"),
  ],
  "related": [],
},

}
