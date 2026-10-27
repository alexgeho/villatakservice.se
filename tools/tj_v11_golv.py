# -*- coding: utf-8 -*-
"""Golvläggare – ortsidor v11: Sigtuna, Hässelby, Enskede, Älvsjö, Spånga, Farsta (2026-10-25).
Fakta endast från källorna i respektive 'sources', öppnade och lästa 2026-10-25:
  SCB (BO0104T04, bostäder i småhus 2025: Sigtuna 7 571, kontrollerat via SCB:s API), Sigtuna kommun (Radon;
  Fukt och mögel), Stockholms stad (Områdesfakta 2025, tabellen "Bostäder efter hustyp och upplåtelse/ägarform":
  Hässelby villastad 5 009 småhusbostäder varav 4 757 äganderätter, Hässelby gård 339, Gamla Enskede 923,
  Enskededalen 544, Enskedefältet 406, Enskede gård 430, Långbro 1 423, Herrängen 1 143, Långsjö 872, Solhem 2 038
  varav 1 946 äganderätter, Bromsten 1 066, Flysta 663, Sundby 559, Sköndal 1 595, Tallkrogen 945, Svedmyra 359;
  Parkplan Älvsjö del 2 – Herrängen, Långsjö), Stadsmuseet via Stockholmskällan (Stockholms Spår: Hässelby gård,
  Enskede gård, Blåsut, Tallkrogen, Svedmyra), Boverket (Fuktrisker med betongplatta på mark, med fördjupningen
  om plattor förr), Golvbranschen GBR (Branschriktlinjer SLIP 22, LUT 22, OLJA 22, UNDERHÅLL 22, RENOV. 24;
  Trägolv på golvvärme maj 2022 (pdf); Stavar som släpper; Knarr i trägolv; Skillnad mellan olika trägolv;
  Fanérgolv; Laminatgolv; Linoleumgolv; Gummigolv; Övriga plastgolv; Om keramik på golv och vägg; Branschstandard
  för RF-mätning) och Skatteverket (Ger arbetet rätt till rotavdrag?: slipa och byta golv, byta plastmatta till
  trägolv, sanera asbest och radon i samband med byggarbete; Så fungerar rotavdraget).
Ortsval: alla sex orterna har ett stort antal småhus i områdesfakta/SCB – inget byte mot Hägersten/Vällingby.
Strukna (ej verifierade eller oklara i källan): vilka golv som ursprungligen lades i husen i respektive område
(fur, linoleum, parkett), vilken grund husen i Märsta och Sigtuna har, att småstugorna i Tallkrogen/Svedmyra har
träbjälklag eller linoleum, hur radhusen vid Astrakangatan är byggda invändigt, byggår per hus i Spånga, Hässelby
villastads tillkomsthistoria (ingen källa öppnad – bara områdesfaktas siffror används), Arbetsmiljöverkets
gränsvärden för trädamm (sidan hittades inte), radonbidrag, kvartsdamm vid slipning av betong, GBR:s uppgifter om
åtgång i liter per kvadratmeter för lut (finns i källan men utelämnas som onödig detalj). Inga priser, garantier,
omdömen, egna uppdrag i orterna eller certifikat.
Kritikpass 2026-10-25: alla siffror kontrollerade mot källtexterna; "många hus i Sigtuna står på platta" struken
(ingen källa) och omskriven till ett villkor; GBR:s "yttemperaturen får aldrig överstiga 27 °C" återgiven som
gräns utan absolutord; Skatteverkets asbest/radon-punkt återgiven som "i samband med byggarbete"; "partikelavskiljare"
rättat till källans "partikelseparator"; "spikar sänks" struket (SLIP 22 säger bara att spikar avlägsnas); Svedmyra "med
början 1931–33"; lamellparkett "oftast" i tre skikt; Flysta "fyra av fem" (663 av 833) i stället för "nästan alla";
Enskede-FAQ om grovslipning fick SLIP 22 som källa. Bilder: alvsjo-2 gjord om två gånger (förvrängda bjälklag/slangar
-> enkel bild av ekgolv med matta), farsta-1 gjord om (kakel i stället för linoleum); alt-texter för hasselby-2 och
spanga-2 anpassade till bilderna.
Korslänkar via V4_MODULES i tjanster_v1.py. Schema: se tools/tj_check.py."""

_L = '<a class="text-link" href="{0}">{1}</a>'

_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_SCB = ("SCB – Antal lägenheter efter region, hustyp och upplåtelseform (BO0104), 2025",
        "https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BO__BO0104__BO0104D/BO0104T04/")
_OF = "https://start.stockholm/globalassets/start/om-stockholms-stad/utredningar-statistik-och-fakta/statistik/omradesfakta/"
_SSM = "https://stockholmskallan.stockholm.se/contentfiles/SSM/Texter/Text_0001/SSM_DOK_{0}.pdf"
_GT = "https://www.golvbranschen.se/teknik--material/"
_GD = "https://www.golvbranschen.se/siteassets/dokument/"
_GBR_SLIP = ("Golvbranschen – Branschriktlinjer SLIP 22, slipning av trägolv (pdf)",
             _GD + "branschriktlinjer/branschriktlinjer---slipning-av-tragolv---slip-22.pdf")
_GBR_LUT = ("Golvbranschen – Branschriktlinjer LUT 22, lutbehandling av trägolv (pdf)",
            _GD + "branschriktlinjer/branschriktlinjer---lutbehandling-av-tragolv---lut-22.pdf")
_GBR_OLJA = ("Golvbranschen – Branschriktlinjer OLJA 22, oljebehandling av trägolv (pdf)",
             _GD + "branschriktlinjer/branschriktlinjer---oljebehandling-av-tragolv---olja-22.pdf")
_GBR_UND = ("Golvbranschen – Branschriktlinjer UNDERHÅLL 22, underhåll av trägolv (pdf)",
            _GD + "branschriktlinjer/branschriktlinjer---underhall-av-tragolv---underhall-22.pdf")
_GBR_RENOV = ("Golvbranschen – Branschriktlinjer RENOV. 24, renovering av halvhårda golv (pdf)",
              _GD + "branschriktlinjer/branschriktliner---renovering-av-halvharda-golv---2024.pdf")
_GBR_TGV = ("Golvbranschen – Trägolv på golvvärme, maj 2022 (pdf)",
            _GD + "tragolv-pa-golvvarme/tragolv-pa-golvvarme-maj-2022.pdf")
_GBR_STAV = ("Golvbranschen – Stavar som släpper", _GT + "tragolv/tekniska-tragolvsfragor/stavar-som-slapper/")
_GBR_KNARR = ("Golvbranschen – Knarr i trägolv", _GT + "tragolv/tekniska-tragolvsfragor/knarr-i-tragolv/")
_GBR_SKILL = ("Golvbranschen – Skillnad mellan olika trägolv", _GT + "tragolv/skillnad-mellan-olika-tragolv/")
_GBR_FANER = ("Golvbranschen – Fanérgolv", _GT + "tragolv/fanergolv/")
_GBR_LAM = ("Golvbranschen – Laminatgolv", _GT + "tragolv/laminatgolv/")
_GBR_LINO = ("Golvbranschen – Linoleumgolv", _GT + "linoleumgolv/")
_GBR_GUMMI = ("Golvbranschen – Gummigolv", _GT + "gummigolv/")
_GBR_PLAST = ("Golvbranschen – Övriga plastgolv", _GT + "plastgolv/ovriga-plastgolv/")
_GBR_KER = ("Golvbranschen – Om keramik på golv och vägg", _GT + "kakel-och-klinker/om-keramik-pa-golv-och-vagg/")
_GBR_RF = ("Golvbranschen – Branschstandard för RF-mätning", _GT + "golvavjamning/branschstandard-for-rf-matning/")
_BOV_PLATTA = ("Boverket – Fuktrisker med betongplatta på mark",
               "https://www.boverket.se/sv/byggande/forebygg-fel-brister-skador/risker-byggande/risker-fuktskador/fuktrisker-for-grund/betongplatta-mark/")
_SIG = "https://www.sigtuna.se/bygga-bo-och-miljo/mitt-boende/storningar-i-boendemiljon/"

