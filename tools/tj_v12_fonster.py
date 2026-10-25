# -*- coding: utf-8 -*-
"""Fönsterbyte – ortsidor v12: Botkyrka, Haninge, Tyresö, Värmdö, Sigtuna, Upplands Väsby (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25: Botkyrka kommun
(Kulturmiljöprogram – Uttran villaområde med "Tidstypiska byggnadsdetaljer" och riktlinjerna; Fasadändring med
webbkartans lager), Boverket (PBL kunskapsbanken: Fönsterbyten – bygglovsplikt och förvanskningsförbudet,
MÖD 2019:25 och P 3853–15; rättsfall: Bygglov för byte av fönster för att klara viss ljudnivå; Risker med fönster
och dörrar; energiguiden: Energirenovera eller byta fönster och dörrar), Haninge kommun (Kulturmiljöinventering
Kolbotten Dalarö 2016; Fasadändring), Stockholms läns museum (Solberga/del av Raksta, rapport 2008:31 –
Strömstugan och Forsby), Riksantikvarieämbetet (Fönster – historik och råd vid renovering, RAÄ 1988:1),
Tyresö kommun (Förändringar i PBL från 1 december 2025), Värmdö kommun (Byggnadsinventering Gustavsberg,
Sweco 2018 – Höjdhagen och Villagatan/Kvarntorpsvägen; Bygga i kulturmiljöer; Bygglov vid fasadändring),
Swedavia (Stockholm Arlanda Airport – För grannar: villkor 23, gränskurvor, bullerisolering, inventering,
in- och utflygningsregler), Sigtuna kommun (Bygga i kulturmiljö), Upplands Väsby kommun (Buller; Fasadändring;
Kulturhistoriska byggnader, kulturmiljöer), Folkhälsomyndigheten (FoHMFS 2014:13) och Skatteverket (Så fungerar
rotavdraget; Ger arbetet rätt till rotavdrag? – privat, småhus och bostadsrätt).
Strukna (ej verifierade): att särskilda adresser/områden i Sigtuna eller Väsby ligger inom Swedavias
bullerisoleringsområden i dag; vilka hus som faktiskt bullerisolerades 1993–2013; att Trafikverket ger bidrag
till fönster i Väsby (kommunen säger bara att man kan vända sig till vägansvarig om bullerskydd till fasaden);
BBR:s U-värdeskrav vid ändring (bara sekundärkällor hittade); Tyresö kulturmiljöprogrammets innehåll (bara
omnämnt i rapporten); Haninges Dalarö-detaljplaner om fönster (Dalarö 4:4 beskriver bara ett enskilt hus);
fönstertyper i 1920-talets kataloghus i Botkyrka (texten avbruten i pdf:en); Värmdös kulturmiljöprogram
(boken Skärgårdsbygd – ej öppnad); alla priser och bidragsbelopp. Inga garantier, omdömen, egna uppdrag eller cert.
Kritikpass 2026-10-25 (även huvudkritik): Haninge-ingressens 'fönstren har ofta bytts flera gånger' struket (ej i inventeringen),
bildalt varmdo-2 omskriven efter omgjord bild.
 varje tal och regel kontrollerad mot källtexten – FBN 55/70/80 dB(A), 150 nätter,
3 rörelser, mål 30/45 dB(A), 250 000 rörelser, +5/+10 dB(A), 750 m och 3 050 m, bana tre efter kl. 22,
FoHMFS 30/45 dB, patent 1889, Höjdhagen 1938–45 och 69 hus, Kullenhusen 1884–89, styckningsplan 1932 och
92 tomter, MÖD-målnummer. Struket i kritikpasset: "Swedavia betalar fönstren" (sidan säger att Swedavia
anlitar entreprenör och tecknar avtal – inte vem som betalar vad i detalj), "kopplade bågar kom till förorterna
på 1930-talet" (RAÄ säger bara att okopplade var vanliga i förorternas egnahem ännu vid slutet av 20-talet),
"Botkyrka kräver lov för perspektivfönster" (ingen sådan regel), "funkisfönster saknade foder" (programmets
bildtext "utan spröjs och fönsterfoder" är tvetydig – bara "utan spröjs" kvar), "fyra kartlager" (kommunen listar
fem; tre fönsterrelevanta nämns). Haninges inventering omskriven: styckningsplanen 1932/92 tomter gäller Västra
Vadviken, ritningar på monteringsfärdiga hus gäller Kolbotten. Bildalt justerade efter vad bilderna visar.
Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_FONSTER = ("Boverket – Energiguiden: Energirenovera eller byta fönster och dörrar",
               "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/fonster_dorrar/")
_BV_FUKT = ("Boverket – Risker med fönster och dörrar (fuktskador)",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/risker-fonster-dorrar/")
_BV_MOD = ("Boverket – PBL kunskapsbanken: Fönsterbyten – bygglovsplikt och förvanskningsförbudet",
           "https://www.boverket.se/sv/PBL-kunskapsbanken/teman/kulturvarden/kulturvarden-i-teori-och-praktik/rattsfall/fonsterbyten/")
_BV_LJUD = ("Boverket – Rättsfall: Bygglov för byte av fönster för att klara viss ljudnivå",
            "https://www.boverket.se/sv/samhallsplanering/arkitektur-och-gestaltad-livsmiljo/arbetssatt/arkitektur-och-pbl/rattsfall/en--och-tvabostadshus/byte-fonster/")
_RAA = ("Riksantikvarieämbetet – Fönster: historik och råd vid renovering (RAÄ 1988:1, pdf)",
        "https://www.raa.se/publicerat/9789172095892.pdf")
_SWEDAVIA = ("Swedavia – Stockholm Arlanda Airport: För grannar (buller, villkor och bullerisolering)",
             "https://www.swedavia.se/arlanda/grannar/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ BOTKYRKA
"fonsterbyte-botkyrka.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Botkyrka", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Botkyrka – fönster epok för epok i villorna",
  "description": "Fönsterbyte i Botkyrka: kulturmiljöprogrammets fönstertyper från småspröjs till perspektivfönster, domstolarnas syn på aluminium och kommunens webbkarta.",
  "h1": "Fönsterbyte i Botkyrka",
  "lead": "Botkyrkas villaområden byggdes under hela 1900-talet, och varje årtionde hade sina egna fönster. Det gör det lätt att välja fel modell när de gamla ska ersättas. Geal Entreprenad AB byter och renoverar fönster i Tullinge, Tumba, Uttran och övriga Botkyrka, utgår från husets egen tid och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Fönstertyper per epok i Botkyrkas villor.",
  "sections": [
    {"id": "epoker-botkyrka", "anchor": "Fönster per epok",
     "h2": "Sex sorters fönster i ett och samma villaområde",
     "paras": [
       "I kulturmiljöprogrammet beskriver Botkyrka kommun Uttran som ett område där villabyggandet går att följa från 1910-talet fram till 2010-talet. För att visa skillnaderna har programmet ritat upp tidstypiska byggnadsdetaljer för varje epok, och fönstren skiljer sig tydligt åt mellan dem. Samma bild hänvisar programmet till för Tullinge villaområde.",
       "Nationalromantikens villor från 1900- och 1910-talen har småspröjsade fönster med vita foder. Jugendhusen från samma tid har tvåluftsfönster där bara den övre delen är småspröjsad. Funktionalismen på 1930- och 1940-talen tog bort spröjsen helt, och programmet nämner även runda fönster som ett av funkisvillans drag.",
       "Även 1950-talets villor fick tvåluftsfönster utan spröjs, här tillsammans med fönsterfoder i tegel och snedställda burspråk. På 1960-talet kom helglasade perspektivfönster med vädringslucka, och 1970-talets villor i vitt mexitegel fick perspektivfönster helt utan foder. Programmet beskriver också femtiotalets stora perspektivfönster som typiska för perioden.",
     ],
     "aside": {"title": "Fönstren i programmet", "items": [
       "1900–1910: småspröjs och vita foder", "Jugend: spröjsad övre del",
       "1930–40: tvåluft utan spröjs", "1950: fönsterfoder i tegel",
       "1960: perspektivfönster med vädringslucka", "1970: perspektivfönster utan foder"]}},
    {"id": "riktlinje-botkyrka", "h2": "Kommunens riktlinje: ge fönstret husets egen tid",
     "paras": [
       "För både Uttran och Tullinge skriver kommunen att villor med bevarad ursprunglig karaktär ska värnas, och att fönster, fasader, tak, entrépartier och balkonger ska ges en tidstypisk utformning när huset ändras. Riktlinjen pekar alltså inte ut en viss fönstermodell för hela Botkyrka. Den säger att fönstret ska höra ihop med det årtionde huset byggdes.",
       "I praktiken går felet åt båda hållen. En funkisvilla kan förlora sin stramhet om den får spröjsade rutor som den inte hade från början, och en villa från 1910-talet blir platt om småspröjsen försvinner. På ett hus från 1960-talet är det perspektivfönstret med sin vädringslucka som bär fasaden, inte några detaljer i bågen.",
       "Därför börjar vårt besök med att bestämma husets epok och hur mycket som finns kvar av originalet. Har fönstren redan bytts en gång kan ett nytt byte vara ett tillfälle att komma närmare den ursprungliga indelningen. Ska fasaden kring fönstren målas samtidigt, läs om " + _L.format("malare-botkyrka.html", "målare i Botkyrka") + ".",
     ],
     "aside": None},
    {"id": "domar-botkyrka", "h2": "Aluminium, löstagbara spröjs och två olika domar",
     "paras": [
       "Boverket har sammanfattat flera domar om fönsterbyten. I ett vägledande avgörande från 2019 (MÖD 2019:25) gällde det två flerbostadshus i 20-talsklassicism där trä hade ersatts av aluminiumklätt trä, kulören ändrats, profilerna blivit kantigare, mittposterna grövre och de fasta spröjsen ersatts med löstagbara. Mark- och miljööverdomstolen ansåg att ändringen knappt märktes för den som passerar på gatan och att bygglov inte krävdes.",
       "Boverket påpekar samtidigt att domen inte betyder att fönsterbyten saknar lovplikt, bara att de här två bytena inte krävde lov. I ett tidigare mål om en villa från 1920-talet (P 3853–15) skulle sju fönster och en fönsterdörr ersättas med aluminiumklädda. Där bedömdes bytet strida mot förvanskningsförbudet och varsamhetskravet, eftersom fönstren med tidsenliga profiler skulle gå förlorade.",
       "Skillnaden ligger i hur värdefullt huset är och vad som faktiskt finns kvar av originalet. För ägaren är slutsatsen enkel: ju mer ursprungligt huset är, desto mer betyder material och profiler i det nya fönstret.",
     ],
     "aside": {"title": "Det domstolarna jämförde", "items": [
       "Trä eller aluminiumklätt trä", "Profilernas form",
       "Mittpostens bredd", "Fasta eller löstagbara spröjs"]}},
    {"id": "karta-botkyrka", "h2": "Kartlagren att titta i innan fönstren beställs",
     "paras": [
       "Ett nytt fönster räknas som en fasadändring, och för en- och tvåbostadshus är den normalt lovfri. Kommunen beskriver ändå en utökad lovplikt för byggnader och områden som omfattas av skyddsbestämmelser eller som är särskilt värdefulla utan att ha sådana bestämmelser.",
       "För att ta reda på om det gäller ditt hus hänvisar kommunen till webbkartan. Under fliken Bibliotek och kultur finns lagret Kulturmiljöprogram, under Bygga och bo lagret Detaljplaner och under Riksintressen lagret Kulturmiljövård. Därtill ska översiktsplanen och eventuella gestaltningsprogram för området kontrolleras.",
       "Vill du ha ett bindande besked kan du söka frivilligt bygglov. Byggnadsnämnden prövar då åtgärden och fattar ett formellt beslut, mot en bygglovsavgift. Ska takkupans fönster bytas i samma veva finns mer under " + _L.format("takrenovering-botkyrka.html", "takrenovering i Botkyrka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planeras fönsterbytet i Botkyrka",
  "steps": [
    ("Epok och skick", "Vi bestämmer husets byggår, vilka fönster som är original och hur de mår."),
    ("Webbkartan", "Kulturmiljöprogram, detaljplan och riksintressen kontrolleras för fastigheten."),
    ("Rätt modell", "Indelning, spröjs, foder och profiler väljs efter husets egen epok."),
    ("Kostnadsförslag", "Byte, renovering, glas, montage och bleck redovisas var för sig och skriftligt."),
    ("Montage", "Fönstren sätts in med drevning, tätning och nya smygar där det behövs."),
    ("Avslut", "Foder och bleck görs klart och vi går igenom varje fönster med dig."),
  ],
  "rot_h2": "ROT-avdrag för fönstren i Botkyrka",
  "rot": [
    "Skatteverket godkänner rotavdrag för att reparera eller byta ut fönster i ett småhus och för att byta fönsterbleck. Företaget får dra av högst 30 procent av arbetskostnaden, och avdraget är högst 50 000 kr per person och år, eller 75 000 kr sammanlagt med rutavdrag.",
    "Material och resor ger inget avdrag, och du ska äga huset medan arbetet görs. Vi drar avdraget på fakturan.",
  ],
  "price_h2": "Det här påverkar priset i Botkyrka",
  "price": [
    "Antal fönster, om spröjs och profiler ska anpassas till husets epok, om perspektivfönster ska tillverkas i stora format, hur mycket foder, smygar och bleck som ska göras om och om ett frivilligt bygglov ska sökas. Du får ett skriftligt kostnadsförslag efter ett kostnadsfritt besök.",
  ],
  "faq": [
    ("Vilka fönster hade en funkisvilla i Tullinge från början?",
     "Enligt Botkyrkas kulturmiljöprogram tvåluftsfönster utan spröjs, ibland kompletterade med runda fönster. Spröjs hör alltså inte till funkisvillans uttryck."),
    ("Får vi sätta in aluminiumklädda fönster på en villa från 1920-talet?",
     "Det beror på hur värdefull villan är. I mål P 3853–15 nekades bygglov för aluminiumklädda fönster på en 1920-talsvilla, eftersom de tidsenliga profilerna skulle gå förlorade."),
    ("Är löstagbara spröjs godtagbara i stället för fasta?",
     "I MÖD 2019:25 godtogs ett byte där fasta spröjs blivit löstagbara, men huset var inte en villa och domen gäller just de förutsättningarna. På ett välbevarat hus väger fasta spröjs tyngre."),
    ("Var i Botkyrkas webbkarta ser man om huset är kulturhistoriskt värdefullt?",
     "Kommunen pekar på lagret Kulturmiljöprogram under fliken Bibliotek och kultur, Detaljplaner under Bygga och bo och Kulturmiljövård under Riksintressen."),
    ("Har perspektivfönster från 1960-talet något bevarandevärde?",
     "Kulturmiljöprogrammet räknar helglasade perspektivfönster med vädringslucka till 1960-talsvillans tidstypiska detaljer. På en välbevarad villa från den tiden är de därför värda att ta hänsyn till."),
  ],
  "sources": [
    ("Botkyrka kommun – Kulturmiljöprogram (pdf)",
     "https://www.botkyrka.se/download/18.1fbbaae6170bff9469deb7f/1602575505534/Kulturmilj%C3%B6program.pdf"),
    ("Botkyrka kommun – Fasadändring",
     "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/fasadandring"),
    _BV_MOD, _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren i Botkyrka bytas?", "Boka ett gratis platsbesök så tar vi reda på husets epok och vilka fönster som passar."),
  "img": [
    ("Villa i Botkyrka med gul tegelfasad och vita treluftsfönster utan spröjs",
     "1950s Swedish single-storey villa with yellow brick facade, white wooden casement windows with two large plain undivided glass panes each, absolutely no glazing bars and no muntins, windows framed by a brick soldier course, low-pitched gable roof with dark concrete tiles, mature birch and pine trees, lawn, quiet suburban street in Tullinge Botkyrka, calm daylight, empty scene"),
    ("Vitt spröjsat tvåluftsfönster med överluft i en ljusgul putsad fasad",
     "close-up of a white painted wooden two-sash window whose upper part is divided by glazing bars into small panes while the lower panes are plain, set in a smooth light yellow plastered wall of an early 1900s Swedish villa, soft daylight, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HANINGE
"fonsterbyte-haninge.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Haninge", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Haninge – sportstugor och skärgårdsväder",
  "description": "Fönsterbyte i Haninge: sportstugornas enluftsfönster och fönsterluckor vid Dalarö, regn och vind mot fönstren i skärgården, bleck, kondens och lov.",
  "h1": "Fönsterbyte i Haninge",
  "lead": "I Kolbotten och Västra Vadviken på Dalarö står hus som en gång byggdes som sportstugor och som sedan ofta har byggts till i samma stil. I lägen mot vattnet får fönstren ta mycket regn och blåst. Geal Entreprenad AB byter och renoverar fönster på Dalarö, i Västerhaninge, Handen och resten av kommunen och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Sportstugor och fönster i skärgårdsväder.",
  "sections": [
    {"id": "sportstugor-haninge", "anchor": "Sportstugornas fönster",
     "h2": "Kolbotten och Vadviken: stugorna från 1930- till 1950-talet",
     "paras": [
       "Inför en ny detaljplan gjordes en kulturmiljöinventering av Kolbotten och Västra Vadviken väster om Dalarö, som finns på Haninge kommuns webbplats. Västra Vadviken styckades enligt en plan från 1932 i 92 tomter, och enligt inventeringens källor byggdes där främst små sportstugor, sällan villor. För Kolbotten finns i bygglovsarkivet flera ritningar på monteringsfärdiga hus från svenska trähusfabrikanter.",
       "Den första generationens sportstugor i landet var enligt inventeringen ofta allmogeinspirerade, med tjärade eller rödfärgade fasader och småspröjsade fönster. Stugorna i Kolbotten och Vadviken har däremot en mer modern prägel. Fönstren har oftast en eller två lufter utan spröjs, fönsterluckor med jalusier är vanliga och många hus har figursågade foder.",
       "Inventeringen konstaterar också att bebyggelsen är väl omhändertagen och flitigt underhållen. Det har lett till att bara ett fåtal byggnader har kvar sin ursprungliga form, fasadbeklädnad och sina fönstersnickerier.",
     ],
     "aside": {"title": "Sportstugans fönster", "items": [
       "En eller två lufter", "Oftast utan spröjs",
       "Fönsterluckor med jalusier", "Figursågade foder"]}},
    {"id": "omgangar-haninge", "h2": "Ett hus som byggts till i flera omgångar",
     "paras": [
       "Ett vanligt mönster i den här typen av områden är enligt inventeringen att först bygga en mindre stuga, för att sedan bygga till, bygga en större bredvid eller riva den gamla. Huvudbyggnaden har ofta byggts till i samma stil som ursprunget. Resultatet blir hus där varje del har fönster från sin egen tid.",
       "När inventeringen pekar ut vilka byggnader som har kulturhistoriskt värde är ett av kriterierna att de har ursprungliga fönster, dörrar och andra yttre detaljer. Kriteriet godtar också att delarna har bytts mot nya med ursprungligt eller tidstypiskt utseende. Det är en bra utgångspunkt även för ett hus som inte är utpekat.",
       "För ett fönsterbyte betyder det att vi först sorterar fönstren efter husets delar. De äldsta kan ofta renoveras, medan senare tillbyggnaders fönster kan bytas till en modell med samma luftindelning och foderform som stugan. Gäller bytet ett hus som ska användas året runt, se även " + _L.format("byggforetag-haninge.html", "byggföretag i Haninge") + ".",
     ],
     "aside": None},
    {"id": "vader-haninge", "h2": "Regn, vind och vatten kring fönstret i skärgården",
     "paras": [
       "Boverket nämner förväntade regnmängder och vindförhållanden bland de faktorer som påverkar sannolikheten för fuktskador på fönster. Till listan hör också en bruten tvåstegstätning vid monteringen, bleck som lutar fel eller inte sluter tätt mot väggen och fönstrets förmåga att leda bort och torka ut vatten. Energiguiden tillägger att gamla tätningar ofta släpper in vatten under fönstren i lägen med slagregn.",
       "Risken minskar enligt Boverket när fönstret sitter väderskyddat, till exempel en bit in i väggen eller under en utskjutande takfot. Sitter det för långt in kan det i stället bli en köldbrygga. På en gavel utan takutsprång kan ett skärmtak ge skydd, och under fönsterblecket bör det finnas en dränerande och ventilerande spalt.",
       "Kondens på utsidan av ett nytt, välisolerat fönster är normalt ingen skada. I kopplade bågar kan fuktig inomhusluft däremot kondensera på insidan av det kalla yttre glaset, och enligt Boverket ger kondens mellan rutorna fuktskador framför allt på bågarna. Ska fasaden runt fönstren ses över samtidigt, läs om " + _L.format("fasadrenovering-haninge.html", "fasadrenovering i Haninge") + ".",
     ],
     "aside": {"title": "Vi kontrollerar", "items": [
       "Blecket: lutning och anslutning", "Tätningen mellan karm och vägg",
       "Spalten under blecket", "Fukt i smyg och bröstning"]}},
    {"id": "lov-haninge", "h2": "Lov och handlingar i Haninge",
     "paras": [
       "Haninge kommun räknar nya fönster eller dörrar som en fasadändring. Bygglov behövs när byggnaden eller området är särskilt värdefullt, och för andra byggnader än en- och tvåbostadshus när ändringen inom detaljplan görs mot en allmän plats. Varsamhetskravet gäller oavsett, och nya åtgärder ska anpassas både till huset och till miljön runt omkring.",
       "Krävs lov vill kommunen ha en situationsplan på en tomtkarta, fotografier av byggnaden och ett förslag till kontrollplan. Den som bygger ansvarar för att göra en riskanalys och för att kontrollplanen följs. Bygglov och startbesked ska finnas innan arbetet börjar.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så byter vi fönster i Haninge",
  "steps": [
    ("Platsbesök", "Fönstren sorteras efter husets delar och skick, och väderutsatta sidor noteras."),
    ("Fukt i väggen", "Smygar, bröstningar och bleck kontrolleras för vatten som läckt in."),
    ("Lovfrågan", "Vi ser efter om huset eller området är särskilt värdefullt enligt kommunens underlag."),
    ("Kostnadsförslag", "Renovering, nya fönster, bleck och luckor står var för sig i ett skriftligt förslag."),
    ("Montage", "Fönstren monteras med tvåstegstätning och bleck som leder vattnet ut från väggen."),
    ("Genomgång", "Vi visar hur luckor, bågar och tätningslister sköts i ett utsatt läge."),
  ],
  "rot_h2": "Rotavdrag för fönster och bleck i Haninge",
  "rot": [
    "Att byta fönsterbleck och att reparera eller byta ut fönster i ett småhus är rotarbete enligt Skatteverket. Avdraget är upp till 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag.",
    "Myggnät och solfilm ger inget avdrag, och inte heller material eller resor. Avdraget görs direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Haninge?",
  "price": [
    "Hur många fönster som kan renoveras, om fönsterluckor och figursågade foder ska behållas eller göras nya, hur mycket fuktskadat trä i smygar och bröstningar som ska bytas, om nya bleck behövs och hur huset nås. Kostnadsförslaget får du skriftligt efter besöket, som är gratis.",
  ],
  "faq": [
    ("Hade sportstugorna vid Dalarö spröjsade fönster?",
     "De allmogeinspirerade stugorna hade ofta småspröjsade fönster, men i Kolbotten och Vadviken har stugorna enligt kommunens inventering mest en- eller tvåluftsfönster utan spröjs."),
    ("Kan fönsterluckorna med jalusier sitta kvar när fönstren byts?",
     "Ofta ja, om det nya fönstret får samma mått och placering i väggen. Jalusiluckor räknas i inventeringen till stugornas karaktär, så de är värda att spara."),
    ("Varför ruttnar smygen under fönstret i vårt hus vid vattnet?",
     "Boverket nämner regn och vind, bleck som lutar fel och bruten tätning som vanliga orsaker. Vi tar bort blecket och undersöker väggen innan nytt fönster sätts in."),
    ("Är det fel på nya fönster som är immiga på utsidan på morgonen?",
     "Nej. Boverket skriver att utvändig kondens på välisolerade fönster normalt inte skadar fönstret. Den försvinner oftast efter ett par timmar."),
    ("Vilka handlingar vill Haninge kommun ha om fönsterbytet kräver lov?",
     "En situationsplan på tomtkarta, fotografier av byggnaden och ett förslag till kontrollplan, utöver själva ansökan."),
  ],
  "sources": [
    ("Haninge kommun – Kulturmiljöinventering Kolbotten, Dalarö (pdf)",
     "https://www.haninge.se/siteassets/bygga-bo-och-miljo/oversiktsplanering-och-detaljplaner/detaljplaner/kust-och-skargard/dalaro-etapp-2-kolbotten/kulturmiljoinventering.pdf"),
    ("Haninge kommun – Fasadändring",
     "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/fasadandring/"),
    _BV_FUKT, _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Behöver fönstren i Haninge bytas eller lagas?", "Boka ett gratis platsbesök så går vi igenom fönster, bleck och väggar."),
  "img": [
    ("Mörkbetsad sportstuga i Haninge med vita fönster och fönsterluckor bland tallar och berghällar",
     "small 1940s Swedish summer cabin seen from the side, dark brown stained horizontal wooden cladding, two white windows with plain clear glass and dark blue trim, white wooden window shutters with horizontal louvres folded open beside each window, low-pitched gable roof with black roofing felt, granite rocks and tall pine trees, glimpse of a calm archipelago bay, Dalarö Haninge, late afternoon light, empty scene, clean image without any watermark or signature"),
    ("Närbild på ett vitt träfönster med fönsterbleck på en rödmålad panelvägg i regn",
     "close-up of the lower part of a white painted wooden window on a red painted wooden panel wall, dark grey metal window sill flashing sloping outward with raindrops, wet wood after rain, overcast daylight"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TYRESÖ
"fonsterbyte-tyreso.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Tyresö", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Tyresö – gamla bågar, beslag och lov",
  "description": "Fönsterbyte i Tyresö: vad museets inventering visar om fönster och beslag i äldre hus, kopplade och okopplade bågar, besiktning före byte och lovplikten.",
  "h1": "Fönsterbyte i Tyresö",
  "lead": "I Tyresös äldre hus är det ofta beslagen och bågarnas konstruktion som berättar mest om fönstrens ålder. Det är detaljer som lätt försvinner vid ett snabbt byte. Geal Entreprenad AB byter och renoverar fönster i Tyresö strand, Trollbäcken, Brevik och övriga kommunen, bedömer varje fönster för sig och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Gamla bågar och beslag i Tyresö.",
  "sections": [
    {"id": "solberga-tyreso", "anchor": "Fönstren i inventeringen",
     "h2": "Hörnjärn och uppställningsbeslag i Solberga och Raksta",
     "paras": [
       "Inför en detaljplan inventerade Stockholms läns museum 2008 bebyggelsen i Solberga och delar av Raksta. Rapporten beskriver fönstren hus för hus. I Strömstugan vid Follbrinksströmmen har fönstren tre rutor per båge med pressade hörnjärn, en typ som enligt rapporten var vanlig under 1900-talets första hälft. Bågarna är kopplade och har invändigt raka uppställningsbeslag av 1800-talstyp.",
       "Samma stuga visar hur ett hus byggs på i omgångar. De tillbyggda delarna har moderna enrutsfönster och en modern småspröjsad båge, och i vindsfönstren sitter en båge med två rutor där ett av fönstren har gångjärnsbeslag av sen 1800-talstyp.",
       "I huset Forsby har fönstren sex rutor, tre per båge. Snickerierna är i huvudsak nytillverkade, men ett antal äldre bågar har kvar gångjärnsbeslag från sent 1800-tal. Rapporten räknar just de bågarna, tillsammans med kakelugn, rörspis och äldre snickerier, till det som tydliggör husets byggnadshistoria.",
     ],
     "aside": {"title": "Ur museets rapport", "items": [
       "Tre rutor per båge", "Pressade hörnjärn",
       "Raka uppställningsbeslag", "Gångjärn av sen 1800-talstyp"]}},
    {"id": "kopplade-tyreso", "h2": "Kopplade eller okopplade bågar",
     "paras": [
       "Riksantikvarieämbetets skrift om fönster beskriver hur de kopplade bågarna kom in i byggandet. C A Flodquist och C G Hallberg fick 1889 patent på ett fönster där två bågar med varsitt glas hålls ihop med gångjärn och hakar, så att innanfönster inte längre behövdes. Från sekelskiftet blev de kopplade, inåtgående bågarna allt vanligare i städerna.",
       "När de kopplade bågarna öppnas inåt försvinner mittposten, och den inre bågen bär den yttre. Därför gjordes innerbågen kraftigare. Enligt skriften var de traditionella okopplade fönstren ändå vanliga i förorternas egnahemsbebyggelse ännu i slutet av 1920-talet, och med funktionalismen försvann spröjsen ur de kopplade bågarna.",
       "För ett hus i Tyresö betyder det att två fönster som ser lika ut utifrån kan vara byggda på helt olika sätt. Om innerbågen ska få ett energiglas är det just den bärande bågen som får mer tyngd, och Boverket påminner om att båge, gångjärn och beslag måste klara det.",
     ],
     "aside": None},
    {"id": "beslag-tyreso", "h2": "Beslagen avslöjar fönstrets ålder",
     "paras": [
       "Riksantikvarieämbetet förklarar att fasta fönster egentligen inte behövde några beslag. När bågarna blev öppningsbara måste de förstärkas med hörnjärn och förses med gångjärn samt stängnings- och uppställningsbeslag. I början var beslagen smidda, och hörnjärnet och gångjärnets övre del gjordes ofta i ett stycke.",
       "Vid mitten av 1800-talet kom hörnjärn som stansades ur plåt, och senare även gjutna och formpressade beslag. De kopplade fönstren förde med sig koppelhakar mellan ytter- och innerbåge, och fönster utan mittpost fick en spanjolettstång som stängningsbeslag.",
       "När vi renoverar bågar tar vi därför vara på beslagen, rengör dem och sätter tillbaka dem. Byts ett fönster helt kan de gamla beslagen ofta sparas till andra bågar i huset. Ska även fasaden runt fönstren lagas, läs om " + _L.format("fasadrenovering-tyreso.html", "fasadrenovering i Tyresö") + ".",
     ],
     "aside": {"title": "Beslag i tidsordning", "items": [
       "Smidda hörnjärn och gångjärn", "Stansade hörnjärn i plåt",
       "Gjutna och formpressade beslag", "Koppelhakar och spanjolett"]}},
    {"id": "besiktning-tyreso", "h2": "Besiktning först – och lov i värdefulla miljöer",
     "paras": [
       "Riksantikvarieämbetet råder att börja med en systematisk besiktning av varje fönster när det är oklart om de behöver vanligt underhåll eller större reparationer. Utan besiktning är det enligt skriften för lätt att döma ut fönster som går att bevara. Det är oftast bottenstyckena i karm och båge som skadas, och ofta räcker det att byta de skadade partierna.",
       "Tyresö kommun skriver att nya fönster på ett en- eller tvåbostadshus inte kräver bygglov, men att ändringen ska göras varsamt och anpassas till byggnadens värden. Lov krävs om fastigheten ligger i ett kulturhistoriskt särskilt värdefullt område eller om byggnaden själv är särskilt värdefull. Kommunen påpekar också att uppdaterade underlag inte finns för alla områden, och erbjuder rådgivning och frivilligt bygglov.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går fönsterarbetet i Tyresö till",
  "steps": [
    ("Besiktning", "Varje fönster bedöms för sig: bottenstycken, kitt, färg, beslag och glas."),
    ("Konstruktion", "Vi noterar om bågarna är kopplade eller okopplade och hur de öppnas."),
    ("Förslag per fönster", "Du får veta vilka fönster som kan lagas, kompletteras eller behöver bytas."),
    ("Kostnadsförslag", "Lagning, nya delar, energiglas och nya fönster redovisas skriftligt och separat."),
    ("Arbetet", "Skadade partier byts, beslag rengörs och sätts tillbaka, nya fönster drevas och tätas."),
    ("Genomgång", "Vi går igenom fönstren med dig och visar hur kitt och färg följs upp."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Tyresö",
  "rot": [
    "Skatteverket räknar både att reparera och att byta ut fönster i ett småhus som rotarbete, liksom att måla fönster. Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kr per person och år, och tillsammans med rutavdrag högst 75 000 kr.",
    "Glasarbeten som görs i företagets egna lokaler ger inget avdrag, och inte heller material. Vi drar avdraget på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Tyresö?",
  "price": [
    "Hur många bågar som kan lagas, hur stora delar av bottenstyckena som måste bytas, om beslagen ska rengöras och flyttas, om innerbågen ska få energiglas och hur många fönster som behöver ersättas helt. Efter ett gratis platsbesök får du förslaget skriftligt.",
  ],
  "faq": [
    ("Hur ser man om ett fönster i Tyresö har kopplade bågar?",
     "Öppna fönstret. Följer ytter- och innerbåge med varandra och hålls ihop med hakar är de kopplade. Okopplade bågar öppnas var för sig."),
    ("Vad är pressade hörnjärn?",
     "Vinkelbeslag som förstärker bågens hörn. Stockholms läns museum beskriver dem som vanliga under 1900-talets första hälft, och Riksantikvarieämbetet att stansade hörnjärn kom vid mitten av 1800-talet."),
    ("Går det att spara de gamla beslagen när fönstret byts?",
     "Ofta. Beslagen kan rengöras och sättas på renoverade bågar i en annan del av huset, så att de inte försvinner helt."),
    ("Klarar en gammal kopplad båge ett energiglas på insidan?",
     "Det beror på bågens dimensioner och skick. Innerbågen bär den yttre, och Boverket påminner om att båge, gångjärn och beslag måste klara den extra tyngden."),
    ("Kräver Tyresö kommun lov för nya fönster i ett äldre torp?",
     "Inte för ett en- eller tvåbostadshus i allmänhet. Lov krävs om torpet eller området är kulturhistoriskt särskilt värdefullt, och kommunen erbjuder rådgivning om du är osäker."),
  ],
  "sources": [
    ("Stockholms läns museum – Solberga/del av Raksta, kulturmiljöunderlag, rapport 2008:31 (pdf)",
     "https://insynsverige.se/documentHandler.ashx?did=20437"),
    _RAA,
    ("Tyresö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
     "https://www.tyreso.se/boende--miljo/bygga/bygga-riva-eller-andra/forandringar-i-plan--och-bygglagen-fran-1-december-2025.html"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Funderar ni på att byta fönstren i Tyresö?", "Boka ett gratis platsbesök så besiktigar vi fönstren ett och ett."),
  "img": [
    ("Rödfärgad timmerstuga i Tyresö med vita sexrutiga fönster och tegeltak vid en skogsbäck",
     "small old Swedish falu red timber cottage with white corner boards, white wooden windows with three panes in each sash, red single-curved clay tile gable roof, natural stone foundation, standing among spruce and birch trees beside a small forest stream, Tyresö, calm daylight, empty scene"),
    ("Närbild på en äldre vitmålad fönsterbåge med gångjärn och flagnande färg",
     "straight-on close-up of the lower outer corner of an old white painted wooden casement window sash with a flat L-shaped metal corner plate screwed onto the face of the sash corner and an old metal butt hinge on the frame beside it, small part of old slightly wavy glass with linseed putty, worn flaking white paint, soft daylight, no hands"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VÄRMDÖ
"fonsterbyte-varmdo.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Värmdö", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Värmdö – Gustavsbergs hus och fönster",
  "description": "Fönsterbyte i Värmdö: bevarandevärda fönster i Höjdhagen och längs Villagatan i Gustavsberg, husens klassning, lov i kulturmiljöer och kommunantikvarien.",
  "h1": "Fönsterbyte i Värmdö",
  "lead": "I Gustavsberg har kommunen gått igenom husen inom riksintresset ett för ett och skrivit ner vilka detaljer som ska bevaras. Fönstren finns med på nästan varje lista. Geal Entreprenad AB byter och renoverar fönster i Gustavsberg, Hemmesta, Ingarö och övriga Värmdö och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Gustavsbergs bevarandevärda fönster.",
  "sections": [
    {"id": "inventering-varmdo", "anchor": "Inventeringen av Gustavsberg",
     "h2": "Varje hus i riksintresset har sin egen lista",
     "paras": [
       "På uppdrag av Värmdö kommun gjorde Sweco Architects 2018 en byggnadsinventering inom riksintresset för kulturmiljövården i Gustavsberg. Varje byggnad har beskrivits, värderats och klassats i en tregradig skala med färgerna blått, grönt och gult, från mycket högt till visst kulturhistoriskt värde. För varje hus finns en lista med rubriken karaktär och bevarandevärda detaljer.",
       "Enligt inventeringen är det de listade egenskaperna som ska respekteras för att underhåll och ändringar ska bli varsamma. Den påpekar också att varsamhetskravet gäller all bebyggelse, och att en ovarsam förändring av ett hus med visst kulturhistoriskt värde kan få lika stora konsekvenser som för ett hus med högt värde.",
       "Fönstren återkommer på listorna i många former: fönstersättning och fönsterstorlek, enluftsfönster med smalt vädringsfönster och pivåfönster, tvåluftsfönster med tre rutor i varje luft och ursprungliga bågar i en bestämd kulör. Innan vi föreslår något tar vi därför fram listan för just ditt hus.",
     ],
     "aside": {"title": "Klassningen i Gustavsberg", "items": [
       "Blått: mycket högt värde", "Grönt: högt värde",
       "Gult: visst värde", "Lista per hus: bevarandevärda detaljer"]}},
    {"id": "hojdhagen", "h2": "Höjdhagen: smäckra bågar och grönmålade källarfönster",
     "paras": [
       "Höjdhagen ritades av Olof Thunström och var det första nyproducerade bostadsområdet i Kooperativa förbundets regi. Mellan 1938 och 1945 uppfördes här 69 friliggande enfamiljshus för de anställda vid fabriken, de så kallade vinkelbodarna. Inventeringen beskriver husen med rödmålad locklistpanel, smäckra fönsterbågar, smala fönsterfoder och ett mycket flackt sadeltak.",
       "För husen som har klassats står fönster, dörrar och skärmtak som är ursprungliga för byggnaden bland de bevarandevärda detaljerna, liksom färgsättningen med faluröd fasad, vitmålade fönster och takbrädor och grönmålade källarfönster. Inventeringen nämner också att Thunström 1960 ritade en tillbyggnad på norra vinkelarmen och att flera hus senare har byggts till på det sättet.",
       "I ett sådant hus är bågarnas smala dimensioner en stor del av uttrycket. Ett nytt fönster med grövre profiler skulle märkas direkt, och Boverket påminner om att grövre snickerier även släpper in mindre dagsljus. Ska panel och knutar målas samtidigt, se " + _L.format("malare-varmdo.html", "målare på Värmdö") + ".",
     ],
     "aside": None},
    {"id": "villagatan", "h2": "Villagatan och Kvarntorpsvägen: sex rutor i varje luft",
     "paras": [
       "Längs Kvarntorpsvägen står tre så kallade Kullenhus i gult tegel från 1884–1889. Bland deras bevarandevärda detaljer listar inventeringen smala stående fönster med tre respektive sex rutor i varje luft och fönsteröverstycken med stående tegel. Inventeringen noterar att husen vid den senaste renoveringen har fått tillbaka spröjsade fönster.",
       "De faluröda fyrfamiljshusen från 1907–1908, ritade av Knut Perno Peterson, har fönster med spröjs bland sina bevarandevärda detaljer, och vita snickerier mot den röda panelen. Utmed Villagatan beskriver inventeringen också en variant från 1909–1911 med två större takkupor och stora spröjsade fönster som ger ljus åt övervåningen.",
       "Exemplet med Kullenhusen visar att ett fönsterbyte också kan gå åt rätt håll: när tidigare förenklingar rättas till kommer husets ursprungliga indelning tillbaka. Vi mäter upp spröjs och rutformat och beställer fönster efter dem.",
     ],
     "aside": {"title": "På listorna längs gatan", "items": [
       "Smala stående fönster", "Tre eller sex rutor per luft",
       "Överstycken i stående tegel", "Spröjs och vita snickerier"]}},
    {"id": "lov-varmdo", "h2": "Lov, anmälan och kommunantikvarien",
     "paras": [
       "Värmdö kommun kräver inget bygglov för nya fönster på en- och tvåbostadshus, men däremot för en fasadändring som nya fönster om fastigheten ligger i ett kulturhistoriskt särskilt värdefullt område eller byggnaden själv är särskilt värdefull. Kommunen räknar sina 14 riksintresseområden och omkring 55 utpekade kulturmiljöområden som särskilt värdefulla.",
       "Kommunen skriver också att underhåll av en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde kräver anmälan och startbesked. Bland det som ska anpassas till omgivningen nämns fönster och dörrar. Kommunantikvarien ger råd, och kommunen föreslår att du fotograferar fastigheten och mejlar innan arbetet planeras.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett fönsterbyte på Värmdö till",
  "steps": [
    ("Husets lista", "Vi tar fram inventeringens bevarandevärda detaljer eller detaljplanens bestämmelser."),
    ("Platsbesök", "Bågar, glas, kulörer och indelning mäts upp och fotograferas."),
    ("Kommunen", "Vid behov kontaktas kommunantikvarien, och lov eller anmälan förbereds."),
    ("Kostnadsförslag", "Renovering, nya fönster, glas och målning anges var för sig och skriftligt."),
    ("Utförande", "Bågar lagas eller nya fönster monteras med samma indelning och kulör."),
    ("Genomgång", "Vi går igenom resultatet med dig och lämnar uppgifter för husets underhåll."),
  ],
  "rot_h2": "Rotavdrag för fönster på Värmdö",
  "rot": [
    "För ett småhus godkänner Skatteverket rotavdrag för att reparera eller byta ut fönster och för att måla dem. Avdraget motsvarar högst 30 procent av arbetskostnaden, med ett tak på 50 000 kr per person och år och 75 000 kr tillsammans med rutavdrag.",
    "Kostnader för material, resor och utrustning ingår inte, och du ska äga bostaden när arbetet görs. Avdraget dras direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Värmdö?",
  "price": [
    "Om fönstren ska renoveras eller tillverkas efter förlaga, hur många rutor och spröjs varje båge har, om ursprunglig kulör ska tas fram, om lov eller anmälan behöver förberedas och hur långt det är till huset. Platsbesöket är gratis och förslaget skriftligt.",
  ],
  "faq": [
    ("Vad betyder blå, grön och gul klassning i Gustavsbergsinventeringen?",
     "Det är en tregradig värdering av husens kulturhistoriska värde: blått mycket högt, grönt högt och gult visst värde. För varje hus listas dessutom de detaljer som ska bevaras."),
    ("Får vi byta fönstren i vår vinkelbod i Höjdhagen?",
     "Inventeringen räknar ursprungliga fönster till de bevarandevärda detaljerna, och Gustavsberg är riksintresse. Börja med att kontakta kommunen, eftersom lov krävs i särskilt värdefulla områden."),
    ("Vilken kulör ska källarfönstren ha i Höjdhagen?",
     "Enligt inventeringen hör grönmålade källarfönster till färgsättningen, tillsammans med faluröd fasad och vitmålade fönster och takbrädor."),
    ("Behövs anmälan för att renovera fönster på ett skyddat hus på Värmdö?",
     "Kommunen skriver att underhåll av en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde kräver anmälan och startbesked."),
    ("Hur når man kommunantikvarien på Värmdö?",
     "Kommunen anger mejladressen kommunantikvarien@varmdo.se och föreslår att du skickar foton på fastigheten och beskriver vad du vill göra."),
  ],
  "sources": [
    ("Värmdö kommun – Byggnadsinventering Gustavsberg, Sweco 2018 (pdf)",
     "https://www.varmdo.se/download/18.410d01c916f1aa3a48ee7cd/1576763774840/14.%20Byggnadsinventering%20Gustavsberg%202018-12-21%20-%20komprimerad.pdf"),
    ("Värmdö kommun – Bygga i kulturmiljöer",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/byggaikulturmiljoer.4.57b4a3ba16e6b961dbf10429.html"),
    ("Värmdö kommun – Bygglov vid fasadändring",
     "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/bygglovvidfasadandring.4.1a14d9c818e5a4c406a626d.html"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska fönstren i Gustavsberg eller på Värmdö bytas?", "Boka ett gratis platsbesök så går vi igenom husets fönster och vad som ska bevaras."),
  "img": [
    ("Faluröd vinkelbyggd villa i Värmdö med vita fönster bland stenblock och tallar",
     "small single-storey 1940s Swedish house shaped like an L with two wings meeting at a right angle, falu red vertical board-and-batten cladding, slender white wooden windows with narrow frames, very low-pitched roof covered with plain black bitumen roofing felt, thin white fascia, placed among low rounded grey granite rock slabs and Scots pines on gentle Swedish archipelago terrain, lawn without fence, Gustavsberg Värmdö, summer daylight, empty scene"),
    ("Gult tegelhus i två våningar med smala spröjsade fönster och rött tegeltak",
     "detached late 1800s two-storey Swedish workers house with light yellow brick facade on a gentle grassy slope with a few old deciduous trees and a gravel path, neighbouring wooden houses partly visible, tall narrow white wooden windows each sash divided into three small panes, straight lintels of vertically laid yellow bricks above the windows, black painted natural stone plinth, red clay tile gable roof with yellow brick chimney, no fence, Gustavsberg Värmdö, calm daylight, empty scene"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SIGTUNA
"fonsterbyte-sigtuna.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Sigtuna", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Sigtuna – Arlanda, bullerisolering och glas",
  "description": "Fönsterbyte i Sigtuna: Swedavias villkor för bullerisolering av bostäder kring Arlanda, hur husets ljudisolering räknas och råd för kulturmiljöer.",
  "h1": "Fönsterbyte i Sigtuna",
  "lead": "Arlanda ligger i Sigtuna kommun, och för många hus här är det fönstren som avgör hur mycket av flyget som hörs inomhus. Innan nya fönster beställs är det bra att veta vad Swedavias bullervillkor innebär. Geal Entreprenad AB byter och renoverar fönster i Märsta, Sigtuna stad, Rosersberg och resten av kommunen och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Arlanda, ljudisolering och fönster i Sigtuna.",
  "sections": [
    {"id": "villkor-sigtuna", "anchor": "Swedavias villkor",
     "h2": "Villkor 23 och de tre gränskurvorna",
     "paras": [
       "Arlandas miljötillstånd togs i anspråk 2016, och i villkor 23 beskrivs Swedavias skyldighet att vidta bullerskyddsåtgärder i bostadsbyggnader. Enligt Swedavia avses både permanentbostäder och fritidsbostäder. Krav på bullerskydd beslutades första gången av Koncessionsnämnden 1993, när bana 3 byggdes. Nya krav kom 1998 och 2003, och bullerisoleringsprogram genomfördes kring flygplatsen fram till 2013.",
       "Vilka bostäder som kan bli aktuella styrs av tre gränskurvor: en flygbullernivå, FBN, på 55 dB(A), en maximal ljudnivå nattetid på 70 dB(A) och en maximal ljudnivå dag- och kvällstid på 80 dB(A). Nattnivån ska överskridas minst tre gånger per natt under minst 150 nätter, och dagnivån regelbundet. Det räcker att huset omfattas av en av kurvorna.",
       "Målet inomhus är en FBN på 30 dB(A) och högst 45 dB(A) som maximal nivå nattetid. I FBN får varje start eller landning kvällstid ett tillägg på 5 dB(A) och nattetid på 10 dB(A). Områdena beräknas för 250 000 flygrörelser per år och räknas om varje år.",
     ],
     "aside": {"title": "Gränskurvorna", "items": [
       "FBN 55 dB(A)", "70 dB(A) max nattetid, 150 nätter",
       "80 dB(A) max dag och kväll", "Mål inne: FBN 30, max 45 dB(A)"]}},
    {"id": "akustiker-sigtuna", "h2": "Så räknas ljudisoleringen i ett hus",
     "paras": [
       "Swedavia anlitar oberoende akustiker som inventerar husen, för det mesta genom ett platsbesök inomhus. I områden med likadana hus kan ett referenshus användas för flera bostäder. Beräkningen följer standarden SS-EN 12354-3 och tar med fönster, friskluftsventiler, väggar och tak.",
       "Vid genomgången bedöms fönsterstorlek, fönstertyp, glastjocklek, tätningslisternas skick, väggtyp, takkonstruktion och rummens storlek. Eftersom ljudnivån kan skilja sig mellan rummen kan vissa rum behöva åtgärdas och andra inte. Behovet blir ett åtgärdsförslag som bifogas ett avtal mellan Swedavia och fastighetsägaren.",
       "Åtgärderna kan enligt Swedavia gå från tätning av lister och byte av glasrutor i befintliga fönster till helt nya fönster. Kostnaderna ska vara rimliga med hänsyn till bostadens standard och värde, och tidigare åtgärder och nedlagda kostnader på fastigheten räknas in.",
     ],
     "aside": None},
    {"id": "eget-byte-sigtuna", "h2": "Om du själv vill byta fönster nära flygplatsen",
     "paras": [
       "Planerar du ett eget fönsterbyte är det klokt att först fråga Swedavia om fastigheten ligger inom ett bullerisoleringsområde eller redan har åtgärdats. Har huset fått bullerisolering tidigare bör det nya fönstret inte vara sämre mot ljud än det som sitter där i dag. Ett fönster väljs då både efter U-värde och efter hur mycket ljud det dämpar.",
       "Boverket påpekar att olika glas och glaskombinationer ger olika bullerdämpning, solavskärmning och dagsljus. Eftersom Swedavias beräkning även tar med friskluftsventiler spelar tilluften roll: en spaltventil i bågen eller karmen är en öppning, och placeringen påverkar hur mycket som hörs i sovrummet.",
       "Tätningen mellan karm och vägg och listerna mellan båge och karm påverkar både ljud och värme. Vi drevar och tätar varje fönster och kontrollerar att bågarna sluter. Ska taket eller vindsbjälklaget också ses över, läs om " + _L.format("takrenovering-sigtuna.html", "takrenovering i Sigtuna") + ".",
     ],
     "aside": {"title": "Det som räknas in", "items": [
       "Fönstertyp och glastjocklek", "Tätningslisternas skick",
       "Friskluftsventiler", "Rummets storlek"]}},
    {"id": "kultur-sigtuna", "h2": "Fönster i Sigtunas kulturmiljöer",
     "paras": [
       "Sigtuna kommun skriver att utformningen av fönster, liksom fasader, tak och entréer, är viktig för en byggnads uttryck, och att ursprungliga material och detaljer bör bevaras eller ersättas med samma material om de måste bytas. För Sigtuna stad finns en bevarande- och förnyelseplan och för dalgången mellan Odensala och Hova särskilda riktlinjer.",
       "Är en byggnad eller ett område särskilt värdefullt kan lov krävas även för en fasadändring som annars är lovfri. Är du osäker kan du skicka in adressen, en beskrivning av vad du vill göra och foton på fastigheten från alla väderstreck, så gör kommunen en bedömning. Även hus som inte är utpekade i något program kan enligt kommunen kräva särskild hänsyn.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går fönsterbytet i Sigtuna till",
  "steps": [
    ("Före besöket", "Du tar reda på hos Swedavia om huset ingår i ett bullerisoleringsområde."),
    ("Platsbesök", "Vi går igenom fönster, glas, lister och ventiler rum för rum."),
    ("Glasval", "Ljud- och energiegenskaper vägs mot husets läge och karaktär."),
    ("Kostnadsförslag", "Fönster, glas, ventiler och montage specificeras i ett skriftligt förslag."),
    ("Montage", "Fönstren monteras med noggrann drevning och tätning runt hela karmen."),
    ("Kontroll", "Vi kontrollerar att bågarna sluter tätt och att ventilerna sitter rätt."),
  ],
  "rot_h2": "ROT-avdrag för fönster och ljudglas i Sigtuna",
  "rot": [
    "Skatteverket godkänner rotavdrag för att reparera eller byta ut fönster i ett småhus och för att montera bullerglas och isolerglas. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr sammanlagt med rutavdrag.",
    "Material, resor och utrustning ger inget avdrag. Vi gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr priset i Sigtuna?",
  "price": [
    "Antal fönster och rum, vilken ljudklass och vilket energiglas som väljs, om befintliga bågar kan få nytt glas i stället för att bytas, om friskluftsventiler ska flyttas eller bytas och hur mycket foder och bleck som ska göras om. Kostnadsförslaget kommer skriftligt efter ett gratis besök.",
  ],
  "faq": [
    ("Kan Swedavia bullerisolera vårt hus i Sigtuna?",
     "Det beror på om huset ligger inom någon av villkorets tre gränskurvor och om målnivåerna inomhus redan klaras. Swedavia gör nya beräkningar varje år, så fråga dem direkt om din fastighet."),
    ("Gäller Arlandas bullerisolering även fritidshus?",
     "Ja. Enligt villkor 23 avses både permanentbostäder och fritidsbostäder med bostadsbyggnader."),
    ("Vad räknar akustikern med när ljudisoleringen bedöms?",
     "Bland annat fönsterstorlek, fönstertyp, glastjocklek, tätningslisternas skick, väggtyp, takkonstruktion och rummens storlek. Friskluftsventiler räknas också in."),
    ("Vilken ljudnivå inomhus är målet nära Arlanda?",
     "Swedavias villkor anger en flygbullernivå inomhus på högst 30 dB(A) och en maximal nivå nattetid på högst 45 dB(A)."),
    ("Hur får man besked om ett hus i Sigtuna ligger i en värdefull kulturmiljö?",
     "Kommunen tar emot adress, beskrivning och foton från alla väderstreck och återkommer med en bedömning."),
  ],
  "sources": [
    _SWEDAVIA,
    ("Sigtuna kommun – Bygga i kulturmiljö",
     "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html"),
    _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Vill ni ha tystare fönster i Sigtuna?", "Boka ett gratis platsbesök så går vi igenom fönster, glas och ventiler."),
  "img": [
    ("Enplansvilla i Sigtuna kommun med ljus träfasad och nya vita fönster",
     "1970s Swedish single-storey villa with light grey painted horizontal wooden cladding, new white windows with slim frames, dark concrete tile gable roof, neat lawn and small apple tree, flat open farmland in the distance, Märsta Sigtuna, overcast daylight, empty scene, clear sky without aircraft"),
    ("Insidan av ett nytt vitt fönster med spaltventil i överkant i ett ljust sovrum",
     "interior view of a new white wooden window in a quiet bright Scandinavian bedroom, thick multi-pane insulated glazing, a slim white slot air vent integrated in the top of the window frame, white window sill, view of green trees outside, soft daylight, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"fonsterbyte-upplands-vasby.html": {
  "kind": "district", "service": "fonsterbyte", "ort": "Upplands Väsby", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Upplands Väsby – inflygning, E4 och ljud",
  "description": "Fönsterbyte i Upplands Väsby: inflygningen mot Arlanda, väg- och tågbuller, riktvärden för ljud inomhus och när ljudkrav och kulturvärden krockar.",
  "h1": "Fönsterbyte i Upplands Väsby",
  "lead": "I Upplands Väsby kommer ljudet från tre håll: inflygningen till Arlanda, E4 och järnvägen. Kommunen påpekar att fastighetsägaren själv ansvarar för att fönstren håller god kvalitet. Geal Entreprenad AB byter och renoverar fönster i villor och radhus i Bollstanäs, Runby, Grimstaby och resten av Väsby och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Inflygning, trafik och tystare fönster i Väsby.",
  "sections": [
    {"id": "inflygning-vasby", "anchor": "Inflygningarna",
     "h2": "Bana ett över Runby, bana tre över centrum",
     "paras": [
       "Upplands Väsby kommun beskriver att det främst är inflygningarna söderifrån som ger flygbuller: till bana ett över Runby och till bana tre över Väsby centrum, Sigma och Löwenströmska sjukhuset. Delar av kommunen kan också påverkas av startande plan. Normalt får bana tre inte användas efter klockan 22, men miljötillståndet tillåter undantag för flygsäkerhet och banarbeten.",
       "Swedavia redovisar villkoren för flygvägarna. Inflygningar som undviker Väsby tätort ska användas när det går utan att flygsäkerhet eller kapacitet påverkas. Vid inflygning till bana 01L får tätorten inte överflygas öster om banans förlängning lägre än 750 meter, och nattetid får avgående trafik från bana 19L inte lämna utflygningsvägen mellan Väsby och Vallentuna förrän den nått 3 050 meter.",
       "Kommunen skriver att den inte kan bestämma hur planen flyger. Klagomål går i första hand till länsstyrelsen, som har tillsynen, men Swedavia kan svara på om det förekommit avvikande flygningar.",
     ],
     "aside": {"title": "Flyget enligt kommunen", "items": [
       "Bana ett: inflygning över Runby", "Bana tre: över centrum och Sigma",
       "Bana tre normalt stängd efter kl. 22", "Tillsyn: länsstyrelsen"]}},
    {"id": "trafik-vasby", "h2": "Väg och järnväg – och fastighetsägarens ansvar",
     "paras": [
       "En stor källa till buller i Väsby är enligt kommunen väg- och järnvägstrafiken. Kommunen skriver att fastighetsägare har en skyldighet att se till att fönstren håller god kvalitet och underhålls för att undvika bullerstörningar. Den som upplever att fastigheten är bullerstörd kan vända sig till den som ansvarar för vägen och fråga om bullerskydd för fasaden. De flesta gator i tätorten är kommunens, medan Trafikverket ansvarar för E4 och andra större vägar.",
       "För bedömningen av buller inomhus hänvisar kommunen till Folkhälsomyndighetens allmänna råd. Där anges 30 dB som ekvivalent ljudnivå och 45 dB som maximal ljudnivå, och råden gäller rum för sömn, vila och daglig samvaro i både permanentbostäder och fritidshus.",
       "Vid besöket tittar vi därför på vilka rum som vetter mot vägen, spåret eller inflygningen. Ett sovrum mot E4 kan behöva ett annat glas än köket på gårdssidan. Läcker det runt karmen hjälper inte ens ett tjockt ljudglas.",
     ],
     "aside": None},
    {"id": "krock-vasby", "h2": "När ljudkravet krockar med husets kulturvärde",
     "paras": [
       "Boverket beskriver ett mål där Trafikverket ville byta fönstren på ett bostadshus till specialfönster för att klara ett föreläggande om ljudnivån inomhus (MÖD 2015-10-14, P 3853–15). Domstolen ansåg att bytet var en förvanskning och inte varsamt. Trafikverket hade inte visat att ljudkravet inte kunde nås på något annat sätt, och det var inte uteslutet att åtgärder som både dämpade ljudet och bevarade kulturvärdena fanns.",
       "Upplands Väsby kommun skriver att en byggnad kan vara kulturhistoriskt värdefull utan att vara utpekad i förväg. Exempel som kommunen nämner är skydd i detaljplan, ingå i ett riksintresse, vara utpekad i en inventering eller vara uppförd före 1920 med bibehållen karaktär. Kommunen har också tagit fram ett kommunövergripande kunskapsunderlag som uppdaterar kulturmiljöprogrammet från 1988.",
       "I ett äldre hus kan ljudet därför ofta dämpas genom att behålla bågarna och komplettera dem, med nytt glas i innerbågen och nya tätningslister, i stället för att byta hela fönstret. Läs mer om fasaden kring fönstren under " + _L.format("fasadrenovering-upplands-vasby.html", "fasadrenovering i Upplands Väsby") + ".",
     ],
     "aside": {"title": "Kan huset vara värdefullt?", "items": [
       "Skyddat i detaljplan", "Del av ett riksintresse",
       "Utpekat i en inventering", "Byggt före 1920 med karaktären kvar"]}},
    {"id": "anmalan-vasby", "h2": "Lovfritt byte – men anmälan om stommen berörs",
     "paras": [
       "För en- och tvåbostadshus krävs normalt inget bygglov för fasadändringar i Upplands Väsby, varken inom eller utanför detaljplan. Lov kan ändå krävas om detaljplanen har utökad lovplikt, om ändringen görs i ett kulturhistoriskt särskilt värdefullt område eller om en särskilt värdefull byggnad får ändrad karaktär.",
       "Kommunen påpekar också att en anmälan ska lämnas in om nya fönster eller dörrar innebär ingrepp i byggnadens stomme. Det kan gälla när en öppning görs bredare för ett större fönster eller en fönsterdörr mot trädgården. Boverket påminner samtidigt om att fönster med grövre snickerier släpper in mindre dagsljus.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett fönsterbyte i Upplands Väsby till",
  "steps": [
    ("Platsbesök", "Vi noterar vilka rum som vetter mot inflygning, väg eller spår."),
    ("Ljud och värme", "Glas och tätning väljs rum för rum efter läge och användning."),
    ("Regler", "Detaljplan, kunskapsunderlaget och eventuell anmälan för ny öppning kontrolleras."),
    ("Kostnadsförslag", "Ett skriftligt förslag med fönster, glas, montage och ventiler var för sig."),
    ("Montage", "Fönstren sätts in och tätas runt hela karmen, så att ljudet inte läcker förbi."),
    ("Kontroll", "Bågarnas tätning kontrolleras och ventilationen gås igenom med dig."),
  ],
  "rot_h2": "Rotavdrag för fönster i villa och radhus i Väsby",
  "rot": [
    "I ett småhus ger det rotavdrag att reparera eller byta ut fönster och att montera bullerglas och isolerglas. Avdraget är högst 30 procent av arbetskostnaden, 50 000 kr per person och år och 75 000 kr tillsammans med rutavdrag.",
    "Är radhuset en bostadsrätt gäller andra regler: att byta fönster ger inget avdrag, men att byta glaset i den inre bågen eller montera tätningslist gör det. Vi drar avdraget på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Upplands Väsby?",
  "price": [
    "Antal fönster, vilken ljudklass glaset ska ha och i vilka rum, om befintliga bågar kan kompletteras i stället för att bytas, om en öppning ska ändras och därmed kräver anmälan och hur mycket foder och bleck som ska göras om. Du får ett skriftligt kostnadsförslag efter ett gratis besök.",
  ],
  "faq": [
    ("Vilka delar av Upplands Väsby hör mest flyg?",
     "Enligt kommunen är det främst inflygningarna söderifrån, till bana ett över Runby och till bana tre över Väsby centrum, Sigma och Löwenströmska sjukhuset."),
    ("Vem ska vi kontakta om bullret från E4 vid vårt hus?",
     "Kommunen hänvisar till den som ansvarar för vägen. För E4 och andra större vägar är det Trafikverket, för de flesta gator i tätorten kommunen."),
    ("Vilken ljudnivå i sovrummet räknas som godtagbar?",
     "Folkhälsomyndighetens allmänna råd, som kommunen hänvisar till, anger 30 dB ekvivalent och 45 dB maximal ljudnivå inomhus."),
    ("Ger nya fönster rotavdrag i ett radhus som är bostadsrätt?",
     "Inte själva bytet. Skatteverket godkänner däremot att byta glaset i den inre fönsterbågen eller montera tätningslist i en bostadsrätt."),
    ("Krävs anmälan för att göra fönsteröppningen större i Väsby?",
     "Ja, om ingreppet påverkar byggnadens stomme. Kommunen skriver att en anmälan ska lämnas in när nya fönster eller dörrar innebär ingrepp i stommen."),
  ],
  "sources": [
    ("Upplands Väsby kommun – Buller",
     "https://www.upplandsvasby.se/bygga-bo-och-miljo/buller-och-luftkvalitet/buller"),
    ("Upplands Väsby kommun – Fasadändring",
     "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/fasadandring"),
    ("Upplands Väsby kommun – Kulturhistoriska byggnader, kulturmiljöer",
     "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/kulturhistoriska-byggnader-kulturmiljoer"),
    ("Folkhälsomyndigheten – Allmänna råd om buller inomhus, FoHMFS 2014:13 (pdf)",
     "https://www.fohm.se/contentassets/66c03ed04e244b92a9165705ef3ac3c2/fohmfs-2014-13.pdf"),
    _SWEDAVIA, _BV_LJUD, _BV_FONSTER, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Vill ni sova tystare i Upplands Väsby?", "Boka ett gratis platsbesök så går vi igenom fönstren rum för rum."),
  "img": [
    ("Radhuslänga i Upplands Väsby med mörk träpanel och vita fönster",
     "row of 1970s Swedish two-storey terraced houses with dark brown vertical wooden cladding, white wooden windows, small front gardens with low hedges, dark concrete tile roofs, quiet residential street, Upplands Väsby, overcast daylight, empty scene, no aircraft"),
    ("Nytt vitt fönster med spröjs i en ljust putsad vägg, sett snett från sidan",
     "angled close-up view of a newly installed white wooden window with triple glazing set into a light plastered wall, clean joints around the frame, white metal sill flashing below, reflections of trees in the glass, daylight, no hands"),
  ],
  "related": [],
},

}
