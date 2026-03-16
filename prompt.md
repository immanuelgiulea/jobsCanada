# AI Exposure of the Canadian Job Market

This document contains canonical NOC 2021 unit-group data for Canada. Employment and wages use annual StatCan tables through 2025, but those tables are published at a coarser occupation grain than the official 516 unit groups, so the dataset allocates published annual totals onto the canonical unit groups using ESDC unit employment weights. Outlook uses unit-level ESDC data for 2025-2027, and AI exposure maps StatCan's official EPIAC framework onto the canonical unit groups from published 2021 Census-based occupation groups.

Sources:
- https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041601
- https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410041701
- https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm
- https://open.canada.ca/data/en/dataset/b0e112e9-cf53-4e79-8838-23cd98debe5b/resource/cb52e1d0-ab62-4357-91cc-d8f5a2114e02
- https://www150.statcan.gc.ca/n1/en/pub/36-28-0001/2026001/article/00001-eng.pdf
- https://statistique.quebec.ca/fr/fichier/exposition-professions-intelligence-artificielle-2024.pdf

## Aggregate statistics

- Canonical unit groups: 516
- Total workers (2025): 21,028,900 (21.0M)
- Job-weighted EPIAC high-exposure share: 59.1%
- Job-weighted AIOE: 6.11
- Job-weighted complementarity: 0.60
- Estimated workers in HELC occupations: 6.5M
- Estimated workers in HEHC occupations: 6.0M
- Estimated workers in low-exposure occupations: 8.6M
- Trend window: 2019 to 2025
- Outlook window: 2025 to 2027

## Exposure mix by EPIAC group

| Group | Estimated workers | % of workers |
|-------|-------------------|--------------|
| HELC | 6.5M | 30.7% |
| HEHC | 6.0M | 28.4% |
| Low exposure | 8.6M | 40.9% |

## Unit groups with the highest EPIAC high-exposure share (2021 mapped source groups)

| Unit group | High-exposure share | Dominant EPIAC group | AIOE | Complementarity | Outlook | Workers |
|------------------|---------------------|----------------------|------|-----------------|---------|---------|
| Registered nurses and registered psychiatric nurses | 100.0% | High exposure, high complementarity | 6.17 | 0.70 | Good | 404K |
| Elementary school and kindergarten teachers | 100.0% | High exposure, high complementarity | 6.48 | 0.68 | Moderate | 295K |
| Financial auditors and accountants | 100.0% | High exposure, low complementarity | 6.66 | 0.59 | Moderate | 263K |
| Administrative assistants | 100.0% | High exposure, low complementarity | 6.48 | 0.56 | Moderate | 255K |
| Professional occupations in advertising, marketing and public relations | 100.0% | High exposure, low complementarity | 6.66 | 0.59 | Limited | 247K |
| Information systems specialists | 100.0% | High exposure, low complementarity | 6.58 | 0.56 | Moderate | 247K |
| Administrative officers | 100.0% | High exposure, low complementarity | 6.48 | 0.56 | Limited | 238K |
| College and other vocational instructors | 100.0% | High exposure, high complementarity | 6.48 | 0.68 | Moderate | 208K |
| Accounting technicians and bookkeepers | 100.0% | High exposure, low complementarity | 6.48 | 0.56 | Good | 194K |
| Software developers and programmers | 100.0% | High exposure, low complementarity | 6.58 | 0.56 | Moderate | 185K |
| Secondary school teachers | 100.0% | High exposure, high complementarity | 6.48 | 0.68 | Moderate | 160K |
| Lawyers and Quebec notaries | 100.0% | High exposure, high complementarity | 6.56 | 0.64 | Moderate | 147K |

## Biggest growers since 2019

| Unit group | High-exposure share | Dominant EPIAC group | Employment change | Workers | Median hourly wage |
|------------------|---------------------|----------------------|-------------------|---------|--------------------|
| Computer and information systems managers | 93.0% | High exposure, high complementarity | +61.3% | 149K | $60.10 |
| Banking, credit and other investment managers | 93.0% | High exposure, high complementarity | +61.3% | 85K | $60.10 |
| Financial managers | 93.0% | High exposure, high complementarity | +61.3% | 85K | $60.10 |
| Advertising, marketing and public relations managers | 93.0% | High exposure, high complementarity | +61.3% | 65K | $60.10 |
| Human resources managers | 93.0% | High exposure, high complementarity | +61.3% | 63K | $60.10 |
| Managers in social, community and correctional services | 93.0% | High exposure, high complementarity | +61.3% | 57K | $60.10 |
| Insurance, real estate and financial brokerage managers | 93.0% | High exposure, high complementarity | +61.3% | 54K | $60.10 |
| Managers in health care | 93.0% | High exposure, high complementarity | +61.3% | 51K | $60.10 |
| School principals and administrators of elementary and secondary education | 93.0% | High exposure, high complementarity | +61.3% | 44K | $60.10 |
| Engineering managers | 93.0% | High exposure, high complementarity | +61.3% | 41K | $60.10 |

## All 516 canonical unit groups

### Registered nurses and registered psychiatric nurses

| Field | Value |
|-------|-------|
| NOC | 31301 |
| Category | Health occupations |
| Workers | 404K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.70 |
| HELC / HEHC / Low | 0.0% / 100.0% / 0.0% |
| Employment change | +28.4% |
| Unemployment | 0.8% |
| Median hourly wage | $46.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in nursing (30). |

### Elementary school and kindergarten teachers

| Field | Value |
|-------|-------|
| NOC | 41221 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 295K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.48 |
| Complementarity | 0.68 |
| HELC / HEHC / Low | 12.0% / 88.0% / 0.0% |
| Employment change | +21.3% |
| Unemployment | 3.5% |
| Median hourly wage | $46.63 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in education services (40). |

### Financial auditors and accountants

| Field | Value |
|-------|-------|
| NOC | 11100 |
| Category | Business, finance and administration occupations |
| Workers | 263K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.66 |
| Complementarity | 0.59 |
| HELC / HEHC / Low | 100.0% / 0.0% / 0.0% |
| Employment change | +24.7% |
| Unemployment | 1.5% |
| Median hourly wage | $42.79 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in business and finance (11). |

### Administrative assistants

| Field | Value |
|-------|-------|
| NOC | 13110 |
| Category | Business, finance and administration occupations |
| Workers | 255K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +15.0% |
| Unemployment | 3.1% |
| Median hourly wage | $29.33 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Professional occupations in advertising, marketing and public relations

| Field | Value |
|-------|-------|
| NOC | 11202 |
| Category | Business, finance and administration occupations |
| Workers | 247K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.66 |
| Complementarity | 0.59 |
| HELC / HEHC / Low | 100.0% / 0.0% / 0.0% |
| Employment change | +37.8% |
| Unemployment | 3.5% |
| Median hourly wage | $41.03 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in business and finance (11). |

### Information systems specialists

| Field | Value |
|-------|-------|
| NOC | 21222 |
| Category | Natural and applied sciences and related occupations |
| Workers | 247K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Administrative officers

| Field | Value |
|-------|-------|
| NOC | 13100 |
| Category | Business, finance and administration occupations |
| Workers | 238K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +15.0% |
| Unemployment | 3.1% |
| Median hourly wage | $29.33 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### College and other vocational instructors

| Field | Value |
|-------|-------|
| NOC | 41210 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 208K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.48 |
| Complementarity | 0.68 |
| HELC / HEHC / Low | 12.0% / 88.0% / 0.0% |
| Employment change | +21.3% |
| Unemployment | 3.5% |
| Median hourly wage | $46.63 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in education services (40). |

### Accounting technicians and bookkeepers

| Field | Value |
|-------|-------|
| NOC | 12200 |
| Category | Business, finance and administration occupations |
| Workers | 194K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Software developers and programmers

| Field | Value |
|-------|-------|
| NOC | 21232 |
| Category | Natural and applied sciences and related occupations |
| Workers | 185K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Secondary school teachers

| Field | Value |
|-------|-------|
| NOC | 41220 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 160K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.48 |
| Complementarity | 0.68 |
| HELC / HEHC / Low | 12.0% / 88.0% / 0.0% |
| Employment change | +21.3% |
| Unemployment | 3.5% |
| Median hourly wage | $46.63 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in education services (40). |

### Lawyers and Quebec notaries

| Field | Value |
|-------|-------|
| NOC | 41101 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 147K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +38.2% |
| Unemployment | 1.9% |
| Median hourly wage | $62.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Human resources professionals

| Field | Value |
|-------|-------|
| NOC | 11200 |
| Category | Business, finance and administration occupations |
| Workers | 144K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.66 |
| Complementarity | 0.59 |
| HELC / HEHC / Low | 100.0% / 0.0% / 0.0% |
| Employment change | +37.8% |
| Unemployment | 3.5% |
| Median hourly wage | $41.03 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in business and finance (11). |

### Professional occupations in business management consulting

| Field | Value |
|-------|-------|
| NOC | 11201 |
| Category | Business, finance and administration occupations |
| Workers | 143K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.66 |
| Complementarity | 0.59 |
| HELC / HEHC / Low | 100.0% / 0.0% / 0.0% |
| Employment change | +37.8% |
| Unemployment | 3.5% |
| Median hourly wage | $41.03 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in business and finance (11). |

### Software engineers and designers

| Field | Value |
|-------|-------|
| NOC | 21231 |
| Category | Natural and applied sciences and related occupations |
| Workers | 134K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### University professors and lecturers

| Field | Value |
|-------|-------|
| NOC | 41200 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 128K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.48 |
| Complementarity | 0.68 |
| HELC / HEHC / Low | 12.0% / 88.0% / 0.0% |
| Employment change | +21.3% |
| Unemployment | 3.5% |
| Median hourly wage | $46.63 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in education services (40). |

### Financial advisors

| Field | Value |
|-------|-------|
| NOC | 11102 |
| Category | Business, finance and administration occupations |
| Workers | 123K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.66 |
| Complementarity | 0.59 |
| HELC / HEHC / Low | 100.0% / 0.0% / 0.0% |
| Employment change | +24.7% |
| Unemployment | 1.5% |
| Median hourly wage | $42.79 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in business and finance (11). |

### Financial and investment analysts

| Field | Value |
|-------|-------|
| NOC | 11101 |
| Category | Business, finance and administration occupations |
| Workers | 89K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.66 |
| Complementarity | 0.59 |
| HELC / HEHC / Low | 100.0% / 0.0% / 0.0% |
| Employment change | +24.7% |
| Unemployment | 1.5% |
| Median hourly wage | $42.79 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in business and finance (11). |

### Medical administrative assistants

| Field | Value |
|-------|-------|
| NOC | 13112 |
| Category | Business, finance and administration occupations |
| Workers | 85K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +15.0% |
| Unemployment | 3.1% |
| Median hourly wage | $29.33 |
| Outlook | Very good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Social workers

| Field | Value |
|-------|-------|
| NOC | 41300 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 83K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +15.8% |
| Unemployment | 1.8% |
| Median hourly wage | $40.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Social policy researchers, consultants and program officers

| Field | Value |
|-------|-------|
| NOC | 41403 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 82K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +27.1% |
| Unemployment | 2.7% |
| Median hourly wage | $45.67 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Post-secondary teaching and research assistants

| Field | Value |
|-------|-------|
| NOC | 41201 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 81K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.48 |
| Complementarity | 0.68 |
| HELC / HEHC / Low | 12.0% / 88.0% / 0.0% |
| Employment change | +21.3% |
| Unemployment | 3.5% |
| Median hourly wage | $46.63 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in education services (40). |

### Therapists in counselling and related specialized therapies

| Field | Value |
|-------|-------|
| NOC | 41301 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 79K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +15.8% |
| Unemployment | 1.8% |
| Median hourly wage | $40.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Supervisors, supply chain, tracking and scheduling coordination occupations

| Field | Value |
|-------|-------|
| NOC | 12013 |
| Category | Business, finance and administration occupations |
| Workers | 78K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Procurement and purchasing agents and officers

| Field | Value |
|-------|-------|
| NOC | 12102 |
| Category | Business, finance and administration occupations |
| Workers | 74K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Civil engineers

| Field | Value |
|-------|-------|
| NOC | 21300 |
| Category | Natural and applied sciences and related occupations |
| Workers | 68K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Employment insurance and revenue officers

