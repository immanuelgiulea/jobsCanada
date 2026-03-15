"""
Generate prompt.md with Canadian occupation data, outlooks, and official EPIAC exposure fields.

Usage:
    uv run python make_prompt.py
"""

import csv


def fmt_money(value):
    if value is None:
        return "?"
    return f"${value:,.2f}"


def fmt_jobs(value):
    if value is None:
        return "?"
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.0f}K"
    return str(value)


def load_records():
    with open("occupations.csv", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    records = []
    for row in rows:
        records.append(
            {
                "title": row["title"],
                "slug": row["slug"],
                "noc_code": row.get("noc_code", ""),
                "category": row["category"],
                "jobs_year": int(row["data_year"]) if row.get("data_year") else None,
                "trend_from_year": int(row["trend_from_year"]) if row.get("trend_from_year") else None,
                "jobs": int(row["num_jobs"]) if row.get("num_jobs") else None,
                "unemployment_rate": float(row["unemployment_rate"]) if row.get("unemployment_rate") else None,
                "trend_pct": float(row["employment_change_pct"]) if row.get("employment_change_pct") else None,
                "pay_hourly": float(row["median_hourly_wage"]) if row.get("median_hourly_wage") else None,
                "outlook_label": row.get("outlook_label") or None,
                "outlook_window_start": int(row["outlook_window_start"]) if row.get("outlook_window_start") else None,
                "outlook_window_end": int(row["outlook_window_end"]) if row.get("outlook_window_end") else None,
                "epiac_reference_year": int(row["epiac_reference_year"]) if row.get("epiac_reference_year") else None,
                "epiac_display_score": int(row["epiac_display_score"]) if row.get("epiac_display_score") else None,
                "epiac_high_exposure_pct": float(row["epiac_high_exposure_pct"]) if row.get("epiac_high_exposure_pct") else None,
                "epiac_helc_pct": float(row["epiac_helc_pct"]) if row.get("epiac_helc_pct") else None,
                "epiac_hehc_pct": float(row["epiac_hehc_pct"]) if row.get("epiac_hehc_pct") else None,
                "epiac_low_pct": float(row["epiac_low_pct"]) if row.get("epiac_low_pct") else None,
                "epiac_aioe": float(row["epiac_aioe"]) if row.get("epiac_aioe") else None,
                "epiac_complementarity": float(row["epiac_complementarity"]) if row.get("epiac_complementarity") else None,
                "epiac_group_label": row.get("epiac_group_label") or None,
                "epiac_source_note": row.get("epiac_source_note") or "",
            }
        )
    return records


def main():
    records = load_records()
    records.sort(key=lambda item: (-(item["epiac_high_exposure_pct"] or 0), -(item["jobs"] or 0)))

    jobs_year = max(record["jobs_year"] for record in records if record["jobs_year"] is not None)
    trend_from_year = min(record["trend_from_year"] for record in records if record["trend_from_year"] is not None)
    outlook_start = max(record["outlook_window_start"] for record in records if record["outlook_window_start"] is not None)
    outlook_end = max(record["outlook_window_end"] for record in records if record["outlook_window_end"] is not None)
    exposure_year = max(record["epiac_reference_year"] for record in records if record["epiac_reference_year"] is not None)
    total_jobs = sum(record["jobs"] or 0 for record in records)

    weighted_high_share = sum((record["epiac_high_exposure_pct"] or 0) * (record["jobs"] or 0) for record in records if record["jobs"]) / total_jobs
    weighted_aioe = sum((record["epiac_aioe"] or 0) * (record["jobs"] or 0) for record in records if record["jobs"]) / total_jobs
    weighted_comp = sum((record["epiac_complementarity"] or 0) * (record["jobs"] or 0) for record in records if record["jobs"]) / total_jobs
    helc_workers = sum((record["jobs"] or 0) * (record["epiac_helc_pct"] or 0) / 100 for record in records)
    hehc_workers = sum((record["jobs"] or 0) * (record["epiac_hehc_pct"] or 0) / 100 for record in records)
    low_workers = sum((record["jobs"] or 0) * (record["epiac_low_pct"] or 0) / 100 for record in records)

    lines = [
        "# AI Exposure of the Canadian Job Market",
        "",
        f"This document contains Statistics Canada occupation-group data for Canada. Employment and wages use annual tables through {jobs_year}, outlook uses province-aggregated ESDC data for {outlook_start}-{outlook_end}, and AI exposure uses StatCan's official EPIAC framework mapped from the {exposure_year} Census-based study.",
        "",
        "Sources:",
        "- https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041601",
        "- https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041701",
        "- https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm",
        "- https://open.canada.ca/data/en/dataset/b0e112e9-cf53-4e79-8838-23cd98debe5b/resource/cb52e1d0-ab62-4357-91cc-d8f5a2114e02",
        "- https://www150.statcan.gc.ca/n1/en/pub/36-28-0001/2026001/article/00001-eng.pdf",
        "- https://statistique.quebec.ca/fr/fichier/exposition-professions-intelligence-artificielle-2024.pdf",
        "",
        "## Aggregate statistics",
        "",
        f"- Occupation groups: {len(records)}",
        f"- Total workers ({jobs_year}): {total_jobs:,} ({total_jobs / 1_000_000:.1f}M)",
        f"- Job-weighted EPIAC high-exposure share: {weighted_high_share:.1f}%",
        f"- Job-weighted AIOE: {weighted_aioe:.2f}",
        f"- Job-weighted complementarity: {weighted_comp:.2f}",
        f"- Estimated workers in HELC occupations: {fmt_jobs(round(helc_workers))}",
        f"- Estimated workers in HEHC occupations: {fmt_jobs(round(hehc_workers))}",
        f"- Estimated workers in low-exposure occupations: {fmt_jobs(round(low_workers))}",
        f"- Trend window: {trend_from_year} to {jobs_year}",
        f"- Outlook window: {outlook_start} to {outlook_end}",
        "",
        "## Exposure mix by EPIAC group",
        "",
        "| Group | Estimated workers | % of workers |",
        "|-------|-------------------|--------------|",
        f"| HELC | {fmt_jobs(round(helc_workers))} | {helc_workers / total_jobs * 100:.1f}% |",
        f"| HEHC | {fmt_jobs(round(hehc_workers))} | {hehc_workers / total_jobs * 100:.1f}% |",
        f"| Low exposure | {fmt_jobs(round(low_workers))} | {low_workers / total_jobs * 100:.1f}% |",
        "",
        f"## Occupations with the highest EPIAC high-exposure share ({exposure_year} mapping)",
        "",
        "| Occupation group | High-exposure share | Dominant EPIAC group | AIOE | Complementarity | Outlook | Workers |",
        "|------------------|---------------------|----------------------|------|-----------------|---------|---------|",
    ]

    for record in records[:12]:
        lines.append(
            f"| {record['title']} | {record['epiac_high_exposure_pct']:.1f}% | {record['epiac_group_label'] or '?'} | {record['epiac_aioe']:.2f} | {record['epiac_complementarity']:.2f} | {record['outlook_label'] or '?'} | {fmt_jobs(record['jobs'])} |"
        )

    growers = [record for record in records if record["trend_pct"] is not None]
    growers.sort(key=lambda item: item["trend_pct"], reverse=True)
    lines.extend(
        [
            "",
            f"## Biggest growers since {trend_from_year}",
            "",
            "| Occupation group | High-exposure share | Dominant EPIAC group | Employment change | Workers | Median hourly wage |",
            "|------------------|---------------------|----------------------|-------------------|---------|--------------------|",
        ]
    )
    for record in growers[:10]:
        lines.append(
            f"| {record['title']} | {record['epiac_high_exposure_pct']:.1f}% | {record['epiac_group_label'] or '?'} | {record['trend_pct']:+.1f}% | {fmt_jobs(record['jobs'])} | {fmt_money(record['pay_hourly'])} |"
        )

    lines.extend(["", f"## All {len(records)} occupation groups", ""])
    for record in records:
        source_note = record["epiac_source_note"].replace("|", "/")
        change = f"{record['trend_pct']:+.1f}%" if record["trend_pct"] is not None else "?"
        unemployment = f"{record['unemployment_rate']:.1f}%" if record["unemployment_rate"] is not None else "?"
        lines.append(f"### {record['title']}")
        lines.append("")
        lines.append("| Field | Value |")
        lines.append("|-------|-------|")
        lines.append(f"| NOC | {record['noc_code']} |")
        lines.append(f"| Category | {record['category']} |")
        lines.append(f"| Workers | {fmt_jobs(record['jobs'])} |")
        lines.append(f"| High-exposure share | {record['epiac_high_exposure_pct']:.1f}% |")
        lines.append(f"| Dominant EPIAC group | {record['epiac_group_label'] or '?'} |")
        lines.append(f"| AIOE | {record['epiac_aioe']:.2f} |")
        lines.append(f"| Complementarity | {record['epiac_complementarity']:.2f} |")
        lines.append(f"| HELC / HEHC / Low | {record['epiac_helc_pct']:.1f}% / {record['epiac_hehc_pct']:.1f}% / {record['epiac_low_pct']:.1f}% |")
        lines.append(f"| Employment change | {change} |")
        lines.append(f"| Unemployment | {unemployment} |")
        lines.append(f"| Median hourly wage | {fmt_money(record['pay_hourly'])} |")
        lines.append(f"| Outlook | {record['outlook_label'] or '?'} |")
        lines.append(f"| Mapping note | {source_note} |")
        lines.append("")

    with open("prompt.md", "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")

    print(f"Wrote prompt.md with {len(records)} occupation groups")


if __name__ == "__main__":
    main()
