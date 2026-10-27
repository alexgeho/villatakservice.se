# -*- coding: utf-8 -*-
"""Takbyte – ortsidor v24: Farsta, Hägersten, Hässelby, Spånga, Vällingby, Älvsjö (2026-10-26).
Hubb: takbyte.html (TJ_HUB["takbyte"]). Intent som tj_v21/v22_takbyte.py: byte av hela taktäckningen med regler,
kontroll och ROT – skild från ortens takrenovering-<ort>.html, taklaggare-<ort>.html och platslagare-<ort>.html.
Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.

Lokal vinkel per sida (en huvudfråga per sida, skild från ortens takläggar- och takrenoveringssidor):
Farsta – radhus och kedjehus i tunnelbanestaden: vem beställer takbytet (äganderätt eller bostadsrätt, stadgarna,
  bostadsrättslagen 7 kap. 7 och 12 §§), Skatteverkets regel om gemensamma ytor (tak) i bostadsrätt, områdesfakta 2025
  per område, Farsta som kulturhistoriskt värdefull miljö (Varsam-tabellen) och längan som en helhet.
Hägersten – samma material eller nytt: Boverkets gräns mellan underhåll och fasadändring (byte till annat material,
  samma material = underhåll), Stadsmuseets karta (blå/grön ring, blått/grönt/gult/grått, streckat = ej inventerat),
  Mälarhöjden (kulturhistoriskt värdefull miljö och generösa byggrätter), områdesfakta 2025.
Hässelby – eternit och asbest på taket: Varsam om asbestcement i Hässelby, Arbetsmiljöverkets krav (tillstånd för
  rivning på tak eller fasad utomhus, byggnader fram till 1982, byggherrens utredning, riv asbest först, provtagning),
  Boverket, Skatteverket (ROT för sanering, inte mätning), områdesfakta.
Spånga – solceller på det nya taket: Stockholms stads regel om bygglov för solceller inom eller i anslutning till
  Försvarsmaktens riksintresse (väderradarn i Håtuna), utökad lovplikt i kulturhistoriskt värdefulla områden (Solhem
  i Varsam-tabellen), integrerade paneler som byte av taktäckningsmaterial (Boverket), villastäderna och områdesfakta.
Vällingby – de gruppbyggda småhusen: Kälvesta (egen småhusstadsdel, liggande träpanel och sadeltak), Vinsta, Nälsta,
  Atlantis och Omega, riksintresset Vällingby–Råcksta, Varsams påverkansaspekter (takens form, material, färgsättning)
  och husgruppen som helhet.
Älvsjö – vinden och takbytet i samma veva: Älvsjö villastad (Hallmans plan, branta tegeltäckta sadeltak med kupa enligt
  Stadsmuseets inventering), generösa byggrätter i äldre planer (Långbro, Herrängen, Långsjö), takkupor som fasadändring,
  anmälan vid ingrepp i bärande konstruktion, områdesfakta.

Fakta endast från källorna i respektive 'sources', öppnade med curl/urllib (Mozilla-UA) 2026-10-26, alla 200;
pdf:erna (Varsam, områdesfakta, Stadsmuseets inventering av Älvsjö) har textlager.
Strukna / ej använda: Stadsmuseets svarstid, avgifter och handläggningstider, att stadgarna i en viss förening lägger
taket på medlemmen (varierar – skrivet som fråga att kontrollera), vilka hus i Hässelby som har eternittak (ingen
källa – skrivet som möjlighet), alla priser, garantier, omdömen, egna uppdrag i orterna och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no text, no letters"

_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"
_STH_FAS = ("Stockholms stad – Fasadändring", _SB + "fasadandring/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_STH_SOL = ("Stockholms stad – Solceller, solpanel, solfångare", _SB + "solceller-solpanel-solfangare/")
_STH_KV = ("Stockholms stad – Kulturhistorisk värdefull byggnad och område", _SB + "kulturhistorisk-vardefull-byggnad-och-omrade/")
_STH_BAR = ("Stockholms stad – Ändra i bärande konstruktion",
            "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/andra-i-barande-konstruktion/")
_BV_FAS = ("Boverket – Fasadändring (PBL kunskapsbanken)",
           "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_BV_ASB = ("Boverket – Risker med hantering av asbest i byggnader",
           "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_AV_TILL = ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest",
            "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/")
_AV_FOR = ("Arbetsmiljöverket – Förebygg riskerna med asbest",
           "https://www.av.se/halsa-och-sakerhet/kemiska-risker/risker-for-vissa-amnen-produkter-och-verksamheter/asbest/forebygg-riskerna-med-asbest/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 och 12 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_ALV_INV = ("Stadsmuseet – Inventering av Älvsjö villastad (Stockholmskällan, pdf)",
            "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf")

_ROT_AMT = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
            "tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ FARSTA
"takbyte-farsta.html": {
  "kind": "district", "service": "takbyte", "ort": "Farsta", "svc_label": "Takbyte",
  "title": "Takbyte i Farsta – radhusen, längan och föreningen",
  "description": "Takbyte i Farsta: radhus i tunnelbanestaden, vem som beställer taket i äganderätt och bostadsrätt, stadgarna, ROT-reglerna och längan som helhet.",
  "h1": "Takbyte i Farsta",
  "lead": "På ett radhus i Farsta är första frågan inte vilket takmaterial du ska välja utan vem som beställer takbytet: du, grannarna i längan eller bostadsrättsföreningen. Geal Entreprenad AB byter tak på radhus, kedjehus och villor i Farsta och tar fram ett underlag som passar den som ska fatta beslutet.",
  "card": "Radhusen, längan och föreningen.",
  "sections": [
    {"id": "radhusen-farsta", "anchor": "Radhusen",
     "h2": "Radhusen längst ut från centrum",
     "paras": [
       "Farsta stod klart 1961 som en av stadens tunnelbanestadsdelar. Enligt stadens strategi för småhusområden placerades de högre husen närmast centrum och tunnelbanestationen, och längst ut kom grupper av rad- och kedjehus. Farsta planerades i stor utsträckning för bilen, med stora parkeringsplatser vid centrum och en mer öppen struktur än i Vällingby.",
       "Strategin beskriver gestaltningen i Farsta som präglad av höga ambitioner, med fasader i rött tegel men också puts och skivor i fibercement. Husen i en grupp byggdes ofta likadana, och strategins tabell markerar tunnelbanestaden Farsta som kulturhistoriskt värdefull miljö. Ett tak som ser annorlunda ut än grannarnas syns därför i hela gruppen.",
     ],
     "aside": {"title": "Småhus i Farsta stadsdel 2025", "items": [
       "Äganderätt: 418", "Bostadsrätt: 126"]}},
    {"id": "vem-farsta", "h2": "Vem beställer taket?",
     "paras": [
       "Stadens områdesfakta för 2025 visar att Farstas småhus ägs på olika sätt. I Farsta strand finns 291 småhus med äganderätt och 31 med bostadsrätt, i Larsboda 131 respektive 65 och i Hökarängen 91 med äganderätt men 232 med bostadsrätt. I hela Farsta stadsdelsområde är 3 806 småhus äganderätter och 639 bostadsrätter.",
       "Äger du ditt radhus beställer du själv, men eftersom taken i en länga hänger ihop lönar det sig att prata med grannarna innan materialet väljs. Bor du i en bostadsrätt avgör föreningens stadgar vem som svarar för taket. Bostadsrättslagen säger att du håller lägenheten i gott skick på egen bekostnad, om inte stadgarna bestämmer något annat, och ingrepp i bärande konstruktion kräver styrelsens tillstånd.",
     ],
     "aside": {"title": "Fråga först", "items": [
       "Äganderätt eller bostadsrätt?", "Vad säger stadgarna om taket?", "Byter grannarna samtidigt?"]}},
    {"id": "langan-farsta", "h2": "Hela längan eller ett hus i taget",
     "paras": [
       "Stadens strategi ger rådet att förändra sammanhållna grupper av småhus utifrån ett helhetsperspektiv och att ta tillvara eller återskapa karaktärsskapande material och kulörer. För ett radhustak betyder det i praktiken samma takmaterial, samma kulör och samma detaljer vid takfot och nock som grannarna, även när husen byts vid olika tillfällen.",
       "När flera hus i längan byts samtidigt kan ställning, avfallshantering och leveranser samordnas, och anslutningarna mellan husen görs i ett svep. När bara ett hus byts lägger vi särskild vikt vid anslutningen mot grannens tak, så att skarven blir tät och vattnet leds rätt. Om tjänsten i stort kan du läsa under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
    {"id": "lov-farsta", "h2": "Lov för ett nytt takmaterial",
     "paras": [
       "Att byta taktäckningsmaterial räknas som fasadändring. På ett en- eller tvåbostadshus krävs normalt inget bygglov, men Stockholms stad påpekar att utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla byggnader och områden. Stadsmuseets klassificeringskarta ger en första indikation på om din fastighet berörs.",
       "Byter du till samma material och utförande som förut är det underhåll och ingen fasadändring. Därför börjar vi med att ta reda på vad som ligger på taket i dag och vad grannarna har. Om husen i Farsta och vanliga takproblem kan du läsa under " + _L.format("taklaggare-farsta.html", "takläggare i Farsta") + ".",
     ],
     "aside": None},
    {"id": "underlag-farsta", "h2": "Underlag till styrelsen eller grannarna",
     "paras": [
       "Ett beslut om takbyte i en förening eller en länga blir enklare med ett gemensamt underlag. Vi beskriver takets skick hus för hus, vad som behöver bytas under pannorna och hur arbetet kan delas upp i etapper.",
       "Kostnadsförslaget delar vi upp så att varje hus eller etapp går att läsa för sig. Då kan styrelsen eller grannarna se vad som är gemensamt, som ställning och etablering, och vad som hör till varje tak.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Farsta till",
  "steps": [
    ("Ägarform och stadgar", "Vi reder ut vem som beställer och vad stadgarna säger om taket."),
    ("Platsbesök", "Taket, anslutningarna mot grannarna och detaljerna går vi igenom."),
    ("Skriftligt kostnadsförslag", "Uppdelat per hus eller etapp, med gemensamma poster för sig."),
    ("Kartan", "Stadsmuseets karta kontrolleras om materialet ska bytas."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Genomgång", "Vi går igenom taket och anslutningarna med dig eller styrelsen."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Farsta",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor och hängrännor på ett småhus som rotarbete. I en bostadsrätt gäller andra regler: arbetet ska utföras i bostaden och gälla det du ansvarar för enligt stadgarna, och arbete på gemensamma ytor som tak och fasader ger inget rotavdrag.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Farsta?",
  "price": [
    "Takets yta, materialet, hur mycket underlag som behöver bytas, anslutningarna mot grannhusen och om flera hus byts samtidigt. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem betalar takbytet på ett radhus i bostadsrätt i Farsta?",
     "Det avgör föreningens stadgar. Bostadsrättslagen utgår från att du håller lägenheten i gott skick om inte stadgarna säger annat, så läs stadgarna innan något beställs."),
    ("Får vi rotavdrag för taket på vårt bostadsrättsradhus?",
     "Nej, enligt Skatteverket ger arbete på gemensamma ytor som tak och fasader i en bostadsrätt inget rotavdrag."),
    ("Måste hela längan byta tak samtidigt?",
     "Nej, men stadens strategi råder att grupper av småhus förändras utifrån helheten. Samma material och kulör som grannarna håller ihop längan även när husen byts vid olika tillfällen."),
    ("Är tunnelbanestaden Farsta kulturhistoriskt värdefull?",
     "Ja, i stadens strategi för småhusområden är Farsta markerat som kulturhistoriskt värdefull miljö. Stadsmuseets karta visar vad som gäller för din fastighet."),
  ],
  "sources": [_VARSAM, ("Stockholms stad – Områdesfakta 2025: Farsta (pdf)", _OF + "soderort/farsta/farsta.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Farsta strand (pdf)", _OF + "soderort/farsta/farsta-strand.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Larsboda (pdf)", _OF + "soderort/farsta/larsboda.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hökarängen (pdf)", _OF + "soderort/farsta/hokarangen.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Farsta stadsdelsområde (pdf)", _OF + "soderort/farsta/farsta-stadsdelsomrade.pdf"),
              _BRL, _STH_FAS, _BV_FAS, _SKV, _SKV2],
  "cta": ("Ska radhuset i Farsta få nytt tak?", "Boka ett gratis platsbesök, så går vi igenom taket och anslutningarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Länga av radhus i tegel med sadeltak av mörka betongpannor",
     "row of 1960s Swedish terraced houses with low-pitched gable roofs of dark concrete roof tiles, red brick and light rendered facades, small front gardens with low hedges, pedestrian path, suburban Stockholm, summer" + _IMG_END),
    ("Ny underlagsduk utrullad över ett takfall",
     "two adjoining roofs of 1960s Swedish brick terraced houses in the same row, low pitch, seen slightly from above, one freshly re-roofed with new dark roof tiles and new metal flashing, the neighbouring roof older with moss, scaffolding along the eaves, daylight" + _IMG_END),
    ("Takfot med ny hängränna och nytt stuprör på ett radhus i tegel",
     "close view of the eaves of a 1960s Swedish terraced house with new galvanised gutter, new eaves flashing and fresh roof tiles, brick wall below, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HÄGERSTEN
"takbyte-hagersten.html": {
  "kind": "district", "service": "takbyte", "ort": "Hägersten", "svc_label": "Takbyte",
  "title": "Takbyte i Hägersten – samma material eller ett nytt?",
  "description": "Takbyte i Hägersten: när nytt takmaterial är fasadändring och när det är underhåll, Stadsmuseets karta och Mälarhöjden som värdefull miljö.",
  "h1": "Takbyte i Hägersten",
  "lead": "Vid ett takbyte i Hägersten avgör ett enda val om du behöver tänka på bygglov: lägger du samma material igen eller byter du till ett annat? Geal Entreprenad AB byter tak på villor och radhus i Mälarhöjden, Västberga och resten av Hägersten och reder ut frågan innan materialet beställs.",
  "card": "Samma material eller ett nytt.",
  "sections": [
    {"id": "materialet-hagersten", "anchor": "Materialet",
     "h2": "Underhåll eller fasadändring",
     "paras": [
       "Boverket förklarar att byte av taktäckningsmaterial betyder ändring till ett annat material, till exempel från tegeltak till plåttak. Det kan också vara tak med integrerade solceller eller solfångare. Att byta till samma material och utförande som förut är däremot inte en fasadändring utan underhåll.",
       "Gränsen spelar roll eftersom fasadändringar på villor i särskilt kulturhistoriskt värdefulla områden kräver bygglov, medan underhåll inte gör det. Lägger du tegel på ett tegeltak är du på den säkra sidan. Vill du byta till plåt, betongpannor eller ett annat utförande kontrollerar vi först vad som gäller för just din fastighet.",
     ],
     "aside": {"title": "Enligt Boverket", "items": [
       "Samma material = underhåll", "Annat material = fasadändring", "Integrerade solpaneler kan räknas som nytt material"]}},
    {"id": "kartan-hagersten", "h2": "Stadsmuseets karta",
     "paras": [
       "Stockholms stad hänvisar till Stadsmuseets klassificeringskarta. Riksintressen för kulturmiljövården har blå ring, områden som översiktsplanen pekar ut som särskilt kulturhistoriskt värdefulla har grön ring, och klassificerade byggnader är markerade med blått, grönt, gult eller grått. Inom ring eller med blå eller grön markering behöver du bygglov för åtgärder som annars är lovfria.",
       "Gul eller grå markering kräver inget lov om inget annat skäl talar för det. Streckade ytor är miljöer som ännu inte inventerats, och där kan lov behövas. Staden betonar att du som byggherre själv ansvarar för att ta reda på vad som gäller, och att du kan kontakta Stadsmuseet för rådgivning.",
     ],
     "aside": {"title": "Kartans markeringar", "items": [
       "Blå ring: riksintresse", "Grön ring: särskilt värdefullt område", "Blått eller grönt: lov krävs", "Gult eller grått: normalt inget lov", "Streckat: ej inventerat"]}},
    {"id": "malarhojden-hagersten", "h2": "Mälarhöjden och de äldre villorna",
     "paras": [
       "Mälarhöjden växte upp som villasamhälle efter privata initiativ genom större markförvärv, skriver staden i sin strategi för småhusområden. I strategins tabell är Mälarhöjden markerat både som kulturhistoriskt värdefull miljö och som område med generösa byggrätter i äldre planer.",
       "Enligt stadens områdesfakta för 2025 finns 988 småhus med äganderätt i Mälarhöjden och 955 i stadsdelen Hägersten. Bebyggelsen i villastäderna är enligt strategin brokig, med hus från flera epoker. Därför ser vi på varje hus för sig, och om det befintliga taket redan är ett byte från originalet går vi tillbaka till ritningarna.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Mälarhöjden: 988", "Hägersten: 955", "Västberga: 280", "Fruängen: 149"]}},
    {"id": "varsamt-hagersten", "h2": "Varsamhetskravet och detaljerna",
     "paras": [
       "Stockholms stad påpekar att alla ändringar ska göras varsamt, oavsett om byggnaden är kulturhistoriskt värdefull eller inte, och att en byggnad som är särskilt värdefull inte får förvanskas. Kraven gäller oavsett om åtgärden kräver lov eller anmälan.",
       "För ett takbyte betyder det att detaljerna också räknas: takfotens utformning, vindskivor, nockens avslutning och plåtarbetena kring skorsten och kupor. Vi tar bilder av detaljerna innan det gamla taket rivs och lägger tillbaka dem på samma sätt. Om husen och vanliga takproblem i stadsdelen kan du läsa under " + _L.format("taklaggare-hagersten.html", "takläggare i Hägersten") + ".",
     ],
     "aside": None},
    {"id": "underlaget-hagersten", "h2": "Det som ligger under pannorna",
     "paras": [
       "När det gamla taket är av ser vi läkt, underlagstäckning och råspont. Skadat trä byts innan något nytt läggs, och plåten kring skorstenar, kupor och ränndalar görs om i samma arbete.",
       "Behöver taket bara ses över utan att bytas kan du läsa om " + _L.format("takbyte-eller-takrenovering.html", "takbyte eller takrenovering") + ". Om tjänsten i stort finns mer under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Hägersten till",
  "steps": [
    ("Platsbesök", "Vi ser vad som ligger på taket i dag och vilka detaljer huset har."),
    ("Kartan", "Stadsmuseets karta och detaljplanen kontrolleras för fastigheten."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt och plåt står var för sig."),
    ("Bygglov vid behov", "Ansökan om nytt material i ett värdefullt område tas fram när det krävs."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Genomgång", "Vi går igenom taket och detaljerna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Hägersten",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor, plåttak, hängrännor och stuprör på ett småhus som rotarbete. Att rengöra takpannor och hängrännor räknas också som rotarbete.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Hägersten?",
  "price": [
    "Takets yta och form, materialet, antalet kupor och skorstenar, hur mycket underlag som behöver bytas och om bygglov krävs. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för att lägga nytt tegel på vårt tegeltak i Mälarhöjden?",
     "Nej, byte till samma material och utförande är underhåll enligt Boverket och ingen fasadändring."),
    ("Vad betyder gul markering i Stadsmuseets karta för vårt tak?",
     "Gul eller grå markering kräver normalt inget bygglov för fasadändring, om inte fastigheten berörs av något annat skäl, till exempel en ring i kartan eller en skyddsbestämmelse i detaljplanen."),
    ("Vårt hus är streckat i kartan – vad betyder det?",
     "Att miljön ännu inte är inventerad. Där kan bygglov behövas, och Stockholms stad hänvisar till Stadsmuseet för rådgivning."),
    ("Räknas tak med inbyggda solceller som nytt takmaterial?",
     "Ja, Boverket nämner tak- eller fasadintegrerade solceller som ett exempel på byte av taktäckningsmaterial."),
  ],
  "sources": [_BV_FAS, _STH_KL, _STH_KV, _STH_FAS, _VARSAM,
              ("Stockholms stad – Områdesfakta 2025: Mälarhöjden (pdf)", _OF + "soderort/hagersten/malarhojden.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hägersten (pdf)", _OF + "soderort/hagersten/hagersten.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Västberga (pdf)", _OF + "soderort/hagersten/vastberga.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Fruängen (pdf)", _OF + "soderort/hagersten/fruangen.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska taket på huset i Hägersten bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och vad som gäller för fastigheten innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre villa med brant tegeltak bland ekar på en höjd",
     "early 1900s Swedish wooden villa with steep red clay tile roof, small dormer and chimney, light painted panel facade with white trim, large oak trees on a hilly plot near lake Mälaren, Stockholm, summer" + _IMG_END),
    ("Tak under omläggning med underlagsduk, läkt och ställning runt huset",
     "freshly laid red clay tile roof on an old Swedish villa with new standing seam flashing around a brick chimney and new ridge tiles, close view, daylight" + _IMG_END),
    ("Tak där teglet delvis tagits av så att råsponten syns, med pannor på ställningen",
     "old roof with clay tiles removed showing wooden roof boarding, new underlay membrane and new battens, stack of red tiles on the scaffolding, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HÄSSELBY
"takbyte-hasselby.html": {
  "kind": "district", "service": "takbyte", "ort": "Hässelby", "svc_label": "Takbyte",
  "title": "Takbyte i Hässelby – eternit och asbest på taket",
  "description": "Takbyte i Hässelby: asbestcement på 1960- och 70-talens hus, tillstånd för rivning av asbest på tak, provtagning före start och ROT för sanering.",
  "h1": "Takbyte i Hässelby",
  "lead": "Har huset i Hässelby byggts före 1982 kan det gamla taket innehålla asbest, och då ska det utredas innan rivningen börjar. Geal Entreprenad AB byter tak på villor, radhus och kedjehus i Hässelby och börjar med att ta reda på vad det gamla materialet består av.",
  "card": "Eternit och asbest på taket.",
  "sections": [
    {"id": "eterniten-hasselby", "anchor": "Eterniten",
     "h2": "Asbestcement i Hässelbys hus",
     "paras": [
       "Stadens strategi för småhusområden beskriver hur många villor i Hässelby villastad på 1960- och 1970-talen ersattes av täta grupper av enhetlig småhusbebyggelse. Om Hässelby skriver strategin också att man i många områden prövade nya material, och att asbestcement, mer känt som eternit, var populärt.",
       "Eterniten innehöll det hälsovådliga ämnet asbest och har i många fall bytts ut, enligt strategin. Boverket nämner takskivor, takpannor och fasadskivor bland de produkter där asbest kan finnas, och skriver att provtagning och analys är det enda säkra sättet att veta.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Hässelby villastad: 4 757", "Hässelby gård: 324", "Hässelby-Vällingby: 9 216"]}},
    {"id": "1982-hasselby", "h2": "Utgå från att huset kan innehålla asbest",
     "paras": [
       "Arbetsmiljöverket skriver att man ska utgå från att alla byggnader som uppförts fram till 1982 kan innehålla asbest, eftersom asbest användes fram till förbudet 1982. Även senare byggnader kan i vissa fall innehålla asbest, eftersom produkter fanns kvar i lager eller importerades.",
       "Vid minsta osäkerhet ska ett prov tas och skickas till ett laboratorium som analyserar det. Därför börjar ett takbyte på ett hus från den tiden med provtagning av det material som ska rivas.",
     ],
     "aside": None},
    {"id": "byggherren-hasselby", "h2": "Du är byggherre",
     "paras": [
       "Enligt Arbetsmiljöverket är det byggherre, projektör och arbetsgivare som ska se till att en undersökning och vid behov provtagning görs. Som husägare som beställer ett takbyte är du byggherre, och den som ska utföra arbetet ska få skriftlig information om det finns asbest i byggnaden.",
       "En arbetsgivare som är det minsta osäker får inte låta någon börja förrän det är klarlagt, och ska då begära ett skriftligt besked från ägaren. Vi hjälper dig att beställa analysen och sammanställa beskedet, så att det finns svart på vitt innan ställningen sätts upp.",
     ],
     "aside": {"title": "Före rivningen", "items": [
       "Provtagning och analys", "Skriftligt besked om resultatet", "Asbesten rivs först", "Avspärrat område och skyltar"]}},
    {"id": "rivningen-hasselby", "h2": "Rivning av asbest kräver tillstånd",
     "paras": [
       "Ett företag som ska riva eller sanera asbesthaltigt material behöver tillstånd från Arbetsmiljöverket, och rivning av asbesthaltigt material på tak eller fasad utomhus är ett av exemplen. Förarbete, omhändertagande av avfallet och städning efteråt räknas också som rivning och sanering.",
       "Asbesten ska så långt det går rivas först, innan annan rivning görs, och området ska vara avspärrat och skyltat. Visar provet asbest anlitas ett företag med tillstånd för den delen, och vi lägger det nya taket när saneringen är klar. Om villastadens tak i övrigt kan du läsa under " + _L.format("takrenovering-hasselby.html", "takrenovering i Hässelby") + ".",
     ],
     "aside": None},
    {"id": "nya-taket-hasselby", "h2": "Det nya taket",
     "paras": [
       "När det gamla materialet är borta ser vi underlaget: läkt, underlagstäckning och råspont. Skadat trä byts, och plåten vid takfot, nock och genomföringar görs om i samma arbete.",
       "För radhusens fasader påpekar strategin att det i dag finns skivor utan asbest som gör det möjligt att behålla uttrycket. Samma tanke gäller taket: ligger huset i en grupp med enhetliga tak väljer vi ett material som liknar grannarnas. Om tjänsten i stort kan du läsa under " + _L.format("takbyte.html", "takbyte") + " och om husen i stadsdelen under " + _L.format("taklaggare-hasselby.html", "takläggare i Hässelby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Hässelby till",
  "steps": [
    ("Platsbesök", "Taket och husets byggår går vi igenom på plats."),
    ("Provtagning", "Prov tas på misstänkt material och skickas för analys."),
    ("Skriftligt kostnadsförslag", "Sanering, rivning, underlag och nytt tak står var för sig."),
    ("Sanering", "Asbesthaltigt material rivs först av företag med tillstånd."),
    ("Takbyte", "Underlaget ses över och det nya taket läggs."),
    ("Genomgång", "Vi går igenom taket och lämnar dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Hässelby",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor, plåttak och hängrännor på ett småhus som rotarbete, och även sanering av asbest i samband med byggarbete. Att mäta asbest ger däremot inget avdrag.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Hässelby?",
  "price": [
    "Takets yta och lutning, om det gamla materialet innehåller asbest, hur mycket underlag som behöver bytas och vilket nytt material du väljer. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vårt hus i Hässelby är från 1968 – kan taket innehålla asbest?",
     "Det kan det. Arbetsmiljöverket säger att alla byggnader uppförda fram till 1982 ska antas kunna innehålla asbest, och bara en analys kan avgöra."),
    ("Får vi riva eternitplattorna på taket själva?",
     "Arbetsmiljöverkets krav gäller företag: rivning av asbesthaltigt material på tak eller fasad utomhus kräver tillstånd. Låt ett företag med tillstånd ta hand om det."),
    ("Vem ska beställa provtagningen?",
     "Arbetsmiljöverket lägger ansvaret för utredningen på byggherren, alltså dig som beställer takbytet. Vi hjälper dig att ta fram underlaget."),
    ("Ger asbestsaneringen rotavdrag?",
     "Ja, Skatteverket godkänner rotavdrag för sanering av asbest i samband med byggarbete, men inte för att mäta asbest."),
    ("Måste det nya taket se ut som det gamla?",
     "Ligger huset i en grupp med enhetliga tak är det klokt att välja ett material som liknar grannarnas, så att gruppens uttryck behålls."),
  ],
  "sources": [_VARSAM, _AV_FOR, _AV_TILL, _BV_ASB, _BV_FAS,
              ("Stockholms stad – Områdesfakta 2025: Hässelby villastad (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-villastad.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hässelby gård (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-gard.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hässelby-Vällingby stadsdelsområde (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-vallingby-stadsdelsomrade.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska taket på huset i Hässelby bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och om prov behöver tas innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Grupp av enplanshus i trä med grå tak bland granar",
     "group of 1960s Swedish detached single storey houses with low-pitched roofs covered in old grey corrugated fibre cement sheets, wooden facades, lawns and pine trees, western Stockholm suburb, overcast daylight" + _IMG_END),
    ("Takfot med ny läkt, hängränna och staplade betongpannor",
     "residential roof work site cordoned off with red and white barrier tape, old grey roof sheets wrapped in thick plastic on a pallet next to scaffolding, wooden house in background, daylight" + _IMG_END),
    ("Trähus med nylagt tak av mörka takpannor",
     "1960s Swedish single storey house with brand new dark grey concrete roof tiles and new black gutters, wooden facade, garden, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"takbyte-spanga.html": {
  "kind": "district", "service": "takbyte", "ort": "Spånga", "svc_label": "Takbyte",
  "title": "Takbyte i Spånga – solceller, radarn och Solhem",
  "description": "Takbyte i Spånga: solceller när taket läggs om, bygglov på grund av väderradarn i Håtuna, integrerade paneler och Solhem som värdefull miljö.",
  "h1": "Takbyte i Spånga",
  "lead": "Många som byter tak i Spånga vill samtidigt sätta upp solceller. I stora delar av Stockholm krävs då bygglov, och i Solhem kan även taket i sig behöva prövas. Geal Entreprenad AB byter tak på villor och radhus i Spånga och planerar taket så att solcellerna kan komma upp när lovet är klart.",
  "card": "Solceller, radarn och Solhem.",
  "sections": [
    {"id": "solceller-spanga", "anchor": "Solcellerna",
     "h2": "Solceller kräver ofta bygglov i Stockholm",
     "paras": [
       "Stockholms stad skriver att du behöver bygglov för solceller på en byggnad inom eller i anslutning till Försvarsmaktens riksintresse i ett område med detaljplan. Därför krävs lov för solceller i stora delar av staden, och en anledning är att området omfattas av riksintresset för väderradarn i Håtuna.",
       "Det betyder att ett takbyte och solceller ofta behöver planeras i två steg: taket kan läggas när det behövs, och solcellerna monteras när bygglovet är klart. Anmälan krävs däremot bara om anläggningen väsentligt påverkar byggnadens bärande delar eller brandskydd, enligt staden.",
     ],
     "aside": {"title": "Solceller i Stockholm", "items": [
       "Bygglov inom detaljplan nära Försvarsmaktens riksintresse", "Utökad lovplikt i värdefulla miljöer", "Anmälan bara vid väsentlig påverkan på bärande delar eller brandskydd"]}},
    {"id": "integrerat-spanga", "h2": "Integrerade paneler eller paneler ovanpå",
     "paras": [
       "Boverket förklarar att byte till takintegrerade solceller eller solfångare kan räknas som byte av taktäckningsmaterial, alltså som fasadändring. Paneler som monteras ovanpå ett vanligt tak är en solenergianläggning på byggnaden.",
       "För dig betyder skillnaden mest vid valet: ska taket och solcellerna vara ett och samma ytskikt, eller ska ett vanligt tak läggas med fästen som panelerna kan monteras i senare? Vi förbereder taket för den lösning du väljer, med rätt infästningar och genomföringar för kablar, så att tätskiktet inte behöver brytas upp efteråt.",
     ],
     "aside": None},
    {"id": "solhem-spanga", "h2": "Solhem och de andra villastäderna",
     "paras": [
       "Stadens strategi för småhusområden räknar Solhem, Bromsten, Flysta och Sundby till villastäderna, och i strategins tabell är Solhem markerat som kulturhistoriskt värdefull miljö. I Solhem fanns från början stora tomter där bara en tiondel av tomten fick bebyggas.",
       "Bromsten, Flysta och Sundby saknar den markeringen i tabellen, men enskilda hus kan ändå vara klassificerade. Stockholms stad påpekar att utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla byggnader och områden. Ligger huset där kan alltså både ett nytt takmaterial och solcellerna kräva lov. Stadsmuseets klassificeringskarta ger en första indikation. Om husen och taken i villastäderna kan du läsa under " + _L.format("takrenovering-spanga.html", "takrenovering i Spånga") + ".",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Solhem: 1 946", "Bromsten: 916", "Flysta: 657", "Sundby: 525"]}},
    {"id": "solkartan-spanga", "h2": "Solkartan och takets riktning",
     "paras": [
       "Staden hänvisar till Stockholms solkarta, där du kan uppskatta hur mycket energi solceller eller solfångare kan ge på din fastighet, och till stadens energi- och klimatrådgivning. Det är ett bra första steg innan du bestämmer om panelerna ska upp på ett visst takfall.",
       "Vid platsbesöket går vi igenom takfallens riktning, skuggor från träd och grannhus och var genomföringar och växelriktare kan placeras. Om tjänsten i stort kan du läsa under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
    {"id": "lasten-spanga", "h2": "Taket ska bära panelerna",
     "paras": [
       "Ett fält med solpaneler ger extra last på takstolarna, och infästningarna ska gå i underlaget. Därför ser vi på takstolar, råspont och läkt när det gamla taket är av, och byter skadat trä innan det nya läggs.",
       "Panelerna ska också kunna nås för service, och snö och vatten ska kunna rinna av runt fälten utan att samlas vid infästningarna. Därför planerar vi fältens placering tillsammans med takets plåtdetaljer och hängrännor.",
       "Om du inte vill sätta upp solceller nu kan vi ändå lägga taket så att de går att montera senare. Om stadsdelens hus och vanliga takproblem kan du läsa under " + _L.format("taklaggare-spanga.html", "takläggare i Spånga") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Spånga till",
  "steps": [
    ("Platsbesök", "Taket, takfallen och önskemål om solceller går vi igenom."),
    ("Kartan", "Stadsmuseets karta och detaljplanen kontrolleras."),
    ("Skriftligt kostnadsförslag", "Tak, underlag, plåt och förberedelser för solceller står var för sig."),
    ("Bygglov", "Ansökan för solcellerna, och för nytt takmaterial när det behövs."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs med fästen."),
    ("Genomgång", "Vi går igenom taket och förberedelserna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Spånga",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor, plåttak och hängrännor på ett småhus som rotarbete. För solceller finns också skattereduktion för grön teknik, och Skatteverket påpekar att rotavdrag och grön teknik inte kan ges för samma arbete.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Spånga?",
  "price": [
    "Takets yta och lutning, materialet, hur mycket underlag som behöver bytas och om taket ska förberedas för solceller. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för solceller på villan i Spånga?",
     "Troligen. Stockholms stad kräver bygglov för solceller inom eller i anslutning till Försvarsmaktens riksintresse i detaljplanerat område, och det gäller stora delar av staden på grund av väderradarn i Håtuna."),
    ("Kan vi byta tak nu och sätta upp solceller senare?",
     "Ja. Taket kan läggas med fästen och genomföringar förberedda, så att panelerna monteras när bygglovet är klart."),
    ("Räknas solcellstak som nytt takmaterial?",
     "Ja, enligt Boverket kan takintegrerade solceller räknas som byte av taktäckningsmaterial."),
    ("Hur vet vi om vårt takfall passar för solceller?",
     "Stockholms solkarta ger en uppskattning av hur mycket energi solceller kan ge på din fastighet. Vid platsbesöket ser vi också på skuggor och takfallens riktning."),
    ("Är Solhem kulturhistoriskt värdefullt?",
     "Ja, Solhem är markerat som kulturhistoriskt värdefull miljö i stadens strategi för småhusområden. Kontrollera din fastighet i Stadsmuseets karta."),
  ],
  "sources": [_STH_SOL, _STH_FAS, _BV_FAS, _VARSAM, _STH_KL,
              ("Stockholms stad – Områdesfakta 2025: Solhem (pdf)", _OF + "vasterort/jarva/solhem.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Bromsten (pdf)", _OF + "vasterort/jarva/bromsten.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Flysta (pdf)", _OF + "vasterort/jarva/flysta.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Sundby (pdf)", _OF + "vasterort/jarva/sundby.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska villan i Spånga få nytt tak och kanske solceller?", "Boka ett gratis platsbesök, så går vi igenom taket och reglerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa i trä med nytt tak och solpaneler på det södra takfallet",
     "Swedish 1920s wooden villa with a new dark roof and a neat array of black solar panels on the south-facing roof slope, garden with fruit trees, suburban Stockholm, sunny day" + _IMG_END),
    ("Takkrokar och skenor som bär solpaneler på ett tak med mörka pannor",
     "close view of aluminium mounting rails and roof hooks installed on a freshly laid dark roof, ready for solar panels, sealed cable entry, daylight" + _IMG_END),
    ("Villagata med äldre trävillor och stora trädgårdar",
     "quiet winding residential street with early 20th century Swedish wooden villas on large garden plots with mature trees and hedges, western Stockholm, summer" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"takbyte-vallingby.html": {
  "kind": "district", "service": "takbyte", "ort": "Vällingby", "svc_label": "Takbyte",
  "title": "Takbyte i Vällingby – Kälvesta och husgrupperna",
  "description": "Takbyte i Vällingby: småhusen i Kälvesta och Nälsta, Atlantis och Omega, riksintresset Vällingby–Råcksta och taket som en del av husgruppen.",
  "h1": "Takbyte i Vällingby",
  "lead": "Runt Vällingby ligger stora områden med radhus, kedjehus och villor som byggdes i grupp, och där är takets form och material en del av hela gruppens uttryck. Geal Entreprenad AB byter tak på småhus i Kälvesta, Vinsta, Råcksta och resten av Vällingby och utgår från grannhusen.",
  "card": "Kälvesta och husgrupperna.",
  "sections": [
    {"id": "kalvesta-vallingby", "anchor": "Kälvesta",
     "h2": "Kälvesta – en stadsdel av småhus",
     "paras": [
       "Stadens strategi för småhusområden beskriver hur andelen småhus ökade i början av 1970-talet, efter kritik mot storskalig bebyggelse, och att stora enheter med enbart småhus då bildade egna stadsdelar, som Kälvesta. Planmönstret är rationellt med tydliga grupper av hus och få matargator.",
       "Strategin lyfter fram att den liggande träpanelen och sadeltaken ger Kälvesta en egen identitet. Enligt stadens områdesfakta för 2025 finns 1 492 småhus med äganderätt i Kälvesta, och nästan inga i annan ägarform.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Kälvesta: 1 492", "Nälsta: 1 297", "Vinsta: 826", "Råcksta: 299", "Vällingby: 220"]}},
    {"id": "gruppen-vallingby", "h2": "Taket som en del av gruppen",
     "paras": [
       "För de gruppbyggda småhusen skriver strategin att områdets karaktär och värde till stor del ligger i den enhetliga gestaltningen, och att möjligheterna att förändra därför ofta är begränsade. Bland det som bedöms ha stor påverkan nämns takens form och material, färgsättning, byggnadsdelar och detaljer.",
       "Strategin ger också rådet att ta tillvara eller återskapa karaktärsskapande material och kulörer vid renoveringar. Vid ett takbyte i en husgrupp börjar vi därför med grannarnas tak: material, kulör, takfot och nock. Lägger vi samma material igen är det underhåll, och då behålls gruppens uttryck.",
     ],
     "aside": {"title": "Stor påverkan enligt strategin", "items": [
       "Takens form", "Material och färgsättning", "Byggnadsdelar och detaljer"]}},
    {"id": "riksintresset-vallingby", "h2": "Vällingby, Råcksta och riksintresset",
     "paras": [
       "Vällingby invigdes 1954 som den första tunnelbanestaden, och Råcksta och Hässelby gård planerades samtidigt. Strategin beskriver flera mycket väl gestaltade radhus- och villaområden i Vällingby, till exempel de kulturhistoriskt synnerligen värdefulla Atlantis i nordost och Omega i nordväst. Vällingby–Råcksta är riksintresse för kulturmiljövården.",
       "Inom ett riksintresse, som visas med blå ring i Stadsmuseets karta, behöver du bygglov för åtgärder som annars är lovfria, skriver Stockholms stad. Ett takbyte till ett annat material kan alltså kräva lov där, medan samma material och utförande räknas som underhåll enligt Boverket.",
     ],
     "aside": None},
    {"id": "detaljer-vallingby", "h2": "Låga tak och små tomter",
     "paras": [
       "I de gruppbyggda småhusområdena från 1960- och 70-talen, där strategin räknar in Kälvesta, var taken ofta platta eller svagt lutande pulpettak, men det förekommer också sadeltak. Husen står på små tomter, ofta tätt intill varandra, och nivåskillnader tas ofta upp med en souterrängvåning.",
       "Det påverkar arbetet: ställning och materialupplag behöver planeras på liten yta, och anslutningarna mot grannens tak eller förråd måste göras tätt. Om stadsdelens tak och vanliga problem kan du läsa under " + _L.format("taklaggare-vallingby.html", "takläggare i Vällingby") + ".",
     ],
     "aside": None},
    {"id": "nalsta-vallingby", "h2": "Nälsta och de friliggande villorna",
     "paras": [
       "Alla småhus i stadsdelsområdet är inte gruppbyggda. Nälsta räknas i stadens strategi till villastäderna, där bebyggelsen var privat organiserad och därför blev brokigare än i de planerade husgrupperna. Där står individuellt utformade hus från olika epoker sida vid sida, och taken varierar från hus till hus.",
       "I en villastad bedömer vi därför varje tak för sig: vad som ligger där i dag, vad huset hade från början och hur det nya taket passar husets ålder och stil. Strategin ger samma råd för villastäderna som för husgrupperna, att ta tillvara karaktärsskapande material och detaljer vid renoveringar.",
     ],
     "aside": None},
    {"id": "underlaget-vallingby", "h2": "Under det gamla taket",
     "paras": [
       "När det gamla taket är av ser vi underlagstäckning, läkt och råspont. Skadat trä byts, och plåt vid takfot, vindskivor och genomföringar görs om i samma arbete.",
       "Ska flera hus i gruppen byta tak kan ställning och leveranser samordnas. Om tjänsten i stort kan du läsa under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Vällingby till",
  "steps": [
    ("Platsbesök", "Taket och grannhusens tak går vi igenom på plats."),
    ("Kartan", "Stadsmuseets karta och detaljplanen kontrolleras."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt och plåt står var för sig."),
    ("Material och kulör", "Vi väljer material och kulör som stämmer med husgruppen."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Genomgång", "Vi går igenom taket och anslutningarna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Vällingby",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor, plåttak och hängrännor på ett småhus som rotarbete. Är radhuset en bostadsrätt ger arbete på gemensamma ytor som tak inget avdrag.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Vällingby?",
  "price": [
    "Takets yta och lutning, materialet, hur mycket underlag som behöver bytas, åtkomsten på en liten tomt och om flera hus byts samtidigt. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi byta till ett annat takmaterial i Kälvesta?",
     "Normalt krävs inget bygglov för en villa, men stadens strategi råder att material och kulör i husgrupperna tas tillvara. Kontrollera också detaljplanen och Stadsmuseets karta."),
    ("Krävs bygglov för nytt tak i Atlantis?",
     "Atlantis pekas ut som kulturhistoriskt synnerligen värdefullt i stadens strategi. Ligger huset inom riksintresset Vällingby–Råcksta eller är det blått eller grönt i Stadsmuseets karta krävs bygglov för fasadändringar som annars är lovfria. Byte till samma material och utförande räknas som underhåll."),
    ("Vad gör vi om grannen har ett annat tak än vi?",
     "Vi utgår från det som är ursprungligt för gruppen och väljer material och kulör därefter, och gör anslutningen mot grannens tak tät."),
    ("Gäller samma sak för en villa i Nälsta?",
     "Nälsta räknas till villastäderna, där husen är individuellt utformade. Där bedöms varje tak för sig utifrån husets ålder och stil."),
    ("Hur många småhus finns i Kälvesta?",
     "Enligt stadens områdesfakta för 2025 finns 1 492 småhus med äganderätt i Kälvesta."),
  ],
  "sources": [_VARSAM, _STH_KL, _STH_FAS, _BV_FAS,
              ("Stockholms stad – Områdesfakta 2025: Kälvesta (pdf)", _OF + "vasterort/hasselby-vallingby/kalvesta.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Nälsta (pdf)", _OF + "vasterort/hasselby-vallingby/nalsta.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Vinsta (pdf)", _OF + "vasterort/hasselby-vallingby/vinsta.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Råcksta (pdf)", _OF + "vasterort/hasselby-vallingby/racksta.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Vällingby (pdf)", _OF + "vasterort/hasselby-vallingby/vallingby.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska taket på huset i Vällingby bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och husgruppen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Länga av småhus med liggande träpanel och sadeltak",
     "group of 1970s Swedish linked houses with horizontal wooden panel facades and gable roofs of dark concrete tiles, small front gardens, footpath, western Stockholm suburb, summer" + _IMG_END),
    ("Rad av likadana sadeltak i ett småhusområde",
     "elevated view of a row of identical low single storey Swedish 1970s group-built houses with simple gable roofs of dark concrete tiles, horizontal wooden panel, no dormers, no chimney pots, small gardens and trees between, daylight" + _IMG_END),
    ("Gavel med vindskiva, takfotsplåt och hängränna på ett trähus",
     "close view of the gable end and eaves of a 1970s wooden linked house with new painted bargeboard, new metal edge flashing and new roof tiles, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"takbyte-alvsjo.html": {
  "kind": "district", "service": "takbyte", "ort": "Älvsjö", "svc_label": "Takbyte",
  "title": "Takbyte i Älvsjö – vinden, kupan och byggrätten",
  "description": "Takbyte i Älvsjö: branta tegeltak med kupa, takkupor som fasadändring, anmälan vid ingrepp i stommen och äldre planer med generösa byggrätter.",
  "h1": "Takbyte i Älvsjö",
  "lead": "När taket på en villa i Älvsjö ändå ska av är det ett tillfälle att samtidigt göra något åt vinden: en ny kupa, mer isolering eller en inredd vind. Geal Entreprenad AB byter tak på villor i Älvsjö, Långbro, Herrängen och Långsjö och planerar takbytet och vinden i samma projekt.",
  "card": "Vinden, kupan och byggrätten.",
  "sections": [
    {"id": "villastaden-alvsjo", "anchor": "Villastaden",
     "h2": "Branta tak med kupa",
     "paras": [
       "Stadsmuseets inventering av Älvsjö villastad beskriver två vanliga hustyper från villastadens första år. Den ena har vit slätputsad bottenvåning, gavelspetsar med mörkbrun panel och brant sadeltak täckt med rött tegel. Den andra har falurödfärgad träpanel, vita snickerier och ett brant tegeltäckt sadeltak med kupa.",
       "Stadsplanen för Älvsjö villastad togs fram av Per Olof Hallman, enligt stadens strategi för småhusområden. Ett brant tak med kupa ger stor vindsvolym, och därför har många hus fått inredd vind genom åren.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Långbro: 1 377", "Herrängen: 1 114", "Långsjö: 839", "Älvsjö: 191"]}},
    {"id": "byggratten-alvsjo", "h2": "Äldre planer med generösa byggrätter",
     "paras": [
       "Strategin skriver att äldre stadsplaner med generösa byggrätter finns bland annat i Älvsjö, Herrängen, Långsjö och Långbro. I tabellen är delar av Älvsjö markerade både som kulturhistoriskt värdefull miljö och med generösa byggrätter, medan Långsjö och delar av Herrängen och Långbro har generösa byggrätter utan den markeringen.",
       "En generös byggrätt säger hur mycket du får bygga, men inte hur. Strategin betonar att områden som Herrängen, Långsjö och Långbro kan se brokiga ut men har gemensamma drag, och att byggnadernas anpassning till terrängen och gaturummet har stor betydelse vid förändringar. Vi börjar därför med detaljplanen innan kupan ritas.",
     ],
     "aside": None},
    {"id": "kupan-alvsjo", "h2": "En ny kupa är en fasadändring",
     "paras": [
       "Stockholms stad räknar mindre takkupor till fasadändringarna, tillsammans med till exempel byte av material på taket. På ett en- eller tvåbostadshus krävs inte längre bygglov för fasadändringar om vissa förutsättningar är uppfyllda, men utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla byggnader och områden. Fasadändringar som inte kräver lov ska ändå stämma med detaljplanen.",
       "Stadsmuseets klassificeringskarta ger en första indikation på om din fastighet berörs. En kupa som tar upp en del av takfallet kräver dessutom att takstolarna byggs om runt öppningen, och det är en ändring i bärande konstruktion.",
     ],
     "aside": {"title": "Kupa i samband med takbyte", "items": [
       "Detaljplanen först", "Stadsmuseets karta", "Konstruktör för stommen", "Anmälan och startbesked"]}},
    {"id": "stommen-alvsjo", "h2": "Ingrepp i stommen kräver anmälan",
     "paras": [
       "Stockholms stad skriver att ändringar som påverkar byggnadens bärande konstruktion kräver anmälan och startbesked, att ritningar kan vara ofullständiga och att du ska kontakta en konstruktör om du är osäker. Det gäller när takstolar kapas för en kupa eller när bjälklaget förstärks för att vinden ska bli bostad.",
       "Därför planerar vi takbytet och vinden tillsammans. Med startbeskedet klart kan det gamla taket rivas, stommen byggas om och det nya taket läggas i ett svep, utan att huset står öppet längre än nödvändigt. Om villastadens tak i övrigt kan du läsa under " + _L.format("takrenovering-alvsjo.html", "takrenovering i Älvsjö") + ".",
     ],
     "aside": None},
    {"id": "isoleringen-alvsjo", "h2": "Isolering och ventilation på vinden",
     "paras": [
       "När vinden inreds eller isoleras om ändras luftflödet under taket. Ventilationen mellan isolering och yttertak behöver fungera, och anslutningarna vid takfot och kupa ska vara täta mot både regn och fukt inifrån.",
       "Vi tar det i samma arbete som det nya taket. Om tjänsten i stort kan du läsa under " + _L.format("takbyte.html", "takbyte") + " och om stadsdelens tak under " + _L.format("taklaggare-alvsjo.html", "takläggare i Älvsjö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Älvsjö till",
  "steps": [
    ("Platsbesök", "Taket, vinden och önskemål om kupa går vi igenom."),
    ("Detaljplan och karta", "Byggrätt, detaljplan och Stadsmuseets karta kontrolleras."),
    ("Skriftligt kostnadsförslag", "Takbyte, kupa och vind står var för sig."),
    ("Anmälan och lov", "Anmälan vid ingrepp i stommen och bygglov när det krävs."),
    ("Takbyte och stomme", "Gammalt tak rivs, stommen byggs om och nytt tak läggs."),
    ("Genomgång", "Vi går igenom taket, kupan och dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Älvsjö",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor, plåttak och hängrännor på ett småhus som rotarbete, och även tilläggsisolering. Rotavdrag ges däremot inte för att bygga en helt ny bostad.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Älvsjö?",
  "price": [
    "Takets yta och lutning, materialet, om en kupa ska byggas, hur mycket av stommen som ändras och om vinden ska isoleras eller inredas. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi bygga en kupa samtidigt som taket byts i Älvsjö?",
     "Ja. En mindre takkupa räknas som fasadändring, och kapas takstolarna krävs anmälan och startbesked. Detaljplanen och Stadsmuseets karta avgör om bygglov också behövs."),
    ("Vad betyder generös byggrätt för vårt hus i Långsjö?",
     "Att den äldre planen tillåter mycket byggnad på tomten. Den säger hur mycket du får bygga, men stadens strategi betonar att förändringar ska ta hänsyn till områdets gemensamma drag."),
    ("Måste en konstruktör vara med när takstolarna ändras?",
     "Stockholms stad råder dig att anlita en konstruktör om du är osäker, och ingrepp i bärande konstruktion kräver anmälan och startbesked."),
    ("Är Älvsjö villastad kulturhistoriskt värdefull?",
     "Delar av Älvsjö är markerade som kulturhistoriskt värdefull miljö i stadens strategi för småhusområden. Kontrollera din fastighet i Stadsmuseets karta."),
  ],
  "sources": [_ALV_INV, _VARSAM, _STH_FAS, _STH_KL, _STH_BAR,
              ("Stockholms stad – Områdesfakta 2025: Långbro (pdf)", _OF + "soderort/hagersten/langbro.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Herrängen (pdf)", _OF + "soderort/hagersten/herrangen.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Långsjö (pdf)", _OF + "soderort/hagersten/langsjo.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Älvsjö (pdf)", _OF + "soderort/hagersten/alvsjo.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska taket på villan i Älvsjö bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och vinden innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Faluröd trävilla med brant tegeltak och vita snickerier",
     "1910s Swedish wooden villa painted falu red with white trim, steep red clay tile gable roof with a small dormer, garden with fruit trees and hedge, southern Stockholm, summer" + _IMG_END),
    ("Takläkt och nya röda takpannor på ett brant tak under omläggning",
     "roof of an old Swedish villa during re-roofing with clay tiles removed, a new timber dormer frame being built into the roof slope, new underlay membrane, scaffolding, daylight" + _IMG_END),
    ("Vind med ny isolering och synliga takstolar",
     "attic of an old house during renovation with exposed rafters, new mineral wool insulation between them and a ventilation gap toward the roof, construction light" + _IMG_END),
  ],
},
}
