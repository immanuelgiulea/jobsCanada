"""
Download and transform StatCan occupation tables into project inputs.

This replaces the BLS handbook scrape with annual Canadian labour-market data
from Statistics Canada:

- 14-10-0416-01 Labour force characteristics by occupation, annual
- 14-10-0417-01 Employee wages by occupation, annual

Outputs:
- occupations.json
- occupations.csv
- pages/<slug>.md

Usage:
    uv run python fetch_statcan.py
"""

from __future__ import annotations

import csv
import json
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from urllib.request import urlopen

from epiac_data import load_group_epiac
from geography import DEFAULT_GEO_CODE, GEO_CODES, STATCAN_GEO_TO_CODE
from outlook_data import load_group_outlooks


EMPLOYMENT_TABLE_ID = "14100416"
WAGE_TABLE_ID = "14100417"
STATCAN_TABLE_URLS = {
    EMPLOYMENT_TABLE_ID: "https://www150.statcan.gc.ca/n1/tbl/csv/14100416-eng.zip",
    WAGE_TABLE_ID: "https://www150.statcan.gc.ca/n1/tbl/csv/14100417-eng.zip",
}
STATCAN_PAGE_URLS = {
    "employment": "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041601",
    "wages": "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041701",
}

DATA_DIR = Path("tmp/statcan")
PAGES_DIR = Path("pages")

EMPLOYMENT_DIMENSION_ID = "3"
WAGE_DIMENSION_ID = "4"
ROOT_NAME_PREFIXES = ("Total, all occupations", "Total employees, all occupations")
SPECIAL_ROW_PREFIXES = ("Total", "Unclassified")

EMPLOYMENT_MEASURES = {"Employment", "Unemployment rate", "Proportion of employment"}
WAGE_MEASURES = {
    "Total employees, all wages",
    "Average hourly wage rate",
    "Average weekly wage rate",
    "Median hourly wage rate",
    "Median weekly wage rate",
}


@dataclass(frozen=True)
class Member:
    name: str
    code: str
    member_id: str
    parent_id: str

    @property
    def label(self) -> str:
        return f"{self.name} {self.code}".strip()


def download_table_zip(table_id: str) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = DATA_DIR / f"{table_id}-eng.zip"
    if zip_path.exists():
        return zip_path

    url = STATCAN_TABLE_URLS[table_id]
    print(f"Downloading {table_id} from {url}")
    with urlopen(url) as response, zip_path.open("wb") as output:
        output.write(response.read())
    return zip_path


def ensure_table_files(table_id: str) -> tuple[Path, Path]:
    zip_path = download_table_zip(table_id)
    extract_dir = DATA_DIR / table_id
    csv_path = extract_dir / f"{table_id}.csv"
    metadata_path = extract_dir / f"{table_id}_MetaData.csv"

    if csv_path.exists() and metadata_path.exists():
        return csv_path, metadata_path

    extract_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(extract_dir)
    return csv_path, metadata_path


def parse_members(metadata_path: Path, dimension_id: str) -> dict[str, Member]:
    members: dict[str, Member] = {}
    in_members_section = False

    with metadata_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        for row in reader:
            if row[:2] == ["Dimension ID", "Member Name"]:
                in_members_section = True
                continue

            if not in_members_section or not row:
                continue

            if row[0] in {"Symbol Legend", "Survey Code", "Subject Code", "Note ID", "Correction ID"}:
                break

            if row[0] != dimension_id:
                continue

            member = Member(
                name=row[1].strip(),
                code=row[2].strip(),
                member_id=row[3].strip(),
                parent_id=row[4].strip(),
            )
            members[member.member_id] = member

    return members


def find_root_id(members: dict[str, Member]) -> str:
    candidates = [
        member.member_id
        for member in members.values()
        if not member.parent_id and member.name.startswith(ROOT_NAME_PREFIXES)
    ]
    if len(candidates) != 1:
        raise ValueError(f"Expected exactly one root member, found {candidates}")
    return candidates[0]


def find_leaf_ids(members: dict[str, Member]) -> list[str]:
    parent_ids = {member.parent_id for member in members.values() if member.parent_id}
    leaf_ids = []
    for member in members.values():
        if member.member_id in parent_ids:
            continue
        if member.name.startswith(SPECIAL_ROW_PREFIXES):
            continue
        leaf_ids.append(member.member_id)
    return sorted(leaf_ids, key=lambda mid: members[mid].label)


