# -*- coding: utf-8 -*-
"""Totalrenovering – ortsidor v25: Botkyrka, Ekerö, Haninge, Järfälla, Norrtälje, Vallentuna (2026-10-26).
Tjänst under villarenovering.html (TJ_HUB["totalrenovering"]). Intent: renovera hela huset på en gång – skild från
ortens byggforetag-<ort>.html och från enskilda rum (badrumsrenovering-/koksrenovering-<ort>.html), som länkas.
Skild från v18/v21/v23 (ordningen, varsam rivning, nyköpt hus, asbest och PCB, bostadsrätten, stommen, värmesystem,
radon före och efter i Sollentuna, ny el, stambyte, bo kvar, eldstäder i Vasastan, småstugor, eternit och
ventilation, villastäder och bärande, avfall och arkiv, nya byggregler och VA, fritidshus som blir permanentboende).
Tre bilder per sida: img[0] hero 4:3, img[1]–[2] 3:2.

Lokal vinkel per sida (en huvudfråga per sida):
Botkyrka – Tullinge: från stationssamhälle med fritidshus till storstadens förort (utvecklingsprogrammet), hus som
  byggts i omgångar, du som byggherre (kommunens definition), bygglovsarkivet, bergvärme hos miljöenheten.
Ekerö – braskamin, kassett och bränslebyte i en renovering (kommunens krav på anmälan, handlingar och sotarintyg),
  större fönster och bärande reglar, kommunens nya bedömning av särskilt värdefulla byggnader, anmälan till
  Roslagsvatten; villakommunen enligt kulturmiljöprogrammet.
Haninge – folkhemmets villor och kedjehus 1940–60 (karaktärsmiljöerna: renovera inifrån, behåll fönster, dörrar
  och fasad), bärande konstruktion (anmälan, konstruktionsritningar, bygglovsarkivet), anmälan om VA-arbete.
Järfälla – kök och badrum som flyttas: stammar i nya lägen kräver anmälan, rörgenomföringar i grunden och ny radonmätning
  (kommunens radonsida: blå lättbetong, mätperiod, referensvärde), kulturmiljöplanen (Dressyrvägens 1960-talshus).
Norrtälje – egen brunn och eget avlopp: WC på BDT-avlopp kräver tillstånd, toalett med mer spolvatten och fler
  byggnader kräver anmälan sex veckor före, brunnsvattnet (Livsmedelsverkets råd via kommunen, saltvatten vid kusten);
  landsbygdskommunen.
Vallentuna – radon när huset byggs om (kommunens radonsida: när man bör mäta, mätperiod, blåbetong, radonbidrag
  före sanering, kartan över mätningar), småhusens andel enligt ÖP 2040.

Fakta endast från källorna i respektive 'sources', öppnade med urllib (Mozilla-UA) 2026-10-26, alla 200;
pdf:erna har textlager. Skatteverkets sidor svarade inte härifrån – samma URL:er och ROT-formuleringar som v23.
Strukna / ej använda: avgifter, handläggningstider (Ekerö, Norrtälje, Järfälla), miljösanktionsavgifternas belopp,
namn på analysföretag, alla priser, garantier, omdömen och cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_IMG_END = ", realistic photo, no people, no hands, no text, no letters"

_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_BOT = "https://www.botkyrka.se/boende-och-narmiljo/bygglov-och-tillstand/sa-soker-du-bygglov/bygglov-a-o/"
_BOT_TULL = ("Botkyrka kommun – Framtid för Tullinge, utvecklingsprogram (pdf)",
             "https://botkyrka.se/download/18.1fbbaae6170bff9469deb44/1584093808003/Tullinge%20utvecklingsprogram.pdf")
_BOT_HERRE = ("Botkyrka kommun – Byggherre", _BOT + "byggherre")
_BOT_ARKIV = ("Botkyrka kommun – Bygglovsarkiv", _BOT + "bygglovsarkiv")
_BOT_BERG = ("Botkyrka kommun – Bergvärme", _BOT + "bergvarme")
_EKE_BYGG = ("Ekerö kommun – Vad vill du bygga?", "https://www.ekero.se/bygga-bo-miljo/bygga-nytt-andra-eller-riva/vad-vill-du-bygga")
_EKE_KMP = ("Ekerö kommun – Kulturmiljöprogram (pdf)",
            "https://www.ekero.se/download/18.553838ea17305720c321ec82/1597925412772/Eker%C3%B6%20kulturmilj%C3%B6program.pdf")
_HAN_KAR = ("Haninge kommun – Haninges karaktärsmiljöer (pdf)",
            "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf")
_HAN_BAR = ("Haninge kommun – Ändring av bärande konstruktion",
            "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/andring-av-barande-konstruktion/")
_HAN_VA = ("Haninge kommun – Anmälan om vatten- och avloppsarbete", "https://www.haninge.se/sjalvservice/vatten--och-avloppsarbete--anmal/")
_JAR_VA = ("Järfälla kommun – Installation eller ändring av vatten och avlopp (VA)",
           "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/installationellerandringavvattenochavloppva.4.69a1b161151015104f4bd741.html")
_JAR_RADON = ("Järfälla kommun – Radon", "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/inomhusmiljo/radon.4.40b7e74714b9b24883d321c4.html")
_JAR_BAR = ("Järfälla kommun – Ändra i bärande konstruktion",
            "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/andraibarandekonstruktion.4.69a1b161151015104f4bca0b.html")
_JAR_KMP = ("Järfälla kommun – Kulturmiljöplan för Järfälla, inledning (pdf)",
            "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4052/1550245824984/kulturmiljoplan-inledning.pdf")
_NOR_AVL = ("Norrtälje kommun – Enskilt avlopp", "https://www.norrtalje.se/info/bygga-bo-miljo/vatten-och-avlopp/enskilda-avlopp/")
_NOR_VAT = ("Norrtälje kommun – Enskilt vatten", "https://www.norrtalje.se/info/bygga-bo-miljo/vatten-och-avlopp/enskilt-vatten/")
_NOR_FAKTA = ("Norrtälje kommun – Fakta och statistik (landsbygd och skärgård)",
              "https://www.norrtalje.se/info/bygga-bo-miljo/norrtalje-vaxer/landsbygd-skargard/fakta-och-statistik/")
_VALL_RADON = ("Vallentuna kommun – Radon", "https://www.vallentuna.se/bygga-bo-och-miljo/miljo-energi-och-halsoskydd/halsoskydd/radon")
_VALL_OP = ("Vallentuna kommun – Översiktsplan 2040 (pdf)",
            "https://vallentuna.se/download/18.63572f8619eeecafce08366/1782478377449/2.11.7%20%C3%96versiktsplan%202040.pdf")

_ROT_SMAHUS = ("För ett småhus räknar Skatteverket bland annat att riva väggar och bygga om planlösningen, arbeta med "
               "tilläggsisolering, sätta kakel och klinker och göra förbättringsarbeten som rotarbete.")
_ROT_SUM = ("Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år, och äger ni huset "
            "två kan båda göra avdrag. Material och resor ger inget avdrag.")

PAGES_TJ = {

# ------------------------------------------------------------------ BOTKYRKA
"totalrenovering-botkyrka.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Botkyrka", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Botkyrka – Tullingehuset i omgångar",
  "description": "Totalrenovering i Botkyrka: hus i Tullinge som byggts om i omgångar, ditt ansvar som byggherre, ritningar i bygglovsarkivet och bergvärme.",
  "h1": "Totalrenovering i Botkyrka",
  "lead": "Många hus i Tullinge och andra delar av Botkyrka har byggts till och om i flera omgångar, från sommarstuga till villa. Geal Entreprenad AB totalrenoverar villor i Botkyrka och börjar med att ta reda på vad huset egentligen består av.",
  "card": "Tullingehuset i omgångar.",
  "sections": [
    {"id": "tullinge-botkyrka", "anchor": "Tullinge",
     "h2": "Från stationssamhälle till storstad",
     "paras": [
       "Botkyrkas utvecklingsprogram för Tullinge beskriver en stadsdel som förändrats från ett litet stationssamhälle med inslag av fritidshus till en del av storstaden Stockholm. Under de trettio åren före programmet mer än fördubblades befolkningen.",
       "Programmet beskriver också vad Tullingeborna värdesätter: en omväxlande miljö med slingrande gator i kuperad terräng och charmiga hus från olika epoker. För den som köper ett äldre hus här betyder det ofta att huset har vuxit i takt med samhället.",
     ],
     "aside": {"title": "Tullinge enligt programmet", "items": [
       "Stationssamhälle med inslag av fritidshus", "Befolkningen mer än fördubblad på trettio år", "Hus från olika epoker i kuperad terräng"]}},
    {"id": "omgangar-botkyrka", "h2": "Ett hus som byggts i omgångar",
     "paras": [
       "Ett hus som började som sommarstuga och sedan byggts till har ofta flera delar med olika grund, stomme och isolering. Övergångarna mellan delarna är ställen där fukt, sättningar och kalla golv kan uppstå.",
       "Därför börjar en totalrenovering med att vi kartlägger huset del för del. Vi lyfter golv och öppnar väggar på några ställen innan kostnadsförslaget skrivs, så att du vet vad det är vi räknar på.",
     ],
     "aside": {"title": "Vi kartlägger", "items": [
       "Grund och golv i varje husdel", "Övergångar mellan tillbyggnader", "Stomme och isolering", "El, vatten och avlopp"]}},
    {"id": "arkivet-botkyrka", "anchor": "Bygglovsarkivet",
     "h2": "Ritningarna i bygglovsarkivet",
     "paras": [
       "I Botkyrkas bygglovsarkiv kan du se och hämta handlingar som tillhör avslutade bygglovsärenden, till exempel ritningar. Du når arkivet genom kommunens e-tjänst och behöver veta adressen eller fastighetsbeteckningen. Pågående ärenden syns inte i arkivet.",
       "Ritningarna visar vad som söktes, men i ett hus som byggts om flera gånger kan verkligheten skilja sig från dem. Vi jämför arkivets ritningar med det vi ser på plats och tar in en konstruktör där bärande väggar ska ändras.",
     ],
     "aside": None},
    {"id": "isolering-botkyrka", "anchor": "Värme och isolering",
     "h2": "Värme och isolering i ett hus med flera delar",
     "paras": [
       "I ett hus som vuxit i omgångar kan den äldsta delen vara klenare isolerad än tillbyggnaden. När huset totalrenoveras får du en chans att jämna ut skillnaden, men det behöver göras med omsorg om fukten. Vi går igenom golv, väggar och vind i varje del och föreslår åtgärder som passar konstruktionen där.",
       "Det är också nu som el och vatten lämpligast dras om, eftersom väggar och golv ändå är öppna. Ett gemensamt grepp om alla installationer gör att huset fungerar som ett hus i stället för flera.",
     ],
     "aside": {"title": "Passar att göra samtidigt", "items": [
       "Isolering där väggar och golv är öppna", "Ny el i hela huset", "Nya vatten- och avloppsledningar", "Byte av uppvärmning"]}},
    {"id": "byggherre-botkyrka", "h2": "Du är byggherre",
     "paras": [
       "Botkyrka kommun förklarar att byggherre är den som för egen räkning utför eller låter utföra projekterings-, byggnads-, rivnings- eller markarbeten. Det är alltså du som beställer arbetet som är byggherre, inte entreprenören som gör det.",
       "Byggherren har det fulla ansvaret för att samhällskraven uppfylls och ska bland annat utöva egenkontroll och upprätta kontrollplaner. Vi tar fram kontrollplanen tillsammans med dig och fyller i den under arbetet, så att du har underlaget när kommunen frågar efter det.",
     ],
     "aside": None},
    {"id": "bergvarme-botkyrka", "h2": "Bergvärme i samma renovering",
     "paras": [
       "Många passar på att byta uppvärmning när huset ändå byggs om. Kommunen skriver att bergvärme inte är en bygglovspliktig åtgärd, men att tillstånd för bergvärme söks hos kommunens miljöenhet.",
       "Ska radiatorer flyttas eller golvvärme läggas behöver det samordnas med borrningen och med el och VVS. Om badrummet och köket kan du läsa under " + _L.format("badrumsrenovering-botkyrka.html", "badrumsrenovering i Botkyrka") + " och " + _L.format("koksrenovering-botkyrka.html", "köksrenovering i Botkyrka") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Botkyrka till",
  "steps": [
    ("Arkivet", "Ritningar från avslutade ärenden hämtas ur bygglovsarkivet."),
    ("Platsbesök och kartläggning", "Varje husdel undersöks, med öppningar där det behövs."),
    ("Skriftligt kostnadsförslag", "Varje del och varje moment står för sig."),
    ("Anmälan och kontrollplan", "Bärande ändringar och installationer anmäls i tid."),
    ("Renovering", "Arbetet sker i den ordning som huset kräver."),
    ("Slutbesked", "Kontrollplanen fylls i och lämnas till kommunen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Botkyrka",
  "rot": [
    _ROT_SMAHUS,
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Botkyrka?",
  "price": [
    "Hur många husdelar som finns, skicket på grund och stomme, el och VVS och vilka ytskikt du väljer. Läs mer under " + _L.format("villarenovering.html", "villarenovering") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Var hittar vi ritningar till vårt hus i Tullinge?",
     "I Botkyrkas bygglovsarkiv, via kommunens e-tjänst. Du behöver adressen eller fastighetsbeteckningen, och bara avslutade ärenden syns."),
    ("Är det vi eller byggfirman som är byggherre?",
     "Det är du som beställer arbetet. Byggherren har fullt ansvar för att samhällskraven uppfylls och ska utöva egenkontroll."),
    ("Vem fyller i kontrollplanen?",
     "Byggherren ansvarar för den, men vi tar fram den tillsammans med dig och fyller i våra kontroller under arbetet."),
    ("Behöver vi bygglov för bergvärme?",
     "Nej, men tillstånd söks hos kommunens miljöenhet."),
    ("Kan vi bo kvar under renoveringen?",
     "Ibland, om arbetet delas upp i etapper. I ett hus där el, vatten och golv byts i alla delar är det ofta enklare att flytta ut en period."),
    ("Varför vill ni öppna väggar innan ni lämnar pris?",
     "I ett hus som byggts i omgångar kan delarna vara byggda på olika sätt. Några öppningar ger ett säkrare kostnadsförslag."),
  ],
  "sources": [_BOT_TULL, _BOT_ARKIV, _BOT_HERRE, _BOT_BERG, _SKV, _SKV2],
  "cta": ("Ska huset i Botkyrka totalrenoveras?", "Boka ett gratis platsbesök, så kartlägger vi huset innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa på en kuperad tomt med tillbyggnader från olika tider",
     "Swedish wooden villa on a hilly wooded plot, original small 1930s summer cottage part with red facade joined to a later larger extension with light grey panel, granite rocks and pine trees, winding gravel road, Tullinge, summer" + _IMG_END),
    ("Ljust vardagsrum med vita väggar efter renovering",
     "still life inside a house under renovation: floorboards lifted where an old cottage part meets a later extension, showing two different floor joist structures side by side, work lamp, daylight" + _IMG_END),
    ("Nyrenoverat vardagsrum med öppen planlösning",
     "bright newly renovated open-plan living room in a Swedish villa with light oak floor, white walls, large windows towards a wooded garden, modern kitchen in the background, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ EKERÖ
"totalrenovering-ekero.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Ekerö", "svc_label": "Totalrenovering",
  "title": "Totalrenovering på Ekerö – braskamin och större fönster",
  "description": "Totalrenovering på Ekerö: braskamin, kassett och bränslebyte, vad anmälan ska innehålla, större fönster i bärande vägg och värdefulla byggnader.",
  "h1": "Totalrenovering på Ekerö",
  "lead": "När ett hus på Ekerö totalrenoveras vill många ha en braskamin i vardagsrummet och större fönster mot sjön. Geal Entreprenad AB totalrenoverar villor på Ekerö och tar med eldstaden och fönstren i anmälan från början.",
  "card": "Braskamin och större fönster.",
  "sections": [
    {"id": "villorna-ekero", "anchor": "Villakommunen",
     "h2": "En villakommun som vuxit snabbt",
     "paras": [
       "Ekerö kommuns kulturmiljöprogram berättar att kommunen har fördubblat sin befolkning sedan 1970, och att villabebyggelsen ökat kraftigt. Kring östra Ekerö och södra Färingsö dominerar småhus från 1900-talets andra hälft, och under 1990- och 2000-talet tillkom inte mindre än 2 475 villor.",
       "Programmet nämner också att fritidshus permanentas i snabb takt. Många av husen som renoveras i dag är alltså byggda för en annan tid och ett annat sätt att bo, och en totalrenovering handlar ofta om att anpassa dem till helårsboende med dagens krav.",
     ],
     "aside": {"title": "Ekerö enligt programmet", "items": [
       "Befolkningen fördubblad sedan 1970", "2 475 nya villor på 1990- och 2000-talet", "Fritidshus permanentas i snabb takt"]}},
    {"id": "eldstaden-ekero", "h2": "Braskamin och kassett kräver anmälan",
     "paras": [
       "Kommunen skriver att du ska göra en anmälan till bygglovsenheten om du vill installera eller göra en större ändring av en eldstad, braskamin, öppen spis eller kakelugn. Det gäller också om du vill installera eller byta ut en spisinsats i en befintlig öppen spis, och om du byter bränsle i din eldstad.",
       "I en totalrenovering är det lätt att eldstaden hamnar sist i planeringen. Vi tar med den i samma anmälan som övriga ändringar, så att skorsten, bjälklag och brandskydd planeras tillsammans med resten av huset.",
     ],
     "aside": {"title": "Anmälan krävs för", "items": [
       "Ny eldstad, braskamin eller kakelugn", "Större ändring av befintlig eldstad", "Ny eller bytt spisinsats i öppen spis", "Byte av bränsle"]}},
    {"id": "handlingarna-ekero", "anchor": "Handlingarna",
     "h2": "Det här ska anmälan innehålla",
     "paras": [
       "Enligt kommunen ska anmälan innehålla en planritning med eldstadens placering, en fasadritning med skorstenen eller rökkanalen inritad, en kontrollplan och typgodkännande, produktbeskrivning eller CE-märkning.",
       "När installationen är klar ska du skicka in ett sotarintyg, den ifyllda kontrollplanen och en ansökan om slutbesked. Vi samlar handlingarna under arbetet, så att eldstaden kan tas i bruk när slutbeskedet finns.",
     ],
     "aside": {"title": "Efter installationen", "items": [
       "Sotarintyg", "Ifylld kontrollplan", "Ansökan om slutbesked"]}},
    {"id": "fonstren-ekero", "h2": "Större fönster i en bärande vägg",
     "paras": [
       "Kommunen skriver att du behöver göra en anmälan om du gör förändringar som väsentligt påverkar brandskydd eller bärande konstruktion, och ger nya reglar för ett större fönster som exempel. Kräver åtgärden ändå bygglov hanteras allt i samma ansökan.",
       "Ett större fönster mot sjön betyder ofta att en del av ytterväggen måste bära på ett nytt sätt. Vi låter en konstruktör dimensionera öppningen och tar med den i anmälan. Samtidigt ser vi över hur det större fönstret påverkar värmen och solinstrålningen i rummet. Om fönsterbyte i övrigt kan du läsa under " + _L.format("fonsterbyte-ekero.html", "fönsterbyte på Ekerö") + ".",
     ],
     "aside": None},
    {"id": "vardefulla-ekero", "h2": "Kommunens nya bedömning",
     "paras": [
       "Ekerö kommun har gjort en ny bedömning av sina särskilt värdefulla byggnader och områden efter ändringarna i plan- och bygglagen, och visar resultatet som undantagsområden i Ekerökartan. Kommunen skriver att det ofta beror på var fastigheten ligger om du kan åberopa ändringarna.",
       "Ligger huset i ett sådant område kan fasadändringar som större fönster kräva bygglov. Ska huset anslutas till kommunalt vatten och avlopp skickar du en anmälan till Roslagsvatten i god tid före byggstart. Om badrum och kök kan du läsa under " + _L.format("badrumsrenovering-ekero.html", "badrumsrenovering på Ekerö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering på Ekerö till",
  "steps": [
    ("Platsbesök", "Vi går igenom huset, skorstenen och var fönstren kan bli större."),
    ("Kartan", "Vi kontrollerar om fastigheten ligger i ett undantagsområde."),
    ("Anmälan", "Eldstad, bärande ändringar och kontrollplan i samma ärende."),
    ("Skriftligt kostnadsförslag", "Varje del och varje moment står för sig."),
    ("Renovering", "Arbetet startar när startbeskedet finns."),
    ("Slutbesked", "Sotarintyg och kontrollplan lämnas till kommunen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen på Ekerö",
  "rot": [
    _ROT_SMAHUS,
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen på Ekerö?",
  "price": [
    "Husets storlek och skick, nya öppningar i bärande väggar, eldstaden och skorstenen, el och VVS och vilka ytskikt du väljer. Läs mer under " + _L.format("villarenovering.html", "villarenovering") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi göra en anmälan för en ny braskamin i vårt hus på Ekerö?",
     "Ja. Kommunen kräver anmälan för att installera eller göra en större ändring av en eldstad, och även för att sätta in en spisinsats eller byta bränsle."),
    ("Gäller anmälan även om vi bara byter till en ny kamin?",
     "Kommunen kräver anmälan för installation och större ändring av eldstäder. Vi går igenom vad som gäller för just ert byte innan arbetet börjar."),
    ("Vad ska vi skicka in när kaminen är klar?",
     "Ett sotarintyg, den ifyllda kontrollplanen och en ansökan om slutbesked."),
    ("Kräver ett större fönster anmälan?",
     "Ja, om nya reglar behövs eller bärande konstruktion påverkas väsentligt. Kommunen nämner just ett större fönster som exempel."),
    ("Ska vi anmäla något till Roslagsvatten?",
     "Ja, om byggnaden ska anslutas till kommunalt vatten och avlopp. Anmälan görs i god tid innan byggstart."),
    ("Hur vet vi om huset ligger i ett värdefullt område?",
     "Kommunen visar sina undantagsområden i Ekerökartan efter sin nya bedömning av särskilt värdefulla byggnader och områden."),
  ],
  "sources": [_EKE_KMP, _EKE_BYGG, _SKV, _SKV2],
  "cta": ("Ska huset på Ekerö totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom huset, eldstaden och fönstren innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa vid Mälaren med stora fönster mot sjön",
     "Swedish 1970s villa with dark wooden facade and large new windows facing a calm lake, lawn sloping down to the water, birch and pine trees, Lake Mälaren islands, summer evening" + _IMG_END),
    ("Ny braskamin med skorsten i ett renoverat vardagsrum",
     "newly installed black cast iron wood stove with a steel chimney pipe on a stone hearth plate in a renovated Swedish living room, white walls, wooden floor, stacked firewood beside, daylight" + _IMG_END),
    ("Ny fönsteröppning med förstärkta reglar i en yttervägg",
     "still life inside a house under renovation: a wider new window opening in a timber-framed exterior wall with doubled studs and a new lintel above, insulation visible, view to the garden outside, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ HANINGE
"totalrenovering-haninge.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Haninge", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Haninge – folkhemsvillan inifrån",
  "description": "Totalrenovering i Haninge: folkhemmets villor och kedjehus, renovera inifrån och behålla fasad, fönster och dörrar, bärande väggar och VA-anmälan.",
  "h1": "Totalrenovering i Haninge",
  "lead": "I Handen, Jordbro, Vendelsö och Västerhaninge finns många villor och kedjehus från folkhemsåren, och kommunen råder ägarna att värna husens utsida. Geal Entreprenad AB totalrenoverar sådana hus i Haninge och gör det mesta av arbetet inifrån.",
  "card": "Folkhemsvillan inifrån.",
  "sections": [
    {"id": "folkhemmet-haninge", "anchor": "Folkhemmets villor",
     "h2": "Folkhemmets villor och kedjehus",
     "paras": [
       "Haninges karaktärsmiljöer beskriver hur småhusen främst växte fram längs Nynäsbanan, som invigdes 1901. Områdena från folkhemsbygget 1940–1960 består av små enhetliga villor, kedjehus eller radhus i grupphusbebyggelse, med god och funktionell utformning.",
       "1940-talets hus är ofta enkla en- eller tvåplansvillor i trä, puts eller fasadtegel med sadeltak eller valmat tak. 1950-talets områden är mer individuellt utformade, med rött eller gult tegel kombinerat med grov spritputs eller trä i mustiga kulörer. Som exempel nämns Handen, Jordbro, Vendelsö, Vendelsömalm och Västerhaninge.",
     ],
     "aside": {"title": "Exempel i karaktärsmiljöerna", "items": [
       "Handen", "Jordbro", "Vendelsö och Vendelsömalm", "Västerhaninge"]}},
    {"id": "inifran-haninge", "h2": "Renovera inifrån",
     "paras": [
       "Kommunens råd för de här områdena är tydliga: byggnadernas bärande karaktärsdrag bör värnas vid om- och tillbyggnader, och större exteriöra ändringar som tilläggsisolering eller tillbyggnad i fasad mot allmän plats bör undvikas. Fasadändringar som avviker från den ursprungliga utformningen ska undvikas, och en tegelfasad ska till exempel inte putsas.",
       "Råden gäller alla småhusområden i kommunen från 1940–60-talet, även de som inte är utpekade som särskilt värdefulla. För en totalrenovering betyder det att energiåtgärder och nya planlösningar i första hand görs inifrån, medan fasaden underhålls i sitt ursprungliga utförande. Vinden, golven och installationerna är där de stora förbättringarna oftast kan göras utan att husets utsida ändras.",
     ],
     "aside": {"title": "Kommunens råd", "items": [
       "Värna husens bärande karaktärsdrag", "Undvik tilläggsisolering mot gatan", "Putsa inte en tegelfasad", "Utgå från originalets fönster och dörrar"]}},
    {"id": "fonster-haninge", "anchor": "Fönster och dörrar",
     "h2": "Fönster och dörrar",
     "paras": [
       "Karaktärsmiljöerna beskriver dörrar och fönster som en bärande del av byggnadens karaktär. Ursprunglig utformning och färgsättning ska värnas och vara utgångspunkt vid förändring.",
       "I en totalrenovering är fönstren ofta en av de största posterna. Vi går igenom om de går att renovera, eller om nya fönster kan göras med samma indelning och proportioner. Läs mer under " + _L.format("fonsterrenovering-haninge.html", "fönsterrenovering i Haninge") + " och " + _L.format("fonsterbyte-haninge.html", "fönsterbyte i Haninge") + ".",
     ],
     "aside": None},
    {"id": "barande-haninge", "h2": "Bärande väggar och öppen planlösning",
     "paras": [
       "Många vill öppna upp mellan kök och vardagsrum. Haninge kommun skriver att ändringar som påverkar byggnadens bärande konstruktion eller stomme kräver en anmälan, och att du behöver startbesked innan arbetet börjar. Är du osäker på om en vägg är bärande ska du kontakta en konstruktör.",
       "Ritningar som visar husets bärande delar kan ibland finnas i kommunens bygglovsarkiv. Kommunen skriver att konstruktionsritningar ska lämnas in, och att de ska tas fram av konstruktörer och vara fackmannamässigt redovisade. En kontrollplan hör också till anmälan.",
     ],
     "aside": None},
    {"id": "va-haninge", "h2": "Anmälan om vatten och avlopp",
     "paras": [
       "Ska du installera eller ändra anordningar för vattenförsörjning eller avlopp i huset eller på tomten ska du enligt kommunen göra en anmälan om VA-arbete. Det sker med en blankett till kommunens VA-verksamhet.",
       "Kommunen påpekar att den inte har information om hur ledningarna går innanför fastighetsgränsen. Därför filmar eller provar vi befintliga ledningar innan nya badrum och kök placeras. Om badrummet kan du läsa under " + _L.format("badrumsrenovering-haninge.html", "badrumsrenovering i Haninge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Haninge till",
  "steps": [
    ("Platsbesök", "Vi går igenom huset, fasaden, fönstren och planlösningen."),
    ("Arkivet", "Ritningar hämtas ur bygglovsarkivet där de finns."),
    ("Konstruktör och anmälan", "Bärande ändringar och VA-arbete anmäls."),
    ("Skriftligt kostnadsförslag", "Varje del och varje moment står för sig."),
    ("Renovering inifrån", "Fasaden underhålls, nytt görs inne i huset."),
    ("Slutbesked", "Kontrollplanen fylls i och lämnas till kommunen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Haninge",
  "rot": [
    _ROT_SMAHUS,
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Haninge?",
  "price": [
    "Husets storlek och skick, om bärande väggar ändras, fönstren, el och VVS och vilka ytskikt du väljer. Läs mer under " + _L.format("villarenovering.html", "villarenovering") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi tilläggsisolera fasaden på vår 50-talsvilla i Haninge?",
     "Kommunen råder att större exteriöra ändringar som tilläggsisolering mot allmän plats bör undvikas i småhusområden från 1940–60-talet. Ofta går det att isolera inifrån eller på vinden i stället."),
    ("Behövs anmälan för att ta bort en vägg mellan kök och vardagsrum?",
     "Ja, om väggen är bärande. Då krävs anmälan, konstruktionsritningar och startbesked innan arbetet börjar."),
    ("Kan vi putsa över tegelfasaden när vi ändå renoverar?",
     "Kommunens råd för småhus från 1940–60-talet är att en tegelfasad inte ska putsas. Fasaden underhålls i stället i sitt ursprungliga utförande."),
    ("Var hittar vi ritningar på husets stomme?",
     "Ibland i kommunens bygglovsarkiv. Saknas de tar en konstruktör fram underlaget."),
    ("Får vi byta fönstren i vår folkhemsvilla?",
     "Kommunen ser fönster och dörrar som en bärande del av husets karaktär. Utgå från originalets utformning och färgsättning, eller renovera de befintliga."),
    ("Måste vi anmäla nytt badrum och kök till kommunen?",
     "Ska anordningar för vatten och avlopp installeras eller ändras görs en anmälan om VA-arbete till kommunen."),
  ],
  "sources": [_HAN_KAR, _HAN_BAR, _HAN_VA, _SKV, _SKV2],
  "cta": ("Ska folkhemsvillan i Haninge totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom huset och kommunens råd innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa i gult och vitt med tegeltak och låg häck mot gatan",
     "1950s Swedish one-storey villa with yellow brick and coarse white rendered facade, saddle roof with red clay tiles, original wooden windows, small garden with low hedge to the street, Haninge suburb, summer" + _IMG_END),
    ("Vägg mellan kök och vardagsrum som öppnats under renovering",
     "still life inside a 1950s house under renovation: interior wall between kitchen and living room partly removed with temporary props and a new beam, protective covering on the floor, daylight" + _IMG_END),
    ("Ljust renoverat kök med träluckor och spröjsade fönster",
     "bright newly renovated kitchen in a 1950s Swedish villa: light wooden cabinets, white tiles, restored original wooden window with view to the garden, linoleum floor, daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ JÄRFÄLLA
"totalrenovering-jarfalla.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Järfälla", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Järfälla – flytta badet och mät radon",
  "description": "Totalrenovering i Järfälla: kök och badrum som flyttas, stammar i nya lägen, rör genom grunden och varför radonhalten ska mätas igen efter renoveringen.",
  "h1": "Totalrenovering i Järfälla",
  "lead": "I en totalrenovering vill många flytta kök och badrum, och då dras nya rör genom huset och ibland genom grunden. Geal Entreprenad AB totalrenoverar villor och radhus i Järfälla och håller ordning på både anmälan och radonfrågan.",
  "card": "Flytta badet och mät radon.",
  "sections": [
    {"id": "husen-jarfalla", "anchor": "Husen i Järfälla",
     "h2": "Småhus med historia",
     "paras": [
       "Järfällas kulturmiljöplan bygger på en inventering som Stockholms läns museum gjorde på kommunens uppdrag. Boken Järfälla kulturhistoriska miljöer kom ut 1991 och redovisar 58 miljöer och objekt, från Säby gård från 1650-talet till Dressyrvägen med småhus från 1960-talet.",
       "Planen påpekar att det för en lekman inte är lika självklart att ett 1960-talsområde är en utvald miljö som en herrgård. Men båda berättar om Järfällas historia, och planen ska ge stöd när varsamhetsreglerna tillämpas vid bygglov.",
     ],
     "aside": {"title": "Kulturmiljöplanen", "items": [
       "58 utvalda miljöer och objekt", "Säby gård från 1650-talet", "Dressyrvägen med 1960-talshus"]}},
    {"id": "stammar-jarfalla", "h2": "Stammar i nya lägen kräver anmälan",
     "paras": [
       "Järfälla kommun ger exempel på åtgärder där du behöver skicka in en anmälan och invänta startbesked: att installera stammar i nya lägen, och att installera eller göra en större ändring av en anläggning för vattenförsörjning eller avlopp i en byggnad eller på en tomt.",
       "Till anmälan hör en situationsplan där det framgår i vilken byggnad ändringen sker, en planritning om ändringarna görs inne i huset och ett förslag till kontrollplan. Flyttas badrummet till andra sidan huset är det alltså inte bara en inredningsfråga. Fall, ventilation och var stammen kan anslutas avgör också var det nya badrummet kan ligga, och vi ritar in det innan anmälan skickas.",
     ],
     "aside": {"title": "Handlingar vid anmälan", "items": [
       "Situationsplan", "Planritning", "Förslag till kontrollplan"]}},
    {"id": "grunden-jarfalla", "anchor": "Rör genom grunden",
     "h2": "Rör genom grunden och radonet",
     "paras": [
       "Kommunen skriver att radon i bostäder kan komma från marken, från den egna brunnens vatten eller från byggnadsmaterial, så kallad blå lättbetong. Järfälla har huvudsakligen normal- och lågriskmark, men små lokala variationer gör det olämpligt att generalisera riskbedömningen områdesvis.",
       "Kommunen rekommenderar en ny radonmätning om du har gjort förändringar i husgrunden, till exempel rörgenomdragningar, eller förändrat husets ventilation. Båda händer ofta i en totalrenovering. Vi tätar genomföringarna noga, och efter renoveringen bör du mäta igen under nästa eldningssäsong.",
     ],
     "aside": None},
    {"id": "matningen-jarfalla", "h2": "Så mäter du radon",
     "paras": [
       "Mätningen ska enligt kommunen göras under flera månader inom perioden 1 oktober–30 april. En korttidsmätning ger bara indikativa värden och har stor felmarginal. Referensvärdet för radon i inomhusluften i bostäder är 200 becquerel per kubikmeter som årsmedelvärde.",
       "Kommunen rekommenderar också en ny mätning om det har gått mer än tio år sedan den senaste. Blir värdet för högt är det ofta förhållandevis enkelt och kostnadseffektivt att åtgärda, enligt kommunen.",
     ],
     "aside": {"title": "Radonmätning i Järfälla", "items": [
       "Mät 1 oktober–30 april", "Flera månader, inte korttid", "Referensvärde 200 Bq/m³", "Mät igen efter ändrad grund eller ventilation"]}},
    {"id": "barande-jarfalla", "h2": "Bärande väggar",
     "paras": [
       "Ska kök och vardagsrum öppnas mot varandra krävs anmälan om väggen är bärande. Kommunen påpekar att ritningar kan vara ofullständiga och att det inte är säkert att de som byggde följde dem, och hänvisar till en konstruktör vid osäkerhet.",
       "Konstruktionsritningen ska upprättas av en sakkunnig konstruktör, och den lämnas in tillsammans med planritning och förslag till kontrollplan. Om köket i sig kan du läsa under " + _L.format("koksrenovering-jarfalla.html", "köksrenovering i Järfälla") + ", och om badrummet under " + _L.format("badrumsrenovering-jarfalla.html", "badrumsrenovering i Järfälla") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Järfälla till",
  "steps": [
    ("Platsbesök", "Vi går igenom planlösningen, stammarna och grunden."),
    ("Anmälan", "Stammar i nya lägen och bärande ändringar anmäls med kontrollplan."),
    ("Skriftligt kostnadsförslag", "Varje del och varje moment står för sig."),
    ("Renovering", "Genomföringar i grunden tätas när rören är dragna."),
    ("Slutbesked", "Kontrollplanen fylls i och lämnas till kommunen."),
    ("Radonmätning", "Mät under eldningssäsongen efter renoveringen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Järfälla",
  "rot": [
    _ROT_SMAHUS + " Radonsanering kan ge avdrag, men inte själva mätningen.",
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Järfälla?",
  "price": [
    "Hur långt kök och badrum flyttas, om grunden måste öppnas, bärande ändringar, el och VVS och vilka ytskikt du väljer. Läs mer under " + _L.format("villarenovering.html", "villarenovering") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi göra en anmälan när badrummet flyttas i vårt hus i Järfälla?",
     "Ja, om stammar installeras i nya lägen. Då krävs anmälan och startbesked enligt kommunen."),
    ("Vem ritar konstruktionen när en bärande vägg tas bort?",
     "En sakkunnig konstruktör. Kommunen skriver att konstruktionsritningen ska upprättas av en sådan."),
    ("Varför ska vi mäta radon efter renoveringen?",
     "Kommunen rekommenderar en ny mätning efter förändringar i husgrunden, som rörgenomdragningar, eller ändrad ventilation."),
    ("När kan vi mäta?",
     "Under flera månader inom perioden 1 oktober–30 april. En korttidsmätning ger bara indikativa värden."),
    ("Kan vi flytta köket utan anmälan?",
     "Flyttas köket utan att stammar dras i nya lägen eller bärande konstruktion ändras krävs normalt ingen anmälan. Vi går igenom ritningen med dig innan."),
    ("Vad är blå lättbetong?",
     "Ett byggnadsmaterial som kan avge radon. Kommunen nämner det tillsammans med marken och brunnsvattnet som källor."),
  ],
  "sources": [_JAR_KMP, _JAR_VA, _JAR_RADON, _JAR_BAR, _SKV, _SKV2],
  "cta": ("Ska huset i Järfälla totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom planlösningen och grunden innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Radhus och villor från 1960-talet längs en lugn gata",
     "row of low one-storey 1960s Scandinavian detached villas with very low pitched roofs and wide eaves, facades of light yellow brick combined with dark brown horizontal wooden panel, large picture windows, open lawns without fences, young birch trees, quiet curving street, modernist Swedish suburb, no chimneys, summer" + _IMG_END),
    ("Nya avloppsrör genom en öppnad betongplatta",
     "still life inside a house under renovation: opened concrete floor slab with new grey plastic waste pipes laid in a trench towards a new bathroom location, gravel and insulation visible, work lamp, daylight" + _IMG_END),
    ("Radondosa på en hylla i ett vardagsrum",
     "small round radon measurement detector placed on a white bookshelf in a calm Swedish living room, sofa and window in soft focus behind, winter daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ NORRTÄLJE
"totalrenovering-norrtalje.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Norrtälje", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Norrtälje – egen brunn och eget avlopp",
  "description": "Totalrenovering i Norrtälje: hus med egen brunn och eget avlopp, när WC eller fler byggnader kräver tillstånd eller anmälan och vattenprov efteråt.",
  "h1": "Totalrenovering i Norrtälje",
  "lead": "Många hus i Norrtälje har egen brunn och eget avlopp, och en totalrenovering med nytt badrum, ny toalett eller fler gäster påverkar båda. Geal Entreprenad AB totalrenoverar hus i Norrtälje och tar med vatten och avlopp i planeringen från början.",
  "card": "Egen brunn och eget avlopp.",
  "sections": [
    {"id": "landsbygden-norrtalje", "anchor": "Landsbygden",
     "h2": "En av Sveriges största landsbygdskommuner",
     "paras": [
       "Norrtälje kommun beskriver sig som en av Sveriges största landsbygdskommuner. Omkring 32 000 personer bor på kommunens landsbygd, och därtill finns drygt 26 000 fritidshus, där ungefär en fjärdedel av brukarna vistas större delen av året i kommunen.",
       "Sedan 1982 har landsbygdsbefolkningen ökat med omkring 60 procent. Det betyder att många hus som byggdes för sommarbruk eller ett enklare liv nu renoveras för att fungera året runt, och utanför tätorterna sker det ofta med egen brunn och eget avlopp.",
     ],
     "aside": {"title": "Norrtälje enligt kommunen", "items": [
       "Omkring 32 000 bor på landsbygden", "Drygt 26 000 fritidshus", "Landsbygdsbefolkningen +60 % sedan 1982"]}},
    {"id": "tillstand-norrtalje", "h2": "När avloppet kräver tillstånd",
     "paras": [
       "Kommunen skriver att det krävs tillstånd för att installera ett avloppssystem för bad-, disk- och tvättvatten, att koppla en vattentoalett till ett befintligt avlopp som tidigare bara tagit emot BDT-vatten, och att flytta en befintlig avloppsanläggning. Åtgärden får inte påbörjas innan tillståndet finns.",
       "Ska ett utedass eller en torrtoalett ersättas av en vattentoalett i renoveringen är det just den situationen kommunen beskriver, och tillståndet behöver sökas innan badrummet byggs.",
     ],
     "aside": {"title": "Tillstånd krävs för", "items": [
       "Nytt avlopp för BDT-vatten", "Vattentoalett på avlopp som bara haft BDT-vatten", "Flytt av befintlig avloppsanläggning"]}},
    {"id": "anmalan-norrtalje", "anchor": "Anmälan",
     "h2": "När det räcker med anmälan",
     "paras": [
       "Anmälan räcker enligt kommunen när fler byggnader kopplas på en befintlig enskild avloppsanläggning, till exempel ett attefallshus, garage eller gäststuga, när en vattenspolande toalett byts mot en som använder mer spolvatten, och när reningsteknik eller funktion ändras. Anmälan ska göras sex veckor innan du avser att utföra åtgärden.",
       "Kommunen påpekar att reglerna för enskilda avlopp kan avvika från andra kommuners, och rekommenderar att du gör en ansökan om du är osäker. Ärendet kan då övergå till anmälan, och kräver det ingenting avslutas det utan avgift.",
     ],
     "aside": None},
    {"id": "brunnen-norrtalje", "h2": "Brunnen när huset används mer",
     "paras": [
       "Med egen brunn ansvarar du själv för att den ger tillräckligt med vatten och att vattnet håller godkänd kvalitet. Kommunen hänvisar till Livsmedelsverket, som rekommenderar att små dricksvattenanläggningar för privat bruk analyseras minst vart tredje år, och oftare om det finns små barn i hushållet eller om man misstänker en förändring.",
       "Norrtälje är en kustnära kommun som till största delen ligger under den så kallade marina gränsen, och kommunen påpekar att man vid brunnsborrning nära kusten bör ta hänsyn till risken att saltvatten tränger in. Ökar vattenförbrukningen efter renoveringen är det klokt att ta ett nytt vattenprov.",
     ],
     "aside": {"title": "Egen brunn", "items": [
       "Analysera vattnet minst vart tredje år", "Oftare med små barn i hushållet", "Saltvatten kan tränga in nära kusten", "Registrera brunnen hos SGU"]}},
    {"id": "samordna-norrtalje", "h2": "Samordna badrum och avlopp",
     "paras": [
       "Ett nytt badrum, en tvättmaskin och en diskmaskin ökar mängden avloppsvatten. Vi går igenom med dig vad avloppsanläggningen har tillstånd för och tar in rätt kompetens när den behöver ändras, innan badrummet byggs.",
       "Om badrummet i sig kan du läsa under " + _L.format("badrumsrenovering-norrtalje.html", "badrumsrenovering i Norrtälje") + ", och om köket under " + _L.format("koksrenovering-norrtalje.html", "köksrenovering i Norrtälje") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering i Norrtälje till",
  "steps": [
    ("Platsbesök", "Vi går igenom huset, brunnen och avloppsanläggningen."),
    ("Tillstånd eller anmälan", "Avloppsfrågan reds ut och söks i tid."),
    ("Skriftligt kostnadsförslag", "Varje del och varje moment står för sig."),
    ("Renovering", "Badrum och kök byggs när avloppet är klart."),
    ("Vattenprov", "Ett nytt prov tas när huset används som planerat."),
    ("Genomgång", "Vi lämnar dokumentation över installationerna."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Norrtälje",
  "rot": [
    _ROT_SMAHUS + " Avdraget gäller både permanentbostad och fritidshus som du äger och själv använder.",
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Norrtälje?",
  "price": [
    "Husets skick, om avloppet behöver byggas om, avståndet till brunn och anläggning, el och VVS och vilka ytskikt du väljer. Läs mer under " + _L.format("villarenovering.html", "villarenovering") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vi vill byta torrtoaletten mot en vattentoalett i vårt hus i Norrtälje – vad krävs?",
     "Ska toaletten kopplas till ett avlopp som tidigare bara tagit emot BDT-vatten krävs tillstånd från kommunen innan arbetet börjar."),
    ("Kan vi koppla gäststugan till husets avlopp?",
     "Det kräver en anmälan sex veckor innan arbetet, enligt kommunen."),
    ("Hur ofta ska brunnsvattnet testas?",
     "Livsmedelsverket rekommenderar minst vart tredje år, och oftare med små barn i hushållet eller vid misstänkt förändring."),
    ("Vår brunn ligger nära havet – vad ska vi tänka på?",
     "Kommunen påpekar att saltvatten kan tränga in i brunnar nära kusten. Ett vattenprov visar om vattnet påverkats."),
    ("Vi är osäkra på om det krävs tillstånd eller anmälan – vad gör vi?",
     "Kommunen rekommenderar att du gör en ansökan. Ärendet kan då övergå till anmälan, eller avslutas utan avgift om inget krävs."),
  ],
  "sources": [_NOR_FAKTA, _NOR_AVL, _NOR_VAT, _SKV, _SKV2],
  "cta": ("Ska huset i Norrtälje totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom huset, brunnen och avloppet innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Rött trähus på landsbygden med åkrar runt omkring",
     "red wooden Swedish country house with white corners and a black roof surrounded by fields and a stone wall, birch trees, gravel driveway, Roslagen countryside near Norrtälje, summer" + _IMG_END),
    ("Brunn med stenring på en gräsmatta vid ett rött trähus",
     "concrete well cover with a metal lid on a lawn next to an old red wooden house, garden hose coiled beside, apple tree, summer daylight" + _IMG_END),
    ("Nyrenoverat badrum i ett äldre trähus på landet",
     "newly renovated bathroom in an old Swedish country house: white wall tiles, grey floor tiles, wall-hung toilet, small window with wooden frame, wooden ceiling boards, soft daylight" + _IMG_END),
  ],
},

# ------------------------------------------------------------------ VALLENTUNA
"totalrenovering-vallentuna.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Vallentuna", "svc_label": "Totalrenovering",
  "title": "Totalrenovering i Vallentuna – radon när huset byggs om",
  "description": "Totalrenovering i Vallentuna: när radonhalten bör mätas vid ombyggnad, ny ventilation eller uppvärmning, hur mätningen går till och radonbidraget.",
  "h1": "Totalrenovering i Vallentuna",
  "lead": "När ett hus totalrenoveras ändras ofta ventilationen, uppvärmningen och ibland grunden, och då kan radonhalten också ändras. Geal Entreprenad AB totalrenoverar villor i Vallentuna och tar med radonfrågan i planeringen.",
  "card": "Radon när huset byggs om.",
  "sections": [
    {"id": "smahusen-vallentuna", "anchor": "Småhusen",
     "h2": "En kommun av småhus",
     "paras": [
       "Enligt Vallentunas översiktsplan fanns det 2017 drygt 13 000 bostäder i kommunen, och omkring 65 procent av dem var småhus. Sedan millennieskiftet har knappt 3 000 nya bostäder tillkommit, de flesta i tätorterna.",
       "Många av villorna har därför några decennier på nacken, och för en del ägare är det dags för en större renovering. När huset ändå byggs om finns det skäl att också se över luften inomhus.",
     ],
     "aside": {"title": "Vallentuna enligt översiktsplanen", "items": [
       "Drygt 13 000 bostäder 2017", "Omkring 65 procent småhus", "Knappt 3 000 nya bostäder sedan 2000"]}},
    {"id": "nar-vallentuna", "h2": "När radonhalten bör mätas",
     "paras": [
       "Vallentuna kommun skriver att det inte finns något generellt krav på att du som privatperson ska känna till radonhalten i ditt hus, men att det kan vara bra att veta för din hälsa och vid en försäljning. Kommunen räknar upp tillfällen när mätning bör göras.",
       "Två av dem gäller en totalrenovering direkt: vid om- och tillbyggnad av småhus, och vid förändring av ventilation eller uppvärmningssystem. Kommunen nämner också husköp, hus i områden med höga halter av markradon eller byggda med blåbetong, och att det gått tio år sedan senaste mätningen.",
     ],
     "aside": {"title": "Mät radon vid", "items": [
       "Husköp", "Om- och tillbyggnad av småhus", "Ändrad ventilation eller uppvärmning", "Blåbetong eller markradon", "Tio år sedan senaste mätningen"]}},
    {"id": "matning-vallentuna", "anchor": "Mätningen",
     "h2": "Så går mätningen till",
     "paras": [
       "En radonmätning görs under perioden 1 oktober–30 april, och mättiden är minst två månader. Det vanligaste är dosor med spårfilm som placeras i huset, oftast i sovrum och ett rum till, till exempel vardagsrummet.",
       "Du kan göra mätningen själv eller ta hjälp av en radonkonsult. Kommunen påpekar att radonmätningen vid ansökan om bygglov måste göras av något av de företag som kommunen godkänt, och att mätningen då kan behövas för att du ska få slutbesked.",
     ],
     "aside": None},
    {"id": "ordningen-vallentuna", "h2": "Mät före, renovera, mät efter",
     "paras": [
       "Den enklaste ordningen är att mäta under vintern innan renoveringen och sedan igen vintern efter. Vet du redan före att halten är hög kan åtgärderna byggas in i renoveringen, till exempel tätning av genomföringar i grunden eller en ny ventilationslösning.",
       "Radon varken syns, luktar eller smakar, och kommunen skriver att det enda sättet att upptäcka det är att mäta. Om ventilation och badrum i övrigt kan du läsa under " + _L.format("badrumsrenovering-vallentuna.html", "badrumsrenovering i Vallentuna") + ".",
     ],
     "aside": None},
    {"id": "ventilation-vallentuna", "anchor": "Ventilationen",
     "h2": "Ventilationen i ett tätare hus",
     "paras": [
       "En totalrenovering gör ofta huset tätare: nya fönster, ny isolering och tätade genomföringar. Det sparar energi, men det ändrar också hur luften rör sig i huset. Därför ser vi över ventilationen i samma projekt, så att det tätare huset får den luftväxling det behöver.",
       "Kommunen räknar just ändrad ventilation som ett tillfälle då radonhalten bör mätas. Ett nytt ventilationssystem och en mätning vintern efter hör därför ihop.",
     ],
     "aside": None},
    {"id": "bidrag-vallentuna", "h2": "Radonbidrag – sök före sanering",
     "paras": [
       "Boverket kan ge radonbidrag till småhusägare vars hus har för höga radonhalter och där radonsanering behövs. Kommunen skriver att ansökan görs hos länsstyrelsen i det län där huset ligger, och att den måste göras innan du börjar saneringen.",
       "Det är en viktig detalj i en totalrenovering. Har saneringsåtgärderna redan byggts in innan ansökan skickats kan bidraget gå förlorat. Kommunen visar också inskickade mätningar på kommunkartan, vilket ger en bild av halterna i närområdet.",
     ],
     "aside": {"title": "Radonbidrag", "items": [
       "Ges av Boverket till småhusägare", "Söks hos länsstyrelsen", "Måste sökas innan saneringen börjar"]}},
  ],
  "steps_h2": "Så går en totalrenovering i Vallentuna till",
  "steps": [
    ("Radonmätning", "Mät under vintern före renoveringen om det går."),
    ("Platsbesök", "Vi går igenom huset, ventilationen och grunden."),
    ("Skriftligt kostnadsförslag", "Varje del och varje moment står för sig."),
    ("Bidrag och anmälan", "Radonbidrag söks innan sanering, anmälan där det krävs."),
    ("Renovering", "Ventilation och tätning byggs in i arbetet."),
    ("Ny mätning", "Mät igen vintern efter renoveringen."),
  ],
  "rot_h2": "ROT-avdrag för totalrenoveringen i Vallentuna",
  "rot": [
    _ROT_SMAHUS + " Radonsanering kan ge avdrag, men inte själva mätningen.",
    _ROT_SUM + " Geal drar av beloppet direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset för totalrenoveringen i Vallentuna?",
  "price": [
    "Husets storlek och skick, ventilationen och grunden, el och VVS och vilka ytskikt du väljer. Läs mer under " + _L.format("villarenovering.html", "villarenovering") + ". Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste vi mäta radon när vi renoverar vårt hus i Vallentuna?",
     "Det finns inget generellt krav för privatpersoner, men kommunen rekommenderar mätning vid om- och tillbyggnad och vid ändrad ventilation eller uppvärmning."),
    ("Hur länge ska vi mäta?",
     "Minst två månader under perioden 1 oktober–30 april."),
    ("Kan vi få bidrag för radonsanering?",
     "Boverket kan ge radonbidrag till småhusägare. Ansökan görs hos länsstyrelsen innan saneringen börjar."),
    ("Var kan vi se om grannarna har höga halter?",
     "Kommunen visar inskickade mätningar på kommunkartan. Det kan finnas mätningar som kommunen inte känner till."),
    ("Behöver mätningen skickas till kommunen?",
     "Normalt inte för småhus, men om du har sökt bygglov kan den behövas för slutbeskedet."),
  ],
  "sources": [_VALL_OP, _VALL_RADON, _SKV, _SKV2],
  "cta": ("Ska huset i Vallentuna totalrenoveras?", "Boka ett gratis platsbesök, så går vi igenom huset och ventilationen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Villa från 1970-talet i ett lugnt villaområde",
     "1970s Swedish two-storey villa with brown wooden panel facade and dark tiled roof, lawn and hedges, quiet residential street in a suburb north of Stockholm, early autumn" + _IMG_END),
    ("Ny ventilationskanal på en vind under renovering",
     "still life in an attic during renovation: new insulated ventilation ducts connected to a compact heat recovery unit, mineral wool insulation between joists, work lamp, daylight from a small window" + _IMG_END),
    ("Radondosa i ett sovrum med vinterljus",
     "small plain white round plastic radon measurement disc without any display or markings, placed on a white bedside table in a calm Swedish bedroom, bed with light linen, window with winter light, soft focus background" + _IMG_END),
  ],
},
}
