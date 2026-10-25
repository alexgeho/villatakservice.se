# -*- coding: utf-8 -*-
"""Målare – ortsidor v2: Danderyd, Lidingö, Järfälla, Haninge, Tyresö, Värmdö (2026-10-25).
Fakta endast från källorna i respektive 'sources' (kommunernas kulturmiljöprogram/riktlinjer och
bygglovssidor, Stockholms läns museum, Riksantikvarieämbetet, Boverket, Skatteverket, SMHI).
Lokala uppgifter delvis omformulerade från tools/takreno_orter.py (TRP), där källan redan var verifierad.
Schema: se tools/tj_check.py."""

_BOV = ("Boverket – Bygglov för fasadändring (PBL kunskapsbanken)",
        "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_RAA = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf)",
        "https://www.raa.se/publicerat/9789172095830.pdf")
_SKV = ("Skatteverket – Så fungerar rotavdraget",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV2 = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
         "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV3 = ("Skatteverket – Rotavdrag vid målning av fönster i bostadsrätt",
         "https://www.skatteverket.se/privat/etjansterochblanketter/svarpavanligafragor/rotochrutarbete/privatrotochrutarbetefaq/ettforetagskamalaomfonstreniminbostadsrattkanjagfarotavdragforalltmaleriarbete.5.71004e4c133e23bf6db8000116517.html")
_SMHI = ("SMHI – Salt i haven runt Sverige",
         "https://www.smhi.se/kunskapsbanken/oceanografi/haven-runt-sverige/salt-i-haven-runt-sverige-")
