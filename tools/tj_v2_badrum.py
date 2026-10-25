# -*- coding: utf-8 -*-
"""Tjänster v2 (2026-10-25) – ortsidor badrumsrenovering i Huddinge, Sollentuna, Lidingö, Nacka,
Solna och Danderyd. Schema: se tools/tj_check.py.
Lokala fakta om bebyggelsen är omformulerade från tools/takreno_orter.py (TRP, granskade i v1) och
bara där källan är kommunen/kulturmiljöprogrammet – inte Wikipedia. Regler om anmälan, ventilation,
VA och ritningsarkiv är hämtade från respektive kommuns webbsidor (öppnade 2026-10-25), ROT från
Skatteverket, golvbrunnar före 1990 från GVK och styrelsens tillstånd från bostadsrättslagen.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller certifikat."""

L = '<a class="text-link" href="{0}">{1}</a>'
X = '<a class="text-link" href="{0}" rel="noopener">{1}</a>'

# Gemensamma källor
S_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
         "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
S_PBF = ("Riksdagen – Plan- och byggförordning (2011:338), 6 kap. 1 § (anmälan)",
         "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-byggforordning-2011338_sfs-2011-338/")
S_GVK_BRUNN = ("GVK – Gamla golvbrunnar", "https://www.gvk.se/branschregler/golvbrunn/gamla-golvbrunnar/")
S_ROT = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
S_ROTJOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
S_PBL = ("Boverket – Lista med PBL-ändringar som trädde i kraft 1 december 2025",
         "https://www.boverket.se/sv/samhallsplanering/uppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/")

GVK_BRUNN = S_GVK_BRUNN[1]

# Huddinge
HUD_VA = "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/installation-eller-andring-av-vatten-och-avlopp-va"
HUD_VENT = "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/ventilation-och-ovk"
HUD_FRITID = "https://www.huddinge.se/bostad-och-miljo/vatten-och-avlopp/ansluta-till-kommunalt-vatten/utbyggnad-av-vatten-och-avlopp-i-fritidsomraden"
HUD_ENSK = "https://www.huddinge.se/bostad-och-miljo/vatten-och-avlopp/avlopp/installera-enskilt-avlopp---steg-for-steg"
HUD_ANSL = "https://www.huddinge.se/bostad-och-miljo/vatten-och-avlopp/ansluta-till-kommunalt-vatten"
HUD_KMP2 = "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf"
HUD_KMP1 = "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram-del-1.pdf"
# Sollentuna
SOL_VA = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/installation-eller-andring-i-installationer-va/"
SOL_VENT = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/installation-eller-andring-av-ventilation/"
SOL_VENTD = "https://www.sollentuna.se/bygga-bo--miljo/Din-bostad-och-tomt/ventilation/"
SOL_OP = "https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/oversiktsplan/oversiktsplan-for-sollentuna-med-sikte-pa-2040.pdf"
SOL_KULT = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/kulturmiljoer/"
# Lidingö
LID_VAD = "https://lidingo.se/bygga-bo/bygglov/vad-vill-du-gora/"
LID_SPILL = "https://lidingo.se/bygga-bo/mitt-boende/vatten-och-avlopp/spillvatten-avlopp/"
LID_ANDR = "https://lidingo.se/bygga-bo/bygglov/andrade-lagar-och-regler-for-byggande/"
LID_KMPFAQ = "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/"
# Nacka
NAC_BAR = "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/jag-vill-gora-ansokan-eller-anmalan/andring-barande-konstruktioner/"
NAC_ANDRA = "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/jag-vill-gora-ansokan-eller-anmalan/andra-anmalningar/"
NAC_VENT = "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/jag-vill-gora-ansokan-eller-anmalan/installera-ventilation/"
NAC_JV = "https://www.nacka.se/499626/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-jarnvagen.pdf"
NAC_SN = "https://www.nacka.se/499628/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-sommarnojen.pdf"
NAC_ALTA = "https://www.nacka.se/49b6e2/globalassets/uppleva-gora/bilder/kultur/kulturhistoria/kulturpromenader/vandring-alta.pdf"
# Solna
SNA_LGH = "https://www.solna.se/bygga-bo--miljo/bygga/guide-till-lov-och-anmalan/for-lagenhetsinnehavare"
SNA_ANM = "https://www.solna.se/bygga-bo--miljo/bygga/anmalan"
SNA_VA = "https://www.solna.se/bygga-bo--miljo/bygga/anmalan/andra-vatten-och-avlopp"
SNA_KULT = "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna"
SNA_FRIA = "https://www.solna.se/bygga-bo--miljo/bygga/bygglov/bygglovsfria-atgarder"
SNA_VILLA = "https://www.solna.se/bygga-bo--miljo/bygga/guide-till-lov-och-anmalan/for-villaagare"
# Danderyd
DAN_ARK = "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/ritningsarkiv/"
DAN_INV = "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/checklistor/checklistor-invandig-andring/"
DAN_OVK = "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/fragor-och-svar/ovk/"
DAN_NY = "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/"
DAN_RIKS = "https://danderyd.se/contentassets/94fc6956dc264c4cab52c0a18ff5bafd/3-riks--och-mellankommunala-intressen.pdf"
DAN_RIKTL = ("https://www.danderyd.se/globalassets/globala-filer/kommun-och-politik/ovriga-styrdokument-ny/styrande-dokument---"
             "samhallsbyggnad-miljo-och-exploatering/riktlinjer-for-kulturmiljohistoriska-byggnader-och-miljoer-i-danderyd-2024.pdf")

