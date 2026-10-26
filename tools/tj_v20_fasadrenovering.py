# -*- coding: utf-8 -*-
"""Fasadrenovering – ortsidor v20: Kungsholmen, Sundbyberg, Södermalm, Vasastan, Vällingby, Östermalm (2026-10-26).
Hubb fasadrenovering.html. Innerstadsorterna har nästan inga villor: sidorna riktar sig till bostadsrättsförening/
fastighetsägare, och rotavdrag anges bara där det gäller (småhus som ägs; inte för BRF-medlem på fasad – Skatteverket).
Skild från ortens övriga sidor (malare-, fonsterrenovering-, fasadmalning-vallingby, byggforetag-vallingby m.fl.) och
från tidigare fasadrenovering-moduler (v3/v6/v10/v12) – egna vinklar, egna FAQ, inga återanvända formuleringar.
Lokal vinkel per sida (en huvudfråga per sida):
Södermalm – kalkputsen på äldre stenhus: Östra Mariaberget efter branden 1759 (slätputs, ljusa gula toner), stenstaden
1870–1930, kalkbruk lagas med kalkbruk, kalkfärg 4–6 strykningar, plåt på putsade lister, klassning/utökad lovplikt;
Östermalm – gatufasad och gårdsfasad: stenstadens sockelvåning/huvudfasad/takfot/attika och enklare gårdsfasader,
lov mot allmän plats för flerbostadshus, NCS-kulörbeskrivning, PBL 8:13/8:17, Villastaden med förgårdar;
Vasastan – ställningen mot gatan: polistillstånd för ställning/container/bod på offentlig plats, 1,6 m/2 m-villkoret,
upplag, avgiftsprincip (inga belopp), bygglov för bod/container/plank, etablering på egen fastighet, underhållsplan i BRL;
Kungsholmen – funkishusens puts i Fredhäll/Kristineberg: putsen som arkitektur (SLM), k-bruk/kc-bruk, putsbortfall och
fukt, tvåstegstätning, tilläggsisolering (kallare yttre del, fönsterläge), fristående hus med flera fasader mot allmän plats;
Sundbyberg – Duvbos villafasader i tre generationer (fasspont i fält, locklistpanel, slätputs med kalkfärg), utökad
lovplikt i Duvbo, programmets underhållsråd, frivilligt bygglov, lov mot allmän plats för stadens flerbostadshus;
Vällingby – tegel, puts och fibercementskivor: vägledningens materialbeskrivning, riksintressets detaljer, tegel
underhållsfritt men taksprång/fogar/anslutningar, asbest i cementfiberplattor + AV-tillstånd, materialbyte som fasadändring.

Fakta endast från källorna i respektive 'sources', öppnade och lästa (urllib, User-Agent Mozilla) 2026-10-26, alla
svarade 200; pdf:er med textlager via pdftotext:
  Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf): Östra Mariaberget (efter branden 1759, 2–3
  våningar, väl proportionerade slätputsade fasader i ljusa gula toner, brutna tak med tegel, ombyggnader och
  påbyggnader mot Hornsgatan under 1800-talets andra hälft, ovanligt sammanhållen bild av 1700-talets stadsbyggande);
  klassiska stenstaden 1870–1930 på Östermalm, Södermalm, Kungsholmen och Norrmalm, normalt fem våningar vid 18 meter
  breda gator, dekorerade fasader i puts eller natursten, sammanbyggda fasader i gatuliv och kringbyggda gårdar,
  gatufasadernas uppdelning i sockelvåning och huvudfasad med markerad takfot och ibland attikavåning samt enklare
  gårdsfasader, byggnadsdetaljering, många hus gul klass (relativt låg) – betydelsen för stadsmiljön avgörande;
  esplanaderna Strandvägen, Valhallavägen, Narvavägen, Karlavägen med bostadspalats från 1800-talets sista decennier;
  Villastaden norr om Humlegården efter 1876 (engelskt mönster, fristående villor indragna med förgårdar, senare högre
  flerbostadshus, måttfullt klassicerande putsarkitektur, förträdgårdar med staket eller murar); Motorn och Vingen i
  norra Vasastaden slutet av 1910-talet, kooperativt byggande med kommunalt stöd; funktionalistiska stadsdelar omkring
  1930, Fredhäll och Kristineberg, fristående huskroppar med öppna gröna gårdar; Vällingby AB 120 (ursprungliga husens
  fönster, entrépartier, balkonger och räcken; centrumanläggningarnas form-, färg- och materialverkan).
  Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf): tunnelbanestaden – blandning av moderna idéer
  och folkhemsideal, rött tegel vanligt, även puts och fibercementskivor, industrialiserad men terränganpassad,
  materialval varierar, tidstypisk färgsättning; Vällingby–Råcksta riksintresse.
  bygglov.stockholm: Fasadändring (exempel byte av kulör/material, tilläggsisolering; flerbostadshus lov mot allmän
  plats, lovfritt annars under förutsättningar; lovfria ska stämma med detaljplan; utökad lovplikt; detaljplan i
  Bygg- och plantjänsten; fasadritning 1:100, fotomontage vid mycket enkla ändringar, material- och kulörbeskrivning i
  NCS; startbesked/slutbesked; en- och tvåbostadshus inte längre lov under förutsättningar); Stadsmuseets klassificering
  (blå ring riksintresse, grön ring, blått/grönt kräver lov för annars lovfria åtgärder); Kulturhistorisk värdefull
  byggnad och område (utökad lovplikt t.ex. underhållsåtgärder, antikvarisk förundersökning); Byggbod, byggetablering,
  byggskylt (lov för bod, plank, skylt, upplag, container; glest byggstängsel utan lov; egen fastighet om det går;
  annans mark – ägarens tillstånd; stadens mark – polistillstånd).
  tillstand.stockholm – Använda offentlig plats för byggverksamhet (polistillstånd före användning, omfattar allt;
  ställningar, containrar, bodar, mobilkranar, byggsäckar, skyltar, tillfart; 1,6 m fritt under eller 2 m för gående;
  upplag för ställningsmaterial i tillståndet; polisens administrationsavgift; stadens avgift per zon, per kvm och år,
  engångskostnad vid kort etablering, kvartalsvis vid lång; ingen reducerad avgift sedan 1 maj 2021; byggskylt högst
  15 kvm). Stadens zonbelopp i kr är medvetet INTE återgivna.
  Stockholms stad – Områdesfakta: Mariatorget 2025 (8 701 bostäder, 5 027 bostadsrätter, 35 i småhus, 0 äganderätter);
  Hedvig Eleonora 2025 (7 344, 5 164 BR, 11 småhus, 2 äganderätter); Västra Matteus 2025 (12 579, 8 990 BR, 0 småhus);
  Östra Matteus 2025 (7 680, 5 593 BR, 0 småhus); Fredhäll 2025 (3 830, 2 219 BR, 0 småhus); Kristineberg 2025 (4 598,
  3 243 BR, 1 småhus); Kungsholmens stadsdelsområde 2024 (44 554, 337 småhus, 272 äganderätter i småhus); Vällingby
  2025 (449 i småhus varav 228 BR och 220 äganderätter, 3 891 i flerbostadshus och övriga hus).
  Länsstyrelserna i Gävleborgs, Västmanlands och Örebro län – Puts på mur och trä (pdf): kalkputs mjuk, tar upp rörelser,
  hållbarare än hårdare puts; rent kalkbruk till mitten av 1900-talet ("så gott som" – återgivet "nästan bara");
  cement – hårdare, mindre elastisk, tätare, problem vid lagning av kalkputs med cementbruk; kalkputs lagas med kalkbruk;
  skador vid läckande stuprör, under fönster, vid grunden; sprickor av sättningar, putsbortfall av vatten/fukt, frost;
  plastfärg för tät; titta noga på orsakerna; kalkfärg 4–6 strykningar, transparent lyster; tjockare kalkfärg med
  dolomit på cementhaltig puts, två strykningar; plasttillsats undviks; plåtlist med traditionell utformning.
  Stockholms läns museum – Byggnadswebben: Putsad fasad (funktionalismen 1930-tal, viktig del av arkitekturen 1930–40-tal,
  slätputs/spritputs, k-bruk, cement tillsatt efter 1940-talet = kc-bruk, mindre elastiskt); Tegelfasad (i stort sett
  underhållsfritt, taksprång, järnoxid -> rött, kalkrik lera -> gult, förband, ligg- och stötfogar, mexitegel inte tegel).
  Boverket – Fuktrisker med fasadens material och ytskikt (tvåstegstätning vid infästningar/anslutningar vid slagregn,
  fuktskador om ytskiktet inte torkar, putsbortfall "nästan alltid" fukt – återgivet "i de allra flesta fall", kalkputs
  suger och avger fukt, frost, tjockare isolering ger kallare yttre del och puts som inte torkar, cementfiberplattor med
  asbest 1940–50-tal, fibrer vid bearbetning t.ex. borrning); Energiguiden: Tilläggsisolera fasaden (fönster och dörrar
  längre in, takfot, exempel på putsade funkishus där takfot, sockel, skärmtak byggts på och fönster flyttats ut).
  Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest (tillstånd för företaget, fasad utomhus, förarbete/
  avfall/städning räknas, ansökan åtta veckor före).
  Riksdagen – PBL 8 kap. 13 § (förvanskningsförbud), 14 § (underhåll, särskilt värdefulla – särskilda värden bevaras),
  17 § (varsamhet vid ändring); Bostadsrättslag 3 kap. 1 a § (teknisk underhållsplan 50 år i ekonomiska planen) och
  7 kap. 4 § (föreningen håller huset i gott skick).
  Sundbybergs stad – Fasadändring (utökad lovplikt i Duvbo och för kulturhistoriskt värdefulla, exempel inkl.
  tilläggsisolering, flerbostadshus lov mot allmän plats, anmälan vid bärande/brand, handlingar, byggherrens ansvar,
  frivilligt bygglov); Miljöprogram Duvbo (pdf: Egna Hem 1898, Dufvebol året därpå, 325 tomter, 1924 +98, riksintresse
  RAÄ 1987, två våningar på höga socklar, linoljefärg/slamfärg, villor ofta byggda av ägarna; tabell sekelskifte/
  1920-tal/1940-tal: fasader, tak, socklar, färgsättning, detaljer; underhållsråd; utökad lovplikt – fasadbeklädnad,
  omfärgning, fönster/dörrar; färgförslag via förvaltningen).
  Skatteverket – Ger arbetet rätt till rotavdrag? (småhus: byta och reparera fasader, mura och reparera fasader, måla
  fasader, ställning i samband med rotarbete, sanera asbest i samband med byggarbete; inget avdrag för att mäta asbest;
  bostadsrätt: inget avdrag för gemensamma ytor som fasader, tilläggsisolera, ställning på utsidan); Så fungerar
  rotavdraget (30 procent, 50 000/75 000 kr, äga och bo, material/resor/utrustning/administration ger inget avdrag).
Strukna (ej verifierade eller medvetet utelämnade): stadens zonavgifter för gata och ställning (kr-belopp – inte
återgivna), Arbetsmiljöverkets sidor om ställningar (404 på testade adresser – inga ställningsregler skrivna),
Stockholms läns museums flik "Underhåll" för tegel (finns inte i sidans text – inget om omfogning tillskrivet museet),
Röda Bergens läge (källan anger inte stadsdel), att Villastaden ligger i stadsdelen Hedvig Eleonora (inte kopplat),
att funkishusen på Kungsholmen har kalkputs (bara museets datering av cementen; prov rekommenderas), att Mariabergets
hus i dag har kalkputs, Duvbo-programmets uppgift att lov inom utökad lovplikt är kostnadsfritt (avgiftsuppgift, 2022),
Sundbybergs telefontider/kontakt, "de flesta i Sundbyberg bor i flerbostadshus" (ingen källa – struket), stadens
balkongvägledning (gäller nya balkonger), alla priser, tidsåtgång och handläggningstider.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert. Perks enbart sajtens befintliga: gratis
platsbesök, skriftligt kostnadsförslag, ROT direkt på fakturan (bara där det gäller), en kontakt.
Kritikpass 2026-10-26 (alla källor öppnade igen, varje faktamening mot källtexten): Södermalm – "ett par kvarter bort"
(egen lägesuppgift) -> "på andra delar av Södermalm"; Mariatorgets småhus: inga äganderätter (tabell kontrollerad).
Östermalm – "Östermalm är en stadsdel av lägenheter" byggde bara på Hedvig Eleonora -> omskrivet; FAQ "Inte alltid" ->
"Det beror på". Vasastan – "nästan alltid ett föreningsprojekt" och "i praktiken alltid" strukna (absoluter);
påståendet att tillståndsavgifter inte ger rotavdrag ersatt med Skatteverkets lydelse (material, resor, utrustning,
administration). Kungsholmen – mening om fönsterläge vid tilläggsisolering saknade källa på sidan: Boverkets energiguide
tillagd som källa och meningen skriven efter dess text; Kristinebergs småhus = 1 (allmännyttan). Sundbyberg – "taken
genomgående rött lertegel" rättat (sekelskiftet även falsad slätplåt/papp i tabellen); "de flesta bor i flerbostadshus"
struket. Vällingby – mexitegel "inte bränd lera" -> museets ord "inte ett tegel". Descriptions kortade till <= 155.
tj_check: inga FEL, ordantal 1220–1429, enda WARN är saknade bilder (genereras senare, -1/-2/-3.webp).
Kritikpass 2 (extern) 2026-10-26: alla 27 käll-URL:er öppnade med curl (-L, Mozilla), 200; alla 12 pdf:er har
textlager (pdftotext); ingen källa struken. Rättat: Södermalm – lead "puts som är äldre än cementen" (dagens puts
okänd) -> "putsades när kalkbruk ännu var det vanliga"; description "kalkputsade stenhus" -> "putsade stenhus";
"räknar Södermalm till stenstaden" -> planens ord "utbredning ... även över Södermalm"; "fasaden är föreningens
ansvar" (BRL ej källa på sidan) -> "föreningen/fastighetsägaren beställer". Östermalm – egen slutsats om gulklassad
fasad vid esplanad "lika känslig" -> "gul klass betyder inte att fasaden saknar betydelse vid prövning"; "ställningen
får planeras" -> "kan"; Hedvig Eleonora-slutsatsen avgränsad ("Där"). Vasastan – "Gemensamt för husen ..." (absolut)
-> "I sådana kvarter"; "Ställningen ska vara tillgänglighetsanpassad" (står inte) -> stadens villkor för
tillgänglighetsanpassad ställning; "därför oftast på föreningens mark" -> "kan ofta"; underhållsplanen "en post med
en tidpunkt" (egen tolkning) struken; ROT "Utan småhus i stadsdelarna" -> bara Västra/Östra Matteus (Vasastan har
fler stadsdelar, t.ex. Gustav Vasa, Norra Adolf Fredrik – inget påstående om hela Vasastan); "äger och bor i" ->
"i eller i nära anslutning till" (Skatteverket). Kungsholmen – "Vilken mark som är allmän plats står i detaljplanen"
saknade källa -> PBL 1 kap. 4 § (definition) tillagd som källa _PBL_AP, text och FAQ efter lagtexten. Sundbyberg –
sekelskiftets tak "ibland även falsad slätplåt" -> "även falsad slätplåt eller papp" (tabellen); "de äldre och de
yngre husen" -> sekelskiftet och 1920-talet (programmets syftning); "påverkar bärande delar" -> "väsentligt";
"styrelsen har ansvaret" (ingen källa) -> stadens lydelse om byggherrens ansvar. Vällingby – "det som ska värnas"
-> "värdebärande karaktärsdrag"; tegel-FAQ: villkoret tillräckliga taksprång tillagt, översynen som vårt arbetssätt.
Kontrollerat utan ändring: alla områdesfakta-tal (Mariatorget 8 701/5 027/35/0 äganderätt; Hedvig Eleonora 7 344/
5 164/11/2; Västra Matteus 12 579/8 990/0; Östra Matteus 7 680/5 593/0; Fredhäll 3 830/2 219/0; Kristineberg 4 598/
3 243/1; Kungsholmen 2024 44 554/337/272; Vällingby 449/228/220/3 891), PBL 8:13/14/17, BRL 3:1 a (50 år) och 7:4,
kalkfärg 4–6 resp. 2 strykningar, 1,6 m/2 m, 15 kvm, 1 maj 2021, åtta veckor (AV), Duvbo 1898/325/1924 +98/1987.
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

# ------------------------------------------------------------------ gemensamma källor
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 8 kap. 13, 14 och 17 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_PBL_AP = ("Riksdagen – Plan- och bygglag (2010:900), 1 kap. 4 § (allmän plats)",
           "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 3 kap. 1 a § och 7 kap. 4 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SB_FAS = ("Stockholms stad – Fasadändring (bygglov.stockholm)",
           "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/")
_SB_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov.stockholm)",
             "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_SB_KVB = ("Stockholms stad – Kulturhistorisk värdefull byggnad och område (bygglov.stockholm)",
           "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/kulturhistorisk-vardefull-byggnad-och-omrade/")
_SB_BOD = ("Stockholms stad – Byggbod, byggetablering, byggskylt (bygglov.stockholm)",
           "https://bygglov.stockholm/nar-behovs-bygglov/bygga-nytt-och-bygga-till/byggbod-byggetablering-byggskylt/")
_TL_BYGG = ("Stockholms stad – Använda offentlig plats för byggverksamhet (tillstand.stockholm)",
            "https://tillstand.stockholm/tillstand-regler-och-tillsyn/anvanda-offentlig-plats/anvanda-offentlig-plats-for-byggverksamhet/")
_OP_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
            "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_OF_MARIA = ("Stockholms stad – Områdesfakta 2025: Mariatorget (pdf)", _OF + "inre-staden/sodermalm/mariatorget.pdf")
_OF_HEDV = ("Stockholms stad – Områdesfakta 2025: Hedvig Eleonora (pdf)", _OF + "inre-staden/norra-innerstaden/hedvig-eleonora.pdf")
_OF_VM = ("Stockholms stad – Områdesfakta 2025: Västra Matteus (pdf)", _OF + "inre-staden/norra-innerstaden/vastra-matteus.pdf")
_OF_OM = ("Stockholms stad – Områdesfakta 2025: Östra Matteus (pdf)", _OF + "inre-staden/norra-innerstaden/ostra-matteus.pdf")
_OF_KUNGS = ("Stockholms stad – Områdesfakta: Kungsholmens stadsdelsområde (pdf)",
             _OF + "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade.pdf")
_OF_FRED = ("Stockholms stad – Områdesfakta 2025: Fredhäll (pdf)", _OF + "inre-staden/kungsholmen/fredhall.pdf")
_OF_KRIST = ("Stockholms stad – Områdesfakta 2025: Kristineberg (pdf)", _OF + "inre-staden/kungsholmen/kristineberg1.pdf")
_OF_VALL = ("Stockholms stad – Områdesfakta 2025: Vällingby (pdf)", _OF + "vasterort/hasselby-vallingby/vallingby.pdf")
_LST_P = ("Länsstyrelserna i Gävleborgs, Västmanlands och Örebro län – Information om byggnadsvård: Puts på mur och trä (pdf)",
          "https://catalog.lansstyrelsen.se/store/23/resource/2000__17")
_SLM_P = ("Stockholms läns museum – Byggnadswebben: Putsad fasad",
          "https://stockholmslansmuseum.se/byggnadswebben/byggnadsvard/exterior/puts/")
_SLM_T = ("Stockholms läns museum – Byggnadswebben: Tegelfasad",
          "https://stockholmslansmuseum.se/byggnadswebben/byggnadsvard/exterior/tegel/")
_BV_FMAT = ("Boverket – Fuktrisker med fasadens material och ytskikt",
            "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-yttervaggar/fasadmaterial-ytskikt/")
_BV_ISOL = ("Boverket – Energiguiden: Tilläggsisolera fasaden",
            "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/tillaggsisolera-fasaden/")
_AV_ASB = ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest",
           "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/")
_SBG_FAS = ("Sundbybergs stad – Fasadändring (bygglovsguide)",
            "https://www.sundbyberg.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/bygglovsguide/fasadandring")
_SBG_DUVBO = ("Sundbybergs stad – Miljöprogram Duvbo (pdf)",
              "https://www.sundbyberg.se/download/18.736374e81919758d37bf776/1725513597936/Miljo%CC%88program%20Duvbo%202024%20tillga%CC%88nglighetsanpassad%20webb.pdf")

PAGES_TJ = {

# ------------------------------------------------------------------ SÖDERMALM
"fasadrenovering-sodermalm.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Södermalm", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering på Södermalm – puts på de äldre stenhusen",
  "description": "Fasadrenovering på Södermalm: putsade stenhus från 1700-talet och stenstaden – lagning med rätt bruk, kalkfärg, plåt på lister och lovfrågan.",
  "h1": "Fasadrenovering på Södermalm",
  "lead": "Många av Södermalms stenhus putsades när kalkbruk ännu var det vanliga. Lagas putsen med fel bruk kan skadan bli större än den var. Geal Entreprenad AB renoverar putsfasader på Södermalm åt bostadsrättsföreningar och fastighetsägare – vi tar reda på vilket bruk som sitter på väggen innan något knackas ner.",
  "card": "Kalkputs, kalkfärg och plåt på lister.",
  "sections": [
    {"id": "mariaberget-sodermalm", "anchor": "Mariaberget",
     "h2": "Östra Mariabergets ljusa slätputs",
     "paras": [
       "Stadens översiktsplan beskriver bebyggelsen vid Östra Mariaberget som ett enastående exempel på 1700-talets medvetna stadsbyggande. Husen kom till efter en stor brand 1759 och uppfördes i två till tre våningar med väl proportionerade, slätputsade fasader i ljusa gula toner. Taken var brutna och lades med tegel. Under 1800-talets andra hälft byggdes många av husen om, och en del – särskilt mot Hornsgatan – fick påbyggnader. Planen kallar området en ovanligt sammanhållen bild av hur Stockholm byggdes på 1700-talet.",
       "På andra delar av Södermalm tar nästa husgeneration vid. Enligt översiktsplanen breder den klassiska stenstaden från 1870–1930 ut sig även över Södermalm, med hyreshus som normalt är fem våningar höga och har tidstypiska, dekorerade fasader i puts eller natursten. För fasadarbetet betyder det att två grannhus kan ha byggts med helt olika bruk, och att en lagningsmetod som fungerar på det ena inte självklart passar det andra.",
     ],
     "aside": {"title": "Två husgenerationer", "items": [
       "Efter branden 1759: två–tre våningar, slätputs", "Ljusa gula toner, brutna tegeltak",
       "Stenstaden 1870–1930: fem våningar", "Dekor i puts eller natursten"]}},
    {"id": "kalkbruk-sodermalm", "h2": "Kalkputs lagas med kalkbruk",
     "paras": [
       "Länsstyrelsernas informationsblad om puts på mur och trä förklarar varför bruket spelar så stor roll. En kalkputs är relativt mjuk och svag och kan därför ta upp en del rörelser i underlaget utan att spricka eller lossna – vilket enligt bladet paradoxalt nog gör den hållbarare än en hårdare puts. Fram till mitten av 1900-talet användes nästan bara rent kalkbruk. Byts en del av kalken mot cement blir putsen hårdare, mindre elastisk och tätare mot fukttransport, och därför uppstår ofta problem när ett kalkputsat hus lagas med cementhaltigt bruk. Bladets råd är tydligt: kalkputs ska lagas med kalkbruk, annars får den gamla putsen och lagningen olika egenskaper.",
       "Skadorna sitter enligt bladet ofta där fasaden har fått ta emot vatten – vid läckande stuprör, under fönster och vid grunden. Sprickor beror på sättningar och rörelser i väggen eller grunden, medan putsbortfall hänger ihop med vatten och fukt: fuktig puts som inte hinner torka fryser sönder och lossnar. Även en för tät färg, till exempel plastfärg, kan skada eftersom fukten inifrån inte kommer ut. Bladet uppmanar den som ska putsa om att först titta noga på fasaden och fundera över orsakerna, och det är där vi börjar: vi letar upp varifrån vattnet kommer innan vi lagar det som vattnet har förstört.",
     ],
     "aside": {"title": "Vi letar orsaken vid", "items": [
       "Stuprör och hängrännor", "Fönsterbleck och smygar", "Sockeln mot gatan", "Tidigare lagningar med cement"]}},
    {"id": "kalkfarg-sodermalm", "h2": "Kalkfärgen, listerna och styrelsens beslut",
     "paras": [
       "Är huset målat med kalkfärg ska man enligt Länsstyrelsernas blad fortsätta med det vid ommålning. Traditionell kalkfärg blandas av våtsläckt kalkpasta, vatten och pigment och behöver fyra till sex strykningar för full täckning, men den blir transparent och får en vacker lyster. Innehåller putsen cement går vanlig kalkfärg inte att använda; då kan en tjockare kalkfärg med ballast av krossad dolomit strykas, och den täcker på två strykningar. Kalkfärger med tillsats av plast bör enligt bladet undvikas. Putsade lister täcks ofta av plåt, och bladet visar hur en plåtlist med traditionell utformning blir mindre iögonfallande än en av modern typ.",
       "Innan arbetet beställs behöver styrelsen veta vad som gäller för huset. Är det markerat med blått eller grönt i Stadsmuseets klassificeringskarta, eller ligger det inom ett riksintresse, krävs enligt Stockholms stad bygglov även för åtgärder som annars är lovfria. I vissa detaljplaner gäller utökad lovplikt för till exempel underhållsåtgärder, och inför arbetet kan det behövas en antikvarisk förundersökning. Plan- och bygglagen kräver dessutom att ett byggnadsverk underhålls så att utformningen i huvudsak bevaras – och på ett särskilt värdefullt hus så att de särskilda värdena bevaras. Om fönstren i samma fasad, se " + _L.format("fonsterrenovering-sodermalm.html", "fönsterrenovering på Södermalm") + ", och om målning inomhus " + _L.format("malare-sodermalm.html", "målare på Södermalm") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi en putsfasad på Södermalm",
  "steps": [
    ("Genomgång med styrelsen", "Vi går runt huset, knackar på putsen och noterar sprickor, bom och gamla lagningar."),
    ("Bruk och färg", "Ett prov av putsen och färgen visar om fasaden är kalkputsad eller innehåller cement."),
    ("Klassning och lov", "Vi kontrollerar Stadsmuseets karta och detaljplanen innan något beställs."),
    ("Skriftligt kostnadsförslag", "Lagning, omputsning, plåt och avfärgning redovisas var för sig."),
    ("Lagning", "Lös puts knackas ner, underlaget rensas och nytt bruk av samma slag läggs i skikt."),
    ("Avfärgning och plåt", "Fasaden avfärgas med en färg som passar putsen, och listernas plåt läggs om."),
  ],
  "rot_h2": "ROT-avdrag vid fasadrenovering på Södermalm",
  "rot": [
    "I ett flerbostadshus är det föreningen eller fastighetsägaren som beställer fasadarbetet. För en bostadsrättshavare räknar Skatteverket fasader till de gemensamma ytorna, och arbete där ger inget rotavdrag – inte heller att montera en byggnadsställning på utsidan av bostaden. I stadsdelen Mariatorget finns enligt stadens områdesfakta 2025 8 701 bostäder, varav 5 027 bostadsrätter, och bara 35 bostäder i småhus. Inget av småhusen där är en äganderätt.",
    "Äger du ett småhus räknas att byta, mura, reparera och måla fasader som rotarbete, liksom ställning i samband med arbetet. Avdraget är högst 30 procent av arbetskostnaden, som mest 50 000 kr per person och år och 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Södermalm?",
  "price": [
    "Fasadens yta och höjd, hur stor del av putsen som har släppt, om tidigare cementlagningar måste tas bort, antalet strykningar kalkfärgen kräver och hur mycket plåt som ska läggas om styr kostnaden. Efter ett gratis platsbesök får styrelsen ett skriftligt kostnadsförslag med varje moment för sig.",
  ],
  "faq": [
    ("Varför ska en kalkputsad fasad inte lagas med cementbruk?",
     "Cement gör putsen hårdare, mindre elastisk och tätare mot fukt. Länsstyrelsernas blad skriver att det ofta ger problem att laga ett kalkputsat hus med cementhaltigt bruk, eftersom lagningen och den gamla putsen får olika egenskaper."),
    ("Hur många gånger behöver kalkfärg strykas på en putsfasad?",
     "Traditionell kalkfärg behöver fyra till sex strykningar för full täckning, enligt Länsstyrelsernas blad. En tjockare kalkfärg med dolomitballast, som används på cementhaltig puts, täcker på två."),
    ("Hur såg husen vid Östra Mariaberget ut när de byggdes?",
     "Enligt stadens översiktsplan uppfördes de efter branden 1759 i två till tre våningar med slätputsade fasader i ljusa gula toner och brutna tegeltak."),
    ("Var på en putsfasad brukar skadorna börja?",
     "Där fasaden får ta emot vatten: vid läckande stuprör, under fönster och vid grunden, enligt Länsstyrelsernas blad om puts."),
    ("Kan föreningens medlemmar få rotavdrag för fasadrenoveringen?",
     "Nej. Skatteverket räknar fasader till de gemensamma ytorna i en bostadsrättsförening, och arbete där ger inget rotavdrag för bostadsrättshavaren."),
  ],
  "sources": [_OP_RIKS, _LST_P, _SB_KLASS, _SB_KVB, _PBL, _OF_MARIA, _SKV, _SKV2],
  "cta": ("Har putsen börjat släppa på föreningens hus?", "Boka ett gratis platsbesök, så tar vi reda på vilket bruk som sitter på väggen och lämnar ett skriftligt kostnadsförslag till styrelsen."),
  "img": [
    ("Ljusgult slätputsat 1700-talshus i tre våningar med brutet tegeltak på en kullerstensgata",
     "row of small three-storey 18th century stone houses in Stockholm Södermalm hillside, smooth pale yellow lime render facades, mansard roofs with red clay tiles, small-paned white windows, cobblestone lane, soft overcast daylight, realistic photo, no people, no text, no letters"),
    ("Putsfasad där lös puts har knackats ner och nytt kalkbruk lagts i skikt nära sockeln",
     "close-up of an old rendered stone facade being repaired near the plinth, loose render removed down to brick and stone, fresh grey lime mortar applied in layers, mason trowel and mortar board resting on scaffold plank, pale ochre lime-washed surface around, realistic photo, no people, no hands, no text, no letters"),
    ("Putsad gesims med nylagd plåtavtäckning och nyavfärgad kalkfärg i ljust gult",
     "close-up of a rendered cornice on an old Stockholm stone building, freshly lime-washed pale yellow render with slightly translucent texture, new dark grey sheet-metal capping with traditional folded edge on top of the cornice, scaffolding tube edge in foreground, realistic photo, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ÖSTERMALM
"fasadrenovering-ostermalm.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Östermalm", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering på Östermalm – gatufasad och gårdsfasad",
  "description": "Fasadrenovering på Östermalm: stenstadens dekorerade gatufasader och enklare gårdsfasader – lov mot allmän plats, kulör i NCS och Villastadens hus.",
  "h1": "Fasadrenovering på Östermalm",
  "lead": "Ett stenhus på Östermalm har oftast två ansikten: en påkostad fasad mot gatan och en enklare mot gården. Reglerna för dem skiljer sig åt, och det gör arbetet också. Geal Entreprenad AB renoverar fasader på Östermalm åt bostadsrättsföreningar och fastighetsägare och planerar gatusidan och gårdssidan var för sig.",
  "card": "Gatufasad, gårdsfasad och lovfrågan.",
  "sections": [
    {"id": "gatufasad-ostermalm", "anchor": "Gatufasaden",
     "h2": "Sockelvåning, huvudfasad och takfot",
     "paras": [
       "Översiktsplanens avsnitt om den klassiska stenstaden, bebyggelsen från 1870–1930 som bland annat breder ut sig över Östermalm, räknar upp vad som bär stadsdelens karaktär. Där finns gatufasadernas tydliga uppdelning i sockelvåning och huvudfasad, oftast med markerad takfot och ibland med en attikavåning, och där finns de enklare gårdsfasaderna. Hyreshusen är normalt fem våningar höga vid 18 meter breda gator och har tidstypiska, dekorerade fasader i puts eller natursten. Längs Strandvägen, Valhallavägen, Narvavägen och Karlavägen beskriver planen esplanader inramade av monumentala bostadspalats från 1800-talets sista decennier.",
       "Planen påpekar också att många hus i stenstaden har en relativt låg klassificering, gul klass, därför att de har förändrats sedan de byggdes. Vid prövning ska ändå betydelsen för stadsmiljön vara avgörande och inte det enskilda husets klassificering. Att ett hus har gul klass betyder alltså inte att fasaden saknar betydelse när en ändring prövas.",
     ],
     "aside": {"title": "Gatufasadens delar", "items": [
       "Sockelvåning", "Huvudfasad med dekor i puts eller natursten", "Markerad takfot", "Ibland en attikavåning"]}},
    {"id": "lov-ostermalm", "h2": "Mot gatan krävs lov – mot gården beror det på",
     "paras": [
       "För ett flerbostadshus skriver Stockholms stad att det krävs bygglov för en fasadändring på fasad eller tak som vetter mot allmän plats, alltså i regel gatan. En ändring som inte vetter mot allmän plats kräver inte lov, om vissa förutsättningar är uppfyllda – den ska till exempel stämma med detaljplanen eller vara en liten avvikelse som inte motverkar planens syfte, och utökad lovplikt får inte gälla. Som fasadändring räknar staden bland annat byte av kulör eller material på fasad eller tak och tilläggsisolering.",
       "Lovfri eller inte, så gäller samma grundkrav på båda sidor om huset. Plan- och bygglagen säger att en ändring av en byggnad ska utföras varsamt så att byggnadens karaktärsdrag och dess tekniska, historiska, kulturhistoriska, miljömässiga och konstnärliga värden tas till vara, och att en särskilt värdefull byggnad inte får förvanskas. Gårdsfasaden kan vara enklare, men den hör till samma hus. Söker föreningen lov ska ansökan enligt staden ha en fasadritning i skala 1:100 och en material- och kulörbeskrivning där kulörerna anges i NCS-systemet. Vid mycket enkla ändringar kan ett fotomontage ersätta fasadritningen. Arbetet får inte börja förrän startbesked har getts, och när föreningen har visat att kraven är uppfyllda kommer ett slutbesked.",
     ],
     "aside": {"title": "Lov för flerbostadshus", "items": [
       "Fasad mot allmän plats: bygglov", "Mot gården: lovfritt under förutsättningar",
       "Kulör anges i NCS", "Fasadritning i skala 1:100"]}},
    {"id": "villastaden-ostermalm", "h2": "Villastaden och de få småhusen",
     "paras": [
       "Norr om Humlegården ligger Villastaden, som enligt översiktsplanen byggdes efter 1876 efter engelskt stadsplanemönster. De tidiga husen blev stora fristående villor indragna från gatan med planterade förgårdar, och när planen fullföljdes växte skalan till högre fristående flerbostadshus. Bland karaktärsdragen nämner planen den måttfullt klassicerande putsarkitekturen och förträdgårdar inhägnade med staket eller murar mot gatan. Här kan fasaden mot gatan alltså stå en bit in på tomten, och ställningen kan planeras över förgården i stället för på trottoaren.",
       "Annars är det lägenheterna som dominerar. Stadens områdesfakta för stadsdelen Hedvig Eleonora 2025 räknar 7 344 bostäder, varav 5 164 bostadsrätter, och bara 11 bostäder i småhus, av vilka två är äganderätter. Där är det alltså nästan undantagslöst en förening eller fastighetsägare som beställer fasadarbetet. Om målning inne i lägenheten, se " + _L.format("malare-ostermalm.html", "målare på Östermalm") + ", och om fasadarbete i stort " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi en fasad på Östermalm",
  "steps": [
    ("Två fasader, två genomgångar", "Vi går igenom gatufasaden och gårdsfasaden var för sig och noterar skador på puts, sten och plåt."),
    ("Klassning och detaljplan", "Vi kontrollerar Stadsmuseets karta och vad detaljplanen säger om just den här fastigheten."),
    ("Skriftligt kostnadsförslag", "Gatusida och gårdssida redovisas separat, så att styrelsen kan ta dem i den ordning den vill."),
    ("Underlag till ansökan", "Behövs lov tar vi fram dagens material och kulörer som grund för beskrivningen i NCS."),
    ("Lagning och dekor", "Puts lagas med bruk som passar det befintliga, och dekoren kompletteras efter befintlig profil."),
    ("Avfärgning och plåt", "Fasaden avfärgas, plåt på lister och takfot ses över och ställningen monteras ner."),
  ],
  "rot_h2": "ROT-avdrag vid fasadrenovering på Östermalm",
  "rot": [
    "En fasadrenovering i ett flerbostadshus beställs av föreningen eller fastighetsägaren. Skatteverket räknar fasader till de gemensamma ytorna och ger därför inget rotavdrag till bostadsrättshavarna, och inte heller för tilläggsisolering eller för ställning på utsidan av bostaden.",
    "Äger du själv ett småhus räknas att byta, mura, reparera och måla fasader som rotarbete. Avdraget är högst 30 procent av arbetskostnaden, som mest 50 000 kr per person och år och 75 000 kr ihop med rutavdrag, och det gäller arbetad tid på plats, inte material eller resor. Vi drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Östermalm?",
  "price": [
    "Fasadens höjd och yta, mängden dekor som ska lagas, om stenpartier behöver åtgärdas, hur mycket plåt som ska bytas och om gatusidan kräver lov styr kostnaden mest. Efter ett gratis platsbesök får styrelsen ett skriftligt kostnadsförslag där gatufasad och gårdsfasad står var för sig.",
  ],
  "faq": [
    ("Behöver föreningen bygglov för att ändra gårdsfasaden på ett flerbostadshus?",
     "Det beror på. I Stockholm krävs lov för fasadändringar mot allmän plats, medan ändringar som inte vetter mot allmän plats kan vara lovfria om vissa förutsättningar är uppfyllda – till exempel att ingen utökad lovplikt gäller."),
    ("Vad betyder gul klass för en fasad på Östermalm?",
     "Översiktsplanen kallar gul klass en relativt låg klassificering, ofta därför att huset har förändrats. Vid prövning i stenstaden ska ändå betydelsen för stadsmiljön vara avgörande."),
    ("Hur ska kulören anges när fasaden ska få ny färg?",
     "Stockholms stad vill att kulörerna i material- och kulörbeskrivningen anges enligt NCS-systemet."),
    ("Vilka delar av en gatufasad pekar översiktsplanen ut som värdebärande?",
     "Uppdelningen i sockelvåning och huvudfasad, oftast med markerad takfot och ibland en attikavåning, samt byggnadsdetaljeringen."),
    ("Får en särskilt värdefull fasad ändras om ändringen är lovfri?",
     "Plan- och bygglagen förbjuder att en särskilt värdefull byggnad förvanskas, och varsamhetskravet gäller vid all ändring – oavsett om åtgärden kräver lov."),
  ],
  "sources": [_OP_RIKS, _SB_FAS, _PBL, _OF_HEDV, _SKV, _SKV2],
  "cta": ("Ska föreningens gatufasad eller gårdsfasad renoveras?", "Boka ett gratis platsbesök, så går vi igenom båda sidorna och lämnar ett skriftligt kostnadsförslag till styrelsen."),
  "img": [
    ("Stenstadshus i fem våningar med dekorerad putsfasad, sockelvåning och markerad takfot vid en esplanad",
     "late 19th century five-storey apartment building on a tree-lined Stockholm boulevard, richly decorated rendered facade in warm beige with stone-look rusticated ground floor, cornice and attic storey, tall windows with ornamented surrounds, autumn trees, empty street early on a Sunday morning, no pedestrians, no cars, no traffic signs, daylight, realistic photo, no people, no text, no letters"),
    ("Enkel slätputsad gårdsfasad med raka fönsterrader och ställning mot innergården",
     "plain smooth rendered courtyard facade of an old Stockholm apartment building, simple rows of windows without ornament, light grey render with a few repaired patches, scaffolding standing in the inner courtyard on gravel, realistic photo, no people, no text, no letters"),
    ("Putsad villa i klassicerande stil indragen bakom förgård med smidesstaket",
     "detached late 1800s rendered villa in restrained classical style set back from the street behind a planted front garden, low stone wall with wrought iron fence, pale ochre render, white window surrounds, Stockholm inner city, daylight, realistic photo, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VASASTAN
"fasadrenovering-vasastan.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Vasastan", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Vasastan – ställningen mot gatan",
  "description": "Fasadrenovering i Vasastan: ställning på trottoaren kräver polistillstånd, bodar och containrar kan kräva lov – så planerar vi gatufasaden och gården.",
  "h1": "Fasadrenovering i Vasastan",
  "lead": "I Vasastan står husen i gatuliv, så ställningen till en gatufasad hamnar på trottoaren. Det kräver tillstånd innan första röret kommer på plats. Geal Entreprenad AB renoverar fasader i Vasastan åt bostadsrättsföreningar och fastighetsägare och planerar etableringen på gatan lika noga som själva putsarbetet.",
  "card": "Ställning, tillstånd och etablering på gatan.",
  "sections": [
    {"id": "gatuliv-vasastan", "anchor": "Husen i gatuliv",
     "h2": "Sammanbyggda hus i gatuliv",
     "paras": [
       "Översiktsplanen räknar Norrmalm till den klassiska stenstaden från 1870–1930 och beskriver en småskalig fastighetsindelning med sammanbyggda fasader i gatuliv och kringbyggda gårdar. I norra Vasastaden pekar planen ut kvarteren Motorn och Vingen, som uppfördes i slutet av 1910-talet som ett tidigt exempel på kooperativt byggande med kommunalt stöd. I sådana kvarter står gatufasaden direkt mot trottoaren, utan förgård att ställa upp ställningen på, och planen anger 18 meter som stenstadens typiska gatubredd – en bredd som ska delas mellan körbana, trottoar, gående och ställning.",
       "Det är också lägenheter som dominerar. Enligt stadens områdesfakta 2025 har Västra Matteus 12 579 bostäder, varav 8 990 bostadsrätter, och Östra Matteus 7 680 bostäder, varav 5 593 bostadsrätter. Ingen av stadsdelarna har en enda bostad i småhus. Fasadrenoveringen blir med andra ord ett projekt för föreningen eller fastighetsägaren, där styrelsen eller ägaren beslutar och betalar.",
     ],
     "aside": {"title": "Bostäder 2025", "items": [
       "Västra Matteus: 12 579", "varav 8 990 bostadsrätter", "Östra Matteus: 7 680", "Inga småhus i någon av dem"]}},
    {"id": "tillstand-vasastan", "h2": "Polistillstånd för ställning, container och bodar",
     "paras": [
       "Stockholms stad skriver att den som behöver använda offentlig plats för byggverksamhet ska söka polistillstånd. Tillståndet måste vara utfärdat innan platsen tas i bruk och ska omfatta allt som ställs dit under hela tiden. Det gäller bland annat byggställningar, containrar, arbetsbodar, mobilkranar, byggsäckar, byggskyltar och tillfartsområdet till etableringen. Behövs en upplagsplats för ställningsmaterial när ställningen monteras upp och ner, ska även den ingå i tillståndet.",
       "Stadens villkor för en tillgänglighetsanpassad byggställning innebär bland annat att minst 1,6 meter ska vara fritt under ställningen eller att minst 2 meter finns kvar för gående på gångbanan. Polisen tar en administrationsavgift för varje ansökan, och staden tar ut en avgift för att platsen används, beroende på vilken avgiftszon gatan ligger i. Byggskylten får vara högst 15 kvadratmeter per projekt. Själva bygglovet är en separat fråga: enligt staden kan det behövas bygglov för byggbodar, container, byggplank, upplag och skyltar, medan ett glest byggstängsel inte kräver lov.",
       "Avgiften för en byggetablering räknas per kvadratmeter och år. Vid en kortare etablering betalas den som en engångskostnad när polistillståndet har kommit, vid en längre faktureras den varje kvartal. Sedan den 1 maj 2021 går det enligt staden inte längre att få reducerad upplåtelseavgift för en byggetablering. Hur länge ställningen står på gatan påverkar alltså föreningens kostnad, och därför lägger vi upp arbetsordningen så att gatusidan blir klar så fort det går.",
     ],
     "aside": {"title": "Kräver polistillstånd på gatan", "items": [
       "Byggställning och ställningsupplag", "Container och byggsäckar", "Arbetsbod", "Tillfart till etableringen"]}},
    {"id": "gard-vasastan", "h2": "Gården, föreningens mark och underhållsplanen",
     "paras": [
       "Staden råder att byggetableringen placeras i anslutning till arbetsplatsen och på egen fastighet om det går. Mot gården kan ställningen ofta stå på föreningens egen fastighet, men ligger etableringen på någon annans mark behövs enligt staden fastighetsägarens tillstånd. Vi lägger därför gärna upp arbetet så att material, container och bod ryms på gården, medan gatusidan bara får den ställning som krävs för just den fasaden. Ändras fasaden mot gatan – till exempel med ny kulör eller nytt material – krävs dessutom bygglov för ett flerbostadshus, eftersom den vetter mot allmän plats.",
       "Bostadsrättslagen säger att föreningen ska hålla huset i gott skick, i den mån ansvaret inte ligger på bostadsrättshavaren. Lagen kräver också att den ekonomiska plan som upprättas innan en förening upplåter lägenheter innehåller en teknisk underhållsplan för fastighetens behov de kommande 50 åren. Finns fasaden med i en sådan plan kan tillståndsfrågan på gatan förberedas i god tid. Om målning inne i lägenheten, se " + _L.format("malare-vasastan.html", "målare i Vasastan") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi en fasad i Vasastan",
  "steps": [
    ("Platsbesök", "Vi går igenom gatufasaden och gårdsfasaden och mäter trottoarens bredd utanför huset."),
    ("Etableringsplan", "Ställning, upplag, container och bod placeras på ritning – så mycket som möjligt på gården."),
    ("Skriftligt kostnadsförslag", "Ställning, lagning, avfärgning och plåt redovisas var för sig."),
    ("Tillstånd", "Polistillstånd för gatusidan och eventuellt bygglov för bod eller container söks innan arbetet startar."),
    ("Fasadarbetet", "Puts lagas och avfärgas, och plåt på lister och fönsterbleck ses över."),
    ("Nedmontering", "Ställningen monteras ner och gatan lämnas tillbaka i det skick tillståndet kräver."),
  ],
  "rot_h2": "ROT-avdrag vid fasadrenovering i Vasastan",
  "rot": [
    "I Västra och Östra Matteus finns inga småhus, så där är det en förening eller fastighetsägare som beställer fasadarbetet. Skatteverket räknar fasader till de gemensamma ytorna i en bostadsrättsförening, och arbete där ger inget rotavdrag. Det gäller också att montera upp eller ned en byggnadsställning på utsidan av bostaden.",
    "Rotavdraget gäller bara arbetskostnaden för arbete i eller i nära anslutning till en bostad som du själv äger och bor i. Kostnader för material, resor, utrustning eller administration ger enligt Skatteverket inget avdrag.",
  ],
  "price_h2": "Vad påverkar priset i Vasastan?",
  "price": [
    "Fasadens höjd och längd mot gatan, hur länge ställningen behöver stå, om etableringen ryms på gården, hur stor del av putsen som ska lagas och hur mycket plåt som byts styr kostnaden. Efter ett gratis platsbesök får styrelsen ett skriftligt kostnadsförslag där ställning och etablering står för sig.",
  ],
  "faq": [
    ("Behövs polistillstånd för en byggställning på trottoaren?",
     "Ja. Stockholms stad skriver att byggställningar på offentlig plats kräver polistillstånd, och att tillståndet måste vara utfärdat innan platsen börjar användas."),
    ("Hur mycket plats måste ställningen lämna åt fotgängare?",
     "Enligt stadens villkor för tillgänglighetsanpassad byggställning ska minst 1,6 meter vara fritt under ställningen eller minst 2 meter vara kvar för gående på gångbanan."),
    ("Behöver containern på gatan bygglov?",
     "Den kan behöva det. Staden skriver att det kan krävas bygglov för att ställa upp en container, och på stadens mark krävs dessutom polistillstånd."),
    ("Var ska ställningsmaterialet ligga när ställningen monteras?",
     "Behövs en upplagsplats på offentlig plats vid upp- och nedmontering ska den enligt staden ingå i polistillståndet."),
    ("Måste en bostadsrättsförening ha en underhållsplan för fasaden?",
     "Bostadsrättslagen kräver att den ekonomiska planen innehåller en teknisk underhållsplan för de kommande 50 åren. Kravet gäller planen som upprättas innan föreningen upplåter lägenheter."),
  ],
  "sources": [_TL_BYGG, _SB_BOD, _SB_FAS, _OP_RIKS, _OF_VM, _OF_OM, _BRL, _SKV, _SKV2],
  "cta": ("Ska föreningens gatufasad renoveras?", "Boka ett gratis platsbesök, så planerar vi ställning och etablering och lämnar ett skriftligt kostnadsförslag till styrelsen."),
  "img": [
    ("Byggställning med arbetsplan längs en putsad gatufasad",
     "low-angle view from the sidewalk looking up along a steel facade scaffold with plain unprinted white protective netting on an early 1900s rendered apartment building, covered pedestrian passage with a plank roof left open under the scaffold, only the scaffolded wall and grey sky in the frame, no shopfronts, no plaques, daylight, realistic photo, no people, no text, no letters, no signs"),
    ("Ställningsfot och gångtunnel under en fasadställning på en trottoar",
     "close-up of scaffold base plates and a protective walkway tunnel beneath facade scaffolding on a city sidewalk, wooden planks overhead, smooth asphalt, stone apartment building plinth beside, realistic photo, no people, no text, no letters, no signs"),
    ("Innergård i stenstaden med container och ställningsmaterial uppställt intill gårdsfasaden",
     "inner courtyard of an old Stockholm apartment block, small construction container and neatly stacked scaffold tubes and planks next to a plain rendered courtyard facade, cobblestone ground, birch tree, realistic photo, no people, no text, no letters, no signs"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ KUNGSHOLMEN
"fasadrenovering-kungsholmen.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Kungsholmen", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering på Kungsholmen – funkishusens puts",
  "description": "Fasadrenovering på Kungsholmen: slätputsen på funkishusen i Fredhäll och Kristineberg – bruket, fukten, tilläggsisolering och lov mot allmän plats.",
  "h1": "Fasadrenovering på Kungsholmen",
  "lead": "På ett funkishus finns ingen dekor att gömma lagningarna bakom. Putsen är själva arkitekturen, och varje fläck med fel struktur syns på långt håll. Geal Entreprenad AB renoverar putsfasader på Kungsholmen åt bostadsrättsföreningar och fastighetsägare, från funkishusen i Fredhäll och Kristineberg till stenstadens kvarter.",
  "card": "Slätputs på funkishus, lagad utan synliga skarvar.",
  "sections": [
    {"id": "funkis-kungsholmen", "anchor": "Funkisputsen",
     "h2": "Putsen som bär funkishusens uttryck",
     "paras": [
       "Omkring 1930 började, enligt stadens översiktsplan, en ny typ av stadsdelar byggas utifrån funktionalismens stilideal. I innerstaden uppfördes de framför allt i utkanterna, och planen nämner Fredhäll och Kristineberg bland exemplen. Idealet var fristående huskroppar med öppna, gröna gårdar – inte slutna kvarter som i stenstaden.",
       "Stockholms läns museum beskriver hur putsen blev mycket populär under funktionalismen på 1930-talet, och att den på 1930- och 40-talets funkishus är en viktig del av arkitekturen. Den släta putsen kan antingen följa murens yta eller dölja ojämnheter i underlaget, medan spritputs innehåller grus eller sten som ger ytan karaktär. Traditionellt görs puts av kalk, sand och vatten, kalkputs eller k-bruk. Efter 1940-talet började man enligt museet tillsätta cement för att göra putsen starkare, kc-bruk, med nackdelen att skiktet blev mindre elastiskt i förhållande till underlaget. Vilket bruk ett enskilt hus har går därför inte att gissa sig till av årtalet – vi tar prov innan vi väljer lagningsbruk.",
     ],
     "aside": {"title": "Putsen enligt museet", "items": [
       "Populär under 1930-talets funktionalism", "Slätputs eller spritputs", "K-bruk: kalk, sand och vatten",
       "Kc-bruk: cement tillsatt efter 1940-talet"]}},
    {"id": "fukt-kungsholmen", "h2": "Fukten, isoleringen och anslutningarna",
     "paras": [
       "Boverket skriver att de vanligaste skadorna på putsade fasader är sprickor och putsbortfall, och att putsbortfall i de allra flesta fall beror på fukt. Kalkputs kan suga upp, transportera och avge fukt utan att stommen skadas, men får putsen för stor fuktbelastning uppstår skador, och fuktig puts kan frysa sönder om fukten blir kvar över vinterhalvåret. Där stuprör är infästa och där fasaden ansluter mot fönster och dörrar behövs enligt Boverket tätning i mer än en nivå, så kallad tvåstegstätning, om detaljerna utsätts för slagregn.",
       "Tilläggsisolering är en åtgärd att väga noga på ett putsat hus. Boverket konstaterar att en tjockare isolering gör att mindre värme läcker ut i ytterväggen, så att väggens yttre delar blir kallare – och att putsade fasader då kan få svårt att torka ut och skadas. I sin energiguide varnar Boverket också för att fönster och dörrar kan hamna längre in i fasaden och takfoten skjuta ut mindre, men nämner exempel på putsade funkishus där takfot, sockel och entréns skärmtak byggts på och fönster och dörrar flyttats ut så att det yttre utseendet är oförvanskat. Stockholms stad räknar tilläggsisolering som en fasadändring, och för ett flerbostadshus krävs bygglov när ändringen görs på en fasad som vetter mot allmän plats.",
     ],
     "aside": {"title": "Där vattnet kommer in", "items": [
       "Infästningar för stuprör", "Anslutningar mot fönster och dörrar", "Sockeln", "Sprickor som inte har lagats"]}},
    {"id": "forening-kungsholmen", "h2": "Fristående hus med flera fasader mot allmän plats",
     "paras": [
       "I stenstaden är det i regel bara gatufasaden som vetter mot allmän plats. Ett fristående funkishus kan i stället ha både gata, park och gångväg runt sig, och då kan fler sidor av huset omfattas av lovplikten. Allmän plats är enligt plan- och bygglagen en gata, en väg, en park, ett torg eller ett annat område som enligt en detaljplan är avsett för ett gemensamt behov. Detaljplanen finns enligt staden i e-tjänsten Bygg- och plantjänsten, och fasadändringar som inte kräver lov ska ändå stämma med planen. Vi går därför igenom planen innan föreningen bestämmer kulör eller material.",
       "Det är också föreningen som beslutar. Bostadsrättslagen säger att föreningen ska hålla huset i gott skick, i den mån ansvaret inte vilar på bostadsrättshavaren. Enligt stadens områdesfakta 2025 har Fredhäll 3 830 bostäder, varav 2 219 bostadsrätter, och inte ett enda småhus. Kristineberg har 4 598 bostäder, varav 3 243 bostadsrätter, och ett småhus. I hela Kungsholmens stadsdelsområde fanns 2024 337 bostäder i småhus av totalt 44 554, och 272 av dem var äganderätter. Om fönstren i samma fasad, se " + _L.format("fonsterrenovering-kungsholmen.html", "fönsterrenovering på Kungsholmen") + ", och om målning inne i lägenheten " + _L.format("malare-kungsholmen.html", "målare på Kungsholmen") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi en putsfasad på Kungsholmen",
  "steps": [
    ("Genomgång", "Vi går runt huset, knackar på putsen och noterar sprickor, bom och missfärgade partier."),
    ("Prov på putsen", "Ett prov visar om det är kalkputs eller kalkcementputs och vilken struktur ytan har."),
    ("Detaljplanen", "Vi tar reda på vilka fasader som vetter mot allmän plats och om lov behövs."),
    ("Skriftligt kostnadsförslag", "Lagning, omputsning, avfärgning och anslutningar redovisas var för sig."),
    ("Lagning i hela fält", "Lös puts tas ner och ytan putsas om till naturliga gränser, så att skarvarna inte syns."),
    ("Avfärgning och kontroll", "Fasaden avfärgas med en färg som släpper igenom fukt, och anslutningarna kontrolleras."),
  ],
  "rot_h2": "ROT-avdrag vid fasadrenovering på Kungsholmen",
  "rot": [
    "För en bostadsrättshavare ger fasadrenoveringen inget rotavdrag: Skatteverket räknar fasader till de gemensamma ytorna, och tilläggsisolering och ställning på utsidan av bostaden ger inte heller avdrag i en bostadsrätt.",
    "Äger du ett av Kungsholmens småhus räknas att byta, mura, reparera och måla fasader som rotarbete. Avdraget är högst 30 procent av arbetskostnaden, med taket 50 000 kr per person och år och 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag, och vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Kungsholmen?",
  "price": [
    "Fasadens yta och höjd, hur stora fält som måste putsas om för att lagningarna inte ska synas, om anslutningar vid fönster och stuprör ska göras om och vilken färgtyp putsen kräver styr kostnaden. Efter ett gratis platsbesök får styrelsen ett skriftligt kostnadsförslag med varje moment för sig.",
  ],
  "faq": [
    ("Varför syns lagningar så tydligt på ett slätputsat funkishus?",
     "Putsen är en viktig del av funkishusens arkitektur, och den släta ytan saknar dekor som döljer skarvar. Därför putsar vi om till naturliga gränser i stället för att laga små fläckar."),
    ("Hur vet man om ett hus från 1930-talet har kalkputs?",
     "Det får man veta genom ett prov. Stockholms läns museum skriver att cement började tillsättas efter 1940-talet, men senare lagningar kan ha gjorts med annat bruk."),
    ("Kan tilläggsisolering skada en putsfasad?",
     "Boverket skriver att tjockare isolering gör väggens yttre delar kallare, så att putsade fasader kan få svårt att torka ut och skadas."),
    ("Vilka fasader på ett fristående flerbostadshus kräver bygglov vid ändring?",
     "De som vetter mot allmän plats, enligt Stockholms stad. Enligt plan- och bygglagen är allmän plats till exempel en gata, en park eller ett torg som i detaljplanen är avsett för ett gemensamt behov."),
    ("Vad är tvåstegstätning vid en fasad?",
     "Tätning i mer än en nivå vid anslutningar och infästningar, till exempel stuprör och fönster. Boverket beskriver den som ett sätt att hindra slagregn från att tränga djupare in i väggen."),
  ],
  "sources": [_OP_RIKS, _SLM_P, _BV_FMAT, _BV_ISOL, _SB_FAS, _PBL_AP, _BRL, _OF_FRED, _OF_KRIST, _OF_KUNGS, _SKV, _SKV2],
  "cta": ("Har putsen släppt på föreningens funkishus?", "Boka ett gratis platsbesök, så tar vi prov på putsen och lämnar ett skriftligt kostnadsförslag till styrelsen."),
  "img": [
    ("Ljust slätputsat funkishus från 1930-talet med fönsterband och öppen gräsgård",
     "1930s functionalist apartment block in Stockholm, smooth light cream render, long rows of horizontal windows and small cantilevered balconies with thin metal railings, standing freely in an open green lawn with pine trees, daylight, realistic photo, no people, no text, no letters"),
    ("Stuprörsinfästning och fönsteranslutning på en slätputsad fasad med fuktskadad puts",
     "close-up of a smooth rendered functionalist facade with a metal downpipe bracket fixed into the render, flaking and cracked render around the bracket and below a window sill, dark damp patch, realistic photo, no people, no hands, no text, no letters"),
    ("Fristående funkishus mellan gata och park med ställning på ena gaveln",
     "freestanding 1930s functionalist apartment building between a quiet street and a park path, scaffolding on one gable end during render repair, pale rendered walls, birch trees, daylight, realistic photo, no people, no text, no letters, no signs"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SUNDBYBERG
"fasadrenovering-sundbyberg.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Sundbyberg", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Sundbyberg – Duvbos villafasader",
  "description": "Fasadrenovering i Sundbyberg: panel och puts på Duvbos villor från tre epoker, den utökade lovplikten och vad som gäller för stadens flerbostadshus.",
  "h1": "Fasadrenovering i Sundbyberg",
  "lead": "En villa i Duvbo kan ha fält av fasspontpanel, locklistpanel eller slätputs beroende på när den byggdes. Det avgör hur fasaden ska renoveras – och i Duvbo krävs lov för det mesta. Geal Entreprenad AB renoverar fasader i Sundbyberg, både på villorna i Duvbo och på stadens flerbostadshus.",
  "card": "Panel och puts på Duvbos villor.",
  "sections": [
    {"id": "duvbo-sundbyberg", "anchor": "Duvbo",
     "h2": "Tre generationer fasader i Duvbo",
     "paras": [
       "Sundbybergs miljöprogram för Duvbo berättar att föreningen Egna Hem bildades 1898 för att skapa egna hem för arbetare. Året därpå köptes egendomen Dufvebol i Spånga församling, och en stadsplan med 325 tomter upprättades. Området utökades 1924 med ytterligare 98 villatomter, och Riksantikvarieämbetet pekade 1987 ut Duvbo som riksintresse för kulturmiljövården – som ett av de första exemplen på en välorganiserad egnahemsförstad i Stockholmstrakten.",
       "Programmet delar in den äldre bebyggelsen i tre generationer med olika fasader. Sekelskiftesvillorna i schweizerstil har stående och liggande fasspontpanel indelad i fält med listverk, höga socklar i natursten och heltäckande linoljefärg eller faluröd slamfärg, och gott om lövsågerier. 1920-talets egnahem har locklistpanel, ibland puts, med markerade knutar, putsade socklar och klassicerade detaljer. Husen från 1940-talet är funktionalistiska, med slätputs, putsade socklar, få och enkla detaljer och kalkfärg i ljusa kulörer. I programmets tabell har alla tre generationerna tak av rött lertegel, sekelskiftesvillorna även falsad slätplåt eller papp.",
       "Både sekelskiftesvillorna och 1920-talets hus står enligt programmet i två våningar på höga, nivåutjämnande socklar, och träfasaderna målades ursprungligen med linoljefärg eller slamfärg i tidstypiska, jordnära färgskalor. Sekelskiftesvillorna byggdes ofta av ägarna själva och visar en rik provkarta på tidens smakriktningar – två grannhus kan alltså ha helt olika panelindelning. När en bräda eller ett fält ska bytas tar vi därför mått och profil från det egna huset, inte från grannens.",
     ],
     "aside": {"title": "Fasaderna enligt programmet", "items": [
       "Sekelskiftet: fasspontpanel i fält", "1920-talet: locklistpanel, ibland puts",
       "1940-talet: slätputs med kalkfärg", "Höga socklar i natursten eller puts"]}},
    {"id": "lov-sundbyberg", "h2": "Utökad lovplikt för fasaden i Duvbo",
     "paras": [
       "För de flesta villor krävs inte längre bygglov för fasadändringar, men Sundbybergs stad skriver att det inte gäller i Duvbo. Där är lovplikten utökad, liksom för byggnader som är kulturhistoriskt värdefulla, och för det mesta krävs bygglov. Enligt miljöprogrammet omfattar den utökade lovplikten bland annat utbyte av fasadbeklädnad och takmaterial, omfärgning av fasaden och utbyte, flyttning eller igensättning av fönster och dörrar. Som fasadändring räknar staden också tilläggsisolering.",
       "Programmet ger även råd för själva underhållet. Vid underhållsarbeten och andra förändringar av husets yttre ska utförande, material och materialbehandling om möjligt väljas i överensstämmelse med originalet eller byggnadens tillkomsttid, och husets tidstypiska uttryck får inte förvanskas genom byte av fasadmaterial eller genom färgsättning. För färgförslag hänvisar programmet till kommunens förvaltning. Till en ansökan behövs enligt staden oftast situationsplan, plan- och fasadritning, kulör- och materialbeskrivning och kontrollplan. Krävs inget lov kan den som vill söka ett så kallat frivilligt bygglov, för att få beslut på att åtgärden följer lagens krav.",
     ],
     "aside": {"title": "Kräver lov i Duvbo", "items": [
       "Ny fasadbeklädnad", "Ny kulör på fasaden", "Byte eller flytt av fönster och dörrar", "Tilläggsisolering"]}},
    {"id": "flerbostadshus-sundbyberg", "h2": "Flerbostadshusen i resten av Sundbyberg",
     "paras": [
       "För stadens flerbostadshus gäller en annan regel än för villorna. För byggnader som inte är en- eller tvåbostadshus kräver Sundbybergs stad bygglov när ändringen görs på fasad eller tak som vetter mot allmän plats. Påverkar arbetet väsentligt byggnadens bärande delar eller brandskydd kan dessutom en anmälan krävas, även när åtgärden inte är lovpliktig, och då ska startbesked ha getts innan arbetet börjar.",
       "Staden påminner också om att byggherren ansvarar för att lagstiftningen följs även när en fasadändring inte kräver lov eller anmälan, bland annat för att det som byggs är lämpligt utformat och att kraven på säkerhet uppfylls. Vi tar fram kulör- och materialbeskrivning och ritningsunderlag när det behövs, och samordnar fasadarbetet med plåt och tak. Mer om andra arbeten i staden finns under " + _L.format("malare-sundbyberg.html", "målare i Sundbyberg") + ", " + _L.format("snickare-sundbyberg.html", "snickare i Sundbyberg") + " och " + _L.format("taklaggare-sundbyberg.html", "takläggare i Sundbyberg") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi en fasad i Sundbyberg",
  "steps": [
    ("Platsbesök", "Vi går igenom panel eller puts, socklar och knutar och bestämmer husets tillkomsttid."),
    ("Lovfrågan", "I Duvbo stämmer vi av lovplikten innan material eller kulör väljs."),
    ("Skriftligt kostnadsförslag", "Lagning, byte av panel, puts och målning redovisas var för sig."),
    ("Ansökan", "Behövs lov tar vi fram kulör- och materialbeskrivning och underlag till ritningarna."),
    ("Renovering", "Panel byts med samma profil och indelning, och puts lagas med bruk som passar det gamla."),
    ("Ytbehandling", "Linoljefärg, slamfärg eller kalkfärg efter vad huset hade från början."),
  ],
  "rot_h2": "ROT-avdrag vid fasadrenovering i Sundbyberg",
  "rot": [
    "Äger du en villa i Duvbo räknar Skatteverket att byta, mura, reparera och måla fasader som rotarbete, liksom att montera och montera ner byggnadsställningar i samband med arbetet. Avdraget är högst 30 procent av arbetskostnaden, som mest 50 000 kr per person och år och 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag. Vi drar avdraget direkt på fakturan.",
    "Bor du i en bostadsrätt i ett av stadens flerbostadshus är fasaden en gemensam yta, och arbete där ger inget rotavdrag.",
  ],
  "price_h2": "Vad påverkar priset i Sundbyberg?",
  "price": [
    "Fasadens yta, hur mycket panel eller puts som måste bytas, om listverk och lövsågerier ska kompletteras, vilken färgtyp huset kräver och om ett bygglov behöver förberedas styr kostnaden. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Krävs bygglov för att måla om en villa i Duvbo i ny kulör?",
     "Ja. Miljöprogrammet räknar omfärgning av fasaden till den utökade lovplikten i Duvbo."),
    ("Vilken panel hade sekelskiftesvillorna i Duvbo?",
     "Stående och liggande fasspontpanel indelad i fält med listverk, enligt stadens miljöprogram."),
    ("Hur var 1940-talets villor i Duvbo putsade och målade?",
     "Med slätputs, putsade socklar och kalkfärg i ljusa kulörer, enligt miljöprogrammet."),
    ("Vad är ett frivilligt bygglov?",
     "Ett lov som du kan söka även när åtgärden inte kräver bygglov. Beslutet ger dig besked om att det du planerar följer lagens krav, skriver Sundbybergs stad."),
    ("När pekades Duvbo ut som riksintresse?",
     "Riksantikvarieämbetet pekade ut området som riksintresse för kulturmiljövården 1987, enligt stadens miljöprogram."),
  ],
  "sources": [_SBG_DUVBO, _SBG_FAS, _SKV, _SKV2],
  "cta": ("Ska fasaden på villan i Duvbo renoveras?", "Boka ett gratis platsbesök, så går vi igenom panel och puts och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Sekelskiftesvilla i Duvbo med fasspontpanel indelad i fält och rött tegeltak",
     "Swedish turn-of-the-century two-storey wooden villa in Swiss chalet style, facade divided into fields of vertical and horizontal tongue-and-groove panelling with trim boards, high natural stone plinth, decorative fretwork on gables, red clay tile roof, mature garden with fruit trees, daylight, realistic photo, no people, no text, no letters"),
    ("Hörn på en villa med locklistpanel, markerade knutbrädor och putsad sockel",
     "close-up of the corner of a 1920s Swedish wooden house with board-and-batten cladding, wide painted corner boards, rendered plinth below, light ochre linseed oil paint, a few new primed battens fitted, daylight, realistic photo, no people, no hands, no text, no letters"),
    ("Putsat flerbostadshus i ljus kulör med ställning längs gatufasaden",
     "mid-century Swedish three-storey rendered apartment building in a light warm colour, scaffolding along the street facade during facade renovation, small balconies, trees along the pavement, daylight, realistic photo, no people, no text, no letters, no signs"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ VÄLLINGBY
"fasadrenovering-vallingby.html": {
  "kind": "district", "service": "fasadrenovering", "ort": "Vällingby", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Vällingby – tegel, puts och skivor",
  "description": "Fasadrenovering i Vällingby: tegel, puts och fibercementskivor – vad som slits, asbest i gamla skivor och när ett materialbyte kräver lov.",
  "h1": "Fasadrenovering i Vällingby",
  "lead": "Tegelfasaden på ett hus i Vällingby behöver sällan mer än översyn, men allt runt den åldras: plåtar, anslutningar och de skivor som ofta sitter bredvid. Geal Entreprenad AB renoverar fasader i Vällingby på radhus, kedjehus och flerbostadshus och väljer åtgärd efter materialet på just den delen av väggen.",
  "card": "Tegel, puts och skivor på tunnelbanestadens hus.",
  "sections": [
    {"id": "material-vallingby", "anchor": "Fasadmaterialen",
     "h2": "Tegel, puts och fibercement i tunnelbanestaden",
     "paras": [
       "Stadens vägledning för småhusområden beskriver tunnelbanestäderna som en blandning av för tiden mycket moderna idéer och det mer traditionella folkhemsidealet. Fasader i rött tegel var vanligt, men det förekom även puts och skivor i fibercement. Byggnadstekniken blev alltmer industrialiserad men gav ändå stort utrymme för terränganpassning. Utformning och materialval varierar mellan områdena, och vägledningen nämner tidstypisk färgsättning bland karaktärsdragen.",
       "I översiktsplanens beskrivning av riksintresset Vällingby räknas de ursprungliga husens gestaltning och byggnadsdetaljer som fönster, entrépartier, balkonger och räcken till de värdebärande karaktärsdragen, liksom centrumanläggningarnas omsorg om form-, färg- och materialverkan. En fasadrenovering här handlar alltså lika mycket om att behålla materialens samspel som om att laga det som är skadat. Stadens områdesfakta 2025 räknar 449 bostäder i småhus i stadsdelen Vällingby, varav 228 bostadsrätter och 220 äganderätter, och 3 891 bostäder i flerbostadshus och övriga hus.",
     ],
     "aside": {"title": "Vällingby 2025", "items": [
       "449 bostäder i småhus", "varav 220 äganderätter", "och 228 bostadsrätter", "3 891 i flerbostadshus och övriga hus"]}},
    {"id": "tegel-vallingby", "h2": "Teglet håller – detaljerna runt det åldras",
     "paras": [
       "Stockholms läns museum beskriver tegel som ett keramiskt naturmaterial av lera som bränns i mycket hög temperatur och som i stort sett kan beskrivas som underhållsfritt. Är fasaden rätt skyddad mot snö och regn, genom tillräckliga taksprång, kan den enligt museet hålla i evighet. Lera rik på järnoxid ger rött tegel, kalkrik lera gult. Teglet muras i förband så att muren hålls samman, med liggfogar horisontellt och stötfogar vertikalt. Museet påpekar också att mexitegel inte är tegel utan en blandning av kalk, sand och krossad sandsten.",
       "Det som slits på en tegelfasad är därför sällan stenen. Boverket påminner om att alla fasader har anslutnings- och infästningsdetaljer – stuprörens infästningar, anslutningar mot fönster och dörrar – och att de kräver tätning i mer än en nivå när de utsätts för slagregn. Fuktskador kan också uppstå om fasadens ytskikt fuktas upp och inte hinner torka ut tillräckligt fort. Vid en fasadrenovering i Vällingby går vi därför igenom fogarna, fönsterblecken, plåtarna vid takfoten och övergångarna mellan tegel, puts och skivor innan vi föreslår något.",
     ],
     "aside": {"title": "Det vi kontrollerar", "items": [
       "Fogar i tegelmuren", "Fönsterbleck och anslutningar", "Takfot och taksprång", "Övergångar mellan material"]}},
    {"id": "skivor-vallingby", "h2": "Gamla skivor och när ett materialbyte kräver lov",
     "paras": [
       "Boverket skriver att många fasader under 1940- och 1950-talen kläddes med cementfiberplattor som innehöll asbestfibrer. Plattorna är nästan underhållsfria så länge de inte skadas, men fibrerna kan frigöras vid bearbetning, till exempel när man borrar i dem. Ska sådana skivor rivas krävs enligt Arbetsmiljöverket tillstånd för företaget som utför arbetet, och förarbetet på platsen, omhändertagandet av avfallet och städningen efteråt räknas också som rivning och sanering. Tillståndet ska sökas åtta veckor innan arbetet påbörjas.",
       "Byte av material eller kulör på fasaden räknar Stockholms stad som fasadändring, och tilläggsisolering likaså. För ett en- eller tvåbostadshus krävs i regel inte längre lov, men inom ett riksintresse för kulturmiljövården – som visas med blå ring i Stadsmuseets klassificeringskarta – krävs bygglov även för åtgärder som annars är lovfria. Vällingby–Råcksta är utpekat som ett sådant riksintresse. Om ommålning av puts, se " + _L.format("fasadmalning-vallingby.html", "fasadmålning i Vällingby") + ", och om plåt vid takfot och fönster " + _L.format("platslagare-vallingby.html", "plåtslagare i Vällingby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi en fasad i Vällingby",
  "steps": [
    ("Platsbesök", "Vi går igenom tegel, puts och skivor och noterar vilka delar av väggen som är skadade."),
    ("Materialprov", "Misstänkta asbestskivor provtas innan något bearbetas."),
    ("Klassning och lov", "Vi kontrollerar Stadsmuseets karta och om åtgärden kräver lov i riksintresset."),
    ("Skriftligt kostnadsförslag", "Fogning, plåt, puts och skivor redovisas var för sig."),
    ("Renovering", "Fogar och anslutningar görs om, och skadade skivor ersätts med material som behåller uttrycket."),
    ("Avslutning", "Plåt och bleck monteras, ställningen tas ner och vi går igenom fasaden tillsammans."),
  ],
  "rot_h2": "ROT-avdrag vid fasadrenovering i Vällingby",
  "rot": [
    "Äger du radhuset eller villan räknar Skatteverket att byta, mura, reparera och måla fasader som rotarbete, och att sanera asbest i samband med byggarbete. Avdraget är högst 30 procent av arbetskostnaden, som mest 50 000 kr per person och år och 75 000 kr tillsammans med rutavdrag. Material och resor ger inget avdrag, och vi drar avdraget direkt på fakturan.",
    "Är radhuset en bostadsrätt hör fasaden till de gemensamma ytorna, och då ger fasadarbetet inget rotavdrag. Att mäta asbest ger inte heller avdrag, varken i småhus eller bostadsrätt.",
  ],
  "price_h2": "Vad påverkar priset i Vällingby?",
  "price": [
    "Fasadens yta, hur många fogar och anslutningar som behöver göras om, om asbesthaltiga skivor ska saneras, vilket ersättningsmaterial som väljs och om åtgärden kräver lov påverkar kostnaden. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver en tegelfasad underhållas?",
     "Teglet i sig kan i stort sett beskrivas som underhållsfritt, enligt Stockholms läns museum, om fasaden skyddas av tillräckliga taksprång. Vi ser därför över taksprång, fogar, plåtar och anslutningar runt fönster och stuprör."),
    ("Är mexitegel samma sak som tegel?",
     "Nej. Stockholms läns museum förklarar att mexitegel inte är ett tegel utan en blandning av kalk, sand och krossad sandsten."),
    ("Hur lång tid före rivning av asbestskivor ska tillstånd sökas?",
     "Arbetsmiljöverket anger att ansökan ska göras åtta veckor innan arbetet ska påbörjas."),
    ("Krävs bygglov för att byta fasadskivor på ett radhus i Vällingby?",
     "Byte av fasadmaterial är en fasadändring. Inom ett riksintresse för kulturmiljövården, som Vällingby–Råcksta, kräver Stockholms stad bygglov även för åtgärder som annars är lovfria."),
    ("Kan sanering av asbesthaltiga fasadskivor på ett radhus ge rotavdrag?",
     "I ett småhus ja, om saneringen görs i samband med byggarbete. Att mäta asbest ger inget avdrag, enligt Skatteverket."),
  ],
  "sources": [_VARSAM, _OP_RIKS, _OF_VALL, _SLM_T, _BV_FMAT, _AV_ASB, _SB_FAS, _SB_KLASS, _SKV, _SKV2],
  "cta": ("Ska fasaden på huset i Vällingby ses över?", "Boka ett gratis platsbesök, så går vi igenom tegel, puts och skivor och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhuslänga från 1950-talet med fasader i rött tegel och ljusa putsade partier",
     "row of 1950s Swedish terraced houses in a Stockholm suburb, facades of red brick combined with light rendered sections, regular window placement, small front gardens, pine trees on a gentle slope, daylight, realistic photo, no people, no text, no letters"),
    ("Rött fasadtegel i förband med liggfogar och stötfogar intill ett fönsterbleck",
     "close-up of a red brick facade laid in bond with horizontal and vertical mortar joints, a painted sheet-metal window sill at the top edge, some joints freshly repointed in grey mortar, daylight, realistic photo, no people, no hands, no text, no letters"),
    ("Gavel på ett kedjehus med grå fasadskivor av fibercement ovanför en tegelsockel",
     "gable end of a 1950s Swedish link house clad in flat grey fibre-cement facade boards above a red brick base, white window frame, ventilation gap visible at the bottom edge, overcast daylight, realistic photo, no people, no text, no letters"),
  ],
  "related": [],
},

}
