# -*- coding: utf-8 -*-
"""Attefallshus och tillbyggnad – ortsidor v32: Kungsholmen (Stora Essingen) och Kista (2026-10-28).
Hubbar: attefallshus.html och tillbyggnad.html. Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.

Lokal vinkel per sida:
attefallshus-kungsholmen – Kungsholmens 272 småhus med äganderätt, varav 268 på Stora Essingen (områdesfakta 2025);
  Stora Essingen som villastad markerad som kulturhistoriskt värdefull miljö i Varsam (s. 85); villastadens tomter
  och grönska; stadens regler för komplementbostadshus och utökad lovplikt; Lilla Essingen utan småhus.
tillbyggnad-kungsholmen – villorna på Stora Essingen (glasverandor, takkupor, individuella hus); 30 kvadratmeter
  BTA/OPA och vad som räknas in; tillbyggnad på flerbostadshus ska följa detaljplanen (de flesta hus på
  Kungsholmen); Varsams vägledning om material och detaljer.
attefallshus-kista – småhusen i Kista och Akalla efter upplåtelseform (områdesfakta 2025); föreningen äger marken i
  bostadsrättsradhus; Varsam om gruppbyggda småhus i storskaliga stadsdelar (Akalla, Husby); huset ska vara mindre
  än det det kompletterar; Kista utbyggt 1975–1980 (Stockholms spår).
tillbyggnad-kista – platta eller svagt lutande pulpettak och nockhöjden som tak för en lovfri tillbyggnad; brandskydd
  mot grannen i radhuslängan (anmälan); avvattning från låglutande tak (Boverket); husgruppens material.

Fakta endast från källorna i respektive 'sources', öppnade med Python/urllib (Mozilla-UA) 2026-10-28, alla svarade
200; pdf:erna har textlager. Skatteverket återställde anslutningen härifrån – samma URL och formuleringar som v22–v31.
Strukna: avgifter, handläggningstider, antal hus per gata, uppgifter om enskilda fastigheter.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_SB = "https://bygglov.stockholm/nar-behovs-bygglov/"
_STH_KBH = ("Stockholms stad – Komplementbostadshus (bygglovsbefriad)", _SB + "bygga-nytt-och-bygga-till/komplementbostadshus-bygglovsbefriad/")
_STH_TBF = ("Stockholms stad – Tillbyggnad (bygglovsbefriad)", _SB + "bygga-nytt-och-bygga-till/tillbyggnad-bygglovsbefriad/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
              _SB + "andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_KISTA_SPAR = ("Stockholms stadsmuseum – Stockholms spår: Kista (pdf)",
               "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000080.pdf")
_BOV_ROLL = ("Boverket – Roller i byggskedet",
             "https://www.boverket.se/sv/energiguiden/energieffektivisera-flerbostadshus/energirenovera/bygga/roller-i-byggskedet/")
_BOV_AVV = ("Boverket – Risker med avvattning från låglutande tak",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttertak/takets-ytskikt/avvattning-laglutande-tak/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")

_REG = _L.format("attefallshus-regler.html", "reglerna för attefallshus")

PAGES_TJ = {

# ------------------------------------------------------------------ ATTEFALLSHUS KUNGSHOLMEN
"attefallshus-kungsholmen.html": {
  "kind": "district", "service": "attefallshus", "ort": "Kungsholmen", "svc_label": "Attefallshus",
  "title": "Attefallshus på Kungsholmen – villorna på Stora Essingen",
  "description": "Attefallshus på Kungsholmen: nästan alla småhus står på Stora Essingen, en villastad med kulturvärden. Mått, lov, grannar och vad som gäller.",
  "h1": "Attefallshus på Kungsholmen",
  "lead": "På Kungsholmen bor de flesta i flerbostadshus, och ett gårdshus på tomten är bara aktuellt där det finns villor. Det gör det främst på Stora Essingen. Geal Entreprenad AB bygger attefallshus och tar fram underlaget för ett bygglov när villastadens kulturvärden kräver det.",
  "card": "Gårdshus vid villorna på Stora Essingen.",
  "sections": [
    {"id": "essingen-smahus", "anchor": "Stora Essingen",
     "h2": "268 av Kungsholmens 272 ägda småhus",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 272 småhus med äganderätt i Kungsholmens stadsdelsområde. 268 av dem ligger på Stora Essingen. Där finns också 35 småhus som hyrs ut och elva som är bostadsrätter. På Lilla Essingen och i resten av stadsdelsområdet bor man i stort sett bara i lägenheter.",
       "Ett komplementbostadshus ska enligt Stockholms stad komplettera ett en- eller tvåbostadshus som redan finns på tomten. På Kungsholmen gäller frågan alltså i praktiken villa- och radhusägarna på Stora Essingen. Den som bor i en bostadsrätt i ett flerbostadshus kan inte bygga ett attefallshus på gården, eftersom huset man bor i inte är ett småhus.",
     ],
     "aside": {"title": "Småhus på Kungsholmen 2025", "items": [
       "272 med äganderätt", "268 av dem på Stora Essingen", "35 hyrda småhus på Stora Essingen", "Lilla Essingen: inga småhus"]}},
    {"id": "villastad-essingen", "h2": "En villastad med kulturvärden",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden räknar Stora Essingen till villastäderna och markerar området som kulturhistoriskt värdefull miljö i sin tabell. Villastäderna beskrivs som privat organiserade områden med individuellt utformade hus, glasverandor, takkupor och snickarglädje, där grönskan i trädgårdarna håller ihop gatubilden.",
       "Vägledningen ber att man bibehåller gaturummens gröna karaktär och undviker att hårdgöra grönytor. För ett gårdshus betyder det att placeringen spelar roll: ett hus som tar trädgården mellan villan och gatan påverkar mer än ett som står mot baksidan. Vi ritar in befintliga träd och höjder på situationsplanen innan vi föreslår ett läge.",
     ],
     "aside": None},
    {"id": "lov-essingen", "h2": "Lovfritt eller bygglov – Stadsmuseets karta avgör",
     "paras": [
       "Stockholms stad skriver att utökad lovplikt gäller för en byggnad, tomt eller ett bebyggelseområde som är särskilt kulturhistoriskt värdefullt, och att det omfattar alla typer av komplementbyggnader. Då krävs bygglov även för ett hus som annars hade varit lovfritt. Om fastigheten berörs ser man i Stadsmuseets klassificeringskarta, där en grön ring markerar områden som pekats ut som särskilt värdefulla i översiktsplanen.",
       "Vägledningens markering och kartans ringar är inte samma sak, så vi slår upp just din fastighet och frågar Stadsmuseet om det är oklart. Krävs bygglov tar vi fram ritningar som visar hur gårdshuset förhåller sig till villan i höjd, material och kulör.",
     ],
     "aside": {"title": "Bygglov krävs om tomten", "items": [
       "Ligger i riksintresse (blå ring)", "Ligger i särskilt värdefullt område (grön ring)", "Är blå- eller grönklassad", "Har skyddsbestämmelser i planen"]}},
    {"id": "matt-essingen", "h2": "Mått och avstånd på villatomten",
     "paras": [
       "Utan bygglov får komplementbostadshuset ha högst 30,0 kvadratmeter byggnadsarea och en taknock på högst 4,0 meter. Det ska vara mindre än villan det kompletterar, och tillsammans med andra komplementbyggnader som byggts utan lov, till exempel en gammal friggebod, får byggnadsarean inte bli mer än 45,0 kvadratmeter.",
       "Huset ska stå 4,5 meter från tomtgränsen. Vill du bygga närmare behövs ett skriftligt medgivande från grannen, och mot gata eller park är det staden som ska medge. Ska huset få vatten och avlopp, ventilation eller en eldstad krävs en anmälan och startbesked innan bygget börjar. Mer om grunderna finns i " + _REG + ".",
     ],
     "aside": None},
    {"id": "plan-essingen", "h2": "Detaljplanen och prickmarken",
     "paras": [
       "Ett komplementbostadshus som inte kräver lov får enligt Stockholms stad strida mot detaljplanen och till exempel placeras på prickmark. Kräver huset bygglov på grund av kulturvärdena prövas det däremot mot planen. Det är ytterligare ett skäl att börja med att ta reda på om tomten omfattas av utökad lovplikt.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus på Stora Essingen",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på tomten, villan och träden."),
    ("Kartan", "Vi kontrollerar klassning och detaljplan för fastigheten."),
    ("Ritningar", "Situationsplan, fasader och kulör som passar villan."),
    ("Lov eller anmälan", "Bygglov där kulturvärden kräver det, annars anmälan."),
    ("Grund och stomme", "Grund, stomme och tak efter startbesked."),
    ("Inflyttning", "Installationer, ytskikt och slutbesked."),
  ],
  "rot_h2": "Inget rotavdrag för ett nytt gårdshus",
  "rot": [
    "Skatteverket skriver att det inte går att få rotavdrag för att bygga en ny bostad eller en ny fristående byggnad som en friggebod eller ett garage. Ett attefallshus står fritt på tomten och räknas därför utan avdrag i kostnadsförslaget.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus på Kungsholmen?",
  "price": [
    "Husets storlek och planlösning, grundläggning på tomtens berg eller lera, om bygglov och ritningar för en kulturmiljö behövs, vatten och avlopp och hur långt material måste bäras från gatan. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan jag bygga ett attefallshus på gården till min bostadsrätt på Kungsholmen?",
     "Nej. Ett komplementbostadshus ska komplettera ett en- eller tvåbostadshus, och ett flerbostadshus räknas inte dit."),
    ("Behöver jag bygglov för ett gårdshus på Stora Essingen?",
     "Det beror på om fastigheten ligger i ett område som pekats ut som särskilt kulturhistoriskt värdefullt. Stadsmuseets klassificeringskarta visar det, och då krävs bygglov."),
    ("Räknas min gamla friggebod in i de 45 kvadratmetrarna?",
     "Ja, om den byggts utan bygglov. Stockholms stad räknar in tidigare komplementbyggnader och attefallshus på tomten."),
    ("Hur många småhus finns det på Stora Essingen?",
     "Stadens områdesfakta räknar 268 småhus med äganderätt 2025, plus 35 som hyrs ut och elva bostadsrätter."),
  ],
  "sources": [_of("Kungsholmens stadsdelsområde", "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade"),
              _of("Stora Essingen", "inre-staden/kungsholmen/stora-essingen"),
              _of("Lilla Essingen", "inre-staden/kungsholmen/lilla-essingen"), _VARSAM, _STH_KBH, _STH_KLASS, _SKV],
  "cta": ("Vill du bygga ett gårdshus på Stora Essingen?", "Boka ett gratis platsbesök, så tar vi reda på vad som gäller för din tomt innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet gårdshus med träpanel i en villaträdgård",
     "small single-storey Swedish guest house with light grey vertical wooden panel and a pitched roof in the back garden of an older villa, mature apple tree, lawn, summer daylight" + _SFX),
    ("Äldre villa med glasveranda och takkupa bakom en häck",
     "1920s Swedish wooden villa with a glazed veranda and a roof dormer behind a trimmed hedge, leafy residential street on an island in Stockholm, summer" + _SFX),
    ("Utsättning av ett gårdshus med pinnar och snöre i trädgården",
     "wooden stakes and a taut string line marking out a small rectangle on a lawn in an older villa garden, mature trees, summer daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ TILLBYGGNAD KUNGSHOLMEN
"tillbyggnad-kungsholmen.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Kungsholmen", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad på Kungsholmen – villa eller föreningshus",
  "description": "Tillbyggnad på Kungsholmen: uterum och kupor på villorna på Stora Essingen, vad som gäller för flerbostadshus, 30 kvadratmeter och lov.",
  "h1": "Tillbyggnad på Kungsholmen",
  "lead": "En tillbyggnad på Kungsholmen kan vara ett uterum på en villa på Stora Essingen eller ett skärmtak på ett föreningshus. Reglerna skiljer sig åt mellan de två. Geal Entreprenad AB ritar och bygger tillbyggnader och tar reda på om du behöver bygglov, anmälan eller ingetdera.",
  "card": "Uterum, kupor och skärmtak.",
  "sections": [
    {"id": "villa-forening", "anchor": "Villa eller förening",
     "h2": "Två slags hus med olika regler",
     "paras": [
       "Stockholms stad skriver att en lovfri tillbyggnad får göras på ett en- eller tvåbostadshus, men också på andra byggnader som flerbostadshus. Skillnaden är detaljplanen. På en villa får en lovfri tillbyggnad strida mot planen och till exempel stå på prickmark. På ett flerbostadshus ska den stämma med planen eller vara en liten avvikelse som inte motverkar planens syfte.",
       "Det spelar roll på Kungsholmen, där stadens områdesfakta räknar över 40 000 lägenheter i flerbostadshus men bara några hundra småhus. Vill en förening bygga ett skärmtak över en entré eller låga balkonger mot gården börjar vi därför med planen. För villaägaren är frågan i stället hur huset och tomten påverkas.",
     ],
     "aside": {"title": "Exempel på tillbyggnader", "items": [
       "Uterum", "Skärmtak", "Större takkupor", "Lågt sittande balkonger"]}},
    {"id": "essingen-villor", "h2": "Villorna på Stora Essingen",
     "paras": [
       "Av Kungsholmens 272 småhus med äganderätt ligger 268 på Stora Essingen. Stadens vägledning Varsam utveckling av småhus- och villaområden räknar ön till villastäderna och markerar den som kulturhistoriskt värdefull miljö. Villastäderna beskrivs med individuellt utformade hus där glasverandor och takkupor ger variation.",
       "Vägledningen ber att man tar tillvara eller återskapar karaktärsskapande material, kulörer och detaljer vid ombyggnad. En tillbyggnad på en sådan villa ritar vi därför med samma taklutning, panel eller puts och fönsterindelning som huset, eller som en tydligt underordnad volym. Ligger fastigheten i ett område som pekats ut som särskilt värdefullt krävs bygglov även för det som annars är lovfritt.",
     ],
     "aside": None},
    {"id": "30-kvm", "h2": "30 kvadratmeter – och vad som räknas in",
     "paras": [
       "En lovfri tillbyggnad får enligt staden vara högst 30,0 kvadratmeter bruttoarea eller öppenarea och inte nå högre än husets taknock. Alla lovfria tillbyggnader på huset räknas ihop, även äldre som en attefallstillbyggnad, ett friggebodsskärmtak eller attefallstakkupor. Har villan redan en sådan är utrymmet mindre än det låter.",
       "Tillbyggnaden ska stå 4,5 meter från tomtgränsen, och närmare krävs ett skriftligt medgivande från berörda grannar med fastighetsbeteckning, situationsplan och underskrifter. Mot gatan är det staden som ska medge. Utan medgivande blir det en bygglovsansökan.",
     ],
     "aside": {"title": "Räknas in i 30 m²", "items": [
       "Attefallstillbyggnad", "Friggebodsskärmtak", "Attefallstakkupor", "Andra lovfria tillbyggnader"]}},
    {"id": "anmalan-kungsholmen", "h2": "Anmälan när stommen eller brandskyddet berörs",
     "paras": [
       "Även när bygglov inte behövs krävs en anmälan och startbesked om tillbyggnaden påverkar husets bärande konstruktion eller brandskydd, eller om den ska få eldstad eller vatten och avlopp. Ett uterum som öppnas mot vardagsrummet genom en ny dörr i en bärande vägg är ett typiskt fall.",
       "Boverket beskriver att byggherren, ofta fastighetsägaren, har det yttersta ansvaret för att lov eller anmälan finns innan arbetet börjar och att kontrollplanen följs. Vi tar fram handlingarna, och när det finns ett startbesked kan bygget börja.",
     ],
     "aside": None},
    {"id": "handlingar-kungsholmen", "h2": "Medgivandet på papper",
     "paras": [
       "Ett medgivande från grannen ska enligt staden vara skriftligt och innehålla fastighetsbeteckning, vilken åtgärd det gäller, en situationsplan med avståndet till gränsen och underskrifter från berörda grannar. Det ska kunna visas upp om byggnadsnämnden gör tillsyn, så vi tar fram situationsplanen som grannen skriver under.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi till på Kungsholmen",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på huset och tomten."),
    ("Plan och karta", "Detaljplan, klassning och tidigare lovfria tillbyggnader."),
    ("Ritningar", "Tillbyggnaden ritad i husets material och taklutning."),
    ("Lov eller anmälan", "Medgivanden, anmälan eller bygglov efter behov."),
    ("Bygget", "Grund, stomme, tak och anslutning mot huset."),
    ("Slutbesked", "Kontrollplanen följs upp och arbetet avslutas."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad på Kungsholmen",
  "rot": [
    "Skatteverket räknar en tillbyggnad av ett småhus som rotarbete när någon av dess sidor sitter ihop med husets yttervägg till minst 75 procent eller när en dörr förbinder tillbyggnaden med huset. Huset ska vara äldre än fem år och det mesta av den ursprungliga stommen ska vara kvar.",
    "Avdraget gäller arbetskostnaden, högst 30 procent och högst 50 000 kronor per person och år. Ett skärmtak eller balkonger på ett föreningshus betalas av föreningen och ger inget rotavdrag. Där avdraget gäller drar Geal det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på en tillbyggnad på Kungsholmen?",
  "price": [
    "Storlek och grundläggning, om en bärande vägg öppnas, hur taket ansluter, fönster och glas i ett uterum och om bygglov och ritningar för en kulturmiljö behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vår förening på Kungsholmen bygga ett skärmtak utan bygglov?",
     "Ja, om det stämmer med detaljplanen eller är en liten avvikelse som inte motverkar planen, och huset inte omfattas av utökad lovplikt."),
    ("Räknas villans gamla attefallstillbyggnad in i 30 kvadratmeter?",
     "Ja. Stockholms stad räknar in tidigare lovfria tillbyggnader på huset, även friggebodsskärmtak och attefallstakkupor."),
    ("Får tillbyggnaden på villan bli högre än taket?",
     "Nej, en lovfri tillbyggnad får inte vara högre än befintlig byggnads taknock."),
    ("Behöver jag anmäla ett uterum som byggs mot vardagsrummet?",
     "Om du öppnar i en bärande vägg eller påverkar brandskyddet behövs en anmälan och startbesked."),
  ],
  "sources": [_of("Kungsholmens stadsdelsområde", "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade"),
              _of("Stora Essingen", "inre-staden/kungsholmen/stora-essingen"), _VARSAM, _STH_TBF, _STH_KLASS, _BOV_ROLL, _SKV],
  "cta": ("Planerar du en tillbyggnad på Kungsholmen?", "Boka ett gratis platsbesök, så går vi igenom plan, lov och utförande innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Uterum i glas och trä mot en villaträdgård",
     "newly built glass and white painted timber conservatory attached to the garden side of an older Swedish villa, stone patio, lawn and shrubs, summer afternoon" + _SFX),
    ("Skärmtak över en port på ett putsat flerbostadshus",
     "simple modern steel and glass canopy over the entrance door of a light rendered 1930s apartment building in Stockholm, courtyard side, daylight" + _SFX),
    ("Stomme till en tillbyggnad mot ett befintligt hus",
     "timber frame of a small house extension under construction against the wall of an existing villa, roof rafters in place, protective plastic on the ground, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ ATTEFALLSHUS KISTA
"attefallshus-kista.html": {
  "kind": "district", "service": "attefallshus", "ort": "Kista", "svc_label": "Attefallshus",
  "title": "Attefallshus i Kista – radhus, föreningar och husgrupper",
  "description": "Attefallshus i Kista: vem som får bygga när radhuset är bostadsrätt, gårdshuset och husgruppen, mått, grannar och vad som gäller i Akalla.",
  "h1": "Attefallshus i Kista",
  "lead": "Småhusen i Kista och Akalla är till stor del radhus och kedjehus i husgrupper, och många av dem är bostadsrätter. Det avgör vem som kan bygga ett gårdshus. Geal Entreprenad AB bygger attefallshus och hjälper dig att reda ut ägande, mått och medgivanden först.",
  "card": "Gårdshus vid radhus och villor.",
  "sections": [
    {"id": "agande-kista", "anchor": "Vem äger marken",
     "h2": "Äganderätt eller bostadsrätt avgör",
     "paras": [
       "Stadens områdesfakta för 2025 räknar i Kista 482 småhus med äganderätt och 404 som är bostadsrätter. I Akalla är förhållandet det omvända: 170 småhus med äganderätt och 493 bostadsrätter. Därtill finns 75 småhus i Kista som ägs av allmännyttan och hyrs ut.",
       "Äger du huset och tomten kan du själv vara byggherre för ett komplementbostadshus. Är radhuset en bostadsrätt är det föreningen som äger fastigheten, och ett nytt hus på marken är en fråga för föreningen och inte för den enskilda medlemmen. Hyr du ett småhus kan du inte bygga på tomten. Vi tar därför reda på upplåtelseformen innan vi ritar något.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Kista: 482 äganderätt", "Kista: 404 bostadsrätt", "Akalla: 170 äganderätt", "Akalla: 493 bostadsrätt"]}},
    {"id": "kista-1975", "h2": "Byggt på fem år, i husgrupper",
     "paras": [
       "Stadsmuseets skrift om Kista berättar att staden köpte marken 1966 och att Kista byggdes ut under åren 1975–1980, med friare arkitektoniska former än i de andra stadsdelarna på Järvafältet. Akalla och Husby räknas i stadens vägledning Varsam utveckling av småhus- och villaområden till de storskaliga stadsdelarna med gruppbyggda småhus.",
       "Vägledningen beskriver radhus och kedjehus i strikt grupperade längor, där enhetligheten inom husgrupperna var mycket stor och färgsättningen noga komponerad. I Akalla finns också villor och atriumhus. Ett gårdshus som syns från gången bör därför ta upp husgruppens material och kulör, även när det får byggas utan lov.",
     ],
     "aside": None},
    {"id": "mindre-an-huset", "h2": "Mindre än huset det kompletterar",
     "paras": [
       "Stockholms stad ställer upp flera villkor för ett lovfritt komplementbostadshus: högst 30,0 kvadratmeter byggnadsarea, en taknock på högst 4,0 meter och en byggnadsarea som är mindre än huset det ska komplettera. På tomten får komplementbyggnader och komplementbostadshus som byggts utan lov tillsammans uppta högst 45,0 kvadratmeter.",
       "Villkoret om att vara mindre än huvudbyggnaden blir verkligt vid ett radhus, där husets egen byggnadsarea kan vara liten. Vi räknar på radhusets byggnadsarea och på bodar och förråd som redan finns innan vi föreslår en storlek. Mer om grunderna finns i " + _REG + ".",
     ],
     "aside": {"title": "Villkor utan bygglov", "items": [
       "Högst 30,0 m² byggnadsarea", "Taknock högst 4,0 m", "Mindre än huvudbyggnaden", "Högst 45,0 m² lovfritt på tomten"]}},
    {"id": "grannar-kista", "h2": "Grannar, gångvägar och anmälan",
     "paras": [
       "Huset ska stå 4,5 meter från tomtgränsen. Närmare krävs ett skriftligt medgivande från grannen, och gränsar tomten mot en gångväg eller park som staden förvaltar är det staden som ska medge.",
       "Ska gårdshuset få vatten och avlopp, ventilation eller en eldstad krävs en anmälan och startbesked. Där fastigheten omfattas av skyddsbestämmelser eller ligger i ett särskilt kulturhistoriskt värdefullt område krävs bygglov, och det visar Stadsmuseets klassificeringskarta.",
     ],
     "aside": None},
    {"id": "prickmark-kista", "h2": "Prickmark och en senare tillbyggnad",
     "paras": [
       "Stockholms stad skriver att ett komplementbostadshus som inte kräver lov får strida mot detaljplanen och till exempel placeras på mark som inte får bebyggas, så kallad prickmark. Det ger ibland ett läge på tomten som annars inte hade gått, men avståndet till gränsen och medgivandena gäller fortfarande.",
       "Vill du senare bygga till gårdshuset får det enligt staden ske utan lov bara om huset efter tillbyggnaden fortfarande är högst 30,0 kvadratmeter och 4,0 meter högt och mindre än huvudbyggnaden. Tillbyggnadens yta räknas in i de 45,0 kvadratmetrarna. Vi ritar därför gärna huset i full storlek från början om tomten tillåter det.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Kista",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på tomten och husgruppen."),
    ("Ägande", "Äganderätt, förening eller hyresrätt – vem är byggherre?"),
    ("Storlek", "Byggnadsarea mot huvudbyggnaden och befintliga bodar."),
    ("Medgivanden", "Grannar och staden där huset kommer närmare än 4,5 meter."),
    ("Anmälan", "Startbesked för vatten, avlopp och ventilation."),
    ("Bygget", "Grund, stomme, installationer och slutbesked."),
  ],
  "rot_h2": "Inget rotavdrag för ett nytt gårdshus i Kista",
  "rot": [
    "Skatteverket ger inget rotavdrag för att bygga en ny bostad eller ett nytt fristående hus som en friggebod eller ett garage. Ett komplementbostadshus står fritt på tomten, och kostnadsförslaget räknas därför utan avdrag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Kista?",
  "price": [
    "Husets storlek och planlösning, grunden, hur långt vatten och avlopp ska dras, åtkomsten till tomten från gångvägen och om bygglov behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan jag bygga ett attefallshus vid mitt bostadsrättsradhus i Kista?",
     "Inte själv. Föreningen äger fastigheten, så ett nytt hus på marken är en fråga för föreningen och styrelsen."),
    ("Får gårdshuset vara lika stort som mitt radhus?",
     "Nej. Ett lovfritt komplementbostadshus ska ha mindre byggnadsarea än huset det kompletterar."),
    ("Hur många småhus i Akalla är bostadsrätter?",
     "Stadens områdesfakta räknar 493 småhus som bostadsrätter och 170 med äganderätt 2025."),
    ("När byggdes Kista?",
     "Enligt Stadsmuseet byggdes Kista ut under åren 1975–1980, efter att staden köpt marken 1966."),
  ],
  "sources": [_of("Kista", "vasterort/jarva/kista"), _of("Akalla", "vasterort/jarva/akalla"), _KISTA_SPAR, _VARSAM,
              _STH_KBH, _STH_KLASS, _SKV],
  "cta": ("Funderar du på ett gårdshus i Kista?", "Boka ett gratis platsbesök, så går vi igenom ägande, storlek och medgivanden innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet gårdshus intill en radhuslänga med trädgård",
     "small modern Swedish backyard guest house with dark brown wooden panel and a low mono-pitch roof next to a 1970s terraced house row with brick and wood facades, small garden, summer" + _SFX),
    ("Radhuslänga från 1970-talet med tegel och trä",
     "Scandinavian late 1970s low terraced houses in Stockholm suburb, dark brown stained wooden panel and yellow brick, low mono-pitch roofs without chimneys, car-free footpath with lawns and birch trees, daylight" + _SFX),
    ("Grund för ett litet hus på en tomt",
     "foundation for a small house being prepared in a backyard: concrete pier footings set out in a rectangle, gravel and string lines, lawn around, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ TILLBYGGNAD KISTA
"tillbyggnad-kista.html": {
  "kind": "district", "service": "tillbyggnad", "ort": "Kista", "svc_label": "Tillbyggnad",
  "title": "Tillbyggnad i Kista – låga tak, radhuslängor och brandskydd",
  "description": "Tillbyggnad i Kista: platta och svagt lutande tak, nockhöjden som gräns, brandskyddet mot grannen i längan och vatten från låga tak.",
  "h1": "Tillbyggnad i Kista",
  "lead": "Radhusen i Kista och Akalla har ofta platta eller svagt lutande tak och delar väggar med grannarna. Det påverkar både hur hög en tillbyggnad får bli och vad som måste anmälas. Geal Entreprenad AB bygger uterum, tillbyggnader och skärmtak och reder ut reglerna innan arbetet börjar.",
  "card": "Tillbyggnad vid radhus och villor.",
  "sections": [
    {"id": "laga-tak", "anchor": "Låga tak",
     "h2": "Taknocken sätter taket för tillbyggnaden",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver småhusen i de storskaliga stadsdelarna, däribland Akalla och Husby, som radhus och kedjehus där taken ofta var platta eller svagt lutande pulpettak. Kista byggdes enligt Stadsmuseet ut under åren 1975–1980.",
       "Stockholms stad skriver att en lovfri tillbyggnad inte får vara högre än den befintliga byggnadens taknock. På ett hus med lågt tak blir det en verklig begränsning: en tillbyggnad med eget sadeltak kan snabbt nå över nocken. Vi ritar därför ofta ett låglutande tak som ansluter under det befintliga.",
     ],
     "aside": {"title": "Lovfri tillbyggnad", "items": [
       "Högst 30,0 m² BTA eller OPA", "Inte högre än taknocken", "4,5 m till gräns eller medgivande", "Tidigare tillbyggnader räknas in"]}},
    {"id": "brandskydd-kista", "h2": "Grannen på andra sidan väggen",
     "paras": [
       "I en radhuslänga delar husen väggar, och brandskyddet mellan bostäderna är byggt in i längan. Staden skriver att en tillbyggnad kräver anmälan och startbesked om den påverkar byggnadens bärande konstruktion eller brandskydd, även när bygglov inte behövs.",
       "En tillbyggnad som går ända fram till grannens gräns eller ansluter mot den gemensamma väggen behöver därför ritas så att brandskyddet hålls. Den ska också stå 4,5 meter från gränsen, eller så behövs ett skriftligt medgivande från grannen med situationsplan och underskrift. Vi tar fram ritningen som grannen skriver under.",
     ],
     "aside": None},
    {"id": "vatten-kista", "h2": "Vattnet från låga tak",
     "paras": [
       "Boverket skriver att låglutande tak belastas mer av nederbördsvatten och att en otillräcklig avvattning kan ge fuktskador. Utvändiga rännor och stuprör kan frysa, och stuprör som går till mark kan skadas av till exempel fordon. Om en brunn sätter igen ska vattnet kunna rinna vidare till en annan brunn eller ut genom ett bräddavlopp.",
       "När en tillbyggnad ansluter mot ett befintligt låglutande tak bestämmer vi tidigt var vattnet ska ta vägen, så att det inte samlas i hörnet mellan de två taken. Det är också där plåtslagaren och takläggaren behöver mötas i arbetet.",
     ],
     "aside": {"title": "Att bestämma tidigt", "items": [
       "Fall mot ränna eller brunn", "Var stupröret ska gå", "Vart vattnet går om brunnen sätts igen", "Anslutning mot gamla taket"]}},
    {"id": "husgrupp-kista", "h2": "Husgruppens material och ägandet",
     "paras": [
       "Vägledningen beskriver en blandning av tegel, trä och skivor på fasaderna men en mycket stor enhetlighet inom varje husgrupp. En tillbyggnad som tar upp längans material och kulör smälter in. Om fastigheten omfattas av skyddsbestämmelser eller ligger i ett särskilt värdefullt område krävs bygglov, och det visar Stadsmuseets klassificeringskarta.",
       "Stadens områdesfakta räknar 404 av småhusen i Kista som bostadsrätter. I en bostadsrätt krävs enligt bostadsrättslagen styrelsens tillstånd för bland annat ingrepp i bärande konstruktion och andra väsentliga förändringar, och marken ägs av föreningen. Äger du huset själv, som gäller 482 av småhusen i Kista, är det du som är byggherre.",
     ],
     "aside": None},
    {"id": "medgivande-kista", "h2": "Medgivandet från grannen",
     "paras": [
       "Staden skriver att ett medgivande ska vara skriftligt och innehålla fastighetsbeteckning, vilken åtgärd det gäller, en situationsplan med åtgärden och avståndet till gränsen inritade och underskrifter från berörda grannar. Får du inte medgivandet behöver du söka bygglov i stället.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi till ett radhus i Kista",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter taket och tittar på längan."),
    ("Höjd och yta", "Taknock, 30 kvadratmeter och tidigare tillbyggnader."),
    ("Ritningar", "Tak, avvattning och anslutning mot grannväggen."),
    ("Anmälan", "Startbesked när brandskydd eller stomme berörs."),
    ("Bygget", "Grund, stomme, tak och plåt."),
    ("Slutbesked", "Kontroller enligt kontrollplanen."),
  ],
  "rot_h2": "ROT-avdrag för tillbyggnad i Kista",
  "rot": [
    "Skatteverket räknar tillbyggnad av ett småhus som rotarbete när en sida sitter ihop med husets yttervägg till minst 75 procent eller när en dörr förbinder delarna. Huset ska vara äldre än fem år. Avdraget gäller arbetskostnaden, högst 30 procent och högst 50 000 kronor per person och år.",
    "I en bostadsrätt gäller avdraget bara arbete inne i bostaden som du ansvarar för enligt stadgarna. Där avdraget gäller drar Geal det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på en tillbyggnad i Kista?",
  "price": [
    "Storlek, grund, takets lutning och anslutning, avvattningen, brandskyddet mot grannen och om en vägg öppnas mot huset. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får min tillbyggnad ha sadeltak när radhuset har platt tak?",
     "Utan bygglov får tillbyggnaden inte vara högre än husets taknock. På ett lågt hus blir därför ett låglutande tak ofta det som fungerar."),
    ("Måste jag anmäla en tillbyggnad som ansluter mot grannens vägg?",
     "Om den påverkar brandskyddet eller den bärande konstruktionen krävs anmälan och startbesked."),
    ("Varför samlas vatten mellan uterummet och huset?",
     "Låglutande tak tar emot mer vatten. Anslutningen och avvattningen behöver planeras så att vattnet leds bort."),
    ("Vem bygger till ett bostadsrättsradhus i Kista?",
     "Föreningen äger marken, och styrelsen behöver ge tillstånd innan något byggs."),
  ],
  "sources": [_of("Kista", "vasterort/jarva/kista"), _KISTA_SPAR, _VARSAM, _STH_TBF, _STH_KLASS, _BOV_AVV, _BRL, _SKV],
  "cta": ("Vill du bygga till ditt radhus i Kista?", "Boka ett gratis platsbesök, så mäter vi tak och tomt och går igenom anmälan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Uterum med låglutande tak på baksidan av ett radhus",
     "small glazed conservatory with a low-pitched roof attached to the back of a late 1970s Swedish terraced house with brown wooden facade, small patio and lawn, daylight" + _SFX),
    ("Plåtränna och stuprör vid ett lågt tak",
     "close view of a new galvanised steel gutter and downpipe at the edge of a low-pitched roof where an extension meets an existing terraced house, overcast sky" + _SFX),
    ("Vägg mellan två radhus i en länga",
     "the junction between two terraced houses in a row seen from the garden side, a partition wall extending out between the small patios, brick and wood, daylight" + _SFX),
  ],
},

}
