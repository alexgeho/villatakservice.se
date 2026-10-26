# -*- coding: utf-8 -*-
"""Fönsterrenovering – ortsidor v31: Lidingö, Sundbyberg, Tyresö (2026-10-27).
Hubb: fonsterbyte.html (deltjänst, TJ_SERVICES["fonsterrenovering"]). Intent: renovera befintliga fönster – skild från
ortens fonsterbyte-<ort>.html, som länkas. Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.

Lokal vinkel per sida:
Lidingö – kulturmiljöprogrammet som antogs 16 december 2024 och ersatte programmet från 1990 (del 1 handbok med råd om
  underhåll, del 2 områdesbeskrivningar, webbkartan, äldre inventeringar 1970–80-tal och 2013–2015, nio
  byggnadsminnen), stadens regel att ändrade fönster är fasadändring och kräver lov i värdefulla områden, frivilligt
  bygglov, Riksantikvarieämbetets råd om underhåll (kitt, målning, bottenstycken).
Sundbyberg – Duvbo enligt stadens miljöprogram (Egna Hem 1898, 325 tomter, 98 tomter till 1924, riksintresse 1987,
  utökad lovplikt för utbyte, flyttning och igensättning av fönster, kostnadsfri; stilarna från sekelskiftet,
  1920-talet och 1940-talet), RAÄ om kopplade bågar (patent 1889, vanliga från sekelskiftet).
Tyresö – Stockholms läns museums kulturmiljöunderlag 2008:31 för Solberga/del av Raksta (byggnadsplan 1952,
  fritidshus från 1950-talet som permanentas, Strömstugans kopplade bågar med tre rutor per båge och pressade
  hörnjärn, Solberga gård renoverad till permanentstandard med de gamla detaljerna), kommunens sida om att måla om.

Fakta endast från källorna i respektive 'sources', öppnade med curl (webbläsar-UA) 2026-10-27, alla svarade 200;
pdf:erna (RAÄ 1988:1, Duvbo-programmet, Solberga-rapporten) har textlager. Lidingös områdes-pdf:er på mediaflow gick
inte att läsa och används inte. Skatteverket 2026-10-27: småhus – reparera eller byta ut fönster; måla fönster under
Målning och tapetsering; högst 30 procent av arbetskostnaden och 50 000 kronor per person och år.
Strukna / ej använda: vilka fönster enskilda Lidingöområden har, handläggningstider och avgifter, U-värden, bidrag.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"

_RAA = ("Riksantikvarieämbetet – Fönster. Historik och råd vid renovering (pdf)", "https://www.raa.se/publicerat/9789172095892.pdf")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_LID_KMP = ("Lidingö stad – Kulturmiljöprogram", "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/")
_LID_FAQ = ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet",
            "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/")
_LID_VAD = ("Lidingö stad – Bygglov och anmälan: Vad vill du göra?", "https://lidingo.se/bygga-bo/bygglov/vad-vill-du-gora/")
_DUVBO = ("Sundbybergs stad – Miljöprogram för Duvbo (pdf)",
          "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf")
_SUND_FAS = ("Sundbybergs stad – Fasadändring (bygglovsguiden)",
             "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/fasadandring")
_SOLB = ("Stockholms läns museum – Solberga/del av Raksta, kulturmiljöunderlag, rapport 2008:31 (pdf)",
         "https://insynsverige.se/documentHandler.ashx?did=20437")
_SKV_SA = ("Skatteverket – Så fungerar rotavdraget",
           "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_TYR_MALA = ("Tyresö kommun – Måla om huset", "https://www.tyreso.se/boende--miljo/bygga/bygglovswebben/mala-om-huset.html")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor "
            "ger inget avdrag, och Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ LIDINGÖ
"fonsterrenovering-lidingo.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Lidingö", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering på Lidingö – det nya kulturmiljöprogrammet",
  "description": "Fönsterrenovering på Lidingö: kulturmiljöprogrammet från 2024, när ändrade fönster kräver lov, kitt och linoljefärg och rotavdrag för villan.",
  "h1": "Fönsterrenovering på Lidingö",
  "lead": "I december 2024 antog Lidingö ett nytt kulturmiljöprogram, och många villaägare har sedan dess upptäckt att huset ligger i ett utpekat område. Där är det ofta både enklast och klokast att renovera de fönster huset redan har. Geal Entreprenad AB renoverar fönster på Lidingö – lagar trä, kittar om, målar och kompletterar med tätning – så att fönstren ser ut som förut.",
  "card": "Fönster i utpekade kulturmiljöer.",
  "sections": [
    {"id": "programmet-lidingo", "anchor": "Programmet",
     "h2": "Kulturmiljöprogrammet från 2024",
     "paras": [
       "Lidingö stad berättar att hela ön har inventerats och att kommunfullmäktige antog det nya kulturmiljöprogrammet den 16 december 2024. Det ersätter programmet från 1990. Vissa kvarter har tagits bort eftersom de förlorat de egenskaper som gjorde dem värdefulla, och nya områden har lagts till. Programmet har två delar: en handbok för fastighetsägare med allmänna råd om underhåll, och en del som beskriver bebyggelsehistorien och varje utpekat område.",
       "Bland de utpekade områdena finns Lidingö villastad, Breviks villastad, Herseruds villastad, Mölna radhusby, Dalakolonin, Grönstakolonin och Stureplatån. Om ditt hus ligger inom ett av dem ser du i stadens webbkarta. Staden skriver också att det finns äldre inventeringar av enskilda byggnader från 1970- och 1980-talen och från 2013–2015, och att du kan be om att få ta del av beskrivningen av din fastighet.",
     ],
     "aside": {"title": "Lidingös kulturmiljöprogram", "items": [
       "Antaget 16 december 2024", "Ersätter programmet från 1990", "Del 1: handbok för fastighetsägare", "Del 2: områdesbeskrivningar"]}},
    {"id": "lov-lidingo", "h2": "Ändrade fönster är en fasadändring",
     "paras": [
       "Lidingö stad räknar det som en fasadändring att ändra fönster och dörrar. Du behöver bygglov om fastigheten ligger inom ett kulturhistoriskt värdefullt område eller om byggnaden i sig är kulturhistoriskt värdefull. Staden skriver samtidigt att programmet är ett kunskapsunderlag som inte är juridiskt bindande, men att det används som stöd vid bygglov.",
       "En renovering som behåller fönstrens material, indelning och kulör ändrar inte det yttre utseendet. Därför är den vägen ofta den enklaste i ett utpekat område. Är du osäker kan du söka frivilligt bygglov, som enligt staden ger dig ett beslut på att det du planerar uppfyller lagens krav. Vill du ändå byta fönster finns " + _L.format("fonsterbyte-lidingo.html", "fönsterbyte på Lidingö") + ".",
     ],
     "aside": {"title": "Bygglov krävs på Lidingö", "items": [
       "I kulturhistoriskt värdefullt område", "För värdefull byggnad", "Frivilligt bygglov går att söka", "Kontroll i webbkartan"]}},
    {"id": "underhall-lidingo", "h2": "Kitt, färg och bottenstycken",
     "paras": [
       "Riksantikvarieämbetets skrift om fönster beskriver underhållet som i första hand ommålning och omkittning. Sol och väta bryter ner och lakar ur färg och kitt på fönstrens mest utsatta delar, och temperaturväxlingar och sprickor i träet gör att färgen flagnar och kittet lossnar. Framför allt sydfasaderna är utsatta.",
       "Skriften konstaterar att det främst är bottenstyckena i karm och båge som skadas, och att det oftast går att byta bara de skadade partierna. Ibland måste en båge nytillverkas. Vi tar loss bågarna, skrapar och lagar, byter rötskadat trä, kittar om och målar, och tillverkar en ny båge efter den gamla bara när den inte går att rädda.",
     ],
     "aside": None},
    {"id": "tathet-lidingo", "h2": "Tätare utan att byta",
     "paras": [
       "Riksantikvarieämbetet skriver att ett äldre fönster kan behöva kompletteras med tätningslister eller en innerbåge för att möta dagens krav på energi och ljud. Det är åtgärder som syns inifrån men inte från gatan, och som därför passar bra i ett hus som ska behålla sitt yttre.",
       "Programmets handbok beskriver hur man underhåller och förvaltar särskilt värdefulla byggnader, och staden påpekar att alla fastigheter inom ett utpekat område bör hanteras varsamt eftersom åtgärder på en tomt påverkar hur hela området upplevs. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte och fönsterrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönster på Lidingö",
  "steps": [
    ("Platsbesök", "Gratis genomgång av varje fönster."),
    ("Webbkartan", "Vi ser om huset ligger i ett utpekat område."),
    ("Nedmontering", "Bågarna tas loss och märks."),
    ("Lagning", "Skrapning, nytt trä där det behövs, omkittning."),
    ("Målning", "Grundning och målning i husets kulör."),
    ("Återmontering", "Justering, tätningslist och beslag."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering på Lidingö",
  "rot": [
    "För en villa eller ett radhus räknar Skatteverket det som rotarbete att reparera fönster och att måla fönster. Är huset yngre än fem år får arbetet bara återställa det ursprungliga skicket. Det är bara arbetad tid på plats hos dig som ger avdrag, inte arbete i en verkstad.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen på Lidingö?",
  "price": [
    "Antal bågar och hur skadade de är, hur mycket kitt och färg som ska bort, om nytt trä eller nya bågar behövs, glas, beslag och tätningslist, och hur många fönster som går att laga på plats. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("När antogs Lidingös nya kulturmiljöprogram?",
     "Kommunfullmäktige antog det den 16 december 2024. Det ersätter programmet från 1990."),
    ("Behöver jag bygglov för att renovera fönstren på min villa i Breviks villastad?",
     "Inte om fönstren får samma utseende som förut. Lov krävs om du ändrar fönstren i ett kulturhistoriskt värdefullt område."),
    ("Är Lidingös kulturmiljöprogram juridiskt bindande?",
     "Nej, staden beskriver det som ett kunskapsunderlag, men det används som stöd när bygglov prövas."),
    ("Går det att få äldre beskrivningar av mitt hus på Lidingö?",
     "Ja, staden har inventeringar från 1970–80-talen och 2013–2015 och lämnar ut dem via kundcenter."),
  ],
  "sources": [_LID_KMP, _LID_FAQ, _LID_VAD, _RAA, _SKV, _SKV_SA],
  "cta": ("Vill du renovera fönstren på Lidingö?", "Boka ett gratis platsbesök, så går vi igenom fönstren och webbkartan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa från början av 1900-talet med spröjsade fönster bland tallar",
     "early 1900s Swedish wooden villa painted light yellow with white small-paned windows and a glazed veranda, standing among tall pine trees on a rocky plot, summer daylight" + _SFX),
    ("Fönsterbåge med nytt kitt och ny grundfärg",
     "close view of an old wooden window sash lying on a workbench, fresh linseed putty along the glass edges and new white primer on the wood, putty knife beside it, soft daylight" + _SFX),
    ("Renoverat fönster med tätningslist på insidan",
     "interior view of an old white painted coupled wooden window with a new thin weatherstrip along the inner sash, plants on the deep sill, light through the glass" + _SFX),
  ],
},

# ------------------------------------------------------------------ SUNDBYBERG
"fonsterrenovering-sundbyberg.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Sundbyberg", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Sundbyberg – villorna i Duvbo",
  "description": "Fönsterrenovering i Sundbyberg: Duvbos egnahemsvillor, utökad lovplikt för fönsterbyte, kopplade bågar från sekelskiftet och rotavdrag.",
  "h1": "Fönsterrenovering i Sundbyberg",
  "lead": "I Duvbo kräver det bygglov att byta ut ett fönster, och stadens miljöprogram säger att husens tidstypiska uttryck inte får förvanskas. För många villaägare är renovering därför det naturliga valet. Geal Entreprenad AB renoverar fönster i Duvbo och övriga Sundbyberg så att de gamla bågarna fungerar och håller tätt igen.",
  "card": "Egnahemsvillornas fönster i Duvbo.",
  "sections": [
    {"id": "duvbo-sundbyberg", "anchor": "Duvbo",
     "h2": "En av landets första egnahemsmiljöer",
     "paras": [
       "Sundbybergs miljöprogram för Duvbo berättar att föreningen Egna Hem bildades i Stockholm 1898 för att skapa egna hem för arbetare. Året därpå köpte föreningen egendomen Dufvebol i Spånga församling och gjorde en stadsplan med 325 tomter. Duvbo växte snabbt fram som en av landets första egnahemsmiljöer, och 1924 utökades området västerut med ytterligare 98 villatomter.",
       "Riksantikvarieämbetet pekade 1987 ut Duvbo som riksintresse för kulturmiljövården, med motiveringen att det är ett av de första exemplen på en välorganiserad egnahemsförstad i Stockholmstrakten. Programmet betonar att det i första hand är samhället som helhet som är värdefullt, inte de enskilda husen.",
     ],
     "aside": {"title": "Duvbo enligt miljöprogrammet", "items": [
       "Egna Hem bildades 1898", "325 tomter i första planen", "98 tomter till 1924", "Riksintresse sedan 1987"]}},
    {"id": "lov-sundbyberg", "h2": "Fönsterbyte kräver lov i Duvbo",
     "paras": [
       "I samband med en planändring utökades bygglovsplikten i Duvbo. Enligt miljöprogrammet omfattar den bland annat utbyte av fasadbeklädnad och takmaterial, omfärgning av fasaden och utbyte, flyttning eller igensättning av fönster och dörrar. Åtgärder inom den utökade lovplikten är kostnadsfria att söka lov för.",
       "Programmet ger också rådet att byggnadens tidstypiska uttryck inte får förvanskas genom ändringar som byte av fönster, fasad- och takmaterial eller färgsättning, och att material och utförande vid underhåll om möjligt ska följa originalet. Det ger också rådet att äldre hus som förändrats kraftigt om möjligt anpassas bättre till omgivningen i samband med andra åtgärder. En renovering som behåller bågarna ändrar inget av detta. Ska fönstren ändå bytas finns " + _L.format("fonsterbyte-sundbyberg.html", "fönsterbyte i Sundbyberg") + ".",
     ],
     "aside": {"title": "Utökad lovplikt i Duvbo", "items": [
       "Utbyte av fönster och dörrar", "Flyttning eller igensättning", "Omfärgning av fasaden", "Lovet är kostnadsfritt"]}},
    {"id": "kopplade-sundbyberg", "h2": "Kopplade bågar från sekelskiftet",
     "paras": [
       "Husen i Duvbo byggdes enligt programmet framför allt vid sekelskiftet 1900 och under 1920-talet, med en senare grupp från 1930- och 40-talen. Sekelskiftesvillorna byggdes ofta av ägarna själva och visar en rik provkarta på tidens smakriktningar, med fasader indelade i fält av stående och liggande spontpanel och snickarglada detaljer. Både de äldre och de yngre husen står i två våningar på höga socklar. Riksantikvarieämbetets skrift om fönster berättar att kopplade fönsterbågar började införas mot slutet av 1800-talet; patentet på fönster med kopplade bågar beviljades 1889. Från sekelskiftet blev de kopplade, inåtgående bågarna allt vanligare.",
       "I ett kopplat fönster hänger den yttre bågen på den inre, som därför ofta är kraftigare. Eftersom husen är så olika ser fönstren också olika ut från villa till villa. När vi renoverar tar vi isär bågparet, lagar och målar båda delarna och sätter ihop dem med beslagen justerade, så att paret sluter tätt mot karmen igen.",
     ],
     "aside": None},
    {"id": "farg-sundbyberg", "h2": "Färgen på fönstren",
     "paras": [
       "Miljöprogrammet beskriver att träfasaderna i Duvbo ursprungligen målades med linoljefärg eller slamfärg i tidstypiska jordnära kulörer, och att 1930- och 40-talshusen är slätputsade och avfärgade i ljusa kulörer. Programmet uppmanar husägare att kontakta stadens plan- och byggförvaltning för färgförslag.",
       "Riksantikvarieämbetet beskriver linoljefärg som en färg där bara linolja är bindemedel, med goda vätningsegenskaper. Vi målar fönstren med linoljefärg i den kulör huset har, och omfärgning av fasaden är inget som ingår i en fönsterrenovering. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte och fönsterrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönster i Sundbyberg",
  "steps": [
    ("Platsbesök", "Gratis genomgång av bågar, karmar och beslag."),
    ("Plan", "Vi kontrollerar om huset ligger i Duvbo."),
    ("Isärtagning", "Kopplade bågar tas isär och märks."),
    ("Lagning", "Skrapning, nytt trä och omkittning."),
    ("Målning", "Linoljefärg i husets befintliga kulör."),
    ("Montering", "Justering, tätning och genomgång."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Sundbyberg",
  "rot": [
    "Skatteverket räknar reparation av fönster och målning av fönster i småhus som rotarbete. Avdraget gäller bara arbetad tid på plats hos dig, inte arbete i en verkstad. Bor du i en bostadsrätt gäller det bara arbete på insidan av fönstren.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Sundbyberg?",
  "price": [
    "Antal kopplade bågar, skadornas omfattning, mängden kitt och färg som ska bort, nytt trä, beslag och tätning och om arbetet görs på plats. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag bygglov för att byta fönster på min villa i Duvbo?",
     "Ja. Den utökade lovplikten i Duvbo omfattar utbyte, flyttning och igensättning av fönster och dörrar. Lovet är kostnadsfritt."),
    ("Kräver en fönsterrenovering i Duvbo bygglov?",
     "Inte om fönstren behåller sitt utseende. Lovplikten gäller utbyte, flyttning och igensättning."),
    ("När började man använda kopplade fönsterbågar?",
     "Mot slutet av 1800-talet. Riksantikvarieämbetet nämner ett patent från 1889, och från sekelskiftet blev de allt vanligare."),
    ("Varför är Duvbo riksintresse?",
     "Riksantikvarieämbetet pekade ut området 1987 som ett av de första exemplen på en välorganiserad egnahemsförstad i Stockholmstrakten."),
  ],
  "sources": [_DUVBO, _SUND_FAS, _RAA, _SKV, _SKV_SA],
  "cta": ("Vill du renovera fönstren i Duvbo?", "Boka ett gratis platsbesök, så går vi igenom bågarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla i trä med snickarglädje och spröjsade fönster",
     "Swedish wooden villa from around 1900 with vertical and horizontal panel fields, decorative fretwork on the gables, white coupled windows, red clay tile roof, mature fruit trees in the garden, summer" + _SFX),
    ("Kopplat fönster med inre och yttre båge isärtagna",
     "an old coupled wooden window with the inner and outer sashes separated and leaning side by side in a workshop, old hinges visible, scraped paint, soft daylight" + _SFX),
    ("Nymålade fönster i en träfasad",
     "close view of freshly painted white coupled windows in an ochre wooden panel facade of an old villa, new putty lines, clean glass reflecting trees, summer daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ TYRESÖ
"fonsterrenovering-tyreso.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Tyresö", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Tyresö – från sommarstuga till året runt",
  "description": "Fönsterrenovering i Tyresö: 1950-talets fritidshus som blir permanentbostäder, äldre bågar och beslag i Solberga och rotavdrag för villan.",
  "h1": "Fönsterrenovering i Tyresö",
  "lead": "I östra Tyresö styckades Tyresögodsets marker till fritidshus, och många av dem används i dag året runt. När ett sådant hus byggs om är det lätt att byta alla fönster, men de gamla bågarna går ofta att rädda. Geal Entreprenad AB renoverar fönster i Tyresö och kompletterar dem så att de klarar ett permanent boende.",
  "card": "Fritidshus som blivit permanentbostäder.",
  "sections": [
    {"id": "godset-tyreso", "anchor": "Fritidshusen",
     "h2": "Godsets marker blev fritidstomter",
     "paras": [
       "Stockholms läns museums kulturmiljöunderlag för Solberga och en del av Raksta berättar att Lagergrens söner bildade ett bolag för att sälja tomter till fritidshus på Tyresögodsets mark. Efter andra världskriget ökade exploateringstrycket, och vid slutet av 1950-talet hade nästan hälften av det gamla godset bebyggts med fritidshus. För Solberga fastställdes en byggnadsplan 1952, som rapporten beskriver som i huvudsak gällande än i dag.",
       "Rapporten skriver att fler har bosatt sig permanent i området och att permanentningen pågår: en del hus är helt ombyggda eller nybyggda, medan andra är välbevarade fritidshus från 1950-talet. Ett exempel som nämns har röd stockpanel med gröna lister och foder och ett tak av tvåkupigt tegel.",
     ],
     "aside": {"title": "Solberga enligt rapport 2008:31", "items": [
       "Byggnadsplan 1952", "Fritidshus från 1950-talet", "Permanentning pågår", "Stora tomter i naturmark"]}},
    {"id": "aldre-tyreso", "h2": "Äldre bågar och beslag",
     "paras": [
       "Rapporten beskriver också de äldre husen i området i detalj. I Strömstugan har fönstren tre rutor per båge med pressade hörnjärn, som var vanliga under 1900-talets första hälft, och bågarna är kopplade med raka uppställningsbeslag av 1800-talstyp på insidan. I ett annat hus är fönstren sexrutiga med tre rutor per båge, och flera äldre bågar har gångjärn av sen 1800-talstyp.",
       "Beslag av det slaget är svåra att ersätta med nya av samma utseende. Vid en renovering tar vi loss, rengör och sätter tillbaka de gamla beslagen, och byter bara det som är trasigt. Riksantikvarieämbetets skrift om fönster nämner komplettering med nya beslag som en möjlighet när de gamla inte räcker.",
     ],
     "aside": {"title": "Detaljer som rapporten nämner", "items": [
       "Tre rutor per båge", "Pressade hörnjärn", "Kopplade bågar", "Beslag av 1800-talstyp"]}},
    {"id": "permanent-tyreso", "h2": "Permanentstandard med de gamla detaljerna",
     "paras": [
       "Om huvudbyggnaden på Solberga gård skriver rapporten att den nyligen genomgått en omfattande renovering där målet varit att nå permanentstandard och samtidigt behålla de gamla detaljerna. Samma tanke fungerar för fönstren i ett fritidshus som ska bli åretruntbostad.",
       "Riksantikvarieämbetet skriver att ett äldre fönster kan kompletteras med tätningslister eller en innerbåge för att klara dagens krav på energi och ljud. Har stugan enkla bågar kan en innerbåge göra stor skillnad vintertid. Vi bedömer på platsen vilka fönster som klarar en komplettering och vilka som behöver nya bågar. Ska fönstren bytas helt finns " + _L.format("fonsterbyte-tyreso.html", "fönsterbyte i Tyresö") + ".",
     ],
     "aside": None},
    {"id": "farg-tyreso", "h2": "Kulören på fönster och foder",
     "paras": [
       "Tyresö kommun skriver att det inte krävs bygglov inom detaljplan för att måla om ett en- och tvåbostadshus, men att detaljplanen kan ha bestämmelser om vilka färger och fasadmaterial husen får ha. För kulturhistoriskt värdefulla byggnader gäller utökad lovplikt.",
       "Rapporten beskriver flera av de äldre husen med rödfärgad locklistpanel och vita knutar, lister, fönster och foder. När vi målar om fönster och foder behåller vi därför husets kulör, till exempel vita eller gröna lister mot en röd panel. Vill du ändra färgen kontrollerar vi detaljplanen i kommunens webbkarta först. Mer om tjänsten finns under " + _L.format("fonsterbyte.html", "fönsterbyte och fönsterrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönster i Tyresö",
  "steps": [
    ("Platsbesök", "Gratis genomgång av bågar, beslag och karmar."),
    ("Förslag", "Renovering, tätning eller innerbåge."),
    ("Nedmontering", "Bågar och beslag märks och tas loss."),
    ("Lagning", "Skrapning, nytt trä och omkittning."),
    ("Målning", "Fönster och foder i husets kulör."),
    ("Montering", "Beslagen tillbaka, justering och tätning."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Tyresö",
  "rot": [
    "Skatteverket godkänner reparation av fönster och målning av fönster i småhus som rotarbete, även i ett fritidshus som du äger och kan använda. Skatteverket skriver att bara arbetad tid på plats hos dig ger rätt till avdrag.",
    _ROT_SUM,
  ],
  "price_h2": "Vad påverkar priset för fönsterrenoveringen i Tyresö?",
  "price": [
    "Antal bågar och rutor, hur mycket röta och gammalt kitt som ska åtgärdas, om glas behöver bytas, om beslag ska renoveras eller kompletteras, innerbågar eller tätningslister och om bågarna lagas på plats. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan fönstren i ett fritidshus från 1950-talet i Tyresö renoveras för åretruntboende?",
     "Ofta ja. Riksantikvarieämbetet nämner tätningslister och innerbåge som sätt att möta dagens krav på energi och ljud."),
    ("Behöver jag bygglov för att måla om fönstren på min villa i Tyresö?",
     "Nej, inte inom detaljplan för ett en- eller tvåbostadshus. Detaljplanen kan däremot ange vilka färger som gäller."),
    ("Går det att behålla gamla fönsterbeslag när fönstren renoveras?",
     "Ja. Vi rengör och sätter tillbaka de gamla beslagen och kompletterar bara det som saknas eller är trasigt."),
    ("När fastställdes byggnadsplanen för Solberga?",
     "Enligt Stockholms läns museums rapport 2008:31 fastställdes den 1952."),
  ],
  "sources": [_SOLB, _TYR_MALA, _RAA, _SKV, _SKV_SA],
  "cta": ("Vill du renovera fönstren i Tyresö?", "Boka ett gratis platsbesök, så går vi igenom bågar och beslag innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Rödfärgat fritidshus från 1950-talet i skogsmark",
     "small 1950s Swedish summer cottage with red vertical log panelling, green window frames and trims, a two-wave clay tile roof, set among pine trees and rocks on a large natural plot, summer daylight" + _SFX),
    ("Äldre fönsterbåge med tre rutor och gamla beslag",
     "close view of an old white painted wooden window sash with three panes, small pressed metal corner irons and old hinges, lying on a workbench during renovation, soft daylight" + _SFX),
    ("Innerbåge monterad i ett äldre fönster",
     "interior view of an old cottage window fitted with an added inner wooden sash with clear glass, painted white, wooden panelled wall around it, plants on the sill, daylight" + _SFX),
  ],
},
}