def top_level_category(member_id: str, members: dict[str, Member], root_id: str) -> str:
    current = members[member_id]
    while current.parent_id and current.parent_id != root_id:
        current = members[current.parent_id]
    return current.name


def parse_float(value: str) -> float | None:
    value = value.strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def to_people(thousands: float | None) -> int | None:
    if thousands is None:
        return None
    return int(round(thousands * 1000))


def slugify_code(code: str) -> str:
    cleaned = code.strip("[]").replace(", ", "-").replace(",", "-").replace(" ", "")
    cleaned = re.sub(r"[^0-9a-zA-Z-]+", "-", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-").lower()
    return f"noc-{cleaned}"


def fmt_number(value: int | None) -> str:
    if value is None:
        return "-"
    return f"{value:,}"


def fmt_percent(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value:.1f}%"


def fmt_currency(value: float | None) -> str:
    if value is None:
        return "-"
    return f"${value:.2f}"


def recent_years(end_year: int, available_years: set[int], count: int = 7) -> list[int]:
    years = []
    for year in range(end_year - count + 1, end_year + 1):
        if year in available_years:
            years.append(year)
    return years


def empty_geo_metrics() -> dict[str, dict[str, dict[int, float]]]:
    metric_names = [
        "employment",
        "men_employment",
        "women_employment",
        "unemployment_rate",
        "employment_share_pct",
        "num_employees",
        "average_hourly_wage",
        "average_weekly_wage",
        "median_hourly_wage",
        "median_weekly_wage",
    ]
    return {
        geo_code: {metric_name: {} for metric_name in metric_names}
        for geo_code in GEO_CODES
    }


def round_value(value: float | None, digits: int) -> float | None:
    if value is None:
        return None
    return round(value, digits)


def build_geo_snapshot(
    geo_metrics: dict[str, dict[int, float]],
    jobs_year: int | None,
    wages_year: int | None,
    baseline_year: int,
    total_latest_jobs: int,
    outlook: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    latest_jobs = geo_metrics["employment"].get(jobs_year) if jobs_year is not None else None
    baseline_jobs = geo_metrics["employment"].get(baseline_year)
    latest_men = geo_metrics["men_employment"].get(jobs_year) if jobs_year is not None else None
    latest_women = geo_metrics["women_employment"].get(jobs_year) if jobs_year is not None else None

    change_abs = None
    change_pct = None
    if latest_jobs is not None and baseline_jobs not in (None, 0):
        change_abs = to_people(latest_jobs - baseline_jobs)
        change_pct = ((latest_jobs - baseline_jobs) / baseline_jobs) * 100

    men_share = None
    women_share = None
    if latest_jobs not in (None, 0):
        if latest_men is not None:
            men_share = (latest_men / latest_jobs) * 100
        if latest_women is not None:
            women_share = (latest_women / latest_jobs) * 100

    employment_share = geo_metrics["employment_share_pct"].get(jobs_year) if jobs_year is not None else None
    if employment_share is None and latest_jobs is not None and total_latest_jobs:
        employment_share = (to_people(latest_jobs) / total_latest_jobs) * 100

    pay_hourly = geo_metrics["median_hourly_wage"].get(wages_year) if wages_year is not None else None
    pay_weekly = geo_metrics["median_weekly_wage"].get(wages_year) if wages_year is not None else None
    average_hourly = geo_metrics["average_hourly_wage"].get(wages_year) if wages_year is not None else None
    average_weekly = geo_metrics["average_weekly_wage"].get(wages_year) if wages_year is not None else None

    snapshot = {
        "jobs": to_people(latest_jobs),
        "jobs_year": jobs_year,
        "trend_pct": round_value(change_pct, 1),
        "trend_from_year": baseline_year if jobs_year is not None else None,
        "unemployment_rate": round_value(
            geo_metrics["unemployment_rate"].get(jobs_year) if jobs_year is not None else None,
            1,
        ),
        "employment_share_pct": round_value(employment_share, 1),
        "men_share_pct": round_value(men_share, 1),
        "women_share_pct": round_value(women_share, 1),
        "employees": to_people(geo_metrics["num_employees"].get(wages_year)) if wages_year is not None else None,
        "pay_hourly": round_value(pay_hourly, 2),
        "pay_weekly": round_value(pay_weekly, 2),
        "outlook_label": outlook.get("outlook_label") or None,
        "outlook_score": round_value(outlook.get("outlook_score"), 2),  # type: ignore[arg-type]
        "outlook_window_start": outlook.get("outlook_window_start") or None,
        "outlook_window_end": outlook.get("outlook_window_end") or None,
        "outlook_release_date": outlook.get("outlook_release_date") or None,
    }
    extras = {
        "employment_change_abs": change_abs,
        "average_hourly_wage": round_value(average_hourly, 2),
        "average_weekly_wage": round_value(average_weekly, 2),
    }
    return snapshot, extras


def main() -> None:
    employment_csv, employment_meta = ensure_table_files(EMPLOYMENT_TABLE_ID)
    wage_csv, wage_meta = ensure_table_files(WAGE_TABLE_ID)

    employment_members = parse_members(employment_meta, EMPLOYMENT_DIMENSION_ID)
    wage_members = parse_members(wage_meta, WAGE_DIMENSION_ID)

    employment_root_id = find_root_id(employment_members)
    _ = find_root_id(wage_members)

    employment_leaves = {
        employment_members[mid].label: employment_members[mid]
        for mid in find_leaf_ids(employment_members)
    }
    wage_leaves = {
        wage_members[mid].label: wage_members[mid]
        for mid in find_leaf_ids(wage_members)
    }

    common_labels = sorted(set(employment_leaves) & set(wage_leaves))
    if not common_labels:
        raise ValueError("No overlapping occupation groups found between StatCan tables")

    occupations = {}
    for label in common_labels:
        member = employment_leaves[label]
        occupations[label] = {
            "title": member.name,
            "noc_code": member.code.strip("[]"),
            "slug": slugify_code(member.code),
            "category": top_level_category(member.member_id, employment_members, employment_root_id),
            "url": STATCAN_PAGE_URLS["employment"],
            "employment_url": STATCAN_PAGE_URLS["employment"],
            "wages_url": STATCAN_PAGE_URLS["wages"],
            "stats_by_geo": empty_geo_metrics(),
        }

    outlook_by_geo, outlook_meta = load_group_outlooks([record["noc_code"] for record in occupations.values()])
    epiac_by_group, _ = load_group_epiac([record["noc_code"] for record in occupations.values()])

    employment_years_by_geo = {geo_code: set() for geo_code in GEO_CODES}
    wage_years_by_geo = {geo_code: set() for geo_code in GEO_CODES}

    with employment_csv.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            geo_code = STATCAN_GEO_TO_CODE.get(row["GEO"])
            if not geo_code:
                continue
            label = row["National Occupational Classification (NOC)"]
            if label not in occupations:
                continue
            measure = row["Labour force characteristics"]
            if measure not in EMPLOYMENT_MEASURES:
                continue
            year = int(row["REF_DATE"])
            value = parse_float(row["VALUE"])
            if value is None:
                continue

            employment_years_by_geo[geo_code].add(year)
            geo_metrics = occupations[label]["stats_by_geo"][geo_code]
            gender = row["Gender"]
            if measure == "Employment":
                if gender == "Total - Gender":
                    geo_metrics["employment"][year] = value
                elif gender == "Men+":
                    geo_metrics["men_employment"][year] = value
                elif gender == "Women+":
                    geo_metrics["women_employment"][year] = value
            elif gender == "Total - Gender":
                if measure == "Unemployment rate":
                    geo_metrics["unemployment_rate"][year] = value
                elif measure == "Proportion of employment":
                    geo_metrics["employment_share_pct"][year] = value

    with wage_csv.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            geo_code = STATCAN_GEO_TO_CODE.get(row["GEO"])
            if not geo_code:
                continue
            if row["Type of work"] != "Both full- and part-time employees":
                continue
            if row["Gender"] != "Total - Gender":
                continue
            if row["Age group"] != "15 years and over":
                continue
            label = row["National Occupational Classification (NOC)"]
            if label not in occupations:
                continue
            measure = row["Wages"]
            if measure not in WAGE_MEASURES:
                continue
            year = int(row["REF_DATE"])
            value = parse_float(row["VALUE"])
            if value is None:
                continue
            wage_years_by_geo[geo_code].add(year)
            key = {
                "Total employees, all wages": "num_employees",
                "Average hourly wage rate": "average_hourly_wage",
                "Average weekly wage rate": "average_weekly_wage",
                "Median hourly wage rate": "median_hourly_wage",
                "Median weekly wage rate": "median_weekly_wage",
            }[measure]
            occupations[label]["stats_by_geo"][geo_code][key][year] = value

    all_job_years = sorted({year for years in employment_years_by_geo.values() for year in years})
    all_wage_years = sorted({year for years in wage_years_by_geo.values() for year in years})
    if not all_job_years or not all_wage_years:
        raise ValueError("StatCan tables did not yield employment and wage data")

    baseline_year = 2019 if 2019 in all_job_years else all_job_years[max(0, len(all_job_years) - 7)]
    jobs_year_by_geo = {
        geo_code: max(years) if years else None
        for geo_code, years in employment_years_by_geo.items()
    }
    wages_year_by_geo = {
        geo_code: max(years) if years else None
        for geo_code, years in wage_years_by_geo.items()
    }
    total_latest_jobs_by_geo = {
        geo_code: sum(
            to_people(record["stats_by_geo"][geo_code]["employment"].get(jobs_year_by_geo[geo_code])) or 0
            for record in occupations.values()
        )
        if jobs_year_by_geo[geo_code] is not None
        else 0
        for geo_code in GEO_CODES
    }

    canada_jobs_year = jobs_year_by_geo[DEFAULT_GEO_CODE]
    canada_wages_year = wages_year_by_geo[DEFAULT_GEO_CODE]
    if canada_jobs_year is None or canada_wages_year is None:
        raise ValueError("Canada-wide data is required for compatibility outputs")

    fieldnames = [
        "title",
        "category",
        "slug",
        "noc_code",
        "data_year",
        "trend_from_year",
        "num_jobs",
        "unemployment_rate",
        "employment_share_pct",
        "employment_change_pct",
        "employment_change_abs",
        "men_share_pct",
        "women_share_pct",
        "num_employees",
        "average_hourly_wage",
        "average_weekly_wage",
        "median_hourly_wage",
        "median_weekly_wage",
        "outlook_label",
        "outlook_score",
        "outlook_window_start",
        "outlook_window_end",
        "outlook_release_date",
        "outlook_source_url",
        "epiac_reference_year",
        "epiac_display_score",
        "epiac_high_exposure_pct",
        "epiac_helc_pct",
        "epiac_hehc_pct",
        "epiac_low_pct",
        "epiac_aioe",
        "epiac_complementarity",
        "epiac_caioe",
        "epiac_group_code",
        "epiac_group_label",
        "epiac_source_title",
        "epiac_source_url",
        "epiac_source_note",
        "epiac_source_groups",
        "url",
        "employment_url",
        "wages_url",
        "stats_by_geo_json",
    ]

    rows = []
    occupations_index = []
    page_records = []

    for label, record in occupations.items():
        stats_by_geo_output: dict[str, dict[str, object]] = {}
        extras_by_geo: dict[str, dict[str, object]] = {}
        for geo_code in GEO_CODES:
            geo_stats, geo_extras = build_geo_snapshot(
                record["stats_by_geo"][geo_code],
                jobs_year_by_geo[geo_code],
                wages_year_by_geo[geo_code],
                baseline_year,
                total_latest_jobs_by_geo[geo_code],
                outlook_by_geo.get(geo_code, {}).get(record["noc_code"], {}),
            )
            stats_by_geo_output[geo_code] = geo_stats
            extras_by_geo[geo_code] = geo_extras

        canada_stats = stats_by_geo_output[DEFAULT_GEO_CODE]
        canada_extras = extras_by_geo[DEFAULT_GEO_CODE]
        epiac = epiac_by_group.get(record["noc_code"], {})

        row = {
            "title": record["title"],
            "category": record["category"],
            "slug": record["slug"],
            "noc_code": record["noc_code"],
            "data_year": canada_stats["jobs_year"] or "",
            "trend_from_year": canada_stats["trend_from_year"] or "",
            "num_jobs": canada_stats["jobs"] or "",
            "unemployment_rate": f"{canada_stats['unemployment_rate']:.1f}" if canada_stats["unemployment_rate"] is not None else "",
            "employment_share_pct": f"{canada_stats['employment_share_pct']:.1f}" if canada_stats["employment_share_pct"] is not None else "",
            "employment_change_pct": f"{canada_stats['trend_pct']:.1f}" if canada_stats["trend_pct"] is not None else "",
            "employment_change_abs": canada_extras["employment_change_abs"] if canada_extras["employment_change_abs"] is not None else "",
            "men_share_pct": f"{canada_stats['men_share_pct']:.1f}" if canada_stats["men_share_pct"] is not None else "",
            "women_share_pct": f"{canada_stats['women_share_pct']:.1f}" if canada_stats["women_share_pct"] is not None else "",
            "num_employees": canada_stats["employees"] or "",
            "average_hourly_wage": f"{canada_extras['average_hourly_wage']:.2f}" if canada_extras["average_hourly_wage"] is not None else "",
            "average_weekly_wage": f"{canada_extras['average_weekly_wage']:.2f}" if canada_extras["average_weekly_wage"] is not None else "",
            "median_hourly_wage": f"{canada_stats['pay_hourly']:.2f}" if canada_stats["pay_hourly"] is not None else "",
            "median_weekly_wage": f"{canada_stats['pay_weekly']:.2f}" if canada_stats["pay_weekly"] is not None else "",
            "outlook_label": canada_stats["outlook_label"] or "",
            "outlook_score": f"{canada_stats['outlook_score']:.2f}" if canada_stats["outlook_score"] is not None else "",
            "outlook_window_start": canada_stats["outlook_window_start"] or "",
            "outlook_window_end": canada_stats["outlook_window_end"] or "",
            "outlook_release_date": canada_stats["outlook_release_date"] or "",
            "outlook_source_url": outlook_by_geo.get(DEFAULT_GEO_CODE, {}).get(record["noc_code"], {}).get("outlook_source_url", ""),
            "epiac_reference_year": epiac.get("epiac_reference_year", ""),
            "epiac_display_score": epiac.get("epiac_display_score", ""),
            "epiac_high_exposure_pct": f"{epiac['epiac_high_exposure_pct']:.1f}" if epiac.get("epiac_high_exposure_pct") is not None else "",
            "epiac_helc_pct": f"{epiac['epiac_helc_pct']:.1f}" if epiac.get("epiac_helc_pct") is not None else "",
            "epiac_hehc_pct": f"{epiac['epiac_hehc_pct']:.1f}" if epiac.get("epiac_hehc_pct") is not None else "",
            "epiac_low_pct": f"{epiac['epiac_low_pct']:.1f}" if epiac.get("epiac_low_pct") is not None else "",
            "epiac_aioe": f"{epiac['epiac_aioe']:.4f}" if epiac.get("epiac_aioe") is not None else "",
            "epiac_complementarity": f"{epiac['epiac_complementarity']:.4f}" if epiac.get("epiac_complementarity") is not None else "",
            "epiac_caioe": f"{epiac['epiac_caioe']:.4f}" if epiac.get("epiac_caioe") is not None else "",
            "epiac_group_code": epiac.get("epiac_group_code", ""),
            "epiac_group_label": epiac.get("epiac_group_label", ""),
            "epiac_source_title": epiac.get("epiac_source_title", ""),
            "epiac_source_url": epiac.get("epiac_source_url", ""),
            "epiac_source_note": epiac.get("epiac_source_note", ""),
            "epiac_source_groups": "; ".join(epiac.get("epiac_source_groups", [])),
            "url": record["url"],
            "employment_url": record["employment_url"],
            "wages_url": record["wages_url"],
            "stats_by_geo_json": json.dumps(
                stats_by_geo_output,
                ensure_ascii=True,
                separators=(",", ":"),
            ),
        }
        rows.append(row)
        occupations_index.append(
            {
                "title": record["title"],
                "category": record["category"],
                "slug": record["slug"],
                "noc_code": record["noc_code"],
                "outlook_label": row["outlook_label"],
                "outlook_score": row["outlook_score"],
                "epiac_display_score": row["epiac_display_score"],
                "epiac_group_label": row["epiac_group_label"],
                "epiac_high_exposure_pct": row["epiac_high_exposure_pct"],
                "url": record["url"],
            }
        )
        page_records.append((record, row))

    rows.sort(key=lambda row: (row["category"], -(row["num_jobs"] or 0), row["title"]))
    occupations_index.sort(key=lambda row: (row["category"], row["title"]))

    with Path("occupations.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with Path("occupations.json").open("w", encoding="utf-8") as handle:
        json.dump(occupations_index, handle, indent=2)

    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    for record, row in page_records:
        canada_metrics = record["stats_by_geo"][DEFAULT_GEO_CODE]
        years = recent_years(
            canada_jobs_year,
            set(canada_metrics["employment"].keys()) | set(canada_metrics["median_hourly_wage"].keys()),
        )
        lines = [
            f"# {record['title']}",
            "",
            f"- NOC 2021 group: {record['noc_code']}",
            f"- Broad category: {record['category']}",
            f"- Employment in Canada ({canada_jobs_year}): {fmt_number(int(row['num_jobs']) if row['num_jobs'] else None)}",
            f"- Unemployment rate ({canada_jobs_year}): {fmt_percent(parse_float(row['unemployment_rate']))}",
            f"- Share of total Canadian employment ({canada_jobs_year}): {fmt_percent(parse_float(row['employment_share_pct']))}",
            f"- Employment change ({baseline_year} to {canada_jobs_year}): {fmt_percent(parse_float(row['employment_change_pct']))} ({fmt_number(int(row['employment_change_abs']) if row['employment_change_abs'] else None)})",
            f"- Men+ share of employment ({canada_jobs_year}): {fmt_percent(parse_float(row['men_share_pct']))}",
            f"- Women+ share of employment ({canada_jobs_year}): {fmt_percent(parse_float(row['women_share_pct']))}",
            f"- Median hourly wage ({canada_wages_year}): {fmt_currency(parse_float(row['median_hourly_wage']))}",
            f"- StatCan EPIAC high-exposure share ({row['epiac_reference_year']}): {fmt_percent(parse_float(row['epiac_high_exposure_pct']))}",
            f"- Dominant EPIAC group: {row['epiac_group_label'] or '-'}",
            f"- Average AIOE / complementarity ({row['epiac_reference_year']}): {(parse_float(row['epiac_aioe']) or 0):.2f} / {(parse_float(row['epiac_complementarity']) or 0):.2f}",
            f"- Employment outlook ({row['outlook_window_start']} to {row['outlook_window_end']}): {row['outlook_label'] or '-'}",
            f"- Median weekly wage ({canada_wages_year}): {fmt_currency(parse_float(row['median_weekly_wage']))}",
            f"- Average hourly wage ({canada_wages_year}): {fmt_currency(parse_float(row['average_hourly_wage']))}",
            f"- Average weekly wage ({canada_wages_year}): {fmt_currency(parse_float(row['average_weekly_wage']))}",
            "",
            "## Recent annual series",
            "",
            "| Year | Employment | Unemployment rate | Median hourly wage |",
            "|------|------------|-------------------|--------------------|",
        ]
        for year in years:
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(year),
                        fmt_number(to_people(canada_metrics["employment"].get(year))),
                        fmt_percent(canada_metrics["unemployment_rate"].get(year)),
                        fmt_currency(canada_metrics["median_hourly_wage"].get(year)),
                    ]
                )
                + " |"
            )
        lines.extend(
            [
                "",
                "## Source tables",
                "",
                f"- Labour force characteristics by occupation, annual: {record['employment_url']}",
                f"- Employee wages by occupation, annual: {record['wages_url']}",
                f"- {row['epiac_source_title']}: {row['epiac_source_url']}",
                f"- {outlook_meta['title']}: {outlook_meta['page_url']}",
                "",
                "## Geography coverage note",
                "",
                "The StatCan occupation tables in this project cover Canada and the provinces only. Yukon, the Northwest Territories, and Nunavut remain in the generated geography metadata, but labour-market metrics for those selectors are left unavailable rather than backfilled.",
            ]
        )
        if row["epiac_source_note"]:
            lines.extend(
                [
                    "",
                    "## EPIAC mapping note",
                    "",
                    row["epiac_source_note"],
                ]
            )
        (PAGES_DIR / f"{record['slug']}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {len(rows)} occupation groups to occupations.csv")
    print(f"Wrote {len(occupations_index)} occupation entries to occupations.json")
    print(f"Wrote {len(page_records)} markdown summaries to {PAGES_DIR}/")
    print("Geography coverage:")
    print("  - Labour-market data: Canada and 10 provinces")
    print("  - Outlook-only metadata: Yukon, Northwest Territories, Nunavut")
    total_jobs = sum(int(row["num_jobs"]) for row in rows if row["num_jobs"])
    print(f"Latest employment represented ({canada_jobs_year}): {total_jobs:,}")


if __name__ == "__main__":
    main()
