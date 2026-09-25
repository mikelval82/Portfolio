"""Shared page shell, artwork and case-page rendering; no file writes."""
from html import escape
import json
from config import BASE

def artwork(kind):
    if kind == 'graph':
        inside = '''<g stroke="#8a938e" stroke-width="1.4" fill="none"><path d="M70 120L150 60L250 70L310 130L235 180L140 190Z"/><path d="M70 120L190 120L150 60M190 120L250 70M190 120L235 180M190 120L140 190M190 120L310 130"/></g><g fill="#162a39"><circle cx="70" cy="120" r="9"/><circle cx="150" cy="60" r="10"/><circle cx="250" cy="70" r="7"/><circle cx="310" cy="130" r="10"/><circle cx="235" cy="180" r="8"/><circle cx="140" cy="190" r="6"/></g><circle cx="190" cy="120" r="25" fill="#b8823c"/><circle cx="190" cy="120" r="35" fill="none" stroke="#b8823c" opacity=".3"/><text x="190" y="125" text-anchor="middle" font-family="monospace" font-size="12" fill="#fff">OWL</text><g font-family="monospace" font-size="10" fill="#344a52"><text x="30" y="102">dataset</text><text x="125" y="40">entities</text><text x="244" y="52">relations</text><text x="270" y="159">mappings</text></g>'''
    elif kind == 'runtime':
        inside = '''<g fill="none" stroke="#8aa9b4" stroke-width="1.5"><path d="M55 80H165V50H315V190H165V150H55Z"/><path d="M115 115H215M235 115H285"/></g><g font-family="monospace" font-size="10" fill="#c2d3cd"><text x="34" y="32">HERO / EXECUTION CONTRACT</text><text x="43" y="118">task</text><text x="183" y="76">context</text><text x="183" y="171">evidence</text><text x="34" y="224">define → execute → verify</text></g><rect x="165" y="91" width="77" height="46" fill="#eab66b"/><text x="203" y="119" text-anchor="middle" font-family="monospace" font-size="12" fill="#111e30">LEASE</text><circle cx="290" cy="115" r="6" fill="#eab66b"/>'''
    elif kind == 'voice':
        bars = ''.join(f'<rect x="{72+i*10}" y="{122-h/2}" width="3" height="{h}" rx="1.5" fill="{"#eab66b" if 7<i<16 else "#94bdba"}"/>' for i,h in enumerate([12,22,16,42,27,64,40,82,106,65,91,130,85,115,72,98,57,71,31,46,20,29,13,9]))
        inside = f'<path d="M25 122H355" stroke="#50716f" stroke-width=".7"/>{bars}<g fill="#c2d3cd" font-family="monospace" font-size="10"><text x="28" y="35">HUMAN</text><text x="290" y="35">AGENT</text><text x="28" y="219">voice → context → response</text></g><circle cx="346" cy="216" r="4" fill="#eab66b"/>'
    else:
        inside = '''<g stroke="#334b5b" stroke-width=".6"><path d="M0 50H380M0 100H380M0 150H380M0 200H380M50 0V250M100 0V250M150 0V250M200 0V250M250 0V250M300 0V250M350 0V250"/></g><path d="M0 110L28 110L38 99L45 115L53 70L61 144L70 105L81 110L110 110L120 99L129 115L137 60L146 149L157 105L170 110L207 110L217 100L225 116L234 69L242 144L251 105L267 110L300 110L310 99L318 115L326 64L335 146L345 105L357 110H380" fill="none" stroke="#eab66b" stroke-width="2"/><path d="M0 176Q30 166 60 177T120 176T180 178T240 175T300 178T380 176" fill="none" stroke="#83aead" stroke-width="2"/><g font-family="monospace" font-size="10" fill="#b6c1ce"><text x="25" y="32">PHYSIOLOGICAL SIGNALS</text><text x="25" y="225">acquire / synchronise / record</text></g>'''
    return f'<div class="project-art {kind}" aria-hidden="true"><svg viewBox="0 0 380 250" xmlns="http://www.w3.org/2000/svg">{inside}</svg></div>'

def layout(title, description, body, path='index.html', noindex=False):
    home = path == 'index.html'
    prefix = '' if home else 'index.html'
    navigation = ''.join(f'<a href="{prefix}#{anchor}">{label}</a>' for anchor,label in [('portfolio','Work'),('biotechnology','Biotech'),('experience','Experience'),('research','Research')])
    person = json.dumps({'@context':'https://schema.org','@type':'Person','name':'Mikel Val Calvo','url':BASE,'jobTitle':'Research Engineer','sameAs':['https://github.com/mikelval82','https://www.linkedin.com/in/mikel-val-calvo-a2757399/','https://scholar.google.es/citations?user=PoviSYIAAAAJ']})
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#111e30">
<title>{escape(title)}</title><meta name="description" content="{escape(description,quote=True)}"><meta name="author" content="Mikel Val Calvo">
<link rel="canonical" href="{BASE if home or noindex else BASE+path}"><meta property="og:type" content="{'website' if home else 'article'}"><meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:url" content="{BASE if home else BASE+path}"><meta property="og:image" content="{BASE}images/about/9.jpg"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{escape(title,quote=True)}"><meta name="twitter:description" content="{escape(description,quote=True)}"><meta name="twitter:image" content="{BASE}images/about/9.jpg">
{'<meta name="robots" content="noindex">' if noindex else ''}<link rel="icon" type="image/svg+xml" href="images/favicon.svg"><link rel="stylesheet" href="css/portfolio.css"><script src="js/portfolio.js" defer></script>
<script type="application/ld+json">{person}</script></head><body id="top"><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap nav-wrap"><a class="brand" href="index.html" aria-label="Mikel Val Calvo, home">Mikel Val Calvo<span> / PhD</span></a><button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false">Menu +</button><nav id="site-nav" class="site-nav" aria-label="Main navigation">{navigation}<a class="nav-contact" href="{prefix}#contact">Let's talk <span aria-hidden="true">↗</span></a></nav></div></header>
<main id="main">{body}</main><footer class="site-footer"><div class="wrap footer-row"><p>© 2026 Mikel Val Calvo · Research &amp; engineering</p><a href="#top">Back to top ↑</a></div></footer></body></html>'''

def section(id, title, content):
    return f'<section id="{id}"><h2>{title}</h2>{content}</section>'

def article(case):
    toc = ''.join(f'<a href="#{id}">{escape(title)}</a>' for id,title,_ in case['sections'])
    sections = ''.join(section(*s) for s in case['sections'])
    next_path,next_title = case['next']
    cover = case.get('cover') or f'<div class="case-art">{artwork(case["art"])}</div>'
    body = f'''<div class="wrap"><header class="article-head"><a class="back-link" href="index.html#portfolio">← Back to selected work</a><p class="eyebrow">{case['eyebrow']}</p><h1>{escape(case['title'])}</h1><p class="article-deck">{case['deck']}</p><div class="article-meta">{case['meta']}</div></header>{cover}<div class="article-layout"><aside class="article-aside"><div class="aside-label">My role</div><p>{case['role']}</p><nav aria-label="On this page">{toc}</nav></aside><article class="prose">{sections}<a class="next-project" href="{next_path}"><div><small>Continue exploring</small><strong>{escape(next_title)}</strong></div><span aria-hidden="true">↗</span></a></article></div></div>'''
    return layout(case['title']+' | Mikel Val Calvo',case['deck'],body,case['path'])
