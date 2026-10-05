import json, urllib.error, os, sys, time, urllib.request, concurrent.futures as cf
TOK=os.environ["REPLICATE_API_TOKEN"]; OUT=os.environ.get("IMG_OUT","/tmp/vts-img"); os.makedirs(OUT,exist_ok=True)
TAIL=", clean editorial illustration, Scandinavian suburban villa context, soft overcast Nordic daylight, muted palette with deep navy #1f2f46 accents, light gray and white, high detail, no text, no letters, no logos, no watermark, no people"
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
]
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
