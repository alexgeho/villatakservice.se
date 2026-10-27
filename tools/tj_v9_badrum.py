# -*- coding: utf-8 -*-
"""Tjänster v9 (2026-10-25) – ortsidor badrumsrenovering på Ekerö och i Norrtälje, Sigtuna, Upplands Väsby,
Hässelby och Enskede. Schema: se tools/tj_check.py.
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25: Ekerö kommun (Anmälan vatten
och avlopp, Kommunalt dricksvatten, Kommunalt avlopp, Eget avlopp, Eget dricksvatten), Norrtälje kommun (Enskilt
avlopp, Enskilt vatten), Norrtälje Vatten och Avfall (Förändring på fastighet, Hälsorisker med stillastående
vatten, Modern teknik för vattenbesparing), SCB (Fritidshus – var finns de?, 2026; BO0104 2024), Sigtuna kommun
(Vatten och avlopp, Installation eller ändring av ventilation, Bostadsanpassningsbidrag), Norrvatten (Frågor och
svar), Upplands Väsby kommun (Ledningsnät och anslutning, Kommunalt avlopp, Kommunalt dricksvatten, Kunskapsunderlag
för kulturmiljö), Stockholms stad (Områdesfakta 2025 Hässelby villastad och Gamla Enskede; Flytta kök eller badrum),
Stockholm Vatten och Avfall (Förebygg översvämningar, Backventiler, Servisledningar och ansvar), Stadsmuseet (Gamla
Enskede, byggnadsinventering 1974–1977), Arbetsmiljöverket (tillstånd för rivning av asbest), GVK (Förstärka
träbjälklag, Tätskikt mot fönster, Tillskjutande markfukt, Dörröppning), riksdagen.se (bostadsrättslagen 7 kap. 7 §)
och Skatteverket (rotavdrag, bidrag utesluter rot).
Strukna (ej verifierade): miljösanktionsavgiftens belopp i Norrtälje (prisuppgift – utelämnad), antal enskilda
avlopp på Ekerö (saknas på kommunens sida), om typhusen i Gamla Enskede saknade badrum från början (inventeringen
anger bara rumsprogram per typ), andel bostadsrätter bland radhusen i Upplands Väsby, vattenhårdhet för brunnar,
frysrisk/tömning av vatten i fritidshus (ingen kommunal källa), källare i Hässelby villastads hus (ingen källa).
Inga priser, garantier utöver lag, omdömen, egna uppdrag i orterna eller certifikat. Korslänkar via V4_MODULES."""

L = '<a class="text-link" href="{0}">{1}</a>'
X = '<a class="text-link" href="{0}" rel="noopener">{1}</a>'

# ------------------------------------------------------------------ gemensamma källor
S_ROT = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
S_ROTJOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
S_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
         "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
S_SCB = ("SCB – Antal lägenheter efter region och hustyp (BO0104), 2024",
         "https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BO__BO0104__BO0104D/BO0104T04/")
NORRV = "https://www.norrvatten.se/dricksvatten/fragor-och-svar/"
S_NORRV = ("Norrvatten – Frågor och svar om dricksvattnet", NORRV)
STHLM_FLYTT = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/flytta-kok-eller-badrum/"
S_STHLM_FLYTT = ("Stockholms stad – Flytta kök eller badrum", STHLM_FLYTT)
GVK = "https://www.gvk.se/branschregler/"

# Ekerö
EK = "https://www.ekero.se/bygga-bo-miljo/vatten-och-avlopp/"
EK_ANM = EK + "anmalan-vatten-och-avlopp"
EK_DV = EK + "kommunalt-dricksvatten"
EK_AVL = EK + "kommunalt-avlopp"
EK_EGET = EK + "eget-avlopp"
EK_BRUNN = EK + "eget-dricksvatten"
# Norrtälje
NT = "https://www.norrtalje.se/info/bygga-bo-miljo/vatten-och-avlopp/"
NT_AVL = NT + "enskilda-avlopp/"
NT_VAT = NT + "enskilt-vatten/"
NV = "https://www.nvaa.se/vatten-och-avlopp/"
NV_FOR = NV + "att-ansluta-till-kommunalt-vatten-och-avlopp/forandring-pa-fastighet-med-kommunalt-vatten-och-avlopp"
NV_STILL = NV + "dricksvatten/halsorisker-med-stillastaende-vatten"
NV_TEK = NV + "dricksvatten/hallbar-vattenanvandning/modern-teknik-for-vattenbesparing"
SCB_FRI = "https://www.scb.se/hitta-statistik/artiklar/2026/fritidshus-vart-finns-de/"
# Sigtuna
SIG = "https://www.sigtuna.se/bygga-bo-och-miljo/"
SIG_VA = SIG + "bygglov/vad-ska-du-bygga/andra-befintlig-byggnad/vatten-och-avlopp.html"
SIG_VENT = SIG + "bygglov/vad-ska-du-bygga/andra-befintlig-byggnad/installation-eller-andring-av-ventilation.html"
SIG_BAB = SIG + "mitt-boende/bostadsanpassningsbidrag.html"
# Upplands Väsby
UV = "https://www.upplandsvasby.se/bygga-bo-och-miljo/vatten-och-avlopp/"
UV_LED = UV + "ledningsnat-anslutning-till-fastighet"
UV_AVL = UV + "avlopp/kommunalt-avlopp"
UV_DV = UV + "dricksvatten/kommunalt-dricksvatten"
UV_KUL = ("https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/"
          "Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf")
# Stockholm Vatten och Avfall
SVOA_FOR = "https://www.svoa.se/villa-och-radhus/vatten-och-avlopp/hantera-oversvamning/nar-det-regnar-mycket/"
SVOA_BACK = "https://www.svoa.se/artiklar-listsida/oversvamning---hantera-och-forebygg/backventiler/"
SVOA_SERV = "https://www.svoa.se/villa-och-radhus/vatten-och-avlopp/bygga-om/servisledningar-och-ansvar/"
OF = "https://start.stockholm.se/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
OF_HV = OF + "vasterort/hasselby-vallingby/hasselby-villastad.pdf"
OF_GE = OF + "soderort/enskede/gamla-enskede.pdf"
AV_ASB = "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/"
SSM_ENS = "https://stockholmskallan.stockholm.se/postfiles/KUL/SSM_Gamla_Enskede__byggnadsinventering_1974_1977_00.pdf"

BRL_TXT = ("Enligt " + X.format(S_BRL[1], "bostadsrättslagen") + " 7 kap. 7 § får du inte utan styrelsens tillstånd "
           "göra ingrepp i bärande konstruktion, installera eller ändra ledningar för avlopp, värme, gas eller vatten "
           "eller ändra ventilationen. Styrelsen får säga nej bara om åtgärden är till påtaglig skada eller olägenhet "
           "för föreningen, och den som är missnöjd kan begära att hyresnämnden prövar frågan.")

