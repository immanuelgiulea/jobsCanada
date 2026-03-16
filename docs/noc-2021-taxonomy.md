# NOC 2021 Taxonomy

This repo uses the official NOC 2021 classification structure as its only occupation taxonomy.

## Migration note

- The upstream repo organized occupations around a smaller 43-group dashboard model tied to a U.S.-centric taxonomy and data workflow.
- This fork migrated the project onto the Canadian NOC 2021 classification instead.
- The Canadian taxonomy change replaced that upstream grouping model with the official NOC 2021 hierarchy: 516 canonical unit groups and 45 official major groups.
- The current repo treats the NOC 2021 hierarchy as the only active taxonomy in generated outputs and dashboard payloads.

## Canonical structure

- Broad categories: 10
- Major groups: 45
- Sub-major groups: 89
- Minor groups: 162
- Unit groups: 516

## Primary dashboard layer

- Canonical occupation IDs are the 516 official NOC 2021 unit groups.
- The primary dashboard roll-up layer is the 45 official NOC 2021 major groups.
- Downstream consumers should resolve occupations by canonical NOC code or canonical slug.
- Official OaSIS occupational profiles attach to that canonical spine through an explicit generated mapping table keyed to the unit-group code.

## Methodology note

- StatCan annual labour-force and wage tables are published at a coarser occupation grain than the official unit groups.
- This repo allocates those annual published totals onto the canonical unit groups using ESDC unit employment weights.
- ESDC outlook remains direct at the unit-group level.
- StatCan EPIAC fields are mapped from published StatCan occupation groups onto the canonical NOC 2021 spine.
- OaSIS profiles use the same canonical spine. The generated `oasis_profile_mappings.csv` file records every profile-to-unit-group attachment and preserves one-to-many cases where OaSIS splits a unit group into multiple profiles.
