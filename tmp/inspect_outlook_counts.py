import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

path = Path('tmp/outlook/unzipped/xl/worksheets/sheet1.xml')
ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
province_names = {
    'NL': 'Newfoundland and Labrador',
    'PE': 'Prince Edward Island',
    'NS': 'Nova Scotia',
    'NB': 'New Brunswick',
    'QC': 'Quebec',
    'ON': 'Ontario',
    'MB': 'Manitoba',
    'SK': 'Saskatchewan',
    'AB': 'Alberta',
    'BC': 'British Columbia',
    'YK': 'Yukon',
    'NT': 'Northwest Territories',
    'NU': 'Nunavut',
}
patterns = [
    re.compile(r'Approximately\s+([0-9][0-9,]*)\s+people\s+work(?:ed)?\s+in\s+this\s+occupation', re.I),
    re.compile(r'([0-9][0-9,]*)\s+people\s+work(?:ed)?\s+in\s+this\s+occupation', re.I),
]
cols = []
matched = 0
unmatched = []
for event, elem in ET.iterparse(path, events=('end',)):
    if not elem.tag.endswith('row'):
        continue
    cells = []
    for c in elem:
        if not c.tag.endswith('c'):
            continue
        t = c.attrib.get('t')
        node = c.find('.//x:t', ns) if t == 'inlineStr' else c.find('x:v', ns)
        cells.append(node.text if node is not None and node.text is not None else '')
    if not cols:
        cols = cells
    elif cells:
        row = dict(zip(cols, cells))
        province = row.get('Province', '')
        if province_names.get(province) != row.get('Economic Region Name', ''):
            elem.clear(); continue
        text = row.get('Employment Trends', '')
        found = None
        for pattern in patterns:
            m = pattern.search(text)
            if m:
                found = int(m.group(1).replace(',', ''))
                break
        if found is not None:
            matched += 1
        elif len(unmatched) < 12:
            unmatched.append({k: row[k] for k in ('NOC_Code','NOC Title','Province','Outlook','Employment Trends')})
    elem.clear()

print('matched', matched)
print('total', 6708)
print('sample_unmatched', unmatched)
