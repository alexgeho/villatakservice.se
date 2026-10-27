# -*- coding: utf-8 -*-
"""Takbyte – ortsidor v22: Ekerö, Lidingö, Sigtuna, Upplands Väsby, Botkyrka, Vallentuna (2026-10-26).
Hubb: takbyte.html (TJ_HUB["takbyte"]). Intent som tj_v21_takbyte.py: byte av hela taktäckningen med regler,
kontroll och ROT – skild från ortens takrenovering-<ort>.html, taklaggare-<ort>.html och platslagare-<ort>.html.
Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.

Rättslig ram: PBL 1 kap. 4 § (fasadändring = byte av kulör, fasadbeklädnad eller taktäckningsmaterial eller annan
påverkan på yttre karaktärsdrag), 9 kap. 15 § p. 3 (lov för fasadändring bara på annan byggnad än en-/tvåbostadshus
mot allmän plats inom detaljplan), 36 § p. 2 (solenergianläggning inom detaljplan i eller nära totalförsvarets
riksintressen), 37 § (särskilt värdefulla byggnader och områden) – riksdagen.se, lydelse 2025:974/2026:406.

Lokal vinkel per sida (skild från ortens takrenovering-, takläggar- och plåtslagarsidor):
Ekerö – kommunens nya bedömning av särskilt värdefulla områden i Ekerökartan, solceller när taket läggs om (Lovö:
  Försvarsmakten remitteras och är ofta negativ, handlingar för lov, anmälan vid bärande/brand), skorsten på taket
  utan bygglov men rökkanal längs fasaden kan kräva lov, eldstad med sotarintyg och slutbesked.
Lidingö – byte av takmaterial som fasadändring, "k-märkt" i fyra betydelser, nio byggnadsminnen (Länsstyrelsen),
  BBR:s exempel på särskilt värdefullt (äldre material och teknik), stadens äldre inventeringar och frivilligt lov.
Sigtuna – kommunens tak-sida: lov för material eller färg i värdefulla miljöer, anmälan även för omläggning vid
  skyddsbestämmelser, frivilligt lov, checklistan (gratis tomtkarta, kontrollplanens innehåll, ritningar med berörda
  delar markerade), foton från alla väderstreck, och Odensala–Hova (lertegel, mansardtak, matt plåt, svart före orange,
  mörka tak med solpaneler som sticker ut).
Upplands Väsby – fasadändring lovfri för villor, solceller kräver bygglov i detaljplanerat område (hela kommunen i
  Försvarsmaktens påverkansområde för väderradar), MSA-område för Uppsala flygplats i norr, anmälan vid ingrepp i
  stommen, "k-märkt" och före 1920, kunskapsunderlaget som uppdaterar programmet från 1988.
Botkyrka – fasadändringens definition med kommunens exempel (tegel till puts, tak- eller fasadintegrerade solpaneler,
  antenner och aggregat på tak), byggnadens karaktärsdrag, utökad lovplikt för solceller och kulturvärden, takkupor
  och byggnadshöjd, taket som takstol plus ytskikt.
Vallentuna – nytt tak utan bygglov för villor, lov i kulturhistoriskt särskilt värdefullt område och handlingarna
  (tomtkarta med byggnaden ikryssad, fasad 1:100, NCS, kontrollplan), skorstenen (bygglov för ny utanpåliggande
  skorsten, Boverkets regler för höjd och placering, anmälan för eldstad, sotarintyg), ritningar ur bygglovsarkivet.

Fakta endast från källorna i respektive 'sources', öppnade med curl (UA Mozilla) 2026-10-26, alla svarade 200
(Skatteverket först timeout, 200 vid nytt försök); Odensala–Hova-pdf:en har textlager.
Strukna / ej använda: alla avgifter och handläggningstider (Sigtunas tio veckor, Ekerös fyra veckor), Botkyrkas
kulturmiljöprogram och Sigtunas bevarande- och förnyelseplan (pdf:erna gav ingen text med pdftotext – inte använda),
Botkyrkas sidor Tak/Takstolar/Takkupa med varningen "informationen kan vara inaktuell" (bara definitionen av tak och
takkupans påverkan på byggnadshöjden används), vilka hus i Väsby som är byggda före 1920 (ingen källa), att
Odensala–Hova-riktlinjerna skulle gälla takbyte på befintliga hus (de gäller ny bebyggelse – skrivet så).
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no text, no letters"

_PBL = ("Riksdagen – Plan- och bygglag (2010:900), 1 kap. 4 § och 9 kap. 15, 36–37 §§",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/plan-och-bygglag-2010900_sfs-2010-900/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")

_EKE_VAD = ("Ekerö kommun – Vad vill du bygga?", "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/vad-vill-du-bygga")
_EKE_SOL = ("Ekerö kommun – Solceller", "https://www.ekero.se/bygga-bo-miljo/energi-och-uppvarmning/solceller")
_LID_VAD = ("Lidingö stad – Vad vill du göra?", "https://lidingo.se/bygga-bo/bygglov/vad-vill-du-gora/")
_LID_KMP = ("Lidingö stad – Frågor och svar om kulturmiljöprogrammet",
            "https://lidingo.se/bygga-bo/bygglov/kulturmiljoprogram/fragor-och-svar-om-kulturmiljoprogrammet/")
_SIG_TAK = ("Sigtuna kommun – Tak", "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/andra-befintlig-byggnad/tak.html")
_SIG_KULT = ("Sigtuna kommun – Bygga i kulturmiljö", "https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html")
_SIG_OH = ("Sigtuna kommun – Riktlinjer för bebyggelseutveckling i dalgången mellan Odensala och Hova (pdf)",
           "https://www.sigtuna.se/download/18.2b81151517d4919beb8c692e/1638798200988/Riktlinjer%20f%C3%B6r%20bebyggelseutveckling%20i%20dalg%C3%A5ngen%20mellan%20Odensala%20och%20Hova.pdf")
_UB = "https://www.upplandsvasby.se/bygga-bo-och-miljo/bygga-nytt-andra-eller-riva/"
_UV_FAS = ("Upplands Väsby kommun – Fasadändring", _UB + "fasadandring")
_UV_SOL = ("Upplands Väsby kommun – Nya regler för solceller – bygglov kan krävas", _UB + "nya-regler-for-solceller---bygglov-kan-kravas")
_UV_KULT = ("Upplands Väsby kommun – Kulturhistoriska byggnader, kulturmiljöer", _UB + "kulturhistoriska-byggnader-kulturmiljoer")
_BA = "https://botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/"
_BOT_FAS = ("Botkyrka kommun – Fasadändring", "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/fasadandring")
_BOT_TAK = ("Botkyrka kommun – Tak", _BA + "tak")
_BOT_KUPA = ("Botkyrka kommun – Takkupa", _BA + "takkupa")
_VB = "https://vallentuna.se/bygga-bo-och-miljo/bygglov-och-anmalan/"
_VAL_FAS = ("Vallentuna kommun – Fasadändring", _VB + "behover-jag-bygglov/fasadandring")
_VAL_ELD = ("Vallentuna kommun – Eldstad", _VB + "behover-jag-bygglov/eldstad")
_VAL_ARK = ("Vallentuna kommun – Bygglovsarkivet", _VB + "bygglovsarkivet")

_ROT_AMT = ("Avdraget är högst 30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor "
            "tillsammans med rutavdrag. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ EKERÖ
"takbyte-ekero.html": {
  "kind": "district", "service": "takbyte", "ort": "Ekerö", "svc_label": "Takbyte",
  "title": "Takbyte på Ekerö – kartan, solceller och skorstenen",
  "description": "Takbyte på Ekerö: Ekerökartan över särskilt värdefulla områden, solceller på det nya taket och Lovö, skorsten, rökkanal och anmälan för eldstad.",
  "h1": "Takbyte på Ekerö",
  "lead": "Ska taket ändå läggas om är det rätt tillfälle att bestämma vad som ska sitta på det de kommande decennierna: solceller, en ny skorsten eller ett annat material. På Ekerö beror svaret på var huset ligger. Geal Entreprenad AB byter tak på villor och fritidshus på Mälaröarna och reder ut reglerna innan materialet beställs.",
  "card": "Kartan, solcellerna och skorstenen.",
  "sections": [
    {"id": "kartan-ekero", "anchor": "Ekerökartan",
     "h2": "Kolla Ekerökartan innan du byter material",
     "paras": [
       "Att byta taktäckningsmaterial räknas som en fasadändring i plan- och bygglagen. På ett en- eller tvåbostadshus kräver det normalt inget bygglov. Men inom särskilt värdefulla områden och på särskilt värdefulla byggnader gäller utökad lovplikt, och då kan ett nytt takmaterial kräva bygglov.",
       "När lagen ändrades gjorde Ekerö kommun en ny bedömning av sina särskilt värdefulla byggnader och områden. Kartan över dem finns i Ekerökartan tillsammans med totalförsvarets riksintressen, och kommunen ber dig börja med att kontrollera om din fastighet berörs. Vi kontrollerar kartan och detaljplanen vid platsbesöket, innan något material väljs.",
     ],
     "aside": {"title": "Kontrollera i kartan", "items": [
       "Särskilt värdefulla byggnader", "Särskilt värdefulla områden", "Totalförsvarets riksintressen"]}},
    {"id": "solceller-ekero", "h2": "Solceller på det nya taket",
     "paras": [
       "Ekerö kommun skriver att solenergi kan vara bra att planera för när du ska lägga om taket, och att solceller på taket vanligtvis inte kräver bygglov. Undantagen är när detaljplanen kräver lov för solpaneler, när fastigheten ligger inom detaljplan och inom område för totalförsvarets riksintressen och när åtgärden sker på särskilt värdefulla byggnader eller i särskilt värdefulla områden.",
       "På Lovö är det särskilt. Vid bygglovsärenden inom detaljplan och områdesbestämmelser där remitteras Försvarsmakten, som enligt kommunen ofta är negativ till solceller, och då kan bygglov inte beviljas. En ansökan om bygglov för solceller ska innehålla situationsplan, fasadritningar med mått på solcellerna, produktblad och kontrollplan. Påverkar anläggningen väsentligt den bärande konstruktionen eller brandskyddet krävs en bygganmälan.",
     ],
     "aside": {"title": "Till ansökan om solceller", "items": [
       "Situationsplan", "Fasadritningar med mått", "Produktblad", "Kontrollplan"]}},
    {"id": "skorsten-ekero", "h2": "Skorsten och rökkanal",
     "paras": [
       "Ska en ny skorsten upp genom det nya taket behövs inget bygglov, skriver kommunen. Vill du i stället dra en rökkanal längs fasaden kan det krävas bygglov för fasadändring. Installation eller större ändring av en eldstad, braskamin, öppen spis eller kakelugn ska anmälas, och det gäller också om du sätter in en spisinsats i en befintlig öppen spis eller byter bränsle i husets huvudsakliga värmekälla.",
       "Anmälan ska innehålla en planritning med eldstaden markerad, en fasadritning med skorstenen eller rökkanalen inritad, en kontrollplan och produktbeskrivning med typgodkännande eller CE-märkning. När installationen är klar skickar du in sotarintyg, den ifyllda kontrollplanen och en ansökan om slutbesked, och eldstaden får inte användas innan slutbeskedet har kommit. Vi plåtar in skorstenen tätt mot det nya taket och samordnar arbetet så att genomföringen är klar när sotaren kommer.",
     ],
     "aside": None},
    {"id": "lasten-ekero", "h2": "Taket som bär",
     "paras": [
       "Även när varken lov eller anmälan krävs måste solceller uppfylla kraven i plan- och bygglagen, plan- och byggförordningen, Boverkets byggregler och Boverkets konstruktionsregler, påpekar kommunen. Ett tyngre takmaterial eller ett fält med solpaneler ändrar lasten på takstolarna, och då bedöms bärförmågan innan något monteras.",
       "Vi går igenom takstolar, råspont och läkt när det gamla taket är av och byter det som är skadat. Om husens tak och epoker på öarna kan du läsa under " + _L.format("takrenovering-ekero.html", "takrenovering på Ekerö") + ", och om våra tjänster i stort under " + _L.format("taklaggare-ekero.html", "takläggare på Ekerö") + " och " + _L.format("takbyte.html", "takbyte") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte på Ekerö till",
  "steps": [
    ("Platsbesök", "Tak, takstolar, skorsten och önskemål om solceller går vi igenom på plats."),
    ("Kartan", "Ekerökartan och detaljplanen kontrolleras för fastigheten."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt, plåt och genomföringar står var för sig."),
    ("Lov och anmälan", "Bygglov för solceller eller anmälan för eldstad när det behövs."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Genomgång", "Vi går igenom taket, plåten och genomföringarna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte på Ekerö",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor och hängrännor på ett småhus som rotarbete, liksom att byta plåttak och stuprör och att montera och montera ner byggnadsställningar. Rotavdrag ges för en bostad som du äger och bor i eller använder som fritidsbostad.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet på Ekerö?",
  "price": [
    "Takets yta och lutning, materialet, skorstenens skick, hur mycket underlag som behöver bytas, om solceller ska förberedas och hur material och ställning kan fraktas till tomten. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi sätta solceller på det nya taket på Lovö?",
     "Det kan bli svårt. Vid bygglovsärenden inom detaljplan och områdesbestämmelser på Lovö remitteras Försvarsmakten, som enligt kommunen ofta är negativ, och då kan bygglov inte beviljas."),
    ("Behövs bygglov för en ny skorsten när taket byts på Ekerö?",
     "Inte för en skorsten på taket, enligt kommunen. En rökkanal längs fasaden kan däremot kräva bygglov för fasadändring."),
    ("Vad ska anmälan av en ny kamin på Ekerö innehålla?",
     "Planritning med eldstaden, fasadritning med skorsten eller rökkanal, kontrollplan och produktbeskrivning med typgodkännande eller CE-märkning."),
    ("Måste en spisinsats anmälas på Ekerö?",
     "Ja. Kommunen skriver att även installation eller byte av en spisinsats i en befintlig öppen spis ska anmälas, liksom byte av bränsle i husets huvudsakliga värmekälla."),
    ("Var ser vi om vårt hus på Ekerö är särskilt värdefullt?",
     "I Ekerökartan, där kommunen visar särskilt värdefulla byggnader och områden tillsammans med totalförsvarets riksintressen."),
  ],
  "sources": [_PBL, _EKE_VAD, _EKE_SOL, _SKV, _SKV2],
  "cta": ("Ska taket på Ekerö bytas?", "Boka ett gratis platsbesök, så går vi igenom taket, kartan och dina planer innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa med nylagt svart pannetak, murad skorsten och ställning längs ena gaveln",
     "Swedish one-and-a-half storey wooden villa painted light grey with a newly laid black concrete tile roof and a brick chimney with fresh black metal flashing, scaffolding along the eaves, birches and a glimpse of Lake Mälaren behind, late summer daylight" + _IMG_END),
    ("Solpaneler monterade på ett tak med svarta betongpannor",
     "pitched roof of a Swedish villa with new dark grey concrete roof tiles and aluminium mounting rails with roof hooks installed for solar panels, no panels yet, clear sky" + _IMG_END),
    ("Tak under byte med ställning längs takfoten och ny duk på en del av takfallet",
     "Swedish villa roof during replacement: old tiles removed, timber rafters and fresh tongue-and-groove roof boarding partly covered with underlayment membrane, scaffolding with guard rail at the eaves, overcast daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ LIDINGÖ
"takbyte-lidingo.html": {
  "kind": "district", "service": "takbyte", "ort": "Lidingö", "svc_label": "Takbyte",
  "title": "Takbyte på Lidingö – nytt material och husets värde",
  "description": "Takbyte på Lidingö: när nytt takmaterial är en fasadändring, vad k-märkt kan betyda, stadens nio byggnadsminnen, äldre inventeringar och frivilligt lov.",
  "h1": "Takbyte på Lidingö",
  "lead": "Samma pannor igen eller ett annat material – på Lidingö är det frågan som avgör om ett takbyte kan bli en lovfråga. Svaret hänger på om huset eller området är särskilt värdefullt, och det är inte självklart. Geal Entreprenad AB byter tak i hela Lidingö och tar reda på husets status innan materialet väljs.",
  "card": "Nytt material, k-märkning och byggnadsminnen.",
  "sections": [
    {"id": "material-lidingo", "anchor": "Nytt takmaterial",
     "h2": "Nytt takmaterial är en fasadändring",
     "paras": [
       "Lidingö stad beskriver en fasadändring som en ändring av det yttre utseendet, till exempel att måla om, byta fasadmaterial, byta takmaterial eller ändra fönster och dörrar. Inom detaljplan krävs bygglov för fasadändring på andra byggnader än en- och tvåbostadshus, komplementbyggnader och komplementbostadshus, när ändringen sker på en fasad eller ett tak mot allmän plats och påverkar husets karaktär. För en villa är huvudregeln alltså att det inte krävs lov.",
       "Men staden skriver också att du behöver bygglov för en fasadändring om din fastighet ligger inom ett kulturhistoriskt värdefullt område eller om byggnaden är kulturhistoriskt värdefull. Byter du lertegel mot betongpannor eller plåt på ett sådant hus är det en lovfråga. För en lovfri fasadändring kan du söka frivilligt bygglov och få miljö- och stadsbyggnadsnämndens beslut på att det du planerar uppfyller lagens krav.",
     ],
     "aside": {"title": "Bygglov kan krävas när", "items": [
       "Huset är kulturhistoriskt värdefullt", "Området är kulturhistoriskt värdefullt",
       "Det är inte ett en- eller tvåbostadshus"]}},
    {"id": "kmarkt-lidingo", "h2": "Fyra saker som kan menas med k-märkt",
     "paras": [
       "Staden påpekar att k-märkt inte är ett juridiskt begrepp. Oftast menas något av följande: att byggnaden är skyddad som byggnadsminne, att den har skyddsbestämmelser i en detaljplan eller områdesbestämmelse, att den är utpekad som värdefull i kulturmiljöprogrammet eller att den ligger i en kulturmiljö som programmet pekar ut. I dagens detaljplaner används huvudsakligen q för skydd av kulturvärden, k för karaktärsdrag och r för rivningsförbud, men äldre planer kan ha andra beteckningar.",
       "Lidingö har nio byggnadsminnen, bland dem Villa Skogsbacken, Täcka Udden, Villa Högberga, Villa Klippudden och radhusen på Canadastigen. För dem är det Länsstyrelsen som beslutar om tillstånd till ändringar och har tillsynen. Ett takbyte på ett byggnadsminne börjar därför med en kontakt med Länsstyrelsen.",
     ],
     "aside": {"title": "K-märkt kan betyda", "items": [
       "Byggnadsminne", "Skyddsbestämmelse i plan",
       "Utpekad i kulturmiljöprogrammet", "Inom utpekad kulturmiljö"]}},
    {"id": "varde-lidingo", "h2": "När ett tak är en del av värdet",
     "paras": [
       "Vad som gör en byggnad särskilt värdefull beskriver staden med hjälp av de allmänna råden i Boverkets byggregler. Ett av exemplen gäller tak direkt: en byggnad kan vara särskilt värdefull om den i sig är en källa till kunskap om äldre material och teknik. Ett gammalt lertegeltak, en falsad plåt eller ett skiffertak kan alltså vara en del av husets värde, inte bara ett ytskikt.",
       "Staden skriver också att kulturmiljöprogrammet pekar ut områden snarare än enskilda hus, och att det därför finns särskilt värdefulla byggnader som inte beskrivs i programmet. Inom de utpekade områdena bör alla fastigheter hanteras varsamt, eftersom åtgärder på ett hus kan påverka helheten. Vid ett takbyte på ett sådant hus föreslår vi att material och detaljer behålls eller återskapas.",
     ],
     "aside": None},
    {"id": "historia-lidingo", "h2": "Husets historia innan pannorna beställs",
     "paras": [
       "Lidingö stad har äldre byggnadsinventeringar för enskilda byggnader, dels från 1970- och 1980-talen, dels från 2013–2015. Via kundcenter för miljö- och stadsbyggnadskontoret kan du be att få ta del av de beskrivningar som finns för din fastighet. Där kan det framgå vilket material taket hade från början.",
       "Med det underlaget kan vi föreslå ett material som passar huset och, om det behövs, ta fram handlingar till ett bygglov eller frivilligt lov. Om villastäderna och takens epoker på ön kan du läsa under " + _L.format("takrenovering-lidingo.html", "takrenovering på Lidingö") + ", om plåt och rännor under " + _L.format("platslagare-lidingo.html", "plåtslagare på Lidingö") + " och om våra tjänster i stort under " + _L.format("taklaggare-lidingo.html", "takläggare på Lidingö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte på Lidingö till",
  "steps": [
    ("Husets status", "Byggnadsminne, skyddsbestämmelser och kulturmiljöprogrammet kontrolleras."),
    ("Platsbesök", "Tak, underlag, plåt och detaljer som bär husets karaktär."),
    ("Materialval", "Samma material eller nytt – och vad det betyder för lovfrågan."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt, plåt och ställning står var för sig."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Genomgång", "Vi går igenom det färdiga taket med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte på Lidingö",
  "rot": [
    "Att byta och reparera takpannor och hängrännor på ett småhus är rotarbete enligt Skatteverket, liksom att byta plåttak och stuprör och att montera och montera ner byggnadsställningar i samband med arbetet. Är bostaden yngre än fem år får arbetet bara återställa det ursprungliga skicket, och nytt material ska då vara likvärdigt med det gamla.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet på Lidingö?",
  "price": [
    "Takets yta och form, materialet, hur mycket underlag som behöver bytas, plåtdetaljer och om material eller detaljer ska återskapas på ett värdefullt hus. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Krävs bygglov för att byta från tegel till plåt på Lidingö?",
     "För en villa normalt inte. Men ligger huset i ett kulturhistoriskt värdefullt område eller är det kulturhistoriskt värdefullt krävs bygglov för fasadändringen."),
    ("Vem ger tillstånd till nytt tak på ett byggnadsminne på Lidingö?",
     "Länsstyrelsen. Den beslutar om byggnadsminnen och hanterar tillstånd för ändringar av dem."),
    ("Vad betyder q, k och r i en detaljplan på Lidingö?",
     "q reglerar skydd av kulturvärden, k reglerar byggnadens karaktärsdrag och r anger rivningsförbud. Äldre planer kan ha andra beteckningar."),
    ("Kan vi få veta vilket tak huset hade från början på Lidingö?",
     "Kanske. Staden har inventeringar från 1970- och 80-talen och 2013–2015, och via kundcenter kan du be att få ta del av beskrivningar för din fastighet."),
  ],
  "sources": [_PBL, _LID_VAD, _LID_KMP, _SKV, _SKV2],
  "cta": ("Ska taket på Lidingö bytas?", "Boka ett gratis platsbesök, så tar vi reda på husets status innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Trävilla med brant sadeltak av rött tegel på en bergig tomt med tallar",
     "early 1900s Swedish wooden villa with a steep pitched roof of red clay tiles, a glazed veranda and decorative gable trim on a rocky hill among pine trees, a glimpse of the sea, summer daylight" + _IMG_END),
    ("Ny råspont av trä på taket innan underlagsduken läggs",
     "stack of old weathered red clay roof tiles on a wooden pallet next to a stack of new red clay tiles of the same profile on a Swedish villa driveway, scaffolding in the background, overcast daylight" + _IMG_END),
    ("Radhuslänga med enhetliga tak och skorstenar sett från gatan",
     "row of 1940s Swedish terraced houses with uniform red tiled roofs, identical chimneys and white rendered facades along a quiet street with small front gardens, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ SIGTUNA
"takbyte-sigtuna.html": {
  "kind": "district", "service": "takbyte", "ort": "Sigtuna", "svc_label": "Takbyte",
  "title": "Takbyte i Sigtuna – lov, checklista och gårdarnas tegel",
  "description": "Takbyte i Sigtuna: när nytt takmaterial eller ny färg kräver lov, kommunens checklista för ansökan och vad riktlinjerna för Odensala–Hova säger om tak.",
  "h1": "Takbyte i Sigtuna",
  "lead": "Sigtuna kommun har många kulturhistoriskt värdefulla byggnader och områden, och för dem kan även ett takbyte bli ett ärende. Kommunen har samlat vad som gäller för tak på en egen sida med en checklista i fem steg. Geal Entreprenad AB byter tak i hela kommunen och tar fram underlaget när det behövs.",
  "card": "Lov, checklista och gårdarnas tegel.",
  "sections": [
    {"id": "lov-sigtuna", "anchor": "Lov eller inte",
     "h2": "När ett nytt tak kräver bygglov",
     "paras": [
       "Vill du byta takmaterial, ändra färg på taket eller på annat sätt ändra takets utseende kan du behöva bygglov, skriver kommunen. Det beror på var byggnaden ligger och om den har ett särskilt kulturhistoriskt värde. Bygglov krävs om åtgärden görs vid, inom eller på en byggnad, tomt, ett område eller en allmän plats som är särskilt kulturhistoriskt värdefull, eller i ett område där detaljplan eller områdesbestämmelser har skyddsbestämmelser.",
       "För byggnader med skyddsbestämmelser kan du behöva göra en anmälan även för underhåll av taket, till exempel en omläggning, fast du varken byter färg eller material. Vill du vara säker inför ett materialbyte kan du söka frivilligt bygglov. Är du osäker på om huset ligger i ett värdefullt område tar kommunen emot foton på fastigheten från samtliga väderstreck och återkommer med en bedömning.",
     ],
     "aside": {"title": "Kan kräva lov eller anmälan", "items": [
       "Nytt takmaterial", "Ny färg på taket", "Annan ändring av utseendet",
       "Omläggning vid skyddsbestämmelser"]}},
    {"id": "checklista-sigtuna", "h2": "Kommunens checklista för takärendet",
     "paras": [
       "Till en ansökan om bygglov för ändring av tak behöver du situationsplan, förslag till kontrollplan och byggnadsritningar. Tomtkartan till situationsplanen laddar du ner som pdf från kommunen, utan inloggning och utan kostnad. På den markerar du tydligt de delar av byggnaden som påverkas.",
       "Kontrollplanen ska visa vilken fastighet det gäller och vem som är byggherre, vad som ska kontrolleras, vem som gör kontrollerna, hur de görs och dokumenteras, när i processen de görs och ha plats för datum och signatur. Enligt kommunen ska ett förslag till kontrollplan lämnas in både vid bygglov och vid anmälan. Ritningarna ska redovisa åtgärden, och berör den bara en del av huset ska hela fasaden eller sektionen visas med de berörda delarna markerade.",
     ],
     "aside": {"title": "Kontrollplanen ska visa", "items": [
       "Fastighet och byggherre", "Vad som kontrolleras", "Vem, hur och när",
       "Plats för datum och signatur"]}},
    {"id": "varsamt-sigtuna", "h2": "Varsamhet i kulturmiljöerna",
     "paras": [
       "I kulturmiljöer ska ändringar göras varsamt, skriver kommunen. Den råder dig att behålla det formspråk, de proportioner och karaktärsdrag som är typiska för byggnaden och tiden, och påpekar att utformningen av tak, fasader, fönster och andra detaljer är viktiga för husets uttryck. Ursprungliga material och detaljer bör bevaras om det går, eller ersättas med samma material om de behöver bytas.",
       "Kommunen pekar ut värdefulla miljöer i bland annat översiktsplanen, kulturminnesvårdsprogrammet, bevarande- och förnyelseplanen för Sigtuna stad och riktlinjerna för Odensala–Hova. Byggnadsminnen och kyrkor finns i Riksantikvarieämbetets bebyggelseregister. Även hus som inte är utpekade kan vara så värdefulla att särskild hänsyn behövs.",
     ],
     "aside": None},
    {"id": "odensala-sigtuna", "h2": "Tegel och mansardtak i Odensala–Hova",
     "paras": [
       "Riktlinjerna för dalgången mellan Odensala och Hova, antagna i december 2020, beskriver de äldre husen. Parstugorna har sadeltak, brutna eller obrutna, täckta med lertegel, och sekelskiftesvillorna från omkring 1900 har lertegeltäckta sadeltak som ibland är brutna. Flera gårdar beskrivs med bevarad Falu rödfärgstradition och rött lertaktegel.",
       "För nya hus i dalgången anger riktlinjerna att takbeläggningen bör vara lertegel, och att plåt i så fall ska upplevas matt på avstånd och att svart kulör då ofta är bättre än en klar orange ton. Dokumentet konstaterar också att ny bebyggelse sticker ut genom vita fasader och mörka tak med solpaneler. Riktlinjerna gäller ny bebyggelse, men vid ett takbyte på en äldre gård visar de vad kommunen ser som karaktären. Om taken i kommunen i stort kan du läsa under " + _L.format("takrenovering-sigtuna.html", "takrenovering i Sigtuna") + " och " + _L.format("taklaggare-sigtuna.html", "takläggare i Sigtuna") + ".",
     ],
     "aside": {"title": "Enligt riktlinjerna", "items": [
       "Lertegel på äldre hus", "Mansardtak på en del villor", "Matt plåt", "Svart före klar orange"]}},
  ],
  "steps_h2": "Så går ett takbyte i Sigtuna till",
  "steps": [
    ("Platsbesök", "Tak, underlag, material och husets karaktärsdrag."),
    ("Värdefullt eller inte", "Detaljplan, skyddsbestämmelser och vid behov kommunens bedömning."),
    ("Underlag", "Situationsplan på tomtkartan, ritningar och förslag till kontrollplan."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt, plåt och ställning står var för sig."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Kontroller", "Våra kontrollpunkter signeras och taket gås igenom med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Sigtuna",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor och hängrännor på ett småhus som rotarbete, liksom att reparera eller byta plåttak och stuprör och att montera och montera ner byggnadsställningar. Arbetet ska göras i eller nära en bostad som du äger och använder som bostad.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Sigtuna?",
  "price": [
    "Takets yta och form, valet mellan lertegel, betongpannor och plåt, hur mycket underlag som behöver bytas, plåtdetaljerna och om ett lov med ritningar behövs. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för att byta färg på taket i Sigtuna?",
     "Det kan behövas om huset eller området är särskilt kulturhistoriskt värdefullt eller om detaljplanen har skyddsbestämmelser. Annars är en färgändring på en villa normalt lovfri."),
    ("Ska en kontrollplan lämnas in även vid anmälan av ett takarbete i Sigtuna?",
     "Ja. Kommunen vill ha ett förslag till kontrollplan oavsett om du söker bygglov eller gör en anmälan."),
    ("Vilka foton vill Sigtuna kommun ha för att bedöma kulturvärdet?",
     "Foton på fastigheten från samtliga väderstreck, tillsammans med adress eller fastighetsbeteckning och en beskrivning av vad du vill göra."),
    ("Vilket takmaterial förordar Sigtuna i dalgången mellan Odensala och Hova?",
     "Riktlinjerna för ny bebyggelse anger lertegel. Används plåt ska den upplevas matt på avstånd, och svart kulör är då ofta bättre än en klar orange ton."),
  ],
  "sources": [_PBL, _SIG_TAK, _SIG_KULT, _SIG_OH, _SKV, _SKV2],
  "cta": ("Ska taket i Sigtuna bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och vad som gäller för huset innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Rödmålad trävilla med vita snickerier och tak av rött lertegel",
     "Swedish turn-of-the-century farmhouse villa painted falu red with white trims and a mansard roof covered with red clay tiles, a central gable, gravel farmyard and large old trees, open Uppland farmland behind, summer daylight" + _IMG_END),
    ("Nya röda lertegelpannor läggs på läkt över ny underlagsduk",
     "close-up of new red clay roof tiles being laid row by row on wooden battens over a fresh underlay membrane on a pitched farmhouse roof, partly finished, daylight" + _IMG_END),
    ("Matt svart plåttak på ett rödmålat uthus i ett odlingslandskap",
     "matte black standing seam metal roof on a falu red wooden outbuilding in an open agricultural valley, older red buildings with clay tile roofs nearby, soft afternoon light" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ UPPLANDS VÄSBY
"takbyte-upplands-vasby.html": {
  "kind": "district", "service": "takbyte", "ort": "Upplands Väsby", "svc_label": "Takbyte",
  "title": "Takbyte i Upplands Väsby – solceller, radar och stommen",
  "description": "Takbyte i Upplands Väsby: nytt tak utan bygglov, solceller som kräver lov i detaljplanerade delar, anmälan vid ingrepp i stommen och husets värde.",
  "h1": "Takbyte i Upplands Väsby",
  "lead": "Ett nytt tak på en villa i Upplands Väsby kräver i regel inget bygglov. Men planerar du solceller i samma veva gäller en särskild regel: i hela den detaljplanerade delen av kommunen krävs bygglov för solceller. Geal Entreprenad AB byter tak i hela Väsby och planerar solcellerna från början.",
  "card": "Nytt tak, solceller och väderradarn.",
  "sections": [
    {"id": "lovfritt-uv", "anchor": "Nytt tak utan lov",
     "h2": "Nytt takmaterial är lovfritt för villan",
     "paras": [
       "Enligt plan- och bygglagen är en fasadändring att en byggnad ändrar kulör, fasadbeklädnad eller taktäckningsmaterial eller att dess yttre karaktärsdrag påverkas på annat sätt. Upplands Väsby kommun skriver att det omfattar väggar, tak och andra delar av utsidan. För en- och tvåbostadshus behövs normalt inget bygglov, varken inom eller utanför detaljplan, för att byta taktäckningsmaterial, och det gäller även komplementbyggnader och komplementbostadshus.",
       "Undantagen är när detaljplanen eller områdesbestämmelser har utökad lovplikt för fasadändring, när fasadändringen görs inom ett kulturhistoriskt särskilt värdefullt område och när byggnaden är särskilt värdefull och ändringen ändrar dess karaktär. Varsamhetskravet gäller oavsett lovplikten, påpekar kommunen.",
     ],
     "aside": {"title": "Lov kan ändå krävas", "items": [
       "Utökad lovplikt i planen", "Kulturhistoriskt särskilt värdefullt område",
       "Särskilt värdefull byggnad", "Solceller inom detaljplan"]}},
    {"id": "solceller-uv", "h2": "Solceller kräver bygglov – på grund av väderradarn",
     "paras": [
       "Sedan ändringarna i plan- och bygglagen den 1 december 2025 finns inget generellt krav på bygglov för solenergianläggningar. Men hela Upplands Väsby ligger inom Försvarsmaktens påverkansområde för väderradar, och därför krävs bygglov för solcellsanläggningar i alla delar av kommunen som är detaljplanerade, även när solcellerna annars inte hade krävt lov. Försvarsmakten och Myndigheten för civilt försvar kan ange vilka åtgärder de vill bli underrättade om, men bygglovsplikten kan inte väljas bort.",
       "Delar av kommunens norra del berörs dessutom av ett så kallat MSA-område, hinderbegränsande ytor för flyg kopplade till Uppsala flygplats, som också kan påverka bedömningen. Ska solceller upp på det nya taket söker vi därför bygglovet innan taket läggs, så att fästen och genomföringar kan monteras i rätt läge från början.",
     ],
     "aside": None},
    {"id": "stommen-uv", "h2": "Anmälan när stommen berörs",
     "paras": [
       "En anmälan ska lämnas in om en ändring påverkar byggnadens bärande konstruktion, skriver kommunen. Vid ett takbyte kan det bli aktuellt om takstolar förstärks för ett tyngre material eller för solpaneler, eller om en bärande del måste bytas. Då behövs startbesked innan arbetet börjar.",
       "Vi bedömer takstolarna när det gamla taket är av, och ser vi att något bärande behöver ändras tar vi in en konstruktör och gör anmälan innan vi fortsätter. Skadad råspont och läkt byts som en del av takbytet. Om husens takmaterial och epoker i Väsby kan du läsa under " + _L.format("takrenovering-upplands-vasby.html", "takrenovering i Upplands Väsby") + ".",
     ],
     "aside": {"title": "Anmälan krävs vid", "items": [
       "Förstärkta takstolar", "Byte av bärande delar", "Annat ingrepp i stommen"]}},
    {"id": "vardefullt-uv", "h2": "Är huset värdefullt?",
     "paras": [
       "K-märkt är ingen juridisk term, skriver kommunen. En byggnad kan vara kulturhistoriskt värdefull genom att vara byggnadsminne, vara skyddad i detaljplan, ingå i ett riksintresse för kulturmiljövården, vara utpekad i en inventering eller vara uppförd före 1920 med bibehållen karaktär. Den behöver inte vara utpekad i förväg, och förvanskningsförbudet gäller även åtgärder som inte kräver lov eller anmälan.",
       "Kommunen har tagit fram ett kommunövergripande kunskapsunderlag för kulturmiljö, en uppdatering av det äldre kulturmiljöprogrammet från 1988, som beskriver byggnader och miljöer som kommunen bedömt som särskilt värdefulla. För byggnadsminnen är det Länsstyrelsen som ger tillstånd till ändringar. Om plåtdetaljer och takavvattning kan du läsa under " + _L.format("platslagare-upplands-vasby.html", "plåtslagare i Upplands Väsby") + " och om våra tjänster i stort under " + _L.format("taklaggare-upplands-vasby.html", "takläggare i Upplands Väsby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Upplands Väsby till",
  "steps": [
    ("Platsbesök", "Tak, takstolar och om solceller ska upp nu eller senare."),
    ("Förutsättningar", "Detaljplan, kulturvärden och om bygglov för solceller behövs."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt, plåt och förberedelser för solceller."),
    ("Lov och anmälan", "Bygglov för solceller och anmälan om stommen berörs."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Genomgång", "Vi går igenom taket och plåtdetaljerna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Upplands Väsby",
  "rot": [
    "Byte och reparation av takpannor och hängrännor på ett småhus ger rotavdrag enligt Skatteverket, liksom att byta plåttak och stuprör och att montera och montera ner byggnadsställningar. Du ska äga bostaden när arbetet görs och helt eller delvis bo i den.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Upplands Väsby?",
  "price": [
    "Takets yta och lutning, materialet, hur mycket underlag och takstolar som behöver åtgärdas, plåtdetaljer och om fästen för solceller ska monteras samtidigt. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför krävs bygglov för solceller i Upplands Väsby?",
     "Hela kommunen ligger inom Försvarsmaktens påverkansområde för väderradar. Därför krävs bygglov för solcellsanläggningar i alla detaljplanerade delar av kommunen."),
    ("Behövs bygglov för att byta betongpannor mot plåt i Upplands Väsby?",
     "För en villa normalt inte. Undantagen är utökad lovplikt i planen, kulturhistoriskt särskilt värdefulla områden och särskilt värdefulla byggnader."),
    ("Kan Försvarsmakten avstå från lovplikten för våra solceller?",
     "Nej. Kommunen skriver att Försvarsmakten och Myndigheten för civilt försvar kan ange vilka åtgärder de vill underrättas om, men lovplikten kan inte väljas bort."),
    ("Är vårt hus i Upplands Väsby kulturhistoriskt värdefullt?",
     "Det kan vara det även om det inte är utpekat. Kommunen nämner bland annat byggnader som är skyddade i plan, utpekade i inventeringar eller uppförda före 1920 med bibehållen karaktär."),
  ],
  "sources": [_PBL, _UV_FAS, _UV_SOL, _UV_KULT, _SKV, _SKV2],
  "cta": ("Ska taket i Upplands Väsby bytas?", "Boka ett gratis platsbesök, så planerar vi taket och solcellerna innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa i tegel och trä med mörkt betongpannetak vid en villagata",
     "1970s Swedish single-storey villa with brown brick and wooden facade and a newly laid dark grey concrete tile roof, scaffolding with guard rail along the eaves, birch trees and a quiet residential street, Uppland suburb, clear daylight" + _IMG_END),
    ("Svart pannat tak med solpaneler och takfönster",
     "close view of black solar panels mounted on aluminium rails over new dark concrete roof tiles on a Swedish villa, neat cable routing at the edge, blue sky" + _IMG_END),
    ("Förstärkta takstolar på en öppen vind under ett takbyte",
     "open attic during a roof replacement on a Swedish house, existing timber roof trusses reinforced with new timber members and metal nail plates, daylight coming through gaps in the roof boarding" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ BOTKYRKA
"takbyte-botkyrka.html": {
  "kind": "district", "service": "takbyte", "ort": "Botkyrka", "svc_label": "Takbyte",
  "title": "Takbyte i Botkyrka – fasadändring, solpaneler och takkupor",
  "description": "Takbyte i Botkyrka: vad kommunen räknar som fasadändring på taket, husets karaktärsdrag, solpaneler och utökad lovplikt, takkupor och byggnadshöjden.",
  "h1": "Takbyte i Botkyrka",
  "lead": "Ett takbyte är sällan bara nya pannor. Ofta byts materialet, solpaneler kommer till eller en takkupa ska byggas medan taket ändå är öppet. Botkyrka kommun beskriver noga när sådana ändringar blir en lovfråga. Geal Entreprenad AB byter tak i hela Botkyrka och går igenom det med dig innan arbetet börjar.",
  "card": "Material, solpaneler och takkupor.",
  "sections": [
    {"id": "fasadandring-botkyrka", "anchor": "Fasadändring",
     "h2": "Vad kommunen räknar som fasadändring på taket",
     "paras": [
       "Plan- och bygglagen definierar fasadändring som att en byggnad byter kulör, fasadbeklädnad eller taktäckningsmaterial eller att dess yttre karaktärsdrag påverkas på annat sätt. Botkyrka kommun förklarar att ett materialbyte innebär att det befintliga materialet byts ut mot ett annat, till exempel från tegel till putsad fasad, och att även installation av tak- eller fasadintegrerade solpaneler i vissa fall kan bedömas som fasadändring. Anläggningar för solenergi, antenner och aggregat för ventilation, kyla och värme kan också räknas som fasadändring när de monteras, flyttas eller ändras på tak.",
       "Inom detaljplan krävs bygglov för en fasadändring om tre saker gäller samtidigt: att det är en fasadändring, att den görs på en annan byggnad än ett en- eller tvåbostadshus, en komplementbyggnad eller ett komplementbostadshus och att ändringen sker på en fasad eller ett tak som vetter mot allmän plats. För en villa är ett nytt takmaterial därför normalt lovfritt.",
     ],
     "aside": {"title": "Kan vara fasadändring", "items": [
       "Nytt takmaterial", "Takintegrerade solpaneler", "Antenner på taket",
       "Aggregat för ventilation, kyla och värme"]}},
    {"id": "karaktar-botkyrka", "h2": "Husets karaktärsdrag",
     "paras": [
       "Om en ändring påverkar husets yttre karaktärsdrag på annat sätt behöver det bedömas utifrån den enskilda byggnaden, skriver kommunen. Karaktärsdragen kan vara storlek, färg, utvändiga materialval, byggnadsstil, ålder, detaljer och proportioner. Ett tak som går från rött tegel till svart plåt ändrar både färg och material på en stor del av huset.",
       "Den utökade lovplikten gäller alla typer av lovfria fasadändringar, inom och utanför detaljplan. Det betyder att en annars lovfri ändring kräver bygglov om den görs på en särskilt värdefull byggnad eller inom en tomt, allmän plats eller ett bebyggelseområde som har skyddsbestämmelser eller är särskilt värdefullt. Kommunen hänvisar till lagren Kulturmiljöprogram, Detaljplaner och Riksintressen i webbkartan, och till översiktsplanen och eventuella gestaltningsprogram.",
     ],
     "aside": {"title": "Karaktärsdrag enligt kommunen", "items": [
       "Storlek och proportioner", "Färg och material", "Byggnadsstil och ålder", "Detaljer"]}},
    {"id": "solpaneler-botkyrka", "h2": "Solpaneler och totalförsvaret",
     "paras": [
       "För solenergi finns en särskild regel. En lovfri fasadändring kräver bygglov om den innebär att en solenergianläggning sätts upp eller väsentligt ändras inom detaljplanelagt område och inom eller i anslutning till områden som är av riksintresse för totalförsvarets anläggningar. Kommunens webbkarta har lagren Totalförsvaret och MSB, Försvarsmaktens civila del, under fliken Riksintressen.",
       "Planerar du solpaneler på det nya taket kontrollerar vi därför båda lagren först. Krävs bygglov söker vi det innan taket läggs, så att fästen och genomföringar kan monteras i rätt läge. Om takvatten, rännor och plåt i kommunen kan du läsa under " + _L.format("platslagare-botkyrka.html", "plåtslagare i Botkyrka") + ".",
     ],
     "aside": None},
    {"id": "takkupa-botkyrka", "h2": "Takkupor medan taket är öppet",
     "paras": [
       "Ett tak består enligt kommunen av en bärande konstruktion, takstolen, och ett skyddande ytskikt. En takkupa ingriper i båda. Kommunen skriver att du måste söka bygglov om du vill bygga större eller flera takkupor på ditt en- eller tvåbostadshus, och påpekar att en ny takkupa kan påverka husets byggnadshöjd. Börjar du bygga innan du har gjort anmälan eller sökt bygglov och fått startbesked kan det bli sanktionsavgifter.",
       "Kommunen anger också att sidan om takkupor kan vara inaktuell efter lagändringen den 1 december 2025. Vi kontrollerar därför vad som gäller för just din kupa innan den ritas. Om husens tak och epoker i Botkyrka kan du läsa under " + _L.format("takrenovering-botkyrka.html", "takrenovering i Botkyrka") + ", och om våra tjänster i stort under " + _L.format("taklaggare-botkyrka.html", "takläggare i Botkyrka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Botkyrka till",
  "steps": [
    ("Platsbesök", "Tak, takstolar, material och planer på solpaneler eller takkupa."),
    ("Webbkartan", "Kulturmiljö, detaljplan och totalförsvarets lager för fastigheten."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt, plåt och eventuella tillägg."),
    ("Lov och anmälan", "Bygglov eller anmälan när solpaneler, kupa eller kulturvärden kräver det."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Genomgång", "Vi går igenom taket, plåten och genomföringarna med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Botkyrka",
  "rot": [
    "Skatteverket räknar byte och reparation av takpannor och hängrännor på ett småhus som rotarbete, och även att byta plåttak och stuprör och att montera och montera ner byggnadsställningar. Är bostaden yngre än fem år får arbetet bara återställa det ursprungliga skicket.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Botkyrka?",
  "price": [
    "Takets yta och lutning, materialet, hur mycket råspont och läkt som behöver bytas, plåtdetaljer och om takkupor eller fästen för solpaneler ska byggas samtidigt. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Räknas takintegrerade solpaneler som fasadändring i Botkyrka?",
     "De kan göra det. Kommunen skriver att installation av tak- eller fasadintegrerade solpaneler i vissa fall kan bedömas som en fasadändring."),
    ("Behövs bygglov för att byta från tegel till plåt på villan i Botkyrka?",
     "Normalt inte, men om huset eller området är särskilt värdefullt eller har skyddsbestämmelser gäller utökad lovplikt och då krävs bygglov."),
    ("Kan en ny takkupa påverka bygglovet i Botkyrka?",
     "Ja. Större eller flera takkupor kräver bygglov enligt kommunen, och en ny takkupa kan påverka husets byggnadshöjd."),
    ("Kan en antenn eller ett aggregat på taket vara en fasadändring i Botkyrka?",
     "Ja. Kommunen skriver att antenner och aggregat för ventilation, kyla och värme kan betraktas som fasadändring när de monteras, flyttas eller ändras på fasad eller tak."),
    ("Vilka egenskaper räknar Botkyrka som husets karaktärsdrag?",
     "Storlek, färg, utvändiga materialval, byggnadsstil, ålder, detaljer och proportioner."),
  ],
  "sources": [_PBL, _BOT_FAS, _BOT_TAK, _BOT_KUPA, _SKV, _SKV2],
  "cta": ("Ska taket i Botkyrka bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och dina planer innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa med nylagt rött tegeltak och en ny takkupa under ställning",
     "Swedish one-and-a-half storey villa with white rendered facade and a newly laid red clay tile roof with a new dormer being finished, scaffolding along the side, garden with lilac bushes, Stockholm southern suburb, summer daylight" + _IMG_END),
    ("Nya röda takpannor läggs på läkt längs takfoten, ställning vid sidan",
     "roof-integrated black solar panels laid flush with surrounding dark roof tiles on a pitched Swedish villa roof, neat metal flashing around the panel field, clear sky" + _IMG_END),
    ("Nyuppbyggd stomme till en takkupa på ett tak med ny underlagsduk",
     "close-up architectural detail photo of a newly framed timber dormer opening in a pitched roof, rafters and fresh roof boarding with grey underlay membrane, still life, deserted, calm Sunday, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VALLENTUNA
"takbyte-vallentuna.html": {
  "kind": "district", "service": "takbyte", "ort": "Vallentuna", "svc_label": "Takbyte",
  "title": "Takbyte i Vallentuna – lovfrågan, skorstenen och ritningarna",
  "description": "Takbyte i Vallentuna: när nytt tak kräver bygglov, handlingarna till ansökan, skorsten och eldstad med sotarintyg och husets ritningar i bygglovsarkivet.",
  "h1": "Takbyte i Vallentuna",
  "lead": "Vallentuna kommun svarar kort på frågan om nytt tak: för ett en- eller tvåbostadshus krävs inget bygglov. Men det finns undantag, och skorstenen har egna regler. Geal Entreprenad AB byter tak på villor och gårdar i hela Vallentuna och börjar med husets egna ritningar.",
  "card": "Lovfrågan, skorstenen och arkivet.",
  "sections": [
    {"id": "lov-vallentuna", "anchor": "Lovfrågan",
     "h2": "Inget bygglov – med två undantag",
     "paras": [
       "Ommålning, nytt tak eller nya fönster kräver inte bygglov för ett en- eller tvåbostadshus, skriver Vallentuna kommun. Ändringar ska ändå göras varsamt och anpassas till byggnadens värden. Bygglov krävs om fastigheten ligger inom ett kulturhistoriskt särskilt värdefullt område eller om byggnaden är kulturhistoriskt särskilt värdefull. Det krävs också om ändringen görs på en fasad eller ett tak mot allmän plats, men det gäller bara flerbostadshus.",
       "Plan- och bygglagen räknar byte av taktäckningsmaterial som fasadändring, så frågan uppstår främst när materialet eller färgen ändras. Vi går igenom detaljplanen och husets historia vid platsbesöket, och behövs lov tar vi fram handlingarna.",
     ],
     "aside": {"title": "Bygglov krävs när", "items": [
       "Området är kulturhistoriskt särskilt värdefullt", "Byggnaden är kulturhistoriskt särskilt värdefull",
       "Taket vetter mot allmän plats på ett flerbostadshus"]}},
    {"id": "handlingar-vallentuna", "h2": "Handlingarna om lov krävs",
     "paras": [
       "Till en ansökan om bygglov för fasadändring vill kommunen ha en situationsplan baserad på tomtkartan med den berörda byggnaden ikryssad, fasadritningar i skala 1:100 på de berörda fasaderna, en redovisning av utvändiga material och kulörer med NCS-koder och en kontrollplan. Materialen kan anges på ansökningsblanketten eller på fasadritningarna.",
       "Ritningarna ska ha information om vad de visar, skala och fastighetsbeteckning, alla mått i millimeter och norrpil på situationsplanen, och de ska lämnas in i en omgång och vara fackmannamässigt utförda. Äldre ritningar kan beställas om de finns i kommunens arkiv, och det sparar arbete när fasaderna ska ritas.",
     ],
     "aside": None},
    {"id": "skorsten-vallentuna", "h2": "Skorstenen och eldstaden",
     "paras": [
       "För skorstenens höjd och placering på taket hänvisar kommunen till Boverkets regler. Bygglov krävs när en ny skorsten ska placeras på fasaden eller när en befintlig utanpåliggande skorsten ska ändras. Installerar du en eldstad, till exempel en braskamin, kakelugn, panna, braskassett eller spisinsats, krävs en anmälan, och det gäller också vid byte från kakelugn till braskamin eller omvänt.",
       "Installationen får inte börja förrän startbeskedet har kommit, och du får inte elda förrän du har fått slutbesked. Slutbeskedet ges när du har lämnat in en ifylld kontrollplan och ett sotarintyg utan anmärkningar. Till anmälan hör planritning med eldstadens placering, fasadritning med skorstenen eller rökröret inritat och prestandadeklarationer för eldstad och skorsten. Vi plåtar in skorstenen mot det nya taket så att den är tät när sotaren besiktigar.",
     ],
     "aside": {"title": "Till anmälan av eldstad", "items": [
       "Situationsplan 1:500", "Planritning med eldstaden", "Fasadritning med skorsten",
       "Prestandadeklarationer", "Kontrollplan"]}},
    {"id": "arkivet-vallentuna", "h2": "Takfallen i bygglovsarkivet",
     "paras": [
       "Kommunens digitala bygglovsarkiv har ritningar för byggnader uppförda ungefär mellan 1950 och 2024, och cirka 75 procent av handlingarna är digitaliserade. Sektionsritningen visar byggnaden i genomskärning med bland annat våningshöjder och takfall, och fasadritningen visar huset utifrån. Allt finns i skala 1:100.",
       "Med husets egna ritningar kan vi räkna på takytan och lutningen redan innan platsbesöket och se hur taket var tänkt från början. Om takens epoker i kommunen kan du läsa under " + _L.format("takrenovering-vallentuna.html", "takrenovering i Vallentuna") + ", om plåt och rännor under " + _L.format("platslagare-vallentuna.html", "plåtslagare i Vallentuna") + " och om våra tjänster i stort under " + _L.format("taklaggare-vallentuna.html", "takläggare i Vallentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Vallentuna till",
  "steps": [
    ("Ritningar", "Husets sektion och fasader hämtas från bygglovsarkivet."),
    ("Platsbesök", "Tak, underlag, skorsten och detaljplan går vi igenom."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag, ytskikt, plåt och skorstensarbete står var för sig."),
    ("Lov och anmälan", "Bygglov i värdefulla miljöer och anmälan för eldstad när det behövs."),
    ("Takbyte", "Gammalt tak rivs, underlaget ses över och nytt tak läggs."),
    ("Genomgång", "Vi går igenom taket och skorstensplåten med dig."),
  ],
  "rot_h2": "ROT-avdrag för takbyte i Vallentuna",
  "rot": [
    "Byte och reparation av takpannor och hängrännor på ett småhus är rotarbete enligt Skatteverket, liksom att byta plåttak och stuprör och att montera och montera ner byggnadsställningar. Rotavdrag ges för en bostad som du äger och bor i eller använder som fritidsbostad.",
    _ROT_AMT,
  ],
  "price_h2": "Vad påverkar priset för takbytet i Vallentuna?",
  "price": [
    "Takets yta och lutning, materialet, hur mycket underlag som behöver bytas, skorstenens skick och plåtdetaljerna, och om ett bygglov med ritningar behövs. Läs mer i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs bygglov för nytt tak på en villa i Vallentuna?",
     "Normalt inte. Kommunen kräver bygglov bara om fastigheten ligger i ett kulturhistoriskt särskilt värdefullt område eller om byggnaden är kulturhistoriskt särskilt värdefull."),
    ("Behövs bygglov för en ny skorsten i Vallentuna?",
     "Ja, om den nya skorstenen placeras på fasaden eller om en befintlig utanpåliggande skorsten ändras. För höjd och placering på taket gäller Boverkets regler."),
    ("När får vi börja elda i den nya kaminen i Vallentuna?",
     "När slutbeskedet har kommit. Det ges efter att du har lämnat in en ifylld kontrollplan och ett sotarintyg utan anmärkningar."),
    ("Behöver vi anmäla bytet från öppen spis till braskassett i Vallentuna?",
     "Ja. Kommunen skriver att även ett byte från öppen spis till braskassett eller spisinsats, som kan ändra eldningsförhållanden och rökgastemperaturer, kräver anmälan."),
    ("Hittar vi ritningar på vårt tak i Vallentunas arkiv?",
     "Om huset är byggt ungefär 1950–2024 finns ritningarna ofta digitalt. Sektionsritningen visar takfallen, och det som inte är digitaliserat kan beställas."),
  ],
  "sources": [_PBL, _VAL_FAS, _VAL_ELD, _VAL_ARK, _SKV, _SKV2],
  "cta": ("Ska taket i Vallentuna bytas?", "Boka ett gratis platsbesök, så går vi igenom taket och skorstenen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa från 1980-talet med nytt rött betongpannetak och murad skorsten",
     "1980s Swedish villa with light wooden facade and a newly laid red concrete tile roof, a plastered brick chimney with new metal flashing, scaffolding at one gable, birch trees and lawn, Uppland suburb, clear daylight" + _IMG_END),
    ("Skorsten med ny plåtinfästning och sotarlucka på ett nylagt tak",
     "close-up of a brick chimney on a newly laid tile roof with fresh black sheet metal flashing, a roof ladder and a small walkway leading to it, blue sky" + _IMG_END),
    ("Gamla ritningar med husets sektion och takfall på ett bord",
     "old architectural drawings showing a house cross-section with roof pitch, spread on a wooden table next to a folding ruler and a pencil, soft window light, no readable text" + _IMG_END),
  ],
},
}
