# -*- coding: utf-8 -*-
"""
Ortsidor för resten av Storstockholm (2026-10-08). Importeras av tools/generate.py
och följer exakt samma mönster som LOC/LOC_EXTRA där (intro, paras, items, faq +
secs/faq i EXTRA). Extra nyckel "why" = egen text i "Varför välja oss"-sektionen
(den gamla mallen säger "precis intill Sundbyberg … snabbt", som inte stämmer för
t.ex. Haninge). Regler: unik lokal text per ort, inga priser, inga påhittade
siffror, inget kontor i området (bas = Bromma/Mariehäll). Bygglov: Stockholms
stad för stadsdelar, respektive kommun för övriga.
"""

# Prioritet: nära basen (västerort) först.
AREAS_NEW = ["Hässelby", "Vällingby", "Kista", "Ekerö", "Hägersten", "Älvsjö",
             "Enskede", "Farsta", "Skärholmen", "Huddinge", "Tyresö", "Haninge",
             "Värmdö", "Upplands Väsby", "Vallentuna", "Österåker", "Botkyrka"]

# Stadsdelar i Stockholms stad (för grupperingen på omraden.html).
STOCKHOLM_STAD = ["Bromma", "Spånga", "Hässelby", "Vällingby", "Kista",
                  "Hägersten", "Älvsjö", "Enskede", "Farsta", "Skärholmen"]

NEIGHBORS_NEW = {
  "Hässelby":   ["Vällingby", "Spånga", "Ekerö", "Järfälla"],
  "Vällingby":  ["Hässelby", "Bromma", "Spånga", "Ekerö"],
  "Kista":      ["Spånga", "Sollentuna", "Järfälla", "Sundbyberg"],
  "Ekerö":      ["Bromma", "Hässelby", "Vällingby"],
  "Hägersten":  ["Älvsjö", "Skärholmen", "Enskede", "Bromma"],
  "Älvsjö":     ["Hägersten", "Enskede", "Huddinge", "Farsta"],
  "Enskede":    ["Farsta", "Älvsjö", "Hägersten", "Nacka"],
  "Farsta":     ["Enskede", "Älvsjö", "Huddinge", "Tyresö", "Haninge"],
  "Skärholmen": ["Hägersten", "Huddinge", "Botkyrka", "Älvsjö"],
  "Huddinge":   ["Älvsjö", "Skärholmen", "Botkyrka", "Farsta", "Haninge"],
  "Tyresö":     ["Haninge", "Farsta", "Nacka", "Värmdö"],
  "Haninge":    ["Tyresö", "Huddinge", "Farsta"],
  "Värmdö":     ["Nacka", "Tyresö", "Lidingö"],
  "Upplands Väsby": ["Sollentuna", "Vallentuna", "Täby", "Järfälla"],
  "Vallentuna": ["Täby", "Upplands Väsby", "Österåker", "Danderyd"],
  "Österåker":  ["Vallentuna", "Täby", "Danderyd", "Lidingö"],
  "Botkyrka":   ["Huddinge", "Skärholmen", "Hägersten"],
}
# Befintliga orter får länkar till nya grannar (inlänkar till de nya sidorna).
NEIGHBORS_ADD = {
  "Bromma":     ["Vällingby", "Ekerö"],
  "Spånga":     ["Hässelby", "Kista"],
  "Sundbyberg": ["Kista"],
  "Sollentuna": ["Kista", "Upplands Väsby"],
  "Järfälla":   ["Hässelby", "Upplands Väsby"],
  "Täby":       ["Vallentuna", "Österåker"],
  "Danderyd":   ["Österåker"],
  "Nacka":      ["Värmdö", "Tyresö"],
  "Lidingö":    ["Värmdö"],
}

