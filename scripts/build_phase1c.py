"""Add Phase 1c (host-country and diaspora sources) sheets to the Phase 1 workbook.
Run from the repo root, in order after the earlier build scripts (each script adds sheets once).
All values were collected on 2026-10-05 from the URLs recorded in each row."""
import sys
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

SRC = sys.argv[1] if len(sys.argv) > 1 else "data/processed/Mapping_Global_China_Phase1_Sources.xlsx"
OUT = sys.argv[2] if len(sys.argv) > 2 else "data/processed/Mapping_Global_China_Phase1_Sources.xlsx"
F = "Arial"
HDR = PatternFill("solid", fgColor="1F3A5F"); HFONT = Font(name=F, bold=True, color="FFFFFF")
BODY = Font(name=F, size=10); LINK = Font(name=F, size=10, color="0563C1", underline="single")
FILL = PatternFill("solid", fgColor="FFF2CC")
wb = load_workbook(SRC)

def sheet(title, headers, rows, widths, link_cols=(), fill_cols=()):
    ws = wb.create_sheet(title); ws.append(headers)
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c); cell.font, cell.fill = HFONT, HDR
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    for r in rows: ws.append(list(r))
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.font = BODY; cell.alignment = Alignment(wrap_text=True, vertical="top")
            if cell.column in link_cols and isinstance(cell.value, str) and cell.value.startswith("http"):
                cell.hyperlink = cell.value; cell.font = LINK
            if cell.column in fill_cols: cell.fill = FILL
    for i, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "C2"; ws.auto_filter.ref = ws.dimensions; ws.row_dimensions[1].height = 32

