---
name: aws-genai-developer-pro
description: AWS Certified Generative AI Developer – Professional (AIP-C01) 학습 가이드. Bedrock 핸즈온 중심 8주 플랜으로 시험을 준비한다. 도메인 비중, 매일 루틴, Boto3 Converse 핸즈온 실행법을 다룬다.
---

# AWS Gen AI Developer (AIP-C01) 학습 스킬

만들면서 배우는 Bedrock 중심 합격 플랜. 강의 시청형이 아니라 핸즈온형.

- 전체 커리큘럼: [`curriculum.md`](curriculum.md)
- Week 1 일차별: [`week-01/README.md`](week-01/README.md)
- 핸즈온 코드: [`code/`](code/)
- Notion 원본: <https://app.notion.com/p/AWS-Gen-AI-Developer-AIP-C01-3877d8322b0481aaa018cd4630c50355>

## 시험 한눈에

- 코드/레벨: AIP-C01 / Professional · 합격 750/1000 · 65+10문항 · 180분 · $300
- 도메인 비중: ① FM 통합·데이터·컴플라이언스 31% · ② 구현·통합 26% · ③ 안전·보안·거버넌스 20% · ④ 운영·최적화 12% · ⑤ 테스트·검증·트러블슈팅 11%
- ①+②=57%가 핵심: Bedrock 모델선택 / RAG(Knowledge Bases) / 프롬프트 / Agents
- 범위 밖: 모델 학습·파인튜닝·고급 ML·피처 엔지니어링

## 8주 흐름

- **Phase 1 (1~2주)** 기반·갭 진단 — 갭 진단 + Bedrock 기본, RAG·벡터스토어
- **Phase 2 (3~5주)** 핵심 구현 — 에이전트, 프롬프트·통합, 보안·거버넌스
- **Phase 3 (6~8주)** 운영·검증·마무리 — 최적화·테스트, 실전 문제, 모의고사

## 매일 루틴

매일 한 토픽을 펼쳐서 진행하고, 끝나면 체크박스를 채운 뒤 GitHub에 커밋.

1. **개념** 30분 — 오늘 토픽의 핵심을 한 문장으로 설명할 수 있게
2. **핸즈온** — 콘솔/코드로 직접 실행 (Day 3부터 `code/` 사용)
3. **체크** — 그날 체크박스 통과 여부 자가평가
4. **산출물 커밋** — 메모/비교표/실험노트를 리포에 남김

> 시험은 "이 서비스가 뭐냐"가 아니라 "이 제약 조건에서 뭘 고를래"를 물음. 항상 비용·성능·보안·거버넌스 4축으로 비교.

## code/ 핸즈온 실행법

```bash
pip install boto3
export AWS_PROFILE=my-profile   # 또는 AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY
python code/converse_api.py "RAG와 파인튜닝의 차이를 3줄로 설명해줘"
```

전제: 해당 리전에서 모델 access 승인 + IAM `bedrock:InvokeModel`. 실험 파라미터(`BEDROCK_TEMPERATURE`, `BEDROCK_MAX_TOKENS` 등)는 [`code/README.md`](code/README.md) 참고.
