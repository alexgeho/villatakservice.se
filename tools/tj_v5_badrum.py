# -*- coding: utf-8 -*-
"""Tjänster v5 (2026-10-25) – ortsidor badrumsrenovering i Tyresö, Värmdö, Haninge, Vallentuna,
Österåker och Botkyrka. Schema: se tools/tj_check.py.
Fakta endast från källorna i respektive 'sources', öppnade 2026-10-25: Tyresö kommun (LTA, Avlopp,
Enskilt vatten och avlopp, Översvämningsrisker och åtgärder, Kranvatten), Värmdö kommun (Ansökan och
anmälan små avlopp, Allmän information om små avlopp, Enskilt dricksvatten, Torra toalettlösningar,
Rådgivning), Haninge kommun (Olika typer av avlopp, Nytt avlopp, Råd tips och risker, Enskilt vatten och
avlopp; VA-rådgivningens presentation Godkända avloppslösningar 2020), Vallentuna kommun (Anslut kommunalt
VA, Enskilt avlopp, Enskilda avlopp – tillsyn, Egen brunn, Dricksvattenkvalitet, Ventilation), Österåkers
kommun (Vatten och avlopp, Avlopp, Dricksvatten, Provtagning av vatten från egen brunn, Vattentjänstplan
2025), Botkyrka kommun (Flytt av kök eller badrum, Anslut till kommunalt vatten och avlopp,
Bygglovsarkiv, Luft ventilation och temperatur, utvecklingsprogrammet Framtid för Tullinge), GVK (gamla
golvbrunnar) och Skatteverket (rotavdrag). Inga priser, garantier utöver lag, omdömen, egna uppdrag i
orterna eller certifikat. Inga produktnamn."""

L = '<a class="text-link" href="{0}">{1}</a>'
X = '<a class="text-link" href="{0}" rel="noopener">{1}</a>'

# ------------------------------------------------------------------ gemensamma källor
S_ROT = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
S_ROTJOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
S_GVK = ("GVK – Gamla golvbrunnar", "https://www.gvk.se/branschregler/golvbrunn/gamla-golvbrunnar/")

# Tyresö
TYR_LTA = "https://www.tyreso.se/boende--miljo/vatten-och-avlopp/avlopp/lta.html"
TYR_AVL = "https://www.tyreso.se/boende--miljo/vatten-och-avlopp/avlopp.html"
TYR_ENSK = "https://www.tyreso.se/boende--miljo/vatten-och-avlopp/avlopp/enskilt-vatten-och-avlopp.html"
TYR_OVS = "https://www.tyreso.se/boende--miljo/vatten-och-avlopp/oversvamningsrisker-och-atgarder.html"
TYR_KRAN = "https://www.tyreso.se/boende--miljo/vatten-och-avlopp/kranvatten.html"
# Värmdö
VAR_ANS = "https://www.varmdo.se/byggabomiljo/vattenochavlopp/smaavlopp/ansokomsmaavlopp.4.1a82111d16e6c321a368eb23.html"
VAR_ALLM = ("https://www.varmdo.se/byggabomiljo/vattenochavlopp/smaavlopptorratoalettlosningarochenskiltvatten/"
            "allmaninformationomsmaavloppochenskiltvatten.4.6111564a196f13870e664bd.html")
VAR_DV = ("https://www.varmdo.se/byggabomiljo/vattenochavlopp/smaavlopptorratoalettlosningarochenskiltvatten/"
          "enskiltdricksvatten.4.1a82111d16e6c321a3692f45.html")
VAR_TORR = ("https://www.varmdo.se/byggabomiljo/vattenochavlopp/smaavlopptorratoalettlosningarochenskiltvatten/"
            "torratoalettlosningar.4.1a82111d16e6c321a368eb79.html")
VAR_HUB = "https://www.varmdo.se/byggabomiljo/vattenochavlopp/smaavlopptorratoalettlosningarochenskiltvatten.4.1a82111d16e6c321a368eacc.html"
VAR_RAD = ("https://www.varmdo.se/byggabomiljo/vattenochavlopp/smaavlopptorratoalettlosningarochenskiltvatten/"
           "radgivningenskiltvattenochsmaavlopp.4.1a82111d16e6c321a368ec40.html")
# Haninge
HAN_BASE = "https://www.haninge.se/bygga-trafik-och-miljo/vatten-och-avlopp/enskilt-vatten-och-avlopp/"
HAN_TYPER = HAN_BASE + "olika-typer-av-avlopp/"
HAN_NYTT = HAN_BASE + "nytt-avlopp/"
HAN_RAD = HAN_BASE + "rad-tips-och-risker/"
HAN_GODK = "https://haninge.se/siteassets/bygga-bo-och-miljo/vatten-och-avlopp/dokument-va/godkanda-avloppslosningar.pdf"
# Vallentuna
VAL_ANSL = "https://vallentuna.se/bygga-bo-och-miljo/vatten-och-avlopp/anslut-kommunalt-va"
VAL_ENSK = "https://vallentuna.se/bygga-bo-och-miljo/vatten-och-avlopp/enskilt-avlopp"
VAL_TILLS = "https://vallentuna.se/bygga-bo-och-miljo/miljo-energi-och-halsoskydd/enskilda-avlopp---tillsyn"
VAL_BRUNN = "https://vallentuna.se/bygga-bo-och-miljo/vatten-och-avlopp/egen-brunn"
VAL_KVAL = "https://vallentuna.se/bygga-bo-och-miljo/vatten-och-avlopp/dricksvattenkvalitet"
VAL_VENT = "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/behover-jag-bygglov/ventilation"
# Österåker
OST_VA = "https://www.osteraker.se/byggabomiljo/vattenochavlopp.4.367d658917909e8fc2b3a4.html"
OST_AVL = "https://www.osteraker.se/byggabomiljo/vattenochavlopp/avlopp.4.367d658917909e8fc2b7b5.html"
OST_DV = "https://www.osteraker.se/byggabomiljo/vattenochavlopp/dricksvatten.4.367d658917909e8fc2b785.html"
OST_PROV = ("https://www.osteraker.se/byggabomiljo/vattenochavlopp/dricksvatten/egetdricksvatten/"
            "provtagningavvattenfranegenbrunn.4.27d4a62417c1135094211b2.html")
OST_VTP = ("https://www.osteraker.se/download/18.40523b741958b6adf7467a/1742387510042/"
           "Vattentj%C3%A4nstplan%20f%C3%B6r%20%C3%96ster%C3%A5kers%20kommun%202025-01-10.pdf")
# Botkyrka
BOT_B = "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/"
BOT_FLYTT = BOT_B + "sa-soker-du-bygglov/bygglov-a-o/flytt-av-kok-eller-badrum"
BOT_ANSL = BOT_B + "ovriga-byggrelaterade-tillstand/anslut-till-kommunalt-vatten-och-avlopp"
BOT_ARK = BOT_B + "sa-soker-du-bygglov/bygglov-a-o/bygglovsarkiv"
BOT_LUFT = "https://www.botkyrka.se/boende-och-narmiljo/bostad-och-tradgard/luft-ventilation-och-temperatur"
BOT_TULL = "https://botkyrka.se/download/18.1fbbaae6170bff9469deb44/1584093808003/Tullinge%20utvecklingsprogram.pdf"

