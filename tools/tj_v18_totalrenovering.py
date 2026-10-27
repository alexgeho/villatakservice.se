# -*- coding: utf-8 -*-
"""Totalrenovering – ortsidor v18: Bromma, Danderyd, Enskede, Huddinge, Kungsholmen, Lidingö (2026-10-26).
Ny tjänst under villarenovering.html (TJ_HUB["totalrenovering"]). Intent: renovera hela huset eller hela
lägenheten på en gång – ordningen mellan arbetena, vad som kräver anmälan eller tillstånd och hur rotavdraget
fungerar för en stor ombyggnad. Skild från ortens byggforetag-<ort>.html (lov, nybyggnad, vind, tomt, byggplatsen),
badrumsrenovering-<ort>.html och koksrenovering-<ort>.html (enskilda rum) – de länkas i stället.
Lokal vinkel per sida (en huvudfråga per sida, så att sidorna inte upprepar varandra):
Bromma – trädgårdsstädernas villor som byggts om invändigt i generationer: ordningen från rivning till ytskikt,
anmälan när kök eller badrum flyttas, förvanskningsförbudet även invändigt; Danderyd – villastäderna Djursholm och
Stocksund: riva varsamt, materialinventering, sortering av rivningsavfallet och återbruk, kommunens råd om fönster
och dörrar; Enskede – Gamla Enskede: renovera ett nyköpt hus innan inflyttning (Skatteverkets regel om nyköpt
bostad, lagfart, ägarskap, elektronisk betalning); Huddinge – grupphus och radhus från 1960–80-talet: asbest och
PCB i hus från rekordåren, bärande väggar enligt kommunen; Kungsholmen – bostadsrätten: styrelsens tillstånd enligt
bostadsrättslagen 7 kap. 7 §, störningar för grannarna (7 kap. 9 §), rotavdrag innanför tak, väggar och golv;
Lidingö – bygga om i stället för att riva: Skatteverkets krav på att större delen av stommen behålls, stadens
anmälningslista och slutbesked, kulturmiljöprogrammets inventeringar.
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-26:
  Skatteverket (Så fungerar rotavdraget: högst 30 procent av arbetskostnaden, material och resor ger inget avdrag,
  äga bostaden under perioden arbetet utförs, nyköpt bostad – ingen annan bor där och du flyttar in direkt efter
  renoveringen, inte för att hyra ut eller sälja, lagfart inom tre månader, köpehandlingar om lagfart saknas,
  femårsregeln och värdeåret, i bostadsrätt bara arbete inne i bostaden, flera ägare kan dela men sammanlagt högst
  30 procent, 75 000 / 50 000 kr, elektronisk betalning sedan 1 januari 2020, bara arbetad tid på plats; Ger
  arbetet rätt till rotavdrag?: bygga om och bygga till i småhus – större delen av den ursprungliga stommen ska
  behållas, riva väggar och bygga om planlösningen, tilläggsisolering, montera fast köks- och badrumsinredning och
  installera vitvaror i samband med omfattande byggarbete eller renovering, inget avdrag för att riva ett hus även om
  ett nytt byggs på den gamla stommen eller för bygglovshandlingar, arkitekt, kvalitetsansvarig, besiktningsman;
  sanera asbest och radon i samband med byggarbete – men inget avdrag för att mäta fukt, radon och asbest; byggstäda grovsopor; modernisera el
  och installera elcentraler; dra in och reparera el-, vatten- och avloppsledningar; bostadsrätt – innanför tak,
  väggar och golv, stadgarnas underhållsansvar, undantag när två bostadsrätter slås ihop eller tvärtom, bostadsytan
  utökas eller oinredd biyta görs om, riva innerväggar och bygga om lägenhetens planlösning, inget avdrag för balkong),
  Riksdagen (bostadsrättslag 1991:614, 7 kap. 7 § – punkterna 1–5, kulturvärden kräver alltid tillstånd, styrelsen får
  vägra bara vid påtaglig skada eller olägenhet, villkor, hyresnämnden; 7 kap. 9 § – störningar som inte skäligen bör
  tålas),
  Stockholms stad, bygglov.stockholm (Flytta kök eller badrum – inget bygglov, anmälan och startbesked om bärande
  konstruktion, brandskydd, ventilation eller ny VA-stam, kanalmått för kombinerad imkanal, rådgör med sotaren,
  bostadsrätt kan behöva föreningens tillstånd; Ändra planlösningen i en byggnad – anmälan om tekniska egenskapskrav
  påverkas, bygglov för att dela en lägenhet, ingen anmälan om bara rummens användning ändras, kontakta styrelsen i god
  tid, Stadsmuseets karta – inte alla byggnader inventerade; Ändra i bärande konstruktion – ritningar kan vara
  ofullständiga och det är inte säkert att de som byggt följt dem, kontakta konstruktör),
  Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf med text: Gamla Enskede första trädgårdsstaden,
  Hallmans stadsplan 1908, 1920-talets trädgårdsstäder i Äppelviken, Ålsten och Smedslätten, Enskedestugan,
  friliggande enfamiljshus i ett plan med delvis inredd vind, Södra Ängby sista och ett av Europas största
  sammanhängande områden av 1930-talsvillor i modernistisk stil, Gamla Enskede, Ålstensgatan och Södra Ängby
  riksintressen, många hus förändrade interiört och tillbyggda),
  Stockholms stad – Områdesfakta (pdf med text: Ålsten 2025 – 1 106 bostäder, 911 i småhus; Smedslätten 2025 – 980
  bostäder, 515 i småhus; Gamla Enskede 2025 – 5 117 bostäder, 923 i småhus, 2 360 bostadsrätter; Kungsholmens
  stadsdelsområde 2024 – 44 554 bostäder, 30 598 bostadsrätter, 337 i småhus, 5 265 lägenheter utan kök och 11 314
  ettor i flerbostadshus),
  Boverket (Förvanskningsförbudet – alla ändringar exteriört och interiört, oberoende av lov- och anmälningsplikt,
  inget förändringsförbud, sakkunnig hjälp; Risker med asbest i byggnader – förbud 1982, främst 1940–1970 men
  1940–1980 sannolikt, listan med kakel- och klinkerfix, socklar i badrum, mattor, lim, golvmassor, rörisolering,
  fönsterkitt, puts, väggskivor, ventilationskanal, fogmassor, färger, vatten- och avloppsrör, bunden form ingen fara,
  sågning/slipning/borrning frigör fibrer, prov i mikroskop, dolda bakom golvmattor och kakel, sanering kräver
  tillstånd från Arbetsmiljöverket),
  Naturvårdsverket (Materialinventering och sortering av bygg- och rivningsavfall – byggherren yttersta ansvaret,
  materialinventering bör alltid göras, trä, mineral, metall, glas, plast och gips sorteras ut på platsen, farligt
  avfall åtskilt och väderskyddat, tegel, konstruktionsvirke, dörrar, fönsterkarmar, beslag, sanitetsgods och
  takpannor kan återanvändas; PCB – nyanvändning förbjuden sedan 1978, inventering av byggnader byggda eller ombyggda
  1956–1973, en- och tvåbostadshus som ägs av fysiska personer berörs inte, fog- och golvmassor),
  Danderyds kommun (Riktlinjer för kulturhistoriska byggnader och miljöer 2024, pdf med text – Kulturmiljökartan,
  fönster och dörrar renoveras hellre än byts, vårdat skick, varsamhet även utan skydd, tidig kontakt för
  rådgivning vid ändringar på eller inom fastigheten; Översiktsplan kap. 3, pdf med text – riksintresse sedan 1987,
  Djursholm landets första som förort anlagda villastad, 1890–1930, stilideal från trävillor till funktionalism),
  Huddinge kommun (Ändra en byggnads bärande konstruktion – anmälan och startbesked, flytta eller ta upp öppningar,
  ändra hur laster tas emot, konstruktör, tillstånd från bostadsrättsförening, entréplan tillgängligt och dagsljus,
  ritningar i bygglovsarkivet stämmer inte säkert; Kulturmiljöprogram del 2, pdf med text – grupphusområden byggda av
  byggbolag på 1960-talet, prefabricerat, 1965–1975 en tredjedel av de nya bostäderna i småhus, radhus i slutet av
  1970-talet och början av 1980-talet i Sörskogen och Utsälje, Östra Skogås terränganpassade småhus),
  Lidingö stad (Vad vill du göra? – anmälningslistan: rivning av byggnad eller del av byggnad med byggnadsarea över 50
  kvadratmeter, bärande delar, brandskydd, hiss, eldstad, rökkanal, ventilation, vatten och avlopp, startbesked och
  slutbesked; Frågor och svar om kulturmiljöprogrammet – inventeringar 1970–80-talet och 2013–2015 via kundcenter,
  nio byggnadsminnen, länsstyrelsen beslutar och ger tillstånd, förvanskning även utan bygglov).
Strukna (ej verifierade eller medvetet utelämnade): Elsäkerhetsverkets regler om vem som får utföra
elinstallationer (inte öppnad i primärkälla – sajtens egen formulering "el och VVS via behöriga" används i stället);
att Ålsten är riksintresse (vägledningen skriver Ålstensgatan – så skrivet); Södra Ängbys bostadsantal (inte
öppnat i den här omgången); att Gamla Enskedes hus har tomträtt (ingen källa öppnad); att husen i Huddinges
grupphusområden innehåller asbest eller PCB (skrivs som Boverkets sannolikhet för byggåren och som villkor); att
radhus i Huddinge ägs av föreningar (ingen källa – PCB-undantaget skrivs bara med Naturvårdsverkets ord); teak i
1970-talsvillor (onödig detalj); Boverkets lista över asbest i takpannor och fasadskivor (gäller exteriören, inte
den här sidan); avgifter för anmälan, lagfart och tillstånd, handläggningstider, tidsåtgång och priser.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert. Perks enbart sajtens befintliga: gratis
platsbesök, skriftligt kostnadsförslag, ROT direkt på fakturan, en kontakt/total entreprenad, el och VVS via behöriga.
Kritikpass 2026-10-26: alla källor öppnade på nytt och varje faktamening kontrollerad. Rättat: att mäta asbest ger
INTE rotavdrag (Skatteverkets lista "Inget avdrag ges för att … mäta fukt, radon och asbest") – Danderyd och Huddinge
omskrivna; "en tredjedel av de nya bostäderna i landet" -> källans formulering plus att Huddinge fick större andel
flerbostadshus; "efter förebilden Gamla Enskede" -> "efter Gamla Enskede som var stadens första"; PCB "ofta fog- och
golvmassor" -> vägledningen tar upp fog- och golvmassor; hänsynsreglerna med Boverkets ord; sammanslagning av två
bostadsrätter skrivet som undantag från kravet innanför tak, väggar och golv; Lidingö – ombyggnad/nytt hus skrivet
utan egen tolkning, FAQ om rivning till stadens lydelse (byggnad eller del av byggnad över 50 m² byggnadsarea),
inventeringarna "be att få ta del av"; Enskede – köpehandlingar "inte hunnit ansöka om lagfart", "aldrig" ->
"inte"; Huddinge-ledet utan generalisering om husens planlösning; Kungsholmen – "alltid tillstånd" omskrivet utan att
ändra innebörden.
Kritikpass 2 2026-10-26: alla 21 källor öppnade igen (curl; alla pdf:er har text). Rättat: Bromma – "ingen anmälan
om bara rummens användning ändras" (källan gäller inom en lägenhet) ersatt med stadens krav att tekniska
egenskapskrav ska uppfyllas oavsett anmälan; Danderyd – "måste saneringen göras av ett företag med tillstånd"
-> Boverkets lydelse (företag som river/sanerar asbest måste ha tillstånd; i regel prov i mikroskop),
ekonomiskt värde även "höga kulturhistoriska värden", Kulturmiljökartan i kulturmiljöhandboken, "oftast" -> "ofta";
Enskede – typritningar/Enskedestugan/enfamiljshus i ett plan anges som vägledningens text om trädgårdsstäderna i
stort (inte bara Gamla Enskede), "små hus" och "den bästa tiden" strukna, "hunnit få lagfart" -> "hunnit ansöka om
lagfart", "Det krav" -> "Det kravet"; Huddinge – "kedjehus" ur rubriken (källan: folkhemsbygget 1940–60),
"just de material Boverket listar" -> "många av", hänsynsreglerna med Boverkets lydelse, "Många grupphus har slutna
kök" struket; Kungsholmen – "nästan allt" -> "ofta flera", flerbostadshus och övriga hus, 7 kap. 7 § andra
stycket med alla fyra värden ("varje åtgärd" = lagens "alltid"), 9 § "eller annars", grannar "gärna", balkong enligt Skatteverkets
lista; Lidingö – 50 m² gäller byggnadens byggnadsarea (aside och FAQ rättade), slutbesked "om nämnden inte
beslutar annat", stommen utan egen tolkning, "Ofta mycket att vinna" struket, bärande delar "väsentligt".
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

# ------------------------------------------------------------------ gemensamma källor
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV_JOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap.",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SB_KOKBAD = ("Stockholms stad – Flytta kök eller badrum",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/flytta-kok-eller-badrum/")
_SB_PLAN = ("Stockholms stad – Ändra planlösningen i en byggnad",
            "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/andra-planlosningen-i-en-byggnad/")
_SB_BAR = ("Stockholms stad – Ändra i bärande konstruktion",
           "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/andra-i-barande-konstruktion/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_OF_ALSTEN = ("Stockholms stad – Områdesfakta 2025: Ålsten (pdf)", _OF + "vasterort/bromma/alsten.pdf")
_OF_SMED = ("Stockholms stad – Områdesfakta 2025: Smedslätten (pdf)", _OF + "vasterort/bromma/smedslatten.pdf")
_OF_GENSK = ("Stockholms stad – Områdesfakta 2025: Gamla Enskede (pdf)", _OF + "soderort/enskede/gamla-enskede.pdf")
_OF_KUNGS = ("Stockholms stad – Områdesfakta: Kungsholmens stadsdelsområde (pdf)",
             _OF + "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade.pdf")
_BOV_FORV = ("Boverket – PBL kunskapsbanken: Förvanskningsförbudet",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/teman/kulturvarden/kulturvarden-i-plan---och-bygglagen/krav-pa-byggnadsverk-och-tomter/forvanskningsforbudet/")
_BOV_ASB = ("Boverket – Risker med asbest i byggnader",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_NV_SORT = ("Naturvårdsverket – Materialinventering och sortering av bygg- och rivningsavfall",
            "https://www.naturvardsverket.se/vagledning-och-stod/avfall/bygg--och-rivningsavfall/materialinventering-och-sortering/")
_NV_PCB = ("Naturvårdsverket – Vägledning om PCB",
           "https://www.naturvardsverket.se/vagledning-och-stod/kemikalier/pcb/")
_DAND_RIKT = ("Danderyds kommun – Riktlinjer för kulturhistoriska byggnader och miljöer i Danderyd 2024 (pdf)",
              "https://www.danderyd.se/globalassets/globala-filer/kommun-och-politik/ovriga-styrdokument-ny/styrande-dokument---samhallsbyggnad-miljo-och-exploatering/riktlinjer-for-kulturmiljohistoriska-byggnader-och-miljoer-i-danderyd-2024.pdf")
_DAND_OP = ("Danderyds kommun – Översiktsplan, kap. 3 Riks- och mellankommunala intressen (pdf)",
            "https://danderyd.se/contentassets/94fc6956dc264c4cab52c0a18ff5bafd/3-riks--och-mellankommunala-intressen.pdf")
_HUD_BAR = ("Huddinge kommun – Ändra en byggnads bärande konstruktion",
            "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/andra-en-byggnads-barande-konstruktion")
_HUD_KMP = ("Huddinge kommun – Kulturmiljöprogram, del 2 (pdf)",
            "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf")
_LID_VAD = ("Lidingö stad – Bygglov och anmälan: Vad vill du göra?", "https://lidingo.se/bygga-bo/bygglov/vad-vill-du-gora/")
_LID_KMP = ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet",
            "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/")

_ROT_SUM = ("Företaget får dra av högst 30 procent av arbetskostnaden på fakturan. Rotavdraget är högst 50 000 kr "
            "per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag.")

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"totalrenovering-bromma.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Bromma", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Bromma – ordningen när hela villan görs om",
  "description": "Totalrenovering i Bromma: villor i trädgårdsstäderna som görs om invändigt – arbetenas ordning, anmälan när kök eller badrum flyttas och rotavdraget.",
  "h1": "Totalrenovering i Bromma",
  "lead": "När kök, badrum, el, rör och ytskikt i en villa ska göras om samtidigt avgör ordningen mellan arbetena både tidplanen och slutresultatet. Geal Entreprenad AB tar totalrenoveringar i Brommas villor och radhus som en total entreprenad, med en kontakt för hela projektet från första rivningen till sista listen.",
  "card": "Hela villan i rätt ordning.",
  "sections": [
    {"id": "husen-bromma", "anchor": "Husen",
     "h2": "Villor som byggts om invändigt i generationer",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver hur trädgårdsstäderna i Äppelviken, Ålsten och Smedslätten tillkom på 1920-talet, efter Gamla Enskede som var stadens första. Södra Ängby blev den sista stadsdelen som planerades efter trädgårdsstadens principer och är enligt vägledningen ett av Europas största sammanhängande områden av villor från 1930-talet i modernistisk stil. Ålstensgatan och Södra Ängby är dessutom utpekade som riksintressen.",
       "Om trädgårdsstäderna skriver vägledningen också att många hus har förändrats interiört och byggts till genom åren för att bättre motsvara moderna behov. I stadens områdesfakta för 2025 ligger 911 av Ålstens 1 106 bostäder i småhus, och i Smedslätten 515 av 980.",
       "För en totalrenovering betyder det att man sällan öppnar upp ett hus som bara har en historia. Bakom en vägg kan det finnas en dörr som satts igen, under golvet en rördragning från ett tidigare badrum. Staden påpekar att gamla ritningar kan vara ofullständiga och att det inte är säkert att de som byggde följde dem, så vi planerar arbetet först när vi har sett konstruktionen på plats.",
     ],
     "aside": {"title": "Bromma i siffror 2025", "items": [
       "Ålsten: 911 av 1 106 bostäder i småhus", "Smedslätten: 515 av 980", "Södra Ängby och Ålstensgatan: riksintressen"]}},
    {"id": "ordning-bromma", "h2": "Från rivning till ytskikt – i en genomtänkt ordning",
     "paras": [
       "Vi lägger upp en totalrenovering så att varje arbete görs medan det är lätt att komma åt. Först rivs det som ska bort och huset inventeras. Därefter görs eventuella ändringar i stommen, som nya öppningar eller förstärkningar. Medan väggar och bjälklag är öppna drar elektriker och rörläggare nya ledningar, och ventilationen ses över. Först när installationerna är klara byggs badrum och kök, och sist kommer golv, väggytor, innertak och snickerier.",
       "Ordningen spelar roll för kvaliteten. Ett nytt golv som läggs innan rören är dragna riskerar att behöva brytas upp igen, och målade väggar tar skada av att elen dras efteråt. Därför tidsätter vi varje moment och bestämmer tillsammans med dig var i huset du kan bo, om du vill bo kvar under en del av tiden.",
     ],
     "aside": {"title": "Ordningen i korthet", "items": [
       "Rivning och inventering", "Stomme och öppningar", "El, VVS och ventilation", "Badrum och kök", "Golv, väggar och snickerier"]}},
    {"id": "anmalan-bromma", "h2": "Flytta kök eller badrum – när det krävs anmälan",
     "paras": [
       "Många totalrenoveringar börjar med en ny planlösning. Stockholms stad skriver att det inte krävs bygglov för att flytta kök eller badrum. Däremot kan det behövas en anmälan och ett startbesked om flytten påverkar den bärande konstruktionen eller brandskyddet, om ventilationen installeras eller ändras väsentligt eller om en ny stam för vatten och avlopp tillkommer.",
       "Ska badrummets ventilationskanal även användas som imkanal för köket behöver kanalens sammanlagda mått vara tillräckligt stort, och staden råder dig att tidigt rådgöra med skorstensfejarmästaren. Oavsett om flytten kräver anmälan eller inte ska arbetet enligt staden utföras så att de tekniska egenskapskraven i plan- och bygglagen uppfylls. Mer om just köket i äldre Brommahus finns under " + _L.format("koksrenovering-bromma.html", "köksrenovering i Bromma") + ", och om vind och bärande väggar under " + _L.format("byggforetag-bromma.html", "byggföretag i Bromma") + ".",
     ],
     "aside": None},
    {"id": "varsamhet-bromma", "h2": "Varsamhet även bakom fasaden",
     "paras": [
       "Boverket förklarar att förvanskningsförbudet i plan- och bygglagen gäller vid alla ändringar av en särskilt värdefull byggnad, både exteriört och interiört, och oavsett om åtgärden kräver lov eller anmälan. Det är samtidigt inget förändringsförbud – det är de egenskaper som gör byggnaden värdefull som är skyddade, och för att klarlägga dem kan sakkunnig hjälp behövas.",
       "På Stadsmuseets karta kan du se om fastigheten är utpekad som kulturhistoriskt värdefull, men staden påpekar att alla byggnader inte är inventerade. Innan något rivs går vi därför igenom huset med dig och noterar sådant som kan vara värt att spara, till exempel dörrar, foder, trappor och fasta skåp. Det som ska vara kvar skyddas under arbetet. Badrummet beskriver vi närmare under " + _L.format("badrumsrenovering-bromma.html", "badrumsrenovering i Bromma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till i Bromma",
  "steps": [
    ("Platsbesök", "Vi går igenom hela huset, öppnar där det behövs och ser hur stomme och installationer ser ut."),
    ("Plan och ordning", "Vi lägger upp rivning, stomme, installationer, rum och ytskikt i en tidplan."),
    ("Skriftligt kostnadsförslag", "Varje del redovisas för sig, så att du ser vad som är arbete och vad som är material."),
    ("Anmälan vid behov", "Påverkas bärande delar, brandskydd, ventilation eller VA-stam görs en anmälan innan arbetet startar."),
    ("Utförande", "Vi samordnar alla moment, och el och VVS utförs via behöriga."),
    ("Slutgenomgång", "Vi går igenom huset rum för rum tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Bromma",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att riva väggar och bygga om planlösningen och att tilläggsisolera. Avdrag ges också för att montera fast köks- och badrumsinredning och installera vitvaror när det görs i samband med en omfattande renovering.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Bromma?",
  "price": [
    "Hur mycket som ska rivas, om stommen ändras, hur mycket el och rör som ska bytas och vilken standard kök, badrum och ytskikt får väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("I vilken ordning görs arbetena vid en totalrenovering av en villa?",
     "Rivning och inventering först, sedan ändringar i stommen, därefter el, vatten, avlopp och ventilation medan allt är öppet. Badrum och kök byggs när installationerna är klara, och golv, väggar och snickerier kommer sist."),
    ("Behövs bygglov för att flytta köket i en villa i Bromma?",
     "Nej, enligt Stockholms stad krävs inte bygglov. En anmälan och ett startbesked kan dock behövas om flytten påverkar bärande konstruktion, brandskydd, ventilation eller om en ny VA-stam tillkommer."),
    ("Får ett kulturhistoriskt värdefullt hus i Bromma byggas om invändigt?",
     "Ja. Boverket skriver att förbudet gäller vid alla ändringar av en särskilt värdefull byggnad, både exteriört och interiört, oavsett lovplikt. Det är dock inget förändringsförbud."),
    ("Kan man lita på de gamla ritningarna till huset?",
     "Bara delvis. Stockholms stad påpekar att ritningar kan vara ofullständiga och att det inte är säkert att de som byggt har följt dem. Därför öppnar vi och kontrollerar på plats."),
    ("Kan badrummets ventilationskanal användas för köksfläkten?",
     "Bara om kanalens sammanlagda mått räcker för båda. Staden råder dig att tidigt fråga skorstensfejarmästaren om förutsättningarna för en ny eller ändrad kanal."),
  ],
  "sources": [_VARSAM, _OF_ALSTEN, _OF_SMED, _SB_BAR, _SB_KOKBAD, _SB_PLAN, _BOV_FORV, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska hela villan i Bromma renoveras?", "Boka ett gratis platsbesök, så går vi igenom huset och ordningen för arbetet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyrenoverat ljust vardagsrum i en äldre villa med öppen planlösning mot köket",
     "renovated living room in a 1920s Swedish garden-city villa opened up towards a new white kitchen, wide oiled pine floorboards, white painted mouldings and original panelled doors kept, multi-pane windows with garden view, soft daylight, empty, no people, no text, no letters"),
    ("Öppen planlösning med kamin och matplats",
     "interior of a Swedish 1930s villa during total renovation, wall studs exposed, new plastic water pipes and electrical cables neatly routed through the studs, subfloor visible, a step ladder and tool boxes on protective board, daylight from windows, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ DANDERYD
"totalrenovering-danderyd.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Danderyd", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Danderyd – riva varsamt, spara det bästa",
  "description": "Totalrenovering i Danderyd: villor i Djursholm och Stocksund – inventera före rivning, sortera avfallet och återbruka dörrar och fönster.",
  "h1": "Totalrenovering i Danderyd",
  "lead": "En totalrenovering börjar ofta med rivning, och i en äldre villa är det där mycket av husets värde kan gå förlorat eller räddas. Geal Entreprenad AB tar totalrenoveringar av villor i Danderyd som en total entreprenad och planerar rivningen lika noga som det som ska byggas nytt.",
  "card": "Riva varsamt, bygga om helt.",
  "sections": [
    {"id": "villastaderna-danderyd", "anchor": "Villastäderna",
     "h2": "Villastäder med riksintresse sedan 1987",
     "paras": [
       "Kommunens översiktsplan beskriver att Danderyd sedan 1987 har två större områden av riksintresse för kulturmiljövården: Djursholms villastad och Stocksunds villastad. Djursholm kallas landets första som förort anlagda villastad, och bebyggelsen speglar framför allt perioden 1890–1930, med stilideal som kan följas från de första enkla trävillorna till nationalromantik, jugend och funktionalism.",
       "Kommunens riktlinjer för kulturhistoriska byggnader och miljöer från 2024 vänder sig till dig som äger en fastighet. Där uppmanas du att söka på din adress i Kulturmiljökartan i kommunens kulturmiljöhandbok och att ta tidig kontakt med kommunen för rådgivning om du planerar ändringar på eller inom din fastighet. Riktlinjerna påminner också om att åtgärder ska utföras varsamt även om fastigheten inte har något utpekat skydd, och att du som ägare är skyldig att hålla byggnaderna i vårdat skick.",
     ],
     "aside": {"title": "Före rivningen", "items": [
       "Sök adressen i Kulturmiljökartan", "Kontakta kommunen för råd", "Inventera material och detaljer"]}},
    {"id": "inventering-danderyd", "h2": "Inventera innan något rivs",
     "paras": [
       "Naturvårdsverket skriver att rivning ska ske planerat, kunnigt och varsamt, och att en materialinventering bör göras före bygg- och rivningsåtgärder. Vid inventeringen identifieras byggprodukter som kan återanvändas och vilket avfall som kan uppstå, inklusive farliga ämnen. Det är byggherren, alltså du som beställer arbetet, som har det yttersta ansvaret för avfallshanteringen.",
       "Boverket påminner om att asbest förbjöds i byggsektorn 1982 men att stora mängder finns kvar i byggnaderna. Asbest kan sitta i bland annat kakel- och klinkerfix, golvmattor och lim, rörisolering, fönsterkitt och puts, ibland dold bakom andra ytskikt. I regel krävs att ett prov analyseras i mikroskop för att veta om materialet innehåller asbest. Företag som river och sanerar asbest måste ha tillstånd från Arbetsmiljöverket, och hittas asbest anlitar vi ett sådant företag för saneringen.",
     ],
     "aside": None},
    {"id": "sortering-danderyd", "h2": "Sortering och återbruk på tomten",
     "paras": [
       "Enligt avfallsförordningen, som Naturvårdsverket redogör för, ska den som producerar bygg- och rivningsavfall sortera ut trä, mineral, metall, glas, plast och gips och hålla dem åtskilda. Sorteringen ska ske där avfallet uppkommer, alltså vid huset. Farligt avfall ska hållas skilt från annat avfall, förvaras väderskyddat och så att ingen utomstående kommer åt det.",
       "Naturvårdsverket nämner också att tegel och konstruktionsvirke kan sparas vid ombyggnad, liksom dörrar, fönsterkarmar, beslag och sanitetsgods. I praktiken innebär det att vi monterar ned sådant som ska användas igen i stället för att bryta loss det, märker delarna och förvarar dem torrt tills de sätts tillbaka.",
     ],
     "aside": {"title": "Sorteras på plats", "items": [
       "Trä", "Mineral – betong, tegel, klinker", "Metall och glas", "Plast och gips", "Farligt avfall för sig"]}},
    {"id": "fonster-danderyd", "h2": "Fönster och dörrar – renovera hellre än byta",
     "paras": [
       "Kommunens riktlinjer lyfter fram äldre byggnadsdetaljer som fönster och dörrar. De har generellt ett högt kulturhistoriskt värde, håller ofta hög kvalitet och kan med fördel renoveras i stället för att bytas ut. Riktlinjerna noterar också att byggnader med höga kulturhistoriska värden och välbevarade byggnadsdetaljer ofta kan höja fastighetens ekonomiska värde.",
       "Vid en totalrenovering är det lätt att allt gammalt hamnar i containern. Vi föreslår i stället att fönster och innerdörrar bedöms var för sig, och att de som går att rädda renoveras medan resten av huset byggs om. Om fönstren finns mer under " + _L.format("fonsterrenovering-danderyd.html", "fönsterrenovering i Danderyd") + ". Kök och badrum beskrivs under " + _L.format("koksrenovering-danderyd.html", "köksrenovering i Danderyd") + " och " + _L.format("badrumsrenovering-danderyd.html", "badrumsrenovering i Danderyd") + ", och tillbyggnad och tomt under " + _L.format("byggforetag-danderyd.html", "byggföretag i Danderyd") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till i Danderyd",
  "steps": [
    ("Platsbesök", "Vi går igenom huset och noterar vad som ska bevaras, renoveras eller rivas."),
    ("Inventering", "Material som kan vara farliga provtas, och delar för återbruk märks upp."),
    ("Skriftligt kostnadsförslag", "Rivning, sanering, återbruk och nybyggnad redovisas som egna poster."),
    ("Varsam rivning", "Det som ska användas igen monteras ned, och avfallet sorteras vid huset."),
    ("Ombyggnad", "Stomme, installationer, rum och ytskikt i tur och ordning – el och VVS via behöriga."),
    ("Slutgenomgång", "Vi går igenom huset med dig och visar vad som har bevarats."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Danderyd",
  "rot": [
    "Enligt Skatteverket kan rotavdrag ges för att sanera asbest i samband med byggarbete, men inte för att mäta asbest. Byggstädning av grovsopor och material efter ett rotarbete räknas däremot som rotarbete.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Danderyd?",
  "price": [
    "Mängden som ska rivas, om material behöver provtas eller saneras, hur mycket som ska återbrukas och omfattningen av själva ombyggnaden påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad ska sorteras ut när en villa rivs invändigt?",
     "Enligt Naturvårdsverkets genomgång av avfallsförordningen trä, mineral, metall, glas, plast och gips. Farligt avfall hålls för sig. Sorteringen görs på platsen där avfallet uppkommer."),
    ("Vem ansvarar för rivningsavfallet vid en renovering?",
     "Naturvårdsverket skriver att byggherren har det yttersta ansvaret för avfallshanteringen. Som beställare är det alltså du, även om entreprenören sköter sorteringen."),
    ("Vilka delar av huset kan återanvändas efter rivningen?",
     "Naturvårdsverket nämner bland annat tegel, konstruktionsvirke, dörrar, fönsterkarmar, beslag och sanitetsgods."),
    ("Ska jag kontakta kommunen innan jag renoverar invändigt i Danderyd?",
     "Kommunens riktlinjer rekommenderar tidig kontakt för rådgivning om du planerar ändringar på eller inom fastigheten, särskilt om byggnaden finns med i kulturmiljöhandboken."),
    ("Ingår asbestsaneringen i rotavdraget vid en totalrenovering?",
     "Ja, Skatteverket godkänner rotavdrag för att sanera asbest när det görs i samband med byggarbete i bostaden."),
  ],
  "sources": [_DAND_OP, _DAND_RIKT, _NV_SORT, _BOV_ASB, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska villan i Danderyd totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom vad som ska sparas och vad som ska rivas innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Stor äldre villa med nyrenoverad hall, bevarade spegeldörrar och trätrappa",
     "renovated entrance hall of a large early 1900s Swedish national romantic villa, restored original panelled doors and a dark oak staircase kept, new light walls, herringbone oak floor, tall multi-pane window, soft daylight, empty, no people, no text, no letters"),
    ("Rum med svart kamin och grå träpanel",
     "several old wooden panelled interior doors and multi-pane window sashes carefully stacked on timber battens under a tarpaulin roof next to a Swedish villa under renovation, sorted piles of wood and metal behind, overcast daylight, no people, no text, no letters, no labels"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ENSKEDE
"totalrenovering-enskede.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Enskede", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Enskede – nyköpt hus före inflyttningen",
  "description": "Totalrenovering i Enskede: renovera ett nyköpt hus i Gamla Enskede innan ni flyttar in – vad som krävs för rotavdrag, lagfart och planering av tiden.",
  "h1": "Totalrenovering i Enskede",
  "lead": "En bra tid att renovera hela huset är mellan tillträdet och inflyttningen, när rummen står tomma. Geal Entreprenad AB tar totalrenoveringar av villor, radhus och bostadsrätter i Enskede som en total entreprenad, och vi hjälper dig att lägga upp arbetet så att det är klart när flyttlasset kommer.",
  "card": "Renovera innan ni flyttar in.",
  "sections": [
    {"id": "husen-enskede", "anchor": "Husen",
     "h2": "Gamla Enskede – Stockholms första trädgårdsstad",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver Gamla Enskede som Stockholms första trädgårdsstad, anlagd efter stadsplanedirektör Per Olof Hallmans stadsplan från 1908. Om trädgårdsstäderna i stort skriver vägledningen att typritningar togs fram för att få ett enhetligt uttryck, och att den mest kända är Enskedestugan. Huvuddelen av bebyggelsen var friliggande enfamiljshus i ett plan med delvis inredd vind, men radhus och parhus förekom också.",
       "Gamla Enskede är i dag en blandad stadsdel. I stadens områdesfakta för 2025 har stadsdelen 5 117 bostäder, varav 923 i småhus och 2 360 bostadsrätter. En totalrenovering kan alltså gälla både en liten villa med snedtak och en lägenhet i ett flerbostadshus.",
       "I ett hus med delvis inredd vind är varje kvadratmeter värdefull. När hela huset görs om samtidigt går det att planera om förvaring, trappa och badrum i ett sammanhang, i stället för att lösa ett rum i taget.",
     ],
     "aside": {"title": "Gamla Enskede 2025", "items": [
       "5 117 bostäder", "923 i småhus", "2 360 bostadsrätter", "Stadsplan från 1908"]}},
    {"id": "nykopt-enskede", "h2": "Rotavdrag för ett hus ni ännu inte bor i",
     "paras": [
       "Skatteverket skriver att du kan få rotavdrag för att renovera en bostad som du nyligen har köpt men ännu inte flyttat in i. Det förutsätter att ingen annan bor i bostaden när arbetet utförs och att du flyttar in direkt efter renoveringen. Köper du i stället en bostad för att hyra ut eller sälja den ges inget rotavdrag.",
       "Du måste äga bostaden under den tid som arbetet utförs. Skatteverket påminner om att lagfart ska sökas inom tre månader efter köpet, och om du inte hunnit ansöka om lagfart kan företaget behöva köpehandlingarna när det ansöker om utbetalningen. För en bostadsrätt behöver företaget i stället föreningens organisationsnummer och lägenhetsnumret.",
     ],
     "aside": None},
    {"id": "tiden-enskede", "h2": "Att hinna klart före flyttdagen",
     "paras": [
       "Vi börjar planera redan före tillträdet om du vill. Vid ett platsbesök under visningsperioden eller strax efter kontraktet går vi igenom huset och gör en första plan för vad som ska göras. När nycklarna är dina kan rivningen börja direkt.",
       "Ett tomt hus gör arbetet enklare: vi kan arbeta i flera rum samtidigt, och inget behöver flyttas fram och tillbaka. Det som tar längst tid är ofta beslut om kök, badrum och material, så de valen gör vi tillsammans tidigt. Om det blir trångt i tidplanen föreslår vi att badrum och kök blir klara först, så att huset går att bo i medan sista ytskikten görs. Badrum i husen beskrivs under " + _L.format("badrumsrenovering-enskede.html", "badrumsrenovering i Enskede") + " och köket under " + _L.format("koksrenovering-enskede.html", "köksrenovering i Enskede") + ".",
     ],
     "aside": {"title": "Före tillträdet", "items": [
       "Platsbesök och första plan", "Val av kök, badrum och material", "Tidplan mot flyttdagen"]}},
    {"id": "betalning-enskede", "h2": "Två ägare, en faktura",
     "paras": [
       "Köper ni huset tillsammans kan ni dela på rotavdraget, men enligt Skatteverket kan det sammanlagt inte bli högre än 30 procent av den totala arbetskostnaden. Om en av er redan har använt sitt utrymme för året kan företaget ansöka om utbetalning för någon annan i hushållet som också äger bostaden.",
       "Från och med den 1 januari 2020 måste betalningen vara elektroniskt spårbar för att rotavdrag ska ges, och först när arbetet är utfört och betalt kan företaget begära utbetalning från Skatteverket. Det är bara arbetad tid på plats hos dig som räknas. Gäller frågan i stället byggplatsen på gatan, container och träd finns mer under " + _L.format("byggforetag-enskede.html", "byggföretag i Enskede") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till i Enskede",
  "steps": [
    ("Platsbesök", "Gärna före tillträdet – vi går igenom huset och gör en första plan."),
    ("Val och tidplan", "Kök, badrum och material väljs tidigt, och tidplanen räknas bakåt från flyttdagen."),
    ("Skriftligt kostnadsförslag", "Arbete och material redovisas var för sig, så att rotavdraget blir tydligt."),
    ("Rivning", "När nycklarna är dina börjar vi riva det som ska bort."),
    ("Ombyggnad", "Installationer, badrum, kök och ytskikt i tur och ordning – el och VVS via behöriga."),
    ("Inflyttningsklart", "Vi går igenom huset med dig innan flyttlasset kommer."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Enskede",
  "rot": [
    "Rotavdrag ges för en nyköpt bostad som ingen annan bor i medan arbetet pågår, om du flyttar in direkt efter renoveringen. Du ska äga bostaden när arbetet utförs.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Enskede?",
  "price": [
    "Husets storlek och skick, hur mycket som rivs, omfattningen av el och rör och vilket kök och badrum du väljer avgör mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får man rotavdrag för att renovera ett hus man inte har flyttat in i än?",
     "Ja, enligt Skatteverket om ingen annan bor där när arbetet utförs och du flyttar in direkt efter renoveringen. Du ska äga bostaden under tiden."),
    ("Kan vi få rotavdrag om vi tänker sälja huset efter renoveringen?",
     "Nej. Skatteverket ger inget rotavdrag för arbete i en bostad som du inte tänker använda som din bostad, utan i stället hyra ut eller sälja."),
    ("Vad behöver företaget om vi inte har fått lagfart än?",
     "Köpehandlingarna. Skatteverket nämner dem som underlag när fastigheten är nyköpt och du inte har hunnit ansöka om lagfart."),
    ("Kan två ägare dela på rotavdraget?",
     "Ja, men tillsammans kan avdraget högst bli 30 procent av arbetskostnaden. Har den ena använt sitt utrymme kan företaget ansöka för en annan ägare i hushållet."),
    ("Hur ska vi betala för att få rotavdrag?",
     "Elektroniskt, så att betalningen går att spåra. Det kravet har gällt sedan den 1 januari 2020 enligt Skatteverket."),
  ],
  "sources": [_VARSAM, _OF_GENSK, _SKV_ROT, _SKV_JOB],
  "cta": ("Har ni köpt hus i Enskede?", "Boka ett gratis platsbesök, gärna före tillträdet, så lägger vi upp renoveringen mot flyttdagen och du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Liten nyrenoverad trävilla med ljust kök och trappa upp till vinden",
     "interior of a small renovated 1910s Swedish wooden cottage, compact new light grey kitchen along one wall, a steep painted wooden staircase leading up to a loft room under the sloping roof, wide pine floor, small multi-pane windows, empty and ready for moving in, soft daylight, no people, no text, no letters"),
    ("Tomt rum i ett äldre hus där golv och väggar är rivna inför renovering",
     "empty room in an old Swedish wooden house stripped for total renovation, old wallpaper removed to bare boards, floor taken up to the joists in one part, window with spring garden outside, broom and dust sheets in a corner, no furniture, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HUDDINGE
"totalrenovering-huddinge.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Huddinge", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Huddinge – grupphus från 60- och 70-talet",
  "description": "Totalrenovering i Huddinge: grupphus och radhus från 1960–80-talet – asbest och PCB före rivning, bärande väggar enligt kommunen och rotavdraget.",
  "h1": "Totalrenovering i Huddinge",
  "lead": "Ett grupphus eller radhus från rekordåren kan ha kök, badrum, el och ytskikt kvar från byggåret eller från en tidig renovering. När allt ska göras om på en gång är det husets ålder som styr vad som behöver undersökas innan något rivs. Geal Entreprenad AB tar totalrenoveringar i Huddinge som en total entreprenad med en kontakt för hela projektet.",
  "card": "Rekordårens hus inifrån och ut.",
  "sections": [
    {"id": "rekordaren-huddinge", "anchor": "Husen",
     "h2": "Grupphus och radhus från rekordåren",
     "paras": [
       "Kommunens kulturmiljöprogram beskriver hur villor under 1960-talet i större omfattning började byggas som grupphusområden, helt uppförda av byggbolag. Konceptet att köpa ett nyckelfärdigt hus hade skapats, och husen byggdes oftast prefabricerat med färdiga byggelement som monterades ihop på plats. Inom miljonprogrammets ramar, 1965–1975, uppfördes en tredjedel av de nya bostäderna i småhus och grupphus, men i Huddinge blev andelen flerbostadshus större.",
       "Som en motreaktion mot de stora flerbostadshusen byggdes radhus i slutet av 1970-talet och början av 1980-talet runt om i Huddinge, till exempel i Sörskogen söder om Huddinge centrum och i Utsälje vid Snättringe. Även Östra Skogås bebyggdes med terränganpassade småhus. 1970-talets villor beskrivs som större och av högre standard än egnahemsrörelsens enkla småhus.",
     ],
     "aside": {"title": "Huddinges småhusår", "items": [
       "1960-tal: grupphus av byggbolag", "1965–1975: miljonprogrammet", "Sent 1970-tal: radhus i Sörskogen och Utsälje"]}},
    {"id": "asbest-huddinge", "h2": "Asbest i hus från 1940 till 1980",
     "paras": [
       "Boverket skriver att det är sannolikt att det finns asbest någonstans i en byggnad som uppfördes under perioden 1940–1980. Rådet är att börja med husets byggår och tidigare renoveringar, och att leta i bygglovshandlingar och annan dokumentation. Det enda säkra sättet att veta är provtagning och analys.",
       "Många av de material som Boverket listar är sådana som rivs i en totalrenovering: kakel- och klinkerfix och fog, socklar i badrum, golv- och väggmattor med lim och underliggande skikt, golvmassor, rörisolering, fönsterkitt, väggskivor inomhus, ventilationskanaler och fogmassor. Så länge asbesten sitter i bunden form är den ingen fara, men när materialet sågas, slipas, borras eller skrapas kan fibrer frigöras och sväva i luften i många timmar. Därför provtas misstänkta material innan rivningen börjar, och hittas asbest saneras den av ett företag med tillstånd från Arbetsmiljöverket.",
     ],
     "aside": {"title": "Vanliga ställen enligt Boverket", "items": [
       "Kakelfix och fog", "Mattor och mattlim", "Rörisolering", "Fönsterkitt", "Väggskivor inomhus"]}},
    {"id": "pcb-huddinge", "h2": "PCB – vad som gäller för ett eget hus",
     "paras": [
       "PCB är en grupp giftiga och svårnedbrytbara ämnen som enligt Naturvårdsverket är förbjudna för nyanvändning sedan 1978. Reglerna om inventering gäller byggnader som byggts eller byggts om under åren 1956–1973, och vägledningen tar särskilt upp fog- och golvmassor som innehåller PCB.",
       "Naturvårdsverket skriver samtidigt att en- och tvåbostadshus som ägs av fysiska personer inte berörs av reglerna. Äger du själv din villa eller ditt radhus är du alltså inte skyldig att inventera för PCB. Boverket påminner dock om att miljöbalkens allmänna hänsynsregler gäller även för privatpersoner: den som vidtar en åtgärd som kan påverka människors hälsa eller miljön är skyldig att skaffa sig tillräcklig kunskap och vidta de skyddsåtgärder som behövs.",
     ],
     "aside": None},
    {"id": "barande-huddinge", "h2": "Öppna upp planlösningen – kommunens krav",
     "paras": [
       "Ska planlösningen i ett grupphus eller radhus öppnas upp är det kommunens regler om bärande konstruktion som gäller. Huddinge kommun skriver att det inte krävs bygglov för att bara ändra i den bärande konstruktionen, men att du behöver göra en anmälan och få ett startbesked om ändringen påverkar konstruktionen, till exempel om du flyttar eller tar upp öppningar i bärande väggar eller ändrar hur laster tas emot i tak och väggar. Är du osäker behöver du kontakta en konstruktör.",
       "Kommunen påpekar också att ritningar i bygglovsarkivet inte säkert stämmer med det som byggdes, och att vissa krav ska uppfyllas även när ingen anmälan behövs, bland annat att entréplanet ska vara tillgängligt och att vissa rum ska ha dagsljus. Bor du i ett radhus som är bostadsrätt kan du behöva föreningens tillstånd. Om tomt, grannar och lovärendet finns mer under " + _L.format("byggforetag-huddinge.html", "byggföretag i Huddinge") + ", och om rummen var för sig under " + _L.format("koksrenovering-huddinge.html", "köksrenovering i Huddinge") + " och " + _L.format("badrumsrenovering-huddinge.html", "badrumsrenovering i Huddinge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till i Huddinge",
  "steps": [
    ("Platsbesök", "Vi går igenom huset, tar reda på byggåret och vilka renoveringar som gjorts tidigare."),
    ("Provtagning", "Misstänkta material provtas innan något rivs."),
    ("Skriftligt kostnadsförslag", "Eventuell sanering, rivning och ombyggnad redovisas som egna poster."),
    ("Anmälan vid behov", "Ska bärande väggar öppnas tas underlag fram med konstruktör och anmälan görs."),
    ("Ombyggnad", "Installationer, rum och ytskikt i tur och ordning – el och VVS via behöriga."),
    ("Slutgenomgång", "Vi går igenom huset med dig när allt är klart."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Huddinge",
  "rot": [
    "Skatteverket godkänner rotavdrag för att modernisera el och installera elcentraler, dra in och reparera vatten- och avloppsledningar, riva väggar och bygga om planlösningen och sanera asbest i samband med byggarbete. Att mäta fukt, radon eller asbest ger däremot inget avdrag.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Huddinge?",
  "price": [
    "Om material behöver provtas eller saneras, om bärande väggar ska öppnas och hur mycket el, rör och ventilation som byts påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste jag inventera PCB innan jag renoverar mitt radhus?",
     "Inte om du som privatperson äger ett en- eller tvåbostadshus. Naturvårdsverket skriver att sådana hus inte berörs av reglerna om inventering."),
    ("Var i ett 1970-talshus kan det finnas asbest?",
     "Boverket nämner bland annat kakelfix och fog, socklar i badrum, mattor och mattlim, golvmassor, rörisolering, fönsterkitt, väggskivor och fogmassor. Bara ett prov ger säkert besked."),
    ("Är asbest farligt om den sitter kvar i väggen?",
     "Inte så länge den sitter i bunden form, enligt Boverket. Risken uppstår när materialet sågas, slipas, borras eller skrapas så att fibrer frigörs."),
    ("Behövs bygglov för att ta bort en bärande vägg i Huddinge?",
     "Nej, men enligt kommunen en anmälan och ett startbesked om ändringen påverkar konstruktionen. Kontakta en konstruktör om du är osäker."),
    ("Vilka krav gäller även om ingen anmälan behövs?",
     "Huddinge kommun nämner bland annat att entréplanet ska vara tillgängligt och att vissa rum behöver dagsljus."),
  ],
  "sources": [_HUD_KMP, _HUD_BAR, _BOV_ASB, _NV_PCB, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska huset i Huddinge totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom husets ålder, material och planlösning innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyrenoverat radhus från 1970-talet med öppen planlösning mellan kök och vardagsrum",
     "renovated interior of a 1970s Swedish terraced house, wall between kitchen and living room removed and replaced by a painted steel beam, new white kitchen with wooden worktop, light oak floor throughout, large window towards a small garden and pine trees, empty, soft daylight, no people, no text, no letters"),
    ("Rivet badrum i ett äldre hus med gammal klinker och rörisolering synlig",
     "stripped bathroom in a 1970s Swedish house during renovation, old brown floor tiles partly removed showing grey adhesive, old pipe insulation visible on exposed pipes, walls opened to the studs, plastic sheeting sealing the doorway, work light, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ KUNGSHOLMEN
"totalrenovering-kungsholmen.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Kungsholmen", "svc_label": "Totalrenovering",
  "title": "Totalrenovering på Kungsholmen – hela bostadsrätten",
  "description": "Totalrenovering på Kungsholmen: renovera hela bostadsrätten – styrelsens tillstånd, hänsyn till grannarna, anmälan vid ny planlösning och rotavdraget.",
  "h1": "Totalrenovering på Kungsholmen",
  "lead": "När en lägenhet ska göras om från golv till tak berörs ofta flera av de åtgärder som bostadsrättslagen kräver styrelsens tillstånd för. Geal Entreprenad AB totalrenoverar bostadsrätter på Kungsholmen och sköter underlaget till styrelsen, samordningen i huset och arbetet i lägenheten med en kontakt för hela projektet.",
  "card": "Hela lägenheten från golv till tak.",
  "sections": [
    {"id": "bostaderna-kungsholmen", "anchor": "Bostäderna",
     "h2": "En stadsdel av bostadsrätter",
     "paras": [
       "Stadens områdesfakta för Kungsholmens stadsdelsområde visar 44 554 bostäder år 2024. Av dem är 30 598 bostadsrätter, medan bara 337 ligger i småhus. Bland lägenheterna i flerbostadshus och övriga hus finns 5 265 utan kök och 11 314 ettor.",
       "Med de siffrorna gäller en totalrenovering här oftast en lägenhet i ett flerbostadshus, och många av lägenheterna är små, så varje förändring av planlösningen märks. Att flytta ett kök, göra plats för ett större badrum eller bygga in en sovalkov påverkar både lägenheten och huset, och därför börjar arbetet i föreningen, inte med rivningen.",
     ],
     "aside": {"title": "Kungsholmen 2024", "items": [
       "44 554 bostäder", "30 598 bostadsrätter", "337 i småhus", "5 265 lägenheter utan kök"]}},
    {"id": "styrelsen-kungsholmen", "h2": "Det styrelsen ska säga ja till",
     "paras": [
       "Enligt bostadsrättslagen 7 kap. 7 § får du inte utan styrelsens tillstånd göra ingrepp i en bärande konstruktion, installera eller ändra ledningar för avlopp, värme, gas eller vatten, installera eller ändra ventilation, ändra eldstad eller rökkanal eller på annat sätt påverka brandskyddet, eller göra någon annan väsentlig förändring av lägenheten. Har lägenheten särskilda historiska, kulturhistoriska, miljömässiga eller konstnärliga värden krävs tillstånd för varje åtgärd som påverkar ett sådant värde.",
       "Styrelsen får vägra bara om åtgärden är till påtaglig skada eller olägenhet för föreningen, och ett tillstånd får förenas med villkor. Är du missnöjd med beslutet kan du begära att hyresnämnden prövar frågan. I en totalrenovering berörs oftast flera punkter samtidigt, så vi tar fram en samlad beskrivning med ritning som du lämnar till styrelsen innan något bokas.",
       "Ska köket flyttas till en annan del av lägenheten är ventilationen ofta den svåra frågan. Stockholms stad påpekar att ett kök behöver tillräcklig frånluft och ska uppfylla kraven för imkanal, och att badrumskanalens sammanlagda mått måste räcka om den ska användas som kombinerad imkanal och frånluftskanal. Staden råder dig att tidigt rådgöra med skorstensfejarmästaren, och i en bostadsrätt att kontakta styrelsen innan du börjar planera flytten.",
     ],
     "aside": {"title": "Kräver tillstånd (7 kap. 7 §)", "items": [
       "Bärande konstruktion", "Avlopp, värme, gas och vatten", "Ventilation", "Eldstad, rökkanal och brandskydd", "Annan väsentlig förändring"]}},
    {"id": "anmalan-kungsholmen", "h2": "Anmälan och bygglov vid ny planlösning",
     "paras": [
       "Stockholms stad skriver att du behöver göra en anmälan och vänta på startbesked om ändringen påverkar byggnadens tekniska egenskaper, till exempel bärande konstruktion, brandskydd eller ventilation. Vill du dela en lägenhet i två krävs bygglov, eftersom det då tillkommer en bostad. Ändrar du bara hur rummen används och inga tekniska egenskapskrav påverkas behövs ingen anmälan.",
       "Staden råder dig att kontakta styrelsen i god tid och att gärna informera grannarna om vad du planerar. Om badrummet och stammarna i husen finns mer under " + _L.format("badrumsrenovering-kungsholmen.html", "badrumsrenovering på Kungsholmen") + ", om golven under " + _L.format("golvlaggare-kungsholmen.html", "golvläggare på Kungsholmen") + " och om väggar och tak under " + _L.format("malare-kungsholmen.html", "målare på Kungsholmen") + ".",
     ],
     "aside": None},
    {"id": "grannarna-kungsholmen", "h2": "Hänsyn till grannarna under bygget",
     "paras": [
       "Bostadsrättslagen 7 kap. 9 § säger att du ska se till att de som bor omkring inte utsätts för störningar som i sådan grad kan vara skadliga för hälsan eller annars försämra deras bostadsmiljö att de inte skäligen bör tålas. Du ska också rätta dig efter de särskilda regler som föreningen meddelar.",
       "I praktiken handlar det om att planera de bullriga momenten, skydda trapphus och hiss och hålla dammet inne i lägenheten. Vi går igenom föreningens ordningsregler innan arbetet börjar, lägger rivning och bilning på de tider som gäller och sätter upp information i trapphuset om vad som pågår.",
       "Ordningen i lägenheten följer samma logik som i ett hus, men på mindre yta. Först rivs det som ska bort och material som ska sparas skyddas. Sedan dras nya ledningar och ventilation medan väggar och golv är öppna, därefter byggs badrum och kök och sist läggs golv och målas väggar och tak. I en liten lägenhet går det sällan att bo kvar under arbetet, så vi räknar tidplanen så att du vet när du kan flytta tillbaka.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till på Kungsholmen",
  "steps": [
    ("Platsbesök", "Vi går igenom lägenheten och föreningens regler för renovering."),
    ("Underlag till styrelsen", "Ritning och beskrivning av alla åtgärder som kräver tillstånd."),
    ("Skriftligt kostnadsförslag", "Varje del redovisas för sig, med arbete och material åtskilda."),
    ("Anmälan vid behov", "Påverkas tekniska egenskaper görs en anmälan innan arbetet startar."),
    ("Utförande", "Trapphus och hiss skyddas, och el och VVS utförs via behöriga."),
    ("Slutgenomgång", "Vi går igenom lägenheten med dig och lämnar underlag till föreningen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering på Kungsholmen",
  "rot": [
    "I en bostadsrätt ger Skatteverket rotavdrag för arbete innanför lägenhetens tak, väggar och golv som du ansvarar för enligt stadgarna, till exempel att riva innerväggar och bygga om planlösningen. Undantag gäller bland annat när två bostadsrätter slås ihop eller delas, när bostadsytan utökas eller när en oinredd biyta blir bostad. Att bygga om, reparera eller underhålla en balkong ger inget avdrag.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Kungsholmen?",
  "price": [
    "Hur mycket av planlösningen som ändras, om ledningar och ventilation berörs, föreningens krav på skydd och arbetstider och vilken standard du väljer påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka åtgärder i en totalrenovering kräver styrelsens tillstånd?",
     "Enligt bostadsrättslagen ingrepp i bärande konstruktion, ändrade ledningar för avlopp, värme, gas eller vatten, ändrad ventilation, ändringar som påverkar brandskyddet och annan väsentlig förändring av lägenheten."),
    ("Får styrelsen säga nej till min renovering?",
     "Bara om åtgärden är till påtaglig skada eller olägenhet för föreningen. Styrelsen kan sätta villkor, och du kan begära att hyresnämnden prövar beslutet."),
    ("Behövs bygglov för att dela en lägenhet på Kungsholmen?",
     "Ja. Stockholms stad skriver att det krävs bygglov när en bostadslägenhet delas i två eller flera, eftersom det då tillkommer bostäder."),
    ("Ger det rotavdrag att slå ihop två bostadsrätter?",
     "Det kan det göra. Skatteverket nämner det som ett undantag från kravet att arbetet ska ligga innanför lägenhetens tak, väggar och golv. Övriga villkor för rotavdrag gäller som vanligt."),
    ("Vad säger lagen om buller och damm under renoveringen?",
     "Bostadsrättslagen kräver att grannarna inte utsätts för störningar som de inte skäligen bör tåla, och att du följer föreningens särskilda regler."),
  ],
  "sources": [_OF_KUNGS, _BRL, _SB_PLAN, _SB_KOKBAD, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska bostadsrätten på Kungsholmen totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom lägenheten och vad styrelsen behöver innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyrenoverad lägenhet i ett äldre stenhus med öppet kök och fiskbensparkett",
     "renovated apartment in a 1930s Stockholm stone building, open kitchen in pale green with white stone worktop joined to the living room, oak herringbone parquet, deep window niches with radiators below, view of a courtyard with brick facades, empty, soft daylight, no people, no text, no letters"),
    ("Trapphus och hissdörr skyddade med skivor och plast under en lägenhetsrenovering",
     "stairwell of an old Stockholm apartment building with the stone stairs and lift doors protected by hardboard sheets and plastic film during an apartment renovation, an open apartment door with dust barrier plastic, warm stairwell light, no people, no text, no letters, no signs"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ LIDINGÖ
"totalrenovering-lidingo.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Lidingö", "svc_label": "Totalrenovering",
  "title": "Totalrenovering på Lidingö – bygga om utan att riva huset",
  "description": "Totalrenovering på Lidingö: bygga om villan i stället för att riva – stommen och rotavdraget, anmälan och slutbesked och stadens inventeringar.",
  "h1": "Totalrenovering på Lidingö",
  "lead": "När en villa är sliten genom hela huset kommer frågan om det är bättre att riva och bygga nytt. Ett alternativ är att behålla stommen och bygga om resten. Geal Entreprenad AB tar totalrenoveringar av villor på Lidingö som en total entreprenad, och vi hjälper dig att se var gränsen går – både tekniskt och för rotavdraget.",
  "card": "Behåll stommen, bygg om resten.",
  "sections": [
    {"id": "stommen-lidingo", "anchor": "Stommen",
     "h2": "Ombyggnad eller rivning – stommen avgör",
     "paras": [
       "Skatteverket ställer ett tydligt krav för att arbete med att bygga om och bygga till ett småhus ska ge rotavdrag: större delen av den ursprungliga byggnadsstommen på huset ska behållas, och huset ska vara äldre än fem år. Att riva ett hus ger inget avdrag, inte ens om ett nytt byggs upp på den gamla stommen.",
       "Gränsen påverkar alltså hur projektet ska läggas upp. Kan bjälklag, ytterväggar och tak stå kvar medan rummen byggs om inifrån, behålls mycket av stommen. Ska större delen av stommen bort uppfylls inte Skatteverkets krav, och för att bygga ett helt nytt hus ges inget rotavdrag. Vi bedömer stommen tidigt, innan några beslut om rivning fattas.",
       "Femårsregeln är sällan ett problem på äldre villor, men Skatteverket påpekar att det är husets värdeår som räknas. Det framgår av det senaste fastighetstaxeringsbeslutet.",
     ],
     "aside": {"title": "Rotavdrag eller inte", "items": [
       "Behålla större delen av stommen: ja", "Riva och bygga nytt: nej", "Bygglovshandlingar och arkitekt: nej"]}},
    {"id": "anmalan-lidingo", "h2": "Det staden vill ha anmält",
     "paras": [
       "Lidingö stad listar de åtgärder som kräver anmälan till miljö- och stadsbyggnadskontoret. Det gäller bland annat rivning av en byggnad eller en del av en byggnad, om byggnaden har en byggnadsarea som är större än 50 kvadratmeter, ändringar som väsentligt påverkar de bärande delarna eller brandskyddet, och installation eller väsentlig ändring av hiss, eldstad, rökkanal, ventilation, vattenförsörjning eller avlopp.",
       "En anmälningspliktig åtgärd får inte påbörjas innan byggnadsnämnden har gett startbesked, och de delar som omfattas får inte tas i bruk förrän det finns ett slutbesked, om nämnden inte beslutar annat. I en totalrenovering påverkar det tidplanen: inflyttningen i de ombyggda delarna ska planeras efter slutbeskedet. Gäller projektet även en tillbyggnad finns mer under " + _L.format("tillbyggnad-lidingo.html", "tillbyggnad på Lidingö") + ".",
     ],
     "aside": {"title": "Anmälan krävs bland annat för", "items": [
       "Rivning i byggnad över 50 m² byggnadsarea", "Bärande delar och brandskydd", "Eldstad, rökkanal och ventilation", "Vatten och avlopp"]}},
    {"id": "kulturmiljo-lidingo", "h2": "Vad staden redan vet om ditt hus",
     "paras": [
       "Enligt stadens frågor och svar om kulturmiljöprogrammet finns äldre byggnadsinventeringar för enskilda byggnader, dels från 1970- och 1980-talet, dels från 2013–2015. Kontaktar du kundcenter för miljö- och stadsbyggnadskontoret kan du be att få ta del av beskrivningar som finns för din fastighet. På Lidingö finns också nio byggnadsminnen, och för dem är det länsstyrelsen som beslutar om tillstånd till förändringar.",
       "Staden påpekar att en särskilt värdefull byggnad inte får förvanskas enligt plan- och bygglagen, även när ändringen inte kräver bygglov. Det är skäl nog att läsa inventeringen innan väggar rivs. Om husen och kulturmiljön i stort finns mer under " + _L.format("byggforetag-lidingo.html", "byggföretag på Lidingö") + ".",
     ],
     "aside": None},
    {"id": "inifran-lidingo", "h2": "Bygga om inifrån",
     "paras": [
       "När stommen får stå kvar går det ändå att förändra det mesta. Rotavdrag ges enligt Skatteverket för att riva väggar och bygga om planlösningen och för att tilläggsisolera, och för att montera fast köks- och badrumsinredning i samband med omfattande renovering. Kök och badrum beskriver vi närmare under " + _L.format("koksrenovering-lidingo.html", "köksrenovering på Lidingö") + " och " + _L.format("badrumsrenovering-lidingo.html", "badrumsrenovering på Lidingö") + ".",
       "Vi börjar med att öppna på några ställen och se hur bjälklag och väggar mår. Därefter bestämmer vi tillsammans med dig vad som byggs om och vad som får vara kvar, och lägger upp arbetet så att anmälan, startbesked och slutbesked passar in i tidplanen.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till på Lidingö",
  "steps": [
    ("Platsbesök", "Vi går igenom huset och bedömer hur mycket av stommen som kan stå kvar."),
    ("Underlag från staden", "Du begär ut eventuell byggnadsinventering, och vi läser den tillsammans."),
    ("Skriftligt kostnadsförslag", "Rivning, ombyggnad och installationer redovisas var för sig."),
    ("Anmälan och startbesked", "Det som kräver anmälan anmäls innan arbetet börjar."),
    ("Ombyggnad", "Stommen behålls, och rum, installationer och ytskikt byggs om – el och VVS via behöriga."),
    ("Slutbesked och genomgång", "De anmälda delarna tas i bruk efter slutbesked, och vi går igenom huset med dig."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering på Lidingö",
  "rot": [
    "För ombyggnad av ett småhus ska större delen av den ursprungliga stommen behållas och huset vara äldre än fem år. Inget avdrag ges för att riva huset, för bygglovshandlingar eller för att anlita arkitekt, kvalitetsansvarig eller besiktningsman.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Lidingö?",
  "price": [
    "Hur mycket av stommen som kan behållas, omfattningen av installationerna, kraven i en eventuell byggnadsinventering och vilken standard du väljer påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får man rotavdrag om man river villan och bygger nytt på samma grund?",
     "Nej. Skatteverket ger inget avdrag för att riva ett hus, även om ett nytt byggs upp på den gamla stommen. Vid ombyggnad ska större delen av stommen behållas."),
    ("Ger arkitektens ritningar rotavdrag?",
     "Nej, Skatteverket godkänner inte avdrag för att skriva bygglovshandlingar eller anlita arkitekt, kvalitetsansvarig eller besiktningsman."),
    ("När får vi flytta in i de ombyggda delarna?",
     "Lidingö stad skriver att delar som omfattas av ett startbesked inte får tas i bruk förrän byggnadsnämnden har gett slutbesked, om nämnden inte beslutar annat."),
    ("Hur tar jag reda på om mitt hus på Lidingö har inventerats?",
     "Kontakta kundcenter för miljö- och stadsbyggnadskontoret. Staden har inventeringar från 1970–80-talet och från 2013–2015, och där kan du be att få ta del av eventuella beskrivningar för din fastighet."),
    ("När måste en rivning anmälas på Lidingö?",
     "Rivning av en byggnad eller en del av en byggnad kräver anmälan om byggnaden har en byggnadsarea som är större än 50 kvadratmeter, enligt staden. Ändringar som väsentligt påverkar de bärande delarna ska också anmälas."),
  ],
  "sources": [_SKV_JOB, _SKV_ROT, _LID_VAD, _LID_KMP],
  "cta": ("Ska villan på Lidingö byggas om?", "Boka ett gratis platsbesök, så bedömer vi stommen och vad som kan behållas innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Ombyggd äldre villa med öppen planlösning, bevarade takbjälkar och stora fönster mot tallar",
     "renovated interior of an early 1900s Swedish wooden villa on Lidingö, original ceiling beams kept and painted white, new open plan between dining area and kitchen, wide pine floor, large windows facing pine trees and a glimpse of the sea, empty, soft daylight, no people, no text, no letters"),
    ("Villa under ombyggnad där ytterväggar och bjälklag står kvar men rummen är rivna",
     "interior of a Swedish villa under renovation where the outer walls, floor joists and roof structure are kept while interior walls have been removed, new timber studs marking a new room layout, daylight through existing windows, sawhorses and timber on the floor, no people, no text, no letters"),
  ],
  "related": [],
},

}