LOC_NEW = {
 "Hässelby": {
   "intro": "Hässelby längst ut i västerort är ett av Stockholms största villaområden. Vi är takläggare i Hässelby för egnahem, villor och radhus i bland annat Hässelby villastad, Hässelby gård och Hässelby strand.",
   "paras": [
     "Hässelby villastad växte fram som egnahemsområde under första halvan av 1900-talet, och många hus är byggda mellan 1920- och 1950-talet. Typiskt är små och medelstora trä- eller putsade hus med branta sadeltak, ofta med lertegel eller betongpannor och en murad skorsten mitt på taket.",
     "Hässelby strand och Hässelby gård har mer efterkrigsbebyggelse – flerbostadshus och radhus från 1950- och 60-talet – medan villorna närmast Mälaren ligger mer vindutsatt. Här finns både låglutande radhustak med papp och klassiska tegeltak som lagts om en eller två gånger.",
     "Många egnahem har byggts till eller fått inredd vind genom åren. Då behöver taket bedömas som en helhet, inte bara den ursprungliga delen – det är ofta i skarven mellan gammalt och nytt som problemen börjar.",
   ],
   "items": ["Egnahem från 1920–50-talet i villastaden.", "Om- och tillbyggda tak bedöms som helhet.", "Tegel, betongpannor och radhustak med papp."],
   "why": "Hässelby ligger i västerort, samma del av Stockholm som vår bas i Mariehäll i Bromma. Det gör det enkelt att boka besiktning och följa projektet på plats.",
   "faq": [
     ("Har ni erfarenhet av egnahemmen i Hässelby villastad?", "Ja. Små hus med branta tak, murade skorstenar och tillbyggda kupor är vanliga här. Vi lägger om eller byter taket och anpassar detaljerna efter husets ursprungliga stil."),
     ("Vilka delar av Hässelby arbetar ni i?", "Hela Hässelby – villastaden, Hässelby gård och Hässelby strand."),
     ("Mitt hus har byggts till – kan den nya takdelen anslutas till den gamla?", "Ja. Anslutningen mellan gammal och ny takdel är en vanlig läckagepunkt. Vid takbyte gör vi om den så att båda delarna får samma underlag och täta plåtdetaljer."),
   ]},
 "Vällingby": {
   "intro": "Vällingby är 1950-talets ABC-stad i västerort, med radhus, kedjehus och lamellhus kring Vällingby centrum. Vi är takläggare i Vällingby för villor, radhus och samfälligheter i bland annat Råcksta, Grimsta, Kälvesta, Nälsta och Vinsta.",
   "paras": [
     "Vällingby planerades som en ABC-stad – arbete, bostad, centrum – och centrum invigdes 1954. Närmast centrum byggdes lamellhus och punkthus, och längre ut radhus, kedjehus och villor. Mycket av bebyggelsen är från 1950- och 60-talet och har nu passerat en eller två takgenerationer.",
     "Radhusen har ofta låga sadeltak eller pulpettak med betongpannor, papp eller plåt. I Kälvesta och Nälsta finns också villor och kedjehus från 1960- och 70-talet, medan andra delar har inslag av äldre småhus.",
     "Många radhus förvaltas av samfälligheter eller bostadsrättsföreningar, där taket är en gemensam fråga. Vi lämnar underlag som styrelsen kan fatta beslut på och planerar arbetet länga för länga.",
   ],
   "items": ["Radhus och kedjehus från 1950–70-talet.", "Underlag för samfälligheter och BRF.", "Betongpannor, papp och plåt på låga lutningar."],
   "why": "Vällingby ligger bara några kilometer från vår bas i Mariehäll, Bromma. Vi kan därför komma ut på besiktning med kort varsel och följa arbetet på plats.",
   "faq": [
     ("Kan ni lämna offert till vår samfällighet i Vällingby?", "Ja. Vi besiktar längorna, beskriver åtgärderna och lämnar ett kostnadsförslag som styrelsen kan ta ställning till."),
     ("Vilka delar av Vällingby arbetar ni i?", "Hela Vällingby med bland annat Råcksta, Grimsta, Kälvesta, Nälsta och Vinsta."),
     ("Mitt radhustak har låg lutning – vilket material passar?", "På låga lutningar fungerar falsad plåt eller papp bäst. Betongpannor kräver en viss minsta lutning enligt tillverkarens anvisningar. Vi bedömer vad som passar ditt hus."),
   ]},
 "Kista": {
   "intro": "Kista i norra Stockholm är mest känt för sin IT-stad, men här finns också radhus, småhus och bostadsrättsföreningar i Kista, Husby och Akalla. Vi är takläggare i Kista för radhus, föreningar och mindre fastigheter.",
   "paras": [
     "Kista, Husby och Akalla byggdes till största delen under 1970-talet på mark som tidigare hörde till Järvafältet. Bebyggelsen är i huvudsak flerbostadshus, men här finns också radhus och mindre grupper av småhus från samma tid.",
     "Taken från 1970-talet är ofta låglutande med papp eller plåt, och många har redan fått ett nytt tätskikt. Med låg lutning blir skarvar, takbrunnar och plåtavtäckningar avgörande för att taket ska hålla tätt.",
     "Nära Kista ligger Helenelund i Sollentuna och villaområdena i Spånga, som vi också arbetar i. Har ni flera byggnader i en förening tar vi gärna ett samlat grepp om alla tak.",
   ],
   "items": ["Radhus och föreningar från 1970-talet.", "Låglutande tak med papp och plåt.", "Besiktning och underlag för styrelser."],
   "why": "Vi utgår från Bromma (Mariehäll) och når Kista via Spånga på kort tid. Det gör det enkelt att komma ut på besiktning och följa projektet.",
   "faq": [
     ("Tar ni takuppdrag åt bostadsrättsföreningar i Kista?", "Ja, vi besiktar och lämnar kostnadsförslag på takbyte, omläggning och plåtarbeten för föreningar och samfälligheter."),
     ("Vilka delar arbetar ni i?", "Kista, Husby och Akalla, och vidare mot Helenelund och Spånga."),
     ("Mitt papptak läcker vid en takbrunn – vad gör ni?", "Vi lokaliserar läckan, byter skadat tätskikt och ser över brunn och anslutningar. Är tätskiktet uttjänt över hela ytan kan ett nytt tak vara bättre."),
   ]},
 "Ekerö": {
   "intro": "Ekerö kommun består av öar i Mälaren – Ekerö, Färingsö, Munsö, Adelsö med flera. Vi är takläggare på Ekerö för villor, gårdar och fritidshus som blivit permanentboenden, i bland annat Ekerö centrum, Stenhamra, Träkvista och Skå.",
   "paras": [
     "Bebyggelsen på Ekerö är blandad: villaområden från 1960-talet och framåt kring Ekerö centrum, Träkvista och Stenhamra, äldre gårdar och torp på Färingsö och Munsö, och många tidigare fritidshus som byggts om till permanentboende.",
     "Mälaren är sötvatten, så saltet som sliter på plåten ute i skärgården är inget stort problem här. Däremot ger de öppna vattenytorna vind som tar i takfötter, nockar och plåtdetaljer, och strandnära hus får mer fukt och påväxt på taken.",
     "Till Adelsö går bilfärjan, och flera öar nås via smala vägar. Vi planerar materialleveranser och etablering i förväg så att vi kan arbeta effektivt även längre ut.",
   ],
   "items": ["Villor, gårdar och permanentade fritidshus.", "Vindutsatta lägen vid Mälaren.", "Granne till Bromma via Nockebybron."],
   "why": "Ekerö är vår närmaste granne västerut – från Mariehäll i Bromma når vi Ekerö via Nockebybron. Det ger korta restider för besiktning och uppföljning.",
   "faq": [
     ("Arbetar ni även på Färingsö, Munsö och Adelsö?", "Ja, vi tar uppdrag i hela Ekerö kommun. För öar med färja planerar vi transporter och leveranser i förväg."),
     ("Vårt fritidshus har blivit permanentbostad – räcker det gamla taket?", "Fritidshus byggdes ofta med enklare tak och tunnare underlag. Vid permanentning är det klokt att besikta taket, särskilt ventilation, underlag och isolering på vinden."),
     ("Påverkar Mälaren taket?", "Sötvattnet ger inte saltkorrosion, men vind och fukt från vattnet sliter på plåtdetaljer och ger mer påväxt. Vi anpassar infästning och underhåll efter läget."),
   ]},
 "Hägersten": {
   "intro": "Hägersten i sydvästra Stockholm har villastäder vid Mälaren och radhusområden från 1930–60-talet. Vi är takläggare i Hägersten för villor och radhus i bland annat Mälarhöjden, Västertorp, Hägerstensåsen och Fruängen.",
   "paras": [
     "Mälarhöjden växte fram som villastad i början av 1900-talet på höjderna ner mot Mälaren. Här finns trävillor och putsade villor med branta tegeltak, valmade tak och kupor – ofta i kuperad terräng med stora ekar och tallar.",
     "Hägerstensåsen och Västertorp har mer bebyggelse från 1930–50-talet, med radhus och mindre villor med tegel- eller betongtak. Fruängen byggdes på 1960-talet och har inslag av radhus och kedjehus med låglutande tak.",
     "Epokerna gör att åtgärderna skiljer sig mycket inom samma stadsdel – från varsam omläggning av ett hundraårigt tegeltak till nytt tätskikt på ett 60-talsradhus. Vi börjar alltid med en besiktning.",
   ],
   "items": ["Villor i Mälarhöjden med branta tegeltak.", "Radhus i Hägerstensåsen, Västertorp och Fruängen.", "Varsam omläggning eller komplett takbyte."],
   "why": "Vi utgår från Bromma (Mariehäll) och når Hägersten via Essingeleden. Vi kommer ut på besiktning och håller tät kontakt under projektet.",
   "faq": [
     ("Kan ni lägga om ett gammalt tegeltak i Mälarhöjden?", "Ja. Är teglet i gott skick kan vi återanvända det och byta läkt och underlag – det bevarar husets karaktär."),
     ("Vilka delar av Hägersten arbetar ni i?", "Bland annat Mälarhöjden, Hägerstensåsen, Västertorp, Fruängen och Hägersten."),
     ("Vi bor i radhus i Fruängen – byter ni enskilda tak?", "Ja, och vi hjälper också föreningar med hela längor."),
   ]},
 "Älvsjö": {
   "intro": "Älvsjö i söderort har några av Stockholms mest omfattande småhusområden. Vi är takläggare i Älvsjö för villor i bland annat Långbro, Herrängen, Solberga, Liseberg och Örby.",
   "paras": [
     "Villabebyggelsen i Älvsjö växte fram längs järnvägen i början av 1900-talet. Långbro och Herrängen har många hus från 1910–40-talet – trävillor och putsade villor med branta tak, verandor och ofta originalteglet kvar.",
     "Solberga och Örby har fler egnahem och småhus från 1930–50-talet, ofta med enklare sadeltak i betongpannor eller tegel. Liseberg har både äldre villor och radhus.",
     "De stora trädgårdarna i Långbro och Herrängen ger skugga och löv, och många hus har byggts ut med kupor och vindsinredning. Vi bedömer hela taket – även de delar som tillkommit senare.",
   ],
   "items": ["Villor från 1910–50-talet i Långbro och Herrängen.", "Omläggning med återanvänt originaltegel.", "Kupor, verandor och utbyggda vindar."],
   "why": "Vi utgår från Bromma (Mariehäll) och når Älvsjö via E4:an söderut. Vi bokar in besiktning och följer projektet på plats.",
   "faq": [
     ("Arbetar ni i Långbro och Herrängen?", "Ja, och i hela Älvsjö – även Solberga, Liseberg och Örby."),
     ("Mitt hus har kvar originalteglet – går det att återanvända?", "Ofta ja. Hela pannor kan läggas tillbaka på nytt underlag och ny läkt, och trasiga ersätts med likvärdiga."),
     ("Byter ni tak på verandor och burspråk?", "Ja, små takytor med plåt eller papp ingår ofta när huvudtaket läggs om."),
   ]},
 "Enskede": {
   "intro": "Enskede söder om Södermalm rymmer Gamla Enskede, en av Stockholms första trädgårdsstäder. Vi är takläggare i Enskede för villor, parhus och radhus i bland annat Gamla Enskede, Enskededalen, Enskede gård, Stureby och Svedmyra.",
   "paras": [
     "Gamla Enskede började byggas strax efter 1900 som trädgårdsstad, med små villor och parhus i trädgårdar längs svängda gator. Många hus har branta tak med lertegel, ofta brutna tak eller sadeltak med kupor.",
     "Enskede gård har mycket bebyggelse från 1930–40-talet med radhus och lamellhus, medan Enskededalen, Stureby och Svedmyra har villor och småhus från 1920-talet och framåt.",
     "Trädgårdsstadens karaktär bygger på enhetlighet: liknande takmaterial, kulörer och detaljer hus efter hus. Vid ett takbyte här är målet att taket ser ut som förut men blir tätt för lång tid.",
   ],
   "items": ["Trädgårdsstaden Gamla Enskede.", "Parhus, radhus och 1930–40-talsvillor.", "Takbyte som bevarar områdets uttryck."],
   "why": "Vi utgår från Bromma (Mariehäll) och når Enskede via Essingeleden och Södra länken. Vi kommer ut på besiktning och följer arbetet på plats.",
   "faq": [
     ("Kan ni byta tak på ett parhus där bara vår halva ska göras?", "Ja. Vi gör en tät anslutning mot grannhalvan och väljer pannor som matchar. Det kan ändå vara klokt att prata med grannen om att göra båda samtidigt."),
     ("Vilka delar av Enskede arbetar ni i?", "Gamla Enskede, Enskededalen, Enskede gård, Stureby, Svedmyra och närliggande områden."),
     ("Går det att få tegel som matchar i Gamla Enskede?", "Ofta går det att återanvända befintligt tegel och komplettera med likvärdiga pannor. Vi bedömer det vid besiktningen."),
   ]},
 "Farsta": {
   "intro": "Farsta i söderort är mer än ett centrum – här finns villor och radhus i bland annat Sköndal, Fagersjö, Larsboda, Farsta strand, Tallkrogen, Gubbängen och Hökarängen. Vi är takläggare i Farsta för villor, radhus och samfälligheter.",
   "paras": [
     "Farsta centrum invigdes 1960 som ett av söderorts ABC-centrum. Runt det byggdes flerbostadshus, men stadsdelsområdet har också stora småhusområden från olika tider.",
     "Sköndal och Tallkrogen har egnahem och villor från 1920–40-talet, ofta med branta sadeltak i tegel eller betong. Fagersjö och Larsboda byggdes ut senare med villor, kedjehus och radhus från 1960- och 70-talet, där betongpannor och låglutande tak dominerar.",
     "Takbehoven skiljer sig därför från kvarter till kvarter. Vi besiktar först och föreslår omläggning, renovering eller byte efter takets faktiska skick.",
   ],
   "items": ["Egnahem i Sköndal och Tallkrogen.", "Radhus och kedjehus i Fagersjö och Larsboda.", "Samfälligheter och enskilda villor."],
   "why": "Vi utgår från Bromma (Mariehäll) och tar uppdrag i hela söderort, däribland Farsta. Vi bokar in besiktning och följer projektet tills taket är klart.",
   "faq": [
     ("Byter ni tak på radhus i Fagersjö och Larsboda?", "Ja, enskilda radhus och hela längor. Vi lämnar underlag till samfälligheten om det behövs."),
     ("Vilka delar av Farsta arbetar ni i?", "Hela stadsdelsområdet, bland annat Sköndal, Fagersjö, Larsboda, Farsta strand, Tallkrogen, Gubbängen och Hökarängen."),
     ("Vårt egnahem i Tallkrogen har gamla betongpannor – byte eller omläggning?", "Det beror på pannornas skick. Är de hela kan omläggning räcka, är de porösa eller frostsprängda är byte bättre."),
   ]},
 "Skärholmen": {
   "intro": "Skärholmen i sydvästra Stockholm omfattar Skärholmen, Sätra, Bredäng och Vårberg. Vi är takläggare i Skärholmen för radhus, kedjehus och bostadsrättsföreningar.",
   "paras": [
     "Skärholmen, Sätra, Bredäng och Vårberg byggdes i huvudsak under 1960- och 70-talet, under miljonprogrammets år. Utöver flerbostadshusen finns radhus- och kedjehusområden från samma tid, ofta förvaltade av samfälligheter eller bostadsrättsföreningar.",
     "Terrängen är kuperad med berg i dagen, och många radhus är byggda i suterräng eller i trappade längor. Det ger tak på olika nivåer med fler anslutningar och plåtdetaljer än på en rak länga.",
     "Taken från den här epoken har nått en ålder där underlaget ofta är slut, även om ytmaterialet ser helt ut. Vi besiktar, dokumenterar och föreslår åtgärder i en ordning som föreningen kan planera ekonomin efter.",
   ],
   "items": ["Radhus och kedjehus från 1960–70-talet.", "Trappade längor och suterränghus.", "Besiktningsrapport för förening och samfällighet."],
   "why": "Vi utgår från Bromma (Mariehäll) och når Skärholmen via Essingeleden och E4/E20. Vi håller kontakt med styrelse eller husägare under hela projektet.",
   "faq": [
     ("Kan ni hjälpa vår förening i Sätra med en takplan?", "Ja. Vi besiktar taken, prioriterar åtgärderna och lämnar kostnadsförslag som går att dela upp i etapper."),
     ("Vilka delar arbetar ni i?", "Skärholmen, Sätra, Bredäng och Vårberg, och vidare mot Hägersten och Huddinge."),
     ("Våra radhus ligger i trappade längor – blir det svårare?", "Det innebär fler anslutningar mellan nivåerna, men det är vanligt för oss. Det viktiga är att plåt och uppvik görs noggrant."),
   ]},
 "Huddinge": {
   "intro": "Huddinge söder om Stockholm har stora villaområden i bland annat Stuvsta, Snättringe, Segeltorp, Fullersta, Trångsund och Skogås. Vi är takläggare i Huddinge för villor och radhus i alla åldrar.",
   "paras": [
     "Huddinges villabebyggelse växte fram längs järnvägen. Stuvsta och Snättringe har många hus från tidigt 1900-tal – trävillor med branta tak, ofta i tegel eller falsad plåt – medan Segeltorp domineras av egnahem från 1920–50-talet.",
     "I Trångsund och Skogås tillkom villor och radhus framför allt under 1960–70-talet, med betongpannor och lägre taklutningar. Flemingsberg och Vårby har mer flerbostadshus och nyare bebyggelse.",
     "Huddinge är kuperat med mycket skog och flera sjöar, bland annat Trehörningen och Orlången. Skogsnära tak får mer barr och påväxt, och sluttande tomter påverkar hur ställning kan placeras.",
   ],
   "items": ["Sekelskiftesvillor i Stuvsta och Snättringe.", "Egnahem i Segeltorp.", "60–70-talshus i Trångsund och Skogås."],
   "why": "Vi utgår från Bromma (Mariehäll) och tar uppdrag söderut i hela Huddinge kommun. Vi bokar besiktning och följer projektet på plats.",
   "faq": [
     ("Vilka delar av Huddinge arbetar ni i?", "Hela kommunen, bland annat Stuvsta, Snättringe, Segeltorp, Fullersta, Trångsund, Skogås och Vårby."),
     ("Kan ni lägga falsat plåttak på en gammal villa i Stuvsta?", "Ja, falsad plåt passar väl på äldre villor och kan utformas så att husets stil bevaras."),
     ("Mitt 70-talshus i Skogås har original betongpannor – vad gäller?", "Har taket inte lagts om sedan huset byggdes är underlagspappen oftast slut. En besiktning visar om pannorna kan återanvändas eller bör bytas."),
   ]},
 "Tyresö": {
   "intro": "Tyresö sydost om Stockholm består till stor del av villaområden mellan skog och vatten. Vi är takläggare i Tyresö för villor, radhus och permanentade fritidshus i bland annat Trollbäcken, Bollmora, Krusboda, Tyresö strand, Brevik och Öringe.",
   "paras": [
     "Mycket av Tyresö var tidigare sommarstugeområden. Brevik, Öringe, Raksta och delar av Tyresö strand har många hus som från början var fritidshus och som byggts ut och permanentats. Bollmora och Krusboda byggdes under 1960–70-talet, och Trollbäcken har stora villaområden från samma tid och framåt.",
     "Läget vid Östersjöns vikar och närheten till Tyresta nationalpark gör att många hus ligger omgivna av skog. Tak under tall och gran får barr i rännorna och mossa på pannorna, och i strandnära lägen tar vinden i takfötter och nockar.",
     "De permanentade fritidshusen har ofta tak som byggts på i etapper. Vi bedömer hela taket och föreslår en lösning som håller för helårsboende.",
   ],
   "items": ["Permanentade fritidshus i Brevik och Öringe.", "Radhus och villor i Krusboda och Trollbäcken.", "Skogs- och vattennära lägen."],
   "why": "Vi utgår från Bromma (Mariehäll) och tar uppdrag i hela Storstockholm, även Tyresö. Vi samlar platsbesök och leveranser så att projektet flyter.",
   "faq": [
     ("Vårt hus var ett fritidshus från början – håller taket?", "Det beror på hur det byggts om. Tak på gamla fritidshus saknar ofta ordentligt underlag och ventilation. En besiktning visar vad som behövs."),
     ("Vilka delar av Tyresö arbetar ni i?", "Hela kommunen, bland annat Trollbäcken, Bollmora, Krusboda, Tyresö strand, Brevik, Öringe och Raksta."),
     ("Byter ni tak på radhus i Krusboda?", "Ja, både enskilda hus och hela längor tillsammans med föreningen."),
   ]},
 "Haninge": {
   "intro": "Haninge söder om Stockholm sträcker sig från Handen och Vendelsö ut till Dalarö och skärgården. Vi är takläggare i Haninge för villor, radhus och sommarhus i bland annat Vendelsö, Brandbergen, Tungelsta, Västerhaninge och Dalarö.",
   "paras": [
     "Vendelsö och Brandbergen har mycket bebyggelse från 1970-talet och framåt, där villor och radhus med betongpannor nu når åldern för takbyte. Västerhaninge och Tungelsta har både äldre villor och nyare områden – Tungelsta har sina rötter i handelsträdgårdarna.",
     "Dalarö är en gammal skärgårdsort med sekelskiftesvillor, sommarvillor och kulturhistoriska miljöer. Här är taken ofta av plåt eller tegel med detaljer som behöver bevaras, och läget vid havet ger salt luft och hård vind.",
     "Fritidshus på öar som Ornö och Utö kräver båt- eller färjetransport av material, vilket vi i så fall planerar särskilt.",
   ],
   "items": ["Villor och radhus i Vendelsö och Brandbergen.", "Sekelskiftesvillor på Dalarö.", "Salt och vind vid kusten."],
   "why": "Vi utgår från Bromma (Mariehäll) och tar uppdrag i hela Storstockholm, även Haninge. Vi planerar resor och etablering så att arbetet går effektivt trots avståndet.",
   "faq": [
     ("Vilka delar av Haninge arbetar ni i?", "Bland annat Handen, Vendelsö, Brandbergen, Jordbro, Västerhaninge, Tungelsta och Dalarö."),
     ("Kan ni bevara detaljerna på en gammal villa på Dalarö?", "Ja, vi väljer material och plåtdetaljer som stämmer med husets stil och utför arbetet varsamt."),
     ("Tar ni uppdrag ute i skärgården?", "Det går att planera, men kräver båt- eller färjetransport. Kontakta oss så bedömer vi förutsättningarna."),
   ]},
 "Värmdö": {
   "intro": "Värmdö öster om Stockholm är skärgårdskommunen med Gustavsberg, Hemmesta, Ingarö, Djurö och tusentals öar. Vi är takläggare på Värmdö för takläggning och takrenovering på villor och fritidshus som blivit permanentboenden.",
   "paras": [
     "Gustavsberg har vuxit kring den gamla porslinsfabriken, med äldre arbetarbostäder, villor och 1960–70-talets bostadsområden. I Hemmesta, Brunn och på Ingarö dominerar villor och fritidshus, där många hus från början byggdes för sommarbruk och sedan permanentats.",
     "Läget i skärgården präglar taken: salt luft påskyndar korrosion på plåt, skruv och beslag, och vinden från fjärdarna tar i nockar, takfötter och vindskivor. Hus på berg och uddar är mer utsatta än de som ligger i skydd av skog.",
     "Många fastigheter nås via smala, ibland privata vägar, och vissa öar bara med båt. Vi planerar därför transporter och leveranser i förväg och samlar arbetsmomenten så att taket blir tätt snabbt.",
   ],
   "items": ["Permanentade fritidshus på Ingarö och i Hemmesta.", "Korrosionsbeständig plåt för skärgårdsklimat.", "Takrenovering och takläggning i utsatta lägen."],
   "why": "Vi utgår från Bromma (Mariehäll) och tar uppdrag på Värmdö med planerade resor över Skurubron. Besiktning och leveranser samlas så att projektet går smidigt.",
   "faq": [
     ("Vilka delar av Värmdö arbetar ni i?", "Bland annat Gustavsberg, Hemmesta, Brunn, Ingarö, Djurö och Stavsnäs. Öar utan fast förbindelse bedömer vi från fall till fall."),
     ("Vilken plåt håller i skärgården?", "Plåt med kraftig ytbeläggning och korrosionsskyddade eller rostfria fästelement. Vi väljer efter hur utsatt huset ligger."),
     ("Räcker takrenovering eller ska vi byta?", "Är underlaget sunt kan rengöring, rostskydd och målning av plåttaket räcka. Är det fuktskadat är byte bättre – besiktningen avgör."),
   ]},
 "Upplands Väsby": {
   "intro": "Upplands Väsby norr om Stockholm har stora villa- och radhusområden från 1960–80-talet. Vi är takläggare i Upplands Väsby för villor och radhus i bland annat Bollstanäs, Vilunda, Runby, Fresta och Smedby.",
   "paras": [
     "Väsby växte kraftigt från 1960-talet, när stora delar av dagens villa- och radhusområden byggdes. Bollstanäs, Vilunda och Runby har villor och radhus från den här tiden, ofta med betongpannor eller plåt på relativt enkla sadeltak.",
     "Det betyder att många tak i kommunen är ungefär jämngamla och har hamnat i samma läge: originalunderlaget har tjänat ut, pannorna har förlorat sin yta och takfotsplåtar och hängrännor behöver bytas.",
     "I Fresta och Smedby finns äldre gårdsbebyggelse och villor, och längs Edssjön och Fysingen ligger hus i mer öppna, vindutsatta lägen.",
   ],
   "items": ["Villor och radhus från 1960–80-talet.", "Betongpannor, plåt och nya hängrännor.", "Samordnade byten i radhusområden."],
   "why": "Vi utgår från Bromma (Mariehäll) och når Upplands Väsby via E4 norrut. Vi kommer ut på besiktning och följer projektet tills taket är klart.",
   "faq": [
     ("Vilka delar av Upplands Väsby arbetar ni i?", "Hela kommunen, bland annat Bollstanäs, Vilunda, Runby, Fresta och Smedby."),
     ("Vårt radhusområde har lika gamla tak – kan vi byta samtidigt?", "Ja. Samordnade byten ger ett enhetligt resultat och enklare etablering. Vi lämnar underlag till samfälligheten."),
     ("Ska vi byta till plåt?", "Plåt är lätt och passar många lutningar. Bygglov krävs normalt inte för villor och radhus sedan 1 december 2025, men samfälligheten kan ha egna regler för enhetligt utseende. Vi går igenom alternativen med er."),
   ]},
 "Vallentuna": {
   "intro": "Vallentuna norr om Stockholm blandar villaområden kring centrum med landsbygd och gårdar i Roslagen. Vi är takläggare i Vallentuna för villor, gårdar och fritidshus i bland annat Vallentuna centrum, Bällsta, Ormsta, Lindholmen, Kårsta och Brottby.",
   "paras": [
     "Tätorten Vallentuna byggdes ut kraftigt under 1970- och 80-talet, med villor och radhus i bland annat Ormsta och Bällsta. Taken från den perioden har ofta betongpannor och originalunderlag som nu behöver ses över.",
     "Utanför tätorten, i Lindholmen, Kårsta och Brottby, finns gårdar, äldre bostadshus och ekonomibyggnader med tegeltak, plåttak och gamla skivtäckningar. Hus i öppet jordbrukslandskap är mer utsatta för vind än de i villaområdena.",
     "Vallentunasjön och de många skogsdungarna ger fukt och påväxt på en del tak. Vi anpassar åtgärderna efter husets ålder, material och läge.",
   ],
   "items": ["Villor och radhus från 1970–80-talet.", "Gårdar och äldre hus på landsbygden.", "Tegel, plåt och betongpannor."],
   "why": "Vi utgår från Bromma (Mariehäll) och tar uppdrag i hela Vallentuna kommun, även på landsbygden. Vi samlar platsbesök och planerar etableringen i förväg.",
   "faq": [
     ("Tar ni uppdrag på landsbygden i Vallentuna?", "Ja, både i tätorten och på gårdar i till exempel Lindholmen, Kårsta och Brottby."),
     ("Lägger ni plåttak på ekonomibyggnader?", "Ja, plåttak på lador, garage och förråd hör till de uppdrag vi tar."),
     ("Vilket material passar ett gammalt gårdshus?", "Lertegel eller falsad plåt brukar passa äldre gårdshus. Vi väljer utifrån husets stil och takstolarnas bärighet."),
   ]},
 "Österåker": {
   "intro": "Österåker nordost om Stockholm sträcker sig från Åkersberga ut i Roslagens skärgård. Vi är takläggare i Österåker för villor, radhus och permanentade sommarhus i bland annat Åkersberga, Österskär, Täljö, Svinninge och på Ljusterö.",
   "paras": [
     "Österskär och Täljö växte fram kring Roslagsbanan som villa- och sommarvilleområden i början av 1900-talet, och här finns fortfarande trävillor med snickarglädje, verandor och branta tak. Många av dem används i dag som permanentboenden.",
     "Åkersberga byggdes ut under 1960–80-talet med villor och radhus, bland annat i Margretelund. Svinninge och Ljusterö har många fritidshus som omvandlats till helårsboende.",
     "Närheten till Trälhavet och Roslagens skärgård ger salt luft och vind, särskilt på uddar och öar. Det påverkar val av plåt, infästning och underhåll.",
   ],
   "items": ["Sekelskiftesvillor i Österskär och Täljö.", "Permanentade fritidshus i Svinninge och på Ljusterö.", "Kustanpassad plåt och infästning."],
   "why": "Vi utgår från Bromma (Mariehäll) och tar uppdrag i hela Österåker, från Åkersberga till öarna. Resor och leveranser planeras så att arbetet kan göras i ett sammanhang.",
   "faq": [
     ("Vilka delar av Österåker arbetar ni i?", "Åkersberga, Österskär, Täljö, Svinninge, Margretelund och Ljusterö med flera."),
     ("Kan ni renovera taket på en gammal sommarvilla i Österskär?", "Ja, vi bevarar husets uttryck – plåtdetaljer, verandatak och takform – och moderniserar underlag och tätskikt."),
     ("Tar ni uppdrag på Ljusterö?", "Ja, med transporter som planeras efter färjan."),
   ]},
 "Botkyrka": {
   "intro": "Botkyrka sydväst om Stockholm har stora villaområden i Tullinge, Tumba och Grödinge och radhusområden från 1960–80-talet. Vi är takläggare i Botkyrka för villor, radhus och samfälligheter.",
   "paras": [
     "Tullinge vid Tullingesjön har villor från tidigt 1900-tal och framåt, i kuperad, skogsklädd terräng. Tumba har växt kring Tumba bruk och järnvägen, med villor och radhus från framför allt 1960–80-talet.",
     "Grödinge och Vårsta har en mer lantlig karaktär med villor, gårdar och fritidshus nära sjöar och skog. I norra Botkyrka, kring Alby, Hallunda och Fittja, dominerar flerbostadshus, men även där finns radhus och småhus.",
     "Variationen gör att takarbetet i Botkyrka spänner från varsam omläggning av äldre villatak i Tullinge till byte av hela radhuslängor i Tumba.",
   ],
   "items": ["Villor i Tullinge och Tumba.", "Radhus och samfälligheter.", "Gårdar och fritidshus i Grödinge."],
   "why": "Vi utgår från Bromma (Mariehäll) och når Botkyrka via E4/E20 söderut. Vi bokar besiktning och följer projektet tills taket är klart.",
   "faq": [
     ("Vilka delar av Botkyrka arbetar ni i?", "Hela kommunen, bland annat Tullinge, Tumba, Grödinge, Vårsta, Norsborg, Hallunda och Alby."),
     ("Byter ni tak på hela radhuslängor i Tumba?", "Ja, vi lämnar underlag till samfälligheten och planerar arbetet länga för länga."),
     ("Vårt hus i Tullinge ligger i slänt mot sjön – går det att bygga ställning?", "Ja, vi anpassar ställningen efter terrängen och använder lift där det behövs."),
   ]},
}

