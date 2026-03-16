"""
Build website data by merging StatCan occupation stats with official EPIAC exposure data.

Reads occupations.csv.
Writes site/data.json.

Usage:
    uv run python build_site_data.py
"""

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

from dashboard_noc_audit import build_dashboard_noc_audit
from geography import DEFAULT_GEO_CODE, GEO_METADATA


SITE_DIR = Path("site")
OUTPUT_PATH = SITE_DIR / "data.json"

STATCAN_EMPLOYMENT_URL = "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041601"
STATCAN_WAGES_URL = "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041701"
STATCAN_EPIAC_URL = "https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm"
STATCAN_EPIAC_TITLE = "Experimental Estimates of Potential Artificial Intelligence Occupational Exposure in Canada, 2024"
STATCAN_EPIAC_CONTEXT_URL = "https://www150.statcan.gc.ca/n1/en/pub/36-28-0001/2026001/article/00001-eng.pdf"
STATCAN_EPIAC_CONTEXT_FR_URL = "https://www150.statcan.gc.ca/n1/fr/pub/36-28-0001/2026001/article/00001-fra.pdf"
ISQ_EPIAC_URL = "https://statistique.quebec.ca/fr/fichier/exposition-professions-intelligence-artificielle-2024.pdf"


def as_int(value):
    return int(value) if value not in (None, "") else None


def as_float(value):
    return float(value) if value not in (None, "") else None


def parse_stats_by_geo(value):
    raw = json.loads(value) if value else {}
    parsed = {}
    for geo in GEO_METADATA:
        stats = raw.get(geo["code"], {})
        parsed[geo["code"]] = {
            "jobs": as_int(stats.get("jobs")),
            "jobs_year": as_int(stats.get("jobs_year")),
            "trend_pct": as_float(stats.get("trend_pct")),
            "trend_from_year": as_int(stats.get("trend_from_year")),
            "unemployment_rate": as_float(stats.get("unemployment_rate")),
            "employment_share_pct": as_float(stats.get("employment_share_pct")),
            "men_share_pct": as_float(stats.get("men_share_pct")),
            "women_share_pct": as_float(stats.get("women_share_pct")),
            "employees": as_int(stats.get("employees")),
            "pay_hourly": as_float(stats.get("pay_hourly")),
            "pay_weekly": as_float(stats.get("pay_weekly")),
            "outlook_label": stats.get("outlook_label") or None,
            "outlook_score": as_float(stats.get("outlook_score")),
            "outlook_window_start": as_int(stats.get("outlook_window_start")),
            "outlook_window_end": as_int(stats.get("outlook_window_end")),
            "outlook_release_date": stats.get("outlook_release_date") or None,
        }
    return parsed


