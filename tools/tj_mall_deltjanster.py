# -*- coding: utf-8 -*-
"""Utrullning 2026-11-19 av pilotmallen (tj_pilot_golvslipning.py) till ortsidorna för fönsterrenovering,
fasadmålning och tapetsering (3 × 33 sidor). Körs från tjanster_v1.py efter piloten och skriver om posterna i TJ –
innehållet i tj_v*_<tjänst>.py är orört, mallen väljer ur det.

Mall (700–900 ord redaktionell text, mätt som i piloten: lead + sektioner + steg + tid + ROT + pris + FAQ):
  1. title «<Tjänst> <Ort> – <vinkel>» (≤ 60 tecken, TITLES nedan; GSC-styrda titlar i seo_overrides.py behålls).
     H1 «<Tjänst> <Ort> – gratis besök och kostnadsförslag» sätts i seo_overrides.py (h1_overrides).
  2. Sidans egna sektioner i ordning (ortens hus och fakta först) – så många som ryms; övriga utgår.
  3. Steg (oförändrade) + «Hur lång tid tar <tjänst> i <Ort>?» (mallstycke ur hubbens granskade text,
     «Tidplanen står i kostnadsförslaget»).
  4. ROT: sidans egna regler för boendeformen + hubbens summering (30 procent, 50 000 / 75 000 kr, material och resor
     ger inget avdrag). Fasadmålning på föreningshus (inget avdrag) lämnas som sidan säger.
  5. «Vad påverkar priset på <tjänst> i <Ort>?»: sidans eget stycke + «Vi publicerar inga prislistor …» med länk i
     texten till hubben.
  6. FAQ: pris (mall, med orten) + upp till tre av sidans egna frågor. Orten står bara i frågor om pris, ROT och
     boendeform; egna frågor om pris eller tid utgår (pris står i mallfrågan, tid i egen sektion).
  7. Källor: bara de som den synliga texten använder. Varje källa knyts till de block (sektion, steg, ROT, pris,
     FAQ) i originalsidan som åberopar den (organisation + ord ur dokumenttiteln, EVIDENCE för undantag); källan
     står kvar om något av blocken står kvar.
Inga nya priser, garantier, årtal, cert, omdömen eller referensuppdrag. Lokala fakta är bara de som redan fanns."""
import html as _H, re as _re

from tj_pilot_golvslipning import _wc

_L = '<a class="text-link" href="{0}">{1}</a>'

