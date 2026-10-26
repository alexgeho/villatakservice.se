# -*- coding: utf-8 -*-
"""Attefallshus – ortsidor v20: Haninge, Huddinge, Nacka, Sollentuna, Tyresö, Österåker (2026-10-26).
Hubb: attefallshus.html (vanlig sida i generate.py, TJ_HUB["attefallshus"]). Regelartikel: attefallshus-regler.html.
Struktur som tj_v16_attefallshus.py. Tre bilder per sida (ägarändring 2026-10-26): img[0] hero 4:3, img[1] innehåll 3:2,
img[2] 3:2 som hör till sidans SISTA innehållssektion.
Rättslig ram (lagtexten på riksdagen.se läst igen 2026-10-26, lydelse lag 2025:974): PBL 1 kap. 4 § (komplementbostadshus
kompletterar ett en- eller tvåbostadshus, självständig bostad); 9 kap. 4 § inom detaljplan 30,0 m² / 4,0 m / inom tomten /
mindre byggnadsarea än huset det kompletterar / sammanlagt 45,0 m²; 9 kap. 5 § utanför 50,0 / 4,5 / 65,0; tidigare lovfria
byggnader räknas in; 9 kap. 34 § bygglov närmare än 4,5 m från gräns eller 30,0 m från järnvägsspårs mitt; 9 kap. 35 §
skriftligt grannmedgivande, vid allmän plats eller järnväg huvudmannen resp. järnvägens infrastrukturförvaltare;
9 kap. 36 § p. 1 bygglov för komplementbostadshus inom eller i anslutning till riksintresse för totalförsvaret när det
gäller flygplatser eller övnings- eller skjutfält; 9 kap. 37 § bygglov i särskilt värdefulla/skyddade områden;
PBF 6 kap. 1 § anmälan för VA, ventilation, eldstad/rökkanal.

Lokal vinkel per sida (skild från v16-orterna, hubb, regelartikel och ortens tillbyggnad-/snickare-/byggföretagssidor):
Haninge – försvarets riksintressen: Utö skjutfält (TM0010) med påverkansområde och Nåttarö, PBL 9:36, Länsstyrelsens
  påpekande att kartan saknar dem; sju riksintressen för kulturmiljön (Dalarö AB 605, Österhaningebygden AB 19, Utö AB 602,
  Ornö AB 604) och kommunens kartskikt under uppdatering; strandskydd 100–300 m; VA-anmälans handlingar; tillsyn efter
  klagomål. (byggforetag-haninge = omvandlingsområden, snickare-haninge = verandor/altan – inte upprepat.)
Huddinge – vattnet: SVOA ansvarar för spillvattennätet, två anmälningar, tillstånd enligt lokala föreskrifter för WC
  till befintligt enskilt avlopp, avloppstillståndet lämnas med anmälan, egen brunn (ansvar, krav vid flera hushåll/
  uthyrning, prov vart tredje år), handlingar när lov ändå krävs (förenklad nybyggnadskarta, marklinjer, NCS).
  (snickare-huddinge = potten/sportstugor, tillbyggnad = kulturmiljöprogrammet, byggforetag = grannar.)
Nacka – gränserna runt tomten: Saltsjöbanans villasamhällen (kulturmiljöprogrammet), 30 m från spårmitt, kommunens
  tillstånd mot kommunägd mark med checklista (<2 m undantagsvis), kulturmiljökartan lila/orange med planenlighetskrav,
  interimistiskt slutbesked vid ny villa. (byggforetag-nacka = VA/LTA, tillbyggnad-nacka = strandskydd/Storängen.)
Sollentuna – hustypen: radhus/kedjehus enligt kommunen, alternativet ytterligare bostad i villan (anmälan, brandskydd),
  de två potterna (komplementbyggnader vs tillbyggnader/skärmtak), imkanal, frivilligt bygglov och ansökans handlingar.
  (byggforetag = tomtdelning/spåret, snickare = altan/foton, tillbyggnad = på höjden.)
Tyresö – VA-anslutningen: kommunens sju steg, förbindelsepunkt, vattenmätare (alternativ 1/2, besiktning), inga
  restriktioner för avlopp/dagvatten, sluttömning, ny anläggningsavgift som nytt boende, avgift per mätare, VA-lån
  (Raksta etapp 8), dagvatten på tomten. (tillbyggnad = byggrätt omvandling, byggforetag = start-/slutbesked/översvämning.)
Österåker – användningen: gäststuga (komplementbyggnad, ej bostad) vs bostad att hyra ut (Boverkets krav), riksintressena
  Åkers kanal AB 62 och Roslags-Kulla AB 63, Österåkerskartan, k/q, kommunens checklista, Fornsök och Länsstyrelsens
  tillstånd, tillsyn/byggsanktionsavgift. (snickare = brygga/före 1920/Roslagsbanan, tillbyggnad = grannmedgivande.)

Fakta endast från källorna i respektive 'sources', öppnade med curl (UA Mozilla) och lästa 2026-10-26 – alla svarade 200,
pdf:erna har textlager (pdftotext):
  Riksdagen: PBL 2010:900 (1 kap. 4 §, 9 kap. 3–6, 16, 34–37 §§ lästa i lagtexten); PBF 2011:338 6 kap. 1 §
  (installation/väsentlig ändring av VA, ventilation, eldstad, rökkanal).
  Boverket: Lista med PBL-ändringar (svarar 200 via omdirigering till /om-boverket/.../lista-pbl--andringar/).
  Skatteverket – Ger arbetet rätt till rotavdrag? (småhus): inget avdrag för att bygga ett helt nytt hus, friggebod,
  garage, växthus eller liknande fristående byggnad; inget för att skriva bygglovshandlingar eller anlita arkitekt,
  besiktningsman eller liknande; aldrig rotavdrag för att bygga en helt ny bostad; tillbyggnad av gäststuga ger avdrag om
  en sida sitter ihop med ytterväggen till minst 75 % eller det finns en dörr emellan; riva väggar/bygga om planlösning
  ger avdrag; bostaden äldre än fem år och större delen av stommen behålls (ROT-texterna formulerade olika per sida).
  Region Stockholm – RUFS-bilagan Riksintressen (pdf): tabell 8 TM0010 Utö skjutfält (riksintresse på land +
  påverkansområde för buller eller annan risk), TM0300 Nåttarö (Värmdö, Haninge, Södertälje, Nynäshamn, sjöövningsområde);
  tabell 3 AB 602 Utö (gruvsamhälle, sommarnöjesmiljö), AB 604 Sundby–Varnö på Ornö (herrgårdsmiljö, odlingslandskap,
  torp); tabell 4 AB 605 Dalarö, AB 63 Roslags-Kulla/Wira (herrgårdslandskap, sockencentrum); tabell 2 AB 54 Storängen,
  AB 122 Saltsjöbadens centrala delar, AB 51 Nacka–Norra Boo–Vaxholm–Oxdjupet–Lindalssundet, AB 62 Åkers kanal.
  Länsstyrelsen Stockholm – Granskningsyttrande Haninge 2050 (2025-12-22, pdf): sju riksintressen för kulturmiljövården,
  AB 605 och AB 19; riksintressen för totalförsvaret och påverkansområden bara i text, saknas i kartan, behövs för att
  bedöma lovplikt inom och i anslutning.
  Haninge kommun: Bygglovsbefriad ny och tillbyggnad (bygglov i särskilt värdefullt område och för komplementbostadshus i
  riksintresse för Försvarsmakten; mått, pott, äldre attefallshus/friggebod räknas in; strandskydd 100–300 m; tillsyn
  efter klagomål; kontakt med mått, produktblad, foto; frivilligt lov; stora delar kulturmiljöer, kartskiktet uppdateras);
  Komplementbyggnad (mått inom/utanför plan); Vatten och avlopp (anmälan, planritning med möblering, kontrollplan,
  VA-ritning före/efter, VA-enheten, tillstånd för enskilt avlopp, slutbesked).
  Huddinge kommun: Lovbefriad komplementbyggnad och komplementbostadshus (lovkrav vid 4,5 m, 30 m järnväg,
  kulturvärden, totalförsvar; handlingar inkl. förenklad nybyggnadskarta, marklinjer, NCS, kontrollplan; anmälan för
  VA/eldstad/ventilation; SVOA, avloppstillstånd hos miljötillsynen lämnas med anmälan; egen brunn; strandskydd hos
  miljötillsynen); Installation eller ändring av VA (handlingar, gratis tomtkarta, byggherren kontaktar SVOA);
  Ansluta attefallshus till VA (SVOA ansvarar för spillvattennätet, dimensionering, tillstånd enligt lokala föreskrifter
  HKF 1300, avgift för anslutning av WC/BDT – belopp ej återgivet); Egen brunn (inget tillstånd för att borra, krav vid
  flera hushåll/uthyrning, Livsmedelsverkets rekommendation vart tredje år, ackrediterat lab, tre bedömningskategorier).
  Nacka kommun: Komplementbostadshus (bygglovsbefriad) (interimistiskt slutbesked vid ny villa, nybyggnad = även flytta,
  fristående, får strida mot detaljplan utom vid utökad lovplikt, 30 m järnväg inom och utanför plan + medgivande från
  infrastrukturförvaltaren, kulturmiljö 8:13 – bygglov och planenlighet, även f.d. friggebod, kartan lila/orange);
  Placering av lovfria åtgärder (alla sidor, medgivande skickas inte in, kommunägd mark kräver skriftligt tillstånd,
  beslut ≠ godkännande av byggnaden, checklistan, <2 m undantagsvis); Kulturmiljöprogram Villasamhällen vid järnvägen
  (pdf: Wallenberg, Saltsjöbaden, villasamhällen från 1890-talet, Igelboda–Solsidan 1910-talet, terränganpassat,
  svängda gator, stora tomter).
  Sollentuna kommun: Komplementbyggnad och komplementbostadshus (lovkrav, 30 m järnväg, pott 45/65 med tidigare
  attefallshus/friggebodar, anmälan inkl. imkanal, detaljplanekrav för komplement till andra byggnader, radhus/kedjehus,
  frivilligt lov, handlingar för ansökan); Attefallshus (samma radhus- och ansvarsavsnitt); Förändringar i PBL
  (granskas inte i förväg, 30 m²/4 m/45 m², tillbyggnadspotten 30 m² med skärmtak och attefallstillbyggnader,
  kulturhistoriskt värdefullt område → bygglov, anmälan vid VA/ventilation); Bygglovsbefriad inredning av ytterligare en
  bostad (anmälan och startbesked, handlingar inkl. brandskydd, lov om ej enbostadshus/kulturvärde, får strida mot plan,
  lov söks samtidigt vid nybyggnad). Handläggningstider och avgifter på sidorna är medvetet INTE använda.
  Tyresö kommun: Förändringar i PBL (30/4/45 inom plan, kulturhistoriskt → bygglov, anmälan vid VA i byggnaden eller inom
  tomten och eldstad, frivilligt lov); VA-anslutning (sju steg, attefallshus i äldre område, situationsplan med ledningar
  och stenkista, kontrollplan med exempel, förbindelsepunkt vid gränsen och ansvarsfördelning, sluttömning via avfall,
  anläggningsavgift som nytt boende på lägenhetsavgiftsnivå, vattenmätarkrav, alternativ 1/2 med besiktning, inga
  restriktioner för avlopp/dagvatten, årlig avgift per mätare, VA-lån Raksta etapp 8); Dagvatten (ägarens ansvar,
  hårdgjorda ytor, grus/stenmjöl/genomsläpplig marksten, växtytor, träd upp till cirka 500 liter per dygn, marklutning,
  lågpunkt).
  Österåkers kommun: Komplementbyggnad (attefallshus, friggebod) (komplementbyggnad får inte inredas till bostad,
  uthyrning bara om Boverkets krav – tillgänglighet, ventilation, energi – och omgivningspåverkan, "kan inte bygga en
  gäststuga och hyra ut den som bostad", bygglov i kulturhistoriskt område, Roslagsbanans 30 m-zon, strandskyddsdispens
  oftast, ingen granskning, tillsyn med byggsanktionsavgift eller rivning, frivilligt lov, ritningschecklistor);
  Kulturhistoriska byggnader, kulturmiljöer (bygglov även för att bygga nytt, Österåkerskartan med överlappande skydd,
  kulturvärden även i vardagliga/yngre byggnader, k = varsamt, q = får inte rivas, checklistans frågor, Fornsök och
  Länsstyrelsens tillstånd med pool som exempel, antikvarie som rådgivare).

Strukna / ej verifierade: alla avgiftsbelopp och handläggningstider (Huddinge, Sollentuna, Tyresö – medvetet utelämnade);
Boverkets sida "Bygga en ny byggnad" om radhus (svarade inte – DNS/timeout – därför bara Sollentunas egen formulering
om radhus/kedjehus, ingen egen tolkning av om radhus är enbostadshus); Trafikverkets riktlinjer om 30 m från järnväg
(ingen läsbar primärkälla – endast PBL 9:34–35 och kommunernas text); vem som är infrastrukturförvaltare för
Saltsjöbanan (ej i källa – skrivet "infrastrukturförvaltaren"); SEOM:s VA-regler i Sollentuna (ingen öppen källa
utom taxan – utelämnat); Berga/Muskö i Haninge (bara i ett remissvar från 2019 – utelämnat); att Haninges
försvarsregel även gäller komplementbyggnader (kommunens komplementbyggnadssida nämner båda, lagen bara
komplementbostadshus – ingen FAQ om det); Österåkers "certifierad kontrollansvarig för kulturvärden" (struket, cert-WARN);
Österåkers "före 1920"-fråga (finns redan på snickare-osteraker); geografiska generaliseringar i ingresserna
("villakvarteren", "längre söderut", "många Nackatomter", "ofta i samma kvarter" – strukna i kritikpasset).
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert. Perks bara: gratis platsbesök, skriftligt
kostnadsförslag, nyckelfärdigt. Egna bedömningar skrivna som vår bedömning/vårt arbetssätt: skriftligt besked från
Haninges bygglovsenhet, ledningsritning för båda anmälningarna (Huddinge), fornlämningsfrågan inför grunden (Österåker).

Kritikpass 2026-10-26 (alla källor öppnade igen och varje faktamening jämförd med källtexten): mått 30,0/4,0/45,0 och
50,0/4,5/65,0, 4,5 m, 30,0 m, 9:35 andra stycket och 9:36 p. 1 (bara flygplatser och övnings- eller skjutfält) stämmer
mot lagtexten; AB-/TM-nummer kontrollerade mot RUFS-tabellerna 2–4 och 8; "sju områden" mot LST-yttrandet. Rättat:
Haninge – ingressens "villorna i Vendelsö" (ej i källa) → tätorten kring Handen och Jordbro (LST:s utredningsområde);
Huddinge – "villakvarteren nära centrum … längre söderut" (ej i källa) struket; Nacka – "Många Nackatomter" → "En tomt
i Nacka kan"; ”Nacka vatten och avfall” → kommunalt VA; AB 51 med fullt namn; Sollentuna – "med egen entré" (ej i
källa) struket, ingressens kvartersgeneralisering omskriven, meningen om ytterligare bostad i ny villa följer nu
kommunens text (lov söks samtidigt när inredningen strider mot planen), skärmtaksmeningen skriven som följd av
kommunens uppdelning; Österåker – "två riksintressen" → "bland annat två" (RUFS-tabellerna är inte uttömmande per
kommun), cert-meningen ersatt med kommunens råd om antikvarie, titeln kortad till 51 tecken. ROT-avsnitten kontrollerade
mot Skatteverket (nytt hus/fristående byggnad/ny bostad ger inget avdrag; 75 %-regeln, arkitekt/bygglovshandlingar och
femårs-/stomregeln återgivna korrekt).
Kritikpass 2 (extern) 2026-10-26: alla 25 käll-URL:er öppnade med curl -L (UA Mozilla), alla 200 (Skatteverket
först timeout, 200 vid nytt försök); de tre pdf:erna (LST-yttrandet, Nackas kulturmiljöprogram, RUFS-bilagan) har
textlager (pdftotext). Ingen källa struken. Boverket-URL:en bytt till slutadressen efter omdirigeringarna
(/om-boverket/boverkets-uppdrag-och-styrning/aktuella-uppdrag/...). PBL 9 kap. 4, 5, 34, 35, 36 och 37 §§ och 1 kap. 4 §
(lydelse 2025:974) samt PBF 6 kap. 1 § lästa på riksdagen.se: 30,0/4,0/45,0, 50,0/4,5/65,0, 4,5 m, 30,0 m, 9:35 andra
stycket och 9:36 p. 1 stämmer. Rättat:
Haninge – ingressen "sommarhusen på Dalarö och öarna i skärgården" (ej i källa) → "Från Handen och Jordbro till Dalarö,
  Utö och Ornö" (orterna finns i LST/RUFS) och "samma litet hus" → "samma lilla hus"; "påverkansområde ... runt det" →
  utan "runt det"; "markanvändningskartan" → "mark- och vattenanvändningskartan" (LST:s ord); "Utö, Ornö eller i södra
  skärgården" → "på eller nära Utö" (Ornö har inget försvarsriksintresse i källorna); 9:37-meningen följer nu lagen
  (tomt med skyddsbestämmelser i detaljplan / särskilt värdefullt bebyggelseområde); asiden "Nära flygplatser/
  skjutfält" → "Vid försvarets ..." (9:36 gäller bara totalförsvarets riksintressen); FAQ Utö "Ofta, ja" → "Det kan
  behövas" (omfattningen av området är inte känd).
Huddinge – ingressens "behöver sällan bygglov" (ej i källa) → "kan byggas utan bygglov om vissa krav uppfylls";
  "byggnadsnämnd ... samtidigt" → "Till kommunen gör du dessutom"; HKF 1300-meningen och FAQ:n återger nu villkoret
  "om åtgärden kan medföra väsentlig ändring av avloppsvattnets mängd eller sammansättning" (FAQ:ns ovillkorliga "Ja"
  struket); "nära en sjö" → "omfattas fastigheten av strandskydd" (kommunens villkor); "generellt krav" → kommunens ord.
Nacka – "Det är ofta på sådana tomter som det finns plats för ett hus till" (ej i källa) ersatt med programmets
  förhållningssätt för Saltsjöbaden (komplementbyggnader underordnas huvudbyggnaden, gatubildens karaktär behålls);
  "infrastrukturförvaltaren räknas som granne" → lagens formulering (grannen anses ha medgett); anmälningsplikten
  hänvisad till PBF (Nackas sida säger bara "kan vara anmälningspliktiga").
Sollentuna – ROT-avsnittet antydde rotavdrag för att inreda en bostad i villan; Skatteverket: "aldrig rotavdrag för att
  bygga en helt ny bostad" → avsnittet omskrivet (inget avdrag för attefallshuset, ingen avdragsutfästelse för den
  extra bostaden), h2 → "Rotavdrag och en ny bostad"; FAQ om "frivilligt bygglov"-ritningar → handlingarna för
  bygglovsansökan (kommunens lista gäller ansökan om bygglov); skärmtaks-FAQ:n "enligt kommunen"; img[2] (friggebod/
  skärmtak = potten, ej sista sektionen) → hoprullade ritningar framför nybyggt hus (sista sektionen: lov/ritningar).
Tyresö – ingressens "kök och badrum ... i kommunens ögon" → kommunens ord (toalett, hygien- och matlagningsmöjligheter,
  nytt boende); "Själva huset är lovfritt" → "kan enligt kommunen byggas utan bygglov ... utom i kulturhistoriskt
  särskilt värdefullt område"; ROT "Rotavdraget är till för arbete i en bostad som redan finns" → Skatteverkets krav
  (i eller nära bostad som kunden äger); FAQ mätare: "räcker den" (ej i källa) struket.
Österåker – "Region Stockholm listar bland annat två riksintressen" → kommunens egen uppgift: fyra riksintressen
  (Roslags-Kulla, Rydboholm, Vira bruk, Åkers kanal) + RUFS-beskrivningen av AB 62/AB 63; tillagt kommunens uppgift om
  landskapsbildsskydd runt Roslags-Kulla och Österåkers kyrka (ny byggnad kräver dispens från Länsstyrelsen); FAQ
  Roslags-Kulla kompletterad med kommunen; frivilligt bygglov → "kommunen prövar ... och lämnar ett beslut" (beslutet
  kan vara nej); "fastigheten är värdefull" → "huset är värdefullt" (checklistans ord); img[2] (stensättning =
  fornlämningssektionen, ej sista) → nyfärdigt rum med pärm (sista sektionen: tillsyn/handlingar att spara).
Kvarstår ej verifierat: att Saltsjöbanan räknas som järnväg enligt PBL 9:34 (kulturmiljöprogrammet kallar den järnväg,
  Nackas sida talar om järnväg generellt); hur stort område runt Utö skjutfält som räknas som "i anslutning till";
  om ett sjöövningsområde (Nåttarö) omfattas av 9:36 p. 1 (texten påstår det inte).
Kända WARN: bara "bild saknas" (bilder genereras senare).
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no text, no letters"

_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 1 kap. 4 § och 9 kap. 4–5, 16, 34–37 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_PBF = ("Riksdagen – Plan- och byggförordning (2011:338), 6 kap. 1 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-byggforordning-2011338_sfs-2011-338/")
_BOV = ("Boverket – Lista med PBL-ändringar som trädde i kraft 1 december 2025",
        "https://www.boverket.se/sv/om-boverket/boverkets-uppdrag-och-styrning/aktuella-uppdrag/avslutade-uppdrag/nytt-regelverk-for-bygglov/lista-pbl--andringar/")
_RUFS = ("Region Stockholm – Riksintressen i regional utvecklingsplan för Stockholmsregionen (bilaga, pdf)",
         "https://www.regionstockholm.se/49dc46/contentassets/d520d8a737244589a241cfae38e13db6/bilaga-riksintressen-i-regional-utvecklingsplan-for-stockholmsregionen.pdf")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")

_HN = "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/"
_HAN_BEF = ("Haninge kommun – Bygglovsbefriad ny och tillbyggnad", _HN + "bygglovsbefriad-ny-och-tillbyggnad/")
_HAN_KB = ("Haninge kommun – Komplementbyggnad", _HN + "komplementbyggnad/")
_HAN_VA = ("Haninge kommun – Vatten och avlopp", _HN + "vatten-och-avlopp/")
_HAN_LST = ("Länsstyrelsen Stockholm – Granskningsyttrande över Haninge 2050, översiktsplan (pdf)",
            "https://www.haninge.se/49eb2d/siteassets/bygga-bo-och-miljo/oversiktsplanering-och-detaljplaner/op-2050-utblick-mot-2070/dokument-op/lansstyrelsens-granskningsyttrande_haninge-2050-oversiktsplan.pdf")

_HB = "https://www.huddinge.se/bostad-och-miljo/"
_HUD_KBH = ("Huddinge kommun – Lovbefriad komplementbyggnad och komplementbostadshus",
            _HB + "bygglov/nar-behover-du-bygglov/lovbefriad-komplementbyggnad-och-komplementbostadshus")
_HUD_VA = ("Huddinge kommun – Installation eller ändring av vatten och avlopp",
           _HB + "bygglov/nar-behover-du-bygglov/installation-eller-andring-av-vatten-och-avlopp-va")
_HUD_ANSL = ("Huddinge kommun – Ansluta attefallshus till vatten och avlopp",
             _HB + "vatten-och-avlopp/ansluta-till-kommunalt-vatten/ansluta-attefallshus-till-vatten-och-avlopp/")
_HUD_BRUNN = ("Huddinge kommun – Egen brunn", _HB + "vatten-och-avlopp/avlopp/egen-brunn/")

_NB = "https://www.nacka.se/boende-miljo/bygga-nytt-andra-eller-riva/"
_NAC_KBH = ("Nacka kommun – Komplementbostadshus (bygglovsbefriad)", _NB + "lovfria-atgarder/komplementbostadshus-bygglovsbefriad/")
_NAC_PLAC = ("Nacka kommun – Placering av lovfria åtgärder", _NB + "Placering-av-lovfria-atgarder/")
_NAC_KMP = ("Nacka kommun – Kulturmiljöprogram: Villasamhällen vid järnvägen (pdf)",
            "https://www.nacka.se/499626/globalassets/stadsutveckling-trafik/dokument/stadsutveckling/sektorprogram/kulturmiljoprogram-jarnvagen.pdf")

_SB = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/"
_SOL_KB = ("Sollentuna kommun – Komplementbyggnad och komplementbostadshus", _SB + "komplementbyggnad/")
_SOL_ATT = ("Sollentuna kommun – Attefallshus", _SB + "attefallshus/")
_SOL_NYA = ("Sollentuna kommun – Förändringar i PBL", _SB + "nya-regler-december-2025/")
_SOL_YTT = ("Sollentuna kommun – Bygglovsbefriad inredning av ytterligare en bostad", _SB + "bygglovsbefriad-inredande-av--ytterligare-bostad/")

_TY = "https://www.tyreso.se/boende--miljo/"
_TYR_PBL = ("Tyresö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
            _TY + "bygga/bygga-riva-eller-andra/forandringar-i-plan--och-bygglagen-fran-1-december-2025.html")
_TYR_ANSL = ("Tyresö kommun – VA-anslutning", _TY + "vatten-och-avlopp/anslutning.html")
_TYR_DAG = ("Tyresö kommun – Dagvatten", _TY + "vatten-och-avlopp/dagvatten.html")

_OB = "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/bygglovsguiden/"
_OST_KB = ("Österåkers kommun – Komplementbyggnad (attefallshus, friggebod)", _OB + "komplementbyggnadattefallshusfriggebod.4.24daed7e19aff7a0474902.html")
_OST_KULT = ("Österåkers kommun – Kulturhistoriska byggnader, kulturmiljöer", _OB + "kulturhistoriskabyggnaderkulturmiljoer.4.367d658917909e8fc2bb42.html")

_REG = _L.format("attefallshus-regler.html", "reglerna för attefallshus")

PAGES_TJ = {

# ------------------------------------------------------------------ HANINGE
"attefallshus-haninge.html": {
  "kind": "district", "service": "attefallshus", "ort": "Haninge", "svc_label": "Attefallshus",
  "title": "Attefallshus i Haninge – skjutfält, kulturmiljö och strand",
  "description": "Attefallshus i Haninge: bygglov nära Utö skjutfält, sju riksintressen för kulturmiljön, strandskydd 100–300 m och anmälan för vatten och avlopp.",
  "h1": "Attefallshus i Haninge",
  "lead": "Från Handen och Jordbro till Dalarö, Utö och Ornö – i Haninge kan samma lilla hus vara lovfritt på en tomt och kräva bygglov på nästa. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och reder först ut vad som gäller för just din fastighet.",
  "card": "Skjutfält, kulturmiljö och skärgårdstomter.",
  "sections": [
    {"id": "forsvaret-haninge", "anchor": "Försvarets områden",
     "h2": "Utö skjutfält och försvarets påverkansområden",
     "paras": [
       "Plan- och bygglagen har en regel som många missar: inom eller i anslutning till ett område av riksintresse för totalförsvarets anläggningar krävs bygglov för ett nytt komplementbostadshus, om området är en flygplats eller ett övnings- eller skjutfält (9 kap. 36 §). Region Stockholms sammanställning pekar ut Utö skjutfält som riksintresse på land och redovisar dessutom ett påverkansområde för buller eller annan risk. Havsområdet vid Nåttarö är riksintresse som sjöövningsområde och berör flera kommuner, däribland Haninge.",
       "Haninge kommun skriver att du behöver bygglov om du vill bygga ett komplementbostadshus i ett område som är utpekat som riksintresse för Försvarsmakten. Var gränserna går är inte självklart. I sitt granskningsyttrande över översiktsplanen Haninge 2050 noterar Länsstyrelsen att riksintressena för totalförsvaret och deras påverkansområden bara beskrivs i text och saknas på mark- och vattenanvändningskartan, och att en sådan redovisning behövs för att bedöma lovplikten. För en tomt på eller nära Utö frågar vi därför bygglovsenheten innan vi ritar.",
     ],
     "aside": {"title": "Bygglov krävs", "items": [
       "Vid försvarets skjutfält", "Vid försvarets flygplatser",
       "I särskilt värdefulla områden", "Under 4,5 m utan grannens ja"]}},
    {"id": "kulturmiljo-haninge", "h2": "Sju riksintressen och en karta under arbete",
     "paras": [
       "Enligt Länsstyrelsen har Haninge sju områden av riksintresse för kulturmiljövården. Två av dem är Dalarö–Jutholmen–Dalarö skans (AB 605) och Österhaningebygden (AB 19). Region Stockholm listar också gruvsamhället och sommarnöjesmiljön på Utö (AB 602) och Sundby–Varnö på Ornö (AB 604), med herrgårdsmiljö, odlingslandskap och torp. Plan- och bygglagen kräver bygglov för nybyggnad inom en tomt som har skyddsbestämmelser i detaljplanen och inom ett bebyggelseområde som är särskilt värdefullt (9 kap. 37 §).",
       "Kommunen skriver själv att stora delar av Haninge är kulturmiljöer och att skärpta krav gäller i särskilt värdefulla områden och riksintressen för kulturmiljövård. Det digitala kartskiktet som visar de särskilt värdefulla miljöerna håller på att uppdateras, och tills det är klart hänvisar kommunen till bygglovsenheten för besked om en enskild fastighet. Vi ber om det beskedet skriftligt och sparar det med husets övriga handlingar.",
     ],
     "aside": None},
    {"id": "strand-va-haninge", "h2": "Strandskydd och vatten på skärgårdstomten",
     "paras": [
       "Haninge kommun påminner om att strandskyddet vanligtvis gäller 100 till 300 meter från kustlinjen, sjöar och större vattendrag, och att du då kan behöva dispens även för ett hus som är fritt från bygglov. På en tomt nära vattnet är det ofta placeringen som avgör, så vi mäter in avståndet till strandlinjen innan huset ritas.",
       "Vatten och avlopp hanteras för sig. Den som installerar en anläggning för vattenförsörjning eller avlopp i en byggnad ska göra en anmälan och få startbesked innan arbetet börjar. Kommunen vill se en planritning som visar hur rummen ska möbleras och användas, ett förslag till kontrollplan och en VA-ritning som beskriver hur det ser ut i dag och hur det blir efter ändringen. Ska huset kopplas på kommunalt VA anmäls det till VA-enheten, och för ett enskilt avlopp söker du tillstånd. Huset får användas först när slutbeskedet har kommit.",
     ],
     "aside": {"title": "Till VA-anmälan", "items": [
       "Planritning med möblering", "Förslag till kontrollplan",
       "VA-ritning före och efter", "Fastighet och kontaktuppgifter"]}},
    {"id": "besked-haninge", "h2": "Fråga först – och väg in tillsynen",
     "paras": [
       "Utanför de utpekade områdena gäller lagens mått: 30,0 kvadratmeter byggnadsarea och 4,0 meter till nocken inom detaljplan, 50,0 och 4,5 utanför, med en gemensam pott på 45,0 respektive 65,0 kvadratmeter. Haninge kommun påpekar att ett attefallshus eller en friggebod som redan står på tomten räknas in i potten, och att byggnaden inte får vara större än huvudbyggnaden.",
       "Är du osäker ber kommunen dig beskriva vad du planerar med mått, produktblad och gärna ett fotografi. Kommunen skriver också att en överprövande myndighet kan komma fram till att en åtgärd är bygglovspliktig om någon klagar, trots kommunens riktlinjer. Den som vill ha ett beslut i förväg kan söka frivilligt bygglov. Altaner och verandor beskrivs under " + _L.format("snickare-haninge.html", "snickare i Haninge") + ", och större byggprojekt i omvandlingsområden under " + _L.format("byggforetag-haninge.html", "byggföretag i Haninge") + ". Måtten och paragraferna finns samlade i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Haninge",
  "steps": [
    ("Fastigheten", "Detaljplan, kulturmiljö, försvarets områden och strandskydd för just din tomt."),
    ("Besked", "Vid osäkerhet ber vi bygglovsenheten om ett skriftligt besked."),
    ("Ritningar", "Plan med möblering, VA-ritning och situationsplan med avstånd."),
    ("Anmälan", "VA, ventilation och eldstad anmäls och vi väntar på startbesked."),
    ("Bygget", "Grund, stomme, tak och installationer fram till nyckelfärdigt."),
    ("Slutbesked", "Huset tas i bruk när slutbeskedet har kommit."),
  ],
  "rot_h2": "Rotavdrag gäller inte det nya huset",
  "rot": [
    "Skatteverkets lista över arbeten som inte ger rotavdrag på ett småhus tar upp att bygga ett helt nytt hus eller en liknande fristående byggnad, och även att skriva bygglovshandlingar eller anlita en arkitekt. Ett komplementbostadshus är en ny fristående byggnad, så både ritningar och bygge räknas utan avdrag i vårt kostnadsförslag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Haninge?",
  "price": [
    "Husets storlek och planlösning, kök och badrum, grund på berg eller lera, avloppslösningen och om material kan köras ända fram eller måste fraktas med båt till en ö. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för ett attefallshus på Utö?",
     "Det kan behövas. Utö skjutfält är riksintresse för totalförsvaret, och inom eller i anslutning till ett skjutfält kräver plan- och bygglagen bygglov för ett komplementbostadshus. Delar av Utö är också riksintresse för kulturmiljövården."),
    ("Hur får vi veta om vår tomt på Dalarö är särskilt värdefull?",
     "Kommunen uppdaterar kartskiktet över särskilt värdefulla kulturmiljöer. Tills det är klart ger bygglovsenheten besked om den enskilda fastigheten."),
    ("Vad ska VA-ritningen för ett attefallshus i Haninge visa?",
     "Vad som ändras i vatten och avlopp, hur det ser ut i dag och hur det ska se ut efter ändringen. Ritningen kan redovisas på planritningen."),
    ("Kan ett lovfritt attefallshus i Haninge bedömas som lovpliktigt i efterhand?",
     "Ja. Kommunen skriver att en överprövande myndighet vid ett klagomål kan bedöma att åtgärden kräver bygglov. Ett frivilligt bygglov ger en prövning i förväg."),
    ("Hur långt från vattnet gäller strandskyddet i Haninge?",
     "Enligt kommunen vanligtvis 100 till 300 meter från kustlinjen, sjöar och större vattendrag. Inom det området kan dispens behövas även när huset är lovfritt."),
  ],
  "sources": [_PBL, _PBF, _BOV, _RUFS, _HAN_LST, _HAN_BEF, _HAN_KB, _HAN_VA, _SKV],
  "cta": ("Funderar du på ett attefallshus i Haninge?", "Boka ett gratis platsbesök, så tar vi reda på vad som gäller för tomten innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet trähus med ljusgrå panel och svart plåttak på en klippig skärgårdstomt med tallar",
     "small newly built Swedish timber guest house with light grey vertical board cladding and a black standing seam metal roof on a rocky archipelago plot among pine trees, an older yellow wooden summer villa partly visible behind, calm sea inlet glimpsed between trunks, Dalarö Haninge Stockholm archipelago, clear morning light" + _SFX),
    ("Utstakning med pinnar och snören på en gräsyta mellan tallar inför ett litet hus",
     "lawn between pine trees on a Swedish coastal plot with wooden stakes and orange string marking the corners of a small house footprint, granite outcrop in the background, overcast daylight" + _SFX),
    ("Äldre friggebod och ett nybyggt litet trähus på samma villatomt",
     "an older small red wooden garden shed with a white door and a newly built slightly larger light grey timber guest house standing on the same lawn of a Swedish villa plot, gravel path between them, pine trees and a low fence behind, south of Stockholm, soft afternoon light" + _SFX),
  ],
},

# ------------------------------------------------------------------ HUDDINGE
"attefallshus-huddinge.html": {
  "kind": "district", "service": "attefallshus", "ort": "Huddinge", "svc_label": "Attefallshus",
  "title": "Attefallshus i Huddinge – avlopp, egen brunn och ritningar",
  "description": "Attefallshus i Huddinge: anslutning via Stockholm Vatten och Avfall, tillstånd för enskilt avlopp, egen brunn och ritningarna när bygglov krävs.",
  "h1": "Attefallshus i Huddinge",
  "lead": "Ett komplementbostadshus i Huddinge kan byggas utan bygglov om vissa krav uppfylls, men det behöver vatten, och där skiljer sig en tomt med kommunalt VA från en tomt med egen brunn och eget avlopp. Geal Entreprenad AB bygger husen nyckelfärdigt och planerar vattnet och avloppet innan grunden läggs.",
  "card": "Avlopp, egen brunn och ritningar.",
  "sections": [
    {"id": "kommunalt-va-huddinge", "anchor": "Kommunalt VA",
     "h2": "Kommunalt VA: två anmälningar på samma hus",
     "paras": [
       "Huddinge kommun skriver att Stockholm Vatten och Avfall ansvarar för det kommunala spillvattennätet i Huddinge, och att anslutningen av ett attefallshus eller en komplementbyggnad ska anmälas dit. Det ansvaret ligger på byggherren. Till kommunen gör du dessutom en anmälan om installationen, och du väntar på startbesked innan rören dras. Samma sak gäller om huset får eldstad eller en anordning för ventilation (plan- och byggförordningen 6 kap. 1 §).",
       "För VA-anmälan räknar kommunen upp en situationsplan på tomtkarta, där du markerar vilken byggnad ändringen gäller om det finns flera på tomten, en planritning när ändringen sker inne i en byggnad och ett förslag till kontrollplan. Tomtkartan kan skrivas ut gratis från kommunen. Vi ritar in husets ledningar fram till villans befintliga, så att samma underlag kan användas i båda anmälningarna.",
     ],
     "aside": {"title": "Anmäls innan arbetet", "items": [
       "Anslutning till Stockholm Vatten och Avfall", "VA-installation till kommunen",
       "Eldstad", "Ventilation"]}},
    {"id": "enskilt-huddinge", "h2": "Enskilt avlopp: tillstånd innan toaletten kopplas in",
     "paras": [
       "När fler bor på tomten ökar belastningen på avloppet. Huddinge kommun skriver att avloppsanordningen behöver vara dimensionerad för den nya belastning som kan uppstå när ett attefallshus eller en komplementbostad byggs. Enligt kommunens lokala föreskrifter krävs tillstånd för att ansluta en vattentoalett till en befintlig avloppsanordning och för att ändra anordningen, om åtgärden kan medföra en väsentlig ändring av avloppsvattnets mängd eller sammansättning.",
       "Ansökan görs hos kommunens miljötillsynsavdelning. Kommunen ber dig sedan lämna in avloppstillståndet samtidigt som du gör anmälan om att bygga komplementbostadshuset. En avgift tas ut för att ansluta vattentoalett eller bad-, disk- och tvättvatten till en befintlig godkänd anordning. Ordningen påverkar tidplanen, så vi tar fram underlaget till avloppsansökan först och börjar inte med grunden förrän det är klart vart vattnet ska.",
     ],
     "aside": None},
    {"id": "brunn-huddinge", "h2": "Egen brunn – räcker vattnet till två hushåll?",
     "paras": [
       "Får fastigheten sitt dricksvatten från en egen brunn ska det enligt kommunen framgå av anmälan om komplementbostadshuset. Att det finns tillräckligt med vatten och att kvaliteten är bra är fastighetsägarens ansvar. Kommunen skriver också att det följer vissa krav när en dricksvattenanläggning försörjer flera hushåll eller när huset ska hyras ut, vilket är just läget när ett attefallshus blir en egen bostad.",
       "För att borra eller gräva en ny brunn krävs inget tillstånd från kommunen. Det finns inget krav på vattenprov, men Livsmedelsverket rekommenderar prov vart tredje år, och kommunen råder dig att anlita ett ackrediterat laboratorium. Svaret bedöms som tjänligt, tjänligt med anmärkning eller otjänligt. Omfattas fastigheten av strandskydd söker du dispens hos samma miljötillsynsavdelning.",
     ],
     "aside": {"title": "Med egen brunn", "items": [
       "Ange brunnen i anmälan", "Ägaren ansvarar för kvaliteten",
       "Prov rekommenderas vart tredje år", "Ackrediterat laboratorium"]}},
    {"id": "ritningar-huddinge", "h2": "Ritningarna när huset ändå kräver lov",
     "paras": [
       "Kommunen listar när bygglov krävs trots att måtten hålls: närmare gränsen än 4,5 meter utan skriftligt medgivande från grannarna, närmare än 30,0 meter från ett järnvägsspårs mitt utan medgivande från infrastrukturförvaltaren, på en tomt eller i ett område med särskilda kulturhistoriska värden, och för ett komplementbostadshus i ett riksintresse för totalförsvaret när det gäller flygplatser eller övnings- och skjutfält.",
       "Då vill kommunen normalt ha en situationsplan på förenklad nybyggnadskarta, fasadritningar med marklinjer, plan- och sektionsritningar, en kulör- och materialbeskrivning där färgen anges med NCS-kod och ett förslag till kontrollplan. Ändras marken mer än lite visas det på situationsplanen eller på en separat markplaneringsritning. Förråd och gäststugor beskrivs under " + _L.format("snickare-huddinge.html", "snickare i Huddinge") + ", och den som hellre bygger ihop ytan med villan läser om " + _L.format("tillbyggnad-huddinge.html", "tillbyggnad i Huddinge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Huddinge",
  "steps": [
    ("Vatten först", "Kommunalt VA, enskilt avlopp eller egen brunn – vi utgår från vad tomten har."),
    ("Tillstånd", "Avloppstillstånd och vid behov strandskyddsdispens hos miljötillsynen."),
    ("Anmälningar", "Byggnadsnämnden och Stockholm Vatten och Avfall, med samma ledningsritning."),
    ("Startbesked", "Arbetet med installationerna börjar när beskedet har kommit."),
    ("Bygget", "Grund, stomme, tak, installationer och ytskikt – nyckelfärdigt."),
    ("Slutbesked", "Genomgång av huset och de handlingar du ska spara."),
  ],
  "rot_h2": "Fristående hus ger inget rotavdrag",
  "rot": [
    "Skatteverket godkänner rotavdrag för en tillbyggnad med gäststuga om någon av tillbyggnadens sidor sitter ihop med husets yttervägg till minst 75 procent eller om det finns en dörr emellan. Ett komplementbostadshus står fritt på tomten, och att bygga ett helt nytt hus eller en liknande fristående byggnad ger inget avdrag. Kostnadsförslaget för attefallshuset är därför utan rotavdrag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Huddinge?",
  "price": [
    "Storlek och planlösning, kök och badrum, grund på berg eller lera, avståndet till befintliga ledningar och om avloppet behöver byggas om för fler boende. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vart anmäler vi att attefallshuset ska kopplas på kommunalt avlopp i Huddinge?",
     "Till Stockholm Vatten och Avfall, som ansvarar för spillvattennätet i Huddinge. Installationen anmäls dessutom till kommunen, som ger startbesked."),
    ("Behövs avloppstillstånd när attefallshusets toalett kopplas till vårt enskilda avlopp i Huddinge?",
     "Kommunens lokala föreskrifter kräver tillstånd för att ansluta en vattentoalett till en befintlig avloppsanordning, om åtgärden kan medföra en väsentlig ändring av avloppsvattnets mängd eller sammansättning. Ansökan görs hos miljötillsynsavdelningen."),
    ("Måste brunnsvattnet provtas innan vi hyr ut attefallshuset i Huddinge?",
     "Kommunen skriver att det inte finns något krav på att ta vattenprov i brunnen, men att det följer krav när anläggningen försörjer flera hushåll eller huset hyrs ut. Livsmedelsverket rekommenderar prov vart tredje år."),
    ("Hur anges färgen på ett attefallshus som kräver bygglov i Huddinge?",
     "I en kulör- och materialbeskrivning, där kulören anges med NCS-kod. Den kan stå i ansökan, på en ritning eller i ett separat dokument."),
    ("Var söker vi strandskyddsdispens för ett attefallshus vid en sjö i Huddinge?",
     "Hos kommunens miljötillsynsavdelning. Dispensen behövs om fastigheten omfattas av strandskydd, även när huset inte kräver bygglov."),
  ],
  "sources": [_PBL, _PBF, _BOV, _HUD_KBH, _HUD_VA, _HUD_ANSL, _HUD_BRUNN, _SKV],
  "cta": ("Funderar du på ett attefallshus i Huddinge?", "Boka ett gratis platsbesök, så går vi igenom vatten, avlopp och placering innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet rödmålat trähus med sadeltak på en skogstomt med blandskog och berg i dagen",
     "small new falu red painted wooden guest house with white trim and a dark grey gable roof on a sloping forest plot with birch and pine trees and exposed grey bedrock, a 1960s Swedish villa partly visible higher up, south of Stockholm, soft late summer afternoon light" + _SFX),
    ("Brunnslock av betong och ett grävt dike med nya rör på en gräsmatta",
     "Swedish garden lawn with a round concrete well cover with a steel lid, beside it an open trench with new blue water pipe and grey sewer pipe on sand bedding leading towards a small wooden house, birch trees, overcast daylight" + _SFX),
    ("Nytt litet trähus i sluttning med synlig marklinje mot sockel och plintar",
     "side view of a newly built small Swedish timber guest house on a gently sloping garden plot, concrete plinth foundation visible on the lower side, freshly graded soil and gravel along the base showing the ground line, painted sample boards in three muted colours leaning against the wall, overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ NACKA
"attefallshus-nacka.html": {
  "kind": "district", "service": "attefallshus", "ort": "Nacka", "svc_label": "Attefallshus",
  "title": "Attefallshus i Nacka – Saltsjöbanan, kommunens mark, karta",
  "description": "Attefallshus i Nacka: lovplikt inom 30 m från Saltsjöbanan, kommunens tillstånd mot gata, park och skog, kulturmiljökartan och huset vid en ny villa.",
  "h1": "Attefallshus i Nacka",
  "lead": "En tomt i Nacka kan gränsa mot en gata, en park, ett skogsområde eller Saltsjöbanan, och det styr var ett litet hus i trädgården får stå. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och börjar med gränserna runt tomten innan vi ritar huset.",
  "card": "Saltsjöbanan, kommunens mark och kulturkartan.",
  "sections": [
    {"id": "saltsjobanan-nacka", "anchor": "Saltsjöbanan",
     "h2": "Villatomter längs Saltsjöbanan",
     "paras": [
       "Nackas kulturmiljöprogram beskriver hur Saltsjöbanan anlades av Knut A Wallenberg i samband med villastaden och badorten Saltsjöbaden, och hur ett antal villasamhällen växte fram längs banans sträckning från 1890-talet. Under 1910-talet förlängdes banan med sträckan Igelboda–Solsidan. Programmet beskriver områdena som terränganpassade, med oregelbundet svängda gator, bevarad natur och stora tomter. För Saltsjöbaden anger programmet att komplementbyggnader ska underordnas huvudbyggnaden och placeras och utformas så att gatubildens karaktär med friliggande hus i grönska behålls.",
       "Närheten till spåret har en egen regel. Plan- och bygglagen kräver bygglov för en nybyggnad inom 30,0 meter från ett järnvägsspårs mitt (9 kap. 34 §), och Nacka kommun skriver att kravet gäller komplementbostadshus både inom och utanför detaljplan. Vill du placera huset närmare krävs ett medgivande från infrastrukturförvaltaren, och enligt 9 kap. 35 § räknas grannen då ha medgett åtgärden. Vi mäter därför avståndet från spårmitt innan placeringen bestäms.",
     ],
     "aside": {"title": "Nära spåret", "items": [
       "Bygglov inom 30,0 m", "Mäts från spårets mitt",
       "Inom och utanför detaljplan", "Medgivande från förvaltaren"]}},
    {"id": "kommunens-mark-nacka", "h2": "Mot gata, park och skog krävs kommunens tillstånd",
     "paras": [
       "Nacka kommun skriver att 4,5-metersregeln gäller alla sidor av tomten, även mot gata, park och annan allmän plats. Grannens skriftliga medgivande skickas inte in till kommunen utan hanteras mellan er. Ligger kommunägd mark på andra sidan gränsen, till exempel en gata, en park, ett grönområde eller ett natur- och skogsområde, krävs i stället ett skriftligt tillstånd från kommunen. Du ansöker via kommunens formulär med tydliga ritningar, och kommunen påpekar att ett beslut om närmare placering inte är ett godkännande av själva byggnaden.",
       "Kommunens checklista visar vad som vägs in: huset ska kunna skötas och underhållas från den egna tomten, påverkan på markhöjd, avrinning och växtlighet på den kommunala marken ska redovisas, och huset får inte skymma sikten mot en allmän gata. Ett staket eller en häck i tomtgränsen ökar möjligheten att få tillstånd. Närmare än 2 meter från gränsen medger kommunen bara undantagsvis.",
     ],
     "aside": {"title": "Kommunens checklista", "items": [
       "Underhåll från egen tomt", "Redovisa mark och avrinning",
       "Ingen skymd sikt mot gata", "Under 2 m bara undantagsvis"]}},
    {"id": "karta-nacka", "h2": "Lila och orange på kulturmiljökartan",
     "paras": [
       "Ligger fastigheten i ett område som är särskilt värdefullt enligt 8 kap. 13 § plan- och bygglagen utökas lovplikten. Nacka kommun skriver att alla komplementbyggnader och komplementbostadshus då kräver bygglov och dessutom ska vara planenliga, alltså rymmas inom detaljplanens byggrätt. Det gäller även sådana byggnader som tidigare kallades friggebod.",
       "Kommunens webbkarta visar de miljöer och objekt som kommunen hittills har bedömt som särskilt kulturhistoriskt värdefulla. Lila markering betyder särskilt höga kulturvärden. Orange markering betyder att ett arbete med att bedöma värdena kan pågå, och då ber kommunen dig kontakta stadsbyggnadsservice. Region Stockholm listar Storängen (AB 54), Saltsjöbadens centrala delar (AB 122) och farledsmiljön Nacka–Norra Boo–Vaxholm–Oxdjupet–Lindalssundet (AB 51) bland riksintressena för kulturmiljövården. Hur en tillbyggnad prövas i Storängen och Saltsjöbaden beskrivs under " + _L.format("tillbyggnad-nacka.html", "tillbyggnad i Nacka") + ".",
     ],
     "aside": None},
    {"id": "ny-villa-nacka", "h2": "Ny villa och attefallshus på samma tomt",
     "paras": [
       "Ska tomten få både en ny villa och ett litet hus behöver ordningen planeras. Nacka kommun skriver att det krävs minst ett interimistiskt slutbesked för en- eller tvåbostadshuset innan ett lovfritt komplementbostadshus kan uppföras i samband med nybyggnaden. Kommunen påpekar också att nybyggnad kan betyda att flytta en befintlig byggnad till en ny plats, och att huset ska stå fristående och vara mindre än byggnaden det kompletterar.",
       "För en- och tvåbostadshus får en lovfri åtgärd strida mot detaljplanen, utom där fastigheten har utökad lovplikt genom lagen, detaljplanen eller områdesbestämmelser. Installationer för vatten, avlopp och ventilation kräver enligt plan- och byggförordningen anmälan även när huset är lovfritt. Hur anslutningen till kommunalt VA går till beskrivs under " + _L.format("byggforetag-nacka.html", "byggföretag i Nacka") + ", och ett helt nytt bostadshus under " + _L.format("nybyggnad-villa.html", "nybyggnad av villa") + ". Mått och paragrafer finns i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Nacka",
  "steps": [
    ("Gränserna", "Grannar, kommunal mark och avståndet till Saltsjöbanan mäts in."),
    ("Kartan", "Vi kontrollerar kulturmiljökartan och detaljplanen."),
    ("Medgivanden", "Grannens ja, kommunens tillstånd eller infrastrukturförvaltarens medgivande."),
    ("Anmälan", "VA, ventilation och eldstad anmäls före arbetet."),
    ("Bygget", "Grund, stomme och installationer fram till nyckelfärdigt."),
    ("Överlämning", "Genomgång av huset och beslut som ska sparas."),
  ],
  "rot_h2": "Nybyggnaden ger inte rotavdrag",
  "rot": [
    "Bland arbetena som inte ger rotavdrag på ett småhus nämner Skatteverket att bygga ett helt nytt hus, en friggebod, ett garage, ett växthus eller en liknande fristående byggnad. Ett komplementbostadshus i trädgården hör till den gruppen, så vi räknar huset utan avdrag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Nacka?",
  "price": [
    "Storlek och standard, kök och badrum, grundläggning på berg eller i sluttning, hur långt det är till befintliga ledningar och hur material kan bäras eller lyftas in på en kuperad tomt. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi bygga attefallshus nära Saltsjöbanan?",
     "Inom 30,0 meter från spårets mitt krävs bygglov, inom och utanför detaljplan. Lovfritt närmare spåret går bara med medgivande från infrastrukturförvaltaren."),
    ("Hur nära en kommunal park i Nacka kan attefallshuset stå?",
     "Närmare än 4,5 meter krävs skriftligt tillstånd från kommunen. Närmare än 2 meter medger kommunen bara undantagsvis."),
    ("Vad betyder orange markering på Nackas kulturmiljökarta?",
     "Att ett arbete med att bedöma de kulturhistoriska värdena kan pågå. Kommunen ber dig då kontakta stadsbyggnadsservice."),
    ("Kan vi bygga attefallshuset samtidigt som vår nya villa i Nacka?",
     "Enligt kommunen krävs minst ett interimistiskt slutbesked för villan innan ett lovfritt komplementbostadshus kan uppföras."),
    ("Ska grannemedgivandet för vårt attefallshus skickas till Nacka kommun?",
     "Nej. Kommunen skriver att medgivandet inte skickas in utan hanteras av de berörda parterna. Mot kommunägd mark krävs däremot kommunens skriftliga tillstånd."),
  ],
  "sources": [_PBL, _PBF, _BOV, _NAC_KMP, _NAC_KBH, _NAC_PLAC, _RUFS, _SKV],
  "cta": ("Funderar du på ett attefallshus i Nacka?", "Boka ett gratis platsbesök, så mäter vi gränser och avstånd innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet trähus med pulpettak på en kuperad tomt med tallar och en äldre panelvilla",
     "small modern dark green stained timber guest house with a mono-pitch roof on a hilly wooded garden plot with pine trees and granite, a large ornate early 1900s Swedish wooden panel villa with a veranda higher up the slope, Saltsjöbaden Nacka, late afternoon sun" + _SFX),
    ("Tomtgräns med låg häck mot ett skogsområde och utstakad husplats",
     "back edge of a Swedish villa garden with a low trimmed hedge marking the boundary towards a public pine and birch forest, wooden stakes and string marking a small house footprint a few metres inside the hedge, moss and granite, overcast daylight" + _SFX),
    ("Nybyggd villa och ett mindre trähus under uppförande på samma tomt",
     "newly built modern Swedish villa with white render and large windows on a rocky plot, next to it a smaller timber guest house under construction with a finished timber frame and roof underlay, construction materials neatly stacked, pine trees, clear day" + _SFX),
  ],
},

# ------------------------------------------------------------------ SOLLENTUNA
"attefallshus-sollentuna.html": {
  "kind": "district", "service": "attefallshus", "ort": "Sollentuna", "svc_label": "Attefallshus",
  "title": "Attefallshus i Sollentuna – radhus, villa och extra bostad",
  "description": "Attefallshus i Sollentuna: radhus och kedjehus, eget hus eller en bostad i villan, potten, imkanal och anmälan samt frivilligt bygglov med ritningar.",
  "h1": "Attefallshus i Sollentuna",
  "lead": "Bor du i radhus eller kedjehus i Sollentuna kan förutsättningarna för ett hus på tomten vara andra än för en fristående villa. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och jämför gärna med alternativet att inreda en bostad i det befintliga huset.",
  "card": "Radhus, villa och en extra bostad.",
  "sections": [
    {"id": "radhus-sollentuna", "anchor": "Radhus och kedjehus",
     "h2": "Radhus, kedjehus och sammanbyggda småhus",
     "paras": [
       "Ett komplementbostadshus ska enligt plan- och bygglagen komplettera ett en- eller tvåbostadshus, stå inom tomten och ha mindre byggnadsarea än huset det kompletterar. Sollentuna kommun skriver att möjligheterna att använda de lovbefriade åtgärderna skiljer sig för den som bor i ett radhus, kedjehus eller annat sammanbyggt småhus, beroende på hur bebyggelsen är utformad, och hänvisar till kommunens Kontaktcenter för vägledning.",
       "För en friliggande villa är förutsättningarna enklare att bedöma. I en radhuslänga eller ett kedjehusområde tar vi med fastighetsgränserna, husets byggnadsarea och vad som redan står på tomten till kommunen innan något ritas. Kommunen påpekar också att en lovbefriad komplementbyggnad som hör till något annat än ett en- eller tvåbostadshus måste stämma med detaljplanen, medan småhusens komplementbyggnader inte har samma krav.",
     ],
     "aside": {"title": "Fråga kommunen om", "items": [
       "Radhus och kedjehus", "Andra sammanbyggda småhus",
       "Tomtens fastighetsgränser", "Det som redan står på tomten"]}},
    {"id": "extra-bostad-sollentuna", "h2": "Ett hus i trädgården eller en bostad i villan",
     "paras": [
       "Den som vill ge plats åt ett vuxet barn eller en hyresgäst kan också inreda ytterligare en bostad i villan. Sollentuna kommun skriver att det i de flesta fall går utan bygglov i ett enbostadshus, men att du gör en anmälan och får startbesked innan arbetet börjar. Till anmälan hör situationsplan på tomtkarta, plan- och sektionsritningar, redovisning av ventilation, förslag på kontrollplan och en beskrivning av brandskyddet. Bygglov krävs om huset inte är ett enbostadshus eller om fastigheten eller byggnaden är kulturhistoriskt värdefull.",
       "Ett komplementbostadshus ger i stället en egen byggnad, men tar del av tomtens pott. Även det kräver anmälan när du installerar ventilation, vatten och avlopp, eldstad, rökkanal eller imkanal. Ska den extra bostaden inredas i ett nytt enbostadshus och strida mot detaljplanen skriver kommunen att lov för inredningen ska sökas samtidigt som bygglovet för huset. Om att bygga ut på höjden eller åt sidan finns mer under " + _L.format("tillbyggnad-sollentuna.html", "tillbyggnad i Sollentuna") + ".",
     ],
     "aside": None},
    {"id": "potten-sollentuna", "h2": "Två potter som är lätta att blanda ihop",
     "paras": [
       "Sollentuna kommun beskriver en sammanlagd pott per tomt för komplementbyggnader och komplementbostadshus: 45 kvadratmeter inom detaljplan och 65 kvadratmeter utanför. Tidigare attefallshus och friggebodar räknas in. En enskild byggnad inom detaljplan får vara högst 30 kvadratmeter och 4 meter till nocken.",
       "Tillbyggnader på huvudbyggnaden har en egen gräns. Enligt kommunen krävs bygglov när de lovbefriade tillbyggnaderna på ett en- eller tvåbostadshus sammanlagt blir mer än 30 kvadratmeter, och där räknas tidigare skärmtak och attefallstillbyggnader in. Med kommunens uppdelning tar ett gammalt skärmtak på villan alltså inte av attefallshusets yta, men en friggebod gör det. Vi går igenom tomten och skriver upp vad som finns innan ytan bestäms.",
     ],
     "aside": {"title": "Räknas in i potten", "items": [
       "Tidigare attefallshus", "Friggebodar",
       "Andra lovfria komplementbyggnader", "Inte skärmtak på villan"]}},
    {"id": "frivilligt-sollentuna", "h2": "Ansvaret ligger på dig – eller ett frivilligt lov",
     "paras": [
       "Kommunen skriver att många åtgärder inte längre granskas innan bygget börjar och att byggherren själv ansvarar för att lagens krav uppfylls, bland annat att det som byggs är lämpligt utformat och anpassat. Ligger fastigheten inom ett kulturhistoriskt särskilt värdefullt område krävs bygglov, och huset får inte heller placeras närmare än 30,0 meter från ett järnvägsspårs mitt utan infrastrukturförvaltarens skriftliga medgivande.",
       "Vill du vara säker kan du söka ett frivilligt bygglov, och byggnadsnämndens beslut visar då att huset uppfyller kraven. För en ansökan om bygglov för en komplementbyggnad räknar kommunen upp ansökan via e-tjänst, förslag på kontrollplan, situationsplan och plan-, fasad- och sektionsritningar, och i vissa fall anmälan av kontrollansvarig. Fler projekt på villatomten beskrivs under " + _L.format("byggforetag-sollentuna.html", "byggföretag i Sollentuna") + ", och mått och paragrafer i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Sollentuna",
  "steps": [
    ("Hustypen", "Villa, kedjehus eller radhus – vi tar reda på vad som gäller för tomten."),
    ("Alternativen", "Fristående hus eller en ytterligare bostad i villan."),
    ("Potten", "Befintliga bodar och tidigare attefallshus räknas in."),
    ("Anmälan eller lov", "Ritningar, kontrollplan och vid behov frivilligt bygglov."),
    ("Bygget", "Grund, stomme, installationer och ytskikt – nyckelfärdigt."),
    ("Avslut", "Slutgenomgång och handlingarna du behöver spara."),
  ],
  "rot_h2": "Rotavdrag och en ny bostad",
  "rot": [
    "Skatteverket ger inget rotavdrag för att bygga ett helt nytt hus eller en liknande fristående byggnad, och det ges inte heller något rotavdrag för att bygga en helt ny bostad. Ett attefallshus räknas därför utan avdrag. För arbete i ett befintligt småhus ställer Skatteverket bland annat kravet att bostaden är äldre än fem år och att större delen av den ursprungliga stommen behålls, så vid en bostad i villan stämmer vi av arbetet mot reglerna innan kostnadsförslaget skrivs.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Sollentuna?",
  "price": [
    "Husets storlek och planlösning, kök och badrum, grundläggning, avståndet till villans ledningar och hur material kan bäras in mellan sammanbyggda hus. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi bygga ett attefallshus på vår radhustomt i Sollentuna?",
     "Det beror på hur bebyggelsen är utformad. Kommunen skriver att möjligheterna skiljer sig för radhus, kedjehus och andra sammanbyggda småhus och ger vägledning via Kontaktcenter."),
    ("Är det enklare att inreda en extra bostad i villan än att bygga ett attefallshus i Sollentuna?",
     "Inte nödvändigtvis. Båda kräver i regel anmälan och startbesked, och för en bostad i villan vill kommunen också ha en beskrivning av brandskyddet."),
    ("Räknas vårt gamla skärmtak in när vi bygger attefallshus i Sollentuna?",
     "Nej, enligt kommunen räknas skärmtak till tillbyggnaderna på huvudbyggnaden. Tidigare attefallshus och friggebodar räknas däremot in i tomtens pott."),
    ("Behöver imkanalen i attefallshusets kök anmälas i Sollentuna?",
     "Ja. Kommunen räknar upp installation av imkanal bland det som kräver anmälan, tillsammans med ventilation, vatten och avlopp, eldstad och rökkanal."),
    ("Vilka handlingar behövs för att söka bygglov för ett attefallshus i Sollentuna?",
     "Kommunen räknar upp ansökan via e-tjänst, situationsplan, plan-, fasad- och sektionsritningar och förslag på kontrollplan. I vissa fall behövs också en anmälan av kontrollansvarig."),
  ],
  "sources": [_PBL, _PBF, _BOV, _SOL_KB, _SOL_ATT, _SOL_NYA, _SOL_YTT, _SKV],
  "cta": ("Funderar du på ett attefallshus i Sollentuna?", "Boka ett gratis platsbesök, så går vi igenom tomten och alternativen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet trähus i trädgården bakom ett kedjehus i tegel och trä",
     "small light beige timber guest house with a gable roof and a small porch at the back of a garden behind a 1970s Swedish brick and wood link house, lawn, apple tree and wooden fence, Sollentuna Stockholm suburb, sunny summer afternoon" + _SFX),
    ("Ljust litet rum med pentry och fönster mot trädgården i ett nybyggt gästhus",
     "interior of a newly built small Swedish guest house, bright open room with a compact white kitchenette and a range hood, light oak floor, white walls, large window towards a green garden, empty and tidy, soft daylight" + _SFX),
    ("Hoprullade ritningar och en tumstock på ett trädgårdsbord framför ett nybyggt litet trähus",
     "rolled-up blank architectural drawing sheets held by a rubber band and a yellow folding ruler on a wooden garden table, in the background a newly built small light beige timber guest house with a gable roof on the lawn of a Swedish suburban villa plot, apple tree, soft overcast daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ TYRESÖ
"attefallshus-tyreso.html": {
  "kind": "district", "service": "attefallshus", "ort": "Tyresö", "svc_label": "Attefallshus",
  "title": "Attefallshus i Tyresö – VA, vattenmätare och dagvatten",
  "description": "Attefallshus i Tyresö: stegen till kommunalt VA, egen vattenmätare, anläggningsavgift för ett nytt boende och regnvattnet från det nya taket.",
  "h1": "Attefallshus i Tyresö",
  "lead": "Ett attefallshus med toalett, hygien- och matlagningsmöjligheter klassas av Tyresö kommun som ett nytt boende, och det märks när huset ska anslutas till vatten och avlopp. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och planerar ledningarna, vattenmätaren och regnvattnet tillsammans med huset.",
  "card": "VA-anslutning, vattenmätare och dagvatten.",
  "sections": [
    {"id": "va-steg-tyreso", "anchor": "VA-anslutningen",
     "h2": "Sju steg till kommunalt vatten och avlopp",
     "paras": [
       "Tyresö kommun skriver att du kan ansluta till det kommunala ledningsnätet även i ett äldre område där det finns ledningar, till exempel när du har byggt ett attefallshus. Kommunens steg är: gör en anmälan, få en anvisad förbindelsepunkt, betala anläggningsavgiften, beställ uppsättning av vattenmätare, anslut till nätet, ansök om slutbesked och betala sedan brukningsavgift varje kvartal.",
       "Anmälan görs till kommunen och följs av ett startbesked. Till den hör en situationsplan på tomtkarta där vatten-, avlopps- och dagvattenledningar ritas in från anslutningspunkten till huset, och dagvattnet också om det leds till en stenkista. Dessutom behövs ett förslag till kontrollplan, och kommunen har ett exempel för VA-anslutning. Förbindelsepunkten ligger normalt vid fastighetsgränsen. Kommunen ansvarar för ledningarna fram dit och du för ledningarna inom fastigheten.",
     ],
     "aside": {"title": "Kommunens steg", "items": [
       "Anmälan och startbesked", "Förbindelsepunkt och avgift",
       "Vattenmätare och anslutning", "Slutbesked"]}},
    {"id": "matare-tyreso", "h2": "Egen vattenmätare och två sätt att dra in vattnet",
     "paras": [
       "När ett komplementbostadshus ansluts till det kommunala nätet i Tyresö ska den nya byggnaden vara ansluten till en vattenmätare. Kommunen beskriver två alternativ. Antingen dras husets vattenledning vidare efter villans befintliga vattenmätare, eftersom servisledningen fram till mätaren ska vara obruten. Eller så tas vattnet från servisledningen mellan förbindelsepunkten och villans mätare, och då ska sammankopplingen besiktigas av VA-avdelningen och en ny vattenmätare installeras i eller före det nya huset.",
       "För avlopp och dagvatten finns enligt kommunen inga motsvarande restriktioner, så husets avloppsledning kan kopplas ihop med fastighetens befintliga ledning som går till den kommunala huvudledningen. Har du i dag ett enskilt avlopp med slamtömning och går över till det kommunala nätet ska du meddela kommunens avfallsfunktion, så att en sluttömning kan göras. Vilket alternativ som passar avgörs av var villans mätare sitter och var huset ska stå, och det är något vi bestämmer innan schaktet planeras.",
     ],
     "aside": None},
    {"id": "avgift-tyreso", "h2": "Ett nytt boende i VA-taxans mening",
     "paras": [
       "Tyresö kommun skriver att en komplementbyggnad eller ett komplementbostadshus med toalett, hygien- och matlagningsmöjligheter ger en ny anläggningsavgift för vatten och avlopp, även om avgiften redan har betalats för det ursprungliga bostadshuset. Skälet är att den nya byggnaden klassas som ett nytt boende, och för ett komplementbostadshus ligger avgiften på samma nivå som en lägenhetsavgift. Storleken styrs av VA-taxan.",
       "Varje vattenmätare ger dessutom en egen årlig avgift enligt taxan, så två mätare ger dubbla årliga VA-avgifter. Det är värt att väga in när du väljer mellan de två sätten att ansluta vattnet. I omvandlingsområden där kommunen bygger ut kommunalt vatten och avlopp, till exempel Raksta etapp 8, kan fastighetsägare ansöka om lån för anläggningsavgifter och gatukostnad. Om byggrätten i omvandlingsområdena finns mer under " + _L.format("tillbyggnad-tyreso.html", "tillbyggnad i Tyresö") + ".",
     ],
     "aside": {"title": "Tänk på", "items": [
       "Ny anläggningsavgift", "Avgift per vattenmätare",
       "Taxan styr beloppet", "VA-lån i omvandlingsområden"]}},
    {"id": "dagvatten-tyreso", "h2": "Regnet från det nya taket",
     "paras": [
       "Ett nytt hus med uteplats ökar de hårda ytorna på tomten. Tyresö kommun skriver att du som fastighetsägare ansvarar för dagvattnet på din fastighet, och ger råd om hur det kan hanteras: begränsa andelen asfalt och stenläggning och välj hellre grus, stenmjöl eller genomsläpplig marksten, anlägg växtytor i tomtens låga delar och spara träd. Enligt kommunen kan ett träd med mycket blad dricka upp till cirka 500 liter vatten per dygn.",
       "Kommunen råder också att marken runt ett hus ska luta bort från byggnaden och att huset inte ska stå i en lågpunkt eller svacka där vatten samlas. Det påverkar var på tomten vi föreslår att attefallshuset placeras. Själva huset kan enligt kommunen byggas utan bygglov inom detaljplan upp till 30 kvadratmeter och 4 meter till nocken, med 45 kvadratmeter sammanlagt, utom i ett kulturhistoriskt särskilt värdefullt område, men anmälan krävs när vatten och avlopp installeras i byggnaden eller inom tomten eller när en eldstad sätts in. Om gäststugor och förråd finns mer under " + _L.format("snickare-tyreso.html", "snickare i Tyresö") + ", och mått och paragrafer i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Tyresö",
  "steps": [
    ("Platsbesök", "Var villans vattenmätare sitter, var ledningarna går och hur tomten lutar."),
    ("Placering", "Huset placeras med hänsyn till gräns, ledningar och regnvatten."),
    ("VA-underlag", "Situationsplan med ledningar och förslag till kontrollplan."),
    ("Anmälan", "Startbesked, förbindelsepunkt och beställning av vattenmätare."),
    ("Bygget", "Grund, stomme, installationer och anslutning – nyckelfärdigt."),
    ("Slutbesked", "Ansökan om slutbesked när installationen är klar."),
  ],
  "rot_h2": "Varför priset anges utan rotavdrag",
  "rot": [
    "Rotavdrag gäller arbete i eller nära en bostad som kunden äger. Skatteverket skriver att det inte går att få rotavdrag för att bygga en helt ny bostad, och ett nytt hus eller en liknande fristående byggnad på småhustomten ger inget avdrag. Ett komplementbostadshus är både en ny bostad och en ny byggnad, så kostnadsförslaget är utan avdrag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Tyresö?",
  "price": [
    "Storlek och planlösning, kök och badrum, grund på berg eller lera, avståndet till villans vattenmätare och avloppsledning och hur dagvattnet ska tas om hand. VA-avgifterna till kommunen kommer utöver vårt arbete. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste attefallshuset i Tyresö ha en egen vattenmätare?",
     "Det ska vara anslutet till en vattenmätare. Antingen dras vattnet vidare efter villans mätare, eller så tas det från servisledningen före mätaren, och då krävs en ny mätare och besiktning av sammankopplingen."),
    ("Varför tar Tyresö kommun ut anläggningsavgift igen för vårt attefallshus?",
     "Med toalett, hygien- och matlagningsmöjligheter klassas huset som ett nytt boende, och då tas en ny anläggningsavgift ut även om villan redan har betalat sin."),
    ("Får attefallshusets avlopp kopplas till villans avloppsledning i Tyresö?",
     "Ja. Kommunen skriver att det inte finns några restriktioner för avlopp och dagvatten, så den nya ledningen kan kopplas till fastighetens befintliga."),
    ("Vad ska situationsplanen visa när attefallshuset ansluts till VA i Tyresö?",
     "Vatten-, avlopps- och dagvattenledningar från anslutningspunkten till huset, och dagvattnet om det leds till en stenkista. Den ritas på en tomtkarta."),
    ("Vi har slamtömning i dag – vad händer när vi ansluter till kommunalt avlopp i Tyresö?",
     "Du meddelar kommunens avfallsfunktion, så att en sluttömning av det enskilda avloppet kan göras."),
  ],
  "sources": [_PBL, _PBF, _BOV, _TYR_PBL, _TYR_ANSL, _TYR_DAG, _SKV],
  "cta": ("Funderar du på ett attefallshus i Tyresö?", "Boka ett gratis platsbesök, så går vi igenom ledningar, mätare och placering innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet grått trähus med sadeltak i en villaträdgård med tallar och berg",
     "small newly built Swedish timber guest house painted warm grey with white window frames and a black gable roof in a villa garden with pine trees and smooth granite, a 1980s yellow wooden villa in the background, Tyresö Stockholm, bright summer day" + _SFX),
    ("Vattenmätare och ventiler på en vägg i ett litet teknikutrymme",
     "close-up of a closed white plastic water meter housing without any display, brass shut-off valves and blue PEX pipes mounted on a white wall in a small utility space of a newly built guest house, neat pipe clamps, floor drain below, clean and tidy, soft indoor light" + _SFX),
    ("Grusgång och växtbädd som tar hand om regnvatten bredvid ett litet trähus",
     "small timber guest house in a Swedish garden with a downpipe leading rainwater into a planted rain garden bed with grasses and stones, permeable gravel path beside the house, ground sloping away from the building, birch trees, after rain, overcast light" + _SFX),
  ],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"attefallshus-osteraker.html": {
  "kind": "district", "service": "attefallshus", "ort": "Österåker", "svc_label": "Attefallshus",
  "title": "Attefallshus i Österåker – uthyrning och kulturmiljö",
  "description": "Attefallshus i Österåker: gäststuga eller bostad att hyra ut, lovplikt i kulturmiljöer, k och q i detaljplanen, fornlämningar och tillsyn i efterhand.",
  "h1": "Attefallshus i Österåker",
  "lead": "Ska det lilla huset på tomten bli en gäststuga för sommaren eller en bostad att hyra ut året runt? I Österåker är det en fråga om både krav och lov. Geal Entreprenad AB bygger komplementbostadshus nyckelfärdigt och tar reda på vad som gäller för tomten innan vi ritar.",
  "card": "Uthyrning, kulturmiljö och fornlämningar.",
  "sections": [
    {"id": "uthyrning-osteraker", "anchor": "Uthyrning",
     "h2": "Gäststuga eller bostad att hyra ut",
     "paras": [
       "Österåkers kommun skiljer tydligt på de två. En komplementbyggnad, till exempel ett förråd, ett garage eller en gäststuga, får inte inredas till bostad. Ett komplementbostadshus är en fullt utrustad bostad som får byggas som komplement till ett en- eller tvåbostadshus. Det får hyras ut, men bara om byggnaden uppfyller Boverkets regler och kraven på en bostad och inte ger för stor omgivningspåverkan. Kommunen nämner tillgänglighet, ventilation och energiförbrukning.",
       "Kommunen sammanfattar konsekvensen kort: du kan inte bygga en gäststuga och hyra ut den som bostad. Därför börjar vi med frågan om vad huset ska användas för. Ska det hyras ut ritar vi det som en bostad från början, med kök, badrum, ventilation och isolering, och anmäler installationerna för vatten, avlopp och ventilation enligt plan- och byggförordningen innan de görs.",
     ],
     "aside": {"title": "Bostad att hyra ut", "items": [
       "Boverkets krav på bostad", "Tillgänglighet",
       "Ventilation", "Energiförbrukning"]}},
    {"id": "kulturmiljo-osteraker", "h2": "Kulturmiljöerna – från Åkers kanal till Roslags-Kulla",
     "paras": [
       "Österåkers kommun har enligt sin egen sida fyra riksintressen för kulturmiljövården: Roslags-Kulla, Rydboholm, Vira bruk och Åkers kanal. Region Stockholm beskriver Åkers kanal (AB 62) som kanal- och farledsmiljö och Roslags-Kulla (AB 63) som herrgårdslandskap och sockencentrum. Runt Roslags-Kulla kyrka och Österåkers kyrka finns dessutom landskapsbildsskydd, och där kräver en ny byggnad dispens från Länsstyrelsen. Kommunen skriver att bygglov krävs om fastigheten ligger i ett kulturhistoriskt särskilt värdefullt område eller om byggnaden är särskilt värdefull, och det gäller även att bygga nytt.",
       "Österåkerskartan visar områden med kulturhistoriska värden, och eftersom flera lagar skyddar dem kan kartan visa miljöer som överlappar varandra. I en detaljplan kan en byggnad ha skyddsbestämmelser. Kommunen förklarar att ett litet k betyder att byggnaden ska behandlas varsamt och ett litet q att den inte får rivas. Kommunen påpekar också att inte bara slott och äldre byggnader kan ha kulturvärden – även enkla, vardagliga byggnader och yngre bebyggelse kan ha det. I kommunens checklista finns frågor som vi går igenom vid platsbesöket: har detaljplanen skyddsbestämmelser för huset, ligger det i eller nära ett kulturmiljöområde, finns det med i en inventering eller ett kulturmiljöprogram och har det en bevarad, tidstypisk karaktär? Ett ja på någon av frågorna kan betyda att huset är värdefullt.",
     ],
     "aside": None},
    {"id": "fornlamning-osteraker", "h2": "Fornlämning på tomten",
     "paras": [
       "En del av kommunens checklista för värdefulla hus handlar om marken: finns det fornlämningar på tomten? Kommunen skriver att det inte behöver betyda att huset är särskilt värdefullt, men att platsen kan ha en lång historia och behöva undersökas. Riksantikvarieämbetets karta Fornsök visar fornlämningarna, och vill du bygga något på en tomt med fornlämningar behöver du söka tillstånd hos Länsstyrelsen. Kommunen ger en pool som exempel, och vår bedömning är att samma fråga behöver ställas inför grunden till ett nytt hus.",
       "När en fastighet berörs av kulturvärden föreslår kommunen att du anlitar en expert på kulturmiljö, till exempel en antikvarie, som kan ge råd om hur påverkan på kulturvärdena kan minskas. Vi kontrollerar Fornsök och Österåkerskartan när vi mäter upp tomten, så att placeringen kan anpassas innan ritningarna är klara.",
     ],
     "aside": {"title": "Kontrollera tidigt", "items": [
       "Österåkerskartan", "Fornsök",
       "Skydd i detaljplanen", "Strandskydd"]}},
    {"id": "tillsyn-osteraker", "h2": "Ingen granskning i förväg – men tillsyn i efterhand",
     "paras": [
       "Kommunen skriver att den inte granskar dina byggplaner innan du börjar när åtgärden är lovfri, och att du själv ansvarar för att bygget följer reglerna. Bygger du fel kan kommunen ingripa i efterhand med tillsyn, och det kan innebära en byggsanktionsavgift eller att det byggda måste rivas. Söker du frivilligt bygglov prövar kommunen i stället om huset ryms inom kraven för de lovfria åtgärderna och lämnar ett beslut.",
       "Kommunen har också checklistor över vilka ritningar som ska skickas in för en ny komplementbyggnad eller ett nytt komplementbostadshus. Ligger tomten inom strandskydd måste du enligt kommunen oftast söka dispens även när huset inte kräver bygglov, och nära Roslagsbanan gäller 30-meterszonen. Om grannmedgivanden och utstakning finns mer under " + _L.format("tillbyggnad-osteraker.html", "tillbyggnad i Österåker") + ", om bryggor och äldre hus under " + _L.format("snickare-osteraker.html", "snickare i Österåker") + " och om mått och paragrafer i " + _REG + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi ett attefallshus i Österåker",
  "steps": [
    ("Användningen", "Gäststuga eller bostad att hyra ut – det styr kraven."),
    ("Kartorna", "Österåkerskartan, detaljplanen och Fornsök för just din tomt."),
    ("Lovväg", "Lovfritt, frivilligt bygglov eller bygglov."),
    ("Ritningar", "Enligt kommunens checklista och anmälan för installationer."),
    ("Bygget", "Grund, stomme, installationer och ytskikt – nyckelfärdigt."),
    ("Avslut", "Genomgång och handlingar att spara inför eventuell tillsyn."),
  ],
  "rot_h2": "Rotavdrag och ett nytt hus på tomten",
  "rot": [
    "Skatteverket räknar att bygga ett helt nytt hus eller en liknande fristående byggnad till arbeten som inte ger rotavdrag, och inte heller att anlita en arkitekt, en besiktningsman eller liknande. Ett komplementbostadshus är nybyggnad, så både projektering och bygge ligger utan avdrag i vårt kostnadsförslag.",
  ],
  "price_h2": "Vad påverkar priset på ett attefallshus i Österåker?",
  "price": [
    "Om huset ska vara gäststuga eller bostad, storlek och standard, grundläggning, avstånd till ledningar och om kulturvärden eller fornlämningar påverkar placering och utförande. Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi hyra ut gäststugan i Österåker som bostad?",
     "Inte om den är byggd som komplementbyggnad. Kommunen skriver att en sådan inte får inredas till bostad. Ett komplementbostadshus får hyras ut om det uppfyller kraven på en bostad."),
    ("Vad betyder litet k och litet q i en detaljplan i Österåker?",
     "Enligt kommunen betyder k att byggnaden ska behandlas varsamt och q att den inte får rivas."),
    ("Hur tar vi reda på om det finns en fornlämning där attefallshuset ska stå?",
     "I Riksantikvarieämbetets karta Fornsök. Ska du bygga på en tomt med fornlämningar behöver du tillstånd från Länsstyrelsen."),
    ("Vad händer om vårt lovfria attefallshus i Österåker inte följer reglerna?",
     "Kommunen kan ingripa i efterhand med tillsyn, och det kan leda till byggsanktionsavgift eller att det byggda måste rivas."),
    ("Är Roslags-Kulla ett riksintresse för kulturmiljövården?",
     "Ja. Kommunen räknar Roslags-Kulla till sina fyra riksintressen för kulturmiljövården, och Region Stockholm listar området (AB 63) med herrgårdslandskap och sockencentrum."),
  ],
  "sources": [_PBL, _PBF, _BOV, _OST_KB, _OST_KULT, _RUFS, _SKV],
  "cta": ("Funderar du på ett attefallshus i Österåker?", "Boka ett gratis platsbesök, så går vi igenom användning, kartor och placering innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet rödmålat trähus med vita knutar på en tomt i ett öppet odlingslandskap",
     "small new falu red wooden guest house with white corner boards and a black metal gable roof on a lawn beside an older Swedish country house, open farmland, stone walls and old oak trees behind, Roslagen Österåker countryside, early summer afternoon" + _SFX),
    ("Gammal kanalmiljö med stenkajer och trähus i skärgårdslandskap",
     "historic narrow canal with old stone embankments and a small wooden bridge in the Roslagen landscape north-east of Stockholm, red and white wooden houses among trees along the water, calm summer morning" + _SFX),
    ("Nyfärdigt, tomt rum i ett litet trähus med en stängd pärm och en tumstock i fönsterkarmen",
     "interior of a newly finished small Swedish timber guest house, empty bright room with white painted wood panel walls and a light pine floor, a closed plain grey ring binder and a yellow folding ruler lying on the deep windowsill, window view to a green rural garden with oak trees, soft daylight" + _SFX),
  ],
},

}
