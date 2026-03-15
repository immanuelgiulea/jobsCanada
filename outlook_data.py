"""
Download and aggregate ESDC 3-year employment outlooks for NOC 2021 groups.

The workbook is published on the Open Government Portal and contains outlook
labels plus narrative text for each unit-group NOC by province and economic
region. This module rolls those unit-group outlooks up by geography and also
builds a Canada-wide aggregate by weighting the geography-level rows together.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
import zipfile
from datetime import datetime, timedelta
from html import unescape
from pathlib import Path
from urllib.request import urlopen

from geography import DEFAULT_GEO_CODE, OUTLOOK_GEO_TO_CODE, OUTLOOK_REGION_NAMES

OUTLOOK_PAGE_URL = (
    "https://open.canada.ca/data/en/dataset/"
    "b0e112e9-cf53-4e79-8838-23cd98debe5b/resource/"
    "cb52e1d0-ab62-4357-91cc-d8f5a2114e02"
)
OUTLOOK_DOWNLOAD_URL = (
    "https://open.canada.ca/data/dataset/"
    "b0e112e9-cf53-4e79-8838-23cd98debe5b/resource/"
    "cb52e1d0-ab62-4357-91cc-d8f5a2114e02/download/"
    "20252027_outlook_n21_en_251208.xlsx"
)
OUTLOOK_FILENAME = "20252027_outlook_n21_en_251208.xlsx"
OUTLOOK_WINDOW_START = 2025
OUTLOOK_WINDOW_END = 2027
OUTLOOK_TITLE = "2025-2027 Employment Outlooks - NOC 2021"
OUTLOOK_SOURCE_NAME = "ESDC 3-Year Employment Outlooks"

OUTLOOK_DIR = Path("tmp/outlook")
SHEET_PATH = "xl/worksheets/sheet1.xml"
XML_NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
EXCEL_EPOCH = datetime(1899, 12, 30)

OUTLOOK_LABEL_TO_SCORE = {
    "Very limited": -2.0,
    "Limited": -1.0,
    "Moderate": 0.0,
    "Good": 1.0,
    "Very good": 2.0,
}

EMPLOYMENT_PATTERNS = [
    re.compile(r"Approximately\s+([0-9][0-9,]*)\s+people\s+work(?:ed)?\s+in\s+this\s+occupation", re.IGNORECASE),
    re.compile(r"([0-9][0-9,]*)\s+people\s+work(?:ed)?\s+in\s+this\s+occupation", re.IGNORECASE),
]


def ensure_outlook_workbook() -> Path:
    OUTLOOK_DIR.mkdir(parents=True, exist_ok=True)
    workbook_path = OUTLOOK_DIR / OUTLOOK_FILENAME
    if workbook_path.exists():
        return workbook_path

    print(f"Downloading outlook workbook from {OUTLOOK_DOWNLOAD_URL}")
    with urlopen(OUTLOOK_DOWNLOAD_URL) as response, workbook_path.open("wb") as output:
        output.write(response.read())
    return workbook_path


def clean_html_text(value: str) -> str:
    text = re.sub(r"<[^>]+>", " ", value or "")
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def extract_employment_count(text: str) -> int | None:
    cleaned = clean_html_text(text)
    for pattern in EMPLOYMENT_PATTERNS:
        match = pattern.search(cleaned)
        if match:
            return int(match.group(1).replace(",", ""))
    return None


def parse_release_date(value: str) -> str | None:
    if not value:
        return None
    try:
        serial = int(float(value))
    except ValueError:
        return None
    return (EXCEL_EPOCH + timedelta(days=serial)).date().isoformat()


def iter_workbook_rows(workbook_path: Path):
    with zipfile.ZipFile(workbook_path) as archive:
        with archive.open(SHEET_PATH) as handle:
            headers = None
            for _event, elem in ET.iterparse(handle, events=("end",)):
                if elem.tag != f"{XML_NS}row":
                    continue

                values = []
                for cell in elem.findall(f"{XML_NS}c"):
                    cell_type = cell.attrib.get("t")
                    if cell_type == "inlineStr":
                        parts = [node.text or "" for node in cell.iterfind(f".//{XML_NS}t")]
                        values.append("".join(parts))
                    else:
                        value_node = cell.find(f"{XML_NS}v")
                        values.append(value_node.text if value_node is not None and value_node.text is not None else "")

                if headers is None:
                    headers = values
                elif values:
                    yield dict(zip(headers, values))

                elem.clear()


def province_total_rows(workbook_path: Path) -> list[dict[str, str]]:
    rows = []
    for row in iter_workbook_rows(workbook_path):
        province = row.get("Province", "")
        if row.get("LANG") and row["LANG"] != "EN":
            continue
        geo_code = OUTLOOK_GEO_TO_CODE.get(province)
        if not geo_code:
            continue
        if OUTLOOK_REGION_NAMES.get(province) != row.get("Economic Region Name", ""):
            continue
        rows.append({**row, "_geo_code": geo_code})
    return rows


def label_from_score(score: float | None) -> str:
    if score is None:
        return "Undetermined"
    return min(OUTLOOK_LABEL_TO_SCORE, key=lambda label: abs(OUTLOOK_LABEL_TO_SCORE[label] - score))


def expand_group_prefixes(group_code: str) -> list[str]:
    prefixes: list[str] = []
    for part in group_code.split(","):
        token = part.strip()
        if not token:
            continue
        if "-" in token:
            start, end = [piece.strip() for piece in token.split("-", 1)]
            if start.isdigit() and end.isdigit() and len(start) == len(end):
                for value in range(int(start), int(end) + 1):
                    prefixes.append(str(value).zfill(len(start)))
                continue
        prefixes.append(token)
    return prefixes


def summarize_outlook_entries(entries: list[dict[str, object]]) -> dict[str, object]:
    valid = [entry for entry in entries if entry["outlook_score"] is not None]
    weighted = [entry for entry in valid if entry["employment_weight"]]

    if weighted:
        total_weight = sum(int(entry["employment_weight"]) for entry in weighted)
        avg_score = sum(float(entry["outlook_score"]) * int(entry["employment_weight"]) for entry in weighted) / total_weight
    elif valid:
        total_weight = len(valid)
        avg_score = sum(float(entry["outlook_score"]) for entry in valid) / total_weight
    else:
        total_weight = 0
        avg_score = None

    release_dates = sorted({entry["release_date"] for entry in entries if entry["release_date"]})
    return {
        "avg_score": avg_score,
        "label": label_from_score(avg_score),
        "release_date": release_dates[-1] if release_dates else None,
        "entry_count": len(entries),
        "valid_count": len(valid),
        "total_weight": total_weight,
        "is_weighted": bool(weighted),
    }


def build_unit_outlooks(workbook_path: Path) -> dict[str, dict[str, dict[str, object]]]:
    by_geo_and_code: dict[str, dict[str, list[dict[str, object]]]] = {}
    for row in province_total_rows(workbook_path):
        geo_code = row.get("_geo_code")
        if not geo_code:
            continue
        code = row.get("NOC_Code", "").replace("NOC_", "")
        if not code:
            continue

        entry = {
            "title": row.get("NOC Title", ""),
            "outlook_label": row.get("Outlook", "").strip() or "Undetermined",
            "outlook_score": OUTLOOK_LABEL_TO_SCORE.get(row.get("Outlook", "").strip()),
            "employment_weight": extract_employment_count(row.get("Employment Trends", "")),
            "release_date": parse_release_date(row.get("Release Date", "")),
        }
        by_geo_and_code.setdefault(str(geo_code), {}).setdefault(code, []).append(entry)

    unit_outlooks: dict[str, dict[str, dict[str, object]]] = {}
    for geo_code, rows_by_code in by_geo_and_code.items():
        unit_outlooks[geo_code] = {}
        for code, rows in rows_by_code.items():
            summary = summarize_outlook_entries(rows)
            unit_outlooks[geo_code][code] = {
                "title": rows[0]["title"],
                "outlook_label": summary["label"],
                "outlook_score": round(summary["avg_score"], 2) if summary["avg_score"] is not None else None,
                "employment_weight": summary["total_weight"] if summary["is_weighted"] else None,
                "row_count": summary["entry_count"],
                "valid_row_count": summary["valid_count"],
                "release_date": summary["release_date"],
            }

    return unit_outlooks


def load_group_outlooks(group_codes: list[str]) -> tuple[dict[str, dict[str, dict[str, object]]], dict[str, object]]:
    workbook_path = ensure_outlook_workbook()
    unit_outlooks_by_geo = build_unit_outlooks(workbook_path)

    release_dates = sorted(
        {
            entry["release_date"]
            for geo_entries in unit_outlooks_by_geo.values()
            for entry in geo_entries.values()
            if entry["release_date"]
        }
    )
    metadata = {
        "title": OUTLOOK_TITLE,
        "page_url": OUTLOOK_PAGE_URL,
        "download_url": OUTLOOK_DOWNLOAD_URL,
        "window_start": OUTLOOK_WINDOW_START,
        "window_end": OUTLOOK_WINDOW_END,
        "release_date": release_dates[-1] if release_dates else None,
        "unit_group_count": sum(len(geo_entries) for geo_entries in unit_outlooks_by_geo.values()),
        "geography_count": len(unit_outlooks_by_geo),
    }

    group_outlooks: dict[str, dict[str, dict[str, object]]] = {DEFAULT_GEO_CODE: {}}
    for group_code in group_codes:
        prefixes = expand_group_prefixes(group_code)
        canada_matches: list[dict[str, object]] = []

        for geo_code, geo_entries in unit_outlooks_by_geo.items():
            matches = [
                entry
                for code, entry in geo_entries.items()
                if any(code.startswith(prefix) for prefix in prefixes)
            ]
            if not matches:
                continue

            canada_matches.extend(matches)
            summary = summarize_outlook_entries(matches)
            group_outlooks.setdefault(geo_code, {})[group_code] = {
                "outlook_label": summary["label"],
                "outlook_score": round(summary["avg_score"], 2) if summary["avg_score"] is not None else None,
                "outlook_window_start": OUTLOOK_WINDOW_START,
                "outlook_window_end": OUTLOOK_WINDOW_END,
                "outlook_release_date": summary["release_date"] or metadata["release_date"],
                "outlook_source_url": OUTLOOK_PAGE_URL,
                "outlook_unit_count": summary["entry_count"],
                "outlook_unit_valid_count": summary["valid_count"],
                "outlook_weight_basis": (
                    "employment_weighted_unit_outlooks"
                    if summary["is_weighted"]
                    else "average_unit_outlooks"
                    if summary["valid_count"]
                    else "undetermined"
                ),
            }

        if canada_matches:
            summary = summarize_outlook_entries(canada_matches)
            group_outlooks[DEFAULT_GEO_CODE][group_code] = {
                "outlook_label": summary["label"],
                "outlook_score": round(summary["avg_score"], 2) if summary["avg_score"] is not None else None,
                "outlook_window_start": OUTLOOK_WINDOW_START,
                "outlook_window_end": OUTLOOK_WINDOW_END,
                "outlook_release_date": summary["release_date"] or metadata["release_date"],
                "outlook_source_url": OUTLOOK_PAGE_URL,
                "outlook_unit_count": summary["entry_count"],
                "outlook_unit_valid_count": summary["valid_count"],
                "outlook_weight_basis": (
                    "employment_weighted_geography_outlooks"
                    if summary["is_weighted"]
                    else "average_geography_outlooks"
                    if summary["valid_count"]
                    else "undetermined"
                ),
            }

    return group_outlooks, metadata
