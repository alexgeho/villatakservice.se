# -*- coding: utf-8 -*-
"""
Ortsidor för Norrtälje, Södertälje och Sigtuna (2026-10-25; ägaren bekräftar uppdrag där).
Samma mönster som omraden_stockholm.py (LOC/LOC_EXTRA) + egen title/desc (ORT_SEO_X) och
en "Källor"-lista (ORT_SRC_X) med sidor som faktiskt öppnats. Inga priser, inga påhittade siffror,
inget kontor i området (bas = Abrahamsberg, Bromma).
"""

AREAS_X = ["Norrtälje", "Södertälje", "Sigtuna"]
NEIGHBORS_X = {
  "Norrtälje": ["Vallentuna", "Österåker", "Täby"],
  "Södertälje": ["Botkyrka", "Huddinge", "Skärholmen"],
  "Sigtuna": ["Upplands Väsby", "Vallentuna", "Sollentuna", "Järfälla"],
}
# Befintliga orter får länkar till de nya (inlänkar).
NEIGHBORS_ADD_X = {
  "Vallentuna": ["Norrtälje", "Sigtuna"],
  "Österåker": ["Norrtälje"],
  "Botkyrka": ["Södertälje"],
  "Huddinge": ["Södertälje"],
  "Upplands Väsby": ["Sigtuna"],
}

