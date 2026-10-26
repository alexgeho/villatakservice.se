# -*- coding: utf-8 -*-
"""Golvslipning – ortsidor v19: Norrtälje, Södermalm, Tyresö, Täby, Upplands Väsby, Vallentuna (2026-10-26).
Deltjänst under golvlaggning.html (TJ_HUB["golvslipning"]). Intent: slipa och ytbehandla ett BEFINTLIGT trägolv –
inte lägga nytt (det är golvlaggare-<ort>.html, som varje sida länkar till i texten).
Lokal vinkel per sida (en huvudfråga per sida, skild från ortens golvlaggare-sida och övriga tjänstesidor på orten,
från v15/v17/v18-sidorna och från varandra):
Norrtälje – skurgolv i fritidshus som står kalla på vintern: varför ett nyslipat golv luddar, från lack till såpa,
kallt vatten, skurning en vårmorgon, springor och drev (kommunens fakta om 26 000 fritidshus, utredningen om
Svartlöga–Rödlöga);
Södermalm – slipa i den nyköpta bostadsrätten mellan tillträde och inflyttning: Skatteverkets regel om nyköpt
bostad, stadgarna, parkett som ligger på sand (1940-talets flytande golv, Norra Hammarbyhamnen runt 1980), svikt och
ondulering, utjämningsmassor under plastmattor (områdesfakta: flyttningar och lägenhetsstorlekar 2025);
Tyresö – gamla brädgolv i torp, arbetarbostäder och 1950-talets stugor: slipa lätt eller inte alls, spik, sickel,
hyvel, lyfta, vända och slå ihop brädorna (Stockholms läns museum, Solberga/del av Raksta 2008);
Täby – golvet där väggen stod när planlösningen ändras i villa, radhus och grupphus: anmälan vid bärande vägg,
skarven, undergolv mot golv, lagning med brädor och stavar, hela rummet slipas (Kulturmiljöer i Täby);
Upplands Väsby – trägolv på platta i 1960–70-talens radhus och kedjehus: glipan vid sockeln som ska vara öppen,
kvartsstav i stället för spackel, fuktkvot och luftfuktighet före ytbehandling, enkla fuktkontroller
(Kunskapsunderlag för kulturmiljö i Upplands Väsby);
Vallentuna – maskhål, gångar och fukt i golvplank på gårdar och i fritidshus: vilka hål som är ofarliga, borrmjöl,
fukt som letar sig ut vid kanterna, mögel, lagning med linoljespackel och lusning (Översiktsplan 2040).

Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-26 (curl/urllib med User-Agent
Mozilla; byggnadsvard.se via webbplatsens WP-API; alla pdf:er har textlager enligt pdftotext):
  Norrtälje kommun (Fakta och statistik, landsbygd och skärgård: en av Sveriges största landsbygdskommuner, cirka
  32 000 bor på landsbygden, drygt 26 000 fritidshus, cirka en fjärdedel av brukarna vistas större delen av året i
  kommunen; Kulturmiljöutredning nr 4 Svartlöga – Rödlöga 2016, pdf: successiv avfolkning under 1900-talet,
  sommargäster i de övergivna bostadshusen och ny fritidshusbebyggelse, främst bebodda sommartid, endast ett fåtal
  vintertid, ingen framdragen el – solceller, gasol och egna vindkraftverk, en- och tvåvånings timrade hus),
  Stockholms stad (Områdesfakta 2025 Södermalm stadsdelsområde, pdf: 13 851 inflyttningar och 14 718 utflyttningar
  2025, 77 525 bostäder, 43 680 bostadsrätter, 17 165 ettor, 21 466 tvåor, 7 856 lägenheter utan kök),
  Stockholms läns museum (Solberga/del av Raksta, rapport 2008:31, pdf via insynsverige: uppdrag av Tyresö kommun,
  exploatering efter Claes Lagergrens död 1930, nästan hälften av godset exploaterat för fritidshus vid slutet av
  1950-talet, byggnadsplan för Solberga 1952, Raksta såldes från 1958, sex byggnader från 1700- och 1800-talet i
  huvudsak arbetarbostäder, fritidshus från 1950-talet och pågående permanentning, äldsta stugan med breda brädor
  spikade med handsmidd spik, farstu med äldre brett brädgolv flyttat från rummet, förslag om skyddsbestämmelser för
  Holländartorp som även omfattar interiören med äldre golv- och takmaterial),
  Täby kommun (Kulturmiljöer i Täby – riktlinjer, antagen av kommunfullmäktige 8 april 2024, pdf: under 1970-talet många radhus och grupphusområden i Täby kyrkby och
  Byle, Norskogen 197 bostäder i villor, parhus och radhus 1957–59, Erikslund enhetligt grupphusområde från första
  halvan av 1970-talet med över 300 bostäder, parhus i två våningar med flacka tak; Råd och riktlinjer för
  grupphusområden: tidstypiskt uttryck, takformer, takmaterial, takfot, färgsättning, fönsterformat),
  Upplands Väsby kommun (Kunskapsunderlag för kulturmiljö, pdf: radhus och kedjehus 1960–70-tal i östra
  kommundelarna, säckgator, bilfria gång- och cykelstråk, 1–2 våningar eller 2 våningar i suterräng, platta eller
  flacka tak, exempel Sjukyrkoberget, Skälby, Fresta, Odenslunda och Apoteksskogen; varsamhetskravet och
  förvanskningsförbudet vid såväl exteriöra som interiöra ändringar; Bo85 första renodlade bostadsmässan i Sverige,
  Runby Backar där Byggforskningsrådet visade hur småhusbyggandet kunde utvecklas),
  Vallentuna kommun (Översiktsplan 2040, pdf: cirka 5 500 på landsbygden 2017, klungor av bebyggelse eller enstaka
  gårdar vid skogspartier, odlingslandskap kring byarna, största delen av byarna på samma plats som under yngre
  järnålder, Skålhamravägen flera relativt stora byar med välbevarad bebyggelse, allt fler bosätter sig i
  fritidshuset, flertalet fritidshusområden omvandlade sedan 1990-talet, Garns-Ekskogen cirka 500 bebyggda
  fastigheter),
  Boverket (Ingrepp i husets bärande delar: vägg som inte är bärande eller förberedd för öppning kan rivas utan
  anmälan, väsentlig påverkan på bärande delar kräver anmälan och startbesked, konstruktör kan vara lämplig),
  Golvbranschen GBR (Branschriktlinjer SLIP 22, pdf: undergolv stabilt utan svikt, svikt kan ge ondulering, kunden
  informeras, risk för stavsläpp i lamellkonstruktion ska upplysas, spikar avlägsnas – slippapper och gnistor, risk
  för dammexplosion, ingen ytbehandling utanför 30–60 % RF eller fuktkvot 6–10 %, variationerna är problemet,
  sprickor i spacklade fogar),
  Svenska Byggnadsvårdsföreningen (byggnadsvard.se, frågespalt och artiklar: Kan man rädda skurgolven? – fibrer reser
  sig efter skurning på obehandlade slipade golv, slipning skadar fibrerna mer än hyvling, övergående efter några
  skurningar med hård borste och tofflor, skor inomhus och sand förr, silverlyster, snabbvuxet virke, skurnylon;
  Såpa eller skura undergolv av furu? – hyvlat golv har mer intakta fibrer och är mindre känsligt för fläckar, lång
  tid innan nyslipade golv får ålderdomlig karaktär, enighet om kallt vatten, koncentrerad såpa i porerna, flammigt
  i början; Göra skurgolv av lackade golv –
  slipa av lacken och såpskura sannolikt vackrare och mer lättskött, fibrerna skadas, sickla på begränsat utrymme;
  Lackat – oljelack: kaustiksoda och tapetklister, skrapa, skura, neutralisera med svag ättiksyralösning; Såpskura
  nylagt furugolv – lut användes inte, kallt vatten, kalk för ljusare ton framhäver kärnveden; Golvbehandling av golv
  i torp? – strimmig trägnagare inte ovanlig i ouppvärmda hus, skurgolv saknar ytbehandling som bromsar uttorkning,
  årlig skurning tidig vårmorgon, sensommar/höst dammsugning och fuktig trasa, foto med någon månads mellanrum,
  borrmjöl och vit trasa, större pågående angrepp, hemförsäkring brukar innehålla skadedjursförsäkring; Täta
  golvspringor med vaxat snöre eller drev? – i uppvärmt hus smalast sensommar/höst och bredast på våren, drev i
  skurgolv fuktas och kan missfärga, sparsamt vatten, lister på notsidan av splintved; Materialhörnan – Parkettgolv
  (Nordiska museet) – stavparkettens genombrott under 1900-talet, 1920-talets stavar klistrade med asfalt på betong,
  flytande golv från mitten av 1940-talet i bl.a. hyreshus: sandbädd, lösa reglar, lamellbrädor, ljudisolering,
  fjädrande; 1980-talets robusta charm – Norra Hammarbyhamnen, HSB runt 1980, invid Hammarbykanalen nära Södermalms
  stenstad, plastmattor utbytta, parketten i vardagsrummen lagd på sand oftast kvar; Lägga ny fiskbensparkett så
  traditionellt som möjligt – hus från 1913, inget trägolv under plastmattorna, fiskben i två rum, asbesthaltiga
  utjämningsmassor under mitten av 1900-talet, analys, grålumppapp mindre stumt och mindre stegljud; Vad göra? –
  grangolv åldras till silvergrått, slipning förstör smutsavvisande skikt, fortsätt med såpa, uppsprucken yta och
  stickor gör slipning befogad; Hur ska jag gå vidare med detta golv – lätt avslipning med handmaskin, oscillerande,
  patinan kvar i ojämnheterna, linoljefärg, golvslip ger platt och dött; Tjärat trägolv? – golvslip tar mycket av
  tjockleken, liten excenterslip 125–150 mm; Trägolv – masonit och linoleum gav mängder av spik, spikarna ur;
  Hur renovera buckliga originalgolv … – brytjärn, golvlister först, vända brädor med kärnsidan upp, banka ihop,
  komplettera med en bräda i ytterkant, inte för tajt, färg och fernissa sicklas, slipning tar patinan, hyvling
  vackrare och mer motståndskraftig; Nåta skurgolv? – 1920-talshus, springor störst på vintern och smalast på
  sensommaren, elastisk fyllning, undvik hampa, lyfta golvet med kofot och slå ihop; Finns det någon metod för att
  lossa golv? – första brädan rundad på undersidan, gå försiktigt fram, kilar och kofot; Renovera eller nytt –
  vardagsrum som varit två rum, olika kvalitet, glipa upp till 2 cm, ena golvet undergolv för linoleum; Golv i
  sekelskifteshus – två rum till ett kök, lackade slitna furugolv, slipning eller helst sickling som kompromiss,
  hantverksmässigt lagade skador, hyvla om eller vända kräver handlag; Ny vägg sekelskifteslägenhet – minimera
  infästningar i parketten; Lägga nytt golv på en tredjedel … – samma dimensioner hos mindre sågverk; Bleka
  järnvitriol på golv? – nya brädor kan gråna utomhus, järnvitriol dystrare gråton och svår styrka; Stavparkett –
  sortera ljusa och mörka, fallande ordning, omvänd i intilliggande rader; Mellanrum mellan golv och sockel –
  spackel smulas sönder, kvartsstav mest hållbar, 1950–60-tal platta på mark med uppreglade golv, glipan för
  luftomsättningen; Mögellukt… – jämför fuktkvot i golv med vägg/innertak, högst någon procent högre, plast på
  golvet; Är mitt hus angripet? – runda hål högst någon mm ofarliga vid oregelbunden uppvärmning, ovala 3–6 mm
  husbock aktiv på sommaren, renoveringar som rubbat klimatet oftast golv, lack/matta på golv mot marken – fukten
  vid kanterna, spricka mellan golv och sockel över 1 cm, häl-test för svikt; Reparera golvplankor med
  insektsangrepp – gångar efter slipning av färg, ouppvärmt och linoleummatta, byta brädor eller spackla och
  måla/betsa; Laga 1700/1800-talsgolv med djupa skador – linoljespackel/linoljekitt, vax inte under målning,
  skåljärn, lusa i samma träslag och årsringstäthet, orsaken åtgärdad, skurgolv tekniskt bäst; Vitt pulver på gamla
  plankor – mögel, förstadium till röta, RH under 70 % i ouppvärmt, dammsugare med rund borste och hepafilter,
  friskluftsmask P3),
  Skatteverket (Ger arbetet rätt till rotavdrag?: slipa och byta golv i småhus – fritidshus räknas som småhus, bostaden
  som köparen äger, yngre än fem år bara återställa, reparera på grund av skadedjur ja, bekämpa skadedjur och mäta
  fukt nej, riva väggar och bygga om planlösningen – äldre än fem år och större delen av stommen behålls,
  bygglovshandlingar och arkitekt nej; bostadsrätt innanför väggar, tak och golv och stadgarnas underhållsansvar;
  Så fungerar rotavdraget: högst 30 procent, 50 000 / 75 000 kr, material och resor/utrustning nej, bara arbetad tid
  på plats, äga bostaden under perioden, fritidshus – annan som bor där permanent ger inget avdrag, nyköpt bostad –
  ingen annan bor där och du flyttar in direkt efter, inte för uthyrning eller försäljning, gemensamt ansvar,
  elektronisk betalning, försäkringsersättning ger inget rotavdrag).
Strukna (ej verifierade eller medvetet utelämnade): att husen på Svartlöga–Rödlöga, i Solberga/Raksta, i Täbys
grupphusområden, i Väsbys radhusområden eller på Vallentunas gårdar faktiskt har de golv som beskrivs (allt skrivet
som villkor "har du …" eller som exempel ur källan); att lägenheterna på Södermalm i allmänhet har parkett på sand
(källan gäller Norra Hammarbyhamnen och "bl.a. hyreshus" i allmänhet); Skatteverket om försäljning av den egna
bostaden (meningen om uthyrning/försäljning står i stycket om nyköpt bostad – återgiven bara där); att golvslipning i
bostadsrätt kräver styrelsens tillstånd (ingen källa på sidan – skrivet som "läs stadgarna"); arbetstider och
ordningsregler i föreningar (ingen källa); vem som räknas som konstruktör eller om konstruktörens arvode ger rot
(Skatteverket nämner arkitekt, kvalitetsansvarig, besiktningsman "eller liknande" – bara de uppräknade nämns);
tillverkar- och varumärkesnamn i källorna (såpa, skurnylon, spackel, husfabrikant i Norskogen, köksstommar);
personnamn i svaren; priser, avgifter och tidsåtgång.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
Kritikpass 2026-10-26: alla källor öppnade igen (byggnadsvard.se via WP-API, pdf:er via pdftotext – samtliga har
textlager; Skatteverket svarade på urllib med webbläsar-User-Agent) och varje faktamening jämförd med källtexten.
Rättat/struket: Norrtälje – meningen om stående/liggande årsringar struken (sidan för lång, källan borttagen),
"föreningen beskriver att byggnadsvårdare är oense" omformulerat, torpsvaret skrivet som källans "bra alternativ"
(i källan i samband med trägnagare), drev-meningen följer källans "mer avtorkning än skurning"; Södermalm – "slipningen
kan börja först efter tillträdet" knutet till rotavdraget (Skatteverkets ägarkrav), aside-rubriken "Golv i lägenheter
på Söder" -> "Så har parkett lagts" (1920- och 1940-talsuppgifterna gäller inte specifikt Södermalm), ettor/tvåor =
1 rk/2 rk i områdesfaktans tabell, antikvarien skriven som boende i området (källans "sitt eget bostadsområde");
Tyresö – handsmidd spik gäller "den äldsta stugan" i ett av husen (inte en egen stuga), brytjärnet "brukar" (inte
"oftast"), permanentningen återgiven som rapportens "pågående"; Täby – dokumentet heter riktlinjer, antagna 2024 (inte
kulturmiljöprogram), fabrikant för Norskogens byggelement struken; Vallentuna – FAQ om gångar hedgad som källans
"förmodligen/antagligen", målning efter angrepp som "kan vara olämpligt" (källans "kanske inte lämpligt"); Väsby –
inga ändringar. tj_check: 0 FEL, inga WARN för v19-sidorna utöver saknade bilder.
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py.
Kritikpass 2 (extern) 2026-10-26: alla 41 källor öppnade med curl (byggnadsvard.se-svaren via WP-API eftersom
svaren är dolda för utloggade på sidan; pdf:er via pdftotext, alla med textlager; Skatteverket via curl).
Rättat: Norrtälje – stycket om "ett hus som står kallt ställer andra krav" struket (egen generalisering, sidan
1510 -> under 1500 ord), "därför tar det lång tid" fel orsak -> källans skäl (golven slits inte längre så),
"grå" struket, aside "Timrade hus i skärgårdsbyarna" -> "på Svartlöga–Rödlöga", "Koncentrerad såpa på fläckar" ->
"i porerna", torpsvaret återger källans sammanhang (ouppvärmt torp med strimmig trägnagare, "bra alternativ");
Södermalm – "i Södermalm" -> "på Södermalm" i title/h1, "Samma sorts golv" -> "Parkett på sand finns också"
(1980-artikeln säger bara "lagd på sand"), GBR "kräver" -> "ska enligt riktlinjerna", aside "Parkett på sand runt
1980" -> "i Norra Hammarbyhamnen", "Utjämningsmassor under mattor" -> "från 1900-talets mitt", FAQ om sand knuten
till Nordiska museets beskrivning; Tyresö – lead "på kort tid" struket, "försiktig med stora maskiner" -> "i flera
svar avråder från golvslip", "gärna oscillerande" är svararens egen preferens, spikförsänkningen återgiven som
läsarens åtgärd (inte föreningens råd), meningen "i flera av husen äldre golv" struken (1511 -> under 1500 ord);
Täby – lead "ofta olika ytbehandling" -> "ibland", "golvet påverkas mest" -> "berörs", sickling-förslaget återgivet
som källans fråga ("kanske kunde vara en kompromiss?"); Väsby – lead/description "1960–70-talens radhus på platta"
struket (kunskapsunderlagets "platta tak" gäller taket, uppreglat golv på platta står bara hos föreningen för
1950–60-tal) -> villkorat "kan ligga", mögelsvaret anges gälla ett torp, "orsaken ska åtgärdas" (källa saknas på
sidan) -> GBR:s fuktkvotsgräns; Vallentuna – insektssvaret anges som svar i frågespalten (besvarat av extern
konsult). Skatteverket (30 %, 50 000/75 000 kr, nyköpt bostad, fritidshus, försäkringsersättning) stämmer ordagrant.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

_SBF = "https://byggnadsvard.se/"
def _sbf(title, slug):
    return ("Svenska Byggnadsvårdsföreningen – " + title, _SBF + slug + "/")

_SBF_RADDA = _sbf("Kan man rädda skurgolven?", "kan-man-radda-skurgolven")
_SBF_UNDERFURU = _sbf("Såpa eller skura undergolv av furu?", "sapa-eller-skura-undergolv-av-furu")
_SBF_LACKSKUR = _sbf("Göra skurgolv av lackade golv", "gora-skurgolv-av-lackade-golv")
_SBF_LACKAT = _sbf("Lackat", "lackat")
_SBF_NYFURU = _sbf("Såpskura nylagt furugolv", "sapskura-nylagt-furugolv")
_SBF_TORP = _sbf("Golvbehandling av golv i torp?", "golvbehandling-av-golv-i-torp")
_SBF_DREV = _sbf("Täta golvspringor med vaxat snöre eller drev?", "tata-golvspringor-med-vaxat-snore-eller-drev")
_SBF_MHPARK = _sbf("Materialhörnan – Parkettgolv", "materialhornan-parkettgolv")
_SBF_1980 = _sbf("1980-talets robusta charm", "1980-talets-robusta-charm")
_SBF_FISKBEN = _sbf("Lägga ny fiskbensparkett så traditionellt som möjligt", "lagga-ny-fiskbensparkett-sa-traditionellt-som-mojligt")
_SBF_VADGORA = _sbf("Vad göra? (grangolv)", "vad-goera")
_SBF_GAVIDARE = _sbf("Hur ska jag gå vidare med detta golv", "hur-ska-jag-ga-vidare-med-detta-golv")
_SBF_TJARAT = _sbf("Tjärat trägolv?", "tjarat-tragolv")
_SBF_TRAGOLV = _sbf("Trägolv (spik i golvet)", "tragolv")
_SBF_BUCKLIGA = _sbf("Hur renovera buckliga originalgolv från början av 1900-talet?", "hur-renovera-buckliga-originalgolv-fran-borjan-av-1900-talet")
_SBF_NATA = _sbf("Nåta skurgolv?", "nata-golv-2")
_SBF_LOSSA = _sbf("Finns det någon metod för att lossa golv?", "finns-det-nagon-metod-for-att-lossa-golv")
_SBF_RENNYTT = _sbf("Renovera eller nytt", "renovera-eller-nytt")
_SBF_SEKEL = _sbf("Golv i sekelskifteshus", "golv-i-sekelskifteshus")
_SBF_NYVAGG = _sbf("Ny vägg sekelskifteslägenhet", "ny-vagg-sekelskifteslagenhet")
_SBF_TREDJEDEL = _sbf("Lägga nytt golv på en tredjedel av golvytan i torpet från 1812", "lagga-nytt-golv-pa-en-tredjedel-av-golvytan-i-torpet-fran-1812")
_SBF_VITRIOL = _sbf("Bleka järnvitriol på golv?", "bleka-jarnvitriol-pa-golv")
_SBF_STAV = _sbf("Stavparkett", "stavparkett")
_SBF_SOCKEL = _sbf("Mellanrum mellan golv och sockel", "mellanrum-mellan-golv-och-sockel")
_SBF_MOGELLUKT = _sbf("Mögellukt…", "moegellukt")
_SBF_ANGRIPET = _sbf("Är mitt hus angripet?", "ar-mitt-hus-angripet")
_SBF_INSEKT = _sbf("Reparera golvplankor med insektsangrepp", "reparera-golvplankor-med-insektsangrepp")
_SBF_DJUPA = _sbf("Laga 1700/1800-talsgolv med djupa skador?", "laga-1700-1800-talsgolv-med-djupa-skador")
_SBF_PULVER = _sbf("Vitt pulver på gamla plankor", "vitt-pulver-pa-gamla-plankor")

_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_GBR_SLIP = ("Golvbranschen – Branschriktlinjer SLIP 22, slipning av trägolv (pdf)",
             "https://www.golvbranschen.se/siteassets/dokument/branschriktlinjer/branschriktlinjer---slipning-av-tragolv---slip-22.pdf")
_BOV_BAR = ("Boverket – Ingrepp i husets bärande delar",
            "https://www.boverket.se/sv/byggande/bygglov-rivningslov-marklov-och-anmalan/vad-far-jag-bygga-utan-bygglov/ingrepp-i-husets-barande-delar/")
_NT_FAKTA = ("Norrtälje kommun – Fakta och statistik om landsbygd och skärgård",
             "https://www.norrtalje.se/info/bygga-bo-miljo/norrtalje-vaxer/landsbygd-skargard/fakta-och-statistik/")
_NT_SVARTLOGA = ("Norrtälje kommun – Kulturmiljöutredning Svartlöga – Rödlöga (pdf)",
                 "https://www.norrtalje.se/globalassets/dokument/dokument-kultur--fritid/dokument-kultur/dokument-riksintressen-i-norrtalje-kommun/svartloga---rodloga.pdf")
_OF_SOD = ("Stockholms stad – Områdesfakta 2025: Södermalms stadsdelsområde (pdf)",
           "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/inre-staden/sodermalm/sodermalm-stadsdelsomrade.pdf")
_TYR_SLM = ("Stockholms läns museum – Solberga/del av Raksta, kulturmiljöunderlag för Tyresö kommun (pdf)",
            "https://insynsverige.se/documentHandler.ashx?did=20437")
_TABY_KM = ("Täby kommun – Kulturmiljöer i Täby (pdf)",
            "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf")
_TABY_GRUPP = ("Täby kommun – Råd och riktlinjer för grupphusområden",
               "https://taby.se/huvudsajter/kulturmiljoer/rad-och-riktlinjer/grupphusomraden")
_VASBY_KU = ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö (pdf)",
             "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf")
_VAL_OP = ("Vallentuna kommun – Översiktsplan 2040 (pdf)",
           "https://vallentuna.se/download/18.63572f8619eeecafce08366/1782478377449/2.11.7%20%C3%96versiktsplan%202040.pdf")

PAGES_TJ = {

# ------------------------------------------------------------------ NORRTÄLJE
"golvslipning-norrtalje.html": {
  "kind": "district", "service": "golvslipning", "ort": "Norrtälje", "svc_label": "Golvslipning",
  "title": "Golvslipning i Norrtälje – skurgolv i fritidshuset",
  "description": "Golvslipning i Norrtälje: från slipat eller lackat golv till skurgolv i fritidshuset – fibrer som reser sig, kallt vatten och ett hus som står kallt.",
  "h1": "Golvslipning i Norrtälje",
  "lead": "Många vill ha ett såpskurat golv i sommarhuset, men ett nyslipat golv beter sig inte som ett gammalt skurgolv. Fibrerna reser sig, springorna växlar med årstiderna och huset kanske står kallt halva året. Geal Entreprenad AB slipar och behandlar trägolv i fritidshus och villor i Norrtälje kommun, och vi börjar med att ta reda på hur golvet ska skötas efteråt.",
  "card": "Från slipat eller lackat golv till skurgolv.",
  "sections": [
    {"id": "fritidshus-norrtalje", "anchor": "Fritidshusen",
     "h2": "Drygt 26 000 fritidshus i kommunen",
     "paras": [
       "Norrtälje kommun beskriver sig som en av Sveriges största landsbygdskommuner. Omkring 32 000 personer bor på landsbygden, och därtill kommer drygt 26 000 fritidshus. Kommunen uppskattar att ungefär en fjärdedel av dem som använder fritidshusen vistas i kommunen större delen av året.",
       "Kommunens kulturmiljöutredning för Svartlöga och Rödlöga i ytterskärgården, från 2016, visar hur det kan se ut längst ut. Under 1900-talet flyttade de bofasta successivt därifrån, och sommargäster tog över de övergivna bostadshusen eller byggde nya fritidshus. Bebyggelsen består till stor del av timrade hus i en eller två våningar. I dag bor bara ett fåtal personer där på vintern, och någon framdragen el finns inte – den löses bland annat med solceller, gasol och egna vindkraftverk.",
     ],
     "aside": {"title": "Norrtälje kommun", "items": [
       "Drygt 26 000 fritidshus", "Cirka 32 000 bor på landsbygden", "Timrade hus på Svartlöga–Rödlöga", "Få bofasta vintertid"]}},
    {"id": "fibrer-norrtalje", "h2": "Därför luddar ett nyslipat skurgolv",
     "paras": [
       "Svenska Byggnadsvårdsföreningen har fått en fråga från en läsare vars skurgolv blev luddigt och fick stickor efter såpskurningen, trots en mjuk borste. Föreningen svarar att det är typiskt för obehandlade, slipade golv: slipningen skadar de ytliga fibrerna mer än en hyvling gör, och de reser sig när träet torkar efter skurningen. Problemet brukar gå över efter några skurningar med hård borste och spring med tofflor. Det är vanligare när virket är snabbvuxet, och man kan prova att polera ytan med skurnylon.",
       "Förr gick man i skor inomhus och skurade golven med sand, skriver föreningen, och det både slipade golvet och gav det dess silverlyster. I ett annat svar påpekar föreningen att ett hyvlat golv har mer intakta fibrer och är mindre känsligt för fläckar än ett nyslipat. Eftersom golven inte längre slits på det sättet tar det lång tid innan ett nylagt eller nyslipat golv får den ålderdomliga karaktären.",
     ],
     "aside": None},
    {"id": "lack-norrtalje", "h2": "Från lackat golv till såpa",
     "paras": [
       "Har golvet i stugan lackats någon gång går det ändå att komma tillbaka till ett skurgolv. I ett svar om lackade golv i ett torp skriver föreningen att det sannolikt blir vackrare och mer lättskött om lacken slipas bort och golvet sedan såpskuras, men att fibrerna skadas av slipningen. På en mindre yta kan man först försöka sickla bort lacken. Är det en oljelack nämner föreningen i ett annat svar kaustiksoda blandad med tapetklister som ett alternativ: blandningen stryks på och skrapas bort, och golvet skuras och neutraliseras sedan med en svag ättiksyralösning.",
       "När lacken är borta skuras golvet. Erfarna byggnadsvårdare är enligt föreningen oense om vilken såpbehandling som är bäst, men eniga om kallt vatten. Koncentrerad såpa som får stanna i träets porer gör fläckar lättare att få bort, även om ytan kan bli lite flammig de första gångerna. Lut användes inte förr eftersom den bryter ned ytan. Vill man ha en ljusare ton kan man blanda i kalk, men det framhäver också kärnveden i furu.",
     ],
     "aside": {"title": "Till skurgolv", "items": [
       "Slipa eller sickla bort lacken", "Skura med kallt vatten", "Koncentrerad såpa i porerna", "Kalk för ljusare ton"]}},
    {"id": "kallt-norrtalje", "h2": "Golvet i ett hus som står kallt",
     "paras": [
       "Om ett ouppvärmt torp med strimmig trägnagare skriver föreningen att ett skurgolv är ett bra alternativ, eftersom det saknar en ytbehandling som bromsar uttorkningen av tiljorna. Den årliga skurningen görs helst en tidig morgon på våren, när luftfuktigheten är som lägst och golvet torkar fort. På sensommaren och hösten kan man få nöja sig med att dammsuga och torka av med en fuktig trasa under morgontimmarna.",
       "Springorna ändras också över året. I ett uppvärmt hus är de enligt föreningen smalast i slutet av sommaren och på hösten och bredast på våren när luften är torr. Drev i springorna blir fuktigt vid skurning och kan ge missfärgningar, så ett drevat skurgolv bör hellre torkas av än skuras med mycket vatten. En mer långsiktig lösning är att limma in smala trälister på notsidan och jämna dem till golvhöjd, gärna av splintved som är mer elastisk än kärnvirke.",
       "Gäller frågan i stället breda golvplank, torpargrunden eller ett nytt golv finns det mer under " + _L.format("golvlaggare-norrtalje.html", "golvläggare i Norrtälje") + ".",
     ],
     "aside": {"title": "Skötsel i ett kallt hus", "items": [
       "Skura en vårmorgon", "Dammsug på hösten", "Lite vatten där det finns drev", "Lister av splintved"]}},
  ],
  "steps_h2": "Så går golvslipningen till i Norrtälje",
  "steps": [
    ("Platsbesök", "Vi ser vad golvet är behandlat med och hur huset värms under året."),
    ("Skriftligt kostnadsförslag", "Slipning, sickling och första skurningen står var för sig."),
    ("Förberedelse", "Möbler bärs ut, och lister märks upp och tas bort."),
    ("Slipning eller sickling", "Lacken tas bort så skonsamt som golvet tillåter."),
    ("Första skurningen", "Golvet skuras med kallt vatten och såpa när det är färdigslipat."),
    ("Genomgång", "Du får veta hur golvet sköts när huset står tomt."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i fritidshuset",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete, och avdraget gäller även ett fritidshus som du äger och använder. Bor någon annan permanent i ditt fritidshus räknas det inte längre som ett fritidshus du kan använda, och då ges inget avdrag.",
    "Avdraget är högst 30 procent av arbetskostnaden, som mest 50 000 kr per person och år, och rot och rut får tillsammans vara högst 75 000 kr. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Norrtälje?",
  "price": [
    "Golvytan, om lacken ska slipas eller sicklas bort, hur många rum det gäller och var i kommunen huset ligger. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför reser sig fibrerna när ett nyslipat skurgolv skuras?",
     "Slipningen skadar ytfibrerna mer än en hyvling. Enligt Svenska Byggnadsvårdsföreningen brukar det gå över efter några skurningar med hård borste."),
    ("Kan ett lackat furugolv i sommarstugan bli ett skurgolv?",
     "Ja. Lacken slipas eller sicklas bort och golvet såpskuras sedan. Byggnadsvårdsföreningen bedömer att det sannolikt blir vackrare och mer lättskött."),
    ("När på året ska man skura golvet i ett hus som står kallt på vintern?",
     "Byggnadsvårdsföreningen föreslår en tidig vårmorgon, när luftfuktigheten är låg och golvet torkar snabbt."),
    ("Ska skurvattnet till ett såpskurat golv vara varmt eller kallt?",
     "Kallt. Byggnadsvårdsföreningen skriver att det råder enighet om kallt vatten, även om åsikterna om såpbehandlingen i övrigt går isär."),
    ("Ger golvslipning i fritidshuset rotavdrag?",
     "Ja, om du äger huset och använder det själv. Bor någon annan där permanent räknas det inte som ditt fritidshus, och då ges inget avdrag."),
  ],
  "sources": [
    _NT_FAKTA, _NT_SVARTLOGA, _SBF_RADDA, _SBF_UNDERFURU, _SBF_LACKSKUR, _SBF_LACKAT, _SBF_NYFURU,
    _SBF_TORP, _SBF_DREV, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i fritidshuset bli ett skurgolv?", "Boka ett gratis platsbesök, så går vi igenom golvet och hur huset används innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Såpskurat furugolv med breda brädor i ett timrat fritidshus i skärgården",
     "interior of an old timbered Swedish archipelago summer house, wide pine floorboards scrubbed with soap to a pale matte silvery finish, white painted log walls, small multi-pane window with soft sea light, a simple wooden bench, no people, no text, no letters"),
    ("Närbild på furubrädor där ena delen är nyslipad och andra delen grå och såpskurad",
     "close-up of pine floorboards, left part freshly sanded pale and slightly fuzzy, right part old soap-scrubbed grey wood with patina, a natural bristle scrubbing brush lying on the boards, soft daylight, no people, no text, no letters, no logos"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SÖDERMALM
"golvslipning-sodermalm.html": {
  "kind": "district", "service": "golvslipning", "ort": "Södermalm", "svc_label": "Golvslipning",
  "title": "Golvslipning på Södermalm – slipa före inflyttningen",
  "description": "Golvslipning på Södermalm: slipa parketten i den nyköpta bostadsrätten före inflyttningen – rotavdraget, stadgarna och parkett som ligger på sand.",
  "h1": "Golvslipning på Södermalm",
  "lead": "Mellan tillträdet och flyttlasset står lägenheten tom, och då går det att slipa alla rum på en gång utan att bära runt på möbler. De veckorna räcker längre om slipningen är planerad innan nycklarna lämnas över. Geal Entreprenad AB slipar och ytbehandlar parkett och trägolv i lägenheter på Södermalm, och vi lägger upp arbetet efter ditt tillträdesdatum.",
  "card": "Slipa golven i den nyköpta lägenheten.",
  "sections": [
    {"id": "flytt-sodermalm", "anchor": "Flyttarna",
     "h2": "Tusentals flyttar till och från Södermalm varje år",
     "paras": [
       "Stadens områdesfakta för 2025 visar hur rörligt Södermalm är. Under året flyttade 13 851 personer in till stadsdelsområdet och 14 718 flyttade ut. Av de 77 525 bostäderna är 43 680 bostadsrätter.",
       "De flesta lägenheterna är små. I flerbostadshusen finns 17 165 ettor och 21 466 tvåor, och 7 856 lägenheter saknar kök. I en liten lägenhet finns det sällan något rum att ställa möblerna i medan golvet slipas, och därför är tiden innan du flyttar in ett bra tillfälle.",
     ],
     "aside": {"title": "Södermalm 2025", "items": [
       "13 851 inflyttningar", "43 680 bostadsrätter", "17 165 ettor", "21 466 tvåor"]}},
    {"id": "nykopt-sodermalm", "h2": "Rotavdrag innan du har flyttat in",
     "paras": [
       "Skatteverket ger rotavdrag för att renovera en bostad som du nyligen har köpt men ännu inte flyttat in i. Villkoren är att ingen annan bor i bostaden medan arbetet utförs och att du flyttar in direkt efter renoveringen. Ska lägenheten i stället hyras ut eller säljas ges inget avdrag.",
       "Du måste också äga bostaden under den tid arbetet utförs, så för att få avdraget kan slipningen börja först efter tillträdet. I en bostadsrätt ska arbetet göras innanför lägenhetens väggar, tak och golv och gälla något som du har underhållsansvar för enligt föreningens stadgar. Läs därför stadgarna innan datumet bokas. Om grannar, ljud och damm under själva slipningen finns det mer på sidan om " + _L.format("golvslipning-kungsholmen.html", "golvslipning på Kungsholmen") + ".",
     ],
     "aside": {"title": "Före slipningen", "items": [
       "Tillträdet har skett", "Ingen annan bor där", "Stadgarna är lästa", "Du flyttar in efteråt"]}},
    {"id": "sand-sodermalm", "h2": "Parkett som ligger på sand",
     "paras": [
       "I Svenska Byggnadsvårdsföreningens tidning beskriver Nordiska museet hur flytande golv blev populärt från mitten av 1940-talet, bland annat i hyreshus. På betongbjälklaget lades en sandbädd som jämnades ut, och på den låg lösa träreglar som lamellbrädorna fästes vid. Golvet blev bättre ljudisolerat och något fjädrande att gå på.",
       "Parkett på sand finns också i nyare hus. I Norra Hammarbyhamnen, invid Hammarbykanalen och nära Södermalms äldre stenstad, byggde HSB stora flerbostadshus runt 1980. En antikvarie vid Stockholms stadsmuseum som bor i området skriver i föreningens tidning att många boende har bytt ut plastmattorna, men att den ursprungliga parketten i vardagsrummen, lagd på sand, oftast finns kvar.",
       "Enligt Golvbranschens riktlinjer för slipning ska undergolvet vara stabilt utan svikt. Sviktar golvet kan slipningen ge onduleringar, alltså en vågig yta, och om svikten inte går att åtgärda ska kunden få veta det innan arbetet börjar. På golv av lamellkonstruktion finns enligt riktlinjerna en risk för stavsläpp, och även om den ska golvsliparen upplysa. Vi går därför över hela golvet och känner efter svikt vid platsbesöket.",
     ],
     "aside": None},
    {"id": "stav-sodermalm", "h2": "Stavparkett och rum där parketten saknas",
     "paras": [
       "Föreningens tidning beskriver också hur stavparketten fick sitt stora genombrott under 1900-talet och hur specialhyvlade stavar på 1920-talet började klistras fast med varm eller kall asfalt direkt på betong. Golvet i en äldre lägenhet kan alltså vara lagt på flera olika sätt, och ibland har det bytts ut i några av rummen.",
       "I en fråga till föreningen beskriver en läsare en lägenhet i ett hus från 1913 där plastmattorna hade rivits och det inte fanns något trägolv under, medan två andra rum hade fiskbensparkett. Föreningen påminner om att asbesthaltiga utjämningsmassor ibland användes under mitten av 1900-talet, så den som river i underlaget bör använda andningsmask och skyddskläder. Säkert besked ger bara en analys. Under ny parkett kan ett lager grålumppapp göra golvet mindre stumt och minska stegljudet.",
       "Ska parketten kompletteras eller bytas i de rummen är det ett jobb för " + _L.format("golvlaggare-sodermalm.html", "golvläggare på Södermalm") + ". Slipningen av den befintliga parketten kan göras i samma veva, så att hela lägenheten är klar till inflyttningen.",
     ],
     "aside": {"title": "Så har parkett lagts", "items": [
       "Stav på asfalt från 1920-talet", "Flytande golv från 1940-talet", "Parkett på sand i Norra Hammarbyhamnen", "Utjämningsmassa från 1900-talets mitt"]}},
  ],
  "steps_h2": "Så planerar vi slipningen på Södermalm",
  "steps": [
    ("Platsbesök", "Vi ser på golvet, gärna före tillträdet om säljaren går med på det."),
    ("Skriftligt kostnadsförslag", "Slipning och ytbehandling av varje rum står som egna poster."),
    ("Stadgarna", "Du kontrollerar att golvet ingår i ditt underhållsansvar."),
    ("Slipning", "Rummen slipas när lägenheten är tom efter tillträdet."),
    ("Ytbehandling", "Lack eller olja läggs på och får härda innan möblerna kommer."),
    ("Inflyttning", "Du flyttar in när ytan tål möbler, och vi går igenom skötseln."),
  ],
  "rot_h2": "ROT-avdrag i en nyköpt bostadsrätt på Södermalm",
  "rot": [
    "Slipning av golv är rotarbete enligt Skatteverket, även i en bostadsrätt, så länge arbetet görs innanför bostadens väggar, tak och golv och du har underhållsansvaret. Betalningen ska vara elektronisk för att du ska ha rätt till avdraget.",
    "Företaget får dra av högst 30 procent av arbetskostnaden. Taket är 50 000 kr i rotavdrag per person och år, och 75 000 kr för rot och rut sammanlagt. Material och resor räknas inte. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Södermalm?",
  "price": [
    "Antalet rum, golvtypen, om golvet sviktar eller har lösa stavar och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan jag få rotavdrag för golvslipning innan jag har flyttat in i bostadsrätten?",
     "Ja, enligt Skatteverket om ingen annan bor där medan arbetet görs och du flyttar in direkt efteråt. Du måste också äga bostaden när arbetet utförs."),
    ("Kan slipningen göras före tillträdet?",
     "För rotavdrag måste du äga bostaden när arbetet utförs. Vi planerar därför slipningen från tillträdesdagen."),
    ("Vad betyder det att parketten ligger på sand?",
     "Att den ligger flytande ovanpå en sandbädd. Nordiska museet beskriver metoden från mitten av 1940-talet: lösa träreglar på en utjämnad sandbädd och golvbrädorna fästa på reglarna. Golvet blir något fjädrande, och därför känner vi efter svikt före slipningen."),
    ("Varför kan ett fjädrande golv bli vågigt efter slipning?",
     "Golvbranschen skriver att svikt i undergolvet kan ge onduleringar. Går svikten inte att åtgärda ska du få veta det innan arbetet börjar."),
    ("Kan det finnas asbest i underlaget under plastmattan i en äldre lägenhet?",
     "Det kan det. Svenska Byggnadsvårdsföreningen skriver att asbesthaltiga utjämningsmassor ibland användes under mitten av 1900-talet. Bara en analys ger besked."),
  ],
  "sources": [
    _OF_SOD, _SBF_MHPARK, _SBF_1980, _SBF_FISKBEN, _GBR_SLIP, _SKV, _SKV2,
  ],
  "cta": ("Har du köpt en lägenhet på Södermalm?", "Boka ett gratis platsbesök, så planerar vi slipningen efter tillträdet och du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipad och lackad ekparkett i ett tomt vardagsrum i en lägenhet med stora fönster",
     "empty living room in a Stockholm apartment just before move-in, freshly sanded and lacquered oak parquet floor, bare white walls, large windows with daylight, a few plain unmarked cardboard boxes stacked by the door, no furniture, no people, no text, no letters, no logos"),
    ("Närbild på ekparkett i fiskbensmönster vid en dörröppning i en äldre lägenhet",
     "close-up of oak herringbone parquet at an interior doorway in an older Stockholm apartment, one half freshly sanded pale oak and the other half old darker lacquer, white door frame and a simple wooden threshold, soft daylight, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TYRESÖ
"golvslipning-tyreso.html": {
  "kind": "district", "service": "golvslipning", "ort": "Tyresö", "svc_label": "Golvslipning",
  "title": "Golvslipning i Tyresö – gamla brädgolv i torp och stugor",
  "description": "Golvslipning i Tyresö: gamla brädgolv i torp och 1950-talets stugor – slipa lätt, sickla, hyvla eller lyfta och slå ihop brädorna och spara patinan.",
  "h1": "Golvslipning i Tyresö",
  "lead": "Ett brädgolv som har legat i ett torp i över hundra år har en patina som en golvslipmaskin lätt tar bort. Ofta kommer man långt med lättare metoder, och ibland är det bättre att lyfta brädorna än att slipa ned dem. Geal Entreprenad AB slipar och renoverar trägolv i villor, stugor och äldre hus i Tyresö, och vi väljer metod efter golvet.",
  "card": "Slipa och spara gamla brädgolv.",
  "sections": [
    {"id": "solberga-tyreso", "anchor": "Husen",
     "h2": "Torp, arbetarbostäder och 1950-talets stugor",
     "paras": [
       "Stockholms läns museum gjorde 2008 en kulturhistorisk bedömning av Solberga och en del av Raksta på uppdrag av kommunen. Efter Claes Lagergrens död 1930 började Tyresögodsets marker exploateras, och vid slutet av 1950-talet hade nästan hälften av det gamla godset exploaterats för fritidshus. För Solberga fastställdes en byggnadsplan 1952, och tomterna i Raksta såldes från 1958.",
       "Inom området finns sex byggnader från 1700- och 1800-talet, i huvudsak arbetarbostäder som har hört till godset. I övrigt finns fritidshus från 1950-talet, och rapporten beskriver att en permanentning pågår. I ett av husen har den äldsta stugan kvar breda golvbrädor spikade med handsmidd spik, och i ett annat har ett äldre brett brädgolv flyttats från rummet till farstun. För Holländartorp föreslår rapporten skyddsbestämmelser som även omfattar interiören med äldre golv- och takmaterial.",
     ],
     "aside": {"title": "Solberga och Raksta", "items": [
       "Byggnadsplan för Solberga 1952", "Tomter i Raksta från 1958", "Sex hus från 1700–1800-tal", "Fritidshus från 1950-talet"]}},
    {"id": "latt-tyreso", "h2": "Måste golvet gå under golvslipen?",
     "paras": [
       "I flera svar avråder Svenska Byggnadsvårdsföreningen från golvslip på gamla golv. Om ett grangolv som först skurats och sedan oljats, och som ägaren tyckte hade blivit grått och trist, svarar föreningen att gran åldras till silvergrått. En slipning förstör det smutsavvisande skiktet och ger ett dött golv utan slitage, så hellre fortsätta med såpa. Har ytan däremot spruckit upp så att man får stickor i fötterna är en slipning befogad.",
       "I ett annat svar, om ett ojämnt golv med färgrester och spikhål i en timrad byggnad, rekommenderar föreningen en lättare avslipning med handslipmaskin (svararen föredrar själv en oscillerande) och att patinan får sitta kvar i brädornas ojämnheter innan golvet målas med linoljefärg. Att köra golvet med golvslip skulle ge en yta som blir platt och död i jämförelse. Om ett golv som verkar tjärat skriver föreningen att golvslipen tar ganska mycket av brädornas tjocklek, och att man i första hand bör slipa med en liten excenterslip på 125–150 millimeter.",
     ],
     "aside": None},
    {"id": "spik-tyreso", "h2": "Spik, sickel och hyvel",
     "paras": [
       "Innan något slipas ska spiken bort. Golvbranschens riktlinjer för slipning påpekar att spik kan förstöra slippapperet och ge gnistor, med risk för dammexplosion i slipdammpåsen. Har golvet varit täckt av masonit och linoleum kan det sitta mängder av spik kvar, och föreningen skriver att alla spikar bör tas ur innan golvet slipas. En läsare i frågespalten försänkte i stället de spikar som höll golvet några millimeter.",
       "Gammal färg och fernissa kan normalt sicklas bort, skriver föreningen i ett svar om breda plankgolv från början av 1900-talet. Är tiljorna tjocka kan man slipa golvet, men då försvinner patinan och historien också. Hyvling ger enligt föreningen en vackrare och mer motståndskraftig yta, men handhyvling är ett grannlaga arbete.",
       "Gäller det i stället golvet i en tillbyggnad eller ovanpå krypgrunden finns det mer under " + _L.format("golvlaggare-tyreso.html", "golvläggare i Tyresö") + ".",
     ],
     "aside": {"title": "Lättare än golvslip", "items": [
       "Oscillerande handslip", "Excenterslip 125–150 mm", "Sickel för färg och fernissa", "Hyvel för en tålig yta"]}},
    {"id": "lyfta-tyreso", "h2": "Lyfta, vända och slå ihop brädorna",
     "paras": [
       "Ibland är springorna så breda att ingen slipning hjälper. I ett svar om ett 1920-talshus vars golv slipats fria från färg beskriver föreningen hur golvet rör sig med årstiderna: springorna är störst på vintern och smalast på sensommaren. En fyllning i springorna behöver därför vara elastisk och kräver underhåll, och material som binder fukt, till exempel hampa, bör undvikas om golvet ska skuras. En mer omfattande åtgärd är att ta loss golvlister och socklar, lyfta golvet försiktigt med kofot, slå ihop brädorna och spika fast dem igen.",
       "Med ett brytjärn för golv brukar det enligt föreningen gå att demontera brädorna försiktigt och lägga tillbaka dem, och ibland kan de vändas, helst med kärnsidan uppåt. Efter ihopbankningen blir golvytan lite smalare, så det kan behövas en kompletterande bräda i samma tjocklek längs ytterkanten. Golvet ska inte läggas för tätt eftersom träet rör sig med årstiderna.",
       "Den första brädan är ofta svårast att få loss. En läsare som lyfte golven i ett gammalt hus upptäckte att brädan närmast väggen var rundad på undersidan, vilket gjorde det lätt. Föreningen påpekar att det finns många varianter beroende på golvtyp, infästning, ålder och tradition, och att man ska gå försiktigt fram så att man ser hur golvet är lagt innan något bryts sönder. Med kilar och kofot kommer man ganska långt.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går arbetet med golvet till i Tyresö",
  "steps": [
    ("Platsbesök", "Vi ser hur brädorna är lagda, spikade och behandlade."),
    ("Skriftligt kostnadsförslag", "Du får förslag på metod, från lätt avslipning till att lyfta golvet."),
    ("Lister och spik", "Socklar märks upp och tas bort, och lös spik dras ur."),
    ("Lyftning vid behov", "Brädorna lyfts och slås ihop där springorna är för breda."),
    ("Slipning", "Ytan slipas, sicklas eller hyvlas så lätt som möjligt."),
    ("Ytbehandling", "Såpa, linoljefärg eller annan behandling enligt överenskommelse."),
  ],
  "rot_h2": "ROT-avdrag för golvarbetet i Tyresö",
  "rot": [
    "Skatteverket räknar slipning och byte av golv som rotarbete i ett småhus, och till småhus räknas även fritidshus. Huset ska användas som bostad, och arbetet ska göras i den bostad som du äger.",
    "Avdraget beräknas på arbetskostnaden och är högst 30 procent av den. Högst 50 000 kr per person och år får vara rotavdrag, och tillsammans med rutavdrag gäller taket 75 000 kr. Material, utrustning och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Tyresö?",
  "price": [
    "Golvytan, hur mycket spik och färg som ska bort, om brädorna behöver lyftas och vilken metod som passar golvet. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Förstör en golvslipmaskin patinan på ett gammalt brädgolv?",
     "Den tar bort mycket av den. Svenska Byggnadsvårdsföreningen föreslår i flera svar en lättare avslipning med en mindre maskin, eller sickling och hyvling."),
    ("Ska ett silvergrått grangolv slipas?",
     "Inte om ytan är hel, enligt Byggnadsvårdsföreningen, som hellre ser att man fortsätter med såpa. Har ytan spruckit och ger stickor är en slipning befogad."),
    ("Hur lossar man den första brädan i ett gammalt golv?",
     "Försiktigt, med kilar och kofot, så att man ser hur golvet är lagt. I ett exempel hos Byggnadsvårdsföreningen var brädan närmast väggen rundad på undersidan och gick lätt att lyfta."),
    ("Varför måste spiken bort innan golvet slipas?",
     "Golvbranschen skriver att spik kan förstöra slippapperet och ge gnistor, med risk för dammexplosion i dammpåsen."),
    ("Går det att vända gamla golvbrädor i stället för att slipa dem?",
     "Ibland, enligt Byggnadsvårdsföreningen, beroende på hur undersidan ser ut. Helst ska kärnsidan vara uppåt när brädorna läggs tillbaka."),
  ],
  "sources": [
    _TYR_SLM, _SBF_VADGORA, _SBF_GAVIDARE, _SBF_TJARAT, _SBF_TRAGOLV, _SBF_BUCKLIGA, _SBF_NATA, _SBF_LOSSA,
    _GBR_SLIP, _SKV, _SKV2,
  ],
  "cta": ("Har du ett gammalt brädgolv i Tyresö?", "Boka ett gratis platsbesök, så föreslår vi en metod som sparar golvet och du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Breda gamla furubrädor med patina i ett torp, lätt slipade och såpade",
     "interior of an old Swedish crofter's cottage, very wide old pine floorboards with soft worn patina, lightly sanded and soap treated, visible hand-forged nail heads, whitewashed walls, small window with daylight, no furniture, no people, no text, no letters"),
    ("Närbild på en gammal golvbräda som lyfts vid väggen med kofot och träkil",
     "close-up of an old wide pine floorboard slightly raised at one end near the wall, a steel crowbar and a small wooden wedge lying on the floor next to it, skirting board removed and leaning against the wall, clean wood, warm daylight, empty room, no people, no hands, no fingers, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TÄBY
"golvslipning-taby.html": {
  "kind": "district", "service": "golvslipning", "ort": "Täby", "svc_label": "Golvslipning",
  "title": "Golvslipning i Täby – golvet där väggen stod",
  "description": "Golvslipning i Täby: när en vägg rivs i villan, radhuset eller grupphuset blir det en skarv i golvet – laga in brädor och stavar och slipa hela rummet.",
  "h1": "Golvslipning i Täby",
  "lead": "När en vägg tas bort för att två rum ska bli ett blir det kvar en rand i golvet där väggen stod. Ibland är det en glipa, ibland ett parti med ett annat golv, och ibland har rummen haft olika ytbehandling. Geal Entreprenad AB slipar och lagar trägolv i villor, radhus och kedjehus i Täby, och vi ser till att det nya rummet får ett golv som hänger ihop.",
  "card": "Laga och slipa golvet efter en riven vägg.",
  "sections": [
    {"id": "husen-taby", "anchor": "Husen",
     "h2": "Grupphus från 1950-talet och framåt",
     "paras": [
       "Kommunens riktlinjer Kulturmiljöer i Täby, antagna 2024, beskriver hur många bostäder i radhus och grupphusområden byggdes under 1970-talet i Täby kyrkby och Byle. Erikslund är ett enhetligt grupphusområde från första halvan av 1970-talet med över 300 bostäder, och parhusen där har två våningar och flacka tak. I Näsbypark kom grupphusområdet Norskogen redan 1957–59, med 197 bostäder i villor, parhus och radhus.",
       "Kommunens råd för grupphusområdena handlar om det som syns utifrån: det tidstypiska uttrycket, takformer och takmaterial, färgsättning och fönsterformat. När en vägg inne i huset ska bort är det i stället golvet som berörs.",
     ],
     "aside": {"title": "Grupphus i Täby", "items": [
       "Norskogen 1957–59, 197 bostäder", "Erikslund, tidigt 1970-tal", "Radhus i Täby kyrkby och Byle", "Råd för fasader och tak"]}},
    {"id": "vaggen-taby", "h2": "Innan väggen rivs",
     "paras": [
       "Boverket skriver att en vägg som inte är bärande, eller en vägg där man redan förberett för att kunna öppna upp när huset byggdes, kan rivas utan anmälan. Påverkas byggnadens bärande delar väsentligt krävs däremot en anmälan till byggnadsnämnden och ett startbesked innan arbetet börjar. För att ta reda på vilka delar som är bärande kan det vara lämpligt att ta hjälp av en konstruktör.",
       "För golvet lönar det sig att bestämma i förväg hur skarven ska lösas, så att väggen inte rivs på ett sätt som skadar brädorna i onödan. Själva väggarbetet beskrivs under " + _L.format("snickare-taby.html", "snickare i Täby") + ". Ska du i stället bygga en ny vägg som går att ta bort igen ger Svenska Byggnadsvårdsföreningen rådet att försöka minimera infästningarna i parketten.",
     ],
     "aside": {"title": "Före rivningen", "items": [
       "Är väggen bärande?", "Anmälan och startbesked vid behov", "Plan för skarven i golvet"]}},
    {"id": "skarven-taby", "h2": "Skarven efter väggen",
     "paras": [
       "I föreningens frågespalt beskriver en läsare ett vardagsrum som tidigare varit två rum. Golvet var olika i de två halvorna: i den ena låg brädorna tätt, i den andra var de slitna och glesa med fler kvisthål, och där väggen hade stått fanns en glipa på upp till två centimeter. Föreningen förklarar att golvet i det ena rummet kan ha varit ett undergolv för en linoleummatta, medan det andra var själva golvet.",
       "I ett annat svar, om två rum med lackade och slitna furugolv som skulle bli ett stort kök, frågar föreningen om inte en slipning eller helst en sickling kunde vara en kompromiss. Hantverksmässigt lagade skador kan enligt föreningen ge en extra dimension. Att hyvla om eller vända på ett befintligt golv är fullt möjligt men kräver en del handlag.",
     ],
     "aside": None},
    {"id": "laga-taby", "h2": "Laga in nya brädor och stavar",
     "paras": [
       "Där väggen stod behöver golvet ofta kompletteras. Om ett torp där en tredjedel av golvet skulle läggas nytt skriver föreningen att det går att få tag på samma dimensioner hos mindre sågverk. Ska nya brädor passa in i ett skurgolv kan de enligt ett annat svar få ligga utomhus och gråna en tid innan de läggs in. Att skynda på med järnvitriol är svårt, eftersom det ger en dystrare gråton än naturligt åldrat trä och styrkan är svår att träffa.",
       "I en stavparkett avslöjar sorteringen om det är en lekman som har lagt den, skriver föreningen: stavarna sorteras i ljusa och mörka och läggs i fallande ordning i varje rad, med intilliggande rader i omvänd ordning. När skarven är lagad slipar vi hela det nya rummet i samma arbetsgång, så att gamla och nya delar får samma yta. Gäller det i stället klinker, golvvärme eller ett helt nytt golv finns mer under " + _L.format("golvlaggare-taby.html", "golvläggare i Täby") + ".",
     ],
     "aside": {"title": "Lagning efter en vägg", "items": [
       "Brädor i samma dimension", "Stavar sorterade efter ton", "Hela rummet slipas", "En gemensam ytbehandling"]}},
  ],
  "steps_h2": "Så går arbetet med golvet till i Täby",
  "steps": [
    ("Platsbesök", "Vi ser på golvet på båda sidor om väggen och hur det är lagt."),
    ("Skriftligt kostnadsförslag", "Lagning av skarven, slipning och ytbehandling redovisas var för sig."),
    ("Väggen rivs", "Rivningen görs först, och golvet skyddas där det ska ligga kvar."),
    ("Lagning", "Glipan fylls med brädor eller stavar som passar det gamla golvet."),
    ("Slipning", "Hela rummet slipas, så att ytan blir enhetlig."),
    ("Ytbehandling", "En behandling läggs på hela golvet, gammalt som nytt."),
  ],
  "rot_h2": "ROT-avdrag när planlösningen ändras i Täby",
  "rot": [
    "Skatteverket ger rotavdrag för att riva väggar och bygga om planlösningen i ett hus, om bostaden är äldre än fem år och större delen av den ursprungliga stommen behålls. Slipning och byte av golv är också rotarbete i ett småhus som du äger och använder som bostad.",
    "Avdraget får vara högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Bygglovshandlingar och arkitekt ger inget avdrag, och det gör inte heller material. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Täby?",
  "price": [
    "Hur lång skarven är, om golvet behöver kompletteras med nya brädor eller stavar, rummets yta och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur lagar man golvet där en innervägg har rivits?",
     "Glipan fylls med brädor eller stavar som passar det gamla golvet, och sedan slipas hela rummet så att ytan blir enhetlig."),
    ("Behövs en anmälan för att riva en vägg i radhuset?",
     "Inte om väggen inte är bärande. Påverkas de bärande delarna väsentligt krävs enligt Boverket anmälan och startbesked."),
    ("Varför ser golvet olika ut i de två rummen som har blivit ett?",
     "Svenska Byggnadsvårdsföreningen förklarar att det ena golvet kan ha varit ett undergolv för en linoleummatta medan det andra var avsett att synas."),
    ("Kan nya golvbrädor få samma grå ton som ett gammalt skurgolv?",
     "Byggnadsvårdsföreningen föreslår att låta dem ligga utomhus och gråna innan de läggs in. Järnvitriol ger en dystrare ton och är svår att dosera."),
    ("Ger rivning av en vägg och slipning av golvet rotavdrag?",
     "Att riva väggar och bygga om planlösningen ger rotavdrag om huset är äldre än fem år och större delen av stommen behålls. Slipningen av golvet är också rotarbete."),
  ],
  "sources": [
    _TABY_KM, _TABY_GRUPP, _BOV_BAR, _SBF_RENNYTT, _SBF_SEKEL, _SBF_NYVAGG, _SBF_TREDJEDEL, _SBF_VITRIOL, _SBF_STAV,
    _SKV, _SKV2,
  ],
  "cta": ("Ska en vägg bort i huset i Täby?", "Boka ett gratis platsbesök, så går vi igenom skarven i golvet och du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Stort rum i ett radhus där golvet har lagats och slipats efter en riven vägg",
     "open plan living room in a 1970s Swedish terraced house after a dividing wall was removed, continuous freshly sanded and oiled pine floor with an almost invisible repaired strip where the wall stood, white walls, large garden window, no furniture, no people, no text, no letters"),
    ("Närbild på parkett där nya ekstavar har lagts in i glipan efter en vägg",
     "close-up of an oak parquet floor where a strip of new lighter oak staves has been fitted into the gap left by a removed wall, older darker staves on both sides, before sanding, soft daylight, no tools, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"golvslipning-upplands-vasby.html": {
  "kind": "district", "service": "golvslipning", "ort": "Upplands Väsby", "svc_label": "Golvslipning",
  "title": "Golvslipning i Upplands Väsby – radhus på platta",
  "description": "Golvslipning i Upplands Väsby: trägolv på reglar ovanpå betongplattan i radhus och kedjehus – glipan vid sockeln, fukten under golvet och listerna.",
  "h1": "Golvslipning i Upplands Väsby",
  "lead": "I ett radhus eller kedjehus kan trägolvet ligga på reglar ovanpå en betongplatta. Det påverkar inte så mycket hur golvet slipas, men desto mer det som händer runt omkring: glipan vid väggen, listerna och fukten under golvet. Geal Entreprenad AB slipar och ytbehandlar trägolv i radhus, kedjehus och villor i Upplands Väsby, och vi börjar med att se hur golvet är byggt.",
  "card": "Slipa trägolvet i radhuset på platta.",
  "sections": [
    {"id": "radhus-vasby", "anchor": "Radhusen",
     "h2": "Radhus och kedjehus i en eller två våningar",
     "paras": [
       "Kommunens kunskapsunderlag för kulturmiljö beskriver hur de östra kommundelarna växte fram med en stor andel småhus och radhus under 1960- och 70-talen. Grupperna av atriumhus, radhus och kedjehus ligger längs säckgator, med bilfria gång- och cykelstråk mellan områdena. Husen är rationellt byggda i en eller två våningar, eller i två våningar i suterräng, med platta eller flacka tak. Exempel finns i Sjukyrkoberget, Skälby, Fresta och Odenslunda, men också centralt i Apoteksskogen.",
       "I Väsby finns också bebyggelse från Bo85, som enligt underlaget var den första renodlade bostadsmässan i Sverige. I småhusområdet Runby Backar visade Byggforskningsrådet hur småhusbyggandet och grupphusområden skulle kunna utvecklas.",
       "Underlaget påpekar att varsamhetskravet och det hårdare kravet i förvanskningsförbudet gäller vid såväl exteriöra som interiöra ändringar, även om värdena inte har pekats ut tidigare.",
     ],
     "aside": {"title": "Radhusområden i Väsby", "items": [
       "Sjukyrkoberget", "Skälby", "Fresta och Odenslunda", "Apoteksskogen"]}},
    {"id": "glipan-vasby", "h2": "Glipan vid sockeln ska vara kvar",
     "paras": [
       "Svenska Byggnadsvårdsföreningen har fått en fråga om en springa mellan golv och sockel som syntes när kvartsstaven togs bort inför en slipning. I lite modernare hus, främst från 1950- och 60-talen, kan glipan enligt föreningen vara en del av konstruktionen. Husen byggdes då med platta på mark och uppreglade golv direkt på betongplattan, och för att golvet inte skulle ruttna av den uppträngande markfukten skulle den fukthaltiga luften under golvet ventileras bort. Då var glipan viktig för luftomsättningen.",
       "En sådan glipa tätar vi inte med fogmassa eller spackel efter slipningen. Föreningen påpekar dessutom att spackel smulas sönder av rörelserna i träet, och att en kvartsstav eller liten list är det mest hållbara sättet att dölja en glipa. Listerna tas bort före slipningen, märks upp och sätts tillbaka på samma plats.",
     ],
     "aside": {"title": "Runt kanterna", "items": [
       "Glipan får vara öppen", "Inget spackel i springan", "Kvartsstav döljer glipan", "Listerna sätts tillbaka"]}},
    {"id": "fukt-vasby", "h2": "Fukten i golvet innan det ytbehandlas",
     "paras": [
       "Golvbranschens riktlinjer för slipning säger att ett trägolv inte ska ytbehandlas när fuktkvoten i träet ligger utanför 6–10 procent, eller när luftfuktigheten inomhus är utanför 30–60 procent relativ fuktighet. Problemet ligger enligt riktlinjerna inte i själva luftfuktigheten utan i variationerna, eftersom rörelserna kan försämra ytbehandlingens resultat och ge sprickor i spacklade fogar. Vi mäter därför fuktkvoten i golvet innan behandlingen.",
       "Luktar det unket i nedre planet kan det finnas skäl att undersöka golvet närmare. Byggnadsvårdsföreningen föreslår i ett svar om mögellukt i ett torp att man mäter fuktkvoten i golvplanken och jämför med ställen som är öppna, till exempel en vägg eller ett innertak – golvet bör ha högst någon procent högre fuktkvot. Man kan också lägga en plast på ungefär en kvadratmeter på golvet och se om det samlas fukt under den.",
       "Är golvet för fuktigt väntar ytbehandlingen tills fuktkvoten ligger rätt. Om radon, markfukt och byte av golv i nedre planet finns det mer under " + _L.format("golvlaggare-upplands-vasby.html", "golvläggare i Upplands Väsby") + ".",
     ],
     "aside": {"title": "Före ytbehandlingen", "items": [
       "Fuktkvot 6–10 procent", "Luftfuktighet 30–60 procent", "Jämför golv och vägg", "Plast på golvet som test"]}},
  ],
  "steps_h2": "Så går golvslipningen till i Upplands Väsby",
  "steps": [
    ("Platsbesök", "Vi ser hur golvet är byggt och hur listerna sitter, och mäter fuktkvoten i träet."),
    ("Skriftligt kostnadsförslag", "Slipning, lister och ytbehandling står som egna poster."),
    ("Lister bort", "Socklar och kvartsstavar märks upp och tas bort före slipningen."),
    ("Slipning", "Golvet slipas i flera steg, och kanterna slipas för sig."),
    ("Ytbehandling", "Behandlingen läggs på när fuktkvot och luftfuktighet ligger rätt."),
    ("Lister tillbaka", "Listerna sätts tillbaka, så att glipan döljs men får vara öppen."),
  ],
  "rot_h2": "ROT-avdrag för golvslipning i Upplands Väsby",
  "rot": [
    "I ett radhus eller kedjehus som du äger och bor i räknar Skatteverket slipning av golv som rotarbete. Är huset en bostadsrätt ska arbetet göras inne i bostaden och ingå i ditt underhållsansvar enligt stadgarna. Du och företaget har ett gemensamt ansvar för att ta reda på om arbetet ger rätt till avdrag.",
    "Bara arbetad tid på plats hos dig ger avdrag, med högst 30 procent av arbetskostnaden. Gränsen är 50 000 kr i rotavdrag per person och år och 75 000 kr för rot och rut tillsammans. Material ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Upplands Väsby?",
  "price": [
    "Golvytan, hur många lister som ska tas loss och sättas tillbaka, om golvet behöver torka innan behandlingen och vilken yta du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Ska glipan mellan golv och sockel tätas efter slipningen?",
     "Inte i ett hus med uppreglat golv på platta. Enligt Svenska Byggnadsvårdsföreningen kan glipan behövas för att ventilera bort fuktig luft under golvet."),
    ("Varför spricker spacklet vid golvlisten?",
     "Träet rör sig, och spacklet smulas sönder med tiden. Byggnadsvårdsföreningen anser att en kvartsstav eller liten list är det mest hållbara sättet att dölja glipan."),
    ("Vilken fuktkvot ska trägolvet ha innan det ytbehandlas?",
     "Golvbranschens riktlinjer anger 6–10 procent, och luftfuktigheten inomhus ska ligga mellan 30 och 60 procent."),
    ("Hur kan man kontrollera om det är fuktigt under trägolvet?",
     "Byggnadsvårdsföreningen föreslår att jämföra fuktkvoten i golvet med en vägg eller ett innertak, eller lägga en plast på golvet och se om fukt samlas under den."),
    ("Gäller rotavdraget för golvslipning i ett radhus som är bostadsrätt?",
     "Ja, om arbetet görs inne i bostaden och golvet ingår i ditt underhållsansvar enligt föreningens stadgar."),
  ],
  "sources": [
    _VASBY_KU, _SBF_SOCKEL, _SBF_MOGELLUKT, _GBR_SLIP, _SKV, _SKV2,
  ],
  "cta": ("Ska trägolvet i radhuset i Väsby slipas?", "Boka ett gratis platsbesök, så ser vi hur golvet är byggt och du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat trägolv i vardagsrummet i ett radhus från 1970-talet med vita socklar",
     "living room of a 1970s Swedish terraced house with a large garden window, freshly sanded and lacquered pine floor, white skirting boards with a thin quarter round moulding, light walls, empty room, soft daylight, no people, no text, no letters"),
    ("Närbild på glipan mellan trägolv och vägg där golvlisten är borttagen",
     "close-up of the narrow gap between a sanded wooden floor and a white wall where the skirting board has been removed, a quarter round moulding strip lying on the floor beside it, soft daylight, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VALLENTUNA
"golvslipning-vallentuna.html": {
  "kind": "district", "service": "golvslipning", "ort": "Vallentuna", "svc_label": "Golvslipning",
  "title": "Golvslipning i Vallentuna – maskhål och fukt i gamla golv",
  "description": "Golvslipning i Vallentuna: maskhål, gångar och fukt i gamla golvplank på gårdar och i fritidshus – vad slipningen visar och vad som behöver åtgärdas först.",
  "h1": "Golvslipning i Vallentuna",
  "lead": "Små hål och gångar i ett gammalt golv syns ofta först när färgen eller mattan är borta och slipningen har börjat. De flesta är spår av något som hände för länge sedan, men ibland säger de något om fukten under golvet. Geal Entreprenad AB slipar och lagar trägolv i villor, gårdar och fritidshus i Vallentuna, och vi tittar på orsaken innan vi bestämmer behandling.",
  "card": "Slipa och laga gamla golvplank.",
  "sections": [
    {"id": "landsbygd-vallentuna", "anchor": "Gårdarna",
     "h2": "Byar, gårdar och fritidshus som blivit bostäder",
     "paras": [
       "Vallentunas översiktsplan beskriver en landsbygd där cirka 5 500 personer bodde 2017, med klungor av bebyggelse eller enstaka gårdar intill skogspartier och träddungar och med odlingslandskap runt byarna. Största delen av dagens byar ligger enligt planen på samma plats som under yngre järnålder, och i riksintresseområdet vid Skålhamravägen finns flera relativt stora byar med välbevarad bebyggelse.",
       "Planen konstaterar också att allt fler bosätter sig i sitt fritidshus eller använder det en större del av året, så att gränsen mellan permanentboende och fritidsboende blir allt mer flytande. Sedan 1990-talet har flertalet fritidshusområden i kommunen omvandlats, och i Garns-Ekskogen finns cirka 500 bebyggda fastigheter.",
       "Ett hus som har stått ouppvärmt delar av året, eller haft en matta på trägolvet i flera decennier, kan ha spår i golvplanken som blir synliga först när golvet slipas.",
     ],
     "aside": {"title": "Ur översiktsplanen", "items": [
       "Cirka 5 500 bor på landsbygden", "Byar på järnålderns platser", "Cirka 500 fastigheter i Garns-Ekskogen", "Fritidshus som blir bostäder"]}},
    {"id": "hal-vallentuna", "h2": "Små hål, ovala hål och gångar",
     "paras": [
       "I en artikel i Svenska Byggnadsvårdsföreningens tidning beskriver en byggmästare med lång erfarenhet av gamla hus hur man läser spåren. Runda maskhål som inte är grövre än någon millimeter är ofarliga och uppkommer i gamla hus med oregelbunden uppvärmning eller som tidvis står helt ouppvärmda. Ovala hål på cirka 3–6 millimeter med lite rufsiga kanter kan däremot vara spår efter husbock, som är aktiv under sommaren.",
       "Föreningen skriver i ett annat svar att angrepp av strimmig trägnagare inte är ovanliga i ouppvärmda hus. För att se om ett angrepp pågår kan man fotografera golvet med någon månads mellanrum och jämföra, eller dammsuga bort borrmjölet och senare dammsuga igen på låg hastighet med en vit, finmaskig trasa över munstycket. Då syns det om nytt borrmjöl har tillkommit. Är angreppet större och pågående är klimatet under golvet gynnsamt för gnagaren, och då kan större åtgärder bli nödvändiga.",
       "Gångar som blir synliga när en gammal färg slipas bort kan enligt ett svar i föreningens frågespalt ha uppstått när huset stod ouppvärmt med en linoleummatta ovanpå. Stör de har man inget annat val än att byta hela eller delar av brädorna, eller spackla och måla eller betsa golvet.",
     ],
     "aside": {"title": "Spår i golvet", "items": [
       "Runda hål, högst någon millimeter", "Ovala hål på 3–6 millimeter", "Nytt borrmjöl?", "Gångar under gammal färg"]}},
    {"id": "fukt-vallentuna", "h2": "Fukten avgör vad golvet tål",
     "paras": [
       "Byggmästaren i föreningens artikel har sett många renoveringar som rubbat husets klimat, och oftast har det handlat om golv. När ett gammalt hus som är grundlagt direkt mot marken får golvet lackat eller täckt med linoleum- eller plastmatta kan fukten inte längre ventileras genom hela golvet, utan letar sig upp vid kanterna. En spricka mellan golv och sockel som är bredare än en centimeter kan tyda på angrepp i golvbjälkarna, och på bottenvåningen kan man gå på tå och sätta ned hälen hårt för att känna var golvet sviktar.",
       "Om ett golv med djupa skador efter kyla, fukt och insekter skriver föreningen att orsaken till angreppen först måste vara åtgärdad. Är den inte det kan det vara olämpligt att måla golvet, eftersom ett tätare ytskikt hindrar fukten från att vädra ut. Ett skurgolv är det tekniskt bästa i det avseendet.",
       "Mögel kan se ut som ett vitt pulver på plankorna. Föreningen förklarar att mögel är en ytlig påväxt men också ett förstadium till röta, och att orsaken är för hög luftfuktighet. I ett ouppvärmt utrymme bör den relativa luftfuktigheten ligga under 70 procent. Påväxten kan tas bort med en dammsugare med rund borste och hepafilter, och den som sanerar bör använda friskluftsmask med P3-filter.",
     ],
     "aside": None},
    {"id": "laga-vallentuna", "h2": "Laga, lusa i eller låta vara",
     "paras": [
       "Mindre skador kan få vara kvar som ett spår av historien, skriver föreningen. Det är svårt att få spackel att hålla över tid eftersom träet rör sig, men linoljespackel eller linoljekitt fungerar hyfsat vid mindre lagningar och är lätt att förnya. Vax går inte att använda om golvet ska målas. Finns det risk för stickor kan man skära ned lite med ett skåljärn.",
       "Större skadade partier kan lusas i med nytt virke av samma träslag och med samma årsringstäthet, så att den nya biten rör sig som resten av brädan. Föreningen skriver att hantverksmässigt utförda lagningar visar att golvet är värdefullt. Ska golvet i stället läggas om, till exempel på en ny grund eller med golvvärme, finns det mer under " + _L.format("golvlaggare-vallentuna.html", "golvläggare i Vallentuna") + ".",
     ],
     "aside": {"title": "Lagning av golvplank", "items": [
       "Linoljespackel i små skador", "Skåljärn mot stickor", "Lusa i samma träslag", "Orsaken åtgärdas först"]}},
  ],
  "steps_h2": "Så går arbetet med golvet till i Vallentuna",
  "steps": [
    ("Platsbesök", "Vi ser på hålen och gångarna och känner efter svikt i golvet."),
    ("Kontroll över tid", "Misstänker vi ett pågående angrepp jämför du borrmjöl eller foton under några månader."),
    ("Skriftligt kostnadsförslag", "Lagning, slipning och ytbehandling redovisas var för sig."),
    ("Lagning", "Skadade partier lusas i eller lagas med linoljespackel."),
    ("Slipning", "Golvet slipas så lätt som möjligt."),
    ("Ytbehandling", "Vi föreslår en behandling som låter golvet torka ut, till exempel såpa."),
  ],
  "rot_h2": "ROT-avdrag för golvet i Vallentuna",
  "rot": [
    "Skatteverket räknar slipning av golv som rotarbete, och även reparation på grund av skadedjur ger avdrag. Att bekämpa skadedjur gör det däremot inte, och inte heller att mäta fukt. Avdraget gäller i småhus och fritidshus som du äger och använder som bostad.",
    "Får du försäkringsersättning för arbetet ges inget rotavdrag. Enligt Byggnadsvårdsföreningen brukar en vanlig hemförsäkring innehålla en skadedjursförsäkring, så kontakta försäkringsbolaget om angreppet är stort. Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rut. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Vallentuna?",
  "price": [
    "Hur stora skadorna är, om brädor ska lusas i eller bytas, golvytan och vilken ytbehandling du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Är små runda maskhål i golvplanken farliga?",
     "Runda hål som inte är grövre än någon millimeter beskrivs i Svenska Byggnadsvårdsföreningens tidning som ofarliga. De uppkommer i hus som har värmts oregelbundet."),
    ("Hur ser man om ett insektsangrepp i golvet pågår?",
     "Dammsug bort borrmjölet och kontrollera senare med en vit trasa över munstycket, eller fotografera golvet med någon månads mellanrum och jämför."),
    ("Varför syns gångar i golvet först efter slipningen?",
     "De kan ha legat under färg eller en matta. I ett svar hos Byggnadsvårdsföreningen bedöms sådana gångar troligen ha uppstått när huset stod ouppvärmt med en linoleummatta på golvet."),
    ("Vad är det vita pulvret på gamla golvplank?",
     "Enligt Byggnadsvårdsföreningen mögelpåväxt, som beror på för hög luftfuktighet. Den kan dammsugas bort med hepafilter och skyddsmask."),
    ("Ger reparation av ett insektsskadat golv rotavdrag?",
     "Ja, Skatteverket godkänner reparation på grund av skadedjur. Själva bekämpningen ger inget avdrag, och inte heller arbete som ersätts av en försäkring."),
  ],
  "sources": [
    _VAL_OP, _SBF_ANGRIPET, _SBF_TORP, _SBF_INSEKT, _SBF_DJUPA, _SBF_PULVER, _SKV, _SKV2,
  ],
  "cta": ("Har golvet i huset i Vallentuna hål eller gångar?", "Boka ett gratis platsbesök, så tittar vi på spåren och orsaken innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Gammalt lätt slipat golvplank av furu med små runda maskhål i en gård på landet",
     "close-up of an old pine floor plank in a 19th century Swedish farmhouse, lightly sanded surface showing a few tiny round woodworm holes and fine natural grain, soft side light, no tools, no people, no text, no letters"),
    ("Rum i ett gammalt trähus på landet med nyslipat och såpat brädgolv och en ilusad lagning",
     "room in an old red wooden farmhouse in the Swedish countryside, freshly sanded and soap scrubbed wide pine floorboards with one neatly inserted repair piece of matching wood, white walls, deep window recess with a view of fields, no furniture, no people, no text, no letters"),
  ],
  "related": [],
},

}
