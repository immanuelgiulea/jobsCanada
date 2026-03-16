# Backlog

## Dashboard hardening + canonical NOC / OaSIS architecture

1. `[x]` Add full geography mode to the current 43-group dashboard.
   Implemented. The repo now emits `stats_by_geo`, ships geography metadata with `CA` plus all provinces and territories, exposes a geography selector in the dashboard, and switches labour-market metrics and ESDC outlooks by geography while keeping EPIAC national and reweighted by local employment counts.

2. `[x]` Validate the dashboard-to-NOC mapping against the official NOC 2021 hierarchy.
   Implemented. The repo now ships a reproducible dashboard-to-NOC audit, documents the 43-group concordance against the official 10/45/89/162/516 hierarchy in `docs/dashboard-to-noc-2021.md`, exposes the hierarchy metadata in `site/data.json`, and keeps small treemap families such as Resources visibly labelled instead of hiding the header.

3. `[ ]` Fix Canada outlook mix semantics and expose provincial dispersion.
   The Canada view currently hides labels such as `Very limited` and `Undetermined` that appear in provincial views like Quebec. Keep the Canada-wide aggregate outlook logic, but also surface provincial bucket dispersion nationally so province-only labels remain visible and explainable.

4. `[ ]` Fix tooltip mapping-note rendering in alternate views.
   In `Exposure vs Change` and `Exposure vs Outlook`, make the tooltip's mapping note legible with proper spacing, punctuation, and wrapping so the second sentence does not run into the first.

5. `[ ]` Rebuild the occupation model around the official NOC 2021 spine.
   Use the 516 NOC 2021 unit groups as the canonical occupation IDs. Adopt the 45 official major groups as the primary roll-up/dashboard layer, and keep the current 43-group dashboard only as a temporary compatibility concordance during migration.

6. `[ ]` Replace the remaining legacy U.S. detail/profile layer with latest-official OaSIS data.
   Add an importer that discovers the latest official OaSIS version at fetch time, records the resolved version in generated metadata, and attaches OaSIS unit groups and occupational profiles to the canonical 516-unit-group spine. Support one-to-many mappings where OaSIS is more granular than a unit group.

7. `[ ]` Add family pages for each dashboard occupation group.
   Build dedicated family pages for the dashboard roll-up groups, showing the selected geography's labour-market summary plus the underlying NOC unit groups and nested OaSIS occupational profiles. Preserve old `occupation.html?slug=...` links by redirecting them to the new family page.

8. `[ ]` Add global NOC search and deep linking.
   Add one search input that matches major-group codes, unit-group codes, occupational profile codes, titles, and aliases. Exact code hits should open the correct family page and focus the matching unit group or profile. Build a compact search index rather than pushing full OaSIS profile payloads into the main dashboard JSON.

9. `[ ]` Map the 44 occupations from GDPval onto the dashboard.
   Investigate whether GDPval can be defensibly mapped onto the canonical occupation spine or whether it should be presented in a separate comparison view with its own occupation grain and methodology note. Do not force a one-to-one mapping unless the correspondence is explicit and auditable.

10. `[ ]` Add task-level exposure estimates from Eloundou et al. (2023).
   Evaluate whether the paper's task-speedup framework can be attached to OaSIS tasks, descriptors, or unit groups with a strict auditable crosswalk. Otherwise keep it in a separate research layer at its native grain. Preserve the original methodological framing that the estimate is about whether an LLM could theoretically make a task at least twice as fast.

11. `[ ]` Add a view for academic research overlays.
   Create a dedicated research view that can compare or summarize academic measures such as AIOE, task-level exposure, GDPval, and other defensible research inputs without overloading the main dashboard view.

12. `[ ]` Add a view for industry research overlays.
   Create a separate industry research view so private-sector methodologies can be shown alongside, but not conflated with, the official StatCan/ESDC pipeline and academic measures.

13. `[ ]` Add a benchmark engine at the task-family level.
   Introduce a benchmark data model keyed to the canonical occupation spine so task-family benchmarking, measured benchmark performance, and model evaluation can be stored with clear provenance.

14. `[ ]` Add a NOC + OaSIS workbench/dashboard surface.
   Build a workbench view that sits on top of the canonical occupation spine and benchmark engine and can show exposure, measured benchmark performance, occupation similarity, and model recommendations.

15. `[ ]` Add EN/FR language switching last.
   Implement the bilingual toggle only after the data model, routes, labels, research views, benchmark engine, and workbench surface stabilize. The language switch should cover dashboard copy, family/profile pages, navigation, search labels, workbench text, and research-view text.
