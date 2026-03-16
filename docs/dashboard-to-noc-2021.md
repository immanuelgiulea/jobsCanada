# Dashboard to NOC 2021 audit

## Summary

- Official NOC 2021 hierarchy reproduced locally: 10 broad categories, 45 major groups, 89 sub-major groups, 162 minor groups, and 516 unit groups.
- Current dashboard layer: 10 families and 43 occupation groups.
- Coverage check: 516/516 unit groups are covered, with 0 gaps and 0 overlaps.
- The dashboard's 10 families follow the NOC 2021 labour-force variant sections (L0-L9), not the official NOC 2021 broad categories.
- The Management family is the main mismatch with the official hierarchy: it combines broad category 0 with the middle-management major groups 10 through 90, so it spans all 10 official broad categories.
- The Resources family is real data, not an orphan tile set. It contains 25 official unit groups through dashboard groups 82-83 and 84-85; any missing header is a treemap layout issue rather than a hierarchy issue.

## Dashboard group shapes

- Custom cross-broad merge of major groups: 2
- Custom merge of major groups within one broad category: 5
- Exact official broad category: 1
- Exact official major group: 21
- Exact official sub-major group: 14

## Family concordance

| Dashboard family | Variant section | Dashboard groups | Official broad categories | Major | Sub-major | Minor | Unit |
|---|---:|---:|---|---:|---:|---:|---:|
| Management occupations | L0 | 4 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 | 10 | 10 | 20 | 48 |
| Business, finance and administration occupations, except management | L1 | 5 | 1 | 4 | 11 | 14 | 51 |
| Natural and applied sciences and related occupations, except management | L2 | 4 | 2 | 2 | 6 | 19 | 63 |
| Health occupations, except management | L3 | 5 | 3 | 3 | 6 | 10 | 42 |
| Occupations in education, law and social, community and government services, except management | L4 | 8 | 4 | 5 | 11 | 15 | 42 |
| Occupations in art, culture, recreation and sport, except management | L5 | 4 | 5 | 5 | 6 | 12 | 34 |
| Sales and service occupations, except management | L6 | 4 | 6 | 4 | 12 | 21 | 56 |
| Trades, transport and equipment operators and related occupations, except management | L7 | 4 | 7 | 4 | 16 | 25 | 89 |
| Natural resources, agriculture and related production occupations, except management | L8 | 2 | 8 | 4 | 4 | 12 | 25 |
| Occupations in manufacturing and utilities, except management | L9 | 3 | 9 | 4 | 7 | 14 | 66 |

## Group concordance

