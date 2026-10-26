# -*- coding: utf-8 -*-
"""Fasadmålning – ortsidor v20: Sigtuna, Sollentuna, Tyresö, Upplands Väsby, Vallentuna, Värmdö (2026-10-26).
Deltjänst under malare.html (TJ_HUB["fasadmalning"]). Intent: utvändig målning av villan – färgtyp, färglager,
förarbete och lov – skild från ortens malare-<ort>.html (kulörhistorik, lov i stort, ute och inne),
fasadrenovering-<ort>.html (byte och lagning av fasadmaterial, isolering), från v15/v17-sidorna (kulörval,
kalkfärg, väder och torktider, nytt trä, underhållscykler, bidrag, uthus och plåt, redargårdar) och från
byggtorg.se/fasadmalning-sollentuna/ och -varmdo/ (dagvatten, farligt avfall, återvinningscentraler, SCB-tal,
Långvik/Sandhamn/Lindalssundet/Norra Stavsudda/Norra Kopparmora).
Lokal vinkel per sida:
Sigtuna – gatufasad, gårdsfasad och uthus i stadskärnan: oljemålad panel mot gatan och rödfärgad gårdssida,
statusskillnader, ommålningscykel, NCS-koder ur stadens provtagningar, plåt och panelbredder;
Sollentuna – ny kulör i villastaden: kulturmiljöplanens villastäder i ÖP, lovplikt och vad ansökan ska innehålla
(situationsplan, fasadritning/fotomontage, kontrollplan), färglager på villor från 1900-talets första hälft;
Tyresö – fritidshusen på Brevikshalvön som blivit helårshus: färglager 1930–60-tal, plastfärg på panelen och hur
den tas bort, detaljplanens färgbestämmelser och kommande planetapper, ROT vid uthyrning;
Upplands Väsby – sekelskiftesvillorna längs Gamla vägen i Bollstanäs: kontrastmålad panel, verandor och
frontespiser, putsade socklar, uthus, staket och lov i särskilt värdefullt område;
Vallentuna – småhusen i Lindholmen från 1970-talet och framåt: asbest i fönsterkitt och puts före skrapning,
täta färgskikt, äganderätt kontra bostadsrätt vid ROT, antikvarisk expertis och lov;
Värmdö – skärgårdsbyarna Gällnö, Hjälmö, Lådna och Harö: röd panel och vita snickerier (två färgtyper), båthus och
bodar, fabriksblandad slamfärg, bryggor utan ROT, lovplikt i riksintressena.

Fakta endast från källorna i respektive 'sources', öppnade med curl och lästa 2026-10-26 (pdf med textlager):
  Sigtuna kommun (Bevarande- och förnyelseplan för Sigtuna stad, antagen 2019, pdf: färgsättningstraditionen
  s. 49–51 – provtagningar på ett tjugotal fasader, brandförsäkringar och målningar, skeden som följer
  ommålningscykeln på cirka 20 år, oljemålad panel förbehållen gatufasaden och synliga gavlar, gårdsfasader och
  uthus rödfärgade in i sen tid, rödfärgade hus ej undersökta, status (ägare, storlek, användning, läge), skillnad
  norra/södra Stora gatan, enklare hus söder om gatan och på Malmen tar över färgsättningen efter 10–20 år,
  1880–90-tal samma färg på fasad och knutar lika vanligt som avvikande, fönster ofta mörkbruna, Gamla tvåan
  (Humlegården 13) röd slamfärg, ockra på spröjs, grön umbra eller grönjord på foder, Malmgården 2030-Y30R och
  4005-G50Y som Geijersgården i Uppsala, NCS-beteckningarna ungefärliga; Ombyggnad s. 44–46 – enkla bebyggelsen
  utan plåtdetaljer från början, plåttäckning vanligare i slutet av 1800-talet, plåtklädda vindskivor modern
  företeelse, äldre utseende förebild vid byte, gammal panel sällsynt, olika brädbredder behålls; Bygga i
  kulturmiljö: lov även för annars lovbefriad fasadändring i särskilt värdefulla miljöer, foton från alla
  väderstreck för bedömning),
  Sollentuna kommun (Fasadändring för en- eller tvåbostadshus: definition, oftast inget lov, radhus/kedjehus
  beroende på utformning, lov i kulturhistoriskt värdefullt område/byggnad, byggherrens ansvar, detaljplaners
  materialbestämmelser, frivilligt lov, foton från samtliga väderstreck, handlingar – e-tjänst, kontrollplan,
  situationsplan på tomtkarta 1:400, fasadritning/fotomontage, fasadritning 1:100 med befintlig och ny fasad,
  äldre ritningar i bygglovsarkivet utan kostnad, markera åtgärden för handläggare och grannar; Kulturhistoriska
  byggnader och områden: lovbefriade åtgärder går inte att tillämpa, lager i detaljplanekartan, värdefull även
  utanför planen; Översiktsplan med sikte på 2040, pdf: villastaden från 1900-talets första hälft, robust
  struktur, kulturmiljöplan 1993 rev. 2012 med tillägg 2002, Norrvikens villastad, Väderholmen, Skansen –
  avstyckning och förtätning tillåts inte, Edsvikens villastad – bara där gatumiljön inte förändras),
  Tyresö kommun (Strategi för Östra Tyresö – Brevikshalvön, Solberga, Raksta och Bergholm, pdf från tyreso.se:
  första sommarvillorna runt Breviksmaren för drygt 100 år sedan, 1930–50-talen avstyckning för fritidshus,
  fritidshus från 1930–60-talen på Brevikshalvön, små byggrätter i avstycknings- och byggnadsplaner,
  permanentbosättningen ökar, cirka 3 300 invånare varav 2 400 i Brevik, värdefulla kulturmiljöer bl.a.
  Breviksnäs och Ällmora fritidshusområde, kommande detaljplaneetapper ska beskriva kulturmiljöns karaktär,
  särskilda bestämmelser om fasadmaterial, tak eller färgsättning; Måla om huset: inget lov inom detaljplan för
  en- och tvåbostadshus, komplementbyggnad, komplementbostadshus, utökad lovplikt för kulturhistoriskt
  värdefulla byggnader, detaljplan kan reglera färger och fasadmaterial, webbkartan – planer och bestämmelser),
  Upplands Väsby kommun (Kunskapsunderlag för kulturmiljö, pdf: Bollstanäs – Gamla vägen s. 159–162 – höjd längs
  bergsslänt mot Norrviken, stickgator, sjöbodar och bryggor, villor från sekelskiftet 1900, framsida mot vägen,
  höga putsade socklar, ca två våningar, verandor, gavlar och balkong mot gatan, panel i kontrast i vitt, gult
  eller rödfärg, putsade hus förekommer, staket och grindar, särskilt värdefullt enligt PBL 8 kap. 13 §,
  egnahemsrörelsen, bevarandevärda karaktärsdrag frontespiser, verandor, enkla äldre uthus, vägledning kulörval
  anpassas; Fasadändring: definition, ny färg utan lov för en- och tvåbostadshus och komplementbyggnader, lov kan
  krävas i särskilt värdefullt område om karaktären ändras, varsamhet oavsett lovplikt),
  Vallentuna kommun (Fördjupad översiktsplan för norra Vallentuna och Lindholmen, pdf: Lindholmen
  stationssamhälle kring Roslagsbanan, bebyggelse huvudsakligen sedan 1970-talet, villor och gruppbyggda
  småhus, senast Kulla, medeltida sätesgården; kulturmiljöprogrammet – antikvarisk expertis anlitas i ärenden
  som berör exempelområden, Lindholmen höga kulturhistoriska kvaliteter, mycket höga i nordvästra delen med
  fornlämningar, hänsyn till skala och bebyggelsemönster; Fasadändring: inget lov för ommålning av en- och
  tvåbostadshus, lov i kulturhistoriskt särskilt värdefullt område/byggnad, handlingar – situationsplan,
  fasadritning 1:100, kulörer med NCS-koder, kontrollplan, äldre ritningar ur arkivet),
  Värmdö kommun (Värmdö – Kulturhistoria i skärgårdsbygd, kommunens kulturmiljöprogram med Stockholms läns
  museum 2014, pdf: Gällnö by – största i Svartsöarkipelagen, sluttningen mot Hemfladen, bostadshus för sig med
  lövträd och syrenbersåer, uthus i utkanten, båthus vid hamnen, de flesta husen rödmålade med snickeridetaljer i
  vitt, en- eller tvåkupigt tegel, glasade verandor med enkel snickarglädje, enkelstuga daterad 1815; Hjälmö och
  Lådna – de flesta husen kring 1900, parstugor revs för hus med verandor, panel rödmålad med vita
  snickeridetaljer; Karklö – båthus vid hamnen, faluröda bostads- och ekonomibyggnader; Harö – ångbåt först på
  1920-talet, äldre folklig byggnadskultur, två parstugor mot Byviken, sjöbodar och bryggor, faluröd panel,
  varierande takmaterial, riksintresse, områdesbestämmelser med utökad lovplikt bör komma till stånd;
  Kulturmiljö och byggnadsvård: 14 riksintressen, bl.a. Husarö, Ingmarsö, Svartsö, Gällnö, Hjälmö och Harö;
  Bygglov vid fasadändring; Förändringar i PBL från 1 december 2025: lovplikt i riksintressen och kulturhistoriskt
  värdefulla områden, kulturmiljökartan),
  Riksantikvarieämbetet (Byggnadsmåleri med traditionella färgtyper, pdf: förord – linoljefärg, slamfärg och
  kalkfärg bland de vanligaste ännu på 1950-talet; linoljefärg dominerade på trähus till mitten av 1900-talet där
  rödfärg inte användes, fabriksblandad från 1930-talet, platstillredd till mitten av 1950-talet, stryks tunt,
  rund eller oval ytanstrykare ca 7 cm; underhållsmåleri på utsatta delar – fönster, vattbräder, trappor,
  räcken, utvändig utsmyckning; ommålning oftare på fönstersnickerier, vindskivor, sydfasader; sandblästring
  olämplig, varmluft skonsammare än bränning, låg antändningstemperatur; fönster sodatvättas för hand,
  kittfalsar grundas; slamfärg – matt, vattenspädbar, fuktgenomsläpplig, fäster bra på ohyvlat, sämre på
  hyvlat, skyddar till viss del träet, järnvitriol viss konserverande effekt, fabriksblandad med
  konserveringsmedel, kan behöva spädas, inte för tjockt, plafondpensel, tvål och vatten, produkter med andra
  bindemedel – latextillsatser, kulör skiljer mellan tillverkare, ommålning borstning–avdamning–en strykning,
  bara slamfärg på slamfärg; kalkfärg – öppen, god vidhäftning på kalkputs, dålig på förgipsade och cementrika
  underlag, övergång till kalkcementbruk vid mitten av 1900-talet),
  Länsstyrelserna i Gävleborgs, Västmanlands och Örebro län (Målning utomhus på trä, pdf: knutar och lister grå
  som sandsten, panel oljemålad som sten eller puts, färgtyper i lager – linoljefärg, alkydoljefärg, plastfärg,
  flagor/sprickor/blåsor, fackman; plastfärg bildar hinna som måste bort före linoljefärg, handskrapa,
  infravärme med brandrisk, kemiska medel undviks; blästring och maskinslipning skadar, högtryckstvätt olämplig,
  spara partier som sitter bra; jordpigment fram till 1950-talet, dovare skala under 1800-talets andra hälft,
  gråvitt, rosa och grönt, fönster mahognybruna eller mörkgröna, skrapa fram lager med vass kniv),
  Boverket (Fuktrisker med fasadens material och ytskikt: tät plastfärg på träpanel, akrylatfärg kräver
  alkydoljegrund som inte alltid användes; Risker med hantering av asbest: förbud inom byggsektorn 1982, främst
  byggnader 1940–1970, frågor och svar – 1940–1980 sannolikt asbest, fönsterkitt och puts bland exemplen,
  bunden form ingen fara, damm vid bearbetning, provtagning och analys enda säkra sättet, bygglovshandlingar),
  Skatteverket (Ger arbetet rätt till rotavdrag?: småhus inkl. fritidshus, komplementhus som garage och förråd
  kan höra till småhuset, arbete i bostaden eller på tomten i nära anslutning, måla fasader, byggnadsställning,
  inte staket och murar, inte reparation och underhåll av båtbryggor, bostadsrätt – inte gemensamma ytor som
  fasader; Så fungerar rotavdraget: 30 procent, 50 000/75 000 kr, äga bostaden, fritidshus, uthyrd del och
  fritidshus där någon annan bor permanent, flera ägare delar avdraget, material och resor ger inget avdrag).
Strukna (ej verifierade, oklara i källan eller medvetet utelämnade): Vallentunas kulturmiljöprogram och
kulturmiljöanalysen för Lindholmen (dok.vallentuna.se gick inte att nå 2026-10-26, vallentuna.se:s gamla
kulturmiljösidor ger 404 – programmet återges bara som FÖP:en citerar det); FÖP västra Vallentuna tätort
(öppnad, men handlar om ny bebyggelse – inte använd); Tyresös kulturmiljöprogram och den översiktliga
kulturmiljöinventeringen 2015 (ingen öppen pdf hittades – bara strategins sammanfattning används);
andelen permanentboende per delområde i Östra Tyresö (diagrammets ordning gick inte att läsa säkert ur pdf:en);
vilka färgtyper Breviks fritidshus faktiskt har (bara skrivet som möjlighet utifrån RAÄ); Sollentunas
handläggningstid och avgift för fasadlov (står på kommunens sida men utelämnat – inga avgifter/tider på sajten);
Sollentunas kulturmiljöplan från 1993 i sig (ingen öppen pdf – bara ÖP:ns hänvisning); att uthusen i Bollstanäs är
rödfärgade (underlaget säger det inte – skrivet villkorligt); vilken färgtyp de vita snickerierna i Värmdös byar
har (boken anger bara kulören – skrivet som vad vi kontrollerar); byggtorgs Värmdö-områden (Långvik, Sandhamn,
Lindalssundet, Norra Stavsudda, Norra Kopparmora) och Gustavsberg (malare-varmdo) – medvetet inte använda;
Sigtunas brandskyddskapitel och trädgårdsråd (inte målning); varumärken, priser, avgifter, tidsåtgång.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
Kritikpass 2026-10-26: alla 24 källor öppnade igen (curl, pdftotext) och varje faktamening kontrollerad mot
källtexten. Rättat: Sigtuna – "både panelen och kulörvalet hängde ihop med status" -> "förekomsten av oljemålad
panel och en del av skillnaderna i kulörval" (planens ordalydelse); linoljefärgens "täckande" (står i
Länsstyrelsens blad, inte RAÄ) ersatt med RAÄ:s "hellre flera tunna strykningar än få tjocka"; "aldrig varit
oljemålade" omskrivet (absolutord). Upplands Väsby – underlagets kulörråd gäller ny bebyggelse, nu skrivet så
("även ny bebyggelse bör anpassas i kulörval"); "många uthus är rödfärgade" struket (står inte i underlaget,
nu villkorligt "är uthuset rödfärgat"). Tyresö – Boverkets "inte alltid användes" omskrivet till "där den
grunden saknades". Värmdö – "flera har glasade verandor" -> "några" (programmet: "några av bostadshusen");
parstugorna på Hjälmö/Lådna -> "många äldre parstugor"; asbest-asiden "fogar kring dörrar" -> "dörrfogar"
(Boverkets lista). Sollentuna – Edsvikens villastad skrivet som ÖP:ns förtätningsregel, inte som allmän
ändringsregel; Sollentunas handläggningstid/avgift medvetet utelämnade. WARN kvar: inga för v20-sidorna.
Kritikpass 2 (extern) 2026-10-26: alla 21 käll-URL:er öppnade med curl (-L, Mozilla-UA), alla 8 pdf:er med
textlager (pdftotext); ingen källa 404, inloggning eller Wikipedia. Tyresö-strategin bytt från insynsverige till
kommunens egen pdf (tyreso.se/download/18.3e77c4cb165a8d8c344b7aff/..., samma text). Rättat: ROT – "30 procent"
-> "högst 30 procent" (Skatteverket); Sollentuna – "bo i det" -> "helt eller delvis bo i det", situationsplanen
visar "tomten och byggnaderna" (inte "huset"), lead "oftast" -> "kan"; Sigtuna – "kvarteret Humlegården" ->
"(Humlegården 13)" som i planen; Tyresö – lead "har ofta målats om" -> "kan ha", "när det byggdes om för
helårsboende" struket (står inte i källan), "Att ta bort all färg är ett stort arbete" struket, infravärme-FAQ
följer bladet ("följ instruktionerna noga"), FAQ "Ja." -> "Det kan den."; Upplands Väsby – "de delar som tar
mest tid" struket, aside "Underhålls löpande" -> "Utsatta delar" (vindskivor/sydfasad står under "ommålning
oftare"), sockeln "kräver en egen färgtyp" -> "är ett annat underlag", lovregeln utan villkoret "om karaktären
ändras" (kommunens sida anger både "alltid" och "kan krävas"), Gamla vägen "utpekad" -> "bedöms i
kunskapsunderlaget"; Vallentuna – lead "står inför ännu en ommålning" struket, "Många hus ... har målats med
täckfärger" -> "kan ha"; Värmdö – description "Harö" -> "Lådna" (vita snickerier anges inte för Harö), lead
"vita foder och knutar" -> "vita snickeridetaljer" (knutar nämns inte), Hjälmö/Lådna "De flesta bostadshusen",
aside tegel "på flera tak", Harö-kausaliteten (ångbåt -> byggnadskultur) delad i två påståenden som i programmet,
bildprompt utan "corner boards". Kontrollerat utan ändring: NCS 2030-Y30R/4005-G50Y, ~20 år, 10–20 år, 1:400/1:100,
1815, 3 300/2 400, Brevik/Breviksnäs/Ällmora, Bollstanäs–Gamla vägen–Norrviken, Lindholmen/Kulla, Gällnö/Hjälmö/
Lådna/Karklö/Harö/Byviken, Norrvikens villastad m.fl., 14 riksintressen, ROT-regler (uthyrning, fritidshus,
staket/murar/båtbryggor, bostadsrättens fasad, komplementhus).
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

_RAA = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf)",
        "https://www.raa.se/publicerat/9789172095830.pdf")
_LST_TRA = ("Länsstyrelserna i Gävleborgs, Västmanlands och Örebro län – Målning utomhus på trä (pdf)",
            "https://catalog.lansstyrelsen.se/store/23/resource/2000__14")
_BOV_YTA = ("Boverket – Fuktrisker med fasadens material och ytskikt",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/")
_BOV_ASB = ("Boverket – Risker med hantering av asbest i byggnader",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_SIG_BFP = ("Sigtuna kommun – Bevarande- och förnyelseplan för Sigtuna stad, antagen 2019 (pdf)",
            "https://www.sigtuna.se/download/18.6ed4dd301706254f993282/1582201854957/Bevarande-%20och%20f%C3%B6rnyelseplan%20f%C3%B6r%20Sigtuna%20stad,%20antagen%202019.pdf")
_SIG_KM = ("Sigtuna kommun – Bygga i kulturmiljö",
           "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html")
_SO_FASAD = ("Sollentuna kommun – Fasadändring för en- eller tvåbostadshus",
             "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/mala-om-en--och-tvabostadshus/")
_SO_KM = ("Sollentuna kommun – Kulturhistoriska byggnader och områden",
          "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/kulturmiljoer/")
_SO_OP = ("Sollentuna kommun – Översiktsplan för Sollentuna med sikte på 2040 (pdf)",
          "https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/oversiktsplan/oversiktsplan-for-sollentuna-med-sikte-pa-2040.pdf")
_TY_OSTRA = ("Tyresö kommun – Strategi för Östra Tyresö: Brevikshalvön, Solberga, Raksta och Bergholm (pdf)",
             "https://www.tyreso.se/download/18.3e77c4cb165a8d8c344b7aff/1538032923020/Strategi%20f%C3%B6r%20%C3%96stra%20Tyres%C3%B6.pdf")
_TY_MALA = ("Tyresö kommun – Måla om huset",
            "https://www.tyreso.se/boende--miljo/bygga/bygglovswebben/mala-om-huset.html")
_UV_KU = ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö i Upplands Väsby (pdf)",
          "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf")
_UV_FASAD = ("Upplands Väsby kommun – Fasadändring",
             "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/fasadandring")
_VAL_FOP = ("Vallentuna kommun – Fördjupad översiktsplan för norra Vallentuna och Lindholmen (pdf)",
            "https://vallentuna.se/download/18.63572f8619eeecafce08379/1782478384567/2.11.4%20F%C3%B6rdjupad%20%C3%B6versiktsplan%20Norra%20Vallentuna%20och%20Lindholmen.pdf")
_VAL_FASAD = ("Vallentuna kommun – Fasadändring",
              "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/behover-jag-bygglov/fasadandring")
_VD_KMP = ("Värmdö kommun och Stockholms läns museum – Värmdö: Kulturhistoria i skärgårdsbygd (pdf)",
           "https://www.varmdo.se/download/18.7faa473e19913ae5e0f1f12/1757318877718/Kulturmilj%C3%B6v%C3%A5rdsprogrammet%20V%C3%A4rmd%C3%B6_2.pdf")
_VD_KB = ("Värmdö kommun – Kulturmiljö och byggnadsvård",
          "https://www.varmdo.se/upplevaochgora/turist/kulturmiljoochbyggnadsvard.4.50cc920016fa8c77c58edccd.html")
_VD_FASAD = ("Värmdö kommun – Bygglov vid fasadändring",
             "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/bygglovvidfasadandring.4.1a14d9c818e5a4c406a626d.html")
_VD_PBL = ("Värmdö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
           "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/forandringaripblfrom1december2025.4.18b9914519a768a188a2872.html")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
            "tillsammans med rutavdrag. Färg, material och resor ger inget avdrag.")
_IMG_END = ", realistic photo, no people, no text, no letters"

PAGES_TJ = {

# ------------------------------------------------------------------ SIGTUNA
"fasadmalning-sigtuna.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Sigtuna", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Sigtuna – gatufasad, gårdsfasad och uthus",
  "description": "Fasadmålning i Sigtuna: oljemålad gatufasad och rödfärgad gårdssida, kulörer ur stadens provtagningar, plåt och panel vid ommålning och ROT.",
  "h1": "Fasadmålning i Sigtuna",
  "lead": "I Sigtunas gamla stadskärna har många hus två sidor som målades på olika sätt: en finare fasad mot gatan och en enklare mot gården. Geal Entreprenad AB målar om fasader, gavlar och uthus i Sigtuna och utgår från vad som redan sitter på varje vägg innan färgtyp och kulör bestäms.",
  "card": "Gatufasad, gårdsfasad och uthus i stadskärnan.",
  "sections": [
    {"id": "gatusidan-sigtuna", "anchor": "Gatan och gården",
     "h2": "Oljefärg mot gatan, rödfärg mot gården",
     "paras": [
       "Bevarande- och förnyelseplanen för Sigtuna stad beskriver hur stadens fasader har färgsatts, och den gör en tydlig skillnad mellan husets sidor. Den fina oljemålade panelen var som regel förbehållen gatufasaden och de gavlar som syntes. Många gårdsfasader förblev, liksom uthusen, rödfärgade långt in i sen tid. Planens färgundersökning handlar därför främst om fasaden mot gatan, och de hus som fortfarande är rödfärgade har inte undersökts, eftersom de inte har haft någon oljefärg att ta prov på.",
       "Ett och samma hus kan alltså bära två färgtyper som sköts olika. Enligt Riksantikvarieämbetets handbok om byggnadsmåleri ska linoljefärg strykas tunt, hellre i flera tunna lager än i få tjocka, medan röd slamfärg är matt, vattenspädbar och släpper igenom fukt. Slamfärgen fäster bra på ohyvlat virke men sämre på hyvlat. Vid platsbesöket går vi därför runt hela huset och bedömer gatusidan, gårdssidan och uthusen var för sig.",
     ],
     "aside": {"title": "Två sidor av samma hus", "items": [
       "Gatufasad – oljemålad panel", "Synliga gavlar – oljemålade",
       "Gårdsfasad – ofta rödfärgad", "Uthus – ofta rödfärgade"]}},
    {"id": "status-sigtuna", "h2": "Kulören följde husets ställning i staden",
     "paras": [
       "Enligt planen hängde förekomsten av oljemålad panel och en del av skillnaderna i kulörval ihop med byggnadens status, som ägare, storlek, användning och läge. Det fanns till exempel en skillnad mellan norra och södra sidan av Stora gatans centrala del. De enklare husen söder om gatan och på Malmen tog över de finare husens färgsättning först efter 10–20 år. Undersökningens indelning i skeden tycks dessutom följa den naturliga ommålningscykeln på ungefär 20 år.",
       "Under 1880- och 1890-talen var det lika vanligt att fasad och knutar hade samma färg som att knutarna avvek, och fönstren var ofta mörkbruna oavsett fasadfärg. Länsstyrelsernas blad om målning utomhus på trä ger en äldre bakgrund: inklädda knutar och lister målades grå med oljefärg för att likna sandsten, och panelklädda fasader oljemålades för att likna sten eller puts. Vilken lösning som hör till just ditt hus visar de gamla färglagren, och därför skrapar vi fram dem innan vi föreslår något.",
     ],
     "aside": None},
    {"id": "ncs-sigtuna", "h2": "Kulörer ur stadens provtagningar – som utgångspunkt",
     "paras": [
       "Planens underlag bygger på provtagningar på ett tjugotal bevarade fasader, uppgifter i brandförsäkringar och äldre målningar. För flera fastigheter anges kulörerna med NCS-koder. Gamla tvåan (Humlegården 13) är avfärgad med röd slamfärg på fasaderna, ockra på fönsterspröjsen och grön umbra eller grönjord på fönsterfodren. Malmgårdens gula fasad anges som 2030-Y30R och de grågröna listverken som 4005-G50Y, samma färgsättning som Geijersgården i Uppsala.",
       "Planen skriver samtidigt att NCS-beteckningarna är ungefärliga och att färgåtergivningen kan vara missvisande. Vi använder därför koderna som ett första förslag och jämför dem med lagren som kommer fram på ditt hus. På gårdssidan är det rödfärgen som ska stämma. Riksantikvarieämbetet påpekar att kulören kan skilja något mellan tillverkare, och att en slamfärgad yta bara ska målas om med slamfärg. När bara en del av en gårdsfasad bättras väljer vi därför samma färg som sitter där.",
     ],
     "aside": {"title": "Exempel ur planen", "items": [
       "Röd slamfärg – Gamla tvåan", "Ockra på fönsterspröjsen",
       "Grön umbra på fodren", "Malmgården – 2030-Y30R"]}},
    {"id": "plat-panel-sigtuna", "h2": "Plåt, panel och lov innan ställningen kommer upp",
     "paras": [
       "När ställningen ändå står uppe är det lätt att vilja byta detaljer. Planen skriver att den enkla bebyggelsen från början inte hade några plåtdetaljer, att plåttäckning blev vanligare i slutet av 1800-talet och att plåtklädda vindskivor är en modern företeelse. Vid byte av plåt bör det äldre utseendet vara förebild. Riktigt gammal träpanel kallas en sällsynthet som bör värnas, och eftersom gamla panelbrädor ofta har olika bredd bör den variationen finnas kvar när bräder byts. Vi målar därför vindskivorna i trä i stället för att klä in dem, och lagade partier får bräder i samma bredd som grannbrädorna.",
       "Kommunens sida om att bygga i kulturmiljö skriver att bygglov kan behövas även för åtgärder som annars är lovbefriade, till exempel fasadändring, om byggnaden eller området är särskilt värdefullt. Är du osäker kan du skicka foton på huset från alla väderstreck, så gör kommunen en bedömning. Om kulörbyte i stadskärnan och färgskalorna epok för epok kan du läsa under " + _L.format("malare-sigtuna.html", "målare i Sigtuna") + ", om puts och sockel under " + _L.format("fasadrenovering-sigtuna.html", "fasadrenovering i Sigtuna") + " och om målning i stort på sidan om " + _L.format("malare.html", "målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Sigtuna till",
  "steps": [
    ("Platsbesök", "Vi går runt huset och skiljer på gatufasad, gårdsfasad och uthus."),
    ("Skrapprov", "Små ytor skrapas fram för att se färgtyp och äldre kulörer."),
    ("Skriftligt kostnadsförslag", "Varje sida och färgtyp står för sig, så att du ser vad som ingår."),
    ("Förarbete", "Oljefärgen tvättas och skrapas, rödfärgen borstas fri från lös färg."),
    ("Strykning", "Linoljefärg i tunna lager och slamfärg i en strykning vid ommålning."),
    ("Genomgång", "Vi går igenom resultatet och skriver ner vilka kulörer som har använts."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Sigtuna",
  "rot": [
    "Skatteverket räknar målning av fasader i ett småhus som rotarbete, liksom att montera och montera ner byggnadsställningen. Komplementhus som förråd och andra mindre byggnader kan höra till småhuset, men målning av staket och murar ger inget avdrag.",
    _ROT_SUM + " Du ska äga huset medan arbetet utförs. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Sigtuna?",
  "price": [
    "Hur många sidor och byggnader som ska målas, om gatufasad och gårdssida har olika färgtyp, hur många knutar, foder och listverk som får egen kulör och hur mycket panel som behöver lagas väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför är gårdssidan rödfärgad när gatufasaden är oljemålad?",
     "Enligt Sigtunas bevarande- och förnyelseplan var den fina oljemålade panelen förbehållen gatufasaden och synliga gavlar. Gårdsfasader och uthus fick ofta behålla rödfärgen."),
    ("Kan NCS-koderna i Sigtunas bevarandeplan användas direkt när färgen beställs?",
     "De är en bra utgångspunkt, men planen skriver själv att beteckningarna är ungefärliga. Jämför dem med färglagren som skrapas fram på huset."),
    ("Ska knutarna ha samma kulör som fasaden på ett äldre hus i Sigtuna?",
     "Det varierar. Under 1880- och 1890-talen var det enligt planen lika vanligt med samma färg på fasad och knutar som att knutarna avvek."),
    ("Får vindskivorna kläs med plåt när huset ändå målas om?",
     "Bevarandeplanen beskriver plåtklädda vindskivor som en modern företeelse, och vid byte av plåtdetaljer bör det äldre utseendet vara förebild."),
    ("Ger det rotavdrag att måla uthuset på tomten?",
     "Komplementhus som förråd kan höra till småhuset enligt Skatteverket, och arbetet ska göras på tomten i nära anslutning till bostaden. Staket och murar ger inget avdrag."),
  ],
  "sources": [_SIG_BFP, _SIG_KM, _RAA, _LST_TRA, _SKV, _SKV2],
  "cta": ("Ska huset i Sigtuna målas om?", "Boka ett gratis platsbesök, så går vi igenom husets alla sidor innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre trähus i Sigtunas stadskärna med ljusgul oljemålad panel mot gatan och grågröna knutar",
     "old two-storey Swedish wooden town house in a historic small lake town street, street facade with light yellow oil painted vertical panel and grey green corner boards, dark brown window frames, gravel street with a low wooden fence, clay tile roof, early summer morning light" + _IMG_END),
    ("Gårdssida av ett gammalt trähus med matt rödfärgad panel och ett rödfärgat uthus på en innergård",
     "backyard side of an old Swedish wooden town house painted with matte red ochre slam paint, next to a small red ochre painted wooden outbuilding with a plank door, lilac bushes and grass in a small courtyard, soft daylight" + _IMG_END),
    ("Gavel med vindskiva i trä och stående panel med brädor i olika bredd under ett tegeltak",
     "close-up of the gable of an old Swedish wooden house with wooden barge boards and vertical oil painted pale yellow panel boards of slightly different widths, old red clay tile roof edge above, no metal flashing, clear sky" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SOLLENTUNA
"fasadmalning-sollentuna.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Sollentuna", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Sollentuna – ny kulör i villastaden",
  "description": "Fasadmålning i Sollentuna: villastäderna i kulturmiljöplanen, när ny kulör kräver lov, vad ansökan ska innehålla och färglager på äldre villor.",
  "h1": "Fasadmålning i Sollentuna",
  "lead": "Sollentunas äldre villastäder växte fram under första halvan av 1900-talet, och där kan en ny kulör bli en fråga för kommunen. Geal Entreprenad AB målar om villor i hela Sollentuna och tar fram kulörförslaget så att det fungerar både på väggen och i en ansökan om lov.",
  "card": "Ny kulör och lov i villastaden.",
  "sections": [
    {"id": "villastaden-sollentuna", "anchor": "Villastaden",
     "h2": "Villastäderna som kulturmiljöplanen pekar ut",
     "paras": [
       "Översiktsplanen skriver att Sollentuna ska bevara den prägel av villastad som växte fram under 1900-talets första hälft. Villastadsdelarna fick tidigt en fungerande struktur av gator och kvarter, som planen beskriver som robust och beständig trots senare avstyckningar. Riktlinjerna i kulturmiljöplanen, antagen 1993 och reviderad 2012, med ett tillägg från 2002, ska tillämpas. Där listas byggnader, områden och miljöer som är särskilt viktiga att värna.",
       "I Norrvikens villastad, Väderholmen och Skansen ska avstyckningar och förtätningar inte tillåtas, eftersom kulturmiljöplanen anger att områdenas karaktär ska behållas. I Edsvikens villastad bör de bara tillåtas där gatumiljöns karaktär inte förändras. Kommunen påpekar samtidigt att ett hus kan vara särskilt värdefullt även om det inte finns med i kulturmiljöplanen, och i kartan med gällande detaljplaner går det att tända ett lager som visar de områden planen omfattar.",
     ],
     "aside": {"title": "Nämns i översiktsplanen", "items": [
       "Norrvikens villastad", "Väderholmen", "Skansen", "Edsvikens villastad"]}},
    {"id": "lov-sollentuna-fasad", "h2": "När en ny kulör kräver bygglov",
     "paras": [
       "Kommunen definierar en fasadändring som att byggnaden byter kulör, fasadbeklädnad eller taktäckning, eller att dess yttre karaktärsdrag påverkas på annat sätt. På ett en- eller tvåbostadshus krävs oftast inget bygglov för det. Lov behövs däremot om fastigheten ligger inom ett kulturhistoriskt värdefullt område eller om huset i sig är kulturhistoriskt värdefullt, och inom sådana områden går de lovbefriade åtgärderna inte att använda. För radhus, kedjehus och andra sammanbyggda småhus beror det på hur bebyggelsen är utformad.",
       "Krävs inget lov ansvarar du ändå som byggherre för att ändringen passar husets och områdets karaktär och stämmer med detaljplanen, och vissa planer reglerar fasadmaterialet. Den som vill ha ett beslut på papper kan söka frivilligt bygglov. Kommunen kan också bedöma om huset ligger i ett värdefullt område utifrån foton från samtliga väderstreck och en beskrivning av vad som ska göras.",
     ],
     "aside": None},
    {"id": "ansokan-sollentuna", "h2": "Det här ska finnas med i ansökan",
     "paras": [
       "Kommunens checklista för fasadändring tar upp ansökan via e-tjänst, en situationsplan på tomtkarta, en fasadritning eller ett fotomontage och ett förslag till kontrollplan. Situationsplanen visar tomten och byggnaderna ovanifrån i skala 1:400, och den del som ändras ska markeras tydligt, både för handläggaren och för grannarna. Fasadritningen ska vara i skala 1:100 och visa både den befintliga och den nya fasaden, med fönster, dörrar och takkupor.",
       "Äldre ritningar på huset kan hämtas ur kommunens bygglovsarkiv utan kostnad och användas som grund. Vår del gäller själva målningen: vilken kulör panelen, knutarna, fodren och fönstren ska ha, och var på fasaden de olika kulörerna hamnar. Då visar ritningen eller fotomontaget det som verkligen ska målas, och samma uppgifter står i vårt skriftliga kostnadsförslag.",
     ],
     "aside": {"title": "Handlingar enligt kommunen", "items": [
       "Situationsplan i skala 1:400", "Fasadritning 1:100 eller fotomontage",
       "Förslag till kontrollplan", "Ansökan via e-tjänst"]}},
    {"id": "farglager-sollentuna", "h2": "Färglagren på en villa från seklets första hälft",
     "paras": [
       "Riksantikvarieämbetet skriver att linoljefärg dominerade på trähus ända in på mitten av 1900-talet, där rödfärg inte användes. Fabriksblandad linoljefärg började tillverkas på 1930-talet, men platstillredd färg förekom till mitten av 1950-talet. En villa från villastädernas första årtionden kan därför ha linoljefärg i de äldsta lagren, även om det som syns i dag är något annat.",
       "Länsstyrelsernas blad om målning utomhus på trä säger att man behöver veta vilka färgtyper huset har, eftersom det kan vara linoljefärg, alkydoljefärg eller plastfärg i olika lager. Flagor, sprickor och blåsor tyder ofta på plastfärg eller alkydoljefärg. Under 1800-talet utökades färgskalan med gråvitt, rosa och grönt, och fönstren målades ofta mahognybruna eller mörkgröna. Vill du ta fram en tidigare färgsättning kan äldre lager skrapas fram med en vass kniv. Om målning inne finns mer under " + _L.format("malare-sollentuna.html", "målare i Sollentuna") + ", om panel och tilläggsisolering under " + _L.format("fasadrenovering-sollentuna.html", "fasadrenovering i Sollentuna") + " och om färgtyper under " + _L.format("malare.html", "målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Sollentuna till",
  "steps": [
    ("Platsbesök", "Vi skrapar fram färglagren och tittar på panel, knutar, foder och fönster."),
    ("Plan och kulturmiljö", "Vi läser detaljplanen och tittar på kulturmiljöplanens lager i kartan."),
    ("Kulörförslag", "Kulör för varje del av fasaden, som underlag till ritning eller fotomontage."),
    ("Skriftligt kostnadsförslag", "Förarbete, färgtyp och antal strykningar står var för sig."),
    ("Förarbete och strykning", "Tvätt, skrapning, grundning och strykning i lämpligt väder."),
    ("Genomgång", "Vi går runt villan med dig och bättrar där det behövs."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Sollentuna",
  "rot": [
    "Att måla fasader på ett småhus ger rotavdrag enligt Skatteverket, och det gör även monteringen och nedmonteringen av byggnadsställningen. Du ska äga huset medan arbetet utförs och helt eller delvis bo i det.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Sollentuna?",
  "price": [
    "Hur många kulörer fasaden får, hur mycket snickerier, knutar och fönster som ska målas, hur många gamla färglager som måste bort och hur hög villan är väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka handlingar behövs för lov att måla villan i en ny kulör i Sollentuna?",
     "Enligt kommunen en ansökan via e-tjänst, en situationsplan på tomtkarta, en fasadritning eller ett fotomontage och ett förslag till kontrollplan."),
    ("Räcker ett fotomontage i stället för en fasadritning?",
     "Kommunens checklista nämner fasadritning eller fotomontage. En fasadritning ska vara i skala 1:100 och visa både befintlig och ny fasad."),
    ("Vilka villaområden i Sollentuna pekar kulturmiljöplanen ut?",
     "Översiktsplanen nämner bland annat Norrvikens villastad, Väderholmen och Skansen, där karaktären ska behållas. Kartan med gällande detaljplaner har ett lager för kulturmiljöplanen."),
    ("Hur ser man om villan är målad med plastfärg?",
     "Flagor, sprickor eller blåsor tyder ofta på plastfärg eller alkydoljefärg, enligt Länsstyrelsernas blad. En fackman kan avgöra vilken färgtyp det är."),
    ("När började man köpa färdigblandad linoljefärg?",
     "Fabriksblandad linoljefärg började tillverkas på 1930-talet, men färg som blandades på plats förekom till mitten av 1950-talet, enligt Riksantikvarieämbetet."),
  ],
  "sources": [_SO_FASAD, _SO_KM, _SO_OP, _RAA, _LST_TRA, _SKV, _SKV2],
  "cta": ("Ska villan i Sollentuna få en ny kulör?", "Boka ett gratis platsbesök, så går vi igenom färglager och kulörförslag innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa från början av 1900-talet med ljusgrön panel och vita knutar i en lummig villastad",
     "early 1900s Swedish two-storey wooden villa with pale green painted vertical panel, white corner boards and window frames, small glazed porch, in a leafy old garden suburb with large oaks and lilacs, quiet gravel street with a picket fence, summer afternoon light, Sollentuna" + _IMG_END),
    ("Färgprover i några kulörer målade bredvid varandra på en träpanel och ett fönsterfoder",
     "close-up of an old wooden house wall with several small painted test patches in muted green, warm grey and off-white placed side by side on vertical panel boards and on a window casing, a paint brush resting on the window sill, soft daylight" + _IMG_END),
    ("Skrapad fläck på en villafasad där flera gamla färglager syns i olika kulörer",
     "macro close-up of a scraped spot on an old wooden facade board revealing several layers of old paint in different colours, pale grey on top, then pink, light green and an ochre bottom layer over bare wood, sharp scraper resting beside it" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ TYRESÖ
"fasadmalning-tyreso.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Tyresö", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Tyresö – fritidshusen i Brevik",
  "description": "Fasadmålning i Tyresö: fritidshus från 1930–60-talen på Brevikshalvön som blivit helårshus – färglager, plastfärg, detaljplanens färgregler och ROT.",
  "h1": "Fasadmålning i Tyresö",
  "lead": "På Brevikshalvön står många hus som byggdes för sommaren och som i dag är helårsbostäder. Fasaden kan ha målats om flera gånger, med olika sorters färg. Geal Entreprenad AB målar om fasader i hela Tyresö och tar först reda på vad som sitter på väggen innan den nya färgen väljs.",
  "card": "Fritidshus som blivit helårshus på Brevikshalvön.",
  "sections": [
    {"id": "brevik-tyreso", "anchor": "Brevik",
     "h2": "Från sommarvillor till helårshus på Brevikshalvön",
     "paras": [
       "Kommunens strategi för Östra Tyresö berättar att de första sommarvillorna byggdes runt Breviksmaren för drygt hundra år sedan. Under 1930–50-talen tog omvandlingen av hela östra Tyresö fart på allvar, och mängder av tomter styckades av och bebyggdes med fritidshus. Fritidshus från 1930-, 40-, 50- och 60-talen breder enligt strategin ut sig över stora områden i Östra Tyresös norra delar och på Brevikshalvön.",
       "Efter hand började allt fler bo kvar året runt. De gamla avstycknings- och byggnadsplanerna gav mycket små byggrätter, men permanentbosättningen har ändå fortsatt att öka. I dag bor ungefär 3 300 personer i Östra Tyresö, varav omkring 2 400 i Brevik. Breviksnäs vid Breviksmaren, som bebyggdes med större sommarnöjen kring förra sekelskiftet, och Ällmora fritidshusområde pekas i strategin ut som värdefulla kulturmiljöer.",
     ],
     "aside": {"title": "Östra Tyresö enligt strategin", "items": [
       "Sommarvillor vid Breviksmaren", "Fritidshus från 1930–60-talen",
       "Omkring 2 400 invånare i Brevik", "Breviksnäs och Ällmora utpekade"]}},
    {"id": "farglager-tyreso", "h2": "Linolja, alkyd eller plastfärg – vad bär panelen?",
     "paras": [
       "Riksantikvarieämbetet skriver i förordet till sin handbok om byggnadsmåleri att linoljefärg, slamfärg och kalkfärg ännu på 1950-talet hörde till de vanligaste färgerna, både vid nymålning och ommålning. Fabriksblandad linoljefärg fanns från 1930-talet. Ett fritidshus från den tiden kan alltså ha fått linoljefärg eller rödfärg från början och senare en eller flera moderna färger ovanpå.",
       "Boverket beskriver vad som hände när träpaneler började målas med tät plastfärg. Akrylatfärg kräver en grundfärg av alkydolja, och där den grunden saknades fuktades panelen upp kraftigt av regn, med fuktskador som följd. Enligt Länsstyrelsernas blad om målning utomhus på trä visar sig plastfärg och alkydoljefärg ofta genom flagor, sprickor eller blåsor. Vi gör därför skrapprov på flera sidor av huset och tittar extra noga där färgen har släppt.",
     ],
     "aside": {"title": "Tecken att se efter", "items": [
       "Flagor", "Sprickor i färgen", "Blåsor", "Uppfuktad panel"]}},
    {"id": "plastfarg-tyreso", "h2": "Plastfärgen måste bort innan linolja kan strykas",
     "paras": [
       "Vill du gå tillbaka till linoljefärg på ett hus med plastfärg ytterst går det inte att måla rakt över. Plastfärg förenas inte med underlaget utan bildar en hinna ovanpå, och enligt Länsstyrelsernas blad måste den hinnan tas bort först. Bäst är att handskrapa med en vass skrapa. Sitter plastfärgen ovanpå äldre linoljefärg kan infravärme användas, eftersom oljefärgen under mjuknar så att plastfärgen går att skrapa av, men arbetet innebär viss brandrisk. Kemiska medel bör undvikas, eftersom de lätt skadar träet.",
       "Blästring och maskinslipning skadar träet, skriver bladet, och högtryckstvätt pressar in vatten i väggen. Riksantikvarieämbetet kallar sandblästring av träfasader olämplig, eftersom underlaget lätt skadas. Bladet påminner också om att partier där färgen sitter bra gärna kan sparas. Vi går igenom med dig vilka väggar som behöver skrapas ner till trä och var det räcker att tvätta, skrapa bort lös färg och måla om med samma färgtyp.",
     ],
     "aside": None},
    {"id": "detaljplan-tyreso", "h2": "Detaljplanen kan styra färgen – även i nästa etapp",
     "paras": [
       "Tyresö kommun skriver att du inte behöver bygglov inom detaljplan för att måla om ett en- eller tvåbostadshus, en komplementbyggnad eller ett komplementbostadshus. För kulturhistoriskt värdefulla byggnader gäller däremot utökad lovplikt. I detaljplanen kan det också finnas bestämmelser om vilka färger och fasadmaterial husen får ha. Planen för din fastighet hittar du i kommunens webbkarta, under planer och bestämmelser.",
       "Östra Tyresö planläggs i etapper. Enligt strategin ska kulturmiljöns karaktär beskrivas i kommande detaljplaneetapper, och i områden med en tydlig karaktär kan särskilda bestämmelser införas, till exempel om fasadmaterial, typ av tak eller färgsättning. Den som målar om nu har därför nytta av att veta vilken etapp huset ligger i. Om rödfärgade hus och lov för ny kulör kan du läsa under " + _L.format("malare-tyreso.html", "målare i Tyresö") + ", om timmer och panel under " + _L.format("fasadrenovering-tyreso.html", "fasadrenovering i Tyresö") + " och om målning i stort under " + _L.format("malare.html", "målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Tyresö till",
  "steps": [
    ("Platsbesök", "Skrapprov på flera sidor av huset för att se vilka färgtyper som sitter på."),
    ("Plan och färg", "Vi tittar i detaljplanen om den har bestämmelser om kulör eller material."),
    ("Skriftligt kostnadsförslag", "Skrapning, färgtyp och antal strykningar står var för sig."),
    ("Färgborttagning", "Plastfärg som släpper skrapas för hand, partier som sitter bra sparas."),
    ("Grundning och strykning", "Bart trä grundas och fasaden stryks i lämpligt väder."),
    ("Genomgång", "Vi går runt huset med dig när sista strykningen har torkat."),
  ],
  "rot_h2": "ROT-avdrag för fasaden på helårs- och fritidshuset",
  "rot": [
    "Rotavdrag ges för arbete i både permanentbostad och fritidshus som du äger, och att måla fasader och sätta upp byggnadsställning räknas som rotarbete. Hyr du ut en del av huset ges inget avdrag för den delen, och bor någon annan permanent i ditt fritidshus räknas det enligt Skatteverket inte längre som ett fritidshus du kan använda.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Tyresö?",
  "price": [
    "Hur många färglager som måste bort, om plastfärg ska skrapas ner till trä, hur mycket panel som behöver lagas och hur stort huset har blivit efter tillbyggnader väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken färg sitter på ett fritidshus från 1940-talet?",
     "Från början kanske linoljefärg eller rödfärg, eftersom de enligt Riksantikvarieämbetet fortfarande hörde till de vanligaste färgerna på 1950-talet. Senare lager kan vara alkyd- eller plastfärg."),
    ("Kan linoljefärg strykas direkt på plastfärg?",
     "Nej. Plastfärg bildar en hinna som måste tas bort innan man kan måla med linoljefärg, enligt Länsstyrelsernas blad om målning utomhus på trä."),
    ("Är infravärme ett säkert sätt att ta bort gammal färg?",
     "Det kan användas när plastfärg sitter ovanpå äldre linoljefärg, men enligt Länsstyrelsernas blad är arbetet förenat med viss brandrisk, så instruktionerna måste följas noga."),
    ("Kan detaljplanen bestämma vilken färg vårt hus i Brevik får ha?",
     "Det kan den. Tyresö kommun skriver att detaljplanen kan ha bestämmelser om färger och fasadmaterial. Planen hittar du i kommunens webbkarta."),
    ("Får vi rotavdrag om vi hyr ut fritidshuset i Tyresö?",
     "Inte för den del som hyrs ut. Bor någon annan permanent i fritidshuset ges inget rotavdrag alls, enligt Skatteverket."),
  ],
  "sources": [_TY_OSTRA, _TY_MALA, _RAA, _BOV_YTA, _LST_TRA, _SKV, _SKV2],
  "cta": ("Ska huset i Tyresö målas om?", "Boka ett gratis platsbesök, så tar vi reda på vilka färglager huset har innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Mindre trähus från 1940-talet som blivit helårsbostad på en tallbevuxen klipptomt nära en vik",
     "small 1940s Swedish wooden summer cottage now a year round home, faded light grey painted horizontal panel with white window frames, on a rocky plot with tall pine trees and blueberry shrubs, glimpse of a calm bay between the trees, Brevik peninsula Tyresö, late summer afternoon" + _IMG_END),
    ("Träpanel där tät plastfärg flagnar och visar ett äldre färglager under",
     "close-up of a weathered wooden facade panel where a thick modern grey plastic paint film is peeling in curled flakes, revealing an older ochre oil paint layer and bare grey wood beneath, sharp hand scraper lying on a windowsill, soft overcast light" + _IMG_END),
    ("Grusväg i ett gammalt fritidshusområde med ommålade trähus bland tallar",
     "narrow gravel road through an old Swedish holiday cottage area turned residential, small freshly repainted wooden houses in muted red, yellow and grey among pine trees and rock outcrops, wild flowers along the roadside, summer evening light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"fasadmalning-upplands-vasby.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Upplands Väsby", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Upplands Väsby – villorna i Bollstanäs",
  "description": "Fasadmålning i Upplands Väsby: sekelskiftesvillor längs Gamla vägen i Bollstanäs – kontrastmålad panel, verandor, putsad sockel, uthus och lov.",
  "h1": "Fasadmålning i Upplands Väsby",
  "lead": "Längs Gamla vägen i Bollstanäs står villor från sekelskiftet 1900 med verandor och gavlar mot gatan och sjön Norrviken nedanför. Geal Entreprenad AB målar om fasader i hela Upplands Väsby och lägger upp arbetet efter husets detaljer, från verandan och sockeln till uthuset.",
  "card": "Sekelskiftesvillorna längs Gamla vägen.",
  "sections": [
    {"id": "bollstanas-uv", "anchor": "Bollstanäs",
     "h2": "Gamla vägen: villor med framsidan mot gatan",
     "paras": [
       "Kommunens kunskapsunderlag för kulturmiljö beskriver Bollstanäs som ett område med bevarad villabebyggelse från sekelskiftet 1900. Gamla vägen går på en höjd längs en bergsslänt som sluttar mot Norrviken, och stickgator leder ner till tomterna vid stranden, där flera har sjöbodar och bryggor. Husen är individuellt utformade men delar stildrag och material. De vänder framsidan mot vägen, där symmetrin och utsmyckningen syns, har höga socklar i puts och är ungefär två våningar höga.",
       "Fasaderna har enligt underlaget i huvudsak stående eller liggande träpanel, målad i kontrast i vitt, gult eller rödfärg, och det finns även putsade hus. Verandor, gavlar och balkonger är riktade mot gatan. Området bedöms som särskilt värdefullt enligt PBL 8 kap. 13 §, och underlaget kopplar det till den statligt understödda egnahemsrörelsen, som gav jordbruksarbetare och hantverkare möjlighet att skaffa mark och bygga ett eget hus.",
     ],
     "aside": {"title": "Bollstanäs enligt underlaget", "items": [
       "Villor från sekelskiftet 1900", "Panel i vitt, gult eller rödfärg",
       "Höga socklar i puts", "Verandor och gavlar mot gatan"]}},
    {"id": "veranda-uv", "h2": "Veranda, frontespis och snickerier",
     "paras": [
       "Kunskapsunderlaget räknar byggnader med ursprunglig volym, med frontespiser och verandor mot gatan, till de karaktärsdrag som ska bevaras. Riksantikvarieämbetets handbok nämner fönster, vattbräder, trappor, räcken och utvändig utsmyckning bland de delar som bör underhållsmålas löpande, eftersom de är hårt utsatta för väder och vind. Väntar man för länge riskerar underlaget att ta skada.",
       "Gammal färg på verandans profilerade delar ska inte blästras bort. Länsstyrelsernas blad skriver att blästring och maskinslipning skadar träet. Riksantikvarieämbetet beskriver varmluft som en skonsammare metod än bränning på mindre ytor, men varnar för att vissa material har låg antändningstemperatur. Vi skrapar för hand där färgen sitter löst och sparar partier där den sitter bra. Fönsterbågarna rengörs bäst med sodatvätt för hand, och blottade kittfalsar grundas innan de kittas.",
     ],
     "aside": {"title": "Utsatta delar", "items": [
       "Fönster och vattbräder", "Trappor och räcken",
       "Utvändig utsmyckning", "Vindskivor och sydfasad"]}},
    {"id": "sockel-uv", "h2": "Den putsade sockeln och panelens kontraster",
     "paras": [
       "De höga putsade socklarna är ett annat underlag än panelen. Riksantikvarieämbetet beskriver kalkfärg som en öppen färg som släpper igenom fukt, med god vidhäftning på kalkputs men dålig på förgipsade och cementrika underlag. Vid mitten av 1900-talet gick man alltmer över från kalkbruk till kalkcementbruk, och samtidigt till andra färger än kalkfärg. Innan sockeln målas behöver vi därför veta om den är putsad med kalkbruk eller har lagats med ett cementrikare bruk senare.",
       "Panelens kontraster ska hålla ihop med sockeln. Länsstyrelsernas blad beskriver hur färgskalan under 1800-talets andra hälft blev dovare, med bruna, gulgrå och gröna kulörer, och att det fram till 1950-talet nästan bara användes billiga jordpigment till utomhusfärg. Vill du ta fram husets tidigare färgsättning kan äldre lager skrapas fram med en vass kniv. Vi målar sedan prov på panel, knutar och foder bredvid varandra innan kulörerna bestäms.",
     ],
     "aside": None},
    {"id": "uthus-lov-uv", "h2": "Uthus, staket och lov i Bollstanäs",
     "paras": [
       "Enkla äldre uthus i anslutning till huvudbyggnaden och äldre staket och grindar mot gatan hör också till det underlaget vill bevara. Är uthuset rödfärgat gäller Riksantikvarieämbetets råd att en slamfärgad yta bara ska målas om med slamfärg. Vid ommålning borstas lös färg och lav bort, väggen dammas av och stryks en gång. Det finns färger med namn som påminner om rödfärg men som har andra bindemedel, så innehållsförteckningen bör läsas noga.",
       "Upplands Väsby kommun skriver att du normalt kan måla om ett en- eller tvåbostadshus och dess komplementbyggnader i en ny färg utan bygglov. Ligger huset inom ett särskilt värdefullt område kan bygglov krävas, och kravet på varsamhet gäller oavsett lovplikt. Eftersom kunskapsunderlaget bedömer Gamla vägen som särskilt värdefull, och underlaget anger att även ny bebyggelse bör anpassas i kulörval till de ursprungliga villorna, är det klokt att fråga kommunen innan kulören byts. Om kulörskalorna i andra områden kan du läsa under " + _L.format("malare-upplands-vasby.html", "målare i Upplands Väsby") + ", om fasadbyten under " + _L.format("fasadrenovering-upplands-vasby.html", "fasadrenovering i Upplands Väsby") + " och om målning i stort under " + _L.format("malare.html", "målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Upplands Väsby till",
  "steps": [
    ("Platsbesök", "Vi tittar på panel, veranda, fönster, sockel och uthus var för sig."),
    ("Färgtyp och kulör", "Skrapprov på panel och snickerier och en kontroll av putsen på sockeln."),
    ("Skriftligt kostnadsförslag", "Verandan, sockeln och uthusen står som egna poster."),
    ("Förarbete", "Handskrapning, sodatvätt av fönsterbågar och kittning av fönster."),
    ("Strykning", "Varje underlag får sin färgtyp och stryks i lämpligt väder."),
    ("Genomgång", "Vi går runt huset med dig och bättrar det som behövs."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning i Upplands Väsby",
  "rot": [
    "Skatteverket räknar målning av fasader på ett småhus som rotarbete, liksom byggnadsställningen. Komplementhus som förråd kan höra till småhuset, men att måla staket eller murar ger inget avdrag, så de gamla staketen mot gatan räknas utanför.",
    _ROT_SUM + " Du ska äga huset när arbetet utförs. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Upplands Väsby?",
  "price": [
    "Hur mycket veranda, snickarglädje och fönster huset har, hur hög villan och sockeln är, om sockeln behöver lagas och hur många uthus som ingår väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur tas gammal färg bort från verandans profilerade lister?",
     "För hand med skrapa där färgen sitter löst. Blästring och maskinslipning skadar träet, och på mindre ytor är varmluft skonsammare än bränning, enligt Riksantikvarieämbetet."),
    ("Vilken färg passar en putsad sockel på en äldre villa?",
     "Kalkfärg fäster bra på kalkputs men dåligt på förgipsade och cementrika underlag. Därför behöver man först veta vad sockeln är putsad med."),
    ("Behövs bygglov för ny kulör på en villa längs Gamla vägen i Bollstanäs?",
     "Kommunens kunskapsunderlag bedömer området som särskilt värdefullt, och där kan bygglov krävas. Fråga kommunen innan kulören byts."),
    ("Ger det rotavdrag att måla det gamla staketet mot gatan?",
     "Nej. Skatteverket godkänner inte målning av staket eller murar för rotavdrag, men målning av husets fasader ger avdrag."),
    ("Hur målas ett rödfärgat uthus om?",
     "Lös färg och lav borstas bort, väggen dammas av och stryks en gång med slamfärg. En slamfärgad yta ska bara målas om med slamfärg."),
  ],
  "sources": [_UV_KU, _UV_FASAD, _RAA, _LST_TRA, _SKV, _SKV2],
  "cta": ("Ska villan i Upplands Väsby målas om?", "Boka ett gratis platsbesök, så går vi igenom veranda, sockel och uthus innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla i två våningar med veranda mot gatan, hög putsad sockel och ljusgul panel",
     "Swedish wooden villa from around 1900, two storeys with a central gable dormer facing a narrow gravel road, light yellow painted vertical panel with white corner boards, a white painted veranda with simple fretwork, a tall rendered stone plinth, old pine and oak trees, lake visible below the slope, summer" + _IMG_END),
    ("Vit veranda med profilerade räcken och snickarglädje där en del är nyskrapad inför målning",
     "close-up of an old white painted wooden veranda with turned balusters and decorative fretwork brackets, some parts hand scraped back to bare wood ready for priming, a hand scraper and a round brush on the veranda floor, soft morning light" + _IMG_END),
    ("Litet rödfärgat uthus bredvid ett gammalt trästaket med grind på en villatomt",
     "small old red ochre painted wooden outbuilding with a plank door on a villa garden plot, next to an old white painted wooden picket fence with a gate and stone gateposts, apple tree and long grass, late summer light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VALLENTUNA
"fasadmalning-vallentuna.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Vallentuna", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Vallentuna – småhusen i Lindholmen",
  "description": "Fasadmålning i Vallentuna: villor och gruppbyggda småhus i Lindholmen från 1970-talet och framåt – asbest i kitt och puts, täta färger, lov och ROT.",
  "h1": "Fasadmålning i Vallentuna",
  "lead": "Lindholmen vid Roslagsbanan är ett småskaligt stationssamhälle där bebyggelsen huvudsakligen har vuxit fram sedan 1970-talet. Geal Entreprenad AB målar om fasader i hela Vallentuna och tar reda på vad huset är byggt och målat med innan något skrapas.",
  "card": "Villor och grupphus från 1970-talet och framåt.",
  "sections": [
    {"id": "lindholmen-vallentuna", "anchor": "Lindholmen",
     "h2": "Stationssamhället vid Roslagsbanan",
     "paras": [
       "Den fördjupade översiktsplanen för norra Vallentuna och Lindholmen beskriver den del av Lindholmen som ligger inom planen som främst det småskaliga stationssamhälle som har vuxit fram kring Roslagsbanan. Bebyggelsen har huvudsakligen tillkommit sedan 1970-talet och består främst av villor och gruppbyggda småhus. Senast har området Kulla byggts. Utvecklingen började ändå långt tidigare, med den medeltida sätesgården och dess ägor.",
       "Planen återger kommunens kulturmiljöprogram, där Lindholmen hör till exempelområdena med höga kulturhistoriska kvaliteter. I nordvästra Lindholmen finns dessutom ett område med mycket höga kvaliteter och ett stort antal fornlämningar. Enligt programmets riktlinjer ska antikvarisk expertis anlitas i ärenden som berör exempelområdena, och vid förändringar bör hänsyn tas till bland annat den befintliga miljöns skala och bebyggelsemönster.",
     ],
     "aside": {"title": "Lindholmen enligt planen", "items": [
       "Stationssamhälle vid Roslagsbanan", "Byggt mest sedan 1970-talet",
       "Villor och gruppbyggda småhus", "Höga kulturhistoriska kvaliteter"]}},
    {"id": "asbest-vallentuna", "h2": "Fönsterkitt och puts från före 1980 – prov innan skrapning",
     "paras": [
       "Ett hus från 1970-talet ligger inom den period då asbest användes i byggmaterial. Boverket skriver att asbest förbjöds inom byggsektorn 1982, och att en byggnad som är uppförd mellan 1940 och 1980 sannolikt innehåller asbest någonstans. Bland exemplen på var den kan finnas nämns fönsterkitt och puts, alltså just det som skrapas, slipas och lagas när en fasad förbereds för målning.",
       "Så länge asbesten är inkapslad eller sitter i bunden form är den ingen fara, men om materialet bearbetas så att det dammar kan mycket små fibrer andas in. Enligt Boverket är provtagning och analys det enda säkra sättet att veta, och uppgifter kan också finnas i bygglovshandlingarna. Därför tittar vi på husets byggår och tidigare renoveringar vid platsbesöket, och om kitt eller puts kan innehålla asbest tas prov innan vi börjar skrapa.",
     ],
     "aside": {"title": "Kan innehålla asbest", "items": [
       "Fönsterkitt", "Puts", "Dörrfogar", "Byggnader från 1940–1980"]}},
    {"id": "tata-farger-vallentuna", "h2": "Täta färgskikt på panelen",
     "paras": [
       "Ett hus från 1970-talet kan ha målats med moderna täckfärger. Boverket beskriver hur träpaneler började strykas med tät plastfärg, och att akrylatfärg kräver alkydoljegrund. När grunden inte användes fuktades panelen upp kraftigt av regn och fick fuktskador. Det är ett skäl att undersöka panelen nertill och runt fönstren innan ny färg läggs på, och att byta bräder som har tagit skada.",
       "Länsstyrelsernas blad om målning utomhus på trä påpekar att ett hus kan ha linoljefärg, alkydoljefärg eller plastfärg i olika lager, och att flagor, sprickor eller blåsor ofta tyder på plast- eller alkydoljefärg. Bladet varnar också för högtryckstvätt, eftersom den pressar in vatten i väggen. Vi tvättar därför fasaden med låg vattenmängd, låter panelen torka och väljer en färg som passar det som redan sitter på väggen.",
     ],
     "aside": None},
    {"id": "lov-vallentuna-fasad", "h2": "Lov och antikvarie när kulören ska bytas",
     "paras": [
       "Vallentuna kommun skriver att ommålning av ett en- eller tvåbostadshus inte kräver bygglov, men att ändringar ska göras varsamt och anpassas till byggnadens värden. Lov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om huset i sig är kulturhistoriskt särskilt värdefullt. En ansökan ska då innehålla en situationsplan, fasadritningar i skala 1:100 och en redovisning av material och kulörer med NCS-koder, och äldre ritningar kan beställas ur kommunens arkiv om de finns.",
       "I Lindholmen, där kulturmiljöprogrammet ser till skala och bebyggelsemönster, är det klokt att ta kontakt med kommunen innan en hel husgrupp får en ny kulör. Vi tar fram kulörer och NCS-koder per fasaddel, så att uppgifterna kan användas direkt i en ansökan. Mer om gårdar och rödfärg finns under " + _L.format("malare-vallentuna.html", "målare i Vallentuna") + ", om permanentade fritidshus under " + _L.format("fasadrenovering-vallentuna.html", "fasadrenovering i Vallentuna") + " och om målning i stort under " + _L.format("malare.html", "målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning i Vallentuna till",
  "steps": [
    ("Platsbesök", "Vi tittar på byggår, tidigare renoveringar, panel, kitt och puts."),
    ("Prov vid behov", "Kan kitt eller puts innehålla asbest tas prov innan något bearbetas."),
    ("Skriftligt kostnadsförslag", "Förarbete, färgtyp, antal strykningar och eventuella panelbyten står var för sig."),
    ("Tvätt och torkning", "Fasaden tvättas skonsamt och panelen får torka innan grundning."),
    ("Strykning", "Grundning av bart trä och strykning i lämpligt väder."),
    ("Genomgång", "Vi går runt huset med dig och bättrar det som behövs."),
  ],
  "rot_h2": "ROT-avdrag: villa med äganderätt eller grupphus i bostadsrätt",
  "rot": [
    "Äger du villan eller radhuset ger målning av fasaden och byggnadsställningen rotavdrag, och är ni flera ägare kan ni dela på avdraget. Ingår huset i en bostadsrättsförening är det annorlunda: Skatteverket godkänner inte arbete på gemensamma ytor som tak och fasader i en bostadsrätt.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan där det gäller.",
  ],
  "price_h2": "Vad påverkar priset i Vallentuna?",
  "price": [
    "Hur stor fasaden är, om prov behöver tas på kitt eller puts, hur mycket panel som behöver bytas och hur många fönster som ska kittas och målas väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan fönsterkittet på ett hus från 1970-talet innehålla asbest?",
     "Det kan det. Boverket nämner fönsterkitt bland exemplen, och byggnader från 1940–1980 innehåller sannolikt asbest någonstans. Prov och analys är det enda säkra sättet att veta."),
    ("Är det farligt att måla över puts som kan innehålla asbest?",
     "Så länge asbesten sitter i bunden form är den ingen fara, enligt Boverket. Risken uppstår när materialet bearbetas så att det dammar."),
    ("Får vi rotavdrag för fasadmålning i en bostadsrättsförening med radhus?",
     "Nej, inte för fasaden. Skatteverket godkänner inte arbete på gemensamma ytor som tak och fasader i en bostadsrätt."),
    ("Behöver man anlita antikvarie för att måla om i Lindholmen?",
     "Kulturmiljöprogrammet säger att antikvarisk expertis anlitas i ärenden som berör exempelområdena, där Lindholmen ingår. Fråga kommunen om din åtgärd berörs."),
    ("Varför ska man inte högtryckstvätta en träfasad?",
     "Länsstyrelsernas blad om målning utomhus på trä skriver att högtryckstvätt pressar in vatten i väggen och därför är olämplig."),
  ],
  "sources": [_VAL_FOP, _VAL_FASAD, _BOV_ASB, _BOV_YTA, _LST_TRA, _SKV, _SKV2],
  "cta": ("Ska huset i Vallentuna målas om?", "Boka ett gratis platsbesök, så går vi igenom panel, kitt och puts innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Grupp av envåningsvillor från 1970-talet med brun och grå panel nära en lokal järnväg",
     "group of single storey Swedish 1970s detached houses and linked townhouses with dark brown and grey stained horizontal wood panel and white window frames, low pitched concrete tile roofs, young birch trees and lawns, a small suburban railway line in the background, late summer afternoon" + _IMG_END),
    ("Fönster i ett 1970-talshus med sprucket gammalt kitt och flagnande färg på bågen",
     "close-up of a 1970s wooden window on a house facade with cracked old grey glazing putty and flaking white paint on the sash, a plastic sample bag and a small putty knife lying on the windowsill, soft daylight" + _IMG_END),
    ("Radhuslänga från 1970-talet där alla hus har samma nymålade kulör",
     "row of Swedish 1970s single storey terraced houses all painted in the same freshly repainted warm grey colour with white trims, small front gardens with low hedges, shared footpath, calm overcast summer day" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VÄRMDÖ
"fasadmalning-varmdo.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Värmdö", "svc_label": "Fasadmålning",
  "title": "Fasadmålning på Värmdö – röda byar och vita snickerier",
  "description": "Fasadmålning på Värmdö: rödmålade hus med vita snickerier i skärgårdsbyarna på Gällnö, Hjälmö och Lådna – två färgtyper, båthus, lov och ROT.",
  "h1": "Fasadmålning på Värmdö",
  "lead": "I skärgårdsbyarna på Värmdö går samma bild igen: röd panel, vita snickeridetaljer och båthus nere vid hamnen. Bakom det enkla uttrycket kan det finnas två färgtyper som sköts på olika sätt. Geal Entreprenad AB målar om fasader på Värmdö och planerar arbetet efter vad varje del av huset är målad med.",
  "card": "Röd panel, vita snickerier och båthus i skärgårdsbyarna.",
  "sections": [
    {"id": "byarna-varmdo", "anchor": "Skärgårdsbyarna",
     "h2": "Gällnö, Hjälmö och Lådna – röda hus bland syrener",
     "paras": [
       "Kommunens kulturmiljöprogram, Värmdö – Kulturhistoria i skärgårdsbygd, beskriver Gällnö by som den största byn i Svartsöarkipelagen och dess äldre bebyggelse som ovanligt väl bevarad. Bostadshusen ligger för sig i sluttningen mot Hemfladen, omgivna av lövträd och syrenbersåer, medan uthus och ekonomibyggnader ligger i utkanten av byn och båthusen nere vid hamnen. De flesta husen är rödmålade med snickeridetaljer i vitt, och några har glasade verandor med enkel snickarglädje runt fönster och dörrar.",
       "På Hjälmö och Lådna är de flesta husen enligt programmet byggda kring sekelskiftet 1900, när många äldre parstugor revs och ersattes med hus med verandor och fyrdelad planlösning. De flesta bostadshusen har panel och är rödmålade med vita snickeridetaljer. Skärgårdsbyarna på Husarö, Ingmarsö, Svartsö, Gällnö och Hjälmö hör till kommunens 14 riksintressen för kulturmiljövården.",
     ],
     "aside": {"title": "Byarna enligt programmet", "items": [
       "Rödmålad panel", "Snickeridetaljer i vitt",
       "En- eller tvåkupigt tegel på flera tak", "Båthus vid hamnen"]}},
    {"id": "tva-fargtyper-varmdo", "h2": "Röd panel och vita snickerier – två arbeten i ett",
     "paras": [
       "Röd panel och vita foder kan vara målade med två olika färgtyper, och därför tar vi vid platsbesöket reda på vad varje del bär. Riksantikvarieämbetets handbok beskriver röd slamfärg som en matt, vattenspädbar och fuktgenomsläpplig färg som fäster bra på ohyvlat virke men sämre på hyvlat. Den skyddar till viss del träet mot nedbrytning, och järnvitriolen i färgen anses ha viss konserverande effekt. En slamfärgad yta ska bara målas om med slamfärg.",
       "Snickerierna kräver mer handarbete. Fönster rengörs bäst med sodatvätt för hand, löst kitt skrapas bort och blottade kittfalsar grundas innan de kittas. Även verktygen skiljer sig: till slamfärg rekommenderar handboken en mindre plafondpensel som rengörs med tvål och vatten, medan linoljefärg på fasadytor stryks tunt med en rund eller oval pensel på ungefär sju centimeter och en mindre pensel för svåråtkomliga ställen. Vi stryker panel och snickerier i separata moment, så att ingen färg hamnar där den inte hör hemma.",
     ],
     "aside": None},
    {"id": "bathus-varmdo", "h2": "Båthus och bodar vid bryggan",
     "paras": [
       "Vid Karklö hamn finns flera båthus bevarade, och strax ovanför ligger faluröda bostads- och ekonomibyggnader med mycket av sin 1800- och 1900-talskaraktär kvar. På Harö ligger sjöbodar och bryggor nere vid Byviken, och husen där är panelade och faluröda med varierande takmaterial. Bodarna står nära vattnet, och slamfärgen kan enligt Riksantikvarieämbetet strykas i både torrt och fuktigt väder utan att hållbarheten försämras, så länge solen inte ligger på för hårt.",
       "Den fabriksblandade slamfärg som säljs i dag innehåller konserveringsmedel, och den kan behöva spädas med vatten för att få en strykbar konsistens. Den ska inte strykas för tjockt. Handboken varnar också för att det i handeln finns färger med namn som påminner om traditionell rödfärg men som har andra bindemedel och andra egenskaper, och råder att läsa innehållsdeklarationen och se upp för latextillsatser. Vi väljer därför färg till bodarna efter vad som redan sitter på dem.",
     ],
     "aside": {"title": "Slamfärg på bodarna", "items": [
       "Tål fuktigt väder vid strykning", "Inte i starkt solsken",
       "Spädas vid behov", "Läs innehållsdeklarationen"]}},
    {"id": "haro-lov-varmdo", "h2": "Harö och lovet i riksintressena",
     "paras": [
       "Harö fick enligt kulturmiljöprogrammet ångbåtsförbindelse först på 1920-talet, och den äldre skärgårdskulturen levde kvar där längre än i andra delar av skärgården. Fortfarande finns här i större omfattning än på andra håll i kommunen en äldre folklig byggnadskultur, bland annat två parstugor i sluttningen mot Byviken. Harö är riksintresse för kulturmiljövården, och programmet föreslår att områdesbestämmelser med bland annat utökad lovplikt och varsamhets- och skyddsbestämmelser bör komma till stånd för delar av området.",
       "Värmdö kommun skriver att det inte krävs bygglov för fasadändring på en- och tvåbostadshus eller komplementbyggnader, men att bygglov krävs för ommålning om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden själv är särskilt värdefull. Sedan den 1 december 2025 gäller lovplikt även inom riksintressena för kulturmiljövården, och kommunens kulturmiljökarta visar vilka fastigheter som berörs. Om väderutsatta fasader och Gustavsberg kan du läsa under " + _L.format("malare-varmdo.html", "målare på Värmdö") + ", om sommarvillor och q-märkta hus under " + _L.format("fasadrenovering-varmdo.html", "fasadrenovering på Värmdö") + " och om målning i stort under " + _L.format("malare.html", "målare") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning på Värmdö till",
  "steps": [
    ("Platsbesök", "Vi bedömer panel, snickerier, verandor och bodar var för sig."),
    ("Kulturmiljökartan", "Vi kontrollerar om fastigheten ligger i ett riksintresse eller värdefullt område."),
    ("Skriftligt kostnadsförslag", "Panel, snickerier och bodar står som egna poster med färgtyp och strykningar."),
    ("Förarbete", "Rödfärgen borstas fri från lös färg och lav, snickerierna tvättas och skrapas."),
    ("Strykning", "Rödfärg och snickerifärg stryks i separata moment."),
    ("Genomgång", "Vi går runt huset och bodarna med dig och bättrar det som behövs."),
  ],
  "rot_h2": "ROT-avdrag för fasadmålning på skärgårdshuset",
  "rot": [
    "Rotavdrag ges för arbete i både permanentbostad och fritidshus som du äger, och målning av fasader räknas som rotarbete. Komplementhus som förråd kan höra till småhuset om arbetet görs på tomten i nära anslutning till bostaden. Att reparera och underhålla båtbryggor, staket och murar ger däremot inget avdrag.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Värmdö?",
  "price": [
    "Hur många byggnader som ska målas, hur mycket snickerier och verandor huset har, om panel och snickerier har olika färgtyp och hur material och ställning tar sig ut till fastigheten väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken pensel används till rödfärg på en skärgårdsstuga?",
     "Riksantikvarieämbetet rekommenderar en mindre plafondpensel. Efter strykningen rengörs penslarna med tvål och vatten."),
    ("Varför står det latex på en burk som säljs som rödfärg?",
     "Det finns färger med namn som påminner om traditionell rödfärg men med andra bindemedel. Riksantikvarieämbetet råder att läsa innehållsdeklarationen och se upp för latextillsatser."),
    ("Ger det rotavdrag att måla bryggan vid sjöboden?",
     "Nej. Skatteverket godkänner inte reparation och underhåll av båtbryggor, staket eller murar för rotavdrag vid ett småhus."),
    ("Behöver ett hus på Harö bygglov för att målas om i en ny kulör?",
     "Harö är riksintresse för kulturmiljövården, och Värmdö kommun skriver att lovplikt gäller inom riksintressena. Kontrollera fastigheten i kulturmiljökartan."),
    ("Varför ska rödfärg från affären ibland spädas med vatten?",
     "Fabriksblandad slamfärg kan behöva spädas för att få en strykbar konsistens, enligt Riksantikvarieämbetet. Den ska inte strykas för tjockt."),
  ],
  "sources": [_VD_KMP, _VD_KB, _VD_FASAD, _VD_PBL, _RAA, _SKV, _SKV2],
  "cta": ("Ska huset i skärgården målas om?", "Boka ett gratis platsbesök, så går vi igenom panel, snickerier och bodar innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Rödmålade trähus med vita snickerier i en skärgårdsby på en sluttning ner mot en vik",
     "small Stockholm archipelago village on a gentle slope down to a sheltered bay, red ochre painted wooden houses with white window frames, white trims and glazed verandas, clay tile roofs, lilac bushes and birch trees, a narrow gravel lane between the houses, calm summer morning" + _IMG_END),
    ("Fönster med vitmålade foder och kittade bågar i en röd slamfärgad panelvägg",
     "close-up of an old six-pane wooden window with freshly painted white casing and sashes with new linseed putty, set in a matte red ochre painted vertical board wall, a small round brush resting on the white windowsill, soft daylight" + _IMG_END),
    ("Rödfärgat båthus på stenfundament vid en brygga i en skärgårdsvik",
     "old red ochre painted wooden boathouse with a plank door standing on stone foundations at the water's edge in a calm archipelago bay, a weathered grey wooden jetty beside it, smooth granite rocks and reeds, summer evening light" + _IMG_END),
  ],
},

}
