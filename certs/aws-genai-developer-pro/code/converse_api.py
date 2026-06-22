"""첫 핸즈온 — Amazon Bedrock Converse API (Boto3).

커리큘럼 "💻 첫 핸즈온 — Boto3 Converse API" 기반 실행 가능 버전.

자격증명·리전·모델·파라미터는 모두 환경변수로 읽는다 (하드코딩 금지).
- AWS 자격증명: 표준 boto3 체인 (환경변수 AWS_ACCESS_KEY_ID /
  AWS_SECRET_ACCESS_KEY / AWS_SESSION_TOKEN, 또는 ~/.aws/credentials,
  AWS_PROFILE). 이 스크립트는 별도로 키를 읽거나 저장하지 않는다.
- AWS_REGION:  기본 us-east-1
- BEDROCK_MODEL_ID: 기본 anthropic.claude-3-5-sonnet-20240620-v1:0
- BEDROCK_TEMPERATURE: 기본 0.5
- BEDROCK_MAX_TOKENS: 기본 512

실행 전제: 해당 리전에서 모델 access 승인 + IAM bedrock:InvokeModel 권한.

사용법:
    python converse_api.py "RAG와 파인튜닝의 차이를 3줄로 설명해줘"
인자 없이 실행하면 기본 프롬프트를 사용한다.
"""

from __future__ import annotations

import os
import sys

import boto3
from botocore.exceptions import BotoCoreError, ClientError

DEFAULT_REGION = "us-east-1"
DEFAULT_MODEL_ID = "anthropic.claude-3-5-sonnet-20240620-v1:0"
DEFAULT_PROMPT = "RAG와 파인튜닝의 차이를 3줄로 설명해줘"


def _read_float_env(name: str, default: float) -> float:
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return float(raw)
    except ValueError:
        raise ValueError(f"환경변수 {name} 값을 float로 변환할 수 없습니다: {raw!r}")


def _read_int_env(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return int(raw)
    except ValueError:
        raise ValueError(f"환경변수 {name} 값을 int로 변환할 수 없습니다: {raw!r}")


def run_converse(prompt: str) -> str:
    """Bedrock Converse API를 한 번 호출하고 응답 텍스트를 반환한다."""
    region = os.environ.get("AWS_REGION", DEFAULT_REGION)
    model_id = os.environ.get("BEDROCK_MODEL_ID", DEFAULT_MODEL_ID)
    temperature = _read_float_env("BEDROCK_TEMPERATURE", 0.5)
    max_tokens = _read_int_env("BEDROCK_MAX_TOKENS", 512)

    client = boto3.client("bedrock-runtime", region_name=region)

    response = client.converse(
        modelId=model_id,
        messages=[
            {"role": "user", "content": [{"text": prompt}]},
        ],
        inferenceConfig={"maxTokens": max_tokens, "temperature": temperature},
    )

    return response["output"]["message"]["content"][0]["text"]


def main() -> int:
    prompt = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PROMPT

    try:
        text = run_converse(prompt)
    except ValueError as error:
        print(f"설정 오류: {error}", file=sys.stderr)
        return 2
    except (ClientError, BotoCoreError) as error:
        # 자격증명 미설정, 모델 access 미승인, 권한 부족 등이 여기로 들어온다.
        print(f"Bedrock 호출 실패: {error}", file=sys.stderr)
        print(
            "확인: AWS 자격증명 설정 / 해당 리전 모델 access 승인 / "
            "bedrock:InvokeModel 권한.",
            file=sys.stderr,
        )
        return 1

    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
