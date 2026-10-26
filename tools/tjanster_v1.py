# -*- coding: utf-8 -*-
"""Register för tjänstehubbar och ortsidor (tjänster v1, 2026-10-25).
Innehållet ligger i tools/tj_*.py som var och en definierar PAGES_TJ = {fil: {...}}.
En modul som inte går att importera hoppas över med varning (så att generatorn inte
stoppas av en halvfärdig fil). Schema per sida – se tools/tj_check.py."""
import importlib, sys

MODULES = ["tj_hub_malare", "tj_hub_badkok", "tj_hub_golvsnick", "tj_malare_a", "tj_malare_b",
           "tj_badrum_bygg", "tj_snickare",
           # v2 (2026-10-25): 18 ortsidor badrum/kök/målare
           "tj_v2_badrum", "tj_v2_kok", "tj_v2_malare",
           # v3 (2026-10-25): 18 ortsidor golvläggare/snickare/fasadrenovering
           "tj_v3_golv", "tj_v3_snickare", "tj_v3_fasad",
           # v4 (2026-10-25): plåtslagarhubb + 18 ortsidor plåtslagare/fönsterbyte/köksrenovering
           "tj_v4_plat", "tj_v4_fonster", "tj_v4_kok",
           # v5 (2026-10-25): 18 ortsidor badrumsrenovering/målare/takbyte
           "tj_v5_badrum", "tj_v5_malare", "tj_v5_takbyte",
           # v6 (2026-10-25): 18 ortsidor golvläggare/snickare/fasadrenovering
           "tj_v6_golv", "tj_v6_snickare", "tj_v6_fasad",
           # v7 (2026-10-25): 18 ortsidor plåtslagare/fönsterbyte/köksrenovering
           "tj_v7_plat", "tj_v7_fonster", "tj_v7_kok",
           # v8 (2026-10-25): 12 ortsidor tillbyggnad/byggföretag (takrenovering-<ort> i takreno_orter.py)
           "tj_v8_tillbyggnad", "tj_v8_bygg",
           # v9 (2026-10-25): 18 ortsidor badrumsrenovering/målare/golvläggare
           "tj_v9_badrum", "tj_v9_malare", "tj_v9_golv",
           # v10 (2026-10-25): 18 ortsidor snickare/fasadrenovering/köksrenovering
           "tj_v10_snickare", "tj_v10_fasad", "tj_v10_kok",
           # v11 (2026-10-25): 18 ortsidor byggföretag/plåtslagare/golvläggare
           "tj_v11_bygg", "tj_v11_plat", "tj_v11_golv",
           # v12 (2026-10-25): 18 ortsidor byggföretag/fasadrenovering/fönsterbyte
           "tj_v12_bygg", "tj_v12_fasad", "tj_v12_fonster",
           # v13 (2026-10-25): 18 ortsidor badrumsrenovering/byggföretag/plåtslagare
           "tj_v13_badrum", "tj_v13_bygg", "tj_v13_plat",
           # v14 (2026-10-25): 18 ortsidor snickare/golvläggare/tillbyggnad
           "tj_v14_snickare", "tj_v14_golv", "tj_v14_tillbyggnad",
           # v15 (2026-10-25): 18 ortsidor fasadmålning/tapetsering (hubb malare.html) och golvslipning (hubb golvlaggning.html)
           "tj_v15_fasadmalning", "tj_v15_golvslipning", "tj_v15_tapetsering",
           # v16 (2026-10-26): 18 ortsidor fönsterrenovering (hubb fonsterbyte.html), attefallshus (hubb attefallshus.html), målare
           "tj_v16_fonsterrenovering", "tj_v16_attefallshus", "tj_v16_malare",
           # v17 (2026-10-26): 18 ortsidor tapetsering/fasadmålning (hubb malare.html) och golvslipning (hubb golvlaggning.html)
           "tj_v17_tapetsering", "tj_v17_golvslipning", "tj_v17_fasadmalning",
           # v18 (2026-10-26): 18 ortsidor tapetsering (hubb malare.html), golvslipning (hubb golvlaggning.html) och
           # totalrenovering (hubb villarenovering.html)
           "tj_v18_tapetsering", "tj_v18_golvslipning", "tj_v18_totalrenovering",
           # v19 (2026-10-26): 18 ortsidor fönsterrenovering (hubb fonsterbyte.html), tapetsering (hubb malare.html) och
           # golvslipning (hubb golvlaggning.html)
           "tj_v19_fonsterrenovering", "tj_v19_tapetsering", "tj_v19_golvslipning",
           # v20 (2026-10-26): 18 ortsidor attefallshus (hubb attefallshus.html), fasadmålning (hubb malare.html) och
           # fasadrenovering (hubb fasadrenovering.html)
           "tj_v20_attefallshus", "tj_v20_fasadmalning", "tj_v20_fasadrenovering",
           # v21 (2026-10-26): 18 ortsidor takbyte (hubb takbyte.html), totalrenovering (hubb villarenovering.html) och
           # fönsterrenovering (hubb fonsterbyte.html)
           "tj_v21_takbyte", "tj_v21_totalrenovering", "tj_v21_fonsterrenovering",
           # v22 (2026-10-26): 18 ortsidor attefallshus (hubb attefallshus.html), tillbyggnad (hubb tillbyggnad.html)
           # och takbyte (hubb takbyte.html)
           "tj_v22_attefallshus", "tj_v22_tillbyggnad", "tj_v22_takbyte",
           # v23 (2026-10-26): 18 ortsidor fönsterbyte (hubb fonsterbyte.html), badrumsrenovering och
           # totalrenovering (hubb villarenovering.html)
           "tj_v23_fonsterbyte", "tj_v23_badrum", "tj_v23_totalrenovering",
           # v24 (2026-10-26): 18 ortsidor takbyte (hubb takbyte.html), fasadmålning (hubb malare.html) och
           # fönsterrenovering (hubb fonsterbyte.html)
           "tj_v24_takbyte", "tj_v24_fasadmalning", "tj_v24_fonsterrenovering",
           # v25 (2026-10-26): 18 ortsidor tapetsering (hubb malare.html), byggföretag (hubb byggfirma.html) och
           # totalrenovering (hubb villarenovering.html)
           "tj_v25_tapetsering", "tj_v25_bygg", "tj_v25_totalrenovering",
           # v26 (2026-10-26): 18 ortsidor attefallshus (hubb attefallshus.html), tillbyggnad (hubb tillbyggnad.html)
           # och köksrenovering (hubb koksrenovering.html)
           "tj_v26_attefallshus", "tj_v26_tillbyggnad", "tj_v26_kok"]
