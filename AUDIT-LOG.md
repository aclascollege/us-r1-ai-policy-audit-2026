# AUDIT LOG — US Carnegie R1 AI Policy Audit (2026-10-17)

Auditor: Study Intelligence (aclas.si research). Audit date: **2026-10-17**.
Methodology: [ai-policy-audit-2026/METHODOLOGY.md](https://github.com/aclascollege/ai-policy-audit-2026/blob/main/METHODOLOGY.md) (same as the 186-row global audit) — English search, YES only when a page on the university's OWN official domain contains AI usage guidance/policy; NO only after real searching; UNCLEAR when unverifiable (dead links, portal-gated, rate-limited, etc.). A wrong YES is worse than an UNCLEAR.

Raw tables: `raw/us-r1-batch-1.md` … `raw/us-r1-batch-16.md` (15 batches × 12 schools + final batch × 7 schools = 187 rows).

## R1 list source + coverage check

- Source: Wikipedia, "List of research universities in the United States", accessed and re-fetched **2026-10-17** (page header confirms "187 institutions … as of the 2025 update").
- The 2025 Carnegie update expanded R1 to **187 institutions**; the "146" figure was the pre-2025 (2021) count. All 187 were audited — no sampling.
- Coverage validated programmatically on 2026-10-17: the 187 audited school names were extracted from the batch tables and compared (normalized) against the 187 names scraped from the Wikipedia R1 table the same day — **exact match: 0 missing, 0 extra, 0 duplicates**. The audit uses Carnegie's official institutional names verbatim (including campus qualifiers like "Georgia Institute of Technology-Main Campus").

## Corrections applied (provenance)

1. **Batch 13, row 9 — wrong school audited.** The original worker audited the University of South Florida in the slot assigned to the University of North Carolina at Chapel Hill. A dedicated re-audit (2026-10-17) confirmed UNC Chapel Hill = YES (`https://curricula.unc.edu/required-syllabus-statements/`, Office of Undergraduate Curricula "Artificial Intelligence (AI) Use Policy", Spring 2026). Row 9 of `us-r1-batch-13.md` now carries the correct school and verdict; the correction is preserved in `raw/us-r1-batch-13-fix.md`.
2. **Batch 10 — two UNCLEAR rows upgraded to YES.** The first pass marked University of Central Florida and University of Colorado Boulder UNCLEAR because direct fetches were rate-limited. A dedicated re-check (2026-10-17) opened and confirmed both URLs (UCF: `https://aiforall.ucf.edu/students/ethical-use-of-ai/`; CU Boulder: `https://www.colorado.edu/center/teaching-learning/technology-ai/teaching-learning-ai/considerations-using-ai-teaching-and-learning`), so batch 10 is now 12/12 YES. Re-check documented in `raw/us-r1-batch-10-fix.md`.

## Headline results

- **YES: 178 / NO: 1 / UNCLEAR: 8** (187 total)

## Schools that could not be classified (UNCLEAR, 8)

| School | Why |
|---|---|
| Brown University (batch 1) | brown.edu has a GAITL committee report (July 2026), sample AI syllabus statements, and an AI Policy Explorer — but Brown's own materials state university-wide baseline GenAI rules were still being drafted (GAITL Phase 2). No published institutional AI usage policy could be confirmed. |
| Clemson University (batch 2) | The CCIT "Generative AI Guidelines" page exists with substantive student/instructor/research rules per search-engine crawl, but direct fetches were rate-blocked and an alternate page rendered empty. Not confirmed live → UNCLEAR. |
| University of Massachusetts-Boston (batch 12) | Only a Writing Center-level AI policy found on umb.edu (defers to instructor policies); no university-wide policy after multiple searches. |
| University of Miami (batch 12) | No university-wide policy after 4 searches; only program-level items (e.g. Business School graduate-admissions AI guidelines). |
| University of New Hampshire-Main Campus (batch 13) | UNH IRB published "Guidance for Research Involving Generative Artificial Intelligence" (April 2026) and its Teaching & Learning hub references a USNH AI Standard per crawl — but no specific UNH policy page could be opened and confirmed. |
| Weill Cornell Medicine (batch 16) | No AI use guidance on weill.cornell.edu (only an "AI to Advance Medicine" program announcement); the library's AI guide sits on third-party libguides.com. |
| UT Health Science Center at San Antonio (batch 8) | An institutional AI policy (HOOP 5.9.10) exists but is hosted on powerdms.com, not uthscsa.edu; on the own domain only course-level AI mentions were found → UNCLEAR per the own-domain rule. |
| UT Southwestern Medical Center (batch 8) | Public page (utsouthwestern.edu/ai/) confirms AI Responsible Usage guidelines exist, but they live behind VPN/intranet; the library AI guide is on third-party libguides.com → UNCLEAR per the portal-gating rule. |

Note: #7 and #9 in batch 8 (UT San Antonio / UT Health Science Center at San Antonio) are now one merged institution, but were audited on their separate assigned domains per the batch plan.

## The single NO

- **University of Wyoming** (batch 15): three English searches found no adopted AI use policy on uwyo.edu — only a 2023 working-group recommendations report (draft syllabus language), library LibGuides, and AI commission/enterprise-platform news. A draft report is not an adopted policy → NO.

## Rows we're least sure about (soft YESes — guidance-level rather than formal policy, school-level scope, or crawl-only confirmation)

Per the methodology's limitations section, school/department-level and guidance-style pages still qualify as YES, but these are the rows most likely to be debated on re-review:

- **Brandeis (b1)** — YES rests on the official AI Task Force page describing the "AI Framework for Brandeis Students"; the framework PDF itself 403'd to our fetch (corroborated via crawl of the official PDF).
- **Baylor College of Medicine (b1)** — YES rests on the official 2026–2027 catalog PDF (§8.4 GenAI guidance, cdn.bcm.edu); the referenced "BCM Institutional Guidelines" appear intranet-only.
- **Colorado State (b2)** — YES via the TILT "AI and the CSU Student Conduct Code" page (posted Jan 2023), an official student-facing interpretation; CSU's newer posture is in the AI@CSU hub.
- **CUNY Graduate Center (b2)** — official PDF explicitly labeled "Draft, June 5, 2026".
- **East Carolina (b3)** — YES rests on a library research guide with AI syllabus templates (guidance-level, adapted from Univ. of Delaware, hosted on ECU's domain).
- **Georgia Tech (b3)** — YES rests on OIT's "Academic Guidance for Generative AI" (faculty/staff); the formal institute-wide policy was still in draft at audit time.
- **Kansas State (b4)** — the official ARM guidance PDF couldn't be opened (429, retry prohibited); page text corroborated via search-engine crawl of the official PDF (methodology allows this fallback).
- **MUSC (b4)** — policy text is NetID-gated; the verified musc.edu URL is a news-format milestones page documenting the "Plagiarism and Artificial Intelligence Guidelines" and the Jan 2024 governance policy rather than the guidelines themselves.
- **Montana State (b5)** — two Center for Faculty Excellence AI URLs from the index 404'd (stale); confirmed instead via the Provost Office "AI Resources" hub (montana.edu/provost/faculty/AI.html).
- **NYU (b5)** — school-level guidance only (Steinhardt AI Hub); countable per methodology but school-level.
- **NDSU (b5)** — page states "there are no standalone AI policies," but the university KB article (updated 2026-08-14) contains substantive university-wide guidance.
- **Northeastern (b5)** — Research Compliance page failed at network level; confirmed via the official "AI at Northeastern — A Student Guide" PDF (learning.northeastern.edu).
- **Nova Southeastern, Ohio University, RPI, Purdue (b6)** — all YES but noted by the worker as the batch's softest calls.
- **SIU-Carbondale (b7)** — only a library LibGuide with faculty guidance found; no university-wide policy.
- **Stony Brook (b7)** — CELT page frames itself as "guidance, not policy"; a stronger University Senate SCEDIT AI statement exists but its PDF couldn't be opened (rate-limited).
- **Texas A&M (b7)** — grad-school-level guidance; campus-wide AI hub (ai.tamu.edu) guidance subpage 404'd, suggesting a recent site restructure.
- **University at Albany (b9)** — teaching-design guidance on discouraging AI misuse rather than an explicit permitted/prohibited-use policy.
- **Kansas (b11)** — page explicitly says KU has "no university-wide policy specific to generative AI in teaching and learning," but is an official AI-hub page giving substantive student-facing AI guidance.
- **UGA (b11)** — CTL page 403'd on fetch; cited the Graduate School thesis/dissertation GenAI policy instead, with CTL default-rule evidence from search-engine crawl only.
- **Louisville (b11)** — Delphi Center for Teaching and Learning guidance (faculty-teaching), not a formal policy statement.
- **UMBC (b12)** — Provost post is public and substantive, but the full guidelines document sits behind my.UMBC files.
- **Toledo (b14)** — YES rests on a verified College of Law-level policy; the Provost's university-level "AI Policies" page exists per search snippets but failed to load (network error).
- **Penn (b14)** — grounded on the verified CETLI "Generative AI Policies" page (updated 2025-08-19); a central ISC community statement could not be confirmed at a verbatim URL.
- **USC Columbia (b14)** — CTE guiding-principles page served on an artinstitute.sc.edu subdomain of sc.edu (linked from a www.sc.edu news announcement); date from the announcement.
- **West Virginia University, Worcester Polytechnic Institute, Yale (b16)** — direct fetches failed (403 / resolver error / 429); verified via search-engine crawl of the official pages per the methodology's crawl-corroboration fallback; Yale's Provost guidelines page re-checks live (200, 2026-10-17).

## Operational notes

- Browser rate limiting (429/403) was hit on several pages; workers used alternative URLs or the documented crawl-corroboration fallback rather than retrying blocked calls. Four 404s were stale-index artifacts (Montana State ×2, Stony Brook's old CELT aibot page, TAMU's ai.tamu.edu guidance subpage).
- Table formatting: note/title cells escape embedded pipes as `\|` (standard markdown), so naive pipe-splitting under-counts columns — real column count is 9 everywhere; validated with an escape-aware parser on 2026-10-17.
