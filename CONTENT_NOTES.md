# Content and implementation notes

## Sources

- `Mikel_Val_Calvo_CV.pdf`, supplied by the owner as the CV sent to Kappa.ai: current positioning, experience, contribution scope, education, tools and team awards.
- Existing portfolio content, retained in Git history: initial research context and page routes.
- https://github.com/tecnomod-um/OntoGenix — public workflow and evaluation link.
- https://github.com/mikelval82/Biosignals — documented acquisition, triggers, labels, EDF output and software citation.
- https://github.com/mikelval82/NeuroSorter-Interface — source reference for the neural signal software.
- https://doi.org/10.1016/j.ipm.2024.104042 — Ontogenix publication reference already present in the source portfolio and supplied CV.

## Editorial changes

- Owner correction during review: based in Crevillente and no longer assigned to Inditex. The website and separate downloadable CV now identify Inditex as a previous assignment, without inventing an end date. The original supplied PDF is preserved.
- Industry experience and 2024–2025 LabLENI tenure follow the newer CV. Ongoing research collaboration is separate from employment.
- Replaced percentage skill bars with capabilities and linked work.
- Selected work separates individual contributions, programme context and team recognition.
- Replaced old long articles with concise project accounts and primary-source links. Prior article content remains in Git history.
- Omitted inconsistent OntoGenix success percentages and other performance/adoption/clinical figures not substantiated by the supplied CV or inspected sources. This is not a determination that those figures are false. Restore only with an attributable evaluation and precise conditions.
- Replaced broken image/video references with decorative, editable SVG illustrations in the build source. These illustrations are conceptual, not measured outputs or screenshots.
- Retained all six service routes with concise English capability pages grounded in the CV. Removed unsourced template-like examples and mixed-language copy.
- No confidential project details were added. The previous Inditex assignment follows the level of detail in the owner-supplied CV.

## Owner clarification for the next content iteration — 2026-09-25

- OntoGenix: the owner confirms responsibility for the concept, architecture, implementation and manuscript writing. Validation was carried out by other team members. Describe the principal contribution without implying sole project or paper authorship; preserve the full bibliographic attribution.
- The most difficult design decision was how to decompose the task into specialised agents while maintaining appropriate context. This will be the central technical narrative. Static code inspection establishes mechanisms, while the owner's account is needed for historical motives and alternatives.
- Other agent projects: the owner describes a primarily conceptual and high-level architectural contribution and has no code available to show. The exact project and adopted decisions remain to be identified. Review the existing CV-derived implementation wording project by project before expanding those claims.
- Recommended portfolio positioning: Research Engineer — Agentic AI & Knowledge Systems, targeting senior applied-research engineering opportunities and progressing towards broader technical leadership. This is career advice, not a change to the current TMC job title.
- These clarifications are incorporated into `TECHNICAL_PORTFOLIO_PLAN.md`. The corresponding case-page expansion and public copy revisions have not yet been applied.

## Repository review and case selection — 2026-09-25

- The owner confirms the historical motivation for specialisation in OntoGenix: several complex steps in an agent task produced hallucinations and errors; specialised roles narrowed both the task and its required context. This is an author account, not a measured reduction in hallucinations.
- Inspected source, prompt templates, the GUI orchestration and stored AmazonRating artifacts at OntoGenix commit `3c1693b6f1292920b479027fe889af9861d99555`; remote HEAD was checked and matched. No app/model execution or evaluation reproduction was performed.
- `case-studies/ontogenix.md` records the actual context inputs, explicit application state, bounded ontology retries and limitations. In particular, the second PlanSage response replaces `answer`, while OntoBuilder consumes that field: possible loss of the initial schema is a static-analysis concern, not a reproduced historical failure.
- Selected ASISVIA as the complementary architecture case. `case-studies/asisvia.md` separates the hospital's public project description, historical owner-supplied portfolio details, the owner's general contribution statement and still-unconfirmed individual decisions. Source: https://hospitalessanroque.com/es/transparencia.
- Do not restore former claims of production deployment, clinical benefit or measured session isolation based on that public description. Public project aims do not establish achieved outcomes or individual attribution.
- These are local planning and case-draft documents; this iteration has not modified website pages or the CV.

## Implemented technical portfolio iteration — 2026-09-25