PAGES_TJ = {

# =============================== BADRUM HUDDINGE ===============================
"badrumsrenovering-huddinge.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Huddinge", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Huddinge – från sportstuga till grupphus",
  "description": "Badrumsrenovering i Huddinge: egnahem, grupphus och permanentade stugor, enskilt eller kommunalt "
                 "avlopp, kommunens regler för anmälan och ROT på fakturan.",
  "h1": "Badrumsrenovering i Huddinge",
  "lead": "Badrumsrenovering i Huddinge kan betyda ett våtrum i ett egnahem i Stuvsta, ett 70-talsbadrum i ett "
          "grupphus i Skogås eller ett första riktiga badrum i en stuga vid Mellansjö. Vi river, bygger upp "
          "underlag och tätskikt och samordnar VVS och el – och vi börjar med att reda ut vart avloppet tar vägen.",
  "card": "Egnahem, grupphus och permanentade stugor.",
  "sections": [
    {"id": "husen", "anchor": "Husen i Huddinge",
     "h2": "Tre slags hus, tre slags badrum",
     "paras": [
       "Huddinges kulturmiljöprogram beskriver villabebyggelsen i lager. Först kom egnahemmen och villastäderna "
       "längs stambanan: Stuvsta och Hörningsnäs började byggas i början av 1900-talet, och på 1920-talet "
       "styckades Segeltorp och Snättringe till tomter. Husen har träpanel och sadeltak eller brutna tak, och i hus "
       "från den tiden har badrummet ofta tillkommit i efterhand, i källaren eller i ett rum som var tänkt för annat.",
       "Under rekordåren och fram till början av 1980-talet byggdes grupphusområden som Sörskogen, Utsälje och "
       "de terränganpassade småhusen i Östra Skogås. Där fanns våtrummet med från början, och i ett hus som "
       "inte renoverats är tätskikt, golvbrunn och rör lika gamla som huset.",
       "Det tredje lagret är sportstugorna vid sjöarna. Vid Mellansjö och Trehörningen byggdes stugor under "
       "1910–30-talen, och vid Gömmarens södra stränder växte ett liknande område fram. Många stugor har "
       "permanentats och byggts till. Ett badrum i ett sådant hus är ofta det första riktiga våtrummet huset "
       "får, och då avgör avloppet mer än kaklet.",
     ],
     "aside": {"title": "Vilket hus gäller det?", "items": [
       "Egnahem från 1910–40-talet: Stuvsta, Snättringe, Segeltorp",
       "Grupphus från 1960–80-talet: Sörskogen, Utsälje, Östra Skogås",
       "Permanentade stugor: Mellansjö, Trehörningen, Gömmaren",
       "Har huset kommunalt vatten och avlopp eller egen anläggning?"]}},
    {"id": "avlopp",
     "h2": "Egen avloppsanläggning eller kommunalt nät",
     "paras": [
       "Det är Stockholm Vatten och Avfall som ansvarar för det kommunala vattnet i Huddinge, och enligt "
       " " + X.format(HUD_VA, "kommunens sida om VA-installationer") + " är det byggherren som "
       "ska kontakta dem om något ska anslutas eller ändras. Saknar huset kommunalt avlopp ska du också höra av "
       "dig till kommunens miljötillsynsavdelning innan du gör ändringar.",
       "För fritidshusområden skriver kommunen att den som vill använda en ny byggrätt, när ett område anpassas "
       "för permanentboende, måste ansluta sig till det allmänna nätet. Har du en godkänd enskild anläggning får "
       "du använda den till dess, men " + X.format(HUD_FRITID, "kommunen uppmanar") + " dig att kontrollera att den "
       "klarar kraven för ditt hus. Vilka områden som ska anpassas ska stå i vattentjänstplanen, som enligt "
       "kommunen planeras att antas hösten 2026.",
       "Ska en ny enskild anläggning byggas krävs ett skriftligt tillstånd innan arbetet börjar. Kommunen anger "
       "att det kan ta ungefär tio veckor från komplett ansökan till " + X.format(HUD_ENSK, "tillstånd") + ". "
       "Planera därför badrummet och avloppet i samma tidplan, så att rummet inte står klart utan att vattnet "
       "har någonstans att ta vägen.",
     ],
     "aside": {"title": "Före ett badrum i en stuga", "items": [
       "Finns kommunalt avlopp i gatan?",
       "Är den egna anläggningen godkänd för WC?",
       "Står området i vattentjänstplanen?",
       "Räcker tidplanen för ett tillstånd?"]}},
    {"id": "anmalan",
     "h2": "Det här vill Huddinge kommun ha in före start",
     "paras": [
       "Ett stambyte där de nya stammarna läggs i samma läge behöver enligt kommunen ingen anmälan. Ska "
       "stammar dras i nya lägen, eller ska en anläggning för vatten och avlopp installeras eller ändras "
       "väsentligt, krävs anmälan och startbesked. Kommunen vill då ha en situationsplan, en planritning, ett "
       "förslag till kontrollplan och – om det tas upp hål i bärande delar – ett utlåtande från en konstruktör. "
       "Är du osäker på om ändringen är stor nog ber kommunen dig kontakta servicecenter.",
       "Ventilationen har egna gränser. På " + X.format(HUD_VENT, "kommunens sida om ventilation") + " står att "
       "byte av fläkt eller don till likvärdiga normalt inte behöver anmälas, och inte heller ett byte från "
       "självdrag till fläktstyrd frånluft i ett en- eller tvåbostadshus. Nya aggregat, kanaler eller "
       "värmeväxlare som påverkar flödena kräver däremot anmälan, och monteras något utvändigt kan det bli en "
       "fråga om bygglov.",
     ],
     "aside": None},
    {"id": "grupphus",
     "h2": "Grupphusbadrummet från 70-talet",
     "paras": [
       "I ett grupphus i Sörskogen eller Skogås är frågan sällan var badrummet ska ligga, utan vad som finns "
       "under ytskikten. Branschorganisationen GVK skriver att " + X.format(GVK_BRUNN, "golvbrunnar tillverkade före 1990") +
       " ska bytas vid till exempel en påkostad renovering eller efter en omfattande vattenskada. Ett badrum "
       "som är original från byggåret har nästan säkert en sådan brunn.",
       "Kulturmiljöprogrammet pekar ut både Sörskogen och Östra Skogås som särskilt värdefulla miljöer. Inne i "
       "badrummet spelar det ingen roll, men ett nytt fönster, ett ventilationsgaller eller en huv på taket kan "
       "kräva lov i sådana områden. Hur husen i kommunen ser ut från taket och uppåt finns under "
       + L.format("takrenovering-huddinge.html", "takrenovering i Huddinge") + ", och grunderna för tätskikt "
       "och fall under " + L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Badrummet i Huddinge steg för steg",
  "steps": [
    ("Besök och avloppsfrågan", "Vi ser badrummet och tar reda på om huset har kommunalt avlopp eller en egen anläggning."),
    ("Anmälan vid behov", "Flyttas stammar eller ändras ventilationen väsentligt tar vi fram underlag för anmälan."),
    ("Skriftligt förslag", "Rivning, underlag, tätskikt, rör, el och ytskikt står som egna poster i kostnadsförslaget."),
    ("Rivning och öppet golv", "Golv och väggar öppnas, och golvbrunn, rör och bjälklag bedöms innan något byggs."),
    ("Uppbyggnad", "Fall mot brunnen, våtrumsskivor och tätskikt läggs, och installatörerna drar rör och el."),
    ("Ytskikt och papper", "Klinker, kakel och porslin på plats; du får egenkontroll och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag i Huddinge – också för avloppet",
  "rot": [
    "Företaget får dra högst 30 procent av arbetskostnaden på fakturan, och rotavdraget får vara högst 50 000 "
    "kronor per person och år, med ett tak på 75 000 kronor ihop med rutavdrag. Material och resor ingår inte.",
    "För ett småhus räknar Skatteverket även in att dra in vatten- och avloppsledningar, att anlägga avlopp "
    "som trekammarbrunnar och infiltrationsbäddar och att dra in kommunalt vatten och avlopp, inklusive "
    "markarbetet. Slamsugning och tömning av septiktankar ger däremot inget avdrag.",
  ],
  "price_h2": "Vad avgör priset på ett badrum i Huddinge?",
  "price": [
    "I en permanentad stuga är det ofta avloppet och underlaget som väger tyngst, i ett grupphus snarare "
    "golvbrunnen och tätskiktet, och i ett egnahem stommen under badrummet. Därtill kommer storlek, ytskikt och "
    "om något ska flyttas. Besöket kostar inget, och du får ett skriftligt förslag innan något beställs.",
  ],
  "faq": [
    ("Kan vi bygga badrum i stugan vid Mellansjö innan kommunalt avlopp finns?",
     "Ja, om den egna avloppsanläggningen är godkänd för det huset. Kommunen rekommenderar att du kontrollerar "
     "det med miljötillsynsavdelningen, och en ny anläggning kräver tillstånd innan den byggs."),
    ("Behöver vi anmäla stambytet i vårt radhus i Utsälje?",
     "Inte om de nya stammarna läggs i samma läge, enligt Huddinge kommun. Flyttas de till nya lägen krävs anmälan och startbesked."),
    ("Får vi byta från självdrag till frånluftsfläkt i badrummet utan anmälan?",
     "I ett en- eller tvåbostadshus i Huddinge behövs normalt ingen anmälan för det bytet. Nya aggregat eller kanaler som ändrar flödena ska däremot anmälas."),
    ("Måste golvbrunnen bytas när vi renoverar ett 70-talsbadrum i Sörskogen?",
     "GVK:s regler säger att brunnar från före 1990 ska bytas vid en påkostad renovering. En ny brunn ingår därför nästan alltid."),
    ("Ger det ROT att ansluta stugan till kommunalt vatten och avlopp?",
     "Ja, för ett småhus räknar Skatteverket indragning av kommunalt vatten och avlopp, med markarbetet, som rotarbete."),
  ],
  "sources": [
    ("Huddinge kommun – Installation eller ändring av vatten och avlopp", HUD_VA),
    ("Huddinge kommun – Ventilation och OVK", HUD_VENT),
    ("Huddinge kommun – Utbyggnad av vatten och avlopp i fritidsområden", HUD_FRITID),
    ("Huddinge kommun – Installera enskilt avlopp, steg för steg", HUD_ENSK),
    ("Huddinge kommun – Kommunalt vatten och avlopp", HUD_ANSL),
    ("Huddinge kommun – Kulturmiljöprogram del 2 (småhus, semesterbostäder)", HUD_KMP2),
    ("Huddinge kommun – Kulturmiljöprogram del 1 (särskilt värdefulla miljöer)", HUD_KMP1),
    S_GVK_BRUNN, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i Huddinge göras om?", "Boka ett gratis besök, så tittar vi på rummet och avloppet på plats."),
  "img": [
    ("Nytt badrum i en permanentad trästuga i Huddinge",
     "small newly built bathroom inside a converted Swedish wooden summer cottage, white painted wood panel ceiling, "
     "light grey floor tiles, white wall tiles, compact walk-in shower with glass screen, small window with pine forest outside"),
    ("Rivet badrumsgolv med ny golvbrunn inför uppbyggnaden",
     "small Swedish house bathroom stripped for renovation, no fixtures, bare grey concrete floor sloping towards a new small round "
     "stainless steel floor drain in the middle, grey plastic drain pipe stubs coming out of the floor, white wet-room boards "
     "stacked against bare walls, a bucket and a spirit level, daylight from a small window"),
  ],
},

# =============================== BADRUM SOLLENTUNA ===============================
"badrumsrenovering-sollentuna.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Sollentuna", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Sollentuna – ventilation och stammar",
  "description": "Badrumsrenovering i Sollentuna: villastad och radhus, tecken på dålig ventilation och "
                 "kommunens regler för anmälan av VA och ventilation. ROT på fakturan.",
  "h1": "Badrumsrenovering i Sollentuna",
  "lead": "När ett badrum i Sollentuna ska göras om är det ofta ventilationen och stammarna som avgör hur stort "
          "jobbet blir, inte kaklet. Vi river ner till underlaget, bygger tätskikt och ytskikt och samordnar VVS "
          "och el – och vi tar reda på vad som behöver anmälas till kommunen innan vi börjar.",
  "card": "Villastad, radhus och ventilationen.",
  "sections": [
    {"id": "husen", "anchor": "Husen i Sollentuna",
     "h2": "Villastad vid järnvägen och radhus från senare år",
     "paras": [
       "Enligt kommunens översiktsplan byggdes järnvägen mellan Stockholm och Uppsala 1866. Rotebro var först "
       "den enda stationen, men i början av 1900-talet anlades stationer i Tureberg och Norrviken, och då "
       "började man bygga småhus och villor. Kommunen vill bevara den prägel av villastad som växte fram under "
       "seklets första hälft, och nämner bland annat Norrvikens villastad, Väderholmen och Skansen.",
       "Efter kriget kom flerbostadshusen, och mellan 1965 och 1975 uppfördes flera miljonprogramsområden. I "
       "Sjöberg byggdes villor, radhus och flerbostadshus främst under 70-, 80- och 90-talen. Sollentuna har "
       "alltså både sekelskiftesvillor där badrummet byggts in i efterhand och radhus och lägenheter där "
       "våtrummet är lika gammalt som huset.",
       "För radhusgrupper skriver översiktsplanen att husen kan förändras, men att varje förändring ska bidra "
       "positivt till helheten. Inne i badrummet märks det inte, men ett nytt fönster eller en ny takhuv syns från gatan.",
     ],
     "aside": {"title": "Sollentuna i korthet", "items": [
       "1866: järnvägen Stockholm–Uppsala",
       "Tidigt 1900-tal: stationer i Tureberg och Norrviken",
       "1965–75: miljonprogramsområden",
       "Sjöberg: villor och radhus från 70–90-talen"]}},
    {"id": "ventilation",
     "h2": "Imman på spegeln säger mycket om badrummet",
     "paras": [
       "På " + X.format(SOL_VENTD, "Sollentuna kommuns sida om ventilation") + " finns några enkla tecken på att "
       "luften inte byts som den ska: imman på badrumsspegeln försvinner inte inom 15 minuter efter duschen, det "
       "luktar avlopp från frånluftsventilen eller ventilen orkar inte suga fast en pappersbit. Fukt som blir "
       "kvar i rummet sliter på fogar, silikon och målade ytor, och i värsta fall på det som sitter bakom.",
       "Bor du i villa råder kommunen dig att ta hjälp av en konsult, och i bostadsrätt ska du kontakta "
       "föreningens styrelse. När badrummet ändå rivs är det rätt läge att se över frånluftsdonets placering, "
       "att det finns en väg in för ersättningsluft – en spalt under dörren eller ett tilluftsdon – och om "
       "fläkten räcker för rummet.",
       "Vill du installera ett nytt ventilationssystem eller göra en större ändring, till exempel byta aggregat, "
       "fläkt eller kanaler, ska det enligt " + X.format(SOL_VENT, "kommunen") + " anmälas och du ska vänta på "
       "startbesked. Behöver aggregat eller kanaler sitta på fasaden kan det dessutom krävas bygglov.",
     ],
     "aside": {"title": "Testa ventilationen själv", "items": [
       "Imman ska vara borta inom 15 minuter",
       "Ingen avloppslukt från ventilen",
       "Ventilen ska hålla fast en pappersbit",
       "Ersättningsluft ska kunna komma in"]}},
    {"id": "stammar",
     "h2": "Stambyte och nya rör – när kommunen ska ha en anmälan",
     "paras": [
       "Sollentuna kommun skriver att du behöver göra en " + X.format(SOL_VA, "anmälan för vatten och avlopp") +
       " om ett stambyte påverkar VA-stammar, byggnadens konstruktion eller planlösning, och när du installerar "
       "eller gör en större ändring av en anläggning för vattenförsörjning eller avlopp. Med anmälan ska följa "
       "en redovisning av VA-anordningarna, plan- och sektionsritningar och ett förslag till kontrollplan. Är "
       "arbetet mer omfattande behövs en kontrollansvarig, och berörs bärande konstruktion krävs konstruktionsritningar.",
       "Kommunen anger en handläggningstid på ungefär två till fyra veckor. Den tiden behöver finnas i "
       "planeringen om badrummet ska flyttas, få en ny dusch på andra sidan rummet eller byggas om i samband med "
       "ett stambyte. Ett badrum som renoveras med samma placering av brunn, toalett och dusch brukar inte "
       "kräva någon anmälan alls.",
     ],
     "aside": None},
    {"id": "radhus",
     "h2": "Radhuset med originalbadrum",
     "paras": [
       "I ett radhus från 70- eller 80-talet är golvbrunnen ofta den del som styr renoveringen. GVK skriver att "
       + X.format(GVK_BRUNN, "golvbrunnar från före 1990") + " ska bytas vid stambyte, vid en påkostad renovering "
       "eller efter en större vattenskada. Byts brunnen behöver golvet byggas om runt den, och då görs fallet om samtidigt.",
       "Väggen mot grannen är en annan sak att tänka på. En läcka där drabbar två hus, och rivning hörs genom "
       "hela längan. Prata med grannarna i förväg och ta reda på om samfälligheten eller föreningen äger någon "
       "del av ledningarna. Mer om metod och papper finns under "
       + L.format("badrumsrenovering.html", "badrumsrenovering i Stockholm") + ", och om husens tak under "
       + L.format("takrenovering-sollentuna.html", "takrenovering i Sollentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går vi till väga i Sollentuna",
  "steps": [
    ("Genomgång i badrummet", "Vi testar frånluften, tittar på brunn och rör och frågar hur rummet används."),
    ("Anmälan eller inte", "Ändras stammar, planlösning eller ventilation tar vi fram underlag för anmälan."),
    ("Kostnadsförslag på papper", "Arbete och material står på egna rader, så att ROT-avdraget går att räkna ut."),
    ("Rivning", "Ytskikt, gamla skivor och brunn tas bort, och underlaget bedöms med rummet öppet."),
    ("Rör, luft och tätskikt", "Installatörerna drar rör och el, frånluften ansluts och sedan byggs fall och tätskikt."),
    ("Klart rum", "Kakel, klinker och porslin monteras, och du får egenkontroll och skötselråd."),
  ],
  "rot_h2": "Rotavdraget för badrummet i Sollentuna",
  "rot": [
    "Av arbetskostnaden kan 30 procent dras direkt på fakturan, så länge du har avdrag kvar: högst 50 000 "
    "kronor rotavdrag per person och år och högst 75 000 kronor tillsammans med rutavdrag. Material och resor räknas inte.",
    "Bor du i bostadsrätt gäller avdraget arbete inne i lägenheten som du ansvarar för enligt stadgarna. "
    "Stambyte och att flytta golvbrunnen räknas där inte, medan byte av golvbrunn och plattsättning gör det.",
  ],
  "price_h2": "Vad styr priset på ett badrum i Sollentuna?",
  "price": [
    "Om brunnen, toaletten och duschen får ligga kvar blir arbetet mindre än om något flyttas. Ventilationen "
    "kan också spela in, liksom underlaget i ett äldre hus och ytskikten du väljer. Vi kommer ut gratis och "
    "lämnar ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur vet jag om fläkten i badrummet i vårt radhus i Sollentuna räcker?",
     "Ett enkelt test från kommunen är att imman på spegeln ska vara borta inom 15 minuter efter dusch och att "
     "ventilen ska kunna hålla fast en pappersbit. Klarar den inte det bör frånluften ses över när rummet ändå rivs."),
    ("Behöver vi anmäla en ny fläkt när badrummet renoveras i Sollentuna?",
     "Sollentuna kommun räknar byte av aggregat, fläkt eller kanaler som en större ändring som ska anmälas. "
     "Kontakta kommunen om du är osäker på om just ditt byte omfattas."),
    ("Hur lång tid tar en VA-anmälan i Sollentuna?",
     "Kommunen anger ungefär två till fyra veckor, och längre när många vill bygga. Arbetet får inte börja förrän startbeskedet finns."),
    ("Kan vi behålla golvbrunnen från 1978 när badrummet görs om?",
     "Enligt GVK:s regler ska golvbrunnar från före 1990 bytas vid en påkostad renovering, så räkna med en ny brunn."),
    ("Ändrar en ny takhuv för badrumsfläkten utseendet på villan i Norrvikens villastad?",
     "Den syns, och i ett område där kommunen vill bevara villastadens karaktär bör du fråga kommunen innan "
     "något nytt sätts på tak eller fasad."),
  ],
  "sources": [
    ("Sollentuna kommun – Ventilation (din bostad)", SOL_VENTD),
    ("Sollentuna kommun – Installation eller ändring av ventilation", SOL_VENT),
    ("Sollentuna kommun – Installation eller ändring av vatten och avlopp", SOL_VA),
    ("Sollentuna kommun – Översiktsplan för Sollentuna med sikte på 2040", SOL_OP),
    ("Sollentuna kommun – Kulturhistoriska byggnader och områden", SOL_KULT),
    S_GVK_BRUNN, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i Sollentuna renoveras?", "Boka ett kostnadsfritt besök, så går vi igenom rummet, stammarna och ventilationen."),
  "img": [
    ("Renoverat badrum med frånluftsdon i taket i ett radhus i Sollentuna",
     "renovated bathroom in a Swedish 1980s terraced house, white round exhaust air valve in the white ceiling, "
     "large matte white wall tiles, dark grey floor tiles, wall-hung toilet, shower area with glass wall, soft daylight"),
    ("Radhuslänga från 1980-talet i Sollentuna",
     "long row of low two-storey Swedish 1980s terraced houses with gently pitched gable roofs of dark concrete tiles, "
     "facades of horizontal wooden panel painted pale yellow and grey, small fenced front gardens with birch trees, "
     "footpath in front, Stockholm suburb, overcast autumn day"),
  ],
},

# =============================== BADRUM LIDINGÖ ===============================
"badrumsrenovering-lidingo.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Lidingö", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering på Lidingö – villor, källare och gästhus",
  "description": "Badrumsrenovering på Lidingö: badrum i villastadens äldre villor, källarbadrum och "
                 "golvbrunnar, gästhus med anmälan för VA och utökad lovplikt.",
  "h1": "Badrumsrenovering på Lidingö",
  "lead": "En badrumsrenovering på Lidingö handlar ofta om ett våtrum i en villa från villastadens första "
          "decennier, ett källarbadrum i ett souterränghus i Brevik eller ett nytt badrum i ett gästhus på tomten. "
          "Vi river, bygger upp underlag och tätskikt och samordnar VVS och el, med ROT-avdraget direkt på fakturan.",
  "card": "Villastad, källarbadrum och gästhus.",
  "sections": [
    {"id": "husen", "anchor": "Husen på Lidingö",
     "h2": "Villor från 1900-talets början och radhusbyar från efterkrigstiden",
     "paras": [
       "AB Lidingö Villastad bildades 1906 av ingenjören Hjalmar Arwin, och enligt stadens kulturmiljöprogram "
       "fanns 293 villor i slutet av 1910. Villastadens kärna är byggd ungefär 1905–1930, och på 1940- och "
       "50-talen styckades många stora tomter och fick nya hus. I Brevik står flera villor i souterräng.",
       "Efterkrigstiden gav radhus. Mölna radhusby byggdes 1960–62 med fyrtio radhuslägenheter i sju längor, och "
       "1979 tillkom närmare hundra radhus och kedjehus kring Klarbärsvägen i Käppala.",
       "För badrummet betyder det två olika utgångslägen. I de äldre villorna har badrummet byggts in senare, "
       "kanske flera gånger, och kan ligga i källaren, på övervåningen eller i en gammal jungfrukammare. I "
       "radhusen fanns våtrummet från start och har samma ålder i hela längan.",
     ],
     "aside": {"title": "Lidingös hus i korthet", "items": [
       "Lidingö villastad: villor från ca 1905–1930",
       "Brevik: villor, flera i souterräng",
       "Mölna radhusby: 1960–62",
       "Käppala: radhus och kedjehus 1979"]}},
    {"id": "kallare",
     "h2": "Källarbadrummet och golvbrunnen som ligger lågt",
     "paras": [
       "Lidingö stad skriver på sin " + X.format(LID_SPILL, "sida om spillvatten") + " att fastigheter med lågt "
       "belägna golvbrunnar, främst hus med källare, riskerar att få avloppsvatten upptryckt bakvägen om "
       "avloppsledningen i gatan blir överbelastad, till exempel vid kraftig nederbörd. Det är ett skäl att fråga en VVS-installatör om "
       "skydd mot bakåtströmning när ett källarbadrum byggs om.",
       "Staden påpekar också att det är fastighetsägaren som ansvarar för dag- och dräneringsvatten på tomten, "
       "och att det i första hand ska tas om hand inom fastigheten. Ett badrum i ett souterrängplan har ofta "
       "golv på betong och väggar mot mark, och fukt kan komma både inifrån och utifrån. Innan nytt tätskikt "
       "läggs undersöker vi underlaget och om det finns tecken på markfukt.",
       "Spillvattnet från Lidingö renas i Käppalaverket, och staden ber alla att bara spola ner toalettpapper. "
       "Tops, hårstrån och fett hör till det som oftast orsakar stopp – värt att tänka på när en ny brunn "
       "och nya rör väl är på plats.",
     ],
     "aside": {"title": "Före ett källarbadrum", "items": [
       "Hur ligger golvbrunnen i förhållande till gatan?",
       "Finns skydd mot bakåtströmning?",
       "Är golv och väggar torra?",
       "Vart går dränering och dagvatten?"]}},
    {"id": "gasthus",
     "h2": "Badrum i gästhuset – byggnaden är lovfri, installationerna inte",
     "paras": [
       "Sedan den 1 december 2025 kan ett komplementbostadshus byggas utan bygglov och utan anmälan om det håller "
       "måtten. Men " + X.format(LID_VAD, "Lidingö stad påpekar") + " att ventilation, vattenförsörjning och "
       "avlopp i en sådan byggnad ska anmälas innan installationen görs. Staden nämner också anmälan när en "
       "extra bostad inreds i ett enbostadshus utan bygglov och vid en lovfri tillbyggnad.",
       "Staden lyfter dessutom ett krav som gäller alla åtgärder, oavsett detaljplan och även när inget lov "
       "behövs: det som byggs ska vara väl gestaltat och anpassat till omgivningen. Mer om reglerna för små "
       "hus på tomten finns under " + L.format("attefallshus.html", "attefallshus") + ".",
     ],
     "aside": None},
    {"id": "utseende",
     "h2": "När badrummet syns på utsidan",
     "paras": [
       "Ett nytt badrumsfönster, ett galler för frånluften eller en huv på taket ändrar husets yttre. Enligt "
       + X.format(LID_ANDR, "Lidingö stad") + " gäller utökad lovplikt för de flesta byggnadsåtgärder i "
       "särskilt kulturhistoriskt värdefulla områden, och de syns som ett blått lager i stadens webbkarta. "
       "Kulturmiljöprogrammet antogs den 16 december 2024. Det är inte juridiskt bindande men används som "
       "underlag vid bygglov, och för radhusen på Canadastigen, som är byggnadsminne, är det Länsstyrelsen som prövar ändringar.",
       "Kontrollera därför kartan innan du bestämmer var frånluften ska gå ut. Ska den dras genom taket "
       "samordnar vi genomföringen med takets tätning; mer om taken på ön finns hos "
       + L.format("taklaggare-lidingo.html", "takläggare på Lidingö") + ", och om metoden för tätskikt under "
       + L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Badrumsrenovering på Lidingö steg för steg",
  "steps": [
    ("Platsbesök", "Vi ser rummet, brunnens läge och om badrummet ligger mot mark."),
    ("Karta och regler", "Vi kollar stadens karta om något ändras på fasad eller tak, och vad som ska anmälas."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där arbete och material står för sig."),
    ("Rivning och kontroll", "Rummet öppnas, och vi bedömer fukt, underlag, brunn och rör."),
    ("Rör, el och tätskikt", "Installatörerna gör sitt, golvet byggs med fall och tätskiktet läggs."),
    ("Ytskikt och överlämning", "Kakel, klinker och porslin monteras, och du får egenkontroll och skötselråd."),
  ],
  "rot_h2": "ROT för badrummet på Lidingö",
  "rot": [
    "Rotavdraget ger 30 procent av arbetskostnaden, upp till 50 000 kronor per person och år och 75 000 kronor "
    "ihop med rutavdrag. Vi drar det direkt på fakturan; material och resor ger inget avdrag.",
    "Ett badrum i ett nybyggt fristående gästhus ger inget rotavdrag, eftersom nybyggnad inte räknas som "
    "rotarbete enligt Skatteverket. Ett badrum i villan eller i en tillbyggnad på ett hus som är äldre "
    "än fem år kan däremot ge avdrag.",
  ],
  "price_h2": "Vad påverkar priset för badrummet på Lidingö?",
  "price": [
    "I ett källarbadrum är det fukten och avloppets läge som brukar avgöra, i en äldre villa underlaget och "
    "rördragningen, och i ett gästhus vägen för vatten och avlopp från huvudbyggnaden. Storlek och ytskikt "
    "kommer sedan. Besöket är kostnadsfritt och du får ett skriftligt förslag.",
  ],
  "faq": [
    ("Kan avloppsvatten tränga upp i källarbadrummet i vår villa på Lidingö?",
     "Lidingö stad varnar för att hus med lågt belägna golvbrunnar kan få avloppsvatten upptryckt när ledningen i "
     "gatan är överbelastad. Fråga om skydd mot bakåtströmning när badrummet byggs om."),
    ("Måste vi anmäla badrummet i vårt nya gästhus på Lidingö?",
     "Själva huset kan vara lovfritt, men staden kräver anmälan för vatten, avlopp och ventilation innan de installeras."),
    ("Behövs lov för ett nytt badrumsfönster i Lidingö villastad?",
     "Ligger huset i ett område med utökad lovplikt, det blå lagret i stadens karta, krävs lov för de flesta "
     "ändringar av fasaden. Kontrollera kartan innan du bestämmer dig."),
    ("Ger ett badrum i ett nybyggt gästhus rotavdrag?",
     "Nej. Skatteverket ger inte rotavdrag för att bygga en ny bostad, och det gäller även ett nytt fristående gästhus."),
    ("Vad ska man tänka på med ett badrum i souterrängplanet i Brevik?",
     "Att golv och väggar kan ligga mot mark. Underlaget ska vara torrt innan tätskiktet läggs, och dränering och "
     "dagvatten på tomten är fastighetsägarens ansvar."),
  ],
  "sources": [
    ("Lidingö stad – Spillvatten och avlopp", LID_SPILL),
    ("Lidingö stad – Vad vill du göra? (bygglov och anmälan)", LID_VAD),
    ("Lidingö stad – Ändrade lagar och regler för byggande", LID_ANDR),
    ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet", LID_KMPFAQ),
    ("Lidingö stad – Kulturmiljöprogram del 2: Lidingö villastad (pdf)", "https://share.mediaflow.com/sv/?9OCCB1KE1L"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Mölna radhusby (pdf)", "https://share.mediaflow.com/sv/?3ZCCS1LEFX"),
    ("Lidingö stad – Kulturmiljöprogram del 2: Gåshaga, Killinge och Käppala (pdf)", "https://share.mediaflow.com/sv/?P7CCT1JEFN"),
    S_PBL, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet på Lidingö göras om?", "Boka ett gratis platsbesök, så går vi igenom rummet, brunnen och reglerna."),
  "img": [
    ("Nyrenoverat badrum på övervåningen i en äldre villa på Lidingö",
     "renovated basement bathroom in an old Swedish villa, low ceiling with recessed spotlights, one small horizontal window high up "
     "on the wall at ground level showing grass outside, light beige stone-look floor tiles, white wall tiles, walk-in shower with "
     "glass screen, wooden vanity, no skylight"),
    ("Äldre villa i souterräng bland tallar på Lidingö",
     "early 1900s Swedish plastered villa built into a slope with a visible lower basement floor and small windows, "
     "red clay tile roof, granite rocks and pine trees, Lidingö, early autumn"),
  ],
},

# =============================== BADRUM NACKA ===============================
"badrumsrenovering-nacka.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Nacka", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Nacka – villastad, sommarhus och radhus",
  "description": "Badrumsrenovering i Nacka: badrum i villastäderna vid Saltsjöbanan, permanentade "
                 "sommarhus i Boo och radhus i Älta. Kommunens regler när badrummet flyttas.",
  "h1": "Badrumsrenovering i Nacka",
  "lead": "En badrumsrenovering i Nacka kan gälla en villa från 1890-talet i Saltsjöbaden, ett sommarhus i Boo "
          "som blivit åretruntbostad eller ett radhus i Älta från slutet av 60-talet. Vi river, bygger upp underlag "
          "och tätskikt och samordnar VVS och el – och tar reda på om kommunen ska ha en anmälan först.",
  "card": "Villastäder, sommarhus och radhus.",
  "sections": [
    {"id": "husen", "anchor": "Husen i Nacka",
     "h2": "Villor vid banan, sommarnöjen vid farleden",
     "paras": [
       "Nackas kulturmiljöprogram beskriver två rötter. Saltsjöbaden anlades som bad- och villastad i början av "
       "1890-talet, och 1896 stod ett sextiotal villor klara. Längs Saltsjöbanan följde Neglinge, byggt i "
       "huvudsak 1895–1910, Storängen, som grundades 1904 av en egnahemsförening, och Saltsjö-Duvnäs 1907.",
       "Vid farleden i Boo byggdes sommarvillor från 1860-talet, och i skogsbackarna bakom kom enklare "
       "sportstugor. Från 1930-talet styckades Sommarbo för små fritidshus, ett område där allt fler i dag bor "
       "året runt. I Älta stod det första radhusområdet, 25 hus söder om Erstaviksvägen, klart 1968–69.",
       "Det ger tre typer av badrum. I sekelskiftesvillan har badrummet byggts in i ett hus som inte var ritat "
       "för det. I sommarhuset har det ofta tillkommit när huset permanentades, ibland i en tillbyggnad. I "
       "radhuset finns originalbadrummet kvar om ingen har rört det.",
     ],
     "aside": {"title": "Nackas hus i korthet", "items": [
       "Saltsjöbaden: villastad från 1890-talet",
       "Neglinge, Storängen, Saltsjö-Duvnäs: 1895–1910",
       "Boo: sommarvillor och stugor, många permanentade",
       "Älta: radhus från 1968 och framåt"]}},
    {"id": "flytta",
     "h2": "Flyttar du badrummet räknar Nacka det som en större ändring",
     "paras": [
       "På sin sida om " + X.format(NAC_BAR, "ändring i bärande konstruktioner eller större ändring av planlösning") +
       " ger Nacka kommun flytt av ett badrum som exempel på en sådan ändring. Den ska anmälas, och precis som "
       "vid ett bygglov behövs ett startbesked innan arbetet börjar. Kommunen skickar en bekräftelse med "
       "handläggarens namn ungefär tio dagar efter att anmälan kommit in. Syftet är enligt kommunen att "
       "säkerställa att samhällets krav på bland annat brandsäkerhet, konstruktion och tillgänglighet uppfylls, "
       "och byggnaden får inte tas i bruk förrän det finns ett slutbesked.",
       "Ett badrum som renoveras på samma plats är en annan sak. Om ett stambyte görs i befintligt VA-schakt "
       "räknar " + X.format(NAC_ANDRA, "kommunen") + " det som underhåll som inte behöver anmälas. Läggs nya "
       "stammar i nya lägen som kan påverka bärande konstruktion ska det däremot anmälas, och kommunen påpekar "
       "att en detaljplan kan innehålla krav på anmälan även för underhåll.",
       "Ventilationen följer samma logik. Installeras ett nytt system eller byts aggregat, fläkt, kanaler eller "
       "värmeväxlare på ett sätt som påverkar flöden eller luftkvalitet ska det " + X.format(NAC_VENT, "anmälas") +
       ", och anläggningen får inte användas förrän det finns ett slutbesked.",
     ],
     "aside": {"title": "Anmälan i Nacka – kort", "items": [
       "Badrummet flyttas: anmälan",
       "Stambyte i samma schakt: underhåll",
       "Stammar i nya lägen: anmälan",
       "Nytt fläktsystem: anmälan och slutbesked"]}},
    {"id": "sommarhus",
     "h2": "När sommarhuset i Boo blir helårsbostad",
     "paras": [
       "Ett badrum i ett hus som byggdes för sommarbruk behöver tåla vinter. Golv och väggar i en gammal "
       "stuga kan vara kalla och dåligt isolerade, och ett våtrum med tätskikt mot en kall vägg riskerar "
       "kondens. Vi börjar därför med att se hur väggar och golv är byggda och om de behöver isoleras eller "
       "byggas om innan tätskikt och skivor sätts upp.",
       "Ligger badrummet i en senare tillbyggnad måste skarven mot den gamla stommen vara tät, och avloppet "
       "dras med rätt fall. Kontrollera också om huset har kommunalt vatten och avlopp eller en egen anläggning "
       "– det avgör vad ett nytt badrum får kopplas till.",
       "Kulturmiljöprogrammet för sommarnöjena beskriver hur schweizer- och cottagevillornas plåttak ersattes av "
       "tegel runt sekelskiftet 1900, och husen har ofta långa, utskjutande taksprång. Ska frånluften från ett "
       "nytt badrum ut genom taket på ett sådant hus bör huven placeras så att den inte stör takets uttryck.",
     ],
     "aside": None},
    {"id": "radhus",
     "h2": "Originalbadrummet i ett radhus i Älta",
     "paras": [
       "Ett radhusbadrum från slutet av 1960-talet har nästan säkert en golvbrunn från byggåret, och enligt GVK "
       "ska " + X.format(GVK_BRUNN, "golvbrunnar från före 1990") + " bytas vid en påkostad renovering. Väggen "
       "mot grannen och de gemensamma ledningarna gör det klokt att prata med grannarna innan du sätter igång.",
       "Mer om tätskikt, fall och papper finns under " + L.format("badrumsrenovering.html", "badrumsrenovering i Stockholm") +
       ", och om husens tak under " + L.format("takrenovering-nacka.html", "takrenovering i Nacka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi badrummet i Nacka",
  "steps": [
    ("Besök på plats", "Vi ser rummet, stommen och var stammar och frånluft går."),
    ("Anmälan om rummet flyttas", "Ska badrummet byta plats eller få nya stammar tar vi fram underlag till kommunen."),
    ("Skriftligt förslag", "Arbete och material står var för sig, så att ROT-avdraget syns."),
    ("Rivning och bedömning", "Rummet rivs, och vi bedömer isolering, underlag och rör i öppet läge."),
    ("Uppbyggnad", "Underlag, fall, skivor och tätskikt byggs, och installatörerna drar rör och el."),
    ("Ytskikt och dokument", "Kakel, klinker och porslin monteras, och du får egenkontroll och skötselråd."),
  ],
  "rot_h2": "Rotavdrag för badrummet i Nacka",
  "rot": [
    "Du får 30 procent av arbetskostnaden i rotavdrag, högst 50 000 kronor per person och år och högst 75 000 "
    "kronor sammanlagt med rutavdrag. Vi drar det direkt på fakturan. Material och resor ingår inte.",
    "Ett permanentat sommarhus räknas som småhus, och avdraget gäller om du äger huset och använder det som "
    "permanent- eller fritidsbostad. Är huset yngre än fem år får arbetet bara återställa det till ursprungligt skick.",
  ],
  "price_h2": "Vad styr priset på badrummet i Nacka?",
  "price": [
    "Det som brukar avgöra är om badrummet flyttas, hur väggar och golv i ett äldre hus behöver byggas om och "
    "om brunn och stammar ska bytas. Ytskikt och utrustning kommer därefter. Platsbesöket är gratis och du får "
    "ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste vi anmäla att vi flyttar badrummet i vår villa i Saltsjöbaden?",
     "Ja, Nacka kommun nämner flytt av badrum som exempel på en större ändring av planlösning som ska anmälas och få startbesked."),
    ("Behöver ett stambyte i radhuset i Älta anmälas?",
     "Inte om stammarna läggs i befintligt schakt, enligt kommunen. Nya lägen som kan påverka bärande konstruktion ska anmälas."),
    ("Kan vi bygga ett badrum i ett sommarhus i Boo som vi ska bo i året runt?",
     "Ja, men väggar och golv behöver ofta isoleras eller byggas om först, och avloppet måste ha en godkänd anslutning."),
    ("Vad gäller om vi byter badrumsfläkten mot ett FTX-aggregat?",
     "Ett nytt aggregat eller värmeväxlare som påverkar flödena ska anmälas till Nacka kommun, och det får inte användas förrän slutbesked finns."),
    ("Finns det regler i detaljplanen som påverkar badrummet?",
     "Det kan det. Nacka kommun påpekar att en detaljplan kan kräva anmälan även för underhåll, till exempel ett stambyte."),
  ],
  "sources": [
    ("Nacka kommun – Ändring i bärande konstruktioner eller större ändring av planlösning", NAC_BAR),
    ("Nacka kommun – Andra anmälningar (stambyte, OVK)", NAC_ANDRA),
    ("Nacka kommun – Installation av ventilation", NAC_VENT),
    ("Nacka kommun – Kulturmiljöprogram: Villasamhällen vid järnvägen", NAC_JV),
    ("Nacka kommun – Kulturmiljöprogram: Sommarnöjen vid farleden", NAC_SN),
    ("Nacka kommun – Kulturpromenad i Älta", NAC_ALTA),
    S_GVK_BRUNN, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i Nacka göras om?", "Boka ett kostnadsfritt besök, så går vi igenom rummet och vad som behöver anmälas."),
  "img": [
    ("Nyrenoverat badrum i en äldre villa i Nacka",
     "newly renovated bathroom in a Swedish 1900s wooden villa, white beadboard wainscot above white hexagon floor tiles, "
     "freestanding white bathtub under a tall old window with white frame, chrome fittings, natural daylight"),
    ("Före detta sommarhus i skogen i Boo, Nacka",
     "Swedish early 1900s summer house now a year-round home, red painted wood with white trim and glazed veranda, "
     "a later low extension, standing-seam metal roof, pine forest on a granite slope, Boo Nacka"),
  ],
},

# =============================== BADRUM SOLNA ===============================
"badrumsrenovering-solna.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Solna", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Solna – bostadsrätt, stambyte och villa",
  "description": "Badrumsrenovering i Solna: bostadsrätt och föreningens medgivande, anmälan och "
                 "startbesked, golvbrunn vid stambyte, ROT och villor i kulturmiljöer.",
  "h1": "Badrumsrenovering i Solna",
  "lead": "Ligger badrummet i en bostadsrätt i Solna börjar renoveringen med föreningen, inte med "
          "kaklet. Vi river, bygger upp underlag och tätskikt och samordnar VVS och el, tar fram det underlag "
          "styrelsen och staden kan behöva och drar ROT-avdraget direkt på fakturan.",
  "card": "Bostadsrätt, stambyte och villor.",
  "sections": [
    {"id": "solna", "anchor": "Badrummen i Solna",
     "h2": "Från stenstaden i Råsunda till villorna vid Stocksundet",
     "paras": [
       "Solna stad räknar upp drygt trettio sammanhängande kulturhistoriskt värdefulla miljöer. Flera är "
       "flerbostadshus: Stenstaden i Råsunda, 1950-talsbebyggelsen i Råsunda, Huvudsta och Skytteholm, "
       "Hagalundshusen och Stjärnhusen i Bergshamra. Där ligger badrummen i lägenheter, och stammarna, "
       "ventilationen och den bärande stommen är gemensamma för hela huset.",
       "Villor och radhus finns också. Staden nämner bland annat Råsunda villastad, villabebyggelsen i norra "
       "Råsunda, Råsta egnahem, Alnäs och Stocksundstorp och Solna kyrkby med radhusbebyggelsen. I ett sådant "
       "hus är du själv byggherre, men i gengäld syns allt som ändras på utsidan i en miljö som staden vill bevara.",
     ],
     "aside": {"title": "Kulturmiljöer med badrum i lägenhet", "items": [
       "Stenstaden i Råsunda",
       "1950-talsbebyggelse i Råsunda, Huvudsta och Skytteholm",
       "Hagalundshusen",
       "Stjärnhusen i Bergshamra"]}},
    {"id": "forening",
     "h2": "Föreningens medgivande först, sedan staden",
     "paras": [
       "Enligt bostadsrättslagen får du inte utan styrelsens tillstånd göra ingrepp i bärande konstruktion, "
       "ändra ledningar för avlopp, värme, gas eller vatten eller ändra ventilationen. Solna stad är ännu "
       "tydligare i sin " + X.format(SNA_LGH, "guide för lägenhetsinnehavare") + ": den som bor i en bostadsrätt "
       "behöver alltid fastighetsägarens medgivande för byggåtgärder. Staden råder dig också att kräva att "
       "leverantören följer kontrollplanen och dokumenterar bygget, och att begära slutbesked när allt är klart.",
       "Den kommunala sidan är en anmälan. " + X.format(SNA_VA, "Solna stad") + " kräver anmälan för invändiga "
       "ändringar som väsentligt påverkar en anläggning för vatten eller avlopp i en byggnad, och du måste vänta "
       "på startbesked. Börjar arbetet utan startbesked kan en byggsanktionsavgift tas ut.",
       "Staden " + X.format(SNA_ANM, "anger") + " att ett anmälansärende ska handläggas inom fyra veckor från att "
       "det är komplett, och att du inom tre veckor får besked om något saknas. Ett badrum som renoveras med "
       "brunn, toalett och dusch kvar på samma plats brukar inte behöva anmälas.",
       "Ska en anmälan göras listar staden bland annat en översiktlig beskrivning av projektet, ett förslag "
       "till kontrollplan, plan- och sektionsritning och, om bärande delar berörs, utlåtande från en "
       "konstruktör. Ibland behövs en certifierad kontrollansvarig, och vid större åtgärder kallas du till "
       "ett tekniskt samråd innan startbeskedet ges.",
     ],
     "aside": {"title": "Till styrelsen", "items": [
       "Beskrivning av arbetet och ritning",
       "Vilka regler tätskiktet byggs efter",
       "Vem som gör VVS och el",
       "När rivningsdagarna infaller"]}},
    {"id": "stambyte",
     "h2": "När föreningen byter stammar",
     "paras": [
       "Ett stambyte är ofta det tillfälle då badrummet i en bostadsrätt görs om, eftersom golv och väggar ändå "
       "rivs. GVK:s regler säger att " + X.format(GVK_BRUNN, "golvbrunnar från före 1990") + " ska bytas just vid "
       "stambyte, liksom vid en påkostad renovering eller efter en stor vattenskada.",
       "Fråga föreningen vad som ingår i deras entreprenad och vad som är ditt. Föreningen ansvarar ofta för "
       "stammarna, medan ytskikt, inredning och utrustning är medlemmens – men det avgörs av stadgarna. Den "
       "gränsen styr också rotavdraget, och den avgör vad du kan välja själv när badrummet byggs upp igen.",
       "Vill du samtidigt göra badrummet större är det två frågor till. Att riva en vägg i en bostadsrätt "
       "kräver enligt Solna stad föreningens godkännande, och är väggen bärande krävs dessutom en anmälan om "
       "ändring av bärande konstruktion. Flyttas toalett eller dusch så att avloppet ändras väsentligt kan det "
       "också bli en anmälan om vatten och avlopp. Ta därför med hela planen när du söker tillstånd hos styrelsen, "
       "inte bara ytskikten.",
     ],
     "aside": None},
    {"id": "villa",
     "h2": "Villa i Råsunda eller Stocksundstorp",
     "paras": [
       "I villorna är det utsidan som kräver eftertanke. " + X.format(SNA_VILLA, "Solna stad") + " skriver att "
       "stora delar av staden omfattas av utökad lovplikt, främst på grund av särskilt värdefulla kulturmiljöer "
       "och riksintressen, och att bygglovsbefriade åtgärder " + X.format(SNA_FRIA, "inte kan utföras") + " i "
       "områden som Råsunda villastad, Råsta egnahem och Alnäs och Stocksundstorp. Ett nytt fönster eller en "
       "ny frånluftshuv kan alltså behöva lov.",
       "Inne i huset gäller samma regler som i resten av landet. Hur ett tätskikt ska byggas står under "
       + L.format("badrumsrenovering.html", "badrumsrenovering i Stockholm") + ", och om frånluften ska gå genom "
       "taket finns mer om taken i staden hos " + L.format("taklaggare-solna.html", "takläggare i Solna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Badrummet i Solna steg för steg",
  "steps": [
    ("Besök och stadgar", "Vi ser badrummet och går igenom vad som är ditt och föreningens ansvar."),
    ("Underlag för tillstånd", "Du får en beskrivning av arbetet att lämna till styrelsen, och vid behov till staden."),
    ("Skriftligt förslag", "Kostnadsförslaget skiljer på arbete och material och visar vad som ger ROT."),
    ("Rivning", "Rummet rivs ner till underlaget, och brunn och anslutningar bedöms."),
    ("Uppbyggnad", "Fall, våtrumsskivor och tätskikt byggs, och installatörerna kopplar in rör och el."),
    ("Klart och dokumenterat", "Ytskikt och porslin på plats; egenkontrollen lämnas till dig och föreningen."),
  ],
  "rot_h2": "Rotavdrag i en bostadsrätt i Solna",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
    "tillsammans med rutavdrag. Vi drar det direkt på fakturan.",
    "I en bostadsrätt ska arbetet enligt Skatteverket göras innanför lägenhetens tak, väggar och golv och gälla "
    "sådant du ansvarar för enligt stadgarna. Kakel, klinker, toalett, dusch, handfat och att byta golvbrunn "
    "ger avdrag. Stambyten, att byta eller flytta avloppsrör och att flytta golvbrunnen ger det inte.",
  ],
  "price_h2": "Vad påverkar priset på badrummet i Solna?",
  "price": [
    "I en bostadsrätt spelar det in vad föreningen redan gör vid ett stambyte, hur stort rummet är och vilka "
    "ytskikt du väljer. I en villa tillkommer underlaget och eventuella ändringar av rör och frånluft. Besöket "
    "är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag föreningens godkännande för att renovera badrummet i Råsunda?",
     "Ja. Solna stad skriver att den som bor i bostadsrätt alltid behöver fastighetsägarens medgivande för "
     "byggåtgärder, och bostadsrättslagen kräver styrelsens tillstånd för ändringar av vatten, avlopp och ventilation."),
    ("Hur lång tid tar Solna stad på sig att handlägga en anmälan för badrummet?",
     "Staden anger fyra veckor från att anmälan är komplett, och besked inom tre veckor om något saknas."),
    ("Får jag rotavdrag när föreningen byter stammarna?",
     "Inte för själva stambytet. Arbetet du beställer inne i lägenheten, som plattsättning och byte av golvbrunn, kan däremot ge avdrag."),
    ("Måste golvbrunnen bytas vid stambytet i vårt 50-talshus i Huvudsta?",
     "GVK:s regler säger att golvbrunnar från före 1990 ska bytas vid stambyte, så det är det normala."),
    ("Kan vi sätta ett nytt badrumsfönster i en villa i Råsta egnahem utan lov?",
     "Räkna med att det krävs lov. Solna stad anger att bygglovsbefriade åtgärder inte kan utföras i Råsta egnahem och andra utpekade kulturmiljöer."),
  ],
  "sources": [
    ("Solna stad – För lägenhetsinnehavare (guide till lov och anmälan)", SNA_LGH),
    ("Solna stad – Ändra vatten och avlopp", SNA_VA),
    ("Solna stad – Anmälan, handläggningstider", SNA_ANM),
    ("Solna stad – Kulturmiljöer i Solna", SNA_KULT),
    ("Solna stad – Bygglovsfria åtgärder", SNA_FRIA),
    ("Solna stad – För villaägare (utökad lovplikt)", SNA_VILLA),
    S_BRL, S_GVK_BRUNN, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i Solna renoveras?", "Boka ett kostnadsfritt besök, så går vi igenom rummet och vad föreningen behöver."),
  "img": [
    ("Renoverat badrum i en lägenhet i ett äldre stenhus i Solna",
     "renovated bathroom in a 1910s Swedish stone apartment building, white subway wall tiles, black and white mosaic "
     "floor, tall ceiling, old deep window niche with white frame, walk-in shower with glass screen, chrome fittings"),
    ("Öppet schakt med nya stammar under ett stambyte i ett flerbostadshus",
     "Swedish apartment bathroom during pipe replacement work, all tiles and fixtures removed, rough concrete walls and floor, "
     "an open vertical shaft in the corner with a new grey plastic sewer stack and new copper water pipes, dust, a work lamp on "
     "a tripod, protective plastic sheet over the doorway, no toilet, no towels, no decoration"),
  ],
},

# =============================== BADRUM DANDERYD ===============================
"badrumsrenovering-danderyd.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Danderyd", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Danderyd – villor, ritningar och FTX",
  "description": "Badrumsrenovering i Danderyd: badrum i Djursholms och Stocksunds villor, ritningar ur "
                 "kommunens arkiv, FTX-ventilation och lovplikt i riksintresset.",
  "h1": "Badrumsrenovering i Danderyd",
  "lead": "En badrumsrenovering i Danderyd gäller ofta en stor äldre villa i Djursholm eller Stocksund, där "
          "badrummet byggts om flera gånger och ritningarna kanske ligger i kommunens arkiv. Vi river, bygger "
          "upp underlag och tätskikt och samordnar VVS och el, med ROT-avdraget på fakturan.",
  "card": "Villastäder, ritningar och ventilation.",
  "sections": [
    {"id": "husen", "anchor": "Husen i Danderyd",
     "h2": "Villor från 1890–1930 – och badrum som byggts om i omgångar",
     "paras": [
       "Djursholm grundades 1889 och beskrivs i kommunens översiktsplan som landets första villastad anlagd "
       "som förort. Bebyggelsen speglar främst åren 1890–1930, med stora villor på naturtomter. Stocksund "
       "växte fram parallellt, och sedan 1987 är Djursholms och Stocksunds villastäder riksintressen för "
       "kulturmiljövården. Enebyberg beskrivs i kommunens riktlinjer från 2024 som tydliga årsringar med "
       "bebyggelse från 1700-talet till 1970-talet, med utpekade egnahemsområden.",
       "I en villa från den tiden var badrummet ofta litet eller fanns inte alls från början. Det har "
       "byggts ut, flyttats eller fått sällskap av fler badrum under årens lopp, och varje omgång kan ha "
       "lämnat rör, brunnar och golvlager efter sig. Därför lönar det sig att veta vad som gjorts innan något rivs.",
       "I egnahemsområdena är husen mindre men lika känsliga för förändring. Kommunens riktlinjer säger att "
       "byggnadernas ursprungliga arkitektoniska uttryck ska bevaras och vara vägledande vid om- och "
       "tillbyggnad. Ska badrummet få ett nytt fönster eller hamna i en tillbyggnad är det alltså husets "
       "ursprungliga form som ska styra, inte en standardlösning.",
     ],
     "aside": {"title": "Danderyd i korthet", "items": [
       "Djursholm: grundat 1889",
       "Stocksund: villastad som växte fram samtidigt",
       "Riksintresse för kulturmiljövården sedan 1987",
       "Enebyberg: egnahem och årsringar till 1970-talet"]}},
    {"id": "ritningar",
     "h2": "Beställ husets ritningar innan badrummet rivs",
     "paras": [
       "I " + X.format(DAN_ARK, "kommunens ritningsarkiv") + " kan du beställa bygglovsritningar för nästan alla "
       "byggnader i Danderyd. Där finns handlingar från tidigare lov och anmälningar, bland annat plan-, "
       "sektions- och konstruktionsritningar, teknisk beskrivning och VVA-ritningar. Kommunen påpekar att det "
       "inte är säkert att allt finns, men en gammal VVA-ritning kan visa var stammar och avlopp gick när huset byggdes om senast. "
       "Du kan också själv söka efter handlingarna kostnadsfritt hos Kontaktcenter Danderyd.",
       "Ska badrummet flyttas eller få nya rör behöver kommunen i en anmälan enligt sin "
       + X.format(DAN_INV, "checklista för invändig ändring") + " en VA-ritning med befintliga och tillkommande "
       "rör, eller en ventilationsritning som visar systemet och till- och frånluftsflöden. Ett enklare kartutdrag "
       "räcker, och för villor behövs ingen situationsplan.",
     ],
     "aside": {"title": "Ur arkivet", "items": [
       "Planritningar och sektioner",
       "Konstruktionsritningar",
       "VVA-ritningar",
       "OVK-protokoll där sådana finns"]}},
    {"id": "ventilation",
     "h2": "FX, FTX och badrummets frånluft",
     "paras": [
       "Har villan fått mekanisk ventilation gäller särskilda regler. Enligt " + X.format(DAN_OVK, "kommunens sida om OVK") +
       " ska ett en- eller tvåbostadshus med FX-, FT- eller FTX-ventilation få en funktionskontroll när systemet "
       "installeras, men någon återkommande besiktning krävs inte. Ett nytt aggregat eller en väsentlig ändring av "
       "ventilationen kräver dessutom anmälan enligt plan- och byggförordningen.",
       "I badrummet betyder det att frånluftsdonet ska placeras där fukten finns, och att flödet ska stämma med "
       "systemet i resten av huset. Byggs badrummet större eller flyttas det kan flödena behöva justeras, och då "
       "är det bra att ha ventilationsritningen eller det senaste protokollet till hands.",
       "Kommunen påpekar att det är ägaren som ska se till att kontrollen blir gjord, och att den ska utföras av "
       "en certifierad besiktningsman. Planera därför in funktionskontrollen när ett nytt aggregat sätts upp i "
       "samband med badrummet, så att den inte glöms bort när hantverkarna har gått.",
     ],
     "aside": None},
    {"id": "riksintresse",
     "h2": "Lovplikt i riksintresset – det som syns från gatan",
     "paras": [
       "På sidan om " + X.format(DAN_NY, "nya regler för bygglov") + " skriver Danderyds kommun att det alltid "
       "gäller lovplikt inom kulturhistoriskt värdefulla områden och riksintressen för kulturmiljövården. Ett nytt "
       "badrumsfönster, ett ventilationsgaller i fasaden eller en huv på taket kan därför behöva lov, och du kan "
       "kontrollera din fastighet i kommunens kulturmiljökarta.",
       "Kommunen påminner också om att den som gör en lovfri åtgärd som ökar bruttoarean ansvarar för att "
       "informera kommunens VA-enhet, och att ett komplementbostadshus kan kräva anmälan när vatten, avlopp "
       "eller ventilation installeras. Mer om tätskikt och papper finns under "
       + L.format("badrumsrenovering.html", "badrumsrenovering") + ", och om villornas tak hos "
       + L.format("takrenovering-danderyd.html", "takrenovering i Danderyd") + ".",
     ],
     "aside": {"title": "Kan kräva lov eller anmälan", "items": [
       "Nytt fönster eller galler i riksintresset",
       "Ny huv eller genomföring på taket",
       "Nytt ventilationsaggregat",
       "Badrum i gästhus med VA"]}},
  ],
  "steps_h2": "Så går badrumsrenoveringen i Danderyd till",
  "steps": [
    ("Besök och ritningar", "Vi ser badrummet och går igenom de ritningar du fått ut ur arkivet."),
    ("Regler och karta", "Ändras något på utsidan kollar vi kulturmiljökartan; ändras rör eller ventilation tar vi fram underlag."),
    ("Kostnadsförslag", "Ett skriftligt förslag med arbete och material på egna rader."),
    ("Rivning och inventering", "Gamla golvlager, rör och brunnar tas bort, och stommen bedöms."),
    ("Rör, luft och tätskikt", "Installatörerna drar nytt och justerar frånluften; golv och tätskikt byggs upp."),
    ("Ytskikt och överlämning", "Kakel, klinker och porslin monteras, och du får egenkontroll och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Danderyd",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden. Per person och år får det vara högst 50 000 kronor, och "
    "högst 75 000 kronor tillsammans med rutavdrag. Äger ni villan tillsammans har var och en eget utrymme, "
    "och vi drar avdraget direkt på fakturan.",
    "Skatteverket godkänner bland annat plattsättning, att dra vatten- och avloppsledningar och att montera "
    "toalett, dusch, badkar och handfat i ett småhus. Material och resor ger inget avdrag.",
  ],
  "price_h2": "Vad styr priset på ett badrum i Danderyd?",
  "price": [
    "I en äldre villa är det ofta det som döljer sig under golvet som avgör: lager från tidigare renoveringar, "
    "rörens skick och hur stommen ser ut. Ventilationen, storleken och ytskikten kommer sedan. Besöket är "
    "kostnadsfritt och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi få ut gamla VVS-ritningar för vår villa i Djursholm?",
     "Ofta. I Danderyds ritningsarkiv finns bland annat VVA-ritningar från tidigare lov och anmälningar, men det är inte säkert att allt finns kvar."),
    ("Behöver villan i Stocksund OVK efter att vi installerat FTX?",
     "En funktionskontroll ska göras när systemet installeras, men för en- och tvåbostadshus krävs ingen återkommande besiktning, enligt kommunen."),
    ("Krävs lov för ett nytt badrumsfönster i Djursholms villastad?",
     "Danderyds kommun skriver att det alltid gäller lovplikt i riksintressen för kulturmiljövården, så räkna med det."),
    ("Vilka ritningar behöver kommunen om vi flyttar badrummet?",
     "En VA-ritning med befintliga och nya rör, eller en ventilationsritning om ventilationen ändras, plus en kontrollplan och ett enklare kartutdrag."),
    ("Ska VA-enheten informeras om vi bygger ett badrum i en lovfri tillbyggnad?",
     "Ökar bruttoarean skriver kommunen att fastighetsägaren ansvarar för att informera VA-enheten."),
  ],
  "sources": [
    ("Danderyds kommun – Ritningsarkiv", DAN_ARK),
    ("Danderyds kommun – Checklistor för invändig ändring", DAN_INV),
    ("Danderyds kommun – Obligatorisk ventilationskontroll", DAN_OVK),
    ("Danderyds kommun – Nya regler för bygglov från 1 december 2025", DAN_NY),
    ("Danderyds kommun – Översiktsplan, Riks- och mellankommunala intressen (pdf)", DAN_RIKS),
    ("Danderyds kommun – Riktlinjer för kulturmiljöhistoriska byggnader och miljöer 2024 (pdf)", DAN_RIKTL),
    S_PBF, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i Danderyd göras om?", "Boka ett gratis besök, så går vi igenom rummet, ritningarna och ventilationen."),
  "img": [
    ("Renoverat badrum i en sekelskiftesvilla i Danderyd",
     "spacious renovated bathroom in a large Swedish 1910s national romantic villa, white panelled walls, grey marble-look "
     "floor tiles, freestanding bathtub, double washbasin with wooden cabinet, tall window with small panes, daylight"),
    ("Stor villa från 1910-talet i Djursholm",
     "large Swedish 1910s national romantic villa with steep red clay tile roof, several dormers and a tall chimney, "
     "dark wooden facade, large oak trees and a rocky natural garden, Djursholm, summer"),
  ],
},

}
