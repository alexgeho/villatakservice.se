# -*- coding: utf-8 -*-
"""Fasadrenovering – ortsidor v3: Bromma, Nacka, Täby, Huddinge, Sollentuna, Lidingö (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade 2026-10-25: kommunernas bygglovssidor om
fasadändring (lydelse efter 1 december 2025), kulturmiljöprogram/-underlag (Stockholms stad: Varsam
utveckling av småhus- och villaområden; Nacka: Sommarnöjen vid farleden; Täby: Kulturmiljöer i Täby;
Huddinge: kulturmiljöprogram del 2; Lidingö: kulturmiljöprogram del 1 och områdesbeskrivningar för
Stureplatån, Hersby gärde och Hersby åker), Sollentunas översiktsplan, Boverket (PBL kunskapsbanken,
energiguiden, fuktrisker för ytterväggar), Arbetsmiljöverket (asbest) och Skatteverket (rotavdrag).
Inga priser, garantier, omdömen, egna uppdrag eller cert. Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_FASAD = ("Boverket – PBL kunskapsbanken: Bygglov för fasadändring",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_BV_ISOL = ("Boverket – Energiguiden: Tilläggsisolera fasaden",
            "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/tillaggsisolera-fasaden/")
_BV_FMAT = ("Boverket – Fuktrisker med fasadens material och ytskikt",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/")
_BV_ENST = ("Boverket – Risker med enstegstätning",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/risker-enstegstatning/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"fasadrenovering-bromma.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Bromma", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Bromma – lockpanel, puts och isolering",
  "description": "Fasadrenovering i Bromma: lockpanel i trädgårdsstäderna, slätputs i Södra Ängby och tilläggsisolering när fönstren sitter i liv. Gratis platsbesök.",
  "h1": "Fasadrenovering i Bromma",
  "lead": "I Brommas trädgårdsstäder och småstugeområden är det ofta detaljerna som avgör om en fasadrenovering blir lyckad: lockläktens dimension, putsens struktur och att fönstren får sitta kvar i liv med väggen. Geal Entreprenad AB renoverar fasader i hela Bromma och samordnar ställning, snickeri, puts, plåt och målning, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Trädgårdsstäder, småstugor och funkis i Bromma.",
  "sections": [
    {"id": "fasadtyper", "anchor": "Brommas fasader",
     "h2": "Stående lockpanel, slätputs och fönster i fasadliv",
     "paras": [
       "Stockholms stad beskriver i vägledningen Varsam utveckling av småhus- och villaområden hur trädgårdsstäderna växte fram. I bland annat Nockeby, Höglandet, Ålsten, Smedslätten och Ulvsunda blev 1920-talets klassiska formspråk rådande: enkla hus i ett och ett halvt plan, symmetriska fasader och branta sadeltak i rött tegel. Det vanligaste fasadmaterialet var stående träpanel med tunn lockläkt, men puts förekom också.",
       "Småstugorna i Norra Ängby och Olovslund är ännu enklare. Enligt vägledningen byggdes de uteslutande i trä, med stående lockpanel och fönster placerade i fasadliv. Södra Ängby skiljer sig från båda med sina kubiska funkisvillor, där fasaderna är brutet vita eller ljust grå i slätputs eller liggande träpanel.",
       "För en fasadrenovering ger det tre olika utgångslägen. På panelhusen handlar arbetet om brädor, läkt och anslutningar. På funkisvillorna är det putsen och underlaget som avgör. På småstugorna gäller det att väggen inte växer så mycket att fönstren hamnar i djupa nischer.",
     ],
     "aside": {"title": "Fasaderna i korthet", "items": [
       "Trädgårdsstad: stående panel med tunn lockläkt", "Småstugor: trä och fönster i fasadliv",
       "Södra Ängby: slätputs eller liggande panel", "Äldre tak: oftast rött tegel"]}},
    {"id": "panel-bromma", "h2": "Byta lockpanel utan att huset ändrar karaktär",
     "paras": [
       "Vägledningens råd för trädgårdsstäderna är att ta tillvara eller återskapa karaktärsskapande material, kulörer, byggnadsdelar och detaljer så långt det går. På en panelfasad sitter karaktären i proportionerna: brädornas bredd, den tunna lockläkten, knutbrädor, foder och vattbrädor. Byts panelen mot en grövre profil syns skillnaden från gatan, även om kulören är densamma.",
       "Boverket skriver att det inte är en fasadändring utan underhåll att byta fasadbeklädnaden mot samma material och utförande. Därför mäter vi upp befintlig panel och läkt innan något rivs och beställer virke som stämmer. Skadorna sitter oftast nederst mot sockeln och under fönsterbleck, och där räcker det ibland att byta de nedersta brädorna och skarva in nya.",
       "När panelen ändå är nere går det att se över vindskyddet bakom och kontrollera att luftspalten fungerar. Takfoten hör till samma helhet. Ska tegeltaket ses över medan ställningen står finns mer om det under " + _L.format("takrenovering-bromma.html", "takrenovering i Bromma") + ".",
     ],
     "aside": None},
    {"id": "isolering-bromma", "h2": "Tilläggsisolera ett hus med fönster i liv",
     "paras": [
       "Boverkets energiguide beskriver utvändig tilläggsisolering som ofta bäst för både energi och fukt, eftersom den befintliga väggen blir varmare och torrare. Samtidigt varnar myndigheten för att fönster och dörrar hamnar längre in, att takfoten inte skjuter ut lika mycket och att fasaden kan hänga ut över sockeln. Resultatet kallas ett överjäst uttryck.",
       "På en småstuga där fönstren sitter i liv med panelen blir effekten tydlig. Ska huset isoleras utvändigt behöver fönstren i regel flyttas ut och fodren göras om, och takfot och sockel kan behöva byggas på. Boverket nämner putsade funkishus där takfot, sockel och entréns skärmtak byggts på och fönster flyttats ut, så att det yttre utseendet blev oförvanskat. Det är ett relevant exempel för villorna i Södra Ängby.",
       "Invändig isolering lämnar fasaden orörd men gör väggens utsida kallare, och risken för röta och mögel ökar ju tjockare man isolerar. Ofta är det klokare att börja uppåt, se " + _L.format("vindsisolering.html", "vindsisolering") + ".",
     ],
     "aside": {"title": "Före tilläggsisolering", "items": [
       "Hur djupt hamnar fönstren?", "Räcker takfotens utsprång?",
       "Sticker väggen ut över sockeln?", "Finns fukt eller röta i väggen i dag?"]}},
    {"id": "lov-bromma", "h2": "Stadens lista över fasadändringar",
     "paras": [
       "På stadens bygglovssida räknas byte av material på fasad, nya eller ändrade fönster och tilläggsisolering upp som fasadändringar. För en- och tvåbostadshus krävs sedan 1 december 2025 normalt inget bygglov för dem, men utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla byggnader och områden och där detaljplanen har skyddsbestämmelser. Stadsmuseets klassificeringskarta ger en första indikation, men staden påpekar att alla byggnader och områden ännu inte är inventerade.",
       "Krävs lov vill staden se en fasadritning i skala 1:100 och en material- och kulörbeskrivning där kulörerna anges i NCS. Äldre ritningar på huset går att ta fram i e-tjänsten Bygg- och plantjänsten. De visar ofta panelens indelning och fönstrens placering som de var tänkta från början.",
       "Även en lovfri renovering ska uppfylla varsamhetskraven och i många fall följa detaljplanen. Ansvaret för det ligger på dig som byggherre, skriver staden, och därför går vi igenom klassning och plan innan något beställs.",
     ],
     "aside": {"title": "Räknas som fasadändring", "items": [
       "Byte av material på fasad eller tak", "Nya eller ändrade fönster och dörrar",
       "Tilläggsisolering", "Byte av kulör"]}},
  ],
  "steps_h2": "Så renoverar vi en fasad i Bromma",
  "steps": [
    ("Besök på plats", "Vi går runt huset, mäter panel och lockläkt, letar röta nederst och knackar på putsen där den låter ihålig."),
    ("Klassning och plan", "Stadsmuseets karta och detaljplanen kontrolleras, så att vi vet om materialbyte eller isolering kräver lov."),
    ("Kostnadsförslag i delar", "Lagning, byte, isolering och målning prissätts var för sig i ett skriftligt förslag."),
    ("Ställning och rivning", "Ställningen anpassas efter tomtens häckar och träd, och skadat material tas ner."),
    ("Ny panel eller puts", "Virke med samma profil, eller bruk som passar underlaget, kommer upp, och fönsteranslutningar och bleck görs om."),
    ("Färg och slutkontroll", "Fasaden ytbehandlas och vi går igenom resultatet tillsammans på plats."),
  ],
  "rot_h2": "ROT-avdrag för fasadrenovering i Bromma",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att byta och reparera fasader, tilläggsisolera och måla fasader, och även att montera och ta ner byggnadsställningar i samband med arbetet. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag.",
    "Är ni två som äger villan har ni var sitt avdragsutrymme. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden i Bromma",
  "price": [
    "Hur stor del av panelen som måste bytas, om lockläkt och foder behöver tillverkas i en äldre dimension, om putsen kan lagas eller ska göras om och om väggen ska isoleras, med allt det innebär för fönster, sockel och takfot. Ställning och skydd av trädgården räknas också in. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan lockpanelen på vår 1920-talsvilla i Nockeby bytas utan lov?",
     "Byts panelen mot samma material och utförande räknas det som underhåll. Ligger huset i ett område med utökad lovplikt kan en annan profil eller ett annat material kräva bygglov, så kontrollera Stadsmuseets karta och detaljplanen först."),
    ("Går det att tilläggsisolera en småstuga i Norra Ängby utvändigt?",
     "Det går, men fönstren sitter i fasadliv och hamnar annars djupt in i väggen. Räkna med att flytta ut fönstren och se över takfot och sockel, och kontrollera först om huset omfattas av utökad lovplikt."),
    ("Hur lagas slätputsen på en funkisvilla i Södra Ängby?",
     "Lösa partier knackas ner och lagas med ett bruk som passar det befintliga underlaget, så att strukturen blir lika. Därefter avfärgas hela ytan så att lagningarna inte syns."),
    ("Var hittar jag de gamla fasadritningarna till mitt hus i Bromma?",
     "Stadsbyggnadskontorets äldre handlingar kan sökas fram och skrivas ut i e-tjänsten Bygg- och plantjänsten. De visar ofta fönstrens placering och panelens indelning."),
    ("Vilka handlingar vill staden ha om fasadrenoveringen i Bromma kräver lov?",
     "Bland annat en fasadritning i skala 1:100 där material och kulörer anges, eller en separat material- och kulörbeskrivning med NCS-koder, samt en situationsplan."),
  ],
  "sources": [
    ("Stockholms stad – Fasadändring (bygglov.stockholm)",
     "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/"),
    _VARSAM, _BV_FASAD, _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på Brommavillan ses över?", "Boka ett gratis platsbesök så går vi igenom panel, puts och fönster tillsammans."),
  "img": [
    ("Trävilla med stående lockpanel och rött tegeltak i en trädgårdsstad i Bromma",
     "1920s Swedish one-and-a-half storey wooden villa with vertical board-and-batten panelling painted pale green, steep red clay tile roof with a small centred dormer, white window frames set flush with the facade, hedge and fruit trees, garden city suburb Bromma Stockholm, soft summer daylight, no people, no text"),
    ("Nya panelbrädor och nytt fönsterbleck nederst på en trävilla",
     "close-up of the lower part of a Swedish wooden house facade where new vertical board-and-batten boards have been fitted above a grey concrete plinth, freshly primed, new metal window sill flashing above, autumn daylight, no people, no text"),
  ],
  "related": [
    ("malare-bromma.html", "Målare i Bromma", "Fasad- och fönstermålning."),
  ],
},

# ------------------------------------------------------------------ NACKA
"fasadrenovering-nacka.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Nacka", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Nacka – sommarvillor, socklar och stugor",
  "description": "Fasadrenovering i Nacka: panel och stensocklar på sommarvillorna vid farleden, kommunens kulturmiljökarta och isolering när stugan blir helårshus.",
  "h1": "Fasadrenovering i Nacka",
  "lead": "Vid farleden i Boo står sommarvillor från 1800-talets slut med ljus panel, höga stensocklar och långa taksprång, och i skogen bakom dem stugor som numera bebos året runt. Geal Entreprenad AB renoverar fasader i hela Nacka – lagar eller byter panel, putsar om och tilläggsisolerar – och börjar med ett gratis platsbesök och ett skriftligt kostnadsförslag.",
  "card": "Sommarvillor, stugor och villor i Nacka.",
  "sections": [
    {"id": "farleden", "anchor": "Sommarvillorna",
     "h2": "Panel, stensockel och taksprång – det som ska bevaras",
     "paras": [
       "Kommunens kulturmiljöprogram för sommarnöjena vid farleden återkommer till samma förhållningssätt område för område: befintliga hus ska respekteras i proportioner, fasadfärg och tak och i detaljer som fönster, panel, utsmyckningar, entréer och räcken. Ljusmålad panel dominerar på de äldre sommarvillorna, och programmet pekar ut rejäla stensocklar, resliga fönster och utskjutande taksprång som bevarandevärda karaktärsdrag.",
       "Variationen är ändå stor. Sjövillan vid Fredriksro på Knarrnäs, en cottagevilla från 1870-talets slut, har en tegelsockel som programmet beskriver som lite speciell. Grävlingsbergsvillorna från 1890-talets slut har inslag av puts, och för Grävlingsberg–Dalen finns skydds- och varsamhetsbestämmelser i detaljplanen. Tegelön ligger dessutom inom riksintresset för kulturmiljövården Stockholms farled.",
       "För en fasadrenovering är det sockeln, panelen och fönstren som bär husets uttryck. En lagning ska därför följa det som finns: samma panelprofil, samma typ av sockel och fönster som sitter kvar där de satt.",
     ],
     "aside": {"title": "Karaktärsdrag på sommarvillorna", "items": [
       "Ljusmålad panel", "Rejäla stensocklar", "Resliga fönster", "Utskjutande taksprång"]}},
    {"id": "sockel", "h2": "Sockeln och nederkanten tar mest stryk",
     "paras": [
       "En hög stensockel håller trästommen borta från markfukten, men övergången mellan sten och panel är en av fasadens känsligaste punkter. Där samlas vatten som rinner längs väggen, och regnstänk från marken når de nedersta brädorna. Boverket påpekar att fuktskador kan uppstå när fasadens ytskikt fuktas upp och inte hinner torka ut tillräckligt fort.",
       "Vi börjar därför nedifrån. Vi kontrollerar att sockelns överkant leder bort vatten, att det finns ett avstånd mellan sockel och panel och att de nedersta brädorna går att byta utan att resten av väggen rubbas. Lösa fogar i en murad sockel lagas med ett bruk som passar stenen, och skadade partier i en tegelsockel byts sten för sten.",
       "Där panelen möter fönstren gäller samma sak. Fönsterbleck och droppkanter ska leda vattnet ut från väggen, och på resliga fönster med smala foder blir en ny bleckprofil lätt för grov. Ska fönstren renoveras samtidigt finns mer under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
    {"id": "stugor", "h2": "När sportstugan blir helårshus",
     "paras": [
       "Programmet beskriver också de enklare stugorna, till exempel uthyrningsstugorna vid Visborgs minne. Där ska fasadmaterial och konstruktion vara av enkelt slag, nuvarande materialtyper användas vid underhåll och fönstren sitta i liv med ytterväggen. På stugorna förekommer stående panel och på de äldre oftast locklistpanel, med foder och vindskivor i nätta dimensioner.",
       "Många stugor i Boo används i dag året runt, och då väcks frågan om väggarna ska isoleras. Boverket skriver att utvändig tilläggsisolering ofta är bäst för energin och fukten, men att fönster och dörrar då hamnar längre in och takfoten skjuter ut mindre. På ett hus med tunna väggar, fönster i liv och små takutsprång syns det tydligt. Resultatet blir oftast bättre om isoleringen görs när panelen ändå ska bytas, så att fönster, foder och takfot kan anpassas i samma arbete.",
       "Invändig isolering lämnar fasaden orörd men gör väggens utsida kallare och ökar risken för fuktskador. Det kan behövas ett ångtätande skikt, och Boverket råder den som är osäker att ta hjälp av en fuktexpert.",
     ],
     "aside": {"title": "Inför isolering av en stuga", "items": [
       "Hur tunn är väggen i dag?", "Sitter fönstren i liv?",
       "Hur stort är takutsprånget?", "Behövs ett ångtätande skikt?"]}},
    {"id": "lov-nacka", "h2": "Lila och orange i kommunens karta",
     "paras": [
       "Nacka kommun räknar upp byte av färg eller material på fasad, nya fönster och tilläggsisolering som exempel på fasadändringar. Inom detaljplan krävs inte längre bygglov för dem på en- eller tvåbostadshus, men åtgärden får inte strida mot planen, och ett ingrepp i den bärande konstruktionen kräver en anmälan.",
       "Ligger fastigheten i ett område som enligt 8 kap. 13 § PBL är särskilt värdefullt utökas lovplikten. Då krävs bygglov för alla fasadändringar som påverkar områdets karaktär eller byggnadens yttre karaktärsdrag. I kommunens webbkarta visar lila markering byggnader och områden med särskilt höga kulturvärden. Orange betyder att en bedömning kan pågå, och då är rådet att kontakta stadsbyggnadsservice.",
       "Att byta en ljusmålad panel mot puts, eller att isolera så att taksprånget krymper, är just den sortens ändring som prövas i de lila områdena. Ett byte mot samma material och utförande räknas enligt Boverket som underhåll. Vid bedömningen av vad som är en byggnads karaktärsdrag nämner Boverket bland annat form, färgsättning, storlek, utvändiga material, ålder och proportioner – och på en sommarvilla vid farleden hänger alla ihop med fasaden.",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången vid en fasadrenovering i Nacka",
  "steps": [
    ("Inventering", "Vi går igenom sockel, panel, fönster och taksprång och öppnar på ställen där vi misstänker fukt."),
    ("Karta och detaljplan", "Kulturmiljökartan och planbestämmelserna stäms av, så att du vet om ändringen kräver lov."),
    ("Förslag i skrift", "Du får ett skriftligt kostnadsförslag där sockellagning, panelbyte och eventuell isolering står var för sig."),
    ("Ställning i terrängen", "På branta tomter planeras ställningen efter berg och murar, och terrasseringar skyddas."),
    ("Sockel, panel och bleck", "Sockeln lagas, skadad panel byts mot samma profil och fönsterbleck anpassas till fodren."),
    ("Målning och avslut", "Fasaden målas och vi går igenom arbetet tillsammans innan ställningen tas ner."),
  ],
  "rot_h2": "Rotavdrag för fasadarbete i Nacka",
  "rot": [
    "För ett småhus godkänner Skatteverket rotavdrag för att byta och reparera fasader, mura och reparera fasader, tilläggsisolera och måla fasader. Det är bara arbetskostnaden som ger avdrag: 30 procent av den, med högst 50 000 kr per person och år och 75 000 kr som tak för rot och rut sammanlagt.",
    "Bortforsling av gammalt material ger inget avdrag. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Nacka?",
  "price": [
    "Sockelns skick, hur många panelbrädor som behöver bytas, om fönsterfoder och bleck ska tillverkas efter förlaga och om väggarna ska isoleras. Branta tomter och hus nära vattnet kan kräva mer ställning och skydd. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi byta den ljusa panelen mot puts på en sommarvilla i Boo?",
     "Ligger huset i ett område med lila markering krävs bygglov, och kulturmiljöprogrammet räknar panelen till det som ska respekteras. Utanför de värdefulla områdena är materialbytet lovfritt, men varsamhetskravet gäller."),
    ("Hur lagas en sprucken stensockel under träfasaden?",
     "Lösa fogar kratsas ur och fogas om med ett bruk som passar stenen, och vi ser till att sockelns överkant leder bort vatten från panelen."),
    ("Kan en stuga med fönster i liv isoleras utan att den ser ombyggd ut?",
     "Ja, om fönster, foder och takfot anpassas samtidigt. Boverket beskriver hur fönster flyttas ut och takfot byggs på för att proportionerna ska behållas."),
    ("Vad betyder orange markering i Nackas kulturmiljökarta?",
     "Att det kan pågå en bedömning av kulturvärdena. Kommunen ber dig då kontakta stadsbyggnadsservice innan du planerar fasadändringar."),
    ("Behövs en anmälan om skadade reglar i ytterväggen byts i Nacka?",
     "Innebär arbetet ingrepp i den bärande konstruktionen kräver Nacka kommun en anmälan, även när själva fasadändringen är lovfri."),
  ],
  "sources": [
    ("Nacka kommun – Fasadändringar",
     "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/lovfria-atgarder/fasadandringar/"),
    ("Nacka kommun – Kulturmiljöprogram: Sommarnöjen vid farleden (pdf)",
     "https://www.nacka.se/499628/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-sommarnojen.pdf"),
    _BV_FASAD, _BV_ISOL, _BV_FMAT, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver fasaden på huset i Nacka ses över?", "Boka ett gratis platsbesök så går vi igenom sockel, panel och fönster på plats."),
  "img": [
    ("Ljusmålad sommarvilla med hög stensockel och långa taksprång vid farleden i Boo",
     "late 1800s Swedish summer villa with light cream painted wooden panel facade, carved decorative details, tall narrow windows, high natural stone plinth, long overhanging eaves, red sheet metal roof, pine trees and rocky slope above the Baltic fairway, Boo Nacka, summer daylight, no people, no text"),
    ("Omfogad stensockel under en ljusmålad träpanel",
     "close-up of a granite stone plinth with repointed mortar joints under the bottom boards of a light painted wooden facade on an old Swedish summer villa, small gap between plinth and boards, daylight, no people, no text"),
  ],
  "related": [
    ("malare-nacka.html", "Målare i Nacka", "Fasad- och fönstermålning."),
    ("snickare-nacka.html", "Snickare i Nacka", "Verandor, panel och foder."),
  ],
},

# ------------------------------------------------------------------ TÄBY
"fasadrenovering-taby.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Täby", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Täby – tegel, träpanel och plåtfasader",
  "description": "Fasadrenovering i Täby: tegelvillor vid Hjortvägen, kedjehus med tegel och panel i kvarteret Hägern och tilläggsisolering enligt kommunens råd.",
  "h1": "Fasadrenovering i Täby",
  "lead": "Många Täbyhus från efterkrigstiden har flera fasadmaterial på samma vägg: tegel i bottenvåningen, målad panel i gaveln och en putsad sockel under. Geal Entreprenad AB renoverar fasader i hela Täby, från tegelvillor till kedjehus, och samordnar murning, snickeri, plåt och målning. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  "card": "Tegelvillor, kedjehus och grupphus i Täby.",
  "sections": [
    {"id": "material-taby", "anchor": "Täbys fasader",
     "h2": "Tegel nedtill, trä upptill",
     "paras": [
       "Kommunens kulturmiljöunderlag Kulturmiljöer i Täby visar hur blandade fasaderna är. Vid östra delen av Hjortvägen står villor från 1950- och 1960-talet i en eller två våningar, med fasader av rött eller gult tegel och grå putsad sockel. Underlaget beskriver en hög andel bevarade ursprungliga material och detaljer, och rådet för området är att behålla tegelfasader, fönstersnickerier, entrépartier och nätta takutsprång.",
       "Kvarteret Hägern i Näsbygård byggdes 1975–1976 som kedjehus med bottenvåning i fasadtegel, småspröjsade fönster med brunsvarta snickerier och gavlar i brun-, röd- eller grönmålad träpanel. Underlaget visar också två hus från 1968 där bottenvåningen har tegel men träpanel under fönstren.",
       "I Norskogen, med elementhus från 1958–1959, sitter fönstren i stället i liv med en fasad av finprofilerad aluminiumplåt. Tre material som åldras på var sitt sätt, och som därför renoveras på var sitt sätt.",
     ],
     "aside": {"title": "Fasader i kommunens underlag", "items": [
       "Hjortvägen: rött eller gult tegel, grå putssockel", "Hägern: tegel i bottenvåning, panel i gavel",
       "Hus från 1968: tegel med panel under fönstren", "Norskogen: aluminiumplåt med fönster i liv"]}},
    {"id": "tegel-panel", "h2": "Där tegel möter panel",
     "paras": [
       "Ett murat tegelskikt håller länge, men fogarna och anslutningarna åldras fortare. Boverket skriver att anslutningar mot fönster och dörrar och infästningar för till exempel stuprör behöver tätning i mer än en nivå, så kallad tvåstegstätning, när de utsätts för slagregn. På Täbys blandfasader finns sådana anslutningar överallt: där panelen börjar ovanför teglet, under fönsterbänkarna och kring bleck.",
       "Det är också där skadorna brukar sitta. Panel som slutar för nära tegelkrönet suger vatten i ändträet, och ett fönsterbleck med för liten lutning leder vatten in mot fogen i stället för ut. Vi byter de skadade brädorna mot samma profil, ser över bleck och droppkanter och lagar fogarna i teglet med ett bruk som passar stenen.",
       "Teglet i sig ska sällan målas eller putsas över. Underlaget räknar tegelfasaderna vid Hjortvägen till det som ska behållas, och för grupphusområdena gäller att undvika stora kontraster i material och färg. Panelen och snickerierna runt omkring målas, och mer om det finns hos " + _L.format("malare-taby.html", "målare i Täby") + ".",
     ],
     "aside": None},
    {"id": "isolering-taby", "h2": "Tilläggsisolera enligt kommunens råd",
     "paras": [
       "I de generella råden för småhusområden skriver kommunen att fönstren vid tilläggsisolering av fasad bör flyttas ut, så att de sitter i samma förhållande till fasaden som tidigare, och att takfoten kanske också behöver förlängas. Boverket beskriver samma problem: en tjockare vägg gör att fönstren hamnar längre in och takfoten skjuter ut mindre.",
       "På ett hus med tegel nedtill är det sällan aktuellt att isolera utanpå teglet. Den panelade gaveln eller panelpartiet under fönstren kan däremot få tjockare isolering när panelen ändå byts, och enligt Boverket är det då tilläggsisoleringen brukar bli mest lönsam. Isoleras väggen invändigt i stället blir teglet kallare, och då ökar risken för frostsprängning. Fönstren behöver inte heller bytas för att huset ska bli varmare: kommunens råd är att äldre fönster av hög kvalitet ofta är värda att underhålla och eventuellt kan kompletteras med invändigt energiglas.",
       "Underlaget visar också hur stor förändringen kan bli. Punkthusen i kvarteret Höstfibblan hade ursprungligen putsade fasader men är i dag tilläggsisolerade och klädda med ljust gul plåt. På en villa i ett enhetligt grupphusområde syns en motsvarande skillnad tydligt mot grannarna. Läs mer om puts, panel och isolering under " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": {"title": "Råd vid tilläggsisolering", "items": [
       "Flytta ut fönstren", "Förläng takfoten vid behov",
       "Isolera när panelen ändå byts", "Arbeta i torrt väder"]}},
    {"id": "lov-taby", "h2": "Lovfritt i Täby – utom i de värdefulla miljöerna",
     "paras": [
       "Täby kommun skriver att det inte behövs bygglov för fasadändringar på en- och tvåbostadshus, om byggnaden inte är särskilt värdefull, inte ligger i ett särskilt värdefullt område och inte har utökad lovplikt i detaljplanen. Den som är osäker på vad som gäller för sin fastighet kan få rådgivning av kommunen.",
       "Även utan lov är kulturmiljöunderlagets riktlinjer värda att följa. För grupphusområdena säger de att ursprunglig färgsättning och ursprungliga fönsterformat ska behållas och att bebyggelsens arkitektoniska uttryck ska vara vägledande vid om- och tillbyggnader. Kommunen råder dessutom fastighetsägare att ta fram husets ritningar och fråga efter äldre handlingar, eftersom många hus har byggts till genom åren.",
     ],
     "aside": None},
  ],
  "steps_h2": "Från platsbesök till färdig fasad i Täby",
  "steps": [
    ("Genomgång av fasaden", "Tegel, fogar, panel, sockel och bleck kontrolleras var för sig, och vi petar i ändträ och nedre brädor."),
    ("Ritningar och riktlinjer", "Vi tittar på husets ritningar och på vad kulturmiljöunderlaget säger om området innan material väljs."),
    ("Kostnadsförslag", "Ett skriftligt förslag där murning, panelbyte, isolering och målning redovisas som separata poster."),
    ("Förberedelser", "Ställning byggs, tegel och fönster täcks och skadad panel rivs."),
    ("Utförande", "Fogar lagas, ny isolering och panel monteras och bleck görs om med tvåstegstätning vid anslutningarna."),
    ("Ytbehandling och genomgång", "Panel och snickerier målas och vi kontrollerar anslutningarna tillsammans med dig."),
  ],
  "rot_h2": "ROT vid fasadrenovering i Täby",
  "rot": [
    "Skatteverkets lista över godkända arbeten i småhus tar med att mura och reparera fasader, byta och reparera fasader, tilläggsisolera och måla fasader. Du får 30 procent av arbetskostnaden i avdrag, högst 50 000 kr per person och år, och rot och rut får tillsammans uppgå till högst 75 000 kr.",
    "Bor du i ett radhus som är en bostadsrätt ger fasadarbeten inget rotavdrag, eftersom fasaden räknas som en gemensam yta. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Faktorer som påverkar kostnaden",
  "price": [
    "Hur mycket av fogarna i teglet som behöver lagas, hur stor andel av panelen som byts, om fönstren ska flyttas ut vid tilläggsisolering och hur många bleck och anslutningar som måste göras om. Ett tvåplanshus behöver mer ställning än en envåningsvilla. Du får ett skriftligt kostnadsförslag efter ett platsbesök som inte kostar något.",
  ],
  "faq": [
    ("Ska teglet på vår 60-talsvilla i Täby målas när fasaden renoveras?",
     "Normalt inte. Kommunens underlag räknar tegelfasaderna till det som ska behållas, bland annat vid Hjortvägen. Vi lagar fogarna och målar panel och snickerier runt omkring."),
    ("Kan gaveln på ett kedjehus i kvarteret Hägern tilläggsisoleras?",
     "Gaveln i träpanel går att isolera när panelen byts, men fönster och takfot behöver anpassas. I ett enhetligt kedjehusområde är det klokt att stämma av med grannarna och kommunen först."),
    ("Hur renoveras en plåtfasad på ett elementhus i Norskogen?",
     "Vi börjar med infästningar, skarvar och anslutningarna mot fönstren, som sitter i liv med plåten. Byts plåten mot ett annat material ändras husets karaktär, så kontrollera först vad som gäller för området."),
    ("Behöver vi lov för att flytta ut fönstren vid tilläggsisolering i Täby?",
     "Inte på ett en- eller tvåbostadshus som varken är särskilt värdefullt, ligger i ett särskilt värdefullt område eller har utökad lovplikt i detaljplanen. Varsamhetskravet gäller ändå, och kommunen erbjuder rådgivning."),
    ("Varför ruttnar panelen närmast teglet på vårt Täbyhus?",
     "Där panelen slutar ovanför tegelkrönet når regnstänk och smältvatten ändträet. Ett bleck med droppkant och ett litet avstånd mellan tegel och bräda gör att virket hinner torka."),
  ],
  "sources": [
    ("Täby kommun – Fasadändring",
     "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/fasadandring"),
    ("Täby kommun – Kulturmiljöer i Täby (pdf)",
     "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"),
    ("Täby kommun – Råd och riktlinjer för grupphusområden",
     "https://taby.se/huvudsajter/kulturmiljoer/rad-och-riktlinjer/grupphusomraden"),
    _BV_FMAT, _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Är det dags att se över fasaden i Täby?", "Boka ett gratis platsbesök så bedömer vi tegel, panel och anslutningar."),
  "img": [
    ("Tegelvilla från 1960-talet med mörk träpanel i gaveln i Täby",
     "1960s Swedish suburban villa with red brick lower floor and dark brown painted vertical wooden panel on the upper gable, black concrete roof tiles, small-paned windows with dark frames, neat lawn and low hedge, Täby north of Stockholm, overcast daylight, no people, no text"),
    ("Anslutning mellan tegel och träpanel under ett fönster",
     "close-up of the junction between a red brick wall and painted wooden panel boards under a window with a new metal sill flashing with drip edge, Swedish 1970s chain house, daylight, no people, no text"),
  ],
  "related": [
    ("malare-taby.html", "Målare i Täby", "Panel, snickerier och fönster."),
    ("snickare-taby.html", "Snickare i Täby", "Fönster, verandor och carport."),
  ],
},

# ------------------------------------------------------------------ HUDDINGE
"fasadrenovering-huddinge.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Huddinge", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Huddinge – eternit, fjällpanel och lov",
  "description": "Fasadrenovering i Huddinge: asbestcementplattor på äldre villor, fjällpanel på fritidshusen och vad kommunen säger om byte av fasadmaterial.",
  "h1": "Fasadrenovering i Huddinge",
  "lead": "Har villan i Huddinge fasadskivor av cementfiber från 1940- eller 50-talet är första frågan inte vilken panel som ska upp, utan vad skivorna innehåller. Geal Entreprenad AB renoverar fasader i hela kommunen och samordnar provtagning, ställning, snickeri, plåt och målning, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villor, grupphus och fritidshus i Huddinge.",
  "sections": [
    {"id": "asbest", "anchor": "Asbestcementplattor",
     "h2": "Fasadplattor som kan innehålla asbest",
     "paras": [
       "Boverket beskriver hur många fasader under 1940- och 1950-talen kläddes med cementfiberplattor som innehöll asbestfibrer. Plattorna är nästan underhållsfria och behöver bara tvättas emellanåt så länge de inte skadas. De förbjöds på 1970-talet, sedan det konstaterats att asbestfibrer kan orsaka cancer, och fibrerna kan frigöras när plattorna bearbetas, till exempel om man borrar i dem.",
       "Arbetsmiljöverket råder att utgå från att alla byggnader som uppförts fram till 1982, då asbest förbjöds i Sverige, kan innehålla asbest. Även senare hus kan i vissa fall ha det, eftersom produkter fanns kvar i lager eller importerades. Bland Huddinges villor och grupphus från folkhemsåren och rekordåren finns alltså många där en fasadrenovering bör börja med ett materialprov.",
       "Proverna ska skickas till ett laboratorium som har tillstånd att hantera asbesthaltigt material. Att undersöka och ta prover kräver inget tillstånd från Arbetsmiljöverket, men det gör själva rivningen. Hittar man under arbetet dolda material som inte har analyserats, till exempel äldre skivor bakom en senare panel, ska prover tas och rivningen avbrytas tills svaret har kommit.",
     ],
     "aside": {"title": "Var uppmärksam på", "items": [
       "Fasadskivor av cementfiber", "Hus byggda före 1982",
       "Skadade eller genomborrade skivor", "Okänt material bakom nyare panel"]}},
    {"id": "rivning", "h2": "Rivning med tillstånd – sedan en ny fasad",
     "paras": [
       "Enligt Arbetsmiljöverket krävs tillstånd för att ett företag ska få riva eller sanera material som innehåller asbest, inomhus som utomhus, och rivning av asbesthaltigt material på tak eller fasad nämns uttryckligen. Ansökan ska lämnas åtta veckor innan arbetet ska börja, och de som leder och deltar i rivningen ska ha gått en utbildning som är specifik för rivning och sanering av asbest.",
       "Förarbete, omhändertagande av avfallet och städning efteråt räknas också som rivning och sanering, och asbesthaltigt avfall ska till asbestdeponi. Området där rivningen pågår ska vara avspärrat och skyltat. Vi planerar därför fasadrenoveringen i två steg: först tas plattorna ner av ett företag som har tillstånd, sedan bygger vi upp den nya fasaden med vindskydd, läkt och beklädnad.",
       "I Stockholms stads vägledning för småhusområden konstateras att det numera finns fasadskivor utan asbest, vilket gör det möjligt att behålla uttrycket på hus där skivorna är en del av arkitekturen. Alternativet är träpanel, och det valet hänger ihop med lovfrågan längre ned.",
     ],
     "aside": None},
    {"id": "fritidshus", "h2": "Fjällpanel på fritidshusen från 1950–80-talen",
     "paras": [
       "Kommunens kulturmiljöprogram beskriver fritidshusområden från 1950–80-talen där stugorna är monteringsfärdiga hus i ett plan med liggande fjällpanel och sadeltak. Rådet för dessa områden är att fasadmaterial, volym och takvinkel bör värnas. För sportstugeområdena i stort skriver programmet att fasadmaterialet bör vara trä, som är tidstypiskt för sådana områden.",
       "Programmet berättar också att en del ägare tilläggsisolerade och byggde om sina stugor när fritidsområdena permanentades. Byts fjällpanelen i samband med en sådan isolering är det värt att behålla den liggande profilen, så att stugan fortsätter att höra ihop med grannhusen.",
       "Boverket skriver att man ska undersöka om fasadens konstruktion har fuktskador innan man tilläggsisolerar, och åtgärda orsaken till mögel eller röta först. I ett äldre fritidshus med enkel stomme är det ofta väggens nederkant och partierna runt fönstren som visar hur det står till. Mer om att isolera uppåt finns under " + _L.format("vindsisolering.html", "vindsisolering") + ".",
     ],
     "aside": {"title": "Programmets råd", "items": [
       "Värna fasadmaterial, volym och takvinkel", "Trä som fasadmaterial i stugområden",
       "Små volymer och läsbara tillägg", "Undvik att fälla träd"]}},
    {"id": "lov-huddinge", "h2": "Byte av fasadmaterial och Huddinges webbkarta",
     "paras": [
       "Huddinge kommun skriver att du inte behöver bygglov för att renovera fasaden när du byter befintligt material mot samma sorts material med samma färg. Att ändra utseendet på ett en- eller tvåbostadshus är också lovfritt, så länge byggnaden eller området inte är kulturhistoriskt värdefullt och detaljplanen inte kräver lov. I värdefulla miljöer krävs bygglov, och kommunens webbkarta visar om byggnaden ligger inom ett kulturmiljöområde.",
       "Ett byte från cementfiberskivor till träpanel är alltså ett materialbyte som kan kräva lov i ett kulturmiljöområde. Är du osäker kan du söka frivilligt bygglov och få ett skriftligt besked; kommunen handlägger det som en vanlig ansökan och tar ut en avgift. Påverkas byggnadens bärande delar väsentligt krävs dessutom en anmälan och ett startbesked.",
       "Kommunen påminner också om att en ändring som inte kräver lov ändå ska vara anpassad till hur området ser ut och till byggnadens speciella karaktär, till exempel husets ålder. På en villa från 1950-talet kan det tala för en ny beklädnad som liknar den gamla i format och kulör.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går fasadrenoveringen till i Huddinge",
  "steps": [
    ("Besiktning av fasaden", "Vi går igenom beklädnad, sockel och fönsteranslutningar och noterar material som behöver provas."),
    ("Materialprov", "Misstänkta skivor provas och analyseras innan något bearbetas."),
    ("Lov och karta", "Ska fasadmaterialet bytas stämmer vi av kommunens webbkarta och detaljplanen."),
    ("Skriftligt kostnadsförslag", "Sanering, ny beklädnad, isolering och målning står som egna poster."),
    ("Sanering och uppbyggnad", "Asbesthaltigt material rivs av ett företag med tillstånd, därefter monteras vindskydd, läkt och ny fasad."),
    ("Målning och kontroll", "Fasaden ytbehandlas, bleck och detaljer kompletteras och vi går igenom resultatet."),
  ],
  "rot_h2": "ROT-avdrag i Huddinge",
  "rot": [
    "Att sanera asbest i samband med byggarbete, byta och reparera fasader och tilläggsisolera räknas som rotarbete i ett småhus. Att mäta asbest ger däremot inget avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och högst 75 000 kr när rot och rut läggs ihop.",
    "Material ingår inte i underlaget för avdraget. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Huddinge?",
  "price": [
    "Om fasaden innehåller asbest och hur stor yta som ska saneras, vilket material den nya fasaden ska ha, om väggen ska tilläggsisoleras och hur fönster och sockel påverkas. Husets höjd och tomtens lutning styr hur mycket ställning som behövs. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi skruva upp ny panel direkt på eternitskivorna på vår villa i Huddinge?",
     "Att borra i asbestcement kan frigöra fibrer, och Boverket nämner just borrning som exempel. Låt prova skivorna först och planera arbetet utifrån svaret."),
    ("Hur vet vi om fasadskivorna på 50-talshuset innehåller asbest?",
     "Genom ett materialprov som analyseras av ett laboratorium med tillstånd för asbesthaltigt material. Arbetsmiljöverket råder att utgå från att hus byggda fram till 1982 kan innehålla asbest."),
    ("Krävs bygglov för att byta eternit mot träpanel i Huddinge?",
     "Inte för ett en- eller tvåbostadshus utanför kulturhistoriskt värdefulla miljöer, om detaljplanen inte kräver det. Kontrollera kommunens webbkarta; i värdefulla områden krävs lov."),
    ("Ger asbestsaneringen av fasaden rotavdrag?",
     "Ja, Skatteverket godkänner sanering av asbest i samband med byggarbete i småhus. Att mäta asbest ger däremot inget avdrag."),
    ("Kan fjällpanelen på vårt fritidshus från 1970-talet bytas mot stående panel?",
     "Det går, men kulturmiljöprogrammet råder att fasadmaterialet värnas i fritidshusområdena. Ligger stugan i ett utpekat kulturmiljöområde kan bytet kräva lov."),
  ],
  "sources": [
    ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest",
     "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/"),
    ("Arbetsmiljöverket – Förebygg riskerna med asbest",
     "https://www.av.se/halsa-och-sakerhet/kemiska-risker/risker-for-vissa-amnen-produkter-och-verksamheter/asbest/forebygg-riskerna-med-asbest/"),
    _BV_FMAT,
    ("Huddinge kommun – Fasadändring",
     "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/fasadandring"),
    ("Huddinge kommun – Kulturmiljöprogram del 2 (pdf)",
     "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf"),
    _VARSAM, _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Funderar du på att byta fasad i Huddinge?", "Boka ett gratis platsbesök så går vi igenom material, prov och lovfrågor."),
  "img": [
    ("Villa från 1950-talet med grå fasadskivor och sadeltak i Huddinge",
     "1950s Swedish one-storey suburban villa clad with grey fibre cement facade boards, white window frames, gable roof with dark concrete tiles, small garden with low hedge and birch trees, Huddinge south of Stockholm, overcast daylight, no people, no text"),
    ("Väderbitna fasadskivor av cementfiber runt ett fönster",
     "close-up of weathered grey fibre cement facade boards around a white wooden window on a 1950s Swedish house, visible fixings and joints, daylight, no people, no text"),
  ],
  "related": [
    ("malare-huddinge.html", "Målare i Huddinge", "Fasader, fönster och invändig målning."),
  ],
},

# ------------------------------------------------------------------ SOLLENTUNA
"fasadrenovering-sollentuna.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Sollentuna", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Sollentuna – renovera, isolera, återbruka",
  "description": "Fasadrenovering i Sollentuna: renovera i stället för att riva, tilläggsisolera när panelen byts och puts på trästomme. Lov enligt kommunens kartlager.",
  "h1": "Fasadrenovering i Sollentuna",
  "lead": "Sollentunas översiktsplan säger att funktionella bostadshus i regel inte ska rivas för att ge plats åt nya, och att byggnader och material ska återanvändas. För en villa eller ett radhus med sliten fasad är det ett skäl att renovera det som finns. Geal Entreprenad AB byter panel, lagar puts och tilläggsisolerar i hela kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villor och radhus i Sollentuna.",
  "sections": [
    {"id": "renovera", "anchor": "Renovera eller riva",
     "h2": "Kommunen vill att husen renoveras",
     "paras": [
       "I översiktsplanen med sikte på 2040 skriver Sollentuna att kommunen, för att leva upp till sin miljö- och klimatpolicy, i regel inte bör medge förtätningar som förutsätter att funktionella bostadshus rivs. Bebyggelsens klimatpåverkan ska begränsas genom att byggnader och material återanvänds, hållbara material väljs och energieffektiva lösningar används. Planen vill också att byggmaterial och byggdetaljer återbrukas i möjligaste mån.",
       "Planen beskriver villastaden som växte fram under 1900-talets första hälft, med en robust kvartersstruktur och en grön lummighet som ska bevaras. Senare tillkom andra områden. I Sjöberg skedde den stora utbyggnaden under 70-, 80- och 90-talen, med en tidstypisk blandning av villor, radhus och flerbostadshus.",
       "För fasaden innebär det att utgångsläget ofta är ett hus som är värt att behålla, men där panel, puts eller isolering har nått slutet av sin livslängd. Friska brädor kan sparas och sättas tillbaka, och originalfönster och detaljer kan renoveras i stället för att bytas.",
     ],
     "aside": {"title": "Ur översiktsplanen", "items": [
       "Funktionella hus ska i regel inte rivas", "Byggnader och material återanvänds",
       "Hållbara material och energieffektiva lösningar", "Byggdetaljer återbrukas"]}},
    {"id": "isolering-sollentuna", "h2": "Tilläggsisolera när panelen ändå ska bytas",
     "paras": [
       "Boverkets energiguide konstaterar att det ofta är en utmaning att få lönsamhet i en tilläggsisolering av fasaden om man bara räknar på energin, och att den blir lönsammast om man passar på när fasaden ändå ska ändras. Ska panelen bytas kan man undersöka om det finns utrymme att komplettera isoleringen eller byta den befintliga mot en med bättre egenskaper.",
       "Myndigheten tar också upp nyttor som inte syns på elräkningen: varmare inomhus på vintern och svalare på sommaren, och att isoleringen kan dämpa buller utifrån. Efteråt behöver värmesystemet justeras in, och i hus med mekanisk ventilation även luftflödena. Ett minskat effektbehov kan dessutom göra det möjligt att säkra ned huvudsäkringen. Tänk också på att väggen blir tjockare, vilket kan påverka dagsljuset och utblicken, och att en utvändig isolering kan inkräkta på grannfastigheten om huset står nära tomtgränsen.",
       "Boverket råder också att dokumentera energianvändningen före renoveringen och följa upp den under första året. Fotografier av väggens uppbyggnad medan den är öppen blir ett värdefullt underlag nästa gång huset ska renoveras. Vill du jämföra med att isolera vinden, se " + _L.format("vindsisolering.html", "vindsisolering") + ".",
     ],
     "aside": None},
    {"id": "puts-regel", "h2": "Puts på trästomme – är fasaden enstegstätad?",
     "paras": [
       "En del yngre hus har puts direkt på isolering på en stomme av träreglar. Boverket beskriver hur träregelväggar började byggas med enstegstätade putssystem eftersom metoden var enkel, och hur fasaden visade sig känslig för skador som släppte in regn och ledde till omfattande fuktskador i väggarna.",
       "På en enstegstätad fasad finns bara en yttre tätningsnivå. Kommer vatten innanför är det inne i väggen och kan bara torka ut långsamt. En tvåstegstätad vägg har i stället en ventilerad luftspalt bakom det yttre skiktet, så att vatten som tar sig förbi kan rinna ut igen. Enligt Boverket fungerar enstegstätning oftast bra på ytor utan genomföringar, men vid fönster, dörrar och andra genomföringar minskar tvåstegstätade detaljer risken.",
       "Vid en renovering av en sådan fasad börjar vi därför med anslutningarna kring fönster och dörrar. Finns det fuktskador i stommen behöver orsaken åtgärdas innan ny puts eller ny beklädnad monteras. Boverket påpekar också att tätning med mjukfog kan ha en relativt kort livslängd även när den är väl utförd, och råder fastighetsägare att besiktiga fasaden regelbundet så att inläckage upptäcks tidigt.",
     ],
     "aside": {"title": "Vanliga riskpunkter", "items": [
       "Fönster och dörrar", "Infästningar för stuprör", "Sprickor i putsen", "Sockel och nederkant"]}},
    {"id": "lov-sollentuna", "h2": "Kulturmiljöplanens lager i detaljplanekartan",
     "paras": [
       "Sollentuna kommun skriver att de bygglovsbefriade åtgärderna inte går att tillämpa för byggnader och områden som är kulturhistoriskt särskilt värdefulla. I kartan med gällande detaljplaner går det att ta fram ett lager som visar vilka områden som omfattas av kulturmiljöplanen. Kommunen påpekar samtidigt att en byggnad kan vara särskilt värdefull även om den inte finns med där, och att du då kan kontakta kommunen.",
       "Utanför de värdefulla miljöerna kräver ett byte av fasadbeklädnad oftast inget bygglov på ett en- eller tvåbostadshus. Vissa detaljplaner har ändå bestämmelser om hur fasadmaterialet ska vara utfört, och för radhus och kedjehus beror möjligheterna på hur bebyggelsen är utformad. Vill du ha ett beslut på att ändringen uppfyller kraven kan du söka frivilligt bygglov.",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgång för fasaden i Sollentuna",
  "steps": [
    ("Platsbesök", "Vi bedömer beklädnad, underlag och anslutningar och noterar vad som kan sparas och återanvändas."),
    ("Fukt och konstruktion", "Vid misstanke om fukt öppnar vi fasaden på utvalda ställen innan arbetet planeras."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där renovering, byte och isolering är uppdelade."),
    ("Detaljplan och kartlager", "Vi kontrollerar detaljplanen och kulturmiljöplanens lager innan material beställs."),
    ("Utförande", "Isolering, vindskydd, luftspalt och beklädnad monteras, med särskild omsorg kring fönster och dörrar."),
    ("Efterarbete", "Fasaden målas eller avfärgas, och vi påminner om injustering av värme och ventilation."),
  ],
  "rot_h2": "Rotavdrag för fasadrenovering i Sollentuna",
  "rot": [
    "I ett småhus ger tilläggsisolering, byte och reparation av fasader, fasadmålning och uppsättning och nedmontering av ställning rotavdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år; tillsammans med rut gäller högst 75 000 kr. Material och resor räknas inte.",
    "Avdraget gäller per person, så två ägare har var sitt utrymme. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad avgör kostnaden?",
  "price": [
    "Hur mycket av beklädnaden som kan sparas, om stommen har fuktskador som måste åtgärdas, hur tjock tilläggsisolering som väljs och hur mycket fönster, dörrar och takfot behöver anpassas. På en putsad regelvägg väger anslutningarna tungt. Vi kommer ut på ett gratis platsbesök och lämnar sedan ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Lönar det sig att tilläggsisolera fasaden på ett 80-talshus i Sjöberg?",
     "Enligt Boverket blir det oftast lönsammast när panelen ändå ska bytas. Hur mycket som sparas beror på hur väl väggarna är isolerade i dag och hur energieffektiv den nya isoleringen är."),
    ("Vår putsade villa i Sollentuna har en trästomme – är det ett problem?",
     "Inte nödvändigtvis, men en enstegstätad putsfasad är känslig för vatten som tar sig in vid fönster och sprickor. Vi kontrollerar anslutningarna och öppnar där det behövs innan något beslutas."),
    ("Hur ser jag om mitt hus omfattas av Sollentunas kulturmiljöplan?",
     "Ta fram kulturmiljöplanens lager i kommunens karta med gällande detaljplaner. Kommunen påpekar att byggnader kan vara värdefulla även utanför lagret, så fråga kommunen om du är osäker."),
    ("Kan gammal panel återanvändas när fasaden renoveras?",
     "Friska brädor kan ofta sparas och sättas tillbaka. Översiktsplanen uppmuntrar återbruk av byggmaterial och byggdetaljer."),
    ("Vad ska göras när fasaden har tilläggsisolerats?",
     "Boverket råder att justera in värmesystemet och vid mekanisk ventilation även luftflödena, och att följa upp energianvändningen under första året."),
  ],
  "sources": [
    ("Sollentuna kommun – Översiktsplan för Sollentuna med sikte på 2040 (pdf)",
     "https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/oversiktsplan/oversiktsplan-for-sollentuna-med-sikte-pa-2040.pdf"),
    ("Sollentuna kommun – Kulturhistoriska byggnader och områden",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/kulturmiljoer/"),
    ("Sollentuna kommun – Fasadändring för en- eller tvåbostadshus",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/fasadandring-for-en--eller-tvabostadshus/"),
    _BV_ISOL, _BV_ENST, _BV_FMAT, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden i Sollentuna renoveras?", "Boka ett gratis platsbesök så går vi igenom vad som kan sparas och vad som behöver bytas."),
  "img": [
    ("Radhus och villor från 1980-talet med träpanel i Sollentuna",
     "1980s Swedish suburban terraced houses and a detached villa with light grey painted horizontal wooden panel, white window frames, gable roofs with red concrete tiles, lush green gardens with birch and pine trees, Sollentuna north of Stockholm, summer daylight, no people, no text"),
    ("Yttervägg med ny isolering, vindskydd och läkt innan panelen sätts upp",
     "exterior wall of a Swedish timber frame house during facade renovation, new mineral wool insulation covered with a white wind barrier and vertical battens forming a ventilated air gap, window opening with new plain metal flashing, no labels, no stickers, no printed tape, no people, daylight, no text"),
  ],
  "related": [
    ("malare-sollentuna.html", "Målare i Sollentuna", "Villor och radhuslängor."),
  ],
},

# ------------------------------------------------------------------ LIDINGÖ
"fasadrenovering-lidingo.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Lidingö", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering på Lidingö – puts och tegel i Hersby",
  "description": "Fasadrenovering på Lidingö: spritputs i Hersby gärde, brädriven puts på Stureplatån, tegel i Hersby åker och stadens blå lager med utökad lovplikt.",
  "h1": "Fasadrenovering på Lidingö",
  "lead": "I Hersby ligger tre av Lidingös radhusområden från efterkrigstiden nära varandra, men med helt olika fasader: brädriven puts på Stureplatån, spritputs i Hersby gärde och rött tegel med gula band i Hersby åker. Geal Entreprenad AB renoverar fasader på hela Lidingö och samordnar ställning, puts, murning, plåt och målning, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Radhus, villor och putsfasader på Lidingö.",
  "sections": [
    {"id": "hersby", "anchor": "Radhusen i Hersby",
     "h2": "Tre radhusområden, tre fasadtekniker",
     "paras": [
       "<strong>Stureplatån.</strong> Radhusen började byggas 1945, och bröderna Erik och Tore Ahlsén ritade längorna i kvarteren Fröja, Heimdal och Skuggan. Kulturmiljöprogrammet beskriver fasader av brädriven slätputs i en färgsättning typisk för 1940-talet, i rött, brutet vitt, gult och grönt, med beigeputsade omfattningar som delar in och ramar in fasaderna.",
       "<strong>Hersby gärde.</strong> Radhusen vid Kämpavägen och Laduvägen ritades 1948 av Ancker, Gate & Lindegren. Fasaderna är spritputsade i gråbeige eller brunrosa, med slätputsade lisener, fönster- och dörromfattningar och gesimser. Fönstren sitter i fasadliv, på övre våningen hänger de i gesimsen, och taken saknar taksprång.",
       "<strong>Hersby åker.</strong> Holger Blom ritade de 13 radhuslängorna, uppförda 1949–1956. Fasaderna är murade i rött tegel med dekorativa band av gult tegel som markerar vånings- och lägenhetsindelning, och socklarna är grå. Programmet beskriver husen som i stort sett oförändrade sedan de byggdes.",
     ],
     "aside": {"title": "Fasaderna i Hersby", "items": [
       "Stureplatån: brädriven slätputs i mättade kulörer", "Hersby gärde: spritputs med släta detaljer",
       "Hersby åker: rött tegel med gula band", "Alla tre: särskilt värdefulla kulturmiljöer"]}},
    {"id": "puts-lidingo", "h2": "Laga puts så att strukturen blir densamma",
     "paras": [
       "På en putsfasad syns en lagning med fel struktur på långt håll. I Hersby gärde är det kontrasten mellan grov spritputs på väggytorna och slät puts kring fönster, dörrar och hörn som bär arkitekturen, och programmet råder att de spritputsade fasaderna underhålls så att de behåller sin ursprungliga karaktär. På Stureplatån är det i stället den släta, brädrivna ytan som ska återskapas.",
       "Boverket skriver att de vanligaste skadorna på putsade fasader är sprickor och putsbortfall, och att putsbortfall i de allra flesta fall beror på fukt. Fuktig puts kan frysa sönder om fukten blir kvar i fasaden över vinterhalvåret. Innan något lagas letar vi därför efter orsaken: ett läckande fönsterbleck, en skadad gesims eller en sockel som suger vatten.",
       "Lös puts knackas ner, underlaget rensas och nytt bruk byggs upp i samma tjocklek och struktur som det gamla. Därefter avfärgas hela fasadytan, så att lagningen smälter in. Programmet råder också att äldre fönster, dörrar och smidesräcken bevaras och renoveras med väl anpassade material och metoder, och att kopior tillverkas när originalen inte går att rädda. Färgsättningen hör till det programmet vill bevara, och mer om den finns hos " + _L.format("malare-lidingo.html", "målare på Lidingö") + ".",
     ],
     "aside": None},
    {"id": "tegel-lidingo", "h2": "Tegelfasaderna i Hersby åker",
     "paras": [
       "För Hersby åker säger programmet att fasaderna av rött tegel med gula band har en sammanhållande verkan i området och bör underhållas så att de behåller sin ursprungliga karaktär. De dekorativa skärmtaken med fransade baldakiner och balkongerna med smidesräcken bör underhållas med traditionella material och metoder.",
       "En tegelfasad behöver sällan mer än lagning av fogar och enstaka stenar, men arbetet syns om fogbruket får fel kulör eller sammansättning. Därför provar vi bruket mot befintliga fogar innan arbetet börjar. Där skärmtak, balkonger och fönsterbleck ansluter mot teglet kontrollerar vi att vattnet leds bort från muren.",
       "Utvändig tilläggsisolering är knappast aktuell på husen i Hersby. Fönstren i Hersby gärde sitter i fasadliv, taken saknar taksprång och fasaderna har lisener och gesimser, och en tjockare vägg skulle ändra allt det. Boverket påpekar att invändig isolering i stället lämnar fasaden orörd, men att den ökar risken för fuktskador som frostsprängning i tegel och sten.",
     ],
     "aside": {"title": "Råd för Hersby åker", "items": [
       "Underhåll rött tegel med gula band", "Bevara och renovera dörrar och fönster",
       "Traditionella metoder för skärmtaken", "Bevara balkongernas smidesräcken"]}},
    {"id": "lov-lidingo", "h2": "Utökad lovplikt kan gälla även underhåll",
     "paras": [
       "Lidingö stad skriver att bygglov för fasadändringar på en- och tvåbostadshus slopades den 1 december 2025, men att utökad lovplikt gäller för de flesta byggnadsåtgärder inom särskilt kulturhistoriskt värdefulla områden. I stadens webbkarta visas de som ett blått lager, och en gulmarkerad fastighet kan ha värden som behöver bedömas.",
       "Kulturmiljöprogrammets första del, en handbok för fastighetsägare, beskriver hur detaljplaner och områdesbestämmelser kan ge utökad lovplikt även för omfärgning, byte av fasadbeklädnad och underhåll av ett byggnadsverk. En skyddsbestämmelse kan dessutom precisera hur underhållet ska utföras. Råden för de enskilda områdena är inte juridiskt bindande, men staden använder dem som stöd när bygglov och planärenden handläggs.",
       "Är du osäker på vad som gäller för ditt radhus kan du söka frivilligt bygglov eller kontakta stadens kundcenter. I en radhuslänga är det också klokt att stämma av med grannarna, eftersom fasaden läses som en helhet.",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången för en fasad på Lidingö",
  "steps": [
    ("Besök i längan", "Vi tittar på puts, tegel, fogar, gesimser och bleck och jämför med grannhusen i samma länga."),
    ("Programmet och kartan", "Vi läser områdets råd i kulturmiljöprogrammet och kontrollerar om fastigheten ligger i det blå lagret."),
    ("Kostnadsförslag", "Lagning, omfogning, avfärgning och plåtarbeten redovisas var för sig i ett skriftligt förslag."),
    ("Provytor", "Bruk och struktur provas på en liten yta, så att lagningen matchar det befintliga."),
    ("Utförande", "Lös puts tas ner, fogar och skador lagas och bleck och gesimser ses över."),
    ("Avfärgning och genomgång", "Fasaden avfärgas i den ursprungliga kulören och vi går igenom resultatet med dig."),
  ],
  "rot_h2": "ROT-avdrag på Lidingö",
  "rot": [
    "Att mura och reparera fasader, byta och reparera fasader och rengöra och måla fasader i ett småhus ger rotavdrag. Skatteverket medger 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och rot och rut tillsammans får inte överstiga 75 000 kr.",
    "Är radhuset en bostadsrätt gäller avdraget bara arbete inne i bostaden, så fasaden ger då inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Kostnaden beror på",
  "price": [
    "Hur stora ytor av putsen som har släppt, hur mycket fogar och tegel som behöver lagas, om gesimser, omfattningar och skärmtak ska återskapas och hur stor del av fasaden som ska avfärgas. Radhus uppe på en bergknalle kan kräva mer ställning. Platsbesöket kostar inget, och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur lagas spritputsen på ett radhus i Hersby gärde?",
     "Lös puts tas ner och nytt bruk läggs på i samma grova struktur som det gamla, medan omfattningar och lisener slätputsas. Därefter avfärgas ytan så att lagningen inte syns."),
    ("Behöver vi lov för att foga om tegelfasaden i Hersby åker?",
     "Omfogning i samma utförande är underhåll. Har detaljplanen utökad lovplikt för underhåll eller en skyddsbestämmelse kan lov ändå krävas, så kontrollera planen och stadens karta."),
    ("Går det att tilläggsisolera ett radhus på Stureplatån?",
     "Utvändigt är det svårt utan att putsfasadens uttryck förändras, och området är utpekat som särskilt värdefullt. Vinden eller invändiga åtgärder är ofta ett bättre ställe att börja."),
    ("Varför släpper putsen på vårt hus på Lidingö?",
     "Enligt Boverket beror putsbortfall i de allra flesta fall på fukt. Vi letar efter källan, som bleck, sockel eller sprickor, innan putsen lagas."),
    ("Är kulturmiljöprogrammets råd för Hersby bindande?",
     "Nej, råden och rekommendationerna är inte juridiskt bindande. Staden använder dem dock som stöd när bygglov och planärenden handläggs."),
  ],
  "sources": [
    ("Lidingö stad – Ändrade lagar och regler för byggande",
     "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/"),
    ("Lidingö stad – Kulturmiljöprogram del 1: Handbok för fastighetsägare (pdf)", "https://share.mediaflow.com/sv/?7ZCCF1REBX"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Stureplatån (pdf)", "https://share.mediaflow.com/sv/?3HCCO15EDL"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Hersby gärde (pdf)", "https://share.mediaflow.com/sv/?7FCCM1UEIL"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Hersby åker (pdf)", "https://share.mediaflow.com/sv/?8HCCO11ESL"),
    _BV_FMAT, _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på Lidingö lagas eller avfärgas?", "Boka ett gratis platsbesök så går vi igenom puts, tegel och lovfrågor."),
  "img": [
    ("Radhuslänga med spritputs och rött tegeltak i Hersby på Lidingö",
     "late 1940s Swedish two-storey terraced row houses with greyish beige rough-cast render, smooth light render around windows and corners, asymmetric gable roofs with red clay tiles and no eaves overhang, small front gardens with low hedges, Lidingö Stockholm, autumn daylight, no people, no text"),
    ("Tegelfasad med gula tegelband på ett radhus från 1950-talet",
     "close-up of a 1950s Swedish terraced house facade in red brick with decorative horizontal bands of yellow brick, grey plinth, muted weathered ochre-yellow brick bands, realistic aged bricks, plain wall without cables, daylight, no people, no text"),
  ],
  "related": [
    ("malare-lidingo.html", "Målare på Lidingö", "Panel, puts och slamfärg."),
    ("byggforetag-lidingo.html", "Byggföretag på Lidingö", "Tillbyggnad och renovering."),
  ],
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
