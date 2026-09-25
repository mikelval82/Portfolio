# HERO and neuroengineering — editorial evidence

Reviewed 2026-09-25. This extends the implemented portfolio. Source review is not hardware or clinical validation.

## Owner confirmations

- HERO Harness is a personal project.
- The owner designed the prototype used by Miguel Terol for behavioural experiments.
- Clarified contribution: concept, hardware, software and experiment design.
- The owner supplied *Horizon Cyber-Vision: A Cybernetic Approach for a Cortical Visual Prosthesis* as the relevant paper.
- AI-SpikeScope returned 404 via GitHub and API; owner explicitly instructed us to omit it. No description inferred from its name.

## Pinned public sources

| Repository | Reviewed revision | Main evidence |
| --- | --- | --- |
| hero-harness | f8d256e5e7bb3e3a63ad2ad22ba01ed9edfe9a26 | application/task_contracts.py, contract_execution.py, contract_verifier.py and corresponding tests |
| MULTI_GEERT | 6ff720ad6bc528ea09e7cd4c88767b48090d8259 | DATA_MANAGER/data_acquirer.py, GUI/M_GEERT_gui.py, README.md |
| GEERT | dba0579863476c508c03a730e7a66bbdb68845d6 | BCI_STANDARD_EXPERIMENT_03.py, README.md, images/GEERT.png |
| GePHYCAM | a2db8cffe89504000b984bcfd82288d6253f7332 | DATA_MANAGERS/video_data_manager.py, GUI/integrator_GUI_00.py, README.md, images/GePHYCAM.png |
| NeuroSorter-Interface | af32c9721c422bd8a29587e7a15d0c98380b0a81 | AUTO_SPIKE_SORTING_GUI.py, CLEANER/cleaner_03.py, SORTER/sorter_umap_louvain_templates.py, README.md, Images/GUI_overview.png |

These repositories were cloned into the parent workspace's temporary research directory, independently of older local working trees. No source application was edited.

## Technical conclusions

- HERO compiles deterministic, immutable per-task JSON; required and context nodes are distinct. The execution service recognises mission/chat/mcp actors and rejects a second active lease. Python verification checks source structure, not behavioural correctness.
- Focused local HERO tests passed: 18 across `tests.application.test_task_contracts`, `test_contract_execution` and `test_contract_verifier`. Command: `python -c "import sys,unittest; sys.path.insert(0,'src'); suite=unittest.defaultTestLoader.loadTestsFromNames(['tests.application.test_task_contracts','tests.application.test_contract_execution','tests.application.test_contract_verifier']); result=unittest.TextTestRunner(verbosity=1).run(suite); sys.exit(not result.wasSuccessful())"`. No provider calls or full-suite claim.
- MULTI_GEERT retains sample timestamps from LSL and separates per-stream buffers/monitors. This does not establish measured synchronisation accuracy. Synthetic source is documented in EEG_generator.py.
- GEERT exposes experiment start/stop/labels and dynamic analysis modules. Historical Linux and hardware requirements remain relevant.
- GePHYCAM separates OpenBCI, E4 and video data managers; saving collects these modalities. Source does not itself establish end-to-end timing accuracy.
- NeuroSorter's entry point imports cleaner_03 and sorter_umap_louvain_templates. These use UMAP/Louvain plus reference/template matching, including DTW in the selected sorter. The prior generic CNN description was removed. Source credits Mikel Val Calvo and Javier Alegre-Cortés, so the page identifies collaborative development.

## Horizon Cyber-Vision access and attribution

- Publisher: https://link.springer.com/chapter/10.1007/978-3-031-06242-1_38
- DOI: https://doi.org/10.1007/978-3-031-06242-1_38
- IWINAC 2022, LNCS 13258, pp. 380–394. Mikel is first and corresponding author on the publisher page.
- Public abstract accessed. Full chapter is subscription content; the PDF was not accessible. Detailed hardware/software architecture, figures and quantitative findings await the owner's PDF.
- Current public case uses the abstract for the general research approach and the owner's statements for personal contribution. It does not infer component choices, measured performance or clinical efficacy.
- Video: https://www.youtube.com/watch?v=j2a538ZC9pA — RTVE Noticias, duration 1:36. Browser access confirmed title and description; the consent overlay limited frame inspection. No detailed component identification or video timestamp is claimed. Linked externally, with no rehosted footage or thumbnail.
- Institutional project context: https://cortivis.umh.es/es/
- The prototype role is separate from the clinical study and the wider team's outcomes.

