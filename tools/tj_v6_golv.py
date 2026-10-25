# -*- coding: utf-8 -*-
"""Golvläggare – ortsidor v6: Danderyd, Ekerö, Sollentuna, Tyresö, Värmdö, Haninge (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade 2026-10-25: Danderyds kommun (Kulturmiljöhandboken
B46 Gamla Djursholm; Riktlinjer för kulturhistoriska byggnader och miljöer 2024; Ritningsarkiv), Ekerö kommun
(Kulturmiljöprogram 2015: Stenhamra, östra Ekerö, Adelsö), Sollentuna kommun (Översiktsplan med sikte på 2040;
Ändring av bärande konstruktion), Tyresö kommun (Planbeskrivning Fasanvägen etapp 13, 2023), Värmdö kommun
(Fritidshusområde i förändring del 1, 2023; Antikvarisk konsekvensanalys Gustavsberg 2023), Haninge kommun
(Haninges karaktärsmiljöer 2019/2020), Boverket (Vad är radon?; Mät radon i ditt hus; Fuktrisker med krypgrund),
Golvbranschen (Uttorkning av golvavjämning) och Skatteverket (rotavdrag).
Strukna (ej verifierade): Golvbranschens temperaturgräns för trägolv på golvvärme (bara tillverkar-/forumuppgifter),
grundläggningstyp (platta/krypgrund/plintar) per område, golvmaterial i originalutförande per område/epok,
kommunala radonkartor för Ekerö/Värmdö/Haninge, kommunens avgift för anmälan i Sollentuna (prisuppgift).
Inga priser, garantier, omdömen, egna uppdrag eller cert. Korslänkar via V4_MODULES i tjanster_v1.py.
Schema: se tools/tj_check.py."""

_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_GBR_U = ("Golvbranschen – Uttorkning av golvavjämning",
          "https://www.golvbranschen.se/teknik--material/golvavjamning/uttorkning-av-golvavjamning/")
_BOV_RADON = ("Boverket – Vad är radon?",
              "https://www.boverket.se/sv/byggande/halsa-och-inomhusmiljo/radon/vad-ar-radon/")
