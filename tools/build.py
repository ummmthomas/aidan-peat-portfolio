#!/usr/bin/env python3
"""Rebuild the site's HTML files from the editable sources in site-src/.

    python3 tools/build.py          # write every route's .html file
    python3 tools/build.py --check  # exit 1 if any .html file is out of date

The live site is a Cargo export: every page is the same HTML shell with all
site content in one JSON blob (window.__PRELOADED_STATE__), which Cargo's
script (assets/cargo/index.js) renders in the browser. That blob is repeated
in every .html file, so it is not edited by hand. Instead:

  site-src/state.json    the Cargo state. A string "@site-src/<path>" is
                         replaced with that file's contents (one trailing
                         newline dropped), so page bodies live in
                         site-src/pages/<purl>.html and the stylesheet in
                         site-src/site.css.
  site-src/pages/*.html  page bodies, in Cargo's HTML (<media-item hash=...>,
                         <gallery-columnized>, <column-set> ...).
  site-src/routes.json   one entry per .html file: <title>, description and
                         share image.
  site-src/shell.html    the HTML shell, with {{TITLE}}, {{META}},
                         {{SITE_CSS}} and {{STATE}} slots.

Homepage and Colbert hub cards lead with a metric pulled from the linked page's impact stats
(<div class="impact-stat" data-value data-label>): the first filled-in stat
marked data-headline="true", else the first filled-in stat. A card whose page
has only [[METRIC]] placeholders shows that placeholder, highlighted, with
its label.

A page in state.json can be written short: {"id", "title", "purl",
"@template": "<id of an existing page>"} copies that page's settings (layout
CSS, overlay behaviour) under the new id. Each page's media library is
completed from the hashes its body uses, so a new <media-item hash=...> only
needs the image to exist somewhere in the site already.
"""
import copy, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'site-src')


def read(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        text = f.read()
    return text[:-1] if text.endswith('\n') else text


def resolve_files(node):
    if isinstance(node, dict):
        return {k: resolve_files(v) for k, v in node.items()}
    if isinstance(node, list):
        return [resolve_files(v) for v in node]
    if isinstance(node, str) and node.startswith('@site-src/'):
        return read(node[1:])
    return node


def expand_templates(state):
    pages = state['pages']['byId']
    for pid, page in list(pages.items()):
        base_id = page.pop('@template', None)
        if not base_id:
            continue
        base = copy.deepcopy(pages[base_id])
        base['local_css'] = (base.get('local_css') or '').replace(f'"{base_id}"', f'"{pid}"')
        base.update({'media': [], 'thumb_media_id': None, 'thumbnail': None,
                     'thumb_meta': {'hide_from_index': True}})
        base.update(page)
        pages[pid] = base


def complete_media(state):
    catalog = {}
    for page in state['pages']['byId'].values():
        for m in page.get('media') or []:
            catalog.setdefault(m['hash'], m)
    for page in state['pages']['byId'].values():
        have = {m['hash'] for m in page.get('media') or []}
        for h in re.findall(r'hash="([A-Za-z0-9]+)"', page.get('content') or ''):
            if h in have:
                continue
            if h not in catalog:
                sys.exit(f"build: page '{page['purl']}' uses hash {h}, which no page's media library has")
            page.setdefault('media', []).append(catalog[h])
            have.add(h)


STAT = re.compile(r'<div class="impact-stat" data-value="([^"]*)" data-label="([^"]*)"( data-headline="true")?>')
CARD = re.compile(r'(<media-item [^>]*href="([^"]+)"[^>]*>)(<figcaption class="caption" slot="caption">)')


def headline_metrics(state):
    pages = state['pages']['byId'].values()
    metrics = {}
    for page in pages:
        stats = [(v, l, bool(h)) for v, l, h in STAT.findall(page.get('content') or '')]
        # Filled-in before placeholder, then data-headline first.
        stats.sort(key=lambda s: (s[0].startswith('[['), not s[2]))
        if stats:
            metrics[page['purl']] = stats[0][:2]
    for page in pages:
        if page['purl'] not in ('homepage', 'pc-project'):
            continue
        def card(m):
            metric = metrics.get(m.group(2))
            if not metric:
                return m.group(0)
            value, label = metric
            # A placeholder shows as a highlighted dummy number until it is filled in.
            value = f'<b class="ph">{value}</b>' if value.startswith('[[') else f'<b>{value}</b>'
            return f'{m.group(1)}{m.group(3)}<span class="card-metric">{value} {label}</span><br />'
        page['content'] = CARD.sub(card, page['content'])


def check_structure(state):
    pages = state['pages']['byId']
    order = state['structure']['byParent']['root']
    for pid in order:
        if pid not in pages:
            sys.exit(f'build: structure lists page {pid}, which is not in pages.byId')
    for pid in pages:
        if pid not in order:
            sys.exit(f'build: page {pid} is missing from structure.byParent.root')
    state['structure']['bySort'] = {pid: i for i, pid in enumerate(order)}
    index = state['structure']['indexById']
    state['structure']['indexById'] = {pid: index.get(pid) for pid in order}


def serialize_state(state):
    # Same encoding as Cargo's export, so an unchanged state builds to identical bytes.
    out = json.dumps(state, ensure_ascii=False, separators=(',', ':'))
    return out.replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')


def attr(value):
    return html.escape(value, quote=True).replace('&#x27;', "'")


def meta_block(route):
    title, desc, image = route['og_title'], route['description'], route['image']
    lines = [
        f'<meta name="description" content="{attr(desc)}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{attr(title)}">',
        f'<meta name="twitter:description" content="{attr(desc)}">',
        f'<meta name="twitter:image" content="{attr(image)}">',
        f'<meta property="og:title" content="{attr(title)}">',
        f'<meta property="og:description" content="{attr(desc)}">',
        f'<meta property="og:url" content="{attr(route["url"])}">',
        f'<meta property="og:image" content="{attr(image)}">',
        '<meta property="og:type" content="website">',
    ]
    return '\n'.join('\t\t' + line for line in lines)


def build():
    state = resolve_files(json.loads(read('site-src/state.json')))
    expand_templates(state)
    check_structure(state)
    complete_media(state)
    headline_metrics(state)
    shell = read('site-src/shell.html') + '\n'
    state_js = serialize_state(state)
    routes = json.loads(read('site-src/routes.json'))['routes']
    files = {}
    for route in routes:
        page = (shell.replace('{{TITLE}}', html.escape(route['title'], quote=False))
                     .replace('{{META}}', meta_block(route))
                     .replace('{{SITE_CSS}}', state['css']['stylesheet'])
                     .replace('{{STATE}}', state_js))
        files[route['file']] = page
    return files


def main():
    check = '--check' in sys.argv
    stale = []
    for name, text in build().items():
        path = os.path.join(ROOT, name)
        old = open(path, encoding='utf-8').read() if os.path.exists(path) else None
        if old == text:
            continue
        stale.append(name)
        if not check:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
    if check:
        if stale:
            print('Out of date (run python3 tools/build.py):', ', '.join(stale))
            sys.exit(1)
        print('All pages up to date.')
    else:
        print('Wrote ' + (', '.join(stale) if stale else 'nothing (already up to date)'))


if __name__ == '__main__':
    main()
