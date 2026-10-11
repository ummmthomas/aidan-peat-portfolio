#!/usr/bin/env python3
"""Preview the site locally: python3 serve.py [port]  ->  http://localhost:8000

Like `python3 -m http.server`, but /about also serves about.html, matching
how the live site's URLs look (the Cargo front end routes on the path).
"""
import http.server, os, sys

class Handler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.path.split('?', 1)[0].split('#', 1)[0].rstrip('/')
        if path and '.' not in os.path.basename(path) and os.path.isfile(self.translate_path(path + '.html')):
            self.path = path + '.html'
        return super().send_head()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print(f'Serving on http://localhost:{port}')
http.server.ThreadingHTTPServer(('', port), Handler).serve_forever()
