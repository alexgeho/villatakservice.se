#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fotorealistiska illustrationer via Replicate (flux-1.1-pro) för ortsidorna
takrenovering-<ort>.html och nya taklaggare-<ort>.html (2026-10-25).
Kor:  python3 tools/gen_images_flux.py [namn ...]
Token: REPLICATE_API_TOKEN i env (skrivs aldrig ut). Ett anrop i taget (429).
Skriver assets/images/<namn>.webp (1200 bred) + <namn>-640.webp. Befintliga hoppas över.
-1 = hero (4:3), -2 = bild i innehållet (3:2). Inga personer, ingen text, inga logotyper.
"""
import io, json, os, sys, time, urllib.error, urllib.request
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "images")
STYLE = (", photorealistic photograph, natural Nordic daylight, realistic proportions, high detail, "
         "Swedish residential architecture, no people, no text, no letters, no signs, no logos, no watermark")

JOBS = {
 "takrenovering-bromma-1": ("4:3", "1920s plastered Swedish garden-city villa with steep red clay tile roof and a central brick chimney, lush garden with apple trees, quiet street in Äppelviken Bromma Stockholm, early autumn"),
 "takrenovering-bromma-2": ("3:2", "close-up of an old red clay tile roof ridge and brick chimney with dark metal flashing on a 1920s Swedish villa, a few autumn leaves in the gutter"),
 "takrenovering-solna-1": ("4:3", "small 1930s Swedish plastered villa with red clay tile hipped roof on a hilly street in Råsunda Solna, birch trees"),
 "takrenovering-solna-2": ("3:2", "slightly elevated view of low-pitched roofs on 1960s Swedish terraced houses with metal flashings, vent pipes and roof penetrations, Bergshamra"),
 "takrenovering-nacka-1": ("4:3", "large early 1900s Swedish wooden seaside villa with ornate gables and a red standing-seam metal roof on a granite slope by a Baltic inlet, Saltsjöbaden, pines"),
 "takrenovering-nacka-2": ("3:2", "1970s Swedish single-storey villa with gray concrete tile roof partly covered with green moss, surrounded by tall pine forest, Boo Nacka"),
 "takrenovering-taby-1": ("4:3", "1970s Swedish villa with brown concrete tile gable roof and wooden facade, lawn and birches, suburb near a sea bay, Näsby Park Täby"),
 "takrenovering-taby-2": ("3:2", "slightly elevated view along a row of 1970s Swedish terraced houses with identical dark concrete tile roofs and connecting metal flashings"),
 "takrenovering-danderyd-1": ("4:3", "large 1910s Swedish national romantic villa with steep red clay tile roof, several dormers and a tall chimney, big oak trees, Djursholm"),
 "takrenovering-danderyd-2": ("3:2", "detail of a roof valley and a dormer on a black standing-seam metal roof of an early 1900s Swedish villa, clean metal valley flashing"),
 "takrenovering-lidingo-1": ("4:3", "early 1900s Swedish wooden villa with glazed veranda and red clay tile roof on a hill with a glimpse of the sea between pines, Lidingö"),
 "takrenovering-lidingo-2": ("3:2", "1960s Swedish single-storey villa with black concrete tile roof and white brick facade among pines, Brevik Lidingö"),
 "takrenovering-huddinge-1": ("4:3", "yellow 1910s Swedish wooden villa with red clay tile roof and decorative gable, mature garden, Snättringe Huddinge"),
 "takrenovering-huddinge-2": ("3:2", "1970s Swedish two-storey terraced houses with dark concrete tile roofs at the edge of a forest, Skogås"),
 "takrenovering-jarfalla-1": ("4:3", "row of 1970s Swedish terraced houses with brown concrete tile roofs and wooden facades in muted colours, small front gardens, Jakobsberg Järfälla"),
 "takrenovering-jarfalla-2": ("3:2", "close-up of the eaves of a 1970s Swedish house: concrete roof tiles, metal drip edge, painted fascia board, ventilated soffit gap and a half-round gutter"),
 "takrenovering-sollentuna-1": ("4:3", "1960s Swedish brick villa with gray concrete tile roof among tall pine trees, Edsberg Sollentuna, overcast autumn"),
 "takrenovering-sollentuna-2": ("3:2", "close-up of gray concrete roof tiles with pine needles and moss collected along a metal gutter"),
 "takrenovering-vallentuna-1": ("4:3", "1980s Swedish villa with red concrete tile roof and light wooden facade in a residential street, Ormsta Vallentuna"),
 "takrenovering-vallentuna-2": ("3:2", "old falu red barn with red corrugated metal roof in open farmland, Roslagen countryside, Vallentuna"),
 "takrenovering-upplands-vasby-1": ("4:3", "quiet Swedish villa street with 1970s houses that all have similar dark concrete tile roofs, Bollstanäs Upplands Väsby"),
 "takrenovering-upplands-vasby-2": ("3:2", "close-up of a concrete tile roof edge with new black metal eaves flashing and a new half-round gutter with downpipe"),
 "takrenovering-varmdo-1": ("4:3", "former Swedish summer cottage turned year-round home, red painted wood with white trim and a dark standing-seam metal roof, in pine forest near the sea, Hemmesta Värmdö"),
 "takrenovering-varmdo-2": ("3:2", "weathered standing-seam metal roof ridge and gable trim of a house on a rocky point with the Baltic archipelago behind, windswept pines"),
 "takrenovering-tyreso-1": ("4:3", "modest old Swedish red wooden summer cottage from the 1940s that has been extended with a later lower wing, two different roof heights, gray concrete tiles on the old part and dark metal on the extension, pine trees and granite, glimpse of a bay, Tyresö"),
 "takrenovering-tyreso-2": ("3:2", "1960s Swedish villa with gray concrete tile roof with moss on the north slope under large spruce trees, Krusboda"),
 "takrenovering-haninge-1": ("4:3", "late 1800s Swedish wooden summer villa with ornate carpentry, glazed veranda and red standing-seam metal roof on a hill above a calm archipelago bay, Dalarö, empty scene"),
 "takrenovering-haninge-2": ("3:2", "1970s Swedish villa with dark brown concrete tile roof and brown wooden facade, birch trees, Vendelsö Haninge"),
 "takrenovering-enskede-1": ("4:3", "1910s Swedish wooden garden-city house with steep red clay tile roof, picket fence and fruit trees, Gamla Enskede Stockholm, spring"),
 "takrenovering-enskede-2": ("3:2", "close-up of old weathered red clay roof tiles with a few slightly lighter replacement tiles and a little moss in the joints"),
 "takrenovering-alvsjo-1": ("4:3", "1920s Swedish wooden villa with brown-red clay tile roof and a glazed veranda with its own small roof, large garden with lilacs, Herrängen Älvsjö"),
 "takrenovering-alvsjo-2": ("3:2", "detail of a small metal-clad bay window roof joined to a red clay tile roof on an old Swedish wooden villa"),
 "takrenovering-norrtalje-1": ("4:3", "red Swedish wooden house with white corners and black standing-seam metal roof on coastal rocks in the Roslagen archipelago, Norrtälje, pines"),
 "takrenovering-norrtalje-2": ("3:2", "small Swedish archipelago summer cottage with low-pitched roof covered in bitumen felt, pines and granite, Roslagen"),
 "takrenovering-sodertalje-1": ("4:3", "1930s Swedish plastered villa with red clay tile roof on a hillside overlooking a lake, Södertälje"),
 "takrenovering-sodertalje-2": ("3:2", "1970s Swedish villa with gray concrete tile roof at the edge of a forest, Pershagen Södertälje"),
 "taklaggare-norrtalje-1": ("4:3", "falu red Swedish farmhouse with red clay tile roof and white corners in open farmland, Rimbo Norrtälje, summer"),
 "taklaggare-norrtalje-2": ("3:2", "row of small red and white fishing huts with metal roofs by a rocky harbour, Grisslehamn style, calm sea"),
 "taklaggare-sodertalje-1": ("4:3", "red Swedish wooden countryside villa with black standing-seam metal roof, meadow and oak trees, Järna"),
 "taklaggare-sodertalje-2": ("3:2", "1960s Swedish brick villa with dark concrete tile roof in a suburban street, Södertälje"),
 "taklaggare-sigtuna-1": ("4:3", "old low wooden houses with red clay tile roofs along a narrow cobbled street in a small historic Swedish town, Sigtuna, lake Mälaren glimpse"),
 "taklaggare-sigtuna-2": ("3:2", "1970s Swedish suburban villas with brown concrete tile roofs and wooden facades, Märsta"),
}

def run(name):
    aspect, prompt = JOBS[name]
    out = os.path.join(IMG, name + ".webp")
    if os.path.exists(out):
        return name + " skip"
    tok = os.environ["REPLICATE_API_TOKEN"]
    body = json.dumps({"input": {"prompt": prompt + STYLE, "aspect_ratio": aspect, "output_format": "png",
                                 "safety_tolerance": 2, "prompt_upsampling": False}}).encode()
    req = urllib.request.Request("https://api.replicate.com/v1/models/black-forest-labs/flux-1.1-pro/predictions",
        data=body, headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json", "Prefer": "wait"})
    for _ in range(8):
        try:
            p = json.loads(urllib.request.urlopen(req, timeout=120).read()); break
        except urllib.error.HTTPError as e:
            if e.code != 429: return f"{name} HTTP {e.code}"
            time.sleep(15)
    else:
        return name + " 429"
    while p["status"] not in ("succeeded", "failed", "canceled"):
        time.sleep(2)
        p = json.loads(urllib.request.urlopen(urllib.request.Request(p["urls"]["get"],
            headers={"Authorization": "Bearer " + tok})).read())
    if p["status"] != "succeeded":
        return name + " FAIL"
    url = p["output"] if isinstance(p["output"], str) else p["output"][0]
    raw = urllib.request.urlopen(url).read()
    if os.environ.get("IMG_RAW"):  # originalet sparas utanför repot (för omkonvertering)
        open(os.path.join(os.environ["IMG_RAW"], name + ".png"), "wb").write(raw)
    convert(name, Image.open(io.BytesIO(raw)))
    return name + " ok"

def convert(name, im, limit=118_000):
    # WebP <= ~120 kB: först sänkt kvalitet, sedan mild utjämning (flux-brus) + kvalitet.
    from PIL import ImageFilter
    im = im.convert("RGB")
    for w, suffix in ((1200, ""), (640, "-640")):
        x = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        tries = [(x, q) for q in (82, 74, 66)] + [(x.filter(ImageFilter.SMOOTH), q) for q in (66, 58, 50, 42, 36)]
        for img, q in tries:
            buf = io.BytesIO(); img.save(buf, "WEBP", quality=q, method=6)
            if buf.tell() <= limit: break
        open(os.path.join(IMG, name + suffix + ".webp"), "wb").write(buf.getvalue())

if __name__ == "__main__":
    if sys.argv[1:2] == ["--reconvert"]:  # gör om WebP från sparade original (IMG_RAW)
        for n in JOBS:
            fp = os.path.join(os.environ["IMG_RAW"], n + ".png")
            if os.path.exists(fp):
                convert(n, Image.open(fp)); print(n, "reconverted")
        sys.exit(0)
    for n in (sys.argv[1:] or list(JOBS)):
        print(run(n), flush=True)