| Field | Value |
|-------|-------|
| NOC | 12104 |
| Category | Business, finance and administration occupations |
| Workers | 60K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Legal administrative assistants

| Field | Value |
|-------|-------|
| NOC | 13111 |
| Category | Business, finance and administration occupations |
| Workers | 57K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +15.0% |
| Unemployment | 3.1% |
| Median hourly wage | $29.33 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Payroll administrators

| Field | Value |
|-------|-------|
| NOC | 13102 |
| Category | Business, finance and administration occupations |
| Workers | 55K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +15.0% |
| Unemployment | 3.1% |
| Median hourly wage | $29.33 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Computer systems developers and programmers

| Field | Value |
|-------|-------|
| NOC | 21230 |
| Category | Natural and applied sciences and related occupations |
| Workers | 49K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Property administrators

| Field | Value |
|-------|-------|
| NOC | 13101 |
| Category | Business, finance and administration occupations |
| Workers | 49K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +15.0% |
| Unemployment | 3.1% |
| Median hourly wage | $29.33 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Database analysts and data administrators

| Field | Value |
|-------|-------|
| NOC | 21223 |
| Category | Natural and applied sciences and related occupations |
| Workers | 48K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Mechanical engineers

| Field | Value |
|-------|-------|
| NOC | 21301 |
| Category | Natural and applied sciences and related occupations |
| Workers | 46K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Human resources and recruitment officers

| Field | Value |
|-------|-------|
| NOC | 12101 |
| Category | Business, finance and administration occupations |
| Workers | 46K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Other financial officers

| Field | Value |
|-------|-------|
| NOC | 11109 |
| Category | Business, finance and administration occupations |
| Workers | 45K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.66 |
| Complementarity | 0.59 |
| HELC / HEHC / Low | 100.0% / 0.0% / 0.0% |
| Employment change | +24.7% |
| Unemployment | 1.5% |
| Median hourly wage | $42.79 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in business and finance (11). |

### Health policy researchers, consultants and program officers

| Field | Value |
|-------|-------|
| NOC | 41404 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 44K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +27.1% |
| Unemployment | 2.7% |
| Median hourly wage | $45.67 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Data scientists

| Field | Value |
|-------|-------|
| NOC | 21211 |
| Category | Natural and applied sciences and related occupations |
| Workers | 44K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Executive assistants

| Field | Value |
|-------|-------|
| NOC | 12100 |
| Category | Business, finance and administration occupations |
| Workers | 42K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Other professional engineers

| Field | Value |
|-------|-------|
| NOC | 21399 |
| Category | Natural and applied sciences and related occupations |
| Workers | 42K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Supervisors, finance and insurance office workers

| Field | Value |
|-------|-------|
| NOC | 12011 |
| Category | Business, finance and administration occupations |
| Workers | 41K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Electrical and electronics engineers

| Field | Value |
|-------|-------|
| NOC | 21310 |
| Category | Natural and applied sciences and related occupations |
| Workers | 40K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Insurance adjusters and claims examiners

| Field | Value |
|-------|-------|
| NOC | 12201 |
| Category | Business, finance and administration occupations |
| Workers | 39K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Business systems specialists

| Field | Value |
|-------|-------|
| NOC | 21221 |
| Category | Natural and applied sciences and related occupations |
| Workers | 37K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Biologists and related scientists

| Field | Value |
|-------|-------|
| NOC | 21110 |
| Category | Natural and applied sciences and related occupations |
| Workers | 37K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.38 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 1.0% / 99.0% / 0.0% |
| Employment change | +29.2% |
| Unemployment | 1.7% |
| Median hourly wage | $44.87 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Physical and life science professionals (211, 212). |

### Education policy researchers, consultants and program officers

| Field | Value |
|-------|-------|
| NOC | 41405 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 35K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +27.1% |
| Unemployment | 2.7% |
| Median hourly wage | $45.67 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Production and transportation logistics coordinators

| Field | Value |
|-------|-------|
| NOC | 13201 |
| Category | Business, finance and administration occupations |
| Workers | 34K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +15.0% |
| Unemployment | 3.1% |
| Median hourly wage | $29.33 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Nursing coordinators and supervisors

| Field | Value |
|-------|-------|
| NOC | 31300 |
| Category | Health occupations |
| Workers | 32K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.70 |
| HELC / HEHC / Low | 0.0% / 100.0% / 0.0% |
| Employment change | +28.4% |
| Unemployment | 0.8% |
| Median hourly wage | $46.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in nursing (30). |

### Computer engineers (except software engineers and designers)

| Field | Value |
|-------|-------|
| NOC | 21311 |
| Category | Natural and applied sciences and related occupations |
| Workers | 32K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Business development officers and market researchers and analysts

| Field | Value |
|-------|-------|
| NOC | 41402 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 31K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +27.1% |
| Unemployment | 2.7% |
| Median hourly wage | $45.67 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Web developers and programmers

| Field | Value |
|-------|-------|
| NOC | 21234 |
| Category | Natural and applied sciences and related occupations |
| Workers | 31K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Very limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Cybersecurity specialists

| Field | Value |
|-------|-------|
| NOC | 21220 |
| Category | Natural and applied sciences and related occupations |
| Workers | 31K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Securities agents, investment dealers and brokers

| Field | Value |
|-------|-------|
| NOC | 11103 |
| Category | Business, finance and administration occupations |
| Workers | 28K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.66 |
| Complementarity | 0.59 |
| HELC / HEHC / Low | 100.0% / 0.0% / 0.0% |
| Employment change | +24.7% |
| Unemployment | 1.5% |
| Median hourly wage | $42.79 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in business and finance (11). |

### Educational counsellors

| Field | Value |
|-------|-------|
| NOC | 41320 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 27K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +15.8% |
| Unemployment | 1.8% |
| Median hourly wage | $40.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Conference and event planners

| Field | Value |
|-------|-------|
| NOC | 12103 |
| Category | Business, finance and administration occupations |
| Workers | 26K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Architects

| Field | Value |
|-------|-------|
| NOC | 21200 |
| Category | Natural and applied sciences and related occupations |
| Workers | 26K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Career development practitioners and career counsellors (except education)

| Field | Value |
|-------|-------|
| NOC | 41321 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 25K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +15.8% |
| Unemployment | 1.8% |
| Median hourly wage | $40.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Natural and applied science policy researchers, consultants and program officers

| Field | Value |
|-------|-------|
| NOC | 41400 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 24K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +27.1% |
| Unemployment | 2.7% |
| Median hourly wage | $45.67 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Industrial and manufacturing engineers

| Field | Value |
|-------|-------|
| NOC | 21321 |
| Category | Natural and applied sciences and related occupations |
| Workers | 24K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Supervisors, general office and administrative support workers

| Field | Value |
|-------|-------|
| NOC | 12010 |
| Category | Business, finance and administration occupations |
| Workers | 23K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Insurance underwriters

| Field | Value |
|-------|-------|
| NOC | 12202 |
| Category | Business, finance and administration occupations |
| Workers | 23K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Economists and economic policy researchers and analysts

| Field | Value |
|-------|-------|
| NOC | 41401 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 21K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +27.1% |
| Unemployment | 2.7% |
| Median hourly wage | $45.67 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Chemists

| Field | Value |
|-------|-------|
| NOC | 21101 |
| Category | Natural and applied sciences and related occupations |
| Workers | 18K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.38 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 1.0% / 99.0% / 0.0% |
| Employment change | +29.2% |
| Unemployment | 1.7% |
| Median hourly wage | $44.87 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Physical and life science professionals (211, 212). |

### Public and environmental health and safety professionals

| Field | Value |
|-------|-------|
| NOC | 21120 |
| Category | Natural and applied sciences and related occupations |
| Workers | 17K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.38 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 1.0% / 99.0% / 0.0% |
| Employment change | +29.2% |
| Unemployment | 1.7% |
| Median hourly wage | $44.87 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Physical and life science professionals (211, 212). |

### Mathematicians, statisticians and actuaries

| Field | Value |
|-------|-------|
| NOC | 21210 |
| Category | Natural and applied sciences and related occupations |
| Workers | 15K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Urban and land use planners

| Field | Value |
|-------|-------|
| NOC | 21202 |
| Category | Natural and applied sciences and related occupations |
| Workers | 15K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Assessors, business valuators and appraisers

| Field | Value |
|-------|-------|
| NOC | 12203 |
| Category | Business, finance and administration occupations |
| Workers | 13K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Petroleum engineers

| Field | Value |
|-------|-------|
| NOC | 21332 |
| Category | Natural and applied sciences and related occupations |
| Workers | 13K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Recreation, sports and fitness policy researchers, consultants and program officers

| Field | Value |
|-------|-------|
| NOC | 41406 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 13K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +27.1% |
| Unemployment | 2.7% |
| Median hourly wage | $45.67 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Geoscientists and oceanographers

| Field | Value |
|-------|-------|
| NOC | 21102 |
| Category | Natural and applied sciences and related occupations |
| Workers | 12K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.38 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 1.0% / 99.0% / 0.0% |
| Employment change | +29.2% |
| Unemployment | 1.7% |
| Median hourly wage | $44.87 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Physical and life science professionals (211, 212). |

### Web designers

| Field | Value |
|-------|-------|
| NOC | 21233 |
| Category | Natural and applied sciences and related occupations |
| Workers | 12K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Chemical engineers

| Field | Value |
|-------|-------|
| NOC | 21320 |
| Category | Natural and applied sciences and related occupations |
| Workers | 12K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Court reporters, medical transcriptionists and related occupations

| Field | Value |
|-------|-------|
| NOC | 12110 |
| Category | Business, finance and administration occupations |
| Workers | 10K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Program officers unique to government

| Field | Value |
|-------|-------|
| NOC | 41407 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 9K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +27.1% |
| Unemployment | 2.7% |
| Median hourly wage | $45.67 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Land surveyors

| Field | Value |
|-------|-------|
| NOC | 21203 |
| Category | Natural and applied sciences and related occupations |
| Workers | 8K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Nurse practitioners

| Field | Value |
|-------|-------|
| NOC | 31302 |
| Category | Health occupations |
| Workers | 7K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.70 |
| HELC / HEHC / Low | 0.0% / 100.0% / 0.0% |
| Employment change | +28.4% |
| Unemployment | 0.8% |
| Median hourly wage | $46.00 |
| Outlook | Very good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in nursing (30). |

### Agricultural representatives, consultants and specialists

| Field | Value |
|-------|-------|
| NOC | 21112 |
| Category | Natural and applied sciences and related occupations |
| Workers | 7K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.38 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 1.0% / 99.0% / 0.0% |
| Employment change | +29.2% |
| Unemployment | 1.7% |
| Median hourly wage | $44.87 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Physical and life science professionals (211, 212). |

### Records management technicians

| Field | Value |
|-------|-------|
| NOC | 12112 |
| Category | Business, finance and administration occupations |
| Workers | 7K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Probation and parole officers

| Field | Value |
|-------|-------|
| NOC | 41311 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 6K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +15.8% |
| Unemployment | 1.8% |
| Median hourly wage | $40.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Aerospace engineers

| Field | Value |
|-------|-------|
| NOC | 21390 |
| Category | Natural and applied sciences and related occupations |
| Workers | 6K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Police investigators and other investigative occupations

| Field | Value |
|-------|-------|
| NOC | 41310 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 6K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +15.8% |
| Unemployment | 1.8% |
| Median hourly wage | $40.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Statistical officers and related research support occupations

| Field | Value |
|-------|-------|
| NOC | 12113 |
| Category | Business, finance and administration occupations |
| Workers | 6K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Health information management occupations

| Field | Value |
|-------|-------|
| NOC | 12111 |
| Category | Business, finance and administration occupations |
| Workers | 5K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Forestry professionals

| Field | Value |
|-------|-------|
| NOC | 21111 |
| Category | Natural and applied sciences and related occupations |
| Workers | 4K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.38 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 1.0% / 99.0% / 0.0% |
| Employment change | +29.2% |
| Unemployment | 1.7% |
| Median hourly wage | $44.87 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Physical and life science professionals (211, 212). |

### Physician assistants, midwives and allied health professionals

| Field | Value |
|-------|-------|
| NOC | 31303 |
| Category | Health occupations |
| Workers | 4K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.70 |
| HELC / HEHC / Low | 0.0% / 100.0% / 0.0% |
| Employment change | +28.4% |
| Unemployment | 0.8% |
| Median hourly wage | $46.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in nursing (30). |

