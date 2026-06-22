# AWS Gen AI Developer (AIP-C01) — 커리큘럼

> Notion 원본: [AWS Gen AI Developer (AIP-C01)](https://app.notion.com/p/AWS-Gen-AI-Developer-AIP-C01-3877d8322b0481aaa018cd4630c50355)

> 목표: AWS Certified Generative AI Developer – Professional (AIP-C01) 합격. 핵심은 **Bedrock 핸즈온**. 강의 시청형이 아니라 만들면서 배우는 플랜.

## 📋 시험 한눈에

| 항목 | 내용 |
| --- | --- |
| 코드 / 레벨 | AIP-C01 / Professional |
| 문항 | 채점 65 + 비채점 10 (객관식·복수응답), 180분 |
| 합격 | 100~1000 척도, **750점** 이상 |
| 응시료 | $300 USD (재응시 50% 바우처) |
| 유효기간 | 3년 |
| 권장 학습량 | 80~120시간 / 6~8주 |
| 범위 밖 | 모델 학습·훈련, 고급 ML, 데이터·피처 엔지니어링 |

## 📊 도메인 가중치 (시간 배분 기준)

| 도메인 | 비중 |
| --- | --- |
| 1. FM 통합·데이터 관리·컴플라이언스 | **31%** |
| 2. 구현·통합 | **26%** |
| 3. AI 안전·보안·거버넌스 | **20%** |
| 4. 운영 효율·최적화 | **12%** |
| 5. 테스트·검증·트러블슈팅 | **11%** |

도메인 1+2 = **57%**. Bedrock 모델선택 / RAG(Knowledge Bases) / 프롬프트 / Agents에 집중.

---

## ✅ 8주 체크리스트

### Phase 1 — 기반·갭 진단 (1~2주차)

**1주차 — 갭 진단 + Bedrock 기본**

- [ ] 공식 Exam Guide(PDF) 정독, 약점 도메인 표시
- [ ] Skill Builder 공식 Practice Question Set으로 베이스라인 점수 측정
- [ ] Bedrock 콘솔에서 FM 직접 호출 (Playground)
- [ ] Boto3 `converse` API로 모델 호출 코드 1개 작성 (아래 자료 참고)
- [ ] 진단 점수 기록 → 40% 미만이면 SA Associate 선행 검토

**2주차 — RAG·벡터스토어 (도메인 1)**

- [ ] Bedrock Knowledge Bases + OpenSearch Serverless로 RAG 1개 구축
- [ ] Titan / 임베딩 모델로 청킹·임베딩 직접 실험
- [ ] LangGraph로 짜던 RAG를 AWS 네이티브로 재구현
- [ ] 하이브리드 검색 / 리랭킹 / 쿼리 변환 개념 정리

### Phase 2 — 핵심 구현 (3~5주차)

**3주차 — 에이전트 (도메인 2)**

- [ ] Bedrock Agents / AgentCore로 action group 에이전트 1개 구축
- [ ] Step Functions·Lambda로 오케스트레이션 실습
- [ ] "비결정적(LLM/에이전트) vs 결정적(Lambda·Step Functions) 분기" 기준 정리
- [ ] HITL(휴먼 인 더 루프) 승인 패턴 구현

**4주차 — 프롬프트·통합 (도메인 2)**

- [ ] Prompt management / 스트리밍 / 멀티모달 실습
- [ ] API Gateway + Lambda로 FM 엔드포인트 노출
- [ ] 멀티 에이전트 패턴 학습 (출제 비중 높음)
- [ ] AppConfig로 동적 모델 전환 패턴 이해

**5주차 — 보안·거버넌스 (도메인 3)**

- [ ] Bedrock Guardrails 설정 (콘텐츠 필터·민감정보 마스킹)
- [ ] IAM 최소권한 / KMS / VPC·PrivateLink로 데이터 경계 설계
- [ ] Responsible AI, 감사 로그, 데이터 거주성 정리
- [ ] Cross-Region Inference로 복원력 패턴 이해

### Phase 3 — 운영·검증·마무리 (6~8주차)

**6주차 — 최적화·테스트 (도메인 4·5)**

- [ ] 비용 최적화: 모델 선택·프롬프트 캐싱·배치 추론
- [ ] CloudWatch 관측·로깅 설정
- [ ] Bedrock Model Evaluation 잡 실행 (품질·책임성 메트릭)
- [ ] 트러블슈팅 시나리오 5개 정리

**7주차 — 실전 문제**

- [ ] 공식 Pretest 응시 → 오답 도메인 재학습
- [ ] SimuLearn 핸즈온 랩 반복
- [ ] 약점 도메인 집중 보강

**8주차 — 모의고사·약점 보강**

- [ ] 모의고사 2회 (목표 75~85% 안정화)
- [ ] 오답 노트 최종 복습
- [ ] 85% 안정 시 실제 시험 예약

---

## 📚 바로 시작 자료

### 🟢 오늘 할 일 (Day 1, ~2시간)

1. Exam Guide PDF 다운로드 후 도메인 5개 task/skill 훑기
2. Bedrock 콘솔 → Model access에서 Claude·Titan 모델 활성화 요청
3. Playground에서 같은 프롬프트를 모델별로 비교
4. 아래 Boto3 코드 실행해서 첫 API 호출 성공시키기

### 🧠 핵심 개념 30분 정리

- **Amazon Bedrock**: 여러 FM(Claude, Titan 등)을 단일 API로 호출하는 매니지드 서비스. 시험의 중심.
- **Knowledge Bases**: RAG를 매니지드로 제공. 데이터 소스 → 청킹 → 임베딩 → 벡터스토어 → 검색을 자동화.
- **OpenSearch Serverless**: 대표 벡터스토어. 시맨틱·하이브리드 검색.
- **Bedrock Agents / AgentCore**: 도구 호출·오케스트레이션. LangGraph의 AWS 네이티브 대응물.
- **Guardrails**: 콘텐츠 필터·PII 마스킹·금지 주제. 거버넌스 핵심.
- **Model Evaluation**: FM 품질·책임성 자동/사람 평가.

### 🔄 내가 아는 것 → AWS 등가물 매핑

| 익숙한 OSS / 개념 | AWS 네이티브 (시험 출제) |
| --- | --- |
| LangGraph 그래프·노드 | Bedrock Agents + Step Functions |
| LangChain RAG 파이프라인 | Bedrock Knowledge Bases |
| 직접 띄운 벡터DB (Chroma 등) | OpenSearch Serverless 벡터검색 |
| 임베딩 모델 직접 호출 | Amazon Titan Embeddings |
| HITL 인터럽트 노드 | Agent + Lambda 승인 단계 |
| MCP 툴 호출 | Agent action groups (스키마 검증) |
| 프롬프트 템플릿 파일 | Bedrock Prompt Management |
| 모델 폴백 로직 | Cross-Region Inference + Step Functions |

> 매주 "OSS로 알던 것 ↔ AWS 등가물" 노트를 늘려가면 시나리오 문제에서 속도가 붙음.

### 💻 첫 핸즈온 — Boto3 Converse API

```python
import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.converse(
    modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
    messages=[
        {"role": "user", "content": [{"text": "RAG와 파인튜닝의 차이를 3줄로 설명해줘"}]}
    ],
    inferenceConfig={"maxTokens": 512, "temperature": 0.5},
)

print(response["output"]["message"]["content"][0]["text"])
```

실행 전: AWS CLI 자격증명 설정 + 해당 리전에서 모델 access 승인 필요. temperature·maxTokens를 바꿔가며 출력 차이를 관찰할 것 (도메인 4 출제 포인트).

> 실행 가능한 버전은 [`code/converse_api.py`](code/converse_api.py) 참고.

### 🎯 "트레이드오프"로 외울 주제 (암기 X, 판단 O)

- RAG: 시맨틱 청킹 / 임베딩 / 하이브리드 검색 / 리랭킹 / 쿼리 변환
- 에이전트: 오케스트레이션 / 도구 사용 / 스키마 검증 / HITL 승인
- 보안: Guardrails / 최소권한 / 감사 로그 / 데이터 경계
- 비용·성능: 모델 선택 / 토큰 최적화 / 배치 추론 / 캐싱
- 복원력: Cross-Region Inference / Step Functions 서킷브레이커

> 시험은 "이 서비스가 뭐냐"가 아니라 "이 제약 조건에서 뭘 고를래"를 물음. 항상 비용·성능·보안·거버넌스 4축으로 비교.

---

## 🔗 공식 리소스

- 시험 소개 페이지: <https://aws.amazon.com/certification/certified-generative-ai-developer-professional/>
- Exam Guide (HTML): <https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html>
- Exam Guide (PDF, task/skill 상세): <https://docs.aws.amazon.com/pdfs/aws-certification/latest/ai-professional-01/ai-professional-01.pdf>
- Skill Builder Exam Prep Plan: <https://skillbuilder.aws/category/exam-prep/generative-ai-developer-professional-AIP-C01>
- 공식 Practice Question Set: <https://skillbuilder.aws/learn/HSEKTD11NX/official-practice-question-set-aws-certified--generative-ai-developer--professional-aipc01--english/ZDANP82P4V>

---

## ⚠️ 놓치기 쉬운 포인트

- **선결 자격증**: 필수는 아니지만 Professional 레벨. AWS 자격증이 하나도 없고 1주차 진단이 40% 미만이면 SA Associate 선행 검토.
- **에이전트 비중 과소평가 금지**: 후기 공통 함정. 도메인 2를 RAG보다 가볍게 보지 말 것.
- **"LangGraph로 안다"가 함정**: 개념은 같아도 시험은 Bedrock 네이티브 동작·제약을 물음.
- **범위 밖에 시간 쓰지 말 것**: 모델 학습·파인튜닝·피처 엔지니어링은 출제 대상 아님.
