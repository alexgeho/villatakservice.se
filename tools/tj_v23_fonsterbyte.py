# -*- coding: utf-8 -*-
"""Fönsterbyte – ortsidor v23: Kungsholmen, Vasastan, Östermalm, Hägersten, Solna, Sundbyberg (2026-10-26).
Hubb: fonsterbyte.html (TJ_HUB["fonsterbyte"]). Intent: byta fönster – skild från ortens fonsterrenovering-<ort>.html
(renovera befintliga bågar), som länkas i stället. Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.
Sidor i innerstaden har egen trust-rad (sidnyckel "trust"): rotavdrag ges inte för fönsterbyte i bostadsrätt.

Lokal vinkel per sida:
Kungsholmen – fönster i flerbostadshus är lovpliktig fasadändring (Stockholms stad), vad som räknas som ändring,
  stenstaden 1870–1930 och funkishusen i Fredhäll och Kristineberg omkring 1930, bostadsrätterna i områdesfakta,
  bostadsrättslagen 7 kap. 7 och 12 §§, handlingarna (fasad 1:100, NCS, detaljritning 1:10–1:50, foton).
Vasastan – storgårdskvarteren Röda Bergen och Motorn och Vingen (riksintresset, "ursprungliga byggnadselement såsom
  fönster"), MÖD 2019:25 om 20-talsklassicerande flerbostadshus (vad som ändrades), Stadsmuseets karta och
  rådgivning, bostadsrätterna i Västra Matteus, Gustav Vasa och Östra Matteus.
Östermalm – stenstaden där betydelsen för stadsmiljön väger tyngre än den enskilda byggnadens klass (gul klass),
  Lärkstaden 1909–1918 och Diplomatstaden (nationalstadsparken = utökad lovplikt), jugendhusets balkongdörrar
  (MÖD P 10515-17), bostadsrätterna i Oscars och Hedvig Eleonora.
Hägersten – villastaden Mälarhöjden (privat initiativ, trä, glasverandor, kulturhistoriskt värdefull, generösa
  byggrätter), kartans färger och ringar, spröjsdomen MÖD P 169-15, äldre handlingar och miljöprogram.
Solna – fasadändring i Solna (alltid lov för särskilt värdefullt, flerbostadshus mot allmän plats), handlingar med
  KA vid fönsterbyte och KUL/antikvarisk förundersökning, Råsundas och Solnas utpekade miljöer, fastighetsägarens
  medgivande.
Sundbyberg – Duvbo (Egna Hem 1898, 325 tomter, 98 till 1924, riksintresse 1987), utökad lovplikt för utbyte av
  fönster och kostnadsfri prövning, programmets råd, övriga Sundbyberg (flerbostadshus mot allmän plats), frivilligt lov.

Fakta endast från källorna i respektive 'sources', öppnade med curl/urllib (Mozilla-UA) 2026-10-26, alla svarade
200; pdf:erna (riksintressen, Varsam, områdesfakta, Duvbo) har textlager och lästes med pdftotext.
Strukna / ej använda: handläggningstider och avgifter, BBR:s U-värden (ingen primärkälla öppnad), att föreningen
alltid äger fönstren (lagen säger att stadgarna avgör – skrivet så), att Röda Bergens egna karaktärsdrag nämner
fönster (det gör listan för storgårdskvarteren och temat, skrivet så), MMD:s utgång i villamålet P 3853-15 (texten
avbruten), Engelbrekts församling (delvis utanför Östermalm). Inga priser, garantier, omdömen, egna uppdrag eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no text, no letters"
_TRUST_BRF = ["Gratis besök och kostnadsförslag", "Handlingar till bygglovet"]

_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"
_STH_FD = ("Stockholms stad – Fönster och dörrar", _SB + "fonster-och-dorrar/")
_STH_FBH = ("Stockholms stad – Flerbostadshus: yttre ändringar", _SB + "flerbostadshus/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 och 12 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_BV_MOD = ("Boverket – Fönsterbyten: bygglovsplikt och förvanskningsförbudet (MÖD 2019:25)",
           "https://www.boverket.se/sv/PBL-kunskapsbanken/teman/kulturvarden/kulturvarden-i-teori-och-praktik/rattsfall/fonsterbyten/")
_BV_SPROJS = ("Boverket – Rättsfall: Bygglov för fönsterbyte på enbostads-/gatuhus (MÖD P 169-15)",
              "https://www.boverket.se/sv/samhallsplanering/arkitektur-och-gestaltad-livsmiljo/arbetssatt/arkitektur-och-pbl/rattsfall/en--och-tvabostadshus/bygglov-for-fonsterbyte-pa-enbostads-gatuhus/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SOL_FAS = ("Solna stad – Fasadändring", "https://www.solna.se/bygga-bo--miljo/bygga/guide/vanliga-byggatgarder/fasadandring")
_SOL_KULT = ("Solna stad – Kulturmiljöer i Solna", "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna")
_SUN_FAS = ("Sundbybergs stad – Fasadändring",
            "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/fasadandring")
_SUN_DUVBO = ("Sundbybergs stad – Miljöprogram Duvbo (pdf)",
              "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf")

PAGES_TJ = {

# ------------------------------------------------------------------ KUNGSHOLMEN
"fonsterbyte-kungsholmen.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Kungsholmen", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte på Kungsholmen – stenhusen och funkishusen",
  "description": "Fönsterbyte på Kungsholmen: när nya fönster i flerbostadshus kräver bygglov, stenstaden och funkishusen i Fredhäll och Kristineberg, föreningen och ROT.",
  "h1": "Fönsterbyte på Kungsholmen",
  "lead": "På Kungsholmen gäller ett fönsterbyte i regel ett flerbostadshus, och då är det en fråga för bygglovet och för föreningen, inte bara för snickaren. Geal Entreprenad AB byter fönster i stenhusen kring Hantverkargatan och i funkishusen i Fredhäll och Kristineberg och tar fram underlaget innan något beställs.",
  "card": "Stenhusen, funkishusen och bygglovet.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "lov-kungsholmen", "anchor": "Bygglov",
     "h2": "Nya fönster i ett flerbostadshus är oftast lovpliktiga",
     "paras": [
       "Stockholms stad räknar att ändra eller sätta in nya fönster eller dörrar som exempel på lovpliktiga fasadändringar på ett flerbostadshus. Det beror på vilken byggnad och vilken fasad ändringen gäller, och staden bedömer utifrån de ändringar som föreslås i ansökan om de kräver lov och om de uppfyller kraven på utformning.",
       "Som ändring räknar staden bland annat att byta material eller kulör på fönstren, ändra storlek eller placering, flytta ett fönster från fasadlivet till ett indraget läge, ändra dimensioner, proportioner eller profilering på karmar, bågar och spröjsar, byta upphängning från sidohängt till vippfönster eller lägga till eller ta bort spröjs och mittpost. Ett hus kan också ha karaktäristiska fönster eller en tidstypisk indelning, och då påverkar en ändring både fasaden och byggnadens karaktär.",
     ],
     "aside": {"title": "Räknas som ändring", "items": [
       "Annat material eller kulör", "Ny storlek eller placering", "Andra profiler och spröjs",
       "Ny upphängning", "Ändrad indelning"]}},
    {"id": "husen-kungsholmen", "h2": "Stenstaden och 1930-talets funkishus",
     "paras": [
       "Stadens underlag om riksintressena beskriver den klassiska stenstaden som bebyggelse från 1870 till 1930 på Östermalm, Södermalm, Kungsholmen och Norrmalm. Hyreshusen är normalt fem våningar höga, står vid 18 meter breda gator och har tidstypiska, dekorerade fasader i puts eller natursten. Gatufasadernas tydliga uppdelning i sockelvåning och huvudfasad och husens byggnadsdetaljering räknas till de värdebärande karaktärsdragen.",
       "Omkring 1930 började en ny typ av stadsdelar byggas efter funktionalistiska ideal, och i innerstaden skedde det framför allt i utkanterna, till exempel i Fredhäll och Kristineberg. Där blev fristående huskroppar med öppna gröna gårdar idealet. Fönstren i ett stenhus från 1890-talet och i ett lamellhus från 1930-talet har alltså helt olika förlagor, och det nya fönstret ritas efter det hus det ska sitta i.",
     ],
     "aside": None},
    {"id": "foreningen-kungsholmen", "h2": "Föreningen beställer, stadgarna avgör",
     "paras": [
       "Enligt stadens områdesfakta för 2025 finns 30 369 bostadsrätter i flerbostadshus i Kungsholmens stadsdelsområde, mot 272 småhus med äganderätt. I Fredhäll är 2 219 bostäder bostadsrätter och i Kristineberg 3 230. Det är alltså i regel en bostadsrättsförening som byter fönstren, och ofta i hela huset på en gång.",
       "Bostadsrättslagen säger att bostadsrättshavaren håller lägenheten i gott skick om inte stadgarna bestämmer något annat, så det är stadgarna som visar vem som ansvarar för fönstren. Vill du själv ändra något krävs styrelsens tillstånd för en väsentlig förändring av lägenheten, och för en lägenhet med särskilda kulturhistoriska värden krävs tillstånd för varje åtgärd som påverkar ett sådant värde.",
     ],
     "aside": {"title": "Bra att ha till styrelsemötet", "items": [
       "Föreningens stadgar", "Foton på gatu- och gårdsfasad", "Husets äldre ritningar"]}},
    {"id": "handlingar-kungsholmen", "h2": "Ritningar, kulörer och foton",
     "paras": [
       "Till en ansökan om fasadändring hör en fasadritning i skala 1:100 med material och kulörer angivna i NCS-systemet, antingen på ritningen eller i en separat beskrivning. En detaljritning visar byggnadsdetaljer som fönster i skala 1:10, 1:20 eller 1:50, och fotografierna ska tydligt visa de sidor av huset som berörs. Staden ber också att plan-, fasad- och sektionsritningar stämmer med varandra.",
       "Äldre handlingar som stadsbyggnadskontoret har på fastigheten kan du själv söka fram och skriva ut i Bygg- och plantjänsten. Vi använder dem för att mäta upp de befintliga fönstren och rita de nya med samma indelning. Vill föreningen hellre behålla bågarna kan du läsa om " + _L.format("fonsterrenovering-kungsholmen.html", "fönsterrenovering på Kungsholmen") + ", och om tjänsten i stort under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett fönsterbyte på Kungsholmen till",
  "steps": [
    ("Platsbesök", "Vi ser fönstren, fasaderna och husets äldre ritningar tillsammans med styrelsen."),
    ("Uppmätning", "Befintliga karmar, bågar, profiler och indelning mäts och fotograferas."),
    ("Skriftligt kostnadsförslag", "Tillverkning, montage och efterarbete står var för sig."),
    ("Bygglov", "Fasadritning, detaljritning, kulörer och foton tas fram för ansökan."),
    ("Montage", "Fönstren byts lägenhet för lägenhet och drevas, tätas och fodras."),
    ("Genomgång", "Vi går igenom fönstren med föreningen och lämnar skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte på Kungsholmen",
  "rot": [
    "För en bostadsrätt ger Skatteverket inget rotavdrag för att byta fönster eller arbeta mellan och på utsidan av befintliga fönster. Avdrag ges för arbete på insidan, till exempel att byta glaset i den inre bågen, montera tätningslist eller byta innerfönster och fönsterfoder, när det är åtgärder som du ansvarar för enligt stadgarna.",
    "Äger du ett småhus på Kungsholmen gäller andra regler: där ger det rotavdrag att reparera eller byta ut fönster. Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år.",
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet på Kungsholmen?",
  "price": [
    "Antal fönster och fasader, om gatufasaden har en annan indelning än gårdsfasaden, profilerna, glas och beslag, ställning eller lift och om bygglovshandlingar behövs. Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver föreningen bygglov för att byta fönster på Kungsholmen?",
     "Oftast. Stockholms stad räknar att ändra eller sätta in nya fönster som exempel på lovpliktig fasadändring på flerbostadshus. Staden bedömer i det enskilda fallet utifrån vad som ändras."),
    ("Räknas det som en ändring om vi tar bort mittposten?",
     "Ja. Staden nämner ändrad indelning av fönster, till exempel att lägga till spröjs eller ta bort mittpost, som en förändring av fönstren."),
    ("Vem ansvarar för fönstren i vår bostadsrätt i Fredhäll?",
     "Det avgör föreningens stadgar. Bostadsrättslagen lägger ansvaret för lägenhetens skick på bostadsrättshavaren om inte stadgarna säger något annat."),
    ("Får vi rotavdrag för nya fönster i bostadsrätten på Kungsholmen?",
     "Nej, inte för själva fönsterbytet. Skatteverket ger avdrag bara för arbete på insidan av befintliga fönster, som nytt glas i den inre bågen eller tätningslist."),
    ("Hur visar vi fönstren i bygglovsansökan?",
     "Med fasadritning i 1:100, kulörer enligt NCS och en detaljritning i 1:10, 1:20 eller 1:50, plus foton av de fasader som berörs."),
  ],
  "sources": [_STH_FD, _STH_FBH, _RIKS, ("Stockholms stad – Områdesfakta 2025: Kungsholmens stadsdelsområde (pdf)", _OF + "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Fredhäll (pdf)", _OF + "inre-staden/kungsholmen/fredhall.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Kristineberg (pdf)", _OF + "inre-staden/kungsholmen/kristineberg1.pdf"),
              _BRL, _SKV, _SKV2],
  "cta": ("Ska fönstren i ert hus på Kungsholmen bytas?", "Boka ett gratis platsbesök, så går vi igenom fönstren och underlaget till bygglovet innan ni får ett skriftligt kostnadsförslag."),
  "img": [
    ("Stenhus från sekelskiftet med putsad fasad och rader av spröjsade fönster",
     "late 19th century Stockholm stone apartment building, five storeys, ornate light ochre plastered facade with a rusticated ground floor and rows of tall white wooden casement windows with transoms, quiet street with parked bicycles, overcast daylight" + _IMG_END),
    ("Funkishus i ljus puts med enkla fönster och gröna gårdar",
     "1930s Swedish functionalist apartment block, four storeys, smooth light grey plaster, simple white two-pane windows set in regular rows, open green lawn and pine trees in front, Stockholm, soft daylight" + _IMG_END),
    ("Nytt fönster med träkarm infällt i en tjock vägg av natursten",
     "close-up architectural detail of a newly installed white wooden casement window in a deep plastered window reveal of a thick old stone wall, fresh sealant along the frame, interior view, daylight through the glass" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VASASTAN
"fonsterbyte-vasastan.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Vasastan", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Vasastan – 1910- och 20-talens storgårdar",
  "description": "Fönsterbyte i Vasastan: storgårdskvarteren Röda Bergen och Motorn och Vingen, vad domstolen tittade på i ett 20-talshus, Stadsmuseets karta och ROT.",
  "h1": "Fönsterbyte i Vasastan",
  "lead": "I Vasastan står några av innerstadens mest helgjutna kvarter från 1910- och 1920-talen, och där är fönstren en del av det som ska bevaras. Geal Entreprenad AB byter fönster åt bostadsrättsföreningar i Vasastan och börjar med att ta reda på vad huset är och vad som får ändras.",
  "card": "Storgårdskvarteren och 20-talets fönster.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "storgardar-vasastan", "anchor": "Storgårdskvarteren",
     "h2": "Röda Bergen och Motorn och Vingen",
     "paras": [
       "Stadens underlag om riksintressena pekar ut Röda Bergen som innerstadens största miljö som helt präglas av 1910- och 1920-talets stadsbyggnadsidéer. Husen följer terrängen, gatorna är vinklade och planen reglerade var prydnadsgavlar skulle finnas och att gårdarna skulle vara öppna och planterade. Kvarteren Motorn och Vingen i norra Vasastaden uppfördes i slutet av 1910-talet som ett tidigt exempel på kooperativt byggande med kommunalt stöd.",
       "För storgårdskvarteren räknar underlaget den sammanhållna stadsbilden till de värdebärande karaktärsdragen, där proportioner, fasadindelning, taklandskap, färgsättning och ursprungliga byggnadselement såsom fönster, entréer och material bidrar till helheten. Staden skriver också att befintliga planer kan behöva kompletteras med hänsyn till de kulturhistoriska värdena.",
     ],
     "aside": {"title": "Utpekade i Vasastan", "items": [
       "Röda Bergen", "Motorn och Vingen", "Del av riksintresset för innerstaden"]}},
    {"id": "domen-vasastan", "h2": "Vad domstolen tittade på i ett 20-talshus",
     "paras": [
       "Boverket har refererat två domar från Mark- och miljööverdomstolen, bland dem MÖD 2019:25, om fönsterbyten i två 20-talsklassicerande flerbostadshus. Fönstren var sidhängda före och efter och indelningen var densamma, men trä hade ersatts av aluminiumklätt trä, kulören var ändrad, profilerna i karm, båge och spröjs var kantigare, mittposterna grövre och fast spröjs hade ersatts av löstagbar. I ett av husen hade okopplade bågar blivit kopplade.",
       "Domstolen ansåg att ändringarna knappt var märkbara från gatan och att de i de fallen inte krävde bygglov. Boverket påpekar att domarna bara säger att just de två bytena var lovfria, och att autenticitet, alltså ursprungligt material och detaljering, väger tungt inom kulturmiljövården. Listan visar ändå exakt vilka detaljer som granskas, och det är dem vi går igenom innan föreningen väljer fönster.",
     ],
     "aside": {"title": "Detaljer som granskades", "items": [
       "Material", "Kulör", "Profiler i karm, båge och spröjs", "Mittpostens bredd", "Fast eller löstagbar spröjs",
       "Kopplade eller okopplade bågar"]}},
    {"id": "kartan-vasastan", "h2": "Stadsmuseets karta och rådgivning",
     "paras": [
       "Stadsmuseets klassificeringskarta visar riksintressen med blå ring och klassificerade byggnader i blått, grönt, gult och grått. För en byggnad som är markerad blå eller grön, eller som ligger inom ett riksintresse, behöver du söka bygglov för åtgärder som annars kan vara lovfria. Streckade ytor är miljöer som ännu inte är inventerade.",
       "Är föreningen osäker kan ni maila Stadsmuseet med adress, fastighetsbeteckning och stadsdel, byggnadsår, eventuella ombyggnader och foton av fasaderna. Museet brukar svara inom tre veckor efter att det har fått alla uppgifter. Som byggherre ansvarar föreningen själv för att ta reda på vad som gäller för fastigheten.",
     ],
     "aside": None},
    {"id": "foreningar-vasastan", "h2": "Bostadsrätterna i Vasastan",
     "paras": [
       "Enligt stadens områdesfakta för 2025 finns 8 985 bostadsrätter i flerbostadshus i Västra Matteus, 5 693 i Gustav Vasa och 5 586 i Östra Matteus. Ett fönsterbyte är därför i regel ett beslut för en förening, och bostadsrättslagen kräver styrelsens tillstånd för en väsentlig förändring av en lägenhet och för varje åtgärd som påverkar ett kulturhistoriskt värde i lägenheten.",
       "Vi mäter upp de befintliga fönstren, ritar de nya med samma profiler och indelning och tar fram fasad- och detaljritningar till ansökan. Om bågarna i stället kan renoveras kan du läsa om " + _L.format("fonsterrenovering-vasastan.html", "fönsterrenovering i Vasastan") + ", och om tjänsten i stort under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
    {"id": 'efterhand-vasastan', "h2": 'Sök lov innan fönstren byts',
     "paras": [
       'I båda målen som Boverket refererar hade fastighetsägaren redan bytt fönstren, och kommunen hade avslagit ansökningarna om bygglov i efterhand. Ärendet gick sedan via länsstyrelsen och mark- och miljödomstolen till Mark- och miljööverdomstolen. Det är en lång väg att gå med fönster som redan sitter i fasaden.',
       'Stockholms stad påminner om att du inte får börja med det du sökt lov för innan du har fått startbesked, och att du får använda det du byggt först när du har fått slutbesked. Nya öppningar kan dessutom påverka byggnadens bärande konstruktion och behöva förstärkas, och en planritning behövs när fönster och dörrar flyttas eller nya installeras. Vi lägger därför in lovet i tidplanen från början.',
     ],
     "aside": {"title": 'Ordningen', "items": ['Ansökan', 'Startbesked', 'Montage', 'Slutbesked']}},
  ],
  "steps_h2": "Så går ett fönsterbyte i Vasastan till",
  "steps": [
    ("Husets status", "Stadsmuseets karta, riksintresset och detaljplanen kontrolleras."),
    ("Platsbesök", "Fönster, profiler, beslag och indelning dokumenteras på gata och gård."),
    ("Skriftligt kostnadsförslag", "Tillverkning, montage och efterarbete står var för sig."),
    ("Bygglov", "Fasad- och detaljritningar, kulörer och foton tas fram."),
    ("Montage", "Fönstren byts i etapper så att lägenheterna kan bo kvar."),
    ("Genomgång", "Vi går igenom fönstren med styrelsen."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Vasastan",
  "rot": [
    "Skatteverket ger inget rotavdrag för att byta fönster i en bostadsrätt, och inte heller för arbete mellan eller på utsidan av befintliga fönster. Avdrag ges för arbete på insidan, till exempel nytt glas i den inre bågen eller tätningslist, när du ansvarar för det enligt stadgarna.",
    "Arbetet ska utföras innanför bostadens tak, väggar och golv. Avdraget är högst 30 procent av arbetskostnaden, och material och resor ger inget avdrag.",
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet i Vasastan?",
  "price": [
    "Antal fönster, om gatu- och gårdsfasaderna har olika fönstertyper, profiler och spröjs, glas och beslag, ställning och om bygglovshandlingar behövs. Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för nya fönster i ett hus i Röda Bergen?",
     "Räkna med det. Röda Bergen ligger inom riksintresset för innerstaden, och för byggnader där krävs bygglov även för åtgärder som annars kan vara lovfria."),
    ("Får vi byta till aluminiumklädda fönster i ett 20-talshus i Vasastan?",
     "Det prövas i varje fall. I MÖD 2019:25 godtogs aluminiumklätt trä, men Boverket betonar att domen bara gäller de två fallen."),
    ("Hur länge brukar Stadsmuseet ta på sig att svara?",
     "Museet brukar svara inom tre veckor efter att det har fått alla uppgifter, enligt Stockholms stad."),
    ("Vad ska vi skicka till Stadsmuseet om vårt hus i Vasastan?",
     "Adress, fastighetsbeteckning och stadsdel, byggnadsår, eventuella ombyggnader med årtal och foton av fastigheten och fasaderna."),
    ("Kan vi få rotavdrag för att byta fönster i vår bostadsrätt i Vasastan?",
     "Nej. Skatteverket ger inget avdrag för fönsterbyte i bostadsrätt, bara för vissa arbeten på insidan av befintliga fönster."),
  ],
  "sources": [_RIKS, _BV_MOD, _STH_KL, _STH_FD,
              ("Stockholms stad – Områdesfakta 2025: Västra Matteus (pdf)", _OF + "inre-staden/norra-innerstaden/vastra-matteus.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Gustav Vasa (pdf)", _OF + "inre-staden/norra-innerstaden/gustav-vasa.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Östra Matteus (pdf)", _OF + "inre-staden/norra-innerstaden/ostra-matteus.pdf"),
              _BRL, _SKV, _SKV2],
  "cta": ("Ska fönstren i ert hus i Vasastan bytas?", "Boka ett gratis platsbesök, så går vi igenom husets status och fönstren innan ni får ett skriftligt kostnadsförslag."),
  "img": [
    ("Bostadshus från 1920-talet i rödaktig puts längs en svängd gata",
     "1920s Stockholm apartment buildings in classicist style with warm reddish and ochre plaster, small-paned white wooden windows and a decorative gable, following a gently curving and sloping street, autumn trees, daylight" + _IMG_END),
    ("Planterad bostadsgård omgiven av putsade hus med spröjsade fönster",
     "large planted courtyard of a 1920s Swedish apartment block, lawn, shrubs and old trees, surrounded by plastered facades with many small-paned white windows, calm afternoon light" + _IMG_END),
    ("Närbild på vitmålat fönster med spröjs och profilerade lister i en putsfasad",
     "close-up of a white painted wooden window sash with glazing bars and profiled mouldings on a 1920s Swedish facade, crisp shadows, plaster wall around" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERMALM
"fonsterbyte-ostermalm.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Östermalm", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte på Östermalm – stenstaden och Lärkstaden",
  "description": "Fönsterbyte på Östermalm: varför stadsmiljön väger tyngre än husets klass, Lärkstaden och Diplomatstaden, jugendhusets balkongdörrar och ROT i bostadsrätt.",
  "h1": "Fönsterbyte på Östermalm",
  "lead": "Ett stenhus på Östermalm kan ha gul klass i Stadsmuseets karta och ändå prövas noga när fönstren byts, eftersom det är gatan och kvarteret som ska bevaras. Geal Entreprenad AB byter fönster åt föreningar och fastighetsägare på Östermalm och utgår från husets egna fönster.",
  "card": "Stenstaden, Lärkstaden och villorna.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "stenstaden-ostermalm", "anchor": "Stenstaden",
     "h2": "Stadsmiljön väger tyngre än husets klass",
     "paras": [
       "Stadens underlag om riksintressena konstaterar att många byggnader i den klassiska stenstaden har relativt låg kulturhistorisk klassificering, gul klass, eftersom de har förändrats sedan de byggdes. Om alla sådana byggnader ersattes skulle stadsmiljön förlora sin historiska prägel, och därför ska betydelsen för stadsmiljön vara avgörande vid prövningen, inte den enskilda byggnadens klassificering.",
       "Bland de värdebärande karaktärsdragen nämns gatufasadernas tydliga uppdelning i sockelvåning och huvudfasad, ofta med markerad takfot, och byggnadsdetaljeringen. Mindre förändringar som vindsinredningar och inre modernisering prövas enligt varsamhetskraven i plan- och bygglagen. Ett fönster som ändrar fasadens rytm eller detaljering är därför en fråga även i ett gulklassat hus.",
     ],
     "aside": {"title": "Värdebärande i stenstaden", "items": [
       "Sockelvåning och huvudfasad", "Markerad takfot", "Byggnadsdetaljering", "Enhetlig höjdskala"]}},
    {"id": "larkstaden-ostermalm", "h2": "Lärkstaden och Diplomatstaden",
     "paras": [
       "Lärkstaden från 1909–1918 beskrivs som ett tidigt exempel på en terränganpassad, oregelbunden stadsplan med många tegelhus och planterade förgårdar, och större delen omfattas av en detaljplan från 1952 som reglerar byggrätten. Diplomatstaden byggdes på 1910- och 1920-talen med stora enfamiljshus i tegel kring Engelska kyrkan och skyddas genom miljöbalkens bestämmelser om nationalstadspark.",
       "Stockholms stad skriver att nationalstadsparken räknas in i riksintressena i Stadsmuseets karta, och att du behöver söka bygglov för åtgärder som annars kan vara lovfria om byggnaden ligger inom ett riksintresse för kulturmiljövården. Även nya fönster i en villa i Diplomatstaden kan därför kräva bygglov.",
     ],
     "aside": None},
    {"id": "dorrar-ostermalm", "h2": "Balkongdörrarna på ett jugendhus",
     "paras": [
       "Boverket refererar ett mål där fyra balkongdörrar på gatufasaden till ett jugendhus hade bytts. Material och färg var desamma, men de nya dörrarna hade grövre och klumpigare dimensioner och ändrade profiler. Byggnadsnämnden nekade bygglov i efterhand, och Mark- och miljööverdomstolen delade bedömningen att bytet var en förvanskning.",
       "Det är profilerna, dimensionerna och proportionerna som avgör, inte bara material och kulör. Vi mäter därför upp de befintliga fönstren och dörrarna och ritar de nya med samma mått på karm, båge och spröjs, så att föreningen kan visa hur de nya ska se ut redan i ansökan.",
     ],
     "aside": {"title": "Det som ändrades i dörrmålet", "items": [
       "Grövre dimensioner", "Ändrade profiler", "Samma material och färg"]}},
    {"id": "foreningen-ostermalm", "h2": "Föreningar och fastighetsägare på Östermalm",
     "paras": [
       "Stadens områdesfakta för 2025 visar 7 721 bostadsrätter i flerbostadshus i Oscars församlingsområde och 5 151 i Hedvig Eleonora, mot ett fåtal småhus. Det är styrelsen som beställer, och bostadsrättslagen kräver styrelsens tillstånd för varje åtgärd som påverkar en lägenhets särskilda kulturhistoriska värden.",
       "Till ansökan tar vi fram fasadritning i 1:100, detaljritning av fönstren i 1:10, 1:20 eller 1:50, kulörer enligt NCS och foton av de berörda fasaderna. Kan bågarna i stället renoveras finns mer under " + _L.format("fonsterrenovering-ostermalm.html", "fönsterrenovering på Östermalm") + ", och om tjänsten i stort under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
    {"id": 'taket-ostermalm', "h2": 'Takfönster i stenstadens taklandskap',
     "paras": [
       'Bland stenstadens värdebärande karaktärsdrag nämner stadens underlag sluttande tak, oftast plåttäckta, med en lutning på upp till 45 grader från fasaden, som ger ett karaktäristiskt taklandskap. Stockholms stad skriver att du ofta behöver bygglov för att sätta in nya takfönster, och att det beror på vilken byggnad och vilken fasad ändringen gäller.',
       'Ska vinden få nya fönster i samband med att gatufönstren byts tar vi med takfönstren i samma ansökan, med en takplan i skala 1:100 som visar både de nya fönstren och de befintliga installationerna på taket. Eftersom taklandskapet räknas till de värdebärande dragen ritar vi in takfönstren i fasadritningen också.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett fönsterbyte på Östermalm till",
  "steps": [
    ("Husets status", "Riksintresse, nationalstadspark, klass och detaljplan kontrolleras."),
    ("Uppmätning", "Fönster och dörrar mäts upp och fotograferas på gata och gård."),
    ("Skriftligt kostnadsförslag", "Tillverkning, montage och efterarbete står var för sig."),
    ("Bygglov", "Ritningar, kulörer och foton tas fram till ansökan."),
    ("Montage", "Fönster och dörrar byts i etapper och tätas och fodras."),
    ("Genomgång", "Vi går igenom resultatet med styrelsen eller fastighetsägaren."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte på Östermalm",
  "rot": [
    "I en bostadsrätt ger Skatteverket inget rotavdrag för att byta fönster, och inte heller för att arbeta mellan eller på utsidan av befintliga fönster. Arbete på insidan, som att byta innerfönster och fönsterfoder eller glaset i den inre bågen, kan ge avdrag om du ansvarar för det enligt stadgarna.",
    "För en villa som du äger och bor i, till exempel i Diplomatstaden, ger det rotavdrag att byta ut fönster. Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år.",
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet på Östermalm?",
  "price": [
    "Antal fönster och dörrar, profiler och spröjs, glas och beslag, om fönster ska tillverkas efter uppmätning, ställning mot gatan och om bygglovshandlingar behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vårt hus på Östermalm har gul klass – behöver vi ändå bygglov för nya fönster?",
     "Det kan ni behöva. Stenstaden ligger inom riksintresset för innerstaden, och staden skriver att betydelsen för stadsmiljön ska vara avgörande, inte den enskilda byggnadens klass."),
    ("Behövs bygglov för nya fönster i en villa i Diplomatstaden?",
     "Räkna med det. Diplomatstaden ligger inom nationalstadsparken, som räknas in i riksintressena, och där krävs bygglov för åtgärder som annars kan vara lovfria."),
    ("Kan nya balkongdörrar räknas som en förvanskning?",
     "Ja. I ett mål om ett jugendhus bedömdes dörrar med grövre dimensioner och ändrade profiler vara en förvanskning, trots samma material och färg."),
    ("Vem på Östermalm godkänner att en bostadsrättshavare byter fönster?",
     "Styrelsen. Bostadsrättslagen kräver tillstånd för varje åtgärd som påverkar en lägenhets särskilda kulturhistoriska värden."),
    ("Får vi rotavdrag för nya fönster i en bostadsrätt på Östermalm?",
     "Nej. Skatteverket ger inget avdrag för fönsterbyte i bostadsrätt, bara för vissa arbeten på insidan av fönstren."),
  ],
  "sources": [_RIKS, _STH_KL, _STH_FD, _BV_MOD,
              ("Stockholms stad – Områdesfakta 2025: Oscars församling (pdf)", _OF + "inre-staden/norra-innerstaden/oscars-kyrka.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hedvig Eleonora (pdf)", _OF + "inre-staden/norra-innerstaden/hedvig-eleonora.pdf"),
              _BRL, _SKV, _SKV2],
  "cta": ("Ska fönstren på Östermalm bytas?", "Boka ett gratis platsbesök, så mäter vi upp fönstren och går igenom husets status innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Stenhus med rusticerad bottenvåning och höga fönster längs en bred gata",
     "grand late 19th century Stockholm stone apartment building on a wide tree-lined boulevard, rusticated ground floor, light stone-coloured plaster, tall white wooden windows with transoms and small balconies, completely empty sidewalk without pedestrians, overcast daylight" + _IMG_END),
    ("Tegelhus från 1910-talet med småspröjsade fönster och planterad förgård",
     "1910s Swedish brick apartment house in national romantic style with small-paned white wooden windows, planted front garden with shrubs, gently sloping quiet street, early spring light" + _IMG_END),
    ("Balkongdörr i trä med smala profiler på en jugendfasad",
     "close-up of an elegant white wooden French balcony door with slim profiles and glazing bars on an Art Nouveau plastered facade with a wrought iron balcony railing, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HÄGERSTEN
"fonsterbyte-hagersten.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Hägersten", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Hägersten – villorna i Mälarhöjden",
  "description": "Fönsterbyte i Hägersten: villastaden Mälarhöjden, när kartan kräver bygglov för nya fönster, spröjsdomen, husets äldre ritningar och ROT för villan.",
  "h1": "Fönsterbyte i Hägersten",
  "lead": "I Hägersten står hundratals villor, och i Mälarhöjden är många av dem trähus med glasverandor och fönster från olika tider. Geal Entreprenad AB byter fönster i villor och radhus i Hägersten och tar reda på om bytet kräver lov innan fönstren beställs.",
  "card": "Villorna, kartan och spröjsen.",
  "sections": [
    {"id": "villastaden-hagersten", "anchor": "Mälarhöjden",
     "h2": "Villastaden Mälarhöjden",
     "paras": [
       "Stadens strategi för småhus- och villaområden beskriver hur villasamhällen som Mälarhöjden växte upp efter privata initiativ genom större markförvärv. Trä var det dominerande fasadmaterialet, även om puts förekom, och glasverandor, takkupor, snickarglädje och färgsättning gav stadsdelarna den variation som syns än i dag. I strategins tabell är Mälarhöjden markerad som kulturhistoriskt värdefull miljö och som område med generösa byggrätter.",
       "Enligt stadens områdesfakta för 2025 finns 988 småhus med äganderätt i Mälarhöjden och 955 i stadsdelen Hägersten. Villastäderna har förtätats successivt, så samma gata kan ha hus från flera decennier. Vi utgår därför från det hus som fönstren ska sitta i, inte från vad som var vanligt det år det byggdes.",
     ],
     "aside": {"title": "Mälarhöjden i stadens tabell", "items": [
       "Villastad", "Kulturhistoriskt värdefull miljö", "Generösa byggrätter"]}},
    {"id": "kartan-hagersten", "h2": "När ett fönsterbyte på villan kräver lov",
     "paras": [
       "Stockholms stad hänvisar till Stadsmuseets karta som en första indikation. Du behöver söka bygglov för åtgärder som annars kan vara lovfria om huset ligger inom ett område som översiktsplanen pekar ut som särskilt kulturhistoriskt värdefullt, grön ring i kartan, om det är markerat blått eller grönt eller om detaljplanen har skyddsbestämmelser. Är huset gult eller grått och inget annat gäller behövs inget lov.",
       "Staden räknar bland annat byte av material eller kulör, ändrad storlek, placering, profilering eller upphängning och ändrad indelning som förändringar av fönster. Byter du till exakt samma utseende är frågan enklare än om spröjsen försvinner eller sidohängda bågar blir vippfönster. Alla ändringar ska göras varsamt och med hänsyn till byggnadens karaktär.",
     ],
     "aside": {"title": "Bygglov kan krävas när", "items": [
       "Grön ring i kartan", "Huset är blått eller grönt", "Detaljplanen skyddar huset", "Streckat, ej inventerat område"]}},
    {"id": "sprojs-hagersten", "h2": "Spröjsen på ett 1970-talshus",
     "paras": [
       "Boverket refererar en dom från Mark- och miljööverdomstolen om ett enbostadshus från mitten av 1970-talet som byggts med spröjsade fönster i en miljö av riksintresse. Ägaren ville byta till fönster utan spröjs, men domstolen bedömde att det inte var en varsam ändring med hänsyn till husets karaktärsdrag, och att det inte hade visats några större kostnadsskillnader mellan fönster med och utan spröjs.",
       "Domstolen utgick från den aktuella byggnadens karaktärsdrag och inte från vad som var tidstypiskt för hus från 1970-talet. I en villastad med hus från många epoker är det just så vi tänker när vi föreslår fönster: samma indelning, samma proportioner och en profil som passar huset.",
     ],
     "aside": None},
    {"id": "ritningar-hagersten", "h2": "Husets ritningar och områdets miljöprogram",
     "paras": [
       "Äldre handlingar som stadsbyggnadskontoret har på fastigheten kan du söka fram i e-tjänsten Bygg- och plantjänsten. Staden har också äldre miljöprogram och typritningssamlingar som kan beställas. De har ingen juridisk status i bygglovsprövningen men ger kunskap om områdets karaktär, och strategin för småhus- och villaområden rekommenderas som stöd innan du söker lov.",
       "Vi mäter upp fönstren på plats och jämför med ritningarna, och behövs lov tar vi fram fasadritning, kulörer och foton. Om villans tak kan du läsa under " + _L.format("taklaggare-hagersten.html", "takläggare i Hägersten") + ", om fasaden under " + _L.format("fasadrenovering-hagersten.html", "fasadrenovering i Hägersten") + " och om tjänsten i stort under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
    {"id": 'insyn-hagersten', "h2": 'Nya öppningar i villan',
     "paras": [
       'Ska villan få ett nytt fönster där det inte fanns något förut påpekar Stockholms stad att nya fönster och ytterdörrar kan ge ökad insyn och bli en olägenhet för grannarna, och staden råder dig att informera grannen innan du söker lov. Nya öppningar kan också påverka husets bärande konstruktion så att den behöver förstärkas.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett fönsterbyte i Hägersten till",
  "steps": [
    ("Kartan", "Stadsmuseets karta och detaljplanen kontrolleras för fastigheten."),
    ("Platsbesök", "Fönster, verandor och karmar mäts upp och fotograferas."),
    ("Skriftligt kostnadsförslag", "Fönster, montage, foder och efterarbete står var för sig."),
    ("Bygglov", "Fasadritning, kulörer och foton när lov krävs."),
    ("Montage", "Fönstren byts, drevas och tätas, och foder och bleck sätts tillbaka."),
    ("Genomgång", "Vi går igenom fönstren och skötseln med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Hägersten",
  "rot": [
    "För ett småhus räknar Skatteverket att reparera eller byta ut fönster och montera bullerglas och isolerglas som rotarbete. Är bostaden yngre än fem år får arbetet bara återställa det ursprungliga skicket.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år, och material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet i Hägersten?",
  "price": [
    "Antal och storlek på fönstren, spröjs och indelning, glas och beslag, om fönstren tillverkas efter uppmätning, verandans fönster och om bygglov behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för nya fönster i vår villa i Mälarhöjden?",
     "Det beror på kartan och detaljplanen. Mälarhöjden är kulturhistoriskt värdefull miljö i stadens strategi, och ligger huset inom grön ring eller är markerat blått eller grönt krävs bygglov."),
    ("Vilka fönsterändringar räknar staden som förändring?",
     "Bland annat annat material eller kulör, ny storlek eller placering, andra profiler, ny upphängning och att lägga till spröjs eller ta bort mittpost."),
    ("Får vi ta bort spröjsen på vårt 70-talshus i Hägersten?",
     "Det kan vara svårt i en värdefull miljö. I en dom ansågs det inte varsamt att byta spröjsade fönster mot fönster utan spröjs på ett hus från mitten av 1970-talet."),
    ("Var hittar vi ritningar på vår villa i Hägersten?",
     "I Bygg- och plantjänsten kan du söka fram och skriva ut äldre handlingar som stadsbyggnadskontoret har på fastigheten."),
    ("Får vi rotavdrag för fönsterbytet på villan?",
     "Ja. Skatteverket räknar byte av fönster på småhus som rotarbete. Avdraget gäller arbetskostnaden."),
  ],
  "sources": [_VARSAM, ("Stockholms stad – Områdesfakta 2025: Mälarhöjden (pdf)", _OF + "soderort/hagersten/malarhojden.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hägersten (pdf)", _OF + "soderort/hagersten/hagersten.pdf"),
              _STH_KL, _STH_FD, _BV_SPROJS, _SKV, _SKV2],
  "cta": ("Ska fönstren i villan i Hägersten bytas?", "Boka ett gratis platsbesök, så går vi igenom fönstren och kartan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Trävilla med glasveranda och spröjsade fönster i en lummig trädgård",
     "early 1900s Swedish wooden villa painted pale yellow with white trim, a glazed veranda with many small window panes, mullioned white windows, lush garden with fruit trees on a slope, Stockholm suburb, summer daylight" + _IMG_END),
    ("Villagata med hus från olika decennier och klippta häckar",
     "quiet Swedish villa street on a hillside with houses from different decades, a 1920s wooden villa next to a 1950s brick house and a 1970s house, clipped hedges and picket fences, late summer" + _IMG_END),
    ("Nytt spröjsat träfönster i en panelvägg med nymålade foder",
     "close-up of a newly installed white wooden window with glazing bars in a painted wooden clapboard wall, freshly painted window trim and metal sill flashing, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SOLNA
"fonsterbyte-solna.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Solna", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Solna – Råsunda och föreningens ansökan",
  "description": "Fönsterbyte i Solna: när Solna kräver bygglov för nya fönster, kontrollansvarig och kulturvärdesutlåtande, Råsundas utpekade miljöer och ROT.",
  "h1": "Fönsterbyte i Solna",
  "lead": "Solna stad räknar nya fönster som en fasadändring, och i Råsundas stenstad och villastad kan det betyda bygglov, kontrollansvarig och ett utlåtande om kulturvärden. Geal Entreprenad AB byter fönster åt föreningar och villaägare i Solna och tar fram handlingarna som ansökan kräver.",
  "card": "Råsunda, bygglovet och handlingarna.",
  "sections": [
    {"id": "lov-solna", "anchor": "Bygglov",
     "h2": "När Solna kräver bygglov för nya fönster",
     "paras": [
       "Solna stad skriver att bygglov krävs i varje fall när fasadändringen görs på en byggnad som är särskilt värdefull eller ligger inom ett särskilt värdefullt område, och när detaljplanen anger att åtgärden kräver lov. Stora delar av Solna har detaljplan, och den kan också reglera hur byggnaderna ska se ut.",
       "Utan sådana skydd behövs inget bygglov för en fasadändring på ett en- eller tvåbostadshus, och inte heller när fasaden inte vetter mot allmän plats. För ett flerbostadshus där fönstren sitter mot gatan behöver föreningen därför räkna med en ansökan. Påverkar bytet konstruktion, brandskydd eller tekniska installationer krävs dessutom en anmälan.",
     ],
     "aside": {"title": "Bygglov krävs när", "items": [
       "Byggnaden är särskilt värdefull", "Området är särskilt värdefullt", "Detaljplanen kräver det"]}},
    {"id": "handlingar-solna", "h2": "Kontrollansvarig och kulturvärden i ansökan",
     "paras": [
       "Till en ansökan om fasadändring vill Solna ha situationsplan baserad på Solnakartan, fasadritning, planritning med åtgärden markerad, material- och kulörbeskrivning och förslag till kontrollplan. Staden anger att en kontrollansvarig kan behövas när ändringen även omfattar till exempel utbyte av fönster eller balkongfronter.",
       "Ibland behövs också en antikvarisk förundersökning eller ett utlåtande från en sakkunnig i kulturvärden, och fotografier där även grannfastigheterna syns. Staden påminner om att du som beställare ansvarar även om en leverantör utför arbetet. Vi tar fram ritningar och foton och samordnar med kontrollansvarig när en sådan krävs.",
     ],
     "aside": {"title": "Kan behövas i Solna", "items": [
       "Kontrollansvarig (KA)", "Utlåtande om kulturvärden", "Foton med grannhusen", "Förslag till kontrollplan"]}},
    {"id": "rasunda-solna", "h2": "Råsunda och Solnas utpekade miljöer",
     "paras": [
       "Solna stad listar ett antal sammanhängande kulturhistoriskt värdefulla miljöer där helhetsintrycket är det viktiga, bland dem Stenstaden i Råsunda, Råsunda villastad, villabebyggelsen i norra Råsunda och 1950-talsbebyggelsen i Råsunda, Skytteholm och Huvudsta. Även Hagalundshusen, de så kallade Blåkulla, och Bergshamra by finns med.",
       "Staden skriver att det i vissa fall är någon enstaka detalj på en byggnad som bedöms värdefull, i andra fall hela byggnaden. Kulturhistoriskt värdefulla byggnader och områden finns i Solnakartan, och där börjar vi innan vi föreslår hur de nya fönstren ska se ut.",
     ],
     "aside": None},
    {"id": "foreningen-solna", "h2": "Föreningen och fastighetsägaren",
     "paras": [
       "Solna stad påpekar att du behöver fastighetsägarens medgivande för byggåtgärder. Bor du i bostadsrätt är det föreningen, och bostadsrättslagen kräver styrelsens tillstånd för en väsentlig förändring av lägenheten. Ofta byter föreningen fönstren i hela huset i samma projekt.",
       "Ställ krav på att leverantören bygger enligt bygglovet, följer kontrollplanen och dokumenterar arbetet, råder staden, och glöm inte att begära slutbesked. Om renovering av befintliga bågar kan du läsa under " + _L.format("fonsterrenovering-solna.html", "fönsterrenovering i Solna") + ", och om tjänsten i stort under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
    {"id": 'beslutet-solna', "h2": 'Från beslut till slutbesked i Solna',
     "paras": [
       'När bygglovet är beviljat kungörs beslutet, och grannar och andra berörda har fyra veckor på sig att överklaga. Därefter vinner beslutet laga kraft. Arbetet måste påbörjas inom två år och avslutas inom fem år från den dagen, annars slutar lovet att gälla, och den som börjar utan startbesked kan få betala en byggsanktionsavgift.',
       'Kräver ändringen en kontrollansvarig håller byggnadsnämnden oftast ett tekniskt samråd, och mot slutet ett slutsamråd där kontrollansvarig redovisar hur kontrollplanen har följts. Solna påminner om att slutbeskedet krävs för att få använda det som byggts. Vi lämnar vår del av dokumentationen när fönstren är på plats.',
     ],
     "aside": {"title": 'Tidsgränser i Solna', "items": ['Fyra veckor till laga kraft', 'Påbörja inom två år', 'Avsluta inom fem år']}},
  ],
  "steps_h2": "Så går ett fönsterbyte i Solna till",
  "steps": [
    ("Solnakartan", "Detaljplan och kulturhistoriskt värdefulla byggnader kontrolleras."),
    ("Platsbesök", "Fönster, fasader och grannhus fotograferas och mäts upp."),
    ("Skriftligt kostnadsförslag", "Fönster, montage och efterarbete står var för sig."),
    ("Ansökan", "Ritningar, kulörer, foton och kontrollplan; KA och kulturvärden vid behov."),
    ("Montage", "Fönstren byts enligt lovet och kontrollplanen."),
    ("Slutbesked", "Dokumentationen lämnas så att slutbesked kan begäras."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Solna",
  "rot": [
    "För en villa eller ett radhus som du äger ger det rotavdrag att reparera eller byta ut fönster, enligt Skatteverket. I en bostadsrätt ges inget avdrag för att byta fönster, bara för vissa arbeten på insidan av befintliga fönster, som glaset i den inre bågen.",
    "Avdraget är högst 30 procent av arbetskostnaden. Rot- och rutavdraget är sammanlagt högst 75 000 kronor per person och år, varav högst 50 000 kronor rotavdrag.",
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet i Solna?",
  "price": [
    "Antal fönster och fasader, profiler och spröjs, glas och beslag, ställning, om kontrollansvarig eller kulturvärdesutlåtande behövs och hur mycket efterarbete som krävs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur länge gäller bygglovet för fönsterbytet i Solna?",
     "Arbetet ska påbörjas inom två år och avslutas inom fem år från att beslutet vann laga kraft, annars slutar lovet att gälla."),
    ("Behöver vår förening i Råsunda bygglov för nya fönster?",
     "Troligen. Stenstaden i Råsunda är utpekad som kulturhistoriskt värdefull miljö, och Solna kräver bygglov för fasadändring i särskilt värdefulla områden."),
    ("När krävs kontrollansvarig för fönsterbyte i Solna?",
     "Solna anger att en kontrollansvarig kan behövas när ändringen även omfattar till exempel utbyte av fönster eller balkongfronter."),
    ("Vad är ett utlåtande från sakkunnig kulturvärden?",
     "Ett utlåtande från en sakkunnig om hur åtgärden påverkar kulturvärdena. Solna kan begära det, eller en antikvarisk förundersökning, i ansökan."),
    ("Behövs bygglov för nya fönster i ett radhus i Solna?",
     "Inte om huset är ett en- eller tvåbostadshus som inte är särskilt värdefullt, ligger utanför särskilt värdefulla områden och detaljplanen inte kräver lov."),
    ("Var ser vi om vårt hus i Solna är kulturhistoriskt värdefullt?",
     "I Solnakartan, där staden visar kulturhistoriskt värdefulla byggnader och områden."),
  ],
  "sources": [_SOL_FAS, _SOL_KULT, _BRL, _SKV, _SKV2],
  "cta": ("Ska fönstren i Solna bytas?", "Boka ett gratis platsbesök, så går vi igenom fönstren och vad ansökan behöver innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Putsade flerbostadshus med jämna fönsterrader längs en gata med björkar",
     "1930s Swedish apartment buildings in light plaster on a hilly street with regular rows of white wooden windows, small front lawns and birch trees, Solna, soft autumn daylight" + _IMG_END),
    ("Villa i puts med tegeltak och spröjsade fönster bakom en häck",
     "small 1920s Swedish plastered villa with red clay tile roof and white small-paned windows behind a clipped hedge, quiet residential street on a slope, summer" + _IMG_END),
    ("Fasadritning med fönster, linjaler och kulörprover på ett bord",
     "architectural facade drawing and a window detail drawing spread on a wooden table with a folding ruler and colour samples, soft window light, no readable text" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SUNDBYBERG
"fonsterbyte-sundbyberg.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Sundbyberg", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Sundbyberg – Duvbo och flerbostadshusen",
  "description": "Fönsterbyte i Sundbyberg: utökad lovplikt för fönster i Duvbo, miljöprogrammets råd, flerbostadshus mot allmän plats, frivilligt bygglov och ROT.",
  "h1": "Fönsterbyte i Sundbyberg",
  "lead": "I Duvbo kräver ett fönsterbyte bygglov, men prövningen är kostnadsfri. I resten av Sundbyberg beror det på huset och vilken fasad fönstren sitter i. Geal Entreprenad AB byter fönster i villor i Duvbo och åt föreningar i hela Sundbyberg.",
  "card": "Duvbo, flerbostadshusen och lovet.",
  "sections": [
    {"id": "duvbo-sundbyberg", "anchor": "Duvbo",
     "h2": "Duvbo, en av landets första egnahemsmiljöer",
     "paras": [
       "Stadens miljöprogram för Duvbo berättar att föreningen Egna Hem bildades 1898 för att skapa egna hem för arbetare, köpte egendomen Dufvebol i Spånga församling året därpå och gjorde en stadsplan med 325 tomter. 1924 utökades området västerut med ytterligare 98 villatomter. Riksantikvarieämbetet pekade 1987 ut Duvbo som riksintresse för kulturmiljövården.",
       "Husen är framför allt byggda vid sekelskiftet 1900 och under 1920-talet, med senare hus från 1930- och 1940-talen. Programmet beskriver sekelskiftesvillorna med fasader i fält av stående och liggande panel och snickarglädje, 1920-talsvillorna som enklare med locklistpanel och 1940-talets hus som slätputsade volymer med få detaljer.",
     ],
     "aside": {"title": "Duvbo i årtal", "items": [
       "1898: föreningen Egna Hem", "325 tomter i första planen", "1924: 98 tomter till", "1987: riksintresse"]}},
    {"id": "lovplikt-sundbyberg", "h2": "Utökad lovplikt för fönster i Duvbo",
     "paras": [
       "I samband med en planändring för Duvbo utökades bygglovsplikten. Den omfattar bland annat utbyte, flyttning eller igensättning av fönster och dörrar, utbyte av fasadbeklädnad och takmaterial, omfärgning och andra ändringar som påverkar byggnadens yttre utseende. Åtgärder inom den utökade lovplikten är kostnadsfria.",
       "Programmet ger också råd: vid underhåll och andra förändringar ska utförande och material om möjligt väljas i överensstämmelse med originalet eller husets tillkomsttid, och byggnadens tidstypiska uttryck får inte förvanskas genom byte av fönster. Äldre hus som har förändrats kraftigt bör enligt programmet om möjligt anpassas bättre till omgivningen i samband med andra åtgärder, och ett fönsterbyte är ett sådant tillfälle. Vi börjar därför med att dokumentera de fönster som finns och föreslår nya med samma indelning och proportioner.",
     ],
     "aside": {"title": "Kräver lov i Duvbo", "items": [
       "Utbyte av fönster och dörrar", "Flytt eller igensättning", "Ny fasadbeklädnad eller takmaterial", "Omfärgning"]}},
    {"id": "ovriga-sundbyberg", "h2": "Fönster i resten av Sundbyberg",
     "paras": [
       "Sundbybergs stad räknar nya fönster och dörrar, eller ändring av befintliga, som fasadändring. För ett en- eller tvåbostadshus krävs inte längre bygglov, förutsatt att huset inte är kulturhistoriskt värdefullt eller ligger i ett särskilt värdefullt bebyggelseområde som Duvbo. För flerbostadshus och andra byggnader krävs bygglov om ändringen görs på en fasad eller ett tak som vetter mot allmän plats.",
       "Även när lov inte krävs kan en anmälan behövas om konstruktionen av bärande delar eller brandskyddet påverkas väsentligt, och då ska startbeskedet ha kommit innan arbetet börjar. Vill du vara säker kan du söka frivilligt bygglov, som enligt staden kostar lika mycket som ett vanligt bygglov.",
     ],
     "aside": None},
    {"id": "handlingar-sundbyberg", "h2": "Handlingarna till ansökan",
     "paras": [
       "Ansökan görs i stadens e-tjänst. Oftast krävs situationsplan som tydligt visar var åtgärden utförs, plan- och fasadritning, kulör- och materialbeskrivning och kontrollplan, och i vissa fall en detaljritning. Ritningarna ska vara fackmannamässigt utförda och skalenliga.",
       "Som byggherre ansvarar du för att lagstiftningen följs även när ingen ansökan krävs. Vi tar fram ritningar och foton och stämmer av fönstren mot husets ålder. Om tjänsten i stort kan du läsa under " + _L.format("fonsterbyte.html", "fönsterbyte") + ", och om fasaden under " + _L.format("fasadrenovering-sundbyberg.html", "fasadrenovering i Sundbyberg") + ".",
     ],
     "aside": None},
    {"id": 'kontrollplan-sundbyberg', "h2": 'Kontrollplanen för fönsterbytet',
     "paras": [
       'Sundbybergs stad beskriver kontrollplanen som en förteckning över de kontroller byggherren ska göra och vem som gör dem. Förslaget lämnas in med bygglovsansökan och ska då inte vara ifyllt eller undertecknat, eftersom det bara visar vilka kontroller som ska göras. I enklare ärenden kan startbeskedet ges samtidigt som bygglovet.',
       'När fönstren sitter skickas kontrollplanen in bestyrkt och underskriven, och därefter handläggs slutbeskedet. Med det avslutas ärendet hos staden. Vi fyller i våra kontrollpunkter för montage, tätning och drevning så att du har dem klara när slutbeskedet ska begäras.',
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett fönsterbyte i Sundbyberg till",
  "steps": [
    ("Platsbesök", "Fönster, fasader och husets tillkomsttid går vi igenom."),
    ("Dokumentation", "Befintliga fönster mäts upp och fotograferas."),
    ("Skriftligt kostnadsförslag", "Fönster, montage och efterarbete står var för sig."),
    ("Ansökan", "Ritningar, kulörer och kontrollplan i Duvbo eller mot allmän plats."),
    ("Montage", "Fönstren byts, drevas och tätas och foder sätts tillbaka."),
    ("Genomgång", "Vi går igenom fönstren och lämnar kontrollplanen ifylld."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte i Sundbyberg",
  "rot": [
    "Skatteverket räknar att reparera eller byta ut fönster på ett småhus som rotarbete, så en villa i Duvbo ger avdrag för arbetskostnaden. I en bostadsrätt ges inget avdrag för att byta fönster, bara för arbete på insidan av befintliga fönster som du ansvarar för enligt stadgarna.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fönsterbytet i Sundbyberg?",
  "price": [
    "Antal fönster, om de tillverkas efter uppmätning med spröjs och profiler, glas och beslag, ställning och om bygglovshandlingar behövs. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver fönsterbytet i Sundbyberg anmälas?",
     "Bara om det väsentligt påverkar konstruktionen av byggnadens bärande delar eller brandskyddet. Då ska startbeskedet ha kommit innan arbetet börjar."),
    ("Vilka hus i Duvbo är äldst?",
     "Enligt miljöprogrammet är husen framför allt byggda vid sekelskiftet 1900 och under 1920-talet. Senare tillkom enklare putsade hus på 1930- och 1940-talen."),
    ("Måste kontrollplanen vara undertecknad när vi söker lov i Sundbyberg?",
     "Nej. Förslaget till kontrollplan ska inte vara ifyllt eller undertecknat i bygglovsskedet. Den undertecknade planen skickas in när arbetet är klart."),
    ("Kostar bygglovet för nya fönster i Duvbo något?",
     "Nej. Enligt miljöprogrammet är åtgärder inom den utökade lovplikten i Duvbo kostnadsfria."),
    ("Behöver jag bygglov för att sätta igen ett fönster på villan i Duvbo?",
     "Ja. Den utökade lovplikten omfattar utbyte, flyttning eller igensättning av fönster och dörrar."),
    ("Behöver vår förening i Sundbyberg bygglov för nya fönster?",
     "Om fönstren sitter på en fasad som vetter mot allmän plats, till exempel gatan, krävs bygglov för flerbostadshus enligt staden."),
    ("Kan jag söka bygglov frivilligt i Sundbyberg?",
     "Ja. Ett frivilligt bygglov prövar om åtgärden följer lagens krav och kostar lika mycket som ett vanligt bygglov."),
    ("Får jag rotavdrag för fönsterbytet på villan i Duvbo?",
     "Ja, för arbetskostnaden. Skatteverket räknar byte av fönster på småhus som rotarbete."),
  ],
  "sources": [_SUN_DUVBO, _SUN_FAS, _SKV, _SKV2],
  "cta": ("Ska fönstren i Sundbyberg bytas?", "Boka ett gratis platsbesök, så går vi igenom fönstren och lovfrågan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla i trä med panel i fält och spröjsade fönster bland stora träd",
     "Swedish wooden villa from around 1900 with facade divided into fields of vertical and horizontal panelling, decorative carpentry, small-paned white windows, red clay tile roof, large old trees and a picket fence, summer" + _IMG_END),
    ("Trävilla med stående panel, takkupa och tak av rött lertegel bland fruktträd",
     "1920s Swedish wooden villa with board-and-batten facade, mansard roof with red clay tiles, simple white windows, garden with fruit trees on a slope, daylight" + _IMG_END),
    ("Närbild på spröjsad fönsterbåge i trä på en panelfasad",
     "close-up of an old style white painted wooden window with six panes and glazing bars set in a painted wooden panel facade with decorative trim, soft daylight" + _IMG_END),
  ],
},
}
