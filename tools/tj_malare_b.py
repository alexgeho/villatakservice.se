# -*- coding: utf-8 -*-
"""Målare – ortsidor del B (tjänster v1, 2026-10-25): Huddinge, Norrtälje, Nacka, Täby.
Schema: se tools/tj_check.py. Fakta endast från öppnade källor (listade i sources per sida).
Vinkel (skild från byggtorg.se): underlag och färgtyp per husgeneration + kommunens regler."""

L = lambda href, txt: f'<a class="text-link" href="{href}">{txt}</a>'
X = lambda href, txt: f'<a class="text-link" href="{href}" rel="noopener">{txt}</a>'

U_BOV = "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/"
U_RAA = "https://www.raa.se/publicerat/9789172095830.pdf"
U_ROT = "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html"
U_ROTLISTA = "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html"
S_BOV = ("Boverket – Fasadändring (PBL kunskapsbanken)", U_BOV)
S_RAA = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färger (pdf)", U_RAA)
S_ROT = ("Skatteverket – Så fungerar rotavdraget", U_ROT)
S_ROTLISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?", U_ROTLISTA)

# ---------------------------------------------------------------- HUDDINGE
U_HUD2 = "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf"
U_HUD1 = "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram-del-1.pdf"
U_HUDF = "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/fasadandring"

