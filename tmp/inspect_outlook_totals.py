import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

path = Path('tmp/outlook/unzipped/xl/worksheets/sheet1.xml')
ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
province_total = []
cols = []
for event, elem in ET.iterparse(path, events=('end',)):
    if not elem.tag.endswith('row'):
        continue
    cells = []
    for c in elem:
        if not c.tag.endswith('c'):
            continue
        t = c.attrib.get('t')
        if t == 'inlineStr':
            node = c.find('.//x:t', ns)
        else:
            node = c.find('x:v', ns)
        cells.append(node.text if node is not None and node.text is not None else '')
    if not cols:
        cols = cells
    elif cells:
        row = dict(zip(cols, cells))
        er = row.get('Economic Region Code', '')
        if re.fullmatch(r'\d+00', er):
            province_total.append(row)
    elem.clear()

print('province_total_rows', len(province_total))
print('distinct_noc', len({r['NOC_Code'] for r in province_total}))
print('distinct_provinces', sorted({r['Province'] for r in province_total}))
print('distinct_outlooks', Counter(r['Outlook'] for r in province_total))
print('sample', [{k: r[k] for k in ('NOC_Code','NOC Title','Outlook','Province','Economic Region Code','Economic Region Name')} for r in province_total[:8]])
