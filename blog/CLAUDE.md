# CLAUDE

이 프로젝트는 블로그 글 작성 자동화 시스템입니다.
메인 에이전트는 직접 리서치나 글쓰기를 하지 않고, 서브 에이전트들을 호출해 작업을 분배하는 오케스트레이터 역할을 합니다.

## 폴더 구조
- `agents/`: 각 단계별 에이전트 정의
- `guides/`: 이미지, 스타일, SEO 등 보조 가이드
- `output/`: 주제별 리서치, 드래프트, 이미지, 최종 결과물

## 작업 단계
1. `agents/researcher.md`를 따라 리서치 실행
   - 결과는 `output/[주제]/research.md`에 저장
2. `agents/writer.md`를 따라 글 작성
   - 결과는 `output/[주제]/draft.md`에 저장
3. `agents/image-maker.md`를 따라 이미지 생성
   - `draft.md`의 `[IMAGE: ...]` 마커를 실제 경로로 치환
4. `agents/assembler.md`를 따라 통합
   - 최종 결과는 `output/[주제]/final.md`와 `output/[주제]/final.html`

## 진행 지침
- 각 단계가 끝날 때마다 사용자에게 현재 상태를 간단히 알립니다.
- 메인 에이전트는 절대 직접 글을 쓰거나 리서치를 수행하지 않습니다.
- 모든 작성/생성 작업은 서브 에이전트에게 위임합니다.