# Moduler vars ortsidor korslänkas med ortens övriga tjänstesidor (åt båda hållen).
V4_MODULES = {"tj_v4_plat", "tj_v4_fonster", "tj_v4_kok", "tj_v5_badrum", "tj_v5_malare", "tj_v5_takbyte",
              "tj_v6_golv", "tj_v6_snickare", "tj_v6_fasad",
              "tj_v7_plat", "tj_v7_fonster", "tj_v7_kok",
              "tj_v8_tillbyggnad", "tj_v8_bygg",
              "tj_v9_badrum", "tj_v9_malare", "tj_v9_golv",
              "tj_v10_snickare", "tj_v10_fasad", "tj_v10_kok",
              "tj_v11_bygg", "tj_v11_plat", "tj_v11_golv",
              "tj_v12_bygg", "tj_v12_fasad", "tj_v12_fonster",
              "tj_v13_badrum", "tj_v13_bygg", "tj_v13_plat",
              "tj_v14_snickare", "tj_v14_golv", "tj_v14_tillbyggnad",
              "tj_v15_fasadmalning", "tj_v15_golvslipning", "tj_v15_tapetsering",
              "tj_v16_fonsterrenovering", "tj_v16_attefallshus", "tj_v16_malare",
              "tj_v17_tapetsering", "tj_v17_golvslipning", "tj_v17_fasadmalning",
              "tj_v18_tapetsering", "tj_v18_golvslipning", "tj_v18_totalrenovering",
              "tj_v19_fonsterrenovering", "tj_v19_tapetsering", "tj_v19_golvslipning",
              "tj_v20_attefallshus", "tj_v20_fasadmalning", "tj_v20_fasadrenovering",
              "tj_v21_takbyte", "tj_v21_totalrenovering", "tj_v21_fonsterrenovering",
              "tj_v22_attefallshus", "tj_v22_tillbyggnad", "tj_v22_takbyte",
              "tj_v23_fonsterbyte", "tj_v23_badrum", "tj_v23_totalrenovering",
              "tj_v24_takbyte", "tj_v24_fasadmalning", "tj_v24_fonsterrenovering",
              "tj_v25_tapetsering", "tj_v25_bygg", "tj_v25_totalrenovering",
              "tj_v26_attefallshus", "tj_v26_tillbyggnad", "tj_v26_kok"}

