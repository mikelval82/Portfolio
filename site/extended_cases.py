"""Personal agent engineering and biomedical research, tied to public evidence."""
from components import flow, summary, source

HERO = 'https://github.com/mikelval82/hero-harness/blob/f8d256e5e7bb3e3a63ad2ad22ba01ed9edfe9a26/'
MULTI = 'https://github.com/mikelval82/MULTI_GEERT/blob/6ff720ad6bc528ea09e7cd4c88767b48090d8259/'
GEERT = 'https://github.com/mikelval82/GEERT/blob/dba0579863476c508c03a730e7a66bbdb68845d6/'
GEPHY = 'https://github.com/mikelval82/GePHYCAM/blob/a2db8cffe89504000b984bcfd82288d6253f7332/'
NEURO = 'https://github.com/mikelval82/NeuroSorter-Interface/blob/af32c9721c422bd8a29587e7a15d0c98380b0a81/'
PAPER = 'https://doi.org/10.1007/978-3-031-06242-1_38'
VIDEO = 'https://www.youtube.com/watch?v=j2a538ZC9pA'

def resources(items):
    return '<ul class="resource-list">'+''.join(f'<li><a href="{url}">{name} ↗</a><span>{detail}</span></li>' for url,name,detail in items)+'</ul>'

def screenshot(path, alt, caption, width, height):
    return f'<figure><a href="{path}" aria-label="Open full-size application screenshot"><img src="{path}" alt="{alt}" width="{width}" height="{height}" loading="lazy"></a><figcaption>{caption} Select the image to inspect it at full size.</figcaption></figure>'