INV = [
 ("Malaysia", "National Heritage Register (Jabatan Warisan Negara)", "Host government (federal heritage department)", "https://www.heritage.gov.my/images/05_daftarwarisan/BANGUNAN_Warisan%20Kebangsaan.pdf",
  "Historical presence and designation layers. Buildings lists: 130 'Warisan Kebangsaan' (National Heritage, declared 2007-2018) and 125 'Warisan' (Heritage, gazetted 1977-2020). Separate lists for archaeological sites and other categories.",
  "Malay", "Structured but as PDF tables per category: number, site, gazette number or declaration date and place. No coordinates, no descriptions.",
  "PDF download and table extraction. No searchable database found.", "Yes: gazette and declaration dates per entry.",
  "Chinese-community sites look rare: one found in the 130 National Heritage buildings (Leong San Tong Khoo Kongsi, Penang, 2018) and none identified in the 125 Heritage buildings. Read by automated summary; recheck by hand.",
  "High (official). Thin for Chinese sites.", ""),
 ("Malaysia", "George Town World Heritage Incorporated (GTWHI)", "Host state agency (World Heritage site manager)", "https://gtwhi.com.my/our-work/buildings/",
  "Historical presence in the George Town World Heritage site: more than 5,000 buildings; 82 Category I buildings, gateways, cemeteries and sites; Category II mostly shophouses.",
  "English, Malay", "Building inventory exists (Special Area Plan) but no list, database or map is published on the page.",
  "Manual. Ask GTWHI for the inventory or use the Special Area Plan document.", "Special Area Plan editions.",
  "Lists 'Chinese temples' and 'water villages (clan jetties)' among building types, alongside mosques, churches and Hindu temples: multicultural framing.",
  "High.", ""),
 ("Malaysia", "Bukit Cina cemetery, Melaka (community-managed)", "Diaspora community / news", "https://www.thestar.com.my/news/nation/2005/07/14/bukit-cina-to-be-gazetted",
  "Chinese cemetery with over 12,000 graves, some claimed to date to the Ming dynasty (per Wikipedia). A 1980s development proposal made it a national controversy; in 2005 it was reported it would be gazetted as an ancient monument.",
  "English, Chinese, Malay", "No register entry found online; evidence is news and community sources.",
  "Manual. Current legal status still to confirm.", "Yes: 1980s dispute and 2005 gazettal report give dated framings.",
  "Good test case: community, state and (later) Chinese-embassy narratives attach to the same hill.", "Medium (news and Wikipedia).", ""),
 ("Central Asia", "Kazakhstan State List of Monuments of History and Culture of Republican Significance", "Host government (legal act)", "https://zakon.uchet.kz/rus/docs/P080000279_",
  "Designation layer for Kazakhstan, including Silk Roads components in Zhetysu.", "Russian, Kazakh",
  "List published as a legal act; also regional lists of local significance.",
  "Not yet read: the legal portal refused automated access. Test in Phase 2 (adilet.zan.kz).", "Yes: successive approved lists (2008, 2020).",
  "Not yet sampled.", "High (official).", ""),
 ("Central Asia", "Kyrgyzstan State List of monuments of republican significance", "Host government (legal act / policy concept)", "https://faolex.fao.org/docs/pdf/kyr161432.pdf",
  "Designation layer: 583 objects on the State List out of about 2,000 immovable monuments (2015 heritage concept).", "Russian, Kyrgyz",
  "Legal text grouped by type (history, archaeology, architecture, art, combined).",
  "PDF or legal-portal text extraction.", "Yes: list and amendments are dated.",
  "Silk Roads components carry dual names, modern and historical: «Ак-Бешим (Суяб)», «Бурана (Баласагын)», «Красноречинское (Невакет)». No China reference in the naming.",
  "High (official).", ""),
 ("Central Asia", "Central Asian Archaeological Landscapes (CAAL), UCL", "International academic project", "https://database.uclcaal.org/",
  "Over 45,000 archaeological sites across Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan and Xinjiang (China); about 250,000 digitised archive files.",
  "English (site)", "Highly structured (Arches heritage-inventory platform).",
  "Open-access core without registration; sensitive data on request. Rights: all rights reserved, so reuse needs permission.", "Archive files are dated.",
  "Treats Xinjiang as part of a Central Asian landscape; partner logos include Northwest University (China).", "High.", ""),
 ("Cambodia", "APSARA National Authority", "Host government (Angkor site manager)", "https://apsaraauthority.gov.kh/our-work/archeological-research-conservation/5",
  "Institutional engagement at Angkor: dated news by temple and by international team (India, US, Japan, South Korea, France, China).",
  "Khmer, English", "Semi-structured dated news posts. No project database.",
  "Scraping of dated posts.", "Yes: posts dated from at least 2024.",
  "China appears as one partner among many: 'China-Cambodia Government Team for Safeguarding Angkor'. Technical, not civilisational, wording.",
  "High for project facts.", ""),
 ("Cambodia", "Chinese-Cambodian associations, temples and schools", "Diaspora community", "",
  "Historical presence layer in Cambodia.", "Chinese, Khmer", "No online register or list found in this pass.",
  "Not found. Needs Chinese-language search and literature in a later pass.", "Unknown.", "Not sampled.", "Unknown.", ""),
 ("Kenya", "National Museums of Kenya: gazetted sites and monuments", "Host government (museums and heritage body)", "https://en.wikipedia.org/wiki/List_of_sites_and_monuments_in_Kenya",
  "Designation layer: 208 gazetted sites and monuments in the Wikipedia compilation, with gazette dates and coordinates. Coast entries include Gedi (1970), Mambrui (1935), Manda (1956), Siyu (1958), Pate (1982), Shanga (1983), Fort Jesus (1970).",
  "English", "Official source is Kenya Gazette notices (kenyalaw.org); Wikipedia offers a structured table.",
  "Wikipedia table or Wikidata for structure; gazette notices for verification.", "Yes: gazette dates from 1935.",
  "NMK's 2024 announcement of Gedi's World Heritage listing calls it 'a testament to the Swahili culture' and does not mention China.",
  "Medium (Wikipedia) to high (gazette).", ""),
 ("United States", "National Register of Historic Places (National Park Service)", "Host government (federal register)", "https://home.nps.gov/subjects/nationalregister/data-downloads.htm",
  "Designation layer for the US: all listed properties, National Historic Landmarks, removed and eligible properties.",
  "English", "Highly structured: Excel spreadsheets (updated 2026-05-22) and a GIS geodatabase.",
  "Bulk download. No API mentioned.", "Yes: listing dates; nomination forms on NPGallery.",
  "Ethnic association is coded under 'Area of Significance' (e.g. 'Ethnic Heritage: Asian') but applied inconsistently, so Chinese-related places are undercounted. About 10% of places are identified with a cultural or ethnic community.",
  "High; incomplete for ethnic coding.", ""),
 ("United States", "NPS Asian American and Pacific Islander theme study, Appendix II study list (2017)", "Host government (thematic study)", "https://www.nps.gov/subjects/tellingallamericansstories/upload/19-Appendix-II-Study-List.pdf",
  "About 90 properties that may be eligible for National Historic Landmark status, grouped by community; roughly 35-40 Chinese American (approximate). Examples: Bok Kai Temple, Weaverville Joss House, China Alley, Rock Springs Massacre Site.",
  "English", "PDF table: property, location, National Register listing year, criteria.", "PDF table extraction.", "Single edition (2017).",
  "Frames sites as part of American national history.", "High.", ""),
 ("United States", "Chinese Railroad Workers in North America Project (Stanford)", "Academic project", "https://web.stanford.edu/group/chineserailroad/cgi-bin/website/researchmaterials/archaeology",
  "Railway-worker sites and archaeology of overseas Chinese communities.", "English, Chinese",
  "No downloadable site list or database on the page; publications and an archaeology network.", "Manual; contact the project.", "Publications dated from 2013.",
  "'Transpacific' framing.", "High (scholarly).", ""),
 ("Australia", "Victorian Heritage Database (Heritage Council of Victoria)", "Host government (state register)", "https://api.heritagecouncil.vic.gov.au/v1/places?kw=chinese&rpp=5",
  "Designation and narrative layers for Victoria: 454 places match the keyword 'chinese' (includes false positives), each with coordinates, summary and statement of significance.",
  "English", "Highly structured.", "Open JSON API (tested 2026-10-05): id, name, latlon, summary, authority, register number.",
  "Heritage studies carry author and year.", "Bendigo Joss House: 'sole reminder' of a once extensive Chinese gold-rush community. Local-history framing.", "High.", ""),
 ("Australia", "Australian Heritage Database (federal)", "Host government (federal)", "https://data.gov.au/data/dataset/australian-heritage-database",
  "More than 20,000 natural, historic and Indigenous places across national lists.", "English",
  "Structured; files and APIs listed on data.gov.au.", "Download or API; licence 'not specified'.", "Updated 2025-06-24.", "Not sampled.", "High.", ""),
 ("Australia", "Chinese Australian Historical Society select list; CHIA image database", "Diaspora community / museum and university", "https://chineseaustralianhistory.org/heritage/",
  "Community-compiled select list of Chinese Australian heritage sites by state (temples, market gardens, cemeteries, Broome Chinatown), linking to official registers. CHIA: archived catalogue of historical images.",
  "English", "Semi-structured web list; CHIA is archived.", "Manual.", "CHIA archived; list is current.",
  "Community advocacy for listing: shows who is asking for recognition.", "Medium-high.", ""),
 ("Cross-country", "Wikidata", "Open knowledge base", "https://query.wikidata.org/",
  "Crosswalk and thin site coverage: 93 Chinatowns (82 with coordinates, 74 with a Chinese label); 2,028 Chinese temples of which about 207 are tagged outside mainland China, Taiwan, Hong Kong and Macao (including historical states); 16 in Malaysia. 6,184 items carry a UNESCO World Heritage ID.",
  "Multilingual", "Highly structured.", "SPARQL API (tested 2026-10-05).", "Edit history only.",
  "No framing text. Use as an ID and name crosswalk, not as the site list.", "Medium; very incomplete for diaspora sites.", ""),
 ("Cross-country", "OpenStreetMap", "Open map database", "https://overpass-api.de/",
  "Much denser than Wikidata: 938 Taoist, Chinese-folk or Confucian places of worship in Malaysia, 392 with a Chinese name.",
  "Multilingual", "Highly structured (tags, coordinates).", "Overpass API. Public servers timed out on multi-country queries; query one country at a time or use a regional extract.", "Edit history.",
  "No framing text. Best seed list for temples; needs checking against registers.", "Medium (crowd-sourced).", ""),
 ("Cross-country", "AidData Global Chinese Development Finance dataset v3.0", "Academic research lab", "https://www.aiddata.org/data/aiddatas-global-chinese-development-finance-dataset-version-3-0",
  "Institutional engagement layer: 20,985 Chinese-financed projects in 165 countries, 2000-2021. Includes heritage aid, e.g. RMB 90 million grant for the Angkor Royal Palace restoration (2018, project 62500).",
  "English", "Highly structured; ZIP download plus GeoJSON locations.", "Bulk download; keyword filter for heritage, restoration, archaeology.", "Project commitment years.",
  "Neutral descriptive records with funder and implementer.", "High.", ""),
 ("Cross-country (model)", "Singapore Historical GIS: Chinese temples (NUS)", "Academic project", "http://shgis.nus.edu.sg/index.php/chinese-temples",
  "More than 1,000 Chinese temples in Singapore with founding years, addresses, deities, inscriptions and links to mother temples in China. Outside the candidate regions; a model for the data to collect.",
  "English, Chinese", "Structured GIS; partly crowd-sourced.", "Web map; availability not tested.", "Tracks temple relocations over time.",
  "Records ties to 'mother temples' in China: a ready-made diaspora-to-China link field.", "High (scholarly).", ""),
]
sheet("1c Host & Diaspora Sources",
      ["Region", "Source", "Owner type", "URL (example page)", "Coverage (layers, regions)", "Language", "How systematic",
       "Access method (preliminary, for Phase 2)", "Historical versions", "Framing notes", "Reliability", "Your notes"],
      INV, [16, 34, 22, 40, 55, 12, 40, 44, 28, 52, 20, 24], link_cols=(4,), fill_cols=(12,))

