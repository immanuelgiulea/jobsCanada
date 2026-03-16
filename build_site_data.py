"""
Build website data from canonical NOC 2021 records.

Reads:
- occupations.csv (canonical 516 unit groups)

Writes:
- site/data.json
"""

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

from geography import DEFAULT_GEO_CODE, GEO_METADATA
from noc_hierarchy import load_official_noc_structure
from outlook_data import label_from_score


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
            "employment_change_abs": as_int(stats.get("employment_change_abs")),
            "unemployment_rate": as_float(stats.get("unemployment_rate")),
            "employment_share_pct": as_float(stats.get("employment_share_pct")),
            "men_share_pct": as_float(stats.get("men_share_pct")),
            "women_share_pct": as_float(stats.get("women_share_pct")),
            "employees": as_int(stats.get("employees")),
            "pay_hourly": as_float(stats.get("pay_hourly")),
            "pay_weekly": as_float(stats.get("pay_weekly")),
            "average_hourly_wage": as_float(stats.get("average_hourly_wage")),
            "average_weekly_wage": as_float(stats.get("average_weekly_wage")),
            "outlook_label": stats.get("outlook_label") or None,
            "outlook_score": as_float(stats.get("outlook_score")),
            "outlook_window_start": as_int(stats.get("outlook_window_start")),
            "outlook_window_end": as_int(stats.get("outlook_window_end")),
            "outlook_release_date": stats.get("outlook_release_date") or None,
            "outlook_weight_basis": stats.get("outlook_weight_basis") or None,
        }
    return parsed


def weighted_average(pairs):
    valid = [(value, weight) for value, weight in pairs if value is not None and weight not in (None, 0)]
    if not valid:
        return None
    total_weight = sum(weight for _, weight in valid)
    if total_weight <= 0:
        return None
    return sum(value * weight for value, weight in valid) / total_weight


def aggregate_major_group_stats(items, geo_code, total_geo_jobs):
    stats = [item["stats_by_geo"][geo_code] for item in items]
    jobs_values = [stat["jobs"] for stat in stats if stat["jobs"] is not None]
    employees_values = [stat["employees"] for stat in stats if stat["employees"] is not None]
    change_values = [stat["employment_change_abs"] for stat in stats if stat["employment_change_abs"] is not None]
    jobs = sum(jobs_values) if jobs_values else None
    employees = sum(employees_values) if employees_values else None
    change_abs = sum(change_values) if change_values else None

    baseline_total = None
    if jobs is not None and change_abs is not None:
        baseline_total = jobs - change_abs

    outlook_pairs = []
    for stat in stats:
        weight = stat["jobs"]
        if weight in (None, 0):
            weight = 1
        outlook_pairs.append((stat["outlook_score"], weight))
    outlook_score = weighted_average(outlook_pairs)
    release_dates = sorted({stat["outlook_release_date"] for stat in stats if stat["outlook_release_date"]})

    weighted_trend = weighted_average([(stat["trend_pct"], stat["jobs"] or 1) for stat in stats])
    weighted_unemployment = weighted_average([(stat["unemployment_rate"], stat["jobs"] or 1) for stat in stats])
    weighted_men = weighted_average([(stat["men_share_pct"], stat["jobs"] or 1) for stat in stats])
    weighted_women = weighted_average([(stat["women_share_pct"], stat["jobs"] or 1) for stat in stats])
    weighted_pay_hourly = weighted_average([(stat["pay_hourly"], stat["jobs"] or 1) for stat in stats])
    weighted_pay_weekly = weighted_average([(stat["pay_weekly"], stat["jobs"] or 1) for stat in stats])
    weighted_avg_hourly = weighted_average([(stat["average_hourly_wage"], stat["jobs"] or 1) for stat in stats])
    weighted_avg_weekly = weighted_average([(stat["average_weekly_wage"], stat["jobs"] or 1) for stat in stats])

    return {
        "jobs": jobs,
        "jobs_year": max((stat["jobs_year"] for stat in stats if stat["jobs_year"] is not None), default=None),
        "trend_pct": round(((jobs - baseline_total) / baseline_total) * 100, 1)
        if baseline_total not in (None, 0) and jobs is not None
        else round(weighted_trend, 1)
        if weighted_trend is not None
        else None,
        "trend_from_year": max((stat["trend_from_year"] for stat in stats if stat["trend_from_year"] is not None), default=None),
        "employment_change_abs": change_abs,
        "unemployment_rate": round(weighted_unemployment, 1) if weighted_unemployment is not None else None,
        "employment_share_pct": round((jobs / total_geo_jobs) * 100, 1) if jobs is not None and total_geo_jobs else None,
        "men_share_pct": round(weighted_men, 1) if weighted_men is not None else None,
        "women_share_pct": round(weighted_women, 1) if weighted_women is not None else None,
        "employees": employees,
        "pay_hourly": round(weighted_pay_hourly, 2) if weighted_pay_hourly is not None else None,
        "pay_weekly": round(weighted_pay_weekly, 2) if weighted_pay_weekly is not None else None,
        "average_hourly_wage": round(weighted_avg_hourly, 2) if weighted_avg_hourly is not None else None,
        "average_weekly_wage": round(weighted_avg_weekly, 2) if weighted_avg_weekly is not None else None,
        "outlook_label": label_from_score(outlook_score),
        "outlook_score": round(outlook_score, 2) if outlook_score is not None else None,
        "outlook_window_start": max((stat["outlook_window_start"] for stat in stats if stat["outlook_window_start"] is not None), default=None),
        "outlook_window_end": max((stat["outlook_window_end"] for stat in stats if stat["outlook_window_end"] is not None), default=None),
        "outlook_release_date": release_dates[-1] if release_dates else None,
        "outlook_weight_basis": "unit_group_jobs_weighted_outlook" if jobs is not None else "average_unit_group_outlook",
    }