SVC = {
 "fonsterrenovering": {
   "name": "Fönsterrenovering", "low": "fönsterrenovering", "hub": "fonsterrenovering.html",
   "time": lambda p, o: [
     f"Hur lång tid en fönsterrenovering {p} {o} tar beror på antalet bågar, hur många som måste tas isär och lagas "
     "och hur högt fönstren sitter. Det som styr kalendern är färgen: tre strykningar med torktid mellan varje lager "
     "gör att en båge är under arbete betydligt längre än den tid vi faktiskt står med penseln.",
     "Utvändigt arbete på plats görs under den varma delen av året och läggs efter väder och väderstreck. "
     "Fönsterhålen är täckta medan bågarna är borta. Tidplanen står i kostnadsförslaget."],
   "price": lambda hub: (
     "Vi publicerar inga prislistor för fönsterrenovering, eftersom två fönster av samma storlek kan vara i helt "
     "olika skick. I kostnadsförslaget står arbete och material var för sig. Hur en renovering går till steg för "
     f"steg, och vad som ingår, beskriver vi på sidan om {hub}."),
   "faq": lambda p, o: (f"Vad kostar fönsterrenovering {p} {o}?",
     "Det beror på antalet bågar, deras skick, hur mycket virke som ska ersättas och om gammal färg ska bort. "
     f"Efter ett gratis platsbesök {p} {o} får du ett skriftligt kostnadsförslag där arbete och material står var för sig."),
   "rot_mat": "Material och resor ger inget avdrag.",
 },
 "fasadmalning": {
   "name": "Fasadmålning", "low": "fasadmålning", "hub": "fasadmalning.html",
   "time": lambda p, o: [
     f"Hur lång tid en fasadmålning {p} {o} tar beror på fasadens yta och höjd, hur mycket gammal färg som ska bort "
     "och på vädret. Själva strykningarna är den kortaste delen. Mellan tvätt och grundning ska fasaden torka, och "
     "mellan strykningarna ska färgen torka, och de pauserna styrs av temperatur och luftfuktighet snarare än av oss.",
     "Utvändig målning görs under den varma delen av året, med marginal för regn. Tidplanen står i kostnadsförslaget."],
   "price": lambda hub: (
     "Vi publicerar inga prislistor för fasadmålning, eftersom förarbetet skiljer mycket mellan två hus av samma "
     "storlek. I kostnadsförslaget står arbete, material och ställning var för sig. Arbetsgången från tvätt till "
     f"sista strykningen, och vad som ingår, beskriver vi på sidan om {hub}."),
   "faq": lambda p, o: (f"Vad kostar fasadmålning {p} {o}?",
     "Det beror på fasadens yta och höjd, hur mycket gammal färg som ska bort, färgtypen och antalet snickerier. "
     f"Efter ett gratis platsbesök {p} {o} får du ett skriftligt kostnadsförslag där arbete, material och ställning står var för sig."),
   "rot_mat": "Färg, material och resor ger inget avdrag.",
 },
 "tapetsering": {
   "name": "Tapetsering", "low": "tapetsering", "hub": "tapetsering.html",
   "time": lambda p, o: [
     f"Hur lång tid en tapetsering {p} {o} tar beror på antalet rum, hur många lager som ska ned och hur mycket "
     "väggen behöver lagas. Själva uppsättningen går fortast. Det som tar tid är underarbetet, eftersom spackel och "
     "förlimning ska torka innan tapeten kommer upp – en tapet som sätts på ett fuktigt underlag riskerar att släppa.",
     "Tidplanen står i kostnadsförslaget. Rummet går att använda när klistret har torkat."],
   "price": lambda hub: (
     "Vi publicerar inga prislistor för tapetsering, eftersom underarbetet avgör mer än väggytan. I kostnadsförslaget "
     "står nedtagning, underarbete och uppsättning var för sig, och tapeten redovisas som material. Tapettyper, "
     f"underarbete och vad som ingår beskriver vi på sidan om {hub}."),
   "faq": lambda p, o: (f"Vad kostar tapetsering {p} {o}?",
     "Det beror på hur många lager som ska ned, hur mycket väggen behöver lagas, takhöjden och mönstret. "
     f"Efter ett gratis platsbesök {p} {o} får du ett skriftligt kostnadsförslag, och ROT-avdraget dras direkt på fakturan."),
   "rot_mat": "Material som tapet och klister ger inget avdrag, och inte heller resor.",
 },
}
# Varianter av mallstyckena (samma påståenden som hubbens granskade text, olika formulering) – annars blir de
# korta sidorna för lika varandra (similarity, 25 %). Variant väljs per sida (VARIANT eller ordningsnummer % 3).
ALT = {
 "fonsterrenovering": {
   "time": [None,
     lambda p, o: [
       f"Antalet bågar avgör mest hur lång tid en fönsterrenovering {p} {o} tar, tillsammans med hur många av dem som "
       "måste tas isär och hur högt de sitter. Färgen sätter takten: varje strykning ska torka innan nästa läggs på, "
       "och därför är en båge under arbete längre än själva penseltiden.",
       "Arbetet på plats görs när det är varmt ute och planeras efter väder och väderstreck, och fönsterhålen hålls "
       "täckta så länge bågarna är borta. Tidplanen står i kostnadsförslaget."],
     lambda p, o: [
       f"En fönsterrenovering {p} {o} tar olika lång tid beroende på hur många bågar huset har, hur många som behöver "
       "lagas och om fönstren sitter högt. Mest tid går åt till att vänta på färgen, eftersom tre strykningar med "
       "torktid emellan inte går att skynda på.",
       "Utvändigt målar vi under årets varma del och väljer dag efter väder och vilket håll fönstret vetter åt. Medan "
       "bågarna är nedtagna är fönsterhålen täckta. Tidplanen står i kostnadsförslaget."]],
   "price": [None,
     lambda hub: (
       "Vi publicerar inga prislistor för fönsterrenovering – skicket kan skilja mycket mellan två lika stora fönster. "
       "Arbete och material redovisas var för sig i kostnadsförslaget. Vad som ingår och hur en renovering går till "
       f"steg för steg beskriver vi på sidan om {hub}."),
     lambda hub: (
       "Vi publicerar inga prislistor för fönsterrenovering, eftersom två fönster med samma mått kan behöva helt olika "
       "mycket arbete. Därför står arbete och material som separata poster i kostnadsförslaget. Arbetsgången och vad "
       f"som ingår finns beskrivet på sidan om {hub}.")]},
 "fasadmalning": {
   "time": [None,
     lambda p, o: [
       f"Hur lång tid en fasadmålning {p} {o} tar styrs av fasadens storlek och höjd, av hur mycket gammal färg som "
       "måste skrapas bort och av vädret. Strykningarna går fort; det är torktiden efter tvätten och mellan lagren som "
       "tar tid, och den bestäms av temperatur och luftfuktighet.",
       "Arbetet görs under årets varma del, och vi planerar med marginal för regn. Tidplanen står i kostnadsförslaget."],
     lambda p, o: [
       f"En fasadmålning {p} {o} tar olika lång tid beroende på väggytan, hur högt huset är, hur mycket färg som ska "
       "bort och vilket väder det blir. Fasaden ska hinna torka efter tvätten och färgen mellan strykningarna, och de "
       "pauserna går inte att korta.",
       "Vi målar under den varma delen av året och lägger in marginal för regniga dagar. Tidplanen står i "
       "kostnadsförslaget."]],
   "price": [None,
     lambda hub: (
       "Vi publicerar inga prislistor för fasadmålning – förarbetet kan skilja mycket mellan två lika stora hus. "
       "Arbete, material och ställning står som egna poster i kostnadsförslaget. Hur arbetet går till från tvätt till "
       f"sista strykning, och vad som ingår, beskriver vi på sidan om {hub}."),
     lambda hub: (
       "Vi publicerar inga prislistor för fasadmålning. Två hus av samma storlek kan kräva helt olika mycket skrapning "
       "och lagning, och därför redovisas arbete, material och ställning var för sig i kostnadsförslaget. Arbetsgången "
       f"och vad som ingår finns på sidan om {hub}.")]},
 "tapetsering": {
   "time": [None,
     lambda p, o: [
       f"Hur lång tid en tapetsering {p} {o} tar beror mest på antalet rum, hur många gamla lager som ska ned och hur "
       "mycket väggen behöver lagas. Uppsättningen går snabbt. Underarbetet tar längre tid, eftersom spackel och "
       "förlimning måste torka först – på ett fuktigt underlag kan tapeten släppa.",
       "Tidplanen står i kostnadsförslaget, och rummet kan användas när klistret har torkat."],
     lambda p, o: [
       f"En tapetsering {p} {o} tar olika lång tid beroende på hur många rum det gäller, hur många lager som ska bort "
       "och hur mycket som ska lagas. Det mesta av tiden går till underarbetet: spackel och förlimning ska vara torra "
       "innan tapeten sätts, annars riskerar den att släppa.",
       "Rummet går att använda när klistret har torkat. Tidplanen står i kostnadsförslaget."]],
   "price": [None,
     lambda hub: (
       "Vi publicerar inga prislistor för tapetsering – det är underarbetet mer än väggytan som avgör. Nedtagning, "
       "underarbete och uppsättning står som egna poster i kostnadsförslaget, och tapeten redovisas som material. Mer "
       f"om tapettyper, underarbete och vad som ingår finns på sidan om {hub}."),
     lambda hub: (
       "Vi publicerar inga prislistor för tapetsering, eftersom två rum med samma väggyta kan kräva helt olika mycket "
       "underarbete. I kostnadsförslaget redovisas nedtagning, underarbete och uppsättning var för sig och tapeten som "
       f"material. Vad som ingår och hur väggen förbereds beskriver vi på sidan om {hub}.")]},
}
VARIANT = {"fonsterrenovering-hasselby": 1}  # fil utan .html -> 0/1/2 när ordningsnumret ger för lika sidor

_ROT_SUM = ("Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
            "tillsammans med rutavdrag.")

