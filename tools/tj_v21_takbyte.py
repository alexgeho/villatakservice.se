# -*- coding: utf-8 -*-
"""Takbyte – ortsidor v21: Nacka, Haninge, Järfälla, Tyresö, Värmdö, Österåker (2026-10-26).
Hubb: takbyte.html (vanlig tjänstesida i generate.py, listar ortsidorna). Intent: byte av hela taktäckningen
(pannor/plåt, underlag, läkt, plåtdetaljer) med regler, kontroll och ROT – skild från ortens takrenovering-<ort>.html
(lagning/omläggning, ortens epoker och kulturmiljöer), taklaggare-<ort>.html (yrket, tjänsteöversikt),
platslagare-<ort>.html och från v5-sidorna (Bromma, Danderyd, Huddinge, Norrtälje, Sollentuna, Täby: lertegel,
lovfrågan underhåll/ändring, solceller och totalförsvar, vikt/anmälan, snö och vind, fritidshus, kulturmiljöhandböcker).
Lokal vinkel per sida:
Nacka – allt som går genom taket (skorsten, ventilationshuvar, antenner, takfönster) som fasadändring i kommunens
lista, eldstad/skorsten och anmälan, utökad lovplikt (lila/orange i kartan) och grannarna efter 1 december 2025;
Haninge – kontrollplan och riskbedömning när takbytet kräver lov eller anmälan: kommunens exempelmallar punkt för
punkt (bärförmåga, fukt, energi, brandspridning, varsamhet), miniriskmetoden och handlingarna;
Järfälla – lovfritt takbyte och dokumentationen som ägaren nu sparar själv (handlingar arkiveras inte), färg/material/
lutning på kommunens tak-sida, brutna sadeltak med lertegel i Björkliden – Kallhälls villastad;
Tyresö – taksäkerheten för sotaren när taket byts: Södertörns brandförsvarsförbunds krav (glidskydd i takfoten, 4 m,
taksteg, takbrygga, infästningar i bärande delar och läkt), sotningen i Tyresö och lov efter 1 december 2025;
Värmdö – underhåll som ändå kräver anmälan och startbesked (skyddad i plan/särskilt bevarandevärde), lovplikt i
riksintressen och kulturmiljöområden, tegel och plåt i Runmarös byar och takformerna i kulturmiljöprogrammets ordlista;
Österåker – är huset särskilt värdefullt (kommunens frågelista), lov även för underhåll och förvanskningsförbudet,
lertegel kontra betongpannor och återbruk av pannor enligt Råd och vägledning för byggande i Svinninge.

Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-26 (curl -L, Mozilla-UA; pdf via
pdftotext med textlager). Undantag: Skatteverkets två sidor svarade inte på curl (anslutningen återställdes), de
lästes i stället med WebFetch samma dag – uppgifterna citerades ordagrant därifrån.
  Boverket (PBL kunskapsbanken – Bygglov för fasadändring: fasadändring = byte av kulör, fasadbeklädnad eller
  taktäckningsmaterial eller annan påverkan på yttre karaktärsdrag; en- och tvåbostadshus inget lov för byte av
  kulör eller material på fasad eller tak; byte till annat material t.ex. tegeltak till plåttak; samma material och
  utförande är underhåll; antenner, aggregat för ventilation/kyla/värme och solenergi på fasad eller tak kan vara
  fasadändring),
  Nacka kommun (Fasadändringar: inom detaljplan inget lov för en-/tvåbostadshus men får inte strida mot plan, exempel
  byte av färg/material på fasad eller tak, nya fönster/dörrar, antenner, ventilationshuvar eller skorstenar, ingrepp i
  bärande konstruktion kräver anmälan, 8 kap. 13 § PBL utökad lovplikt – lov för samtliga fasadändringar om karaktär
  påverkas, kartan lila = särskilt höga kulturvärden, orange = bedömning kan pågå, kontakta Stadsbyggnadsservice;
  Bygga eldstad eller rökkanal: anmälan för ny eller väsentligt ändrad eldstad (tyngre eldstad, annat bränsle),
  skorsten utanpå fasaden kan kräva bygglov för fasadändring i kulturmiljö, besiktning av sotare, slutbesked innan
  eldstaden används; Nyhet "Nya PBL-regler ger mer frihet – och större ansvar": från 1 december 2025, slopat lov för
  fasadändringar som målning, byte fasadmaterial, solceller, takfönster på en-/tvåbostadshus, krav kvarstår eller
  högre i särskilt värdefulla miljöer, risk för tillsynsärende, många tillsynsanmälningar från grannar, prata med
  grannarna tidigt, webbkartan med detaljplaner och äldre stads- och byggnadsplaner),
  Haninge kommun (Fasadändring: lov om särskilt värdefull byggnad/område, exempel byte av taktäckningsmaterial,
  antenner, solceller; kontrollplan, byggherrens riskanalys, mallar; stora delar av Haninge är kulturmiljöer, kartskiktet
  uppdateras – kontakta bygglovsenheten; frivilligt lov; beskriv med mått, produktblad, foto; Ändring av bärande
  konstruktion: anmälan och startbesked, konstruktör vid osäkerhet, ritningar i bygglovsarkivet, tomtkarta, planritning
  1:100, teknisk beskrivning bl.a. takkonstruktion, konstruktionsritningar av konstruktörer; Exempel kontrollplan
  fasadändring (pdf): punkterna utförande mot beslutsunderlag, bärförmåga vid ökad/omfördelad last (EKS), fukt (BBR
  6:95), energi (BBR 9:91–9:92), brandklass, brandspridning mellan byggnader (BBR 5:611), varsamt (8 kap. 17 § PBL),
  kontrollant E = entreprenör, intyg och underskrift; Exempel riskbedömning (pdf): miniriskmetoden, sannolikhet,
  konsekvens, riskvärde, medelhög risk -> punkt i kontrollplanen),
  Järfälla kommun (Tak: byta takmaterial, ändra färg eller utseende kan vara lovpliktig fasadändring, ändrad lutning/
  höjning t.ex. platt tak till sadeltak oftast tillbyggnad; Fasadändring: inget lov för en-/tvåbostadshus utom i
  särskilt värdefull byggnad/område eller vid utökad lovplikt i plan, ska stämma med plan eller liten avvikelse, anmälan
  om bärande konstruktion påverkas väsentligt, varsamt, frivilligt lov, handlingar situationsplan, planritning,
  fasadritning, kontrollplan, konstruktionsritning; Bygglovsbefriade åtgärder: från 1 december 2025, omfattas av BBR,
  kan kräva anmälan, ägaren ansvarar, dokumentera, spara dokument och ritningar – arkiveras inte längre hos kommunen,
  rätt kompetens, byggherren juridiskt ansvar, frivilligt lov trygghet inför större investering; Kulturmiljöplan för
  Järfälla, Kallhäll (pdf): Björkliden – Kallhälls villastad, tomter för egnahem från 1912, Bolinderarbetare,
  inkorporerat 1955, egnahem i en våning med källare och inredd vind, sadeltak ofta brutna med brant fall, vanligaste
  takmaterialet rött lertegel, traditionella material bytts mot modernare, utökad rådgivning vid bygglov föreslås),
  Tyresö kommun (Sotning och brandskyddskontroll: Södertörns brandförsvarsförbund, Nacka och Tyresö Sotningsdistrikt AB,
  brev eller kort, ringer inte upp, falska sotare; Förändringar i PBL från 1 december 2025: nytt tak utan bygglov för
  en-/tvåbostadshus, varsamt, lov i kulturhistoriskt särskilt värdefullt område/byggnad, anmälan och startbesked om
  konstruktionen berörs, kommunen granskar inte längre många åtgärder),
  Södertörns brandförsvarsförbund (Taksäkerhet: glidskydd för markstege förankrat i fast byggnadsdel i takfoten, inte i
  hängrännan – 150 kg, de flesta fallolyckor i övergången markstege–takstege, under 4 m fasadhöjd utvändig uppgång,
  över 4 m fast fasadstege eller invändig uppgång genom taklucka, bärläktsteg eller takstege till skorsten, takbrygga
  om mer än en meter till skorstenen, lösa taksteg rak linje, normalt för högst 4 m fasadhöjd och under 45 grader,
  fasta takstegar minst 4 infästningspunkter i bärande delar, bärighet för sotare, infästning i läkt kräver läkt i bra
  skick, BBR avsnitt 8:2; Sotning och rengöring: medlemskommuner inkl. Haninge och Tyresö, register, ägarens ansvar,
  roterande undertryckssotning sedan våren 2022 underifrån via eldstad/sotlucka),
  Värmdö kommun (Bygga i kulturmiljöer: förvanskningsförbud oavsett lov, 14 riksintressen och cirka 55
  kulturmiljöområden som räknas som särskilt värdefulla, tänk på bl.a. takets form och lutning, kommunantikvarien,
  anmälan och startbesked för underhåll av byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde,
  ibland strandskyddsdispens/länsstyrelsens tillstånd, byggnadsminnen; Förändringar i PBL från 1 december 2025:
  skärpta krav i riksintressen och kulturhistoriskt värdefulla miljöer, kulturmiljökartan, ägaren ansvarar;
  Kulturmiljöprogram "Värmdö – Kulturhistoria i skärgårdsbygd" (pdf): Runmarö – Uppeby tegelklädda sadeltak, Nore
  parstuga med brutet tak där Strindberg bodde sommaren 1889, Nores tak täckta med tegelpannor, Norrsunda/Södersunda
  tegel dominerande, glasverandor, sjöbodar och båthus tak av tegelpannor eller plåt, Vånö tegel eller plåt;
  ordförklaringar: sadeltak, brutet tak/mansardtak, valmat tak, säteritak, pulpettak, falsat plåttak, takfot,
  takutsprång),
  Österåkers kommun (Kulturhistoriska byggnader, kulturmiljöer: bygglov i särskilt värdefullt område/byggnad även för
  bl.a. fasadändring, underhåll och solpaneler, Österåkerskartan, frågelista – skyddsbestämmelser, kulturmiljöområde,
  inventering/kulturmiljöprogram, tidstypisk karaktär, ursprunglig form och detaljer, byggt före 1920; k = varsamt,
  q = får inte rivas; varsamhetskravet; frivilligt bygglov – fördel vid försäljning; förvanskningsförbudet skärpt från
  1 december 2025; antikvarisk förundersökning eller enklare antikvariskt utlåtande; Råd och vägledning för byggande i
  Svinninge 2008 (pdf): taket husets "femte fasad", lertegelpannor som åldras vackert i stället för betongtegelpannor,
  tegel på alla byggnader från slutet av 1800-talet, nya material sedan 1950-talet, lertegel andas, se över före
  vintern, läckage oftast underlagspapp eller gammal läkt, byt inte allt tegel för ett par trasiga pannor –
  komplettera med begagnade eller nya, grannar kan ha tegel från samma bruk, betongpannor tjockare, tyngre, kulören
  bleks, nya byggnader lertegel, slätplåt eller papp, sedum),
  Skatteverket (Ger arbetet rätt till rotavdrag?: byta och reparera hängrännor och takpannor, byta plåttak, hängrännor
  och stuprör, mura och reparera skorstenar, montera/nedmontera byggnadsställningar, byggstäda – men inte forsla bort
  byggmaterial och skräp, inte kontrollera eldstäder och skorstenar, solceller och grön teknik inte båda; Så fungerar
  rotavdraget: högst 30 procent, 50 000 kr rot, 75 000 kr rot+rut, äga under arbetet, helt eller delvis bo,
  permanentbostad och fritidshus, uthyrd del ger inte avdrag, material och resor ger inte avdrag, flera ägare delar).
Strukna/utelämnade: Nackas automatiserade eldstadsbeslut "inom fem minuter" (handläggningstid – utelämnad);
SBFF:s avgifter och sotningsintervall; vad roterande undertryckssotning betyder för hur ofta sotaren går upp på taket
(står inte – inte skrivet); Haninges avgifter och e-tjänstens detaljer; namnen i Haninges riskexempel; vilket år
Järfällas kulturmiljöplan antogs (står inte i Kallhällsdelen); om Runmarö är riksintresse (programmet säger det inte
i de lästa avsnitten – skrivet som "beskrivs i kulturmiljöprogrammet", kontroll i kartan); Långvik på Runmarö
(byggtorg) – medvetet inte använt; Svinninge-programmets herrgårdsvillor (används av takrenovering-osteraker) – bara
vägledningens takavsnitt används; Österåkers telefontider; BBR-paragrafer i ny numrering efter 2025 (bara som Haninges
mall anger dem). Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
Kritikpass 2026-10-26: varje faktamening kontrollerad mot källtexterna (tb/src, pdftotext; Skatteverket via
WebFetch). Rättat: Nacka – "nytt hål i takstolarna för en huv" -> "takstolar ändras för ett nytt takfönster" (egen
slutsats, mildare); Tyresö – "brandskyddskontrollen och taksäkerheten är ändå kvar som krav" -> förbundets ordalydelse
"en förutsättning för sotning och brandskyddskontroll"; FAQ lösa taksteg – "brantare tak behöver andra lösningar"
(står inte för >45 grader) -> "för högre fasader fast fasadstege eller invändig uppgång"; Tyresös anmälningsmening
gäller i källan tillbyggnad – skriven utan "enligt kommunen" som allmän möjlighet; descriptions Tyresö/Värmdö
kortade (<=155). Kontrollerat utan ändring: 150 kg, 4 m, 45 grader, en meter, fyra infästningspunkter, våren 2022,
1912/1955, 1:100, 14 riksintressen/cirka 55 områden, Strindberg 1889 i Nore, före 1920, k/q, 1950-talet, BBR-punkterna
i Haninges mall, ROT-reglerna. Medvetet "på Värmdö" i H1/title (ortens övriga sidor skriver så).
WARN kvar för v21-sidorna: bara "bild saknas" (bilderna genereras separat).
Kritikpass (strikt) 2026-10-26: alla 21 käll-URL:er öppnade igen (curl -L, Mozilla-UA; Skatteverket svarade
på curl efter omförsök; pdf:er med textlager via pdftotext: Haninges två mallar, Kallhäll, Värmdöprogrammet,
Svinninge). Ändrat: Haninge – lead "De flesta takbyten ... görs utan bygglov" (obelagd andel) -> "kräver normalt
inget bygglov"; kontrollplanen "de flesta punkterna" -> "samtliga punkter" (alla rader har E, även FAQ); miniriskmetoden
"medelhög/hög -> punkt" skrivet som exemplets praxis (text + FAQ). Järfälla – lead "de flesta villaägare" (obelagt)
-> "behövs normalt inget bygglov", "ingen ritning och inget beslut i arkivet" -> kommunens ord "dokument och ritningar
arkiveras inte längre"; alt-text "takkupor" struken (finns inte i bilden). Tyresö – alt-text "hängränna och stuprör"
-> beskriver takstegens nedre ände i takfoten (som prompten). Österåker – "inte för att teglet är slut" struket (står
inte i vägledningen); "Hus i grannskapet är ofta" -> "kan ofta vara" (källans ord); FAQ "betongpannor på äldre hus"
-> "ersätta lertegel med betongpannor"; FAQ "Ofta." (obelagt) -> "Ja, om pannorna är hela." Nacka – FAQ-frågan om orange
markering omformulerad (FEL: dubblett med fasadrenovering-nacka). Kontrollerat utan ändring: Nackas lista (antenner,
ventilationshuvar, skorstenar), eldstad/sotare/slutbesked, lila/orange, grannar/tillsyn, webbkartan; Boverket
(tegel->plåt, samma material = underhåll, antenner/aggregat); Haninge (byte av taktäckningsmaterial, kartskiktet,
konstruktör, bygglovsarkiv, 1:100, mått/produktblad/foto, BBR-punkterna); Järfälla (tak-sidan, två undantag, liten
avvikelse, oftast tillbyggnad, BBR/anmälan, kompetens, frivilligt lov, handlingar, Björkliden 1912/1955/brutna
sadeltak/rött lertegel/utökad rådgivning); SBFF (150 kg, 4 m, en meter, 45 grader, 4 infästningar, läkt i bra skick,
BBR 8:2, våren 2022); Tyresö (Nacka och Tyresö Sotningsdistrikt AB, brev/kort, nytt tak utan lov, varsamt); Värmdö
(anmälan vid underhåll, strandskydd/länsstyrelsen, byggnadsminne, 14/cirka 55, Uppeby/Nore 1889/Norrsunda–
Södersunda/Vånö, ordlistan, komplementhus "garage, förråd och andra mindre byggnader" = Skatteverkets ord);
Österåker (frågelistan, k/q, varsamhetskravet, lov även för underhåll, förvanskningsförbud 1 dec 2025, antikvarisk
förundersökning, frivilligt lov/försäljning, femte fasad, 1800-talets slut, 1950-talet, andas, papp/läkt, vintern,
begagnade pannor, betongpannor tjockare/tyngre/bleks, slätplåt/papp/sedum); ROT-meningarna mot båda Skatteverkssidorna.
Inga priser, garantier, omdömen eller egna uppdrag i orterna. tj_check: 0 FEL, inga WARN för v21-takbyte.
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

_BV_FASAD = ("Boverket – PBL kunskapsbanken: Bygglov för fasadändring",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_NA_FASAD = ("Nacka kommun – Fasadändringar",
             "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/lovfria-atgarder/fasadandringar/")
_NA_ELD = ("Nacka kommun – Bygga eldstad eller rökkanal",
           "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/jag-vill-gora-ansokan-eller-anmalan/bygga-eldstad-eller-rokkanal/")
_NA_PBL = ("Nacka kommun – Nya PBL-regler ger mer frihet och större ansvar för Nackas fastighetsägare",
           "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/nyheter-om-nya-lagandringen/2025/10/nya-pbl-regler-ger-mer-frihet-och-storre-ansvar-for-nackas-fastighetsagare/")
_HA_FASAD = ("Haninge kommun – Fasadändring",
             "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/fasadandring/")
_HA_BAR = ("Haninge kommun – Ändring av bärande konstruktion",
           "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/andring-av-barande-konstruktion/")
_HA_KP = ("Haninge kommun – Exempel kontrollplan fasadändring (pdf)",
          "https://www.haninge.se/493343/contentassets/85064aaf727946da8f0d3ba867ad3daf/exempel-kontrollplan-fasadandring.pdf")
_HA_RISK = ("Haninge kommun – Exempel riskbedömning enligt miniriskmetoden (pdf)",
            "https://www.haninge.se/4904ed/contentassets/85064aaf727946da8f0d3ba867ad3daf/exempel-riskbedomning.pdf")
_JA_TAK = ("Järfälla kommun – Tak",
           "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/vadvilldubyggaellerandra/tak.4.69a1b161151015104f4bd603.html")
_JA_FASAD = ("Järfälla kommun – Fasadändring",
             "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/vadvilldubyggaellerandra/fasadandring.4.1966aa14175c8663c9323310.html")
_JA_BEFR = ("Järfälla kommun – Bygglovsbefriade åtgärder",
            "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/bygglovsbefriadeatgarder.4.a41712119a05132defe8bb3.html")
_JA_KALL = ("Järfälla kommun – Kulturmiljöplan för Järfälla, Kallhäll (pdf)",
            "https://www.jarfalla.se/download/18.68e7a727168e12dd179a407f/1550245859848/kulturmiljoplan-kallhall.pdf")
_TY_SOT = ("Tyresö kommun – Sotning och brandskyddskontroll",
           "https://www.tyreso.se/boende--miljo/bygga/sotning-och-brandskyddskontroll.html")
_TY_PBL = ("Tyresö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
           "https://www.tyreso.se/boende--miljo/bygga/bygga-riva-eller-andra/forandringar-i-plan--och-bygglagen-fran-1-december-2025.html")
_SBFF_TAK = ("Södertörns brandförsvarsförbund – Taksäkerhet",
             "https://www.sbff.se/hem--fritid/sotning-och-brandskyddskontroll/taksakerhet/")
_SBFF_SOT = ("Södertörns brandförsvarsförbund – Sotning och rengöring",
             "https://www.sbff.se/hem--fritid/sotning-och-brandskyddskontroll/sotning-och-rengoring/")
_VD_KM = ("Värmdö kommun – Bygga i kulturmiljöer",
          "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/byggaikulturmiljoer.4.57b4a3ba16e6b961dbf10429.html")
_VD_PBL = ("Värmdö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
           "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/forandringaripblfrom1december2025.4.18b9914519a768a188a2872.html")
_VD_KMP = ("Värmdö kommun och Stockholms läns museum – Värmdö: Kulturhistoria i skärgårdsbygd (pdf)",
           "https://www.varmdo.se/download/18.7faa473e19913ae5e0f1f12/1757318877718/Kulturmilj%C3%B6v%C3%A5rdsprogrammet%20V%C3%A4rmd%C3%B6_2.pdf")
_OS_KM = ("Österåkers kommun – Kulturhistoriska byggnader, kulturmiljöer",
          "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/bygglovsguiden/kulturhistoriskabyggnaderkulturmiljoer.4.367d658917909e8fc2bb42.html")
_OS_RAD = ("Österåkers kommun – Råd och vägledning för byggande i Svinninge (pdf)",
           "https://www.osteraker.se/download/18.5bb0400617c11d33b5536/1632390824156/rad_och_vagledning_svinninge.pdf")

_IMG_END = ", realistic photo, no people, no text, no letters"

PAGES_TJ = {

# ------------------------------------------------------------------ NACKA
"takbyte-nacka.html": {
  "kind": "district", "service": "takbyte", "ort": "Nacka", "svc_label": "Takbyte",
  "title": "Takbyte i Nacka – skorsten, huvar och grannar",
  "description": "Takbyte i Nacka: skorsten, ventilationshuvar och antenner som fasadändring, eldstad och anmälan, kulturmiljökartan och grannarna efter 1 december 2025.",
  "h1": "Takbyte i Nacka",
  "lead": "När ett tak byts i Nacka är pannorna sällan det svåra. Det är allt som går genom taket – skorstenen, ventilationshuvarna, antennen och takfönstren – som avgör vad som behöver stämmas av innan arbetet börjar. Geal Entreprenad AB byter tak på villor och radhus i hela Nacka och går igenom varje genomföring vid ett gratis platsbesök.",
  "card": "Skorsten, huvar och genomföringar vid nytt tak.",
  "sections": [
    {"id": "genomforingar-nacka", "anchor": "Genom taket",
     "h2": "Det som sticker upp genom taket räknas också",
     "paras": [
       "Nacka kommun listar vad som räknas som fasadändring, och där står inte bara byte av färg eller material på fasad eller tak. Även antenner, ventilationshuvar och skorstenar finns med, liksom nya fönster och dörrar. Boverket skriver på samma sätt att antenner, solenergianläggningar och aggregat för ventilation, kyla och värme kan räknas som fasadändring när de monteras, flyttas eller ändras på ett tak.",
       "Inom detaljplan krävs inte längre bygglov för fasadändringar på ett en- eller tvåbostadshus, men åtgärden får inte strida mot detaljplanen. Kommunen påpekar också att ett ingrepp i den bärande konstruktionen kräver en anmälan. Det kan bli aktuellt om en murstock ska tas bort eller om takstolar behöver ändras för ett nytt takfönster. Därför går vi igenom varje genomföring innan nya pannor beställs, och skriver in i kostnadsförslaget vad som flyttas, tas bort eller blir kvar.",
     ],
     "aside": {"title": "Fasadändring enligt Nacka", "items": [
       "Färg eller material på tak", "Ventilationshuvar", "Antenner", "Skorstenar"]}},
    {"id": "skorsten-nacka", "h2": "Skorstenen och eldstaden när taket ändå är öppet",
     "paras": [
       "Ett takbyte är ett naturligt tillfälle att bestämma vad som ska hända med skorstenen. Plåten runt den görs om när pannorna byts, och krönet kan lagas medan ställningen står. Planerar du samtidigt en ny eldstad gäller andra regler. Nacka kommun skriver att en anmälan ska göras för att installera en ny eldstad eller väsentligt ändra en befintlig, till exempel genom att sätta in en tyngre eldstad eller byta bränsleslag. En skorsten som byggs utanpå fasaden kan dessutom kräva bygglov för fasadändring om huset ligger i en kulturmiljö.",
       "När en ny eldstad är installerad ska den besiktigas av en sotare, och kommunen ger slutbesked innan den får användas. Vi samordnar takarbetet så att skorstenen är klar och tätt inplåtad innan eldstaden tas i bruk. Skatteverket räknar att mura och reparera skorstenar på ett småhus som rotarbete, men inte att kontrollera eldstäder och skorstenar. Mer om lagning och omputsning finns under " + _L.format("skorstensrenovering.html", "skorstensrenovering") + ".",
     ],
     "aside": None},
    {"id": "kulturmiljo-nacka", "h2": "Lila eller orange i kartan – då gäller andra regler",
     "paras": [
       "För fastigheter som ligger i ett område som är särskilt värdefullt enligt 8 kap. 13 § plan- och bygglagen utökas bygglovsplikten. Kommunen skriver att bygglov då krävs för samtliga fasadändringar på fastigheten om områdets karaktär eller byggnadens yttre karaktärsdrag påverkas. Ett nytt takmaterial, en ny huv på gatusidan eller en borttagen skorsten kan alltså bli en lovfråga.",
       "I kommunens karta visar lila markering byggnader och områden med särskilt höga kulturvärden. Orange markering betyder att det kan pågå ett arbete med att bedöma de kulturhistoriska värdena, och då hänvisar kommunen till Stadsbyggnadsservice. Om husens historia och takens epoker i kommunen kan du läsa under " + _L.format("takrenovering-nacka.html", "takrenovering i Nacka") + ", och om plåttak nära farleden under " + _L.format("platslagare-nacka.html", "plåtslagare i Nacka") + ".",
     ],
     "aside": {"title": "Kartans markeringar", "items": [
       "Lila – särskilt höga kulturvärden", "Orange – bedömning kan pågå",
       "Ingen markering – detaljplanen styr"]}},
    {"id": "grannar-nacka", "h2": "Prata med grannarna innan ställningen kommer",
     "paras": [
       "Inför lagändringen den 1 december 2025 skrev kommunen att fler åtgärder får göras utan bygglov, men att ansvaret för att veta vad som gäller hamnar hos fastighetsägaren. Om något byggs felaktigt är risken stor att det blir ett tillsynsärende, och kundrådgivarna på Stadsbyggnadsservice berättar att många tillsynsanmälningar kommer från grannar som inte känt till vad som skulle göras. Deras råd är att vara påläst, ha god framförhållning och prata med grannarna tidigt.",
       "Ett takbyte märks på tomterna runt omkring. Ställningen kan behöva stå nära tomtgränsen, och gammalt tegel och papp ska fraktas bort. Vi går igenom placeringen vid platsbesöket så att du kan berätta för grannarna vad som händer och hur länge. I kommunens webbkarta finns både gällande detaljplaner och äldre stads- och byggnadsplaner, och den är ett bra första steg. Vad vi gör i övrigt i kommunen finns under " + _L.format("taklaggare-nacka.html", "takläggare i Nacka") + ", och hur ett byte går till i stort under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Nacka till",
  "steps": [
    ("Platsbesök", "Vi går igenom tak, vind och varje genomföring: skorsten, huvar, antenn och takfönster."),
    ("Karta och plan", "Detaljplanen och kommunens kulturmiljökarta kontrolleras för fastigheten."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, pannor, plåt och genomföringar står var för sig."),
    ("Etablering", "Ställning och container placeras som vi har gått igenom med dig."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs med ny plåt kring genomföringarna."),
    ("Genomgång", "Vi går igenom taket, skorstensplåten och huvarna tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Nacka",
  "rot": [
    "Enligt Skatteverket ger det rotavdrag att byta takpannor, plåttak, hängrännor och stuprör på ett småhus, liksom att mura och reparera skorstenar, sätta upp och ta ner byggnadsställningen och byggstäda efteråt. Att forsla bort byggmaterial och skräp ger däremot inget avdrag.",
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor räknas inte. Du ska äga huset när arbetet görs. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för takbytet i Nacka?",
  "price": [
    "Takets yta och lutning, materialet, hur många genomföringar som ska plåtas in eller flyttas, skorstenens skick, hur mycket råspont som behöver bytas och hur ställningen kan stå på en tomt med berg eller nivåskillnader. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Räknas en ny ventilationshuv på taket som en fasadändring i Nacka?",
     "Ja. Nacka kommun nämner ventilationshuvar, antenner och skorstenar bland exemplen på fasadändringar. På ett en- eller tvåbostadshus inom detaljplan krävs normalt inget lov, men planen ska följas."),
    ("Kan vi ta bort skorstenen ovanför taket när taket byts?",
     "Det kan gå, men skorstenar räknas som fasadändring, och ett ingrepp i den bärande konstruktionen kräver anmälan. I ett särskilt värdefullt område kan bygglov krävas."),
    ("Måste en ny kamin vara klar innan taket läggs om?",
     "Nej, men en ny eldstad kräver anmälan, besiktning av sotare och slutbesked innan den används. Det är praktiskt att plåta in skorstenen i samma veva som taket."),
    ("Vad innebär en orange markering i kartan för ett takbyte i Nacka?",
     "Att det kan pågå ett arbete med att bedöma de kulturhistoriska värdena. Kommunen hänvisar då till Stadsbyggnadsservice för besked."),
    ("Varför ska vi prata med grannarna före ett lovfritt takbyte?",
     "Enligt Nacka kommun kommer många tillsynsanmälningar från grannar som inte vetat vad som skulle göras. Ett samtal i förväg kan undvika det."),
  ],
  "sources": [_NA_FASAD, _NA_ELD, _NA_PBL, _BV_FASAD, _SKV, _SKV2],
  "cta": ("Ska taket i Nacka bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och alla genomföringar innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa i Nacka med nylagt tak av röda tegelpannor, murad skorsten och ventilationshuv bland tallar",
     "Swedish two-storey villa on a rocky plot among pine trees, newly laid red clay tile roof with a plastered brick chimney with new black metal flashing and a small black ventilation cap on the roof slope, scaffolding still standing along one side, late summer daylight" + _IMG_END),
    ("Murad skorsten med ny svart plåtinfästning mot nya tegelpannor på ett villatak",
     "close-up of a plastered brick chimney on a pitched roof with new black sheet metal flashing neatly fitted against fresh red clay roof tiles, a roof ladder section beside it, clear blue sky" + _IMG_END),
    ("Takfall med ny ventilationshuv, takfönster och antennfäste på ett nylagt betongpannetak",
     "pitched roof of a Swedish villa covered with new dark grey concrete roof tiles, a black ventilation cap, a roof window with metal flashing and a small antenna mast bracket, all neatly sealed, overcast daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HANINGE
"takbyte-haninge.html": {
  "kind": "district", "service": "takbyte", "ort": "Haninge", "svc_label": "Takbyte",
  "title": "Takbyte i Haninge – kontrollplan och riskbedömning",
  "description": "Takbyte i Haninge: när nytt tak kräver lov eller anmälan, kommunens kontrollplan och riskbedömning punkt för punkt och vilka handlingar som behövs.",
  "h1": "Takbyte i Haninge",
  "lead": "Ett takbyte på en villa i Haninge kräver normalt inget bygglov. Men när huset ligger i en värdefull miljö, eller när det nya taket påverkar bärande delar, behöver kommunen en kontrollplan. Geal Entreprenad AB byter tak i hela Haninge och hjälper dig att ta fram underlaget när ett ärende krävs.",
  "card": "Kontrollplan och riskbedömning vid takbyte.",
  "sections": [
    {"id": "arende-haninge", "anchor": "Lov eller anmälan",
     "h2": "När ett takbyte blir ett ärende hos kommunen",
     "paras": [
       "Haninge kommun nämner byte av fasadbeklädnad eller taktäckningsmaterial som exempel på fasadändring. På ett en- eller tvåbostadshus krävs normalt inget lov för det, men lov behövs om ändringen görs på en byggnad eller i ett område som är särskilt värdefullt. Kommunen skriver att stora delar av Haninge är kulturmiljöer och att skärpta krav gäller i särskilt värdefulla områden och riksintressen. Kartskiktet som visar de miljöerna håller på att uppdateras, och tills det är klart kan bygglovsenheten svara på om en fastighet omfattas.",
       "En anmälan behövs om arbetet påverkar byggnadens bärande konstruktion, och då krävs startbesked innan arbetet börjar. Det kan gälla när takstolar förstärks för ett tyngre material eller när en bärande del byts. Är du osäker på om en del är bärande hänvisar kommunen till en konstruktör, och ritningar som visar husets bärande delar kan ibland finnas i bygglovsarkivet. Du har också rätt att få åtgärden prövad i ett frivilligt lov.",
     ],
     "aside": {"title": "Ärende kan krävas när", "items": [
       "Huset eller området är särskilt värdefullt", "Takstolar förstärks eller byts",
       "Ett tyngre material läggs på", "Du vill ha ett frivilligt lov"]}},
    {"id": "kontrollplan-haninge", "h2": "Kontrollplanen punkt för punkt",
     "paras": [
       "Haninge har lagt ut ett exempel på en kontrollplan för fasadändring av en- och tvåbostadshus. Där finns punkter som passar ett takbyte väl: att utförandet stämmer med beslutsunderlaget, att befintliga konstruktioner har tillräcklig bärförmåga vid ökad eller omfördelad last, skydd mot fukt i byggnadskonstruktionen, att byggnadens energieffektivitet inte försämras, skydd mot brandspridning mellan byggnader och att utförandet görs varsamt enligt 8 kap. 17 § plan- och bygglagen.",
       "För varje punkt anges vem som kontrollerar, hur det görs och mot vilket underlag. I exemplet står entreprenören som kontrollant för samtliga punkter, och den som har utfört kontrollen skriver under. När vi byter taket kontrollerar vi de punkter som gäller själva takarbetet, till exempel att underlag och infästningar görs enligt ritningen. Bärförmågan bedöms av en konstruktör när lasten ökar.",
     ],
     "aside": {"title": "Ur kommunens exempel", "items": [
       "Bärförmåga vid ökad last", "Skydd mot fukt",
       "Brandspridning mellan byggnader", "Varsamt utförande"]}},
    {"id": "risk-haninge", "h2": "Riskbedömningen som ligger bakom",
     "paras": [
       "Kommunen påpekar att du som byggherre är ansvarig för att göra en riskanalys för projektet och att utifrån den ta fram kontrollplanen. Exemplet använder miniriskmetoden. Varje identifierad risk får ett värde för sannolikhet och ett för konsekvens, och tillsammans ger de ett riskvärde. När en risk i exemplet bedöms som medelhög eller hög läggs en punkt till i kontrollplanen.",
       "För ett takbyte kan det handla om risken att vatten kommer in medan taket är öppet, att ett tyngre material belastar takstolarna mer än beräknat eller att ett takfall närmare än vanligt intill en grannbyggnad kräver hänsyn till brandspridning. Vi går igenom sådana risker vid platsbesöket, så att du har ett underlag till riskbedömningen innan kontrollplanen skrivs.",
     ],
     "aside": None},
    {"id": "handlingar-haninge", "h2": "Handlingarna till ansökan eller anmälan",
     "paras": [
       "Vid en anmälan om ändring i bärande konstruktion tar Haninge upp en tomtkarta där byggnaden är markerad, en planritning i skala 1:100 och en teknisk beskrivning av bland annat bärande stomme och takkonstruktion. Konstruktionsritningar ska tas fram av konstruktörer, och vid större projekt kan även konstruktionsdokumentation och dimensioneringskontroll krävas. Till en fasadändring hör också en markering på tomtkartan av den byggnad som berörs.",
       "Är du osäker på vad som gäller ber kommunen dig beskriva vad du planerar med mått, produktblad och gärna ett fotografi. Produktbladen för pannor, underlag och plåt får du av oss tillsammans med det skriftliga kostnadsförslaget. Om husens epoker och takformer i kommunen kan du läsa under " + _L.format("takrenovering-haninge.html", "takrenovering i Haninge") + ", om falsad plåt och brutna tak under " + _L.format("platslagare-haninge.html", "plåtslagare i Haninge") + " och om våra tjänster i stort under " + _L.format("taklaggare-haninge.html", "takläggare i Haninge") + ".",
     ],
     "aside": {"title": "Vid anmälan", "items": [
       "Tomtkarta med markerad byggnad", "Planritning 1:100",
       "Teknisk beskrivning", "Konstruktionsritningar"]}},
  ],
  "steps_h2": "Så går ett takbyte i Haninge till",
  "steps": [
    ("Platsbesök", "Vi bedömer tak, takstolar och vind och ser om det nya materialet ändrar lasten."),
    ("Lovfrågan", "Vi går igenom om huset ligger i en värdefull miljö och om en anmälan behövs."),
    ("Underlag", "Produktblad och beskrivning av arbetet till riskbedömning och kontrollplan."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt, plåt och ställning står var för sig."),
    ("Takbyte", "Taket läggs enligt underlaget, och våra kontrollpunkter signeras under arbetet."),
    ("Genomgång", "Vi går igenom taket och den ifyllda kontrollplanen med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Haninge",
  "rot": [
    "Att byta takpannor, plåttak, hängrännor och stuprör på ett småhus är rotarbete enligt Skatteverket. Det gäller även ställningsarbetet och byggstädningen efter takbytet, men inte bortforsling av byggmaterial och skräp.",
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Är ni flera ägare som bor i huset kan ni dela på avdraget. Geal drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för takbytet i Haninge?",
  "price": [
    "Takets yta och lutning, valet av material, om takstolarna behöver förstärkas, hur mycket underlag som ska bytas, plåtarbetena och om ett ärende hos kommunen kräver extra underlag eller kontroller. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem skriver under kontrollplanen när taket byts i Haninge?",
     "Den som utför kontrollen för respektive punkt skriver under. I kommunens exempel är entreprenören kontrollant för samtliga punkter, och byggherren intygar att planen har följts."),
    ("Vad är miniriskmetoden i en riskbedömning?",
     "Varje risk får ett värde för sannolikhet och ett för konsekvens, som tillsammans ger ett riskvärde. I Haninges exempel får risker som bedöms som medelhöga eller höga en egen punkt i kontrollplanen."),
    ("Hur vet vi om villan i Haninge ligger i en särskilt värdefull miljö?",
     "Kommunen uppdaterar kartskiktet över värdefulla kulturmiljöer. Tills det är klart kan bygglovsenheten svara på om fastigheten omfattas."),
    ("Behövs konstruktionsritningar om takstolarna förstärks?",
     "Ja, vid en anmälan om ändring i bärande konstruktion ska konstruktionsritningar lämnas in, och de ska tas fram av konstruktörer."),
    ("Kan vi lämna in produktblad för att få besked om lov för nytt takmaterial?",
     "Haninge kommun ber den som är osäker att beskriva åtgärden med mått, produktblad och gärna ett fotografi, så blir det lättare att bedöma om lov behövs."),
  ],
  "sources": [_HA_FASAD, _HA_BAR, _HA_KP, _HA_RISK, _SKV, _SKV2],
  "cta": ("Ska taket i Haninge bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och vad kommunen kan behöva innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa i Haninge med nytt tak av svarta betongpannor och nya hängrännor en klar höstdag",
     "Swedish 1970s one-storey villa with a newly laid black concrete tile gable roof, new black gutters and downpipes, light wooden facade, birch trees and a lawn, clear autumn day" + _IMG_END),
    ("Svarta betongpannor läggs på läkt, halva takfallet klart",
     "roof replacement in progress on a Swedish house: visible wooden roof trusses, new tongue and groove roof boarding partly covered with black underlay felt and fresh pale battens, stacks of new roof tiles on the scaffolding, no workers, overcast daylight" + _IMG_END),
    ("Förstärkta takstolar på en kallvind med nya reglar bredvid de gamla",
     "interior of a cold attic in a Swedish villa with old wooden roof trusses reinforced by new pale timber members bolted alongside them, mineral wool insulation on the floor, daylight from a small gable window" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"takbyte-jarfalla.html": {
  "kind": "district", "service": "takbyte", "ort": "Järfälla", "svc_label": "Takbyte",
  "title": "Takbyte i Järfälla – lovfritt men dokumenterat",
  "description": "Takbyte i Järfälla: nytt material, ny färg eller ny lutning, vad du ska spara när taket byts utan lov och brutna tegeltak i Kallhälls villastad.",
  "h1": "Takbyte i Järfälla",
  "lead": "Sedan den 1 december 2025 behövs normalt inget bygglov för att byta taket på en villa i Järfälla. Det betyder också att dokument och ritningar inte längre arkiveras hos kommunen. Geal Entreprenad AB byter tak i hela Järfälla och ser till att du har papperen på vad som gjordes.",
  "card": "Lovfritt takbyte och papperen du sparar.",
  "sections": [
    {"id": "material-farg-jarfalla", "anchor": "Material, färg, form",
     "h2": "Nytt material, ny färg eller ny takform",
     "paras": [
       "Järfälla kommun skriver att det kan vara en lovpliktig fasadändring att byta takmaterial, ändra färg på taket eller på annat sätt ändra takets utseende. För ett en- eller tvåbostadshus krävs ändå inget bygglov för en fasadändring, med två undantag: om huset eller området är särskilt värdefullt, eller om detaljplanen har en utökad lovplikt. Ändringen ska dessutom stämma med detaljplanen eller vara en liten avvikelse som inte motverkar planens syfte.",
       "Takformen är en annan sak. Kommunen skriver att den som vill ändra lutningen eller höja taket, till exempel byta från platt tak till sadeltak, oftast gör en tillbyggnad eftersom byggnadens volym ändras. Ett takbyte med samma form och lutning är alltså en enklare fråga än ett byte där taket samtidigt byggs om. En anmälan behövs om bärande konstruktion påverkas väsentligt.",
     ],
     "aside": {"title": "Enligt kommunen", "items": [
       "Nytt material – kan vara fasadändring", "Ny färg på taket – kan vara fasadändring",
       "Ny lutning eller höjning – oftast tillbyggnad", "Bärande delar – anmälan"]}},
    {"id": "dokumentation-jarfalla", "h2": "Inget lov – men papperen sparar du själv",
     "paras": [
       "På sidan om bygglovsbefriade åtgärder påminner kommunen om att sådana åtgärder fortfarande omfattas av Boverkets byggregler och kan kräva anmälan. Som fastighetsägare ansvarar du själv för att reglerna följs. Kommunen uppmanar därför till att dokumentera hur kraven uppfylls och att spara alla dokument och ritningar, eftersom de vid bygglovsbefriade åtgärder inte längre arkiveras hos kommunen.",
       "För ett tak betyder det en pärm eller mapp med det skriftliga kostnadsförslaget, produktbladen för pannor eller plåt, underlagspapp och läkt, fotografier av råsponten innan den täcktes och en beskrivning av vad som byttes. Vill du sälja huset om några år kan just det vara svaret på frågan om när taket lades och hur. Kommunen skriver också att du ska försäkra dig om att den du anlitar har rätt kompetens, eftersom du som byggherre har det juridiska ansvaret.",
     ],
     "aside": {"title": "Spara efter takbytet", "items": [
       "Skriftligt kostnadsförslag", "Produktblad för material",
       "Foton av underlaget", "Beskrivning av arbetet"]}},
    {"id": "frivilligt-jarfalla", "h2": "Frivilligt lov som trygghet",
     "paras": [
       "För alla bygglovsbefriade åtgärder går det att söka ett frivilligt bygglov. Järfälla kommun beskriver det som en trygghet inför en större investering, och ett sätt att säkerställa att det som byggs följer regler, krav och detaljplan. För ett tak kan det vara värt att överväga när materialet byts mot något helt annat eller när huset ligger i ett område där du är osäker på planens bestämmelser.",
       "Söker du lov ska ansökan enligt kommunen innehålla en situationsplan, en planritning, en fasadritning där ändringen är markerad och ett förslag till kontrollplan. Påverkas den bärande konstruktionen krävs också en konstruktionsritning. Vi tar fram uppgifterna om material, kulör och utförande som ritningen och kontrollplanen behöver.",
     ],
     "aside": None},
    {"id": "bjorkliden-jarfalla", "h2": "Brutna tegeltak i Kallhälls villastad",
     "paras": [
       "Kulturmiljöplanens del om Kallhäll beskriver Björkliden, där tomter för egnahem började styckas av 1912. Området lockade Bolinderarbetare som ville bygga eget, och det blev en del av Järfälla först 1955. Husen är egnahem med enkel utformning, vanligen i en våning med källare och inredd vind. Taken är sadeltak, ofta brutna, med brant fall, och det vanligaste takmaterialet är rött lertegel.",
       "Planen noterar att flera egnahem har förändrats genom att traditionella material och färger bytts ut mot modernare, och föreslår utökad rådgivning vid bygglovsansökningar för att behålla traditionella material. Ett brutet tak har två lutningar på varje sida, och brytlinjen behöver egen plåt och omsorg när underlaget läggs. Om lertegeltak och radhuslängor i kommunen kan du läsa under " + _L.format("takrenovering-jarfalla.html", "takrenovering i Järfälla") + ", om takvatten under " + _L.format("platslagare-jarfalla.html", "plåtslagare i Järfälla") + " och om våra tjänster under " + _L.format("taklaggare-jarfalla.html", "takläggare i Järfälla") + ".",
     ],
     "aside": {"title": "Björkliden enligt planen", "items": [
       "Egnahem från 1912", "En våning och inredd vind",
       "Brutna sadeltak med brant fall", "Rött lertegel vanligast"]}},
  ],
  "steps_h2": "Så går ett takbyte i Järfälla till",
  "steps": [
    ("Platsbesök", "Vi bedömer taket, vinden och takformen och noterar material och kulör."),
    ("Plan och lov", "Detaljplanen kontrolleras, och vi går igenom om ett frivilligt lov är värt att söka."),
    ("Skriftligt kostnadsförslag", "Material, underlag och arbetsmoment beskrivs så att det kan sparas."),
    ("Takbyte", "Gammalt tak rivs, råsponten fotograferas och nytt underlag, läkt och tak läggs."),
    ("Plåt och avvattning", "Brytlinjer, skorsten och takfot plåtas, och rännorna ses över."),
    ("Överlämning", "Du får produktblad, foton och en beskrivning av vad som gjordes."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Järfälla",
  "rot": [
    "Skatteverket räknar byte av takpannor, plåttak, hängrännor och stuprör på ett småhus som rotarbete, och även att montera och montera ner byggnadsställningen och att byggstäda efter arbetet. Du behöver äga huset medan arbetet utförs och helt eller delvis bo i det.",
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material, resor och bortforsling ger inget avdrag. Geal drar ROT direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för takbytet i Järfälla?",
  "price": [
    "Takets yta, om taket är brutet eller rakt, valet av material, hur mycket råspont och läkt som behöver bytas, plåtarbetena och om du vill söka frivilligt lov med ritningar. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Sparar Järfälla kommun handlingarna när taket byts utan bygglov?",
     "Nej. Kommunen skriver att dokument och ritningar för bygglovsbefriade åtgärder inte längre arkiveras hos kommunen, så du behöver spara dem själv."),
    ("Är det en tillbyggnad att göra om ett platt tak till sadeltak i Järfälla?",
     "Oftast ja, enligt kommunen, eftersom byggnadens volym ändras när lutningen ändras eller taket höjs."),
    ("Behöver vi lov för att byta till en annan färg på taket?",
     "På ett en- eller tvåbostadshus normalt inte, men lov krävs om huset eller området är särskilt värdefullt eller om detaljplanen har utökad lovplikt."),
    ("Vad ska vi spara efter ett lovfritt takbyte?",
     "Kostnadsförslaget, produktblad för material, foton av underlaget och en beskrivning av arbetet. Kommunen uppmanar ägaren att dokumentera hur reglerna uppfylls."),
    ("Vilket takmaterial är vanligast på egnahemmen i Björkliden?",
     "Enligt Järfällas kulturmiljöplan är rött lertegel det vanligaste, och taken är ofta brutna sadeltak med brant fall."),
  ],
  "sources": [_JA_TAK, _JA_FASAD, _JA_BEFR, _JA_KALL, _BV_FASAD, _SKV, _SKV2],
  "cta": ("Ska taket i Järfälla bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och vad du bör spara innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Egnahem med brutet tak av rött lertegel och ljus träpanel i en lummig villastad",
     "small Swedish one-and-a-half-storey wooden house from the 1920s with a mansard gambrel roof: each roof side has a steep lower slope and a gentle upper slope with a clear break line, covered in red clay tiles, light grey vertical board facade, white window frames, mature fruit trees and lilac bushes in the garden, narrow road without pavement, summer daylight" + _IMG_END),
    ("Läktat tak i hela längden inför pannläggning",
     "close-up of the break line on a gambrel roof under replacement: lower steep slope with new black underlay felt and pale battens, a new metal flashing strip along the break line, upper slope already covered with new red clay tiles, overcast daylight" + _IMG_END),
    ("Nytt underlag, läkt och lertegel framlagt på byggnadsställningen innan taket läggs om",
     "scaffolding platform along the eaves of a Swedish wooden house with a roll of black roof underlay, a bundle of pale wooden battens and stacked new red clay roof tiles, the roof deck behind half covered with new underlay, overcast daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ TYRESÖ
"takbyte-tyreso.html": {
  "kind": "district", "service": "takbyte", "ort": "Tyresö", "svc_label": "Takbyte",
  "title": "Takbyte i Tyresö – taksäkerhet för sotaren",
  "description": "Takbyte i Tyresö: glidskydd, takstege och takbrygga enligt Södertörns brandförsvarsförbund, sotningen i kommunen och lov efter 1 december 2025.",
  "h1": "Takbyte i Tyresö",
  "lead": "Ett nytt tak ska inte bara hålla tätt. Har huset en eldstad ska sotaren och brandskyddskontrollanten också kunna ta sig upp på ett säkert sätt. Geal Entreprenad AB byter tak i hela Tyresö och planerar taksäkerheten samtidigt som det nya taket läggs.",
  "card": "Nytt tak med säker väg till skorstenen.",
  "sections": [
    {"id": "glidskydd-tyreso", "anchor": "Taksäkerhet",
     "h2": "Glidskyddet sitter i takfoten – inte i rännan",
     "paras": [
       "Tyresö ingår i Södertörns brandförsvarsförbund, som sköter sotning och brandskyddskontroll åt kommunen. Förbundet kallar taksäkerheten en förutsättning för sotning och brandskyddskontroll. Om uppgången sker utvändigt, med en lös markstege och sedan en takstege på taket, behöver det finnas ett glidskydd att fästa markstegen i så att den inte kan glida åt sidan eller bakåt.",
       "Glidskyddet ska vara förankrat i en fast byggnadsdel i takfoten och inte i hängrännan, eftersom rännan ofta inte klarar hållfasthetskravet på 150 kg. Förbundet skriver att de flesta fallolyckor sker i övergången mellan markstege och takstege. När takfoten ändå är frilagd vid ett takbyte är det rätt tillfälle att förankra glidskyddet ordentligt.",
     ],
     "aside": {"title": "Glidskyddet", "items": [
       "Förankrat i fast byggnadsdel", "I takfoten, inte i rännan",
       "Ska klara 150 kg", "Där de flesta fallolyckor sker"]}},
    {"id": "uppgang-tyreso", "h2": "Utvändig eller invändig väg upp",
     "paras": [
       "Fasadhöjden avgör vilken uppgång som passar. Enligt förbundet kan en utvändig uppgång användas när höjden från marken till takfoten är mindre än 4 meter. Är den högre bör det finnas en fast förankrad fasadstege eller en invändig uppgång genom en taklucka. Vid utvändig uppgång ska det efter markstege och glidskydd finnas bärläktsteg eller en takstege fram till skorstenen. Vid invändig uppgång ska det finnas en takbrygga fram till skorstenen om avståndet är över en meter.",
       "Lösa taksteg ska installeras enligt tillverkarens instruktioner och följa en rak linje. Förbundet skriver att de generellt är godkända för hus med en fasadhöjd på högst 4 meter och taklutningar under 45 grader. Fasta takstegar ska ha minst fyra infästningspunkter i bärande byggnadsdelar, upptill och nedtill. Mer om stegar och snörasskydd finns under " + _L.format("taksakerhet-snorasskydd.html", "taksäkerhet och snörasskydd") + ".",
     ],
     "aside": None},
    {"id": "lakt-tyreso", "h2": "Ny läkt ger fäste för nya taksteg",
     "paras": [
       "Taksäkerheten måste bära tyngden av sotare och brandskyddskontrollanter, och infästningarna ska följa tillverkarnas monteringsanvisningar. Förbundet påpekar att takläkten måste vara i bra skick om takskydd monteras i den. På ett gammalt tak är det svårt att veta hur läkten under pannorna mår. Vid ett takbyte läggs ny läkt, och placeringen av taksteg, takbrygga och glidskydd kan planeras innan pannorna läggs på.",
       "Förbundet hänvisar till kraven på skydd mot fall i Boverkets byggregler. Sedan våren 2022 sotas eldstäder i förbundets kommuner med roterande undertryckssotning, där verktyget förs in i skorstenen underifrån via eldstaden eller sotluckan i stället för ovanifrån taket. Förbundet beskriver ändå taksäkerheten som en förutsättning för både sotning och brandskyddskontroll. Om takens historia i kommunen kan du läsa under " + _L.format("takrenovering-tyreso.html", "takrenovering i Tyresö") + ".",
     ],
     "aside": {"title": "Planeras före pannorna", "items": [
       "Taksteg i rak linje", "Takbrygga vid behov",
       "Glidskydd i takfoten", "Infästning i ny läkt"]}},
    {"id": "sotning-lov-tyreso", "h2": "Sotningen i Tyresö och lovfrågan",
     "paras": [
       "Enligt Tyresö kommun är det Nacka och Tyresö Sotningsdistrikt AB som sotar i kommunen. När det är dags får du ett brev eller ett kort med datum och tid, och kommunen varnar för personer som ringer och säger att de kommer från kommunen för sotning. Hos varje sotningsentreprenör finns ett register över vilka eldstäder som finns i distriktet och när de senast sotades och kontrollerades, och förbundet påminner om att fastighetsägaren ansvarar för att eldstaden finns med där. Har du fått nytt tak kan det vara bra att berätta det vid nästa besök.",
       "Ett nytt tak kräver inte bygglov på ett en- eller tvåbostadshus, skriver kommunen, men ändringen ska göras varsamt. Ligger fastigheten i ett kulturhistoriskt särskilt värdefullt område, eller är byggnaden själv särskilt värdefull, krävs bygglov. Berörs konstruktionen kan det krävas anmälan och startbesked. Om stuprör och rännor finns mer under " + _L.format("platslagare-tyreso.html", "plåtslagare i Tyresö") + " och om våra tjänster under " + _L.format("taklaggare-tyreso.html", "takläggare i Tyresö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Tyresö till",
  "steps": [
    ("Platsbesök", "Vi mäter fasadhöjd och taklutning och tittar på skorstenen och dagens taksäkerhet."),
    ("Regler och plan", "Vi kontrollerar om fastigheten ligger i en särskilt värdefull miljö."),
    ("Skriftligt kostnadsförslag", "Tak, underlag, plåt och taksäkerhet står var för sig."),
    ("Rivning och underlag", "Gammalt tak rivs, råsponten ses över och nytt underlag och ny läkt läggs."),
    ("Nytt tak och taksäkerhet", "Pannor eller plåt läggs, och glidskydd, taksteg och takbrygga monteras."),
    ("Genomgång", "Vi går igenom taket och vägen upp till skorstenen med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Tyresö",
  "rot": [
    "Skatteverket räknar byte av takpannor, plåttak, hängrännor och stuprör på ett småhus som rotarbete, liksom att sätta upp och ta ner byggnadsställningen. Rotavdrag ges för arbete i både permanentbostad och fritidshus som du äger och bor i, helt eller delvis. Den del av huset som du hyr ut ger inget avdrag.",
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för takbytet i Tyresö?",
  "price": [
    "Takets yta och lutning, materialet, fasadhöjden, hur mycket råspont som behöver bytas, plåtarbetena kring skorstenen och vilken taksäkerhet som ska monteras. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får glidskyddet för stegen fästas i hängrännan?",
     "Nej. Södertörns brandförsvarsförbund skriver att glidskyddet ska förankras i en fast byggnadsdel i takfoten, eftersom rännan ofta inte klarar kravet på 150 kg."),
    ("När behövs en takbrygga fram till skorstenen?",
     "Vid invändig uppgång genom en taklucka ska det finnas en takbrygga fram till skorstenen om avståndet är över en meter, enligt förbundet."),
    ("Räcker lösa taksteg på en villa med brant tak?",
     "Lösa taksteg är enligt förbundet generellt godkända för hus med högst 4 meters fasadhöjd och taklutningar under 45 grader. För högre fasader anger förbundet en fast fasadstege eller en invändig uppgång."),
    ("Vem sotar i Tyresö och hur får vi veta när sotaren kommer?",
     "Nacka och Tyresö Sotningsdistrikt AB sotar i kommunen. Du får ett brev eller ett kort med datum och tid."),
    ("Går sotaren fortfarande upp på taket i Södertörns kommuner?",
     "Sotningen görs sedan våren 2022 underifrån med roterande undertryckssotning, men taksäkerheten är enligt förbundet fortfarande en förutsättning för sotning och brandskyddskontroll."),
  ],
  "sources": [_SBFF_TAK, _SBFF_SOT, _TY_SOT, _TY_PBL, _SKV, _SKV2],
  "cta": ("Ska taket i Tyresö bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och taksäkerheten innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa i Tyresö med nytt tegeltak, svart takstege upp till skorstenen och tallar runt huset",
     "Swedish wooden villa on a pine forest plot with a newly laid red clay tile roof, a black metal roof ladder running in a straight line from the eaves to a brick chimney, a short roof walkway beside the chimney, clear summer sky" + _IMG_END),
    ("Takfot med ny hängränna och stuprör under nylagda tegelpannor",
     "close-up of the eaves of a house with new red clay roof tiles, a black half-round gutter and a black downpipe, brick wall below, daylight" + _IMG_END),
    ("Takbrygga och taksteg monterade på nya betongpannor fram till en murad skorsten",
     "black roof walkway and roof steps mounted on new dark concrete roof tiles leading to a plastered brick chimney with black flashing, view along the roof slope, overcast sky" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VÄRMDÖ
"takbyte-varmdo.html": {
  "kind": "district", "service": "takbyte", "ort": "Värmdö", "svc_label": "Takbyte",
  "title": "Takbyte på Värmdö – anmälan, kulturmiljö, Runmarö",
  "description": "Takbyte på Värmdö: när samma material ändå kräver anmälan, lovplikt i kulturmiljöerna, tegel och plåt i Runmarös byar och takformerna.",
  "h1": "Takbyte på Värmdö",
  "lead": "Att lägga samma sorts pannor igen räknas normalt som underhåll. På Värmdö kan även ett sådant takbyte kräva en anmälan, om huset är skyddat eller har ett särskilt bevarandevärde. Geal Entreprenad AB byter tak på Värmdö och går igenom husets ställning i kommunens kartor innan materialet beställs.",
  "card": "Anmälan, kulturmiljö och tak i skärgårdsbyarna.",
  "sections": [
    {"id": "underhall-varmdo", "anchor": "Underhåll och anmälan",
     "h2": "När underhåll ändå kräver anmälan",
     "paras": [
       "Boverket skiljer mellan att byta till ett annat taktäckningsmaterial, som är en fasadändring, och att byta till samma material och utförande, som räknas som underhåll. På ett en- eller tvåbostadshus krävs normalt inget bygglov för något av dem. Värmdö kommun skriver dock att du behöver göra en anmälan och få startbesked om du ska underhålla en byggnad som är skyddad i detaljplanen eller har ett särskilt bevarandevärde.",
       "I vissa fall behövs fler tillstånd, till exempel strandskyddsdispens eller tillstånd från länsstyrelsen, även när åtgärden inte kräver bygglov. Är huset ett byggnadsminne krävs länsstyrelsens tillstånd innan det ändras. Därför tittar vi först på planen och kartorna, och sedan på pannorna.",
     ],
     "aside": {"title": "Kan krävas på Värmdö", "items": [
       "Anmälan och startbesked", "Strandskyddsdispens",
       "Tillstånd från länsstyrelsen", "Bygglov i kulturmiljö"]}},
    {"id": "kulturmiljo-varmdo", "h2": "Lovplikt i riksintressen och kulturmiljöområden",
     "paras": [
       "Med ändringarna i plan- och bygglagen från den 1 december 2025 blev det enklare att bygga utan lov på många håll, men kraven skärptes i riksintressen och kulturhistoriskt värdefulla miljöer. Där gäller lovplikt, skriver kommunen. På Värmdö finns 14 områden av riksintresse och cirka 55 utpekade kulturmiljöområden, och alla räknas som särskilt värdefulla. Om fastigheten berörs syns i kommunens kulturmiljökarta.",
       "Särskilt värdefulla byggnader får inte förvanskas, oavsett om bygglov krävs eller inte. När något ska ändras i en kulturmiljö råder kommunen dig att tänka särskilt på material och byggnadssätt, färger och takets form och lutning. Kommunantikvarien ger tips och råd, och kommunen föreslår att du först tar en promenad i området och fotograferar din fastighet. Om plåtdetaljer i blåsiga lägen kan du läsa under " + _L.format("platslagare-varmdo.html", "plåtslagare på Värmdö") + ".",
     ],
     "aside": None},
    {"id": "runmaro-varmdo", "h2": "Tegel och plåt i Runmarös byar",
     "paras": [
       "Kulturmiljöprogrammet beskriver byarna på Runmarö, och taken återkommer i texten. I Uppeby täcks flera av de knuttimrade husen av tegelklädda sadeltak. I Nore, där August Strindberg tillbringade sommaren 1889 i en parstuga med brutet tak, är taken täckta med tegelpannor. I Norrsunda och Södersunda är tegel det dominerande taktäckningsmaterialet, och många sjöbodar och båthus har tak av tegelpannor eller plåt. I Vånö är tegel eller plåt de vanligaste materialen.",
       "För den som byter tak i en sådan by blir frågan sällan vilket material som är modernast, utan vad som redan finns på huset och grannhusen. Ett hus med tegel bör kunna få tegel igen, och en sjöbod med plåt kan få ny plåt. Om hus som byggs om för helårsboende kan du läsa under " + _L.format("takrenovering-varmdo.html", "takrenovering på Värmdö") + ".",
     ],
     "aside": {"title": "Runmarö enligt programmet", "items": [
       "Uppeby – tegelklädda sadeltak", "Nore – tegelpannor",
       "Norrsunda och Södersunda – mest tegel", "Vånö – tegel eller plåt"]}},
    {"id": "takformer-varmdo", "h2": "Takformerna med programmets egna ord",
     "paras": [
       "Programmets ordlista är ett bra stöd när taket ska beskrivas i en ansökan eller ett kostnadsförslag. Ett sadeltak har två takfall som sluttar från varandra, ett upp och ned vänt V. Ett brutet tak har takfall som bryts och får en brantare nedre del, och mansardtaket beskrivs som ett sadeltak som från ungefär två tredjedelar ned från nocken sluttar brantare. Ett valmat tak avslutas på kortsidorna med ett sluttande parti, och ett säteritak är valmat och brutet av ett lågt vertikalt parti. Ett pulpettak har ett enda takfall.",
       "Ordlistan förklarar också falsat plåttak som taktäckning av tunnplåt som sammanfogas genom att kanterna böjs om, takfoten som den del av fasaden där tak och yttervägg möts och takutsprånget som den del av takfallet som skjuter ut över fasadlivet. Det är ofta just takfot och utsprång som avslöjar om ett nytt tak har lagts med samma mått som det gamla. Mer om våra tjänster finns under " + _L.format("taklaggare-varmdo.html", "takläggare på Värmdö") + " och om bytet i stort under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte på Värmdö till",
  "steps": [
    ("Kartor och plan", "Kulturmiljökartan och detaljplanen kontrolleras för fastigheten."),
    ("Platsbesök", "Vi mäter takfot och utsprång och noterar material, takform och skick."),
    ("Anmälan eller lov", "Vi tar fram uppgifterna om material och utförande som ärendet kräver."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt, plåt och ställning står var för sig."),
    ("Takbyte", "Taket läggs med samma takfot och utsprång som tidigare, om inget annat är beslutat."),
    ("Genomgång", "Vi går igenom det färdiga taket och detaljerna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte på Värmdö",
  "rot": [
    "Rotavdrag ges för arbete i både permanentbostad och fritidshus som du äger och helt eller delvis bor i. Skatteverket räknar byte av takpannor, plåttak, hängrännor och stuprör på ett småhus som rotarbete, och komplementhus som förråd och andra mindre byggnader kan höra till småhuset.",
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för takbytet på Värmdö?",
  "price": [
    "Takets yta och form, om flera byggnader på tomten ska få nytt tak, materialet, hur mycket råspont som behöver bytas, plåtarbetena och hur ställning och material kan komma fram till huset. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan det krävas anmälan för att lägga samma pannor igen på Värmdö?",
     "Ja, om byggnaden är skyddad i detaljplanen eller har särskilt bevarandevärde. Då kräver Värmdö kommun anmälan och startbesked även för underhåll."),
    ("Hur många kulturmiljöområden finns det i Värmdö kommun?",
     "Kommunen anger 14 områden av riksintresse och cirka 55 utpekade kulturmiljöområden, som alla räknas som särskilt värdefulla."),
    ("Vilket takmaterial är vanligast i byarna på Runmarö?",
     "Enligt kulturmiljöprogrammet är tegel dominerande i Norrsunda och Södersunda, medan sjöbodar, båthus och husen i Vånö ofta har tegel eller plåt."),
    ("Vad är skillnaden mellan ett brutet tak och ett säteritak?",
     "Ett brutet tak har en brantare nedre del. Ett säteritak är valmat och brutet av ett lågt vertikalt parti, enligt ordlistan i Värmdös kulturmiljöprogram."),
    ("Vem kan ge råd om takmaterial i en kulturmiljö på Värmdö?",
     "Kommunantikvarien ger tips och råd. Kommunen föreslår att du först fotograferar din fastighet och tittar på området."),
  ],
  "sources": [_VD_KM, _VD_PBL, _VD_KMP, _BV_FASAD, _SKV, _SKV2],
  "cta": ("Ska taket på Värmdö bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och vad som gäller för huset innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Rödmålat knuttimrat hus med sadeltak av röda tegelpannor i en skärgårdsby på en sluttning",
     "old red ochre painted log house with white trims and a gable roof of red clay tiles on a gentle slope in a Stockholm archipelago village, lilac bushes and leafy trees, a narrow gravel lane, calm summer morning" + _IMG_END),
    ("Sjöbod med tak av falsad plåt bredvid en brygga i en skyddad vik",
     "small red painted wooden boathouse with a grey standing seam metal roof at the water's edge of a sheltered archipelago bay, a weathered wooden jetty beside it, smooth granite rocks and reeds, summer evening light" + _IMG_END),
    ("Takfot och takutsprång på ett äldre trähus med nya tegelpannor och ny plåt",
     "close-up of the eaves and roof overhang of an old wooden house with white painted fascia board, new red clay tiles and new black metal drip edge, red painted wall below, soft daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"takbyte-osteraker.html": {
  "kind": "district", "service": "takbyte", "ort": "Österåker", "svc_label": "Takbyte",
  "title": "Takbyte i Österåker – lertegel, lov och återbruk",
  "description": "Takbyte i Österåker: kommunens frågor om huset är värdefullt, lov även för underhåll, lertegel eller betongpannor och återbruk av hela pannor.",
  "h1": "Takbyte i Österåker",
  "lead": "Innan taket byts på ett äldre hus i Österåker lönar det sig att ta reda på om huset räknas som särskilt värdefullt. Då kan även underhåll kräva bygglov. Geal Entreprenad AB byter tak i hela Österåker och går igenom husets värden och materialvalet innan något rivs.",
  "card": "Lertegel, lovfrågan och återbruk av pannor.",
  "sections": [
    {"id": "vardefullt-osteraker", "anchor": "Är huset värdefullt?",
     "h2": "Kommunens frågor: är ditt hus värdefullt?",
     "paras": [
       "Österåkers kommun har en lista med frågor för den som undrar om huset har kulturvärden. Finns det en detaljplan med skyddsbestämmelser för huset? Ligger det i eller nära ett kulturmiljöområde i Österåkerskartan? Finns det med i en inventering eller ett kulturmiljöprogram? Har det en bevarad och tidstypisk karaktär, med ursprunglig form och volym eller bevarade byggnadsdetaljer? Är huset byggt före 1920? Svarar du ja på någon av frågorna kan huset vara värdefullt.",
       "I en detaljplan betyder ett litet k att byggnaden ska behandlas varsamt, och ett litet q att den inte får rivas. Kommunen påpekar att även enkla, vardagliga byggnader och yngre bebyggelse kan ha kulturvärden. Har du kunskap om när huset byggdes blir det lättare att göra varsamma val vid renoveringen. Varsamhetskravet gäller enligt kommunen alla byggnader och alla ändringar, oberoende av husets ålder och oavsett om åtgärden kräver lov eller anmälan. Varsamheten kan till exempel gälla färgsättning, proportioner och detaljer.",
     ],
     "aside": {"title": "Ett ja kan räcka", "items": [
       "Skyddsbestämmelser i planen", "Kulturmiljöområde i kartan",
       "Med i inventering eller program", "Byggt före 1920"]}},
    {"id": "lov-underhall-osteraker", "h2": "Bygglov även för underhåll",
     "paras": [
       "Ligger fastigheten i ett kulturhistoriskt särskilt värdefullt område, eller är byggnaden själv särskilt värdefull, behöver du enligt kommunen söka bygglov för bland annat fasadändring, underhåll och solpaneler. Från den 1 december 2025 skärptes reglerna om förvanskningsförbudet, och i sådana miljöer införs eller behålls en utökad lovplikt. Kommunen ber dig kontakta bygglovsenheten innan arbetet påbörjas.",
       "Till bygglovsansökan kan det behövas en antikvarisk förundersökning som beskriver byggnadens kulturvärden och hur de påverkas, och ibland en konsekvensbeskrivning. För mindre åtgärder kan ett enklare antikvariskt utlåtande räcka. Även när lov inte krävs går det att söka frivilligt bygglov, vilket kommunen skriver kan vara en fördel om du planerar att sälja huset.",
     ],
     "aside": None},
    {"id": "lertegel-osteraker", "h2": "Lertegel eller betongpannor",
     "paras": [
       "Kommunens Råd och vägledning för byggande i Svinninge kallar taket husets femte fasad. Där står att taktegel användes på alla byggnader från slutet av 1800-talet och framåt, att nya material kom in på marknaden från 1950-talet och att äkta lertegel är ett naturmaterial som kan andas, så att fukt kan ventileras ut. Vägledningen råder att inte ersätta lertegel med betongpannor, eftersom de är tjockare och tyngre och kulören bleks med åren.",
       "Vägledningen påpekar också att ett tegeltak som inte håller tätt oftast läcker för att underlagspappen har spruckit eller för att läkten under är gammal och skadad. Det är just underlag och läkt som byts vid ett takbyte. Vägledningen råder också att se över taket innan vintern och rätta till lossnade pannor eller byta spruckna. För nya byggnader nämns nytt lertegel, slätplåt eller papp, och sedumtak som ett alternativ. Om sommarvillornas tak i kommunen kan du läsa under " + _L.format("takrenovering-osteraker.html", "takrenovering i Österåker") + ".",
     ],
     "aside": {"title": "Enligt vägledningen", "items": [
       "Lertegel kan andas", "Betongpannor är tjockare och tyngre",
       "Läckage oftast från papp eller läkt", "Taket är husets femte fasad"]}},
    {"id": "aterbruk-osteraker", "h2": "Nytt underlag – och teglet tillbaka på taket",
     "paras": [
       "Enligt vägledningen finns det ingen anledning att byta ut allt taktegel för att ett par pannor är trasiga. Komplettera i stället med begagnade eller nya pannor. Hus i grannskapet kan ofta vara belagda med tegel från samma bruk, så det kan vara värt att fråga grannarna eller annonsera efter tegel.",
       "Vid ett sådant takbyte tas pannorna ner och sorteras, och hela pannor ställs undan. Underlagspapp, läkt och plåt byts, och skadad råspont ersätts. Därefter läggs teglet tillbaka, och de pannor som saknas ersätts med begagnat eller nytt tegel som passar. Är det gamla teglet för skadat lägger vi nytt tegel, och kulören stäms av mot huset. Våra övriga tjänster i kommunen finns under " + _L.format("taklaggare-osteraker.html", "takläggare i Österåker") + ", och om bytet i stort under " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Österåker till",
  "steps": [
    ("Platsbesök", "Vi bedömer tak, underlag och vind och räknar hur stor del av teglet som är helt."),
    ("Husets värden", "Detaljplan och Österåkerskartan kontrolleras innan materialet väljs."),
    ("Skriftligt kostnadsförslag", "Rivning, sortering, underlag, tegel och plåt står var för sig."),
    ("Nedtagning", "Pannorna tas ner och sorteras, hela pannor ställs undan."),
    ("Nytt underlag", "Råspont lagas och ny underlagspapp, läkt och plåt läggs."),
    ("Teglet tillbaka", "Hela pannor läggs tillbaka och kompletteras, och vi går igenom taket med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Österåker",
  "rot": [
    "Skatteverket räknar det som rotarbete att byta och reparera takpannor och hängrännor på ett småhus, och även att montera och montera ner byggnadsställningen och att byggstäda efter arbetet. Du ska äga huset när arbetet utförs och helt eller delvis bo i det, och det gäller även fritidshus.",
    "Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material, resor och bortforsling ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för takbytet i Österåker?",
  "price": [
    "Takets yta och form, hur stor del av teglet som kan läggas tillbaka, hur mycket råspont som behöver bytas, plåtarbetena kring kupor och skorsten och om ett antikvariskt underlag behövs. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur vet vi om vårt hus i Österåker räknas som värdefullt?",
     "Kommunen har frågor att gå igenom: skyddsbestämmelser i planen, läge i ett kulturmiljöområde, med i en inventering, tidstypisk karaktär eller byggt före 1920. Ett ja kan räcka."),
    ("Kan vi behöva bygglov för att lägga om ett tegeltak i Österåker?",
     "Ja, om fastigheten ligger i ett särskilt värdefullt område eller huset är särskilt värdefullt. Då kräver kommunen bygglov även för underhåll."),
    ("Varför avråder Österåkers vägledning från att ersätta lertegel med betongpannor?",
     "Vägledningen för Svinninge skriver att betongpannor är tjockare och tyngre än lertegel och att kulören bleks med åren."),
    ("Går det att lägga tillbaka det gamla teglet efter ett takbyte?",
     "Ja, om pannorna är hela. De sorteras ut och läggs tillbaka på nytt underlag och ny läkt, och saknade pannor kompletteras med begagnat eller nytt tegel."),
    ("Vad är ett enklare antikvariskt utlåtande?",
     "Ett kortare underlag om byggnadens kulturvärden som enligt Österåkers kommun kan räcka för mindre åtgärder, i stället för en hel antikvarisk förundersökning."),
  ],
  "sources": [_OS_KM, _OS_RAD, _BV_FASAD, _SKV, _SKV2],
  "cta": ("Ska taket i Österåker bytas?", "Boka ett gratis platsbesök, så går vi igenom taket, teglet och lovfrågan innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla i Österåker med branta tak av patinerat rött lertegel och veranda mot vattnet",
     "Swedish turn-of-the-century wooden summer villa painted pale yellow with white trims, steep roofs covered with weathered red clay tiles with varied patina, a glazed veranda facing a calm bay, tall pine and birch trees, summer afternoon light" + _IMG_END),
    ("Sorterade gamla lertegelpannor staplade på pallar bredvid ett tak med ny underlagspapp och läkt",
     "neat stacks of old red clay roof tiles sorted on wooden pallets on a lawn next to a house whose roof shows new black underlay felt and fresh pale battens, scaffolding along the eaves, overcast daylight" + _IMG_END),
    ("Tak där återlagda patinerade tegelpannor möter några nyare pannor",
     "close-up of a pitched roof with re-laid old weathered red clay tiles in slightly varied shades, a few replacement tiles of matching shape, new black flashing at the edge, soft daylight" + _IMG_END),
  ],
},

}
