#!/usr/bin/env python3
import json
from pathlib import Path

TSV = Path("words.tsv")
OUT = Path("words.json")

if not TSV.exists():
    raise SystemExit("Missing words.tsv")

lines = TSV.read_text(encoding="utf-8").splitlines()
header = lines[0].split("\t")

required = {"id", "word", "hint", "level", "file"}
if not required.issubset(set(header)):
    raise SystemExit(f"TSV must contain columns: {required}")

idx = {name: header.index(name) for name in header}

words = []
for line in lines[1:]:
    if not line.strip():
        continue
    cols = line.split("\t")
    entry = {
        "id": cols[idx["id"]],
        "word": cols[idx["word"]],
        "hint": cols[idx["hint"]],
        "level": int(cols[idx["level"]]),
        "file": cols[idx["file"]]
    }
    words.append(entry)

OUT.write_text(
    json.dumps(words, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)

print(f"Created {OUT} with {len(words)} entries.")
