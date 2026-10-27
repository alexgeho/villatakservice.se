# -*- coding: utf-8 -*-
"""Innerstaden – ortsidor v32 (2026-10-28): takbyte Södermalm, Vasastan, Östermalm; fasadmålning Kungsholmen,
Vasastan; totalrenovering Östermalm. Tre bilder per sida: img[0] hero 4:3, img[1] och img[2] 3:2.
Husen är flerbostadshus som ägs av föreningar eller hyresvärdar – inga villor påstås där de inte finns.
Tak och fasad på ett föreningshus ger inget rotavdrag: egen trust-rad (sidnyckel "trust").

Lokal vinkel per sida:
takbyte-sodermalm – byggställning, container och bodar på gatan (polistillstånd, 1,6/2 meter, bygglov för container
  och bod, tillstand.stockholm); hyresvärdar och föreningar (områdesfakta 2025); nytt takmaterial mot gatan kräver
  bygglov; stenstadens plåttak (riksintresset).
takbyte-vasastan – föreningen som byggherre (Boverket, roller i byggskedet), byggherre kontra beställare,
  kontrollplan och slutbesked; tre församlingsområden i siffror; materialbyte och utökad lovplikt.
takbyte-ostermalm – taksäkerhet: tillträde, förflyttning och skydd mot fall när taket ska beträdas för drift,
  snörasskydd över entréer, anpassning vid ändring (Boverket, BFS 2024:9); stenstadens siluett (riksintresset);
  Hedvig Eleonora i siffror.
fasadmalning-kungsholmen – Kristineberg och Fredhäll (staden köpte marken 1920, tävlingar 1927 och 1929, ljusa
  slätputsade fasader, Stockholms spår); gatufasad mot gårdsfasad och bygglov; Stora Essingens villor.
fasadmalning-vasastan – stenstadens gatufasader (sockelvåning och huvudfasad, enklare gårdsfasader, riksintresset);
  kulör mot gatan och mot gården; Stadsmuseets klassning; föreningarna i siffror.
totalrenovering-ostermalm – bostadsrättslagen 7 kap. 7 § (fem punkter och lägenheter med kulturhistoriska värden),
  planlösning utan anmälan och när anmälan krävs, ritningar som kan vara ofullständiga, självdrag i äldre hus.

Fakta endast från källorna i respektive 'sources', öppnade med Python/urllib (Mozilla-UA) 2026-10-28, alla svarade
200; pdf:erna har textlager. Skatteverket återställde anslutningen – samma URL och formuleringar som v22–v31.
Strukna: avgifter, handläggningstider, namn på enskilda fastigheter och föreningar, påståenden om takmaterial i
enskilda kvarter. Inga priser, garantier, omdömen, egna uppdrag i orterna eller cert.
"""

_L = '<a class="text-link" href="{0}">{1}</a>'
_SFX = ", realistic photo, no people, no hands, no text, no letters"
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"


def _of(namn, path):
    return (f"Stockholms stad – Områdesfakta 2025: {namn} (pdf)", _OF + path + ".pdf")


_TRUST_BRF = ["Gratis besök och kostnadsförslag", "Underlag till föreningens styrelse"]
_SB = "https://bygglov.stockholm/nar-behovs-bygglov/"
_STH_FASAD = ("Stockholms stad – Fasadändring", _SB + "andra-byggnads-yttre-utseende/fasadandring/")
_STH_KLASS = ("Stockholms stad – Stadsmuseets kulturhistoriska klassificering",
              _SB + "andra-byggnads-yttre-utseende/stadsmuseets-kulturhistoriska-klassificering/")
_STH_PLAN = ("Stockholms stad – Ändra planlösningen i en byggnad", _SB + "andra-inomhus/andra-planlosningen-i-en-byggnad/")
_STH_BAR = ("Stockholms stad – Ändra i bärande konstruktion", _SB + "andra-inomhus/andra-i-barande-konstruktion/")
_STH_VENT = ("Stockholms stad – Ventilation", _SB + "andra-inomhus/ventilation/")
_STH_PLATS = ("Stockholms stad – Använda offentlig plats för byggverksamhet",
              "https://tillstand.stockholm/tillstand-regler-och-tillsyn/anvanda-offentlig-plats/anvanda-offentlig-plats-for-byggverksamhet/")
_RIKS = ("Stockholms stad – Översiktsplan: Riksintressen enligt miljöbalken (pdf)",
         "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/oversiktsplan-for-stockholm/riksintresse-ta.pdf")
_VARSAM = ("Stockholms stad – Varsam utveckling av småhus- och villaområden (pdf)",
           "https://vaxer.stockholm/siteassets/stockholm-vaxer/tema/stockholms-arkitektur/varsam-utveckling-ta.pdf")
_BOV_ROLL = ("Boverket – Roller i byggskedet",
             "https://www.boverket.se/sv/energiguiden/energieffektivisera-flerbostadshus/energirenovera/bygga/roller-i-byggskedet/")
_BOV_TAK = ("Boverket – Taksäkerhet (PBL kunskapsbanken)",
            "https://www.boverket.se/sv/PBL-kunskapsbanken/regler-om-byggande/sakerhet-anvandning/taksakerhet/")
_KRISTINEBERG = ("Stockholms stadsmuseum – Stockholms spår: Kristineberg (pdf)",
                 "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_000078.pdf")
_BRL = ("Riksdagen – Bostadsrättslag (1991:614), 7 kap. 7 §",
        "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/")
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")

_ROT_TAK = [
  "Skatteverket ger rotavdrag i en bostadsrätt bara för arbete inne i bostaden som du ansvarar för enligt stadgarna. Arbete på gemensamma delar som tak och fasader ger inget rotavdrag, varken för föreningen eller för de boende.",
  "Ett takbyte på ett flerbostadshus betalas därför av föreningen eller hyresvärden utan avdrag, och kostnadsförslaget ställs till den som äger huset.",
]
_ROT_FASAD = [
  "Rotavdrag ges i en bostadsrätt bara för arbete inne i bostaden som bostadsrättshavaren ansvarar för enligt stadgarna. Fasader och tak är gemensamma delar, och en fasadmålning på ett flerbostadshus ger därför inget avdrag.",
  "Kostnadsförslaget ställs till föreningen eller fastighetsägaren. Äger du en villa gäller andra regler: där kan målning av fasaden ge rotavdrag på arbetskostnaden.",
]

