# -*- coding: utf-8 -*-
"""Tjänster v29 (2026-10-27): snickare på Kungsholmen, i Vasastan, på Östermalm och i Skärholmen,
målare i Skärholmen, golvläggare i Kista och Sundbyberg, fasadrenovering i Kista.
Lokala vinklar skilda från ortens befintliga sidor. Fakta endast från källorna i 'sources', öppnade 2026-10-27
(Skatteverket återställer anslutningen härifrån – samma adresser och ROT-meningar som i v23–v28).
Inga priser, garantier, recensioner, kundcase eller certifieringar."""
from tj_v29_takreno_a import SKV_ROT, SKV_RATT, OF, BL_FASAD, BL_KLASS, VARSAM, SSM, NO_PEOPLE

BRL = "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/"
RIKS = "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf"
BL_PLAN = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/andra-planlosningen-i-en-byggnad/"
BL_BARANDE = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/andra-i-barande-konstruktion/"
BL_INREKLASS = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/stadsmuseets-kulturhistoriska-klassificering/"
BL_ALTAN = "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/mur-plank-altan/"
BOV_ALTAN = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/mur-plank-altan-och-annat/"
BOV_ASBEST = "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/"
AV_ASBEST = ("https://www.av.se/halsa-och-sakerhet/kemiska-risker/risker-for-vissa-amnen-produkter-och-verksamheter/"
             "asbest/forebygg-riskerna-med-asbest/")
BOV_PLATTA = ("https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/"
              "fuktrisker-for-grund/betongplatta-mark/")
GB_AVJ = "https://www.golvbranschen.se/teknik--material/golvavjamning/uttorkning-av-golvavjamning/"
GB_LAMELL = "https://www.golvbranschen.se/teknik--material/tragolv/lamellparkett/"
GB_MASSIVA = "https://www.golvbranschen.se/teknik--material/tragolv/massiva-tragolv/"
DUVBO = ("https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/"
         "Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf")
SBG_DUVBO = "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/duvbo"
BOV_UTANLOV = "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/andra-fasad-eller-tak/"

ROT_BRF = ("Bor du i bostadsrätt ger arbete inne i lägenheten rotavdrag enligt "
           f'<a class="text-link" href="{SKV_ROT}" rel="noopener">Skatteverket</a>, för det som du själv ansvarar för '
           "enligt stadgarna – väggar, golv, tak och fast inredning innanför lägenhetens gränser. Avdraget är 30 procent "
           "av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med rutavdrag.")
ROT_SMAHUS = ("Äger du ett småhus ger arbetet rotavdrag när du bor i huset eller har det som fritidshus. Avdraget är 30 "
              "procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor tillsammans med "
              f'rutavdrag, enligt <a class="text-link" href="{SKV_ROT}" rel="noopener">Skatteverket</a>.')
ROT_END = "Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan."

PAGES_TJ = {}

