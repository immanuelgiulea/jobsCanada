"""
Download and transform StatCan occupation tables into canonical NOC 2021 inputs.

Generated outputs:

- `occupations.csv` / `occupations.json`: canonical NOC 2021 unit groups (516)

The official NOC 2021 hierarchy is the canonical spine. StatCan annual labour-
force and wage tables are published at a coarser occupation grain, so canonical
unit-group counts are estimated by allocating each published source group across
its unit groups using ESDC outlook employment weights.
"""

from __future__ import annotations

import csv
import json
import math
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from urllib.request import urlopen

from epiac_data import load_group_epiac
from geography import DEFAULT_GEO_CODE, GEO_CODES, STATCAN_GEO_TO_CODE
from noc_hierarchy import load_official_noc_structure
from oasis_data import build_and_write_oasis_artifacts, profiles_by_unit_group, unit_group_lookup
from outlook_data import expand_group_prefixes, load_group_outlooks, load_unit_outlooks


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
CANONICAL_INDEX_PATH = Path("occupations.json")
CANONICAL_CSV_PATH = Path("occupations.csv")

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


def slugify_code(code: str, prefix: str = "noc") -> str:
    cleaned = code.strip("[]").replace(", ", "-").replace(",", "-").replace(" ", "")
    cleaned = re.sub(r"[^0-9a-zA-Z-]+", "-", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-").lower()
    return f"{prefix}-{cleaned}"


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


def markdown_bullets(items: list[object], *, empty_message: str | None = None) -> list[str]:
    if not items:
        return [empty_message] if empty_message else []

    lines: list[str] = []
    for item in items:
        if item is None:
            continue
        text = str(item).strip()
        if text:
            lines.append(f"- {text}")
    return lines or ([empty_message] if empty_message else [])


def markdown_exclusions(items: list[dict[str, object]]) -> list[str]:
    if not items:
        return ["No explicit exclusions listed in the current OaSIS release."]

    lines = []
    for item in items:
        code = str(item.get("excluded_profile_code") or "").strip()
        title = str(item.get("job_title") or "").strip()
        if code and title:
            lines.append(f"- {code}: {title}")
        elif title:
            lines.append(f"- {title}")
        elif code:
            lines.append(f"- {code}")
    return lines or ["No explicit exclusions listed in the current OaSIS release."]


def markdown_core_competencies(items: list[dict[str, object]]) -> list[str]:
    if not items:
        return ["No core competencies listed in the current OaSIS release."]

    lines = []
    for item in items:
        competency = str(item.get("competency") or "").strip()
        statement = str(item.get("statement") or "").strip()
        if competency and statement:
            lines.append(f"- {competency}: {statement}")
        elif competency:
            lines.append(f"- {competency}")
        elif statement:
            lines.append(f"- {statement}")
    return lines or ["No core competencies listed in the current OaSIS release."]


def build_oasis_page_lines(
    unit_code: str,
    oasis_meta: dict[str, object],
    oasis_unit_group: dict[str, object],
    oasis_profiles: list[dict[str, object]],
) -> list[str]:
    profile_count = int(oasis_unit_group["profile_count"])
    mapping_kind = str(oasis_unit_group["mapping_kind"]).replace("_", " ")
    lines = [
        "## OaSIS profile coverage",
        "",
        f"- Resolved OaSIS release: {oasis_meta['title']}",
        f"- Official OaSIS package: {oasis_meta['package_url']}",
        f"- OaSIS profiles attached to this unit group: {profile_count}",
        f"- Mapping mode: {mapping_kind}",
        f"- Explicit mapping method: {oasis_meta['mapping_method']}",
    ]
    if not oasis_profiles:
        lines.extend(
            [
                "",
                "No OaSIS profiles were attached to this unit group in the generated artifact. See `oasis.json` and `oasis_profile_mappings.csv` for the audit report.",
            ]
        )
        return lines

    lines.extend(
        [
            "",
            f"This canonical unit group ({unit_code}) maps to {profile_count} official OaSIS profile(s) in the resolved release.",
        ]
    )
    for profile in oasis_profiles:
        example_titles = [str(item.get("job_title_text") or "").strip() for item in profile["example_titles"]]
        lines.extend(
            [
                "",
                f"### {profile['oasis_profile_code']} {profile['profile_title']}",
                "",
                profile["lead_statement"] or "Lead statement unavailable in the current OaSIS release.",
                "",
                "#### Core competencies",
                "",
            ]
        )
        lines.extend(markdown_core_competencies(profile["core_competencies"]))
        lines.extend(["", "#### Main duties", ""])
        lines.extend(markdown_bullets(profile["main_duties"], empty_message="No main duties listed in the current OaSIS release."))
        lines.extend(["", "#### Employment requirements", ""])
        lines.extend(
            markdown_bullets(
                profile["employment_requirements"],
                empty_message="No employment requirements listed in the current OaSIS release.",
            )
        )
        lines.extend(["", "#### Example titles", ""])
        lines.extend(markdown_bullets(example_titles, empty_message="No example titles listed in the current OaSIS release."))
        lines.extend(["", "#### Workplaces and employers", ""])
        lines.extend(
            markdown_bullets(
                profile["workplaces_employers"],
                empty_message="No workplaces or employers listed in the current OaSIS release.",
            )
        )
        lines.extend(["", "#### Additional information", ""])
        lines.extend(
            markdown_bullets(
                profile["additional_information"],
                empty_message="No additional information listed in the current OaSIS release.",
            )
        )
        lines.extend(["", "#### Exclusions", ""])
        lines.extend(markdown_exclusions(profile["exclusions"]))
    return lines


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
) -> dict[str, object]:
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

    return {
        "jobs": to_people(latest_jobs),
        "jobs_year": jobs_year,
        "trend_pct": round_value(change_pct, 1),
        "trend_from_year": baseline_year if jobs_year is not None else None,
        "employment_change_abs": change_abs,
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
        "average_hourly_wage": round_value(average_hourly, 2),
        "average_weekly_wage": round_value(average_weekly, 2),
        "outlook_label": outlook.get("outlook_label") or None,
        "outlook_score": round_value(outlook.get("outlook_score"), 2),  # type: ignore[arg-type]
        "outlook_window_start": outlook.get("outlook_window_start") or None,
        "outlook_window_end": outlook.get("outlook_window_end") or None,
        "outlook_release_date": outlook.get("outlook_release_date") or None,
        "outlook_weight_basis": outlook.get("outlook_weight_basis") or None,
    }


