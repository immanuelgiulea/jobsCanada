from __future__ import annotations

DEFAULT_GEO_CODE = "CA"

GEO_DEFINITIONS = [
    {
        "code": "CA",
        "label_en": "Canada",
        "label_fr": "Canada",
        "type": "country",
        "statcan_name": "Canada",
        "outlook_code": "CA",
    },
    {
        "code": "NL",
        "label_en": "Newfoundland and Labrador",
        "label_fr": "Terre-Neuve-et-Labrador",
        "type": "province",
        "statcan_name": "Newfoundland and Labrador",
        "outlook_code": "NL",
    },
    {
        "code": "PE",
        "label_en": "Prince Edward Island",
        "label_fr": "Ile-du-Prince-Edouard",
        "type": "province",
        "statcan_name": "Prince Edward Island",
        "outlook_code": "PE",
    },
    {
        "code": "NS",
        "label_en": "Nova Scotia",
        "label_fr": "Nouvelle-Ecosse",
        "type": "province",
        "statcan_name": "Nova Scotia",
        "outlook_code": "NS",
    },
    {
        "code": "NB",
        "label_en": "New Brunswick",
        "label_fr": "Nouveau-Brunswick",
        "type": "province",
        "statcan_name": "New Brunswick",
        "outlook_code": "NB",
    },
    {
        "code": "QC",
        "label_en": "Quebec",
        "label_fr": "Quebec",
        "type": "province",
        "statcan_name": "Quebec",
        "outlook_code": "QC",
    },
    {
        "code": "ON",
        "label_en": "Ontario",
        "label_fr": "Ontario",
        "type": "province",
        "statcan_name": "Ontario",
        "outlook_code": "ON",
    },
    {
        "code": "MB",
        "label_en": "Manitoba",
        "label_fr": "Manitoba",
        "type": "province",
        "statcan_name": "Manitoba",
        "outlook_code": "MB",
    },
    {
        "code": "SK",
        "label_en": "Saskatchewan",
        "label_fr": "Saskatchewan",
        "type": "province",
        "statcan_name": "Saskatchewan",
        "outlook_code": "SK",
    },
    {
        "code": "AB",
        "label_en": "Alberta",
        "label_fr": "Alberta",
        "type": "province",
        "statcan_name": "Alberta",
        "outlook_code": "AB",
    },
    {
        "code": "BC",
        "label_en": "British Columbia",
        "label_fr": "Colombie-Britannique",
        "type": "province",
        "statcan_name": "British Columbia",
        "outlook_code": "BC",
    },
    {
        "code": "YT",
        "label_en": "Yukon",
        "label_fr": "Yukon",
        "type": "territory",
        "statcan_name": None,
        "outlook_code": "YK",
    },
    {
        "code": "NT",
        "label_en": "Northwest Territories",
        "label_fr": "Territoires du Nord-Ouest",
        "type": "territory",
        "statcan_name": None,
        "outlook_code": "NT",
    },
    {
        "code": "NU",
        "label_en": "Nunavut",
        "label_fr": "Nunavut",
        "type": "territory",
        "statcan_name": None,
        "outlook_code": "NU",
    },
]

GEO_CODES = [geo["code"] for geo in GEO_DEFINITIONS]
GEO_METADATA = [
    {
        "code": geo["code"],
        "label_en": geo["label_en"],
        "label_fr": geo["label_fr"],
        "type": geo["type"],
    }
    for geo in GEO_DEFINITIONS
]
GEO_CODE_TO_LABEL = {geo["code"]: geo["label_en"] for geo in GEO_DEFINITIONS}
GEO_SORT_INDEX = {geo["code"]: index for index, geo in enumerate(GEO_DEFINITIONS)}
STATCAN_GEO_TO_CODE = {
    geo["statcan_name"]: geo["code"]
    for geo in GEO_DEFINITIONS
    if geo["statcan_name"]
}
OUTLOOK_GEO_TO_CODE = {
    geo["outlook_code"]: geo["code"]
    for geo in GEO_DEFINITIONS
    if geo["outlook_code"]
}
OUTLOOK_REGION_NAMES = {
    geo["outlook_code"]: geo["label_en"]
    for geo in GEO_DEFINITIONS
    if geo["outlook_code"] and geo["type"] != "country"
}
