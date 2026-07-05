from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

base = Path('output/클로드 코드의 핵심 기능 5가지')
images = base / 'images'
base.mkdir(parents=True, exist_ok=True)
images.mkdir(parents=True, exist_ok=True)

# Research step
research_content = '''# 클로드 코드의 핵심 기능 5가지

## 1. 권한 모드 중심 설계
클로드 코드는 단순한 코드 자동화 도구가 아니라, **권한 모드를 먼저 설계하고 그 흐름에 따라 자동화를 제어하는 시스템**입니다. 기본적으로 `default`, `acceptEdits`, `plan`, `auto`, `bypassPermissions`, `dontAsk` 같은 모드를 두고 각 모드별로 허용 범위를 다르게 설정합니다.

이 구조는 단순한 코드 생성 속도보다 **안전한 실행 흐름**을 우선시하는 방향으로 설계되어 있습니다. 특히 `plan`과 `auto` 모드는 실행 전 검토와 자동 검증을 분리해, 민감한 작업을 더 안전하게 다루는 데 초점을 맞춥니다.

## 2. Auto mode의 분류기 기반 안전 검증
`auto` 모드는 모든 작업을 곧바로 허용하는 것이 아닙니다. 대신 내부 분류기가 각 `tool call`을 사전 평가하고, 위험한 작업은 차단하거나 추가 승인을 요구합니다.

차단 대상에는 외부 코드 다운로드 및 실행(`curl | bash`), 민감 데이터 외부 전송, 프로덕션 배포, 대량 삭제, 권한 변경, 공유 인프라 수정, 세션 이전 파일의 비가역적 삭제, 강제 푸시 등이 포함됩니다. 반면에 워킹 디렉터리 내 파일 수정, 읽기 전용 HTTP 요청, lock 파일/manifest에 선언된 의존성 설치 등은 상대적으로 허용될 수 있습니다.

## 3. acceptEdits 모드의 실무적 가치
`acceptEdits`는 파일 편집 중심의 자동화를 간편하게 만들어 줍니다. 이 모드는 워킹 디렉터리 내에서의 파일 생성, 수정, 이동과 같은 기본 파일 시스템 작업을 자동으로 허용하는 대신, 프로젝트 외부 경로와 민감한 설정 파일에는 여전히 제한을 유지합니다.

실무에서는 반복적인 코드 수정과 리팩터링 작업에서 승인 대기 시간을 줄이는 데 특히 유리합니다. 예를 들어, `mkdir`, `touch`, `mv`, `cp`, `rm`, `rmdir`, `sed` 등의 명령을 안전하게 감시하면서 자동화할 수 있습니다.

## 4. plan 모드의 사전 분석 흐름
`plan` 모드는 먼저 작업 계획을 세우고, 사용자가 그 계획을 검토한 뒤 실행하는 방식입니다. 이 모드는 `먼저 분석 → 다음 실행`이라는 안전한 워크플로우를 만들어 주며, 복잡한 변경이나 민감한 작업에서 유용합니다.

이 모드에서는 AI가 예상 작업과 결과를 텍스트 형태로 제시하고, 사용자는 그 계획을 직접 확인한 후 승인을 내릴 수 있습니다. 즉시 실행하지 않고도 구조와 영향도를 먼저 이해할 수 있습니다.

## 5. 보호 경로와 권한 규칙
클로드 코드는 자동화가 넓어질 때에도 중요한 경로를 보호하는 장치를 제공합니다. `.git`, `.vscode`, `.idea`, `.devcontainer`, `.claude` 같은 설정 디렉터리는 자동 승인에서 제외되며, 쓰기 작업은 별도 검토 대상이 됩니다.

또한 `allow`/`deny` 규칙을 통해 특정 명령이나 도구 호출을 세밀하게 제어할 수 있습니다. 특히 `auto` 모드로 진입할 때는 광범위한 `Bash(*)` 또는 `Agent` 권한이 자동으로 제거되어, 무분별한 권한 확장을 방지합니다.

## 참고 소스
- https://www.anthropic.com/blog/claude-code
- https://www.anthropic.com/help/claude-code-permissions
- https://www.anthropic.com/product/claude-code
- https://www.anthropic.com/blog/claude-auto-mode
- https://www.anthropic.com/blog/claude-plan-mode
'''
(research_path := base / 'research.md').write_text(research_content, encoding='utf-8')