EXTENDED_CASES = [
dict(path='project-hero.html', title='HERO Harness', eyebrow='Personal project / Agent engineering',
 deck='Turning a software task into an explicit contract, controlled execution and inspectable evidence.',
 meta='Personal project · Python · Public source', art='runtime',
 role='Personal software-engineering project: design and development of the agent orchestration runtime.',
 cover=summary([('My contribution','Personal project: architecture and development'),('Engineering focus','Task context, execution ownership and verification'),('Evidence','Public implementation and focused contract tests')]),
 sections=[
 ('overview','What does it mean for an agent to finish?',
  '<p>An agent can produce a plausible patch while leaving part of a task unresolved. HERO explores how a software-engineering runtime can make the intended change explicit and check the resulting code against it.</p><p>My personal project brings together task decomposition, approved design snapshots and recorded execution. It extends the context-design questions in <a href="blog-ontogenix.html">OntoGenix</a> into software engineering: what a task owns, what it needs to know and what evidence is required to accept its result.</p>'),
 ('architecture','From approved design to verification',
  flow('HERO contract execution path', [('Approve','Brief and design snapshot'),('Compile','ChangeSet and task contract'),('Execute','One active execution lease'),('Verify','Code checks and recorded evidence')],
       'The runtime separates the task definition, the executor and the acceptance checks. Graph Lab is a separate visual client, connected through an authenticated local worker API.')+
  '<p>The public implementation separates domain models, application services and adapters. This makes the contract and execution rules inspectable independently of an LLM provider or a graphical interface.</p>'),
 ('decisions','Three concrete engineering decisions',
  '<div class="decision"><p class="eyebrow">01 / Context with ownership</p><h3>A contract per task</h3><p>The compiler selects the relevant operations, nodes, relationships and validation obligations from an approved snapshot. It marks nodes as required or contextual: information needed to understand a change does not automatically become another implementation obligation.</p><p>The JSON is deterministically ordered. Replacing an existing contract with different content raises a conflict.</p>'+source('src/mission_orchestrator/application/task_contracts.py','Inspect TaskContractCompiler',HERO)+'</div>'+
  '<div class="decision"><p class="eyebrow">02 / Coordination</p><h3>One owner of execution</h3><p>Mission, chat and MCP are recognised execution actors. The contract execution service rejects a second executor while a lease is active and checks whether the mission stage permits the requested action.</p><p><strong>Trade-off:</strong> serial ownership makes coordination easier to reason about, but limits concurrent execution within that mission.</p>'+source('src/mission_orchestrator/application/contract_execution.py','Inspect begin, validate and complete',HERO)+'</div>'+
  '<div class="decision"><p class="eyebrow">03 / Evidence</p><h3>Check the code structure</h3><p>The Python verifier parses source without executing it. It checks required paths, declarations, signatures and supported relationships, while reporting contextual or external nodes as advisory. Completion is refused when a required structural check fails.</p><p><strong>Boundary:</strong> structural agreement does not establish correct runtime behaviour. Project tests and execution evidence remain necessary.</p>'+source('src/mission_orchestrator/application/contract_verifier.py','Inspect PythonContractVerifier',HERO)+'</div>'),
 ('evidence','A reproducible, bounded check',
  '<p>A focused local run passed <strong>18 tests</strong> across task-contract compilation, contract execution and the Python verifier at revision <code>f8d256e</code>. The tests cover immutable task context, competing executors and acceptance failures, among other cases.</p><p class="source-note">This is a local contract test run, not a full suite result or a live LLM-provider evaluation. No productivity benchmark or production deployment is claimed.</p>'+
  resources([(HERO+'tests/application/test_task_contracts.py','Task contract tests','Deterministic compilation, immutable content and contextual nodes.'),(HERO+'tests/application/test_contract_execution.py','Execution tests','Lease conflicts, patch scope and completion checks.'),(HERO+'tests/application/test_contract_verifier.py','Verifier tests','Structural obligations and failure cases.'),('https://github.com/mikelval82/hero-harness','Explore HERO Harness','Current repository, setup and architecture documentation.')]))],
 next=('blog-ontogenix.html','OntoGenix')),

dict(path='project-neuroprosthesis.html', title='Horizon Cyber-Vision', eyebrow='Neuroengineering / Experimental prototype',
 deck='Concept, hardware, software and experiment design for cortical visual prosthesis research.',
 meta='Universidad Miguel Hernández · IWINAC 2022 · Collaborative research', art='signal',
 role='Prototype concept, hardware and software design, and behavioural experiment design. First and corresponding author of the 2022 paper.',
 cover=summary([('My contribution','Concept, hardware, software and experimental design'),('Research setting','Prototype used by Miguel Terol in behavioural experiments'),('Evidence','Research publication and reporting on the wider project')]),
 sections=[
 ('contribution','Engineering the experiment as a system',
  '<p>I designed the experimental prototype used by Miguel Terol in behavioural experiments. My contribution covered its concept, hardware and software, together with the design of experiments.</p><p>This work connects my software-engineering background to physical prototypes and human behaviour: the research question, the system a participant uses and the experimental task have to make sense together.</p>'),
 ('approach','An engineering cycle around behaviour',
  '<p>The research question is how to turn a camera view into information that helps a person navigate. The prototype connects visual processing, gaze and an output representation; behavioural tasks then expose the limitations of that representation.</p><p>The 2022 paper describes a shared platform for simulated prosthetic vision (SPV) and a cortical prosthesis. Its reported experiments evaluate the simulation path. The intracortical path is part of the system design, with further validation still ahead in that publication.</p>'),
 ('architecture','One platform, two output paths',
  flow('Shared visual processing and gaze pathway', [('Capture','Scene camera and eye-tracking input'),('Process','Image, depth, object and edge information'),('Select','Configurable region around gaze position'),('Route','Simulation display or stimulation interface')],
       'Architecture summary based on sections 2.1–2.5 and Figure 5. Image processing and gaze acquisition run in separate processes; the selected information feeds the output path.')+
  '<div class="output-paths"><div><p class="eyebrow">Evaluated in the paper</p><h3>Simulated vision</h3><p>Generate a phosphene representation and display it in the headset. The proof-of-concept experiments use a 32 × 32 phosphene grid.</p></div><div><p class="eyebrow">Cortical system design</p><h3>Stimulation interface</h3><p>Replace the simulation stage with stimulus generation through the Ripple system and the intracortical array.</p></div></div>'+
  '<p>The hardware design brings together a Logitech C920 camera, Tobii Pro3 eye tracking and an NVIDIA Jetson TX2. The simulation uses a headset display; the cortical configuration includes a 96-channel Utah array and a Ripple Summit neuroprocessor. Battery power and a backpack support the portable arrangement.</p>'+
  '<p>The software uses Python multiprocessing, a PyQt5 experiment interface, Jetson-inference and PyTorch. The interface controls recording, activates individual drivers, associates detected objects with stimulation patterns and exposes process state through a logger.</p>'+
  f'<p class="source-note"><a href="{PAPER}">Hardware and software: sections 2.1–2.5, Figures 4–7, pp. 384–387 ↗</a></p>'),
 ('decisions','Engineering choices and their trade-offs',
  '<div class="decision"><p class="eyebrow">01 / Modularity</p><h3>Separate acquisition, processing and output</h3><p>Camera, gaze, depth and other drivers can be activated independently. The output can change from a simulated display to stimulation while retaining the upstream processing. This makes the prototype configurable for different experiments; timing across processes remains an integration concern.</p></div>'+
  '<div class="decision"><p class="eyebrow">02 / Context selection</p><h3>Use gaze to define the region of interest</h3><p>Eye tracking provides a region around the gaze position, reducing the visual information that needs to be encoded. The trade-off is dependence on gaze estimation and calibration. The paper also identifies eye movements and phosphene locations as challenges for the cortical configuration.</p></div>'+
  '<div class="decision"><p class="eyebrow">03 / Experimental feedback</p><h3>Evaluate the representation through navigation</h3><p>The initial simulation applies Canny edges and Gaussian convolution. Walking time and collisions show whether this simplified representation is useful in a task. The paper treats it as a starting point: the simulation does not reproduce all the properties of electrically evoked phosphenes.</p></div>'),
 ('performance','Reported processing rates',
  '<div class="table-scroll" role="region" aria-label="Processing rates reported in the 2022 paper" tabindex="0"><table><caption>Published prototype measurements · section 2.5</caption><thead><tr><th scope="col">Process / visualisation</th><th scope="col">Reported rate</th></tr></thead><tbody><tr><th scope="row">Camera image</th><td>37.78 ± 2.84 frames/s</td></tr><tr><th scope="row">Monocular depth</th><td>42.21 ± 4.54 frames/s</td></tr><tr><th scope="row">Object detection</th><td>23.99 ± 2.15 frames/s</td></tr><tr><th scope="row">Simulated prosthetic vision</th><td>45.92 ± 8.32 frames/s</td></tr><tr><th scope="row">Eye-tracking data</th><td>100 Hz</td></tr></tbody></table></div>'+
  '<p class="source-note">These are the paper’s per-process figures for its prototype and configuration. They are not a measurement of complete camera-to-stimulation delay. The ± values are reproduced as reported; section 2.5 does not identify their statistical definition. These measurements were not rerun for this portfolio.</p>'),
 ('evaluation','What the behavioural study established',
  '<p><strong>Protocol:</strong> five volunteers, two environments and two conditions: blindfolded with a cane, and simulated prosthetic vision. Each condition was repeated five times per volunteer in the obstacle corridor and StreetLab. The blindfolded condition came first. Outcomes were walking time and collisions.</p><p>The corridor results show adaptation over repeated trials; the SPV walking-time curve had not plateaued after five trials. In StreetLab, walking times were similar across conditions, while SPV produced more collisions and performance varied by route. These findings identify changes needed in the visual representation and evaluation protocol.</p><p><strong>Limits:</strong> the sample is small, condition order is fixed, and the tested simulation simplifies cortical perception. The publication presents a proof of concept, with the full cybernetic development cycle still incomplete. It does not establish clinical efficacy of the implanted system.</p>'+
  f'<p class="source-note"><a href="{PAPER}">Protocol, results and discussion: sections 2.6–4, Figures 8–11, pp. 388–391 ↗</a></p>'),
 ('publication','Publication',
  resources([(PAPER,'Horizon Cyber-Vision: A Cybernetic Approach for a Cortical Visual Prosthesis','Mikel Val Calvo et al. · IWINAC 2022 · LNCS 13258 · pp. 380–394. First and corresponding author.')])),
 ('context','The prototype in its research context',
  '<p>The RTVE report introduces Miguel Terol and the wider UMH visual-prosthesis research. My contribution here is the experimental prototype and experiment design; the clinical study and its outcomes belong to the multidisciplinary research team.</p>'+
  f'<a class="media-link" href="{VIDEO}"><span class="media-play" aria-hidden="true">▶</span><span><strong>Watch the RTVE report</strong><small>Project context · YouTube · 1 min 36 s</small></span><span aria-hidden="true">↗</span></a>'+
  resources([('https://cortivis.umh.es/es/','Cortivis · UMH','Institutional context for the cortical visual prosthesis programme.')]))],
 next=('project-biotechnology.html','Biotechnology & neuroengineering software')),

dict(path='project-biotechnology.html', title='Biotechnology & neuroengineering', eyebrow='Research portfolio / Scientific software',
 deck='Software for acquiring signals, recording experimental context and analysing neural activity.',
 meta='EEG · Physiology · Video · Neural waveforms', art='signal',
 role='Research software design and development across EEG, multimodal acquisition and neural signal analysis. NeuroSorter is collaborative work.',
 cover=summary([('Breadth','EEG, physiological signals, video and spikes'),('Engineering focus','Acquisition, buffering, event labels and analysis interfaces'),('Evidence','Public source and historical application screenshots')]),
 sections=[
 ('overview','The software behind an experiment',
  '<p>My biotechnology and neuroengineering work spans the tools used to collect data, preserve experimental context and inspect the resulting signals. These projects address different parts of that workflow.</p>'+
  flow('Research software portfolio map',[('EEG','GEERT and MULTI_GEERT'),('Physiology + video','GePHYCAM and BIOSIGNALS'),('Neural analysis','NeuroSorter')], 'A map of complementary projects, not a claim that the repositories form one integrated system.')+
  '<p>Alongside the software, I designed the concept, hardware, software and experiments for the <a href="project-neuroprosthesis.html">Horizon Cyber-Vision prototype</a>.</p>'),
 ('geert','GEERT · EEG experimentation',
  '<p>GEERT brings EEG acquisition, visualisation, signal processing and event labels into a BCI research interface. An external experiment can send start, stop and label messages through TCP/IP; the application coordinates recording and exposes hooks for Python analysis modules.</p><p>The key design concern is keeping the recorded signal connected to the experimental task. The repository documents EDF output and a Linux-based environment.</p>'+
  screenshot('images/geert-interface.png','GEERT interface with multichannel EEG traces, spectral views and recording controls','Historical GEERT screenshot from the project repository.',811,527)+
  resources([(GEERT+'BCI_STANDARD_EXPERIMENT_03.py','Application and recording lifecycle','Source: acquisition, trigger handling and GUI coordination.'),('https://github.com/mikelval82/GEERT','GEERT repository','Documentation, dependencies and research-software citation.') ])),
 ('multi-geert','MULTI_GEERT · Multiple EEG streams',
  '<p>MULTI_GEERT extends the acquisition problem to several devices using Lab Streaming Layer. The interface discovers streams, lets the researcher select them and creates a monitor for each chosen EEG inlet.</p><p>A separate acquisition process maintains per-stream buffers and state. It retains the timestamp returned with each LSL sample, while remote commands can be distributed to the monitors. The repository also includes a synthetic EEG generator for development without a physical device.</p><p><strong>Engineering boundary:</strong> retaining timestamps supports alignment; timing accuracy across devices still needs measurement in the actual experiment.</p>'+
  resources([(MULTI+'DATA_MANAGER/data_acquirer.py','Acquisition process and per-stream buffers','Inspect how samples and timestamps enter the data managers.'),(MULTI+'GUI/M_GEERT_gui.py','Stream selection and monitor lifecycle','Inspect the separation between acquisition and presentation.'),('https://github.com/mikelval82/MULTI_GEERT','MULTI_GEERT repository','Setup, synthetic streams and remote-control protocol.') ])),
 ('gephycam','GePHYCAM · Physiology and video',
  '<p>GePHYCAM brings EEG, peripheral physiological signals and a camera into one experimental interface. Its code separates data managers for OpenBCI, Empatica E4 and video, and coordinates recording through the application controls.</p><p>The video manager consumes frames through a queue and maintains its own buffer. The saving path collects data from the separate managers; the documented formats are EDF for physiology and MP4 for video. Event labels provide the behavioural context.</p>'+
  screenshot('images/gephycam-interface.png','GePHYCAM displaying EEG, physiological traces and a camera view in a shared experiment interface','Historical GePHYCAM screenshot from the project repository.',801,586)+
  resources([(GEPHY+'DATA_MANAGERS/video_data_manager.py','Video acquisition and buffering','Thread, queue and frame storage.'),(GEPHY+'GUI/integrator_GUI_00.py','Recording coordination and saving','The shared interface joins the separate data managers.'),('https://github.com/mikelval82/GePHYCAM','GePHYCAM repository','Documentation and research-software citation.') ])),
 ('analysis','BIOSIGNALS and NeuroSorter',
  '<p><a href="blog-biosignals.html">BIOSIGNALS</a> focuses on physiological acquisition, event annotations and recording control. Its case study follows the sample-based event timing and storage path.</p><p><a href="blog-neurosorter.html">NeuroSorter</a> addresses the analysis stage: cleaning neural waveforms, grouping spikes and letting the researcher inspect and adjust the result. The inspected interface connects UMAP-based graph construction, Louvain clustering and template comparison.</p>'),
 ('scope','Research use and evidence',
  '<p>The repositories and screenshots show the implemented workflows. They are research software with version-specific hardware and dependency requirements. This portfolio review inspected the source; it did not reconnect the devices or reproduce timing, classification or clinical validation.</p><p>The common engineering thread is making experiments workable: clear component boundaries, retained event information and interfaces that keep the researcher involved.</p>')],
 next=('blog-neurosorter.html','NeuroSorter')),

dict(path='blog-neurosorter.html', title='NeuroSorter', eyebrow='Research software / Neural signal analysis',
 deck='Connecting automated waveform cleaning and clustering with researcher inspection.',
 meta='Collaborative research software · Python · PyQt5', art='signal',
 role='Collaborative software development with Javier Alegre-Cortés, credited in the public source.',
 cover=summary([('My contribution','Collaborative research software development'),('Engineering focus','Cleaning, clustering, template comparison and manual curation'),('Evidence','Public algorithms, application wiring and interface')]),
 sections=[
 ('overview','From waveforms to inspectable groups',
  '<p>Neural recordings contain candidate spikes alongside noise and artefacts. NeuroSorter connects automated cleaning and grouping to a graphical interface where researchers can inspect waveforms and adjust unit assignments.</p>'+
  screenshot('images/neurosorter-interface.png','NeuroSorter waveform viewer with automatic cleaning, sorting and manual unit-curation controls','Historical interface screenshot from the collaborative repository.',1824,890)),
 ('architecture','The implemented analysis path',
  flow('NeuroSorter analysis components',[('Load','Recording and waveform data'),('Clean','Graph clusters and reference waveforms'),('Sort','UMAP graph, Louvain and template matching'),('Inspect','Waveform display and manual curation')],
       'The application wires a spike denoiser and a template-based sorter into the data manager, then connects the GUI to that manager.')+
  '<p>The cleaner normalises waveforms, constructs a UMAP neighbourhood graph and partitions it using Louvain. It compares cluster waveforms with spike and artefact references.</p><p>The sorter also builds a UMAP graph and uses Louvain communities. In the variant selected by the application, a subsequent template comparison uses dynamic time warping. The interface documents manual reassignment, rejection as noise and undo of the latest edit.</p>'+
  resources([(NEURO+'AUTO_SPIKE_SORTING_GUI/AUTO_SPIKE_SORTING_GUI.py','Application wiring','The actual cleaner and sorter imported by the GUI.'),(NEURO+'AUTO_SPIKE_SORTING_GUI/CLEANER/cleaner_03.py','Waveform cleaner','Neighbourhood graph, communities and reference comparison.'),(NEURO+'AUTO_SPIKE_SORTING_GUI/SORTER/sorter_umap_louvain_templates.py','Template-based sorter','Clustering followed by template comparison.') ])),
 ('decisions','Keep automated analysis inspectable',
  '<p>This design gives researchers an automated starting point and a route to inspect and revise it. A useful cluster is not automatically a biologically validated neuron: waveform quality, parameters and experimental context still matter.</p><p>The public modules credit both Mikel Val Calvo and Javier Alegre-Cortés. No accuracy or generalisation claim is inferred from the presence of the algorithms. The historical application was inspected without running a new neural-recording benchmark.</p>'),
 ('source','Explore the project',resources([('https://github.com/mikelval82/NeuroSorter-Interface','NeuroSorter-Interface','Source, historical interface and usage documentation.'),('project-biotechnology.html','The wider research software portfolio','EEG, physiological acquisition and camera-based experiments.')]))],
 next=('project-neuroprosthesis.html','Horizon Cyber-Vision')),
]
