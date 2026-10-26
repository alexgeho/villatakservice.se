# -*- coding: utf-8 -*-
"""Fönsterrenovering – ortsidor v19: Haninge, Järfälla, Kungsholmen, Sollentuna, Solna, Södermalm (2026-10-26).
Deltjänst under fonsterbyte.html (TJ_HUB["fonsterrenovering"]). Intent: renovera de befintliga fönstren i stället
för att byta dem. Skild från ortens fonsterbyte-<ort>.html (lov, spröjs, buller, fönsterhistorik) och från v16-sidorna
(Bromma, Danderyd, Huddinge, Nacka, Norrtälje, Sigtuna) – inga lokala vinklar, formuleringar eller FAQ återanvända.
Lokal vinkel per sida (en huvudfråga per sida):
Haninge – gårdarna på landsbygden: kommunens råd för den agrara miljön (bevara ursprungliga fönster, mittposten),
ladugårdarnas spröjsade fönster 1890–1940, snedställd bräda kontra bleck, målning i rätt tid; rotavdrag på
lantbruksenhet (inte ekonomibyggnader);
Järfälla – fönstrets nederkant: bottenstycken, bleck och fönsteromfattning på Stäkets och Bonäs villor
(kulturmiljöplanen), lovfrågan vid ny kulör, rotavdrag för fönsterbleck i småhus men inte i bostadsrätt;
Kungsholmen – fönstret i bostadsrätten: stadgarna och bostadsrättslagen 7 kap. 4, 12 och 13 §§, vad som ger rotavdrag
på insidan, 1930-talets kopplade inåtgående bågar som kärvar (justering, hyvling, lister);
Sollentuna – täta gamla fönster i villastaden utan att strypa tilluften: Boverkets varning om äldre ventilation,
kondens utvändigt, RAÄ:s regler för lister, kommunens sidor om ventilation och anmälan;
Solna – 1950-talets miljöer i stadens lista: asbest/PCB i kitt och fogar, tillstånd för sanering, kopplade bågar och
linoljefärg, lov för ny kulör på flerbostadshus och föreningens medgivande;
Södermalm – föreningens fönster i stenstaden: konditionsbesiktning före byte (RAÄ:s exempel från 1903 med 215
fönster), droppnäsa/bleck/spanjolett, Stadsmuseets klasser, utökad lovplikt, PBL 8 kap. 14 §.

Fakta endast från källorna i respektive 'sources', öppnade och lästa med curl 2026-10-26 (alla svarade 200; pdf:er
med textlager via pdftotext):
  Skatteverket – Ger arbetet rätt till rotavdrag? (småhus: reparera eller byta ut fönster, måla fönster, byta och
  reparera fönsterbleck, sanera asbest i samband med byggarbete; inget avdrag för att mäta asbest; plåt- och
  glasarbeten i företagets lokaler ger inget avdrag; bostadsrätt: innanför tak, väggar och golv och enligt stadgarna,
  arbete på insidan av befintliga fönster t.ex. glas i inre bågen och tätningslist, byta och reparera innerfönster
  och fönsterfoder, måla insidan av fönster; inget avdrag för att byta fönster och gångjärn, arbeta mellan eller på
  utsidan, måla utsidan, fönsterbleck, gemensamma ytor som fasader).
  Skatteverket – Så fungerar rotavdraget (30 procent av arbetskostnaden, material och resor ger inget avdrag,
  75 000/50 000 kr, äga bostaden, fritidshus, komplementhus som garage och förråd del av bostaden i småhus, småhus på
  lantbruksenhet – inget avdrag för ekonomibyggnader eller utanför tomten, flera ägare högst 30 procent sammanlagt,
  faktureras eller betala, bostadsrättsföreningens organisationsnummer och lägenhetsnummer vanligen fyra siffror,
  bara arbetad tid på plats, elektronisk betalning sedan 1 januari 2020, avdrag på fakturan).
  Riksdagen – bostadsrättslag 1991:614, 7 kap. 4 § (föreningen håller lägenheten, huset och marken i gott skick i den
  mån ansvaret inte vilar på bostadsrättshavaren), 12 § (bostadsrättshavaren håller lägenheten i gott skick om inte
  annat bestämts i stadgarna), 13 § (tillträde för arbete som föreningen svarar för; inte större olägenhet än
  nödvändigt). Plan- och bygglag 2010:900, 8 kap. 14 § (vårdat skick, underhåll så att utformning och tekniska
  egenskaper i huvudsak bevaras; särskilt värdefullt – underhållas så att de särskilda värdena bevaras).
  Riksantikvarieämbetet – Fönster: historik och råd vid renovering (RAÄ 1988:1, OCR-text, läsbar): spanjolett vid
  fönster utan mittpost, koppelhakar; fönsterbleck – snedställd bräda på trähus, järnplåt på större stenhus,
  inslagskant i spår, karmbottenstycke med droppnäsa i stenhus under senare 1800-tal, bleck som täcker hela
  karmbottenstycket vanligt från sekelskiftet; ordlistan (droppnäsa, foder, fönsterbleck, mittpost nödvändig vid
  klenare konstruktion med hakar); linoljefärg förespråkades ännu på 1950-talet, grundning och två strykningar enligt
  Hantverkets bok 1953; rötskador där väta trängt in och torkar långsamt, samband röta–rost, 1960–70-talens fönster och
  olämpligt lösta konstruktionsdetaljer; skador under hörnbeslag och i fogar; karmbottenstycke – i allmänhet räcker
  att limma in nytt virke i yttre delen; virkeskrav före 1950-talet (vinteravverkat, lufttorkat, lagrat ett par år),
  reparationsvirke ska likna det gamla; kopplade bågar tunga, sluter inte alltid tätt, igengrodda kopplingsbeslag,
  nya handtag och stängningsbeslag; tätningslister av gummi, profiltyper, innerbågen ska tätas, måla och justera före
  listerna, modellera för springbredd, för tjock list ger spänningar; bågar slängs i container vid ombyggnader –
  oftast inte för att de är dåliga utan för att kostnaden är svår att beräkna, konditionsbesiktning, exempel 25 %
  droppnäsor och 10 % karmbottenstycken; exempel 1903 kv Sparven vid Birger Jarlsgatan (kopplade inåtgående,
  summarisk besiktning dömde ut, nära 70 % av 215 fönster besiktigade, droppnäsor 41 %, glasningslister 66 %,
  kärnfuru, övre bågar originaldelar kvar); exempel 1937 smalhus Uppsala (kopplat inåtgående, nästan kvadratiskt,
  utan mittpost, överfalsad innerbåge med plats för list, vädringsventil i bröstningen, inga rötskador men svåra att
  öppna och stänga, justering, hyvling, gummilister).
  Länsstyrelserna i Gävleborgs, Västmanlands och Örebro län – Fönster (pdf med text: nedre delen särskilt utsatt,
  rötskador i bågens och karmens bottenstycken, röta bakom hörnjärnen, rostiga beslag kan oftast renoveras, kopior
  finns, kopplat fönster med två utåtgående bågar under första hälften av 1900-talet; bladets kostnadstabell i kr är
  medvetet INTE använd); Målning utomhus på trä (pdf med text: fönster och dörrar målas om oftare än fasader,
  söderfasader oftare, blästring och maskinslipning skadar träet, högtryckstvätt pressar in vatten, plastfärg bildar
  en hinna som måste bort, fönster under 1800-talets andra hälft ofta rött, brunt eller grönt).
  Boverket – Energiguiden: fönster och dörrar (täta – isolering runt karmen, drevning, lister, energiförluster ökar
  markant, äldre ventilationssystem kan räkna med luft genom otäta fönster, kontrollera tilluft, kondens utvändigt,
  energiglas/tvåglaskassett på insidan, fogmassor med PCB eller asbest saneringspliktigt); Risker med asbest
  (förbud 1982, främst 1940–1970, 1940–1980 sannolikt, listan med fönsterkitt, tätmassor, fogmassor, prov i
  mikroskop).
  Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest (tillstånd för företag, förarbete, avfall och
  städning räknas som sanering).
  Stockholms stad – Områdesfakta: Kungsholmens stadsdelsområde (bostäder 2024: 44 554, 30 598 bostadsrätter, 337 i
  småhus); Södermalms stadsdelsområde (bostäder 2025: 77 525, 43 680 bostadsrätter, 211 i småhus, 73 952 i
  flerbostadshus och övriga hus). Översiktsplan – Riksintressen enligt miljöbalken (pdf med text: klassiska
  stenstaden 1870–1930 på Östermalm, Södermalm, Kungsholmen och Norrmalm; nya funktionalistiska stadsdelar omkring
  1930 bl.a. Fredhäll och Kristineberg; tidig bebyggelse på malmarna – Fjällgatan, Katarinaberget, Vita bergen,
  Åsöberget, Östra Mariaberget, byggnadsdetaljer som fönster, entréportar och ornamentik; Draget och Ryssjan vid
  Blecktornsparken 1920-talet; många stenstadshus gul klass för att de förändrats, betydelsen för stadsmiljön
  avgörande). bygglov.stockholm: Fönster och dörrar (listan över ändringar, beror på byggnaden, informera grannar eller
  styrelsen); Stadsmuseets kulturhistoriska klassificering (blått/grönt/gult/grått, bygglov för blå/gröna och inom
  riksintresse); Kulturhistorisk värdefull byggnad och område (utökad lovplikt t.ex. underhållsåtgärder, antikvarisk
  förundersökning).
  Haninge kommun – Haninges karaktärsmiljöer (pdf med text: agrara miljön – renovering och underhåll, vårdat skick,
  fönster starkt karaktärsbärande, ursprungliga fönster bevaras i möjligaste mån, vid byte ursprunglig utformning;
  komplementbyggnader i regel fristående; nya fönster symmetriskt, kvadratiska eller stående, mittposten viktig;
  ladugårdar 1890–1940 med spröjsade fönster, schweizerstil till nationalromantik; egnahemsområden 1910–1940 i
  Tungelsta, Vendelsö, Vendelsömalm, Handen, Västerhaninge, Norrby med enkelt spröjsade fönster, ursprunglig
  utformning och färgsättning ska värnas; antikvarisk sakkunnig vid bygglov som påverkar värdena).
  Järfälla kommun – Kulturmiljöplan Stäket (pdf med text: villasamhället, första villorna 1904, färgsättning
  ursprungligen rött eller ljusa oljefärger, individuell utformning med omsorg om detaljer, förslag om q och utökad
  lovplikt på Gyllenstiernas väg; Bonäs – Frans Hallberg 1907, rödfärgad panel, Bonäsvägen 27 gulmålad, vita
  fönsteromfattningar och snickerier); Fasadändring (inget lov för en- och tvåbostadshus utom särskilt värdefullt
  och utökad lovplikt; nya fönster och byte av färg som exempel).
  Sollentuna kommun – Översiktsplan med sikte på 2040 (pdf med text: järnvägen 1866, Rotebro, Tureberg och Norrviken i
  början av 1900-talet, småhus och villor, villastadens prägel från 1900-talets första hälft, Norrvikens villastad,
  Väderholmen och Skansen, inte medge förtätningar som förutsätter rivning av funktionella bostadshus);
  Kulturhistoriska byggnader och områden (bygglovsbefriade åtgärder gäller inte, kan vara värdefull utan att stå i
  planen); Ventilation (tecken på dålig ventilation, villaägare kontaktar konsultföretag); Installation eller ändring
  av ventilation (anmälan och startbesked, även större ändring – aggregat, fläkt, kanaler).
  Solna stad – Kulturmiljöer i Solna (lista över sammanhängande miljöer med fyra 1950-talsmiljöer, helhetsintrycket,
  ursprunglig karaktär); Fasadändring (lov för fasad mot allmän plats på andra byggnader än en- och tvåbostadshus inom
  detaljplan, särskilt värdefullt, exempel byte av färg och nya fönster); För lägenhetsinnehavare (fastighetsägarens
  medgivande); För villaägare (utökad lovplikt i stora delar, vanligaste anledningar kulturmiljöer och riksintressen).
Strukna (ej verifierade eller medvetet utelämnade): Södra Maria-inventeringen 1978 (pdf:ens OCR är sönderspärrad –
inte använd); Sollentunas och Solnas kulturmiljöprogram i pdf (hittades inte); att kopplade fönster sitter i just
Fredhäll/Kristineberg eller i Solnas 1950-talshus (skrivs som RAÄ:s exempel och Länsstyrelsens allmänna datering);
att Draget och Ryssjan ligger på Södermalm uttryckligen (källan säger "vid Blecktornsparken" – så skrivet);
Stadsmuseets svarstid och telefonnummer, Arbetsmiljöverkets ansökningstid, kommunernas handläggningstider; att en
bostadsrättsförening kan eller inte kan få rotavdrag (Skatteverket säger inget uttryckligt – bara bostadsrättshavarens
regler skrivna); att justering av gångjärn ger rotavdrag (bara byte av gångjärn nämns – utelämnat); Boverkets
rättsfall om fönsterbyten (handlar om byte); alla priser, tidsåtgång, fönsterantal och bladets kostnadstabell.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert. Perks enbart sajtens befintliga: gratis
platsbesök, skriftligt kostnadsförslag, ROT direkt på fakturan, en kontakt.
Kritikpass 2026-10-26 (alla källor öppnade igen, varje faktamening mot källtexten): Haninge – rådet om dörrars och
fönsters "ursprungliga utformning och färgsättning" hör till folkhemsbyggets småhus 1940–1960, inte egnahemmen
(omskrivet: egnahem = träpanel, enkelt spröjsade fönster, ursprungligt arkitektoniskt uttryck); mittposten "kan bara
ersättas" -> "kan ersättas om ... spanjolettbeslag" (RAÄ:s ordlista); mittpostrådet anges som kommunens råd för nya
byggnader. Järfälla – "Skadorna" -> "Rötskadorna" (bladet talar om rötskador i bottenstyckena); FAQ om uttorkning
tillskriven RAÄ. Kungsholmen – "de flesta bor i bostadsrätt" -> de flesta bostäder är bostadsrätter (30 598 av
44 554); "inte alltid" struket. Sollentuna – vädringsventilen 1937 kopplad till tätning OCH sänkt rumshöjd (RAÄ).
Solna – "ny kulör mot gatan kräver lov" mildrat till stadens lydelse (lov för fasadändring mot allmän plats; byte av
färg är stadens exempel) i rubrik, text och FAQ. Södermalm – konditionsbesiktning "en viktig förutsättning" (RAÄ:s
ord, inte "lösningen"); "de mest utsatta delarna tar skada först" skrivet som vad exemplet visade; "malmarnas
småhus" -> Södermalms småhus (områdesfakta anger inte var de 211 ligger).
Kritikpass 2 (extern) 2026-10-26: alla 27 källor öppnade med curl (200, pdf:er med textlager via pdftotext).
Södermalm – klassernas definitioner (blått högst, grönt särskilt värdefullt, gult positiv betydelse) stod inte i
de listade källorna: struket, kartan beskrivs bara med blått/grönt/gult/grått; FAQ om gul klass omskriven till
översiktsplanens "relativt låg klassificering" + stadens regel om gult/grått utan annat skydd; ROT för småhus
villkorat "Äger du" (områdesfakta: av 211 småhus är 13 äganderätter, resten hyres-/bostadsrätter); "de flesta
fönster ... förening eller fastighetsägare beslutar" -> bostadssiffrorna; lead utan påståendet att frågan
"kommer tidigt". Solna – "nya fönster" som stadens exempel på fasadändring fanns inte på sidan (bara "byte av
fasadfärg"): rättat i text och FAQ; "helhetsintryck som staden vill bevara" om fönsterindelning (egen slutsats)
struket. Sollentuna – lead "varmare att sitta vid" -> släpper ut mindre värme (Boverket: energiförluster);
FAQ om modellera och om måla före list skrivna efter RAÄ:s ordalydelse; kondens-FAQ gäller bättre isolerade
fönster, inte "efter tätning". Järfälla – vita omfattningar gäller Bonäs villor, inte Stäkets; "därför räcker
det sällan att bara byta" (RAÄ). Haninge – "ofta lika gamla" uthus struket; "högst 30 procent". Solna och
Haninge – beloppsmeningen grammatiskt jämnad ("som mest 50 000 kr").
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'

# ------------------------------------------------------------------ gemensamma källor
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_RAA_F = ("Riksantikvarieämbetet – Fönster: historik och råd vid renovering (RAÄ 1988:1, pdf)",
          "https://www.raa.se/publicerat/9789172095892.pdf")
_LST_F = ("Länsstyrelserna i Gävleborgs, Västmanlands och Örebro län – Information om byggnadsvård: Fönster (pdf)",
          "https://catalog.lansstyrelsen.se/store/23/resource/2000__13")
_LST_M = ("Länsstyrelserna i Gävleborgs, Västmanlands och Örebro län – Målning utomhus på trä (pdf)",
          "https://catalog.lansstyrelsen.se/store/23/resource/2000__14")
_BV_F = ("Boverket – Energiguiden: Energirenovera eller byta fönster och dörrar",
         "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/fonster_dorrar/")
_BV_ASB = ("Boverket – Risker med asbest i byggnader",
           "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_AV_ASB = ("Arbetsmiljöverket – Tillstånd för rivning eller sanering av asbest",
           "https://www.av.se/halsa-och-sakerhet/kemiska-risker/tillstand/asbest/tillstand-for-rivning-av-asbest/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 4, 12 och 13 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 8 kap. 14 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_SB_F = ("Stockholms stad – Fönster och dörrar (bygglov.stockholm)",
         "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fonster-och-dorrar/")
_SB_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov.stockholm)",
             "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_SB_KVB = ("Stockholms stad – Kulturhistorisk värdefull byggnad och område (bygglov.stockholm)",
           "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/kulturhistorisk-vardefull-byggnad-och-omrade/")
_OP_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
            "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_OF_KUNGS = ("Stockholms stad – Områdesfakta: Kungsholmens stadsdelsområde (pdf)",
             _OF + "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade.pdf")
_OF_SOD = ("Stockholms stad – Områdesfakta 2025: Södermalms stadsdelsområde (pdf)",
           _OF + "inre-staden/sodermalm/sodermalm-stadsdelsomrade.pdf")
_HAN_KAR = ("Haninge kommun – Haninges karaktärsmiljöer, kulturmiljöprogram (pdf)",
            "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf")
_JF_STA = ("Järfälla kommun – Kulturmiljöplan, Stäket (pdf)",
           "https://www.jarfalla.se/download/18.68e7a727168e12dd179a407e/1550245842779/kulturmiljoplan-staket.pdf")
_JF_FAS = ("Järfälla kommun – Fasadändring",
           "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/vadvilldubyggaellerandra/fasadandring.4.1966aa14175c8663c9323310.html")
_SOL_OP = ("Sollentuna kommun – Översiktsplan för Sollentuna med sikte på 2040 (pdf)",
           "https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/oversiktsplan/oversiktsplan-for-sollentuna-med-sikte-pa-2040.pdf")
_SOL_KUL = ("Sollentuna kommun – Kulturhistoriska byggnader och områden",
            "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/kulturmiljoer/")
_SOL_VENT = ("Sollentuna kommun – Ventilation (din bostad)",
             "https://www.sollentuna.se/bygga-bo--miljo/Din-bostad-och-tomt/ventilation/")
_SOL_VINST = ("Sollentuna kommun – Installation eller ändring av ventilation",
              "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/installation-eller-andring-av-ventilation/")
_SOLNA_KUL = ("Solna stad – Kulturmiljöer i Solna", "https://www.solna.se/bygga-bo--miljo/stadsmiljo/kulturmiljoer-i-solna")
_SOLNA_FAS = ("Solna stad – Fasadändring", "https://www.solna.se/bygga-bo--miljo/bygga/vanliga-byggatgarder/fasadandring")
_SOLNA_LGH = ("Solna stad – För lägenhetsinnehavare (guide till lov och anmälan)",
              "https://www.solna.se/bygga-bo--miljo/bygga/guide-till-lov-och-anmalan/for-lagenhetsinnehavare")
_SOLNA_VILLA = ("Solna stad – För villaägare (guide till lov och anmälan)",
                "https://www.solna.se/bygga-bo--miljo/bygga/guide-till-lov-och-anmalan/for-villaagare")

PAGES_TJ = {

# ------------------------------------------------------------------ HANINGE
"fonsterrenovering-haninge.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Haninge", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Haninge – gårdarnas gamla fönster",
  "description": "Fönsterrenovering i Haninge: boningshus och uthus på landsbygden – kommunens råd, mittposten, vattenbräda och bleck och rotavdraget på en lantbruksenhet.",
  "h1": "Fönsterrenovering i Haninge",
  "lead": "På en gård i Haninge har inte bara boningshuset fönster. Ladugård, förråd och andra uthus har sina egna, och de är lika värda att ta hand om. Geal Entreprenad AB renoverar fönster på Haninges gårdar och villor – vi lagar bågar och karmar, kittar, målar och ser över hur vattnet leds bort under fönstret.",
  "card": "Gårdens fönster, från boningshus till ladugård.",
  "sections": [
    {"id": "landsbygd-haninge", "anchor": "Landsbygden",
     "h2": "Kommunens råd: behåll de ursprungliga fönstren",
     "paras": [
       "Haninges kulturmiljöprogram, Haninges karaktärsmiljöer, har ett eget avsnitt om att värna den agrara miljön. Under rubriken renovering och underhåll skriver kommunen att befintliga byggnader ska hållas i vårdat skick och att ursprungliga karaktärsdrag och detaljer ska värnas. Fönster och dörrar beskrivs som något med starkt karaktärsbärande effekt, och vid renovering och underhåll bör de ursprungliga fönstren i möjligaste mån bevaras. Måste ett fönster ändå bytas ska ursprunglig utformning eftersträvas.",
       "Liknande råd finns för villorna. I egnahemsområdena från 1910–1940-talen, med exempel i Tungelsta, Vendelsö, Vendelsömalm, Handen, Västerhaninge och Norrby, nämner programmet träpanel och enkelt spröjsade fönster bland de tongivande dragen och råder att husens ursprungliga arkitektoniska uttryck värnas. För folkhemsbyggets småhus från 1940–1960-talen skriver kommunen att dörrar och fönster är en bärande del av byggnadens karaktär och att deras ursprungliga utformning och färgsättning ska vara utgångspunkt vid förändring. Vid bygglov som kan påverka kulturmiljöns värden ska enligt programmet en antikvarisk sakkunnig medverka.",
     ],
     "aside": {"title": "Programmets råd om fönster", "items": [
       "Bevara ursprungliga fönster", "Vid byte: ursprunglig utformning", "Mittposten är en viktig del",
       "Antikvarisk sakkunnig vid bygglov som påverkar värdena"]}},
    {"id": "uthus-haninge", "h2": "Ladugårdens och uthusens fönster",
     "paras": [
       "Programmet beskriver hur landsbygdens byggnadstradition rymmer flera komplementbyggnader för olika funktioner, som i regel står fristående från bostadshuset. Om ladugårdarna skriver kommunen att en ny typ började byggas på landsbygden mellan 1890 och 1940. De var rationellt byggda med målade fasader, tegeltak och spröjsade fönster, och fasadens detaljer skiftade med tiden från schweizerstil till nationalromantik. Vi ger därför uthusens fönster samma omsorg som boningshusets, även när rotavdraget inte följer med.",
       "Mittposten fyller både en estetisk och en praktisk roll. För nya byggnader råder kommunen att ta efter den äldre traditionen, med symmetriskt placerade fönster i kvadratiskt eller stående format, och betonar att mittposten är en viktig del av fönstrets uttryck. Riksantikvarieämbetet förklarar varför: mittposten behövs i klenare fönsterkonstruktioner som stängs med fönsterhakar, men kan ersättas om fönstret stängs med spanjolettbeslag. Vid en renovering behåller vi därför mittposten och lagar hakar och gångjärn i stället för att bygga om bågarna.",
     ],
     "aside": None},
    {"id": "vatten-haninge", "h2": "Vattenbräda, bleck och färg i rätt tid",
     "paras": [
       "Nedtill behöver ett fönster någon form av vattenavledning som skyddar fasaden. Riksantikvarieämbetet skriver att det på trähus förr var vanligt att helt enkelt sätta en snedställd bräda som vattenavvisare, medan de större stenhusen tidigt fick bleck av järnplåt. På ett gammalt gårdshus i trä kan det alltså vara mer rätt att laga eller göra om brädan än att sätta dit ett nytt plåtbleck.",
       "Länsstyrelsernas informationsblad om målning utomhus på trä påminner om att fönster och dörrar behöver målas om oftare än fasader, och söderfasader oftare än de andra. Bladet avråder från blästring och maskinslipning, som skadar träet, och från högtryckstvätt, som pressar in vatten i väggen. Plastfärg förenas inte med underlaget utan bildar en hinna som måste bort innan linoljefärg kan användas. Om kulörerna skriver bladet att färgskalan blev dovare under 1800-talets andra hälft och att fönstren då ofta målades i rött, brunt eller grönt.",
       "Om du hellre vill ha nya fönster i gårdens hus, läs om " + _L.format("fonsterbyte-haninge.html", "fönsterbyte i Haninge") + ". Kulörer för fasad och snickerier tar vi upp under " + _L.format("malare-haninge.html", "målare i Haninge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönstren på en gård i Haninge",
  "steps": [
    ("Rundvandring på gården", "Vi går igenom fönstren i boningshuset och i uthusen och noterar skicket på vart och ett."),
    ("Hus för hus", "Bostadshus och ekonomibyggnader hålls isär, så att det syns vad som kan ge rotavdrag."),
    ("Skriftligt kostnadsförslag", "Lagning, kittning och målning anges för varje byggnad."),
    ("Bågar och karmar", "Ruttet virke skarvas, och mittpost, hakar och gångjärn behålls och lagas."),
    ("Vattenavledning", "Brädan eller blecket under fönstret ses över och görs om vid behov."),
    ("Linoljefärg", "Bågar och karmar målas i tunna lager, gärna i husets ursprungliga kulör."),
  ],
  "rot_h2": "ROT-avdrag för fönsterarbetet i Haninge",
  "rot": [
    "Skatteverket räknar att reparera eller byta ut fönster och att måla fönster som rotarbete i ett småhus, och komplementhus som garage och förråd räknas som en del av bostaden. Ligger ditt hus på en lantbruksenhet gäller en snävare regel: avdrag ges bara för arbete i bostadsbyggnaden och på tomten runt den, inte för arbete på ekonomibyggnader eller utanför tomten.",
    "Avdraget är högst 30 procent av arbetskostnaden, som mest 50 000 kr per person och år och högst 75 000 kr ihop med rutavdrag. Det är bara arbetad tid på plats hos dig som räknas, inte material eller resor. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Haninge?",
  "price": [
    "Antalet fönster i boningshus och uthus, hur mycket virke som behöver lagas, om plastfärg ska bort och om bräda eller bleck ska göras om väger tyngst. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag där bostadshus och ekonomibyggnader står var för sig.",
  ],
  "faq": [
    ("Ger fönsterrenovering på en ladugård rotavdrag?",
     "Inte om gården är en lantbruksenhet. Skatteverket ger då avdrag bara för arbete i bostadsbyggnaden och på tomten runt den, inte för ekonomibyggnader."),
    ("Vad säger Haninge kommun om gamla fönster på landsbygden?",
     "Kulturmiljöprogrammet råder att de ursprungliga fönstren i möjligaste mån bevaras vid renovering och underhåll, och att ursprunglig utformning eftersträvas om ett fönster måste bytas."),
    ("Varför ska mittposten i ett gammalt fönster sitta kvar?",
     "Kommunen kallar den en viktig del av fönstrets uttryck, och Riksantikvarieämbetet förklarar att klenare fönster som stängs med hakar behöver den."),
    ("Kan man högtryckstvätta gamla fönster innan de målas om?",
     "Länsstyrelsernas blad om utomhusmålning avråder, eftersom högtryckstvätt pressar in vatten i väggen. Blästring och maskinslipning skadar träet."),
    ("Vilken färg hade fönstren på gårdarna förr?",
     "Enligt Länsstyrelsernas blad blev färgskalan dovare under 1800-talets andra hälft, och fönstren målades då ofta i rött, brunt eller grönt."),
  ],
  "sources": [_HAN_KAR, _RAA_F, _LST_M, _SKV, _SKV2],
  "cta": ("Har gården kvar sina gamla fönster?", "Boka ett gratis platsbesök, så går vi igenom fönstren i hus och uthus och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Rödmålad ladugård med små spröjsade fönster och tegeltak i ett öppet odlingslandskap",
     "old Swedish red-painted barn from around 1900 in an open farming landscape south of Stockholm, row of small white multi-pane wooden windows with glazing bars, clay tile roof, stone foundation, freshly painted window frames, late summer afternoon, realistic photo, no people, no text, no letters"),
    ("Tvåluftsfönster med mittpost, fönsterhakar och snedställd vattenbräda på ett gårdshus",
     "close-up of a two-pane wooden casement window with a central mullion and iron window hooks on an old ochre wooden farmhouse, slanted wooden drip board below the window, dark green linseed oil paint on the sashes, realistic photo, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"fonsterrenovering-jarfalla.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Järfälla", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Järfälla – bottenstycke och bleck",
  "description": "Fönsterrenovering i Järfälla: fönstrets nederkant på villorna vid Stäket och Bonäs – bottenstycken, bleck, vita omfattningar och lovfrågan vid ny kulör.",
  "h1": "Fönsterrenovering i Järfälla",
  "lead": "Rötskadorna på ett gammalt fönster sitter oftast nedtill, där vattnet rinner av. Geal Entreprenad AB renoverar fönster i Järfälla och lägger särskild vikt vid bottenstyckena, blecket och omfattningen – de delar som skyddar resten av fönstret och väggen bakom.",
  "card": "Bottenstycken, bleck och vita omfattningar.",
  "sections": [
    {"id": "staket-jarfalla", "anchor": "Stäket och Bonäs",
     "h2": "Villorna vid Stäket och Bonäs",
     "paras": [
       "Järfällas kulturmiljöplan beskriver Stäkets villasamhälle, där de första villorna byggdes 1904 på branten ned mot järnvägen. Utformningen var ganska individuell och ofta med stor omsorg om detaljerna, och färgsättningen hölls enligt planen ursprungligen i rött eller ljusa oljefärger. Vid Bonäs lät bankdirektören Frans Hallberg 1907 bygga en stor villa i rödfärgad liggande panel, och både den och den gulmålade villan på Bonäsvägen 27 har fönsteromfattningar och övriga snickerier hållna i vitt.",
       "För villorna längs Gyllenstiernas väg föreslår planen skyddsbestämmelser för några av de äldsta och mest välbevarade husen och i övrigt utökad lovplikt, med krav på utformning, materialval och färgsättning i samband med renoveringar. Kommunen skriver att fasadändringar på en- och tvåbostadshus inte kräver bygglov, men att det inte gäller en byggnad eller ett område som är särskilt värdefullt, eller där detaljplanen har utökad lovplikt. Byte av färg räknas som en fasadändring, så innan bågar eller omfattningar får en ny kulör kontrollerar vi vad detaljplanen säger.",
     ],
     "aside": {"title": "Stäket i kulturmiljöplanen", "items": [
       "De första villorna 1904", "Ursprungligen rött eller ljusa oljefärger", "Vita omfattningar vid Bonäs"]}},
    {"id": "nedtill-jarfalla", "h2": "Rötan börjar i bottenstyckena",
     "paras": [
       "Länsstyrelsernas fönsterblad förklarar att vattnet som rinner på fönstrets utsida gör den nedre delen särskilt utsatt. Det är i bågens och karmens bottenstycken som rötskador oftast uppstår, och man får också se upp med röta bakom hörnjärnen. Riksantikvarieämbetet skriver att skadorna i allmänhet uppstått för att väta under lång tid har kunnat tränga in i virket, medan den utsatta delen bara har kunnat torka långsamt. Skriften pekar också på ett samband mellan rötskador och rost på skruvar och beslag.",
       "Riksantikvarieämbetet noterar att kärnfuru klarar stora påfrestningar, och det är sådant virke vi väljer till lagningarna. Är karmens bottenstycke skadat räcker det enligt Riksantikvarieämbetet i allmänhet att limma in nytt virke i karmens yttre, mest utsatta del – bara i enstaka fall måste hela bottenstycket bytas. I bågarna sitter skadorna ofta under hörnbeslagen och i fogarna, och därför räcker det sällan att bara byta det nedre bågträet. Rostiga beslag behöver inte kasseras: enligt fönsterbladet kan de oftast renoveras, och kopior av gamla modeller finns att köpa. Bladet påpekar också att gamla fönster är tillverkade av mycket bra virke, att det därför lönar sig att underhålla dem och att även svårt skadade fönster kan repareras med gott resultat.",
     ],
     "aside": {"title": "Det vi kontrollerar nedtill", "items": [
       "Bågens bottenstycke", "Karmens bottenstycke", "Virket bakom hörnjärnen", "Blecket mot karmen"]}},
    {"id": "bleck-jarfalla", "h2": "Blecket och omfattningen skyddar väggen",
     "paras": [
       "Riksantikvarieämbetet beskriver fönsterblecket som en plåt som avleder vatten som annars kan skada karm och vägg. Blecket sitter fäst i karmens nederkant. Under 1800-talet fick det en bockad inslagskant, som först drevs in i karmen och sedan lades i ett spår som fanns färdigt i karmbottenstycket. Fönster i fasadliv har ibland också ett övre bleck. Vi ser därför lika noga på hur blecket ansluter till karmen som på själva plåten.",
       "Fodret, eller omfattningen, är listerna som ramar in fönsteröppningen utvändigt och invändigt. På villorna vid Bonäs är de vita omfattningarna en del av husens uttryck, och vi lagar dem med samma profil i stället för att byta till enklare lister. Behöver panelen runt fönstret lagas, se " + _L.format("snickare-jarfalla.html", "snickare i Järfälla") + ". Är fönstret för långt gånget beskriver vi alternativen under " + _L.format("fonsterbyte-jarfalla.html", "fönsterbyte i Järfälla") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönstren på en villa i Järfälla",
  "steps": [
    ("Kontroll nedtill", "Vi känner efter röta i bottenstyckena och bakom hörnjärnen och ser hur blecket ansluter."),
    ("Detaljplanen", "Ska kulören ändras tar vi först reda på om huset omfattas av utökad lovplikt."),
    ("Skriftligt kostnadsförslag", "Lagning av båge, karm, bleck och omfattning redovisas var för sig."),
    ("Lagning", "Nytt virke limmas in där det gamla är skadat, och rostiga beslag rostskyddas."),
    ("Bleck och foder", "Blecket läggs om mot karmen och omfattningen lagas med samma profil."),
    ("Målning", "Grundning, kittning och linoljefärg i tunna lager med torktid emellan."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Järfälla",
  "rot": [
    "För småhus finns att reparera eller byta ut fönster, att måla fönster och att byta och reparera fönsterbleck på Skatteverkets lista över rotarbeten. I ett radhus som är en bostadsrätt ger fönsterbleck och fönstrens utsida däremot inget avdrag; där godkänns bara arbete på insidan av befintliga fönster, som tätningslist eller nytt glas i innerbågen.",
    "Avdraget är högst 30 procent av arbetskostnaden och som mest 50 000 kr per person och år, eller 75 000 kr inklusive rutavdrag. Det gäller arbetskostnaden, inte material eller resor, och vi drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Järfälla?",
  "price": [
    "Hur många bottenstycken som måste lagas, om blecket ska göras om, hur mycket av omfattningarna som är skadat och hur mycket gammal färg som ska bort styr priset mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför ruttnar fönstrets nederkant först?",
     "Vattnet som rinner på fönstrets utsida gör den nedre delen särskilt utsatt, enligt Länsstyrelsernas fönsterblad. Där torkar virket dessutom långsamt, enligt Riksantikvarieämbetet."),
    ("Måste hela karmbottenstycket bytas när det är ruttet?",
     "Sällan. Riksantikvarieämbetet skriver att det i allmänhet räcker att limma in nytt virke i karmens yttre, mest utsatta del."),
    ("Får man rotavdrag för nya bleck under fönstren i Järfälla?",
     "I ett småhus ja, enligt Skatteverkets lista över rotarbeten. I en bostadsrätt ger fönsterbleck inget avdrag."),
    ("Behövs bygglov för att måla om fönsteromfattningarna vid Stäket?",
     "Fasadändring på en- och tvåbostadshus kräver normalt inte lov i Järfälla, men undantag gäller särskilt värdefulla byggnader och områden och detaljplaner med utökad lovplikt."),
    ("Kan rostiga fönsterbeslag renoveras?",
     "Oftast. Länsstyrelsernas fönsterblad skriver att beslagen i regel går att renovera även om de är rostiga, och att kopior av gamla modeller finns att köpa."),
  ],
  "sources": [_JF_STA, _JF_FAS, _LST_F, _RAA_F, _SKV, _SKV2],
  "cta": ("Har fönstren börjat ruttna nedtill?", "Boka ett gratis platsbesök, så kontrollerar vi bottenstycken, bleck och omfattningar och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa från tidigt 1900-tal med rödfärgad panel, vita fönsteromfattningar och nymålade fönster",
     "early 1900s Swedish wooden villa on a sloping natural lot near a lake north-west of Stockholm, horizontal red painted panel, white window surrounds and trim, freshly repainted white two-pane windows, steep clay tile roof, pine trees, summer daylight, realistic photo, no people, no text, no letters"),
    ("Karmbottenstycke med inlimmat nytt virke och nytt fönsterbleck",
     "close-up of an old wooden window frame bottom being repaired, a piece of new pine glued into the weathered outer part of the frame sill, new painted sheet-metal window flashing fitted into a groove, clamps and putty knife nearby, realistic photo, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ KUNGSHOLMEN
"fonsterrenovering-kungsholmen.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Kungsholmen", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering på Kungsholmen – fönstret i bostadsrätten",
  "description": "Fönsterrenovering på Kungsholmen: vad stadgarna lägger på dig och vad föreningen sköter, kopplade bågar som kärvar och rotavdraget för insidan.",
  "h1": "Fönsterrenovering på Kungsholmen",
  "lead": "På Kungsholmen är de flesta bostäder bostadsrätter, och då är fönstren sällan bara en teknisk fråga – det gäller också vem som ansvarar för vilken del. Geal Entreprenad AB renoverar fönster i lägenheter på Kungsholmen: vi justerar bågar som kärvar, byter lister och glas i innerbågen och målar insidan, och vi går igenom gränsen mot föreningen innan arbetet börjar.",
  "card": "Fönstret i bostadsrätten, insida och beslag.",
  "sections": [
    {"id": "bostadsratt-kungsholmen", "anchor": "Bostadsrätten",
     "h2": "Ett fönster, två ansvarsområden",
     "paras": [
       "Enligt stadens områdesfakta fanns det 44 554 bostäder i Kungsholmens stadsdelsområde 2024, och 30 598 av dem var bostadsrätter. Bara 337 låg i småhus. Bebyggelsen spänner från den klassiska stenstaden, som översiktsplanen daterar till 1870–1930 och som bland annat breder ut sig över Kungsholmen, till de funktionalistiska stadsdelarna i Fredhäll och Kristineberg som började byggas omkring 1930.",
       "Bostadsrättslagen säger att du som bostadsrättshavare på egen bekostnad ska hålla lägenheten i gott skick, om inte stadgarna bestämmer något annat. Föreningen ska hålla lägenheten, huset och marken i gott skick i den mån ansvaret inte vilar på dig. Fönstren nämns inte särskilt i lagen, så det är föreningens stadgar som drar gränsen, och den kan dras olika i olika föreningar. Läs därför stadgarna, och fråga gärna styrelsen, innan du beställer arbete på fönstren.",
     ],
     "aside": {"title": "Kungsholmen 2024", "items": [
       "44 554 bostäder", "30 598 bostadsrätter", "337 bostäder i småhus"]}},
    {"id": "insidan-kungsholmen", "h2": "Det du kan beställa själv – och vad avdraget täcker",
     "paras": [
       "Skatteverkets regler för bostadsrätt följer samma gräns. Avdrag ges bara för arbete inne i bostaden, innanför tak, väggar och golv, och för åtgärder som du ansvarar för enligt stadgarna. För fönster godkänns arbete på insidan av befintliga fönster, till exempel att byta glaset i den inre bågen eller montera tätningslist. Att måla insidan av fönstren och att byta och reparera innerfönster och fönsterfoder finns också med.",
       "Lika tydligt är vad som inte ger avdrag: att byta fönster eller gångjärn i fönster, att arbeta mellan bågarna eller på utsidan och att måla eller olja fönstrens utsida. Renoverar föreningen husets fönster har dess företrädare enligt bostadsrättslagen rätt att komma in i lägenheten när det behövs för arbete som föreningen svarar för, och föreningen ska se till att du inte drabbas av större olägenhet än nödvändigt.",
     ],
     "aside": {"title": "Rotavdrag i bostadsrätt", "items": [
       "Glas i innerbågen: ja", "Tätningslist på insidan: ja", "Måla insidan: ja",
       "Utsidan och mellan bågarna: nej", "Byta gångjärn: nej"]}},
    {"id": "funkis-kungsholmen", "h2": "1930-talets kopplade bågar som kärvar",
     "paras": [
       "Riksantikvarieämbetets skrift om fönster beskriver ett fönster från 1937 i ett smalhus i Uppsala, i ett område där alla hus byggdes på 1930-talet. Fönstret är kopplat och inåtgående, nästan kvadratiskt och saknar mittpost, och innerbågen är överfalsad med plats för en tätningslist. När fönstren i huset sågs över hade inget av dem rötskador, men många var svåra att öppna och stänga. Snickeriarbetet bestod i att justera upphängningsbeslagen och hyvla bågarna där de klämde, och alla tätningslister byttes mot gummilister.",
       "Samma skrift påpekar att äldre kopplade bågar kan vara stora och tunga, sluta otätt och ha igengrodda kopplingsbeslag eller skevheter. Ibland behöver de nya handtag och stängningsbeslag för att bli lätta att hantera. Vi börjar därför med upphängningen: först när bågen hänger rätt är det meningsfullt att byta list.",
     ],
     "aside": None},
    {"id": "styrelsen-kungsholmen", "h2": "Innan arbetet: stadgarna, styrelsen och fasaden",
     "paras": [
       "Stockholms stad räknar bland annat nytt material eller ny kulör, ändrade profiler på karmar, bågar och spröjsar och en annan indelning eller upphängning som ändringar av fönster, och om en sådan ändring kräver bygglov beror på byggnaden. Staden uppmanar också den som planerar ett arbete att informera grannarna eller styrelsen. Att justera, täta och måla innerbågen i samma kulör finns inte med i stadens lista.",
       "Vill du förbättra fönstret mer än en ny list ger, beskriver Boverkets energiguide hur den inre rutan kan bytas eller kompletteras med energiglas, till exempel med en tvåglaskassett på insidan. Glas i den inre bågen är ett av de arbeten som Skatteverket godkänner i en bostadsrätt. Hur insidan av fönster och element målas i en bostadsrätt tar vi upp under " + _L.format("malare-kungsholmen.html", "målare på Kungsholmen") + ", och nya fönster under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönstren i en lägenhet på Kungsholmen",
  "steps": [
    ("Stadgarna först", "Vi går igenom vilka delar av fönstret stadgarna lägger på dig och vilka som är föreningens."),
    ("Besök i lägenheten", "Varje fönster öppnas och stängs, och vi ser hur bågarna hänger, sluter och var de klämmer."),
    ("Skriftligt kostnadsförslag", "Arbetet delas upp så att det syns vad som görs på insidan."),
    ("Justering", "Beslagen ställs in och bågar som klämmer hyvlas så att de går lätt."),
    ("List och glas", "Ny tätningslist på innerbågen och vid behov nytt glas i den inre bågen."),
    ("Målning på insidan", "Innerbågar och foder målas, och golv och möbler skyddas under tiden."),
  ],
  "rot_h2": "ROT-avdrag för fönsterarbete på Kungsholmen",
  "rot": [
    "I en bostadsrätt ger fönsterarbete avdrag när det görs på insidan och gäller något du ansvarar för enligt stadgarna. Företaget behöver då bostadsrättsföreningens organisationsnummer och lägenhetsnumret, som vanligen har fyra siffror.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kr per person och år, eller 75 000 kr tillsammans med rutavdrag. Material och resor ingår inte, betalningen ska vara elektronisk och vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Kungsholmen?",
  "price": [
    "Antalet fönster, hur mycket justering och hyvling bågarna behöver, om glaset i innerbågen ska bytas och hur mycket som ska målas på insidan påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vem ansvarar för fönstren i en bostadsrätt på Kungsholmen?",
     "Det avgör föreningens stadgar. Bostadsrättslagen säger att du ska hålla lägenheten i gott skick om inte stadgarna bestämmer annat, och att föreningen ansvarar för resten."),
    ("Ger byte av gångjärn i fönstret rotavdrag i en bostadsrätt?",
     "Nej. Skatteverket listar byte av fönster och gångjärn i fönster bland arbeten som inte ger avdrag i en bostadsrätt. Tätningslist och nytt glas i den inre bågen ger däremot avdrag."),
    ("Varför är de kopplade fönstren i lägenheten så svåra att stänga?",
     "Kopplade bågar kan vara tunga, skeva eller ha igengrodda kopplingsbeslag. I Riksantikvarieämbetets exempel från 1937 räckte det att justera beslagen och hyvla där bågarna klämde."),
    ("Får föreningen gå in i min lägenhet när fönstren renoveras?",
     "Ja, bostadsrättslagen ger föreningens företrädare rätt att komma in när det behövs för arbete som föreningen svarar för. Föreningen ska samtidigt se till att du inte drabbas av större olägenhet än nödvändigt."),
    ("Vilka uppgifter behövs för rotavdrag i en bostadsrätt?",
     "Utöver dina egna uppgifter behöver företaget bostadsrättsföreningens organisationsnummer och lägenhetsnumret, som vanligen har fyra siffror, enligt Skatteverket."),
  ],
  "sources": [_OF_KUNGS, _OP_RIKS, _BRL, _SKV, _SKV2, _RAA_F, _SB_F, _BV_F],
  "cta": ("Kärvar fönstren i lägenheten?", "Boka ett gratis platsbesök, så går vi igenom bågar, lister och stadgarna och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Inåtgående kopplat tvåluftsfönster med nymålade innerbågar i en ljus lägenhet",
     "interior of a 1930s Stockholm functionalist apartment, square two-pane inward-opening coupled wooden window without mullion, freshly painted white inner sashes, slim brass espagnolette handle, empty deep window sill, view of trees and a light rendered facade opposite, soft daylight, realistic photo, no people, no text, no letters"),
    ("Öppen innerbåge med ny gummilist och skruvmejsel vid justering av beslagen",
     "close-up of an open inward-opening wooden window sash in an apartment, new black rubber weatherstrip fitted in the rebate, a screwdriver lying flat on the window sill next to an adjusted brass hinge, white painted wood, no hands, natural light, realistic photo, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SOLLENTUNA
"fonsterrenovering-sollentuna.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Sollentuna", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Sollentuna – täta utan att kväva huset",
  "description": "Fönsterrenovering i Sollentuna: täta gamla fönster i villastaden utan att strypa tilluften – lister, justering, kondens och anmälan av ventilation.",
  "h1": "Fönsterrenovering i Sollentuna",
  "lead": "Ett gammalt fönster som tätas släpper ut mindre värme, men i ett äldre hus kan otätheterna ha varit en del av ventilationen. Geal Entreprenad AB renoverar och tätar fönster i Sollentunas villor och radhus och ser till att luften fortfarande har en väg in.",
  "card": "Täta gamla fönster med ventilationen i åtanke.",
  "sections": [
    {"id": "villastaden-sollentuna", "anchor": "Villastaden",
     "h2": "Villastaden från 1900-talets första hälft",
     "paras": [
       "Kommunens översiktsplan berättar att järnvägen mellan Stockholm och Uppsala byggdes 1866 och att Rotebro först var den enda stationen i Sollentuna. I början av 1900-talet tillkom stationer i Tureberg och Norrviken, och då började man också bygga småhus och villor. Planen vill att Sollentuna bevarar den prägel av villastad som växte fram under 1900-talets första hälft, och i Norrvikens villastad, Väderholmen och Skansen ska avstyckningar och förtätningar inte tillåtas där kulturmiljöplanen anger att karaktären är viktig att behålla.",
       "Översiktsplanen skriver också att kommunen i regel inte bör medge förtätningar som förutsätter att funktionella bostadshus rivs, med hänvisning till resurshushållning och minskad klimatpåverkan. Vi ser på fönstren på samma sätt: det som fungerar tas om hand. Kommunens sida om kulturhistoriska byggnader påminner om att de bygglovsbefriade åtgärderna inte kan användas för särskilt värdefulla byggnader och områden, och att ett hus kan vara värdefullt även om det inte finns med i kulturmiljöplanen.",
     ],
     "aside": {"title": "Villastaden i översiktsplanen", "items": [
       "Järnvägen 1866", "Tureberg och Norrviken i början av 1900-talet",
       "Norrvikens villastad, Väderholmen och Skansen"]}},
    {"id": "tatning-sollentuna", "h2": "Täta – men måla och justera först",
     "paras": [
       "Boverkets energiguide kallar tätning det enklaste sättet att förbättra ett fönster: se över isoleringen runt karmen, drevningen och listerna mellan båge och karm, och renovera bågen eller karmen. Om fönster och dörrar inte är lufttäta ökar energiförlusterna markant, och listerna bör ses över regelbundet.",
       "Riksantikvarieämbetet ger några praktiska regler. Fönstret ska målas och justeras innan listerna sätts upp, och springans bredd kan mätas genom att fästa små klumpar modellera där listen ska sitta. En för tjock list gör fönstret svårstängt och ger spänningar som kan skada båge och glas. Listerna görs främst av gummi och finns i ett par profiltyper för olika springbredder, och det är innerbågen som ska få listen. Äldre kopplade bågar kan vara tunga och sluta dåligt, och ibland behöver de nya handtag och stängningsbeslag.",
     ],
     "aside": {"title": "Före listen", "items": [
       "Måla bågen", "Justera gångjärn och beslag", "Mät springan", "Välj rätt profil"]}},
    {"id": "ventilation-sollentuna", "h2": "När otätheten var husets tilluft",
     "paras": [
       "Boverket varnar för att ett äldre ventilationssystem kan vara inställt efter att luft rör sig genom och kring otäta fönster, och att den luften kan vara en betydande del av tilluften. Den som tätar sina fönster behöver därför också kontrollera behovet av tilluft, så att ventilationen och luftkvaliteten inte blir för dåliga. Guiden påminner även om att bättre isolerade fönster ger kallare rutor på utsidan och därmed större risk för kondens utvändigt.",
       "Sollentuna kommun beskriver tecken på dålig ventilation, till exempel lukt som kommer in genom frånluftsventilerna eller ventiler som inte orkar suga tag i en pappersbit. Som villaägare uppmanas du att kontakta ett konsultföretag för råd. Ska ventilation installeras, eller ett befintligt system ändras mer, till exempel med nytt aggregat, fläkt eller nya kanaler, krävs enligt kommunen anmälan och startbesked. I ett av Riksantikvarieämbetets exempel, ett fönster från 1937, ledde den bättre tätningen tillsammans med en lägre rumshöjd till ökade krav på reglerbar ventilation, och fönstret fick en vädringsventil i bröstningen under karmbottenstycket.",
       "Om badrummets ventilation, se " + _L.format("badrumsrenovering-sollentuna.html", "badrumsrenovering i Sollentuna") + ". Är det trafikbuller du vill få bort, läs om " + _L.format("fonsterbyte-sollentuna.html", "fönsterbyte i Sollentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så tätar och renoverar vi fönstren i Sollentuna",
  "steps": [
    ("Genomgång", "Vi öppnar varje fönster, ser hur bågarna sluter och var det drar."),
    ("Ventilationen", "Vi noterar hur huset ventileras och var tilluften kommer in i dag."),
    ("Skriftligt kostnadsförslag", "Målning, justering och tätning anges för varje fönster."),
    ("Målning och justering", "Bågarna målas och gångjärn och beslag ställs in före tätningen."),
    ("Lister", "Profilen väljs efter springans bredd och listen sätts på innerbågen."),
    ("Kontroll", "Vi stänger varje fönster och ser att det går lätt och sluter."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenoveringen i Sollentuna",
  "rot": [
    "Att reparera och måla fönster i ett småhus räknas som rotarbete, och avdraget gäller även ett fritidshus som du äger. I ett radhus som är en bostadsrätt godkänns bara arbete på insidan av befintliga fönster, som att montera tätningslist eller byta glaset i den inre bågen.",
    "Avdraget motsvarar högst 30 procent av arbetskostnaden, med taket 50 000 kr per person och år och 75 000 kr tillsammans med rutavdrag. Två ägare kan dela på avdraget, men sammanlagt blir det högst 30 procent. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Sollentuna?",
  "price": [
    "Antalet bågar, hur mycket målning och justering som behövs innan listerna sätts, om beslag måste kompletteras och om innerbågen ska få energiglas påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan tätade fönster ge sämre luft i en äldre villa?",
     "Ja, om ventilationen är inställd efter att luft kommer in genom otäta fönster. Boverket råder dig att då också kontrollera behovet av tilluft."),
    ("Varför ska fönstret målas innan tätningslisten sätts?",
     "Riksantikvarieämbetet kallar det en självklar regel att fönstret målas och justeras innan listerna sätts upp. En för tjock list gör enligt skriften fönstret svårstängt."),
    ("Hur mäter man vilken tätningslist ett gammalt fönster behöver?",
     "Enligt Riksantikvarieämbetet kan springans bredd mätas genom att fästa små klumpar modellera där listen ska sitta."),
    ("Varför kan det bli imma på utsidan av ett bättre isolerat fönster?",
     "Bättre isolerade fönster gör att rutorna blir kallare på utsidan. Boverket påpekar att risken för kondens utvändigt då ökar."),
    ("Behöver jag göra en anmälan till Sollentuna kommun om jag ändrar ventilationen?",
     "Enligt kommunen krävs anmälan och startbesked för att installera ventilation och för större ändringar av ett befintligt system, till exempel nytt aggregat, fläkt eller nya kanaler."),
  ],
  "sources": [_SOL_OP, _SOL_KUL, _SOL_VENT, _SOL_VINST, _BV_F, _RAA_F, _SKV, _SKV2],
  "cta": ("Drar det från fönstren?", "Boka ett gratis platsbesök, så går vi igenom bågar, lister och ventilation och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Äldre villa i trä med nymålade spröjsade fönster i en lummig trädgård",
     "1920s Swedish wooden villa in a leafy garden suburb north of Stockholm, light grey painted panel facade, white multi-pane coupled windows freshly painted, tall birch and oak trees, picket fence, early autumn daylight, realistic photo, no people, no text, no letters"),
    ("Innerbåge med ny gummilist och små klumpar modellera för att mäta springan",
     "close-up of an old wooden inner window sash on a table, new grey rubber weatherstrip partly fitted in the rebate, small lumps of modelling clay pressed on the frame edge, utility knife and folding rule beside it, soft daylight, realistic photo, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SOLNA
"fonsterrenovering-solna.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Solna", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Solna – 1950-talets fönster",
  "description": "Fönsterrenovering i Solna: hus från 1950-talet i Råsunda, Skytteholm och Huvudsta – kitt och fogar, kopplade bågar och lov för ny kulör.",
  "h1": "Fönsterrenovering i Solna",
  "lead": "Solna stad pekar ut fyra miljöer med 1950-talsbebyggelse bland stadens sammanhängande kulturhistoriskt värdefulla miljöer. Geal Entreprenad AB renoverar fönster i Solna, och i hus från de åren börjar vi med kittet och fogarna innan något skrapas bort.",
  "card": "Fönster från 1950-talet, kitt och fogar.",
  "sections": [
    {"id": "femtiotal-solna", "anchor": "1950-talet",
     "h2": "Fyra 1950-talsmiljöer i stadens lista",
     "paras": [
       "På stadens sida om kulturmiljöer finns en lista över sammanhängande kulturhistoriskt värdefulla miljöer, där helheten bedöms som viktig. Det rör sig ofta om enhetliga miljöer som är goda representanter för sin tid, och det är helhetsintrycket som räknas. Fyra av miljöerna är 1950-talsbebyggelse: i Råsunda, vid Förvaltarvägen med kv Fjorden, kv Nordan och Stinsbostaden vid Solna station, i Skytteholm och i Huvudsta. På listan finns också äldre miljöer som Råsunda villastad, stenstaden i Råsunda, Gamla Hagalund och Råsta egnahem.",
       "Staden skriver att det är mycket viktigt att ta hänsyn till husens ursprungliga karaktär när de anpassas till nya behov, så att deras historiska värde inte går förlorat. Därför renoverar vi fönstren med samma indelning och kulör som förut.",
     ],
     "aside": {"title": "1950-talsmiljöer i listan", "items": [
       "Råsunda", "Förvaltarvägen, kv Fjorden och kv Nordan", "Skytteholm", "Huvudsta"]}},
    {"id": "kitt-solna", "h2": "Kitt och fogar från asbestens årtionden",
     "paras": [
       "Boverket skriver att asbest förbjöds inom byggsektorn 1982 men att stora mängder finns kvar, och att det främst är byggnader uppförda mellan 1940 och 1970 som innehåller asbest. Är huset byggt 1940–1980 är det enligt Boverket sannolikt att det finns asbest någonstans i byggnaden. Fönsterkitt, fogmassor och tätmassor finns med på verkets lista över material där asbest kan förekomma, och i regel krävs att ett prov analyseras i mikroskop för att veta. Boverkets energiguide råder dig också att undersöka om gamla fogmassor innehåller till exempel PCB eller asbest, som är saneringspliktigt.",
       "Därför tar vi prov på kitt och fogar i hus från de här årtiondena innan något skrapas eller värms bort. Arbetsmiljöverket kräver tillstånd för att ett företag ska få riva eller sanera material som innehåller asbest, och förarbete på platsen, omhändertagande av avfallet och städning efteråt räknas också som sanering. Visar provet asbest anlitar vi ett företag med sådant tillstånd för just den delen.",
     ],
     "aside": None},
    {"id": "bagar-solna", "h2": "Kopplade bågar och linoljefärg",
     "paras": [
       "Under första hälften av 1900-talet infördes enligt Länsstyrelsernas fönsterblad det kopplade fönstret med två utåtgående bågar. Riksantikvarieämbetet påpekar att linoljefärg ännu på 1950-talet var den färg som förespråkades för utvändig snickerimålning, och att grundning och två strykningar var det minsta som borde utföras enligt Hantverkets bok från 1953.",
       "Skriften beskriver också de krav som före 1950-talet ställdes på fönstervirke – avverkat under vinterhalvåret, lufttorkat och lagrat ett par år före användning – och att de omfattande skador som visat sig på 1960- och 1970-talens fönster delvis beror på olämpligt lösta konstruktionsdetaljer. Vid lagning är det enligt skriften viktigt att det nya virket liknar det gamla, och det är så vi väljer det.",
     ],
     "aside": {"title": "Ytbehandling enligt 1950-talets råd", "items": [
       "Linoljefärg", "Grundning", "Minst två strykningar"]}},
    {"id": "lov-solna", "h2": "Ny kulör på ett flerbostadshus kan kräva lov",
     "paras": [
       "Solna stad skriver att bygglov krävs för fasadändring på en byggnad som inte är ett en- eller tvåbostadshus inom detaljplan, när ändringen görs på en fasad eller ett tak som vetter mot allmän plats. Lov krävs också för ändringar på särskilt värdefulla byggnader och i särskilt värdefulla områden. Byte av fasadfärg är ett av stadens exempel på fasadändringar. Ska bågarna i ett flerbostadshus få en ny kulör mot gatan tar vi därför upp lovfrågan med staden innan arbetet börjar.",
       "Bor du i bostadsrätt skriver staden att du behöver fastighetsägarens medgivande för byggåtgärder. För villaägare gäller utökad lovplikt i stora delar av Solna, och de vanligaste skälen är särskilt värdefulla kulturmiljöer och riksintressen. Fasadens puts och snickerier tar vi upp under " + _L.format("fasadrenovering-solna.html", "fasadrenovering i Solna") + ", och nya fönster under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönster från 1950-talet i Solna",
  "steps": [
    ("Byggår och miljö", "Vi tar reda på när huset byggdes och om det ligger i en av stadens utpekade miljöer."),
    ("Prov på kitt och fogar", "I hus från 1940–1980 tas prov innan något tas bort."),
    ("Skriftligt kostnadsförslag", "Lagning, eventuell sanering, kittning och målning redovisas var för sig."),
    ("Medgivande och lov", "Föreningens medgivande och eventuellt lov klaras av innan arbetet börjar."),
    ("Snickeri", "Skadat virke byts mot virke som liknar det gamla."),
    ("Linoljefärg", "Grundning och minst två strykningar på utsidan."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Solna",
  "rot": [
    "I en villa eller ett radhus som du äger räknar Skatteverket reparation och målning av fönster som rotarbete, och sanering av asbest ger avdrag när den görs i samband med byggarbete. Själva provet ger inget avdrag, eftersom Skatteverket inte godkänner att mäta asbest. I en bostadsrätt ger bara arbete på insidan avdrag, till exempel att måla insidan av fönstren eller byta glaset i innerbågen.",
    "Avdraget är högst 30 procent av arbetskostnaden, som mest 50 000 kr per person och år och 75 000 kr inklusive rutavdrag. Vi drar det direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Solna?",
  "price": [
    "Antalet fönster, om prov och sanering av kitt eller fogar behövs, hur mycket virke som ska bytas och om en ny kulör kräver lov påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka 1950-talsmiljöer i Solna räknas som kulturhistoriskt värdefulla?",
     "Stadens lista tar upp 1950-talsbebyggelsen i Råsunda, vid Förvaltarvägen med kv Fjorden, kv Nordan och Stinsbostaden, i Skytteholm och i Huvudsta."),
    ("Krävs bygglov för att måla om fönstren i ett flerbostadshus i Solna?",
     "Det kan krävas. Solna stad skriver att fasadändring på andra byggnader än en- och tvåbostadshus inom detaljplan kräver lov när fasaden vetter mot allmän plats, och byte av fasadfärg är ett av stadens exempel på fasadändringar."),
    ("Får vilket företag som helst ta bort kitt som innehåller asbest?",
     "Nej. Arbetsmiljöverket kräver tillstånd för att ett företag ska få riva eller sanera material som innehåller asbest."),
    ("Vilken färg rekommenderades för fönster på 1950-talet?",
     "Linoljefärg. Riksantikvarieämbetet skriver att den ännu på 1950-talet förespråkades för utvändig snickerimålning, med grundning och minst två strykningar."),
    ("Ger provtagning av asbest i fönsterkitt rotavdrag?",
     "Nej. Skatteverket ger inget avdrag för att mäta asbest, men sanering i samband med byggarbete kan ge avdrag i ett småhus."),
  ],
  "sources": [_SOLNA_KUL, _SOLNA_FAS, _SOLNA_LGH, _SOLNA_VILLA, _BV_ASB, _BV_F, _AV_ASB, _LST_F, _RAA_F, _SKV, _SKV2],
  "cta": ("Bor du i ett hus från 1950-talet?", "Boka ett gratis platsbesök, så går vi igenom fönster, kitt och fogar och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Flerbostadshus från 1950-talet med rader av kopplade fönster och en grönskande gård",
     "1950s Swedish three-storey apartment building in Solna, light ochre rendered facade, rows of white coupled outward-opening wooden windows, small balconies with slim metal railings, mature trees and lawn in front, soft daylight, realistic photo, no people, no text, no letters"),
    ("Kopplad fönsterbåge på arbetsbord med ett prov av gammalt kitt i en provpåse",
     "old coupled wooden window sash from the 1950s lying on a workbench, small sample of old window putty sealed in a clear sample bag beside it, putty knife lying on the bench, empty workshop, no hands, no gloves, natural light, realistic photo, no people, no text, no letters"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SÖDERMALM
"fonsterrenovering-sodermalm.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Södermalm", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering på Södermalm – besiktiga före byte",
  "description": "Fönsterrenovering på Södermalm: föreningens fönster i stenstaden – besiktning fönster för fönster, droppnäsor och glasningslister, klassificering och lov.",
  "h1": "Fönsterrenovering på Södermalm",
  "lead": "Ska föreningens fönster bytas eller renoveras? Geal Entreprenad AB renoverar fönster i Södermalms flerbostadshus och i de få småhusen, och vi börjar med att besiktiga fönstren ett och ett innan något beslut fattas.",
  "card": "Föreningens fönster, besiktigade före beslut.",
  "sections": [
    {"id": "husen-sodermalm", "anchor": "Husen",
     "h2": "Malmarnas hus och stenstadens kvarter",
     "paras": [
       "I stadens områdesfakta för 2025 har Södermalms stadsdelsområde 77 525 bostäder. 43 680 av dem är bostadsrätter och bara 211 ligger i småhus, medan 73 952 finns i flerbostadshus och övriga hus. De allra flesta bostäderna ligger alltså i flerbostadshus, och av småhusen är bara ett fåtal äganderätter.",
       "Stadens översiktsplan pekar ut flera värdekärnor inom riksintresset för kulturmiljövården. Den tidiga bebyggelsen på malmarna – Fjällgatan, Katarinaberget, Vita bergen, Åsöberget och Östra Mariaberget – nämns tillsammans med den klassiska stenstaden från 1870–1930 och storgårdskvarteren Draget och Ryssjan vid Blecktornsparken från 1920-talet. För malmarnas bebyggelse räknar planen upp byggnadsdetaljer som fönster, entréportar och ornamentik bland de karaktärsdrag som tillsammans bildar en karaktäristisk helhetsbild.",
     ],
     "aside": {"title": "Södermalm 2025", "items": [
       "77 525 bostäder", "43 680 bostadsrätter", "211 bostäder i småhus"]}},
    {"id": "besiktning-sodermalm", "h2": "Fönster som döms ut utan att ha besiktigats",
     "paras": [
       "Riksantikvarieämbetets skrift om fönster beskriver ett mönster vid ombyggnader: de gamla bågarna slängs i container och ersätts med nya fönster i instickskarmar. Enligt skriften beror det oftast inte i första hand på att fönstren är dåliga, utan på att kostnaden för en renovering är svårare att beräkna än kostnaden för nya fönster. En viktig förutsättning för att bevara dem är enligt skriften en noggrann konditionsbesiktning, som gör att åtgärderna kan preciseras och kvantifieras – till exempel att en viss andel av droppnäsorna och karmbottenstyckena ska bytas.",
       "Ett exempel i skriften gäller ett hus från 1903 vid Birger Jarlsgatan i Stockholm med ursprungliga kopplade, inåtgående fönster. Efter en summarisk besiktning dömdes de först ut. När nära 70 procent av de 215 fönstren sedan besiktigades noggrant visade det sig att de i huvudsak var i god kondition. Problemen fanns i droppnäsorna, där 41 procent var i bristfälligt skick, och i glasningslisterna av trä, där 66 procent var urlakade eller rötskadade. Fönstren behölls, de utsatta delarna byttes mot utvald kärnfuru och resten justerades, rengjordes och målades.",
     ],
     "aside": {"title": "Vi besiktigar per fönster", "items": [
       "Droppnäsa och glasningslist", "Karmbottenstycke och bleck", "Beslag och spanjolett", "Kitt och färg"]}},
    {"id": "detaljer-sodermalm", "h2": "Droppnäsa, bleck och spanjolett",
     "paras": [
       "Kopplade, inåtgående fönster har några typiska detaljer. Riksantikvarieämbetet förklarar att fönster utan mittpost stängs med en spanjolettstång, och att droppnäsan – en trälist eller ett bleck som leder bort vattnet från bågens nederkant – är vanligast på inåtgående fönster. Under senare delen av 1800-talet fick fönster i stenhus ibland ett karmbottenstycke med droppnäsa i stället för fönsterbleck, och från sekelskiftet blev det vanligt med bleck som täcker hela den utåt blottlagda delen av karmbottenstycket, en följd av att bågarna går inåt.",
       "I 1903-exemplet var det de mest utsatta delarna som hade tagit skada, och det är dem vi byter. Originaldelarna satt kvar på de flesta övre bågarna, som sitter mer skyddade. Vid skador på karmbottenstycken räcker det enligt skriften i allmänhet att limma in nytt virke i karmens yttre, mest utsatta del.",
     ],
     "aside": None},
    {"id": "lov-sodermalm", "h2": "Klassificering, lov och föreningens underhåll",
     "paras": [
       "Plan- och bygglagen kräver att ett byggnadsverk hålls i vårdat skick och underhålls så att utformningen och de tekniska egenskaperna i huvudsak bevaras. Är byggnaden särskilt värdefull ska den underhållas så att de särskilda värdena bevaras. Stadsmuseets klassificeringskarta markerar bebyggelsen med blått, grönt, gult och grått. Är byggnaden blå- eller grönmarkerad, eller ligger den inom ett riksintresse för kulturmiljövården, behöver du enligt staden söka bygglov för åtgärder som annars kan vara bygglovsbefriade.",
       "Staden påpekar också att vissa detaljplaner har utökad lovplikt, ibland även för underhållsåtgärder, och att en antikvarisk förundersökning kan behövas före arbetet. Översiktsplanen noterar att många hus i stenstaden har en relativt låg klass, gul, för att de förändrats sedan byggtiden, men att det är betydelsen för stadsmiljön som ska vara avgörande vid prövningen, inte den enskilda byggnadens klass. När material, kulör, profiler och indelning behålls handlar det inte om någon av de fönsterändringar som staden räknar upp. Ska fönstren ändå bytas, se " + _L.format("fonsterbyte.html", "fönsterbyte") + ", och om snickeri inne i lägenheterna, se " + _L.format("snickare-sodermalm.html", "snickare på Södermalm") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi föreningens fönster på Södermalm",
  "steps": [
    ("Underlag från föreningen", "Vi tar del av underhållsplanen och ser vilken klass huset har på Stadsmuseets karta."),
    ("Konditionsbesiktning", "Fönstren besiktigas ett och ett, och skadorna noteras för varje del."),
    ("Skriftligt kostnadsförslag", "Förslaget anger hur många droppnäsor, glasningslister och karmbottenstycken som behöver bytas."),
    ("Planering mot lägenheterna", "Ordningen läggs så att varje lägenhet berörs så kort tid som möjligt."),
    ("Snickeri och målning", "Utsatta delar byts mot kärnfuru, och bågarna kittas och målas."),
    ("Justering", "Spanjoletter och beslag ställs in så att bågarna sluter."),
  ],
  "rot_h2": "ROT-avdrag vid fönsterrenovering på Södermalm",
  "rot": [
    "Rotavdraget gäller arbete i en bostad som du äger och betalar för. I en bostadsrätt ger Skatteverket bara avdrag för arbete inne i bostaden som du ansvarar för enligt stadgarna – på fönster till exempel glas i den inre bågen och tätningslist. Arbete på fönstrens utsida och mellan bågarna, och på gemensamma ytor som fasaden, ger inget avdrag för bostadsrättshavaren.",
    "Äger du ett av Södermalms få småhus räknas att reparera, byta ut och måla fönster som rotarbete. Avdraget är högst 30 procent av arbetskostnaden, med taket 50 000 kr per person och år och 75 000 kr tillsammans med rutavdrag, och det dras på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Södermalm?",
  "price": [
    "Antalet fönster, hur många delar som behöver bytas enligt besiktningen, hur mycket gammal färg som ska bort och hur arbetet måste planeras mot lägenheterna styr kostnaden. Efter ett gratis platsbesök får styrelsen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Lönar det sig att besiktiga föreningens fönster innan de byts?",
     "Riksantikvarieämbetet beskriver ett hus från 1903 där fönstren först dömdes ut, men en noggrann besiktning visade att de i huvudsak var i god kondition. Problemen fanns främst i droppnäsor och glasningslister."),
    ("Vad betyder gul klass på Stadsmuseets karta?",
     "Översiktsplanen kallar gul klass en relativt låg kulturhistorisk klassificering. Enligt staden behövs inget lov för bygglovsbefriade åtgärder på ett gult eller grått hus, om inget annat skydd gäller, till exempel riksintresse."),
    ("Vad är en droppnäsa på ett fönster?",
     "En trälist eller ett bleck som leder bort vatten från fönsterbågens nederkant. Den är vanligast på inåtgående fönster, enligt Riksantikvarieämbetet."),
    ("Kan underhåll av fönster kräva bygglov på Södermalm?",
     "Det kan det. Stockholms stad skriver att vissa detaljplaner har utökad lovplikt för åtgärder som annars inte kräver lov, till exempel underhållsåtgärder."),
    ("Ger föreningens fönsterrenovering rotavdrag till medlemmarna?",
     "Inte för fasaden eller fönstrens utsida. I en bostadsrätt godkänner Skatteverket bara arbete inne i bostaden som bostadsrättshavaren själv ansvarar för enligt stadgarna och betalar för."),
  ],
  "sources": [_OF_SOD, _OP_RIKS, _RAA_F, _PBL, _SB_KLASS, _SB_KVB, _SB_F, _SKV, _SKV2],
  "cta": ("Ska föreningens fönster bytas eller renoveras?", "Boka ett gratis platsbesök, så besiktigar vi fönstren och lämnar ett skriftligt kostnadsförslag till styrelsen."),
  "img": [
    ("Kopplat inåtgående fönster i ett stenhus med ny droppnäsa och bleck över karmbottenstycket",
     "exterior close-up of an early 1900s Stockholm stone apartment building window, coupled inward-opening wooden casement with a new pale pine drip moulding on the lower outer sash, painted sheet-metal sill covering the frame bottom, ochre rendered facade, overcast daylight, realistic photo, no people, no text, no letters"),
    ("Sekelskiftesbåge med spanjolett och lösa glasningslister av trä på en arbetsbänk",
     "old turn-of-the-century inward-opening wooden window sash on a workbench, wooden glazing beads removed and stacked beside it, brass espagnolette bar, partly scraped paint, chisel and new pine strips, daylight, realistic photo, no people, no text, no letters"),
  ],
  "related": [],
},

}
