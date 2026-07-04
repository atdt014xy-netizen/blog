# Claude Code 리서치 요약

## 1. 연구 목적
Claude Code가 무엇인지, 어떤 기능을 제공하는지, 그리고 블로그나 콘텐츠 작성에 바로 활용할 수 있는 핵심 포인트를 공식 문서와 저장소 기준으로 정리한다.

## 2. 확인한 출처
다음 공식 자료를 기준으로 정리했다.

1. Anthropic 공식 문서: Claude Code Overview
   - https://code.claude.com/docs/en/overview
2. Anthropic 공식 문서: Common Workflows
   - https://code.claude.com/docs/en/common-workflows
3. Anthropic 공식 문서: Setup
   - https://code.claude.com/docs/en/setup
4. Anthropic 공식 문서: Memory
   - https://code.claude.com/docs/en/memory
5. Anthropic 공식 문서: Hooks reference
   - https://code.claude.com/docs/en/hooks
6. Anthropic 공식 문서: Sub-agents
   - https://code.claude.com/docs/en/sub-agents
7. Anthropic 공식 GitHub 저장소
   - https://github.com/anthropics/claude-code

## 3. Claude Code의 핵심 기능 5가지

### 1) 코드베이스 탐색과 이해를 돕는 AI 엔지니어링 도구
공식 문서는 Claude Code를 “agentic coding tool”로 설명하며, 코드베이스를 읽고, 파일을 수정하고, 명령을 실행하고, git 워크플로우를 다루는 데 적합하다고 명시한다.

- 코드 구조를 파악하고 관련 파일을 탐색하는 흐름이 가능하다.
- 버그 수정, 리팩터링, 테스트 작성 같은 일반적인 개발 작업을 자연어로 지시할 수 있다.
- 공식 문서의 common workflows 섹션에서도 “understand a codebase”, “fix bugs”, “refactor”, “write tests” 같은 사용 사례가 제시된다.

### 2) 터미널과 CLI 작업을 직접 수행하는 개발 보조 도구
Claude Code는 터미널에서 직접 동작하는 도구로 소개된다. 따라서 코드 편집뿐 아니라 명령 실행, 테스트, 배포 관련 작업까지 한 흐름으로 처리할 수 있다.

- 터미널 기반 작업이 가능하다.
- git 관련 작업, worktree 사용, 스크립트나 CI와의 연동 같은 실무 시나리오가 문서에 포함되어 있다.
- 공식 문서에는 Windows, macOS, Linux, WSL 등 다양한 환경 지원이 명시되어 있다.

### 3) 파일 편집과 반복적 개발 작업을 자동화할 수 있는 기능
공식 문서와 저장소는 Claude Code가 파일을 직접 수정하고, 반복적 개발 작업을 처리하는 데 유용하다고 설명한다.

- 코드 수정, 문서 작성, 테스트 작성, 리팩터링 등 여러 작업을 하나의 세션 안에서 처리할 수 있다.
- “common workflows” 페이지에서는 버그 수정, 문서 작업, PR 생성 같은 실제 작업 흐름이 제시된다.
- 이 기능은 단순한 챗봇형 질의응답이 아니라, 개발 작업의 실행 단계까지 연결하는 도구로 이해할 수 있다.

### 4) 프로젝트 지식과 지시사항을 지속적으로 기억하는 메모리 기능
Claude Code는 CLAUDE.md 파일과 auto memory를 통해 프로젝트별 지시사항과 기억을 유지할 수 있다.

- CLAUDE.md 파일은 프로젝트, 사용자, 조직 단위의 지시사항을 저장하는 방식이다.
- auto memory는 Claude Code가 반복적인 작업에서 패턴이나 선호도를 기억하도록 돕는다.
- 공식 문서에서는 “project instructions”, “build commands”, “coding standards” 등을 지속적으로 반영하는 방식으로 설명한다.

### 5) 훅과 서브에이전트로 확장성을 높이는 구조
Claude Code는 기본 기능 외에도 훅(hooks)과 서브에이전트(subagents)를 지원한다.

- 훅은 특정 이벤트에 맞춰 자동화를 연결할 수 있는 기능이다. 예를 들어 도구 사용 전후, 세션 시작/종료, 파일 변경 이벤트 등에 반응하도록 구성할 수 있다.
- 서브에이전트는 특정 작업에 특화된 에이전트를 분리해 실행할 수 있다. 공식 문서는 탐색용 Explore, 계획용 Plan, 범용 작업용 general-purpose 같은 내장 에이전트를 설명한다.
- 이 구조는 단일 세션에서 복잡한 작업을 나누어 처리하는 데 유리하다.

## 4. 추가로 확인된 실무 포인트

### 설치와 접근성
- 공식 문서에는 native install, Homebrew, WinGet, npm, apt/dnf/apk 등 다양한 설치 방법이 소개되어 있다.
- Windows, macOS, Linux, WSL을 모두 지원한다.
- 설치 후 `claude` 명령으로 실행할 수 있다.

### 인증과 사용 조건
- 공식 문서에 따르면 Claude Code는 Pro, Max, Team, Enterprise, Console 계정이 필요하다.
- 무료 Claude.ai 플랜은 Claude Code 접근이 포함되지 않는다고 명시되어 있다.

### 보안 및 개인정보 관련 정보
- 공식 GitHub 저장소 페이지에는 데이터 수집, 개인정보 처리, 플러그인/도구와의 연동 방식에 대한 정보가 포함되어 있다.
- 이 자료는 기능 설명과 함께 보안·개인정보 관점도 함께 확인할 수 있게 해 준다.

## 5. 정리
Claude Code는 단순한 코드 생성 도구가 아니라, 코드 탐색, 명령 실행, 파일 수정, 프로젝트 기억, 자동화 확장까지 연결하는 개발용 에이전트 도구로 이해할 수 있다.

특히 다음 세 가지가 핵심 포인트로 보인다.

- 코드 작업을 자연어로 지시하고 실행까지 연결한다.
- 터미널 기반 작업과 git/테스트/스크립트 흐름을 지원한다.
- 메모리, 훅, 서브에이전트로 확장 가능한 구조를 갖는다.
