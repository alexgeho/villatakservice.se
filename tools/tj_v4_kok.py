# -*- coding: utf-8 -*-
"""Tjänster v4 – ortsidor köksrenovering i Huddinge, Sollentuna, Järfälla, Haninge, Tyresö och Värmdö
(2026-10-25). Schema: se tools/tj_check.py. Bebyggelsefakta är omformulerade från tools/takreno_orter.py
(TRP, kontrollerade mot källorna där). Nya fakta öppnade och kontrollerade 2026-10-25: Huddinge kommun
(VA, bärande konstruktion, ventilation och OVK), Sollentuna kommun (ventilation, VA, bärande konstruktion),
Järfälla kommun (bärande konstruktion, bygglovsbefriade åtgärder, ABVA), Haninge kommun (anmälan om VA-arbete,
ventilation, bärande konstruktion), Tyresö kommun (VA-anslutning, ändringar i PBL), Värmdö kommun (små
avlopp, ändringar i PBL) och Skatteverket (rotarbete i småhus). Inga priser, garantier, omdömen, egna uppdrag
eller cert."""

L = '<a class="text-link" href="{0}">{1}</a>'
X = '<a class="text-link" href="{0}" rel="noopener">{1}</a>'

S_ROT = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
S_ROTJOB = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
            "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")

U_HUD_VA = "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/installation-eller-andring-av-vatten-och-avlopp-va/"
U_HUD_BAR = "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/andra-en-byggnads-barande-konstruktion"
U_HUD_VENT = "https://www.huddinge.se/bostad-och-miljo/bygglov/nar-behover-du-bygglov/ventilation-och-ovk"
U_HUD_KMP = "https://webb.huddinge.se/globalassets/huddinge.se/_gemensamma/styrdokument-overgripande/program/kulturmiljoprogram/kulturmiljoprogram--del-2.pdf"

U_SOL_VENT = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/installation-eller-andring-av-ventilation/"
U_SOL_VA = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/installation-eller-andring-i-installationer-va/"
U_SOL_BAR = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/andring-av-barande-konstruktion/"
U_SOL_OP = "https://www.sollentuna.se/globalassets/bygga-bo-och-miljo/oversiktsplan/oversiktsplan-for-sollentuna-med-sikte-pa-2040.pdf"
U_SOL_KM = "https://www.sollentuna.se/bygga-bo--miljo/bygga-nytt-andra-eller-riva/kulturmiljoer/"

U_JAR_BAR = "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/andraibarandekonstruktion.4.69a1b161151015104f4bca0b.html"
U_JAR_BEF = "https://www.jarfalla.se/byggaboochmiljo/byggaochbo/bygglov/behovslovelleranmalan/bygglovsbefriadeatgarder.4.a41712119a05132defe8bb3.html"
U_JAR_ABVA = "https://www.jarfalla.se/download/18.2703617f44b5b1b6ed8b3/1648040574196/abva-jarfalla.pdf"
U_JAR_JAK = "https://www.jarfalla.se/download/18.68e7a727168e12dd179a4080/1550245872956/kulturmiljoplan-jakobsberg.pdf"
U_JAR_KAL = "https://www.jarfalla.se/download/18.68e7a727168e12dd179a407f/1550245859848/kulturmiljoplan-kallhall.pdf"

U_HAN_KAR = "https://www.haninge.se/contentassets/44e92cc3b6374ed186a0e26c7b1c1509/haninges-karaktarsmiljoer.pdf"
U_HAN_VA = "https://www.haninge.se/sjalvservice/vatten--och-avloppsarbete--anmal/"
U_HAN_VENT = "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/ventilation/"
U_HAN_BAR = "https://www.haninge.se/bygga-trafik-och-miljo/bygga-nytt-andra-riva/vad-vill-du-bygga/andring-av-barande-konstruktion/"
U_HAN_DAL = "https://www.haninge.se/siteassets/bygga-bo-och-miljo/oversiktsplanering-och-detaljplaner/detaljplaner/kust-och-skargard/dalaro-34-hotell-bellevue/antikvarisk-forundersokning.pdf"

U_TYR_VA = "https://www.tyreso.se/boende--miljo/vatten-och-avlopp/anslutning.html"
U_TYR_PBL = "https://www.tyreso.se/boende--miljo/bygga/bygga-riva-eller-andra/forandringar-i-plan--och-bygglagen-fran-1-december-2025.html"
U_TYR_SLM = "https://insynsverige.se/documentHandler.ashx?did=20437"
U_TYR_FAS = "https://www.tyreso.se/download/18.38176aff18b5b7301f888ab9/1698683875432/Planbeskrivning%20Fasanv%C3%A4gen%20etapp%2013.pdf"

U_VAR_AVL = "https://www.varmdo.se/byggabomiljo/vattenochavlopp/smaavlopp/ansokomsmaavlopp.4.1a82111d16e6c321a368eb23.html"
U_VAR_PBL = "https://www.varmdo.se/byggabomiljo/bygganyttandraellerriva/forandringaripblfrom1december2025.4.18b9914519a768a188a2872.html"
U_VAR_PFO = "https://www.varmdo.se/download/18.52346f71869c9938611c2df/1678200543391/Broschyr%20PFO%20del%201%20-%20uppdaterad%202023.pdf"
U_VAR_GUS = "https://varmdo.se/download/18.3dd2ab3d18c629ae56f50ed/1702902627509/Antikvarisk%20konsekvensanalys%20AIX%202023-09-27.pdf"

