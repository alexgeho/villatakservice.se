# -*- coding: utf-8 -*-
"""Fasadmålning – ortsidor v28: Botkyrka, Spånga, Älvsjö, Österåker, Östermalm, Kista (2026-10-27).
Deltjänst under malare.html (TJ_HUB["fasadmalning"]). Intent: måla om fasaden utvändigt – färgtyp, kulör, förarbete
och lov. Skild från ortens malare-<ort>.html och fasadrenovering-<ort>.html och från v15/v17/v20/v24-sidorna.

Lokal vinkel per sida:
Botkyrka – Tullinges villaområde 1900–1940 (kulturmiljöprogrammet: nationalromantik, kataloghus från 1920-talet,
  1930–40-talets slätputs och stående locklistpanel, folkhemmets puts och tegel; riktlinjen om tidstypisk utformning),
  Botkyrkas sida om fasadändring (kulörbyte, t.ex. röd till vit, webbkartans lager), RAÄ om samma färgtyp.
Spånga – villastäderna Bromsten, Flysta och Sundby (Varsam: trä dominerande, glasverandor, snickarglädje; municipal-
  samhället Spånga), RAÄ: tvätta och bättra i första hand, söderfasader oftare, blottlägga gamla färglager, sandblästring
  olämpligt på trä, varmluft på mindre ytor; Solhem som värdefull miljö.
Älvsjö – två färgtyper på samma hus: villastadens slätputsade bottenvåning och panelklädda gavelspetsar (Stadsmuseets
  inventering), kalkfärg på kalkputs och dess villkor (RAÄ), linoljefärg på trä (RAÄ), gränsen mellan puts och panel,
  Älvsjö villastad som värdefull miljö med generösa byggrätter (Varsam).
Österåker – Svinningeudd och Nantes: fasadkulörerna (bruna, gula, grå, beige) och linoljefärgen på fasspontpanelen,
  rådet för nya hus (ljusa kulörer med oljefärg eller Falu rödfärg) ur Råd och vägledning för byggande i Svinninge,
  Österåkers bygglovsguide (lov även för underhåll i särskilt värdefulla miljöer), RAÄ om slamfärg och om att byta färgtyp.
Östermalm – husets första kulör: riksintresset Stockholms innerstad med Djurgården (AB 115: den täta och enhetliga
  stenstaden, Villastaden, Lärkstaden, Diplomatstaden), RAÄ om att blottlägga äldre färglager och spara provytor,
  samråd med länsmuseet, områdesfakta Hedvig Eleonora (bostadsrätter), lov mot allmän plats, ingen ROT – egen trust-rad.
Kista – husgruppens kulörer i de storskaliga stadsdelarna (Varsam: tegel, trä och skivor, noga komponerad och enhetlig
  färgsättning, villor och atriumhus i Akalla), Kista 1975–80 med friare arkitektur (Stockholms spår), ägarformer i Kista
  och Akalla (områdesfakta 2025), RAÄ om att undersöka befintlig målning och om utsatta byggnadsdelar.

Fakta endast från källorna i respektive 'sources', öppnade med urllib (Mozilla-UA) 2026-10-27, alla 200 utom
Skatteverket (återställd anslutning – samma adresser och ROT-meningar som v23–v25). Pdf:erna (RAÄ Byggnadsmåleri,
Varsam, riksintresse-pdf, områdesfakta, Stadsmuseets inventering av Älvsjö, Botkyrkas kulturmiljöprogram, Svinninge-
riktlinjerna, Stockholms spår) har textlager.
Strukna / ej använda: kulörer för enskilda kvarter i Kista och på Östermalm (ingen källa), garantitider, avgifter,
handläggningstider, priser, omdömen, egna uppdrag i orterna och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no hands, no text, no letters"

_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_RIKS = ("Stockholms stad – Översiktsplan, riksintressen (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"
_STH_FAS = ("Stockholms stad – Fasadändring", _SB + "fasadandring/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_BV_FAS = ("Boverket – Fasadändring (PBL kunskapsbanken)",
           "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_RAA_MAL = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf)", "https://www.raa.se/publicerat/9789172095830.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 och 12 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SPAR_KISTA = ("Stockholms stadsmuseum – Stockholms spår: Kista (pdf)",
               "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000080.pdf")

_ROT_AMT = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
            "tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.")
_ROT_VILLA = ("Utvändig målning av ett småhus som du äger och bor i räknas som rotarbete hos Skatteverket. Avdraget gäller "
              "arbetskostnaden, inte färgen.")

_TRUST_BRF = ["Gratis besök och kostnadsförslag", "Handlingar till bygglovet"]

PAGES_TJ = {

# ------------------------------------------------------------------ BOTKYRKA
"fasadmalning-botkyrka.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Botkyrka", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Botkyrka – Tullinges villor och kulörbytet",
  "description": "Fasadmålning i Botkyrka: Tullinges villor från 1900–1940, riktlinjen om tidstypiska fasader, kulörbyte som fasadändring och lagren i webbkartan.",
  "h1": "Fasadmålning i Botkyrka",
  "lead": "En villa i Tullinge kan vara nationalromantisk från 1910-talet, ett kataloghus från 1920-talet eller ett putsat funkishus, och varje epok har sina material och sin färgsättning. Botkyrka kommun räknar dessutom ett byte av kulör som en fasadändring. Geal Entreprenad AB målar om fasader på villor och radhus i Botkyrka och utgår från husets epok när färgtyp och kulör väljs.",
  "card": "Tullinges villor och kulörbytet.",
  "sections": [
    {"id": "tullinge-botkyrka", "anchor": "Tullinge",
     "h2": "Villaområdet som växte fram vid stationen",
     "paras": [
       "Enligt Botkyrkas kulturmiljöprogram öppnade Tullinge järnvägsstation 1903, och det var starten för att Tullinge kunde bli ett villasamhälle. Den tidiga exploateringen sköttes av Tullinge AB, och på 1920-talet planlades egnahemsområdet Hamra söder om järnvägen för tjänstemän och arbetare vid AB Separators gjuteri.",
       "Programmet beskriver Tullinge villaområde som representativt för villabyggandet under 1900–1940-talen, och det är framför allt bebyggelsen från den perioden som är kulturhistoriskt intressant. Vid Tullingesjön finns villor i nationalromantisk och jugendinspirerad stil, och i egnahemsområdet dominerar kataloghus.",
     ],
     "aside": {"title": "Tullinge i korthet", "items": [
       "Stationen öppnade 1903", "Hamra egnahem planlades på 1920-talet", "Villor från 1900–1940-talen"]}},
    {"id": "epokerna-botkyrka", "h2": "Fyra epoker, fyra fasader",
     "paras": [
       "Kulturmiljöprogrammet beskriver de nationalromantiska villorna från 1900–1910-talen med branta takfall, liggande fasadpanel, småspröjsade fönster och vitmålade fönsterfoder. Kataloghusen kom på 1920-talet och spreds snabbt till villasamhällena. Från 1930–40-talen kommer enkla volymer med slätputsade fasader eller stående locklistpanel.",
       "Folkhemmets villor från 1940–50-talen beskrivs med putsarkitektur under 1940-talet och fasadtegel under 1950-talet. En puts, en liggande panel och en locklistpanel kräver olika färgtyper och olika förarbete, och därför börjar vi med att bestämma vilken epok huset hör till.",
     ],
     "aside": {"title": "Fasader per epok", "items": [
       "1900–1910-tal: liggande panel, vita foder", "1920-tal: kataloghus", "1930–40-tal: slätputs eller locklistpanel", "1940–50-tal: puts och tegel"]}},
    {"id": "riktlinjen-botkyrka", "h2": "Kommunens riktlinje för villorna",
     "paras": [
       "För Tullinge villaområde skriver kulturmiljöprogrammet att villor med bevarad ursprunglig karaktär ska värnas och att ändringar ska göras med respekt för huvudbyggnadens karaktärsdrag. Fasader, tak, fönster, entrépartier och balkonger ska ges en tidstypisk utformning.",
       "Vid en fasadmålning betyder det att färgsättningen helst ska spegla husets tid. Riksantikvarieämbetet ger samma råd ur teknisk synvinkel: vid ommålning bör man i de flesta fall hålla sig till samma färgtyp som tidigare, och äldre färgsättning och kulörval bör bevaras eftersom de i regel är typiska för husets epok.",
     ],
     "aside": None},
    {"id": "kuloren-botkyrka", "h2": "När en ny kulör är en fasadändring",
     "paras": [
       "Botkyrka kommun förklarar att byte av kulör räknas som fasadändring, och ger exemplet att måla om en byggnad från röd till vit. På ett en- eller tvåbostadshus är fasadändringen normalt lovfri, men utökad lovplikt kan gälla om byggnaden eller området är särskilt värdefullt eller om detaljplanen kräver lov.",
       "Kommunen hänvisar till sin webbkarta. Under den blå fliken Bibliotek och kultur finns lagret Kulturmiljöprogram, under Bygga och bo lagret Detaljplaner och under Riksintressen lagret Kulturmiljövård. Vi går igenom kartan för din fastighet innan en ny kulör föreslås.",
     ],
     "aside": {"title": "Lager i Botkyrkas webbkarta", "items": [
       "Bibliotek och kultur: Kulturmiljöprogram", "Bygga och bo: Detaljplaner", "Riksintressen: Kulturmiljövård"]}},
    {"id": "arbetet-botkyrka", "h2": "Förarbetet avgör resultatet",
     "paras": [
       "Riksantikvarieämbetet påpekar att trä som ska målas måste vara torrt och att fuktkvoten inte får överstiga 15 procent vid målningstillfället. Vid ommålning av en linoljemålad panel tvättas ytan, spikar som krupit upp slås in, lös färg skrapas bort och skadade partier bättras innan slutstrykningen. Myndigheten skriver att fasaden kan tvättas med soda och vatten, och att dagens luftföroreningar gör tvätten nödvändig även där man förr inte tvättade före ommålning.",
       "Om måleri i Botkyrka i övrigt kan du läsa under " + _L.format("malare-botkyrka.html", "målare i Botkyrka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Botkyrka till",
  "steps": [
    ("Webbkartan", "Kulturmiljöprogram, detaljplan och riksintressen kontrolleras för fastigheten."),
    ("Platsbesök", "Husets epok, fasadmaterial och nuvarande färgtyp går vi igenom."),
    ("Skriftligt kostnadsförslag", "Förarbete, färgtyp och antal strykningar redovisas."),
    ("Kulören", "Ny kulör stäms av mot reglerna innan den beställs."),
    ("Målning", "Tvätt, skrapning, bättring och strykning i rätt färgtyp."),
    ("Genomgång", "Vi går igenom fasaderna och snickerierna med dig."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Botkyrka",
  "rot": [_ROT_VILLA, _ROT_AMT],
  "price_h2": "Vad påverkar priset för fasadmålningen i Botkyrka?",
  "price": [
    "Fasadernas yta och material, hur mycket som behöver skrapas och bättras, färgtyp, antal strykningar och ställning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken färgsättning hade de nationalromantiska villorna i Tullinge?",
     "Kulturmiljöprogrammet beskriver liggande fasadpanel, småspröjsade fönster och vitmålade fönsterfoder som karaktäristiskt för villorna från 1900–1910-talen."),
    ("Räknas det som fasadändring att måla om vårt hus i Tullinge från rött till vitt?",
     "Ja. Botkyrka kommun ger just det exemplet: att måla om en byggnad från röd till vit kulör är en fasadändring."),
    ("Var ser jag om mitt hus i Botkyrka ingår i kulturmiljöprogrammet?",
     "I kommunens webbkarta, under den blå fliken Bibliotek och kultur och lagret Kulturmiljöprogram."),
    ("Hur torr måste panelen vara innan den målas?",
     "Riksantikvarieämbetet anger att fuktkvoten i träet inte får överstiga 15 procent vid målningstillfället."),
  ],
  "sources": [("Botkyrka kommun – Kulturmiljöprogram (pdf)", "https://www.botkyrka.se/download/18.1fbbaae6170bff9469deb7f/1602575505534/Kulturmilj%C3%B6program.pdf"),
              ("Botkyrka kommun – Fasadändring", "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/fasadandring"),
              _RAA_MAL, _SKV, _SKV2],
  "cta": ("Ska villan i Botkyrka målas om?", "Boka ett gratis platsbesök, så går vi igenom husets epok, färgtyp och kulör innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nationalromantisk villa med mörkgrön panel och vita fönsterfoder",
     "1910s Swedish national romantic villa with horizontal wooden facade panel painted in a muted green-grey, steep red clay tile roof, small-paned windows with white painted frames, garden with birch trees, railway village suburb south of Stockholm, summer" + _IMG_END),
    ("Funkisvilla med slätputsad fasad i ljus kulör",
     "1930s Swedish functionalist villa with smooth light rendered facade in pale cream, simple cubic volume, windows without glazing bars, low hipped roof, lawn and pine trees, summer" + _IMG_END),
    ("Nyskrapad panel med bättrade partier före slutstrykning",
     "close view of a wooden facade panel on an old house prepared for repainting, loose paint scraped off, some areas primed, nail heads set, paint scraper lying on a scaffold plank, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"fasadmalning-spanga.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Spånga", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Spånga – bättra eller måla om hela villan?",
  "description": "Fasadmålning i Spånga: villastäderna Bromsten, Flysta och Sundby, när det räcker att tvätta och bättra och hur gammal färg tas bort från trä.",
  "h1": "Fasadmålning i Spånga",
  "lead": "En trävilla i Bromsten eller Flysta behöver sällan målas om på alla fyra sidor samtidigt. Söderfasaden och snickerierna slits fortare än norrsidan, och ibland räcker det att tvätta och bättra. Geal Entreprenad AB målar om fasader på villor och radhus i Spånga och bedömer varje fasad för sig innan omfattningen bestäms.",
  "card": "Bättra eller måla om hela villan.",
  "sections": [
    {"id": "villastaderna-spanga", "anchor": "Villastäderna",
     "h2": "Villastäderna längs järnvägen",
     "paras": [
       "Stadens strategi för småhusområden, Varsam, beskriver hur små stationssamhällen uppstod när järnvägen byggdes ut, och hur några på 1910-talet fick status som municipalsamhällen med egen administration, bland annat Spånga. I strategins tabell räknas Bromsten, Flysta, Sundby och Solhem till villastäderna.",
       "Villastäderna var privat organiserade, och Varsam beskriver en brokigare bebyggelse än i de egnahemsområden staden planerade. Trä var det dominerande fasadmaterialet, även om puts förekom, och glasverandor, takkupor, snickarglädje och färgsättning ger en variation som syns än i dag.",
     ],
     "aside": {"title": "Villastäder i Spånga", "items": [
       "Bromsten", "Flysta", "Sundby", "Solhem (värdefull miljö)"]}},
    {"id": "battra-spanga", "h2": "Tvätta och bättra i första hand",
     "paras": [
       "Riksantikvarieämbetet påpekar att bättringsmåleri kan vara lämpligt även utomhus, eftersom vissa byggnadsdelar slits snabbare än andra. Söderfasader behöver målas om oftare än norrfasader, och fönster och delar av dem oftare än fasaden runt omkring. Mild rengöring och bättring av skadade partier är enligt myndigheten ett utmärkt sätt att förlänga livslängden på en linoljefärg som i övrigt är hel.",
       "Därför går vi igenom fasaderna en och en. Är norr- och östsidan i gott skick kan det räcka att tvätta dem och bättra skadorna, medan söder- och västsidan och snickerierna målas om helt. Det ger en lägre kostnad nu och en jämnare underhållscykel framåt.",
     ],
     "aside": {"title": "Slits fortast enligt RAÄ", "items": [
       "Söderfasader", "Fönstersnickerier", "Vindskivor", "Vattbrädor och räcken"]}},
    {"id": "fargtypen-spanga", "h2": "Vad sitter på väggen i dag?",
     "paras": [
       "Riksantikvarieämbetet varnar för att måla över äldre färgtyper med moderna material, eftersom nästa underhåll då ofta blir komplicerat och en återgång kan kräva att all färg tas bort. Har en villa målats om flera gånger kan det vara svårt även för en fackman att säga vilka färgtyper som använts. Brister i underlaget och ett tidigare felaktigt val av färgtyp rättas enligt myndigheten inte till genom att lägga på ytterligare färgskikt.",
       "Vi tar därför prov på hur färgen sitter och vad den består av innan något beställs. Myndigheten påpekar också att tidigare kulörer i många fall kan hittas genom att blottlägga äldre färglager, och att det är bra att spara några obehandlade provytor på undanskymda ställen som dokumentation för nästa gång.",
     ],
     "aside": None},
    {"id": "skrapningen-spanga", "h2": "Gammal färg av utan att skada träet",
     "paras": [
       "Ska färgen bort på större ytor avråder Riksantikvarieämbetet från att sandblästra träfasader, eftersom underlaget lätt skadas. På mindre ytor kan färgen tas bort med varmluft, som är skonsammare än bränning, men även då krävs försiktighet eftersom vissa material har låg antändningstemperatur.",
       "Spikar som krupit upp slås in och lösa partier skrapas till fast underlag innan grundning. Om fasadmaterial och reparationer i Spånga kan du läsa under " + _L.format("fasadrenovering-spanga.html", "fasadrenovering i Spånga") + ".",
     ],
     "aside": None},
    {"id": "solhem-spanga", "h2": "Solhem och kulören",
     "paras": [
       "I Varsam-tabellen är Solhem markerat som kulturhistoriskt värdefull miljö, till skillnad från Bromsten, Flysta och Sundby. Stockholms stad skriver att byte av kulör räknas som fasadändring och att utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla områden.",
       "Ska kulören ändras kontrollerar vi Stadsmuseets klassificeringskarta och detaljplanen för fastigheten först. Om måleri i Spånga i övrigt kan du läsa under " + _L.format("malare-spanga.html", "målare i Spånga") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Spånga till",
  "steps": [
    ("Platsbesök", "Varje fasad bedöms för sig: skador, färgtyp och nedsmutsning."),
    ("Omfattning", "Vi föreslår vad som bättras och vad som målas om helt."),
    ("Skriftligt kostnadsförslag", "Fasad för fasad, med snickerier för sig."),
    ("Kulören", "Ändras kulören kontrolleras karta och detaljplan."),
    ("Målning", "Tvätt, skrapning, bättring och strykning i samma färgtyp."),
    ("Genomgång", "Vi går igenom fasaderna och lämnar uppgift om färgtypen."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Spånga",
  "rot": [_ROT_VILLA, _ROT_AMT],
  "price_h2": "Vad påverkar priset för fasadmålningen i Spånga?",
  "price": [
    "Hur många fasader som målas om helt, skador och skrapning, färgtyp, snickerier och ställning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste hela villan i Bromsten målas om samtidigt?",
     "Nej, det behövs inte i alla fall. Riksantikvarieämbetet påpekar att söderfasader och snickerier slits fortare, och att mild rengöring och bättring kan förlänga livslängden på en färg som i övrigt är hel."),
    ("Kan vi sandblästra bort gammal färg från panelen?",
     "Riksantikvarieämbetet avråder från sandblästring av träfasader eftersom underlaget lätt skadas. På mindre ytor kan varmluft användas med försiktighet."),
    ("Hur hittar vi villans ursprungliga kulör?",
     "Tidigare kulörer kan ofta hittas genom att blottlägga äldre färglager, enligt Riksantikvarieämbetet. Vi tar prov på ett undanskymt ställe."),
    ("Är Flysta kulturhistoriskt värdefullt?",
     "Flysta saknar den markeringen i stadens strategi Varsam, där bara Solhem av villastäderna i Spånga är markerat som kulturhistoriskt värdefull miljö. Stadsmuseets karta visar vad som gäller för den enskilda fastigheten."),
  ],
  "sources": [_VARSAM, _RAA_MAL, _STH_FAS, _STH_KL, _SKV, _SKV2],
  "cta": ("Ska villan i Spånga målas om?", "Boka ett gratis platsbesök, så går vi igenom fasaderna en och en innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Trävilla med glasveranda på en villagata i Spånga",
     "early 1900s Swedish wooden villa with a glazed veranda, ornamental woodwork, light yellow painted panel and white trim, red tile roof, garden with fruit trees and hedge, villa street northwest of Stockholm, summer" + _IMG_END),
    ("Söderfasad med flagnande färg bredvid en hel norrfasad",
     "exterior corner of an old Swedish wooden villa seen from the garden: the sunlit outside wall has faded, cracked and flaking light yellow paint, the adjoining shaded outside wall has intact paint, white corner board, grass and shrubs at the base, blue sky, daylight" + _IMG_END),
    ("Färgprov där äldre färglager blottlagts på en panel",
     "close view of an old painted wooden facade board where a small area has been carefully scraped to reveal several older paint layers in different colours, scraper lying beside, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"fasadmalning-alvsjo.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Älvsjö", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Älvsjö – puts nedtill, panel upptill",
  "description": "Fasadmålning i Älvsjö: villor med putsad bottenvåning och panelklädda gavlar, kalkfärg på putsen, linoljefärg på träet och gränsen mellan dem.",
  "h1": "Fasadmålning i Älvsjö",
  "lead": "Många villor i Älvsjö villastad har två fasadmaterial på samma hus: slätputs på bottenvåningen och träpanel i gavelspetsarna. Puts och trä behöver olika färgtyper, och det är där en fasadmålning i Älvsjö skiljer sig från en vanlig trävilla. Geal Entreprenad AB målar om fasader i Älvsjö och väljer färgtyp för varje material för sig.",
  "card": "Puts nedtill, panel upptill.",
  "sections": [
    {"id": "villastaden-alvsjo", "anchor": "Villastaden",
     "h2": "Hustypen från 1910-talet",
     "paras": [
       "Stadsmuseets inventering av Älvsjö villastad beskriver hur AB Hem på landet köpte mark från Älvsjö säteri 1908 och 1911. En relativt vanlig hustyp var det friliggande enfamiljshuset med vit slätputsad bottenvåning och gavelspetsar klädda med mörkbrunmålad panel på förvandring, småspröjsade fönster med luckor och brant sadeltak med rött tegel.",
       "Inventeringen visar också en ritning från 1913–1914 till en villa i villastaden med just slätputsad bottenvåning och gavelspetsar med panel på förvandring. Enligt inventeringen finns hustypen kvar i Älvsjö i så gott som helt ursprungligt skick.",
     ],
     "aside": {"title": "Vanlig hustyp i inventeringen", "items": [
       "Vit slätputsad bottenvåning", "Gavelspetsar med panel på förvandring", "Småspröjsade fönster med luckor", "Brant tegeltäckt sadeltak"]}},
    {"id": "putsen-alvsjo", "h2": "Putsen och kalkfärgen",
     "paras": [
       "Riksantikvarieämbetet beskriver kalkfärg som den färg som i århundraden använts på puts, och anger att den i dag främst används vid ommålning av putsytor som tidigare kalkats och på ny kalkputs på kulturhistoriskt värdefulla hus. Kalkfärgen fäster bra på kalkputs men dåligt på cementrika eller förgipsade underlag, och den släpper nästan obehindrat igenom fukt.",
       "Har bottenvåningen lagats med cementhaltig puts någon gång ska sådana lagningar enligt myndigheten tas bort och putsas om med kalkputs innan fasaden kalkas. Därför börjar vi med att knacka och titta på putsen, så att vi vet vilket underlag färgen ska ligga på.",
     ],
     "aside": {"title": "Kalkfärg enligt RAÄ", "items": [
       "Fäster på kalkputs", "Dålig vidhäftning på cementrikt underlag", "Släpper igenom fukt", "Ommålning: 3–7 strykningar"]}},
    {"id": "panelen-alvsjo", "h2": "Panelen och linoljefärgen",
     "paras": [
       "På gavelspetsarnas panel är linoljefärg den traditionella färgtypen. Riksantikvarieämbetet skriver att linoljefärg dominerade på trähus ända fram till mitten av 1900-talet där rödfärg inte användes, att den ska strykas tunt och att den torkar långsammare än moderna färger. Bästa målningsperioden är maj till augusti, och direkt solsken bör undvikas.",
       "Myndigheten påpekar också att det inte räcker att välja en traditionell färgtyp: kulör och teknik ska vara riktiga för just den byggnaden. Om villastadens kulörer och snickerier kan du läsa under " + _L.format("malare-alvsjo.html", "målare i Älvsjö") + ".",
     ],
     "aside": None},
    {"id": "granssnittet-alvsjo", "h2": "Gränsen mellan puts och trä",
     "paras": [
       "Kalkfärg ska enligt Riksantikvarieämbetet målas utan avbrott på en fasadyta och får bara göra uppehåll vid hörn eller andra naturliga gränser. På en Älvsjövilla är övergången mellan puts och panel en sådan gräns, och vi planerar arbetet så att putsen målas klart innan panelen ovanför strykes.",
       "Kalkfärg målas utomhus från senvåren till eftersommaren och i god tid före frost, med ett skikt per dag. Eftersom linoljefärgen på panelen har sin bästa period under samma månader lägger vi upp ett schema där de två färgtyperna inte stör varandra.",
     ],
     "aside": None},
    {"id": "omradet-alvsjo", "h2": "Värdefull miljö med generösa byggrätter",
     "paras": [
       "I stadens strategi Varsam är del av Älvsjö markerad som kulturhistoriskt värdefull miljö och som område med generösa byggrätter i äldre planer. Stockholms stad räknar byte av kulör som fasadändring och påpekar att utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla områden.",
       "Behålls kulören är det underhåll, men ska den ändras kontrollerar vi Stadsmuseets klassificeringskarta först. Om puts och panel som material kan du läsa under " + _L.format("fasadrenovering-alvsjo.html", "fasadrenovering i Älvsjö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Älvsjö till",
  "steps": [
    ("Platsbesök", "Puts, panel och nuvarande färgtyper går vi igenom."),
    ("Putsen", "Lagningar och underlag kontrolleras innan färgtyp väljs."),
    ("Skriftligt kostnadsförslag", "Puts och panel redovisas var för sig."),
    ("Schema", "Kalkning och oljemålning planeras så att de inte krockar."),
    ("Målning", "Putsen kalkas yta för yta, panelen strykes tunt med linoljefärg."),
    ("Genomgång", "Vi går igenom fasaderna och lämnar uppgift om färgtyperna."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Älvsjö",
  "rot": [_ROT_VILLA, _ROT_AMT],
  "price_h2": "Vad påverkar priset för fasadmålningen i Älvsjö?",
  "price": [
    "Andelen puts och panel, putslagningar, färgtyper, antal strykningar, snickerier och ställning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan samma färg användas på putsen och panelen på vår villa i Älvsjö?",
     "Oftast inte. Kalkfärg är den traditionella färgen på kalkputs och linoljefärg på trä, enligt Riksantikvarieämbetet, och de har olika egenskaper och arbetsgång."),
    ("Vad gör vi med gamla cementlagningar i den putsade bottenvåningen?",
     "Riksantikvarieämbetet anger att lagningar med cementhaltig eller förgipsad puts ska tas bort och putsas om med kalkputs innan fasaden kalkas."),
    ("Hur många strykningar kalkfärg behövs utomhus?",
     "Riksantikvarieämbetet anger 3–7 strykningar utomhus, med ett skikt per dag och fixering med kalkvatten."),
    ("Vilken hustyp var vanlig i Älvsjö villastad på 1910-talet?",
     "Stadsmuseets inventering nämner villan med vit slätputsad bottenvåning, gavelspetsar med mörkbrunmålad panel, småspröjsade fönster med luckor och brant tegeltak."),
  ],
  "sources": [("Stadsmuseet – Inventering av Älvsjö villastad (Stockholmskällan, pdf)", "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf"),
              _RAA_MAL, _VARSAM, _STH_FAS, _STH_KL, _SKV, _SKV2],
  "cta": ("Ska villan i Älvsjö målas om?", "Boka ett gratis platsbesök, så går vi igenom putsen och panelen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa med vit putsad bottenvåning och panelklädd gavel",
     "1910s Swedish villa with white smooth rendered ground floor and dark brown painted wooden panel in the gable above, small-paned windows with shutters, steep red clay tile gable roof, garden with lilac and fruit trees, Stockholm suburb, summer" + _IMG_END),
    ("Övergången mellan puts och träpanel på en gavel",
     "close view of the junction between a white lime rendered wall and a dark brown painted wooden gable panel above, with a horizontal wooden drip board between them, daylight" + _IMG_END),
    ("Nykalkad putsyta med levande yta",
     "close view of a freshly lime-washed rendered wall in white with a lively slightly mottled surface, window shutter edge visible, soft daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"fasadmalning-osteraker.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Österåker", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Österåker – sommarvillornas fasadkulörer",
  "description": "Fasadmålning i Österåker: Svinninges sommarvillor med linoljemålad panel, kulörerna i kommunens riktlinjer, rådet för nya hus och lov för underhåll.",
  "h1": "Fasadmålning i Österåker",
  "lead": "Sommarvillorna i Svinninge målades med linoljefärg i bruna, gula, grå och beige toner, och snickerierna i kontrasterande färger. Kommunens riktlinjer för området beskriver både de gamla kulörerna och vad nya hus bör målas med. Geal Entreprenad AB målar om fasader på villor och fritidshus i Österåker och utgår från riktlinjerna när kulören väljs.",
  "card": "Sommarvillornas fasadkulörer.",
  "sections": [
    {"id": "svinninge-osteraker", "anchor": "Svinninge",
     "h2": "Kommunens äldsta sommarhusbebyggelse",
     "paras": [
       "Österåkers kommuns skrift Råd och vägledning för byggande i Svinninge beskriver det strandnära området Svinningeudd och Nantes som kommunens äldsta och bäst bevarade sommarhusbebyggelse. Där står också att de flesta tomterna har en storlek som överstiger 1 500 kvadratmeter och ger mycket luft mellan husen.",
       "Skriften beskriver brokigheten som en stor tillgång, men en som måste hanteras varsamt för att området inte ska uppfattas som osammanhängande. En fasad i fel kulör eller färgtyp är ett av de sätt som helheten kan brytas på.",
     ],
     "aside": {"title": "Svinningeudd och Nantes", "items": [
       "Kommunens äldsta sommarhusbebyggelse", "Tomter ofta över 1 500 m²", "Brokigheten är en tillgång"]}},
    {"id": "kulorerna-osteraker", "h2": "Bruna, gula, grå och beige fasader",
     "paras": [
       "Enligt riktlinjerna är de flesta sommarvillorna i Svinningeudd och Nantes klädda med liggande hyvlad fasspontpanel som ursprungligen målades med linoljefärg. Sommarvillorna från sekelskiftet hade en rik färgskala, och bruna, gula, grå och beiga nyanser var vanliga på fasaden, medan fönsterfoder och listverk ofta fick färger som avvek från byggnadskroppen.",
       "Sportstugorna beskrivs med mörkt bruna fasader och gröna snickerier, men också med faluröda fasader och vita snickerier. Vid en ommålning tar vi reda på vilken grupp huset hör till och vilken kulör det hade, innan vi föreslår färgsättning.",
     ],
     "aside": {"title": "Kulörer enligt riktlinjerna", "items": [
       "Sommarvillor: bruna, gula, grå, beige", "Foder och listverk: avvikande färg", "Sportstugor: mörkbrunt eller faluröd"]}},
    {"id": "nyahus-osteraker", "h2": "Rådet för nya hus och tillbyggnader",
     "paras": [
       "För ny bebyggelse skriver riktlinjerna att fasadmaterialet i huvudsak bör vara trä målat i ljusa kulörer med oljefärg eller Falu rödfärg, alternativt andra slamfärgskulörer, och att alternativa material prövas i bygglov. Det rådet är också en bra utgångspunkt när en tillbyggnad ska målas i samma veva som huset.",
       "Riksantikvarieämbetet beskriver slamfärg som billig, fuktgenomsläpplig och den i särklass mest underhållsvänliga färgtypen, där det bara är att borsta och måla om. Men myndigheten påpekar också att den som en gång har bytt till en annan färgtyp, till exempel latex, alkyd eller linoljefärg, inte kan gå tillbaka till slamfärg ens om den befintliga färgen tas bort.",
     ],
     "aside": None},
    {"id": "lovet-osteraker", "h2": "Även underhåll kan kräva lov",
     "paras": [
       "Österåkers kommun skriver att du behöver söka bygglov om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden är särskilt värdefull, och nämner bland annat att ändra fasaden och att underhålla. Kommunen uppmanar dig att kontakta bygglovenheten innan arbetet påbörjas och hänvisar till Österåkerskartan för att se om fastigheten ligger i ett kulturmiljöområde.",
       "Kommunen ger också några frågor för att bedöma om ett hus kan vara värdefullt, bland annat om det har bevarade byggnadsdetaljer som fönster och fasadmaterial. Vi går igenom kartan innan arbetet planeras. Om fasadmaterial och skärgårdshus i kommunen kan du läsa under " + _L.format("fasadrenovering-osteraker.html", "fasadrenovering i Österåker") + ".",
     ],
     "aside": {"title": "Kontrollera först", "items": [
       "Österåkerskartan", "Detaljplanens skyddsbestämmelser", "Kulturmiljöprogram eller inventering"]}},
    {"id": "linoljan-osteraker", "h2": "Linoljefärg på fasspontpanelen",
     "paras": [
       "Riksantikvarieämbetet anger att linoljefärg ska strykas tunt i flera skikt, att trä inte får ha högre fuktkvot än omkring 15 procent och att maj till augusti är bästa målningsperioden. Direkt solsken bör undvikas, och det är bäst att följa solens gång och stryka fasader som redan varit solbelysta.",
       "En rätt sammansatt och påförd linoljefärg har enligt myndigheten lång livslängd, men utsatta delar som fönstersnickerier, vindskivor och sydfasader behöver målas oftare. Om måleri i Österåker i övrigt kan du läsa under " + _L.format("malare-osteraker.html", "målare i Österåker") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Österåker till",
  "steps": [
    ("Kartan", "Österåkerskartan och detaljplanen kontrolleras för fastigheten."),
    ("Platsbesök", "Panel, snickerier och nuvarande färgtyp går vi igenom."),
    ("Färgsättning", "Kulörer för fasad och snickerier föreslås utifrån husets tid."),
    ("Skriftligt kostnadsförslag", "Fasader och snickerier redovisas för sig."),
    ("Målning", "Tvätt, skrapning, bättring och tunna strykningar."),
    ("Genomgång", "Vi går igenom resultatet och lämnar uppgift om färgtypen."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Österåker",
  "rot": [_ROT_VILLA + " Det gäller även fritidshus som du äger.", _ROT_AMT],
  "price_h2": "Vad påverkar priset för fasadmålningen i Österåker?",
  "price": [
    "Fasadernas yta, panelens skick, snickerier och lövsågerier, färgtyp, antal kulörer och ställning i kuperad terräng. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka fasadkulörer hade sommarvillorna i Svinninge?",
     "Enligt kommunens riktlinjer var bruna, gula, grå och beiga nyanser vanliga på fasaden, med foder och listverk i avvikande färger."),
    ("Vad bör ett nytt hus eller en tillbyggnad i Svinninge målas med?",
     "Riktlinjerna anger trä målat i ljusa kulörer med oljefärg eller Falu rödfärg, eller andra slamfärgskulörer. Alternativa material prövas i bygglov."),
    ("Kan vi gå tillbaka till slamfärg på en panel som är målad med latex?",
     "Enligt Riksantikvarieämbetet går det inte att måla om med slamfärg när man en gång bytt till en annan färgtyp, även om den befintliga färgen tas bort."),
    ("Kan vanligt underhåll kräva bygglov i Österåker?",
     "Ja, i ett kulturhistoriskt särskilt värdefullt område eller på en särskilt värdefull byggnad nämner kommunen underhåll bland de åtgärder som kräver lov. Kontakta bygglovenheten innan arbetet börjar."),
  ],
  "sources": [("Österåkers kommun – Råd och vägledning för byggande i Svinninge (pdf)", "https://www.osteraker.se/download/18.5bb0400617c11d33b5536/1632390824156/rad_och_vagledning_svinninge.pdf"),
              ("Österåkers kommun – Kulturhistoriska byggnader, kulturmiljöer", "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/bygglovsguiden/kulturhistoriskabyggnaderkulturmiljoer.4.367d658917909e8fc2bb42.html"),
              _RAA_MAL, _SKV, _SKV2],
  "cta": ("Ska sommarvillan i Österåker målas om?", "Boka ett gratis platsbesök, så går vi igenom panel, kulörer och lovfrågan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sommarvilla med gul fasspontpanel och glasveranda vid vattnet",
     "late 1800s Swedish summer villa with horizontal planed wooden panel painted in warm light yellow, white ornamental fretwork on a glazed veranda, darker window frames, red tile roof, pine trees and glimpse of the sea in the Stockholm archipelago, summer" + _IMG_END),
    ("Sportstuga med mörkbrun fasad och gröna snickerier",
     "small 1930s Swedish wooden cottage with dark brown painted facade and green painted window frames and corner boards, pine forest plot, summer" + _IMG_END),
    ("Lövsågad verandadetalj med nymålade foder",
     "close view of ornamental fretwork on the veranda of an old Swedish summer villa, freshly repainted in contrasting colours, beige panel and dark red trim, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERMALM
"fasadmalning-ostermalm.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Östermalm", "svc_label": "Fasadmålning",
  "trust": _TRUST_BRF,
  "title": "Fasadmålning på Östermalm – husets ursprungliga kulör",
  "description": "Fasadmålning på Östermalm: stenstaden i riksintresset, Lärkstaden och Diplomatstaden, husets tidigare kulörer i färglagren och föreningens underlag.",
  "h1": "Fasadmålning på Östermalm",
  "lead": "När en förening på Östermalm ska måla om fasaden är en av de första frågorna vilken kulör huset hade från början. Svaret finns ofta i färglagren under den nuvarande färgen. Geal Entreprenad AB målar fasader på flerbostadshus på Östermalm och hjälper styrelsen att ta fram underlaget om kulör, färgtyp och lov.",
  "card": "Husets ursprungliga kulör.",
  "sections": [
    {"id": "riksintresset-ostermalm", "anchor": "Riksintresset",
     "h2": "Stenstaden i riksintresset",
     "paras": [
       "Östermalm ligger inom riksintresset Stockholms innerstad med Djurgården (AB 115). I stadens beskrivning nämns det sena 1800-talets stadsbyggande med esplanadsystemet, gator av olika bredd och byggnader i bestämda hushöjder, områden planlagda enligt 1874 års byggnadsstadga och den täta och enhetliga stenstadsbebyggelsen. Villastaden räknas också dit.",
       "Bland uttrycken för 1900-talets stadsbyggande nämns Lärkstaden och Diplomatstaden. En fasad på Östermalm är alltså en del av en helhet som är utpekad på nationell nivå, och kulören är en av de saker som syns mest.",
     ],
     "aside": {"title": "Ur riksintresset AB 115", "items": [
       "Den täta och enhetliga stenstaden", "Villastaden", "Lärkstaden", "Diplomatstaden"]}},
    {"id": "fargarkeologi-ostermalm", "h2": "Färglagren berättar",
     "paras": [
       "Riksantikvarieämbetet skriver att äldre färgsättning och kulörval bör bevaras, eftersom de i regel är typiska för den epok huset kommer från, och att prov på tidigare kulörer i många fall kan hittas genom att blottlägga äldre färglager. Ett litet område skrapas försiktigt ner genom lagren, och kulörerna under dokumenteras.",
       "Myndigheten rekommenderar också att några ytor lämnas helt obehandlade vid en renovering, gärna små och på undanskymda ställen. Sådana provytor är i praktiken den bästa dokumentationen för den som ska välja metod nästa gång, och uppgifter om material och metod bör sparas.",
     ],
     "aside": {"title": "Råd från RAÄ", "items": [
       "Blottlägg äldre färglager", "Spara obehandlade provytor", "Dokumentera material och metod", "Samråd med länsmuseet vid högt värde"]}},
    {"id": "lanmuseet-ostermalm", "h2": "När huset har högt kulturhistoriskt värde",
     "paras": [
       "Anses huset ha högt kulturhistoriskt värde råder Riksantikvarieämbetet att man samråder med länsmuseet om val av kulör, pigment och bindemedel. Länsmuseet kan i regel hänvisa till sakkunniga målarmästare och konservatorer eller ge andra råd.",
       "Stockholms stad hänvisar till Stadsmuseets klassificeringskarta för att se om en byggnad är kulturhistoriskt värdefull. På kartan är riksintressen markerade med blå ring och klassad bebyggelse med blått, grönt, gult eller grått, och staden skriver att du behöver söka bygglov för annars lovfria åtgärder om byggnaden ligger inom ett riksintresse eller är markerad med blått eller grönt.",
       "Kartan uppdateras när nya bedömningar görs, så klassningen kan ändras över tid. Vi kontrollerar den aktuella klassningen och detaljplanen innan styrelsen får ett förslag, så att föreningen vet om ett lov behövs och vilket underlag som kan krävas.",
     ],
     "aside": None},
    {"id": "foreningen-ostermalm", "h2": "Ett beslut för föreningen",
     "paras": [
       "Stadens områdesfakta för 2025 visar 5 151 bostadsrätter i flerbostadshus i Hedvig Eleonora församlingsområde och 2 072 övriga hyresrätter, men bara ett par småhus. Den som beställer en fasadmålning på Östermalm är därför i regel en bostadsrättsförening eller en fastighetsägare.",
       "Stockholms stad skriver att det för byggnader som inte är en- eller tvåbostadshus krävs bygglov för fasadändringar på fasad eller tak som vetter mot allmän plats. Ett byte av kulör är en fasadändring, och vi tar därför fram kulörförslaget och fotounderlaget så att det kan användas i en ansökan.",
     ],
     "aside": {"title": "Hedvig Eleonora 2025", "items": [
       "Bostadsrätter i flerbostadshus: 5 151", "Övriga hyresrätter: 2 072", "Småhus med äganderätt: 2"]}},
    {"id": "fargtypen-ostermalm", "h2": "Samma färgtyp som tidigare",
     "paras": [
       "Riksantikvarieämbetet påpekar att man vid ommålning i de flesta fall bör hålla sig till samma färgtyp som tidigare, och att ett byte av färgtyp också ändrar utseendet. På en putsad stenhusfasad tar vi därför reda på vad den är målad med i dag innan färgtypen bestäms.",
       "Om puts och fasadmaterial på Östermalm kan du läsa under " + _L.format("fasadrenovering-ostermalm.html", "fasadrenovering på Östermalm") + ", och om måleri i stadsdelen under " + _L.format("malare-ostermalm.html", "målare på Östermalm") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning på Östermalm till",
  "steps": [
    ("Platsbesök", "Fasaderna, putsen och nuvarande färgtyp går vi igenom med styrelsen."),
    ("Färglagren", "Ett litet område skrapas ner och tidigare kulörer dokumenteras."),
    ("Klassning och plan", "Stadsmuseets karta och detaljplanen kontrolleras."),
    ("Skriftligt kostnadsförslag", "Varje fasad, ställning och väderskydd för sig."),
    ("Lov", "Kulörförslag och foton tas fram när kulören ändras mot gatan."),
    ("Målning och dokumentation", "Fasaden målas och provytor och metod dokumenteras."),
  ],
  "rot_h2": "Rotavdrag och föreningens fasad",
  "rot": [
    "Skatteverket ger rotavdrag i en bostadsrätt bara för arbete inne i bostaden som bostadsrättshavaren ansvarar för enligt stadgarna. Arbete på gemensamma ytor, till exempel tak och fasader, ger inget rotavdrag.",
    "En fasadmålning på ett föreningshus betalas därför av föreningen utan avdrag, och kostnadsförslaget ställs till föreningen.",
  ],
  "price_h2": "Vad påverkar priset för fasadmålningen på Östermalm?",
  "price": [
    "Fasadernas yta och höjd, putsens skick, färgtyp, färgundersökning, ställning och väderskydd mot gatan och om bygglov behövs. Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur tar vi reda på vilken kulör vårt hus på Östermalm hade från början?",
     "Riksantikvarieämbetet skriver att tidigare kulörer i många fall kan hittas genom att blottlägga äldre färglager. Ett litet område skrapas ner och kulörerna dokumenteras."),
    ("Ingår Lärkstaden i riksintresset för Stockholms innerstad?",
     "Ja, stadens beskrivning av riksintresset Stockholms innerstad med Djurgården nämner Lärkstaden och Diplomatstaden bland uttrycken för 1900-talets stadsbyggande."),
    ("Vad är en provyta och varför ska den sparas?",
     "En liten obehandlad yta på ett undanskymt ställe som visar hur fasaden målats tidigare. Riksantikvarieämbetet kallar sådana ytor den bästa dokumentationen inför nästa renovering."),
    ("När ska föreningen samråda med länsmuseet om fasadfärgen?",
     "Riksantikvarieämbetet råder att man samråder med länsmuseet om val av kulör, pigment och bindemedel när huset anses ha högt kulturhistoriskt värde."),
    ('Varför ska föreningen hålla sig till samma färgtyp på fasaden?',
     'Riksantikvarieämbetet påpekar att man vid ommålning i de flesta fall bör hålla sig till samma färgtyp, eftersom ett byte också ändrar utseendet och kan göra nästa underhåll svårare.'),
  ],
  "sources": [_RIKS, _RAA_MAL,
              ("Stockholms stad – Områdesfakta 2025: Hedvig Eleonora (pdf)", _OF + "inre-staden/norra-innerstaden/hedvig-eleonora.pdf"),
              _STH_FAS, _STH_KL, _BV_FAS, _BRL, _SKV],
  "cta": ("Ska föreningens fasad på Östermalm målas om?", "Boka ett gratis platsbesök, så går vi igenom fasaderna, färglagren och lovfrågan innan föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Putsad stenhusfasad på en esplanad på Östermalm",
     "empty street, no pedestrians, no cars: late 1800s Stockholm stone apartment building with ornate rendered facade in warm sandstone colour, tall windows with surrounds, tree-lined esplanade in front, Östermalm style, daylight" + _IMG_END),
    ("Färgtrappa där äldre kulörer blottlagts på en putsfasad",
     "close view of a small rectangular area on a rendered facade where paint has been scraped in steps to reveal several older paint layers in ochre, grey and pale pink, daylight" + _IMG_END),
    ("Fasad bakom ställning med väderskydd",
     "empty street, no pedestrians: scaffolding with white weather protection sheeting in front of an ornate Stockholm stone apartment building during repainting, street trees, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ KISTA
"fasadmalning-kista.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Kista", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Kista – radhus, atriumhus och husgruppen",
  "description": "Fasadmålning i Kista och Akalla: småhus från 1975–1980 i tegel, trä och skivor, husgruppens färgsättning och vem som beställer målningen.",
  "h1": "Fasadmålning i Kista",
  "lead": "Småhusen i Kista och Akalla byggdes i grupper där fasadmaterial och kulörer bestämdes för hela gruppen. När ett hus målas om påverkar det alltså mer än det egna huset. Geal Entreprenad AB målar om fasader på radhus, kedjehus, villor och atriumhus i Kista och utgår från husgruppen när kulören väljs.",
  "card": "Radhus, atriumhus och husgruppen.",
  "sections": [
    {"id": "friare-kista", "anchor": "Arkitekturen",
     "h2": "Friare former än i grannstadsdelarna",
     "paras": [
       "Enligt Stadsmuseets skrift om Kista i serien Stockholms spår byggdes stadsdelen ut 1975–1980, och staden tillämpade här betydligt friare former för den arkitektoniska utformningen än i de övriga stadsdelarna på Järvafältet. Man strävade också efter att samlokalisera arbetsplatser, bostäder, service och kollektivtrafik.",
       "I stadens strategi Varsam räknas Akalla och Husby till de storskaliga stadsdelarna, och strategin nämner Akalla som exempel där det byggdes villor och atriumhus vid sidan av radhusen och kedjehusen.",
     ],
     "aside": None},
    {"id": "materialen-kista", "h2": "Tegel, trä och skivor på samma hus",
     "paras": [
       "Varsam beskriver hur småhusen i de storskaliga stadsdelarna ofta fick en blandning av fasadmaterial som tegel, trä och skivor, medan enhetligheten inom husgrupperna var mycket stor. Färgsättningen var noga komponerad och enhetlig, men kunde variera mellan olika kvarter eller områden.",
       "För en fasadmålning betyder blandningen att varje material behöver sin egen bedömning. Riksantikvarieämbetet påpekar att man först måste känna till hur den befintliga målningen är utförd och i vilket skick den är, och skilja skador som beror på naturligt åldrande från sådana som beror på brister i underlaget eller ett olämpligt färgval.",
     ],
     "aside": {"title": "Varsam om husgrupperna", "items": [
       "Tegel, trä och skivor", "Noga komponerad färgsättning", "Enhetligt inom gruppen", "Variation mellan kvarter"]}},
    {"id": "agarna-kista", "h2": "Vem beställer målningen?",
     "paras": [
       "Stadens områdesfakta för 2025 visar 482 småhus med äganderätt och 404 i bostadsrätt i stadsdelen Kista. I Akalla är 493 småhus bostadsrätter och 170 äganderätter. I en förening är fasaden i regel gemensam och målas i ett sammanhang för hela gruppen.",
       "Äger du ditt hus själv bestämmer du, men eftersom färgsättningen var tänkt för hela gruppen är det klokt att stämma av kulören med grannarna. Stockholms stad räknar byte av kulör som fasadändring, och lovfria fasadändringar ska ändå stämma med detaljplanen.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Kista: 482 äganderätt, 404 bostadsrätt", "Akalla: 170 äganderätt, 493 bostadsrätt"]}},
    {"id": "atrium-kista", "h2": "Atriumhusens inre gård",
     "paras": [
       "Ett atriumhus har en del av sina fasader vända in mot en egen gård. De väggarna syns inte från gångvägen och vetter åt andra väderstreck än husets yttre fasader, så de åldras inte i samma takt. Riksantikvarieämbetet påpekar att söderfasader behöver målas om oftare än norrfasader och att utsatta delar som vattbrädor, räcken och fönster bör underhållsmålas löpande.",
       "Vi bedömer därför gårdsväggar och yttre väggar var för sig. Om måleri i Kista i övrigt, även inomhus, kan du läsa under " + _L.format("malare-kista.html", "målare i Kista") + ".",
     ],
     "aside": None},
    {"id": "planen-kista", "h2": "Detaljplanen och de äldre programmen",
     "paras": [
       "Stockholms stad påpekar att en fasadändring som inte kräver bygglov ändå ska stämma överens med detaljplanen, eller vara en liten avvikelse som inte motverkar planens syfte. Detaljplanen för fastigheten finns i stadens e-tjänst Bygg- och plantjänsten, och där kan du också själv ta fram äldre handlingar som stadsbyggnadskontoret har för huset.",
       "Staden skriver dessutom att det finns äldre miljöprogram och typritningssamlingar som går att beställa. De har ingen juridisk status i bygglovsprövningen, men är ett bra underlag för att förstå ett områdes karaktär. För en husgrupp där kulörerna en gång valdes samlat kan sådana handlingar visa hur färgsättningen var tänkt.",
     ],
     "aside": {"title": "Underlag att ta fram", "items": [
       "Detaljplanen", "Äldre bygglovshandlingar", "Miljöprogram och typritningar"]}},
    {"id": "dokumentation-kista", "h2": "Spara kulören för nästa gång",
     "paras": [
       "Riksantikvarieämbetet rekommenderar att uppgifter om vilka material renoveringen utförts med bevaras. I en husgrupp där många hus ska ha samma kulör är det extra viktigt, eftersom nästa ägare eller nästa styrelse då vet vad som använts.",
       "Vi lämnar uppgift om färgtyp, kulör och tillverkare när arbetet är klart. Om snickeriarbeten som uterum och förråd i stadsdelen kan du läsa under " + _L.format("snickare-kista.html", "snickare i Kista") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Kista till",
  "steps": [
    ("Ägarform", "Vi reder ut om du eller föreningen beställer målningen."),
    ("Platsbesök", "Tegel, trä, skivor och nuvarande målning bedöms var för sig."),
    ("Husgruppen", "Kulören stäms av mot grannhusen och detaljplanen."),
    ("Skriftligt kostnadsförslag", "Per hus eller per grupp när flera målas samtidigt."),
    ("Målning", "Tvätt, förarbete och strykning anpassad efter varje material."),
    ("Dokumentation", "Färgtyp, kulör och tillverkare lämnas efter arbetet."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Kista",
  "rot": [
    _ROT_VILLA + " I en bostadsrätt ger arbete på gemensamma ytor som fasader inget rotavdrag.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för fasadmålningen i Kista?",
  "price": [
    "Andelen trä och skivor som ska målas, förarbetets omfattning, antal hus i gruppen, kulörer och ställning. Efter ett gratis platsbesök får du eller föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Var det vanligt med atriumhus i Akalla?",
     "Stadens strategi Varsam nämner Akalla som ett av exemplen där det byggdes villor och atriumhus vid sidan av radhusen och kedjehusen."),
    ("Ska vårt radhus i Kista ha samma kulör som grannarnas?",
     "Färgsättningen i husgrupperna var enligt Varsam noga komponerad och enhetlig. Vi föreslår därför kulör utifrån gruppen och detaljplanen."),
    ("Varför ska tegel, trä och skivor bedömas var för sig?",
     "Materialen åldras olika och kräver olika förarbete. Riksantikvarieämbetet påpekar att man först måste veta hur den befintliga målningen är utförd och vad skadorna beror på."),
    ("Behöver gårdsväggarna i ett atriumhus målas lika ofta som de yttre?",
     "Inte nödvändigtvis. Väggar slits olika beroende på läge och väderstreck, och Riksantikvarieämbetet påpekar att söderfasader behöver målas oftare än norrfasader."),
  ],
  "sources": [_SPAR_KISTA, _VARSAM,
              ("Stockholms stad – Områdesfakta 2025: Kista (pdf)", _OF + "vasterort/jarva/kista.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Akalla (pdf)", _OF + "vasterort/jarva/akalla.pdf"),
              _RAA_MAL, _STH_FAS, _SKV, _SKV2],
  "cta": ("Ska huset i Kista målas om?", "Boka ett gratis platsbesök, så går vi igenom materialen och husgruppens kulörer innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Grupp av 1970-talsradhus med tegel och träpanel",
     "group of late 1970s Swedish terraced houses with a mix of yellow brick, stained wooden panel and fibre cement boards, coordinated colours within the group, pedestrian path and small gardens, northwest Stockholm suburb, summer" + _IMG_END),
    ("Atriumhus med gård och träfasad",
     "small enclosed courtyard of a 1970s Swedish single-storey atrium house with wooden facade panels painted in a muted red, glass doors facing the courtyard, potted plants, daylight" + _IMG_END),
    ("Träpanel och tegel i möte på en radhusfasad",
     "close view of a 1970s house facade where brick wall meets a painted wooden panel section, freshly repainted panel next to clean brick, daylight" + _IMG_END),
  ],
},
}
