import csv
import json
from pathlib import Path

tsv_path = Path("conj/conjunct_words.tsv")
json_path = Path("conj/conjunct_words.json")

words = []

with tsv_path.open(encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        words.append({
            "conj_id": row["conj_id"].strip(),
            "word": row["word"].strip(),
            "hint": row["hint"].strip(),
            "level": int(row["level"]) if row["level"] else None,
            "file": row["file"].strip(),
            "idx": int(row["idx"]) if row["idx"] else None
        })

with json_path.open("w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"✔ Wrote {len(words)} conjunct words → {json_path}")
