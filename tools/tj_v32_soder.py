# -*- coding: utf-8 -*-
"""Ortsidor v32 (2026-10-28): fasadmålning Sundbyberg; fasadrenovering Botkyrka och Skärholmen; golvläggare,
byggföretag och totalrenovering Skärholmen; totalrenovering Kista. Tre bilder per sida: img[0] hero 4:3,
img[1] och img[2] 3:2.

Lokal vinkel per sida:
fasadmalning-sundbyberg – centrala Sundbyberg norr om järnvägen: slätputs i ljusa ockra- och terranyanser, 1940-tal
  längs Vegagatan, Prästgårdsgatan och Fågelsången, torgets stenhuskvarter (antikvarisk utredning 2016);
  kulör- och materialbeskrivning, frivilligt bygglov och utökad lovplikt (Sundbybergs bygglovsguide).
fasadrenovering-botkyrka – Tuna: radhusen söder om Lindhovsvägen i tegel och trä, riktlinjen om ursprungliga dörrar
  och fönster, lamellhusens tegelgavlar och putsade långsidor; Fittja (ca 2 500 bostäder, 1970-talets början);
  kommunens definition av fasadändring; tilläggsisolering (Boverket); eternit (Arbetsmiljöverket).
fasadrenovering-skarholmen – småhusen i fyra delar (områdesfakta 2025); materialblandning och enhetlighet i
  husgrupperna (Varsam); asbestcement i tak och väggar; tilläggsisolering och proportioner; lov för en- och
  tvåbostadshus och Bredäng.
golvlaggare-skarholmen – plastmattor, golvplattor, fix och fog som kan innehålla asbest i hus byggda före 1982,
  tillstånd för rivning (Arbetsmiljöverket); lamellparkett, linoleum och PVC (Golvbranschen); hyresrätt.
byggforetag-skarholmen – radhusägaren som byggherre (Boverket), miljöinventering före rivning (Arbetsmiljöverket),
  container och bod på gatan (Stockholms stad), lov i husgrupperna.
totalrenovering-skarholmen – 1960-talets småhus: frånluftsventilation 1961–1975, asbest 1940–1970, hyresrätt och
  bostadsrätt i flerbostadshusen, Bredäng och fasaden.
totalrenovering-kista – hus från 1975–1980: från- och tilluft från 1976, asbest i hus byggda till 1982, styrelsens
  tillstånd, planlösning och anmälan.

Fakta endast från källorna i respektive 'sources', öppnade med Python/urllib (Mozilla-UA) 2026-10-28, alla svarade
200; pdf:erna har textlager. Skatteverket återställde anslutningen – samma URL och formuleringar som v22–v31.
Strukna: avgifter, handläggningstider, namn på enskilda fastigheter, påståenden om material i enskilda husgrupper.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_SB = "https://bygglov.stockholm/nar-behovs-bygglov/"
_STH_FASAD = ("Stockholms stad – Fasadändring", _SB + "andra-byggnads-yttre-utseende/fasadandring/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
              _SB + "andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_STH_PLAN = ("Stockholms stad – Ändra planlösningen i en byggnad", _SB + "andra-inomhus/andra-planlosningen-i-en-byggnad/")
_STH_BAR = ("Stockholms stad – Ändra i bärande konstruktion", _SB + "andra-inomhus/andra-i-barande-konstruktion/")
_STH_VENT = ("Stockholms stad – Ventilation", _SB + "andra-inomhus/ventilation/")
_STH_TBF = ("Stockholms stad – Tillbyggnad (bygglovsbefriad)", _SB + "bygga-nytt-och-bygga-till/tillbyggnad-bygglovsbefriad/")
_STH_PLATS = ("Stockholms stad – Använda offentlig plats för byggverksamhet",
              "https://tillstand.stockholm/tillstand-regler-och-tillsyn/anvanda-offentlig-plats/anvanda-offentlig-plats-for-byggverksamhet/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_KISTA_SPAR = ("Stockholms stadsmuseum – Stockholms spår: Kista (pdf)",
               "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000080.pdf")
_BOV_ROLL = ("Boverket – Roller i byggskedet",
             "https://www.boverket.se/sv/energiguiden/energieffektivisera-flerbostadshus/energirenovera/bygga/roller-i-byggskedet/")
_BOV_ASB = ("Boverket – Risker med hantering av asbest i byggnader",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_BOV_ISO = ("Boverket – Energiguiden: Tilläggsisolera fasaden",
            "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/tillaggsisolera-fasaden/")
_AV_HAR = ("Arbetsmiljöverket – Här finns asbest", "https://www.av.se/produktion-industri-och-logistik/asbest/har-finns-asbest/")
_AV_FOR = ("Arbetsmiljöverket – Förebygg riskerna med asbest",
           "https://www.av.se/halsa-och-sakerhet/kemiska-risker/risker-for-vissa-amnen-produkter-och-verksamheter/asbest/forebygg-riskerna-med-asbest/")
_GB_LAM = ("Golvbranschen – Lamellparkett", "https://www.golvbranschen.se/teknik--material/tragolv/lamellparkett/")
_GB_LIN = ("Golvbranschen – Linoleumgolv", "https://www.golvbranschen.se/teknik--material/linoleumgolv/")
_GB_PVC = ("Golvbranschen – Plastgolv, PVC", "https://www.golvbranschen.se/teknik--material/plastgolv/plastgolv---pvc/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SBG_FASAD = ("Sundbybergs stad – Fasadändring",
              "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/fasadandring")
_SBG_UTR = ("Sundbybergs stad – Antikvarisk utredning för Sundbybergs bebyggelse (pdf)",
            "https://www.sundbyberg.se/download/18.2e6195c8190a64a78d4166d1/1722330773238/Antikvarisk%20utredning%20f%C3%B6r%20Sundbybergs%20bebyggelse.pdf")
_BOT_FASAD = ("Botkyrka kommun – Fasadändring",
              "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/fasadandring")
_BOT_KMP = ("Botkyrka kommun – Kulturmiljöprogram (pdf)",
            "https://www.botkyrka.se/download/18.1fbbaae6170bff9469deb7f/1602575505534/Kulturmilj%C3%B6program.pdf")

_SKH = [_of("Skärholmens stadsdelsområde", "soderort/skarholmen/skarholmen-stadsdelsomrade")]
_SKH4 = [_of("Skärholmen", "soderort/skarholmen/skarholmen"), _of("Bredäng", "soderort/skarholmen/bredang"),
         _of("Sätra", "soderort/skarholmen/satra"), _of("Vårberg", "soderort/skarholmen/varberg")]

PAGES_TJ = {

# ------------------------------------------------------------------ FASADMÅLNING SUNDBYBERG
"fasadmalning-sundbyberg.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Sundbyberg", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Sundbyberg – ockra, terra och ljus puts",
  "description": "Fasadmålning i Sundbyberg: stadskärnans ljusa putsfasader, kulör- och materialbeskrivning till bygglovet, frivilligt lov och när lovplikten är utökad.",
  "h1": "Fasadmålning i Sundbyberg",
  "lead": "Centrala Sundbyberg är en stad av putsade flerbostadshus i ljusa kulörer, och kommunens kulturmiljöutredning vill att nya hus anpassas till dem. Geal Entreprenad AB målar fasader på flerbostadshus och villor och tar fram kulörförslag och handlingar när bygglov behövs.",
  "card": "Puts och kulör i stadskärnan.",
  "sections": [
    {"id": "stadskarnan-sbg", "anchor": "Stadskärnan",
     "h2": "Ljusa ockra- och terranyanser norr om järnvägen",
     "paras": [
       "Den antikvariska utredningen för Sundbybergs bebyggelse, gjord av Stockholms läns museum 2016, beskriver stadskärnan norr om järnvägen som en kombination av slutna kvarter och friliggande lamellhus. Bebyggelsen hålls ihop av närliggande hushöjder, fasadmaterial och färgsättningar, och återkommande är slätputsade fasader i ljusa färgnyanser, ibland tegel, och fyra–fem våningar.",
       "I riktlinjerna står att tillkommande hus ska anpassas till angränsande bebyggelse i arkitektur, material och färgsättning, och att det kännetecknande är putsarkitektur, ofta färgsatt i ljusa ockra- och terranyanser. Det säger också något om vad en ny kulör på ett befintligt hus bör förhålla sig till.",
     ],
     "aside": {"title": "Stadskärnan norr om järnvägen", "items": [
       "Slätputs i ljusa nyanser", "Ockra och terra", "Ibland tegel", "Fyra–fem våningar"]}},
    {"id": "1940-sbg", "h2": "1940-talets öppna kvarter och torget",
     "paras": [
       "Utredningen pekar ut sammanhållen 1940-talsbebyggelse i öppna kvarter längs Vegagatan, Prästgårdsgatan, Fågelsången och delar av Järnvägsgatan. Norr om Tulegatan finns ett punkthusområde från 1940-talet anlagt enligt principen hus i park. Söder om järnvägen flankeras Sundbybergs torg av ett stenhuskvarter där byggnader från olika tider samspelar i höjd och genom putsade fasader i olika kulörer.",
       "När ett av husen i en sådan grupp målas om är grannhusens kulörer en del av underlaget. Vi tar fram ett kulörförslag som visar huset tillsammans med sina grannar innan föreningen bestämmer sig.",
     ],
     "aside": None},
    {"id": "lov-sbg", "h2": "När Sundbyberg kräver bygglov",
     "paras": [
       "Sundbybergs stad skriver att byte av kulör räknas som fasadändring. För flerbostadshus och andra byggnader som inte är en- eller tvåbostadshus krävs bygglov när ändringen görs på en fasad som vetter mot allmän plats. För en- och tvåbostadshus krävs inte längre bygglov, förutsatt att huset inte är kulturhistoriskt värdefullt eller ligger i ett särskilt värdefullt område som Duvbo.",
       "I Duvbo och för kulturhistoriskt värdefulla byggnader är lovplikten utökad, och där krävs det för det mesta bygglov för fasadändringar. Även när lov inte krävs kan man söka ett frivilligt bygglov för att få beslut på att åtgärden följer lagen. Enligt staden kostar det lika mycket som ett vanligt bygglov.",
     ],
     "aside": {"title": "Bygglov krävs för ny kulör", "items": [
       "Flerbostadshus mot allmän plats", "Kulturhistoriskt värdefulla hus", "Hus i Duvbo", "Annars frivilligt lov"]}},
    {"id": "handlingar-sbg", "h2": "Kulör- och materialbeskrivning till ansökan",
     "paras": [
       "Bland de handlingar staden oftast kräver för ett bygglov för fasadändring finns en situationsplan, plan- och fasadritning, en kulör- och materialbeskrivning och en kontrollplan. Ritningarna ska vara fackmannamässigt utförda och skalenliga, och ansökan görs i kommunens e-tjänst.",
       "Vi tar fram kulör- och materialbeskrivningen med kulörkoder och färgtyp för fasad, listverk och fönsteromfattningar. Är huset en villa ger målningen rotavdrag på arbetskostnaden, och för föreningshus ställs kostnadsförslaget till föreningen.",
     ],
     "aside": None},
    {"id": "hallonbergen", "h2": "Hallonbergen och Rissne",
     "paras": [
       "Den antikvariska utredningen beskriver Hallonbergen som ett enhetligt, storskaligt bostadsområde från rekordåren. Stadsplanen antogs 1968 och området stod klart 1973. Fasaderna är komponerade av ljus kalksandsten omväxlande med gjutna betongelement, och förnyelsen på 1990-talet gav en del hus nya exteriörer med påbyggda sadeltak och utstickande balkonger.",
       "Rissne fick sin stadsplan 1980, och 1982 flyttade de första hyresgästerna in. Fasader av kalksandsten och betong är inte självklart något som ska målas, så vi bedömer varje hus för sig innan vi föreslår målning.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Sundbyberg till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på puts, färg och grannhusen."),
    ("Lovfrågan", "Fasad mot gata, värdefulla hus och Duvbo."),
    ("Kulörförslag", "Kulör- och materialbeskrivning för huset."),
    ("Ansökan", "Ritningar och handlingar när bygglov krävs."),
    ("Förarbete", "Rengöring, lagning och grundning."),
    ("Målning", "Fasad, listverk och detaljer."),
  ],
  "rot_h2": "Rotavdrag för fasadmålning i Sundbyberg",
  "rot": [
    "Målning av fasaden på ett småhus som du äger och bor i ger rotavdrag på arbetskostnaden, högst 30 procent och högst 50 000 kronor per person och år. Material och resor ger inget avdrag, och Geal drar avdraget direkt på fakturan.",
    "I en bostadsrätt ges rotavdrag bara för arbete inne i bostaden. Fasaden är en gemensam del, så målningen av ett föreningshus betalas av föreningen utan avdrag.",
  ],
  "price_h2": "Vad påverkar priset på en fasadmålning i Sundbyberg?",
  "price": [
    "Fasadernas yta och höjd, putsens skick, antalet detaljer och kulörer, ställning och om bygglov med kulör- och materialbeskrivning behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka kulörer är typiska för putshusen i centrala Sundbyberg?",
     "Kommunens antikvariska utredning beskriver putsarkitektur, ofta färgsatt i ljusa ockra- och terranyanser, men även tegel."),
    ("Behöver vår förening i Sundbyberg bygglov för att byta kulör mot gatan?",
     "Ja. För flerbostadshus krävs bygglov när kulören ändras på en fasad som vetter mot allmän plats."),
    ("Kan vi söka bygglov för fasaden i Sundbyberg fast det inte krävs?",
     "Ja, ett så kallat frivilligt bygglov ger beslut på att åtgärden följer lagen. Sundbyberg tar samma avgift som för ett vanligt lov."),
    ("Vilka handlingar behövs för bygglov för fasadändring i Sundbyberg?",
     "Oftast situationsplan, plan- och fasadritning, kulör- och materialbeskrivning och kontrollplan."),
  ],
  "sources": [_SBG_UTR, _SBG_FASAD, _SKV],
  "cta": ("Ska fasaden målas i Sundbyberg?", "Boka ett gratis platsbesök, så tar vi fram kulörförslag och går igenom lovet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust ockragula putshus i ett öppet kvarter",
     "1940s Swedish four storey apartment building with smooth pale ochre render and simple windows in an open block with lawns and birch trees, summer daylight" + _SFX),
    ("Nymålad puts i ljus ockra vid ett fönster",
     "close view of a freshly painted smooth rendered wall in pale ochre next to a white window frame on an apartment building, soft daylight" + _SFX),
    ("Putsade stenhus i olika kulörer vid ett torg",
     "a row of old plastered apartment buildings in different pale colours around a small town square in a Stockholm suburb, cobblestones, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ FASADRENOVERING BOTKYRKA
"fasadrenovering-botkyrka.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Botkyrka", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Botkyrka – tegel och trä i Tuna och Fittja",
  "description": "Fasadrenovering i Botkyrka: radhusen i Tuna i tegel och trä, Fittjas 1970-talshus, kommunens regler för fasadändring, tilläggsisolering och eternit.",
  "h1": "Fasadrenovering i Botkyrka",
  "lead": "Botkyrkas kulturmiljöprogram lyfter fram flera bostadsområden från 1950- till 1970-talen där fasaderna är en stor del av värdet. Geal Entreprenad AB renoverar fasader på villor, radhus och flerbostadshus och tar reda på vad kommunen kräver innan materialet byts.",
  "card": "Tegel, trä och puts från efterkrigstiden.",
  "sections": [
    {"id": "tuna", "anchor": "Tuna",
     "h2": "Radhusen i Tuna – tegel och trä",
     "paras": [
       "Kulturmiljöprogrammet beskriver Tuna som ett område med det tidiga 1960-talets bebyggelse av hög kvalitet, planerat under sent 1950-tal och utbyggt under början av 1960-talet. Bland småhusen utmärker sig radhusområdet söder om Lindhovsvägen, som präglas av kombinationen av tegel och trä i fasaderna och ett enkelt, sakligt formspråk.",
       "Programmets riktlinje är att radhusbebyggelsens tidstypiska karaktär värnas, att ursprungliga dörrar och fönster bibehålls och att det enkla formspråket respekteras. För en fasadrenovering betyder det att träpartierna byts eller lagas i samma indelning och att tegelpartierna behålls.",
     ],
     "aside": {"title": "Tuna enligt programmet", "items": [
       "Planerat sent 1950-tal", "Byggt tidigt 1960-tal", "Radhus i tegel och trä", "Ursprungliga dörrar och fönster"]}},
    {"id": "lamellhus-tuna", "h2": "Tegelgavlar, puts och kopparplåt",
     "paras": [
       "I samma område står lamellhus i tre våningar kring fyra innergårdar, och programmet nämner kombinationen av tegelgavlar och putsade långsidor som ett medvetet drag. Punkthusen i kvarteret Kaplanen började byggas 1958 och avslutas med ett band av kopparplåt, och de har ljusputsade fasader.",
       "I Fittja byggdes enligt programmet omkring 2 500 bostäder i början av 1970-talet, med hög- och låghus, radhus och villor. Prefabricerade betongelement med frilagd ballast och tydliga balkongenheter präglar fasaderna, och de målade balkongfronterna ger färg mot ett annars lågmält uttryck. Riktlinjen är att den repetitiva estetiken i material, volymer och detaljer värnas.",
     ],
     "aside": None},
    {"id": "lov-botkyrka", "h2": "Vad kommunen räknar som fasadändring",
     "paras": [
       "Botkyrka kommun skriver att en fasadändring är en ändring som innebär att byggnaden byter kulör, fasadbeklädnad eller taktäckningsmaterial, eller att dess yttre karaktärsdrag påverkas på annat sätt, till exempel genom nya fönster och dörrar. Att byta från tegel till puts är ett exempel kommunen själv ger.",
       "Inom detaljplan krävs bygglov när ändringen görs på en annan byggnad än ett en- eller tvåbostadshus och på en fasad mot allmän plats. Är byggnaden eller området särskilt värdefullt, eller finns skyddsbestämmelser, krävs bygglov även för fasadändringar som annars är lovfria. Vilka områden det gäller visar kommunens webbkarta.",
     ],
     "aside": {"title": "Fasadändring är", "items": [
       "Ny kulör", "Ny fasadbeklädnad", "Nytt taktäckningsmaterial", "Nya fönster och dörrar"]}},
    {"id": "isolering-botkyrka", "h2": "Tilläggsisolering och gammal eternit",
     "paras": [
       "Boverket skriver att utvändig tilläggsisolering ofta är bäst ur energi- och fuktsynpunkt, men att den ur kulturmiljösynpunkt ofta är problematisk. Fönster och dörrar kan hamna längre in i fasaden, takfoten skjuter inte ut lika mycket och fasaden kan hänga ut över sockeln, så att huset får ett överjäst uttryck.",
       "Arbetsmiljöverket skriver att man ska räkna med att det finns asbest i hus byggda fram till 1982, bland annat i asbestcementskivor, eternit, på tak och väggar. Innan gamla skivor rivs ska materialen undersökas, och för att riva asbesthaltigt material krävs tillstånd. Vi tar in en provtagning innan rivningen planeras.",
     ],
     "aside": None},
    {"id": "missgrepp-botkyrka", "h2": "När ett hus redan är ombyggt",
     "paras": [
       "Boverket skriver att en utvändig tilläggsisolering ibland kan vara oproblematisk om utförandet anpassas till husets utseende, och att det för ett hus som redan är kraftigt ombyggt kan vara ett sätt att rätta till missgrepp och ge huset en utformning som bättre passar dess ålder.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi en fasad i Botkyrka",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på material och skador."),
    ("Program och karta", "Kulturmiljöprogram, detaljplan och webbkarta."),
    ("Provtagning", "Asbest i gamla skivor och fogar undersöks."),
    ("Lov", "Bygglov där material eller kulör ändras och kräver det."),
    ("Renovering", "Byte av panel, lagning av tegel och puts."),
    ("Avslut", "Målning, plåt och slutkontroll."),
  ],
  "rot_h2": "ROT-avdrag för fasadrenovering i Botkyrka",
  "rot": [
    "Äger du ett småhus ger fasadrenovering rotavdrag på arbetskostnaden när du bor i huset eller har det som fritidshus. Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor ger inget avdrag.",
    "I en bostadsrätt är fasaden föreningens, och arbetet ger inget avdrag för bostadsrättshavaren. Där avdraget gäller drar Geal det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på en fasadrenovering i Botkyrka?",
  "price": [
    "Fasadytan och materialet, hur mycket panel eller puts som behöver bytas, om asbest måste saneras, tilläggsisolering och om bygglov krävs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag byta fönstren i mitt radhus i Tuna?",
     "Kulturmiljöprogrammets riktlinje är att ursprungliga dörrar och fönster bibehålls i radhusen. Kontrollera detaljplanen och kommunens karta innan du planerar ett byte."),
    ("Krävs bygglov för att byta fasadmaterial på ett flerbostadshus i Botkyrka?",
     "Ja, inom detaljplan om fasaden vetter mot allmän plats. I särskilt värdefulla miljöer krävs bygglov även i andra fall."),
    ("Kan det finnas asbest i fasadskivorna på mitt hus från 1960-talet?",
     "Ja. Arbetsmiljöverket skriver att man ska räkna med asbest i hus byggda fram till 1982, bland annat i eternitskivor på tak och väggar."),
    ("Varför kan tilläggsisolering förstöra husets utseende?",
     "Boverket skriver att fönster kan hamna längre in, takfoten skjuta ut mindre och fasaden hänga ut över sockeln."),
  ],
  "sources": [_BOT_KMP, _BOT_FASAD, _BOV_ISO, _AV_HAR, _AV_FOR, _SKV],
  "cta": ("Behöver fasaden renoveras i Botkyrka?", "Boka ett gratis platsbesök, så tittar vi på material och lov innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus från 1960-talet med tegel och trä",
     "early 1960s Swedish terraced houses with alternating red brick and dark wooden panel sections, simple flat facades, small front gardens, daylight" + _SFX),
    ("Ny träpanel monteras bredvid tegel",
     "close view of new vertical wooden panel boards installed next to an old red brick wall section on a terraced house, fresh timber, overcast daylight" + _SFX),
    ("Lamellhus med tegelgavel och putsad långsida",
     "three storey 1960s apartment building with a red brick gable end and a light rendered long side, courtyard with trees, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ FASADRENOVERING SKÄRHOLMEN
"fasadrenovering-skarholmen.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Skärholmen", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Skärholmen – tegel, trä och skivor",
  "description": "Fasadrenovering i Skärholmen: småhusen i Bredäng, Sätra, Skärholmen och Vårberg, blandade material, asbest i skivor, tilläggsisolering och lov.",
  "h1": "Fasadrenovering i Skärholmen",
  "lead": "Nästan 2 000 småhus i Skärholmens stadsdelsområde är radhus, kedjehus och villor från miljonprogrammets tid, ofta med tegel, trä och skivor på samma hus. Geal Entreprenad AB renoverar fasader på sådana hus och undersöker de gamla materialen innan något rivs.",
  "card": "Fasader på radhus och kedjehus.",
  "sections": [
    {"id": "smahus-skh", "anchor": "Småhusen",
     "h2": "Småhus i fyra delar",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 1 976 småhus med äganderätt i Skärholmens stadsdelsområde. De fördelar sig på Vårberg med 577, Skärholmen med 543, Sätra med 536 och Bredäng med 320. Lägenheterna i flerbostadshusen är däremot till största delen hyresrätter.",
       "Stadens vägledning Varsam utveckling av småhus- och villaområden räknar alla fyra till de storskaliga stadsdelarna. Bredäng började byggas 1962 som den första stadsdelen som planerades i stor skala, och Sätra följde. Bredäng är i vägledningens tabell markerad som kulturhistoriskt värdefull miljö.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Vårberg 577", "Skärholmen 543", "Sätra 536", "Bredäng 320"]}},
    {"id": "material-skh", "h2": "Olika material, samma husgrupp",
     "paras": [
       "Vägledningen beskriver småhusens utformning som mer varierad än flerbostadshusens, med en blandning av fasadmaterial som tegel, trä och skivor, men med en mycket stor enhetlighet inom varje husgrupp. Färgsättningen var noga komponerad och kunde variera mellan kvarter.",
       "En fasadrenovering på ett radhus blir därför en fråga om hela längan. Byts träpanelen på ett hus till en annan profil eller ett annat material syns det mot grannarna. Vi föreslår material som följer husgruppen och tar upp frågan med grannar eller samfällighet när det behövs.",
     ],
     "aside": None},
    {"id": "asbest-skh", "h2": "Skivor och fogar från 1960-talet",
     "paras": [
       "Boverket skriver att det främst är byggnader från åren 1940–1970 som innehåller asbest, och Arbetsmiljöverket att man ska räkna med asbest i hus byggda fram till 1982. Exempel är asbestcementskivor, eternit, för tak och väggar och tillsatser i murbruk, fix och fog.",
       "Så länge asbesten är inkapslad är den ingen fara, men bearbetas den så att det dammar blir den det. Enligt Arbetsmiljöverket ska materialen därför undersökas innan rivning och renovering, och det krävs tillstånd för att riva asbesthaltigt material. Vi provtar skivor och fogar innan vi planerar rivningen.",
     ],
     "aside": {"title": "Kan innehålla asbest", "items": [
       "Eternitskivor på väggar", "Eternit på tak", "Fix och fog", "Murbruk"]}},
    {"id": "isolering-skh", "h2": "Tilläggsisolering och lov",
     "paras": [
       "Boverket skriver att utvändig tilläggsisolering ofta är bäst ur fuktsynpunkt men kan ändra husets utseende: fönster hamnar längre in, takfoten skjuter ut mindre och fasaden kan hänga ut över sockeln. På hus med låga, svagt lutande tak, som vägledningen beskriver, blir takfoten särskilt känslig.",
       "Stockholms stad skriver att fasadändringar på en- och tvåbostadshus inte längre kräver bygglov om vissa förutsättningar är uppfyllda. Det gäller inte där utökad lovplikt finns, till exempel i områden som pekats ut som särskilt kulturhistoriskt värdefulla. Om fastigheten berörs visar Stadsmuseets klassificeringskarta.",
     ],
     "aside": None},
    {"id": "bilfritt-skh", "h2": "Bilfritt mellan husen",
     "paras": [
       "Vägledningen beskriver hur de storskaliga stadsdelarna byggdes med trafikseparering: matargator runt stadsdelarna, parkering vid bostadskvarteren och bilfria bostadsmiljöer som binds ihop av gång- och cykelvägar. Småhusområdena anlades med samma slags trafiksystem.",
       "För en fasadrenovering betyder det att ställning, material och rivningsmassor ofta bärs eller körs med små maskiner från parkeringen till huset. Vi planerar upplaget tillsammans med grannarna eller samfälligheten så att gångvägarna går att använda under arbetet.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi en fasad i Skärholmen",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på material och husgruppen."),
    ("Provtagning", "Skivor, fogar och fix undersöks för asbest."),
    ("Karta", "Klassning och om lov krävs."),
    ("Förslag", "Material och kulör som följer längan."),
    ("Renovering", "Rivning, eventuell isolering och ny fasad."),
    ("Avslut", "Plåt, foder och slutkontroll."),
  ],
  "rot_h2": "ROT-avdrag för fasadrenovering i Skärholmen",
  "rot": [
    "Äger du ett småhus ger fasadrenovering rotavdrag på arbetskostnaden. Avdraget är högst 30 procent och högst 50 000 kronor per person och år, och material och resor ger inget avdrag.",
    "Bor du i en bostadsrätt är fasaden föreningens, och då ger arbetet inget avdrag för dig. Där avdraget gäller drar Geal det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på en fasadrenovering i Skärholmen?",
  "price": [
    "Fasadens yta och material, om asbest måste saneras, om huset tilläggsisoleras, anslutningar mot grannhusen och om lov krävs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan fasadskivorna på mitt radhus i Skärholmen innehålla asbest?",
     "Ja, om huset är byggt före 1982. Arbetsmiljöverket nämner asbestcementskivor på tak och väggar och skriver att material ska undersökas före rivning."),
    ("Hur många småhus finns det i Skärholmens stadsdelsområde?",
     "Stadens områdesfakta räknar 1 976 småhus med äganderätt 2025, flest i Vårberg."),
    ("Behöver jag bygglov för att byta panel på mitt radhus i Bredäng?",
     "Om fastigheten omfattas av utökad lovplikt krävs bygglov. Stadsmuseets klassificeringskarta visar om den gör det."),
    ("Varför ska mitt radhus se ut som grannarnas?",
     "Stadens vägledning beskriver en mycket stor enhetlighet inom husgrupperna som ett karaktärsdrag i stadsdelen."),
    ("Hur kommer material och ställning fram till radhuset i Skärholmen?",
     "Småhusområdena byggdes med parkering vid kvarteren och bilfria gångvägar. Material bärs eller körs ofta från parkeringen, och upplaget planeras med grannarna."),
  ],
  "sources": _SKH + _SKH4 + [_VARSAM, _BOV_ASB, _AV_HAR, _AV_FOR, _BOV_ISO, _STH_FASAD, _STH_KLASS, _SKV],
  "cta": ("Ska fasaden renoveras i Skärholmen?", "Boka ett gratis platsbesök, så undersöker vi materialen och går igenom lovet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Kedjehus från 1960-talet med tegel och träpanel",
     "row of 1960s Swedish linked houses with mixed yellow brick and stained wooden panel facades, low pitched roofs, footpath and lawns, daylight" + _SFX),
    ("Grå fasad och gammalt tak på ett äldre radhus",
     "close view of old grey fibre cement facade sheets on the gable of a 1960s terraced house, slightly weathered, daylight" + _SFX),
    ("Takfot och fönster på ett radhus under renovering",
     "renovation of a terraced house facade: old panel removed around a window, insulation boards and battens visible, low roof eaves above, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ GOLVLÄGGARE SKÄRHOLMEN
"golvlaggare-skarholmen.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Skärholmen", "svc_label": "Golvläggare",
  "title": "Golvläggare i Skärholmen – gamla mattor och nya golv",
  "description": "Golvläggare i Skärholmen: plastmattor och golvplattor som kan innehålla asbest, lamellparkett, linoleum och PVC i radhus och lägenheter.",
  "h1": "Golvläggare i Skärholmen",
  "lead": "Många golv i Skärholmen, Bredäng, Sätra och Vårberg ligger kvar sedan husen byggdes på 1960- och 70-talen. Innan en gammal plastmatta rivs behöver man veta vad den innehåller. Geal Entreprenad AB lägger nya golv i radhus och lägenheter och undersöker de gamla först.",
  "card": "Nya golv i radhus och lägenheter.",
  "sections": [
    {"id": "hus-skh-golv", "anchor": "Husen",
     "h2": "Radhus och hyreslägenheter",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 1 976 småhus med äganderätt i Skärholmens stadsdelsområde. I flerbostadshusen finns omkring 3 500 lägenheter hos allmännyttan, 6 500 hos privata hyresvärdar och 3 300 bostadsrätter. Stadens vägledning Varsam beskriver stadsdelarna som storskaliga, byggda från 1962 och framåt.",
       "Den som hyr kan enligt Stockholms stad normalt inte göra ändringar som påverkar husets tekniska egenskaper, och i en bostadsrätt behövs föreningens tillstånd för sådana. Ett golvbyte är oftast enklare, men i radhusen är det också där de äldsta golven brukar ligga kvar.",
     ],
     "aside": {"title": "Skärholmen 2025", "items": [
       "1 976 småhus med äganderätt", "3 479 lägenheter hos allmännyttan", "6 502 hos privata hyresvärdar", "3 315 bostadsrätter"]}},
    {"id": "asbest-golv", "h2": "Plastmattan och limmet under",
     "paras": [
       "Arbetsmiljöverket skriver att man ska räkna med att det finns asbest i hus byggda fram till 1982. Bland exemplen nämns golvmaterial av plast, vissa golvplattor och plastmattor, och tillsatser i fix och fog. Asbest i bunden form dammar normalt inte så länge man inte rör materialet, men när en matta rivs eller slipas bort gör man just det.",
       "Byggherren ska enligt Arbetsmiljöverket se till att materialen undersöks innan rivning och renovering, och för att riva asbesthaltigt material krävs tillstånd och särskild utbildning. Vi tar prov på mattor, plattor och lim innan vi river, och lägger hellre det nya golvet på ett säkert underlag än river i blindo.",
     ],
     "aside": {"title": "Kan innehålla asbest", "items": [
       "Golvmaterial av plast", "Vissa golvplattor", "Plastmattor", "Fix och fog"]}},
    {"id": "tra-skh", "h2": "Lamellparkett ovanpå det gamla",
     "paras": [
       "Golvbranschen beskriver lamellparkett som en golvprodukt med två eller flera träbaserade skikt, där toppskiktet är massivt trä på minst 2,5 millimeter. Skikten limmas ihop med fiberriktningen vriden 90 grader mot varandra för att minska golvets fuktrörelser. Ek dominerar som ytskikt.",
       "Ett flytande lamellgolv kan ofta läggas ovanpå ett befintligt golv som får ligga kvar, vilket är en fördel när den gamla mattan inte ska röras. Vi kontrollerar då att underlaget är plant och torrt och att dörrar och trösklar går att anpassa.",
     ],
     "aside": None},
    {"id": "matta-skh", "h2": "Linoleum eller ny plastmatta",
     "paras": [
       "Linoleum tillverkas enligt Golvbranschen av linolja och andra vegetabiliska oljor med trämjöl och kalkstensmjöl, oftast på en bärare av juteväv, i tjocklekar från 2 till 4 millimeter. PVC-golv finns som homogena produkter, med samma sammansättning genom hela mattan, och heterogena med ett tunnare slitskikt överst.",
       "I hallar och kök i radhusen väljer många en matta igen. Vi lägger linoleum eller PVC, och i våtrum en våtrumsgodkänd matta. Mer om tjänsten finns under " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "yta-skh", "h2": "Ytbehandling och skötsel",
     "paras": [
       "Golvbranschen skriver att lamellparkett huvudsakligen levereras lackerad från fabrik, naturoljad eller UV-oljad, och att ytskiktet kan ha stavar i olika bredd och längd och ibland fasad kant.",
       "PVC-golv har enligt Golvbranschen ofta en ytbehandling av polyuretan som ger beständighet mot fläckar och friktionsmärken och minskar behovet av polish och vax. Vi går igenom skötseln när golvet är lagt.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så lägger vi nytt golv i Skärholmen",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på golvet och underlaget."),
    ("Provtagning", "Gamla mattor, plattor och lim undersöks."),
    ("Val av golv", "Lamellparkett, linoleum eller PVC."),
    ("Underlag", "Avjämning och fuktkontroll vid behov."),
    ("Läggning", "Golv, lister och trösklar."),
    ("Avslut", "Städning och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för golvläggning i Skärholmen",
  "rot": [
    "Äger du ett småhus ger golvbytet rotavdrag på arbetskostnaden när du bor i huset. Avdraget är högst 30 procent och högst 50 000 kronor per person och år, och material och resor ger inget avdrag.",
    "I en bostadsrätt ger golvbyte inne i lägenheten rotavdrag för det du ansvarar för enligt stadgarna. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett nytt golv i Skärholmen?",
  "price": [
    "Golvytan, vad som ligger under, om asbest måste saneras, hur mycket avjämning som behövs och vilket golv du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan den gamla plastmattan i mitt radhus i Skärholmen innehålla asbest?",
     "Ja, om huset är byggt före 1982. Arbetsmiljöverket nämner plastmattor, vissa golvplattor och fix och fog bland materialen."),
    ("Får jag riva en asbesthaltig matta själv?",
     "Arbetsmiljöverket skriver att det krävs tillstånd och särskild utbildning för att riva asbesthaltigt material. Låt prova mattan först."),
    ("Hur tjockt är träskiktet på lamellparkett?",
     "Enligt Golvbranschen är toppskiktet massivt trä på minst 2,5 millimeter."),
    ("Kan nytt golv läggas ovanpå den gamla plastmattan?",
     "Ofta, med ett flytande lamellgolv, om underlaget är plant och torrt. Då behöver den gamla mattan inte rivas."),
    ("Vad är skillnaden mellan en homogen och en heterogen plastmatta?",
     "Enligt Golvbranschen har en homogen matta samma sammansättning genom hela tjockleken, medan en heterogen har bottenskikt och ett tunnare slitskikt överst."),
  ],
  "sources": _SKH + [_VARSAM, _AV_HAR, _AV_FOR, _STH_PLAN, _GB_LAM, _GB_LIN, _GB_PVC, _SKV],
  "cta": ("Vill du byta golv i Skärholmen?", "Boka ett gratis platsbesök, så tittar vi på det gamla golvet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nylagt ljust ekgolv i ett vardagsrum i ett radhus",
     "newly laid light oak engineered parquet floor in an empty living room of a 1960s Swedish terraced house, white walls, large window to a small garden, daylight" + _SFX),
    ("Gammal mönstrad plastmatta i en hall",
     "old patterned vinyl floor covering from the 1960s in an empty hallway of a Swedish house, worn edges near a door threshold, daylight" + _SFX),
    ("Linoleummatta i ett kök",
     "new marbled grey linoleum floor in a simple empty Swedish kitchen with white cabinets, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ BYGGFÖRETAG SKÄRHOLMEN
"byggforetag-skarholmen.html": {
  "kind": "district", "service": "byggforetag", "ort": "Skärholmen", "svc_label": "Byggföretag",
  "title": "Byggföretag i Skärholmen – radhusägaren som byggherre",
  "description": "Byggföretag i Skärholmen: ditt ansvar som byggherre i radhuset, miljöinventering före rivning, container på gatan och lov i husgrupperna.",
  "h1": "Byggföretag i Skärholmen",
  "lead": "Den som äger ett radhus i Skärholmen och bygger om är byggherre, med ett ansvar som finns kvar även när ett byggföretag gör jobbet. Geal Entreprenad AB tar hand om hela ombyggnaden och hjälper dig med det byggherren ska se till.",
  "card": "Hela ombyggnaden av radhuset.",
  "sections": [
    {"id": "agare-skh", "anchor": "Radhusägarna",
     "h2": "Nästan 2 000 radhus, kedjehus och villor",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 1 976 småhus med äganderätt i Skärholmens stadsdelsområde, fördelade på Vårberg, Skärholmen, Sätra och Bredäng. Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver småhusen i de storskaliga stadsdelarna som huvudsakligen radhus och kedjehus, med enstaka villor och atriumhus, till exempel i Sätra.",
       "Äger du huset äger du också ansvaret för det du bygger. Det gäller vare sig du bygger till, gör om planlösningen eller byter fasad.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Vårberg 577", "Skärholmen 543", "Sätra 536", "Bredäng 320"]}},
    {"id": "byggherre-skh", "h2": "Byggherrens ansvar",
     "paras": [
       "Boverket beskriver byggherren som den som för egen räkning utför eller låter utföra byggnads- eller rivningsarbeten, och skriver att byggherren ofta också är fastighetsägaren. Byggherren har det yttersta ansvaret för att byggnaden uppfyller bestämmelserna och att rätt kompetens finns med i projektet.",
       "När en åtgärd kräver lov eller anmälan ska byggherren se till att arbetet inte börjar före startbesked, att det kontrolleras enligt kontrollplanen och att det inte tas i bruk före slutbesked. Kräver det inget lov gäller ändå kraven på bland annat utformning, tekniska egenskaper och varsamhet. Vi tar fram handlingar och kontrollplan och följer upp dem under bygget.",
     ],
     "aside": {"title": "Byggherren ska se till att", "items": [
       "Lov eller anmälan finns", "Inget börjar före startbesked", "Kontrollplanen följs", "Slutbesked finns före inflyttning"]}},
    {"id": "inventering-skh", "h2": "Inventera före rivning",
     "paras": [
       "Arbetsmiljöverket skriver att en miljöinventering av hälsofarliga ämnen ska göras innan arbetet påbörjas, redan i planeringen. Man ska utgå från att byggnader uppförda fram till 1982 kan innehålla asbest, och det är byggherre, projektör och arbetsgivare som ska se till att en undersökning och eventuell provtagning görs.",
       "Husen i Skärholmen byggdes från 1960-talet och framåt, så inventeringen hör till de första stegen. Hittas asbest planeras saneringen av ett företag med tillstånd innan resten av ombyggnaden börjar.",
     ],
     "aside": None},
    {"id": "gatan-skh", "h2": "Container, bod och husgruppen",
     "paras": [
       "Behöver en container, en bod eller ett upplag stå på gata eller annan offentlig plats krävs enligt Stockholms stad polistillstånd, och för container, byggbod och upplag dessutom bygglov. Ett glest byggstängsel kräver inget bygglov.",
       "En tillbyggnad på ett radhus får enligt staden vara högst 30 kvadratmeter utan lov, inte högre än husets nock och 4,5 meter från gränsen om inte grannen medger annat. Vägledningen beskriver en mycket stor enhetlighet inom husgrupperna, och Bredäng är markerat som kulturhistoriskt värdefull miljö. Mer om hur vi arbetar finns under " + _L.format("byggfirma.html", "byggfirma") + ".",
     ],
     "aside": None},
    {"id": "ritningar-skh", "h2": "Ritningar till ditt hus",
     "paras": [
       "Stockholms stad skriver att man kan logga in med bank-id och se ritningarna till sitt hus, men att ritningar kan vara ofullständiga och att det inte är säkert att de som byggt har följt dem. Staden kan inte bedöma om en planerad ändring påverkar den bärande konstruktionen, utan hänvisar till en konstruktör.",
       "Inför en ombyggnad hämtar vi ritningarna, kontrollerar dem mot huset på plats och tar in en konstruktör när en vägg ska bort. Ändringar i bärande konstruktion kräver anmälan och startbesked.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi om ett radhus i Skärholmen",
  "steps": [
    ("Platsbesök", "Gratis besök där vi går igenom huset och dina planer."),
    ("Inventering", "Asbest och andra ämnen undersöks före rivning."),
    ("Handlingar", "Ritningar, lov eller anmälan och kontrollplan."),
    ("Etablering", "Container, bod och tillstånd vid behov."),
    ("Ombyggnad", "Rivning, stomme, installationer och ytskikt."),
    ("Slutbesked", "Kontroller och dokumentation."),
  ],
  "rot_h2": "Rotavdrag när radhuset byggs om i Skärholmen",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år. Material och resor ger inget avdrag, och du ska äga bostaden när arbetet utförs.",
    "Skatteverket ger rotavdrag för om- och tillbyggnad av ett småhus du äger. För arbete som ger avdrag drar Geal det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på en ombyggnad i Skärholmen?",
  "price": [
    "Hur mycket som byggs om, om asbest måste saneras, om bärande väggar berörs, behovet av lov och kontrollplan och vilken standard du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Är jag byggherre när ett byggföretag bygger om mitt radhus i Skärholmen?",
     "Ja, som fastighetsägare som låter utföra arbetet. Boverket skriver att byggherren har det yttersta ansvaret enligt plan- och bygglagen."),
    ("Vem ska se till att huset undersöks för asbest?",
     "Arbetsmiljöverket skriver att byggherre, projektör och arbetsgivare ska se till att en undersökning och eventuell provtagning görs."),
    ("Behöver containern på gatan tillstånd?",
     "Ja. På offentlig plats krävs polistillstånd, och enligt Stockholms stad även bygglov för containern."),
    ("Hur många radhus och villor finns det i Skärholmen?",
     "Stadens områdesfakta räknar 1 976 småhus med äganderätt i stadsdelsområdet 2025."),
    ("Stämmer ritningarna till mitt radhus i Skärholmen med verkligheten?",
     "Inte säkert. Stockholms stad skriver att ritningar kan vara ofullständiga, så vid ändringar i stommen tar vi in en konstruktör."),
  ],
  "sources": _SKH + _SKH4 + [_VARSAM, _BOV_ROLL, _AV_FOR, _STH_PLATS, _STH_TBF, _SKV],
  "cta": ("Ska radhuset byggas om i Skärholmen?", "Boka ett gratis platsbesök, så går vi igenom ansvar, inventering och lov innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhuslänga i Skärholmen med små trädgårdar",
     "row of 1960s Swedish terraced houses with brick and wood facades, low pitched roofs and small front gardens along a footpath, daylight" + _SFX),
    ("Rivning inne i ett radhus med skyddsplast",
     "interior renovation in a terraced house: walls stripped to studs, protective plastic sheeting, a stack of new plasterboard and tools, daylight" + _SFX),
    ("Container framför en radhuslänga",
     "an empty plain grey steel skip container without stickers on a parking area in front of a row of Swedish 1960s terraced houses with brown wooden panel and yellow brick, low roofs without chimneys, overcast day" + _SFX),
  ],
},

# ------------------------------------------------------------------ TOTALRENOVERING SKÄRHOLMEN
"totalrenovering-skarholmen.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Skärholmen", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Skärholmen – 1960-talets radhus",
  "description": "Totalrenovering i Skärholmen: radhus och kedjehus från 1960-talet, frånluftsventilation, asbest, anmälan och vad som gäller i bostadsrätt och hyresrätt.",
  "h1": "Totalrenovering i Skärholmen",
  "lead": "Ett radhus i Bredäng, Sätra, Skärholmen eller Vårberg som totalrenoveras har ofta ventilation, golv och ledningar från byggåret. Geal Entreprenad AB renoverar hela huset eller lägenheten och utgår från vad som byggdes på 1960-talet.",
  "card": "Renovera hela huset eller lägenheten.",
  "sections": [
    {"id": "hus-skh-tot", "anchor": "Husen",
     "h2": "Byggt från 1962",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden berättar att Bredäng började byggas 1962 som den första stadsdelen som planerades i stor skala, följd av Sätra. 1965 intensifierades bostadsbyggandet i hela landet, och en stor andel av miljonprogrammets bebyggelse var gruppbyggda småhus och radhus.",
       "Stadens områdesfakta för 2025 räknar 1 976 småhus med äganderätt i stadsdelsområdet. Vägledningen beskriver att omsorgen om de enskilda bostädernas planlösningar var stor och att goda ljusförhållanden och funktionalitet var ledord, och det är ofta den planlösningen man utgår från vid en totalrenovering.",
     ],
     "aside": {"title": "Skärholmen", "items": [
       "Bredäng från 1962", "Därefter Sätra", "1 976 småhus med äganderätt", "Radhus och kedjehus"]}},
    {"id": "ventilation-skh", "h2": "Frånluft från 1960-talet",
     "paras": [
       "Stockholms stad beskriver frånluftsventilation som vanlig i hus byggda mellan 1961 och 1975. Centrala fläktar drar ut luften via don i kök, badrum och toalett, och tilluften tas in genom uteluftsdon i ytterväggarna och genom otätheter. När nya fönster sätts in och huset blir tätare behöver uteluften fortfarande hitta en väg in.",
       "Installation eller väsentlig ändring av ventilationen kräver anmälan och startbesked, och aggregat som monteras utvändigt kan kräva bygglov. Vi tar reda på vilket system huset har innan kök och badrum ritas.",
     ],
     "aside": None},
    {"id": "asbest-skh-tot", "h2": "Asbest i 1960-talets material",
     "paras": [
       "Boverket skriver att det främst är byggnader från åren 1940–1970 som innehåller asbest, och att det är stor sannolikhet att man stöter på asbest vid renovering, ombyggnad och rivning. Arbetsmiljöverket nämner bland annat eternitskivor, fix och fog, golvmaterial av plast och isolering.",
       "En totalrenovering rör nästan alla de materialen. Därför börjar vi med en inventering och provtagning, och det som innehåller asbest saneras av ett företag med tillstånd innan väggar och golv rivs.",
     ],
     "aside": {"title": "Att undersöka först", "items": [
       "Golvmattor och plattor", "Fix och fog i våtrum", "Eternitskivor", "Isolering"]}},
    {"id": "upplatelse-skh", "h2": "Äganderätt, bostadsrätt eller hyresrätt",
     "paras": [
       "I flerbostadshusen i Skärholmens stadsdelsområde är de flesta lägenheter hyresrätter: omkring 3 500 hos allmännyttan och 6 500 hos privata hyresvärdar, mot 3 300 bostadsrätter. Stockholms stad skriver att du som hyr normalt inte får göra ändringar i bärande konstruktion, brandskydd, ventilation eller vatten och avlopp, och att du i en bostadsrätt behöver föreningens tillstånd.",
       "I ett ägt radhus bestämmer du själv inomhus, men fasaden är en del av husgruppen. Bredäng är i stadens vägledning markerat som kulturhistoriskt värdefull miljö, så ska fönster eller fasad ändras kontrollerar vi klassningen. Mer om tjänsten finns under " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
    {"id": "el-skh", "h2": "Ny el i ett hus från 1960-talet",
     "paras": [
       "Elsäkerhetsverket skriver att förändringar i den fasta elinstallationen, som ett nytt uttag i köket eller ledningar i väggarna, ska göras av ett registrerat elinstallationsföretag. Själv får man bara göra enklare saker, som att byta glödlampor eller en trasig proppsäkring.",
       "Vid en totalrenovering av ett radhus från 1960-talet dras ofta ny el i hela huset. Vi samordnar elinstallatören med rivning och ny planlösning, så att ledningarna dras innan väggarna stängs.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Skärholmen till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi går igenom huset."),
    ("Inventering", "Provtagning av material som kan innehålla asbest."),
    ("Ritningar", "Planlösning, ventilation, el och VVS."),
    ("Anmälan", "Startbesked när stomme eller ventilation ändras."),
    ("Rivning och installationer", "Sanering, rivning och nya ledningar."),
    ("Ytskikt", "Golv, väggar, kök och badrum."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Skärholmen",
  "rot": [
    "I ett småhus räknar Skatteverket bland annat rivning av väggar, ny planlösning, tilläggsisolering och kakel och klinker som rotarbete. Avdraget gäller arbetskostnaden, inte material och resor.",
    "I en bostadsrätt gäller avdraget arbete innanför lägenhetens tak, väggar och golv som du ansvarar för enligt stadgarna. Avdraget är högst 30 procent och högst 50 000 kronor per person och år, och Geal drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på en totalrenovering i Skärholmen?",
  "price": [
    "Hur mycket som rivs, om asbest måste saneras, ventilationens skick, om planlösningen ändras och vilken standard du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken ventilation har ett radhus från 1960-talet i Skärholmen?",
     "Enligt Stockholms stad är frånluftsventilation vanlig i hus byggda 1961–1975. Vi kontrollerar vad ditt hus har."),
    ("Måste jag provta för asbest innan jag totalrenoverar?",
     "Material ska undersökas innan rivning och renovering. Boverket skriver att det främst är hus från 1940–1970 som innehåller asbest."),
    ("Får jag totalrenovera min hyreslägenhet i Bredäng?",
     "Nej, som hyresgäst får du normalt inte ändra bärande delar, ventilation eller vatten och avlopp. Det är hyresvärdens beslut."),
    ("Hur gamla är radhusen i Bredäng och Sätra?",
     "Enligt stadens vägledning började Bredäng byggas 1962 och Sätra därefter, så de äldsta husen är från 1960-talet."),
    ("Får jag dra om elen själv när jag totalrenoverar radhuset?",
     "Nej. Elsäkerhetsverket skriver att förändringar i den fasta elinstallationen ska göras av ett registrerat elinstallationsföretag."),
  ],
  "sources": _SKH + [_VARSAM, _STH_VENT, _STH_PLAN, _BOV_ASB, _AV_HAR, _STH_KLASS, _SKV],
  "cta": ("Planerar du en totalrenovering i Skärholmen?", "Boka ett gratis platsbesök, så går vi igenom huset och materialen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust renoverat vardagsrum i ett radhus från 1960-talet",
     "bright renovated living room in a 1960s Swedish terraced house with white walls, light wooden floor, large window to a small garden, empty room, daylight" + _SFX),
    ("Frånluftsdon i taket i ett badrum",
     "close view of a round white exhaust air valve in the ceiling of a newly tiled small bathroom, soft light" + _SFX),
    ("Provtagning av gammalt golv med skyddad yta",
     "a small square sample cut out of an old patterned vinyl floor covering, the piece lying beside the hole next to a utility knife and a blank transparent plastic bag without print, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ TOTALRENOVERING KISTA
"totalrenovering-kista.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Kista", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Kista – hus från 1975–1980",
  "description": "Totalrenovering i Kista: radhus och lägenheter från 1975–1980, från- och tilluft med värmeåtervinning, asbest före 1982 och styrelsens tillstånd.",
  "h1": "Totalrenovering i Kista",
  "lead": "Husen i Kista byggdes på bara fem år i slutet av 1970-talet, och många har kvar sitt ursprungliga ventilationssystem och sina ursprungliga material. Geal Entreprenad AB totalrenoverar radhus och lägenheter i Kista och utgår från hur husen är byggda.",
  "card": "Renovera hela huset eller lägenheten.",
  "sections": [
    {"id": "kista-hus", "anchor": "Husen",
     "h2": "En stadsdel från 1975–1980",
     "paras": [
       "Stadsmuseets skrift om Kista berättar att staden köpte marken 1966 och att Kista byggdes ut under åren 1975–1980, med friare arkitektoniska former än i de andra stadsdelarna på Järvafältet. Kista centrum invigdes 1977.",
       "Stadens områdesfakta för 2025 räknar i Kista omkring 3 600 bostadsrätter och 1 600 lägenheter hos privata hyresvärdar i flerbostadshus, och bland småhusen 482 med äganderätt och 404 bostadsrätter. En totalrenovering i Kista gäller därför ofta en bostadsrätt, i lägenhet eller radhus.",
     ],
     "aside": {"title": "Kista 2025", "items": [
       "3 565 bostadsrätter i flerbostadshus", "1 625 hos privata hyresvärdar", "482 småhus med äganderätt", "404 småhus som bostadsrätter"]}},
    {"id": "ftx-kista", "h2": "Från- och tilluft i hus från 1976",
     "paras": [
       "Stockholms stad beskriver från- och tilluftsventilation, ofta med värmeåtervinning, som vanlig i hus byggda från 1976 och framåt. Centrala fläktar styr både från- och tilluft, och systemet ställer höga krav på drift, skötsel och regelbundet underhåll. I hus från 1961–1975 är frånluft vanligare.",
       "När väggar flyttas eller kök och badrum byggs om rubbas lätt balansen mellan till- och frånluft. Installation eller väsentlig ändring av ventilationen kräver anmälan och startbesked, och i en bostadsrätt även styrelsens tillstånd. Vi tar reda på vilket system huset har innan vi ritar.",
     ],
     "aside": None},
    {"id": "asbest-kista", "h2": "Byggt före 1982",
     "paras": [
       "Arbetsmiljöverket skriver att man ska utgå från att alla byggnader uppförda fram till 1982 kan innehålla asbest, eftersom asbest användes fram till förbudet det året. Även senare byggnader kan i vissa fall innehålla asbest från lager eller import.",
       "Kista byggdes före förbudet. Innan golv, kakel och väggar rivs ska materialen därför undersökas, och det är enligt Arbetsmiljöverket byggherrens, projektörens och arbetsgivarens ansvar att det görs. Vi tar prov i planeringen så att en eventuell sanering hinns med.",
     ],
     "aside": {"title": "Före rivning", "items": [
       "Miljöinventering", "Provtagning vid osäkerhet", "Sanering med tillstånd", "Därefter rivning"]}},
    {"id": "styrelse-kista", "h2": "Styrelsen och anmälan",
     "paras": [
       "Bostadsrättslagen kräver styrelsens tillstånd för ingrepp i bärande konstruktion, ändringar av ledningar för avlopp, värme, gas och vatten, ventilation, eldstad eller brandskydd och andra väsentliga förändringar. Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet för föreningen.",
       "Stockholms stad skriver att du inte behöver anmäla en ändrad planlösning inom lägenheten om inga tekniska egenskapskrav påverkas, till exempel när köket flyttas. Påverkas bärande konstruktion eller brandskydd krävs anmälan och startbesked. Mer om tjänsten finns under " + _L.format("villarenovering.html", "villarenovering och totalrenovering") + ".",
     ],
     "aside": None},
    {"id": "el-kista", "h2": "Uttag, ledningar och elföretaget",
     "paras": [
       "Enligt Elsäkerhetsverket ska de flesta elinstallationsarbeten utföras av ett registrerat elinstallationsföretag, och vid ändringar i den fasta installationen, till exempel ett uttag i köket eller nya ledningar i väggar, ska ett sådant anlitas. Även byte av ett befintligt vägguttag ska göras av ett elföretag om arbetet inte kan kontrolleras korrekt.",
       "När köket flyttas eller väggar rivs i en lägenhet eller ett radhus i Kista följer elen med. Vi lägger in elinstallatören i tidplanen så att ledningarna dras innan väggar och tak stängs.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Kista till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi går igenom bostaden."),
    ("Inventering", "Provtagning av material före rivning."),
    ("Tillstånd", "Underlag till styrelsen."),
    ("Anmälan", "Startbesked när stomme, brand eller ventilation berörs."),
    ("Rivning och installationer", "El, vatten, avlopp och ventilation."),
    ("Ytskikt", "Golv, väggar, kök och badrum."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Kista",
  "rot": [
    "I en bostadsrätt ger Skatteverket rotavdrag för arbete innanför lägenhetens tak, väggar och golv som du ansvarar för enligt stadgarna. Stambyten och gemensamma delar ger inget avdrag. I ett ägt småhus räknas bland annat rivning av väggar och ny planlösning som rotarbete.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på en totalrenovering i Kista?",
  "price": [
    "Bostadens storlek, om asbest måste saneras, hur ventilationen påverkas, hur mycket av planlösningen som ändras och vilken standard du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken ventilation har en lägenhet i Kista från slutet av 1970-talet?",
     "Enligt Stockholms stad är från- och tilluft, ofta med värmeåtervinning, vanligt i hus byggda från 1976. Vi kontrollerar vad just ert hus har."),
    ("Kan det finnas asbest i ett hus i Kista?",
     "Ja. Arbetsmiljöverket skriver att man ska utgå från att byggnader uppförda fram till 1982 kan innehålla asbest."),
    ("Behöver jag anmäla att jag flyttar köket i min lägenhet i Kista?",
     "Inte om inga tekniska egenskapskrav påverkas. Ändras ventilation, brandskydd eller bärande delar krävs anmälan."),
    ("När invigdes Kista centrum?",
     "Enligt Stadsmuseet invigdes Kista centrum 1977."),
    ("Vem ska se till att materialen provas före rivning i Kista?",
     "Enligt Arbetsmiljöverket är det byggherre, projektör och arbetsgivare som ska se till att en undersökning och eventuell provtagning görs."),
  ],
  "sources": [_of("Kista", "vasterort/jarva/kista"), _KISTA_SPAR, _STH_VENT, _STH_PLAN, _AV_FOR, _BRL, _SKV],
  "cta": ("Planerar du en totalrenovering i Kista?", "Boka ett gratis platsbesök, så går vi igenom ventilation, material och tillstånd innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Renoverat kök och vardagsrum i en lägenhet från 1970-talet",
     "renovated open kitchen and living room in a late 1970s Swedish apartment with white cabinets, light oak floor, large windows, empty room, daylight" + _SFX),
    ("Ventilationsaggregat i ett förråd",
     "a white residential heat recovery ventilation unit with insulated ducts mounted on the wall of a small storage room, clean, soft light" + _SFX),
    ("Rivet badrum med blottade väggar",
     "stripped bathroom during renovation: old tiles removed, bare concrete walls and floor drain, protective plastic at the doorway, daylight" + _SFX),
  ],
},

}
