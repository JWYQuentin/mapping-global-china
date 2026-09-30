# Data lineage log

One entry per collection step: what was collected, from where, when, and how. Add new entries at the top.

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
