# -*- coding: utf-8 -*-
"""Köksrenovering – ortsidor v26: Kungsholmen, Vasastan, Östermalm, Österåker, Skärholmen, Farsta (2026-10-26).
Hubb: koksrenovering.html (TJ_HUB["koksrenovering"]). Tre bilder per sida.

Fakta endast från källorna i respektive 'sources', öppnade med curl (UA Mozilla) 2026-10-26, alla svarade 200:
  bygglov.stockholm – Flytta kök eller badrum: inget bygglov; anmälan och startbesked vid ändring av bärande
    konstruktion eller brandskydd, installation/väsentlig ändring av ventilation (aggregat, fläkt, kanaler,
    värmeväxlare), ny VA-stam i nytt schakt; badrumskanal som kombinerad imkanal – kontrollera måtten; rådgör med
    sotaren; hyresrätt: normalt inte; bostadsrätt: tillstånd från föreningen; kulturhistoriska värden.
  bygglov.stockholm – Stadsmuseets kulturhistoriska klassificering (blå/grön/gul/grå, riksintresse).
  Riksdagen – Bostadsrättslag (1991:614) 7 kap. 7 § (lydelse 2022:1026): styrelsens tillstånd för ingrepp i bärande
    konstruktion, ledningar för avlopp, värme, gas eller vatten, ventilation, eldstad/rökkanal/brandskydd, annan
    väsentlig förändring; lägenhet med särskilda kulturhistoriska värden – tillstånd krävs när värdet påverkas;
    styrelsen får vägra bara vid påtaglig skada eller olägenhet; hyresnämnden kan pröva.
  Områdesfakta 2025 (pdf, textlager): Kungsholmens stadsdelsområde 44 554 bostäder, 30 369 bostadsrätter i
    flerbostadshus, 10 476 övriga hyresrätter, 1 510 allmännytta; Gustav Vasa 1 107 lägenheter utan kök av 8 532,
    Västra Matteus 782 av 11 913, Östra Matteus 692 av 7 636; Hedvig Eleonora 7 290 lägenheter varav 939 utan kök och
    1 119 med fem rum eller fler, 5 151 bostadsrätter; Skärholmens stadsdelsområde 3 479 allmännytta + 6 502 övriga
    hyresrätter + 3 315 bostadsrätter i flerbostadshus, 1 976 småhus med äganderätt; Farsta stadsdelsområde
    10 543 allmännytta + 4 614 övriga hyresrätter + 9 914 bostadsrätter i flerbostadshus, 639 bostadsrätter och 3 806
    äganderätter i småhus.
  Österåkers kommun – Anmälan (lista inkl. nya eller förändrade rördragningar i bjälklag, ventilation, bärande väggar;
    kontrollplan för alla anmälningar; Boverkets nya byggregler från 1 juli 2025, övergång till 1 juli 2026) och Vatten
    och avlopp (Roslagsvatten, områden från fritidshus till permanentboende, eget avlopp och egen brunn, 140 liter per
    person och dag, tio liter till mat och dryck, vattensmarta råd).
  Stockholmskällan – På upptäcktsfärd kring Skärholmen (inflyttning 1965, centrum 1968); Varsam utveckling (pdf):
    storskalig stadsdel, Bredäng 1962, Sätra, 1965, industrialiserad byggteknik.
  Stockholms stadsmuseum – Stockholms spår: Farsta (ABC-stad, centrum 1960, radhusområden i utkanterna).
  Skatteverket – Ger arbetet rätt till rotavdrag? (WebFetch): fast köksinredning och vitvaror i samband med omfattande
    renovering, byta köksluckor; bostadsrätt: arbete inom lägenheten som bostadsrättshavaren ansvarar för enligt
    stadgarna; inte reparation av diskmaskin (rut).
Strukna: gasspisar (ingen källa om installation lästes färdigt), priser, tider, märken.
Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"

_STH_KOK = ("Stockholms stad – Flytta kök eller badrum", "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/flytta-kok-eller-badrum/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
              "https://bygglov.stockholm/nar-behovs-bygglov/andra-inomhus/stadsmuseets-kulturhistoriska-klassificering/")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_ROT_BR = ("Skatteverket godkänner rotavdrag i en bostadsrätt för arbete inne i lägenheten som du själv ansvarar för "
           "enligt föreningens stadgar – till exempel att montera fast köksinredning och installera vitvaror i samband med "
           "en omfattande renovering, byta köksluckor eller riva innerväggar. Avdraget gäller arbetskostnaden, och Geal "
           "drar det direkt på fakturan.")
_ROT_HUS = ("I ett småhus ger köksrenoveringen rotavdrag på arbetskostnaden, till exempel för att montera fast "
            "inredning och installera vitvaror när köket byggs om. Material ger inget avdrag, och reparation av "
            "diskmaskin räknas enligt Skatteverket till rut. Geal drar avdraget direkt på fakturan.")

PAGES_TJ = {

# ------------------------------------------------------------------ KUNGSHOLMEN
"koksrenovering-kungsholmen.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Kungsholmen", "svc_label": "Köksrenovering",
  "title": "Köksrenovering på Kungsholmen – fläkt, kanal och styrelse",
  "description": "Köksrenovering på Kungsholmen: imkanal och köksfläkt i flerbostadshus, när anmälan krävs, styrelsens tillstånd i bostadsrätt och vad hyresgäster får göra.",
  "h1": "Köksrenovering på Kungsholmen",
  "lead": "På Kungsholmen bor de flesta i bostadsrätt i flerbostadshus, och då handlar ett nytt kök lika mycket om fläkten, kanalen och föreningen som om luckorna. Geal Entreprenad AB planerar köket med dig, tar fram underlaget till styrelsen och bygger det färdigt.",
  "card": "Fläkten, kanalen och föreningen.",
  "sections": [
    {"id": "boende-kungsholmen", "anchor": "Boendet",
     "h2": "Bostadsrätt i flerbostadshus – oftast",
     "paras": [
       "Stadens områdesfakta för 2025 räknar 44 554 bostäder i Kungsholmens stadsdelsområde. 30 369 av dem är bostadsrätter i flerbostadshus, 10 476 är övriga hyresrätter och 1 510 hör till allmännyttan. Bara några hundra är småhus. För de allra flesta som vill renovera köket är alltså bostadsrättsföreningen den första instansen.",
       "Bostadsrättslagen säger att du inte får göra vissa åtgärder i lägenheten utan styrelsens tillstånd: ingrepp i bärande konstruktion, installation eller ändring av ledningar för avlopp, värme, gas eller vatten, installation eller ändring av ventilation, ändring av eldstad eller rökkanal och annan väsentlig förändring. Ett kök där diskbänken flyttas eller fläkten byts mot en annan typ hamnar oftast på den listan.",
     ],
     "aside": {"title": "Kräver styrelsens tillstånd", "items": [
       "Ingrepp i bärande konstruktion", "Ledningar för avlopp, värme, gas, vatten", "Ventilation", "Annan väsentlig förändring"]}},
    {"id": "flakt-kungsholmen", "h2": "Köksfläkten och imkanalen",
     "paras": [
       "Stockholms stad påpekar att ett kök behöver tillräcklig frånluft och ska uppfylla kraven för imkanal. Om badrummets frånluftskanal ska användas som kombinerad kanal för både kök och badrum måste kanalens sammanlagda mått räcka. Staden rekommenderar att man rådgör tidigt med sotaren om förutsättningarna för en ny eller ändrad ventilations- eller imkanal.",
       "I ett flerbostadshus är ventilationen gemensam, och en kraftigare fläkt kan störa luftflödena i grannarnas lägenheter. Vi tar därför reda på vilket system huset har – självdrag, mekanisk frånluft eller från- och tilluft – innan vi föreslår fläkt. Ska ventilationen ändras väsentligt, till exempel med ett nytt aggregat eller nya kanaler, behövs en anmälan och ett startbesked.",
     ],
     "aside": {"title": "Fråga sotaren eller föreningen", "items": [
       "Vilket ventilationssystem huset har", "Kanalens mått", "Om kanalen delas med badrummet", "Vilken fläkt som passar"]}},
    {"id": "anmalan-kungsholmen", "h2": "När köket behöver anmälas",
     "paras": [
       "Staden skriver att det inte behövs bygglov för att flytta ett kök. Däremot behövs anmälan och startbesked om flytten innebär ändring av bärande konstruktion eller brandskydd, väsentlig ändring av ventilationen eller en ny VA-stam i ett nytt schakt. Oavsett om anmälan krävs ska arbetet uppfylla de tekniska egenskapskraven i plan- och bygglagen.",
       "Många kök på Kungsholmen öppnas mot vardagsrummet. Är väggen bärande blir det både en anmälan till staden och en fråga för styrelsen. Vi tar fram ritningar och konstruktionsunderlag och lämnar in dem innan väggen rörs. Hur badrummet i samma lägenhet hanteras beskriver vi under " + _L.format("badrumsrenovering-kungsholmen.html", "badrumsrenovering på Kungsholmen") + ".",
     ],
     "aside": None},
    {"id": "hyresratt-kungsholmen", "h2": "Bor du i hyresrätt?",
     "paras": [
       "Staden skriver att den som bor i hyresrätt normalt inte får flytta kök eller badrum. Ett nytt kök i en hyreslägenhet är fastighetsägarens beslut, och då är det hyresvärden som beställer arbetet. I en bostadsrätt kan styrelsen bara vägra tillstånd om åtgärden är till påtaglig skada eller olägenhet för föreningen, och den som är missnöjd med beslutet kan begära att hyresnämnden prövar saken.",
       "För att styrelsen ska kunna svara snabbt behöver den en tydlig beskrivning: vad som ska göras, var ledningar och fläkt hamnar och vem som utför arbetet. Vi skriver den beskrivningen och bifogar ritningar. Många föreningar vill också ha intyg och dokumentation från el- och VVS-arbetena när köket är klart, så att det finns underlag om något händer senare i huset. Vi samlar dem och lämnar över dem till dig och styrelsen. Läs mer om helheten under " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi ett kök på Kungsholmen",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter köket och tittar på kanal och ledningar."),
    ("Förslag", "Planlösning, fläkt och placering av diskbänk och vitvaror."),
    ("Föreningen", "Underlag till styrelsen för tillstånd enligt bostadsrättslagen."),
    ("Anmälan", "Anmälan till staden där bärande delar, ventilation eller ny stam berörs."),
    ("Rivning och bygge", "Rivning, el och VVS via behöriga installatörer, montering av köket."),
    ("Slutkontroll", "Genomgång av köket och dokumentation till föreningen."),
  ],
  "rot_h2": "ROT-avdrag för kök i bostadsrätt",
  "rot": [_ROT_BR],
  "price_h2": "Vad påverkar priset på ett kök på Kungsholmen?",
  "price": [
    "Om köket stannar på samma plats eller flyttas, om en vägg öppnas, fläkt och kanal, el och VVS, inredning och vitvaror samt hur material kommer upp i trapphuset. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi använda badrumskanalen till köksfläkten på Kungsholmen?",
     "Bara om kanalens sammanlagda mått räcker för både badrummets frånluft och köket. Staden råder dig att kontrollera måtten och prata med sotaren först."),
    ("Behövs bygglov för att flytta köket i en lägenhet på Kungsholmen?",
     "Nej. Men anmälan och startbesked krävs om bärande delar, brandskydd eller ventilation ändras väsentligt eller om en ny VA-stam dras i ett nytt schakt."),
    ("Kan styrelsen säga nej till vår köksrenovering på Kungsholmen?",
     "Bara om åtgärden är till påtaglig skada eller olägenhet för föreningen. Tillståndet kan förenas med villkor, och hyresnämnden kan pröva ett nej."),
    ("Får vi byta kök i en hyreslägenhet på Kungsholmen?",
     "Staden skriver att du som hyresgäst normalt inte får flytta kök eller badrum. Kontakta hyresvärden."),
    ("Hur många bostadsrätter finns det på Kungsholmen?",
     "Enligt stadens områdesfakta för 2025 är 30 369 av de 44 554 bostäderna i stadsdelsområdet bostadsrätter i flerbostadshus."),
  ],
  "sources": [_STH_KOK, _BRL, _of("Kungsholmens stadsdelsområde", "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade"), _SKV],
  "cta": ("Planerar du ett nytt kök på Kungsholmen?", "Boka ett gratis platsbesök, så tar vi fram förslaget och underlaget till föreningen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyrenoverat kök i en äldre stadslägenhet med vita luckor och fönster mot gården",
     "newly renovated kitchen in an older Stockholm city apartment, white painted cabinet doors, oak worktop, stainless steel extractor hood on the wall, tall window with deep sill facing a courtyard, wooden floor, soft daylight" + _SFX),
    ("Köksfläkt och ventilationskanal i taket under montering",
     "kitchen under renovation in an apartment, new extractor hood mounted on the wall with a round metal duct leading up into the ceiling, empty walls ready for cabinets, protective paper on the floor, no workers, daylight" + _SFX),
    ("Öppning mellan kök och vardagsrum i en äldre lägenhet",
     "older city apartment with a wide new opening between kitchen and living room, plastered edges, herringbone parquet floor, kitchen island in the background, soft afternoon light" + _SFX),
  ],
},

# ------------------------------------------------------------------ VASASTAN
"koksrenovering-vasastan.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Vasastan", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Vasastan – från kokvrå till kök",
  "description": "Köksrenovering i Vasastan: lägenheter utan fullt kök, att göra en kokvrå till kök, frånluft och imkanal, styrelsens tillstånd och anmälan till staden.",
  "h1": "Köksrenovering i Vasastan",
  "lead": "I Vasastan finns många små lägenheter som saknar ett fullständigt kök. Att göra en kokvrå till ett riktigt kök är en annan uppgift än att byta luckor. Geal Entreprenad AB går igenom ventilation, ledningar och föreningens regler och bygger köket färdigt.",
  "card": "Kokvrån som blir kök.",
  "sections": [
    {"id": "utan-kok-vasastan", "anchor": "Utan kök",
     "h2": "Tusentals lägenheter utan fullt kök",
     "paras": [
       "Stadens områdesfakta för 2025 redovisar lägenheter efter storlek, och en egen kolumn gäller lägenheter utan kök. I statistikområdet Gustav Vasa är det 1 107 av 8 532 lägenheter i flerbostadshus, i Västra Matteus 782 av 11 913 och i Östra Matteus 692 av 7 636. Det handlar ofta om ettor med kokvrå eller kokskåp.",
       "Att göra en sådan lägenhet till en etta med kök är en av de vanligaste förändringarna i små lägenheter. Det kräver mer än nya skåp: köket behöver tillräcklig frånluft, avloppet ska klara diskmaskin och diskbänk, och elen ska räcka till spis och ugn. El och VVS utförs av behöriga installatörer.",
     ],
     "aside": {"title": "Lägenheter utan kök 2025", "items": [
       "Gustav Vasa 1 107", "Västra Matteus 782", "Östra Matteus 692"]}},
    {"id": "franluft-vasastan", "h2": "Frånluften avgör",
     "paras": [
       "Stockholms stad skriver att ett kök ska ha tillräcklig frånluft och uppfylla kraven för imkanal. Ska badrummets kanal användas för både badrum och kök måste kanalens sammanlagda mått räcka, och staden rekommenderar att du rådgör med sotaren tidigt. I en kokvrå finns ibland bara en enkel ventil, och då är det frågan om kanalen kan ta emot en köksfläkt som styr hur köket kan byggas.",
       "Kräver köket en ny kanal eller en väsentlig ändring av ventilationen – till exempel en fläkt som påverkar luftflödena – behövs en anmälan till staden och ett startbesked. Vi tar reda på hur huset ventileras innan vi ritar köket, så att det inte blir en överraskning när skåpen redan är beställda.",
     ],
     "aside": None},
    {"id": "foreningen-vasastan", "h2": "En väsentlig förändring för föreningen",
     "paras": [
       "De flesta lägenheter i Vasastan är bostadsrätter – i Västra Matteus 8 985 av bostäderna i flerbostadshus enligt områdesfakta. Bostadsrättslagen kräver styrelsens tillstånd för installation eller ändring av ledningar för vatten och avlopp, för ändrad ventilation och för annan väsentlig förändring av lägenheten. Att bygga ett kök där det inte har funnits något är just en sådan förändring.",
       "Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet för föreningen, men den får förena tillståndet med villkor – till exempel om hur rör dras eller vem som utför arbetet. Vi skriver en beskrivning med ritningar som styrelsen kan ta ställning till.",
     ],
     "aside": {"title": "Underlag till styrelsen", "items": [
       "Ritning före och efter", "Var vatten och avlopp ansluts", "Fläkt och kanal", "Vem som gör arbetet"]}},
    {"id": "flytta-vasastan", "h2": "Flytta köket eller bygga nytt på samma plats",
     "paras": [
       "Staden kräver inte bygglov för att flytta ett kök, men en anmälan om flytten innebär en ny VA-stam i ett nytt schakt, ändring av bärande konstruktion eller brandskydd, eller väsentligt ändrad ventilation. Det är därför oftast enklast att bygga köket där kokvrån redan finns, nära stammarna och kanalen.",
       "I en liten lägenhet handlar resten om att få plats: smala skåp, en spis med två eller fyra plattor, diskmaskin i halv bredd och förvaring ända upp till taket. Vi ritar köket efter de mått lägenheten har, och vi tar hänsyn till fönster, dörrar och element så att skåpen inte tar ljuset eller blockerar en dörr. I äldre hus är väggarna sällan raka, och då måttbeställs ofta bänkskiva och passbitar efter att väggarna har kontrollerats. Mer om kök i allmänhet finns under " + _L.format("koksrenovering.html", "köksrenovering") + ", och om badrummet i samma lägenhet under " + _L.format("badrumsrenovering-vasastan.html", "badrumsrenovering i Vasastan") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så bygger vi kök i Vasastan",
  "steps": [
    ("Platsbesök", "Gratis besök där vi mäter kokvrån och tittar på kanal och stammar."),
    ("Förslag", "Kökslösning efter lägenhetens mått, med fläkt och vitvaror."),
    ("Föreningen", "Beskrivning och ritningar för styrelsens tillstånd."),
    ("Anmälan", "Anmälan till staden där ventilation eller ny stam kräver det."),
    ("Bygget", "El och VVS via behöriga installatörer, montering och anslutning."),
    ("Överlämning", "Genomgång av köket och dokumentation till föreningen."),
  ],
  "rot_h2": "ROT-avdrag när kokvrån blir kök",
  "rot": [_ROT_BR],
  "price_h2": "Vad påverkar priset på ett kök i Vasastan?",
  "price": [
    "Om ventilationen räcker eller behöver ändras, hur långt det är till stammarna, el till spis och ugn, inredning och vitvaror samt hur material bärs upp i ett äldre trapphus. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan vi göra kokvrån till ett riktigt kök i vår etta i Vasastan?",
     "Ofta ja, men det kräver styrelsens tillstånd och en ventilation som klarar en köksfläkt. Vi kontrollerar kanalen innan köket ritas."),
    ("Behövs anmälan för att bygga kök i en kokvrå i Vasastan?",
     "Om ventilationen ändras väsentligt eller en ny VA-stam dras i ett nytt schakt krävs anmälan och startbesked enligt staden."),
    ("Hur många lägenheter i Vasastan saknar kök?",
     "Enligt områdesfakta 2025 är det 1 107 i Gustav Vasa, 782 i Västra Matteus och 692 i Östra Matteus."),
    ("Får styrelsen sätta villkor för vårt nya kök i Vasastan?",
     "Ja. Bostadsrättslagen låter styrelsen förena tillståndet med villkor, och den får bara vägra om åtgärden är till påtaglig skada eller olägenhet."),
    ("Var ska köket helst ligga när en etta i Vasastan får kök?",
     "Oftast där kokvrån redan finns, nära stammarna och kanalen. Att flytta köket kan kräva en ny stam i ett nytt schakt och då en anmälan."),
  ],
  "sources": [_of("Gustav Vasa", "inre-staden/norra-innerstaden/gustav-vasa"),
              _of("Västra Matteus", "inre-staden/norra-innerstaden/vastra-matteus"),
              _of("Östra Matteus", "inre-staden/norra-innerstaden/ostra-matteus"), _STH_KOK, _BRL, _SKV],
  "cta": ("Vill du få ett riktigt kök i Vasastan?", "Boka ett gratis platsbesök, så mäter vi kokvrån och kanalen innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Litet nytt kök längs en vägg i en etta med högt i tak",
     "small new kitchen along one wall in a studio apartment with high ceiling and stucco, slim light grey cabinets up to the ceiling, compact induction hob, small extractor hood, wooden floor, tall window with daylight" + _SFX),
    ("Gammal kokvrå med enkel spis och skåp före renovering",
     "old cramped kitchenette in a city studio apartment before renovation, small old electric stove with two plates, worn cabinets and a small sink in a niche, vintage tiles, daylight" + _SFX),
    ("Smal diskmaskin och skåp i ett kompakt kök",
     "compact apartment kitchen detail with a slimline integrated dishwasher, narrow drawers and a small oak worktop with a sink, white tiled backsplash, soft daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ ÖSTERMALM
"koksrenovering-ostermalm.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Östermalm", "svc_label": "Köksrenovering",
  "title": "Köksrenovering på Östermalm – stora våningar, kulturvärden",
  "description": "Köksrenovering på Östermalm: stora lägenheter, köket som flyttas, ny stam i nytt schakt, kulturhistoriska värden i lägenheten och föreningens tillstånd.",
  "h1": "Köksrenovering på Östermalm",
  "lead": "På Östermalm finns många stora lägenheter där köket ligger långt från matsalen eller där en ägare vill flytta det. Det väcker frågor om stammar, kanaler och lägenhetens kulturvärden. Geal Entreprenad AB utreder förutsättningarna och bygger köket med en kontakt för hela projektet.",
  "card": "Stora lägenheter och kulturvärden.",
  "sections": [
    {"id": "stora-ostermalm", "anchor": "Stora lägenheter",
     "h2": "Stora lägenheter, många rum",
     "paras": [
       "Stadens områdesfakta för 2025 visar att statistikområdet Hedvig Eleonora har 7 290 lägenheter i flerbostadshus. 1 119 av dem har fem rum eller fler, och 939 saknar fullt kök. 5 151 av bostäderna är bostadsrätter. Det är alltså både stora våningar och små lägenheter i samma kvarter.",
       "I de stora lägenheterna vill många flytta köket till ett ljusare rum eller öppna det mot en matsal. Staden skriver att det inte behövs bygglov för att flytta ett kök. Men om flytten kräver en ny VA-stam i ett nytt schakt, om ventilationen ändras väsentligt eller om bärande konstruktion eller brandskydd påverkas, krävs anmälan och startbesked.",
     ],
     "aside": {"title": "Hedvig Eleonora 2025", "items": [
       "7 290 lägenheter", "1 119 med fem rum eller fler", "939 utan fullt kök", "5 151 bostadsrätter"]}},
    {"id": "kulturvarden-ostermalm", "h2": "När lägenheten har kulturvärden",
     "paras": [
       "Bostadsrättslagen har en särskild regel som är viktig i äldre hus: för en lägenhet med särskilda historiska, kulturhistoriska, miljömässiga eller konstnärliga värden krävs styrelsens tillstånd för varje åtgärd som påverkar ett sådant värde. Det kan gälla allt från en äldre köksinredning till stuckatur, dörrar och kakelugnar i rummet dit köket ska flyttas.",
       "Staden påminner också om att du ska ta hänsyn till byggnadens kulturhistoriska värden vid alla ändringar. Stadsmuseets klassificeringskarta visar hur huset är klassat. Vi går igenom vad som finns kvar av ursprunglig inredning innan vi föreslår var köket ska ligga, och vi föreslår hellre en lösning som låter detaljerna vara kvar. Finns ett äldre skafferi eller originalluckor kan de ofta renoveras och byggas in i det nya köket i stället för att rivas.",
     ],
     "aside": {"title": "Ta reda på först", "items": [
       "Husets klass i Stadsmuseets karta", "Vad som är original i köket", "Stuckatur och dörrar i rummet", "Föreningens regler"]}},
    {"id": "stammar-ostermalm", "h2": "Stammar, schakt och kanaler",
     "paras": [
       "Ett kök som flyttas långt från stammarna behöver ofta antingen långa ledningar med fall i golvet eller en ny stam i ett nytt schakt. Det senare kräver anmälan till staden och styrelsens tillstånd, eftersom ledningar för vatten och avlopp ändras. Bostadsrättslagen kräver tillstånd även för ändring av ledningar för värme och gas och för ändrad ventilation.",
       "Köksfläkten är den andra stora frågan. Staden skriver att köket ska ha tillräcklig frånluft och uppfylla kraven för imkanal, och att sotaren bör tillfrågas tidigt om en ny eller ändrad kanal. I hus med kakelugnar och gamla rökkanaler är det extra viktigt att veta vilka kanaler som används till vad.",
     ],
     "aside": None},
    {"id": "foreningen-ostermalm", "h2": "Styrelsen och arbetet i huset",
     "paras": [
       "Styrelsen får bara vägra tillstånd om åtgärden är till påtaglig skada eller olägenhet för föreningen, men den kan förena tillståndet med villkor. I större föreningar finns ofta regler för arbetstider, skydd i trapphus och hiss och hur byggavfall ska tas om hand. Vi följer dem och tar fram den dokumentation styrelsen vill ha efter arbetet. I en stor lägenhet kan det också vara klokt att göra köket i etapper, så att en del av bostaden går att använda medan arbetet pågår, och att planera hur material ska bäras in utan att skada trapphusets äldre ytor.",
       "El och VVS utförs av behöriga installatörer. Är det badrummet som också ska göras om beskriver vi det under " + _L.format("badrumsrenovering-ostermalm.html", "badrumsrenovering på Östermalm") + ", och mer om kök i allmänhet finns under " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi ett kök på Östermalm",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på stammar, kanaler och originaldetaljer."),
    ("Utredning", "Klassning, ventilation och ledningsdragning utreds innan köket placeras."),
    ("Föreningen", "Underlag till styrelsen för tillstånd, med ritningar."),
    ("Anmälan", "Anmälan till staden vid ny stam, ändrad ventilation eller bärande delar."),
    ("Bygget", "El och VVS via behöriga installatörer, snickerier och montering."),
    ("Dokumentation", "Genomgång och dokumentation till dig och föreningen."),
  ],
  "rot_h2": "ROT-avdrag i en bostadsrätt på Östermalm",
  "rot": [_ROT_BR],
  "price_h2": "Vad påverkar priset på ett kök på Östermalm?",
  "price": [
    "Om köket flyttas eller stannar, ny stam och schakt, ventilation, hänsyn till originaldetaljer, inredning och vitvaror samt föreningens regler för arbetet. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs styrelsens tillstånd för att ta bort ett gammalt originalkök på Östermalm?",
     "Om lägenheten har särskilda kulturhistoriska värden och åtgärden påverkar dem krävs styrelsens tillstånd enligt bostadsrättslagen."),
    ("Kräver en ny stam för ett flyttat kök anmälan på Östermalm?",
     "Ja. Staden skriver att en ny VA-stam i ett nytt schakt kräver anmälan och startbesked."),
    ("Hur många stora lägenheter finns i Hedvig Eleonora?",
     "Enligt områdesfakta 2025 har 1 119 av 7 290 lägenheter i flerbostadshus fem rum eller fler."),
    ("Vem ska vi fråga om köksfläkten i ett hus med kakelugnar?",
     "Sotaren. Staden råder dig att rådgöra med sotaren tidigt om förutsättningarna för en ny eller ändrad ventilations- eller imkanal."),
    ("Kan styrelsen säga nej till att vi flyttar köket på Östermalm?",
     "Bara om åtgärden är till påtaglig skada eller olägenhet för föreningen. Tillståndet kan förenas med villkor, och ett nej kan prövas av hyresnämnden."),
  ],
  "sources": [_of("Hedvig Eleonora", "inre-staden/norra-innerstaden/hedvig-eleonora"), _STH_KOK, _STH_KLASS, _BRL, _SKV],
  "cta": ("Vill du flytta eller förnya köket på Östermalm?", "Boka ett gratis platsbesök, så utreder vi stammar, kanaler och kulturvärden innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Rymligt kök i en sekelskifteslägenhet med högt i tak och fiskbensparkett",
     "spacious renovated kitchen in a turn-of-the-century apartment with very high ceiling and ornate stucco cornice, painted green shaker cabinets, marble worktop, large kitchen island, herringbone parquet, tall windows, soft daylight" + _SFX),
    ("Vit kakelklädd eldstad i ett rum bredvid ett nytt kök",
     "tall traditional Swedish kakelugn, a round white glazed ceramic tile stove reaching almost to the ceiling with a decorative crown, no metal stove pipe, standing in the corner of a room next to a newly renovated open kitchen in an old city apartment, wooden floor, stucco ceiling, daylight" + _SFX),
    ("Nytt rörschakt med ledningar i ett kök under renovering",
     "kitchen under renovation in an old apartment, a new vertical pipe shaft framed with studs and open showing new water and drain pipes, protective covering on the floor, no workers, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ ÖSTERÅKER
"koksrenovering-osteraker.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Österåker", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Österåker – helårshus, brunn och anmälan",
  "description": "Köksrenovering i Österåker: kök i fritidshus som blir helårshus, eget avlopp och egen brunn, vad som kräver anmälan och kontrollplan i kommunen.",
  "h1": "Köksrenovering i Österåker",
  "lead": "I Österåker blir allt fler fritidshus helårsbostäder, och då är köket ofta det första som behöver göras om. Med egen brunn och eget avlopp spelar vatten och avlopp större roll än i stan. Geal Entreprenad AB planerar köket efter husets förutsättningar och bygger det färdigt.",
  "card": "Helårshus, brunn och avlopp.",
  "sections": [
    {"id": "helarshus-osteraker", "anchor": "Helårshus",
     "h2": "Från fritidshus till helårshus",
     "paras": [
       "Österåkers kommun beskriver sig som en kommun som växer snabbt, där flera områden utanför tätorten utvecklas från fritidshus till mer permanent boende. I vissa av dem finns ännu inget kommunalt vatten och avlopp, och de boende har eget avlopp och egen brunn. Kommunalt vatten och avlopp sköts av Roslagsvatten.",
       "Ett kök i ett fritidshus är ofta byggt för korta perioder: liten diskbänk, ingen diskmaskin och en enkel fläkt. När huset ska användas året runt behöver köket klara mer vatten, mer värme och mer matlagning. Vi börjar med att ta reda på hur huset får sitt vatten och vart avloppet går. I ett äldre fritidshus behöver vi också se efter hur elen är dragen, om golvet bär en tyngre köksö och om väggarna är isolerade för vinterbruk. Ett nytt kök i ett oisolerat hörn kan få kalla ytor och fukt bakom skåpen.",
     ],
     "aside": None},
    {"id": "va-osteraker", "h2": "Eget avlopp och egen brunn",
     "paras": [
       "Kommunen skriver att vi i Sverige i snitt använder 140 liter vatten per person och dag, varav ungefär tio liter till mat och dryck. Resten går bland annat till disk, dusch och toalett. Med egen brunn kan det bli problem när grundvattennivåerna sjunker, och kommunen ger råd som att fylla diskmaskinen innan den körs och att inte diska under rinnande vatten. Snålspolande kranar är ett annat av kommunens råd.",
       "För ett kök betyder det att vi väljer blandare och diskmaskin med låg vattenförbrukning när huset har egen brunn. Har huset eget avlopp är det miljö- och hälsoskyddsavdelningen som svarar på frågor om anläggningen, och det är bra att veta om den är byggd för permanentboende innan köket får fler vattenförbrukare.",
     ],
     "aside": {"title": "Kommunens råd i köket", "items": [
       "Fyll diskmaskinen", "Diska inte under rinnande vatten", "Snålspolande kranar", "Laga droppande kranar"]}},
    {"id": "anmalan-osteraker", "h2": "Det här kräver anmälan i Österåker",
     "paras": [
       "Kommunens lista över anmälningspliktiga åtgärder är tydlig. Anmälan krävs bland annat vid installation eller väsentlig ändring av vattenförsörjning eller avlopp i en byggnad, vid ändring av bärande väggar och balkar, vid nya eller förändrade rördragningar inne i bjälklag, vid ny eller ändrad ventilation och vid installation av en kamin eller eldstad.",
       "Ett kök som flyttas eller får en ny diskplats med rör genom bjälklaget hamnar alltså på listan. Till anmälan vill kommunen ha relevanta handlingar – till exempel VA-situationsplan, planritning, VVS-ritning eller konstruktionsritningar – och ett förslag till kontrollplan, som behövs för alla anmälningar. Arbetet får börja först när startbeskedet har kommit.",
     ],
     "aside": {"title": "Kräver anmälan", "items": [
       "Ny eller ändrad VA-installation", "Rördragning i bjälklag", "Ändrad ventilation", "Bärande väggar och balkar"]}},
    {"id": "byggregler-osteraker", "h2": "Byggreglerna och kontrollplanen",
     "paras": [
       "Från den 1 juli 2025 gäller Boverkets nya byggregler. Kommunen har lagt ut mallar för en enkel kontrollplan både för de nya reglerna och för de äldre reglerna BBR och EKS, eftersom det under en övergångsperiod fram till den 1 juli 2026 gick att välja. Vi tar fram kontrollplanen efter de regler som gäller för ditt ärende.",
       "El och VVS utförs av behöriga installatörer. Om köket ska få en vedspis eller om en kamin ska stå i samma rum krävs en egen anmälan. Funderar du på att bygga ut huset samtidigt beskriver vi det under " + _L.format("tillbyggnad-osteraker.html", "tillbyggnad i Österåker") + ", och mer om kök i allmänhet finns under " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi ett kök i Österåker",
  "steps": [
    ("Platsbesök", "Gratis besök där vi ser hur vatten, avlopp och ventilation är ordnade."),
    ("Förslag", "Kök med vattensnåla val om huset har egen brunn."),
    ("Anmälan", "Anmälan med handlingar och kontrollplan där det krävs."),
    ("Rivning", "Det gamla köket rivs och underlaget kontrolleras."),
    ("Bygget", "El och VVS via behöriga installatörer, montering av köket."),
    ("Överlämning", "Genomgång av köket och dokumentation."),
  ],
  "rot_h2": "ROT-avdrag för köket",
  "rot": [_ROT_HUS],
  "price_h2": "Vad påverkar priset på ett kök i Österåker?",
  "price": [
    "Om köket flyttas, rördragning genom bjälklag, ventilation, el till spis och ugn i ett äldre hus, inredning och vitvaror samt transport till skärgård eller landsbygd. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kräver ett nytt kök anmälan i Österåker?",
     "Om du ändrar vatten och avlopp väsentligt, drar nya rör i bjälklaget, ändrar ventilationen eller bärande väggar krävs anmälan enligt kommunens lista."),
    ("Vilken kontrollplan ska vi använda i Österåker?",
     "Kommunen har mallar för en enkel kontrollplan både för Boverkets nya byggregler och för BBR och EKS. Vilken som gäller beror på ärendet."),
    ("Vem svarar på frågor om eget avlopp i Österåker?",
     "Miljö- och hälsoskyddsavdelningen. Frågor om kommunalt vatten och avlopp går till Roslagsvatten."),
    ("Hur sparar vi vatten i köket när vi har egen brunn i Österåker?",
     "Kommunen råder dig att fylla diskmaskinen innan den körs, inte diska under rinnande vatten och laga droppande kranar."),
    ("Behövs anmälan om vi sätter en vedspis i köket i Österåker?",
     "Ja. Kommunen räknar installation av kamin eller eldstad till de åtgärder som kräver anmälan och startbesked."),
  ],
  "sources": [("Österåkers kommun – Anmälan", "https://www.osteraker.se/byggabomiljo/bygganyttandraellerriva/anmalan.4.367d658917909e8fc2bad6.html"),
              ("Österåkers kommun – Vatten och avlopp", "https://www.osteraker.se/byggabomiljo/vattenochavlopp.4.367d658917909e8fc2b3a4.html"),
              _SKV],
  "cta": ("Vill du förnya köket i Österåker?", "Boka ett gratis platsbesök, så går vi igenom vatten, avlopp och ventilation innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust nytt kök i ett trähus med fönster mot skog och vatten",
     "bright new kitchen in a Swedish wooden house with white painted wood panel walls, light oak cabinets, a window over the sink looking out to pine forest and a glimpse of water, wide plank floor, summer daylight" + _SFX),
    ("Enkelt gammalt kök i ett fritidshus före renovering",
     "simple old kitchen in a Swedish summer cottage before renovation, small sink, old cabinets with worn paint, small window with checked curtain removed, wooden floor, daylight" + _SFX),
    ("Snålspolande köksblandare över en diskho",
     "close-up of a modern water-saving kitchen mixer tap over a stainless steel sink with an integrated dishwasher below, light worktop, soft daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ SKÄRHOLMEN
"koksrenovering-skarholmen.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Skärholmen", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Skärholmen – miljonprogram och radhus",
  "description": "Köksrenovering i Skärholmen: kök från 1960-talet i bostadsrätt och radhus, vad hyresgäster får göra, styrelsens tillstånd, fläkt och anmälan.",
  "h1": "Köksrenovering i Skärholmen",
  "lead": "Skärholmen byggdes på 1960-talet, och många kök har samma planlösning som när husen var nya. Vem som får bygga om köket beror på om du hyr, äger en bostadsrätt eller har ett radhus. Geal Entreprenad AB reder ut vad som gäller och bygger köket färdigt.",
  "card": "1960-talskök, bostadsrätt och radhus.",
  "sections": [
    {"id": "historia-skarholmen", "anchor": "1960-talet",
     "h2": "Ett 1960-talsområde",
     "paras": [
       "Enligt Stockholmskällan började inflyttningen i det nya Skärholmen 1965, och Skärholmens centrum invigdes 1968. Stadens vägledning Varsam utveckling av småhus- och villaområden räknar Skärholmen, Bredäng, Sätra och Vårberg till de storskaliga stadsdelarna. Bredäng började byggas 1962 och följdes av Sätra, och industrialiseringen av byggtekniken fick sitt genombrott just då.",
       "Det betyder att många kök i området är byggda med standardiserade mått och har ventilation och ledningar som är dragna på samma sätt i hela huset. Det kan göra det enklare att bygga ett nytt kök på samma plats – och svårare att flytta det. Vägledningen beskriver också hur gruppbyggda småhus och radhus utgjorde en stor del av miljonprogrammet, och hur andelen småhus ökade i början av 1970-talet. I de husen är köken ofta små och ligger mot entrén, och den vanligaste önskan är att öppna dem mot vardagsrummet.",
     ],
     "aside": None},
    {"id": "upplatelse-skarholmen", "h2": "Hyresrätt, bostadsrätt eller radhus",
     "paras": [
       "Stadens områdesfakta för 2025 räknar i Skärholmens stadsdelsområde 3 479 lägenheter hos allmännyttan och 6 502 övriga hyresrätter i flerbostadshus, 3 315 bostadsrätter i flerbostadshus och 1 976 småhus med äganderätt. De flesta hushåll hyr alltså. Stockholms stad skriver att den som bor i hyresrätt normalt inte får flytta kök eller badrum – ett nytt kök i en hyreslägenhet beställs av hyresvärden.",
       "I en bostadsrätt kräver bostadsrättslagen styrelsens tillstånd för ändring av ledningar för vatten och avlopp, för ändrad ventilation, för ingrepp i bärande konstruktion och för annan väsentlig förändring. I ett småhus med äganderätt är det du själv som ansvarar för att arbetet uppfyller kraven.",
     ],
     "aside": {"title": "Skärholmens stadsdelsområde 2025", "items": [
       "3 479 allmännytta", "6 502 övriga hyresrätter", "3 315 bostadsrätter", "1 976 småhus med äganderätt"]}},
    {"id": "flakt-skarholmen", "h2": "Fläkt och frånluft i flerbostadshus",
     "paras": [
       "Stockholms stad skriver att ett kök ska ha tillräcklig frånluft och uppfylla kraven för imkanal. Ska en kanal användas för både kök och badrum måste dess mått räcka, och sotaren bör tillfrågas tidigt. I hus med gemensam mekanisk frånluft är det ofta föreningen som bestämmer vilken typ av köksfläkt som får sättas upp, så att flödena i huset inte rubbas.",
       "En väsentlig ändring av ventilationen – till exempel en fläkt med egen motor som påverkar luftflödena, nya kanaler eller ett aggregat – kräver anmälan och startbesked. Att byta till en kolfilterfläkt eller en spiskåpa av samma typ som tidigare är normalt en enklare fråga, men det är föreningens regler som gäller. Staden påpekar också att arbetet ska uppfylla de tekniska egenskapskraven i plan- och bygglagen även när ingen anmälan krävs.",
     ],
     "aside": {"title": "Fråga föreningen om", "items": [
       "Tillåten typ av köksfläkt", "Regler för ledningar och stammar", "Arbetstider i huset", "Vem som får göra VVS"]}},
    {"id": "radhus-skarholmen", "h2": "Radhusen i Sätra och Vårberg",
     "paras": [
       "Vägledningen beskriver hur en stor del av miljonprogrammets bebyggelse var gruppbyggda småhus och radhus. I Sätra finns enligt områdesfakta 536 småhus med äganderätt och i Vårberg 577. I ett sådant hus kan köket ofta göras om friare, men en flytt som kräver nya rör i bjälklaget, ändrad ventilation eller en öppning i en bärande vägg kräver ändå anmälan till staden.",
       "Vi ritar köket efter husets mått och ser till att el och VVS utförs av behöriga installatörer. Står badrummet också på tur beskriver vi det under " + _L.format("badrumsrenovering-skarholmen.html", "badrumsrenovering i Skärholmen") + ", och mer om kök i allmänhet finns under " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi ett kök i Skärholmen",
  "steps": [
    ("Platsbesök", "Gratis besök där vi ser hur kök, kanal och ledningar är ordnade."),
    ("Upplåtelseform", "Vi stämmer av vad föreningen eller hyresvärden tillåter."),
    ("Förslag", "Kök efter lägenhetens eller radhusets mått, med fläkt och vitvaror."),
    ("Tillstånd och anmälan", "Styrelsens tillstånd och anmälan till staden där det krävs."),
    ("Bygget", "Rivning, el och VVS via behöriga installatörer, montering."),
    ("Överlämning", "Genomgång av köket och dokumentation."),
  ],
  "rot_h2": "ROT-avdrag för kök i Skärholmen",
  "rot": [_ROT_BR],
  "price_h2": "Vad påverkar priset på ett kök i Skärholmen?",
  "price": [
    "Om köket stannar på samma plats, fläkt och ventilation, el och VVS, inredning och vitvaror och om en vägg öppnas. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Får vi renovera köket i vår hyreslägenhet i Skärholmen?",
     "Staden skriver att den som hyr normalt inte får flytta kök eller badrum. Kontakta hyresvärden om köket behöver göras om."),
    ("Vilken köksfläkt får vi sätta upp i en bostadsrätt i Skärholmen?",
     "Det beror på husets ventilation och föreningens regler. Ändrad ventilation kräver styrelsens tillstånd enligt bostadsrättslagen."),
    ("Behövs anmälan för att flytta köket i ett radhus i Sätra?",
     "Om flytten kräver nya rör i bjälklaget, ändrad ventilation eller en öppning i en bärande vägg krävs anmälan och startbesked."),
    ("När byggdes Skärholmen?",
     "Inflyttningen började 1965 och Skärholmens centrum invigdes 1968, enligt Stockholmskällan."),
    ("Kan styrelsen neka oss att byta kök i Skärholmen?",
     "Bara om åtgärden är till påtaglig skada eller olägenhet för föreningen. Styrelsen kan sätta villkor, och den som är missnöjd kan begära att hyresnämnden prövar beslutet."),
    ("Behövs bygglov för att flytta köket i en lägenhet i Skärholmen?",
     "Nej. Stockholms stad kräver inget bygglov, men anmälan och startbesked om bärande delar, brandskydd eller ventilation ändras väsentligt eller om en ny VA-stam dras i ett nytt schakt."),
    ("Ger ett nytt kök i en bostadsrätt i Skärholmen rotavdrag?",
     "Ja, för arbete inne i lägenheten som du ansvarar för enligt stadgarna, till exempel att montera fast köksinredning vid en omfattande renovering."),
  ],
  "sources": [("Stockholmskällan – På upptäcktsfärd kring Skärholmen (Riksutställningar och Stockholms stadsmuseum)",
               "https://stockholmskallan.stockholm.se/post/35428"),
              _VARSAM, _of("Skärholmens stadsdelsområde", "soderort/skarholmen/skarholmen-stadsdelsomrade"),
              _of("Sätra", "soderort/skarholmen/satra"), _of("Vårberg", "soderort/skarholmen/varberg"),
              _STH_KOK, _BRL, _SKV],
  "cta": ("Vill du byta kök i Skärholmen?", "Boka ett gratis platsbesök, så stämmer vi av föreningens regler innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nytt kök med ljusa luckor i en lägenhet från 1960-talet",
     "newly renovated kitchen in a 1960s Swedish apartment, light grey flat cabinet doors, white laminate worktop, built-in oven in a tall unit, simple extractor hood, window with view of other apartment blocks and trees, daylight" + _SFX),
    ("Lamellhus från 1960-talet bland träd",
     "1960s Swedish apartment blocks with light facades and balconies among pine trees and lawns in a large-scale suburb, footpath, summer daylight" + _SFX),
    ("Radhuslänga från 1970-talet med små trädgårdar",
     "1970s Swedish terraced houses with brown wooden panels and small front gardens with hedges along a car-free path, summer daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ FARSTA
"koksrenovering-farsta.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Farsta", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Farsta – ABC-staden och radhusen",
  "description": "Köksrenovering i Farsta: kök i bostadsrätt i ABC-staden, radhus i bostadsrättsförening, villor med äganderätt, anmälan, fläkt och styrelsens tillstånd.",
  "h1": "Köksrenovering i Farsta",
  "lead": "I Farsta bor många i bostadsrätt i flerbostadshus eller i ett radhus som ägs av en förening, och det avgör vem som ska godkänna ett nytt kök. Geal Entreprenad AB tar reda på vad som gäller för ditt hus, ritar köket och bygger det färdigt.",
  "card": "ABC-staden, radhus och villor.",
  "sections": [
    {"id": "abc-farsta", "anchor": "ABC-staden",
     "h2": "Farsta – den första ABC-staden i Söderort",
     "paras": [
       "Stadsmuseet beskriver hur Farsta byggdes som den första ABC-staden i Söderort, där A stod för arbetsplatser, B för bostäder och C för centrum. Farsta centrum invigdes i oktober 1960. Närmast centrum står höga punkthus, längre ut lägre bostadshus, och i utkanterna lades flera stora radhusområden.",
       "Stadens områdesfakta för 2025 räknar i Farsta stadsdelsområde 10 543 lägenheter hos allmännyttan och 4 614 övriga hyresrätter i flerbostadshus, 9 914 bostadsrätter i flerbostadshus, 639 bostadsrätter i småhus och 3 806 småhus med äganderätt. Ett kök i Farsta kan alltså vara en hyresvärds, en förenings eller ditt eget att besluta om.",
     ],
     "aside": {"title": "Farsta stadsdelsområde 2025", "items": [
       "9 914 bostadsrätter i flerbostadshus", "639 bostadsrätter i småhus", "3 806 småhus med äganderätt"]}},
    {"id": "radhus-brf-farsta", "h2": "Radhus i bostadsrättsförening",
     "paras": [
       "Ett radhus med bostadsrätt ser ut som ett eget hus, men det är föreningen som äger det. Bostadsrättslagen gäller då fullt ut: styrelsens tillstånd krävs för ingrepp i bärande konstruktion, ändring av ledningar för avlopp, värme eller vatten, ändring av ventilation och annan väsentlig förändring. Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet för föreningen.",
       "Skatteverket ger rotavdrag i en bostadsrätt för arbete inne i bostaden som du ansvarar för enligt stadgarna. Därför är det värt att läsa stadgarna innan köket planeras – de visar både vad du själv ansvarar för och vad föreningen ska godkänna.",
     ],
     "aside": {"title": "Läs stadgarna om", "items": [
       "Vad du ansvarar för i bostaden", "Ledningar och stammar", "Ventilation och fläkt", "Krav på dokumentation"]}},
    {"id": "anmalan-farsta", "h2": "När köket kräver anmälan",
     "paras": [
       "Stockholms stad kräver inget bygglov för att flytta ett kök, men anmälan och startbesked om flytten påverkar bärande konstruktion eller brandskydd, om ventilationen installeras eller ändras väsentligt eller om en ny VA-stam dras i ett nytt schakt. Oavsett om anmälan krävs ska arbetet uppfylla de tekniska egenskapskraven.",
       "I de äldre radhusen och villorna är det ofta väggen mellan kök och vardagsrum som ska bort. Är den bärande behövs konstruktionsunderlag, en anmälan och – i en bostadsrätt – styrelsens tillstånd. Vi tar fram underlaget innan något rivs. När väggen är borta behöver golv, tak och el i båda rummen ofta anpassas, och det är bra att planera det i samma omgång så att köket och vardagsrummet blir färdiga samtidigt.",
     ],
     "aside": None},
    {"id": "flakt-farsta", "h2": "Fläkten och kanalen",
     "paras": [
       "Staden påpekar att ett kök ska ha tillräcklig frånluft och klara kraven för imkanal, och att en kanal som delas med badrummet måste ha tillräckliga mått. Sotaren kan svara på vad en befintlig kanal tål. I ett flerbostadshus från ABC-stadens tid är ventilationen ofta gemensam för hela huset, och då bestämmer föreningen vilken fläkt som passar.",
       "El och VVS utförs av behöriga installatörer. Bor du i Tallkrogen och vill bygga ut den lilla stugan samtidigt beskriver vi det under " + _L.format("attefallshus-farsta.html", "attefallshus i Farsta") + ", och mer om kök i allmänhet finns under " + _L.format("koksrenovering.html", "köksrenovering") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi ett kök i Farsta",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på kök, väggar, kanal och ledningar."),
    ("Stadgar och regler", "Vi går igenom vad föreningen ska godkänna och vad du ansvarar för."),
    ("Förslag", "Planlösning, fläkt, inredning och vitvaror."),
    ("Tillstånd och anmälan", "Styrelsens tillstånd och anmälan till staden där det krävs."),
    ("Bygget", "Rivning, el och VVS via behöriga installatörer, montering."),
    ("Överlämning", "Genomgång av köket och dokumentation."),
  ],
  "rot_h2": "ROT-avdrag för köket i Farsta",
  "rot": [_ROT_BR],
  "price_h2": "Vad påverkar priset på ett kök i Farsta?",
  "price": [
    "Om köket flyttas eller en vägg öppnas, fläkt och kanal, el och VVS, inredning och vitvaror samt föreningens krav på dokumentation. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi föreningens tillstånd för nytt kök i ett bostadsrättsradhus i Farsta?",
     "Ja, om arbetet rör ledningar, ventilation, bärande delar eller är en annan väsentlig förändring. Det följer av bostadsrättslagen."),
    ("Får vi ta bort väggen mellan kök och vardagsrum i Farsta?",
     "Om väggen är bärande krävs konstruktionsunderlag och anmälan till staden, och i en bostadsrätt styrelsens tillstånd."),
    ("Ger ett nytt kök i en bostadsrätt i Farsta rotavdrag?",
     "Ja, för arbete inne i bostaden som du ansvarar för enligt stadgarna, till exempel att montera fast köksinredning vid en omfattande renovering."),
    ("Vem vet om köksfläkten passar husets ventilation i Farsta?",
     "Sotaren och föreningen. Staden råder dig att rådgöra med sotaren tidigt om en ny eller ändrad kanal."),
    ("Får vi byta kök i en hyreslägenhet i Farsta?",
     "Staden skriver att den som hyr normalt inte får flytta kök eller badrum. Ett nytt kök i en hyreslägenhet är hyresvärdens beslut."),
  ],
  "sources": [("Stockholms stadsmuseum – Stockholms spår: Farsta (pdf)",
               "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000015.pdf"),
              _of("Farsta stadsdelsområde", "soderort/farsta/farsta-stadsdelsomrade"), _STH_KOK, _BRL, _SKV],
  "cta": ("Planerar du ett nytt kök i Farsta?", "Boka ett gratis platsbesök, så går vi igenom stadgarna och huset innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyrenoverat kök i ett radhus med vita luckor och matplats vid fönstret",
     "newly renovated kitchen in a 1960s Swedish terraced house, white cabinets, wood worktop, dining table by a large window facing a small garden, vinyl plank floor, daylight" + _SFX),
    ("Höga punkthus och lägre bostadshus i en förort från 1960",
     "Swedish 1960 suburb with tall point-block apartment towers in the background and lower residential buildings in front, trees and lawns, summer daylight" + _SFX),
    ("Öppning där en vägg mellan kök och vardagsrum har tagits bort",
     "interior of a terraced house during renovation where the wall between kitchen and living room has been removed, new wooden beam over the opening, protective covering on the floor, no workers, daylight" + _SFX),
  ],
},
}
