# -*- coding: utf-8 -*-
"""Tapetsering – ortsidor v15: Södermalm, Vasastan, Solna, Lidingö, Hässelby, Spånga (2026-10-25).
Deltjänst under malare.html (TJ_HUB["tapetsering"]). Intent: tapet – tapettyper, underlag, äldre tapeter och
limfärg, fukt – skild från ortens malare-<ort>.html (som handlar om fasad, kulör och lov) och från hubben.
Lokal vinkel per sida:
Södermalm – tapetlagren i malmarnas äldre hus: spännpapp och makulatur, datering, spara en bit, styrelsens
tillstånd när lägenheten har kulturvärden (bostadsrättslagen 7 kap. 7 § andra stycket) och förvanskningsförbudet
inomhus; Vasastan – putsväggen i stenstadens hyreshus: kridering och dålig vidhäftning, förlimning med utspätt
klister och täckpapp, bronstryck, grannar och föreningens regler; Solna – väggen avslöjar husets ålder: Råsunda och
1950-talsbebyggelsen, kridering före sandspacklet, vinyl och non-woven; Lidingö – villans tapeter och varsamheten:
värdefull utan att stå i programmet, byggnadsminnen, inventeringar, kallställda gästhus och täta tapeter;
Hässelby – grupphusen och villastaden: gipsväggar och oförlimmade spacklingar, glasverandan, blöta upp gamla lager;
Spånga – villastäderna Solhem, Bromsten, Flysta och Sundby: tapet efter husets epok, lumppapp och spännpapp,
torrt underlag och värme, en pappspänd tapet som släppt.
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
  Svenska Byggnadsvårdsföreningen (byggnadsvard.se: Underlag för tapetsering – fukt i kök och badrum, underlag i nya
  och gamla hus, veck på spänd papp, extra rulle, vassa korn, kridering i hus från 1920–1950-talen, sandspackel vid
  mitten av 1950-talet, bronstryck – grunda med alkydfärg eller shellack; Vad är makulatur – restpapper, spännpapp
  vanlig under 1800-talet, fungerar på panel; Underlag för tapetsering på putsad tegelvägg fr 1895 – husfix eller
  väggspackel, grunda med tapetklister utspätt med 40–50 % vatten, täckpapp (målarpapp) i 60 cm bredd, låt torka;
  Tapeter – täta hydrofoba skikt i gamla hus, fukt anrikas, alternativ limfärgstapeter, lerklining och
  diffusionsöppna färger; Tapetsera med modern tapet i gammalt hus – uppvärmt året runt inga problem, kallställt
  kan fukt anrikas bakom tätskiktet; Spärrmålning med miljövänlig färg – ett lager tapet på gips ingen fara,
  spacklingarna oftast inte förlimmade, 50 % stärkelseklister och 50 % vatten, mögel under tätt ytskikt om huset
  står ouppvärmt, non-woven plastbehandlade och täta, papperstapet med stärkelseklister; Tapetsering med lumppapp –
  underlaget inte tillräckligt torrt och/eller inte förlimmat, kylan; Rädda pappspändtapet som släppt – skära upp,
  fukta baksidan, spika tillbaka, klistra remsor; Vävtapet – underlaget slätt och fast),
  Kulturen i Lund (Tapeter, pdf: trämassa omkring 1870, enklare tapeter på obehandlat papper, otaliga lager, blöta
  upp ett tapetsjok, arsenik – förbud mot handel 1876, stämpeln "Arsenikfri", havregrötstapeten i slutet av
  1930-talet, fondtapeter på 1950-talet, första vinyltapeten 1959, genombrott på 1970-talet, pvc-yta lättskött,
  handtryck efter eget original), Riksantikvarieämbetet (Byggnadsmåleri med traditionella färgtyper, pdf: limfärg som
  tryckfärg på tapeter ända in på 1950-talet, kridering på puts under tapeterna innan sandspacklet, känslig mot fukt –
  olämplig i kök och badrum), Boverket (PBL kunskapsbanken: Förvanskningsförbudet – gäller exteriört och interiört,
  oberoende av lovplikt, inget förändringsförbud, byggnader före 1920-talets bebyggelseexpansion med huvudsaklig
  karaktär bevarad, källa till kunskap om äldre material och teknik), Riksdagen (bostadsrättslag 1991:614, 7 kap.
  7 §, 9 § och 12 §), Skatteverket (Ger arbetet rätt till rotavdrag?: tapetsera i småhus, bostadsrätt och
  ägarlägenhet, innanför bostadens tak, väggar och golv, våtrumstapet till kakel; Så fungerar rotavdraget),
  Stockholms stad (Områdesfakta 2025: Mariatorget, Östra Matteus, Hässelby villastad, Solhem, Bromsten;
  bygglov.stockholm: Stadsmuseets kulturhistoriska klassificering – rådgivning, svar inom tre veckor; Översiktsplan –
  Riksintressen enligt miljöbalken (pdf med text): omkring 300 hus kvar från tidig bebyggelse på malmarna, mestadels
  på Södermalm, svårt att tala om originalutförande, bevarade inredningar; klassiska stenstaden 1870–1930, 300 000
  invånare vid sekelskiftet, normalt fem våningar, inre modernisering prövas enligt varsamhetskraven, gul klass;
  Varsam utveckling av småhus- och villaområden (pdf med text): villastäderna, Spånga municipalsamhälle på
  1910-talet, Solhem en tiondel av tomten, trä dominerande, glasverandor, Hässelby villastad 1960–1970-talen,
  tabellen s. 86 – Solhem kulturhistoriskt värdefull miljö), Solna stad (Kulturmiljöer i Solna: stenstaden och
  villastaden i Råsunda, 1950-talsbebyggelse i Råsunda, Skytteholm och Huvudsta), Lidingö stad (Frågor och svar
  om kulturmiljöprogrammet: inte varje byggnad inventerad, inventeringar 1970–1980-talet och 2013–2015, nio
  byggnadsminnen, länsstyrelsen hanterar tillstånd, förvanskning även utan bygglov, underhålla befintliga material
  hellre än byta, byggnadsvårdsbidrag hos länsstyrelsen).
Strukna (ej verifierade eller medvetet utelämnade): att byggåret brukar stå i föreningens årsredovisning; att
väggarna i Vasastans lägenheter "oftast" är puts (bara villkor); att papperstapet är ett "öppet" ytskikt (källan
nämner den bara som alternativ till non-woven och latexgrund – i Lidingös lista står nu bara källans alternativ
limfärgstapeter, lerklining och diffusionsöppna färger); att spacklingar sitter "i skarvar och skruvhål"; att
makulatur "ofta" sitter under äldre tapeter; att ett kriderat lager "släpper lätt" (nu RAÄ: limfärg känslig mot
fukt); att en tunn tapet kräver slätare underlag; att en tät vinyltapet behöver ritsas; hur non-woven sätts upp (klister på väggen) och att den kan
dras av torr – stod bara hos återförsäljare, inte i en oberoende källa; att tapeter kan "skiktas" (bara ett
forum); hur många tapetlager som är för många (texten bröts av bakom inloggning); varför non-woven inte ska sitta
på spännpapp (källan anger inget skäl); arsenik som hälsorisk vid rivning (källan säger bara att handel förbjöds
1876); vad Stadsmuseet samlar in för tapetprov (ingen källa); vilka tapeter som satt i Råsundas, Lidingös eller
Spångas hus från början; att 1960–70-talets grupphus i Hässelby har gipsväggar (skrivs som villkor, "är väggen av
gips"); arbetstider för renovering i bostadsrätt (finns bara i varje förenings ordningsregler); varumärken på tapeter
och klister; priser, avgifter och tidsåtgång.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
Kritikpass 2026-10-25: alla siffror och påståenden kontrollerade mot källtexterna igen – Mariatorget 2025: 8 701
bostäder, 5 027 bostadsrätter, 35 i småhus; Östra Matteus 2025: 7 680 bostäder, 5 593 bostadsrätter, inga småhus;
Hässelby villastad 2025: 7 029 bostäder, 5 009 i småhus, 4 757 äganderätter; Solhem 2025: 3 470 bostäder, 2 038 i
småhus, 1 946 äganderätter; Bromsten 2025: 3 826 bostäder, 2 735 i flerbostadshus, 1 066 i småhus; omkring 300 hus;
1870–1930; 300 000; fem våningar; 1920-talets bebyggelseexpansion; 1920–1950-talen och mitten av 1950-talet
(kridering/sandspackel); 40–50 % vatten och 60 cm täckpapp; 50/50 stärkelseklister; 1870 (trämassa); 1876
(arsenik); 1959 och 1970-talet (vinyl); slutet av 1930-talet (havregrötstapeten); 1950-talet (fondtapeter); nio
byggnadsminnen; 1970–1980-talet och 2013–2015 (Lidingös inventeringar); tre veckor (Stadsmuseet); 1910-talet
(Spånga municipalsamhälle); en tiondel av tomten (Solhem). Formuleringar rättade i passet: "styrelsen måste alltid
godkänna" -> lagens krav på tillstånd när lägenheten har särskilda kulturvärden och åtgärden påverkar dem, som en
fråga till styrelsen; "non-woven andas inte" -> källans "plastbehandlade och täta"; "kridering finns i alla
stenstadshus" -> RAÄ:s "förr, innan sandspacklet" och föreningens "kan befaras i hus från 1920–1950-talen";
"tapet tål inte badrum" -> föreningens "bara inte luftfuktigheten blir för hög, som den kan bli i kök och badrum".
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py.
Extern kritiker 2026-10-26: H1 'på Södermalm/Lidingö', struket väv-stycket i Hässelby (ej i källorna), papperstapet på veranda ej som föreningens fuktöppna alternativ, 'ofta' struket om blötläggning, BRL 7 § med undantag för kulturhistoriska värden, 'på en vägg' och 'oftast' strukna, 'Tidigt 1900-tal'. Hässelby fyllt på med egna arbetsrutiner (inga fakta).
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

_SBF = "https://byggnadsvard.se/"
_SBF_UND = ("Svenska Byggnadsvårdsföreningen – Underlag för tapetsering", _SBF + "underlag-for-tapetsering/")
_SBF_MAK = ("Svenska Byggnadsvårdsföreningen – Vad är makulatur och hur arbetar man med den?",
            _SBF + "vad-ar-makulatur-och-hur-arbetar-man-med-den/")
_SBF_PUTS = ("Svenska Byggnadsvårdsföreningen – Underlag för tapetsering på putsad tegelvägg",
             _SBF + "underlag-for-tapetsering-pa-putsad-tegelvagg-fr-1895/")
_SBF_TAT = ("Svenska Byggnadsvårdsföreningen – Tapeter (täta skikt i gamla hus)", _SBF + "tapeter-2/")
_SBF_MOD = ("Svenska Byggnadsvårdsföreningen – Tapetsera med modern tapet i gammalt hus?",
            _SBF + "tapetsera-med-modern-tapet-i-gammalt-hus/")
_SBF_GIPS = ("Svenska Byggnadsvårdsföreningen – Spärrmålning under ny tapet", _SBF + "sparrmalning-med-miljovanlig-farg/")
_SBF_LUMP = ("Svenska Byggnadsvårdsföreningen – Tapetsering med lumppapp", _SBF + "tapetsering-med-lumppapp/")
_SBF_SPANN = ("Svenska Byggnadsvårdsföreningen – Rädda pappspänd tapet som släppt från väggen",
              _SBF + "radda-pappspandtapet-som-slappt-fran-vagg/")
_SBF_VAV = ("Svenska Byggnadsvårdsföreningen – Vävtapet", _SBF + "vavtapet/")
_KULT = ("Kulturen i Lund – Tapeter (pdf)", "https://www.kulturen.com/wp-content/uploads/2018/02/Tapeter.pdf")
_RAA = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf)", "https://www.raa.se/publicerat/9789172095830.pdf")
_BOV_FORV = ("Boverket – PBL kunskapsbanken: Förvanskningsförbudet",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/teman/kulturvarden/kulturvarden-i-plan---och-bygglagen/krav-pa-byggnadsverk-och-tomter/forvanskningsforbudet/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap.",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SSM_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
              "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/stadsmuseets-kulturhistoriska-klassificering/")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_SOLNA_KM = ("Solna stad – Kulturmiljöer i Solna", "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna")
_LID_FAQ = ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet",
            "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/")

_ROT_SUM = ("Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
            "tillsammans med rutavdrag. Material som tapet och klister ger inget avdrag, och inte heller resor.")

PAGES_TJ = {

# ------------------------------------------------------------------ SÖDERMALM
"tapetsering-sodermalm.html": {
  "kind": "district", "service": "tapetsering", "ort": "Södermalm", "svc_label": "Tapetsering",
  "title": "Tapetsering på Södermalm – gamla tapetlager och ny tapet",
  "description": "Tapetsering på Södermalm: ny tapet i äldre hus och bostadsrätter – spännpapp, tapetlager som berättar husets historia och när styrelsen ska tillfrågas.",
  "h1": "Tapetsering på Södermalm",
  "lead": "Under en tapet på Södermalm sitter ofta en annan, och under den kanske en tredje. Lagren kan vara det enda som visar hur lägenheten sett ut genom åren. Geal Entreprenad AB tapetserar i lägenheter och äldre hus på Södermalm, och innan något rivs ner tittar vi på vad som redan sitter på väggen och om det är värt att spara.",
  "card": "Ny tapet och gamla tapetlager.",
  "sections": [
    {"id": "aldre-hus-sodermalm", "anchor": "Husen",
     "h2": "Där malmarnas äldsta hus står kvar",
     "paras": [
       "Stadens översiktsplan beskriver att det bara finns en liten del kvar av det som byggdes på malmarna under 1700-talet och början av 1800-talet, omkring 300 hus, och att de flesta ligger på Södermalm. Planen konstaterar också att de flesta av husen byggts om och till genom århundradena, så att det är svårt att tala om ett originalutförande. Några har bevarade inredningar med till exempel dekorativt målade tak.",
       "Det mesta av stadsdelen är ändå bostadsrätter i flerbostadshus. I områdesfakta för Mariatorget 2025 finns 8 701 bostäder, varav 5 027 bostadsrätter och bara 35 i småhus. Oavsett om väggen sitter i ett trähus vid ett av bergen eller i ett stenhus från sekelskiftet börjar tapetseringen på samma sätt: vi tar reda på vad som ligger under.",
     ],
     "aside": {"title": "Mariatorget, bostäder 2025", "items": [
       "8 701 bostäder", "5 027 bostadsrätter", "35 i småhus"]}},
    {"id": "lagren-sodermalm", "h2": "Tapetlagren är en tidslinje",
     "paras": [
       "Kulturen i Lund förklarar varför gamla väggar kan ha så många lager. Omkring 1870 började tapeter tryckas på billigt papper av trämassa, och de enklaste trycktes på obehandlat papper som lätt blev fläckigt. Då tapetserade man om ofta, och lager lades på lager. Om man blöter upp ett tapetsjok går det att skilja lagren åt och följa hur modet har växlat.",
       "Baksidan kan hjälpa till med dateringen. Grön färg med arsenik gjorde att handel med arsenikhaltiga tapeter förbjöds i Sverige 1876, och tapeterna fick därefter stämpeln ”Arsenikfri” på baksidan. Riksantikvarieämbetet skriver att limfärg användes som tryckfärg på tapeter ända in på 1950-talet.",
       "Under tapeterna i ett äldre hus kan det sitta makulatur. Svenska Byggnadsvårdsföreningen beskriver ordet som ett samlingsnamn för restpapper, från tidningspapper till spännpapp, och spännpapp blev ett vanligt underlag för tapeter under 1800-talet. Ska lagren bort tar vi först en bit av varje och sparar den. Kulturen skriver att det går att beställa handtryckta tapeter efter ett eget original, så biten kan bli förlagan till nästa tapet.",
     ],
     "aside": {"title": "Ledtrådar i lagren", "items": [
       "Tryck på obehandlat papper", "Stämpeln Arsenikfri", "Limfärgstryck", "Tidningar som makulatur"]}},
    {"id": "styrelsen-sodermalm", "h2": "När styrelsen ska tillfrågas",
     "paras": [
       "Bostadsrättslagen 7 kap. 12 § säger att den som har bostadsrätten på egen bekostnad ska hålla lägenheten i gott skick, om stadgarna inte säger något annat. Lagens 7 § har dock ett andra stycke som är viktigt på Södermalm: för en lägenhet med särskilda historiska, kulturhistoriska, miljömässiga eller konstnärliga värden krävs styrelsens tillstånd för en åtgärd som påverkar ett sådant värde. Sitter det en gammal tapet eller ett målat tak som kan vara ett sådant värde frågar vi styrelsen innan något rivs.",
       "Även plan- och bygglagen gäller inne i huset. Boverket skriver att förvanskningsförbudet gäller vid alla ändringar, såväl exteriört som interiört, och oberoende av om åtgärden kräver lov. Förbudet är inget förändringsförbud, men det som gör byggnaden värdefull är skyddat, och byggnader från tiden före 1920-talets bebyggelseexpansion med sin huvudsakliga karaktär bevarad räknas som särskilt värdefulla om inget talar emot.",
       "Är du osäker kan Stadsmuseet hjälpa till. Stockholms stad skriver att museet ger rådgivning och bedömning och brukar svara inom tre veckor när det har fått adress, byggår och foton på fastigheten.",
     ],
     "aside": None},
    {"id": "underlag-sodermalm", "h2": "Ny tapet på ett gammalt underlag",
     "paras": [
       "Byggnadsvårdsföreningen räknar puts, timmer, spänd papp och spänd väv som lämpliga underlag i gamla hus. På spänd papp kan tapeten bilda veck i hörnen som behöver justeras efter några år. Att tapetsera ovanpå en gammal tapet går oftast bra, men bronstryck kan slå igenom den nya, och då grundar man först med alkydfärg eller shellack.",
       "Väljer du en tapet av äldre typ som kan försvinna ur sortimentet råder föreningen dig att köpa en extra rulle för framtida lagningar. Ska väggarna bara målas finns mer om det under " + _L.format("malare.html", "målare") + ". Hör köket till lägenhetens äldre delar kan du läsa om " + _L.format("koksrenovering-sodermalm.html", "köksrenovering på Södermalm") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen till på Södermalm",
  "steps": [
    ("Platsbesök", "Vi lyfter en kant och ser hur många lager som sitter på väggen och vad som ligger underst."),
    ("Prov och dokumentation", "En bit av varje lager tas tillvara och fotograferas innan något rivs."),
    ("Frågan till styrelsen", "Kan lagren eller ett målat tak vara ett kulturvärde skickar du en kort beskrivning till föreningen."),
    ("Skriftligt kostnadsförslag", "Nedtagning, underarbete och uppsättning redovisas var för sig."),
    ("Underarbete", "Lösa partier fästs eller tas ner, väggen lagas och grundas där det behövs."),
    ("Uppsättning", "Våderna sätts upp med passning av mönstret, och överbliven tapet lämnas kvar för lagningar."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i bostadsrätten",
  "rot": [
    "Skatteverket räknar tapetsering som rotarbete i bostadsrätt, ägarlägenhet och småhus. I bostadsrätten ska arbetet göras inne i bostaden, innanför dess tak, väggar och golv.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Södermalm?",
  "price": [
    "Hur många lager som ska ner, hur mycket väggen behöver lagas och hur krävande mönstret är att passa väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur gammal kan tapeten under tapeten vara i ett hus på Södermalm?",
     "Det varierar. Står det ”Arsenikfri” på baksidan är den troligen från tiden efter förbudet 1876, och tryck på obehandlat trämassepapper hör till tiden från omkring 1870."),
    ("Kan en gammal tapet tas ner och användas som förlaga?",
     "Ja. Vi sparar en bit av varje lager, och Kulturen i Lund skriver att det går att beställa handtryckta tapeter efter ett eget original."),
    ("Behöver föreningen godkänna att jag byter tapet?",
     "Normalt inte, men har lägenheten särskilda kulturvärden kräver lagen styrelsens tillstånd för åtgärder som påverkar dem. Fråga hellre en gång för mycket."),
    ("Kan ny tapet sitta direkt på den gamla?",
     "Det går oftast bra enligt Byggnadsvårdsföreningen. Har den gamla tapeten bronstryck grundar vi först så att trycket inte slår igenom."),
    ("Vem kan bedöma om tapeterna i vårt hus är värdefulla?",
     "Stadsmuseet ger rådgivning och bedömning. Skicka adress, byggår och foton, så brukar museet svara inom tre veckor."),
  ],
  "sources": [
    _RIKS, ("Stockholms stad – Områdesfakta 2025: Mariatorget (pdf)", _OF + "inre-staden/sodermalm/mariatorget.pdf"),
    _KULT, _RAA, _SBF_MAK, _SBF_UND, _BRL, _BOV_FORV, _SSM_KLASS, _SKV, _SKV2,
  ],
  "cta": ("Ska lägenheten på Södermalm få ny tapet?", "Boka ett gratis platsbesök, så tittar vi på vad som sitter på väggen i dag innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nytapetserat rum i en äldre lägenhet med ljus blommönstrad tapet och vita fönsterfoder",
     "empty room in an 18th century Stockholm house on Södermalm, freshly hung pale cream wallpaper with a small faded floral pattern, low ceiling, wide old pine floorboards, deep window recess with white painted wooden frames, soft daylight, no furniture, no people, no text, no letters"),
    ("Flera lager gamla tapeter och tidningsmakulatur som syns i en uppfläkt väggbit",
     "close-up of an old interior wall where a torn section reveals several layers of old wallpaper with different faded patterns, beneath them brown spännpapp backing paper, aged plaster edge, warm side light, no readable text, no letters, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VASASTAN
"tapetsering-vasastan.html": {
  "kind": "district", "service": "tapetsering", "ort": "Vasastan", "svc_label": "Tapetsering",
  "title": "Tapetsering i Vasastan – putsväggar i stenstadens hus",
  "description": "Tapetsering i Vasastan: ny tapet på putsade väggar i sekelskifteshus – kridering, förlimning, täckpapp, bronstryck och hänsyn till grannarna i föreningen.",
  "h1": "Tapetsering i Vasastan",
  "lead": "I ett stenhus från sekelskiftet i Vasastan kan den släta väggen vara puts på murverk, och under färgen eller tapeten kan det sitta ett gammalt utjämningslager som inte vill bära något nytt. Geal Entreprenad AB tapetserar i Vasastans bostadsrätter, och det mesta av arbetet görs innan första våden kommer upp: vi provar väggen, lagar den och förlimmar.",
  "card": "Ny tapet på gamla putsväggar.",
  "sections": [
    {"id": "stenstaden-vasastan", "anchor": "Stenstaden",
     "h2": "Stenstadens hyreshus från 1870 till 1930",
     "paras": [
       "Översiktsplanen kallar de täta kvarteren från 1870–1930 för den klassiska stenstaden. Under 1800-talets andra hälft tredubblades befolkningen till 300 000 vid sekelskiftet, och hyreshusen som byggdes då är normalt fem våningar höga med dekorerade fasader i puts eller natursten. Planen beskriver också att inre modernisering prövas enligt plan- och bygglagens varsamhetskrav, och att många hus har låg klassificering, gul klass, eftersom de förändrats sedan de byggdes.",
       "I dag är nästan alla lägenheter bostadsrätter. Områdesfakta för Östra Matteus räknar 7 680 bostäder 2025, varav 5 593 bostadsrätter och inga i småhus. Den som tapetserar gör det alltså i regel mitt i ett hus med grannar på alla sidor.",
     ],
     "aside": {"title": "Östra Matteus, bostäder 2025", "items": [
       "7 680 bostäder", "5 593 bostadsrätter", "Inga småhus"]}},
    {"id": "kridering-vasastan", "h2": "Kridering: när väggen inte bär tapeten",
     "paras": [
       "Riksantikvarieämbetet beskriver att det förr, innan sandspacklet kom, var vanligt att limfärg användes som utjämnande lager på puts under tapeterna. Det kallades kridering. Svenska Byggnadsvårdsföreningen skriver att dålig vidhäftning kan befaras i hus från 1920–1950-talen, där väggarna underbehandlades med lim och krita, och att sandspackel började användas vid mitten av 1950-talet.",
       "Limfärg är enligt Riksantikvarieämbetet känslig mot fukt, och nytt klister är blött. Därför provar vi först med en fuktig svamp eller en remsa tejp på en undanskymd yta. Kritar det, eller följer det gamla lagret med, behöver det tas bort eller bindas innan vi sätter upp ny tapet.",
     ],
     "aside": {"title": "Prova väggen först", "items": [
       "Kritar ytan?", "Släpper lagret när det blöts?", "Lösa tapetrester?", "Sprickor i putsen?"]}},
    {"id": "putsen-vasastan", "h2": "Från bar puts till färdig vägg",
     "paras": [
       "Byggnadsvårdsföreningen har svarat på hur en frilagd putsvägg i ett hus från 1895 förbereds, sedan lösa tapeter och tidningspapper ångats bort. Hål lagas med väggspackel. Sedan grundas väggen med tapetklister som spätts ut med 40–50 procent vatten och får torka, och därefter klistras en täckpapp, så kallad målarpapp, i 60 centimeters bredd upp på väggen och får torka innan den nya tapeten sätts upp.",
       "Föreningen påpekar att vassa korn och toppar efter dålig slipning eller orent klister syns genom tapeten mer än åsar och gropar, så slipningen är viktigare än man tror. Har väggen en gammal tapet med bronstryck som ska sitta kvar under den nya grundas den med alkydfärg eller shellack, så att trycket inte slår igenom.",
       "Ska väggarna bara målas finns mer under " + _L.format("malare.html", "målare") + ". Det trägolv som ofta ligger i samma rum beskrivs under " + _L.format("golvlaggare-vasastan.html", "golvläggare i Vasastan") + ".",
     ],
     "aside": None},
    {"id": "sekelskiftet-vasastan", "h2": "Tapeterna när husen var nya",
     "paras": [
       "Kulturen i Lund beskriver hur jugendstilen slog igenom på bred front i Sverige i början av 1900-talet, med växtmönster och slingrande stjälkar som tidiga mönster och stelare ornament senare. Tapeter fanns då i alla prisklasser och nådde nästan alla svenska hem. Samtidigt förespråkade radikala kretsar ljus och luft i hemmen, och Ellen Key föreslog att man skulle köpa de billigaste tapeterna och sätta dem med mönstret mot väggen och den ljusa baksidan utåt.",
       "Vill du ge en sekelskifteslägenhet en tapet som hör till huset finns det i dag tillverkare som tagit upp äldre mönster i sina kollektioner, skriver Kulturen. Hittar vi rester av en äldre tapet bakom en list eller ett element tar vi vara på biten, så att du kan jämföra.",
     ],
     "aside": None},
    {"id": "grannar-vasastan", "h2": "Grannarna och föreningens regler",
     "paras": [
       "Bostadsrättslagen 7 kap. 9 § säger att den som bor i lägenheten ska se till att grannarna inte utsätts för störningar som är skadliga för hälsan eller annars försämrar deras bostadsmiljö så att de inte skäligen bör tålas. Den säger också att man ska rätta sig efter de särskilda regler som föreningen meddelar. Har föreningen regler om tider för renovering följer vi dem, och vi bär ut rester och emballage utan att lämna dem i trapphuset.",
       "En ny tapet nämns inte bland de åtgärder som enligt 7 kap. 7 § kräver styrelsens tillstånd, som ingrepp i bärande konstruktion eller ändrade ledningar. Har lägenheten särskilda kulturvärden kräver lagen dock tillstånd för åtgärder som påverkar dem, och det kan gälla en bevarad tapet.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen till i Vasastan",
  "steps": [
    ("Platsbesök", "Vi provar väggen: kritar den, sitter gamla lager fast och var behövs lagning?"),
    ("Skriftligt kostnadsförslag", "Nedtagning, lagning, förlimning, täckpapp och uppsättning står som egna poster."),
    ("Skydd", "Golv, element och fönsterbänkar täcks, och vi planerar bärandet i trapphuset."),
    ("Underarbete", "Lösa lager ångas bort, putsen lagas och väggen förlimmas och får torka."),
    ("Uppsättning", "Tapeten sätts upp våd för våd från en lodlinje, med passning av mönstret."),
    ("Avslut", "Överbliven tapet lämnas till dig och skarvarna går vi igenom tillsammans."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Vasastan",
  "rot": [
    "Att tapetsera ger rotavdrag i en bostadsrätt enligt Skatteverket, så länge arbetet görs innanför bostadens tak, väggar och golv. Arbete i trapphus och andra gemensamma utrymmen ingår inte.",
    _ROT_SUM + " Avdraget dras direkt på Geals faktura.",
  ],
  "price_h2": "Vad påverkar priset i Vasastan?",
  "price": [
    "Väggens skick styr mest: hur mycket som ska ångas bort, om putsen behöver täckpapp och hur många rum som tapetseras. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad är kridering och varför spelar det roll för ny tapet?",
     "Det är ett gammalt utjämningslager av lim och krita på putsen. Det kan ge dålig vidhäftning, så vi provar ytan innan ny tapet sätts upp."),
    ("Måste putsväggen täckas med papp innan den tapetseras?",
     "Det beror på väggen, men på en frilagd och lagad putsvägg råder Byggnadsvårdsföreningen att förlimma och klistra upp en täckpapp innan den nya tapeten."),
    ("Hur gör man med en gammal tapet med guldtryck under den nya?",
     "Bronstryck kan slå igenom. Väggen grundas därför med alkydfärg eller shellack innan den nya tapeten kommer upp."),
    ("Får vi tapetsera på kvällarna i vår förening i Vasastan?",
     "Det beror på föreningens regler. Lagen säger att man ska rätta sig efter dem och inte störa grannarna mer än de skäligen bör tåla."),
    ("Syns ojämnheter i väggen genom ny tapet?",
     "Ja. Byggnadsvårdsföreningen skriver att vassa korn och toppar syns mer än åsar och gropar, så spacklingen slipas noga."),
  ],
  "sources": [
    _RIKS, ("Stockholms stad – Områdesfakta 2025: Östra Matteus (pdf)", _OF + "inre-staden/norra-innerstaden/ostra-matteus.pdf"),
    _RAA, _SBF_UND, _SBF_PUTS, _BRL, _SKV, _SKV2,
  ],
  "cta": ("Ska lägenheten i Vasastan tapetseras?", "Boka ett gratis platsbesök, så provar vi väggen och berättar vad underarbetet kräver innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nytapetserat rum i en sekelskifteslägenhet med hög takhöjd, stuckatur och grågrön tapet",
     "empty room in a Stockholm 1900s stone apartment building, tall ceiling with white plaster cornice, walls freshly papered with a muted grey-green wallpaper with a subtle vertical stripe, tall double windows with white frames, herringbone oak floor, soft daylight, no furniture, no people, no text, no letters"),
    ("Putsvägg under arbete med en klistrad remsa täckpapp, spackelspade och klisterhink",
     "close-up of a plastered apartment wall being prepared for wallpaper, one vertical strip of plain off-white lining paper pasted on the patched plaster, a bucket of wallpaper paste with a wide brush and a putty knife on a protective sheet on the floor, natural window light, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SOLNA
"tapetsering-solna.html": {
  "kind": "district", "service": "tapetsering", "ort": "Solna", "svc_label": "Tapetsering",
  "title": "Tapetsering i Solna – väggen avslöjar husets ålder",
  "description": "Tapetsering i Solna: Råsundas stenstad och villastad och 1950-talets bostäder – kridering, sandspackel, vinyl, non-woven och papperstapet på rätt underlag.",
  "h1": "Tapetsering i Solna",
  "lead": "Hur en vägg ska förberedas för ny tapet beror mycket på när huset byggdes. En lägenhet i Råsunda kan ha ett helt annat underlag än en lägenhet i ett hus från 1950-talet i Huvudsta, även om väggarna ser likadana ut när de är målade. Geal Entreprenad AB tapetserar i lägenheter, radhus och villor i Solna och börjar med att ta reda på vad väggen består av.",
  "card": "Tapet efter husets ålder och underlag.",
  "sections": [
    {"id": "epoker-solna", "anchor": "Husens åldrar",
     "h2": "Från Råsundas stenstad till 1950-talets hus",
     "paras": [
       "Solna stad räknar upp drygt 30 sammanhängande kulturhistoriskt värdefulla miljöer. Bland dem finns stenstaden och villastaden i Råsunda, villabebyggelsen i norra Råsunda och 1950-talsbebyggelse i Råsunda, Skytteholm och Huvudsta. Staden har också en karta över kulturhistoriskt klassade byggnader.",
       "För den som ska tapetsera spelar årtalet roll av ett enkelt skäl: väggarna förbehandlades på olika sätt under olika perioder, och det som sitter under färgen eller den gamla tapeten bestämmer hur den nya fäster. Därför frågar vi efter byggåret och provar sedan väggen.",
       "Även den gamla tapeten kan berätta något. Riksantikvarieämbetet skriver att limfärg användes som tryckfärg på tapeter ända in på 1950-talet, och limfärg är känslig mot fukt. Kulturen i Lund beskriver 1950-talets tapeter med neutrala bottenfärger, linjära mönster och färgaccenter, och fondtapeter med djärvare mönster. Sitter en sådan tapet kvar i en lägenhet från den tiden är den värd att titta på innan den rivs.",
     ],
     "aside": {"title": "Miljöer i stadens lista", "items": [
       "Stenstaden i Råsunda", "Råsunda villastad", "1950-tal i Huvudsta", "1950-tal i Skytteholm"]}},
    {"id": "kridering-solna", "h2": "Före och efter sandspacklet",
     "paras": [
       "Svenska Byggnadsvårdsföreningen skriver att dålig vidhäftning kan befaras i hus från 1920–1950-talen, då väggarna underbehandlades med lim och krita, så kallad kridering. Vid mitten av 1950-talet började sandspackel användas som underlag. Riksantikvarieämbetet beskriver samma sak från andra hållet: förr, innan sandspacklet kom, var limfärg ett vanligt utjämnande lager på puts under tapeterna.",
       "I praktiken betyder det att en vägg i ett hus från 1930-talet kan behöva tas ner till fast underlag eller bindas innan ny tapet kommer upp, medan en sandspacklad vägg från slutet av 1950-talet oftare bara behöver lagas, slipas och grundas. Limfärg är dessutom känslig för fukt, och ett blött klister kan få den att släppa.",
     ],
     "aside": None},
    {"id": "tapettyper-solna", "h2": "Papper, vinyl eller non-woven",
     "paras": [
       "Kulturen i Lund skriver att den första vinyltapeten tillverkades i Sverige 1959 men slog igenom på allvar först på 1970-talet. Ytan av pvc-plast gjorde tapeten lättskött och hållbar. Byggnadsvårdsföreningen beskriver non-woventapeter som plastbehandlade och täta, och nämner papperstapet som sätts upp med stärkelseklister som ett alternativ för den som vill undvika latexgrund.",
       "Vilken tapet som passar beror på rummet och huset. I ett hus som värms upp året runt är ett tätt ytskikt på insidan inget problem enligt föreningen. Vi går igenom alternativen med dig innan du väljer mönster.",
       "Är det väggarna utanpå huset som ska ses över, eller fönster och snickerier som ska målas, finns det mer under " + _L.format("malare-solna.html", "målare i Solna") + ".",
     ],
     "aside": {"title": "Tre vanliga tapettyper", "items": [
       "Papperstapet – stärkelseklister", "Vinyltapet – pvc-yta, lättskött", "Non-woven – plastbehandlad och tät"]}},
    {"id": "bostadsratt-solna", "h2": "Tapet i en bostadsrätt i Solna",
     "paras": [
       "Enligt bostadsrättslagen 7 kap. 12 § ska den som har bostadsrätten på egen bekostnad hålla lägenheten i gott skick, om stadgarna inte säger något annat. En ny tapet är inte någon av de åtgärder som 7 § räknar upp som tillståndspliktiga, som ingrepp i bärande konstruktion eller ändrade ledningar för vatten och avlopp.",
       "Tapet hör inte hemma där luftfuktigheten blir hög, skriver Byggnadsvårdsföreningen, och den kan bli det i kök och badrum. Skatteverket nämner för övrigt att byta våtrumstapet mot kakel som ett förbättringsarbete som ger rotavdrag.",
       "Ofta görs tapetseringen samtidigt som annat måleri i lägenheten. I en bostadsrätt räknar Skatteverket även målning av tak, väggar och element, innerdörrar och insidan av ytterdörrar och fönster som rotarbete, men inte målning av fönstrens eller ytterdörrarnas utsida, balkonger eller fasader.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen till i Solna",
  "steps": [
    ("Byggår och prov", "Du berättar när huset byggdes, och vi provar om väggen kritar eller släpper."),
    ("Val av tapettyp", "Papper, vinyl eller non-woven väljs efter rummet och underlaget."),
    ("Skydd", "Golv, element och fönsterbänkar täcks, och arbetet läggs på tider som passar föreningens regler."),
    ("Skriftligt kostnadsförslag", "Underarbete och uppsättning redovisas var för sig."),
    ("Underarbete", "Gamla lager tas ner där det behövs, väggen spacklas, slipas och grundas."),
    ("Uppsättning", "Tapeten sätts upp med det klister som hör till tapettypen."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Solna",
  "rot": [
    "Skatteverket räknar tapetsering som rotarbete, både i en villa och i en bostadsrätt. I bostadsrätten gäller det arbete inne i lägenheten, innanför tak, väggar och golv.",
    _ROT_SUM + " Geal drar av rotavdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Solna?",
  "price": [
    "Hur mycket av det gamla som ska ner, vilket underlag väggen behöver och vilken tapettyp du väljer påverkar mest. Efter det kostnadsfria platsbesöket får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför släpper ny tapet i vår lägenhet från 1930-talet?",
     "Det kan bero på kridering, ett äldre underlag av lim och krita som Byggnadsvårdsföreningen kopplar till hus från 1920–1950-talen. Lagret behöver tas ner eller bindas."),
    ("Är vinyltapet ett bra val i hallen?",
     "Kulturen i Lund beskriver vinyltapetens pvc-yta som lättskött och hållbar, vilket passar i en hall. Rummet ska inte ha hög luftfuktighet."),
    ("Kan man sätta tapet i badrummet i Solna?",
     "Vanlig tapet passar inte där luftfuktigheten blir hög, som i badrum. Där behövs ett våtrumsskikt i stället."),
    ("Hur vet jag när mitt hus i Solna är byggt?",
     "Föreningen eller fastighetsägaren brukar veta. Solna stad har också en karta över kulturhistoriskt klassade byggnader."),
    ("Behöver jag styrelsens tillstånd för att tapetsera om?",
     "Normalt inte. Tapetsering är inte någon av de åtgärder som bostadsrättslagen kräver tillstånd för, om lägenheten inte har särskilda kulturhistoriska värden."),
  ],
  "sources": [
    _SOLNA_KM, _SBF_UND, _RAA, _KULT, _SBF_GIPS, _SBF_MOD, _BRL, _SKV, _SKV2,
  ],
  "cta": ("Ska du tapetsera om i Solna?", "Boka ett gratis platsbesök, så provar vi väggen och hjälper dig välja tapettyp innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nytapetserat vardagsrum i en 1950-talslägenhet med ljus mönstrad tapet",
     "empty living room in a 1950s Swedish apartment, one wall freshly papered with a light beige wallpaper with a simple linear mid-century pattern, other walls plain white, parquet floor, window with a white wooden frame and a radiator under it, soft daylight, no furniture, no people, no text, no letters"),
    ("Tre tapetrullar i olika material på ett bord bredvid en tapetborste och en tapetkniv",
     "three rolls of wallpaper in different materials lying on a wooden pasting table, one plain paper, one with a slightly glossy vinyl surface, one matte non-woven, a wallpaper smoothing brush and a snap-off knife beside them, neutral room in background, natural light, no people, no hands, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ LIDINGÖ
"tapetsering-lidingo.html": {
  "kind": "district", "service": "tapetsering", "ort": "Lidingö", "svc_label": "Tapetsering",
  "title": "Tapetsering på Lidingö – villans tapeter och varsamhet",
  "description": "Tapetsering på Lidingö: ny tapet i äldre villor – varsamhetskravet inomhus, byggnadsminnen, kallställda gästhus och täta tapeter samt spännpapp på panel.",
  "h1": "Tapetsering på Lidingö",
  "lead": "I en äldre villa på Lidingö kan väggarna inne vara lika viktiga för husets karaktär som fasaden. Geal Entreprenad AB tapetserar i villor, radhus och gästhus på Lidingö, och vi börjar med två frågor: är huset värdefullt, och värms det upp hela året?",
  "card": "Ny tapet med hänsyn till huset.",
  "sections": [
    {"id": "vardefullt-lidingo", "anchor": "Värdefulla hus",
     "h2": "Värdefullt även om det inte står i programmet",
     "paras": [
       "Lidingö stad förklarar att arbetet med kulturmiljöprogrammet inte omfattade en inventering av varje enskild byggnad. Programmet pekar ut områden, och det finns särskilt värdefulla byggnader på ön som inte beskrivs i det. Staden har äldre inventeringar av enskilda byggnader, dels från 1970- och 1980-talen, dels från 2013–2015, och via miljö- och stadsbyggnadskontorets kundcenter kan du be att få ta del av det som finns för din fastighet.",
       "Plan- och bygglagens förbud mot att förvanska en särskilt värdefull byggnad gäller även om ändringen inte kräver bygglov, påpekar staden. Boverket lägger till att förbudet gäller vid alla ändringar, såväl exteriört som interiört. En bevarad tapet, en målad bård eller en väggbeklädnad från husets byggtid kan alltså vara en del av det som ska tas om hand.",
     ],
     "aside": {"title": "Ta reda på först", "items": [
       "Finns huset i en inventering?", "Ligger det i ett utpekat område?", "Är det byggnadsminne?", "Vilka tapeter sitter kvar?"]}},
    {"id": "varsamt-lidingo", "h2": "Varsamt betyder att utgå från det som finns",
     "paras": [
       "Staden beskriver varsamhet med några enkla råd: utgå från de karaktärsdrag och värden som just din byggnad har, underhåll befintliga material hellre än att byta, och låt det nya anpassa sig till husets stil och till vad som var typiskt när det byggdes. För en tapetsering kan det betyda att en gammal tapet lagas och får sitta kvar i ett rum, medan ett annat får nytt.",
       "Ska det gamla bytas ut tar vi vara på en bit innan det rivs. Kulturen i Lund skriver att det går att få tag på äldre originaltapeter eller beställa handtryckta tapeter efter ett eget original. Är huset kulturhistoriskt särskilt värdefullt kan du enligt staden söka byggnadsvårdsbidrag hos länsstyrelsen.",
       "Ön har nio byggnadsminnen, bland dem flera villor och radhusen på Canadastigen. De skyddas av kulturmiljölagen, och det är länsstyrelsen som hanterar tillstånd för förändringar av dem.",
     ],
     "aside": None},
    {"id": "gasthus-lidingo", "h2": "Gästhuset som står kallt på vintern",
     "paras": [
       "Svenska Byggnadsvårdsföreningen skriver att alla täta, vattenavvisande skikt under vissa omständigheter kan ställa till problem i gamla hus. I ett hus som i övrigt inte är diffusionstätt kan fukt som vandrar genom väggen hindras och samlas vid det täta skiktet. Om huset värms upp året runt är ett tätt skikt på insidan inget problem, men om det kallställs på vintern kan fukt anrikas bakom det.",
       "Står ett gästhus, en sommarstuga eller ett uthus på tomten ouppvärmt delar av året väljer vi därför ytskikt som släpper igenom fukt. Föreningen nämner limfärgstapeter, lerklining och diffusionsöppna färger som alternativ till täta tapeter. I villan som värms hela året är valet friare.",
     ],
     "aside": {"title": "Öppna alternativ", "items": [
       "Limfärgstapet", "Lerklining", "Diffusionsöppen färg"]}},
    {"id": "panel-lidingo", "h2": "Tapet på panel och timmer",
     "paras": [
       "I ett äldre trähus kan tapeten sitta på papp som spänts över brädor eller timmer. Byggnadsvårdsföreningen skriver att spännpapp blev ett vanligt underlag för tapeter under 1800-talet och fungerar utmärkt på panel, och att den ger en mer levande yta än gips. På spänd papp kan tapeten bilda veck i hörnen som behöver justeras efter några år.",
       "Har pappen eller tapeten släppt i ett hörn går det att laga i stället för att byta, och därför är det klokt att spara den överblivna tapeten. Om huset utanpå behöver ny färg finns det mer under " + _L.format("malare-lidingo.html", "målare på Lidingö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen till på Lidingö",
  "steps": [
    ("Platsbesök", "Vi tittar på husets ålder, vad som sitter på väggarna och om huset värms hela året."),
    ("Underlag om huset", "Du tar fram inventering eller områdesbeskrivning från staden om det finns."),
    ("Skriftligt kostnadsförslag", "Lagning av gammal tapet, nedtagning och ny tapet redovisas var för sig."),
    ("Underarbete", "Spännpapp fästs eller byts, väggar lagas och grundas där det behövs."),
    ("Uppsättning", "Tapeten sätts upp med klister som passar underlaget."),
    ("Rester och prov", "Överbliven tapet och en bit av den gamla lämnas till dig."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering på Lidingö",
  "rot": [
    "I ett småhus räknar Skatteverket tapetsering som rotarbete, liksom att måla väggar, tak och golv. Avdraget gäller även i bostadsrätt och ägarlägenhet.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Lidingö?",
  "price": [
    "Om gammal tapet ska lagas eller tas ner, om spännpappen behöver förnyas och hur många rum det gäller väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan mitt hus på Lidingö vara värdefullt fast det inte finns i kulturmiljöprogrammet?",
     "Ja. Staden skriver att programmet pekar ut områden, inte varje byggnad, och att det finns särskilt värdefulla byggnader som inte beskrivs i det. Kundcenter kan berätta vad som finns om just din fastighet."),
    ("Gäller förvanskningsförbudet även tapeterna inne i huset?",
     "Boverket skriver att förbudet gäller vid alla ändringar, såväl exteriört som interiört, även när inget lov krävs."),
    ("Vilken tapet passar i ett gästhus som inte värms på vintern?",
     "Ett öppet ytskikt, till exempel en limfärgstapet, lerklining eller en diffusionsöppen färg. Täta tapeter kan samla fukt bakom sig om huset kallställs."),
    ("Kan man få bidrag för att bevara gamla tapeter?",
     "Är huset kulturhistoriskt särskilt värdefullt kan du enligt Lidingö stad söka byggnadsvårdsbidrag hos länsstyrelsen."),
    ("Går det att tapetsera direkt på panelväggen?",
     "Ofta spänns papp över panelen först. Spännpappen ger ett underlag som Byggnadsvårdsföreningen beskriver som utmärkt på panel."),
  ],
  "sources": [
    _LID_FAQ, _BOV_FORV, _KULT, _SBF_TAT, _SBF_MOD, _SBF_MAK, _SBF_UND, _SBF_SPANN, _SKV, _SKV2,
  ],
  "cta": ("Ska villan på Lidingö få ny tapet?", "Boka ett gratis platsbesök, så går vi igenom husets väggar och vad som är värt att spara innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nytapetserat sovrum i en äldre trävilla med ljusblå tapet och vitmålad panel",
     "empty bedroom in an early 1900s Swedish wooden villa, walls freshly papered with a pale blue wallpaper with a small repeating leaf pattern above a white painted wooden wainscot, white window with mullions and a glimpse of pine trees outside, wide painted floorboards, soft daylight, no furniture, no people, no text, no letters"),
    ("Spännpapp uppspikad över en panelvägg, redo för tapet",
     "close-up of an interior wooden board wall in an old Swedish house covered with stretched brown spännpapp backing paper fixed with small tacks along the edges, a roll of the same paper and a tack hammer on the floor, natural window light, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HÄSSELBY
"tapetsering-hasselby.html": {
  "kind": "district", "service": "tapetsering", "ort": "Hässelby", "svc_label": "Tapetsering",
  "title": "Tapetsering i Hässelby – grupphus, gips och villastad",
  "description": "Tapetsering i Hässelby: ny tapet i grupphus och villor – gipsväggar med oförlimmade spacklingar, gamla lager, glasverandan och tapet i ouppvärmda rum.",
  "h1": "Tapetsering i Hässelby",
  "lead": "I Hässelby villastad står äldre trävillor och tätare småhusgrupper från 1960- och 1970-talen sida vid sida, och väggarna inne skiljer sig lika mycket som husen utanpå. Geal Entreprenad AB tapetserar i radhus, kedjehus och villor i Hässelby, och underarbetet väljer vi efter väggen.",
  "card": "Ny tapet i grupphus och villor.",
  "sections": [
    {"id": "husen-hasselby", "anchor": "Husen",
     "h2": "En villastad som fick grupphus",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden beskriver villastäderna som privat organiserade områden med individuellt utformade hus, där trä var det vanligaste fasadmaterialet och glasverandor, takkupor och snickarglädje gav variation. Under 1960- och 1970-talen ersattes många villor i Hässelby villastad av täta, stora och sammanhållna grupper av enhetlig småhusbebyggelse.",
       "Stadsdelen är fortfarande främst småhus. Enligt områdesfakta 2025 finns 7 029 bostäder i Hässelby villastad, varav 5 009 i småhus. Av bostäderna är 4 757 äganderätter, så det är oftast husägaren själv som bestämmer vad som ska upp på väggarna.",
       "Vägledningen beskriver också hur villastäderna har förtätats genom att tomter delats av, och att radhus, parhus och mindre flerfamiljshus har byggts både inom och intill den ursprungliga bebyggelsen. Olika tidsepoker finns alltså representerade på samma gata, och det gäller också väggarna inne: en äldre trävilla, ett grupphus och ett nyare hus kan kräva var sitt underarbete.",
     ],
     "aside": {"title": "Hässelby villastad, bostäder 2025", "items": [
       "7 029 bostäder", "5 009 i småhus", "4 757 äganderätter"]}},
    {"id": "gips-hasselby", "h2": "Gipsväggen och spacklingarna",
     "paras": [
       "Svenska Byggnadsvårdsföreningen räknar gipsskivor, betong och puts som lämpliga underlag för tapet i nyare hus. Är väggen av gips med ett enda lager gammal tapet är det enligt föreningen ingen fara att sätta ny ovanpå. Det känsliga är spacklingarna på skivorna, som oftast inte är förlimmade.",
       "Föreningen beskriver ett sätt att lösa det: stryk väggen med utspätt tapetklister, hälften stärkelseklister och hälften vatten, och låt det torka innan den nya tapeten sätts upp.",
       "Ska de gamla lagren bort helt går det att lösa upp dem med vatten. Kulturen i Lund skriver att den som blöter upp ett tapetsjok kan skilja de olika lagren från varandra, och ibland följa modets växlingar bakåt genom åren.",
     ],
     "aside": {"title": "Före ny tapet på gips", "items": [
       "Ta bort lösa rester", "Laga och slipa spacklingar", "Förlimma med utspätt klister", "Låt torka"]}},
    {"id": "vinyl-hasselby", "h2": "Sjuttiotalets tapeter och dagens val",
     "paras": [
       "Kulturen i Lund skriver att vinyltapeten slog igenom på allvar på 1970-talet, med en yta av pvc-plast som var lättskött och hållbar. Tapeter i starka färger med stora medaljongmönster ersatte då 1960-talets färglösa tapeter med svaga mönster. Sitter det en tät tapet kvar sedan dess tar vi ner den innan väggen förlimmas.",
       "Byggnadsvårdsföreningen beskriver non-woventapeter som plastbehandlade och täta. I ett hus som värms upp året runt är ett tätt ytskikt på insidan inget problem enligt föreningen, så i ett grupphus som värms hela året är valet friare. I de äldre villorna kan underlaget vara ett annat. Föreningen skriver att dålig vidhäftning kan befaras i hus från 1920–1950-talen, där väggarna behandlades med lim och krita, och att sandspackel kom vid mitten av 1950-talet. Där provar vi väggen innan vi bestämmer hur den ska förberedas. Mer om målning av fasad och snickerier i stadsdelen finns under " + _L.format("malare-hasselby.html", "målare i Hässelby") + ".",
     ],
     "aside": None},
    {"id": "veranda-hasselby", "h2": "Glasverandan och andra kalla rum",
     "paras": [
       "En glasveranda som inte värms på vintern är ett annat rum än vardagsrummet. Byggnadsvårdsföreningen påpekar att fukt kan anrikas bakom ett tätt skikt om huset kallställs, och att det kan bildas mögel under ett tätt ytskikt om huset står ouppvärmt periodvis. Där väljer vi hellre en papperstapet med stärkelseklister än en tät non-woventapet. Vi frågar därför hur rummet används under året innan tapeten beställs, och planerar ni att värma verandan längre fram kan tapetvalet vänta tills det är bestämt.",
       "Det gäller också rum där luftfuktigheten blir hög. Föreningen skriver att tapeter kan användas på många underlag, bara inte luftfuktigheten blir för hög, som den kan bli i kök och badrum.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen till i Hässelby",
  "steps": [
    ("Platsbesök", "Vi ser vilket underlag väggen har och om rummet värms hela året."),
    ("Skriftligt kostnadsförslag", "Nedtagning, förlimning och uppsättning redovisas som egna poster."),
    ("Nedtagning", "Gamla tapeter blöts upp och tas ner där det behövs."),
    ("Förlimning", "Spacklingar lagas och slipas, och väggen stryks med utspätt klister."),
    ("Uppsättning", "Tapeten sätts upp våd för våd, och skarvarna trycks till."),
    ("Genomgång", "Vi går igenom rummen med dig och lämnar överbliven tapet för framtida lagningar."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Hässelby",
  "rot": [
    "Skatteverket räknar tapetsering som rotarbete i ett småhus, och samma sak gäller i bostadsrätt och ägarlägenhet.",
    _ROT_SUM + " Geal drar av avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Hässelby?",
  "price": [
    "Hur många lager som ska ner, hur mycket spackling väggarna behöver och hur stora ytorna är styr mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag. Ska flera rum göras räcker ett besök för hela huset, och vill du ha samma tapet i flera rum räknar vi på antalet rullar för alla rum samtidigt.",
  ],
  "faq": [
    ("Kan ny tapet sättas direkt på gipsväggen i vårt radhus?",
     "Oftast, men spacklingarna i skarvarna behöver förlimmas så att tapeten fäster jämnt. Vi stryker med utspätt klister och låter det torka."),
    ("Hur får man ner gammal tapet från 1970-talet?",
     "Pappersbaserade lager kan gå att blöta upp, men hur det går beror på tapettypen. Vi provar på en liten yta först."),
    ("Kan vi tapetsera glasverandan?",
     "Ja, men värms den inte på vintern väljer vi hellre papperstapet med stärkelseklister än en tät tapet. Fukt kan annars samlas bakom tapeten."),
    ("Fungerar non-woven i ett hus som värms hela året?",
     "Ja. Byggnadsvårdsföreningen skriver att ett tätt skikt på insidan inte är något problem om huset värms upp året runt."),
    ("Vad är förlimning?",
     "Att stryka väggen med utspätt tapetklister och låta det torka innan tapeten sätts upp. Byggnadsvårdsföreningen föreslår hälften stärkelseklister och hälften vatten."),
  ],
  "sources": [
    _VARSAM, ("Stockholms stad – Områdesfakta 2025: Hässelby villastad (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-villastad.pdf"),
    _SBF_UND, _SBF_GIPS, _SBF_MOD, _KULT, _SKV, _SKV2,
  ],
  "cta": ("Ska huset i Hässelby få ny tapet?", "Boka ett gratis platsbesök, så går vi igenom väggarna och rummen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nytapetserat rum i ett radhus från 1970-talet med grafisk tapet på en vägg",
     "empty living room in a 1970s Swedish terraced house, one feature wall freshly papered with a calm green wallpaper with a large round retro pattern, other walls white, light wooden floor, wide window with a view of a small garden hedge, soft daylight, no furniture, no people, no text, no letters"),
    ("Gipsvägg med slipade spacklingar i skarvarna och en roller med klister",
     "close-up of a plasterboard interior wall with sanded white filler along the joints and screw holes, a paint roller with diluted wallpaper paste resting on a tray on a dust sheet, half of the wall darker where it is still wet, natural light, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SPÅNGA
"tapetsering-spanga.html": {
  "kind": "district", "service": "tapetsering", "ort": "Spånga", "svc_label": "Tapetsering",
  "title": "Tapetsering i Spånga – tapet efter villans epok",
  "description": "Tapetsering i Spånga: Solhem, Bromsten, Flysta och Sundby – tapet som passar husets tid, spännpapp och lumppapp, torrt underlag och lagning.",
  "h1": "Tapetsering i Spånga",
  "lead": "I Spångas villastäder står hus från många årtionden på samma gata, och en tapet som passar i en villa från 1910-talet kan se fel ut i ett hus från 1950-talet. Geal Entreprenad AB tapetserar i villor, radhus och lägenheter i Spånga, och vi hjälper dig både med underlaget och med att välja en tapet som hör till huset.",
  "card": "Tapet som passar husets tid.",
  "sections": [
    {"id": "villastader-spanga", "anchor": "Villastäderna",
     "h2": "Solhem, Bromsten, Flysta och Sundby",
     "paras": [
       "Stadens vägledning Varsam utveckling av småhus- och villaområden räknar Bromsten, Nälsta, Solhem, Flysta och Sundby till villastäderna. De växte fram kring järnvägen, och på 1910-talet fick bland annat Spånga status som municipalsamhälle med egen administration. I Solhem fick bara en tiondel av tomten bebyggas, och vägledningens tabell markerar Solhem som kulturhistoriskt värdefull miljö. Närmast stationerna och längs huvudgatorna byggdes tätare, med flerbostadshus.",
       "Det märks i siffrorna. I områdesfakta 2025 har Solhem 3 470 bostäder, varav 2 038 i småhus och 1 946 äganderätter. Bromsten har 3 826 bostäder, och där ligger 2 735 i flerbostadshus och 1 066 i småhus.",
     ],
     "aside": {"title": "Bostäder 2025", "items": [
       "Solhem: 3 470, varav 2 038 i småhus", "Bromsten: 3 826, varav 2 735 i flerbostadshus"]}},
    {"id": "epoken-spanga", "h2": "En tapet som hör till husets tid",
     "paras": [
       "Vägledningen beskriver villastäderna som områden med individuellt utformade hus från olika tidsepoker. Kulturen i Lund visar hur tapeterna växlade: jugendstilens slingrande växtmönster i början av 1900-talet, den melerade beige ”havregrötstapeten” som blev populär i slutet av 1930-talet, fondtapeter med djärvare mönster på 1950-talet och starka färger med stora medaljonger på 1970-talet.",
       "I dag har flera tillverkare tagit upp äldre mönster i sina kollektioner, skriver Kulturen. Har huset kvar en bit av en tidigare tapet, bakom en list eller i en garderob, kan den visa vad som satt där. Vägledningen påpekar att förändringar i de villastäder som är kulturhistoriskt värdefulla, som Solhem, behöver visa hänsyn till de värdena.",
       "Gäller frågan fasadens kulör eller fönstren utanpå finns det mer under " + _L.format("malare-spanga.html", "målare i Spånga") + ".",
     ],
     "aside": {"title": "Tapeter genom 1900-talet", "items": [
       "Tidigt 1900-tal: jugend med växtmönster", "Sent 1930-tal: melerad beige", "1950-tal: fondtapeter", "1970-tal: starka färger"]}},
    {"id": "underlag-spanga", "h2": "Papp på väggen och ett torrt underlag",
     "paras": [
       "I äldre villor sitter tapeten ofta på papp. Svenska Byggnadsvårdsföreningen beskriver spännpapp som ett traditionellt underlag som blev vanligt under 1800-talet. Ett annat är lumppapp. När en målare klistrat upp lumppapp på nylagd lerputs och den sedan satt helt lös, svarade föreningen att underlaget troligen inte varit tillräckligt torrt eller inte förlimmats, och att kyla kan ställa till det om det är fuktigt när arbetet görs.",
       "Därför tapetserar vi inte på en nyputsad eller nyspacklad vägg innan den torkat, och vi vill att huset är uppvärmt medan klistret binder. Mitt i en renovering, när värmen är avstängd, väntar vi hellre några dagar.",
       "Pappen behöver inte nödvändigtvis tapetseras. Byggnadsvårdsföreningen skriver att spännpapp fungerar utmärkt på panel som underlag både för tapeter och till exempel för limfärg, och Riksantikvarieämbetet nämner papp, makulerad juteväv, trä och puts bland de underlag limfärg kan målas på. I ett rum där en målad vägg passar huset bättre kan det vara ett alternativ till tapet.",
     ],
     "aside": None},
    {"id": "lagning-spanga", "h2": "När en pappspänd tapet släpper",
     "paras": [
       "En tapet på spänd papp kan släppa i ett hörn. Byggnadsvårdsföreningen beskriver hur det lagas: skär upp en bit ut från hörnet och fukta baksidan, spika tillbaka pappen i kanterna, klistra remsor och klistra tapeten över. För det behövs tapet att laga med, och därför råder föreningen den som väljer en äldre typ av tapet att köpa en extra rulle.",
       "Titta också efter tecken på fukt innan något nytt sätts upp. Föreningen skriver att hög fuktighet i äldre hus och oeldade sommarhus brukar skada papperstapeter långsamt, och att det syns som lösa skarvar, fuktfläckar och svarta prickar. Då letar vi efter orsaken innan vi tapetserar.",
       "Bor du i en bostadsrätt i Bromsten eller vid stationen behöver du normalt inte styrelsens tillstånd för ny tapet. Bostadsrättslagen 7 kap. 7 § räknar i stället upp ingrepp i bärande konstruktion, ändrade ledningar och ventilation och andra väsentliga förändringar.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går tapetseringen till i Spånga",
  "steps": [
    ("Platsbesök", "Vi ser hur gammalt huset är, vad som sitter på väggarna och om underlaget är torrt."),
    ("Val av tapet", "Vi letar efter rester av äldre tapeter och går igenom mönster som passar huset."),
    ("Skriftligt kostnadsförslag", "Lagning, underlag och uppsättning står som egna poster."),
    ("Underlag", "Spännpapp eller lumppapp fästs, väggen förlimmas och får torka i ett varmt hus."),
    ("Uppsättning", "Tapeten sätts upp, och en extra rulle sparas för lagningar."),
  ],
  "rot_h2": "ROT-avdrag för tapetsering i Spånga",
  "rot": [
    "Att tapetsera räknas som rotarbete hos Skatteverket, i villan likaväl som i en bostadsrätt eller ägarlägenhet. I bostadsrätten ska arbetet göras innanför bostadens tak, väggar och golv.",
    _ROT_SUM + " Avdraget dras direkt på Geals faktura.",
  ],
  "price_h2": "Vad påverkar priset i Spånga?",
  "price": [
    "Om väggen behöver nytt pappunderlag, hur mycket som ska lagas och hur svår tapeten är att passa påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken sorts tapet passar i en villa från 1930-talet i Spånga?",
     "Kulturen i Lund beskriver den melerade beige ”havregrötstapeten” som populär i slutet av 1930-talet. Finns en rest av den ursprungliga tapeten kvar är den den bästa ledtråden."),
    ("Varför släpper papp som klistrats på en nyputsad vägg?",
     "Enligt Byggnadsvårdsföreningen beror det troligen på att underlaget inte var tillräckligt torrt eller inte förlimmat, eller på kyla och fukt när arbetet gjordes."),
    ("Kan en pappspänd tapet som släppt i hörnet lagas?",
     "Ja. Man skär upp en bit, fuktar baksidan, spikar tillbaka pappen, klistrar remsor och sätter tapet över."),
    ("Varför ska man spara en extra rulle tapet?",
     "Äldre typer av tapeter kan försvinna ur sortimentet. En extra rulle gör det möjligt att laga senare."),
    ("Kan ni tapetsera medan resten av villan renoveras?",
     "Ja, men vi väntar tills väggarna är torra och huset uppvärmt, så att klistret binder ordentligt."),
  ],
  "sources": [
    _VARSAM,
    ("Stockholms stad – Områdesfakta 2025: Solhem (pdf)", _OF + "vasterort/jarva/solhem.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Bromsten (pdf)", _OF + "vasterort/jarva/bromsten.pdf"),
    _KULT, _RAA, _SBF_MAK, _SBF_LUMP, _SBF_SPANN, _SBF_UND, _BRL, _SKV, _SKV2,
  ],
  "cta": ("Ska villan i Spånga få ny tapet?", "Boka ett gratis platsbesök, så tittar vi på väggarna och husets tid innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nytapetserat rum i en villa från 1930-talet med melerad beige tapet",
     "empty room in a 1930s Swedish villa, walls freshly papered with a plain mottled warm beige wallpaper, white painted door with simple panels, window with white frame and a view of a garden apple tree, light pine floorboards, soft daylight, no furniture, no people, no text, no letters"),
    ("Tapetrullar, en tapetborste och en sax på ett tapetbord i ett tomt rum",
     "a long wooden wallpaper pasting table in an empty room with two unopened wallpaper rolls in a muted floral pattern, one roll unrolled with its plain back side up, a wide pasting brush, a smoothing brush and long scissors, a bucket on the floor, natural daylight, no people, no hands, no text, no letters"),
  ],
  "related": [],
},

}
