# -*- coding: utf-8 -*-
"""Målare – ortsidor v9: Botkyrka, Österåker, Spånga, Hägersten, Farsta, Vällingby (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25: Botkyrka kommun
(Kulturmiljöprogram antaget 2014-05-22: Tuna, Segersjö, Näs by; Fasadändring i Bygglov A–Ö), Österåkers kommun
(Kulturmiljöprogram för Svinninge 2008; Kulturhistoriska byggnader, kulturmiljöer i bygglovsguiden), Stockholms
stad (bygglov.stockholm: Fasadändring, Stadsmuseets kulturhistoriska klassificering; Varsam utveckling av småhus-
och villaområden; Översiktsplan – Riksintressen: Vällingby AB 120; Områdesfakta 2025 för Mälarhöjden,
Midsommarkransen, Tallkrogen, Svedmyra, Sköndal, Vällingby, Råcksta, Flysta, Sundby), Stadsmuseet via
Stockholmskällan (Stockholms Spår: Tallkrogen, Svedmyra, Råcksta, Mälarhöjden, Midsommarkransen,
Hägerstensåsen; J. Ferenius och L. Johannesson: Ur Hem på landets arkiv), Boverket (Fasadändring i PBL
kunskapsbanken; Asbest), Riksantikvarieämbetet (Byggnadsmåleri med traditionella färgtyper), riksdagen.se
(bostadsrättslagen 7 kap. 12 §) och Skatteverket (rotavdrag).
Strukna (ej verifierade eller oklara i källan): Alby gårds gula fasadkulör (källtexten går inte att knyta säkert
till området), riktlinjetexten för Segersjö (trasig textkodning i pdf:en), läget för Näs by inom kommunen,
Vira bruks och Åkersbergas färgsättning (ingen källa hittad), hur Österåkers bygglovenhet bedömer kulörbyte
utanför Svinninge, att Mälarhöjdens villor har viss färgtyp, Langendal-radhusens nuvarande kulörer, om
radhusen i Atlantis och Omega har fasadskivor av asbestcement, att varje Solhemsvilla har klassning,
Tallkrogens äldre miljöprogram (inte läst). Inga priser, garantier, omdömen, egna uppdrag eller cert.
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py."""

_BOV = ("Boverket – Fasadändring (PBL kunskapsbanken)",
        "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_RAA = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf)",
        "https://www.raa.se/publicerat/9789172095830.pdf")