# Tjänster: brödsmula, Service-schema, kortsnitt.
TJ_SERVICES = {
  "malare":            {"crumb": "Målare", "service_type": "Målning inomhus och utomhus", "card": "Målning inne och ute."},
  "badrumsrenovering": {"crumb": "Badrumsrenovering", "service_type": "Badrumsrenovering", "card": "Nytt badrum med tätskikt."},
  "koksrenovering":    {"crumb": "Köksrenovering", "service_type": "Köksrenovering", "card": "Nytt eller renoverat kök."},
  "golvlaggning":      {"crumb": "Golvläggning", "service_type": "Golvläggning och golvslipning", "card": "Nya golv och slipning."},
  "snickare":          {"crumb": "Snickare", "service_type": "Snickeriarbeten", "card": "Snickeri inne och ute."},
  "fasadrenovering":   {"crumb": "Fasadrenovering", "service_type": "Fasadrenovering", "card": "Puts, panel och tilläggsisolering."},
  "platslagare":       {"crumb": "Plåtslagare", "service_type": "Plåtslageri – plåttak, takavvattning och beslag", "card": "Plåttak, hängrännor och beslag."},
  "fonsterbyte":       {"crumb": "Fönsterbyte", "service_type": "Fönsterbyte", "card": "Nya fönster och fönsterdörrar."},
  "takbyte":           {"crumb": "Takbyte", "service_type": "Takbyte", "card": "Byte av tegel-, betong- och plåttak."},
  "tillbyggnad":       {"crumb": "Tillbyggnad", "service_type": "Tillbyggnad", "card": "Mer boyta i samma hus."},
  "byggforetag":       {"crumb": "Byggfirma", "service_type": "Byggföretag – total entreprenad", "card": "Total entreprenad för villan."},
  # v15: deltjänster utan egen hubb – brödsmulan pekar på huvudtjänstens hubb.
  "fasadmalning":      {"crumb": "Målare", "service_type": "Fasadmålning", "card": "Utvändig målning av fasaden."},
  "tapetsering":       {"crumb": "Målare", "service_type": "Tapetsering", "card": "Ny tapet på väggarna."},
  "golvslipning":      {"crumb": "Golvläggning", "service_type": "Golvslipning", "card": "Slipa och ytbehandla trägolv."},
  # v16: fönsterrenovering är deltjänst under fonsterbyte.html; attefallshus.html är en vanlig sida i generate.py.
  "fonsterrenovering": {"crumb": "Fönsterbyte", "service_type": "Fönsterrenovering", "card": "Renovera de befintliga fönstren."},
  "attefallshus":      {"crumb": "Attefallshus", "service_type": "Attefallshus – komplementbostadshus", "card": "Komplementbostadshus på tomten.",
                        # nybyggnad ger inget rotavdrag – ersätter standardpunkten "ROT-avdrag direkt på fakturan".
                        "trust": ["Gratis besök och kostnadsförslag", "Nyckelfärdigt från grund till inflyttning"]},
  # v18: totalrenovering-<ort> hör till villarenovering.html (vanlig sida i generate.py). Intent: renovera hela
  # huset eller lägenheten – skild från byggforetag-<ort> (total entreprenad, lov och nybyggnad).
  "totalrenovering":   {"crumb": "Villarenovering", "service_type": "Totalrenovering", "card": "Renovera hela huset eller lägenheten."},
}
# Hubb per tjänst. byggforetag-<ort> hör till befintliga byggfirma.html (samma intent).
TJ_HUB = {"malare": "malare.html", "badrumsrenovering": "badrumsrenovering.html",
          "koksrenovering": "koksrenovering.html", "golvlaggning": "golvlaggning.html",
          "snickare": "snickare.html", "fasadrenovering": "fasadrenovering.html",
          "fonsterbyte": "fonsterbyte.html", "platslagare": "platslagare.html", "byggforetag": "byggfirma.html",
          # v5: takbyte.html är en vanlig tjänstesida i generate.py (inte i TJ) men listar ortsidorna.
          "takbyte": "takbyte.html",
          # v8: tillbyggnad.html är en vanlig sida i generate.py men listar ortsidorna.
          "tillbyggnad": "tillbyggnad.html",
          # v15: deltjänster – listas på huvudtjänstens hubb ("Fasadmålning per område" m.fl.).
          "fasadmalning": "malare.html", "tapetsering": "malare.html", "golvslipning": "golvlaggning.html",
          # v16
          "fonsterrenovering": "fonsterbyte.html", "attefallshus": "attefallshus.html",
          # v18: villarenovering.html är en vanlig sida i generate.py men listar ortsidorna.
          "totalrenovering": "villarenovering.html"}

TJ = {}
V4_FILES = set()
for _m in MODULES:
    try:
        _pt = importlib.import_module(_m).PAGES_TJ
        TJ.update(_pt)
        if _m in V4_MODULES:
            V4_FILES |= set(_pt)
    except ModuleNotFoundError as e:
        if e.name != _m:
            print(f"VARNING: {_m}: {e}", file=sys.stderr)
    except Exception as e:  # halvfärdig fil – hoppa över
        print(f"VARNING: {_m} hoppas över: {type(e).__name__}: {e}", file=sys.stderr)

# Hubbar först, sedan ortsidor (ordning för sitemap).
TJ = dict(sorted(TJ.items(), key=lambda kv: (kv[1]["kind"] != "hub", kv[0])))
TJ_DISTRICTS = {}
for _f, _d in TJ.items():
    _d["file"] = _f
    if _d["kind"] == "district":
        TJ_DISTRICTS.setdefault(_d["service"], []).append(_f)

# v4: korslänkar på samma ort. Ny ortsida -> ortens övriga tjänstesidor, och befintliga
# ortsidor -> den nya sidan (kort i blocket "Fler tjänster på/i <ort>").
def _add_card(d, f):
    rel = d.setdefault("related", [])
    if f != d["file"] and all(r[0] != f for r in rel):
        rel.append((f, TJ[f]["h1"], TJ[f]["card"]))
for _f in sorted(V4_FILES):
    _d = TJ[_f]
    if _d["kind"] != "district":
        continue
    for _g, _e in TJ.items():
        if _g != _f and _e["kind"] == "district" and _e.get("ort") == _d["ort"] and _e["service"] != _d["service"]:
            _add_card(_d, _g)
            _add_card(_e, _f)