### Other professional occupations in social science

| Field | Value |
|-------|-------|
| NOC | 41409 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 4K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +27.1% |
| Unemployment | 2.7% |
| Median hourly wage | $45.67 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Geological engineers

| Field | Value |
|-------|-------|
| NOC | 21331 |
| Category | Natural and applied sciences and related occupations |
| Workers | 4K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Mining engineers

| Field | Value |
|-------|-------|
| NOC | 21330 |
| Category | Natural and applied sciences and related occupations |
| Workers | 3K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Customs, ship and other brokers

| Field | Value |
|-------|-------|
| NOC | 13200 |
| Category | Business, finance and administration occupations |
| Workers | 3K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +15.0% |
| Unemployment | 3.1% |
| Median hourly wage | $29.33 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Landscape architects

| Field | Value |
|-------|-------|
| NOC | 21201 |
| Category | Natural and applied sciences and related occupations |
| Workers | 3K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.58 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 92.1% / 7.9% / 0.0% |
| Employment change | +43.3% |
| Unemployment | 3.3% |
| Median hourly wage | $50.29 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Computer and information systems professionals (217); Architects and statisticians (215, 216). |

### Supervisors, library, correspondence and related information workers

| Field | Value |
|-------|-------|
| NOC | 12012 |
| Category | Business, finance and administration occupations |
| Workers | 3K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.48 |
| Complementarity | 0.56 |
| HELC / HEHC / Low | 82.0% / 18.0% / 0.0% |
| Employment change | +12.1% |
| Unemployment | 2.8% |
| Median hourly wage | $34.13 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Administrative occupations in finance, insurance and business (12, 13). |

### Physicists and astronomers

| Field | Value |
|-------|-------|
| NOC | 21100 |
| Category | Natural and applied sciences and related occupations |
| Workers | 2K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.38 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 1.0% / 99.0% / 0.0% |
| Employment change | +29.2% |
| Unemployment | 1.7% |
| Median hourly wage | $44.87 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Physical and life science professionals (211, 212). |

### Metallurgical and materials engineers

| Field | Value |
|-------|-------|
| NOC | 21322 |
| Category | Natural and applied sciences and related occupations |
| Workers | 2K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.55 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 13.0% / 87.0% / 0.0% |
| Employment change | +18.1% |
| Unemployment | 2.4% |
| Median hourly wage | $52.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Engineers (213, 214). |

### Religious leaders

| Field | Value |
|-------|-------|
| NOC | 41302 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 1K |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +15.8% |
| Unemployment | 1.8% |
| Median hourly wage | $40.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Meteorologists and climatologists

| Field | Value |
|-------|-------|
| NOC | 21103 |
| Category | Natural and applied sciences and related occupations |
| Workers | 318 |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.38 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 1.0% / 99.0% / 0.0% |
| Employment change | +29.2% |
| Unemployment | 1.7% |
| Median hourly wage | $44.87 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Physical and life science professionals (211, 212). |

### Other professional occupations in physical sciences

| Field | Value |
|-------|-------|
| NOC | 21109 |
| Category | Natural and applied sciences and related occupations |
| Workers | 212 |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.38 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 1.0% / 99.0% / 0.0% |
| Employment change | +29.2% |
| Unemployment | 1.7% |
| Median hourly wage | $44.87 |
| Outlook | Very good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Physical and life science professionals (211, 212). |

### Judges

| Field | Value |
|-------|-------|
| NOC | 41100 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 0 |
| High-exposure share | 100.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.56 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 24.0% / 76.0% / 0.0% |
| Employment change | +38.2% |
| Unemployment | 1.9% |
| Median hourly wage | $62.92 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in law and social, community and government services (41). |

### Retail and wholesale trade managers

| Field | Value |
|-------|-------|
| NOC | 60020 |
| Category | Sales and service occupations |
| Workers | 336K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +0.9% |
| Unemployment | 2.1% |
| Median hourly wage | $39.05 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Computer and information systems managers

| Field | Value |
|-------|-------|
| NOC | 20012 |
| Category | Natural and applied sciences and related occupations |
| Workers | 149K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Home building and renovation managers

| Field | Value |
|-------|-------|
| NOC | 70011 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 144K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Managers in agriculture

| Field | Value |
|-------|-------|
| NOC | 80020 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 118K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Construction managers

| Field | Value |
|-------|-------|
| NOC | 70010 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 116K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Manufacturing managers

| Field | Value |
|-------|-------|
| NOC | 90010 |
| Category | Occupations in manufacturing and utilities |
| Workers | 108K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Restaurant and food service managers

| Field | Value |
|-------|-------|
| NOC | 60030 |
| Category | Sales and service occupations |
| Workers | 105K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +0.9% |
| Unemployment | 2.1% |
| Median hourly wage | $39.05 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Banking, credit and other investment managers

| Field | Value |
|-------|-------|
| NOC | 10021 |
| Category | Business, finance and administration occupations |
| Workers | 85K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Financial managers

| Field | Value |
|-------|-------|
| NOC | 10010 |
| Category | Business, finance and administration occupations |
| Workers | 85K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Advertising, marketing and public relations managers

| Field | Value |
|-------|-------|
| NOC | 10022 |
| Category | Business, finance and administration occupations |
| Workers | 65K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Human resources managers

| Field | Value |
|-------|-------|
| NOC | 10011 |
| Category | Business, finance and administration occupations |
| Workers | 63K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Managers in social, community and correctional services

| Field | Value |
|-------|-------|
| NOC | 40030 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 57K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Insurance, real estate and financial brokerage managers

| Field | Value |
|-------|-------|
| NOC | 10020 |
| Category | Business, finance and administration occupations |
| Workers | 54K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Accommodation service managers

| Field | Value |
|-------|-------|
| NOC | 60031 |
| Category | Sales and service occupations |
| Workers | 52K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +0.9% |
| Unemployment | 2.1% |
| Median hourly wage | $39.05 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Managers in health care

| Field | Value |
|-------|-------|
| NOC | 30010 |
| Category | Health occupations |
| Workers | 51K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### School principals and administrators of elementary and secondary education

| Field | Value |
|-------|-------|
| NOC | 40021 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 44K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Engineering managers

| Field | Value |
|-------|-------|
| NOC | 20010 |
| Category | Natural and applied sciences and related occupations |
| Workers | 41K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Facility operation and maintenance managers

| Field | Value |
|-------|-------|
| NOC | 70012 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 37K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Managers in transportation

| Field | Value |
|-------|-------|
| NOC | 70020 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 33K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Corporate sales managers

| Field | Value |
|-------|-------|
| NOC | 60010 |
| Category | Sales and service occupations |
| Workers | 31K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +0.9% |
| Unemployment | 2.1% |
| Median hourly wage | $39.05 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Other managers in public administration

| Field | Value |
|-------|-------|
| NOC | 40019 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 26K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Administrators - post-secondary education and vocational training

| Field | Value |
|-------|-------|
| NOC | 40020 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 24K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Purchasing managers

| Field | Value |
|-------|-------|
| NOC | 10012 |
| Category | Business, finance and administration occupations |
| Workers | 24K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Managers in customer and personal services

| Field | Value |
|-------|-------|
| NOC | 60040 |
| Category | Sales and service occupations |
| Workers | 18K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +0.9% |
| Unemployment | 2.1% |
| Median hourly wage | $39.05 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Architecture and science managers

| Field | Value |
|-------|-------|
| NOC | 20011 |
| Category | Natural and applied sciences and related occupations |
| Workers | 18K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Senior government managers and officials

| Field | Value |
|-------|-------|
| NOC | 00011 |
| Category | Legislative and senior management occupations |
| Workers | 16K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | -39.3% |
| Unemployment | ? |
| Median hourly wage | $81.54 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Utilities managers

| Field | Value |
|-------|-------|
| NOC | 90011 |
| Category | Occupations in manufacturing and utilities |
| Workers | 16K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Other business services managers

| Field | Value |
|-------|-------|
| NOC | 10029 |
| Category | Business, finance and administration occupations |
| Workers | 14K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Other administrative services managers

| Field | Value |
|-------|-------|
| NOC | 10019 |
| Category | Business, finance and administration occupations |
| Workers | 14K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Managers in natural resources production and fishing

| Field | Value |
|-------|-------|
| NOC | 80010 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 14K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Government managers - economic analysis, policy development and program administration

| Field | Value |
|-------|-------|
| NOC | 40011 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 13K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Telecommunication carriers managers

| Field | Value |
|-------|-------|
| NOC | 10030 |
| Category | Business, finance and administration occupations |
| Workers | 12K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Senior managers - financial, communications and other business services

| Field | Value |
|-------|-------|
| NOC | 00012 |
| Category | Legislative and senior management occupations |
| Workers | 12K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | -39.3% |
| Unemployment | ? |
| Median hourly wage | $81.54 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Recreation, sports and fitness program and service directors

| Field | Value |
|-------|-------|
| NOC | 50012 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 12K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Senior managers - construction, transportation, production and utilities

| Field | Value |
|-------|-------|
| NOC | 00015 |
| Category | Legislative and senior management occupations |
| Workers | 7K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | -39.3% |
| Unemployment | ? |
| Median hourly wage | $81.54 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Managers in horticulture

| Field | Value |
|-------|-------|
| NOC | 80021 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 6K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Managers - publishing, motion pictures, broadcasting and performing arts

| Field | Value |
|-------|-------|
| NOC | 50011 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 5K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Library, archive, museum and art gallery managers

| Field | Value |
|-------|-------|
| NOC | 50010 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 5K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Government managers - health and social policy development and program administration

| Field | Value |
|-------|-------|
| NOC | 40010 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 5K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Postal and courier services managers

| Field | Value |
|-------|-------|
| NOC | 70021 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 3K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Fire chiefs and senior firefighting officers

| Field | Value |
|-------|-------|
| NOC | 40041 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 2K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Commissioned police officers and related occupations in public protection services

| Field | Value |
|-------|-------|
| NOC | 40040 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 1K |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Government managers - education policy development and program administration

| Field | Value |
|-------|-------|
| NOC | 40012 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 827 |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Managers in aquaculture

| Field | Value |
|-------|-------|
| NOC | 80022 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 699 |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +7.3% |
| Unemployment | 1.7% |
| Median hourly wage | $52.20 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Legislators

| Field | Value |
|-------|-------|
| NOC | 00010 |
| Category | Legislative and senior management occupations |
| Workers | 0 |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | -39.3% |
| Unemployment | ? |
| Median hourly wage | $81.54 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Senior managers - health, education, social and community services and membership organizations

| Field | Value |
|-------|-------|
| NOC | 00013 |
| Category | Legislative and senior management occupations |
| Workers | 0 |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | -39.3% |
| Unemployment | ? |
| Median hourly wage | $81.54 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Senior managers - trade, broadcasting and other services

| Field | Value |
|-------|-------|
| NOC | 00014 |
| Category | Legislative and senior management occupations |
| Workers | 0 |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | -39.3% |
| Unemployment | ? |
| Median hourly wage | $81.54 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Commissioned officers of the Canadian Armed Forces

| Field | Value |
|-------|-------|
| NOC | 40042 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 0 |
| High-exposure share | 93.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.49 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 6.0% / 87.0% / 7.0% |
| Employment change | +61.3% |
| Unemployment | 2.4% |
| Median hourly wage | $60.10 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Management occupations (0). |

### Retail salespersons and visual merchandisers

| Field | Value |
|-------|-------|
| NOC | 64100 |
| Category | Sales and service occupations |
| Workers | 591K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Sales and account representatives - wholesale trade (non-technical)

| Field | Value |
|-------|-------|
| NOC | 64101 |
| Category | Sales and service occupations |
| Workers | 244K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Other customer and information services representatives

| Field | Value |
|-------|-------|
| NOC | 64409 |
| Category | Sales and service occupations |
| Workers | 183K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Security guards and related security service occupations

| Field | Value |
|-------|-------|
| NOC | 64410 |
| Category | Sales and service occupations |
| Workers | 103K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Customer services representatives - financial institutions

| Field | Value |
|-------|-------|
| NOC | 64400 |
| Category | Sales and service occupations |
| Workers | 68K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Maîtres d'hôtel and hosts/hostesses

| Field | Value |
|-------|-------|
| NOC | 64300 |
| Category | Sales and service occupations |
| Workers | 55K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Bartenders

