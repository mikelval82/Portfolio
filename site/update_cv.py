"""One-off correction of the original two-page portfolio CV.

This is not a general CV generator and is not part of the website build.
Requires PyMuPDF and Windows Calibri only when applying the migration.
"""
import argparse
import hashlib
from pathlib import Path
import tempfile

ORIGINAL_SHA256 = '699b3bfde0325ced94410a153ebf6d4729f04959d7abd27b5bb990fdf41f60b3'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def update_cv(source, output, overwrite=False):
    import pymupdf as pdf

    require(source.resolve() != output.resolve(), 'Preserve the original CV')
    require(not output.exists() or overwrite, 'Output exists; choose another path or pass --overwrite')
    require(hashlib.sha256(source.read_bytes()).hexdigest() == ORIGINAL_SHA256, 'This migration only supports the original two-page CV; source hash does not match')
    doc = pdf.open(source)
    require(len(doc) == 2, 'Expected the original two-page CV')
    page = doc[0]
    original = page.get_text()
    require('Assigned to the Inditex AI Team' in original, 'Unexpected source text')
    font_path = Path('C:/Windows/Fonts/calibri.ttf')
    require(font_path.is_file(), 'Windows Calibri is required for this original layout')
    font = pdf.Font(fontfile=str(font_path))
    colour = tuple(v / 255 for v in (21, 27, 32))

    profile = ('AI consultant and applied researcher with a PhD, an MSc in Advanced AI, and experience spanning '
               'LLM-based agents, retrieval-augmented generation (RAG), knowledge graphs and database integration. '
               'Previously contributed to data-agent design for Inditex and led MindFrameAI at LabLENI. '
               'Combines Python engineering with experimental design, multidisciplinary research and peer-reviewed '
               'publications, including Ontogenix for LLM-driven ontology engineering.')
    contribution = ('Previously contributed to the design of an LLM-based data agent that orchestrates business data '
                     'and enables natural-language queries for executives, commercial teams and marketing stakeholders.')
    lableni_lead = ('Led MindFrameAI research on cognitive architectures, empathetic agents and multi-agent systems; '
                    'coordinated technical work across multidisciplinary projects.')
    asisvia_concept = 'Conceived generative AI for managing interviews and analysing results in ASISVIA.'
    architecture_scope = ('Contributed to concepts and high-level software architecture for agent-based systems '
                          'and immersive training.')

    def wrap(text, size, width):
        lines, line = [], ''
        for word in text.split():
            candidate = (line + ' ' + word).strip()
            if font.text_length(candidate, fontsize=size) > width:
                lines.append(line)
                line = word
            else:
                line = candidate
        if line: lines.append(line)
        return lines

    profile_lines = wrap(profile, 10.56, 494)
    contribution_lines = wrap(contribution, 10.56, 485)
    require(len(profile_lines) <= 5, 'Profile text exceeds its original area')
    require(len(contribution_lines) <= 2, 'Contribution text exceeds its original area')
    lableni_lines = wrap(lableni_lead, 10.56, 485)
    asisvia_lines = wrap(asisvia_concept, 10.56, 485)
    architecture_lines = wrap(architecture_scope, 10.56, 485)
    require(len(lableni_lines) <= 2, 'LabLENI text exceeds its original area')
    require(len(asisvia_lines) == 1, 'ASISVIA text exceeds its original area')
    require(len(architecture_lines) <= 2, 'Architecture text exceeds its original area')
    for rect in [(50,138,548,205),(50,460,545,475),(59,477,548,507),
                 (59,548,548,574),(59,575,548,588),(59,589,548,616)]:
        page.add_redact_annot(pdf.Rect(rect), fill=(1,1,1))
    page.apply_redactions(images=0,graphics=0)
    page.insert_font(fontname='PortfolioCalibri', fontfile=str(font_path))
    for i,line in enumerate(profile_lines):
        page.insert_text((50.4,147.26+i*13.32),line,fontname='PortfolioCalibri',fontsize=10.56,color=colour)
    page.insert_text((50.4,469.99),'TMC People Drive Technology | Previous assignment: Inditex AI Team',fontname='PortfolioCalibri',fontsize=9.96,color=colour)
    for i,line in enumerate(contribution_lines):
        page.insert_text((59.784,488.83+i*13.32),line,fontname='PortfolioCalibri',fontsize=10.56,color=colour)
    for lines, baseline in [(lableni_lines,557.14),(asisvia_lines,584.5),(architecture_lines,598.3)]:
        for i,line in enumerate(lines):
            page.insert_text((59.784,baseline+i*13.32),line,fontname='PortfolioCalibri',fontsize=10.56,color=colour)
    location='Crevillente, Spain'
    page.insert_text((545-font.text_length(location,fontsize=9.48),105.14),location,fontname='PortfolioCalibri',fontsize=9.48,color=colour)
    doc.subset_fonts()
    with tempfile.NamedTemporaryFile(dir=output.parent, suffix='.pdf', delete=False) as pending:
        temporary = Path(pending.name)
    try:
        doc.save(temporary,garbage=4,deflate=True)
        doc.close()
        with pdf.open(temporary) as result:
            updated=' '.join(result[0].get_text().split()).replace('\u2010','-')
            require('Crevillente, Spain' in updated, 'Updated CV text failed verification')
            require('Previous assignment: Inditex AI Team' in updated, 'Updated CV text failed verification')
            require('Assigned to the Inditex AI Team' not in updated, 'Updated CV text failed verification')
            require('Contributes to data-' not in updated, 'Updated CV text failed verification')
            require('Conceived generative AI for managing interviews and analysing results in ASISVIA.' in updated, 'Updated CV text failed verification')
            require('Implemented empathetic virtual assistants' not in updated, 'Updated CV text failed verification')
            require('Developed multiuser XR training simulators' not in updated, 'Updated CV text failed verification')
            require(len(result) == 2, 'Updated CV must retain two pages')
        temporary.replace(output)
    finally:
        if not doc.is_closed:
            doc.close()
        temporary.unlink(missing_ok=True)
    print('Updated downloadable CV; original preserved; two-page layout retained.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='Unmodified original CV; verified by SHA-256')
    parser.add_argument('output', type=Path, help='Separate corrected PDF; never the source path')
    parser.add_argument('--overwrite', action='store_true', help='Allow replacing an existing output PDF')
    args = parser.parse_args()
    try:
        update_cv(args.source, args.output, args.overwrite)
    except (ImportError, OSError, ValueError) as error:
        parser.exit(1, f'CV update failed: {error}\n')


if __name__ == '__main__':
    main()
