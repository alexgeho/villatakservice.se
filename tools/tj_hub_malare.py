# -*- coding: utf-8 -*-
"""Tjänstehubbar: malare.html, fasadrenovering.html, fonsterbyte.html (tjänster v1, 2026-10-25).
Fakta kontrollerade mot källorna i "sources" (sidor som faktiskt öppnats 2026-10-25):
Boverket PBL kunskapsbanken (fasadändring, lydelse efter 1 december 2025), Boverkets energiguide
(fönster, tilläggsisolering av fasad), Stockholms stad (nya PBL-regler), Stadsmuseet (klassificering),
Riksantikvarieämbetet "Byggnadsmåleri" (färgtyper, förarbete), Skatteverket (rotavdrag, lista över rotarbeten).
Inga priser, garantier utöver lag, omdömen, case eller cert. Schema: se tools/tj_check.py."""

BV_FASAD = "https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/"
BV_FONSTER = "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/fonster_dorrar/"
BV_ISOL = "https://www.boverket.se/sv/energiguiden/energirenovera-smahus/5.valja_atgarder/tillaggsisolera-fasaden/"
STHLM_PBL = "https://bygglov.stockholm/sok-lov-eller-anmalan/stora-forandringar-i-plan--och-bygglagen-och-byggreglerna/"
SSM = "https://stadsmuseet.stockholm/kunskap-och-samlingar/kulturmiljo/klassificering/"
RAA = "https://www.raa.se/publicerat/9789172095830.pdf"
SKV_LISTA = "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html"
SKV_ROT = "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html"

def _x(url, text):
    return f'<a class="text-link" href="{url}" rel="noopener">{text}</a>'

def _l(href, text):
    return f'<a class="text-link" href="{href}">{text}</a>'

S_BV_FASAD = ("Boverket – PBL kunskapsbanken: Bygglov för fasadändring", BV_FASAD)
S_STHLM = ("Stockholms stad – Stora förändringar i plan- och bygglagen och byggreglerna", STHLM_PBL)
S_SSM = ("Stadsmuseet i Stockholm – Kulturhistorisk klassificering", SSM)
S_RAA = ("Riksantikvarieämbetet – Byggnadsmåleri med traditionella färger (pdf)", RAA)
S_SKV_LISTA = ("Skatteverket – Ger arbetet rätt till rotavdrag?", SKV_LISTA)
S_SKV_ROT = ("Skatteverket – Så fungerar rotavdraget", SKV_ROT)
S_BV_FONSTER = ("Boverket – Energiguiden: Energirenovera eller byta fönster och dörrar", BV_FONSTER)
S_BV_ISOL = ("Boverket – Energiguiden: Tilläggsisolera fasaden", BV_ISOL)

