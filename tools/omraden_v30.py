# -*- coding: utf-8 -*-
"""
Takläggarsidor för innerstaden (v30, 2026-10-27): Kungsholmen, Södermalm, Vasastan och Östermalm.
Samma mönster som omraden_extra.py (LOC/LOC_EXTRA/ORT_SEO/ORT_SRC). Skillnader mot villaorterna:
husen är flerbostadshus som ägs av bostadsrättsföreningar eller hyresvärdar, så beställaren är en styrelse
och rotavdrag gäller inte takarbetet (gemensam yta). Hero-punkterna byts därför (ORT_TRUST_V30) och varje
sida får en tredje bild (ORT_IMG3_V30).

Fakta endast från källorna i ORT_SRC_V30, öppnade med curl (Mozilla-UA) 2026-10-27, alla svarade 200:
  Områdesfakta 2025 (Kungsholmen: tabell för 2024) – bostäder efter hustyp och upplåtelseform.
  Stockholms stad – Riksintressen enligt miljöbalken (pdf, textlager): den klassiska stenstaden 1870–1930 på
    Östermalm, Södermalm, Kungsholmen och Norrmalm; fem våningar vid 18 meter breda gator; sockelvåning och
    huvudfasad med markerad takfot, ibland attikavåning; sluttande tak, oftast plåttäckta, upp till 45 grader;
    vindsinredningar prövas enligt varsamhetskraven; hus från rivnings- och saneringsvågen 1950–1980 kan ändras
    friare; många hus har gul klass, och betydelsen för stadsmiljön är avgörande vid prövningen.
  bygglov.stockholm: Flerbostadshus (mindre takkupor är lovpliktiga fasadändringar, större takkupa är tillbyggnad,
    detaljritning 1:10–1:50, äldre handlingar i Bygg- och plantjänsten), Fasadändring (flerbostadshus: lov när
    ändringen vetter mot allmän plats; kulör eller material på tak), Solenergianläggning (väderradarn i Håtuna,
    vägledningen inte uppdaterad efter 1 december 2025, anmälan bara vid väsentlig påverkan på bärande delar eller
    brandskydd, solkartan), Eldstad och skorsten (anmälan, bygglov för ny utvändig skorsten, samråd med
    skorstensfejarmästaren), Luftvärmepump och ventilationshuv (ett aggregat under 80 x 60 x 30 cm som inte syns
    från gatan; ny huv oftast bygglov), Kulturhistoriskt värdefull byggnad (förvanskningsförbud, utökad lovplikt i
    detaljplan även för underhåll, antikvarisk förundersökning, konsekvensbeskrivning, KUL), Stadsmuseets
    klassificering (blå och grön ring, blå och grön markering, streckade ytor, e-post till Stadsmuseet med adress,
    fastighetsbeteckning, byggår, ombyggnader och foton, svar inom tre veckor), Ändra i bärande konstruktion
    (ritningar kan vara ofullständiga).
  Skatteverket (samma URL och formulering som v27–v29; sidan återställde anslutningen härifrån): arbete på
    gemensamma ytor som tak och fasader ger inget rotavdrag för bostadsrättshavaren.
Inga priser, garantier, omdömen, egna uppdrag i stadsdelarna eller cert. Inget kontor i innerstaden (bas = Bromma).
"""

_L = '<a class="text-link" href="{0}" rel="noopener">{1}</a>'
_S = "https://bygglov.stockholm/nar-behovs-bygglov/"
_OF = ("https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/"
       "statistik/omradesfakta/inre-staden/")
_SFX = ", realistic photo, no people, no hands, no text, no letters"

AREAS_V30 = ["Kungsholmen", "Södermalm", "Vasastan", "Östermalm"]
NEIGHBORS_V30 = {
  "Kungsholmen": ["Vasastan", "Södermalm", "Bromma", "Solna"],
  "Södermalm":   ["Kungsholmen", "Östermalm", "Hägersten", "Enskede"],
  "Vasastan":    ["Kungsholmen", "Östermalm", "Solna", "Sundbyberg"],
  "Östermalm":   ["Vasastan", "Södermalm", "Lidingö", "Danderyd"],
}
NEIGHBORS_ADD_V30 = {
  "Bromma": ["Kungsholmen"],
  "Solna": ["Vasastan", "Kungsholmen"],
  "Lidingö": ["Östermalm"],
  "Hägersten": ["Södermalm"],
}

ORT_TRUST_V30 = {o: ["Gratis besök och kostnadsförslag", "Underlag till föreningens styrelse"] for o in AREAS_V30}

_SOL = ("Stockholms stad – Solceller, solpanel och solfångare", _S + "andra-byggnads-yttre-utseende/solceller-solpanel-solfangare/")
_FASAD = ("Stockholms stad – Fasadändring", _S + "andra-byggnads-yttre-utseende/fasadandring/")
_FLERBO = ("Stockholms stad – Flerbostadshus", _S + "andra-byggnads-yttre-utseende/flerbostadshus/")
_SKORST = ("Stockholms stad – Eldstad, braskamin och skorsten", _S + "andra-byggnads-yttre-utseende/eldstad-braskamin-och-skorsten/")
_HUV = ("Stockholms stad – Luftvärmepump, ventilationsaggregat och ventilationshuv",
        _S + "andra-byggnads-yttre-utseende/luftvarmepump-ventilationsaggregat-och-ventilationshuv/")