| Field | Value |
|-------|-------|
| NOC | 64301 |
| Category | Sales and service occupations |
| Workers | 31K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Hotel front desk clerks

| Field | Value |
|-------|-------|
| NOC | 64314 |
| Category | Sales and service occupations |
| Workers | 19K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Pursers and flight attendants

| Field | Value |
|-------|-------|
| NOC | 64311 |
| Category | Sales and service occupations |
| Workers | 16K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Travel counsellors

| Field | Value |
|-------|-------|
| NOC | 64310 |
| Category | Sales and service occupations |
| Workers | 14K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Airline ticket and service agents

| Field | Value |
|-------|-------|
| NOC | 64312 |
| Category | Sales and service occupations |
| Workers | 14K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Tailors, dressmakers, furriers and milliners

| Field | Value |
|-------|-------|
| NOC | 64200 |
| Category | Sales and service occupations |
| Workers | 12K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Postal services representatives

| Field | Value |
|-------|-------|
| NOC | 64401 |
| Category | Sales and service occupations |
| Workers | 10K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Casino workers

| Field | Value |
|-------|-------|
| NOC | 64321 |
| Category | Sales and service occupations |
| Workers | 8K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Ground and water transport ticket agents, cargo service representatives and related clerks

| Field | Value |
|-------|-------|
| NOC | 64313 |
| Category | Sales and service occupations |
| Workers | 3K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Image, social and other personal consultants

| Field | Value |
|-------|-------|
| NOC | 64201 |
| Category | Sales and service occupations |
| Workers | 2K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Moderate |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Tour and travel guides

| Field | Value |
|-------|-------|
| NOC | 64320 |
| Category | Sales and service occupations |
| Workers | 2K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### Outdoor sport and recreational guides

| Field | Value |
|-------|-------|
| NOC | 64322 |
| Category | Sales and service occupations |
| Workers | 2K |
| High-exposure share | 89.1% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.15 |
| Complementarity | 0.54 |
| HELC / HEHC / Low | 82.8% / 6.3% / 10.9% |
| Employment change | -4.8% |
| Unemployment | 4.8% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to a weighted blend of published StatCan EPIAC occupation groups from the 2021 Census (NOC 2016): Sales representatives and salespersons in wholesale and retail trade (64); Service representatives and other customer and personal services occupations (65). |

### General practitioners and family physicians

| Field | Value |
|-------|-------|
| NOC | 31102 |
| Category | Health occupations |
| Workers | 86K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +23.2% |
| Unemployment | 0.8% |
| Median hourly wage | $51.73 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Pharmacists

| Field | Value |
|-------|-------|
| NOC | 31120 |
| Category | Health occupations |
| Workers | 54K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +23.2% |
| Unemployment | 0.8% |
| Median hourly wage | $51.73 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Specialists in clinical and laboratory medicine

| Field | Value |
|-------|-------|
| NOC | 31100 |
| Category | Health occupations |
| Workers | 39K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +23.2% |
| Unemployment | 0.8% |
| Median hourly wage | $51.73 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Physiotherapists

| Field | Value |
|-------|-------|
| NOC | 31202 |
| Category | Health occupations |
| Workers | 35K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +12.0% |
| Unemployment | ? |
| Median hourly wage | $50.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Dentists

| Field | Value |
|-------|-------|
| NOC | 31110 |
| Category | Health occupations |
| Workers | 27K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +23.2% |
| Unemployment | 0.8% |
| Median hourly wage | $51.73 |
| Outlook | Very good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Occupational therapists

| Field | Value |
|-------|-------|
| NOC | 31203 |
| Category | Health occupations |
| Workers | 23K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +12.0% |
| Unemployment | ? |
| Median hourly wage | $50.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Psychologists

| Field | Value |
|-------|-------|
| NOC | 31200 |
| Category | Health occupations |
| Workers | 21K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +12.0% |
| Unemployment | ? |
| Median hourly wage | $50.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Audiologists and speech-language pathologists

| Field | Value |
|-------|-------|
| NOC | 31112 |
| Category | Health occupations |
| Workers | 20K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +23.2% |
| Unemployment | 0.8% |
| Median hourly wage | $51.73 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Dietitians and nutritionists

| Field | Value |
|-------|-------|
| NOC | 31121 |
| Category | Health occupations |
| Workers | 15K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +23.2% |
| Unemployment | 0.8% |
| Median hourly wage | $51.73 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Veterinarians

| Field | Value |
|-------|-------|
| NOC | 31103 |
| Category | Health occupations |
| Workers | 14K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +23.2% |
| Unemployment | 0.8% |
| Median hourly wage | $51.73 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Specialists in surgery

| Field | Value |
|-------|-------|
| NOC | 31101 |
| Category | Health occupations |
| Workers | 11K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +23.2% |
| Unemployment | 0.8% |
| Median hourly wage | $51.73 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Kinesiologists and other professional occupations in therapy and assessment

| Field | Value |
|-------|-------|
| NOC | 31204 |
| Category | Health occupations |
| Workers | 10K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +12.0% |
| Unemployment | ? |
| Median hourly wage | $50.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Chiropractors

| Field | Value |
|-------|-------|
| NOC | 31201 |
| Category | Health occupations |
| Workers | 9K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +12.0% |
| Unemployment | ? |
| Median hourly wage | $50.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Optometrists

| Field | Value |
|-------|-------|
| NOC | 31111 |
| Category | Health occupations |
| Workers | 8K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +23.2% |
| Unemployment | 0.8% |
| Median hourly wage | $51.73 |
| Outlook | Very good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Other professional occupations in health diagnosing and treating

| Field | Value |
|-------|-------|
| NOC | 31209 |
| Category | Health occupations |
| Workers | 7K |
| High-exposure share | 86.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.29 |
| Complementarity | 0.73 |
| HELC / HEHC / Low | 0.0% / 86.0% / 14.0% |
| Employment change | +12.0% |
| Unemployment | ? |
| Median hourly wage | $50.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Professional occupations in health (except nursing) (31). |

### Program leaders and instructors in recreation, sport and fitness

| Field | Value |
|-------|-------|
| NOC | 54100 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 191K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +32.7% |
| Unemployment | 5.6% |
| Median hourly wage | $20.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Graphic designers and illustrators

| Field | Value |
|-------|-------|
| NOC | 52120 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 90K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +20.8% |
| Unemployment | 6.2% |
| Median hourly wage | $33.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Producers, directors, choreographers and related occupations

| Field | Value |
|-------|-------|
| NOC | 51120 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 51K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Translators, terminologists and interpreters

| Field | Value |
|-------|-------|
| NOC | 51114 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 39K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Photographers

| Field | Value |
|-------|-------|
| NOC | 53110 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 38K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Interior designers and interior decorators

| Field | Value |
|-------|-------|
| NOC | 52121 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 28K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +20.8% |
| Unemployment | 6.2% |
| Median hourly wage | $33.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Editors

| Field | Value |
|-------|-------|
| NOC | 51110 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 26K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Motion pictures, broadcasting, photography and performing arts assistants and operators

| Field | Value |
|-------|-------|
| NOC | 53111 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 24K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Registrars, restorers, interpreters and other occupations related to museum and art galleries

| Field | Value |
|-------|-------|
| NOC | 53100 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 21K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Librarians

| Field | Value |
|-------|-------|
| NOC | 51100 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 20K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Journalists

| Field | Value |
|-------|-------|
| NOC | 51113 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 19K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Theatre, fashion, exhibit and other creative designers

| Field | Value |
|-------|-------|
| NOC | 53123 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 19K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Technical writers

| Field | Value |
|-------|-------|
| NOC | 51112 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 15K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Graphic arts technicians

| Field | Value |
|-------|-------|
| NOC | 52111 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 13K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +20.8% |
| Unemployment | 6.2% |
| Median hourly wage | $33.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Audio and video recording technicians

| Field | Value |
|-------|-------|
| NOC | 52113 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 13K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +20.8% |
| Unemployment | 6.2% |
| Median hourly wage | $33.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Other technical and coordinating occupations in motion pictures, broadcasting and the performing arts

| Field | Value |
|-------|-------|
| NOC | 52119 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 11K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +20.8% |
| Unemployment | 6.2% |
| Median hourly wage | $33.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Coaches

| Field | Value |
|-------|-------|
| NOC | 53201 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 9K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Library and public archive technicians

| Field | Value |
|-------|-------|
| NOC | 52100 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 8K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +20.8% |
| Unemployment | 6.2% |
| Median hourly wage | $33.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Film and video camera operators

| Field | Value |
|-------|-------|
| NOC | 52110 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 6K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +20.8% |
| Unemployment | 6.2% |
| Median hourly wage | $33.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Announcers and other broadcasters

| Field | Value |
|-------|-------|
| NOC | 52114 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 5K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +20.8% |
| Unemployment | 6.2% |
| Median hourly wage | $33.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Conservators and curators

| Field | Value |
|-------|-------|
| NOC | 51101 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 3K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Archivists

| Field | Value |
|-------|-------|
| NOC | 51102 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 2K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Broadcast technicians

| Field | Value |
|-------|-------|
| NOC | 52112 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 2K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +20.8% |
| Unemployment | 6.2% |
| Median hourly wage | $33.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Artisans and craftspersons

| Field | Value |
|-------|-------|
| NOC | 53124 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 1K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Patternmakers - textile, leather and fur products

| Field | Value |
|-------|-------|
| NOC | 53125 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 1K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Sports officials and referees

| Field | Value |
|-------|-------|
| NOC | 53202 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 1K |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Authors and writers (except technical)

| Field | Value |
|-------|-------|
| NOC | 51111 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 739 |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Conductors, composers and arrangers

| Field | Value |
|-------|-------|
| NOC | 51121 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 0 |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Musicians and singers

| Field | Value |
|-------|-------|
| NOC | 51122 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 0 |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +15.8% |
| Unemployment | 3.2% |
| Median hourly wage | $39.11 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Dancers

| Field | Value |
|-------|-------|
| NOC | 53120 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 0 |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Actors, comedians and circus performers

| Field | Value |
|-------|-------|
| NOC | 53121 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 0 |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Painters, sculptors and other visual artists

| Field | Value |
|-------|-------|
| NOC | 53122 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 0 |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Athletes

| Field | Value |
|-------|-------|
| NOC | 53200 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 0 |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | -2.2% |
| Unemployment | 7.9% |
| Median hourly wage | $26.50 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Other performers

| Field | Value |
|-------|-------|
| NOC | 55109 |
| Category | Occupations in art, culture, recreation and sport |
| Workers | 0 |
| High-exposure share | 79.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.11 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 46.0% / 33.0% / 21.0% |
| Employment change | +32.7% |
| Unemployment | 5.6% |
| Median hourly wage | $20.00 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Occupations in art, culture, recreation and sports (51, 52). |

### Receptionists

| Field | Value |
|-------|-------|
| NOC | 14101 |
| Category | Business, finance and administration occupations |
| Workers | 155K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Accounting and related clerks

| Field | Value |
|-------|-------|
| NOC | 14200 |
| Category | Business, finance and administration occupations |
| Workers | 153K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### General office support workers

| Field | Value |
|-------|-------|
| NOC | 14100 |
| Category | Business, finance and administration occupations |
| Workers | 139K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Shippers and receivers

| Field | Value |
|-------|-------|
| NOC | 14400 |
| Category | Business, finance and administration occupations |
| Workers | 122K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Data entry clerks

| Field | Value |
|-------|-------|
| NOC | 14111 |
| Category | Business, finance and administration occupations |
| Workers | 38K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Banking, insurance and other financial clerks

| Field | Value |
|-------|-------|
| NOC | 14201 |
| Category | Business, finance and administration occupations |
| Workers | 35K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Dispatchers

| Field | Value |
|-------|-------|
| NOC | 14404 |
| Category | Business, finance and administration occupations |
| Workers | 34K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Purchasing and inventory control workers

| Field | Value |
|-------|-------|
| NOC | 14403 |
| Category | Business, finance and administration occupations |
| Workers | 31K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Storekeepers and partspersons

| Field | Value |
|-------|-------|
| NOC | 14401 |
| Category | Business, finance and administration occupations |
| Workers | 23K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Correspondence, publication and regulatory clerks

| Field | Value |
|-------|-------|
| NOC | 14301 |
| Category | Business, finance and administration occupations |
| Workers | 22K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Library assistants and clerks

