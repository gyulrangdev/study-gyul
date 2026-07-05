# study-gyul

개인 공부 기록과 실습 코드를 도메인별로 모아둔 저장소입니다.

## 폴더별 학습 내용

### `ai/`

- [`ai/2025-langchain-rag/`](ai/2025-langchain-rag/): LangChain RAG 스터디 기록입니다. RAG 개념, 파인튜닝과의 차이, LangChain 구성 요소, 프롬프트 템플릿, Output Parser, RAG 구현 흐름을 정리했습니다.
- [`ai/ai-engineering-from-scratch-study/`](ai/ai-engineering-from-scratch-study/): AI Engineering From Scratch 기반 스터디입니다. 개발 환경 설정, 행렬 변환, 확률과 분포 등 AI 엔지니어링 기초를 주차별로 정리합니다.
- [`ai/deep-ml/`](ai/deep-ml/): Deep-ML 문제 풀이와 개념 연습 공간입니다. 행렬 전치, 단일 뉴런 역전파, 기본 autograd, MSE 기반 경사하강법 변형, Adam Optimizer를 NumPy와 PyTorch로 학습합니다.
- [`ai/gpt-playground/`](ai/gpt-playground/): OpenAI API 호출과 GPT 기반 시스템 설계 어시스턴트 실험 코드가 있습니다.
- [`ai/llm_study/`](ai/llm_study/): 『LLM을 활용한 실전 AI 애플리케이션 개발』 책 기반 스터디입니다. LLM 개념, Hugging Face 토크나이저, attention mask, padding 등을 정리했습니다.
- [`ai/prompt-cursor-rules/`](ai/prompt-cursor-rules/): Cursor rules와 프롬프트 자동화 실험, MCP(Model Context Protocol) 개념 번역 정리를 담았습니다.

### `frontend/`

- [`frontend/2024-modern-react-deep-dive-study/`](frontend/2024-modern-react-deep-dive-study/): 『모던 리액트 Deep Dive』 2024 스터디입니다. React 핵심 개념, 훅, 렌더링, 상태 관리, Next.js, 성능과 보안 주제를 정리했습니다.
- [`frontend/2024-msmrh-study/`](frontend/2024-msmrh-study/): 『리액트 훅을 활용한 마이크로 상태 관리』 스터디입니다. `useState`, `useReducer`, Context, 구독 패턴, Zustand, Jotai, Valtio, React Tracked를 학습했습니다.
- [`frontend/React-Deep-Dive-2025/`](frontend/React-Deep-Dive-2025/): 『모던 리액트 Deep Dive』 2025 스터디입니다. React 핵심 요소, 훅, SSR, 상태 관리, React 17/18 변경 사항, Next.js 13, 웹 지표, 성능 측정, 보안을 다뤘습니다.
- [`frontend/blog/`](frontend/blog/): React 공식 문서 스터디 회고를 정리한 글입니다. React 19 신규 API, Server Components, Server Actions, 동시성 렌더링, AI 도구를 활용한 학습 방식을 기록했습니다.
- [`frontend/onebite-react/`](frontend/onebite-react/): 한입 크기로 잘라 먹는 React 학습 실습 코드입니다. JavaScript와 React 기초 예제를 섹션별로 작성했습니다.
- [`frontend/seo_study/`](frontend/seo_study/): SEO 마스터 클래스 학습 기록입니다. 키워드 리서치, 온페이지 SEO, Google Search Console, URL 구조, 국제 SEO, 백링크, 사이트 속도, 이미지 SEO, 리치 스니펫, SEO 감사 체크리스트를 정리했습니다.
- [`frontend/turing-frontend-test/`](frontend/turing-frontend-test/): 테스트와 함께 프론트엔드 개발하기 실습 코드입니다. Next.js, Vitest browser mode, Testing Library, 접근성 기반 테스트, React Cosmos, PandaCSS, Ariakit 기반 컴포넌트 테스트를 다룹니다.

### `backend/`

- [`backend/study-hexagonal-developer/`](backend/study-hexagonal-developer/): 개발자 기본기와 백엔드 설계 관점의 학습 기록입니다. 구현 기술 학습법, 소프트웨어 가치와 비용, 코드 이해, 응집도와 결합도, 리팩터링, 테스트, 아키텍처와 패턴, 업무 관리, 글쓰기와 발표를 정리했습니다.

### `cs/`

- [`cs/algorithm-2024/`](cs/algorithm-2024/): 이진 트리 중심의 알고리즘 문제 풀이 기록입니다. 트리의 최대 깊이, 직경, 동일 값 경로 등을 정리했습니다.
- [`cs/gyul-algorithm-study/`](cs/gyul-algorithm-study/): TypeScript 기반 알고리즘 풀이 저장소입니다. 문자열, 배열, 투 포인터, 이진 탐색, 이진 트리, 정렬, 집합, DP, 그래프 탐색과 백트래킹을 연습했습니다.
- [`cs/study-multi-paradigm-programming/`](cs/study-multi-paradigm-programming/): 『멀티패러다임 프로그래밍』 스터디입니다. 객체지향, 함수형, 명령형 패러다임, 타입 시스템, LISP, Generator/Iterator, 비동기 프로그래밍을 학습합니다.
- [`cs/study-the-missing-readme/`](cs/study-the-missing-readme/): 『필독! 개발자 온보딩 가이드』 스터디입니다. 개발자 성장, 자기주도 학습, 레거시 코드와 기술 부채, 운영 환경을 고려한 코드 작성, 방어적 프로그래밍, 로깅을 정리했습니다.

### `certs/`

- [`certs/aws-certifed-developer-study/`](certs/aws-certifed-developer-study/): AWS Developer 자격증 준비 기록입니다. IAM, AWS CLI/SDK, MFA, IAM 역할과 보안 도구, 공동 책임 모델, EC2 스토리지(EBS, AMI, EFS), ELB/ASG, 오답노트를 정리했습니다.
- [`certs/aws-genai-developer-pro/`](certs/aws-genai-developer-pro/): AWS Certified Generative AI Developer - Professional(AIP-C01) 준비 자료입니다. Bedrock, Knowledge Bases, RAG, Agents, Guardrails, 모델 평가, 비용 최적화, 보안과 거버넌스를 8주 커리큘럼으로 정리했습니다.

### `scripts/`

- [`scripts/publish_deep_ml.sh`](scripts/publish_deep_ml.sh): Deep-ML 문제 폴더를 정리한 뒤 커밋하고 원격 저장소에 올리는 보조 스크립트입니다.

## Deep-ML 정리 방식

Deep-ML 문제는 [`ai/deep-ml/problems/`](ai/deep-ml/problems/) 아래에 문제별 폴더로 정리합니다. 각 문제 폴더에는 다음 흐름을 유지합니다.

- 문제를 짧게 다시 설명한 노트
- NumPy로 먼저 확인하는 워밍업 코드
- PyTorch로 같은 개념을 연결해보는 시도
- 사용자가 직접 푼 뒤에만 추가하는 최종 제출 코드

문제 폴더를 업데이트한 뒤에는 필요할 때 `scripts/publish_deep_ml.sh`를 사용해 Deep-ML 기록을 커밋하고 푸시합니다.