HUDDINGE = {
  "kind": "district", "service": "malare", "ort": "Huddinge", "svc_label": "Målare",
  "title": "Målare i Huddinge – egnahem, tegelvillor och stugor",
  "description": "Målare i Huddinge: fasad och fönster på egnahem, 50-talsvillor med puts och tegel, grupphus och gamla stugor – plus vad kommunen säger om kulör.",
  "h1": "Målare i Huddinge",
  "lead": "Ska du anlita en målare i Huddinge avgör fasadens material mer än kulörkartan: träpanel på ett "
          "egnahem i Stuvsta, spritputs och tegel på en 50-talsvilla eller panel och mexitegel på ett "
          "radhus från 1970-talet. Vi målar fasader, fönster och rum i hela kommunen och börjar med ett gratis "
          "platsbesök.",
  "card": "Fasad, fönster och rum i Huddinge.",
  "sections": [
    {"id": "husen", "anchor": "Husen och målningen",
     "h2": "Fyra husgenerationer, fyra olika målningsjobb",
     "paras": [
       "Huddinges " + X(U_HUD2, "kulturmiljöprogram") + " delar in småhusen efter epok. Egnahemsområdena "
       "från 1910–40-talet, till exempel Stuvsta, Snättringe, Segeltorp och Fullersta, präglas av träpanel, "
       "enkelt spröjsade fönster och tegeltäckta sadeltak eller brutna tak. Här är nästan allt som syns målat "
       "trä – panel, knutar, foder, vindskivor och bågar – och det är detaljerna som bär husets karaktär.",
       "Folkhemsåren gav små villor, kedjehus och radhus i trä, puts eller fasadtegel, enligt programmet i "
       "ljusa eller mustiga kulörer. På 1950-talet blandades ofta rött eller gult tegel med grov spritputs "
       "eller trä. En sådan fasad är tre material som sköts på tre sätt, inte en yta som målas i ett svep.",
       "Under rekordåren dominerade grupphusen, och i slutet av 1970-talet byggdes radhusområden som Sörskogen "
       "och Utsälje. Programmet nämner tegel och kalksandsten, så kallat mexitegel, ofta kombinerat med panel och "
       "mustiga färger som blev ljusare mot 1980-talet. Vid Mellansjö och Gömmaren finns de gamla sportstugorna, "
       "byggda i en tid då den lilla röda stugan nära vattnet var idealet.",
     ],
     "aside": {"title": "Det som oftast målas", "items": [
       "Egnahem: panel, knutar, foder och spröjsade bågar",
       "40–50-tal: putspartier och inslag av trä",
       "Grupphus: panel mellan tegel eller mexi, fönster",
       "Stugor: röd träpanel"]}},
    {"id": "underlag",
     "h2": "Samma färgtyp som förut – det viktigaste valet",
     "paras": [
       "Riksantikvarieämbetets " + X(U_RAA, "skrift om byggnadsmåleri") + " ger ett tydligt råd: vid "
       "ommålning bör man i de flesta fall hålla sig till den färgtyp som redan sitter på huset. Att lägga "
       "moderna färger över äldre beskrivs som en teknisk risk som gör nästa underhåll svårare. Därför "
       "tar vi reda på vad som finns på fasaden innan vi föreslår färg, ofta genom att skrapa på ett "
       "undanskymt ställe.",
       "På Huddinges blandfasader från 1950-talet bedöms puts och trä var för sig. Spritputs ska enligt "
       "samma skrift rengöras skonsamt med våt- eller vattenblästring snarare än med stålborste, och gamla lagningar med fel "
       "bruk kan behöva göras om innan något målas. Tegel och mexitegel på grupphusen lämnar vi omålat; "
       "där gäller jobbet panelen, foder och fönster runt omkring.",
       "Skriften påpekar också att söderfasader behöver målas oftare än norrfasader, och fönster oftare än "
       "väggen runt dem. På ett egnahem med fri söderfasad kan det därför vara rimligt att måla södersidan "
       "och fönstren nu och låta norrsidan vänta.",
     ],
     "aside": None},
    {"id": "kulorer",
     "h2": "Vad kulturmiljöprogrammet råder om kulörer",
     "paras": [
       "Programmets råd gäller alla småhusområden från respektive epok, även de som inte är utpekade. För "
       "rekordårens småhus står det att den ursprungliga färgsättningen bör vara vägledande vid ommålning, "
       "med mustiga kulörer som gult och brunt som tongivande.",
       "I områden i omvandling, där gamla sommarstugor blandas med nyare villor, avråder programmet från "
       "fasadkulörer i vita nyanser och föreslår rött, brunt, grönt och gult. För egnahemmen är rådet att "
       "husets ursprungliga arkitektur ska värnas. All bebyggelse omfattas dessutom av varsamhetskravet i "
       "plan- och bygglagen.",
       "Råden är ingen lovplikt i sig, men de visar vad kommunen väger in. Ska ett radhus i en enhetlig "
       "länga byta från mörkbrunt till ljusgrått är det klokt att först prata med grannarna eller "
       "samfälligheten. Gäller arbetet mer än ytan, se " + L("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": {"title": "Råd ur programmet", "items": [
       "Rekordår: ursprunglig färgsättning vägledande",
       "Omvandlingsområden: undvik vita nyanser",
       "Egnahem: värna husets ursprungliga uttryck",
       "Allt: varsamhetskrav enligt PBL"]}},
    {"id": "lov",
     "h2": "Ny kulör och bygglov i Huddinge",
     "paras": [
       "Huddinge kommun skriver på sin " + X(U_HUDF, "sida om fasadändring") + " att ett en- eller "
       "tvåbostadshus inte behöver bygglov för att ändra utseende, så länge byggnaden eller området inte är "
       "kulturhistoriskt värdefullt och detaljplanen inte kräver lov. Att renovera fasaden med samma material "
       "och samma färg är också lovfritt. Om huset ligger i ett kulturmiljöområde ser du i kommunens webbkarta.",
       "Kulturmiljöprogrammets " + X(U_HUD1, "översikt") + " pekar ut särskilt värdefulla miljöer, bland dem "
       "Centrala Stuvsta, Sörskogen, Mellansjö och Östra Skogås. I sådana miljöer krävs enligt kommunen lov "
       "för att ändra husets utseende, till exempel med ny kulör. Boverket "
       "förklarar dessutom att ett byte av färgtyp, till exempel från linoljefärg till plastfärg, inte är ett "
       "kulörbyte men kan påverka husets yttre karaktärsdrag. I ett utpekat område kan alltså även en "
       "ommålning i samma nyans behöva prövas om färgen är av en annan sort.",
     ],
     "aside": None},
    {"id": "inomhus",
     "h2": "Målning inomhus i villor och radhus",
     "paras": [
       "Inomhus styr underlaget mer än reglerna. I ett egnahem från 1920-talet kan det finnas äldre färgtyper "
       "under senare lager. Riksantikvarieämbetet framhåller att det ofta räcker att rengöra milt och bättra "
       "skadorna med samma färgtyp, vilket dessutom gör nästa renovering lättare. I yngre hus är väggarna "
       "oftare skivor som spacklas, slipas och målas två gånger.",
       "Utomhusmålning görs enligt samma källa under april–september, medan rummen kan målas året runt i ett "
       "uppvärmt hus. Fasaden passar alltså på sommaren och vardagsrum, hall och trapphus på vintern.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett målningsjobb till i Huddinge",
  "steps": [
    ("Platsbesök och provskrapning", "Vi går runt huset, ser vad som är trä, puts och tegel och tar reda på vilken färgtyp som sitter på fasaden."),
    ("Kommunens karta", "Vi kontrollerar tillsammans om fastigheten ligger i ett kulturmiljöområde eller har bestämmelser i detaljplanen."),
    ("Skriftligt kostnadsförslag", "Fasader, fönster och rum redovisas var för sig, så att du kan välja ordning och omfattning."),
    ("Underarbete", "Lös färg skrapas bort, puts rengörs skonsamt, skadat trä lagas och ytor som ska målas får torka."),
    ("Målning", "Fasaden målas under den torra säsongen; rum målas när det passar dig, även vintertid."),
    ("Genomgång", "Vi går igenom resultatet och skriver upp färgtyp och kulör, så att nästa ommålning blir enkel."),
  ],
  "rot_h2": "ROT-avdrag för målare i Huddinge",
  "rot": [
    "Skatteverket räknar målning av fasader, fönster, väggar, tak och golv samt tapetsering som rotarbete i "
    "ett småhus. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per person och år, och "
    "tillsammans med RUT högst 75 000 kronor. Färgen räknas som material och ger inget avdrag. Vi drar "
    "avdraget direkt på fakturan.",
    "I en bostadsrätt ger bara arbete inne i lägenheten avdrag, inte fasad, balkong eller utsidan av fönster. "
    "Målning av staket och murar ger inte avdrag i någon boendeform, enligt " + X(U_ROTLISTA, "Skatteverkets lista") + ".",
  ],
  "price_h2": "Vad styr kostnaden för målning i Huddinge?",
  "price": [
    "Mest påverkar underarbetet: hur mycket färg som släpper, om puts eller trä behöver lagas och hur många "
    "detaljer huset har. Ett egnahem med spröjsade bågar, foder och knutar tar längre tid per kvadratmeter än "
    "en slät panel, och på en brant tomt styr terrängen hur ställningen kan stå.",
    "Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag som visar vad som ingår.",
  ],
  "faq": [
    ("Kan ni måla bara södersidan på vårt egnahem i Stuvsta?",
     "Ja, om övriga sidor är i gott skick. Söderfasader slits fortare än norrfasader, så det är vanligt att "
     "de målas oftare. Vi använder samma färgtyp och kulör som finns, så att skillnaden mellan sidorna blir liten."),
    ("Ska spritputsen på vår 50-talsvilla i Huddinge målas eller bara tvättas?",
     "Det beror på skicket. Ibland räcker en skonsam tvätt med vatten och lagning av skadade partier. Ska den "
     "målas väljer vi en färg som passar putsen och det som redan sitter på den."),
    ("Behöver mexiteglet på vårt radhus från 1970-talet målas?",
     "Nej. Kalksandstenen är ett fasadmaterial som programmet beskriver som typiskt för epoken, och målar man "
     "över den ändras husets uttryck. Vi målar panel, foder och fönster runt teglet."),
    ("Vi har en röd sportstuga vid Mellansjö – får vi byta kulör?",
     "Mellansjö är ett av de särskilt värdefulla områdena i kulturmiljöprogrammet, och där krävs normalt lov för ny "
     "kulör. För områden i omvandling, där gamla stugor blandas med nya villor, avråder programmet dessutom "
     "från vita nyanser. Samma kulör som tidigare räknas normalt som underhåll."),
    ("Vart vänder jag mig om jag är osäker på om kulörbytet kräver lov i Huddinge?",
     "Kommunens servicecenter kan svara på allmänna frågor. Vill du ha ett skriftligt beslut kan du söka "
     "frivilligt bygglov, som prövas som en vanlig ansökan och kostar en avgift."),
  ],
  "sources": [
    ("Huddinge kommun – Kulturmiljöprogram del 2 (småhus, semesterbostäder)", U_HUD2),
    ("Huddinge kommun – Kulturmiljöprogram del 1 (särskilt värdefulla miljöer)", U_HUD1),
    ("Huddinge kommun – Ändra fasad eller tak", U_HUDF),
    S_BOV, S_RAA, S_ROT, S_ROTLISTA,
  ],
  "cta": ("Målare till ditt hus i Huddinge", "Boka ett gratis platsbesök så går vi igenom fasad, fönster och rum och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Nymålad ockragul träpanel med vita foder på ett egnahem i Huddinge",
     "freshly repainted ochre yellow wooden 1920s Swedish detached house with white corner boards and window trim, small-paned windows, red clay tile gambrel roof, old fruit trees, hilly suburban street, Stuvsta Huddinge, summer"),
    ("Radhus med ljust mexitegel och brunmålad panel i Huddinge",
     "1970s Swedish terraced houses with light grey calcium silicate brick and freshly painted dark brown wooden panel sections, brown window frames, pine trees and bare granite rock, Huddinge, late summer"),
  ],
}

# ---------------------------------------------------------------- NORRTÄLJE
U_SCB = "https://www.scb.se/hitta-statistik/artiklar/2026/fritidshus-vart-finns-de/"
U_NTF = "https://www.norrtalje.se/sjalvservice/bygga-bo-miljo/fasadandring/"
U_NTB = "https://www.norrtalje.se/info/trafik-gator-parker/bevarandeprogram-for-norrtalje-stad/"
U_NTL = "https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/lovbefriade-atgarder/"

NORRTALJE = {
  "kind": "district", "service": "malare", "ort": "Norrtälje", "svc_label": "Målare",
  "title": "Målare i Norrtälje – fritidshus, kust och småstad",
  "description": "Målare i Norrtälje: slamfärg och linoljefärg på trähus, hus i öppna kustlägen, permanentade fritidshus och lovreglerna i kommunen och stadskärnan.",
  "h1": "Målare i Norrtälje",
  "lead": "En målare i Norrtälje arbetar ofta på hus där ägaren bara är på plats delar av året, eller där "
          "material måste fram med båt. På ett äldre trähus i Roslagen är frågan om färgtyp ofta viktigare än "
          "kulören. Vi målar fasader, fönster och interiörer i hela kommunen – i staden, i Rimbo och Hallstavik "
          "och längs kusten.",
  "card": "Trähus, fritidshus och kustlägen i Norrtälje.",
  "sections": [
    {"id": "roslagen", "anchor": "Husen i kommunen",
     "h2": "Fritidshus, tätorter och en gammal stadskärna",
     "paras": [
       "Norrtälje är enligt " + X(U_SCB, "SCB") + " Sveriges mest fritidshustäta kommun, med 27 352 "
       "fritidshus 2025. Många av dem används i dag långt utanför sommaren. Ett hus som byggdes för "
       "juni–augusti och nu värms upp året runt ställer andra krav både på fasaden och på rummen innanför.",
       "Stadskärnan har ett " + X(U_NTB, "bevarandeprogram") + " som kommunfullmäktige fastställde 1981 och "
       "som kommunen sedan har uppdaterat, och den del som ligger inom riksintresset för kulturmiljövården ska "
       "bevaras och vårdas. Där är äldre trähus och gårdar en stor del av stadsbilden.",
       "Utanför staden finns villaområden i Rimbo och Hallstavik och äldre kustbebyggelse, bland annat i "
       "Grisslehamn på Väddö.",
     ],
     "aside": {"title": "Vanliga uppdrag här", "items": [
       "Fritidshus som blivit åretruntboende",
       "Villor i Rimbo och Hallstavik",
       "Gårdar i och kring stadskärnan",
       "Hus i öppna lägen mot havet"]}},
    {"id": "fargtyp",
     "h2": "Slamfärg, linoljefärg eller modern täckfärg?",
     "paras": [
       "Riksantikvarieämbetet beskriver i sin " + X(U_RAA, "skrift om traditionellt måleri") + " slamfärg "
       "som matt, fuktgenomsläpplig och enkel att stryka. Den fäster bra på ohyvlat virke men sämre på hyvlat, "
       "och den är enligt skriften den mest underhållsvänliga färgtypen: borsta av och måla om. Linoljefärg "
       "dominerade på trähus ända till mitten av 1900-talet där rödfärg inte användes.",
       "På en gammal rödfärgad stuga är det därför sällan rätt att byta till en täckande plastfärg. Skriften "
       "varnar för att moderna färger över äldre typer ger en teknisk risk, och att man ofta inte kan gå "
       "tillbaka utan att ta bort all färg. Vi börjar med att ta reda på vad som sitter på väggen och om "
       "panelen är hyvlad eller sågad.",
       "Ett byte av färgtyp kan också vara en lovfråga. Boverket skriver att en övergång från slamfärg till "
       "silikonhartsfärg inte räknas som kulörbyte, men att den kan påverka byggnadens yttre karaktärsdrag.",
     ],
     "aside": {"title": "Före vi väljer färg", "items": [
       "Vilken färgtyp sitter på fasaden i dag?",
       "Är panelen hyvlad eller ohyvlad?",
       "Finns röta vid sockel och fönsterbleck?",
       "Är huset i ett särskilt värdefullt område?"]}},
    {"id": "kusten",
     "h2": "Väder, sol och vind vid kusten",
     "paras": [
       "Enligt samma skrift bör utomhusmålning i Mellansverige göras under april–september, och trä som ska "
       "målas får inte ha högre fuktkvot än 15 procent. Med linoljefärg är maj–augusti bäst, och direkt "
       "solsken undviks eftersom ytan kan torka för fort och slå blåsor. Målaren följer solen och tar de "
       "fasader som redan har haft sol.",
       "Ett hus på en udde eller i ett öppet läge mot havet får hårdare väder än en gård i skogen kring "
       "Rimbo. De mest utsatta delarna – fönster, vattbrädor, trappor, räcken och plåt – bör enligt "
       "Riksantikvarieämbetet underhållsmålas löpande, annars tar underlaget skada. Därför föreslår vi ofta "
       "att fönster och snickerier målas oftare än själva väggen.",
       "Saknar fastigheten bilväg ända fram planerar vi transport av ställning, färg och avfall redan vid "
       "besöket.",
     ],
     "aside": None},
    {"id": "lov",
     "h2": "Lovreglerna för ny kulör i Norrtälje kommun",
     "paras": [
       "Norrtälje kommun skriver på sin " + X(U_NTF, "sida om fasadändring") + " att byte av färg räknas "
       "som fasadändring. Inom detaljplan krävs lov för hus som inte är en- eller tvåbostadshus om fasaden "
       "vetter mot väg eller allmän plats, och för alla hus om detaljplanen har utökad lovplikt. Utanför "
       "detaljplan krävs lov om fastigheten ligger i ett särskilt värdefullt område. Enligt Boverket krävs lov "
       "också för särskilt värdefulla byggnader och där detaljplanen har skyddsbestämmelser.",
       "Kommunens karta visar om fastigheten ligger inom detaljplan och i ett värdefullt område. Kommunen "
       "bedömer inte enskilda åtgärder per telefon eller e-post; vill du ha ett bindande besked kan du söka "
       "frivilligt lov. Gäller det en gård i stadskärnan är bevarandeprogrammet värt att läsa innan kulören "
       "bestäms. Att måla om i samma kulör räknas enligt Boverket normalt som underhåll.",
     ],
     "aside": None},
    {"id": "inomhus",
     "h2": "När sommarhuset blir åretruntbostad",
     "paras": [
       "När ett fritidshus permanentas kan det vara läge att måla rummen i samma veva som andra arbeten på "
       "huset. Inomhus kan man måla året runt så länge huset är uppvärmt, så det arbetet passar gärna under "
       "vinterhalvåret. Har stugan äldre linoljefärg på väggar eller snickerier är det bra att veta att den "
       "gulnar något med tiden, mest i mörka utrymmen.",
       "Blir det fler arbeten än målning samordnar vi dem som en helhet – läs om " +
       L("villarenovering.html", "villarenovering") + " och om takarbeten hos " +
       L("taklaggare-norrtalje.html", "takläggare i Norrtälje") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras ett målningsjobb i Norrtälje",
  "steps": [
    ("Bilder och första samtal", "Är du inte på plats kan du skicka bilder på fasader och rum, så förbereder vi besöket."),
    ("Platsbesök", "Vi tittar på färgtyp, panel och träets skick och på hur ställning och material tar sig fram, även om det kräver båt."),
    ("Kontroll i kommunkartan", "Vi ser om fastigheten ligger inom detaljplan eller i ett särskilt värdefullt område."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där transport, lagningar och målning står var för sig."),
    ("Målning i torrt väder", "Utvändigt arbete läggs i den varma, torra delen av säsongen; rum kan göras under vintern."),
    ("Avslut", "Vi går igenom jobbet på plats eller med bilder och lämnar uppgift om färgtyp och kulör."),
  ],
  "rot_h2": "ROT-avdrag för målning i Norrtälje",
  "rot": [
    "Rotavdraget gäller enligt " + X(U_ROT, "Skatteverket") + " även fritidshus och bostäder där du bara "
    "bor ibland, så länge du äger bostaden och du eller dina föräldrar helt eller delvis bor där. Avdraget är 30 procent av "
    "arbetskostnaden, högst 50 000 kronor per person och år (högst 75 000 kronor tillsammans med RUT). "
    "Färg, resor och transporter ger inget avdrag. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Norrtälje?",
  "price": [
    "Avståndet och vägen fram påverkar mer här än i tätare kommuner: ska ställning och färg fraktas med båt "
    "eller bäras sista biten syns det i förslaget. Därtill kommer husets storlek, hur mycket gammal färg som "
    "måste tas bort och om panel eller fönsterbleck behöver lagas.",
    "Platsbesöket är kostnadsfritt, och du får ett skriftligt kostnadsförslag innan något arbete startar.",
  ],
  "faq": [
    ("Kan ni måla fritidshuset i Norrtälje medan vi är hemma i stan?",
     "Ja. Vi kommer överens om nycklar, var ställning och färg får stå och hur vi stämmer av, till exempel "
     "med bilder under arbetet."),
    ("Vår stuga i Roslagen har slamfärg – kan vi byta till täckande färg?",
     "Det går, men det är sällan klokt. Slamfärg är lätt att underhålla, och en modern färg ovanpå kan ge "
     "problem som bara löses genom att all färg tas bort. Ligger huset i ett värdefullt område kan bytet "
     "dessutom kräva lov."),
    ("Vi har en gård i Norrtäljes gamla stadskärna – vad ska vi kolla före ommålning?",
     "Läs detaljplanen och kommunens bevarandeprogram för stadskärnan, som ligger inom riksintresset. Ska "
     "kulören ändras är ett frivilligt lov ett sätt att få ett säkert besked."),
    ("Hur ofta behöver fönstren målas på ett hus nära havet?",
     "Det finns inget fast intervall; det beror på läge och väderstreck. Fönster och vattbrädor slits "
     "fortare än väggen, så vi ser över dem vid varje besök och föreslår bättring innan träet tar skada."),
    ("Är det för sent att måla fasaden i oktober?",
     "Ofta ja. Riksantikvarieämbetets råd är att måla ute mellan april och september, när träet är torrt. "
     "Hösten passar bättre för invändig målning och för att boka nästa säsong."),
  ],
  "sources": [
    ("SCB – Fritidshus, var finns de?", U_SCB),
    ("Norrtälje kommun – Fasadändring", U_NTF),
    ("Norrtälje kommun – Lovbefriade åtgärder (kartor, frivilligt lov)", U_NTL),
    ("Norrtälje kommun – Bevarandeprogram för Norrtälje stad", U_NTB),
    S_BOV, S_RAA, S_ROT,
  ],
  "cta": ("Målare till huset i Norrtälje", "Boka ett gratis platsbesök – vi planerar även för hus som bara nås med båt."),
  "img": [
    ("Faluröd trästuga med vita knutar vid vattnet i Norrtälje kommun",
     "traditional Swedish falu red wooden summer house with white corner boards and white window frames, freshly painted matte red rough-sawn panel, granite rocks and pine trees by the Baltic sea, Roslagen archipelago, Norrtälje, summer"),
    ("Nymålade fönster och vattbräda på ett trähus i Roslagen",
     "close-up of freshly painted white wooden window frame and window sill on a falu red wooden house, rough-sawn vertical board panel, coastal light, Roslagen Sweden"),
  ],
}

# ---------------------------------------------------------------- NACKA
U_NKF = "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/lovfria-atgarder/fasadandringar/"
U_NKN = "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/nyheter-om-nya-lagandringen/2025/10/nya-pbl-regler-ger-mer-frihet-och-storre-ansvar-for-nackas-fastighetsagare/"
U_NKJ = "https://www.nacka.se/499626/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-jarnvagen.pdf"
U_NKS = "https://www.nacka.se/499628/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-sommarnojen.pdf"

NACKA = {
  "kind": "district", "service": "malare", "ort": "Nacka", "svc_label": "Målare",
  "title": "Målare i Nacka – sekelskiftesvillor och sommarnöjen",
  "description": "Målare i Nacka: linoljefärg på sekelskiftesvillor längs Saltsjöbanan, sommarvillor i Boo, snickerier och fönster – och kulturmiljökartans lovregler.",
  "h1": "Målare i Nacka",
  "lead": "Som målare i Nacka arbetar man ofta på trähus där snickerierna betyder lika mycket som väggarna: "
          "villorna längs Saltsjöbanan och sommarvillorna vid farleden i Boo. Där avgör kulturmiljökartan och "
          "färgen som redan sitter på huset mer än en kulörkarta. Vi målar fasader, fönster och rum i hela "
          "Nacka och börjar med ett gratis platsbesök.",
  "card": "Panelvillor och sommarnöjen i Nacka.",
  "sections": [
    {"id": "saltsjobanan", "anchor": "Villorna vid banan",
     "h2": "Panelarkitekturen längs Saltsjöbanan",
     "paras": [
       "Nackas " + X(U_NKJ, "kulturmiljöprogram för villasamhällena vid järnvägen") + " beskriver hur "
       "Saltsjöbaden, Neglinge, Storängen och Saltsjö-Duvnäs växte fram från 1890-talet med påkostade villor "
       "i tidstypisk panelarkitektur, på stora och kuperade tomter. Solsidan bebyggdes framför allt "
       "1930–1950.",
       "Programmets förhållningssätt är att tidstypisk utformning av fasader, fönster, fönsteromfattningar, "
       "entrépartier, räcken, staket och grindar ska behållas. För en målare betyder det många ytor och "
       "mycket handarbete: profilerade foder, lister och spröjs ska skrapas och målas, inte bytas eller "
       "kläs in. Ett trasigt foder lagas hellre än ersätts av en slät bräda.",
     ],
     "aside": {"title": "Ytor på en sekelskiftesvilla", "items": [
       "Panel, knutbrädor och vindskivor",
       "Profilerade fönsteromfattningar och spröjsade bågar",
       "Verandor, räcken och entrépartier",
       "Staket och trädgårdsgrindar"]}},
    {"id": "farleden",
     "h2": "Sommarnöjena i Boo – från ljus panel till falurött",
     "paras": [
       "Programmet för " + X(U_NKS, "sommarnöjena vid farleden") + " berättar om schweizervillor med långt "
       "utskjutande tak, lövsågade ornament och verandor, byggda från 1860-talet i bland annat Vikingshill "
       "och på Tegelön. Ljusmålad panel dominerar på de äldre sommarvillorna. Runt sekelskiftet slog "
       "nationalromantiken igenom, och husen fick fasader i falurött eller timmerbrunt med stramare foder.",
       "De senare sportstugorna i skogsbackarna har enligt programmet en enklare arkitektur och en "
       "naturanpassad färgsättning. För komplementbyggnader föreslås en enkel färgsättning, med knutar och "
       "foder i ungefär samma färg som fasaden.",
       "Ornament och verandor är det som först tar stryk av väder. Vi går igenom dem bit för bit, lagar "
       "lösa delar och målar dem för hand, så att detaljerna finns kvar till nästa ommålning.",
     ],
     "aside": None},
    {"id": "linolja",
     "h2": "Linoljefärg på de äldre trähusen",
     "paras": [
       "Riksantikvarieämbetets " + X(U_RAA, "skrift om byggnadsmåleri") + " beskriver linoljefärg som den "
       "färg som dominerade på trähus fram till mitten av 1900-talet där rödfärg inte användes. Den tränger "
       "in och fäster bra, och med åren kritar den, vilket gör nästa ommålning enklare. Den är också "
       "förhållandevis lätt att underhålla och att ta bort.",
       "Skriften rekommenderar att måla med linoljefärg när det är varmt och torrt, helst maj–augusti, och "
       "att undvika direkt sol. Den råder också att spara små omålade provytor på undanskymda ställen, så "
       "att den som målar nästa gång kan se vad som använts. Det gör vi på äldre villor, och vi skriver "
       "upp färgtyp och kulör åt dig.",
       "Har huset i stället fått plastfärg vid en tidigare ommålning bedömer vi om den kan målas över eller "
       "behöver tas bort. Det går inte att avgöra utan att se fasaden.",
     ],
     "aside": None},
    {"id": "lov",
     "h2": "Kulturmiljökartan styr lovplikten i Nacka",
     "paras": [
       "Sedan 1 december 2025 behövs normalt inget bygglov för fasadändringar som målning på ett en- eller "
       "tvåbostadshus. Nacka kommun " + X(U_NKN, "skriver") + " samtidigt att lättnaderna inte gäller i "
       "särskilt värdefulla byggnader och områden, där kraven på lov kvarstår och i vissa fall blir högre.",
       "På sidan om " + X(U_NKF, "fasadändringar") + " förklarar kommunen att lovplikten i sådana områden "
       "omfattar alla fasadändringar som påverkar områdets eller husets karaktär. Kartan visar i lila miljöer "
       "med särskilt höga kulturvärden, och orange betyder att en bedömning kan pågå. Kulturmiljöprogrammet "
       "anger dessutom att Storängen har utökad lovplikt för bland annat omfärgning, och att antikvarisk "
       "medverkan kan krävas vid bygglov i villasamhällena.",
       "Boverket påpekar att även ett byte av färgtyp, till exempel från linoljefärg till plastfärg, kan "
       "påverka husets karaktärsdrag. Att måla om i samma kulör räknas däremot normalt som underhåll. Vi "
       "kontrollerar fastigheten i kartan innan vi föreslår färg, så att du vet vad som gäller innan arbetet "
       "bokas.",
     ],
     "aside": {"title": "Kolla före kulörval", "items": [
       "Lila eller orange markering i kommunens karta",
       "Detaljplanens bestämmelser för fastigheten",
       "Byte av kulör eller av färgtyp",
       "Om samfälligheten har egna färgregler"]}},
  ],
  "steps_h2": "Så målar vi ett äldre trähus i Nacka",
  "steps": [
    ("Platsbesök", "Vi går runt huset, provskrapar och ser vilken färgtyp som finns och hur snickerierna mår."),
    ("Kulturmiljökartan", "Vi slår upp fastigheten och detaljplanen och ser om ny kulör eller färgtyp kräver lov."),
    ("Skriftligt kostnadsförslag", "Fasad, fönster, veranda och staket står var för sig i förslaget."),
    ("Skrapning och lagning", "Lös färg skrapas bort, ornament och foder lagas och ytorna rengörs inför målning."),
    ("Målning", "Utvändigt arbete görs under den varma och torra säsongen och följer solen runt huset."),
    ("Dokumentation", "Du får uppgift om färgtyp och kulör, och små provytor sparas till nästa gång."),
  ],
  "rot_h2": "ROT-avdrag för målare i Nacka",
  "rot": [
    "Att måla fasader, fönster, väggar och tak samt att tapetsera räknas som rotarbete i en villa, enligt "
    + X(U_ROTLISTA, "Skatteverket") + ". Avdraget är 30 procent av arbetskostnaden, högst 50 000 kronor per "
    "person och år, och ROT och RUT är tillsammans högst 75 000 kronor. Material ingår inte. Vi drar "
    "avdraget direkt på fakturan.",
    "Bor du i bostadsrätt ger bara arbete inne i lägenheten avdrag. Målning av fasad, balkong och utsidan "
    "av fönster och dörrar, liksom av staket och murar, ger inget avdrag.",
  ],
  "price_h2": "Vad styr priset på målning i Nacka?",
  "price": [
    "På en sekelskiftesvilla är det detaljerna som kostar tid: profilerade foder, spröjsade bågar, "
    "verandaräcken och lövsågade ornament. Därtill kommer hur mycket färg som måste skrapas bort, om trä "
    "behöver lagas och hur ställningen kan stå på en brant sjötomt.",
    "Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag. Behövs även andra arbeten på huset "
    "samordnar vi dem – läs om " + L("villarenovering.html", "villarenovering") + " och om takarbeten hos " +
    L("taklaggare-nacka.html", "takläggare i Nacka") + ".",
  ],
  "faq": [
    ("Får verandan på vår schweizervilla i Boo målas i en annan kulör än fasaden?",
     "Det beror på var villan ligger. I ett område med lila markering i Nackas karta krävs lov för ändringar "
     "som påverkar husets karaktär, och kulör räknas dit. Vi kontrollerar fastigheten innan vi föreslår "
     "färgsättning."),
    ("Krävs lov för att måla om vår villa i Storängen i samma kulör?",
     "Samma kulör räknas normalt som underhåll. Storängen har dock utökad lovplikt för omfärgning enligt "
     "kulturmiljöprogrammet, så byter du nyans eller färgtyp bör du kontakta kommunen först."),
    ("Kan ni laga lövsågade ornament innan de målas?",
     "Ja, lösa och spruckna delar lagas och fästs innan målning. Saknas en del helt kan en snickare göra en "
     "kopia efter de bevarade."),
    ("Hur märker man om fasaden har linoljefärg eller plastfärg?",
     "Linoljefärg kritar med åren, så att ytan kan kännas pulvrig mot handen. Men flera lager från olika "
     "årtionden kan dölja varandra, så säkrast är en provskrapning, som vi gör vid besöket."),
    ("Vad betyder orange markering i Nackas karta för en målare?",
     "Att kommunen kan hålla på att bedöma kulturvärdena. Planerar du ny kulör ska du kontakta "
     "stadsbyggnadsservice innan arbetet bokas."),
  ],
  "sources": [
    ("Nacka kommun – Fasadändringar (utökad lovplikt, kulturmiljökarta)", U_NKF),
    ("Nacka kommun – Nya PBL-regler ger mer frihet och större ansvar", U_NKN),
    ("Nacka kommun – Kulturmiljöprogram: Villasamhällen vid järnvägen (pdf)", U_NKJ),
    ("Nacka kommun – Kulturmiljöprogram: Sommarnöjen vid farleden (pdf)", U_NKS),
    S_BOV, S_RAA, S_ROT, S_ROTLISTA,
  ],
  "cta": ("Målare till din villa i Nacka", "Boka ett gratis platsbesök så går vi igenom fasad, snickerier och fönster."),
  "img": [
    ("Ljusmålad sekelskiftesvilla med snickarglädje och veranda i Nacka",
     "freshly painted pale yellow Swedish 1900s wooden villa with ornate white carved trim, glazed veranda, profiled window surrounds and red tile roof, steep rocky garden with pine trees by the sea, Saltsjobaden Nacka, summer"),
    ("Nymålade lövsågade ornament och verandaräcke på en schweizervilla i Nacka",
     "close-up of freshly painted white fretwork ornaments and veranda railing on a 19th century Swiss chalet style wooden summer villa, light painted panel, Stockholm archipelago"),
  ],
}

# ---------------------------------------------------------------- TÄBY
U_TBF = "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/fasadandring"
U_TBK = "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"

TABY = {
  "kind": "district", "service": "malare", "ort": "Täby", "svc_label": "Målare",
  "title": "Målare i Täby – trävillor, puts och kedjehus",
  "description": "Målare i Täby: panel och foder på villastadens trähus, putsade villor i Näsbypark, kedjehus från 1970-talet och vad Kulturmiljöer i Täby säger.",
  "h1": "Målare i Täby",
  "lead": "En målare i Täby möter tre helt olika fasader: trävillorna från början av 1900-talet vid "
          "Roslagsbanan, de putsade villorna i Näsbypark och 1970-talets kedjehus med tegel och brun panel. "
          "Kommunens underlag beskriver kulörerna område för område. Vi målar fasader, fönster och rum i hela "
          "Täby, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Trävillor, puts och kedjehus i Täby.",
  "sections": [
    {"id": "travillor", "anchor": "Trävillorna",
     "h2": "Trävillorna i kyrkbyn och Viggbyholm",
     "paras": [
       "Enligt kommunens underlag " + X(U_TBK, "Kulturmiljöer i Täby") + " växte en villastad fram kring "
       "järnvägsstationen i Täby kyrkby efter en avstyckningsplan från 1907. De äldre villorna har ofta "
       "liggande spontad panel, målad med falu rödfärg eller täckmålad i ljusa toner, och fönsterfoder, "
       "vindbrädor och knutar är oftast vita.",
       "I Norra Viggbyholm, på båda sidor om Roslagsbanan, byggdes först mest sommarstugor och från 1930-talet allt fler villor. Där "
       "är träfasaderna täckmålade i ljusa kulörer eller avfärgade i falurött med foder i en kontrasterande "
       "färg, medan de putsade husen har milda pastellfärger. Riktlinjen är att den ursprungliga "
       "färgsättningen ska vara vägledande.",
       "För målningen betyder det två system på samma hus: en färg för panelen och en annan för foder, knutar "
       "och vindskivor, ofta också en tredje för fönsterbågarna. Rödfärgad panel och täckmålad panel är "
       "dessutom olika färgtyper som inte ska blandas ihop.",
     ],
     "aside": {"title": "Typiskt för de äldre villorna", "items": [
       "Liggande spontad panel",
       "Falu rödfärg eller ljus täckfärg",
       "Vita foder, knutar och vindbrädor",
       "Spröjsade fönster, verandor och burspråk"]}},
    {"id": "puts",
     "h2": "Putsade villor i Näsbypark",
     "paras": [
       "Kulturmiljöunderlaget visar bland annat en villa i Näsbypark från 1926 med putsad fasad avfärgad i "
       "vitt och mörkt gröna fönstersnickerier. På en sådan fasad är det putsen och färgen på den som "
       "bestämmer metoden.",
       "Riksantikvarieämbetets " + X(U_RAA, "skrift om byggnadsmåleri") + " förklarar att kalkfärg i dag "
       "främst används för att måla om tidigare kalkavfärgade ytor. Den fäster bra på kalkputs men dåligt "
       "på cementrika underlag, och den släpper igenom fukt. Färgen stryks ett skikt per dag och ska läggas "
       "utan avbrott på en fasadyta, annars syns skarvar; uppehåll görs bara vid hörn eller andra naturliga "
       "gränser. Utomhus görs arbetet från senvåren till eftersommaren, i god tid före frost.",
       "Därför behöver en kalkputsad villa ett arbetslag som hinner en hel fasad i taget och en plan för "
       "vädret. Skador lagas med puts som liknar den befintliga innan färgen läggs på.",
     ],
     "aside": None},
    {"id": "kedjehus",
     "h2": "Kedjehus och radhus från 1960–70-talen",
     "paras": [
       "Kvarteret Kammaren från 1976 beskrivs i underlaget som ett ovanligt välbevarat kedjehuskvarter: "
       "bottenvåning i fasadtegel, gavlar i brunmålad stående panel och bruna fönstersnickerier. Riktlinjen "
       "är att behålla originalkulörerna och inte putsa över teglet. Den mörka färgsättningen beskrivs som "
       "typisk för tiden.",
       "Kvarteret Ankaret i Näsbypark, radhus från 1968 som byggdes för officerare vid Sjökrigsskolan på Näsby "
       "slott, har vit kalksandsten och liggande panel i ljust grått. För de nyare husen vid slottet finns ett färgprogram som ska följas vid underhåll och "
       "ommålning. För grupphusområden i stort säger riktlinjerna att den ursprungliga färgsättningen bör "
       "behållas och att carport och altan inte ska bryta av i färg.",
       "Vi målar panel, foder och snickerier och lämnar teglet orört. Ska en hel länga målas samtidigt "
       "stämmer vi av kulören med samfälligheten innan vi börjar.",
     ],
     "aside": None},
    {"id": "lov",
     "h2": "Lovplikt och kommunens riktlinjer i Täby",
     "paras": [
       "Täby kommun skriver på sin sida om " + X(U_TBF, "fasadändring") + " att ett en- eller "
       "tvåbostadshus inte behöver bygglov för att byta kulör, så länge byggnaden inte är särskilt värdefull, "
       "inte ligger i ett särskilt värdefullt område och inte har utökad lovplikt i detaljplanen.",
       "Kulturmiljöer i Täby antogs av kommunfullmäktige den 8 april 2024. Riktlinjerna är inte juridiskt "
       "bindande, men de ska vägleda kommunens beslut. Området närmast Näsby slott är byggnadsminne sedan "
       "1943, och där krävs Länsstyrelsens tillstånd för ändringar som strider mot skyddsbestämmelserna.",
       "Enligt Boverket är det inget kulörbyte att gå från linoljefärg till plastfärg, men ett sådant byte "
       "kan påverka husets karaktärsdrag och därmed vara lovpliktigt i ett värdefullt område. Mer om "
       "helhetsjobb finns under " + L("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": {"title": "Kontrollera först", "items": [
       "Nämns huset eller kvarteret i Kulturmiljöer i Täby?",
       "Har detaljplanen skyddsbestämmelser?",
       "Ändras kulör eller färgtyp?",
       "Gäller ett färgprogram för området?"]}},
  ],
  "steps_h2": "Så går ett målningsjobb till i Täby",
  "steps": [
    ("Besök på plats", "Vi ser om fasaden är trä, puts eller tegel och provskrapar för att se vilken färg som sitter där."),
    ("Kulturmiljöunderlaget", "Vi läser vad Kulturmiljöer i Täby och detaljplanen säger om just ditt område."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där fasad, snickerier och invändiga rum står för sig."),
    ("Förarbete", "Lös färg tas bort, puts och trä lagas, och ytor som inte ska målas skyddas."),
    ("Målning", "Kalkputs målas en fasad i taget utan uppehåll; trä målas när det är torrt och inte i stark sol."),
    ("Överlämning", "Vi går igenom resultatet med dig och skriver ner färgtyp och kulörer för framtida underhåll."),
  ],
  "rot_h2": "ROT-avdrag för målning i Täby",
  "rot": [
    "För en villa eller ett radhus som du äger räknar " + X(U_ROTLISTA, "Skatteverket") + " målning av "
    "fasad, fönster, väggar, tak, golv och element samt tapetsering som rotarbete. Avdraget är 30 procent av "
    "arbetskostnaden, högst 50 000 kronor per person och år, och ROT plus RUT får vara högst 75 000 kronor. "
    "Vi drar det direkt på fakturan.",
    "I en bostadsrätt ger bara arbete inne i lägenheten avdrag, till exempel innerdörrar och insidan av "
    "fönster. Staket och murar ger inget avdrag.",
  ],
  "price_h2": "Vad styr priset för målning i Täby?",
  "price": [
    "Metoden styr mest. En kalkputsad fasad kräver flera strykningar och ett arbetslag som hinner en hel yta "
    "i taget, en trävilla med vita foder och spröjsade bågar tar tid i detaljerna, och ett kedjehus med "
    "tegel har mindre yta att måla. Därtill kommer hur mycket som behöver lagas.",
    "Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag innan vi bokar in arbetet.",
  ],
  "faq": [
    ("Kan en kalkputsad villa i Näsbypark målas med vanlig fasadfärg?",
     "Det går tekniskt med vissa färger, men Riksantikvarieämbetet råder att hålla sig till samma färgtyp som "
     "tidigare. Kalkfärg på kalkputs släpper igenom fukt och är enkel att måla om nästa gång. Vi tar reda på "
     "vad som sitter på putsen innan vi föreslår något."),
    ("Vi bor i ett kedjehus från 1970-talet i Täby – får vi måla den bruna panelen vit?",
     "Utanför särskilt värdefulla områden krävs normalt inget lov. Är kvarteret beskrivet i Kulturmiljöer i "
     "Täby rekommenderar kommunen ändå originalkulörerna, och i en enhetlig länga bör grannarna vara med på "
     "beslutet."),
    ("Ska vita foder och knutar målas samtidigt som den faluröda panelen?",
     "Oftast ja, eftersom ställningen redan står. Rödfärgen och täckfärgen på foderna är olika färgtyper "
     "och stryks var för sig."),
    ("Gäller något särskilt för de nya husen vid Näsby slott?",
     "Ja, för den nyare bebyggelsen vid slottet finns ett färgprogram som ska följas vid underhåll och "
     "ommålning. Vi stämmer av programmet innan arbetet börjar."),
    ("Varför målas en putsfasad med kalkfärg bara en strykning om dagen?",
     "Det är Riksantikvarieämbetets råd för kalkfärg: ett skikt per dag, på en puts som är lagom fuktig, och "
     "ofta flera strykningar. Därför tar en kalkad fasad längre tid än en målad träfasad av samma storlek."),
  ],
  "sources": [
    ("Täby kommun – Kulturmiljöer i Täby, antagen 2024 (pdf)", U_TBK),
    ("Täby kommun – Fasadändring", U_TBF),
    S_BOV, S_RAA, S_ROT, S_ROTLISTA,
  ],
  "cta": ("Målare till ditt hus i Täby", "Boka ett gratis platsbesök så bedömer vi fasaden och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Faluröd trävilla med vita foder och spröjsade fönster i Täby",
     "freshly painted falu red early 1900s Swedish wooden villa with horizontal tongue and groove panel, white window trim, white corner boards and small-paned windows, glazed veranda, birch trees, Taby kyrkby, summer"),
    ("Vitt kalkputsad 1920-talsvilla med gröna fönster i Täby",
     "1920s Swedish classicist villa with freshly lime-washed white rendered facade and dark green window frames, slightly flared red tile roof, garden with lilac and lawn, Nasbypark Taby"),
  ],
}

PAGES_TJ = {
  "malare-huddinge.html": HUDDINGE,
  "malare-norrtalje.html": NORRTALJE,
  "malare-nacka.html": NACKA,
  "malare-taby.html": TABY,
}