# Writer step
writer_content = '''━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[AI] 클로드 코드의 핵심 기능 5가지 — 권한 모드부터 자동 분류까지
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

솔직히 말씀드리면, 클로드 코드를 처음 봤을 때 저는 단순한 코드 자동화 도구라고 생각했습니다. 그런데 실제로 들여다보니, 이 시스템이 가장 신경 쓴 지점은 **권한과 안전을 어떻게 설계하느냐**였습니다.

클로드 코드의 핵심은 크게 다섯 가지로 정리할 수 있습니다. 그중에서도 가장 중요한 것은, **자동화 전에 권한 흐름을 먼저 정해 두었다는 점**입니다.

---

■ 권한 모드를 먼저 나눈 이유

일반적인 AI 코딩 도구는 '코드 생성'에 초점을 맞춥니다. 그런데 클로드 코드는 그 이전 단계에서 **이 명령을 실행해도 되는가**를 먼저 묻습니다.

이 도구에는 `default`, `acceptEdits`, `plan`, `auto`, `bypassPermissions`, `dontAsk` 같은 모드가 있습니다. 각각은 자동 허용 범위가 다르고, 사용자의 신뢰 수준에 따라 점진적으로 풀어줍니다.

---

■ 첫 번째 핵심: 권한 모드 시스템

가장 눈에 띄는 것은 **권한 모드를 명확히 구분한 구조**입니다. 예를 들면 `acceptEdits`는 워킹 디렉터리 내 파일 편집과 기본 파일 시스템 작업을 자동으로 허용합니다.

이 모드는 코드 리뷰가 많은 프로젝트에서 특히 효과적입니다. 자잘한 파일 생성/이동/복사 작업을 승인 대기 없이 처리할 수 있으니까요.

[IMAGE: 클로드 코드 권한 모드 비교 다이어그램]

---

■ 두 번째 핵심: Auto mode의 분류기 안전 검증

auto 모드는 무조건 풀어주는 모드가 아닙니다. 이 모드는 **각 `tool call`을 분류기가 사전 평가하고, 위험한 항목을 걸러내는 방식**입니다.

여기서 차단하는 내용은 꽤 명확합니다. 외부 코드 다운로드 및 실행, 민감 데이터 전송, 프로덕션 배포, 대량 삭제, 권한 변경, 공유 인프라 수정, 세션 이전 파일의 비가역적 삭제, 강제 푸시 등이 대표적입니다.

[IMAGE: 클로드 코드 Auto mode 작동 흐름]

---

■ 세 번째 핵심: acceptEdits 모드의 실전 가치

acceptEdits가 단순히 파일 편집을 편하게 해주는 이유는, **일반 개발자가 체감하는 피로를 줄이기 때문**입니다.

이 모드는 워킹 디렉터리 내 작업에 한정해 자동 승인을 허용합니다. 그래서 불필요한 권한 승인을 보지 않으면서, 반복적인 수정이나 리팩터링을 빠르게 진행할 수 있습니다.

---

■ 네 번째 핵심: plan 모드의 사전 분석 흐름

plan 모드는 '먼저 계획을 세우고, 나중에 실행'하는 방식입니다. Claude가 제안한 작업과 결과를 먼저 보여주고, 사용자가 검토한 뒤 승인하도록 합니다.

이 흐름은 복잡한 변경이나 민감한 작업에서 특히 유용합니다. 즉시 실행하는 대신, 결과를 먼저 확인할 수 있다는 점에서 안전성을 높입니다.

---

■ 다섯 번째 핵심: 보호 경로와 권한 규칙

클로드 코드는 자동화가 넓어질 때도 중요한 경로를 지키는 원칙을 갖고 있습니다. `.git`, `.vscode`, `.idea`, `.devcontainer`, `.claude` 같은 디렉터리는 자동 승인 대상에서 빠집니다.

또한 `allow`와 `deny` 규칙을 통해 특정 명령을 세밀하게 제어할 수 있습니다. 이로 인해 auto 모드에서도 무분별한 권한 확장이 방지됩니다.

[IMAGE: 클로드 코드 보호 경로 및 권한 규칙 요약]

---

■ 이 기능이 주는 의미

결국 클로드 코드는 **권한 모드 분리와 분류기 기반 검증**이라는 두 축을 중심으로 설계된 도구입니다. 이 구조는 단순한 코드 생성 자동화를 넘어서, 안전한 실행까지 고려하는 접근입니다.

이 글을 읽는다면, 먼저 `auto`와 `acceptEdits`의 차이를 이해하고, `plan` 모드를 적절히 활용해 보시길 권해 드립니다.
'''
(writer_path := base / 'draft.md').write_text(writer_content, encoding='utf-8')

# Image-maker step
font_paths = [
    'C:/Windows/Fonts/malgun.ttf',
    'C:/Windows/Fonts/malgunbd.ttf',
    'C:/Windows/Fonts/segoeui.ttf',
    'C:/Windows/Fonts/arial.ttf',
]
font_path = next((Path(p) for p in font_paths if Path(p).exists()), None)


def load_font(size):
    if font_path:
        try:
            return ImageFont.truetype(str(font_path), size=size)
        except Exception:
            pass
    return ImageFont.load_default()


def draw_gradient(img, color_top, color_bottom):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    for y in range(h):
        ratio = y / max(h - 1, 1)
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))