LOC_X = {'Norrtälje': {'intro': 'Norrtälje kommun sträcker sig från Rimbo i väster och Hallstavik i norr till Väddö och '
                        'skärgården mot Ålands hav. Vi är takläggare i Norrtälje för villor, fritidshus och '
                        'äldre hus i bland annat Norrtälje stad, Rimbo, Hallstavik och Grisslehamn.',
               'paras': ['Runt Norrtälje stad finns flera områden med villor och radhus. Rimbo och '
                         'Hallstavik växte efter kriget – enligt SCB gick Rimbo från knappt 1 700 invånare '
                         '1960 till omkring 3 400 år 1975, och båda orterna fick många nya villor. Utanför tätorterna finns gårdar, kustbyar och tusentals '
                         'fritidshus, många på tomter där vägen slutar en bit från huset.',
                         'På villorna i tätorterna är pannor av betong eller tegel det vanliga, medan '
                         'fritidshusen oftare har papp eller plåt. Skadorna sitter för det mesta i '
                         'underlaget, inte i själva täckningen. På ett sommarhus är det vanligt att '
                         'råsponten är tunn och att takfoten saknar ordentlig luftspalt. Det märks först när '
                         'huset börjar användas på vintern.',
                         'Mot Ålands hav och i ytterskärgården sliter vinden på nockar, gavlar och '
                         'plåtdetaljer. Inåt land, i skogsbygden, är det snarare skugga och barr som gör att '
                         'taket håller fukt. Vi anpassar därför både material och utförande efter var huset '
                         'ligger, inte bara efter hur gammalt det är.'],
               'items': ['Fritidshus som ska bli åretruntbostad',
                         'Efterkrigsvillor i Rimbo och Hallstavik',
                         'Kustnära hus i vind och salt'],
               'why': 'Vi utgår från Bromma och tar uppdrag i hela Norrtälje kommun, från tätorterna till '
                      'skärgården. Längre resor samordnar vi så att besök och arbete samlas i färre turer.',
               'faq': [('Tar ni uppdrag på Väddö och i Grisslehamn?',
                        'Ja, hela Norrtälje kommun ingår, även Väddö och Grisslehamn. Vi samlar besök och '
                        'leveranser så att jobbet kan göras i ett sammanhang. Vi tar också uppdrag i Rimbo, '
                        'Hallstavik och Norrtälje stad.'),
                       ('Vilket tak passar en stuga med låg taklutning?',
                        'Papp eller falsad plåt brukar fungera bäst när lutningen är låg. Vi mäter och '
                        'föreslår material utifrån det. Betongpannor och tegel kräver brantare tak, så de '
                        'passar sällan en låg sommarstuga.')]},
 'Södertälje': {'intro': 'Södertälje kommun rymmer staden vid kanalen, stationsorterna Järna och Hölö och '
                         'landsbygden i Enhörna och på Mörkö. Vi är takläggare i Södertälje för villor, '
                         'radhus och fritidshus i bland annat Pershagen, Västergård, Blombacka, Järna, Hölö '
                         'och Enhörna.',
                'paras': ['De äldsta villakvarteren är egnahemsområden från början av 1900-talet, där staden '
                          'styckade gårdsmark i små tomter. Senare kom villaområdena i Järna och Hölö, där '
                          'Hölö fick nya villakvarter under 1960–80-talen. Under 1960- och 70-talen byggdes '
                          'dessutom stora bostadsområden i stadsdelar som Bårsta, Ronna, Saltskog, Geneta '
                          'och Hovsjö, och i kommunens alla socknar tillkom fritidshusområden under samma '
                          'period.',
                          'Sekelskiftshusen har ofta branta sadeltak och murade tegelskorstenar, medan '
                          'efterkrigsvillorna har flackare tak. I sommarstugeområden som Sandviken i Enhörna '
                          'har 1930-talets fritidshus flacka tak. Det gör att två villor på samma gata kan '
                          'behöva helt olika lösningar. Vi utgår från det enskilda huset.',
                          'Mälaren, Hallsfjärden och Järnafjärden ger blåsiga lägen på många tomter. På '
                          'bergknallar med tall samlas barr och mossa på taken. I Bergvik sluttar tomterna '
                          'kraftigt ner mot Mälarens vatten, och där tar takfoten mer väder än i de inre '
                          'kvarteren.'],
                'items': ['Egnahemsvillor från tidigt 1900-tal',
                          'Villor och radhus i Järna och Hölö',
                          'Fritidshus vid Mälaren'],
                'why': 'Vi utgår från Bromma och tar uppdrag i hela Södertälje kommun, från stadskärnan till '
                       'Hölö och Mörkö. Besök och etablering samordnar vi så att resvägen inte styr arbetet. '
                       'Efter platsbesöket får du en tydlig bedömning och offert.',
                'faq': [('Tar ni uppdrag i Hölö och på Mörkö?',
                         'Ja, hela kommunen ingår. Vi samlar platsbesöket och planerar leveranser i förväg. '
                         'Vi arbetar även i Järna, Enhörna och i stadens villaområden.'),
                        ('Lägger ni om tak på radhus i Södertuna?',
                         'Ja. På radhus planerar vi gärna flera tak i samma etapp om grannarna vill, så att '
                         'anslutningarna mellan husen blir lika. Ett enskilt radhus går också bra; då '
                         'anpassar vi anslutningarna mot grannarnas tak.'),
                        ('Kan ni byta tak på ett 1910-talshus utan att ändra utseendet?',
                         'Ja, vi behåller lutning, taksprång och skorsten och föreslår ett material som '
                         'passar husets tid. Tegelskorstenen ses över samtidigt och kläs så att den '
                         'utkragande formen syns.')]},
 'Sigtuna': {'intro': 'Sigtuna kommun rymmer både en av de första städerna i det dåvarande Sverige och '
                      'Märsta, som växte i takt med Arlanda. Vi är takläggare i Sigtuna för villor och '
                      'radhus i bland annat Märsta, Arenberga, Norrbacka, Steninge, Ekilla, Rosersberg och '
                      'Sigtuna stad.',
             'paras': ['Enligt SCB hade Märsta knappt 2 900 invånare 1960, över 10 000 fem år senare '
                       'och nästan 17 000 år 1970. Under de åren växte nya områden med kedjehus, radhus '
                       'och villor fram runt stationsorten.',
                       'Husen från de åren har ofta pannor på sitt ursprungliga underlag, och i '
                       'radhuslängorna är taken som regel lika gamla. Det betyder '
                       'att en hel länga ofta når slutet av takets livslängd samtidigt, och att det kan vara '
                       'klokt att planera tillsammans med grannarna.',
                       'Rosersberg ligger mellan Märsta och Upplands Väsby, nära Mälaren och Fysingen. I Sigtuna stad ligger husen i sluttningen ner mot Mälaren, och taklandskapet domineras enligt kommunens bevarandeplan av rött lertegel med inslag av plåttak. Hus nära vattnet och på höjderna får mer vind än de som ligger skyddat i '
                       'kvarteren.'],
             'items': ['Radhus och villor från 1960–70-talen i Märsta',
                       'Tegeltak i Sigtuna stads kulturmiljö',
                       'Nyare villor i Rosersberg'],
             'why': 'Vi utgår från Bromma och tar uppdrag i hela Sigtuna kommun, från Märsta och Rosersberg '
                    'till Sigtuna stad. Vi har inget kontor i kommunen men samlar besök så att planeringen '
                    'blir smidig.',
             'faq': [('Tar ni uppdrag i Rosersberg och Steninge?',
                      'Ja, hela Sigtuna kommun ingår. Vi bokar platsbesök och planerar arbetet därifrån. Vi '
                      'arbetar även i Märsta, Ekilla, Norrbacka och Sigtuna stad.'),
                     ('Kan ni lägga om taket på en hel radhuslänga i Arenberga?',
                      'Ja. Vill flera grannar göra samtidigt planerar vi längan som en etapp, så att '
                      'anslutningarna mellan husen blir lika. Ett enskilt radhus går också bra, men då '
                      'behöver anslutningarna mot grannhusen göras extra noga.'),
]}}