PAGES_TJ = {

# ------------------------------------------------------------------ TAKBYTE SÖDERMALM
"takbyte-sodermalm.html": {
  "kind": "district", "service": "takbyte", "ort": "Södermalm", "svc_label": "Takbyte",
  "title": "Takbyte på Södermalm – ställning, gatan och nytt material",
  "description": "Takbyte på Södermalm: polistillstånd för ställning och container på gatan, bygglov för nytt takmaterial och vem som beställer – förening eller hyresvärd.",
  "h1": "Takbyte på Södermalm",
  "lead": "Att byta taket på ett hus på Södermalm börjar ofta på trottoaren. Ställningen, containern och materialet behöver plats på gatan, och det kräver tillstånd. Geal Entreprenad AB byter tak på flerbostadshus och tar fram underlaget till föreningen eller hyresvärden innan arbetet börjar.",
  "card": "Nytt tak på föreningens eller hyresvärdens hus.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "gatan-sodermalm", "anchor": "Tillstånd på gatan",
     "h2": "Ställningen står på stadens mark",
     "paras": [
       "Stockholms stad skriver att den som behöver använda offentlig plats för byggverksamhet ska söka polistillstånd, och att tillståndet ska vara utfärdat innan platsen tas i bruk. Det gäller bland annat byggställningar, containrar, arbetsbodar, mobilkranar och byggsäckar. På en gata med hus i gatuliv, som i stora delar av Södermalm, står ställningen ofta på trottoaren.",
       "Staden ställer krav på hur ställningen står. Minst 1,6 meter ska vara fritt under den, eller minst 2 meter av gångbanan ska finnas kvar för gående. Behövs plats för ställningsmaterial vid upp- och nedmontering ska den ingå i tillståndet. Vi söker tillståndet i god tid och planerar etableringen så att porten och gångbanan går att använda.",
     ],
     "aside": {"title": "Polistillstånd krävs för", "items": [
       "Byggställningar", "Containrar och byggsäckar", "Arbetsbodar", "Mobilkranar"]}},
    {"id": "container-sodermalm", "h2": "Container och bod kan kräva bygglov",
     "paras": [
       "Utöver polistillståndet skriver staden att bygglov behövs för att uppföra en byggbod, ställa upp en container, anordna upplag för byggmaterial och sätta upp byggplank eller byggskylt. Ett glest byggstängsel kräver däremot inget bygglov.",
       "När det gamla taket rivs ska materialet ner till gatan, och då behövs både container och tillstånd. Vi lägger in tillstånden i tidplanen innan föreningen bestämmer startdatum, så att arbetet inte står still i väntan på ett papper.",
     ],
     "aside": None},
    {"id": "vem-sodermalm", "h2": "Förening eller hyresvärd beställer",
     "paras": [
       "Stadens områdesfakta för 2025 räknar på Södermalm drygt 43 500 bostadsrätter i flerbostadshus, cirka 21 700 lägenheter hos privata hyresvärdar och drygt 8 600 hos allmännyttan. Taket på ett sådant hus är husägarens sak. Det är föreningen eller hyresvärden som beställer ett takbyte, och för de boende är det framför allt en fråga om information och tillträde till vinden.",
       "Boverket beskriver att byggherren, till exempel en bostadsrättsförening, har det yttersta ansvaret för att lov och startbesked finns och att kontrollplanen följs. Vi tar fram underlag till styrelsen eller fastighetsägaren om material, etablering och tider.",
     ],
     "aside": {"title": "Södermalm 2025", "items": [
       "43 542 bostadsrätter i flerbostadshus", "21 740 hos privata hyresvärdar", "8 670 hos allmännyttan", "13 småhus med äganderätt"]}},
    {"id": "material-sodermalm", "h2": "Samma material eller ett nytt",
     "paras": [
       "Stockholms stad räknar byte av kulör eller material på tak som en fasadändring. På ett flerbostadshus krävs bygglov när ändringen görs på ett tak som vetter mot allmän plats. Ligger huset inom ett riksintresse, ett särskilt värdefullt område eller är det blå- eller grönklassat krävs bygglov även för ändringar som annars hade varit lovfria.",
       "Stadens redovisning av riksintressena beskriver den klassiska stenstadens tak som sluttande, oftast plåttäckta och med en lutning upp till 45 grader från fasaden, vilket ger ett karaktäristiskt taklandskap. Byts ett plåttak mot ett nytt plåttak i samma utförande är det underhåll. Vill föreningen byta material eller kulör tar vi fram handlingar för bygglovet.",
     ],
     "aside": None},
    {"id": "eternit-sodermalm", "h2": "Gamla material på gårdshus och detaljer",
     "paras": [
       "Arbetsmiljöverket skriver att man ska räkna med att det finns asbest i hus byggda fram till 1982, bland annat i asbestcementskivor, eternit, för tak och väggar, och i fix och fog. Det gäller inte bara huvudtaket utan också gårdshus, tillbyggnader och detaljer som byggts eller lagats under de åren.",
       "Byggherren ska enligt Arbetsmiljöverket se till att materialen undersöks innan rivning. Hittas asbest i det som ska rivas planeras saneringen av ett företag med tillstånd innan takbytet börjar.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte på Södermalm till",
  "steps": [
    ("Platsbesök", "Gratis besök på vinden och taket tillsammans med föreningen."),
    ("Underlag", "Material, utförande och om bygglov behövs."),
    ("Tillstånd", "Polistillstånd för ställning och etablering på gatan."),
    ("Etablering", "Ställning, väderskydd och container."),
    ("Takbyte", "Gammalt tak rivs, underlag ses över och nytt tak läggs."),
    ("Avslut", "Plåtdetaljer, besiktning och nedmontering."),
  ],
  "rot_h2": "Rotavdrag och föreningens tak",
  "rot": _ROT_TAK,
  "price_h2": "Vad påverkar priset på ett takbyte på Södermalm?",
  "price": [
    "Takets yta och lutning, hur mycket underlag som behöver bytas, plåtdetaljer kring kupor och skorstenar, ställningens storlek och tiden på gatan samt om bygglov behövs. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver vi polistillstånd för ställningen vid takbytet på Södermalm?",
     "Ja, om ställningen står på offentlig plats som trottoaren. Tillståndet ska vara klart innan platsen används."),
    ("Krävs bygglov för containern på gatan?",
     "Ja. Stockholms stad skriver att det krävs bygglov för att ställa upp en container på offentlig plats, utöver polistillståndet."),
    ("Hur mycket av trottoaren måste vara fri under ställningen?",
     "Minst 1,6 meter fritt under ställningen eller minst 2 meter kvar för gående på gångbanan."),
    ("Kan jag som bostadsrättshavare beställa ett nytt tak på vårt hus?",
     "Nej. Taket är en gemensam del av huset, och det är föreningen som beställer och betalar takbytet."),
  ],
  "sources": [_of("Södermalms stadsdelsområde", "inre-staden/sodermalm/sodermalm-stadsdelsomrade"), _STH_PLATS, _STH_FASAD,
              _STH_KLASS, _RIKS, _BOV_ROLL, _SKV],
  "cta": ("Ska föreningens tak bytas på Södermalm?", "Boka ett gratis platsbesök, så går vi igenom tak, tillstånd och etablering innan föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Byggställning med väderskydd mot en gata i stenstaden",
     "scaffolding with white weather protection sheeting covering the facade and roof of a late 1800s plastered apartment building on a narrow street in Stockholm, pavement kept free under the scaffold, overcast day" + _SFX),
    ("Nylagt rött pannat tak på ett flerbostadshus, ställning längs kanten",
     "close view of a newly laid dark grey standing seam metal roof with a small metal-clad dormer on an old Stockholm apartment building, plain unmarked metal sheets, plastered chimneys behind, clear sky" + _SFX),
    ("Container för rivningsmaterial vid trottoarkanten",
     "an empty steel construction skip container placed at the kerb in front of an old apartment building in Stockholm, traffic cones around it, plain unmarked surfaces, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ TAKBYTE VASASTAN
"takbyte-vasastan.html": {
  "kind": "district", "service": "takbyte", "ort": "Vasastan", "svc_label": "Takbyte",
  "title": "Takbyte i Vasastan – föreningen som byggherre",
  "description": "Takbyte i Vasastan: föreningen som byggherre, skillnaden mot beställare, startbesked och slutbesked, nytt material och lov i stenstaden.",
  "h1": "Takbyte i Vasastan",
  "lead": "Nästan alla hus i Vasastan ägs av bostadsrättsföreningar eller hyresvärdar. När taket ska bytas är det föreningen som bär ansvaret enligt plan- och bygglagen, inte entreprenören. Geal Entreprenad AB byter tak på flerbostadshus och hjälper styrelsen att få ordning på handlingarna.",
  "card": "Takbyte för föreningar och fastighetsägare.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "foreningar-vasastan", "anchor": "Föreningarna",
     "h2": "Över 20 000 bostadsrätter",
     "paras": [
       "Stadens områdesfakta för 2025 redovisar Vasastan i församlingsområdena Gustav Vasa, Västra Matteus och Östra Matteus. Tillsammans har de drygt 20 000 bostadsrätter i flerbostadshus, omkring 6 500 lägenheter hos privata hyresvärdar och ungefär 1 200 hos allmännyttan. Småhus finns det nästan inga.",
       "Ett takbyte i Vasastan beställs alltså av en förening eller en hyresvärd. För styrelsen är takbytet ofta det största projektet på många år, och det kommer med en roll som inte alla styrelseledamöter känner till: byggherrens.",
     ],
     "aside": {"title": "Vasastan 2025", "items": [
       "20 264 bostadsrätter", "6 509 hos privata hyresvärdar", "1 201 hos allmännyttan", "Tre församlingsområden"]}},
    {"id": "byggherre-vasastan", "h2": "Föreningen är byggherre",
     "paras": [
       "Boverket beskriver byggherren som den som för egen räkning utför eller låter utföra byggnads- eller rivningsarbeten, och skriver att det kan vara en juridisk person som en bostadsrättsförening. Byggherren har det yttersta ansvaret för att byggnaden uppfyller bestämmelserna och att rätt kompetens finns med.",
       "När en åtgärd kräver lov eller anmälan ska byggherren bland annat se till att arbetet inte börjar före startbesked, att det kontrolleras enligt kontrollplanen och att det inte tas i bruk utan slutbesked. Kräver takbytet inget lov gäller ändå kraven på utformning, tekniska egenskaper, varsamhet och underhåll.",
     ],
     "aside": {"title": "Byggherren ansvarar för", "items": [
       "Inget arbete före startbesked", "Kontroll enligt kontrollplanen", "Ingen användning före slutbesked", "Varsamhet även utan lov"]}},
    {"id": "bestallare-vasastan", "h2": "Beställare i avtalet, byggherre i lagen",
     "paras": [
       "Boverket skiljer på rollerna. Byggherre är ett begrepp i plan- och bygglagen och gäller förhållandet mellan föreningen och samhället. I avtalet med entreprenören kallas föreningen i stället ofta beställare. De offentligrättsliga kraven kan inte förhandlas bort, medan mycket i avtalet går att komma överens om.",
       "För styrelsen betyder det att ansvaret för lov och kontroller ligger kvar hos föreningen även när en entreprenör gör jobbet. Vi tar fram kontrollpunkter och dokumentation för taket, så att styrelsen kan visa vad som är gjort.",
     ],
     "aside": None},
    {"id": "lov-vasastan", "h2": "Nytt material, ny kulör och lovet",
     "paras": [
       "Stockholms stad räknar byte av material eller kulör på taket som en fasadändring, och på ett flerbostadshus krävs bygglov när taket vetter mot allmän plats. Inom ett riksintresse för kulturmiljövården, ett särskilt värdefullt område eller på blå- och grönklassade hus krävs bygglov även för det som annars är lovfritt.",
       "Den klassiska stenstaden från 1870–1930 breder enligt stadens redovisning av riksintressena ut sig över bland annat Norrmalm, där Vasastaden ingår, och kännetecknas av sluttande, oftast plåttäckta tak. Vi slår upp huset i Stadsmuseets klassificeringskarta innan föreningen väljer material.",
     ],
     "aside": None},
    {"id": "vind-vasastan", "h2": "Takbyte och vindsinredning samtidigt",
     "paras": [
       "Stadens redovisning av riksintressena skriver att stenstaden kan fortsätta att utvecklas genom mer begränsade förändringar, som vindsinredningar, och att sådana prövas enligt varsamhetskraven i plan- och bygglagen. Stadsbyggnadskontorets vägledningar för vindsinredningar och balkonger utgör underlag för prövningen.",
       "Funderar föreningen på att inreda vinden är det klokt att bestämma det innan taket byts, eftersom takkupor, takfönster och isolering påverkar hur det nya taket byggs. Ska vinden inte inredas byter vi taket så att det går att göra senare.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte i Vasastan till",
  "steps": [
    ("Platsbesök", "Gratis besök på taket och vinden med styrelsen."),
    ("Roller", "Vem är byggherre, beställare och kontaktperson?"),
    ("Lov", "Klassning, material och om bygglov eller anmälan krävs."),
    ("Etablering", "Ställning och tillstånd för gatan."),
    ("Takbyte", "Rivning, underlag och nytt tak."),
    ("Dokumentation", "Kontroller och underlag till föreningen."),
  ],
  "rot_h2": "Rotavdrag och takbyte i en förening",
  "rot": _ROT_TAK,
  "price_h2": "Vad påverkar priset på ett takbyte i Vasastan?",
  "price": [
    "Takets yta och form, antalet kupor, skorstenar och huvar, underlagets skick, ställningens storlek och om bygglov och handlingar behövs. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Är det vi i styrelsen eller entreprenören som är byggherre vid takbytet?",
     "Föreningen. Boverket skriver att en bostadsrättsförening kan vara byggherre, och byggherren har det yttersta ansvaret enligt plan- och bygglagen."),
    ("Kan föreningen avtala bort ansvaret för lov och kontroller?",
     "Nej. Boverket skriver att de offentligrättsliga kraven inte kan förhandlas bort, även om mycket i avtalet med entreprenören kan."),
    ("Behöver vi bygglov för att byta från plåt till ett annat material?",
     "Ett nytt material på ett tak som vetter mot gatan räknas som fasadändring och kräver bygglov på ett flerbostadshus."),
    ("Hur många bostadsrätter finns det i Vasastan?",
     "Stadens områdesfakta räknar drygt 20 000 bostadsrätter i flerbostadshus i de tre församlingsområdena 2025."),
    ("Får föreningen inreda vinden i samband med takbytet?",
     "Det kan prövas. Stadens redovisning av riksintressena skriver att vindsinredningar i stenstaden prövas enligt varsamhetskraven, med stadsbyggnadskontorets vägledning som underlag."),
  ],
  "sources": [_of("Gustav Vasa", "inre-staden/norra-innerstaden/gustav-vasa"),
              _of("Västra Matteus", "inre-staden/norra-innerstaden/vastra-matteus"),
              _of("Östra Matteus", "inre-staden/norra-innerstaden/ostra-matteus"), _BOV_ROLL, _STH_FASAD, _STH_KLASS, _RIKS, _SKV],
  "cta": ("Står föreningen i Vasastan inför ett takbyte?", "Boka ett gratis platsbesök, så går vi igenom taket och föreningens ansvar innan ni får ett skriftligt kostnadsförslag."),
  "img": [
    ("Plåttak och takkupor på stenhus i ett kvarter",
     "rooftops of late 19th century plastered apartment buildings in a Stockholm city block with dark standing seam metal roofs, dormers and chimneys, seen from a higher roof, clear afternoon" + _SFX),
    ("Långt rött pannat tak på ett flerbostadshus med skorstenar",
     "a closed binder, roof drawings and a calculator on a meeting table in a small association room in an old building, window light" + _SFX),
    ("Ny plåt på ett takfall med snörasskydd",
     "new dark grey standing seam steel roof slope with a snow guard rail along the eaves on an old apartment building, blue sky" + _SFX),
  ],
},

# ------------------------------------------------------------------ TAKBYTE ÖSTERMALM
"takbyte-ostermalm.html": {
  "kind": "district", "service": "takbyte", "ort": "Östermalm", "svc_label": "Takbyte",
  "title": "Takbyte på Östermalm – taksäkerhet och snörasskydd",
  "description": "Takbyte på Östermalm: taksäkerhet för sotare och fastighetsskötare, snörasskydd över entréer, lov för nytt material och stenstadens siluett.",
  "h1": "Takbyte på Östermalm",
  "lead": "När ett tak på Östermalm byts är det också läge att se över hur man tar sig upp och rör sig på det, och hur snö och is hålls kvar över entréerna. Geal Entreprenad AB byter tak på flerbostadshus och tar med taksäkerheten i underlaget till föreningen.",
  "card": "Nytt tak med taksäkerhet och snörasskydd.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "siluett-ostermalm", "anchor": "Stenstaden",
     "h2": "En del av stadens siluett",
     "paras": [
       "Stadens redovisning av riksintressena beskriver stenstadens stora sammanhållna bebyggelsemassa på Norrmalm och Östermalm som grundanslaget i dagens stadssiluett. Husen uppfördes till största delen under 1800-talets senare del. Taken beskrivs som sluttande och oftast plåttäckta.",
       "Stadens områdesfakta för 2025 räknar i Hedvig Eleonora drygt 5 100 bostadsrätter i flerbostadshus och omkring 2 100 lägenheter hos privata hyresvärdar. Ett takbyte på Östermalm beställs alltså i regel av en förening eller en hyresvärd.",
     ],
     "aside": {"title": "Hedvig Eleonora 2025", "items": [
       "5 151 bostadsrätter", "2 072 hos privata hyresvärdar", "67 hos allmännyttan", "11 småhus"]}},
    {"id": "taksakerhet-ostermalm", "h2": "Taksäkerhet för dem som ska upp på taket",
     "paras": [
       "Boverket skriver att reglerna om taksäkerhet ska förebygga att människor faller ner från taket under byggnadens användning och drift. Det ska finnas tillträdesanordningar till taket, fasta anordningar för att förflytta sig på taket och skyddsanordningar mot fall, om det finns ett fast arbetsställe på taket eller taket annars behöver beträdas för byggnadens drift.",
       "På ett stenhus med skorstenar och ventilationshuvar behöver sotare och fastighetsskötare upp. Kraven gäller fullt ut för nya byggnader, och vid en ändring får de enligt Boverket anpassas om det finns skäl. Vi går igenom takstegar, takbryggor och förankringar med föreningen innan det nya taket läggs, eftersom de fästs i samma underlag.",
     ],
     "aside": {"title": "Tre slags anordningar", "items": [
       "Tillträde till taket", "Fasta anordningar för förflyttning", "Skydd mot fall från taket", "När taket behöver beträdas för drift"]}},
    {"id": "snoras-ostermalm", "h2": "Snö och is över entréerna",
     "paras": [
       "Boverket skriver att det vid entréer ska finnas skyddsanordningar på taket mot fallande is och snö när byggnaden är utformad så att det finns särskilda risker. Fasadens höjd, takets lutning och friktionen i takmaterialet kan vara skäl. För att hantera snölasten kan snörasskyddet behöva vara längre än bara sträckan över entrén.",
       "Ett hus i gatuliv med entré mot trottoaren är just den situation reglerna tar sikte på. När plåten byts monterar vi snörasskydd i den nya täckningen i stället för att skruva fast dem i efterhand.",
     ],
     "aside": None},
    {"id": "lov-ostermalm", "h2": "Material, kulör och bygglov",
     "paras": [
       "Stockholms stad räknar byte av material eller kulör på tak som en fasadändring. För ett flerbostadshus krävs bygglov när ändringen görs på ett tak som vetter mot allmän plats. Ligger huset inom ett riksintresse eller i ett område som pekats ut som särskilt värdefullt, eller är det blå- eller grönklassat, krävs bygglov även för det som annars är lovfritt.",
       "Om huset berörs visar Stadsmuseets klassificeringskarta, och staden hänvisar till Stadsmuseet för bedömning när det är oklart. Ska taket läggas om i samma material och utförande handlar det om underhåll, men varsamhetskraven gäller ändå.",
     ],
     "aside": None},
    {"id": "tatt-ostermalm", "h2": "Täta infästningar i det nya taket",
     "paras": [
       "Boverket skriver att regnvatten kan läcka in genom otätheter vid genomföringar, skarvar, ränndalar och infästningar, och att läckage ofta är svårt att lokalisera i efterhand. Bland exemplen nämns otäta infästningar för taksäkerhetsutrustning och räcken, otäta luckor och huvar och genomföringar vid till exempel skorstenar.",
       "När takbryggor, stegar och snörasskydd monteras i samband med takbytet kan infästningarna tätas i samma moment som plåten läggs. Vi går igenom varje genomföring innan taket stängs.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett takbyte på Östermalm till",
  "steps": [
    ("Platsbesök", "Gratis besök på taket med föreningen eller förvaltaren."),
    ("Taksäkerhet", "Stegar, bryggor och förankringar ses över."),
    ("Lov", "Klassning, material och eventuellt bygglov."),
    ("Etablering", "Ställning, väderskydd och tillstånd för gatan."),
    ("Takbyte", "Rivning, underlag, ny plåt och snörasskydd."),
    ("Avslut", "Kontroller och dokumentation till föreningen."),
  ],
  "rot_h2": "Rotavdrag och takbyte på ett föreningshus",
  "rot": _ROT_TAK,
  "price_h2": "Vad påverkar priset på ett takbyte på Östermalm?",
  "price": [
    "Takets yta och höjd, antalet skorstenar och kupor, underlagets skick, taksäkerhet och snörasskydd, ställningen mot gatan och om bygglov behövs. En överblick finns i " + _L.format("vad-kostar-takbyte.html", "vad kostar ett takbyte") + ". Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Måste vi sätta upp nya takbryggor när taket byts på Östermalm?",
     "Kraven på taksäkerhet gäller när taket behöver beträdas för byggnadens drift. Vid en ändring får kraven anpassas om det finns skäl, så vi går igenom behovet med föreningen."),
    ("När krävs snörasskydd över en entré?",
     "När byggnaden är utformad så att det finns särskilda risker för fallande is och snö, till exempel på grund av fasadens höjd, takets lutning eller materialet."),
    ("Krävs bygglov för att byta till en annan kulör på plåttaket?",
     "Ja, på ett flerbostadshus om taket vetter mot allmän plats. Inom riksintresse eller på klassade hus krävs bygglov även i övrigt."),
    ("Hur många småhus finns det i Hedvig Eleonora?",
     "Stadens områdesfakta räknar elva småhus 2025, mot drygt 7 000 lägenheter i flerbostadshus."),
  ],
  "sources": [_of("Hedvig Eleonora", "inre-staden/norra-innerstaden/hedvig-eleonora"), _RIKS, _BOV_TAK, _STH_FASAD, _STH_KLASS, _SKV],
  "cta": ("Ska taket bytas på ert hus på Östermalm?", "Boka ett gratis platsbesök, så går vi igenom tak, taksäkerhet och lov innan föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Plåttak med takbrygga och skorstenar på ett stenhus",
     "dark standing seam metal roof of a late 1800s light plastered Stockholm apartment building with ornate stucco facade, a metal roof walkway leading to plastered chimneys, blue sky, Scandinavian city" + _SFX),
    ("Röda takpannor läggs på läkt på ett flerbostadshus",
     "close view of a steel snow guard rail mounted along the eaves of a metal roof above the arched entrance of an old plastered apartment building, winter light" + _SFX),
    ("Takstege mot en skorsten på ett plåttak",
     "a fixed steel roof ladder and safety hooks on a sloping metal roof leading up to a chimney on an old city building, clear sky" + _SFX),
  ],
},

# ------------------------------------------------------------------ FASADMÅLNING KUNGSHOLMEN
"fasadmalning-kungsholmen.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Kungsholmen", "svc_label": "Fasadmålning",
  "title": "Fasadmålning på Kungsholmen – ljus puts och gårdsfasader",
  "description": "Fasadmålning på Kungsholmen: de ljusa slätputsade husen i Kristineberg och Fredhäll, gata mot gård, bygglov för ny kulör och villorna på Stora Essingen.",
  "h1": "Fasadmålning på Kungsholmen",
  "lead": "Kungsholmen är en stadsdel av flerbostadshus, och en fasadmålning beställs i regel av en förening eller en hyresvärd. Om en ny kulör kräver bygglov beror på vilken fasad det gäller. Geal Entreprenad AB målar fasader och tar fram underlaget till styrelsen eller fastighetsägaren.",
  "card": "Målning av puts och gårdsfasader.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "kristineberg", "anchor": "Kristineberg och Fredhäll",
     "h2": "Ljusa slätputsade fasader i Kristineberg",
     "paras": [
       "Stadsmuseets skrift om Kristineberg berättar att staden köpte Kristineberg och Fredhäll 1920 och att de flesta bostadshusen byggdes under 1930-talet efter stadsplanetävlingar 1927 och 1929. Tjockhus med en bredd på 15–16 meter blev den dominerande hustypen, och efter stadens tävling om billiga bostäder 1932 byggdes de första smalhusen längs Onkel Adams väg.",
       "Skriften beskriver ljusa slätputsade fasader som ett genomgående drag. När ett sådant hus målas om blir kulören en del av en helhet som sträcker sig över hela kvarteret, och det är ett skäl att stämma av kulören mot grannhusen och Stadsmuseets bedömning, inte bara mot det egna huset.",
     ],
     "aside": {"title": "Kristineberg och Fredhäll", "items": [
       "Staden köpte marken 1920", "Tävlingar 1927 och 1929", "Mest 1930-talshus", "Ljus slätputs"]}},
    {"id": "gata-gard-kungsholmen", "h2": "Mot gatan eller mot gården",
     "paras": [
       "Stockholms stad skriver att det för flerbostadshus krävs bygglov när fasadändringen görs på en fasad eller ett tak som vetter mot allmän plats. Byte av kulör räknas som fasadändring. Ändringar mot gården kan göras utan bygglov om vissa förutsättningar är uppfyllda och huset inte omfattas av utökad lovplikt.",
       "För föreningen betyder det att samma kulör på gatufasaden kan målas om utan lov, medan en ny kulör mot gatan kräver bygglov. Ligger huset i ett riksintresse, i ett särskilt värdefullt område eller är blå- eller grönklassat krävs bygglov även mot gården. Vi börjar med att slå upp huset i Stadsmuseets klassificeringskarta.",
     ],
     "aside": {"title": "Bygglov för ny kulör", "items": [
       "Gatufasad på flerbostadshus", "Alla fasader inom riksintresse", "Blå- eller grönklassade hus", "Skyddsbestämmelser i planen"]}},
    {"id": "foreningar-kungsholmen", "h2": "Föreningen beställer målningen",
     "paras": [
       "Stadens områdesfakta för 2025 räknar på Kungsholmen drygt 30 000 bostadsrätter i flerbostadshus och omkring 10 500 lägenheter hos privata hyresvärdar. Fasaden är en gemensam del av huset, och det är föreningen eller hyresvärden som beställer och betalar en målning.",
       "Inför en stämma eller ett styrelsebeslut behöver föreningen veta vad som ska målas, vilken färgtyp som passar putsen och om lov krävs. Vi tar fram det underlaget efter platsbesöket, med kulörförslag som stämmer med husets ålder.",
     ],
     "aside": None},
    {"id": "essingen-fasad", "h2": "Villorna på Stora Essingen",
     "paras": [
       "De få villorna på Kungsholmen ligger nästan alla på Stora Essingen, som stadens vägledning Varsam utveckling av småhus- och villaområden räknar till villastäderna och markerar som kulturhistoriskt värdefull miljö. På en villa krävs normalt inte bygglov för att byta kulör, men det gäller inte om villan eller området är särskilt kulturhistoriskt värdefullt.",
       "Vägledningen beskriver villastädernas individuellt utformade hus, och ber att man tar tillvara karaktärsskapande material, kulörer och detaljer vid ombyggnad. Mer om villamålning finns under " + _L.format("malare-kungsholmen.html", "målare på Kungsholmen") + ".",
     ],
     "aside": None},
    {"id": "stadshagen", "h2": "Stadshagen och Stora Bryggeriet",
     "paras": [
       "Stadsmuseets skrift om Stadshagen berättar att Stadshagsberget under 1930-talet bebyggdes med det första större hyreshusområdet i Stadshagen, och att några av Stora Bryggeriets fabriksbyggnader från 1890 finns kvar. Där står alltså hus från olika tider och med olika fasadmaterial nära varandra.",
       "Vid en målning i ett sådant kvarter föreslår vi kulörer utifrån det egna husets ålder och material och inte efter grannhuset. En gammal fabriksbyggnad och ett bostadshus från 1930-talet behöver inte ha samma kulör.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning på Kungsholmen till",
  "steps": [
    ("Platsbesök", "Gratis besök där vi tittar på puts, färg och skador."),
    ("Klassning", "Stadsmuseets karta och om bygglov krävs."),
    ("Underlag", "Kulörförslag och färgtyp till styrelsen."),
    ("Ställning", "Ställning och tillstånd mot gatan."),
    ("Lagning", "Sprickor och lös puts lagas före målning."),
    ("Målning", "Grundning och målning i rätt väder."),
  ],
  "rot_h2": "Rotavdrag och föreningens fasad",
  "rot": _ROT_FASAD,
  "price_h2": "Vad påverkar priset på en fasadmålning på Kungsholmen?",
  "price": [
    "Fasadernas yta och höjd, putsens skick, hur mycket som behöver lagas, färgtyp, ställning mot gata och gård och om bygglov behövs. Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Behöver föreningen bygglov för att måla gårdsfasaden i en ny kulör?",
     "Inte om huset saknar utökad lovplikt och förutsättningarna i övrigt är uppfyllda. Inom riksintresse eller på blå- och grönklassade hus krävs bygglov."),
    ("När byggdes husen i Kristineberg?",
     "Enligt Stadsmuseet byggdes de flesta under 1930-talet, efter stadsplanetävlingar 1927 och 1929."),
    ("Får vi måla om gatufasaden i samma kulör utan lov?",
     "Ja, att måla om i samma kulör är underhåll. Det är bytet av kulör mot gatan som kräver bygglov på ett flerbostadshus."),
    ("Kan jag få rotavdrag för fasadmålning på min villa på Stora Essingen?",
     "Ja, målning av fasaden på ett småhus som du äger kan ge rotavdrag på arbetskostnaden."),
  ],
  "sources": [_of("Kungsholmens stadsdelsområde", "inre-staden/kungsholmen/kungsholmens-stadsdelsomrade"), _KRISTINEBERG,
              _STH_FASAD, _STH_KLASS, _VARSAM, _SKV],
  "cta": ("Ska fasaden målas på ert hus på Kungsholmen?", "Boka ett gratis platsbesök, så tittar vi på putsen och lovet innan föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust putsade 1930-talshus i en sluttning",
     "row of light ochre and pale yellow smooth rendered 1930s functionalist apartment buildings on a slope with trees and lawns, Stockholm, summer daylight" + _SFX),
    ("Nymålad putsfasad med fönster i rader",
     "close view of a freshly painted pale smooth rendered facade with rows of simple white windows on a 1930s apartment building, soft daylight" + _SFX),
    ("Ställning mot en gårdsfasad",
     "scaffolding with planks set up against the courtyard side of a light rendered apartment building, small courtyard with bushes, overcast day" + _SFX),
  ],
},

