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
cols = []
province_total = []
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
        name = row.get('Economic Region Name', '')
        if province and province_names.get(province) == name:
            province_total.append(row)
    elem.clear()

print('province_total_rows', len(province_total))
print('distinct_noc', len({r['NOC_Code'] for r in province_total}))
print('province_counts', Counter(r['Province'] for r in province_total))
print('distinct_outlooks', Counter(r['Outlook'] for r in province_total))