## Editorial placement

- Lead cases: OntoGenix, HERO Harness and Horizon Cyber-Vision.
- Dedicated homepage biotechnology section and a software overview page preserve the breadth of GEERT, MULTI_GEERT, GePHYCAM, BIOSIGNALS and NeuroSorter.
- ASISVIA stays accessible as a complementary conception case.
- The historical neuroprosthetics route now resolves to Horizon Cyber-Vision.
- Original and downloadable CV PDFs remain unchanged in this iteration.

## Source access update: owner-provided PDF excerpt

The owner's Debian computer was reached through authenticated SSH, and the named paper was copied with SCP to the local research directory. Local and remote SHA-256 match: `a251ff5714f137c4e9ad1878307b16627e9aa80c513f6e77e93a5a5e2e935655`.

The file contains only two pages: the article's first page (380) and last page (394). Both were rendered and visually inspected. They confirm the title, authors and abstract, but do not include the architecture, methods or experimental sections. The full-chapter access limitation therefore remains. No technical claims were added from missing pages, and no paper PDF was added to the public portfolio assets.

## Full chapter recovered and reviewed

This update supersedes the earlier access limitation. The complete chapter was found in the owner's IWINAC 2022 proceedings. The local book copy matches the remote SHA-256: `4852310766246ac4fea5272b3b547ac6c0af5404123044b4d645fbb7e672493e`. PDF pages 406–420 correspond to printed pages 380–394.

A separate 15-page PDF was extracted for the owner outside the website repository. All 15 pages render pixel-identically to the corresponding book pages. Chapter SHA-256: `4097a5f4af0a2a3b777cd855880ce995a3d7d0ee349a2aaef7a8db5e62798176`. No source pages were changed or added to public website assets.

Evidence incorporated into the case:

- Sections 2.1–2.5, Figures 4–7: shared acquisition/processing architecture with separate SPV display and cortical-stimulation output paths; independent processes and configurable experiment GUI. The new HTML diagram is an editorial summary of these components.
- Hardware (pp. 384–385): Logitech C920, headset/display, Tobii Pro3, Jetson TX2, battery/backpack; the cortical configuration includes the 96-channel Utah array and Ripple Summit system. These are components of the system described in the paper, not a claim of inventing or manufacturing each commercial component.
- Software (pp. 385–387): Python multiprocessing, PyQt5, Jetson-inference and PyTorch; gaze-defined ROI; selectable drivers, object/stimulus associations and logging.
- Section 2.5 processing figures: camera 37.78 ± 2.84 frames/s; depth 42.21 ± 4.54; object detection 23.99 ± 2.15; SPV 45.92 ± 8.32; eye tracking 100 Hz. The ± statistic is not defined there and is not labelled as a standard deviation or confidence interval. These are not end-to-end latency figures and were not reproduced locally.
- Sections 2.6–3: five volunteers, blindfolded/cane versus SPV, five repetitions per condition and environment, corridor plus StreetLab, 32 × 32 simulated phosphenes. Blindfolded trials precede SPV trials. Walking time and collisions are the reported behavioural measures.
- Figures 10–11 and discussion: adaptation in the corridor; SPV walking time not yet plateaued after five trials; similar StreetLab walking times but more collisions under SPV and route-dependent behaviour. No unsupported superiority or clinical efficacy claim.
- Section 4 explicitly says the development cycle is incomplete and only SPV has been tested in this work. The prototype attribution supplied by the owner and the later RTVE project report remain separate from the 2022 evaluation.

The relevant hardware, architecture, GUI and result figures were inspected visually, alongside the full chapter text.
