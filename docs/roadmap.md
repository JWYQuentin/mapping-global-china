# Roadmap

The project runs in three stages: a feasibility study (Phases 0-7), a feasibility report to the supervisor, and then ML exploration and scale-up only after approval. Items marked *(supervisor)* come from the supervisor's brief; the rest are working suggestions.

Last updated: 2026-09-30.

## Phase 0: Admin and setup

- [ ] Arrange course credit through Columbia *(supervisor)*
- [x] Set up this repository with folders for raw data, processed data, scripts and docs
- [x] Start a data-lineage log ([data_lineage.md](data_lineage.md))
- [ ] Agree a check-in rhythm with the supervisor

## Phase 1: Source discovery and inventory

Feasibility items 1 (identify data sources) and 4 (incorporate UNESCO data systematically).

**1a. UNESCO** *(supervisor)*: done 2026-09-30

- [x] List every World Heritage and Tentative List entry for China
- [x] Flag transnational and serial nominations (Silk Roads, Maritime Silk Road)
- [x] Collect nomination files, advisory body evaluations and Committee decisions
- [x] Look beyond China's page at other UNESCO records (intangible heritage, Memory of the World, Silk Roads programme)
- [x] Document how UNESCO data can be pulled systematically

**1b. Chinese sources** *(supervisor)*: done 2026-09-30

- [x] Government: National Cultural Heritage Administration, Ministry of Culture and Tourism, national ICH database
- [x] Embassy websites in host countries
- [x] Universities and research institutes

**1c. Host-country and diaspora sources** *(supervisor)*

- [ ] Host-country heritage registers and institutions
- [ ] Records of Chinatowns, temples, cemeteries, clan and native-place associations, schools, ports, mining and railway sites

**1d. Non-site data** *(supervisor)*

- [ ] Legal agreements, heritage-protection frameworks and bilateral cooperation
- [ ] UNESCO meetings and nominations, institutional partnerships and training
- [ ] Archaeological and restoration projects involving Chinese institutions, foundations or companies

## Phase 2: Access assessment

Feasibility items 2 (APIs vs scraping) and 5 (can Chinese websites be searched or scraped).

- [ ] Record API, bulk download, scraping or manual collection for every source *(supervisor)*
- [ ] Check terms of use and robots.txt before scraping
- [ ] Test Chinese government, embassy, university and heritage sites for references to overseas heritage *(supervisor)*
- [ ] Log each test: query, hits, samples, problems

## Phase 3: Data model and entity matching

Feasibility item 3.

- [ ] Draft a linked model (Sites, Actors, Engagements, Framings, Designations, Sources) and map the supervisor's draft schema onto it *(supervisor)*
- [ ] Capture whether a "Chinese" framing appeared before or after Chinese institutional engagement *(supervisor)*
- [ ] Write the entity-matching strategy: UNESCO IDs as anchors, Wikidata crosswalk, multi-script name normalisation, fuzzy matching with a distance check, manual review queue *(supervisor)*

## Phase 4: Proof-of-concept dataset

Feasibility item 6: three or four countries or regions *(supervisor)*. Candidates to agree with the supervisor: Malaysia (Melaka, George Town), Central Asia (Kazakhstan, Kyrgyzstan), Cambodia (Angkor), Kenya (Lamu, Malindi), and a Western diaspora case for contrast.

## Phase 5: Tracking framing changes over time

Feasibility item 8 *(supervisor)*. Dated sources found so far: NCHA five-year plans (2017, 2021, 2026), embassy archives (from 2005), UNESCO nomination files and decisions, and the Wayback Machine.

## Phase 6: Automation vs manual verification

Feasibility item 7 *(supervisor)*: time and error rates per step, and which tasks need Chinese-language or domain judgement.

## Phase 7: Feasibility report

Covers all eight feasibility items and ends with a recommendation on whether a global dataset is feasible.

## Phases 8-9: after approval

ML exploration (entity matching, framing classification, narrative detection, clustering of engagement types) and scale-up into a Mapping Global China map layer.
