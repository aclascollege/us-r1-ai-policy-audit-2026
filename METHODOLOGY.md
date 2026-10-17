# Methodology — US Carnegie R1 AI Policy Audit 2026

Audit date: **2026-10-17**. Snapshot, not a live registry.

## Universe

All **187 institutions** in the 2025 Carnegie Classification R1 category
("very high research activity"), cross-checked against the Wikipedia "List of
research universities in the United States" R1 table re-fetched on audit day:
exact match, 0 missing / 0 extra. (The "146" figure sometimes cited is the
2021 Carnegie count.)

## What counts

Same rules as the global audit (`../ai-policy-audit-2026/METHODOLOGY.md`):

- **YES** = a page on the university's **own official domain** containing
  guidance/policy on AI use (students, teaching, research, or all-community).
  Generic academic-integrity pages that never mention AI do **not** count.
  Every YES URL was opened and confirmed live on 2026-10-17 (crawl-corroboration
  fallback transparently noted where used).
- **NO** = adopted no AI policy after real searching (English).
- **UNCLEAR** = could not verify (rate-blocked, portal-gated, third-party
  domain only, draft-only). Not proven absent.

## Caveats

- ~30 "soft YES" rows are flagged in `AUDIT-LOG.md` (guidance-level documents,
  school-level scope, crawl-only confirmations, draft-labeled PDFs, one
  NetID-gated policy). Highest-risk: CUNY Graduate Center ("Draft" label),
  Kansas / Kansas State (guidance but "no university-wide policy" stated),
  WVU / WPI / Yale (crawl-only), MUSC (policy NetID-gated).
- Two rows were corrected during the audit; provenance kept in
  `raw/us-r1-batch-10-fix.md` and `raw/us-r1-batch-13-fix.md`.

## Reproducibility

`parse.py` generated CSV/JSON from `raw/` batch tables (fixes applied).