# Vinkel i title per sida (≤ 60 tecken med «<Tjänst> <Ort> – »); «, gratis offert» läggs till när det ryms.
# Sidor med GSC-styrd title i seo_overrides.py saknas här. Vinkeln ska stå i någon av de kvarvarande sektionerna.
ANGLE = {
 "fasadmalning-alvsjo": "puts och panel", "fasadmalning-botkyrka": "Tullinges villor",
 "fasadmalning-bromma": "kulör i trädgårdsstaden", "fasadmalning-danderyd": "kalkfärg och ljus puts",
 "fasadmalning-ekero": "rätt säsong och torrt trä", "fasadmalning-enskede": "trädgårdsstadens kulörer",
 "fasadmalning-farsta": "radhus med fasadskivor", "fasadmalning-hagersten": "trävillor i Mälarhöjden",
 "fasadmalning-haninge": "villor och grupphus", "fasadmalning-hasselby": "villastaden och radhusen",
 "fasadmalning-huddinge": "laga med friskt trä", "fasadmalning-jarfalla": "underhåll i rätt tid",
 "fasadmalning-kista": "radhus och atriumhus", "fasadmalning-lidingo": "värdefulla hus",
 "fasadmalning-nacka": "uthus, räcken och plåt", "fasadmalning-norrtalje": "röda bodar i Roslagen",
 "fasadmalning-osteraker": "sommarvillornas kulörer", "fasadmalning-ostermalm": "husets ursprungliga kulör",
 "fasadmalning-sigtuna": "oljefärg mot gatan", "fasadmalning-skarholmen": "radhus från 60- och 70-tal",
 "fasadmalning-sodermalm": "putsfasad mot gatan", "fasadmalning-sollentuna": "ny kulör i villastaden",
 "fasadmalning-solna": "radhus och föreningshus", "fasadmalning-spanga": "bättra eller måla om",
 "fasadmalning-sundbyberg": "ljus puts i stadskärnan", "fasadmalning-taby": "kulör i kedjehusområden",
 "fasadmalning-tyreso": "fritidshusen i Brevik", "fasadmalning-upplands-vasby": "villorna i Bollstanäs",
 "fasadmalning-vallentuna": "småhusen i Lindholmen", "fasadmalning-vallingby": "puts från 1950-talet",
 "fasadmalning-varmdo": "röda hus i skärgården", "fasadmalning-vasastan": "stenstadens putsfasader",
 "fonsterrenovering-alvsjo": "småspröjs och luckor", "fonsterrenovering-bromma": "småstugornas fönster",
 "fonsterrenovering-ekero": "centrum och villorna", "fonsterrenovering-enskede": "trädgårdsstadens fönster",
 "fonsterrenovering-farsta": "småstugorna i Svedmyra", "fonsterrenovering-hagersten": "fönster från flera epoker",
 "fonsterrenovering-haninge": "gårdarnas gamla fönster", "fonsterrenovering-hasselby": "radhusen från 1957",
 "fonsterrenovering-huddinge": "egnahemmens bågar", "fonsterrenovering-jarfalla": "röta i bottenstycket",
 "fonsterrenovering-kista": "radhus från 1970-talet", "fonsterrenovering-kungsholmen": "fönster i bostadsrätt",
 "fonsterrenovering-lidingo": "kitt och linoljefärg", "fonsterrenovering-nacka": "Saltsjöbadens villor",
 "fonsterrenovering-norrtalje": "gårdar och timmerhus", "fonsterrenovering-ostermalm": "30-talsfönster på Gärdet",
 "fonsterrenovering-skarholmen": "radhusen i Sätra", "fonsterrenovering-sodermalm": "besiktning före byte",
 "fonsterrenovering-sollentuna": "täta gamla fönster", "fonsterrenovering-spanga": "villorna i Solhem",
 "fonsterrenovering-sundbyberg": "villorna i Duvbo", "fonsterrenovering-tyreso": "gamla bågar och beslag",
 "fonsterrenovering-upplands-vasby": "kedjehus från 1960-tal", "fonsterrenovering-vallentuna": "tegelvillorna i Karby",
 "fonsterrenovering-vallingby": "radhusens fönster", "fonsterrenovering-varmdo": "glasverandor i Barnvik",
 "fonsterrenovering-vasastan": "jugendfönster",
 "tapetsering-alvsjo": "bårder och dekor", "tapetsering-botkyrka": "tretex och masonit",
 "tapetsering-bromma": "spara gamla tapetlager", "tapetsering-danderyd": "villor och papptak",
 "tapetsering-ekero": "timmerväggar och masonit", "tapetsering-enskede": "vindsrum och snedtak",
 "tapetsering-farsta": "lägenhet och radhus", "tapetsering-hagersten": "villor och lägenheter",
 "tapetsering-haninge": "läs lagren först", "tapetsering-hasselby": "gipsväggar i grupphus",
 "tapetsering-huddinge": "papp på väggen", "tapetsering-jarfalla": "radhus med skivväggar",
 "tapetsering-kista": "betong- och gipsväggar", "tapetsering-kungsholmen": "putsväggar i stenstaden",
 "tapetsering-lidingo": "varsamt i äldre villor", "tapetsering-nacka": "schablonmålning under tapeten",
 "tapetsering-norrtalje": "tapet i fritidshuset", "tapetsering-osteraker": "sommarvilla året runt",
 "tapetsering-ostermalm": "klassade våningar", "tapetsering-sigtuna": "timmerhus i trästaden",
 "tapetsering-skarholmen": "hyresrätt eller bostadsrätt", "tapetsering-sodermalm": "gamla tapetlager",
 "tapetsering-sollentuna": "ett lager till eller skrapa", "tapetsering-solna": "rätt tapet på rätt vägg",
 "tapetsering-spanga": "tapet efter villans epok", "tapetsering-sundbyberg": "lägenheter från 40- och 50-tal",
 "tapetsering-taby": "lister, foder och bröstpanel", "tapetsering-tyreso": "väggen vid kakelugnen",
 "tapetsering-upplands-vasby": "plasttapet i radhus", "tapetsering-vallentuna": "spännpapp och papperstapet",
 "tapetsering-vallingby": "väggar från 1950-talet", "tapetsering-varmdo": "riva eller spara lagren",
 "tapetsering-vasastan": "putsväggar i sekelskifteshus",
}

