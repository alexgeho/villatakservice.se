# -*- coding: utf-8 -*-
"""Tjänstehubbar golvlaggning.html och snickare.html (tjänster v1, 2026-10-25).
Fakta kontrollerade mot källorna i "sources" (sidor som faktiskt öppnats 2026-10-25):
Skatteverket (rotarbeten per boendeform, 30 %/50 000/75 000 kr), Golvbranschen (RF i
underlag, fuktmätning), Byggkeramikrådet (golvvärme under plattor), Boverket (PBL-ändringar
1 december 2025: altan, tillbyggnad, komplementbyggnad/komplementbostadshus, bärande delar),
riksdagen.se (bostadsrättslagen 7 kap. 7 §). Inga priser, garantier, omdömen, case eller cert.
Strukna (ej verifierade): hur många gånger ett golv kan slipas, kritiska RF-värden per
golvtyp, stegljudskrav i flerbostadshus."""

SKV_ROT = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
           "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
SKV_SA = ("Skatteverket – Så fungerar rotavdraget",
          "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
BRL = ("Riksdagen – Bostadsrättslag (1991:614)",
       "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")

PAGES_TJ = {
"golvlaggning.html": {
  "kind": "hub", "service": "golvlaggning", "svc_label": "Golvläggning",
  "title": "Golvläggning i Stockholm – parkett, trägolv och slipning",
  "description": "Golvläggning i Stockholm: parkett, massivt trägolv, laminat och klinker, "
                 "undergolv och fukt i betong, golvslipning med lack eller olja. ROT på arbetet.",
  "h1": "Golvläggning i Stockholm",
  "lead": "Vi lägger parkett, massiva trägolv, laminat och klinker i villor och lägenheter i hela "
          "Stockholm, och vi slipar och behandlar gamla trägolv. Före varje golv kontrollerar vi "
          "underlaget, eftersom ett ojämnt eller fuktigt undergolv är den vanligaste orsaken till "
          "att ett nytt golv knarrar, glipar eller buktar.",
  "card": "Parkett, trägolv, klinker och slipning.",
  "sections": [
    {"id": "golvtyper", "anchor": "Golvtyper",
     "h2": "Parkett, massivt trä, laminat eller klinker",
     "paras": [
       "Valet av golv handlar mer om rummet än om smak. I hall och kök slits golvet av grus, "
       "väta och stolsben, i sovrum knappt alls. Ett golv som ska tåla många år i en hall behöver "
       "därför en tåligare yta än ett golv i ett gästrum, och det påverkar både material och "
       "ytbehandling.",
       "Flerskiktsparkett har ett tunt toppskikt av ädelträ på en stomme av barrträ eller "
       "fiberskiva. Den läggs ofta flytande på en underlagsduk och går snabbt att få på plats. "
       "Massiva plankgolv av ek, ask eller furu spikas eller limmas och kan slipas ned genom en "
       "större del av tjockleken. Laminat är en tryckt yta på en fiberskiva, tåligt mot repor men "
       "inte möjligt att slipa om. Klinker passar i hall, kök och tvättstuga, där vatten och smuts "
       "kommer in.",
       "Under klinker med golvvärme gäller särskilda regler. Byggkeramikrådet anger i sina "
       "<a class=\"text-link\" href=\"https://www.bkr.se/vanliga-fragor\" rel=\"noopener\">svar "
       "på vanliga frågor</a> att golvvärmen inte får slås på förrän tidigast 28 dygn efter "
       "plattsättningen, att temperaturen ska höjas långsamt och att ytskiktet inte får bli "
       "varmare än 27 °C. Ska golvet ligga i ett badrum blir det ett våtrumsjobb med tätskikt – "
       "läs mer om <a class=\"text-link\" href=\"badrumsrenovering.html\">badrumsrenovering</a>."],
     "aside": {"title": "Det här bestämmer golvvalet",
               "items": ["Hur hårt rummet slits",
                         "Om rummet kan bli blött",
                         "Undergolv av trä eller betong",
                         "Golvvärme eller inte",
                         "Om golvet ska kunna slipas om senare"]}},
    {"id": "underlag",
     "h2": "Undergolvet bestämmer hur det nya golvet beter sig",
     "paras": [
       "I äldre villor ligger golvet ofta på träreglar och golvspånskiva eller råspont, och med "
       "åren har bjälklaget satt sig. Där riktar vi upp, skruvar fast lösa skivor som knarrar och "
       "byter delar som har blivit mjuka. På betong eller gamla klinkergolv jämnar vi ut svackor "
       "med avjämningsmassa innan ytskiktet läggs, så att skarvarna i ett flytande golv inte "
       "glipar.",
       "Betong är det känsliga fallet. Golvbranschen skriver i sin text om "
       "<a class=\"text-link\" href=\"https://www.golvbranschen.se/teknik--material/golvavjamning/uttorkning-av-golvavjamning/\" "
       "rel=\"noopener\">uttorkning av golvavjämning</a> att trä tar upp fukt ur omgivningen och "
       "sväller när den relativa fuktigheten är hög, och att betongens fuktnivå bör kontrolleras "
       "innan avjämningen läggs. Kräver ytskiktet till exempel högst 85 procent RF, får betongen "
       "under inte ligga över den nivån.",
       "Branschens limrekommendationer säger att en korrekt RF-mätning i underlaget görs av en "
       "fuktkontrollant med auktorisation från RBK. Fukt som stängs in mellan betong och golv "
       "kan bryta ned lim och golvmaterial och ge emissioner till inomhusluften. På en källare, "
       "en ny platta eller ett golv som har haft en vattenskada föreslår vi därför en mätning "
       "innan vi beställer material, och vi följer materialleverantörens anvisningar för lim "
       "och fuktspärr."],
     "aside": {"title": "Vanliga åtgärder före läggning",
               "items": ["Rivning och bortforsling av gammalt golv",
                         "Uppriktning av träbjälklag",
                         "Avjämning av betong",
                         "Fuktmätning på betong",
                         "Byte av trösklar och golvlister"]}},
    {"id": "slipning",
     "h2": "Golvslipning: slipa och lacka, olja eller såpa trägolvet",
     "paras": [
       "Ett massivt trägolv eller en parkett med tjockt slitskikt behöver sällan bytas. Repor, "
       "gråa gångstråk och gammal gulnad lack slipas bort med maskin i flera steg, från grovt "
       "till fint papper, och kanter och hörn tas med kantslip. Djupa hack, lösa stavar och "
       "springor åtgärdas innan finslipningen.",
       "Hur mycket som går att slipa beror på hur tjockt träet är ovanför spontens överkant. Vi "
       "lyfter en tröskel eller en golvlist och mäter innan vi lovar något. Är slitskiktet för "
       "tunt eller golvet av laminat, är ett nytt golv rätt väg i stället för en slipning.",
       "Efter slipningen väljer du yta. Lack lägger en hård film ovanpå träet som tål hårt slitage "
       "och lätt går att torka av. Olja tränger in i träet, ger en mattare yta och fräschas upp "
       "med ny olja där det slits, utan ny slipning. Såpa är den traditionella behandlingen på "
       "furugolv och kräver regelbunden såpskurning. Kulör kan läggas till, till exempel vitpigment "
       "på ek eller furu."],
     "aside": {"title": "Ytbehandlingar",
               "items": ["Lack – tålig film, lättstädat",
                         "Olja – matt yta, punktvis underhåll",
                         "Såpa – traditionellt på furu",
                         "Pigment – ljusare eller tonad ton"]}},
    {"id": "bostadsratt",
     "h2": "Nytt golv i bostadsrätt eller villa",
     "paras": [
       "I en bostadsrätt står du själv för golvet i lägenheten, men bostadsrättslagens 7 kap. 7 § "
       "kräver styrelsens tillstånd för ingrepp i bärande konstruktion, ändring av ledningar för "
       "vatten, avlopp eller värme och andra väsentliga förändringar av lägenheten. Ett nytt "
       "parkettgolv brukar inte vara något av det, men golvvärme med vattenburen slinga eller "
       "ett golv där bjälklaget ska förstärkas eller ändras kan vara det. Läs föreningens stadgar och fråga "
       "styrelsen om den har egna krav på underlag och ljuddämpning.",
       "I en villa är golvet oftast en del av ett större jobb, till exempel när en planlösning "
       "öppnas upp eller hela huset renoveras. Då samordnar vi golvet med övriga moment inom "
       "<a class=\"text-link\" href=\"villarenovering.html\">villarenovering</a>, så att golvet "
       "läggs sist, efter målning och snickerier, och inte skadas under resten av bygget."],
     "aside": None},
  ],
  "steps_h2": "Så går golvjobbet till",
  "steps": [
    ("Platsbesök", "Vi tittar på rummen, mäter ytorna och kontrollerar undergolv, trösklar och eventuellt slitskikt."),
    ("Skriftligt kostnadsförslag", "Du får ett förslag där arbete och material står var för sig, med de förarbeten som behövs."),
    ("Förberedelse", "Möbler flyttas, gammalt golv rivs och undergolvet riktas upp eller jämnas ut. På betong mäts fukten vid behov."),
    ("Läggning eller slipning", "Golvet läggs, spikas eller limmas, eller så slipas det befintliga golvet i flera steg."),
    ("Ytbehandling och lister", "Lack, olja eller såpa läggs på, och golvlister och trösklar monteras."),
    ("Genomgång", "Vi går igenom golvet med dig och berättar hur ytan ska skötas."),
  ],
  "rot_h2": "ROT-avdrag för golvläggning och golvslipning",
  "rot": [
    "Att slipa och byta golv finns med bland Skatteverkets exempel på rotarbeten, både i småhus "
    "och i bostadsrätt. Det gör också att sätta klinker och att måla golv. I ett småhus räknas "
    "dessutom en förbättring som att byta plastmatta mot trägolv.",
    "Avdraget är 30 procent av arbetskostnaden och gäller bara arbetet, inte golvmaterial, lim "
    "eller resor. Varje person kan få högst 50 000 kronor i rotavdrag per år, och rot och rut "
    "får tillsammans uppgå till högst 75 000 kronor. Vi drar avdraget direkt på fakturan. Vid "
    "en slipning är nästan allt arbete, medan materialet väger tyngre när ett nytt golv läggs."],
  "price_h2": "Vad påverkar priset på ett nytt eller slipat golv?",
  "price": [
    "Antalet kvadratmeter är bara en del av kostnaden. Lika viktigt är hur mycket undergolvet "
    "behöver riktas eller jämnas ut, om gammalt golv ska rivas och forslas bort, hur många "
    "trösklar och dörrkarmar golvet ska passa mot, och vilket material du väljer. Vid slipning "
    "styr golvets skick, antalet skador som ska lagas och vald ytbehandling.",
    "Därför börjar vi med ett gratis platsbesök. Efter besöket får du ett skriftligt "
    "kostnadsförslag med arbete och material var för sig, så att du ser vad ROT-avdraget "
    "gäller."],
  "faq": [
    ("Kan man lägga nytt golv ovanpå det gamla?",
     "Ofta går det med ett flytande golv, om det gamla är plant, fast och torrt. Golvet blir "
     "högre, så trösklar och dörrar kan behöva kortas. Mjuka plastmattor och golv som rör sig "
     "tas hellre bort först."),
    ("Ska jag lacka eller olja mitt slipade trägolv?",
     "Lack ger en tålig yta som är lätt att torka av och passar i kök och hall. Olja ger en "
     "mattare och varmare yta som kan bättras punktvis, men den behöver ny olja med jämna "
     "mellanrum."),
    ("Hur vet jag om min parkett går att slipa?",
     "Det avgörs av slitskiktet, alltså hur tjockt träet är ovanför sponten. Vi lyfter en "
     "tröskel eller list och mäter vid besöket."),
    ("Varför behöver betongen fuktmätas innan golvet läggs?",
     "Fukt som stängs in under golvet kan få trä att svälla och bryta ned lim. Golvbranschen "
     "hänvisar till fuktkontrollanter med auktorisation från RBK för en korrekt mätning."),
    ("Behöver jag fråga föreningen innan jag byter golv i min bostadsrätt?",
     "För ett vanligt golvbyte oftast inte, men ingrepp i bärande konstruktion eller i rör för "
     "vatten och värme kräver styrelsens tillstånd enligt bostadsrättslagen. Kontrollera även "
     "stadgarna."),
  ],
  "sources": [
    SKV_ROT, SKV_SA,
    ("Golvbranschen – Uttorkning av golvavjämning",
     "https://www.golvbranschen.se/teknik--material/golvavjamning/uttorkning-av-golvavjamning/"),
    ("Golvbranschen – Samlade limrekommendationer", "https://golvbranschen.se/rad-riktlinjer/limrekommendationer"),
    ("Byggkeramikrådet – Vanliga frågor", "https://www.bkr.se/vanliga-fragor"),
    BRL,
  ],
  "cta": ("Vill du ha nytt golv eller slipa det gamla?",
          "Boka ett gratis platsbesök så mäter vi underlaget och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat ljust ekgolv i ett vardagsrum med stora fönster",
     "freshly sanded and oiled light oak plank floor in a bright Scandinavian living room of a 1930s Stockholm villa, large windows, white walls, empty room, soft daylight"),
    ("Halvlagd flerskiktsparkett på underlagsduk i ett tomt rum",
     "empty room, oak engineered parquet floor being installed: the left half of the floor is finished with tight parallel rows of boards, the right half shows bare white foam underlay, a stack of plank packages against the wall, no hands, no people, natural light"),
  ],
  "related": [
    ("snickare.html", "Snickare i Stockholm", "Trösklar, lister, dörrar och inredning."),
    ("malare.html", "Målare i Stockholm", "Väggar och tak innan golvet läggs."),
    ("badrumsrenovering.html", "Badrumsrenovering i Stockholm", "Klinker och tätskikt i våtrum."),
    ("villarenovering.html", "Villarenovering", "Hela huset med en kontakt."),
  ],
},

"snickare.html": {
  "kind": "hub", "service": "snickare", "svc_label": "Snickare",
  "title": "Snickare i Stockholm – altan, väggar, dörrar och inredning",
  "description": "Snickare i Stockholm för bygg- och inredningssnickeri: altan och trall, "
                 "innerväggar, dörrar, trappor, listverk och platsbyggd förvaring. ROT på arbetet.",
  "h1": "Snickare i Stockholm",
  "lead": "Behöver du en snickare i Stockholm för en ny altan, en vägg som ska flyttas, nya "
          "innerdörrar eller platsbyggda garderober tar vi jobbet från ritning till sista "
          "listen. Vi utgår från huset du har och säger till när ett jobb kräver bygglov, "
          "anmälan eller styrelsens tillstånd.",
  "card": "Altan, väggar, dörrar och inredning.",
  "sections": [
    {"id": "snickeri", "anchor": "Vad snickaren gör",
     "h2": "Byggsnickeri och inredningssnickeri",
     "paras": [
       "Byggsnickeri är det som håller ihop huset: stommar till väggar, bjälklag, takstolar, "
       "altaner och mindre tillbyggnader. Inredningssnickeri är det du ser och tar i varje dag, "
       "som dörrar och karmar, foder och golvlister, trappor, bänkar och platsbyggda skåp. Många "
       "jobb är både och, till exempel en ny vägg som ska få dörr, foder och lister.",
       "Vi arbetar i villor, radhus och lägenheter i hela Stockholm, från Bromma där vi har vår "
       "bas till kranskommunerna. Ett snickeriarbete hänger ofta ihop med andra moment, och vi "
       "samordnar dem som en total entreprenad med en kontaktperson. El och VVS i samma projekt "
       "utförs av installatörer med rätt behörighet för just de arbetena."],
     "aside": {"title": "Vanliga snickeriuppdrag",
               "items": ["Altan, trall och trappor ute",
                         "Nya eller flyttade innerväggar",
                         "Byte av innerdörrar och karmar",
                         "Trappor, räcken och ledstänger",
                         "Foder, golvlister och taklister",
                         "Platsbyggda garderober och bokhyllor"]}},
    {"id": "ute",
     "h2": "Altan, trall och mindre tillbyggnader",
     "paras": [
       "En altan byggs på plintar eller en grund, med bärlina, reglar och trall ovanpå. Det som "
       "avgör hur länge den håller är sådant som inte syns när den är klar: att virket under "
       "trallen kan torka ut, att det finns luft mellan trall och mark, att reglarna inte ligger "
       "direkt mot husets fasad och att vattnet rinner bort från huset. En gammal altan med "
       "ruttna reglar går ofta att bygga om på samma plats.",
       "Ska altanen få tak, väggar eller glas blir det i regel en tillbyggnad av huset. Större "
       "projekt, som ett nytt rum eller ett fristående gästhus, beskriver vi på sidorna om "
       "<a class=\"text-link\" href=\"tillbyggnad.html\">tillbyggnad</a> och "
       "<a class=\"text-link\" href=\"attefallshus.html\">attefallshus</a>."],
     "aside": None},
    {"id": "lov",
     "h2": "Lov och anmälan efter PBL-ändringarna 1 december 2025",
     "paras": [
       "Plan- och bygglagens kapitel om lov skrevs om från 1 december 2025. För altaner gäller nu "
       "enligt <a class=\"text-link\" href=\"https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/bygglov-for-anlaggningar/altan/\" "
       "rel=\"noopener\">Boverket</a> att bygglov inom detaljplan krävs först om altanen blir "
       "högre än 1,8 meter över marken och placeras inom 3,6 meter från en byggnad, eller högre "
       "än 1,2 meter och placeras längre bort. Höjden mäts från marken vid altanens yttersida "
       "till altangolvets ovansida. Ett lovfritt räcke räknas inte in, men ett plank ovanpå "
       "altanen gör det. Utanför detaljplan finns inga motsvarande mått.",
       "Ett småhus får byggas till utan bygglov med sammanlagt högst 30 kvadratmeter, om "
       "tillbyggnaden inte är högre än husets taknock och placeras minst 4,5 meter från gränsen "
       "eller har grannens skriftliga medgivande. Lovfria tillbyggnader som redan finns, till "
       "exempel en attefallstillbyggnad eller ett skärmtak, räknas in i de 30 kvadratmeterna. "
       "Friggebod och attefallshus har ersatts av lovfria komplementbyggnader och "
       "komplementbostadshus, med högst 30 kvadratmeter per byggnad och 45 kvadratmeter "
       "sammanlagt på tomten inom detaljplan.",
       "Lovfritt betyder inte anmälningsfritt. Påverkas husets bärande delar väsentligt, till "
       "exempel när en bärande vägg tas bort, krävs anmälan och startbesked innan arbetet "
       "börjar, och Boverket rekommenderar att en konstruktör tar reda på vad som bär. Lov kan "
       "också krävas i särskilt värdefulla miljöer och nära gräns eller järnväg, så vi stämmer "
       "av med kommunens byggnadsnämnd när huset ligger i ett sådant läge."],
     "aside": {"title": "Lovfritt inom detaljplan (småhus)",
               "items": ["Altan upp till 1,8 m inom 3,6 m från huset",
                         "Altan upp till 1,2 m längre bort",
                         "Tillbyggnad högst 30 m² totalt",
                         "Komplementbyggnad högst 30 m², 45 m² sammanlagt",
                         "Bärande ändring: anmälan och startbesked"]}},
    {"id": "inne",
     "h2": "Innerväggar, dörrar, trappor och listverk",
     "paras": [
       "En ny innervägg byggs med reglar av trä eller stål, isolering för ljudet och gips eller "
       "skiva, och får dörr, foder och lister så att den ser ut att ha stått där från början. Att "
       "ta bort en vägg är ett större beslut: är den bärande behövs en ny balk och en anmälan. "
       "Boverket nämner också att en vägg som var förberedd för att öppnas när huset byggdes "
       "kan tas bort utan anmälan, om de bärande delarna inte påverkas väsentligt.",
       "Byte av innerdörrar handlar ofta om karmar som har satt sig, nya trösklar efter ett "
       "golvbyte eller dörrar som ska matcha husets epok. Trappor renoveras genom att steg och "
       "sättsteg byts eller slipas och räcken förstärks. I äldre hus kan gamla profilerade foder "
       "och taklister kompletteras med nya i samma profil, så att ett renoverat rum inte bryter "
       "mot resten av huset.",
       "Platsbyggda garderober och bokhyllor under trappor, i snedtak och i nischer tar vara på "
       "ytor där köpta möbler inte passar. I en bostadsrätt krävs styrelsens tillstånd för "
       "ingrepp i bärande konstruktion och för andra väsentliga förändringar av lägenheten, "
       "enligt bostadsrättslagens 7 kap. 7 §. Golvet efter ett väggbyte tar vi hand om inom "
       "<a class=\"text-link\" href=\"golvlaggning.html\">golvläggning</a>."],
     "aside": None},
  ],
  "steps_h2": "Så går ett snickeriuppdrag till",
  "steps": [
    ("Platsbesök", "Vi mäter, ser på konstruktionen och reder ut om något bär, om lov eller anmälan kan behövas."),
    ("Kostnadsförslag och ritning", "Du får ett skriftligt kostnadsförslag och vid behov en enkel ritning över det som ska byggas."),
    ("Lov, anmälan och tillstånd", "Behövs bygglov, anmälan eller styrelsens tillstånd tar vi fram underlaget innan arbetet börjar."),
    ("Stomme och grovsnickeri", "Grund, reglar, balkar och stomme byggs först, och el och VVS dras in där det behövs."),
    ("Finsnickeri", "Trall, skivor, dörrar, foder, lister och inredning monteras och passas in."),
    ("Slutgenomgång", "Vi går igenom jobbet tillsammans och lämnar de handlingar som hör till."),
  ],
  "rot_h2": "ROT-avdrag för snickeriarbete",
  "rot": [
    "Skatteverket räknar flera snickeriarbeten som rotarbete i ett småhus: att bygga en altan "
    "som byggs ihop med huset, att reparera entrétrappor och altaner, att riva väggar och bygga "
    "om planlösningen, att byta och reparera dörrar och att montera platsbyggda garderober och "
    "bokhyllor. En tillbyggnad ger rätt till avdrag när den sitter ihop med huset, och huset ska "
    "då vara äldre än fem år. En helt ny fristående byggnad, som ett nytt gästhus eller garage, "
    "ger inget avdrag, och inte heller staket eller fristående möbler.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år, och rot "
    "och rut får sammanlagt bli högst 75 000 kronor. Material och resor ingår inte. Vi drar "
    "avdraget direkt på fakturan. I en bostadsrätt gäller andra gränser – att bygga en altan "
    "ger till exempel inget avdrag där."],
  "price_h2": "Vad styr priset på snickeriarbetet?",
  "price": [
    "Priset för ett snickeriuppdrag styrs av hur mycket som ska byggas från grunden och hur "
    "mycket som ska passas in mot det befintliga. En altan på plan mark med fria mått går "
    "fortare än en på sluttning med trappor. En vägg med dörr, el och lister tar längre tid än "
    "en enkel skiljevägg, och snickerier i ett äldre hus med sneda vinklar kräver mer "
    "anpassning. Material, virkeskvalitet och eventuell konstruktör eller lovhandlingar räknas "
    "till.",
    "Vi kommer ut på ett gratis platsbesök och lämnar sedan ett skriftligt kostnadsförslag där "
    "arbete och material redovisas var för sig."],
  "faq": [
    ("Behöver jag bygglov för att bygga en altan?",
     "Inom detaljplan krävs lov först om altanen blir högre än 1,8 meter och ligger inom 3,6 "
     "meter från huset, eller högre än 1,2 meter längre bort. Utanför detaljplan finns inga "
     "sådana mått, men särskilt värdefulla miljöer kan ha krav."),
    ("Får jag riva en innervägg utan att göra en anmälan?",
     "Ja, om väggen inte bär och de bärande delarna inte påverkas väsentligt. Bär väggen krävs "
     "anmälan och startbesked, och en konstruktör bör räkna på den nya balken."),
    ("Ger platsbyggda garderober rätt till ROT?",
     "Ja, Skatteverket räknar montering av platsbyggda fasta möbler som garderober och "
     "bokhyllor som rotarbete. Fristående möbler ger inget avdrag."),
    ("Räknas ett skärmtak över altanen in i ytan för lovfri tillbyggnad?",
     "Ja. Boverket skriver att lovfria skärmtak och tillbyggnader som redan finns ska räknas in "
     "i de 30 kvadratmeter ett småhus får byggas till utan lov."),
    ("Kan ni bygga om en gammal altan på samma plats?",
     "Ofta. Är plintarna och bärlinorna friska kan trall och reglar bytas, annars byggs "
     "altanen om från grunden. Det avgörs vid platsbesöket."),
  ],
  "sources": [
    ("Boverket – Lista med PBL-ändringar som trädde i kraft 1 december 2025",
     "https://www.boverket.se/sv/samhallsplanering/uppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/"),
    ("Boverket – Bygglov för altan (PBL kunskapsbanken)",
     "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/bygglov-for-anlaggningar/altan/"),
    ("Boverket – Mur, plank, altan och annat",
     "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/mur-plank-altan-och-annat/"),
    ("Boverket – Göra en tillbyggnad",
     "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/gora-en-tillbyggnad/"),
    ("Boverket – Ingrepp i husets bärande delar",
     "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/ingrepp-i-husets-barande-delar/"),
    SKV_ROT, SKV_SA, BRL,
  ],
  "cta": ("Har du ett snickeriprojekt?",
          "Boka ett gratis platsbesök så går vi igenom vad som ska byggas och vad som krävs för lov."),
  "img": [
    ("Ny trätrall på en altan vid en röd trävilla med vita knutar",
     "new pressure-treated wooden deck with steps and simple railing attached to a red Swedish wooden villa with white corners, garden, summer, Stockholm suburb"),
    ("Platsbyggd vit garderob under ett snedtak med fyllningsdörrar",
     "custom built-in white wardrobe with panel doors fitted under a sloping attic ceiling, wooden floor, bright Scandinavian interior, no people"),
  ],
  "related": [
    ("tillbyggnad.html", "Tillbyggnad", "Mer yta i anslutning till huset."),
    ("attefallshus.html", "Attefallshus", "Fristående hus på tomten."),
    ("golvlaggning.html", "Golvläggning i Stockholm", "Parkett, trägolv och slipning."),
    ("byggfirma.html", "Byggfirma i Stockholm", "Total entreprenad för villan."),
  ],
},
}
