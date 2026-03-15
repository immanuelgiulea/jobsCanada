from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

STATCAN_EPIAC_TITLE = "Experimental Estimates of Potential Artificial Intelligence Occupational Exposure in Canada, 2024"
STATCAN_EPIAC_URL = "https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm"
STATCAN_EPIAC_REFERENCE_YEAR = 2021
STATCAN_EPIAC_OCC_SYSTEM = "NOC 2016"
STATCAN_EPIAC_MEDIAN_AIOE = 6.0
STATCAN_EPIAC_MEDIAN_COMPLEMENTARITY = 0.6
STATCAN_EMPLOYMENT_STUDY_EN_URL = "https://www150.statcan.gc.ca/n1/en/pub/36-28-0001/2026001/article/00001-eng.pdf"
STATCAN_EMPLOYMENT_STUDY_FR_URL = "https://www150.statcan.gc.ca/n1/fr/pub/36-28-0001/2026001/article/00001-fra.pdf"
ISQ_EPIAC_PDF_URL = "https://statistique.quebec.ca/fr/fichier/exposition-professions-intelligence-artificielle-2024.pdf"

GROUP_LABELS = {
    "HELC": "High exposure, low complementarity",
    "HEHC": "High exposure, high complementarity",
    "LOW": "Low exposure",
}


@dataclass(frozen=True)
class EPIACRow:
    key: str
    title: str
    employment: int
    aioe: float
    complementarity: float
    caioe: float
    helc_pct: float
    hehc_pct: float
    low_pct: float

    @property
    def high_exposure_pct(self) -> float:
        return self.helc_pct + self.hehc_pct

    @property
    def dominant_group(self) -> str:
        values = {
            "HELC": self.helc_pct,
            "HEHC": self.hehc_pct,
            "LOW": self.low_pct,
        }
        return max(values, key=values.get)


