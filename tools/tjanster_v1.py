# -*- coding: utf-8 -*-
"""Register för tjänstehubbar och ortsidor (tjänster v1, 2026-10-25).
Innehållet ligger i tools/tj_*.py som var och en definierar PAGES_TJ = {fil: {...}}.
En modul som inte går att importera hoppas över med varning (så att generatorn inte
stoppas av en halvfärdig fil). Schema per sida – se tools/tj_check.py."""
import importlib, sys

MODULES = ["tj_hub_malare", "tj_hub_badkok", "tj_hub_golvsnick", "tj_malare_a", "tj_malare_b",
           "tj_badrum_bygg", "tj_snickare"]

# Tjänster: brödsmula, Service-schema, kortsnitt.
TJ_SERVICES = {
  "malare":            {"crumb": "Målare", "service_type": "Målning inomhus och utomhus", "card": "Målning inne och ute."},
  "badrumsrenovering": {"crumb": "Badrumsrenovering", "service_type": "Badrumsrenovering", "card": "Nytt badrum med tätskikt."},
  "koksrenovering":    {"crumb": "Köksrenovering", "service_type": "Köksrenovering", "card": "Nytt eller renoverat kök."},
  "golvlaggning":      {"crumb": "Golvläggning", "service_type": "Golvläggning och golvslipning", "card": "Nya golv och slipning."},
  "snickare":          {"crumb": "Snickare", "service_type": "Snickeriarbeten", "card": "Snickeri inne och ute."},
  "fasadrenovering":   {"crumb": "Fasadrenovering", "service_type": "Fasadrenovering", "card": "Puts, panel och tilläggsisolering."},
  "fonsterbyte":       {"crumb": "Fönsterbyte", "service_type": "Fönsterbyte", "card": "Nya fönster och fönsterdörrar."},
  "byggforetag":       {"crumb": "Byggfirma", "service_type": "Byggföretag – total entreprenad", "card": "Total entreprenad för villan."},
}
# Hubb per tjänst. byggforetag-<ort> hör till befintliga byggfirma.html (samma intent).
TJ_HUB = {"malare": "malare.html", "badrumsrenovering": "badrumsrenovering.html",
          "koksrenovering": "koksrenovering.html", "golvlaggning": "golvlaggning.html",
          "snickare": "snickare.html", "fasadrenovering": "fasadrenovering.html",
          "fonsterbyte": "fonsterbyte.html", "byggforetag": "byggfirma.html"}

TJ = {}
for _m in MODULES:
    try:
        TJ.update(importlib.import_module(_m).PAGES_TJ)
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