| Field | Value |
|-------|-------|
| NOC | 14300 |
| Category | Business, finance and administration occupations |
| Workers | 16K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Survey interviewers and statistical clerks

| Field | Value |
|-------|-------|
| NOC | 14110 |
| Category | Business, finance and administration occupations |
| Workers | 12K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Collection clerks

| Field | Value |
|-------|-------|
| NOC | 14202 |
| Category | Business, finance and administration occupations |
| Workers | 11K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Personnel clerks

| Field | Value |
|-------|-------|
| NOC | 14102 |
| Category | Business, finance and administration occupations |
| Workers | 11K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Production logistics workers

| Field | Value |
|-------|-------|
| NOC | 14402 |
| Category | Business, finance and administration occupations |
| Workers | 7K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Court clerks and related court services occupations

| Field | Value |
|-------|-------|
| NOC | 14103 |
| Category | Business, finance and administration occupations |
| Workers | 6K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Transportation route and crew schedulers

| Field | Value |
|-------|-------|
| NOC | 14405 |
| Category | Business, finance and administration occupations |
| Workers | 4K |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### Desktop publishing operators and related occupations

| Field | Value |
|-------|-------|
| NOC | 14112 |
| Category | Business, finance and administration occupations |
| Workers | 472 |
| High-exposure share | 76.0% |
| Dominant EPIAC group | High exposure, low complementarity |
| AIOE | 6.22 |
| Complementarity | 0.50 |
| HELC / HEHC / Low | 76.0% / 0.0% / 24.0% |
| Employment change | +2.3% |
| Unemployment | 4.4% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Office support and co-ordination occupations (14, 15). |

### User support technicians

| Field | Value |
|-------|-------|
| NOC | 22221 |
| Category | Natural and applied sciences and related occupations |
| Workers | 129K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Computer network and web technicians

| Field | Value |
|-------|-------|
| NOC | 22220 |
| Category | Natural and applied sciences and related occupations |
| Workers | 52K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Electronic service technicians (household and business equipment)

| Field | Value |
|-------|-------|
| NOC | 22311 |
| Category | Natural and applied sciences and related occupations |
| Workers | 52K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Drafting technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22212 |
| Category | Natural and applied sciences and related occupations |
| Workers | 41K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Occupational health and safety specialists

| Field | Value |
|-------|-------|
| NOC | 22232 |
| Category | Natural and applied sciences and related occupations |
| Workers | 40K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Electrical and electronics engineering technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22310 |
| Category | Natural and applied sciences and related occupations |
| Workers | 36K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Civil engineering technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22300 |
| Category | Natural and applied sciences and related occupations |
| Workers | 30K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Chemical technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22100 |
| Category | Natural and applied sciences and related occupations |
| Workers | 28K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Construction inspectors

| Field | Value |
|-------|-------|
| NOC | 22233 |
| Category | Natural and applied sciences and related occupations |
| Workers | 28K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Mechanical engineering technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22301 |
| Category | Natural and applied sciences and related occupations |
| Workers | 28K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Construction estimators

| Field | Value |
|-------|-------|
| NOC | 22303 |
| Category | Natural and applied sciences and related occupations |
| Workers | 26K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Industrial engineering and manufacturing technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22302 |
| Category | Natural and applied sciences and related occupations |
| Workers | 23K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Information systems testing technicians

| Field | Value |
|-------|-------|
| NOC | 22222 |
| Category | Natural and applied sciences and related occupations |
| Workers | 22K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Landscape and horticulture technicians and specialists

| Field | Value |
|-------|-------|
| NOC | 22114 |
| Category | Natural and applied sciences and related occupations |
| Workers | 19K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Architectural technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22210 |
| Category | Natural and applied sciences and related occupations |
| Workers | 14K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Industrial designers

| Field | Value |
|-------|-------|
| NOC | 22211 |
| Category | Natural and applied sciences and related occupations |
| Workers | 13K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Industrial instrument technicians and mechanics

| Field | Value |
|-------|-------|
| NOC | 22312 |
| Category | Natural and applied sciences and related occupations |
| Workers | 12K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Biological technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22110 |
| Category | Natural and applied sciences and related occupations |
| Workers | 11K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Technical occupations in geomatics and meteorology

| Field | Value |
|-------|-------|
| NOC | 22214 |
| Category | Natural and applied sciences and related occupations |
| Workers | 9K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Geological and mineral technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22101 |
| Category | Natural and applied sciences and related occupations |
| Workers | 9K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Non-destructive testers and inspectors

| Field | Value |
|-------|-------|
| NOC | 22230 |
| Category | Natural and applied sciences and related occupations |
| Workers | 7K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Engineering inspectors and regulatory officers

| Field | Value |
|-------|-------|
| NOC | 22231 |
| Category | Natural and applied sciences and related occupations |
| Workers | 7K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Land survey technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22213 |
| Category | Natural and applied sciences and related occupations |
| Workers | 7K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Forestry technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 22112 |
| Category | Natural and applied sciences and related occupations |
| Workers | 6K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Aircraft instrument, electrical and avionics mechanics, technicians and inspectors

| Field | Value |
|-------|-------|
| NOC | 22313 |
| Category | Natural and applied sciences and related occupations |
| Workers | 5K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Conservation and fishery officers

| Field | Value |
|-------|-------|
| NOC | 22113 |
| Category | Natural and applied sciences and related occupations |
| Workers | 4K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Agricultural and fish products inspectors

| Field | Value |
|-------|-------|
| NOC | 22111 |
| Category | Natural and applied sciences and related occupations |
| Workers | 4K |
| High-exposure share | 74.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.17 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 34.0% / 40.0% / 26.0% |
| Employment change | +17.8% |
| Unemployment | 3.9% |
| Median hourly wage | $36.92 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations related to natural and applied sciences (22). |

### Early childhood educators and assistants

| Field | Value |
|-------|-------|
| NOC | 42202 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 284K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +14.9% |
| Unemployment | 3.6% |
| Median hourly wage | $26.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Social and community service workers

| Field | Value |
|-------|-------|
| NOC | 42201 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 185K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +14.9% |
| Unemployment | 3.6% |
| Median hourly wage | $26.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Elementary and secondary school teacher assistants

| Field | Value |
|-------|-------|
| NOC | 43100 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 125K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +33.5% |
| Unemployment | 5.6% |
| Median hourly wage | $29.74 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Police officers (except commissioned)

| Field | Value |
|-------|-------|
| NOC | 42100 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 92K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +34.7% |
| Unemployment | ? |
| Median hourly wage | $50.08 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Home support workers, caregivers and related occupations

| Field | Value |
|-------|-------|
| NOC | 44101 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 71K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | -8.4% |
| Unemployment | 4.4% |
| Median hourly wage | $21.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Paralegals and related occupations

| Field | Value |
|-------|-------|
| NOC | 42200 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 47K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +14.9% |
| Unemployment | 3.6% |
| Median hourly wage | $26.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Firefighters

| Field | Value |
|-------|-------|
| NOC | 42101 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 45K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +34.7% |
| Unemployment | ? |
| Median hourly wage | $50.08 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Correctional service officers

| Field | Value |
|-------|-------|
| NOC | 43201 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 30K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +33.5% |
| Unemployment | 5.6% |
| Median hourly wage | $29.74 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Home child care providers

| Field | Value |
|-------|-------|
| NOC | 44100 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 24K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | -8.4% |
| Unemployment | 4.4% |
| Median hourly wage | $21.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Other instructors

| Field | Value |
|-------|-------|
| NOC | 43109 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 24K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +33.5% |
| Unemployment | 5.6% |
| Median hourly wage | $29.74 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Student monitors, crossing guards and related occupations

| Field | Value |
|-------|-------|
| NOC | 45100 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 23K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | -8.4% |
| Unemployment | 4.4% |
| Median hourly wage | $21.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Border services, customs, and immigration officers

| Field | Value |
|-------|-------|
| NOC | 43203 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 21K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +33.5% |
| Unemployment | 5.6% |
| Median hourly wage | $29.74 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### By-law enforcement and other regulatory officers

| Field | Value |
|-------|-------|
| NOC | 43202 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 12K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +33.5% |
| Unemployment | 5.6% |
| Median hourly wage | $29.74 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Instructors of persons with disabilities

| Field | Value |
|-------|-------|
| NOC | 42203 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 6K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +14.9% |
| Unemployment | 3.6% |
| Median hourly wage | $26.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Sheriffs and bailiffs

| Field | Value |
|-------|-------|
| NOC | 43200 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 3K |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +33.5% |
| Unemployment | 5.6% |
| Median hourly wage | $29.74 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Religion workers

| Field | Value |
|-------|-------|
| NOC | 42204 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 454 |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +14.9% |
| Unemployment | 3.6% |
| Median hourly wage | $26.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Specialized members of the Canadian Armed Forces

| Field | Value |
|-------|-------|
| NOC | 42102 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 0 |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +34.7% |
| Unemployment | ? |
| Median hourly wage | $50.08 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Operations members of the Canadian Armed Forces

| Field | Value |
|-------|-------|
| NOC | 43204 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 0 |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | +33.5% |
| Unemployment | 5.6% |
| Median hourly wage | $29.74 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Primary combat members of the Canadian Armed Forces

| Field | Value |
|-------|-------|
| NOC | 44200 |
| Category | Occupations in education, law and social, community and government services |
| Workers | 0 |
| High-exposure share | 66.0% |
| Dominant EPIAC group | High exposure, high complementarity |
| AIOE | 6.12 |
| Complementarity | 0.63 |
| HELC / HEHC / Low | 32.0% / 34.0% / 34.0% |
| Employment change | -8.4% |
| Unemployment | 4.4% |
| Median hourly wage | $21.00 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in law and social services (42, 43, 44). |

### Retail sales supervisors

| Field | Value |
|-------|-------|
| NOC | 62010 |
| Category | Sales and service occupations |
| Workers | 243K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Cooks

| Field | Value |
|-------|-------|
| NOC | 63200 |
| Category | Sales and service occupations |
| Workers | 196K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Technical sales specialists - wholesale trade

| Field | Value |
|-------|-------|
| NOC | 62100 |
| Category | Sales and service occupations |
| Workers | 136K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Real estate agents and salespersons

| Field | Value |
|-------|-------|
| NOC | 63101 |
| Category | Sales and service occupations |
| Workers | 128K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Hairstylists and barbers

| Field | Value |
|-------|-------|
| NOC | 63210 |
| Category | Sales and service occupations |
| Workers | 100K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Insurance agents and brokers

| Field | Value |
|-------|-------|
| NOC | 63100 |
| Category | Sales and service occupations |
| Workers | 96K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Estheticians, electrologists and related occupations

| Field | Value |
|-------|-------|
| NOC | 63211 |
| Category | Sales and service occupations |
| Workers | 75K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Food service supervisors

| Field | Value |
|-------|-------|
| NOC | 62020 |
| Category | Sales and service occupations |
| Workers | 73K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Financial sales representatives

| Field | Value |
|-------|-------|
| NOC | 63102 |
| Category | Sales and service occupations |
| Workers | 73K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Chefs

| Field | Value |
|-------|-------|
| NOC | 62200 |
| Category | Sales and service occupations |
| Workers | 62K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Cleaning supervisors

| Field | Value |
|-------|-------|
| NOC | 62024 |
| Category | Sales and service occupations |
| Workers | 40K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Bakers

| Field | Value |
|-------|-------|
| NOC | 63202 |
| Category | Sales and service occupations |
| Workers | 35K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Retail and wholesale buyers

| Field | Value |
|-------|-------|
| NOC | 62101 |
| Category | Sales and service occupations |
| Workers | 27K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Customer and information services supervisors

| Field | Value |
|-------|-------|
| NOC | 62023 |
| Category | Sales and service occupations |
| Workers | 26K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Butchers - retail and wholesale

| Field | Value |
|-------|-------|
| NOC | 63201 |
| Category | Sales and service occupations |
| Workers | 15K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Accommodation, travel, tourism and related services supervisors

| Field | Value |
|-------|-------|
| NOC | 62022 |
| Category | Sales and service occupations |
| Workers | 14K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Other services supervisors

| Field | Value |
|-------|-------|
| NOC | 62029 |
| Category | Sales and service occupations |
| Workers | 14K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Funeral directors and embalmers

