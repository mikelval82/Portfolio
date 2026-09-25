# Validation record — 25 September 2026

Validated locally at `http://127.0.0.1:8765/` on branch `improve-portfolio`.

## Static checks

- `python site/check.py`: 13 HTML pages, 248 local references, no missing assets or fragments; one H1 and main landmark per page; form fields have associated labels.
- JavaScript syntax check passed (`Get-Content js/portfolio.js -Raw | node --check`).
- `git diff --check`: no whitespace errors.

## Browser checks

- All 11 main/project/capability pages returned HTTP 200 at desktop (1440 px) and mobile (390 px) viewport widths, with no horizontal document overflow or JavaScript page errors.
- Homepage also checked at 320 px and 768 px with no horizontal document overflow.
- Inspected rendered homepage, project grid and OntoGenix case study on desktop/mobile.
- Mobile menu opens, closes with Escape and closes after selecting a section. Anchor navigation leaves the target visible below the header.
- Navigation remains available with JavaScript disabled.
- The BIOSIGNALS screenshot is lazy-loaded; verified it decodes successfully after scrolling it into view.
- Contact form: intercepted HTTP 500 preserves the message and restores the submit button; intercepted HTTP 200 shows success and resets the fields. Both responses were mocked: no real messages were sent and actual Formspree delivery is unverified.
- CV download responds with HTTP 200 and `application/pdf`.

## Downloadable CV

- Updated only the portfolio copy: Crevillente added; Inditex contribution and assignment put in the past tense.
- Two pages and six hyperlinks preserved.
- Rendered and visually inspected both pages. Page 2 has identical rendered pixels to the supplied original.
- Original supplied PDF SHA-256: `699b3bfde0325ced94410a153ebf6d4729f04959d7abd27b5bb990fdf41f60b3`.
- Corrected portfolio copy SHA-256: `7a2d889499e0f8b6e339407c733cd828b1eba278d53f64f4a21a064586476ece`.

## Scope

No public deployment, real message delivery test, exhaustive accessibility audit or independent scientific-results audit was performed. The website and PDF remain ready for review locally.

## Latest iteration — technical cases implemented

This section supersedes the earlier page counts and downloadable-CV hash above.

- Static build: eight canonical pages, four redirect pages and two legacy entry pages. `site/check.py` checked all 14 HTML documents and 242 local references, including redirect fragments, with no errors.
- Ad hoc HTML nesting inspection passed. Rebuilding produced identical hashes for all generated HTML, sitemap and robots files.
- Playwright checked each of the eight canonical pages at 1440, 768, 390 and 320 px: 32 combinations, all HTTP 200, one H1, no document overflow and no JavaScript page errors. HTTP cache was disabled to avoid earlier preview content.
- Inspected rendered desktop homepage, OntoGenix architecture/table and results chart; mobile case summary, vertical diagram and ASISVIA page. The context table stays in a keyboard-focusable scrolling region (334 px viewport / 550 px content at the tested mobile width).
- Verified all four old routes navigate to their intended page or fragment. Mobile menu opens and closes with Escape. The OntoGenix architecture anchor lands below the 72 px header. ASISVIA navigation and all four conceptual-flow steps remain available without JavaScript.
- The contact handler was unchanged; its previously recorded mocked-response checks were not rerun. No messages were sent.
- Updated downloadable CV rendered with PyMuPDF and both pages visually inspected. The installed MiKTeX `pdftoppm` was unusable because its setup was unfinished; no system setup was changed. Two pages and six hyperlinks preserved; page 2 remains pixel-identical to the supplied original.
- Served PDF bytes match the corrected local PDF, with `application/pdf`. New SHA-256: `f51c065b50e005caded6a849fc13b20eacefd8927a47cecaafecdb1460a635ff`.
- Website rendering and content checks do not establish runtime correctness of OntoGenix or BIOSIGNALS, or reproduce either project's research evaluation.

## Latest extension: HERO, neuroprosthesis and biotechnology

This section supersedes the earlier page and reference counts.