_BOV_MAT = ("Boverket – Mät radon i ditt hus",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-felaktig-ventilation/radon/mat/")
_BOV_KRYP = ("Boverket – Fuktrisker med krypgrund",
             "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-for-grund/krypgrund/")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ DANDERYD
"golvlaggare-danderyd.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Danderyd", "svc_label": "Golvläggare",
  "title": "Golvläggare i Danderyd – gamla trägolv i värdefulla villor",
  "description": "Golvläggare i Danderyd: varsam slipning av originalgolv i Djursholm, ritningar ur kommunens arkiv och golv i Enebybergs egnahem. Gratis platsbesök.",
  "h1": "Golvläggare i Danderyd",
  "lead": "Många villor i Danderyd har golv som är lika gamla som huset. Att slipa fram dem, laga dem eller lägga nytt är ett beslut som påverkar både rummet och husets värde. Geal Entreprenad AB slipar, lagar och lägger golv i hela Danderyd – Djursholm, Stocksund, Enebyberg och Danderyd – med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Originalgolv i villor från 1890-talet och framåt.",
  "sections": [
    {"id": "gamla-djursholm", "anchor": "Villorna i Danderyd",
     "h2": "Fyra villor, fyra sätt att bygga golv",
     "paras": [
       "Kulturmiljöhandboken beskriver kvarteren Delling och Gamla Djursholm vid Stora Värtans strand som platsen för några av Djursholms arkitekturhistoriskt mest intressanta villor. De spänner i ålder från 1890 till 1960-talet. Här står en stor brunmålad trävilla från 1890-talet, en medeltidsromantisk tegelvilla, en putsad klassicistisk villa från 1920-talet och en nästan brutalistisk betongvilla.",
       "Exemplet visar hur olika ett golvjobb kan bli inom samma kvarter. I en trävilla vilar golvet på träbjälkar som rör sig med årstiderna. I en betongvilla ligger det på ett bjälklag som först behöver vara tillräckligt torrt. Golvbranschen rekommenderar att fukten i ett betongbjälklag kontrolleras innan avjämningsmassa läggs, så att den inte överstiger vad det nya golvet tål. Vi börjar därför med att ta reda på hur just ditt hus är byggt.",
     ],
     "aside": {"title": "Vi tittar på", "items": [
       "Bjälklag av trä eller betong", "Brädornas tjocklek över sponten",
       "Spår av äldre ombyggnader", "Fukt i källare och nedre plan"]}},
    {"id": "originalgolv", "h2": "Originalgolvet är en del av huset",
     "paras": [
       "Handboken uppmanar till att försöka bevara de ursprungliga materialen, som med sin ålder och patina berättar om byggnadernas historia, äldre hantverksskicklighet och byggnadsteknik. Kommunens riktlinjer från 2024 lägger till att åtgärder ska utföras varsamt och med hänsyn till byggnadens särart även när fastigheten inte har något utpekat skydd. Kommunen ber dig också ta tidig kontakt för rådgivning om du planerar ändringar på eller inom din fastighet.",
       "För golvet betyder det att vi hellre lagar än river. Skadade brädor kan bytas mot likvärdiga, gamla spikhål fyllas och ett slitet parti slipas ner utan att hela rummet tas om. Ett nytt golv ovanpå det gamla kan vara rätt, men det bör vara ett medvetet val och inte en följd av att ingen tittade under mattan.",
     ],
     "aside": None},
    {"id": "ritningar-danderyd", "h2": "Bygglovsritningarna visar bjälklaget",
     "paras": [
       "Danderyds kommun har ett ritningsarkiv med handlingar som har lämnats in vid tidigare bygglov och andra åtgärder på fastigheten. Via kommunens e-tjänst går det att beställa bygglovsritningar för nästan alla byggnader i kommunen, men kommunen påpekar att det inte är säkert att allt du önskar finns kvar.",
       "Inför ett större golvjobb är sektionsritningen det mest användbara bladet. Där syns ofta hur bjälklaget är uppbyggt, åt vilket håll bjälkarna går och om ett våningsplan har byggts om. Det hjälper oss att bedöma om golvvärme, ett tjockare golv eller en ny trappa går att få in utan att röra bärande delar. Ska bjälkar kapas eller förstärkas blir det en fråga för kommunen, och det säger vi till om redan vid besöket.",
     ],
     "aside": None},
    {"id": "enebyberg-golv", "h2": "Egnahem och sena tillägg i Enebyberg",
     "paras": [
       "Riktlinjerna beskriver Enebyberg som en kommundel med tydliga årsringar, med bebyggelse från 1700-talet till 1970-talet. Bland de särskilt värdefulla miljöerna finns egnahemsområdet, där riktlinjerna lyfter fram äldre byggnadsdetaljer som fönster och portar i originalutförande.",
       "Inne i ett egnahem som har byggts till i flera omgångar kan varje rum ha sin egen historia. Ett kök från en senare ombyggnad kan ligga några centimeter högre än hallen, och en tillbyggnad har kanske ett helt annat underlag än det ursprungliga huset. Vi mäter nivåerna i alla rum innan golvet väljs, så att trösklar och övergångar blir få och dörrarna inte behöver kapas i onödan.",
     ],
     "aside": {"title": "När rummen har olika ålder", "items": [
       "Mät höjden i varje rum", "Välj samma golv eller tydlig gräns",
       "Planera trösklar före beställning", "Kontrollera dörrarnas frigång"]}},
    {"id": "slipa-lagom", "h2": "Slipa så lite som möjligt",
     "paras": [
       "Ett trägolv tål bara ett visst antal grundslipningar innan slitskiktet är förbrukat. Har golvet slipats några gånger tidigare kan det vara klokt att nöja sig med en lättare mellanslipning och ny lack eller olja, i stället för att gå ner till rent trä. Vi mäter hur mycket trä som finns kvar över sponten och föreslår den lättaste behandling som ger ett bra resultat.",
       "Missfärgningar och mörka partier i gamla golv går sällan att slipa bort helt utan att golvet tunnas ut för mycket. Då kan en pigmenterad olja eller såpa jämna ut intrycket. Vi lägger en provyta där det inte syns, så att du ser resultatet innan hela rummet behandlas. Mer om golvtyper och ytbehandling finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvjobbet till i Danderyd",
  "steps": [
    ("Besök", "Vi går igenom rummen, lyfter en list och ser vad golvet är gjort av och hur det har behandlats tidigare."),
    ("Underlag", "Om du har beställt ritningar ur kommunens arkiv går vi igenom dem tillsammans."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag med laga, slipa eller lägga nytt som separata alternativ."),
    ("Skydd", "Trappor, dörrar och rum som inte berörs skyddas innan något damm uppstår."),
    ("Arbete", "Brädor lagas, golvet slipas i flera steg eller ett nytt golv läggs på ett riktat underlag."),
    ("Yta och skötsel", "Ytbehandlingen görs efter provytan, och du får råd om hur golvet ska skötas."),
  ],
  "rot_h2": "ROT-avdrag för golvarbete i Danderyd",
  "rot": [
    "Skatteverket räknar slipning, lagning och byte av golv som rotarbete i ett småhus som du äger och bor i. Avdraget är 30 procent av arbetskostnaden och högst 50 000 kr per person och år. Tillsammans med rutavdrag är taket 75 000 kr.",
    "Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan, så du betalar bara din del av arbetskostnaden.",
  ],
  "price_h2": "Vad styr kostnaden i Danderyd?",
  "price": [
    "Mest avgör golvets skick: hur många brädor som behöver bytas, hur mycket trä som finns kvar och om det finns gamla lim- eller färgrester. Rummens storlek, antal trappor och om möbler ska flyttas spelar också in. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi slipa originalgolvet i vår villa i Gamla Djursholm utan att fråga kommunen?",
     "Att slipa och underhålla ett golv kräver normalt inget lov. Kommunens riktlinjer säger ändå att åtgärder ska göras varsamt, och kommunen erbjuder rådgivning innan du ändrar något på eller inom fastigheten."),
    ("Var hittar vi ritningar på hur bjälklaget i vår villa i Danderyd är byggt?",
     "Danderyds kommun har ett ritningsarkiv där du kan beställa bygglovsritningar via en e-tjänst. Alla handlingar finns inte kvar, men sektionsritningar är ofta det som hjälper oss mest."),
    ("Hur många gånger till kan ett gammalt furugolv slipas?",
     "Det beror på hur mycket trä som finns kvar över sponten. Vi mäter vid besöket och föreslår en lätt mellanslipning om golvet redan har slipats flera gånger."),
    ("Kan ett nytt golv läggas ovanpå det gamla i ett egnahem i Enebyberg?",
     "Ofta går det, om det gamla golvet ligger stabilt och höjden räcker vid dörrar och trösklar. Vi mäter nivåerna i alla rum innan vi föreslår det."),
    ("Behöver betongbjälklaget i en villa från 1960-talet fuktmätas innan nytt golv läggs?",
     "Golvbranschen rekommenderar att fukten i betongbjälklaget kontrolleras innan avjämning läggs. Vi ser till att mätningen görs innan golvet beställs."),
  ],
  "sources": [
    ("Danderyds kommun – Kulturmiljöhandboken: B46 Gamla Djursholm (pdf)",
     "https://sync.danderyd.se/globalassets/globala-filer/bygga-bo-och-miljo/bygglov/kulturmiljohandboken/b46-gamla-djursholm.pdf"),
    ("Danderyds kommun – Riktlinjer för kulturhistoriska byggnader och miljöer i Danderyd 2024 (pdf)",
     "https://www.danderyd.se/globalassets/globala-filer/kommun-och-politik/ovriga-styrdokument-ny/styrande-dokument---samhallsbyggnad-miljo-och-exploatering/riktlinjer-for-kulturmiljohistoriska-byggnader-och-miljoer-i-danderyd-2024.pdf"),
    ("Danderyds kommun – Ritningsarkiv", "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/ritningsarkiv/"),
    _GBR_U, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i villan i Danderyd slipas eller lagas?", "Boka ett gratis platsbesök så tittar vi på golvet och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat brett trägolv i ett ljust rum i en äldre villa i Danderyd",
     "freshly sanded and oiled wide old pine floorboards in an empty large bright room of a Swedish wooden villa from around 1900 in Djursholm, tall white painted panelled door, deep white skirting boards, tall window with white frame and view of old oak trees, soft daylight, no people, no text"),
    ("Gamla golvbrädor med spikhål och slitage före slipning",
     "close-up of an old Swedish wooden floor where three lighter new pine boards have been fitted between darker old worn boards before sanding, old nail holes filled, simple hand tools and a carpenter's square resting on the floor, natural light, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ EKERÖ
"golvlaggare-ekero.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Ekerö", "svc_label": "Golvläggare",
  "title": "Golvläggare i Ekerö – villor i Stenhamra och omgjorda stugor",
  "description": "Golvläggare i Ekerö: nya golv i 1960- och 70-talsvillor i Stenhamra, radon när golvet öppnas och golv i sommarhus som blivit helårshus. Gratis platsbesök.",
  "h1": "Golvläggare i Ekerö",
  "lead": "På Mälaröarna finns allt från stenhuggarbyns arbetarlängor till modernistiska villagator och sommarhus som i dag är helårsbostäder. Golven i husen är lika olika som husen själva. Geal Entreprenad AB lägger nya golv och slipar gamla i hela Ekerö kommun, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villor i Stenhamra och omgjorda sommarhus.",
  "sections": [
    {"id": "stenhamra", "anchor": "Husen i Ekerö",
     "h2": "Stenhamra: från stenhuggarby till villaort",
     "paras": [
       "Ekerö kommuns kulturmiljöprogram berättar att Stenhamra på Färingsös sydvästra sida etablerades 1884, när stenbrottet grundades. Intill brottet byggdes Stenhuggarbyn med arbetarbostäder och skola, och några av arbetarlängorna flyttades dit 1889 från Stockholms stads gamla stenbrott i Huvudsta. Brottet lades ned 1937.",
       "Under det tidiga 1900-talet började arbetarna bygga egna hem utanför byn, och de villorna finns kvar men har byggts om under åren. I dag domineras Stenhamra av villor från andra halvan av 1900-talet, framför allt enfamiljshus från 1960- och 70-talen. Programmet pekar ut Ramundvägen som ett ovanligt välgestaltat modernistiskt villaområde med mycket höga arkitektoniska värden.",
     ],
     "aside": {"title": "Husen i Stenhamra", "items": [
       "Arbetarlängor i Stenhuggarbyn", "Egnahem från tidigt 1900-tal",
       "Villor från 1960- och 70-talen", "Modernistiska Ramundvägen"]}},
    {"id": "sextiotal", "h2": "Golven i ett hus från 1960- eller 70-talet",
     "paras": [
       "Ett enfamiljshus från de här decennierna har ofta fått nya golv i omgångar. Under en laminatskiva från 1990-talet kan det ligga en plastmatta, och under den ett äldre parkett- eller brädgolv. Varje lager gör golvet högre och kan dölja skador i underlaget. Vi tar därför upp en bit i ett hörn eller vid en tröskel och ser vad som finns innan vi föreslår att riva, slipa eller bygga på.",
       "I ett modernistiskt hus är golvet ofta en stor del av rummets karaktär, med öppna planlösningar där samma golv löper genom flera rum. Där vill man undvika trösklar och skarvar mitt i ytan. Vi planerar läggningsriktning och övergångar så att golvet blir sammanhängande, och visar prover i husets eget ljus innan du bestämmer dig.",
     ],
     "aside": None},
    {"id": "blabetong-ekero", "h2": "Blåbetong och radon när golvet öppnas",
     "paras": [
       "Boverket skriver att marken under och runt huset är den vanligaste källan till radon, men att byggmaterialet också kan bidra. Alunskifferbaserad lättbetong, så kallad blåbetong, användes från 1929 till slutet av 1970-talet. I både väggar och bjälklag kan den ge höga halter när luftväxlingen är dålig.",
       "Boverket rekommenderar att du mäter radon när du bygger om eller till huset. I villor och radhus ska mätningen göras under eldningssäsongen, oktober till och med april, och pågå i minst två, helst tre månader. Ska vi ta upp ett golv mot marken eller öppna ett bjälklag i ett hus från perioden är det bra att ha ett aktuellt mätvärde, och att planera en ny mätning när arbetet är klart.",
     ],
     "aside": {"title": "Radon och golvbyte", "items": [
       "Finns en mätning från senaste tio åren?", "Mät oktober till april",
       "Minst två månader i bostaden", "Mät igen efter ombyggnaden"]}},
    {"id": "permanentat-ekero", "h2": "Sommarvillor som har blivit helårshus",
     "paras": [
       "Kulturmiljöprogrammet konstaterar att permanentning av fritidshus sker i snabb takt i kommunen. På östra Ekerö har områden med sommarbostäder, till exempel Älvnäs, Gällstaö och Erikssten, permanentats och förtätats de senaste decennierna, och där har sommarvillor och sportstugor från 1900-talet byggts om eller rivits. På Adelsö uppfördes förhållandevis stora fritidshusområden under andra halvan av 1900-talet, dolda i skogsterräng på öns södra sida och intill färjeläget.",
       "Ett golv i ett hus som var byggt för sommaren har sällan legat på ett underlag som är tänkt för vinterns kyla. När huset blir permanentbostad märks det i form av kalla golv, glipor och sviktande partier. Golvbytet är ett bra tillfälle att se över bjälklaget innan det nya golvet läggs ovanpå.",
     ],
     "aside": None},
    {"id": "mellan-ekero", "h2": "När det gamla och det nya huset ska ha samma golv",
     "paras": [
       "Ombyggda sommarhus har ofta en äldre del och en nyare, och de ligger sällan på exakt samma höjd. Vill du ha ett sammanhängande golv genom båda delarna behöver underlaget i den lägre delen byggas upp, eller en tröskel placeras där den gör minst skada. Vi mäter höjderna i hela huset och visar vad respektive lösning innebär innan något beställs. En tröskel kan också vara ett medvetet sätt att visa var det gamla huset slutar och det nya börjar.",
       "Badrum och tvättstuga hör till ett eget arbetsmoment med tätskikt, och kök kräver ofta att golvet planeras före skåpen. Ska fler rum göras om samtidigt är det klokt att lägga golvet i en ordning som gör att inget behöver rivas upp igen. Mer om material och underlag finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Golvjobbet i Ekerö steg för steg",
  "steps": [
    ("Platsbesök", "Vi tittar på golvets lager, mäter höjder och ser hur bjälklaget känns när man går på det."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag där rivning, underlag och nytt golv står var för sig."),
    ("Planering", "Vi bestämmer ordningen mellan rummen och om radonmätning eller fuktmätning behövs innan."),
    ("Rivning och underlag", "Gamla lager tas bort, underlaget riktas och nivåskillnader byggs upp."),
    ("Läggning eller slipning", "Golvet läggs med trösklar och lister anpassade efter dörrarna, eller slipas och behandlas."),
    ("Genomgång", "Vi går igenom resultatet och lämnar råd om skötsel."),
  ],
  "rot_h2": "Rotavdrag för golv i Ekerö",
  "rot": [
    "Att byta eller slipa golv ger rotavdrag på arbetskostnaden, både i villa, radhus och fritidshus som du äger och använder. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Material och resor räknas inte in. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här påverkar kostnaden",
  "price": [
    "Antalet gamla lager som ska bort, hur mycket underlaget behöver byggas upp och om bjälklaget behöver åtgärdas påverkar mest. Läget spelar också in, till exempel om material ska fraktas till en ö med färja. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vi har köpt en 70-talsvilla i Stenhamra – vad ligger under laminatgolvet?",
     "Det vet man först när en bit tas upp. Ofta finns ett eller flera äldre lager. Vi lyfter en del vid en tröskel och visar vad som finns innan vi föreslår något."),
    ("Ska vi mäta radon innan golvet i vårt hus på Ekerö byts?",
     "Boverket rekommenderar mätning när man bygger om. Öppnas golv mot marken eller bjälklag i ett hus byggt mellan 1929 och slutet av 1970-talet är ett aktuellt värde värdefullt."),
    ("Hur vet vi om huset är byggt med blåbetong?",
     "Blåbetong användes från 1929 till slutet av 1970-talet. Ett säkert besked ger en radonmätning, och det är den som avgör om något behöver åtgärdas."),
    ("Golvet i vår omgjorda sommarstuga i Älvnäs är kallt – räcker ett nytt golv?",
     "Sällan på egen hand. Kylan kommer oftast från bjälklaget under. Vi tittar på hur det är byggt och föreslår vad som behöver göras innan nytt golv läggs."),
    ("Kan ni lägga golv i ett fritidshus på Adelsö?",
     "Ja, vi tar golvjobb i hela Ekerö kommun. Transport av material med färja planeras in i tidplanen och syns i kostnadsförslaget."),
  ],
  "sources": [
    ("Ekerö kommun – Kulturmiljöprogram 2015 (pdf)",
     "https://www.ekero.se/download/18.553838ea17305720c321ec82/1597925412772/Eker%C3%B6%20kulturmilj%C3%B6program.pdf"),
    _BOV_RADON, _BOV_MAT, _SKV, _SKV2,
  ],
  "cta": ("Ska golven i huset i Ekerö göras om?", "Boka ett gratis platsbesök så tittar vi under ytan och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust ekgolv i ett öppet vardagsrum i en modernistisk villa från 1960-talet i Ekerö",
     "interior of an empty living room in a modest 1960s Swedish single-storey brick villa, newly laid light oak parquet floor running continuously into the dining area, ordinary wooden windows with white frames and low sills, white painted walls, a simple brick fireplace, view of a lawn, birch trees and a neighbouring villa, summer daylight, no people, no text"),
    ("Gammal plastmatta som ligger ovanpå ett äldre parkettgolv i ett hörn",
     "corner of an empty room in a 1970s Swedish house where a piece of laminate flooring has been lifted, revealing an older patterned vinyl floor and beneath it old wooden parquet, removed skirting board on the floor, natural light, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SOLLENTUNA
"golvlaggare-sollentuna.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Sollentuna", "svc_label": "Golvläggare",
  "title": "Golvläggare i Sollentuna – golv i radhus och villor",
  "description": "Golvläggare i Sollentuna: golv i radhus i Sjöberg och villor i Tureberg, golvvärme och när ingrepp i bjälklaget kräver anmälan. Gratis platsbesök.",
  "h1": "Golvläggare i Sollentuna",
  "lead": "I Sollentuna bor många i villa eller radhus, i allt från tidiga 1900-talsvillor nära stationerna till radhusgrupper från 1970- och 80-talen. Golvjobben varierar därefter. Geal Entreprenad AB lägger nya golv, slipar trägolv och planerar golvvärme i hela Sollentuna, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Radhus i Sjöberg och villor nära stationerna.",
  "sections": [
    {"id": "stationerna", "anchor": "Husen i Sollentuna",
     "h2": "Från järnvägsstationerna till Sjöbergs radhus",
     "paras": [
       "Sollentunas översiktsplan beskriver hur järnvägen mellan Stockholm och Uppsala byggdes 1866, med Rotebro som första station. I början av 1900-talet anlades stationer i Tureberg och Norrviken, senare även i Helenelund och Häggvik, och det var då man började bygga småhus och villor. Översiktsplanen vill att Sollentuna bevarar den prägel av villastad som växte fram under 1900-talets första hälft.",
       "Sjöberg är ett exempel på en senare utbyggnad. Enligt översiktsplanen styckades de första villatomterna av redan på 1920-talet, men området präglades fram till 1960-talet av skog och fritidsbebyggelse. Den stora utbyggnaden skedde under 70-, 80- och 90-talen, med en blandning av villor, radhus och flerbostadshus.",
     ],
     "aside": {"title": "Golvjobb vi ser i Sollentuna", "items": [
       "Slipning i äldre villor", "Nytt golv i hela radhusplanet",
       "Golv mot betong i nedre plan", "Golvvärme i kök och hall"]}},
    {"id": "radhusplanet", "h2": "Ett golv genom hela radhusplanet",
     "paras": [
       "I ett radhus från 1970- eller 80-talet är bottenplanet ofta en sammanhängande yta med hall, kök och vardagsrum. Det gör det lockande att lägga samma golv överallt. Det är också det jobb som kräver mest planering, eftersom köksskåp, trappa och dörrkarmar ska anpassas samtidigt och ett flytande golv över en stor yta behöver rörelsefogar på rätt ställen.",
       "Ligger bottenplanet på betong behöver fukten kontrolleras innan något läggs. Golvbranschen rekommenderar att bjälklagets relativa fuktighet kontrolleras innan avjämningsmassan läggs, och att underliggande betong har nått den nivå som golvet kräver. Mätningen görs av en fuktkontrollant inom RBK, och vi samordnar den åt dig.",
     ],
     "aside": None},
    {"id": "bjalklag-sollentuna", "h2": "När ingrepp i bjälklaget kräver anmälan",
     "paras": [
       "Sollentuna kommun skriver att den som vill göra ändringar som påverkar den bärande konstruktionen, till exempel ingrepp i en takstol eller i ett bjälklag, behöver göra en anmälan och få startbesked. Till anmälan hör plan- och sektionsritning, konstruktionsritningar och ett förslag till kontrollplan, och vid mer omfattande arbeten även en kontrollansvarig.",
       "Ett vanligt golvbyte rör inte bjälklaget. Annorlunda blir det om bjälkar ska kapas för en ny trappa, sänkas för att få plats med golvvärme eller förstärkas för att bära ett tungt stengolv. Vi bedömer vid besöket om det du vill göra hamnar där, och lägger i så fall in tiden för anmälan i tidplanen.",
     ],
     "aside": {"title": "Kan kräva anmälan", "items": [
       "Kapade bjälkar för ny trappa", "Sänkt bjälklag för golvvärme",
       "Förstärkning för stengolv", "Borttagen bärande vägg"]}},
    {"id": "golvvarme-sollentuna", "h2": "Golvvärme i ett befintligt hus",
     "paras": [
       "Golvvärme i hall, kök eller badrum är en vanlig önskan när golvet ändå ska bytas. Elektrisk golvvärme byggs in i ett tunt skikt ovanpå underlaget och kopplas in av en elinstallatör. Vattenburen golvvärme kopplas till husets värmesystem och kräver mer bygghöjd, vilket i ett befintligt hus ofta betyder att golvet blir högre eller att underlaget behöver göras om.",
       "Vilket golv som passar ovanpå beror på systemet. Klinker leder värmen bra, medan trägolv och parkett ska vara avsedda för golvvärme enligt tillverkarens anvisningar. Vi tar fram ett förslag där golv, underlag och värmesystem hänger ihop och samordnar med elektriker eller rörläggare för de delar som kräver det.",
     ],
     "aside": None},
    {"id": "villa-sollentuna", "h2": "Trägolv i de äldre villorna",
     "paras": [
       "I villorna från 1900-talets första hälft finns ofta trägolv kvar i vardagsrum och sovrum, ibland under en senare matta. De kan slipas fram och få ny yta. Var försiktig med att slipa ett golv som redan har slipats många gånger; vi mäter hur mycket trä som finns kvar och föreslår en lättare behandling om marginalen är liten.",
       "I ett radhus delar du dessutom vägg med grannen, och ett hårt golv kan göra stegljud och skrapande stolar tydligare både hos dig och hos dem. Ett underlag som dämpar ljudet och filtar under möblerna gör stor skillnad. Läs mer om golvtyper och slipning på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången för golvet i Sollentuna",
  "steps": [
    ("Besök", "Vi mäter ytor och höjder, tittar på underlaget och går igenom dina önskemål om golvvärme."),
    ("Bedömning", "Vi säger om något i förslaget rör bjälklaget och kräver anmälan till kommunen."),
    ("Kostnadsförslag", "Arbete, material, fuktmätning och eventuella installatörer står på egna rader."),
    ("Förberedelse", "Möbler flyttas, gamla golv tas bort och fukten mäts där golvet ligger på betong."),
    ("Läggning", "Underlag, eventuell golvvärme och nytt golv läggs, med anpassade trösklar och lister."),
    ("Överlämning", "Vi städar, går igenom golvet och lämnar skötselråd."),
  ],
  "rot_h2": "Rotavdrag för golvläggning i Sollentuna",
  "rot": [
    "Skatteverket räknar golvläggning och golvslipning som rotarbete i ett småhus som du äger och bor i. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Bara arbetskostnaden ger avdrag, inte golvmaterial eller resor. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Sollentuna?",
  "price": [
    "Ytans storlek, hur mycket som ska rivas och om underlaget behöver riktas styr mest. Golvvärme, fuktmätning och anpassning av trappor och köksskåp tillkommer om de ingår. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi få samma golv i hela bottenplanet i vårt radhus i Sjöberg?",
     "Oftast ja. Det kräver planering kring trappa, köksskåp och dörrar, och ett flytande golv över en stor yta behöver rörelsefogar. Vi visar var de hamnar innan vi beställer."),
    ("Behöver vi anmäla till Sollentuna kommun om vi sänker bjälklaget för golvvärme?",
     "Ja, kommunen kräver anmälan och startbesked för ingrepp i bjälklag. Ett vanligt golvbyte utan ingrepp i bjälkarna kräver ingen anmälan."),
    ("Vilken golvvärme passar när vi byter golv i köket i en villa i Norrviken?",
     "Elektrisk golvvärme tar minst bygghöjd. Vattenburen kopplas till husets värmesystem och kräver mer höjd. Vi går igenom båda alternativen vid besöket."),
    ("Kan vi lägga trägolv på golvvärme i vårt hus i Sollentuna?",
     "Det går med ett golv som tillverkaren anger är avsett för golvvärme. Vi följer tillverkarens anvisningar för läggning och för hur värmen ska ställas in."),
    ("Vem mäter fukten i betongplattan innan nytt golv läggs i radhuset?",
     "En fuktkontrollant inom RBK. Vi bokar och samordnar mätningen så att resultatet finns innan golvet köps in."),
  ],
  "sources": [
    ("Sollentuna kommun – Översiktsplan för Sollentuna med sikte på 2040 (pdf)",
     "https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/oversiktsplan/oversiktsplan-for-sollentuna-med-sikte-pa-2040.pdf"),
    ("Sollentuna kommun – Ändring av bärande konstruktion",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/andring-av-barande-konstruktion/"),
    _GBR_U, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i radhuset eller villan i Sollentuna bytas?", "Boka ett gratis platsbesök så går vi igenom underlag, golvvärme och golvval på plats."),
  "img": [
    ("Nylagt ljust ekgolv genom hall och vardagsrum i ett radhus från 1970-talet i Sollentuna",
     "interior of an empty ground floor in a 1970s Swedish terraced house, newly laid light oak plank floor running continuously from the entrance hall into the living room, simple wooden staircase with white painted sides, large window to a small garden with birch trees, white walls, soft daylight, no people, no text"),
    ("Nylagt grått klinkergolv i hallen i ett radhus i Sollentuna",
     "newly laid matte light grey large format ceramic floor tiles with thin grey grout lines in the empty entrance hall of a 1970s Swedish terraced house, white painted walls, simple white front door with small window, a light oak floor visible through the opening to the living room, clean, natural daylight, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TYRESÖ
"golvlaggare-tyreso.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Tyresö", "svc_label": "Golvläggare",
  "title": "Golvläggare i Tyresö – golv i omgjorda fritidshus",
  "description": "Golvläggare i Tyresö: golv i fritidshus som blivit villor, nivåskillnader mot tillbyggnaden, krypgrund och radon när golvet öppnas. Gratis platsbesök.",
  "h1": "Golvläggare i Tyresö",
  "lead": "Många hus i Tyresö började som fritidshus och har blivit villor genom tillbyggnader i flera omgångar. Golven berättar ofta den historien, med olika höjder, underlag och material från rum till rum. Geal Entreprenad AB lägger nya golv, slipar gamla och rättar till underlaget i hela Tyresö, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Fritidshus som byggts om till villor.",
  "sections": [
    {"id": "fritidshusen", "anchor": "Husen i Tyresö",
     "h2": "Godsmark som blev fritidshus och sedan villor",
     "paras": [
       "Tyresö kommuns planbeskrivning för Fasanvägen etapp 13 berättar att Brevikshalvön tillhörde Tyresögodset från medeltiden fram till 1930. Under 1930–1950-talen styckades stora arealer av för fritidshus, och sedan 1990-talet har antalet åretruntboende ökat. Kommunen har beslutat att bejaka omvandlingen från fritidshusområde till område för permanentboende.",
       "I planområdet finns 119 bostadsfastigheter. Planbeskrivningen konstaterar att husen genom tillbyggnader och ombyggnationer har anpassats efter dagens standard och enskilda behov, och att bebyggelsen varierar från enklare fritidshus till moderna medelstora och större villor. Den ursprungliga karaktären av sommarstugeområde är särskilt väl bevarad i den södra delen.",
     ],
     "aside": {"title": "Typiskt i ett ombyggt fritidshus", "items": [
       "Olika golvhöjd i gammal och ny del", "Flera lager golv på varandra",
       "Svikt mellan glest lagda bjälkar", "Kalla golv mot ytterväggen"]}},
    {"id": "stuga-och-tillbyggnad", "h2": "Där stugan möter tillbyggnaden",
     "paras": [
       "När en stuga från 1940-talet har fått en tillbyggnad från 1990-talet ligger de två delarna sällan på samma höjd eller på samma slags underlag. Ofta är det just i övergången som golvet knarrar, spricker eller har en tröskel som ingen tycker om. Ska golvet bli sammanhängande behöver underlaget i den lägre delen byggas upp och skarven mellan de två bjälklagen överbryggas.",
       "Ibland är det bättre att låta delarna få var sitt golv och en tydlig gräns, till exempel vid en dörröppning. Vi mäter höjder och svikt i båda delarna och visar dig vad respektive lösning innebär, så att beslutet bygger på hur huset faktiskt ser ut. Dörrarnas frigång, trappor och anslutningen mot altandörren avgör ofta vilken höjd golvet kan få, och därför mäter vi dem innan materialet väljs.",
     ],
     "aside": None},
    {"id": "krypgrund-tyreso", "h2": "Golvet ovanpå en krypgrund",
     "paras": [
       "Står huset på krypgrund vilar golvbjälklaget på låga murar med ett luftutrymme mot marken. Boverket skriver att framför allt den uteluftsventilerade krypgrunden med träbjälklag ofta drabbas av fuktskador. På våren och sommaren kyls varm, fuktig uteluft ned i den kallare grunden, och fukten kan ge skador på bjälklagets undersida. Luft rör sig dessutom ofta mellan grunden och bostaden.",
       "Innan vi lägger ett nytt golv på ett sådant bjälklag vill vi veta hur det mår underifrån. Finns det lukt, missfärgningar eller lös isolering är det grunden som behöver åtgärdas först. Ett nytt golv ovanpå ett fuktigt bjälklag döljer bara problemet.",
     ],
     "aside": {"title": "Kontrollera i krypgrunden", "items": [
       "Lukt av mögel eller jord", "Fläckar på bjälklagets undersida",
       "Vatten vid grundmuren", "Lös eller fuktig isolering"]}},
    {"id": "radon-tyreso", "h2": "Radon i marken och i huset",
     "paras": [
       "Planbeskrivningen bedömer att marken i Fasanvägens planområde är av normalrisktyp när det gäller markradon, och att nya bostäder ska byggas radonskyddade. Boverket rekommenderar att den som bygger om eller till sitt hus mäter radon, under eldningssäsongen oktober till april och under minst två, helst tre månader.",
       "Vid ett golvbyte i ett befintligt hus är det framför allt golv som ligger direkt mot marken och genomföringar för rör som påverkar hur luft från marken tar sig in. Har huset inte mätts på länge kan det vara klokt att mäta innan ett större golvarbete och sedan igen när det är klart.",
     ],
     "aside": None},
    {"id": "naturtomt", "h2": "Golv som tål en naturtomt",
     "paras": [
       "Planbeskrivningen lyfter fram naturtomterna, där husen ligger direkt i skogen utan anlagda gräsmattor. Det är fint att bo så, men barr, grus och sand följer med in på skorna. I hall och vid altandörren håller ett tåligt golv bättre, till exempel klinker eller ett trägolv med en hård lack, medan sovrum och vardagsrum kan få en mjukare oljad yta.",
       "Vi föreslår gärna en tydlig zon innanför entrén där golvet tål mer, och en övergång som ligger där den inte syns. Mer om material och ytbehandlingar finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett golvjobb till i Tyresö",
  "steps": [
    ("Besök", "Vi mäter höjder i alla delar av huset, känner efter svikt och tittar ner i krypgrunden om det går."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag där underlag, golv och eventuella åtgärder på grunden står var för sig."),
    ("Planering", "Vi bestämmer ordningen mellan rummen och om radon- eller fuktmätning behövs först."),
    ("Underlag", "Gamla golv tas bort, bjälklag riktas och nivåskillnader byggs upp."),
    ("Läggning", "Nytt golv läggs eller gamla brädor slipas, med lister och trösklar anpassade efter dörrarna."),
    ("Avslut", "Vi går igenom golvet och lämnar råd om skötsel."),
  ],
  "rot_h2": "ROT-avdrag för golv i Tyresö",
  "rot": [
    "Skatteverket räknar golvläggning och golvslipning som rotarbete, i villa och i fritidshus som du äger och använder. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Material och resor ingår inte. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Tyresö?",
  "price": [
    "Nivåskillnader mellan husets delar, bjälklagets skick och hur många gamla lager som ska bort påverkar mest. Behöver grunden åtgärdas innan golvet läggs blir det ett eget moment. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Golvet i vårt hus på Brevikshalvön har en tröskel mellan stugan och tillbyggnaden – går den att ta bort?",
     "Ofta går det, genom att bygga upp underlaget i den lägre delen och överbrygga skarven. Ibland är en tydlig gräns vid en dörr bättre. Vi mäter och visar alternativen."),
    ("Kan ni lägga nytt golv om det luktar unket från krypgrunden?",
     "Då vill vi först veta varför. Boverket varnar för fuktskador i uteluftsventilerade krypgrunder, och ett nytt golv ovanpå ett fuktigt bjälklag löser inte problemet."),
    ("När ska vi mäta radon om golvet i vår villa i Tyresö ska bytas?",
     "Boverket rekommenderar mätning under oktober till april, i minst två månader. Mät gärna före ett större golvarbete och igen när det är klart."),
    ("Vilket golv passar i hallen när tomten är en naturtomt med barr och grus?",
     "Ett tåligt golv som klinker eller trä med hård lack. Vi föreslår ofta en slitzon innanför entrén och en mjukare yta i övriga rum."),
    ("Gäller rotavdraget för golv i fritidshuset i Tyresö som vi inte bor i året om?",
     "Ja, Skatteverket ger rotavdrag även för fritidshus som du äger och använder. Avdraget gäller arbetskostnaden."),
  ],
  "sources": [
    ("Tyresö kommun – Planbeskrivning, detaljplan för Fasanvägen etapp 13 (pdf)",
     "https://www.tyreso.se/download/18.38176aff18b5b7301f888ab9/1698683875432/Planbeskrivning%20Fasanv%C3%A4gen%20etapp%2013.pdf"),
    _BOV_KRYP, _BOV_MAT, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i huset i Tyresö göras om?", "Boka ett gratis platsbesök så mäter vi höjder och tittar på underlaget innan du bestämmer dig."),
  "img": [
    ("Nylagt brett trägolv i ett ombyggt fritidshus bland tallar i Tyresö",
     "interior of an empty living room in an extended old Swedish summer cottage turned year-round home, newly laid wide light pine floorboards, white painted wooden panel walls, low ceiling with exposed beams, glazed door to a wooden deck, view of tall pine trees and granite rock, soft daylight, Stockholm archipelago area, no people, no text"),
    ("Övergång mellan två golvnivåer vid en dörröppning i ett ombyggt hus",
     "close-up of a doorway in an old Swedish wooden house where an older worn wooden floor meets a slightly higher newer floor section, a simple solid oak threshold bridging the step, white painted door frame, natural light, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VÄRMDÖ
"golvlaggare-varmdo.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Värmdö", "svc_label": "Golvläggare",
  "title": "Golvläggare på Värmdö – golv när fritidshuset blir helårshus",
  "description": "Golvläggare på Värmdö: golv i fritidshus som blir permanentbostäder, vattenburen golvvärme vid byte till bergvärme och äldre bruksbostäder i Gustavsberg.",
  "h1": "Golvläggare på Värmdö",
  "lead": "På Värmdö väljer allt fler att bo året om i hus som byggdes för sommaren. Det är ofta golvet som först avslöjar att huset inte var tänkt för vintern. Geal Entreprenad AB lägger nya golv, slipar gamla och rättar till underlaget på hela Värmdö, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Fritidshus som blir permanentbostäder.",
  "sections": [
    {"id": "forandringsomraden", "anchor": "Husen på Värmdö",
     "h2": "Tusentals fritidshus blir permanentbostäder",
     "paras": [
       "Värmdö kommuns broschyr Fritidshusområde i förändring beskriver hur fler och fler väljer att bosätta sig permanent i kommunens fritidshusområden. Många av dem ska planläggas och få kommunalt vatten och avlopp, och det handlar om tusentals fastigheter. De områden som först ska anpassas kallas prioriterade förändringsområden och pekas ut i översiktsplanen Värmdö 2035.",
       "Planprocessen pågår enligt kommunen normalt i två till tre år. Först när detaljplanen har fått laga kraft och vatten och avlopp är utbyggt kan man söka bygglov enligt den nya planen. För golvet spelar det mindre roll, eftersom invändiga golvarbeten inte kräver lov. Men den som planerar en större ombyggnad gör klokt i att samordna golvet med det som kommer senare, så att inget behöver rivas upp igen.",
     ],
     "aside": {"title": "Inför permanentboendet", "items": [
       "Kalla golv mot ytterväggarna", "Svikt i gamla bjälklag",
       "Nya VA-ledningar under golvet", "Byte av uppvärmning"]}},
    {"id": "kalla-golv", "h2": "Varför sommarhusets golv är kallt",
     "paras": [
       "Ett golv i ett hus som användes några månader om året behövde inte hålla värmen i januari. Bjälklaget kan vara sparsamt isolerat, och golvbrädorna ligger ibland direkt på bjälkarna utan något mellanskikt. När huset värms upp hela vintern blir golven kalla och glipor öppnar sig mellan brädorna när luften blir torr.",
       "Ett nytt golv ovanpå löser sällan kylan på egen hand. Vid platsbesöket tittar vi på hur bjälklaget är byggt och om det går att komma åt underifrån. Ibland är det rimligt att ta upp golvet, se över isoleringen och sedan lägga tillbaka brädorna eller ett nytt golv. Då blir det också möjligt att dra nya rör eller kablar innan golvet stängs. Gamla brädor som tas upp märks och läggs åt sidan, så att de kan läggas tillbaka i samma ordning om de är i gott skick.",
     ],
     "aside": None},
    {"id": "bergvarme-golv", "h2": "Bergvärme och vattenburen golvvärme",
     "paras": [
       "Kommunens riktlinjer för förändringsområdena säger att det inom varje fastighet ska finnas plats för bland annat parkering, ett eventuellt attefallshus och bergvärme. För många som går från sommarhus till helårshus blir uppvärmningen en av de större frågorna.",
       "Byter du till ett vattenburet system är det värt att fundera på golvvärme i samma veva, särskilt om golven ändå ska tas upp. Vattenburen golvvärme kräver mer bygghöjd än en elmatta, och golvet ovanpå ska vara avsett för golvvärme enligt tillverkarens anvisningar. Vi planerar underlag och golv tillsammans med den som installerar värmesystemet, så att höjder och trösklar stämmer.",
     ],
     "aside": {"title": "Samordna med värmesystemet", "items": [
       "Bygghöjd för slingor och isolering", "Golv avsett för golvvärme",
       "Fördelare och styrning", "Tidplan för installatören"]}},
    {"id": "gustavsberg-golv", "h2": "Golv i Gustavsbergs äldre bostäder",
     "paras": [
       "En antikvarisk konsekvensanalys från 2023 sammanfattar riksintresset Gustavsberg som ett brukssamhälle med industriell verksamhet från tidigt 1800-tal till 1970-talet, präglat av 1800-talets patriarkaliska industrisamhälle och 1900-talets moderna bruks- och mönstersamhälle. De tidigaste bruksgatorna från det sena 1800-talet ligger närmast Farstaviken, och längre ut finns bostäder från 1900-talet, ofta inbäddade i grönska.",
       "I äldre trähus kan breda brädgolv finnas kvar under senare mattor. Har de legat dolda länge är de ofta i bättre skick än man tror. Vi tar upp en bit vid en tröskel, bedömer brädorna och föreslår att slipa och laga om det är rimligt, hellre än att riva. Mer om slipning finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "logistik-varmdo", "h2": "Golvjobb långt från fastlandsvägen",
     "paras": [
       "Ett golvjobb på en ö utan bro kräver att material, verktyg och avfall planeras in i förväg, eftersom allt ska fraktas fram och tillbaka. Golvmaterial behöver dessutom ofta ligga inne i huset en tid innan läggning, så att det hinner anpassa sig till rummets klimat. Det gör att leveransen behöver komma i god tid.",
       "Vi går igenom transporter och tidplan vid platsbesöket och skriver in dem i kostnadsförslaget, så att du vet vad som ingår innan arbetet börjar.",
     ],
     "aside": None},
  ],
  "steps_h2": "Golvjobbet på Värmdö steg för steg",
  "steps": [
    ("Platsbesök", "Vi tittar på golv och bjälklag, mäter höjder och går igenom planer på uppvärmning och VA."),
    ("Förslag", "Du får ett skriftligt kostnadsförslag med underlag, golv och transporter på egna rader."),
    ("Samordning", "Vi bestämmer ordningen med eventuell rörläggare, elektriker eller värmeinstallatör."),
    ("Rivning och underlag", "Gamla golv tas bort, bjälklaget ses över och underlaget riktas."),
    ("Läggning eller slipning", "Nytt golv läggs eller gamla brädor slipas och behandlas."),
    ("Avslut", "Vi tar med oss avfallet, går igenom golvet och lämnar skötselråd."),
  ],
  "rot_h2": "Rotavdrag för golv på Värmdö",
  "rot": [
    "Rotavdraget gäller både permanentbostad och fritidshus som du äger och använder. Att lägga nytt golv eller slipa ett gammalt räknas som rotarbete, och avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Golvmaterial och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden på Värmdö?",
  "price": [
    "Bjälklagets skick, om golvet behöver tas upp för isolering eller nya ledningar och hur materialet ska fraktas till huset påverkar mest. Golvvärme och samordning med andra hantverkare tillkommer om de ingår. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vi ska bo året om i vårt fritidshus på Värmdö – hjälper ett nytt golv mot kylan?",
     "Sällan på egen hand. Kylan kommer oftast från bjälklaget. Vi tittar på hur det är byggt och föreslår om golvet bör tas upp och isoleringen ses över först."),
    ("Behövs bygglov för att byta golv i ett hus i ett förändringsområde på Värmdö?",
     "Nej, invändiga golvarbeten kräver inte bygglov. Lovfrågan blir aktuell först för till- och nybyggnader enligt den nya detaljplanen."),
    ("Ska vi lägga in vattenburen golvvärme när vi byter till bergvärme?",
     "Det kan vara ett bra tillfälle om golven ändå tas upp. Det kräver mer bygghöjd än en elmatta. Vi planerar höjder och golvval tillsammans med installatören."),
    ("Kan det gamla brädgolvet i vårt hus i Gustavsberg slipas?",
     "Ofta går det, om brädorna är hela och tjocka nog. Vi tar upp en bit vid en tröskel och bedömer dem innan vi föreslår slipning eller lagning."),
    ("Hur gör ni med golvmaterial till ett hus på en ö utan bro?",
     "Vi planerar transport med båt eller färja i förväg och låter materialet ligga inne i huset innan läggning. Transporterna står i kostnadsförslaget."),
  ],
  "sources": [
    ("Värmdö kommun – Fritidshusområde i förändring, del 1 Planering (pdf, 2023)",
     "https://www.varmdo.se/download/18.52346f71869c9938611c2df/1678200543391/Broschyr%20PFO%20del%201%20-%20uppdaterad%202023.pdf"),
    ("Värmdö kommun – Antikvarisk konsekvensanalys, Gustavsberg (pdf, 2023)",
     "https://varmdo.se/download/18.3dd2ab3d18c629ae56f50ed/1702902627509/Antikvarisk%20konsekvensanalys%20AIX%202023-09-27.pdf"),
    _SKV, _SKV2,
  ],
  "cta": ("Ska golven i huset på Värmdö klara vintern?", "Boka ett gratis platsbesök så tittar vi på golv och bjälklag och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat brädgolv i ett ljust rum i ett skärgårdshus på Värmdö",
     "interior of an empty bright room in an old red wooden Swedish archipelago house on Värmdö, freshly sanded wide pine floorboards with a matte white oiled finish, white painted tongue and groove walls, small paned window with view of the Baltic sea, rocks and pine trees, soft daylight, no people, no text"),
    ("Upptaget golv med synliga bjälkar och ny isolering i ett äldre fritidshus",
     "opened floor in an empty room of an old Swedish wooden summer house under renovation, a few straight parallel wooden floor joists running in one direction only, clean yellow mineral wool insulation batts fitted neatly between the joists, the rest of the room still with old pine floorboards, a tidy stack of removed boards against the white panelled wall, natural light, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HANINGE
"golvlaggare-haninge.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Haninge", "svc_label": "Golvläggare",
  "title": "Golvläggare i Haninge – egnahem, sportstugor och souterräng",
  "description": "Golvläggare i Haninge: trägolv i egnahem i Tungelsta och Vendelsö, golv i sportstugor och fritidshus som byggs om, och golv i souterrängvåningen.",
  "h1": "Golvläggare i Haninge",
  "lead": "Haninge har egnahem längs Nynäsbanan, sportstugor nära vattnet och fritidshus som håller på att bli villor. Golven i husen har legat olika länge och på olika underlag. Geal Entreprenad AB lägger nya golv, slipar gamla och rättar till underlaget i hela Haninge, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Egnahem, sportstugor och hus i sluttning.",
  "sections": [
    {"id": "tungelsta", "anchor": "Husen i Haninge",
     "h2": "Småbruken i Tungelsta och villorna längs Nynäsbanan",
     "paras": [
       "Haninges karaktärsmiljöer, en del av kommunens kulturmiljöprogram, beskriver hur småhusen främst växte fram längs Nynäsbanan, som invigdes 1901. Särskilt för Haninge är Tungelsta, där AB Egna hem köpte upp flera stora gårdar och styckade dem för att sälja till arbetarklassen. Villkoret var att köparen drev ett småbruk med jordbruk eller växthus, och Tungelsta blev ett centrum för handelsträdgårdar.",
       "Egnahemsområdena från 1910–1940-talen finns i Tungelsta, Vendelsö, Vendelsömalm, Handen, Västerhaninge och Norrby. De första villorna präglas av jugend och nationalromantik, som senare övergick i nyklassicism och tidig funkis, och tongivande är träpanel, enkelt spröjsade fönster och tegeltäckta sadel- eller brutna tak.",
     ],
     "aside": {"title": "I ett egnahem från 1910–40-talen", "items": [
       "Trägolv under senare mattor", "Rum som byggts till i omgångar",
       "Bjälklag som satt sig", "Höjdskillnad mot köket"]}},
    {"id": "egnahem-golv", "h2": "Trägolvet i egnahemmet",
     "paras": [
       "I ett hus som har haft samma golv i hundra år har brädorna ofta slitits ojämnt, med nötta stråk vid dörrar och spis och mindre slitna ytor under möblerna. Det betyder inte att golvet är slut. Med en försiktig grundslipning, några utbytta brädor och en ny yta kan det se nästan nytt ut utan att tappa sin ålder.",
       "Har golvet målats eller fått en matta limmad direkt på brädorna krävs mer förarbete. Vi prövar på en liten yta hur färgen eller limmet släpper innan vi lovar något om resultatet, och skriver in förarbetet som en egen post i kostnadsförslaget.",
       "Ett egnahem som har byggts till i omgångar har ofta rum på olika höjd, där köket eller en senare tillbyggnad ligger något högre än hallen. Vi mäter nivåerna i hela planet innan vi väljer golv, så att övergångarna blir få och hamnar vid dörröppningar i stället för mitt i ett rum. Det gör också att dörrarna inte behöver kapas mer än nödvändigt.",
     ],
     "aside": None},
    {"id": "sportstugor", "h2": "Sportstugor och fritidshus i byggsats",
     "paras": [
       "Karaktärsmiljöerna pekar ut sportstugorna från 1920–1950-talen som små och enkla volymer i naturen, ofta med röda fasader och vita knutar. Exempel är Årsta havsbad, Vendelsö, Hermanstorp, Norrby och skärgården. Fritidshusområdena från andra halvan av 1900-talet byggdes mer rationellt, ofta med prefabricerade byggsatser och stugor i liknande utförande.",
       "Att husen i ett sådant område är byggda på samma sätt gör det lättare att förutse vad som finns under golvet. Men små stugor har ofta tunna bjälklag och golv som ligger tätt mot marken. Vi tittar på svikt och fukt innan vi föreslår ett tyngre golv, och väljer gärna ett lättare golv om underlaget inte är byggt för mer.",
     ],
     "aside": None},
    {"id": "omvandling-haninge", "h2": "När den gamla stugan blir en extra bostad",
     "paras": [
       "I omvandlingsområden som Hermanstorp, Norrby och Kolartorp börjar sommarstugorna permanentas. Kommunens råd är att ett befintligt fritidshus med fördel kan sparas som en extra lägenhet om en ny huvudbyggnad uppförs på tomten. Då får stugan ett nytt liv, och golvet behöver klara mer än en sommar i taget.",
       "Ett golv i en gäststuga eller extra bostad ska tåla vardag men inte nödvändigtvis se ut som i huvudbyggnaden. Ett slipat och oljat brädgolv kan ofta behållas. Är golvet för skadat lägger vi ett nytt som passar stugans skala, och ser till att övergången mot våtrum och entré blir tät och tålig.",
     ],
     "aside": {"title": "Stugan som extra bostad", "items": [
       "Behåll brädgolvet om det går", "Tålig yta vid entrén",
       "Tät övergång mot våtrummet", "Lättare golv på tunt bjälklag"]}},
    {"id": "souterrang", "h2": "Golv i souterräng och källarplan",
     "paras": [
       "För nya hus i omvandlingsområdena råder kommunen att större nivåskillnader på tomten tas upp med förhöjd sockel, souterräng- eller källarvåning. Det innebär att många hus har ett nedre plan som delvis ligger mot marken, ofta med golv på betong.",
       "Golvbranschen rekommenderar att fukten i bjälklaget kontrolleras innan avjämningsmassa läggs, så att den inte överstiger vad ytskiktet tål. Vi ser till att mätningen görs i god tid och väljer golv efter resultatet. Våtrum i nedre planet hör till badrumsrenoveringen. Mer om golvtyper finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi golv i Haninge",
  "steps": [
    ("Platsbesök", "Vi tittar på golvet, provar svikten och ser om det ligger på trä eller betong."),
    ("Provyta", "På ett gammalt golv provar vi slipning eller borttagning av färg och lim på en liten yta."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där förarbete, golv och fuktmätning står var för sig."),
    ("Förarbete", "Gamla mattor och lim tas bort, brädor lagas och underlaget riktas."),
    ("Läggning eller slipning", "Golvet slipas och behandlas eller ett nytt läggs, med trösklar och lister anpassade."),
    ("Genomgång", "Vi går igenom golvet med dig och lämnar skötselråd."),
  ],
  "rot_h2": "Rotavdrag för golv i Haninge",
  "rot": [
    "Golvläggning och golvslipning ger rotavdrag i småhus och fritidshus som du äger och använder. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Material och resor ingår inte. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Haninge?",
  "price": [
    "Hur mycket förarbete golvet kräver, om brädor behöver bytas och om underlaget ligger på trä eller betong styr mest. I nedre plan tillkommer fuktmätning och avjämning. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan det hundra år gamla trägolvet i vårt egnahem i Tungelsta slipas?",
     "Ofta går det. Slitna stråk vid dörrar och spis går att jämna ut, och enstaka brädor kan bytas. Vi mäter tjockleken och provslipar en liten yta först."),
    ("Golvet i vår stuga i Årsta havsbad är målat – går det att få fram träet?",
     "Ibland. Det beror på färgtyp och hur djupt den sitter. Vi provar på en liten yta och visar resultatet innan vi föreslår hela golvet."),
    ("Vi bygger nytt på tomten i Norrby och sparar stugan – vilket golv passar där?",
     "Ett slipat och oljat brädgolv kan ofta behållas. Annars väljer vi ett golv som passar stugans skala och klarar året runt."),
    ("Hur gör ni med golvet i ett souterrängplan mot marken i Haninge?",
     "Golvet ligger oftast på betong, och fukten kontrolleras innan något läggs. Vi väljer golv och underlag efter mätresultatet."),
    ("Klarar en liten fritidsstuga från 1970-talet ett klinkergolv?",
     "Det beror på bjälklaget. Små stugor har ofta tunna bjälklag, och då föreslår vi ett lättare golv eller en förstärkning som vi bedömer på plats."),
  ],
  "sources": [
    ("Haninge kommun – Haninges karaktärsmiljöer, kulturmiljöprogram (pdf)",
     "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf"),
    _GBR_U, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i huset i Haninge slipas eller bytas?", "Boka ett gratis platsbesök så provar vi golvet på plats och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Slipat trägolv i ett ljust rum i ett egnahem från 1920-talet i Haninge",
     "interior of an empty room in a 1920s Swedish wooden egnahem villa, freshly sanded and lightly oiled old pine floorboards with natural wear marks near the door, white painted panelled door, simple white skirting, small paned window with view of an old apple tree garden, soft daylight, no people, no text"),
    ("Liten röd sportstuga med vita knutar bland tallar nära vattnet",
     "small old red painted Swedish wooden sports cottage from the 1930s with white corners and a small porch, standing on a natural plot among pine trees and granite rocks near a calm bay, Stockholm archipelago, summer, no people, no text"),
  ],
  "related": [],
},

}