PAGES_TJ = {
# ------------------------------------------------------------------ MÅLARE
"malare.html": {
  "kind": "hub", "service": "malare", "svc_label": "Målare",
  "title": "Målare i Stockholm – fasad, fönster och inomhus",
  "description": "Målare i Stockholm för villa och radhus: fasadmålning av trä och puts, fönster och invändig "
                 "målning. Färgtyp, förarbete, kulörbyte och ROT-avdrag.",
  "h1": "Målare i Stockholm",
  "lead": "Ska villan målas om ute eller inne tar Geal hand om hela jobbet, från tvätt, skrapning och lagning "
          "av trä till sista strykningen på fasad, fönster, väggar och tak. Färgtypen väljs efter vad huset är "
          "målat med i dag, och ROT-avdraget dras direkt på fakturan.",
  "card": "Fasad, fönster och invändig målning.",
  "sections": [
    {"id": "fasad", "anchor": "Fasadmålning",
     "h2": "Fasadmålning: färgtypen betyder mer än kulören",
     "paras": [
       "Det viktigaste beslutet när en träfasad ska målas om är vilken färgtyp som ska på. Riksantikvarieämbetets "
       f"handbok {_x(RAA, 'Byggnadsmåleri')} råder fastighetsägare att i de flesta fall stanna vid samma färgtyp "
       "som tidigare, och särskilt utomhus på ytor med linoljefärg, slamfärg, trätjära eller kalkfärg. Att lägga "
       "en modern färg ovanpå en äldre typ beskrivs som en teknisk risk: nästa underhåll blir krångligt, och vill "
       "man gå tillbaka krävs i praktiken att all gammal färg tas bort.",
       "Därför börjar vi med att ta reda på vad som faktiskt sitter på väggen. På ett hus som målats om många "
       "gånger kan även en erfaren målare ha svårt att avgöra vilka färger som använts, eftersom antalet "
       "färgtyper mångdubblades under 1900-talets andra hälft. Vi skrapar fram lagren och provar på en mindre "
       "yta när det behövs. Först därefter bestäms färgsystem och antal strykningar.",
       "Slamfärg, oftast den röda, är matt, vattenspädbar och släpper igenom fukt. Den fäster bra på ohyvlat "
       "virke men sämre på hyvlad panel, och enligt handboken är den den mest underhållsvänliga av alla "
       "färgtyper: borsta av och måla om. Linoljefärg stryks i flera tunna lager och torkar långsammare än "
       "moderna färger. Rätt sammansatt och påförd anges den hålla i ungefär 15–20 år, beroende på hur utsatt "
       "fasaden är. Har huset en modern fabriksfärg gäller samma princip: underlaget styr nästa färg.",
     ],
     "aside": {"title": "Färgtyper på fasad", "items": [
       "Slamfärg – matt, för ohyvlat virke",
       "Linoljefärg – tunna lager, lång livslängd",
       "Kalkfärg – på ren kalkputs",
       "Modern fasadfärg – följ det som redan sitter där"]}},
    {"id": "underarbete",
     "h2": "Förarbetet är det som gör att färgen sitter",
     "paras": [
       "En fasadmålning är till största delen förarbete. Ytan tvättas, spikar som krupit ut slås in och all lös "
       "färg borstas och skrapas bort. Grånat trä, så kallat blåträ, slipas ner till frisk yta, och rötskadat "
       "virke byts mot nytt – ofta ändträ längst ner på panelen och kring fönstren. Högtryckstvätt är vanligt "
       "i dag, men den som tvättar måste behärska tekniken så att vatten inte trycks in i väggen.",
       "Hur mycket som ska grundas beror på skicket. Handboken anger att det räcker att grunda de skadade "
       "partierna när omkring tio procent av färgskiktet är skadat, medan hela ytan bör grundas när 30–40 "
       "procent är skadat. Fönstersnickerier, vindskivor och sydfasader tar mest stryk och behöver målas oftare "
       "än resten av huset. Att bättra dem i tid kan skjuta upp en hel ommålning.",
       "Väder och säsong spelar stor roll. Linoljefärg bör strykas när det är varmt och torrt, med en fukthalt i "
       "träet på högst cirka 15 procent. Riksantikvarieämbetet nämner maj–augusti som bästa period och avråder "
       "från stark direkt sol, som kan ge blåsor. I praktiken följer man solen runt huset och målar de väggar "
       "som redan har varit solbelysta. Ska huset målas i grått, vitt eller en annan ny kulör gäller samma "
       "förarbete – det är underlaget som avgör resultatet.",
     ],
     "aside": {"title": "Förarbete i ordning", "items": [
       "Tvätt av fasaden",
       "Skrapning och slipning",
       "Byte av rötskadat trä",
       "Grundning av bart trä",
       "Kittning av sprickor",
       "Mellan- och slutstrykning"]}},
    {"id": "inomhus",
     "h2": "Invändig målning och tapetsering",
     "paras": [
       "Inomhus målar vi väggar, tak, snickerier, dörrar och element, och vi tapetserar. Arbetsgången liknar den "
       "utvändiga: golv och inredning skyddas, sprickor och hål lagas, ytorna spacklas och slipas, grundas där "
       "underlaget kräver det och stryks sedan färdigt. Ett jämnt resultat avgörs nästan helt av spacklingen och "
       "av att varje lager får torka ordentligt innan nästa.",
       "I äldre villor kan det finnas traditionella färger kvar under senare lager. Limfärg var vanlig i tak "
       "ända fram till 1950-talet och användes som tryckfärg på tapeter. Den är känslig för fukt och passar "
       "därför inte i kök och badrum, och det befintliga lagret styr vilken färg som kan läggas ovanpå. Linoljefärg "
       "hörde ännu på 1950-talet till de vanligaste färgerna och kan sitta kvar på äldre snickerier.",
       "Ska huset renoveras mer än så samordnar vi måleriet med övriga hantverkare i samma entreprenad. Läs mer "
       f"om {_l('villarenovering.html', 'renovering av villan')} eller om hur Geal arbetar som "
       f"{_l('byggfirma.html', 'byggfirma med total entreprenad')}. Behöver taket målas samtidigt finns "
       f"{_l('takmalning.html', 'takmålning')} som egen tjänst.",
     ],
     "aside": None},
    {"id": "kulor",
     "h2": "Ny kulör på huset – vad gäller sedan 1 december 2025",
     "paras": [
       "Sedan den 1 december 2025 behövs inte bygglov för att byta kulör på ett en- eller tvåbostadshus, och inte "
       "heller för att byta material på fasad eller tak. Det framgår av "
       f"{_x(BV_FASAD, 'Boverkets PBL kunskapsbanken')}. Att måla om i samma kulör som tidigare räknas normalt "
       "som underhåll.",
       "Undantagen är många i Stockholmstrakten. Lov krävs ändå om huset omfattas av skyddsbestämmelser i "
       "detaljplan eller områdesbestämmelser, om det är en särskilt värdefull byggnad, om det ligger i ett "
       "särskilt värdefullt bebyggelseområde eller om planen har utökad lovplikt. Stockholms stad hänvisar till "
       f"{_x(SSM, 'Stadsmuseets klassificeringskarta')} som en första indikation, där blå och grön markering "
       "betyder höga kulturhistoriska värden. I grannkommunerna får du fråga bygglovsenheten.",
       "Boverket påpekar att ett byte av färgtyp, till exempel från slamfärg till silikonhartsfärg eller från "
       "linoljefärg till plastfärg, inte är ett kulörbyte men kan påverka byggnadens yttre karaktärsdrag. Det "
       "spelar roll för flerbostadshus inom detaljplan, där fasadändring mot gata eller park fortfarande kräver "
       "lov, och i skyddade miljöer. Även lovfri målning ska följa varsamhetskravet och i vissa fall detaljplanen.",
     ],
     "aside": {"title": "Lov krävs ändå om", "items": [
       "detaljplanen har skyddsbestämmelser",
       "huset är särskilt värdefullt",
       "området är särskilt värdefullt",
       "planen har utökad lovplikt"]}},
  ],
  "steps_h2": "Så går målningsjobbet till",
  "steps": [
    ("Platsbesök", "Vi tittar på underlag, färglager och skador och frågar vad du vill uppnå med kulör och glans."),
    ("Skriftligt kostnadsförslag", "Förarbete, färgtyp, antal strykningar och ROT-avdrag står specificerat."),
    ("Lovfrågan", "Vi kontrollerar om huset är klassat eller har skyddsbestämmelser innan en ny kulör beställs."),
    ("Förarbete", "Tvätt, skrapning, lagning av trä eller puts, spackling inomhus och grundning."),
    ("Målning", "Mellan- och slutstrykning i lämpligt väder, med torktid mellan varje lager."),
    ("Slutgenomgång", "Vi går igenom ytorna tillsammans, bättrar det som behövs och städar upp."),
  ],
  "rot_h2": "ROT-avdrag för målning och tapetsering",
  "rot": [
    f"I {_x(SKV_LISTA, 'Skatteverkets lista över rotarbeten')} för småhus finns målning av golv, tak, väggar, "
    "fönster och element, målning av fasader samt tapetsering. Avdraget är 30 procent av arbetskostnaden, högst "
    "50 000 kronor per person och år, och ROT och RUT får tillsammans vara högst 75 000 kronor. Material och "
    "resor ger inte avdrag. Geal drar avdraget direkt på fakturan.",
    "I bostadsrätt är gränsen snävare: målning av väggar, tak, golv, element, innerdörrar och insidan av "
    "ytterdörrar och fönster ger avdrag, men inte målning av fasader eller utsidan av fönster. Att måla staket "
    "eller murar ger inte ROT.",
  ],
  "price_h2": "Vad styr kostnaden för målningen",
  "price": [
    "Kostnaden styrs av ytans storlek och höjd, om det behövs ställning eller lift, hur mycket som måste skrapas "
    "och lagas, hur många fönster och snickerier som ingår och vilken färgtyp och hur många strykningar som "
    "krävs. Inomhus påverkar spackling, skyddstäckning och tapetval mest.",
    "Vi kommer ut utan kostnad, tittar på underlaget och lämnar ett skriftligt kostnadsförslag där förarbete, "
    "färgsystem och ROT-avdrag är specificerade.",
  ],
  "faq": [
    ("Kan en fasad med slamfärg målas över med linoljefärg?",
     "Det är sällan att rekommendera. Slamfärg sitter oftast på ohyvlat virke, och Riksantikvarieämbetet råder "
     "att i de flesta fall behålla samma färgtyp vid ommålning. Ska färgtypen bytas behöver den gamla färgen i "
     "praktiken tas bort, och det tar vi upp i kostnadsförslaget."),
    ("Hur länge håller en fasad målad med linoljefärg?",
     "Riksantikvarieämbetet anger ungefär 15–20 år för en rätt sammansatt och påförd linoljefärg, beroende på "
     "väder och läge. Fönstersnickerier, vindskivor och sydvägg behöver ofta bättras tidigare."),
    ("Vilka månader är bäst för utvändig målning?",
     "För linoljefärg nämns maj–augusti som bästa period. Träet ska vara torrt, med en fukthalt på högst cirka "
     "15 procent, och stark direkt sol undviks eftersom färgen kan bilda blåsor."),
    ("Behöver jag bygglov för att måla villan i en annan kulör?",
     "Inte för ett en- eller tvåbostadshus sedan 1 december 2025, så länge huset inte omfattas av "
     "skyddsbestämmelser, är särskilt värdefullt, ligger i ett särskilt värdefullt område eller har utökad "
     "lovplikt i planen. I Stockholms stad ger Stadsmuseets klassificeringskarta en första fingervisning."),
    ("Ger målning av staketet rätt till ROT-avdrag?",
     "Nej. Skatteverket räknar inte målning av staket eller murar som rotarbete. Fasad, fönster och "
     "invändiga ytor i villan ger däremot avdrag på arbetskostnaden."),
    ("Kan ni tapetsera och måla i samma uppdrag?",
     "Ja. Vi förbereder väggarna, tapetserar och målar tak och snickerier i samma uppdrag, och "
     "tapetseringen ger rätt till ROT-avdrag på arbetskostnaden."),
  ],
  "sources": [S_RAA, S_BV_FASAD, S_STHLM, S_SSM, S_SKV_LISTA, S_SKV_ROT],
  "cta": ("Dags att måla om?", "Boka ett kostnadsfritt platsbesök så går vi igenom underlag, färgtyp och kostnadsförslag."),
  "img": [
    ("Nymålad ljusgul trävilla med vita knutar och fönsterfoder i Stockholm",
     "freshly repainted pale yellow wooden villa with white corner boards and white window trim, Stockholm "
     "suburb, late summer afternoon, green garden and birch trees"),
    ("Skrapad träpanel och penslar inför ommålning med linoljefärg",
     "close-up of scraped and sanded wooden facade boards prepared for repainting, round paint brushes and an "
     "open can of linseed oil paint on a plank, soft daylight"),
  ],
  "related": [
    ("fasadrenovering.html", "Fasadrenovering i Stockholm", "Panel, puts och tilläggsisolering."),
    ("fonsterbyte.html", "Fönsterbyte i Stockholm", "Byta eller renovera fönster."),
    ("takmalning.html", "Takmålning", "Målning av plåt- och betongtak."),
    ("villarenovering.html", "Villarenovering", "Hela huset i en entreprenad."),
  ],
},
# ------------------------------------------------------------------ FASADRENOVERING
"fasadrenovering.html": {
  "kind": "hub", "service": "fasadrenovering", "svc_label": "Fasadrenovering",
  "title": "Fasadrenovering i Stockholm – panel, puts och isolering",
  "description": "Fasadrenovering i Stockholm: byte av träpanel, lagning och omputsning, tilläggsisolering "
                 "utan fuktproblem och vad som gäller för lov sedan 1 december 2025.",
  "h1": "Fasadrenovering i Stockholm",
  "lead": "En fasadrenovering kan vara allt från att byta några rötskadade panelbrädor till att riva hela "
          "beklädnaden, tilläggsisolera och sätta upp ny panel eller puts. Geal bedömer först vad väggen behöver "
          "och samordnar sedan ställning, snickeri, puts, plåt och målning i en och samma entreprenad.",
  "card": "Puts, panel och tilläggsisolering.",
  "sections": [
    {"id": "panel", "anchor": "Träfasad",
     "h2": "Träfasaden: laga brädor eller byta hela panelen",
     "paras": [
       "På en träfasad uppstår skadorna där vatten blir kvar: nederst mot sockeln, kring fönstren och under "
       "fönsterbleck, och på ändträ som saknar skydd. I sin energiguide skriver "
       f"{_x(BV_FONSTER, 'Boverket')} att gamla fönstertätningar ofta släpper in vatten under fönstren, särskilt "
       "på väggar som tar emot slagregn. En fasadrenovering börjar därför med att vi känner på virket, petar i "
       "misstänkta partier och öppnar där det behövs.",
       "Är det mesta av panelen frisk räcker det att byta de skadade brädorna mot nya med samma profil och "
       "dimension och sedan måla. Har panelen gjort sitt över stora ytor, eller har upprepade ommålningar med "
       "olika färgtyper byggt upp ett skikt som flagnar, kan det vara klokare att byta hela beklädnaden. Då går "
       "det också att se över vindskydd, läkt och isolering bakom panelen.",
       "Byts panelen mot samma material och utförande som tidigare räknas det som underhåll och inte som "
       "fasadändring. Ska fasaden få en ny färg efteråt hänger valet av färgtyp ihop med panelen: slamfärg "
       f"fäster bra på ohyvlat virke men sämre på hyvlad panel. Mer om det på sidan om {_l('malare.html', 'målare')}.",
     ],
     "aside": {"title": "Vanliga skadeställen", "items": [
       "Nederkant mot sockeln",
       "Under fönsterbleck",
       "Ändträ och knutbrädor",
       "Vindskivor och sydvägg"]}},
    {"id": "puts",
     "h2": "Putsfasader: lagning, omputsning och rätt bruk",
     "paras": [
       "En putsad fasad lagas bäst med ett bruk som passar det som redan sitter på väggen. "
       f"{_x(RAA, 'Riksantikvarieämbetet')} beskriver hur man vid mitten av 1900-talet gick alltmer från "
       "kalkbruk till kalkcementbruk, och samtidigt till andra färger än kalkfärg. Kalkfärg fäster bra på "
       "kalkputs men dåligt på cementrika underlag, och den släpper igenom fukt nästan obehindrat.",
       "Därför tar vi reda på vilken puts huset har innan sprickor lagas eller fasaden putsas om. Lösa partier "
       "knackas ner, underlaget rensas och nytt bruk byggs upp mot den gamla ytan. När skadorna är många eller "
       "putsen har släppt över stora delar blir en omputsning av hela fasaden aktuell, och då behöver även "
       "sockel, fönsteranslutningar och plåtar ses över i samma veva.",
       "Efter lagningen ska fasaden avfärgas med en färg som fungerar på just det underlaget. Handboken anger "
       "att kalkfärg i dag främst används vid ommålning av ytor som redan är kalkavfärgade och vid nymålning av "
       "ren kalkputs på kulturhistoriskt värdefulla hus.",
     ],
     "aside": {"title": "Innan putsen lagas", "items": [
       "Vilket bruk sitter på väggen?",
       "Kalkfärg eller modern färg?",
       "Sprickor vid fönster och sockel?",
       "Ställning runt hela huset?"]}},
    {"id": "isolering",
     "h2": "Tilläggsisolering av fasaden utan nya fuktproblem",
     "paras": [
       f"{_x(BV_ISOL, 'Boverkets energiguide')} beskriver utvändig tilläggsisolering som oftast bäst både för "
       "energin och för fukten, eftersom den gamla väggen blir varmare och torrare och köldbryggor kan byggas "
       "bort. Invändig isolering gör tvärtom väggens utsida kallare, så att fukt torkar ut långsammare, och "
       "risken för röta, mögel och frostsprängning ökar ju tjockare man isolerar.",
       "En utvändig isolering förändrar däremot huset. Väggen blir tjockare, fönster och dörrar hamnar längre in, "
       "takfoten skjuter ut mindre och fasaden kan hänga ut över sockeln. Boverket varnar för ett överjäst "
       "uttryck och för att utåtgående fönster kanske inte längre går att haka av. Ofta behöver fönstren flyttas "
       "ut och sockel och takfot byggas på för att proportionerna ska bli rätt.",
       "Bäst blir det när panelen ändå ska bytas, så att samma arbete inte görs två gånger. Arbetet bör ske i "
       "torrt väder så att fukt inte stängs in, och ligger huset nära tomtgränsen kan en tjockare vägg inkräkta "
       "på grannens mark. Jämför gärna med att isolera uppåt – se "
       f"{_l('vindsisolering.html', 'vindsisolering')} och {_l('energieffektivt-tak.html', 'energieffektivt tak')}.",
     ],
     "aside": {"title": "Räkna med att se över", "items": [
       "Fönsterplacering och smygar",
       "Sockel och takfot",
       "Plåtar och fönsterbleck",
       "Avstånd till tomtgränsen"]}},
    {"id": "lov",
     "h2": "Lov för fasadrenovering sedan 1 december 2025",
     "paras": [
       "För villor, parhus och andra en- och tvåbostadshus krävs sedan 1 december 2025 inget bygglov för att "
       "byta fasadmaterial, till exempel från puts till träpanel, eller för att påverka husets karaktärsdrag på "
       f"annat sätt, enligt {_x(BV_FASAD, 'Boverkets kunskapsbank')}. Undantagen gäller skyddsbestämmelser i "
       "detaljplan eller områdesbestämmelser, särskilt värdefulla byggnader och miljöer samt planer med utökad "
       "lovplikt.",
       f"I Stockholms stad skriver {_x(STHLM_PBL, 'stadsbyggnadskontoret')} att Stadsmuseets klassificeringskarta "
       "ger en första indikation på om bygglov behövs. Lovfria åtgärder ska ändå uppfylla varsamhetskraven, och "
       "Boverket påpekar att en tilläggsisolering kan vara otillåten om den förvanskar en särskilt värdefull "
       "byggnad. För flerbostadshus inom detaljplan krävs fortfarande lov för fasadändring mot allmän plats.",
       "Påverkar arbetet den bärande konstruktionen eller brandskyddet kan det dessutom behövas en anmälan, även "
       "när lov inte krävs, och i vissa fall ska åtgärden följa detaljplanens bestämmelser trots att den är "
       "lovfri. Fastighetsägaren förväntas själv ta ansvar för att kraven uppfylls, skriver Stockholms stad.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går fasadrenoveringen till",
  "steps": [
    ("Genomgång av fasaden", "Vi kontrollerar panel, puts, sockel, fönsteranslutningar och plåtar och öppnar där det behövs."),
    ("Kostnadsförslag", "Ett skriftligt förslag som skiljer på lagning, byte, isolering och målning."),
    ("Lov och grannar", "Vi stämmer av klassning, detaljplan och gränsavstånd innan något beställs."),
    ("Ställning och rivning", "Ställning byggs, och skadad panel eller lös puts tas bort."),
    ("Reparation och ny beklädnad", "Trä byts, isolering kompletteras och ny panel eller puts kommer på plats."),
    ("Ytbehandling och kontroll", "Fasaden målas eller avfärgas, plåtar monteras och vi går igenom resultatet tillsammans."),
  ],
  "rot_h2": "ROT-avdrag vid fasadrenovering",
  "rot": [
    f"Enligt {_x(SKV_LISTA, 'Skatteverkets lista')} ger det ROT i småhus att byta, mura och reparera "
    "fasader, tilläggsisolera, rengöra fasader och måla fasader. Avdraget är 30 procent av "
    "arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor för ROT och RUT tillsammans. "
    "Material, utrustning och resor ger inte avdrag. Geal drar avdraget direkt på fakturan.",
    "För bostadsrätt ger varken tilläggsisolering, fasadtvätt eller målning av fasaden rätt till ROT.",
  ],
  "price_h2": "Vad påverkar kostnaden för en fasadrenovering",
  "price": [
    "Fasadens yta och höjd, hur stor del av panelen eller putsen som är skadad, valet mellan lagning och byte, "
    "om väggen ska tilläggsisoleras och hur mycket fönster, sockel och plåtar behöver anpassas. Ställning och "
    "bortforsling av gammalt material är också en del av kalkylen.",
    "Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag med varje moment för sig.",
  ],
  "faq": [
    ("Kan jag byta från puts till träpanel på villan utan bygglov?",
     "Ja, för ett en- eller tvåbostadshus sedan 1 december 2025 – om huset inte omfattas av skyddsbestämmelser, "
     "är särskilt värdefullt, ligger i ett särskilt värdefullt område eller har utökad lovplikt. Varsamhetskravet "
     "gäller ändå."),
    ("Är det bättre att tilläggsisolera fasaden inifrån eller utifrån?",
     "Utvändigt är oftast bäst för energi och fukt eftersom den gamla väggen blir varmare och torrare. Invändig "
     "isolering bevarar fasaden men ökar risken för fuktskador i väggen och gör rummen mindre."),
    ("Hur vet man om fasaden är putsad med kalkbruk eller kalkcementbruk?",
     "Husets ålder ger en ledtråd, eftersom kalkcementbruk tog över vid mitten av 1900-talet, men säkert besked "
     "får man genom att undersöka putsen på plats. Det avgör både lagningsbruk och färg."),
    ("Måste fönstren flyttas ut när fasaden tilläggsisoleras?",
     "Ofta, om de inte ska hamna djupt inne i väggen. Boverket nämner också att sockel och takfot kan behöva "
     "byggas på för att huset ska behålla sina proportioner."),
    ("Ger fasadtvätt före renoveringen rätt till ROT-avdrag?",
     "I villa ja, eftersom Skatteverket räknar rengöring av fasader som rotarbete. I bostadsrätt ger fasadtvätt "
     "inget avdrag."),
  ],
  "sources": [S_BV_FASAD, S_BV_ISOL, S_BV_FONSTER, S_STHLM, S_SSM, S_RAA, S_SKV_LISTA, S_SKV_ROT],
  "cta": ("Behöver fasaden ses över?", "Boka ett kostnadsfritt platsbesök så bedömer vi panel, puts och isolering."),
  "img": [
    ("Villa i Stockholm med ny liggande träpanel och nya fönsterbleck",
     "1950s Swedish one-and-a-half storey villa with gable roof, facade newly clad with uniform horizontal "
     "white-primed wooden panel boards, new metal window sills, light scaffolding along one wall, suburban Stockholm, overcast daylight"),
    ("Putsfasad med sprickor kring ett fönster",
     "close-up of a rendered lime plaster facade with freshly patched cracks around a white window, before "
     "painting, soft daylight, Stockholm"),
  ],
  "related": [
    ("malare.html", "Målare i Stockholm", "Fasad, fönster och invändig målning."),
    ("fonsterbyte.html", "Fönsterbyte i Stockholm", "Byta eller renovera fönster."),
    ("vindsisolering.html", "Vindsisolering", "Tilläggsisolering uppåt."),
    ("villarenovering.html", "Villarenovering", "Hela huset i en entreprenad."),
  ],
},
# ------------------------------------------------------------------ FÖNSTERBYTE
"fonsterbyte.html": {
  "kind": "hub", "service": "fonsterbyte", "svc_label": "Fönsterbyte",
  "title": "Fönsterbyte i Stockholm – nya fönster eller renovering",
  "description": "Fönsterbyte i Stockholm: när det lönar sig att byta, när äldre fönster bör renoveras, "
                 "U-värde och kallras, lov sedan 1 december 2025 och ROT.",
  "h1": "Fönsterbyte i Stockholm",
  "lead": "Ett fönsterbyte lönar sig bäst när de gamla fönstren är i dåligt skick. Är karm och bågar friska kan "
          "tätning eller energiglas på insidan ge en bättre totalkalkyl. Geal hjälper dig att välja, byter eller "
          "renoverar fönstren och tar hand om smygar, bleck och anslutningar mot fasaden.",
  "card": "Byta eller renovera fönster.",
  "sections": [
    {"id": "byta-eller-renovera", "anchor": "Byta eller renovera",
     "h2": "Byta eller renovera – fönstrens skick avgör",
     "paras": [
       f"{_x(BV_FONSTER, 'Boverkets energiguide')} sammanfattar valet tydligt. Att förbättra befintliga fönster "
       "ger oftast mindre energibesparing än nya, men kostar oftast mindre och kan därför ge en bättre "
       "totalkalkyl. Är fönstren i dåligt skick blir det tvärtom, eftersom en renovering då blir dyr. Ett typiskt "
       "fall där byte är motiverat är treglasfönster från 1970-talet där glaskassetten har slutat fungera och "
       "monteringen i instickskarmar ger stora energiförluster.",
       "Äldre träfönster med friska karmar kan ofta renoveras. Bågarna tas loss, gammal färg och kitt skrapas "
       "bort även i kittfalsen, skadat trä lagas, glasen kittas om och snickerierna målas. Riksantikvarieämbetet "
       "påpekar att fönstersnickerier hör till de mest utsatta delarna av ett hus och behöver målas om oftare "
       "än resten av fasaden.",
       "Innan något rivs ska gamla fogmassor och kitt undersökas. Boverket påminner om att fogmassor kan "
       "innehålla PCB eller asbest, som är saneringspliktigt, och att kitt kan innehålla asbest som ska hanteras "
       "enligt arbetsmiljöreglerna.",
     ],
     "aside": {"title": "Tecken på att byte ligger nära", "items": [
       "Glaskassetter som tappat funktion",
       "Röta i karm eller bågens nederkant",
       "Instickskarmar från 1970-talet",
       "Bågar som inte går att få täta"]}},
    {"id": "energi",
     "h2": "U-värde, kallras och vad ett nytt fönster gör",
     "paras": [
       "Fönster isolerar sämre än väggen runt omkring. Enligt Boverket motsvarar även de bästa fönstren bara "
       "ungefär fem centimeter vanlig isolering, och ett gammalt fönster släpper igenom betydligt mer. Ju lägre "
       "U-värde, desto mindre värme går förlorad, och som tumregel uppstår inget kallras när U-värdet är lägre "
       "än 1,0.",
       "Jämför U-värdet för hela fönstret – glas, båge och karm – och inte bara glaset. Tänk också på att bättre "
       "isolerade fönster får en kallare utsida, så att det oftare bildas kondens utvändigt, och att grövre "
       "profiler släpper in mindre dagsljus. Olika glas ger dessutom olika solskydd, ljudisolering och "
       "dagsljusinsläpp.",
       "Det enklaste steget är att täta: isoleringen runt karmen, drevningen och listerna mellan båge och karm. "
       "Nästa steg är att byta eller komplettera innerrutan med energiglas eller en tvåglaskassett. I ett äldre "
       "hus kan ventilationen vara beroende av luft som läcker in kring fönstren, så tilluften behöver "
       "kontrolleras när huset blir tätare.",
     ],
     "aside": {"title": "Inför beställningen", "items": [
       "U-värde för hela fönstret",
       "Glas för sol, buller och ljus",
       "Säkerhetsklass mot inbrott",
       "Brandklass om sådan finns",
       "Utrymningsväg vid brand"]}},
    {"id": "aldre-fonster",
     "h2": "Äldre fönster i kulturhistoriska hus",
     "paras": [
       "Fönstren är en stor del av ett hus uttryck. Boverket lyfter fram material, proportioner, indelning och "
       "profilering, och att äldre glas och invändig profilering kan betyda mycket för hur ett rum upplevs. Ett "
       "nytt fönster bör därför anpassas till husets ålder och karaktär, med samma indelning och liknande "
       "profiler.",
       "Behålls originalfönstren är det lättare att bevara kulturvärdet, och det går åt mindre nya material. "
       "Finns munblåst eller valsat glas kvar kan det flyttas till ytterbågarna när innerbågen får energiglas, "
       "så att utsidan behåller sitt gamla utseende. På ett hus där fönstren redan bytts mot olämpliga modeller "
       "kan ett nytt byte i stället bli ett sätt att återställa utseendet.",
       "Ofta hänger fönstren ihop med resten av väggen: ruttna smygar, trasiga bleck eller en fasad som ska "
       f"tilläggsisoleras. Läs mer om {_l('fasadrenovering.html', 'fasadrenovering')} och om "
       f"{_l('takfonster.html', 'takfönster')} om även taket berörs.",
     ],
     "aside": None},
    {"id": "lov",
     "h2": "Fönsterbyte och lov sedan 1 december 2025",
     "paras": [
       f"{_x(BV_FASAD, 'Boverket')} räknar byte eller ändring av fönster som en åtgärd som kan påverka "
       "byggnadens karaktärsdrag och därmed vara en fasadändring. För en- och tvåbostadshus krävs ändå inget "
       "bygglov för fasadändring sedan 1 december 2025, om inte huset omfattas av skyddsbestämmelser, är "
       "särskilt värdefullt, ligger i ett särskilt värdefullt område eller planen har utökad lovplikt.",
       "För flerbostadshus inom detaljplan krävs lov när fönstren sitter i en fasad mot gata, park eller annan "
       f"allmän plats. I Stockholms stad ger {_x(SSM, 'Stadsmuseets klassificeringskarta')} en första "
       "indikation; i övriga kommuner frågar du bygglovsenheten. Lovfritt betyder inte kravlöst – "
       "varsamhetskravet gäller, och bytet får inte strida mot detaljplanen.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går fönsterbytet till",
  "steps": [
    ("Besök och mätning", "Vi bedömer karmar, bågar och glas och mäter upp varje fönster."),
    ("Byte eller renovering", "Du får ett underlag för vilka fönster som bör bytas och vilka som kan renoveras."),
    ("Kontroll före start", "Lovfrågan, gamla fogmassor och kitt samt ventilationen ses över."),
    ("Skriftligt kostnadsförslag", "Fönstertyp, glas, montage, smygar, bleck och ROT-avdrag står specificerat."),
    ("Montage", "Gamla fönster tas ur och nya monteras; vid kyla kan arbetet göras med fönstertält."),
    ("Anslutningar och genomgång", "Drevning, tätning, foder och bleck görs klart och vi går igenom resultatet."),
  ],
  "rot_h2": "ROT-avdrag för fönsterbyte",
  "rot": [
    f"I småhus ger det ROT att reparera eller byta fönster, montera bullerglas och isolerglas och byta "
    f"fönsterbleck, enligt {_x(SKV_LISTA, 'Skatteverket')}. Solfilm och myggnät ger inte avdrag. Avdraget är "
    "30 procent av arbetskostnaden, högst 50 000 kronor per person och år och högst 75 000 kronor för ROT och "
    "RUT tillsammans. Själva fönstren räknas som material. Geal drar avdraget direkt på fakturan.",
    "I bostadsrätt ger bara arbete på insidan av befintliga fönster avdrag, till exempel att byta glaset i "
    "innerbågen eller montera tätningslist. Att byta fönster eller arbeta mellan bågarna eller på utsidan ger "
    "inte ROT.",
  ],
  "price_h2": "Vad styr kostnaden för fönsterbytet",
  "price": [
    "Antal och storlek på fönstren, material i båge och karm, vilket glas som väljs, om indelning och profiler "
    "ska anpassas till ett äldre hus, hur mycket smygar, foder och bleck som behöver göras om och om övre plan "
    "kräver ställning. Sanering av gammal fogmassa påverkar också.",
    "Efter ett kostnadsfritt platsbesök får du ett skriftligt kostnadsförslag med fönster, montage och "
    "ROT-avdrag specificerat.",
  ],
  "faq": [
    ("Går det att byta fönster mitt i vintern?",
     "Ja. Enligt Boverket kan fönster bytas och renoveras oavsett årstid, och när det är kallt kan man använda "
     "så kallade fönstertält."),
    ("Lönar det sig att byta treglasfönster från 1970-talet?",
     "Ofta, om glaskassetterna har slutat fungera och fönstren sitter i instickskarmar. Boverket nämner just "
     "den kombinationen som en källa till betydande energiförluster."),
    ("Vilket U-värde behövs för att slippa kallras vid fönstret?",
     "Boverkets tumregel är att kallras inte uppträder när U-värdet är lägre än 1,0. Jämför då värdet för hela "
     "fönstret, inte bara glaset."),
    ("Får jag ROT-avdrag för nya fönster i en bostadsrätt?",
     "Nej. I bostadsrätt ger bara arbete på insidan av befintliga fönster avdrag, till exempel nytt glas i "
     "innerbågen eller tätningslist."),
    ("Kan gammalt fönsterkitt innehålla asbest?",
     "Ja, det kan det. Boverket påminner om att kitt kan innehålla asbest och att äldre fogmassor kan innehålla "
     "PCB eller asbest. Det undersöks innan arbetet börjar och hanteras enligt arbetsmiljöreglerna."),
    ("Måste nya fönster ha samma spröjsindelning som de gamla?",
     "På en villa utan skyddsbestämmelser är det inget lovkrav, men Boverket rekommenderar att nya fönster "
     "anpassas till husets ålder och karaktär. I skyddade miljöer krävs lov, och då prövas utformningen."),
  ],
  "sources": [S_BV_FONSTER, S_BV_FASAD, S_STHLM, S_SSM, S_RAA, S_SKV_LISTA, S_SKV_ROT],
  "cta": ("Funderar du på nya fönster?", "Boka ett kostnadsfritt platsbesök så bedömer vi om fönstren ska bytas eller renoveras."),
  "img": [
    ("Äldre villa i Stockholm med nya vita träfönster med spröjs",
     "1920s Swedish ochre yellow wooden villa with vertical board-and-batten panel and newly installed white "
     "wooden two-pane windows with muntins, white window trim, suburban Stockholm garden, clear autumn day"),
    ("Fönsterbåge som renoveras med skrapad kittfals och nytt glas",
     "close-up of an old wooden window sash on a workbench being restored, scraped putty rebate, new glass pane, "
     "paint scraper and putty knife, soft daylight"),
  ],
  "related": [
    ("fasadrenovering.html", "Fasadrenovering i Stockholm", "Panel, puts och tilläggsisolering."),
    ("malare.html", "Målare i Stockholm", "Fasad, fönster och invändig målning."),
    ("takfonster.html", "Takfönster", "Nya fönster i taket."),
    ("villarenovering.html", "Villarenovering", "Hela huset i en entreprenad."),
  ],
},
}
