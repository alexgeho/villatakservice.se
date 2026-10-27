# -*- coding: utf-8 -*-
"""Köksrenovering – ortsidor v10: Ekerö, Norrtälje, Hägersten, Sundbyberg, Kista, Södermalm (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
  Ekerö kommun (Vad vill du bygga: eldstad, kamin och rökkanal, vatten och avlopp; Sotning, brandskydd och
  fyrverkerier: imkanaler; Elda inomhus och utomhus; Eget dricksvatten; Gröna påsen och matavfall; Närsorterat),
  Norrtälje kommun (Eldstad och rökkanal, självservice; Tidsintervall sotning och brandskyddskontroll;
  Brandskyddskontroll av eldstad; Lovbefriade åtgärder; Landsbygd och skärgård – fakta och statistik),
  Myndigheten för civilt försvar (Förvara gasol hemma; Gasol i hemmet och på fritiden), Stadsmuseet via
  Stockholmskällan (Stockholms Spår: Västertorp, Fruängen, Kista), Stockholms stad (Områdesfakta 2025: Västertorp,
  Fruängen, Västberga, Kista, Akalla, Södermalms stadsdelsområde; bygglov.stockholm: Flytta kök eller badrum,
  Stadsmuseets kulturhistoriska klassificering; Översiktsplanen – riksintressen, pdf), Sundbybergs stad (Miljöprogram
  Duvbo 2022/2024; bygglovsguiden: Fasadändring, Tillbyggnad – bygglovsbefriad, OVK), Driva Gas/Driva Gasnät
  (Gasinstallation; Kundservice; Namnbyte juni 2026), Energigas Sverige (Gassäkerhetsanvisningar för installation
  av gasapparater i hushåll, pdf), Lantmäteriverkets föreskrifter LMVFS 2007:3 (via lagen.nu), Boverket (Lista med
  PBL-ändringar 1 december 2025; Risker med asbest i byggnader), Arbetsmiljöverket (Tillstånd för rivning av
  asbest), Elsäkerhetsverket (Vad får jag göra själv med el?), riksdagen.se (bostadsrättslagen 7 kap. 7 och 12 §§)
  och Skatteverket (Så fungerar rotavdraget; Ger arbetet rätt till rotavdrag?).
Strukna (ej verifierade eller oklara i källan): Ekerös egen bedömning av anmälan för köksfläkt (ingen kommunsida
hittad – texten hänvisar till Boverket), vilka hus på Ekerö som har vedspis eller egen brunn, hur vanliga gasol-
och vedspisar är i Norrtäljes fritidshus, att Västertorps och Fruängens kök har asbest (bara Boverkets
tidsintervall används), vilka byggherrar som byggde husen i Västertorp, hur radhusen i Kista och Akalla är byggda
(plan, stammar, fasadmaterial), att Kistas kök från 1970-talet har för få elgrupper, exakt vad "lägenhet utan kök"
i områdesfakta omfattar (texten återger bara registrets definitioner bredvid siffran), hur många lägenheter på
Södermalm som har gasspis, om Duvbos utökade lovplikt fortfarande är avgiftsfri utöver det miljöprogrammet anger,
uppgifter om enskilda småhus på Södermalm. Inga priser, garantier, omdömen, egna uppdrag eller cert.
Kritikpass 2026-10-25: "radhus" i Kista ersatt med "småhus" (områdesfakta anger bara småhus), Duvbo-programmets
uppgift att ärenden inom utökad lovplikt är kostnadsfria struken (stadens nuvarande sidor bekräftar inte), Skatteverkets
gräns flytta/byta avloppsrör kontra dra ledningar i bostadsrätt struken (oklar).
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py."""

_L = '<a class="text-link" href="{0}">{1}</a>'