PAGES_TJ = {

# =============================== BADRUM TYRESÖ ===============================
"badrumsrenovering-tyreso.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Tyresö", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Tyresö – LTA, källare och avlopp",
  "description": "Badrumsrenovering i Tyresö: badrum när huset får LTA-avlopp, källarbadrum och golvbrunn, "
                 "kommunens regler för VA-ändringar och ROT direkt på fakturan.",
  "h1": "Badrumsrenovering i Tyresö",
  "lead": "I Tyresö avgörs ett nytt badrum ofta av det som händer utanför huset: en pumpstation för lätt "
          "trycksatt avlopp på tomten, en källare där vatten kan tränga upp genom golvbrunnen eller en egen "
          "avloppsanläggning som ska ta emot mer vatten. Geal Entreprenad AB river, bygger tätskikt och "
          "samordnar VVS och el, och vi går igenom hur avloppet fungerar innan rummet ritas.",
  "card": "LTA-avlopp, källarbadrum och golvbrunn.",
  "sections": [
    {"id": "lta", "anchor": "Badrum och LTA",
     "h2": "När avloppet pumpas bort i stället för att rinna",
     "paras": [
       "På " + X.format(TYR_LTA, "Tyresö kommuns sida om LTA") + ", lätt trycksatt avlopp, förklaras skillnaden "
       "mot ett vanligt system. I ett konventionellt system rinner avloppsvattnet med självfall till "
       "huvudledningen. Med LTA behövs en pumpenhet på fastigheten som pumpar bort det. Fastighetsägaren ordnar "
       "och bekostar allt arbete på tomten fram till förbindelsepunkten, medan kommunens del är ledningen i gatan.",
       "Att installera stationen och dra rör på tomten är enligt kommunen anmälningspliktigt. I ansökan om "
       "startbesked ska det framgå var stationen ska stå och hur rören dras mellan byggnaden, stationen och "
       "förbindelsepunkten. Installationen ska fotodokumenteras i öppet schakt, och stationen behöver en "
       "elförsörjning som är installerad av en elektriker. Ordningen är bestämd: startbesked, beställning och "
       "installation, skriftligt besked om att förbindelsepunkten är upprättad, anläggningsavgift och sist driftsättning.",
       "För badrummet betyder det att rördragningen från huset ritas in redan i anmälan. Ska badrummet flyttas, "
       "få en ny golvbrunn eller kompletteras med ett andra våtrum är det därför klokt att bestämma det innan "
       "anmälan skickas, i stället för att koppla den nya stationen till gamla rör och ändra senare.",
     ],
     "aside": {"title": "LTA i rätt ordning", "items": [
       "Startbesked för station och rör",
       "Installation med foto i öppet schakt",
       "Besked om förbindelsepunkten",
       "Avgift och sedan driftsättning"]}},
    {"id": "eget-avlopp",
     "h2": "Fler duschar på en egen avloppsanläggning",
     "paras": [
       "Saknar fastigheten kommunalt avlopp krävs tillstånd för att inrätta ett enskilt avlopp. På "
       + X.format(TYR_ENSK, "sidan om enskilt vatten och avlopp") + " skriver kommunen också att du ska anmäla "
       "om du ändrar en anläggning så att avloppsvattnets mängd eller sammansättning ändras väsentligt. Ett nytt "
       "badrum med dusch och toalett i ett hus som tidigare hade ett enkelt våtrum kan vara en sådan ändring, "
       "och det är kommunen som gör bedömningen.",
       "Slamavskiljare och slutna tankar ska tömmas av kommunens entreprenör, och det är inte tillåtet att anlita "
       "någon annan för tömningen. Ansluts huset senare till det kommunala nätet ska den gamla anläggningen tas "
       "ur bruk, och slamtjänsten sägs upp separat eftersom det inte sker automatiskt.",
       "Har huset egen brunn påminner kommunen om att hålla koll på vattennivå och vattenkvalitet och använda "
       "vattnet hållbart, så att risken för saltvatteninträngning minskar. Inför ett nytt avlopp kan du boka den "
       "kostnadsfria VA-rådgivning som Tyresö delar med Haninge och Nynäshamn.",
     ],
     "aside": None},
    {"id": "kallare",
     "h2": "Källarbadrummet och vatten som tränger upp",
     "paras": [
       "Kommunens " + X.format(TYR_OVS, "sida om översvämningsrisker") + " beskriver hur vatten kan tränga upp "
       "genom golvbrunn och spygatter när dagvattensystemet inte hinner leda bort allt vatten vid kraftigt regn. "
       "Vid stopp i avloppet kan vatten komma in i källaren även i torrt väder, och risken för stopp är störst i "
       "fastighetens egen ledning. Trädrötter i rörskarvar och ledningar som skadats av sättningar är två av "
       "orsakerna som kommunen nämner.",
       "Ett enkelt test finns på samma sida. Lyft på locket till rensbrunnen vid förbindelsepunkten: står det "
       "vatten i den sitter stoppet i kommunens ledning, är den tom sitter det i fastighetens. Kommunen skriver "
       "också att den inte betalar ersättning för översvämningsskador om avloppet i gatan byggts om till ett "
       "tvådelat system och fastigheten trots uppmaning inte separerat sitt eget avlopp.",
       "Fastighetens VA-system ska enligt kommunen vara väl underhållet, inte minst anordningarna som skyddar "
       "mot inträngande avloppsvatten, och alla förändringar av fastighetens VA-system ska godkännas av tekniska "
       "kontoret. Ett nytt källarbadrum är alltså en fråga för kommunen redan på ritningsstadiet. Marken runt "
       "huset ska luta bort från fasaden, minst 15 centimeter på de första tre metrarna enligt kommunens "
       "tumregel. Stuprör och rännor hör till samma sak, se " + L.format("taklaggare-tyreso.html", "takläggare i Tyresö") + ".",
     ],
     "aside": {"title": "Före ett källarbadrum", "items": [
       "Skydd mot inträngande avloppsvatten",
       "Rensbrunn vid förbindelsepunkten",
       "Separerat spill- och dagvatten?",
       "Mark som lutar bort från huset"]}},
    {"id": "vatten",
     "h2": "Mjukt vatten och ventiler som går att stänga",
     "paras": [
       "Det kommunala dricksvattnet i Tyresö kommer från Mälaren och distribueras av Stockholm Vatten. På "
       + X.format(TYR_KRAN, "sidan om kranvatten") + " anger kommunen en hårdhet på 4–5 dH, vilket räknas som "
       "mjukt, och skriver att disk- och tvättmaskin därför inte behöver något avhärdningsmedel. Har huset egen "
       "brunn kan vattnet vara ett helt annat, och då är ett vattenprov ett bra underlag innan nya blandare väljs.",
       "Läckande installationer är en annan orsak till vattenskador som kommunen tar upp. Råden är att byta "
       "äldre vatteninstallationer som är i dåligt skick, att stänga huvudventilerna vid vattenmätaren om du är "
       "borta en längre tid och att sätta avstängningsventiler på till exempel tvättmaskinen. I ett nytt "
       "badrum planerar vi in avstängningar som går att nå utan att något behöver rivas.",
       "Ska köket kopplas om samtidigt finns mer under " + L.format("koksrenovering-tyreso.html", "köksrenovering i Tyresö")
       + ", och om snickeriet i en stuga som byggs om under " + L.format("snickare-tyreso.html", "snickare i Tyresö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Tyresö",
  "steps": [
    ("Besök och avloppsfrågan", "Vi ser rummet och tar reda på om huset har självfall, LTA eller egen anläggning."),
    ("Ledningar och källare", "Rensbrunn, golvbrunn och ledningar bedöms, liksom risken för inträngande vatten."),
    ("Underlag till kommunen", "Ändras VA-installationen tar vi fram ritningar och underlag för anmälan."),
    ("Skriftligt förslag", "Rivning, tätskikt, VVS, el och ytskikt står som egna poster."),
    ("Rivning och uppbyggnad", "Fall mot ny golvbrunn, våtrumsskivor och tätskikt; installatörerna drar rör och el."),
    ("Ytskikt och genomgång", "Kakel, klinker och porslin monteras, och vi visar var avstängningarna sitter."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Tyresö",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag. För ett småhus räknar Skatteverket bland annat kakel- och klinkersättning, att "
    "dra in och reparera vatten- och avloppsledningar och att installera vattenmätarkonsol och vattenfelsbrytare som rotarbete.",
    "Att filma avloppsrören ger däremot inget avdrag, inte ens i samband med annat rotarbete, och inte heller "
    "slamsugning och tömning av septiktankar. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Tyresö?",
  "price": [
    "Om avloppet går med självfall, via en LTA-station eller till en egen anläggning, om badrummet ligger i "
    "källaren, om golvbrunn och ledningar behöver bytas och vilka ytskikt du väljer. Platsbesöket är gratis, "
    "och du får ett skriftligt kostnadsförslag innan något beställs.",
  ],
  "faq": [
    ("Kan badrummet byggas om innan LTA-stationen på vår tomt i Tyresö är i drift?",
     "Rummet kan byggas, men anslutningen mot det kommunala nätet tas i bruk först när stationen är driftsatt. "
     "Kommunen påpekar att testkörningen kräver vatten, så brunnen behöver fungera om kommunalt vatten ännu inte finns."),
    ("Hur vet vi om stoppet i källarens golvbrunn sitter i vår ledning eller kommunens?",
     "Lyft på locket till rensbrunnen vid förbindelsepunkten. Står det vatten i den sitter stoppet i kommunens "
     "ledning enligt Tyresö kommun, och är den tom sitter det i fastighetens."),
    ("Behöver ett nytt källarbadrum i Tyresö godkännas av kommunen?",
     "Kommunen skriver att alla förändringar av fastighetens VA-system ska godkännas av tekniska kontoret. "
     "Kontakta kommunen innan nya ledningar dras."),
    ("Måste vi anmäla vår egen avloppsanläggning när vi bygger ett andra badrum?",
     "Ja, om ändringen gör att avloppsvattnets mängd eller sammansättning ändras väsentligt. Det är kommunen "
     "som bedömer det, så fråga innan bygget börjar."),
    ("Får vi anlita en annan firma än kommunens för att tömma slamavskiljaren i Tyresö?",
     "Nej. Slamavskiljare och slutna tankar ska tömmas av kommunens entreprenör."),
  ],
  "sources": [
    ("Tyresö kommun – LTA (lätt trycksatta avlopp)", TYR_LTA),
    ("Tyresö kommun – Enskilt vatten och avlopp", TYR_ENSK),
    ("Tyresö kommun – Översvämningsrisker och åtgärder", TYR_OVS),
    ("Tyresö kommun – Kranvatten", TYR_KRAN),
    ("Tyresö kommun – Avlopp", TYR_AVL),
    ("Haninge kommun – Enskilt vatten och avlopp (VA-rådgivning för Haninge, Tyresö och Nynäshamn)", HAN_BASE),
    S_ROTJOB, S_ROT,
  ],
  "cta": ("Ska badrummet i Tyresö göras om?", "Boka ett gratis besök, så går vi igenom rummet och avloppet på plats."),
  "img": [
    ("Nyrenoverat badrum med duschhörna i en villa i Tyresö",
     "newly renovated small basement bathroom in a Swedish 1960s villa, light grey large floor tiles sloping to a square "
     "stainless steel floor drain, white wall tiles, walk-in shower with clear glass screen, small high basement window "
     "with daylight, white washbasin cabinet, clean and empty"),
    ("Locket till en nedgrävd avloppspumpstation på en villatomt i Tyresö",
     "small round dark grey plastic lid of a buried sewage pump station set in a freshly laid lawn next to a red painted "
     "wooden Swedish house, a narrow strip of new turf showing where a pipe trench was dug, pine trees and granite rocks, overcast day"),
  ],
  "related": [],
},

# =============================== BADRUM VÄRMDÖ ===============================
"badrumsrenovering-varmdo.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Värmdö", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering på Värmdö – brunn, salt och avlopp",
  "description": "Badrumsrenovering på Värmdö: när brunnsvattnet är salt, snålspolande dusch och toalett, "
                 "tillstånd för avlopp och torrtoalett och ROT på fakturan.",
  "h1": "Badrumsrenovering på Värmdö",
  "lead": "På Värmdö saknar cirka 13 500 fastigheter kommunalt vatten och avlopp, och där börjar ett "
          "badrumsprojekt med två frågor: hur mycket vatten brunnen tål och vart avloppet tar vägen. "
          "Geal Entreprenad AB river, bygger tätskikt och ytskikt och samordnar VVS och el, och vi planerar "
          "badrummet efter de förutsättningar som gäller på just din tomt.",
  "card": "Brunnsvatten, salt och eget avlopp.",
  "sections": [
    {"id": "brunnen", "anchor": "Brunnen och badrummet",
     "h2": "Ett badrum som brunnen orkar med",
     "paras": [
       "Värmdö kommun skriver på " + X.format(VAR_DV, "sidan om enskilt dricksvatten") + " att grundvattennivån "
       "under sommarhalvåret är låg på många håll i landet, samtidigt som uttagen ofta är som störst, och att "
       "risken för både grundvattenbrist och saltvatteninträngning ökar i kustnära områden. Eftersom Värmdö är "
       "en skärgårdskommun med många kustnära fastigheter uppmanar kommunen till extra försiktighet med vattnet på sommaren.",
       "Det förebyggande rådet handlar om förbrukningen. Kommunen nämner att vattenförbrukande installationer "
       "som duschmunstycke, toalettstol och disk- och tvättmaskin kan bytas mot mer snålspolande alternativ, och "
       "att läckande ledningar, kranar och toalettstolar bör lagas så snart läckan har upptäckts. När badrummet "
       "ändå görs om är det enkelt att välja snålare armaturer och en toalett med mindre spolvolym.",
       "Det är fastighetsägaren som ansvarar för sin enskilda brunn. Sinar den kan vatten hämtas i dunkar vid "
       "kommunens tappställen, men kommunen ordnar inte utkörning av vatten eller möjlighet att duscha och tvätta. "
       "Ett badkar eller en dusch med stort flöde är därför ett val som bör vägas mot vad brunnen ger.",
     ],
     "aside": {"title": "Vattensnålt badrum", "items": [
       "Snålspolande duschmunstycke",
       "Toalett med liten spolvolym",
       "Kranar och toalett som inte läcker",
       "Läckor lagade direkt"]}},
    {"id": "klorid",
     "h2": "Salt i brunnen och korrosion i installationen",
     "paras": [
       "Förhöjda kloridhalter är enligt kommunen en indikation på att grundvattnet påverkats av saltvatten, "
       "vilket är ett vanligt förekommande problem i Värmdö kommun. Kommunen hänvisar till Livsmedelsverket: vid "
       "kloridhalter över 100 mg/l är vattnet tjänligt med anmärkning, halter över 100 mg/l kan påskynda "
       "korrosion och halter över 300 mg/l kan ge smakförändringar. Redan över 50 mg/l tyder halten på saltvatteninträngning.",
       "Förhöjd korrosion kan dessutom leda till högre halter av metaller i vattnet från en anläggning. För "
       "badrummet är det ett skäl att ta ett vattenprov innan nya rör och blandare väljs. Kommunen rekommenderar "
       "prov minst vart tredje år för en enskild dricksvattenbrunn, och minst en gång per år om fler än två "
       "fastigheter delar brunn eller om det finns små barn i hushållet.",
       "Den viktigaste åtgärden vid förhöjda kloridhalter är att minska uttaget. Kommunen föreslår också att se "
       "över pumpen och dess placering i brunnen, eftersom äldre pumpar ofta har för hög kapacitet och tar mycket "
       "vatten vid ett och samma tillfälle. Hur analysresultaten ska tolkas kan du få hjälp med i kommunens "
       + X.format(VAR_RAD, "oberoende och kostnadsfria rådgivning") + ".",
     ],
     "aside": {"title": "Klorid i brunnsvattnet", "items": [
       "Över 50 mg/l: tecken på saltvatten",
       "Över 100 mg/l: kan påskynda korrosion",
       "Över 300 mg/l: kan ändra smaken",
       "Prov minst vart tredje år"]}},
    {"id": "toalett",
     "h2": "Torrtoalett, vattentoalett och tillstånd",
     "paras": [
       "Har huset i dag en torrtoalett och ett avlopp bara för bad-, disk- och tvättvatten blir badrummet en "
       "avloppsfråga. Kommunen skriver att " + X.format(VAR_TORR, "alla torrtoaletter kräver tillstånd") + " och att "
       "det dessutom behövs dispens för att hantera latrin och urin på den egna fastigheten. Spolvatten får inte "
       "anslutas till en torrtoalett.",
       "Ska huset få en vattentoalett behöver WC-vattnet ett godkänt omhändertagande. Enligt "
       + X.format(VAR_ANS, "sidan om ansökan och anmälan för små avlopp") + " krävs tillstånd för en helt ny "
       "anläggning, oavsett om den är för WC, för WC och BDT eller bara för BDT, och även när den ersätter en "
       "befintlig. Kommunens tabell över skyddsnivåer anger sluten tank som godkänd för WC vid både normal och "
       "hög skyddsnivå. Ett byte av slamavskiljare eller sluten tank med likvärdig funktion på samma plats "
       "kräver däremot varken tillstånd eller anmälan.",
       "Kommunen räknar med omkring två till tre månader från att handläggningen påbörjats innan gräv- och "
       "anläggningsarbetet kan börja, och sommaren kan ta längre tid. Till ansökan hör en situationsplan där "
       "anläggningen ritas in tillsammans med vattenbrunnar inom 100 meter och energibrunnar inom 50 meter. Vi "
       "lägger därför rivningen inne i huset så att den inte börjar innan beslutet finns.",
     ],
     "aside": None},
    {"id": "kopa",
     "h2": "Nyköpt hus med eget avlopp",
     "paras": [
       "I Värmdö kommun är det oftast hög skyddsnivå, skriver kommunen i sin " + X.format(VAR_ALLM, "allmänna information om små avlopp")
       + ", på grund av tunna jordlager och närheten till sjöar, vattendrag och enskilda dricksvattenbrunnar. "
       "Den som köper ett hus med enskild VA-försörjning har undersökningsplikt och bör bland annat kontrollera "
       "att avloppsanläggningen har ett giltigt tillstånd och om det finns krav på åtgärder.",
       "Det är viktigt för badrummet, eftersom ett tillstånd gäller för precis den tekniska lösning och den "
       "placering som har prövats. Vill du byta fabrikat på reningsanläggningen eller flytta den behövs ett nytt "
       "tillstånd. Ett badrum som planeras utifrån en anläggning utan giltigt tillstånd kan alltså behöva ritas om.",
       "Ska ett fritidshus göras om till helårsbostad hänger badrummet ofta ihop med kök och tak. Mer om det "
       "finns under " + L.format("koksrenovering-varmdo.html", "köksrenovering på Värmdö") + " och "
       + L.format("takrenovering-varmdo.html", "takrenovering på Värmdö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi ett badrum på Värmdö",
  "steps": [
    ("Besök på tomten", "Vi ser badrummet, brunnen och avloppsanläggningen och frågar hur många som bor i huset."),
    ("Vattenprov och tillstånd", "Vi går igenom provsvar och avloppstillstånd, så att badrummet passar anläggningen."),
    ("Kostnadsförslag", "Rivning, tätskikt, VVS, el och ytskikt står var för sig i ett skriftligt förslag."),
    ("Väntan på beslut", "Krävs tillstånd för avloppet börjar rivningen först när kommunen har beslutat."),
    ("Bygge", "Golvbrunn, fall, våtrumsskivor och tätskikt; vattensnåla armaturer monteras."),
    ("Genomgång", "Vi går igenom badrummet med dig och lämnar egenkontroll och skötselråd."),
  ],
  "rot_h2": "Rotavdrag för badrummet på Värmdö",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr ihop med "
    "rutavdrag. Material och resor ingår inte.",
    "För ett småhus räknar Skatteverket att byta flottör, packningar, silar eller andra delar av toaletter och "
    "handfat som rotarbete, liksom markarbeten för avlopp som infiltrationsanläggningar. Slamsugning och tömning "
    "av septiktankar ger däremot inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden på Värmdö?",
  "price": [
    "Hur badrummet ansluts till avloppet, om en ny anläggning eller sluten tank behövs, hur långt ledningarna "
    "ska dras och vilka armaturer och ytskikt du väljer. Besöket kostar inget, och du får ett skriftligt "
    "kostnadsförslag innan arbetet börjar.",
  ],
  "faq": [
    ("Hur hög kloridhalt i brunnen tyder på saltvatten på Värmdö?",
     "Enligt kommunen tyder halter redan över 50 mg/l på saltvatteninträngning, och över 100 mg/l kan vattnet "
     "påskynda korrosion i installationen."),
    ("Behöver torrtoaletten i vårt fritidshus på Värmdö tillstånd?",
     "Ja. Kommunen skriver att alla torrtoaletter kräver tillstånd, och att det dessutom behövs dispens för att "
     "hantera latrin och urin på den egna fastigheten."),
    ("Kräver ett byte av den slutna tanken tillstånd på Värmdö?",
     "Nej, inte om den nya tanken har likvärdig funktion och placeras på samma ställe. En helt ny anläggning "
     "kräver däremot tillstånd."),
    ("Hur lång tid tar ett avloppstillstånd på Värmdö?",
     "Kommunen räknar med ungefär två till tre månader från att handläggningen påbörjats, och sommaren kan ta längre tid."),
    ("Vad ska vi kontrollera om vi köper hus med eget avlopp på Värmdö och vill bygga nytt badrum?",
     "Att avloppsanläggningen har giltigt tillstånd och om det finns krav på åtgärder. Tillståndet gäller bara "
     "den lösning och placering som prövats."),
  ],
  "sources": [
    ("Värmdö kommun – Enskilt dricksvatten", VAR_DV),
    ("Värmdö kommun – Ansökan och anmälan små avlopp", VAR_ANS),
    ("Värmdö kommun – Torra toalettlösningar", VAR_TORR),
    ("Värmdö kommun – Allmän information om små avlopp och enskilt vatten", VAR_ALLM),
    ("Värmdö kommun – Små avlopp, torra toalettlösningar och enskilt vatten", VAR_HUB),
    ("Värmdö kommun – Rådgivning enskilt vatten och små avlopp", VAR_RAD),
    S_ROTJOB, S_ROT,
  ],
  "cta": ("Ska badrummet på Värmdö göras om?", "Boka ett gratis besök, så tittar vi på badrummet, brunnen och avloppet."),
  "img": [
    ("Ljust badrum med vattensnål dusch i ett helårsbostad på Värmdö",
     "bright newly renovated bathroom in a converted Swedish archipelago house, white painted wooden ceiling boards, "
     "light grey floor tiles, white wall tiles, compact walk-in shower with a small water-saving shower head and glass "
     "screen, window with a view of pine trees and a glimpse of the Baltic sea, clean and empty"),
    ("Borrad brunn på berget intill ett hus på Värmdö",
     "a short plain black steel water well casing pipe, about 40 cm tall with a flat round cap, sticking straight up from "
     "moss-covered granite bedrock in a garden next to a falu red wooden house with white corners, windswept pines and a "
     "glimpse of the Baltic archipelago behind, late summer daylight"),
  ],
  "related": [],
},

# =============================== BADRUM HANINGE ===============================
"badrumsrenovering-haninge.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Haninge", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Haninge – vakuumtoalett och sluten tank",
  "description": "Badrumsrenovering i Haninge: ny vattentoalett till sluten tank, vakuum eller urinsortering, "
                 "avlopp på öarna, kommunens arkiv och ROT direkt på fakturan.",
  "h1": "Badrumsrenovering i Haninge",
  "lead": "Där ett hus i Haninge har eget avlopp styr kommunens krav på kretsloppsanpassad teknik hur ett nytt "
          "badrum kan byggas, från toalettens spolvolym till var tanken ska stå. Geal Entreprenad AB river, "
          "bygger tätskikt och ytskikt och samordnar VVS och el, och vi planerar toalett, golvbrunn och ledningar "
          "efter den avloppslösning som är godkänd för fastigheten.",
  "card": "Vakuumtoalett, sluten tank och öarna.",
  "sections": [
    {"id": "kretslopp", "anchor": "Krav på ny toalett",
     "h2": "En ny vattentoalett ska spola mindre än en liter",
     "paras": [
       "Haninge kommun skriver på sidan om " + X.format(HAN_TYPER, "olika typer av avlopp") + " att det bästa "
       "alternativet för ett enskilt avlopp är en kretsloppsanpassad lösning med två separata rör: ett för "
       "toalettvattnet och ett för vatten från bad, disk och tvätt. Om du installerar en ny vattentoalett krävs "
       "en toalett som spolar mindre än en liter per spolning i genomsnitt, kombinerad med en separat rening av "
       "BDT-vattnet. Vid nybyggnation och när det är skäligt att separera WC-vattnet krävs kretsloppsanpassad "
       "teknik, även om undantag kan förekomma.",
       "För ett nytt avlopp med WC-vatten är enligt " + X.format(HAN_NYTT, "sidan om nytt avlopp") + " bara "
       "vakuumtoalett eller urinsorterande toalett tillåten, och WC-vattnet ska gå till en sluten tank. Att koppla "
       "en vattentoalett till ett befintligt avlopp hör till de åtgärder som kräver ansökan eller anmälan, liksom "
       "att ändra placering av anläggningen eller installera en ny typ av anläggning.",
       "Skälet är kretsloppet. WC-vatten är näringsrikt och innehåller mindre tungmetaller än BDT-vatten, och "
       "kommunen samlar in det i slutna tankar, behandlar det så att det blir hygieniskt och använder det som "
       "gödsel på åkermark. Därför ska bara kiss, bajs och toalettpapper spolas ner.",
     ],
     "aside": {"title": "Haninges krav i korthet", "items": [
       "Under en liter per spolning",
       "Vakuum- eller urinsorterande toalett",
       "Sluten tank för WC-vattnet",
       "Egen rening för bad, disk och tvätt"]}},
    {"id": "toaletten",
     "h2": "Vakuum eller urinsortering – det märks i badrummet",
     "paras": [
       "En vakuumtoalett spolar enligt kommunen 0,5–0,7 liter per spolning och transporterar avfallet med luft, så "
       "ledningarna behöver ingen lutning. Kommunen rekommenderar den för permanentboende. För badrummet innebär "
       "det större frihet att placera toaletten, eftersom den inte behöver ligga där ett självfall räcker fram till tanken.",
       "En urinsorterande vattentoalett har separata hål för urin och latrin och spolar ungefär en liter. "
       "Kommunen bedömer att den inte är lämplig för permanentboende, eftersom den ger fler tömningar och kräver "
       "en annorlunda användning och rengöring. VA-rådgivningens presentation om "
       + X.format(HAN_GODK, "godkända avloppslösningar") + " beskriver också att den urinsorterande toaletten "
       "använder självfall och kräver fall till den slutna tanken, medan vakuumtoaletten klarar klena ledningar.",
       "Valet påverkar alltså både var toaletten kan stå, hur golvet byggs upp och hur ledningarna dras genom "
       "huset. Vi bestämmer toalettyp innan underlaget i rummet byggs, så att fall, ledningsdragning och "
       "anslutning till tanken stämmer med varandra.",
     ],
     "aside": None},
    {"id": "tanken",
     "h2": "Sluten tank med larm inne i bostaden",
     "paras": [
       "Den slutna tanken ska enligt kommunen tömmas minst en gång per år av kommunens entreprenör och ha en stor "
       "manlucka på minst 400 millimeter. Den ska också ha ett larm som varnar ungefär två veckor innan tanken är "
       "full, och larmet ska placeras i bostaden. I Haninge och Nynäshamn kan du få tillstånd för en extremt "
       "snålspolande toalett till sluten tank även på öar, men på många öar är tömning möjlig bara två gånger "
       "per år, så tanken behöver dimensioneras med god marginal.",
       "Innan du ansöker om enskilt avlopp ska du begära ett yttrande från slamtömningsentreprenören SRV och "
       "bifoga det i ansökan. Entreprenören ska yttra sig i alla ärenden, både nya anläggningar och ändringar, "
       "och för fastigheter på öar kan särskilda regler gälla för framkomligheten. Arbetet får börja först när "
       "kommunens skriftliga beslut finns, och ett avlopp som installeras utan tillstånd kan ge miljösanktionsavgift.",
       "När anläggningen är klar ska en entreprenörsrapport och fotodokumentation skickas in. Det är "
       "fastighetsägarens ansvar att visa att avloppet byggts enligt tillståndet. Muskö är enligt kommunen ett "
       "prioriterat område för återföring av WC-vatten till jordbruket.",
     ],
     "aside": {"title": "Tanken ska ha", "items": [
       "Manlucka på minst 400 mm",
       "Larm cirka två veckor före full tank",
       "Larmet placerat i bostaden",
       "Tömning minst en gång per år"]}},
    {"id": "arkivet",
     "h2": "Vad finns på tomten i dag?",
     "paras": [
       "Vill du veta vilket avlopp som finns på fastigheten i dag hänvisar kommunen till Haningearkivet, där "
       "handlingarna finns. Alla hus med indraget vatten måste ha ett avlopp med slamavskiljare och en "
       "reningsanläggning, och på Avloppsguiden går det att testa om det egna avloppet är grönt, gult eller rött.",
       "Har huset egen brunn ska brunnsvattnet enligt " + X.format(HAN_RAD, "kommunens råd") + " i första hand gå "
       "till dryck och matlagning. Kommunen föreslår snålspolande kranar och duschmunstycken och en mycket "
       "snålspolande toalett, och för permanentboende en extra snålspolande toalett. Regnvatten från taket kan "
       "samlas i en tank och enligt kommunen användas till bland annat tvätt och toalettspolning.",
       "Ska regnvatten samlas från taket hänger det ihop med rännor och stuprör, se "
       + L.format("takrenovering-haninge.html", "takrenovering i Haninge") + ". Görs köket om samtidigt finns mer under "
       + L.format("koksrenovering-haninge.html", "köksrenovering i Haninge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Badrummet i Haninge steg för steg",
  "steps": [
    ("Besök och avloppsläge", "Vi ser badrummet och tar reda på om huset har kommunalt avlopp, tank eller annan anläggning."),
    ("Toalett och tank", "Vid eget avlopp väljer vi toalettyp efter kommunens krav och hur huset används."),
    ("Kostnadsförslag", "Rivning, tätskikt, VVS, el och ytskikt står var för sig."),
    ("Yttrande och beslut", "Krävs tillstånd väntar arbetet på SRV:s yttrande och kommunens beslut."),
    ("Bygge", "Golvbrunn, fall, tätskikt och ledningar mot tanken eller det kommunala nätet."),
    ("Genomgång", "Vi går igenom rummet, larmet och skötseln med dig."),
  ],
  "rot_h2": "Rotavdrag för badrummet i Haninge",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag. Material, till exempel toalett och tank, räknas inte.",
    "För ett småhus godkänner Skatteverket att dra in och reparera vatten- och avloppsledningar och att anlägga "
    "avlopp, inklusive markarbeten som infiltrationsbäddar. Slamsugning och tömning av septiktankar ger däremot "
    "inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Haninge?",
  "price": [
    "Om huset har kommunalt avlopp eller ska ha sluten tank, vilken toalettyp som krävs, hur långt ledningarna "
    "ska dras och om fastigheten ligger på en ö. Därtill kommer storlek och ytskikt. Besöket är gratis, och du "
    "får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste en ny toalett i Haninge vara extremt snålspolande om huset har eget avlopp?",
     "Ja. Installerar du en ny vattentoalett kräver kommunen en toalett som spolar mindre än en liter i genomsnitt, "
     "och för ett nytt avlopp med WC är bara vakuum- eller urinsorterande toalett tillåten."),
    ("Varför avråder Haninge kommun från urinsorterande toalett för permanentboende?",
     "Kommunen anger att den ger fler tömningar och kräver annorlunda användning och rengöring. För "
     "permanentboende rekommenderas i stället vakuumtoalett."),
    ("Var ska larmet för den slutna tanken sitta?",
     "I bostaden. Tanken ska ha ett larm som varnar ungefär två veckor innan den är full, och en manlucka på minst 400 millimeter."),
    ("Hur tar vi reda på vilket avlopp som finns på vår fastighet i Haninge?",
     "Kommunen hänvisar till Haningearkivet, där handlingarna finns. Vid besöket tittar vi också på brunnar och "
     "ledningar som syns på tomten."),
    ("Behöver slamtömningsentreprenören tillfrågas innan vi söker tillstånd för nytt avlopp?",
     "Ja. I Haninge ska du först begära ett yttrande från SRV och bifoga det i ansökan, oavsett om det gäller en "
     "ny anläggning eller en ändring."),
  ],
  "sources": [
    ("Haninge kommun – Olika typer av avlopp", HAN_TYPER),
    ("Haninge kommun – Nytt avlopp eller ändring av befintligt avlopp", HAN_NYTT),
    ("Haninge kommun – Råd, tips och risker (enskilt vatten)", HAN_RAD),
    ("Haninge kommun – Enskilt vatten och avlopp", HAN_BASE),
    ("Haninge kommun, VA-rådgivningen – Godkända avloppslösningar (presentation 2020)", HAN_GODK),
    S_ROTJOB, S_ROT,
  ],
  "cta": ("Ska badrummet i Haninge göras om?", "Boka ett gratis besök, så går vi igenom badrummet och avloppet på plats."),
  "img": [
    ("Kompakt badrum med vägghängd toalett i ett hus i Haninges skärgård",
     "compact newly renovated bathroom in a Swedish archipelago summer house converted for year-round living, white "
     "wall-hung toilet, small white washbasin, light grey floor tiles, white painted tongue-and-groove wood panel on "
     "the upper walls, small window with pine trees and calm water outside, clean and empty"),
    ("Badrum med badkar, handdukstork och mörk kakelvägg",
     "small falu red wooden Swedish cottage with white trim on a rocky island in the Stockholm archipelago, a simple "
     "wooden jetty, pine trees on granite, calm water, summer afternoon"),
  ],
  "related": [],
},

# =============================== BADRUM VALLENTUNA ===============================
"badrumsrenovering-vallentuna.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Vallentuna", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Vallentuna – nytt våtrum och VA-anmälan",
  "description": "Badrumsrenovering i Vallentuna: anmälan för nytt våtrum, Roslagsvattens syn, enskilt avlopp "
                 "och egen brunn på landsbygden och ROT direkt på fakturan.",
  "h1": "Badrumsrenovering i Vallentuna",
  "lead": "I Vallentuna kan ett nytt badrum betyda en ny dusch i en villa i tätorten eller ett första riktigt "
          "våtrum i ett hus på landsbygden med egen brunn och eget avlopp. Geal Entreprenad AB river, bygger "
          "tätskikt och ytskikt och samordnar VVS och el, och vi reder ut vad kommunen och Roslagsvatten behöver "
          "ha in innan arbetet börjar.",
  "card": "Nytt våtrum, Roslagsvatten och egen brunn.",
  "sections": [
    {"id": "anmalan", "anchor": "Anmälan för nytt våtrum",
     "h2": "Ett nytt våtrum i ett befintligt hus kräver anmälan",
     "paras": [
       "Vallentuna kommun skriver på sidan om att " + X.format(VAL_ANSL, "ansluta till kommunalt VA") + " att ny "
       "installation eller väsentlig förändring av vatten och avlopp kräver anmälan hos byggnadsnämnden. Du ska ha "
       "fått startbesked innan arbetet börjar, och startbeskedet gäller inte bara ledningarna utan också de "
       "grävarbeten som behövs.",
       "Anmälan ska innehålla en VA-situationsplan där grävarbetet och de planerade ledningarna och brunnarna "
       "ritas in från förbindelsepunkten fram till byggnaden, eventuellt en planritning som redovisar ett "
       "nytillkommet våtrum eller kök i en befintlig byggnad, och en kontrollplan. Görs installationen utan "
       "startbesked är nämnden enligt lag skyldig att öppna ett tillsynsärende med sikte på sanktionsavgift.",
       "Efter startbeskedet ska en anmälan också göras till Roslagsvatten innan inkoppling eller utbyggnad av "
       "förbindelsepunkten kan börja. Roslagsvatten synar fastighetens VA-installation, medger anslutning, "
       "installerar vattenmätare och driftsätter anläggningen. Därefter ansöker fastighetsägaren om slutbesked "
       "och bifogar den intygade kontrollplanen.",
     ],
     "aside": {"title": "Ordningen i Vallentuna", "items": [
       "Anmälan till bygglovsenheten",
       "Startbesked före grävning",
       "Anmälan till Roslagsvatten",
       "Syn, vattenmätare och slutbesked"]}},
    {"id": "vattnet",
     "h2": "Var vattnet kommer ifrån och vart det tar vägen",
     "paras": [
       "Roslagsvatten AB ansvarar för Vallentunas vatten och avlopp. Dricksvattnet kommer från Görvälnverket i "
       "Mälaren, som drivs av kommunalförbundet Norrvatten, och avloppsvattnet renas i Käppala reningsverk på "
       "Lidingö. Karby och Brottby är anslutna till Margretelunds reningsverk i Österåker, och Ekskogen och "
       "Kårsta har egna mindre reningsverk. Vissa delar av kommunen är inte anslutna alls, och där har hushållen "
       "egen brunn och enskilt avlopp.",
       "Ventilationen har egna regler. Vill du göra en " + X.format(VAL_VENT, "väsentlig ändring av ventilationen") +
       " kan det krävas anmälan, och kommunen påpekar att ändringar ibland påverkar brandskyddet så mycket att "
       "anmälan krävs även av det skälet. Till en anmälan hör situationsplan i skala 1:500, planritningar i "
       "skala 1:100, teknisk beskrivning och kontrollplan.",
     ],
     "aside": None},
    {"id": "enskilt",
     "h2": "Ungefär 2 800 enskilda avlopp i kommunen",
     "paras": [
       "I Vallentuna finns ungefär 2 800 enskilda avloppsanläggningar, och ett standardhushåll använder enligt "
       + X.format(VAL_ENSK, "kommunen") + " cirka 800–1 000 liter vatten om dagen som måste tas omhand. Ska en ny "
       "anläggning byggas eller en befintlig ändras krävs ansökan om tillstånd eller anmälan till Bygg- och "
       "miljötillsynsnämnden, och den som bygger utan riskerar miljösanktionsavgift.",
       "En komplett ansökan består av blankett, situationsplan och sektionsritning. På situationsplanen ska "
       "bland annat de hus som ska kopplas på, platsen för slamtömningsbilen, den egna och grannarnas "
       "dricksvattentäkt med avstånd i meter och eventuella borrhål för bergvärme finnas med. Är ansökan komplett "
       "får du enligt kommunen svar inom sex veckor, men kompletteringar och grannyttranden kan behövas.",
       "Kommunen har " + X.format(VAL_TILLS, "tillsyn över enskilda avlopp") + " med fokus på cirka 200 "
       "fastigheter om året och ett intervall på tio år, och WC-avlopp prioriteras. Äldre anläggningar kräver "
       "ofta åtgärder för att klara dagens reningskrav. Har huset ett minireningsverk kan tillståndet innehålla "
       "villkor om service och provtagning, och tillståndsbeslutet kan miljöavdelningen hjälpa till att hitta.",
     ],
     "aside": {"title": "Före ett badrum med eget avlopp", "items": [
       "Finns tillståndsbeslutet kvar?",
       "Tål anläggningen fler duschar?",
       "Villkor om service och provtagning?",
       "Sex veckor för en komplett ansökan"]}},
    {"id": "brunn",
     "h2": "Egen brunn: prova vattnet innan rummet byggs",
     "paras": [
       "För dig med " + X.format(VAL_BRUNN, "egen brunn") + " rekommenderar miljöavdelningen mikrobiologisk och "
       "kemisk analys, radon om brunnen är borrad och gärna tungmetaller som bly, arsenik och uran. Resultaten har "
       "enligt kommunen betydelse för om desinfektion eller filter behöver installeras. Ska ett filter monteras är "
       "det bra att veta det innan våtrum och tvättstuga byggs, så att det finns plats och åtkomst.",
       "De senaste årens torka har enligt kommunen gett många brunnsägare vattenbrist och ibland sämre "
       "vattenkvalitet, och kommunen uppmanar därför till registrering i SGU:s brunnsarkiv. En grävd brunn har "
       "enligt kommunen ofta lägre kapacitet och är känsligare för föroreningar från omgivningen.",
       "Om husens tak och fasader i kommunen finns mer under " + L.format("takrenovering-vallentuna.html", "takrenovering i Vallentuna")
       + " och " + L.format("malare-vallentuna.html", "målare i Vallentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går vi till väga i Vallentuna",
  "steps": [
    ("Besök", "Vi ser rummet och tar reda på om huset har kommunalt VA eller egen brunn och eget avlopp."),
    ("Anmälan eller tillstånd", "Behövs anmälan till bygglovsenheten eller tillstånd för avloppet tar vi fram underlag."),
    ("Kostnadsförslag", "Arbete och material står på egna rader, så att ROT-avdraget går att räkna ut."),
    ("Rivning", "Ytskikt, gamla skivor och brunn tas bort, och underlaget bedöms med rummet öppet."),
    ("Rör, tätskikt och syn", "Installatörerna drar rör och el, tätskiktet läggs och Roslagsvatten synar vid nyanslutning."),
    ("Klart rum", "Kakel, klinker och porslin monteras, och kontrollplanen intygas inför slutbesked."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Vallentuna",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr ihop med "
    "rutavdrag. Material och resor räknas inte.",
    "Skatteverket godkänner radonsanering i samband med byggarbete på ett småhus, men inte att mäta radon eller "
    "fukt. Vid borrning av en ny brunn räknas arbetskostnaden med en schablon på 35 procent av totalkostnaden, "
    "och maskiner som borraggregat ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset i Vallentuna?",
  "price": [
    "Om badrummet ligger kvar eller blir ett nytt våtrum, om huset ska anslutas eller har eget avlopp, hur "
    "ledningarna ska dras och vilka ytskikt du väljer. Vi kommer ut gratis och lämnar ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi anmäla ett nytt badrum i en befintlig byggnad i Vallentuna?",
     "Om det innebär ny installation eller väsentlig förändring av vatten och avlopp krävs anmälan, och kommunen "
     "kan vilja se en planritning över det nya våtrummet. Fråga bygglovsenheten om du är osäker."),
    ("Vem synar VA-installationen innan huset kopplas på i Vallentuna?",
     "Roslagsvatten AB. De synar installationen, medger anslutning och sätter upp vattenmätaren, och sedan "
     "ansöker du om slutbesked hos kommunen."),
    ("Hur lång tid tar ett avloppstillstånd i Vallentuna?",
     "Är ansökan komplett får du svar inom sex veckor, enligt kommunen. Kompletteringar och grannyttranden kan förlänga tiden."),
    ("Vilka prover bör vi ta på brunnsvattnet i Vallentuna innan badrummet byggs om?",
     "Miljöavdelningen rekommenderar mikrobiologisk och kemisk analys, radon om brunnen är borrad och gärna "
     "tungmetaller som bly, arsenik och uran."),
    ("Ger det ROT-avdrag att sanera radon när badrummet renoveras?",
     "Ja, Skatteverket godkänner radonsanering i samband med byggarbete på ett småhus. Själva mätningen ger däremot inget avdrag."),
  ],
  "sources": [
    ("Vallentuna kommun – Anslut kommunalt VA", VAL_ANSL),
    ("Vallentuna kommun – Enskilt avlopp", VAL_ENSK),
    ("Vallentuna kommun – Enskilda avlopp, tillsyn", VAL_TILLS),
    ("Vallentuna kommun – Egen brunn", VAL_BRUNN),
    ("Vallentuna kommun – Dricksvattenkvalitet", VAL_KVAL),
    ("Vallentuna kommun – Ventilation (bygglov och anmälan)", VAL_VENT),
    S_ROTJOB, S_ROT,
  ],
  "cta": ("Ska badrummet i Vallentuna renoveras?", "Boka ett kostnadsfritt besök, så går vi igenom rummet, ledningarna och vattnet."),
  "img": [
    ("Nytt badrum i ett äldre hus på landsbygden i Vallentuna",
     "newly renovated bathroom in an old Swedish countryside house, light grey floor tiles, white wall tiles, white "
     "painted wooden ceiling, walk-in shower with glass screen, window looking out over open fields and a falu red barn "
     "in the distance, clean and empty"),
    ("Våtrum under uppbyggnad med nya rör och golvbrunn",
     "Swedish house wet room under construction, bare concrete floor sloping to a new round floor drain, new white "
     "plastic water pipes and grey drain pipe stubs coming out of the wall and floor, wet-room boards on the walls, "
     "a spirit level leaning on the wall, daylight from a small window"),
  ],
  "related": [],
},

# =============================== BADRUM ÖSTERÅKER ===============================
"badrumsrenovering-osteraker.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Österåker", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Österåker – VA-utbyggnad och öarna",
  "description": "Badrumsrenovering i Österåker: badrum när kommunen bygger ut VA, eget avlopp på Ljusterö, "
                 "vattensmarta val, brunnsprov och ROT direkt på fakturan.",
  "h1": "Badrumsrenovering i Österåker",
  "lead": "I Österåker blir fritidshus helårsbostäder samtidigt som kommunen bygger ut vatten och avlopp i "
          "etapper, och badrummet hamnar ofta mitt i den förändringen. Geal Entreprenad AB river, bygger "
          "tätskikt och ytskikt och samordnar VVS och el, och vi börjar med att ta reda på om huset har kommunalt "
          "VA, eget avlopp eller är på väg att anslutas.",
  "card": "VA-utbyggnad, öar och vattensmarta val.",
  "sections": [
    {"id": "utbyggnad", "anchor": "VA-utbyggnaden",
     "h2": "Vattentjänstplanen och områdena som står på tur",
     "paras": [
       "Den 10 mars 2025 antog kommunfullmäktige Österåkers första vattentjänstplan. Den ska läsas som ett "
       "komplement till VA-planen och är inte juridiskt bindande, utan ett vägledande verktyg. "
       + X.format(OST_VTP, "Planen") + " räknar upp kommunens utmaningar: stark befolkningstillväxt, högt "
       "bebyggelsetryck, förekomst av tungmetaller, permanentning av fritidshus, stor säsongsvariation i "
       "befolkningen och att en stor del av kommunen är skärgård.",
       "Utbyggnaden koncentreras de närmaste åren till de västra delarna, med programområdena Åkers Runö och "
       "Täljö–Gottsunda och utvecklingen av Åkersberga centrum. Området kring Täljö, Alsro och Gottsunda omfattar "
       "både nybyggnadsområden och förnyelseområden. I Östanå ska ett nytt reningsverk med större kapacitet än det "
       "i Roslags-Kulla göra fortsatt utbyggnad möjlig, till exempel inom detaljplanen för Wira utby.",
       "På sydvästra Ljusterö är delar av Linanäs–Laggarsvik anslutna till allmänt vatten och spillvatten, men "
       "stora delar har enskilda anläggningar och en blandning av permanentbostäder och fritidshus. Där har "
       "tidplanen för VA-utbyggnaden förskjutits och beskrivs som osäker. För badrummet betyder det att samma "
       "fråga får olika svar i olika delar av kommunen: bygga för det avlopp som finns nu, eller för det som kommer.",
     ],
     "aside": {"title": "Utbyggnad enligt planen", "items": [
       "Åkers Runö och Täljö–Gottsunda",
       "Kanalstaden",
       "Nytt reningsverk i Östanå",
       "Linanäs–Laggarsvik: osäker tidplan"]}},
    {"id": "eget-avlopp",
     "h2": "Eget avlopp på fastlandet och på öarna",
     "paras": [
       "En fastighet med indraget vatten ska ha en fungerande och godkänd avloppsanläggning, skriver kommunen på "
       + X.format(OST_AVL, "sidan om avlopp") + ", oavsett om det är permanentboende eller fritidsboende. Ska ett "
       "nytt avlopp anläggas eller ett befintligt ändras krävs anmälan eller tillstånd från Miljö- och "
       "hälsoskyddsnämnden. Anslutning av en ny byggnad är ett exempel på anmälan, och den anmälan som ska göras "
       "enligt plan- och bygglagen ingår i samma blankett.",
       "För att slamtömningen ska fungera får avståndet till farbar väg, eller till båtens angörningsplats, vara "
       "högst tio meter. Annars behöver fastighetsägaren anlägga en sugledning. Högre krav på rening gäller i "
       "tätbebyggda områden med många brunnar, nära utpekade sjöar, inom 100 meter från stränder och i skyddade "
       "naturområden. Berörda grannar ska få möjlighet att yttra sig innan ansökan skickas in.",
       "Kommunen påpekar också att den kan lämna bygglov först när det är klarlagt hur vatten och avlopp kan "
       "ordnas. Ska huset byggas till för att få plats med ett nytt badrum är avloppet alltså en del av lovfrågan.",
     ],
     "aside": {"title": "Inför en avloppsansökan", "items": [
       "Situationsplan och provgrop",
       "Dricksvattenbrunnar i närheten",
       "Högst tio meter för slamtömning",
       "Grannyttrande"]}},
    {"id": "vattensmart",
     "h2": "Vattensmarta val i badrummet",
     "paras": [
       "Delar av Österåker får sitt dricksvatten från Mälaren via Norrvatten och Roslagsvatten, men kommunen "
       "påpekar på " + X.format(OST_VA, "sidan om vatten och avlopp") + " att vattenverket har begränsad kapacitet, "
       "och att den som har egen brunn kan få problem när grundvattennivåerna sjunker. Var och en av oss använder "
       "i snitt 140 liter vatten om dagen, och bara cirka tio liter av dem går till mat och dryck. Resten går "
       "till dusch, toalett, tvätt och disk.",
       "Kommunens råd blir därför konkreta för den som bygger badrum. Med ett snålspolande duschmunstycke kan "
       "vattenmängden halveras, ett badkar rymmer 200 liter och en droppande kran kan förbruka cirka 1 500 liter "
       "vatten per år. Har du en brunn kan en dusch med vattensnålt munstycke vara ett bättre val än ett badkar.",
       "Pool och badtunna är ett eget kapitel. Det är inte tillåtet att fylla dem med grundvatten från egen borrad "
       "brunn eller en gemensam brunn, eftersom så stora uttag riskerar sinande brunnar eller högre salthalter. "
       "Kommunalt vatten, till exempel via tankbil, går däremot bra.",
     ],
     "aside": None},
    {"id": "prover",
     "h2": "Brunnsprovet som underlag",
     "paras": [
       "Den som har egen brunn ansvarar själv för att kontrollera vattenkvaliteten. Kommunen hänvisar till "
       "Livsmedelsverkets rekommendation om prov minst vart tredje år och skriver att en normal analys passar för "
       "de flesta brunnar, med radon som tillägg för en borrad brunn. Provkit kan hämtas i Åkersberga och på "
       "Ljusterö, och svaret kommer normalt inom 14 dagar.",
       "Om " + X.format(OST_PROV, "resultatet visar problem") + " påpekar kommunen att det vid mikrobiologiska "
       "problem ibland är bättre att åtgärda orsaken än att installera ett filter, till exempel otätheter som "
       "släpper in ytvatten i brunnen. Vatten med PFAS över riktvärdet går enligt kommunen bra att använda för "
       "dusch och tvätt.",
       "Om taken på husen i kommunen finns mer under " + L.format("taklaggare-osteraker.html", "takläggare i Österåker") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en badrumsrenovering till i Österåker",
  "steps": [
    ("Besök", "Vi ser badrummet och tar reda på om huset har kommunalt VA, eget avlopp eller väntar på anslutning."),
    ("Avlopp och vatten", "Vi går igenom avloppets tillstånd, avståndet för slamtömning och eventuella brunnsprov."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där rivning, installationer och ytskikt står var för sig."),
    ("Anmälan vid behov", "Ska en ny byggnad kopplas på eller avloppet ändras lämnas underlag in innan arbetet börjar."),
    ("Bygge", "Golvbrunn, fall, tätskikt och vattensnåla armaturer; installatörerna drar rör och el."),
    ("Genomgång", "Vi går igenom rummet med dig och lämnar egenkontroll och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Österåker",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans "
    "med rutavdrag. Material och resor räknas inte.",
    "För ett småhus räknar Skatteverket att göra förbättringsarbeten i våtrum, till exempel byta plastmatta eller "
    "våtrumstapet mot kakel, och att dra in vatten- och avloppsledningar som rotarbete. Ett fritidshus räknas som "
    "småhus om du använder det som bostad. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Österåker?",
  "price": [
    "Om huset har kommunalt VA, eget avlopp eller ska anslutas, hur ledningarna dras, om fastigheten ligger på en "
    "ö och vilka ytskikt och armaturer du väljer. Besöket är gratis, och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Ska vi vänta med badrummet tills vårt område i Österåker får kommunalt VA?",
     "Det beror på tidplanen. Vattentjänstplanen visar i vilken ordning kommunen planerar att bygga ut, och för "
     "vissa områden beskrivs tidplanen som osäker. Det kan vi gå igenom vid besöket."),
    ("Hur nära vägen måste slamavskiljaren ligga på Ljusterö?",
     "Högst tio meter från farbar väg eller från båtens angörningsplats, annars behöver du anlägga en sugledning, enligt kommunen."),
    ("Får vi fylla badtunnan med vatten från vår borrade brunn i Österåker?",
     "Nej. Kommunen tillåter inte det, eftersom stora uttag kan få brunnar att sina eller ge högre salthalter. "
     "Kommunalt vatten, till exempel via tankbil, går bra."),
    ("Kan vi duscha i brunnsvatten med PFAS över riktvärdet?",
     "Enligt Österåkers kommun går vatten med halter över riktvärdet bra att använda för dusch och tvätt. "
     "Kontakta miljö- och hälsoskyddsavdelningen om du är osäker."),
    ("Behövs en separat bygganmälan när gästhuset ansluts till vårt avlopp?",
     "Anslutning av en ny byggnad anmäls till Miljö- och hälsoskyddsnämnden, och den anmälan som krävs enligt "
     "plan- och bygglagen ingår i samma blankett."),
  ],
  "sources": [
    ("Österåkers kommun – Vattentjänstplan för Österåkers kommun (2025, pdf)", OST_VTP),
    ("Österåkers kommun – Avlopp", OST_AVL),
    ("Österåkers kommun – Vatten och avlopp", OST_VA),
    ("Österåkers kommun – Dricksvatten", OST_DV),
    ("Österåkers kommun – Provtagning av vatten från egen brunn", OST_PROV),
    S_ROTJOB, S_ROT,
  ],
  "cta": ("Ska badrummet i Österåker göras om?", "Boka ett gratis besök, så går vi igenom rummet, avloppet och vattnet."),
  "img": [
    ("Badrum med dusch i stället för badkar i en villa i Österåker",
     "newly renovated bathroom in a Swedish 1970s villa, walk-in shower with a frameless glass wall and a simple "
     "shower head, no bathtub, white matte wall tiles, dark grey floor tiles, white washbasin on a light oak vanity, "
     "frosted window with soft daylight, clean and empty"),
    ("Trähus vid vattnet på Ljusterö",
     "Swedish wooden house painted pale yellow with white corners on a gentle slope down to a calm bay, gravel road in "
     "front, pine and birch trees, a small wooden boat jetty, Roslagen archipelago island, early summer daylight"),
  ],
  "related": [],
},

# =============================== BADRUM BOTKYRKA ===============================
"badrumsrenovering-botkyrka.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Botkyrka", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Botkyrka – flytta badrummet rätt",
  "description": "Badrumsrenovering i Botkyrka: när flytt av badrum kräver anmälan, stammar och frånluft, "
                 "anslutning till kommunalt VA, bygglovsarkivet och ROT på fakturan.",
  "h1": "Badrumsrenovering i Botkyrka",
  "lead": "Ett badrum i Botkyrka kan ligga i en villa i Tullinge, ett radhus i Tumba eller en bostadsrätt i "
          "Hallunda, och reglerna skiljer sig mer mellan husen än man tror. Geal Entreprenad AB river, bygger "
          "tätskikt och ytskikt och samordnar VVS och el, och vi går igenom vad kommunen kräver innan ett badrum "
          "flyttas eller byggs om.",
  "card": "Flytt av badrum, stammar och frånluft.",
  "sections": [
    {"id": "flytt", "anchor": "Flytta badrummet",
     "h2": "Att flytta badrummet kräver inget lov, men ibland anmälan",
     "paras": [
       "Botkyrka kommun skriver på sidan om " + X.format(BOT_FLYTT, "flytt av kök eller badrum") + " att en flytt "
       "inte är bygglovspliktig och ofta inte heller anmälningspliktig. Kommunen listar sedan när anmälan krävs. "
       "Det gäller håltagning i bjälklag om den berör bärande delar, ändring av bärande vägg, väsentlig ändring "
       "av ventilationen och väsentlig ändring av vatten- och avloppsinstallationerna. Är du osäker på om en "
       "håltagning påverkar bärande konstruktion bör en konstruktör bedöma det.",
       "Kommunen ger exempel på gränsdragningen. En ny VA-stam i ett nytt schakt är en väsentlig ändring, medan en "
       "ny stam i befintligt schakt med samma placering inte är anmälningspliktig. Rördragning inom en lägenhet "
       "till befintlig stam är normalt inte anmälningspliktig, inte heller mindre håltagningar i en brandcellsgräns "
       "som tätas direkt i rätt brandteknisk klass.",
       "I fastigheter med skyddsbestämmelse i detaljplanen eller med områdesbestämmelser gäller en utökad "
       "anmälningsplikt och eventuellt bygglovsplikt. Kommunen påpekar att delar av informationen på webbplatsen "
       "kan vara inaktuell sedan de nya bygglovsreglerna började gälla den 1 december 2025, så stäm av med "
       "kommunen innan arbetet planeras i detalj.",
     ],
     "aside": {"title": "Anmälan krävs vid", "items": [
       "Håltagning som berör bärande bjälklag",
       "Ny VA-stam i nytt schakt",
       "Nytt aggregat, fläkt eller nya kanaler",
       "Skyddsbestämmelse i detaljplanen"]}},
    {"id": "luft",
     "h2": "Frånluften och fukten i rummet",
     "paras": [
       "För ventilationen räknar kommunen installation eller byte av aggregat, fläkt, ventilationskanaler eller "
       "värmeväxlare som påverkar ventilationsflöden eller luftkvalitet som en väsentlig ändring. Att använda en "
       "befintlig frånluftskanal i ett badrum räknas däremot inte som väsentlig ändring och behöver inte anmälas. "
       "Flyttas badrummet bort från den gamla kanalen blir frågan därför större.",
       "På kommunens " + X.format(BOT_LUFT, "sida om luft, ventilation och temperatur") + " anges en rekommenderad "
       "relativ luftfuktighet inomhus på 30–70 procent, och kommunen skriver att för hög luftfuktighet kan orsaka "
       "fuktproblem och kvalster. Fukt tillförs bland annat från tvätt och från människorna i huset. Ett badrum "
       "där duschen används varje dag behöver en frånluft som klarar att föra bort fukten.",
       "I ett hus eller radhus där golvbrunnen är från före 1990 ska den enligt GVK:s "
       + X.format(S_GVK[1], "branschregler") + " bytas vid renovering. När brunnen byts byggs golvet om runt den, och "
       "då görs fallet om samtidigt.",
     ],
     "aside": None},
    {"id": "ansluta",
     "h2": "Från egen anläggning till kommunalt VA",
     "paras": [
       "Ska huset anslutas till kommunalt vatten och avlopp beskriver " + X.format(BOT_ANSL, "kommunen") + " stegen. "
       "Nybyggnadskartan visar förbindelsepunkten, där fastighetens ledningar ansluter till det allmänna nätet. "
       "När du vill att den fysiska förbindelsepunkten ska upprättas skickar du in en servisanmälan, och därefter "
       "tar det upp till åtta veckor. Du behöver också redovisa hur dagvattnet ska tas om hand, med en kort "
       "redogörelse och en geologisk undersökning.",
       "Förbindelsepunkten ligger 0,5 meter utanför tomtgränsen. Därifrån och in i huset ansvarar du för arbetet. "
       "När det är klart begär du uppsättning av vattenmätare, och kommunens VA-enhet monterar mätaren när "
       "konsolen är på plats. Anslutningsavgiften ska vara betald innan anslutningen får användas.",
       "Ett badrum som görs om samtidigt kan få nya ledningar fram till den nya anslutningen i stället för att de "
       "gamla förlängs, och mätarkonsolen kan placeras där den är lätt att nå.",
     ],
     "aside": {"title": "Anslutning i Botkyrka", "items": [
       "Nybyggnadskarta med förbindelsepunkt",
       "Servisanmälan, upp till åtta veckor",
       "Redovisning av dagvatten",
       "Konsol på plats, sedan vattenmätare"]}},
    {"id": "arkiv",
     "h2": "Ritningarna i bygglovsarkivet",
     "paras": [
       "Innan ett badrum flyttas är det bra att veta hur bjälklag och väggar är byggda. I " + X.format(BOT_ARK, "Botkyrkas bygglovsarkiv")
       + " kan du se och hämta handlingar, till exempel ritningar, från avslutade bygglovsärenden. Du når arkivet "
       "via en e-tjänst och behöver fastighetens adress eller fastighetsbeteckning. Pågående ärenden syns inte.",
       "Kommunens utvecklingsprogram " + X.format(BOT_TULL, "Framtid för Tullinge") + " från 2010 beskriver "
       "förändringstrycket i Tullinge som högt och konstaterar att det byggs många bostäder i stadsdelen, mest "
       "spridda enskilda småhus. Ett nyare småhus och ett äldre hus kan alltså stå på samma gata, och därför "
       "börjar vi med ritningarna.",
       "Om taken i kommunen finns mer under " + L.format("taklaggare-botkyrka.html", "takläggare i Botkyrka") +
       ", och om grunderna för tätskikt och fall under " + L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Badrummet i Botkyrka steg för steg",
  "steps": [
    ("Platsbesök", "Vi tittar på rummet, golvbrunnen, frånluften och var stammen går."),
    ("Ritningar och anmälan", "Ritningar hämtas ur arkivet, och krävs anmälan tar vi fram underlaget."),
    ("Skriftligt förslag", "Rivning, underlag, tätskikt, rör, el och ytskikt står som egna poster."),
    ("Rivning", "Golv och väggar öppnas, och bjälklag, brunn och rör bedöms innan något byggs."),
    ("Uppbyggnad", "Ny golvbrunn, fall och tätskikt; installatörerna drar rör, el och frånluft."),
    ("Klart rum", "Klinker, kakel och porslin på plats; du får egenkontroll och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag i villa, radhus och bostadsrätt",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr ihop med "
    "rutavdrag. Material och resor räknas inte.",
    "I en bostadsrätt godkänner Skatteverket bland annat att byta golvbrunn, dra vatten- och avloppsledningar och "
    "sätta kakel och klinker. Stambyte, att flytta eller byta ut avloppsrör och att flytta golvbrunnen ger däremot "
    "inget avdrag. I villa och radhus räknas även att dra in och reparera vatten- och avloppsledningar. Geal drar "
    "avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset i Botkyrka?",
  "price": [
    "Om badrummet ligger kvar eller flyttas, om bjälklag, stam eller ventilation berörs, om golvbrunnen behöver "
    "bytas och vilka ytskikt du väljer. Besöket är gratis, och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste vi anmäla det om vi flyttar badrummet till andra sidan huset i Tullinge?",
     "Inte i sig. Botkyrka kommun kräver anmälan om flytten innebär håltagning som berör bärande bjälklag, ändring "
     "av bärande vägg, ny VA-stam i nytt schakt eller väsentlig ändring av ventilationen."),
    ("Får vi använda den gamla frånluftskanalen till det renoverade badrummet?",
     "Ja. Att använda en befintlig frånluftskanal i ett badrum räknas enligt kommunen inte som en väsentlig "
     "ändring och behöver inte anmälas."),
    ("Hur lång tid tar det att få en förbindelsepunkt för kommunalt VA i Botkyrka?",
     "Upp till åtta veckor från att servisanmälan registrerats, enligt kommunen. Därefter ansvarar du för arbetet "
     "från förbindelsepunkten in i huset."),
    ("Var hittar vi ritningar över vårt radhus i Tumba innan badrummet görs om?",
     "I Botkyrkas bygglovsarkiv, som nås via en e-tjänst. Du behöver adressen eller fastighetsbeteckningen, och "
     "bara avslutade ärenden syns."),
    ("Ger det ROT att flytta golvbrunnen i en bostadsrätt i Botkyrka?",
     "Nej. För bostadsrätt godkänner Skatteverket byte av golvbrunn men inte att flytta den, och inte heller stambyte."),
  ],
  "sources": [
    ("Botkyrka kommun – Flytt av kök eller badrum", BOT_FLYTT),
    ("Botkyrka kommun – Anslut till kommunalt vatten och avlopp", BOT_ANSL),
    ("Botkyrka kommun – Bygglovsarkiv", BOT_ARK),
    ("Botkyrka kommun – Luft, ventilation och temperatur", BOT_LUFT),
    ("Botkyrka kommun – Framtid för Tullinge, utvecklingsprogram (pdf)", BOT_TULL),
    S_GVK, S_ROTJOB, S_ROT,
  ],
  "cta": ("Ska badrummet i Botkyrka göras om?", "Boka ett gratis besök, så går vi igenom rummet, stammen och ventilationen."),
  "img": [
    ("Renoverat badrum i ett radhus i Botkyrka",
     "renovated bathroom in a Swedish 1970s terraced house, large light grey wall tiles, dark anthracite floor tiles, "
     "wall-hung toilet, white washbasin on a wooden vanity, shower corner with glass wall, white round exhaust air valve "
     "in the ceiling, soft daylight, clean and empty"),
    ("Renoverat badrum med kommod, badkar och vägghängd toalett",
     "small Swedish terraced house bathroom completely stripped for renovation, no fixtures and no bathtub, bare grey "
     "concrete walls and floor, a round white exhaust air valve fitted in the bare ceiling, a hole in the floor where the "
     "old floor drain was removed, grey drain pipe stub, stacked white wet-room boards leaning against the wall, small "
     "window with daylight"),
  ],
  "related": [],
},

}