def csv_int(value: int | None) -> int | str:
    return value if value is not None else ""


def csv_float(value: float | None, digits: int) -> str:
    if value is None:
        return ""
    return f"{value:.{digits}f}"


def apportion_integer(total: int | None, weights: list[float]) -> list[int | None]:
    if total is None:
        return [None] * len(weights)
    if not weights:
        return []

    sign = -1 if total < 0 else 1
    absolute_total = abs(total)
    normalized = [max(0.0, float(weight)) for weight in weights]
    if sum(normalized) <= 0:
        normalized = [1.0] * len(weights)

    total_weight = sum(normalized)
    exact = [(absolute_total * weight) / total_weight for weight in normalized]
    floors = [math.floor(value) for value in exact]
    remainder = absolute_total - sum(floors)
    order = sorted(
        range(len(exact)),
        key=lambda idx: (exact[idx] - floors[idx], normalized[idx], -idx),
        reverse=True,
    )
    for idx in order[:remainder]:
        floors[idx] += 1
    return [sign * value for value in floors]


def unit_allocation_weights(
    unit_codes: list[str],
    geo_code: str,
    unit_outlooks_by_geo: dict[str, dict[str, dict[str, object]]],
) -> list[float]:
    weights: list[float] = []
    for unit_code in unit_codes:
        weight = unit_outlooks_by_geo.get(geo_code, {}).get(unit_code, {}).get("employment_weight")
        if weight in (None, 0):
            weight = unit_outlooks_by_geo.get(DEFAULT_GEO_CODE, {}).get(unit_code, {}).get("employment_weight")
        weights.append(float(weight) if weight not in (None, "") else 0.0)
    return weights


def build_metric_note() -> str:
    return (
        "StatCan annual labour-force and wage tables do not publish this official NOC 2021 unit group "
        "directly. Labour-market counts are estimated by allocating the published StatCan annual occupation "
        "tables across official unit groups using ESDC outlook employment weights. Rates and wage fields "
        "inherit published source-group values until a direct canonical StatCan release is added."
    )


