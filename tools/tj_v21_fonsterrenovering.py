# -*- coding: utf-8 -*-
"""Fönsterrenovering – ortsidor v21: Täby, Upplands Väsby, Vallentuna, Vasastan, Värmdö, Östermalm (2026-10-26).
Deltjänst under fonsterbyte.html (TJ_HUB["fonsterrenovering"]). Intent: renovera de befintliga fönstren (kitt,
linoljefärg, bågar, spröjs, glas, beslag, tätning, innerbåge) i stället för att byta dem. Skild från ortens
fonsterbyte-<ort>.html (Täby: trä/originalformat/grupphus/energiglas; Upplands Väsby: flygbuller och ljud;
Vallentuna: flygbuller, glasval och lov; Värmdö: Gustavsbergs inventering) och från v16/v19-sidorna (Bromma, Danderyd,
Huddinge, Nacka, Norrtälje, Sigtuna, Haninge, Järfälla, Kungsholmen, Sollentuna, Solna, Södermalm) – inga lokala
vinklar, formuleringar eller FAQ återanvända. Vasastan och Östermalm har inga fonsterbyte-sidor: länk till
fonsterbyte.html. Byggtorg har bara fonsterrenovering-taby (Viggbyholm, Byle, kyrkbyn, Ella gård, Ensta,
Gribbylund, Hägerneholm, SCB, Hagby ÅVC) – inget av det används här.
Lokal vinkel per sida (en huvudfråga per sida):
Täby – storgårdarna söder om Vallentunasjön (Hagby–Såsta–Broby–Karby–Visinge–Efraimsberg, riksintresset
Skålhamravägen AB 71): fönsterkulör gård för gård, provytor enligt RAÄ, småspröjsade bågar och spröjslagning,
lov/detaljplaneskydd (Broby), ekonomibyggnader och ROT på lantbruksenhet;
Upplands Väsby – kedjehusen väster om Hammarbyvägen i Apoteksskogen–Sigma (1960-tal, särskilt värdefullt enligt
PBL 8:13): enluftsfönster med sidofönster, ursprungligen ljust grå eller gröna, enhetliga husgrupper, röta under
hörnbeslag och i fogar (60–70-talens fönster), asbest i kitt, lov och anmälan;
Vallentuna – 1960-talets tegelvillor i Karby (FÖP Karby och Brottby): fog och tätning mellan karm och tegel, vatten
under fönster, PCB/asbest i fogmassor, söderfasaden först (RAÄ), 70-talets treglas i instickskarmar (Brottby), lov;
Vasastan – Birkastaden (Stadsmuseets inventering 1973/74): 148 fastigheter 1902–12, Höög, kv Skålen och Gjutaren,
RAÄ:s jugendfönster (smalt, kopplat inåtgående, spröjsad överdel, spanjolett), gathus/gårdshus mot berget,
Stadsmuseets karta och bostadsrättens insida;
Värmdö – Barnviks by i Djurö socken (kulturmiljöprogrammet): glasverandor och äldre fönster, kitt per ruta,
bottenstycken, områdesbestämmelser med utökad lovplikt, anmälan vid underhåll, fritidshus och ROT;
Östermalm – Gärdesstaden vid Tessinparken (1932–37, nationalstadspark): en hel ruta per båge, glas från
cylinder- och Fourcaulttiden, limmade bågar (lim från 1930-talet) och snedskarvning, lov i nationalstadsparken,
bostadsrättens insida.

Fakta endast från källorna i respektive 'sources', öppnade med curl (-L, --http1.1, Mozilla-UA) och lästa
2026-10-26; alla svarade 200, pdf:er med textlager via pdftotext:
  Täby kommun – Kulturmiljöer i Täby, antagen (pdf): avsnittet Hagby – Litsby – Såsta – Broby – Karby – Valla –
  Visinge – Efraimsberg (jordbrukslandskapet söder om Vallentunasjön, förhistorisk centralbygd, lång
  brukningskontinuitet, 1800-talets sammanslagna egendomar, mindre herrgårdar med påkostade manbyggnader; större
  delen inom riksintresset Skålhamravägen AB 71, sannolikt särskilt värdefullt enligt PBL 8 kap. 13 §; Såstas äldre
  huvudbyggnad 1700-tal, timrad tvåvåning, vit panel, mörkgröna knutbrädor, fönstersnickerier och fönsterfoder;
  Såsta vagnslider rödfärgad lockläktpanel, vita småspröjsade fönster; Såstaholm påbörjad 1903, ljus puts,
  småspröjsade fönster; Broby 1700-tal, faluröd panel, profilsågade fönsterfoder, fönstersnickerier i guldockra,
  äldre bostadsbebyggelse skyddad i detaljplan; Karby huvudbyggnad 1864; Visinge huvudbyggnad 1780-tal, gul
  oljefärg, vita knutar, gröna fönstersnickerier, flera fönstertyper, tvåluftsfönster småspröjsade i övre delen;
  Marielund två boningshus kring 1900, tvåluftsfönster med spröjs och dekorativa foder; riktlinjerna: befintliga
  karaktärsdrag bör tillvaratas, lokal byggnadstradition tongivande, ombyggnader anpassas i material och
  färgsättning, äldre ekonomibyggnader bör bevaras; avsnittet Fittja: Fittja gård väster om kyrkbyns tätort,
  årtalet 1864 i frontespisen, bruna fönstersnickerier).
  Täby kommun – Fasadändring (byte av kulör = fasadändring; inget lov för en- och tvåbostadshus utom särskilt
  värdefull byggnad/område eller utökad lovplikt i detaljplan).
  Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö (pdf): Apoteksskogen – Sigma s. 114–123 (särskilt
  värdefullt PBL 8:13, uppfört 1950-, 60-tal och senare, utbyggt under 1960-talet, grannskapsenhet, kedjehus,
  lameller, punkthus, stadsdelscentrum; kedjehusen väster om Hammarbyvägen: lågt och tätt, en våning, kopplade i
  vinkel med garage och biluppställning; vit slätputs, mörkmålad sockel, svartmålat fasadband av stående träpanel,
  fönster ursprungligen ljust grå eller gröna av enluftstyp med ett sidofönster, flack pulpetform ursprungligen
  papp, bildtext med grönmålade fönster; vägledning: underhåll som enhetligt utformade grupper, respekt för
  ursprungliga materialkombinationer); Radhus och kedjehus 1960–70-tal s. 42–43 (enhetlig färgsättning och
  utformning av fasaddetaljer per bebyggelsegrupp, bibehåll och underhåll färgskalor).
  Upplands Väsby kommun – Fasadändring (definition med kulör; en- och tvåbostadshus normalt inget lov; lov kan krävas
  inom kulturhistoriskt särskilt värdefullt område; anmälan om nya fönster innebär ingrepp i stommen; varsamhet
  oavsett lovplikt).
  Vallentuna kommun – Fördjupad översiktsplan Karby och Brottby (pdf): Karbys villasamhälle utbyggt på 1960-talet,
  många tegelvillor i funktionalistisk stil, sparade tallar, tidstypiska detaljer, husen indragna från gatan, de
  flesta villorna har tegelfasader, tegel det dominerande materialet som utgångspunkt; Brottby typiska villor från
  1970-talet; historiskt rik miljö längs Långhundraleden, Vada–Össeby-Garn riksintresse, ny bebyggelse delvis inom
  riksintresset.
  Vallentuna kommun – Fasadändring (inget lov för ommålning, nytt tak eller nya fönster på en- och tvåbostadshus;
  lov om fastigheten ligger i kulturhistoriskt särskilt värdefullt område eller byggnaden är det; varsamhet).
  Stockholms stadsmuseum – Birkastaden, Röda Bergen, Rörstrand, byggnadsinventering 1973 (pdf, 1974, utdrag
  29 s. med textlager): gatorna på stadsplanen för Norrmalm 1879 och regleringsplanen 1886, större delen bebyggd
  1902–12, 148 fastigheter, A J Höög (Dorph & Höög, från 1910 Höög & Morssing) 59 hus ca 40 %, få förändringar,
  många fasader omputsade och förenklade men i stort sett ursprunglig utformning, kv Skålen Karlbergsvägen 78–84
  nationalromantik med tegel, gavlar, burspråk och smårutiga fönster i fasadlivet, 1920-talshusen i kv Gjutaren
  mot S:t Eriksgatan klassicistiska med slammad puts, breda gathus och gårdshus, T-hus, gathus 2–4 rok, gårdshus
  smålägenheter med enklare snickerier, mörka gårdshus i kv Volontären och Ugnen mot norr och bergväggar.
  Stockholmskällan / Stadsmuseet – Stockholms Spår: Gärdet (pdf): övningsfält sedan 1600-talets mitt, militären
  ut 1905, tävlingen vunnen av Arvid Stille 1929, friliggande hus i grönska, utbyggnad från 1932 vid
  Valhallavägen, husen kring Tessinparken klara 1937, punkthusen på Gärdeshöjden i stort klara 1940.
  Stockholms stad – Parkplan Östermalm, beskrivning av parker (pdf, Östermalms stadsdelsförvaltning 2018):
  Tessinparken anlades som del av Gärdesbebyggelsen, ingår i Nationalstadsparken sedan 1995.
  Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf): Gärdesstaden 1932–37 vid Tessinparken, en
  av Sveriges mest kända och helgjutna miljöer från funktionalismens genombrottstid, skyddas genom bestämmelser om
  nationalstadspark, värdebärande: omsorgsfullt utförda byggnadsdetaljer som fönster, entrépartier och
  balkongräcken; den klassiska stenstaden 1870–1930 med utbredning på Östermalm, Södermalm, Kungsholmen och Norrmalm.
  Stockholms stad (bygglov.stockholm) – Fönster och dörrar (byta material eller kulör, ändra profilering på karmar,
  bågar och spröjsar, byta upphängning, ändra indelning t.ex. lägga till spröjs eller ta bort mittpost; lovplikten
  beror på byggnaden); Stadsmuseets kulturhistoriska klassificering (riksintressen med blå ring, nationalstadsparken
  räknas dit, bygglov för annars lovbefriade åtgärder inom riksintresse eller blå/grön markering).
  Värmdö kommun och Stockholms läns museum – Värmdö: Kulturhistoria i skärgårdsbygd (pdf): 19. Barnvik, Djurö
  socken (höjdrygg längs strandkanten, gamla landsvägen, tre gårdar och flertal bostadslägenheter kring 1900,
  ett tiotal bevarade äldre bostadshus, ekonomibyggnader, uthus, lantarbetarlägenheter; sadel- eller mansardtak av
  tegel, rödmålade träpaneler, i huvudsak vita foder, ursprungligen enkelt utseende anpassat efter sekelskiftets
  ideal, många glasverandor; många bostadshus med ursprunglig karaktär med äldre paneler, glasverandor och fönster
  ger höga miljöskapande kvaliteter; två sommarvillor kring sekelskiftet, semesterparadis; fritidshus och
  permanentbostäder under 1900-talets andra hälft; områdesbestämmelser antagna av Samhällsplaneringsnämnden med
  utökad lovplikt samt varsamhets- och skyddsbestämmelser); s. 308 (PBL 8 kap. 14 § underhåll – utformning och
  tekniska egenskaper bevaras, särskilt värdefull byggnad – särskilda värden bevaras).
  Värmdö kommun – Bygga i kulturmiljöer (14 riksintressen, cirka 55 kulturmiljöområden, alla särskilt värdefulla;
  tänk på fönster och dörrar; anmälan och startbesked för underhåll av byggnad skyddad i detaljplan eller med
  särskilt bevarandevärde; kommunantikvarien); Förändringar i PBL från 1 december 2025 (lovplikt inom
  kulturhistoriskt värdefulla områden och riksintressen, kulturmiljökartan).
  Riksantikvarieämbetet – Fönster: historik och råd vid renovering (RAÄ 1988:1, pdf, OCR-text läsbar): spröjsar
  försvann mot slutet av 1800-talet, kom tillbaka kring sekelskiftet, försvann igen med funktionalismen på
  1930-talet (en hel glasruta, lägre fönster för lägre rumshöjder); jugendfönstret från Stockholm (mindre och
  relativt smalt, spröjsad överdel i dekorativt syfte, kopplade inåtgående bågar, mittposten borta, spanjolett);
  sammanfogningar demonterbara, limmet introduceras på 1930-talet, lärobok 1931: alla sammansättningar i bågar
  limmas; cylindermetoden till 1933 (parallella skiftningar, tunt, relativt klart), Fourcault från 1913, i dag
  bara floatglas; gammalt glas vid glasning i värdefulla hus, levande ojämn yta, tillvarataget glas genom
  glasmästerier; rötskador där väta trängt in och torkar långsamt, samband röta–rost, 1960–70-talens fönster
  olämpligt lösta konstruktionsdetaljer, skador under hörnbeslag och i fogar, pluggning av skruvhål, halvsulning,
  diagonalmått/styvt papper, snedskarvning, profil efter originalet, vattenfast lim, lagningsvirke av samma kvalitet
  och årsringsorientering; spröjsar skadas som nederstycket, klena, kittfals och fogar, hel spröjs – glas och beslag
  bort, bågen slås isär, ny spröjs efter förebild och tappas, mindre lagningar utan isärtagning; bara nedslitna
  partier behöver kittas och målas, i tid räcker rengöring och bättring.
  Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf): äldre färgsättning och kulörval bör
  bevaras, provytor på undanskymda ställen, uppgifter om material bevaras; söderfasader oftare än norrfasader,
  fönster oftare än fasaden; fönster m.m. löpande underhållsmålas, väntar man för länge blir det dyrare; fönster
  rengörs bäst med sodatvätt för hand, kittfalsar skrapas och grundas före kittning; fönsterkittet ska vara helt så
  att fukt inte orsakar röta; ytterbågens insida med utomhusfärg.
  Länsstyrelserna i Gävleborgs, Västmanlands och Örebro län – Fönster (pdf): bågar med tappar och träplugg utan lim
  kan tas isär; vattnet på utsidan gör nedre delen utsatt, rötskador oftast i bågens och karmens bottenstycken;
  rostiga beslag kan oftast renoveras; hörnjärn rostskyddas; rötskadat virke skarvas med nytt virke av god
  kvalitet; linoljekitt (bladets kostnadstabell i kr medvetet INTE använd).
  Boverket – Energiguiden: fönster och dörrar (täta: isolering runt karmen, drevning, lister; gamla tätningar
  släpper igenom vatten under fönstren särskilt vid slagregn; utred fuktskador; fogmassor med PCB eller asbest
  saneringspliktiga; kitt kan innehålla asbest; inre rutan till energiglas/tvåglaskassett; äldre munblåst eller
  valsat glas som ytterrutor; 70-talets treglas i instickskarmar; förbättra befintliga fönster kan vara mer
  lönsamt om de är i gott skick). Boverket – Risker med hantering av asbest (förbud 1982, främst 1940–1970,
  1940–1980 sannolikt, fönsterkitt och fogmassor bland exemplen).
  Skatteverket – Ger arbetet rätt till rotavdrag? (småhus: reparera eller byta ut fönster, måla fönster, byta och
  reparera fönsterbleck, sanera asbest i samband med byggarbete, inte mäta asbest, glasa in balkonger och altaner,
  inte glasarbeten i företagets lokaler; bostadsrätt: innanför tak, väggar och golv enligt stadgarna, insidan av
  fönster – glas i inre bågen, tätningslist, innerfönster, fönsterfoder, måla insidan – inte utsidan, mellan
  bågarna eller gångjärn). Skatteverket – Så fungerar rotavdraget (högst 30 procent av arbetskostnaden, 50 000 /
  75 000 kr, bara arbetskostnaden, äga bostaden, fritidshus men inte om någon annan bor där permanent, lantbruksenhet
  – bostadsbyggnaden och tomten, inte ekonomibyggnader).
Strukna (ej verifierade, oklara i källan eller medvetet utelämnade): Hagby gårds byggår (underlaget anger både 1891
och 1893 – utelämnat); Såstaholms arkitekt; Vallentunas kulturmiljöprogram och kulturmiljöanalysen för Lindholmen
(dok.vallentuna.se svarade inte 2026-10-26); Kårsta som riksintresse (ÖP 2040 och malare-vallentuna motsäger
varandra – inte använt); att Karbys tegelvillor har skalmur eller viss fönstertyp (skrivet bara som tegelfasad);
att Birkastadens lägenheter är bostadsrätter (ingen källa – skrivet villkorat); Stadsmuseets svarstid; att
Gärdet tillhör Östermalm förankrat i Parkplan Östermalm (Tessinparken i stadsdelsförvaltningens parkplan), inte
i ÖP; Gärdets bostadsrättsandel (används redan av golvslipning-ostermalm – utelämnad); vilken glastyp Gärdets hus
faktiskt har (skrivet som möjlighet utifrån RAÄ:s årtal); Boverkets bidrag (osäkert om det är öppet);
Länsstyrelsens kostnadstabell; alla priser, avgifter, handläggningstider och tidsåtgång. Inga garantier, omdömen,
egna uppdrag i orterna eller cert. Perks enbart sajtens befintliga: gratis platsbesök, skriftligt
kostnadsförslag, ROT direkt på fakturan.
Kritikpass 2026-10-26 (alla 21 källor öppnade igen, varje faktamening mot källtexten): Upplands Väsby –
energiguidens kitt/asbest "ska hanteras" -> "bör hanteras" (guidens ordalydelse); lovregeln i särskilt värdefullt
område "kan krävas" -> "krävs" (kommunens lista "Det krävs alltid bygglov ... inom ett kulturhistoriskt särskilt
värdefullt område"; ordet "alltid" undvikt). Vallentuna – "delar av planområdet ligger inom riksintresset" ->
"planen föreslår att ny bebyggelse delvis hamnar inom riksintresset" (FÖP:ens lydelse). Vasastan – bostadsrättslagen
kontrollerad (7 kap. 12 §: egen bekostnad, gott skick, om inte stadgarna bestämmer annat). Vasastan och Östermalm –
Boverkets slagregnsmening och RAÄ:s söder/norr-mening används bara på Vallentunasidan (inga dubbla fakta mellan
sidorna). Kontrollerat utan ändring: 1864 (Karby, Fittja), 1780-tal (Visinge), 1903 (Såstaholm), AB 71, 1879/1886,
1902–12, 148/59/ca 40 %, Karlbergsvägen 78–84, 1905/1929/1932/1937/1940, 1995 (Tessinparken), 1913/1927/1933 (glas),
1931 (lim), 1982/1940–1970/1940–1980 (asbest), 14 riksintressen och cirka 55 kulturmiljöområden, ROT-regler
(lantbruksenhet, fritidshus, bostadsrättens insida, glasarbeten i egna lokaler, mäta/sanera asbest, fönsterbleck).
tj_check: 0 FEL; WARN kvar bara "bild saknas" (bilderna genereras av ägaren).
Kritikpass (strikt) 2026-10-26: alla 21 källor öppnade igen (curl; Skatteverket efter omförsök; pdf:er med
textlager – RAÄ-skrifterna och Gärdet-pdf:en är OCR men läsbara). Ändrat: Vasastan – title "Birkastadens
jugendfönster" -> "jugendhusen i Birkastaden" (inventeringen beskriver jugendutformade fasader, inte husens fönster;
RAÄ:s jugendfönster är ett allmänt Stockholmsexempel), card och description i samma anda, lead "husen hade i stort
sett kvar" -> "fasaderna" (inventeringens ord), FAQ "jugendfönster i Vasastan" -> "i Stockholm" (RAÄ). Östermalm –
title/card/steps_h2 "Gärdets 1930-talsfönster" -> "1930-talshusen på Gärdet" (att originalfönstren finns kvar är
obelagt; Gärdesstaden 1932–37 är belagt), description "glas från 1930-talet" -> "äldre glas". Täby – riktlinjen om
ekonomibyggnader "ska ske hänsynsfullt" -> "bör" (källans ord). Kontrollerat utan ändring: Täby (centralbygd, AB 71 och
PBL 8:13 "sannolikt" gäller även avsnittet Hagby–Efraimsberg, Karby 1864, Visinge 1780-tal/gul oljefärg/gröna
snickerier/tvåluftsfönster, Såsta mörkgrönt, Broby guldockra/detaljplaneskydd, Såstaholm 1903, vagnslidret,
Marielund, Fittja 1864/bruna snickerier; RAÄ provytor/kulörval; spröjslagningen); Upplands Väsby (Apoteksskogen
1960-tal, grannskapsenhet, PBL 8:13, kedjehusen väster om Hammarbyvägen, vit slätputs/svart fasadband, ljust grå eller
grön, enluft med sidofönster, papp, vägledningarna; RAÄ röta/1960–70-tal/hörnbeslag/plugg/halvsulning/diagonal;
Boverket asbest 1940–1980/fönsterkitt; kommunens lista "alltid bygglov ... särskilt värdefullt område"; anmälan vid
ingrepp i stommen); Vallentuna (Karby 1960-tal, tegelvillor, tallar, indragna hus, "de flesta villorna har
tegelfasader", Brottby 1970-tal, Vada–Össeby-Garn; Boverket slagregn/PCB/asbest/treglas; RAÄ söder/norr, nedslitna
partier, sodatvätt); Vasastan (1879/1886, 1902–12, 148/59/ca 40 %, tre hus rivna 1960-tal, kv Skålen 78–84, kv
Gjutaren, T-hus, Volontären/Ugnen; RAÄ jugendfönstret; stadens fönsterlista; blå/grön markering kräver lov;
stenstaden 1870–1930 på Norrmalm; BRL 7:12); Värmdö (Barnvik: höjdrygg, tre gårdar, ett tiotal hus, glasverandor,
områdesbestämmelser med utökad lovplikt, sommarvillor, fritidshus andra hälften av 1900-talet, PBL 8:14; RAÄ kitt;
Länsstyrelsernas blad); Östermalm (Gärdet 1600-tal/1905/1929/1932/1937/1940, Frölén, skiffertak, portar; ÖP
helgjutna/fönster som värdebärande/nationalstadspark; Tessinparken 1995; RAÄ 1930-tal, cylinder till 1933, Fourcault
1913, Glava 1927, floatglas, gammalt glas, lim 1931, snedskarv, årsringar); ROT mot Skatteverket. tj_check: 0 FEL,
inga WARN för v21-fönsterrenovering.
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
_RAA_M = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färgtyper (pdf)",
          "https://www.raa.se/publicerat/9789172095830.pdf")
_LST_F = ("Länsstyrelserna i Gävleborgs, Västmanlands och Örebro län – Information om byggnadsvård: Fönster (pdf)",
          "https://catalog.lansstyrelsen.se/store/23/resource/2000__13")
_BV_F = ("Boverket – Energiguiden: Energirenovera eller byta fönster och dörrar",
         "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/fonster_dorrar/")
_BV_ASB = ("Boverket – Risker med hantering av asbest i byggnader",
           "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/asbest/")
_SB_F = ("Stockholms stad – Fönster och dörrar (bygglov.stockholm)",
         "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fonster-och-dorrar/")
_SB_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering (bygglov.stockholm)",
             "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_OP_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
            "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 12 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")

# ------------------------------------------------------------------ lokala källor
_TABY_KM = ("Täby kommun – Kulturmiljöer i Täby, antagen (pdf)",
            "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf")
_TABY_FAS = ("Täby kommun – Fasadändring",
             "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/fasadandring")
_UV_KU = ("Upplands Väsby kommun – Kunskapsunderlag för kulturmiljö i Upplands Väsby (pdf)",
          "https://www.upplandsvasby.se/download/18.11ea930419a75a29e90820/1763480197488/Kunskapsunderlag%20f%C3%B6r%20kulturmilj%C3%B6%20i%20Upplands%20V%C3%A4sby%201.pdf")
_UV_FAS = ("Upplands Väsby kommun – Fasadändring",
           "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/fasadandring")
_VAL_KB = ("Vallentuna kommun – Fördjupad översiktsplan för Karby och Brottby (pdf)",
           "https://vallentuna.se/download/18.63572f8619eeecafce08376/1782478381270/2.11.8%20F%C3%B6rdjupad%20%C3%B6versiktsplan%20Karby%20Brottby.pdf")
_VAL_FAS = ("Vallentuna kommun – Fasadändring",
            "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/behover-jag-bygglov/fasadandring")
_SSM_BIRKA = ("Stockholms stadsmuseum – Birkastaden, Röda Bergen, Rörstrand: byggnadsinventering 1973 (pdf)",
              "https://stockholmskallan.stockholm.se/postfiles/KUL/SSM_Birkastaden,_Roda_Bergen,_Rorstrand__by_1974_00.pdf")
_SSM_GARDET = ("Stockholmskällan / Stadsmuseet – Stockholms Spår: Gärdet (pdf)",
               "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000031.pdf")
_PP_OST = ("Stockholms stad – Parkplan Östermalm: beskrivning av parker (pdf)",
           "https://start.stockholm/globalassets/start/om-stockholms-stad/sa-arbetar-staden/natur-parker-och-gronomraden/parkplan-ostermalm---beskrivning-av-parker.pdf")
_VD_KMP = ("Värmdö kommun och Stockholms läns museum – Värmdö: Kulturhistoria i skärgårdsbygd (pdf)",
           "https://www.varmdo.se/download/18.7faa473e19913ae5e0f1f12/1757318877718/Kulturmilj%C3%B6v%C3%A5rdsprogrammet%20V%C3%A4rmd%C3%B6_2.pdf")
_VD_KM = ("Värmdö kommun – Bygga i kulturmiljöer",
          "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/bygglov/byggaikulturmiljoer.4.57b4a3ba16e6b961dbf10429.html")
_VD_PBL = ("Värmdö kommun – Förändringar i plan- och bygglagen från 1 december 2025",
           "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/forandringaripblfrom1december2025.4.18b9914519a768a188a2872.html")

_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
            "tillsammans med rutavdrag. Det är bara arbetskostnaden som ger avdrag.")
_IMG_END = ", realistic photo, no people, no text, no letters"

PAGES_TJ = {

# ------------------------------------------------------------------ TÄBY
"fonsterrenovering-taby.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Täby", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Täby – gårdarna vid Vallentunasjön",
  "description": "Fönsterrenovering i Täby: storgårdarna söder om Vallentunasjön, fönsterkulör gård för gård, småspröjsade bågar och lov i riksintresset.",
  "h1": "Fönsterrenovering i Täby",
  "lead": "Söder om Vallentunasjön ligger Täbys gamla storgårdar, och kommunens kulturmiljöunderlag beskriver fönster i olika kulörer från gård till gård. Geal Entreprenad AB renoverar fönster i hela Täby – kittar, lagar bågar och spröjs och målar med linoljefärg – och utgår från den färgsättning som redan finns på huset.",
  "card": "Gårdarnas fönster, kulör och spröjs.",
  "sections": [
    {"id": "gardarna-taby", "anchor": "Gårdarna",
     "h2": "Storgårdarna söder om Vallentunasjön",
     "paras": [
       "Kunskapsunderlaget Kulturmiljöer i Täby beskriver jordbrukslandskapet söder om Vallentunasjön, med Hagby, Litsby, Såsta, Broby, Karby, Valla, Visinge och Efraimsberg, som en förhistorisk centralbygd med lång brukningskontinuitet. Under 1800-talet slogs egendomar samman till medelstora och stora gårdar, och några fick karaktär av mindre herrgårdar med påkostade manbyggnader. Karby gårds huvudbyggnad uppfördes 1864, och Visinge har en huvudbyggnad från 1780-talet.",
       "Större delen av området ligger inom riksintresset för kulturmiljövården Skålhamravägen (AB 71). Underlaget skriver att ett sådant område sannolikt också är ett särskilt värdefullt område enligt plan- och bygglagen 8 kap. 13 §. Riktlinjerna säger att befintliga karaktärsdrag bör tas tillvara, att den lokala byggnadstraditionen ska fortsätta vara tongivande och att ombyggnader vid gårdsmiljöerna bör anpassas i material och färgsättning. Ett renoverat originalfönster gör just det. Är ett fönster för skadat för att lagas finns mer under " + _L.format("fonsterbyte-taby.html", "fönsterbyte i Täby") + ".",
     ],
     "aside": {"title": "Gårdarna i underlaget", "items": [
       "Hagby och Litsby", "Såsta och Broby", "Karby och Valla", "Visinge och Efraimsberg"]}},
    {"id": "kulorer-taby", "h2": "Varje gård har sin fönsterkulör",
     "paras": [
       "Underlaget beskriver färgsättningen gård för gård. Såsta gårds äldre huvudbyggnad från 1700-talet är en timrad tvåvåningsbyggnad med vit panel, och där är knutbrädor, fönstersnickerier och fönsterfoder mörkgröna. Broby har faluröd panel, profilsågade fönsterfoder och fönstersnickerier i guldockra. På Visinge är panelen målad med gul oljefärg, knutarna vita och fönstersnickerierna gröna. Fittja gård, väster om kyrkbyn, har årtalet 1864 i frontespisen och bruna fönstersnickerier.",
       "Riksantikvarieämbetets handbok om byggnadsmåleri skriver att äldre färgsättning och kulörval bör bevaras, eftersom de i regel är typiska för den tid huset kommer från eller har brukats under. Handboken råder också att spara några små provytor utan behandling på undanskymda ställen och att bevara uppgifter om vilka material renoveringen gjordes med, så att nästa renovering har något att gå på. Vi gör så när vi skrapar bågarna: en liten yta får vara kvar, och vi skriver ner kulör och färgtyp åt dig.",
     ],
     "aside": {"title": "Fönsterkulörer i underlaget", "items": [
       "Såsta – mörkgrönt", "Broby – guldockra", "Visinge – grönt", "Fittja – brunt"]}},
    {"id": "sprojs-taby", "h2": "Småspröjsade bågar lagas spröjs för spröjs",
     "paras": [
       "Flera av gårdarnas fönster är indelade i små rutor. På Visinge finns flera olika fönstertyper, och i bottenvåningen sitter tvåluftsfönster som är småspröjsade i övre delen. Såstaholms huvudbyggnad, som började uppföras 1903, har ljust putsad fasad och småspröjsade fönster, och de två boningshusen vid Marielund har tvåluftsfönster med spröjs och dekorativa foder. Även Såsta gårds vagnslider har vita småspröjsade fönster i en rödfärgad lockläktpanel.",
       "Riksantikvarieämbetets skrift om fönster beskriver att spröjsar skadas på samma sätt som bågens nederstycke. Angreppen är ofta små men kan vara allvarliga, eftersom spröjsarna är så klena, och röta uppstår både i kittfalsen och i fogarna mot bågen. Ska en hel spröjs ersättas måste glas och beslag tas bort så att bågen kan slås isär, och den nya spröjsen tillverkas med den gamla som förebild och tappas på samma sätt. Vid mindre skador kan de skadade delarna bytas utan att bågen tas isär. Därefter kittas varje ruta med linoljekitt.",
     ],
     "aside": None},
    {"id": "lov-taby", "h2": "Lov, detaljplan och uthusens fönster",
     "paras": [
       "Täby kommun skriver att en fasadändring kan vara att byta kulör, och att en- och tvåbostadshus inte behöver bygglov för fasadändringar om byggnaden inte är särskilt värdefull, ligger i ett särskilt värdefullt område eller har utökad lovplikt i detaljplanen. I Broby är den äldre bostadsbebyggelsen skyddad i detaljplan. Att skrapa, kitta och måla bågarna i samma kulör som i dag är underhåll, men ska fönstren få en ny kulör på en av gårdarna bör du fråga kommunen först.",
       "Underlaget säger också att äldre ekonomibyggnader bör bevaras och att ombyggnad bör ske hänsynsfullt om de får ny användning. Deras fönster renoveras på samma sätt som bostadshusets, men rotavdraget skiljer sig: för ett småhus på en lantbruksenhet ger Skatteverket avdrag för arbete i bostadsbyggnaden och på tomten runt den, inte på ekonomibyggnader. Om målning av fasad och snickerier kan du läsa under " + _L.format("malare-taby.html", "målare i Täby") + " och om nya fönster under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönster på en gård i Täby",
  "steps": [
    ("Platsbesök", "Vi går igenom fönstren på bostadshuset och uthusen och noterar kulör, indelning och skador."),
    ("Skrapprov", "En liten yta skrapas fram för att se vilka färglager och kulörer bågarna har haft."),
    ("Skriftligt kostnadsförslag", "Kittning, spröjslagning och målning står för sig, byggnad för byggnad."),
    ("Lagning", "Bågar med skadade spröjsar tas isär vid behov och lagas med virke av samma slag."),
    ("Kitt och linoljefärg", "Rutorna kittas med linoljekitt och bågarna målas i tunna lager i gårdens kulör."),
    ("Genomgång", "Vi visar provytan som har sparats och lämnar uppgifter om kulör och färgtyp."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Täby",
  "rot": [
    "Skatteverket räknar reparation och målning av fönster i ett småhus som rotarbete. På en lantbruksenhet gäller avdraget bostadsbyggnaden och tomten runt den, inte ekonomibyggnaderna, och du ska äga bostaden när arbetet utförs.",
    _ROT_SUM + " Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Täby?",
  "price": [
    "Antalet fönster och lufter, hur många småspröjsade rutor som ska kittas om, om spröjsar eller bottenstycken behöver bytas och hur många byggnader på gården som ingår påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken kulör hade fönstren på Såsta och Broby gårdar?",
     "Enligt Täbys kulturmiljöunderlag är fönstersnickerierna mörkgröna på Såsta gårds äldre huvudbyggnad och målade i guldockra på Broby."),
    ("Varför ska en liten yta på fönsterbågen lämnas oskrapad?",
     "Riksantikvarieämbetet råder att spara små provytor utan behandling på undanskymda ställen. De visar nästa gång vilka färger och material som har använts."),
    ("Kan en enstaka rutten spröjs bytas utan att hela bågen tas isär?",
     "Vid mindre skador går det, enligt Riksantikvarieämbetet. Ska hela spröjsen ersättas måste glas och beslag bort så att bågen kan slås isär."),
    ("Ligger gårdarna söder om Vallentunasjön i ett riksintresse?",
     "Större delen av området ingår i riksintresset för kulturmiljövården Skålhamravägen (AB 71), enligt kommunens underlag Kulturmiljöer i Täby."),
    ("Behöver jag bygglov för att måla gårdens fönster i en ny kulör i Täby?",
     "Inte för ett vanligt en- eller tvåbostadshus. Är byggnaden eller området särskilt värdefullt, eller har detaljplanen utökad lovplikt, kan det krävas enligt Täby kommun."),
  ],
  "sources": [_TABY_KM, _TABY_FAS, _RAA_M, _RAA_F, _LST_F, _SKV, _SKV2],
  "cta": ("Har gården gamla fönster som behöver ses över?", "Boka ett gratis platsbesök, så går vi igenom fönstren på alla byggnader och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Vitmålad huvudbyggnad med tegeltak och mörkgröna fönster på en gård i jordbrukslandskap",
     "old white painted two-storey timber manor farmhouse with a red clay tile mansard roof in Swedish farmland, dark green painted window frames, casings and corner boards, small-paned windows, gravel yard and large old trees, open fields and a lake in the distance, early summer morning light" + _IMG_END),
    ("Småspröjsad fönsterbåge med nytt linoljekitt och guldockra foder i en faluröd panelvägg",
     "close-up of an old two-light wooden window with small panes, freshly puttied with linseed putty, golden ochre painted sashes and profiled casing set in a red ochre painted wooden board wall, soft daylight" + _IMG_END),
    ("Fönsterbågar med spröjs på en arbetsbänk under renovering",
     "old small-paned wooden window sashes lying on a workbench in a carpentry workshop, one sash partly stripped of paint, a new pine muntin piece next to it, putty knife and paint scraper on the bench, warm workshop light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"fonsterrenovering-upplands-vasby.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Upplands Väsby", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Upplands Väsby – 1960-talets kedjehus",
  "description": "Fönsterrenovering i Upplands Väsby: kedjehusen i Apoteksskogen, enluftsfönster med sidofönster, grå och gröna bågar, röta vid beslagen och lov.",
  "h1": "Fönsterrenovering i Upplands Väsby",
  "lead": "I Apoteksskogen byggdes på 1960-talet en hel grannskapsenhet med punkthus, lameller och kedjehus i en våning. Geal Entreprenad AB renoverar fönster i Upplands Väsby och ser till att bågarna i ett kedjehus fortsätter att stämma med grannhusens, både i kulör och utförande.",
  "card": "Kedjehusens fönster, kulör och beslag.",
  "sections": [
    {"id": "apoteksskogen-uv", "anchor": "Apoteksskogen",
     "h2": "Kedjehusen väster om Hammarbyvägen",
     "paras": [
       "Kommunens kunskapsunderlag för kulturmiljö beskriver Apoteksskogen som ett större bebyggelseområde som byggdes ut under 1960-talet, med kedjehus, lameller, punkthus och ett mindre stadsdelscentrum. Området planerades som en så kallad grannskapsenhet och bedöms tillsammans med Sigma som ett särskilt värdefullt bebyggelseområde enligt plan- och bygglagen 8 kap. 13 §. Kedjehusområdet väster om Hammarbyvägen skiljer sig från resten genom att vara lågt och tätt, med markbostäder och egna trädgårdar. Husen har en våning och står sammankopplade i vinkel, med plats för garage och bil emellan.",
       "Fasaderna är slätputsade i vitt med mörkmålad sockel, och mot taket löper ett svartmålat fasadband av stående träpanel. Taken har flack pulpetform och var från början täckta med papp. Fönstren var enligt underlaget ursprungligen ljust grå eller gröna och av enluftstyp med ett sidofönster, och bland bilderna finns ett hus med välbevarad fasad och grönmålade fönster.",
     ],
     "aside": {"title": "Kedjehusen enligt underlaget", "items": [
       "Vit slätputs, mörk sockel", "Svart fasadband av trä", "Enluftsfönster med sidofönster", "Ursprungligen grå eller gröna bågar"]}},
    {"id": "grupp-uv", "h2": "Samma fönster i hela husgruppen",
     "paras": [
       "Vägledningen för Apoteksskogen och Sigma säger att bebyggelsen ska underhållas som enhetligt utformade grupper inom den större helhetsmiljön, med respekt för ursprungliga materialkombinationer. Den karaktärsmiljö som kommunen kallar radhus och kedjehus från 1960–70-talen beskrivs på samma sätt: enhetlig färgsättning och utformning av fasaddetaljer per bebyggelsegrupp är ett bevarandevärt drag, och områdenas färgskalor ska bibehållas och underhållas.",
       "När ett kedjehus renoveras för sig berör fönstren därför hela längans uttryck. Innan vi målar skrapar vi fram de äldsta färglagren på bågarna och jämför med grannhusen, så att det går att se om fönstren fortfarande har en grå eller grön ton eller har fått en annan kulör senare. Huvudbågen och sidofönstret får samma förarbete och samma kulör. Gäller frågan i stället nya fönster, till exempel för bättre ljudisolering, finns mer under " + _L.format("fonsterbyte-upplands-vasby.html", "fönsterbyte i Upplands Väsby") + ".",
     ],
     "aside": None},
    {"id": "rota-uv", "h2": "Röta vid beslag och fogar i 1960-talets bågar",
     "paras": [
       "Riksantikvarieämbetets skrift om fönster beskriver att rötskador uppstår där väta under lång tid har kunnat tränga in i virket och bara torka ut långsamt, och att det finns ett samband mellan röta och rost på skruvar och beslag. De omfattande skador som har visat sig på 1960- och 70-talens fönster beror enligt skriften även på olämpligt lösta konstruktionsdetaljer. Bågarna är ofta skadade under hörnbeslagen och i fogarna, och därför räcker det sällan att bara byta det nedre bågträet.",
       "Vid mindre skador vid ett vinkelbeslag kan skruvhålen borras upp och pluggas med nytt virke, och skadade partier kan halvsulas så att bara de yttre delarna ersätts. Innan beslagen lossas mäts bågens diagonaler, så att formen inte ändras när den sätts ihop. Länsstyrelsernas blad om fönster tillägger att rostiga beslag oftast går att renovera. Vi rostskyddsbehandlar dem och skruvar tillbaka dem i friskt virke.",
     ],
     "aside": {"title": "Det vi kontrollerar", "items": [
       "Virket under hörnbeslagen", "Fogarna i bågens hörn", "Nedre bågträet", "Kittet mot glaset"]}},
    {"id": "lov-uv", "h2": "Kitt, lov och anmälan i ett värdefullt område",
     "paras": [
       "Kitt från den här tiden behöver undersökas innan det tas bort. Boverket skriver att det sannolikt finns asbest någonstans i en byggnad som är uppförd mellan 1940 och 1980, och fönsterkitt finns bland exemplen. Energiguiden påpekar att kitt kan innehålla asbest, vilket bör hanteras enligt arbetsmiljöreglerna. Vi tar därför prov innan vi skrapar ur kittfalsarna.",
       "Upplands Väsby kommun skriver att en- och tvåbostadshus i normala fall inte behöver bygglov för fasadändringar, som en ny kulör. Inom ett kulturhistoriskt särskilt värdefullt område krävs däremot bygglov för fasadändringar, och kravet på varsamhet gäller oavsett lovplikt. En anmälan behövs om nya fönster innebär ingrepp i stommen. En renovering där bågarna behåller form och kulör är underhåll. Om målning av puts läser du mer under " + _L.format("malare-upplands-vasby.html", "målare i Upplands Väsby") + " och om fönsterbyte i stort under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönstren i ett kedjehus i Upplands Väsby",
  "steps": [
    ("Platsbesök", "Vi öppnar varje båge och sidofönster och känner efter röta under beslag och i fogar."),
    ("Prov på kitt och färg", "Kittet provas för asbest och färglagren skrapas fram för att se ursprungskulören."),
    ("Skriftligt kostnadsförslag", "Lagning, kittning och målning står var för sig, fönster för fönster."),
    ("Lagning", "Skadat virke halvsulas, beslag rostskyddas och skruvas i friskt trä."),
    ("Kittning och målning", "Linoljekitt i falsen och tunna strykningar i den kulör husgruppen har."),
    ("Genomgång", "Vi går igenom fönstren med dig och justerar där en båge tar emot."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Upplands Väsby",
  "rot": [
    "Skatteverket räknar reparation och målning av fönster i ett småhus som rotarbete. Är ditt kedjehus en bostadsrätt – Skatteverket nämner att även ett radhus kan vara det – ger bara arbete på insidan av fönstren avdrag, till exempel nytt glas i den inre bågen, tätningslist eller målning av insidan.",
    _ROT_SUM + " Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Upplands Väsby?",
  "price": [
    "Antalet fönster och sidofönster, hur mycket virke som behöver bytas vid beslag och fogar och om kittet måste saneras påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilken kulör hade fönstren i kedjehusen i Apoteksskogen från början?",
     "Enligt kommunens kunskapsunderlag var fönstren ursprungligen ljust grå eller gröna och av enluftstyp med ett sidofönster."),
    ("Varför ruttnar 1960-talets fönsterbågar under hörnbeslagen?",
     "Fukt samlas vid rostiga skruvar och beslag och torkar ut långsamt. Riksantikvarieämbetet pekar också på olämpligt lösta konstruktionsdetaljer i 1960- och 70-talens fönster."),
    ("Är Apoteksskogen ett kulturhistoriskt värdefullt område?",
     "Ja. Kommunens kunskapsunderlag bedömer Apoteksskogen och Sigma som ett särskilt värdefullt bebyggelseområde enligt plan- och bygglagen 8 kap. 13 §."),
    ("Varför mäts fönsterbågens diagonaler innan beslagen lossas?",
     "Så att bågen får samma form när den sätts ihop igen. Riksantikvarieämbetet råder att mäta noggrant eller föra över måtten på ett styvt papper."),
    ("Behövs en anmälan för fönsterarbete i ett kedjehus i Upplands Väsby?",
     "Kommunen kräver en anmälan när nya fönster eller dörrar innebär ingrepp i husets stomme. En renovering av befintliga bågar gör inte det."),
  ],
  "sources": [_UV_KU, _UV_FAS, _RAA_F, _LST_F, _BV_ASB, _BV_F, _SKV, _SKV2],
  "cta": ("Behöver kedjehusets fönster renoveras?", "Boka ett gratis platsbesök, så går vi igenom bågar, beslag och kulör och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Vitputsade kedjehus i en våning med svart träpanel under takfoten och grönmålade fönster",
     "row of single-storey 1960s Swedish link houses with smooth white rendered facades, a black painted vertical wooden fascia band under a low flat monopitch roof, dark plinth, pale green painted wooden windows each with a narrow side window, carports between the houses, low clipped hedges and a tree by each driveway, overcast spring day" + _IMG_END),
    ("Treluftsfönster i en vit putsfasad, nymålat i ljusgrått",
     "close-up of a 1960s three-light wooden window in a smooth white rendered wall, freshly painted pale grey frame and sashes, simple metal sill, soft daylight" + _IMG_END),
    ("Nedre hörnet av en fönsterbåge med renoverat hörnbeslag och lagat virke",
     "close-up of the lower corner of an old painted wooden window sash on a workbench, a cleaned and rust-protected steel corner bracket beside newly spliced pine wood, screws and a small try square, workshop light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VALLENTUNA
"fonsterrenovering-vallentuna.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Vallentuna", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Vallentuna – tegelvillorna i Karby",
  "description": "Fönsterrenovering i Vallentuna: 1960-talets tegelvillor i Karby, tätning runt karmen, vatten under fönstret, gamla fogmassor och 70-talets treglas.",
  "h1": "Fönsterrenovering i Vallentuna",
  "lead": "I Karby växte ett villasamhälle fram på 1960-talet, och de flesta husen där har fasader av tegel. Geal Entreprenad AB renoverar fönster i Vallentuna och ser över både bågarna och anslutningen mellan karmen och tegelväggen.",
  "card": "Fönster i tegelvillan, fog och bågar.",
  "sections": [
    {"id": "karby-vallentuna", "anchor": "Karby",
     "h2": "Villasamhället i Karby från 1960-talet",
     "paras": [
       "Den fördjupade översiktsplanen för Karby och Brottby beskriver Karbys villasamhälle som utbyggt på 1960-talet. Bebyggelsen är till stor del typisk för tiden, med många tegelvillor i funktionalistisk stil som är varsamt placerade i terrängen och har sparade äldre tallar mellan husen. Många av villorna har enligt planen arkitektoniska kvaliteter med tidstypiska detaljer, och även strukturen med husen indragna från gatan är tidstypisk. I Brottby finns typiska villor från 1970-talet.",
       "Planen pekar ut teglet som det dominerande materialet i området och vill att det ska vara utgångspunkt när något nytt gestaltas. Karby och Brottby ligger dessutom i en historiskt rik miljö längs Långhundraleden, och planen föreslår att ny bebyggelse delvis hamnar inom riksintresset för kulturmiljövården Vada–Össeby-Garn. I en tegelvilla är det originalfönstren, inramade av muren, som bär mycket av de tidstypiska detaljerna, och därför lagar vi dem hellre än byter.",
     ],
     "aside": {"title": "Karby och Brottby i planen", "items": [
       "Villasamhälle från 1960-talet", "Tegelvillor i funktionalistisk stil", "Sparade tallar mellan husen", "Villor från 1970-talet i Brottby"]}},
    {"id": "karm-vallentuna", "h2": "Mötet mellan karm och tegelvägg",
     "paras": [
       "Boverkets energiguide skriver att det enklaste sättet att förbättra ett fönster är att se till att det är tätt, och nämner isoleringen runt karmen, drevningen och listerna mellan båge och karm. Guiden påpekar också att gamla fönstertätningar ofta släpper igenom vatten under fönstren, särskilt i lägen som utsätts för slagregn, och råder att utreda om det finns fuktskador i väggen innan något görs.",
       "Vid platsbesöket tittar vi därför på fogen mellan karm och tegel, på blecket under fönstret och på karmens bottenstycke innan vi rör bågarna. Gamla fogmassor ska undersökas innan de tas bort: energiguiden skriver att de kan innehålla till exempel PCB eller asbest, som är saneringspliktigt. Boverkets sida om asbest anger att materialet förbjöds inom byggsektorn 1982 och främst finns i byggnader från 1940–1970. Ett prov avgör, och först därefter fogar vi om.",
     ],
     "aside": None},
    {"id": "soder-vallentuna", "h2": "Södersidans fönster först",
     "paras": [
       "Riksantikvarieämbetets handbok om byggnadsmåleri skriver att söderfasader behöver målas om oftare än norrfasader, och att fönster behöver det oftare än fasaden omkring. Fönster hör till de byggnadsdelar som bör underhållsmålas löpande. Väntar man för länge riskerar underlaget att ta skada, och då blir kommande renoveringar både dyrare och mer komplicerade.",
       "I en villa med fönster åt alla håll är det därför sällan alla bågar som behöver samma insats. RAÄ:s skrift om fönster påpekar att bara de partier som verkligen är nedslitna behöver kittas och målas om, och görs det i tid räcker det ofta med rengöring och bättring. Fönstersnickerier rengörs bäst med sodatvätt för hand, löst kitt skrapas bort och blottade kittfalsar grundas innan de kittas. Vi delar upp kostnadsförslaget fönster för fönster, så att de mest utsatta kan göras först.",
     ],
     "aside": {"title": "Ordningen vid ommålning", "items": [
       "Sodatvätt för hand", "Skrapning av löst kitt", "Grundning av kittfalsen", "Kittning och tunna strykningar"]}},
    {"id": "treglas-vallentuna", "h2": "När 1970-talets treglas inte går att rädda",
     "paras": [
       "Boverket beskriver ett fall där byte är rimligare än renovering: treglasfönster vars glaskassett har förlorat sin funktion samtidigt som monteringen i instickskarmar ger betydande energiförluster. Det är enligt Boverket vanligt för treglasfönster som sattes in under sjuttiotalet. Är fönstren i stället i gott skick kan det vara mer lönsamt att förbättra dem, till exempel genom att täta eller byta den inre rutan till energiglas, än att byta till nya.",
       "Vallentuna kommun skriver att en- och tvåbostadshus inte behöver bygglov för ändringar som nya fönster, men att lov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden är särskilt värdefull. Ändringar ska ändå göras varsamt och anpassas till byggnadens värden. Om fönsterbyte, flygbuller och glasval kan du läsa under " + _L.format("fonsterbyte-vallentuna.html", "fönsterbyte i Vallentuna") + ", och om fasadens färg under " + _L.format("malare-vallentuna.html", "målare i Vallentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönstren i en tegelvilla i Vallentuna",
  "steps": [
    ("Platsbesök", "Vi går runt villan och tittar på fogar, bleck och bågar på varje sida."),
    ("Prov på fogmassa", "Gamla fogar och kitt provas innan något tas bort."),
    ("Skriftligt kostnadsförslag", "Varje fönster för sig, så att de mest utsatta kan göras först."),
    ("Fog och bleck", "Fogen mellan karm och tegel görs om och skadade bleck byts."),
    ("Bågarna", "Sodatvätt, skrapning, grundning av kittfals, kittning och målning."),
    ("Genomgång", "Vi kontrollerar att bågarna sluter tätt och går lätt att öppna."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Vallentuna",
  "rot": [
    "Skatteverket godkänner rotavdrag i ett småhus för att reparera fönster, måla fönster och byta eller reparera fönsterbleck. Att mäta asbest ger inget avdrag, men sanering av asbest i samband med byggarbete gör det.",
    _ROT_SUM + " Du ska äga huset när arbetet utförs, och vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Vallentuna?",
  "price": [
    "Antalet fönster, hur mycket fog och bleck som behöver göras om, om fogmassan måste saneras och hur många bågar som bara behöver bättras påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför kommer det in vatten under fönstret i en tegelvilla?",
     "Boverket skriver att gamla fönstertätningar ofta släpper igenom vatten under fönstren, särskilt i lägen med slagregn. Fogen mellan karm och vägg och blecket behöver ses över."),
    ("Kan fogmassan runt fönstren i en villa från 1960-talet innehålla PCB?",
     "Det kan den. Boverket råder att undersöka om gamla fogmassor innehåller till exempel PCB eller asbest innan de tas bort, eftersom de då är saneringspliktiga."),
    ("Behöver fönstren på norrsidan målas lika ofta som på södersidan?",
     "Nej, enligt Riksantikvarieämbetet behöver söderfasader målas om oftare än norrfasader. Ofta räcker det att bättra de partier som är nedslitna."),
    ("När är det bättre att byta än att renovera treglasfönster från 1970-talet?",
     "När glaskassetten har förlorat sin funktion och monteringen i instickskarmar ger stora energiförluster, enligt Boverket. Det är vanligt för treglasfönster från sjuttiotalet."),
    ("Vad säger planen för Karby om villornas tegel?",
     "Den fördjupade översiktsplanen för Karby och Brottby pekar ut teglet som områdets dominerande material och beskriver 1960-talets tegelvillor som typiska för sin tid."),
  ],
  "sources": [_VAL_KB, _VAL_FAS, _BV_F, _BV_ASB, _RAA_M, _RAA_F, _SKV, _SKV2],
  "cta": ("Drar det eller läcker det vid fönstren?", "Boka ett gratis platsbesök, så går vi igenom fogar, bleck och bågar och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Tegelvilla från 1960-talet i funktionalistisk stil med vita fönster bland höga tallar",
     "single-storey 1960s Swedish brick villa in functionalist style with red-brown brick facade, white painted wooden windows, low pitched roof, set back from a quiet residential street among tall old pine trees on a gently sloping plot, late summer afternoon" + _IMG_END),
    ("Fönster i tegelvägg med ny fog mellan karm och mur och nytt fönsterbleck",
     "close-up of a white painted wooden window frame set in a red-brown brick wall, fresh sealant joint between frame and brickwork and a new grey metal window sill flashing below, clean brick reveal, overcast daylight" + _IMG_END),
    ("Fönsterbågar som skrapas på bockar utomhus intill en tegelvilla",
     "two white painted wooden window sashes resting on sawhorses outdoors next to a brick villa, one partly scraped with paint flakes on a drop cloth, a bucket with a soft brush beside it, pine trees in the background, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VASASTAN
"fonsterrenovering-vasastan.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Vasastan", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering i Vasastan – jugendhusen i Birkastaden",
  "description": "Fönsterrenovering i Vasastan: Birkastadens hus från 1902–12, jugendtidens fönster med spröjsad överdel, gathus och gårdshus, lov och avdrag.",
  "h1": "Fönsterrenovering i Vasastan",
  "lead": "Birkastaden byggdes på kort tid i början av 1900-talet, och enligt Stadsmuseets inventering hade fasaderna i stort sett kvar sin ursprungliga utformning. Geal Entreprenad AB renoverar fönster i Vasastan – i lägenheter och åt föreningar – och utgår från hur fönstren i just det huset en gång utformades.",
  "card": "Fönster i Birkastadens jugendhus.",
  "sections": [
    {"id": "birkastaden-vasastan", "anchor": "Birkastaden",
     "h2": "148 fastigheter på tio år",
     "paras": [
       "Stockholms stadsmuseum inventerade Birkastaden, Röda Bergen och Rörstrand 1973. Gatorna i Birkastaden lades in på stadsplanen för Norrmalm 1879 och på regleringsplanen 1886, och större delen av området bebyggdes 1902–12. Arkitekten A J Höög, genom firmorna Dorph & Höög och från 1910 Höög & Morssing, medverkade till 59 av områdets 148 fastigheter, ungefär 40 procent, och det är en förklaring till det enhetliga intrycket. Tre bostadshus revs under 1960-talet och ersattes med nya.",
       "Inventeringen konstaterar att fastigheterna hade genomgått få förändringar sedan de byggdes. Många fasader hade putsats om och därmed förenklats, men i stort sett hade de kvar sin ursprungliga utformning. Där puts och dekor har förenklats kan fönstren vara en av de delar som fortfarande visar hur huset var tänkt. Höög & Morssings fyra hus i kvarteret Skålen, Karlbergsvägen 78–84, är nationalromantiska med tegelklädda fasader, gavlar, burspråk och smårutiga fönster i fasadlivet, medan 1920-talshusen i kvarteret Gjutaren mot S:t Eriksgatan har slammade putsfasader i klassicistisk anda.",
     ],
     "aside": {"title": "Birkastaden i inventeringen", "items": [
       "Bebyggd 1902–12", "148 fastigheter", "59 hus med Höög som arkitekt", "Nationalromantik i kv Skålen"]}},
    {"id": "jugend-vasastan", "h2": "Jugendfönstret: smalt, kopplat och spröjsat upptill",
     "paras": [
       "Riksantikvarieämbetets skrift om fönster beskriver ett typiskt jugendfönster från sekelskiftets Stockholm. Det är mindre och relativt smalt jämfört med 1880-talets höga fönster, överdelen är spröjsad men nu främst i dekorativt syfte, och bågarna är kopplade och inåtgående. Mittposten är borta, och bågarna låses med spanjolettbeslag. Skriften visar också att spröjsarna hade försvunnit mot slutet av 1800-talet, när glasformaten blev större, och kom tillbaka kring sekelskiftet.",
       "Stockholms stad räknar bland annat en ändrad indelning, som att lägga till spröjs eller ta bort en mittpost, och ett byte av upphängning som ändringar av fönster, och om sådana ändringar kräver bygglov beror på byggnaden. En renovering som behåller den dekorativa överdelen, de kopplade inåtgående bågarna och spanjoletten ändrar inget av detta. I överdelen finns däremot många små kittfalsar, och RAÄ påpekar att spröjsar skadas på samma sätt som bågens nederstycke – angreppen är ofta små men kan vara allvarliga eftersom spröjsarna är så klena.",
     ],
     "aside": None},
    {"id": "gardshus-vasastan", "h2": "Gathus mot gatan, gårdshus mot berget",
     "paras": [
       "Inventeringen beskriver att Birkastadens fastigheter oftast har breda gathus med flyglar och likaledes breda gårdshus, och att de så kallade T-husen med en gårdsflygel mitt på huskroppen är vanliga. Gathusen rymmer större lägenheter om två till fyra rum och kök, medan gårdshusen har mindre lägenheter med enklare snickerier. Många lägenheter i gårdshusen är mycket mörka, särskilt i kvarteren Volontären och Ugnen som ligger mot norr och vetter mot höga bergväggar och murar.",
       "Fönstren på en och samma fastighet kan alltså sitta i helt olika lägen: mot en solig gata eller mot en skuggig gård. Vid besiktningen bedömer vi gatufasadens och gårdsfasadens fönster var för sig och noterar skicket på bottenstycken, kitt och färg per fönster. Till en förening kan kostnadsförslaget delas upp på samma sätt, så att de mest nedslitna fönstren kan prioriteras.",
     ],
     "aside": {"title": "Vi noterar per fönster", "items": [
       "Spanjolett och kopplingsbeslag", "Kitt i den spröjsade överdelen", "Bottenstycken i båge och karm", "Färg på ytterbågens insida"]}},
    {"id": "lov-vasastan", "h2": "Stadsmuseets karta, stadgarna och avdraget",
     "paras": [
       "Stadsmuseets klassificeringskarta visar om en byggnad ligger inom ett riksintresse för kulturmiljövården eller är markerad med blått eller grönt. I så fall behöver du enligt Stockholms stad söka bygglov för åtgärder som annars kan vara bygglovsbefriade. Kartan ger en första indikation, men det finns byggnader som museet ännu inte har inventerat. I översiktsplanens beskrivning av riksintresset ingår den klassiska stenstaden med bebyggelse från 1870–1930, med utbredning på bland annat Norrmalm.",
       "Bor du i en bostadsrätt säger bostadsrättslagen att du ska hålla lägenheten i gott skick om inte stadgarna bestämmer något annat. Skatteverket ger då rotavdrag bara för arbete på insidan av fönstren, som att måla insidan, byta glas i den inre bågen eller montera tätningslist, inte för utsidan eller arbete mellan bågarna. Om dörrar, foder och målning inomhus kan du läsa under " + _L.format("malare-vasastan.html", "målare i Vasastan") + ", och om nya fönster under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönster i ett hus i Birkastaden",
  "steps": [
    ("Fönster för fönster", "Vi öppnar varje båge och kontrollerar spanjolett, kopplingsbeslag och kitt."),
    ("Karta och stadgar", "Vi tittar på Stadsmuseets karta och vilka delar stadgarna lägger på dig."),
    ("Skriftligt kostnadsförslag", "Gatufasad och gårdsfasad, insida och utsida redovisas var för sig."),
    ("Lagning", "Skadade spröjsar och bottenstycken lagas med virke av samma kvalitet."),
    ("Kitt och målning", "Linoljekitt i falsarna och tunna strykningar, även på ytterbågens insida."),
    ("Genomgång", "Vi kontrollerar att bågarna går lätt och sluter innan vi lämnar."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering i Vasastan",
  "rot": [
    "Skatteverket godkänner i en bostadsrätt bara arbete innanför lägenhetens tak, väggar och golv som du ansvarar för enligt stadgarna. För fönster betyder det insidan: målning, glas i den inre bågen, tätningslist, innerfönster och fönsterfoder. Äger du ett småhus gäller i stället reparation och målning av hela fönstret.",
    _ROT_SUM + " Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Vasastan?",
  "price": [
    "Antalet fönster, hur många som har spröjsad överdel, om skadorna sitter i gathusets eller gårdshusets fönster och om bara insidan eller hela fönstret ska renoveras påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur ser ett typiskt jugendfönster i Stockholm ut?",
     "Enligt Riksantikvarieämbetet är det relativt smalt, har en spröjsad överdel i dekorativt syfte och kopplade inåtgående bågar som låses med spanjolett. Mittposten saknas."),
    ("Vem ritade husen i Birkastaden?",
     "Enligt Stadsmuseets inventering medverkade arkitekt A J Höög, genom Dorph & Höög och senare Höög & Morssing, till 59 av områdets 148 fastigheter."),
    ("Räknas det som en ändring av fönstret att ta bort en mittpost?",
     "Ja. Stockholms stad nämner ändrad indelning, till exempel att lägga till spröjs eller ta bort en mittpost, som en ändring av fönster. Om den kräver bygglov beror på byggnaden."),
    ("Varför är lägenheterna i Birkastadens gårdshus så mörka?",
     "Inventeringen pekar på kvarteren Volontären och Ugnen, där gårdshusen ligger mot norr och vetter mot höga bergväggar och murar."),
    ("Ger renovering av ytterbågen rotavdrag i en bostadsrätt?",
     "Nej. Skatteverket godkänner inte arbete på utsidan eller mellan bågarna i en bostadsrätt, bara på fönstrets insida."),
  ],
  "sources": [_SSM_BIRKA, _RAA_F, _RAA_M, _SB_F, _SB_KLASS, _OP_RIKS, _BRL, _SKV, _SKV2],
  "cta": ("Ska fönstren i huset ses över?", "Boka ett gratis platsbesök, så går vi igenom fönstren på gatusidan och gårdssidan och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Jugendhus i Vasastan med putsad fasad och smala fönster som är spröjsade upptill",
     "early 1900s Stockholm jugend apartment building facade, five storeys, light rendered facade with simple art nouveau ornament, rows of narrow tall wooden windows with small panes only in the upper part, white painted coupled sashes, quiet street with parked bicycles, soft morning light" + _IMG_END),
    ("Öppet kopplat inåtgående fönster med spröjsad överdel och spanjolett",
     "interior view of an open inward-opening coupled wooden window from around 1905 in a Stockholm apartment, white painted sashes, decorative small panes in the upper part, long brass espagnolette bolt, deep window niche, soft daylight" + _IMG_END),
    ("Smal innergård med gårdshus vars fönster vetter mot en hög bergvägg",
     "narrow inner courtyard of an early 1900s Stockholm apartment block, rendered courtyard building with rows of white painted wooden windows facing a high natural rock wall and a stone retaining wall, cobblestones, diffuse light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VÄRMDÖ
"fonsterrenovering-varmdo.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Värmdö", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering på Värmdö – glasverandorna i Barnvik",
  "description": "Fönsterrenovering på Värmdö: Barnviks by med glasverandor och äldre fönster, områdesbestämmelser med utökad lovplikt, kitt per ruta och fritidshus.",
  "h1": "Fönsterrenovering på Värmdö",
  "lead": "I Barnviks by i Djurö socken har många bostadshus kvar äldre paneler, glasverandor och fönster. Geal Entreprenad AB renoverar fönster på Värmdö och tar hand om verandornas glaspartier lika noga som husets egna fönster.",
  "card": "Glasverandor och äldre fönster.",
  "sections": [
    {"id": "barnvik-varmdo", "anchor": "Barnvik",
     "h2": "Barnviks by på höjdryggen",
     "paras": [
       "Kulturmiljöprogrammet Värmdö – Kulturhistoria i skärgårdsbygd, framtaget av kommunen och Stockholms läns museum, beskriver Barnviks by som placerad på en höjdrygg längs strandkanten, med den gamla landsvägen mellan byn och de södra odlingsmarkerna. Omkring sekelskiftet 1900 bestod byn av tre gårdar och ett flertal bostadslägenheter, och i dag finns ett tiotal bevarade äldre bostadshus, flera ekonomibyggnader och uthus samt enstaka lantarbetarlägenheter.",
       "Bebyggelsen har karaktär från sekelskiftet 1900, med sadeltak eller mansardtak av tegel, rödmålade träpaneler, i huvudsak vita foder och bevarade äldre detaljer. Mansardtak, liggtimmer och fältstensgrunder tyder enligt programmet på att flera hus uppfördes vid mitten av 1800-talet eller tidigare. Husen hade från början ett enkelt utseende men anpassades efter sekelskiftets ideal, och många har glasverandor. Programmet framhåller att bostadshusen, av vilka många fortfarande har en ursprunglig karaktär med äldre paneler, glasverandor och fönster, ger byn höga miljöskapande kvaliteter.",
     ],
     "aside": {"title": "Barnvik i programmet", "items": [
       "Ett tiotal äldre bostadshus", "Rödmålad panel, vita foder", "Många glasverandor", "Två sommarvillor kring 1900"]}},
    {"id": "veranda-varmdo", "h2": "Glasverandans rutor och bottenstycken",
     "paras": [
       "En glasveranda består till stor del av glasade partier, och varje ruta sitter i en egen kittfals. Riksantikvarieämbetets handbok om byggnadsmåleri skriver att det är särskilt viktigt att fönsterkittet är helt, så att fukt inte tränger in i träet och orsakar röta. Vid ommålning skrapas löst kitt bort, blottade kittfalsar grundas innan de kittas, och även ytterbågens insida ska strykas med utomhusfärg.",
       "Länsstyrelsernas blad om fönster beskriver att vattnet som rinner på fönstrets utsida gör den nedre delen särskilt utsatt, och att rötskadorna oftast kommer i bågens och karmens bottenstycken. På en veranda tittar vi därför också på bröstningen och bottenstyckena under glaspartierna. Rötskadat virke skarvas med nytt virke av god kvalitet, så att resten av partiet kan sitta kvar. Bladet påpekar att gamla fönster är tillverkade av mycket bra virke, att det därför lönar sig att underhålla dem och att även svårt skadade fönster kan repareras med gott resultat.",
     ],
     "aside": {"title": "Verandans utsatta delar", "items": [
       "Kittet runt varje ruta", "Bottenstycken under glaset", "Bröstningen", "Ytterbågens insida"]}},
    {"id": "bestammelser-varmdo", "h2": "Områdesbestämmelser med utökad lovplikt",
     "paras": [
       "Samhällsplaneringsnämnden har antagit områdesbestämmelser för Barnvik, och enligt programmet gäller därmed bland annat utökad lovplikt samt varsamhets- och skyddsbestämmelser. Värmdö kommun skriver att det i kommunen finns 14 riksintressen och omkring 55 utpekade kulturmiljöområden som alla räknas som särskilt värdefulla, och att fönster och dörrar hör till det man särskilt ska tänka på när något ändras i en kulturmiljö.",
       "Kommunen skriver också att underhåll av en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde kräver anmälan och startbesked. Om det gäller ditt hus tar vi med det i planeringen, och kommunantikvarien kan ge råd innan arbetet börjar. Programmets genomgång av plan- och bygglagen påpekar att en byggnad ska underhållas så att utformningen och de tekniska egenskaperna bevaras, och att en särskilt värdefull byggnad ska underhållas så att de särskilda värdena bevaras.",
     ],
     "aside": None},
    {"id": "fritidshus-varmdo", "h2": "Sommarvillor, fritidshus och nya fönster",
     "paras": [
       "Två välbevarade sommarvillor från tiden kring förra sekelskiftet ligger i anslutning till byn, och under 1900-talets andra hälft byggdes fritidshus och nya permanentbostäder intill den. Programmet beskriver villorna som exempel på hur äldre byars marker kom att bebyggas när skärgården blev ett eftertraktat semesterparadis.",
       "Den som bara bor i huset på somrarna kan ändå få rotavdrag: Skatteverket godkänner arbete i ett fritidshus du äger, men inte om någon annan bor där permanent. Ett renoverat fönster behåller husets utseende, medan ett nytt fönster i ett område med utökad lovplikt kan kräva lov – kommunen skriver att lovplikt gäller inom kulturhistoriskt värdefulla områden. Om Gustavsbergs fönster och lov för nya fönster kan du läsa under " + _L.format("fonsterbyte-varmdo.html", "fönsterbyte på Värmdö") + ", och om panel och färg under " + _L.format("fasadmalning-varmdo.html", "fasadmålning på Värmdö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönster och glasverandor i Barnvik",
  "steps": [
    ("Platsbesök", "Vi går igenom husets fönster och verandans glaspartier ruta för ruta."),
    ("Bestämmelserna", "Vi kontrollerar vad områdesbestämmelserna kräver och om anmälan behövs."),
    ("Skriftligt kostnadsförslag", "Huset och verandan redovisas var för sig."),
    ("Kitt och lagning", "Löst kitt tas bort, falsarna grundas och skadade bottenstycken skarvas."),
    ("Målning", "Bågarna målas i husets kulör, även ytterbågens insida."),
    ("Genomgång", "Vi går runt huset och verandan med dig när arbetet är klart."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering på Värmdö",
  "rot": [
    "Skatteverket räknar reparation och målning av fönster i ett småhus som rotarbete, och det gäller även ett fritidshus som du äger. Att glasa in balkonger och altaner finns också bland de godkända glasarbetena, medan glasarbete i företagets egna lokaler inte ger avdrag.",
    _ROT_SUM + " Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Värmdö?",
  "price": [
    "Antalet fönster och verandapartier, hur många rutor som behöver kittas om, hur mycket virke som ska skarvas och vad områdesbestämmelserna kräver påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad säger kulturmiljöprogrammet om husen i Barnviks by?",
     "Att många bostadshus fortfarande har en ursprunglig karaktär med äldre paneler, glasverandor och fönster, och att det ger byn höga miljöskapande kvaliteter."),
    ("Gäller utökad lovplikt i Barnvik?",
     "Ja. Områdesbestämmelser för Barnvik har antagits, och enligt kulturmiljöprogrammet gäller bland annat utökad lovplikt samt varsamhets- och skyddsbestämmelser."),
    ("Ska ytterbågens insida målas med inomhusfärg?",
     "Nej. Riksantikvarieämbetet påpekar att även ytterbågens insida bör strykas med utomhusfärg."),
    ("Behöver jag göra en anmälan för att underhålla ett skyddat hus på Värmdö?",
     "Värmdö kommun skriver att underhåll av en byggnad som är skyddad i detaljplan eller har särskilt bevarandevärde kräver anmälan och startbesked."),
    ("Ger renovering av glasverandan på ett fritidshus rotavdrag?",
     "Reparation av fönster i ett fritidshus du äger kan ge rotavdrag enligt Skatteverket. Det gäller inte om någon annan bor permanent i huset."),
  ],
  "sources": [_VD_KMP, _VD_KM, _VD_PBL, _RAA_M, _LST_F, _SKV, _SKV2],
  "cta": ("Behöver glasverandan eller fönstren ses över?", "Boka ett gratis platsbesök, så går vi igenom rutor, kitt och bottenstycken och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Rödmålat bostadshus med vita foder och en glasveranda med småspröjsade fönster i en skärgårdsby",
     "old red ochre painted wooden house from around 1900 in a Stockholm archipelago village on a ridge near the shore, white window casings, a glazed veranda with many small white painted window panes, mansard roof with red clay tiles, old fruit trees and a gravel road, summer morning" + _IMG_END),
    ("Glasverandans fönsterparti med nykittade rutor och vitmålade spröjsar",
     "close-up of an old glazed wooden veranda with many small panes, white painted muntins, fresh linseed putty around each pane, red painted boards below, soft daylight" + _IMG_END),
    ("Bottenstycke på ett verandaparti med nytt inskarvat virke före målning",
     "close-up of the bottom rail of an old veranda window section with a newly spliced piece of unpainted pine joined to white painted old wood, the window section resting on a workbench, no tools, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ ÖSTERMALM
"fonsterrenovering-ostermalm.html": {
  "kind": "district", "service": "fonsterrenovering", "ort": "Östermalm", "svc_label": "Fönsterrenovering",
  "title": "Fönsterrenovering på Östermalm – 1930-talshusen på Gärdet",
  "description": "Fönsterrenovering på Östermalm: funktionalismens fönster på Gärdet, en hel ruta per båge, äldre glas, limmade bågar och nationalstadsparken.",
  "h1": "Fönsterrenovering på Östermalm",
  "lead": "Gärdesstaden runt Tessinparken byggdes 1932–37 och beskrivs i stadens översiktsplan som en av Sveriges mest kända miljöer från funktionalismens genombrottstid. Geal Entreprenad AB renoverar fönster på Östermalm och tar hand om 1930-talets bågar så att glas, profiler och kulörer får sitta kvar.",
  "card": "Fönster och glas i Gärdets 1930-talshus.",
  "sections": [
    {"id": "gardet-ostermalm", "anchor": "Gärdet",
     "h2": "Gärdesstaden vid Tessinparken",
     "paras": [
       "Stadsmuseets guide Stockholms Spår berättar att Ladugårdsgärdet hade varit militärt övningsfält sedan 1600-talets mitt. Militären flyttade ut 1905, och en stadsplanetävling vanns 1929 av arkitekten Arvid Stille. Planen bygger på de funktionalistiska idealen med friliggande hus i parkliknande grönska, utan staket eller slutna gårdar. Utbyggnaden började 1932 vid Valhallavägen, husen kring Tessinparken var färdiga 1937 och punkthusen på Gärdeshöjden stod i stort sett klara 1940. Sture Frölén ritade flera av husen. På nedre Gärdet ligger gavlarna på rad utmed Tessinparken, och där skulle alla hus från början ha skiffertak. Balkongerna fick många olika former av räcken, och ytterportar av glas och stål växlar med ekportar.",
       "Översiktsplanen beskriver Gärdesstaden som en av Sveriges mest kända och helgjutna miljöer från funktionalismens genombrottstid, med stora arkitekturhistoriska och stadsbyggnadshistoriska kulturvärden. Bland de värdebärande karaktärsdragen nämns det omsorgsfulla utförandet av husens byggnadsdetaljer, som fönster, entrépartier och balkongräcken. Området skyddas av miljöbalkens bestämmelser om nationalstadspark, och Östermalms parkplan anger att Tessinparken ingår i nationalstadsparken sedan 1995.",
     ],
     "aside": {"title": "Gärdet i korthet", "items": [
       "Tävlingen vanns 1929", "Utbyggnad från 1932", "Tessinparkens hus klara 1937", "Del av nationalstadsparken"]}},
    {"id": "glas-ostermalm", "h2": "En hel ruta i varje båge",
     "paras": [
       "Riksantikvarieämbetets skrift om fönster beskriver hur de spröjsade bågarna försvann igen på 1930-talet. Med funktionalismen fick glasformatet styra, och bågen försågs med en enda hel glasruta. Fönstren blev också lägre, eftersom de anpassades till de nya, lägre rumshöjderna.",
       "Glaset i de här rutorna kan vara äldre än man tror. Enligt skriften användes cylindermetoden, där glaset blåstes som en cylinder och planades ut, ända fram till 1933 i Sverige, medan maskindraget glas tillverkades med Fourcaultmetoden från 1913. Landets största fönsterglasbruk under 1900-talets första decennier, Glava i Värmland, blåste glaset för hand fram till 1927. I dag tillverkas bara floatglas. Det blåsta eller maskindragna glaset har en levande, ojämn yta som floatglaset saknar, och vid glasning av äldre fönster i kulturhistoriskt värdefulla hus bör gammalt glas användas så långt det går. Vi tar därför ur och sparar hela rutor när en båge renoveras, och en sprucken ruta kan ersättas med tillvarataget äldre glas.",
     ],
     "aside": {"title": "Glas enligt RAÄ", "items": [
       "Cylinderblåst glas till 1933", "Maskindraget glas från 1913", "Bara floatglas i dag", "Äldre glas kan återanvändas"]}},
    {"id": "lim-ostermalm", "h2": "Limmade bågar lagas med snedskarv",
     "paras": [
       "Äldre fönster sattes ihop med tappar och träplugg utan lim och kan därför tas isär och lagas, skriver Länsstyrelsernas blad om fönster. Riksantikvarieämbetet påpekar att limmet introducerades i fönsterkonstruktionerna just på 1930-talet: en lärobok från 1931 anger att alla sammansättningar i fönsterbågar ska limmas. En båge från Gärdets första år kan därför vara limmad, och då går den inte att slå isär på samma sätt som ett sekelskiftesfönster.",
       "Skadat virke byts i stället där det sitter. RAÄ beskriver hur bågens nedre del kan halvsulas, så att bara de yttre delarna ersätts, och hur nytt virke snedskarvas för att få en så lång anliggningsyta som möjligt och limmas med vattenfast lim. Profilen fräses med originalet som förebild, och lagningsvirket bör ha samma kvalitet och årsringarna orienterade på samma sätt som det gamla, så att det inte uppstår spänningar.",
     ],
     "aside": None},
    {"id": "lov-ostermalm", "h2": "Nationalstadsparken och bostadsrättens insida",
     "paras": [
       "Stockholms stad räknar nationalstadsparken till riksintressena för kulturmiljövården på Stadsmuseets karta. Ligger en byggnad där behöver du söka bygglov för åtgärder som annars kan vara bygglovsbefriade, och att byta material eller kulör på fönster, ändra profileringen på karmar och bågar eller byta upphängning räknas som ändringar av fönster. En renovering som behåller glas, profiler och kulör hör inte till den listan.",
       "I en bostadsrätt avgör föreningens stadgar vilka delar av fönstret som är ditt ansvar, och Skatteverket ger rotavdrag för arbete på insidan men inte för utsidan eller mellan bågarna. Boverkets energiguide beskriver hur den inre rutan kan bytas till eller kompletteras med energiglas, och den som har kvar äldre munblåst eller valsat glas kan kanske använda det som ytterrutor. Om måleri i stenstadens våningar kan du läsa under " + _L.format("malare-ostermalm.html", "målare på Östermalm") + ", och om nya fönster under " + _L.format("fonsterbyte.html", "fönsterbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi fönster i 1930-talshusen på Gärdet",
  "steps": [
    ("Besiktning", "Vi går igenom varje fönster och noterar glas, kitt, färg och om bågarna är limmade."),
    ("Karta och stadgar", "Vi kontrollerar Stadsmuseets karta och vilka delar stadgarna lägger på dig."),
    ("Skriftligt kostnadsförslag", "Insida och utsida, lagning och glas står var för sig."),
    ("Glaset tas till vara", "Hela rutor tas ur och sparas, spruckna ersätts helst med äldre glas."),
    ("Lagning", "Skadat virke halvsulas eller snedskarvas och limmas med vattenfast lim."),
    ("Kitt och målning", "Kittfalsar grundas, rutorna kittas och bågarna målas i tunna lager."),
  ],
  "rot_h2": "ROT-avdrag för fönsterrenovering på Östermalm",
  "rot": [
    "I en bostadsrätt ger Skatteverket avdrag för arbete inne i lägenheten som du ansvarar för enligt stadgarna. På fönstren omfattar det glasbyte i den inre bågen, tätningslist, innerfönster, fönsterfoder och målning av insidan, men inte byte av gångjärn.",
    _ROT_SUM + " Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på Östermalm?",
  "price": [
    "Antalet fönster, hur många rutor som ska tas ur och sättas tillbaka, om virke måste snedskarvas i limmade bågar och om både insida och utsida ingår påverkar mest. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("När byggdes husen vid Tessinparken på Gärdet?",
     "Utbyggnaden började 1932 vid Valhallavägen och husen kring Tessinparken var färdiga 1937, enligt Stadsmuseets Stockholms Spår."),
    ("Varför har 1930-talets fönster inga spröjsar?",
     "Med funktionalismen fick glasformatet styra, och bågen fick en enda hel ruta, skriver Riksantikvarieämbetet. Fönstren blev också lägre med de nya rumshöjderna."),
    ("Kan en limmad fönsterbåge från 1930-talet lagas?",
     "Ja. Skadat virke kan halvsulas eller snedskarvas och limmas med vattenfast lim, med profilen fräst efter originalet."),
    ("Hur känner man igen cylinderblåst fönsterglas?",
     "Enligt Riksantikvarieämbetet på sina parallella skiftningar och ojämnheter. Glaset är dessutom mycket tunt och relativt klart."),
    ("Krävs bygglov för att renovera fönster i nationalstadsparken?",
     "Byte av kulör, material eller profiler kan kräva lov där, eftersom nationalstadsparken räknas som riksintresse. Underhåll som behåller fönstrets utseende finns inte bland stadens exempel på ändringar, om inte detaljplanen har utökad lovplikt."),
  ],
  "sources": [_SSM_GARDET, _OP_RIKS, _PP_OST, _RAA_F, _LST_F, _SB_F, _SB_KLASS, _BV_F, _SKV, _SKV2],
  "cta": ("Ska 1930-talsfönstren renoveras?", "Boka ett gratis platsbesök, så går vi igenom glas, bågar och kitt och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Funktionalistiska lamellhus i ljus puts med regelbundna fönsterrader i ett grönt parkstråk",
     "parallel 1930s functionalist four-storey apartment slab blocks in Stockholm with flat roofs, plain light rendered facades and regular rows of white painted wooden windows with single large panes, set in a green park with mature trees and lawns between the buildings, completely empty paths without pedestrians, early summer morning" + _IMG_END),
    ("Fönsterbåge med en hel glasruta av äldre glas som just har kittats",
     "close-up of a white painted 1930s wooden window sash with one large single pane of old slightly wavy drawn glass, fresh linseed putty along the rebate, a putty knife resting on the sash on a workbench, soft daylight" + _IMG_END),
    ("Nedre hörnet av en fönsterbåge med snedskarvat nytt virke i limtvingar",
     "lower corner of an old white painted wooden window sash on a workbench with a newly scarf-jointed piece of light pine glued in, clamps holding the joint, wood shavings around, workshop light" + _IMG_END),
  ],
},

}
