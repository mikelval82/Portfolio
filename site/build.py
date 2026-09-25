"""Build the static portfolio with Python's standard library."""
import argparse
from html import escape
from config import ROOT, BASE
from render import artwork, layout, article
from technical_cases import TECHNICAL_CASES
from capabilities import CAPABILITIES, LEGACY_ROUTES
from extended_cases import EXTENDED_CASES

CASES = TECHNICAL_CASES + EXTENDED_CASES

def render_site():
    """Return generated paths and text without changing files on disk."""
    outputs = {}
    home = (ROOT/'site/home.html').read_text(encoding='utf-8')
    for kind in ['graph','voice','signal','runtime']:
        home = home.replace('{{'+kind.upper()+'_ART}}',artwork(kind))
    outputs['index.html'] = layout('Mikel Val Calvo | Research Engineer · Agentic AI & Knowledge Systems', 'Research engineer specialising in agentic AI and knowledge systems. Explore agent engineering, knowledge systems, neuroprosthesis design and scientific software.',home)
    pages = ['index.html']
    for case in CASES:
        outputs[case['path']] = article(case)
        pages.append(case['path'])
    for path,title,deck,art,intro,skills,related in CAPABILITIES:
        skill_body = ''.join(f'<h3>{escape(k)}</h3><p>{escape(v)}</p>' for k,v in skills)
        resources = '<ul class="resource-list">'+''.join(f'<li><a href="{p}">{escape(t)} ↗</a><span>{escape(d)}</span></li>' for p,t,d in related)+'</ul>'
        case = dict(path=path,title=title,deck=deck,eyebrow='Expertise / Applied research & engineering',meta='Experience across research and industry',art=art,role='Explore the relevant projects for contribution and professional context.',sections=[('background','Experience & context',intro),('capabilities','Areas of contribution',skill_body),('projects','Selected work',resources),('contact','Discuss a project','<p>For applied AI opportunities or research collaborations, <a href="index.html#contact">get in touch</a> or <a href="Mikel_Val_Calvo_CV.pdf">read my CV</a>.</p>')],next=related[0][:2])
        outputs[path] = article(case)
        pages.append(path)
    for path, (target, title) in LEGACY_ROUTES.items():
        body = f'<div class="wrap"><header class="article-head"><p class="eyebrow">Explore the work</p><h1>{escape(title)}</h1><p class="article-deck">This content is now part of a focused case or capability page.</p><a class="button" href="{target}">Continue to {escape(title)} →</a></header></div>'
        html = layout(title+' | Mikel Val Calvo', 'Explore the related project and experience.', body, path, noindex=True)
        html = html.replace('</head>', f'<meta http-equiv="refresh" content="0;url={target}"></head>')
        html = html.replace(f'<link rel="canonical" href="{BASE}">', f'<link rel="canonical" href="{BASE+target.split("#")[0]}">')
        outputs[path] = html
    for path in ['blog-single.html','portfolio-single.html']:
        body='<div class="wrap"><header class="article-head"><p class="eyebrow">Research &amp; engineering</p><h1>Explore the work.</h1><p class="article-deck">Selected projects, research software and publications by Mikel Val Calvo.</p><div class="actions"><a class="button" href="index.html#portfolio">View projects ↗</a><a class="button secondary" href="index.html#research">View research ↗</a></div></header></div>'
        outputs[path] = layout('Selected work | Mikel Val Calvo','Explore projects and published research.',body,path,noindex=True)
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+BASE+('' if p=='index.html' else p)+'</loc></url>' for p in pages)+'</urlset>\n'
    outputs['sitemap.xml'] = sitemap
    outputs['robots.txt'] = 'User-agent: *\nAllow: /\nSitemap: '+BASE+'sitemap.xml\n'
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if generated files are missing or stale; do not write files.')
    args = parser.parse_args()
    outputs = render_site()
    if args.check:
        stale = [name for name, content in outputs.items()
                 if not (ROOT/name).is_file() or (ROOT/name).read_text(encoding='utf-8') != content]
        if stale:
            print('Generated files are missing or stale:\n' + '\n'.join(stale))
            print('Run: python site/build.py')
            return 1
        print(f'All {len(outputs)} generated files match their sources.')
    else:
        for name, content in outputs.items():
            (ROOT/name).write_text(content, encoding='utf-8')
        print(f'Built {1 + len(CASES) + len(CAPABILITIES)} portfolio pages, {len(LEGACY_ROUTES)} redirects and 2 legacy entry points.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