- Build: 11 canonical pages, four redirects and two legacy entries. `python site/check.py` checks 17 HTML files and 319 local references without errors. Ad hoc HTML nesting inspection also passed.
- Playwright: all 11 canonical pages at 1440, 768, 390 and 320 px (44 combinations), all HTTP 200, one H1 per page, no document overflow, template placeholders or JavaScript page errors.
- Visually inspected the biotechnology section on desktop and mobile, the HERO header and introduction, and the Horizon Cyber-Vision mobile summary. Source screenshots for GEERT, GePHYCAM and NeuroSorter were also inspected. Element/full-page captures can relocate fixed navigation during capture; a normal viewport capture and DOM bounds confirmed the mobile page displays correctly, including the hidden skip link when unfocused.
- New Biotech navigation closes the mobile menu and positions the section below the header. Navigation and all six biotechnology entry links remain available with JavaScript disabled.
- Verified the changed `service-neuroprosthetics.html` redirect reaches `project-neuroprosthesis.html`.
- Focused HERO evidence: 18 tests passed for task compilation, execution and verification at public commit f8d256e5e7bb3e3a63ad2ad22ba01ed9edfe9a26. Command and scope are in `case-studies/hero-and-neuroengineering.md`.
- The biomedical applications were inspected statically, without devices or classification benchmarks. The full Horizon Cyber-Vision chapter was inaccessible; only its abstract and publication metadata were reviewed.
- The CV is unchanged: SHA-256 `f51c065b50e005caded6a849fc13b20eacefd8927a47cecaafecdb1460a635ff`. Contact behaviour is unchanged and no real messages were sent. No deployment was performed.

## Full Horizon Cyber-Vision chapter and case update

- Complete source chapter read from the owner-provided IWINAC 2022 proceedings (book PDF pages 406-420, printed pages 380-394). The copied book hash matches the remote source.
- Extracted a separate 15-page PDF outside the website repository. Reopened it and verified that every page renders pixel-identically to the source at 72 dpi; all pages also rendered at higher resolution. Hardware, architecture, GUI and results figures were visually inspected.
- Case expanded with architecture, output paths, component choices, published processing rates, experimental protocol and limitations. No new clinical efficacy claim or replication result.
- Static check: 17 pages, 323 local references, no errors. Diff whitespace check passed.
- Updated case checked at 1440, 768, 390 and 320 px: HTTP 200, one H1, two output branches, no page overflow or JavaScript errors. Desktop architecture and mobile performance table visually inspected. The two-column results table was adjusted to fit small screens without horizontal scrolling.
- Original and downloadable CV PDFs unchanged. The chapter PDF is not hosted by the portfolio. No deployment performed.

## Script structure and README review

- Separated repository configuration, shared page rendering and reusable HTML components from case content. The extended cases no longer import the OntoGenix content module for shared helpers.
- `python site/build.py` and `python site/build.py --check` pass. All 19 generated HTML/XML/text files and the downloadable PDF are byte-identical to the versions before this refactor.
- `python site/check.py`: 17 HTML pages, 323 local references, no errors. It now verifies the expected page inventory and reports a missing PDF without an unhandled file error.
- Isolated temporary-copy checks confirmed that stale and missing HTML fail `--check`, check mode writes no files, rebuilding restores a valid site, and a missing CV produces a diagnostic and nonzero exit status.
- All nine Python files pass syntax parsing. JavaScript syntax passed through `Get-Content -Raw -Encoding UTF8 js/portfolio.js | node --check`; passing the filename directly to Node was blocked by the local sandbox's path permissions.
- The optional CV migration has argument help, lazy dependency loading, an exact original-file hash check, source/output separation and explicit overwrite handling. Help works with Python site packages disabled. Importing the module performs no migration.
- Reproduced the CV into a temporary file using the existing local PyMuPDF tools. Both pages render pixel-identically to the reviewed downloadable CV at 1.6 scale; hyperlinks match. Existing-output, source-overwrite and unsupported-source rejection checks pass with `python -O`. Original and committed-copy hashes remain unchanged.
- README documents the actual module structure, active and legacy assets, editing commands, validation limits, optional CV dependency and the verified Pages source (`main`, repository root). Added a GitHub Actions workflow for generation consistency, static validation and JavaScript syntax. Its remote execution is separate from these local results.