# Ny description där den gamla nämnde sektioner som har utgått (130–158 tecken, bara innehåll som står kvar).
DESC = {
 "fasadmalning-danderyd": "Fasadmålning i Danderyd: ljus puts och mörka trävillor i Djursholm och Stocksund, kalkfärg i många tunna lager och kulör efter färgprov. Gratis platsbesök.",
 "fasadmalning-ekero": "Fasadmålning på Ekerö: sommarvillor och fritidshus på Mälaröarna – när på året fasaden kan målas och hur torrt träet ska vara. Gratis platsbesök.",
 "fasadmalning-farsta": "Fasadmålning i Farsta: radhus med tegel, puts, fasadskivor och trä – prov och analys av gamla fasadskivor innan de tvättas eller slipas. Gratis platsbesök.",
 "fasadmalning-hagersten": "Fasadmålning i Hägersten: trävillor i Mälarhöjden – vilka färglager som sitter på väggen och hur gammal färg tas bort utan att skada snickarglädjen.",
 "fasadmalning-huddinge": "Fasadmålning i Huddinge: sommarvillor och gårdar där ruttna bräder och vindskivor byts mot friskt trä innan fasaden målas om. Gratis platsbesök och ROT.",
 "fasadmalning-jarfalla": "Fasadmålning i Järfälla: underhåll i rätt tid på egnahem i Björkliden – söderväggen, fönstren och vindskivorna först, mild rengöring och bättring.",
 "fasadmalning-nacka": "Fasadmålning i Nacka: sommarvillor vid farleden – uthus och gäststuga i husets färger och räcken, trappor och plåt som slits först. Gratis platsbesök.",
 "fasadmalning-norrtalje": "Fasadmålning i Norrtälje: gårdar i Roslagen med redargårdarna på Björkö-Arholma och rödfärgade bodar, båthus och lador. Gratis platsbesök och ROT.",
 "fasadmalning-sigtuna": "Fasadmålning i Sigtuna: oljemålad gatufasad och rödfärgad gårdssida i trästaden och kulörer som följde husets ställning i staden. Gratis platsbesök.",
 "fasadmalning-taby": "Fasadmålning i Täby: kulör per husgrupp i Ella gård, Erikslund och Vallatorp, där kedjehus och grupphus målades i samma färg. Gratis platsbesök och ROT.",
 "fasadmalning-tyreso": "Fasadmålning i Tyresö: fritidshus från 1930–60-talen på Brevikshalvön som blivit helårshus – vilken färg panelen bär i dag. Gratis platsbesök och ROT.",
 "fasadmalning-upplands-vasby": "Fasadmålning i Upplands Väsby: sekelskiftesvillor längs Gamla vägen i Bollstanäs med veranda, frontespis och snickerier. Gratis platsbesök och ROT.",
 "fasadmalning-vallentuna": "Fasadmålning i Vallentuna: villor och småhus vid Roslagsbanan – prov på fönsterkitt och puts från före 1980 och täta färgskikt på panelen. Gratis besök.",
 "fasadmalning-vallingby": "Fasadmålning i Vällingby: kedjehus och radhus byggda i grupper på 1950-talet och putsen där cementen styr färgvalet. Gratis platsbesök och kostnadsförslag.",
 "fasadmalning-varmdo": "Fasadmålning på Värmdö: röda hus med vita snickerier i skärgårdsbyarna på Gällnö, Hjälmö och Lådna – två färgtyper i ett arbete. Gratis platsbesök.",
 "fonsterrenovering-bromma": "Fönsterrenovering i Bromma: småstugornas fönster i fasadliv, typritningen som facit och kitt och linoljefärg på bågarna. Gratis platsbesök och ROT-avdrag.",
 "fonsterrenovering-haninge": "Fönsterrenovering i Haninge: boningshus, ladugårdar och uthus på landsbygden – kommunens råd att behålla de ursprungliga fönstren och mittposten.",
 "fonsterrenovering-huddinge": "Fönsterrenovering i Huddinge: okopplade bågar i egnahemsområdena och tätning av innerbågen så att ytterbågen inte ruttnar. Gratis platsbesök och ROT.",
 "fonsterrenovering-jarfalla": "Fönsterrenovering i Järfälla: villorna vid Stäket och Bonäs – röta som börjar i bottenstyckena och hur nederkanten lagas. Gratis platsbesök och ROT.",
 "fonsterrenovering-nacka": "Fönsterrenovering i Nacka: Saltsjöbadens villor från 1890-talet och linoljefärg i tunna lager på hårt utsatta bågar. Gratis platsbesök och ROT-avdrag.",
 "fonsterrenovering-sodermalm": "Fönsterrenovering på Södermalm: föreningens fönster i stenstaden och på malmarna – besiktning fönster för fönster innan något döms ut. Gratis besök.",
 "fonsterrenovering-sollentuna": "Fönsterrenovering i Sollentuna: gamla fönster i villastaden tätas med list först när de är målade och justerade, så att huset får luft. Gratis besök.",
 "fonsterrenovering-vallentuna": "Fönsterrenovering i Vallentuna: 1960-talets tegelvillor i Karby, tätning runt karmen och mötet mellan karm och tegelvägg. Gratis platsbesök och ROT.",
 "fonsterrenovering-varmdo": "Fönsterrenovering på Värmdö: Barnviks by med glasverandor, verandans rutor och bottenstycken och gamla fönster som lagas. Gratis platsbesök och ROT.",
 "fonsterrenovering-vasastan": "Fönsterrenovering i Vasastan: Birkastadens hus från 1902–12 och jugendtidens smala, kopplade fönster med spröjsad överdel. Gratis platsbesök.",
 "tapetsering-botkyrka": "Tapetsering i Botkyrka: ny tapet på tretex och masonit i äldre villor – spärrgrund, spänd papp och lagning av hål och skarvar. Gratis platsbesök och ROT.",
 "tapetsering-danderyd": "Tapetsering i Danderyd: ny tapet i Djursholms och Stocksunds villor, kommunens råd vid ändringar och pappspänt innertak som lagas av målare.",
 "tapetsering-ekero": "Tapetsering på Ekerö: sommarhus som blivit året-runt-hus – masonit och hårdboard och timmerväggar som pappspänns före tapeten. Gratis platsbesök och ROT.",
 "tapetsering-enskede": "Tapetsering i Enskede: ny tapet i trädgårdsstadens vindsrum – spännpapp i snedtakets vinklar och kattvindar bakom väggen. Gratis platsbesök och ROT.",
 "tapetsering-haninge": "Tapetsering i Haninge: egnahemsvillor vid Nynäsbanan och sommarvillor vid vattnet – vad den understa tapeten säger om huset. Gratis platsbesök och ROT.",
 "tapetsering-kungsholmen": "Tapetsering på Kungsholmen: putsade väggar i stenstaden och i Fredhäll – förlimning, lagningar efter ny el och dekor i putsen. Gratis besök och ROT.",
 "tapetsering-lidingo": "Tapetsering på Lidingö: ny tapet i äldre villor – varsamhetskravet inomhus, byggnadsminnen och tapet i gästhus som står kalla på vintern. Gratis besök.",
 "tapetsering-nacka": "Tapetsering i Nacka: villor i Saltsjöbaden och Storängen – schablonmålning under tapeten och hur dekoren tas fram igen. Gratis platsbesök och ROT.",
 "tapetsering-norrtalje": "Tapetsering i Norrtälje: fritidshus som står kalla eller värms upp – vad det gör med tapeten och vad vi ser efter innan ny tapet. Gratis besök och ROT.",
 "tapetsering-sigtuna": "Tapetsering i Sigtuna: timmerhus i stadskärnan och på Malmen – skydd som kan gälla interiören och brandrisken när gamla lager tas ner. Gratis besök.",
 "tapetsering-skarholmen": "Tapetsering i Skärholmen: lägenheter från miljonprogrammets år – vad hyresgäster får göra enligt jordabalken och när rotavdrag gäller. Gratis besök.",
 "tapetsering-sollentuna": "Tapetsering i Sollentuna: när den gamla tapeten tål ett lager till, när den ska ner och att måla direkt på tapet. Gratis platsbesök och ROT-avdrag.",
 "tapetsering-sundbyberg": "Tapetsering i Sundbyberg: lamellhusens lägenheter från 1940- och 50-talen – släta väggar för dagens tapeter, sandspackel och spåntapet. Gratis besök.",
 "tapetsering-taby": "Tapetsering i Täby: villor vid Roslagsbanan – hur tapeten möter lister, foder och bröstpanel och kanterna vid underarbetet. Gratis platsbesök och ROT.",
 "tapetsering-tyreso": "Tapetsering i Tyresö: rum med öppen spis, kamin eller kakelugn – sotarens besked om väggen närmast eldstaden. Gratis platsbesök och ROT-avdrag.",
 "tapetsering-vasastan": "Tapetsering i Vasastan: ny tapet på putsade väggar i stenstadens hus – kridering, förlimning och täckpapp på bar puts. Gratis platsbesök och ROT.",
}

