# -*- coding: utf-8 -*-
"""Takbyte – ortsidor v5: Bromma, Danderyd, Huddinge, Norrtälje, Sollentuna, Täby (2026-10-25).
Hubb: takbyte.html (vanlig tjänstesida i generate.py, listar ortsidorna).
Fakta endast från källorna i respektive 'sources', öppnade 2026-10-25: Stockholms stad (bygglov.stockholm:
Fasadändring; Solceller, solpanel, solfångare; vägledningen Varsam utveckling av småhus- och villaområden),
Danderyds kommun (Nya regler för bygglov från 1 december 2025; Solenergi; Riktlinjer för kulturmiljöhistoriska
byggnader och miljöer 2024; kulturmiljöhandboken B46 Gamla Djursholm), Huddinge kommun (Ändra fasad eller tak;
Solceller; Takkupa; kulturmiljöprogram del 2), Norrtälje kommun (Lovbefriade åtgärder; Skillnad mellan
åtgärder; Riksintresseområden för kulturmiljövården; kulturmiljöutredningen Arholma), Sollentuna kommun
(Byta takmaterial; Solceller och solfångare; Kulturhistoriska byggnader och områden; Tilläggsisolera),
Täby kommun (Fasadändring; Kulturmiljöer i Täby), Boverket (PBL kunskapsbanken: fasadändring; snölaster;
vindlaster) och Skatteverket (rotavdrag). Inga priser, garantier, omdömen, egna uppdrag eller cert.
Schema: se tools/tj_check.py."""

# ------------------------------------------------------------------ gemensamma källor
_BV_FASAD = ("Boverket – PBL kunskapsbanken: Bygglov för fasadändring",
             "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/")
_BV_SNO = ("Boverket – Snölaster",
           "https://www.boverket.se/sv/PBL-kunskapsbanken/regler-om-byggande/barformaga-stadga-bestandighet/laster/snolaster/")
_BV_VIND = ("Boverket – Vindlaster",
            "https://www.boverket.se/sv/PBL-kunskapsbanken/regler-om-byggande/barformaga-stadga-bestandighet/laster/vindlaster/")
_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
              "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_L = '<a class="text-link" href="{0}">{1}</a>'