_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 8 kap. 14 och 17 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ DANDERYD
"malare-danderyd.html": {
  "kind": "district", "service": "malare", "ort": "Danderyd", "svc_label": "Målare",
  "title": "Målare i Danderyd – tidstypisk färgsättning",
  "description": "Målare i Danderyd: kommunens riktlinjer för ommålning, lovplikt i riksintressena och renovering av äldre fönster och portar. Gratis platsbesök.",
  "h1": "Målare i Danderyd",
  "lead": "I Danderyd är det sällan kulören ensam som avgör hur ett hus ska målas om. Kommunens riktlinjer från 2024 säger för område efter område att tidstypisk färgsättning ska vara vägledande, och i villastäderna Djursholm och Stocksund gäller lovplikt för ommålning. Geal Entreprenad AB tar målningsuppdrag ute och inne i hela kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villor, egnahem och grupphus i Danderyd.",
  "sections": [
    {"id": "riktlinjer", "anchor": "Kommunens riktlinjer",
     "h2": "En mening som återkommer i nästan varje område",
     "paras": [
       "Miljö- och stadsbyggnadsnämnden antog i december 2024 riktlinjer för kulturhistoriska byggnader och miljöer i Danderyd. Dokumentet är en vägledning när kommunen prövar plan- och lovärenden, men det vänder sig också direkt till fastighetsägarna. Riktlinjerna går igenom 27 områden i Enebyberg, Danderyd, Djursholm och Stocksund, och i nästan alla står samma rad: tidstypisk färgsättning ska vara vägledande vid ommålning.",
       "Det gäller inte bara sekelskiftesvillorna. Raden finns för egnahemmen i Enebyberg och Klingsta, för funktionalismen i Klingsta och Stocksund, för grupphusbebyggelsen i både Danderyd och Djursholm och för 1940- och 50-talshusen i Söderskogen. För området som kallas det moderna Danderyd lägger riktlinjerna till att fasaduttryck som inte hör till 1950- eller 1960-talets stilideal bör undvikas.",
       "Ett radhus från 1970-talet kan alltså omfattas av samma resonemang som en villa från 1910. Skillnaden är vilken tid som är den tidstypiska – och det är det första en målare behöver ta reda på innan kulörer och färgtyp väljs.",
     ],
     "aside": {"title": "Innan kulören väljs", "items": [
       "Sök adressen i kommunens kulturmiljökarta", "Vilket område och vilken stil hör huset till?",
       "Finns originalritningar med färgangivelser?", "Vilken färgtyp sitter på i dag?"]}},
    {"id": "lov-danderyd", "h2": "Ommålning är lovfri – utom där det räknas",
     "paras": [
       "På sin sida om de nya reglerna från 1 december 2025 skriver Danderyds kommun att ommålning, nytt tak och nya fönster inte kräver bygglov på ett en- eller tvåbostadshus. Ändringarna ska ändå göras varsamt och anpassas till byggnadens värden. Lov krävs alltid om fastigheten ligger i ett kulturhistoriskt särskilt värdefullt område eller om byggnaden själv är särskilt värdefull, och kommunen skriver att lovplikten alltid gäller inom riksintressen för kulturmiljövården. Djursholms och Stocksunds villastäder är riksintressen sedan 1987.",
       "Boverket skiljer mellan att byta kulör och att måla om i samma kulör. Det senare räknas i regel som underhåll. Att byta färgtyp, till exempel från linoljefärg till en plastfärg, är inget kulörbyte, men det kan påverka husets yttre karaktärsdrag och därmed bli en del av prövningen i ett värdefullt område.",
       "Är du osäker på om en ny kulör är förenlig med kraven kan du söka ett frivilligt bygglov. Kommunen nämner den möjligheten för de lovbefriade åtgärderna, och med ett beslut i handen vet du att färgsättningen håller.",
     ],
     "aside": {"title": "Lov krävs för ny kulör om", "items": [
       "Huset ligger i Djursholms eller Stocksunds riksintresse",
       "Området är kulturhistoriskt särskilt värdefullt", "Byggnaden själv är särskilt värdefull",
       "Detaljplanen har utökad lovplikt"]}},
    {"id": "tidstypiskt", "h2": "Så tar man reda på vad som är tidstypiskt",
     "paras": [
       "Det bästa underlaget sitter ofta på huset. Under lister, bakom stuprör och i skyddade hörn kan äldre färglager finnas kvar som visar husets tidigare kulörer. Riksantikvarieämbetet rekommenderar dessutom att man vid varje renovering lämnar några små provytor obehandlade på undanskymda ställen och sparar uppgifter om vilka material som har använts. Det beskrivs som den bästa dokumentationen för nästa ommålning.",
       "Myndigheten råder också till att skriva en tydlig arbetsbeskrivning när traditionella färgtyper ska användas, där bindemedel, pigment och behandlingsmetod anges. Annars finns en risk att utföranden med helt andra egenskaper betraktas som likvärdiga. För en villa i ett riksintresse är en sådan beskrivning dessutom ett bra underlag om kommunen vill se hur arbetet ska göras.",
       "I grupphusområdena är frågan enklare men lika viktig. Riktlinjerna vill att områdenas enhetliga karaktär mot gatan behålls, och ett hus som får en egen kulör i en länga eller rad syns tydligt.",
     ],
     "aside": None},
    {"id": "snickerier", "h2": "Fönster och portar: renovera och måla hellre än byta",
     "paras": [
       "Riktlinjerna lyfter särskilt fram äldre fönster och dörrar. De beskrivs som byggnadsdelar med generellt högt kulturhistoriskt värde, ofta av hög kvalitet, som med fördel kan renoveras i stället för att bytas ut. I flera områden står det uttryckligen att fönster och portar i originalutförande ska värnas.",
       "För målaren innebär det kittning, skrapning och målning av bågar, karmar och foder – ett arbete som tar tid men som riksantikvarieämbetets handbok beskriver som löpande underhåll. Fönster, vattbräder, trappor och räcken är hårt utsatta för väder, och väntar man för länge riskerar underlaget att skadas. Söderfasader behöver dessutom målas om oftare än norrfasader. Är fönstren för långt gångna finns mer om alternativen under " + _L.format("fonsterbyte.html", "fönsterbyte") + ", och trasiga foder eller dörrblad kan lagas av en " + _L.format("snickare.html", "snickare") + " innan de målas.",
     ],
     "aside": None},
    {"id": "tomt", "h2": "Vårdat skick på stora trädgårdstomter",
     "paras": [
       "Riktlinjerna påminner om att du som fastighetsägare enligt plan- och bygglagen ska hålla byggnaderna i vårdat skick och underhålla dem så att utformning och tekniska egenskaper i huvudsak bevaras. Regelbunden målning är en stor del av det underhållet.",
       "Trädgården räknas också in i kulturmiljön. Riktlinjerna nämner äldre träd, fruktträd, staket, murar och grusade gångar som värden att ta hänsyn till. Därför planeras ställning, avtäckning och uppställning vid platsbesöket, så att rabatter, häckar och gamla träd klarar sig medan fasaden målas.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Danderyd till",
  "steps": [
    ("Platsbesök", "Vi tittar på fasad, fönster och portar och gör skrapprov för att se vilka färglager och färgtyper som finns."),
    ("Riktlinjer och karta", "Vi stämmer av kulturmiljökartan och vad riktlinjerna säger om området, och om ny kulör kräver lov."),
    ("Arbetsbeskrivning och kostnadsförslag", "Färgtyp, kulör, underarbete och antal strykningar skrivs ut, så att förslaget kan användas som underlag."),
    ("Förarbete", "Tvätt, skrapning, lagning av trä och kittning av fönster. Provytor lämnas på undanskymda ställen."),
    ("Målning", "Strykningarna görs i lämpligt väder och med de torktider färgtypen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och noterar vilka material som använts."),
  ],
  "rot_h2": "ROT-avdrag för målning i Danderyd",
  "rot": [
    "Skatteverket räknar målning av fasader, fönster, väggar, tak och golv samt tapetsering som rotarbete i ett småhus. Att måla staket och murar ger inget avdrag, och färg räknas som material. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och tillsammans med rutavdrag högst 75 000 kr.",
    "Bor ni två ägare i villan kan ni båda göra avdrag för er del av arbetet. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad avgör priset?",
  "price": [
    "På Danderyds äldre villor väger fönster, portar och snickerier tyngst, tillsammans med husets höjd och hur mycket gammal färg som måste bort. Traditionella färgtyper kan kräva fler och tunnare strykningar. På grupphus och radhus är det oftare panelens skick och mängden skrapning som styr. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Gäller kommunens riktlinjer för ommålning även vårt radhus i Danderyd?",
     "Om radhuset ligger i ett av de områden riktlinjerna beskriver, till exempel grupphusbebyggelsen i Danderyd eller Djursholm, är tidstypisk färgsättning vägledande även där. Riktlinjerna är en vägledning, men kommunen använder dem vid lovprövning."),
    ("Behöver jag lov för att måla om villan i Djursholm i exakt samma kulör?",
     "Samma kulör och samma färgtyp räknas enligt Boverket normalt som underhåll. Ska kulören eller färgtypen ändras inom riksintresset gäller enligt kommunen lovplikt."),
    ("Hur får man fram husets ursprungliga kulörer?",
     "Genom skrapprov på skyddade ställen, äldre ritningar och foton. Riksantikvarieämbetet rekommenderar också att man sparar provytor vid varje renovering, så att nästa ommålning har ett facit."),
    ("Kan ni renovera och måla de gamla fönstren i stället för att byta dem?",
     "Ja. Bågarna skrapas, kittas och målas, och skadat trä lagas. Kommunens riktlinjer förordar renovering av äldre fönster och portar framför byte."),
    ("Är frivilligt bygglov värt det för en ny fasadkulör i Danderyd?",
     "Kommunen erbjuder det för lovbefriade åtgärder. Det tar längre tid, men du får ett beslut på att färgsättningen uppfyller kraven, vilket kan vara tryggt på ett hus nära ett värdefullt område."),
  ],
  "sources": [
    ("Danderyds kommun – Riktlinjer för kulturmiljöhistoriska byggnader och miljöer 2024 (pdf)",
     "https://www.danderyd.se/globalassets/globala-filer/kommun-och-politik/ovriga-styrdokument-ny/styrande-dokument---samhallsbyggnad-miljo-och-exploatering/riktlinjer-for-kulturmiljohistoriska-byggnader-och-miljoer-i-danderyd-2024.pdf"),
    ("Danderyds kommun – Nya regler för bygglov från 1 december 2025",
     "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/"),
    ("Danderyds kommun – Översiktsplan, Riks- och mellankommunala intressen (pdf)",
     "https://danderyd.se/contentassets/94fc6956dc264c4cab52c0a18ff5bafd/3-riks--och-mellankommunala-intressen.pdf"),
    _RAA, _BOV, _SKV, _SKV2,
  ],
  "cta": ("Ska huset i Danderyd målas om?", "Boka ett gratis platsbesök så går vi igenom färglager, kulör och lovfrågor på plats."),
  "img": [
    ("Nymålad ljusputsad villa med mörka fönsterbågar och stor trädgård i Djursholm",
     "large early 1900s Swedish national romantic villa with freshly painted light rendered facade, dark painted window frames with small panes, steep red clay tile roof, big old oak and fruit trees in a large garden, Djursholm Danderyd, early summer, no people"),
    ("Fönsterbåge där äldre färglager har skrapats fram före ommålning",
     "close-up of an old wooden window sash on a Swedish villa being restored, scraped paint revealing several older colour layers, fresh linseed putty along the glass, small paint brush and scraper on the window sill, no people"),
  ],
},

# ------------------------------------------------------------------ LIDINGÖ
"malare-lidingo.html": {
  "kind": "district", "service": "malare", "ort": "Lidingö", "svc_label": "Målare",
  "title": "Målare på Lidingö – mörk panel, ljus puts och slamfärg",
  "description": "Målare på Lidingö: färgsättning enligt stadens kulturmiljöprogram, utökad lovplikt i kartans blå lager och traditionella färgtyper. Gratis platsbesök.",
  "h1": "Målare på Lidingö",
  "lead": "Ska huset på Lidingö målas om finns det sällan ett bättre underlag än stadens kulturmiljöprogram från 2024. Där beskrivs, område för område, vilka fasader och kulörer husen hade från början – från tjärad panel i Herserud till slammat tegel i Mölna. Geal Entreprenad AB tar målningsuppdrag ute och inne på hela ön, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villastäder, radhusbyar och stugor på Lidingö.",
  "sections": [
    {"id": "fasader", "anchor": "Fasaderna på Lidingö",
     "h2": "Fyra miljöer, fyra färgskalor",
     "paras": [
       "<strong>Herseruds villastad.</strong> Flera av de tidiga villorna från omkring 1908–1915 är klädda med liggande panel och stående lockpanel i gavlarna. Kulturmiljöprogrammet skriver att panelen i regel var mörkfärgad eller tjärad från början, och att bottenvåningen inte sällan är slätputsad och ljus i kontrast mot den mörka övervåningen. Andra villor har mörk panel med listverk i vitt.",
       "<strong>Lidingö villastad.</strong> Under 1920-talet byggdes villor i en klassicerande stil med förebilder i svenskt 1700-tal och empir. Fasaderna kläddes med locklistpanel eller puts i ljusa kulörer, med detaljer som hörnpilastrar och lunettfönster. Programmet säger att ursprunglig färgsättning och fasadmaterial bör vara vägledande vid ommålning.",
       "<strong>Mölna radhusby.</strong> Nils Teschs radhus har fasader av slammat tegel avfärgat i ljust beigegrått. Programmet rekommenderar att fönster och ytterdörrar behålls och renoveras så långt som möjligt och målas med traditionella färgtyper, och att den ursprungliga färgsättningen bevaras.",
       "<strong>Dalakolonin på Bosön.</strong> Här har de äldsta av omkring 60 stugor faluröd panel, ofta vitmålade spröjsade fönster och fönsterluckor. Bystugan från 1930 har faluröd panel, listverk i vitt och luckor i dalablått.",
     ],
     "aside": {"title": "Ur kulturmiljöprogrammet", "items": [
       "Herserud: mörk eller tjärad panel", "Villastaden: ljus locklistpanel eller puts",
       "Mölna: slammat tegel i ljust beigegrått", "Dalakolonin: faluröd panel och vita fönster"]}},
    {"id": "lov-lidingo", "h2": "Det blå lagret i stadens karta avgör",
     "paras": [
       "Lidingö stad skriver att bygglov för fasadändringar på en- och tvåbostadshus slopades den 1 december 2025, och nämner uttryckligen målning bland de ändringar som omfattas. Undantaget är de områden och byggnader som är särskilt värdefulla. De har utökad lovplikt, och i stadens webbkarta visas de som ett blått lager. Klickar du på din fastighet syns det om den omfattas.",
       "Är fastigheten i stället gulmarkerad kan det enligt staden finnas värden som behöver bedömas, och då är rådet att kontakta kundcenter innan du bestämmer dig. Kulturmiljöprogrammet, som kommunfullmäktige antog den 16 december 2024, är inte juridiskt bindande men används som kunskapsunderlag vid bygglov.",
       "Boverket påpekar att ett byte av färgtyp inte räknas som kulörbyte, men att det kan påverka husets karaktärsdrag. I Mölna, där programmet uttryckligen förordar traditionella färgtyper, är det därför klokt att låta färgtypen ingå i samma fråga som kulören.",
     ],
     "aside": {"title": "Kontrollera i kartan", "items": [
       "Blått lager: utökad lovplikt", "Gul markering: värden att bedöma",
       "Byggnadsminne: Länsstyrelsen prövar", "Detaljplanens bestämmelser"]}},
    {"id": "fargtyper", "h2": "Tjära, slamfärg och puts – tre olika underlag",
     "paras": [
       "En tjärad eller mörk panel från villastädernas första år kan ha strukits om med helt andra produkter under 1900-talet. Riksantikvarieämbetet varnar för att lägga moderna färger över äldre färgtyper och skriver att röd slamfärg som har blandats med trätjära normalt behöver samma tillsats även vid ommålning, för att färgen ska fästa och kulören bli jämn. Skrapprov på flera ställen visar vad som faktiskt sitter på.",
       "På Dalakolonins stugor är frågan om slamfärgen ska fortsätta. Myndigheten är tydlig: en slamfärgsmålad yta ska bara målas om med slamfärg, och har man en gång gått över till en annan färgtyp går det inte att återvända, även om den gamla färgen tas bort.",
       "Putsade bottenvåningar och slammade tegelfasader kräver en färg som fungerar med putsens sammansättning. Kalkfärg har god vidhäftning på kalkputs men dålig på cementrika underlag. Ska putsen lagas mer omfattande hör det hemma under " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
    {"id": "fjardar", "h2": "Fjärdarna runt ön sliter på utsatta sidor",
     "paras": [
       "Lidingö är en ö, och många hus står högt i terrängen eller nära stranden. Väggar som vetter mot öppet vatten får mer sol, regn och blåst. Riksantikvarieämbetet skriver att söderfasader behöver målas om oftare än norrfasader och att fönster, vattbräder, trappor och räcken bör underhållsmålas löpande, eftersom målningen där har en direkt skyddande funktion.",
       "Det betyder att alla sidor av ett hus sällan behöver samma insats samma år. En bättringsmålning av de mest utsatta delarna kan skjuta upp en hel ommålning. Ska taket ses över samtidigt som ställningen står uppe, kan " + _L.format("takmalning.html", "takmålning") + " eller plåtarbeten samordnas med fasaden.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning på Lidingö till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, puts, fönster och snickerier och gör skrapprov för att se vilken färgtyp som finns."),
    ("Kartan och programmet", "Vi kontrollerar om fastigheten ligger i det blå lagret och vad kulturmiljöprogrammet säger om området."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, underarbete och antal strykningar står med, och utsatta fasader kan prissättas för sig."),
    ("Förarbete", "Tvätt, skrapning och lagning av trä eller puts, kittning av fönster och skydd av trädgården."),
    ("Målning", "Grundning och strykningar i lämpligt väder, med de torktider färgtypen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "Rotavdrag för målning på Lidingö",
  "rot": [
    "I villa och radhus med äganderätt ger både fasadmålning, fönstermålning och invändig målning rotavdrag, men inte målning av staket eller murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och tillsammans med rutavdrag högst 75 000 kr. Färgen räknas som material.",
    "I bostadsrätt gäller avdraget bara arbete inne i lägenheten, och för fönster bara insidan. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden?",
  "price": [
    "Priset beror mest på underarbetet: hur mycket gammal färg som måste bort, hur mycket trä eller puts som behöver lagas och hur många fönster med spröjs som ska kittas. Traditionella färgtyper kan kräva fler strykningar, och höga hus på branta tomter behöver mer ställning. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag måla om min villa i Herserud i en ljus kulör när den var mörk från början?",
     "Ligger huset i det blå lagret krävs bygglov för ny kulör. Kulturmiljöprogrammet beskriver den mörka eller tjärade panelen som ursprunglig och säger att tidstypisk färgsättning bör vara vägledande, så räkna med att staden väger in det."),
    ("Kan vi stryka modern täckfärg på stugan i Dalakolonin?",
     "Det går, men Riksantikvarieämbetet avråder. Har slamfärgen en gång täckts med en annan färgtyp går det inte att återgå till slamfärg, och programmet beskriver den faluröda panelen som en del av områdets karaktär."),
    ("Vilken färg ska man använda på fönstren i Mölna radhusby?",
     "Kulturmiljöprogrammet rekommenderar traditionella färgtyper och att befintliga fönster och dörrar renoveras så långt det går."),
    ("Vår fastighet på Lidingö är gulmarkerad i kartan – får vi välja kulör fritt?",
     "Gulmarkeringen betyder enligt staden att det kan finnas värden som behöver bedömas. Kontakta kundcenter innan kulören bestäms, så vet vi vad som gäller när arbetet planeras."),
    ("Behöver alla fasader målas samtidigt på ett hus vid vattnet?",
     "Inte nödvändigtvis. Söderfasader och sidor mot öppet vatten slits fortare, och en bättringsmålning av dem kan räcka några år innan resten behöver göras."),
  ],
  "sources": [
    ("Lidingö stad – Ändrade lagar och regler för byggande",
     "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/"),
    ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet",
     "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Herseruds villastad (pdf)", "https://share.mediaflow.com/sv/?F6CCU10E82"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Lidingö villastad (pdf)", "https://share.mediaflow.com/sv/?9OCCB1KE1L"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Mölna radhusby (pdf)", "https://share.mediaflow.com/sv/?3ZCCS1LEFX"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Dalakolonin (pdf)", "https://share.mediaflow.com/sv/?13CCQ1AEVX"),
    _RAA, _BOV, _SKV, _SKV2, _SKV3,
  ],
  "cta": ("Ska huset på Lidingö målas om?", "Boka ett gratis platsbesök så går vi igenom färgtyp, kulör och kartan på plats."),
  "img": [
    ("Villa med mörk träpanel på övervåningen och ljus puts på bottenvåningen på Lidingö",
     "two-storey early 1910s Swedish national romantic villa, ground floor with smooth white lime render, upper floor and gable clad in dark brown tarred horizontal wooden boards with vertical boards in the gable, clear contrast between light ground floor and dark upper floor, white window frames, steep red clay tile roof, mature pines and low granite outcrops in a garden, Stockholm suburb, summer, no people"),
    ("Faluröd stuga med vita knutar och spröjsade fönster på Lidingö",
     "small old Swedish allotment cottage with falu red wooden panelling, white mullioned windows and window shutters painted dala blue, felt-covered gable roof, birch trees and meadow, Lidingö, summer, no people"),
  ],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"malare-jarfalla.html": {
  "kind": "district", "service": "malare", "ort": "Järfälla", "svc_label": "Målare",
  "title": "Målare i Järfälla – spritputs, radhuslängor och kulör",
  "description": "Målare i Järfälla: putsade radhus och kedjehus från 60-talet, färgsättning per länga enligt kulturmiljöplanen och lov för ny kulör. Gratis platsbesök.",
  "h1": "Målare i Järfälla",
  "lead": "Många av Järfällas småhus byggdes i grupp av samma byggfirma, med samma puts eller panel och en gemensam färgskala. När husen målas om är det därför längan eller kvarteret som är enheten, inte det enskilda huset. Geal Entreprenad AB tar målningsuppdrag i hela kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Putsade radhus, kedjehus och villor i Järfälla.",
  "sections": [
    {"id": "grupper", "anchor": "Husen i Järfälla",
     "h2": "Byggfirmornas hus och deras ursprungliga färger",
     "paras": [
       "Kommunens kulturmiljöplan från 1999 beskriver material och färgsättning för varje utpekad miljö. I Ekedal, som Widmark &amp; Platzer började bygga 1958, är husen genomgående spritputsade och radhusens gavlar har dekorband i slätputs. Färgskalan var från början grå, beige och gul. Kedjehusen vid Dressyrvägen från mitten av 1960-talet har beige spritputs med dekorband i vitt, och vid Betselvägens 1950-talsvillor dominerar ljus, beige puts.",
       "Vid Skogsvägen och Toppvägen, byggda i början av 1960-talet av flera olika firmor, är fasaderna i stället oftast locklistpanel i ljusa kulörer. Kedjehusen vid Toppvägen har tvåfärgade gavlar, ljusare nedtill och mörkare upptill.",
       "I Kallhäll byggde Bolinders radhus och villor för sina anställda. Radhusen hade ljust målad locklistpanel men kläddes på 1970-talet med plåtpanel i en dovare färgskala. Villorna i Skogstorp hade också locklistpanel i grått, gult, beige eller ljus puts, och planen konstaterar att många har ändrats sedan dess.",
     ],
     "aside": {"title": "Ursprungliga färgskalor", "items": [
       "Ekedal: grått, beige och gult", "Dressyrvägen: beige med vita dekorband",
       "Toppvägen: tvåfärgade gavlar", "Bolinderbyn: ljus locklistpanel"]}},
    {"id": "langan", "h2": "Flera nyanser inom samma skala – inte en egen kulör",
     "paras": [
       "Kulturmiljöplanen är ovanligt konkret om vad som går förlorat. Om Ekedal skriver den att radhuslängorna i vissa fall ger ett splittrat intryck, eftersom den genomtänkta färgsättningen av varje länga, med flera nyanser inom samma färgskala, har bytts ut mot en mer individuell färgsättning. Planen tycker att färgsättningen bör knyta an mer till den ursprungliga när husen renoveras.",
       "För Dressyrvägen, som beskrivs som mycket välbevarad, är rekommendationen att material och färgsättning inte ändras vid renoveringar. Och för Bolinderbyn skriver planen att det är av största vikt att alla radhuslängor har samma typ av fasadmaterial och en genomtänkt färgsättning.",
       "Praktiskt betyder det att grannarna i en länga tjänar på att bestämma kulörer tillsammans, gärna med en gemensam provyta på en gavel. Riksantikvarieämbetet påpekar, om kalkfärg, att kulöravvikelser lätt uppstår om färgen blandas vid olika tillfällen. Samma risk finns när en länga målas i flera omgångar, så färgen bör beställas med samma recept för alla hus.",
     ],
     "aside": None},
    {"id": "puts", "h2": "Att måla spritputs",
     "paras": [
       "En spritputsad fasad har en grov, ojämn yta som samlar smuts och påväxt i fördjupningarna. Riksantikvarieämbetet skriver att spritputs bör rengöras skonsamt med våt- eller vattenblästring i stället för stålborste, så att strukturen inte slits ner. Sprickor och lösa partier lagas med ett bruk som liknar det befintliga innan något målas.",
       "Valet av färg beror på vad putsen består av och vad den är målad med sedan tidigare. Kalkfärg fäster bra på kalkputs men dåligt på cementrika underlag, och myndigheten noterar att man vid mitten av 1900-talet alltmer gick över till kalkcementbruk och andra färger än kalkfärg. En puts från 1960-talet behöver därför provas innan färgtypen bestäms. Ska fasaden i stället putsas om eller tilläggsisoleras är det ett jobb för " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
       "Kulturmiljöplanen beskriver materialval och dekor som typiska för de områden Widmark &amp; Platzer byggde i Järfälla. Dekorbanden i slätputs målas därför för hand och i sin egen kulör, så att gavlarna behåller sitt utseende.",
     ],
     "aside": {"title": "Före målning av puts", "items": [
       "Skonsam tvätt av strukturen", "Lagning av sprickor med likvärdigt bruk",
       "Prov av vilken färg som sitter på", "Gemensam provyta för längan"]}},
    {"id": "lov-jarfalla", "h2": "Lov och detaljplan i Järfälla",
     "paras": [
       "Järfälla kommun skriver att fasadändringar på en- och tvåbostadshus inte kräver bygglov, och räknar byte av färg på fasaden till fasadändringarna. Undantagen är särskilt värdefulla byggnader och områden och detaljplaner med utökad lovplikt. Kommunen påpekar också att lovfria fasadändringar ändå ska stämma med detaljplanen och utföras varsamt så att husets värden tas till vara.",
       "Kulturmiljöplanen föreslog redan 1999 att utökad lovplikt för fasadändringar skulle införas i Ekedal och Dressyrvägen om planerna ändrades. Om det har skett beror på vilken plan som gäller för ditt hus, och det går att kontrollera i Järfällakartan eller hos kommunen. Den som vill ha ett beslut kan också söka frivilligt bygglov.",
     ],
     "aside": None},
    {"id": "brf", "h2": "Radhus i bostadsrätt",
     "paras": [
       "Enligt kulturmiljöplanen är radhusen i Bolinderbyn upplåtna med bostadsrätt. I ett bostadsrättsradhus är fasaden föreningens ansvar, och en ommålning beställs av föreningen för hela området. Som boende ansvarar du för väggar, tak och snickerier inne i lägenheten, och det är också bara det arbetet som ger dig rotavdrag.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Järfälla till",
  "steps": [
    ("Platsbesök", "Vi tittar på puts eller panel, dekorband och fönster och gör prov för att se vilken färg som sitter på."),
    ("Plan och färgskala", "Vi går igenom detaljplanen och vad kulturmiljöplanen säger om området, och föreslår kulörer för hela längan."),
    ("Skriftligt kostnadsförslag", "Tvätt, lagning, färgtyp och antal strykningar står med – per hus, så att varje ägare får sin del."),
    ("Förarbete", "Skonsam tvätt av putsen, lagning av sprickor och skrapning av panel och fönster."),
    ("Målning", "Strykningarna görs i rätt väder, med samma färgtillverkning på hela längan."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "Rotavdrag för målning i Järfälla",
  "rot": [
    "Äger du ditt radhus eller din villa räknar Skatteverket målning av fasad, fönster, väggar, tak och golv samt tapetsering som rotarbete. Målning av staket och murar ger inget avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och ROT och RUT får tillsammans vara högst 75 000 kr.",
    "När flera grannar målar samtidigt gör var och en avdraget för sitt eget hus. I bostadsrätt gäller avdraget bara arbete inne i lägenheten. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset?",
  "price": [
    "På putsade hus avgör mängden sprickor och lagningar och hur mycket dekor som ska målas för hand. På panelhus är det skrapningen och fönstren. Målar flera hus i en länga samtidigt kan ställning och etablering delas. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi måla vårt radhus i Ekedal i en annan kulör än grannarna?",
     "Det beror på detaljplanen. Kulturmiljöplanen beskriver just individuell färgsättning av husen som det som gör längorna splittrade och förordar en färgskala per länga, så stäm av med kommunen och grannarna först."),
    ("Kan spritputsen på ett kedjehus från 60-talet målas med kalkfärg?",
     "Bara om putsen tål det. Kalkfärg fäster dåligt på cementrika underlag, och många putser från den tiden innehåller cement. Ett prov visar vad som fungerar."),
    ("Vilken kulör hade husen vid Dressyrvägen från början?",
     "Enligt kulturmiljöplanen beige spritputs med dekorband i vitt. Planen rekommenderar att material och färgsättning behålls vid renoveringar."),
    ("Kan vi gå tillbaka från plåtpanel till målad träpanel i Bolinderbyn?",
     "Kulturmiljöplanen ser det som önskvärt att fasaderna återgår till stående locklistpanel eller puts. Det är en fasadrenovering och beslutas av bostadsrättsföreningen, som äger fasaderna."),
  ],
  "sources": [
    ("Järfälla kommun – Kulturmiljöplan, Jakobsberg (pdf)",
     "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4080/1550245872956/kulturmiljoplan-jakobsberg.pdf"),
    ("Järfälla kommun – Kulturmiljöplan, Kallhäll (pdf)",
     "https://www.jarfalla.se/download/18.68e7a727168e12dd179a407f/1550245859848/kulturmiljoplan-kallhall.pdf"),
    ("Järfälla kommun – Kulturmiljöplan, inledning (pdf)",
     "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4052/1550245824984/kulturmiljoplan-inledning.pdf"),
    ("Järfälla kommun – Fasadändring",
     "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/vadvilldubyggaellerandra/fasadandring.4.1966aa14175c8663c9323310.html"),
    _RAA, _BOV, _SKV, _SKV2,
  ],
  "cta": ("Radhus, kedjehus eller villa i Järfälla?", "Boka ett gratis platsbesök – gärna tillsammans med grannarna i längan."),
  "img": [
    ("Beigeputsade hus med gavlarna mot gatan i ett villaområde i Järfälla",
     "1960s Swedish suburban street with simple single-storey linked houses with attic, gable ends facing the street, plain beige rough-cast spray render facades with one thin white smooth horizontal band, small square windows, steep plain red clay tile roofs without dormers, low flat-roofed garages connecting the houses, low hedges, modest Scandinavian design, Järfälla, summer, no people"),
    ("Närbild på spritputs och slätputsat dekorband på en radhusgavel",
     "close-up of a Swedish 1960s terraced house gable with coarse rough-cast render painted light grey and a smooth rendered decorative band painted white, small hairline crack being repaired, natural daylight, no people"),
  ],
},

# ------------------------------------------------------------------ HANINGE
"malare-haninge.html": {
  "kind": "district", "service": "malare", "ort": "Haninge", "svc_label": "Målare",
  "title": "Målare i Haninge – kulörer från egnahem till Dalarö",
  "description": "Målare i Haninge: färgråd för egnahem, folkhemshus, rekordårens grupphus och sommarvillor enligt kommunens karaktärsmiljöer. Gratis platsbesök.",
  "h1": "Målare i Haninge",
  "lead": "Haninge kommun har skrivit färgråd för nästan varje sorts småhus i kommunen, från egnahemmen i Tungelsta till sommarvillorna på Dalarö. Råden gäller som vägledning även där husen inte är utpekade som särskilt värdefulla. Geal Entreprenad AB tar målningsuppdrag i hela Haninge, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Egnahem, grupphus och sommarvillor i Haninge.",
  "sections": [
    {"id": "epoker", "anchor": "Färgerna epok för epok",
     "h2": "Vad karaktärsmiljöerna säger om färg",
     "paras": [
       "Skriften Haninges karaktärsmiljöer delar in bebyggelsen i tidstypiska grupper och beskriver material och färger för var och en. Egnahemmen från 1910–1940-talen, i bland annat Tungelsta, Vendelsö och Västerhaninge, kännetecknas av träpanel, enkelt spröjsade fönster och tegeltäckta tak.",
       "Folkhemmets småhus från 1940-talet beskrivs som enkla villor i trä, puts eller tegel med färgsättning i ljusa eller mustiga kulörer. På 1950-talet kombinerades ofta rött eller gult tegel med grov spritputs eller trä i mustiga kulörer. Rekordårens grupphus från 1960–1980-talen har varierande material, men mustiga färger är vanliga, och skriften noterar att färgsättningen blev ljusare under 1980-talet när pastellfärgerna slog igenom.",
       "För sommarnöjena, med Dalarö och Smådalarö som exempel, skriver kommunen att olje- och slamfärger i ljusa och mustiga kulörer är vanliga. I de agrara miljöerna är falurött vanligast på bostadshusen, men även ljusa slam- och oljefärger förekommer.",
     ],
     "aside": {"title": "Typiska kulörer", "items": [
       "Egnahem: träpanel, spröjsade fönster", "1950-tal: tegel och spritputs, mustiga kulörer",
       "1980-tal: ljusare pasteller", "Sommarvillor: olje- och slamfärg"]}},
    {"id": "omvandling", "h2": "Fritidshus som blir helårshus: undvik vitt",
     "paras": [
       "I områden där sommarstugor permanentas, som Hermanstorp, Norrby och Kolartorp, beskriver kommunen en blandning av gamla gårdar, sommarbostäder och nya typhus i kuperad terräng med mycket barr- och lövträd. Råden för de områdena är ovanligt raka: undvik fasadkulörer i vita nyanser, välj gärna rött, brunt, grönt eller gult.",
       "För gårdarna på landsbygden skriver kommunen att en tillbyggnad ska anpassas i färg och form till den ursprungliga volymen, och för sommarvillornas panelarkitektur att tillbyggnader ska utföras i samma arkitektoniska utformning som huset. För den som både bygger till och målar om är det enklast att bestämma kulören för hela huset innan arbetet börjar, så att gammal och ny panel får samma behandling. Mer om själva tillbyggnaden finns under " + _L.format("tillbyggnad.html", "tillbyggnad") + ".",
     ],
     "aside": None},
    {"id": "detaljer", "h2": "Fönster, dörrar och fasadmaterial",
     "paras": [
       "För folkhemmets hus skriver kommunen att dörrar och fönster är en bärande del av byggnadens karaktär och att ursprunglig utformning och färgsättning ska värnas och vara utgångspunkt vid förändring. Det betyder att foder och bågar i originalkulör är värda att behålla även när fasaden i övrigt får ny färg.",
       "Skriften varnar också för fasadändringar som avviker från husets ursprungliga utformning, och ger exemplet att en fasad i tegel inte ska putsas. Samma logik gäller målning: ett rött eller gult fasadtegel som inte har målats tidigare bör helst få förbli omålat, medan putspartierna och träet bredvid underhålls.",
       "Riksantikvarieämbetet påpekar att fönster, vattbräder, trappor och räcken är byggnadsdelar som bör underhållsmålas löpande, eftersom de tar mest väder och skadas fort om målningen släpper. Är fönstren för dåliga för att renoveras, se " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
    {"id": "lov-haninge", "h2": "När ny kulör kräver lov i Haninge",
     "paras": [
       "Sedan 1 december 2025 krävs normalt inget bygglov för att byta kulör på ett en- eller tvåbostadshus, enligt Boverket. Haninge kommun skriver att skärpta krav gäller i särskilt värdefulla områden och i riksintressen för kulturmiljövården, och att ändringar alltid ska göras varsamt. Kommunen uppdaterar sitt digitala kartskikt över särskilt värdefulla kulturmiljöer, och tills det är klart kan bygglovsenheten svara på om en fastighet berörs.",
       "Dalarö–Jutholmen–Dalarö skans är riksintresse för kulturmiljövården, med sommarvillorna från slutet av 1800-talet som en del av motiveringen. Där kan detaljplanen för den enskilda fastigheten ha egna bestämmelser, så den behöver läsas först. Kommunen påminner om att all bebyggelse omfattas av hänsyns- och varsamhetskraven i plan- och bygglagen, oavsett om karaktärsmiljöerna är juridiskt bindande eller inte.",
     ],
     "aside": {"title": "Kontrollera före ny kulör", "items": [
       "Kommunens kartskikt över värdefulla miljöer", "Detaljplanen för fastigheten",
       "Riksintresset på Dalarö", "Karaktärsmiljöernas råd för epoken"]}},
    {"id": "skargard", "h2": "Skärgårdsläge och skog",
     "paras": [
       "Dalarö ligger vid inloppet till Stockholm och tar vind från öppet vatten. Östersjön är bräckt, enligt SMHI med 6–9 gram salt per kilo i Egentliga Östersjön, men regn och blåst räcker för att en fasad mot sjön ska slitas betydligt fortare än en mot skogen. I omvandlingsområdena står husen i stället tätt inpå träden, där fasaderna torkar långsamt och får påväxt som måste tvättas bort före målning.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Haninge till",
  "steps": [
    ("Platsbesök", "Vi tittar på fasadmaterial, fönster och snickerier och gör skrapprov för att se vilken färg som sitter på."),
    ("Epok och regler", "Vi går igenom vad karaktärsmiljöerna säger om husets tid och om fastigheten berörs av skärpta krav."),
    ("Skriftligt kostnadsförslag", "Underarbete, färgtyp och antal strykningar specificeras, och tillbyggnader räknas in."),
    ("Förarbete", "Tvätt av påväxt, skrapning, lagning av trä och kittning av fönster."),
    ("Målning", "Strykningarna görs i lämpligt väder och med de torktider färgtypen kräver."),
    ("Genomgång", "Vi går igenom fasaden tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "Rotavdrag för målning i Haninge",
  "rot": [
    "Skatteverket räknar målning av fasader, fönster, väggar, tak och golv samt tapetsering som rotarbete i småhus, men inte målning av staket och murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och ROT och RUT får sammanlagt vara högst 75 000 kr.",
    "Ett fritidshus du själv äger kan också ge rotavdrag. Färgen och övrigt material ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden?",
  "price": [
    "Kostnaden beror på hur mycket som måste skrapas och lagas, hur många fönster och detaljer som ingår och hur högt huset är. På sommarvillor med rika snickerier och glasverandor tar detaljerna mest tid, på grupphus är det fasadytan. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför avråder Haninge kommun från vita fasader i fritidshusområdena?",
     "Kommunens karaktärsmiljöer beskriver områdena i omvandling som skogs- och naturnära, och råden säger att vita nyanser bör undvikas. Rött, brunt, grönt och gult passar bättre in i den miljön."),
    ("Ska tegelfasaden på vår 50-talsvilla i Handen målas?",
     "Helst inte. Kommunen varnar för fasadändringar som avviker från husets ursprungliga utformning, och ett omålat fasadtegel är en del av karaktären. Puts- och trädelarna intill kan målas."),
    ("Vilken färgtyp passar en sommarvilla på Dalarö?",
     "Kommunen skriver att olje- och slamfärger i ljusa och mustiga kulörer är vanliga i sommarnöjesmiljöerna. Skrapprov visar vad huset har i dag, och i riksintresset bör kulörbyte stämmas av med kommunen."),
    ("Behöver tillbyggnaden på vår stuga i Haninge ha samma färg som stugan?",
     "Kommunens karaktärsmiljöer säger för både gårdar och sommarvillor att tillbyggnader ska anpassas till det befintliga huset. Därför är det naturligt att måla gammal och ny del i samma kulör."),
  ],
  "sources": [
    ("Haninge kommun – Haninges karaktärsmiljöer (pdf)",
     "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf"),
    ("Haninge kommun – Fasadändring",
     "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/fasadandring/"),
    ("Haninge kommun – Antikvarisk förundersökning, Dalarö 3:4 Hotell Bellevue (pdf)",
     "https://www.haninge.se/siteassets/bygga-bo-och-miljo/oversiktsplanering-och-detaljplaner/detaljplaner/kust-och-skargard/dalaro-34-hotell-bellevue/antikvarisk-forundersokning.pdf"),
    _SMHI, _RAA, _BOV, _SKV, _SKV2,
  ],
  "cta": ("Ska huset i Haninge målas om?", "Boka ett gratis platsbesök så går vi igenom husets epok, färgtyp och kulör på plats."),
  "img": [
    ("Nymålad gul sommarvilla med veranda och vita snickerier på Dalarö",
     "late 1800s Swedish wooden summer villa with ornate carpentry and a glazed veranda, freshly painted pale yellow facade with white trim, on a hill above a calm archipelago bay, Dalarö Haninge, summer, no people"),
    ("Villa i gult fasadtegel med mörka fönsterbågar i Haninge",
     "1950s Swedish two-storey villa combining yellow facing brick with rough-cast render painted in a deep ochre tone, dark window frames, low hedge, birch trees, Handen Haninge, no people"),
  ],
},

# ------------------------------------------------------------------ TYRESÖ
"malare-tyreso.html": {
  "kind": "district", "service": "malare", "ort": "Tyresö", "svc_label": "Målare",
  "title": "Målare i Tyresö – rödfärgade hus och äldre interiörer",
  "description": "Målare i Tyresö: rödfärgad panel med vita detaljer, ommålning inomhus i äldre hus, lov i kulturhistoriskt värdefulla områden. Gratis platsbesök.",
  "h1": "Målare i Tyresö",
  "lead": "Rött och vitt går igen i Tyresös äldre hus, från gårdarna och kvarnmiljön vid Uddbykvarn till 1950-talets fritidshus. Inomhus kan samma hus ha färglager som är lika värda att spara som fasaden. Geal Entreprenad AB tar målningsuppdrag ute och inne i hela kommunen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Rödfärgade hus, stugor och interiörer i Tyresö.",
  "sections": [
    {"id": "rodfarg", "anchor": "Rött och vitt",
     "h2": "Rödfärgad locklistpanel med vita foder",
     "paras": [
       "Stockholms läns museum inventerade 2008 bebyggelsen i Solberga och delar av Raksta inför detaljplaneläggning. Rapporten beskriver hus efter hus med rödfärgad locklistpanel och vitmålade knutar, lister, fönster och foder. Byggnaden som kallas Telegrafen vid Uddbykvarn, ett timmerhus från tidigt 1800-tal, har just den kombinationen, liksom flera av gårdarnas bostadshus och uthus.",
       "Även 1950-talets fritidshus finns med. Ett välbevarat exempel beskrivs med röd stockpanel, gröna lister och foder och tvåkupigt tegeltak. Samtidigt konstaterar rapporten att permanentningen pågår och att en del hus är helt ombyggda eller nybyggda.",
       "För flera av de äldre byggnaderna föreslår museet skyddsbestämmelser som omfattar fasad- och takmaterial och uttryckligen den röda färgsättningen. Det säger något om hur tungt kulören väger i den här miljön.",
     ],
     "aside": {"title": "Vanligt i de äldre husen", "items": [
       "Rödfärgad locklistpanel", "Vitmålade knutar, foder och fönster", "Dubbla vindskivor, vita eller svarta",
       "Röd stockpanel på 50-talsstugor"]}},
    {"id": "slamfarg", "h2": "Rödfärg som ska förbli rödfärg",
     "paras": [
       "Riksantikvarieämbetet beskriver röd slamfärg som en matt, fuktöppen färg som är lätt att underhålla: det räcker ofta att borsta bort lös färg och stryka på nytt. Men myndigheten är lika tydlig med begränsningen. En slamfärgsmålad yta ska bara målas om med slamfärg, och har man en gång bytt till exempelvis latex-, alkyd- eller linoljefärg går det inte att återvända, även om den gamla färgen tas bort.",
       "Har slamfärgen tidigare blandats med trätjära behöver tillsatsen normalt finnas med även vid ommålningen, annars blir vidhäftningen och kulören ojämn. De vita fodren och fönstren är däremot ofta målade med linoljefärg eller en modern täckfärg, och de behöver sin egen förbehandling.",
       "Säsongen spelar också roll. Riksantikvarieämbetet anger april till september som period för utomhusmålning i Mellansverige, och för linoljefärg maj till augusti, med torrt trä och utan direkt solsken på den yta som målas. Ett hus i skuggigt läge under tallar behöver därför planeras in när veckorna är torra, inte bara när ställningen är ledig.",
     ],
     "aside": None},
    {"id": "inne", "h2": "Inomhus: tvätta för gott innan du målar över",
     "paras": [
       "När Solberga gård renoverades till permanentstandard bevarades äldre material inne, foder och lister kompletterades med samma utseende som de befintliga och den äldre färgsättningen togs fram, enligt museets rapport. Det är ett bra exempel på att ett äldre hus kan få modern standard utan att interiören målas över.",
       "Riksantikvarieämbetet skriver att det inte alltid är nödvändigt att måla om helt. Är ytorna i gott skick frånsett mindre skador och smuts räcker det ofta att tvätta för gott, alltså rengöra milt och bättra skadorna med samma färgtyp. Metoden är enligt myndigheten ofta billigare, ger ett resultat som är lättare att renovera och sparar äldre målerihantverk.",
       "I äldre hus kan taken vara målade med limfärg, som var vanlig som takfärg fram till 1950-talet. Limfärg är känslig för fukt och passar inte i kök eller badrum, och den ska i första hand målas om med limfärg. Ska huset samtidigt byggas om invändigt kan målningen ingå i en " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": {"title": "Tecken på äldre färgtyper inne", "items": [
       "Matt tak som kritar av sig", "Snickerier med många oljefärgslager", "Pärlspont och bröstpanel",
       "Matta, vita spisar och murar"]}},
    {"id": "lov-tyreso", "h2": "Lov för ny kulör i Tyresö",
     "paras": [
       "Tyresö kommun skriver att ommålning, nytt tak eller nya fönster på ett en- eller tvåbostadshus inte kräver bygglov, men att ändringar alltid ska göras varsamt och anpassas till byggnadens värden. Lov krävs alltid om fastigheten ligger i ett kulturhistoriskt särskilt värdefullt område eller om byggnaden själv är kulturhistoriskt särskilt värdefull. Sådana områden kan vara utpekade i översiktsplanen, kulturmiljöprogrammet eller detaljplanen.",
       "Tyresö slott med omgivning är riksintresse för kulturmiljövården, och delar av Solberga och Raksta ligger nära. Ska ett rödfärgat hus där få en annan kulör är det klokt att fråga kommunen först. Byggs en gammal stuga till, se " + _L.format("snickare-tyreso.html", "snickare i Tyresö") + " för hur till- och ombyggnaden kan planeras.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Tyresö till",
  "steps": [
    ("Platsbesök", "Vi tittar på fasad och interiör och gör prov för att se om det är slamfärg, oljefärg, limfärg eller modern färg."),
    ("Kulör och regler", "Vi stämmer av om huset ligger i ett kulturhistoriskt värdefullt område och vilken färgsättning det hade."),
    ("Skriftligt kostnadsförslag", "Arbete ute och inne specificeras för sig, med färgtyp, underarbete och antal strykningar."),
    ("Förarbete", "Borstning eller skrapning ute, mild rengöring och bättring inne där det räcker."),
    ("Målning", "Färgen stryks i den ordning och med de torktider färgtypen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "Rotavdrag för målning i Tyresö",
  "rot": [
    "Skatteverket ger rotavdrag för målning och tapetsering inomhus och för målning av fasader och fönster på ett småhus, men inte för målning av staket och murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och tillsammans med rutavdrag högst 75 000 kr. Färgen är material och ingår inte.",
    "Bor du i bostadsrätt gäller avdraget bara arbete inne i lägenheten. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset?",
  "price": [
    "Utomhus styrs kostnaden av hur mycket lös färg som måste bort, hur mycket panel som behöver bytas och hur många fönster och foder som ska målas i en annan färgtyp än fasaden. Inomhus är det skillnad på att bättra och att måla om helt. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi måla vårt gamla rödfärgade hus i Solberga med vanlig täckfärg?",
     "Tekniskt går det, men Riksantikvarieämbetet avråder eftersom man inte kan återgå till slamfärg efteråt. Museets rapport föreslår dessutom skydd för den röda färgsättningen på flera av de äldre husen."),
    ("Måste hela köket målas om, eller kan de gamla luckorna bara bättras?",
     "Är färgen hel kan det räcka att rengöra milt och bättra skadorna med samma färgtyp. Riksantikvarieämbetet beskriver det som ofta billigare och lättare att underhålla."),
    ("Hur vet man om taket i en äldre villa i Tyresö är målat med limfärg?",
     "Limfärg är matt och kritar ofta av sig när man stryker med handen. Ett prov med en fuktig trasa ger en första fingervisning innan ny färg väljs."),
    ("Gäller lovplikten för ny kulör nära Tyresö slott?",
     "Tyresö slott med omgivning är riksintresse för kulturmiljövården, och kommunen kräver alltid lov i kulturhistoriskt särskilt värdefulla områden. Fråga kommunen innan kulören ändras."),
  ],
  "sources": [
    ("Tyresö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
     "https://www.tyreso.se/boende--miljo/bygga/bygga-riva-eller-andra/forandringar-i-plan--och-bygglagen-fran-1-december-2025.html"),
    ("Stockholms läns museum – Solberga/del av Raksta, kulturmiljöunderlag inför detaljplaneläggning (rapport 2008:31)",
     "https://insynsverige.se/documentHandler.ashx?did=20437"),
    _RAA, _BOV, _SKV, _SKV2,
  ],
  "cta": ("Ska huset i Tyresö målas, ute eller inne?", "Boka ett gratis platsbesök så går vi igenom färgtyper och kulörer på plats."),
  "img": [
    ("Rödfärgat trähus med vita knutar och fönsterfoder bland tallar i Tyresö",
     "old Swedish two-storey timber house clad with falu red vertical board-and-batten panelling, white painted corners, window frames and trim, red clay tile roof, pine trees on rocky ground near a stream, Tyresö, summer, no people"),
    ("Äldre rum med pärlspontpanel, vitmålade foder och matt tak i ett hus i Tyresö",
     "interior of an old Swedish wooden house: room with beadboard wainscot, white painted door and window architraves, matt off-white ceiling, wide pine floorboards, soft daylight through a small-paned window, no people"),
  ],
},

# ------------------------------------------------------------------ VÄRMDÖ
"malare-varmdo.html": {
  "kind": "district", "service": "malare", "ort": "Värmdö", "svc_label": "Målare",
  "title": "Målare på Värmdö – skärgårdshus och bruksgator",
  "description": "Målare på Värmdö: fasader i vind och sol vid fjärdarna, faluröd fjällpanel i Gustavsberg och lov för ommålning i kulturmiljöer. Gratis platsbesök.",
  "h1": "Målare på Värmdö",
  "lead": "På Värmdö slits en fasad ojämnt. Sidan mot fjärden får sol, regn och blåst, medan sidan mot skogen står fuktig i skugga. I Gustavsberg tillkommer bruksgatornas enhetliga kulörer. Geal Entreprenad AB tar målningsuppdrag på hela Värmdö, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Skärgårdshus, fritidshus och bruksmiljö på Värmdö.",
  "sections": [
    {"id": "lage", "anchor": "Skärgårdsläget",
     "h2": "Varje fasad har sitt eget väder",
     "paras": [
       "Många hus på Värmdö står på uddar, öar och berg vid öppet vatten. Vattnet är bräckt – enligt SMHI 6–9 gram salt per kilo i Egentliga Östersjön – men det är vind, regn och sol från öppet vatten som sliter mest på en målad fasad. Riksantikvarieämbetet skriver att söderfasader behöver målas om oftare än norrfasader och att fönster, vattbräder, trappor och räcken bör underhållsmålas löpande, eftersom de är hårdast utsatta.",
       "På ett hus i skogen eller i en nordsluttning är problemet i stället påväxt. Där står fasaden fuktig länge efter regn och behöver tvättas och få torka ordentligt innan den målas. Myndigheten noterar att zinkvitt i linoljefärg har en mögelhämmande effekt, och att en mindre mängd bör ingå i all linoljefärg för utomhusbruk.",
       "Därför delas arbetet ofta upp. Mot vattnet kan det vara dags för en hel ommålning, medan skogssidan klarar sig med tvätt och bättring några år till. Myndigheten beskriver just bättringsmåleri som lämpligt även utomhus, eftersom olika byggnadsdelar slits olika fort.",
     ],
     "aside": {"title": "Slits först", "items": [
       "Söder- och sjöfasader", "Fönsterbågar och vattbräder", "Trappor, räcken och altanstolpar",
       "Vindskivor på hus i öppna lägen"]}},
    {"id": "gustavsberg", "h2": "Gustavsberg: faluröd fjällpanel och vita knutar",
     "paras": [
       "Gustavsberg är riksintresse för kulturmiljövården. Bland det som pekas ut finns bruksgatorna från 1800-talets senare hälft och bostadshusens enhetliga volymer, material och färgsättning inom varje bebyggelsegrupp. En antikvarisk konsekvensanalys som kommunen lät göra 2023 beskriver Grindstugatan som ett representativt exempel: de flesta husen är från 1870-talet och har sadeltak, faluröda fasader med fjällpanel och vita knutar.",
       "Analysen återger också hur en äldre detaljplan skyddar en byggnad i området, där underhåll ska ske med ursprungliga material och kulörer. Det visar vad som väger tungt här. En ny kulör på ett hus längs bruksgatorna bryter mot hela gatans bild, även om ändringen i sig ser liten ut.",
       "Riksantikvarieämbetet påpekar att ljusa slamfärger varken visuellt eller tekniskt är lika tåliga som mörkare, och att en slamfärgsmålad yta bara ska målas om med slamfärg. På de faluröda husen är det alltså oftast både kulören och färgtypen som bör behållas.",
     ],
     "aside": None},
    {"id": "lov-varmdo", "h2": "Ommålning och lov i Värmdö kommun",
     "paras": [
       "Värmdö kommun skriver att det inte krävs bygglov för fasadändring, nytt tak eller nya fönster på en- och tvåbostadshus. Men om fastigheten ligger i ett kulturhistoriskt särskilt värdefullt område eller om byggnaden själv är särskilt värdefull krävs alltid bygglov för fasadändringar som ommålning. Enligt kommunens sida om ändringarna i plan- och bygglagen gäller lovplikten också inom riksintressen för kulturmiljövården, och kulturmiljökartan visar vilka fastigheter som berörs.",
       "Plan- och bygglagen ställer dessutom krav på alla hus. Ett byggnadsverk ska hållas i vårdat skick och underhållet ska anpassas till omgivningens karaktär och byggnadens värden. Ändringar ska göras varsamt, med hänsyn till husets karaktärsdrag. För en målare innebär det att börja med vad huset redan har, inte med en ny färgkarta.",
     ],
     "aside": {"title": "Lov krävs för ommålning om", "items": [
       "Huset ligger i riksintresset Gustavsberg", "Området är kulturhistoriskt särskilt värdefullt",
       "Byggnaden själv är särskilt värdefull", "Detaljplanen har utökad lovplikt"]}},
    {"id": "fritidshus", "h2": "Fritidshus som blir helårshus",
     "paras": [
       "Kommunen har tusentals fritidshusfastigheter där allt fler bor permanent, och de första områdena som ska anpassas för helårsboende får detaljplan och kommunalt vatten och avlopp. När ett sådant hus byggs till eller tilläggsisoleras får det ofta ny panel på en del av fasaden, medan resten har decennier av färglager.",
       "Då lönar det sig att måla hela huset i samma omgång, med samma färgtyp på gammal och ny panel. Ny obehandlad panel behöver grundas ordentligt, och den äldre delen kan behöva skrapas ner till fast underlag. Mer om ombyggnaden finns under " + _L.format("tillbyggnad.html", "tillbyggnad") + ", och för takets del hos " + _L.format("takrenovering-varmdo.html", "takrenovering på Värmdö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning på Värmdö till",
  "steps": [
    ("Platsbesök", "Vi går runt huset, bedömer varje fasad för sig och gör skrapprov för att se vilken färgtyp som sitter på."),
    ("Kulturmiljö och plan", "Vi kontrollerar kulturmiljökartan och detaljplanen om kulören ska ändras."),
    ("Skriftligt kostnadsförslag", "Hel ommålning och bättring prissätts per fasad, så att du kan välja vad som görs nu."),
    ("Förarbete", "Tvätt av påväxt, skrapning, byte av skadat trä och kittning av fönster."),
    ("Målning", "Strykningarna görs under säsongen och i torrt väder, med de torktider färgtypen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "Rotavdrag för målning på Värmdö",
  "rot": [
    "Rotavdraget gäller både för permanentbostad och för fritidshus som du äger. Skatteverket räknar målning av fasader, fönster, väggar, tak och golv samt tapetsering som rotarbete, men inte målning av staket och murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och ROT och RUT får tillsammans vara högst 75 000 kr.",
    "Färgen räknas som material och ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset?",
  "price": [
    "Priset styrs av hur många fasader som behöver en hel ommålning, hur mycket lös färg och påväxt som måste bort och hur mycket trä som behöver bytas. Hus på berg och uddar kan kräva mer ställning, och öar utan bilväg kräver transport av material. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför flagnar färgen fortare på sjösidan av vårt hus på Värmdö?",
     "Sol, regn och vind från öppet vatten sliter mest. Riksantikvarieämbetet skriver att söderfasader behöver målas om oftare än norrfasader, och på ett hus vid fjärden gäller det även sidan mot vattnet."),
    ("Får vi måla vårt hus på Grindstugatan i Gustavsberg i en annan färg än falurött?",
     "Gustavsberg är riksintresse för kulturmiljövården och kommunen kräver lov för ommålning där. Bruksgatornas enhetliga färgsättning pekas ut som en del av riksintresset, så räkna med att en ny kulör prövas noga."),
    ("Räcker det att måla de utsatta sidorna av fritidshuset?",
     "Ofta ja. Är skogssidan i bra skick kan den tvättas och bättras, medan söder- och sjösidan får en hel ommålning. Kostnadsförslaget kan delas upp per fasad."),
    ("Ska ny och gammal panel målas samtidigt när stugan byggs till?",
     "Det är oftast bäst. Då får båda delarna samma färgtyp och kulör, och ställningen behöver bara resas en gång."),
  ],
  "sources": [
    ("Värmdö kommun – Bygglov vid fasadändring",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/bygglovvidfasadandring.4.1a14d9c818e5a4c406a626d.html"),
    ("Värmdö kommun – Förändringar i PBL från 1 december 2025",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/forandringaripblfrom1december2025.4.18b9914519a768a188a2872.html"),
    ("Värmdö kommun – Antikvarisk konsekvensanalys, riksintresset Gustavsberg (2023, pdf)",
     "https://varmdo.se/download/18.3dd2ab3d18c629ae56f50ed/1702902627509/Antikvarisk%20konsekvensanalys%20AIX%202023-09-27.pdf"),
    ("Värmdö kommun – Fritidshusområde i förändring, del 1 Planering (2023, pdf)",
     "https://www.varmdo.se/download/18.52346f71869c9938611c2df/1678200543391/Broschyr%20PFO%20del%201%20-%20uppdaterad%202023.pdf"),
    _PBL, _SMHI, _RAA, _BOV, _SKV, _SKV2,
  ],
  "cta": ("Ska huset på Värmdö målas om?", "Boka ett gratis platsbesök så går vi igenom varje fasad och vad den behöver."),
  "img": [
    ("Nymålat rött skärgårdshus med vita knutar på en klippa vid en fjärd på Värmdö",
     "freshly painted falu red wooden archipelago house with white corner boards and window frames on smooth granite rocks by a wide Baltic bay, windswept pine trees, Värmdö Stockholm archipelago, summer, no people"),
    ("Faluröda trähus med liggande panel längs en bruksgata i Gustavsberg",
     "row of small 1870s Swedish workers' houses with falu red horizontal shiplap siding, white corner boards, gable roofs, hedges and gardens along a narrow tree-lined street, Gustavsberg Värmdö, summer, no people"),
  ],
},
}
