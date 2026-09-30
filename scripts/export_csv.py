"""Export every sheet of the Phase 1 workbook to CSV (UTF-8) for diffing and pipelines.

Run from the repo root: python scripts/export_csv.py
"""
import csv
import re
from pathlib import Path
from openpyxl import load_workbook

SRC = Path("data/processed/Mapping_Global_China_Phase1_Sources.xlsx")
OUT = Path("data/processed/csv")
OUT.mkdir(parents=True, exist_ok=True)

wb = load_workbook(SRC, data_only=True)
for i, ws in enumerate(wb.worksheets):
    if ws.title == "README":
        continue
    name = re.sub(r"[^a-z0-9]+", "_", ws.title.lower()).strip("_")
    path = OUT / f"{i:02d}_{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for row in ws.iter_rows(values_only=True):
            w.writerow(["" if v is None else v for v in row])
    print("wrote", path)
