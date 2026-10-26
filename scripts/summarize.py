#!/usr/bin/env python3
"""Print a per-provider summary from data/providers.csv and data/model.json.

Usage: scripts/summarize.py [free|all]
"""
import csv
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((root / "data" / "providers.csv").open()))
mode = sys.argv[1] if len(sys.argv) > 1 else "free"

if mode == "free":
    rows = [r for r in rows if r["free"] in {"yes", "partial", "local", "claimed", "listed"}]
    rows.sort(key=lambda r: ({"yes": 0, "local": 1, "partial": 2, "claimed": 3, "listed": 4}[r["free"]], r["name"].lower()))
else:
    rows.sort(key=lambda r: r["name"].lower())

width = max(len(r["name"]) for r in rows) if rows else 10
for r in rows:
    how = re.sub(r"\s+", " ", r["how_to_get_free"])[:110]
    print(f'{r["free"]:<13} {r["provider_id"]:<26} {r["name"]:<{width}}  {how}')
print(f"\n{len(rows)} providers shown")