# Undantag i FAQ-valet: fil -> lista med (index i sidans faq, ny fråga | None). Saknas filen väljs automatiskt.
FAQ = {}

# Källa (regex mot namnet) -> regex som måste finnas i ett block för att blocket ska räknas som belägg.
# Används när organisationens namn inte står i texten eller när flera källor har samma organisation.
EVIDENCE = [
 (r"^Skatteverket", r"."),  # ROT-sektionen står alltid kvar
 (r"Områdesfakta (?:20\d\d: )?(.+?) \((?:20\d\d, )?pdf\)", None),  # stadsdelens namn (första ordet) i blocket
 (r"Stadsmuseets kulturhistoriska klassificering", r"[Ss]tadsmuse|klassificer"),
 (r"Varsam utveckling", r"[Vv]arsam|strategi(n|ns)?\b|vägledning"),
 (r"Boverket – Fuktrisker", r"akrylatfärg|plastfärg|putsbortfall|[Ff]ukt"),
 (r"Riksintressen enligt miljöbalken|Översiktsplan, riksintressen", r"riksintresse|översiktsplan"),
 (r"[Ff]asadändring", r"[Ff]asadändring|[Bb]ygglov|[Ll]ovplikt|\blov\b|\blovet\b|karaktärsdrag"),
 (r"[Kk]ulturmiljö(program|plan)", r"[Kk]ulturmiljö(program|plan)"),
 (r"[Öö]versiktsplan", r"[Öö]versiktsplan"),
 (r"Byggnadsmåleri med traditionella färgtyper", r"[Bb]yggnadsmåleri|traditionella färgtyper|måleri från|snickerimålning|[Ff]ärgskiktet"),
 (r"För BRF och hyresvärd", r"BRF|[Ff]ören\w+|hyresvärd"),
 (r"För lägenhetsinnehavare", r"lägenhetsinnehavare|fastighetsägarens medgivande"),
 (r"Sotning och brandskyddskontroll", r"[Ss]otning|brandskydd"),
 (r"Ändrade lagar och regler för byggande", r"ändrade|nya regler|lagändring|1 december 2025"),
 (r"Stockholms stad – Fönster och dörrar", r"fönster och dörrar|[Ss]tadens sida om fönster|kräva (bygg)?lov|bygglovsenheten|"
  r"ändring(ar)? av (ett )?fönst|fönsterändring|söka bygglov|ny kulör som en ändring"),
 (r"^Sollentuna kommun – Kulturhistoriska byggnader", r"[Kk]ulturhistorisk"),
 (r"Kulturhistorisk värdefull byggnad och område \(bygglov", r"blå- eller grönmarkerad|klassificeringskarta|blått, grönt"),
 (r"Förändringar i plan- och bygglagen från 1 december 2025", r"1 december 2025|lovplikt gäller inom"),
 (r"^Värmdö kommun – Kulturmiljö och byggnadsvård", r"kulturmiljökarta|bygglov krävs för ommålning"),
 (r"– Vad vill du bygga\?", r"fastighetsgränsen|[Ff]asadändring kräver"),
 (r"^Sollentuna kommun – Ventilation", r"[Vv]entil"),
 (r"^Sollentuna kommun – Installation eller ändring av ventilation", r"anmälan och startbesked"),
 # Svenska Byggnadsvårdsföreningen – artiklar (fakta per artikel enligt modulernas docstrings, tj_v15–v19_tapetsering.py)
 (r"– Ta bort tapetrester", r"i plast och blöt|släpper mellan lagren"),
 (r"– Nygamla tapeter", r"limtrycksmetoden|tidstypiska kul"),
 (r"– Tryckta papperstapeter", r"blocktryck|vått-i-vått|Ullskalan|ljusäkt|kromoxid|ockror"),
 (r"– Renovera spännpappväggar", r"blivit slak|sträcka sig igen"),
 (r"– Hur bevara blommig 60-talstapet", r"rekonstruerar tapeter|retrotapeter|svårt för en lekman"),
 (r"– Ålder på gammal tapet\?", r"1860–1880|lerklining eller tidningspapper|pappspända väggar var vanliga|1900–1920"),
 (r"– Åldersbestämning av tapet", r"1910|valstryck|flödig|vattenfärg|tapetkatalog"),
 (r"– Renovera innerväggar", r"lagningsgips|botanisera"),
 (r"– Spärrmålning under ny tapet", r"ett enda lager gammal tapet|stärkelseklister|inte förlimmade|plastbehandlade|ouppvärmt"),
 (r"– ”Varningar”", r"släpper i kanterna|avskurna kablar|lappning"),
 (r"– Vad är makulatur", r"makulatur|restpapper|mer levande yta|blev vanligt under 1800-talet|vanligt underlag för tapeter under 1800|utmärkt på panel"),
 (r"– Bredspackla med sandspackel", r"hydrauliskt kalkbruk|gipsbaserat spackel"),
 (r"– Linus på väggen", r"färgtillverkaren|traditionella färger|hygroskop|treetex"),
 (r"– Hur åtgärda veckade hörn", r"[Ss]kär upp hörnen|målarpapp|veckade"),
 (r"– Folkhemmets färger", r"Folkhemmets färger|1930 och 1960|enfärgade ytor"),
 (r"– Underlag för tapetsering på putsad tegelvägg", r"1895|husfix|frilagd (och lagad )?putsvägg|täckpapp|40–50 %"),
 (r"– Underlag för tapetsering$", r"artikel(n)? om underlag|[Uu]nderlag för tapetsering|1920–1950-talen|sandspackel|lim och krit|"
  r"[Kk]ridering|vassa korn|bronstryck|fyra skikt|tidningsprovet|ett lager till|sträcker (tapeten )?upp sig|foderlister|"
  r"våglinje|tapetkniv|i- och skarvspackling|oeldade sommarhus|svarta prickar|extra rulle|lämpliga underlag|luftfuktighet|bukta"),
 (r"– Att rekonstruera tapeter", r"rekonstruera en tapet|tio eller femton lager"),
 (r"– Att värma eller inte värma", r"1964|stödvärme|tapeter som lossnar"),
 (r"– Bestäm husets/tapetens ålder", r"nio lager|1880–90-talet|gulnade råpapper|infärgad pappersmassa"),
 (r"– Bubblig spännpapp", r"[Bb]ubblor|pappspik|torr- och våtremsor"),
 (r"– Dekorativ puts i lägenhet", r"provskrapa|skalpell|meander|dekor i putsen|fråga grannarna"),
 (r"– Direktklistrad papp mot underpanel", r"underpanel|spännlister|brädgårdsvirke|pappkläddes|klassiska tillvägagångssättet"),
 (r"– Felvänd tapet i innertak", r"baksidan nedåt|återbruk"),
 (r"– Fixa iordning vägg beklädd med tretex", r"spärrgrund|lösningsmedel|längre nubb|miljövänligt material"),
 (r"– Hur gör vi med gamla strukturtapeter", r"flossbar|strukturtapet|renoveringsgips"),
 (r"– Hårdboard som väggbeklädnad", r"[Hh]årdboard|HDF|6 mm"),
 (r"– Identifiera gamla tapeter", r"rekommenderar normalt inga företag|specialkunskap"),
 (r"– Inomhus betongvägg", r"silikatfärg|70-talslägenhet|inte (självklart )?så vacker"),
 (r"– Kan ett nödtorftigt isolerat trähus", r"1965|textilier|stoppade möbler|buckliga|hygrometer|grundvärme"),
 (r"– Laga lerklining inför tapetsering", r"inte för hårt spackel|mekanisk stress|kan lossna av"),
 (r"– Laga putsade innerväggar", r"1870-talet|ny el|lerputs löser sig|vädra ut fukt|nedknackat"),
 (r"– Laga reva i spännpapp", r"[Rr]eva|revorna|häftklammer|spikremsa|fuktrosor"),
 (r"– Laga tretex och tapet som släppt", r"gipsbaserat spackel som (ges|får) struktur|våtrumslim"),
 (r"– Lerklina eller behålla tapeter", r"tilläggsisoler|glasull|originalpappen|sentida isoleringen"),
 (r"– Limfärg på väggar", r"[Ll]imfärg(en)? ger ett sämre|fintapet"),
 (r"– Materialhörnan – Pappspänt tak", r"amatör|yrkesmålarnas|hörnpapp|stödjande brädor|spännas om"),
 (r"– Måla eller tapetsera på gamla masonitskivor", r"[Mm]asonit|golvtäckpapp"),
 (r"– Måla om pappspänt tak", r"grundat innan|klisterremsorna|mager oljefärg"),
 (r"– Ny vägg sekelskifteslägenhet", r"kloasong|pärlspont|tapetdörr|takstuck|ny vägg"),
 (r"– Pappspänning på OSB-skivor", r"OSB|klistrar (man )?våderna och inte underlaget"),
 (r"– Pappspänning på lerklining", r"spik(en)? att fästa|ramar|täckpapp"),
 (r"– Pappspänning på ojämn timmervägg", r"skrot|såt(en|ar)|trekantlister|möss|benlim"),
 (r"– Pappspänt tak – lös våd", r"latexfog|torr remsa|yttersta våden"),
 (r"– Passion för schabloner", r"Byggnadskultur 2017|i århundraden|1990-talet|industrialiserades"),
 (r"– Putsa murstock", r"1923|dold bakom skivor|gärna även klistret"),
 (r"– Renovera hus från 1890", r"lerklining som målas|1890"),
 (r"– Riva ner tapeter eller inte", r"kulturlager|dilemma"),
 (r"– Rädda pappspänd tapet som släppt", r"skär upp en bit|fukta baksidan|spika tillbaka"),
 (r"– Rädda underliggande schablonmålning", r"målerikonservator|färgborttagning|plastfolie|uppfuktning"),
 (r"– Schablonmåleri", r"sekelskiftesgård|tempera|retusch|äldre tekniker"),
 (r"– Spännpapp på vägg", r"hörnkappor|remsor över alla skarvar|tomrummen"),
 (r"– Strömbrytare och uttag", r"[Ss]trömbrytare|strömställare|elektriker|kablar"),
 (r"– Ta hand om tapetskatten", r"hänger löst|egen tyngd|patina|försiktiga medel"),
 (r"– Tapeter \(täta skikt", r"vattenavvisande|diffusionsöppna|limfärgstapeter"),
 (r"– Tapeter på svenska väggar", r"stämpl|tillverkningsår"),
 (r"– Tapeter på tretex", r"40–50-talet satte tretex|tretexskivor i alla rum"),
 (r"– Tapetsera med modern tapet i gammalt hus", r"värms (upp )?(hela )?året runt|kallställ|anrikas"),
 (r"– Tapetsera på inre lagret", r"spaltbar|inre lagret|sträcka upp sig när det torkar"),
 (r"– Tapetsera på puts av kalkbruk", r"kalkbruk|suger ur bindemedlet"),
 (r"– Tapetsera på trasig pappspänning", r"grovt plank|limfärgstapet|löser (sig|mönstret)|oljegrund"),
 (r"– Tapetsera vardagsrum renoverat", r"50–60-talet|tre lager tapet"),
 (r"– Tapetsering lerklinade väggar", r"pulverklister|golvpapp"),
 (r"– Tapetsering med lumppapp", r"lumppapp"),
 (r"– Underlag vid tapetsering i gammalt torp", r"timmervägg bör pappspännas|mager oljefärgsgrund"),
 (r"– Vad målar jag med runt kakelugn", r"1700-talshus|silikatfärg på skivorna|brandisolerade"),
 (r"– Vägg bakom kamin", r"1919|kamin"),
 (r"– Ytskikt och isolering i 1800-talshus", r"borra i murstock|regel i golv och tak"),
 (r"– Var tapeter på 50-talet", r"knappast (var )?bättre|kraven på finish|färghandel|spåntapet|snåla"),
 (r"– Varför kondens", r"[Kk]ondens|70–75 %|kalla ytor"),
 (r"– Äggoljetempera på tapet", r"[Ää]ggoljetempera"),
 (r"– Ålder på tapet i gammalt torp", r"omkring 1870|blödde in|blöder in"),
 (r"– Vävtapet", r"[Vv]äv(en|tapet)|slätt och fast"),
 (r"– Väggytskikt av papp", r"uppfuktad i perioder|porös"),
 (r"^Riksantikvarieämbetet – Fönster", r"Riksantikvarieämbet|RAÄ"),
 (r"^Länsstyrelserna.*Puts på mur", r"&[Pp]uts"),
 (r"^Länsstyrelserna.*Målning utomhus på trä", r"&[Tt]rä|[Ss]öderfasad|tvätta"),
 (r"^Huddinge kommun – Ändra fasad", r"&[Bb]ygglov|renovera fasaden"),
 (r"^Tyresö kommun – Måla om huset", r"&[Mm]åla om|[Bb]ygglov|[Dd]etaljplan"),
]

