# -*- coding: utf-8 -*-
"""Tjänstehubbar badrumsrenovering.html och koksrenovering.html (tjänster v1, 2026-10-25).
Fakta endast från källorna i respektive "sources" (öppnade 2026-10-25):
GVK (zoner, fall, golvbrunnar före 1990, våtrumsanmälan/våtrumsintyg), Byggkeramikrådet (BBV,
behörighet, golvvärme), Säker Vatten (intyg, branschlegitimation, råd för bostadsrätt),
Boverket (vattentätt skikt, anmälningsplikt), Elsäkerhetsverket, Skatteverket (rot),
riksdagen.se (bostadsrättslagen 7 kap. 7 §). Inga påståenden om Geal utöver det sajten anger."""

GVK_KVAL = "https://www.gvk.se/branschregler/kvalitetsdokument/"
GVK_FORE = "https://www.gvk.se/kvalitetsarbete/gvks-kvalitetsarbete/fore-arbetets-utforande/"
GVK_EFTER = "https://www.gvk.se/kvalitetsarbete/gvks-kvalitetsarbete/efter-arbetets-utforande/"
GVK_LUTN = "https://www.gvk.se/branschregler/golv/golvlutning/"
GVK_ZON = "https://www.gvk.se/branschregler/vatzoner/"
GVK_BRUNN = "https://www.gvk.se/branschregler/golvbrunn/gamla-golvbrunnar/"
GVK_EL = "https://www.gvk.se/branschregler/elgenomforing-i-badrum/"
BKR_BEH = "https://www.bkr.se/om-behorighet"
BKR_FAQ = "https://www.bkr.se/vanliga-fragor"
SV_KONS = "https://sakervatten.se/bygga-ratt/konsumenter/"
BOV_FUKT = "https://www.boverket.se/sv/PBL-kunskapsbanken/regler-om-byggande/hygien-halsa-och-miljo/fuktsakerhet/"
BOV_ANM = "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/anmalan/"
ESV = "https://www.elsakerhetsverket.se/privatpersoner/anlita-ett-elinstallationsforetag"
SKV_ROT = "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html"
SKV_GODK = "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/gerarbetetratttillrotavdrag.106.5c1163881590be297b5899d.html"
SKV_ROTRUT = "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete.4.2e56d4ba1202f95012080002966.html"
KTJL = "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/konsumenttjanstlag-1985716_sfs-1985-716/"
BRL = "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bostadsrattslag-1991614_sfs-1991-614/"


def ext(url, text):
    return f'<a class="text-link" href="{url}" rel="noopener">{text}</a>'


def lnk(href, text):
    return f'<a class="text-link" href="{href}">{text}</a>'


