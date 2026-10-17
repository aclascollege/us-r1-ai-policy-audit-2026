#!/usr/bin/env python3
"""Parse the US Carnegie R1 AI Policy Audit 2026 raw batch tables into CSV + JSON.
Applies the two fix files (batch-10 rows 4,7; batch-13 row 9).
Run: python3 parse.py
"""
import csv, json, re
from pathlib import Path
from collections import Counter

HERE = Path(__file__).parent
RAW = HERE / "raw"

def split_row(line: str):
    parts = re.split(r'(?<!\\)\|', line.strip())
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [p.replace("\\|", "|").strip() for p in parts]

def is_header_or_sep(cells):
    if not cells:
        return True
    first = cells[0].strip()
    if re.fullmatch(r"[\s\-|:]+", first):
        return True
    return not re.match(r"^[\d]", first)

def norm(v):
    return re.sub(r"\*", "", v).strip().upper()

def parse_file(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = split_row(line)
        if is_header_or_sep(cells):
            continue
        rows.append(cells)
    return rows

# key: (batch_no, row_no) -> cells
table = {}
for i in range(1, 17):
    p = RAW / f"us-r1-batch-{i}.md"
    for cells in parse_file(p):
        table[(i, int(cells[0]))] = cells

# apply fixes
for cells in parse_file(RAW / "us-r1-batch-10-fix.md"):
    table[(10, int(cells[0]))] = cells
for cells in parse_file(RAW / "us-r1-batch-13-fix.md"):
    table[(13, int(cells[0]))] = cells

rows = [table[k] for k in sorted(table)]
print("total rows:", len(rows))
names = [c[1] for c in rows]
assert len(rows) == 187, f"expected 187, got {len(rows)}"
assert len(set(names)) == 187, "duplicate university names!"

recs = []
for n, c in enumerate(rows, 1):
    pol = norm(c[3])
    assert pol in ("YES", "NO", "UNCLEAR"), f"bad policy value: {c[3]}"
    url = c[4]
    url = None if url in ("—", "-", "") else url
    recs.append({
        "id": f"us-r1-{n:03d}",
        "university": c[1],
        "official_domain": c[2],
        "has_policy": pol,
        "policy_url": url,
        "page_title": c[5] or None,
        "date_info": c[6] or None,
        "scope": c[7] or None,
        "note": c[8] or None,
    })

print("counts:", dict(Counter(r["has_policy"] for r in recs)))
print("NO:", [r["university"] for r in recs if r["has_policy"] == "NO"])
print("UNCLEAR:", [r["university"] for r in recs if r["has_policy"] == "UNCLEAR"])

with open(HERE / "us-r1-ai-policy-audit-2026.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(recs[0].keys()))
    w.writeheader()
    w.writerows(recs)

with open(HERE / "us-r1-ai-policy-audit-2026.json", "w", encoding="utf-8") as f:
    json.dump({
        "dataset": "US Carnegie R1 AI Policy Audit 2026",
        "audit_date": "2026-10-17",
        "publisher": "Study Intelligence (aclas.si)",
        "license": "CC-BY-4.0",
        "universe": "2025 Carnegie Classification R1 institutions (187)",
        "records": recs,
    }, f, ensure_ascii=False, indent=1)
print("wrote csv + json")
