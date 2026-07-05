from pathlib import Path
import re

base = Path('output/클로드 코드의 핵심 기능 5가지')
draft = base / 'draft.md'
final_md = base / 'final.md'
final_html = base / 'final.html'
text = draft.read_text(encoding='utf-8')
final_md.write_text(text, encoding='utf-8')

lines = text.splitlines()
html_lines = [
    '<!DOCTYPE html>',
    '<html lang="ko">',
    '<head>',
    '<meta charset="UTF-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<title>클로드 코드의 핵심 기능 5가지</title>',
    '<style>',
    'body{margin:0;padding:40px;background:#f4f5f9;color:#111;font-family:-apple-system,BlinkMacSystemFont,Apple SD Gothic Neo,Malgun Gothic,맑은 고딕,Segoe UI,Roboto,Helvetica,Arial,sans-serif;line-height:1.75;}',
    '.container{max-width:720px;margin:0 auto;background:#fff;padding:36px 40px;box-shadow:0 16px 30px rgba(0,0,0,.08);border-radius:16px;}',
    'h1{font-size:2.4rem;margin-bottom:1rem;line-height:1.15;color:#111;}',
    'h2{font-size:1.55rem;margin:2.4rem 0 1rem;line-height:1.3;color:#111;}',
    'p{margin:1.2em 0;color:#333;font-size:1rem;}',
    'code{background:#f3f4f7;color:#111;padding:0.18em 0.32em;border-radius:8px;white-space:pre-wrap;font-size:0.96em;}',
    'strong{font-weight:700;}',
    'img{max-width:100%;height:auto;border-radius:12px;margin:1.5rem 0;}',
    'hr{border:none;border-top:1px solid #e4e6eb;margin:2.5rem 0;}',
    '.placeholder{background:#eef1fb;color:#2a3c6b;border-radius:14px;padding:18px;margin:1.8rem 0;text-align:center;font-size:0.95rem;border:1px dashed #c9d2ea;}',
    '</style>',
    '</head>',
    '<body>',
    '<div class="container">'
]
paragraph = []

def flush_para():
    global paragraph
    if not paragraph:
        return
    block = ' '.join(paragraph).strip()
    if not block:
        paragraph = []
        return
    block = block.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    block = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', block)
    block = re.sub(r'`([^`]+)`', r'<code>\1</code>', block)
    block = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', block)
    html_lines.append(f'<p>{block}</p>')
    paragraph = []

for line in lines:
    stripped = line.strip()
    if not stripped:
        flush_para()
        continue
    if stripped.startswith('━━━━━━━━'):
        continue
    if stripped == '---':
        flush_para()
        html_lines.append('<hr>')
        continue
    if stripped.startswith('■ '):
        flush_para()
        html_lines.append(f'<h2>{stripped[2:]}</h2>')
        continue
    if stripped.startswith('# '):
        flush_para()
        html_lines.append(f'<h1>{stripped[2:]}</h1>')
        continue
    paragraph.append(stripped)

flush_para()
html_lines.extend(['</div>', '</body>', '</html>'])
final_html.write_text('\n'.join(html_lines), encoding='utf-8')
print('created', final_md, final_html)
