# Phase 1 findings

Last updated: 2026-09-30. Full data in `data/processed/`.

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

## Further reading

- Tansen Sen, "Inventing the 'Maritime Silk Road'", *Modern Asian Studies* 57 (2023): 1059-1104. doi:10.1017/S0026749X22000348