| Field | Value |
|-------|-------|
| NOC | 62201 |
| Category | Sales and service occupations |
| Workers | 6K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Upholsterers

| Field | Value |
|-------|-------|
| NOC | 63221 |
| Category | Sales and service occupations |
| Workers | 5K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Jewellers, jewellery and watch repairers and related occupations

| Field | Value |
|-------|-------|
| NOC | 62202 |
| Category | Sales and service occupations |
| Workers | 4K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Executive housekeepers

| Field | Value |
|-------|-------|
| NOC | 62021 |
| Category | Sales and service occupations |
| Workers | 2K |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | -5.2% |
| Unemployment | 3.2% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Shoe repairers and shoemakers

| Field | Value |
|-------|-------|
| NOC | 63220 |
| Category | Sales and service occupations |
| Workers | 0 |
| High-exposure share | 46.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 6.09 |
| Complementarity | 0.60 |
| HELC / HEHC / Low | 19.0% / 27.0% / 54.0% |
| Employment change | +0.4% |
| Unemployment | 2.9% |
| Median hourly wage | $22.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Sales and service supervisors (62, 63). |

### Licensed practical nurses

| Field | Value |
|-------|-------|
| NOC | 32101 |
| Category | Health occupations |
| Workers | 78K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Massage therapists

| Field | Value |
|-------|-------|
| NOC | 32201 |
| Category | Health occupations |
| Workers | 44K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Paramedical occupations

| Field | Value |
|-------|-------|
| NOC | 32102 |
| Category | Health occupations |
| Workers | 40K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Dental hygienists and dental therapists

| Field | Value |
|-------|-------|
| NOC | 32111 |
| Category | Health occupations |
| Workers | 38K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Pharmacy technicians

| Field | Value |
|-------|-------|
| NOC | 32124 |
| Category | Health occupations |
| Workers | 33K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Medical radiation technologists

| Field | Value |
|-------|-------|
| NOC | 32121 |
| Category | Health occupations |
| Workers | 30K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Animal health technologists and veterinary technicians

| Field | Value |
|-------|-------|
| NOC | 32104 |
| Category | Health occupations |
| Workers | 27K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Medical laboratory technologists

| Field | Value |
|-------|-------|
| NOC | 32120 |
| Category | Health occupations |
| Workers | 27K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Other technical occupations in therapy and assessment

| Field | Value |
|-------|-------|
| NOC | 32109 |
| Category | Health occupations |
| Workers | 25K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Respiratory therapists, clinical perfusionists and cardiopulmonary technologists

| Field | Value |
|-------|-------|
| NOC | 32103 |
| Category | Health occupations |
| Workers | 16K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Opticians

| Field | Value |
|-------|-------|
| NOC | 32100 |
| Category | Health occupations |
| Workers | 10K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Medical sonographers

| Field | Value |
|-------|-------|
| NOC | 32122 |
| Category | Health occupations |
| Workers | 9K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Other medical technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 32129 |
| Category | Health occupations |
| Workers | 7K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Traditional Chinese medicine practitioners and acupuncturists

| Field | Value |
|-------|-------|
| NOC | 32200 |
| Category | Health occupations |
| Workers | 6K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Dental technologists and technicians

| Field | Value |
|-------|-------|
| NOC | 32112 |
| Category | Health occupations |
| Workers | 6K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Other practitioners of natural healing

| Field | Value |
|-------|-------|
| NOC | 32209 |
| Category | Health occupations |
| Workers | 5K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Cardiology technologists and electrophysiological diagnostic technologists

| Field | Value |
|-------|-------|
| NOC | 32123 |
| Category | Health occupations |
| Workers | 4K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Denturists

| Field | Value |
|-------|-------|
| NOC | 32110 |
| Category | Health occupations |
| Workers | 2K |
| High-exposure share | 31.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.89 |
| Complementarity | 0.62 |
| HELC / HEHC / Low | 13.0% / 18.0% / 69.0% |
| Employment change | +16.5% |
| Unemployment | 1.0% |
| Median hourly wage | $35.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Technical occupations in health (32). |

### Process control and machine operators, food and beverage processing

| Field | Value |
|-------|-------|
| NOC | 94140 |
| Category | Occupations in manufacturing and utilities |
| Workers | 73K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Other products assemblers, finishers and inspectors

| Field | Value |
|-------|-------|
| NOC | 94219 |
| Category | Occupations in manufacturing and utilities |
| Workers | 45K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Machine operators of other metal products

| Field | Value |
|-------|-------|
| NOC | 94107 |
| Category | Occupations in manufacturing and utilities |
| Workers | 31K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Motor vehicle assemblers, inspectors and testers

| Field | Value |
|-------|-------|
| NOC | 94200 |
| Category | Occupations in manufacturing and utilities |
| Workers | 31K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Furniture and fixture assemblers, finishers, refinishers and inspectors

| Field | Value |
|-------|-------|
| NOC | 94210 |
| Category | Occupations in manufacturing and utilities |
| Workers | 30K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, food and beverage processing

| Field | Value |
|-------|-------|
| NOC | 92012 |
| Category | Occupations in manufacturing and utilities |
| Workers | 29K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Power engineers and power systems operators

| Field | Value |
|-------|-------|
| NOC | 92100 |
| Category | Occupations in manufacturing and utilities |
| Workers | 29K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Metalworking and forging machine operators

| Field | Value |
|-------|-------|
| NOC | 94105 |
| Category | Occupations in manufacturing and utilities |
| Workers | 26K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, other mechanical and metal products manufacturing

| Field | Value |
|-------|-------|
| NOC | 92023 |
| Category | Occupations in manufacturing and utilities |
| Workers | 23K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Electronics assemblers, fabricators, inspectors and testers

| Field | Value |
|-------|-------|
| NOC | 94201 |
| Category | Occupations in manufacturing and utilities |
| Workers | 20K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Central control and process operators, petroleum, gas and chemical processing

| Field | Value |
|-------|-------|
| NOC | 93101 |
| Category | Occupations in manufacturing and utilities |
| Workers | 18K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Chemical plant machine operators

| Field | Value |
|-------|-------|
| NOC | 94110 |
| Category | Occupations in manufacturing and utilities |
| Workers | 18K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Mechanical assemblers and inspectors

| Field | Value |
|-------|-------|
| NOC | 94204 |
| Category | Occupations in manufacturing and utilities |
| Workers | 18K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Industrial butchers and meat cutters, poultry preparers and related workers

| Field | Value |
|-------|-------|
| NOC | 94141 |
| Category | Occupations in manufacturing and utilities |
| Workers | 18K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Industrial sewing machine operators

| Field | Value |
|-------|-------|
| NOC | 94132 |
| Category | Occupations in manufacturing and utilities |
| Workers | 17K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Plastics processing machine operators

| Field | Value |
|-------|-------|
| NOC | 94111 |
| Category | Occupations in manufacturing and utilities |
| Workers | 16K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Industrial painters, coaters and metal finishing process operators

| Field | Value |
|-------|-------|
| NOC | 94213 |
| Category | Occupations in manufacturing and utilities |
| Workers | 16K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, motor vehicle assembling

| Field | Value |
|-------|-------|
| NOC | 92020 |
| Category | Occupations in manufacturing and utilities |
| Workers | 12K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Assemblers and inspectors of other wood products

| Field | Value |
|-------|-------|
| NOC | 94211 |
| Category | Occupations in manufacturing and utilities |
| Workers | 12K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Water and waste treatment plant operators

| Field | Value |
|-------|-------|
| NOC | 92101 |
| Category | Occupations in manufacturing and utilities |
| Workers | 12K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Machine operators, mineral and metal processing

| Field | Value |
|-------|-------|
| NOC | 94100 |
| Category | Occupations in manufacturing and utilities |
| Workers | 12K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Machining tool operators

| Field | Value |
|-------|-------|
| NOC | 94106 |
| Category | Occupations in manufacturing and utilities |
| Workers | 12K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, petroleum, gas and chemical processing and utilities

| Field | Value |
|-------|-------|
| NOC | 92011 |
| Category | Occupations in manufacturing and utilities |
| Workers | 12K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, forest products processing

| Field | Value |
|-------|-------|
| NOC | 92014 |
| Category | Occupations in manufacturing and utilities |
| Workers | 12K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Assemblers and inspectors, electrical appliance, apparatus and equipment manufacturing

| Field | Value |
|-------|-------|
| NOC | 94202 |
| Category | Occupations in manufacturing and utilities |
| Workers | 11K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Aircraft assemblers and aircraft assembly inspectors

| Field | Value |
|-------|-------|
| NOC | 93200 |
| Category | Occupations in manufacturing and utilities |
| Workers | 11K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Testers and graders, food and beverage processing

| Field | Value |
|-------|-------|
| NOC | 94143 |
| Category | Occupations in manufacturing and utilities |
| Workers | 10K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, other products manufacturing and assembly

| Field | Value |
|-------|-------|
| NOC | 92024 |
| Category | Occupations in manufacturing and utilities |
| Workers | 9K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Plastic products assemblers, finishers and inspectors

| Field | Value |
|-------|-------|
| NOC | 94212 |
| Category | Occupations in manufacturing and utilities |
| Workers | 9K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Assemblers, fabricators and inspectors, industrial electrical motors and transformers

| Field | Value |
|-------|-------|
| NOC | 94203 |
| Category | Occupations in manufacturing and utilities |
| Workers | 9K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, mineral and metal processing

| Field | Value |
|-------|-------|
| NOC | 92010 |
| Category | Occupations in manufacturing and utilities |
| Workers | 8K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, plastic and rubber products manufacturing

| Field | Value |
|-------|-------|
| NOC | 92013 |
| Category | Occupations in manufacturing and utilities |
| Workers | 8K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Sawmill machine operators

| Field | Value |
|-------|-------|
| NOC | 94120 |
| Category | Occupations in manufacturing and utilities |
| Workers | 8K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Rubber processing machine operators and related workers

| Field | Value |
|-------|-------|
| NOC | 94112 |
| Category | Occupations in manufacturing and utilities |
| Workers | 7K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Woodworking machine operators

| Field | Value |
|-------|-------|
| NOC | 94124 |
| Category | Occupations in manufacturing and utilities |
| Workers | 7K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Pulp mill, papermaking and finishing machine operators

| Field | Value |
|-------|-------|
| NOC | 94121 |
| Category | Occupations in manufacturing and utilities |
| Workers | 7K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Plateless printing equipment operators

| Field | Value |
|-------|-------|
| NOC | 94150 |
| Category | Occupations in manufacturing and utilities |
| Workers | 6K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Paper converting machine operators

| Field | Value |
|-------|-------|
| NOC | 94122 |
| Category | Occupations in manufacturing and utilities |
| Workers | 6K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, furniture and fixtures manufacturing

| Field | Value |
|-------|-------|
| NOC | 92022 |
| Category | Occupations in manufacturing and utilities |
| Workers | 5K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Concrete, clay and stone forming operators

| Field | Value |
|-------|-------|
| NOC | 94103 |
| Category | Occupations in manufacturing and utilities |
| Workers | 5K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Other wood processing machine operators

| Field | Value |
|-------|-------|
| NOC | 94129 |
| Category | Occupations in manufacturing and utilities |
| Workers | 5K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, electronics and electrical products manufacturing

| Field | Value |
|-------|-------|
| NOC | 92021 |
| Category | Occupations in manufacturing and utilities |
| Workers | 5K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Fish and seafood plant workers

| Field | Value |
|-------|-------|
| NOC | 94142 |
| Category | Occupations in manufacturing and utilities |
| Workers | 4K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Binding and finishing machine operators

| Field | Value |
|-------|-------|
| NOC | 94152 |
| Category | Occupations in manufacturing and utilities |
| Workers | 3K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Inspectors and testers, mineral and metal processing

| Field | Value |
|-------|-------|
| NOC | 94104 |
| Category | Occupations in manufacturing and utilities |
| Workers | 3K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Glass forming and finishing machine operators and glass cutters

| Field | Value |
|-------|-------|
| NOC | 94102 |
| Category | Occupations in manufacturing and utilities |
| Workers | 3K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Foundry workers

| Field | Value |
|-------|-------|
| NOC | 94101 |
| Category | Occupations in manufacturing and utilities |
| Workers | 3K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Lumber graders and other wood processing inspectors and graders