LOC_EXTRA_NEW = {
 "Hässelby": {
   "secs": [
     ("Vanliga tak och problem i Hässelby", [
       "På egnahem från 1920–40-talet är det vanligt att originalteglet ligger kvar men att läkt och underlagspapp bytts någon gång efter kriget – eller aldrig. Typiska skador är fuktfläckar kring skorstenen, där murbruket vittrat, och spruckna pannor längs nocken. Hus från 1950-talet har oftare betongpannor eller fibercementplattor.",
       "Äldre fibercementplattor, så kallad eternit, kan innehålla asbest om de lagts före början av 1980-talet. De ska inte högtryckstvättas eller brytas sönder, utan rivas av behörig personal. Vi bedömer materialet vid besiktningen och planerar rivningen därefter."]),
     ("Planera takprojektet i Hässelby", [
       "Tomterna i villastaden är ofta smala med hus nära gatan, så ställning och container behöver placeras med omsorg. Vi går igenom etableringen med dig vid platsbesöket.",
       "Hässelby tillhör Stockholms stad, och bygglovsfrågor hanteras av stadsbyggnadskontoret. Sedan 1 december 2025 är byte av takmaterial och kulör på villor normalt lovfritt, men har detaljplanen skyddsbestämmelser för huset krävs fortfarande bygglov – kontrollera planen innan du går från tegel till plåt."]),
   ],
   "faq": [
     ("Vad gör ni om taket har eternitplattor?", "Vi bedömer om plattorna kan innehålla asbest. I så fall rivs de av behörig personal enligt Arbetsmiljöverkets regler innan det nya taket läggs."),
     ("Behöver jag bygglov för takbyte i Hässelby villastad?", "Material- och kulörbyte på villor kräver normalt inte lov sedan 1 december 2025, men i kulturhistoriskt värdefulla miljöer kan lov krävas – stäm av med Stockholms stad."),
     ("Kan ni lägga nytt tak på ett radhus i Hässelby strand?", "Ja, både enskilda radhus och hela längor. Plåtdetaljerna mellan husen görs om så att anslutningarna blir täta."),
   ]},
 "Vällingby": {
   "secs": [
     ("Vanliga tak och problem i Vällingby", [
       "På 1950–60-talets radhus är takfoten ofta kort och luftspalten mellan isolering och yttertak knapp. När vinden har tilläggsisolerats ser vi ofta kondens och mögel på råsponten trots att taket är tätt. Mellan husen i en länga är brandväggarnas plåtavtäckningar typiska läckagepunkter.",
       "Lamellhusen kring centrum har ofta låglutande tak med papp eller plåt, där skarvar, brunnar och genomföringar för ventilation behöver ses över regelbundet."]),
     ("Planera takprojektet i Vällingby", [
       "Vällingby är ett av Stockholms mest kända efterkrigsområden, och stadsplanen tar hänsyn till dess kulturhistoriska värde. Vid byte av material eller kulör på radhus eller villor är det därför klokt att kontrollera detaljplanen hos Stockholms stad innan ni bestämmer er.",
       "I radhusområden blir resultatet bäst om hela längan byts samtidigt – då blir kulör och höjder lika och anslutningarna mellan husen kan göras om. Enskilda hus går också, men då är anslutningen mot grannen extra viktig."]),
   ],
   "faq": [
     ("Varför luktar det mögel på vinden i vårt 50-talsradhus?", "Ofta beror det på dålig ventilation efter tilläggsisolering. Vi kontrollerar takfot och luftspalt vid besiktningen."),
     ("Behöver vi bygglov för att byta tak i Vällingby?", "För radhus och villor normalt inte, inte heller vid byte av material eller kulör. Omfattas området av skyddsbestämmelser i detaljplanen krävs lov – stäm av med stadsbyggnadskontoret i Stockholm."),
     ("Kan ett enskilt radhus i en länga få nytt tak?", "Ja, men anslutningen mot grannhusen måste göras noggrant. Ofta är det bättre att samordna med grannarna."),
   ]},
 "Kista": {
   "secs": [
     ("Vanliga tak och problem i Kista", [
       "Papptak och plåttak med låg lutning åldras på andra sätt än branta tegeltak. Typiska skador är blåsor och sprickor i pappen, glipor vid uppvik mot väggar och ventilationshuvar samt stående vatten där underlaget sjunkit. På radhusen är plåtavtäckningar på brandväggar och takfötter vanliga läckagepunkter.",
       "Husen ligger i öppna lägen nära Järvafältet där vinden tar i. Lösa plåtdetaljer och dåligt fästa nockar blir ofta synliga efter en stormvinter, och då lönar det sig att se över infästningen innan skadorna växer."]),
     ("Planera takprojektet i Kista", [
       "I föreningar och samfälligheter är det styrelsen som beslutar om tak. Vi lämnar en besiktningsrapport och ett kostnadsförslag som går att ta upp på stämman, och planerar arbetet så att de boende påverkas så lite som möjligt.",
       "Kista tillhör Stockholms stad. På radhus är byte av tätskikt, material eller kulör normalt lovfritt. På flerbostadshus inom detaljplan kräver en fasadändring bygglov om taket vetter mot gata eller annan allmän plats, och höjs taket krävs alltid lov."]),
   ],
   "faq": [
     ("Hur ofta ska ett låglutande papptak kontrolleras?", "Minst en gång om året, helst efter vintern. Skarvar, brunnar och uppvik är de vanligaste läckagepunkterna."),
     ("Kan ni byta från papp till plåt på ett radhus?", "Ofta ja, om lutningen och underlaget tillåter. På radhus krävs normalt inget bygglov sedan 1 december 2025; på flerbostadshus kan lov krävas om taket vetter mot gata."),
     ("Ser ni över taken efter storm?", "Ja, vi kontrollerar och fäster plåt, nockar och detaljer efter stormskador."),
   ]},
 "Ekerö": {
   "secs": [
     ("Vanliga tak och problem på Ekerö", [
       "Ombyggda fritidshus har ofta tak som lagts för säsongsboende: papp på råspont, tunn läkt eller plåt utan ordentligt underlag. När huset värms året runt och vinden isoleras uppstår kondens om luftspalten inte räcker. Vi ser också tak där flera tillbyggnader lagts ihop med olika lutningar och material.",
       "På äldre gårdar på Färingsö och Munsö finns lertegel och skivtäckningar av olika slag, och på ekonomibyggnader ibland gamla fibercementskivor som kan innehålla asbest. De ska hanteras av behörig personal vid rivning."]),
     ("Planera takprojektet på Ekerö", [
       "Bygglov och anmälan hanteras av Ekerö kommun. Att byta material eller kulör på taket till en villa kräver normalt inget lov sedan 1 december 2025. Kring Drottningholm, som är världsarv, och i andra särskilt värdefulla miljöer gäller dock bygglovsplikt – stäm av med kommunen först.",
       "Många tomter på öarna nås via smala grusvägar. Vi kontrollerar framkomligheten för lastbil, container och ställning vid platsbesöket och planerar leveranserna därefter."]),
   ],
   "faq": [
     ("Behöver jag bygglov för takbyte på Ekerö?", "Normalt inte, även om du byter material eller kulör. I särskilt värdefulla miljöer som kring Drottningholm krävs lov – stäm av med Ekerö kommun."),
     ("Kan ni lägga plåttak på ett gammalt torp?", "Ja, falsad plåt passar många äldre hus. Vi bedömer underlaget och anpassar detaljerna efter huset."),
     ("Kommer lastbilen fram till vår tomt?", "Det kontrollerar vi vid platsbesöket. Vid trånga vägar planerar vi mindre leveranser eller annan placering av container."),
   ]},
 "Hägersten": {
   "secs": [
     ("Vanliga tak och problem i Hägersten", [
       "På Mälarhöjdens äldre villor är ränndalar, kupor och skorstenar de vanligaste läckagepunkterna. Valmade och brutna tak har fler anslutningar än ett enkelt sadeltak, och gamla plåtdetaljer av zink eller galvaniserad plåt kan vara genomrostade även när teglet ser fint ut.",
       "De branta tomterna ner mot Mälaren och de stora träden ger skuggiga takfall med mossa och hängrännor som fylls av löv. På radhusen i Hägerstensåsen och Västertorp ser vi ofta trötta betongpannor och slitna plåtavtäckningar mellan husen."]),
     ("Planera takprojektet i Hägersten", [
       "I Mälarhöjden står många hus i slänt, vilket kräver ställning anpassad efter terrängen och ibland lift. Vi bedömer etableringen på plats innan vi lämnar kostnadsförslag.",
       "Hägersten tillhör Stockholms stad och bygglov söks hos stadsbyggnadskontoret. Material- och kulörbyte på villatak är i regel lovfritt sedan 1 december 2025, men omfattas huset av skyddsbestämmelser i detaljplanen krävs bygglov, och varsamhetskravet gäller alltid. Kontrollera planen för just din tomt."]),
   ],
   "faq": [
     ("Behöver jag bygglov för att byta tak i Mälarhöjden?", "I regel inte. Har detaljplanen skyddsbestämmelser för huset krävs lov även för material- eller kulörbyte – kontakta Stockholms stad."),
     ("Byter ni gamla plåtdetaljer kring skorstenen?", "Ja, nya beslag, ränndalar och skorstensplåt ingår ofta i en omläggning."),
     ("Hur hanterar ni tomter i slänt?", "Vi anpassar ställningen efter terrängen och använder lift där det behövs."),
   ]},
 "Älvsjö": {
   "secs": [
     ("Vanliga tak och problem i Älvsjö", [
       "På hus från 1910–30-talet har taket ofta redan lagts om en gång, ibland med bitumenpapp som nu är spröd. Fuktfläckar i vindsbjälklaget, rostiga spikar i läkten och vatten som rinner längs skorstenen är typiska tecken. Verandor och burspråk har ofta egna små tak med plåt som behöver ny falsning.",
       "Egnahemmen från 1940–50-talet har ofta betongpannor som börjat vittra. Ytan blir porös, pannorna suger vatten och mossan får fäste – särskilt på norrsidan under träden."]),
     ("Planera takprojektet i Älvsjö", [
       "Älvsjö hör till Stockholms stad, och bygglov hanteras av stadsbyggnadskontoret. Sedan 1 december 2025 behövs normalt inget lov för att byta takmaterial eller kulör på en villa. I de äldre villaområdena kan detaljplanen ha skyddsbestämmelser som gör att lov ändå krävs – kolla det innan du väljer nytt material.",
       "Gatorna i villaområdena är ofta smala med parkering längs kanten. Vi planerar container och leveranser så att grannarna kan ta sig fram under hela arbetet."]),
   ],
   "faq": [
     ("Behöver jag bygglov för takbyte i Långbro?", "Normalt inte, inte ens vid nytt material eller ny kulör. Undantag gäller om detaljplanen har skyddsbestämmelser – stäm av med Stockholms stad."),
     ("Varför växer det mossa på mina betongpannor?", "Äldre betongpannor blir porösa och håller fukt. Taktvätt kan hjälpa, men är pannorna vittrade är byte ofta bättre."),
     ("Hur vet jag om pappen under teglet är slut?", "Fuktfläckar på vinden och rost på spik är tecken. En besiktning ger säkert besked."),
   ]},
 "Enskede": {
   "secs": [
     ("Vanliga tak och problem i Enskede", [
       "På de drygt hundraåriga husen i Gamla Enskede har taken i regel lagts om minst en gång. Kupor, brutna takfall och skorstenar mellan parhushalvorna är vanliga läckagepunkter, liksom gamla ränndalar av zink. I parhusen hänger halvornas tak ihop, och en skada på ena sidan kan visa sig hos grannen.",
       "Radhusen i Enskede gård och småhusen i Stureby och Svedmyra har oftare enklare sadeltak med betongpannor eller tegel, där underlaget är det som tagit slut. Gamla fruktträd och stora lövträd ger mycket löv i hängrännorna på hösten."]),
     ("Planera takprojektet i Enskede", [
       "Gamla Enskede är en kulturhistoriskt värdefull miljö. Fasadändringar på villor blev visserligen lovfria 1 december 2025, men i särskilt värdefulla områden och där detaljplanen har skyddsbestämmelser krävs fortfarande bygglov. Ska du ändra material, kulör, kupor eller takfönster här – stäm av med stadsbyggnadskontoret i Stockholms stad först.",
       "Tomterna är små och gatorna smala, så ställning och container planeras tillsammans med grannarna. I parhus lönar det sig ofta att samordna så att båda halvorna får nytt tak samtidigt."]),
   ],
   "faq": [
     ("Får jag sätta in takfönster i Gamla Enskede?", "Det kan kräva bygglov på grund av områdets kulturvärden. Stäm av med Stockholms stad innan – vi hjälper dig med underlag."),
     ("Varför läcker det vid skorstenen mellan parhusen?", "Ofta är plåten eller fogarna kring skorstenen uttjänta. Vi byter beslag och tätar anslutningen."),
     ("Kan ni samordna takbyte för båda parhushalvorna?", "Ja, vi lämnar gärna ett gemensamt förslag så att taket blir enhetligt."),
   ]},
 "Farsta": {
   "secs": [
     ("Vanliga tak och problem i Farsta", [
       "Kedjehus och radhus från 1960–70-talet har ofta tak som är original eller lagts om en gång. Pannorna har tappat sin ytbehandling, underlagspappen är spröd och takfotsplåtarna har rostat. Garage och förråd som binder ihop kedjehusen har ofta låglutande papptak som läcker vid anslutningen mot huset.",
       "Många villor ligger nära Drevviken och Magelungen eller i skogsnära lägen, vilket ger fuktigare takytor och mer påväxt. Regelbunden rensning av hängrännor och taktvätt förlänger livet på taket."]),
     ("Planera takprojektet i Farsta", [
       "När flera kedjehus i samma område byter tak blir etableringen enklare och anslutningarna enhetliga. Prata gärna med grannarna innan du bestämmer dig.",
       "Farsta tillhör Stockholms stad. Sedan 1 december 2025 krävs normalt inget bygglov för att byta takmaterial eller kulör på villor och radhus. Ska taket höjas eller takformen ändras bör du kontrollera med stadsbyggnadskontoret."]),
   ],
   "faq": [
     ("Läcker det ofta mellan garage och hus på kedjehus?", "Ja, anslutningen mellan låga garagetak och husets vägg är en vanlig läckagepunkt. Vi gör om uppviket och plåten."),
     ("Behöver jag bygglov för att byta till plåttak i Farsta?", "För en villa eller ett radhus normalt inte sedan 1 december 2025, så länge huset inte är särskilt kulturhistoriskt värdefullt."),
     ("Tvättar ni tak nära Drevviken?", "Ja, taktvätt och mossbehandling är vanligt i fuktiga, skogsnära lägen."),
   ]},
 "Skärholmen": {
   "secs": [
     ("Vanliga tak och problem i Skärholmen", [
       "På 1960–70-talens radhus är låglutande tak med papp eller betongpannor vanliga. Typiska problem är läckage vid uppvik mot högre längor, igensatta takbrunnar och rostiga takfotsplåtar. Där taken tilläggsisolerats utan att luftspalten anpassats kan det bildas kondens på vinden.",
       "Fibercementskivor på tak och fasader förekommer i bebyggelse från den här tiden och kan innehålla asbest. Vid rivning krävs behörig personal och rätt hantering, vilket vi planerar in redan i kostnadsförslaget."]),
     ("Planera takprojektet i Skärholmen", [
       "Skärholmen tillhör Stockholms stad. För radhus är nytt tak – även i annat material eller annan kulör – normalt lovfritt. Flerbostadshus inom detaljplan kan kräva lov om taket vetter mot allmän plats, och ändrad takhöjd kräver lov.",
       "I radhusområden med gemensamma gårdar och smala gångvägar planerar vi var ställning, container och material ska stå, så att framkomligheten för boende och räddningstjänst behålls."]),
   ],
   "faq": [
     ("Hur vet vi om underlaget är slut fast pannorna ser hela ut?", "Vid besiktning kontrollerar vi vinden: fuktfläckar, mögel och rost på spik visar att underlaget inte håller längre."),
     ("Hanterar ni asbest vid takbyte?", "Asbestrivning kräver särskild behörighet. Vi planerar den med behörig personal innan det nya taket läggs."),
     ("Kan arbetet göras i etapper?", "Ja, i föreningar delar vi ofta upp arbetet per länga eller per år."),
   ]},
 "Huddinge": {
   "secs": [
     ("Vanliga tak och problem i Huddinge", [
       "På äldre villor i Stuvsta och Snättringe ser vi ofta tak där plåt och tegel blandats efter tidigare reparationer, rostiga ränndalar och läckage vid skorstenar. Egnahemmen i Segeltorp har ofta byggts på med kupor eller vindsinredning, vilket ger fler anslutningar att hålla täta.",
       "Radhus och villor från 1960–70-talet i Trångsund och Skogås har nått åldern då både pannor och underlag behöver bytas. Skogsnära lägen ger mossa och barr i hängrännor, och på skuggiga takfall håller pannorna kvar fukt längre."]),
     ("Planera takprojektet i Huddinge", [
       "Huddinge är egen kommun, så bygglov och anmälan hanteras av Huddinge kommun – inte Stockholms stad. Material- och kulörbyte på villatak kräver normalt inget lov. I äldre villaområden kan detaljplanen ha skyddsbestämmelser, och då krävs lov – stäm av med kommunen.",
       "Många tomter i Huddinge sluttar eller ligger på berg. Vi bedömer vid platsbesöket hur ställning och materialhantering ska lösas."]),
   ],
   "faq": [
     ("Var söker jag bygglov för takbyte i Huddinge?", "Hos Huddinge kommun. För takbyte på villa behövs normalt inget lov, även om materialet ändras."),
     ("Ska man byta hängrännor samtidigt?", "Ofta ja. Gamla rännor och stuprör har sällan lika lång livslängd kvar som det nya taket."),
     ("Har ni erfarenhet av kupor och vindsinredningar?", "Ja, anslutningar kring kupor och takfönster är en vanlig del av våra uppdrag."),
   ]},
 "Tyresö": {
   "secs": [
     ("Vanliga tak och problem i Tyresö", [
       "På permanentade fritidshus möter vi ofta tak med flera lutningar och material efter olika tillbyggnader, papp direkt på råspont och för liten luftspalt efter att vinden isolerats. Det ger kondens och mögel på vinden, och ibland läckage där takdelarna möts.",
       "I villaområdena från 1960–70-talet är betongpannor vanligast. Närheten till vatten och skog ger fuktiga takytor där mossa trivs och plåtdetaljer korroderar snabbare. Vattnet i vikarna är bräckt och mindre salt än ute i havsbandet, men vind och fukt sliter ändå på exponerade tak."]),
     ("Planera takprojektet i Tyresö", [
       "Bygglov och anmälan hanteras av Tyresö kommun. Nytt takmaterial eller ny kulör på en villa är normalt lovfritt, men höjs taket – till exempel när ett fritidshus byggs på – krävs bygglov. Byts takstolarna krävs anmälan.",
       "Många tomter i de gamla sommarstugeområdena nås via smala vägar och ligger på berg. Vi kontrollerar framkomlighet och var container och ställning kan stå vid platsbesöket."]),
   ],
   "faq": [
     ("Behöver jag bygglov för takbyte i Tyresö?", "Inte för att byta material eller kulör. Höjer du taket över befintlig nock krävs lov hos Tyresö kommun."),
     ("Varför bildas kondens på vinden i vårt ombyggda fritidshus?", "Ofta för att isoleringen ökats utan att ventilationen anpassats. Vi ser över luftspalt och takfot."),
     ("Kommer ni fram på smala vägar?", "Vi bedömer framkomligheten vid platsbesöket och anpassar leveranserna."),
   ]},
 "Haninge": {
   "secs": [
     ("Vanliga tak och problem i Haninge", [
       "I 70- och 80-talsområdena i Vendelsö och Brandbergen är det betongpannor och underlagspapp som åldrats. Typiskt är vittrade pannor, spröd papp vid takfoten och läckage kring ventilationshuvar. På radhus är plåten på brandväggarna ofta det första som ger efter.",
       "På Dalarö och längs kusten sliter salt och vind på plåt, spik och beslag. Där väljer vi korrosionsbeständig plåt och fästelement och lägger extra vikt vid infästningen av nock, vindskivor och takfotsplåt."]),
     ("Planera takprojektet i Haninge", [
       "Bygglov hanteras av Haninge kommun. Byte av takmaterial eller kulör på villa kräver normalt inget lov. Dalarö har kulturhistoriskt värdefulla miljöer där skyddsbestämmelser kan göra att lov ändå krävs – stäm av med kommunen innan du ändrar något.",
       "Avståndet från vår bas i Bromma gör att vi samlar besiktningar och planerar etableringen noga, så att arbetet kan pågå i ett sammanhang när det väl har startat."]),
   ],
   "faq": [
     ("Behöver jag bygglov för takbyte på Dalarö?", "Det kan krävas, eftersom delar av Dalarö är kulturhistoriskt värdefulla miljöer där lovplikten finns kvar. Stäm av med Haninge kommun."),
     ("Rostar plåten snabbare vid kusten?", "Ja, salt luft påskyndar korrosionen. Rätt plåt och regelbundet underhåll ger ändå lång livslängd."),
     ("Byter ni tak på radhus i Brandbergen?", "Ja, enskilda hus och hela längor."),
   ]},
 "Värmdö": {
   "secs": [
     ("Vanliga tak och problem på Värmdö", [
       "På permanentade fritidshus är det vanligt med tak där underlaget aldrig byggdes för helårsboende: tunn råspont, papp utan luftspalt och plåt som skruvats direkt på läkt. När vinden isoleras och huset värms året runt uppstår kondens och mögel om ventilationen inte följer med.",
       "Plåttak i havsnära lägen rostar ofta först vid skruvar, skarvar och takfot. Vi ser också vindskador där nockplåtar och vindskivor lossnat efter höststormar. Tidigt underhåll – tvätt, rostskydd och efterdragning av skruv – förlänger livet betydligt."]),
     ("Planera takprojektet på Värmdö", [
       "Bygglov och anmälan hanteras av Värmdö kommun. Takbyte på villa är normalt lovfritt även med nytt material eller ny kulör, men höjs taket krävs lov, och i värdefulla kulturmiljöer som delar av Gustavsberg kan lovplikten finnas kvar. Planerar du samtidigt att bygga till kan strandskyddet spela in.",
       "Höst och vinter ger hårdare väder i skärgården. Vi planerar takbyten här i första hand till perioder med stabilare väder och ser till att taket är tätt varje kväll."]),
   ],
   "faq": [
     ("Behöver jag bygglov för att byta tak på Värmdö?", "Normalt inte, även vid byte av material. Höjer du taket eller bygger till samtidigt – kontakta Värmdö kommun."),
     ("När på året är det bäst att byta tak i skärgården?", "Vår till tidig höst ger oftast stabilast väder, men det går att arbeta även senare med rätt planering."),
     ("Kan ni efterdra och rostskydda vårt plåttak?", "Ja, det är ett kostnadseffektivt sätt att förlänga livslängden om plåten fortfarande är sund."),
   ]},
 "Upplands Väsby": {
   "secs": [
     ("Vanliga tak och problem i Upplands Väsby", [
       "Typiskt för hus från 1960–80-talet är betongpannor med sliten yta, underlagspapp som spricker vid takfoten och läkt som börjat ruttna där vatten letat sig in. Takfönster och genomföringar från senare ombyggnader är ofta dåligt inplåtade.",
       "Många villor har kvar hängrännor och stuprör från när huset byggdes. Rostiga rännkrokar och läckande skarvar gör att vatten rinner längs fasaden och ner vid grunden – därför byter vi ofta avvattningen i samma projekt som taket."]),
     ("Planera takprojektet i Upplands Väsby", [
       "Bygglov hanteras av Upplands Väsby kommun. Sedan 1 december 2025 kräver material- eller kulörbyte på villor och radhus normalt inget lov. Samfälligheter kan ändå ha egna regler för enhetligt utseende, och är huset skyddat i detaljplanen krävs lov.",
       "Besikta gärna taket på våren eller hösten, så att ett eventuellt byte kan planeras till en period med torrt väder och god framförhållning."]),
   ],
   "faq": [
     ("Var söker jag bygglov i Upplands Väsby?", "Hos Upplands Väsby kommun. Ett vanligt takbyte på villa eller radhus kräver normalt inget lov."),
     ("Byter ni hängrännor och stuprör samtidigt?", "Ja, det rekommenderar vi ofta när avvattningen är lika gammal som taket."),
     ("Hur gamla är taken i Bollstanäs?", "Många hus är från 1960–70-talet. Har taket inte bytts sedan dess är underlaget ofta slut."),
   ]},
 "Vallentuna": {
   "secs": [
     ("Vanliga tak och problem i Vallentuna", [
       "I villaområdena från 1970–80-talet ser vi betongpannor som tappat ytan, underlagspapp som spruckit och läkt som tagit fukt vid takfoten. På äldre gårdshus är det ofta takstolar och underlag som behöver förstärkas innan ett tyngre tak kan läggas.",
       "På ekonomibyggnader och äldre bostadshus förekommer korrugerade fibercementskivor. Om de lagts före början av 1980-talet kan de innehålla asbest och ska rivas av behörig personal – något vi planerar in innan arbetet startar."]),
     ("Planera takprojektet i Vallentuna", [
       "Bygglov hanteras av Vallentuna kommun. Nytt takmaterial på ett bostadshus kräver normalt inget lov. För särskilt värdefulla gårdsmiljöer och hus med skyddsbestämmelser krävs lov, och förstärks takstolarna krävs anmälan.",
       "På gårdar med långa uppfarter och mjuk mark planerar vi var container och ställning ska stå och när leveranser kan ske, så att marken klarar tunga transporter."]),
   ],
   "faq": [
     ("Behöver jag bygglov för plåttak på en gård i Vallentuna?", "Normalt inte. Är gården utpekad som särskilt värdefull kan lov krävas – stäm av med Vallentuna kommun."),
     ("Vad gör ni om gamla skivor kan innehålla asbest?", "Vi bedömer materialet och planerar rivning med behörig personal innan det nya taket läggs."),
     ("Klarar takstolarna ett tyngre tak?", "Det kontrollerar vi vid besiktning. Ibland krävs förstärkning innan tegel kan läggas."),
   ]},
 "Österåker": {
   "secs": [
     ("Vanliga tak och problem i Österåker", [
       "Sekelskiftesvillorna har ofta plåttak eller tegel med många detaljer: verandatak, kupor, burspråk och dekorativa vindskivor. Gammal plåt kan ha rostat igenom vid falsar och ränndalar, och tidigare lagningar med takpapp eller fogmassa döljer ibland större skador.",
       "Fritidshus som permanentats har ofta tak som inte är byggda för helårsuppvärmning, med för liten luftspalt och enkla underlag. Kombinationen av havsnära fukt och varm vind ger kondens om ventilationen inte är rätt."]),
     ("Planera takprojektet i Österåker", [
       "Bygglov hanteras av Österåkers kommun. Material- och kulörbyte på villatak är normalt lovfritt, men i äldre villamiljöer som Österskär kan skyddsbestämmelser göra att lov krävs. Varsamhetskravet gäller alltid – stäm av med kommunen.",
       "För hus på öar planerar vi färje- eller båttransporter av material och container. På fastlandet bedömer vi framkomlighet och tomtens förutsättningar vid platsbesöket."]),
   ],
   "faq": [
     ("Behöver jag bygglov för takbyte i Österskär?", "Normalt inte. Har huset skyddsbestämmelser i detaljplanen krävs lov – kontakta Österåkers kommun."),
     ("Vårt plåttak har lagats med fogmassa – är det tätt?", "Sällan på sikt. Fogmassa döljer ofta rost under. Vi bedömer om plåten kan lagas eller bör bytas."),
     ("Varför blir det kondens på vinden i vårt sommarhus?", "Oftast för att huset värms året runt utan att takets ventilation anpassats. Vi ser över luftspalt och takfot."),
   ]},
 "Botkyrka": {
   "secs": [
     ("Vanliga tak och problem i Botkyrka", [
       "Tullinges äldre villor har ofta branta tak med tegel eller plåt som lagts om tidigare, där underlaget nu åter är slut. Skuggiga lägen under tallar ger mossa på pannorna och barr i rännorna, och stora takytor mot sjön får mer vind.",
       "I radhus- och villaområdena från 1960–80-talet är betongpannor och papp vanligast. Vi ser ofta spruckna takfotsplåtar, läckande genomföringar och bristande ventilation där vindar tilläggsisolerats."]),
     ("Planera takprojektet i Botkyrka", [
       "Bygglov hanteras av Botkyrka kommun. Att byta takmaterial eller kulör på villa och radhus kräver normalt inget lov. Höjs taket, eller ligger huset i en skyddad kulturmiljö, krävs lov – stäm av med kommunen innan arbetet planeras.",
       "I samfälligheter är det bra att börja med en gemensam besiktning av alla tak. Då kan ni prioritera vilka längor som ska göras först och fördela kostnaderna över tid."]),
   ],
   "faq": [
     ("Var söker jag bygglov för takbyte i Botkyrka?", "Hos Botkyrka kommun. Ett vanligt takbyte på villa kräver normalt inget lov."),
     ("Kan ni besikta alla tak i vår samfällighet?", "Ja, vi gör en samlad besiktning och föreslår en prioriteringsordning."),
     ("Tvättar ni tak i Tullinge?", "Ja, taktvätt och mossbehandling är vanligt i de skogsnära delarna."),
   ]},
}

