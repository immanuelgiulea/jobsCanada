from pathlib import Path

path = Path('fetch_statcan.py')
text = path.read_text(encoding='utf-8')
replacements = [
    (
        'from urllib.request import urlopen\n',
        'from urllib.request import urlopen\n\nfrom outlook_data import load_group_outlooks\n',
    ),
    (
        '    with employment_csv.open(newline="", encoding="utf-8-sig") as handle:\n',
        '    outlook_by_group, outlook_meta = load_group_outlooks([record["noc_code"] for record in occupations.values()])\n\n    with employment_csv.open(newline="", encoding="utf-8-sig") as handle:\n',
    ),
    (
        '        "median_weekly_wage",\n        "url",\n',
        '        "median_weekly_wage",\n        "outlook_label",\n        "outlook_score",\n        "outlook_window_start",\n        "outlook_window_end",\n        "outlook_release_date",\n        "outlook_source_url",\n        "url",\n',
    ),
    (
        '        row = {\n            "title": record["title"],\n',
        '        outlook = outlook_by_group.get(record["noc_code"], {})\n\n        row = {\n            "title": record["title"],\n',
    ),
    (
        '            "median_weekly_wage": f"{record[\'median_weekly_wage\'].get(wages_year):.2f}" if record["median_weekly_wage"].get(wages_year) is not None else "",\n            "url": record["url"],\n',
        '            "median_weekly_wage": f"{record[\'median_weekly_wage\'].get(wages_year):.2f}" if record["median_weekly_wage"].get(wages_year) is not None else "",\n            "outlook_label": outlook.get("outlook_label", ""),\n            "outlook_score": f"{outlook[\'outlook_score\']:.2f}" if outlook.get("outlook_score") is not None else "",\n            "outlook_window_start": outlook.get("outlook_window_start", ""),\n            "outlook_window_end": outlook.get("outlook_window_end", ""),\n            "outlook_release_date": outlook.get("outlook_release_date", ""),\n            "outlook_source_url": outlook.get("outlook_source_url", ""),\n            "url": record["url"],\n',
    ),
    (
        '        occupations_index.append({\n            "title": record["title"],\n            "category": record["category"],\n            "slug": record["slug"],\n            "noc_code": record["noc_code"],\n            "url": record["url"],\n        })\n',
        '        occupations_index.append({\n            "title": record["title"],\n            "category": record["category"],\n            "slug": record["slug"],\n            "noc_code": record["noc_code"],\n            "outlook_label": row["outlook_label"],\n            "outlook_score": row["outlook_score"],\n            "url": record["url"],\n        })\n',
    ),
    (
        '            f"- Median hourly wage ({wages_year}): {fmt_currency(parse_float(row[\'median_hourly_wage\']))}",\n',
        '            f"- Median hourly wage ({wages_year}): {fmt_currency(parse_float(row[\'median_hourly_wage\']))}",\n            f"- Employment outlook ({row[\'outlook_window_start\']} to {row[\'outlook_window_end\']}): {row[\'outlook_label\'] or \'-\'}",\n',
    ),
    (
        '                f"- Labour force characteristics by occupation, annual: {record[\'employment_url\']}",\n                f"- Employee wages by occupation, annual: {record[\'wages_url\']}",\n',
        '                f"- Labour force characteristics by occupation, annual: {record[\'employment_url\']}",\n                f"- Employee wages by occupation, annual: {record[\'wages_url\']}",\n                f"- {outlook_meta[\'title\']}: {outlook_meta[\'page_url\']}",\n',
    ),
]
for old, new in replacements:
    if old not in text:
        raise SystemExit(f'missing snippet: {old[:80]!r}')
    text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