FR = [
 ("2025-10-24", "APSARA National Authority", "Host government", "Cambodia", "Angkor Royal Palace restoration",
  "the China-Cambodia Government Team for Safeguarding Angkor with Mr. Li Xiangdong, Deputy Director-General of the China Academy of Cultural Heritage",
  "Technical partnership; China as one team among several", "https://apsaraauthority.gov.kh/2025/10/24/meeting-and-inspects-work-on-the-royal-palace/"),
 ("2024-07-27", "National Museums of Kenya", "Host government", "Kenya", "Gedi World Heritage listing",
  "a testament to the Swahili culture", "Swahili / national heritage; no China reference", "https://museums.or.ke/?p=2296"),
 ("2015-01-26", "Government of Kyrgyzstan (heritage concept 2015-2020)", "Host government", "Kyrgyzstan", "Silk Roads components",
  "городища «Ак-Бешим (Суяб)»", "Dual modern and historical naming; no China reference", "https://faolex.fao.org/docs/pdf/kyr161432.pdf"),
 ("Undated (current page)", "George Town World Heritage Incorporated", "Host state agency", "Malaysia", "George Town building types",
  "Among the types of buildings that can be found in George Town are shophouses, bungalows, mosques, churches, Chinese temples, Hindu temples, administration buildings, commerce and trade buildings, godowns and offices, water villages (clan jetties) and residential blocks.",
  "Multicultural; Chinese sites as one strand", "https://gtwhi.com.my/our-work/buildings/"),
 ("2005-07-14", "The Star (Malaysia)", "Host-country media", "Malaysia", "Bukit Cina cemetery, Melaka",
  "Bukit Cina, the ancient Chinese cemetery that became a controversial issue in the 1980s following a proposal to develop it, will be gazetted as an ancient monument.",
  "Contested site; state recognition after community dispute", "https://www.thestar.com.my/news/nation/2005/07/14/bukit-cina-to-be-gazetted"),
 ("Undated (register entry)", "Heritage Council of Victoria", "Host government", "Australia", "Bendigo Chinese Temple (Joss House), VHR H1791",
  "stands as sole reminder of once extensive Chinese community that flocked to this area during the gold rush",
  "Local gold-rush history; diaspora community", "https://vhd.heritagecouncil.vic.gov.au/places/34220"),
 ("Undated", "Article hosted by Peking University Center for African Studies", "Media, republished by a Chinese university", "Kenya", "Mambrui excavation (Peking University with National Museums of Kenya)",
  "undermines Portuguese explorer Vasco Da Gama's claim to have been the first international trader to open up East Africa",
  "Zheng He; China before Europe", "https://caspu.pku.edu.cn/en/publications/africanhistory/228981.html"),
]
sheet("1c Framing Examples",
      ["Date", "Actor", "Actor type", "Country", "Topic / site", "Original wording (as retrieved)", "Framing tags (my coding)", "Source", "Verification status"],
      [r + ("Check against source page",) for r in FR], [18, 34, 22, 14, 34, 64, 34, 44, 22], link_cols=(8,), fill_cols=(9,))