_KULT = ("Stockholms stad – Kulturhistorisk värdefull byggnad och område",
         _S + "andra-byggnads-yttre-utseende/kulturhistorisk-vardefull-byggnad-och-omrade/")
_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
          _S + "andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_BAR = ("Stockholms stad – Ändra i bärande konstruktion", _S + "andra-inomhus/andra-i-barande-konstruktion/")
_RIKS = ("Stockholms stad – Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_FUKT = ("Boverket – Fuktrisker för yttertak", "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttertak/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta: {namn} (pdf)", _OF + path + ".pdf")


LOC_V30 = {
 "Kungsholmen": {
   "intro": "På Kungsholmen är de flesta tak föreningarnas tak. Vi är takläggare på Kungsholmen för "
            "bostadsrättsföreningar och fastighetsägare – omläggning av plåttak, takkupor, takavvattning och "
            "underlag inför solceller, från Fredhäll och Kristineberg till Marieberg.",
   "paras": [
     "Stadens områdesfakta räknar 44 554 bostäder i Kungsholmens stadsdelsområde för 2024. Av dem "
     "var 30 598 bostadsrätter, och bara 337 låg i småhus. Den som hör av sig om ett tak här gör det därför "
     "nästan alltid för en förening eller en hyresvärd, och beslutet fattas av en styrelse efter ett underlag – "
     "inte vid köksbordet en kväll.",
     "Stadens beskrivning av riksintressena räknar Kungsholmen till den klassiska stenstaden, den täta "
     "kvartersstaden från 1870–1930 som också finns på Östermalm, Södermalm och Norrmalm. Taken där beskrivs "
     "som sluttande och oftast plåttäckta, med en lutning på upp till 45 grader från fasaden. Taklandskapet "
     "räknas som en del av det som ska bevaras.",
     "Men allt på Kungsholmen är inte stenstad. Samma text påpekar att hus som kom till under rivnings- och "
     "saneringsvågen 1950–1980 kan förändras med friare förutsättningar. Innan vi föreslår material eller kulör "
     "tar vi därför reda på när huset byggdes, hur det är klassat och vad detaljplanen säger.",
     "Ett plåttak på ett stenhus läggs om i etapper som styrelsen ofta vill kunna planera över flera år: först "
     "de takfall som läcker, sedan resten. Vi delar därför upp kostnadsförslaget i takfall och detaljer – "
     "takfot, ränndalar, skorstensbeslag, huvar och snörasskydd – så att föreningen ser vad som är akut och vad "
     "som kan vänta till nästa budgetår.",
   ],
   "items": ["Plåttak på föreningarnas hus", "Takkupor och detaljritningar", "Taket före solceller"],
   "why": "Vi utgår från Bromma och tar takuppdrag på hela Kungsholmen. Styrelsen får en skriftlig bedömning med "
          "foton från taket och vinden och ett kostnadsförslag som går att lägga fram på ett styrelsemöte.",
   "faq": [
     ("Kan vår förening få fram gamla ritningar på huset på Kungsholmen?",
      "Ja. Stockholms stad skriver att du själv kan leta fram och skriva ut äldre handlingar som "
      "stadsbyggnadskontoret har på fastigheten i e-tjänsten Bygg- och plantjänsten."),
     ("Hur vet styrelsen på Kungsholmen vad som är akut på taket?",
      "Efter besiktningen får ni foton och en bedömning per takfall och detalj. Läckage och skador som släpper in "
      "vatten markerar vi som akuta, slitage som kan vänta som planerat underhåll."),
     ("Får föreningen sätta solceller på taket på Kungsholmen utan bygglov?",
      "Oftast inte. Staden skriver att bygglov krävs för solceller i stora delar av Stockholm, eftersom området "
      "omfattas av Försvarsmaktens riksintresse för väderradarn i Håtuna."),
   ]},
 "Södermalm": {
   "intro": "Södermalm är till största delen flerbostadshus, och bakom nästan varje takbeställning står en förening "
            "eller en hyresvärd. Vi är takläggare på Södermalm för omläggning av plåttak, skorstensbeslag, takavvattning "
            "och takarbeten som ska stämmas av mot husets kulturvärden.",
   "paras": [
     "Enligt stadens områdesfakta fanns 77 525 bostäder i Södermalms stadsdelsområde 2025. 43 680 var "
     "bostadsrätter, 23 361 hyresrätter hos privata värdar och 10 471 hyresrätter i allmännyttan. Småhusen var "
     "211 till antalet. Här beställs alltså takarbeten av styrelser och förvaltare, och arbetet planeras ofta "
     "ihop med andra underhållsåtgärder i huset.",
     "Södermalm hör enligt stadens riksintressebeskrivning till den klassiska stenstaden från 1870–1930. Där "
     "betonas den enhetliga höjdskalan, de sammanbyggda gatufasaderna och de sluttande, oftast plåttäckta taken. "
     "Texten säger samtidigt att hus från saneringsåren 1950–1980 och kvarter där stenstaden aldrig byggdes "
     "färdigt kan ändras friare. Vilket som gäller avgörs hus för hus.",
     "Det som skiljer ett stenhustak från ett villatak är ofta antalet genomföringar. Där skorstenar, "
     "ventilationshuvar och takluckor står tätt är det vid varje genomföring som plåtarbetet avgör om taket "
     "håller tätt. Vi går därför igenom alla anslutningar från vinden och från taket innan vi föreslår en åtgärd.",
     "Södermalm är också kuperat. Kvarter på höjderna och längs branterna har tak som syns på långt håll, och "
     "gårdarna kan ligga på andra nivåer än gatan. Det påverkar hur ställning och materialhissar kan placeras "
     "och hur arbetet delas upp. Vi går igenom etableringen på plats med förvaltaren innan arbetet planeras in.",
   ],
   "items": ["Plåttak på stenhus", "Skorstenar och rökkanaler", "Hus med höga kulturvärden"],
   "why": "Vi utgår från Bromma och tar takuppdrag på hela Södermalm, från Hornstull till Danvikstull. Förvaltaren "
          "eller styrelsen får en skriftlig bedömning, foton och ett kostnadsförslag som visar vad som ingår. "
          "Behöver huset en antikvarisk förundersökning eller ett bygglov tar vi med det i tidplanen från början.",
   "faq": [
     ("Behöver föreningen göra en anmälan när en ny eldstad ansluts till skorstenen på Södermalm?",
      "Ja. Stockholms stad skriver att det krävs anmälan och startbesked för att installera en eldstad, skorsten "
      "eller rökkanal, och för att byta eldstad om det innebär en ny anslutning till befintlig rökkanal."),
     ("Vem beställer takarbetet i ett hyreshus på Södermalm?",
      "Fastighetsägaren eller förvaltaren. I ett hyreshus är det hyresvärden som äger huset och beställer "
      "arbetet, i en bostadsrättsförening är det styrelsen."),
     ("Ger takomläggningen på vårt hus på Södermalm rotavdrag?",
      "Nej, inte för den enskilda bostadsrättshavaren. Skatteverket ger inget rotavdrag för arbete på gemensamma "
      "ytor som tak och fasader."),
   ]},
 "Vasastan": {
   "intro": "I Vasastan är de flesta bostäder bostadsrätter, och taken är föreningarnas. Vi är takläggare i Vasastan för "
            "omläggning av plåttak, takfötter och takavvattning, och för det som sitter på taken: huvar, "
            "kanaler och aggregat som behöver anslutas tätt.",
   "paras": [
     "Stadens områdesfakta för 2025 räknar 12 579 bostäder i Västra Matteus och 8 889 i Gustav Vasa, de två "
     "statistikområden som täcker stora delar av Vasastan. I Västra Matteus var 8 990 av bostäderna "
     "bostadsrätter, i Gustav Vasa 5 707. Småhus finns i praktiken inte – i Västra Matteus redovisas inget "
     "enda. Takarbeten beställs därför av föreningar.",
     "Riksintressebeskrivningen tecknar stenstadens normalhus: fem våningar vid en 18 meter bred gata, en "
     "gatufasad som delas i sockelvåning och huvudfasad, en markerad takfot och ibland en attikavåning. "
     "Gårdsfasaderna är enklare. För en takläggare betyder det att takfoten mot gatan och plåtdetaljerna där "
     "hör till husets ansikte, medan gårdssidan oftast ger mer frihet i val av detaljer.",
     "Har taket fått nya installationer genom åren – frånluftsfläktar, kanaler, aggregat eller antenner – "
     "är varje sådan sak ett hål i taket som ska vara tätt. Vid en "
     "omläggning ser vi över alla genomföringar och föreslår vilka som kan samlas eller tas bort.",
     "Gatorna i Vasastan är raka och husen står i gatuliv, så takfoten hänger rakt över trottoaren. Det gör att "
     "snörasskydd, hängrännor och stuprör har en praktisk betydelse för fastighetsägaren på vintern, och att "
     "arbete vid takfoten behöver planeras så att gående kan passera tryggt. Vi går igenom hur arbetet mot gatan "
     "ska skyddas innan vi lämnar kostnadsförslaget.",
   ],
   "items": ["Plåttak och takfötter mot gatan", "Huvar, kanaler och aggregat", "Klassning och stadsbild"],
   "why": "Vi utgår från Bromma och tar takuppdrag i hela Vasastan, från Sankt Eriksplan till Odenplan och "
          "Roslagstull. Styrelsen får en skriftlig bedömning och ett kostnadsförslag med foton från taket, uppdelat "
          "på takfall och detaljer så att föreningen kan besluta i etapper om det behövs.",
   "faq": [
     ("Behöver vår förening i Vasastan bygglov för en ny ventilationshuv på taket?",
      "Oftast ja. Stockholms stad skriver att en ny ventilationshuv på taket eller en kanal på fasaden oftast "
      "kräver bygglov, eftersom det kan påverka byggnadens utseende."),
     ("Byter ni hängrännor och snörasskydd när taket i Vasastan läggs om?",
      "Ja, om de är slitna. Vid en omläggning brukar vi byta fotplåtar och hängrännor samtidigt, och vi föreslår "
      "snörasskydd där taket vetter mot gata eller gångväg."),
     ("Kan ett aggregat stå på taket utan bygglov i Vasastan?",
      "Staden skriver att ett enda aggregat som är mindre än 80 x 60 x 30 centimeter inte kräver bygglov om det "
      "inte påverkar husets karaktär och inte stör stadsbilden, till exempel genom att det inte syns från gatan."),
   ]},
 "Östermalm": {
   "intro": "På Östermalm är taken en del av stenstadens kulturvärden. Vi är takläggare på Östermalm för föreningar och fastighetsägare – omläggning av "
            "plåttak, takfötter, kupor och takavvattning – och tar fram underlaget som Stadsmuseet och "
            "stadsbyggnadskontoret behöver.",
   "paras": [
     "I statistikområdet Hedvig Eleonora på Östermalm fanns 7 344 bostäder 2025 enligt stadens områdesfakta. "
     "5 164 var bostadsrätter och 2 110 hyresrätter hos privata värdar, medan allmännyttan hade 68. "
     "Taken ägs alltså av föreningar och fastighetsägare, och det är styrelsen eller förvaltaren som beställer.",
     "Östermalm hör till den klassiska stenstaden från 1870–1930 enligt stadens riksintressebeskrivning. Där "
     "lyfts breda trädkantade esplanader, en enhetlig höjdskala och sammanbyggda fasader fram, liksom "
     "sluttande, oftast plåttäckta tak. Vindsinredningar och andra begränsade förändringar kan prövas, men "
     "enligt varsamhetskraven i plan- och bygglagen.",
     "Klassningen spelar stor roll här. Stadsmuseets karta markerar byggnader med blått, grönt, gult och grått, "
     "och riksintresset med en blå ring. Är huset blå- eller grönmarkerat krävs bygglov även för åtgärder som "
     "annars är lovfria. Vi börjar därför varje takprojekt med att slå upp fastigheten.",
     "Många tak på Östermalm har takkupor, torn och detaljer i plåt som är en del av husets arkitektur. När ett "
     "sådant tak läggs om är det detaljerna som tar tid: kupornas sidor och tak, ränndalar mellan takfall och "
     "dekorativa plåtar längs takfoten. Vi mäter och dokumenterar dem innan rivningen, så att de nya delarna "
     "får samma form och mått som de gamla.",
   ],
   "items": ["Plåttak på stenhus", "Kontakt med Stadsmuseet", "Takfötter, kupor och detaljer"],
   "why": "Vi utgår från Bromma och tar takuppdrag på hela Östermalm, från Strandvägen till Gärdet och "
          "Hjorthagen. Styrelsen får en skriftlig bedömning, foton och ett kostnadsförslag att besluta om. "
          "Behövs Stadsmuseets bedömning eller ett bygglov planerar vi in det innan ställningen beställs.",
   "faq": [
     ("Hur lång tid tar det att få Stadsmuseets bedömning av ett hus på Östermalm?",
      "Staden skriver att museet brukar svara inom tre veckor efter att det har fått alla efterfrågade "
      "uppgifter. Under helger och semestrar kan det ta längre tid."),
     ("Kan dekorativa plåtdetaljer på taket göras om i samma form på Östermalm?",
      "Ja. Vi mäter och fotograferar detaljerna innan de tas ner och tillverkar nya med samma profil och mått, "
      "så att taket ser ut som tidigare."),
     ("Vad ska föreningen skicka till Stadsmuseet?",
      "Adress, fastighetsbeteckning och stadsdel, byggår, eventuella ombyggnader och årtal för dem samt foton av "
      "fastigheten, både översiktliga och av fasaderna."),
   ]},
}

LOC_EXTRA_V30 = {
 "Kungsholmen": {"secs": [
   ("Solceller på ett tak i stenstaden", [
     "Många föreningar på Kungsholmen frågar om solceller. Stockholms stad skriver att bygglov ofta krävs, och "
     "att det beror på vilken typ av byggnad det är och vilket takfall panelerna ska sitta på. Staden pekar "
     "också på Försvarsmaktens riksintresse: inom eller i anslutning till det krävs bygglov för solceller i "
     "område med detaljplan, och därför i stora delar av Stockholm, bland annat på grund av väderradarn i Håtuna.",
     "Staden varnar för att dess vägledning om solenergianläggningar inte är uppdaterad efter lagändringarna "
     "1 december 2025. Anmälan behövs bara när byggnadens bärande delar eller brandskydd påverkas väsentligt. "
     "Vår del är taket under panelerna: ska ett plåttak bära solceller bör det vara omlagt eller i så gott skick "
     "att det inte behöver rivas strax efter montaget. Stadens solkarta ger en första bild av hur mycket sol "
     "taket får."]),
   ("Takkupor och detaljritningar", [
     "Stadens sida om flerbostadshus räknar mindre takkupor till de lovpliktiga fasadändringarna, medan en "
     "större takkupa räknas som en tillbyggnad. I båda fallen behövs ritningar. Fasadritningen görs i skala "
     "1:100, och för en ny takkupa kan staden vilja se en detaljritning i 1:10, 1:20 eller 1:50 som visar hur "
     "plåt, fönster och anslutningar mot det befintliga taket utförs.",
     "Vi hjälper föreningen och dess arkitekt med hur kupan ska täckas och anslutas, så att detaljerna på "
     "ritningen går att bygga och håller tätt i ränndalarna och vid takfoten."]),
   ("Ritningarna i arkivet och verkligheten på vinden", [
     "Äldre ritningar finns i stadens arkiv och kan hämtas i Bygg- och plantjänsten. Staden påpekar själv att "
     "ritningar kan vara ofullständiga och att det inte är säkert att de som byggde följde dem. Vi använder "
     "därför ritningarna som en karta men kontrollerar takstolar, underlag och genomföringar på plats.",
     "Det vi ser på vinden – fuktfläckar på råsponten, rost i infästningar, gamla lagningar – sammanfattar vi "
     "med foton i det underlag som styrelsen får."]),
   ("Gatusidan eller gårdssidan", [
     "För ett flerbostadshus skriver Stockholms stad att bygglov behövs när en ändring görs på en fasad eller ett "
     "tak som vetter mot allmän plats, till exempel en gata eller en park. Ändringar som inte vetter mot allmän "
     "plats kan göras utan lov om vissa förutsättningar är uppfyllda. Staden räknar byte av kulör eller material "
     "på taket som en fasadändring, liksom nya ventilationshuvar, skorstenar och solenergianläggningar.",
     "Samtidigt ska en lovfri ändring stämma med detaljplanen eller vara en liten avvikelse som inte motverkar "
     "planens syfte, och i särskilt kulturhistoriskt värdefulla miljöer krävs lov ändå. Ska föreningen byta "
     "från svart till grå plåt mot gatan är det alltså en lovfråga, medan samma byte mot gården kan vara lovfritt "
     "– om inget annat gäller för fastigheten. Vi tar reda på det innan kostnadsförslaget skrivs."]),
 ], "faq": [
   ("Får föreningen byta kulör på plåttaket mot gården utan bygglov på Kungsholmen?",
    "Ofta, om taket inte vetter mot allmän plats och huset inte är särskilt värdefullt. Staden skriver att "
    "lovfria ändringar ändå ska följa detaljplanen eller vara en liten avvikelse från den."),
   ("Behöver en större takkupa på Kungsholmen bygglov?",
    "En större takkupa räknas enligt Stockholms stad som en tillbyggnad. Mindre takkupor räknas som "
    "fasadändring, som på ett flerbostadshus är lovpliktig när den vetter mot allmän plats."),
   ("Ger takarbetet på föreningens hus på Kungsholmen rotavdrag?",
    "Nej. Skatteverket ger inget rotavdrag för arbete på gemensamma ytor som tak, fasader och trapphus."),
 ]},
 "Södermalm": {"secs": [
   ("Skorstenen – där takläggaren och sotaren möts", [
     "Stockholms stad skriver att det krävs anmälan och startbesked för att installera eldstad, skorsten eller "
     "rökkanal. Det gäller också när en spisinsats byts så att eldningsförhållandena ändras, när en tyngre "
     "eldstad kräver förstärkning av bärande delar och när en ny eldstad ansluts till en befintlig rökkanal med "
     "ny håltagning. En ny utvändig skorsten kan dessutom kräva bygglov och ska redovisas på fasadritningar.",
     "Staden råder fastighetsägare att tidigt rådgöra med skorstensfejarmästaren om både eldstad och "
     "skorstenens utformning och placering. För oss betyder det att skorstensbeslaget, takgenomföringen och "
     "eventuella stegar och gångbryggor planeras ihop med sotarens krav innan plåten läggs."]),
   ("När huset är särskilt värdefullt", [
     "Alla ändringar ska göras varsamt, och på ett särskilt kulturhistoriskt värdefullt hus får åtgärden inte "
     "förvanska byggnadens karaktär. Staden skriver att en detaljplan kan innehålla bestämmelser om utökad "
     "lovplikt, så att lov krävs även för underhållsåtgärder som annars är lovfria.",
     "Inför arbetet kan det behövas en antikvarisk förundersökning och en konsekvensbeskrivning, och ibland "
     "ska en certifierad sakkunnig inom kulturvärden kopplas in. Vi lägger in den tiden i planeringen, så att "
     "föreningen inte står med en ställning uppe medan underlaget tas fram."]),
   ("Hyresvärd eller förening", [
     "Med drygt 33 000 hyresrätter och nästan 44 000 bostadsrätter i stadsdelsområdet har Södermalm två sorters "
     "beställare. Hos en hyresvärd är det förvaltaren som tar beslutet, i en förening styrelsen och ibland "
     "stämman. Vi anpassar underlaget efter det – med foton, en beskrivning av skicket och ett kostnadsförslag "
     "uppdelat på de delar som kan beslutas var för sig."]),
   ("Flacka tak på gårdshus och tillbyggnader", [
     "Alla tak på Södermalm är inte branta stenstadstak. Gårdshus, påbyggnader och senare tillägg har ibland "
     "flacka eller låglutande tak täckta med papp eller plåt. Boverket skriver att låglutande tak ofta drabbas "
     "av läckage, vilket kan leda till fuktskador och dålig inomhusmiljö.",
     "På ett lågt tak rinner vattnet långsamt, och det samlas vid brunnar, skarvar och anslutningar mot högre "
     "väggar. Vi kontrollerar fall, brunnar och uppvik mot väggar och föreslår om taket kan lagas eller behöver "
     "ett nytt tätskikt. Det är ofta billigare att åtgärda ett lågt tak samtidigt som huvudtaket, eftersom "
     "ställning och etablering redan finns på plats."]),
 ], "faq": [
   ("Ska sotaren vara med när skorstensbeslaget görs om på Södermalm?",
    "Det är klokt. Stockholms stad råder fastighetsägare att tidigt rådgöra med skorstensfejarmästaren om "
    "skorstenens utformning och placering, och stegar och gångbryggor ska passa sotarens arbete."),
   ("Läcker flacka tak oftare än branta?",
    "Boverket skriver att låglutande tak ofta drabbas av läckage. Därför är brunnar, fall och anslutningar mot "
    "väggar det första vi kontrollerar på ett lågt tak."),
   ("Kan underhåll av taket kräva bygglov på Södermalm?",
    "Ja, om detaljplanen har bestämmelser om utökad lovplikt. Stockholms stad nämner underhållsåtgärder som ett "
    "exempel på vad som då kan kräva lov."),
   ("Kan ni göra takarbetet på Södermalm i etapper?",
    "Ja. Vi delar upp kostnadsförslaget i takfall och detaljer, så att föreningen eller hyresvärden kan ta det "
    "som läcker först och resten senare. Ställningen styr ofta hur etapperna läggs."),
   ("Vad innebär en antikvarisk förundersökning inför ett takarbete på Södermalm?",
    "Ett underlag som visar husets kulturvärden och hur en planerad åtgärd påverkar dem. Staden skriver att den "
    "kan behövas tillsammans med en konsekvensbeskrivning inför arbete på värdefulla byggnader."),
 ]},
 "Vasastan": {"secs": [
   ("Huvar, aggregat och kanaler på taket", [
     "Stockholms stad skriver att du inte behöver bygglov för en luftvärmepump, ett ventilationsaggregat eller "
     "liknande om det bara är ett aggregat, om det är mindre än 80 x 60 x 30 centimeter och om det inte påverkar "
     "byggnadens karaktär eller stör stadsbilden. En ny ventilationshuv på taket eller en kanal på fasaden "
     "kräver däremot oftast bygglov.",
     "När en förening i Vasastan lägger om taket är det ett bra tillfälle att se över allt som sticker upp. "
     "Uttjänta huvar kan tas bort och genomföringarna plåtas igen. Nya huvar placeras där de syns minst från "
     "gatan och där plåtslagaren kan ansluta dem tätt."]),
   ("Gula hus är inte automatiskt fria", [
     "Riksintressebeskrivningen konstaterar att många hus i stenstaden har en relativt låg klassning, gul klass, "
     "eftersom de har ändrats sedan de byggdes. Den säger samtidigt att stadsmiljön skulle förlora sin prägel om "
     "alla sådana hus byggdes om fritt, och att betydelsen för stadsmiljön ska vara avgörande vid prövningen – "
     "inte den enskilda byggnadens klassning.",
     "För ett tak betyder det att kulör, material och detaljer mot gatan ska passa in i gatans helhet även på "
     "ett gulklassat hus. Ligger huset dessutom inom riksintresset, som Stadsmuseets karta visar med en blå ring, "
     "krävs lov även för sådant som annars är lovfritt."]),
   ("Takfoten mot gatan", [
     "Takfoten och den översta delen av gatufasaden är det som syns mest av ett stenstadstak från gatan. "
     "Vid en omläggning byter vi hängrännor, fotplåtar och snörasskydd så att de följer husets befintliga "
     "linjer och kulör, och vi föreslår material efter vad huset har i dag."]),
   ("När vinden ska inredas", [
     "Riksintressebeskrivningen nämner vindsinredningar bland de mer begränsade förändringar som kan prövas i "
     "stenstaden, i enlighet med varsamhetskraven. Stadsbyggnadskontorets vägledningar för vindsinredningar och "
     "balkonger används som underlag vid prövningen.",
     "För taket innebär en vindsinredning ofta nya takkupor eller takfönster. Staden räknar en större takkupa som "
     "en tillbyggnad och mindre takkupor som en lovpliktig fasadändring. Vi ser till att de nya öppningarna "
     "planeras ihop med omläggningen, så att taket inte behöver brytas upp två gånger, och att plåtdetaljerna "
     "runt kuporna följer det övriga taket."]),
 ], "faq": [
   ("Var hittar föreningen ritningarna till huset i Vasastan?",
    "Stockholms stad skriver att äldre handlingar som stadsbyggnadskontoret har på fastigheten kan hämtas i "
    "e-tjänsten Bygg- och plantjänsten."),
   ("Kan föreningen lägga om taket och inreda vinden samtidigt i Vasastan?",
    "Ja, och det är ofta praktiskt. Nya takkupor kräver lov, och en större kupa räknas som tillbyggnad enligt "
    "Stockholms stad, så lovet bör vara klart innan omläggningen börjar."),
   ("Räcker det att huset är gulklassat för att slippa bygglov i Vasastan?",
    "Inte alltid. Gul eller grå markering kräver inte lov i sig, men ligger huset inom ett riksintresse eller i "
    "ett särskilt värdefullt område krävs lov ändå, enligt Stockholms stad."),
   ("Kan föreningen ta bort gamla huvar när taket läggs om?",
    "Ofta ja, om de inte längre används. Det minskar antalet genomföringar. Vi stämmer av med föreningen och "
    "ventilationsansvarig vilka kanaler som är ur bruk innan något tas bort."),
 ]},
 "Östermalm": {"secs": [
   ("Fråga Stadsmuseet i förväg", [
     "Stadsmuseets klassificeringskarta ger en första indikation på om ett hus är kulturhistoriskt värdefullt, "
     "men staden skriver att det kan behövas en bedömning från museet. Förfrågan skickas med e-post till "
     "Stadsmuseet tillsammans med adress, fastighetsbeteckning och stadsdel, byggår, eventuella ombyggnader och "
     "foton av fastigheten och dess fasader. Museet brukar svara inom tre veckor efter att allt har kommit in.",
     "Streckade ytor i kartan är miljöer som ännu inte har inventerats. Där kan bygglov krävas trots att huset "
     "saknar färg, och då är museets bedömning ett bra första steg innan föreningen beställer ritningar."]),
   ("Esplanaderna och taklandskapet", [
     "Riksintressebeskrivningen nämner breda trädkantade esplanader, en enhetlig höjdskala och sammanbyggda "
     "fasader i gatuliv som stenstadens kännetecken. Gatufasaden delas i sockelvåning och huvudfasad med en "
     "markerad takfot. Taket är därför den översta delen av en gatubild som är tänkt som en helhet.",
     "När vi lägger om ett plåttak här behåller vi takets form och lutning och stämmer av kulören mot huset. "
     "Detaljer som takfotens plåtar, snörasskydd och stuprör följer det befintliga mönstret."]),
   ("Utökad lovplikt och underhåll", [
     "En detaljplan kan enligt staden innehålla skyddsbestämmelser och bestämmelser om utökad lovplikt, och då "
     "kan även underhållsåtgärder kräva lov. Vi läser detaljplanen för fastigheten innan vi föreslår material, "
     "så att föreningen vet om omläggningen behöver lov innan arbetet planeras in.",
     "Om huset är särskilt värdefullt kan staden också kräva en antikvarisk förundersökning, en "
     "konsekvensbeskrivning eller att en certifierad sakkunnig inom kulturvärden följer arbetet. Det påverkar "
     "tidplanen mer än själva plåtarbetet, och därför tar vi upp frågan redan vid första besöket."]),
   ("Fukt från en kall vind", [
     "Under stenstadens plåttak finns ofta en vind som inte värms upp. Boverket skriver att kalla vindar ofta "
     "drabbas av fuktskador, och att det kan leda till dålig inomhusmiljö och hälsoproblem. Fukten kan komma "
     "uppifrån genom ett läckande tak, men också inifrån huset.",
     "Därför börjar vi en takbesiktning på Östermalm inne på vinden. Mörka partier på råsponten, mögellukt eller "
     "rost i plåtens infästningar visar var vatten eller fuktig luft har kommit in. Ibland räcker det att täta "
     "några genomföringar, ibland behöver underlaget bytas när plåten läggs om. Styrelsen får foton på det vi "
     "har sett och vår bedömning av vad som är brådskande och vad som kan vänta."]),
 ], "faq": [
   ("Vad betyder en streckad yta i Stadsmuseets karta på Östermalm?",
    "Att miljön ännu inte är inventerad. Bygglov kan ändå krävas, och föreningen kan be Stadsmuseet om en "
    "bedömning innan arbetet planeras."),
   ("Varför börjar ni på vinden när taket ska ses över på Östermalm?",
    "För att fuktskador ofta syns där först. Boverket skriver att kalla vindar ofta drabbas av fuktskador, och "
    "på råsponten syns var vatten har kommit in."),
   ("Ger takarbetet på vår förenings hus på Östermalm rotavdrag?",
    "Nej. Skatteverket ger inget rotavdrag för arbete på gemensamma ytor som tak och fasader."),
   ("Vem beställer takarbetet på ett stenhus på Östermalm?",
    "Ägaren. I en bostadsrättsförening är det styrelsen, och i ett hyreshus fastighetsägaren eller förvaltaren. "
    "Enskilda bostadsrättshavare beställer inte arbete på taket."),
   ("Vad betyder en blå ring i Stadsmuseets karta på Östermalm?",
    "Att området är riksintresse för kulturmiljövården. Där krävs bygglov även för åtgärder som annars är "
    "lovfria, enligt Stockholms stad."),
   ("Kan underhåll av ett tak på Östermalm kräva bygglov?",
    "Ja, om detaljplanen har bestämmelser om utökad lovplikt. Staden nämner underhållsåtgärder som ett exempel."),
 ]},
}

ORT_SEO_V30 = {
 "Kungsholmen": {"title": "Takläggare på Kungsholmen – plåttak för föreningar",
                 "desc": "Takläggare på Kungsholmen för bostadsrättsföreningar: plåttak, takkupor och detaljritningar, "
                         "taket före solceller och underlag till styrelsen."},
 "Södermalm":   {"title": "Takläggare på Södermalm – plåttak, skorstenar och lov",
                 "desc": "Takläggare på Södermalm för föreningar och hyresvärdar: plåttak på stenhus, skorstenar och "
                         "rökkanaler, utökad lovplikt och antikvariska underlag."},
 "Vasastan":    {"title": "Takläggare i Vasastan – plåttak, takfot och huvar",
                 "desc": "Takläggare i Vasastan för bostadsrättsföreningar: plåttak och takfötter mot gatan, "
                         "ventilationshuvar och aggregat, klassning och bygglov."},
 "Östermalm":   {"title": "Takläggare på Östermalm – plåttak och Stadsmuseet",
                 "desc": "Takläggare på Östermalm för föreningar: plåttak på stenhus, Stadsmuseets bedömning, utökad "
                         "lovplikt och takfötter som följer gatubilden."},
}

ORT_SRC_V30 = {
 "Kungsholmen": [_of("Kungsholmens stadsdelsområde", "kungsholmen/kungsholmens-stadsdelsomrade"), _RIKS, _SOL,
                 _FLERBO, _FASAD, _BAR, _SKV],
 "Södermalm":   [_of("Södermalms stadsdelsområde", "sodermalm/sodermalm-stadsdelsomrade"), _RIKS, _SKORST, _KULT, _FUKT, _SKV],
 "Vasastan":    [_of("Västra Matteus", "norra-innerstaden/vastra-matteus"), _of("Gustav Vasa", "norra-innerstaden/gustav-vasa"),
                 _RIKS, _HUV, _KLASS, _FLERBO],
 "Östermalm":   [_of("Hedvig Eleonora", "norra-innerstaden/hedvig-eleonora"), _RIKS, _KLASS, _KULT, _FUKT, _SKV],
}

# (alt hero, alt bild 2), alt bild 3 och prompter för gen_images_flux.py.
ORT_HERO_ALT_V30 = {
 "Kungsholmen": ("Sammanbyggda stenhus med branta plåttak längs en gata i innerstaden",
                 "Svart falsat plåttak med takkupor på ett stenhus från sekelskiftet"),
 "Södermalm": ("Takåsar med plåttak och murade skorstenar över ett kvarter med stenhus",
               "Murad skorsten med nytt plåtbeslag på ett falsat plåttak"),
 "Vasastan": ("Stenhus i fem våningar med markerad takfot mot en bred gata",
              "Ventilationshuvar och plåtgenomföringar på ett grått falsat plåttak"),
 "Östermalm": ("Sammanbyggda stenhus med plåttak och takkupor längs en trädkantad esplanad",
               "Takfot med plåtdetaljer och stuprör på ett sekelskiftshus i sten"),
}
ORT_IMG3_V30 = {
 "Kungsholmen": "Solpaneler monterade på ett plåttak ovanför en innergård",
 "Södermalm": "Takstege och gångbrygga vid en skorsten på ett plåttak",
 "Vasastan": "Hängränna och snörasskydd längs takfoten på ett stenhus",
 "Östermalm": "Plåttak med takkupor och skorstenar över ett kvarter med stenhus",
}
ORT_IMG_PROMPTS_V30 = {
 "taklaggare-kungsholmen-1": ("4:3", "row of joined late 19th century Stockholm stone apartment buildings, five storeys, plastered facades in ochre and grey, steep black standing seam metal roofs with small dormers, a calm city street with trees, overcast daylight" + _SFX),
 "taklaggare-kungsholmen-2": ("3:2", "close view of a black standing seam metal roof with two small metal clad dormers on a Stockholm stone apartment building from around 1900, roof ridge and chimney visible, soft daylight" + _SFX),
 "taklaggare-kungsholmen-3": ("3:2", "rows of dark solar panels mounted on brackets over a grey standing seam metal roof of an old Stockholm apartment building, other roofs and chimneys in the background, clear sky" + _SFX),
 "taklaggare-sodermalm-1": ("4:3", "rooftops of a Stockholm stone city block seen from above, grey and black standing seam metal roofs, many brick chimneys and ventilation hoods, copper green church tower far away, late afternoon light" + _SFX),
 "taklaggare-sodermalm-2": ("3:2", "close view of a rendered brick chimney on a grey standing seam metal roof with a new neatly folded metal flashing around its base, overcast daylight" + _SFX),
 "taklaggare-sodermalm-3": ("3:2", "black metal roof ladder and a short metal walkway leading to a chimney on a steep grey standing seam metal roof of an old apartment building, city roofs behind, daylight" + _SFX),
 "taklaggare-vasastan-1": ("4:3", "five storey Stockholm stone apartment building from 1890s with plastered facade, ground floor base, marked cornice and a sloping metal roof, seen from across an empty street early on a Sunday morning, street completely empty, no pedestrians, no cars, spring daylight" + _SFX),
 "taklaggare-vasastan-2": ("3:2", "several round metal ventilation hoods and pipe penetrations with folded metal collars on a grey standing seam metal roof of an old apartment building, overcast sky" + _SFX),
 "taklaggare-vasastan-3": ("3:2", "close view of the eaves of an old stone apartment building: half-round metal gutter, snow guard rail and the edge of a standing seam metal roof above a plastered cornice, daylight" + _SFX),
 "taklaggare-ostermalm-1": ("4:3", "row of joined five storey Stockholm stone apartment buildings from the 1890s with plastered facades in light ochre and grey, flat fronts with straight cornices, black standing seam metal roofs with small dormers, along a wide tree-lined boulevard, no stepped gables, no Dutch gables, empty street, autumn daylight" + _SFX),
 "taklaggare-ostermalm-2": ("3:2", "close view of the eaves of a stone apartment building from around 1900: decorated cornice, metal edge flashing, half-round gutter and a downpipe, daylight" + _SFX),
 "taklaggare-ostermalm-3": ("3:2", "view across the rooftops of a dense Stockholm stone city block of five storey apartment buildings: black standing seam metal roof with several small dormers and brick chimneys, other metal roofs in the foreground, no detached houses, soft evening light" + _SFX),
}