_HOUSING = r"bostadsrätt|radhus|villa|villan|fritidshus|lägenhet|kedjehus|parhus|egnahem|sommarhus|småhus|flerbostadshus|föreningshus"
_TOPIC_OK = r"kosta|pris|rot|avdrag|" + _HOUSING
_PRICE_Q = r"[Vv]ad kostar|[Pp]ris|kostnad"
_TIME_Q = r"[Hh]ur lång tid|[Hh]ur länge|[Hh]ur många dagar|[Hh]ur snabbt"

# organisation (början av källans namn) -> hur den nämns i texten
ORG = [
 (r"^Skatteverket", r"Skatteverket|rotavdrag|ROT-avdrag|[Aa]vdraget"),
 (r"^Boverket", r"Boverket"),
 (r"^Riksantikvarieämbetet", r"Riksantikvarieämbet"),
 (r"^Länsstyrelserna i Gävleborgs", r"[Ll]änsstyrelsernas|[Ll]änsstyrelserna|informationsblad|fönsterblad"),
 (r"^Länsstyrelsen i Stockholms län", r"Länsstyrelsen"),
 (r"^Svenska Byggnadsvårdsföreningen", r"Byggnadsvårdsförening|[Ff]öreningen (skriver|påpekar|svarar|råder|avråder|rekommenderar|tipsar|förklarar|beskriver|menar|nämner|varnar)|enligt föreningen"),
 (r"^Arbetsmiljöverket", r"Arbetsmiljöverket"),
 (r"^Riksdagen", r"(plan- och bygg|bostadsrätts|miljö|kulturmiljö|ordnings|arbetsmiljö)lag|[Ll]agen\b|balk|förordning|PBL"),
 (r"^Kulturen i Lund", r"Kulturen"),
 (r"^Stockholms läns museum", r"[Ll]änsmuse|läns museum"),
 (r"^Värmdö kommun och Stockholms läns museum", r"Värmdö|länsmuse|läns museum"),
 (r"^(Stadsmuseet|Stockholms stadsmuseum|Stockholmskällan)", r"[Ss]tadsmuse|Stockholmskällan"),
 (r"^Södertörns brandförsvarsförbund", r"[Bb]randförsvar|räddningstjänst"),
 (r"^(\w+?)s? (kommun|stad)$|^(\w+?)s? (kommun|stad) ", None),  # «Botkyrka kommun», «Stockholms stad»
]
_GENERIC = {w[:max(4, len(w) - 2)] for w in "tapet tapeter tapetsering fönster fönstren fasad fasader fasaden målning måla "
             "färg renovera renovering gamla gammal äldre stockholm stockholms villa villor småhus hus huset byggnad "
             "byggnader information råd kommun stad".split()}