PAGES_TJ = {

# ------------------------------------------------------------------ SIGTUNA
"golvlaggare-sigtuna.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Sigtuna", "svc_label": "Golvläggare",
  "title": "Golvläggare i Sigtuna – nytt golv på betongplatta",
  "description": "Golvläggare i Sigtuna: golv på betongplatta, fuktmätning före läggning, gamla sandbäddar och flytspackel och radon när rör dras genom grunden.",
  "h1": "Golvläggare i Sigtuna",
  "lead": "Står huset på en betongplatta är det skikten mellan betongen och ytan som avgör om ett nytt golv håller, inte själva golvet. Enligt SCB finns 7 571 bostäder i småhus i Sigtuna kommun. Geal Entreprenad AB lägger nya golv och slipar trägolv i Märsta, Valsta, Sigtuna stad, Rosersberg och resten av kommunen, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Golv på platta, fuktmätning och radon.",
  "sections": [
    {"id": "plattor-forr", "anchor": "Betongplattan",
     "h2": "Plattan under golvet har byggts på många sätt",
     "paras": [
       "Boverket beskriver hur betongplattan på mark kom in i bostadsbyggandet i början av 1960-talet och hur sättet att bygga golv ovanpå den har ändrats flera gånger sedan dess, ofta för att lösa ett problem som den förra metoden gav. En plastfolie över betongen med ångöppen isolering ovanpå skulle stoppa fukten underifrån, men under folien kunde smuts ge påväxt och lukt. Flytande golv på en bädd av sand ersatte träreglarna, men sanden var inte ren och gav också påväxt. Flytande golv på cellplast sviktade och gav gnisselljud.",
       "Boverket nämner också avjämningsmassa med kasein, ett flytspackel med benmjöl, som kunde brytas ned kemiskt när fukten var hög och påverka inomhusmiljön. Två hus från samma årtionde kan därför ha helt olika golv under ytan. Vi börjar med att lyfta en tröskel eller en sockellist för att se vilka skikt som finns, innan vi föreslår vad som ska rivas och vad som kan ligga kvar.",
     ],
     "aside": {"title": "Kan ligga under ytan", "items": [
       "Plastfolie direkt på betongen", "Sandbädd under ett flytande golv",
       "Cellplast under spånskivor", "Äldre flytspackel med kasein"]}},
    {"id": "sand-och-tra", "h2": "Trä mot betong och sand med organiskt material",
     "paras": [
       "Sigtuna kommun räknar upp ett antal konstruktioner som kan leda till fuktproblem i ett hus. Två av dem rör golvet direkt: trämaterial i kontakt med betong, till exempel impregnerat virke som har gjutits in i bottenplattan, och sand ovanpå plattan som är förorenad med organiskt material. Kommunen nämner också otillräcklig dränering runt huset, hus i låglänta lägen med högt grundvatten och stuprör som inte leder bort vattnet, i kombination med fel lutning på marken.",
       "Mögel och fuktiga byggmaterial kan enligt kommunen ge kraftiga dofter. Känns en unken lukt när den gamla mattan eller spånskivan lyfts, avbryter vi och tar reda på varifrån fukten kommer innan något nytt läggs. Ett nytt golv ovanpå en fuktig bädd flyttar bara problemet ett lager upp. Leder stuprören vattnet mot grunden finns det mer om takavvattningen under " + _L.format("takrenovering-sigtuna.html", "takrenovering i Sigtuna") + ".",
     ],
     "aside": None},
    {"id": "fuktmatning-sigtuna", "h2": "Fuktmätning innan golvet läggs",
     "paras": [
       "Om betongen inte har torkat tillräckligt innan golvet läggs kan det enligt Boverket uppstå fuktskador under golvet, i golvmaterialet eller i limmet, och det kan ge dålig lukt i huset. Därför mäter man den relativa fuktigheten, RF, i betongen och i ett eventuellt avjämningsskikt. Golvbranschen skriver att mätning i golvavjämning numera görs enligt RBK:s fuktmätningsmanual inom RBK:s system för fuktkontrollanter, och att en RF-mätning på självtorkande avjämning inte ger ett relevant värde inför en tidig golvläggning, eftersom massan fortsätter att torka kemiskt inifrån.",
       "Mätvärdet styr sedan valet av golv. Linoleum har enligt Golvbranschen ett lågt ånggenomgångsmotstånd och kan därför läggas på betong med en restfukt på upp till 90 procent RF. För trägolv är kraven högre: Golvbranschens handbok om trägolv på golvvärme anger att parkett ska skyddas mot fukt från undergolvet när RF överstiger 60 procent, och att ett fuktskydd som ångspärr krävs på golv mot mark. Handboken påpekar också att det bara får finnas ett fuktskydd i golvet, eftersom fukt annars kan stängas in mellan två skikt.",
     ],
     "aside": {"title": "Före läggning på platta", "items": [
       "Lyft en list och se skikten", "Låt mäta RF i betong och spackel",
       "Välj golv efter mätvärdet", "Ett fuktskydd, inte två"]}},
    {"id": "radon-sigtuna", "h2": "Rör genom plattan och radon",
     "paras": [
       "Radon från marken kan enligt Sigtuna kommun läcka in genom otätheter i grunden och där rör och kablar går in i huset. Kommunen nämner också blåbetong, som tillverkades mellan 1929 och 1975, och skriver att många hus med källare eller suterrängvåning från den tiden kan innehålla den. Radonhalten bör ligga under 200 becquerel per kubikmeter luft, och mätningen ska pågå i minst två månader under eldningssäsongen, mellan 1 oktober och 30 april.",
       "Ska golvet öppnas för nya avloppsrör, till exempel när " + _L.format("badrumsrenovering-sigtuna.html", "badrummet i Sigtuna görs om") + ", tätar vi kring genomföringarna innan golvet stängs. Har huset inte mätts på länge är det klokt att beställa mätdosor från ett ackrediterat laboratorium inför vintern efter arbetet. Kommunen hänvisar till Swedac och Svensk Radonförening för att hitta ett sådant. Vill du jämföra golvtyper innan du bestämmer dig finns en genomgång på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett golvbyte på platta till i Sigtuna",
  "steps": [
    ("Platsbesök", "Vi lyfter en list eller tröskel, känner efter lukt och frågar om husets ålder och tidigare golvbyten."),
    ("Fuktmätning vid behov", "Ser underlaget tveksamt ut föreslår vi en RF-mätning innan golvtyp väljs."),
    ("Skriftligt kostnadsförslag", "Rivning, nytt underlag, fuktskydd och golv redovisas som egna poster."),
    ("Rivning och underlag", "Gamla skikt tas bort, plattan rensas och avjämnas om det behövs."),
    ("Läggning", "Fuktskydd, mellanlägg och det nya golvet läggs, med rörelsefog mot väggarna."),
    ("Avslut", "Lister och trösklar monteras och vi går igenom skötseln av golvet med dig."),
  ],
  "rot_h2": "ROT-avdrag för golvet i Sigtuna",
  "rot": [
    "Skatteverket ger rotavdrag för att slipa och byta golv och för att byta en plastmatta mot trägolv. På listan över godkända arbeten står också att sanera asbest och radon i samband med byggarbete. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och tillsammans med rutavdrag högst 75 000 kr.",
    "Material och resekostnader ger inget avdrag. Geal drar avdraget direkt på fakturan och ansöker om det hos Skatteverket.",
  ],
  "price_h2": "Vad påverkar priset på ett golv i Sigtuna?",
  "price": [
    "Golvytan och hur mycket av det gamla underlaget som måste bort betyder mest. En fuktmätning eller en ny avjämning kommer till som egna poster. Efter det kostnadsfria platsbesöket får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur vet vi om betongplattan i vårt hus i Märsta är torr nog för ett nytt golv?",
     "Genom en mätning av den relativa fuktigheten i betongen och i eventuell avjämning. Golvbranschen hänvisar till RBK:s fuktmätningsmanual. Mätvärdet avgör vilket golv och vilket fuktskydd som passar."),
    ("Kan linoleum läggas på en betongplatta som inte är helt torr?",
     "Golvbranschen skriver att linoleum kan läggas på betong med en restfukt på upp till 90 procent RF tack vare materialets låga ånggenomgångsmotstånd. Varifrån fukten kommer behöver ändå utredas först."),
    ("Vad betyder det om det luktar unket när den gamla golvmattan i Sigtuna lyfts?",
     "Sigtuna kommun skriver att mögel och fuktiga byggmaterial kan ge kraftiga dofter. Vi tar reda på orsaken, till exempel organisk sand eller trä mot betong, innan något nytt läggs."),
    ("Behöver vi mäta radon efter att plattan har öppnats för nya avloppsrör?",
     "Det är klokt. Kommunen skriver att radon kan läcka in där rör går in i huset. Mätningen ska pågå i minst två månader mellan 1 oktober och 30 april."),
    ("Kan vi lägga två lager plastfolie under trägolvet för säkerhets skull?",
     "Nej. Golvbranschens handbok säger att det bara får finnas ett fuktskydd i golvkonstruktionen, eftersom fukt annars kan stängas in mellan skikten."),
  ],
  "sources": [
    _SCB,
    ("Sigtuna kommun – Fukt och mögel", _SIG + "fukt-och-mogel.html"),
    ("Sigtuna kommun – Radon", _SIG + "radon.html"),
    _BOV_PLATTA, _GBR_RF, _GBR_LINO, _GBR_TGV, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i huset i Sigtuna bytas?", "Boka ett gratis platsbesök, så lyfter vi en list och ser vad som ligger under innan du får ett skriftligt kostnadsförslag."),
  "img": [
    ("Nylagt ljust ekgolv i vardagsrummet i en enplansvilla",
     "empty bright living room in a Swedish single-storey 1970s villa, newly laid light natural oak plank floor, white walls, white skirting boards, large window with view of a lawn and birch trees, soft overcast daylight, no furniture, no people, no text"),
    ("Betongplatta med ångspärr och golvbrädor redo för läggning",
     "corner of an empty room during floor renovation in a Swedish house, bare clean grey concrete slab, a neatly unrolled clear polyethylene vapour barrier sheet with taped overlaps covering part of the slab, a roll of thin white foam underlay and a stack of packaged light oak floor planks against a white wall, skirting boards removed, natural daylight from a window, no people, no hands, no tools, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ HÄSSELBY
"golvlaggare-hasselby.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Hässelby", "svc_label": "Golvläggare",
  "title": "Golvläggare i Hässelby – slipa trägolvet i villa och radhus",
  "description": "Golvläggare i Hässelby: går trägolvet att slipa igen, svikt och vågor i ytan, slipningens tre steg och hur slipdammet hanteras. Gratis platsbesök.",
  "h1": "Golvläggare i Hässelby",
  "lead": "Ett trägolv som har legat i en villa i femtio år kan få en ny yta, men bara om det finns tillräckligt med trä kvar och undergolvet ligger stilla. Geal Entreprenad AB slipar, lagar och lägger golv i Hässelby villastad, Hässelby gård och Hässelby strand. Du får ett gratis platsbesök och ett skriftligt kostnadsförslag, och ROT-avdraget dras direkt på fakturan.",
  "card": "Slipa trägolvet – eller lägga nytt.",
  "sections": [
    {"id": "hasselby-hus", "anchor": "Husen i Hässelby",
     "h2": "Fem tusen småhusbostäder i villastaden",
     "paras": [
       "Enligt Stockholms stads områdesfakta för 2025 finns 7 029 bostäder i Hässelby villastad, och 5 009 av dem ligger i småhus. Nästan alla, 4 757, är äganderätter. I grannområdet Hässelby gård finns ytterligare 339 bostäder i småhus. Stadsmuseets Stockholms Spår berättar att radhusen vid Astrakangatan och Friherre Lövstavägen uppfördes av Småstugebyrån 1957 och att de ansågs mycket moderna när de var nya.",
       "Ett hus som har haft flera ägare kan ha fått golvet slipat mer än en gång, och ibland har nya golv lagts ovanpå gamla. Därför börjar vi med att ta reda på vad golvet är gjort av och hur mycket trä som finns kvar, innan vi föreslår slipning eller ett nytt golv.",
     ],
     "aside": None},
    {"id": "slipbart", "h2": "Går golvet att slipa en gång till?",
     "paras": [
       "Golvbranschens riktlinjer för slipning, SLIP 22, börjar med en kontroll av golvet. Det finns golv som liknar ett slipbart trägolv men inte går att slipa, till exempel laminat, golv med ett slitskikt tunnare än en millimeter och fabrikslackerade golv som är EB-härdade. Är man osäker på slitskiktet rekommenderar riktlinjerna att man kontrollerar med en kniv i en springa i ett hörn av rummet. Golvbranschen räknar med att ungefär en millimeter försvinner vid varje slipning.",
       "Har slitskiktet lossnat på något ställe ska det limmas fast före slipningen. Spikar ska tas bort, eftersom de förstör slippappret och kan ge gnistor som i värsta fall antänder dammet i slipmaskinens påse. Visar det sig att golvet inte tål en slipning till, är ett nytt golv ovanpå eller i stället för det gamla nästa alternativ. Det tar vi upp med dig innan något arbete börjar.",
     ],
     "aside": {"title": "Kontroll före slipning", "items": [
       "Kniv i en springa i hörnet", "Lösa stavar limmas först",
       "Spikar tas bort", "Svikt rättas eller noteras"]}},
    {"id": "svikt-hasselby", "h2": "Svikt och vågor i ytan",
     "paras": [
       "Undergolvet ska enligt SLIP 22 vara stabilt och utan svikt. Sviktar golvkonstruktionen kan ytan bli vågig efter slipningen, det som branschen kallar ondulering, och då blir resultatet inte godtagbart. Går svikten inte att åtgärda före slipningen ska kunden få veta det innan arbetet börjar. Vågor kan också komma från en felinställd slipmaskin, och det är golvsliparens ansvar att maskinen är rätt inställd och servad.",
       "I ett äldre hus kan svikten sitta i en enskild bjälke eller i en bräda som har släppt från sitt underlag. Vi går över golvet och lyssnar och känner efter innan vi lämnar ett kostnadsförslag. Behöver bjälklaget förstärkas eller brädor bytas tar vi med det som en egen post. Mer om snickeriarbeten i huset finns på sidan om " + _L.format("snickare-hasselby.html", "snickare i Hässelby") + ".",
     ],
     "aside": None},
    {"id": "tre-steg", "h2": "Grovslipning, mellanslipning och finslipning",
     "paras": [
       "SLIP 22 delar slipningen i tre steg. Grovslipningen tar bort all tidigare ytbehandling och jämnar till golvet, normalt med korn 36–50. Mellanslipningen görs i två steg med finare korn, normalt 60–80, för att få bort reporna från grovslipningen. Finslipningen jämnar ut skillnaden mellan kantslipen och den stora maskinen, och slutresultatet ska motsvara korn 100 på barrträ och korn 120 på lövträ.",
       "Slipriktningen följer träet. Ett golv med brädor finslipas i träets längdriktning, medan rutmönster, fiskben och andra mönster normalt slipas diagonalt först och sedan i rummets längdriktning eller från det håll ljuset kommer. Golvet bör inte ytbehandlas när luftfuktigheten inomhus ligger utanför 30–60 procent eller när träets fuktkvot ligger utanför 6–10 procent. Riktlinjerna påpekar att det är variationerna i fukt, inte nivån i sig, som ger sprickor i spacklade fogar.",
     ],
     "aside": {"title": "Slipningens steg", "items": [
       "Grovslipning, korn 36–50", "Mellanslipning, korn 60–80",
       "Finslipning motsvarande korn 100–120", "Ytbehandling vid 30–60 % RF"]}},
    {"id": "slipdamm", "h2": "Slipdammet: hälsa och brandrisk",
     "paras": [
       "Golvbranschen skriver att slipdamm från bland annat ek och bok är cancerframkallande. Slipningen bör göras med en partikelseparator eller cyklondammsugare med HEPA-filter, och den som slipar ska ha andningsskydd av klass P3, hörselskydd och maskinen kopplad via jordfelsbrytare. Därför stänger vi dörrar och täcker öppningar mot rum som inte slipas.",
       "Damm som har blandats med rester av lack eller olja kan självantända. Dammpåsen ska tömmas efter slipningen och innehållet förvaras utomhus eller på en brandsäker plats. Golvbranschens riktlinjer för oljebehandling tillägger att trasor som har varit i kontakt med olja ska ligga i vatten i minst ett dygn eller brännas direkt. Ska väggarna målas efter golvet finns mer under " + _L.format("malare-hasselby.html", "målare i Hässelby") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en golvslipning till i Hässelby",
  "steps": [
    ("Platsbesök", "Vi kontrollerar slitskikt, spikar och svikt och frågar om tidigare slipningar."),
    ("Skriftligt kostnadsförslag", "Slipning, lagning och ytbehandling redovisas var för sig."),
    ("Förberedelse", "Möbler flyttas, lösa stavar limmas och angränsande rum skyddas mot damm."),
    ("Slipning", "Golvet grov-, mellan- och finslipas med dammavskiljning."),
    ("Ytbehandling", "Lack, olja eller annan behandling läggs på vid rätt fukt och temperatur."),
    ("Avslut", "Dammpåsar tas ut, lister sätts tillbaka och du får skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för slipning och nytt golv i Hässelby",
  "rot": [
    "Att slipa och byta golv i ett småhus du äger är rotarbete enligt Skatteverket. Avdraget är 30 procent av arbetskostnaden och högst 50 000 kr per person och år. Rot och rut får tillsammans vara högst 75 000 kr.",
    "Material, som lack och olja, och resekostnader ger inget avdrag. Geal gör avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar kostnaden för en slipning i Hässelby?",
  "price": [
    "Golvytan, hur många rum som slipas och hur mycket som behöver lagas före slipningen betyder mest. Mönstergolv och trappor tar längre tid än raka brädor. Platsbesöket är gratis och du får ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Hur många gånger kan trägolvet i vår villa i Hässelby slipas?",
     "Det beror på hur tjockt träet är ovanför not och spår. Golvbranschen räknar med att ungefär en millimeter försvinner per slipning, så vi mäter innan vi föreslår något."),
    ("Varför slipas ett fiskbensgolv diagonalt först?",
     "Enligt Golvbranschens riktlinjer slipas mönstergolv där träet ligger åt olika håll normalt diagonalt först och sedan i rummets längdriktning, så att inga slipränder syns."),
    ("Är slipdammet från ett ekgolv farligt att andas in?",
     "Golvbranschen skriver att slipdamm från bland annat ek och bok är cancerframkallande. Slipningen görs därför med dammavskiljning och HEPA-filter, och den som slipar har andningsskydd av klass P3."),
    ("Varför ska dammpåsen från golvslipen inte stå kvar inomhus?",
     "Slipdamm som blandats med lack- eller oljerester kan självantända. Riktlinjerna säger att påsen ska tömmas och innehållet förvaras utomhus eller på en brandsäker plats."),
    ("Kan ett golv som blev vågigt vid en tidigare slipning rättas till?",
     "Ofta. Vågigheten kan komma från svikt i undergolvet eller från en felinställd maskin. Vi kontrollerar först om golvet sviktar, och därefter kan en ny grovslipning jämna till ytan."),
  ],
  "sources": [
    ("Stockholms stad – Områdesfakta 2025: Hässelby villastad (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-villastad.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Hässelby gård (pdf)", _OF + "vasterort/hasselby-vallingby/hasselby-gard.pdf"),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Hässelby gård (pdf)", _SSM.format("000086")),
    _GBR_SLIP, _GBR_SKILL, _GBR_OLJA, _SKV, _SKV2,
  ],
  "cta": ("Ska trägolvet i Hässelby slipas?", "Boka ett gratis platsbesök, så kontrollerar vi slitskikt och svikt och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Nyslipat och lackat furugolv i ett ljust rum i en äldre villa",
     "empty sunlit room on the upper floor of an older Swedish wooden villa, freshly sanded and clear-lacquered wide pine floorboards with a soft satin sheen, white painted wood panelling on the lower walls, white window with small panes, sloping ceiling, no furniture, no people, no text"),
    ("Fiskbensparkett i ek sedd ovanifrån",
     "top-down view of an oak herringbone parquet floor in a Swedish home where one half is freshly sanded pale bare wood and the other half still has the old worn yellowed lacquer, a straight clean boundary between the two areas, white skirting board along one edge, natural daylight, no people, no hands, no machines, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ENSKEDE
"golvlaggare-enskede.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Enskede", "svc_label": "Golvläggare",
  "title": "Golvläggare i Enskede – lut, såpa och olja på furugolvet",
  "description": "Golvläggare i Enskede: lutbehandling av fur- och grangolv, såpa eller olja som slutbehandling, olja i springor och rätt såpa till det oljade golvet.",
  "h1": "Golvläggare i Enskede",
  "lead": "Ett golv av fur eller gran behöver inte lackas. Lut, såpa och olja är äldre behandlingar som ger träet en annan ton och går att bättra på i ett gångstråk utan att hela rummet slipas om. Geal Entreprenad AB slipar och behandlar trägolv i Gamla Enskede, Enskededalen, Enskedefältet och Enskede gård, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Lut, såpa och olja på fur och gran.",
  "sections": [
    {"id": "enskede-omraden", "anchor": "Husen i Enskede",
     "h2": "Trädgårdsstäder från 1910- till 1930-talet",
     "paras": [
       "Stockholms stad köpte Enskede gård och drygt 600 hektar mark 1904. Enligt Stadsmuseets Stockholms Spår växte sedan den ena trädgårdsstaden efter den andra upp: Gamla Enskede, den första i sitt slag i landet, Enskededalen och Enskedefältet med sina småstugor. Enskededalens villor tillkom 1917–25 med den svenska småstaden som förebild, och merparten av villorna i Enskede gård byggdes under 1920- och 30-talen.",
       "Stadens områdesfakta för 2025 visar att husen fortfarande dominerar på flera håll. Gamla Enskede har 923 bostäder i småhus, Enskededalen 544, Enskede gård 430 och Enskedefältet 406, där nästan alla är äganderätter. Vilket trä golven i ditt hus är gjorda av ser vi först på plats, men står det fur eller gran under en gammal lack finns fler val än att lacka om.",
     ],
     "aside": None},
    {"id": "lut-enskede", "h2": "Vad luten gör med fur och gran",
     "paras": [
       "Golvbranschens riktlinjer för lutbehandling, LUT 22, beskriver traditionell lutning av homogena golv av fur och gran, och med extra försiktighet även lamellgolv. Lut består av natrium- och kaliumhydroxid i vattenlösning och är starkt frätande. Ett lutat golv tar emot pigment djupare och jämnare, och i kombination med vit olja bevaras träets ljushet. Lövträ kräver andra produkter och ingår inte i riktlinjerna.",
       "Eftersom luten fräter är skyddstäckningen viktig. Riktlinjerna varnar särskilt för skador på målade ytor, metall och lövträ, och den som lutar ska ha gummihandskar och skyddsglasögon. I ett hus med målade socklar, dörrfoder och trappor tejpar och täcker vi därför allt som gränsar mot golvet innan vi börjar. Ska snickerier lagas samtidigt, se " + _L.format("snickare-enskede.html", "snickare i Enskede") + ".",
     ],
     "aside": {"title": "Lutat golv i korthet", "items": [
       "Homogena golv av fur eller gran", "Hela planklängder åt gången",
       "Lut vått i vått", "Såpa, olja eller hårdvaxolja efteråt"]}},
    {"id": "lutning", "h2": "Så lutas golvet i ett rum",
     "paras": [
       "Golvet slipas först, så att den gamla ytbehandlingen är borta. Enligt LUT 22 arbetar man sedan i hela planklängder: man börjar längst in i ett hörn, lägger lut på ett par plankors bredd och arbetar sig bort till det andra hörnet, vänder och fortsätter tills man backar ut ur rummet. Luten ska läggas vått i vått för att undvika skarvar. Den ska röras om under arbetet, eftersom kalk och pigment annars sjunker till botten av kärlet.",
       "Efter ett dygn jämnas överskottet av kalk och pigment ut med ett skurblock eller en skurmaskin med röd rondell, och golvet dammsugs noga. Golvets fuktkvot bör då inte vara högre än tolv procent innan slutbehandlingen läggs på. Riktlinjerna rekommenderar inte lack ovanpå lut. Ett mindre prov på golvet visar vilken slutbehandling som ger det utseende du vill ha.",
     ],
     "aside": None},
    {"id": "sapa-olja", "h2": "Såpa eller olja som slutbehandling",
     "paras": [
       "Såpa är den traditionella slutbehandlingen och finns ofärgad eller med vitt pigment. Det krävs i regel tre till fyra omgångar innan golvet är mättat. Golvolja ger en sidenmatt yta, och en ofärgad olja kan ge träet en bärnstensfärgad ton som ljusnar något med tiden. Hårdvaxolja finns i flera glansgrader. Ett oljat golv har fördelen att det går att punktbättra, så att bara ett slitet gångstråk behöver underhållas.",
       "I ett äldre hus med springor mellan brädorna finns en risk som Golvbranschens riktlinjer för oljebehandling pekar ut: oljan kan rinna ned genom springor och kvisthål i bjälklagets fyllning. Trasor som har använts till olja ska ligga i vatten i minst ett dygn eller brännas direkt, eftersom de kan självantända. Till det dagliga underhållet anger riktlinjerna en återfettande golvsåpa med en fetthalt på 20–30 procent, som inte ska förväxlas med vanlig gul- eller grönsåpa.",
     ],
     "aside": {"title": "Underhåll av oljat golv", "items": [
       "Torra metoder i första hand", "Återfettande golvsåpa, inte grönsåpa",
       "Golvet torrt inom ett par minuter", "Gångstråk oljas oftare"]}},
    {"id": "enskede-rum", "h2": "Golvet i köket, badrummet och övriga rum",
     "paras": [
       "Ett lutat och såpat golv passar i torra rum. I köket kan en hårdare behandling vara klokare, och i badrummet är det tätskiktet under klinkern som gäller. Ska köket byggas om i samma veva finns mer under " + _L.format("koksrenovering-enskede.html", "köksrenovering i Enskede") + ", och om våtrummet under " + _L.format("badrumsrenovering-enskede.html", "badrumsrenovering i Enskede") + ". Allmänt om golvtyper och ytbehandlingar finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en lutbehandling till i Enskede",
  "steps": [
    ("Platsbesök", "Vi kontrollerar träslag, springor och tidigare behandling och bestämmer var ett prov ska göras."),
    ("Skriftligt kostnadsförslag", "Slipning, lutning och slutbehandling redovisas som egna poster."),
    ("Skyddstäckning", "Socklar, foder, trappor och metall täcks innan luten tas fram."),
    ("Slipning och lutning", "Golvet slipas till rent trä och lutas i hela planklängder."),
    ("Slutbehandling", "Såpa, olja eller hårdvaxolja läggs på i flera omgångar."),
    ("Skötselråd", "Du får råd om rätt såpa och om hur gångstråken underhålls."),
  ],
  "rot_h2": "ROT-avdrag för golvbehandlingen i Enskede",
  "rot": [
    "Skatteverket godkänner rotavdrag för att slipa och byta golv i ett småhus du äger. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och tillsammans med rutavdrag högst 75 000 kr.",
    "Lut, såpa, olja och resekostnader ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Enskede?",
  "price": [
    "Golvytan, hur mycket gammal lack som ska slipas bort och vilken slutbehandling du väljer avgör mest. Såpa kräver fler omgångar än olja. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Kan ett lackat furugolv i Enskede lutas och såpas i stället?",
     "Ja, om lacken först slipas bort helt. Grovslipningen tar bort all tidigare ytbehandling, och därefter kan golvet lutas och såpas eller oljas."),
    ("Varför rekommenderas inte lack ovanpå ett lutat golv?",
     "Golvbranschens riktlinjer för lutbehandling avråder från lack på lut och anger såpa, olja eller hårdvaxolja som slutbehandling. Vi gör ett prov innan hela ytan behandlas."),
    ("Hur många gånger behöver ett nylutat golv såpas?",
     "Enligt Golvbranschen krävs i regel tre till fyra omgångar såpa innan golvet är mättat."),
    ("Vilken såpa ska användas till ett oljat trägolv?",
     "En återfettande golvsåpa med en fetthalt på 20–30 procent. Golvbranschen påpekar att den inte ska förväxlas med vanlig gul- eller grönsåpa."),
    ("Kan golvolja rinna ner mellan brädorna i ett gammalt bjälklag?",
     "Ja. Golvbranschen varnar för att olja kan flyta ned i bjälklagets fyllning genom springor och kvisthål, så de behöver uppmärksammas innan oljan läggs på."),
  ],
  "sources": [
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Enskede gård (pdf)", _SSM.format("000016")),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Blåsut (pdf)", _SSM.format("000020")),
    ("Stockholms stad – Områdesfakta 2025: Gamla Enskede (pdf)", _OF + "soderort/enskede/gamla-enskede.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Enskededalen (pdf)", _OF + "soderort/skarpnack/enskededalen.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Enskedefältet (pdf)", _OF + "soderort/enskede/enskedefaltet.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Enskede gård (pdf)", _OF + "soderort/enskede/enskede-gard.pdf"),
    _GBR_SLIP, _GBR_LUT, _GBR_OLJA, _GBR_UND, _SKV, _SKV2,
  ],
  "cta": ("Vill du ge furugolvet i Enskede en ny yta?", "Boka ett gratis platsbesök, så tittar vi på träet och föreslår lut, såpa eller olja i ett skriftligt kostnadsförslag."),
  "img": [
    ("Lutat och såpat furugolv med vit ton i ett rum i en äldre villa",
     "empty bright room in an old Swedish 1920s garden-city villa, wide pine floorboards treated with white lye and soap giving a pale matte Scandinavian look, light grey painted wall panelling, white tiled stove in a corner, tall window with white frames and a view of an apple tree, soft daylight, no furniture, no people, no text"),
    ("Närbild på breda furubrädor med vit lutning och matt såpad yta",
     "close-up of wide old pine floorboards with visible knots and fine gaps between boards, treated with white lye and floor soap giving a pale whitish matte surface, warm wood grain showing through, soft side light, no people, no hands, no tools, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ ÄLVSJÖ
"golvlaggare-alvsjo.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Älvsjö", "svc_label": "Golvläggare",
  "title": "Golvläggare i Älvsjö – golvvärme under trägolv i villan",
  "description": "Golvläggare i Älvsjö: trägolv på golvvärme i äldre villor, högst 27 grader på ytan, golvvärme bredvid radiatorer och träbjälklag som ska isoleras.",
  "h1": "Golvläggare i Älvsjö",
  "lead": "Ett varmt golv i hallen eller köket är en vanlig önskan när en äldre villa renoveras. Under ett trägolv kräver golvvärmen dock rätt temperatur, rätt fuktskydd och ett bjälklag som håller värmen kvar. Geal Entreprenad AB lägger golv i Långbro, Herrängen, Långsjö och övriga Älvsjö, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Golvvärme under trägolv i äldre villor.",
  "sections": [
    {"id": "alvsjo-villor", "anchor": "Husen i Älvsjö",
     "h2": "Egnahem, småstugor och sommarhus kring Långsjön",
     "paras": [
       "Stadens parkplan för Herrängen och Långsjö berättar att John Edvard Lignell, som bodde på Örby slott, köpte Herrängens gård 1901 och började stycka av marken. Köparna var egnahemsbyggare, och det blev början på villastaden. Fram till 1910 fanns en viss villabebyggelse, men det var därefter som exploateringen tog fart med villor, småstugor och sommarhus.",
       "Områdesfakta för 2025 visar hur mycket av detta som står kvar: 1 423 bostäder i småhus i Långbro, 1 143 i Herrängen och 872 i Långsjö. Ett hus som byggdes för sommaren eller för radiatorer är sällan byggt med golvvärme i tankarna. Därför börjar vi med bjälklaget, inte med golvet.",
     ],
     "aside": None},
    {"id": "golvvarme-tra", "h2": "Trägolv på golvvärme: 27 grader är gränsen",
     "paras": [
       "Golvbranschens handbok Trägolv på golvvärme anger att yttemperaturen på ett trägolv inte får överstiga 27 °C, och att det gäller även under mattor och andra övertäckningar, där temperaturen blir högre än på resten av golvet. Golvvärmetillverkarna dimensionerar enligt handboken sina system för högst 26 °C vid golvytan. Blir golvet varmare finns risk för en forcerad uttorkning och bestående skador.",
       "Träslaget spelar roll. Lamellparkett av bok och kanadensisk lönn sväller och krymper mer än andra träslag, och i ett kallt och torrt klimat som det svenska anses de olämpliga på golvvärme. Massiva trägolv rör sig mer än lamellgolv, oavsett golvvärme, och handboken räknar med en krympning på ungefär en procent av brädans bredd vid 30–60 procent luftfuktighet. Breda brädor ger därför större springor på vintern än smala stavar.",
     ],
     "aside": {"title": "Välj golv för golvvärme", "items": [
       "Högst 27 °C på ytan", "Undvik bok och kanadensisk lönn",
       "Smala stavar ger mindre springor", "Luftfuktighet 30–60 %"]}},
    {"id": "radiatorer-alvsjo", "h2": "Golvvärme i ett rum och radiatorer i resten",
     "paras": [
       "I en äldre villa blir golvvärmen ofta ett tillägg till radiatorerna. Enligt handboken kräver nya radiatorer ungefär 55 °C när det är som kallast ute, och äldre radiatorsystem ännu mer, medan golvvärmen behöver ungefär 15 grader lägre. Står golvvärmen bara för en del av huset krävs därför i allmänhet en separat styrning av vattentemperaturen till de två systemen. Normal framledningstemperatur för golvvärme ligger enligt handboken på 30–40 °C.",
       "Väljs elektrisk golvvärme under trä- eller laminatgolv ska varje rum ha egen termostat, med en golvgivare som begränsar temperaturen. Golvvärmen får inte styras med enbart en rumsgivare, och golvytans effekt ska vara högst 75 watt per kvadratmeter. Behövs mer är det enligt handboken tilläggsisolering eller en kompletterande värmekälla som gäller. Ska köket få golvvärme finns mer under " + _L.format("koksrenovering-alvsjo.html", "köksrenovering i Älvsjö") + ".",
     ],
     "aside": None},
    {"id": "bjalklag-alvsjo", "h2": "Golvvärme i ett gammalt träbjälklag",
     "paras": [
       "Vid renovering är de lätta golvvärmesystemen vanligast, som läggs på eller i träbjälklaget. Handboken betonar att en värmebehovsberäkning är särskilt viktig i äldre hus och att möjligheten att tilläggsisolera bjälklaget bör undersökas. Isoleringen ska fylla hela bjälklagsfacket och ligga an mot golvvärmen, och det får inte finnas luftspalter mellan isolering och bjälkar. Vid ombyggnad kan en vindväv minska luftrörelserna som kyler isoleringen och slingorna.",
       "Trägolvet ska ha ett fuktskydd, till exempel en ångspärr, så nära golvet som möjligt. Det är obligatoriskt på golvvärme och på bjälklag över en ventilerad krypgrund. Ligger bjälklaget mot mark ska fuktförhållandena kartläggas och eventuella problem åtgärdas innan golvvärmen läggs in. Mer om hur golvet byggs upp i stort finns på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": {"title": "Inför golvvärme i en äldre villa", "items": [
       "Beräkna värmebehovet", "Isolering utan luftspalter",
       "Ångspärr nära trägolvet", "Golvgivare som begränsning"]}},
    {"id": "stavslapp-alvsjo", "h2": "Parkett som redan ligger på golvvärme",
     "paras": [
       "Ligger det redan en lamellparkett på golvvärme och den ska slipas om, finns en risk som Golvbranschen beskriver som stavsläpp: slitskiktet lossnar från skiktet under. Det kan bero på att limfogen har blivit spröd med åren och på för stora fuktrörelser, och vibrationerna från slipningen kan få en försvagad limfog att brista. Branschen rekommenderar 15–25 °C och 30–60 procent luftfuktighet, och med golvvärme högst 27 °C på ytan.",
       "Det finns inget sätt att i förväg veta om ett golv kommer att släppa, och det kan hända flera månader efter en renovering. Några enstaka stavar kan oftast limmas tillbaka. Vi berättar om risken innan vi slipar en lamellparkett, så att du kan väga en slipning mot ett nytt golv.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så planerar vi golv och golvvärme i Älvsjö",
  "steps": [
    ("Platsbesök", "Vi tittar på bjälklag, värmesystem och nuvarande golv och frågar vilka rum som ska bli varma."),
    ("Värmebehov och val", "Vi går igenom golvvärmens typ, styrning och träslag innan något beställs."),
    ("Skriftligt kostnadsförslag", "Isolering, golvvärme, fuktskydd och golv redovisas som egna poster."),
    ("Bjälklaget", "Gamla skikt tas bort och bjälklaget isoleras och förbereds."),
    ("Läggning", "Golvvärme, ångspärr och trägolv läggs vid rätt rumsklimat."),
    ("Start", "Golvvärmen startas enligt tillverkarens anvisningar och du får skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för golvet i Älvsjö",
  "rot": [
    "Skatteverket ger rotavdrag för att slipa och byta golv i en bostad du äger, även ett fritidshus. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och rot och rut får tillsammans vara högst 75 000 kr.",
    "Material, som golvvärmeslingor och golvbrädor, ger inget avdrag, och det gör inte heller resorna. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad styr kostnaden i Älvsjö?",
  "price": [
    "Mest påverkar om bjälklaget behöver isoleras, vilken golvvärme som väljs och hur stor golvytan är. Elarbetet för en elektrisk golvvärme är en egen post. Platsbesöket är gratis och kostnadsförslaget skriftligt.",
  ],
  "faq": [
    ("Hur varmt får trägolvet bli med golvvärme i vår villa i Älvsjö?",
     "Golvbranschen anger högst 27 °C på ytan, även under mattor där temperaturen blir högre än på resten av golvet."),
    ("Passar ett bokgolv ovanpå golvvärme?",
     "Golvbranschens handbok anser lamellparkett av bok och kanadensisk lönn olämplig på golvvärme i svenskt klimat, eftersom de träslagen sväller och krymper mer än andra."),
    ("Kan golvvärmen i hallen gå på samma vattentemperatur som radiatorerna?",
     "I allmänhet inte. Radiatorer behöver betydligt varmare vatten än golvvärme, så handboken anger att det krävs separat styrning av vattentemperaturen till de två systemen."),
    ("Varför räcker det inte med en rumsgivare för elektrisk golvvärme under parkett?",
     "Golvbranschen anger att trä- och laminatgolv ska styras med rumsgivare och en golvgivare som begränsar temperaturen. Enbart rumsgivare kan låta golvet bli för varmt."),
    ("Kan lamellparketten släppa när den slipas om på golvvärme?",
     "Det kan hända. Golvbranschen skriver att stavsläpp inte går att förutse och kan uppstå även månader efter slipningen. Vi tar upp risken innan arbetet börjar."),
  ],
  "sources": [
    ("Stockholms stad – Parkplan Älvsjö del 2: Herrängen, Långsjö (pdf)",
     "https://start.stockholm/globalassets/start/om-stockholms-stad/sa-arbetar-staden/natur-parker-och-gronomraden/parkplan-alvsjo-del-2---herrangen-langsjo-parker-och-natur.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Långbro (pdf)", _OF + "soderort/hagersten/langbro.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Herrängen (pdf)", _OF + "soderort/hagersten/herrangen.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Långsjö (pdf)", _OF + "soderort/hagersten/langsjo.pdf"),
    _GBR_TGV, _GBR_STAV, _SKV, _SKV2,
  ],
  "cta": ("Vill du ha golvvärme under trägolvet i Älvsjö?", "Boka ett gratis platsbesök, så går vi igenom bjälklag, värmesystem och golvval och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Hall i en äldre villa med nytt ekgolv och ljusa väggar",
     "empty entrance hall of an older Swedish wooden villa from the 1910s, newly laid narrow light oak floorboards, white painted panelled door, light warm grey walls, a white radiator under a small window, staircase with white balusters in the background, soft daylight, no furniture, no people, no text"),
    ("Stor lokal med nylagt ljust golv",
     "low angle close-up of a newly laid light oak plank floor in an older Swedish villa, a thin flat-woven striped wool rug lying flat on part of the floor, warm sunlight from a window falling across boards and rug, white skirting board and lower part of a white panelled wall, no furniture, no people, no hands, no text"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ SPÅNGA
"golvlaggare-spanga.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Spånga", "svc_label": "Golvläggare",
  "title": "Golvläggare i Spånga – parkett, fanér eller laminat?",
  "description": "Golvläggare i Spånga: så skiljer du massivt trä, lamellparkett, fanér och laminat åt, vad som går att slipa och varför ett flytande golv knarrar.",
  "h1": "Golvläggare i Spånga",
  "lead": "Fyra golv kan se nästan likadana ut i ett rum men kräva helt olika åtgärder när de blir slitna. Ett av dem går utmärkt att slipa, ett annat inte alls. Geal Entreprenad AB lägger nya golv och renoverar gamla i Solhem, Bromsten, Flysta och Sundby, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Massivt, lamell, fanér eller laminat.",
  "sections": [
    {"id": "spanga-smahus", "anchor": "Husen i Spånga",
     "h2": "Över 4 300 småhusbostäder i fyra stadsdelar",
     "paras": [
       "Stockholms stads områdesfakta för 2025 räknar 2 038 bostäder i småhus i Solhem, och 1 946 av dem är äganderätter. Bromsten har 1 066, Flysta 663 och Sundby 559. I Flysta ligger fyra av fem bostäder i småhus. Sammantaget är det över 4 300 villor och radhus i de fyra stadsdelarna.",
       "I hus som har renoverats i omgångar är det vanligt att rummen har olika golv: ett ursprungligt trägolv i ett rum, en parkett från en senare renovering i ett annat och kanske ett klickgolv i en tillbyggnad. Innan vi föreslår slipning eller ett nytt golv tar vi reda på vilken sorts golv som ligger i varje rum.",
     ],
     "aside": None},
    {"id": "fyra-golv", "h2": "Fyra golv som liknar varandra",
     "paras": [
       "Golvbranschen skiljer på fyra vanliga typer. Ett massivt trägolv består av samma träslag rakt igenom, till exempel brädor, kortstavsparkett eller mosaikparkett, och går därför utmärkt att slipa. Lamellparkett, eller flerskiktsparkett, är oftast byggd i tre skikt med fiberriktningen vinkelrätt mot varandra, vilket minskar golvets rörelser. Slitskiktet överst är minst 2,5 millimeter, och golvet går att slipa.",
       "Ett fanérgolv har också ett ytskikt av trä, men det är tunnare än 2,5 millimeter och i regel ungefär en millimeter. Eftersom ungefär en millimeter försvinner vid en slipning går det normalt inte att slipa om. Ett laminatgolv har en kärna av träfiberskiva och ett ytskikt med tryckt dekor, ofta av plast. Det kan varken slipas, oljas eller lackas om, och enligt Golvbranschen ska det inte heller behandlas med polish eller vax.",
     ],
     "aside": {"title": "Så skiljer du dem åt", "items": [
       "Massivt: samma trä rakt igenom", "Lamellparkett: slitskikt minst 2,5 mm",
       "Fanér: cirka 1 mm trä", "Laminat: tryckt dekor"]}},
    {"id": "slipa-inte", "h2": "När golvet inte går att slipa",
     "paras": [
       "Ett slitet fanér- eller laminatgolv byts i stället för att slipas. Är ytan lackad kan den enligt Golvbranschen fräschas upp med en så kallad refresher enligt tillverkarens anvisning, och ett lackat laminatgolv sköts som ett lackat trägolv. Är golvet ett naturoljat fanérgolv går det lättare att punktbättra än andra ytbehandlingar.",
       "Fanérgolvets låga bygghöjd, oftast 7–8,5 millimeter, gör det enligt Golvbranschen lämpligt som renoveringsgolv. Laminat finns från 6 till 12 millimeter, och vissa har ett stegljudsdämpande skikt redan från fabriken. Båda typerna är träbaserade och sväller och krymper med luftfuktigheten. De mår bäst vid 30–60 procent luftfuktighet och är avsedda för torra utrymmen. Vill du hellre ha ett golv som kan slipas i framtiden är massivt trä eller lamellparkett rätt val.",
     ],
     "aside": None},
    {"id": "knarr-spanga", "h2": "Knarr i ett flytande golv",
     "paras": [
       "Golvbranschen skiljer på två slags ljud. Enstaka knäppningar som hörs när man går över golvet men inte när man strax går tillbaka samma väg kallas spänningsljud och räknas som en naturlig del av ett trägolv. Knarr som hörs varje gång golvet belastas, över en större yta eller i gångstråken, räknas däremot som ett fel.",
       "Orsakerna kan enligt branschen vara ett ojämnt undergolv, ett för mjukt mellanlägg av foam eller liknande, eller att golvet sitter i spänn för att rörelsefogen mot väggar eller fast inredning är för liten. Hög luftfuktighet kan få brädorna att svälla och gnida mot varandra, och ibland är det fel i själva golvet, till exempel en felfräst profil. Därför kontrollerar vi planheten och lämnar en rörelsefog runt hela golvet, även mot köksskåp och trappor. Ska köket byggas om, se " + _L.format("koksrenovering-spanga.html", "köksrenovering i Spånga") + ".",
     ],
     "aside": {"title": "Vanliga orsaker till knarr", "items": [
       "Ojämnt undergolv", "För mjukt mellanlägg",
       "För liten rörelsefog", "Hög luftfuktighet"]}},
    {"id": "spanga-val", "h2": "Golv efter rum och planer",
     "paras": [
       "I vardagsrum och sovrum där golvet ska hålla länge brukar vi föreslå ett golv som går att slipa. I en tillbyggnad där bygghöjden är knapp kan ett tunnare golv vara lösningen. Ska väggar och lister målas om samtidigt finns mer under " + _L.format("malare-spanga.html", "målare i Spånga") + ", och om golvtyper och ytbehandlingar på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går ett golvbyte till i Spånga",
  "steps": [
    ("Platsbesök", "Vi tar reda på vilket golv som ligger i varje rum och om det går att slipa."),
    ("Val av golv", "Vi går igenom bygghöjd, rum och slitage och föreslår golvtyp."),
    ("Skriftligt kostnadsförslag", "Rivning, underlag och nytt golv redovisas som egna poster."),
    ("Underlaget", "Det gamla golvet tas bort eller underlaget riktas så att det blir plant."),
    ("Läggning", "Mellanlägg och golv läggs med rörelsefog mot väggar och fast inredning."),
    ("Avslut", "Lister och trösklar sätts tillbaka och du får skötselråd för golvtypen."),
  ],
  "rot_h2": "ROT-avdrag för golvet i Spånga",
  "rot": [
    "Skatteverket räknar det som rotarbete att slipa och byta golv i ett småhus du äger och bor i. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och högst 75 000 kr tillsammans med rutavdrag.",
    "Själva golvet och resorna ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Spånga?",
  "price": [
    "Golvytan, vilken golvtyp du väljer och hur mycket undergolvet behöver riktas avgör mest. Ett golv som kan slipas i stället för att bytas blir ofta en mindre insats. Du får ett skriftligt kostnadsförslag efter ett gratis platsbesök.",
  ],
  "faq": [
    ("Hur ser vi om golvet i vår villa i Spånga är fanér eller parkett?",
     "På tjockleken på träskiktet överst. Ett fanérgolv har ungefär en millimeter trä, en lamellparkett minst 2,5 millimeter. Vi kontrollerar det i en springa eller vid en tröskel."),
    ("Går det att olja om ett laminatgolv som har blivit matt?",
     "Nej. Golvbranschen skriver att laminat inte kan slipas, oljas eller lackas om, och att det inte heller ska behandlas med polish eller vax."),
    ("Är det fel på golvet om det knäpper till ibland när man går över det?",
     "Inte nödvändigtvis. Enstaka spänningsljud räknas som normalt för ett trägolv. Knarr som hörs varje gång golvet belastas räknas däremot som ett fel."),
    ("Varför ska det vara en springa mellan det flytande golvet och väggen?",
     "Trägolv sväller och krymper med luftfuktigheten. Är rörelsefogen mot väggar och fast inredning för liten kan golvet hamna i spänn och knarra."),
    ("Kan ett fanérgolv läggas ovanpå det gamla golvet?",
     "Ofta. Golvbranschen nämner fanérgolvets låga bygghöjd som en fördel vid renovering. Underlaget måste vara plant, och höjden vid dörrar och trösklar behöver kontrolleras."),
  ],
  "sources": [
    ("Stockholms stad – Områdesfakta 2025: Solhem (pdf)", _OF + "vasterort/jarva/solhem.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Bromsten (pdf)", _OF + "vasterort/jarva/bromsten.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Flysta (pdf)", _OF + "vasterort/jarva/flysta.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Sundby (pdf)", _OF + "vasterort/jarva/sundby.pdf"),
    _GBR_SKILL, _GBR_FANER, _GBR_LAM, _GBR_KNARR, _SKV, _SKV2,
  ],
  "cta": ("Vet du vilket golv som ligger i huset i Spånga?", "Boka ett gratis platsbesök, så tar vi reda på det och föreslår slipning eller nytt golv i ett skriftligt kostnadsförslag."),
  "img": [
    ("Vardagsrum i en villa med nylagd lamellparkett i ek",
     "empty bright living room in a Swedish 1950s wooden villa, newly laid three-strip oak parquet floor with a matte lacquer, white walls, white skirting boards, wide window overlooking a garden with fruit trees, soft daylight, no furniture, no people, no text"),
    ("Golvprover i olika uppbyggnad med kanterna synliga",
     "close-up side view of four floor board samples lying next to each other on a wooden table, showing their edges and layers: solid oak board, three-layer oak parquet with a thick top layer, thin wood veneer floor on fibreboard core, and laminate with printed wood decor on fibreboard, natural daylight, no people, no hands, no text, no labels"),
  ],
  "related": [],
},

# ------------------------------------------------------------------ FARSTA
"golvlaggare-farsta.html": {
  "kind": "district", "service": "golvlaggning", "ort": "Farsta", "svc_label": "Golvläggare",
  "title": "Golvläggare i Farsta – linoleum, plastgolv och klinker",
  "description": "Golvläggare i Farsta: linoleum och plastgolv i småstugan, renovering av en sliten matta i stället för byte, gummigolv i hallen och klinker på träbjälklag.",
  "h1": "Golvläggare i Farsta",
  "lead": "I en liten stuga betyder golvet i hall och kök mycket, eftersom det är där alla går. Linoleum, plastgolv och gummi tål slitage, och en gammal matta kan ibland renoveras i stället för att rivas. Geal Entreprenad AB lägger och renoverar golv i Tallkrogen, Svedmyra, Sköndal, Gubbängen och övriga Farsta, med gratis platsbesök, skriftligt kostnadsförslag och ROT-avdraget direkt på fakturan.",
  "card": "Linoleum, plastgolv och klinker i småstugan.",
  "sections": [
    {"id": "farsta-stugor", "anchor": "Husen i Farsta",
     "h2": "Småstugor byggda av färdiga delar",
     "paras": [
       "Svedmyra byggdes enligt Stadsmuseets Stockholms Spår ut med småstugor med början 1931–33. Självbyggarna fick ett förmånligt lån och betalade resten med eget arbete, och Småstugebyrån stod för instruktioner och byggmaterial. Materialet var monteringsfärdigt, och väggar och takstolar lyftes på plats i stora element. Tallkrogen byggdes från 1933, och även där levererades byggnadsdelarna färdiga från fabriken.",
       "Stadens områdesfakta för 2025 räknar 945 bostäder i småhus i Tallkrogen, 359 i Svedmyra och 1 595 i Sköndal. I små rum med mycket slitage är golvmaterialet ett praktiskt val lika mycket som ett utseendeval, och det är där halvhårda golv som linoleum, plast och gummi kommer in.",
     ],
     "aside": None},
    {"id": "linoleum-farsta", "anchor": "Linoleum",
     "h2": "Linoleum: linolja, trämjöl och kalksten",
     "paras": [
       "Ordet linoleum kommer av linolja. Enligt Golvbranschen består bindemedlet av vegetabiliska oljor som linolja och tallolja med träharts, och det härdar när det reagerar med luftens syre. Fyllmedlet är trämjöl, ibland korkmjöl, och kalkstensmjöl. Mönstret går genom hela slitskiktet. Mattorna tillverkas oftast på en bärare av juteväv, i två meters bredd och två till fyra millimeters tjocklek, och plattor finns bland annat i 500 × 500 millimeter.",
       "Linoleum tål nötning och repor men inte ständig väta, och det ska inte läggas i våta utrymmen. En ny matta kan ha en gul ton, så kallad oxidationsgulning, som enligt branschen försvinner helt efter några dygn i dagsljus. Ett färgprov bör därför bedömas först när det har legat i dagsljus. För den som vill dämpa stegljud finns linoleum med ett skikt av korkbaserad linoleum eller med en baksida av plastskum.",
     ],
     "aside": {"title": "Linoleum i korthet", "items": [
       "Linolja, trämjöl och kalksten", "Mönster genom hela skiktet",
       "Inte i våtrum", "Gul ton som försvinner i dagsljus"]}},
    {"id": "renovera-matta", "h2": "Renovera en sliten matta i stället för att byta",
     "paras": [
       "Golvbranschens riktlinjer RENOV. 24 beskriver hur halvhårda golv av PVC, linoleum och gummi kan renoveras i torra utrymmen. Först kontrolleras vilken matta det är, vilken ytbehandling eller polish som finns på ytan och vad du förväntar dig av resultatet. Riktlinjerna påpekar att ett golv i dåligt skick ibland behöver en täckande färg för att dölja skador, och att en transparent lack då inte räcker.",
       "Polishen löses med en tvättlösning som får verka i ungefär en kvart, och golvet våtslipas. Därefter nollställs golvet genom att tvättas minst två gånger med rent vatten, och efter en lätt torrslipning läggs ytbehandlingen på. Ett linoleumgolv ska grundas med en grundlack, och oftast behövs två omgångar färg och två omgångar lack, eller bara två omgångar lack om ytan ska vara transparent. Uppvik och socklar ingår normalt inte om det inte har avtalats.",
     ],
     "aside": {"title": "Renovering av halvhårt golv", "items": [
       "Polishen löses och slipas bort", "Golvet tvättas med rent vatten",
       "Grundlack på linoleum", "Färg och lack i två omgångar"]}},
    {"id": "plast-gummi", "h2": "Plastgolv utan PVC och gummi i hallen",
     "paras": [
       "Det finns plastgolv som inte innehåller PVC, tillverkade av till exempel polyolefin eller polyeten. Enligt Golvbranschen har de oftast ett ytskydd av akrylat, och då behövs inget vax eller polish. Mattorna är två millimeter tjocka och kan vikas upp på väggen. Gummigolv har hög slitstyrka, bestående elasticitet och god stegljudsdämpning, och finns i rullar på två till fyra millimeter eller som plattor upp till nio millimeter.",
       "Ett gummigolv levereras oftast med en skyddsyta som tas bort vid byggstädningen. I en hall där grus och väta kommer in från trädgården kan ett tåligt golv vara värt mer än ett varmt. Ska plastmattan i ett våtrum bytas gäller branschens regler för våtrum, och mer om det finns på sidan om " + _L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
     ],
     "aside": None},
    {"id": "klinker-farsta", "h2": "Klinker i hallen på ett träbjälklag",
     "paras": [
       "Keramiska plattor är tyngre än de flesta andra golvmaterial. Golvbranschen skriver att underlaget måste vara tillräckligt bärande och att det i vissa fall behöver förstärkas. Klinker har en låg vattenabsorption, vanligen 0–6 procent, och granitkeramik högst 0,5 procent. Granitkeramik är frostbeständig och kan därför läggas även utomhus, till exempel på trappan utanför entrén.",
       "Läggs golvvärme under klinkern får värmen enligt branschen slås på tidigast efter 28 dygn och sedan höjas med 3 °C per dygn. Terrakottaplattor är porösa och ska inte läggas på ett underlag med risk för fukt underifrån, och inte heller i kök där fett kan ge fläckar. Ska taket ses över i samma veva finns mer under " + _L.format("taklaggare-farsta.html", "takläggare i Farsta") + ", och om golvtyper i stort på sidan om " + _L.format("golvlaggning.html", "golvläggning") + ".",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går golvarbetet till i Farsta",
  "steps": [
    ("Platsbesök", "Vi tar reda på vilken matta som ligger, hur den har skötts och vad underlaget tål."),
    ("Renovera eller byta", "Vi går igenom om mattan kan renoveras eller om ett nytt golv är bättre."),
    ("Skriftligt kostnadsförslag", "Renovering, rivning, underlag och nytt golv redovisas var för sig."),
    ("Förarbete", "Polish tas bort eller den gamla mattan rivs och underlaget lagas."),
    ("Läggning eller ytbehandling", "Nytt golv läggs, eller den gamla mattan får färg och lack."),
    ("Skötselråd", "Du får råd om städning och underhåll för just din golvtyp."),
  ],
  "rot_h2": "ROT-avdrag för golvet i Farsta",
  "rot": [
    "Att slipa och byta golv i ett småhus du äger ger rotavdrag enligt Skatteverket. Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och rot och rut får tillsammans vara högst 75 000 kr.",
    "Mattor, plattor, lack och resekostnader ger inget avdrag. Geal drar avdraget direkt på fakturan.",
  ],
  "price_h2": "Vad påverkar priset i Farsta?",
  "price": [
    "Golvytan, om den gamla mattan kan renoveras eller måste rivas och hur mycket underlaget behöver lagas avgör mest. Klinker på träbjälklag kan kräva förstärkning. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag.",
  ],
  "faq": [
    ("Går det att få linoleummattan i vår småstuga i Tallkrogen fin igen utan att byta den?",
     "Ofta. Golvbranschens riktlinjer beskriver hur polishen tas bort, golvet våtslipas och får ny grundlack, färg och lack. Är mattan mycket skadad kan det behövas en täckande färg."),
    ("Varför ser den nya linoleummattan lite gul ut?",
     "Det kallas oxidationsgulning. Golvbranschen skriver att den försvinner helt efter några dygn i dagsljus."),
    ("Kan linoleum läggas i tvättstugan eller badrummet?",
     "Nej. Linoleum tål inte ständig väta och ska enligt Golvbranschen inte läggas i våta utrymmen."),
    ("Bär ett gammalt träbjälklag klinker i hallen?",
     "Det beror på bjälklaget. Keramik är tyngre än de flesta golvmaterial, och Golvbranschen skriver att underlaget ibland behöver förstärkas. Vi bedömer det på plats."),
    ("När får golvvärmen under den nya klinkern slås på?",
     "Enligt Golvbranschen tidigast efter 28 dygn, och sedan ska temperaturen höjas med 3 °C per dygn."),
  ],
  "sources": [
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Svedmyra (pdf)", _SSM.format("000043")),
    ("Stockholmskällan – Stadsmuseet, Stockholms Spår: Tallkrogen (pdf)", _SSM.format("000041")),
    ("Stockholms stad – Områdesfakta 2025: Tallkrogen (pdf)", _OF + "soderort/farsta/tallkrogen.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Svedmyra (pdf)", _OF + "soderort/farsta/svedmyra.pdf"),
    ("Stockholms stad – Områdesfakta 2025: Sköndal (pdf)", _OF + "soderort/farsta/skondal.pdf"),
    _GBR_LINO, _GBR_RENOV, _GBR_PLAST, _GBR_GUMMI, _GBR_KER, _SKV, _SKV2,
  ],
  "cta": ("Ska golvet i hallen eller köket i Farsta bytas eller renoveras?", "Boka ett gratis platsbesök, så går vi igenom mattan och underlaget och lämnar ett skriftligt kostnadsförslag."),
  "img": [
    ("Kök i en småstuga med nylagt linoleumgolv i varm gul ton",
     "small bright kitchen in a Swedish 1930s wooden cottage, newly laid seamless sheet linoleum floor in a matte warm ochre colour with a subtle fine marbled pattern, no tiles and no grout lines, simple white painted wooden kitchen cabinets with a wooden worktop, small window with white frame and a view of a garden, soft daylight, clean and empty, no shelves, no decorations, no signs, no chalkboard, no people, no text"),
    ("Hall med gråa klinkerplattor och en ljus trädörr",
     "small entrance hall in a Swedish 1930s wooden cottage with a newly laid floor of matte grey granite ceramic tiles with narrow joints, white painted wooden front door with a small window, white wall panelling, a simple wooden bench, soft daylight, no people, no shoes, no text"),
  ],
  "related": [],
},

}
