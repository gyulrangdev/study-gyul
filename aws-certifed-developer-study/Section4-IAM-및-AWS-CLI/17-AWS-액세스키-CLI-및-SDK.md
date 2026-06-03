# 핵심 요약

AWS에 접근하는 세 가지 방법: 관리 콘솔, CLI, SDK에 대한 설명과 각각의 인증 방식에 대한 내용입니다.

# AWS 액세스 방법

## 1. AWS 관리 콘솔

- 웹 인터페이스 기반
- 인증 방식: 사용자 이름/비밀번호 + MFA

## 2. AWS CLI (Command Line Interface)

- 터미널에서 명령어로 AWS 서비스 조작
- 인증 방식: 액세스 키
- 주요 특징:
  - 모든 명령어는 'aws'로 시작
  - AWS 서비스의 API 직접 접근 가능
  - 작업 자동화를 위한 스크립트 개발 가능
  - 오픈소스 (GitHub에서 확인 가능)

## 3. AWS SDK (Software Development Kit)

- 프로그래밍 언어별 라이브러리
- 인증 방식: 액세스 키
- 지원 언어:
  - JavaScript, Python, PHP, .NET
  - Ruby, Java, Go, Node.js, C++
  - Android, iOS (모바일 SDK)
  - IoT 디바이스용 SDK

# 액세스 키

## 특징

- 관리 콘솔에서 생성
- 사용자가 직접 관리
- 구성:
  - 액세스 키 ID (사용자 이름과 유사)
  - 비밀 액세스 키 (비밀번호와 유사)

## 보안 주의사항

- 절대 타인과 공유 금지
- 개인별로 고유한 액세스 키 사용
- 보안상 중요한 자격 증명으로 취급

# 참고 사항

- AWS CLI는 Python SDK(Boto)를 기반으로 구축
- CLI와 SDK는 동일한 액세스 키로 보호
- 관리 콘솔 대신 CLI만 사용하는 사용자도 존재