_STOP = set("och eller med för som till från över under inte utan efter före samt eget egna egen sina sitt sin hur vad när var vilka vilken detta denna dessa pdf den det har kan ska bör att".split())


def _plain(x):
    return _H.unescape(_re.sub(r"<[^>]+>", " ", x))


def _org_rx(name):
    for pat, rx in ORG:
        m = _re.search(pat, name)
        if m:
            if rx is None:
                place = next(g for g in m.groups() if g and g not in ("kommun", "stad"))
                kind = "kommun" if "kommun" in m.group(0) else "stad"
                return (rf"{place}s? {kind}|{place}s \w*(program|plan|guide)|{kind}ens|[Kk]ommunens|"
                        rf"{kind}en (skriver|anger|beskriver|säger|pekar|räknar)")
            return rx
    return None


def _tokens(name):
    t = name.split(" – ", 1)[1] if " – " in name else name
    ws = [w.lower() for w in _re.findall(r"[A-Za-zÅÄÖåäöéü][\wåäöéü-]{3,}", t)]
    return [w[:max(4, len(w) - 2)] for w in ws if w not in _STOP]


def _blocks(d):
    """Originalsidans block: (nyckel, text)."""
    b = [("lead", d["lead"])]
    for s in d["sections"]:
        b.append(("sec:" + s["id"], " ".join([s["h2"]] + s["paras"] + ([s["aside"]["title"]] + s["aside"]["items"] if s.get("aside") else []))))
    b += [("steps", " ".join(x for st in d["steps"] for x in st)), ("rot", " ".join(d["rot"])), ("price", " ".join(d["price"]))]
    b += [(f"faq:{i}", q + " " + a) for i, (q, a) in enumerate(d["faq"])]
    return [(k, _plain(v)) for k, v in b]


def source_blocks(d):
    """Källa -> mängd block i originalsidan som använder den. None = kunde inte avgöras (rapporteras)."""
    blocks, out = _blocks(d), {}
    srcs = d["sources"]
    for name, _u in srcs:
        orx = _org_rx(name)
        same = [n for n, _ in srcs if orx and _org_rx(n) == orx]
        m = next(((_re.search(p, name), e) for p, e in EVIDENCE if _re.search(p, name)), None)
        ev_hit = set()
        if m is not None:
            ev = m[1] if m[1] is not None else _re.escape(_re.sub(r"s$", "", _re.split(r"[ ,]", m[0].group(1))[0]))
            need_org = ev.startswith("&")
            ev = ev.lstrip("&")
            # lead, steg, pris och ROT åberopar sällan en källa: där räknas bara block som också nämner organisationen
            ev_hit = {k for k, t in blocks if _re.search(ev, t)
                      and (not need_org or (orx and _re.search(orx, t)))
                      and (k.startswith(("sec:", "faq:")) or (orx and _re.search(orx, t)) or name.startswith("Skatteverket")
                           or (k == "steps" and "Stadsmuse" in name))}  # steget «kontroll i Stadsmuseets karta»
            if len(same) != 1 or name.startswith("Skatteverket"):
                out[name] = ev_hit or "UNUSED"  # dokumentets kännetecken finns inte på originalsidan
                continue
        toks = _tokens(name)
        # ord som står i mer än hälften av sidans block säger inget om vilken källa som används (t.ex. «tapet»)
        common = {w for w in set(toks) if sum(1 for _k, t in blocks if w in t.lower()) > len(blocks) / 2}
        toks = [w for w in toks if w not in common and w not in _GENERIC]
        scored = []
        for k, t in blocks:
            tl = t.lower()
            o = bool(orx and _re.search(orx, t))
            sc = sum(1 for w in set(toks) if w in tl)
            scored.append((k, o, sc))
        if orx and len(same) == 1:
            hit = {k for k, o, sc in scored if o} | ev_hit
            if not hit:
                out[name] = "UNUSED"  # organisationen nämns inte någonstans på originalsidan
                continue
        else:
            hit = {k for k, o, sc in scored if (o or not orx) and sc > 0} | ev_hit
        if not hit and orx:
            # kunde inte avgöras: kandidater = alla block som nämner organisationen
            out[name] = ("?", {k for k, o, sc in scored if o})
            continue
        out[name] = hit or None
    return out


# Meningar där sidans egen regel stod ihop med summeringen: regeln behålls, summeringen ersätts av hubbens.
ROT_KEEP = {
 "Målning av fasaden på ett småhus som du äger och bor i ger rotavdrag på arbetskostnaden, högst 30 procent och högst 50 000 kronor per person och år.":
   "Målning av fasaden på ett småhus som du äger och bor i ger rotavdrag på arbetskostnaden.",
 "Du ska äga huset när arbetet utförs, och vi drar avdraget direkt på fakturan.": "Du ska äga huset när arbetet utförs.",
 "I en bostadsrätt eller ett ägt radhus drar Geal av rotavdraget direkt på fakturan: högst 30 procent av arbetskostnaden och högst 50 000 kr per person och år, inom gränsen 75 000 kr för rot och rut sammanlagt.":
   "I en bostadsrätt eller ett ägt radhus ger tapetseringen rotavdrag.",
}


