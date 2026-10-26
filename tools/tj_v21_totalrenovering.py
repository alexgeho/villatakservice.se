# -*- coding: utf-8 -*-
"""Totalrenovering – ortsidor v21: Nacka, Sollentuna, Solna, Södermalm, Täby, Vasastan (2026-10-26).
Tjänst under villarenovering.html (TJ_HUB["totalrenovering"]). Intent: renovera hela huset eller hela lägenheten
på en gång – skild från ortens byggforetag-<ort>.html (lov, nybyggnad, tomt) och från enskilda rum
(badrumsrenovering-/koksrenovering-<ort>.html), som länkas i stället. Skild från v18-sidorna (Bromma: arbetenas
ordning; Danderyd: varsam rivning och återbruk; Enskede: nyköpt hus och ROT; Huddinge: asbest och PCB; Kungsholmen:
bostadsrättslagen 7 kap. 7 och 9 §§; Lidingö: stommen behålls) och från byggtorg.se/totalrenovering-nacka/,
-sollentuna/ och -taby/ (SCB-tal, riksintressen, Storängen/Saltsjöbaden, anmälan vid större planändring och
ventilation, stambyte i schakt, kulturmiljöplanen och Norrvikens villastad, takstol, radhus i bostadsrättsförening,
Ella gård/Norskogen/Hägern/Näsbydal, grupphusråd, bärande väggar och äldre ritningar) – inga av de vinklarna används.
Lokal vinkel per sida (en huvudfråga per sida):
Nacka – byta värmesystem i samma omgång: bergvärme kräver anmälan till kommunen, SGU-avstånd för borrhål, västra och
centrala Sicklaön (tunnelbanan), Sandasjöns vattenskyddsområde, kommunens energi- och klimatrådgivare, Boverkets
nya bidrag (bara material) och ROT för arbetet, självdrag när skorstenen kallnar;
Sollentuna – radon: kommunen anger mätning var tionde år eller vid större renoveringar, radonkartan (bara
enbostadshus, högst tio år gamla mätningar), blåbetong 1929–1975, mätperiod och tidplan, SSM:s åtgärder, inget
radonbidrag längre;
Solna – elen när bostadsrätten görs om: Solna stads råd till lägenhetsinnehavare, innehavaransvaret i bostadsrätt,
äldre elanläggning får sitta kvar men det som byggs om följer nya krav, dokumentation och märkning, ROT för el;
Södermalm – samordna lägenheten med föreningens stambyte: Stockholms stads anmälningsregler, tillgängligheten får
inte försämras (badrumsgolv, dörrar), områdesfakta 2025, ROT-gränsen mellan stambyte och eget VVS-arbete;
Täby – bygga om för att kunna bo kvar: Täby kommuns bostadsanpassning, Boverkets handbok (eftersatt underhåll,
egen avvikelse från tillgänglighetskraven, omodernt ingen avslagsgrund), konsumenttjänstlagen;
Vasastan – husets värden inomhus: Stadsmuseets inventering av nordvästra Vasastaden (lägenhetsstorlekar, badrum och
tvättstuga i gemensamma lokaler), klassificeringens färger, förvanskning inomhus, eldstad/kakelugn och anmälan, ROT.

Fakta endast från källorna i respektive 'sources', öppnade med curl (-L, Mozilla-UA) och lästa 2026-10-26
(pdf:er med textlager via pdftotext):
  Skatteverket (Så fungerar rotavdraget: bara arbetskostnad, högst 30 procent på fakturan, material och resor ger
  inget avdrag, äga bostaden, 75 000 / 50 000 kr; Ger arbetet rätt till rotavdrag?: småhus – riva väggar och bygga
  om planlösningen, installera/byta värmepumpar men inte både ROT och grön teknik för samma arbete, markarbeten för
  värmeförsörjning, sanera asbest och radon i samband med byggarbete, inget avdrag för att mäta fukt, radon och
  asbest; bostadsrätt – innanför tak, väggar och golv och enligt stadgarna, installera och komplettera elcentraler,
  dra elledningar från proppskåpet ut i bostaden, byta och montera vägguttag, inbyggda spotlights, inget avdrag för
  att dra el till en elcentral utanför bostaden, dra vatten- och avloppsledningar som tjänar bostaden, byta
  golvbrunn, blandare, kakel och klinker, inget avdrag för stambyten, flytta eller byta avloppsrör eller flytta
  golvbrunn, mura och reparera öppen spis och kakelugn, inget avdrag för att sota eller kontrollera eldstäder),
  Nacka kommun (Installera värmepump, till exempel bergvärme: mark/vatten anmäls, luftvärmepump ingen anmälan,
  e-tjänst, typ av värmepump/borrhålsplacering/borrföretag/installatör, börja med installatören, energirådgivare för
  dimensionering, västra och centrala Sicklaön – rådfråga ansvariga för tunnelbaneutbyggnaden, individuell
  bedömning, mätrör i energibrunnen på vissa fastigheter, längre handläggning, Sandasjöns vattenskyddsområde –
  remiss till Nacka vatten och avfall AB, primär zon vanligen inte tillåten, ägaren ska känna till ledningarna och
  står för skador, Ledningskollen, borrvatten infiltreras på egen fastighet annars sedimentering i container,
  SGU-avstånd 10/20/20/30/5/10 m, situationsplan på kartutdrag ur webbkartan utan kostnad, grannyttrande om
  avstånden inte följs; Nackas energi- och klimatrådgivare: bidrag för energieffektivisering sedan 1 september
  2026, kontakta rådgivaren, opartisk och kostnadsfri),
  Boverket (Bidrag för energieffektivisering i småhus: fjärrvärme eller värdeår senare än 1989 omfattas inte, äga och
  stadigvarande bo, permanentbostad, värdeår kan justeras framåt vid större till- eller ombyggnationer, uppgift i
  fastighetstaxeringsbeslutet, ansökan inom sex månader från påbörjad åtgärd, projektering räknas inte, bara
  materialkostnader, arbetskostnad kan ge rotavdrag; Energiguiden – berg-, sjö- och jordvärmepump: kräver vattenburet
  system med golvvärme eller radiatorer, dimensionera för värme och varmvatten, mindre effektbehov ger mindre pump
  och grundare borrhål, täta fönster och dörrar, självdrag – kallare skorstensstock, minskad ventilation, lukt, fukt,
  sämre luft, fukt på vinden; Bostadsanpassningsbidraget – handboken: vad är bidraget, exempel – trösklar, dusch i
  stället för badkar, spisvakt, ramp, bredda dörröppningar, normalt ansökan före åtgärd, i efterhand svårare,
  ingen prövning av ekonomin; Bostadens skick – lag (2018:222) 8 § punkt 1–4, punkt 4 bara när sökanden själv låtit
  uppföra eller ändra, bidrag beviljas om någon annan avvikit; Eftersatt underhåll – bedömning utifrån användningen
  före anpassningen, badkarsexemplet, omodernt ingen avslagsgrund, äldre kök med lägre diskbänk),
  Sollentuna kommun (Radon: mark och berggrund, sprickor och otätheter i grunden, genomföringar för el, vatten och
  avlopp, blåbetong 1929–1975, ventilation kan minska halten, kommunalt vatten inte radonhaltigt, egen brunn, 200
  Bq/m³, halten varierar mellan närstående hus, mät var tionde år eller i samband med större renoveringar, ägaren
  ansvarar, minst två månader oktober–april, beställning oktober–februari, spårfilm, Swedac, radonkartan – bara
  enbostadshus, mätningar högst tio år gamla, kontaktcenter),
  Strålsäkerhetsmyndigheten (Radon i småhus: otätt mot marken räcker, mäta enda sättet, eldningssäsong 1 oktober–30
  april, minst två punkter och varje plan med boendeutrymmen, ackrediterat laboratorium, ny mätning efter tio år
  eller efter byggnadsåtgärder som kan påverka halten, kommunens miljökontor kan ha tidigare resultat; Åtgärder mot
  radon: ta reda på källan, radonkonsult, byggnadsmaterial – ökad luftväxling, ofta frånluft med fläkt, mark – täta,
  annars radonsug, radonbrunn eller smalrör, ny långtidsmätning efter åtgärd; Nya fönster: kan påverka
  luftomsättningen, mät igen vid all renovering; Radonbidrag: går inte längre att söka),
  Solna stad (För lägenhetsinnehavare: fastighetsägarens medgivande, krav på leverantören – bygglov, kontrollplan,
  dokumentation, begär slutbesked, flytta kök – föreningens godkännande och ibland VA-anmälan, riva vägg – bärande
  kräver anmälan; Ändra vatten och avlopp: invändiga ändringar som väsentligt påverkar VA kräver anmälan och
  startbesked, kontrollplan; Kulturmiljöer i Solna: listan med Stenstaden i Råsunda, Råsunda villastad,
  1950-talsbebyggelse i Råsunda, Skytteholm och Huvudsta, Hagalundshusen, Gamla Hagalund, karta över
  kulturhistoriskt klassade byggnader),
  Elsäkerhetsverket (Bygga och renovera: registrerat elinstallationsföretag, verksamhetstypen Bostäder, Kolla
  elföretaget, sovrum till badrum som exempel, inga regler om uppgradering av befintlig anläggning, huvudregeln om
  reglerna när anläggningen togs i bruk, ombyggnad och utvidgning följer nya krav, besiktning av hela anläggningen,
  risk för strömgenomgång och brand; Ansvaret för elanläggningen: innehavaren ansvarar, i bostadsrätt du,
  föreningen eller båda, grundprincip tillträde och rätt att ändra, ansvar att ta reda på om anläggningen behöver
  uppdateras vid renovering; Dokumentation och märkning: information om anläggningen, gruppförteckningen,
  kartläggning, dokumentation som "kvitto", uppdaterad märkning, kontroll innan den tas i bruk, skriv in i avtalet),
  Stockholms stad, bygglov.stockholm (Stambyte: oftast samma läge utan anmälan, anmälan och startbesked vid nya lägen
  eller väsentliga ingrepp i bärande, regler för våtrum och vatteninstallationer, tillgängligheten får inte försämras
  – höjda golv i wc/badrum, olämplig inredning, för smala dörröppningar, konstruktör; Installation eller ändring av
  VA: anmälan vid väsentlig ändring eller ny installation, exempel stam i nytt läge; Ombyggnad: informera gärna
  grannar eller styrelsen, slutbesked innan det används; Stadsmuseets kulturhistoriska klassificering: karta,
  uppdateras, ej inventerade byggnader, kontakta stadsmuseet med adress, fastighetsbeteckning, byggnadsår,
  ombyggnader och foton; Kulturhistorisk värdefull byggnad och område: varsamhet för alla ändringar, förvanskning
  oavsett lov eller anmälan, antikvarisk förundersökning och konsekvensbeskrivning, sakkunnig inom kulturvärden
  (KUL); Eldstad, braskamin och skorsten: anmälan och startbesked för eldstad, skorsten, rökkanal, spisinsats vid
  ändrade eldningsförhållanden, tyngre eldstad med förstärkning, ny anslutning med håltagning och murning, annat
  bränsleslag, rådgör tidigt med skorstensfejarmästaren, krav på utsläpp och verkningsgrad, CE-märkning,
  Miljöförvaltningen tillsyn och krav vid olägenhet),
  Stockholms stad – Områdesfakta Södermalms stadsdelsområde (pdf: 77 525 bostäder 2025, 43 680 bostadsrätter varav
  43 542 i flerbostadshus/övriga hus, 211 i småhus, 21 466 lägenheter om två rum och kök – flest),
  Stadsmuseet (Kulturhistorisk klassificering: blått, grönt, gult, grått och streckat, expertutlåtande utan juridisk
  verkan, prövning i bygglov, Bebyggelseregistret med motiveringar, Digitala Stadsmuseet; Nordvästra Vasastaden –
  byggnadsinventering 1989, pdf: avgränsning Norrtullsgatan, Norra Stationsgatan, Gävlegatan/S:t Eriksgatan,
  Odengatan, inventeringar 1974–78, många förändringar sedan dess interiört och exteriört, söder om Karlbergsvägen
  bebyggt på 1880- och 90-talen, arbetar- och lägre tjänstemannaklass, merparten små lägenheter, gathusen större,
  gårdshusen enklast, praktlägenheter mot Odengatan, Karlbergsvägen och S:t Eriksgatan, få hus med hiss, badrum och
  tvättstuga ofta i gemensamma lokaler på vinden eller gården),
  Riksdagen (Bostadsrättslag 1991:614, 7 kap. 7 § punkt 4 – installation eller ändring av eldstad eller rökkanal
  kräver styrelsens tillstånd),
  Täby kommun (Bostadsanpassning: bestående funktionsnedsättning, bo kvar, fasta funktioner – trösklar,
  stödhandtag, badrum, ramper, dörrautomatik, inte om hjälpmedel räcker, byte till hus med trappor, e-tjänst,
  intyg från arbetsterapeut/fysioterapeut/läkare, ibland fastighetsägarens medgivande, sökanden är beställare och
  konsumenttjänstlagen gäller, bidraget betalas ut efter slutförd åtgärd).
Strukna (ej verifierade eller medvetet utelämnade): bidragets belopp och procentsats (Boverket anger dem, men sajten
använder bara ROT-siffrorna), Skatteverkets schablon för värmepumpsentreprenad (procentsatser utelämnade),
Nackas krav på borrarens certifiering och Normbrunn-16 (onödigt för sidan; ordet certifiering undviks), Nackas
avgift i miljötaxan och handläggningstider, Stadsmuseets svarstid, Täbys handläggningstider, att Täbys fjärrvärme
bara går till flerbostadshus och lokaler (läst på kommunens energisida men inte använt – en vinkel per sida),
radonnivåer i Sollentuna i stort (radonkartan visar enskilda fastigheter – inga generaliseringar), att lägenheter i
Vasastan har kakelugnar (skrivs villkorligt), att badrum i Vasastans lägenheter generellt är senare tillägg
(inventeringen gäller nordvästra Vasastaden – skrivs så), bostadsrättslagens paragrafer (Kungsholmen-sidan),
Stjärnhusen i Bergshamra (ordet stjärn flaggas av kontrollen – inte nämnt), hur ROT och bostadsanpassningsbidrag
samverkar (ingen källa öppnad – inte nämnt), priser, avgifter, tidsåtgång.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert. Perks enbart sajtens befintliga: gratis
platsbesök, skriftligt kostnadsförslag, ROT direkt på fakturan, en kontakt/total entreprenad.
Kritikpass 2026-10-26: alla 31 käll-URL:er öppnade igen med curl (-4 -L, Mozilla-UA; Skatteverket svarade först
efter omförsök), nordvästra Vasastaden-pdf:en och områdesfakta-pdf:en med textlager. Varje faktamening kontrollerad
mot källtexten. Rättat: Nacka – Sicklaön "i vissa delar av" västra och centrala (kommunens lydelse, även FAQ),
grannar som motsätter sig – "kommunen avgör vem som har rätt"; Sollentuna – "alltid räcker" -> "är tillräcklig
för att kunna" (SSM), miljökontorets mätresultat "i vissa fall"; Solna – "bygger enligt bygglovet" (stadens
ord), slutbesked som stadens påminnelse; Södermalm – "nästan alltid" -> "i regel", "flerbostadshus och övriga
hus", två rum och kök gäller flerbostadshusen, IMD vid "nyinstallation eller väsentlig ändring" (stadens lydelse);
Täby – lagens punkt 3 med lagtextens ord ("avsaknad av eller avsevärda brister"); Vasastan – gul klass
"och/eller", Miljöförvaltningens krav gäller olägenhet för människors hälsa, föreningens tillstånd för eldstad
med bostadsrättslagen som källa (lagt till), badrummet som senare tillägg skrivet villkorligt ("kan vara").
tj_check: 0 FEL; enda WARN för v21-sidorna är "bild saknas" (bilderna genereras separat).
Kritikpass (strikt) 2026-10-26: alla källor öppnade igen, även de sex bygglov.stockholm-sidorna som byggs med
_SB-prefixet (stambyte, VA, ombyggnad, klassificering, kulturhistoriskt värdefull, eldstad – alla 200 med rätt titel);
pdf:er (områdesfakta Södermalm, nordvästra Vasastaden) med textlager. Ändrat: Sollentuna – "En radonmätning ska pågå"
-> "bör pågå" (SSM:s ord); alt-text "En liten radonmätare" -> "Två små radonmätare" (prompten visar två dosor).
Vasastan – "annars är bygglovsbefriade" -> "annars kan vara bygglovsbefriade" (stadens ord); blått/grönt-regeln
verifierad i listan "Du behöver söka bygglov om ... är markerat med blå eller grön färg i kartan" (behållen).
Kontrollerat utan ändring: Nacka (anmälan mark/vatten, luft ingen anmälan, installatör först, SGU 10/20/20/30/5 m,
grannyttrande, kommunen avgör, Sicklaön "i delar av", mätrör, Sandasjön/primär zon, ledningar/kostnader,
Ledningskollen, infiltration/container, bidrag sedan 1 sept 2026, rådgivaren opartisk och kostnadsfri; Boverket
fjärrvärme/1989/värdeår/sex månader/projektering/bara material/rotavdrag, vattenburet system, dimensionering,
effektbehov/borrhål, självdrag-skorsten-lukt-fukt-vind); Sollentuna (mätning var tionde år eller vid större
renoveringar, 200 Bq/m³, ägaransvar, variation mellan hus, karta bara enbostadshus/högst tio år, kontaktcenter,
blåbetong 1929–1975, kommunalt vatten, beställning okt–feb; SSM 1 okt–30 apr, två punkter/varje plan, ackrediterat
lab, tio år/byggnadsåtgärder, fönsterbyte, åtgärder, radonbidrag finns inte); Solna (medgivande, kök/vägg/bärande,
bygglov/kontrollplan/dokumentation/slutbesked, förteckningen); Elsäkerhetsverket (innehavare, bostadsrätt du/föreningen/
båda, grundprincip, registrerat för Bostäder, Kolla elföretaget, sovrum->badrum, huvudregeln, ombyggnad följer nya
krav, besiktning, gruppförteckning, kartläggning, kvitto, märkning, avtal); Södermalm (77 525/43 680/211/21 466 = 2 rok
i flerbostadshus, stambyte samma läge/nya lägen/bärande/konstruktör/våtrum, tillgänglighet, ändring/ombyggnad, IMD);
Täby (bostadsanpassning, intyg, beställare/konsumenttjänstlagen, utbetalning efter åtgärd, trapphiss, offerter;
Boverket exempel, före/efterhand, ekonomi, allergi/syn, bestående eller långvarig, 8 § punkt 1–4, omodernt,
diskbänk, användning före anpassning); Vasastan (inventeringens gränser, 1880–90-tal, arbetar-/lägre tjänstemannaklass,
gathus/gårdshus, praktlägenheter, hiss, badrum/tvättstuga, 1974–78; klassernas definitioner, expertutlåtande,
Bebyggelseregistret, tjugoårsgräns, eldstadslistan, CE, Miljöförvaltningen, BRL 7 kap. 7 § p. 4); ROT-meningarna
mot Skatteverket (bostadsrätt el/VVS/murning, stambyten, småhus värmepump/grön teknik, femårsregeln, stommen).
Inga priser, garantier, omdömen eller egna uppdrag. tj_check: 0 FEL, inga WARN för v21-totalrenovering.
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

# ------------------------------------------------------------------ gemensamma källor
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SKV_JOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/"

# Nacka
_NAC_VP = ("Nacka kommun – Installera värmepump, till exempel bergvärme",
           "https://www.nacka.se/boende-miljo/hem/installera-varmepump/")
_NAC_EKR = ("Nacka kommun – Nackas energi- och klimatrådgivare",
            "https://www.nacka.se/boende-miljo/klimat-och-miljo/for-dig-som-nackabo/energi-och-klimatradgivare/")
_BOV_BID = ("Boverket – Bidrag för energieffektivisering i småhus",
            "https://www.boverket.se/sv/bidrag--garantier/bidrag-for-energieffektivisering-i-smahus/")
_BOV_BERG = ("Boverket – Energiguiden: berg-, sjö- och jordvärmepumpar",
             "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/berg--sjo--och-jordvarme/")
# Sollentuna
_SO_RADON = ("Sollentuna kommun – Radon", "https://www.sollentuna.se/bygga-bo--miljo/Din-bostad-och-tomt/radon/")
_SSM_SMAHUS = ("Strålsäkerhetsmyndigheten – Radon i småhus",
               "https://www.stralsakerhetsmyndigheten.se/omraden/radon/radon-i-smahus/")
_SSM_ATG = ("Strålsäkerhetsmyndigheten – Åtgärder mot radon",
            "https://www.stralsakerhetsmyndigheten.se/omraden/radon/atgarder-mot-radon/")
_SSM_FONSTER = ("Strålsäkerhetsmyndigheten – Vi har bytt fönster, kan det påverka radonhalten?",
                "https://www.stralsakerhetsmyndigheten.se/omraden/radon/fragor-och-svar-om-radon/vi-har-bytt-fonster-i-vart-hus-kan-det-paverka-radonhalten-i-bostaden/")
_SSM_BIDRAG = ("Strålsäkerhetsmyndigheten – Jag har hört talas om radonbidrag, hur får jag det?",
               "https://www.stralsakerhetsmyndigheten.se/omraden/radon/fragor-och-svar-om-radon/jag-har-hort-talas-om-radonbidrag-hur-far-jag-det/")
# Solna
_SOL_LGH = ("Solna stad – Guide till lov och anmälan: för lägenhetsinnehavare",
            "https://www.solna.se/bygga-bo--miljo/bygga/guide-till-lov-och-anmalan/for-lagenhetsinnehavare")
_SOL_VA = ("Solna stad – Ändra vatten och avlopp", "https://www.solna.se/bygga-bo--miljo/bygga/anmalan/andra-vatten-och-avlopp")
_SOL_KM = ("Solna stad – Kulturmiljöer i Solna", "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna")
_ELS_RENO = ("Elsäkerhetsverket – Bygga och renovera",
             "https://www.elsakerhetsverket.se/privatpersoner/din-elanlaggning/bygga-och-renovera")
_ELS_ANSV = ("Elsäkerhetsverket – Ansvaret för elanläggningen",
             "https://www.elsakerhetsverket.se/privatpersoner/din-elanlaggning/ansvaret-for-elanlaggningen")
_ELS_DOK = ("Elsäkerhetsverket – Dokumentation och märkning",
            "https://www.elsakerhetsverket.se/privatpersoner/anlita-ett-elinstallationsforetag/dokumentation-och-markning")
# Södermalm
_SB_STAM = ("Stockholms stad – Stambyte", _SB + "stambyte/")
_SB_VA = ("Stockholms stad – Installation eller ändring av vatten och avlopp (VA)",
          _SB + "installation-eller-andring-av-vatten-och-avlopp-va/")
_SB_OMB = ("Stockholms stad – Ombyggnad", _SB + "ombyggnad/")
_OF_SOD = ("Stockholms stad – Områdesfakta: Södermalms stadsdelsområde (pdf)",
           "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/inre-staden/sodermalm/sodermalm-stadsdelsomrade.pdf")
# Täby
_TAB_BAB = ("Täby kommun – Bostadsanpassning",
            "https://www.taby.se/omsorg-och-stod/funktionsnedsattning/hjalp-i-hemmet/bostadsanpassning")
_BAB_VAD = ("Boverket – Vad är bostadsanpassningsbidrag?",
            "https://www.boverket.se/sv/babhandboken/for-dig-som-soker/vad-ar-bostadsanpassningsbidrag/")
_BAB_SKICK = ("Boverket – Bostadsanpassningsbidrag: bostadens skick",
              "https://www.boverket.se/sv/babhandboken/bostadsanpassningsbidrag/villkor-for-bostadsanpassningsbidrag/bostadens-skick/")
_BAB_EFT = ("Boverket – Bostadsanpassningsbidrag: eftersatt underhåll",
            "https://www.boverket.se/sv/babhandboken/bostadsanpassningsbidrag/villkor-for-bostadsanpassningsbidrag/bostadens-skick/eftersatt-underhall/")
# Vasastan
_NVV = ("Stadsmuseet – Nordvästra Vasastaden, byggnadsinventering 1989 (pdf)",
        "https://stockholmskallan.stockholm.se/postfiles/KUL/SSM_Nordvastra_Vasastaden__byggn_inv_1989_00.pdf")
_SM_KLASS = ("Stadsmuseet – Kulturhistorisk klassificering",
             "https://stadsmuseet.stockholm/kunskap-och-samlingar/kulturmiljo/klassificering/")
_SB_SMI = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
           _SB + "stadsmuseets-kulturhistoriska-klassificering/")
_SB_KULT = ("Stockholms stad – Kulturhistorisk värdefull byggnad och område",
            _SB + "kulturhistorisk-vardefull-byggnad-och-omrade/")
_SB_ELD = ("Stockholms stad – Eldstad, braskamin och skorsten", _SB + "eldstad-braskamin-och-skorsten/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap.",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")

_ROT_SUM = ("Företaget får dra av högst 30 procent av arbetskostnaden på fakturan. Rotavdraget är högst 50 000 kr "
            "per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag.")
_IMG_END = ", realistic photo, no people, no text, no letters"

PAGES_TJ = {

# ------------------------------------------------------------------ NACKA
"totalrenovering-nacka.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Nacka", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Nacka – byt värmesystem i samma omgång",
  "description": "Totalrenovering i Nacka: byt värmesystem när villan ändå görs om – anmälan av bergvärme, borrhålets avstånd, Sicklaön, nytt bidrag och rotavdraget.",
  "h1": "Totalrenovering i Nacka",
  "lead": "När en villa ska renoveras från grunden är det ofta också läge att se över hur huset värms upp. Geal Entreprenad AB tar totalrenoveringar av villor i Nacka som en total entreprenad och planerar ett byte av värmesystem tillsammans med resten av ombyggnaden, så att rör, radiatorer och ventilation hamnar rätt från början.",
  "card": "Nytt värmesystem när huset ändå görs om.",
  "sections": [
    {"id": "varmen-nacka", "anchor": "Värmen",
     "h2": "Värmesystemet i samma omgång som resten av huset",
     "paras": [
       "Boverkets energiguide beskriver att en berg-, sjö- eller jordvärmepump kan installeras om huset har ett vattenburet värmesystem med golvvärme eller radiatorer. Saknas ett sådant system behöver det byggas först, och det arbetet är lättare att få in när golv och väggar ändå är öppna under en totalrenovering. Värmepumpen ska dimensioneras så att den täcker både värme och varmvatten.",
       "Guiden påpekar också att åtgärder som minskar effektbehovet, till exempel att täta fönster och dörrar, gör att du kan välja en mindre värmepump och att borrhålet inte behöver bli lika djupt. Därför bestämmer vi först vad som ska göras med fönster, isolering och täthet, och låter installatören dimensionera värmepumpen efter det.",
       "En sak glöms lätt bort. Har huset självdragsventilation bygger den på att skorstenen blir varm. När ved, olja eller pellets ersätts med en värmepump blir skorstensstocken kallare och ventilationen minskar, vilket enligt Boverket kan ge lukt, fukt och sämre inomhusluft, och fukt på vinden när den inte längre värms av skorstenen. Ventilationen behöver alltså ingå i samma plan.",
     ],
     "aside": {"title": "Planera i den här ordningen", "items": [
       "Fönster, täthet och isolering", "Värmebehov och dimensionering", "Vattenburet system", "Ventilation när skorstenen kallnar"]}},
    {"id": "anmalan-nacka", "h2": "Bergvärme ska anmälas till Nacka kommun",
     "paras": [
       "Nacka kommun skriver att värmepumpar som tar upp värme från mark eller vatten måste anmälas, medan en luftvärmepump inte kräver någon anmälan. Anmälan görs i kommunens e-tjänst och ska ange typ av värmepump, borrhålets placering, borrföretag och installatör. Kommunen råder dig att börja med att välja installatör, som ofta hjälper till att anlita borrföretaget.",
       "Borrhålet ska markeras på ett kartutdrag över fastigheten, som du kan hämta utan kostnad ur kommunens webbkarta, tillsammans med avståndet till närmaste tomtgräns och närliggande byggnad. Nacka tillämpar Sveriges geologiska undersöknings rekommenderade avstånd. Följs de inte räknas grannarna som berörda och har rätt att yttra sig. Motsätter sig en granne borrningen är det kommunen som avgör vem som har rätt.",
     ],
     "aside": {"title": "Avstånd från borrhålet", "items": [
       "10 m till grannens tomtgräns", "20 m till andra energibrunnar", "20 m till grävda brunnar", "30 m till borrade brunnar",
       "5 m till allmänna VA-ledningar"]}},
    {"id": "sicklaon-nacka", "h2": "Sicklaön, Sandasjön och ledningarna på tomten",
     "paras": [
       "Ligger villan i vissa delar av västra eller centrala Sicklaön måste kommunen rådfråga de ansvariga för utbyggnaden av tunnelbanan till Nacka innan borrningen bedöms. Bedömningen görs fastighet för fastighet, och på vissa fastigheter ska ett mätrör installeras i energibrunnen för att mäta grundvattennivån. Ligger fastigheten inom Sandasjöns vattenskyddsområde remitteras ärendet till Nacka vatten och avfall AB, och inom vattenskyddsområdets primära zon tillåts borrning vanligen inte.",
       "Du som fastighetsägare ska enligt kommunen känna till var ledningarna för vatten, avlopp med mera går på tomten, och du står för eventuella kostnader om borrningen skadar dem. Husritningar och tjänsten Ledningskollen ger en bild av vad som finns i marken. Vattnet från borrningen tas vanligtvis om hand på den egna fastigheten om det kan infiltrera där, annars ska det avslammas i container och transporteras bort.",
     ],
     "aside": None},
    {"id": "bidrag-nacka", "h2": "Bidrag för materialet, rotavdrag för arbetet",
     "paras": [
       "Sedan den 1 september 2026 kan småhusägare söka bidrag för energieffektivisering, och Nacka kommun hänvisar till sin energi- och klimatrådgivare, som ger opartisk och kostnadsfri rådgivning om vilka åtgärder och vilket uppvärmningssystem som passar huset. Enligt Boverket omfattas inte småhus som är anslutna till fjärrvärme eller har ett värdeår senare än 1989. Värdeåret kan justeras framåt vid större till- eller ombyggnader, så kontrollera uppgiften i beslutet om fastighetstaxering.",
       "Bidraget gäller bara materialkostnader, och Boverket skriver att arbetskostnaden därför kan ge rotavdrag. Ansökan ska komma in inom sex månader från att åtgärden påbörjades, och projektering räknas inte som påbörjad åtgärd. Om köket i en äldre villa finns mer under " + _L.format("koksrenovering-nacka.html", "köksrenovering i Nacka") + ", om vatten och avlopp när du bygger under " + _L.format("byggforetag-nacka.html", "byggföretag i Nacka") + " och om renovering av hela huset på sidan om " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till i Nacka",
  "steps": [
    ("Platsbesök", "Vi går igenom huset, dagens värmesystem, ventilationen och skorstenen."),
    ("Energiplan", "Fönster, täthet och isolering bestäms först, sedan dimensioneras värmen."),
    ("Skriftligt kostnadsförslag", "Arbete och material redovisas var för sig, vilket underlättar både bidrag och rotavdrag."),
    ("Anmälan", "Bergvärme anmäls till kommunen innan borrningen börjar."),
    ("Utförande", "Vi samordnar rivning, borrning, installationer och ytskikt med en kontakt för hela projektet."),
    ("Slutgenomgång", "Vi går igenom huset och det nya värmesystemet tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Nacka",
  "rot": [
    "Skatteverket ger rotavdrag för att installera och byta värmepumpar och värmepannor i ett småhus, men rotavdrag och skattereduktion för grön teknik kan inte ges för samma arbete. Markarbeten för värmeförsörjning och att riva väggar och bygga om planlösningen räknas också som rotarbete.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Nacka?",
  "price": [
    "Vilket värmesystem huset har i dag, om ett vattenburet system behöver dras in, hur mycket ventilationen behöver ändras och hur stor del av huset som renoveras väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver en luftvärmepump anmälas till Nacka kommun?",
     "Nej. Kommunen skriver att en värmepump som utvinner värme ur luften inte behöver anmälas. Bergvärme och andra värmepumpar som tar värme ur mark eller vatten ska anmälas."),
    ("Hur nära grannens tomtgräns får ett borrhål för bergvärme ligga i Nacka?",
     "Kommunen tillämpar rekommendationen minst 10 meter. Följs avstånden inte räknas grannarna som berörda och får yttra sig innan kommunen beslutar."),
    ("Går det att borra för bergvärme på västra Sicklaön?",
     "Det prövas från fall till fall. I delar av västra och centrala Sicklaön måste kommunen först rådfråga de ansvariga för tunnelbaneutbyggnaden, och på vissa fastigheter krävs ett mätrör i energibrunnen."),
    ("Kan man få både energibidrag och rotavdrag för en ny värmepump?",
     "Enligt Boverket täcker bidraget bara materialkostnaderna, så arbetskostnaden kan ge rotavdrag. Rotavdrag och skattereduktion för grön teknik går däremot inte att få för samma arbete."),
    ("Varför kan det bli fuktigt på vinden efter bytet till värmepump?",
     "I ett hus med självdrag hjälper den varma skorstenen ventilationen. Blir skorstensstocken kall minskar ventilationen, och vinden värms inte längre lika mycket, skriver Boverket."),
  ],
  "sources": [_NAC_VP, _NAC_EKR, _BOV_BID, _BOV_BERG, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska villan i Nacka byggas om och få ny värme?", "Boka ett gratis platsbesök, så går vi igenom huset och värmesystemet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Renoverat vardagsrum i en äldre trävilla med nya vattenradiatorer under spröjsade fönster",
     "renovated living room in an old Swedish wooden villa near the sea, new white water radiators under multi-pane windows, wide light pine floorboards, white panelled walls, view to pine trees and a bay, soft daylight, empty room" + _IMG_END),
    ("Liten borrigg för bergvärme på en bergig villatomt med skyddsskivor på gräsmattan",
     "small tracked geothermal drilling rig standing on a rocky Swedish villa garden plot beside an old wooden house, protective boards laid on the lawn, granite outcrops and pine trees, overcast daylight" + _IMG_END),
    ("Nyinstallerad bergvärmepump med isolerade rör i ett ljust pannrum",
     "newly installed ground source heat pump unit in a clean bright basement boiler room of a Swedish house, insulated pipes running along a white wall, grey painted concrete floor, plain unbranded casing" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SOLLENTUNA
"totalrenovering-sollentuna.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Sollentuna", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Sollentuna – mät radon före och efter",
  "description": "Totalrenovering i Sollentuna: varför radonhalten ska mätas när huset byggs om, kommunens radonkarta, blåbetong, tätning mot marken och rotavdraget.",
  "h1": "Totalrenovering i Sollentuna",
  "lead": "En stor renovering kan ändra hur luften rör sig i huset och därmed hur mycket radon som stannar inomhus. Geal Entreprenad AB totalrenoverar villor och radhus i Sollentuna och tar upp radonfrågan redan vid platsbesöket, så att eventuella åtgärder kan göras medan golv och väggar är öppna.",
  "card": "Radon med i planen för hela huset.",
  "sections": [
    {"id": "radon-sollentuna", "anchor": "Radon",
     "h2": "Kommunen nämner större renoveringar som skäl att mäta",
     "paras": [
       "Sollentuna kommun skriver att radonhalten i en byggnad behöver mätas var tionde år, eller i samband med större renoveringar, för att se till att den inte överstiger 200 becquerel per kubikmeter. Det är du som fastighetsägare som ansvarar för att mätningar görs och för att åtgärda om det behövs. Kommunen påpekar också att mätvärdena kan variera mellan närstående hus, eftersom byggnadsteknik, utförande och ventilation skiljer sig åt.",
       "Strålsäkerhetsmyndigheten rekommenderar en ny mätning när det har gått mer än tio år eller när byggnadsåtgärder som kan påverka radonhalten har genomförts. Myndigheten tar fönsterbyte som exempel: nya fönster kan ändra luftomsättningen i huset, och vid all renovering rekommenderas att radonhalten mäts igen. En totalrenovering rör ofta både fönster, ventilation och golv på en gång.",
     ],
     "aside": {"title": "Mät igen när", "items": [
       "Mer än tio år har gått", "Fönster har bytts", "Byggnadsåtgärder kan ha påverkat halten", "Huset har genomgått en större renovering"]}},
    {"id": "karta-sollentuna", "h2": "Radonkartan, blåbetongen och dricksvattnet",
     "paras": [
       "I kommunens radonkarta kan du se mätvärden på olika fastigheter. Kartan visar i nuläget bara enbostadshus, alltså villor, radhus och liknande, och mätningarna som syns är högst tio år gamla. Finns ingen mätning på din fastighet kan du fråga kommunens kontaktcenter. Ett lågt värde hos grannen säger dock inte säkert något om ditt hus, eftersom halterna varierar från hus till hus inom samma område.",
       "Radon kommer oftast från marken och berggrunden och tar sig in genom sprickor och otätheter i grunden eller där el, vatten och avlopp går in i byggnaden. Strålsäkerhetsmyndigheten skriver att radonhalten i marken är tillräcklig för att kunna ge för hög halt inomhus om huset är otätt mot marken. Radon kan också komma från blåbetong som tillverkades 1929–1975. Det kommunala dricksvattnet i Sollentuna är inte radonhaltigt, men har du egen brunn behöver du själv kontrollera vattnet.",
     ],
     "aside": None},
    {"id": "matning-sollentuna", "h2": "Mätningen ska passa in i tidplanen",
     "paras": [
       "En radonmätning bör pågå i minst två månader under eldningssäsongen, som enligt Strålsäkerhetsmyndigheten normalt är mellan den 1 oktober och den 30 april. I ett småhus mäts i minst två punkter och på varje plan med boendeutrymmen. Den vanligaste metoden är spårfilmsdosor från ett ackrediterat laboratorium, som du kan placera ut själv. I Sollentuna kan mätning beställas från oktober till slutet av februari.",
       "Det påverkar planeringen av en totalrenovering. Vill du veta om huset behöver radonåtgärder innan golven rivs upp behöver mätningen göras under vinterhalvåret före byggstarten. Blir huset klart under sommaren får den uppföljande långtidsmätningen vänta till nästa eldningssäsong. I vissa fall kan kommunens miljökontor också ha resultat från tidigare mätningar.",
     ],
     "aside": {"title": "Mätningen i korthet", "items": [
       "Minst två månader", "1 oktober–30 april", "Minst två punkter", "Varje plan med boendeutrymmen"]}},
    {"id": "atgarder-sollentuna", "h2": "Åtgärder medan golv och väggar är öppna",
     "paras": [
       "Strålsäkerhetsmyndigheten skriver att första steget är att ta reda på varifrån radonet kommer, och att en radonkonsult kan hjälpa till med utredningen. Kommer det från byggnadsmaterialet kan luftväxlingen ökas, och i enklare fall räcker ofta ett frånluftssystem med fläkt. Kommer det från marken kan sprickor och otätheter i grunden tätas, och räcker inte det kan en radonsug, radonbrunn eller smalrör skapa undertryck under huset. Efter åtgärden ska en ny långtidsmätning visa att den har haft effekt.",
       "Under en totalrenovering ligger genomföringar för rör och kablar ofta åtkomliga, och ventilationen byggs ändå om. Det radonbidrag som tidigare fanns går däremot inte längre att söka, enligt myndigheten. Om ventilation och stammar i badrummet finns mer under " + _L.format("badrumsrenovering-sollentuna.html", "badrumsrenovering i Sollentuna") + ", om köket under " + _L.format("koksrenovering-sollentuna.html", "köksrenovering i Sollentuna") + " och om större ombyggnader på sidan om " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till i Sollentuna",
  "steps": [
    ("Platsbesök", "Vi går igenom huset, grunden och ventilationen och frågar efter tidigare radonmätningar."),
    ("Mätning före", "Om tiden medger mäter du radonhalten under eldningssäsongen innan byggstart."),
    ("Skriftligt kostnadsförslag", "Eventuella radonåtgärder redovisas som egna poster, skilda från övrig renovering."),
    ("Rivning och tätning", "Genomföringar för el, vatten och avlopp tätas medan de går att komma åt."),
    ("Installationer och ytskikt", "Ventilation, rum och ytskikt byggs om i tur och ordning."),
    ("Mätning efter", "En ny långtidsmätning visar radonhalten i det renoverade huset."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Sollentuna",
  "rot": [
    "Skatteverket ger rotavdrag för att sanera radon i samband med byggarbete i ett småhus, liksom för att riva väggar och bygga om planlösningen. Att mäta radon ger däremot inget avdrag.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Sollentuna?",
  "price": [
    "Hur stor del av huset som renoveras, om grunden behöver tätas, om ventilationen ska byggas om och vilken standard rummen får väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Ska radonhalten mätas igen efter en totalrenovering i Sollentuna?",
     "Ja. Kommunen skriver att radon behöver mätas var tionde år eller i samband med större renoveringar, och Strålsäkerhetsmyndigheten rekommenderar ny mätning efter byggnadsåtgärder som kan påverka halten."),
    ("Kan vi gå efter grannens värde i Sollentunas radonkarta?",
     "Inte säkert. Kommunen påpekar att halten kan variera mellan närstående hus. Kartan visar bara enbostadshus och mätningar som är högst tio år gamla."),
    ("Kan blåbetong i väggarna ge radon?",
     "Ja, enligt Sollentuna kommun kan radon komma från blåbetong som tillverkades 1929–1975. Kommer radonet från byggnadsmaterialet kan ökad luftväxling sänka halten."),
    ("Går det att söka radonbidrag i dag?",
     "Nej. Strålsäkerhetsmyndigheten skriver att radonbidraget inte längre går att söka, eftersom inga medel finns avsatta i statens budget."),
    ("När på året kan radon mätas i ett hus i Sollentuna?",
     "Under eldningssäsongen, normalt 1 oktober–30 april, i minst två månader. Kommunen skriver att mätning kan beställas från oktober till slutet av februari."),
  ],
  "sources": [_SO_RADON, _SSM_SMAHUS, _SSM_FONSTER, _SSM_ATG, _SSM_BIDRAG, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska huset i Sollentuna totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom huset, grunden och ventilationen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Totalrenoverat enplanshus med öppen planlösning mellan kök och vardagsrum och ljust ekgolv",
     "renovated interior of a 1950s Swedish one-storey villa, open plan between a new white kitchen and the living room, light oak floor, white walls, a discreet exhaust air vent in the ceiling, large windows to a leafy garden, soft daylight, empty" + _IMG_END),
    ("Betonggolv i en källare under renovering med tätade genomföringar runt rör",
     "basement of a Swedish house during renovation, bare concrete floor slab with sealed joints around water pipe and cable penetrations, cracks filled with grey sealant, a work lamp on a tripod, clean and tidy" + _IMG_END),
    ("En liten radonmätare av plast på en vägghylla i ett sovrum",
     "one small plain white round plastic disc, completely smooth with no markings or labels, standing on an empty plain white wall shelf on an interior wall of a calm Swedish bedroom, away from windows and radiators, nothing else on the shelf, no books, no paper, winter daylight through the window" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SOLNA
"totalrenovering-solna.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Solna", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Solna – ny el i hela lägenheten",
  "description": "Totalrenovering i Solna: elen när bostadsrätten byggs om – vem som är innehavare, regler för det som ändras, dokumentationen, föreningen och ROT.",
  "h1": "Totalrenovering i Solna",
  "lead": "När en lägenhet totalrenoveras dras elen ofta om i samma veva som kök, badrum och väggar görs om. Geal Entreprenad AB totalrenoverar bostadsrätter i Solna och planerar elarbetet tillsammans med resten av lägenheten, från föreningens medgivande till dokumentationen du får när allt är klart.",
  "card": "Hela lägenheten, elen inräknad.",
  "sections": [
    {"id": "lagenheterna-solna", "anchor": "Lägenheterna",
     "h2": "Från Råsundas stenstad till 1950-talets hus",
     "paras": [
       "Solna stads förteckning över kulturhistoriskt värdefulla miljöer visar hur olika lägenhetshusen i staden är. Där finns bland annat Stenstaden i Råsunda, 1950-talsbebyggelsen i Råsunda, Skytteholm och Huvudsta, Hagalundshusen och Gamla Hagalund. I stadens karta över kulturhistoriskt klassade byggnader kan du se om just ditt hus är utpekat.",
       "Oavsett när huset byggdes gäller samma grundregler för dig som bor i en bostadsrätt. Solna stad skriver att du behöver fastighetsägarens medgivande för byggåtgärder. Att flytta köket kräver föreningens godkännande och i vissa fall en anmälan om ändring av vatten och avlopp. Att riva en vägg kräver godkännande, och är väggen bärande krävs en anmälan om ändring av bärande konstruktion. Staden råder dig att ställa krav på att den du anlitar bygger enligt bygglovet, följer kontrollplanen och dokumenterar bygget, och att begära slutbesked när allt är klart.",
     ],
     "aside": {"title": "Exempel ur stadens förteckning", "items": [
       "Stenstaden i Råsunda", "1950-talsbebyggelse i Råsunda", "1950-talsbebyggelse i Huvudsta", "Gamla Hagalund"]}},
    {"id": "innehavare-solna", "h2": "Vem ansvarar för elen i en bostadsrätt?",
     "paras": [
       "Elsäkerhetsverket skriver att alla bostäder har en elanläggning med en innehavare, och att det är innehavaren som ansvarar för att anläggningen är säker. I en bostadsrätt kan innehavaren vara du själv, bostadsrättsföreningen eller båda. Grundprincipen är att ansvaret ligger på den som har tillträde till att kontrollera anläggningen och rätt att ändra den.",
       "Som innehavare ska du se till att arbete på anläggningen görs av personer med rätt kompetens, och när du bygger om eller renoverar är det du som behöver ta reda på om anläggningen behöver uppdateras. Elinstallationer i bostäder får bara göras av ett elinstallationsföretag som är registrerat hos Elsäkerhetsverket för verksamhetstypen Bostäder, och det kan du kontrollera i myndighetens tjänst Kolla elföretaget. Vid en totalrenovering är det därför bra att tidigt reda ut med föreningen var gränsen går mellan lägenhetens el och husets.",
     ],
     "aside": None},
    {"id": "regler-solna", "h2": "Det som byggs om följer dagens regler",
     "paras": [
       "Enligt Elsäkerhetsverket finns det inga regler som säger att en befintlig elanläggning måste uppgraderas när nya säkerhetskrav införs. Huvudregeln är att anläggningen får vara utförd enligt de regler som gällde när den togs i bruk, förutsatt att den är i gott skick och att den inte används på ett nytt sätt som gör den farlig. Bygger du om eller utvidgar en gammal anläggning ska ombyggnaden däremot följa de nya kraven.",
       "Myndigheten tar själv ett exempel som ofta dyker upp i en totalrenovering: ett sovrum som görs om till badrum innebär ändringar i elanläggningen. Den påpekar också att det kan vara klokt att låta elinstallationsföretaget besiktiga hela anläggningen i samband med en renovering, eftersom åldrande elanläggningar kan innebära risk för strömgenomgång och brand. Då vet du vilka delar som kan sitta kvar och vilka som bör bytas medan väggarna ändå är öppna.",
     ],
     "aside": {"title": "Elen vid en totalrenovering", "items": [
       "Det gamla får sitta kvar om det är i gott skick", "Det som byggs om följer nya krav", "Besiktning av hela anläggningen", "Registrerat elinstallationsföretag"]}},
    {"id": "dokumentation-solna", "h2": "Papperen du ska ha när lägenheten är klar",
     "paras": [
       "För att kunna arbeta i anläggningen behöver elinstallationsföretaget veta hur den är uppbyggd, och som innehavare ska du lämna den informationen, ofta i form av gruppförteckningen till elcentralen. Saknas underlag kan företaget hjälpa till med en kartläggning. När arbetet är klart ska företaget lämna över dokumentation och uppdaterad märkning och kontrollera anläggningen innan den tas i bruk. Elsäkerhetsverket kallar dokumentationen ett kvitto på att arbetet uppfyller reglerna och råder dig att skriva in i avtalet vilken dokumentation du ska få.",
       "Har en del av renoveringen krävt anmälan ska du också begära slutbesked när allt är klart, påminner Solna stad. Om köket och anmälan finns mer under " + _L.format("koksrenovering-solna.html", "köksrenovering i Solna") + ", om badrum och stambyte under " + _L.format("badrumsrenovering-solna.html", "badrumsrenovering i Solna") + ", om väggar och förvaring under " + _L.format("snickare-solna.html", "snickare i Solna") + " och om renovering av hela bostaden på sidan om " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till i Solna",
  "steps": [
    ("Platsbesök", "Vi går igenom lägenheten, elcentralen och det du vill ändra."),
    ("Medgivande från föreningen", "Vi tar fram en beskrivning av åtgärderna som underlag till styrelsen."),
    ("Skriftligt kostnadsförslag", "El, VVS, rivning och ytskikt redovisas var för sig."),
    ("Anmälan vid behov", "Påverkas bärande väggar eller vatten och avlopp väsentligt görs en anmälan."),
    ("Utförande", "Elarbetet görs av ett registrerat elinstallationsföretag, samordnat med övriga moment."),
    ("Överlämning", "Du får dokumentation över elen och vi går igenom lägenheten tillsammans."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Solna",
  "rot": [
    "I en bostadsrätt ger Skatteverket rotavdrag för att installera och komplettera elcentraler, dra elledningar från proppskåpet ut i bostaden och byta vägguttag eller installera inbyggda spotlights. Arbetet ska göras innanför lägenhetens tak, väggar och golv och gälla det du ansvarar för enligt stadgarna. Att dra el till en elcentral utanför bostaden ger inget avdrag.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Solna?",
  "price": [
    "Hur mycket av elen som byts, om kök eller badrum flyttas, hur många väggar som ändras och vilken standard lägenheten får väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste all gammal el bytas när lägenheten i Solna totalrenoveras?",
     "Nej. Elsäkerhetsverket skriver att en befintlig anläggning i gott skick får vara utförd enligt de regler som gällde när den togs i bruk. Det som byggs om eller utvidgas ska följa de nya kraven."),
    ("Är det jag eller föreningen som ansvarar för elen i lägenheten?",
     "Det kan vara du, föreningen eller båda. Enligt Elsäkerhetsverket ligger ansvaret på den som har tillträde till att kontrollera anläggningen och rätt att ändra den."),
    ("Vilka papper ska vi få efter elarbetet?",
     "Dokumentation och underlag över arbetet samt uppdaterad märkning av anläggningen. Elsäkerhetsverket råder dig att skriva in i avtalet vilken dokumentation som ska lämnas."),
    ("Ger en ny elcentral i bostadsrätten rotavdrag?",
     "Ja, Skatteverket godkänner att installera och komplettera elcentraler i bostaden. Att dra el till en elcentral utanför lägenheten ger inget avdrag."),
    ("Vad säger Solna stad om att riva en vägg i en bostadsrätt?",
     "Det kräver föreningens godkännande men inte bygglov. Är väggen bärande krävs en anmälan om ändring av bärande konstruktion."),
  ],
  "sources": [_SOL_LGH, _SOL_VA, _SOL_KM, _ELS_ANSV, _ELS_RENO, _ELS_DOK, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska lägenheten i Solna göras om helt?", "Boka ett gratis platsbesök, så går vi igenom lägenheten och elen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Totalrenoverad lägenhet med nytt kök, inbyggda spotlights och ekparkett",
     "renovated apartment in a 1940s Swedish suburban stone building, open kitchen with white cabinets and a light worktop, new recessed ceiling spotlights, white wall sockets above the worktop, oak parquet floor, tall windows, empty, soft daylight" + _IMG_END),
    ("Ny elcentral med automatsäkringar i en lägenhetshall",
     "close-up of a newly installed small white residential fuse box with two rows of plain white circuit breakers in an apartment hallway wall, cover open, neatly routed white cables, completely unmarked blank surfaces without any labels, numbers or symbols" + _IMG_END),
    ("Rum under renovering med nyfrästa spår och elrör fram till dosor i väggen",
     "close-up of a bare grey plastered wall in an apartment under renovation with several freshly cut narrow vertical and horizontal grooves in the plaster, grey flexible corrugated electrical conduit pipes laid in the grooves and ending in round recessed wall boxes, dust sheets on the floor, daylight from a tall window" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SÖDERMALM
"totalrenovering-sodermalm.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Södermalm", "svc_label": "Totalrenovering",
  "title": "Totalrenovering på Södermalm – lägenheten och stambytet",
  "description": "Totalrenovering på Södermalm: samordna lägenhetens renovering med föreningens stambyte – anmälan, tillgänglighet i badrummet och rotavdraget.",
  "h1": "Totalrenovering på Södermalm",
  "lead": "Står föreningen inför ett stambyte kan det vara klokt att låta totalrenoveringen av lägenheten följa samma tidplan. Geal Entreprenad AB totalrenoverar bostadsrätter på Södermalm och planerar arbetet i lägenheten så att det går ihop med det föreningen gör i husets stammar.",
  "card": "Lägenheten i takt med stambytet.",
  "sections": [
    {"id": "bostaderna-sodermalm", "anchor": "Bostäderna",
     "h2": "Över 43 000 bostadsrätter i stadsdelsområdet",
     "paras": [
       "Stadens områdesfakta för Södermalms stadsdelsområde visar 77 525 bostäder år 2025. Av dem är 43 680 bostadsrätter, och nästan alla ligger i flerbostadshus och övriga hus. Bara 211 bostäder finns i småhus. I flerbostadshusen är två rum och kök den vanligaste storleken, med 21 466 lägenheter.",
       "En totalrenovering på Södermalm gäller alltså i regel en lägenhet i ett hus där vatten- och avloppsstammarna går genom flera lägenheter. När föreningen planerar ett stambyte öppnas badrum och kök i hela huset, och då kan det vara läge att göra om resten av lägenheten i samma period i stället för att riva upp nya ytor två gånger.",
     ],
     "aside": {"title": "Södermalm 2025", "items": [
       "77 525 bostäder", "43 680 bostadsrätter", "211 bostäder i småhus", "21 466 lägenheter om två rum och kök"]}},
    {"id": "stambyte-sodermalm", "h2": "När stambytet behöver anmälas",
     "paras": [
       "Stockholms stad skriver att ett stambyte oftast innebär att befintliga installationer byts ut i samma läge, och då behövs ingen anmälan. En anmälan och ett startbesked krävs däremot om VA-stammarna placeras i nya lägen eller om stambytet innebär väsentliga ingrepp i byggnadens bärande konstruktion. Är du osäker om bärande delar berörs råder staden dig att kontakta en konstruktör. Oavsett anmälningsplikt ska arbetet följa reglerna för arbeten i våtrum och för vatteninstallationer.",
       "För din del av planen betyder det att placeringen av badrum och kök bör vara bestämd innan föreningen låser sin projektering. Vill du flytta badrummet så att en stam hamnar i ett nytt läge blir det en anmälningspliktig ändring, och staden skriver att du inte får börja innan startbesked har getts. Ta därför upp önskemålen med styrelsen så tidigt som möjligt, och informera gärna grannarna om vad du planerar.",
       "Staden skiljer också mellan ändring och ombyggnad. Vid en ändring gäller anmälan bara den del av byggnaden som ändras. Vid en ombyggnad förnyas hela eller en betydande och avgränsbar del av byggnaden på ett påtagligt sätt, och då gäller ansökan eller anmälan hela byggnaden. Vid en sådan ombyggnad av ett befintligt flerbostadshus, där installationerna för tappvarmvatten nyinstalleras eller ändras väsentligt, ska individuell mätning och debitering av varmvattnet installeras. Det är föreningens fråga, men bra att känna till när ditt badrum och kök ritas.",
     ],
     "aside": None},
    {"id": "tillganglighet-sodermalm", "h2": "Badrumsgolvet får inte hamna för högt",
     "paras": [
       "Staden påpekar att tillgängligheten inte får försämras vid ett stambyte. Som exempel på försämrad tillgänglighet nämns att golven i wc eller badrum höjs, att inredning placeras på ett olämpligt sätt eller att dörröppningar blir för smala.",
       "I praktiken är det ofta golvet som är svårast. Nytt tätskikt, golvvärme och fall mot golvbrunnen ska rymmas utan att tröskeln mot hallen blir ett hinder. Därför ritar vi badrummet i lägenhetens helhet: dörrbredder, golvnivåer i angränsande rum och var tvättmaskin och dusch ska stå. När hela lägenheten ändå görs om kan golvnivåerna i hall och badrum planeras samtidigt i stället för att anpassas i efterhand.",
     ],
     "aside": {"title": "Försämrad tillgänglighet enligt staden", "items": [
       "Höjda golv i wc eller badrum", "Olämpligt placerad inredning", "För smala dörröppningar"]}},
    {"id": "rot-grans-sodermalm", "h2": "Föreningens arbete, ditt arbete och rotavdraget",
     "paras": [
       "I en bostadsrätt ger Skatteverket rotavdrag för arbete innanför lägenhetens tak, väggar och golv som du ansvarar för enligt stadgarna. Det gäller till exempel att dra vatten- och avloppsledningar som tjänar bostaden, byta golvbrunn, installera blandare och sätta kakel och klinker. Att utföra stambyten, flytta eller byta ut avloppsrör eller flytta golvbrunnen ger däremot inget avdrag.",
       "Gränsen mellan föreningens beställning och din blir därför viktig. I vårt kostnadsförslag står det du själv beställer för sig, så att det går att se vad som kan ge rotavdrag. Om badrummet och ansvaret vid vattenskador finns mer under " + _L.format("badrumsrenovering-sodermalm.html", "badrumsrenovering på Södermalm") + ", om köket under " + _L.format("koksrenovering-sodermalm.html", "köksrenovering på Södermalm") + ", om snickerier under " + _L.format("snickare-sodermalm.html", "snickare på Södermalm") + " och om större renoveringar på sidan om " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till på Södermalm",
  "steps": [
    ("Platsbesök", "Vi går igenom lägenheten och vad du vill ändra i badrum, kök och planlösning."),
    ("Samråd med styrelsen", "Föreningens tidplan för stambytet och gränsen mellan föreningens och ditt arbete."),
    ("Skriftligt kostnadsförslag", "Det du själv beställer redovisas för sig, med arbete och material åtskilda."),
    ("Anmälan vid behov", "Hamnar en stam i nytt läge görs en anmälan och vi inväntar startbesked."),
    ("Utförande", "Lägenheten byggs om i takt med stambytet, med skyddade trapphus och ytor."),
    ("Slutgenomgång", "Vi går igenom lägenheten rum för rum tillsammans med dig, med badrum, kök och golvnivåer."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering på Södermalm",
  "rot": [
    "Rotavdraget i en bostadsrätt gäller bara arbete inne i lägenheten som du ansvarar för enligt föreningens stadgar. Stambyten och flyttade avloppsrör eller golvbrunnar ger inget avdrag, även om de görs samtidigt som din renovering.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Södermalm?",
  "price": [
    "Hur mycket av lägenheten som görs om, om badrum eller kök flyttas, hur arbetet samordnas med föreningens stambyte och vilken standard du väljer påverkar mest. Arbetar föreningens entreprenör och vi i samma lägenhet bestäms ordningen mellan momenten i förväg. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste föreningens stambyte på Södermalm anmälas till staden?",
     "Oftast inte. Stockholms stad skriver att ett byte där installationerna hamnar i samma läge inte behöver anmälas, men att nya lägen för VA-stammarna eller väsentliga ingrepp i bärande konstruktion kräver anmälan och startbesked."),
    ("Vilka VVS-arbeten i badrummet ger rotavdrag i en bostadsrätt?",
     "Arbete innanför lägenhetens tak, väggar och golv som du ansvarar för, till exempel ledningar som tjänar bostaden, byte av golvbrunn och blandare. Stambyten och flyttad golvbrunn ger inget avdrag."),
    ("Får badrumsgolvet byggas högre när badrummet görs om?",
     "Staden skriver att tillgängligheten inte får försämras, och nämner höjda golv i wc eller badrum som exempel. Golvnivån behöver därför planeras med tröskel och dörrbredd."),
    ("Hur många bostadsrätter finns det på Södermalm?",
     "Enligt stadens områdesfakta fanns 43 680 bostadsrätter av totalt 77 525 bostäder i Södermalms stadsdelsområde år 2025."),
    ("När får arbetet börja om en ny stam placeras i ett nytt läge?",
     "Först när staden har gett startbesked. En stam i nytt läge räknas som en väsentlig ändring som ska anmälas."),
  ],
  "sources": [_OF_SOD, _SB_STAM, _SB_VA, _SB_OMB, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska lägenheten på Södermalm göras om i samband med stambytet?", "Boka ett gratis platsbesök, så går vi igenom lägenheten och föreningens planer innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Totalrenoverad lägenhet i ett äldre stenhus med nytt badrum och fiskbensparkett i hallen",
     "renovated apartment in an 1890s Stockholm stone building, view from a hallway with oak herringbone parquet into a new bathroom with light grey tiles, tall white panelled doors with mouldings, high ceilings, soft daylight, empty" + _IMG_END),
    ("Öppet schakt i ett badrum under stambyte med nya avloppsrör och vattenledningar",
     "corner of a stripped old apartment bathroom during pipe replacement, seen from the doorway at eye level, an open rectangular wall shaft in the corner with a new vertical grey plastic drain stack and two new copper water pipes, bare concrete floor, rough plastered walls, normal wide-angle photo" + _IMG_END),
    ("Badrumsdörr med låg tröskel mellan ekparkett och nytt klinkergolv",
     "close-up of a bathroom doorway in an old apartment with a very low threshold between oak parquet and a new matte grey tiled floor, white painted door frame, soft daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ TÄBY
"totalrenovering-taby.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Täby", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Täby – bygg om för att kunna bo kvar",
  "description": "Totalrenovering i Täby: trösklar, dörrar och badrum när huset görs om för att fungera längre – villkoren för bostadsanpassningsbidrag och rotavdraget.",
  "h1": "Totalrenovering i Täby",
  "lead": "När ett hus ska totalrenoveras är det ett bra tillfälle att tänka på hur det ska fungera om några år, när trösklar, trappor och ett trångt badrum kan bli ett hinder. Geal Entreprenad AB totalrenoverar villor och radhus i Täby och tar med framkomligheten i planen från början.",
  "card": "Ett hus som går att bo kvar i.",
  "sections": [
    {"id": "bo-kvar-taby", "anchor": "Bo kvar",
     "h2": "Det som gör huset lättare att bo kvar i",
     "paras": [
       "Boverkets handbok om bostadsanpassningsbidrag ger exempel på vanliga anpassningar: att ta bort trösklar, ordna en duschplats i stället för badkar, installera en spisvakt, bygga en ramp till entrén och bredda dörröppningar. Täby kommun nämner också stödhandtag, anpassade badrum och dörrautomatik. Det handlar om att kunna förflytta sig inomhus och ta sig in i och ut ur bostaden.",
       "Många av de ändringarna rör just de delar som ändå byggs om i en totalrenovering. När innerväggar rivs och byggs upp igen kan dörröppningarna göras bredare. När golven läggs om kan nivåskillnaderna mellan rummen tas bort. När badrummet görs om kan duschen hamna i golvnivå med plats att röra sig runt. Att planera för det från början är oftast enklare än att bygga om en färdig yta senare.",
     ],
     "aside": {"title": "Exempel på anpassningar", "items": [
       "Ta bort trösklar", "Dusch i stället för badkar", "Bredare dörröppningar", "Ramp till entrén", "Spisvakt"]}},
    {"id": "bidraget-taby", "h2": "Bostadsanpassningsbidraget i Täby",
     "paras": [
       "Har du en bestående funktionsnedsättning och behöver anpassa bostaden för att kunna bo kvar kan du söka bostadsanpassningsbidrag hos Täby kommun. Bidraget gäller fasta funktioner, och behovet ska inte kunna lösas på ett enklare sätt, till exempel med hjälpmedel. Du ansöker i kommunens e-tjänst och bifogar ett intyg från arbetsterapeut, fysioterapeut, läkare eller annan medicinskt sakkunnig som styrker att åtgärderna är nödvändiga.",
       "Kommunen skriver att det är den som ansöker som är beställare av arbetet, och att konsumenttjänstlagen därför gäller mellan dig och den entreprenör som utför det. Bidraget betalas ut när åtgärden är slutförd. Boverket påpekar att man normalt söker innan något görs. Det går att söka i efterhand, men då kan det vara svårare att utreda om villkoren är uppfyllda. Kommunen ska inte heller bedöma din ekonomi. Bidraget omfattar i princip alla typer av funktionsnedsättningar, till exempel rörelsenedsättning, nedsatt syn eller allergi, men nedsättningen ska vara bestående eller åtminstone långvarig. Täby kommun skriver att handläggaren kan hjälpa dig att ta in offerter och fastighetsägarens medgivande.",
     ],
     "aside": None},
    {"id": "villkoren-taby", "h2": "Villkor som påverkar en totalrenovering",
     "paras": [
       "Enligt lagen om bostadsanpassningsbidrag lämnas inget bidrag om åtgärderna behövs på grund av byggnadstekniska brister, eftersatt underhåll, avsaknad av eller avsevärda brister i grundläggande bostadsfunktioner eller avvikelser från bygglagstiftningens krav på tillgänglighet. Den sista punkten gäller bara när sökanden själv har låtit uppföra eller ändra huset. Om en ombyggnad som du beställer avviker från tillgänglighetskraven kan du alltså inte räkna med bidrag för att rätta till just det senare.",
       "Boverket betonar samtidigt att omodernt inte är en avslagsgrund. Ett äldre kök med lägre diskbänk som fungerade innan funktionsnedsättningen bör kunna anpassas med bidrag. Vid bedömningen av eftersatt underhåll ska delarna bedömas utifrån hur de användes före anpassningen. Därför håller vi isär det som är renovering och det som är anpassning i planen, och bygger det som ändras så att tillgängligheten inte blir sämre.",
     ],
     "aside": {"title": "Inget bidrag om åtgärden behövs på grund av", "items": [
       "Byggnadstekniska brister", "Eftersatt underhåll", "Brister i grundläggande bostadsfunktioner", "Egen avvikelse från tillgänglighetskraven"]}},
    {"id": "planera-taby", "h2": "Ett hus i ett plan, eller ett plan som räcker",
     "paras": [
       "Täby kommun påpekar att den som byter bostad förväntas välja en som passar ens förutsättningar. Den som inte klarar trappor och flyttar till ett hus med trappor kan inte få bidrag för en trapphiss. För dig som vill stanna i huset du har kan en totalrenovering vara tillfället att samla sovrum, badrum och kök på entréplanet. Om badrummet finns mer under " + _L.format("badrumsrenovering-taby.html", "badrumsrenovering i Täby") + ", om köket under " + _L.format("koksrenovering-taby.html", "köksrenovering i Täby") + ", om golvet där en vägg har rivits under " + _L.format("golvslipning-taby.html", "golvslipning i Täby") + " och om större ombyggnader på sidan om " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går totalrenoveringen till i Täby",
  "steps": [
    ("Platsbesök", "Vi går igenom hur du rör dig i huset: entré, trappor, dörrar och badrum."),
    ("Plan", "Renovering och anpassningar läggs i samma plan, med dörrbredder och golvnivåer."),
    ("Skriftligt kostnadsförslag", "Anpassningar och övrig renovering redovisas som egna poster."),
    ("Ansökan", "Söker du bostadsanpassningsbidrag gör du det hos kommunen innan arbetet."),
    ("Utförande", "Vi samordnar rivning, installationer och ytskikt med en kontakt för hela projektet."),
    ("Slutgenomgång", "Vi går igenom huset tillsammans med dig när allt är klart."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Täby",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att riva väggar och bygga om planlösningen och att göra förbättringsarbeten, till exempel att byta våtrumstapet mot kakel. Huset ska vara äldre än fem år, och större delen av den ursprungliga stommen ska behållas.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Täby?",
  "price": [
    "Hur många väggar och dörröppningar som ändras, om golvnivåer ska jämnas ut, hur badrum och kök byggs om och vilken standard du väljer väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan man få bostadsanpassningsbidrag i Täby när huset ändå ska renoveras?",
     "Bidraget gäller anpassningar som är nödvändiga på grund av en bestående funktionsnedsättning, inte renoveringen i övrigt. Det lämnas inte för åtgärder som behövs på grund av eftersatt underhåll."),
    ("Vem är beställare när arbetet betalas med bostadsanpassningsbidrag?",
     "Den som ansöker. Täby kommun skriver att konsumenttjänstlagen därför gäller mellan dig och entreprenören."),
    ("Vilket intyg behövs för att söka bostadsanpassning i Täby?",
     "Ett intyg från arbetsterapeut, fysioterapeut, läkare eller annan medicinskt sakkunnig som styrker att åtgärderna är nödvändiga."),
    ("Kan ett äldre kök anpassas med bidrag fast det är omodernt?",
     "Ja. Boverket skriver att omodernt inte är en avslagsgrund, och tar ett äldre kök med lägre diskbänk som exempel."),
    ("Kan bidrag nekas om vår egen ombyggnad inte följer tillgänglighetskraven?",
     "Ja. Lagen undantar åtgärder som behövs på grund av avvikelser från tillgänglighetskraven när sökanden själv har låtit ändra huset."),
  ],
  "sources": [_TAB_BAB, _BAB_VAD, _BAB_SKICK, _BAB_EFT, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska huset i Täby göras om för att fungera längre?", "Boka ett gratis platsbesök, så går vi igenom hur du använder huset innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Totalrenoverat enplanshus med breda dörröppningar utan trösklar mellan kök och vardagsrum",
     "renovated single-storey Swedish 1970s house interior, wide doorways without thresholds between the kitchen and the living room, light oak floor running through all rooms, white kitchen with a lowered section of worktop, large windows to a garden, soft daylight, empty" + _IMG_END),
    ("Badrum med dusch i golvnivå, stödhandtag och fällbar duschsits",
     "spacious bathroom in a Swedish house with a walk-in shower level with the floor, light grey tiles, white fold-down shower seat and grab bars on the wall, wide door opening, uncluttered, soft light" + _IMG_END),
    ("Entré till ett villahus med låg ramp och bred ytterdörr",
     "entrance of a Swedish 1970s brick and wood house with a long sloping concrete wheelchair ramp without any steps, with a simple metal handrail, leading to a wide front door at ground level under a small porch roof, low shrubs beside the path, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VASASTAN
"totalrenovering-vasastan.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Vasastan", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Vasastan – husets värden och eldstäder",
  "description": "Totalrenovering i Vasastan: Stadsmuseets inventering och klassificering, varsamhet inomhus, kakelugn och eldstad, föreningens tillstånd och rotavdraget.",
  "h1": "Totalrenovering i Vasastan",
  "lead": "I Vasastans stenstad har många lägenheter förändrats sedan husen byggdes, men det som finns kvar kan vara just det som ger huset dess värde. Geal Entreprenad AB totalrenoverar bostadsrätter i Vasastan och tar reda på vad som är utpekat i huset innan något rivs.",
  "card": "Hela lägenheten, med husets värden kvar.",
  "sections": [
    {"id": "husen-vasastan", "anchor": "Husen",
     "h2": "Små lägenheter i gårdshusen, större mot gatan",
     "paras": [
       "Stadsmuseets inventering av nordvästra Vasastaden omfattar området mellan Norrtullsgatan, Norra Stationsgatan, Gävlegatan, S:t Eriksgatan och Odengatan. Där började området söder om Karlbergsvägen bebyggas på 1880- och 1890-talen. De flesta som flyttade dit kom ur arbetar- eller lägre tjänstemannaklassen, och merparten av lägenheterna var små. Gathusen kunde ha något större och mer påkostade lägenheter, medan de enklaste låg i gårdshusen, och några praktlägenheter finns mot Odengatan, Karlbergsvägen och S:t Eriksgatan.",
       "Inventeringen berättar också att få hus från början hade hiss, och att badrum och tvättstuga ofta låg i gemensamma lokaler på vinden eller på gården. I många av de äldsta husen kan lägenhetens badrum alltså vara ett senare tillägg. Husen inventerades 1974–78, och sedan dess har många förändringar skett både interiört och exteriört. Det som ser ursprungligt ut behöver därför inte vara det.",
     ],
     "aside": {"title": "Nordvästra Vasastaden enligt Stadsmuseet", "items": [
       "Bebyggt från 1880-talet", "Små lägenheter i gårdshusen", "Praktlägenheter mot de stora gatorna", "Badrum ofta i gemensamma lokaler"]}},
    {"id": "klassning-vasastan", "h2": "Blått, grönt, gult eller grått på Stadsmuseets karta",
     "paras": [
       "Stadsmuseet klassificerar byggnader i tre nivåer. Blått omfattar miljöer med synnerligen höga kulturhistoriska värden. Grönt betyder att miljön bedöms vara särskilt värdefull från historisk, kulturhistorisk, miljömässig eller konstnärlig synpunkt. Gult betyder positiv betydelse för stadsbilden och/eller visst kulturhistoriskt värde, medan grått inte går att hänföra till någon av kategorierna. Streckade fält är ännu inte klassificerade. Klassificeringen är ett expertutlåtande utan juridisk verkan, och prövningen görs i bygglovsprocessen.",
       "Motiveringarna till klassificeringen finns i Bebyggelseregistret, och inventeringar och faktablad kan finnas på Digitala Stadsmuseet. Stockholms stad skriver att alla ändringar ska göras varsamt, och att en särskilt kulturhistoriskt värdefull byggnad inte får förvanskas, oavsett om åtgärden kräver lov eller anmälan. Inför arbetet kan en antikvarisk förundersökning och en konsekvensbeskrivning behövas, och ibland en sakkunnig inom kulturvärden. Är du osäker kan du kontakta Stadsmuseet med adress, fastighetsbeteckning, byggnadsår, kända ombyggnader och foton.",
     ],
     "aside": None},
    {"id": "eldstad-vasastan", "h2": "Kakelugnen, öppna spisen och rökkanalen",
     "paras": [
       "Finns det en kakelugn eller öppen spis i lägenheten väcker en totalrenovering ofta frågan om den ska användas igen eller kompletteras. Stockholms stad kräver anmälan och startbesked för att installera en eldstad, skorsten eller rökkanal, för att sätta in eller byta en spisinsats om eldningsförhållandena ändras, för att byta till en tyngre eldstad som kräver förstärkning och för en ny anslutning till befintlig rökkanal med håltagning och murning. Staden råder dig att tidigt rådgöra med skorstensfejarmästaren.",
       "Nya eldstäder för ved eller pellets ska klara krav på utsläpp och lägsta verkningsgrad, och en CE-märkt produkt uppfyller dem. Miljöförvaltningen har tillsyn över eldningen och kan kräva att den begränsas om den orsakar olägenhet för människors hälsa. I en bostadsrätt krävs dessutom styrelsens tillstånd enligt bostadsrättslagen för att installera eller ändra en eldstad eller rökkanal. Om dörrar och foder finns mer under " + _L.format("malare-vasastan.html", "målare i Vasastan") + ", om badrummet under " + _L.format("badrumsrenovering-vasastan.html", "badrumsrenovering i Vasastan") + ", om golven under " + _L.format("golvlaggare-vasastan.html", "golvläggare i Vasastan") + " och om större renoveringar på sidan om " + _L.format("villarenovering.html", "villarenovering") + ".",
     ],
     "aside": {"title": "Anmälan krävs bland annat för", "items": [
       "Ny eldstad, skorsten eller rökkanal", "Spisinsats med ändrade eldningsförhållanden", "Tyngre eldstad som kräver förstärkning", "Ny anslutning till befintlig rökkanal"]}},
    {"id": "oklassat-vasastan", "h2": "Om huset är streckat eller inte inventerat",
     "paras": [
       "Stadsmuseet uppdaterar kartan när nya bedömningar görs, och värderingarna kan ändras över tid. Ett streckat fält betyder att fastigheten ännu inte är klassificerad, till exempel för att bebyggelsen var för ung när klassificeringen gjordes. Museet tillämpar i dag en tidsgräns på tjugo år för det som ska värderas, och skriver att fastigheter som inte är klassificerade ändå kan ha stora kulturhistoriska värden.",
       "Stockholms stad påpekar att kartan bara ger en första indikation och att det är du som byggherre som ansvarar för att ta reda på vad som gäller för fastigheten. Är huset blått eller grönt, eller omfattas det av skyddsbestämmelser i detaljplanen, krävs bygglov för åtgärder som annars kan vara bygglovsbefriade. Det är därför bra att ha klassificeringen och planbestämmelserna framför sig innan ritningarna till en totalrenovering görs, särskilt om renoveringen också berör fönster, balkong eller annat som syns utåt.",
     ],
     "aside": {"title": "Bygglov för annars lovfria åtgärder om huset", "items": [
       "Är blått eller grönt på kartan", "Ligger i ett riksintresse för kulturmiljövården", "Har skyddsbestämmelser i detaljplanen"]}},
  ],
  "steps_h2": "Så går totalrenoveringen till i Vasastan",
  "steps": [
    ("Platsbesök", "Vi går igenom lägenheten och noterar dörrar, lister, stuckatur, fasta skåp och eldstäder."),
    ("Husets värden", "Vi läser klassificeringen och motiveringen i Bebyggelseregistret tillsammans med dig."),
    ("Föreningens tillstånd", "Vi tar fram en beskrivning av åtgärderna som underlag till styrelsen."),
    ("Skriftligt kostnadsförslag", "Det som ska bevaras, renoveras och byggas nytt redovisas var för sig."),
    ("Utförande", "Det som ska vara kvar skyddas, och eldstadsarbete börjar först efter startbesked."),
    ("Slutgenomgång", "Vi går igenom lägenheten rum för rum tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering i Vasastan",
  "rot": [
    "I en bostadsrätt ger Skatteverket rotavdrag för att mura och reparera öppen spis och kakelugn, liksom för annat arbete innanför lägenhetens tak, väggar och golv som du ansvarar för enligt stadgarna. Att sota skorstenar eller kontrollera eldstäder ger inget avdrag, och inte heller arbete på gemensamma ytor som tak, fasader, trapphus och entréer.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Vasastan?",
  "price": [
    "Hur mycket av lägenheten som görs om, hur mycket av snickerier, stuckatur och eldstäder som ska bevaras och skyddas, om en eldstad ska tas i bruk igen och vilka krav föreningen ställer på arbetet påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad betyder gul klassning på Stadsmuseets karta?",
     "Att miljön bedöms ha positiv betydelse för stadsbilden och/eller visst kulturhistoriskt värde. Blått och grönt är de högre nivåerna."),
    ("Har Stadsmuseets klassificering juridisk verkan?",
     "Nej. Stadsmuseet beskriver den som ett expertutlåtande. Prövningen görs i bygglovsprocessen, men varsamhetskravet och förvanskningsförbudet i plan- och bygglagen gäller ändå."),
    ("Måste en ny braskamin i lägenheten i Vasastan anmälas?",
     "Ja. Stockholms stad kräver anmälan och startbesked för att installera en eldstad, och råder dig att tidigt rådgöra med skorstensfejarmästaren."),
    ("Ger det rotavdrag att mura om kakelugnen i en bostadsrätt?",
     "Ja, Skatteverket godkänner att mura och reparera öppen spis och kakelugn i bostadsrätten. Sotning och kontroll av eldstäder ger inget avdrag."),
    ("Var hittar jag motiveringen till hur mitt hus i Vasastan är klassat?",
     "I Bebyggelseregistret. Inventeringar och faktablad kan också finnas på Digitala Stadsmuseet."),
  ],
  "sources": [_NVV, _SM_KLASS, _SB_SMI, _SB_KULT, _SB_ELD, _BRL, _SKV_JOB, _SKV_ROT],
  "cta": ("Ska lägenheten i Vasastan totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom lägenheten och husets värden innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Renoverat rum i ett sekelskifteshus med eldstad, takstuckatur och fiskbensparkett",
     "renovated apartment in an 1890s Stockholm stone building, preserved tall traditional Swedish white glazed ceramic tile stove (kakelugn), a tall cylindrical tower of white tiles reaching almost to the ceiling, standing in the corner of the room, no metal wood stove, oak herringbone parquet, high ceiling with plaster cornice, tall windows, freshly painted pale walls, empty, soft daylight" + _IMG_END),
    ("Takstuckatur och takrosett skyddade medan rummet under renoveras",
     "high ceiling with ornate plaster cornice and a ceiling rose in an old apartment, the room below under renovation with dust sheets on the floor and a trestle, daylight from tall windows" + _IMG_END),
    ("Närbild på mässingsluckor och vitt glaserat kakel på en gammal kakelugn",
     "close-up of the brass doors of an old Swedish tiled stove with white glazed tiles, freshly cleaned, soft daylight" + _IMG_END),
  ],
},

}
