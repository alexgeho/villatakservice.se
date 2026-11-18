# -*- coding: utf-8 -*-
"""Hubbar för deltjänster (2026-11-18, SEO-plan 18.11 avsnitt 4a): golvslipning.html, fasadmalning.html,
tapetsering.html, fonsterrenovering.html. Var och en är den starka Stockholmssidan för sina 32 ortsidor.

Keyword Planner (OneDrive/KeyWords/2026-10-21, byggtorg_A/B.csv):
  golvslipning 500, offert golvslipning 50, golvslipning rotavdrag 50 ("golvslipning stockholm" finns inte i exporten);
  fasadmålning 500, fasadmålning pris/kostnad 50, offert fasadmålning 50 ("fasadmålning stockholm" finns inte i
  exporten; GSC 15.10–11.11: 107 visningar); tapetsering stockholm 50, offert tapetsering 50;
  renovera fönster 500, fönsterrenovering pris/kostnad 50 ("fönsterrenovering stockholm" finns inte i exporten).

Regler: inga nya priser eller siffror. Fakta är bara sådant som redan står på sajtens ortsidor med källa
(Golvbranschens riktlinjer SLIP/LACK/OLJA/UNDERHÅLL 22, Skatteverket, Boverket, Riksantikvarieämbetet,
Svenska Byggnadsvårdsföreningen) eller allmän arbetsbeskrivning utan tal. Inga garantier, omdömen, case eller cert.
Bilder: tre per hubb via tools/gen_images_flux.py (utan personer, som övriga sajten)."""

from tj_v15_golvslipning import _GBR_SLIP, _GBR_LACK, _GBR_OLJA, _GBR_UND, _GBR_LAMELL, _GBR_STAV
from tj_v15_fasadmalning import _BOV_FASAD, _BOV_YTA, _LST_TRA, _RAA
from tj_v15_tapetsering import _SBF_UND, _SBF_TAT
from tj_v16_fonsterrenovering import _RAA_F, _BV_F, _BV_ASB, _LST_F

_L = '<a class="text-link" href="{0}">{1}</a>'
_SKV = ("Skatteverket – Ger arbetet rätt till rotavdrag?",
        "https://www.skatteverket.se/foretag/skatterochavdrag/rotochrut/gerarbetetratttillrotavdrag.4.5c1163881590be297b5173bf.html")
_SKV2 = ("Skatteverket – Så fungerar rotavdraget",
         "https://www.skatteverket.se/privat/fastigheterochbostad/rotarbeteochrutarbete/safungerarrotavdraget.4.5947400c11f47f7f9dd80004014.html")
_ROT_SUM = ("Avdraget är 30 procent av arbetskostnaden, högst 50 000 kr per person och år och högst 75 000 kr "
            "tillsammans med rutavdrag.")

