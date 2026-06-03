# 핵심 요약

IAM 정책의 구조와 상속 방식, 정책 적용 방법에 대한 상세 설명입니다.

# IAM 정책 적용 방식

## 그룹 정책

- 그룹 레벨에서 정책 연결 가능
- 그룹의 모든 구성원에게 정책이 상속됨
- 서로 다른 그룹은 다른 정책 적용 가능

## 인라인 정책

- 개별 사용자에게 직접 연결되는 정책
- 그룹 소속 여부와 관계없이 적용 가능
- 특정 사용자에게만 적용되는 고유한 권한 부여 시 사용

## 다중 정책 상속

- 한 사용자가 여러 그룹에 속한 경우, 모든 그룹의 정책을 상속
- 예: 개발자 그룹과 감사팀 그룹에 속한 사용자는 두 그룹의 정책 모두 적용

# IAM 정책 구조

## 필수 요소

- Version: 정책 언어의 버전 (일반적으로 "2012-10-17")
- Statement: 권한을 정의하는 주요 요소들의 집합

## Statement 구성 요소

### 필수 요소

- Effect: 권한의 허용/거부 여부 ("Allow" 또는 "Deny")
- Action: 허용/거부되는 API 호출 목록
- Resource: 정책이 적용되는 AWS 리소스 목록

### 선택적 요소

- Sid: Statement 식별자
- Principal: 정책이 적용되는 대상 (사용자, 계정, 역할)
- Condition: 정책 적용 조건

# 시험 준비 포인트

- Effect, Principal, Action, Resource에 대한 깊은 이해 필요
- 정책의 상속 구조 이해
- JSON 형식의 정책 문서 구조 파악

```json
{
  "Version": "2012-10-17",
  "Id": "S3PolicyId1", // 선택사항
  "Statement": [
    {
      "Sid": "Statement1", // 선택사항
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root"
      },
      "Action": ["s3:GetObject", "s3:PutObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::mybucket/*", "arn:aws:s3:::mybucket"],
      "Condition": {
        // 선택사항
        "StringEquals": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}
```

# 주요 구성 요소 설명

## 필수 요소

- `Version`: 정책 언어 버전 (보통 "2012-10-17" 사용)
- `Statement`: 권한 설정의 핵심 요소

## Statement 내부 요소

### 필수 항목

- `Effect`: "Allow" 또는 "Deny"로 권한 허용/거부 설정
- `Action`: AWS 서비스의 API 작업 목록
- `Resource`: 정책이 적용될 AWS 리소스의 ARN

### 선택 항목

- `Id`: 정책 식별자
- `Sid`: Statement 식별자
- `Principal`: 정책 적용 대상(사용자/역할/계정)
- `Condition`: 정책 적용 조건 (IP 주소, 시간 등)

## 예시 설명

- 위 정책은 특정 AWS 계정(123456789012)에게
- mybucket이라는 S3 버킷에 대해
- GetObject, PutObject, ListBucket 권한을 허용
- 203.0.113.0/24 IP 대역에서만 접근 가능하도록 설정