OFFICIAL_ROWS = {
    "management_0": EPIACRow("management_0", "Management occupations (0)", 1_500_200, 6.4858, 0.6599, 4.4635, 6, 87, 7),
    "business_finance_11": EPIACRow("business_finance_11", "Professional occupations in business and finance (11)", 491_600, 6.6558, 0.5901, 5.0478, 100, 0, 0),
    "admin_12_13": EPIACRow("admin_12_13", "Administrative occupations in finance, insurance and business (12, 13)", 979_700, 6.4791, 0.5592, 5.1198, 82, 18, 0),
    "office_14_15": EPIACRow("office_14_15", "Office support and co-ordination occupations (14, 15)", 832_500, 6.2227, 0.5029, 5.2678, 76, 0, 24),
    "education_40": EPIACRow("education_40", "Professional occupations in education services (40)", 675_000, 6.4791, 0.6780, 4.3461, 12, 88, 0),
    "professional_41": EPIACRow("professional_41", "Professional occupations in law and social, community and government services (41)", 406_600, 6.5639, 0.6414, 4.6434, 24, 76, 0),
    "support_42_43_44": EPIACRow("support_42_43_44", "Support occupations in law and social services (42, 43, 44)", 617_400, 6.1154, 0.6333, 4.3856, 32, 34, 34),
    "arts_51_52": EPIACRow("arts_51_52", "Occupations in art, culture, recreation and sports (51, 52)", 277_500, 6.1135, 0.6011, 4.5674, 46, 33, 21),
    "sales_supervisors_62_63": EPIACRow("sales_supervisors_62_63", "Sales and service supervisors (62, 63)", 620_200, 6.0893, 0.6046, 4.5206, 19, 27, 54),
    "sales_reps_64": EPIACRow("sales_reps_64", "Sales representatives and salespersons in wholesale and retail trade (64)", 482_300, 6.0790, 0.5537, 4.8267, 89, 11, 0),
    "service_reps_65": EPIACRow("service_reps_65", "Service representatives and other customer and personal services occupations (65)", 516_600, 6.2254, 0.5300, 5.1038, 77, 2, 21),
    "support_sales_66_67": EPIACRow("support_sales_66_67", "Support occupations in sales and service (66, 67)", 1_040_700, 5.5812, 0.5093, 4.6833, 1, 0, 99),
    "technical_22": EPIACRow("technical_22", "Technical occupations related to natural and applied sciences (22)", 477_100, 6.1674, 0.6195, 4.5010, 34, 40, 26),
    "computer_217": EPIACRow("computer_217", "Computer and information systems professionals (217)", 426_900, 6.5851, 0.5516, 5.2472, 100, 0, 0),
    "engineers_213_214": EPIACRow("engineers_213_214", "Engineers (213, 214)", 210_800, 6.5463, 0.6340, 4.6747, 13, 87, 0),
    "physical_life_211_212": EPIACRow("physical_life_211_212", "Physical and life science professionals (211, 212)", 59_900, 6.3805, 0.6591, 4.4004, 1, 99, 0),
    "architects_stats_215_216": EPIACRow("architects_stats_215_216", "Architects and statisticians (215, 216)", 50_200, 6.5470, 0.6391, 4.6462, 25, 75, 0),
    "nursing_30": EPIACRow("nursing_30", "Professional occupations in nursing (30)", 317_500, 6.1660, 0.6995, 4.0007, 0, 100, 0),
    "health_31": EPIACRow("health_31", "Professional occupations in health (except nursing) (31)", 153_500, 6.2932, 0.7266, 3.9209, 0, 86, 14),
    "technical_health_32": EPIACRow("technical_health_32", "Technical occupations in health (32)", 309_200, 5.8897, 0.6250, 4.2623, 13, 18, 69),
    "assist_health_34": EPIACRow("assist_health_34", "Assisting occupations in support of health services (34)", 374_000, 5.6574, 0.6095, 4.1815, 0, 0, 100),
    "trades_72": EPIACRow("trades_72", "Industrial, electrical and construction trades (72)", 606_000, 5.5727, 0.6381, 3.9541, 0, 0, 100),
    "maintenance_73": EPIACRow("maintenance_73", "Maintenance and equipment operation trades (73)", 408_500, 5.6534, 0.6609, 3.8844, 0, 7, 93),
    "transport_74_75": EPIACRow("transport_74_75", "Transport and heavy equipment operators and servicers (74, 75)", 702_100, 5.5430, 0.6095, 4.0975, 0, 0, 100),
    "helpers_76": EPIACRow("helpers_76", "Trades helpers, construction labourers and related occupations (76)", 186_800, 5.3881, 0.6021, 4.0165, 0, 0, 100),
    "natural_resources_8": EPIACRow("natural_resources_8", "Natural resources, agriculture and related production occupations (8)", 221_300, 5.4180, 0.5746, 4.1757, 0, 0, 100),
    "machine_ops_92_94": EPIACRow("machine_ops_92_94", "Machine operators and supervisors in manufacturing and utilities (92, 94)", 302_400, 5.7288, 0.5829, 4.3706, 0, 10, 90),
    "assemblers_95_96": EPIACRow("assemblers_95_96", "Assemblers and labourers in manufacturing and utilities (95, 96)", 343_400, 5.5736, 0.5196, 4.6156, 0, 0, 100),
}

GROUP_MAPPING = {
    "0": [("management_0", None)],
    "10,20,30,40,50": [("management_0", None)],
    "60": [("management_0", None)],
    "70,80,90": [("management_0", None)],
    "111": [("business_finance_11", None)],
    "112": [("business_finance_11", None)],
    "12": [("admin_12_13", None)],
    "13": [("admin_12_13", None)],
    "14": [("office_14_15", None)],
    "211": [("physical_life_211_212", None)],
    "212": [("computer_217", 426_900), ("architects_stats_215_216", 50_200)],
    "213": [("engineers_213_214", None)],
    "22": [("technical_22", None)],
    "311": [("health_31", None)],
    "312": [("health_31", None)],
    "313": [("nursing_30", None)],
    "32": [("technical_health_32", None)],
    "33": [("assist_health_34", None)],
    "411": [("professional_41", None)],
    "412": [("education_40", None)],
    "413": [("professional_41", None)],
    "414": [("professional_41", None)],
    "421": [("support_42_43_44", None)],
    "422": [("support_42_43_44", None)],
    "43": [("support_42_43_44", None)],
    "44-45": [("support_42_43_44", None)],
    "51": [("arts_51_52", None)],
    "52": [("arts_51_52", None)],
    "53": [("arts_51_52", None)],
    "54-55": [("arts_51_52", None)],
    "62": [("sales_supervisors_62_63", None)],
    "63": [("sales_supervisors_62_63", None)],
    "64": [("sales_reps_64", 482_300), ("service_reps_65", 516_600)],
    "65": [("support_sales_66_67", None)],
    "72": [("trades_72", None)],
    "73": [("maintenance_73", None)],
    "74": [("transport_74_75", None)],
    "75": [("transport_74_75", None)],
    "82-83": [("natural_resources_8", None)],
    "84-85": [("natural_resources_8", None)],
    "92-93": [("machine_ops_92_94", None)],
    "94": [("machine_ops_92_94", None)],
    "95": [("assemblers_95_96", None)],
}


