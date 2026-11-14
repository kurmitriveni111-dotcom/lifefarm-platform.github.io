#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
required=['index.html','editor.html','legal.html','content/articles.json','content/gallery.json','assets/js/site.js','assets/js/editor.js','assets/css/editor.css','sw.js','manifest.webmanifest','.github/workflows/pages.yml','vercel.json']
errors=[]
for x in required:
 if not (root/x).is_file(): errors.append('Missing '+x)
for x in ['content/articles.json','content/gallery.json','manifest.webmanifest','vercel.json']:
 try: json.loads((root/x).read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'Invalid JSON {x}: {e}')
# Verify local href/src references in HTML (ignore external, mailto, anchors, and markdown links)
for f in root.glob('*.html'):
 s=f.read_text(encoding='utf-8')
 for val in re.findall(r"(?:href|src)=[\"']([^\"']+)[\"']",s):
  if val.startswith(('http:','https:','mailto:','#','data:','javascript:')): continue
  target=(f.parent/val.split('#')[0].split('?')[0]).resolve()
  if val.split('#')[0].split('?')[0] and not target.exists(): errors.append(f'Broken local link in {f.name}: {val}')
# Ensure no server-service requirements remain
for f in [root/'index.html',root/'assets/js/site.js',root/'editor.html',root/'assets/js/editor.js']:
 s=f.read_text(encoding='utf-8').lower()
 for term in ['database_url','github_client_secret','smtp_pass','private_blob_read_write_token','/api/auth/','/api/cms/']:
  if term in s: errors.append(f'Unexpected backend dependency {term} in {f.relative_to(root)}')
if errors:
 print('FAIL');print('\n'.join(errors));sys.exit(1)
print('PASS: required files present')
print('PASS: JSON files valid')
print('PASS: HTML local links resolve')
print('PASS: static edition has no listed backend credential/API dependency')
print("NOTE: live deployment and browser interaction tests require the owner account/device.")