# ------------------------------------------------------------------ FASADMÅLNING VASASTAN
"fasadmalning-vasastan.html": {
  "kind": "district", "service": "fasadmalning", "ort": "Vasastan", "svc_label": "Fasadmålning",
  "title": "Fasadmålning i Vasastan – gatufasad, gårdsfasad och lov",
  "description": "Fasadmålning i Vasastan: stenstadens gatufasader med sockelvåning, enklare gårdsfasader, bygglov för ny kulör och föreningarnas roll.",
  "h1": "Fasadmålning i Vasastan",
  "lead": "Ett stenhus i Vasastan har två slags fasader: en påkostad mot gatan och en enklare mot gården. De målas ofta olika och lyder under olika regler. Geal Entreprenad AB målar fasader på flerbostadshus och tar fram underlaget till styrelsen.",
  "card": "Fasadmålning för föreningar.",
  "trust": _TRUST_BRF,
  "sections": [
    {"id": "stenstaden-vasastan", "anchor": "Stenstaden",
     "h2": "Gatufasaden med sockelvåning och takfot",
     "paras": [
       "Stadens redovisning av riksintressena beskriver den klassiska stenstaden som en tät kvartersstad med bebyggelse från 1870–1930, utbredd över bland annat Norrmalm där Vasastaden ingår. Bland de värdebärande dragen nämns gatufasadernas tydliga uppdelning i sockelvåning och huvudfasad, oftast med markerad takfot, och enklare gårdsfasader.",
       "För en fasadmålning betyder det att gatufasadens indelning ska synas även efter målningen. Sockelvåningen, listerna och omfattningarna kring fönster och portar har ofta egna kulörer, och de målas för sig. Stadens redovisning nämner också byggnadsdetaljering som ett värdebärande drag. I norra Vasastaden ligger dessutom kvarteren Motorn och Vingen, uppförda i slutet av 1910-talet som ett tidigt exempel på kooperativt byggande med kommunalt stöd, där bebyggelsen med gårdar och allmänna platser enligt staden har stort kulturvärde att bevara.",
     ],
     "aside": {"title": "Stenstadens drag", "items": [
       "Sockelvåning och huvudfasad", "Markerad takfot", "Enklare gårdsfasader", "Byggnadsdetaljering"]}},
    {"id": "gard-vasastan", "h2": "Gårdsfasaden har andra regler",
     "paras": [
       "Stockholms stad skriver att det för flerbostadshus krävs bygglov när kulör eller material ändras på en fasad som vetter mot allmän plats. Mot gården kan en fasadändring göras utan bygglov om vissa förutsättningar är uppfyllda. Men inom ett riksintresse för kulturmiljövården, i ett särskilt värdefullt område eller på blå- och grönklassade hus krävs bygglov även där.",
       "I praktiken målar vi ofta gårdsfasaderna i samma kulör som tidigare, och då är det underhåll. Vill föreningen ljusa upp en mörk gård med en ny kulör går vi först igenom husets klassning och om bygglov behövs.",
     ],
     "aside": None},
    {"id": "klass-vasastan", "h2": "Stadsmuseets klassning",
     "paras": [
       "Stadsmuseets klassificeringskarta visar riksintressen med blå ring, särskilt värdefulla områden med grön ring och klassade hus i blått, grönt, gult och grått. Staden skriver att byggherren själv ansvarar för att ta reda på vad som gäller för fastigheten och hänvisar till Stadsmuseet för rådgivning och bedömning.",
       "Är huset streckat i kartan är miljön inte inventerad, och då kan bygglov ändå krävas. Vi slår upp fastigheten innan vi föreslår kulörer, så att föreningen vet om lovet ska in i tidplanen.",
     ],
     "aside": {"title": "Kartans markeringar", "items": [
       "Blå ring: riksintresse", "Grön ring: särskilt värdefullt område", "Blått och grönt: högt värde", "Streckat: ej inventerat"]}},
    {"id": "foreningar-vasastan-fasad", "h2": "Över 20 000 bostadsrätter",
     "paras": [
       "Stadens områdesfakta för 2025 räknar i församlingsområdena Gustav Vasa, Västra Matteus och Östra Matteus drygt 20 000 bostadsrätter i flerbostadshus och omkring 6 500 lägenheter hos privata hyresvärdar. Fasaden är en gemensam del av huset, och målningen beställs av föreningen eller hyresvärden.",
       "Vi lämnar ett underlag som styrelsen kan ta till stämman: vilka fasader som ska målas, färgtyp, kulör, ställning mot gata och gård och om bygglov behövs.",
     ],
     "aside": None},
    {"id": "stallning-vasastan", "h2": "Ställningen mot gatan",
     "paras": [
       "Stockholms stad skriver att en byggställning på offentlig plats kräver polistillstånd, och att tillståndet ska vara utfärdat innan platsen används. Minst 1,6 meter ska vara fritt under ställningen, eller minst 2 meter av gångbanan ska finnas kvar för gående. Upplag för ställningsmaterial ska ingå i tillståndet.",
       "I Vasastans gator står gatufasaden direkt mot trottoaren, så ställningen och dess tillstånd blir en del av tidplanen. Gårdsfasaderna kan ofta målas från ställning eller lift på gården utan tillstånd för gatan.",
     ],
     "aside": {"title": "Ställning på gatan", "items": ["Polistillstånd före start", "1,6 m fritt under", "Eller 2 m gångbana kvar", "Upplag ingår i tillståndet"]}},
  ],
  "steps_h2": "Så går en fasadmålning i Vasastan till",
  "steps": [
    ("Platsbesök", "Gratis besök på gatan och gården med styrelsen."),
    ("Klassning", "Stadsmuseets karta och lovfrågan."),
    ("Underlag", "Kulörer för sockel, huvudfasad och detaljer."),
    ("Ställning", "Ställning och polistillstånd mot gatan."),
    ("Förarbete", "Rengöring, lagning och grundning."),
    ("Målning", "Huvudfasad, detaljer och gårdsfasader."),
  ],
  "rot_h2": "Rotavdrag och fasadmålning i Vasastan",
  "rot": _ROT_FASAD,
  "price_h2": "Vad påverkar priset på en fasadmålning i Vasastan?",
  "price": [
    "Fasadernas yta och höjd, antalet detaljer och kulörer, putsens skick, ställning mot gata och gård och om bygglov behövs. Efter ett gratis platsbesök får föreningen ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Varför målas sockelvåningen i Vasastan ofta i en annan kulör?",
     "Stenstadens gatufasader är uppdelade i sockelvåning och huvudfasad. Indelningen räknas som ett värdebärande drag och brukar synas i kulörerna."),
    ("Krävs bygglov för att måla gårdsfasaden i en ny kulör i Vasastan?",
     "Inom riksintresse, särskilt värdefulla områden och på blå- eller grönklassade hus krävs bygglov även mot gården."),
    ("Vad betyder streckat i Stadsmuseets karta?",
     "Att miljön inte är inventerad än. Bygglov kan då ändå behövas, och staden hänvisar till Stadsmuseet för bedömning."),
    ("Vem betalar fasadmålningen i en bostadsrättsförening?",
     "Föreningen. Fasaden är en gemensam del av huset."),
    ("Behöver vi polistillstånd för ställningen när gatufasaden målas?",
     "Ja, om ställningen står på offentlig plats som trottoaren. Tillståndet ska vara utfärdat innan platsen används."),
  ],
  "sources": [_of("Gustav Vasa", "inre-staden/norra-innerstaden/gustav-vasa"),
              _of("Västra Matteus", "inre-staden/norra-innerstaden/vastra-matteus"),
              _of("Östra Matteus", "inre-staden/norra-innerstaden/ostra-matteus"), _RIKS, _STH_FASAD, _STH_KLASS, _SKV],
  "cta": ("Ska fasaden målas på ert hus i Vasastan?", "Boka ett gratis platsbesök, så går vi igenom gatu- och gårdsfasad och lovet innan föreningen får ett skriftligt kostnadsförslag."),
  "img": [
    ("Stenhus med sockelvåning i en annan kulör än fasaden",
     "late 19th century Stockholm apartment building facade with a darker rusticated ground floor, pale ochre upper floors, white window surrounds and a cornice, quiet street, daylight" + _SFX),
    ("Enkel putsad gårdsfasad i ett innerstadskvarter",
     "plain light grey rendered courtyard facade of an old Stockholm apartment block with simple windows, a small paved courtyard with a tree, soft daylight" + _SFX),
    ("Listverk och fönsteromfattning nära en fasad",
     "close view of a plastered window surround and moulded cornice on an old city facade freshly painted in off-white against a pale yellow wall, daylight" + _SFX),
  ],
},