PAGES_TJ = {
# ================================================================== GOLVSLIPNING
"golvslipning.html": {
  "kind": "hub", "service": "golvslipning", "svc_label": "Golvslipning", "sort_ort": True,
  "crumb": "Golvslipning", "parent": ("Golvläggning", "golvlaggning.html"),
  "title": "Golvslipning Stockholm – slipa parkett och trägolv, ROT",
  "description": "Golvslipning i Stockholm: vi slipar parkett, brädgolv och trappor och ytbehandlar med lack, olja eller lut. Gratis platsbesök, ROT-avdrag på fakturan.",
  "h1": "Golvslipning i Stockholm",
  "lead": "Geal Entreprenad AB slipar parkett, brädgolv och trätrappor i villor, radhus och lägenheter i hela Stockholm och avslutar med lack, olja, hårdvaxolja eller lut och såpa. Du får ett gratis platsbesök och ett skriftligt kostnadsförslag, och ROT-avdraget dras direkt på fakturan. På den här sidan ser du vad som ingår, hur arbetet går till steg för steg, vad priset beror på och vilka golv som går att slipa.",
  "card": "Slipa parkett och trägolv – lack, olja eller lut.",
  "sections": [
    {"id": "ingar", "anchor": "Vad ingår",
     "h2": "Det här ingår i en golvslipning",
     "paras": [
       "En golvslipning tar bort den gamla ytbehandlingen och det översta, slitna träet, så att repor, gråa gångstråk och gulnad lack försvinner. Golvet slipas med bandmaskin i flera steg, från grovt till fint papper, och kanter och hörn tas med kantslip så att ytan får samma struktur ända ut till listen. Golvbranschens riktlinjer för slipning, SLIP 22, säger att finslipningen ska göras i träets längdriktning och att inga slipränder får finnas kvar annat än efter slutpappret.",
       "Före finslipningen lagar vi det som slipningen inte tar bort: lösa stavar limmas, uppstickande spik dras eller slås ned, djupa hack och kvisthål fylls och enstaka skadade brädor eller stavar byts. Sedan dammsugs golvet noga och ytbehandlas i flera lager. I ett vanligt uppdrag ingår också att vi skyddar angränsande rum, tar hand om slipdammet och går igenom skötseln av den nya ytan med dig.",
       "Ska ett nytt golv läggas i stället, eller är du osäker på om det gamla går att rädda, finns mer under " + _L.format("golvlaggning.html", "golvläggning i Stockholm") + ".",
     ],
     "aside": {"title": "Ingår normalt", "items": [
       "Gratis platsbesök och skriftligt kostnadsförslag", "Slipning i flera steg och kantslipning",
       "Lagning av hack, springor och lösa stavar", "Ytbehandling i flera lager",
       "Dammavskiljning och städning", "Skötselråd för den nya ytan"]}},
    {"id": "golvtyper",
     "h2": "Vilka golv går att slipa?",
     "paras": [
       "Massiva brädgolv av furu, gran eller ek och massiv stavparkett tål i regel flera slipningar, eftersom det finns mycket trä ovanför spontens överkant. Lamellparkett har ett tunnare toppskikt av ädelträ på en stomme av annat material, och där avgör slitskiktets tjocklek om en slipning till är möjlig. Laminat är en tryckt yta och går inte att slipa.",
       "Vi mäter innan vi lovar något. Vid platsbesöket lyfter vi en tröskel eller en golvlist, eller tittar i en springa, och ser hur mycket trä som finns kvar. På äldre lamellgolv finns en risk som Golvbranschen beskriver som stavsläpp: enstaka stavar i toppskiktet kan lossna när golvet slipas. Det berättar vi om i förväg, så att du vet vad som kan hända och hur det lagas.",
       "Mönsterlagda golv som fiskben och rutmönster slipas på ett eget sätt. Träet ligger åt olika håll, och enligt SLIP 22 slipas ett sådant golv normalt först diagonalt och sedan i rummets längdriktning eller från det håll ljuset kommer. Trappsteg och vilplan i trä slipas med mindre maskiner och för hand.",
     ],
     "aside": {"title": "Kontrolleras vid platsbesöket", "items": [
       "Massivt trä eller lamell", "Slitskiktets tjocklek", "Lösa stavar och svikt", "Spik, springor och fuktskador",
       "Vilken ytbehandling som sitter i dag"]}},
    {"id": "ytbehandling",
     "h2": "Lack, olja, hårdvaxolja eller lut och såpa",
     "paras": [
       "Efter slipningen är träet oskyddat, och valet av yta bestämmer både utseende och skötsel. Lack lägger en film ovanpå träet. Den tål slitage i hall och kök, är lätt att torka av och finns i olika glansgrader. Olja tränger ned i träet och ger en mattare yta som känns som trä. Ett oljat golv kan underhållas punktvis, till exempel i ett gångstråk, utan att hela rummet slipas om. Hårdvaxolja ligger mellan de två.",
       "Lut och såpa är den traditionella behandlingen på furu och gran och ger en ljus, matt yta. Luten är frätande, så angränsande ytor skyddstäcks, och Golvbranschens riktlinjer avråder från lack på ett lutat golv. Vill du ändra kulör, ljusare eller mörkare, görs det med pigment i oljan eller hårdvaxoljan, och vi gör då en provyta på ditt golv som du godkänner innan hela ytan behandlas.",
       "Riktlinjerna anger också under vilka förhållanden ytan ska läggas. Träet ska vara torrt, och rummet ska hålla normal rumstemperatur under behandlingen. Har golvet golvvärme sänks den före arbetet och höjs stegvis efteråt.",
     ],
     "aside": {"title": "Ytbehandlingar", "items": [
       "Lack – tålig film, lättstädat", "Olja – matt yta, punktvis underhåll", "Hårdvaxolja – mellanting",
       "Lut och såpa – ljus furu och gran", "Pigment – ny kulör efter provyta"]}},
    {"id": "damm",
     "h2": "Damm, ljud och säkerhet under arbetet",
     "paras": [
       "Golvslipning dammar och låter. Enligt Golvbranschens riktlinjer bör slipningen göras med partikelseparator eller cyklondammsugare med HEPA-filter, och den som slipar använder andningsskydd i klass P3 och hörselskydd. Vi stänger och tätar dörrar till övriga rum, så att dammet stannar där arbetet pågår.",
       "Slipdamm och oljiga trasor kan självantända. Riktlinjerna för underhåll säger att trasor, rondeller och slipdamm som varit i kontakt med oxiderande oljor ska läggas i vatten direkt efter användning. Dammsäcken töms och tas ut ur bostaden när arbetsdagen är slut.",
       "I en bostadsrätt hör golvet oftast till det du själv ansvarar för, men föreningens ordningsregler bestämmer när bullrande arbeten får pågå. Vi lägger slipdagarna efter de reglerna och går igenom tidplanen med dig före start, så att du kan berätta för grannarna vilka dagar det låter.",
     ],
     "aside": None},
    {"id": "underhall",
     "h2": "Underhåll som skjuter upp nästa slipning",
     "paras": [
       "Ett trägolv tål bara ett visst antal slipningar, så den billigaste slipningen är den som inte behöver göras. Ett lackat golv kan fräschas upp med lackrefresher eller lackas över innan slitaget har gått igenom lacken och ned i träet. Före en överlackering görs ett vidhäftningsprov, eftersom rester av vax, polish eller olämpliga rengöringsmedel kan hindra den nya lacken från att fästa.",
       "Ett oljat golv underhålls med ny olja där ytan har blivit torr och matt, oftast i gångstråken, och städas med en golvsåpa som återfettar. Ett såpat golv skuras med såpa. Oavsett yta gör möbeltassar, en dörrmatta som fångar gruset och torr eller lätt fuktig städning mer för golvets livslängd än något annat. Vilken skötsel som gäller för just din yta går vi igenom när arbetet är klart.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en golvslipning till – steg för steg",
  "steps": [
    ("Platsbesök", "Vi tittar på golvet, kontrollerar slitskiktet och mäter ytorna. Besöket är gratis."),
    ("Skriftligt kostnadsförslag", "Slipning, lagning och ytbehandling står som egna poster, med ROT-avdraget uträknat."),
    ("Förberedelse", "Rummen töms, spik tas bort, lösa stavar limmas och dörrar till övriga rum tätas."),
    ("Slipning", "Grov-, mellan- och finslipning med dammavskiljare, och kantslip längs väggar och i hörn."),
    ("Ytbehandling", "Lack, olja, hårdvaxolja eller lut läggs i flera lager med torktid emellan."),
    ("Genomgång", "Vi går igenom golvet med dig och lämnar skötselråd för den yta du har valt."),
  ],
  "time_h2": "Hur lång tid tar en golvslipning?",
  "time": [
    "Ett golvjobb består av dagar med maskiner och dagar då lacken eller oljan torkar och rummet står tyst. Hur många dagar det blir beror på ytan, antalet rum, hur mycket som ska lagas och vilken ytbehandling du väljer. En pigmenterad produkt behöver längre torktid mellan lagren än en opigmenterad, och lut ska ligga ett dygn innan överskottet jämnas av.",
    "Enligt Golvbranschens riktlinjer för lackering kan rummet normalt möbleras efter minst ett dygn, medan mattor och andra täta material bör vänta minst en vecka och starkt slitage minst två veckor. Tidplanen för just ditt golv står i kostnadsförslaget.",
  ],
  "rot_h2": "Så fungerar ROT-avdraget vid golvslipning",
  "rot": [
    "Att slipa golv finns med bland Skatteverkets exempel på rotarbeten, både i småhus och i bostadsrätt. I bostadsrätten ska du ha underhållsansvaret för golvet enligt föreningens stadgar, och arbetet ska göras inne i bostaden. Även fritidshus räknas som småhus.",
    _ROT_SUM + " Avdraget gäller bara arbetad tid på plats hos dig – lack, olja och resor ger inget avdrag. Vid en golvslipning är det mesta av kostnaden arbete, och därför får avdraget stor betydelse. Geal drar avdraget direkt på fakturan och ansöker om utbetalningen hos Skatteverket, så du betalar bara din del.",
  ],
  "price_h2": "Vad beror priset på?",
  "price": [
    "Vi publicerar inga prislistor för golvslipning, eftersom två golv med samma yta kan kräva helt olika mycket arbete. Det som väger tyngst är golvytan och antalet rum, golvets skick och hur mycket som ska lagas före slipningen, vilken ytbehandling du väljer och hur många lager den kräver, samt om trappa, trösklar och lister ingår. Ett golv som ska fram under en gammal matta kräver mer förarbete än ett lackat parkettgolv.",
    "Efter platsbesöket får du ett skriftligt kostnadsförslag där arbete och material står var för sig och ROT-avdraget är uträknat. Besöket och kostnadsförslaget är gratis.",
  ],
  "faq": [
    ("Vad kostar golvslipning i Stockholm?",
     "Det beror på ytan, golvets skick, hur mycket som ska lagas och vilken ytbehandling du väljer. Vi kommer ut gratis, tittar på golvet och lämnar ett skriftligt kostnadsförslag med ROT-avdraget uträknat."),
    ("Går det att slipa lamellparkett?",
     "Ja, om slitskiktet räcker. Vi kontrollerar tjockleken vid en tröskel eller i en springa innan vi föreslår slipning, och berättar om risken för stavsläpp på äldre lamellgolv."),
    ("Ska jag välja lack eller olja efter golvslipningen?",
     "Lack ger en tålig film som passar hall och kök. Olja ger en mattare yta som kan underhållas punktvis utan ny slipning. Vi visar skillnaden på en provyta om du är osäker."),
    ("Hur snart kan vi möblera efter att golvet har lackats?",
     "Enligt Golvbranschens riktlinjer kan rummet normalt möbleras efter minst ett dygn. Mattor och andra täta material bör vänta minst en vecka."),
    ("Får jag rotavdrag för golvslipning i en bostadsrätt i Stockholm?",
     "Ja. Skatteverket räknar slipning av golv som rotarbete i bostadsrätt, om du har underhållsansvaret för golvet enligt stadgarna och arbetet görs inne i bostaden."),
    ("Dammar det mycket när golvet slipas?",
     "Maskinerna är kopplade till dammavskiljare med HEPA-filter, och dörrar till övriga rum tätas. Lite fint damm kan ändå förekomma i rummet där vi arbetar, och vi städar innan ytbehandlingen."),
  ],
  "sources": [_GBR_SLIP, _GBR_LACK, _GBR_OLJA, _GBR_UND, _GBR_LAMELL, _GBR_STAV, _SKV, _SKV2],
  "cta": ("Dags att slipa golvet?", "Boka ett gratis platsbesök, så kontrollerar vi golvet och lämnar ett skriftligt kostnadsförslag med ROT-avdraget uträknat."),
  "img": [
    ("Nyslipat och lackat plankgolv av ek i ett ljust, tomt vardagsrum",
     "empty living room in a Swedish apartment from the 1930s with a freshly sanded and matte lacquered light oak plank floor, long straight parallel boards running towards the window, plain white walls, a simple white painted panel door, tall window with white frame and deep window sill, white skirting boards, soft Nordic daylight"),
    ("Slipmaskin med dammpåse på ett nyslipat brädgolv av furu",
     "a heavy professional drum floor sanding machine seen from the side, a low wide metal body on two wheels with a long angled handle bar and a grey cloth dust collection bag hanging from the handle, standing on a pine plank floor in an empty room; behind the machine the floor is freshly sanded natural pale raw pine, in front of the machine the floor is still old glossy dark amber varnish with scratches; white walls, window light"),
    ("Tre provbitar och en pensel på en ekyta",
     "close-up of a freshly sanded oak floor with three neat rectangular sample patches side by side, one clear matte lacquer, one natural oil and one white pigmented oil, a clean brush lying on a folded cloth beside them"),
  ],
  "related": [
    ("golvlaggning.html", "Golvläggning i Stockholm", "Nytt golv när det gamla inte går att slipa."),
    ("snickare.html", "Snickare i Stockholm", "Trösklar, lister och trappor."),
    ("malare.html", "Målare i Stockholm", "Väggar och snickerier före golvet."),
    ("villarenovering.html", "Villarenovering", "Golvet som del av en större renovering."),
  ],
},

# ================================================================== FASADMÅLNING
"fasadmalning.html": {
  "kind": "hub", "service": "fasadmalning", "sort_ort": True, "svc_label": "Fasadmålning",
  "crumb": "Fasadmålning", "parent": ("Målare", "malare.html"),
  "title": "Fasadmålning Stockholm – måla om huset, ROT på fakturan",
  "description": "Fasadmålning i Stockholm: tvätt, skrapning, grundning och två strykningar på trä och puts, med ställning. Gratis platsbesök, ROT-avdrag på fakturan.",
  "h1": "Fasadmålning i Stockholm",
  "lead": "Geal Entreprenad AB målar om träfasader och putsade fasader på villor och radhus i hela Stockholm, med tvätt, skrapning, grundning och två strykningar. Du får ett gratis platsbesök och ett skriftligt kostnadsförslag, och ROT-avdraget dras direkt på fakturan. Här ser du vad som ingår, hur arbetet går till, vad priset beror på och vad som gäller för färgtyp, kulör och lov.",
  "card": "Måla om träfasad eller puts – med ställning.",
  "sections": [
    {"id": "ingar", "anchor": "Vad ingår",
     "h2": "Det här ingår i en fasadmålning",
     "paras": [
       "Det mesta av en fasadmålning är förarbete. Fasaden tvättas så att smuts, alger och kritande färg försvinner, och sedan får den torka. Lös och flagnande färg skrapas bort för hand, spik som har krupit upp slås i och skadade brädor byts. Bart trä grundas, och därefter stryks fasaden två gånger.",
       "Foder, knutar, vindskivor och takfot hör till fasaden och målas i samma omgång, liksom fönstrens utsidor om du vill. Fönster, mark och planteringar närmast huset täcks under arbetet. Ställning eller lift ingår i kostnadsförslaget, och på höga gavlar är ställningen en förutsättning för att skrapa och måla ordentligt.",
       "Visar det sig vid skrapningen att panelen är rötskadad, eller att putsen har släppt, räcker det inte att måla. Då beskriver vi vad som behöver bytas eller lagas innan färgen läggs på – mer om det finns under " + _L.format("fasadrenovering.html", "fasadrenovering") + ".",
     ],
     "aside": {"title": "Ingår normalt", "items": [
       "Gratis platsbesök och skriftligt kostnadsförslag", "Ställning och skyddstäckning",
       "Tvätt och skrapning", "Byte av enstaka skadade brädor", "Grundning av bart trä",
       "Två strykningar på fasad, foder och knutar"]}},
    {"id": "fargtyp",
     "h2": "Rätt färgtyp för trä och puts",
     "paras": [
       "Den nya färgen ska passa det som redan sitter på väggen. På en träfasad kan det finnas linoljefärg, alkydoljefärg eller plastfärg i olika lager, och vid platsbesöket skrapar vi fram lagren på några ställen för att se vad vi målar på. Slamfärg, som den röda på ohyvlad panel, är matt, vattenspädbar och fuktgenomsläpplig, och en slamfärgad fasad målas om med slamfärg.",
       "Boverket skriver att akrylatfärg är en tät plastfärg som kräver grundfärg av alkydolja, och att panel där grunden hoppats över har fuktats upp kraftigt av regn. Därför grundar vi bart trä innan täckfärgen läggs på. På hyvlad panel som bär linoljefärg fortsätter vi med linoljefärg. Enligt Riksantikvarieämbetet kan få färgtyper målas i så många skikt utan att den gamla färgen måste tas bort.",
       "En putsad fasad målas med en färg som passar putsen under. Vi tar reda på vilken puts och vilken färg som sitter där i dag innan vi föreslår något, eftersom en tät färg på en puts som behöver andas kan stänga inne fukt.",
     ],
     "aside": {"title": "Det här avgör färgvalet", "items": [
       "Trä eller puts", "Hyvlad eller ohyvlad panel", "Vilken färg som sitter där i dag",
       "Hur mycket gammal färg som måste bort"]}},
    {"id": "kulor",
     "h2": "Kulör, provytor och bygglov",
     "paras": [
       "En kulör ser annorlunda ut på en hel fasad än på en färgkarta. Vi målar därför provytor direkt på huset, gärna i både sol och skugga, och du väljer när du har sett dem i dagsljus. Foder och knutar provas tillsammans med fasadkulören.",
       "Enligt Boverket krävs inget bygglov för att byta kulör på ett en- eller tvåbostadshus, utom där utökad lovplikt gäller. Ligger huset i ett område som kommunen har pekat ut som särskilt värdefullt, eller är byggnaden själv särskilt värdefull, kan lov krävas även för ommålning. Boverket påpekar också att ett byte av färgtyp, till exempel från linoljefärg till plastfärg, kan påverka byggnadens yttre karaktärsdrag.",
       "Reglerna tillämpas av kommunen, och detaljplanen kan ha egna bestämmelser. Är du osäker ger kommunens bygglovsavdelning besked för din fastighet.",
     ],
     "aside": {"title": "Före kulörbytet", "items": [
       "Provytor på fasaden", "Kontroll av detaljplanen", "Fråga till kommunen vid värdefull miljö"]}},
    {"id": "vader",
     "h2": "Väder, säsong och ställning",
     "paras": [
       "Utvändig målning är ett säsongsarbete. Fasaden ska vara torr när den målas, och färgen behöver tid att torka mellan strykningarna. Vi lägger därför arbetet inom säsongen, med marginal för regn och för att en tvättad fasad ska hinna torka innan grundningen.",
       "Väderstrecken behandlas olika. En sydfasad i stark sol torkar fort och målas hellre när solen har gått vidare, medan en nordsida kan behöva längre tid efter tvätten. På en putsad fasad kan ställningen behöva täckas in för att skydda mot slagregn och för snabb uttorkning medan färgen härdar.",
     ],
     "aside": None},
    {"id": "snickerier",
     "h2": "Foder, knutar, fönster och plåt i samma omgång",
     "paras": [
       "När ställningen ändå står runt huset lönar det sig att ta allt som nås från den. Vindskivor, takfot och foder är de delar som är mest utsatta för väder, och de visar ofta skador tidigare än själva panelen. Ändträ nedtill på panelbrädor och knutar suger vatten och grundas därför extra noga.",
       "Fönstrens utsidor kan målas i samma omgång. Har bågarna sprucket kitt eller röta i bottenstyckena räcker det inte med färg, och då beskriver vi vad som behöver göras under " + _L.format("fonsterrenovering.html", "fönsterrenovering") + ". Fönsterbleck, stuprör och hängrännor ses över medan de är åtkomliga, och det som ska bytas hör till " + _L.format("platslagare.html", "plåtslagarens") + " arbete.",
       "Vi skriver ut i kostnadsförslaget vilka delar som ingår, så att det inte uppstår frågor om vad som räknas till fasaden.",
     ],
     "aside": {"title": "Nås från ställningen", "items": [
       "Vindskivor och takfot", "Foder och knutar", "Fönstrens utsidor", "Fönsterbleck, hängrännor och stuprör"]}},
    {"id": "underhall",
     "h2": "Så håller den nya färgen längre",
     "paras": [
       "En målad fasad behöver tillsyn mellan ommålningarna. Gå runt huset en gång om året och titta särskilt på söder- och västsidan, på brädornas nederkanter och på vågräta ytor där vatten blir stående. Små skador som bättras i tid hindrar att vatten tar sig in bakom färgen.",
       "Håll växtlighet och jord borta från panelens nederkant, rensa hängrännorna så att vatten inte rinner över fasaden och tvätta bort alger och smuts med mjuk borste. Linoljefärg kritar och mattas med tiden, vilket är normalt och gör fasaden lätt att måla om utan att all gammal färg behöver tas bort.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fasadmålning till – steg för steg",
  "steps": [
    ("Platsbesök", "Vi skrapar fram färglagren på några ställen och tittar på panel, puts och snickerier. Besöket är gratis."),
    ("Skriftligt kostnadsförslag", "Förarbete, färgtyp, antal strykningar och ställning står var för sig, med ROT-avdraget uträknat."),
    ("Kulör och provytor", "Provytor målas på fasaden, och vid behov kontrolleras detaljplanen med kommunen."),
    ("Ställning, tvätt och skrapning", "Ställningen reses, fasaden tvättas och får torka, och lös färg skrapas bort."),
    ("Grundning och strykning", "Bart trä grundas och fasaden stryks två gånger i lämpligt väder."),
    ("Genomgång", "Vi går runt huset med dig, bättrar det som behövs och river ställningen."),
  ],
  "time_h2": "Hur lång tid tar en fasadmålning?",
  "time": [
    "Tiden beror på fasadens yta och höjd, hur mycket gammal färg som ska bort och på vädret. Själva strykningarna är den kortaste delen. Mellan tvätt och grundning ska fasaden torka, och mellan strykningarna ska färgen torka, och de pauserna styrs av temperatur och luftfuktighet snarare än av oss.",
    "Tidplanen står i kostnadsförslaget. Regnar det flyttar vi arbetsdagarna i stället för att tumma på kvaliteten – vi målar inte på en blöt fasad för att hålla ett datum.",
  ],
  "rot_h2": "Så fungerar ROT-avdraget vid fasadmålning",
  "rot": [
    "Skatteverket ger rotavdrag för att måla och rengöra fasaden på ett småhus, och för att montera och montera ned en byggnadsställning i samband med arbetet. Det gäller villor, radhus och fritidshus som du äger. Är radhuset en bostadsrätt ger fasadmålning däremot inget avdrag, eftersom fasaden då är föreningens ansvar.",
    _ROT_SUM + " Färg, material och resor ger inget avdrag. Geal drar avdraget direkt på fakturan och ansöker om utbetalningen hos Skatteverket, så du betalar bara din del.",
  ],
  "price_h2": "Vad beror priset på?",
  "price": [
    "Vi publicerar inga prislistor för fasadmålning, eftersom förarbetet skiljer mycket mellan två hus av samma storlek. Det som väger tyngst är fasadens yta och höjd, hur mycket gammal färg som måste skrapas bort, om brädor behöver bytas, vilken färgtyp underlaget kräver och hur många foder, knutar, vindskivor och fönster som ska målas. Behovet av ställning eller lift påverkar också.",
    "Efter platsbesöket får du ett skriftligt kostnadsförslag där arbete, material och ställning står var för sig och ROT-avdraget är uträknat. Besöket och kostnadsförslaget är gratis.",
  ],
  "faq": [
    ("Vad kostar fasadmålning i Stockholm?",
     "Det beror på fasadens yta och höjd, hur mycket gammal färg som ska bort, färgtypen och antalet snickerier. Vi kommer ut gratis och lämnar ett skriftligt kostnadsförslag med ROT-avdraget uträknat."),
    ("När på året kan fasaden målas om?",
     "Under den varma delen av året, när fasaden hinner torka efter tvätten och färgen torkar mellan strykningarna. Vi planerar arbetet med marginal för regn."),
    ("Behöver jag bygglov för att byta kulör på villan?",
     "Enligt Boverket krävs inget bygglov för kulörbyte på ett en- eller tvåbostadshus, utom där utökad lovplikt gäller eller där byggnaden eller området är särskilt värdefullt. Kommunen ger besked för din fastighet."),
    ("Ingår ställningen i rotavdraget?",
     "Ja. Skatteverket räknar arbetet med att montera och montera ned en byggnadsställning som rotarbete när det görs i samband med fasadmålningen på ett småhus."),
    ("Måste all gammal färg skrapas bort?",
     "Nej, bara den som sitter löst eller flagnar. Färg som sitter fast är ett bra underlag, men den nya färgen måste passa färgtypen under."),
    ("Kan ni måla en putsad fasad i Stockholm?",
     "Ja. Vi tar först reda på vilken puts och färg som sitter på väggen, lagar sprickor och släpp och väljer en färg som passar putsen."),
    ("Målar ni fönster och foder när fasaden målas om?",
     "Ja. Foder, knutar, vindskivor och fönstrens utsidor målas i samma omgång om du vill, och det står som egna poster i kostnadsförslaget."),
  ],
  "sources": [_BOV_FASAD, _BOV_YTA, _LST_TRA, _RAA, _SKV, _SKV2],
  "cta": ("Dags att måla om huset?", "Boka ett gratis platsbesök, så tittar vi på fasaden och lämnar ett skriftligt kostnadsförslag med ROT-avdraget uträknat."),
  "img": [
    ("Nymålad gul trävilla med vita knutar och foder i en trädgård",
     "freshly painted pale yellow Swedish two-storey wooden villa from the 1920s with vertical board panel, white corner boards and white window trim, red clay tile roof, an ordinary sized white front door with a small porch and two steps, green lawn, birch trees and lilac bushes, gravel path, clear summer daylight, eye-level view from the garden"),
    ("Träpanel under ommålning: skrapat trä, vit grundfärg och färdigmålad röd yta",
     "close-up of the vertical wooden panel wall of a Swedish house being repainted, the left third scraped down to bare weathered grey-brown wood, the middle third primed matte white, the right third freshly painted in deep falu red, a paint brush lying across an open paint can on a simple wooden trestle in front of the wall, green grass below, soft daylight"),
    ("Tre provytor i grått, gult och rött målade på en träpanel",
     "close-up of a vertical wooden panel facade with three painted colour sample patches side by side in light grey, warm yellow and falu red, a paint brush resting on an open paint can on a trestle in front, soft daylight"),
  ],
  "related": [
    ("malare.html", "Målare i Stockholm", "Målning inomhus och utomhus."),
    ("fasadrenovering.html", "Fasadrenovering i Stockholm", "Ny panel, puts och tilläggsisolering."),
    ("fonsterrenovering.html", "Fönsterrenovering i Stockholm", "Kitt och linoljefärg på gamla fönster."),
    ("takmalning.html", "Takmålning", "Målning av plåt- och betongtak."),
  ],
},

# ================================================================== TAPETSERING
"tapetsering.html": {
  "kind": "hub", "service": "tapetsering", "sort_ort": True, "svc_label": "Tapetsering",
  "crumb": "Tapetsering", "parent": ("Målare", "malare.html"),
  "title": "Tapetsering Stockholm – tapetserare med gratis offert",
  "description": "Tapetsering i Stockholm: vi tar ned gammal tapet, lagar och förlimmar väggen och sätter upp ny tapet med mönsterpassning. Gratis besök, ROT på fakturan.",
  "h1": "Tapetsering i Stockholm",
  "lead": "Geal Entreprenad AB tapetserar i lägenheter, radhus och villor i hela Stockholm: vi tar ned gamla tapeter, lagar och förlimmar väggen och sätter upp den nya tapeten med mönstret passat. Du får ett gratis platsbesök och ett skriftligt kostnadsförslag, och ROT-avdraget dras direkt på fakturan. Här ser du vad som ingår, hur arbetet går till, vad priset beror på och vad väggen kräver innan första våden kommer upp.",
  "card": "Ny tapet – underarbete och uppsättning.",
  "sections": [
    {"id": "ingar", "anchor": "Vad ingår",
     "h2": "Det här ingår i en tapetsering",
     "paras": [
       "En tapet blir inte bättre än väggen under. Därför börjar arbetet med att golv, lister och möbler skyddas och att den gamla tapeten tas ned eller, när den sitter fast och är slät, behålls som underlag. Sedan lagas hål och sprickor, skarvar spacklas och slipas och väggen grundas eller förlimmas så att klistret får fäste.",
       "Därefter mäts våderna ut från en lodlinje, mönstret passas i höjd och våderna sätts kant i kant. Vi skär rent mot tak, lister, foder och eluttag och går över skarvarna innan klistret har torkat.",
       "Ska väggar eller tak målas i samma rum gör vi det före tapeten – mer om det finns under " + _L.format("malare.html", "målare i Stockholm") + ".",
     ],
     "aside": {"title": "Ingår normalt", "items": [
       "Gratis platsbesök och skriftligt kostnadsförslag", "Skydd av golv, lister och möbler",
       "Nedtagning av gammal tapet", "Spackling, slipning och förlimning",
       "Uppsättning med mönsterpassning", "Städning efter arbetet"]}},
    {"id": "tapettyper",
     "h2": "Papper, non-woven eller vinyl",
     "paras": [
       "Papperstapet är den klassiska tapeten. Den klistras på baksidan, får svälla en stund och sätts sedan upp, och den kräver en jämn vägg eftersom ojämnheter syns igenom. Non-woventapet har en baksida av fiber som inte sväller. Där läggs klistret direkt på väggen, vilket gör uppsättningen snabbare och skarvarna lättare att få täta. Vinyltapet har ett ytskikt av plast som tål avtorkning.",
       "Valet handlar inte bara om mönster. Svenska Byggnadsvårdsföreningen varnar för täta, vattenavvisande skikt i gamla hus och nämner att mögel har förekommit bakom moderna tapeter som sätts upp med klister på väggen. I ett hus som är uppvärmt året runt är det sällan ett problem, men i ett äldre hus eller ett hus som står kallt delar av året väljer vi hellre en papperstapet med stärkelseklister, som släpper igenom fukt.",
       "Stora mönster ger mer spill, eftersom varje våd måste passas mot den förra. Det räknar vi med när antalet rullar bestäms. Rullar från en senare tillverkningsomgång kan skilja i nyans, så antalet bör stämma från början.",
     ],
     "aside": {"title": "Tre tapettyper", "items": [
       "Papper – klassisk, kräver slät vägg", "Non-woven – klister på väggen, formstabil", "Vinyl – avtorkningsbar yta"]}},
    {"id": "underlag",
     "h2": "Väggen under tapeten",
     "paras": [
       "Hur mycket underarbete som behövs syns först när en kant lyfts. I äldre lägenheter kan flera lager tapet sitta på varandra, ibland på spänd papp. I hus från 1920- till 1950-talen är putsväggarna ofta kriderade, alltså strukna med en kritblandning som ger dålig vidhäftning om den inte tvättas bort eller binds. På gipsskivor är det spacklingarna som är känsliga, eftersom de oftast inte är förlimmade.",
       "På en frilagd och lagad putsvägg råder Svenska Byggnadsvårdsföreningen att förlimma och klistra upp en täckpapp innan den nya tapeten. Förlimningen gör att väggen suger jämnt, och pappen ger ett slätt underlag. När en tapet släpper efter kort tid beror det enligt föreningen oftast på att underlaget inte var tillräckligt torrt eller inte förlimmat.",
       "Vi provar därför väggen innan vi lämnar kostnadsförslaget och skriver ut vilket underarbete som ingår.",
     ],
     "aside": {"title": "Kontrolleras vid platsbesöket", "items": [
       "Antal tapetlager", "Puts, gips eller spänd papp", "Kridering eller gammal limfärg",
       "Sprickor, hål och lösa partier", "Fukt i väggen"]}},
    {"id": "fukt",
     "h2": "Kök, badrum och hus som står kalla",
     "paras": [
       "Tapet i kök fungerar bra på väggar som inte utsätts för stänk, och där väljer vi en yta som går att torka av. I badrummets våtzoner hör tapet inte hemma – där krävs tätskikt, och det beskriver vi under " + _L.format("badrumsrenovering.html", "badrumsrenovering") + ".",
       "I oeldade sommarhus och äldre hus med hög fuktighet skadas papperstapeter långsamt, skriver Svenska Byggnadsvårdsföreningen, och det syns som lösa skarvar, fuktfläckar och svarta prickar. Sitter det en tät tapet eller ett tätt färgskikt på en vägg i ett hus som står kallt kan fukt samlas bakom ytan. Då tar vi ned det täta skiktet innan väggen förlimmas och väljer en tapet som passar huset.",
       "I en bostadsrätt är tapetsering något du normalt får göra utan att fråga föreningen. Finns det äldre tapetlager eller målade tak som kan ha kulturvärde fotograferar vi dem och sparar en bit innan något tas ned.",
     ],
     "aside": None},
    {"id": "monster",
     "h2": "Mönsterpassning, hörn och detaljer",
     "paras": [
       "Det som skiljer en bra tapetsering från en dålig syns i detaljerna. Första våden sätts efter en lodlinje och inte efter ett hörn eller en dörrkarm, eftersom väggar i äldre hus sällan står i lod. Vi väljer var i rummet mönstret ska börja, oftast mitt på den vägg som syns först, så att mönstret hamnar symmetriskt där ögat landar och den oundvikliga skarven där mönstret inte går ihop hamnar i ett undanskymt hörn.",
       "I hörn delas våden så att tapeten går runt hörnet med en smal remsa, i stället för att en hel våd viks om och spricker när huset rör sig. Runt eluttag och strömbrytare skärs tapeten in under locket, och mot tak, lister och foder skärs den med vass kniv mot en bredspackel. Ojämna tak och sneda lister döljs bäst med ett litet mönster eller en enfärgad tapet, och det säger vi vid platsbesöket.",
       "Tapet på en enda vägg, en fondvägg, följer samma arbetsgång. Där blir mötet mot de målade väggarna viktigast, och vi målar därför de andra väggarna först.",
     ],
     "aside": {"title": "Det här avgör resultatet", "items": [
       "Första våden i lod", "Mönstret centrerat på huvudväggen", "Delad våd i hörnen", "Rena snitt mot tak och lister"]}},
    {"id": "forbered",
     "h2": "Så förbereder du rummet",
     "paras": [
       "Du behöver inte tömma rummet helt. Det räcker att möblerna ställs mitt på golvet så att vi kommer åt väggarna, och att tavlor, hyllor och gardinstänger tas ned. Lösa lock till eluttag och strömbrytare skruvar vi av själva, med strömmen bruten.",
       "Har du redan köpt tapeten är det bra om rullarna ligger framme vid platsbesöket, så att vi kan kontrollera att alla har samma tillverkningsnummer och räkna om de räcker. Vill du ha hjälp att räkna innan du beställer gör vi det på plats.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en tapetsering till – steg för steg",
  "steps": [
    ("Platsbesök", "Vi lyfter en kant, ser vad som sitter på väggen och mäter rummen. Besöket är gratis."),
    ("Skriftligt kostnadsförslag", "Nedtagning, underarbete och uppsättning står var för sig, med ROT-avdraget uträknat."),
    ("Skydd och nedtagning", "Golv och lister täcks, och gamla tapeter blöts upp och tas ned där de inte kan sitta kvar."),
    ("Underarbete", "Hål och sprickor lagas, väggen spacklas, slipas och förlimmas och får torka."),
    ("Uppsättning", "Våderna sätts från en lodlinje med mönstret passat och skärs rent mot tak och lister."),
    ("Genomgång", "Vi går igenom rummen och skarvarna med dig när arbetet är klart."),
  ],
  "time_h2": "Hur lång tid tar en tapetsering?",
  "time": [
    "Tiden beror på antalet rum, hur många lager som ska ned och hur mycket väggen behöver lagas. Själva uppsättningen går fortast. Det som tar tid är underarbetet, eftersom spackel och förlimning ska torka innan tapeten kommer upp – en tapet som sätts på ett fuktigt underlag riskerar att släppa.",
    "Tidplanen står i kostnadsförslaget. Rummet går att använda när klistret har torkat.",
  ],
  "rot_h2": "Så fungerar ROT-avdraget vid tapetsering",
  "rot": [
    "Skatteverket räknar tapetsering som rotarbete i bostadsrätt, ägarlägenhet och småhus. I bostadsrätten ska arbetet göras inne i bostaden, innanför dess tak, väggar och golv.",
    _ROT_SUM + " Material som tapet och klister ger inget avdrag, och inte heller resor. Eftersom underarbete och uppsättning är arbetad tid på plats hos dig ger det mesta av kostnaden underlag för rotavdraget. Geal drar avdraget direkt på fakturan och ansöker om utbetalningen hos Skatteverket, så du betalar bara din del.",
  ],
  "price_h2": "Vad beror priset på?",
  "price": [
    "Vi publicerar inga prislistor för tapetsering, eftersom underarbetet avgör mer än väggytan. Det som väger tyngst är hur många lager som ska ned, hur mycket väggen behöver lagas och spacklas, takhöjden, antalet fönster, dörrar och hörn att skära runt och hur krävande mönstret är att passa. Tapeten väljer och köper du själv eller genom oss, och den redovisas som material.",
    "Efter platsbesöket får du ett skriftligt kostnadsförslag där arbete och material står var för sig och ROT-avdraget är uträknat. Besöket och kostnadsförslaget är gratis.",
  ],
  "faq": [
    ("Vad kostar tapetsering i Stockholm?",
     "Det beror på hur många lager som ska ned, hur mycket väggen behöver lagas, takhöjden och mönstret. Vi kommer ut gratis och lämnar ett skriftligt kostnadsförslag med ROT-avdraget uträknat."),
    ("Måste den gamla tapeten tas ned först?",
     "Inte i varje rum. En slät tapet som sitter fast kan fungera som underlag, men lösa, strukturerade eller täta tapeter tas ned. Det avgör vi när vi har lyft en kant."),
    ("Får jag rotavdrag för tapetsering i en bostadsrätt i Stockholm?",
     "Ja. Skatteverket räknar tapetsering som rotarbete i bostadsrätt när arbetet görs inne i bostaden. Tapet och klister är material och ger inget avdrag."),
    ("Vilken tapet passar i ett äldre hus?",
     "I ett hus som står kallt delar av året, eller där väggarna behöver släppa igenom fukt, väljer vi hellre papperstapet med stärkelseklister än en tapet med tätt ytskikt."),
    ("Hur många rullar tapet behövs?",
     "Det beror på väggytan, takhöjden och mönstrets rapport. Vi räknar ut antalet vid platsbesöket. Köp alla rullar ur samma tillverkningsomgång, eftersom nyansen kan skilja mellan omgångar."),
    ("Varför släpper en ny tapet från väggen?",
     "Enligt Svenska Byggnadsvårdsföreningen beror det oftast på att underlaget inte var tillräckligt torrt eller inte förlimmat. Därför låter vi spackel och förlimning torka innan tapeten sätts upp."),
    ("Kan ni tapetsera en fondvägg i en lägenhet i Stockholm?",
     "Ja. En fondvägg följer samma arbetsgång som ett helt rum: väggen lagas och förlimmas, och tapeten sätts med mönstret centrerat. Målas övriga väggar gör vi det först."),
  ],
  "sources": [_SBF_UND, _SBF_TAT, _SKV, _SKV2],
  "cta": ("Dags för ny tapet?", "Boka ett gratis platsbesök, så provar vi väggen och lämnar ett skriftligt kostnadsförslag med ROT-avdraget uträknat."),
  "img": [
    ("Nytapetserat sovrum med blommig tapet i en lägenhet i Stockholm",
     "empty bedroom in an older Stockholm apartment with freshly hung floral botanical wallpaper in muted green on all walls, perfectly matched seams, white ceiling, white painted skirting boards and door frame, wooden floor covered with protective paper along the wall, soft daylight from a window"),
    ("Tapetbord med en tapetrulle, klisterhink och pensel i ett rum med skyddstäckt golv",
     "a plain wooden folding wallpaper pasting table in a room under renovation, a length of floral patterned wallpaper rolled out along the table, a white bucket of wallpaper paste with a wide pasting brush resting on it, a wallpaper smoothing brush and a pair of long scissors on the table, smooth light grey prepared wall behind, protective paper on the floor, daylight"),
    ("Vägg där tapet med blommönster har satts upp bredvid en ännu otapetserad yta",
     "straight frontal view of an interior wall, the left two thirds of the wall completely covered with blue and white floral patterned wallpaper hung in four vertical strips side by side, thin straight vertical seams faintly visible between the strips, the flower pattern continuous across the seams, the right third of the wall is bare unpainted light grey plaster, an aluminium step ladder stands in front of the bare part, white skirting board, floor covered with protective paper"),
  ],
  "related": [
    ("malare.html", "Målare i Stockholm", "Tak, väggar och snickerier."),
    ("snickare.html", "Snickare i Stockholm", "Lister, foder och dörrar."),
    ("golvslipning.html", "Golvslipning i Stockholm", "Slipa golvet innan tapeten sätts upp."),
    ("villarenovering.html", "Villarenovering", "Ytskikten som del av en större renovering."),
  ],
},

# ================================================================== FÖNSTERRENOVERING
"fonsterrenovering.html": {
  "kind": "hub", "service": "fonsterrenovering", "sort_ort": True, "svc_label": "Fönsterrenovering",
  "crumb": "Fönsterrenovering", "parent": ("Fönsterbyte", "fonsterbyte.html"),
  "title": "Fönsterrenovering Stockholm – renovera träfönster, ROT",
  "description": "Fönsterrenovering i Stockholm: vi skrapar, lagar, kittar och målar träfönster med linoljefärg och tätar innerbågen. Gratis besök, ROT-avdrag på fakturan.",
  "h1": "Fönsterrenovering i Stockholm",
  "lead": "Geal Entreprenad AB renoverar träfönster på villor, radhus och äldre flerbostadshus i hela Stockholm: vi skrapar, lagar rötskadat virke, kittar om, målar med linoljefärg och tätar innerbågen. Du får ett gratis platsbesök och ett skriftligt kostnadsförslag, och ROT-avdraget dras direkt på fakturan. Här ser du vad som ingår, hur arbetet går till, vad priset beror på och när det är bättre att byta fönstren.",
  "card": "Renovera träfönster – kitt, linoljefärg och tätning.",
  "sections": [
    {"id": "ingar", "anchor": "Vad ingår",
     "h2": "Det här ingår i en fönsterrenovering",
     "paras": [
       "En fönsterrenovering börjar med en genomgång fönster för fönster. Vi känner efter röta i bågarnas bottenstycken och i karmens nedre del, tittar på kitt, färg och beslag och delar in fönstren i dem som bara behöver målas om och dem som måste tas isär och lagas. Indelningen står i kostnadsförslaget.",
       "Bågarna lyfts av och fönsterhålen täcks under tiden. Lös färg skrapas bort, sprucket kitt tas ur, trasigt glas byts och rötskadat virke skärs bort och ersätts med nytt, friskt trä. Sedan kittas rutorna om, och bågarna grundas och målas. Karmen, fönsterblecket och fodren på utsidan ses över i samma omgång.",
       "Till sist justeras gångjärn och beslag så att bågen sluter, och innerbågen får en tätningslist. Ett renoverat fönster ska gå lätt att öppna, stänga tätt och ha ett helt färgskikt som håller vattnet borta från träet.",
     ],
     "aside": {"title": "Ingår normalt", "items": [
       "Gratis platsbesök och skriftligt kostnadsförslag", "Genomgång fönster för fönster",
       "Skrapning och lagning av virke", "Omkittning och byte av trasigt glas",
       "Grundning och målning med linoljefärg", "Tätningslist och justering av beslag"]}},
    {"id": "renovera-eller-byta",
     "h2": "Renovera eller byta fönstren?",
     "paras": [
       "Äldre träfönster är ofta gjorda av tätvuxet virke som går att laga gång på gång. Skadorna sitter oftast nedtill, i bågens bottenstycke och i karmens nedre hörn, där vatten blir stående. Är resten av virket friskt lagas den delen, och fönstret behåller sina proportioner, sitt glas och sina beslag.",
       "Ett byte är rimligare när rötan har gått långt upp i både båge och karm, när fönstren redan har bytts mot en enklare konstruktion som inte går att laga eller när du vill ändra fönstrens storlek. Då beskriver vi alternativen under " + _L.format("fonsterbyte.html", "fönsterbyte i Stockholm") + ".",
       "I hus med kulturvärde finns ytterligare ett skäl att renovera: de ursprungliga fönstren är en stor del av husets utseende, och ett byte kan kräva lov. Vi säger vad vi ser vid platsbesöket och rekommenderar inte en renovering av fönster som inte tål den.",
     ],
     "aside": {"title": "Tecken på att renovering räcker", "items": [
       "Röta bara i bottenstycket", "Friskt virke i karmen", "Sprucket kitt och flagnande färg",
       "Bågar som kärvar eller drar"]}},
    {"id": "kitt-farg",
     "h2": "Linoljekitt och linoljefärg",
     "paras": [
       "Riksantikvarieämbetet rekommenderar linoljekitt eller annat kitt på vegetabilisk oljebas till gamla fönster. Kittet är en knådbar massa av linolja och krita som håller väl på en linoljegrundad båge, men som torkar för snabbt och ofta spricker om kittfalsen inte har grundats först. Därför grundar vi falsen innan rutan kittas.",
       "Ett fönster målas normalt med tre strykningar – grundning, mellanstrykning och slutstrykning – och färgen ska inte läggas på för tjockt. Linoljefärg torkar långsamt, så varje lager får sin tid. Sitter det gammal plastfärg på bågarna tas den bort där den har släppt eller stängt in fukt.",
       "Målningen görs på plats när vädret tillåter. Bågarna kan också tas ned och målas på verkstad, vilket gör det möjligt att arbeta även vintertid och ger ett jämnare resultat.",
     ],
     "aside": {"title": "Tre strykningar", "items": [
       "Grundning", "Mellanstrykning", "Slutstrykning"]}},
    {"id": "tatning-energi",
     "h2": "Tätning, energiglas och gammalt kitt",
     "paras": [
       "Drag från ett gammalt fönster beror oftare på otäta bågar än på glaset. Det är innerbågen som ska tätas: läcker den varm rumsluft ut mellan bågarna kondenserar fukten på ytterbågens insida, rinner ned och samlas i kittfalsen, och där börjar rötan. En tätningslist på innerbågen och en översyn av drevningen runt karmen gör stor skillnad för komforten.",
       "Boverkets energiguide beskriver flera sätt att förbättra ett befintligt fönster utan att byta det, bland annat att täta det och att byta den inre rutan till energiglas. På kopplade fönster kan glaset i innerbågen bytas medan den gamla rutan sitter kvar ytterst, så att fasadens uttryck inte ändras.",
       "I hus från mitten av 1900-talet kan fönsterkitt och fogmassor innehålla asbest eller PCB. Boverket skriver att provtagning är det enda säkra sättet att veta. Vid misstanke bör kittet därför provtas innan det skrapas.",
     ],
     "aside": None},
    {"id": "fonstertyper",
     "h2": "Fönstertyper vi renoverar",
     "paras": [
       "Äldre svenska träfönster finns i några huvudtyper, och de renoveras på lite olika sätt. De äldsta har en enkel ytterbåge och en lös innerbåge som sätts i till vintern. I många egnahem från 1900-talets första decennier sitter okopplade fönster, där ytter- och innerbågen öppnas var för sig. Senare blev kopplade fönster vanliga: två bågar som sitter ihop och öppnas som en, och som kan delas för putsning och målning.",
       "På alla typerna är det ytterbågen som tar vädret och innerbågen som ska vara tät. Spröjsade bågar har många små rutor och därmed mycket kitt, vilket gör kittningen till en stor del av arbetet. Gamla rutor av munblåst eller valsat glas har en levande yta som nytt glas saknar, och vi är därför rädda om dem när bågarna tas isär. Spricker en ruta ersätter vi den med glas som liknar det gamla om du vill.",
       "Altandörrar och fönsterdörrar i trä renoveras på samma sätt som fönstren, med extra uppmärksamhet på tröskeln och dörrbladets nederkant.",
     ],
     "aside": {"title": "Vanliga typer", "items": [
       "Enkelbåge med lös innerbåge", "Okopplade bågar", "Kopplade bågar", "Spröjsade fönster", "Fönsterdörrar i trä"]}},
    {"id": "underhall",
     "h2": "Underhåll efter renoveringen",
     "paras": [
       "Ett renoverat fönster håller länge om färgskiktet hålls helt. Titta över fönstren en gång om året, särskilt bågarnas bottenstycken och karmens nedre del på husets söder- och västsida. Linoljefärg mattas med tiden, och en mattad yta kan strykas med linolja eller målas om med ett tunt lager innan träet har blivit bart.",
       "Sprickor i kittet lagas när de upptäcks, så att vatten inte tar sig in bakom glaset. Håll dräneringshål och fönsterbleck rena, och låt inte snö eller löv ligga mot bågarna. Tätningslisten på innerbågen byts när den har tappat sin spänst.",
     ],
     "aside": None},
  ],
  "steps_h2": "Så går en fönsterrenovering till – steg för steg",
  "steps": [
    ("Platsbesök", "Vi går igenom varje båge och karm, känner efter röta och tittar på kitt, färg och beslag. Besöket är gratis."),
    ("Skriftligt kostnadsförslag", "Det framgår vilka fönster som målas om och vilka som tas isär, med ROT-avdraget uträknat."),
    ("Bågarna av", "Bågarna lyfts av och fönsterhålen täcks medan arbetet pågår."),
    ("Skrapning och lagning", "Lös färg och sprucket kitt tas bort, rötskadat virke ersätts och trasigt glas byts."),
    ("Kittning och målning", "Rutorna kittas med linoljekitt, och bågarna målas med tre strykningar linoljefärg."),
    ("Tätning och justering", "Innerbågen får tätningslist, gångjärn justeras och vi går igenom fönstren med dig."),
  ],
  "time_h2": "Hur lång tid tar en fönsterrenovering?",
  "time": [
    "Tiden beror på antalet bågar, hur många som måste tas isär och lagas och hur högt fönstren sitter. Det som styr kalendern är färgen: tre strykningar linoljefärg med torktid mellan varje lager gör att en båge är under arbete betydligt längre än den tid vi faktiskt står med penseln.",
    "Utvändigt arbete på plats görs under den varma delen av året och läggs efter väder och väderstreck. På vintern kan bågarna i stället målas på verkstad. Fönsterhålen är täckta medan bågarna är borta, och tidplanen står i kostnadsförslaget.",
  ],
  "rot_h2": "Så fungerar ROT-avdraget vid fönsterrenovering",
  "rot": [
    "På Skatteverkets lista över rotarbeten för småhus finns att reparera eller byta ut fönster, att måla fönster och att reparera fönsterbleck. Snickeriet, kittningen och målningen kan alltså alla ge avdrag. I en bostadsrätt ger bara arbete på fönstrets insida avdrag, till exempel att byta glaset i den inre bågen eller måla insidan.",
    _ROT_SUM + " Material och resor ger inget avdrag, och bara arbetad tid på plats hos dig räknas – det som görs på verkstad redovisar vi för sig på fakturan, utan avdrag. Geal drar avdraget direkt på fakturan och ansöker om utbetalningen hos Skatteverket.",
  ],
  "price_h2": "Vad beror priset på?",
  "price": [
    "Vi publicerar inga prislistor för fönsterrenovering, eftersom två fönster av samma storlek kan vara i helt olika skick. Det som väger tyngst är antalet bågar och hur högt de sitter, hur många som måste tas isär, hur mycket virke som behöver ersättas, om gammal plastfärg ska bort, om bågarna målas på plats eller på verkstad och om innerbågarna ska få energiglas.",
    "Efter platsbesöket får du ett skriftligt kostnadsförslag där arbete och material står var för sig och ROT-avdraget är uträknat. Besöket och kostnadsförslaget är gratis.",
  ],
  "faq": [
    ("Vad kostar fönsterrenovering i Stockholm?",
     "Det beror på antalet bågar, deras skick, hur mycket virke som ska ersättas och om målningen görs på plats eller på verkstad. Vi kommer ut gratis och lämnar ett skriftligt kostnadsförslag med ROT-avdraget uträknat."),
    ("Är det bättre att renovera än att byta fönster?",
     "Om virket är friskt utom i bottenstycket räcker oftast en renovering, och fönstret behåller sitt utseende. Har rötan gått långt i både båge och karm är ett byte rimligare."),
    ("Kan gamla fönster bli energisnålare utan att bytas?",
     "Ja. Boverkets energiguide nämner tätning av fönstret och byte av den inre rutan till energiglas som sätt att förbättra ett befintligt fönster."),
    ("Varför målar ni med linoljefärg?",
     "Linoljefärg tränger in i träet och kan målas om i många lager utan att den gamla färgen måste tas bort. Den torkar långsamt, och därför läggs den i tre tunna strykningar."),
    ("Får jag rotavdrag för fönsterrenovering i Stockholm?",
     "I ett småhus ja – Skatteverket räknar reparation och målning av fönster som rotarbete. I en bostadsrätt ger bara arbete på fönstrets insida avdrag."),
    ("Går det att renovera fönster i Stockholm under vintern?",
     "Bågarna kan tas ned och målas på verkstad under vintern. Arbete som görs på verkstad ger dock inget rotavdrag, eftersom avdraget bara gäller arbetad tid hos dig."),
    ("Kan gamla munblåsta rutor sparas när fönstren renoveras?",
     "Ja. Rutorna tas försiktigt ur när bågen kittas om och sätts tillbaka. Ska innerbågen få energiglas kan den gamla rutan sitta kvar i ytterbågen."),
  ],
  "sources": [_RAA_F, _LST_F, _BV_F, _BV_ASB, _SKV, _SKV2],
  "cta": ("Dags att renovera fönstren?", "Boka ett gratis platsbesök, så går vi igenom fönstren ett för ett och lämnar ett skriftligt kostnadsförslag med ROT-avdraget uträknat."),
  "img": [
    ("Nyrenoverade vitmålade spröjsade träfönster på en äldre villa i Stockholm",
     "close view of freshly renovated white painted wooden multi-pane casement windows with glossy linseed oil paint and neat putty lines on an early 1900s Swedish villa with a pale plastered facade, old slightly wavy glass reflecting trees, summer daylight"),
    ("Gammal fönsterbåge med skrapad färg på arbetsbockar, med kittkniv och en burk kitt",
     "an old wooden window sash lying flat on two trestles in a workshop, old paint scraped to bare wood on one half, fresh linseed putty neatly applied around one glass pane, a putty knife and a tin of putty beside it, daylight from a workshop window"),
    ("Flagnad färg och bart trä nedtill på ett gammalt träfönster, med stämjärn och slipkloss",
     "close-up of the lower corner of an old wooden window sash where a rotten piece has been cut out and replaced with a precisely fitted piece of new pale pine, primed grey around the joint, a chisel and sandpaper on the workbench"),
  ],
  "related": [
    ("fonsterbyte.html", "Fönsterbyte i Stockholm", "När fönstren behöver bytas."),
    ("fasadmalning.html", "Fasadmålning i Stockholm", "Måla fasaden i samma omgång."),
    ("snickare.html", "Snickare i Stockholm", "Foder, lister och fönsterbänkar."),
    ("platslagare.html", "Plåtslagare i Stockholm", "Nya fönsterbleck."),
  ],
},
}


# Länk i texten från huvudtjänstens hubb till den nya hubben (anropas från tjanster_v1.py).
_PARENT_LINKS = [
    ("golvlaggning.html", "slipning", " Hela arbetsgången, ytbehandlingarna och torktiderna beskriver vi på sidan om "
     + _L.format("golvslipning.html", "golvslipning i Stockholm") + "."),
    ("malare.html", "fasad", " Arbetsgången från tvätt till sista strykningen beskriver vi på sidan om "
     + _L.format("fasadmalning.html", "fasadmålning i Stockholm") + "."),
    ("malare.html", "h2:Invändig målning och tapetsering", " Mer om tapettyper och underarbete finns under "
     + _L.format("tapetsering.html", "tapetsering i Stockholm") + "."),
    ("fonsterbyte.html", "byta-eller-renovera", " Hur en renovering går till steg för steg beskriver vi under "
     + _L.format("fonsterrenovering.html", "fönsterrenovering i Stockholm") + "."),
]


def link_parents(TJ):
    for f, sid, text in _PARENT_LINKS:
        sec = next(x for x in TJ[f]["sections"] if x["id"] == sid or "h2:" + x["h2"] == sid)
        if text not in sec["paras"][-1]:
            sec["paras"] = sec["paras"][:-1] + [sec["paras"][-1] + text]
