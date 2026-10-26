#!/usr/bin/env python3
"""Print every $0 model enabled in this OpenCode install, grouped by provider.

Reads data/model.json (produced by scripts/snapshot.sh).
"""
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
models = json.loads((root / "data" / "model.json").read_text())["data"]

by_provider: dict[str, list[str]] = {}
for m in models:
    cost = (m.get("cost") or [{}])[0] or {}
    if not (cost.get("input") or 0) and not (cost.get("output") or 0):
        by_provider.setdefault(m["providerID"], []).append(m["id"])

for pid in sorted(by_provider):
    print(f"{pid} ({len(by_provider[pid])}):")
    for mid in sorted(by_provider[pid]):
        print(f"  {pid}/{mid}")