| Code | Dashboard group | Family | Mapping kind | Broad | Major | Sub-major | Minor | Unit |
|---|---|---|---|---|---:|---:|---:|---:|
| 14 | Administrative and financial support and supply chain logistics occupations | L1 | Exact official major group | 1 | 1 | 4 | 5 | 18 |
| 13 | Administrative occupations and transportation logistics occupations | L1 | Exact official major group | 1 | 1 | 2 | 3 | 8 |
| 12 | Administrative and financial supervisors and specialized administrative occupations | L1 | Exact official major group | 1 | 1 | 3 | 4 | 17 |
| 111 | Professional occupations in finance | L1 | Exact official sub-major group | 1 | 1 | 1 | 1 | 5 |
| 112 | Professional occupations in business | L1 | Exact official sub-major group | 1 | 1 | 1 | 1 | 3 |
| 33 | Assisting occupations in support of health services | L3 | Exact official major group | 3 | 1 | 1 | 1 | 5 |
| 313 | Nursing and allied health professionals | L3 | Exact official sub-major group | 3 | 1 | 1 | 1 | 4 |
| 32 | Technical occupations in health | L3 | Exact official major group | 3 | 1 | 2 | 4 | 18 |
| 311 | Health treating and consultation services professionals | L3 | Exact official sub-major group | 3 | 1 | 1 | 3 | 9 |
| 312 | Therapy and assessment professionals | L3 | Exact official sub-major group | 3 | 1 | 1 | 1 | 6 |
| 10, 20, 30, 40, 50 | Specialized middle management occupations | L0 | Custom cross-broad merge of major groups | 1, 2, 3, 4, 5 | 5 | 5 | 10 | 26 |
| 70, 80, 90 | Middle management occupations in trades, transportation, production and utilities | L0 | Custom cross-broad merge of major groups | 7, 8, 9 | 3 | 3 | 5 | 11 |
| 60 | Middle management occupations in retail and wholesale trade and customer services | L0 | Exact official major group | 6 | 1 | 1 | 4 | 5 |
| 0 | Legislative and senior management occupations | L0 | Exact official broad category | 0 | 1 | 1 | 1 | 6 |
| 212 | Professional occupations in applied sciences (except engineering) | L2 | Exact official sub-major group | 2 | 1 | 1 | 4 | 15 |
| 22 | Technical occupations related to natural and applied sciences | L2 | Exact official major group | 2 | 1 | 3 | 7 | 27 |
| 213 | Professional occupations in engineering | L2 | Exact official sub-major group | 2 | 1 | 1 | 5 | 12 |
| 211 | Professional occupations in natural sciences | L2 | Exact official sub-major group | 2 | 1 | 1 | 3 | 9 |
| 84-85 | Workers and labourers in natural resources, agriculture and related production | L8 | Custom merge of major groups within one broad category | 8 | 2 | 2 | 6 | 15 |
| 82-83 | Supervisors and occupations in natural resources, agriculture and related production | L8 | Custom merge of major groups within one broad category | 8 | 2 | 2 | 6 | 10 |
| 54-55 | Support occupations in art, culture and sport | L5 | Custom merge of major groups within one broad category | 5 | 2 | 2 | 2 | 2 |
| 51 | Professional occupations in art and culture | L5 | Exact official major group | 5 | 1 | 1 | 3 | 11 |
| 52 | Technical occupations in art, culture and sport | L5 | Exact official major group | 5 | 1 | 1 | 3 | 9 |
| 53 | Occupations in art, culture and sport | L5 | Exact official major group | 5 | 1 | 2 | 4 | 12 |
| 412 | Professional occupations in education services | L4 | Exact official sub-major group | 4 | 1 | 1 | 3 | 5 |
| 422 | Paraprofessional occupations in legal, social, community and education services | L4 | Exact official sub-major group | 4 | 1 | 1 | 1 | 5 |
| 414 | Professional occupations in government services | L4 | Exact official sub-major group | 4 | 1 | 1 | 1 | 9 |
| 413 | Professional occupations in social and community services | L4 | Exact official sub-major group | 4 | 1 | 1 | 3 | 7 |
| 43 | Assisting occupations in education and in legal and public protection | L4 | Exact official major group | 4 | 1 | 2 | 2 | 7 |
| 411 | Professional occupations in law | L4 | Exact official sub-major group | 4 | 1 | 1 | 1 | 2 |
| 421 | Occupations in front-line public protection services | L4 | Exact official sub-major group | 4 | 1 | 1 | 1 | 3 |
| 44-45 | Care providers and public protection support occupations and student monitors, crossing guards and related occupations | L4 | Custom merge of major groups within one broad category | 4 | 2 | 3 | 3 | 4 |
| 94 | Machine operators, assemblers and inspectors in processing, manufacturing and printing | L9 | Exact official major group | 9 | 1 | 2 | 8 | 40 |
| 92-93 | Supervisors, central control and process operators in processing, manufacturing and utilities and aircraft assemblers and inspectors | L9 | Custom merge of major groups within one broad category | 9 | 2 | 4 | 5 | 17 |
| 95 | Labourers in processing, manufacturing and utilities | L9 | Exact official major group | 9 | 1 | 1 | 1 | 9 |
| 65 | Sales and service support occupations | L6 | Exact official major group | 6 | 1 | 3 | 6 | 16 |
| 64 | Sales and service representatives and other customer and personal services occupations | L6 | Exact official major group | 6 | 1 | 4 | 7 | 18 |
| 63 | Occupations in sales and services | L6 | Exact official major group | 6 | 1 | 2 | 4 | 10 |
| 62 | Retail sales and service supervisors and specialized occupations in sales and services | L6 | Exact official major group | 6 | 1 | 3 | 4 | 12 |
| 72 | Technical trades and transportation officers and controllers | L7 | Exact official major group | 7 | 1 | 8 | 13 | 53 |
| 73 | General trades | L7 | Exact official major group | 7 | 1 | 4 | 6 | 18 |
| 75 | Helpers and labourers and other transport drivers, operators and labourers | L7 | Exact official major group | 7 | 1 | 2 | 4 | 9 |
| 74 | Mail and message distribution, other transport equipment operators and related maintenance workers | L7 | Exact official major group | 7 | 1 | 2 | 2 | 9 |

## Official broad categories

- `0`: Legislative and senior management occupations
- `1`: Business, finance and administration occupations
- `2`: Natural and applied sciences and related occupations
- `3`: Health occupations
- `4`: Occupations in education, law and social, community and government services
- `5`: Occupations in art, culture, recreation and sport
- `6`: Sales and service occupations
- `7`: Trades, transport and equipment operators and related occupations
- `8`: Natural resources, agriculture and related production occupations
- `9`: Occupations in manufacturing and utilities

## Sources

- [NOC 2021 V1 classification structure](https://www.statcan.gc.ca/en/subjects/standard/noc/2021/indexV1)
- [NOC 2021 V1 variant: Aggregates for Analysis of labour force](https://www.statcan.gc.ca/en/subjects/standard/noc/2021/indexV1/noc-2021-v1.0-variant-aggregates-analysis-labour-force)
- [ESDC 2025-2027 Employment Outlooks - NOC 2021](https://open.canada.ca/data/en/dataset/b0e112e9-cf53-4e79-8838-23cd98debe5b/resource/cb52e1d0-ab62-4357-91cc-d8f5a2114e02)
