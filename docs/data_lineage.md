# Data lineage log

One entry per collection step: what was collected, from where, when, and how. Add new entries at the top.

## 2026-10-05: Phase 1d, non-site data

| Source | URL | Method | Output |
| --- | --- | --- | --- |
| China MFA treaty database | https://treaty.mfa.gov.cn/web/index.jsp | Browser (desktop app, US connection); keyword search for 文物, 文化遗产, 考古, 世界遗产, 非物质文化遗产; all result pages collected | `1d Agreements (MFA DB)` |
| Belt and Road Forum project list (Oct 2023) | https://www.mfa.gov.cn/zyxw/202310/t20231018_11163412.shtml | Browser; lines filtered by keyword | `1d Programmes & Outcomes` |
| Xinhua articles on the Asian fund (2023, 2025) | http://www.news.cn/ (see row URLs) | Browser; text copied from page | `1d Programmes & Outcomes` |
| UNESCO pages (laws, sessions, partners, Core Data Portal, category 2 centres) | See row URLs | Web fetch (summarised) | `1d Non-site Data Sources` |
| US State Department, Chinese media, China Daily | See row URLs | Web fetch (summarised) | `1d Non-site Data Sources`, `1d Programmes & Outcomes` |

## 2026-10-05: Phase 1c, host-country and diaspora sources

| Source | URL | Method | Output |
| --- | --- | --- | --- |
| Wikidata | https://query.wikidata.org/ | Browser; SPARQL counts of Chinatowns, Chinese temples, World Heritage IDs | `1c Host & Diaspora Sources` |
| OpenStreetMap (Overpass API) | https://overpass.kumi.systems/api/interpreter | Browser; count of Taoist, Chinese-folk and Confucian places of worship in Malaysia. Queries for Cambodia and Kenya timed out | `1c Host & Diaspora Sources` |
| Victorian Heritage Database API | https://api.heritagecouncil.vic.gov.au/v1/places?kw=chinese | Browser; JSON read directly | `1c Host & Diaspora Sources` |
| Host-country registers and bodies (Malaysia, Kyrgyzstan, Cambodia, Kenya, US, Australia), CAAL, AidData, community lists | See row URLs | Web fetch (summarised); quotes need checking against pages | `1c Host & Diaspora Sources`, `1c Framing Examples` |

## 2026-09-30: Phase 1b, Chinese sources

| Source | URL | Method | Output |
| --- | --- | --- | --- |
| NCHA homepage, site map, articles | http://www.ncha.gov.cn/ | Browser (desktop app, US connection); page text read in browser | `1b Chinese Sources`, `1b Framing Examples`, `1b Chinese Projects Abroad` |
| NCHA 13th five-year plan (2017) | http://www.ncha.gov.cn/art/2017/2/27/art_2237_43663.html | Browser; sentences filtered by keyword | `1b Framing Examples` |
| 14th five-year heritage plan (2021) | https://www.ndrc.gov.cn/fggz/fzzlgh/gjjzxgh/202112/t20211201_1306596.html | Web fetch | `1b Framing Examples` |
| NCHA 15th five-year plan (2026) | http://www.ncha.gov.cn/art/2026/7/29/art_2318_48456.html | Browser; sentences filtered by keyword | `1b Framing Examples` |
| MCT homepage | https://www.mct.gov.cn/ | Browser | `1b Chinese Sources` |
| ihchina.cn national ICH list | https://www.ihchina.cn/getProject.html?keywords=... | Browser; JSON endpoint queried for 送王船, 南音, 妈祖 | `1b Framing Examples` |
| Chinese embassies (Cambodia, Malaysia, Kenya, Uzbekistan) | https://kh.china-embassy.gov.cn/ and others | Browser and web search restricted to each domain | `1b Chinese Sources`, `1b Framing Examples` |
| CASS / cssn.cn, chinanews.com.cn | See row URLs | Web fetch | `1b Chinese Projects Abroad` |

## 2026-09-30: Phase 1a, UNESCO

| Source | URL | Method | Output |
| --- | --- | --- | --- |
| World Heritage List XML feed (EN) | https://whc.unesco.org/en/list/xml/ | Browser fetch of syndicated feed; China records extracted | `data/raw/unesco_whc_feed_china_extract_2026-09-30.json`; `China WH List` |
| World Heritage List XML feed (EN), all 1,273 records | https://whc.unesco.org/en/list/xml/ | Keyword search of `short_description` and `justification` for China/Chinese/Silk Road | `Sites Abroad Linked to China` |
| World Heritage List XML feed (ZH) | https://whc.unesco.org/zh/list/xml/ | Browser fetch; Chinese names and descriptions | Chinese name columns |
| China States Party page | https://whc.unesco.org/en/statesparties/cn | Web fetch | `China Tentative List`; counts cross-checked |
| Site pages 1223 (Melaka), 948 (Hoi An), 1442 | https://whc.unesco.org/en/list/1223/ etc. | Read individually (not scraped) | `Sites Abroad Linked to China` |
| Documents page for 1442 | https://whc.unesco.org/en/list/1442/documents/ | Web fetch | `Docs - Silk Roads 1442` |
| Tentative List entry 6093 | https://whc.unesco.org/en/tentativelists/6093/ | Web fetch | `China Tentative List` notes |
| UNESCO ICH pages | https://ich.unesco.org/en/state/china-CN | Browser and web fetch | `Other UNESCO Records` |
| Syndication terms | https://whc.unesco.org/en/syndication | Web fetch | README terms of use |

Checks: China's counts (61 properties: 42 cultural, 15 natural, 4 mixed; 60 Tentative List entries) match between the XML feed and the States Party page.