def main():
    with Path("occupations.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        raise ValueError("occupations.csv is empty")

    jobs_year = max(int(row["data_year"]) for row in rows if row.get("data_year"))
    trend_from_year = min(int(row["trend_from_year"]) for row in rows if row.get("trend_from_year"))
    outlook_start = max(int(row["outlook_window_start"]) for row in rows if row.get("outlook_window_start"))
    outlook_end = max(int(row["outlook_window_end"]) for row in rows if row.get("outlook_window_end"))
    outlook_release_date = max((row["outlook_release_date"] for row in rows if row.get("outlook_release_date")), default="")
    outlook_url = next((row["outlook_source_url"] for row in rows if row.get("outlook_source_url")), "")
    epiac_reference_year = max(int(row["epiac_reference_year"]) for row in rows if row.get("epiac_reference_year"))
    epiac_source_url = next((row["epiac_source_url"] for row in rows if row.get("epiac_source_url")), STATCAN_EPIAC_URL)
    epiac_source_title = next((row["epiac_source_title"] for row in rows if row.get("epiac_source_title")), STATCAN_EPIAC_TITLE)
    dashboard_audit = build_dashboard_noc_audit()
    audit_groups_by_code = {
        item["dashboard_group_code"]: item for item in dashboard_audit["dashboard"]["groups"]
    }

    occupations = []
    for row in rows:
        group_audit = audit_groups_by_code[row["noc_code"]]
        occupations.append(
            {
                "title": row["title"],
                "slug": row["slug"],
                "category": row["category"],
                "dashboard_family_code": group_audit["dashboard_family_variant_section_code"],
                "noc_code": row["noc_code"],
                "dashboard_mapping_kind": group_audit["mapping_kind"],
                "dashboard_mapping_kind_label": group_audit["mapping_kind_label"],
                "official_broad_category_codes": group_audit["official_broad_category_codes"],
                "official_broad_category_labels": group_audit["official_broad_category_titles"],
                "official_major_group_count": group_audit["official_major_group_count"],
                "official_sub_major_group_count": group_audit["official_sub_major_group_count"],
                "official_minor_group_count": group_audit["official_minor_group_count"],
                "official_unit_group_count": group_audit["official_unit_group_count"],
                "jobs": as_int(row["num_jobs"]),
                "jobs_year": as_int(row["data_year"]),
                "trend_pct": as_float(row["employment_change_pct"]),
                "trend_from_year": as_int(row["trend_from_year"]),
                "unemployment_rate": as_float(row["unemployment_rate"]),
                "employment_share_pct": as_float(row["employment_share_pct"]),
                "men_share_pct": as_float(row["men_share_pct"]),
                "women_share_pct": as_float(row["women_share_pct"]),
                "pay_hourly": as_float(row["median_hourly_wage"]),
                "pay_weekly": as_float(row["median_weekly_wage"]),
                "employees": as_int(row["num_employees"]),
                "outlook_label": row.get("outlook_label", "") or None,
                "outlook_score": as_float(row.get("outlook_score", "")),
                "outlook_window_start": as_int(row.get("outlook_window_start", "")),
                "outlook_window_end": as_int(row.get("outlook_window_end", "")),
                "outlook_release_date": row.get("outlook_release_date", "") or None,
                "exposure": as_int(row.get("epiac_display_score", "")),
                "exposure_metric": "high_exposure_share",
                "exposure_rationale": row.get("epiac_source_note", "") or None,
                "epiac_reference_year": as_int(row.get("epiac_reference_year", "")),
                "epiac_high_exposure_pct": as_float(row.get("epiac_high_exposure_pct", "")),
                "epiac_helc_pct": as_float(row.get("epiac_helc_pct", "")),
                "epiac_hehc_pct": as_float(row.get("epiac_hehc_pct", "")),
                "epiac_low_pct": as_float(row.get("epiac_low_pct", "")),
                "epiac_aioe": as_float(row.get("epiac_aioe", "")),
                "epiac_complementarity": as_float(row.get("epiac_complementarity", "")),
                "epiac_caioe": as_float(row.get("epiac_caioe", "")),
                "epiac_group_code": row.get("epiac_group_code", "") or None,
                "epiac_group_label": row.get("epiac_group_label", "") or None,
                "epiac_source_title": row.get("epiac_source_title", "") or None,
                "epiac_source_url": row.get("epiac_source_url", "") or None,
                "epiac_source_groups": [part.strip() for part in row.get("epiac_source_groups", "").split(";") if part.strip()],
                "url": row.get("url", ""),
                "employment_url": row.get("employment_url", ""),
                "wages_url": row.get("wages_url", ""),
                "outlook_url": row.get("outlook_source_url", ""),
                "stats_by_geo": parse_stats_by_geo(row.get("stats_by_geo_json", "")),
            }
        )

    occupations.sort(key=lambda item: (item["category"], -(item["jobs"] or 0), item["title"]))

    payload = {
        "meta": {
            "title": "AI Exposure of the Canadian Job Market",
            "geography": "Canada",
            "default_geography": DEFAULT_GEO_CODE,
            "geographies": GEO_METADATA,
            "occupation_count": len(occupations),
            "dashboard_family_count": dashboard_audit["dashboard"]["dashboard_family_count"],
            "jobs_year": jobs_year,
            "trend_from_year": trend_from_year,
            "outlook_window_start": outlook_start,
            "outlook_window_end": outlook_end,
            "outlook_release_date": outlook_release_date or None,
            "official_noc_2021_hierarchy": dashboard_audit["official_hierarchy"],
            "dashboard_hierarchy": {
                key: value
                for key, value in dashboard_audit["dashboard"].items()
                if key != "groups"
            },
            "exposure_reference_year": epiac_reference_year,
            "exposure_metric": "StatCan EPIAC high-exposure share",
            "exposure_metric_scale": "0-10 display score derived from the share of workers in high-exposure EPIAC occupations",
            "exposure_note": "Official exposure fields come from StatCan's 2024 EPIAC study based on the 2021 Census and are mapped to the current NOC 2021 occupation groups used in this dashboard.",
            "source": "Statistics Canada annual occupation tables with StatCan EPIAC study mapping",
            "source_tables": [
                {
                    "name": "14-10-0416-01 Labour force characteristics by occupation, annual",
                    "url": STATCAN_EMPLOYMENT_URL,
                },
                {
                    "name": "14-10-0417-01 Employee wages by occupation, annual",
                    "url": STATCAN_WAGES_URL,
                },
                {
                    "name": epiac_source_title,
                    "url": epiac_source_url,
                },
                {
                    "name": "2025-2027 Employment Outlooks - NOC 2021",
                    "url": outlook_url,
                },
            ],
            "research_sources": [
                {
                    "name": "StatCan: Employment growth in Canada since the beginning of the generative AI era",
                    "url": STATCAN_EPIAC_CONTEXT_URL,
                },
                {
                    "name": "StatCan: Croissance de l'emploi au Canada depuis le debut de l'ere de l'IA generative",
                    "url": STATCAN_EPIAC_CONTEXT_FR_URL,
                },
                {
                    "name": "ISQ: Exposition des professions a l'intelligence artificielle en 2024",
                    "url": ISQ_EPIAC_URL,
                },
            ],
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        },
        "occupations": occupations,
    }

    SITE_DIR.mkdir(exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle)

    total_jobs = sum(item["jobs"] for item in occupations if item["jobs"])
    print(f"Wrote {len(occupations)} occupation groups to {OUTPUT_PATH}")
    print(f"Total workers represented ({jobs_year}): {total_jobs:,}")


if __name__ == "__main__":
    main()
