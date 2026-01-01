import csv, json
from collections import defaultdict
from pathlib import Path

CONJ_TSV = Path("conjuncts.tsv")
WORDS_TSV = Path("conjunct_words.tsv")
OUT_JSON = Path("conjuncts.json")

def read_tsv(path: Path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def main():
    conj_rows = read_tsv(CONJ_TSV)
    word_rows = read_tsv(WORDS_TSV)

    words_by = defaultdict(list)
    for r in word_rows:
        cid = r["conj_id"].strip()
        words_by[cid].append({
            "word": r["word"].strip(),
            "hint": r.get("hint","").strip(),
            "level": int(r.get("level","1") or "1"),
            "file": r["file"].strip()
        })

    out = []
    for r in conj_rows:
        cid = r["id"].strip()
        c1 = r.get("c1","").strip()
        c2 = r.get("c2","").strip()
        formation = [c1, c2] if (c1 and c2) else None

        audio = (r.get("audio","") or "").strip() or None

        out.append({
            "id": cid,
            "module": r["module"].strip(),
            "form": r["form"].strip(),
            "hint": r.get("hint","").strip(),
            "formation": formation,   # only shown if present
            "audio": audio,           # optional isolated conjunct audio (Module A)
            "words": words_by.get(cid, [])
        })

    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_JSON} with {len(out)} conjuncts.")

if __name__ == "__main__":
    main()
