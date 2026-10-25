# -*- coding: utf-8 -*-
"""Fasadrenovering – ortsidor v10: Haninge, Järfälla, Värmdö, Norrtälje, Upplands Väsby, Hässelby (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25: Haninge kommun (Haninges
karaktärsmiljöer, WSP 2019, uppdaterad nov. 2020: folkhemsbygget, rekordårens småhus, landsbygdens hustyper;
Fasadändring), Järfälla kommun (Kulturmiljöplan, inledning och Stäket: Biskop Olovs väg, Enköpingsvägen–
Gyllenstiernas väg, Bonäs–Trappeberg, Ryttarstugan; Fasadändring), Värmdö kommun (Detaljplan PFO I7 Fågelvik–
Nykvarn, planbeskrivning, granskningshandling 2023-06-12; Bygga i kulturmiljöer; Bygglov vid fasadändring;
Förändringar i PBL från 1 december 2025), Norrtälje kommun (Kulturmiljöutredning nr 20 Hallstavik och nr 5
Grisslehamn, 2016; Fasadändring), Upplands Väsby kommun (Kunskapsunderlag för kulturmiljö 2025: Grimstaby,
Bo 85 Runby Backar och Carlslund; Fasadändring), Stockholms stad (bygglov.stockholm: Fasadändring, Stadsmuseets
kulturhistoriska klassificering; Varsam utveckling av småhus- och villaområden; Områdesfakta Hässelby villastad
2025), Stockholmshem/BOOM-gruppen KTH via Stockholmskällan (Västra Smedshagen, Hässelby Villastad, 1996, ocr),
Boverket (PBL kunskapsbanken: fasadändring; energiguiden: tilläggsisolera fasaden; fuktrisker med fasadmaterial
och ytskikt; risker med enstegstätning; asbest), Arbetsmiljöverket (tillstånd för rivning av asbest) och
Skatteverket (rotavdrag).
Strukna (ej verifierade eller oklara i källan): försäljningssumman för TV-villan vid Biskop Olovs väg (belopp),
om Fågelvik–Nykvarn-planen har antagits (bara granskningshandlingen läst), fasadmaterial på Hallstaviks
1920-talsegnahem (källan anger inte material), Grisslehamns sommarvillors material och kulörer, att
Grimstabys fönster är "utformade i plåt" (oklar formulering), byggår och material för Hässelbys tidiga
arbetarvillor (källan anger inte), Stadsmuseets inventering av Hässelby villastad (inte läst), att
Värmdös kulturmiljöprogram Skärgårdsbygd (2014) beskriver Fågelvik (inte läst), uppgifter om slagregn och
vind per ort. Inga priser, garantier, omdömen, egna uppdrag eller cert.
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_FASAD = ("Boverket – PBL kunskapsbanken: Bygglov för fasadändring",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_BV_ISOL = ("Boverket – Energiguiden: Tilläggsisolera fasaden",
            "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/tillaggsisolera-fasaden/")
_BV_FMAT = ("Boverket – Fuktrisker med fasadens material och ytskikt",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/")
_BV_ENST = ("Boverket – Risker med enstegstätning",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/risker-enstegstatning/")
_BV_ASB = ("Boverket – Asbest", "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_AV_ASB = ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest",
           "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_STH_FASAD = ("Stockholms stad – Fasadändring (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_JAR_STA = ("Järfälla kommun – Kulturmiljöplan för Järfälla: Stäket (pdf)",
            "https://www.jarfalla.se/download/18.68e7a727168e12dd179a407e/1550245842779/kulturmiljoplan-staket.pdf")
_JAR_INL = ("Järfälla kommun – Kulturmiljöplan för Järfälla: inledning (pdf)",
            "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4052/1550245824984/kulturmiljoplan-inledning.pdf")
_UV_KUN = ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö i Upplands Väsby (2025, pdf)",
           "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ HANINGE
"fasadrenovering-haninge.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Haninge", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Haninge – tegel, mexi och panel",
  "description": "Fasadrenovering i Haninge: tegel som inte ska putsas, mexitegel och panel i grupphusen, timmerhus på landet och lovfrågan. Gratis platsbesök.",
  "h1": "Fasadrenovering i Haninge",
  "lead": "Haninges kulturmiljöprogram delar in småhusen efter byggepok, och för varje epok finns råd om just fasaden. En tegelvilla från 1950-talet, ett grupphus i mexitegel från 1970-talet och en panelad gård på landet kräver tre olika sätt att renovera. Geal Entreprenad AB renoverar fasader i Handen, Jordbro, Vendelsö, Västerhaninge och övriga Haninge, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Tegelvillor, grupphus och panelade gårdar.",
  "sections": [
    {"id": "folkhemmet", "anchor": "Villorna från 1940- och 50-talen",
     "h2": "Folkhemmets villor: tegel ska förbli tegel",
     "paras": [
       "Programmet Haninges karaktärsmiljöer, som WSP tog fram åt kommunen 2019 och som senast uppdaterades i november 2020, beskriver 1940-talets småhus som enkla en- eller tvåplansvillor i trä, puts eller fasadtegel. På 1950-talet blev fasaderna mer sammansatta: rött eller gult tegel kombinerat med grov spritputs eller med trä i mustiga kulörer. Exempel på sådana områden finns enligt programmet i Handen, Jordbro, Vendelsö, Vendelsömalm och Västerhaninge.",
       "Råden är konkreta. Fasadändringar som avviker från husets ursprungliga utformning ska undvikas, och programmet tar själv exemplet att en fasad i tegel inte ska putsas. Dörrar och fönster räknas som en bärande del av karaktären, och programmet påpekar att även mindre fasadändringar kan påverka ett helt kvarter.",
       "För en tegelvilla handlar renoveringen därför om att laga murverket och byta skadade stenar i stället för att dölja det. Spritputsen lagas med en puts som liknar den gamla i struktur. Boverket konstaterar att putsbortfall nästan undantagslöst beror på fukt, så vi letar efter orsaken, till exempel ett läckande bleck eller ett stuprör, innan någon yta åtgärdas.",
     ],
     "aside": {"title": "1940- och 50-talens villor", "items": [
       "Trä, puts eller fasadtegel", "Tegel tillsammans med spritputs",
       "Tegelfasad ska inte putsas", "Dörrar och fönster bär karaktären"]}},
    {"id": "rekordaren", "h2": "Grupphus i mexitegel och panel",
     "paras": [
       "Rekordårens småhus från 1960- till 1980-talet ligger oftast i grupper där samma volym upprepas längs gatan, till exempel i Jordbro, Brandbergen, Västerhaninge och Handen. Programmet nämner tegel och kalksandsten, så kallat mexitegel, gärna i kombination med panel. Mot 1980-talet blev färgerna ljusare och dekorativa snickerier kom tillbaka.",
       "Programmet säger att husens typiska fasadutformning när det gäller materialval och färgsättning ska värnas, och att större exteriöra ändringar som tilläggsisolering mot allmän plats bör undvikas. Byter du panel på ett radhus är det alltså klokt att välja samma profil och riktning som grannarna har.",
       "Hus från den här tiden kan innehålla asbest. Boverket skriver att det är sannolikt i byggnader uppförda 1940–1980 och att provtagning är det enda säkra sättet att veta. Visar provet asbest i en fasadbeklädnad ska rivningen enligt Arbetsmiljöverket göras av ett företag med tillstånd, som ska söka det åtta veckor innan arbetet börjar. Taket ses ofta över samtidigt, och mer om det finns under " + _L.format("takrenovering-haninge.html", "takrenovering i Haninge") + ".",
     ],
     "aside": None},
    {"id": "landsbygden", "h2": "Panelade timmerhus på landsbygden",
     "paras": [
       "På Haninges landsbygd är trä och sten de vanligaste materialen. Programmet beskriver hur timmerstommarna under 1800-talet kläddes med stående panel, oftast locklist- eller lockribbpanel, och hur liggande panel förekom från 1800-talets mitt. De större boningshusen fick ibland reverterade fasader, vilket innebär att trästommen putsades. Tegel och senare tillägg av plåtfasader räknar programmet som främmande material på landsbygden.",
       "Ett av råden är riktat direkt till den som har ett hus som redan har tilläggsisolerats: vid en fasadändring kan fasaden med fördel återställas, och ny isolering kan i stället göras inifrån. Boverket beskriver avvägningen. Utvändig isolering är ofta bäst för energi och fukt men kan ge fönster som hamnar djupt in och en vägg som hänger ut över sockeln. Invändig isolering lämnar fasaden orörd men gör väggen kallare, vilket ökar risken för röta i trä och frostsprängning i tegel och sten.",
       "Vi börjar därför med att undersöka vad som finns under den nuvarande panelen. Ibland finns den gamla locklistpanelen kvar under en senare inklädnad, och då kan den ofta lagas och sparas. Om kulören finns mer under " + _L.format("malare-haninge.html", "målare i Haninge") + ".",
     ],
     "aside": {"title": "På en gård i Haninge", "items": [
       "Locklist- eller lockribbpanel", "Reverterad, putsad trästomme",
       "Plåtfasad är främmande", "Isolera hellre inifrån"]}},
    {"id": "lov-haninge", "h2": "Lovfrågan när kartan inte är klar",
     "paras": [
       "Sedan den 1 december 2025 behövs normalt inget bygglov för att byta kulör eller fasadmaterial på ett en- eller tvåbostadshus. Boverket påpekar att det ändå kan krävas lov om huset omfattas av utökad lovplikt, i plan- och bygglagen eller i detaljplanen. Haninge kommun skriver att lov behövs om fasaden ändras på en byggnad eller i ett område som är särskilt värdefullt, och att stora delar av Haninge är kulturmiljöer.",
       "Kommunen uppdaterar just nu det digitala kartskiktet som visar de särskilt värdefulla kulturmiljöerna. Tills det är klart får du kontakta bygglovsenheten för att veta om din fastighet omfattas. Det går också att söka frivilligt lov. Krävs lov behöver byggherren även en kontrollplan, och kommunen har lagt ut ett exempel på en kontrollplan för fasadändring. Mer om material och metoder står på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Haninge till",
  "steps": [
    ("Epok och material", "Vi tar reda på när huset byggdes och vilket fasadmaterial det hade från början."),
    ("Platsbesök", "Tegel, puts, panel, sockel och bleck gås igenom, och vi noterar var fukten kommer in."),
    ("Prov vid behov", "På hus från 1940–1980 föreslår vi prov på misstänkt material innan något rivs."),
    ("Skriftligt kostnadsförslag", "Lagning, byte och eventuell isolering beskrivs och prissätts var för sig."),
    ("Lovfrågan", "Vi hjälper dig att formulera frågan till bygglovsenheten om fastigheten kan vara särskilt värdefull."),
    ("Utförande och genomgång", "Arbetet görs i torrt väder, och vi går runt huset tillsammans när det är klart."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Haninge",
  "rot": [
    "För ett småhus räknar Skatteverket in att byta och reparera fasader, tilläggsisolera, måla fasader och reparera eller byta fönster. Även att sanera asbest i samband med byggarbete ger rotavdrag, medan en mätning av asbest i sig inte gör det.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Haninge?",
  "price": [
    "Hur stor del av murverket eller panelen som är skadad, om fogar och puts måste lagas, om provtagning behövs och om en äldre inklädnad ska tas bort. På en gård med flera byggnader görs varje hus till en egen post. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag putsa över teglet på min villa från 1950-talet i Haninge?",
     "Kommunens kulturmiljöprogram avråder uttryckligen och tar själv exemplet att en fasad i tegel inte ska putsas. Bättre är att laga fogar och byta skadade stenar."),
    ("Vad är mexitegel?",
     "Kalksandsten, ett murmaterial som programmet nämner bland de vanliga fasadmaterialen i Haninges grupphus från 1960- och 70-talen, gärna kombinerat med träpanel."),
    ("Ska ett tilläggsisolerat gammalt hus på landet i Haninge få tillbaka sin panel?",
     "Programmet anser att fasaden med fördel kan återställas vid en fasadändring och att ny isolering kan göras inifrån. Boverket varnar samtidigt för fuktrisker med invändig isolering, så lösningen behöver anpassas efter väggen."),
    ("Hur vet jag om mitt hus i Haninge ligger i en särskilt värdefull kulturmiljö?",
     "Kommunen håller på att uppdatera kartskiktet. Fram till dess ger bygglovsenheten besked om din fastighet, och du kan också söka frivilligt lov."),
    ("Måste fasadskivorna på vårt radhus i Jordbro testas för asbest?",
     "Är huset byggt mellan 1940 och 1980 bedömer Boverket att asbest är sannolik någonstans i byggnaden, och bara ett prov kan ge besked. Vi föreslår prov innan skivor tas ner."),
  ],
  "sources": [
    ("Haninge kommun – Haninges karaktärsmiljöer, kulturmiljöprogram (WSP 2019, uppdaterad 2020, pdf)",
     "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf"),
    ("Haninge kommun – Fasadändring",
     "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/fasadandring/"),
    _BV_FASAD, _BV_ISOL, _BV_FMAT, _BV_ASB, _AV_ASB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset i Haninge renoveras?", "Boka ett gratis platsbesök så går vi igenom tegel, puts eller panel och vad som bör sparas."),
  "img": [
    ("Villa från 1950-talet med fasad i rött tegel och partier av ljus spritputs i Haninge",
     "1950s Swedish single-storey suburban villa with a facade combining red brick walls and light beige rough dash render panels, low pitched tiled roof, small front garden with a low hedge, birch and pine trees, Handen Haninge, overcast autumn daylight, no people"),
    ("Hörn på en tegelfasad där några stenar och fogar har lagats vid sockeln",
     "close-up of the lower corner of a red brick villa facade in Sweden where a few bricks and mortar joints near the concrete plinth have been newly repaired, a downpipe and a metal window sill flashing above, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"fasadrenovering-jarfalla.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Järfälla", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Järfälla – Stäkets villor och kedjehus",
  "description": "Fasadrenovering i Järfälla: spontpanel på kedjehusen vid Biskop Olovs väg, sekelskiftesvillor i Stäket, asbest i 60-talshus och lov. Gratis platsbesök.",
  "h1": "Fasadrenovering i Järfälla",
  "lead": "I Stäket, där Järfälla möter Upplands-Bro, finns några av kommunens mest beskrivna fasader: villor från försöket att skapa ett exklusivt villasamhälle 1904 och kedjehus från 1960 med en noga genomtänkt färgsättning. Kommunens kulturmiljöplan säger vad som bör behållas på dem. Geal Entreprenad AB renoverar fasader i Stäket, Jakobsberg, Kallhäll och övriga Järfälla, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Kedjehus, sekelskiftesvillor och parstuga i Stäket.",
  "sections": [
    {"id": "biskop-olovs-vag", "anchor": "Kedjehusen i Stäket",
     "h2": "Biskop Olovs väg: spontpanelen ska inte bli lockpanel",
     "paras": [
       "Kedjehusen vid Biskop Olovs väg byggdes 1960. Eftersom kommunalt vatten och avlopp saknades rådde byggnadsförbud i Stäket, men ingenjören Joel Liljendahl konstruerade ett separat avloppssystem av vakuumtyp, och då gavs dispens. I området ligger också den så kallade TV-villan, som enligt kulturmiljöplanen byggdes färdig på fyra dagar och auktionerades ut i Lennart Hylands program Stora famnen i maj 1959.",
       "Planen beskriver fasaderna i detalj. Vid gatans södra del har husen spontad träpanel, med bottenvåningarna i ljusgrått och gavlarna i övervåningen i omväxlande brunt, rött och grönt. I den norra delen är bottenvåningarna i stället klädda med rött fasadtegel. Taken är täckta med rött lertegel.",
       "Rekommendationen är att inga förändringar ska göras mot gatan och att den spontade träpanelen ska behållas vid renoveringar i stället för att bytas mot exempelvis grövre lockpanel. Vid ett panelbyte tar vi därför mått på den befintliga profilen och beställer samma, och tillbyggnader hänvisar planen till trädgårdssidan.",
     ],
     "aside": {"title": "Biskop Olovs väg", "items": [
       "Kedjehus från 1960", "Spontad träpanel i söder",
       "Rött fasadtegel i norr", "Inga ändringar mot gatan"]}},
    {"id": "villasamhallet", "h2": "Villasamhället från 1904 och Ryttarstugan",
     "paras": [
       "Från Almarestäkets gård styckades tomter i ett försök att skapa ett villasamhälle av samma slag som Djursholm och Saltsjöbaden. De första villorna byggdes 1904 på branten ner mot järnvägen, och tomterna var ursprungligen stora, upp mot 2 000 kvadratmeter. Planen beskriver träpanel i olika former som det vanliga fasadmaterialet, men puts förekommer också. Färgsättningen hölls från början i rött eller ljusa oljefärger.",
       "Vid Bonäs och Trappeberg finns tre välbevarade villor: Hallbergska villan från 1907 med liggande rödfärgad panel, en ljusputsad villa vid Trappeberg och en villa på Bonäsvägen 27 med gulmålad träpanel. Ryttarstugan på Dragonvägen 2 är kommunens enda kvarvarande parstuga, timrad och klädd med locklistpanel i falurött.",
       "För Gyllenstiernas väg anger planen att något skydd för de kulturhistoriska värdena saknas i stadsplanen, och den föreslår utökad lovplikt med krav på material och färgsättning vid renoveringar. På sådana hus lagar vi hellre panelen än byter den, och om färgen finns mer under " + _L.format("malare-jarfalla.html", "målare i Järfälla") + ".",
     ],
     "aside": None},
    {"id": "dolt", "h2": "Där tegel möter panel – och det som kan finnas bakom",
     "paras": [
       "På ett kedjehus med tegel i bottenvåningen och panel ovanför är skarvarna de svaga punkterna. Boverket beskriver hur anslutningar mot fönster, dörrar och stuprör behöver tätas i mer än en nivå, så kallad tvåstegstätning, så att vatten som kommer förbi det yttre skiktet kan rinna ut igen. Fogar av mjukfog har enligt Boverket visat sig kunna ha en relativt kort livslängd även när de är väl utförda.",
       "Hus från den här tiden kan också dölja asbest. Boverket skriver att många fasader under 1940- och 50-talen kläddes med cementfiberplattor med asbest, att plattorna förbjöds på 1970-talet och att fibrer kan frigöras om man borrar i dem. Uppgifter kan finnas i bygglovshandlingarna, men enligt Boverket är bara prov säkra.",
       "Ska fönstren bytas samtidigt som fasaden görs om finns mer under " + _L.format("fonsterbyte-jarfalla.html", "fönsterbyte i Järfälla") + ". Ett gemensamt kostnadsförslag gör det lättare att planera blecken och anslutningarna runt de nya fönstren.",
     ],
     "aside": {"title": "Kontrollera vid besöket", "items": [
       "Fogar mellan tegel och karm", "Bleck under fönstren",
       "Stuprörens infästningar", "Äldre fasadskivor"]}},
    {"id": "lov-jarfalla", "h2": "Bygglov och anmälan i Järfälla",
     "paras": [
       "Järfälla kommun skriver att det inte krävs bygglov för fasadändringar på en- och tvåbostadshus och deras komplementbyggnader, men att det inte gäller om ändringen görs på en byggnad eller i ett område som är särskilt värdefullt. Lov krävs också om detaljplanen har utökad lovplikt. En anmälan krävs om byggnadens bärande konstruktion påverkas väsentligt, vilket kan bli aktuellt om en fönsteröppning flyttas.",
       "Kulturmiljöplanen blev klar 2001, uppdaterades i samband med arbetet med översiktsplanen och digitaliserades 2016. Planens förslag om utökad lovplikt är förslag som blir bindande när de förs in i en detaljplan, men ligger ett hus i ett särskilt värdefullt område gäller lovplikten ändå. Kommunen påpekar att även lovfria fasadändringar ska utföras varsamt, och att det går att söka frivilligt bygglov för att få ett säkert besked. Fler råd om material finns på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Järfälla till",
  "steps": [
    ("Läs planen", "Vi går igenom vad kulturmiljöplanen och detaljplanen säger om just ditt område."),
    ("Mät profilen", "Panelens dimension och profil mäts så att nytt virke kan beställas likadant."),
    ("Prov på skivor", "Äldre fasadskivor provas innan de tas ner, så att rätt hantering kan planeras."),
    ("Skriftligt kostnadsförslag", "Panel, fogar, bleck och anslutningar redovisas som egna poster."),
    ("Utförande", "Skadat virke byts eller lagas, och anslutningarna mot fönster och tegel görs om."),
    ("Genomgång", "Vi visar vad som har gjorts och vilka delar som bör ses över framöver."),
  ],
  "rot_h2": "ROT-avdrag för fasadarbete i Järfälla",
  "rot": [
    "I ett småhus ger både byte och reparation av fasader, tilläggsisolering och fasadmålning rotavdrag, liksom byggnadsställningar som monteras i samband med arbetet. Är kedjehuset en bostadsrätt ger fasaden inget avdrag, eftersom Skatteverket räknar den som gemensam yta.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Järfälla?",
  "price": [
    "Hur mycket panel som behöver bytas, om profilen måste specialbeställas, hur många fönsteranslutningar som ska göras om och om fasadskivor måste saneras. Branta tomter som de i Stäket kan påverka hur ställningen ställs upp. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Får vi byta till lockpanel på vårt kedjehus vid Biskop Olovs väg?",
     "Kulturmiljöplanen rekommenderar att den spontade träpanelen behålls och inte byts mot exempelvis grövre lockpanel. Kontrollera också om detaljplanen har fått utökad lovplikt innan något beställs."),
    ("Har Järfällas kulturmiljöplan juridisk verkan för min fasad?",
     "Planen innehåller beskrivningar och förslag. Bindande är detaljplanens bestämmelser och reglerna om särskilt värdefulla byggnader och områden, och varsamhetskravet gäller oavsett."),
    ("Vilken färg hade villorna i Stäket från början?",
     "Enligt kulturmiljöplanen hölls färgsättningen i villasamhället ursprungligen i rött eller ljusa oljefärger, och fasaderna var mest av träpanel."),
    ("Behövs anmälan om ett fönster flyttas när fasaden görs om?",
     "Järfälla kommun skriver att en anmälan krävs om byggnadens bärande konstruktion påverkas väsentligt. Att ta upp eller flytta en öppning kan göra det."),
    ("Hur vet jag om de gamla fasadskivorna innehåller asbest?",
     "Bara ett prov som analyseras ger säkert besked. Boverket nämner att bygglovsritningar kan ge en ledtråd men att uppgifterna kan vara osäkra."),
  ],
  "sources": [
    _JAR_STA, _JAR_INL,
    ("Järfälla kommun – Fasadändring",
     "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/vadvilldubyggaellerandra/fasadandring.4.1966aa14175c8663c9323310.html"),
    _BV_FASAD, _BV_FMAT, _BV_ENST, _BV_ASB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset i Järfälla ses över?", "Boka ett gratis platsbesök så går vi igenom panel, fogar och anslutningar och vad planen säger om ditt område."),
  "img": [
    ("Kedjehus från 1960 med ljusgrå spontpanel och färgade gavlar längs en böjd gata i Stäket",
     "row of 1960 Swedish one-and-a-half storey link houses along a gently curving street, ground floors clad in light grey tongue and groove wooden panel, upper gables painted alternately brown, red and green, steep red clay tile roofs, simple plain Scandinavian 1960s design without bay windows, small front gardens with low hedges, Stäket Järfälla, soft daylight, no people"),
    ("Spontad träpanel med nya bräder inskarvade under ett fönster",
     "close-up of light grey painted tongue and groove horizontal wooden facade panel on a Swedish 1960s house where a few new primed boards have been spliced in under a white window with a metal sill flashing, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VÄRMDÖ
"fasadrenovering-varmdo.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Värmdö", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering på Värmdö – sommarvillor och q-märkta hus",
  "description": "Fasadrenovering på Värmdö: 1910-talsvillor på Ingarö, anmälan för underhåll av skyddade hus, isolering av sommarhus och lov. Gratis platsbesök.",
  "h1": "Fasadrenovering på Värmdö",
  "lead": "När ett fritidshusområde på Värmdö planläggs för permanentboende kan husen få nya bestämmelser i detaljplanen, och några blir skyddade. Då kan även vanligt underhåll av fasaden kräva en anmälan. Geal Entreprenad AB renoverar fasader på Ingarö, i Gustavsberg, Hemmesta och övriga Värmdö kommun, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Sommarvillor, skyddade hus och helårsboende.",
  "sections": [
    {"id": "fagelvik", "anchor": "Villorna vid Lagnöström",
     "h2": "Fågelvik: villor från 1910-talet på Ingarö",
     "paras": [
       "Planbeskrivningen för området Fågelvik–Nykvarn på Ingarö, i granskningsversionen från juni 2023, berättar hur Aktiebolaget Ingarö Strand bildades 1909 och ägde bland annat Fågelviks gård. Huvudägaren James Funch började stycka av tomter för att sälja till sommargäster, och i sluttningen ner mot Lagnöström ligger flera av de villor som byggdes där, de flesta under 1910-talet.",
       "De äldsta villorna beskrivs som en stilblandning av jugend och nationalromantik. De flesta är byggda i trä i en och en halv våning, med träpanel och huvudsakligen brutna, tegelklädda sadeltak. Vissa är välbevarade medan andra har förändrats mycket, och under 1950- och 60-talen tillkom mindre fritidshus. Den smala grusvägen längs vattnet är den planerade strandpromenaden, som minner om planerna på en villastad likt Saltsjöbaden.",
       "Majoriteten av bebyggelsen i planområdet har träfasad. På en villa av den här åldern är det ofta de ursprungliga panelbrädorna och foderna som bär karaktären, och de går i många fall att laga bräda för bräda.",
     ],
     "aside": {"title": "Villorna i Fågelvik", "items": [
       "Byggda främst på 1910-talet", "Jugend och nationalromantik",
       "Träpanel och brutet tegeltak", "Glest, med utsikt mot vattnet"]}},
    {"id": "skyddade", "h2": "När detaljplanen sätter q eller k på huset",
     "paras": [
       "I planförslaget har de kulturhistoriskt intressanta byggnaderna värderats i en tregradig skala: blå för särskilt värdefulla, grön för högt och gul för visst kulturhistoriskt värde. Blå och gröna byggnader får rivningsförbud. Byggnader med särskilda värden får skyddsbestämmelser, märkta q, och byggnader med höga kulturmiljövärden får varsamhetsbestämmelser, märkta k.",
       "Planbeskrivningen påpekar att byggnader som omfattas av skyddsbestämmelser kräver en anmälan vid underhåll. Värmdö kommun skriver detsamma generellt: du behöver göra en anmälan och få startbesked om du ska underhålla en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde. Byggnadsminnen kräver dessutom tillstånd från länsstyrelsen.",
       "För en fasadrenovering betyder det att tidplanen ska rymma kommunens handläggning. Kommunantikvarien ger råd och föreslår att du fotograferar fastigheten och mejlar innan du bestämmer dig. Gäller det även taket finns mer under " + _L.format("takrenovering-varmdo.html", "takrenovering på Värmdö") + ".",
     ],
     "aside": None},
    {"id": "helarsboende", "h2": "Sommarhuset blir helårshus – isolera utan att förvanska",
     "paras": [
       "Syftet med planen för Fågelvik–Nykvarn är att anpassa området för permanentboende, och i ett hus som ska bebos året runt vill många tilläggsisolera. Boverket beskriver utvändig tilläggsisolering som ofta bäst för energi och fukt, men varnar för att den kan förändra huset: fönster och dörrar hamnar längre in, takfoten skjuter ut mindre och fasaden kan hänga ut över sockeln.",
       "Boverket råder också att isolera i torrt väder för att inte stänga in fukt i väggarna, och konstaterar att det blir lönsammast när fasaden ändå ska göras om, till exempel när panelen byts. På en sommarvilla med profilerade foder och snickerier kan det vara bättre att isolera på insidan eller bara i vissa väggar.",
       "I Fågelvik–Nykvarn reglerar planförslaget att lägsta grundläggningsnivå för huvudbyggnad är +2,7 meter (RH2000), eftersom havsnivån väntas stiga. För befintliga hus nära stranden är det ännu ett skäl att kontrollera sockeln och de nedersta brädorna. Ska snickerier som dörrar och fönster göras om finns " + _L.format("snickare-varmdo.html", "snickare på Värmdö") + ".",
     ],
     "aside": {"title": "Före isoleringen", "items": [
       "Är huset q- eller k-märkt?", "Ändras fönstrens läge?",
       "Räcker takfoten till?", "Torrt väder under arbetet"]}},
    {"id": "lov-varmdo", "h2": "Lov på Värmdö efter den 1 december 2025",
     "paras": [
       "Värmdö kommun skriver att det inte krävs bygglov för fasadändring, nytt tak eller nya fönster på en- och tvåbostadshus. Ligger fastigheten däremot i ett kulturhistoriskt särskilt värdefullt område, eller är byggnaden särskilt värdefull, krävs bygglov även för ommålning, nytt tak, nya fönster, solceller och takfönster. Kommunen hänvisar till sin kulturmiljökarta för att kontrollera det.",
       "Boverket förklarar att byte till samma material och utförande räknas som underhåll och inte som fasadändring. Ligger fastigheten inom strandskyddat område kan en åtgärd dessutom kräva strandskyddsdispens, påpekar kommunen. Läs mer om panel, puts och isolering på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering på Värmdö till",
  "steps": [
    ("Kartor och plan", "Vi tittar i kulturmiljökartan och detaljplanen efter q- och k-bestämmelser."),
    ("Platsbesök", "Panel, foder, sockel och anslutningar gås igenom, och vi bedömer vad som kan lagas."),
    ("Skriftligt kostnadsförslag", "Lagning, byte och isolering redovisas som egna poster med material angivna."),
    ("Anmälan eller lov", "Krävs anmälan eller bygglov planerar vi arbetet efter kommunens beslut."),
    ("Utförande", "Arbetet läggs i torra perioder, och logistiken planeras efter vägar och eventuell båttransport."),
    ("Genomgång", "Vi går igenom fasaden tillsammans och visar vilka delar som har bytts."),
  ],
  "rot_h2": "ROT-avdrag för fasaden på Värmdö",
  "rot": [
    "Skatteverket räknar fasadarbeten, tilläggsisolering, fasadmålning och fönsterbyte som rotarbete i ett småhus. Avdraget gäller bara arbetskostnaden, inte material eller resor.",
    "Det är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden på Värmdö?",
  "price": [
    "Hur mycket originalpanel som kan sparas, om profiler och foder måste tillverkas, om huset ska isoleras och hur långt det är till närmaste väg. Skyddade hus kan kräva mer lagning och mindre byte. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag göra en anmälan för att måla om eller laga fasaden på ett q-märkt hus på Värmdö?",
     "Ja, kommunen skriver att du behöver göra en anmälan och få startbesked om du ska underhålla en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde."),
    ("Vad betyder blå, grön och gul klassning i en detaljplan på Värmdö?",
     "Det är en tregradig värdering av kulturhistoriskt intressanta byggnader. Blått är särskilt värdefullt, grönt högt och gult visst kulturhistoriskt värde. I Fågelvik–Nykvarn får blå och gröna byggnader rivningsförbud."),
    ("Kan vi tilläggsisolera utvändigt på vår sommarvilla från 1910-talet?",
     "Det går, men Boverket varnar för att fönster, takfot och sockel kan få fel proportioner. På en villa med rika detaljer kan invändig eller partiell isolering vara bättre. Kontrollera först om huset har q- eller k-bestämmelse."),
    ("Krävs lov för att byta panel till samma sort på Värmdö?",
     "Enligt Boverket räknas byte till samma material och utförande som underhåll och inte som fasadändring. Är byggnaden skyddad i detaljplan kan underhållet ändå kräva anmälan."),
    ("Vem kan ge råd om fasaden på ett kulturhistoriskt hus i Värmdö kommun?",
     "Kommunantikvarien. Kommunen föreslår att du går runt i området, fotograferar fastigheten och mejlar dina frågor."),
  ],
  "sources": [
    ("Värmdö kommun – Detaljplan PFO I7 Fågelvik–Nykvarn, planbeskrivning, granskningshandling 2023-06-12 (pdf)",
     "https://www.varmdo.se/download/18.7146d8511884c6c1a3f47eef/1686725748924/Granskningshandling%20PFO%20I7%20Planbeskrivning%202023-06-12.pdf"),
    ("Värmdö kommun – Bygga i kulturmiljöer",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/byggaikulturmiljoer.4.57b4a3ba16e6b961dbf10429.html"),
    ("Värmdö kommun – Bygglov vid fasadändring",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/bygglovvidfasadandring.4.1a14d9c818e5a4c406a626d.html"),
    ("Värmdö kommun – Förändringar i PBL från 1 december 2025",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/forandringaripblfrom1december2025.4.18b9914519a768a188a2872.html"),
    _BV_FASAD, _BV_ISOL, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset på Värmdö renoveras?", "Boka ett gratis platsbesök så går vi igenom panel, sockel och vad detaljplanen säger om huset."),
  "img": [
    ("Trävilla från 1910-talet med brutet tegeltak i en sluttning mot vattnet på Ingarö",
     "1910s Swedish one-and-a-half storey wooden summer villa in Jugend and national romantic style with painted vertical and horizontal wooden panelling, white window frames, a steep broken mansard-like red tile roof, on a wooded slope above a narrow strait, gravel road along the shore, Ingarö Värmdö, summer daylight, no people"),
    ("Profilerade fönsterfoder och panel på en äldre sommarvilla där några brädor har lagats",
     "close-up of the facade of an old Swedish summer villa with ornate profiled white window casings and painted vertical wooden panel, a few boards near the bottom newly spliced and primed, stone foundation below, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ NORRTÄLJE
"fasadrenovering-norrtalje.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Norrtälje", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Norrtälje – bruksvillor och Grisslehamn",
  "description": "Fasadrenovering i Norrtälje: Rödvillorna i Hallstavik, ingenjörsvillor, sommarvillor i Grisslehamn och lovreglerna i kommunen. Gratis platsbesök.",
  "h1": "Fasadrenovering i Norrtälje",
  "lead": "Norrtälje kommun har 26 riksintresseområden för kulturmiljövården och har låtit utreda 22 av dem. Utredningarna innehåller råd till den som bor i områdena, och flera av dem gäller fasaden: laga hellre än byt, behåll originalmaterialet och anpassa ny panel till huset. Geal Entreprenad AB renoverar fasader i Norrtälje stad, Hallstavik, Grisslehamn och övriga Roslagen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Bruksvillor, sommarvillor och Roslagens trähus.",
  "sections": [
    {"id": "rodvillorna", "anchor": "Rödvillorna i Hallstavik",
     "h2": "Rödvillorna i Hallstavik",
     "paras": [
       "Hallsta pappersbruk planlades 1913 av Holmens bruk i Norrköping. Arkitekten John Åkerlund planerade den första etappen av brukets bostäder i trädgårdsstadens anda, med vägar och tomter anpassade efter terrängen. Rödvillorna byggdes 1914–1915 och stod klara när den första arbetsstyrkan från Norrköping kom i juli 1915.",
       "Kulturmiljöutredningen för Hallstavik från 2016 beskriver en enhetlig, lantlig arkitektur med tegelbelagda sadeltak, rödmålad locklistpanel och vitmålade fasaddetaljer. Husen byggdes i två varianter: 29 tvåfamiljshus med två lägenheter om två rum och kök, och fyra något större enfamiljshus som var tänkta för förmän.",
       "Utredningens råd är tydliga. Vid renovering av fasader och fasaddetaljer förordas i första hand lagning eller byte av skadade delar, och Rödvillorna målas med faluröd slamfärg. Ny fasadpanel ska anpassas till huset i utformning och material. Vi byter därför bara de brädor som är skadade och väljer en locklistpanel med samma mått som den gamla.",
     ],
     "aside": {"title": "Rödvillorna", "items": [
       "Byggda 1914–1915", "Rödmålad locklistpanel",
       "Tegelbelagda sadeltak", "Laga före byte"]}},
    {"id": "etapperna", "h2": "Tjänstemannavillor och brukets senare etapper",
     "paras": [
       "Samtidigt med Rödvillorna byggdes tjänstemannavillor med sjöutsikt norr om fabriken. Arkitekten Folke Bensow ritade 1916 en ingenjörsbostad för en familj, under 1920-talet följde egnahemsområden söder om bruket och längst i norr uppfördes tio tjänstemannavillor av en typ som Stig Dranger ritade 1951. Utredningen beskriver hur husens placering, storlek och utformning speglar brukets sociala skiktningar.",
       "Det första rådet i utredningen är att värna varje utbyggnadsetapps ursprungliga karaktär, både i formgivning och material. Färgerna ska väljas efter respektive etapp, och äldre fönstersnickerier av trä beskrivs som ofta mycket välgjorda. De målas med linoljefärg, och renovering föredras framför byte.",
       "För en fasadrenovering betyder det att en villa från 1910-talet och en från 1950-talet inte ska få samma panel bara för att de ligger i samma samhälle. Går fönstren inte längre att renovera finns mer under " + _L.format("fonsterbyte-norrtalje.html", "fönsterbyte i Norrtälje") + ".",
     ],
     "aside": None},
    {"id": "grisslehamn", "h2": "Grisslehamn: originalexteriören ska vara kvar",
     "paras": [
       "Grisslehamn var en knutpunkt för postvägen mellan Stockholm och Åbo via Åland, en postgång som löpte i närmare 300 år. Kulturmiljöutredningen för orten, också från 2016, beskriver ett posthus från 1756, gränsposteringens byggnader från 1800-talet och en kustmiljö med sommarvillor och pensionat från det tidiga 1900-talet.",
       "Råden är tydliga. Byggnadernas ursprungliga exteriör får inte förändras genom till exempel byte av fasadmaterial, fönster, takmaterial eller färgtyp och kulör. Underhåll bör ske varsamt med traditionella metoder och material, och variationen mellan husen bör bevaras eftersom materialen berättar om äldre hantverk och byggteknik.",
       "Boverket ger en teknisk förklaring till varför det är klokt. En fasad ska framför allt hindra regn från att tränga in, och skadorna uppstår ofta där material möts, vid fönster och infästningar. Därför lagar vi sådana detaljer med samma material som tidigare. Om kulören finns mer hos " + _L.format("malare-norrtalje.html", "målare i Norrtälje") + ".",
     ],
     "aside": {"title": "Råd för Grisslehamn", "items": [
       "Behåll fasadmaterialet", "Samma färgtyp som förut",
       "Traditionella metoder", "Gamla fönster bevaras"]}},
    {"id": "lov-norrtalje", "h2": "Lovreglerna i Norrtälje kommun",
     "paras": [
       "Norrtälje kommun listar när fasadändringar kräver bygglov. För en- och tvåbostadshus nämns bland annat utökad lovplikt i detaljplanen och fastigheter i områden som är särskilt värdefulla, och kommunen har en karta där du kan kontrollera det. Boverket förklarar att reglerna sedan den 1 december 2025 annars inte kräver lov för kulör eller fasadmaterial på sådana hus.",
       "Kommunen ger allmän rådgivning men kan inte bedöma enskilda åtgärder via e-post eller telefon. Vill du ha ett bindande besked behöver du söka frivilligt bygglov, och kommunen fattar beslut inom tio veckor från att ärendet är komplett. Läs mer om material och metoder på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Norrtälje till",
  "steps": [
    ("Utredningen först", "Ligger huset i ett riksintresseområde läser vi rådet i kommunens kulturmiljöutredning."),
    ("Platsbesök", "Panel, foder, bleck och sockel gås igenom, och vi mäter de befintliga profilerna."),
    ("Skriftligt kostnadsförslag", "Lagning och byte av delar redovisas för sig, med material och färgtyp angivna."),
    ("Lov eller inte", "Vi stämmer av kartan och detaljplanen och om frivilligt lov är värt att söka."),
    ("Utförande", "Skadade brädor byts mot likadana och anslutningar vid fönster och tak görs om."),
    ("Genomgång", "Vi går runt huset tillsammans och går igenom underhållet framåt."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Norrtälje",
  "rot": [
    "Att byta och reparera fasader, tilläggsisolera, måla fasader och reparera eller byta fönster räknas som rotarbete i ett småhus. Byggnadsställningar som monteras för arbetet ger också avdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Norrtälje?",
  "price": [
    "Hur många brädor och foder som måste bytas, om profilen måste tillverkas särskilt, vilken färgtyp som ska användas och avståndet till huset. En villa i Hallstavik och en sommarvilla i Grisslehamn kan kräva helt olika material. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur ska fasaden på en rödvilla i Hallstavik renoveras?",
     "Kulturmiljöutredningen förordar lagning eller byte av skadade delar, och att Rödvillorna målas med faluröd slamfärg. Ny panel ska anpassas till husets utformning och material."),
    ("Får jag byta fasadmaterial på en sommarvilla i Grisslehamn?",
     "Utredningen för Grisslehamn säger att byggnadernas ursprungliga exteriör inte får förändras genom byte av fasadmaterial, fönster, takmaterial eller färgtyp och kulör. Kontrollera även detaljplanen och kommunens karta."),
    ("Hur många riksintressen för kulturmiljövården finns i Norrtälje kommun?",
     "Kommunen anger 26 områden. År 2011 beslutade kommunen att utreda 22 av dem, och utredningarna med råd för boende finns digitalt."),
    ("Kan Norrtälje kommun säga per telefon om min fasadändring kräver lov?",
     "Kommunen ger allmän rådgivning men kan inte bedöma enskilda åtgärder via e-post eller telefon. För ett bindande besked söker du frivilligt bygglov."),
    ("Ska en 1950-talsvilla i Hallstavik ha samma panel som Rödvillorna?",
     "Nej, utredningen råder att varje utbyggnadsetapp ska behålla sin egen karaktär i formgivning, material och färg."),
  ],
  "sources": [
    ("Norrtälje kommun – Kulturmiljöutredning nr 20: Hallstavik (2016, pdf)",
     "https://www.norrtalje.se/globalassets/dokument/dokument-kultur--fritid/dokument-kultur/dokument-riksintressen-i-norrtalje-kommun/hallstavik.pdf"),
    ("Norrtälje kommun – Kulturmiljöutredning nr 5: Grisslehamn (2016, pdf)",
     "https://www.norrtalje.se/globalassets/dokument/dokument-kultur--fritid/dokument-kultur/dokument-riksintressen-i-norrtalje-kommun/grisslehamn.pdf"),
    ("Norrtälje kommun – Fasadändring", "https://www.norrtalje.se/sjalvservice/bygga-bo-miljo/fasadandring/"),
    ("Norrtälje kommun – Lovbefriade åtgärder",
     "https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/lovbefriade-atgarder/"),
    _BV_FASAD, _BV_FMAT, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset i Norrtälje renoveras?", "Boka ett gratis platsbesök så går vi igenom panel, foder och vad som kan lagas i stället för att bytas."),
  "img": [
    ("Rödmålad tvåfamiljsvilla med locklistpanel och tegeltak i ett lummigt bruksområde i Hallstavik",
     "early 1910s Swedish two-family worker's villa with red painted board and batten panelling, white window frames and corner boards, red clay tile gable roof, small garden with low hedge along a winding green street, pine trees, Hallstavik Norrtälje, summer daylight, no people"),
    ("Rödmålad locklistpanel där några nya brädor har satts in nära grunden",
     "close-up of red painted vertical board and batten wooden facade on an old Swedish house, a few new boards near the stone foundation primed and ready for falu red paint, white window casing at the edge, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"fasadrenovering-upplands-vasby.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Upplands Väsby", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Upplands Väsby – Grimstaby och Bo 85",
  "description": "Fasadrenovering i Upplands Väsby: trä och puts i Grimstaby, experimentella fasader från bomässan Bo 85, asbest, fukt och lovregler. Gratis platsbesök.",
  "h1": "Fasadrenovering i Upplands Väsby",
  "lead": "Upplands Väsbys kunskapsunderlag för kulturmiljö pekar ut flera småhusområden från 1970- och 80-talen som särskilt värdefulla, däribland Grimstaby och områdena från bomässan Bo 85. Där ska både material och färgskala behållas när fasaden renoveras. Geal Entreprenad AB renoverar fasader i Grimstaby, Runby, Bollstanäs och övriga Upplands Väsby, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Radhus från 70-talet och hus från bomässan.",
  "sections": [
    {"id": "grimstaby", "anchor": "Grimstaby och Bo 85",
     "h2": "Grimstaby: trä och puts i en gemensam färgskala",
     "paras": [
       "Grimstaby byggdes 1975–77 och ritades av Brunnberggruppen. Kommunens kunskapsunderlag för kulturmiljö från 2025 beskriver området som ett uttryck för 1970-talets nya ideal och en tydlig motreaktion mot miljonprogrammet, med bostadsgårdar längs ett i huvudsak bilfritt stråk, radhus främst i en våning och några högre flerbostadshus. Taken är branta sadeltak med betongpannor.",
       "Fasaderna varierar mellan trä och puts, och trädetaljerna har en kontrasterande kulör mot putsen. Panelens riktning och indelning används som dekorativt element, och starka kulörer kombineras med pastell. Hela området hålls ihop av en gemensam färgskala.",
       "Grimstaby räknas i underlaget som ett särskilt värdefullt bebyggelseområde enligt plan- och bygglagen. Vägledningen säger att färgskalorna ska underhållas och behållas, och att tillägg som ombyggnad av tak, nya takkupor eller nya dörrar och fönster inte ska tillåtas. Byts panel på ett av radhusen behöver den därför få samma riktning, samma indelning och samma bredd som tidigare, och om kulören finns mer under " + _L.format("malare-upplands-vasby.html", "målare i Upplands Väsby") + ".",
     ],
     "aside": {"title": "Fasaderna i Grimstaby", "items": [
       "Trä och puts växlar", "Panelriktning som dekor",
       "Gemensam färgskala", "Inga nya fönsteröppningar"]}},
    {"id": "bo85", "h2": "Bo 85: hus från Sveriges första renodlade bostadsmässa",
     "paras": [
       "Bo 85 i Upplands Väsby var enligt kunskapsunderlaget den första renodlade bostadsmässan i Sverige, med temat Bygg för gemenskap. Vid Lövstavägens slut i Runby Backar lät Byggforskningsrådet bygga ett tjugotal småhus och villor, en blandning av prefabricerade och arkitektritade hus. Underlaget räknar den särpräglade materialkombinationen till det som bör bevaras.",
       "I Carlslund beskrivs en lekfull arkitektur med lätta material som trä, plåt och glas tillsammans med ljus puts i pastellkulörer som turkos, gul, rosa och mintgrön. Den östra delen har en upprepad hustyp med faluröd träpanel. Vägledningen säger att områdets experimentella uttryck med glas, aluminium, kakel och puts ska vårdas.",
       "En fasad från en bostadsmässa kan vara svår att matcha om ett material inte längre finns att köpa. Vi dokumenterar därför profiler och skivformat innan något tas ner. Gäller arbetet även taket finns mer under " + _L.format("takrenovering-upplands-vasby.html", "takrenovering i Upplands Väsby") + ".",
     ],
     "aside": None},
    {"id": "asbest-fukt", "h2": "Asbest och fukt i 1970- och 80-talens väggar",
     "paras": [
       "Boverket skriver att användningen av asbest förbjöds inom byggsektorn 1982, och att det främst är byggnader från 1940 till 1970 som innehåller asbest, men att den kan finnas även i äldre hus. Bedömningen börjar med byggåret och tidigare renoveringar. Ett radhus i Grimstaby från 1975–77 bör därför provas innan skivor eller fogar tas bort, medan ett hus från bomässan 1985 är byggt efter förbudet.",
       "En annan risk i hus från den här tiden är fukt. Boverket beskriver hur vatten som tar sig förbi det enda tätande lagret på en enstegstätad fasad hamnar inne i väggen och bara kan torka ut långsamt. En luftspalt bakom panelen gör att vatten som kommer förbi kan rinna ut igen, och vid fönster saknas ofta vattenavledning mellan karm och omfattning.",
       "Vid besöket kontrollerar vi därför fogar, fönsteranslutningar och om panelen har en luftspalt bakom sig. Saknas luftspalten kan den byggas in när panelen ändå byts.",
     ],
     "aside": {"title": "Kontrollera vid besöket", "items": [
       "Byggår och tidigare renoveringar", "Luftspalt bakom panelen",
       "Fogar vid fönster", "Skivmaterial i fasaden"]}},
    {"id": "lov-vasby", "h2": "Lov och anmälan i Upplands Väsby",
     "paras": [
       "Upplands Väsby kommun skriver att en- och tvåbostadshus i normala fall inte behöver bygglov för fasadändringar, varken inom eller utanför detaljplan. Ligger huset i ett kulturhistoriskt särskilt värdefullt område krävs däremot bygglov, och detsamma gäller om detaljplanen har utökad lovplikt. Kunskapsunderlaget visar vilka områden kommunen räknar som särskilt värdefulla.",
       "En anmälan ska lämnas in om nya fönster eller dörrar innebär ingrepp i stommen. Kommunen påpekar också att solceller inom detaljplan kräver bygglov i hela kommunen, eftersom den ligger inom riksintresse för väderradar. Varsamhetskravet gäller även när inget lov behövs. Mer om material och metoder står på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Upplands Väsby till",
  "steps": [
    ("Område och byggår", "Vi tar reda på om huset ligger i ett av de utpekade områdena och när det byggdes."),
    ("Dokumentation", "Panelens riktning, bredd och kulörer fotograferas och mäts innan något rivs."),
    ("Prov vid behov", "Fogar och skivor i hus från före förbudet provas för asbest."),
    ("Skriftligt kostnadsförslag", "Byte, lagning och luftspalt redovisas var för sig, med material angivna."),
    ("Utförande", "Panelen sätts upp med luftspalt, och anslutningarna vid fönster görs om."),
    ("Genomgång", "Vi går runt huset och jämför med grannhusen i gruppen."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Upplands Väsby",
  "rot": [
    "För ett småhus med äganderätt ger både fasadbyte, fasadreparation, tilläggsisolering och fasadmålning rotavdrag. Är radhuset en bostadsrätt räknas fasaden som gemensam yta, och då ger arbetet inget rotavdrag.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ingår inte. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Upplands Väsby?",
  "price": [
    "Hur stor del av panelen eller putsen som behöver bytas, om ett särskilt material måste letas fram, om provtagning och sanering behövs och hur många fönsteranslutningar som ska göras om. Ett gratis platsbesök följs av ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi välja en ny kulör på vårt radhus i Grimstaby?",
     "Kunskapsunderlaget säger att områdets färgskalor ska underhållas och behållas. Eftersom Grimstaby räknas som särskilt värdefullt kan en fasadändring kräva bygglov, så stäm av med kommunen först."),
    ("Vad var Bo 85 i Upplands Väsby?",
     "Sveriges första renodlade bostadsmässa, med temat Bygg för gemenskap. Den lämnade bland annat småhusen vid Lövstavägen i Runby Backar och bebyggelsen i Carlslund."),
    ("Kan ett hus från 1985 innehålla asbest?",
     "Boverket skriver att asbest förbjöds inom byggsektorn 1982, så ett hus från bomässan är byggt efter förbudet. Har det renoverats med äldre material, eller är det byggt tidigare, kan prov ändå behövas."),
    ("Behöver jag anmäla till kommunen om vi gör en ny fönsteröppning i Upplands Väsby?",
     "Kommunen skriver att en anmälan ska lämnas in om nya fönster eller dörrar innebär ingrepp i stommen. I Grimstaby avråder kunskapsunderlaget dessutom från nya dörrar och fönster."),
    ("Varför kräver solceller på fasaden bygglov i Upplands Väsby?",
     "Enligt kommunen ligger hela kommunen inom riksintresse för väderradar, och därför kräver solceller inom detaljplan bygglov."),
  ],
  "sources": [
    _UV_KUN,
    ("Upplands Väsby kommun – Fasadändring",
     "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/fasadandring"),
    _BV_FASAD, _BV_ENST, _BV_ASB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset i Upplands Väsby renoveras?", "Boka ett gratis platsbesök så går vi igenom panel, puts och färgskala och vad som gäller i ditt område."),
  "img": [
    ("Radhus från 1970-talet med fasader i puts och träpanel i olika kulörer runt en gård i Grimstaby",
     "late 1970s Swedish low-rise terraced houses grouped around a green courtyard, facades alternating light render and wooden panel in contrasting colours with strong accent colours and pastels, steep gable roofs with concrete tiles and dormers, small gardens with low fences, forest at the edge, Grimstaby Upplands Väsby, autumn daylight, no people"),
    ("Träpanel med stående och liggande partier på ett radhus från 1970-talet",
     "close-up of a Swedish 1970s terraced house facade where vertical and horizontal wooden panel sections meet light render, painted in contrasting colours, a window with a sill flashing, a few new boards fitted in the same direction, daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HÄSSELBY
"fasadrenovering-hasselby.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Hässelby", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Hässelby – villastadens många årsringar",
  "description": "Fasadrenovering i Hässelby: villastaden från 1890-talet, grupphus från 60- och 70-talen, asbest, fukt och Stadsmuseets karta. Gratis platsbesök.",
  "h1": "Fasadrenovering i Hässelby",
  "lead": "Hässelby villastad började med arbetare som byggde egna hus på arrenderad mark och fick sedan handelsträdgårdar, sommarstugor och täta grupphus. Därför ser fasaderna mycket olika ut, och ett hus kan ha flera lager av gamla renoveringar. Geal Entreprenad AB renoverar fasader i Hässelby villastad, Hässelby gård, Hässelby strand och övriga Västerort, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Villastad, sommarstugor och grupphus.",
  "sections": [
    {"id": "historia", "anchor": "Villastadens årsringar",
     "h2": "Från arrendetomter till villastad",
     "paras": [
       "Stockholms stad köpte egendomarna Riddersvik och Lövsta 1885 och anlade några år senare en sopförbränningsstation där. Enligt en skrift som BOOM-gruppen vid KTH tog fram åt Stockholmshem 1996 räknas Villastadens födelse till 1893, när några av arbetarna fick arrendera var sin tomt för att själva bygga sina bostäder. Greve Carl Bonde lät sedan stycka av ytterligare 1 000 tunnland.",
       "År 1914 blev samhället municipalsamhälle med namnet Hässelby Villastad, en stadsplan fastställdes 1926 och samma år blev orten köping. På 1920-talet byggdes ett hundratal sommarstugor på Lambarholmen. Inkorporeringen med Stockholm trädde i kraft 1949, och under 1950-talet rådde i princip byggnadsförbud medan staden planerade områdets framtid.",
       "För fasaden betyder historien att två hus på samma gata kan ha helt olika stommar. Ett hus som började som sommarstuga eller som ett egenbygge kan ha byggts till i flera omgångar, och under en senare fasadskiva kan det finnas äldre panel. Vi tar därför bort en bit av beklädnaden på ett dolt ställe innan vi föreslår en lösning.",
     ],
     "aside": {"title": "Hässelby villastad", "items": [
       "Arrendetomter från 1893", "Municipalsamhälle 1914",
       "Stadsplan och köping 1926", "Del av Stockholm från 1949"]}},
    {"id": "grupphus", "h2": "Grupphus från 1960- och 70-talen – och asbest",
     "paras": [
       "Stadens strategi Varsam utveckling av småhus- och villaområden beskriver hur många villor i Hässelby villastad under 1960- och 1970-talen ersattes av täta grupper av enhetlig småhusbebyggelse. I skriften från 1996 står att nästan 80 procent av bostäderna då var byggda efter 1970. Stadens områdesfakta för 2025 räknar 5 009 bostäder i småhus av totalt 7 029 i stadsdelen, och de flesta av dem är äganderätter.",
       "Boverket bedömer att asbest sannolikt finns någonstans i byggnader uppförda 1940–1980. Fasader kläddes under 1940- och 50-talen ofta med cementfiberplattor med asbest, som förbjöds på 1970-talet, och fibrer kan frigöras om man borrar i dem. Att riva sådant material på en fasad kräver enligt Arbetsmiljöverket att företaget har tillstånd.",
       "Är det asbest i fasadskivorna planerar vi arbetet så att rivningen görs av ett företag med tillstånd och att den nya fasaden byggs upp efteråt. På ett grupphus syns ett byte i hela raden, så det är bra att prata med grannarna innan materialet väljs. Mer om kulörer finns hos " + _L.format("malare-hasselby.html", "målare i Hässelby") + ".",
     ],
     "aside": None},
    {"id": "fukt-hasselby", "h2": "Fukt vid fönster, fogar och sockel",
     "paras": [
       "Boverket beskriver fasadens viktigaste uppgift som att hindra regn från att tränga in i huset. De svaga punkterna är anslutningar mot fönster och dörrar, infästningar av stuprör och skarvar mellan byggdelar. Där behövs tvåstegstätning, så att vatten som kommer förbi det yttre skiktet kan ledas ut igen.",
       "På putsade hus beror putsbortfall enligt Boverket nästan undantagslöst på fukt, och puts som är fuktig över vintern kan frysa sönder. Kalkputs kan suga upp, transportera och avge fukt utan att skada stommen, men bara så länge fuktbelastningen inte blir för stor.",
       "Vid besöket tittar vi därför på fönsterblecken, på hur nära marken panelen eller putsen slutar och på stuprörens fästen. Ska takfoten och hängrännorna ses över samtidigt finns mer under " + _L.format("takrenovering-hasselby.html", "takrenovering i Hässelby") + ".",
     ],
     "aside": {"title": "Vanliga skadeställen", "items": [
       "Under fönsterbleck", "Nedersta brädorna mot sockeln",
       "Kring stuprörens fästen", "Sprickor i puts vid hörn"]}},
    {"id": "lov-hasselby", "h2": "Stadsmuseets karta och lovfrågan",
     "paras": [
       "Stockholms stad skriver att det inte längre krävs bygglov för fasadändringar på en- eller tvåbostadshus om vissa förutsättningar är uppfyllda. Lov behövs om byggnaden eller området är särskilt kulturhistoriskt värdefullt eller om detaljplanen har skyddsbestämmelser. Stadsmuseets klassificeringskarta ger en första indikation: hus markerade med gult eller grått behöver inte lov om inget annat gäller, medan streckade ytor ännu inte är inventerade.",
       "Är du osäker kan du kontakta Stadsmuseet, som brukar svara inom tre veckor efter att ha fått alla uppgifter. I stadens e-tjänst Bygg- och plantjänsten finns detaljplanen och äldre ritningar för fastigheten, som kan visa husets ursprungliga fasad. Mer om panel, puts och isolering står på sidan om " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadrenovering i Hässelby till",
  "steps": [
    ("Ritningar och karta", "Vi tittar i stadens arkiv och i Stadsmuseets karta för att se husets ursprung."),
    ("Provöppning", "En liten bit av beklädnaden tas bort på ett dolt ställe så att vi ser vad som finns under."),
    ("Prov vid behov", "Fasadskivor och fogar i hus från 1940–1980 provas innan de tas ner."),
    ("Skriftligt kostnadsförslag", "Rivning, nytt material, isolering och bleck redovisas som egna poster."),
    ("Utförande", "Den nya fasaden byggs med luftspalt och tvåstegstätning vid fönster och dörrar."),
    ("Genomgång", "Vi går igenom huset tillsammans och visar vad som har bytts."),
  ],
  "rot_h2": "ROT-avdrag för fasaden i Hässelby",
  "rot": [
    "Skatteverket räknar byte och reparation av fasader, tilläggsisolering och fasadmålning som rotarbete i ett småhus. Asbestsanering i samband med byggarbetet ger också avdrag, men inte en mätning av asbest som görs för sig.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. I en bostadsrätt ger fasaden inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Hässelby?",
  "price": [
    "Vad som döljer sig under den nuvarande beklädnaden, om asbest måste saneras, hur stor yta som ska bytas och om huset ska isoleras samtidigt. Ett grupphus med samma fasad som grannarna kan också påverka materialvalet. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Hur gamla är husen i Hässelby villastad?",
     "Bebyggelsen började växa fram när arbetare från 1893 fick arrendera tomter och bygga själva. Många hus ersattes av grupphus på 1960- och 70-talen, så åldern varierar mycket från gata till gata."),
    ("Vad betyder streckade ytor i Stadsmuseets karta?",
     "Att miljön ännu inte är inventerad. Ligger huset där, utanför ett särskilt värdefullt område, kan bygglov ändå behövas, och Stadsmuseet kan göra en bedömning."),
    ("Var hittar jag de ursprungliga ritningarna till mitt hus i Hässelby?",
     "I Stockholms stads e-tjänst Bygg- och plantjänsten kan du själv leta fram äldre handlingar för din fastighet, och där finns också detaljplanen."),
    ("Ger asbestsanering av fasaden rotavdrag?",
     "Ja, enligt Skatteverket ger sanering av asbest i samband med byggarbete rotavdrag. Enbart mätning eller provtagning av asbest ger inget avdrag."),
    ("Varför lossnar putsen på vår villa i Hässelby?",
     "Boverket skriver att putsbortfall nästan undantagslöst beror på fukt. Vi letar efter källan, till exempel ett bleck eller en sockel, innan putsen lagas."),
  ],
  "sources": [
    ("Stockholmskällan / Stockholmshem – Västra Smedshagen, Hässelby Villastad (BOOM-gruppen KTH, 1996, pdf)",
     "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0006397_01_ocr.pdf"),
    ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
     "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf"),
    ("Stockholms stad – Områdesfakta Hässelby villastad (2025, pdf)",
     "https://start.stockholm.se/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/vasterort/hasselby-vallingby/hasselby-villastad.pdf"),
    _STH_FASAD, _STH_KLASS, _BV_FMAT, _BV_ASB, _AV_ASB, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fasaden på huset i Hässelby renoveras?", "Boka ett gratis platsbesök så tar vi reda på vad som finns under beklädnaden och vad som bör göras."),
  "img": [
    ("Gata i Hässelby villastad med äldre trävillor bakom klippta häckar",
     "suburban street in Hässelby villastad Stockholm with an older Swedish wooden villa with painted panel and white window frames next to a row of 1970s single-storey grouped houses with brown wooden panel and low pitched roofs, mature fruit trees and hedges, autumn daylight, no people"),
    ("Fasad där en bit av en äldre fasadskiva har tagits bort så att träpanelen under syns",
     "close-up of a Swedish 1960s house wall clad with flat grey rectangular cement fibre facade boards; two whole boards near the bottom corner have been neatly unscrewed and removed, revealing older weathered horizontal painted wooden panel behind, straight clean edges, daylight, no people, no hands"),
  ],
  "related": [],
},

}