LOC_EXTRA_X = {'Norrtälje': {'secs': [('Vanliga tak och problem i Norrtälje',
                         ['På fritidshus från mitten av 1900-talet ser vi ofta tunt underlag, papp som '
                          'spruckit i skarvarna och takfötter där vatten trängt in. Har stugan byggts till i '
                          'flera omgångar finns dessutom skarvar mellan takfall som är svåra att hålla täta.',
                          'I Rimbo och Hallstavik är det typiska fallet ett pannbelagt villatak där '
                          'underlagspapp och läkt har tjänat ut. Då håller en hel omläggning oftast längre '
                          'än att laga punktvis.',
                          'Gamla plåttak på uthus och gäststugor har ofta tappat färgen och börjat rosta i '
                          'falsarna. Ibland räcker en ommålning, men när plåten är genomrostad är nytt tak '
                          'enda hållbara vägen. Vi säger vad vi ser och föreslår den åtgärd som passar '
                          'husets skick.']),
                        ('Planera takprojektet i Norrtälje',
                         ['Bygglov hanteras av Norrtälje kommun. Nytt takmaterial på ett en- eller '
                          'tvåbostadshus kräver i regel inget lov sedan december 2025, men på kommunens sida '
                          'om <a class="text-link" '
                          'href="https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/lovbefriade-atgarder/" '
                          'rel="noopener">lovbefriade åtgärder</a> ser du hur du kontrollerar om fastigheten '
                          'ligger i ett särskilt värdefullt område, där lov kan krävas.',
                          'Kommunen ger inga bindande besked per telefon eller e-post – för det söker du '
                          'frivilligt bygglov. Höjs taket kan det räknas som tillbyggnad, så stäm av med kommunen innan takets form eller höjd ändras.',
                          'Tänk också på årstiden. Ett tak på en ö eller långt ut på Väddö läggs helst under '
                          'en period med stabilt väder, och leveranser kan behöva bokas i god tid. Vi går '
                          'igenom tidplanen redan vid besöket, så att ni vet när huset kan stå med öppet '
                          'tak.']),
                        ('Fritidshusen och skärgården',
                         ['Med 27 352 fritidshus enligt SCB har Norrtälje fler fritidshus än någon annan '
                          'svensk kommun. Kommunen uppger att ungefär en fjärdedel av brukarna vistas här '
                          'större delen av året, och många hus har gått från sommarbruk till åretruntboende.',
                          'För oss betyder det att ett takjobb ofta också blir ett vindsjobb. När huset '
                          'värms upp på vintern måste taket ventileras så att fukt inte fastnar under '
                          'råsponten – läs hur vi lägger upp en <a class="text-link" '
                          'href="takrenovering-norrtalje.html">takrenovering i Norrtälje</a>.',
                          'Vanliga åtgärder i samband med permanentning är ny råspont där den gamla inte '
                          'bär, ventilerade takfötter och nya genomföringar för ventilation och skorsten. '
                          'Det är arbeten som blir enklare och billigare att göra när taket ändå är öppet.']),
                        ('Hallstavik och kusten vid Grisslehamn',
                         ['Hallstavik har vuxit fram som brukssamhälle kring pappersbruket, och Visit Roslagen beskriver det gamla brukssamhället som kulturskyddat. Där bör material och utseende '
                          'stämmas av med kommunen innan takarbetet planeras.',
                          'Grisslehamn på Väddö ligger längst ut mot Ålands hav. Längs kusten väljer vi plåt och infästningar med '
                          'tanke på vind och salt, och vid ett <a class="text-link" '
                          'href="takbyte.html">takbyte</a> ingår vindskivor och nockar i bedömningen.',
                          'Enligt SCB hade Hallstavik omkring 3 800 invånare 1960 och drygt 5 100 år 1975, och '
                          'villorna från tillväxtåren har nu tak som ofta behöver ses över. Där är en '
                          'omläggning med nytt underlag det vanligaste uppdraget.'])],
               'faq': [('Tar ni hand om rivningen av ett gammalt papptak?',
                        'Ja. Rivningsmassorna planeras in från början. Gammal papp sorteras som byggavfall och lämnas på '
                        'godkänd mottagning.'),
                       ('Kan ni kolla kommunkartan åt oss innan takbytet?',
                        'Ja, vi tittar efter särskilt värdefulla områden och skyddsbestämmelser och säger '
                        'till om ni bör kontakta kommunen. Det är ni som fastighetsägare som ansvarar för '
                        'lovfrågan, men vi hjälper gärna till med underlaget.'),
                       ('Gör ni tak på gäststugor och uthus också?',
                        'Ja, ofta i samma etapp som huvudbyggnaden, så att transporter och ställning kan '
                        'samordnas. Ett mindre tak kan vara bra att börja med om ni vill se hur vi '
                        'arbetar.')]},
 'Södertälje': {'secs': [('Vanliga tak och problem i Södertälje',
                          ['På egnahemsvillorna är råsponten ofta original och har på sina ställen tagit '
                           'fukt, särskilt kring skorstenen och vid takfoten. Gamla plåtbeslag runt '
                           'tegelskorstenar är en vanlig läckkälla. Vid besiktningen lyfter vi därför på '
                           'några pannor eller tittar in från vinden, eftersom underlaget sällan syns från '
                           'marken.',
                           'På husen från 1950–70-talen är det oftare underlagspapp, läkt och fotplåt som '
                           'tjänat ut. På flacka tak och pulpettak syns problemen först vid anslutningar mot '
                           'vägg.',
                           'I sommarstugeområdena har många hus byggts till i etapper. Då möts olika takfall '
                           'i vinklar som vatten gärna hittar in i, och vid ett takarbete gör vi om de '
                           'anslutningarna så att hela taket fungerar som en enhet.']),
                         ('Planera takprojektet i Södertälje',
                          ['Bygglov hanteras av Södertälje kommun. Enligt kommunens sida om <a '
                           'class="text-link" '
                           'href="https://www.sodertalje.se/bo-och-bygga/bygga-nytt-och-riva/fasad-tak-fonster-och-dorrar/" '
                           'rel="noopener">fasad- och takändringar</a> krävs lov om huset ligger i ett '
                           'kulturmiljöområde med utökad lovplikt; för vanliga en- och tvåbostadshus i '
                           'övrigt är byte av takmaterial normalt lovfritt.',
                           'Är du osäker kan du ringa kommunens kontaktcenter på 08-523 010 00 innan du '
                           'bestämmer material. Hur vi lägger upp en renovering beskriver vi under <a '
                           'class="text-link" href="takrenovering-sodertalje.html">takrenovering i '
                           'Södertälje</a>.',
                           'Kommunens kulturmiljöinventering finns som delrapporter för Mörkö, Hölö, Järna, '
                           'Enhörna, Vårdinge, Södertälje med omgivande land och stadskärnan. Där beskrivs '
                           'bland annat Blombacka egnahemsområde, och den som äger ett hus i ett av de '
                           'utpekade områdena bör kontrollera vad som gäller innan materialet byts.']),
                         ('Järna och Hölö – orterna söder om staden',
                          ['Hölö växte fram som stationssamhälle kring järnvägen som öppnade 1913 och har i '
                           'dag omkring 1 000 invånare. Enligt kommunens kulturmiljöinventering finns här '
                           'villakvarter från 1900-talets andra hälft. Kring stationen byggdes på 1930-talet '
                           'flerfamiljshus och små enskilda villor.',
                           'I Järna finns radhus i Södertuna från 1980–90-talen och nya områden med '
                           'typhusvillor norr om tätorten. När ett radhustak från den perioden behöver ett '
                           '<a class="text-link" href="takbyte.html">takbyte</a> är det ofta flera hus i '
                           'raden som är i samma skick.',
                           'Äldre delar av Järna har egnahem från 1930–40-talen med flacka sadeltak och '
                           'villor från 1960-talet med pulpettak väster om Åsgatan. De låga taken kräver '
                           'täckning som klarar liten lutning, och anslutningar mot vägg och skorsten '
                           'behöver göras med omsorg.']),
                         ('Enhörna och Mälarstränderna',
                          ['I Enhörna finns villabebyggelse främst vid Ekeby, och sommarstugeområden som '
                           'Sandviken och Vattubrinken har delvis blivit permanentbostäder. Många av husen '
                           'ligger i sluttningar ner mot Mälaren. Enligt kommunens kulturmiljöinventering '
                           'har trycket på boende på landsbygden varit stort sedan slutet av 1900-talet, och '
                           'vid Ekeby pågår en ständig utbyggnad.',
                           'När en sommarstuga blir åretruntbostad behöver taket ofta mer än ny täckning. Vi '
                           'ser över vind och ventilation samtidigt, så att fukt från det uppvärmda huset '
                           'inte samlas under yttertaket.',
                           'I Sandvikens södra del står fritidshus från 1960-talet på bergknallar i '
                           'tallskog. Barren samlas i rännor och ränndalar, så efter ett takarbete '
                           'rekommenderar vi regelbunden rensning och tillsyn av mossa.'])],
                'faq': [('Arbetar ni i Blombacka och Pershagen med de gamla villorna?',
                         'Ja. Där tar vi extra hänsyn till skorstenar, taksprång och takfallens lutning, som '
                         'är en del av husens karaktär. Vi kontrollerar också om huset ingår i kommunens '
                         'kulturmiljöinventering.'),
                        ('Hur gör ni på en brant tomt ner mot Mälaren?',
                         'Vi planerar ställning och materialhantering efter terrängen och bestämmer var '
                         'container kan stå innan arbetet börjar. Ibland behöver material bäras eller lyftas '
                         'sista biten, och det tar vi med i offerten.'),
                        ('Kan ni lägga plåt på ett pulpettak från 1960-talet?',
                         'Ja, falsad plåt passar ofta låga lutningar. Vi kontrollerar först underlaget och '
                         'anslutningen mot fasaden. Är råsponten skadad byts den innan plåten läggs.')]},
 'Sigtuna': {'secs': [('Vanliga tak och problem i Sigtuna',
                       ['På 1960–70-talens radhus och villor i Märsta är det oftast underlagspapp, läkt och '
                        'plåtdetaljer som nått slutet av sin livslängd, även när pannorna fortfarande ser '
                        'hela ut. Läckor börjar gärna vid skorstenar, ränndalar och mellan grannhusens tak.',
                        'I Sigtuna stad är det andra frågor: gamla lertegelpannor som behöver kompletteras, '
                        'murade skorstenar och plåtdetaljer som ska utformas som förr.',
                        'I Rosersberg och andra delar med nyare villor är det sällan underlaget som är '
                        'problemet. Där handlar uppdragen oftare om plåtdetaljer, avvattning, takfönster och '
                        'anslutningar vid tillbyggnader.']),
                      ('Planera takprojektet i Sigtuna',
                       ['Bygglov hanteras av Sigtuna kommun. På kommunens sida om <a class="text-link" '
                        'href="https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/andra-befintlig-byggnad/tak.html" '
                        'rel="noopener">tak</a> står att bygglov krävs för nytt takmaterial eller ny kulör '
                        'om byggnaden är särskilt kulturhistoriskt värdefull eller om detaljplan eller '
                        'områdesbestämmelser har skyddsbestämmelser. För vissa skyddade byggnader kan det '
                        'behövas en anmälan redan för en omläggning, även utan byte av material eller färg.',
                        'Vill du vara säker kan du söka frivilligt bygglov via kommunens e-tjänst. Ansökan '
                        'ska innehålla situationsplan, förslag till kontrollplan och ritningar.',
                        'Kommunen påpekar att även byggnader som inte är utpekade i något program kan vara '
                        'så värdefulla att särskild hänsyn behövs. Är du osäker om ditt hus kan du skicka in '
                        'bilder till kommunen och få en bedömning innan du väljer material.']),
                      ('Sigtuna stad – tegeltaken i riksintresset',
                       ['Sigtuna grundlades under vikingatiden och kallas i kommunens bevarandeplan Sveriges äldsta stad. Staden är riksintresse för kulturmiljövården. '
                        'Kommunens bevarande- och förnyelseplan från 2019 anger att tegeltak i regel ska '
                        'ersättas med likadana pannor, att ett enkupigt lertegel inte ska bytas mot '
                        'tvåkupigt och att gamla pannor är en tillgång som i första hand ska kompletteras.',
                        'Planen säger också att plåtklädda vindskivor är en modern företeelse och att murade '
                        'eller putsade skorstenar är att föredra framför plåtklädda. Läs mer om kulturmiljön '
                        'på kommunens sida om att <a class="text-link" '
                        'href="https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html" '
                        'rel="noopener">bygga i kulturmiljö</a>, och om hur vi arbetar med <a '
                        'class="text-link" href="takrenovering.html">takrenovering</a> av äldre tak.',
                        'Enligt bevarandeplanen är solceller bygglovspliktiga inom riksintresset, och i centrala staden och på '
                        'Malmen ska panelerna stämma med takets färg. Längs en del av Stora gatan får det '
                        'inte finnas synliga solceller på takfall mot gatan, så det är bra att ta med i '
                        'planeringen om taket ska bytas.']),
                      ('Arlanda och flygbullret',
                       ['Arlanda ligger i kommunen och är riksintresse enligt miljöbalken. Enligt kommunens '
                        'sida om <a class="text-link" '
                        'href="https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/flygbuller.html" '
                        'rel="noopener">flygbuller</a> begär kommunen ett yttrande från Swedavia när någon '
                        'vill bygga nytt eller bygga till inom influensområdet.',
                        'Kommunens sida nämner nybyggnad och tillbyggnad, inte takbyte. Planerar du samtidigt en tillbyggnad är det bra att räkna med Swedavias yttrande i tidplanen.',
                        'Kommunen skriver att byggnation inom bullerstört område i vissa fall kan accepteras '
                        'om huset får bullerbegränsande åtgärder, till exempel avskärmning eller isolering.'])],
             'faq': [('Får jag byta lertegel mot betongpannor i Sigtuna stad?',
                      'Inom bevarandeplanens område ska tegeltak i regel ersättas med likadana pannor. '
                      'Kontakta kommunen innan du väljer annat material.'),
                     ('Kan ni spara de gamla pannorna vid omläggning?',
                      'Ja. Hela pannor tas ner, sorteras och läggs tillbaka, och saknade pannor kompletteras '
                      'med likadana. Pannor som inte behövs på huvudbyggnaden kan sparas, till exempel i ett '
                      'uthus, som reserv.'),
                     ('Hur vet jag om mitt hus i Sigtuna är kulturhistoriskt värdefullt?',
                      'Kommunen kan göra en bedömning om du skickar in bilder på huset via deras webbplats. '
                      'Vi hjälper gärna till med bilder och beskrivning av taket.')]}}

