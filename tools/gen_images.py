import json, urllib.error, os, sys, time, urllib.request, concurrent.futures as cf
TOK=os.environ["REPLICATE_API_TOKEN"]; OUT=os.environ.get("IMG_OUT","/tmp/vts-img"); os.makedirs(OUT,exist_ok=True)
TAIL=", photorealistic photograph, natural colors, Scandinavian suburban villa context, soft overcast Nordic daylight, muted palette with deep navy #1f2f46 accents, light gray and white, high detail, no text, no letters, no logos, no watermark, no people"
JOBS=[
("takmalning-plattak-process","realistic_image","standing-seam metal roof on a Swedish 1960s villa being repainted: left half old faded chalky gray sheet with rust spots, right half freshly painted dark graphite, paint roller and bucket resting on roof safety rail"),
("takmalning-betongpannor","realistic_image","close-up of concrete roof tiles, half cleaned and half freshly coated in black roof paint, moss removed, gentle slope"),
("takbesiktning-checklista","digital_illustration","isometric diagram of a gabled villa roof with highlighted inspection points: ridge, chimney flashing, valley, gutters, roof window, underlayment at eaves, small numbered circular markers without text"),
("takbyte-lager","realistic_image","new roof being laid on a Swedish 1960s villa: lower part already covered with new dark gray concrete tiles, upper part showing fresh black underlayment membrane and new wooden battens, stack of tiles on roof, scaffolding with guard rail, overcast day"),
("takrenovering-omlaggning","realistic_image","roof relaying in progress on a Swedish 1970s villa: half the roof with tiles removed showing new black underlayment and fresh wooden battens, removed concrete tiles stacked neatly on the roof, scaffolding with guard rail"),
("taktvatt-mossa","realistic_image","low-pressure roof washing of moss-covered gray concrete tiles, gentle water spray, clean stripe visible next to mossy area, gutter, pine trees, overcast day"),
("takmaterial-jamforelse","realistic_image","studio product photo of four roof material samples lying side by side on a plain light gray surface, top view: black standing-seam steel sheet piece, gray concrete roof tile, red clay roof tile, black bitumen roofing felt roll, nothing else in frame, no signs, no labels"),
("plattak-falsat","realistic_image","black standing-seam metal roof on a 1930s Swedish functionalist white villa, low pitch, crisp seams, birch trees"),
("ort-bromma-villa","realistic_image","1930s Swedish functionalist white villa with low pitched red clay tile roof in a leafy garden suburb of Bromma Stockholm, autumn"),
("ort-sundbyberg-villa","realistic_image","1920s wooden villa with steep red clay tile roof and dormer in a garden suburb near Stockholm, Duvbo style, autumn"),
("ort-danderyd-villa","realistic_image","large 1910s stone villa with complex roof of black standing-seam steel, dormers and a small tower, big oaks, Djursholm style, autumn"),
("ort-sollentuna-villa","realistic_image","1970s Swedish split-level villa with gray concrete tile roof among pine trees, moss on north side of roof"),
("ort-solna-villa","realistic_image","1940s small Swedish villa with red clay tile roof, plastered facade, Råsunda style garden suburb"),
("ort-taby-radhus","realistic_image","row of 1970s Swedish terraced houses with low-pitched black roofs and wooden facades, Täby style"),
("ort-spanga-villa","realistic_image","1960s Swedish brick villa with brown concrete tile roof, large garden, birch trees"),
("ort-nacka-villa","realistic_image","seaside Swedish villa on a granite rock with standing-seam steel roof, Baltic sea inlet and pines in background, Saltsjöbaden style"),
("ort-hasselby-villa","realistic_image","small 1930s Swedish egnahem wooden villa with steep red clay tile gable roof and chimney, picket fence, apple trees, Hässelby villastad garden suburb, early autumn"),
("ort-vallingby-radhus","realistic_image","row of 1950s Swedish terraced houses in yellow brick with low-pitched dark concrete tile roofs, small front gardens, pine trees, Vällingby ABC suburb style"),
("ort-kista-radhus","realistic_image","1970s Swedish terraced houses with flat bitumen roofs and metal flashings, wooden facades in muted colors, open meadow landscape behind, Järvafältet style"),
("ort-ekero-villa","realistic_image","red Swedish wooden house with white trim and black standing-seam metal roof on a lake shore, lake Mälaren and reeds in background, birch trees, Ekerö countryside"),
("ort-hagersten-villa","realistic_image","1920s Swedish plastered villa with steep red clay tile hipped roof and dormer on a wooded hill above a lake, Mälarhöjden style, oaks"),
("ort-alvsjo-villa","realistic_image","1920s small Swedish wooden egnahem villa with brown-red clay tile roof, glazed veranda, large garden with lilacs, Långbro Herrängen style suburb"),
("ort-enskede-villa","realistic_image","Swedish 1910s garden city semi-detached wooden houses with steep red clay tile mansard roofs, picket fences and fruit trees along a quiet street, Gamla Enskede style"),
("ort-farsta-villa","realistic_image","1960s Swedish single-storey villa in light brick with low-pitched gray concrete tile roof, carport, pine forest edge, Farsta Sköndal style suburb"),
("ort-skarholmen-radhus","realistic_image","view of the roofs from a slightly elevated angle at dawn: 1960s Swedish two-storey terraced houses with dark low-pitched roofs and wooden balconies, hilly terrain with granite rock and pines, Sätra style"),
("ort-huddinge-villa","realistic_image","1910s Swedish wooden villa with steep black standing-seam metal roof and decorative gable, mature garden, Stuvsta villastad style"),
("ort-tyreso-villa","realistic_image","former Swedish summer cottage converted to year-round home, red painted wood with gray concrete tile roof, on a rocky pine slope near a Baltic bay, Tyresö style"),
("ort-haninge-villa","realistic_image","1970s Swedish villa with dark brown concrete tile roof and wooden facade in a suburb, birch trees, Vendelsö style"),
("ort-varmdo-villa","realistic_image","Swedish archipelago house on granite rocks by the sea, white painted wood with black standing-seam metal roof, windswept pines, Värmdö archipelago"),
("ort-upplands-vasby-villa","realistic_image","close-up view of the roof and upper facade at dawn, private garden: 1970s Swedish split-level villa with gray concrete tile roof and brown wooden facade, lawn and birch trees, Upplands Väsby suburb"),
("ort-vallentuna-villa","realistic_image","Swedish farmhouse villa in Roslagen countryside, falu red wood with white corners and red clay tile roof, open fields behind, Vallentuna"),
("ort-osteraker-villa","realistic_image","close-up view of the roof and upper facade at dawn, private garden: Swedish early 1900s seaside summer villa turned year-round home with ornate wooden veranda and red sheet metal roof, Baltic inlet and pines, Österskär style"),
("ort-botkyrka-villa","realistic_image","1960s Swedish villa with dark concrete tile roof on a slope above a lake, pine trees, Tullinge style suburb"),
("ort-jarfalla-radhus","realistic_image","row of 1970s Swedish terraced houses with dark brown concrete tile roofs and wooden facades, forest behind, Viksjö Järfälla style"),
("ort-lidingo-villa","realistic_image","close-up view of the roof and upper facade at dawn, private garden: Swedish early 1900s villa by the sea with weathered green-gray standing-seam metal roof and wooden details, rocky shore, Lidingö style"),
]
JOBS=[j for j in JOBS if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","assets","images",j[0]+".webp"))]
def run(j):
    name,style,prompt=j
    dst=f"{OUT}/{name}.png"
    if os.path.exists(dst): return name+" skip"
    body=json.dumps({"input":{"prompt":prompt+TAIL,"size":"1536x1024","style":style}}).encode()
    r=urllib.request.Request("https://api.replicate.com/v1/models/recraft-ai/recraft-v3/predictions",body,{"Authorization":f"Bearer {TOK}","Content-Type":"application/json","Prefer":"wait"})
    for k in range(8):
        try: d=json.load(urllib.request.urlopen(r,timeout=120)); break
        except urllib.error.HTTPError as e:
            if e.code!=429: return name+" HTTP "+str(e.code)+" "+e.read().decode()[:200]
            time.sleep(12)
    else: return name+" 429 give up"
    while d["status"] not in ("succeeded","failed","canceled"):
        time.sleep(2); d=json.load(urllib.request.urlopen(urllib.request.Request(d["urls"]["get"],headers={"Authorization":f"Bearer {TOK}"})))
    if d["status"]!="succeeded": return name+" FAIL "+str(d.get("error"))
    url=d["output"] if isinstance(d["output"],str) else d["output"][0]
    urllib.request.urlretrieve(url,dst); return name+" ok"
with cf.ThreadPoolExecutor(1) as ex:
    for r in ex.map(run,JOBS): print(r,flush=True)