def normalize_group_code(code: str) -> str:
    return code.replace(" ", "")


def _resolve_weights(pairs: list[tuple[str, int | None]]) -> list[tuple[EPIACRow, float]]:
    rows: list[tuple[EPIACRow, float]] = []
    for key, weight in pairs:
        row = OFFICIAL_ROWS[key]
        rows.append((row, float(weight if weight is not None else row.employment)))
    return rows


def _weighted(rows: list[tuple[EPIACRow, float]], attr: str) -> float:
    total = sum(weight for _, weight in rows)
    if total <= 0:
        return 0.0
    return sum(getattr(row, attr) * weight for row, weight in rows) / total


def _dominant_group(helc_pct: float, hehc_pct: float, low_pct: float) -> str:
    values = {"HELC": helc_pct, "HEHC": hehc_pct, "LOW": low_pct}
    return max(values, key=values.get)


def load_group_epiac(group_codes: Iterable[str]) -> tuple[dict[str, dict[str, object]], dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for original_code in group_codes:
        code = normalize_group_code(original_code)
        if code not in GROUP_MAPPING:
            raise KeyError(f"No EPIAC mapping defined for occupation group {original_code!r}")

        rows = _resolve_weights(GROUP_MAPPING[code])
        aioe = _weighted(rows, "aioe")
        complementarity = _weighted(rows, "complementarity")
        caioe = _weighted(rows, "caioe")
        helc_pct = _weighted(rows, "helc_pct")
        hehc_pct = _weighted(rows, "hehc_pct")
        low_pct = _weighted(rows, "low_pct")
        high_exposure_pct = helc_pct + hehc_pct
        dominant_group = _dominant_group(helc_pct, hehc_pct, low_pct)
        source_titles = [row.title for row, _ in rows]
        exact = len(source_titles) == 1
        if exact:
            mapping_note = (
                f"Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census ({STATCAN_EPIAC_OCC_SYSTEM}): "
                f"{source_titles[0]}."
            )
        else:
            mapping_note = (
                f"Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census ({STATCAN_EPIAC_OCC_SYSTEM}): "
                f"{'; '.join(source_titles)}."
            )

        result[original_code] = {
            "epiac_reference_year": STATCAN_EPIAC_REFERENCE_YEAR,
            "epiac_aioe": round(aioe, 4),
            "epiac_complementarity": round(complementarity, 4),
            "epiac_caioe": round(caioe, 4),
            "epiac_helc_pct": round(helc_pct, 1),
            "epiac_hehc_pct": round(hehc_pct, 1),
            "epiac_low_pct": round(low_pct, 1),
            "epiac_high_exposure_pct": round(high_exposure_pct, 1),
            "epiac_display_score": max(0, min(10, int(round(high_exposure_pct / 10)))),
            "epiac_group_code": dominant_group,
            "epiac_group_label": GROUP_LABELS[dominant_group],
            "epiac_source_groups": source_titles,
            "epiac_source_title": STATCAN_EPIAC_TITLE,
            "epiac_source_url": STATCAN_EPIAC_URL,
            "epiac_source_note": mapping_note,
        }

    meta = {
        "epiac_title": STATCAN_EPIAC_TITLE,
        "epiac_source_url": STATCAN_EPIAC_URL,
        "epiac_reference_year": STATCAN_EPIAC_REFERENCE_YEAR,
        "epiac_occ_system": STATCAN_EPIAC_OCC_SYSTEM,
        "epiac_median_aioe": STATCAN_EPIAC_MEDIAN_AIOE,
        "epiac_median_complementarity": STATCAN_EPIAC_MEDIAN_COMPLEMENTARITY,
        "epiac_group_labels": GROUP_LABELS,
        "context_sources": [
            {
                "name": "StatCan: Employment growth in Canada since the beginning of the generative AI era",
                "url": STATCAN_EMPLOYMENT_STUDY_EN_URL,
            },
            {
                "name": "ISQ: Exposition des professions a l'intelligence artificielle en 2024",
                "url": ISQ_EPIAC_PDF_URL,
            },
        ],
    }
    return result, meta
