# code/ — 핸즈온 코드

AIP-C01 학습용 실행 가능한 Bedrock 예제.

## converse_api.py

Amazon Bedrock Converse API를 Boto3로 호출하는 첫 핸즈온 (Week 1 / Day 3).

### 1. 설치

```bash
pip install boto3
```

### 2. AWS 자격증명 설정

다음 중 하나. 코드에 키를 하드코딩하지 않는다.

```bash
# 방법 A: 환경변수
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...        # 임시 자격증명일 때만

# 방법 B: 프로파일
export AWS_PROFILE=my-profile
# 또는 `aws configure` 로 ~/.aws/credentials 구성
```

해당 리전에서 **모델 access 승인**과 IAM `bedrock:InvokeModel` 권한이 필요하다.

### 3. (선택) 동작 파라미터

| 환경변수 | 기본값 | 설명 |
| --- | --- | --- |
| `AWS_REGION` | `us-east-1` | Bedrock 리전 |
| `BEDROCK_MODEL_ID` | `anthropic.claude-3-5-sonnet-20240620-v1:0` | 모델 ID |
| `BEDROCK_TEMPERATURE` | `0.5` | 0.0(결정적)~1.0(다양) |
| `BEDROCK_MAX_TOKENS` | `512` | 출력 토큰 상한 (=비용·지연) |

### 4. 실행

```bash
python converse_api.py
python converse_api.py "RAG와 파인튜닝의 차이를 3줄로 설명해줘"
```

### 5. 실험 포인트 (Day 3 체크)

- `BEDROCK_TEMPERATURE=0.0` vs `1.0` 출력 차이 관찰
- `BEDROCK_MAX_TOKENS`를 줄여 응답이 잘리는 지점 확인
- 출력 파싱 경로 `output → message → content[0].text` 이해

종료 코드: `0` 성공 / `1` Bedrock 호출 실패(자격증명·access·권한) / `2` 설정 오류.
