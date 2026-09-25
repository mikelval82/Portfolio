"""Three capability areas, each connected to concrete work."""

CAPABILITIES = [
 ('service-llm.html', 'Agents & knowledge systems', 'Designing task boundaries, context and data transformations.', 'graph',
  '<p>I design and build systems that connect language models with structured data and knowledge. OntoGenix provides an example from concept through implementation and publication. My personal project HERO explores task contracts, controlled execution and verification in an agent runtime.</p><p>My industry experience also includes contributing to data-agent design during a previous Inditex assignment through TMC.</p>',
  [('Task and context design','Specialised responsibilities, explicit intermediate artifacts and application-controlled workflows.'),('Knowledge engineering','Ontology generation, graph-based integration and mappings between source data and semantic representations.'),('Implementation','Python systems connecting LLM calls, user interaction and executable checks.')],
  [('blog-ontogenix.html#architecture','Follow the OntoGenix architecture','See what each agent receives and produces.'),('project-hero.html#decisions','HERO: contracts and runtime control','Task ownership, execution leases and structural verification.'),('blog-ontogenix.html#decisions','Read the engineering decisions','Specialisation, parsing, error feedback and their limits.')]),
 ('service-research.html', 'System conception & applied research', 'Connecting an application problem with a coherent AI system.', 'voice',
  '<p>I work across problem formulation, high-level architecture, implementation and scientific communication. The scope differs by project: OntoGenix includes implementation; my ASISVIA contribution centres on the generative interview-and-analysis concept.</p><p>At LabLENI I led MindFrameAI and coordinated work across multidisciplinary projects. My research also includes human–robot interaction and participation in neuroengineering teams.</p>',
  [('Problem formulation','Define the interaction, information needs and boundaries of an AI application.'),('Architecture and research coordination','Connect components and disciplinary perspectives, with a clear account of individual and team contributions.'),('Applications','Generative interviews in ASISVIA; immersive training work in THOT; human–robot interaction and neuroprosthetics research.')],
  [('project-asisvia.html','ASISVIA: conception and design','Generative AI for interview management and analysis.'),('blog-ontogenix.html#evaluation','Research results with their conditions','Published team evaluation, protocol and limits.'),('blog-neurosorter.html','Neural signal research software','An additional link to the neuroengineering background.')]),
 ('service-vision.html', 'Biotechnology & neuroengineering', 'Connecting scientific software, physical prototypes and experimental design.', 'signal',
  '<p>My research background combines software engineering, physiological signal processing and multimodal emotion recognition. It includes EEG and camera acquisition tools, collaborative neural-analysis software, and the concept, hardware, software and experiment design for a visual-neuroprosthesis prototype.</p>',
  [('Experimental systems','Prototype concept, hardware and software, and behavioural experiment design in Horizon Cyber-Vision.'),('Acquisition and context','GEERT, MULTI_GEERT, GePHYCAM and BIOSIGNALS: signal acquisition, stream buffers, recording control and event annotations.'),('Neural analysis','Collaborative development of NeuroSorter, connecting waveform cleaning, graph clustering and researcher curation.')],
  [('project-neuroprosthesis.html','Horizon Cyber-Vision','Experimental prototype, contribution and publication.'),('project-biotechnology.html','Research software portfolio','Inspect the distinct EEG, physiology and video workflows.'),('blog-neurosorter.html','NeuroSorter','Neural waveform cleaning, clustering and manual curation.')]),
]

LEGACY_ROUTES = {
    'project-conversational-ai.html': ('project-asisvia.html', 'ASISVIA'),
    'service-vr.html': ('service-research.html#capabilities', 'System conception & applied research'),
    'service-health.html': ('project-asisvia.html', 'ASISVIA'),
    'service-neuroprosthetics.html': ('project-neuroprosthesis.html', 'Horizon Cyber-Vision'),
}
