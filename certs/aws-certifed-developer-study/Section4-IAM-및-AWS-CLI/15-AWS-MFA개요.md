# 핵심 요약

AWS IAM의 보안 메커니즘인 비밀번호 정책과 MFA(Multi-Factor Authentication)에 대한 상세 설명입니다.

# 비밀번호 정책

## 주요 설정 옵션

- 최소 비밀번호 길이 설정
- 문자 유형 요구사항 설정
  - 대문자
  - 소문자
  - 숫자
  - 특수문자
- 사용자의 비밀번호 변경 권한 설정
- 비밀번호 만료 기간 설정
- 비밀번호 재사용 방지 설정

# MFA (Multi-Factor Authentication)

## MFA 개념

- 알고 있는 것(비밀번호)과 소유한 것(보안 장치)의 조합
- 단순 비밀번호보다 높은 보안성 제공
- 비밀번호가 유출되어도 물리적 장치 없이는 접근 불가

## MFA 장치 종류

### 가상 MFA 장치

- Google Authenticator 등의 인증 앱 사용
- 하나의 장치에서 여러 계정 관리 가능
- 루트 계정, IAM 사용자 모두에 사용 가능

### 물리적 보안 키

- U2F(Universal Second Factor) 보안 키
  - Yubikey (타사 제품)
  - 하나의 키로 여러 계정 지원

### 하드웨어 보안 토큰

- Gemalto 제공 하드웨어 토큰
- SurePassID 토큰 (AWS GovCloud용)

# 보안 권장사항

- 루트 계정과 모든 IAM 사용자에 MFA 활성화 권장
- 강력한 비밀번호 정책 설정
- 정기적인 비밀번호 변경 요구