PAGES_TJ = {
# ---------------------------------------------------------------- BADRUM
"badrumsrenovering.html": {
  "kind": "hub", "service": "badrumsrenovering", "svc_label": "Badrumsrenovering",
  "title": "Badrumsrenovering i Stockholm – tätskikt, fall och intyg",
  "description": "Badrumsrenovering i Stockholm: tätskikt enligt branschregler, fall mot golvbrunn, el och VVS, intygen du ska få och ROT. Gratis platsbesök.",
  "h1": "Badrumsrenovering i Stockholm",
  "lead": "Ett nytt badrum står och faller med tätskiktet, fallet mot golvbrunnen och papperen du får när jobbet är klart. Geal Entreprenad AB renoverar badrum i villor, radhus och bostadsrätter i hela Stockholm med en kontakt för rivning, våtrum, el, VVS och plattsättning. Du får ett gratis platsbesök och ett skriftligt kostnadsförslag innan något rivs.",
  "card": "Tätskikt, golvbrunn, el, VVS och intyg.",
  "sections": [
    {"id": "tatskikt", "anchor": "Tätskikt och regler",
     "h2": "Det viktigaste i badrummet syns inte när det är klart",
     "paras": [
       "Kakel, klinker och plastmatta är ytskikt. Det som skyddar huset mot vatten är tätskiktet under, och anslutningarna mot golvbrunn, rör och dörröppning. Enligt " + ext(BOV_FUKT, "Boverkets byggregler om fuktsäkerhet") + " ska ytor inomhus som kan väntas få vatten på sig ha ett vattentätt skikt, om det inte är obehövligt. Skiktet ska vara tätt även i skarvar, anslutningar och genomföringar, och i ytor med mycket vatten, som golvet i en dusch, ska antalet genomföringar begränsas. I rum med dusch ställer reglerna dessutom krav på golvavlopp och på att vattnet kan rinna dit.",
       "BBR säger vad resultatet ska klara. Hur det görs i praktiken står i branschreglerna: GVK:s regler för våtrum, Byggkeramikrådets regler för våtrum med keramik (BBV) och Säker Vattens regler för VVS-installationer. Regelverken gäller olika delar av samma rum, och försäkringsbolagen har enligt GVK och Säker Vatten i regel som villkor att gällande branschregler har följts när ett våtrum byggts. Ett badrum som avviker från reglerna kan alltså bli en försäkringsfråga den dag något läcker.",
       "Byggkeramikrådet beskriver att ett " + ext(BKR_BEH, "behörigt plattsättningsföretag") + " är utbildat i BBV, använder godkända tätskiktssystem och får utfärda rådets kvalitetsdokument. Hos GVK är motsvarigheten ett auktoriserat företag som anmäler våtrummet till GVK:s stickprovskontroller. Fråga den du anlitar vilket regelverk tätskiktet byggs efter och vem som utför det – det ska stå i offerten.",
     ],
     "aside": {"title": "Regelverken i ett badrum", "items": [
       "Boverkets byggregler: krav på vattentätt skikt och golvavlopp.",
       "GVK: branschregler för tätskikt i våtrum.",
       "Byggkeramikrådet (BBV): våtrum med kakel och klinker.",
       "Säker Vatten: rör, golvbrunn och VVS-installationer.",
     ]}},
    {"id": "golvbrunn", "h2": "Fall mot golvbrunnen och en brunn i rätt ålder",
     "paras": [
       "GVK delar in " + ext(GVK_ZON, "våtrummet i zoner") + ": plats för bad eller dusch, våtzon 1 och våtzon 2. Kraven på tätskiktet är högst där vattnet träffar mest. Vid duschplatsen ska golvet enligt " + ext(GVK_LUTN, "GVK:s regler om golvlutning") + " luta mot brunnen inom intervallet 1:150 till 1:50, i genomsnitt omkring 13 millimeter per meter. Lutningen gäller både underlaget för tätskiktet och det färdiga ytskiktet, och tätskiktets uppvik vid dörren ska ligga minst 20 millimeter över brunnens fläns så att vatten inte rinner ut i hallen.",
       "Byggkeramikrådet tillåter ett plant golv utan tröskel in till badrummet, men tätskiktet ska ändå vikas upp vid dörröppningen. Att lägga nytt kakel ovanpå gammalt kan enligt rådet fungera för en kosmetisk förändring om väggen bär den dubbla vikten och materialtillverkaren godkänner det, men ett felaktigt fall rättas inte till på det sättet – lutningen mot avloppet måste finnas redan i underlaget.",
       "Golvbrunnen är en vanlig fråga vid renovering. Enligt " + ext(GVK_BRUNN, "GVK om gamla golvbrunnar") + " ska en brunn som är äldre än 1990 bytas för att reglerna ska följas, och samma regel finns hos Säker Vatten. En nyare brunn kan behållas om den är i gott skick och fixerad enligt dagens monteringsanvisningar. Går åldern inte att fastställa rekommenderar GVK byte. Har badrummet inte renoverats sedan huset byggdes är byggåret en bra ledtråd: är huset från före 1990 ska brunnen alltså bytas.",
     ],
     "aside": None},
    {"id": "el-vvs", "h2": "El, rör och golvvärme i våtrummet",
     "paras": [
       "Elinstallationer som du inte får göra själv ska enligt " + ext(ESV, "Elsäkerhetsverket") + " utföras av ett registrerat elinstallationsföretag, och registreringen kan du kontrollera. GVK skriver att el i våtrum ska planeras i samråd med elinstallatören, eftersom placeringen av dosor och genomföringar avgör om tätskiktet kan anslutas tätt. Byggkeramikrådet ställer högre krav på elgenomföringar i själva duschplatsen än i resten av rummet.",
       "För rör och golvbrunn gäller Säker Vattens branschregler. Säker Vatten anger att ett " + ext(SV_KONS, "auktoriserat VVS-företag") + " ska lämna ett intyg efter arbetet där omfattning och eventuella avvikelser framgår, och att montörerna ska kunna visa branschlegitimation. Hos Geal utförs el och VVS av behöriga installatörer, och det framgår av kostnadsförslaget vem som gör vad.",
       "Golvvärme ska enligt Byggkeramikrådet ligga under tätskiktet, och dess placering ska dokumenteras så att ingen borrar i slingorna när en toalett monteras senare. Värmen får inte slås på förrän tidigast 28 dygn efter plattsättningen och ska sedan höjas långsamt. Det är en detalj som påverkar när badrummet kan användas fullt ut.",
     ],
     "aside": None},
    {"id": "dokumentation", "h2": "Papperen du ska ha när badrummet är klart",
     "paras": [
       "Ett badrum som är rätt byggt men saknar dokumentation är svårt att visa upp vid en försäkringsskada eller en husförsäljning. GVK beskriver i sina " + ext(GVK_KVAL, "kvalitetsdokument") + " att ett auktoriserat företag anmäler tätskiktsarbetet och lämnar en kopia av våtrumsanmälan till beställaren. Enligt " + ext(GVK_FORE, "GVK:s råd inför arbetet") + " bör du begära den kopian innan jobbet startar. Avviker underlaget från reglerna ska det noteras i en avvikelserapport från förkontrollen.",
       "Har du anlitat ett GVK-auktoriserat företag ska du som konsument enligt GVK få ett våtrumsintyg när arbetet är klart. Byggkeramikrådets kvalitetsdokument fyller samma funktion för våtrum med keramik, men gäller inte för väggpartier som är målade i stället för kaklade. Från VVS-installatören ska du få Säker Vattens intyg. " + ext(GVK_EFTER, "GVK:s råd efter arbetet") + " är att också spara monteringsanvisningar och produktblad för tätskiktet, skötselråd för ytskikten, fotodokumentation och slutfakturan, och att notera vilken utgåva av branschreglerna rummet är byggt efter.",
       "Enligt " + ext(KTJL, "konsumenttjänstlagen (17 §)") + " ska du reklamera ett fel inom skälig tid efter att du märkt det, och en reklamation inom två månader räknas enligt lagen som gjord i rätt tid. För arbete på byggnader går den yttre gränsen för att reklamera vid tio år efter att uppdraget avslutades. Geal lämnar garanti enligt lag (konsumenttjänstlagen).",
     ],
     "aside": {"title": "Spara i en pärm", "items": [
       "Kopia av våtrumsanmälan eller motsvarande.",
       "Våtrumsintyg eller kvalitetsdokument.",
       "VVS-intyg från installatören.",
       "Produktblad, skötselråd och foton.",
       "Slutfaktura med arbete och material var för sig.",
     ]}},
    {"id": "bostadsratt", "h2": "Bostadsrätt eller villa – vem bestämmer?",
     "paras": [
       "I en bostadsrätt får du enligt " + ext(BRL, "bostadsrättslagen (7 kap. 7 §)") + " inte utan styrelsens tillstånd göra ingrepp i bärande konstruktion, installera eller ändra ledningar för avlopp, värme, gas eller vatten, ändra ventilationen eller göra någon annan väsentlig förändring av lägenheten. En badrumsrenovering berör i regel flera av punkterna. Styrelsen får säga nej bara om åtgärden är till påtaglig skada eller olägenhet för föreningen, den får sätta villkor, och är du missnöjd kan hyresnämnden pröva beslutet.",
       "Säker Vatten råder dig att läsa föreningens stadgar och underhållsplan, söka godkännande i god tid med handlingar som visar vad som ska göras, och att i regel inte börja innan styrelsens skriftliga medgivande finns. Grannar kan behöva informeras, till exempel när vattnet stängs av. Planerar föreningen ett stambyte är det klokt att samordna badrummet med det – läs mer om helhetsprojekt på " + lnk("villarenovering.html", "villarenovering") + ".",
       "I en villa bestämmer du själv, men ansvarar också för helheten. Enligt " + ext(BOV_ANM, "Boverket om anmälan") + " kräver installation eller väsentlig ändring av en anläggning för vatten eller avlopp i en byggnad anmälan och startbesked från kommunen, liksom väsentlig ändring av ventilationen. Om just din ombyggnad är en väsentlig ändring avgör kommunen, så ska avlopp eller ventilation flyttas är det värt att fråga kommunens bygglovsenhet först.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en badrumsrenovering till",
  "steps": [
    ("Platsbesök", "Vi tittar på rummet, golvbrunnen, ventilationen och vad som finns bakom ytskikten, och stämmer av om föreningen eller kommunen behöver kopplas in."),
    ("Skriftligt kostnadsförslag", "Du får en offert där arbete och material står var för sig, med tätskiktssystem, VVS och el beskrivna."),
    ("Rivning och förkontroll", "Ytskikt och inredning rivs, underlaget kontrolleras och eventuella avvikelser noteras innan nytt byggs upp."),
    ("Rör, el och underlag", "Installatörerna drar rör och el, golvet byggs upp med fall mot brunnen och väggarna förbereds för tätskikt."),
    ("Tätskikt och ytskikt", "Tätskiktet monteras enligt tillverkarens anvisningar och branschreglerna, därefter plattsättning eller matta."),
    ("Montering och dokumentation", "Porslin, blandare och inredning monteras, och du får intyg, produktblad och skötselråd."),
  ],
  "rot_h2": "ROT-avdrag för badrummet",
  "rot": [
    "Rotavdraget är 30 procent av arbetskostnaden och högst 50 000 kr per person och år. Rot och rut får tillsammans uppgå till högst 75 000 kr. Material, resor och fuktmätningar ger inget avdrag. Enligt " + ext(SKV_GODK, "Skatteverkets lista över godkända arbeten") + " räknas bland annat kakel och klinker, att byta våtrumstapet mot kakel, installation av dusch, badkar, toalett, handfat och blandare samt modernisering av el. Geal drar avdraget direkt på fakturan.",
    "I bostadsrätt gäller avdraget arbeten innanför lägenhetens tak, väggar och golv som du ansvarar för enligt stadgarna. Byte av golvbrunn ger avdrag, men inte flytt av golvbrunn, flytt eller byte av avloppsrör eller stambyte. I ett småhus som är yngre än fem år ger bara arbete som återställer det ursprungliga skicket avdrag, inte om- eller tillbyggnad – det är " + ext(SKV_ROT, "Skatteverkets så kallade femårsregel") + ". För en bostadsrättslägenhet i ett flerbostadshus gäller inte den begränsningen.",
  ],
  "price_h2": "Vad styr kostnaden för ett badrum?",
  "price": [
    "Rummets storlek och hur mycket som ska rivas påverkar mest, följt av om golvbrunn, rör och el ska flyttas eller bara bytas på plats. Ett golv som måste byggas upp på nytt för att få rätt fall, en gammal brunn som behöver bytas eller ett bjälklag som ska förstärkas lägger till arbete. Materialval som storformatsplattor, golvvärme och inbyggd teknik spelar också in.",
    "Därför lämnar vi inga schablonpriser. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag för just ditt badrum, med ROT-avdraget beräknat.",
  ],
  "faq": [
    ("Måste golvbrunnen bytas när jag renoverar badrummet?", "Om brunnen är tillverkad före 1990 ska den bytas enligt GVK:s och Säker Vattens branschregler. En nyare brunn i gott skick kan sitta kvar om den är fixerad enligt gällande anvisningar. Är åldern oklar rekommenderar GVK byte."),
    ("Vilka intyg ska jag få efter en badrumsrenovering?", "Ett våtrumsintyg eller kvalitetsdokument för tätskiktet, ett intyg från VVS-installatören och produktblad och skötselråd för materialen. Spara dem tillsammans med slutfakturan."),
    ("Hur mycket ska golvet luta mot golvbrunnen?", "Vid duschplatsen anger GVK ett fall mellan 1:150 och 1:50, i genomsnitt omkring 13 millimeter per meter. Lutningen ska finnas både i underlaget och i det färdiga golvet."),
    ("Kan jag ha målade väggar i en del av badrummet?", "Ja, enligt Byggkeramikrådet går det att kombinera kaklade och målade väggar, men då gäller olika branschregler för respektive del och tätskikten ska överlappa. Kvalitetsdokumentet för keramik omfattar inte de målade partierna."),
    ("Behöver styrelsen godkänna min badrumsrenovering?", "I de flesta fall ja. Bostadsrättslagen kräver styrelsens tillstånd för bland annat ändring av vatten- och avloppsledningar och ventilation. Sök godkännandet innan du bokar hantverkare."),
    ("När kan jag sätta på golvvärmen i det nya badrummet?", "Byggkeramikrådet anger tidigast 28 dygn efter plattsättning, och temperaturen ska sedan höjas långsamt enligt leverantörens anvisning."),
  ],
  "sources": [
    ("Boverket – Fuktsäkerhet (PBL kunskapsbanken)", BOV_FUKT),
    ("Boverket – Anmälan (PBL kunskapsbanken)", BOV_ANM),
    ("GVK – Kvalitetsdokument", GVK_KVAL),
    ("GVK – Före arbetets utförande", GVK_FORE),
    ("GVK – Efter arbetets utförande", GVK_EFTER),
    ("GVK – Golvlutning", GVK_LUTN),
    ("GVK – Våtzoner", GVK_ZON),
    ("GVK – Gamla golvbrunnar", GVK_BRUNN),
    ("GVK – Elgenomföring i badrum", GVK_EL),
    ("Byggkeramikrådet – Om behörighet", BKR_BEH),
    ("Byggkeramikrådet – Vanliga frågor", BKR_FAQ),
    ("Säker Vatten – Konsumenter", SV_KONS),
    ("Elsäkerhetsverket – Anlita ett elinstallationsföretag", ESV),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_GODK),
    ("Skatteverket – Rot och rut", SKV_ROTRUT),
    ("Bostadsrättslag (1991:614), riksdagen.se", BRL),
    ("Konsumenttjänstlag (1985:716), riksdagen.se", KTJL),
  ],
  "cta": ("Planerar du ett nytt badrum?", "Boka ett gratis platsbesök så får du ett skriftligt kostnadsförslag med ROT-avdraget inräknat."),
  "img": [
    ("Nyrenoverat badrum med ljusgrå klinker, glasad duschvägg och golvbrunn i duschplatsen",
     "newly renovated Scandinavian bathroom in a Stockholm villa, light grey large-format floor tiles sloping to a square stainless floor drain, frameless glass shower screen, white wall tiles, wall-hung toilet, oak vanity, soft daylight from a small window"),
    ("Badrum under renovering med blått tätskikt på väggar och golv runt golvbrunnen",
     "bathroom under renovation, walls and floor coated with blue liquid waterproofing membrane, new floor drain with clamping ring in the shower area, pipe penetrations sealed with collars, construction lighting, no tiles yet, clean and orderly"),
  ],
  "related": [
    ("koksrenovering.html", "Köksrenovering i Stockholm", "Planering, el, VVS och ventilation i köket."),
    ("villarenovering.html", "Villarenovering", "Flera rum eller hela huset i ett projekt."),
    ("golvlaggning.html", "Golvläggning", "Nya golv och slipning i resten av huset."),
    ("byggfirma.html", "Byggfirma i Stockholm", "Total entreprenad med en kontakt."),
  ],
},
# ---------------------------------------------------------------- KÖK
"koksrenovering.html": {
  "kind": "hub", "service": "koksrenovering", "svc_label": "Köksrenovering",
  "title": "Köksrenovering i Stockholm – el, VVS, fläkt och ROT",
  "description": "Köksrenovering i Stockholm: planering, el och VVS, köksfläkt, öppen planlösning och bärande väggar, föreningens tillstånd och ROT. Gratis platsbesök.",
  "h1": "Köksrenovering i Stockholm",
  "lead": "En köksrenovering kan vara allt från nya luckor och bänkskiva till ett helt nytt kök med flyttad diskbänk och öppen planlösning. Ju mer som flyttas – vatten, avlopp, el, fläkt eller väggar – desto fler regler berörs. Geal Entreprenad AB tar hela köksprojektet i villor och bostadsrätter i Stockholm, från rivning till sista skåpslucka, med gratis platsbesök och skriftligt kostnadsförslag.",
  "card": "Planering, el, VVS, fläkt och väggar.",
  "sections": [
    {"id": "planering", "anchor": "Planering",
     "h2": "Planera utifrån det som är svårt att flytta",
     "paras": [
       "Skåp och luckor går att rita om nästan hur som helst. Det som avgör hur stort projektet blir är var diskbänken, köksfläkten och spisen hamnar i förhållande till befintliga avlopp, ventilationskanal och elcentral. Ligger allt kvar på samma plats kan köket ofta bytas utan ingrepp i husets installationer. Ska diskbänken till en köksö eller fläkten till en annan vägg krävs nya rör, ny kanaldragning och ofta ny el.",
       "Bestäm därför tidigt vad som ska vara kvar. Tre nivåer är vanliga: byte av luckor, bänkskiva och vitvaror i befintlig stomme; nytt kök med samma planlösning; eller nytt kök där funktioner flyttas eller en vägg tas bort. Den sista nivån är den enda som normalt berör bygglagstiftningen och, i bostadsrätt, föreningens tillstånd.",
       "Tänk också på hur gammalt köket och huset är. I äldre villor kan elcentral och avlopp behöva ses över samtidigt, och då är det enklare att göra det medan köket ändå är rivet. Vill du göra om fler rum i samma veva kan det vara värt att läsa om " + lnk("villarenovering.html", "villarenovering") + " och om " + lnk("badrumsrenovering.html", "badrumsrenovering") + ", eftersom kök och badrum ofta delar stam.",
     ],
     "aside": {"title": "Tre nivåer av köksrenovering", "items": [
       "Ansiktslyft: luckor, bänkskiva, vitvaror.",
       "Nytt kök i samma planlösning.",
       "Ny planlösning: flytt av funktioner eller väggar.",
     ]}},
    {"id": "barande-vagg", "h2": "Öppen planlösning och bärande väggar",
     "paras": [
       "Att riva väggen mellan kök och vardagsrum är en av de vanligaste önskningarna. Är väggen bärande gäller plan- och bygglagen: enligt " + ext(BOV_ANM, "Boverket") + " är en ändring som väsentligt påverkar konstruktionen av byggnadens bärande delar anmälningspliktig. Arbetet får inte påbörjas förrän byggnadsnämnden gett startbesked, och den ombyggda delen får inte tas i bruk förrän slutbesked finns, om nämnden inte beslutar annat.",
       "Om en vägg bär eller inte går sällan att avgöra med blotta ögat. Bjälklagets riktning, vad som står ovanpå och hur huset är byggt spelar in. I praktiken behövs ofta en konstruktionsberäkning för balk och upplag, och den ingår i underlaget till anmälan. Räkna med att den här delen styr tidplanen, eftersom du behöver vänta på startbesked innan rivningen.",
       "I bostadsrätt kräver ett ingrepp i bärande konstruktion dessutom styrelsens tillstånd enligt bostadsrättslagen. Föreningen kan vilja se konstruktörens underlag innan den svarar. Skatteverket godkänner rotavdrag i småhus för att riva väggar och bygga om planlösningen, så länge större delen av den ursprungliga stommen behålls.",
     ],
     "aside": None},
    {"id": "flakt", "h2": "Köksfläkt och ventilation",
     "paras": [
       "Köksfläkten är en del av husets ventilation och därför mer än en vitvara. Installation eller väsentlig ändring av en anordning för ventilation är anmälningspliktig enligt plan- och bygglagen. Att byta en fläkt mot en likvärdig på samma plats är något annat än att dra en ny kanal genom ett bjälklag eller ansluta en motordriven fläkt till ett system som är byggt för självdrag.",
       "I flerbostadshus kan köksventilationen hänga ihop med husets gemensamma system, och då är det föreningen som vet vilken typ av köksfläkt som passar. Bostadsrättslagen kräver styrelsens tillstånd för installation eller ändring av ventilationen. " + ext(SV_KONS, "Säker Vatten") + " påminner om att även brandskyddsregler kan beröra ventilationssystemet vid en renovering, trots att själva åtgärden inte gäller ventilation.",
       "I villan är det enklare men kraven på funktion är desamma: fläkten ska föra bort os och fukt utan att ändra balansen i resten av husets ventilation. Rengöring av ventilation och imkanaler räknas enligt Skatteverket som rotarbete i småhus, medan rengöring av själva spisfläkten hör till rut.",
     ],
     "aside": None},
    {"id": "el-vvs-kok", "h2": "El, vatten och avlopp i köket",
     "paras": [
       "Säker Vattens råd till " + ext(SV_KONS, "konsumenter") + " gäller uttryckligen kök, badrum och tvättstuga. Ett auktoriserat VVS-företag ska lämna ett intyg efter arbetet med omfattningen och eventuella avvikelser, och montörerna ska kunna visa branschlegitimation. Intyget är en värdehandling som ska sparas – det är det du kan visa upp vid en vattenskada under diskbänken.",
       "Ny belysning under överskåpen, fler uttag på bänken eller en induktionshäll med större effektbehov är elinstallationer som ska göras av ett " + ext(ESV, "registrerat elinstallationsföretag") + ". I äldre hus kan elcentralen behöva kompletteras när köket får fler maskiner. Hos Geal utförs el och VVS av behöriga installatörer som samordnas med snickeriet, så att rör och kablar ligger rätt innan skåpen monteras.",
       "I villa kan installation eller väsentlig ändring av en anläggning för vatten eller avlopp i byggnaden kräva anmälan. Vad som räknas som väsentligt bedömer kommunen, så en helt ny avloppsdragning till en köksö är värd att stämma av där innan arbetet planeras klart.",
     ],
     "aside": {"title": "Fråga efter i offerten", "items": [
       "Vem som utför el och VVS.",
       "Om intyg lämnas för VVS-arbetet.",
       "Om ventilationen ändras och vem som anmäler.",
       "Arbete och material var för sig.",
     ]}},
    {"id": "golv-vaggar", "h2": "Golv, väggar och ordningen i bygget",
     "paras": [
       "Ska golvet bytas är det ofta enklast att göra det innan de nya skåpen står på plats, så att det går in under stommen – men det beror på golvtyp och tillverkarens anvisningar. Behålls ett äldre trägolv kan det slipas i samma veva som resten av rummet – se " + lnk("golvlaggning.html", "golvläggning och slipning") + ". Väggar som ska målas eller tapetseras görs innan överskåpen hängs upp.",
       "Stänkskyddet bakom bänken och spisen är den yta som utsätts mest. Kakel, glas och skivmaterial har olika krav på underlag och infästning, och eluttagen i stänkskyddet ska placeras innan plattorna sätts. Skatteverket godkänner rotavdrag för att sätta kakel, byta golv och väggmaterial samt måla eller lacka köksluckor.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en köksrenovering till",
  "steps": [
    ("Platsbesök och önskemål", "Vi går igenom köket, avlopp, ventilation och el och vilka väggar som berörs, och vad du vill uppnå."),
    ("Kostnadsförslag och tillstånd", "Du får ett skriftligt förslag. Vid behov tas underlag fram för anmälan till kommunen eller ansökan hos styrelsen."),
    ("Rivning", "Gamla skåp, vitvaror och ytskikt monteras ner och bärs ut, och vatten och el kopplas bort på ett säkert sätt."),
    ("Installationer", "Installatörerna drar rör, el och kanaler för fläkten enligt den nya planen, innan väggar och golv stängs."),
    ("Golv, väggar och skåp", "Golv och väggar färdigställs, stommen monteras och bänkskivan mäts in och sätts på plats."),
    ("Vitvaror och slutkontroll", "Vitvaror, blandare och belysning ansluts och provas, och du får intyg och skötselanvisningar."),
  ],
  "rot_h2": "ROT-avdrag för köket – vad räknas?",
  "rot": [
    "Du får rotavdrag med 30 procent av arbetskostnaden, högst 50 000 kr per person och år, och rot och rut får tillsammans vara högst 75 000 kr. Skåp, bänkskiva, vitvaror och annat material ger inget avdrag. Enligt " + ext(SKV_GODK, "Skatteverkets förteckning") + " räknas bland annat att montera fast köksinredning och installera vitvaror i samband med omfattande byggarbete eller renovering, att byta köksluckor, att modernisera el och byta uttag, att installera blandare och kranar samt att sätta kakel. Att enbart reparera en diskmaskin är rut, inte rot.",
    "I bostadsrätt gäller avdraget arbete inne i lägenheten som du ansvarar för enligt stadgarna, och fast köksinredning och vitvaror räknas när de monteras i samband med byggarbetet. Geal drar avdraget direkt på fakturan och ansöker om utbetalningen hos " + ext(SKV_ROT, "Skatteverket") + ".",
  ],
  "price_h2": "Vad påverkar priset på en köksrenovering?",
  "price": [
    "Den största skillnaden ligger i nivån: ett ansiktslyft med nya luckor och bänkskiva är ett mindre jobb än ett kök där diskbänk och fläkt flyttas. En bärande vägg som tas bort lägger till konstruktionsberäkning, balk och anmälan. Val av stomme, bänkskiva och vitvaror styr materialkostnaden, och i äldre hus kan elcentral och avlopp behöva åtgärdas.",
    "Vi lämnar inga schablonpriser. Efter ett gratis platsbesök får du ett skriftligt kostnadsförslag där arbete och material står var för sig, så att du ser vad ROT-avdraget gäller.",
  ],
  "faq": [
    ("Behöver jag anmäla till kommunen om jag river väggen till köket?", "Ja, om väggen är bärande och ändringen väsentligt påverkar konstruktionen. Då krävs anmälan och startbesked innan rivningen, och slutbesked innan den ombyggda delen tas i bruk."),
    ("Får jag byta köksfläkt i min bostadsrätt?", "Det beror på föreningen. Ventilationen är ofta gemensam i flerbostadshus, och bostadsrättslagen kräver styrelsens tillstånd för att installera eller ändra ventilationen. Fråga styrelsen vilka fläktar som får anslutas."),
    ("Kan jag få rotavdrag för nya vitvaror?", "Inte för själva vitvarorna, eftersom material inte ger avdrag. Arbetet med att installera dem räknas om det görs i samband med en större renovering eller byggarbete."),
    ("Kan diskbänken flyttas till en köksö?", "Oftast ja, men det kräver nya avlopps- och vattenledningar i golvet eller bjälklaget. I bostadsrätt behövs styrelsens tillstånd, och i villa kan en ny avloppsdragning behöva anmälas."),
    ("Ska golvet läggas före eller efter köksskåpen?", "Ofta är det enklast att lägga golvet först så att det går in under stommen, men det beror på golvtypen och tillverkarens anvisningar. Det bestäms i planeringen."),
  ],
  "sources": [
    ("Boverket – Anmälan (PBL kunskapsbanken)", BOV_ANM),
    ("Säker Vatten – Konsumenter", SV_KONS),
    ("Elsäkerhetsverket – Anlita ett elinstallationsföretag", ESV),
    ("Skatteverket – Så fungerar rotavdraget", SKV_ROT),
    ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_GODK),
    ("Skatteverket – Rot och rut", SKV_ROTRUT),
    ("Bostadsrättslag (1991:614), riksdagen.se", BRL),
  ],
  "cta": ("Dags för ett nytt kök?", "Boka ett gratis platsbesök så får du ett skriftligt kostnadsförslag för hela köket."),
  "img": [
    ("Nyrenoverat ljust kök med köksö, ekbänkskiva och köksfläkt i en villa i Stockholm",
     "newly renovated bright Scandinavian kitchen in a Stockholm villa, white flat-front cabinets, oak worktop, kitchen island with integrated sink, stainless cooker hood above induction hob, white tiled splashback, light oak floor, daylight through large window"),
    ("Kök under renovering med nya rör och elkablar på plats innan skåpen monteras",
     "kitchen under renovation, old cabinets removed, new water and drain pipes and electrical cables roughed in at the wall, freshly plastered walls, new ventilation duct for cooker hood, open plan opening with new steel beam above, clean construction site, no people"),
  ],
  "related": [
    ("badrumsrenovering.html", "Badrumsrenovering i Stockholm", "Tätskikt, golvbrunn och intyg i våtrummet."),
    ("snickare.html", "Snickare", "Inredning, väggar och snickeri inomhus."),
    ("malare.html", "Målare", "Väggar, tak och lackade luckor."),
    ("villarenovering.html", "Villarenovering", "Kök, badrum och helhet i ett projekt."),
  ],
},
}