# ======================================================== SNICKARE PÅ KUNGSHOLMEN
PAGES_TJ["snickare-kungsholmen.html"] = {
    "kind": "district", "service": "snickare", "ort": "Kungsholmen", "svc_label": "Snickare",
    "title": "Snickare på Kungsholmen – förvaring i små lägenheter",
    "description": "Snickare på Kungsholmen: platsbyggd förvaring, garderober och sovalkover i små lägenheter, "
                   "vad styrelsen måste godkänna och ROT i bostadsrätt.",
    "h1": "Snickare på Kungsholmen",
    "lead": "Mer än två av tre lägenheter på Kungsholmen har högst två rum och kök. När ytan är liten är det "
            "snickeriet som gör skillnaden: en garderob som går ända upp till taket, en bänk med lådor under, "
            "en sovalkov som får plats där det förut var en hörna. Vi mäter, ritar och bygger på plats – och "
            "tar reda på vad föreningen behöver godkänna innan vi börjar.",
    "card": "Förvaring och platsbyggt i små lägenheter.",
    "sections": [
        {"id": "lagenheter", "anchor": "Lägenheterna", "h2": "Små lägenheter i en stad av föreningar",
         "paras": [
             "Stadens statistik för 2024 visar 42 420 lägenheter i flerbostadshus på Kungsholmen. 5 265 saknar "
             "eget kök, 11 314 är ettor och 12 505 är tvåor. Tillsammans är det mer än två av tre lägenheter.",
             "30 598 av stadsdelens bostäder är bostadsrätter. Det betyder att de flesta som vill bygga om något "
             "inne i lägenheten har en styrelse att stämma av med – åtminstone när ändringen går utöver ytskikt "
             "och lösa möbler."],
         "aside": {"title": "Kungsholmen (2024)",
                   "items": ["42 420 lägenheter i flerbostadshus", "5 265 utan eget kök",
                             "11 314 ettor och 12 505 tvåor", "30 598 bostadsrätter"]}},
        {"id": "forvaring", "h2": "Förvaring som byggs för rummet",
         "paras": [
             "En färdig garderob har standardmått, men väggarna i ett äldre hus är sällan raka och takhöjden "
             "varierar. En platsbyggd garderob mäts mot rummet och kan gå ända upp till taket, runt en "
             "fönsternisch eller in under en snedtakshörna. I en liten lägenhet är det ofta de sista 40 "
             "centimetrarna under taket som ger mest förvaring.",
             "Vi bygger också sängar på hög höjd med förvaring under, bänkar med lådor i hallen och hyllor i "
             "nischer. Allt byggs i stommar som skruvas fast i väggen, så att det kan monteras ner igen om du "
             "flyttar och nästa ägare vill ha det på ett annat sätt."]},
        {"id": "funkis", "h2": "Funkislägenheterna i Fredhäll och Kristineberg",
         "paras": [
             "Omkring 1930 byggdes nya stadsdelar efter funktionalismens ideal, i innerstaden framför allt i "
             "utkanterna som Fredhäll och Kristineberg. Fristående huskroppar med öppna gröna gårdar blev idealet, "
             "och lägenheterna planerades för ljus och luft snarare än för många rum.",
             "I sådana lägenheter är väggarna mellan rummen ofta tunna och ytorna noga utnyttjade från början. "
             "Innan vi flyttar en garderob eller bygger in en alkov tar vi reda på vad väggen består av och om det "
             "går ledningar i den. Det gör vi från ritningar när föreningen har dem och genom att undersöka "
             "väggen på plats."]},
        {"id": "styrelsen", "anchor": "Styrelsen", "h2": "Det styrelsen måste godkänna",
         "paras": [
             "Enligt "
             f'<a class="text-link" href="{BRL}" rel="noopener">bostadsrättslagen</a> (7 kap. 7 §) behöver du '
             "styrelsens tillstånd för ingrepp i en bärande konstruktion, ändring av ledningar för avlopp, värme, "
             "gas eller vatten, ändring av ventilation, ändring som påverkar brandskyddet och annan väsentlig "
             "förändring av lägenheten.",
             "En garderob som skruvas fast i en vägg kräver normalt inget tillstånd. Det gör däremot en ny vägg "
             "som påverkar ventilationen – till exempel en sovalkov som stänger in ett rum utan eget "
             "ventilationsdon. Staden skriver att man inte behöver göra en anmälan om planlösningen ändras inom "
             f'lägenheten utan att några tekniska egenskapskrav påverkas, men <a class="text-link" href="{BL_PLAN}" '
             'rel="noopener">i en bostadsrätt behövs tillstånd från föreningen</a> för de anmälningspliktiga '
             "ändringarna."]},
        {"id": "luft", "h2": "Glöm inte luften och ljuset",
         "paras": [
             "En inbyggd garderob framför ett ventilationsdon eller en alkov utan luftväg till resten av rummet "
             "ger instängd luft. Vi planerar snickerierna så att tilluft och frånluft fortsätter att fungera, med "
             "springor, galler eller avstånd där det behövs.",
             "Samma sak gäller ljuset. I en lägenhet med fönster bara åt ett håll ska en ny vägg eller ett högt "
             "skåp inte stänga ute dagsljuset från resten av bostaden. Ofta räcker ett glasparti överst i en "
             "alkovvägg för att rummet bakom ska få ljus."]},
    ],
    "steps_h2": "Så går ett snickeriuppdrag på Kungsholmen till",
    "steps": [
        ("Besök", "Gratis besök där vi mäter rummet och går igenom vad du vill få plats med."),
        ("Ritning", "Skiss med mått, material och var ventilation och el finns."),
        ("Styrelsen", "Vi visar vad som behöver föreningens tillstånd och tar fram underlag."),
        ("Tillverkning", "Stommar och luckor kapas efter rummets mått."),
        ("Montering", "Allt monteras och justeras på plats, med skydd i trapphuset."),
        ("Genomgång", "Vi går igenom resultatet och städar efter oss."),
    ],
    "rot_h2": "ROT-avdrag för snickeri i bostadsrätten",
    "rot": [ROT_BRF + " " + ROT_END,
            "Material som garderobsstommar, luckor och beslag ger inget avdrag, bara arbetet."],
    "price_h2": "Vad påverkar priset på Kungsholmen?",
    "price": ["Måtten och antalet luckor och lådor, materialet, hur ojämna väggarna är, om el eller ventilation "
              "berörs och om styrelsen behöver underlag. Efter besöket får du ett skriftligt kostnadsförslag."],
    "faq": [
        ("Behöver jag styrelsens tillstånd för en platsbyggd garderob?",
         "Normalt inte, om den bara skruvas fast i väggen och inte påverkar ventilation, ledningar eller bärande "
         "delar. Är du osäker visar vi vad som gäller innan arbetet börjar."),
        ("Kan ni bygga en sovalkov i min etta på Kungsholmen?",
         "Ofta ja. Vi planerar alkoven så att ljus och luft når båda sidor. Påverkar den ventilationen behövs "
         "styrelsens tillstånd enligt bostadsrättslagen."),
        ("Får jag rotavdrag för en inbyggd garderob?",
         "Ja, för arbetet, om det görs i den del av lägenheten som du själv ansvarar för. Materialet ger inget avdrag."),
        ("Mina väggar är sneda – går det ändå att bygga till taket?",
         "Ja. Platsbyggda stommar mäts mot rummet och anpassas med lister och passbitar mot väggar och tak."),
    ],
    "sources": [
        ("Stockholms stad – Områdesfakta Kungsholmens stadsdelsområde (2025)",
         OF + "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade.pdf"),
        ("Stockholms stad – Riksintressen i översiktsplanen", RIKS),
        ("Riksdagen – Bostadsrättslag (1991:614)", BRL),
        ("Stockholms stad – Ändra planlösningen i en byggnad", BL_PLAN),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "cta": ("Behöver lägenheten på Kungsholmen mer förvaring?",
            "Boka ett gratis besök, så mäter vi upp och visar vad som får plats innan du får ett skriftligt kostnadsförslag."),
    "img": [
        ("Platsbyggd vit garderob från golv till tak i ett litet sovrum",
         "small bright bedroom in an older Stockholm apartment with a custom built white floor-to-ceiling wardrobe "
         "fitted exactly between the walls, simple panel doors with slim handles, wooden floor, window with "
         "daylight" + NO_PEOPLE),
        ("Bänk med lådor och hyllor i en hallnisch",
         "custom built wooden bench with deep drawers and open shelves above, fitted into a hallway niche of an "
         "older apartment, painted light grey, coat hooks, wooden floor, soft daylight" + NO_PEOPLE),
        ("Sovalkov med glasparti överst i en etta",
         "studio apartment with a new low partition wall forming a sleeping alcove, a row of glass panes along the "
         "top of the wall letting daylight through, white painted woodwork, bed visible behind, calm interior"
         + NO_PEOPLE),
    ],
}

# ======================================================== SNICKARE I VASASTAN
PAGES_TJ["snickare-vasastan.html"] = {
    "kind": "district", "service": "snickare", "ort": "Vasastan", "svc_label": "Snickare",
    "title": "Snickare i Vasastan – öppna upp mellan rummen",
    "description": "Snickare i Vasastan: öppna upp mellan kök och vardagsrum, bärande väggar, anmälan, styrelsens "
                   "tillstånd och lister som passar lägenheten.",
    "h1": "Snickare i Vasastan",
    "lead": "Många som köper en äldre lägenhet i Vasastan vill öppna upp – mellan köket och vardagsrummet eller "
            "mellan två små rum. Det är snickarens jobb, men först måste någon ta reda på om väggen bär. Vi "
            "hjälper dig från ritning och styrelsens tillstånd till nya foder, dörröppningar och lister som "
            "passar lägenheten.",
    "card": "Öppna upp, nya dörröppningar och listverk.",
    "sections": [
        {"id": "lagenheter", "anchor": "Lägenheterna", "h2": "Lägenheter i stenstad och storgårdskvarter",
         "paras": [
             "Stadens statistik för 2024 visar 12 579 bostäder i Västra Matteus och 8 889 i Gustav Vasa, två av "
             "Vasastans statistikområden. Tvåor är vanligast i Västra Matteus, och de flesta bostäderna är "
             "bostadsrätter – 8 990 i Västra Matteus och 5 707 i Gustav Vasa.",
             "Husen är från olika tider. Stora delar är stenstad från perioden 1870–1930, och i Röda Bergen och kvarteren Motorn "
             "och Vingen byggdes på 1910- och 1920-talen nya kvarter med friare planformer och gårdar. Väggarna "
             "mellan rummen är byggda på olika sätt i olika hus, och det är just det som avgör vad som går att "
             "ta bort."],
         "aside": {"title": "Vasastan (2024)",
                   "items": ["Västra Matteus: 12 579 bostäder", "Gustav Vasa: 8 889 bostäder",
                             "8 990 respektive 5 707 bostadsrätter"]}},
        {"id": "barande", "anchor": "Bärande vägg", "h2": "Bär väggen eller inte?",
         "paras": [
             "Staden skriver att du behöver göra en anmälan och invänta startbesked om ändringen påverkar "
             "byggnadens bärande konstruktion. Ritningar kan ge en bild av hur huset är byggt, men staden "
             "påpekar att de kan vara ofullständiga och att det inte är säkert att byggarna följde dem.",
             "Staden kan inte heller bedöma åt dig om en vägg bär. Därför tar vi in en konstruktör när det finns "
             "minsta tvekan. Bär väggen kan öppningen ofta ändå göras, men med en balk och en anmälan – och med "
             "styrelsens tillstånd. Äldre handlingar kan du själv hitta och skriva ut via "
             f'<a class="text-link" href="{BL_BARANDE}" rel="noopener">stadsbyggnadskontoret</a>.']},
        {"id": "styrelsen", "anchor": "Styrelsen", "h2": "Styrelsen före sågen",
         "paras": [
             "Enligt bostadsrättslagen (7 kap. 7 §) får du inte göra ingrepp i en bärande konstruktion, ändra "
             "ledningar eller ventilation eller göra någon annan väsentlig förändring utan styrelsens tillstånd. "
             "Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet för föreningen, och "
             "tillståndet kan förenas med villkor.",
             "Vi tar fram en enkel ritning som visar vad som ska göras, vilka ledningar som finns i väggen och hur "
             "golv och tak lagas efter öppningen. Det brukar göra styrelsens beslut enklare och snabbare."]},
        {"id": "lister", "h2": "Foder, lister och dörrar som passar huset",
         "paras": [
             "När en vägg tas bort syns det i golvet, i taket och på väggarna intill. Golvet får en skarv där väggen "
             "stod, taklisten tar slut mitt i rummet och dörrfodren på andra sidan passar inte längre. Det är "
             "detaljerna som avgör om öppningen ser ut att ha funnits där från början.",
             "Vi tar fram lister och foder med samma profil som lägenhetens befintliga, eller låter tillverka dem "
             "när de inte går att köpa. Golvskarven läggs med samma material, och taklisten förlängs eller avslutas "
             "på ett sätt som passar rummet."]},
        {"id": "inget", "h2": "Ändringar som inte kräver anmälan",
         "paras": [
             "Allt kräver inte anmälan. Staden skriver att man inte behöver anmäla en ändring av planlösningen inom "
             "en lägenhet om inga tekniska egenskapskrav påverkas, till exempel om man flyttar eller bygger ut "
             "kök eller badrum eller ändrar hur rummen används.",
             "Att sätta in en ny dörr i en icke-bärande vägg, bygga en garderob eller byta innerdörrar kräver "
             "alltså oftast bara styrelsens godkännande om det påverkar något av det som räknas upp i "
             f'bostadsrättslagen. Läs stadens sida om att <a class="text-link" href="{BL_PLAN}" rel="noopener">ändra '
             "planlösningen</a> innan du bestämmer dig."]},
    ],
    "steps_h2": "Så öppnar vi upp en lägenhet i Vasastan",
    "steps": [
        ("Besök", "Gratis besök där vi tittar på väggen, golvet och taket."),
        ("Ritningar", "Vi hämtar äldre handlingar och tar vid behov in en konstruktör."),
        ("Tillstånd", "Underlag till styrelsen och anmälan till staden om väggen bär."),
        ("Rivning", "Väggen rivs med dammskydd och skydd i trapphuset."),
        ("Lagning", "Balk vid behov, golvskarv, tak och väggar lagas."),
        ("Snickerier", "Foder, lister och dörrar i samma profil som lägenheten."),
    ],
    "rot_h2": "ROT-avdrag för snickeri i Vasastan",
    "rot": [ROT_BRF + " " + ROT_END,
            "Stadens avgift för en anmälan ger inget avdrag."],
    "price_h2": "Vad påverkar priset i Vasastan?",
    "price": ["Om väggen bär, hur stor öppningen blir, vad som finns i väggen, hur golv och tak ska lagas och hur "
              "mycket listverk och foder som behöver tillverkas. Du får ett skriftligt kostnadsförslag efter besöket."],
    "faq": [
        ("Hur vet jag om väggen i min lägenhet i Vasastan är bärande?",
         "Ritningar ger en första bild, men staden påpekar att de kan vara ofullständiga. Vid tvekan tar vi in en "
         "konstruktör som bedömer väggen på plats."),
        ("Behöver jag göra en anmälan för att riva en vägg?",
         "Ja, om väggen påverkar husets bärande konstruktion. Då ska du göra en anmälan och vänta på startbesked "
         "innan arbetet börjar."),
        ("Kan styrelsen säga nej?",
         "Bara om åtgärden är till påtaglig skada eller olägenhet för föreningen, enligt bostadsrättslagen. "
         "Tillståndet kan förenas med villkor."),
        ("Går det att få tag på lister som passar en sekelskifteslägenhet?",
         "Ofta ja, och annars kan de tillverkas efter en bit av den befintliga listen så att profilen blir densamma."),
    ],
    "sources": [
        ("Stockholms stad – Ändra i bärande konstruktion", BL_BARANDE),
        ("Stockholms stad – Ändra planlösningen i en byggnad", BL_PLAN),
        ("Riksdagen – Bostadsrättslag (1991:614)", BRL),
        ("Stockholms stad – Riksintressen i översiktsplanen", RIKS),
        ("Stockholms stad – Områdesfakta Västra Matteus (2025)", OF + "inre-staden/norra-innerstaden/vastra-matteus.pdf"),
        ("Stockholms stad – Områdesfakta Gustav Vasa (2025)", OF + "inre-staden/norra-innerstaden/gustav-vasa.pdf"),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ],
    "cta": ("Vill du öppna upp lägenheten i Vasastan?",
            "Boka ett gratis besök, så tittar vi på väggen och visar vad som krävs innan du får ett skriftligt kostnadsförslag."),
    "img": [
        ("Öppning mellan kök och vardagsrum i en äldre lägenhet",
         "bright older Stockholm apartment where a wide new opening connects the kitchen and the living room, "
         "white painted wooden architraves matching the old ones, herringbone parquet floor running through, "
         "high ceiling with cornice, daylight" + NO_PEOPLE),
        ("Profilerade taklister och dörrfoder i en sekelskifteslägenhet",
         "close view of profiled white wooden ceiling cornice and a traditional panelled door with wide moulded "
         "architrave in a 1900s apartment, soft daylight on the details" + NO_PEOPLE),
        ("Golvskarv lagad med samma parkett där en vägg har tagits bort",
         "close view of an oak parquet floor where a strip of matching new parquet fills the line of a removed "
         "wall, neatly fitted and finished, skirting boards on both sides" + NO_PEOPLE),
    ],
}

# ======================================================== SNICKARE PÅ ÖSTERMALM
PAGES_TJ["snickare-ostermalm.html"] = {
    "kind": "district", "service": "snickare", "ort": "Östermalm", "svc_label": "Snickare",
    "title": "Snickare på Östermalm – laga snickerier med kulturvärde",
    "description": "Snickare på Östermalm: lagning av dörrar, paneler och fasta snickerier i äldre våningar, "
                   "kulturvärden i lägenheten och styrelsens tillstånd.",
    "h1": "Snickare på Östermalm",
    "lead": "I en våning på Östermalm är snickerierna ofta lika gamla som huset: spegeldörrar, paneler, "
            "foder och inbyggda skåp. De går oftast att laga, och det är oftast både billigare och "
            "bättre än att byta. Vi reparerar, kompletterar och bygger nytt där det behövs – och tar reda på "
            "om lägenhetens kulturvärden kräver styrelsens tillstånd först.",
    "card": "Lagning av dörrar, paneler och fasta snickerier.",
    "sections": [
        {"id": "hus", "anchor": "Husen", "h2": "Stenstad, villor och föreningar",
         "paras": [
             "Stenstaden på Östermalm uppfördes till största delen under 1800-talets senare del och är, tillsammans "
             "med Norrmalm, den största samlade årsringen i stadens bebyggelse. I Hedvig Eleonora, ett av "
             "Östermalms statistikområden, fanns 2024 7 344 bostäder, varav 5 164 bostadsrätter.",
             "Östermalm har också villaområden. Lärkstaden byggdes 1909–1918 med tegelhus och planterade förgårdar, "
             "och Diplomatstaden fick på 1910- och 1920-talen stora enfamiljshus runt Engelska kyrkan. I husen "
             "från den här tiden finns ofta originalsnickerier kvar."],
         "aside": {"title": "Hedvig Eleonora (2024)",
                   "items": ["7 344 bostäder", "5 164 bostadsrätter", "11 bostäder i småhus"]}},
        {"id": "laga", "anchor": "Laga", "h2": "Laga hellre än byta",
         "paras": [
             "En gammal spegeldörr i massivt trä som kärvar har oftast bara satt sig eller fått för många lager "
             "färg i kanten. Den kan justeras, hyvlas och få nya gångjärn eller ett nytt lås. En panel som har "
             "spruckit kan limmas och kompletteras med en bit i samma profil.",
             "Vi tar ner det som behöver lagas, märker varje del och sätter tillbaka allt på samma plats. Saknas "
             "en list eller en panelbit tillverkas den efter den befintliga. Det nya ska inte synas när det är "
             "målat."]},
        {"id": "kulturvarde", "h2": "Lägenheter med kulturvärden",
         "paras": [
             "Bostadsrättslagen (7 kap. 7 §) säger att det alltid krävs styrelsens tillstånd för en åtgärd som "
             "påverkar en lägenhets särskilda historiska, kulturhistoriska, miljömässiga eller konstnärliga "
             "värden. Det gäller alltså även sådant som annars inte hade behövt något tillstånd.",
             "Stadsmuseet klassar byggnader och miljöer, och staden skriver att den som äger en byggnad med "
             "särskilda kulturhistoriska värden kan behöva söka bygglov för åtgärder som annars är lovfria. "
             f'Titta i <a class="text-link" href="{BL_INREKLASS}" rel="noopener">Stadsmuseets klassificeringskarta</a> '
             "och fråga styrelsen innan något originalsnickeri rivs."]},
        {"id": "nytt", "h2": "När något nytt ska byggas",
         "paras": [
             "Ska en ny garderob, bokhylla eller dörr in i en äldre våning försöker vi få den att höra ihop med "
             "det som finns: samma typ av foder runt, samma höjd på socklar och lister och en kulör som passar.",
             "Ibland är det bättre att det nya syns som nytt – en enkel, väl utförd inredning som inte försöker "
             "härma. Det avgör du, men vi visar alternativen innan något tillverkas."]},
        {"id": "villor", "h2": "Villorna i Lärkstaden och Diplomatstaden",
         "paras": [
             "Staden beskriver villorna i Lärkstaden och Diplomatstaden som omsorgsfullt utformade, med stor omsorg "
             "i materialbehandlingen. Diplomatstaden skyddas genom miljöbalkens bestämmelser om nationalstadspark, "
             "och större delen av Lärkstaden omfattas av en detaljplan från 1952.",
             "I en villa gäller samma princip som i en våning: laga det som finns, komplettera med samma profil "
             "och stäm av med staden innan något på husets utsida ändras. Inne i huset är det ägaren som "
             "bestämmer, så länge inga skyddsbestämmelser säger något annat."]},
    ],
    "steps_h2": "Så arbetar vi med snickerier på Östermalm",
    "steps": [
        ("Besök", "Gratis besök där vi går igenom dörrar, paneler och listverk."),
        ("Klassning", "Vi kollar Stadsmuseets karta och om styrelsens tillstånd behövs."),
        ("Dokumentation", "Delar fotograferas och märks innan de tas ner."),
        ("Lagning", "Justering, hyvling, limning och nya beslag."),
        ("Komplettering", "Saknade delar tillverkas i samma profil."),
        ("Återmontering", "Allt sätts tillbaka på sin plats, klart för målning."),
    ],
    "rot_h2": "ROT-avdrag för snickeri på Östermalm",
    "rot": [ROT_BRF + " " + ROT_END,
            "I en villa ger arbetet rotavdrag när du äger och bor i huset."],
    "price_h2": "Vad påverkar priset på Östermalm?",
    "price": ["Hur många dörrar och paneler som ska lagas, hur mycket som måste tillverkas nytt, om beslag ska bytas "
              "och om arbetet ska samordnas med målaren. Efter besöket får du ett skriftligt kostnadsförslag."],
    "faq": [
        ("Mina gamla spegeldörrar kärvar – måste de bytas?",
         "Sällan. De kan oftast justeras, hyvlas och få nya gångjärn. Det är ofta färglager i kanterna som "
         "gör att de tar emot."),
        ("Behöver jag styrelsens tillstånd för att ta bort en gammal panel?",
         "Om lägenheten har särskilda kulturhistoriska värden krävs alltid tillstånd för en åtgärd som påverkar "
         "dem, enligt bostadsrättslagen. Fråga styrelsen innan något rivs."),
        ("Kan ni tillverka en list som inte finns att köpa?",
         "Ja. Vi tar en bit av den befintliga listen som mall och låter tillverka nya med samma profil."),
        ("Får jag rotavdrag för att laga dörrar och paneler?",
         "Ja, för arbetet, när det görs i den del av lägenheten som du ansvarar för enligt stadgarna."),
    ],
    "sources": [
        ("Riksdagen – Bostadsrättslag (1991:614)", BRL),
        ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (ändra inomhus)", BL_INREKLASS),
        ("Stockholms stad – Riksintressen i översiktsplanen", RIKS),
        ("Stockholms stad – Områdesfakta Hedvig Eleonora (2025)", OF + "inre-staden/norra-innerstaden/hedvig-eleonora.pdf"),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "cta": ("Har du snickerier som behöver lagas?",
            "Boka ett gratis besök, så går vi igenom dörrar, paneler och listverk och lämnar ett skriftligt kostnadsförslag."),
    "img": [
        ("Spegeldörrar och paneler i en äldre våning",
         "elegant late 19th century Stockholm apartment interior with tall white double panelled doors, wooden wall "
         "panelling below a dado rail, ornate ceiling cornice and a herringbone parquet floor, soft daylight from "
         "tall windows" + NO_PEOPLE),
        ("Gammal spegeldörr lutad mot väggen under renovering",
         "old white panelled interior door lying on two wooden trestles in a protected room, new brass hinges and a "
         "small hand plane resting beside it, dust sheets on the floor" + NO_PEOPLE),
        ("Lagad trädetalj med ny bit i samma profil",
         "close view of an old profiled wooden skirting board where a new piece with exactly the same profile has "
         "been fitted, primed and ready for paint, older wooden floor" + NO_PEOPLE),
    ],
}

# ======================================================== SNICKARE I SKÄRHOLMEN
PAGES_TJ["snickare-skarholmen.html"] = {
    "kind": "district", "service": "snickare", "ort": "Skärholmen", "svc_label": "Snickare",
    "title": "Snickare i Skärholmen – altan och plank vid radhuset",
    "description": "Snickare i Skärholmen: altan, plank och förråd vid radhus i Bredäng, Sätra och Vårberg, "
                   "lovfria mått och grannens skriftliga medgivande.",
    "h1": "Snickare i Skärholmen",
    "lead": "Nästan alla småhus i Skärholmen är radhus och kedjehus som ägs av de boende. Den lilla tomten "
            "bakom huset är där snickaren gör mest nytta: en altan i nivå med vardagsrummet, ett plank som "
            "skyddar mot insyn och ett förråd för cyklar och trädgårdsmöbler. Vi bygger dem så att de håller "
            "måtten för lovfria åtgärder och passar husgruppen.",
    "card": "Altan, plank och förråd vid radhuset.",
    "sections": [
        {"id": "radhus", "anchor": "Radhusen", "h2": "Radhusen i Bredäng, Sätra och Vårberg",
         "paras": [
             "Bredäng började byggas 1962 och var den första stadsdelen i Stockholm som planerades i stor skala, "
             "följd av Sätra. En stor del av bebyggelsen blev radhus och kedjehus, byggda i grupper med enhetlig "
             "gestaltning och noga komponerad färgsättning.",
             "Stadens statistik för 2024 visar 1 991 småhus i Skärholmens stadsdelsområde, varav 1 976 med "
             "äganderätt. Tomterna är små, och grannen finns nära – vilket påverkar både vad som får byggas "
             "och hur."],
         "aside": {"title": "Skärholmens småhus (2024)",
                   "items": ["1 991 småhus", "1 976 med äganderätt", "Vårberg 580, Sätra 538, Bredäng 322"]}},
        {"id": "altan", "anchor": "Altan", "h2": "Altanen och måtten",
         "paras": [
             "Enligt Boverket krävs inget bygglov för en altan inom detaljplan om den är högst 1,8 meter över marken "
             "och ligger inom 3,6 meter från huset, eller högst 1,2 meter över marken och ligger längre bort. "
             "Ska altanen byggas närmare tomtgränsen än 4,5 meter behövs grannens medgivande, och det ska alltid "
             "vara skriftligt.",
             "På en radhustomt är det sällan altanen blir hög, men gränsen mot grannen ligger oftast inom "
             "4,5 meter. Vi ritar därför en enkel skiss som grannen kan skriva under, med altanens mått och "
             "placering. Ändras markens höjd med mer än en halv meter inom detaljplan krävs dessutom marklov, "
             "enligt staden."]},
        {"id": "plank", "h2": "Plank och insynsskydd",
         "paras": [
             "Ett plank inom detaljplan kräver inget bygglov om det är högst 1,8 meter och står inom 3,6 meter från "
             "huset, eller högst 1,2 meter längre bort. Står planket på en altan eller mur räknas höjden för hela "
             "konstruktionen, från marken utanför. Närmare gränsen än 4,5 meter behövs grannens skriftliga "
             "medgivande.",
             "Ett vanligt staket och en pergola med glest lagda ribbor kräver enligt Boverket inget bygglov alls. "
             "Ibland räcker det för att få den avskildhet man vill ha."]},
        {"id": "gruppen", "h2": "Bygg så att det passar husgruppen",
         "paras": [
             "Även när en altan eller ett plank är lovfritt ska det anpassas till omgivningen och inte innebära en "
             "betydande olägenhet för grannarna. I Skärholmen, där husen i varje grupp byggdes lika, syns det "
             "tydligt om ett plank får en helt annan färg eller höjd än grannarnas.",
             "Staden räknar Bredäng som kulturhistoriskt värdefull miljö. Det är ett skäl till att välja samma "
             "kulör och liknande utförande som grannarna, och att titta i detaljplanen innan något byggs."]},
        {"id": "forrad", "h2": "Förråd och skärmtak",
         "paras": [
             "Ett förråd för cyklar och trädgårdsmöbler kan byggas som en del av planket eller fristående. Vilka "
             "regler som gäller beror på storlek och placering, och vi stämmer av mot detaljplanen och stadens "
             f'regler innan vi bygger. Stadens sida om <a class="text-link" href="{BL_ALTAN}" rel="noopener">mur, '
             "plank och altan</a> är en bra början.",
             "Virket till altan, plank och förråd ska tåla väder. Vi väljer material efter läget och lämnar råd om "
             "underhåll, så att det du bygger håller i många år."]},
    ],
    "steps_h2": "Så bygger vi vid radhuset i Skärholmen",
    "steps": [
        ("Besök", "Gratis besök där vi mäter tomten och tittar på grannarnas utförande."),
        ("Regler", "Vi kontrollerar mått, detaljplan och om marklov behövs."),
        ("Skiss", "Ritning med mått och placering som grannen kan skriva under."),
        ("Grund", "Plintar och reglar placeras och riktas in."),
        ("Bygget", "Altan, plank eller förråd byggs och skruvas."),
        ("Genomgång", "Vi går igenom resultatet och lämnar råd om underhåll."),
    ],
    "rot_h2": "ROT-avdrag för altan och plank",
    "rot": ["Rotavdrag gäller arbete på bostaden och vissa arbeten på tomten. Vilka arbeten med altan, plank och "
            f'förråd som räknas framgår av <a class="text-link" href="{SKV_RATT}" rel="noopener">Skatteverkets lista</a>, '
            "och vi skriver i kostnadsförslaget vad som gäller för ditt arbete.",
            "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år. " + ROT_END],
    "price_h2": "Vad påverkar priset i Skärholmen?",
    "price": ["Altanens eller plankets storlek, höjd och material, hur marken ser ut, om befintliga konstruktioner ska "
              "rivas och hur nära grannen det byggs. Efter besöket får du ett skriftligt kostnadsförslag."],
    "faq": [
        ("Behöver jag bygglov för en altan vid mitt radhus i Sätra?",
         "Inte om den håller måtten: högst 1,8 meter hög inom 3,6 meter från huset eller högst 1,2 meter längre "
         "bort. Närmare gränsen än 4,5 meter behövs grannens skriftliga medgivande."),
        ("Räcker det att grannen säger ja muntligt?",
         "Nej. Boverket skriver att grannemedgivandet alltid ska vara skriftligt, till exempel som underskrift "
         "på en ritning."),
        ("Hur högt får planket vara?",
         "Högst 1,8 meter inom 3,6 meter från huset och högst 1,2 meter längre bort, om du vill bygga utan "
         "bygglov inom detaljplan. Står det på en altan räknas hela höjden från marken."),
        ("Får jag välja en annan färg på planket än grannarna?",
         "Det är inte förbjudet i sig, men det ska passa omgivningen. I husgrupper som byggts lika rekommenderar "
         "vi samma kulör som grannarna."),
    ],
    "sources": [
        ("Boverket – Mur, plank, altan och annat", BOV_ALTAN),
        ("Stockholms stad – Mur, plank och altan", BL_ALTAN),
        ("Stockholms stad – Varsam utveckling av småhus- och villaområden", VARSAM),
        ("Stockholms stad – Områdesfakta Skärholmens stadsdelsområde (2025)",
         OF + "soderort/skarholmen/skarholmen-stadsdelsomrade.pdf"),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
        ("Skatteverket – Arbeten som ger rätt till rotavdrag", SKV_RATT),
    ],
    "cta": ("Vill du ha en altan eller ett plank vid radhuset?",
            "Boka ett gratis besök, så mäter vi tomten och tar fram en skiss innan du får ett skriftligt kostnadsförslag."),
    "img": [
        ("Låg trätrall bakom ett radhus med plank mot grannen",
         "small back garden of a Swedish 1960s terraced house with a new low wooden deck level with the patio door "
         "and a stained wooden privacy fence along the boundary to the neighbour, potted plants, lawn, summer"
         + NO_PEOPLE),
        ("Mörkgrått plank i trä mot grannen",
         "close view of a new vertical board privacy fence stained dark grey with even gaps, sturdy posts and a "
         "simple top rail, garden behind, daylight" + NO_PEOPLE),
        ("Litet förråd i trä i änden av en radhustomt",
         "small wooden garden shed with a pitched roof built at the end of a narrow terraced house plot, matching "
         "the fence colour, bicycles hidden inside with closed door, lawn and shrubs" + NO_PEOPLE),
    ],
}

# ======================================================== MÅLARE I SKÄRHOLMEN
PAGES_TJ["malare-skarholmen.html"] = {
    "kind": "district", "service": "malare", "ort": "Skärholmen", "svc_label": "Målare",
    "title": "Målare i Skärholmen – lägenheten, trapphuset och radhuset",
    "description": "Målare i Skärholmen: lägenhet, trapphus och radhus – vem som ansvarar för ytorna och gamla "
                   "material i hus från 1960- och 70-talen.",
    "h1": "Målare i Skärholmen",
    "lead": "I Skärholmen bor man i hyresrätt, bostadsrätt och egna radhus, och det avgör vem som beställer "
            "målningen. Medlemmen i en bostadsrättsförening ansvarar för lägenhetens ytor, föreningen för "
            "trapphuset och radhusägaren för allt. Vi målar väggar, tak och snickerier – och kontrollerar "
            "gamla ytor innan vi slipar i hus från miljonprogrammets tid.",
    "card": "Lägenheter, trapphus och radhus.",
    "sections": [
        {"id": "boende", "anchor": "Boendet", "h2": "Tre sätt att bo – tre beställare",
         "paras": [
             "Stadens statistik för 2024 visar 16 620 bostäder i Skärholmens stadsdelsområde. 3 912 tillhör "
             "allmännyttan och 7 394 är övriga hyresrätter. 3 338 är bostadsrätter, och 1 976 ligger i småhus "
             "som ägs med äganderätt.",
             "Det betyder att målning här beställs av tre olika slags kunder. Hyresvärden målar sina lägenheter, "
             "bostadsrättshavaren sin lägenhet och föreningen de gemensamma utrymmena. Radhusägaren bestämmer "
             "själv över hela huset."],
         "aside": {"title": "Skärholmen (2024)",
                   "items": ["16 620 bostäder", "11 306 hyresrätter, varav 3 912 allmännyttan",
                             "3 338 bostadsrätter", "1 976 småhus med äganderätt"]}},
        {"id": "ansvar", "anchor": "Ansvaret", "h2": "Vem ansvarar för väggarna?",
         "paras": [
             f'Enligt <a class="text-link" href="{BRL}" rel="noopener">bostadsrättslagen</a> (7 kap. 12 §) ska '
             "bostadsrättshavaren på egen bekostnad hålla lägenheten i gott skick, om inte stadgarna säger något "
             "annat. Väggar, tak och snickerier inne i lägenheten är alltså normalt ditt ansvar – och din "
             "beställning.",
             "Trapphus, tvättstuga och andra gemensamma utrymmen är föreningens. Där är det styrelsen som beställer, "
             "och arbetet planeras så att de boende kan ta sig in och ut medan färgen torkar."]},
        {"id": "gamla", "h2": "Gamla ytor i hus från 1960- och 70-talen",
         "paras": [
             "Bredäng började byggas 1962 och Sätra strax efter, och stora delar av Skärholmen är byggda under "
             "1960- och 1970-talen. Boverket skriver att asbest förbjöds inom byggsektorn 1982 och att det främst "
             "är byggnader från 1940–1970 som innehåller asbest, men att det kan finnas även i andra hus.",
             "Så länge materialet sitter fast och inte bearbetas är det ingen fara. Det är när det slipas, borras "
             "eller rivs som fibrer kan frigöras. Innan vi slipar ner gamla spacklade ytor eller tar bort gamla "
             "väggbeklädnader frågar vi därför efter husets historia och tar prov vid minsta tvekan."]},
        {"id": "radhus", "h2": "Radhusets insida",
         "paras": [
             "I ett radhus från 1960- eller 1970-talet har väggarna ofta målats om i flera omgångar. Ytan kan se "
             "hel ut, men gamla lager kan släppa när ny färg läggs på. Vi tvättar, provmålar en bit och spacklar "
             "där det behövs innan hela väggen målas.",
             "Trappor, dörrar och fönsterbänkar slits mer än väggarna och behöver en färg som tål det. Vi väljer "
             "färg efter ytan: en för väggar, en annan för snickerier och en för våtare utrymmen som tvättstuga "
             "och hall."]},
        {"id": "trapphus", "h2": "Trapphuset i föreningen",
         "paras": [
             "Ett trapphus målas i etapper så att det går att ta sig förbi under hela arbetet. Vi sätter upp information i "
             "förväg, skyddar golv och räcken och målar dörrar och väggar i en ordning som gör att varje del hinner "
             "torka.",
             "Styrelsen får ett skriftligt kostnadsförslag efter ett gratis besök, med de ytor som ska målas, "
             "kulörerna och en tidsplan som kan sättas upp i trapphuset."]},
    ],
    "steps_h2": "Så lägger vi upp målningen i Skärholmen",
    "steps": [
        ("Besök", "Gratis besök där vi tittar på ytorna och vem som beställer."),
        ("Kontroll", "Vi frågar efter husets historia och tar prov vid tvekan."),
        ("Förslag", "Skriftligt kostnadsförslag med ytor, kulörer och tidsplan."),
        ("Förarbete", "Tvätt, spackling och provmålning."),
        ("Målning", "Väggar, tak och snickerier med rätt färg för varje yta."),
        ("Avslut", "Städning och genomgång."),
    ],
    "rot_h2": "ROT-avdrag för målning i Skärholmen",
    "rot": [ROT_BRF + " " + ROT_END,
            ROT_SMAHUS + " Föreningens trapphus ger inget rotavdrag."],
    "price_h2": "Vad påverkar priset för målning i Skärholmen?",
    "price": ["Ytornas storlek och skick, hur mycket som behöver spacklas, antalet dörrar och snickerier, om prov "
              "behöver tas och om arbetet görs i ett bebott trapphus. Du får ett skriftligt kostnadsförslag."],
    "faq": [
        ("Vem betalar målningen i min bostadsrätt i Skärholmen?",
         "Du, i regel. Bostadsrättslagen säger att bostadsrättshavaren håller lägenheten i gott skick på egen "
         "bekostnad, om inte stadgarna säger något annat."),
        ("Kan det finnas asbest i väggarna i ett hus från 1960-talet?",
         "Det kan det. Boverket skriver att främst byggnader från 1940–1970 innehåller asbest. Därför slipar vi "
         "inte gamla ytor innan vi vet vad de består av."),
        ("Hur målar ni trapphuset utan att stänga det?",
         "I etapper, med skyddat golv och information till de boende i förväg, så att det går att passera."),
        ("Får jag rotavdrag för målning av mitt radhus?",
         "Ja, för arbetskostnaden om du äger och bor i huset. Materialet ger inget avdrag."),
    ],
    "sources": [
        ("Stockholms stad – Områdesfakta Skärholmens stadsdelsområde (2025)",
         OF + "soderort/skarholmen/skarholmen-stadsdelsomrade.pdf"),
        ("Riksdagen – Bostadsrättslag (1991:614)", BRL),
        ("Stockholms stad – Varsam utveckling av småhus- och villaområden", VARSAM),
        ("Boverket – Asbest", BOV_ASBEST),
        ("Arbetsmiljöverket – Förebygg riskerna med asbest", AV_ASBEST),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ],
    "cta": ("Ska lägenheten, trapphuset eller radhuset målas?",
            "Boka ett gratis besök, så går vi igenom ytorna och lämnar ett skriftligt kostnadsförslag."),
    "img": [
        ("Nymålat vardagsrum i en lägenhet från 1960-talet",
         "freshly painted living room in a Swedish 1960s apartment with smooth light warm white walls, white "
         "painted window frame and radiator, light wooden floor partly covered with protective paper, daylight"
         + NO_PEOPLE),
        ("Trapphus med nymålade väggar och skyddat golv",
         "stairwell of a Swedish 1960s apartment building with freshly painted walls in a soft colour, stone "
         "stairs protected with paper and tape, metal handrail, daylight from a window" + NO_PEOPLE),
        ("Provmålad yta på en spacklad vägg",
         "close view of an interior wall with a small freshly painted test patch next to filled and sanded spots, "
         "a paint tray and roller resting on a dust sheet on the floor" + NO_PEOPLE),
    ],
}

# ======================================================== GOLVLÄGGARE I KISTA
PAGES_TJ["golvlaggare-kista.html"] = {
    "kind": "district", "service": "golvlaggning", "ort": "Kista", "svc_label": "Golvläggare",
    "title": "Golvläggare i Kista – nytt golv på betongplattan",
    "description": "Golvläggare i Kista: nya golv i radhus och lägenheter från 1975–80, fukt i betongplatta på "
                   "mark, uppreglade golv, avjämning och flytande parkett.",
    "h1": "Golvläggare i Kista",
    "lead": "Kistas radhus och lägenheter byggdes 1975–1980, och många golv har nu bytts en eller två gånger. "
            "I ett radhus på betongplatta är det som ligger under golvet viktigare än själva parketten: hur "
            "plattan är isolerad, hur fuktig den är och om golvet är uppreglat. Vi tar reda på det innan vi "
            "lägger nytt.",
    "card": "Nya golv på betong i radhus och lägenheter.",
    "sections": [
        {"id": "hus", "anchor": "Husen", "h2": "En stadsdel från 1975–1980",
         "paras": [
             "Staden köpte marken på Järvafältet 1966, och Kista byggdes ut under åren 1975–1980 med 2 500 "
             "lägenheter i flerbostadshus och omkring 780 småhus. Stadens statistik för 2024 visar 971 småhus i "
             "Kista, varav 482 med äganderätt och 404 bostadsrätter.",
             "Golven i husen är alltså snart 50 år gamla, och i många har de bytts under åren. Vid ett nytt "
             "golvbyte vet man därför sällan vad som ligger under det golv man ser – och det är där vi börjar."],
         "aside": {"title": "Kista (2024)",
                   "items": ["971 småhus", "482 med äganderätt", "404 bostadsrätter", "Byggt 1975–1980"]}},
        {"id": "platta", "anchor": "Betongplattan", "h2": "Betongplattan och fukten",
         "paras": [
             "Boverket beskriver hur betongplattor på mark har byggts olika genom åren. När plattor på mark "
             "infördes i bostäder i början av 1960-talet byggdes de främst med isolering ovanpå och ofta utan "
             "ångtätt skikt mot marken. Golven var vanligtvis uppreglade med isolering mellan reglarna.",
             "Med isoleringen ovanpå blir betongen nästan lika kall som marken under, och då blir fuktigheten i "
             "betongen hög. Boverket skriver att träreglar och smuts på betongytan då kan bli fuktiga och ge "
             "mikrobiell påväxt och lukt. Därför tar vi reda på hur just ditt golv är byggt innan vi föreslår "
             "något."]},
        {"id": "uppbyggnad", "h2": "Ta reda på vad som ligger under",
         "paras": [
             "Vi börjar med att lyfta en tröskel eller öppna golvet på ett ställe där det inte syns. Då ser vi om "
             "golvet är uppreglat, vad som ligger mellan reglarna och om det luktar. Finns ritningar från byggtiden "
             "tittar vi på dem också.",
             "Luktar det unket eller är reglarna fuktiga ska orsaken åtgärdas innan ett nytt golv läggs. Annars "
             "flyttar problemet bara upp i det nya golvet. Är konstruktionen torr och frisk kan ett nytt golv "
             "läggas direkt på det befintliga underlaget."]},
        {"id": "avjamning", "h2": "Avjämning och fuktmätning",
         "paras": [
             "Ska golvet läggas direkt på betong behöver ytan ofta jämnas av. Golvbranschen skiljer mellan "
             "normaltorkande och självtorkande avjämning. Den normaltorkande måste torka till den fukthalt som "
             "lim och golv kräver innan golvet läggs.",
             "Golvbranschen rekommenderar att betongens fukthalt kontrolleras innan avjämningen läggs, så att den "
             "inte är högre än vad golvet tål. Trägolv är särskilt känsliga eftersom trä tar upp fukt och sväller."]},
        {"id": "parkett", "h2": "Flytande parkett i radhuset",
         "paras": [
             "Lamellparkett består enligt Golvbranschen av två eller flera skikt där det översta är massivt trä, "
             "minst 2,5 millimeter tjockt. Skikten är limmade korsvis för att minska golvets fuktrörelser, och "
             "parketten läggs normalt flytande.",
             "I ett radhus med betongplatta läggs flytande parkett på en underlagsmatta med fuktspärr när "
             "underlaget är friskt. I hall och kök väljer vi gärna ett golv som tål vatten och grus bättre. Läs mer "
             'om <a class="text-link" href="golvlaggning.html">golvläggning</a>.']},
    ],
    "steps_h2": "Så går ett golvbyte till i Kista",
    "steps": [
        ("Besök", "Gratis besök där vi öppnar golvet på ett dolt ställe."),
        ("Underlag", "Vi ser om golvet är uppreglat och om det finns fukt eller lukt."),
        ("Förslag", "Skriftligt kostnadsförslag med underlag och golvval."),
        ("Rivning", "Det gamla golvet tas bort och sorteras."),
        ("Förarbete", "Fuktmätning, avjämning eller nytt underlag."),
        ("Läggning", "Nytt golv, trösklar och lister."),
    ],
    "rot_h2": "ROT-avdrag för golvbyte i Kista",
    "rot": [ROT_SMAHUS + " " + ROT_END,
            "Bor du i en bostadsrätt ger golvbyte inne i lägenheten rotavdrag för det som du ansvarar för enligt "
            'stadgarna. '],
    "price_h2": "Vad påverkar priset i Kista?",
    "price": ["Golvytan, vad som ligger under, om fukt eller lukt måste åtgärdas, hur mycket avjämning som behövs och "
              "vilket golv du väljer. Efter besöket får du ett skriftligt kostnadsförslag."],
    "faq": [
        ("Det luktar unket från golvet i vårt radhus i Kista – vad kan det vara?",
         "Det kan vara fukt i ett uppreglat golv på betongplatta. Boverket beskriver att sådana golv kan få "
         "mikrobiell påväxt och lukt. Vi öppnar golvet och tar reda på orsaken."),
        ("Kan nytt golv läggas ovanpå det gamla?",
         "Ibland, om underlaget är torrt, friskt och jämnt. Är det inte det måste det gamla bort först."),
        ("Varför ska betongen fuktmätas?",
         "För att golvet och limmet tål en viss fukthalt. Golvbranschen rekommenderar att fukten kontrolleras "
         "innan avjämning och golv läggs."),
        ("Passar flytande parkett i ett radhus på platta?",
         "Ja, när underlaget är friskt och en underlagsmatta med fuktspärr används."),
    ],
    "sources": [
        ("Stockholms stadsmuseum – Stockholms spår: Kista", SSM + "SSM_DOK_000080.pdf"),
        ("Stockholms stad – Områdesfakta Kista (2025)", OF + "vasterort/jarva/kista.pdf"),
        ("Boverket – Fuktrisker för betongplatta på mark", BOV_PLATTA),
        ("Golvbranschen – Uttorkning av golvavjämning", GB_AVJ),
        ("Golvbranschen – Lamellparkett", GB_LAMELL),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ],
    "cta": ("Ska golvet bytas i radhuset eller lägenheten i Kista?",
            "Boka ett gratis besök, så tittar vi under golvet innan du får ett skriftligt kostnadsförslag."),
    "img": [
        ("Nylagd ljus ekparkett i ett vardagsrum i ett radhus",
         "living room of a Swedish late 1970s terraced house with newly laid light oak floating parquet, white "
         "skirting boards, patio door to a small garden, daylight, minimal furniture" + NO_PEOPLE),
        ("Uppreglat golv på betong med reglar och isolering",
         "opened floor section in a house showing wooden joists laid on a concrete slab with mineral wool "
         "insulation between them, the old floorboards removed, a moisture meter lying on the concrete" + NO_PEOPLE),
        ("Avjämnad betongyta före golvläggning",
         "smooth grey self-levelled concrete floor surface in an empty room ready for new flooring, a roll of foam "
         "underlay with moisture barrier leaning against the wall, daylight" + NO_PEOPLE),
    ],
}

# ======================================================== GOLVLÄGGARE I SUNDBYBERG
PAGES_TJ["golvlaggare-sundbyberg.html"] = {
    "kind": "district", "service": "golvlaggning", "ort": "Sundbyberg", "svc_label": "Golvläggare",
    "title": "Golvläggare i Sundbyberg – trägolv i Duvbos villor",
    "description": "Golvläggare i Sundbyberg: massiva trägolv i Duvbos villor, hur ofta ett trägolv kan renoveras, "
                   "nya golv i äldre hus och rätt klimat för trä.",
    "h1": "Golvläggare i Sundbyberg",
    "lead": "Villorna i Duvbo byggdes kring sekelskiftet 1900 och på 1920-talet, och i många finns de gamla "
            "trägolven kvar under mattor och senare golv. Ett massivt trägolv kan renoveras många gånger. När "
            "det inte går, eller när ett rum behöver ett nytt golv, lägger vi ett som passar husets ålder.",
    "card": "Trägolv i äldre villor och nya golv.",
    "sections": [
        {"id": "duvbo", "anchor": "Duvbo", "h2": "Villor från två epoker",
         "paras": [
             "Husen i Duvbo är framför allt byggda vid sekelskiftet 1900 och under 1920-talet. Sekelskiftesvillorna "
             "byggdes ofta av ägarna själva, och 1920-talsvillorna är enklare och mer regelbundna. Riksantikvarieämbetet "
             "pekade 1987 ut Duvbo som riksintresse för kulturmiljövården.",
             "Kommunens miljöprogram handlar om husens utsida, men samma tanke om varsamhet gäller inne: det som "
             "är gammalt och fungerar ska helst få vara kvar. Det gäller inte minst golven."],
         "aside": {"title": "Duvbo",
                   "items": ["Villor från sekelskiftet 1900", "Villor från 1920-talet",
                             "Riksintresse sedan 1987"]}},
        {"id": "massiva", "anchor": "Massiva trägolv", "h2": "Ett massivt trägolv kan renoveras många gånger",
         "paras": [
             "Golvbranschen beskriver massiva trägolv som golv där hela tjockleken är samma träslag. De kan "
             "renoveras i hög utsträckning, och det som sätter gränsen är tjockleken mellan ytan och not och spont. "
             "Så länge det finns tillräckligt med trä kvar kan golvet slipas igen.",
             "Innan vi föreslår ett nytt golv tittar vi därför på det gamla. Vi lyfter en tröskel eller en list "
             "och mäter hur mycket trä som finns kvar ovanför sponten. Är det tillräckligt kan golvet slipas och "
             'behandlas i stället – läs mer om <a class="text-link" href="golvslipning-sundbyberg.html">golvslipning '
             "i Sundbyberg</a>."]},
        {"id": "nytt", "h2": "När ett nytt golv behövs",
         "paras": [
             "Ibland är det gamla golvet för slitet, för skadat eller borta sedan länge. Då lägger vi nytt. I ett "
             "äldre hus väljer vi gärna massiva brädor eller ett golv med bredd och träslag som passar huset, "
             "spikat eller skruvat på reglar eller blindbotten.",
             "I ett nyare tillbygge kan lamellparkett vara ett alternativ. "
             "Den består av flera korslimmade skikt och rör sig mindre med fukten. Vi går igenom för- och "
             "nackdelar innan du bestämmer dig."]},
        {"id": "klimat", "h2": "Fukt och temperatur",
         "paras": [
             "Trä krymper och sväller med luftens fuktighet. Golvbranschen rekommenderar att rumstemperaturen hålls "
             "mellan cirka 15 och 25 grader och den relativa fuktigheten mellan 30 och 60 procent för att golvet "
             "inte ska röra sig för mycket. Våta rengöringsmetoder avråds.",
             "I en gammal villa varierar klimatet mer än i ett nytt hus. Därför låter vi nytt virke vänja sig vid "
             "rummet innan det läggs, och vi lämnar råd om skötsel så att golvet håller sig fint."]},
        {"id": "lagenheter", "h2": "Lägenheter i Sundbyberg",
         "paras": [
             "Bor du i en bostadsrätt i Sundbyberg är golvet inne i "
             "lägenheten normalt ditt ansvar, men ett golvbyte som påverkar ljudet till grannen under kan kräva "
             "att du tar hänsyn till föreningens regler.",
             "Vi går igenom vad föreningen har för krav innan vi beställer material, och väljer underlag och golv "
             'efter det. Läs mer om <a class="text-link" href="golvlaggning.html">golvläggning</a>.']},
    ],
    "steps_h2": "Så går ett golvjobb till i Sundbyberg",
    "steps": [
        ("Besök", "Gratis besök där vi tittar på det gamla golvet."),
        ("Mätning", "Vi mäter hur mycket trä som finns kvar ovanför sponten."),
        ("Förslag", "Slipa och behandla, laga eller lägga nytt – skriftligt kostnadsförslag."),
        ("Material", "Nytt virke får vänja sig vid rummet innan läggning."),
        ("Läggning", "Golvet läggs, spikas eller skruvas och listas."),
        ("Råd", "Skötselråd för trägolv i ett äldre hus."),
    ],
    "rot_h2": "ROT-avdrag för golv i Sundbyberg",
    "rot": [ROT_SMAHUS + " " + ROT_END,
            "Bor du i en bostadsrätt ger golvbyte inne i lägenheten rotavdrag för det som du ansvarar för enligt "
            'stadgarna. '],
    "price_h2": "Vad påverkar priset i Sundbyberg?",
    "price": ["Golvytan, om det gamla golvet kan renoveras, hur underlaget ser ut, vilket golv du väljer och hur "
              "mycket som ska lagas runt trösklar och lister. Du får ett skriftligt kostnadsförslag efter besöket."],
    "faq": [
        ("Hur många gånger kan ett gammalt trägolv slipas?",
         "Så länge det finns tillräckligt med trä ovanför not och spont, enligt Golvbranschen. Vi mäter det innan "
         "vi föreslår något."),
        ("Vi har hittat ett gammalt trägolv under mattan i vår villa i Duvbo – går det att rädda?",
         "Ofta ja. Massiva trägolv kan renoveras många gånger. Vi tittar på skador, spikhål och hur mycket trä "
         "som finns kvar."),
        ("Varför rör sig trägolvet mellan sommar och vinter?",
         "Trä krymper och sväller med luftens fuktighet. Golvbranschen rekommenderar 30–60 procent relativ "
         "fuktighet och 15–25 grader."),
        ("Passar lamellparkett i en gammal villa?",
         "Den kan passa i nyare tillbyggnader. I de gamla rummen väljer vi oftast massivt trä."),
    ],
    "sources": [
        ("Sundbybergs stad – Miljöprogram för Duvbo (2024)", DUVBO),
        ("Sundbybergs stad – Duvbo", SBG_DUVBO),
        ("Golvbranschen – Massiva trägolv", GB_MASSIVA),
        ("Golvbranschen – Lamellparkett", GB_LAMELL),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ],
    "cta": ("Ska golvet i villan eller lägenheten i Sundbyberg göras om?",
            "Boka ett gratis besök, så tittar vi på det gamla golvet innan du får ett skriftligt kostnadsförslag."),
    "img": [
        ("Gamla breda trägolvsbrädor i en villa från sekelskiftet",
         "room in a Swedish wooden villa from about 1900 with old wide pine floorboards showing natural patina, "
         "white painted skirting boards, a tall window with daylight, simple furniture removed, calm interior"
         + NO_PEOPLE),
        ("Tvärsnitt av gamla golvbrädor med not och spont vid en dörröppning",
         "close view of a doorway where a threshold has been removed, showing the end cross-section of old thick "
         "tongue and groove pine floorboards with visible tongue, plain wood, no measuring tools, soft daylight" + NO_PEOPLE),
        ("Nya massiva brädor som acklimatiseras i ett rum",
         "stack of new solid pine floorboards resting on spacers in an empty room of an older house to acclimatise "
         "before laying, window light" + NO_PEOPLE),
    ],
}

# ======================================================== FASADRENOVERING I KISTA
PAGES_TJ["fasadrenovering-kista.html"] = {
    "kind": "district", "service": "fasadrenovering", "ort": "Kista", "svc_label": "Fasadrenovering",
    "title": "Fasadrenovering i Kista – radhusens fasader efter 50 år",
    "description": "Fasadrenovering i Kista: småhus från 1975–80, panel och skivor som byts, tilläggsisolering "
                   "som fasadändring och gamla material.",
    "h1": "Fasadrenovering i Kista",
    "lead": "Kistas småhus byggdes 1975–1980 och har nu stått i snart 50 år. Oavsett om fasaden är av trä, skivor "
            "eller tegel har den fått sin beskärda del av väder och vind. En fasadrenovering i Kista kan vara allt från att byta "
            "enstaka brädor till ny panel och tilläggsisolering – och i radhus som ägs av en förening är det "
            "ofta styrelsen som bestämmer.",
    "card": "Panel, skivor och isolering på radhus.",
    "sections": [
        {"id": "hus", "anchor": "Husen", "h2": "Friare former på Järvafältet",
         "paras": [
             "När Kista byggdes ut 1975–1980 tillämpade staden enligt Stadsmuseet betydligt friare former för "
             "arkitekturen än i de andra stadsdelarna på Järvafältet. Bebyggelsen fick 2 500 lägenheter i "
             "flerbostadshus och omkring 780 småhus.",
             "Stadens statistik för 2024 visar 971 småhus i Kista. 482 ägs med äganderätt och 404 är "
             "bostadsrätter. För en fasadrenovering betyder det att ungefär hälften av radhusägarna beställer "
             "själva, medan resten har en förening som kan ansvara för fasaden."],
         "aside": {"title": "Kistas småhus (2024)",
                   "items": ["971 småhus", "482 med äganderätt", "404 bostadsrätter", "Byggda 1975–1980"]}},
        {"id": "skador", "anchor": "Skadorna", "h2": "Där fasaden tar stryk först",
         "paras": [
             "På en träfasad är det nederkanten som drabbas först: brädorna närmast marken och ovanför fönster och "
             "dörrar där vattnet rinner av. Där börjar rötan, och där släpper färgen först.",
             "Vi går runt huset och känner på panelen med en syl, tittar på fönsterbleck och anslutningar och "
             "kontrollerar att luftspalten bakom panelen är öppen nedtill. Är skadorna begränsade räcker det att "
             "byta de brädor som är dåliga och måla om."]},
        {"id": "material", "h2": "Gamla material i fasaden",
         "paras": [
             "Boverket skriver att asbest förbjöds inom byggsektorn 1982. Hus byggda före dess kan alltså innehålla "
             "asbesthaltiga material, till exempel i vissa fasadskivor. Så länge materialet sitter fast och inte "
             "bearbetas är det ingen fara, men när det sågas, borras eller rivs kan fibrer frigöras.",
             "Kistas småhus är byggda just innan förbudet. Innan vi river skivor eller annat material som kan vara "
             "från byggtiden tar vi reda på vad det är, och vid tvekan tas prov. Arbetsmiljöverket har regler för "
             "hur asbest ska hanteras när det rivs."]},
        {"id": "isolering", "h2": "Tilläggsisolering är en fasadändring",
         "paras": [
             "Staden räknar tilläggsisolering som en fasadändring, liksom byte av kulör eller material på fasaden. "
             "På ett en- eller tvåbostadshus krävs inte längre bygglov för fasadändringar om vissa förutsättningar "
             "är uppfyllda, men ändringen ska stämma med detaljplanen och göras varsamt.",
             "Tilläggsisolering gör väggen tjockare. Fönster, dörrar, takfot och fönsterbleck måste anpassas, och "
             "i ett radhus påverkas även anslutningen mot grannens fasad. Vi visar hur det löses innan något "
             "beställs."]},
        {"id": "forening", "h2": "Radhus i förening",
         "paras": [
             "I ett radhusområde där husen är bostadsrätter avgör stadgarna vem som ansvarar för fasaden. Ofta är "
             "det föreningen, och då görs fasaderna längs en hel länga eller ett helt område samtidigt.",
             "Styrelsen får ett skriftligt kostnadsförslag efter ett gratis besök, med foton av skadorna och vad "
             "som bör göras nu och vad som kan vänta. Läs mer om "
             '<a class="text-link" href="fasadrenovering.html">fasadrenovering</a>.']},
    ],
    "steps_h2": "Så renoverar vi en fasad i Kista",
    "steps": [
        ("Besök", "Gratis besök där vi går runt huset och kontrollerar panel och anslutningar."),
        ("Material", "Vi tar reda på vad fasaden består av och tar prov vid tvekan."),
        ("Förslag", "Skriftligt kostnadsförslag med foton och prioriteringar."),
        ("Ställning", "Ställning och skydd för trädgård och grannar."),
        ("Utförande", "Byte av panel, isolering, bleck och anslutningar."),
        ("Målning", "Grundmålning och färdigmålning i vald kulör."),
    ],
    "rot_h2": "ROT-avdrag för fasadrenovering i Kista",
    "rot": [ROT_SMAHUS + " " + ROT_END,
            "Ansvarar en bostadsrättsförening för fasaden ger arbetet inget rotavdrag för medlemmarna."],
    "price_h2": "Vad påverkar priset i Kista?",
    "price": ["Fasadens yta och material, hur mycket som behöver bytas, om fasaden ska tilläggsisoleras, om gamla "
              "material måste hanteras särskilt och om flera hus görs samtidigt. Du får ett skriftligt "
              "kostnadsförslag."],
    "faq": [
        ("Kan fasaden på vårt radhus i Kista innehålla asbest?",
         "Det kan den, eftersom husen byggdes innan asbest förbjöds 1982. Vi tar reda på vad materialet är innan "
         "något rivs och tar prov vid tvekan."),
        ("Behöver vi bygglov för att tilläggsisolera?",
         "På ett en- eller tvåbostadshus krävs i regel inte bygglov, men ändringen ska stämma med detaljplanen. "
         "Kontrollera detaljplanen innan arbetet beställs."),
        ("Måste hela panelen bytas?",
         "Nej, ofta inte. Många gånger är det bara de nedersta brädorna och delar runt fönster som är dåliga. Då byts de och "
         "fasaden målas om."),
        ("Vem beställer fasadrenoveringen i vår brf?",
         "Det beror på stadgarna. Ansvarar föreningen för fasaden är det styrelsen som beställer."),
    ],
    "sources": [
        ("Stockholms stadsmuseum – Stockholms spår: Kista", SSM + "SSM_DOK_000080.pdf"),
        ("Stockholms stad – Områdesfakta Kista (2025)", OF + "vasterort/jarva/kista.pdf"),
        ("Stockholms stad – Fasadändring", BL_FASAD),
        ("Boverket – Ändra fasad eller tak", BOV_UTANLOV),
        ("Boverket – Asbest", BOV_ASBEST),
        ("Arbetsmiljöverket – Förebygg riskerna med asbest", AV_ASBEST),
        ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ],
    "cta": ("Behöver fasaden på radhuset i Kista göras om?",
            "Boka ett gratis besök, så går vi runt huset och lämnar ett skriftligt kostnadsförslag."),
    "img": [
        ("Radhus från 1970-talet med träpanel och små förträdgårdar",
         "row of Swedish late 1970s terraced houses with vertical wooden board facades painted in muted brown and "
         "ochre tones, white window frames, small front gardens with shrubs, overcast day" + NO_PEOPLE + ", no cars"),
        ("Nederkant av en träfasad med ny panel bredvid gammal",
         "close view of the lower part of a wooden house facade where several new unpainted boards have replaced "
         "rotten ones next to old painted boards, metal flashing above the plinth, gravel below" + NO_PEOPLE),
        ("Ställning vid en radhusfasad under renovering",
         "scaffolding along the facade of a Swedish 1970s terraced house during renovation, new wooden battens "
         "and insulation boards partly fitted, tools neatly stacked, clear day" + NO_PEOPLE),
    ],
}

# Extra sektion sist på sidor som behöver mer innehåll (läggs före sista bilden).
_EXTRA = {
    "snickare-ostermalm.html": {
        "id": "samordning", "h2": "Snickaren först, målaren sedan",
        "paras": [
            "Lagade dörrar, paneler och lister behöver i regel målas efteråt. Därför planerar vi arbetet så att "
            "snickeriet är klart innan målaren börjar, och lämnar ytorna rengjorda och spacklade där vi har lagat.",
            "Har lägenheten flera lager gammal färg på dörrar och foder tar vi ner dem till en verkstad om det "
            "behövs, så att de kan justeras och lagas ordentligt. Delarna märks och kommer tillbaka till samma "
            "plats, med samma beslag om de går att återanvända. Vill du att målaren också ska ta hand om "
            'resten av lägenheten kan vi samordna det – läs mer om <a class="text-link" href="malare-ostermalm.html">'
            "målare på Östermalm</a>."]},
    "snickare-skarholmen.html": {
        "id": "underhall", "h2": "Underhåll som förlänger livet",
        "paras": [
            "En altan eller ett plank i trä står ute året runt. Det som avgör hur länge det håller är oftast hur "
            "vattnet rinner av: brädor med en liten springa emellan, stolpar som inte står i stående vatten och "
            "ändträ som skyddas.",
            "Vi bygger med det i tankarna och lämnar råd om när virket ska tvättas och behandlas. Ett plank som "
            "målas om vart några år och en altan som rensas från löv mellan brädorna håller betydligt längre än "
            "en som lämnas utan tillsyn. Vill du ha hjälp med det också kommer vi gärna tillbaka."]},
    "malare-skarholmen.html": {
        "id": "kulor", "h2": "Välja kulör i en äldre lägenhet",
        "paras": [
            "Ljuset i en lägenhet i ett hus från 1960-talet beror mycket på väderstrecket och på hur stora fönstren "
            "är. En kulör som ser ljus ut i butiken kan bli grå i ett rum mot norr. Därför målar vi gärna en "
            "provyta på väggen innan hela rummet målas.",
            "Snickerier som dörrar och foder kan få en egen nyans som skiljer sig lite från väggarna. Det gör att "
            "rummet får djup utan att bli mörkare. Vi hjälper dig att välja kulörer som passar ljuset och "
            "rummets storlek, och skriver in dem i kostnadsförslaget så att inget blir fel."]},
    "golvlaggare-kista.html": {
        "id": "hall", "h2": "Golv i hall, kök och trappa",
        "paras": [
            "I hallen och köket möter golvet vatten, grus och snö. Där passar ett golv som tål fukt och slitage "
            "bättre än parkett, till exempel klinker eller ett slitstarkt plastgolv. Övergången till parketten "
            "görs med en tröskel eller list som inte blir en snubbelkant.",
            "Har radhuset två plan behöver trappan ofta göras om när golven byts. Vi mäter "
            "stegen och föreslår om de ska kläs med samma material som golvet eller renoveras för sig. Det "
            "gör att huset får ett sammanhållet uttryck från hall till övervåning."]},
    "golvlaggare-sundbyberg.html": {
        "id": "trosklar", "h2": "Trösklar, lister och nivåer",
        "paras": [
            "I en gammal villa är golven sällan helt plana. Mellan rummen kan nivåerna skilja sig, och trösklarna "
            "är ofta höga. När ett golv byts eller renoveras tittar vi på hur övergångarna ska lösas, så att "
            "dörrarna går att stänga och ingen snubblar.",
            "Gamla golvlister med profiler går ofta att ta ner och sätta tillbaka. Saknas några tillverkas nya i "
            "samma profil. Det gör att rummet ser ut som förut, trots att golvet är nytt eller nyslipat. Vi "
            "sparar och märker de gamla delarna innan arbetet börjar."]},
    "fasadrenovering-kista.html": {
        "id": "farg", "h2": "Kulör och husgruppens uttryck",
        "paras": [
            "Radhus byggs i grupper där husen hör ihop. Byter ett hus kulör eller material syns det "
            "längs hela längan. På ett en- eller tvåbostadshus krävs i regel inte bygglov för att måla om i en "
            "ny kulör, men ändringen ska enligt Boverket anpassas till omgivningen och göras varsamt.",
            "Vi föreslår därför att grannarna stäms av innan en ny kulör väljs, och att samma kulörkod används "
            "om flera hus renoveras vid olika tillfällen. Kulören skrivs in i kostnadsförslaget, så att den kan "
            "användas igen nästa gång."]},
}
for _f, _s in _EXTRA.items():
    PAGES_TJ[_f]["sections"].append(_s)

_EXTRA_FAQ = {
    "golvlaggare-kista.html": [
        ("Vilket golv passar i hallen i ett radhus i Kista?",
         "Ett golv som tål vatten, grus och snö, till exempel klinker eller ett slitstarkt plastgolv, med en låg "
         "övergång till parketten i resten av huset.")],
    "golvlaggare-sundbyberg.html": [
        ("Kan de gamla golvlisterna sättas tillbaka?",
         "Ofta ja. Vi tar ner, märker och sparar dem innan arbetet börjar. Saknas några tillverkas nya med samma profil.")],
    "fasadrenovering-kista.html": [
        ("Får vi måla radhuset i en annan kulör än grannarna?",
         "På ett en- eller tvåbostadshus krävs i regel inget bygglov för en ny kulör, men ändringen ska anpassas "
         "till omgivningen. I en husgrupp rekommenderar vi att grannarna stäms av först."),
        ("Hur länge står ställningen?",
         "Det beror på hur mycket som ska bytas. Du får en tidsplan i kostnadsförslaget, och vi informerar "
         "grannarna innan ställningen kommer.")],
}
for _f, _q in _EXTRA_FAQ.items():
    PAGES_TJ[_f]["faq"] = PAGES_TJ[_f]["faq"] + _q
