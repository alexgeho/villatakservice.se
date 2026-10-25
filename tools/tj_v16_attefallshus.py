# -*- coding: utf-8 -*-
"""Attefallshus – ortsidor v16: Bromma, Danderyd, Ekerö, Norrtälje, Täby, Värmdö (2026-10-26).
Hubb: attefallshus.html (vanlig sida i generate.py, TJ_HUB["attefallshus"]). Regelartikel: attefallshus-regler.html.
Rättslig ram (samma som de två sidorna, KOMPL_SRC i generate.py, kontrollerad igen 2026-10-26 i lagtexten på
riksdagen.se, lydelse enligt lag 2025:974): komplementbostadshus enligt PBL 1 kap. 4 §; 9 kap. 4 § inom detaljplan
30,0 m² byggnadsarea, 4,0 m taknockshöjd, inom tomten, mindre byggnadsarea än byggnaden det kompletterar, sammanlagt
45,0 m²; 9 kap. 5 § utanför detaljplan 50,0 m², 4,5 m, 65,0 m²; tidigare lovfria byggnader räknas in; 9 kap. 16 §
ombyggnad av komplementbyggnad till komplementbostadshus; 9 kap. 34–35 §§ 4,5 m till gräns, skriftligt medgivande,
vid allmän plats lämnas medgivandet av huvudmannen; 9 kap. 36 § totalförsvar; 9 kap. 37 § bygglov för särskilt
värdefulla byggnader och områden; PBF 6 kap. 1 § anmälan för VA, ventilation, eldstad/rökkanal.

Lokal vinkel per sida (skild från ortens tillbyggnad-/snickare-/byggföretagssidor och från hubb + regelartikel):
Bromma – trädgårdsstaden nästan helt inom detaljplan (30/45-fallet), Ålstensgatan–Södra Ängby (riksintresse AB 643),
Stadsmuseets karta och förfrågan till museet, prickmark, medgivande mot gata/park från stadsbyggnadskontoret, dubbla
VA-anmälningar (byggnadsnämnden + Stockholm Vatten och Avfall) och slutbesked före inflyttning;
Danderyd – Djursholm (AB 38) och Stocksund (AB 48), lovplikt i kulturmiljökartans områden, frivilligt bygglov,
VA-enheten när BTA ökar, kommunens medgivande mot allmän plats, strandskydd: äldre planer före 1 juli 1975 och
utökat strandskydd vid Sätra ängar, Cedergrenska parken och Rösjön;
Ekerö – mycket byggs utanför detaljplan (50/65/4,5-fallet), två världsarv och riksintressen (Adelsö, Munsö, Stavsund,
Helgö, Stenhamra AB 28), områdesbestämmelser kring Munsö kyrka, kommunens undantagsområden (översvämning, erosion),
strandskydd 100–300 m och dispensansökan, enskilt avlopp: tillstånd för WC-anslutning (FMH 13 §);
Norrtälje – landets mest fritidshustäta kommun (SCB 2025), huvudbyggnadens storlek begränsar huset, en- eller
tvåbostadshus, riksintressen (Norrtälje stad AB 84, Hallstavik, Herräng, Grisslehamn, Skebobruk–Edsbro, Arholma),
strandskyddet i miljöbalken (14–15, 18 c, 18 e, 18 i §§), avloppstillstånd/anmälan (FMH 13–14 §§), NVAA servisanmälan;
Täby – kvartersmark i detaljplan där strandskyddet är upphävt, Q/q-bestämmelser och riksintressena Skålhamravägen
(AB 71) och Täby prästgårdsmark (AB 73), handlingar vid VA-anmälan, ny adress vid uthyrning, Roslagsvattens tekniska
regler för inkoppling (efter vattenmätaren, rensbrunn, dagvatten, tryck);
Värmdö – näst flest fritidshus, prioriterade förändringsområden (PFO) där tomten ska rymma ett attefallshus,
14 riksintressen och cirka 55 kulturmiljöområden = särskilt värdefulla, Gustavsberg (AB 56), 100 m från strand,
tillstånd för att ansluta en byggnad till befintligt avlopp.

Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-26:
  Riksdagen: PBL (2010:900) 9 kap. 4–5, 16, 34–37 §§ (lagtexten nedladdad och läst); PBF (2011:338) 6 kap. 1 §
  (via KOMPL_SRC); Miljöbalken (1998:808) 7 kap. 13–15 §§, 18 c, 18 e (punkt 1–2), 18 i §§; Förordning (1998:899) om
  miljöfarlig verksamhet och hälsoskydd 13–14 §§.
  Boverket: Lista med PBL-ändringar (KOMPL_SRC).
  Skatteverket: Ger arbetet rätt till rotavdrag? – inget avdrag för att bygga ett helt nytt hus, friggebod, garage,
  växthus eller liknande fristående byggnad; inget rotavdrag för att bygga en helt ny bostad.
  Länsstyrelsen Stockholm: Strandskyddsdispens – kommunen beslutar i de flesta fall, särskilda skäl, kartskiktet kan
  visa strandskydd vid små/anlagda vatten som tappat skyddet 1 juli 2025, vissa kompletteringsåtgärder utan dispens.
  Region Stockholm: Riksintressen i regional utvecklingsplan (RUFS 2050-bilagan, pdf med text): 113 områden i länet,
  tabellerna med AB-nummer, meningen om särskilt känsliga områden (Stocksund, Djursholm, Gustavsberg, Norrtälje m.fl.).
  SCB: Fritidshus – var finns de? (2026): Norrtälje 27 352, Värmdö 14 709 fritidshus 2025.
  Stockholms stad: Komplementbostadshus, bygglovsbefriad (får strida mot detaljplanen/prickmark, medgivandets innehåll,
  stadsbyggnadskontoret vid allmän plats, anmälan VA/ventilation/eldstad); Stadsmuseets kulturhistoriska
  klassificering (ringar, färger, streckade ytor, e-post, tre veckor); Installation eller ändring av VA (anmälan,
  separat anmälan till Stockholm Vatten och Avfall, enskilt avlopp hos miljöförvaltningen, fyra veckor, slutbesked);
  Varsam utveckling av småhus- och villaområden (pdf med text): trädgårdsstaden "(nästan) alltid en detaljplan",
  Ålstensgatan och Södra Ängby riksintressen, Södra Ängby 1930-talsvillor, aspekter (volym, grön karaktär, gaturum),
  lovgivningsavsnittet s. 77 (skrivet före 2025 – återgivet som stadens äldre vägledning).
  Danderyds kommun: Nya regler för bygglov från 1 december 2025 (uppdaterad 2026-06-09); Strandskydd (uppdaterad
  2023-02-21); Översiktsplan kap. 3 Riks- och mellankommunala intressen (pdf med text).
  Ekerö kommun: Vad vill du bygga? (komplementbostadshus, undantagsområden, karta); Strandskydd, bryggor och sjöbodar;
  Eget avlopp; Ekerö kulturmiljöprogram 2015 (pdf med text: förord två världsarv, bebyggelsetryck och permanentning,
  riksintressena Adelsö, Norra och Södra Munsö, Ekerö/Stavsund, Helgö, Munsö kyrka områdesbestämmelser, bilagan
  "Bygga nytt i gammal bygd").
  Norrtälje Vatten och Avfall: Förändring på fastighet med kommunalt VA (servisanmälan, nytt antal bostadslägenheter,
  VA-samfällighet).
  Täby kommun: Komplementbyggnad; Strandskydd; Vatten och avlopp, installation eller ändring; Kulturmiljöer i Täby,
  antagen (pdf med text: Q/q, riksintressena AB 71 och AB 73, PBL 8 kap. 13 §, bygglovbefriade åtgärder).
  Roslagsvatten: Regler för komplementbostad (Ekerö, Knivsta, Täby, Vallentuna, Vaxholm, Österåker).
  Värmdö kommun: Förändringar i PBL från 1 december 2025; Bygga i kulturmiljöer; Ansökan och anmälan små avlopp;
  Broschyr Fritidshusområde i förändring del 1 (pdf med text).
Strukna/ej verifierade: Norrtälje kommuns egna sidor (norrtalje.se svarade inte 2026-10-26 – ECONNREFUSED/timeout,
även i webbläsaren – därför inga uppgifter om kommunens egen tolkning, karta eller strandskyddssidor); RAÄ:s pdf
"Stockholm AB riksintressen" (gav 404, i stället Region Stockholms bilaga); hur stor andel av respektive kommun som är
detaljplanelagd (ingen källa – bara Ekerös "många av nybyggnaderna … utanför detaljplanelagt område" och Varsams
"(nästan) alltid en detaljplan" används); att fritidshus räknas som en- eller tvåbostadshus (ej verifierat – skrivet
som villkor); Roslagsvattens uppgift "sedan 1 augusti 2020 … 30 m²" (gammal regel, inte använd); avgifter
(bygglovstaxa, VA-avgifter, lägenhetsavgift – medvetet utelämnade); totalförsvarsområden per kommun (bara Ekerö nämner
dem, och snickare-ekero har redan detta – utelämnat på Ekerö); handläggningstider utöver Stockholms fyra veckor och
Stadsmuseets tre veckor; Ekerö-uppgifter om färjor och vägar. Inga priser, garantier, omdömen, egna uppdrag i orterna
eller cert.
Siffror kontrollerade mot källtexten igen: 30,0/45,0/4,0 och 50,0/65,0/4,5 (PBL), 4,5 m och 30 m (PBL 34 §),
100 m och högst 300 m (MB 7:14), 1987, 11 områden, 9 värdekärnor, 1890–1930 (Danderyd ÖP), 1 juli 1975 (Danderyd),
AB 38, 48, 56, 84, 93, 96, 97, 98, 619, 610, 616, 28, 643 och 113 områden (Region Stockholm), AB 71/73 (Täby),
14 riksintressen och cirka 55 kulturmiljöområden (Värmdö), 27 352 och 14 709 (SCB 2025), tre veckor, fyra veckor.
Egna bedömningar (inte källfakta, skrivna som vår bedömning): placering bakom huvudbyggnaden (Bromma, Värmdö),
underordnat hus och grupphusmönster (Täby), stugans storlek som exempel (Ekerö 40 m², Norrtälje 35 m²).
Kända WARN: "ROT"-ord finns bara i ROT-avsnittet som förklarar att huset inte ger avdrag. OBS för leaden: heron på
alla TJ-sidor visar bockpunkten "ROT-avdrag direkt på fakturan" (hero() i generate.py) – för attefallshus motsägs den
av Skatteverket; bör bytas via trust=… för service "attefallshus" (inte ändrat här enligt briefen).
Kritiker 2026-10-26 (alla källor öppnade: PBL/PBF/MB/FMH på riksdagen.se, Boverket, Skatteverket, Länsstyrelsen,
Region Stockholm-bilagan, SCB, Roslagsvatten, NVAA och samtliga kommun-/stadssidor och pdf:er – alla svarade 200, pdf:erna
har textlager; LST:s pdf om kompletteringsåtgärder är skannad och används inte): PBL-mått 30,0/4,0/45,0 och 50,0/4,5/65,0,
4,5 m, 9:16, 9:34–37 och PBF 6:1 stämmer mot lagtexten och attefallshus-regler.html. Rättat: Bromma – H2 "I trädgårdsstaden
gäller 30 m²" motsade Varsam-pdf:en (trädgårdsstadsmiljöer och riksintressen omfattas inte av bygglovsbefrielsen) – nu
"Inom detaljplan … om huset är lovfritt" + den meningen; stadens nuvarande lovplikt för riksintresse/grön ring; FAQ Södra
Ängby enligt staden; "ska sparas" → "bör kunna visa upp"; "vanligt sätt" och "brukar störa minst" → vår bedömning.
Danderyd – Edsviken/Värtan (ej i källa) struket ur H2/FAQ; kommunens medgivande mot allmän plats "i vissa fall";
dispens "i regel"; frivilligt bygglov-råd som vår bedömning. Ekerö – stugexemplet skrivet som tänkt räkneexempel
(bostadshuset 40 m² → nya huset mindre än 40 m²); totalförsvarets riksintressen tillagda (kommunens sida, 9:36);
områdesbestämmelser Munsö kyrka hänvisade till programmet; dispens "i regel". Norrtälje – exemplet tänkt och "mindre än
35 m²"; RUFS "störst risk" → "stor risk"; "i eller intill" → "i" + riksintresse ≠ automatiskt särskilt värdefullt;
fel påstående om att kartskiktet "missar små vatten" ersatt med LST:s faktiska text (MB 7:13 a–b, skiktet kan visa skydd
som upphört); MB 7:17-undantaget för kompletteringsåtgärder tillagt; BDT-anmälan med reservation för kommunal
tillståndsplikt (FMH 13 § 4 st.). Täby – "de flesta villatomter inom detaljplan" (ej i källa) struket; KMP-meningen om
attefallsåtgärder omskriven till källans "många bygglovsbefriade åtgärder får inte utföras"; q-FAQ följer 9:37 (gäller
när skyddet omfattar tomten/området); Värtan struket ur H2; egna omdömen som vår bedömning. Värmdö – kommunantikvarie-
meningen följer kommunens text; "många skärgårdstomter" generalisering struken; dispens "i regel". ROT-avsnitten
kontrollerade mot Skatteverket (nytt hus/fristående byggnad/ny bostad ger aldrig rotavdrag) – oförändrade.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 1 kap. 4 § och 9 kap. 4–5, 16, 34–37 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_PBF = ("Riksdagen – Plan- och byggförordning (2011:338), 6 kap. 1 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-byggforordning-2011338_sfs-2011-338/")
_BOV = ("Boverket – Lista med PBL-ändringar som trädde i kraft 1 december 2025",
        "https://www.boverket.se/sv/samhallsplanering/uppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/")
_MB = ("Riksdagen – Miljöbalk (1998:808), 7 kap. 13–15, 18 c, 18 e och 18 i §§",
       "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/miljobalk-1998808_sfs-1998-808/")
_FMH = ("Riksdagen – Förordning (1998:899) om miljöfarlig verksamhet och hälsoskydd, 13–14 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-1998899-om-miljofarlig-verksamhet-och_sfs-1998-899/")
_LST = ("Länsstyrelsen Stockholm – Strandskyddsdispens",
        "https://www.lansstyrelsen.se/stockholm/natur-och-landsbygd/aktiviteter-och-ingrepp-i-naturen/strandskyddsdispens.html")
_RUFS = ("Region Stockholm – Riksintressen i regional utvecklingsplan för Stockholmsregionen (bilaga, pdf)",
         "https://www.regionstockholm.se/49dc46/contentassets/d520d8a737244589a241cfae38e13db6/bilaga-riksintressen-i-regional-utvecklingsplan-for-stockholmsregionen.pdf")
_SCB = ("SCB – Fritidshus: var finns de? (2026)", "https://www.scb.se/hitta-statistik/artiklar/2026/fritidshus-vart-finns-de/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_ROSL = ("Roslagsvatten – Regler för komplementbostad", "https://roslagsvatten.se/anslutning-regler-f%C3%B6r-komplementbostad")

_SB = "https://bygglov.stockholm/nar-behovs-bygglov/"
_SB_KBH = ("Stockholms stad – Komplementbostadshus (bygglovsbefriad)", _SB + "bygga-nytt-och-bygga-till/komplementbostadshus-bygglovsbefriad/")
_SB_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering", _SB + "bygga-nytt-och-bygga-till/stadsmuseets-kulturhistoriska-klassificering/")
_SB_VA = ("Stockholms stad – Installation eller ändring av vatten och avlopp", _SB + "installationer/installation-eller-andring-av-vatten-och-avlopp-va/")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")

_DAN_NYA = ("Danderyds kommun – Nya regler för bygglov från 1 december 2025",
            "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/")
_DAN_SS = ("Danderyds kommun – Strandskydd", "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/fragor-och-svar/strandskydd/")
_DAN_OP = ("Danderyds kommun – Översiktsplan, kap. 3 Riks- och mellankommunala intressen (pdf)",
           "https://danderyd.se/contentassets/94fc6956dc264c4cab52c0a18ff5bafd/3-riks--och-mellankommunala-intressen.pdf")

_EK = "https://www.ekero.se/bygga-bo-miljo/"
_EK_VAD = ("Ekerö kommun – Vad vill du bygga?", _EK + "bygga-nytt-andra-eller-riva/vad-vill-du-bygga")
_EK_SS = ("Ekerö kommun – Strandskydd, bryggor och sjöbodar", _EK + "bygga-nytt-andra-eller-riva/strandskydd-bryggor-och-sjobodar")
_EK_AVL = ("Ekerö kommun – Eget avlopp", _EK + "vatten-och-avlopp/eget-avlopp")
_EK_KMP = ("Ekerö kommun – Ekerö kulturmiljöprogram 2015 (pdf)",
           "https://www.ekero.se/download/18.553838ea17305720c321ec82/1597925412772/Eker%C3%B6%20kulturmilj%C3%B6program.pdf")

_NVAA = ("Norrtälje Vatten och Avfall – Förändring på fastighet med kommunalt vatten och avlopp",
         "https://www.nvaa.se/vatten-och-avlopp/att-ansluta-till-kommunalt-vatten-och-avlopp/forandring-pa-fastighet-med-kommunalt-vatten-och-avlopp")

_TB = "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/"
_TAB_KB = ("Täby kommun – Komplementbyggnad", _TB + "komplementbyggnad")
_TAB_SS = ("Täby kommun – Strandskydd", _TB + "strandskydd")
_TAB_VA = ("Täby kommun – Vatten och avlopp, installation eller ändring", _TB + "vatten-och-avlopp-installation-eller-andring")
_TAB_KMP = ("Täby kommun – Kulturmiljöer i Täby, antagen (pdf)",
            "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf")

_VD = "https://www.varmdo.se/byggabomiljo/"
_VD_PBL = ("Värmdö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
           _VD + "bygganyttandraellerriva/forandringaripblfrom1december2025.4.18b9914519a768a188a2872.html")
_VD_KM = ("Värmdö kommun – Bygga i kulturmiljöer", _VD + "bygganyttandraellerriva/bygglov/byggaikulturmiljoer.4.57b4a3ba16e6b961dbf10429.html")
_VD_AVL = ("Värmdö kommun – Ansökan och anmälan små avlopp", _VD + "vattenochavlopp/smaavlopp/ansokomsmaavlopp.4.1a82111d16e6c321a368eb23.html")
_VD_PFO = ("Värmdö kommun – Fritidshusområde i förändring, del 1 Planering (pdf)",
           "https://www.varmdo.se/download/18.52346f71869c9938611c2df/1678200543391/Broschyr%20PFO%20del%201%20-%20uppdaterad%202023.pdf")

_REG = _L.format("attefallshus-regler.html", "nya regler för attefallshus")

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"attefallshus-bromma.html": {
  "kind": "district", "service": "attefallshus", "ort": "Bromma", "svc_label": "Attefallshus",
  "title": "Attefallshus i Bromma – trädgårdsstad, karta och 30 m²",
  "description": "Attefallshus i Bromma: 30 m² inom detaljplan, lovplikt i kulturmiljöer enligt Stadsmuseets karta, medgivande mot gata och park och anmälan för VA.",
  "h1": "Attefallshus i Bromma",
  "lead": "Ett litet hus i trädgården kan ge plats åt en vuxen son eller dotter, en förälder eller en hyresgäst i Bromma. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och går igenom detaljplanen, Stadsmuseets karta och anmälan för vatten och avlopp innan något beställs.",
  "card": "Trädgårdsstad, karta och 30 m² inom plan.",
  "sections": [
    {"id": "detaljplan-bromma", "anchor": "Detaljplanen",
     "h2": "Inom detaljplan gäller 30 kvadratmeter – om huset är lovfritt",
     "paras": [
       "Stadens vägledning för småhusområden konstaterar att nästan varje tomt i trädgårdsstäderna har en detaljplan. För ett attefallshus i Bromma är det därför plan- och bygglagens regler för detaljplanelagt område som gäller: huset får ha högst 30,0 kvadratmeter byggnadsarea och 4,0 meter taknockshöjd, och alla lovfria komplementbyggnader på tomten får tillsammans uppta högst 45,0 kvadratmeter. En friggebod eller ett förråd som redan står där tar alltså en del av utrymmet. Samma vägledning skriver att Stockholms trädgårdsstadsmiljöer och områden av riksintresse inte omfattas av bygglovsbefrielsen, så i trädgårdsstaden kan huset i stället kräva bygglov.",
       "Stockholms stad skriver att ett komplementbostadshus som inte kräver lov får strida mot detaljplanen och därför kan stå på prickmark. Planen kan ändå innehålla egna bestämmelser om skydd eller krav på lov, så vi läser den i stadens Bygg- och plantjänsten innan vi ritar. Vägledningen pekar också ut vad som påverkar ett villaområde mest när det förtätas: volymen på komplementbyggnader, den gröna karaktären med träd och häckar och hur byggnader förhåller sig till gatan. Vår bedömning är att ett litet hus längre in på tomten, bakom huvudbyggnaden, stör minst.",
     ],
     "aside": {"title": "Inom detaljplan", "items": [
       "Högst 30,0 m² byggnadsarea", "Taknock högst 4,0 m",
       "Högst 45,0 m² lovfritt på tomten", "Mindre än villan"]}},
    {"id": "karta-bromma", "h2": "Ålsten, Södra Ängby och Stadsmuseets karta",
     "paras": [
       "Region Stockholms sammanställning av riksintressen för kulturmiljövården listar Ålstensgatan och Södra Ängby som ett gemensamt riksintresse (AB 643), och stadens vägledning beskriver Södra Ängby som ett av Europas största sammanhängande områden med modernistiska villor från 1930-talet. Stockholms stad skriver i dag att bygglov krävs om tomten ligger inom ett riksintresse för kulturmiljövården eller i ett område som översiktsplanen pekar ut som särskilt kulturhistoriskt värdefullt. Enligt 9 kap. 37 § krävs bygglov för nybyggnad i särskilt värdefulla områden, och det gäller även ett komplementbostadshus.",
       "Stadsmuseets klassificeringskarta ger den första indikationen. En blå ring markerar riksintresse och en grön ring områden som översiktsplanen pekar ut som särskilt kulturhistoriskt värdefulla. Byggnader i blått eller grönt kräver lov, gult och grått gör det inte om inget annat gäller. Streckade ytor är ännu inte inventerade. Där mejlar du Stadsmuseet adress, fastighetsbeteckning, stadsdel, byggår, tidigare ombyggnader och foton, och museet brukar svara inom tre veckor efter att allt har kommit in.",
     ],
     "aside": None},
    {"id": "grans-bromma", "h2": "Nära granne, gata eller park",
     "paras": [
       "På en tomt i trädgårdsstaden räcker 4,5 meter till gränsen ofta inte långt. Närmare än så krävs ett skriftligt medgivande från de berörda grannarna, annars bygglov. Staden räknar upp vad medgivandet ska innehålla: fastighetsbeteckning, vilken åtgärd det gäller, en situationsplan med avståndet till gränsen och grannarnas underskrifter. Staden skriver att du bör kunna visa upp det för byggnadsnämnden vid tillsyn, så spara det.",
       "Gränsar tomten mot en gata eller en park är kommunen oftast huvudman för den allmänna platsen, och då är det kommunens medgivande som räknas enligt 9 kap. 35 §. I Stockholm skickar du den förfrågan till stadsbyggnadskontoret. Vill du hellre bygga ihop ytan med villan finns " + _L.format("tillbyggnad-bromma.html", "tillbyggnad i Bromma") + ", och alla mått och paragrafer står i " + _REG + ".",
     ],
     "aside": {"title": "Medgivandet ska innehålla", "items": [
       "Fastighetsbeteckning", "Vilken åtgärd det gäller",
       "Situationsplan med avstånd", "Grannarnas underskrifter"]}},
    {"id": "va-bromma", "h2": "Två anmälningar innan rören dras",
     "paras": [
       "Själva huset kräver ingen anmälan, men installationerna gör det. Stockholms stad skriver att en ny installation för vatten eller avlopp ska anmälas till byggnadsnämnden och att arbetet inte får börja före startbesked. Beslutet ska komma inom fyra veckor från att anmälan är komplett. Ska huset kopplas till stadens ledningsnät görs dessutom en egen anmälan till Stockholm Vatten och Avfall. Ventilation och eldstad anmäls till byggnadsnämnden på samma sätt.",
       "När arbetet är klart och kraven visade får du slutbesked, och först då får huset tas i bruk. Vi planerar därför ledningsdragningen tidigt, eftersom avståndet till villans befintliga ledningar och höjdskillnaden på tomten påverkar både schaktet och var huset kan stå.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Bromma",
  "steps": [
    ("Tomt och plan", "Vi mäter upp tomten och läser detaljplanen och klassificeringskartan."),
    ("Placering", "Avstånd till gräns, gata och träd ritas in på en situationsplan."),
    ("Medgivanden", "Vid behov tar du fram grannarnas och kommunens skriftliga medgivanden."),
    ("Anmälan", "VA, ventilation och eldstad anmäls och vi väntar på startbesked."),
    ("Bygget", "Grund, stomme, tak, installationer och ytskikt – nyckelfärdigt."),
    ("Slutbesked", "Huset tas i bruk när slutbeskedet har kommit."),
  ],
  "rot_h2": "Varför attefallshuset inte ger rotavdrag",
  "rot": [
    "Skatteverket räknar upp vad som inte ger rotavdrag på ett småhus, och där står att bygga ett helt nytt hus, en friggebod, ett garage, ett växthus eller en liknande fristående byggnad. Ett komplementbostadshus är en ny fristående byggnad och därmed nybyggnad. Vårt kostnadsförslag för huset visar därför hela beloppet utan avdrag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Bromma?",
  "price": [
    "Husets storlek och planlösning, om det får kök och badrum, grundläggningen på tomten, hur långt ledningarna måste dras och hur material kan köras fram mellan villa och staket. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får attefallshuset i Bromma stå på prickmark?",
     "Ja, Stockholms stad skriver att ett komplementbostadshus som inte kräver lov får strida mot detaljplanen. Planen kan ändå ha skyddsbestämmelser eller krav på lov."),
    ("Behövs bygglov för ett attefallshus i Södra Ängby?",
     "Ja, i regel. Ålstensgatan och Södra Ängby är riksintresse för kulturmiljövården, och Stockholms stad skriver att bygglov krävs inom sådana områden. Kontrollera fastigheten på Stadsmuseets karta."),
    ("Vem ger medgivande om huset ska stå nära gatan i Bromma?",
     "Kommunen är oftast huvudman för gatan. I Stockholm skickar du förfrågan om medgivande till stadsbyggnadskontoret."),
    ("Hur lång tid tar det att få startbesked för vatten och avlopp i Stockholm?",
     "Staden skriver att beslutet ska komma inom fyra veckor från att anmälan är komplett. Tiden kan förlängas en gång för stora ärenden."),
    ("Räcker anmälan till byggnadsnämnden för att koppla in vatten i Bromma?",
     "Nej, anslutningen till stadens ledningsnät anmäls separat till Stockholm Vatten och Avfall."),
  ],
  "sources": [_PBL, _PBF, _BOV, _VARSAM, _RUFS, _SB_KBH, _SB_KLASS, _SB_VA, _SKV],
  "cta": ("Funderar du på ett attefallshus i Bromma?", "Boka ett gratis platsbesök, så går vi igenom planen, placeringen och ledningarna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet nybyggt trähus med sadeltak längst in i en villaträdgård med äppelträd och häck",
     "small newly built one-storey Swedish timber guest house with a gable roof and pale grey standing board facade at the back of a lush villa garden, apple trees, trimmed hedge, a 1920s garden city villa partly visible in the foreground, Bromma Stockholm, early summer evening light"),
    ("Utstakning med pinnar och snöre på en gräsmatta bakom en villa inför ett litet hus",
     "garden lawn behind a Swedish villa with wooden stakes and a string line marking out the footprint of a small house, a folding measuring tape lying on the grass, hedge and fence in the background, soft overcast daylight"),
  ],
},

# ------------------------------------------------------------------ DANDERYD
"attefallshus-danderyd.html": {
  "kind": "district", "service": "attefallshus", "ort": "Danderyd", "svc_label": "Attefallshus",
  "title": "Attefallshus i Danderyd – villastad, lovplikt och strand",
  "description": "Attefallshus i Danderyd: lovplikt i Djursholms och Stocksunds kulturmiljöer, frivilligt bygglov, kommunens medgivande och strandskydd vid äldre planer.",
  "h1": "Attefallshus i Danderyd",
  "lead": "På en stor naturtomt i Danderyd finns ofta plats för ett litet hus till, men i villastäderna är det sällan bara måtten som avgör. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och börjar med att ta reda på om tomten ligger i ett område där kommunen kräver bygglov.",
  "card": "Villastäder, lovplikt och strandskydd.",
  "sections": [
    {"id": "villastad-danderyd", "anchor": "Villastäderna",
     "h2": "Djursholm och Stocksund – riksintresse sedan 1987",
     "paras": [
       "Danderyds översiktsplan beskriver två större riksintressen för kulturmiljövården, Djursholms villastad och Stocksunds villastad, utpekade sedan 1987. Djursholm var landets första villastad anlagd som förort, och bebyggelsen speglar främst åren 1890–1930. Uttrycket för riksintresset är bland annat det oregelbundna planmönstret kring Roslagsbanan, de stora naturtomterna och villorna. Stocksund präglas av ett planmönster anpassat till den kuperade terrängen. Översiktsplanen har preciserat riksintressena i 11 värdekärnor, och kommunen arbetar med detaljplaner för de 9 värdekärnorna i Djursholm.",
       "Region Stockholm räknar Stocksund och Djursholm till de riksintressen i länet som är särskilt känsliga för förändring. Det märks i kommunens besked om de nya reglerna: inom kulturhistoriskt värdefulla områden och riksintressen för kulturmiljövården gäller lovplikt, även för ett komplementbostadshus som annars hade varit lovfritt. Kommunens kulturmiljökarta visar om tomten eller byggnaderna på den är utpekade.",
     ],
     "aside": {"title": "Riksintressen i Danderyd", "items": [
       "Djursholms villastad (AB 38)", "Stocksunds villastad (AB 48)",
       "11 värdekärnor i översiktsplanen", "Lovplikt i kulturmiljöerna"]}},
    {"id": "frivilligt-danderyd", "h2": "Lovfritt eller frivilligt bygglov",
     "paras": [
       "Utanför de utpekade områdena får du bygga huset utan lov om det håller sig inom 30,0 kvadratmeter byggnadsarea och 4,0 meter till nocken, och om alla lovfria byggnader på tomten tillsammans stannar vid 45,0 kvadratmeter. Kommunen påpekar att det då inte görs någon granskning innan bygget börjar, och att ansvaret för att lagens krav uppfylls ligger på dig som fastighetsägare.",
       "Den som vill ha ett besked i förväg kan söka ett frivilligt bygglov. Med ett sådant beslut från byggnadsnämnden vet du att huset du planerar uppfyller kraven. Vi bedömer att det kan vara värt det när tomten ligger nära gränsen till en värdekärna eller när huset ska hyras ut. Vill du hellre bygga ihop ytan med villan finns " + _L.format("tillbyggnad-danderyd.html", "tillbyggnad i Danderyd") + ", och måtten med paragrafer står i " + _REG + ".",
     ],
     "aside": None},
    {"id": "va-grans-danderyd", "h2": "VA-enheten, startbesked och gränsen mot gatan",
     "paras": [
       "Kommunen skriver att ett komplementbostadshus kan behöva anmälan och startbesked trots lovbefrielsen, till exempel när en anläggning för vatten och avlopp installeras i huset eller på tomten, eller när huset får ventilation. Ökar bruttoarean på fastigheten ska du dessutom själv informera kommunens VA-enhet.",
       "Närmare än 4,5 meter från gränsen krävs skriftliga medgivanden från alla berörda grannar. I vissa fall kan kommunen lämna medgivandet mot gata, torg, park eller naturområden. Förfrågan skickas via självservice med en skalenlig situationsplan, måttsatt mot fastighetsgränsen. Placeringen får inte hindra drift och underhåll av den allmänna platsen eller försämra sikten. Kommunen påminner om att detaljplanen ibland stoppar en placering nära gränsen, även om grannen säger ja.",
     ],
     "aside": {"title": "Till kommunen", "items": [
       "Anmälan för VA och ventilation", "Information till VA-enheten",
       "Medgivande mot allmän plats", "Situationsplan i skala"]}},
    {"id": "strand-danderyd", "h2": "Strandskydd längs kusten och vid Rösjön",
     "paras": [
       "Det generella strandskyddet gäller 100 meter från strandkanten, på land och i vattnet. Danderyds kommun skriver att strandskyddet inte gäller där en detaljplan antogs före den 1 juli 1975, och att kuststräckan till stor del är planlagd genom sådana äldre planer. När en äldre plan ersätts av en ny återinträder strandskyddet, och i nya planer står det om det har upphävts.",
       "Vid Sätra ängar, Cedergrenska parken och Rösjön är strandskyddet utökat. Ligger tomten inom strandskyddet där krävs i regel dispens för ett nytt hus, och det är miljö- och stadsbyggnadsnämnden som prövar ansökan. Att huset är lovfritt enligt plan- och bygglagen påverkar inte strandskyddet, som regleras i miljöbalken.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett attefallshus till i Danderyd",
  "steps": [
    ("Kartan först", "Vi kontrollerar kulturmiljökartan, detaljplanen och strandskyddet."),
    ("Lovväg", "Lovfritt, frivilligt bygglov eller bygglov – vi väljer väg tillsammans."),
    ("Ritningar", "Plan, fasader och en situationsplan med mått mot gränserna."),
    ("Anmälan", "VA och ventilation anmäls och VA-enheten informeras."),
    ("Byggnation", "Grund, stomme och installationer fram till nyckelfärdigt hus."),
    ("Överlämning", "Genomgång av huset och handlingarna du ska spara."),
  ],
  "rot_h2": "Attefallshuset räknas som nybyggnad – inget rotavdrag",
  "rot": [
    "Rotavdraget gäller arbete på en bostad som redan finns. Skatteverket skriver att det inte går att få rotavdrag för att bygga en helt ny bostad, och att avdraget inte gäller ett helt nytt hus eller en liknande fristående byggnad på tomten. Ett komplementbostadshus i trädgården är just en sådan ny byggnad, så priset vi lämnar är utan avdrag.",
  ],
  "price_h2": "Vad påverkar kostnaden för ett attefallshus i Danderyd?",
  "price": [
    "Storlek och standard, om huset får kök och badrum, grund i kuperad eller bergig terräng, hur långt det är till villans ledningar och om ett bygglov behövs. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi bygga attefallshus utan lov i Djursholm?",
     "Inte om tomten ligger i ett kulturhistoriskt värdefullt område eller riksintresse – där gäller lovplikt enligt kommunen. Kulturmiljökartan visar vad som gäller för fastigheten."),
    ("Vad är ett frivilligt bygglov för ett attefallshus?",
     "Ett lov du söker fast åtgärden är lovfri. Beslutet från byggnadsnämnden bekräftar att det planerade huset uppfyller lagens krav."),
    ("Måste Danderyds VA-enhet få veta att vi bygger ett gästhus?",
     "Ja, när en lovfri åtgärd ökar bruttoarean på fastigheten ska du enligt kommunen själv informera VA-enheten."),
    ("Gäller strandskyddet på villatomter vid vattnet i Danderyd?",
     "Inte där en detaljplan från före den 1 juli 1975 gäller. Ersätts planen återinträder strandskyddet, så den aktuella planen avgör."),
    ("Kan kommunen ge medgivande när attefallshuset ska stå nära en park i Danderyd?",
     "I vissa fall, ja – mot gata, torg, park och naturområden kan kommunen lämna medgivande. Du skickar en skalenlig situationsplan via självservice."),
  ],
  "sources": [_PBL, _PBF, _BOV, _DAN_OP, _RUFS, _DAN_NYA, _DAN_SS, _MB, _SKV],
  "cta": ("Funderar du på ett attefallshus i Danderyd?", "Boka ett gratis platsbesök, så tittar vi på kartan, planen och strandskyddet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet mörkt trähus med pulpettak bland tallar och berghällar på en stor villatomt",
     "small modern dark-stained timber guest house with a mono-pitch roof set among pine trees and smooth granite outcrops on a large wooded villa plot, an older early 1900s wooden villa glimpsed behind the trees, Djursholm Danderyd Sweden, late afternoon sun"),
    ("Grund med plintar på en sluttande naturtomt med berg i dagen och tallar",
     "construction site on a sloping natural plot with exposed granite bedrock, concrete pier foundations and a timber floor frame being prepared for a small house, pine trees around, overcast daylight, Sweden"),
  ],
},

# ------------------------------------------------------------------ EKERÖ
"attefallshus-ekero.html": {
  "kind": "district", "service": "attefallshus", "ort": "Ekerö", "svc_label": "Attefallshus",
  "title": "Attefallshus på Ekerö – utanför plan, strand och avlopp",
  "description": "Attefallshus på Ekerö: 50 m² utanför detaljplan, riksintressen på Mälaröarna, strandskydd upp till 300 m och tillstånd för toalett till eget avlopp.",
  "h1": "Attefallshus på Ekerö",
  "lead": "På Mälaröarna ligger många villor och permanentade fritidshus utan detaljplan, och då blir både huset och reglerna annorlunda än i staden. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och reder ut plan, kulturmiljö, strandskydd och avlopp innan bygget planeras.",
  "card": "Utanför plan, strandskydd och eget avlopp.",
  "sections": [
    {"id": "utanfor-plan-ekero", "anchor": "Utanför detaljplan",
     "h2": "Utanför detaljplan får huset bli 50 kvadratmeter",
     "paras": [
       "Ekerö kulturmiljöprogram från 2015 beskriver ett högt bebyggelsetryck, med nya bostäder och permanentning av fritidshus i snabb takt, och konstaterar att många av nybyggnaderna och förtätningarna sker utanför detaljplanelagt område. För ett attefallshus är det en avgörande fråga. Utanför detaljplan får huset ha upp till 50,0 kvadratmeter byggnadsarea och 4,5 meter till nocken, och alla lovfria komplementbyggnader på tomten får tillsammans vara 65,0 kvadratmeter. Inom detaljplan gäller 30,0, 4,0 och 45,0.",
       "Två villkor gäller oavsett läge: huset ska ha mindre byggnadsarea än bostadshuset det kompletterar, och det ska stå inom tomten. Kommunen skriver att tidigare friggebodar och attefallsåtgärder räknas in i de totala ytorna. Ett tänkt räkneexempel: är bostadshuset på tomten en äldre stuga med 40 kvadratmeter byggnadsarea måste det nya huset vara mindre än 40 kvadratmeter, trots att gränsen utanför detaljplan är 50,0.",
     ],
     "aside": {"title": "Utanför detaljplan", "items": [
       "Högst 50,0 m² byggnadsarea", "Taknock högst 4,5 m",
       "Högst 65,0 m² lovfritt på tomten", "Mindre än huvudbyggnaden"]}},
    {"id": "kulturmiljo-ekero", "h2": "Två världsarv och flera riksintressen",
     "paras": [
       "Ekerö är enligt kulturmiljöprogrammet den enda kommunen i landet med två världsarv. Stora delar av Adelsö ingår i riksintresset Adelsö–Björkö–Birka, stora delar av Norra Munsö är riksintresse med rundkyrkan och herrgårdsmiljöerna, och Södra Munsö med Kärsö utgör ett herrgårdslandskap av riksintresse. Även herrgårdslandskapet kring Stavsund och östra Helgö pekas ut, och Region Stockholm listar Stenhamra (AB 28) som riksintresse. Enligt programmet gäller områdesbestämmelser med utökad lovplikt kring Munsö kyrka, där bland annat ekonomibyggnader kräver lov.",
       "Kommunen skriver att de nya lovbefrielserna inte kan användas i särskilt värdefulla områden enligt kommunens karta, och inte heller där en detaljplan har skyddsbestämmelser mot föroreningar, olyckor, översvämning eller erosion. Samma karta visar totalförsvarets riksintressen, där kommunen skriver att ett komplementbostadshus inte får byggas lovfritt (9 kap. 36 §). Programmets bilaga om att bygga nytt i gammal bygd betonar skala, gestaltning och noggrann markberedning, och att ett modernt men genomtänkt hus kan passa bättre än ett historiserande. Det tar vi med oss när vi ritar ett hus nära en gård eller ett odlingslandskap.",
     ],
     "aside": None},
    {"id": "strand-ekero", "h2": "Strandskydd på 100 till 300 meter",
     "paras": [
       "Ekerö kommun skriver att det generella strandskyddet är 100 meter från strandkanten men på vissa ställen upp till 300 meter, och att det gäller både på land och i vattnet. Miljöbalken förbjuder nya byggnader inom strandskyddsområdet, så ett lovfritt attefallshus vid Mälaren behöver i regel ändå dispens om det hamnar där. Det krävs särskilda skäl, till exempel att platsen redan är ianspråktagen eller väl avskild från stranden av en väg eller bebyggelse.",
       "Till ansökan vill kommunen ha en beskrivning av vad som ska byggas och av de särskilda skälen, en situationsplan, fasad- och planritningar, en beskrivning av växt- och djurlivet och uppgifter om servitut. Därför ritar vi huset färdigt innan ansökan lämnas, så att dispensen gäller just den placering som ska byggas. Om altaner, bryggor och gäststugor i övrigt finns mer under " + _L.format("snickare-ekero.html", "snickare på Ekerö") + ".",
     ],
     "aside": {"title": "Dispensansökan", "items": [
       "Beskrivning och särskilda skäl", "Situationsplan",
       "Fasad- och planritningar", "Växt- och djurliv"]}},
    {"id": "avlopp-ekero", "h2": "Eget avlopp: tillstånd när toaletten kopplas in",
     "paras": [
       "Många fastigheter utanför planlagda områden har eget avlopp. Ekerö kommun skriver att ett nytt enskilt avlopp kräver tillstånd och att en ändring av en befintlig anläggning oftast kräver anmälan. Förordningen om miljöfarlig verksamhet är tydlig på en punkt: att ansluta en vattentoalett till en befintlig avloppsanordning kräver tillstånd. Ett attefallshus med toalett som kopplas till villans gamla anläggning hamnar alltså i den kategorin.",
       "Kommunen råder dig att kontakta miljöenheten för rådgivning innan ansökan. Anläggningen för vatten och avlopp anmäls dessutom till byggnadsnämnden enligt plan- och byggförordningen, och arbetet väntar på startbesked. Finns kommunalt vatten och avlopp anmäler du inkopplingen till Roslagsvatten i god tid före byggstart. Mer om måtten och paragraferna finns i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus på Ekerö",
  "steps": [
    ("Läget", "Detaljplan eller inte, kulturmiljö och strandskydd för just din fastighet."),
    ("Storleken", "Vi räknar ut hur stort huset får bli utifrån villan och potten."),
    ("Avloppet", "Ny anläggning, ansluten till befintlig eller kommunalt VA."),
    ("Ansökningar", "Dispens, avloppstillstånd och anmälan med ritningar."),
    ("Bygget", "Grund, stomme och installationer fram till inflyttning."),
    ("Avslut", "Slutgenomgång och de handlingar du behöver spara."),
  ],
  "rot_h2": "Rotavdrag gäller inte ett nytt attefallshus",
  "rot": [
    "Skatteverket ger inget rotavdrag för att bygga ett helt nytt hus eller en liknande fristående byggnad på tomten, och inte heller för att bygga en helt ny bostad. Ett komplementbostadshus på Ekerö är nybyggnad, även om det står på samma tomt som villan, och därför räknar vi priset för huset utan avdrag.",
  ],
  "price_h2": "Vad styr priset på ett attefallshus på Ekerö?",
  "price": [
    "Storlek upp till 50 kvadratmeter, grund på berg eller lera, avloppslösningen, avståndet till befintliga ledningar och hur material kan transporteras till tomten. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur stort attefallshus får vi bygga på en tomt utan detaljplan på Ekerö?",
     "Upp till 50,0 kvadratmeter byggnadsarea och 4,5 meter till nocken, men mindre än bostadshuset. Alla lovfria byggnader på tomten får tillsammans vara 65,0 kvadratmeter."),
    ("Behöver vi tillstånd om attefallshusets toalett kopplas till vårt egna avlopp?",
     "Ja. Att ansluta en vattentoalett till en befintlig avloppsanordning kräver tillstånd enligt förordningen om miljöfarlig verksamhet och hälsoskydd."),
    ("Hur långt från Mälaren gäller strandskyddet på Ekerö?",
     "Normalt 100 meter från strandkanten, på vissa ställen upp till 300 meter, både på land och i vattnet."),
    ("Kan ett lovfritt attefallshus byggas i ett riksintresse på Mälaröarna?",
     "Inte i de särskilt värdefulla områden som kommunens karta visar. Där gäller inte lovbefrielserna, och kring Munsö kyrka finns dessutom områdesbestämmelser."),
    ("Kan vår lilla stuga begränsa hur stort det nya attefallshuset blir?",
     "Ja, om stugan är bostadshuset på tomten. Det nya huset ska ha mindre byggnadsarea än bostadshuset det kompletterar."),
  ],
  "sources": [_PBL, _PBF, _BOV, _EK_VAD, _EK_KMP, _RUFS, _EK_SS, _MB, _EK_AVL, _FMH, _SKV],
  "cta": ("Funderar du på ett attefallshus på Ekerö?", "Boka ett gratis platsbesök, så tittar vi på plan, strand och avlopp innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet rödmålat trähus med vita knutar på en gräsyta vid en äldre gård med åkermark bakom",
     "small new red painted wooden house with white corner boards and a black metal roof on a lawn next to an older Swedish farmhouse, open farmland and oak trees behind, Mälaren islands Ekerö landscape, calm summer day"),
    ("Grön markbädd och slamavskiljarlock på en gräsyta bredvid ett litet hus på landet",
     "rural Swedish garden with a green plastic septic tank lid and inspection pipes of a soil infiltration bed in the lawn, a small wooden guest house in the background, birch trees, overcast daylight"),
  ],
},

# ------------------------------------------------------------------ NORRTÄLJE
"attefallshus-norrtalje.html": {
  "kind": "district", "service": "attefallshus", "ort": "Norrtälje", "svc_label": "Attefallshus",
  "title": "Attefallshus i Norrtälje – stuga, strandskydd och avlopp",
  "description": "Attefallshus i Norrtälje: hur stort huset får bli bredvid en liten stuga, riksintressen i Roslagen, strandskydd i miljöbalken och tillstånd för avloppet.",
  "h1": "Attefallshus i Norrtälje",
  "lead": "Norrtälje har fler fritidshus än någon annan kommun, och många tomter i Roslagen har plats för ett litet hus till. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och börjar med frågorna som brukar avgöra här: hur stort huset får bli, var stranden går och vad som händer med avloppet.",
  "card": "Stugtomter, strandskydd och avlopp.",
  "sections": [
    {"id": "stugtomt-norrtalje", "anchor": "Stugtomten",
     "h2": "Bredvid en liten stuga blir huset mindre",
     "paras": [
       "SCB räknade 27 352 fritidshus i Norrtälje kommun 2025, flest i landet. Ett komplementbostadshus ska enligt plan- och bygglagen komplettera ett en- eller tvåbostadshus, och dess byggnadsarea ska vara mindre än byggnadsarean för det hus det kompletterar. Ett tänkt exempel: är bostadshuset på tomten en sommarstuga med 35 kvadratmeter byggnadsarea måste det nya huset vara mindre än 35 kvadratmeter för att vara lovfritt, oavsett vad gränserna i övrigt tillåter.",
       "Ligger tomten utanför detaljplan får huset ha högst 50,0 kvadratmeter byggnadsarea och 4,5 meter till nocken. Alla lovfria komplementbyggnader och komplementbostadshus på tomten får då tillsammans vara 65,0 kvadratmeter, och den gamla friggeboden eller vedboden räknas in. Inom detaljplan gäller 30,0 kvadratmeter, 4,0 meter och 45,0 kvadratmeter.",
     ],
     "aside": {"title": "Gäller samtidigt", "items": [
       "Mindre än huvudbyggnaden", "50,0 m² utanför detaljplan",
       "65,0 m² lovfritt på tomten", "4,5 m till gräns"]}},
    {"id": "riksintresse-norrtalje", "h2": "Riksintressen från staden till Arholma",
     "paras": [
       "Region Stockholms sammanställning visar flera riksintressen för kulturmiljövården i kommunen: Norrtälje stad som småstadsmiljö (AB 84), industrimiljön i Hallstavik (AB 96), gruv- och brukssamhället Herräng (AB 97), Grisslehamn (AB 98), Skebobruk och Edsbro (AB 93) och skärgårdsmiljön på Arholma (AB 619). Norrtälje stad nämns bland de riksintressen i länet som löper stor risk för påverkan vid förändring.",
       "Plan- och bygglagen kräver bygglov för nybyggnad i ett särskilt värdefullt bebyggelseområde och där en detaljplan eller områdesbestämmelser skyddar särskilda värden (9 kap. 37 §). Ett riksintresse är inte automatiskt ett sådant område, men ligger tomten i ett av områdena ovan tar vi reda på hur kommunen bedömer platsen innan vi ritar, i stället för att utgå från att huset är lovfritt.",
     ],
     "aside": None},
    {"id": "strand-norrtalje", "h2": "Strandskyddet följer miljöbalken, inte lovreglerna",
     "paras": [
       "Strandskyddet omfattar enligt miljöbalken land och vatten intill 100 meter från strandlinjen, och länsstyrelsen kan i det enskilda fallet utvidga området till högst 300 meter. Inom området får inga nya byggnader uppföras, och inte heller grävas eller förberedas för dem. Ett attefallshus som är lovfritt enligt plan- och bygglagen kräver alltså i regel ändå dispens om det hamnar inom strandskyddet. Länsstyrelsen skriver att vissa kompletterande åtgärder till en huvudbyggnad inte behöver dispens, men enligt 7 kap. 17 § gäller det bara inom 15 meter från huvudbyggnaden, inte närmare strandlinjen än 25 meter och inom en tomtplats som angetts i ett dispensbeslut.",
       "Kommunen beslutar i de flesta fall om dispens, och det krävs särskilda skäl. Två sådana är att området redan har tagits i anspråk så att det saknar betydelse för strandskyddet, eller att det är väl avskilt från stranden av en väg eller bebyggelse. I beslutet ska det stå hur mycket mark som får användas som tomt. Sedan den 1 juli 2025 gäller strandskyddet inte vid små sjöar på högst en hektar och vattendrag på högst två meters bredd, och Länsstyrelsen påpekar att kartskiktet fortfarande kan visa strandskydd vid sådana vatten. Därför kan vattnet behöva mätas på plats. Om pentry, altan och snickeri i stugan finns mer under " + _L.format("snickare-norrtalje.html", "snickare i Norrtälje") + ".",
     ],
     "aside": {"title": "Inom 100 meter", "items": [
       "Inga nya byggnader", "Inga förberedande markarbeten",
       "Dispens med särskilda skäl", "Tomtplatsen anges i beslutet"]}},
    {"id": "avlopp-norrtalje", "h2": "Avloppet: tillstånd, anmälan eller servisanmälan",
     "paras": [
       "Förordningen om miljöfarlig verksamhet och hälsoskydd skiljer på avlopp med och utan toalett. Det krävs tillstånd för att inrätta en avloppsanordning som en vattentoalett ska anslutas till, och för att ansluta en vattentoalett till en befintlig anordning. Ett avlopp utan toalett, till exempel för dusch och disk, anmäls i stället till den kommunala nämnden, om inte kommunen har föreskrivit tillstånd för delar av kommunen, och en ändring som väsentligt påverkar avloppsvattnets mängd eller sammansättning ska också anmälas.",
       "Har fastigheten kommunalt vatten och avlopp ska du snarast meddela Norrtälje Vatten och Avfall om antalet bostadslägenheter ändras, genom en servisanmälan. Är fastigheten ansluten via en VA-samfällighet anmäls förändringen i stället till samfälligheten. Installationerna anmäls även till byggnadsnämnden innan de görs. Alla mått och paragrafer finns samlade i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Norrtälje",
  "steps": [
    ("Platsbesök", "Vi mäter huvudbyggnaden, befintliga bodar och avståndet till vatten och gräns."),
    ("Ytan", "Vi räknar ut hur stort det nya huset får bli."),
    ("Prövningar", "Strandskydd, kulturmiljö och avlopp reds ut före ritningarna."),
    ("Ansökan och anmälan", "Dispens, avloppstillstånd och anmälan med ritningar."),
    ("Bygget", "Grund, stomme och installationer till inflyttningsklart hus."),
    ("Genomgång", "Vi går igenom huset och handlingarna med dig."),
  ],
  "rot_h2": "Inget rotavdrag för ett nytt hus på tomten",
  "rot": [
    "Det är lätt att tro att ett hus på den egna tomten räknas som en förbättring av fastigheten, men Skatteverket säger något annat. Att bygga ett helt nytt hus, en friggebod, ett garage, ett växthus eller en liknande fristående byggnad ger inget rotavdrag på ett småhus. Attefallshuset är nybyggnad, och därför redovisar vi priset utan avdrag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Norrtälje?",
  "price": [
    "Storleken, grundläggningen på berg eller mark, vilken avloppslösning som krävs, om det finns vatten indraget i dag och hur långt det är till tomten för material och personal. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får attefallshuset vara större än vår sommarstuga i Roslagen?",
     "Inte utan bygglov. Byggnadsarean ska vara mindre än byggnadsarean för det hus som komplementbostadshuset kompletterar."),
    ("Kan vi bygga ett attefallshus 60 meter från stranden i Norrtälje utan dispens?",
     "I regel inte, om platsen ligger inom strandskyddet. Miljöbalken förbjuder nya byggnader inom 100 meter från strandlinjen, och lovfriheten ändrar inte det."),
    ("Krävs avloppstillstånd för ett attefallshus med bara dusch och diskbänk?",
     "Ett avlopp utan vattentoalett kräver anmälan till den kommunala nämnden, om inte kommunen har föreskrivit tillstånd. Tillstånd krävs när en vattentoalett ska anslutas."),
    ("Vem ska veta om attefallshuset när vi har VA via en samfällighet i Norrtälje?",
     "Enligt Norrtälje Vatten och Avfall anmäler du förändringen till VA-samfälligheten och inte direkt till dem."),
    ("Behövs bygglov för ett attefallshus i Grisslehamn?",
     "Grisslehamn är riksintresse för kulturmiljövården. Räknas platsen som särskilt värdefull krävs bygglov enligt 9 kap. 37 §, så fråga kommunen först."),
  ],
  "sources": [_PBL, _PBF, _BOV, _SCB, _RUFS, _MB, _LST, _FMH, _NVAA, _SKV],
  "cta": ("Funderar du på ett attefallshus i Norrtälje?", "Boka ett gratis platsbesök, så går vi igenom ytan, stranden och avloppet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet nytt trähus i falurött bredvid en äldre sommarstuga på en klippig tomt i Roslagen",
     "small new falu red wooden guest house with white trim next to an older Swedish summer cottage on a rocky plot with pine trees and smooth granite, glimpse of a calm bay in the distance, Roslagen Norrtälje archipelago, bright summer day"),
    ("Måttband mellan strandkant och en utstakad husplats på en tomt med tallar",
     "rocky shoreline plot in the Swedish archipelago with a yellow measuring tape stretched from the water's edge up towards wooden stakes marking a house site among pine trees, calm water, soft morning light"),
  ],
},

# ------------------------------------------------------------------ TÄBY
"attefallshus-taby.html": {
  "kind": "district", "service": "attefallshus", "ort": "Täby", "svc_label": "Attefallshus",
  "title": "Attefallshus i Täby – detaljplan, Q-märkning och VA",
  "description": "Attefallshus i Täby: lovfritt i villaområdena om inte planen har q-bestämmelser, strandskydd på kvartersmark, VA-anmälan och Roslagsvattens regler.",
  "h1": "Attefallshus i Täby",
  "lead": "Ligger villatomten i Täby inom detaljplan kan ett attefallshus byggas utan bygglov, så länge måtten och planen tillåter det. Men planen kan innehålla skyddsbestämmelser, och installationerna för vatten och avlopp behöver i regel anmälas. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och tar hand om underlaget till kommunen och Roslagsvatten.",
  "card": "Detaljplan, Q-märkning och VA-inkoppling.",
  "sections": [
    {"id": "plan-taby", "anchor": "Detaljplanen",
     "h2": "Lovfritt i villaområdet – utom där planen skyddar",
     "paras": [
       "Täby kommun skriver att ett komplementbostadshus sedan den 1 december 2025 kan uppföras utan bygglov och oftast utan anmälan. Lov behövs om huset inte ryms i de lovbefriade måtten, om fastigheten har kulturhistoriska värden eller om detaljplanen har utökad lovplikt. Inom detaljplan betyder måtten högst 30,0 kvadratmeter byggnadsarea, 4,0 meter till nocken och sammanlagt 45,0 kvadratmeter lovfritt på tomten.",
       "Kunskapsunderlaget Kulturmiljöer i Täby förklarar att skyddsbestämmelser i detaljplanen ofta betecknas med Q, q eller rivningsförbud på plankartan. Underlaget skriver också att många bygglovsbefriade åtgärder inte får utföras på byggnader eller i områden som bedöms vara särskilt värdefulla, att varsamhetskravet gäller alla byggnader och att särskilt värdefull bebyggelse inte får förvanskas. Varje fastighetsägare ansvarar själv för att kontrollera vad som gäller, så plankartan är det första vi tittar på.",
     ],
     "aside": {"title": "Lov behövs när", "items": [
       "Måtten överskrids", "Fastigheten har kulturvärden",
       "Planen har utökad lovplikt", "Skydd i detaljplanen"]}},
    {"id": "riksintresse-taby", "h2": "Skålhamravägen och Täby prästgårdsmark",
     "paras": [
       "Täby har två riksintressen för kulturmiljövården: Skålhamravägen (AB 71), en vägsträckning med förhistoriskt ursprung genom ett odlingslandskap med runristningar och stensträngar, och Täby prästgårdsmark (AB 73), en fornlämningsmiljö med rötter i bronsåldern. Kommunens underlag skriver att ett område av riksintresse sannolikt också är ett sådant särskilt värdefullt område som plan- och bygglagen avser.",
       "För de flesta villaområden är riksintressena långt borta, men för gårdar och hus längs Skålhamravägen eller nära prästgården betyder det att ett nytt hus på tomten kan kräva bygglov. Underlaget beskriver också värdefulla miljöer i tätorten och äldre gårdsmiljöer, och det läser vi innan vi föreslår form, färg och placering. Vår bedömning är att ett litet hus som underordnar sig villan och följer tomtens nivåer är lättast att få in i en sådan miljö. Hör huset till ett grupphusområde tittar vi också på hur grannhusens förråd och carportar är placerade, så att det nya huset inte bryter mönstret längs gatan.",
     ],
     "aside": None},
    {"id": "strand-taby", "h2": "Strandskydd på villatomter nära vatten",
     "paras": [
       "Ligger tomten nära vatten är strandskyddet nästa fråga. Täby kommun skriver att du inte behöver söka strandskyddsdispens för åtgärder på kvartersmark inom detaljplanerat område när strandskyddet har upphävts genom detaljplanen. Det gäller till exempel bostadsfastigheter, och kommunens detaljplaner visar om din fastighet ligger inom ett sådant område.",
       "Utanför sådana planer krävs dispens för att bygga nytt, för att ändra byggnader eller deras användning och för att utöka den privata hemfridszonen. Dispens kräver särskilda skäl, och kommunen skriver att de bedöms väldigt noggrant. Till ansökan hör situationsplan, plan-, fasad- och sektionsritningar och fotografier. Vill du i stället bygga ihop ytan med villan finns " + _L.format("tillbyggnad-taby.html", "tillbyggnad i Täby") + ".",
     ],
     "aside": {"title": "Ingen dispens när", "items": [
       "Tomten är kvartersmark", "Detaljplanen upphäver strandskyddet",
       "Planen visar det för fastigheten", "Annars: dispens först"]}},
    {"id": "va-taby", "h2": "Anmälan till kommunen och inkoppling hos Roslagsvatten",
     "paras": [
       "Ett hus att bo i får vatten, avlopp och ventilation, och då krävs i regel anmälan och startbesked enligt plan- och byggförordningen. Täby kommun räknar upp vad som ofta ska med: anmälan via blankett eller e-tjänst, redovisning av vatten- och avloppsanordningarna, planritning och sektionsritning och ett förslag på kontrollplan. Är arbetet mer omfattande behövs en kontrollansvarig. Ska huset hyras ut som självständig bostad söker du dessutom en ny adress hos kommunens geodataenhet.",
       "Roslagsvatten sköter vatten och avlopp i Täby och vill ha en VA-anmälan med ritning över ledningsdragningen i god tid före byggstart. Vattenledningen kopplas efter vattenmätaren, och spillvattnet ansluts till fastighetens befintliga spillvattenledning, helst via en rensbrunn. Dag- och dräneringsvatten får inte gå till spillvattnet. Roslagsvatten varnar också för sämre vattentryck om huset ligger högre och längre bort från förbindelsepunkten. Måtten och paragraferna i stort finns i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Täby",
  "steps": [
    ("Plankartan", "Vi kontrollerar Q- och q-bestämmelser, utökad lovplikt och strandskydd."),
    ("Placering", "Huset ritas in med mått mot gränser och befintliga ledningar."),
    ("VA-underlag", "Ritning över ledningsdragningen och förslag på kontrollplan."),
    ("Anmälningar", "Till kommunen och Roslagsvatten innan byggstart."),
    ("Bygget", "Grund, stomme, installationer och ytskikt."),
    ("Inflyttning", "Genomgång och adress om huset ska hyras ut."),
  ],
  "rot_h2": "Attefallshuset ger inte rotavdrag",
  "rot": [
    "Rotavdrag gäller reparation, underhåll och om- och tillbyggnad av en befintlig bostad. Skatteverket skriver uttryckligen att det inte ges för att bygga ett helt nytt hus eller en liknande fristående byggnad på småhustomten, och ett komplementbostadshus är en sådan. Priset för huset lämnar vi därför utan rotavdrag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Täby?",
  "price": [
    "Storlek och planlösning, kök och badrum, grundläggning, längden på ledningarna till villans spillvatten och vattenmätare och om en kontrollansvarig behövs. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad betyder q på plankartan för vårt attefallshus i Täby?",
     "Att planen har skyddsbestämmelser för kulturvärden. Omfattar de tomten eller området krävs bygglov för ett nytt hus enligt 9 kap. 37 §, så läs bestämmelsen noga."),
    ("Behöver vi strandskyddsdispens för ett attefallshus på en villatomt vid vattnet i Täby?",
     "Inte om tomten är kvartersmark i en detaljplan som upphäver strandskyddet. Kommunens detaljplaner visar vad som gäller."),
    ("Var ska spillvattnet från attefallshuset kopplas in hos Roslagsvatten?",
     "Till fastighetens befintliga spillvattenledning inom tomten, helst via en rensbrunn. Vattnet kopplas efter vattenmätaren."),
    ("Behöver ett attefallshus för uthyrning i Täby en egen adress?",
     "Ja, om det ska vara en självständig bostad som används som bostad söker du ny adress hos kommunens geodataenhet."),
    ("Vilka ritningar behövs för VA-anmälan till ett attefallshus i Täby?",
     "Kommunen nämner redovisning av vatten- och avloppsanordningarna, planritning och sektionsritning samt förslag på kontrollplan."),
  ],
  "sources": [_PBL, _PBF, _BOV, _TAB_KB, _TAB_KMP, _TAB_SS, _TAB_VA, _ROSL, _SKV],
  "cta": ("Funderar du på ett attefallshus i Täby?", "Boka ett gratis platsbesök, så går vi igenom plankartan och VA-inkopplingen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet ljusgrått trähus med sadeltak i en trädgård bakom en villa från 1970-talet",
     "small light grey timber guest house with a gable roof and a small wooden deck in the back garden of a 1970s Swedish suburban villa with brown wood panelling, lawn, birch and lilac, Täby Stockholm, sunny late summer afternoon"),
    ("Öppet schakt med nya grå avloppsrör och en rensbrunn i en villaträdgård",
     "open trench in a Swedish villa garden with new grey plastic sewer pipes and a round inspection chamber, blue water pipe alongside, sand bedding, small wooden house frame in the background, overcast day"),
  ],
},

# ------------------------------------------------------------------ VÄRMDÖ
"attefallshus-varmdo.html": {
  "kind": "district", "service": "attefallshus", "ort": "Värmdö", "svc_label": "Attefallshus",
  "title": "Attefallshus på Värmdö – fritidsområde, kulturmiljö, avlopp",
  "description": "Attefallshus på Värmdö: förändringsområden med plats för attefallshus, 14 riksintressen, 55 kulturmiljöområden, 100 m från strand och avloppstillstånd.",
  "h1": "Attefallshus på Värmdö",
  "lead": "Många fritidshusområden på Värmdö håller på att bli permanentområden, och ett litet hus på tomten är ett sätt att få plats med fler. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och reder ut plan, kulturmiljö, strand och avlopp innan vi ritar.",
  "card": "Fritidsområden, kulturmiljö och avlopp.",
  "sections": [
    {"id": "pfo-varmdo", "anchor": "Fritidshusområden",
     "h2": "Förändringsområden där tomten ska rymma ett attefallshus",
     "paras": [
       "SCB räknade 14 709 fritidshus på Värmdö 2025, näst flest i landet. Kommunens broschyr om fritidshusområden i förändring beskriver hur tusentals fastigheter i områden med många permanentboende ska planläggas och få kommunalt vatten och avlopp. Områdena som går först kallas prioriterade förändringsområden och pekas ut i översiktsplanen Värmdö 2035. Bland riktlinjerna står att fastighetens storlek bedöms utifrån områdets karaktär och att det inom fastigheten ska finnas plats för parkering, ett möjligt attefallshus och bergvärme.",
       "Så länge området saknar detaljplan gäller gränserna utanför plan: 50,0 kvadratmeter byggnadsarea, 4,5 meter till nocken och 65,0 kvadratmeter lovfritt på tomten. När den nya planen fått laga kraft gäller 30,0, 4,0 och 45,0 i stället. Står huset redan där när planen kommer räknas det in i potten. Att bygga före eller efter planen är därför ett val värt att göra medvetet, och vi går igenom vad det betyder för din tomt.",
     ],
     "aside": {"title": "Före och efter plan", "items": [
       "Utan plan: 50,0 m² och 4,5 m", "Utan plan: 65,0 m² på tomten",
       "Med plan: 30,0 m² och 4,0 m", "Med plan: 45,0 m² på tomten"]}},
    {"id": "kulturmiljo-varmdo", "h2": "Gustavsberg, Sandhamn och 55 kulturmiljöområden",
     "paras": [
       "Värmdö kommun skriver att det finns 14 områden av riksintresse och cirka 55 utpekade kulturmiljöområden i kommunen, och att alla räknas som särskilt värdefulla. Region Stockholms sammanställning nämner bland andra Gustavsberg (AB 56), Sandhamn–Grönskär (AB 610) och delar av Möja (AB 616), och räknar Gustavsberg till de riksintressen i länet som är särskilt känsliga för förändring.",
       "I kommunens information om de nya reglerna står att det inom kulturhistoriskt värdefulla områden och riksintressen för kulturmiljövården gäller lovplikt, och att kulturmiljökartan visar om fastigheten berörs. Kommunen ber dig tänka särskilt på material, färger, takets form och lutning och byggnadens placering, och kommunantikvarien hjälper till med råd. Kommunen påminner också om att strandskyddsdispens eller tillstånd från länsstyrelsen kan krävas även när åtgärden inte kräver bygglov.",
     ],
     "aside": None},
    {"id": "strand-varmdo", "h2": "Nära vattnet och nära grannen",
     "paras": [
       "Kommunen sammanfattar två saker som inte ändrades den 1 december 2025: utan tillstånd får du inte bygga närmare än 4,5 meter från tomtgränsen eller inom 100 meter från strand. På en strandnära skärgårdstomt kan det vara den andra gränsen som styr. Strandskyddet regleras i miljöbalken och förbjuder nya byggnader inom strandskyddsområdet, så ett lovfritt hus kräver i regel dispens med särskilda skäl.",
       "Placeringen avgör ofta om dispens alls är möjlig. Vår bedömning är att ett hus på den redan använda delen av tomten, bakom huvudbyggnaden sett från stranden, har bättre förutsättningar än ett hus på en orörd udde. Närmare än 4,5 meter från gränsen krävs skriftliga medgivanden från grannarna. Vill du i stället bygga ut huvudbyggnaden finns " + _L.format("tillbyggnad-varmdo.html", "tillbyggnad på Värmdö") + ".",
     ],
     "aside": {"title": "Gäller som förut", "items": [
       "4,5 m till tomtgräns", "100 m från strand",
       "Dispens med särskilda skäl", "Skriftligt grannmedgivande"]}},
    {"id": "avlopp-varmdo", "h2": "Avlopp: tillstånd för att ansluta en byggnad",
     "paras": [
       "Värmdö kommun skriver att du behöver ansöka om tillstånd om du vill ansluta en eller flera byggnader till din befintliga avloppsanläggning. Ett attefallshus med toalett, dusch och kök som kopplas till villans anläggning är just ett sådant fall. Tillståndet gäller exakt den tekniska lösning och den placering som visas på situationsplanen, och du ska vänta på kommunens skriftliga beslut innan arbetet börjar.",
       "Kommunen kan ge en preliminär bedömning av vilken skyddsnivå som gäller på fastigheten, men inte råda om vilken anläggning du ska välja. Anläggningen för vatten och avlopp i huset anmäls även till byggnadsnämnden innan den görs. Ligger tomten i ett förändringsområde där kommunalt VA ska byggas ut kan det påverka vilken lösning som är rimlig i väntan på ledningarna. Måtten och paragraferna i sin helhet finns i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus på Värmdö",
  "steps": [
    ("Tomten", "Plan eller inte, kulturmiljökartan och avståndet till strand och gräns."),
    ("Ytan", "Hur stort huset får bli i dag och efter en ny detaljplan."),
    ("Avloppet", "Befintlig anläggning, ny lösning eller väntan på kommunalt VA."),
    ("Tillstånd", "Dispens, avloppstillstånd och anmälan med ritningar."),
    ("Bygget", "Grund på berg eller mark, stomme och installationer."),
    ("Avslut", "Genomgång och de beslut och handlingar du ska spara."),
  ],
  "rot_h2": "Rotavdrag och attefallshus på Värmdö",
  "rot": [
    "Rotavdraget är till för arbete på en befintlig bostad. Skatteverket skriver att det inte går att få rotavdrag för att bygga en helt ny bostad, och att ett helt nytt hus eller en liknande fristående byggnad på småhustomten inte ger avdrag. Ett komplementbostadshus är nybyggnad, så vi lämnar priset utan rotavdrag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus på Värmdö?",
  "price": [
    "Storlek, grundläggning på berg, avloppslösningen, hur långt ledningar och el måste dras och om material kan köras fram eller måste bäras eller fraktas sista biten. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Ska vi bygga attefallshuset före eller efter den nya detaljplanen på Värmdö?",
     "Utan plan gäller 50,0 kvadratmeter och 4,5 meter, med plan 30,0 och 4,0. Ett hus som redan står där räknas in i potten när planen kommer."),
    ("Måste vi söka avloppstillstånd för ett attefallshus som kopplas till villans avlopp på Värmdö?",
     "Ja. Kommunen kräver tillstånd för att ansluta en eller flera byggnader till en befintlig avloppsanläggning."),
    ("Gäller lovfriheten för attefallshus i Gustavsberg?",
     "Gustavsberg är riksintresse för kulturmiljövården, och kommunen skriver att lovplikt gäller i sådana områden. Kulturmiljökartan visar om fastigheten berörs."),
    ("Hur många kulturmiljöområden finns det på Värmdö?",
     "Kommunen anger 14 riksintresseområden och cirka 55 utpekade kulturmiljöområden, som alla räknas som särskilt värdefulla."),
    ("Kan kommunen säga vilken avloppsanläggning vi ska välja till attefallshuset?",
     "Nej, men den kan ge en preliminär bedömning av skyddsnivån på fastigheten och berätta om en teknik har bedömts tidigare."),
  ],
  "sources": [_PBL, _PBF, _BOV, _SCB, _VD_PFO, _VD_KM, _RUFS, _VD_PBL, _MB, _VD_AVL, _SKV],
  "cta": ("Funderar du på ett attefallshus på Värmdö?", "Boka ett gratis platsbesök, så går vi igenom plan, strand och avlopp innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet trähus med svart plåttak på en bergig skärgårdstomt bakom ett större fritidshus",
     "small new grey-green painted wooden guest house with a black standing seam metal roof set on granite rock among pine trees behind a larger Swedish summer house, archipelago water visible between the trees, Värmdö Stockholm archipelago, clear summer morning"),
    ("Plintgrund i betong på berghäll med tallar inför ett litet hus",
     "close-up of a building site in a dense pine forest: four grey concrete pier foundations drilled into a smooth granite outcrop, a stack of fresh timber beams beside them, moss and blueberry shrubs, no water, no finished building, soft overcast daylight, Sweden"),
  ],
},

}
