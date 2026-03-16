"""
Discover, cache, and normalize the latest official OaSIS release.

OaSIS profile codes are anchored to the official five-digit NOC 2021 unit-group
codes. This module resolves the latest package from the Open Government CKAN
API, caches the English CSV resources needed for the profile layer, and writes
generated artifacts with explicit profile-to-unit mappings and audit metadata.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import urlopen

from noc_hierarchy import load_official_noc_structure


OASIS_DIR = Path("tmp/oasis")
OASIS_ARTIFACT_PATH = Path("oasis.json")
OASIS_PROFILE_MAPPING_PATH = Path("oasis_profile_mappings.csv")

OASIS_PACKAGE_SEARCH_ENDPOINT = "https://open.canada.ca/data/api/action/package_search"
OASIS_PACKAGE_SHOW_ENDPOINT = "https://open.canada.ca/data/api/action/package_show"
OASIS_PACKAGE_PAGE_TEMPLATE = "https://open.canada.ca/data/en/dataset/{package_id}"

PACKAGE_QUERY = '"Occupational and Skills Information System (OaSIS)"'
PACKAGE_TITLE_RE = re.compile(
    r"^Occupational and Skills Information System \(OaSIS\)\s*-?\s*(?P<year>\d{4})\s+Version\s+(?P<version>\d+(?:\.\d+)*)$",
    re.IGNORECASE,
)
PROFILE_CODE_RE = re.compile(r"^(?P<noc_code>\d{5})\.(?P<suffix>\d{2})$")

RESOURCE_KEY_PATTERNS = {
    "additional_information": ("additionalinformation",),
    "core_competencies": ("corecompetencies",),
    "employment_requirements": ("employmentrequirements",),
    "example_titles": ("exampletitles",),
    "exclusions": ("exclusions",),
    "labels": ("labels",),
    "lead_statement": ("leadstatement",),
    "main_duties": ("mainduties",),
    "workplaces_employers": ("workplacesemployers",),
}


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def _normalize_resource_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _version_tuple(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in value.split("."))


def _json_request(url: str) -> dict[str, object]:
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def _download_file(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(url) as response, destination.open("wb") as output:
        output.write(response.read())


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _resource_language(resource: dict[str, object]) -> str:
    language = resource.get("language")
    if isinstance(language, list):
        if not language:
            return ""
        return str(language[0]).lower()
    return str(language or "").lower()


def _parse_package_identity(package: dict[str, object]) -> dict[str, object]:
    title = str(package.get("title") or "").strip()
    match = PACKAGE_TITLE_RE.match(title)
    if not match:
        raise ValueError(f"Unexpected OaSIS package title format: {title!r}")
    version = match.group("version")
    return {
        "title": title,
        "year": int(match.group("year")),
        "version": version,
        "version_tuple": _version_tuple(version),
    }


def discover_latest_oasis_package() -> dict[str, object]:
    search_url = f"{OASIS_PACKAGE_SEARCH_ENDPOINT}?{urlencode({'q': PACKAGE_QUERY, 'rows': 50})}"
    payload = _json_request(search_url)
    result = payload.get("result")
    if not isinstance(result, dict):
        raise ValueError("CKAN package_search response did not contain a result object")

    candidates: list[dict[str, object]] = []
    for package in result.get("results", []):
        if not isinstance(package, dict):
            continue
        title = str(package.get("title") or "").strip()
        if not PACKAGE_TITLE_RE.match(title):
            continue
        identity = _parse_package_identity(package)
        candidates.append({**package, **identity})

    if not candidates:
        raise ValueError("No official OaSIS packages were returned by the CKAN API")

    latest = max(
        candidates,
        key=lambda package: (
            int(package["year"]),
            tuple(package["version_tuple"]),
            str(package.get("metadata_modified") or ""),
            str(package.get("metadata_created") or ""),
        ),
    )
    latest["package_search_url"] = search_url
    latest["package_search_fetched_at_utc"] = _now_utc()
    return latest


def _package_dir(package: dict[str, object]) -> Path:
    version_slug = str(package["version"]).replace(".", "-")
    return OASIS_DIR / f"{package['year']}-v{version_slug}-{package['id']}"


def _english_csv_resources(package: dict[str, object]) -> list[dict[str, object]]:
    resources = []
    for resource in package.get("resources", []):
        if not isinstance(resource, dict):
            continue
        if str(resource.get("format") or "").upper() != "CSV":
            continue
        if _resource_language(resource) != "en":
            continue
        resources.append(resource)
    if not resources:
        raise ValueError("Latest OaSIS package did not expose any English CSV resources")
    return resources


def _resource_key(name: str) -> str | None:
    normalized = _normalize_resource_name(name)
    for key, patterns in RESOURCE_KEY_PATTERNS.items():
        if any(pattern in normalized for pattern in patterns):
            return key
    return None


def _cache_package_json(package: dict[str, object], package_dir: Path) -> Path:
    package_path = package_dir / "package.json"
    package_dir.mkdir(parents=True, exist_ok=True)
    with package_path.open("w", encoding="utf-8") as handle:
        json.dump(package, handle, indent=2, ensure_ascii=True)
    return package_path


def _cache_resources(package: dict[str, object], package_dir: Path) -> list[dict[str, object]]:
    cached_resources: list[dict[str, object]] = []
    for resource in sorted(_english_csv_resources(package), key=lambda item: str(item.get("name") or "")):
        parsed = urlparse(str(resource["url"]))
        basename = Path(parsed.path).name or f"{resource['id']}.csv"
        cached_path = package_dir / "resources" / f"{resource['id']}-{basename}"
        if not cached_path.exists():
            print(f"Downloading OaSIS resource {resource['name']} from {resource['url']}")
            _download_file(str(resource["url"]), cached_path)
        cached_resources.append(
            {
                "id": str(resource.get("id") or ""),
                "name": str(resource.get("name") or ""),
                "format": str(resource.get("format") or ""),
                "language": _resource_language(resource),
                "url": str(resource.get("url") or ""),
                "key": _resource_key(str(resource.get("name") or "")),
                "cache_path": str(cached_path),
                "bytes": cached_path.stat().st_size,
                "sha256": _sha256(cached_path),
                "cached_at_utc": datetime.fromtimestamp(cached_path.stat().st_mtime, tz=timezone.utc).isoformat(),
            }
        )
    return cached_resources


def _load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        sample = handle.read(4096)
        handle.seek(0)
        delimiter = ";"
        if sample.count(",") > sample.count(";"):
            delimiter = ","
        reader = csv.DictReader(handle, delimiter=delimiter)
        return [{key.strip(): (value or "").strip() for key, value in row.items()} for row in reader]


def _resource_rows(cached_resources: list[dict[str, object]]) -> dict[str, list[dict[str, str]]]:
    rows_by_key: dict[str, list[dict[str, str]]] = {}
    for resource in cached_resources:
        key = resource.get("key")
        if not key:
            continue
        cache_path = Path(str(resource["cache_path"]))
        rows_by_key[str(key)] = _load_csv_rows(cache_path)
    return rows_by_key


def _group_values(rows: list[dict[str, str]], code_field: str, value_field: str) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        code = row.get(code_field, "").strip()
        value = row.get(value_field, "").strip()
        if code and value:
            grouped[code].append(value)
    return dict(grouped)


def _group_example_titles(rows: list[dict[str, str]]) -> dict[str, list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        code = row.get("OaSIS profile code", "").strip()
        if not code:
            continue
        concordance_raw = row.get("Concordance number", "").strip()
        concordance = int(concordance_raw) if concordance_raw.isdigit() else None
        grouped[code].append(
            {
                "concordance_number": concordance,
                "job_title_type": row.get("Job title type", "").strip() or None,
                "job_title_text": row.get("Job title text", "").strip(),
            }
        )
    return dict(grouped)


def _group_exclusions(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        code = row.get("OaSIS profile code", "").strip()
        excluded_code = row.get("Excluded code", "").strip()
        job_title = row.get("Job title", "").strip()
        if code and (excluded_code or job_title):
            grouped[code].append(
                {
                    "excluded_profile_code": excluded_code or None,
                    "job_title": job_title or None,
                }
            )
    return dict(grouped)


def _group_core_competencies(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        code = row.get("Code", "").strip()
        competency = row.get("Core Competencies - English", "").strip()
        statement = row.get("Competency Statements - English", "").strip()
        if code and (competency or statement):
            grouped[code].append(
                {
                    "competency": competency or None,
                    "statement": statement or None,
                }
            )
    return dict(grouped)


def _mapping_kind(profile_count: int) -> str:
    if profile_count <= 0:
        return "missing"
    if profile_count == 1:
        return "one_to_one"
    return "one_to_many"


def build_oasis_artifact(package: dict[str, object], cached_resources: list[dict[str, object]]) -> dict[str, object]:
    official_noc = load_official_noc_structure()
    unit_nodes = {str(unit["code"]): unit for unit in official_noc["unit_groups"]}
    rows_by_key = _resource_rows(cached_resources)

    labels_rows = rows_by_key.get("labels", [])
    if not labels_rows:
        raise ValueError("OaSIS labels resource is required to build profile mappings")

    labels_by_code = {
        row.get("OaSIS profile code", "").strip(): row.get("Label", "").strip()
        for row in labels_rows
        if row.get("OaSIS profile code", "").strip()
    }
    lead_statements = {
        row.get("OaSIS profile code", "").strip(): row.get("Lead statement", "").strip()
        for row in rows_by_key.get("lead_statement", [])
        if row.get("OaSIS profile code", "").strip()
    }
    main_duties = _group_values(rows_by_key.get("main_duties", []), "OaSIS profile code", "Main duties")
    employment_requirements = _group_values(
        rows_by_key.get("employment_requirements", []),
        "OaSIS profile code",
        "Employment requirement",
    )
    additional_information = _group_values(
        rows_by_key.get("additional_information", []),
        "OaSIS profile code",
        "Additional information (EN)",
    )
    workplaces_employers = _group_values(
        rows_by_key.get("workplaces_employers", []),
        "OaSIS profile code",
        "Workplace/employer name",
    )
    example_titles = _group_example_titles(rows_by_key.get("example_titles", []))
    exclusions = _group_exclusions(rows_by_key.get("exclusions", []))
    core_competencies = _group_core_competencies(rows_by_key.get("core_competencies", []))

    profiles: list[dict[str, object]] = []
    mapping_rows: list[dict[str, object]] = []
    unit_group_to_profiles: dict[str, list[str]] = defaultdict(list)
    unmapped_profiles: list[dict[str, str]] = []
    ambiguous_profiles: list[dict[str, str]] = []

    for profile_code in sorted(labels_by_code):
        match = PROFILE_CODE_RE.match(profile_code)
        if not match:
            unmapped_profiles.append(
                {
                    "oasis_profile_code": profile_code,
                    "reason": "Profile code did not match the expected NOC.suffix pattern",
                }
            )
            continue

        noc_code = match.group("noc_code")
        suffix = match.group("suffix")
        unit_node = unit_nodes.get(noc_code)
        if unit_node is None:
            unmapped_profiles.append(
                {
                    "oasis_profile_code": profile_code,
                    "reason": f"Profile prefix {noc_code} is not an official canonical unit group",
                }
            )
            continue

        unit_group_to_profiles[noc_code].append(profile_code)
        profile = {
            "oasis_profile_code": profile_code,
            "profile_title": labels_by_code[profile_code],
            "noc_code": noc_code,
            "unit_group_title": unit_node["title"],
            "profile_suffix": suffix,
            "is_unit_group_profile": suffix == "00",
            "mapping_status": "mapped",
            "mapping_method": "explicit_profile_prefix_to_canonical_unit_group",
            "lead_statement": lead_statements.get(profile_code) or None,
            "main_duties": main_duties.get(profile_code, []),
            "employment_requirements": employment_requirements.get(profile_code, []),
            "additional_information": additional_information.get(profile_code, []),
            "workplaces_employers": workplaces_employers.get(profile_code, []),
            "example_titles": example_titles.get(profile_code, []),
            "exclusions": exclusions.get(profile_code, []),
            "core_competencies": core_competencies.get(profile_code, []),
        }
        profiles.append(profile)
        mapping_rows.append(
            {
                "oasis_profile_code": profile_code,
                "noc_code": noc_code,
                "profile_title": labels_by_code[profile_code],
                "unit_group_title": unit_node["title"],
                "profile_suffix": suffix,
                "is_unit_group_profile": suffix == "00",
                "mapping_status": "mapped",
            }
        )

    unit_groups: list[dict[str, object]] = []
    for noc_code, unit_node in sorted(unit_nodes.items()):
        profile_codes = sorted(unit_group_to_profiles.get(noc_code, []))
        mapping_kind = _mapping_kind(len(profile_codes))
        unit_groups.append(
            {
                "noc_code": noc_code,
                "title": unit_node["title"],
                "broad_category_code": unit_node["broad_category_code"],
                "broad_category_title": unit_node["broad_category_title"],
                "major_group_code": unit_node["major_group_code"],
                "major_group_title": unit_node["major_group_title"],
                "sub_major_group_code": unit_node["sub_major_group_code"],
                "sub_major_group_title": unit_node["sub_major_group_title"],
                "minor_group_code": unit_node["minor_group_code"],
                "minor_group_title": unit_node["minor_group_title"],
                "profile_count": len(profile_codes),
                "profile_codes": profile_codes,
                "profile_titles": [labels_by_code[profile_code] for profile_code in profile_codes],
                "has_split_profiles": len(profile_codes) > 1,
                "has_unit_group_profile": f"{noc_code}.00" in profile_codes,
                "mapping_kind": mapping_kind,
            }
        )

    one_to_many_unit_group_count = sum(1 for unit_group in unit_groups if unit_group["profile_count"] > 1)
    unit_group_cardinality = {
        str(unit_group["noc_code"]): {
            "profile_count": int(unit_group["profile_count"]),
            "mapping_kind": str(unit_group["mapping_kind"]),
        }
        for unit_group in unit_groups
    }
    for row in mapping_rows:
        cardinality = unit_group_cardinality[str(row["noc_code"])]
        row["unit_group_profile_count"] = cardinality["profile_count"]
        row["mapping_kind"] = cardinality["mapping_kind"]
    profiles.sort(key=lambda item: str(item["oasis_profile_code"]))
    mapping_rows.sort(key=lambda item: str(item["oasis_profile_code"]))

    artifact = {
        "meta": {
            "title": package["title"],
            "resolved_year": package["year"],
            "resolved_version": package["version"],
            "package_id": package["id"],
            "package_url": OASIS_PACKAGE_PAGE_TEMPLATE.format(package_id=package["id"]),
            "package_api_url": f"{OASIS_PACKAGE_SHOW_ENDPOINT}?{urlencode({'id': str(package['id'])})}",
            "package_search_url": package["package_search_url"],
            "package_search_fetched_at_utc": package.get("package_search_fetched_at_utc"),
            "package_show_fetched_at_utc": package.get("package_show_fetched_at_utc"),
            "package_metadata_created": package.get("metadata_created"),
            "package_metadata_modified": package.get("metadata_modified"),
            "package_notes": package.get("notes") or "",
            "cache_dir": str(_package_dir(package)),
            "generated_at_utc": _now_utc(),
            "profile_count": len(profiles),
            "unit_group_count": len(unit_groups),
            "mapped_profile_count": len(mapping_rows),
            "unmapped_profile_count": len(unmapped_profiles),
            "ambiguous_profile_count": len(ambiguous_profiles),
            "one_to_many_unit_group_count": one_to_many_unit_group_count,
            "mapping_method": (
                "The explicit mapping table matches each OaSIS profile code's five-digit prefix to the "
                "official canonical NOC 2021 unit-group spine."
            ),
            "resources": cached_resources,
            "missing_expected_resources": sorted(
                key
                for key in RESOURCE_KEY_PATTERNS
                if key not in {str(resource.get('key')) for resource in cached_resources if resource.get('key')}
            ),
        },
        "unit_groups": unit_groups,
        "profiles": profiles,
        "reports": {
            "unmapped_profiles": unmapped_profiles,
            "ambiguous_profiles": ambiguous_profiles,
            "unit_groups_without_profiles": [unit_group["noc_code"] for unit_group in unit_groups if unit_group["profile_count"] == 0],
        },
        "mapping_rows": mapping_rows,
    }
    return artifact


def write_oasis_artifacts(artifact: dict[str, object]) -> None:
    with OASIS_ARTIFACT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(artifact, handle, indent=2, ensure_ascii=True)
        handle.write("\n")

    fieldnames = [
        "oasis_profile_code",
        "noc_code",
        "profile_title",
        "unit_group_title",
        "profile_suffix",
        "is_unit_group_profile",
        "unit_group_profile_count",
        "mapping_kind",
        "mapping_status",
    ]
    with OASIS_PROFILE_MAPPING_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(artifact["mapping_rows"])


def build_and_write_oasis_artifacts() -> dict[str, object]:
    latest_package = discover_latest_oasis_package()
    package_show_url = f"{OASIS_PACKAGE_SHOW_ENDPOINT}?{urlencode({'id': str(latest_package['id'])})}"
    package_payload = _json_request(package_show_url)
    package_result = package_payload.get("result")
    if not isinstance(package_result, dict):
        raise ValueError("CKAN package_show response did not contain a result object")

    package = {**package_result, **_parse_package_identity(package_result)}
    package["package_search_url"] = latest_package["package_search_url"]
    package["package_search_fetched_at_utc"] = latest_package["package_search_fetched_at_utc"]
    package["package_show_fetched_at_utc"] = _now_utc()

    package_dir = _package_dir(package)
    _cache_package_json(package, package_dir)
    cached_resources = _cache_resources(package, package_dir)
    artifact = build_oasis_artifact(package, cached_resources)
    write_oasis_artifacts(artifact)
    return artifact


def load_oasis_artifact() -> dict[str, object] | None:
    if not OASIS_ARTIFACT_PATH.exists():
        return None
    with OASIS_ARTIFACT_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def unit_group_lookup(artifact: dict[str, object]) -> dict[str, dict[str, object]]:
    return {str(unit_group["noc_code"]): unit_group for unit_group in artifact["unit_groups"]}


def profiles_by_unit_group(artifact: dict[str, object]) -> dict[str, list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for profile in artifact["profiles"]:
        grouped[str(profile["noc_code"])].append(profile)
    for profiles in grouped.values():
        profiles.sort(key=lambda item: str(item["oasis_profile_code"]))
    return dict(grouped)
