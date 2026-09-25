"""Check generated routes, assets, fragments, basic semantics and CV integrity."""
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
from config import ROOT
from build import render_site

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.refs, self.labels, self.fields = path, [], [], [], []
        self.h1, self.lang, self.main = 0, None, 0
        self.errors = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        if tag == 'label': self.labels.append(a.get('for'))
        if tag in ('input', 'textarea') and a.get('type') not in ('hidden','submit'):
            self.fields.append(a.get('id'))
        if tag == 'img' and 'alt' not in a: self.errors.append('Image missing alt text')
        if tag == 'meta' and a.get('http-equiv','').lower() == 'refresh':
            content = a.get('content','')
            if ';url=' in content:
                self.refs.append((tag,'redirect',content.split(';url=',1)[1]))
            else:
                self.errors.append('Invalid redirect destination')
        for attr in ['href','src','action']:
            if a.get(attr): self.refs.append((tag,attr,a[attr]))

def main():
    pages={p.name:Page(p) for p in ROOT.glob('*.html')}
    errors=[]
    expected = {name for name in render_site() if name.endswith('.html')}
    errors.extend('Missing generated page: '+name for name in sorted(expected - pages.keys()))
    errors.extend('Unexpected HTML page: '+name for name in sorted(pages.keys() - expected))
    references=0
    for name,p in pages.items():
        local=list(p.errors)
        if p.lang != 'en': local.append('Missing English document language')
        if p.h1 != 1: local.append(f'Expected one H1; found {p.h1}')
        if p.main != 1: local.append('Expected one main landmark')
        if len(p.ids)!=len(set(p.ids)): local.append('Duplicate IDs')
        if any(not field or field not in p.labels for field in p.fields): local.append('Unlabelled form field')
        for tag,attr,ref in p.refs:
            u=urlsplit(ref)
            if u.scheme or u.netloc:
                if u.scheme=='http' and attr=='src': local.append(f'Mixed-content resource {ref}')
                continue
            target=(ROOT/unquote(u.path)) if u.path else p.path
            references+=1
            if not target.exists(): local.append(f'Missing local target {ref}')
            elif u.fragment and target.suffix=='.html':
                destination=pages.get(target.name)
                if destination and unquote(u.fragment) not in destination.ids: local.append(f'Missing fragment {ref}')
        errors.extend(name+': '+e for e in local)
    cv=ROOT/'Mikel_Val_Calvo_CV.pdf'
    cv_bytes = cv.read_bytes() if cv.is_file() else b''
    if not cv_bytes.startswith(b'%PDF-'): errors.append('Missing or invalid CV PDF')
    print(json.dumps({'pages':len(pages),'local_references_checked':references,'cv_sha256':hashlib.sha256(cv_bytes).hexdigest() if cv_bytes else None,'errors':errors},indent=2))
    raise SystemExit(bool(errors))

if __name__=='__main__': main()