_SKV = ("Skatteverket – Så fungerar rotavdraget",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV2 = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_STH_FASAD = ("Stockholms stad – Fasadändring (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov.stockholm)",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_BOV_ASB = ("Boverket – Asbest", "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614)",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SSM = "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_{0}.pdf"

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ BOTKYRKA
"malare-botkyrka.html": {
  "kind": "district", "service": "malare", "ort": "Botkyrka", "svc_label": "Målare",
  "title": "Målare i Botkyrka – kulörer i Tuna, Segersjö och byarna",
  "description": "Målare i Botkyrka: dova kulörer i Tuna, puts och fjällpanel i Segersjö, faluröda byar och kommunens webbkarta för lovfrågan. Gratis platsbesök.",
  "h1": "Målare i Botkyrka",
  "lead": "Botkyrkas kulturmiljöprogram beskriver färgen område för område: kvarter där varje gård har sin egen kulör, radhus där tegel och trä samspelar och byar där husen är faluröda. Geal Entreprenad AB målar fasader, fönster och snickerier ute och inne i hela kommunen, från Tumba och Tullinge till Grödinge, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Tidstypiska kulörer från 1960-tal till gamla byar.",
  "sections": [
    {"id": "tuna", "anchor": "Kulörerna i Botkyrka",
     "h2": "Tuna: olika färger i varje kvarter",
     "paras": [
       "Kulturmiljöprogrammet, som kommunfullmäktige antog i maj 2014, lyfter fram Tuna i Tumba som ett exempel på det tidiga 1960-talets bebyggelse med hög kvalitet i gestaltning och genomförande. Området planerades under sent 1950-tal och har punkthus, kringbyggda lamellhuskvarter, villor och radhus.",
       "Om lamellhusen skriver programmet att de har kvar en tidstypisk färgsättning med dova kulörer och olika färger inom varje kvarter. Långsidorna är putsade och gavlarna av tegel, och riktlinjerna säger att lamellhusens tidstypiska karaktär ska bevaras. För punkthusen skriver programmet att repetitionen ska värnas vid ändring och underhåll av fasaderna och att balkongfronterna ska utformas enhetligt.",
       "Radhusen söder om Lindhovsvägen beskrivs som välbevarade och av hög arkitektonisk kvalitet, med en kombination av tegel och trä i fasaderna och ett enkelt, sakligt formspråk. Där handlar en målning nästan bara om träpartierna. Ursprungliga dörrar och fönster ska enligt programmet behållas, så vi skrapar, lagar och målar dem hellre än att föreslå byte.",
     ],
     "aside": {"title": "Tuna i programmet", "items": [
       "Dova kulörer i lamellhusen", "Olika färg i varje kvarter",
       "Radhus i tegel och trä", "Ursprungliga dörrar behålls"]}},
    {"id": "segersjo", "h2": "Segersjö: färgad puts och mörk fjällpanel",
     "paras": [
       "Segersjöområdet planerades under 1940-talet på mark som kommunen köpte av Tumba pappersbruk, i första hand för att ge bostäder åt personalen vid bruket och vid sanatorierna i Uttran och Tullinge. Programmet beskriver bebyggelsen som präglad av hög kvalitet i gestaltning, utförande och materialval.",
       "Två färgdetaljer nämns särskilt. Olika kulörer i puts och på balkongfronter har använts för att skapa variation i ett i övrigt enhetligt formspråk. I 1960-talsdelen är en tidstypisk detalj att taken avslutas med en mörklaserad sarg av liggande fjällpanel.",
       "En mörk lasyr på fjällpanel ska få fortsätta se ut som lasyr, så vi tvättar, slipar bort grått trä och bättrar med samma typ av produkt. Skulle sargen strykas med täckande färg ändras både kulör och karaktär. Är det hela takfoten som behöver ses över finns mer under " + _L.format("takrenovering-botkyrka.html", "takrenovering i Botkyrka") + ".",
     ],
     "aside": None},
    {"id": "byarna", "h2": "Faluröda byar och gårdar",
     "paras": [
       "Utanför tätorterna pekar programmet ut gamla byar med lång kontinuitet. I Näs by finns ett tjugotal äldre byggnader från främst 1700- och 1800-talen, med panelklädda boningshus och timrade ekonomibyggnader som alla är målade i en enhetlig faluröd kulör. Programmet räknar den enhetliga karaktären till det som ska respekteras.",
       "Riksantikvarieämbetets handbok om traditionella färgtyper beskriver slamfärgen som en av de äldsta och mest använda färgerna i landet. Den varnar för att en slamfärgad yta inte går att återföra till slamfärg när den väl har målats med till exempel latex-, alkyd- eller linoljefärg, även om den gamla färgen tas bort. Ny panel som sätts in i en gammal fasad ser enligt handboken ljusare ut i början, men kulören jämnar ut sig efter ett tag.",
       "För en lada eller ett boningshus i en sådan by betyder det rödfärg igen, med borstning och lagning av trä före strykningen. Ska fönster och knutar målas samtidigt tar vi med dem i samma kostnadsförslag, men som egna poster.",
     ],
     "aside": {"title": "I byarna", "items": [
       "Enhetlig faluröd kulör", "Panel och timrade uthus",
       "Rödfärg på rödfärg", "Lagning före strykning"]}},
    {"id": "lov-botkyrka", "h2": "Ny kulör? Börja i kommunens webbkarta",
     "paras": [
       "Botkyrka kommun förklarar att byte av kulör, till exempel att måla om ett hus från rött till vitt, räknas som fasadändring. På ett en- eller tvåbostadshus är det normalt lovfritt, men den utökade lovplikten gäller för alla typer av lovfria fasadändringar, både inom och utanför detaljplan, om byggnaden eller området är särskilt värdefullt.",
       "För att se om det gäller ditt hus hänvisar kommunen till sin webbkarta. Under fliken Bibliotek och kultur finns lagret Kulturmiljöprogram, och under Riksintressen lagret Kulturmiljövård. Kommunen skriver också att detaljplanen och översiktsplanen bör kontrolleras, liksom om området har ett gestaltningsprogram.",
       "Den som vill vara säker kan söka frivilligt bygglov. Då prövar byggnadsnämnden åtgärden och fattar ett bindande beslut, mot en avgift. Boverket påpekar att ommålning i samma kulör normalt räknas som underhåll, medan ett byte av färgtyp, till exempel från slamfärg till silikonhartsfärg, kan bedömas påverka husets karaktärsdrag. Läs mer om färg och fasad på " + _L.format("malare.html", "sidan om målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Botkyrka till",
  "steps": [
    ("Platsbesök", "Vi tittar på puts, tegel, panel och fönster och tar reda på vilken färg och vilken typ av färg som sitter på."),
    ("Kartan", "Vi går igenom kommunens webbkarta och detaljplanen för fastigheten innan kulören bestäms."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, förarbete och antal strykningar skrivs ut, med fönster och snickerier för sig."),
    ("Förarbete", "Tvätt, skrapning, slipning av grått trä, lagning och kittning av fönster."),
    ("Målning", "Grundning och strykningar görs när vädret tillåter, med de torktider färgen kräver."),
    ("Genomgång", "Vi går igenom huset tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Botkyrka",
  "rot": [
    "Skatteverket räknar målning av fasader samt av golv, tak, väggar, fönster och element som rotarbete i ett småhus. Staket och murar ger inget avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "I en bostadsrätt, till exempel i ett av lamellhusen, gäller avdraget bara arbete inne i lägenheten. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Botkyrka?",
  "price": [
    "Mest avgör hur mycket trä som ska målas och i vilket skick det är. Ett radhus i tegel och trä har få kvadratmeter men många detaljer, en rödfärgad lada har stora ytor som går fort, och en 1960-talsvilla med lasyrad panel kräver mest slipning. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får jag byta kulör på mitt radhus i Tuna?",
     "Tuna ingår i kulturmiljöprogrammet, och kommunen hänvisar till programmets kartlager när man ska bedöma om utökad lovplikt gäller. Kontrollera webbkartan och fråga kommunen innan du bestämmer en ny kulör."),
    ("Vilka lager i Botkyrkas webbkarta visar om huset är kulturhistoriskt värdefullt?",
     "Kommunen nämner lagret Kulturmiljöprogram under fliken Bibliotek och kultur och lagret Kulturmiljövård under fliken Riksintressen, och dessutom detaljplanerna under Bygga och bo."),
    ("Kan den mörka fjällpanelen på ett 1960-talshus i Segersjö målas med täckfärg?",
     "Tekniskt går det, men programmet räknar den mörklaserade sargen som en tidstypisk detalj, och täckfärg ändrar uttrycket. Vi rekommenderar att den underhålls med lasyr i samma ton."),
    ("Vad är frivilligt bygglov och när är det värt att söka?",
     "En prövning hos byggnadsnämnden som ger ett bindande beslut, fast åtgärden inte kräver lov. Det kan vara värt det vid ett kulörbyte i ett känsligt område, men prövningen kostar en bygglovsavgift."),
    ("Kan en gammal uthuslänga i en faluröd by målas med vanlig täckfärg?",
     "Riksantikvarieämbetet avråder, eftersom det inte går att återgå till slamfärg efteråt, och kulturmiljöprogrammet räknar byarnas enhetliga faluröda kulör till det som ska respekteras."),
  ],
  "sources": [
    ("Botkyrka kommun – Kulturmiljöprogram, antaget 2014 (pdf)",
     "https://www.botkyrka.se/download/18.1fbbaae6170bff9469deb7f/1602575505534/Kulturmilj%C3%B6program.pdf"),
    ("Botkyrka kommun – Fasadändring (Bygglov A–Ö)",
     "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/fasadandring"),
    _BOV, _RAA, _SKV, _SKV2,
  ],
  "cta": ("Ska huset i Botkyrka målas om?", "Boka ett gratis platsbesök så går vi igenom färgtyp, kulör och vad kommunens karta säger om fastigheten."),
  "img": [
    ("Radhus från 1960-talet med tegelgavlar och målade träpartier i Tumba",
     "row of early 1960s Swedish single-storey terraced houses with red brick end walls and dark painted vertical wooden panel sections between the windows, simple flat geometric design, small front gardens with low hedges, pine trees behind, Tumba Botkyrka, autumn daylight, no people"),
    ("Faluröd panelklädd byggnad med vita fönster och svart dörr i odlingslandskapet i Botkyrka",
     "old Swedish timber farm outbuilding painted in matte traditional falu red slurry paint with white window frames and a black wooden door, next to a red panelled farmhouse, open fields and a gravel road, Botkyrka countryside, overcast summer day, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"malare-osteraker.html": {
  "kind": "district", "service": "malare", "ort": "Österåker", "svc_label": "Målare",
  "title": "Målare i Österåker – sommarvillor, verandor och röda stugor",
  "description": "Målare i Österåker: linoljefärg på sekelskiftesvillor i Svinninge, glasverandor, röda stugor med vita knutar och lovfrågan i värdefulla områden.",
  "h1": "Målare i Österåker",
  "lead": "På Svinningehalvön står grosshandlarvillor från 1880- och 90-talen med panel som från början var målad med oljefärg, intill enkla röda stugor och villor från efterkrigstiden. Tre hustyper som behöver tre olika sorters färg. Geal Entreprenad AB målar fasader, verandor, fönster och interiörer i Åkersberga, Svinninge och övriga Österåker, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Sommarvillor, röda stugor och efterkrigsvillor.",
  "sections": [
    {"id": "sommarvillorna", "anchor": "Husen i Svinninge",
     "h2": "Fasspontpanel som målades med oljefärg",
     "paras": [
       "Kulturmiljöprogrammet för Svinninge, som Österåkers kommun tog fram 2008 inför detaljplanearbetet, beskriver sommarvillorna i Nantes och Svinningeudd som tvåvånings hus av resvirke med fasader av liggande fasspontpanel. Panelen har artikulerade våningsband och fönsteromfattningar, taksprånget skjuter ut, och programmet konstaterar att panelen ursprungligen var målad med oljefärg.",
       "Riksantikvarieämbetet skriver att linoljefärg ända in på mitten av 1900-talet dominerade på trähus där rödfärg inte användes, och att den i dag mest används vid ommålning av tidigare oljefärgsmålade ytor. En rätt sammansatt och rätt struken linoljefärg har enligt handboken en livslängd på ungefär 15–20 år, men fönstersnickerier, vindskivor och sydfasader behöver målas om oftare.",
       "Därför börjar vi med att ta reda på vad som sitter på panelen i dag. Har den fått plastfärg i en senare omgång blir valet ett annat än om oljefärgen finns kvar under smutsen. Boverket påpekar att ett byte från linoljefärg till plastfärg kan bedömas påverka husets karaktärsdrag.",
     ],
     "aside": {"title": "Sommarvillans delar", "items": [
       "Liggande fasspontpanel", "Våningsband och fönsteromfattningar",
       "Utskjutande taksprång", "Verandor mot vattnet"]}},
    {"id": "verandor", "h2": "Glasverandor och flyglar mot vattnet",
     "paras": [
       "Herrgårdsvillan med frontespis är den klart vanligaste villatypen i området, och programmet beskriver att många villor har en stor glasveranda mot sjön och att de uppglasade flyglarna är ett återkommande stildrag. Villa Johannesberg nämns som ett mycket välbevarat sommarnöje med torn, två flyglar med gästhus, ekonomibyggnad och badhus.",
       "En glasveranda är målning i miniatyr: många smala spröjs, bågar och kittfalsar på liten yta. Handboken råder att skrapa upp även kittfalsarna, ta bort allt löst kitt och grunda de blottade falsarna innan de kittas om, och att också insidan av ytterbågen ska strykas med utomhusfärg. Det är ett tålamodsarbete som vi redovisar som egen post.",
       "Linoljefärg ska strykas tunt, och handboken anger maj till augusti som bästa period, med trä som inte har högre fukthalt än ungefär 15 procent. Direkt solsken bör undvikas eftersom färgen kan få blåsor, så vi följer solen och målar de sidor som redan har haft sol. Mer om fönstren finns under " + _L.format("fonsterbyte-osteraker.html", "fönsterbyte i Österåker") + ".",
     ],
     "aside": None},
    {"id": "stugorna", "h2": "Röda stugor och 1950-talets putsade villor",
     "paras": [
       "Bredvid villorna byggdes enklare egnahem för familjer som bodde i området året runt och försörjde sig på sommargästerna. Programmet beskriver dem som enkla röda stugor med vita knutar från åren kring sekelskiftet. Efter sekelskiftet blev den röda stugan med vita knutar populär som byggnadstyp, och på 1930- och 40-talen tillkom sportstugor, en av dem med stående locklistpanel.",
       "Rödfärgen behandlas helt annorlunda än oljefärgen på villorna. Ytan borstas ren från lös färg och lavar, rötskadat ändträ lagas och sedan stryks rödfärg på rödfärg. Kommer industritillverkad rödfärg till användning påpekar handboken att man ska se till att få samma kulör som tidigare, särskilt vid bättring. De vita knutarna och fönstren målas för sig med täckande färg.",
       "På 1950- och 60-talen uppfördes enstaka villor för permanentboende som enligt programmet har hög arkitektonisk kvalitet, utformade som låga murade envåningshus med putsade eller murade fasader. Där är det fönster, dörrar och takfot som målas, och putsen bara om den har varit målad tidigare. Vill du läsa om taken i samma miljö finns " + _L.format("takrenovering-osteraker.html", "takrenovering i Österåker") + ".",
     ],
     "aside": {"title": "Tre färgsystem", "items": [
       "Villor: linoljefärg", "Stugor: röd slamfärg",
       "Knutar och fönster: täckfärg", "Efterkrigsvillor: puts och snickerier"]}},
    {"id": "lov-osteraker", "h2": "Varsamhet och lov i värdefulla miljöer",
     "paras": [
       "Programmet påpekar att varsamhetskravet i plan- och bygglagen gäller för all bebyggelse i området, så att byggnadens särdrag beaktas vid ändringar. Delar av Nantes och Svinningeudd beskrivs som kommunens äldsta, bäst bevarade och samlade sommarbebyggelse.",
       "På kommunens sida om kulturhistoriska byggnader står att du behöver söka bygglov om fastigheten ligger i ett kulturhistoriskt, särskilt värdefullt område eller om byggnaden är särskilt värdefull, till exempel om du vill ändra fasaden eller underhålla. Kommunen ber dig kontakta bygglovenheten innan arbetet börjar, och Österåkerskartan visar områden med kulturhistoriska värden.",
       "Utanför sådana områden är ett kulörbyte på en villa normalt lovfritt sedan den 1 december 2025, enligt Boverket, och ommålning i samma kulör räknas som underhåll. Vi går igenom kartan med dig vid besöket. Läs mer om målning ute och inne på " + _L.format("malare.html", "sidan om målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Österåker till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, verandor, fönster och uthus och tar reda på om det är oljefärg, rödfärg eller plastfärg som sitter på."),
    ("Kartan", "Fastigheten kontrolleras i Österåkerskartan, och i värdefulla områden kontaktas bygglovenheten."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, förarbete och antal strykningar står med, och verandan redovisas för sig."),
    ("Förarbete", "Tvätt, skrapning, ilagning av friskt trä och kittning av bågar och glasfalsar."),
    ("Målning", "Tunna strykningar i torrt väder under säsongen, med de torktider färgen behöver."),
    ("Genomgång", "Vi går igenom huset tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Österåker",
  "rot": [
    "För villor, radhus och fritidshus som du äger räknar Skatteverket fasadmålning och målning av fönster, väggar och tak som rotarbete. Målning av staket och murar ger inget avdrag. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Färg, kitt och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här påverkar priset i Österåker",
  "price": [
    "En sekelskiftesvilla med glasveranda, flyglar och mycket listverk tar betydligt längre tid än en röd stuga av samma storlek, och kuperade sjötomter kan påverka hur ställningen kan stå. Mängden lös färg och skadat trä avgör hur stort förarbetet blir. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi måla vår sommarvilla i Svinninge med linoljefärg igen fast den har plastfärg i dag?",
     "Det beror på hur mycket av plastfärgen som sitter fast och vad som finns under. Vi gör skrapprov och berättar vad som är möjligt innan något beställs."),
    ("Hur länge håller linoljefärg på en fasad i skärgården?",
     "Riksantikvarieämbetet anger ungefär 15–20 år för en rätt sammansatt och rätt utförd målning, men utsatta delar som fönster, vindskivor och sydfasader behöver målas om tidigare."),
    ("Vilken tid på året målar ni utvändigt med oljefärg?",
     "Helst maj till augusti, när det är varmt och torrt och träet inte är fuktigare än ungefär 15 procent. Vi undviker direkt solsken på den sida som målas."),
    ("Behöver jag bygglov för att underhålla fasaden på en värdefull villa i Österåker?",
     "Kommunen skriver att bygglov kan behövas för både fasadändring och underhåll om byggnaden eller området är särskilt värdefullt. Kontakta bygglovenheten innan arbetet börjar."),
    ("Ska de vita knutarna på en röd stuga målas med samma färg som väggarna?",
     "Nej, väggarna stryks med röd slamfärg och knutar, foder och fönster med en täckande färg. De två målas i separata moment."),
  ],
  "sources": [
    ("Österåkers kommun – Kulturmiljöprogram för Svinninge (pdf)",
     "https://www.osteraker.se/download/18.367d658917909e8fc2bc760/1632320809578/kulturmiljoprogram_Svinninge.pdf"),
    ("Österåkers kommun – Kulturhistoriska byggnader, kulturmiljöer",
     "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/bygglovsguiden/kulturhistoriskabyggnaderkulturmiljoer.4.367d658917909e8fc2bb42.html"),
    _BOV, _RAA, _SKV, _SKV2,
  ],
  "cta": ("Ska villan eller stugan i Österåker målas om?", "Boka ett gratis platsbesök så går vi igenom färgtyp, veranda och fönster på plats."),
  "img": [
    ("Gul sekelskiftesvilla med glasveranda på en sluttning vid vattnet i Österåker",
     "large Swedish wooden summer villa from the 1890s with pale yellow horizontal bevelled panel, white window surrounds and marked floor bands, a big two-storey glazed veranda facing the water, stone foundation, fruit trees on a terraced garden sloping to a calm Baltic inlet, Svinninge Österåker, summer daylight, no people"),
    ("Spröjsade verandafönster med skrapad färg inför ommålning",
     "close-up of an old wooden glazed veranda on a Swedish summer villa, small-paned windows with white painted muntins, some window frames scraped bare with old putty removed in the glazing rebates, a scraper and a round brush resting on the window sill, soft daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SPÅNGA
"malare-spanga.html": {
  "kind": "district", "service": "malare", "ort": "Spånga", "svc_label": "Målare",
  "title": "Målare i Spånga – Solhems färgsättning och villastäderna",
  "description": "Målare i Spånga: Solhems ursprungliga kulörer enligt Stadsmuseets ritningar, villorna i Bromsten, Flysta och Sundby och Stadsmuseets karta för lovfrågan.",
  "h1": "Målare i Spånga",
  "lead": "För Solhem i Spånga finns akvarellerade ritningar som visar vilka färger de första villorna var tänkta att ha, och de finns i dag hos Stadsmuseet. Geal Entreprenad AB målar fasader, fönster och interiörer i Solhem, Bromsten, Flysta, Sundby och övriga Spånga, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Solhems färgskala och villorna kring stationen.",
  "sections": [
    {"id": "solhems-farger", "anchor": "Solhems färger",
     "h2": "Rödfärg, vita foder och gröna verandor",
     "paras": [
       "I en artikel på Stockholmskällan beskriver Jonas Ferenius och Lars Johannesson hur AB Hem på landet lämnade ritningar och fotografier från Duvbo och Solhem till Stadsmuseet. Bland dem finns en svit med 15 akvarellerade byggnadsritningar på kartong, alla till tomter som såldes senast i juli 1905.",
       "Ritningarna visar enligt artikeln en helsvensk, nationalromantiskt präglad stil, och färgsättningen genomgående ett genomtänkt samspel mellan kulörer. Vanligast är rödfärgade fasader med vindskivor, knutar och fönsterfoder i vitt och entré och veranda i grönt. Några hus har ljus beige panel med bruna snickerier, och ett har grön fasad med snickerier i samma färg och fönsterbågar i brunt.",
       "Våren 1904 ordnade bolaget en tävling om ritningar till egnahem, och de inlämnade skisserna ställdes ut i Lantbruksakademiens sal, där de väckte stort intresse. Bolagets ingenjör Gunnar Way-Matthiesen, en av pristagarna, skulle se till att husen följde bolagets bestämmelser om stugstil, tegeltak och tilltalande färg. Solhem skulle se bättre ut än de villasamhällen som beskrevs som fulla av hus i mot varandra skrikande färger.",
     ],
     "aside": {"title": "Ritningarnas färgskala", "items": [
       "Röd fasad, vita knutar och foder", "Gröna entréer och verandor",
       "Ljus beige panel, bruna snickerier", "Grön fasad, bruna fönsterbågar"]}},
    {"id": "forandrade-villor", "h2": "När villan har bytt panel och färg",
     "paras": [
       "Artikeln konstaterar att alla sju byggnader från ritningarna som finns kvar har förändrats. Panelen har bytts mot eternit, lackpanel eller kalksandsten och de tätspröjsade fönstren har bytts ut. Efterfrågan på tomter ledde till att många tomter styckades, och många av de äldre villorna förändrades kraftigt på 1960- och 70-talen.",
       "För den som vill ge en Solhemsvilla tillbaka något av den ursprungliga karaktären är färgsättningen det enklaste steget. Stockholms stads vägledning för småhusområden råder att ta tillvara eller återskapa karaktärsskapande material, kulörer och detaljer så långt det går. Vi gör skrapprov under listverk och foder, där äldre lager kan finnas kvar, innan kulören bestäms.",
       "Är panelen utbytt mot fasadskivor från 1960- eller 70-talet behöver vi veta vad de består av innan något tvättas eller slipas. Boverket listar fasadskivor bland byggprodukter som kan innehålla asbest och skriver att högtryckstvätt, stålborstning och slipning kan frigöra fibrer. Byte av panel hör hemma under " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
    {"id": "villastaderna", "h2": "Bromsten, Flysta och Sundby",
     "paras": [
       "Vägledningen räknar Solhem, Bromsten, Flysta och Sundby till typen villastad, men av de fyra är bara Solhem markerat som kulturhistoriskt värdefull miljö. I de övriga tre handlar målningen därför mer om husets eget skick och ägarens val än om en gemensam färgskala.",
       "Stadens områdesfakta för 2025 visar hur tydligt det här är villaområden med enskilda ägare. I Flysta är 657 av 663 småhus äganderätter och i Sundby 525 av 559. Det är alltså i regel ägaren själv som beställer fasadmålningen, inte en förening.",
       "Inomhus målar vi väggar, tak, snickerier och dörrar och tapetserar. Ska köket göras om samtidigt finns mer under " + _L.format("koksrenovering-spanga.html", "köksrenovering i Spånga") + ", och för taket under " + _L.format("takrenovering-spanga.html", "takrenovering i Spånga") + ".",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Flysta: 657 av 663 äganderätter", "Sundby: 525 av 559 äganderätter",
       "Solhem: värdefull miljö", "Bromsten, Flysta, Sundby: villastad"]}},
    {"id": "lov-spanga", "h2": "Stadsmuseets karta och lovplikten",
     "paras": [
       "Stockholms stad skriver att fasadändringar på en- och tvåbostadshus inte längre kräver bygglov om vissa förutsättningar är uppfyllda. Utökad lovplikt gäller om huset är markerat med blått eller grönt i Stadsmuseets klassificeringskarta eller ligger i ett område med grön eller blå ring. Streckade ytor är miljöer som ännu inte har inventerats, och även där kan lov behövas.",
       "Är du osäker kan du mejla Stadsmuseet med adress, fastighetsbeteckning, stadsdel, byggnadsår, senare ombyggnader och foton av fasaderna. Museet brukar svara inom tre veckor från att det har fått alla uppgifter. Boverket påpekar att ommålning i samma kulör normalt är underhåll, medan ett byte av färgtyp kan räknas som en påverkan på husets karaktärsdrag.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Spånga till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, foder, verandor och fönster och gör skrapprov där äldre färglager kan finnas kvar."),
    ("Kartan", "Stadsmuseets klassificering och detaljplanen kontrolleras innan kulören bestäms."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulörer för fasad och snickerier, förarbete och antal strykningar skrivs ut."),
    ("Förarbete", "Tvätt, skrapning, lagning av trä och kittning av fönster. Häckar och rabatter skyddas."),
    ("Målning", "Grundning och strykningar i lämpligt väder, snickerierna i egen kulör."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Spånga",
  "rot": [
    "För en villa med äganderätt räknar Skatteverket fasadmålning och målning av golv, tak, väggar, fönster och element som rotarbete, men inte staket och murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Spånga?",
  "price": [
    "Flera kulörer på samma hus, som röd fasad med vita foder och gröna dörrar, tar längre tid än en kulör rakt igenom, eftersom varje del målas för sig. Antalet verandor, fönster och listverk spelar in, liksom hur mycket lös färg som ska bort. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka färger hade Solhems villor från början?",
     "Enligt Stadsmuseets ritningar från 1904–05 var de flesta rödfärgade med vita vindskivor, knutar och fönsterfoder och med entré och veranda i grönt. Några hade ljus beige panel med bruna snickerier."),
    ("Behöver jag bygglov för att måla om min villa i Solhem i en annan kulör?",
     "Solhem är utpekat som kulturhistoriskt värdefull miljö. Titta i Stadsmuseets klassificeringskarta: är huset blått eller grönt, eller ligger det inom grön eller blå ring, krävs bygglov för ett kulörbyte."),
    ("Hur får jag besked från Stadsmuseet om mitt hus i Spånga?",
     "Mejla adress, fastighetsbeteckning, byggnadsår, uppgifter om ombyggnader och foton av fasaderna. Museet brukar svara inom tre veckor."),
    ("Kan ni måla fasadskivor från 1960-talet på en villa i Spånga?",
     "Först behöver vi veta om skivorna innehåller asbest. Boverket skriver att tvätt med högtryck, stålborstning och slipning kan frigöra fibrer, så ett prov tas innan något bearbetas."),
    ("Kan ni måla fönsterbågarna i en annan kulör än fodren?",
     "Ja. Det var vanligt i Solhem från början, och vi målar bågar, foder och dörrar som separata moment så att kulörerna hålls rena."),
  ],
  "sources": [
    ("Stockholmskällan – J. Ferenius och L. Johannesson: Ur Hem på landets arkiv (pdf)",
     "https://stockholmskallan.stockholm.se/postfiles/SMF/SD/SSMB_0005802_01.pdf"),
    _VARSAM,
    ("Stockholms stad – Områdesfakta Flysta (2025)", _OF + "vasterort/jarva/flysta.pdf"),
    ("Stockholms stad – Områdesfakta Sundby (2025)", _OF + "vasterort/jarva/sundby.pdf"),
    _STH_FASAD, _STH_KLASS, _BOV, _BOV_ASB, _SKV, _SKV2,
  ],
  "cta": ("Ska villan i Spånga få tillbaka sina färger?", "Boka ett gratis platsbesök så gör vi skrapprov och går igenom kulörerna på plats."),
  "img": [
    ("Rödfärgad villa i nationalromantisk stil med vita knutar och grön veranda i Spånga",
     "early 1900s Swedish national romantic wooden villa painted in matte falu red with white corner boards, white window surrounds and white barge boards, a small entrance veranda painted dark green, red clay tile roof, garden with apple trees and a clipped hedge, Solhem Spånga Stockholm, summer daylight, no people"),
    ("Fönsterfoder med skrapprov som visar äldre färglager",
     "close-up of an old Swedish wooden window surround on a red painted villa, a small scraped test patch on the white window trim revealing older layers of green and cream paint underneath, a paint scraper resting on the window sill, natural daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HÄGERSTEN
"malare-hagersten.html": {
  "kind": "district", "service": "malare", "ort": "Hägersten", "svc_label": "Målare",
  "title": "Målare i Hägersten – villor i Mälarhöjden och bostadsrätter",
  "description": "Målare i Hägersten: villorna i Mälarhöjden, lägenheter i Midsommarkransen och på Hägerstensåsen, ansvaret i bostadsrätt och rotavdraget inomhus.",
  "h1": "Målare i Hägersten",
  "lead": "Hägersten rymmer både jugendkvarter med små bostadsrätter och villor vid Mälaren. I Midsommarkransen finns över 4 000 bostadsrätter, medan nästan alla småhus i Mälarhöjden är äganderätter. Geal Entreprenad AB målar lägenheter, villor och radhus i Mälarhöjden, Midsommarkransen, Hägerstensåsen, Västertorp och Fruängen, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Lägenheter, villor vid Mälaren och radhus.",
  "sections": [
    {"id": "bostadsratt", "anchor": "Bostadsrätten",
     "h2": "Midsommarkransen: lägenheter i 1910-talets stenhus",
     "paras": [
       "Stadsmuseets skrift om Midsommarkransen berättar att Nyborgs AB köpte tegelbruket och marken runtomkring 1907 och att utbyggnaden kunde börja 1910. Gedigna stenhus i enkel jugendstil uppfördes, två våningar höga i stadslika kvarter, med fullt utbyggda vindar och förhöjda källare för butiker. Lägenheterna var i regel små och enkelt utrustade. Förstaden hette först Tellusborg och fick namnet Midsommarkransen 1926.",
       "Enligt stadens områdesfakta för 2025 fanns 4 371 bostadsrätter i stadsdelen. Hägerstensåsen, där de första smalhusen stod klara 1939 och de sista 1948, hade 2 034. Stadsmuseet skriver att andelen privata fastighetsägare på åsen var mycket hög och att andelen smålägenheter var mycket stor. Fruängen byggdes i huvudsak under senare delen av 1950-talet som en av de tunnelbanestäder som staden lät uppföra för att lösa efterkrigstidens bostadsbrist. I de flesta av de här husen är det lägenheten som målas, inte fasaden.",
       "Bostadsrättslagen säger i 7 kap. 12 § att bostadsrättshavaren på egen bekostnad ska hålla lägenheten i gott skick, om inte annat bestämts i stadgarna. Väggar, tak och snickerier inne i lägenheten är därför normalt ditt ansvar, men läs föreningens stadgar, eftersom de kan fördela ansvaret annorlunda.",
     ],
     "aside": {"title": "Bostadsrätter 2025", "items": [
       "Midsommarkransen: 4 371", "Hägerstensåsen: 2 034",
       "Ansvar enligt stadgarna", "Fasaden ger inget rotavdrag"]}},
    {"id": "aldre-tak", "h2": "Gamla tak och väggar inomhus",
     "paras": [
       "I en lägenhet från 1910- eller 1940-talet kan taken ha limfärg och väggarna flera lager tapet och färg. Riksantikvarieämbetet skriver att limfärg som takfärg var vanlig ända fram till 1950-talet, och att den i dag främst används vid ommålning av ytor som tidigare har målats med limfärg. Vilken färg som passar beror alltså på vad som redan sitter i taket.",
       "Därför provar vi underlaget innan något beställs: kritar taket, har väggen tapet under färgen och var behövs spackling? Handboken påpekar att man vid ommålning av äldre ytor som inte varit spacklade tidigare inte bör införa spackling, så hur slät ytan ska bli bestämmer vi tillsammans med dig.",
       "Ska fönster eller ytterdörr målas i en bostadsrätt ger bara insidan rotavdrag. Vem som ansvarar för utsidan står i föreningens stadgar.",
     ],
     "aside": {"title": "Före målning inomhus", "items": [
       "Kritar takets färg?", "Tapet under färgen?",
       "Spackling eller inte", "Insidan av fönster och dörr"]}},
    {"id": "malarhojden", "h2": "Mälarhöjden: villor från tre epoker",
     "paras": [
       "Mälarhöjden har en helt annan bebyggelse. Stadsmuseets skrift beskriver promenaden längs Mälarstranden mellan Klubbensborg och Lyran med stora utsirade trävillor från 1800-talets andra hälft, strama vita funkishus från 1930-talet vid Pettersbergsvägen och senare kataloghus. Från 1913, när Fridhems villastad fick spårvagn till staden, blev det vanligare att bo här året runt, och området planlades 1923.",
       "Enligt områdesfakta för 2025 fanns 1 086 bostäder i småhus i Mälarhöjden, varav 988 äganderätter. Stadens vägledning för småhusområden räknar Mälarhöjden som villastad och som kulturhistoriskt värdefull miljö. För en ny kulör på villan är det därför klokt att börja med Stadsmuseets klassificeringskarta.",
       "En utsirad trävilla från 1800-talet har mycket snickerier som skrapas och målas för hand, medan ett vitt funkishus kräver att putsen och den gamla färgen fungerar ihop. Mer om husen och taken i stadsdelen finns under " + _L.format("taklaggare-hagersten.html", "takläggare i Hägersten") + ".",
     ],
     "aside": None},
    {"id": "lov-hagersten", "h2": "Lovplikt för villor och flerbostadshus",
     "paras": [
       "Stockholms stad skriver att det inte längre krävs bygglov för fasadändringar på en- och tvåbostadshus om vissa förutsättningar är uppfyllda, men att utökad lovplikt gäller i särskilt kulturhistoriskt värdefulla byggnader och områden. För flerbostadshus gäller en annan regel: en ändring på fasad eller tak som vetter mot allmän plats kräver bygglov.",
       "Vill en bostadsrättsförening i Midsommarkransen byta kulör på gatufasaden behöver den alltså söka lov. Boverket anger att ommålning i samma kulör normalt räknas som underhåll. Läs mer om målning ute och inne på " + _L.format("malare.html", "sidan om målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Hägersten till",
  "steps": [
    ("Platsbesök", "Vi tittar på tak, väggar, snickerier och fönster och provar hur den gamla färgen sitter."),
    ("Ansvar och regler", "I bostadsrätt går vi igenom vad stadgarna säger, för villor Stadsmuseets karta."),
    ("Skriftligt kostnadsförslag", "Rum, ytor, färgtyp, spackling och antal strykningar skrivs ut."),
    ("Skydd", "Golv, trapphus, möbler och rum som inte berörs täcks innan något damm uppstår."),
    ("Målning", "Spackling, slipning och strykningar i rätt ordning, med torktid mellan varje steg."),
    ("Genomgång", "Vi går igenom rummen tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Hägersten",
  "rot": [
    "I en bostadsrätt räknar Skatteverket målning av golv, tak, väggar och element som rotarbete, liksom målning av innerdörrar och insidan av ytterdörrar och fönster. Att måla fasader eller balkonger ger inget avdrag. I en villa ingår även fasadmålning.",
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Hägersten?",
  "price": [
    "I en lägenhet styr antalet rum, takhöjden och hur mycket spackling väggarna behöver, och om taken har limfärg som måste tas bort. För en villa avgör mängden snickerier och hur fasaden är klädd. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem ansvarar för att måla väggarna i min bostadsrätt i Midsommarkransen?",
     "Enligt bostadsrättslagen ska du hålla lägenheten i gott skick på egen bekostnad, om inte stadgarna säger något annat. Läs föreningens stadgar för att se var gränsen går."),
    ("Får jag rotavdrag för att måla insidan av fönstren i en bostadsrätt?",
     "Ja. Skatteverket godkänner målning av insidan av ytterdörrar och fönster i en bostadsrätt, men inte utsidan eller fasaden."),
    ("Kan taket i en lägenhet från 1910-talet ha limfärg?",
     "Det är möjligt. Limfärg var vanlig som takfärg fram till 1950-talet enligt Riksantikvarieämbetet. Vi provar taket innan färg väljs."),
    ("Behöver vår förening bygglov för att byta kulör på gatufasaden?",
     "Ja, för ett flerbostadshus krävs bygglov för en fasadändring som vetter mot allmän plats, enligt Stockholms stad. Ommålning i samma kulör räknas normalt som underhåll."),
    ("Gäller lovfriheten för kulörbyte även på en villa i Mälarhöjden?",
     "Mälarhöjden är markerat som kulturhistoriskt värdefull miljö i stadens vägledning. Kontrollera Stadsmuseets karta, eftersom utökad lovplikt gäller för hus som är klassade blått eller grönt."),
  ],
  "sources": [
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Midsommarkransen (pdf)", _SSM.format("000070")),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Hägerstensåsen (pdf)", _SSM.format("000088")),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Mälarhöjden (pdf)", _SSM.format("000069")),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Fruängen (pdf)", _SSM.format("000056")),
    ("Stockholms stad – Områdesfakta Midsommarkransen (2025)", _OF + "soderort/hagersten/midsommarkransen.pdf"),
    ("Stockholms stad – Områdesfakta Hägerstensåsen (2025)", _OF + "soderort/hagersten/hagerstensasen.pdf"),
    ("Stockholms stad – Områdesfakta Mälarhöjden (2025)", _OF + "soderort/hagersten/malarhojden.pdf"),
    _BRL, _VARSAM, _STH_FASAD, _BOV, _RAA, _SKV, _SKV2,
  ],
  "cta": ("Ska lägenheten eller villan i Hägersten målas?", "Boka ett gratis platsbesök så provar vi underlaget och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust vardagsrum med nymålade väggar och stuckatur i en äldre lägenhet i Hägersten",
     "empty bright living room in an old Swedish apartment from the 1910s with freshly painted pale warm white walls, a simple plaster ceiling cornice, white panelled door and deep window niche with white painted window, wooden herringbone parquet floor partly covered with protective paper, Midsommarkransen Stockholm, soft daylight, no people"),
    ("Skyddat golv, målarpenslar och spackel inför målning av en lägenhet",
     "interior of an empty Swedish apartment room prepared for painting, floor covered with plain grey protective paper and masking tape along the white skirting boards, an aluminium stepladder, a paint tray with a roller, a wall with freshly filled and sanded white patches of filler, window with daylight, no buckets, no cans, no labels, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ FARSTA
"malare-farsta.html": {
  "kind": "district", "service": "malare", "ort": "Farsta", "svc_label": "Målare",
  "title": "Målare i Farsta – småstugor i Tallkrogen och Svedmyra",
  "description": "Målare i Farsta: locklistpanel på småstugorna i Tallkrogen och Svedmyra, de ljusa kulörerna, grå ädelputs från 1950-talet och Sköndals småhus.",
  "h1": "Målare i Farsta",
  "lead": "Farsta är mer än centrumet från 1960. I stadsdelsområdet ligger Söderorts största småstugeområde, där närmare tusen trähus byggdes med ägarnas eget arbete som insats. Geal Entreprenad AB målar fasader, fönster och interiörer i Tallkrogen, Svedmyra, Sköndal, Gubbängen och övriga Farsta, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Småstugor, ädelputs och radhus i Söderort.",
  "sections": [
    {"id": "tallkrogen", "anchor": "Småstugorna",
     "h2": "Tallkrogen: tusen stugor av mer än tio typer",
     "paras": [
       "Stadsmuseets skrift om Tallkrogen berättar att utbyggnaden började 1933 och att området blev det största småstugeområdet i Söderort. Närmare 1 000 småstugor växte upp på den flacka åkermarken under det följande decenniet. Vid en första anblick ser det ut som samma stuga upprepad, men det finns mer än tio olika hustyper.",
       "Småstugan lanserades i slutet av 1920-talet för mindre bemedlade. Kontantinsatsen ersattes med eget arbete, staden gav förmånliga lån och byggnadsdelarna levererades färdiga från fabriken. Gatorna är utlagda som löparbanor runt en idrottsarena och heter till exempel Kulstötarvägen, Maratonvägen och Olympiavägen.",
       "Enligt stadens områdesfakta för 2025 fanns 945 bostäder i småhus i Tallkrogen, och 941 av dem var äganderätter. Varje stuga har alltså sin egen ägare, men området är byggt för att se enhetligt ut.",
     ],
     "aside": {"title": "Tallkrogen i siffror", "items": [
       "Utbyggnaden började 1933", "Närmare 1 000 småstugor",
       "Mer än tio hustyper", "941 äganderätter 2025"]}},
    {"id": "kulorerna", "h2": "Ljusa kulörer och stående panel med lockläkt",
     "paras": [
       "Stockholms stads vägledning för småhusområden beskriver att småstugornas fasader var av stående träpanel med tunn lockläkt och att färgsättningen från början var strikt reglerad till ett fåtal kulörer, ofta ljusa nyanser av grått, grönt och gult. Rödfärg fick användas efter särskild ansökan. Vägledningen markerar Tallkrogen, delar av Svedmyra och delar av Sköndal som kulturhistoriskt värdefulla miljöer.",
       "Lockpanel har många kanter. Varje läkt har två sidor och en framkant som ska täckas, och det är i skarven mellan läkt och bräda som vatten och smuts samlas. Vi tvättar, skrapar bort lös färg längs läkterna och slår i spikar som har krupit upp, så att de inte syns genom den nya färgen.",
       "Vägledningen råder att ta tillvara eller återskapa karaktärsskapande material, kulörer och detaljer, och påpekar att den enskilda byggnaden har stor påverkan på hela kvarterets karaktär. En ny stark kulör på en stuga i en grupp med ljusa hus syns därför mer än man tror.",
     ],
     "aside": None},
    {"id": "svedmyra", "h2": "Svedmyra: rött lertegel och grå ädelputs",
     "paras": [
       "Svedmyra byggdes ut med småstugor med början 1931–33. Stadsmuseet beskriver hur väggar och takstolar lyftes på plats i stora element för att göra bygget billigare, och hur Småstugebyrån gav både instruktioner och byggmaterial. Till områdets tidiga karaktär hör trähusfasadernas locklistpaneler och takens röda lertegel, men också viss variation i detaljerna.",
       "Den östra delen kompletterades under 1950-talet med ädelputsade småstugor i dämpade gråtoner. Där är det putsen som ger huset dess ton. Har den inte målats tidigare tvättar vi och lagar sprickor, och målar fönster, dörrar och takfot.",
       "Sköndal hade enligt områdesfakta 1 595 bostäder i småhus 2025, varav 1 194 äganderätter, och delar av stadsdelen är småstugeområde. Mer om taken finns under " + _L.format("taklaggare-farsta.html", "takläggare i Farsta") + ".",
     ],
     "aside": {"title": "Fasader i Farsta", "items": [
       "Locklistpanel i trä", "Ädelputs i gråtoner",
       "Rött lertegel på taken", "Radhusområden i utkanterna"]}},
    {"id": "lov-farsta", "h2": "Typritningar, karta och lovplikt",
     "paras": [
       "Vägledningen berättar att stadsbyggnadskontoret i slutet av 1970-talet samlade alla typritningar för småstugorna från 1927 till 1957, och att de finns hos stadsbyggnadskontoret eller på Stockholmskällan. Ritningen för din hustyp visar hur stugan såg ut från början.",
       "I Hökarängen, som tillsammans med Gubbängen var Stockholms första tunnelbaneförstad, är det flerbostadshusen som dominerar. Stadsmuseet beskriver fasaderna som vanligen spritputsade i olika jordfärger, med fasadindelningar och fönsteromfattningar av vita slätputsade band, byggda under senare delen av 1940-talet och början av 1950-talet. För ett flerbostadshus krävs enligt Stockholms stad bygglov för en fasadändring som vetter mot allmän plats, så en bostadsrättsförening som vill byta kulör behöver söka lov.",
       "För småhusen skriver staden att utökad lovplikt gäller om huset är markerat med blått eller grönt i Stadsmuseets klassificeringskarta eller ligger inom ett område med grön ring, och att kulörbyte då kräver bygglov. Ommålning i samma kulör räknas enligt Boverket normalt som underhåll. Läs mer om färg och fasad på " + _L.format("malare.html", "sidan om målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Farsta till",
  "steps": [
    ("Platsbesök", "Vi tittar på lockpanel, puts, fönster och dörrar och ser vilken kulör och färgtyp som sitter på."),
    ("Kartan", "Stadsmuseets klassificering och detaljplanen kontrolleras innan kulör väljs."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, förarbete och antal strykningar skrivs ut, fönster och dörrar för sig."),
    ("Förarbete", "Tvätt, skrapning längs läkterna, spikar slås i, trä lagas och fönster kittas."),
    ("Målning", "Grundning och strykningar i lämpligt väder, med de torktider färgen kräver."),
    ("Genomgång", "Vi går igenom stugan tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Farsta",
  "rot": [
    "Skatteverket räknar fasadmålning och målning av golv, tak, väggar, fönster och element som rotarbete i ett småhus, men inte staket och murar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "I en bostadsrätt i Farsta centrum eller Hökarängen gäller avdraget bara arbete inne i lägenheten. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Farsta?",
  "price": [
    "En småstuga är liten, men lockpanelen har många kanter och fönstren sitter i fasadliv, så förarbetet tar ofta lika lång tid som strykningen. Tillbyggnader mot trädgården och hur mycket lös färg som ska bort spelar också in. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka kulörer hade småstugorna i Tallkrogen från början?",
     "Enligt stadens vägledning var färgsättningen reglerad till ett fåtal ljusa kulörer, ofta i grått, grönt och gult. Rödfärg fick användas efter särskild ansökan."),
    ("Var hittar jag typritningen till min småstuga i Svedmyra?",
     "Stadsbyggnadskontoret sammanställde typritningarna för stugorna från 1927–1957, och de finns enligt staden hos stadsbyggnadskontoret eller på Stockholmskällan."),
    ("Ska ädelputsen på en småstuga från 1950-talet målas?",
     "Har den inte målats tidigare föreslår vi att den tvättas och lagas i stället, så att den grå tonen och strukturen finns kvar."),
    ("Behöver jag bygglov för att måla min stuga i Tallkrogen i en ny kulör?",
     "Tallkrogen är markerat som kulturhistoriskt värdefull miljö. Kontrollera Stadsmuseets karta. Är stugan klassad blått eller grönt krävs bygglov för ett kulörbyte."),
    ("Varför tar det så lång tid att måla en lockpanel?",
     "Varje läkt har tre sidor som ska täckas, och lös färg sitter ofta i skarven mot brädan. Förarbetet längs läkterna är det som gör att färgen håller."),
  ],
  "sources": [
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Tallkrogen (pdf)", _SSM.format("000041")),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Svedmyra (pdf)", _SSM.format("000043")),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Hökarängen (pdf)", _SSM.format("000082")),
    ("Stockholms stad – Områdesfakta Tallkrogen (2025)", _OF + "soderort/farsta/tallkrogen.pdf"),
    ("Stockholms stad – Områdesfakta Sköndal (2025)", _OF + "soderort/farsta/skondal.pdf"),
    _VARSAM, _STH_FASAD, _STH_KLASS, _BOV, _SKV, _SKV2,
  ],
  "cta": ("Ska småstugan eller villan i Farsta målas om?", "Boka ett gratis platsbesök så går vi igenom panel, kulör och kartan på plats."),
  "img": [
    ("Rad av små trähus med stående lockpanel i ljusa kulörer i Tallkrogen",
     "quiet narrow residential street with small detached 1930s Swedish one-and-a-half storey wooden cottages standing a few metres apart, each in its own garden, vertical board-and-batten panel painted pale grey, pale green or pale yellow, red clay tile gable roofs, low clipped hedges and apple trees, no road markings, Tallkrogen Stockholm, spring daylight, no people, no cars"),
    ("Gulmålad stående träpanel med slitna partier och pensel inför ommålning",
     "close-up of a weathered pale yellow vertical board-and-batten wooden wall on a small Swedish cottage, some battens scraped and sanded showing bare wood, a few nail heads, a paint scraper and a wire brush lying on a wooden trestle in the grass, natural daylight, no people, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VÄLLINGBY
"malare-vallingby.html": {
  "kind": "district", "service": "malare", "ort": "Vällingby", "svc_label": "Målare",
  "title": "Målare i Vällingby – radhus i riksintresset och lägenheter",
  "description": "Målare i Vällingby: lovplikt i riksintresset Vällingby–Råcksta, Langendals radhus, radhus som bostadsrätt och rotavdraget i lägenheten. Gratis platsbesök.",
  "h1": "Målare i Vällingby",
  "lead": "Vällingby och Råcksta är riksintresse för kulturmiljövården, och det påverkar mer än centrumet. Ska ett radhus få en ny kulör gäller andra regler här än i de flesta villaområden. Geal Entreprenad AB målar radhus, lägenheter och villor i Vällingby, Råcksta, Grimsta och Kälvesta, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Radhus och lägenheter i ABC-staden.",
  "sections": [
    {"id": "riksintresset", "anchor": "Riksintresset",
     "h2": "Riksintresset gäller även radhusen",
     "paras": [
       "Stockholms översiktsplan beskriver Vällingby-Råcksta (AB 120) som landets första ABC-stad, med arbete, bostäder och centrum, och ingen skulle ha längre än 900 meter till tunnelbanan. Bland de värdebärande dragen räknas de ursprungliga husens gestaltning och byggnadsdetaljer som fönster, entrépartier, balkonger och räcken, och centrumanläggningarnas omsorg om form-, färg- och materialverkan.",
       "Det är detta som gör färgfrågan annorlunda här. Stockholms stad skriver att du behöver söka bygglov för åtgärder som annars är bygglovsbefriade om huset ligger inom ett riksintresse för kulturmiljövården, som visas med blå ring i Stadsmuseets klassificeringskarta. Ett kulörbyte på ett radhus i Vällingby kan alltså kräva lov, trots att samma åtgärd är lovfri i många andra stadsdelar. För flerbostadshus krävs bygglov för fasadändringar mot allmän plats oavsett läge, så en förening med lamellhus kring centrum behöver söka lov för en ny kulör på gatusidan.",
       "Att måla om i samma kulör räknas enligt Boverket normalt som underhåll. Därför börjar vi med att ta reda på exakt vilken kulör och glans huset har i dag, så att ommålningen verkligen blir samma.",
     ],
     "aside": {"title": "Vällingby–Råcksta", "items": [
       "Riksintresse AB 120", "Blå ring i Stadsmuseets karta",
       "Kulörbyte kan kräva lov", "Samma kulör är underhåll"]}},
    {"id": "langendal", "h2": "Langendals radhus och områdena Atlantis och Omega",
     "paras": [
       "Stadsmuseets skrift om Råcksta beskriver bostadshusen som mycket välplanerade och kanske något av det bästa som byggdes under 1950-talet. Särskilt radhusen vid Långseleringen och Ramselegatan har uppmärksammats. De ritades av arkitekten Adrian Langendal och var färdiga 1953, och karakteristiskt är den livfulla färgsättningen och omväxlande detaljer som de dekorativa räckena vid de franska fönstren.",
       "Stadens vägledning för småhusområden nämner också radhusområdena Atlantis i nordost och Omega i nordväst som kulturhistoriskt synnerligen värdefulla. Vägledningen räknar tidstypisk färgsättning och enhetligt utformade husgrupper till karaktärsdragen i tunnelbanestädernas radhusområden.",
       "Smidesräcken vid franska fönster målas för hand. Riksantikvarieämbetets handbok beskriver för linoljefärg på järn och plåt att ytan stålborstas och dammas av och sedan grundas och stryks en till två gånger. Kulören tar vi fram från räcket innan något beställs. Stadsdelen har också äldre spår: Råcksta gård byggdes enligt Stadsmuseet på 1720-talet som en timrad, rödfärgad herrgård och moderniserades in- och utvändigt på 1770-talet.",
     ],
     "aside": None},
    {"id": "bostadsratt-radhus", "h2": "När radhuset är en bostadsrätt",
     "paras": [
       "Enligt stadens områdesfakta för 2025 fanns 449 bostäder i småhus i Vällingby, och 228 av dem var bostadsrätter. I Råcksta var 91 av 390 småhus bostadsrätter. I ett radhusområde som ägs av en förening är fasaden normalt föreningens, och då är det styrelsen som beställer målningen.",
       "Skatteverket ger rotavdrag i en bostadsrätt bara för arbete inne i bostaden, till exempel målning av väggar, tak och insidan av fönster och ytterdörrar. Att måla fasader, balkonger eller altaner ger inget avdrag, och arbete på gemensamma delar som tak, fasader och trapphus ingår inte heller. Föreningen kan alltså inte dra rotavdrag för fasadmålningen.",
       "Bor du i ett radhus med äganderätt gäller i stället reglerna för småhus, och då ger även fasaden rotavdrag. Sitter det äldre fasadskivor på huset tar vi reda på vad de består av innan de tvättas eller slipas, eftersom Boverket varnar för att asbest kan frigöras vid högtryckstvätt och slipning.",
     ],
     "aside": {"title": "Småhus 2025", "items": [
       "Vällingby: 449, varav 228 bostadsrätter", "Råcksta: 390, varav 299 äganderätter",
       "Föreningen beställer fasaden", "Rotavdrag bara inomhus i BRF"]}},
    {"id": "inomhus-vallingby", "h2": "Lägenheterna kring centrum",
     "paras": [
       "Kring centrum ligger enligt översiktsplanen en zon med höga punkthus och lägre flerbostadshus, och där är det lägenheten som målas. Vi målar väggar, tak, snickerier och dörrar och tapetserar, och skyddar golv och trapphus innan arbetet börjar. I hus från 1950-talet provar vi hur den gamla takfärgen sitter innan något nytt stryks på.",
       "Mer om radhusens tak och plåtdetaljer finns under " + _L.format("taklaggare-vallingby.html", "takläggare i Vällingby") + ", och om målning i allmänhet på " + _L.format("malare.html", "sidan om målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en målning i Vällingby till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, räcken, fönster och dörrar, eller på väggar och tak i lägenheten."),
    ("Kulör och lov", "Nuvarande kulör tas fram och Stadsmuseets karta kontrolleras innan något beställs."),
    ("Skriftligt kostnadsförslag", "Färgtyp, kulör, förarbete och antal strykningar, för föreningar gärna hus för hus."),
    ("Förarbete", "Tvätt, skrapning, rostborttagning på räcken, lagning och kittning."),
    ("Målning", "Grundning och strykningar i lämpligt väder, med de torktider färgen kräver."),
    ("Genomgång", "Vi går igenom resultatet tillsammans och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för målning i Vällingby",
  "rot": [
    "För radhus och villor med äganderätt räknar Skatteverket fasadmålning och målning av golv, tak, väggar, fönster och element som rotarbete. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "I en bostadsrätt gäller avdraget bara målning inne i bostaden. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Vällingby?",
  "price": [
    "För ett radhus avgör mängden trä, räcken och fönster och om flera hus i samma grupp målas samtidigt, så att ställningen kan flyttas mellan dem. I en lägenhet är det antalet rum och hur mycket spackling som behövs. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver jag bygglov för att måla mitt radhus i Vällingby i en ny kulör?",
     "Ligger huset inom riksintresset Vällingby–Råcksta, ja. Där gäller utökad lovplikt för åtgärder som annars är lovfria. Ommålning i samma kulör räknas normalt som underhåll."),
    ("Kan vår bostadsrättsförening få rotavdrag för att måla radhusens fasader?",
     "Nej. Skatteverket ger inte rotavdrag för målning av fasader i bostadsrätt eller för arbete på föreningens gemensamma delar."),
    ("Hur målas smidesräcken vid franska fönster?",
     "Rost och lös färg borstas bort, ytan dammas av och grundas och räcket stryks en eller två gånger i samma kulör som förut."),
    ("Vilka radhusområden i Vällingby räknas som särskilt värdefulla?",
     "Stadens vägledning nämner Atlantis och Omega, och Stadsmuseet lyfter fram Langendals radhus vid Långseleringen och Ramselegatan i Råcksta."),
    ("Kan ni måla flera radhus i samma länga vid samma tillfälle?",
     "Ja. Vi kan lämna ett gemensamt kostnadsförslag där varje hus redovisas för sig och planera ställningen så att den flyttas mellan husen."),
  ],
  "sources": [
    ("Stockholms stad – Översiktsplan för Stockholm: Riksintressen, Vällingby AB 120 (pdf)",
     "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf"),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Råcksta (pdf)", _SSM.format("000072")),
    ("Stockholms stad – Områdesfakta Vällingby (2025)", _OF + "vasterort/hasselby-vallingby/vallingby.pdf"),
    ("Stockholms stad – Områdesfakta Råcksta (2025)", _OF + "vasterort/hasselby-vallingby/racksta.pdf"),
    _VARSAM, _STH_FASAD, _STH_KLASS, _BOV, _BOV_ASB, _RAA, _SKV, _SKV2,
  ],
  "cta": ("Ska radhuset eller lägenheten i Vällingby målas?", "Boka ett gratis platsbesök så tar vi fram kulören och går igenom lovfrågan på plats."),
  "img": [
    ("Radhus från 1950-talet med franska fönster och dekorativa räcken i Råcksta",
     "1950s Scandinavian modernist two-storey terraced houses in a Stockholm suburb, simple flat plastered facades in soft ochre, light green and pale pink, low-pitched roofs, plain white windows, small French windows with simple black wrought iron railings, green lawns, big pine trees and exposed granite bedrock, Råcksta Vällingby, autumn daylight, no people, no cars"),
    ("Smidesräcke med flagnande färg och rost vid ett franskt fönster inför ommålning",
     "close-up of a decorative black wrought iron railing at a French window on a 1950s Swedish plastered house, part of the railing freshly primed in red-brown anti-rust primer and part still showing old flaking black paint, a wire brush resting on the window ledge, daylight, no people, no hands"),
  ],
  "related": [],
},

}