PAGES_TJ = {

# =============================== KÖK HUDDINGE ===============================
"koksrenovering-huddinge.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Huddinge", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Huddinge – grupphus, egnahem och stugor",
  "description": "Köksrenovering i Huddinge: grupphuskök från 1970-talet, egnahem i Stuvsta och permanentade "
                 "stugor. Fläkt, avlopp och bärande väggar efter kommunens regler.",
  "h1": "Köksrenovering i Huddinge",
  "lead": "I Huddinge kan nästa kök sitta i ett egnahem från 1920-talet, i ett grupphus i Skogås eller i en "
          "sportstuga som blivit helårsbostad. Husets ålder avgör hur ventilationen fungerar, var avloppet går "
          "och vilka väggar som bär. Vi börjar med ett gratis platsbesök, samordnar snickeri, el och VVS och "
          "drar ROT-avdraget direkt på fakturan.",
  "card": "Grupphus, egnahem och stugor.",
  "sections": [
    {"id": "husen", "anchor": "Husen i Huddinge",
     "h2": "Från egnahemmet vid stambanan till radhuset i Sörskogen",
     "paras": [
       "Enligt " + X.format(U_HUD_KMP, "Huddinges kulturmiljöprogram") + " började Stuvsta egnahemsområde "
       "och Hörningsnäs villastad byggas i början av 1900-talet, och på 1920-talet blev Segeltorp och "
       "Snättringe villatomter. Köken i de husen har ofta bytts flera gånger, och bakom den senaste "
       "inredningen kan det finnas allt från ett gammalt skafferi till en igensatt rökkanal.",
       "Under rekordåren och fram till början av 1980-talet tillkom grupphusområden som Sörskogen, Utsälje "
       "och Östra Skogås. Där byggdes många hus med samma planlösning, och köket ligger därför ofta på samma "
       "ställe i varje hus i längan, med samma mått på stommen och samma dragning av rör.",
       "Vid Mellansjö och Trehörningen byggdes sportstugor på 1910–30-talet, och vid Gömmaren växte ett "
       "sportstugeområde fram. Många av stugorna har permanentats och byggts till. Där kan köket ha flyttat med varje tillbyggnad, och det är först när "
       "golv och väggar öppnas som det syns hur ledningarna verkligen går.",
     ],
     "aside": {"title": "Tre typer av kök", "items": [
       "Egnahem: ombyggt i flera omgångar",
       "Grupphus: samma plan i hela längan",
       "Permanentad stuga: köket har flyttat med tillbyggnaderna",
       "Alla: ta fram ritningar före besöket"]}},
    {"id": "flakt",
     "h2": "Ny köksfläkt – när kommunen vill ha en anmälan",
     "paras": [
       "Huddinge kommun beskriver på sidan om " + X.format(U_HUD_VENT, "ventilation och OVK") + " vilka "
       "ändringar som kräver anmälan och startbesked. Att byta fläkt, fläktmotor eller filter räknas normalt "
       "som underhåll, liksom att byta don och ventiler mot likvärdiga. Även bytet från självdrag till "
       "fläktstyrd frånluft i ett en- eller tvåbostadshus kan enligt kommunen göras utan anmälan.",
       "Anmälan krävs däremot när ett aggregat, en fläkt eller nya kanaler påverkar flödena eller "
       "luftkvaliteten, eller när ventilationen anpassas till en ny planlösning. Det blir aktuellt när köket "
       "öppnas mot vardagsrummet och den gamla frånluften inte längre räcker för den större ytan.",
       "Dras kanalen eller sätts ett aggregat på utsidan av huset kan det enligt kommunen vara en ändring av "
       "det yttre som kräver bygglov. Ska en ny kanal ut genom taket samordnar vi genomföringen med taket, se "
       + L.format("taklaggare-huddinge.html", "takläggare i Huddinge") + ".",
     ],
     "aside": {"title": "Ventilationen i Huddinge", "items": [
       "Byte av fläkt eller filter: ingen anmälan",
       "Självdrag till frånluftsfläkt i villa: ingen anmälan",
       "Nytt aggregat eller nya kanaler: anmälan",
       "Utvändig kanal: kan kräva bygglov"]}},
    {"id": "avlopp-vagg",
     "h2": "Diskbänk på ny plats och väggen mot vardagsrummet",
     "paras": [
       "Flyttas diskbänken bara några decimeter längs samma vägg räcker det oftast att förlänga anslutningen. "
       "Ska den till en köksö eller till andra sidan rummet blir det en ny avloppsdragning. Kommunen skriver "
       "att den som " + X.format(U_HUD_VA, "installerar eller väsentligt ändrar vatten och avlopp") + " "
       "behöver göra en anmälan, och att ett utlåtande från konstruktör krävs om hål tas upp i bärande delar.",
       "Har fastigheten kommunalt vatten och avlopp ansvarar byggherren för att kontakta Stockholm Vatten och "
       "Avfall om anslutningen ändras. Har fastigheten inte kommunalt avlopp ska du "
       "även kontakta kommunens miljötillsyn. Mer om den frågan finns under "
       + L.format("badrumsrenovering-huddinge.html", "badrumsrenovering i Huddinge") + ".",
       "Att ta upp en öppning i en bärande vägg kräver enligt kommunens sida om "
       + X.format(U_HUD_BAR, "bärande konstruktion") + " anmälan och startbesked, och kommunen påpekar att "
       "ritningarna i bygglovsarkivet inte säkert stämmer med det som byggdes. Därför bedömer en konstruktör "
       "väggen på plats innan något rivs.",
     ],
     "aside": None},
    {"id": "grupphuskok",
     "h2": "Grupphusköket från 70-talet",
     "paras": [
       "Ett grupphuskök är sällan stort, och önskan är ofta att öppna det mot vardagsrummet eller flytta "
       "diskbänken till en ny plats. Om väggen mellan rummen är en lätt mellanvägg eller bär bjälklaget "
       "går inte att se på ytan, så det får konstruktören avgöra innan planen låses.",
       "Eftersom längorna är byggda lika går det ofta att använda grannens erfarenhet, till exempel om hur "
       "frånluften är dragen eller var stammen går. Det ersätter inte en egen bedömning, men gör planeringen "
       "snabbare. Golvet under de gamla skåpen saknar ibland ytskikt, och då behöver det läggas nytt där "
       "inredningen flyttas, se " + L.format("golvlaggare-huddinge.html", "golvläggare i Huddinge") + ".",
       "Många väljer att göra om hela bottenvåningen samtidigt. Då är det klokt att måla tak och väggar "
       "innan den nya inredningen kommer på plats – " + L.format("malare-huddinge.html", "målare i Huddinge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till i Huddinge",
  "steps": [
    ("Platsbesök", "Vi mäter köket, ser var frånluft, stam och el går och tittar på väggen mot vardagsrummet."),
    ("Ritningar och konstruktör", "Arkivritningar tas fram, och ska en vägg bort bedömer en konstruktör den på plats."),
    ("Skriftligt kostnadsförslag", "Rivning, installationer, snickeri och montering redovisas var för sig, med anmälan om den behövs."),
    ("Rivning och installationer", "Gamla skåp tas bort, och avlopp, vatten, el och fläkt dras enligt den nya planen."),
    ("Ytskikt och stomme", "Golv och väggar blir klara, stommen monteras och bänkskivan mäts in."),
    ("Inkoppling och genomgång", "Vitvaror och belysning ansluts och provas, och vi går igenom köket tillsammans."),
  ],
  "rot_h2": "ROT-avdrag för köket i Huddinge",
  "rot": [
    "Skatteverket godkänner rotavdrag i småhus för att montera fast köksinredning och installera vitvaror "
    "när det sker i samband med en omfattande renovering. Även att riva väggar och bygga om planlösningen, "
    "sätta kakel, modernisera elen och installera avlopp och ventilation räknas som rotarbete. Avdraget är "
    "30 procent av arbetskostnaden, högst 50 000 kr per person och år, och 75 000 kr sammanlagt med rut.",
    "Skåp, bänkskiva och vitvaror är material och ger inget avdrag. Vi skriver arbete och material var för "
    "sig och drar avdraget på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden för ett kök i Huddinge?",
  "price": [
    "Mest avgör om diskbänk och spis kan stå kvar där avlopp och frånluft redan finns. En vägg som ska "
    "öppnas, ny avloppsdragning till en köksö eller ny ventilation lägger till arbete och ibland en anmälan. "
    "Efter ett gratis besök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi anmäla till Huddinge kommun om köksfläkten byts?",
     "Inte om det är ett byte av fläkt eller filter som inte ändrar flödena. Kommunen kräver anmälan först "
     "när ett aggregat eller nya kanaler påverkar ventilationen."),
    ("Vem kontaktar vi om köksavloppet flyttas i ett hus med kommunalt VA i Huddinge?",
     "Byggherren ska kontakta Stockholm Vatten och Avfall om anslutningen ändras. Är ändringen väsentlig "
     "krävs dessutom en anmälan till kommunen."),
    ("Kan köket i ett grupphus i Skogås öppnas mot vardagsrummet?",
     "Ofta, men en del mellanväggar bär bjälklaget. En konstruktör avgör det på plats, och påverkas den "
     "bärande konstruktionen krävs anmälan och startbesked."),
    ("Stämmer arkivritningarna för vårt hus i Huddinge?",
     "Inte säkert. Kommunen påpekar själv att det som byggdes kan skilja sig från ritningarna, så de bör "
     "kontrolleras på plats."),
    ("Vi har eget avlopp vid sjön – vad gäller när köket flyttas?",
     "Har fastigheten inte kommunalt vatten och avlopp ska du enligt kommunen även kontakta "
     "miljötillsynen när anslutningar ändras."),
  ],
  "sources": [
    ("Huddinge kommun – Ventilation och OVK", U_HUD_VENT),
    ("Huddinge kommun – Installation eller ändring av vatten och avlopp", U_HUD_VA),
    ("Huddinge kommun – Ändra en byggnads bärande konstruktion", U_HUD_BAR),
    ("Huddinge kommun – Kulturmiljöprogram del 2 (pdf)", U_HUD_KMP),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Huddinge göras om?", "Boka ett gratis besök, så går vi igenom fläkt, avlopp och väggar på plats."),
  "img": [
    ("Ljust renoverat kök med grå luckor och vit bänkskiva i ett radhus i Huddinge",
     "renovated kitchen in a 1970s Swedish terraced house, light grey flat-front cabinets, white worktop, "
     "new stainless cooker hood, window towards a small garden with pine trees, light oak floor, soft daylight, "
     "no people, no text"),
    ("Öppnad mellanvägg mellan kök och vardagsrum under renovering",
     "interior of a Swedish 1970s house during kitchen renovation, wall between kitchen and living room "
     "partly opened with a new timber header, exposed plumbing pipes on the floor, dust sheets, daylight, "
     "no people, no text"),
  ],
  "related": [],
},

# =============================== KÖK SOLLENTUNA ===============================
"koksrenovering-sollentuna.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Sollentuna", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Sollentuna – villastad och radhuslängor",
  "description": "Köksrenovering i Sollentuna: villor i Tureberg och Norrviken, radhus från 1960–80-talet, "
                 "anmälan för fläkt och avlopp och ritningar ur bygglovsarkivet.",
  "h1": "Köksrenovering i Sollentuna",
  "lead": "Sollentuna har både villor från villastadens första tid och stora radhusområden från 1960-talet "
          "och framåt. Ett kök i en sekelskiftesvilla och ett kök i en radhuslänga kräver olika förarbete, och "
          "kommunen har tydliga regler för när ventilation, avlopp och väggar ska anmälas. Vi börjar med ett "
          "gratis platsbesök och ett skriftligt kostnadsförslag.",
  "card": "Villastad och radhuslängor.",
  "sections": [
    {"id": "husen", "anchor": "Husen i Sollentuna",
     "h2": "Villastad längs järnvägen, radhus i flera vågor",
     "paras": [
       "Enligt " + X.format(U_SOL_OP, "Sollentunas översiktsplan") + " började småhus och villor byggas i "
       "början av 1900-talet när stationerna i Tureberg och Norrviken anlades, och kommunen vill bevara den "
       "prägel av villastad som växte fram under seklets första hälft. Köken i de husen har ofta byggts om "
       "flera gånger, och det gamla läget kan skymta fram i form av en igensatt kanal eller ett flyttat avlopp.",
       "Från 1960-talet till början av 1980-talet byggdes större radhusområden i flera delar av "
       "kommunen. I en länga är köken ofta likadana, och originalköken är i dag "
       "så gamla att stommen, bänkskivan och elen ofta behöver bytas samtidigt.",
       "Översiktsplanen säger också att radhus och sammanhållna grupper kan förändras, men att varje ändring "
       "ska bidra till helheten. För köket handlar det främst om det som syns utifrån: en ny fläkthuv i "
       "fasaden eller ett nytt fönster mot gatan.",
     ],
     "aside": {"title": "Före besöket", "items": [
       "Byggår och eventuella ombyggnader",
       "Ritningar ur bygglovsarkivet",
       "Var frånluften går i dag",
       "Önskemål om öppen planlösning"]}},
    {"id": "anmalan",
     "h2": "Tre anmälningar som kan bli aktuella i köket",
     "paras": [
       "Sollentuna kommun har en sida för varje åtgärd. Om " + X.format(U_SOL_VENT, "ventilation") + " skriver "
       "kommunen att anmälan krävs för ett nytt ventilationssystem eller en större ändring av det befintliga, "
       "till exempel byte av aggregat, fläkt eller kanaler. Kommer aggregat eller kanaler på fasaden kan det "
       "dessutom krävas bygglov.",
       "För " + X.format(U_SOL_VA, "vatten och avlopp") + " gäller anmälan när en anläggning installeras eller "
       "ändras i större omfattning, och vid stambyte som påverkar stammarna, konstruktionen eller planlösningen. "
       "Att " + X.format(U_SOL_BAR, "riva en bärande vägg") + " eller göra ingrepp i bjälklag kräver anmälan "
       "och startbesked med plan- och sektionsritning, konstruktionsritningar och förslag till kontrollplan.",
       "Kommunen anger en handläggningstid på ungefär två till fem veckor för bärande konstruktion och två "
       "till fyra veckor för ventilation och VA, och skriver att den just nu kan vara längre. Vi lägger "
       "därför in anmälan tidigt i tidplanen, så att rivningen kan börja när startbeskedet har kommit.",
     ],
     "aside": {"title": "Kräver anmälan i Sollentuna", "items": [
       "Nytt ventilationssystem eller ny fläkt som ändrar systemet",
       "Större ändring av vatten och avlopp",
       "Ingrepp i bärande vägg eller bjälklag"]}},
    {"id": "radhusko",
     "h2": "Originalköket i radhuslängan",
     "paras": [
       "I ett radhus från 1970-talet är utrymmet för köket givet av längans mått, och i hus som byggts "
       "lika går stammen ofta i samma läge. Därför lönar det sig att behålla diskbänken där den är "
       "och lägga arbetet på stomme, bänkskiva och belysning.",
       "Vill du öppna mot vardagsrummet är det väggens funktion som avgör. Kommunen tipsar om att äldre "
       "ritningar finns gratis i bygglovsarkivet, och de visar ofta hur bjälklaget är upplagt. En konstruktör "
       "kontrollerar ändå väggen på plats, eftersom huset kan ha ändrats sedan ritningarna gjordes.",
       "Många passar på att göra om badrummet i samma veva, eftersom stammen ofta är lika gammal – se "
       + L.format("badrumsrenovering-sollentuna.html", "badrumsrenovering i Sollentuna") + ". Ska listverk "
       "och dörrar anpassas efter det nya köket gör vi det i samma entreprenad, se "
       + L.format("snickare-sollentuna.html", "snickare i Sollentuna") + ".",
     ],
     "aside": None},
    {"id": "villakok",
     "h2": "Köket i en äldre villa i Tureberg eller Norrviken",
     "paras": [
       "I en äldre villa kan köket vara ett eget rum med dörr, och huset kan ha en skorsten med "
       "kanaler som inte längre används. Ska en köksfläkt kopplas till en befintlig kanal måste den klara uppgiften, "
       "och ändras systemet krävs anmälan. Ibland är det enklare att dra en ny kanal genom taket.",
       "Kommunen hänvisar på sidan om " + X.format(U_SOL_KM, "kulturhistoriska byggnader") + " till ett "
       "kartlager med områden i kulturmiljöplanen. Inne i huset påverkar det sällan köket, men ett nytt "
       "fönster, en dörr mot trädgården eller en fläkthuv på fasaden kan behöva prövas.",
       "I en villa med flera våningar kan även bjälklaget över köket behöva kontrolleras om tunga skåp eller "
       "en ny kanal ska fästas i taket. Ska en ny kanal ut genom taket tar vi med genomföringen och plåten "
       "runt den, se "
       + L.format("taklaggare-sollentuna.html", "takläggare i Sollentuna") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Arbetsgången för ett nytt kök i Sollentuna",
  "steps": [
    ("Besök och mätning", "Vi går igenom köket, stammen, frånluften och väggarna och mäter upp rummet."),
    ("Arkiv och konstruktör", "Äldre ritningar hämtas ur bygglovsarkivet, och vid behov bedömer en konstruktör väggen."),
    ("Förslag och anmälan", "Du får ett skriftligt kostnadsförslag, och vid behov skickas anmälan in i god tid."),
    ("Rivning och rördragning", "Den gamla inredningen tas bort, och el, vatten, avlopp och fläktkanal förbereds."),
    ("Montering", "Stommen monteras, bänkskivan mäts in och kakel eller stänkskydd sätts upp."),
    ("Slutkontroll", "Vitvaror ansluts, belysning provas och du får dokumentationen från arbetet."),
  ],
  "rot_h2": "Rotavdrag för köksrenovering i Sollentuna",
  "rot": [
    "I ett småhus ger det rotavdrag att montera fast köksinredning och installera vitvaror i samband med en "
    "omfattande renovering, att byta och reparera köksluckor och att sätta kakel och klinker, enligt "
    "Skatteverket. Avdraget är 30 procent av arbetskostnaden med ett tak på 50 000 kr per person och år, och "
    "högst 75 000 kr tillsammans med rutavdrag.",
    "Själva skåpen och vitvarorna räknas som material. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Det här påverkar priset i Sollentuna",
  "price": [
    "Om diskbänk och spis kan stå kvar, om en vägg ska öppnas med balk, om elen behöver moderniseras och om "
    "en ny kanal ska dras genom taket. Därefter avgör val av stomme, bänkskiva och vitvaror. Efter ett "
    "gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur lång handläggningstid har Sollentuna för en anmälan om bärande vägg?",
     "Kommunen anger ungefär två till fem veckor och skriver att det just nu kan ta längre tid. Arbetet får "
     "börja först efter startbesked."),
    ("Kostar det något att ta fram gamla ritningar på huset i Sollentuna?",
     "Nej, kommunen skriver att äldre ritningar kan sökas fram ur bygglovsarkivet utan kostnad."),
    ("Måste köksfläkten anmälas om vi byter till ett nytt ventilationsaggregat?",
     "Ja. Sollentuna kräver anmälan vid en större ändring av ventilationen, till exempel byte av aggregat, "
     "fläkt eller kanaler."),
    ("Kan vi ha kvar stammen när radhusköket renoveras?",
     "Oftast, om den är i gott skick. Ska den bytas och det påverkar stammar, konstruktion eller planlösning "
     "krävs anmälan."),
    ("Behövs bygglov för en fläkthuv på fasaden till ett radhus i Sollentuna?",
     "Det kan krävas om installationen innebär en stor förändring av husets yttre. Stäm av med kommunen innan "
     "kanalen dras ut genom väggen."),
  ],
  "sources": [
    ("Sollentuna kommun – Installation eller ändring av ventilation", U_SOL_VENT),
    ("Sollentuna kommun – Installation eller ändring av vatten och avlopp", U_SOL_VA),
    ("Sollentuna kommun – Ändring av bärande konstruktion", U_SOL_BAR),
    ("Sollentuna kommun – Översiktsplan med sikte på 2040 (pdf)", U_SOL_OP),
    ("Sollentuna kommun – Kulturhistoriska byggnader och områden", U_SOL_KM),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Planerar du ett nytt kök i Sollentuna?", "Boka ett gratis platsbesök, så går vi igenom stam, fläkt och väggar."),
  "img": [
    ("Nyrenoverat kök med vita luckor och mörk bänkskiva i ett radhus i Sollentuna",
     "newly renovated kitchen in a Swedish 1970s terraced house, white handleless cabinets, dark grey "
     "worktop, oak floor, window with view of a quiet residential street and birch trees, daylight, "
     "no people, no text"),
    ("Kök under montering med nya skåpstommar och förberedda anslutningar",
     "Swedish kitchen under installation, new white cabinet carcasses mounted on the wall, no worktop yet, "
     "water and drain connections prepared under the window, electrical outlets, tools on the floor, "
     "daylight, no people, no text"),
  ],
  "related": [],
},

# =============================== KÖK JÄRFÄLLA ===============================
"koksrenovering-jarfalla.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Järfälla", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Järfälla – kedjehus, radhus och souterräng",
  "description": "Köksrenovering i Järfälla: serietillverkade radhus och kedjehus i Jakobsberg, Kallhäll och "
                 "Skogstorp, bärande väggar, avfallskvarn och papper att spara.",
  "h1": "Köksrenovering i Järfälla",
  "lead": "Järfällas småhus byggdes ofta i serier av samma byggfirma, och köket ligger därför på samma plats i "
          "många hus i området. Det gör planeringen enklare, men bärande väggar, avlopp och ventilation måste "
          "ändå bedömas i varje hus. Vi kommer ut gratis, går igenom köket och lämnar ett skriftligt "
          "kostnadsförslag.",
  "card": "Kedjehus, radhus och souterräng.",
  "sections": [
    {"id": "husen", "anchor": "Husen i Järfälla",
     "h2": "Kök byggda i serie – Kallhäll och Jakobsberg",
     "paras": [
       "Kommunens " + X.format(U_JAR_KAL, "kulturmiljöplan för Kallhäll") + " beskriver hur Bolinders lät "
       "bygga radhus för sina anställda längs Bolindervägen från 1945, och intill dem egnahemsvillor i "
       "Skogstorp. Ett kök som planerades för 1940-talets hushåll har sällan plats för det man vill ha "
       "i dag, och frågan blir ofta om ytan kan lånas från ett angränsande rum.",
       "I " + X.format(U_JAR_JAK, "planen för Jakobsberg") + " beskrivs Ekedal, som började byggas 1958 med "
       "radhuslängor längre ned och villor högre upp, och kedjehusen vid Dressyrvägen. Grändvillorna vid "
       "Hovvägen, byggda i souterräng, kom omkring 1960. Gemensamt är att ett kök sällan är unikt i sitt område – "
       "grannen har ofta samma mått och samma installationer.",
       "Det gör att erfarenheter från ett hus ofta går att använda i nästa, till exempel var stammen går. "
       "Men husen har byggts om på olika sätt genom åren, så varje kök bedöms för sig. I många hus har "
       "köket redan bytts en gång, och då kan nya ledningar ligga ovanpå gamla eller skåp ha flyttats utan "
       "att eluttagen följt med.",
     ],
     "aside": {"title": "Vanliga hus i Järfälla", "items": [
       "Bolinderbyn: radhus från 1945",
       "Ekedal: radhus och villor från 1958",
       "Dressyrvägen: kedjehus",
       "Hovvägen: souterrängvillor från omkring 1960"]}},
    {"id": "souterrang",
     "h2": "Souterränghus och kök på två plan",
     "paras": [
       "I Ekedal finns souterrängradhus, där huset ligger i en slänt och har ett plan delvis under mark. Står "
       "köket på entréplanet går stammen ned genom det nedre planet. Ska köket flyttas eller få "
       "en köksö behöver fallet på avloppet räknas ut, och ibland är det enklare att flytta diskmaskin och "
       "diskbänk tillsammans till en vägg där stammen redan finns.",
       "Väggarna mellan kök och vardagsrum kan bära bjälklaget i hus med två plan. Järfälla kommun skriver på "
       "sidan om " + X.format(U_JAR_BAR, "bärande konstruktion") + " att ritningar visar husets principiella "
       "konstruktion, men att de kan vara ofullständiga och att det inte är säkert att de som byggde följde "
       "dem. Kommunen kan inte bedöma väggen åt dig och hänvisar till en konstruktör.",
       "Påverkas den bärande konstruktionen krävs anmälan och startbesked med planritning, konstruktionsritning "
       "från en sakkunnig konstruktör och förslag till kontrollplan. När handlingarna är kompletta räknar "
       "kommunen med beslut inom fyra veckor.",
     ],
     "aside": None},
    {"id": "avfallskvarn",
     "h2": "Avfallskvarn och fett i Järfällas avlopp",
     "paras": [
       "Huvudman för den allmänna VA-anläggningen i Järfälla är kommunen själv. Enligt "
       + X.format(U_JAR_ABVA, "kommunens allmänna bestämmelser för vatten och avlopp (ABVA)") + " får "
       "spillvatten från en matavfallskvarn inte släppas till avloppet utan huvudmannens skriftliga "
       "medgivande. Vill du ha en avfallskvarn i det nya köket behöver medgivandet alltså finnas innan den "
       "installeras.",
       "Samma bestämmelser säger att fett i större mängd inte får tillföras avloppet. I ett vanligt hushåll "
       "handlar det om att torka ur stekpannor och kasta fettet i soporna i stället för att spola ned det.",
       "Ska ledningarna i köket ändras väsentligt, eller en ny anläggning installeras, krävs anmälan och "
       "startbesked. Det gäller även om resten av renoveringen är lovfri. Badrummet är ofta kopplat till "
       "samma stam, se " + L.format("badrumsrenovering-jarfalla.html", "badrumsrenovering i Järfälla") + ".",
     ],
     "aside": {"title": "Före beställningen", "items": [
       "Avfallskvarn: skriftligt medgivande först",
       "Ny avloppsdragning: kan kräva anmälan",
       "Bärande vägg: konstruktör och startbesked"]}},
    {"id": "dokumentera",
     "h2": "Lovfritt betyder att du själv sparar papperen",
     "paras": [
       "Sedan den 1 december 2025 är fler åtgärder bygglovsbefriade. Järfälla kommun påpekar på sidan om "
       + X.format(U_JAR_BEF, "bygglovsbefriade åtgärder") + " att sådana åtgärder ändå ska följa Boverkets "
       "byggregler och kan kräva anmälan, till exempel vid väsentliga ändringar av bärande konstruktion, "
       "vatten, avlopp och ventilation.",
       "Kommunen råder också fastighetsägare att dokumentera hur reglerna uppfylls och spara dokument och "
       "ritningar, eftersom handlingar för bygglovsbefriade åtgärder inte längre arkiveras hos kommunen. Det "
       "är värt att tänka på även i köket: en ritning över nya ledningar och en anteckning om var väggen "
       "öppnats är bra att ha när huset en dag ska säljas.",
       "Be därför om ritningar och handlingar när köket är klart och spara dem med husets papper. Ska fasaden eller fönstren "
       "målas om i samband med en tillbyggnad, se " + L.format("malare-jarfalla.html", "målare i Järfälla") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi ett kök i Järfälla",
  "steps": [
    ("Besök på plats", "Vi mäter upp köket och ser hur stam, frånluft och väggar är placerade."),
    ("Konstruktion och VA", "Konstruktören bedömer väggar som ska öppnas, och vi stämmer av avloppets fall."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag där arbete och material står var för sig."),
    ("Anmälan vid behov", "Anmälan lämnas in, och arbetet börjar när startbeskedet har kommit."),
    ("Bygge och montering", "Rivning, installationer, ytskikt och montering görs i en planerad ordning."),
    ("Överlämning", "Vi provar vitvaror och belysning och lämnar över ritningar och handlingar."),
  ],
  "rot_h2": "ROT-avdrag för köket i Järfälla",
  "rot": [
    "Skatteverket räknar det som rotarbete i ett småhus att riva väggar och bygga om planlösningen, att montera "
    "fast köksinredning och installera vitvaror vid en omfattande renovering och att installera avlopp och "
    "ventilation. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst "
    "75 000 kr tillsammans med rut.",
    "Bortforsling av gammal inredning ger inte rotavdrag. Avdraget dras direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på ett kök i Järfälla?",
  "price": [
    "Om köket kan ligga kvar där stammen går, om en vägg i ett hus med två plan ska öppnas och om avloppet "
    "behöver dras om med rätt fall. Därefter styr stomme, bänkskiva och vitvaror. Platsbesöket är gratis och "
    "kostnadsförslaget skriftligt.",
  ],
  "faq": [
    ("Får vi installera en avfallskvarn i köket i Järfälla?",
     "Bara med kommunens skriftliga medgivande som huvudman för VA-anläggningen. Ansök innan kvarnen köps "
     "och installeras."),
    ("Kan Järfälla kommun säga om väggen i vårt radhus är bärande?",
     "Nej, kommunen skriver att den inte kan göra den bedömningen och hänvisar till en konstruktör."),
    ("Hur snabbt får vi startbesked för att öppna en bärande vägg i Järfälla?",
     "Kommunen räknar med beslut inom fyra veckor från att alla handlingar har kommit in."),
    ("Varför ska vi spara ritningarna över det nya köket själva?",
     "Järfälla kommun påpekar att handlingar för bygglovsbefriade åtgärder inte längre arkiveras hos kommunen. "
     "Ritningar över ledningar och väggar är bra att ha vid en framtida försäljning."),
    ("Kan köket i ett souterränghus i Ekedal flyttas till andra planet?",
     "Det går, men avloppet behöver tillräckligt fall till stammen, och ändras ledningarna väsentligt krävs "
     "anmälan. Ofta är det enklare att flytta köket på samma plan."),
  ],
  "sources": [
    ("Järfälla kommun – Ändra i bärande konstruktion", U_JAR_BAR),
    ("Järfälla kommun – Bygglovsbefriade åtgärder", U_JAR_BEF),
    ("Järfälla kommun – ABVA, allmänna bestämmelser för vatten och avlopp (pdf)", U_JAR_ABVA),
    ("Järfälla kommun – Kulturmiljöplan, Jakobsberg (pdf)", U_JAR_JAK),
    ("Järfälla kommun – Kulturmiljöplan, Kallhäll (pdf)", U_JAR_KAL),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Järfälla bytas?", "Boka ett gratis besök, så går vi igenom stam, väggar och planlösning."),
  "img": [
    ("Renoverat kök med gröna luckor och träbänkskiva i ett kedjehus i Järfälla",
     "renovated kitchen in a Swedish 1960s link house, sage green shaker cabinets, oak worktop, white tiled "
     "splashback, window over the sink facing a small lawn, pendant lamp, daylight, no people, no text"),
    ("Nytt avlopp och vattenledningar förberedda för en köksö",
     "Swedish house kitchen under renovation, new grey plastic drain pipe and water pipes coming up through "
     "a newly opened floor where a kitchen island will stand, subfloor visible, daylight, no people, no text"),
  ],
  "related": [],
},

# =============================== KÖK HANINGE ===============================
"koksrenovering-haninge.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Haninge", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Haninge – egnahem, grupphus och Dalarö",
  "description": "Köksrenovering i Haninge: egnahem i Tungelsta, rekordårens grupphus och sommarvillor på "
                 "Dalarö. Anmälan om VA-arbete, ventilation och bärande vägg.",
  "h1": "Köksrenovering i Haninge",
  "lead": "Haninges småhus kommer från tre epoker: egnahemmen, folkhemmet och rekordåren. Varje epok har sitt "
          "eget kök, och på Dalarö finns dessutom sommarvillor från 1800-talets slut. Vi utgår från huset, "
          "samordnar snickeri, el och VVS och börjar med ett gratis platsbesök och ett skriftligt "
          "kostnadsförslag.",
  "card": "Egnahem, grupphus och Dalarö.",
  "sections": [
    {"id": "epokerna", "anchor": "Husen i Haninge",
     "h2": "Egnahem, folkhem och rekordår – tre slags kök",
     "paras": [
       "Haninge kommun delar i " + X.format(U_HAN_KAR, "Haninges karaktärsmiljöer") + " in småhusen i tre "
       "epoker. Egnahemsområdena från 1910–1940-talen finns i bland annat Tungelsta, Vendelsö, Handen och "
       "Västerhaninge. I ett hus som är hundra år gammalt har köket i regel byggts om flera gånger, och "
       "det är vanligt att en vägg redan har flyttats eller tagits bort.",
       "Folkhemmets villor, kedjehus och radhus från 1940–1960-talen finns i Handen, Jordbro, Vendelsö och "
       "Västerhaninge. Rekordårens småhus från 1960–1980-talen ligger ofta i grupphusområden i Jordbro, "
       "Brandbergen, Västerhaninge och Handen, där många hus har samma planlösning och därmed samma "
       "läge för kök och stam.",
       "Karaktärsmiljöerna gäller som råd för alla småhusområden från respektive epok. Inne i köket påverkar "
       "det sällan något, men ett nytt fönster eller en fläkthuv på fasaden ska passa husets karaktär.",
     ],
     "aside": {"title": "Kök efter epok", "items": [
       "1910–40-tal: egnahem, ombyggda i omgångar",
       "1940–60-tal: villor, kedjehus och radhus",
       "1960–80-tal: grupphus med samma planlösning",
       "Dalarö: sommarvillor från 1880–90-talen"]}},
    {"id": "va-anmalan",
     "h2": "Haninge Vatten och avlopp vill ha en anmälan",
     "paras": [
       "I Haninge är det kommunens enhet för vatten och avlopp som tar emot anmälningar om VA-arbeten. "
       "Kommunen skriver på sidan om " + X.format(U_HAN_VA, "anmälan om vatten- och avloppsarbete") + " att "
       "den som ska installera eller ändra anordningar för vattenförsörjning eller avlopp i huset eller på "
       "tomten ska anmäla det. Det görs på en blankett som skickas med e-post eller post eller lämnas på "
       "kontoret i Handen.",
       "Enheten har ingen information om hur ledningarna är dragna innanför fastighetsgränsen. Det är alltså "
       "upp till fastighetsägaren att ta reda på var ledningarna går, och i ett äldre egnahem kan avloppet "
       "behöva filmas innan köket ritas.",
       "Ska diskbänken stå kvar där den står räcker oftast en ny anslutning. Ska den till en köksö blir det en "
       "ny dragning, och då hör anmälan till planeringen.",
       "I egnahemmen från 1910–40-talen kan avloppet vara draget i flera omgångar, med delar från olika "
       "decennier. Ligger huset i ett område där det kommunala nätet byggts ut senare kan köket ha kopplats "
       "om utan att de gamla ledningarna tagits bort. Det är sådant som syns först när golvet öppnas, och "
       "därför räknar vi med en kontroll av ledningarna innan inredningen beställs.",
     ],
     "aside": None},
    {"id": "flakt-vagg",
     "h2": "Ventilation och bärande väggar enligt kommunen",
     "paras": [
       "För " + X.format(U_HAN_VENT, "ventilation") + " kräver Haninge kommun anmälan och startbesked när ett "
       "nytt system installeras eller det befintliga ändras i större omfattning, till exempel när aggregat "
       "eller kanaler byts. Går installationen genom brandcellsgränser behövs brandskyddsdokumentation, och "
       "påverkas fasaden kan det krävas bygglov.",
       "Att ändra något som påverkar husets " + X.format(U_HAN_BAR, "bärande delar") + " kräver också anmälan. "
       "Kommunen påpekar att ritningar över de bärande delarna ibland finns i bygglovsarkivet, och att man "
       "ska kontakta en konstruktör om man är osäker. Planritningen ska visa läget före och efter ändringen, "
       "gärna i skala 1:100.",
       "Kräver bygget bygglov kan kommunen pröva de delar som ska anmälas samtidigt, så att bara en ansökan "
       "behövs. Det är praktiskt om köket görs om i samband med en tillbyggnad.",
     ],
     "aside": {"title": "Anmälan i Haninge", "items": [
       "VA-arbete: blankett till Vatten och avlopp",
       "Ventilation: anmälan och startbesked",
       "Bärande vägg: anmälan och konstruktör",
       "Startbesked före start, slutbesked före användning"]}},
    {"id": "dalaro",
     "h2": "Kök i en sommarvilla på Dalarö",
     "paras": [
       "Dalarö blev en exklusiv bad- och sommarort från 1860-talet, och under 1880–90-talen byggdes ett stort "
       "antal sommarvillor, enligt en " + X.format(U_HAN_DAL, "antikvarisk förundersökning") + " för kommunen. "
       "Orten är riksintresse för kulturmiljövården, och flera fastigheter har egna detaljplaner med "
       "varierande bestämmelser.",
       "I en sommarvilla som används året runt kan köket ha flyttats in i ett rum som från början hade en "
       "annan funktion. Snickerier, dörrar och fönster är ofta värda att bevara, och en ny fläktkanal bör "
       "dras invändigt eller genom taket snarare än genom en synlig fasad.",
       "Vi kontrollerar planen för just din fastighet innan något som syns utifrån ändras. Takgenomföringen "
       "samordnar vi med taket, se " + L.format("takrenovering-haninge.html", "takrenovering i Haninge") + ", och "
       "ytskikt inomhus med " + L.format("malare-haninge.html", "målare i Haninge") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går köksrenoveringen till i Haninge",
  "steps": [
    ("Besök och inventering", "Vi tittar på köket, väggarna och ventilationen och tar reda på hur avloppet går."),
    ("Underlag", "Ritningar hämtas ur arkivet, och vid behov anlitas konstruktör eller filmas avloppet."),
    ("Kostnadsförslag och anmälan", "Du får ett skriftligt förslag, och anmälningar skickas in innan arbetet börjar."),
    ("Rivning", "Gammal inredning rivs, och väggar och golv förbereds för de nya installationerna."),
    ("Installationer och montering", "El, vatten, avlopp och fläkt dras, och stomme och bänkskiva monteras."),
    ("Avslut", "Vi provar allt, städar och går igenom köket med dig."),
  ],
  "rot_h2": "Rotavdrag för köket i Haninge",
  "rot": [
    "Enligt Skatteverket ger det rotavdrag i småhus att montera fast köksinredning och installera vitvaror i "
    "samband med en omfattande renovering, att sätta kakel, att modernisera elen och byta vägguttag och att "
    "installera blandare och kranar. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person "
    "och år och 75 000 kr tillsammans med rut.",
    "Material och resor ger inget avdrag. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Haninge?",
  "price": [
    "Om köket stannar kvar på samma plats, hur avloppet är draget i dag, om en vägg ska öppnas och om "
    "ventilationen behöver göras om. I en äldre villa kan även snickerier som ska bevaras påverka. Du får ett "
    "skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Var anmäler vi ändrat köksavlopp i Haninge?",
     "Till kommunens enhet för vatten och avlopp, på en blankett som skickas med e-post eller post eller "
     "lämnas på kontoret i Handen."),
    ("Vet Haninge kommun hur avloppet går på vår tomt?",
     "Nej. Kommunen har ingen information om ledningar innanför fastighetsgränsen, så det får utredas på plats."),
    ("Behövs brandskyddsdokumentation när köksfläkten byts i Haninge?",
     "Bara om installationen går genom brandcellsgränser. Ett nytt ventilationssystem eller en större ändring "
     "kräver ändå anmälan."),
    ("Kan anmälan för köket prövas tillsammans med bygglovet för en tillbyggnad?",
     "Ja, Haninge kommun kan pröva de anmälningspliktiga delarna i samma ärende som bygglovet."),
    ("Vad ska vi tänka på med köket i en sommarvilla på Dalarö?",
     "Dalarö är riksintresse för kulturmiljövården och många fastigheter har egna planbestämmelser. Kontrollera "
     "planen innan något som syns utifrån ändras."),
  ],
  "sources": [
    ("Haninge kommun – Anmälan om vatten- och avloppsarbete", U_HAN_VA),
    ("Haninge kommun – Ventilation", U_HAN_VENT),
    ("Haninge kommun – Ändring av bärande konstruktion", U_HAN_BAR),
    ("Haninge kommun – Haninges karaktärsmiljöer (pdf)", U_HAN_KAR),
    ("Haninge kommun – Antikvarisk förundersökning, Dalarö 3:4 Hotell Bellevue (pdf)", U_HAN_DAL),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Dags för nytt kök i Haninge?", "Boka ett gratis platsbesök, så går vi igenom avlopp, fläkt och väggar."),
  "img": [
    ("Renoverat kök med vita spegelluckor i ett äldre egnahem i Haninge",
     "renovated kitchen in a 1930s Swedish wooden owner-built house, white framed cabinet doors, light "
     "wooden worktop, old wooden floorboards, small paned window with view of a garden, simple pendant "
     "lamp, daylight, no people, no text"),
    ("Köksö med barstolar och öppna hyllor",
     "Swedish kitchen renovation detail, new round galvanised exhaust duct above the planned cooker position, "
     "new electrical boxes in a freshly plastered wall, no cabinets yet, daylight, no people, no text"),
  ],
  "related": [],
},

# =============================== KÖK TYRESÖ ===============================
"koksrenovering-tyreso.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Tyresö", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Tyresö – stugor som blir helårshus",
  "description": "Köksrenovering i Tyresö: omvandlingsområden på Brevikshalvön och i Raksta, anslutning till "
                 "kommunalt VA, tillbyggnad och anmälan efter 1 december 2025.",
  "h1": "Köksrenovering i Tyresö",
  "lead": "I östra Tyresö har många fritidshus blivit helårsbostäder, och när det kommunala vattnet och "
          "avloppet byggs ut blir köket ofta det första som görs om. Ett kök i en ombyggd stuga kräver annat "
          "förarbete än i en villa i Trollbäcken. Vi börjar med ett gratis platsbesök och ett skriftligt "
          "kostnadsförslag och samordnar snickeri, el och VVS.",
  "card": "Stugor som blir helårshus.",
  "sections": [
    {"id": "omvandling", "anchor": "Husen i Tyresö",
     "h2": "Från godsmark och sommarstugor till villor",
     "paras": [
       "Enligt ett " + X.format(U_TYR_SLM, "kulturmiljöunderlag från Stockholms läns museum") + " började "
       "Tyresögodsets mark säljas efter 1930, och vid slutet av 1950-talet hade nästan hälften av godset "
       "exploaterats för fritidshus. Solberga fick byggnadsplan 1952, och i Raksta började tomtförsäljningen "
       "efter en plan 1958. Underlaget konstaterar att permanentningen pågår och att en del hus är helt "
       "ombyggda.",
       "På Brevikshalvön styckades stora arealer för fritidshus under 1930–50-talen, och kommunen har beslutat "
       "att bejaka omvandlingen till helårsboende. " + X.format(U_TYR_FAS, "Detaljplanen för Fasanvägen etapp 13") +
       " omfattar till exempel 119 bostadsfastigheter.",
       "För köket betyder det att utgångsläget varierar kraftigt. I en stuga kan köket vara en enkel vägg med "
       "diskbänk och en kanal som inte var tänkt för en kraftig fläkt, medan en villa i Trollbäcken har ett "
       "kök från en senare ombyggnad.",
     ],
     "aside": {"title": "Före besöket", "items": [
       "Har fastigheten kommunalt VA i dag?",
       "Är huset tillbyggt, och i så fall när?",
       "Var går frånluften från köket?",
       "Planeras en större tillbyggnad?"]}},
    {"id": "va-anslutning",
     "h2": "När det kommunala avloppet kommer",
     "paras": [
       "Tyresö kommun beskriver på sidan om " + X.format(U_TYR_VA, "VA-anslutning") + " stegen för att ansluta "
       "sig till det kommunala ledningsnätet: anmälan och startbesked, en anvisningspunkt, anläggningsavgift, "
       "vattenmätare, anslutning och slutbesked. Till anmälan ska en situationsplan som visar ledningsdragningen "
       "på tomten och ett förslag till kontrollplan bifogas.",
       "Den som har enskilt avlopp med slamtömning och kopplar över till det kommunala nätet ska meddela "
       "kommunens avfallsenhet, så att en sluttömning kan göras. Den gamla anläggningen ska alltså inte bara "
       "lämnas kvar.",
       "Att lägga om köket samtidigt som huset ansluts är ofta klokt. Då kan nya ledningar dras inne i huset "
       "till den plats där diskbänken ska stå, i stället för att den gamla dragningen förlängs. Badrummet "
       "påverkas i regel av samma omläggning.",
       "Kommunen anvisar var fastigheten ska anslutas, och anslutningen får göras först när kommunen meddelat "
       "att punkten är klar. Därför planerar vi köket så att rivning och nya ledningar inne i huset kan göras "
       "i god tid, medan själva inkopplingen mot den kommunala ledningen väntar tills beskedet har kommit.",
     ],
     "aside": {"title": "Stegen vid VA-anslutning", "items": [
       "Anmälan och startbesked", "Anvisningspunkt och avgift", "Vattenmätare",
       "Anslutning och slutbesked", "Sluttömning av gammal tank"]}},
    {"id": "tillbyggnad",
     "h2": "Köket i en tillbyggnad",
     "paras": [
       "Många som permanentar ett fritidshus bygger till, och då hamnar köket ofta i den nya delen. Tyresö "
       "kommun skriver på sidan om " + X.format(U_TYR_PBL, "ändringarna i PBL") + " att en tillbyggnad på mer "
       "än sammantaget 30 kvadratmeter kräver bygglov, och att tidigare lovbefriade tillbyggnader och skärmtak "
       "räknas in.",
       "Även när tillbyggnaden är lovfri kan den kräva anmälan och startbesked, till exempel om husets "
       "konstruktion berörs. Det blir ofta fallet när en yttervägg öppnas för att koppla ihop det gamla köket "
       "med den nya delen. Kommunen skriver också att den inte längre granskar många åtgärder som tidigare "
       "krävde lov, så fastighetsägaren måste själv se till att reglerna följs.",
       "Fönster, panel och förstukvist hör till samma ombyggnad, se " + L.format("snickare-tyreso.html", "snickare i Tyresö") +
       ". Ska taket byggas ihop över gammal och ny del, se " + L.format("takrenovering-tyreso.html", "takrenovering i Tyresö") + ".",
     ],
     "aside": None},
    {"id": "flakt",
     "h2": "Köksfläkten i en stuga med tunna väggar",
     "paras": [
       "En stuga byggd för sommarbruk har ofta självdrag eller ingen ordnad ventilation alls. När huset blir "
       "tätare och värms året runt behöver köket en fungerande frånluft, och en fläkt som kopplas till en "
       "gammal kanal kan ändra flödena i hela huset.",
       "Ett nytt ventilationssystem eller en större ändring av det gamla kräver anmälan. En kanal genom taket "
       "är ofta bättre än genom väggen, eftersom fläkthuven då inte syns på fasaden. I områden som är "
       "kulturhistoriskt särskilt värdefulla krävs dessutom bygglov för ändringar som påverkar det yttre.",
       "Tänk också på luften som ska ersätta den som fläkten suger ut. I ett tätare hus behövs uteluftsdon "
       "eller ett system med tilluft, annars fungerar fläkten sämre. "
       "Väggar och tak inne i den gamla delen kan vara klädda med träpanel som är värd att behålla. Ska de "
       "målas om efter renoveringen, se " + L.format("malare-tyreso.html", "målare i Tyresö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett nytt kök till i Tyresö",
  "steps": [
    ("Platsbesök", "Vi ser hur huset är byggt, var ledningarna går och om köket ska ligga kvar eller flyttas."),
    ("VA och tillbyggnad", "Vi stämmer av hur köket passar ihop med VA-anslutningen och en eventuell tillbyggnad."),
    ("Kostnadsförslag", "Du får ett skriftligt förslag med rivning, installationer och montering var för sig."),
    ("Anmälan", "Anmälan och handlingar lämnas in, och arbetet börjar efter startbesked."),
    ("Bygge", "Ledningar dras, väggar och golv byggs upp och köket monteras."),
    ("Slutbesked och genomgång", "Vi provar installationerna, städar och går igenom köket med dig."),
  ],
  "rot_h2": "ROT-avdrag för köksrenovering i Tyresö",
  "rot": [
    "Ett fritidshus räknas som småhus hos Skatteverket, men huset ska användas som bostad. Godkänt rotarbete "
    "är bland annat att montera fast köksinredning och installera vitvaror vid en omfattande renovering, att "
    "riva väggar och ändra planlösningen och att installera avlopp. Avdraget är 30 procent av "
    "arbetskostnaden, högst 50 000 kr per person och år och 75 000 kr ihop med rut.",
    "Avdraget gäller bara arbetskostnaden, inte material. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden i Tyresö?",
  "price": [
    "Hur mycket av huset som byggs om samtidigt, om köket flyttar till en tillbyggnad, hur ledningarna ska "
    "dras till den nya anslutningspunkten och om ventilationen måste göras om. Efter ett gratis platsbesök "
    "får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Vad ska vi göra med den gamla slamtanken när huset i Tyresö ansluts till kommunalt avlopp?",
     "Meddela kommunens avfallsenhet att ni kopplar över, så att en sluttömning kan göras."),
    ("Kan köket göras om samtidigt som fastigheten ansluts till kommunalt VA?",
     "Ja, och det är ofta praktiskt. Nya ledningar kan då dras direkt till den plats där diskbänken ska stå."),
    ("Kräver en köksutbyggnad på stugan bygglov i Tyresö?",
     "Över 30 kvadratmeter sammantaget krävs bygglov, och tidigare lovfria tillbyggnader räknas in. Berörs "
     "konstruktionen kan även en mindre tillbyggnad kräva anmälan."),
    ("Ger köksrenovering i ett fritidshus rotavdrag?",
     "Ja, om huset används som bostad. Skatteverket räknar fritidshus som småhus."),
    ("Vad ska bifogas när vi anmäler VA-anslutningen i Tyresö?",
     "En situationsplan som visar ledningarna på tomten och ett förslag till kontrollplan, enligt kommunen."),
  ],
  "sources": [
    ("Tyresö kommun – VA-anslutning", U_TYR_VA),
    ("Tyresö kommun – Förändringar i plan- och bygglagen från 1 december 2025", U_TYR_PBL),
    ("Stockholms läns museum – Solberga/del av Raksta, kulturmiljöunderlag (2008:31)", U_TYR_SLM),
    ("Tyresö kommun – Planbeskrivning, Fasanvägen etapp 13 (pdf)", U_TYR_FAS),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i Tyresö göras om?", "Boka ett gratis platsbesök, så planerar vi köket efter huset och VA-anslutningen."),
  "img": [
    ("Nytt kök med vita luckor och träpanel i ett ombyggt fritidshus i Tyresö",
     "new kitchen in a converted Swedish 1950s summer cottage, white cabinets, light birch worktop, "
     "painted wooden panel walls, window with view of pine trees and granite rocks, wooden floor, daylight, "
     "no people, no text"),
    ("Nya vatten- och avloppsledningar dragna i golvet i en tillbyggnad",
     "new extension of a Swedish wooden house under construction, new insulated water pipes and grey drain "
     "pipes laid in the floor joists where a kitchen will be, plywood subfloor partly laid, daylight, "
     "no people, no text"),
  ],
  "related": [],
},

# =============================== KÖK VÄRMDÖ ===============================
"koksrenovering-varmdo.html": {
  "kind": "district", "service": "koksrenovering", "ort": "Värmdö", "svc_label": "Köksrenovering",
  "title": "Köksrenovering på Värmdö – eget avlopp och helårshus",
  "description": "Köksrenovering på Värmdö: kök i fritidshus som blir helårshus, eget BDT-avlopp, kommunalt "
                 "VA i förändringsområdena och bruksbebyggelsen i Gustavsberg.",
  "h1": "Köksrenovering på Värmdö",
  "lead": "På Värmdö har många kök byggts för sommarbruk och ska nu fungera året runt. Diskvattnet går ofta "
          "till en egen avloppsanläggning, och i flera områden är kommunalt vatten och avlopp på väg. Vi "
          "planerar köket efter de förutsättningarna, samordnar snickeri, el och VVS och börjar med ett gratis "
          "platsbesök och ett skriftligt kostnadsförslag.",
  "card": "Fritidshus, eget avlopp och Gustavsberg.",
  "sections": [
    {"id": "fritidshus", "anchor": "Husen på Värmdö",
     "h2": "Sommarkök som ska klara vintern",
     "paras": [
       "Värmdö kommun har tusentals fastigheter i fritidshusområden där allt fler bor permanent, enligt "
       "broschyren " + X.format(U_VAR_PFO, "Fritidshusområde i förändring") + ". De områden som först ska "
       "anpassas för helårsboende kallas prioriterade förändringsområden. De pekas ut i översiktsplanen och "
       "får detaljplan och kommunalt vatten och avlopp.",
       "Ett kök som byggdes för sommaren är ofta enkelt: en diskbänk mot ytterväggen, få eluttag och en "
       "ventil i stället för en fläkt. När huset ska användas hela året behövs fler uttag, en fungerande "
       "frånluft och ledningar som inte fryser. Vattenledningar i en kall yttervägg kan "
       "frysa.",
       "Har huset byggts till i omgångar kan köket ligga i den äldsta och kallaste delen. Då är det ofta "
       "bättre att flytta det till en varmare del än att isolera om den gamla väggen. Var golvet i den "
       "nya delen ligger i förhållande till det gamla avgör också hur avloppet kan dras.",
       "Elen är en annan sak att se över. Ett sommarhus har ofta få grupper i elcentralen, och en modern spis, "
       "ugn, diskmaskin och fläkt kräver mer. Skatteverket räknar det som rotarbete att installera och "
       "komplettera elcentraler, så elen kan moderniseras i samma entreprenad som köket.",
     ],
     "aside": {"title": "Före besöket", "items": [
       "Eget avlopp eller kommunalt VA?",
       "Ligger fastigheten i ett förändringsområde?",
       "Var går vattenledningarna i dag?",
       "Är huset tillbyggt i omgångar?"]}},
    {"id": "eget-avlopp",
     "h2": "Diskvattnet och den egna avloppsanläggningen",
     "paras": [
       "Diskvatten räknas till bad-, disk- och tvättavlopp, BDT. Värmdö kommun skriver på sidan om "
       + X.format(U_VAR_AVL, "ansökan och anmälan för små avlopp") + " att en helt ny avloppsanläggning kräver "
       "tillstånd, oavsett om den är för WC, för WC och BDT eller enbart för BDT, och att man måste invänta "
       "kommunens skriftliga beslut innan arbetet börjar.",
       "Tillstånd krävs också för att ansluta en eller flera byggnader till en befintlig anläggning. Flyttar "
       "köket till ett gästhus eller en ny byggnad på tomten är det alltså inte bara en VVS-fråga. Tillståndet "
       "gäller dessutom för exakt den lösning och placering som prövats.",
       "När ett fritidshus används året runt ökar mängden diskvatten. Är du osäker på om anläggningen räcker, "
       "eller om det du planerar kräver tillstånd eller anmälan, kan du kontakta kommunen innan du ansöker. "
       "Badrummet påverkar samma anläggning, och därför planerar vi gärna båda rummen tillsammans.",
     ],
     "aside": {"title": "Små avlopp på Värmdö", "items": [
       "Ny anläggning: tillstånd",
       "Ny byggnad till befintlig anläggning: tillstånd",
       "Byte av slamavskiljare med samma funktion: varken tillstånd eller anmälan",
       "Vänta på skriftligt beslut"]}},
    {"id": "kommunalt-va",
     "h2": "När förändringsområdet får kommunalt VA",
     "paras": [
       "I de prioriterade förändringsområdena byggs kommunalt vatten och avlopp ut i samband med detaljplanen. "
       "När fastigheten ska kopplas på är det ett bra tillfälle att se över ledningarna inne i huset och lägga "
       "köket där det passar bäst, i stället för där den gamla anläggningen styrde.",
       "Planläggningen innebär ofta också att byggrätterna ses över, och många bygger till eller på. Då kan "
       "köket få plats i den nya delen, och ventilationen kan planeras från början med en kanal genom taket. "
       "Ska taket byggas om över en tillbyggnad, se " + L.format("takrenovering-varmdo.html", "takrenovering på Värmdö") + ".",
       "Kommunen påpekar på sidan om " + X.format(U_VAR_PBL, "ändringarna i PBL") + " att det är fastighetsägaren "
       "som ansvarar för att byggnationen följer lagens krav, även när åtgärden är lovfri.",
     ],
     "aside": None},
    {"id": "gustavsberg",
     "h2": "Kök i Gustavsbergs bruksbebyggelse",
     "paras": [
       "Gustavsberg är riksintresse för kulturmiljövården. En " + X.format(U_VAR_GUS, "antikvarisk konsekvensanalys") +
       " från kommunen beskriver brukssamhället och det mönstersamhälle som Kooperativa Förbundet byggde, och "
       "Grindstugatan med bostadshus från 1870-talet, sadeltak och faluröd fjällpanel med vita knutar.",
       "Värmdö kommun skriver att det gäller lovplikt inom riksintressen för kulturmiljövården och i "
       "kulturhistoriskt värdefulla områden, och kommunens kulturmiljökarta visar vilka fastigheter som berörs. "
       "Inne i köket är det sällan något som prövas, men en fläkthuv på fasaden, ett nytt fönster eller en ny "
       "dörr kan kräva lov.",
       "I de äldre husen kan det finnas snickerier, dörrar och golv som är värda att spara när köket byts. "
       "Ska fasad eller fönster målas om, se " + L.format("malare-varmdo.html", "målare på Värmdö") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så renoverar vi ett kök på Värmdö",
  "steps": [
    ("Besök på plats", "Vi ser över köket, ledningarna, ventilationen och hur avloppet tar hand om diskvattnet."),
    ("Avlopp och lov", "Vi stämmer av om ändringen kräver tillstånd för avloppet eller lov för det som syns utifrån."),
    ("Skriftligt kostnadsförslag", "Du får ett förslag där rivning, installationer och montering står var för sig."),
    ("Rivning och frostsäkring", "Gammal inredning tas bort, och vattenledningar flyttas från kalla väggar."),
    ("Montering", "Stommen sätts upp, bänkskivan mäts in och vitvaror och fläkt installeras."),
    ("Genomgång", "Vi provar allt och går igenom köket tillsammans med dig."),
  ],
  "rot_h2": "Rotavdrag för köket på Värmdö",
  "rot": [
    "Skatteverket räknar ett fritidshus som småhus, men det ska användas som bostad. Rotavdrag ges bland annat "
    "för att montera fast köksinredning och installera vitvaror i samband med en omfattande renovering, att "
    "modernisera elen och byta vägguttag och att installera ventilation och imkanaler. Avdraget är 30 procent "
    "av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr tillsammans med rut.",
    "Material och resor ger inget avdrag. Vi drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden på Värmdö?",
  "price": [
    "Om köket kan ligga kvar, om ledningar måste flyttas från kalla väggar, om avloppet behöver ett nytt "
    "tillstånd och om ventilationen ska göras om. Läge och åtkomst på ön påverkar också. Efter ett gratis "
    "platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behövs tillstånd om köket flyttar till ett gästhus på tomten på Värmdö?",
     "Ja, om gästhuset ska anslutas till den befintliga avloppsanläggningen. Värmdö kommun kräver tillstånd för "
     "att ansluta fler byggnader."),
    ("Räknas diskvattnet som BDT-avlopp?",
     "Ja, BDT står för bad-, disk- och tvättavlopp. En ny anläggning enbart för BDT kräver också tillstånd på "
     "Värmdö."),
    ("Får vi byta slamavskiljaren utan att söka tillstånd?",
     "Ja, enligt kommunen om den nya har likvärdig funktion och placeras på samma ställe."),
    ("Kan vi vänta med köket tills kommunalt VA byggs ut i vårt område?",
     "Det är ofta klokt, eftersom ledningarna i huset ändå ska kopplas om. Då kan köket placeras där det "
     "passar bäst."),
    ("Krävs lov för en ny köksdörr mot trädgården i Gustavsberg?",
     "Ligger huset inom riksintresset eller i ett kulturhistoriskt värdefullt område gäller lovplikt. Kontrollera "
     "kommunens kulturmiljökarta först."),
  ],
  "sources": [
    ("Värmdö kommun – Ansökan och anmälan små avlopp", U_VAR_AVL),
    ("Värmdö kommun – Förändringar i PBL från 1 december 2025", U_VAR_PBL),
    ("Värmdö kommun – Fritidshusområde i förändring, del 1 (pdf)", U_VAR_PFO),
    ("Värmdö kommun – Antikvarisk konsekvensanalys, riksintresset Gustavsberg (pdf)", U_VAR_GUS),
    S_ROT, S_ROTJOB,
  ],
  "cta": ("Ska köket i fritidshuset bli ett helårskök?", "Boka ett gratis platsbesök, så går vi igenom avlopp, el och ventilation."),
  "img": [
    ("Ljust kök med träbänkskiva i ett permanentat fritidshus på Värmdö",
     "bright kitchen in a Swedish archipelago summer house converted for year-round living, white painted "
     "wooden cabinets, oak worktop, wide plank floor, window with view of pine trees and a glimpse of the sea, "
     "daylight, no people, no text"),
    ("Slamavskiljare och avloppsrör på en skärgårdstomt",
     "rocky Swedish archipelago garden with a green plastic septic tank lid and an inspection pipe in the "
     "grass, red wooden house wall in the background, pines, overcast daylight, no people, no text"),
  ],
  "related": [],
},
}
