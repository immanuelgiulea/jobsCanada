"""
Load the official NOC 2021 classification structure.

This module treats the official 10 / 45 / 89 / 162 / 516 hierarchy as the
canonical occupation spine for the project.
"""

from __future__ import annotations

import csv
from pathlib import Path
from urllib.request import urlopen


NOC_DIR = Path("tmp/noc")
CLASSIFICATION_STRUCTURE_FILENAME = "noc-2021-v1.0-classification-structure.csv"
CLASSIFICATION_STRUCTURE_PATH = NOC_DIR / CLASSIFICATION_STRUCTURE_FILENAME
CLASSIFICATION_STRUCTURE_URL = (
    "https://www.statcan.gc.ca/en/subjects/standard/noc/2021/indexV1/"
    "noc-2021-v1.0-classification-structure.csv"
)
CLASSIFICATION_STRUCTURE_PAGE_URL = "https://www.statcan.gc.ca/en/subjects/standard/noc/2021/indexV1"

LEVEL_TO_KIND = {
    1: "broad_category",
    2: "major_group",
    3: "sub_major_group",
    4: "minor_group",
    5: "unit_group",
}
KIND_TO_COLLECTION = {
    "broad_category": "broad_categories",
    "major_group": "major_groups",
    "sub_major_group": "sub_major_groups",
    "minor_group": "minor_groups",
    "unit_group": "unit_groups",
}
KIND_TO_LABEL = {
    "broad_category": "Broad Category",
    "major_group": "Major Group",
    "sub_major_group": "Sub-major Group",
    "minor_group": "Minor Group",
    "unit_group": "Unit Group",
}


def ensure_classification_structure_csv() -> Path:
    NOC_DIR.mkdir(parents=True, exist_ok=True)
    if CLASSIFICATION_STRUCTURE_PATH.exists():
        return CLASSIFICATION_STRUCTURE_PATH

    print(f"Downloading official NOC 2021 classification structure from {CLASSIFICATION_STRUCTURE_URL}")
    with urlopen(CLASSIFICATION_STRUCTURE_URL) as response, CLASSIFICATION_STRUCTURE_PATH.open("wb") as output:
        output.write(response.read())
    return CLASSIFICATION_STRUCTURE_PATH


def parent_code_for(code: str, kind: str) -> str | None:
    if kind == "broad_category":
        return None
    if kind == "major_group":
        return code[:1]
    if kind == "sub_major_group":
        return code[:2]
    if kind == "minor_group":
        return code[:3]
    if kind == "unit_group":
        return code[:4]
    raise ValueError(f"Unsupported hierarchy kind {kind!r}")


def _build_node(code: str, kind: str, title: str, definition: str | None) -> dict[str, object]:
    return {
        "code": code,
        "kind": kind,
        "kind_label": KIND_TO_LABEL[kind],
        "title": title,
        "definition": definition,
        "parent_code": parent_code_for(code, kind),
    }


def load_official_noc_structure(csv_path: Path | None = None) -> dict[str, object]:
    path = csv_path or ensure_classification_structure_csv()
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    nodes_by_code: dict[str, dict[str, object]] = {}
    hierarchy: dict[str, list[dict[str, object]]] = {
        "broad_categories": [],
        "major_groups": [],
        "sub_major_groups": [],
        "minor_groups": [],
        "unit_groups": [],
    }

    for row in rows:
        level = int(row["Level"])
        kind = LEVEL_TO_KIND[level]
        code = row["Code - NOC 2021 V1.0"].strip()
        title = row["Class title"].strip()
        definition = row["Class definition"].strip() or None
        node = _build_node(code, kind, title, definition)
        nodes_by_code[code] = node
        hierarchy[KIND_TO_COLLECTION[kind]].append(node)

    for kind in hierarchy:
        hierarchy[kind].sort(key=lambda item: str(item["code"]))

    for code, node in nodes_by_code.items():
        broad_code = code[:1]
        node["broad_category_code"] = broad_code
        node["broad_category_title"] = nodes_by_code[broad_code]["title"]

        if len(code) >= 2:
            major_code = code[:2]
            node["major_group_code"] = major_code
            node["major_group_title"] = nodes_by_code[major_code]["title"]
        else:
            node["major_group_code"] = None
            node["major_group_title"] = None

        if len(code) >= 3:
            sub_major_code = code[:3]
            node["sub_major_group_code"] = sub_major_code
            node["sub_major_group_title"] = nodes_by_code[sub_major_code]["title"]
        else:
            node["sub_major_group_code"] = None
            node["sub_major_group_title"] = None

        if len(code) >= 4:
            minor_code = code[:4]
            node["minor_group_code"] = minor_code
            node["minor_group_title"] = nodes_by_code[minor_code]["title"]
        else:
            node["minor_group_code"] = None
            node["minor_group_title"] = None

        if len(code) >= 5:
            unit_code = code[:5]
            node["unit_group_code"] = unit_code
            node["unit_group_title"] = nodes_by_code[unit_code]["title"]
        else:
            node["unit_group_code"] = None
            node["unit_group_title"] = None

    counts = {
        "broad_category_count": len(hierarchy["broad_categories"]),
        "major_group_count": len(hierarchy["major_groups"]),
        "sub_major_group_count": len(hierarchy["sub_major_groups"]),
        "minor_group_count": len(hierarchy["minor_groups"]),
        "unit_group_count": len(hierarchy["unit_groups"]),
    }

    return {
        **hierarchy,
        "counts": counts,
        "nodes_by_code": nodes_by_code,
        "source_url": CLASSIFICATION_STRUCTURE_URL,
        "source_page_url": CLASSIFICATION_STRUCTURE_PAGE_URL,
        "source_path": str(path),
    }