def main():
    with Path("occupations.csv").open(encoding="utf-8", newline="") as handle:
        canonical_rows = list(csv.DictReader(handle))

    if not canonical_rows:
        raise ValueError("occupations.csv is empty")

    official_noc = load_official_noc_structure()
    jobs_year = max(int(row["data_year"]) for row in canonical_rows if row.get("data_year"))
    trend_from_year = min(int(row["trend_from_year"]) for row in canonical_rows if row.get("trend_from_year"))
    outlook_start = max(int(row["outlook_window_start"]) for row in canonical_rows if row.get("outlook_window_start"))
    outlook_end = max(int(row["outlook_window_end"]) for row in canonical_rows if row.get("outlook_window_end"))
    outlook_release_date = max((row["outlook_release_date"] for row in canonical_rows if row.get("outlook_release_date")), default="")
    epiac_reference_year = max(int(row["epiac_reference_year"]) for row in canonical_rows if row.get("epiac_reference_year"))

    occupations = []
    for row in canonical_rows:
        occupations.append(
            {
                "title": row["title"],
                "slug": row["slug"],
                "category": row["category"],
                "noc_code": row["noc_code"],
                "broad_category_code": row["broad_category_code"],
                "broad_category_title": row["broad_category_title"],
                "major_group_code": row["major_group_code"],
                "major_group_title": row["major_group_title"],
                "sub_major_group_code": row["sub_major_group_code"],
                "sub_major_group_title": row["sub_major_group_title"],
                "minor_group_code": row["minor_group_code"],
                "minor_group_title": row["minor_group_title"],
                "definition": row.get("definition", "") or None,
                "metric_source_kind": row.get("metric_source_kind") or None,
                "metric_source_note": row.get("metric_source_note") or None,
                "metric_rationale": row.get("metric_source_note") or None,
                "jobs": as_int(row["num_jobs"]),
                "jobs_year": as_int(row["data_year"]),
                "trend_pct": as_float(row["employment_change_pct"]),
                "trend_from_year": as_int(row["trend_from_year"]),
                "employment_change_abs": as_int(row["employment_change_abs"]),
                "unemployment_rate": as_float(row["unemployment_rate"]),
                "employment_share_pct": as_float(row["employment_share_pct"]),
                "men_share_pct": as_float(row["men_share_pct"]),
                "women_share_pct": as_float(row["women_share_pct"]),
                "pay_hourly": as_float(row["median_hourly_wage"]),
                "pay_weekly": as_float(row["median_weekly_wage"]),
                "average_hourly_wage": as_float(row["average_hourly_wage"]),
                "average_weekly_wage": as_float(row["average_weekly_wage"]),
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

    occupations.sort(key=lambda item: item["noc_code"])

    total_jobs_by_geo = {}
    for geo in GEO_METADATA:
        geo_code = geo["code"]
        total_jobs_by_geo[geo_code] = sum(item["stats_by_geo"][geo_code]["jobs"] or 0 for item in occupations)

    nodes_by_code = official_noc["nodes_by_code"]
    major_group_buckets = {}
    for occupation in occupations:
        major_group_buckets.setdefault(occupation["major_group_code"], []).append(occupation)

    major_groups = []
    for major_group_code, items in sorted(major_group_buckets.items()):
        first = items[0]
        stats_by_geo = {
            geo["code"]: aggregate_major_group_stats(items, geo["code"], total_jobs_by_geo[geo["code"]])
            for geo in GEO_METADATA
        }
        canada_stats = stats_by_geo[DEFAULT_GEO_CODE]
        weighted_exposure = weighted_average([(item["exposure"], item["jobs"] or 1) for item in items])
        weighted_high = weighted_average([(item["epiac_high_exposure_pct"], item["jobs"] or 1) for item in items])
        weighted_helc = weighted_average([(item["epiac_helc_pct"], item["jobs"] or 1) for item in items])
        weighted_hehc = weighted_average([(item["epiac_hehc_pct"], item["jobs"] or 1) for item in items])
        weighted_low = weighted_average([(item["epiac_low_pct"], item["jobs"] or 1) for item in items])
        weighted_aioe = weighted_average([(item["epiac_aioe"], item["jobs"] or 1) for item in items])
        weighted_comp = weighted_average([(item["epiac_complementarity"], item["jobs"] or 1) for item in items])
        weighted_caioe = weighted_average([(item["epiac_caioe"], item["jobs"] or 1) for item in items])
        major_groups.append(
            {
                "title": first["major_group_title"],
                "slug": f"major-{major_group_code}",
                "category": first["broad_category_title"],
                "definition": nodes_by_code[major_group_code].get("definition") or None,
                "noc_code": major_group_code,
                "broad_category_code": first["broad_category_code"],
                "broad_category_title": first["broad_category_title"],
                "major_group_code": major_group_code,
                "major_group_title": first["major_group_title"],
                "official_sub_major_group_count": len({item["sub_major_group_code"] for item in items}),
                "official_minor_group_count": len({item["minor_group_code"] for item in items}),
                "official_unit_group_count": len(items),
                "canonical_unit_codes": [item["noc_code"] for item in items],
                "jobs": canada_stats["jobs"],
                "jobs_year": canada_stats["jobs_year"],
                "trend_pct": canada_stats["trend_pct"],
                "trend_from_year": canada_stats["trend_from_year"],
                "employment_change_abs": canada_stats["employment_change_abs"],
                "unemployment_rate": canada_stats["unemployment_rate"],
                "employment_share_pct": canada_stats["employment_share_pct"],
                "men_share_pct": canada_stats["men_share_pct"],
                "women_share_pct": canada_stats["women_share_pct"],
                "pay_hourly": canada_stats["pay_hourly"],
                "pay_weekly": canada_stats["pay_weekly"],
                "average_hourly_wage": canada_stats["average_hourly_wage"],
                "average_weekly_wage": canada_stats["average_weekly_wage"],
                "employees": canada_stats["employees"],
                "outlook_label": canada_stats["outlook_label"],
                "outlook_score": canada_stats["outlook_score"],
                "outlook_window_start": canada_stats["outlook_window_start"],
                "outlook_window_end": canada_stats["outlook_window_end"],
                "outlook_release_date": canada_stats["outlook_release_date"],
                "exposure": round(weighted_exposure) if weighted_exposure is not None else None,
                "exposure_metric": "high_exposure_share",
                "exposure_rationale": "Aggregated from canonical unit groups. EPIAC values roll up unit-level mappings from published StatCan occupation groups.",
                "metric_rationale": "This major group aggregates canonical unit groups. Labour-market counts and wages reflect the unit-group estimates allocated from published StatCan annual occupation tables using ESDC employment weights.",
                "epiac_reference_year": epiac_reference_year,
                "epiac_high_exposure_pct": round(weighted_high, 1) if weighted_high is not None else None,
                "epiac_helc_pct": round(weighted_helc, 1) if weighted_helc is not None else None,
                "epiac_hehc_pct": round(weighted_hehc, 1) if weighted_hehc is not None else None,
                "epiac_low_pct": round(weighted_low, 1) if weighted_low is not None else None,
                "epiac_aioe": round(weighted_aioe, 4) if weighted_aioe is not None else None,
                "epiac_complementarity": round(weighted_comp, 4) if weighted_comp is not None else None,
                "epiac_caioe": round(weighted_caioe, 4) if weighted_caioe is not None else None,
                "epiac_group_code": max(((item["epiac_group_code"], item["jobs"] or 1) for item in items if item["epiac_group_code"]), key=lambda pair: pair[1], default=(None, 0))[0],
                "epiac_group_label": max(((item["epiac_group_label"], item["jobs"] or 1) for item in items if item["epiac_group_label"]), key=lambda pair: pair[1], default=(None, 0))[0],
                "epiac_source_title": STATCAN_EPIAC_TITLE,
                "epiac_source_url": STATCAN_EPIAC_URL,
                "epiac_source_groups": sorted({group for item in items for group in item["epiac_source_groups"]}),
                "url": first["url"],
                "employment_url": first["employment_url"],
                "wages_url": first["wages_url"],
                "outlook_url": first["outlook_url"],
                "stats_by_geo": stats_by_geo,
            }
        )

    payload = {
        "meta": {
            "title": "AI Exposure of the Canadian Job Market",
            "geography": "Canada",
            "default_geography": DEFAULT_GEO_CODE,
            "geographies": GEO_METADATA,
            "occupation_count": len(occupations),
            "canonical_unit_group_count": len(occupations),
            "major_group_count": len(major_groups),
            "primary_rollup_layer": "major_groups",
            "primary_rollup_count": len(major_groups),
            "jobs_year": jobs_year,
            "trend_from_year": trend_from_year,
            "outlook_window_start": outlook_start,
            "outlook_window_end": outlook_end,
            "outlook_release_date": outlook_release_date or None,
            "official_noc_2021_hierarchy": official_noc["counts"],
            "primary_rollup_note": "The dashboard rolls canonical NOC 2021 unit groups through the 45 official major groups.",
            "metric_model_note": "StatCan annual labour-force and wage tables are published at a coarser occupation grain than official NOC 2021 unit groups, so the unit-group labour metrics are allocated using ESDC unit employment weights. Outlook remains direct from the ESDC unit-group release.",
            "exposure_reference_year": epiac_reference_year,
            "exposure_metric": "StatCan EPIAC high-exposure share",
            "exposure_metric_scale": "0-10 display score derived from the share of workers in high-exposure EPIAC occupations",
            "exposure_note": "Official EPIAC fields are mapped from published StatCan occupation groups onto the canonical NOC 2021 unit groups.",
            "source": "Statistics Canada annual occupation tables rebuilt onto the canonical NOC 2021 spine",
            "source_tables": [
                {"name": "14-10-0416-01 Labour force characteristics by occupation, annual", "url": STATCAN_EMPLOYMENT_URL},
                {"name": "14-10-0417-01 Employee wages by occupation, annual", "url": STATCAN_WAGES_URL},
                {"name": STATCAN_EPIAC_TITLE, "url": STATCAN_EPIAC_URL},
                {"name": "2025-2027 Employment Outlooks - NOC 2021", "url": next((item["outlook_url"] for item in major_groups if item.get("outlook_url")), "")},
            ],
            "research_sources": [
                {"name": "StatCan: Employment growth in Canada since the beginning of the generative AI era", "url": STATCAN_EPIAC_CONTEXT_URL},
                {"name": "StatCan: Croissance de l'emploi au Canada depuis le debut de l'ere de l'IA generative", "url": STATCAN_EPIAC_CONTEXT_FR_URL},
                {"name": "ISQ: Exposition des professions a l'intelligence artificielle en 2024", "url": ISQ_EPIAC_URL},
            ],
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        },
        "occupations": occupations,
        "major_groups": major_groups,
    }

    SITE_DIR.mkdir(exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle)

    total_jobs = sum(item["jobs"] for item in occupations if item["jobs"])
    print(f"Wrote {len(occupations)} canonical occupation groups to {OUTPUT_PATH}")
    print(f"Wrote {len(major_groups)} primary major-group rollups to payload")
    print(f"Total workers represented ({jobs_year}): {total_jobs:,}")


if __name__ == "__main__":
    main()