def _fix_rot(rot, svc):
    """Sidans ROT-regler behålls; summeringen (procent, tak, material, resor, fakturan) ersätts med hubbens."""
    txt = " ".join(rot)
    if not _re.search(r"procent", txt):
        return rot, False  # fasad på föreningshus: sidan säger att avdraget inte gäller
    drop = _re.compile(r"procent|50 000|75 000|[Bb]ara arbetskostnaden|^(Material|Tapet|Färg|Glas|Kitt|Resor)[^.]*ger inget avdrag|"
                       r"^(Kitt|Tapet|Färg|Glas)[^.]*räknas inte( in)?\.$|betalas fullt ut|görs direkt på fakturan|drar Geal det direkt på fakturan|[Mm]aterial ingår inte|"
                       r"(drar|gör) (av )?(avdraget|beloppet|det|rotavdraget) (direkt )?på fakturan|dras (direkt )?på fakturan")
    summary = _ROT_SUM + " " + SVC[svc]["rot_mat"] + " Geal drar avdraget direkt på fakturan."
    out, placed = [], False
    for p in rot:
        sents = _re.split(r"(?<=[.!?])\s+(?=[A-ZÅÄÖ])", p)
        keep = []
        for s_ in sents:
            if s_ in ROT_KEEP:  # sidans egen regel i en mening som också innehöll summeringen
                s_ = ROT_KEEP[s_]
                keep.append(s_)
                if not placed:
                    keep.append(summary)
                    placed = True
                continue
            if not drop.search(s_):
                keep.append(s_)
            elif not placed:  # summeringen står där sidans egen summering stod, så att ordningen behålls
                keep.append(summary)
                placed = True
        if keep:
            out.append(" ".join(keep))
    if not placed:
        out.append(summary)
    return out, True


def _visible(d):
    t = [d["lead"], d["steps_h2"], d.get("time_h2", ""), d["rot_h2"], d["price_h2"]]
    for s in d["sections"]:
        t += [s["h2"]] + s["paras"] + ([s["aside"]["title"]] + s["aside"]["items"] if s.get("aside") else [])
    t += [x for st in d["steps"] for x in st] + d.get("time", []) + d["rot"] + d["price"] + [x for f in d["faq"] for x in f]
    return t


def editorial_words(d):
    return sum(_wc(x) for x in _visible(d))


def _own_faq(f, d, ort):
    if f in FAQ:
        return [(q or d["faq"][i][0], d["faq"][i][1], i) for i, q in FAQ[f]]
    out = []
    for i, (q, a) in enumerate(d["faq"]):
        if _re.search(_PRICE_Q, q) or _re.search(_TIME_Q, q):
            continue
        if ort in q and not _re.search(_TOPIC_OK, q, _re.I):
            q2 = _re.sub(rf"\s+(i|på) {_re.escape(ort)}(?=[?,])", "", q)
            if ort in q2:
                continue
            q = q2
        out.append((q, a, i))
    return out


def apply(TJ):
    report = {}
    order = {}
    for f in sorted(TJ):
        if TJ[f]["service"] in SVC and TJ[f]["kind"] == "district":
            order[f] = len([x for x in order if TJ[x]["service"] == TJ[f]["service"]])
    for f, d in TJ.items():
        svc = d["service"]
        if svc not in SVC or d["kind"] != "district":
            continue
        c, ort = SVC[svc], d["ort"]
        prep = "på" if _re.match(rf"{c['name']} på ", d["title"]) else "i"
        hub = _L.format(c["hub"], f"{c['low']} i Stockholm")
        sb = source_blocks(d)
        orig = {"sections": d["sections"], "faq": d["faq"], "sources": d["sources"], "rot": d["rot"], "title": d["title"]}
        d["_orig"] = orig
        key = f[:-5]
        if key in ANGLE:
            t = f"{c['name']} {ort} – {ANGLE[key]}"
            if len(t + ", gratis offert") <= 60:
                t += ", gratis offert"
            elif svc != "fasadmalning" and len(t + ", ROT") <= 60:
                t += ", ROT"  # fasadmålning: inget ROT-suffix (gäller inte fasaden på föreningshus)
            assert len(t) <= 60, (f, t)
            d["title"] = t
        if key in DESC:
            assert 130 <= len(DESC[key]) <= 155, (f, len(DESC[key]))
            d["description"] = DESC[key]
        d["time_h2"] = f"Hur lång tid tar {c['low']} {prep} {ort}?"
        v = VARIANT.get(f[:-5], order[f] % 3)
        d["time"] = (ALT[svc]["time"][v] or c["time"])(prep, ort)
        d["rot"], rot_std = _fix_rot(orig["rot"], svc)
        d["price_h2"] = f"Vad påverkar priset på {c['low']} {prep} {ort}?"
        d["price"] = list(d["price"]) + [(ALT[svc]["price"][v] or c["price"])(hub)]
        tmpl = [c["faq"](prep, ort)]
        own = _own_faq(f, d, ort)
        best = None
        secs = orig["sections"]
        for k in range(len(secs), 0, -1):
            for n in (3, 2, 1):
                if n > len(own):
                    continue
                d["sections"] = secs[:k]
                d["faq"] = tmpl + [(q, a) for q, a, _i in own[:n]]
                w = editorial_words(d)
                if 700 <= w <= 900:
                    best = (k, n)
                    break
            if best:
                break
        assert best, (f, "hittar ingen kombination 700–900 ord")
        k, n = best
        d["sections"] = secs[:k]
        kept_faq = own[:n]
        d["faq"] = tmpl + [(q, a) for q, a, _i in kept_faq]
        kept_blocks = {"lead", "steps", "rot", "price"} | {"sec:" + s["id"] for s in d["sections"]} | {f"faq:{i}" for _q, _a, i in kept_faq}
        srcs, unknown = [], []
        for name, url in orig["sources"]:
            hit = sb.get(name)
            if hit == "UNUSED":
                unknown.append("(oanvänd redan före, struken) " + name)
                continue
            if isinstance(hit, tuple):  # oavgjord: står kvar bara om ett kvarvarande block nämner organisationen
                if hit[1] & kept_blocks:
                    srcs.append((name, url)); unknown.append(name)
                continue
            if hit is None:
                srcs.append((name, url)); unknown.append(name)
            elif hit & kept_blocks:
                srcs.append((name, url))
        if not any(n_.startswith("Skatteverket") for n_, _ in srcs) and rot_std:
            unknown.append("(Skatteverket saknas)")
        d["sources"] = srcs
        d["_unknown_sources"] = unknown
        d["_source_blocks"] = sb
        d["pilot_words"] = editorial_words(d)
        report[f] = (k, len(secs), n, d["pilot_words"])
    return report
