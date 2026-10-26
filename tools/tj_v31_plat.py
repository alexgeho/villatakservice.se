# -*- coding: utf-8 -*-
"""Plåtslagare – ortsidor v31: Kista, Skärholmen, Österåker (2026-10-27).
Hubb: platslagare.html (TJ_HUB["platslagare"]). Intent: plåttak, hängrännor, stuprör och beslag. Tre bilder per sida:
img[0] hero 4:3, img[1] och img[2] 3:2.

Lokal vinkel per sida:
Kista – Stockholms spår (Kista utbyggt 1975–1980, omkring 780 småhus), områdesfakta 2025 för Kista och Akalla (många
  småhus är bostadsrätter), Varsam om de storskaliga stadsdelarnas småhus (platta tak eller pulpettak, Akalla nämns),
  Boverket om att byta taktäckningsmaterial utan bygglov, Skatteverkets regel att plåttak, hängrännor och stuprör
  inte ger rotavdrag i bostadsrätt, bostadsrättslagen 7 kap. 12 §.
Skärholmen – Varsam om gruppbyggda småhus (souterrängvåning, små tomter, enhetlig färgsättning, platta tak och
  pulpettak), områdesfakta 2025 (småhus med äganderätt), Stockholm Vatten och Avfall om backventiler och egna
  dagvattenanslutningar.
Österåker – Råd och vägledning för byggande i Svinninge 2008 (Svinningeudd och Nantes kommunens äldsta och bäst
  bevarade sommarhusbebyggelse, plåt för fönsterbleck och stuprör, rött lertegel eller ståndfalsad plåt, slätplåt
  eller papp på nya byggnader), kommunens sida om att bygglov krävs i särskilt värdefulla områden även för underhåll.

Fakta endast från källorna i respektive 'sources', öppnade med curl (webbläsar-UA) 2026-10-27, alla svarade 200; pdf:erna
har textlager. Skatteverket 2026-10-27: småhus – reparera, rengöra eller byta ut plåttak, hängrännor och stuprör,
byggnadsställning i samband med rotarbete, rengöra tak och hängrännor; bostadsrätt – inget avdrag för plåttak,
hängrännor och stuprör eller arbete på gemensamma ytor som tak och fasader.
Strukna / ej använda: vilka tak enskilda hus i orterna har, att Kista finns i Varsam-tabellen, plåtpriser, livslängder.
Inga garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_BV_TAK = ("Boverket – Ändra fasad eller tak",
           "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/andra-fasad-eller-tak/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 12 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SPAR_KISTA = ("Stockholms stadsmuseum – Stockholms spår: Kista (pdf)",
               "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000080.pdf")
_SVOA_BACK = ("Stockholm Vatten och Avfall – Backventiler",
              "https://www.svoa.se/artiklar-listsida/oversvamning---hantera-och-forebygg/backventiler/")
_OST_SVIN = ("Österåkers kommun – Råd och vägledning för byggande i Svinninge (pdf)",
             "https://www.osteraker.se/download/18.5bb0400617c11d33b5536/1632390824156/rad_och_vagledning_svinninge.pdf")
_OST_KULT = ("Österåkers kommun – Kulturhistoriska byggnader, kulturmiljöer",
             "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/bygglovsguiden/kulturhistoriskabyggnaderkulturmiljoer.4.367d658917909e8fc2bb42.html")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Plåt och annat "
            "material ger inget avdrag, och Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ KISTA
"platslagare-kista.html": {
  "kind": "district", "service": "platslagare", "ort": "Kista", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Kista – tak och rännor på 1970-talshusen",
  "description": "Plåtslagare i Kista: hängrännor, stuprör och plåtdetaljer på radhus från 1975–1980, föreningens ansvar, byte av takmaterial och rotavdrag.",
  "h1": "Plåtslagare i Kista",
  "lead": "Småhusen i Kista och Akalla byggdes för snart femtio år sedan, och hängrännor, stuprör och beslag från den tiden behöver ofta ses över. Geal Entreprenad AB utför plåtarbeten på radhus, kedjehus och villor i Kista och tar fram underlag när en förening ska besluta för en hel husgrupp.",
  "card": "Rännor, stuprör och beslag.",
  "sections": [
    {"id": "aldern-kista", "anchor": "Husen",
     "h2": "Hus från 1975–1980",
     "paras": [
       "Stadsmuseets Stockholms spår om Kista berättar att staden köpte marken på Järvafältet 1966 och byggde ut Kista åren 1975–1980. Bebyggelsen beskrivs som 2 500 lägenheter i flerbostadshus och omkring 780 småhus. Stadsdelen fick friare arkitektoniska former än de andra stadsdelarna på Järvafältet. Är rännor och beslag original har de alltså suttit uppe i runt femtio år.",
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver småhusen i de storskaliga stadsdelarna som radhus och kedjehus, i Akalla också villor och atriumhus, och skriver att taken ofta var platta eller svagt lutande pulpettak. På sådana tak har takfotsplåt, vattenavrinning och anslutningar mot väggar stor betydelse, och det är där vi börjar vår genomgång.",
     ],
     "aside": {"title": "Kista enligt Stockholms spår", "items": [
       "Utbyggd 1975–1980", "Omkring 780 småhus", "2 500 lägenheter", "Friare arkitektur än grannarna"]}},
    {"id": "forening-kista", "h2": "Ditt ansvar eller föreningens",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 971 småhus i Kista, varav 404 bostadsrätter, och 671 i Akalla, varav 493 bostadsrätter. I ett bostadsrättsradhus säger bostadsrättslagen att medlemmen håller lägenheten i gott skick om inte stadgarna bestämmer något annat. Om tak, rännor och stuprör är ditt eller föreningens ansvar varierar därför mellan föreningar.",
       "Ansvarar föreningen tar vi fram ett underlag för hela husgruppen: vad som behöver bytas nu, vad som kan vänta och hur arbetet kan delas upp. Ansvarar du själv tittar vi bara på ditt hus, men stämmer av färg och profil mot grannarna så att längan ser enhetlig ut.",
     ],
     "aside": {"title": "Bostadsrätter bland småhusen 2025", "items": [
       "Kista: 404 av 971", "Akalla: 493 av 671", "Stadgarna avgör ansvaret", "Underlag till styrelsen"]}},
    {"id": "byta-kista", "h2": "Byta takmaterial utan bygglov",
     "paras": [
       "Boverket skriver att du inte behöver bygglov för att byta taktäckningsmaterial på ett småhus, även om det nya taket ser annorlunda ut eller är av ett annat material. Innan du byter måste du kontrollera att taket klarar den nya belastningen, och ändringen ska göras varsamt och anpassas till omgivningen. Bygglov kan ändå krävas om detaljplanen har bestämmelser om utökad lovplikt. Boverket påpekar också att bestämmelser om minskad lovplikt i detaljplaner upphör att gälla den 1 december 2027, och att de åtgärderna då kräver bygglov.",
       "I en husgrupp där alla tak är lika är anpassningen en fråga om att välja samma kulör och profil som grannarna. Vill föreningen byta material på alla tak samtidigt tar vi fram ett förslag med konstruktörens kontroll av lasterna. Mer om tak finns under " + _L.format("takbyte-kista.html", "takbyte i Kista") + ".",
     ],
     "aside": None},
    {"id": "rannor-kista", "h2": "Hängrännor, stuprör och beslag",
     "paras": [
       "En hängränna som lutar fel eller ett stuprör som lossnat leder vatten mot fasaden och grunden. Vi kontrollerar fall, skarvar och fästen, byter skadade delar och ser till att stuprören leder vattnet bort från huset. Fönsterbleck och takfotsplåt ses över i samma veva.",
       "Skatteverket räknar rengöring av tak och hängrännor som rotarbete i ett småhus, liksom att reparera eller byta plåttak, hängrännor och stuprör. Behövs en byggnadsställning ingår också montering och nedmontering av den i det avdragsgilla arbetet. Mer om tjänsten finns under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med plåt i Kista",
  "steps": [
    ("Platsbesök", "Gratis genomgång av rännor, stuprör och tak."),
    ("Ansvar", "Stadgarna visar om du eller föreningen beställer."),
    ("Förslag", "Kulör och profil som passar husgruppen."),
    ("Säkerhet", "Ställning eller skylift vid behov."),
    ("Montage", "Nya rännor, stuprör, bleck och beslag."),
    ("Kontroll", "Vi provar avrinningen och går igenom arbetet."),
  ],
  "rot_h2": "ROT-avdrag för plåtarbeten i Kista",
  "rot": [
    "Äger du huset ger Skatteverket rotavdrag för att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör och för att montera ställning i samband med arbetet. Är radhuset en bostadsrätt ger plåtarbeten på tak, rännor och stuprör inget avdrag, eftersom de inte görs inne i bostaden.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för plåtarbeten i Kista?",
  "price": [
    "Hur många meter ränna och stuprör som ska bytas, takets form och höjd, om ställning behövs, bleck och beslag och om flera hus i gruppen görs samtidigt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem betalar nya hängrännor på mitt bostadsrättsradhus i Kista?",
     "Det avgörs av föreningens stadgar. Bostadsrättslagen lägger underhållet på medlemmen bara om stadgarna inte säger något annat."),
    ("Får jag rotavdrag för nya stuprör på ett radhus med äganderätt i Akalla?",
     "Ja, Skatteverket godkänner reparation och byte av plåttak, hängrännor och stuprör i småhus."),
    ("Behöver jag bygglov för att byta till plåttak på mitt radhus i Kista?",
     "Normalt inte. Boverket skriver att byte av taktäckningsmaterial på småhus är lovfritt, om inte detaljplanen säger annat."),
    ("Vilka tak har småhusen i de storskaliga stadsdelarna?",
     "Stadens vägledning beskriver dem som oftast platta eller svagt lutande pulpettak, men det förekommer även sadeltak."),
  ],
  "sources": [_SPAR_KISTA, _of("Kista", "vasterort/jarva/kista"), _of("Akalla", "vasterort/jarva/akalla"), _VARSAM, _BV_TAK, _BRL, _SKV],
  "cta": ("Behöver rännorna ses över i Kista?", "Boka ett gratis platsbesök, så går vi igenom rännor, stuprör och tak innan du eller föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhuslänga med låglutande tak och plåtdetaljer",
     "row of late 1970s Swedish terraced houses with low-pitched mono-pitch roofs, dark sheet metal fascia and gutters, brown wooden facades, small front gardens, summer daylight" + _SFX),
    ("Ny hängränna och stuprör på ett radhus",
     "close view of a new dark grey steel gutter and downpipe on the corner of a brown wooden terraced house, neat brackets and joints, blue sky, daylight" + _SFX),
    ("Takfot med plåtbeslag på ett låglutande tak",
     "close view of the eave of a low-pitched roof with folded sheet metal edge flashing, a gutter below and wooden fascia, clean modern detailing, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"platslagare-skarholmen.html": {
  "kind": "district", "service": "platslagare", "ort": "Skärholmen", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Skärholmen – radhus med souterräng",
  "description": "Plåtslagare i Skärholmen: rännor och stuprör på radhus med souterräng i Sätra, Bredäng och Vårberg, dagvatten och backventil och rotavdrag.",
  "h1": "Plåtslagare i Skärholmen",
  "lead": "Radhusen i Sätra, Bredäng, Vårberg och Skärholmen är ofta byggda i sluttningar, med en souterrängvåning mot ena sidan. Där är det extra viktigt att regnvattnet från taket hamnar rätt. Geal Entreprenad AB byter hängrännor, stuprör och plåtbeslag på småhus i Skärholmens stadsdelsområde.",
  "card": "Rännor och stuprör i sluttningarna.",
  "sections": [
    {"id": "husgrupper-skarholmen", "anchor": "Husgrupperna",
     "h2": "Gruppbyggda småhus i sluttning",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver de gruppbyggda småhusen i de storskaliga stadsdelarna, där Bredäng, Sätra, Skärholmen och Vårberg ingår. Nivåskillnaderna tas ofta upp med en souterrängvåning, tomterna är små och husgrupperna har mycket enhetlig utformning. Taken är huvudsakligen platta eller pulpettak, men sadeltak med brant takfall förekommer också.",
       "Färgsättningen var enligt vägledningen noga komponerad och enhetlig inom husgrupperna. Det gäller också plåten: rännor, stuprör och vindskivebeslag i samma kulör håller ihop längan. Vi tar med en kulörkarta till platsbesöket och jämför med grannhusen innan något beställs. Vägledningen nämner också att mindre tillbyggnader, som inglasade uterum, är vanliga i områdena. Där taket på ett uterum möter husväggen behövs ett plåtbeslag som leder bort vattnet, och det kontrollerar vi samtidigt.",
     ],
     "aside": {"title": "Varsam om husgrupperna", "items": [
       "Souterrängvåning i sluttningar", "Små tomter", "Platta tak eller pulpettak", "Enhetlig färg i gruppen"]}},
    {"id": "agare-skarholmen", "h2": "Nästan alla äger sitt radhus",
     "paras": [
       "Stadens områdesfakta för 2025 visar att nästan alla småhus i stadsdelsområdet ägs med äganderätt: 577 i Vårberg, 543 i Skärholmen, 536 i Sätra och 320 i Bredäng. Det betyder att det oftast är du som husägare som beställer plåtarbetet och som får rotavdrag för det. Vägledningen påpekar att de små tomterna begränsar större förändringar av de enskilda husen, så arbetet handlar oftast om att byta och förbättra det som finns.",
       "När husen sitter ihop kan grannarna dela ränna eller stuprör vid gaveln. Då samordnar vi med grannen så att skarven blir tät och vattnet leds rätt. Vill flera grannar byta samtidigt kan vi göra hela längan i ett svep, och varje ägare får sitt eget kostnadsförslag.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Vårberg: 577", "Skärholmen: 543", "Sätra: 536", "Bredäng: 320"]}},
    {"id": "dagvatten-skarholmen", "h2": "Stuprör, dagvatten och backventil",
     "paras": [
       "Stockholm Vatten och Avfall skriver att en backventil installeras på servisledningen för att hindra avloppsvatten från gatan att tränga in i källaren genom golvbrunnar. Innan en backventil sätts in måste du säkerställa att du inte har några egna dagvattenanslutningar på samma ledning. Är ventilen stängd kan dagvattnet annars inte ta sig ut, utan blir kvar på fastigheten. Bolaget skriver också att en backventil kräver regelbunden tillsyn och skötsel, och att avloppsvattnet inte kan spolas ut från huset medan den är stängd.",
       "För ett hus med souterrängvåning betyder det att det spelar roll vart stuprören leder vattnet. Vi tar reda på om dina stuprör är anslutna till ledningen eller släpper ut vattnet på marken innan vi byter dem, och berättar vad det betyder om du funderar på en backventil.",
     ],
     "aside": None},
    {"id": "tak-skarholmen", "h2": "Platta tak och pulpettak",
     "paras": [
       "Ett platt eller svagt lutande tak avvattnas annorlunda än ett brant sadeltak, och plåtdetaljerna vid takfot och vindskivor är det som håller vattnet borta från väggen. Vi kontrollerar beslagen, byter skadad plåt och ser till att fallet i rännorna stämmer.",
       "Boverket skriver att du inte behöver bygglov för att byta taktäckningsmaterial på ett småhus, men att du ska kontrollera att taket klarar den nya belastningen och att ändringen ska anpassas till omgivningen. I Bredäng, som stadens vägledning markerar som kulturhistoriskt värdefull miljö, kontrollerar vi kartan först. Mer om tjänsten finns under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med plåt i Skärholmen",
  "steps": [
    ("Platsbesök", "Gratis genomgång av tak, rännor och stuprör."),
    ("Dagvatten", "Vart leder stuprören vattnet i dag?"),
    ("Kulör", "Samma färg som husgruppen."),
    ("Säkerhet", "Ställning mot den höga sidan vid behov."),
    ("Montage", "Rännor, stuprör, beslag och bleck."),
    ("Kontroll", "Vattenprov och genomgång med dig."),
  ],
  "rot_h2": "ROT-avdrag för plåtarbeten i Skärholmen",
  "rot": [
    "Skatteverket räknar det som rotarbete att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör på ett småhus du äger, och att montera och montera ner ställning i samband med arbetet. Är huset yngre än fem år får arbetet bara återställa det ursprungliga skicket.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för plåtarbeten i Skärholmen?",
  "price": [
    "Antal meter ränna och stuprör, husets höjd mot souterrängsidan, ställning, beslag och bleck, och om grannar i längan byter samtidigt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan mina stuprör påverka en backventil i ett radhus i Vårberg?",
     "Ja. Stockholm Vatten och Avfall skriver att det inte får finnas egna dagvattenanslutningar på den ledning där backventilen ska sitta."),
    ("Måste rännorna på mitt radhus i Sätra ha samma färg som grannarnas?",
     "Ändringen ska anpassas till omgivningen, och stadens vägledning beskriver enhetlig färgsättning inom husgrupperna."),
    ("Kan grannarna i längan i Bredäng byta hängrännor samtidigt?",
     "Ja, vi kan göra hela längan i ett svep. Varje ägare får sitt eget kostnadsförslag och sitt eget rotavdrag."),
    ("Vad är en souterrängvåning?",
     "En våning som delvis ligger under mark på ena sidan. Stadens vägledning skriver att nivåskillnader i husgrupperna ofta tas upp så."),
  ],
  "sources": [_VARSAM, _of("Skärholmen", "soderort/skarholmen/skarholmen"), _of("Sätra", "soderort/skarholmen/satra"),
              _of("Bredäng", "soderort/skarholmen/bredang"), _of("Vårberg", "soderort/skarholmen/varberg"), _SVOA_BACK, _BV_TAK, _SKV],
  "cta": ("Behöver rännorna bytas i Skärholmen?", "Boka ett gratis platsbesök, så går vi igenom tak, rännor och stuprör innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus i sluttning med souterrängvåning",
     "Scandinavian modernist 1960s terraced houses in a Stockholm suburb built on a slope, partly underground lower floor on the downhill side, light grey wood panels and yellow brick, low mono-pitch roofs with dark gutters and downpipes, no chimneys, lawn and birch trees, summer" + _SFX),
    ("Stuprör som leder ut vatten på marken",
     "close view of a dark grey sheet metal downpipe ending in a short outlet over a concrete splash block on gravel next to a brick wall, daylight" + _SFX),
    ("Plåtbeslag längs gaveln på ett plåttak",
     "close view of the gable end of a low-pitched roof with folded sheet metal barge flashing and a gutter at the eave, wooden facade below, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"platslagare-osteraker.html": {
  "kind": "district", "service": "platslagare", "ort": "Österåker", "svc_label": "Plåtslagare",
  "title": "Plåtslagare i Österåker – sommarvillorna i Svinninge",
  "description": "Plåtslagare i Österåker: plåt för fönsterbleck och stuprör i Svinninge, ståndfalsad plåt som takmaterial, bygglov i värdefulla miljöer och rotavdrag.",
  "h1": "Plåtslagare i Österåker",
  "lead": "På Svinningeudd och i Nantes finns Österåkers äldsta och bäst bevarade sommarhusbebyggelse, där plåt används till fönsterbleck och stuprör och ibland till hela taket. Geal Entreprenad AB utför plåtarbeten på villor och fritidshus i Österåker och utgår från kommunens råd när huset står i en värdefull miljö.",
  "card": "Plåtdetaljer på sommarvillorna.",
  "sections": [
    {"id": "svinninge-osteraker", "anchor": "Svinninge",
     "h2": "Kommunens äldsta sommarhusbebyggelse",
     "paras": [
       "Österåkers kommuns skrift Råd och vägledning för byggande i Svinninge från 2008 beskriver det strandnära området Svinningeudd och Nantes som kommunens äldsta och bäst bevarade sommarhusbebyggelse och en stor tillgång för kommunen. Både sommargäster och åretruntboende är delaktiga i att förvalta miljön.",
       "Skriften beskriver de äldre husen som enkla byggnadskroppar i ett eller två plan, där verandor och förstukvistar lagts till. Alla bostadshus har väl synliga sadeltak, ofta belagda med lertegel. Husens olika delar hålls ihop av enhetliga traditionella material: trä för fönster och fasad, tegel för skorstenen och plåt för fönsterbleck och stuprör. Fasaderna bör enligt riktlinjerna i huvudsak vara av trä, målat i ljusa kulörer med oljefärg eller Falu rödfärg.",
     ],
     "aside": {"title": "Svinninge enligt kommunens råd", "items": [
       "Råd och vägledning 2008", "Svinningeudd och Nantes", "Sadeltak, ofta lertegel", "Plåt för bleck och stuprör"]}},
    {"id": "takmaterial-osteraker", "h2": "Lertegel eller ståndfalsad plåt",
     "paras": [
       "Bland skriftens riktlinjer står att tak bör ha beläggning av rött lertegel eller ståndfalsad plåt, och att alternativa material prövas i bygglov. För nya byggnader rekommenderar skriften nytt lertegel, slätplåt eller papp. Skriften avråder från att ersätta lertegel med betongtakpannor, som är tjockare och tyngre och vars kulör bleks med åren.",
       "Skriften kallar taket husets femte fasad, som spelar stor roll för hur bebyggelsen upplevs. Den skriver också att ett tegeltak som inte håller tätt oftast beror på att underlagspappen spruckit eller att läkten är gammal och skadad, och att det inte finns någon anledning att byta allt tegel för att några delar är skadade. Ett plåttak med stående falsar passar alltså in i Svinninge. Vid ett byte från tegel till plåt eller tvärtom tar vi med kommunens riktlinjer i förslaget och kontrollerar om bygglov krävs. Mer om takbyten finns under " + _L.format("takbyte-osteraker.html", "takbyte i Österåker") + ".",
     ],
     "aside": {"title": "Takmaterial enligt riktlinjerna", "items": [
       "Rött lertegel", "Ståndfalsad plåt", "Nya hus: även slätplåt eller papp", "Inte betongpannor"]}},
    {"id": "lov-osteraker", "h2": "Bygglov även för underhåll",
     "paras": [
       "Österåkers kommun skriver att du behöver söka bygglov om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden är särskilt värdefull. Det gäller enligt kommunen till exempel om du vill ändra fasaden, bygga till, riva, underhålla eller sätta upp solpaneler. Kommunen påpekar att även små ändringar kan påverka en känslig byggnad.",
       "Österåkerskartan visar områden med kulturhistoriska värden, och kommunen ber dig kontakta bygglovenheten innan arbetet börjar. Vi tittar i kartan tillsammans med dig och tar fram ritningar och beskrivning om lov behövs för att byta plåt på taket eller ändra bleck och stuprör.",
     ],
     "aside": None},
    {"id": "detaljer-osteraker", "h2": "Bleck, stuprör och skorstensbeslag",
     "paras": [
       "Kommunens sida räknar bevarade byggnadsdetaljer som fönster och fasadmaterial till det som kan göra ett hus värdefullt. Ett fönsterbleck eller ett stuprör är en liten del av fasaden, men på ett hus där allt annat är ursprungligt syns ett avvikande beslag. Vi bockar bleck efter de gamla och väljer stuprör med samma dimension och kulör.",
       "Kring skorstenen och vid takfoten är plåten utsatt för väder. Vi lagar eller byter beslag där vatten tränger in och kontrollerar att rännorna har rätt fall. Mer om tjänsten finns under " + _L.format("platslagare.html", "plåtslagare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så arbetar vi med plåt i Österåker",
  "steps": [
    ("Platsbesök", "Gratis genomgång av tak, bleck och stuprör."),
    ("Kartan", "Vi ser om huset ligger i en värdefull miljö."),
    ("Förslag", "Material och kulör enligt kommunens råd."),
    ("Bygglov", "Ritningar och beskrivning när lov krävs."),
    ("Montage", "Bleck, rännor, stuprör och takplåt."),
    ("Kontroll", "Avrinning och anslutningar provas."),
  ],
  "rot_h2": "ROT-avdrag för plåtarbeten i Österåker",
  "rot": [
    "Skatteverket ger rotavdrag för att reparera, rengöra eller byta ut plåttak, hängrännor och stuprör på ett småhus du äger, och avdraget gäller även ett fritidshus du kan använda. Arbete med ställning i samband med arbetet ingår.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för plåtarbeten i Österåker?",
  "price": [
    "Takets storlek och lutning, om hela taket eller bara detaljer ska bytas, bockade bleck efter gamla förlagor, bygglovsritningar, ställning, hur lätt det är att komma fram till huset och resväg ut på öar. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag ha plåttak på min sommarvilla i Svinninge?",
     "Kommunens riktlinjer anger rött lertegel eller ståndfalsad plåt. Andra material prövas i bygglov."),
    ("Kräver underhåll av plåten bygglov i Österåker?",
     "I ett kulturhistoriskt särskilt värdefullt område kan det göra det. Kommunen nämner underhåll bland åtgärderna som kräver lov där."),
    ("Varför avråder kommunen från betongpannor i Svinninge?",
     "Skriften beskriver dem som tjockare och tyngre än lertegel och skriver att kulören bleks med åren."),
    ("Får jag rotavdrag för nya stuprör på mitt fritidshus i Österåker?",
     "Ja, om du äger huset och kan använda det. Skatteverket godkänner byte av hängrännor och stuprör på småhus."),
  ],
  "sources": [_OST_SVIN, _OST_KULT, _SKV,
              ("Skatteverket – Så fungerar rotavdraget",
               "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")],
  "cta": ("Behöver plåten ses över i Österåker?", "Boka ett gratis platsbesök, så går vi igenom tak och plåtdetaljer innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sommarvilla med sadeltak och veranda vid vattnet",
     "early 1900s Swedish wooden summer villa painted light yellow with white trims, a glazed veranda, a steep red clay tile roof with a brick chimney, set on a rocky plot near the water among pine trees, summer" + _SFX),
    ("Ståndfalsat plåttak på ett trähus",
     "close view of a dark grey standing seam metal roof on an old wooden house, straight vertical seams, eave with gutter, pine trees in the background, daylight" + _SFX),
    ("Fönsterbleck och stuprör mot en träfasad",
     "close view of a white painted wooden window with a dark sheet metal sill and a round downpipe beside it on a light yellow wooden panel facade, daylight" + _SFX),
  ],
},
}