ws = wb["README"]
ws["A1"] = "Mapping Global China - Phase 1 source inventory (1a UNESCO, 1b Chinese sources, 1c host-country and diaspora sources)"
r = ws.max_row + 2
add = [
 ("Phase 1c (added 2026-10-05)", None),
 ("Host-country and diaspora sources surveyed", "=COUNTA('1c Host & Diaspora Sources'!B2:B200)"),
 ("Host-country framing examples", "=COUNTA('1c Framing Examples'!A2:A200)"),
 ("1c Host & Diaspora Sources", "Same inventory format as 1b, with a Region column: Malaysia, Central Asia, Cambodia, Kenya, United States, Australia and cross-country datasets."),
 ("1c Framing Examples", "How host-country bodies describe sites. Wording was retrieved through a web-reading tool, so each quote needs checking against its page (yellow column)."),
]
for i, (a, b) in enumerate(add):
    ws.cell(row=r + i, column=1, value=a).font = Font(name=F, size=11 if i == 0 else 10, bold=(i == 0))
    if b is not None:
        c = ws.cell(row=r + i, column=2, value=b); c.font = Font(name=F, size=10); c.alignment = Alignment(wrap_text=True, vertical="top")
wb.save(OUT); print("saved", OUT, len(INV), len(FR))
