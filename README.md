# Mapping Global China: Chinese Heritage Beyond China (pilot)

A feasibility study for a new layer of the Mapping Global China project: a global map of Chinese heritage presence and heritage-making outside China.

The project asks:

> What counts as "Chinese heritage" outside China, who defines it as such, and how is that definition changing over time?

It keeps each physical site separate from the actors and narratives attached to it, and it records each source's original wording rather than imposing one definition.

- **Supervisor:** Prof. Maria Adele Carrai (University of Oxford)
- **Researcher:** Quentin Mei (M.S. Data Science, Columbia University)
- **Stage:** feasibility study, Phase 1 (source discovery and inventory)

## Status

| Phase | Scope | Status |
| --- | --- | --- |
| 0 | Admin, course credit, repo setup | In progress |
| 1a | UNESCO data | Done (2026-09-30) |
| 1b | Chinese government, embassy and research sources | Done (2026-09-30) |
| 1c | Host-country and diaspora sources | Next |
| 1d | Non-site data (agreements, partnerships, projects) | Not started |
| 2 | Access assessment (APIs vs scraping) | Not started |
| 3 | Data model and entity matching | Not started |
| 4 | Proof-of-concept dataset (3-4 regions) | Not started |
| 5 | Tracking framing changes over time | Not started |
| 6 | Automation vs manual verification | Not started |
| 7 | Feasibility report | Not started |

The full plan is in [docs/roadmap.md](docs/roadmap.md), and the Phase 1 findings so far are in [docs/findings_phase1.md](docs/findings_phase1.md).

## Repository layout

```
data/
  raw/          Source extracts as collected (dated file names)
  processed/    Phase 1 workbook (.xlsx) and one CSV per sheet in csv/
scripts/        Build scripts that produce data/processed from data/raw
docs/           Roadmap, findings and data-lineage log
```

## Data

`data/processed/Mapping_Global_China_Phase1_Sources.xlsx` contains:

| Sheet | Contents |
| --- | --- |
| China WH List | China's 61 World Heritage properties: Chinese names, coordinates, transnational flag, outward links in UNESCO's text |
| China Tentative List | China's 60 Tentative List entries |
| Sites Abroad Linked to China | 33 World Heritage sites in other countries whose UNESCO text mentions China, Chinese people or the Silk Roads |
| Other UNESCO Records | Intangible heritage, Memory of the World, Silk Roads programme, related centres |
| Docs - Silk Roads 1442 | Document trail for the Silk Roads: Chang'an-Tianshan Corridor |
| Data Access | What each UNESCO source offers, gaps and terms of use |
| 1b Chinese Sources | 12 Chinese sources assessed for coverage, structure, access, history and framing |
| 1b Framing Examples | 20 dated verbatim quotes (Chinese with English gloss) |
| 1b Chinese Projects Abroad | 15 aid-restoration and joint-archaeology projects |

The same sheets are in `data/processed/csv/` as UTF-8 CSV files.

## Rebuild

```bash
pip install -r requirements.txt
python scripts/build_phase1a.py
python scripts/build_phase1b.py
python scripts/export_csv.py
```

`build_phase1b.py` builds on the Phase 1a workbook, and the CSV export reads the combined workbook. The Phase 1a workbook is an intermediate file and is not committed.

## Terms of use and attribution

UNESCO World Heritage data comes from the World Heritage Centre's syndication feeds and web pages. UNESCO states that "any republication, online or in any other form, of any UNESCO/WHC data requires prior written authorization."

Copyright © 1992-2026 UNESCO/World Heritage Centre. All rights reserved. Source: https://whc.unesco.org

This repository is for non-commercial research. Written permission from UNESCO should be obtained before any UNESCO-derived data is published as part of a public map layer.

Quotes from Chinese government, embassy and research websites are short excerpts, each linked to its source for research and commentary.

English glosses and the "link type" and "framing tags" columns are the researcher's own coding and have not yet been reviewed.
