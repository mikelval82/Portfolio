"""Reusable HTML components independent of individual project content."""
from html import escape

def source(path, label, base):
    return f'<a href="{base}{path}">{escape(label)} ↗</a>'

def flow(label, steps, caption, control=''):
    nodes = ''.join(f'<li><span class="flow-index">{i:02}</span><strong>{escape(name)}</strong><span>{escape(detail)}</span></li>' for i,(name,detail) in enumerate(steps,1))
    lead = f'<div class="flow-control">{control}</div>' if control else ''
    return f'<figure class="flow-diagram" aria-label="{escape(label)}">{lead}<ol class="flow-path">{nodes}</ol><figcaption>{caption}</figcaption></figure>'

def summary(items):
    return '<dl class="case-summary">'+''.join(f'<div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>' for k,v in items)+'</dl>'