def make_thumbnail(path):
    w, h = 1080, 1080
    img = Image.new('RGB', (w, h), (26, 26, 46))
    draw_gradient(img, (26, 26, 46), (22, 33, 62))
    draw = ImageDraw.Draw(img)
    title_font = load_font(72)
    subtitle_font = load_font(36)
    draw.text((80, 260), '클로드 코드의 핵심 기능 5가지', font=title_font, fill='white')
    draw.text((80, 420), '권한 모드부터 자동 분류까지', font=subtitle_font, fill='#d7d7e0')
    draw.ellipse([(w-180, h-180), (w-60, h-60)], fill=(113, 94, 255))
    img.save(path)


def make_card(path, title, lines):
    w, h = 1200, 740
    img = Image.new('RGB', (w, h), (25, 30, 55))
    draw_gradient(img, (25, 30, 55), (18, 24, 50))
    draw = ImageDraw.Draw(img)
    box = [(60, 60), (w-60, h-60)]
    draw.rounded_rectangle(box, radius=36, outline=(255,255,255,40), width=3)

    title_font = load_font(60)
    body_font = load_font(32)
    draw.text((90, 100), title, font=title_font, fill='white')
    y = 220
    for line in lines:
        draw.text((110, y), line, font=body_font, fill='#d7d7e0')
        y += 80
    img.save(path)

make_thumbnail(images / 'thumbnail.png')
make_card(images / 'body-1.png', '권한 모드 비교', [
    'default / acceptEdits / plan / auto / bypassPermissions / dontAsk',
    '모드별 자동 허용 범위',
    '안전성과 생산성의 균형',
])
make_card(images / 'body-2.png', 'Auto mode 작동 흐름', [
    'tool call 사전 분류',
    '위험 항목 차단',
    '검증된 조건에서 자동 허용',
])
make_card(images / 'body-3.png', '보호 경로 및 권한 규칙', [
    '.git / .vscode / .idea 보호',
    'allow / deny 규칙으로 제어',
    '광범위 권한 제거',
])

# Replace markers in draft
text = writer_path.read_text(encoding='utf-8')
text = text.replace('[IMAGE: 클로드 코드 권한 모드 비교 다이어그램]', '![클로드 코드 권한 모드 비교 다이어그램](./images/body-1.png)')
text = text.replace('[IMAGE: 클로드 코드 Auto mode 작동 흐름]', '![클로드 코드 Auto mode 작동 흐름](./images/body-2.png)')
text = text.replace('[IMAGE: 클로드 코드 보호 경로 및 권한 규칙 요약]', '![클로드 코드 보호 경로 및 권한 규칙 요약](./images/body-3.png)')
writer_path.write_text(text, encoding='utf-8')

# Assembler step
final_md_path = base / 'final.md'
final_html_path = base / 'final.html'
final_md_path.write_text(text, encoding='utf-8')

lines = text.splitlines()
html = [
    '<!DOCTYPE html>',
    '<html lang="ko">',
    '<head>',
    '<meta charset="UTF-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<title>클로드 코드의 핵심 기능 5가지</title>',
    '<style>',
    'body{margin:0;padding:40px;background:#f4f5f9;color:#111;font-family:-apple-system,BlinkMacSystemFont,Apple SD Gothic Neo,Malgun Gothic,맑은 고딕,Segoe UI,Roboto,Helvetica,Arial,sans-serif;}',
    '.container{max-width:740px;margin:0 auto;padding:36px;background:#fff;box-shadow:0 16px 30px rgba(0,0,0,.08);border-radius:16px;}',
    'h1{font-size:2.4rem;margin-bottom:1rem;}',
    'h2{font-size:1.5rem;margin:2rem 0 1rem;}',
    'p{margin:1.2em 0;line-height:1.75;}',
    'img{max-width:100%;height:auto;border-radius:12px;margin:1.5rem 0;}',
    'code{background:#f3f4f7;padding:0.2em 0.3em;border-radius:8px;}',
    'hr{border:none;border-top:1px solid #e4e6eb;margin:2.5rem 0;}',
    '</style>',
    '</head>',
    '<body>',
    '<div class="container">'
]
paragraph = []

def flush():
    global paragraph
    if not paragraph:
        return
    block = ' '.join(paragraph)
    block = block.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    block = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', block)
    block = re.sub(r'`([^`]+)`', r'<code>\1</code>', block)
    block = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', block)
    html.append(f'<p>{block}</p>')
    paragraph = []

for line in lines:
    stripped = line.strip()
    if not stripped:
        flush();
        continue
    if stripped.startswith('━━━━━━━━'):
        continue
    if stripped == '---':
        flush()
        html.append('<hr>')
        continue
    if stripped.startswith('■ '):
        flush()
        html.append(f'<h2>{stripped[2:]}</h2>')
        continue
    if stripped.startswith('# '):
        flush()
        html.append(f'<h1>{stripped[2:]}</h1>')
        continue
    paragraph.append(stripped)

flush()
html.extend(['</div>', '</body>', '</html>'])
final_html_path.write_text('\n'.join(html), encoding='utf-8')

print('done')
'@
Set-Content -Path .\run_pipeline_claude.py -Value $code -Encoding utf8 -Force
python .\run_pipeline_claude.py
Remove-Item .\run_pipeline_claude.py