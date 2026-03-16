# NOC 2021 Taxonomy

This repo uses the official NOC 2021 classification structure as its only occupation taxonomy.

## Active scope

- The official NOC 2021 hierarchy is the only active taxonomy in generated outputs and dashboard payloads.
- Canonical occupation IDs are the 516 official unit groups.
- The primary dashboard roll-up layer is the 45 official major groups.
- Official OaSIS occupational profiles attach to that canonical spine through an explicit generated mapping table keyed to unit-group code.

## Canonical structure

- Broad categories: 10
- Major groups: 45
- Sub-major groups: 89
- Minor groups: 162
- Unit groups: 516

## Primary dashboard layer

- Downstream consumers should resolve occupations by canonical NOC code or canonical slug.

## Methodology note

- StatCan annual labour-force and wage tables are published at a coarser occupation grain than the official unit groups.
- This repo allocates those annual published totals onto the canonical unit groups using ESDC unit employment weights.
- ESDC outlook remains direct at the unit-group level.
- StatCan EPIAC fields are mapped from published StatCan occupation groups onto the canonical NOC 2021 spine.
- OaSIS profiles use the same canonical spine. The generated `oasis_profile_mappings.csv` file records every profile-to-unit-group attachment and preserves one-to-many cases where OaSIS splits a unit group into multiple profiles.