| Field | Value |
|-------|-------|
| NOC | 94123 |
| Category | Occupations in manufacturing and utilities |
| Workers | 3K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Textile fibre and yarn, hide and pelt processing machine operators and workers

| Field | Value |
|-------|-------|
| NOC | 94130 |
| Category | Occupations in manufacturing and utilities |
| Workers | 3K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Central control and process operators, mineral and metal processing

| Field | Value |
|-------|-------|
| NOC | 93100 |
| Category | Occupations in manufacturing and utilities |
| Workers | 2K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Weavers, knitters and other fabric making occupations

| Field | Value |
|-------|-------|
| NOC | 94131 |
| Category | Occupations in manufacturing and utilities |
| Workers | 2K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Camera, platemaking and other prepress occupations

| Field | Value |
|-------|-------|
| NOC | 94151 |
| Category | Occupations in manufacturing and utilities |
| Workers | 2K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Inspectors and graders, textile, fabric, fur and leather products manufacturing

| Field | Value |
|-------|-------|
| NOC | 94133 |
| Category | Occupations in manufacturing and utilities |
| Workers | 1K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Supervisors, textile, fabric, fur and leather products processing and manufacturing

| Field | Value |
|-------|-------|
| NOC | 92015 |
| Category | Occupations in manufacturing and utilities |
| Workers | 1K |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Photographic and film processors

| Field | Value |
|-------|-------|
| NOC | 94153 |
| Category | Occupations in manufacturing and utilities |
| Workers | 665 |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Machine operators and inspectors, electrical apparatus manufacturing

| Field | Value |
|-------|-------|
| NOC | 94205 |
| Category | Occupations in manufacturing and utilities |
| Workers | 665 |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | +1.5% |
| Unemployment | 4.3% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Pulping, papermaking and coating control operators

| Field | Value |
|-------|-------|
| NOC | 93102 |
| Category | Occupations in manufacturing and utilities |
| Workers | 589 |
| High-exposure share | 10.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.73 |
| Complementarity | 0.58 |
| HELC / HEHC / Low | 0.0% / 10.0% / 90.0% |
| Employment change | -9.9% |
| Unemployment | 2.0% |
| Median hourly wage | $39.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Machine operators and supervisors in manufacturing and utilities (92, 94). |

### Transport truck drivers

| Field | Value |
|-------|-------|
| NOC | 73300 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 334K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Bus drivers, subway operators and other transit operators

| Field | Value |
|-------|-------|
| NOC | 73301 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 101K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Heavy equipment operators

| Field | Value |
|-------|-------|
| NOC | 73400 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 89K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### General building maintenance workers and building superintendents

| Field | Value |
|-------|-------|
| NOC | 73201 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 79K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Residential and commercial installers and servicers

| Field | Value |
|-------|-------|
| NOC | 73200 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 58K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Painters and decorators (except interior decorators)

| Field | Value |
|-------|-------|
| NOC | 73112 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 43K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Plasterers, drywall installers and finishers and lathers

| Field | Value |
|-------|-------|
| NOC | 73102 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 29K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Roofers and shinglers

| Field | Value |
|-------|-------|
| NOC | 73110 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 21K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Other repairers and servicers

| Field | Value |
|-------|-------|
| NOC | 73209 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 15K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Floor covering installers

| Field | Value |
|-------|-------|
| NOC | 73113 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 15K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Concrete finishers

| Field | Value |
|-------|-------|
| NOC | 73100 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 15K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Printing press operators

| Field | Value |
|-------|-------|
| NOC | 73401 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 14K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Tilesetters

| Field | Value |
|-------|-------|
| NOC | 73101 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 9K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Railway and yard locomotive engineers

| Field | Value |
|-------|-------|
| NOC | 73310 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 8K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Glaziers

| Field | Value |
|-------|-------|
| NOC | 73111 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 8K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Railway conductors and brakemen/women

| Field | Value |
|-------|-------|
| NOC | 73311 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 6K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Pest controllers and fumigators

| Field | Value |
|-------|-------|
| NOC | 73202 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 5K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Drillers and blasters - surface mining, quarrying and construction

| Field | Value |
|-------|-------|
| NOC | 73402 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 4K |
| High-exposure share | 7.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.65 |
| Complementarity | 0.66 |
| HELC / HEHC / Low | 0.0% / 7.0% / 93.0% |
| Employment change | +6.5% |
| Unemployment | 5.7% |
| Median hourly wage | $29.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Maintenance and equipment operation trades (73). |

### Food counter attendants, kitchen helpers and related support occupations

| Field | Value |
|-------|-------|
| NOC | 65201 |
| Category | Sales and service occupations |
| Workers | 383K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Cashiers

| Field | Value |
|-------|-------|
| NOC | 65100 |
| Category | Sales and service occupations |
| Workers | 342K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Store shelf stockers, clerks and order fillers

| Field | Value |
|-------|-------|
| NOC | 65102 |
| Category | Sales and service occupations |
| Workers | 271K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Light duty cleaners

| Field | Value |
|-------|-------|
| NOC | 65310 |
| Category | Sales and service occupations |
| Workers | 242K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Food and beverage servers

| Field | Value |
|-------|-------|
| NOC | 65200 |
| Category | Sales and service occupations |
| Workers | 179K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Janitors, caretakers and heavy-duty cleaners

| Field | Value |
|-------|-------|
| NOC | 65312 |
| Category | Sales and service occupations |
| Workers | 108K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Operators and attendants in amusement, recreation and sport

| Field | Value |
|-------|-------|
| NOC | 65211 |
| Category | Sales and service occupations |
| Workers | 65K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Specialized cleaners

| Field | Value |
|-------|-------|
| NOC | 65311 |
| Category | Sales and service occupations |
| Workers | 44K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Pet groomers and animal care workers

| Field | Value |
|-------|-------|
| NOC | 65220 |
| Category | Sales and service occupations |
| Workers | 34K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Other service support occupations

| Field | Value |
|-------|-------|
| NOC | 65329 |
| Category | Sales and service occupations |
| Workers | 28K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Other sales related occupations

| Field | Value |
|-------|-------|
| NOC | 65109 |
| Category | Sales and service occupations |
| Workers | 19K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Dry cleaning, laundry and related occupations

| Field | Value |
|-------|-------|
| NOC | 65320 |
| Category | Sales and service occupations |
| Workers | 16K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Service station attendants

| Field | Value |
|-------|-------|
| NOC | 65101 |
| Category | Sales and service occupations |
| Workers | 10K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Meat cutters and fishmongers - retail and wholesale

| Field | Value |
|-------|-------|
| NOC | 65202 |
| Category | Sales and service occupations |
| Workers | 7K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Support occupations in accommodation, travel and facilities set-up services

| Field | Value |
|-------|-------|
| NOC | 65210 |
| Category | Sales and service occupations |
| Workers | 3K |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Other support occupations in personal services

| Field | Value |
|-------|-------|
| NOC | 65229 |
| Category | Sales and service occupations |
| Workers | 721 |
| High-exposure share | 1.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.58 |
| Complementarity | 0.51 |
| HELC / HEHC / Low | 1.0% / 0.0% / 99.0% |
| Employment change | -3.7% |
| Unemployment | 5.6% |
| Median hourly wage | $18.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Support occupations in sales and service (66, 67). |

### Nurse aides, orderlies and patient service associates

| Field | Value |
|-------|-------|
| NOC | 33102 |
| Category | Health occupations |
| Workers | 330K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.66 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +13.2% |
| Unemployment | 2.1% |
| Median hourly wage | $25.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assisting occupations in support of health services (34). |

### Material handlers

| Field | Value |
|-------|-------|
| NOC | 75101 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 240K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +10.7% |
| Unemployment | 8.1% |
| Median hourly wage | $24.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Construction trades helpers and labourers

| Field | Value |
|-------|-------|
| NOC | 75110 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 143K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +10.7% |
| Unemployment | 8.1% |
| Median hourly wage | $24.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Carpenters

| Field | Value |
|-------|-------|
| NOC | 72310 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 143K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Automotive service technicians, truck and bus mechanics and mechanical repairers

| Field | Value |
|-------|-------|
| NOC | 72410 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 143K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Electricians (except industrial and power system)

| Field | Value |
|-------|-------|
| NOC | 72200 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 119K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Delivery service drivers and door-to-door distributors

| Field | Value |
|-------|-------|
| NOC | 75201 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 111K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +10.7% |
| Unemployment | 8.1% |
| Median hourly wage | $24.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Construction millwrights and industrial mechanics

| Field | Value |
|-------|-------|
| NOC | 72400 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 97K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Welders and related machine operators

| Field | Value |
|-------|-------|
| NOC | 72106 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 95K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Landscaping and grounds maintenance labourers

| Field | Value |
|-------|-------|
| NOC | 85121 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 74K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Heavy-duty equipment mechanics

| Field | Value |
|-------|-------|
| NOC | 72401 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 71K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Contractors and supervisors, mechanic trades

| Field | Value |
|-------|-------|
| NOC | 72020 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 70K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Plumbers

| Field | Value |
|-------|-------|
| NOC | 72300 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 62K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Taxi and limousine drivers and chauffeurs

| Field | Value |
|-------|-------|
| NOC | 75200 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 62K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +10.7% |
| Unemployment | 8.1% |
| Median hourly wage | $24.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Contractors and supervisors, other construction trades, installers, repairers and servicers

| Field | Value |
|-------|-------|
| NOC | 72014 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 59K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Contractors and supervisors, heavy equipment operator crews

| Field | Value |
|-------|-------|
| NOC | 72021 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 55K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Heating, refrigeration and air conditioning mechanics

| Field | Value |
|-------|-------|
| NOC | 72402 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 48K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Labourers in food and beverage processing

| Field | Value |
|-------|-------|
| NOC | 95106 |
| Category | Occupations in manufacturing and utilities |
| Workers | 44K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.52 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -15.3% |
| Unemployment | 7.2% |
| Median hourly wage | $21.32 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assemblers and labourers in manufacturing and utilities (95, 96). |

### Dental assistants and dental laboratory assistants

| Field | Value |
|-------|-------|
| NOC | 33100 |
| Category | Health occupations |
| Workers | 42K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.66 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +13.2% |
| Unemployment | 2.1% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assisting occupations in support of health services (34). |

### Machinists and machining and tooling inspectors

| Field | Value |
|-------|-------|
| NOC | 72100 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 38K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Industrial electricians

| Field | Value |
|-------|-------|
| NOC | 72201 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 38K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Pharmacy technical assistants and pharmacy assistants

| Field | Value |
|-------|-------|
| NOC | 33103 |
| Category | Health occupations |
| Workers | 38K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.66 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +13.2% |
| Unemployment | 2.1% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assisting occupations in support of health services (34). |

### Supervisors, motor transport and other ground transit operators

| Field | Value |
|-------|-------|
| NOC | 72024 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 37K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Contractors and supervisors, carpentry trades

| Field | Value |
|-------|-------|
| NOC | 72013 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 36K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Public works maintenance equipment operators and related workers

| Field | Value |
|-------|-------|
| NOC | 74205 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 36K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +12.5% |
| Unemployment | 4.6% |
| Median hourly wage | $29.33 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Other assisting occupations in support of health services

| Field | Value |
|-------|-------|
| NOC | 33109 |
| Category | Health occupations |
| Workers | 35K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.66 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +13.2% |
| Unemployment | 2.1% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assisting occupations in support of health services (34). |

### Contractors and supervisors, electrical trades and telecommunications occupations

| Field | Value |
|-------|-------|
| NOC | 72011 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 34K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Medical laboratory assistants and related technical occupations

| Field | Value |
|-------|-------|
| NOC | 33101 |
| Category | Health occupations |
| Workers | 32K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.66 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +13.2% |
| Unemployment | 2.1% |
| Median hourly wage | $25.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assisting occupations in support of health services (34). |

### Auto body collision, refinishing and glass technicians and damage repair estimators

| Field | Value |
|-------|-------|
| NOC | 72411 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 31K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Underground production and development miners

| Field | Value |
|-------|-------|
| NOC | 83100 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 30K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Livestock labourers

| Field | Value |
|-------|-------|
| NOC | 85100 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 28K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Contractors and supervisors, landscaping, grounds maintenance and horticulture services

| Field | Value |
|-------|-------|
| NOC | 82031 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 27K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Oil and gas well drillers, servicers, testers and related workers

