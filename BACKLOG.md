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
