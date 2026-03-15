import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

path = Path('tmp/outlook/unzipped/xl/worksheets/sheet1.xml')
ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
cols = []
province_counter = Counter()
region_name_counter = Counter()
found_canada = []
row_count = 0
for event, elem in ET.iterparse(path, events=('end',)):
    if elem.tag.endswith('row'):
        row_count += 1
        cells = []
        for c in elem:
            if not c.tag.endswith('c'):
                continue
            value = ''
            t = c.attrib.get('t')
            if t == 'inlineStr':
                node = c.find('.//x:t', ns)
                value = node.text if node is not None and node.text is not None else ''
            else:
                node = c.find('x:v', ns)
                value = node.text if node is not None and node.text is not None else ''
            cells.append(value)
        if row_count == 1:
            cols = cells
        elif cells:
            data = dict(zip(cols, cells))
            province_counter[data.get('Province', '')] += 1
            region_name_counter[data.get('Economic Region Name', '')] += 1
            if data.get('Province') in {'CA', 'CAN'} or data.get('Economic Region Name') == 'Canada':
                found_canada.append({k: data.get(k) for k in ('NOC_Code','NOC Title','Outlook','Province','Economic Region Code','Economic Region Name')})
                if len(found_canada) >= 5:
                    break
        elem.clear()

print('rows_seen', row_count)
print('columns', cols)
print('top_provinces', province_counter.most_common(15))
print('has_canada_rows', bool(found_canada))
print('sample_canada_rows', found_canada)