ORT_SEO_X = {'Norrtälje': {'title': 'Takläggare i Norrtälje – villa, skärgård och fritidshus',
               'desc': 'Takläggare i Norrtälje för villor i Rimbo och Hallstavik, hus i Norrtälje stad och '
                       'fritidshus på Väddö och i skärgården. Omläggning, plåt och takbyte.'},
 'Södertälje': {'title': 'Takläggare i Södertälje – villor från Hölö till Enhörna',
                'desc': 'Takläggare i Södertälje för sekelskiftsvillor, efterkrigshus och fritidshus i '
                        'Pershagen, Västergård, Järna, Hölö och Enhörna. Plåt, tegel och omläggning.'},
 'Sigtuna': {'title': 'Takläggare i Sigtuna – Märsta, Sigtuna stad och Rosersberg',
             'desc': 'Takläggare i Sigtuna kommun för radhus och villor i Märsta, Steninge och Rosersberg '
                     'och för tegeltak i Sigtuna stads kulturmiljö. Omläggning och takbyte.'}}

ORT_SRC_X = {'Norrtälje': [('Norrtälje kommun – Lovbefriade åtgärder',
                'https://www.norrtalje.se/info/bygga-bo-miljo/bygga-andra-riva/lovbefriade-atgarder/'),
               ('SCB – Fritidshus, var finns de?',
                'https://www.scb.se/hitta-statistik/artiklar/2026/fritidshus-vart-finns-de/'),
               ('Norrtälje kommun – Fakta och statistik om landsbygden',
                'https://www.norrtalje.se/info/bygga-bo-miljo/norrtalje-vaxer/landsbygd-skargard/fakta-och-statistik/'),
               ('SCB – Folkmängd och landareal i tätorter, per tätort', 'https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__MI__MI0810__MI0810A/LandarealTatortN/'),
               ('Visit Roslagen – Kulturföreningen Rödvillan, Hallstavik',
                'https://roslagen.se/en/culture-and-history/museum/cultural-association-rodvillan-2/')],
 'Södertälje': [('Södertälje kommun – Fasad, tak, fönster och dörrar',
                 'https://www.sodertalje.se/bo-och-bygga/bygga-nytt-och-riva/fasad-tak-fonster-och-dorrar/'),
                ('Södertälje kommun – Kulturmiljöer',
                 'https://www.sodertalje.se/kultur-och-fritid/kulturmiljoer/'),
                ('Södertälje kommun – Inventering av kulturmiljöer: Järna',
                 'https://www.sodertalje.se/contentassets/801b52a57aed44f592a5d6bf3ff8bb96/3-jarna.pdf'),
                ('Södertälje kommun – Inventering av kulturmiljöer: Hölö',
                 'https://www.sodertalje.se/contentassets/801b52a57aed44f592a5d6bf3ff8bb96/2-holo.pdf'),
                ('Södertälje kommun – Inventering av kulturmiljöer: Enhörna',
                 'https://www.sodertalje.se/contentassets/801b52a57aed44f592a5d6bf3ff8bb96/4-enhorna.pdf'),
                ('Södertälje kommun – Inventering av kulturmiljöer: Södertälje med omgivande land',
                 'https://www.sodertalje.se/contentassets/801b52a57aed44f592a5d6bf3ff8bb96/6-sodertalje-med-omgivande-land.pdf')],
 'Sigtuna': [('Sigtuna kommun – Tak (bygglov)',
              'https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/vad-ska-du-bygga/andra-befintlig-byggnad/tak.html'),
             ('Sigtuna kommun – Bygga i kulturmiljö',
              'https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/bygga-i-kulturmiljo.html'),
             ('Sigtuna kommun – Flygbuller',
              'https://www.sigtuna.se/bygga-bo-och-miljo/bygglov/var-far-du-bygga/flygbuller.html'),
             ('Sigtuna kommun – Bevarande- och förnyelseplan för Sigtuna stad (2019)',
              'https://www.sigtuna.se/download/18.6ed4dd301706254f993282/1582201854957/Bevarande-%20och%20f%C3%B6rnyelseplan%20f%C3%B6r%20Sigtuna%20stad,%20antagen%202019.pdf'),
             ('SCB – Folkmängd och landareal i tätorter, per tätort', 'https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__MI__MI0810__MI0810A/LandarealTatortN/'),
             ('Boverket – Fasadändring, anmälningsplikt och lov',
              'https://www.boverket.se/sv/PBL-kunskapsbanken/lov--byggande/anmalningsplikt/byggnader/fasadandring/')]}