| Field | Value |
|-------|-------|
| NOC | 83101 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 26K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Steamfitters, pipefitters and sprinkler system installers

| Field | Value |
|-------|-------|
| NOC | 72301 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 26K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Public works and maintenance labourers

| Field | Value |
|-------|-------|
| NOC | 75212 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 26K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +10.7% |
| Unemployment | 8.1% |
| Median hourly wage | $24.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Other labourers in processing, manufacturing and utilities

| Field | Value |
|-------|-------|
| NOC | 95109 |
| Category | Occupations in manufacturing and utilities |
| Workers | 26K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.52 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -15.3% |
| Unemployment | 7.2% |
| Median hourly wage | $21.32 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assemblers and labourers in manufacturing and utilities (95, 96). |

### Specialized livestock workers and farm machinery operators

| Field | Value |
|-------|-------|
| NOC | 84120 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 26K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Telecommunications equipment installation and cable television service technicians

| Field | Value |
|-------|-------|
| NOC | 72205 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 23K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Mail and parcel sorters and related occupations

| Field | Value |
|-------|-------|
| NOC | 74100 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 22K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +12.5% |
| Unemployment | 4.6% |
| Median hourly wage | $29.33 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Couriers and messengers

| Field | Value |
|-------|-------|
| NOC | 74102 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 22K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +12.5% |
| Unemployment | 4.6% |
| Median hourly wage | $29.33 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Letter carriers

| Field | Value |
|-------|-------|
| NOC | 74101 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 22K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +12.5% |
| Unemployment | 4.6% |
| Median hourly wage | $29.33 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Aircraft mechanics and aircraft inspectors

| Field | Value |
|-------|-------|
| NOC | 72404 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 21K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Harvesting labourers

| Field | Value |
|-------|-------|
| NOC | 85101 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 20K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Air pilots, flight engineers and flying instructors

| Field | Value |
|-------|-------|
| NOC | 72600 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 19K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Contractors and supervisors, machining, metal forming, shaping and erecting trades and related occupations

| Field | Value |
|-------|-------|
| NOC | 72010 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 18K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Automotive and heavy truck and equipment parts installers and servicers

| Field | Value |
|-------|-------|
| NOC | 74203 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 18K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +12.5% |
| Unemployment | 4.6% |
| Median hourly wage | $29.33 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Labourers in metal fabrication

| Field | Value |
|-------|-------|
| NOC | 95101 |
| Category | Occupations in manufacturing and utilities |
| Workers | 18K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.52 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -15.3% |
| Unemployment | 7.2% |
| Median hourly wage | $21.32 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assemblers and labourers in manufacturing and utilities (95, 96). |

### Nursery and greenhouse labourers

| Field | Value |
|-------|-------|
| NOC | 85103 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 18K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Contractors and supervisors, oil and gas drilling and services

| Field | Value |
|-------|-------|
| NOC | 82021 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 17K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Ironworkers

| Field | Value |
|-------|-------|
| NOC | 72105 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 16K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Sheet metal workers

| Field | Value |
|-------|-------|
| NOC | 72102 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 16K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Crane operators

| Field | Value |
|-------|-------|
| NOC | 72500 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 16K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Electrical power line and cable workers

| Field | Value |
|-------|-------|
| NOC | 72203 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 16K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Labourers in wood, pulp and paper processing

| Field | Value |
|-------|-------|
| NOC | 95103 |
| Category | Occupations in manufacturing and utilities |
| Workers | 16K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.52 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -15.3% |
| Unemployment | 7.2% |
| Median hourly wage | $21.32 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assemblers and labourers in manufacturing and utilities (95, 96). |

### Contractors and supervisors, pipefitting trades

| Field | Value |
|-------|-------|
| NOC | 72012 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 15K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Air transport ramp attendants

| Field | Value |
|-------|-------|
| NOC | 74202 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 14K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +12.5% |
| Unemployment | 4.6% |
| Median hourly wage | $29.33 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Bricklayers

| Field | Value |
|-------|-------|
| NOC | 72320 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 13K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Electrical mechanics

| Field | Value |
|-------|-------|
| NOC | 72422 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 13K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Cabinetmakers

| Field | Value |
|-------|-------|
| NOC | 72311 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 12K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Motorcycle, all-terrain vehicle and other related mechanics

| Field | Value |
|-------|-------|
| NOC | 72423 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 12K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Supervisors, mail and message distribution occupations

| Field | Value |
|-------|-------|
| NOC | 72025 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 11K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Fishermen/women

| Field | Value |
|-------|-------|
| NOC | 83121 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 11K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Telecommunications line and cable installers and repairers

| Field | Value |
|-------|-------|
| NOC | 72204 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 10K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Tool and die makers

| Field | Value |
|-------|-------|
| NOC | 72101 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 10K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Supervisors, mining and quarrying

| Field | Value |
|-------|-------|
| NOC | 82020 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 9K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Other technical trades and related occupations

| Field | Value |
|-------|-------|
| NOC | 72999 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 9K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Insulators

| Field | Value |
|-------|-------|
| NOC | 72321 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 9K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Logging machinery operators

| Field | Value |
|-------|-------|
| NOC | 83110 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 9K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Other trades helpers and labourers

| Field | Value |
|-------|-------|
| NOC | 75119 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 8K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +10.7% |
| Unemployment | 8.1% |
| Median hourly wage | $24.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Railway yard and track maintenance workers

| Field | Value |
|-------|-------|
| NOC | 74200 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 8K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +12.5% |
| Unemployment | 4.6% |
| Median hourly wage | $29.33 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Labourers in chemical products processing and utilities

| Field | Value |
|-------|-------|
| NOC | 95102 |
| Category | Occupations in manufacturing and utilities |
| Workers | 8K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.52 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -15.3% |
| Unemployment | 7.2% |
| Median hourly wage | $21.32 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assemblers and labourers in manufacturing and utilities (95, 96). |

### Utility maintenance workers

| Field | Value |
|-------|-------|
| NOC | 74204 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 8K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +12.5% |
| Unemployment | 4.6% |
| Median hourly wage | $29.33 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Labourers in rubber and plastic products manufacturing

| Field | Value |
|-------|-------|
| NOC | 95104 |
| Category | Occupations in manufacturing and utilities |
| Workers | 7K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.52 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -15.3% |
| Unemployment | 7.2% |
| Median hourly wage | $21.32 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assemblers and labourers in manufacturing and utilities (95, 96). |

### Longshore workers

| Field | Value |
|-------|-------|
| NOC | 75100 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 7K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +10.7% |
| Unemployment | 8.1% |
| Median hourly wage | $24.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Gas fitters

| Field | Value |
|-------|-------|
| NOC | 72302 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 7K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Structural metal and platework fabricators and fitters

| Field | Value |
|-------|-------|
| NOC | 72104 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 6K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Deck officers, water transport

| Field | Value |
|-------|-------|
| NOC | 72602 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 6K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Elevator constructors and mechanics

| Field | Value |
|-------|-------|
| NOC | 72406 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 6K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Silviculture and forestry workers

| Field | Value |
|-------|-------|
| NOC | 84111 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 6K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Appliance servicers and repairers

| Field | Value |
|-------|-------|
| NOC | 72421 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 6K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Chain saw and skidder operators

| Field | Value |
|-------|-------|
| NOC | 84110 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 6K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Water transport deck and engine room crew

| Field | Value |
|-------|-------|
| NOC | 74201 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 5K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +12.5% |
| Unemployment | 4.6% |
| Median hourly wage | $29.33 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Fishing vessel deckhands

| Field | Value |
|-------|-------|
| NOC | 84121 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 5K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Labourers in textile processing and cutting

| Field | Value |
|-------|-------|
| NOC | 95105 |
| Category | Occupations in manufacturing and utilities |
| Workers | 5K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.52 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -15.3% |
| Unemployment | 7.2% |
| Median hourly wage | $21.32 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assemblers and labourers in manufacturing and utilities (95, 96). |

### Labourers in mineral and metal processing

| Field | Value |
|-------|-------|
| NOC | 95100 |
| Category | Occupations in manufacturing and utilities |
| Workers | 5K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.52 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -15.3% |
| Unemployment | 7.2% |
| Median hourly wage | $21.32 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assemblers and labourers in manufacturing and utilities (95, 96). |

### Railway and motor transport labourers

| Field | Value |
|-------|-------|
| NOC | 75211 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 5K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +10.7% |
| Unemployment | 8.1% |
| Median hourly wage | $24.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Power system electricians

| Field | Value |
|-------|-------|
| NOC | 72202 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 5K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Agricultural service contractors and farm supervisors

| Field | Value |
|-------|-------|
| NOC | 82030 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 5K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Oil and gas drilling, servicing and related labourers

| Field | Value |
|-------|-------|
| NOC | 85111 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 4K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Labourers in fish and seafood processing

| Field | Value |
|-------|-------|
| NOC | 95107 |
| Category | Occupations in manufacturing and utilities |
| Workers | 4K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.52 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -15.3% |
| Unemployment | 7.2% |
| Median hourly wage | $21.32 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Assemblers and labourers in manufacturing and utilities (95, 96). |

### Supervisors, printing and related occupations

| Field | Value |
|-------|-------|
| NOC | 72022 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 4K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Logging and forestry labourers

| Field | Value |
|-------|-------|
| NOC | 85120 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 4K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Oil and gas well drilling and related workers and services operators

| Field | Value |
|-------|-------|
| NOC | 84101 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 4K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Underground mine service and support workers

| Field | Value |
|-------|-------|
| NOC | 84100 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 3K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Very limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Supervisors, logging and forestry

| Field | Value |
|-------|-------|
| NOC | 82010 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 3K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Railway carmen/women

| Field | Value |
|-------|-------|
| NOC | 72403 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 3K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Boilermakers

| Field | Value |
|-------|-------|
| NOC | 72103 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 3K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Air traffic controllers and related occupations

| Field | Value |
|-------|-------|
| NOC | 72601 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 3K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Other small engine and small equipment repairers

| Field | Value |
|-------|-------|
| NOC | 72429 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 3K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Mine labourers

| Field | Value |
|-------|-------|
| NOC | 85110 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 2K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Aquaculture and marine harvest labourers

| Field | Value |
|-------|-------|
| NOC | 85102 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 2K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Boat and cable ferry operators and related occupations

| Field | Value |
|-------|-------|
| NOC | 75210 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 2K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.54 |
| Complementarity | 0.61 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +10.7% |
| Unemployment | 8.1% |
| Median hourly wage | $24.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Transport and heavy equipment operators and servicers (74, 75). |

### Machine fitters

| Field | Value |
|-------|-------|
| NOC | 72405 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 2K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Limited |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Engineer officers, water transport

| Field | Value |
|-------|-------|
| NOC | 72603 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 2K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Oil and solid fuel heating mechanics

| Field | Value |
|-------|-------|
| NOC | 72420 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 1K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Railway traffic controllers and marine traffic regulators

| Field | Value |
|-------|-------|
| NOC | 72604 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 1K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Supervisors, railway transport operations

| Field | Value |
|-------|-------|
| NOC | 72023 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 1K |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Moderate |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Water well drillers

| Field | Value |
|-------|-------|
| NOC | 72501 |
| Category | Trades, transport and equipment operators and related occupations |
| Workers | 355 |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.57 |
| Complementarity | 0.64 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | +2.8% |
| Unemployment | 4.1% |
| Median hourly wage | $37.00 |
| Outlook | Good |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Industrial, electrical and construction trades (72). |

### Fishing masters and officers

| Field | Value |
|-------|-------|
| NOC | 83120 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 0 |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -5.6% |
| Unemployment | 6.0% |
| Median hourly wage | $42.00 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

### Trappers and hunters

| Field | Value |
|-------|-------|
| NOC | 85104 |
| Category | Natural resources, agriculture and related production occupations |
| Workers | 0 |
| High-exposure share | 0.0% |
| Dominant EPIAC group | Low exposure |
| AIOE | 5.42 |
| Complementarity | 0.57 |
| HELC / HEHC / Low | 0.0% / 0.0% / 100.0% |
| Employment change | -14.6% |
| Unemployment | 12.6% |
| Median hourly wage | $23.00 |
| Outlook | Undetermined |
| Mapping note | Mapped to the closest published StatCan EPIAC occupation group from the 2021 Census (NOC 2016): Natural resources, agriculture and related production occupations (8). |