PAGES_TJ = {

# ------------------------------------------------------------------ BROMMA
"takbyte-bromma.html": {
  "kind": "district", "service": "takbyte", "ort": "Bromma", "svc_label": "Takbyte",
  "title": "Takbyte i Bromma – lertegel, småstugor och solceller",
  "description": "Takbyte i Bromma: rött lertegel på småstugorna, när ett nytt takmaterial blir en fasadändring och varför solceller ofta kräver bygglov i Stockholm.",
  "h1": "Takbyte i Bromma",
  "lead": "När ett Brommatak ska bytas handlar valet sällan bara om livslängd. På småstugorna i Norra Ängby och Olovslund hörde det röda lerteglet till typritningen, och i stora delar av Stockholm kräver solceller bygglov. Geal Entreprenad AB har sitt kontor i Bromma, byter tak i hela stadsdelen och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Lertegel, småstugor och solceller i Bromma.",
  "sections": [
    {"id": "smastugor-bromma", "anchor": "Småstugornas tak",
     "h2": "Typritningar och rött lertegel på småstugorna",
     "paras": [
       "Stockholms stads vägledning Varsam utveckling av småhus- och villaområden beskriver hur småstugeområdena byggdes ut i regi av stadens småstugebyrå. Pungpinan och Olovslund var först ut, och 1927 stod de första stugorna klara. Därefter följde bland annat Norra Ängby. Kraven var att husen skulle vara billiga och lätta att uppföra, och det ledde till standardisering och kataloger med hustyper.",
       "Enligt vägledningen täcktes taken med enkupigt eller tvåkupigt rött lertegel, och områdenas enhetliga karaktär hänger på volymer, proportioner och takens utformning. Pungpinan, Olovslund och Norra Ängby är dessutom utpekade som riksintressen för kulturmiljövården. Ett nytt tak i betong, i plåt eller i en annan kulör syns därför direkt i en rad av likadana hus.",
       "I slutet av 1970-talet samlade stadsbyggnadskontoret typritningarna från 1927–1957 i en sammanställning, som stöd för den som ville ändra sin stuga. En sådan ritning kan visa takvinkel, takfot och skorstenens läge, vilket är bra underlag när pannor, läkt och plåt ska beställas. Hur äldre tak i stadsdelen renoveras beskrivs under " + _L.format("takrenovering-bromma.html", "takrenovering i Bromma") + ".",
     ],
     "aside": {"title": "Småstugornas tak", "items": [
       "Hustyper från stadens småstugebyrå", "Enkupigt eller tvåkupigt rött lertegel",
       "Pungpinan, Olovslund och Norra Ängby är riksintressen", "Typritningar 1927–1957 samlade"]}},
    {"id": "material-bromma", "h2": "Samma material eller ett annat – det avgör lovfrågan",
     "paras": [
       "Boverket förklarar att ett byte till ett annat taktäckningsmaterial, till exempel från tegeltak till plåttak, är en fasadändring. Att byta till samma material i samma utförande räknas däremot som underhåll. Sedan 1 december 2025 krävs normalt inget bygglov för fasadändringar på en- och tvåbostadshus, men i Bromma är undantagen många.",
       "Staden skriver att bygglov krävs om åtgärden görs på en byggnad eller inom ett bebyggelseområde som är särskilt kulturhistoriskt värdefullt, eller om detaljplanen eller områdesbestämmelserna har skydd för särskilda värden. Stadsmuseets klassificeringskarta ger en första indikation, men staden påpekar att du kan behöva kontakta Stadsmuseet för en bedömning. Detaljplanen finns i e-tjänsten Bygg- och plantjänsten.",
       "Det enklaste beslutet är ofta att lägga nytt lertegel av samma typ som det gamla. Då uppstår ingen lovfråga, och huset behåller sitt uttryck. Vill du byta till betong eller plåt går vi igenom klassningen och detaljplanen innan något beställs. Skillnaderna mellan materialen finns i " + _L.format("tegel-betong-plattak.html", "tegel, betong eller plåt") + ".",
     ],
     "aside": {"title": "Underhåll eller ändring", "items": [
       "Samma material och utförande: underhåll", "Tegel till plåt: fasadändring",
       "Värdefull byggnad eller miljö: bygglov", "Skydd i detaljplanen: bygglov"]}},
    {"id": "solceller-bromma", "h2": "Solceller på det nya taket kräver ofta bygglov",
     "paras": [
       "Stockholms stad skriver att det krävs bygglov för solceller på en byggnad inom eller i anslutning till Försvarsmaktens riksintresse i ett område med detaljplan, och att det därför behövs bygglov i stora delar av Stockholm. En anledning är riksintresset för väderradarn i Håtuna. Enligt Boverket gäller undantaget för anläggningar på högst 11 kilowatt inte när det finns en utökad lovplikt.",
       "Därför lönar det sig att bestämma sig före takbytet. Ska panelerna upp inom några år kan infästningarna planeras medan läkt och underlag ändå är frilagda, och ansökan kan skickas in under tiden. Staden hänvisar till Stockholms solkarta för en första uppskattning av hur mycket el taket kan ge, och till energi- och klimatrådgivningen.",
       "Skatteverket påpekar att du inte kan få rotavdrag för en solcellsinstallation som redan har gett skattereduktion för grön teknik. Själva takbytet ger rotavdrag på vanligt sätt. Mer om paneler på villatak finns under " + _L.format("solceller-tak.html", "solceller på taket") + ".",
     ],
     "aside": None},
    {"id": "utforande-bromma", "h2": "Ett takbyte på en tät småstugegata",
     "paras": [
       "Småstugorna står tätt, i grupper av hus av samma typ, ofta i gatuliv eller bakom förgårdsmark med häckar. Det styr var ställning, container och nya pannor kan stå. Vi planerar etableringen vid platsbesöket, så att häckar och förgårdsmark skonas och grannarna vet hur länge ställningen står.",
       "Under bytet hålls huset tätt varje kväll. När det gamla teglet är nere syns råsponten i dagsljus, och skadade brädor byts innan ny underlagspapp och läkt läggs. Plåten runt skorstenen, ränndalarna och fotplåten görs om, och " + _L.format("hangrannor-stupror.html", "hängrännor och stuprör") + " byts om de är lika gamla som taket.",
       "Kontoret på Byggmästarvägen i Bromma gör det nära till platsbesök och uppföljning. Våra övriga tjänster i stadsdelen finns under " + _L.format("taklaggare-bromma.html", "takläggare i Bromma") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Bromma till",
  "steps": [
    ("Platsbesök", "Vi går igenom taket, vinden och skorstenen och noterar pannornas typ och kulör."),
    ("Klassning och plan", "Stadsmuseets karta och detaljplanen kontrolleras innan materialet väljs."),
    ("Materialval", "Samma tegel igen eller ett annat material, och om solceller ska förberedas."),
    ("Kostnadsförslag", "Rivning, underlag, pannor, plåt och ställning står var för sig i ett skriftligt förslag."),
    ("Takbyte", "Gammalt tak rivs, råsponten ses över och nytt underlag, läkt och nya pannor läggs."),
    ("Slutgenomgång", "Vi går igenom taket och plåtdetaljerna tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Bromma",
  "rot": [
    "Skatteverket räknar det som rotarbete att byta och reparera takpannor, plåttak och hängrännor på ett småhus, liksom att montera och montera ner byggnadsställningar och att byggstäda efter arbetet. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material, resor och bortforsling ger inget avdrag.",
    "Du behöver äga huset medan arbetet utförs och bo i det. Geal drar av ROT direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden för takbytet i Bromma",
  "price": [
    "Takets yta och lutning, om nytt lertegel av samma typ ska läggas eller ett annat material, hur mycket råspont som behöver bytas, plåtarbetena kring skorsten och kupor, hur ställningen kan stå på en trång tomt och om infästningar för solceller ska förberedas. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ", och efter platsbesöket får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi byta lertegel mot betongpannor på vår småstuga i Norra Ängby?",
     "Ett byte till ett annat taktäckningsmaterial är en fasadändring. Är huset eller området klassat som särskilt värdefullt, eller skyddar detaljplanen särskilda värden, krävs bygglov. Kontrollera Stadsmuseets karta och detaljplanen först."),
    ("Var finns ritningar som visar hur taket på en Brommasmåstuga såg ut från början?",
     "Stadsbyggnadskontoret samlade typritningarna från 1927–1957 i en sammanställning. Staden hänvisar också till äldre miljöprogram och typritningssamlingar som går att beställa."),
    ("Behöver vi bygglov för solceller efter takbytet i Bromma?",
     "Ofta ja. Staden kräver bygglov för solceller inom detaljplan i eller i anslutning till Försvarsmaktens riksintresse, vilket berör stora delar av Stockholm, bland annat på grund av väderradarn i Håtuna."),
    ("Räknas det som underhåll om vi lägger samma sorts tegel igen?",
     "Ja, enligt Boverket är ett byte till samma material i samma utförande underhåll och inte en fasadändring. Ändringen ska ändå göras varsamt."),
    ("Kan vi få både rotavdrag och grön teknik för solcellerna på det nya taket?",
     "Inte för samma installation, enligt Skatteverket. Arbetet med själva takbytet ger däremot rotavdrag."),
  ],
  "sources": [
    ("Stockholms stad – Fasadändring (bygglov.stockholm)",
     "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/fasadandring/"),
    ("Stockholms stad – Solceller, solpanel, solfångare (bygglov.stockholm)",
     "https://bygglov.stockholm/nar-behovs-bygglov/andra-byggnads-yttre-utseende/solceller-solpanel-solfangare/"),
    ("Stockholms stad – Varsam utveckling av småhus- och villaområden, strategi med vägledningar (pdf)",
     "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf"),
    _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska taket på Brommahuset bytas?", "Boka ett gratis platsbesök så går vi igenom taket, materialet och lovfrågan."),
  "img": [
    ("Rad av småstugor i Bromma med branta sadeltak i rött lertegel och ljus träpanel",
     "row of small 1930s Swedish one-and-a-half storey wooden cottages with steep gable roofs of red single-roll clay tiles, light grey and pale green vertical board-and-batten facades, low hedges and front gardens, garden suburb Norra Ängby Bromma Stockholm, late summer daylight"),
    ("Takbyte på ett mindre trähus – nytt underlag på ena takfallet, gamla tegelpannor kvar på det andra",
     "roof replacement in progress on a small Swedish wooden house: one roof slope stripped with new black underlayment felt and fresh pale wooden battens, the other slope still covered with old red clay tiles, a neat stack of old tiles on the scaffolding, nobody on the roof, overcast daylight"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ DANDERYD
"takbyte-danderyd.html": {
  "kind": "district", "service": "takbyte", "ort": "Danderyd", "svc_label": "Takbyte",
  "title": "Takbyte i Danderyd – villastaden, takmaterial och solceller",
  "description": "Takbyte i Danderyd: kulturmiljöhandboken om takmaterial, villorna i Gamla Djursholm, när ett nytt tak kräver lov och varför solceller kräver bygglov.",
  "h1": "Takbyte i Danderyd",
  "lead": "I Djursholm och andra delar av Danderyd räknas det ursprungliga takmaterialet till det som ska bevaras, och hela kommunen ligger inom Försvarsmaktens påverkansområde för väderradar. Geal Entreprenad AB byter tak på villor och radhus i hela Danderyd, går igenom kommunens kulturmiljöunderlag innan materialet väljs och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Villastaden, takmaterial och solceller.",
  "sections": [
    {"id": "handboken-danderyd", "anchor": "Kulturmiljöhandboken",
     "h2": "Vad kulturmiljöhandboken säger om takmaterial",
     "paras": [
       "Danderyds kulturmiljöhandbok har områdesblad för de utpekade miljöerna. För samtliga områden anges att stor vikt ska läggas vid att byggnadernas ursprungliga exteriör inte förändras genom byte av till exempel fasadmaterial, fönster, takmaterial eller färgtyp och kulör, och att underhållet sker varsamt med traditionella material och metoder.",
       "Handboken lyfter också fram värdet av de ursprungliga materialen, som med sin ålder och patina berättar om byggnadernas historia, äldre hantverksskicklighet och byggnadsteknik. För ett takbyte betyder det att ett gammalt tegel- eller plåttak inte självklart ska ersättas med något annat, och att hela pannor kan vara värda att lägga tillbaka.",
       "Kommunens riktlinjer från 2024 pekar åt samma håll. Där uppmanas fastighetsägaren att söka på sin adress i kulturmiljökartan för att se om fastigheten är utpekad och vilken arkitekturstil huset tillhör. Riktlinjerna påminner om att byggnader enligt plan- och bygglagen ska hållas i vårdat skick och underhållas så att utformning och tekniska egenskaper i huvudsak bevaras.",
     ],
     "aside": {"title": "Handbokens råd", "items": [
       "Den ursprungliga exteriören behålls", "Takmaterial byts inte i onödan",
       "Traditionella material och metoder", "Patina har ett eget värde"]}},
    {"id": "gamla-djursholm", "h2": "Gamla Djursholm: villor från 1890 till 1960-tal",
     "paras": [
       "Bladet för Gamla Djursholm beskriver kvarteren Delling och Gamla Djursholm vid Stora Värtans strand, där några av Djursholms arkitekturhistoriskt mest intressanta villor ligger. De spänner i ålder från 1890 till 1960-tal: en stor brunmålad trävilla från 1890-talet, en medeltidsromantisk tegelvilla, en putsad klassicistisk villa från 1920-talet och en nästan brutalistisk betongvilla.",
       "Området räknas som särskilt värdefullt och är riksintresse för kulturmiljövården. Husen har inventerats och delats in i tre klasser: omistlig, värdefull och intressant. För de omistliga ska förändringar göras med mycket stor hänsyn till byggnadens egenart, och tre fastigheter i kvarteret Delling har dessutom skyddsbestämmelser i detaljplanen.",
       "Exemplet visar varför ett takbyte i Djursholm börjar med husets klass och planens bestämmelser. Fyra villor på samma strandväg kan behöva fyra helt olika tak. Takens epoker och renovering i kommunen beskrivs under " + _L.format("takrenovering-danderyd.html", "takrenovering i Danderyd") + ".",
     ],
     "aside": {"title": "Inventeringens klasser", "items": [
       "Omistlig: mycket stor hänsyn", "Värdefull: stor varsamhet", "Intressant: skyddad genom området"]}},
    {"id": "lov-danderyd", "h2": "Nytt tak utan lov – och när lov ändå krävs",
     "paras": [
       "På sidan om de nya reglerna från 1 december 2025 svarar kommunen att fasadändringar som ommålning, nytt tak eller fönster inte kräver bygglov på en- och tvåbostadshus. Ändringarna ska ändå göras varsamt och anpassas till byggnadens värden. Lov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller riksintresse för kulturmiljövården, eller om byggnaden själv är särskilt värdefull.",
       "Boverket skiljer mellan underhåll och ändring. Att lägga samma material i samma utförande är underhåll, medan ett byte från tegeltak till plåttak är en fasadändring. Den som vill ha ett beslut på att åtgärden uppfyller lagens krav kan enligt kommunen söka ett frivilligt bygglov, även när lov inte krävs.",
       "Grupphusen har egna riktlinjer. För grupphusbebyggelsen i Danderyd anges att områdenas enhetliga karaktär mot gatan ska bibehållas och att äldre material och byggnadsdetaljer ska värnas vid renovering och ombyggnad. Byter ett hus i gruppen till en annan panna eller kulör bryts den helheten.",
     ],
     "aside": None},
    {"id": "solceller-danderyd", "h2": "Solceller kräver bygglov i hela Danderyd",
     "paras": [
       "Enligt kommunen ligger hela Danderyd inom Försvarsmaktens påverkansområde för väderradar. Därför krävs bygglov för solceller inom detaljplanerade områden, även när åtgärden annars skulle vara bygglovsbefriad. Kommunens solkarta visar hur mycket solinstrålning ett tak tar emot.",
       "Planerar du solceller är takbytet rätt tillfälle att bestämma placering och infästning, och ansökan kan förberedas medan taket läggs. I en värdefull miljö spelar placeringen roll, eftersom panelerna påverkar husets uttryck mot gatan. Mer om paneler på villatak finns under " + _L.format("solceller-tak.html", "solceller på taket") + ".",
       "Kommunen erbjuder kostnadsfri energi- och klimatrådgivning om solenergi. Skatteverket påminner om att samma solcellsinstallation inte kan ge både rotavdrag och skattereduktion för grön teknik, medan arbetet med själva taket ger rotavdrag enligt reglerna nedan.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Danderyd till",
  "steps": [
    ("Platsbesök", "Vi bedömer tak, underlag och plåt och noterar material, kulör och detaljer som ska bevaras."),
    ("Kulturmiljökartan", "Vi kontrollerar om fastigheten är utpekad och vad detaljplanen säger."),
    ("Material och lov", "Samma material igen, eller ett annat material med bygglov om det krävs."),
    ("Kostnadsförslag", "Rivning, underlag, pannor eller plåt, plåtdetaljer och ställning redovisas var för sig."),
    ("Takbyte", "Det gamla taket tas ner, hela pannor sorteras ut och nytt underlag och ny läkt läggs."),
    ("Genomgång", "Vi går igenom det färdiga taket och detaljerna tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Danderyd",
  "rot": [
    "Att byta och reparera takpannor, plåttak och hängrännor på ett småhus är rotarbete enligt Skatteverket, och det gäller även ställningsarbete och byggstädning i samband med arbetet. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material, resor och bortforsling ger inget avdrag.",
    "Du behöver äga villan när arbetet utförs och använda den som bostad. Avdraget görs direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden för takbytet i Danderyd",
  "price": [
    "Takets yta, lutning och form med torn, kupor och brutna takfall, om hela pannor ska läggas tillbaka, om ett traditionellt material krävs, hur mycket plåtarbete som ingår och hur ställningen kan stå på en kuperad tomt. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter platsbesöket får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur vet vi om vår villa i Djursholm är klassad som omistlig eller värdefull?",
     "Klassningen står i kulturmiljöhandbokens blad för området. Sök också på adressen i kommunens kulturmiljökarta, och kontakta kommunen om du är osäker."),
    ("Får vi byta ett gammalt plåttak mot tegel på en villa i Danderyd?",
     "Ett byte till ett annat taktäckningsmaterial är en fasadändring. Ligger huset i ett särskilt värdefullt område eller riksintresse, eller är det särskilt värdefullt, krävs bygglov."),
    ("Varför krävs bygglov för solceller överallt i Danderyd?",
     "Hela kommunen ligger inom Försvarsmaktens påverkansområde för väderradar. Inom detaljplan krävs därför bygglov för solceller."),
    ("Gäller kommunens riktlinjer också för grupphus och radhus i Danderyd?",
     "Ja, grupphusbebyggelsen har egna riktlinjer där enhetligheten mot gatan och äldre material och detaljer ska värnas vid renovering."),
    ("Vad ger ett frivilligt bygglov när vi byter tak i Danderyd?",
     "Ett beslut från byggnadsnämnden på att åtgärden uppfyller lagens krav, även om lov inte behövs. Det kan vara tryggt i en känslig miljö."),
  ],
  "sources": [
    ("Danderyds kommun – Nya regler för bygglov från 1 december 2025",
     "https://www.danderyd.se/bygga-bo-och-miljo/bygga-andra-riva/nya-regler-for-bygglov-fran-1-december-2025/"),
    ("Danderyds kommun – Solenergi och solceller",
     "https://www.danderyd.se/bygga-bo-och-miljo/energi/solenergi-och-solceller/"),
    ("Danderyds kommun – Riktlinjer för kulturmiljöhistoriska byggnader och miljöer i Danderyd (2024, pdf)",
     "https://www.danderyd.se/globalassets/globala-filer/kommun-och-politik/ovriga-styrdokument-ny/styrande-dokument---samhallsbyggnad-miljo-och-exploatering/riktlinjer-for-kulturmiljohistoriska-byggnader-och-miljoer-i-danderyd-2024.pdf"),
    ("Danderyds kommun – Kulturmiljöhandboken, B46 Gamla Djursholm (pdf)",
     "https://sync.danderyd.se/globalassets/globala-filer/bygga-bo-och-miljo/bygglov/kulturmiljohandboken/b46-gamla-djursholm.pdf"),
    _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska taket på villan i Danderyd bytas?", "Boka ett gratis platsbesök så går vi igenom taket, kulturmiljön och materialvalet."),
  "img": [
    ("Äldre villa i Danderyd med brant tak i falsad plåt och två kupor nära vattnet",
     "large late 1800s Swedish wooden villa with light ochre painted horizontal panel and white trim, steep roof covered entirely in dark grey standing-seam sheet metal with clearly visible vertical seams, two dormers, tall old oaks, glimpse of a calm bay, Djursholm Danderyd, early autumn daylight"),
    ("Hela tegelpannor staplade på en ställning bredvid ett takfall med ny läkt",
     "old red clay roof tiles stacked upright in neat rows on a scaffolding platform at the eaves of a Swedish villa, next to them a roof slope with black underlayment and new horizontal wooden battens ready for tiling, no people, soft overcast daylight"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HUDDINGE
"takbyte-huddinge.html": {
  "kind": "district", "service": "takbyte", "ort": "Huddinge", "svc_label": "Takbyte",
  "title": "Takbyte i Huddinge – tyngre tak, stugor och landsbygd",
  "description": "Takbyte i Huddinge: samma material och färg utan lov, när ett tyngre tak kräver anmälan, takvinkeln på fritidshusen och teglet på landsbygdens gårdar.",
  "h1": "Takbyte i Huddinge",
  "lead": "Huddinge rymmer allt från gårdar och torp på landsbygden till fritidshusområden från 1950–80-talet och tätt bebyggda villakvarter. Vid ett takbyte här styr kommunens regler om samma material och samma färg, och om det nya taket blir tyngre än det gamla. Geal Entreprenad AB byter tak i hela Huddinge och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Tyngre tak, stugor och landsbygd.",
  "sections": [
    {"id": "regler-huddinge", "anchor": "Kommunens regler",
     "h2": "Samma material och samma färg – eller en fasadändring",
     "paras": [
       "Huddinge kommun räknar byte av kulör, fasadmaterial och taktäckningsmaterial som en fasadändring. På sidan Ändra fasad eller tak skriver kommunen att du inte behöver bygglov för att byta tak om du byter befintligt material till samma sorts material med samma färg. En- och tvåbostadshus kan också ändra utseende utan lov, så länge byggnaden eller området inte är kulturhistoriskt värdefullt.",
       "Lov krävs däremot om huset eller området är kulturhistoriskt värdefullt, och ingenting blir lovfritt om detaljplanen säger att bygglov behövs. Kommunen understryker att lagens krav gäller även utan lov: ändringen ska utföras varsamt och byggnaden ska passa in i omgivningen. Den som vill ha ett skriftligt besked kan söka frivilligt lov, som handläggs som en vanlig ansökan.",
       "Söker du lov för ett nytt takmaterial vill kommunen ha en situationsplan, där en gratis tomtkarta kan användas för att markera byggnaden, och en fasadritning. Vilka miljöer kulturmiljöprogrammet pekar ut beskrivs under " + _L.format("takrenovering-huddinge.html", "takrenovering i Huddinge") + ".",
     ],
     "aside": {"title": "Utan lov enligt kommunen", "items": [
       "Samma sorts material", "Samma färg", "Inga kulturvärden i hus eller område",
       "Ingen lovplikt i detaljplanen"]}},
    {"id": "vikt-huddinge", "h2": "När det nya taket väger mer än det gamla",
     "paras": [
       "Även när bygglov inte behövs kan ett takbyte kräva en anmälan. Kommunen skriver att du behöver skicka in en anmälan och få startbesked om ändringen innebär att byggnadens bärande delar påverkas väsentligt. Samma sak gäller en solenergianläggning som påverkar den bärande konstruktionen.",
       "Det blir aktuellt när ett lätt tak ersätts med ett tyngre, till exempel när plåt eller papp byts mot betong- eller tegelpannor, eller när solpaneler ska ligga ovanpå de nya pannorna. Takstolarna dimensionerades för det tak som lades från början. Vi tittar på takstolarnas dimensioner och skick vid besöket, och vid ett byte till ett tyngre tak behöver en konstruktör bedöma lasten innan något beställs.",
       "Boverket beskriver att snölasten på ett tak påverkas av takets form och av förhållandena på platsen, bland annat snöras från närliggande tak, snödrift och upprepad upptining och frysning. På en kuperad skogstomt blir snön gärna liggande på ett skuggat takfall. Snörasskydd och takstege ses över i samma omgång, se " + _L.format("taksakerhet-snorasskydd.html", "taksäkerhet och snörasskydd") + ".",
     ],
     "aside": {"title": "Taket blir tyngre när", "items": [
       "Plåt eller papp byts mot pannor", "Solpaneler läggs ovanpå pannorna",
       "Snö samlas på ett skuggat takfall", "Anmälan om bärande delar påverkas väsentligt"]}},
    {"id": "fritidshus-huddinge", "h2": "Fritidshusområdena och takvinkeln",
     "paras": [
       "Kulturmiljöprogrammet beskriver fritidshusområdena från 1950–80-talet som sammanhållna miljöer med en planerad gatustruktur. Stugorna är monteringsfärdiga fritidshus i ett plan med liggande fjällpanel och sadeltak, placerade en bit upp på tomten i kuperad terräng med blandskog.",
       "Programmets råd är att fasadmaterial, volym och takvinkel bör värnas. Ett takbyte är därför inte rätt tillfälle att höja taket eller ändra lutningen, även om stugan har blivit ett åretruntboende. En takkupa räknas som en tillbyggnad, och kommunen skriver att alla takkupor, oavsett om de kräver lov, ska ha god gestaltning och passa till byggnaden och området.",
       "För de äldre sportstugeområdena från 1920–50-talet betonar programmet att stugorna bör behålla små volymer och att tillägg ska vara läsbara. Där är ofta det enklaste taket det rätta: samma lutning, samma takfot och ett material som passar stugans skala.",
     ],
     "aside": None},
    {"id": "landsbygd-huddinge", "h2": "Gårdar och torp på Huddinges landsbygd",
     "paras": [
       "Programmets råd för landsbygden utgår från en äldre byggnadstradition med träfasad och sadeltak eller brutna sadeltak täckta med tegel. Som exempel visas en torpmiljö vid Sundby gård, en parstuga med röda fasader och tegeltäckt sadeltak, och huvudbyggnaden på Balingsta med brutet sadeltak täckt med tegel.",
       "Enligt programmet är tegeltäckta tak det vanligaste på landsbygden, men vass, plåt och sedum kan vara aktuella i vissa miljöer. Råden gäller hela landsbygden, även utanför de utpekade kulturmiljöområdena, och programmet påminner om att all bebyggelse omfattas av varsamhetskraven i plan- och bygglagen.",
       "Ska solceller upp efter takbytet krävs bygglov enligt kommunen bland annat om fastigheten ligger inom detaljplan i eller i anslutning till ett riksintresse för totalförsvaret, eller om byggnaden eller miljön har kulturvärden. Mer om paneler finns under " + _L.format("solceller-tak.html", "solceller på taket") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Huddinge till",
  "steps": [
    ("Platsbesök", "Vi bedömer tak, takstolar och vind och noterar material, färg och takvinkel."),
    ("Regler och plan", "Detaljplan och kulturmiljöprogram kontrolleras, och vi ser om bytet kan kräva anmälan."),
    ("Materialval", "Samma material och färg, eller ett annat material med lov och lastbedömning."),
    ("Kostnadsförslag", "Rivning, underlag, ytskikt, plåt och ställning redovisas var för sig."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs, och huset hålls tätt varje kväll."),
    ("Genomgång", "Vi går igenom taket, avvattningen och taksäkerheten med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Huddinge",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor, plåttak, hängrännor och stuprör på ett småhus som rotarbete, och även att sätta upp och ta ner byggnadsställningar och byggstäda efteråt. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material, resor och bortforsling räknas inte.",
    "Du behöver äga huset medan arbetet pågår och använda det som bostad. Geal drar av ROT direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden för takbytet i Huddinge",
  "price": [
    "Takets yta och lutning, om samma material läggs igen eller ett tyngre material väljs, om takstolarna behöver förstärkas, mängden plåtarbete, hur ställningen kan stå på en sluttande tomt och om flera byggnader på en gård ska få nytt tak. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter platsbesöket får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi bygglov om vi lägger samma sorts pannor i samma färg på huset i Huddinge?",
     "Nej, enligt kommunen krävs inget lov för att byta till samma sorts material med samma färg, så länge detaljplanen inte kräver lov och huset eller området inte har kulturvärden."),
    ("Måste vi göra en anmälan om plåttaket byts mot betongpannor?",
     "Ja, om bytet innebär att byggnadens bärande delar påverkas väsentligt. Då krävs anmälan och startbesked, och en konstruktör behöver bedöma om takstolarna klarar den nya lasten."),
    ("Får vi höja taket på vår fritidsstuga i Huddinge när det ändå byts?",
     "Kulturmiljöprogrammet råder att takvinkel och volym på fritidshusen bör värnas. En höjning kan dessutom räknas som tillbyggnad, så stäm av med kommunen först."),
    ("Vilket takmaterial passar ett torp på Huddinges landsbygd?",
     "Enligt kulturmiljöprogrammet är tegel det vanligaste på landsbygden, medan vass, plåt och sedum kan passa i vissa miljöer."),
    ("Kan vi sätta solceller på det nya taket utan bygglov i Huddinge?",
     "Bara om alla kommunens villkor är uppfyllda, bland annat att fastigheten inte ligger inom detaljplan i eller nära ett riksintresse för totalförsvaret och att hus och miljö saknar kulturvärden."),
  ],
  "sources": [
    ("Huddinge kommun – Ändra fasad eller tak",
     "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/fasadandring"),
    ("Huddinge kommun – Solceller, solfångare och solpaneler",
     "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/solceller-och-solfangare"),
    ("Huddinge kommun – Takkupa",
     "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/takkupor"),
    ("Huddinge kommun – Kulturmiljöprogram del 2 (pdf)",
     "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf"),
    _BV_SNO, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska taket i Huddinge bytas?", "Boka ett gratis platsbesök så går vi igenom taket, takstolarna och reglerna."),
  "img": [
    ("Rött trähus med tegeltäckt sadeltak på en gård i Huddinges odlingslandskap",
     "traditional falu red Swedish wooden farmhouse with white corners and a bright red clay tile gable roof with clearly visible rows of curved red tiles, small red outbuilding with corrugated metal roof, open meadow and mixed forest on a hill behind, rural Huddinge south of Stockholm, summer daylight"),
    ("Takstolar och råspont på en vind inför byte till tyngre takmaterial",
     "interior of a cold attic in a 1960s Swedish house: wooden roof trusses and old roof boarding visible in daylight from a small gable window, a folding ruler resting on one truss, dust and old insulation on the floor, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ NORRTÄLJE
"takbyte-norrtalje.html": {
  "kind": "district", "service": "takbyte", "ort": "Norrtälje", "svc_label": "Takbyte",
  "title": "Takbyte i Norrtälje – kust, snö och Roslagens tak",
  "description": "Takbyte i Norrtälje: Roslagens traditionella taktäckning, vind och snö vid kusten, kommunens kartor över värdefulla områden och ROT för fritidshuset.",
  "h1": "Takbyte i Norrtälje",
  "lead": "Norrtälje kommun har många riksintresseområden för kulturmiljövården, och många hus står öppet mot havet. Vid ett takbyte här väger både vind, snö och lokal byggtradition in i valet av material. Geal Entreprenad AB byter tak i Norrtälje med omnejd och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Kust, snö och Roslagens tak.",
  "sections": [
    {"id": "tradition-norrtalje", "anchor": "Roslagens tak",
     "h2": "Spån, enkupigt tegel och plåt i Roslagens byggtradition",
     "paras": [
       "Norrtälje kommun beslutade 2011 att göra kulturhistoriska utredningar av flertalet av kommunens riksintresseområden för kulturmiljövården, både som beslutsunderlag och för att informera allmänheten. Utredningarna finns digitalt på kommunens webbplats, och tryckta versioner säljs bland annat på Roslagsmuseet.",
       "Utredningen för Arholma ger en bild av hur taken har sett ut. Taktäckningen var traditionellt ofta tjärat spån på ekonomibyggnader och torp. Senare kom det enkupiga teglet på bostadshusen, medan plåt och tvåkupigt tegel blev vanligast på ekonomibyggnaderna. Järnplåt och lertegel var dyrt och hörde till herrgårdarna fram till 1900-talet.",
       "Utredningens råd är att taktäckningen väljs med hänsyn till lokal tradition och byggnadens funktion. Den visar också hur lätt det gamla försvinner: på Arholma kyrka har de tegelbelagda taken bytts mot plåt, medan exteriören i övrigt är i stort sett oförändrad. Hur husen i kommunen ser ut i stort beskrivs under " + _L.format("taklaggare-norrtalje.html", "takläggare i Norrtälje") + ".",
     ],
     "aside": {"title": "Enligt Arholmautredningen", "items": [
       "Tjärat spån på uthus och torp", "Enkupigt tegel på bostadshus",
       "Plåt och tvåkupigt tegel på ekonomibyggnader", "Järnplåt och lertegel hörde till herrgårdarna"]}},
    {"id": "vind-norrtalje", "h2": "Vind och snö bestämmer infästningen",
     "paras": [
       "Boverkets vägledning om vindlast delar in terrängen i typer. Den mest utsatta, terrängtyp 0, är havs- eller kustområde exponerat för öppet hav, och därefter kommer sjö eller plant område utan hinder. Ett hus på en udde i Roslagen står alltså i den terräng där vinden tar i mest, medan ett hus i skogen inåt land är bättre skyddat.",
       "För snö finns en ny karta över snölast på mark. Underlaget är framtaget av SMHI från mätdata och modellering av årsmaxima 1961–2020 och har bearbetats av Boverket till zoner, som går att se i Boverkets karttjänst. Snölasten på själva taket beror dessutom på takets form, snödrift av vind, snöras från närliggande tak och upprepad upptining och frysning.",
       "För ett takbyte betyder det att pannor, nock och plåt fästs för det läge huset faktiskt har, och att snörasskydd sätts där snön glider ner mot entré och gångar. Vid platsbesöket noterar vi hur huset står mot vind och väderstreck och tar med det i förslaget, se även " + _L.format("taksakerhet-snorasskydd.html", "taksäkerhet och snörasskydd") + ".",
     ],
     "aside": {"title": "Det som påverkar lasten", "items": [
       "Läge mot öppet hav", "Snözon enligt Boverkets karta", "Snödrift och snöras",
       "Upptining och frysning"]}},
    {"id": "lov-norrtalje", "h2": "Kommunens kartor före materialvalet",
     "paras": [
       "Enligt Boverket är ett byte till ett annat taktäckningsmaterial en fasadändring, medan samma material i samma utförande är underhåll. Sedan 1 december 2025 krävs normalt inget bygglov för fasadändringar på en- och tvåbostadshus, men utökad lovplikt gäller vid särskilt värdefulla byggnader och områden. Norrtälje kommun hänvisar till sin karta, där du kan se om fastigheten ligger inom detaljplan, inom ett särskilt värdefullt område eller inom riksintresse för totalförsvaret.",
       "I samma karta finns bevarandeprogrammet för Norrtälje stad, så för ett äldre hus i staden är det första stället att titta innan pannor eller plåt beställs. Utanför detaljplan kan prövningen enligt kommunen påverkas av riksintressen för bland annat kulturmiljövård, naturvård och friluftsliv.",
       "Kommunen ger allmän rådgivning men bedömer inte enskilda åtgärder via e-post eller telefon. Vill du ha ett bindande besked kan du söka frivilligt bygglov. En ändring av byggnadens konstruktion kan dessutom vara anmälningspliktig, något som blir aktuellt om ett tyngre tak ska läggas. Mer om reglerna finns i " + _L.format("bygglov-takbyte.html", "bygglov vid takbyte") + ".",
     ],
     "aside": None},
    {"id": "fritidshus-norrtalje", "h2": "När sommarhuset ska bli ett åretruntboende",
     "paras": [
       "Ett hus som byggdes för sommarbruk har ofta ett enklare tak än en villa. När huset ska bebos och värmas året runt ändras förutsättningarna för både vinden och taket. Boverkets formel för snölast har till exempel en termisk koefficient som beror på energiförlusterna genom taket.",
       "Vid ett takbyte kan " + _L.format("vindsisolering.html", "tilläggsisolering av vinden") + " och ventilationen samordnas, men isoleringen får inte stänga luftspalten vid takfoten. Byts ett " + _L.format("papptak.html", "papptak") + " mot pannor blir taket dessutom tyngre, så takstolarna behöver bedömas innan materialet väljs.",
       "Rotavdraget gäller enligt Skatteverket även för ett hus som du själv använder som fritidsbostad, så länge du äger det medan arbetet utförs. Det gör att ett takbyte på sommarhuset ger avdrag på samma sätt som på villan.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Norrtälje till",
  "steps": [
    ("Platsbesök", "Vi bedömer tak, takstolar och vind och noterar hur huset står mot vind och väderstreck."),
    ("Kartor och regler", "Detaljplan, värdefulla områden och bevarandeprogram kontrolleras i kommunens karta."),
    ("Materialval", "Material efter husets tradition och läge, och lastbedömning om taket blir tyngre."),
    ("Kostnadsförslag", "Rivning, underlag, ytskikt, plåt, infästning och ställning står var för sig."),
    ("Takbyte", "Gammalt tak rivs, nytt underlag och nytt tak läggs, och huset hålls tätt varje kväll."),
    ("Genomgång", "Vi går igenom taket, snörasskyddet och plåtdetaljerna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Norrtälje",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor, plåttak och hängrännor på ett småhus som rotarbete, och även ställningsarbete och byggstädning i samband med arbetet. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material, resor och bortforsling ger inget avdrag.",
    "Du ska äga huset när arbetet utförs och använda det som permanentbostad eller fritidsbostad. Geal drar av ROT direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden för takbytet i Norrtälje",
  "price": [
    "Takets yta och lutning, val av material, om takstolarna behöver förstärkas för ett tyngre tak, hur utsatt läget är för vind, mängden plåt och snörasskydd, och hur materialet tar sig till huset, till exempel på en ö eller en smal skogsväg. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter platsbesöket får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilket takmaterial är traditionellt på äldre hus i Roslagen?",
     "Enligt kommunens utredning för Arholma var tjärat spån vanligt på ekonomibyggnader och torp, enkupigt tegel kom senare på bostadshusen och plåt och tvåkupigt tegel på ekonomibyggnaderna."),
    ("Var ser vi om vårt hus ligger i ett särskilt värdefullt område i Norrtälje?",
     "I kommunens karta, där även detaljplaner, riksintresse för totalförsvaret och bevarandeprogrammet för Norrtälje stad finns."),
    ("Behöver ett tak vid havet i Roslagen fästas på ett annat sätt?",
     "Boverket räknar kustområden som är exponerade för öppet hav som den mest utsatta terrängtypen för vind. Pannor, nock och plåt behöver därför fästas efter husets läge."),
    ("Får vi rotavdrag för takbyte på vårt fritidshus i Norrtälje?",
     "Ja, om du äger huset och själv använder det som fritidsbostad, enligt Skatteverkets regler."),
    ("Kan kommunen svara i telefon om vårt takbyte i Norrtälje kräver lov?",
     "Kommunen ger allmän rådgivning men bedömer inte enskilda åtgärder via e-post eller telefon. För ett bindande besked kan du söka frivilligt bygglov."),
  ],
  "sources": [
    ("Norrtälje kommun – Lovbefriade åtgärder",
     "https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/lovbefriade-atgarder/"),
    ("Norrtälje kommun – Skillnad mellan bygglovspliktiga, anmälningspliktiga och bygglovsbefriade åtgärder",
     "https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/skillnad-mellan-atgarder/"),
    ("Norrtälje kommun – Riksintresseområden för kulturmiljövården",
     "https://www.norrtalje.se/info/kultur-och-fritid/kultur-och-konst/norrtalje-museerkulturarv-och-stadsarkiv/upptack-kulturarvet/riksintressen/riksintresseomraden/"),
    ("Norrtälje kommun – Kulturmiljöutredning nr 1: Arholma (pdf)",
     "https://www.norrtalje.se/globalassets/dokument/dokument-kultur--fritid/dokument-kultur/dokument-riksintressen-i-norrtalje-kommun/arholma.pdf"),
    _BV_VIND, _BV_SNO, _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska taket i Norrtälje bytas?", "Boka ett gratis platsbesök så går vi igenom taket, läget och materialvalet."),
  "img": [
    ("Rött trähus med svart falsat plåttak på klipporna vid havet i Roslagen",
     "falu red Swedish wooden house with white corners and a black standing-seam metal roof on smooth granite rocks by the open Baltic sea, windswept pines, Roslagen archipelago near Norrtälje, clear autumn day"),
    ("Röda tegelpannor med lav på ett äldre hus i skärgården",
     "close-up of an old roof covered in red single-roll clay tiles with a mortar-free ridge of round ridge tiles, lichen on a few tiles, blue sea and rocky islets out of focus in the background, Swedish archipelago, no people"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SOLLENTUNA
"takbyte-sollentuna.html": {
  "kind": "district", "service": "takbyte", "ort": "Sollentuna", "svc_label": "Takbyte",
  "title": "Takbyte i Sollentuna – ansökan, solceller och radhus",
  "description": "Takbyte i Sollentuna: kommunens besked om nytt takmaterial, handlingarna om lov krävs, solceller som kräver bygglov i hela kommunen och tak på radhus.",
  "h1": "Takbyte i Sollentuna",
  "lead": "Sollentuna kommun har en egen sida om att byta takmaterial, och hela kommunen ligger inom totalförsvarets riksintresseområde. Det gör det tydligt vad som gäller när taket ska bytas – och viktigt att planera eventuella solceller i tid. Geal Entreprenad AB byter tak i hela Sollentuna och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Ansökan, solceller och radhus.",
  "sections": [
    {"id": "takmaterial-sollentuna", "anchor": "Byta takmaterial",
     "h2": "Kommunens besked om att byta takmaterial",
     "paras": [
       "Sollentuna beskriver en fasadändring som att byggnaden byter kulör, fasadbeklädnad eller taktäckningsmaterial, eller att de yttre karaktärsdragen påverkas på annat sätt. På en- och tvåbostadshus krävs det oftast inte bygglov. Bor du i radhus, kedjehus eller ett annat sammanbyggt småhus beror möjligheterna på hur bebyggelsen är utformad, och kommunen ber dig då kontakta kontaktcenter för vägledning.",
       "Bygglov behövs om fastigheten ligger inom ett kulturhistoriskt värdefullt område eller om byggnaden är kulturhistoriskt värdefull. Kommunen skriver att de bygglovsbefriade åtgärderna inte går att tillämpa i sådana områden, och att ett hus kan vara särskilt värdefullt även om det inte finns med i kulturmiljöplanen. Vissa detaljplaner reglerar dessutom hur tak- och fasadmaterial ska vara utförda.",
       "För att få en bedömning kan du skicka in adress eller fastighetsbeteckning, foton på huset från samtliga väderstreck och en beskrivning av vad du vill göra, och kommunen återkopplar med en bedömning. Det är ett enkelt första steg innan pannor eller plåt beställs.",
     ],
     "aside": {"title": "Till kommunens bedömning", "items": [
       "Adress eller fastighetsbeteckning", "Foton från samtliga väderstreck",
       "Beskrivning av det nya taket", "E-postadress för svaret"]}},
    {"id": "ansokan-sollentuna", "h2": "Om lov krävs: handlingarna för ett nytt takmaterial",
     "paras": [
       "Kommunens checklista för bygglov vid byte av takmaterial anger att ansökan görs via e-tjänst och ska innehålla förslag till kontrollplan, situationsplan på en baskarta och fasadritning eller fotomontage. Handläggningstiden anges till ungefär två till fyra veckor.",
       "Fasadritningen ska vara i skala 1:100 och visa både den befintliga fasaden, med fönster, dörrar och takkupor, och den nya fasaden, med en tydlig markering av var ändringen görs. Situationsplanen kan för enklare åtgärder ritas på en tomtkarta i skala 1:400, som går att skriva ut som pdf från kommunens webbplats.",
       "Äldre ritningar på huset kan sökas fram kostnadsfritt i kommunens bygglovsarkiv. Kommunen erbjuder just nu ingen mall för kontrollplan och räknar med att kunna erbjuda den igen under hösten 2026, så till dess tas kontrollplanen fram på egen hand. Vi lämnar uppgifter om material, kulör och utförande som underlag till handlingarna.",
     ],
     "aside": {"title": "Enligt checklistan", "items": [
       "Ansökan via e-tjänst", "Förslag till kontrollplan", "Situationsplan på baskarta",
       "Fasadritning 1:100 eller fotomontage"]}},
    {"id": "solceller-sollentuna", "h2": "Solceller kräver bygglov i hela kommunen",
     "paras": [
       "Enligt kommunen omfattas hela Sollentuna av totalförsvarets riksintresseområde. Därför kräver solceller och solfångare på en byggnad inom detaljplanelagt område bygglov. Utanför detaljplan krävs lov om fastigheten ligger i ett kulturhistoriskt värdefullt område eller om byggnaden är kulturhistoriskt värdefull.",
       "En ansökan om solceller kräver mer än ett materialbyte. Utöver kontrollplan, situationsplan och fasadritning i skala 1:100 vill kommunen ha tillverkarens specifikation av panelerna, i vissa fall en takplan och konstruktionsritningar om den bärande konstruktionen påverkas. Handläggningstiden anges till ungefär fyra till tio veckor.",
       "Anmälan krävs om anläggningen väsentligt påverkar bärande konstruktion eller brandskydd, och kommunen påpekar att ett batterilager på mer än 20 kWh inne i byggnaden kan behöva bli en egen brandcell. Eftersom handläggningen tar längre tid än själva takbytet lönar det sig att söka i god tid, så att infästningarna kan förberedas medan taket ligger öppet. Läs mer under " + _L.format("solceller-tak.html", "solceller på taket") + ".",
     ],
     "aside": None},
    {"id": "radhus-sollentuna", "h2": "Radhus, kedjehus och tilläggsisolering",
     "paras": [
       "I ett sammanbyggt hus är taket en del av hela längan, och kommunen skriver att möjligheterna att göra en fasadändring utan lov beror på hur bebyggelsen är utformad. Byter flera grannar samtidigt blir pannor, kulör och plåtdetaljer desamma, och anslutningen mot grannens tak behöver bara göras en gång.",
       "Kommunen påpekar också att tilläggsisolering kan räknas som en fasadändring, eftersom den kan ändra husets utseende. Isoleras taket från utsidan i samband med bytet kan takfot och vindskivor behöva ändras, så den frågan bör ställas till kommunen tillsammans med frågan om materialet. Mer om isolering finns under " + _L.format("vindsisolering.html", "vindsisolering") + ".",
       "Även när inget lov krävs är du som byggherre ansvarig för att lagen följs, bland annat att ändringen anpassas till byggnadens och områdets karaktär och stämmer med detaljplanen. Vill du ha ett beslut kan du söka frivilligt bygglov. Hur vi arbetar i kommunen i övrigt beskrivs under " + _L.format("taklaggare-sollentuna.html", "takläggare i Sollentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Sollentuna till",
  "steps": [
    ("Platsbesök", "Vi bedömer tak, underlag och vind och tar foton av huset från alla väderstreck."),
    ("Kommunens bedömning", "Vid behov skickas foton och beskrivning till kommunen för ett besked om kulturvärden."),
    ("Material och handlingar", "Material och kulör bestäms, och vi lämnar uppgifter till en eventuell ansökan."),
    ("Kostnadsförslag", "Rivning, underlag, ytskikt, plåt och ställning redovisas var för sig."),
    ("Takbyte", "Gammalt tak rivs, nytt underlag och nytt tak läggs, och huset hålls tätt varje kväll."),
    ("Genomgång", "Vi går igenom taket och detaljerna med dig och grannarna i längan."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Sollentuna",
  "rot": [
    "För ett småhus räknar Skatteverket det som rotarbete att byta och reparera takpannor, plåttak och hängrännor, och även att montera och montera ner byggnadsställningar och byggstäda efter arbetet. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material, resor och bortforsling ger inget avdrag.",
    "Du behöver äga huset medan arbetet utförs och bo i det. Geal drar av ROT direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden för takbytet i Sollentuna",
  "price": [
    "Takets yta och lutning, val av material och kulör, om flera hus i en länga byter samtidigt, mängden plåt kring kupor och skorstenar, om taket ska tilläggsisoleras och om infästningar för solceller ska förberedas. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter platsbesöket får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur lång tid tar ett bygglov för nytt takmaterial i Sollentuna?",
     "Kommunen anger en handläggningstid på ungefär två till fyra veckor för bygglov vid byte av takmaterial, och just nu något längre eftersom många vill bygga."),
    ("Varför krävs bygglov för solceller överallt i Sollentuna?",
     "Hela kommunen ligger inom totalförsvarets riksintresseområde, och inom detaljplan krävs då bygglov för solceller och solfångare."),
    ("Vilka foton vill Sollentuna kommun ha för att bedöma om huset har kulturvärden?",
     "Foton på fastigheten från samtliga väderstreck, tillsammans med adress eller fastighetsbeteckning och en beskrivning av vad du vill göra."),
    ("Var hittar vi gamla ritningar på vårt hus i Sollentuna?",
     "I kommunens bygglovsarkiv, där äldre ritningar kan sökas fram utan kostnad."),
    ("Räknas tilläggsisolering av taket som en fasadändring i Sollentuna?",
     "Det kan den göra, enligt kommunen, eftersom isoleringen kan ändra husets yttre utseende. Fråga kommunen innan taket byggs på."),
  ],
  "sources": [
    ("Sollentuna kommun – Byta takmaterial",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/byta-takmaterial/"),
    ("Sollentuna kommun – Solceller och solfångare",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/solceller-solfangare/"),
    ("Sollentuna kommun – Kulturhistoriska byggnader och områden",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/kulturmiljoer/"),
    ("Sollentuna kommun – Tilläggsisolera",
     "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/tillaggsisolera/"),
    _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska taket i Sollentuna bytas?", "Boka ett gratis platsbesök så går vi igenom taket, materialet och vad kommunen behöver."),
  "img": [
    ("Radhuslänga i Sollentuna med betongpannor och ljus träpanel bland tallar",
     "row of 1970s Swedish two-storey terraced houses with dark grey concrete tile gable roofs, light brown wooden panel facades, small front gardens and tall pine trees, residential street in Sollentuna north of Stockholm, autumn daylight"),
    ("Radhus i Sollentuna med gamla betongpannor och mossa, mogna för takbyte",
     "slightly elevated view along the roofs of 1970s Swedish two-storey terraced houses with light wooden panel facades: one house has brand new dark grey concrete roof tiles, the neighbouring houses still have old faded grey concrete tiles with some moss, metal flashing at the joint, pine trees behind, no people, overcast"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ TÄBY
"takbyte-taby.html": {
  "kind": "district", "service": "takbyte", "ort": "Täby", "svc_label": "Takbyte",
  "title": "Takbyte i Täby – betongpannor, kedjehus och tegelvillor",
  "description": "Takbyte i Täby: svarta betongpannor i Näsbygård, riktlinjerna om takmaterial och takfot, tegelvillorna i Ensta och de brutna taken vid Roslagsbanan.",
  "h1": "Takbyte i Täby",
  "lead": "Täby har villor och grupphus från 1900-talets början till slutet av 1990-talet, och kommunens kulturmiljöunderlag beskriver taken på många av dem i detalj. Det gör det lättare att välja rätt panna, plåt och kulör när taket ska bytas. Geal Entreprenad AB byter tak i hela Täby och lämnar ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  "card": "Betongpannor, kedjehus och tegelvillor.",
  "sections": [
    {"id": "hagern-taby", "anchor": "Kedjehusen",
     "h2": "Svarta betongpannor och svartmålad plåt i Näsbygård",
     "paras": [
       "Kvarteret Hägern i Näsbygård beskrivs i Kulturmiljöer i Täby som ett enhetligt anlagt småhusområde med småskaliga kvarter och intima gaturum, uppfört 1975–1976. Kedjehusen har bottenvåning i fasadtegel, branta tak med svarta betongpannor, små takkupor inklädda med svartmålad plåt, svartmålade vindskivor och nätta takutsprång. Arkitekturen hämtar inspiration från lantliga byggnadstraditioner.",
       "Kvarteret Tranan från 1998–1999 visar en yngre variant: parhus och enbostadshus i herrgårdsliknande arkitektur med sadeltak och röda betongpannor, där två enbostadshus vid områdets entré har tak av svartmålad bandplåt och små takkupor. Även där är pannornas kulör och kupornas plåt en del av helheten.",
       "I sådana områden handlar ett takbyte om att upprepa det som finns: samma pannform, samma kulör, samma plåt kring kuporna och samma takutsprång. Det är också där en avvikande panna syns tydligast från gatan.",
     ],
     "aside": {"title": "Kvarteret Hägern 1975–76", "items": [
       "Kedjehus med fasadtegel", "Branta tak med svarta betongpannor",
       "Takkupor i svartmålad plåt", "Svarta vindskivor och nätta takutsprång"]}},
    {"id": "riktlinjer-taby", "h2": "Takform, takmaterial och takfot behålls",
     "paras": [
       "Kulturmiljöer i Täby ger riktlinjer både för småhusområden och för grupphusområden. I båda fallen står det att befintliga takformer, takmaterial och takfotens utformning bör bibehållas på befintliga hus och väljas även för tillbyggnader. För grupphusen ska tillägg som carport och altan anpassas genom att undvika avvikande takvinklar och stora kontraster i material.",
       "Kommunens sida om fasadändring anger att det inte behövs bygglov för fasadändringar på en- och tvåbostadshus om byggnaden inte är särskilt värdefull, inte ligger i ett särskilt värdefullt område och inte har utökad lovplikt i detaljplanen. Är du osäker ber kommunen dig kontakta dem för rådgivning. Boverket räknar ett byte till ett annat taktäckningsmaterial som fasadändring, medan samma material i samma utförande är underhåll.",
       "Ett byte från betongpannor till plåt på ett hus i ett värdefullt område kan alltså kräva lov, medan nya betongpannor av samma slag normalt läggs utan. Lovfrågan beskrivs närmare i " + _L.format("bygglov-takbyte.html", "bygglov vid takbyte") + ", och takens skick under " + _L.format("takrenovering-taby.html", "takrenovering i Täby") + ".",
     ],
     "aside": None},
    {"id": "ensta-taby", "h2": "Tegelvillor från efterkrigstiden i Ensta",
     "paras": [
       "Ensta växte fram kring Roslagsbanans hållplats från 1911. Enligt kommunens underlag gjorde 1930-talets styckningsplan för Ensta Villastad att villabyggandet tog fart, och det var särskilt intensivt under 1940–60-talen. Intrycket domineras fortfarande av efterkrigstidens varierade och gedigna tegel- och putsarkitektur, till exempel en villa från 1959 med fasader av gult tegel och tak av brunt glaserat tegel.",
       "Det är inte säkert att samma pannmodell går att få i dag. Vid ett takbyte på ett sådant hus jämför vi därför form, yta och kulör med de pannor som går att beställa, innan något bestäms. Går det att spara hela pannor till de takfall som syns mot gatan kan nya pannor läggas där de syns minst.",
       "Mitt i området ligger Ensta krog, en gästgivargård med ursprung i 1600-talet. Huvudbyggnaden är timrad och har sadeltak täckt med röda tvåkupiga betongpannor, medan den västra flygeln har valmat tak med enkupigt tegel. Underlaget rekommenderar att ett antikvariskt åtgärdsförslag ligger till grund när krogen underhålls.",
     ],
     "aside": None},
    {"id": "brutna-tak-taby", "h2": "Brutna tak vid Roslagsbanans stationer",
     "paras": [
       "I Sågtorp och Mosstorp växte villorna fram från tidigt 1900-tal vid Roslagsbanans stationer, planerade efter trädgårdsstadsideal i kuperad terräng. Enligt underlaget har den äldre bebyggelsen sadeltak eller brutna tak, ibland utkragande nedtill, oftast täckta med tegelpannor eller plåt. Villa Ytterby från 1912 vid Roslags-Näsby station har ett brutet takfall i tegel med utsvängd nedre del.",
       "På ett brutet tak med utsvängd takfot ligger svårigheten i brytningen och svängen. Läkten måste följa formen, pannorna ska ligga tätt i knäcken och plåten vid takfoten ska följa svängen. Vi mäter upp profilen vid besöket, så att det nya taket får samma linje som det gamla.",
       "Ska solceller upp på det nya taket gäller Boverkets undantag för anläggningar på högst 11 kilowatt inte där utökad lovplikt råder, till exempel vid särskilt värdefulla byggnader. Fråga kommunen vad som gäller just din adress innan infästningarna förbereds. Mer om paneler finns under " + _L.format("solceller-tak.html", "solceller på taket") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Täby till",
  "steps": [
    ("Platsbesök", "Vi bedömer tak och underlag och noterar pannform, kulör, kupor och takfot."),
    ("Underlag och plan", "Kulturmiljöunderlaget och detaljplanen kontrolleras för området."),
    ("Matchning", "Nya pannor jämförs med de gamla i form, yta och kulör innan beställning."),
    ("Kostnadsförslag", "Rivning, underlag, pannor, plåt och ställning redovisas var för sig."),
    ("Takbyte", "Gammalt tak rivs, nytt underlag och ny läkt läggs efter takets profil, och huset hålls tätt varje kväll."),
    ("Genomgång", "Vi går igenom taket, kuporna och takfoten tillsammans med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Täby",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor, plåttak och hängrännor på ett småhus som rotarbete, och även att sätta upp och ta ner byggnadsställningar och byggstäda efteråt. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rutavdrag. Material, resor och bortforsling ger inget avdrag.",
    "Du behöver äga huset medan arbetet utförs och bo i det. Avdraget görs direkt på fakturan.",
  ],
  "price_h2": "Det här styr kostnaden för takbytet i Täby",
  "price": [
    "Takets yta, lutning och form, hur många kupor det finns, om pannor ska matchas mot ett äldre tak, om hela pannor kan sparas, plåtarbetena vid takfot och kupor och hur ställningen kan stå. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter platsbesöket får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vilka pannor ska vi välja när kedjehuset i kvarteret Hägern får nytt tak?",
     "Kommunens underlag beskriver svarta betongpannor, takkupor i svartmålad plåt och svarta vindskivor, och riktlinjerna säger att takmaterialet bör behållas. Samma pannform och kulör håller ihop kvarteret."),
    ("Behöver vi bygglov för att byta betongpannor mot plåt i Täby?",
     "Bara om huset är särskilt värdefullt, ligger i ett särskilt värdefullt område eller har utökad lovplikt i detaljplanen. Kontakta kommunen om du är osäker."),
    ("Går det att hitta nya pannor som passar ett glaserat tegeltak från 1950-talet?",
     "Det är inte säkert att samma modell finns kvar. Vi jämför form, yta och kulör med de pannor som går att beställa och föreslår hur hela gamla pannor kan återanvändas där de syns mest."),
    ("Hur byts ett brutet tak med utsvängd takfot på en äldre villa i Täby?",
     "Profilen mäts upp först, och läkt, pannor och plåt läggs så att brytningen och svängen vid takfoten får samma linje som tidigare."),
    ("Kan vi lägga solceller på det nya taket utan bygglov i Täby?",
     "Boverkets undantag för anläggningar på högst 11 kilowatt gäller inte där utökad lovplikt råder. Fråga kommunen vad som gäller din adress."),
  ],
  "sources": [
    ("Täby kommun – Kulturmiljöer i Täby (antagen, pdf)",
     "https://taby.se/download/18.6e9443de19c985b90eb19a1e/1772544386382/kulturmiljoer-i-taby_antagen.pdf"),
    ("Täby kommun – Fasadändring",
     "https://taby.se/bygga-bo-och-miljo/bygga-riva-och-forandra/behover-jag-bygglov/fasadandring"),
    _BV_FASAD, _SKV_LISTA, _SKV_ROT,
  ],
  "cta": ("Ska taket i Täby bytas?", "Boka ett gratis platsbesök så går vi igenom taket, pannorna och kommunens riktlinjer."),
  "img": [
    ("Kedjehus i Täby med fasadtegel, träpanel och branta tak av svarta betongpannor",
     "row of 1970s Swedish linked houses with ground floor in red-brown facing brick and upper gables in brown wooden panel, steep roofs covered with black concrete roof tiles, small dormers clad in black painted sheet metal, black barge boards, small front gardens, Täby north of Stockholm, autumn daylight"),
    ("Brunt glaserat tegeltak på en gul tegelvilla från 1950-talet",
     "close-up of a roof covered with brown glazed clay roof tiles with a soft sheen, edge of a yellow brick villa facade from the 1950s below, Swedish suburb, no people, soft daylight"),
  ],
  "related": [],
},
}
