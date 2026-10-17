# US Carnegie R1 AI Policy Audit 2026

An open dataset of **all 187 US Carnegie R1 research universities** (2025
Carnegie Classification), audited for whether each publishes official AI usage
guidance/policy on its own domain.

## Headline numbers

- **178 of 187 (95.2%)** publish verifiable AI usage guidance — the US research
  sector has effectively standardized on governing AI, not banning it.
- **1 confirmed NO:** University of Wyoming (no adopted policy; only a 2023
  working-group draft).
- **8 UNCLEAR** (could not verify — not proven absent): Brown, Clemson,
  UT Health San Antonio, UT Southwestern, UMass-Boston, Miami, UNH,
  Weill Cornell Medicine. Reasons per row in `note`.

## Files

| File | Description |
|---|---|
| `us-r1-ai-policy-audit-2026.csv` / `.json` | 187 rows, one per R1 university |
| `METHODOLOGY.md` | Definitions, verification rules, caveats |
| `AUDIT-LOG.md` | List source, corrections, least-sure rows |
| `raw/` | The 16 audited batch tables + 2 fix files (provenance) |
| `parse.py` | Exact script that generated CSV/JSON from raw tables |

## Columns

`id`, `university`, `official_domain`, `has_policy` (`YES`/`NO`/`UNCLEAR`),
`policy_url` (opened and confirmed live on 2026-10-17), `page_title`,
`date_info`, `scope` (students / faculty-teaching / all-community…),
`note`.

## Notes

- Snapshot date: **2026-10-17**. Policies change; verify before citing a row.
- ~30 rows are "soft YES" (guidance-level vs formal policy, crawl-only
  confirmation, draft-labeled PDFs) — flagged in `AUDIT-LOG.md`. A wrong YES
  is worse than an UNCLEAR; treat soft YESes accordingly.
- Corrections welcome via issues/PRs.

## License

[CC-BY-4.0](LICENSE) — cite "Study Intelligence (aclas.si)".