# Bilder (Recraft via Replicate, tools/gen_images.py). Läggs bara in om filen finns.
ORT_IMG_NEW = {
 "Hässelby": ("ort-hasselby-villa", "Litet egnahem i trä med brant tegeltak, typiskt för Hässelby villastad"),
 "Vällingby": ("ort-vallingby-radhus", "Radhuslänga från 1950-talet med låglutande betongpannetak, typisk för Vällingby"),
 "Kista": ("ort-kista-radhus", "Radhus från 1970-talet med plåtdetaljer i öppet läge nära Järvafältet"),
 "Ekerö": ("ort-ekero-villa", "Rött trähus med svart falsat plåttak vid Mälarens strand på Ekerö"),
 "Hägersten": ("ort-hagersten-villa", "Putsad 1920-talsvilla med valmat tegeltak och kupa, typisk för Mälarhöjden"),
 "Älvsjö": ("ort-alvsjo-villa", "Liten trävilla med tegeltak och glasveranda, typisk för Långbro och Herrängen"),
 "Enskede": ("ort-enskede-villa", "Trävilla med brant tegeltak och staket i trädgårdsstaden Gamla Enskede"),
 "Farsta": ("ort-farsta-villa", "Enplansvilla från 1960-talet med betongpannor, typisk för Farstas villaområden"),
 "Skärholmen": ("ort-skarholmen-radhus", "Radhus från 1960-talet i kuperad terräng, typiska för Sätra och Skärholmen"),
 "Huddinge": ("ort-huddinge-villa", "Äldre trävilla med svart falsat plåttak, typisk för Stuvsta"),
 "Tyresö": ("ort-tyreso-villa", "Permanentat fritidshus med betongpannor på berg vid en vik i Tyresö"),
 "Haninge": ("ort-haninge-villa", "Villa från 1970-talet med bruna betongpannor, typisk för Vendelsö"),
 "Värmdö": ("ort-varmdo-villa", "Skärgårdshus med svart plåttak på klippor vid havet på Värmdö"),
 "Upplands Väsby": ("ort-upplands-vasby-villa", "Villa från 1970-talet med grå betongpannor i Upplands Väsby"),
 "Vallentuna": ("ort-vallentuna-villa", "Faluröd gårdsbyggnad med tegeltak i Vallentunas jordbrukslandskap"),
 "Österåker": ("ort-osteraker-villa", "Sekelskiftesvilla med veranda och rött plåttak, typisk för Österskär"),
 "Botkyrka": ("ort-botkyrka-villa", "Villa från 1960-talet med betongpannor i sluttning ovanför en sjö i Tullinge"),
 "Järfälla": ("ort-jarfalla-radhus", "Radhuslänga från 1970-talet med bruna betongpannor, typisk för Viksjö"),
 "Lidingö": ("ort-lidingo-villa", "Sekelskiftesvilla med patinerat plåttak vid vattnet på Lidingö"),
}
