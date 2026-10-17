# Methodology — Global University AI Policy Audit 2026

Audit date: **2026-10-14**. Snapshot, not a live registry.

## What was counted

**YES** = a page on the university's **own official domain** containing guidance or
policy on AI use (students, teaching, research, or all-community). Generic
academic-integrity pages that never mention AI do **not** count.

**NO** = searched in English (+ local language for non-English countries) and found
no such page.

**UNCLEAR** = could not verify — dead links, portal-gated intranets, crawler-blocked
domains (e.g. ui.ac.id), or insufficient evidence either way.

## How each record was verified

Web search + direct verification: each policy URL below was opened and confirmed to
load AI usage guidance on 2026-10-14, or corroborated by search-engine crawl of the
official page plus the MDPI April 2026 systematic audit of top-200 universities'
GenAI guidelines where direct fetch failed.

Searches ran in English + local languages (German, French, Chinese, Japanese, Korean,
Spanish, Portuguese, Arabic, Indonesian, Thai, Vietnamese). This matters: continental
European and East Asian universities often publish first in the national language,
and English-only surveys systematically undercount them.

## Samples

- **QS 2026 ranks 1–50** (50 rows), **51–100** (49 rows), **101–150** (50 rows):
  every ranked institution checked in order.
- **Global South flagships** (37 rows): flagship universities across Brazil, Argentina,
  Egypt, Nigeria, Kenya, South Africa, India, Pakistan, Bangladesh, Indonesia,
  Philippines, Vietnam, Thailand, Malaysia, Mexico, Chile, China.

## Known limitations (read before citing)

1. 15 university names appear in two samples (30 rows flagged `name_overlap`) —
   the rank-band files overlap (e.g. TU Delft listed at QS 47 and QS 61).
   Institution-level counts should deduplicate on `university`.
2. ~5 Global South YES cases are faculty/school-level, not university-wide.
3. Last-updated dates are inconsistently displayed by universities; "issued in the
   last 12 months" is approximate.
4. Two secondary-literature errors were caught and excluded during the audit
   (a paper conflating Quinnipiac's catalog with Qatar University; a
   micro-credential page cited as a "policy").
5. Policies are being published monthly — verify before citing any single row
   for a current claim.

## Reproducibility

`parse.py` in this directory is the exact script that generated the CSV/JSON from
the raw audit tables. Raw tables: `~/workspace/aclas-report/ai-policy-audit/`
(`qs-001-050.md`, `qs-051-100.md`, `qs-101-150.md`, `global-south-35.md`).
Corrections welcome via issues or pull requests.
