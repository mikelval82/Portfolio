# Mikel Val Calvo — Research & Engineering

Static professional portfolio for agentic AI, knowledge systems, biotechnology and neuroengineering.

- [Public portfolio](https://mikelval82.github.io/Portfolio/)
- [Downloadable CV](Mikel_Val_Calvo_CV.pdf)
- Website source: this repository, `mikelval82/Portfolio`.
- [Professional-Profile](https://github.com/mikelval82/Professional-Profile) is a separate repository for supplied CVs. When this checkout sits inside it, run the commands below from the **Portfolio** directory.

## Preview and validate

Use Python **3.12 or newer**. Building and checking the site use only the standard library: no package installation, API credentials or Node.js are needed.

```powershell
python site/build.py
python site/build.py --check
python site/check.py
python -m http.server 8765 --bind 127.0.0.1
```

Open <http://127.0.0.1:8765>. Stop the preview server with Ctrl+C. Build commands resolve paths relative to their own location, not the working directory; the preview server serves the directory where it is started.

## Source structure

Only `build.py`, `check.py` and the optional `update_cv.py` are executable commands. The other Python files are imported modules. Run scripts by path as shown above; `site` is also a Python standard-library module, so do not use `python -m site.build`.

| File | Responsibility |
| --- | --- |
| `site/build.py` | Assemble page content, generate HTML/robots/sitemap, or check generated files without writing. |
| `site/check.py` | Check the expected HTML inventory, local links, redirect targets, fragments, basic HTML semantics and PDF signature. |
| `site/config.py` | Repository path and public base URL. |
| `site/render.py` | Shared HTML shell, navigation, metadata, artwork and case-page layout. |
| `site/components.py` | Reusable flow diagrams, case summaries and source links; independent of case content. |
| `site/home.html` | Homepage source template and artwork placeholders. |
| `site/technical_cases.py` | OntoGenix, ASISVIA and BIOSIGNALS content, including the context table and evaluation chart. |
| `site/extended_cases.py` | HERO, Horizon Cyber-Vision, biotechnology and NeuroSorter content. |
| `site/capabilities.py` | Three capability areas and four legacy redirect definitions. |
| `site/update_cv.py` | Optional, one-off migration of the exact original CV. Never run during a website build. |
| `css/portfolio.css` | Active design tokens, responsive layouts, print and reduced-motion styles. |
| `js/portfolio.js` | Active mobile navigation and contact-form enhancement. |
| `images/` | Portraits, source-attributed screenshots and favicon. |

Content modules use `components.py`; `build.py` passes their data to `render.py` and writes the results. Importing these modules does not write files or process the CV. Older `css/style.css`, `js/script.js` and `plugins/` remain from the previous template and are not loaded by the current pages.

## Editing workflow

1. Edit the relevant source template, content module, CSS or JavaScript. Root-level HTML files are generated: do not edit them directly.
2. Run `python site/build.py` after changing templates or Python content.
3. Run `python site/build.py --check` and `python site/check.py`. The first exits with an error if any of the 19 generated files is missing or stale; the second currently checks 17 HTML pages and 323 local references.
4. Preview affected pages on desktop and mobile. With Node.js installed, `node --check js/portfolio.js` also checks JavaScript syntax.
5. Review `git diff` and commit both source changes and regenerated output. The build is deterministic and does not modify the PDF.

The static checks do not verify external links, layout, accessibility conformance, real contact delivery or scientific results. See [VALIDATION.md](VALIDATION.md) for the actual browser and artifact checks. GitHub Actions runs generation consistency, static checks and JavaScript syntax on pushes and pull requests.

## Publication

GitHub Pages is configured to publish the **root of `main`**. Generated HTML is committed, so the host does not need Python. Pushing a feature branch makes the changes available for review; merging it into `main` triggers publication. The validation workflow does not deploy the site.

For a contribution, push the working branch and open a pull request targeting `main`. Check its validation results and the diff before merging. Neither `build.py` nor `check.py` commits, pushes or deploys anything.

## Pages and behaviour

The homepage leads with OntoGenix, HERO and Horizon Cyber-Vision, followed by biotechnology, experience, expertise, research, background and contact. Eleven canonical pages cover the homepage, seven cases and three capability areas. Four old routes redirect using static HTML refresh plus a visible link; two generic legacy entry pages remain available with `noindex`. The sitemap contains only canonical pages. Legacy section anchors remain valid, and `#biotechnology` provides a direct entry point.

Navigation and content work without JavaScript. JavaScript adds the mobile disclosure menu, Escape handling and enhanced submission to the existing Formspree endpoint. A direct email link remains available. Automated form checks use intercepted responses and send no real messages.

## Downloadable CV

`Mikel_Val_Calvo_CV.pdf` is the reviewed website copy: Crevillente, a previous Inditex assignment, and the owner's clarified contributions to ASISVIA and other agent projects. The original supplied PDF is preserved outside this repository.

`site/update_cv.py` documents corrections to that specific original two-page PDF. It is **not a general CV generator**: the original SHA-256 must match, coordinates depend on its layout, and applying it requires PyMuPDF and Windows Calibri. Its help works without PyMuPDF:

```powershell
python site/update_cv.py --help
# Optional reproduction on Windows, using the preserved original:
python -m pip install PyMuPDF
python site/update_cv.py ..\Mikel_Val_Calvo_CV.pdf ..\CV-corrected-review.pdf
```

The command never changes the source. Replacing an existing output requires `--overwrite`. Render and inspect both output pages before replacing the checked-in CV. A matching PDF signature alone does not establish a correct layout.

## Evidence and editorial notes

The cases distinguish implementation, conceptual design, collaborative software and prototype design. HERO is a personal project. Horizon Cyber-Vision uses the complete 2022 chapter, separating published processing rates and its five-volunteer SPV study from clinical outcomes. The chapter PDF is not hosted here. AI-SpikeScope is excluded at the owner's request.

- [CONTENT_NOTES.md](CONTENT_NOTES.md): sources, attribution and editorial boundaries.
- [case-studies/](case-studies/): supporting research notes and an editable diagram.
- [TECHNICAL_PORTFOLIO_PLAN.md](TECHNICAL_PORTFOLIO_PLAN.md): improvement plan and implementation history.
- [VALIDATION.md](VALIDATION.md): chronological validation record; later entries supersede earlier counts and limitations.