# ------------------------------------------------------------------ TOTALRENOVERING ÖSTERMALM
"totalrenovering-ostermalm.html": {
  "kind": "district", "service": "totalrenovering", "ort": "Östermalm", "svc_label": "Totalrenovering",
  "title": "Totalrenovering på Östermalm – lägenheten och styrelsen",
  "description": "Totalrenovering på Östermalm: styrelsens tillstånd enligt bostadsrättslagen, lägenheter med kulturvärden, ny planlösning, bärande väggar och ventilation.",
  "h1": "Totalrenovering på Östermalm",
  "lead": "En totalrenovering på Östermalm gäller i regel en lägenhet i ett äldre stenhus. Innan något rivs behövs styrelsens tillstånd, och ibland en anmälan till staden. Geal Entreprenad AB totalrenoverar lägenheter och tar fram underlaget till föreningen.",
  "card": "Renovera hela lägenheten.",
  "sections": [
    {"id": "lagenheter-ostermalm", "anchor": "Lägenheterna",
     "h2": "Fem tusen bostadsrätter i ett församlingsområde",
     "paras": [
       "Stadens områdesfakta för 2025 räknar i Hedvig Eleonora drygt 5 100 bostadsrätter i flerbostadshus, omkring 2 100 lägenheter hos privata hyresvärdar och elva småhus. Stenstaden här uppfördes enligt stadens redovisning av riksintressena till största delen under 1800-talets senare del.",
       "Hyr du lägenheten får du enligt staden normalt inte göra ändringar i bärande delar, ventilation eller vatten och avlopp. En totalrenovering är därför i praktiken något som bostadsrättshavare och fastighetsägare gör, och för bostadsrättshavaren börjar den hos styrelsen.",
     ],
     "aside": {"title": "Hedvig Eleonora 2025", "items": [
       "5 151 bostadsrätter", "2 072 hos privata hyresvärdar", "67 hos allmännyttan", "11 småhus"]}},
    {"id": "styrelsen-ostermalm", "h2": "Fem saker kräver styrelsens tillstånd",
     "paras": [
       "Bostadsrättslagen säger att du inte utan styrelsens tillstånd får göra ingrepp i en bärande konstruktion, installera eller ändra ledningar för avlopp, värme, gas eller vatten, installera eller ändra ventilation, installera eller ändra eldstad eller rökkanal eller på annat sätt påverka brandskyddet, eller göra någon annan väsentlig förändring av lägenheten.",
       "För en lägenhet med särskilda historiska, kulturhistoriska, miljömässiga eller konstnärliga värden krävs enligt lagen tillstånd för varje åtgärd som påverkar ett sådant värde. Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet för föreningen, och den kan förena tillståndet med villkor.",
     ],
     "aside": {"title": "Styrelsens tillstånd krävs för", "items": [
       "Bärande konstruktion", "Avlopp, värme, gas och vatten", "Ventilation", "Eldstad, rökkanal, brandskydd"]}},
    {"id": "planlosning-ostermalm", "h2": "Ny planlösning – med eller utan anmälan",
     "paras": [
       "Stockholms stad skriver att du inte behöver göra en anmälan när du ändrar planlösningen inom en lägenhet och inga tekniska egenskapskrav påverkas, till exempel om du flyttar köket eller badrummet eller ändrar hur rummen används. Delar du en lägenhet i två krävs däremot bygglov, eftersom en ny bostad skapas.",
       "Påverkas bärande konstruktion eller brandskydd, eller ändras ventilation eller vatten och avlopp väsentligt, krävs en anmälan och startbesked. Staden påpekar att ritningar kan vara ofullständiga och att det inte är säkert att husen byggts efter dem, så vid osäkerhet om en vägg är bärande tar vi in en konstruktör.",
     ],
     "aside": None},
    {"id": "ventilation-ostermalm", "h2": "Självdraget i det gamla huset",
     "paras": [
       "Staden beskriver att det i äldre hus ofta finns självdragsventilation, där använd luft sugs ut genom kanaler i kök och badrum och tilluft kommer in via ventiler, vädringsfönster eller otätheter. På sommaren kan drageffekten utebli.",
       "Vid en totalrenovering går vi därför igenom kanalerna innan kök och badrum ritas, och väsentliga ändringar av ventilationen tar vi upp med styrelsen och staden. Mer om tjänsten finns under " + _L.format("villarenovering.html", "villarenovering och totalrenovering") + ".",
     ],
     "aside": None},
    {"id": "el-ostermalm", "h2": "Elen i den gamla lägenheten",
     "paras": [
       "Elsäkerhetsverket skriver att de flesta elinstallationsarbeten ska utföras av ett registrerat elinstallationsföretag, och att det vid förändringar i den fasta installationen, till exempel ett uttag i köket eller ledningar i väggar, ska anlitas ett sådant. Vid en totalrenovering byts ofta hela elen i lägenheten.",
       "Är styrelsen missnöjd med din ansökan, eller du med styrelsens beslut, kan du enligt bostadsrättslagen begära att hyresnämnden prövar frågan. Vi tar därför fram ett underlag som visar vad som ändras och hur, så att beslutet kan fattas på rätt grund.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en totalrenovering på Östermalm till",
  "steps": [
    ("Platsbesök", "Gratis besök i lägenheten och genomgång av ritningar."),
    ("Ansökan", "Underlag till styrelsen för tillståndet."),
    ("Anmälan", "Startbesked om stomme, brand eller ventilation berörs."),
    ("Rivning", "Skydd av trapphus och bortforsling."),
    ("Installationer", "El, vatten, avlopp och ventilation."),
    ("Ytskikt", "Golv, väggar, kök och badrum."),
  ],
  "rot_h2": "ROT-avdrag för totalrenovering på Östermalm",
  "rot": [
    "I en bostadsrätt ger Skatteverket rotavdrag för arbete innanför lägenhetens tak, väggar och golv som du ansvarar för enligt stadgarna, till exempel att riva innerväggar och bygga om planlösningen. Stambyten och arbete på gemensamma delar ger inget avdrag för bostadsrättshavaren.",
    "Avdraget är högst 30 procent av arbetskostnaden och högst 50 000 kronor per person och år. Material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset på en totalrenovering på Östermalm?",
  "price": [
    "Lägenhetens storlek, hur mycket av planlösningen som ändras, om bärande väggar, ventilation och ledningar berörs, föreningens villkor för arbetet och vilken standard du väljer. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan styrelsen säga nej till min totalrenovering på Östermalm?",
     "Styrelsen får bara vägra om åtgärden är till påtaglig skada eller olägenhet för föreningen, men den kan ställa villkor."),
    ("Behöver jag tillstånd för att ändra något i en lägenhet med kulturvärden?",
     "Ja. Bostadsrättslagen kräver tillstånd för varje åtgärd som påverkar ett sådant värde."),
    ("Måste jag anmäla till staden när jag flyttar köket i lägenheten?",
     "Nej, inte om inga tekniska egenskapskrav påverkas. Ändras bärande konstruktion, brandskydd, ventilation eller vatten och avlopp väsentligt krävs anmälan."),
    ("Kan jag lita på de gamla ritningarna när jag river en vägg?",
     "Inte helt. Staden skriver att ritningar kan vara ofullständiga och att det inte är säkert att huset byggts efter dem. Vid osäkerhet tar vi in en konstruktör."),
    ("Vad gör jag om styrelsen säger nej till min renovering?",
     "Enligt bostadsrättslagen kan du begära att hyresnämnden prövar frågan."),
  ],
  "sources": [_of("Hedvig Eleonora", "inre-staden/norra-innerstaden/hedvig-eleonora"), _RIKS, _BRL, _STH_PLAN, _STH_BAR, _STH_VENT, _SKV],
  "cta": ("Planerar du en totalrenovering på Östermalm?", "Boka ett gratis platsbesök, så går vi igenom lägenheten och föreningens tillstånd innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Ljust renoverat rum med stuckatur i en sekelskifteslägenhet",
     "bright empty room in a renovated late 1800s Stockholm apartment with ornate ceiling plaster mouldings, tall windows, herringbone parquet, white walls, daylight" + _SFX),
    ("Rum under renovering med skyddat golv och öppen vägg",
     "renovation in progress in an old city apartment: protective paper covering the floor, a partly removed non-load-bearing wall showing studs, tools on the floor, daylight from tall windows" + _SFX),
    ("Ventilationsgaller högt upp på en vägg i ett kök",
     "close view of an old cast metal ventilation grille high on a white painted kitchen wall near the ceiling in an old apartment, soft daylight" + _SFX),
  ],
},

}