_SKV = ("Skatteverket – Så fungerar rotavdraget",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV2 = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_BOV_PBL = ("Boverket – Lista med PBL-ändringar som trädde i kraft den 1 december 2025",
            "https://www.boverket.se/sv/om-boverket/boverkets-uppdrag/aktuella-regeringsuppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/")
_BOV_ASB = ("Boverket – Risker med hantering av asbest i byggnader",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_AV_ASB = ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest",
           "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614)",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_ELS = ("Elsäkerhetsverket – Vad får jag göra själv med el?",
        "https://www.elsakerhetsverket.se/privatpersoner/detta-far-du-gora-sjalv-med-el/vad-far-jag-gora-sjalv-med-el")
_STH_FLYTT = ("Stockholms stad – Flytta kök eller badrum",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/flytta-kok-eller-badrum/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_STH_RIKS = ("Stockholms stad – Riksintressen i översiktsplanen (pdf)",
             "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SSM = "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_{0}.pdf"
_EK = "https://www.ekero.se/bygga-bo-miljo/"
_NT = "https://www.norrtalje.se/info/trygghet-sakerhet/raddningstjansten/"
_SB = "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/"

PAGES_TJ = {

# ------------------------------------------------------------------ EKERÖ
"koksrenovering-ekero.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Ekerö", "svc_label": "Köksrenovering",
  "title": "Köksrenovering på Ekerö – vedspis, brunn och sortering",
  "description": "Köksrenovering på Ekerö: anmälan av vedspis och kakelugn, köksfläkt och sotning, vatten från egen brunn och plats för nya sopsorteringen.",
  "h1": "Köksrenovering på Ekerö",
  "lead": "På Mälaröarna kan köket stå i ett hus med egen eldstad eller egen brunn, och med de nya sorteringsreglerna ska fler fraktioner sorteras ut hemma. Geal Entreprenad AB bygger om kök i villor och fritidshus på Ekerö, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Vedspis, egen brunn och nya sopsorteringen.",
  "sections": [
    {"id": "vedspis", "anchor": "Vedspis och kakelugn",
     "h2": "Vedspis eller kakelugn i köket kräver anmälan",
     "paras": [
       "Ekerö kommun skriver att den som vill installera eller göra en större ändring av en eldstad, braskamin, öppen spis eller kakelugn ska göra en anmälan till bygglovsenheten. Det gäller också när en spisinsats sätts in eller byts i en befintlig öppen spis, och när man byter bränsle i husets huvudsakliga värmekälla.",
       "Till anmälan hör enligt kommunen en planritning där eldstadens placering är markerad, en fasadritning med skorstenen eller rökkanalen inritad, en kontrollplan och ett typgodkännande, en produktbeskrivning eller CE-märkning. Är anmälan komplett kommer beslutet inom fyra veckor, och med beslutet följer startbeskedet. När installationen är klar skickar man in sotarintyg, den ifyllda kontrollplanen och en ansökan om slutbesked. Eldstaden får inte användas innan slutbeskedet har kommit.",
       "För oss styr det ordningen i bygget. Skåp, bänkskiva och väggbeklädnad runt en vedspis planeras efter de avstånd som tillverkaren anger, och eldstadens plats bestäms innan köksinredningen mäts in. En skorsten på taket kräver inget bygglov enligt kommunen, men en rökkanal längs fasaden kan behöva bygglov för fasadändring. Mer om taket kring skorstenen finns under " + _L.format("takrenovering-ekero.html", "takrenovering på Ekerö") + ".",
     ],
     "aside": {"title": "Anmälan av eldstad", "items": [
       "Planritning med eldstaden", "Fasadritning med skorsten",
       "Kontrollplan och produktblad", "Sotarintyg före slutbesked"]}},
    {"id": "flakt-sotning", "h2": "Köksfläkten och sotningen på Mälaröarna",
     "paras": [
       "Sotningen i kommunen är ett uppdrag för Södertörns brandförsvarsförbund, som har upphandlat en sotare som skickar brev när det är dags. Om köksfläkten skriver kommunen att kravet på att inspektera imkanaler inte längre finns, eftersom risken för brand eller brandspridning genom dem är mycket låg.",
       "Boverket påpekar dock i sin genomgång av lagändringarna från den 1 december 2025 att det krävs anmälan för vissa tekniska installationer, till exempel vatten, avlopp och ventilation. En spisfläkt som byts mot en likvärdig på samma plats är något annat än en ny kanal genom vindsbjälklaget, och det reder vi ut innan fläkten väljs.",
     ],
     "aside": None},
    {"id": "brunn", "h2": "Ny blandare och vatten från egen brunn",
     "paras": [
       "Kommunen konstaterar att den som har eget avlopp för det mesta också har eget dricksvatten, och att brunnsägaren själv ansvarar för vattnets kvalitet och för att hålla brunnen i bra skick. Livsmedelsverket rekommenderar enligt kommunen att brunnsvattnet kontrolleras minst vart tredje år, och delar fler än två fastigheter på brunnen är det bra att testa minst en gång om året.",
       "Ett nytt kök är ett bra tillfälle att ta ett prov. Visar svaret att vattnet behöver behandlas påverkar det vad som ska rymmas under diskbänken, och det är enklare att planera skåpet för ett filter innan stommen monteras än efteråt.",
       "Har fastigheten kommunalt vatten och avlopp är det Roslagsvatten som ansvarar för det, och en anmälan ska skickas dit i god tid om en byggnad ska anslutas. Med eget avlopp är frågan en annan: kommunen skriver att den som bygger om så att det blir mer avloppsvatten kan behöva söka tillstånd eller anmäla ändring av den enskilda avloppsanläggningen. Om vattnet i badrummet kan du läsa under " + _L.format("badrumsrenovering-ekero.html", "badrumsrenovering på Ekerö") + ".",
     ],
     "aside": {"title": "Har du egen brunn?", "items": [
       "Prov minst vart tredje år", "Oftare om brunnen delas",
       "Provsvaret till kommunen", "Plats för filter under diskbänken"]}},
    {"id": "sortering", "h2": "Plats för fler sopfraktioner under diskbänken",
     "paras": [
       "I dag lägger hushållen på Ekerö matavfallet i Gröna påsen, som slängs i den vanliga soptunnan och sorteras ut maskinellt. Kommunen skriver att den gröna plastpåsen ersätts av en brun papperspåse när de nya kärlen kommer. Då läggs matavfallet i den bruna påsen och påsen direkt i kärlets fack för matavfall, och den bruna påsen ska inte läggas i en plastpåse.",
       "Bakgrunden är nya regler om fastighetsnära insamling av förpackningar, som enligt kommunen ska gälla senast 2027 och kallas Närsorterat. Matavfall, restavfall och förpackningar av papper, plast, metall och glas ska sorteras ut nära bostaden. Roslagsvatten sköter kommunens sophantering sedan årsskiftet 2024/2025.",
       "För köket betyder det fler fraktioner att hitta plats för. Vi föreslår att sorteringen planeras som en egen utdragslåda under diskbänken, med ett luftigt fack för papperspåsen, och att skåpet bredvid tar förpackningarna om utrymmet räcker. Det är enklare att bestämma på ritningen än att bygga om när de nya kärlen har kommit. Ska väggarna målas i samma veva, se " + _L.format("malare-ekero.html", "målare på Ekerö") + ", och om planering i stort på sidan om " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till på Ekerö",
  "steps": [
    ("Platsbesök", "Vi går igenom kök, eldstad, vattenintag och avlopp och tar reda på om huset har kommunalt vatten eller egen brunn."),
    ("Eldstad och anmälan", "Ska en vedspis eller kakelugn in tar vi fram underlaget till anmälan innan inredningen ritas."),
    ("Skriftligt kostnadsförslag", "Rivning, snickeri, el och VVS står som egna poster, och arbete skiljs från material."),
    ("Rivning och installationer", "Gamla skåp tas bort och rör, el och fläkt dras enligt den nya planen."),
    ("Montering", "Stomme, sorteringslådor, bänkskiva och vitvaror monteras."),
    ("Genomgång", "Vi provar fläkt, blandare och vitvaror och går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för köket på Ekerö",
  "rot": [
    "I ett småhus räknar Skatteverket det som rotarbete att montera fast köksinredning och installera vitvaror i samband med en omfattande renovering, att modernisera elen och byta uttag och att installera blandare och kranar. Även att installera och reparera braskaminer och att mura och reparera skorstenar och kakelugnar ger avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Du ska äga bostaden och helt eller delvis bo i den, och ett fritidshus som du själv använder räknas. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök på Ekerö?",
  "price": [
    "Mest avgör om köket byggs om på samma plats eller om vatten, avlopp och fläkt flyttas, och om en eldstad ska in. En vedspis lägger till anmälan, skorstensarbete och mer anpassning av skåpen runt den. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi göra en anmälan för en vedspis i köket på Ekerö?",
     "Ja. Kommunen kräver anmälan för att installera eller väsentligt ändra en eldstad, och vedspisen får inte användas förrän slutbesked har getts, efter att sotarintyg och ifylld kontrollplan har skickats in."),
    ("Måste imkanalen från köksfläkten inspekteras på Ekerö?",
     "Nej. Kommunen skriver att kravet på att inspektera imkanaler har tagits bort, eftersom risken för brand genom dem är mycket låg. Eldstäder och skorstenar sotas däremot enligt kommunens ordning."),
    ("Hur ofta bör vi ta vattenprov när köket på Ekerö har egen brunn?",
     "Livsmedelsverket rekommenderar minst vart tredje år, enligt kommunen, och minst en gång om året om fler än två fastigheter delar brunnen. Kommunen vill ha en kopia av provsvaret."),
    ("Vad händer med Gröna påsen när sorteringen i köket ändras?",
     "Kommunen skriver att den gröna plastpåsen ersätts av en brun papperspåse när de nya kärlen kommer. Den bruna påsen läggs direkt i kärlets fack för matavfall och inte i en plastpåse."),
    ("Kan ett nytt kök i fritidshuset på Ekerö påverka det egna avloppet?",
     "Ja, om ombyggnaden ger mer avloppsvatten. Kommunen skriver att man då kan behöva söka tillstånd eller anmäla ändring av den enskilda avloppsanläggningen."),
  ],
  "sources": [
    ("Ekerö kommun – Vad vill du bygga? (eldstad, kamin och rökkanal)", _EK + "bygga-nytt-andra-eller-riva/vad-vill-du-bygga"),
    ("Ekerö kommun – Sotning, brandskydd och fyrverkerier", _EK + "sotning-brandskydd-och-fyrverkerier"),
    ("Ekerö kommun – Eget dricksvatten", _EK + "vatten-och-avlopp/eget-dricksvatten"),
    ("Ekerö kommun – Gröna påsen och matavfall", _EK + "avfall-och-atervinning/sopsortering-och-kallsortering/grona-pasen-och-matavfall"),
    ("Ekerö kommun – Närsorterat, nya regler om sopsortering", _EK + "avfall-och-atervinning/narsorterat"),
    _BOV_PBL, _SKV, _SKV2,
  ],
  "cta": ("Ska köket på Ekerö byggas om?", "Boka ett gratis platsbesök, så går vi igenom eldstad, vatten och sortering på plats."),
  "img": [
    ("Ljust lantligt kök med vit vedspis och träbänkskiva i en villa på Ekerö",
     "bright renovated country kitchen in a Swedish wooden villa on Ekerö in Lake Mälaren, white enamelled cast-iron wood-burning kitchen stove on a stone hearth beside light grey-green painted cabinets, oak worktop, small-paned window looking out on pine trees and a glimpse of the lake, wide pine floorboards, soft daylight, no people"),
    ("Kök med svarta underskåp, öppna hyllor och vitt kakel",
     "close-up of an open pull-out drawer under a kitchen sink in a newly renovated Scandinavian kitchen, several separate bins for food waste with a brown paper bag, plastic, paper and metal packaging, white plumbing trap and shut-off valve visible behind, clean and bright, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ NORRTÄLJE
"koksrenovering-norrtalje.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Norrtälje", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Norrtälje – gasol, vedspis och gäststuga",
  "description": "Köksrenovering i Norrtälje: gasolspisen och flaskan i köksskåpet, vedspisens sotning och brandskyddskontroll och pentry i en lovfri gäststuga.",
  "h1": "Köksrenovering i Norrtälje",
  "lead": "Kommunen har drygt 26 000 fritidshus, och ungefär en fjärdedel av dem som använder husen vistas i kommunen större delen av året. Ett kök som byggdes för sommaren ska då fungera även när det är kallt, och har stugan en gasolspis eller en vedspis finns det regler för båda. Geal Entreprenad AB bygger om kök i fritidshus och villor i Norrtälje kommun, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Gasolspis, vedspis och pentry i gäststugan.",
  "sections": [
    {"id": "gasol", "anchor": "Gasol i köket",
     "h2": "Gasolspisen och flaskan i köksskåpet",
     "paras": [
       "Myndigheten för civilt försvar, MCF, räknar villa, radhus och fritidshus till samma grupp när det gäller brandfarlig gas. I bostaden får man där hantera behållare som rymmer högst 30 liter, och myndigheten råder att man inte har mer hemma än man behöver, normalt en behållare som används och en i reserv. Ingen hantering bör ske på vinden.",
       "Flaskan får stå i köket eller i ett köksskåp, men skåpet ska vara ventilerat direkt ut i rummet. MCF skriver att det vanligtvis krävs öppningar både högt och lågt i förvaringsutrymmet och att öppningarnas area ska motsvara en procent av utrymmets golvarea. Det måttet tar vi med när skåpet bredvid spisen ritas, så att ventilationsöppningarna inte hamnar bakom en sockel som stänger dem.",
       "Slangen mellan flaskan och spisen är enligt MCF en vanlig orsak till olyckor. Den ska vara avsedd för gasol, sitta fast med slangklämma och kontrolleras inför varje säsong, och anläggningen ska täthetsprovas varje gång behållaren byts och minst vartannat år. Lågans inre del ska vara blågrön, och gula inslag betyder att brännaren behöver service. Gasol är ungefär 1,5 gånger tyngre än luft och kan därför först sjunka mot golvet vid en läcka.",
     ],
     "aside": {"title": "Gasol i fritidshuset", "items": [
       "Högst 30 liter i bostaden", "Ventilerat skåp, högt och lågt",
       "Öppningar på 1 % av golvarean", "Täthetsprov vid flaskbyte"]}},
    {"id": "vedspis", "h2": "Vedspisen: anmälan, sotning och brandskyddskontroll",
     "paras": [
       "Ska en vedspis installeras eller ändras väsentligt ska det anmälas till bygg- och miljönämnden, och arbetet får inte börja förrän startbesked har getts. Kommunen skriver att ett byte av eldstad i de flesta fall kräver anmälan. För att slippa måste den nya vara likvärdig i typ, storlek, effekt och anslutning till rökkanalen. Till anmälan hör situationsplan, planritning med eldstadens placering och fasadritning där skorstenen syns, och handläggningstiden är fyra veckor från att anmälan är komplett.",
       "När vedspisen är i bruk gäller kommunens frister. En lokaleldstad som är den huvudsakliga värmekällan i rummet eller används för matlagning ska enligt kommunens tabell sotas varje år och brandskyddskontrolleras vart tredje år. Eldas den i mindre omfattning blir intervallen tre år för sotning och sex år för kontroll. Brandskyddskontrollen görs av Räddningstjänsten i Norrtälje kommun, som bland annat tittar på eldstad, skorsten, tak och närliggande byggnadsdelar.",
       "Vid kontrollen ska rens- och inspektionsluckor gå att öppna, och räddningstjänsten ber att de inte blockeras. Därför planerar vi skåp och väggpaneler runt spisen så att luckorna går att nå. Taket ska ha godkända takskyddsanordningar hela vägen till skorstenen, se " + _L.format("takrenovering-norrtalje.html", "takrenovering i Norrtälje") + ".",
     ],
     "aside": None},
    {"id": "gaststuga", "h2": "Pentry i gäststugan eller ett större kök i huset",
     "paras": [
       "Den lovbefriade åtgärden attefallshus togs bort den 1 december 2025 och ersattes av bygglovsbefriad komplementbyggnad och komplementbostadshus. Utanför detaljplan får ett lovfritt komplementbostadshus enligt kommunen ha en byggnadsarea på högst 50 kvadratmeter och en taknockshöjd på högst 4,5 meter, och alla lovfria fristående byggnader på tomten får tillsammans vara högst 65 kvadratmeter. Inom detaljplan är gränserna 30 och 45 kvadratmeter och 4 meter.",
       "Byggnaden ska ha mindre byggnadsarea än huset den kompletterar. Bygglov krävs ändå om den placeras närmare än 4,5 meter från gränsen utan grannens skriftliga medgivande, om området är särskilt värdefullt eller om den ligger inom ett riksintresse för totalförsvaret. Tidigare lovfria byggnader på tomten räknas in i ytan, även sådana som byggdes enligt de äldre reglerna.",
       "Boverket påpekar att själva byggnaden ofta inte kräver anmälan, men att tekniska installationer som vatten, avlopp och ventilation gör det. Ett pentry med diskho i gäststugan kan alltså behöva anmälas även om stugan är lovfri. Ska köket i huvudbyggnaden bli större får en lovfri tillbyggnad vara högst 30 kvadratmeter och inte gå över den befintliga taknocken. Om stommen och virket läser du hos " + _L.format("snickare-norrtalje.html", "snickare i Norrtälje") + ", och om köksplanering på sidan om " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": {"title": "Lovfritt utanför detaljplan", "items": [
       "Komplementbostadshus högst 50 m²", "Nockhöjd högst 4,5 meter",
       "Tillbyggnad högst 30 m²", "4,5 meter till gräns"]}},
  ],
  "steps_h2": "Så går köksrenoveringen till i Norrtälje",
  "steps": [
    ("Platsbesök", "Vi går igenom kök, spis, eldstad och vatten, och om köket ska användas året runt eller mest på sommaren."),
    ("Gasol och eldstad", "Vi bedömer om eldstaden behöver anmälas och hur gasolflaskan ska stå."),
    ("Skriftligt kostnadsförslag", "Rivning, snickeri, VVS och el redovisas var för sig, med arbete och material åtskilda."),
    ("Rivning och installationer", "Gamla skåp tas bort, och vatten, avlopp och el dras om."),
    ("Montering", "Stomme, ventilerat gasolskåp, bänkskiva och vitvaror monteras."),
    ("Genomgång", "Vi provar spis, fläkt och blandare och går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för köket i fritidshuset",
  "rot": [
    "Ett fritidshus som du själv använder ger rätt till rotavdrag, men enligt Skatteverket inte om någon annan bor där permanent. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "I ett småhus räknas bland annat att montera fast köksinredning och installera vitvaror i samband med en omfattande renovering, att installera och reparera braskaminer och att installera avlopp och ventilation. Material och resor ger inget avdrag, och Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Norrtälje?",
  "price": [
    "Mycket handlar om vad som ska finnas kvar. Behålls gasolspisen eller vedspisen blir skåpen runt dem ett eget moment, och ska en ny eldstad in tillkommer anmälan och skorstensarbete. Avstånd och åtkomst, till exempel till en stuga på en ö, kan påverka hur material och avfall fraktas. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur mycket gasol får vi ha i köket i sommarhuset i Norrtälje?",
     "MCF anger högst 30 liter brandfarlig gas i en villa eller ett fritidshus och råder att man har en behållare i bruk och en i reserv. Flaskan får stå i ett köksskåp som är ventilerat direkt ut i rummet."),
    ("Hur ofta ska vedspisen i köket sotas i Norrtälje kommun?",
     "Används spisen för matlagning eller är den rummets huvudsakliga värmekälla anger kommunens frister sotning varje år och brandskyddskontroll vart tredje år. Eldas den mindre blir det tre respektive sex år."),
    ("Måste vi anmäla en ny vedspis som ersätter en gammal på samma plats?",
     "Oftast. Kommunen skriver att byte av eldstad i de flesta fall kräver anmälan, och att det bara kan undvikas om den nya är likvärdig i typ, storlek, effekt och anslutning till rökkanalen."),
    ("Får vi bygga ett pentry i en gäststuga utan bygglov i Norrtälje?",
     "Stugan kan vara lovfri som komplementbostadshus om gränserna för storlek, höjd och avstånd uppfylls. Vatten, avlopp och ventilation kan ändå kräva anmälan."),
    ("Vem gör brandskyddskontrollen av eldstaden i Norrtälje?",
     "Räddningstjänsten i Norrtälje kommun. Kontrollanten granskar bland annat eldstaden, skorstenen, fläkt, spjäll och rökkanaler och byggnadsdelar som ligger nära."),
  ],
  "sources": [
    ("Myndigheten för civilt försvar – Förvara gasol hemma",
     "https://www.mcf.se/sv/rad-till-privatpersoner/brandsakerhet/gasol-i-hemmet-och-pa-fritiden/forvara-gasol-hemma/"),
    ("Myndigheten för civilt försvar – Gasol i hemmet och på fritiden",
     "https://www.mcf.se/sv/rad-till-privatpersoner/brandsakerhet/brandfarliga-gaser-och-vatskor-i-hem--och-fritidsmiljo/gasol-hemma/"),
    ("Norrtälje kommun – Eldstad och rökkanal", "https://www.norrtalje.se/sjalvservice/bygga-bo-miljo/eldstad-och-rokkanal/"),
    ("Norrtälje kommun – Tidsintervall sotning och brandskyddskontroll", _NT + "tidsintervall-sotning-och-brandskyddskontroll/"),
    ("Norrtälje kommun – Brandskyddskontroll av eldstad", _NT + "privatperson/din-eldstad/brandskyddskontroll-av-eldstad/"),
    ("Norrtälje kommun – Lovbefriade åtgärder", "https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/lovbefriade-atgarder/"),
    ("Norrtälje kommun – Landsbygd och skärgård, fakta och statistik",
     "https://www.norrtalje.se/info/bygga-bo-miljo/norrtalje-vaxer/landsbygd-skargard/fakta-och-statistik/"),
    _BOV_PBL, _SKV, _SKV2,
  ],
  "cta": ("Ska sommarköket i Norrtälje bli ett riktigt kök?", "Boka ett gratis platsbesök, så går vi igenom gasol, eldstad och vatten på plats."),
  "img": [
    ("Kök i ett rödmålat fritidshus i Roslagen med vedspis och gasolspis",
     "renovated kitchen in a red-painted Swedish wooden summer cottage in Roslagen, black cast-iron wood-burning kitchen stove next to a small freestanding gas cooker, white painted wooden cabinets with a ventilated lower door, wooden worktop, window with white frames overlooking pine forest and the Baltic archipelago, painted wooden floor, summer daylight, no people"),
    ("Liten rödmålad gäststuga bredvid ett äldre sommarhus på en tomt i Norrtälje",
     "small new Swedish guest cottage with falu red vertical wooden panel and white window frames standing on a lawn beside an older summer house, black metal roof, birch trees and granite rocks, Norrtälje archipelago, early summer daylight, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HÄGERSTEN
"koksrenovering-hagersten.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Hägersten", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Hägersten – Västertorp, Fruängen och asbest",
  "description": "Köksrenovering i Hägersten: lägenheter från 1940- och 50-talen i Västertorp och Fruängen, asbestprov före rivning och köket som öppnas mot vardagsrummet.",
  "h1": "Köksrenovering i Hägersten",
  "lead": "Västertorp och Fruängen byggdes när asbest fortfarande användes i byggmaterial, och många av lägenheterna där är i dag bostadsrätter. Det påverkar både vad som ska provas före rivningen och vem som ska säga ja till ändringarna. Geal Entreprenad AB bygger om kök i bostadsrätter, radhus och villor i Hägersten, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Efterkrigstidens lägenheter och asbestprov.",
  "sections": [
    {"id": "efterkrigstiden", "anchor": "Västertorp och Fruängen",
     "h2": "Två förorter från efterkrigstiden",
     "paras": [
       "Enligt Stadsmuseets Stockholms Spår byggdes Västertorp ut efter en stadsplan som fastställdes 1947 och som liknade idealstadsdelen i generalplanen Det framtida Stockholm från 1945. Här genomfördes för första gången i Sverige ett trafikseparerat samhälle, där fotgängarna gick på gångvägar i parkerna mellan husen. Tunnelbanestationen invigdes 1964.",
       "Fruängen uppfördes i huvudsak under senare delen av 1950-talet, som en av de tunnelbanestäder som byggdes i kommunal regi för att få bukt med bostadsbristen efter kriget. Stadsplanerna upprättades 1952–53 av Göran Sidenbladh vid stadsplanekontoret, och området skulle få bostäder för över 8 000 invånare.",
       "Stadens områdesfakta för 2025 visar hur husen används i dag. I Västertorp finns 4 315 bostäder, varav 1 627 bostadsrätter, och nästan hälften av lägenheterna i flerbostadshusen är tvåor. I Fruängen är 3 495 av 5 474 bostäder bostadsrätter. Styrelsen har alltså ofta ett ord med i laget när köket görs om. Mer om planeringen i allmänhet finns på sidan om " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": {"title": "Hägersten i siffror 2025", "items": [
       "Västertorp: 4 315 bostäder", "Fruängen: 5 474 bostäder",
       "Västberga: 289 småhusbostäder", "Flest tvåor i Västertorp"]}},
    {"id": "asbest", "h2": "Prov före rivning i kök från 1940-talet och framåt",
     "paras": [
       "Boverket skriver att det är sannolikt att det finns asbest någonstans i en byggnad som uppfördes mellan 1940 och 1980, och att användningen förbjöds inom byggsektorn 1982. Asbest kan också ha kommit in vid senare renoveringar. Så länge materialet är inkapslat är det ingen fara, men när det bearbetas så att det dammar frigörs fibrer som är farliga att andas in.",
       "I ett kök finns flera av de ställen som Boverket räknar upp: kakel- och klinkerfix och fog, golvmattor och limmet under dem, golvplattor, fönsterbänkar, tätmassor och ventilationskanaler. Provtagning och analys är enligt Boverket det enda säkra sättet att veta. Därför tar vi prov på misstänkta material innan något rivs i en lägenhet från den här tiden.",
       "Visar provet asbest krävs enligt Arbetsmiljöverket tillstånd för att ett företag ska få riva eller sanera materialet, och ansökan ska göras åtta veckor innan arbetet ska börja. Rivning inomhus görs i inneslutning med luftsluss och undertryck. Det påverkar tidplanen mer än något annat i köket, så vi vill ha svaret innan startdatum bestäms.",
     ],
     "aside": {"title": "Vanliga ställen i köket", "items": [
       "Kakelfix och fog", "Golvmatta och lim",
       "Fönsterbänkar", "Ventilationskanal"]}},
    {"id": "oppna-koket", "h2": "Öppna köket mot vardagsrummet i en tvåa",
     "paras": [
       "Vill du ta bort väggen mellan kök och vardagsrum i en bostadsrätt gäller bostadsrättslagen: ingrepp i en bärande konstruktion, ändring av ledningar för avlopp, värme, gas eller vatten och ändring av ventilationen kräver styrelsens tillstånd. Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet för föreningen, och tillståndet kan förenas med villkor. Den som är missnöjd med beslutet kan begära att hyresnämnden prövar frågan.",
       "Stockholms stad kräver inget bygglov för att flytta ett kök, men en anmälan och ett startbesked om ändringen påverkar bärande konstruktion eller brandskydd, ändrar ventilationen väsentligt eller kräver en ny VA-stam i ett nytt schakt. Beslut ska komma inom fyra veckor från att anmälan är komplett, med möjlighet till förlängning en gång. En konstruktionsritning till anmälan ska tas fram av en sakkunnig konstruktör.",
       "I områdets radhus och villor, till exempel de knappt 300 småhusbostäderna i Västberga, bestämmer du själv, men samma tekniska krav gäller. Mer om väggar och tak inomhus finns hos " + _L.format("malare-hagersten.html", "målare i Hägersten") + ", och om husens tak hos " + _L.format("taklaggare-hagersten.html", "takläggare i Hägersten") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till i Hägersten",
  "steps": [
    ("Platsbesök", "Vi ser på kök, väggar, golv och fönsterbänkar och tar reda på husets byggår."),
    ("Asbestprov", "Misstänkta material provas och analyseras innan något rivs."),
    ("Underlag till styrelsen", "Du får en beskrivning av arbetet att lämna till föreningen, med konstruktörens underlag om en vägg berörs."),
    ("Skriftligt kostnadsförslag", "Rivning, eventuell sanering, installationer och montering redovisas var för sig."),
    ("Rivning och installationer", "Gamla skåp och ytskikt tas bort och rör, el och fläkt dras enligt planen."),
    ("Montering och genomgång", "Stomme, bänkskiva och vitvaror monteras och vi går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för köket i en bostadsrätt i Hägersten",
  "rot": [
    "I en bostadsrätt godtar Skatteverket rotavdrag för att riva innerväggar och bygga om lägenhetens planlösning, för att montera fast köksinredning och installera vitvaror i samband med byggarbetet och för att byggstäda material och grovsopor efteråt. Arbetet ska göras innanför lägenhetens väggar, tak och golv och ingå i ditt underhållsansvar enligt stadgarna.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag, och att forsla bort rivningsrester räknas inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Hägersten?",
  "price": [
    "Visar provet asbest tillkommer sanering av ett företag med tillstånd, och det kan också flytta startdatum. En bärande vägg som ska bort lägger till konstruktör, anmälan och balk. Hiss och trapphus påverkar hur skåp och bänkskiva kommer upp. Du får ett skriftligt kostnadsförslag efter det gratis platsbesöket.",
  ],
  "faq": [
    ("Hur vet vi om köket i vår lägenhet i Västertorp innehåller asbest?",
     "Boverket bedömer att asbest är sannolik i hus från 1940–1980, men det enda säkra är provtagning och analys. Vi tar prov på misstänkta material innan rivningen."),
    ("Hur lång tid tar det att få tillstånd för asbestsanering?",
     "Arbetsmiljöverket vill ha ansökan åtta veckor innan arbetet ska börja. Det är företaget som ska riva eller sanera som söker tillståndet."),
    ("Får styrelsen i Fruängen säga nej till att vi river väggen mot vardagsrummet?",
     "Bara om åtgärden är till påtaglig skada eller olägenhet för föreningen. Tillståndet kan förenas med villkor, och är du missnöjd kan hyresnämnden pröva frågan."),
    ("Räknas bortforsling av det gamla köket in i rotavdraget?",
     "Nej. Att forsla bort material och rivningsrester ger inget avdrag. Däremot räknas byggstädning av material och grovsopor efter rotarbetet."),
    ("Kan badrummets frånluftskanal också bli imkanal för köksfläkten?",
     "Stockholms stad skriver att kanalens sammanlagda mått måste räcka innan den används som kombinerad imkanal och frånluftskanal. Staden råder dig också att tidigt fråga sotaren om förutsättningarna."),
  ],
  "sources": [
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Västertorp (pdf)", _SSM.format("000097")),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Fruängen (pdf)", _SSM.format("000056")),
    ("Stockholms stad – Områdesfakta 2025: Västertorp (pdf)", _OF + "soderort/hagersten/vastertorp.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Fruängen (pdf)", _OF + "soderort/hagersten/fruangen.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Västberga (pdf)", _OF + "soderort/hagersten/vastberga.pdf"),
    _BOV_ASB, _AV_ASB, _BRL, _STH_FLYTT, _SKV, _SKV2,
  ],
  "cta": ("Ska köket i Hägersten rivas och göras om?", "Boka ett gratis platsbesök, så går vi igenom material, prover och planlösning på plats."),
  "img": [
    ("Renoverat lägenhetskök i ett hus från 1950-talet i Hägersten",
     "renovated small galley kitchen in a 1950s Swedish apartment block, pale sage green flat-front cabinets, light terrazzo-look worktop, white tiled splashback, original wooden window with deep stone sill looking out on pine trees and other low lamella apartment buildings, linoleum floor, soft daylight, no people"),
    ("Ljust kök med matbord och köksfläkt",
     "empty unoccupied old 1950s Swedish apartment kitchen being prepared for renovation, nobody in the room, upper cabinets removed, old vinyl floor mat with a small square piece cut out for sampling, small sealed plastic sample bags on a work bench, plastic sheeting taped over the doorway, daylight from a window, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SUNDBYBERG
"koksrenovering-sundbyberg.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Sundbyberg", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Sundbyberg – Duvbo och lägenheter i stan",
  "description": "Köksrenovering i Sundbyberg: köksfönster, fläkthuv och tillbyggnad i riksintresset Duvbo, och föreningens tillstånd och OVK i flerbostadshusen.",
  "h1": "Köksrenovering i Sundbyberg",
  "lead": "Sundbyberg har två helt olika kök att bygga om: lägenhetsköket i ett flerbostadshus och köket i en villa i Duvbo, där det mesta som syns utifrån kräver bygglov. Geal Entreprenad AB bygger om kök i båda sorterna, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Duvbos villor och stadens lägenhetskök.",
  "sections": [
    {"id": "duvbo", "anchor": "Duvbo villastad",
     "h2": "Duvbo – en av landets första egnahemsmiljöer",
     "paras": [
       "Enligt stadens miljöprogram för Duvbo bildades föreningen Egna Hem 1898 för att skapa egna hem åt arbetare i bostadsnödens Stockholm. Året därpå köpte föreningen egendomen Dufvebol i Spånga församling och gjorde en stadsplan med 325 tomter, och 1924 utökades området västerut med ytterligare 98 villatomter. Riksantikvarieämbetet pekade 1987 ut Duvbo som riksintresse för kulturmiljövården.",
       "Husen är framför allt byggda vid sekelskiftet 1900 och under 1920-talet, i två våningar på höga nivåutjämnande socklar. Sekelskiftesvillorna byggdes ofta av ägarna själva och har fasader av stående och liggande spontpanel med snickarglädje, medan 1920-talsvillorna är enklare med locklistpanel. På 1930- och 40-talen tillkom slätputsade hus med flacka tak av rött lertegel.",
       "Innan vi föreslår en ny planlösning i ett sådant hus går vi igenom vad som kommer att synas utifrån, eftersom det är där reglerna i Duvbo är strängast.",
     ],
     "aside": {"title": "Duvbo i årtal", "items": [
       "1898: föreningen Egna Hem bildas", "1899: Dufvebol köps, 325 tomter",
       "1924: 98 tomter till", "1987: riksintresse"]}},
    {"id": "fonster-flakt", "h2": "Nytt köksfönster eller fläkthuv kräver bygglov i Duvbo",
     "paras": [
       "Sundbybergs stad skriver att det inte längre krävs bygglov för fasadändringar på en- och tvåbostadshus, men att det inte gäller i ett särskilt värdefullt bebyggelseområde som Duvbo. Där krävs bygglov för fasadändringar, och till dem räknar staden bland annat nya fönster och dörrar eller ändring av befintliga, ventilationshuvar och skorstenar.",
       "Miljöprogrammet räknar upp vad den utökade lovplikten i Duvbo omfattar: utbyte av fasadbeklädnad och takmaterial, omfärgning, utbyte, flyttning eller igensättning av fönster och dörrar och andra ändringar som påverkar husets yttre.",
       "Ett större fönster vid diskbänken, en dörr från köket ut mot trädgården eller en ny fläkthuv på fasaden är därför bygglovsfrågor i Duvbo. Vi stämmer av det innan köket ritas, så att väggarna inte behöver öppnas två gånger. Till ansökan hör enligt staden oftast situationsplan, plan- och fasadritning, kulör- och materialbeskrivning och kontrollplan.",
     ],
     "aside": {"title": "Bygglov i Duvbo", "items": [
       "Nytt eller flyttat köksfönster", "Ny dörr mot trädgården",
       "Fläkthuv på fasaden", "Ny skorsten"]}},
    {"id": "tillbyggnad", "h2": "Bygga ut köket i en villa i Duvbo",
     "paras": [
       "På andra håll i Sundbyberg går det att bygga till upp till 30 kvadratmeter utan bygglov, men staden skriver att den lättnaden inte gäller för kulturhistoriskt värdefulla byggnader eller i Duvbo. En köksutbyggnad kräver alltså bygglov där.",
       "Miljöprogrammet ger riktlinjerna. Tillbyggnaden får inte dominera över den ursprungliga huskroppen eller påverka gatubilden, husets ursprungliga volym ska gå att urskilja och tillbyggnaden ska ansluta till husets form, material och färg. Tillbyggnader med plana tak hör enligt programmet inte hemma bland egnahemsbebyggelsen från 1900–1920-talen, och tillbyggnader och uthus ska placeras så att områdets öppenhet bevaras.",
       "Även med bygglov kan en anmälan behövas, till exempel för vatten och avlopp till en diskbänk i den nya delen eller för en eldstad. Hur taket på en tillbyggnad kan anslutas till det gamla läser du om hos " + _L.format("taklaggare-sundbyberg.html", "takläggare i Sundbyberg") + ".",
     ],
     "aside": None},
    {"id": "lagenheten", "h2": "Lägenhetsköket: styrelsen, fasaden och OVK",
     "paras": [
       "I ett flerbostadshus behöver du enligt bostadsrättslagen styrelsens tillstånd för att ändra ledningar för avlopp, värme, gas eller vatten och för att installera eller ändra ventilationen. Föreningen svarar för reparationer av ventilationskanaler och av ledningar som den har dragit och som tjänar fler än en lägenhet, så den gemensamma kanalen bakom köksfläkten är föreningens ansvar.",
       "Ska en egen fläkt ha utlopp genom ytterväggen blir det dessutom en fasadfråga. För andra byggnader än en- och tvåbostadshus kräver staden bygglov om ändringen görs på en fasad eller ett tak som vetter mot allmän plats, och ventilationshuvar räknas som fasadändring.",
       "Staden påminner också om att ventilationen ska kontrolleras genom OVK när ett befintligt system byggs om, och därefter vart tredje eller vart sjätte år beroende på systemtyp. Kravet gäller inte en- och tvåbostadshus, och brister ska åtgärdas senast sex månader efter besiktningen. Ta därför reda på hos styrelsen vilken sorts köksfläkt huset är byggt för innan du väljer. Mer om planering finns på sidan om " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till i Sundbyberg",
  "steps": [
    ("Platsbesök", "Vi går igenom kök, fönster, fläkt och stammar, och om huset ligger i Duvbo."),
    ("Lov eller tillstånd", "I Duvbo stämmer vi av vad som kräver bygglov; i en lägenhet tar vi fram underlag till styrelsen."),
    ("Skriftligt kostnadsförslag", "Rivning, snickeri, el och VVS står som egna poster."),
    ("Rivning och installationer", "Gamla skåp tas bort och rör, el och fläkt dras enligt den nya planen."),
    ("Montering", "Stomme, bänkskiva och vitvaror monteras."),
    ("Genomgång", "Fläkt, blandare och vitvaror provas och vi går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för köket i Sundbyberg",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. I en villa i Duvbo räknar Skatteverket bland annat att riva väggar och bygga om planlösningen, att byta köksluckor och att modernisera elen.",
    "I en bostadsrätt ger arbete på de delar av ventilationskanalen som finns innanför lägenhetens tak, väggar och golv avdrag, men inte rengöring av ventilation och imkanaler. Material och resor ger inget avdrag, och Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Sundbyberg?",
  "price": [
    "I Duvbo spelar det roll om köket bara byggs om inne eller om fönster, dörr eller fläkthuv ändras så att bygglov behövs. En tillbyggnad lägger till ritningar, lov och arbete med tak och grund. I lägenheten är huvudfrågan om köket stannar vid stammen eller flyttas. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för ett större köksfönster i vår villa i Duvbo?",
     "Ja. I Duvbo krävs bygglov för fasadändringar, och dit räknar staden nya eller ändrade fönster och dörrar."),
    ("Kan vi bygga ut köket utan bygglov i Duvbo?",
     "Nej. Staden skriver att den lovfria tillbyggnaden på upp till 30 kvadratmeter inte gäller i Duvbo eller för kulturhistoriskt värdefulla byggnader."),
    ("Får vi dra köksfläkten ut genom fasaden på ett flerbostadshus i Sundbyberg?",
     "Det kräver styrelsens tillstånd, och vetter fasaden mot allmän plats kräver staden dessutom bygglov, eftersom ventilationshuvar räknas som fasadändring."),
    ("Vem ansvarar för den gemensamma ventilationskanalen bakom vår köksfläkt?",
     "Föreningen. Enligt bostadsrättslagen svarar bostadsrättshavaren inte för reparationer av ventilationskanaler, eller av ledningar som föreningen har dragit och som tjänar fler än en lägenhet."),
    ("Hur ofta ska ventilationen i vårt flerbostadshus i Sundbyberg kontrolleras?",
     "Vart tredje år med FT- eller FTX-ventilation och vart sjätte år med F-, FX- eller S-ventilation, enligt staden. En kontroll ska också göras när ett befintligt system byggs om."),
  ],
  "sources": [
    ("Sundbybergs stad – Miljöprogram Duvbo (pdf)",
     "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf"),
    ("Sundbybergs stad – Fasadändring (bygglovsguiden)", _SB + "fasadandring"),
    ("Sundbybergs stad – Tillbyggnad, bygglovsbefriad (bygglovsguiden)", _SB + "tillbyggnad---bygglovsbefriad"),
    ("Sundbybergs stad – Obligatorisk ventilationskontroll, OVK", _SB + "obligatorisk-ventilationskontroll-ovk"),
    _BRL, _SKV, _SKV2,
  ],
  "cta": ("Ska köket i Sundbyberg göras om?", "Boka ett gratis platsbesök, så går vi igenom lov, tillstånd och planlösning på plats."),
  "img": [
    ("Renoverat kök i en sekelskiftesvilla i Duvbo med spröjsat fönster mot trädgården",
     "renovated kitchen in a Swedish wooden villa from around 1900, painted panelled cabinets in warm off-white, dark green tiled splashback, wooden worktop, tall small-paned window with white frame looking out on an old garden with fruit trees, wide painted pine floorboards, soft daylight, no people"),
    ("Ljusgul trävilla från sekelskiftet på hög stensockel bland fruktträd i Duvbo",
     "two-storey Swedish wooden villa from around 1900 with pale yellow vertical and horizontal panel divided into fields, decorative carved wooden details, red clay tile roof, high natural stone plinth, garden with fruit trees, a simple picket fence and a hedge along a winding street, Duvbo Sundbyberg, summer daylight, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ KISTA
"koksrenovering-kista.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Kista", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Kista – småhus i förening och 70-talskök",
  "description": "Köksrenovering i Kista: småhus som bostadsrätt, styrelsens tillstånd, ansvaret för ledningar och vattenskador, rotavdrag och elen i ett 70-talskök.",
  "h1": "Köksrenovering i Kista",
  "lead": "I Kista och Akalla är hundratals småhus upplåtna med bostadsrätt. Ett småhus i en förening ser ut som ett eget hus, men det är föreningens, och styrelsen ska godkänna det mesta som rör ledningar, ventilation och väggar. Geal Entreprenad AB bygger om kök i radhus, lägenheter och villor i Kista med omnejd, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Småhus i förening och kök från 1970-talet.",
  "sections": [
    {"id": "jarvafaltet", "anchor": "Husen i Kista",
     "h2": "Järvafältets stadsdel från 1970-talet",
     "paras": [
       "Kista ligger på det gamla militära övningsområdet Järvafältet. Enligt Stadsmuseets Stockholms Spår köpte staden marken 1966, och stadsdelen byggdes ut 1975–1980 med betydligt friare arkitektoniska former än i de övriga stadsdelarna på Järvafältet. Bebyggelsen beskrivs där som 2 500 lägenheter i flerbostadshus och omkring 780 småhus, och Kista centrum invigdes 1977.",
       "Stadens områdesfakta för 2025 visar att 404 av småhusbostäderna i Kista är bostadsrätter och 482 äganderätter. I grannstadsdelen Akalla är 493 småhusbostäder bostadsrätter och 170 äganderätter. Antalet lägenheter i Kistas flerbostadshus ökade samtidigt från 4 879 till 5 318 mellan 2024 och 2025.",
       "För köket gör det stor skillnad vilken av grupperna du tillhör. Äger du huset bestämmer du själv inom lagens krav. Är huset upplåtet med bostadsrätt gäller i stort sett samma regler som för en lägenhet i ett flerbostadshus. Husen från utbyggnaden 1975–1980 är dessutom byggda före 1982, då asbest enligt Boverket förbjöds inom byggsektorn, så misstänkta material provas innan något rivs.",
     ],
     "aside": {"title": "Kista och Akalla 2025", "items": [
       "Kista: 404 småhus med bostadsrätt", "Kista: 482 småhus med äganderätt",
       "Akalla: 493 med bostadsrätt", "Akalla: 170 med äganderätt"]}},
    {"id": "foreningen", "h2": "Småhuset är en bostadsrätt – det här ska styrelsen godkänna",
     "paras": [
       "Bostadsrättslagen räknar upp de åtgärder i lägenheten som kräver styrelsens tillstånd: ingrepp i en bärande konstruktion, installation eller ändring av ledningar för avlopp, värme, gas eller vatten, installation eller ändring av ventilationen, ändringar som påverkar brandskyddet och andra väsentliga förändringar. Det gäller även när lägenheten är ett småhus.",
       "Ansvaret för skicket följer av samma lag. Du ska hålla lägenheten i gott skick på egen bekostnad, om inte stadgarna säger något annat, men svarar inte för reparationer av ledningar för avlopp, värme, gas, el och vatten som föreningen har dragit och som tjänar fler än en lägenhet. Det kan göra stor skillnad i en husgrupp där stammar och kanaler kan vara gemensamma för flera hus.",
       "En punkt är lätt att missa. Vid en brand- eller vattenledningsskada svarar du bland annat om skadan har uppkommit genom vårdslöshet eller försummelse av någon som utför arbete i lägenheten för din räkning. Därför beskriver vi i underlaget till styrelsen vem som gör el och VVS och hur arbetet utförs, och du får handlingar att spara efteråt.",
     ],
     "aside": None},
    {"id": "elen", "h2": "Elen när köket får fler maskiner",
     "paras": [
       "Enligt Elsäkerhetsverket ska de flesta elinstallationsarbeten utföras av ett registrerat elinstallationsföretag. Vid förändringar i den fasta installationen, till exempel ett nytt uttag i köket eller elledningar i väggarna, ska ett sådant företag anlitas. Att byta ett ojordat vägguttag mot ett jordat får du inte heller göra själv.",
       "Det du själv får göra är begränsat: byta trasiga proppar, byta glödlampor och lamphållare, byta en fast ansluten armatur i torra utrymmen och byta en befintlig strömbrytare eller ett befintligt vägguttag för högst 16 A som sitter i egen dosa. Det förutsätter att du vet hur det görs och att arbetet kan kontrolleras.",
       "Får det nya köket fler maskiner och uttag än det gamla går vi igenom uttag och grupper vid platsbesöket och låter elföretaget bedöma vad som behöver kompletteras innan skåp och stänkskydd monteras.",
     ],
     "aside": {"title": "Elen i köket", "items": [
       "Nytt uttag: registrerat elföretag", "Ojordat till jordat: elföretag",
       "Byta glödlampa: själv", "Byta befintligt uttag: med rätt kunskap"]}},
    {"id": "flytta", "h2": "Flytta diskbänken eller spisen i småhuset",
     "paras": [
       "Stockholms stad kräver inget bygglov för att flytta ett kök. En anmälan och ett startbesked behövs däremot om flytten påverkar bärande konstruktion eller brandskydd, innebär en väsentlig ändring av ventilationen eller kräver en ny VA-stam i ett nytt schakt. Staden råder dig att tidigt rådgöra med sotaren om en ny eller ändrad imkanal och att kontakta styrelsen innan du börjar planera.",
       "Har huset två plan kan en ny plats för diskbänken hamna långt från stammen. Ju längre avloppet ska dras, desto mer golv eller bjälklag behöver öppnas, och det är också en ändring av ledningar som styrelsen ska godkänna. Mer om husens tak finns hos " + _L.format("taklaggare-kista.html", "takläggare i Kista") + ", och om köksplanering i stort på sidan om " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till i Kista",
  "steps": [
    ("Platsbesök", "Vi går igenom kök, stam, frånluft och el och tar reda på om huset är en bostadsrätt eller en äganderätt."),
    ("Underlag till styrelsen", "I en förening får du en beskrivning av arbetet och av vilka som utför el och VVS."),
    ("Skriftligt kostnadsförslag", "Rivning, el, VVS och montering redovisas var för sig, med arbete skilt från material."),
    ("Rivning och installationer", "Gamla skåp tas bort och el, rör och fläkt dras enligt den nya planen."),
    ("Montering", "Stomme, bänkskiva och vitvaror monteras och ansluts."),
    ("Genomgång och handlingar", "Vi provar allt, går igenom köket med dig och lämnar handlingar att spara."),
  ],
  "rot_h2": "ROT-avdrag för köket i ett småhus i Kista",
  "rot": [
    "Skatteverket skriver att du i en bostadsrätt bara kan få rotavdrag för arbeten inne i din bostad, och att det inte ges för arbete på till exempel fasad eller balkong, ens om bostadsrätten är ett radhus eller parhus. Innanför väggar, tak och golv räknas bland annat att montera fast köksinredning och installera vitvaror i samband med byggarbetet, att dra elledningar från proppskåpet ut i bostaden och att installera blandare och kranar.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Äger du huset gäller reglerna för småhus. Material och resor ger inget avdrag, och Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Kista?",
  "price": [
    "Det som styr mest är om diskbänk och spis står kvar vid stam och kanal eller flyttas. Behöver elen kompletteras med nya grupper tillkommer elarbete, och i ett hus i två plan kan ett nytt avlopp kräva att golv öppnas. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste styrelsen godkänna vårt nya kök i ett småhus i Akalla?",
     "Ja, om arbetet ändrar ledningar för vatten och avlopp, ventilationen, bärande konstruktion eller brandskyddet. Bostadsrättslagen kräver styrelsens tillstånd för sådana åtgärder."),
    ("Vem svarar om hantverkaren orsakar en vattenskada i vår bostadsrätt i Kista?",
     "Enligt bostadsrättslagen svarar du som bostadsrättshavare för reparationen om skadan har uppkommit genom vårdslöshet eller försummelse av någon som utför arbete i lägenheten för din räkning."),
    ("Får vi rotavdrag för arbete på utsidan av huset när det är en bostadsrätt?",
     "Nej. Skatteverket godtar i en bostadsrätt bara arbete inne i bostaden, även när bostadsrätten är ett radhus eller parhus."),
    ("Får jag själv sätta in ett extra uttag ovanför köksbänken?",
     "Nej. Elsäkerhetsverket räknar ett nytt uttag i köket som en förändring i den fasta installationen, och den ska göras av ett registrerat elinstallationsföretag."),
    ("Behöver vi anmäla till staden om vi flyttar diskbänken i vårt småhus i Kista?",
     "Inte för själva flytten. Stockholms stad kräver anmälan och startbesked om ventilationen ändras väsentligt, om bärande konstruktion eller brandskydd påverkas eller om en ny VA-stam dras i ett nytt schakt."),
  ],
  "sources": [
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Kista (pdf)", _SSM.format("000080")),
    ("Stockholms stad – Områdesfakta 2025: Kista (pdf)", _OF + "vasterort/jarva/kista.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Akalla (pdf)", _OF + "vasterort/jarva/akalla.pdf"),
    _BRL, _ELS, _STH_FLYTT, _BOV_ASB, _SKV, _SKV2,
  ],
  "cta": ("Ska köket i småhuset i Kista bli nytt?", "Boka ett gratis platsbesök, så går vi igenom föreningens regler, el och planlösning på plats."),
  "img": [
    ("Nytt kök med vita luckor och ekbänkskiva i ett småhus från 1970-talet i Kista",
     "renovated kitchen in a 1970s Swedish terraced house, white matt flat cabinet fronts, oak worktop, light grey tiled splashback with several new electrical sockets above the counter, window looking out on a small back garden with a wooden fence and other low terraced houses with brown wooden facades, daylight, no people"),
    ("Småhus i grupp med bruna träfasader och små förgårdar i Kista",
     "row of 1970s Swedish two-storey terraced houses with dark brown stained wooden panel facades and light brick sections, small front gardens with bushes, a footpath and birch trees, Kista Stockholm, autumn daylight, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SÖDERMALM
"koksrenovering-sodermalm.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Södermalm", "svc_label": "Köksrenovering",
  "title": "Köksrenovering på Södermalm – kokvrå, gas och kulturvärden",
  "description": "Köksrenovering på Södermalm: från kokvrå till kök, gasspis på stadsgasnätet, lägenheter med kulturvärden och de få småhusen på malmarnas höjder.",
  "h1": "Köksrenovering på Södermalm",
  "lead": "Nästan alla Södermalms omkring 77 500 bostäder ligger i flerbostadshus, och mer än hälften är bostadsrätter. Köket kan vara en kokvrå i en etta, en gasspis på stadsgasnätet eller ett kök i ett hus med kulturvärden. Geal Entreprenad AB bygger om kök i lägenheter på hela Södermalm, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Kokvrå, gasspis och kulturvärden i lägenheten.",
  "sections": [
    {"id": "kokvra", "anchor": "Kokvrå eller kök",
     "h2": "Från kokvrå till kök",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 73 952 bostäder i flerbostadshus på Södermalm. Av dem redovisas 7 856 som lägenheter utan kök och 17 165 som ettor med kök. De små lägenheterna är alltså många, och i dem handlar en köksrenovering om att få plats med mer på liten yta.",
       "I lägenhetsregistret är ett kök ett utrymme för matlagning med en golvyta på minst sju kvadratmeter, bänkar och skåp inräknade, och med direkt eller indirekt dagsljus. Ett mindre utrymme där en person ändå kan vistas räknas som kokvrå, och ett kokskåp är inredning för matlagning med vatten, avlopp och kylskåp. En kokvrå med matrum räknas som kök om utrymmena tillsammans är minst sju kvadratmeter och har dagsljus.",
       "Ska kokvrån bli ett kök genom att en vägg flyttas krävs styrelsens tillstånd om väggen är bärande eller om rör och ventilation berörs. Stockholms stad påpekar att ventilationskanalens sammanlagda mått ska räcka om badrumskanalen ska användas som kombinerad imkanal för köket och frånluftskanal för badrummet, och att ett kök behöver tillräcklig frånluft.",
     ],
     "aside": {"title": "Lägenhetsregistrets begrepp", "items": [
       "Kök: minst 7 m² och dagsljus", "Kokvrå: mindre än 7 m²",
       "Kokskåp: vatten, avlopp och kylskåp", "Kokvrå med matrum kan bli kök"]}},
    {"id": "gasspis", "h2": "Gasspisen på stadsgasnätet",
     "paras": [
       "I Stockholm finns ett stadsgasnät, där gasen är en blandning av metan och luft. Nätbolaget, som sedan juni 2026 heter Driva Gasnät, skriver att den som byter gasspis först måste ta reda på vilket nät lägenheten är ansluten till. På stadsgasnätet ska spisen vara godkänd för stadsgas med beteckningen 1a eller 1e och ha dysor märkta G110 eller G150.1. I Hammarby sjöstad levereras i stället biogas i fordonsgasnätet, och där ska spisen vara anpassad för naturgas eller biogas med beteckningen 2H.",
       "Enligt nätbolaget får arbeten på gasnätet, både byte och bortkoppling av en gasapparat, bara göras av gasinstallatörer som är godkända för det, och en förteckning över dem finns hos Energigas Sverige. Energigas Sveriges anvisningar för hushållsapparater, framtagna tillsammans med bland andra Gasnätet Stockholm, säger att allt installationsarbete kräver föranmälan eller efteranmälan till nätbolaget och att apparater tillverkade efter den 1 januari 1996 ska vara CE-märkta för den aktuella gasen.",
       "Gasledningen är också en föreningsfråga, eftersom bostadsrättslagen kräver styrelsens tillstånd för att installera eller ändra ledningar för gas. Ska gasspisen bort helt samordnar vi bortkopplingen med gasinstallatören och anslutningen av den nya spisen med elföretaget. Boverket nämner dessutom gasspisar bland de produkter där asbest kan förekomma, så en gammal spis hanteras varsamt vid rivningen.",
     ],
     "aside": {"title": "Byta gasspis", "items": [
       "Kontrollera vilket gasnät", "Stadsgas: 1a eller 1e",
       "Hammarby sjöstad: 2H", "Anmälan till nätbolaget"]}},
    {"id": "kulturvarden", "h2": "Lägenheter med kulturhistoriska värden",
     "paras": [
       "Bostadsrättslagen har en regel som är särskilt relevant i innerstaden. För en lägenhet med särskilda historiska, kulturhistoriska, miljömässiga eller konstnärliga värden krävs styrelsens tillstånd för varje åtgärd som påverkar ett sådant värde. Lagen kräver också tillstånd för installation eller ändring av eldstad eller rökkanal, vilket berör den som har en kakelugn eller en gammal spisanordning i köket.",
       "Stockholms stad skriver att hänsyn till byggnadens kulturhistoriska värden ska tas vid alla ändringar, även när ett kök flyttas inomhus. Stadsmuseets klassificeringskarta ger en första indikation. Riksintressen för kulturmiljövården är markerade med blå ring, områden som översiktsplanen pekar ut som särskilt kulturhistoriskt värdefulla med grön ring, och för blå- eller grönmarkerade byggnader krävs bygglov för åtgärder som annars är lovfria. Museet brukar svara inom tre veckor när det har fått de uppgifter det ber om.",
       "Skatteverket godtar rotavdrag i en bostadsrätt för att mura och reparera öppen spis och kakelugn, så en kakelugn som ska stå kvar i köket kan lagas i samma veva. Mer om snickerier och listverk i lägenheten finns hos " + _L.format("snickare-sodermalm.html", "snickare på Södermalm") + ".",
     ],
     "aside": None},
    {"id": "malmarna", "h2": "De få småhusen på malmarnas höjder",
     "paras": [
       "Bara 211 av bostäderna i stadsdelsområdet ligger i småhus, enligt områdesfakta. Översiktsplanens redovisning av riksintresset pekar ut Fjällgatan, Katarinaberget, Vita bergen, Åsöberget och Östra Mariaberget som värdekärnor för den tidiga bebyggelsen på malmarna. Av den perioden återstår omkring 300 hus, de flesta på Södermalm.",
       "Redovisningen påpekar att de flesta äldre byggnaderna har byggts om och till under århundradena, så att det är svårt att tala om ett originalutförande. Den småskaliga bebyggelsen, trädgårdarna och detaljer som fönster och entréportar räknas till det som ger miljön dess karaktär. I ett sådant hus planerar vi köket så att fönster och fasad lämnas orörda, och ändringar som syns utifrån stäms av med staden först. Mer om planering finns på sidan om " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till på Södermalm",
  "steps": [
    ("Platsbesök", "Vi mäter kök eller kokvrå och ser var stam, kanal, gasledning och el finns."),
    ("Underlag till styrelsen", "Du får en beskrivning av arbetet och av vilka som gör el, VVS och gas."),
    ("Skriftligt kostnadsförslag", "Rivning, installationer, snickeri och montering redovisas var för sig."),
    ("Skydd och rivning", "Trapphuset skyddas och gamla skåp och vitvaror bärs ut."),
    ("Installationer och montering", "Rör, el och fläkt dras och den nya inredningen monteras."),
    ("Genomgång", "Spis, fläkt och blandare provas och vi går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för köket i en bostadsrätt på Södermalm",
  "rot": [
    "I en bostadsrätt räknar Skatteverket bland annat att dra vatten- och avloppsledningar inne i lägenheten, att montera fast köksinredning och installera vitvaror i samband med byggarbetet, att byta köksluckor och att installera inbyggda spotlights.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Arbetet ska ingå i ditt underhållsansvar enligt stadgarna. Material ger inget avdrag, och Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök på Södermalm?",
  "price": [
    "Att göra om en kokvrå till kök är ett större jobb än att byta inredning på samma plats, särskilt om en vägg flyttas. En gasspis som ska bytas eller kopplas bort lägger till gasinstallatörens arbete. Trapphus, hiss och möjligheten att ställa en container på gatan påverkar hur rivning och leveranser går till. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vår kokvrå på Södermalm byggas om till ett riktigt kök?",
     "Det beror på yta och dagsljus. I lägenhetsregistret är ett kök minst sju kvadratmeter med dagsljus. Ska en vägg flyttas eller rör och ventilation ändras krävs styrelsens tillstånd."),
    ("Vilken gasspis kan vi köpa till en lägenhet på stadsgasnätet?",
     "En spis som är godkänd för stadsgas, med beteckningen 1a eller 1e och dysor märkta G110 eller G150.1, enligt nätbolaget. Installationen ska anmälas till nätbolaget."),
    ("Får vi ta bort gasspisen och sätta in en induktionshäll?",
     "Det går, men gasledningen berörs och styrelsen ska ge tillstånd. Bortkopplingen görs av en gasinstallatör, och en fast ansluten häll ska kopplas in av ett registrerat elinstallationsföretag."),
    ("Behöver styrelsen godkänna att vi river den gamla kakelugnen i köket?",
     "Ja. Bostadsrättslagen kräver tillstånd för ändring av eldstad eller rökkanal, och om lägenheten har kulturhistoriska värden även för varje åtgärd som påverkar dem."),
    ("Hur tar vi reda på om huset på Södermalm är kulturhistoriskt klassat?",
     "Stadsmuseets klassificeringskarta ger en första indikation. Är byggnaden blå- eller grönmarkerad eller ligger i ett område med blå eller grön ring gäller utökad lovplikt. Museet svarar på frågor via e-post."),
  ],
  "sources": [
    ("Stockholms stad – Områdesfakta 2025: Södermalms stadsdelsområde (pdf)", _OF + "inre-staden/sodermalm/sodermalm-stadsdelsomrade.pdf"),
    ("Lantmäteriverkets föreskrifter (LMVFS 2007:3) om lägenhetsregister (lagen.nu)", "https://lagen.nu/lmvfs/2007:3"),
    ("Driva Gasnät – Gasinstallation", "https://driva.se/privatkund/gasinstallation"),
    ("Driva – Kundservice och vanliga frågor", "https://driva.se/privatkund/kundservice"),
    ("Driva – Stockholm Gas och Gasnätet Stockholm byter namn", "https://driva.se/namnbyte"),
    ("Energigas Sverige – Installation av gasapparater för matlagning i hushåll (pdf)",
     "https://www.energigas.se/media/1532/installation-hushaall_2016-sammanslagen.pdf"),
    _BRL, _STH_FLYTT, _STH_KLASS, _STH_RIKS, _BOV_ASB, _ELS, _SKV, _SKV2,
  ],
  "cta": ("Ska köket på Södermalm göras om?", "Boka ett gratis platsbesök, så går vi igenom kokvrå, gas och föreningens regler på plats."),
  "img": [
    ("Renoverat kök i en sekelskifteslägenhet på Södermalm med gasspis",
     "renovated kitchen in a late 1800s Stockholm stone-city apartment, high ceiling with plaster cornice, deep blue painted shaker cabinets, white marble-look worktop, freestanding enamel gas cooker with burners, tall double casement window with deep sill looking onto a courtyard, old wide pine floorboards, daylight, no people"),
    ("Små äldre trähus längs en kullerstensgata på Södermalms höjder",
     "small old wooden houses painted ochre and falu red along a narrow cobblestone lane on a hill, wooden fences and small gardens with lilac, larger stone apartment buildings in the background, Stockholm Södermalm, summer daylight, no people"),
  ],
  "related": [],
},

}