PAGES_TJ = {

# =============================== BADRUM EKERÖ ===============================
"badrumsrenovering-ekero.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Ekerö", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Ekerö – anmälan, mjukt vatten och avlopp",
  "description": "Badrumsrenovering på Ekerö: när ett nytt badrum ska anmälas, mjukt Mälarvatten och "
                 "varmvattenberedaren, eget avlopp och brunn. Gratis platsbesök.",
  "h1": "Badrumsrenovering i Ekerö",
  "lead": "Ekerö kommun nämner just ett nytt badrum som exempel på en ändring av vatten och avlopp som ska anmälas. "
          "Därför börjar en badrumsrenovering på Mälaröarna med att reda ut vad som faktiskt ändras: läget på "
          "golvbrunnen, nya ledningar eller ett avlopp som får ta emot mer vatten. Geal Entreprenad AB river, bygger "
          "tätskikt och ytskikt och samordnar VVS och el, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Anmälan, mjukt vatten och eget avlopp.",
  "sections": [
    {"id": "anmalan", "anchor": "Anmälan på Ekerö",
     "h2": "Ett nytt badrum är en anmälan på Ekerö",
     "paras": [
       "Enligt SCB fanns det 9 131 bostäder i småhus i Ekerö kommun 2024. Kommunens " + X.format(EK_ANM, "sida om anmälan för vatten och avlopp") + " säger att du ska göra en "
       "anmälan vid en större ändring av avloppet eller en helt ny installation. Som exempel nämns ett nytt badrum, "
       "en komplementbostad och en ny golvbrunn i garaget.",
       "Ordningen är fast. Ansluts fastigheten för första gången går en anmälan först till Roslagsvatten, som har "
       "hand om det kommunala nätet. Sedan skickas anmälan till bygglovsenheten tillsammans med en kontrollplan och "
       "en VA-situationsplan. Arbetet får inte börja förrän kommunen har gett startbesked, och när det är klart "
       "lämnar du in den slutliga situationsplanen och den ifyllda kontrollplanen. Installationen får användas "
       "först när slutbeskedet har kommit.",
       "För oss betyder det att badrummet ritas klart innan något rivs. Var golvbrunnen hamnar, hur ledningarna går "
       "och om toaletten flyttas avgör vad som ska stå i handlingarna, och kontrollplanen fylls i under arbetets gång "
       "i stället för i efterhand.",
     ],
     "aside": {"title": "I rätt ordning", "items": [
       "Roslagsvatten vid ny anslutning",
       "Anmälan med kontrollplan",
       "Startbesked före rivning",
       "Slutbesked före användning"]}},
    {"id": "mjukt-vatten",
     "h2": "Mjukt Mälarvatten och varmvattenberedaren",
     "paras": [
       "Det kommunala vattnet på Ekerö kommer från Mälaren och renas i Norsborgs vattenverk. Bor du på Lovön kommer "
       "det från Lovöverket, och Vifärna har ett eget vattenverk. Enligt " + X.format(EK_DV, "kommunens sida om dricksvattnet")
       + " är vattnet mjukt, 4,4 dH, med pH 8,2 på Ekerösidan och 8,1 i området kring Stenhamra.",
       "Kommunen påpekar att mjukt vatten löser upp betong och cement och att risken för korrosion på metall ökar. "
       "Varmvattenberedare rostar sönder fortare, och vattenledningar kan skadas. När badrummet ändå är öppet är det "
       "därför ett bra tillfälle att se över beredarens ålder och skick och var den står, så att den kan bytas utan "
       "att det nya kaklet behöver röras.",
       "Vid ett strömavbrott är skillnaden mellan orterna stor. I Stenhamra och Ekerö tätort håller vattentorn uppe "
       "trycket, medan trycket i Vifärna, Kungsberga, Munsö kyrkby, Munsö Söderby, Stenby och Hovgården skapas med "
       "pumpar. Där kan du bli utan vatten när strömmen går. En avstängningsventil som är lätt att nå gör det enklare "
       "att hantera både avbrott och läckor.",
     ],
     "aside": None},
    {"id": "eget-avlopp",
     "h2": "Eget avlopp: tillstånd, anmälan och tillsyn",
     "paras": [
       "Kommunens avloppsnät renas i sex reningsverk som tillsammans kan ta emot avloppsvatten från 26 500 personer, "
       "och i dag är omkring 17 000 anslutna. Den som inte kan ansluta behöver enligt " + X.format(EK_EGET, "sidan om eget avlopp")
       + " tillstånd för att anlägga ett enskilt avlopp, och för att ändra en befintlig anläggning krävs oftast en "
       "anmälan. Kommunen råder dig att kontakta miljöenheten för rådgivning innan du ansöker.",
       "Miljöenheten inspekterar dessutom enskilda anläggningar områdesvis, i dag sådana som är äldre än tio år. Får "
       "huset ett andra badrum eller en dusch där det tidigare bara fanns ett enkelt våtrum är det klokt att ta reda "
       "på om anläggningen är dimensionerad för det, innan rummet byggs.",
       "Har du egen brunn ansvarar du själv för att vattnet räcker och håller god kvalitet. På " + X.format(EK_BRUNN, "sidan om egen brunn")
       + " hänvisar kommunen till Livsmedelsverkets råd att kontrollera vattnet minst vart tredje år, och provsvaret "
       "bör skickas i kopia till miljöenheten. Ett aktuellt prov är ett bra underlag när blandare och beredare väljs.",
     ],
     "aside": {"title": "Fråga innan bygget", "items": [
       "Klarar avloppet fler duschar?",
       "Krävs anmälan för ändringen?",
       "Hur gammalt är brunnsprovet?",
       "Var sitter avstängningen?"]}},
    {"id": "huset",
     "h2": "Badrummet i resten av huset",
     "paras": [
       "Ett badrum på Ekerö kan sitta i en villa från 1970-talet eller i ett sommarhus som har blivit helårsbostad. "
       "Golven, väggarna och ventilationen ser olika ut, och det avgör hur rummet byggs upp. Golvet i ett våtrum ska "
       "luta mot golvbrunnen så att vattnet inte leds ut i hallen, och väggarna byggs med skivor som tål ett tätskikt.",
       "Ska golven i resten av huset bytas samtidigt finns mer under " + L.format("golvlaggare-ekero.html", "golvläggare på Ekerö")
       + ", och om taket och ventilationsgenomföringarna under " + L.format("taklaggare-ekero.html", "takläggare på Ekerö")
       + ". Mer om hur vi bygger badrum generellt står på sidan om " + L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går badrumsrenoveringen till på Ekerö",
  "steps": [
    ("Platsbesök", "Vi ser rummet, golvbrunnen och ledningarna och frågar om huset har kommunalt eller eget avlopp."),
    ("Handlingar", "Ändras VA-installationen tar vi fram ritningar till anmälan och ett förslag till kontrollplan."),
    ("Kostnadsförslag", "Rivning, tätskikt, VVS, el och ytskikt står som separata poster i ett skriftligt förslag."),
    ("Rivning och underlag", "Efter startbesked rivs rummet ner till stommen och golvet byggs upp med fall mot brunnen."),
    ("Tätskikt och installationer", "Tätskiktet läggs, och behöriga installatörer drar rör och el."),
    ("Slutbesked", "Kontrollplanen fylls i, kaklet sätts och du får underlaget till slutbeskedet."),
  ],
  "rot_h2": "ROT-avdrag för badrummet på Ekerö",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag. Kakel- och klinkersättning och att dra in och reparera vatten- och avloppsledningar "
    "räknas som rotarbete i ett småhus som du äger, och det gäller även fritidshus.",
    "Material ger inget avdrag. Geal drar avdraget direkt på fakturan, så du betalar bara din del av arbetskostnaden.",
  ],
  "price_h2": "Vad styr kostnaden på Ekerö?",
  "price": [
    "Mest avgör om VA-installationen ändras, om golvbrunnen flyttas, hur underlaget ser ut när det gamla har rivits "
    "och vilka ytskikt du väljer. Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag innan något beställs.",
  ],
  "faq": [
    ("Måste vi göra en anmälan till Ekerö kommun för att bygga ett nytt badrum?",
     "Ja, kommunen nämner ett nytt badrum som exempel på en ändring som ska anmälas. Arbetet får börja först efter "
     "startbesked, och badrummet får användas när slutbeskedet har kommit."),
    ("Varför rostar varmvattenberedare snabbare på Ekerö?",
     "Kommunen skriver att vattnet är mjukt, 4,4 dH, och att mjukt vatten ökar risken för korrosion på metall. "
     "Det gör att beredare kan rosta sönder fortare."),
    ("Kan vi bli utan vatten i badrummet på Munsö vid strömavbrott?",
     "Ja, enligt kommunen skapas trycket i bland annat Munsö kyrkby och Munsö Söderby med pumpar, och då kan "
     "vattnet försvinna när strömmen går. I Stenhamra och Ekerö tätort finns vattentorn."),
    ("Behöver vi kontakta miljöenheten innan vi bygger ett andra badrum på en fastighet med eget avlopp?",
     "Det är klokt. En ändring av anläggningen kräver oftast en anmälan, och kommunen erbjuder rådgivning "
     "innan du ansöker."),
    ("Vilka handlingar ska lämnas in när badrummet på Ekerö är klart?",
     "Den slutliga VA-situationsplanen och den ifyllda kontrollplanen. När kommunen har granskat dem kommer slutbeskedet."),
  ],
  "sources": [
    ("Ekerö kommun – Anmälan vatten och avlopp", EK_ANM),
    ("Ekerö kommun – Kommunalt dricksvatten", EK_DV),
    ("Ekerö kommun – Kommunalt avlopp", EK_AVL),
    ("Ekerö kommun – Eget avlopp", EK_EGET),
    ("Ekerö kommun – Eget dricksvatten, om du har egen brunn", EK_BRUNN),
    S_SCB, S_ROTJOB, S_ROT,
  ],
  "cta": ("Ska badrummet på Ekerö byggas om?", "Boka ett gratis platsbesök, så går vi igenom rummet och vad som behöver anmälas."),
  "img": [
    ("Nyrenoverat ljust badrum med dusch i en villa på Ekerö",
     "newly renovated bright bathroom in a Swedish 1970s single-storey villa, one wall-hung white toilet, light grey matt "
     "floor tiles laid continuously into a walk-in shower area without any shower tray, one small square stainless floor "
     "drain inside the shower area, single fixed clear glass shower screen, white wall tiles, white washbasin cabinet, "
     "small window with a view of birch and pine trees, clean and empty"),
    ("Duschhörna med glasvägg och handfat på kommod",
     "white cylindrical domestic hot water heater standing on a tiled floor in a clean small Swedish utility room, "
     "a few neat vertical copper pipes along the wall with one red and one blue shut-off valve handle, small round floor "
     "drain, plain white walls, simple and tidy, nothing else in the room, no people"),
  ],
  "related": [],
},

# =============================== BADRUM NORRTÄLJE ===============================
"badrumsrenovering-norrtalje.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Norrtälje", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Norrtälje – fritidshus, avlopp och brunn",
  "description": "Badrumsrenovering i Norrtälje: tillstånd för WC och BDT-avlopp, salt i kustnära brunnar "
                 "och stillastående vatten i sommarhuset. Gratis platsbesök.",
  "h1": "Badrumsrenovering i Norrtälje",
  "lead": "I Norrtälje kommun får många hus sitt första riktiga badrum först när sommarhuset ska användas året runt. "
          "Då gäller kommunens egna regler för avlopp, som är strängare än på många andra håll. Geal Entreprenad AB "
          "river, bygger tätskikt och ytskikt och samordnar VVS och el, och vi går igenom avlopp och vatten innan "
          "badrummet ritas. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  "card": "Fritidshus, WC-tillstånd och brunn.",
  "sections": [
    {"id": "fritidshusen", "anchor": "Fritidshusen",
     "h2": "Landets mest fritidshustäta kommun",
     "paras": [
       "SCB räknade 2025 till 27 352 fritidshus i Norrtälje, fler än i någon annan kommun i landet. Värmdö kom tvåa "
       "med 14 709. Det säger något om vilka badrum som byggs här: ofta i ett hus som från början hade ett enkelt "
       "våtrum, en dusch i uthuset eller ingen toalett alls.",
       "När ett sådant hus får en dusch, en vattentoalett och kanske en tvättmaskin ändras både mängden vatten och "
       "vad det innehåller. Därför är avloppet den första frågan, före kakel och porslin. I tätorterna med kommunalt "
       "VA ligger frågan i stället hos Norrtälje Vatten och Avfall, som vill veta om fastighetens användning ändras.",
       "Rotavdrag gäller även för ett fritidshus som du äger. Mer om att bygga om sommarhuset finns under "
       + L.format("snickare-norrtalje.html", "snickare i Norrtälje") + ".",
     ],
     "aside": None},
    {"id": "tillstand",
     "h2": "Tillstånd för vattentoalett – och för BDT-vatten",
     "paras": [
       "På " + X.format(NT_AVL, "kommunens sida om enskilt avlopp") + " står att Norrtälje har egna regler som kan "
       "avvika från andra kommuners. Tillstånd krävs för att installera ett avlopp för vattentoalett, för att "
       "installera ett avlopp för bad-, disk- och tvättvatten, för att koppla en vattentoalett till ett avlopp som "
       "tidigare bara tog emot BDT-vatten och för att flytta en befintlig anläggning. Åtgärden får inte påbörjas "
       "innan tillståndet finns.",
       "Anmälan räcker för att koppla fler byggnader till en befintlig anläggning, för att dra om ledningarna, för "
       "att byta en toalett så att spolvattenmängden ökar och för att ändra reningstekniken. Anmälan ska då lämnas "
       "sex veckor innan arbetet ska göras.",
       "Är du osäker rekommenderar kommunen att du gör en ansökan. Den övergår till en anmälan om det räcker, och "
       "behövs ingenting avslutas ärendet utan avgift. Den som installerar ett tillståndspliktigt avlopp utan tillstånd "
       "kan få betala miljösanktionsavgift. För ett nytt badrum betyder det att tidplanen börjar hos kommunen.",
     ],
     "aside": {"title": "Kräver tillstånd", "items": [
       "Avlopp för vattentoalett",
       "Avlopp för BDT-vatten",
       "WC till ett BDT-avlopp",
       "Flytt av anläggningen"]}},
    {"id": "brunnen",
     "h2": "Brunnen nära havet",
     "paras": [
       "Kommunen ligger till största delen under den marina gränsen och har alltså en gång varit täckt av salt eller "
       "bräckt vatten. Enligt " + X.format(NT_VAT, "sidan om enskilt vatten") + " kan saltvatten tränga in i en brunn "
       "som är borrad för djupt eller där uttaget är för stort, och på sommaren och i tätbebyggda områden kan det bli "
       "extra kritiskt. Första åtgärden kan vara att höja pumpen och minska förbrukningen.",
       "Ett badrum som används av fler personer året runt tar mer vatten. Norrtälje Vatten och Avfall skriver att en "
       "snålspolande kran kan halvera vattenuttaget jämfört med en traditionell, med bibehållet tryck. Snålspolande "
       "toalett, blandare och duschmunstycke är därför ett naturligt val när brunnen är begränsad.",
       "Livsmedelsverket rekommenderar att vattnet från en privat brunn analyseras minst vart tredje år, och kommunen "
       "hänvisar till Vattencentrum, som ger kostnadsfri och opartisk rådgivning om enskilt vatten och avlopp.",
     ],
     "aside": None},
    {"id": "stillastaende",
     "h2": "Vatten som står still i ett hus som står tomt",
     "paras": [
       "Ett sommarhus står ofta oanvänt i veckor. Norrtälje Vatten och Avfall varnar för att mikroorganismer, bland "
       "annat legionellabakterier, förökar sig där vattnet står stilla och är varmare än 20 grader. Smittan sprids "
       "genom vattendimma, till exempel i en dusch.",
       "Rådet är att spola kranar och tappställen regelbundet, särskilt de som sällan används. Varmvattnet ska vara "
       "minst 60 grader i beredaren och minst 50 grader vid tappstället efter en minuts spolning, och kallvattnet ska "
       "vara under 20 grader. I badrummet planerar vi därför korta rördragningar till duschen, så att lite vatten blir "
       "stående i ledningarna.",
       "Är huset anslutet till kommunalt VA ska du meddela Norrtälje Vatten och Avfall om användningen av byggnaden "
       "ändras, eftersom det kan ge en tilläggsavgift. Fönster och tak i Roslagen behandlas under "
       + L.format("fonsterbyte-norrtalje.html", "fönsterbyte i Norrtälje") + " och " + L.format("takbyte-norrtalje.html", "takbyte i Norrtälje") + ".",
     ],
     "aside": {"title": "Före första vintern", "items": [
       "Korta rör till duschen",
       "Beredare på minst 60 grader",
       "Snålspolande blandare",
       "Ventiler som är lätta att nå"]}},
  ],
  "steps_h2": "Så planeras badrummet i Norrtälje",
  "steps": [
    ("Avlopp och vatten", "Vi tar reda på om huset har kommunalt VA, ett befintligt tillstånd eller inget avlopp alls."),
    ("Kommunen", "Krävs tillstånd eller anmälan väntar bygget tills beslutet finns, och vi anpassar tidplanen."),
    ("Ritning och förslag", "Du får ett skriftligt kostnadsförslag där rivning, tätskikt, VVS, el och ytskikt står var för sig."),
    ("Rivning och uppbyggnad", "Golvet byggs upp med fall mot golvbrunnen, och väggarna får skivor för tätskikt."),
    ("Installationer", "Behöriga installatörer drar rör och el och monterar snålspolande porslin och blandare."),
    ("Genomgång", "Vi visar ventiler och beredare och lämnar dokumentationen från tätskikt och VVS."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Norrtälje",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden och högst 50 000 kr per person och år, med ett gemensamt tak på "
    "75 000 kr för rot och rut. Det gäller både permanentbostad och fritidshus som du äger.",
    "Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Norrtälje?",
  "price": [
    "Om avloppet kräver tillstånd eller ombyggnad, om badrummet byggs i ett tidigare torrt rum, hur huset är grundlagt "
    "och vilka ytskikt du väljer. Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi tillstånd för att sätta in en vattentoalett i sommarhuset i Norrtälje?",
     "Ja. I Norrtälje kommun krävs tillstånd för ett avlopp för vattentoalett och för att koppla en vattentoalett "
     "till ett avlopp som tidigare bara tog emot BDT-vatten."),
    ("Hur lång tid före bygget ska en avloppsanmälan lämnas in i Norrtälje?",
     "Kommunen kräver att anmälan lämnas sex veckor innan åtgärden ska utföras, till exempel när ledningarna dras om."),
    ("Kan ett nytt badrum ge salt vatten i brunnen vid kusten?",
     "Ett större vattenuttag ökar risken för saltvatteninträngning enligt kommunen. Snålspolande blandare och "
     "toalett minskar uttaget, och vid salt vatten kan pumpen behöva höjas."),
    ("Vilken temperatur ska varmvattnet ha i ett fritidshus som står tomt ibland?",
     "Minst 60 grader i beredaren och minst 50 grader vid tappstället efter en minuts spolning, enligt Norrtälje "
     "Vatten och Avfall. Spola gärna alla kranar när huset öppnas."),
    ("Ska vi meddela NVAA när fritidshuset blir permanentbostad?",
     "Ja, om huset har kommunalt VA. Ändrad användning av en byggnad kan ge en tilläggsavgift och ska meddelas "
     "via en servisanmälan."),
  ],
  "sources": [
    ("SCB – Fritidshus, var finns de? (2026)", SCB_FRI),
    ("Norrtälje kommun – Enskilt avlopp", NT_AVL),
    ("Norrtälje kommun – Enskilt vatten", NT_VAT),
    ("Norrtälje Vatten och Avfall – Hälsorisker med stillastående vatten", NV_STILL),
    ("Norrtälje Vatten och Avfall – Modern teknik för vattenbesparing", NV_TEK),
    ("Norrtälje Vatten och Avfall – Förändring på fastighet med kommunalt vatten och avlopp", NV_FOR),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska sommarhuset i Norrtälje få ett riktigt badrum?", "Boka ett gratis platsbesök, så går vi igenom avlopp, vatten och rummet."),
  "img": [
    ("Nybyggt badrum med kaklad dusch och panelat tak i ett fritidshus i Roslagen",
     "newly built small bathroom in a Swedish wooden archipelago summer house converted for year-round living, the "
     "shower corner fully tiled with white wall tiles from floor to ceiling, white painted wooden panel ceiling, grey "
     "floor tiles sloping to a small floor drain in the shower, clear glass shower screen, white toilet, small white "
     "window with view of pines and granite rocks, empty, no people"),
    ("Foderrör från en borrad brunn på en tomt med tallar och berg vid kusten",
     "small Swedish drilled water well: a short black steel well casing pipe with a cap sticking up about 30 cm from "
     "moss and granite bedrock on a natural plot with low pine trees, a red wooden cottage in the background and a "
     "glimpse of the Baltic sea, overcast, no people"),
  ],
  "related": [],
},

# =============================== BADRUM SIGTUNA ===============================
"badrumsrenovering-sigtuna.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Sigtuna", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Sigtuna – anmälan, ventilation och dusch",
  "description": "Badrumsrenovering i Sigtuna och Märsta: när kommunen kräver anmälan, ny fläkt och "
                 "bostadsanpassning från badkar till dusch. Gratis platsbesök.",
  "h1": "Badrumsrenovering i Sigtuna",
  "lead": "Sigtuna kommun hade 7 387 bostäder i småhus 2024 enligt SCB, från villorna i Sigtuna stad till radhusen i Märsta. "
          "Badrummen där är ofta lika gamla som husen, och en renovering väcker samma frågor: vad kommunen behöver "
          "veta, hur fläkten ska fungera och om badkaret ska bli en dusch. Geal Entreprenad AB river, bygger tätskikt "
          "och samordnar VVS och el, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Anmälan, fläkt och dusch i stället för badkar.",
  "sections": [
    {"id": "anmalan-sigtuna", "anchor": "När kommunen ska veta",
     "h2": "När badrummet blir en anmälan i Sigtuna",
     "paras": [
       "På " + X.format(SIG_VA, "kommunens sida om vatten och avlopp") + " står att en anmälan behövs när du väsentligt ändrar "
       "eller gör en ny installation för vatten eller avlopp. Kommunen räknar en ändring som väsentlig när "
       "installationen påverkar husets bärande konstruktion eller när ett stambyte påverkar VA-stammarna.",
       "Till anmälan bifogas en situationsplan på kommunens tomtkarta, en redovisning av vatten- och "
       "avloppsanordningarna, plan- och sektionsritning och konstruktionsritningar om bärande delar berörs. Ett förslag "
       "till kontrollplan ska alltid lämnas, och vid omfattande arbeten behövs även en kontrollansvarig. Tomtkartan går "
       "att ladda ner gratis utan inloggning.",
       "Saknar fastigheten kommunalt avlopp är det strängare: att anlägga ett nytt eller ändra ett befintligt enskilt "
       "avlopp är tillståndspliktigt enligt miljöbalken. Vill du ansluta huset till det kommunala nätet görs anmälan "
       "till Sigtuna Vatten och renhållning.",
     ],
     "aside": {"title": "Väsentlig ändring", "items": [
       "Påverkar bärande konstruktion",
       "Stambyte som rör VA-stammarna",
       "Ny installation för VA",
       "Nytt eller ändrat enskilt avlopp"]}},
    {"id": "flakten",
     "h2": "Fläkten och kanalen",
     "paras": [
       "Ett badrum behöver frånluft, och fläkten byts ofta samtidigt med resten av rummet. Enligt "
       + X.format(SIG_VENT, "kommunens sida om ventilation") + " ska både ett nytt ventilationssystem och en ändring av "
       "ett befintligt anmälas, och arbetet får börja först när startbeskedet har kommit. Innebär åtgärden en stor "
       "förändring av husets utsida, till exempel ett aggregat eller kanaler på fasaden, krävs bygglov i stället.",
       "Till en anmälan om ventilation vill kommunen ha situationsplan, planritning, fasadritningar, förslag till "
       "kontrollplan och, om bärande delar berörs, konstruktionsritning och ett utlåtande från konstruktören. Vid "
       "större ändringar bedömer kommunen om det behövs en kontrollansvarig.",
       "Att byta en trasig badrumsfläkt mot en likvärdig är något annat än att bygga om systemet. Vi tar reda på hur "
       "ventilationen i huset fungerar i dag, var frånluften går ut och om den nya lösningen kan behöva anmälas, innan "
       "något beställs. Ett badrum som får dusch i stället för badkar ger mer fukt i luften, och då ska fläkten orka "
       "ta hand om den.",
     ],
     "aside": None},
    {"id": "badkar-dusch",
     "h2": "Från badkar till dusch med bostadsanpassningsbidrag",
     "paras": [
       "Den som har en långvarig funktionsnedsättning kan söka " + X.format(SIG_BAB, "bostadsanpassningsbidrag") + " hos "
       "kommunen. Bland exemplen nämner Sigtuna att ta bort badkar och ordna duschplats, förbättra belysningen och "
       "sätta in stödhandtag i badrummet. Tillfälliga problem, som ett benbrott, ger inte rätt till bidrag, och det "
       "gäller inte heller normalt underhåll eller anpassning av ett fritidshus.",
       "Anpassningar utanför bostaden kan också ge bidrag, till exempel ramper och ledstänger vid entrén. "
       "Skatteverket skriver att du inte kan få rotavdrag för arbete som du får bidrag för. Ska badrummet både anpassas "
       "och renoveras behöver de två delarna därför hållas isär i kostnadsförslaget, så att det framgår vad bidraget "
       "gäller och vad du betalar själv.",
       "En duschplats utan tröskel går att bygga. Enligt " + X.format(GVK + "golv/dorroppning/", "GVK:s regler för dörröppning")
       + " finns inget krav på tröskel i ett våtrum, men då ska fuktkänsligt material vid dörren skyddas och golvbrunnens "
       "fläns ligga minst 20 millimeter under tätskiktets översta punkt vid dörröppningen.",
     ],
     "aside": {"title": "Bidraget kan gälla", "items": [
       "Duschplats i stället för badkar",
       "Stödhandtag",
       "Bättre belysning",
       "Borttagna trösklar"]}},
    {"id": "vattnet-sigtuna",
     "h2": "Vatten från Görvälnverket",
     "paras": [
       "Har huset kommunalt vatten kommer det från Norrvatten, som renar vatten från Mälaren i Görvälnverket. Enligt "
       + X.format(NORRV, "Norrvattens frågor och svar") + " är vattnet medelhårt på gränsen till mjukt, 6–7 dH, med "
       "pH 8,2–8,4. Vita fläckar på blankt metall är ofta ofarliga kalkutfällningar som kan tas bort med en mild syra.",
       "Norrvatten ger inga råd om vilken varmvattenberedare du ska köpa men föreslår att du talar om vattnets pH för "
       "butiken. Samma uppgift är bra att ha när blandare och duschsystem väljs. Har huset egen brunn kan vattnet "
       "vara helt annorlunda, och då är ett vattenprov ett bättre underlag än Norrvattens siffror.",
       "Måla om i resten av huset efter renoveringen? Se " + L.format("malare-sigtuna.html", "målare i Sigtuna") + ". "
       "Tak och plåt beskrivs under " + L.format("takrenovering-sigtuna.html", "takrenovering i Sigtuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Sigtuna",
  "steps": [
    ("Platsbesök", "Vi ser rummet, ventilationen och golvbrunnen och frågar hur badrummet ska användas."),
    ("Anmälan eller inte", "Påverkas stammar, bärande delar eller ventilation tar vi fram underlag för anmälan."),
    ("Kostnadsförslag", "Skriftligt förslag med separata poster, och anpassningar för sig om bidrag söks."),
    ("Rivning", "Rummet rivs ner till stommen och golvbrunnen bedöms eller byts."),
    ("Uppbyggnad", "Fall mot brunnen, våtrumsskivor och tätskikt; installatörerna drar rör och el."),
    ("Ytskikt och genomgång", "Kakel, klinker och porslin monteras, och du får dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Sigtuna",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag. Arbete som du får bidrag för ger inget avdrag.",
    "Material ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Sigtuna?",
  "price": [
    "Om stammar, ventilation eller bärande delar berörs, om badkaret byts mot dusch, golvbrunnens skick och vilka "
    "ytskikt du väljer. Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("När räknar Sigtuna kommun en ändring av vatten och avlopp som väsentlig?",
     "När installationen påverkar byggnadens bärande konstruktion eller när ett stambyte påverkar VA-stammarna. "
     "Då ska ändringen anmälas och startbesked inväntas."),
    ("Behöver en ny badrumsfläkt anmälas i Sigtuna?",
     "Ett nytt ventilationssystem eller en ändring av det befintliga ska anmälas enligt kommunen. Sätts aggregat eller "
     "kanaler på fasaden kan bygglov krävas."),
    ("Kan vi få bidrag för att byta badkaret mot en dusch i Märsta?",
     "Bostadsanpassningsbidrag kan sökas om behovet beror på en långvarig funktionsnedsättning. Sigtuna nämner just "
     "att ta bort badkar och ordna duschplats som exempel."),
    ("Går det att kombinera bostadsanpassningsbidrag och rotavdrag för samma badrum?",
     "Inte för samma arbete. Skatteverket ger inget rotavdrag för arbete som du får bidrag för, så delarna hålls isär "
     "i kostnadsförslaget."),
    ("Hur hårt är kranvattnet i Sigtuna?",
     "Norrvatten anger 6–7 tyska hårdhetsgrader, medelhårt på gränsen till mjukt, och pH 8,2–8,4."),
  ],
  "sources": [
    ("Sigtuna kommun – Vatten och avlopp (ändra befintlig byggnad)", SIG_VA),
    ("Sigtuna kommun – Installation eller ändring av ventilation", SIG_VENT),
    ("Sigtuna kommun – Bostadsanpassningsbidrag", SIG_BAB),
    S_NORRV,
    ("GVK – Dörröppning i våtrum", GVK + "golv/dorroppning/"),
    S_SCB, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i Sigtuna eller Märsta göras om?", "Boka ett gratis platsbesök, så går vi igenom rummet och vad kommunen behöver veta."),
  "img": [
    ("Tillgängligt badrum med duschplats utan tröskel i ett radhus i Märsta",
     "accessible renovated bathroom in a Swedish 1970s terraced house seen from the doorway, completely flat continuous "
     "floor with the same light beige tiles in the whole room and in the shower area, no step, no curb and no shower tray, "
     "one linear floor drain along the back wall of the shower, fold-down white shower seat and a grab bar on the tiled "
     "wall, one toilet with grab bar on the side wall, soft daylight, empty, no people"),
    ("Frånluftsdon i taket ovanför en dusch i ett badrum",
     "close-up of a round white ceiling exhaust air valve in a freshly renovated Swedish bathroom ceiling above a "
     "shower area with white tiles, simple white ceiling, clean and minimal, no people, no text"),
  ],
  "related": [],
},

# =============================== BADRUM UPPLANDS VÄSBY ===============================
"badrumsrenovering-upplands-vasby.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Upplands Väsby", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Upplands Väsby – radhus och suterräng",
  "description": "Badrumsrenovering i Upplands Väsby: radhus i grupper och samfälld VA, badrum i suterrängplan "
                 "och bostadsrätt. Gratis platsbesök och ROT på fakturan.",
  "h1": "Badrumsrenovering i Upplands Väsby",
  "lead": "I Upplands Väsby sitter många badrum i radhus och kedjehus som byggdes i grupper på 1960- och 70-talen, "
          "ibland i ett nedre plan i suterräng. Badrummet är ditt, men ledningarna och reglerna kan vara gemensamma "
          "med grannarna. Geal Entreprenad AB river, bygger tätskikt och ytskikt och samordnar VVS och el, med gratis "
          "platsbesök och skriftligt kostnadsförslag.",
  "card": "Radhus, suterräng och samfälld VA.",
  "sections": [
    {"id": "grupperna", "anchor": "Radhusen i Väsby",
     "h2": "Radhus i grupper – ledningar i grupp",
     "paras": [
       "Kommunens " + X.format(UV_KUL, "kunskapsunderlag för kulturmiljö") + " beskriver hur de östra kommundelarna har "
       "vuxit fram med en stor andel småhus och radhus från 1960- och 70-talen. Husen är rationellt byggda i en eller "
       "två våningar, ibland två våningar i suterräng, och grupperna är olika sinsemellan men enhetliga inom varje grupp.",
       "Att husen är byggda samtidigt syns också under golvet. På " + X.format(UV_LED, "sidan om ledningsnät och anslutning")
       + " skriver kommunen att flera fastigheter bara får dela en förbindelsepunkt för spill- eller dagvatten om de har "
       "bildat en gemensamhetsanläggning, och det är då samfällighetsföreningen som är kommunens motpart. Ligger en "
       "sådan anläggning under radhuslängan är det klokt att fråga föreningen innan en ny golvbrunn eller toalett "
       "kopplas på.",
       "Kommunen påpekar också att dagvatten och dräneringsvatten inte får kopplas till spillvattenservisen, och att "
       "eget vatten inte får kopplas ihop med kommunens. Vid skador på en privat VA-anläggning kan VA-jouren hjälpa "
       "till med att stänga av vattnet, och vilka ledningar som finns utanför tomtgränsen går att beställa via Ledningskollen.",
     ],
     "aside": {"title": "Fråga grannarna om", "items": [
       "Gemensam förbindelsepunkt?",
       "Samfällighetens regler",
       "Var stammen går i längan",
       "Avstängning för hela längan"]}},
    {"id": "suterrang",
     "h2": "Badrummet i suterrängplanet",
     "paras": [
       "Ett badrum i ett nedre plan som ligger delvis under mark har en annan fuktsituation än ett rum på entréplan. "
       "GVK:s " + X.format(GVK + "tatskikt/tillskjutande-markfukt-och-tatskikt/", "regel om tillskjutande markfukt")
       + " säger att man vid fukt underifrån ska utreda i vilka delar av utrymmet tätskiktet behövs, och att "
       "tätskiktsprodukten ska vara avsedd för underlag med tillskjutande fukt.",
       "Fukten kan kontrolleras genom att man säkerställer att det finns ett kapillärbrytande material eller "
       "värmeisolering under golvet, vilket kan framgå av konstruktionsritningen, eller genom en fuktsäkerhetsprojektering "
       "som görs av en fuktsakkunnig. Det är beställarens ansvar att den görs. Vi börjar därför med att leta fram "
       "husets ritningar och se hur grunden är uppbyggd.",
       "Det finns särskilt anpassade vätskebaserade tätskikt för rum med fukt underifrån, och GVK råder att alltid "
       "stämma av med leverantören innan tätskiktet läggs. I ett radhus där flera grannar har samma planlösning kan "
       "samma fråga dessutom gälla hela längan.",
     ],
     "aside": None},
    {"id": "bostadsratt-vasby",
     "h2": "När radhuset är en bostadsrätt",
     "paras": [
       "Bor du i ett radhus som tillhör en bostadsrättsförening är det "
       "föreningen som äger huset, och då gäller bostadsrättslagen. " + BRL_TXT,
       "En badrumsrenovering berör i regel flera av punkterna. Sök därför styrelsens tillstånd innan "
       "hantverkare bokas, och fråga samtidigt vilka krav föreningen har på dokumentation av tätskikt och VVS.",

       "Rotavdrag för en bostadsrätt gäller bara arbete inne i lägenheten. Köket i samma typ av radhus beskrivs under "
       + L.format("koksrenovering-upplands-vasby.html", "köksrenovering i Upplands Väsby") + ".",
     ],
     "aside": None},
    {"id": "avloppet-vasby",
     "h2": "Vad som inte får hällas i avloppet",
     "paras": [
       "Spillvattnet från Väsby renas i Käppalaförbundets reningsverk på Lidingö. På " + X.format(UV_AVL, "kommunens sida om avlopp")
       + " står att målarfärg, lacknafta, lösningsmedel och andra kemikalier aldrig får hällas i avloppet, eftersom de "
       "skadar mikroorganismerna i reningsverket. Under en renovering gäller det till exempel rester av färg och "
       "primer, som i stället ska tas om hand separat och inte spolas ner i golvbrunnen.",
       "Dricksvattnet kommer från Mälaren och produceras av Norrvatten i Görvälnverket. Kommunen påminner om att "
       "varmvatten inte ska användas till mat och dryck, eftersom varmvattenledningar inomhus ofta är gjorda av koppar "
       "som löses ut. Fasaderna och färgerna i radhusgrupperna beskrivs under "
       + L.format("malare-upplands-vasby.html", "målare i Upplands Väsby") + ".",
     ],
     "aside": {"title": "Inte i golvbrunnen", "items": [
       "Rester av färg och primer",
       "Lacknafta och lösningsmedel",
       "Andra kemikalier",
       "Pool- och spavatten"]}},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Upplands Väsby",
  "steps": [
    ("Platsbesök", "Vi ser rummet och frågar om huset är äganderätt, bostadsrätt eller del av en samfällighet."),
    ("Ritningar och grund", "Vi letar fram husets ritningar och ser om badrummet ligger mot mark."),
    ("Kostnadsförslag", "Rivning, tätskikt, VVS, el och ytskikt står var för sig i ett skriftligt förslag."),
    ("Rivning", "Rummet rivs, och rivningsavfall och kemikalierester sorteras och körs bort."),
    ("Uppbyggnad", "Fall mot golvbrunnen, tätskikt anpassat för underlaget och installationer av behöriga installatörer."),
    ("Ytskikt och dokumentation", "Kakel och porslin monteras, och du får underlaget som föreningen kan begära."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Upplands Väsby",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans "
    "med rutavdrag. I ett radhus med äganderätt gäller det hela badrummet, i en bostadsrätt bara arbete inne i lägenheten.",
    "Material ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Upplands Väsby?",
  "price": [
    "Om badrummet ligger mot mark, om golvbrunn och ledningar behöver bytas, hur stort rummet är och vilka ytskikt du "
    "väljer. Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver samfälligheten tillfrågas när vi bygger om badrummet i vårt radhus i Väsby?",
     "Det beror på hur ledningarna är dragna. Delar längan förbindelsepunkt genom en gemensamhetsanläggning är "
     "samfällighetsföreningen kommunens motpart, och då är det klokt att fråga föreningen före en ny anslutning."),
    ("Vilket tätskikt passar i ett badrum i suterrängplan?",
     "GVK säger att tätskiktet ska vara avsett för underlag med tillskjutande fukt, och att det ska utredas vilka delar "
     "av rummet som behöver tätskikt."),
    ("Får rester av primer och fogmassa spolas ner i golvbrunnen under renoveringen?",
     "Nej. Upplands Väsby kommun skriver att färg, lacknafta och andra kemikalier aldrig ska hällas i avloppet. "
     "Resterna tas om hand separat."),
    ("Kan dräneringen kopplas till spillvattnet när badrummet i källarplanet görs om?",
     "Nej, enligt kommunen får dagvatten och dräneringsvatten inte kopplas till spillvattenservisen."),
    ("Varför ska man inte dricka varmvatten från kranen i radhuset?",
     "Kommunen påpekar att varmvattenledningar ofta är av koppar som löses ut i varmvattnet. Använd kallvatten till mat och dryck."),
  ],
  "sources": [
    ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö (pdf)", UV_KUL),
    ("Upplands Väsby kommun – Ledningsnät, anslutning till fastighet", UV_LED),
    ("Upplands Väsby kommun – Kommunalt avlopp", UV_AVL),
    ("Upplands Väsby kommun – Kommunalt dricksvatten", UV_DV),
    ("GVK – Tillskjutande markfukt och tätskikt", GVK + "tatskikt/tillskjutande-markfukt-och-tatskikt/"),
    S_BRL, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i radhuset i Väsby göras om?", "Boka ett gratis platsbesök, så går vi igenom rummet, ledningarna och vad föreningen behöver veta."),
  "img": [
    ("Renoverat badrum med fönster i marknivå i ett radhus i Upplands Väsby",
     "renovated basement-level bathroom in a Swedish 1970s house built into a slope, low flat white ceiling with no roof "
     "window, the only window is a small wide basement window placed high in the back wall at ground level with green "
     "grass visible outside, dark grey floor tiles, walk-in shower with fixed glass screen and small floor drain, white "
     "wall tiles, oak vanity, clean and empty, no people"),
    ("Rad av radhus från 1970-talet med tegel och träpanel längs en gångväg",
     "row of single-storey Swedish 1970s terraced houses built as one uniform group, red brick facades with dark "
     "brown horizontal wooden panel below a low almost flat roof with a thick fascia, no chimneys, small front gardens "
     "and a car-free paved footpath, birch trees, autumn, no people, no cars"),
  ],
  "related": [],
},

# =============================== BADRUM HÄSSELBY ===============================
"badrumsrenovering-hasselby.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Hässelby", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Hässelby – källare och bostadsrätt",
  "description": "Badrumsrenovering i Hässelby: källarbadrum och översvämning, backventil, asbest i "
                 "äldre våtrum och styrelsens tillstånd i bostadsrätt. Gratis platsbesök.",
  "h1": "Badrumsrenovering i Hässelby",
  "lead": "Hässelby villastad är till största delen en stadsdel av egna hus, men här finns också radhus och "
          "lägenheter i bostadsrätt. Vilka regler som gäller för badrummet beror på hur du äger bostaden och var i "
          "huset rummet ligger. Geal Entreprenad AB river, bygger tätskikt och ytskikt och samordnar VVS och el, med "
          "gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Källarbadrum, backventil och bostadsrätt.",
  "sections": [
    {"id": "agandet", "anchor": "Villa eller bostadsrätt",
     "h2": "Villa, radhus eller bostadsrätt i Hässelby",
     "paras": [
       "Enligt " + X.format(OF_HV, "stadens områdesfakta") + " fanns det 7 029 bostäder i Hässelby villastad 2025, och "
       "5 009 av dem låg i småhus. De allra flesta småhusen, 4 757, var äganderätter, men 204 småhus var bostadsrätter, "
       "och totalt fanns 794 bostadsrätter i stadsdelen.",
       "I en villa eller ett radhus med äganderätt beslutar du själv om badrummet, men du ansvarar också för ledningarna "
       "på tomten. Stockholm Vatten och Avfall skriver att fastighetsägaren bekostar läckor, stopp och reparationer "
       "inom den egna fastigheten och att ansvaret går över till dem vid förbindelsepunkten.",
       "Bor du i bostadsrätt, i ett radhus eller en lägenhet, är det föreningen som äger huset. " + BRL_TXT,
     ],
     "aside": {"title": "Vem bestämmer?", "items": [
       "Äganderätt: du själv",
       "Bostadsrätt: styrelsen först",
       "Ledningar på tomten: ägaren",
       "Efter förbindelsepunkten: SVOA"]}},
    {"id": "kallaren",
     "h2": "Badrum i källaren och kraftiga regn",
     "paras": [
       "Ett badrum i källaren ligger lägst i huset och är det rum som först får vatten vid översvämning. Stockholm "
       "Vatten och Avfall påpekar att det kan hända även i torrt väder, och då handlar det ofta om en vattenläcka "
       "eller ett avloppsstopp.",
       "I " + X.format(SVOA_FOR, "checklistan för att förebygga översvämningar") + " råder SVOA att golvet i källaren "
       "ska vara av ett material som tål vatten och att du ska ha tunga, tättslutande föremål som sandsäckar till hands "
       "att lägga över golvbrunnar och toalettstolar. Takvatten från stuprör bör inte ledas till avloppsledningen, "
       "dräneringen och fuktskyddet på väggar under mark ska vara täta och marken ska luta från huset.",
       "Samma råd gäller när ett källarbadrum byggs om. Klinker, tätskikt och en golvbrunn med rätt fall tål vatten "
       "bättre än en matta på ett gammalt betonggolv, men de hjälper inte om vattnet kommer upp genom brunnen. "
       "Därför ser vi också över stuprören och marken runt huset, se " + L.format("taklaggare-hasselby.html", "takläggare i Hässelby") + ".",
     ],
     "aside": None},
    {"id": "backventil",
     "h2": "Backventil – bara med eftertanke",
     "paras": [
       "En backventil sitter på servisledningen och ska hindra avloppsvatten från gatan att tränga in genom golvbrunnar "
       "och andra avloppsenheter. På " + X.format(SVOA_BACK, "SVOA:s sida om backventiler") + " står att du som kund "
       "får installera en på eget initiativ, men att den kräver ingrepp i ledningssystemet och inte passar i alla "
       "anläggningar. Du ansvarar själv för den.",
       "Innan ventilen sätts in måste du veta att det inte finns egna dagvattenanslutningar på samma ledning. När "
       "ventilen är stängd kommer det vattnet annars inte ut, och inte heller avloppsvattnet från ditt eget hus. En "
       "backventil behöver dessutom regelbunden tillsyn enligt tillverkarens anvisning, och en dåligt skött ventil kan "
       "i värsta fall ge större skada.",
     ],
     "aside": {"title": "Före en backventil", "items": [
       "Inga dagvattenanslutningar på ledningen",
       "Plats för tillsyn och skötsel",
       "Undvik avlopp under stängning",
       "Skötselanvisning sparad"]}},
    {"id": "aldre-vatrum",
     "h2": "Äldre våtrum, asbest och ny stam",
     "paras": [
       "Många villor i Hässelby villastad ersattes på 1960- och 70-talen av grupper av enhetliga småhus. Ett badrum som "
       "inte har rivits sedan dess kan innehålla material från byggtiden. Arbetsmiljöverket skriver att asbest i "
       "bostadshus kan finnas i väggar, golv och tak, och att det krävs tillstånd för att riva eller sanera material som "
       "innehåller asbest. Ansökan ska göras åtta veckor innan arbetet börjar.",
       "Är vi osäkra på vad mattor, fix eller skivor innehåller tar vi prov innan något rivs, och sanering görs av ett "
       "företag med tillstånd. Stockholms stad påminner om att flytt av ett badrum inte kräver bygglov, men att en anmälan "
       "behövs om ventilationen ändras väsentligt eller om en ny VA-stam dras i ett nytt schakt.",
       "Fasaderna och färgerna i stadsdelen beskrivs under " + L.format("malare-hasselby.html", "målare i Hässelby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Hässelby",
  "steps": [
    ("Platsbesök", "Vi ser rummet, golvbrunnen och ledningarna och frågar hur bostaden ägs."),
    ("Material och ledningar", "Misstänkta material provas före rivning, och vi ser över stuprör och mark vid källarbadrum."),
    ("Kostnadsförslag", "Rivning, tätskikt, VVS, el och ytskikt står som separata poster i ett skriftligt förslag."),
    ("Rivning och uppbyggnad", "Rummet rivs till stommen, och golvet får fall mot en ny golvbrunn."),
    ("Tätskikt och installationer", "Tätskikt enligt branschreglerna, och behöriga installatörer drar rör och el."),
    ("Ytskikt och genomgång", "Kakel och porslin monteras, och du får dokumentationen för huset eller föreningen."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Hässelby",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
    "tillsammans med rutavdrag. I en bostadsrätt gäller det bara arbete inne i lägenheten.",
    "Material ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Hässelby?",
  "price": [
    "Om badrummet ligger i källaren, om golvbrunn och ledningar byts, om äldre material behöver saneras och vilka "
    "ytskikt du väljer. Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi sätta in en backventil själva i villan i Hässelby?",
     "Ja, Stockholm Vatten och Avfall skriver att du får installera en på eget initiativ, men du ansvarar för den. "
     "Först måste det vara säkert att inga egna dagvattenledningar är kopplade till samma ledning."),
    ("Vem betalar om avloppet i vår tomt i Hässelby är stopp?",
     "Fastighetsägaren ansvarar för ledningarna inom den egna fastigheten. Stockholm Vatten och Avfall tar över vid "
     "förbindelsepunkten."),
    ("Vilket golv passar i ett källarbadrum som kan få in vatten?",
     "SVOA råder att golvet i källaren ska vara av ett material som tål vatten. Klinker på tätskikt med fall mot "
     "golvbrunnen är ett vanligt val."),
    ("Kan det finnas asbest i ett badrum från 1960-talet?",
     "Arbetsmiljöverket skriver att asbest i bostadshus kan finnas i väggar, golv och tak. Är materialet okänt tas "
     "prov innan rivning."),
    ("Behöver vi styrelsens tillstånd för att renovera badrummet i ett radhus i bostadsrätt i Hässelby?",
     "Ja, om du ändrar ledningar för vatten och avlopp, ventilationen eller bärande delar, enligt bostadsrättslagen "
     "7 kap. 7 §."),
  ],
  "sources": [
    ("Stockholms stad – Områdesfakta Hässelby villastad (2025)", OF_HV),
    ("Stockholm Vatten och Avfall – Förebygg översvämningar", SVOA_FOR),
    ("Stockholm Vatten och Avfall – Backventiler", SVOA_BACK),
    ("Stockholm Vatten och Avfall – Servisledningar och ansvar", SVOA_SERV),
    ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest", AV_ASB),
    ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
     "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf"),
    S_STHLM_FLYTT, S_BRL, S_ROT,
  ],
  "cta": ("Ska badrummet i Hässelby byggas om?", "Boka ett gratis platsbesök, så går vi igenom rummet, ledningarna och vad som gäller för din bostad."),
  "img": [
    ("Renoverat källarbadrum med klinkergolv i en villa i Hässelby",
     "renovated basement bathroom in a Swedish 1940s villa, grey stone-look floor tiles continuing into a walk-in "
     "shower without a tray, one small square stainless floor drain inside the shower, single fixed glass screen, white "
     "wall tiles, one small basement window high on the wall with daylight, one wall-hung toilet, white towel radiator, "
     "clean and empty, no people"),
    ("Duschhörna med glasdörrar och rutigt golv",
     "close-up of a square stainless steel floor drain grate set in newly laid grey ceramic floor tiles with neat grout "
     "lines sloping towards it, a few water droplets, in a Swedish bathroom, no people, no text"),
  ],
  "related": [],
},

# =============================== BADRUM ENSKEDE ===============================
"badrumsrenovering-enskede.html": {
  "kind": "district", "service": "badrumsrenovering", "ort": "Enskede", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Enskede – typhus i trä och bostadsrätter",
  "description": "Badrumsrenovering i Enskede: våtrum i typhus med träbjälklag, fönster i badrummet och "
                 "bostadsrätterna i Gamla Enskede. Gratis platsbesök och ROT.",
  "h1": "Badrumsrenovering i Enskede",
  "lead": "I Gamla Enskede står trähus som byggdes efter typritningar från 1908 och framåt, och runt dem finns "
          "flerbostadshus där de flesta lägenheterna är bostadsrätter. Ett badrum i ett plankhus på träbjälklag "
          "och ett badrum i en lägenhet kräver olika förberedelser. Geal Entreprenad AB river, bygger tätskikt och "
          "ytskikt och samordnar VVS och el, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Typhus i trä, träbjälklag och bostadsrätt.",
  "sections": [
    {"id": "typhusen", "anchor": "Typhusen i Enskede",
     "h2": "Typhus med plankstomme och källare",
     "paras": [
       "Stadsmuseets " + X.format(SSM_ENS, "byggnadsinventering av Gamla Enskede") + " berättar att utbyggnaden "
       "började sommaren 1908. I tomträttskontraktet åtog sig staden att anlägga och underhålla vägar och ledningar för "
       "vatten, avlopp och gas, och husen fick bara innehålla ett kök.",
       "Inventeringen beskriver husen typ för typ. Många är fristående enfamiljshus med källare, en våning och inredd "
       "vind, byggda i trä med plankstomme. Flera av de tidiga typerna anges som 3 rum och kök, medan till exempel en "
       "typ från 1911 och en typ som Bostadsföreningen Sten Sture uppförde i ett tiotal exemplar 1922 anges med bad.",
       "Ett badrum i ett sådant hus kan alltså ha byggts till eller om i efterhand, kanske i flera omgångar. Innan "
       "något nytt planeras vill vi se vad som döljer sig under golvet och bakom väggarna, och hur avloppet går ner "
       "genom källaren till ledningen i gatan.",
     ],
     "aside": {"title": "Vanligt i typhusen", "items": [
       "Plankstomme av trä",
       "Källare under huset",
       "Inredd vind",
       "Rumsprogram per hustyp"]}},
    {"id": "trabjalklag",
     "h2": "Kakel på ett träbjälklag",
     "paras": [
       "Ett trägolv rör sig med årstiderna. GVK:s " + X.format(GVK + "golv/forstarka-trabjalklag/", "regel om att förstärka träbjälklag")
       + " säger att golv som ska få kakel, klinker eller natursten måste förstärkas för att motverka svikt och "
       "fuktrörelser. Sviktar golvet för mycket lossnar plattorna.",
       "Förstärkningen kan göras med en formstabil skiva som limmas och skruvas fast eller med lättfyllnadsmassa mellan "
       "golvbjälkarna. Reglerna utgår från ett visst avstånd mellan bjälkarna och en största spännvidd, och i ett hus "
       "från 1910-talet behöver bjälkarnas dimension och skick därför kontrolleras först.",
       "Ska badrummet få golvvärme rekommenderar GVK att en konstruktionsritning ligger till grund för utförandet, så "
       "att bjälklagets stabilitet inte äventyras. Golven i resten av huset beskrivs under sidan om "
       + L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
    {"id": "fonstret",
     "h2": "Fönstret i badrummet",
     "paras": [
       "Har badrummet ett fönster gäller särskilda regler, och GVK kallar fönster i badrum för en riskkonstruktion. "
       "Enligt " + X.format(GVK + "tatskikt/tatskikt-mot-fonster/", "GVK:s regel om tätskikt mot fönster") + " ska ett "
       "fönster inte placeras i plats för bad eller dusch. Sitter det i våtzonen ska väggens tätskikt anslutas mot "
       "karmen enligt tätskiktsleverantörens anvisning, och fönstersmygarna ska luta in mot rummet.",
       "GVK rekommenderar också att fönstrets underkant sitter minst 150 millimeter över golvet, och att den som "
       "duschar nära ett fönster som kan få vattenstänk använder ett duschdraperi eller liknande. Går duschen inte att "
       "flytta bort från fönstret föreslår vi en lösning med glasvägg. Fönstret i sig, och hur det tål "
       "fukt, tas upp under " + L.format("fasadrenovering-enskede.html", "fasadrenovering i Enskede") + ".",
     ],
     "aside": {"title": "Fönster i våtzonen", "items": [
       "Tätskikt anslutet mot karmen",
       "Smygar som lutar inåt",
       "Underkant minst 150 mm upp",
       "Inte i själva duschplatsen"]}},
    {"id": "bostadsratterna",
     "h2": "Bostadsrätterna i Gamla Enskede",
     "paras": [
       "Gamla Enskede är inte bara villor. Enligt " + X.format(OF_GE, "stadens områdesfakta") + " fanns det 5 117 "
       "bostäder i stadsdelen 2025. 923 av dem låg i småhus, men 3 708 låg i flerbostadshus, och 2 303 av dessa var "
       "bostadsrätter.",
       BRL_TXT + " Stockholms stad påpekar att du kan behöva föreningens tillstånd och råder dig att kontakta styrelsen "
       "innan du börjar planera att flytta kök eller badrum.",
       "Kommunen behöver bara kopplas in om flytten påverkar bärande konstruktion eller brandskydd, om ventilationen "
       "ändras väsentligt eller om en ny VA-stam dras i ett nytt schakt. Ett större kök i samma hus beskrivs under "
       + L.format("koksrenovering-enskede.html", "köksrenovering i Enskede") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går badrumsrenoveringen till i Enskede",
  "steps": [
    ("Platsbesök", "Vi ser rummet, golvet och fönstret och frågar om huset är villa eller bostadsrätt."),
    ("Bjälklag och stam", "I villan kontrolleras bjälkarna, i lägenheten var stammen och frånluften går."),
    ("Kostnadsförslag", "Förstärkning, rivning, tätskikt, VVS, el och ytskikt står som separata poster."),
    ("Rivning och förstärkning", "Rummet rivs, och träbjälklaget förstärks innan tätskiktet läggs."),
    ("Tätskikt och installationer", "Tätskikt mot golv, väggar och fönster; behöriga installatörer drar rör och el."),
    ("Ytskikt och genomgång", "Kakel och porslin monteras, och du får dokumentationen."),
  ],
  "rot_h2": "ROT-avdrag för badrummet i Enskede",
  "rot": [
    "Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans "
    "med rutavdrag. I en bostadsrätt gäller det arbete inne i lägenheten, i en villa hela badrummet.",
    "Material ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Enskede?",
  "price": [
    "I villan mest bjälklagets skick och hur mycket som måste förstärkas, i lägenheten stammens läge och föreningens "
    "krav. Ytskikten spelar in i båda. Platsbesöket är gratis, och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Går det att ha klinker på golvet i ett typhus med träbjälklag i Gamla Enskede?",
     "Ja, men GVK kräver att träbjälklaget förstärks mot svikt och fuktrörelser, med en formstabil skiva eller "
     "lättfyllnadsmassa mellan bjälkarna."),
    ("Får badrummets fönster sitta i duschen?",
     "GVK säger att fönster inte ska placeras i plats för bad eller dusch. Sitter det i våtzonen ska tätskiktet "
     "anslutas mot karmen och smygarna luta in mot rummet."),
    ("Hade typhusen i Gamla Enskede badrum från början?",
     "Stadsmuseets inventering anger bad för vissa typer, till exempel en från 1911, medan flera tidiga typer beskrivs "
     "som 3 rum och kök. Badrummet i ditt hus kan alltså ha tillkommit senare."),
    ("Behöver vi kontakta styrelsen innan vi flyttar badrummet i en bostadsrätt i Gamla Enskede?",
     "Ja. Stockholms stad råder dig att kontakta bostadsrättsföreningens styrelse innan du börjar planera en flytt "
     "av kök eller badrum."),
    ("Kan vi få golvvärme i badrummet i ett trähus från 1910-talet?",
     "Ofta ja. GVK rekommenderar att en konstruktionsritning ligger till grund för golvvärme i ett träbjälklag."),
  ],
  "sources": [
    ("Stadsmuseet via Stockholmskällan – Gamla Enskede, byggnadsinventering 1974–1977 (pdf)", SSM_ENS),
    ("Stockholms stad – Områdesfakta Gamla Enskede (2025)", OF_GE),
    ("GVK – Förstärka träbjälklag", GVK + "golv/forstarka-trabjalklag/"),
    ("GVK – Tätskikt mot fönster", GVK + "tatskikt/tatskikt-mot-fonster/"),
    S_STHLM_FLYTT, S_BRL, S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska badrummet i Enskede göras om?", "Boka ett gratis platsbesök, så går vi igenom golvet, fönstret och vad som gäller för din bostad."),
  "img": [
    ("Renoverat badrum med fönster i ett äldre trähus i Gamla Enskede",
     "renovated small bathroom on the upper floor of a Swedish 1910s wooden house, sloping attic ceiling, small white "
     "wooden window with deep sill tiled and sloping inwards, white wall tiles, hexagon grey floor tiles, freestanding "
     "white bathtub away from the window, warm daylight, clean and empty, no people"),
    ("Dusch med två duschset och klinker på golv och väggar",
     "top-down view of a bathroom floor under renovation in an old Swedish wooden house: new light brown chipboard "
     "subfloor panels with neat rows of screws and visible panel joints, a new round grey plastic floor drain fitting "
     "installed in the middle of the floor, bare wooden walls at the edges, construction dust, daylight, no people, no tools"),
  ],
  "related": [],
},

}
