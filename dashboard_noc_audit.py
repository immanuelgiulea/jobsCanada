"""
Audit the current 43-group dashboard against the official NOC 2021 hierarchy.

This module treats the 516 NOC 2021 unit groups found in the ESDC outlook
workbook as the local canonical spine. It then measures how the current
dashboard groups partition that spine and renders a markdown concordance.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from outlook_data import expand_group_prefixes, load_unit_group_catalog


OCCUPATIONS_PATH = Path("occupations.csv")
DOC_OUTPUT_PATH = Path("docs/dashboard-to-noc-2021.md")

OFFICIAL_BROAD_CATEGORIES = {
    "0": "Legislative and senior management occupations",
    "1": "Business, finance and administration occupations",
    "2": "Natural and applied sciences and related occupations",
    "3": "Health occupations",
    "4": "Occupations in education, law and social, community and government services",
    "5": "Occupations in art, culture, recreation and sport",
    "6": "Sales and service occupations",
    "7": "Trades, transport and equipment operators and related occupations",
    "8": "Natural resources, agriculture and related production occupations",
    "9": "Occupations in manufacturing and utilities",
}

DASHBOARD_FAMILY_VARIANT_SECTIONS = {
    "Management occupations": {"code": "L0", "title": "Management occupations"},
    "Business, finance and administration occupations, except management": {
        "code": "L1",
        "title": "Business, finance and administration occupations, except management",
    },
    "Natural and applied sciences and related occupations, except management": {
        "code": "L2",
        "title": "Natural and applied sciences and related occupations, except management",
    },
    "Health occupations, except management": {
        "code": "L3",
        "title": "Health occupations, except management",
    },
    "Occupations in education, law and social, community and government services, except management": {
        "code": "L4",
        "title": "Occupations in education, law and social, community and government services, except management",
    },
    "Occupations in art, culture, recreation and sport, except management": {
        "code": "L5",
        "title": "Occupations in art, culture, recreation and sport, except management",
    },
    "Sales and service occupations, except management": {
        "code": "L6",
        "title": "Sales and service occupations, except management",
    },
    "Trades, transport and equipment operators and related occupations, except management": {
        "code": "L7",
        "title": "Trades, transport and equipment operators and related occupations, except management",
    },
    "Natural resources, agriculture and related production occupations, except management": {
        "code": "L8",
        "title": "Natural resources, agriculture and related production occupations, except management",
    },
    "Occupations in manufacturing and utilities, except management": {
        "code": "L9",
        "title": "Occupations in manufacturing and utilities, except management",
    },
}

GROUP_KIND_LABELS = {
    "exact_broad_category": "Exact official broad category",
    "exact_major_group": "Exact official major group",
    "exact_sub_major_group": "Exact official sub-major group",
    "custom_multi_major_group_merge": "Custom merge of major groups within one broad category",
    "custom_cross_broad_major_group_merge": "Custom cross-broad merge of major groups",
    "custom_dashboard_merge": "Custom dashboard merge",
}

SOURCE_LINKS = [
    (
        "NOC 2021 V1 classification structure",
        "https://www.statcan.gc.ca/en/subjects/standard/noc/2021/indexV1",
    ),
    (
        "NOC 2021 V1 variant: Aggregates for Analysis of labour force",
        "https://www.statcan.gc.ca/en/subjects/standard/noc/2021/indexV1/noc-2021-v1.0-variant-aggregates-analysis-labour-force",
    ),
    (
        "ESDC 2025-2027 Employment Outlooks - NOC 2021",
        "https://open.canada.ca/data/en/dataset/b0e112e9-cf53-4e79-8838-23cd98debe5b/resource/cb52e1d0-ab62-4357-91cc-d8f5a2114e02",
    ),
]


def classify_group_kind(prefixes: list[str]) -> str:
    if len(prefixes) == 1 and len(prefixes[0]) == 1:
        return "exact_broad_category"
    if len(prefixes) == 1 and len(prefixes[0]) == 2:
        return "exact_major_group"
    if len(prefixes) == 1 and len(prefixes[0]) == 3:
        return "exact_sub_major_group"
    if prefixes and all(len(prefix) == 2 for prefix in prefixes):
        if len({prefix[0] for prefix in prefixes}) == 1:
            return "custom_multi_major_group_merge"
        return "custom_cross_broad_major_group_merge"
    return "custom_dashboard_merge"


def load_dashboard_groups(occupations_path: Path = OCCUPATIONS_PATH) -> list[dict[str, str]]:
    with occupations_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"{occupations_path} is empty")
    return rows


def build_dashboard_noc_audit(occupations_path: Path = OCCUPATIONS_PATH) -> dict[str, object]:
    dashboard_rows = load_dashboard_groups(occupations_path)
    unit_catalog = load_unit_group_catalog()
    unit_codes = sorted(unit_catalog)

    coverage: dict[str, list[str]] = defaultdict(list)
    group_summaries: list[dict[str, object]] = []

    for row in dashboard_rows:
        prefixes = expand_group_prefixes(row["noc_code"])
        matched_codes = sorted(
            code for code in unit_codes if any(code.startswith(prefix) for prefix in prefixes)
        )
        broad_codes = sorted({code[:1] for code in matched_codes})
        for code in matched_codes:
            coverage[code].append(row["noc_code"])

        group_kind = classify_group_kind(prefixes)
        family_section = DASHBOARD_FAMILY_VARIANT_SECTIONS[row["category"]]
        group_summaries.append(
            {
                "dashboard_group_code": row["noc_code"],
                "dashboard_group_title": row["title"],
                "dashboard_family": row["category"],
                "dashboard_family_variant_section_code": family_section["code"],
                "dashboard_family_variant_section_title": family_section["title"],
                "group_prefixes": prefixes,
                "mapping_kind": group_kind,
                "mapping_kind_label": GROUP_KIND_LABELS[group_kind],
                "official_broad_category_codes": broad_codes,
                "official_broad_category_titles": [OFFICIAL_BROAD_CATEGORIES[code] for code in broad_codes],
                "official_major_group_count": len({code[:2] for code in matched_codes}),
                "official_sub_major_group_count": len({code[:3] for code in matched_codes}),
                "official_minor_group_count": len({code[:4] for code in matched_codes}),
                "official_unit_group_count": len(matched_codes),
            }
        )

    uncovered_codes = sorted(code for code in unit_codes if code not in coverage)
    overlapping_codes = sorted(code for code, groups in coverage.items() if len(groups) > 1)

    family_members: dict[str, list[str]] = defaultdict(list)
    for summary in group_summaries:
        family_members[str(summary["dashboard_family"])].append(str(summary["dashboard_group_code"]))

    family_summaries: list[dict[str, object]] = []
    for family, family_section in DASHBOARD_FAMILY_VARIANT_SECTIONS.items():
        member_groups = [
            summary
            for summary in group_summaries
            if summary["dashboard_family"] == family
        ]
        member_codes = {str(summary["dashboard_group_code"]) for summary in member_groups}
        family_units = sorted(
            code for code, groups in coverage.items() if any(group in member_codes for group in groups)
        )
        broad_codes = sorted({code[:1] for code in family_units})
        family_summaries.append(
            {
                "dashboard_family": family,
                "dashboard_family_variant_section_code": family_section["code"],
                "dashboard_family_variant_section_title": family_section["title"],
                "dashboard_group_count": len(member_groups),
                "dashboard_group_codes": [summary["dashboard_group_code"] for summary in member_groups],
                "official_broad_category_codes": broad_codes,
                "official_broad_category_titles": [OFFICIAL_BROAD_CATEGORIES[code] for code in broad_codes],
                "official_major_group_count": len({code[:2] for code in family_units}),
                "official_sub_major_group_count": len({code[:3] for code in family_units}),
                "official_minor_group_count": len({code[:4] for code in family_units}),
                "official_unit_group_count": len(family_units),
            }
        )

    kind_counts = Counter(summary["mapping_kind"] for summary in group_summaries)
    official_counts = {
        "broad_category_count": len({code[:1] for code in unit_codes}),
        "major_group_count": len({code[:2] for code in unit_codes}),
        "sub_major_group_count": len({code[:3] for code in unit_codes}),
        "minor_group_count": len({code[:4] for code in unit_codes}),
        "unit_group_count": len(unit_codes),
    }

    resources_family = next(
        family
        for family in family_summaries
        if family["dashboard_family"]
        == "Natural resources, agriculture and related production occupations, except management"
    )

    return {
        "official_hierarchy": official_counts,
        "dashboard": {
            "dashboard_family_count": len(family_summaries),
            "dashboard_group_count": len(group_summaries),
            "coverage": {
                "covered_unit_group_count": len(unit_codes) - len(uncovered_codes),
                "uncovered_unit_group_count": len(uncovered_codes),
                "overlapping_unit_group_count": len(overlapping_codes),
                "is_exact_partition": not uncovered_codes and not overlapping_codes,
            },
            "group_kind_counts": dict(kind_counts),
            "family_model_note": (
                "The dashboard's 10 families follow the NOC 2021 labour-force variant "
                "sections (L0-L9), not the official NOC 2021 broad categories."
            ),
            "management_family_note": (
                "The Management family is the main mismatch with the official hierarchy: "
                "it combines broad category 0 with the middle-management major groups 10 "
                "through 90, so it spans all 10 official broad categories."
            ),
            "resources_header_note": (
                "The Resources family is real data, not an orphan tile set. It contains "
                f"{resources_family['official_unit_group_count']} official unit groups "
                "through dashboard groups 82-83 and 84-85; any missing header is a treemap "
                "layout issue rather than a hierarchy issue."
            ),
            "families": family_summaries,
            "groups": group_summaries,
        },
    }


def render_dashboard_noc_audit_markdown(audit: dict[str, object]) -> str:
    official = audit["official_hierarchy"]
    dashboard = audit["dashboard"]

    lines = [
        "# Dashboard to NOC 2021 audit",
        "",
        "## Summary",
        "",
        (
            f"- Official NOC 2021 hierarchy reproduced locally: "
            f"{official['broad_category_count']} broad categories, "
            f"{official['major_group_count']} major groups, "
            f"{official['sub_major_group_count']} sub-major groups, "
            f"{official['minor_group_count']} minor groups, and "
            f"{official['unit_group_count']} unit groups."
        ),
        (
            f"- Current dashboard layer: {dashboard['dashboard_family_count']} families and "
            f"{dashboard['dashboard_group_count']} occupation groups."
        ),
        (
            f"- Coverage check: {dashboard['coverage']['covered_unit_group_count']}/"
            f"{official['unit_group_count']} unit groups are covered, with "
            f"{dashboard['coverage']['uncovered_unit_group_count']} gaps and "
            f"{dashboard['coverage']['overlapping_unit_group_count']} overlaps."
        ),
        f"- {dashboard['family_model_note']}",
        f"- {dashboard['management_family_note']}",
        f"- {dashboard['resources_header_note']}",
        "",
        "## Dashboard group shapes",
        "",
    ]

    for kind in sorted(dashboard["group_kind_counts"]):
        count = dashboard["group_kind_counts"][kind]
        lines.append(f"- {GROUP_KIND_LABELS[kind]}: {count}")

    lines.extend(
        [
            "",
            "## Family concordance",
            "",
            "| Dashboard family | Variant section | Dashboard groups | Official broad categories | Major | Sub-major | Minor | Unit |",
            "|---|---:|---:|---|---:|---:|---:|---:|",
        ]
    )

    for family in dashboard["families"]:
        broad_codes = ", ".join(family["official_broad_category_codes"])
        lines.append(
            "| "
            + " | ".join(
                [
                    str(family["dashboard_family"]),
                    str(family["dashboard_family_variant_section_code"]),
                    str(family["dashboard_group_count"]),
                    broad_codes,
                    str(family["official_major_group_count"]),
                    str(family["official_sub_major_group_count"]),
                    str(family["official_minor_group_count"]),
                    str(family["official_unit_group_count"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Group concordance",
            "",
            "| Code | Dashboard group | Family | Mapping kind | Broad | Major | Sub-major | Minor | Unit |",
            "|---|---|---|---|---|---:|---:|---:|---:|",
        ]
    )

    for group in dashboard["groups"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(group["dashboard_group_code"]),
                    str(group["dashboard_group_title"]),
                    str(group["dashboard_family_variant_section_code"]),
                    str(group["mapping_kind_label"]),
                    ", ".join(group["official_broad_category_codes"]),
                    str(group["official_major_group_count"]),
                    str(group["official_sub_major_group_count"]),
                    str(group["official_minor_group_count"]),
                    str(group["official_unit_group_count"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Official broad categories",
            "",
        ]
    )
    for code, title in OFFICIAL_BROAD_CATEGORIES.items():
        lines.append(f"- `{code}`: {title}")

    lines.extend(
        [
            "",
            "## Sources",
            "",
        ]
    )
    for label, url in SOURCE_LINKS:
        lines.append(f"- [{label}]({url})")

    return "\n".join(lines) + "\n"


def write_dashboard_noc_audit_markdown(output_path: Path = DOC_OUTPUT_PATH) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        render_dashboard_noc_audit_markdown(build_dashboard_noc_audit()),
        encoding="utf-8",
    )
    return output_path


if __name__ == "__main__":
    path = write_dashboard_noc_audit_markdown()
    print(f"Wrote dashboard audit to {path}")