- Owner authorised implementation. Homepage now foregrounds Research Engineer / Agentic AI & Knowledge Systems, with role-specific project cards and capability-to-evidence links.
- OntoGenix page now documents architecture, task context, two engineering decisions, stored AmazonRating artifacts and a six-dataset time-saving chart. Chart values and protocol come from the team's evaluation repository; validation is explicitly attributed to the team. No new model run or scientific validation was performed.
- Owner's specific ASISVIA clarification: conception of the generative AI system for managing interviews and analysing results. The page uses that confirmed contribution. It does not attribute session isolation, provider selection or production delivery to the owner.
- BIOSIGNALS source inspected at `821d3dd2d48c16bedf5e10f8cbbdc74d1a04f85a`. The GUI imports `data_manager_02`, whose annotations use sample index / sampling rate and whose stored files are NumPy dictionaries. The repository also includes an EDF writer. The page distinguishes these rather than claiming every current workflow writes EDF. No hardware experiment was run.
- Three capability pages replace six repetitive descriptions. Four static redirects preserve former routes; the sitemap lists canonical pages only.
- Diagrams and results chart use editable, accessible HTML/CSS in `site/technical_cases.py`. Diagram captions distinguish source reconstruction from conceptual design. Homepage illustrations remain decorative.
- Updated the separate downloadable CV: ASISVIA system conception and conceptual/high-level architectural scope replace broader implementation wording for those projects. Source PDFs remain intact.
- Changes are applied to local website pages and the downloadable CV, superseding the planning-only status of the preceding entries. No commit, push or public deployment has been performed.

## Technical changes

- Static HTML/CSS with a small JavaScript enhancement; the redesigned pages load no jQuery, Bootstrap, animation frameworks, remote fonts or trackers.
- Shared navigation, mobile menu, visible form labels, keyboard focus, skip link, responsive layouts and reduced-motion support.
- Existing contact destination preserved. Actual message delivery is not tested without an explicit instruction to send a message.
- Static link/asset/fragment checks in `site/check.py`; visual and interaction checks in a browser.
- Existing vendor assets are retained to avoid destructive cleanup, but are not loaded by the redesigned pages.
- GitHub Pages is unchanged until the owner chooses to publish the branch.

## Extension: HERO and biotechnology / 2026-09-25

- Added HERO Harness as a personal project case, with source-linked task contracts, execution ownership and Python structural verification. A local focused run passed 18 tests; no live-provider or full-suite result is claimed.
- Added Horizon Cyber-Vision as a featured prototype case. The owner confirmed concept, hardware, software and experiment design. The public publisher page confirms first and corresponding authorship. Only the abstract was accessible; detailed chapter review awaits the PDF.
- The RTVE video links to the wider project's context. Clinical outcomes are not attributed to the owner. No footage is rehosted.
- Added a dedicated biotechnology homepage section and an overview covering GEERT, MULTI_GEERT, GePHYCAM, BIOSIGNALS and NeuroSorter. Source-based implementation details accompany historical application screenshots from the owner's public repositories.
- Replaced the generic CNN claim in NeuroSorter with the actual imported UMAP/Louvain/template workflow. Source coauthor Javier Alegre-Cortes is acknowledged on the case page.
- AI-SpikeScope is omitted following the owner's explicit instruction after the supplied URL returned 404.
- Source revisions, files, ownership confirmations and remaining access limits are recorded in `case-studies/hero-and-neuroengineering.md`.
- These changes affect website content and structure. The downloadable and original CV files are unchanged in this iteration. No publication or deployment took place.

## Horizon Cyber-Vision full-paper update

The owner helped locate the full IWINAC 2022 proceedings on their Debian computer. The book was copied through authenticated SSH/SCP and its hash verified. The complete 15-page chapter has now been read; the earlier abstract-only access limitation is resolved.

The case now includes a source-based architecture diagram with two output paths, hardware and software components, three engineering trade-offs, the published processing rates and the behavioural study's protocol and limitations. The paper's five-volunteer simulated-vision evaluation is explicitly separate from the intracortical design and later clinical reporting. Source sections and figure numbers are recorded in `case-studies/hero-and-neuroengineering.md`.

An unchanged chapter extract is provided locally to the owner outside the website repository. The site links to the publication DOI rather than hosting the PDF. CV files are unchanged; no deployment was performed.
