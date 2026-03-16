# AI Exposure of the Canadian Job Market

Analyzing how exposed Canadian occupation groups are to AI using official Statistics Canada and ESDC sources instead of the U.S. Bureau of Labor Statistics.

## What's here

This fork now combines three Canadian data sources:

- [14-10-0416-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041601) Labour force characteristics by occupation, annual
- [14-10-0417-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041701) Employee wages by occupation, annual
- [2025-2027 Employment Outlooks - NOC 2021](https://open.canada.ca/data/en/dataset/b0e112e9-cf53-4e79-8838-23cd98debe5b/resource/cb52e1d0-ab62-4357-91cc-d8f5a2114e02)

AI exposure is no longer driven by an LLM score in the site build. The dashboard now uses official StatCan EPIAC data from:

- [Experimental Estimates of Potential Artificial Intelligence Occupational Exposure in Canada, 2024](https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm)

That study reports AIOE, complementarity, and HELC/HEHC/low-exposure splits for published occupation groups based on the **2021 Census**. This repo maps those published EPIAC groups onto the **43 current NOC 2021 occupation groups** used in the StatCan annual tables.

Context studies using the same framework:

- [StatCan, January 28, 2026: employment growth since the start of the generative AI era](https://www150.statcan.gc.ca/n1/en/pub/36-28-0001/2026001/article/00001-eng.pdf)
- [ISQ, February 3, 2026: Exposition des professions a l'intelligence artificielle en 2024](https://statistique.quebec.ca/fr/fichier/exposition-professions-intelligence-artificielle-2024.pdf)

## Data pipeline

1. `fetch_statcan.py`
   Downloads the StatCan occupation tables, merges the latest employment and wage series, adds province-aggregated ESDC outlooks, and maps official StatCan EPIAC exposure fields onto the 43 dashboard occupation groups.
2. `build_site_data.py`
   Builds `site/data.json` for the frontend from `occupations.csv`.
3. `make_prompt.py`
   Builds `prompt.md`, a single markdown summary of the Canadian dataset with official EPIAC fields.
4. `site/index.html`
   Interactive visualization where area = Canadian employment and color = EPIAC high-exposure share.

## Key files

| File | Description |
|------|-------------|
| `occupations.json` | Canadian occupation-group index with NOC codes and EPIAC mapping summary |
| `occupations.csv` | Employment, wages, outlooks, and official EPIAC fields |
| `prompt.md` | Single-file markdown summary of the Canadian dataset |
| `docs/dashboard-to-noc-2021.md` | Audit of how the 43-group dashboard partitions the official NOC 2021 hierarchy |
| `pages/` | Generated occupation summaries and source notes |
| `site/` | Static website |
| `dashboard_noc_audit.py` | Reproducible dashboard-to-NOC concordance and markdown audit generator |
| `epiac_data.py` | Official EPIAC source rows and mapping logic |
| `outlook_data.py` | ESDC outlook ingestion and aggregation logic |
| `score.py` | Optional legacy LLM scoring script, not used by the site build |

## Important differences from upstream

- Source data is **Canadian** and based on **StatCan / ESDC**, not BLS handbook pages.
- Exposure is based on **official StatCan EPIAC / AIOE / complementarity** data, not only an LLM judgment.
- The dashboard mixes different reference periods intentionally:
  - exposure: mapped from the StatCan 2024 EPIAC study using **2021 Census** occupation data
  - employment and wages: latest StatCan annual tables through **2025**
  - outlook: province-aggregated ESDC outlook data for **2025-2027**
- The site works with **43 Canadian NOC occupation groups** rather than 342 detailed U.S. occupations.

## Setup

```bash
uv sync
```

No API key is required for the current site build.

## Usage

```bash
# Download and build the Canadian occupation dataset
uv run python fetch_statcan.py

# Build website data
uv run python build_site_data.py

# Generate prompt.md
uv run python make_prompt.py

# Serve the site locally
cd site && python -m http.server 8000
```

Optional legacy script:

```bash
# Experimental OpenRouter-based scoring path kept for comparison only
uv run python score.py
```

## Notes

- The StatCan downloads are cached in `tmp/statcan/`.
- `pages/` is generated output and can be recreated from `fetch_statcan.py`.
- The EPIAC mapping is an inference from the closest published StatCan occupation groups to the current NOC 2021 dashboard groups. Each generated row and page includes a mapping note.

## Backlog

1. `[x]` Add full geography mode to the current 43-group dashboard.
   Implemented in the current repo: the fetch/build pipeline now emits `stats_by_geo`, the site includes a geography selector, and the dashboard switches labour-market metrics and outlook by geography while keeping EPIAC national.

2. `[x]` Validate the dashboard-to-NOC mapping against the official NOC 2021 hierarchy.
   Implemented. The repo now generates [`docs/dashboard-to-noc-2021.md`](docs/dashboard-to-noc-2021.md), exposes hierarchy metadata in `site/data.json`, confirms that the 43 dashboard groups partition all 516 official unit groups with no gaps or overlaps, distinguishes the dashboard's labour-force-variant families from the official broad categories, and keeps small treemap families such as Resources visibly labelled.

3. `[x]` Fix Canada outlook mix semantics and expose provincial dispersion.
   Implemented in the current repo: the Canada view now separates the Canada-wide aggregate outlook mix from a province-dispersion summary computed from province labels, keeps province-only buckets such as `Very limited` and `Undetermined` visible nationally, and was checked against the generated Canada and Quebec source data.

4. `[x]` Fix tooltip mapping-note rendering in alternate views.
   Implemented in the current repo: the shared dashboard tooltip now normalizes mapping-note sentence spacing, renders multi-sentence notes as separate paragraphs, and keeps long notes readable in `Exposure vs Change` and `Exposure vs Outlook` on desktop and mobile.

5. `[ ]` Rebuild the occupation model around the official NOC 2021 spine.
   Use the 516 unit groups as canonical IDs, adopt the 45 official major groups as the primary dashboard roll-up layer, and keep the current 43-group model only as a temporary compatibility layer.

6. `[ ]` Replace the remaining legacy U.S. detail/profile layer with latest-official OaSIS data.
   Add an importer that resolves the latest official OaSIS version at fetch time and attaches OaSIS profiles to the canonical occupation spine, including one-to-many mappings where OaSIS is more granular.

7. `[ ]` Add family pages for each dashboard occupation group.
   Build dedicated family pages for the dashboard roll-up groups, showing labour-market summary, underlying NOC unit groups, and nested OaSIS occupational profiles.

8. `[ ]` Add global NOC search and deep linking.
   Add one search input that matches major-group codes, unit-group codes, occupational profile codes, titles, and aliases, and route exact hits to the correct family page and focused result.

9. `[ ]` Map the 44 occupations from GDPval onto the dashboard.
   Only ship a direct mapping if the correspondence to the canonical occupation spine is explicit and auditable; otherwise present GDPval in a separate comparison view at its own grain.

10. `[ ]` Add task-level exposure estimates from Eloundou et al. (2023).
   Attach this framework only where a strict auditable crosswalk exists; otherwise keep it in a separate research layer while preserving the original methodological framing.

11. `[ ]` Add a view for academic research overlays.
   Create a dedicated research view for academic measures such as AIOE, task-level exposure, GDPval, and related defensible inputs.

12. `[ ]` Add a view for industry research overlays.
   Create a separate industry research view so private-sector methodologies can be shown alongside, but not conflated with, official or academic measures.

13. `[ ]` Add a benchmark engine at the task-family level.
   Introduce benchmark data keyed to the canonical occupation spine so measured benchmark performance can be stored and compared with clear provenance.

14. `[ ]` Add a NOC + OaSIS workbench/dashboard surface.
   Build a workbench view that can show exposure, measured benchmark performance, occupation similarity, and model recommendations on top of the canonical spine and benchmark engine.

15. `[ ]` Add EN/FR language switching last.
   Implement the bilingual toggle only after the data model, routes, labels, research views, benchmark engine, and workbench surface stabilize.
