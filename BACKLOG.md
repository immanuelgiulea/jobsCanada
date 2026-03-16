# Backlog

## Dashboard hardening + canonical NOC / OaSIS architecture

Conventions:
- One backlog item = one implementation thread.
- Items 3-4 are bug/task-sized follow-ups.
- Items 5-16 are epics.
- Every open item includes `Done when:` criteria.

1. `[x]` Add full geography mode to the current dashboard.
   Implemented. The repo now emits `stats_by_geo`, ships geography metadata with `CA` plus all provinces and territories, exposes a geography selector in the dashboard, and switches labour-market metrics and ESDC outlooks by geography while keeping EPIAC national and reweighted by local employment counts.

2. `[x]` Validate the canonical taxonomy against the official NOC 2021 hierarchy.
   Implemented. The repo now reproduces the official 10/45/89/162/516 hierarchy locally, exposes that hierarchy metadata in `site/data.json`, and keeps the dashboard roll-ups aligned to the official structure.

3. `[x]` Bug: Fix Canada outlook mix semantics and expose provincial dispersion.
   Implemented. The Canada view now separates the Canada-wide aggregate outlook mix from a province-dispersion summary computed from province labels, keeps province-only buckets such as `Very limited` and `Undetermined` visible nationally, and was validated against the generated Canada and Quebec source data.

4. `[x]` Bug: Fix tooltip mapping-note rendering in alternate views.
   Implemented. The shared dashboard tooltip now normalizes mapping-note sentence spacing, renders multi-sentence notes as readable paragraphs, and constrains wrapping/height so long and weighted-blend notes stay legible without clipping in treemap, `Exposure vs Change`, and `Exposure vs Outlook` on desktop and mobile.

5. `[x]` Epic: Rebuild the occupation model around the official NOC 2021 spine.
   Implemented. The repo now treats the official 516 NOC 2021 unit groups as canonical occupation IDs, exposes the 45 official major groups as the primary dashboard roll-up layer, and lets downstream consumers resolve occupations by canonical unit-group codes or slugs from `occupations.csv`, `occupations.json`, and `site/data.json`.

6. `[x]` Epic: Replace the remaining legacy U.S. detail/profile layer with latest-official OaSIS data.
   Implemented. `fetch_statcan.py` now resolves the latest official OaSIS package from the Open Canada CKAN API at fetch time, caches the English CSV release under `tmp/oasis/`, writes generated `oasis.json` and `oasis_profile_mappings.csv` artifacts with resolved version/source/fetch metadata, and attaches all 900 OaSIS occupational profiles to the canonical 516-unit-group spine through an explicit mapping table. One-to-many mappings are preserved on the canonical rows, in `site/data.json`, and in the generated markdown pages, while unmapped or ambiguous profiles are surfaced in the OaSIS audit report instead of being dropped.

7. `[ ]` Epic: Remove all remaining U.S.-only product remnants after the OaSIS migration.
   After item 6, the runtime product, build pipeline, generated artifacts, and user-facing copy should be fully Canadian. Any remaining U.S.-only material should either be deleted or quarantined as clearly non-functional archival history.
   Done when:
   - No active build step, generated artifact, route, or UI surface depends on U.S.-only sources such as BLS or O*NET.
   - No user-facing copy, links, labels, tooltips, or documentation in the shipped product references U.S.-only sources or terminology.
   - Any leftover U.S.-only files are either removed or moved to a clearly marked non-product archival location that is not used by the build.
   - The runtime product and build pipeline can be described as fully Canadian without caveats.

8. `[ ]` Epic: Add family pages for each official major group.
   Build dedicated major-group pages showing the selected geography's labour-market summary plus the underlying NOC unit groups and nested OaSIS occupational profiles. Preserve existing `occupation.html?slug=...` links by redirecting them to the new family page where appropriate.
   Done when:
   - Every official major group has a dedicated family page route.
   - Each family page shows geography-specific summary metrics, underlying unit groups, and nested OaSIS profiles.
   - Existing `occupation.html?slug=...` links redirect successfully to the new family page.
   - Family pages are usable on both desktop and mobile layouts.

9. `[ ]` Epic: Add global NOC search and deep linking.
   Add one search input that matches major-group codes, unit-group codes, occupational profile codes, titles, and aliases. Exact code hits should open the correct family page and focus the matching unit group or profile. Build a compact search index rather than pushing full OaSIS profile payloads into the main dashboard JSON.
   Done when:
   - Search indexes major-group codes, unit-group codes, OaSIS profile codes, titles, and aliases.
   - Exact code hits deep-link to the correct page and focused result.
   - Ambiguous text searches return grouped suggestions without breaking navigation state.
   - Search is driven by a generated compact index rather than full page payloads.

