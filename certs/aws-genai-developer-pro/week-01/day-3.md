# Day 3 — Boto3 Converse API

**목표**: 코드로 Bedrock을 호출하고 파라미터를 조절할 수 있다.

**개념** — `bedrock-runtime`의 `converse`가 표준. 핵심 파라미터 temperature·topP·maxTokens. 결정성 필요하면 temperature↓. 출력 토큰=비용·지연.

**핸즈온** — `code/day03_converse.py` 실행 → temperature 0.0/1.0 비교 → maxTokens 줄여 잘리는 지점 확인.

> 실행 가능한 예제는 리포의 [`../code/converse_api.py`](../code/converse_api.py) 참고.

**체크**

- [ ] converse 호출 성공
- [ ] temperature 효과 관찰
- [ ] 출력 파싱 경로(output→message→content) 이해

**산출물**: 코드 + 실행 결과 메모 커밋
