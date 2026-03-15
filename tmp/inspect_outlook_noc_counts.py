import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

path = Path('tmp/outlook/unzipped/xl/worksheets/sheet1.xml')
ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
province_names = {
    'NL': 'Newfoundland and Labrador','PE': 'Prince Edward Island','NS': 'Nova Scotia','NB': 'New Brunswick','QC': 'Quebec','ON': 'Ontario','MB': 'Manitoba','SK': 'Saskatchewan','AB': 'Alberta','BC': 'British Columbia','YK': 'Yukon','NT': 'Northwest Territories','NU': 'Nunavut',
}
pattern = re.compile(r'Approximately\s+([0-9][0-9,]*)\s+people\s+work(?:ed)?\s+in\s+this\s+occupation', re.I)
cols = []
matched_by_noc = defaultdict(int)
outlooks_by_noc = defaultdict(set)
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
        if province_names.get(row.get('Province','')) != row.get('Economic Region Name',''):
            elem.clear(); continue
        noc = row['NOC_Code']
        outlooks_by_noc[noc].add(row['Outlook'])
        if pattern.search(row.get('Employment Trends','')):
            matched_by_noc[noc] += 1
    elem.clear()

zeros = [noc for noc, s in outlooks_by_noc.items() if matched_by_noc[noc] == 0]
print('distinct_noc', len(outlooks_by_noc))
print('noc_with_zero_matched_counts', len(zeros))
print('sample_zero', zeros[:20])
print('noc_with_full13_counts', sum(1 for v in matched_by_noc.values() if v == 13))
