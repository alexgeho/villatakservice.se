# -*- coding: utf-8 -*-
"""Fönsterrenovering – ortsidor v24: Enskede, Älvsjö, Spånga, Hägersten, Vällingby, Österåker (2026-10-26).
Deltjänst under fonsterbyte.html (TJ_HUB["fonsterrenovering"]). Intent: renovera de befintliga fönstren (kitt,
linoljefärg, bågar, spröjs, bottenstycken, beslag, tätning, innerbåge) i stället för att byta dem. Skild från ortens
fonsterbyte-<ort>.html (Hägersten, Österåker) och från v16/v19/v21-sidorna.

Lokal vinkel per sida:
Enskede – Gamla Enskedes fönster enligt Varsam (grunt placerade två- och treluftsfönster med stående proportioner,
  småspröjs ovanför tvärposten, dovare kulör på putsade hus), riksintresset och Stockholms lista över ändringar som
  kräver lov, RAÄ om spröjsarnas återkomst 1900–1930, linoljekitt.
Älvsjö – villastadens fönster i Stadsmuseets inventering (småspröjsade fönster med luckor, ritning 1913–14, färgtonen
  som Hem på landet godkände), RAÄ om kopplade inåtgående bågar från sekelskiftet, luckor och beslag, värdefull miljö.
Spånga – Solhem och villastäderna, Hem på landet som återanvände ritningar från Solhem (Stadsmuseets inventering av
  Älvsjö), Stockholms lista (upphängning, spröjs, mittpost), RAÄ om tätningslister och tillsatsrutor i stället för byte.
Hägersten – fönster från flera epoker i Mälarhöjden (villastad, värdefull miljö): RAÄ om spröjs fram till 1930, hel
  glasruta på 1930-talet och lim i fönstren från 1930-talet; renovering efter ålder.
Vällingby – tunnelbanestadens radhus och kedjehus (regelbunden fönstersättning, Atlantis och Omega, riksintresset),
  bostadsrätt eller äganderätt (stadgarna, Skatteverkets regler för insida och utsida), 1950-talets fönster med hel ruta.
Österåker – sommarvillorna i Svinninge, Svinningeudd och Nantes (Råd och riktlinjer 2008): enkla bågar och lösa
  innerbågar på gångjärn, kärnvirke, byt bara rötskadade delar, kopior i stället för standardfönster, glasverandornas
  handblåsta glas, fönsterbågar i engelskt rött, grönt eller brunt; kommunens krav på lov även för underhåll i
  särskilt värdefulla områden.

Fakta endast från källorna i respektive 'sources', öppnade med curl/urllib (Mozilla-UA) 2026-10-26, alla 200;
pdf:erna (Varsam, områdesfakta, RAÄ Fönster, Stadsmuseets inventering, Svinninge) har textlager.
Strukna / ej använda: metylenklorid som färgborttagning (nämns av RAÄ men rekommenderas inte här), Stadsmuseets
svarstid, avgifter, vilka hus i Mälarhöjden som har vilka fönster (ingen källa), alla priser, garantier, omdömen,
egna uppdrag i orterna och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no text, no letters"

_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/"
_STH_FD = ("Stockholms stad – Fönster och dörrar", _SB + "fonster-och-dorrar/")
_STH_KL = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_RAA_F = ("Riksantikvarieämbetet – Fönster. Historik och råd vid renovering (pdf)", "https://www.raa.se/publicerat/9789172095892.pdf")
_ALV_INV = ("Stadsmuseet – Inventering av Älvsjö villastad (Stockholmskällan, pdf)",
            "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005549_01.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 12 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_OST_SVIN = ("Österåkers kommun – Råd och riktlinjer för byggande i Svinninge (pdf)",
             "https://www.osteraker.se/download/18.5bb0400617c11d33b5536/1632390824156/rad_och_vagledning_svinninge.pdf")
_OST_KULT = ("Österåkers kommun – Kulturhistoriska byggnader, kulturmiljöer",
             "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/bygglovsguiden/kulturhistoriskabyggnaderkulturmiljoer.4.367d658917909e8fc2bb42.html")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
            "tillsammans med rutavdrag. Material och resor ger inget avdrag.")
_ROT_SMA = "Skatteverket räknar reparation av fönster och målning av fönster på ett småhus som rotarbete."

PAGES_TJ = {

# ------------------------------------------------------------------ ENSKEDE
"fonsterrenovering-enskede.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Enskede", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Enskede – trädgårdsstadens fönster",
  "description": "Fönsterrenovering i Enskede: Gamla Enskedes fönster med småspröjs, lovet i riksintresset, linoljekitt och linoljefärg och tätning utan nya bågar.",
  "h1": "Fönsterrenovering i Enskede",
  "lead": "I Gamla Enskede är fönstren en av de detaljer som gör trädgårdsstaden till riksintresse, och de flesta går att renovera i stället för att bytas. Geal Entreprenad AB renoverar fönster i villor och radhus i Gamla Enskede, Enskededalen och Enskedefältet och behåller bågarnas mått och spröjsar.",
  "card": "Trädgårdsstadens fönster.",
  "sections": [
    {"id": "fonstren-enskede", "anchor": "Fönstren",
     "h2": "Fönstren i Gamla Enskede",
     "paras": [
       "Stadens strategi för småhusområden beskriver fönstren i Gamla Enskede: de sitter grunt i förhållande till fasadlivet och är oftast två- eller treluftsfönster med stående proportioner. Ovanför tvärposten är rutorna i många fall småspröjsade. På de putsade husen bygger färgsättningen på kontrast mellan fasad och fönstersnickerier, som ofta har en dovare kulör.",
       "Gamla Enskede anlades efter Per Olof Hallmans stadsplan från 1908, och det nationalromantiska inslaget med fönster med småspröjsade rutor blev tydligt där. Strategin räknar ursprungliga byggnadsdetaljer som fönster, entrédörrar och räcken till trädgårdsstädernas karaktärsdrag.",
     ],
     "aside": {"title": "Typiskt för Gamla Enskede", "items": [
       "Grunt placerade fönster", "Två- och treluftsfönster", "Småspröjs ovanför tvärposten", "Dovare kulör på snickerierna"]}},
    {"id": "sprojsen-enskede", "h2": "Spröjsar som kom tillbaka",
     "paras": [
       "Riksantikvarieämbetet beskriver hur glasformaten växte under 1800-talet tills spröjsarna inte behövdes. Kring sekelskiftet och fram till 1930 kom stilideal med historiska förebilder, och spröjsarna kom tillbaka. Det är den tiden Gamla Enskedes fönster hör till.",
       "Spröjsarna är ofta smäckra och det är där rötskador och lös kitt syns först. Vid en renovering byts bara skadade spröjsar och delar av bågen, med nytt virke som skarvas in efter det gamla. Profilerna behålls, så att fönstret ser likadant ut efteråt.",
     ],
     "aside": None},
    {"id": "lovet-enskede", "h2": "Renovering eller ändring",
     "paras": [
       "Stockholms stad räknar upp vilka ändringar av fönster som kan kräva bygglov: byte av material eller kulör, ändrade dimensioner, proportioner eller profiler på karmar, bågar och spröjsar, ändrad upphängning och ändrad indelning, till exempel att lägga till spröjs eller ta bort mittpost. Gamla Enskede är riksintresse för kulturmiljövården, och där krävs bygglov för åtgärder som annars är lovfria.",
       "En renovering som behåller material, kulör, mått och indelning ändrar inte fönstret och är underhåll. Det är ett av skälen till att renovering ofta är den enklaste vägen i Gamla Enskede. Om fasaderna i stadsdelen kan du läsa under " + _L.format("fasadrenovering-enskede.html", "fasadrenovering i Enskede") + ".",
     ],
     "aside": {"title": "Kan kräva lov enligt staden", "items": [
       "Nytt material eller ny kulör", "Ändrade profiler och spröjsar", "Ändrad upphängning", "Ny indelning av fönstret"]}},
    {"id": "kittet-enskede", "h2": "Linoljekitt och linoljefärg",
     "paras": [
       "Riksantikvarieämbetet rekommenderar linoljefärg vid utvändig fönstermålning, både vid renovering och nymålning. Linoljefärgen tränger in i virket och fäster väl, medan latexfärger lägger sig som en film på ytan. Till kittning av gamla fönster rekommenderas linoljekitt eller annat kitt på vegetabilisk oljebas, och falsen ska vara rengjord och grundad innan kittet läggs.",
       "Normalt räcker det att kitta om bågens nedre del. Målningen görs med grundning, mellanstrykning och slutstrykning, och partier där färgen sitter bra slipas i stället för att grundas. Om fönsterbyte i stort kan du läsa under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
    {"id": "tatningen-enskede", "h2": "Tätare utan nya bågar",
     "paras": [
       "Riksantikvarieämbetet skriver att dagens tätningslister är väl lämpade för gamla fönster och ger en avsevärd förbättring av både ljud- och värmeisolering. Det är innerbågen, inte ytterbågen, som ska tätas, och fönstret ska målas och justeras innan listerna sätts upp.",
       "Med rätt tätningslist och tillsatsruta blir ett gammalt fönster enligt Riksantikvarieämbetet lika energisnålt som ett nytt. Enligt stadens områdesfakta för 2025 finns 898 småhus med äganderätt i Gamla Enskede, och i många av dem sitter fönster som går att ta hand om på det sättet. Vi börjar med att se på varje fönster för sig.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Enskede till",
  "steps": [
    ("Inventering", "Varje fönster besiktigas för sig: virke, kitt, färg och beslag."),
    ("Skriftligt kostnadsförslag", "Fönster för fönster, så att du ser vad som behöver göras."),
    ("Snickerireparationer", "Skadade spröjsar och bottenstycken byts med nytt virke som skarvas in."),
    ("Kittning och målning", "Linoljekitt och linoljefärg i grundning, mellan- och slutstrykning."),
    ("Tätning och beslag", "Innerbågen tätas, bågarna justeras och beslag kompletteras."),
    ("Genomgång", "Vi går igenom fönstren och skriver ner kulör och material."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Enskede",
  "rot": [
    _ROT_SMA + " Du ska äga huset när arbetet utförs.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Enskede?",
  "price": [
    "Antalet fönster och bågar, mängden spröjs, hur mycket virke som behöver bytas, om bågarna renoveras på plats eller i verkstad och om innerbågen ska kompletteras. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov för att renovera fönstren i Gamla Enskede?",
     "Inte om fönstren behåller material, kulör, mått och indelning. Ändringar av till exempel spröjs, profiler eller kulör kan kräva lov i riksintresset."),
    ("Vilken färg ska fönstren i Gamla Enskede målas med?",
     "Riksantikvarieämbetet rekommenderar linoljefärg utvändigt. Kulören stämmer vi av mot husets fasad, eftersom snickerierna på putsade hus ofta har en dovare kulör."),
    ("Kan gamla fönster bli lika täta som nya?",
     "Enligt Riksantikvarieämbetet blir ett gammalt fönster lika energisnålt som ett nytt med rätt tätningslist och tillsatsruta."),
    ("Behöver hela fönstret kittas om?",
     "Normalt räcker det att kitta om bågens nedre del, enligt Riksantikvarieämbetet. Vid större reparationer tas allt gammalt kitt loss."),
  ],
  "sources": [_VARSAM, _STH_FD, _STH_KL, _RAA_F,
              ("Stockholms stad – Områdesfakta 2025: Gamla Enskede (pdf)", _OF + "soderort/enskede/gamla-enskede.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska fönstren i Enskede renoveras?", "Boka ett gratis platsbesök, så går vi igenom fönstren ett och ett innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Treluftsfönster med småspröjs i en rödfärgad trävägg",
     "old Swedish national romantic three-light wooden window with small panes above the transom, painted white, set almost flush in a falu red board facade, garden city house, summer" + _IMG_END),
    ("Fönsterbåge i verkstad med nytt virke inskarvat i nederdelen",
     "old wooden window sash on a workbench with a new piece of pine spliced into the bottom rail, glass removed, linseed putty and putty knife beside it, workshop light" + _IMG_END),
    ("Nykittat fönster med linoljefärg i dov grön kulör",
     "close view of a freshly puttied and painted old window sash in muted dark green linseed oil paint, small panes with old slightly wavy glass, rendered wall around, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"fonsterrenovering-alvsjo.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Älvsjö", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Älvsjö – småspröjs och fönsterluckor",
  "description": "Fönsterrenovering i Älvsjö: villastadens småspröjsade fönster med luckor, kopplade inåtgående bågar, kitt, linoljefärg och beslag.",
  "h1": "Fönsterrenovering i Älvsjö",
  "lead": "Villorna i Älvsjö villastad byggdes på 1910-talet med småspröjsade fönster och ofta fönsterluckor, och många av dem finns kvar. Geal Entreprenad AB renoverar fönster i villor i Älvsjö, Långbro, Herrängen och Långsjö och tar hand om bågar, luckor och beslag i samma arbete.",
  "card": "Småspröjs och fönsterluckor.",
  "sections": [
    {"id": "villorna-alvsjo", "anchor": "Villorna",
     "h2": "Villastadens fönster",
     "paras": [
       "Stadsmuseets inventering av Älvsjö villastad visar en ritning till en villa uppförd 1913–1914, som representerar en vanlig villatyp i Älvsjö i mitten av 1910-talet: slätputsad bottenvåning, gavelspetsar med panel på förvandring och småspröjsade fönster med luckor. En annan vanlig typ hade falurödfärgad träpanel och vitmålade snickerier.",
       "Inventeringen berättar också att bolaget AB Hem på landet, som sålde tomterna, ville godkänna den yttre färgtonen för att undvika oharmoniska färger mellan grannhusen. Båda hustyperna finns enligt inventeringen kvar i nästan helt ursprungligt skick.",
     ],
     "aside": {"title": "Villatyp från 1910-talet", "items": [
       "Slätputsad bottenvåning", "Panel på förvandring i gavlarna", "Småspröjsade fönster", "Fönsterluckor"]}},
    {"id": "bagarna-alvsjo", "h2": "Kopplade bågar som öppnas inåt",
     "paras": [
       "Riksantikvarieämbetet beskriver hur kopplade, inåtgående fönsterbågar blev allt vanligare från sekelskiftet. När de kopplade bågarna öppnas inåt utesluts mittposten, och den inre bågen blir den bärande som den yttre hänger på. Därför görs den inre bågen ofta kraftigare.",
       "De äldre kopplade bågarna kan vara stora och tunga, med igengrodda kopplingsbeslag och skevheter, skriver Riksantikvarieämbetet. Vid en renovering lossar vi bågarna från varandra, rengör och justerar beslagen och kompletterar med nya handtag och stängningsbeslag där de gamla inte fungerar.",
     ],
     "aside": None},
    {"id": "luckorna-alvsjo", "h2": "Luckor och beslag",
     "paras": [
       "Fönsterluckorna sitter ute i väder året runt och har ofta samma skador som bågarna: släppt färg, sprickor och röta i nederkanten. Vi tar ner luckorna, lagar skadat trä, målar dem och sätter tillbaka dem med justerade gångjärn och hakar.",
       "Riksantikvarieämbetet påpekar att lämpliga beslag av äldre typ kan vara svåra att få tag på och råder att inte kasta gamla fönsterbeslag. Hörnbeslag av äldre typ har stor betydelse för fönstrets styrka och karaktär och bör användas som de var tänkta. Vi rengör och återanvänder de beslag som går.",
     ],
     "aside": {"title": "Det vi tar hand om", "items": [
       "Bågar och spröjsar", "Kitt och färg", "Fönsterluckor", "Beslag och hörnjärn"]}},
    {"id": "fargtonen-alvsjo", "h2": "Färgtonen och linoljefärgen",
     "paras": [
       "Eftersom Hem på landet ville godkänna villornas yttre färgton hörde fönstrens kulör till helheten redan från början. Vid en renovering skrapar vi fram äldre färglager på bågar och foder för att se vilken kulör fönstren haft, innan ny färg väljs.",
       "Linoljefärg torkar genom att ta upp syre ur luften och fyller porer och ojämnheter bättre än andra färger, skriver Riksantikvarieämbetet. Den torkar långsamt, men när den åldras vittrar den på ett sätt som ger goda förutsättningar för nästa underhållsmålning.",
     ],
     "aside": None},
    {"id": "kartan-alvsjo", "h2": "Värdefull miljö",
     "paras": [
       "I stadens strategi för småhusområden är delar av Älvsjö markerade som kulturhistoriskt värdefull miljö. Stockholms stad räknar upp ändringar av fönster som kan kräva bygglov, bland annat ny kulör, ändrade profiler och spröjsar och ändrad indelning, och i särskilt värdefulla områden krävs lov även för åtgärder som annars är lovfria.",
       "En renovering som behåller mått, profiler, indelning och kulör är underhåll. Stadsmuseets klassificeringskarta ger en första bild av om ditt hus berörs. Om villastadens fasader och färgtoner kan du läsa under " + _L.format("malare-alvsjo.html", "målare i Älvsjö") + ".",
     ],
     "aside": None},
    {"id": "malningen-alvsjo", "h2": "Rengöring, kitt och färg",
     "paras": [
       "Riksantikvarieämbetet beskriver rengöring med soda- eller ammoniaklösning och noggrann sköljning, och att lös färg och lös kitt skrapas bort. Ibland behöver all färg tas bort, till exempel om fönstret målats med olämplig färg eller om färgskiktet blivit för tjockt.",
       "Därefter kittas falsarna med linoljekitt och fönstret målas med linoljefärg i tre strykningar. Med tätningslist på innerbågen blir fönstren också tätare. Om fönsterbyte i stort kan du läsa under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Älvsjö till",
  "steps": [
    ("Inventering", "Bågar, luckor, kitt och beslag besiktigas fönster för fönster."),
    ("Skriftligt kostnadsförslag", "Varje fönster och lucka står för sig."),
    ("Nedtagning", "Bågar och luckor tas ner och märks för att komma tillbaka på rätt plats."),
    ("Reparation", "Skadat virke byts, kitt läggs om och beslagen rengörs och justeras."),
    ("Målning", "Linoljefärg i grundning, mellan- och slutstrykning."),
    ("Uppsättning", "Bågar och luckor sätts tillbaka, justeras och tätas."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Älvsjö",
  "rot": [
    _ROT_SMA + " Att byta eller reparera fönsterbleck räknas också.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Älvsjö?",
  "price": [
    "Antalet fönster och luckor, mängden spröjs, skadorna i virket, beslagens skick och om all färg behöver tas bort. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan fönsterluckorna på vår villa i Älvsjö renoveras?",
     "Ja. Skadat trä lagas, luckorna målas och gångjärn och hakar justeras eller byts när de inte fungerar."),
    ("Våra kopplade bågar går trögt – måste de bytas?",
     "Oftast inte. Riksantikvarieämbetet beskriver igengrodda kopplingsbeslag och skevheter som vanliga problem, som kan åtgärdas med justering och nya handtag och stängningsbeslag."),
    ("Ska vi spara de gamla beslagen?",
     "Ja, Riksantikvarieämbetet råder att inte kasta gamla fönsterbeslag, eftersom beslag av äldre typ är svåra att få tag på."),
    ("Behöver vi lov för att måla fönstren i en ny kulör?",
     "Ny kulör räknas som en ändring som kan kräva lov, särskilt i de delar av Älvsjö som är kulturhistoriskt värdefulla. Samma kulör är underhåll."),
  ],
  "sources": [_ALV_INV, _RAA_F, _VARSAM, _STH_FD, _STH_KL, _SKV, _SKV2],
  "cta": ("Ska fönstren i villan i Älvsjö renoveras?", "Boka ett gratis platsbesök, så går vi igenom fönster och luckor innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa med slätputsad bottenvåning och småspröjsade fönster med luckor",
     "1910s Swedish villa with white smooth rendered ground floor, dark brown painted board gable above, small-paned windows with wooden shutters, steep red tile roof, garden, southern Stockholm, summer" + _IMG_END),
    ("Kopplade fönsterbågar som öppnas inåt",
     "interior view of an old Swedish coupled inward-opening double casement window with small panes, brass coupling hooks and handles, painted white, daylight from outside" + _IMG_END),
    ("Fönsterlucka som målas om på bockar",
     "old wooden window shutter laid on trestles being repainted dark green, sanded edges, paint can and brush beside it, outdoor workshop area, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SPÅNGA
"fonsterrenovering-spanga.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Spånga", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Spånga – villorna i Solhem",
  "description": "Fönsterrenovering i Spånga: villorna i Solhem och Bromsten, fönsterändringar som kräver lov, tätningslister och tillsatsrutor i stället för nya fönster.",
  "h1": "Fönsterrenovering i Spånga",
  "lead": "Villorna i Solhem och de andra villastäderna i Spånga har ofta kvar sina ursprungliga fönster, och de går i regel att göra täta igen utan att bytas. Geal Entreprenad AB renoverar fönster i villor i Solhem, Bromsten, Flysta och Sundby och behåller fönstrens mått och utseende.",
  "card": "Villorna i Solhem.",
  "sections": [
    {"id": "solhem-spanga", "anchor": "Solhem",
     "h2": "Solhem och villastäderna",
     "paras": [
       "Stadens strategi för småhusområden räknar Solhem, Bromsten, Flysta och Sundby till villastäderna. I Solhem fanns från början stora tomter där bara en tiondel fick bebyggas, och i strategins tabell är Solhem markerat som kulturhistoriskt värdefull miljö.",
       "Stadsmuseets inventering av Älvsjö villastad berättar att bolaget AB Hem på landet ofta använde ritningar som tidigare använts i andra villastäder som bolaget exploaterade, till exempel Solhem. Villorna i de två villastäderna kan alltså ha gemensamma förlagor.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Solhem: 1 946", "Bromsten: 916", "Flysta: 657", "Sundby: 525"]}},
    {"id": "andringar-spanga", "h2": "Ändringar som kan kräva lov",
     "paras": [
       "Stockholms stad räknar upp vilka fönsterändringar som kan kräva bygglov: att byta material eller kulör, ändra storlek, dimensioner, proportioner eller profiler på karmar, bågar och spröjsar, byta upphängning, till exempel från sidohängda fönster till vippfönster, och ändra indelningen genom att lägga till spröjs eller ta bort mittpost.",
       "Det är bygglovsenheten som bedömer utifrån den ändring som föreslås om den kräver lov för just den byggnaden, skriver staden. Staden påpekar att byggnaden kan ha karaktäristiska fönster eller tidstypisk fönsterindelning, där en ändring påverkar både fasaden och husets karaktär. I Solhem, som är kulturhistoriskt värdefull miljö, gäller utökad lovplikt. En renovering som behåller mått, profiler, indelning och kulör är däremot underhåll.",
     ],
     "aside": {"title": "Kan kräva lov enligt staden", "items": [
       "Nytt material eller ny kulör", "Andra profiler eller spröjsar", "Ny upphängning", "Mittpost bort eller spröjs till"]}},
    {"id": "tatningen-spanga", "h2": "Tätningslister i stället för nya fönster",
     "paras": [
       "Riksantikvarieämbetet skriver att de två vanligaste skälen till att byta gamla fönster är att värme- och ljudisoleringen ska bli bättre, men att det finns billigare lösningar. Dagens tätningslister av gummi passar gamla fönster väl och ger en avsevärd förbättring. Svarta och bruna lister är av EPDM-gummi, vita av silikongummi.",
       "Det är innerbågen som ska tätas, inte ytterbågen, och fönstret ska vara målat och justerat innan listerna sätts. En för tjock list gör fönstret svårstängt och kan skada båge och glas, så vi mäter springan innan vi väljer list.",
     ],
     "aside": None},
    {"id": "tillsatsrutor-spanga", "h2": "Tillsatsruta eller ny innerbåge",
     "paras": [
       "En tillsatsruta är ett extra glas i en profil som fästs på innerbågen, och enligt Riksantikvarieämbetet ger gummilisterna ett lufttätt utrymme där glasen inte behöver tvättas. Vill du behålla de profiler som finns på det befintliga fönstret är en extra träbåge på insidan oftast den bästa lösningen.",
       "Med rätt tätningslist och tillsatsruta blir ett gammalt fönster enligt Riksantikvarieämbetet lika energisnålt som ett nytt. Om villastädernas hus i övrigt kan du läsa under " + _L.format("totalrenovering-spanga.html", "totalrenovering i Spånga") + ".",
     ],
     "aside": None},
    {"id": "virket-spanga", "h2": "Virket och bottenstyckena",
     "paras": [
       "Det är framför allt bottenstyckena i karm och båge som drabbas av större skador, skriver Riksantikvarieämbetet, och oftast går det att byta bara de skadade partierna. För karmbottenstycken räcker det i allmänhet att limma in nytt virke i den yttersta, mest utsatta delen.",
       "Virket som används vid reparation bör enligt Riksantikvarieämbetet likna och kunna samverka med det som använts tidigare. Riksantikvarieämbetet anger bland annat hög kärnvedsandel, högt kådinnehåll, täta årsringar och kärnsidan vänd utåt.",
       "Utan besiktning är det lätt att döma ut fönster som går att bevara, påpekar Riksantikvarieämbetet. Därför börjar vi med att gå igenom varje fönster för sig. Om fönsterbyte i stort kan du läsa under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Spånga till",
  "steps": [
    ("Besiktning", "Varje fönster gås igenom: virke, kitt, färg, beslag och täthet."),
    ("Skriftligt kostnadsförslag", "Renovering, tätning och eventuell innerbåge står var för sig."),
    ("Reparation", "Skadade bottenstycken och delar av bågar byts med nytt virke."),
    ("Kittning och målning", "Linoljekitt och linoljefärg i tre strykningar."),
    ("Tätning", "Bågarna justeras och innerbågen förses med tätningslist."),
    ("Genomgång", "Vi går igenom fönstren och hur de sköts framöver."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Spånga",
  "rot": [
    _ROT_SMA + " Att montera isolerglas räknas också, liksom att byta eller reparera fönsterbleck.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Spånga?",
  "price": [
    "Antalet fönster och bågar, skadorna i virket, om all färg behöver tas bort och om fönstren ska få tätningslister, tillsatsrutor eller nya innerbågar. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi lov för att sätta tätningslister i fönstren i Solhem?",
     "Nej, tätningslister på innerbågen ändrar inte fönstrets utseende utifrån. Det som kan kräva lov är ändringar av material, kulör, profiler, upphängning eller indelning."),
    ("Kan vi byta våra sidohängda fönster mot vippfönster?",
     "Byte av upphängning är en av de ändringar som Stockholms stad räknar upp som fasadändring, och i Solhem gäller utökad lovplikt."),
    ("Blir gamla fönster lika energisnåla som nya?",
     "Enligt Riksantikvarieämbetet, ja, med rätt tätningslist och tillsatsruta."),
    ("Gäller samma regler i Bromsten och Flysta som i Solhem?",
     "Bromsten och Flysta är inte markerade som kulturhistoriskt värdefull miljö i stadens strategi, men enskilda hus kan vara klassade. Stadsmuseets karta ger en första bild."),
    ("Vilken tätningslist ska vi välja?",
     "Det beror på springan. Vi mäter den innan, eftersom en för tjock list gör fönstret svårstängt och kan skada båge och glas."),
  ],
  "sources": [_VARSAM, _ALV_INV, _STH_FD, _RAA_F,
              ("Stockholms stad – Områdesfakta 2025: Solhem (pdf)", _OF + "vasterort/jarva/solhem.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Bromsten (pdf)", _OF + "vasterort/jarva/bromsten.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Flysta (pdf)", _OF + "vasterort/jarva/flysta.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Sundby (pdf)", _OF + "vasterort/jarva/sundby.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska fönstren i villan i Spånga renoveras?", "Boka ett gratis platsbesök, så går vi igenom fönstren ett och ett innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre trävilla med småspröjsade fönster på en stor trädgårdstomt",
     "early 1900s Swedish wooden villa with small-paned white windows, light grey panel facade, glazed veranda, large garden with old fruit trees, north-western Stockholm, summer" + _IMG_END),
    ("Tätningslist och verktyg vid falsen på en innerbåge",
     "close view of a black rubber weatherstrip lying partly pressed into the rebate of an old painted wooden inner window sash, staple gun on the sill, no hands, no people, daylight" + _IMG_END),
    ("Inre träbåge med extra glas på ett gammalt fönster",
     "interior view of an old Swedish wooden window fitted with an additional inner wooden sash with clear glass, matching profiles, painted white, plants on the sill, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HÄGERSTEN
"fonsterrenovering-hagersten.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Hägersten", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Hägersten – fönster från olika epoker",
  "description": "Fönsterrenovering i Hägersten: villor från flera epoker i Mälarhöjden, spröjsade bågar före 1930, hel glasruta och lim efter, renovering efter ålder.",
  "h1": "Fönsterrenovering i Hägersten",
  "lead": "I Mälarhöjden och resten av Hägersten står villor från olika årtionden sida vid sida, och fönstren är byggda på olika sätt beroende på när huset kom till. Geal Entreprenad AB renoverar fönster i villor och radhus i Hägersten och anpassar arbetet efter hur fönstret är tillverkat.",
  "card": "Fönster från olika epoker.",
  "sections": [
    {"id": "epokerna-hagersten", "anchor": "Epokerna",
     "h2": "Villor från många årtionden",
     "paras": [
       "Mälarhöjden växte upp som villasamhälle efter privata initiativ, skriver staden i sin strategi för småhusområden. Villastäderna präglas av en blandning av hustyper från olika epoker, och den successiva kompletteringen speglas i bebyggelsens utformning. Mälarhöjden är markerat som kulturhistoriskt värdefull miljö och har äldre planer med generösa byggrätter.",
       "Enligt stadens områdesfakta för 2025 finns 988 småhus med äganderätt i Mälarhöjden och 955 i stadsdelen Hägersten. I en sådan miljö kan grannhusens fönster vara från helt olika tider, och det märks när de ska renoveras.",
     ],
     "aside": {"title": "Småhus med äganderätt 2025", "items": [
       "Mälarhöjden: 988", "Hägersten: 955", "Västberga: 280"]}},
    {"id": "fore1930-hagersten", "h2": "Före 1930: spröjs och demonterbara bågar",
     "paras": [
       "Riksantikvarieämbetet beskriver hur spröjsarna kom tillbaka kring sekelskiftet och fram till 1930, med stilideal som hade historiska förebilder. Fönstren i den äldre bebyggelsen har ofta småspröjsade rutor, och från sekelskiftet blev kopplade, inåtgående bågar allt vanligare.",
       "De äldre sammanfogningarna i bågar och karmar går att ta isär, påpekar Riksantikvarieämbetet. Det gör att skadade delar, som en spröjs eller nederdelen av en båge, kan bytas utan att hela bågen tas isär, och att ett gammalt fönster går att renovera gång på gång.",
     ],
     "aside": None},
    {"id": "efter1930-hagersten", "h2": "Från 1930-talet: hel glasruta och lim",
     "paras": [
       "På 1930-talet försvann de spröjsade bågarna igen, och fönsterbågen fick en enda hel glasruta. Samtidigt introducerades limmet i fönsterkonstruktionerna: en handbok från 1931 skriver att alla sammansättningar i fönsterbågar limmas, enligt Riksantikvarieämbetet.",
       "Limmade bågar är svårare att ta isär, så där lagar vi skador genom att skarva in nytt virke i den skadade delen i stället för att demontera bågen. Löst kitt tas bort med ett smalt stämjärn och stor försiktighet, eftersom glaset lätt spricker, särskilt där glasningsstiften sitter.",
     ],
     "aside": {"title": "Enligt Riksantikvarieämbetet", "items": [
       "Fram till 1930: spröjsade bågar", "1930-talet: en hel glasruta", "Från 1930-talet: limmade bågar"]}},
    {"id": "inventeringen-hagersten", "h2": "Varje fönster för sig",
     "paras": [
       "Är det osäkert om fönstren bara behöver vanligt underhåll eller större reparationer råder Riksantikvarieämbetet att börja med en systematisk besiktning av varje fönster för sig. En sådan inventering ger underlag för en mer exakt kostnadsberäkning, och utan besiktning är det lätt att döma ut fönster som går att bevara.",
       "Med dagens metoder kan målningen ofta göras i en verkstad. Då går det att renovera fönster även på vintern, och resultatet blir enligt Riksantikvarieämbetet jämnare. Medan bågarna är borta sätter vi upp tillfälliga skydd i fönsteröppningarna.",
     ],
     "aside": None},
    {"id": "lovet-hagersten", "h2": "Renovera utan att ändra",
     "paras": [
       "Stockholms stad räknar upp fönsterändringar som kan kräva bygglov, som ny kulör eller nytt material, ändrade profiler och spröjsar, ändrad upphängning och ny indelning. I särskilt kulturhistoriskt värdefulla områden krävs lov även för åtgärder som annars är lovfria, och Stadsmuseets klassificeringskarta ger en första bild av vad som gäller för ditt hus.",
       "En renovering behåller mått, profiler och indelning och räknas som underhåll. Om fönsterbyte i stadsdelen kan du läsa under " + _L.format("fonsterbyte-hagersten.html", "fönsterbyte i Hägersten") + ".",
     ],
     "aside": None},
    {"id": "malningen-hagersten", "h2": "Kitt, färg och tätning",
     "paras": [
       "Oavsett epok är underhållet i första hand ommålning och kittning, skriver Riksantikvarieämbetet. Sol och väta bryter ner färg och kitt på de mest utsatta delarna, och särskilt sydfasaderna är utsatta. Normalt räcker det att kitta om bågens nedre del.",
       "Vi målar med linoljefärg i grundning, mellanstrykning och slutstrykning och tätar innerbågen med tätningslist när fönstret är justerat. Om stadsdelens fasader kan du läsa under " + _L.format("fasadrenovering-hagersten.html", "fasadrenovering i Hägersten") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Hägersten till",
  "steps": [
    ("Besiktning", "Fönstrens ålder, konstruktion och skador går vi igenom fönster för fönster."),
    ("Skriftligt kostnadsförslag", "Varje fönster och moment står för sig."),
    ("Reparation", "Skadade delar byts eller skarvas efter hur bågen är sammanfogad."),
    ("Kittning", "Löst kitt tas bort försiktigt och falsen kittas om med linoljekitt."),
    ("Målning och tätning", "Linoljefärg i tre strykningar och tätningslist på innerbågen."),
    ("Genomgång", "Vi går igenom fönstren och skriver ner kulör och material."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Hägersten",
  "rot": [
    _ROT_SMA + " Du ska äga huset när arbetet utförs.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Hägersten?",
  "price": [
    "Antalet fönster, hur de är konstruerade, skadorna i virket, mängden spröjs och om fönstren ska tätas eller få innerbåge. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur vet vi hur gamla fönstren i vårt hus i Mälarhöjden är?",
     "Konstruktionen säger mycket. Spröjsade bågar hör enligt Riksantikvarieämbetet till tiden fram till 1930, medan bågar med en hel glasruta och limmade fogar kom på 1930-talet."),
    ("Går limmade fönsterbågar att renovera?",
     "Ja, men de är svårare att ta isär. Skador lagas då genom att nytt virke skarvas in i den skadade delen."),
    ("Kan fönstren renoveras på vintern?",
     "Ja, om bågarna tas till verkstad. Riksantikvarieämbetet skriver att målningen då kan göras även vintertid och att resultatet blir jämnare."),
    ("Är Mälarhöjden kulturhistoriskt värdefullt?",
     "Ja, Mälarhöjden är markerat som kulturhistoriskt värdefull miljö i stadens strategi för småhusområden. Kontrollera din fastighet i Stadsmuseets karta."),
  ],
  "sources": [_VARSAM, _RAA_F, _STH_FD, _STH_KL,
              ("Stockholms stad – Områdesfakta 2025: Mälarhöjden (pdf)", _OF + "soderort/hagersten/malarhojden.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Hägersten (pdf)", _OF + "soderort/hagersten/hagersten.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Västberga (pdf)", _OF + "soderort/hagersten/vastberga.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska fönstren i huset i Hägersten renoveras?", "Boka ett gratis platsbesök, så går vi igenom fönstren ett och ett innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Två grannvillor från olika epoker med olika fönster",
     "two neighbouring Swedish villas from different eras side by side, an early 1900s wooden villa with small-paned windows and a 1930s functionalist white rendered house with large single-pane windows, gardens with oak trees, south-western Stockholm, summer" + _IMG_END),
    ("Fönsterbåge med spröjs som tagits isär för reparation",
     "old wooden window sash partly disassembled on a workbench, separate glazing bars and stiles with mortise and tenon joints visible, clamps and chisel beside, workshop light" + _IMG_END),
    ("Vit funkisbåge och kittknivar på en arbetsbänk",
     "still life, empty room: a 1930s single-pane white painted wooden window sash lying flat on a workbench, fresh linseed putty bead along the glass edge, a putty knife lying on the bench next to it, soft daylight, realistic photo, no people, no hands, no text" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VÄLLINGBY
"fonsterrenovering-vallingby.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Vällingby", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Vällingby – radhusens fönster",
  "description": "Fönsterrenovering i Vällingby: radhus och kedjehus i tunnelbanestaden, riksintresset, ägarform och vad rotavdraget täcker i en bostadsrätt.",
  "h1": "Fönsterrenovering i Vällingby",
  "lead": "Radhusen och kedjehusen runt Vällingby centrum har ofta en regelbunden fönstersättning som är lika i hela gruppen, och därför är det värt att behålla fönstren. Geal Entreprenad AB renoverar fönster i radhus, kedjehus och villor i Vällingby, Råcksta och Kälvesta och reder ut vem som ansvarar för vad.",
  "card": "Radhusens fönster.",
  "sections": [
    {"id": "tunnelbanestaden-vallingby", "anchor": "Tunnelbanestaden",
     "h2": "Tunnelbanestadens radhus",
     "paras": [
       "Vällingby invigdes 1954 som den första tunnelbanestaden, och runt centrum placerades bostäder i fallande skala med radhus och kedjehus längst ut. Stadens strategi för småhusområden beskriver flera mycket väl gestaltade radhus- och villaområden, till exempel de kulturhistoriskt synnerligen värdefulla Atlantis och Omega. Vällingby–Råcksta är riksintresse för kulturmiljövården.",
       "Strategin beskriver kedjehusen i Vällingby som moderna byggnadsvolymer med asymmetriska gavlar och en mer traditionell fasadutformning, med regelbunden fönstersättning och material som tegel och puts.",
     ],
     "aside": {"title": "Vällingby enligt strategin", "items": [
       "Första tunnelbanestaden 1954", "Atlantis och Omega", "Regelbunden fönstersättning", "Riksintresse Vällingby–Råcksta"]}},
    {"id": "gruppen-vallingby", "h2": "Fönstren som en del av gruppen",
     "paras": [
       "För de gruppbyggda småhusområdena räknar strategin enhetligt utformade husgrupper och tidstypisk färgsättning till karaktärsdragen, och den råder att karaktärsskapande material, byggnadsdelar och detaljer tas tillvara vid renoveringar. Ett nytt fönster med annan indelning eller grövre profiler syns i hela längan.",
       "Stockholms stad räknar ändrade profiler, ny indelning, ny upphängning och ny kulör till de fönsterändringar som kan kräva bygglov, och inom riksintresset krävs lov även för åtgärder som annars är lovfria. En renovering som behåller fönstrets utseende är underhåll.",
     ],
     "aside": None},
    {"id": "aganderatt-vallingby", "h2": "Äganderätt eller bostadsrätt",
     "paras": [
       "Enligt stadens områdesfakta för 2025 finns 228 småhus med bostadsrätt och 220 med äganderätt i stadsdelen Vällingby. I Kälvesta är nästan alla de 1 492 småhusen äganderätter, och där beställer ägaren själv. Stadens strategi beskriver Kälvestas radhus och kedjehus med liggande träpanel och sadeltak.",
       "Bor du i ett radhus med bostadsrätt avgör föreningens stadgar vem som ansvarar för fönstren. Bostadsrättslagen utgår från att du håller lägenheten i gott skick, om inte stadgarna bestämmer annat. Det påverkar både vem som beställer och vilket rotavdrag som gäller.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Vällingby: 220 äganderätt, 228 bostadsrätt", "Råcksta: 299 äganderätt, 91 bostadsrätt", "Kälvesta: 1 492 äganderätt"]}},
    {"id": "fonstren-vallingby", "h2": "1950-talets fönster",
     "paras": [
       "Riksantikvarieämbetet beskriver hur de spröjsade bågarna försvann på 1930-talet och fönsterbågen fick en enda hel glasruta, och hur limmet samtidigt infördes i fönsterkonstruktionerna. Fönster från tiden efter 1930-talet har därför ofta en hel ruta i varje båge och limmade fogar.",
       "Limmade bågar lagas genom att nytt virke skarvas in i den skadade delen. Det är framför allt bottenstyckena i karm och båge som drabbas, och för karmen räcker det i allmänhet att limma in nytt virke i den yttre, mest utsatta delen. Om fasaderna i stadsdelen kan du läsa under " + _L.format("fasadrenovering-vallingby.html", "fasadrenovering i Vällingby") + ".",
     ],
     "aside": None},
    {"id": "underhallet-vallingby", "h2": "Kitt, färg och tätning",
     "paras": [
       "Riksantikvarieämbetet rekommenderar linoljefärg och linoljekitt vid renovering av träfönster, och tre strykningar: grundning, mellanstrykning och slutstrykning. Tätningslister på innerbågen förbättrar både ljud- och värmeisolering, och fönstret ska målas och justeras innan listerna sätts.",
       "Går bågarna trögt eller sluter dåligt kan det behövas nya handtag och stängningsbeslag, och gångjärnen justeras så att bågen sluter tätt mot karmen innan listen sätts. Med dagens metoder kan målningen också göras i verkstad, så att fönstren kan renoveras även på vintern.",
       "Ska flera hus i längan renoveras samtidigt kan arbetet samordnas, så att fönstren får samma kulör och samma utförande. Om fönsterbyte i stort kan du läsa under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Vällingby till",
  "steps": [
    ("Ägarform", "Vi reder ut om du eller föreningen ansvarar för fönstren."),
    ("Besiktning", "Varje fönster gås igenom: virke, kitt, färg och beslag."),
    ("Skriftligt kostnadsförslag", "Utsida och insida står för sig, så att ROT kan räknas rätt."),
    ("Reparation", "Skadade bottenstycken skarvas och kitt läggs om."),
    ("Målning och tätning", "Linoljefärg i tre strykningar och tätningslist på innerbågen."),
    ("Genomgång", "Vi går igenom fönstren och skriver ner kulören."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Vällingby",
  "rot": [
    _ROT_SMA + " I en bostadsrätt ger byte eller reparation av fönster inget avdrag, men arbete på fönstrens insida, till exempel innerfönster och fönsterfoder, kan ge avdrag om du ansvarar för det enligt stadgarna.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Vällingby?",
  "price": [
    "Antalet fönster, skadorna i virket, rutornas storlek, om fönstren ska tätas och om flera hus i gruppen renoveras samtidigt. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem ansvarar för fönstren i vårt bostadsrättsradhus i Vällingby?",
     "Det avgör föreningens stadgar. Bostadsrättslagen utgår från att du håller lägenheten i gott skick, om inte stadgarna bestämmer annat."),
    ("Får vi rotavdrag för att renovera fönstren i en bostadsrätt?",
     "Bara för arbete på insidan som du ansvarar för, till exempel innerfönster och fönsterfoder. Reparation av fönstren i övrigt ger inget avdrag i en bostadsrätt."),
    ("Kräver nya fönster i Atlantis bygglov?",
     "Vällingby–Råcksta är riksintresse för kulturmiljövården. Ligger huset inom det, vilket Stadsmuseets karta visar med blå ring, krävs lov för fasadändringar som annars är lovfria. En renovering som behåller utseendet är underhåll."),
    ("Kan hela längan renovera fönstren samtidigt?",
     "Ja, och det gör det lättare att få samma kulör och utförande på alla hus. Vi lämnar då ett kostnadsförslag där varje hus står för sig."),
    ("Går det att laga ett fönster med limmade fogar?",
     "Ja, genom att skarva in nytt virke i den skadade delen i stället för att ta isär bågen."),
  ],
  "sources": [_VARSAM, _STH_FD, _STH_KL, _RAA_F, _BRL,
              ("Stockholms stad – Områdesfakta 2025: Vällingby (pdf)", _OF + "vasterort/hasselby-vallingby/vallingby.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Råcksta (pdf)", _OF + "vasterort/hasselby-vallingby/racksta.pdf"),
              ("Stockholms stad – Områdesfakta 2025: Kälvesta (pdf)", _OF + "vasterort/hasselby-vallingby/kalvesta.pdf"),
              _SKV, _SKV2],
  "cta": ("Ska fönstren i radhuset i Vällingby renoveras?", "Boka ett gratis platsbesök, så går vi igenom fönstren och ansvarsfrågan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Kedjehus från 1950-talet med regelbunden fönstersättning",
     "1950s Swedish linked houses with asymmetric gables, light rendered and brick facades and regularly spaced wooden windows with large single panes, lawns and pine trees, western Stockholm, summer" + _IMG_END),
    ("Fönsterbåge med stor ruta där bottenstycket lagas",
     "1950s wooden window sash with one large pane on a workbench, a new piece of wood glued into the bottom rail, clamps, workshop light" + _IMG_END),
    ("Rad av radhusfönster i samma kulör efter renovering",
     "row of identical freshly painted wooden windows along a 1950s Swedish terraced house facade, uniform colour, clean putty lines, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"fonsterrenovering-osteraker.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Österåker", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Österåker – sommarvillorna i Svinninge",
  "description": "Fönsterrenovering i Österåker: sommarvillornas enkla bågar och lösa innerbågar, glasverandornas handblåsta glas och lov i värdefulla miljöer.",
  "h1": "Fönsterrenovering i Österåker",
  "lead": "Många äldre sommarvillor i Österåker har bara enkla fönsterbågar, eftersom de byggdes för sommaren. När de blir åretruntboende är det lättare att komplettera fönstren än att byta dem. Geal Entreprenad AB renoverar fönster i villor och fritidshus i Svinninge, Åkersberga och resten av Österåker.",
  "card": "Sommarvillorna i Svinninge.",
  "sections": [
    {"id": "svinninge-osteraker", "anchor": "Svinninge",
     "h2": "Sommarvillorna i Svinninge",
     "paras": [
       "Kommunens råd och riktlinjer för byggande i Svinninge beskriver Svinningeudd och Nantes som kommunens äldsta och bäst bevarade sommarhusbebyggelse. Där finns sommarvillor från sekelskiftet, ofta klädda med liggande hyvlad fasspontpanel som ursprungligen målades med linoljefärg, och senare sportstugor och fritidshus från 1930-talet och framåt.",
       "Allt fler flyttar enligt kommunen ut permanent, och fritidshusen byggs om för att passa dagens krav på permanentbostäder. Det är då fönstren brukar bli en fråga, eftersom ett hus som ska värmas året runt ställer andra krav än en sommarvilla.",
     ],
     "aside": {"title": "Husen i Svinninge", "items": [
       "Sommarvillor från sekelskiftet", "Röda stugor med vita knutar", "Sportstugor från 1930-talet", "Fritidshus som blir åretruntbostäder"]}},
    {"id": "innerbagar-osteraker", "h2": "Lösa innerbågar på gångjärn",
     "paras": [
       "Eftersom sommarvillorna bara användes under den varma säsongen har de flesta äldre hus enkla fönsterbågar, skriver kommunen. Det bästa sättet att få bättre värmeekonomi är enligt riktlinjerna att tillverka lösa innerbågar som monteras på gångjärn.",
       "Innerbågen tillverkas efter det befintliga fönstrets mått och profiler och hängs på insidan. Fönstret ser likadant ut från utsidan, och båda bågarna kan öppnas för vädring och fönsterputs.",
     ],
     "aside": None},
    {"id": "karnvirket-osteraker", "h2": "Kärnvirke som håller",
     "paras": [
       "Äldre fönster tillverkades så gott som undantagslöst av utvalt kärnvirke och har mycket lång livslängd om de underhålls kontinuerligt, skriver kommunen. Vid renovering räcker det oftast att byta de rötskadade delarna, oftast spröjsarna och bågens undre del.",
       "Behöver ett enstaka fönster bytas helt råder riktlinjerna att låta en fönsterhantverkare specialtillverka en kopia av det gamla. Nya standardfönster har sällan samma proportioner som de gamla, och fel insatta kan de förstöra utseendet på hela fasaden.",
     ],
     "aside": {"title": "Råd i riktlinjerna", "items": [
       "Byt bara rötskadade delar", "Lösa innerbågar på gångjärn", "Kopia i stället för standardfönster"]}},
    {"id": "vardefullt-osteraker", "h2": "Är huset värdefullt?",
     "paras": [
       "Österåkers kommun har en lista med frågor för att avgöra om ett hus kan vara värdefullt: om det finns skyddsbestämmelser i detaljplanen, om huset ligger i eller nära ett kulturmiljöområde i Österåkerskartan, om det finns med i en inventering eller ett kulturmiljöprogram, om det har bevarade byggnadsdetaljer som fönster och om det är byggt före 1920. Svarar du ja på någon av frågorna kan huset vara värdefullt.",
       "Sommarvillorna från sekelskiftet i Nantes beskrivs i riktlinjerna med regelbundet placerade fönster med smårutig indelning, och kommunen visar äldre fönster med små rutor, smäcker konstruktion och sannolikt munblåst glas. Det är precis den sortens fönster som är värda att renovera.",
     ],
     "aside": {"title": "Kan vara värdefullt om huset", "items": [
       "Har skyddsbestämmelser i detaljplanen", "Ligger i ett kulturmiljöområde", "Har bevarade fönster", "Är byggt före 1920"]}},
    {"id": "verandorna-osteraker", "h2": "Glasverandornas glas",
     "paras": [
       "Många glasverandor har rikt spröjsade fönster, ibland med färgat glas, och det ursprungliga glaset var ofta handblåst. Kommunen påpekar att det är svårt att ersätta med dagens planglas, som ger ett helt annat uttryck, och att man därför ska vara extra rädd om de ursprungliga glasen.",
       "Vid renovering av en veranda tar vi därför ut gamla glas försiktigt, märker dem och sätter tillbaka dem i samma båge. Stolpar och räcken har ofta rötskador nertill, och där byter vi bara de skadade delarna mot nya med samma utseende.",
     ],
     "aside": None},
    {"id": "fargen-osteraker", "h2": "Färgen och lovet",
     "paras": [
       "Sommarvillorna hade enligt riktlinjerna en rik färgskala, och fönsterbågarna målades ofta i en mörkare färg som engelskt rött, grönt eller brunt. Sportstugorna hade ofta mörkt bruna fasader med gröna snickerier, eller faluröda fasader med vita snickerier.",
       "Österåkers kommun skriver att du behöver bygglov om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden är särskilt värdefull, och att det kan gälla även underhåll. Österåkerskartan visar områden med kulturhistoriska värden. Om fönsterbyte i kommunen kan du läsa under " + _L.format("fonsterbyte-osteraker.html", "fönsterbyte i Österåker") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering i Österåker till",
  "steps": [
    ("Platsbesök", "Fönster, veranda och husets ålder går vi igenom."),
    ("Kartan", "Österåkerskartan och detaljplanen kontrolleras."),
    ("Skriftligt kostnadsförslag", "Renovering, glas och innerbågar står var för sig."),
    ("Reparation", "Rötskadade spröjsar och bågdelar byts, gamla glas sparas."),
    ("Innerbågar", "Lösa innerbågar tillverkas och hängs på gångjärn."),
    ("Målning och genomgång", "Linoljefärg i husets kulör, och vi går igenom resultatet."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Österåker",
  "rot": [
    _ROT_SMA + " Avdraget gäller även en bostad som du använder som fritidsbostad.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Österåker?",
  "price": [
    "Antalet fönster, verandans storlek och spröjsning, hur mycket virke som är rötskadat, om innerbågar ska tillverkas och om gamla glas ska sparas. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur gör vi sommarvillans fönster varmare utan att byta dem?",
     "Österåkers riktlinjer för Svinninge rekommenderar lösa innerbågar som monteras på gångjärn. Fönstret ser likadant ut utifrån."),
    ("Kan vi behålla det gamla glaset i glasverandan?",
     "Ja, och kommunen råder att vara extra rädd om det, eftersom handblåst glas är svårt att ersätta med dagens planglas."),
    ("Behövs bygglov för att renovera fönstren i Svinningeudd?",
     "Det kan behövas. Kommunen skriver att lov kan krävas även för underhåll i särskilt värdefulla områden. Kontakta bygglovsenheten och se Österåkerskartan."),
    ("Vilken kulör hade fönsterbågarna på sommarvillorna?",
     "Enligt riktlinjerna ofta en mörkare färg som engelskt rött, grönt eller brunt."),
  ],
  "sources": [_OST_SVIN, _OST_KULT, _SKV, _SKV2],
  "cta": ("Ska fönstren i huset i Österåker renoveras?", "Boka ett gratis platsbesök, så går vi igenom fönster och veranda innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sommarvilla med glasveranda och spröjsade fönster vid vattnet",
     "Swedish turn-of-the-century summer villa with horizontal light painted panel, glazed veranda with many small panes facing the water, window sashes painted dark red, pine trees and rocks, Stockholm archipelago, summer" + _IMG_END),
    ("Lös innerbåge på gångjärn innanför ett gammalt fönster",
     "interior view of an old single-glazed wooden window with an added inner wooden sash hung on hinges and opened inward, matching small panes, painted white, wooden floor, daylight" + _IMG_END),
    ("Gammalt handblåst glas med ojämn yta i en verandabåge",
     "close view of old hand-blown window glass with slight waves and bubbles in a small-paned veranda sash, reflections of trees, daylight" + _IMG_END),
  ],
},
}
