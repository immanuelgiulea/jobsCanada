# Backlog

## Provincial dashboard + OaSIS drill-down

1. Add full geography mode to the current 43-group dashboard.
   Use `Canada` plus all 13 provinces and territories as selector values, and extend the StatCan ingest so each dashboard group has geography-specific jobs, trend, unemployment, employment share, paid employees, men/women share, and median hourly/weekly wage. Keep Canada as the default view. Keep EPIAC exposure as official mapped national metadata, but recompute weighted aggregates using the selected geography's employment counts. Use province-specific ESDC outlooks instead of the current Canada-only aggregation when a geography is selected.

2. Replace the remaining legacy U.S. detail/profile layer with latest-official OaSIS data.
   Add an importer that discovers the latest official OaSIS version at fetch time, records the resolved version in generated metadata, and maps OaSIS unit groups and occupational profiles onto the existing 43 dashboard groups. Capture full profile content exposed by OaSIS for each profile, including codes, titles, aliases, lead statements, main duties, core competencies, descriptor sections, source URLs, and version metadata.

3. Add family pages for each dashboard occupation group.
   Clicking a dashboard group should open a dedicated family page for that group and the selected geography. The page should show the group's geography-specific labour-market summary, the matching NOC unit groups, and the nested OaSIS occupational profiles inside that family. Preserve old `occupation.html?slug=...` links by redirecting them to the new family page.

4. Add global NOC search and deep linking.
   Add one search input that matches dashboard group codes, unit-group codes, occupational profile codes, titles, and aliases. Exact code hits should open the correct family page and focus the matching unit group or profile. Build a compact search index rather than pushing full OaSIS profile payloads into the main dashboard JSON.

5. Map the 44 occupations from GDPval onto the dashboard.
   Investigate whether GDPval can be defensibly mapped onto the current 43 dashboard groups or whether it should be presented in a separate comparison view with its own occupation grain and methodology note. Do not force a one-to-one mapping unless the correspondence is explicit and auditable.

6. Add task-level exposure estimates from Eloundou et al. (2023).
   Evaluate whether the paper's task-speedup framework should be attached to OaSIS tasks/profiles or shown as a separate research layer. Preserve the original methodological framing that the estimate is about whether an LLM could theoretically make a task at least twice as fast.

7. Add a view for academic research overlays.
   Create a dedicated research view that can compare or summarize academic measures such as AIOE, task-level exposure, and other defensible research inputs without overloading the main dashboard view.

8. Add a view for industry research overlays.
   Create a separate industry research view so private-sector methodologies can be shown alongside, but not conflated with, the official StatCan/ESDC pipeline and academic measures.

9. Add EN/FR language switching last.
   Implement the bilingual toggle only after the data model, routes, labels, and research views stabilize. The language switch should cover dashboard copy, family/profile pages, navigation, search labels, and research-view text without blocking the higher-priority data and view work above.