10. `[ ]` Epic: Map the 44 occupations from GDPval onto the dashboard.
   Investigate whether GDPval can be defensibly mapped onto the canonical occupation spine or whether it should be presented in a separate comparison view with its own occupation grain and methodology note. Do not force a one-to-one mapping unless the correspondence is explicit and auditable.
   Done when:
   - The GDPval occupation grain and code system are documented in the repo.
   - Any mapping to the canonical spine cites an explicit and auditable crosswalk or method note.
   - Unmapped GDPval records remain available in a source-grain comparison view instead of being discarded.
   - GDPval never overwrites official StatCan/ESDC fields.

11. `[ ]` Epic: Add task-level exposure estimates from Eloundou et al. (2023).
   Evaluate whether the paper's task-speedup framework can be attached to OaSIS tasks, descriptors, or unit groups with a strict auditable crosswalk. Otherwise keep it in a separate research layer at its native grain. Preserve the original methodological framing that the estimate is about whether an LLM could theoretically make a task at least twice as fast.
   Done when:
   - The source methodology, task grain, and citation are captured in generated metadata.
   - Any mapping to OaSIS or canonical NOC IDs is explicit, auditable, and versioned.
   - If no strict crosswalk exists, the dataset is exposed at its native grain in a separate research layer.
   - The UI preserves the original task-speedup framing and does not relabel it as official exposure.

12. `[ ]` Epic: Add a view for academic research overlays.
   Create a dedicated research view that can compare or summarize academic measures such as AIOE, task-level exposure, GDPval, and other defensible research inputs without overloading the main dashboard view.
   Done when:
   - A dedicated academic research route exists and is reachable from the main navigation.
   - The route can show multiple academic datasets with source, year, grain, and methodology notes.
   - Incompatible datasets stay visibly separate instead of being blended into a single composite score.
   - The academic research view does not change the main dashboard ranking or coloring rules.

13. `[ ]` Epic: Add a view for industry research overlays.
   Create a separate industry research view so private-sector methodologies can be shown alongside, but not conflated with, the official StatCan/ESDC pipeline and academic measures.
   Done when:
   - A dedicated industry research route exists and is reachable from the main navigation.
   - Each dataset shows publisher, date, methodology note, source link, and mapping status.
   - Industry layers remain visually and textually distinct from official and academic measures.
   - Unmapped industry datasets can still be displayed at source grain.

14. `[ ]` Epic: Add a benchmark engine at the task-family level.
   Introduce a benchmark data model keyed to the canonical occupation spine so task-family benchmarking, measured benchmark performance, and model evaluation can be stored with clear provenance.
   Done when:
   - Benchmark definitions, runs, and results are stored against stable canonical occupation/task-family IDs.
   - Each benchmark result records model, version, date, prompt/config provenance, and scoring method.
   - Benchmark data can be queried by occupation, task family, and model without bespoke one-off transforms.
   - The engine supports later dashboard/workbench consumption without redesigning the schema.

15. `[ ]` Epic: Add a NOC + OaSIS workbench/dashboard surface.
   Build a workbench view that sits on top of the canonical occupation spine and benchmark engine and can show exposure, measured benchmark performance, occupation similarity, and model recommendations.
   Done when:
   - A dedicated workbench route exists on top of the canonical occupation spine.
   - The workbench can show exposure, measured benchmark performance, occupation similarity, and model recommendations in one workflow.
   - Workbench results can drill from roll-up groups to unit groups and linked OaSIS profiles.
   - The workbench runs directly on the canonical NOC 2021 spine without secondary taxonomy adapters.

16. `[ ]` Epic: Add EN/FR language switching last.
   Implement the bilingual toggle only after the data model, routes, labels, research views, benchmark engine, and workbench surface stabilize. The language switch should cover dashboard copy, family/profile pages, navigation, search labels, workbench text, and research-view text.
   Done when:
   - The app supports a stable EN/FR toggle that persists across routes and deep links.
   - Dashboard, family pages, search UI, research views, and workbench chrome all localize correctly.
   - Generated metadata supports bilingual labels where source material exists in both languages.
   - Missing French source text falls back gracefully without breaking page structure or navigation.