def build_source_group_unit_map(
    source_group_codes: list[str],
    official_unit_codes: list[str],
) -> tuple[dict[str, str], dict[str, list[str]]]:
    unit_to_source_group: dict[str, str] = {}
    source_units_by_group: dict[str, list[str]] = {}

    for source_group_code in source_group_codes:
        prefixes = expand_group_prefixes(source_group_code)
        matched_unit_codes = sorted(
            code for code in official_unit_codes if any(code.startswith(prefix) for prefix in prefixes)
        )
        if not matched_unit_codes:
            raise ValueError(f"Published source group {source_group_code!r} did not match any official unit groups")

        source_units_by_group[source_group_code] = matched_unit_codes
        for unit_code in matched_unit_codes:
            if unit_code in unit_to_source_group:
                raise ValueError(f"Unit group {unit_code} is covered more than once in the source allocation map")
            unit_to_source_group[unit_code] = source_group_code

    uncovered_unit_codes = sorted(code for code in official_unit_codes if code not in unit_to_source_group)
    if uncovered_unit_codes:
        raise ValueError(
            "Published source-group allocation does not cover all canonical unit groups: "
            + ", ".join(uncovered_unit_codes[:10])
        )

    return unit_to_source_group, source_units_by_group


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

    source_groups: dict[str, dict[str, object]] = {}
    for label in common_labels:
        member = employment_leaves[label]
        source_group_code = member.code.strip("[]")
        source_groups[source_group_code] = {
            "title": member.name,
            "noc_code": source_group_code,
            "category": top_level_category(member.member_id, employment_members, employment_root_id),
            "employment_url": STATCAN_PAGE_URLS["employment"],
            "wages_url": STATCAN_PAGE_URLS["wages"],
            "raw_geo_metrics": empty_geo_metrics(),
        }

    source_outlooks_by_geo, _ = load_group_outlooks(list(source_groups))
    epiac_by_group, _ = load_group_epiac(list(source_groups))

    employment_years_by_geo = {geo_code: set() for geo_code in GEO_CODES}
    wage_years_by_geo = {geo_code: set() for geo_code in GEO_CODES}

    with employment_csv.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            geo_code = STATCAN_GEO_TO_CODE.get(row["GEO"])
            if not geo_code:
                continue
            label = row["National Occupational Classification (NOC)"]
            if label not in employment_leaves:
                continue
            source_group_code = employment_leaves[label].code.strip("[]")
            measure = row["Labour force characteristics"]
            if measure not in EMPLOYMENT_MEASURES:
                continue
            year = int(row["REF_DATE"])
            value = parse_float(row["VALUE"])
            if value is None:
                continue

            employment_years_by_geo[geo_code].add(year)
            geo_metrics = source_groups[source_group_code]["raw_geo_metrics"][geo_code]
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
            if label not in wage_leaves:
                continue
            source_group_code = wage_leaves[label].code.strip("[]")
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
            source_groups[source_group_code]["raw_geo_metrics"][geo_code][key][year] = value

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
            to_people(record["raw_geo_metrics"][geo_code]["employment"].get(jobs_year_by_geo[geo_code])) or 0
            for record in source_groups.values()
        )
        if jobs_year_by_geo[geo_code] is not None
        else 0
        for geo_code in GEO_CODES
    }

    canada_jobs_year = jobs_year_by_geo[DEFAULT_GEO_CODE]
    canada_wages_year = wages_year_by_geo[DEFAULT_GEO_CODE]
    if canada_jobs_year is None or canada_wages_year is None:
        raise ValueError("Canada-wide data is required for canonical outputs")

    for source_group_code, record in source_groups.items():
        stats_by_geo_output: dict[str, dict[str, object]] = {}
        for geo_code in GEO_CODES:
            stats_by_geo_output[geo_code] = build_geo_snapshot(
                record["raw_geo_metrics"][geo_code],
                jobs_year_by_geo[geo_code],
                wages_year_by_geo[geo_code],
                baseline_year,
                total_latest_jobs_by_geo[geo_code],
                source_outlooks_by_geo.get(geo_code, {}).get(source_group_code, {}),
            )
        record["stats_by_geo"] = stats_by_geo_output
        record["epiac"] = epiac_by_group.get(source_group_code, {})

    official_noc = load_official_noc_structure()
    oasis_artifact = build_and_write_oasis_artifacts()
    oasis_unit_groups = unit_group_lookup(oasis_artifact)
    oasis_profiles_by_unit = profiles_by_unit_group(oasis_artifact)
    oasis_meta = oasis_artifact["meta"]
    unit_outlooks_by_geo, unit_outlook_meta = load_unit_outlooks()
    official_unit_codes = [str(unit["code"]) for unit in official_noc["unit_groups"]]
    unit_to_source_group, source_units_by_group = build_source_group_unit_map(
        sorted(source_groups),
        official_unit_codes,
    )

    canonical_fieldnames = [
        "title",
        "category",
        "slug",
        "noc_code",
        "broad_category_code",
        "broad_category_title",
        "major_group_code",
        "major_group_title",
        "sub_major_group_code",
        "sub_major_group_title",
        "minor_group_code",
        "minor_group_title",
        "definition",
        "metric_source_kind",
        "metric_source_note",
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
        "oasis_profile_count",
        "oasis_profile_codes",
        "oasis_mapping_kind",
        "url",
        "employment_url",
        "wages_url",
        "stats_by_geo_json",
    ]

    metric_note = build_metric_note()
    canonical_records: dict[str, dict[str, object]] = {}
    for unit in official_noc["unit_groups"]:
        unit_code = str(unit["code"])
        source_group_code = unit_to_source_group[unit_code]
        source_record = source_groups[source_group_code]
        source_epiac = source_record["epiac"]
        oasis_unit_group = oasis_unit_groups[unit_code]
        canonical_records[unit_code] = {
            "title": unit["title"],
            "category": unit["broad_category_title"],
            "slug": slugify_code(unit_code),
            "noc_code": unit_code,
            "broad_category_code": unit["broad_category_code"],
            "broad_category_title": unit["broad_category_title"],
            "major_group_code": unit["major_group_code"],
            "major_group_title": unit["major_group_title"],
            "sub_major_group_code": unit["sub_major_group_code"],
            "sub_major_group_title": unit["sub_major_group_title"],
            "minor_group_code": unit["minor_group_code"],
            "minor_group_title": unit["minor_group_title"],
            "definition": unit["definition"] or "",
            "metric_source_kind": "published_annual_group_allocation",
            "metric_source_note": metric_note,
            "epiac_reference_year": source_epiac.get("epiac_reference_year"),
            "epiac_display_score": source_epiac.get("epiac_display_score"),
            "epiac_high_exposure_pct": source_epiac.get("epiac_high_exposure_pct"),
            "epiac_helc_pct": source_epiac.get("epiac_helc_pct"),
            "epiac_hehc_pct": source_epiac.get("epiac_hehc_pct"),
            "epiac_low_pct": source_epiac.get("epiac_low_pct"),
            "epiac_aioe": source_epiac.get("epiac_aioe"),
            "epiac_complementarity": source_epiac.get("epiac_complementarity"),
            "epiac_caioe": source_epiac.get("epiac_caioe"),
            "epiac_group_code": source_epiac.get("epiac_group_code"),
            "epiac_group_label": source_epiac.get("epiac_group_label"),
            "epiac_source_title": source_epiac.get("epiac_source_title"),
            "epiac_source_url": source_epiac.get("epiac_source_url"),
            "epiac_source_note": str(source_epiac.get("epiac_source_note", "")),
            "epiac_source_groups": source_epiac.get("epiac_source_groups", []),
            "oasis_profile_count": oasis_unit_group["profile_count"],
            "oasis_profile_codes": oasis_unit_group["profile_codes"],
            "oasis_mapping_kind": oasis_unit_group["mapping_kind"],
            "url": str(official_noc["source_page_url"]),
            "employment_url": source_record["employment_url"],
            "wages_url": source_record["wages_url"],
            "stats_by_geo": {},
        }

    for geo_code in GEO_CODES:
        for source_group_code, unit_codes in source_units_by_group.items():
            source_stats = source_groups[source_group_code]["stats_by_geo"][geo_code]
            weights = unit_allocation_weights(unit_codes, geo_code, unit_outlooks_by_geo)
            job_allocations = apportion_integer(source_stats["jobs"], weights)
            employee_allocations = apportion_integer(source_stats["employees"], weights)
            change_allocations = apportion_integer(source_stats["employment_change_abs"], weights)
            for idx, unit_code in enumerate(unit_codes):
                unit_outlook = unit_outlooks_by_geo.get(geo_code, {}).get(unit_code, {})
                canonical_records[unit_code]["stats_by_geo"][geo_code] = {
                    "jobs": job_allocations[idx],
                    "jobs_year": source_stats["jobs_year"],
                    "trend_pct": source_stats["trend_pct"],
                    "trend_from_year": source_stats["trend_from_year"],
                    "employment_change_abs": change_allocations[idx],
                    "unemployment_rate": source_stats["unemployment_rate"],
                    "employment_share_pct": None,
                    "men_share_pct": source_stats["men_share_pct"],
                    "women_share_pct": source_stats["women_share_pct"],
                    "employees": employee_allocations[idx],
                    "pay_hourly": source_stats["pay_hourly"],
                    "pay_weekly": source_stats["pay_weekly"],
                    "average_hourly_wage": source_stats["average_hourly_wage"],
                    "average_weekly_wage": source_stats["average_weekly_wage"],
                    "outlook_label": unit_outlook.get("outlook_label") or None,
                    "outlook_score": round_value(unit_outlook.get("outlook_score"), 2),  # type: ignore[arg-type]
                    "outlook_window_start": unit_outlook_meta["window_start"],
                    "outlook_window_end": unit_outlook_meta["window_end"],
                    "outlook_release_date": unit_outlook.get("release_date") or unit_outlook_meta["release_date"],
                    "outlook_weight_basis": "unit_group_outlook",
                }

        geo_total_jobs = sum(
            stats.get("jobs") or 0
            for record in canonical_records.values()
            for stats in [record["stats_by_geo"][geo_code]]
        )
        for record in canonical_records.values():
            stats = record["stats_by_geo"][geo_code]
            if stats["jobs"] is not None and geo_total_jobs:
                stats["employment_share_pct"] = round((stats["jobs"] / geo_total_jobs) * 100, 1)

    canonical_rows: list[dict[str, object]] = []
    occupations_index: list[dict[str, object]] = []
    for unit_code, record in canonical_records.items():
        canada_stats = record["stats_by_geo"][DEFAULT_GEO_CODE]
        row = {
            "title": record["title"],
            "category": record["category"],
            "slug": record["slug"],
            "noc_code": unit_code,
            "broad_category_code": record["broad_category_code"],
            "broad_category_title": record["broad_category_title"],
            "major_group_code": record["major_group_code"],
            "major_group_title": record["major_group_title"],
            "sub_major_group_code": record["sub_major_group_code"],
            "sub_major_group_title": record["sub_major_group_title"],
            "minor_group_code": record["minor_group_code"],
            "minor_group_title": record["minor_group_title"],
            "definition": record["definition"],
            "metric_source_kind": record["metric_source_kind"],
            "metric_source_note": record["metric_source_note"],
            "data_year": csv_int(canada_stats["jobs_year"]),
            "trend_from_year": csv_int(canada_stats["trend_from_year"]),
            "num_jobs": csv_int(canada_stats["jobs"]),
            "unemployment_rate": csv_float(canada_stats["unemployment_rate"], 1),
            "employment_share_pct": csv_float(canada_stats["employment_share_pct"], 1),
            "employment_change_pct": csv_float(canada_stats["trend_pct"], 1),
            "employment_change_abs": csv_int(canada_stats["employment_change_abs"]),
            "men_share_pct": csv_float(canada_stats["men_share_pct"], 1),
            "women_share_pct": csv_float(canada_stats["women_share_pct"], 1),
            "num_employees": csv_int(canada_stats["employees"]),
            "average_hourly_wage": csv_float(canada_stats["average_hourly_wage"], 2),
            "average_weekly_wage": csv_float(canada_stats["average_weekly_wage"], 2),
            "median_hourly_wage": csv_float(canada_stats["pay_hourly"], 2),
            "median_weekly_wage": csv_float(canada_stats["pay_weekly"], 2),
            "outlook_label": canada_stats["outlook_label"] or "",
            "outlook_score": csv_float(canada_stats["outlook_score"], 2),
            "outlook_window_start": csv_int(canada_stats["outlook_window_start"]),
            "outlook_window_end": csv_int(canada_stats["outlook_window_end"]),
            "outlook_release_date": canada_stats["outlook_release_date"] or "",
            "outlook_source_url": str(unit_outlook_meta["page_url"]),
            "epiac_reference_year": record["epiac_reference_year"] or "",
            "epiac_display_score": record["epiac_display_score"] or "",
            "epiac_high_exposure_pct": csv_float(record["epiac_high_exposure_pct"], 1),
            "epiac_helc_pct": csv_float(record["epiac_helc_pct"], 1),
            "epiac_hehc_pct": csv_float(record["epiac_hehc_pct"], 1),
            "epiac_low_pct": csv_float(record["epiac_low_pct"], 1),
            "epiac_aioe": csv_float(record["epiac_aioe"], 4),
            "epiac_complementarity": csv_float(record["epiac_complementarity"], 4),
            "epiac_caioe": csv_float(record["epiac_caioe"], 4),
            "epiac_group_code": record["epiac_group_code"] or "",
            "epiac_group_label": record["epiac_group_label"] or "",
            "epiac_source_title": record["epiac_source_title"] or "",
            "epiac_source_url": record["epiac_source_url"] or "",
            "epiac_source_note": record["epiac_source_note"] or "",
            "epiac_source_groups": "; ".join(record["epiac_source_groups"]),
            "oasis_profile_count": csv_int(record["oasis_profile_count"]),
            "oasis_profile_codes": "; ".join(record["oasis_profile_codes"]),
            "oasis_mapping_kind": record["oasis_mapping_kind"],
            "url": record["url"],
            "employment_url": record["employment_url"],
            "wages_url": record["wages_url"],
            "stats_by_geo_json": json.dumps(
                record["stats_by_geo"],
                ensure_ascii=True,
                separators=(",", ":"),
            ),
        }
        canonical_rows.append(row)
        occupations_index.append(
            {
                "title": record["title"],
                "category": record["category"],
                "slug": record["slug"],
                "noc_code": unit_code,
                "broad_category_code": record["broad_category_code"],
                "major_group_code": record["major_group_code"],
                "major_group_title": record["major_group_title"],
                "outlook_label": row["outlook_label"],
                "outlook_score": row["outlook_score"],
                "epiac_display_score": row["epiac_display_score"],
                "epiac_group_label": row["epiac_group_label"],
                "epiac_high_exposure_pct": row["epiac_high_exposure_pct"],
                "oasis_profile_count": row["oasis_profile_count"],
                "oasis_mapping_kind": row["oasis_mapping_kind"],
                "url": record["url"],
            }
        )

    canonical_rows.sort(key=lambda row: str(row["noc_code"]))
    occupations_index.sort(key=lambda row: str(row["noc_code"]))

    with CANONICAL_CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=canonical_fieldnames)
        writer.writeheader()
        writer.writerows(canonical_rows)

    with CANONICAL_INDEX_PATH.open("w", encoding="utf-8") as handle:
        json.dump(occupations_index, handle, indent=2)

    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    for record in canonical_records.values():
        canada_stats = record["stats_by_geo"][DEFAULT_GEO_CODE]
        lines = [
            f"# {record['title']}",
            "",
            f"- NOC 2021 unit group: {record['noc_code']}",
            f"- Broad category: {record['broad_category_code']} {record['broad_category_title']}",
            f"- Major group: {record['major_group_code']} {record['major_group_title']}",
            f"- Sub-major group: {record['sub_major_group_code']} {record['sub_major_group_title']}",
            f"- Minor group: {record['minor_group_code']} {record['minor_group_title']}",
            f"- Employment in Canada ({canada_jobs_year} estimate): {fmt_number(canada_stats['jobs'])}",
            f"- Unemployment rate ({canada_jobs_year} published-source rate): {fmt_percent(canada_stats['unemployment_rate'])}",
            f"- Share of total Canadian employment ({canada_jobs_year} estimate): {fmt_percent(canada_stats['employment_share_pct'])}",
            f"- Employment change ({baseline_year} to {canada_jobs_year} published-source rate): {fmt_percent(canada_stats['trend_pct'])} ({fmt_number(canada_stats['employment_change_abs'])})",
            f"- Men+ share of employment ({canada_jobs_year} published-source rate): {fmt_percent(canada_stats['men_share_pct'])}",
            f"- Women+ share of employment ({canada_jobs_year} published-source rate): {fmt_percent(canada_stats['women_share_pct'])}",
            f"- Median hourly wage ({canada_wages_year} published-source rate): {fmt_currency(canada_stats['pay_hourly'])}",
            f"- StatCan EPIAC high-exposure share ({record['epiac_reference_year']} mapped): {fmt_percent(record['epiac_high_exposure_pct'])}",
            f"- Dominant EPIAC group: {record['epiac_group_label'] or '-'}",
            f"- Average AIOE / complementarity ({record['epiac_reference_year']} mapped): {(record['epiac_aioe'] or 0):.2f} / {(record['epiac_complementarity'] or 0):.2f}",
            f"- Employment outlook ({unit_outlook_meta['window_start']} to {unit_outlook_meta['window_end']}): {canada_stats['outlook_label'] or '-'}",
            f"- Attached OaSIS occupational profiles: {record['oasis_profile_count']}",
            f"- Median weekly wage ({canada_wages_year} published-source rate): {fmt_currency(canada_stats['pay_weekly'])}",
            f"- Average hourly wage ({canada_wages_year} published-source rate): {fmt_currency(canada_stats['average_hourly_wage'])}",
            f"- Average weekly wage ({canada_wages_year} published-source rate): {fmt_currency(canada_stats['average_weekly_wage'])}",
            "",
            "## Official definition",
            "",
            record["definition"] or "Definition unavailable.",
            "",
            "## Methodology notes",
            "",
            record["metric_source_note"],
            "",
            record["epiac_source_note"],
            "",
        ]
        lines.extend(
            build_oasis_page_lines(
                str(record["noc_code"]),
                oasis_meta,
                oasis_unit_groups[str(record["noc_code"])],
                oasis_profiles_by_unit.get(str(record["noc_code"]), []),
            )
        )
        lines.extend(
            [
                "",
                "## Source tables",
                "",
                f"- Official NOC 2021 classification structure: {official_noc['source_url']}",
                f"- Labour force characteristics by occupation, annual: {record['employment_url']}",
                f"- Employee wages by occupation, annual: {record['wages_url']}",
                f"- {record['epiac_source_title']}: {record['epiac_source_url']}",
                f"- {unit_outlook_meta['title']}: {unit_outlook_meta['page_url']}",
                f"- {oasis_meta['title']}: {oasis_meta['package_url']}",
                "",
                "## Geography coverage note",
                "",
                "The StatCan occupation tables in this project cover Canada and the provinces only. Yukon, the Northwest Territories, and Nunavut remain in the generated geography metadata, but labour-market metrics for those selectors are left unavailable rather than backfilled.",
            ]
        )
        (PAGES_DIR / f"{record['slug']}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {len(canonical_rows)} canonical unit groups to {CANONICAL_CSV_PATH}")
    print(f"Wrote {len(occupations_index)} canonical occupation entries to {CANONICAL_INDEX_PATH}")
    print(
        "Wrote "
        f"{oasis_meta['profile_count']} OaSIS profiles across {oasis_meta['unit_group_count']} unit groups to oasis.json"
    )
    print("Wrote explicit OaSIS profile mappings to oasis_profile_mappings.csv")
    print(f"Wrote {len(canonical_rows)} markdown summaries to {PAGES_DIR}/")
    print("Geography coverage:")
    print("  - Labour-market data: Canada and 10 provinces")
    print("  - Outlook-only metadata: Yukon, Northwest Territories, Nunavut")
    total_jobs = sum(int(row["num_jobs"]) for row in canonical_rows if row["num_jobs"])
    print(f"Latest employment represented ({canada_jobs_year}): {total_jobs:,}")


if __name__ == "__main__":
    main()
