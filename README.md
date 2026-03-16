# AI Exposure of the Canadian Job Market

Analyzing how exposed Canadian occupation groups are to AI using official Statistics Canada and ESDC sources instead of the U.S. Bureau of Labor Statistics.

## What's here

This fork now combines three Canadian data sources:

- [14-10-0416-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041601) Labour force characteristics by occupation, annual
- [14-10-0417-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041701) Employee wages by occupation, annual
- [2025-2027 Employment Outlooks - NOC 2021](https://open.canada.ca/data/en/dataset/b0e112e9-cf53-4e79-8838-23cd98debe5b/resource/cb52e1d0-ab62-4357-91cc-d8f5a2114e02)

AI exposure is no longer driven by an LLM score in the site build. The dashboard now uses official StatCan EPIAC data from:

- [Experimental Estimates of Potential Artificial Intelligence Occupational Exposure in Canada, 2024](https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm)

That study reports AIOE, complementarity, and HELC/HEHC/low-exposure splits for published occupation groups based on the **2021 Census**. This repo uses the official **516 NOC 2021 unit groups** as the canonical occupation IDs, rolls them up through the official **45 major groups**, allocates annual labour metrics from the published StatCan occupation tables, and maps official EPIAC fields onto the canonical spine.

Context studies using the same framework:

- [StatCan, January 28, 2026: employment growth since the start of the generative AI era](https://www150.statcan.gc.ca/n1/en/pub/36-28-0001/2026001/article/00001-eng.pdf)
- [ISQ, February 3, 2026: Exposition des professions a l'intelligence artificielle en 2024](https://statistique.quebec.ca/fr/fichier/exposition-professions-intelligence-artificielle-2024.pdf)

## Data pipeline

1. `fetch_statcan.py`
   Downloads the StatCan occupation tables, allocates those annual labour metrics onto the canonical 516 NOC 2021 unit groups using ESDC unit employment weights, and writes the canonical occupation outputs.
2. `build_site_data.py`
   Builds `site/data.json` for the frontend from the canonical unit-group layer and the official 45 major-group rollups.
3. `make_prompt.py`
   Builds `prompt.md`, a single markdown summary of the Canadian dataset with official EPIAC fields.
4. `site/index.html`
   Interactive visualization where area = Canadian employment and color = EPIAC high-exposure share.

## Key files

| File | Description |
|------|-------------|
| `occupations.json` | Canonical NOC 2021 unit-group index with NOC codes and major-group metadata |
| `occupations.csv` | Canonical 516-unit-group labour, outlook, and EPIAC fields |
| `prompt.md` | Single-file markdown summary of the Canadian dataset |
| `docs/noc-2021-taxonomy.md` | Canonical taxonomy and methodology note for the official NOC 2021 spine |
| `pages/` | Generated occupation summaries and source notes |
| `site/` | Static website |
| `epiac_data.py` | Official EPIAC source rows and mapping logic |
| `outlook_data.py` | ESDC outlook ingestion and aggregation logic |
| `score.py` | Optional legacy LLM scoring script, not used by the site build |

## Important differences from upstream

- Source data is **Canadian** and based on **StatCan / ESDC**, not BLS handbook pages.
- The upstream repo used a smaller **43-group** dashboard model tied to a U.S.-oriented taxonomy; this fork migrated to the Canadian **NOC 2021** hierarchy with **45 official major groups** and **516 canonical unit groups**.
- Exposure is based on **official StatCan EPIAC / AIOE / complementarity** data, not only an LLM judgment.
- The dashboard mixes different reference periods intentionally:
  - exposure: mapped from the StatCan 2024 EPIAC study using **2021 Census** occupation data
  - employment and wages: latest StatCan annual tables through **2025**
  - outlook: province-aggregated ESDC outlook data for **2025-2027**
- The dataset uses the official **516 Canadian NOC 2021 unit groups** as canonical IDs and the official **45 major groups** as the primary dashboard roll-up.

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
- The EPIAC mapping is an inference from the closest published StatCan occupation groups to the canonical NOC 2021 spine. Each generated row and page includes a mapping note.

## Backlog

See [BACKLOG.md](BACKLOG.md) for the current implementation backlog.
