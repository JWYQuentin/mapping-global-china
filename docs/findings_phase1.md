# Phase 1 findings

Last updated: 2026-10-05. Full data in `data/processed/`.

## 1a. UNESCO

| Finding | Detail |
| --- | --- |
| China's lists | 61 World Heritage properties (42 cultural, 15 natural, 4 mixed) and 60 Tentative List entries. |
| Transnational | Only one: Silk Roads: the Routes Network of Chang'an-Tianshan Corridor (2014, with Kazakhstan and Kyrgyzstan, 33 components). |
| Maritime Silk Road | No joint nomination on UNESCO's lists. The term appears only in China's own Tentative List entries: 2008 (sea routes at Ningbo and Quanzhou) and 2016 (31 sea-route sites, China only). Quanzhou (2021) was inscribed as a "maritime emporium", not under the Silk Road name. |
| Outward links in UNESCO text | 9 Chinese properties mention cross-border links or exchange, e.g. Kaiping Diaolou (émigrés) and Kulangsu (Sino-foreign exchange). |
| Sites abroad | 29 properties in other countries whose UNESCO text links them to China (33 including 4 geographic-only mentions): Chinese communities (Melaka/George Town, Hoi An, Vigan), labour (Sawahlunto), porcelain trade (Kilwa, Qalhat), Silk Roads cities. |
| Other UNESCO records | Joint intangible heritage with Malaysia (Ong Chun/Wangchuan/Wangkang, 2020) and Mongolia (Urtiin Duu); parallel national inscriptions of Khoomei (China 2009, Mongolia 2010); Memory of the World: Qiaopi overseas Chinese remittance letters (2013). |

**Data access**

- UNESCO publishes the World Heritage List as XML, XLSX and KML, in English and Chinese. The Chinese feed has gaps (e.g. no Chinese name for the Silk Roads property).
- The feeds carry only short descriptions. Chinese links for Melaka and Hoi An appear only in the full Statement of Outstanding Universal Value on site pages, which are not syndicated.
- UNESCO's terms forbid scraping non-syndicated pages and require written permission to republish its data.
- There is no bulk feed for Tentative Lists.

## 1b. Chinese sources

| Finding | Detail |
| --- | --- |
| Best dated series | NCHA five-year plans (2017, 2021, 2026). In 2017 the Maritime Silk Road nomination is domestic work; by 2026 it is "transnational joint nomination" preparatory work, alongside the Tea Road and China-Egypt hydrological heritage. |
| Most structured source | The national intangible heritage database (ihchina.cn) has an open JSON endpoint with item IDs, categories, listing year and place. |
| Framing gap | China's national list titles the Wangchuan ceremony 闽台送王船 (Fujian-Taiwan); UNESCO's 2020 joint inscription frames it as China + Malaysia (Melaka). Nanyin and Mazu entries frame overseas practice as a bond with "overseas compatriots" and Taiwan. |
| Embassies | All *.china-embassy.gov.cn sites share one Foreign Ministry template with dated URLs; archives reach back to 2005 (Kenya). Some pre-2013 links now redirect to the homepage. |
| Institutional engagement | Aid restoration (Mongolia 1959-61, Angkor since 1998, Nepal, Myanmar) and joint archaeology (Uzbekistan, Honduras, Egypt, Romania, Greece, Tunisia, Kyrgyzstan, Kenya). |
| Possible future source | NCHA's 2026 plan commits to an "Asian cultural heritage database" under the China-led Alliance for Cultural Heritage in Asia. |

**Access notes for Phase 2**

- NCHA's site search does not respond to plain URL queries; it needs browser automation.
- ihchina.cn can be queried directly.
- Embassy sites can be crawled by URL pattern.
- Chinese sites loaded normally from a US connection.
- No open databases were found at overseas-Chinese institutions, so the diaspora layer will rely more on host-country sources (1c).

## 1c. Host-country and diaspora sources

| Finding | Detail |
| --- | --- |
| Official registers under-record Chinese sites | Malaysia's National Heritage buildings list (130 entries) has one clearly Chinese-community site, Leong San Tong Khoo Kongsi (2018). The US National Register codes ethnic association inconsistently, and the National Park Service says such places are undercounted. |
| Host countries frame sites locally | Kenya's National Museums call Gedi "a testament to the Swahili culture" with no China reference. Kyrgyzstan lists Silk Roads sites under local and historical names. Cambodia's APSARA treats China as one technical partner among several. |
| Best structured host source | The Victorian Heritage Database (Australia) has an open JSON API: 454 places match "chinese", each with coordinates and a significance statement. The US National Register offers spreadsheet downloads. |
| Best seed list for temples | OpenStreetMap has 938 Taoist, Chinese-folk or Confucian places of worship in Malaysia (392 with Chinese names). Wikidata has 16 Chinese temples there, so it works as an ID crosswalk, not a site list. |
| Institutional-engagement data | AidData's Global Chinese Development Finance dataset v3.0 (20,985 projects, 2000-2021) is downloadable and includes heritage aid, e.g. the RMB 90 million Angkor Royal Palace grant (2018). |
| Central Asia inventory | UCL's CAAL database holds over 45,000 archaeological sites across five republics and Xinjiang; open to search, all rights reserved. |
| Contested-site test case | Bukit Cina cemetery, Melaka: a 1980s development dispute, then a 2005 report that it would be gazetted. |

**Gaps**

- No online register found for Chinese associations, temples or schools in Cambodia.
- Kazakhstan's state list could not be read (the legal portal refused automated access).
- George Town's building inventory is not published online.
- No downloadable list of US railway-worker sites.
- 1c quotes and list counts were retrieved through a web-reading tool and need checking against their pages.

## 1d. Non-site data

| Finding | Detail |
| --- | --- |
| Best agreements source | China's Foreign Ministry treaty database is searchable and structured. 31 records match heritage keywords: 6 on illicit trafficking, 8 heritage-cooperation memoranda, 11 exhibition agreements from 1973-76. |
| It is incomplete | It holds 5 country agreements on illicit trafficking plus the US memorandum, mostly up to 2009. Chinese media citing officials give 26 countries (2023) and 27 (2026); no public list was found. |
| Wording shifts over time | Titles move from "exhibition of unearthed relics" (1970s) to "preventing theft and illicit export" and "cooperating to protect cultural heritage" (2005-09). |
| Maritime Silk Road as a Belt and Road deliverable | The October 2023 Belt and Road Forum list commits NCHA to the Maritime Silk Road transnational nomination, a China-Saudi excavation at Serrin port, and an archaeological park at Nateshwar, Bangladesh. |
| China funds other countries' nominations | Through UNESCO, China has supported World Heritage nominations and training in Africa since 2014. A USD 1 million fund (2025-2028) is named for Quanzhou. |
| China-led organisation | The Alliance for Cultural Heritage in Asia became an intergovernmental organisation in June 2024. Its fund has announced two rounds of 15 projects. |
| Structured UNESCO sources | The Core Data Portal gives project budgets by donor with spreadsheet downloads; the national heritage laws database has the same table for every country. |

**Gaps**

- No list of the 27 agreement countries.
- No source found for Chinese companies in heritage work abroad.
- The alliance's project lists appear only in news reports.
- Summit outcome lists (China-Central Asia, FOCAC) not yet read.

## Further reading

- Tansen Sen, "Inventing the 'Maritime Silk Road'", *Modern Asian Studies* 57 (2023): 1059-1104. doi:10.1017/S0026749X22000348
