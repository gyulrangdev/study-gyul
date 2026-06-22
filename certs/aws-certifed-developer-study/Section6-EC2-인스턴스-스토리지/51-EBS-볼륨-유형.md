# 핵심 요약

EBS 볼륨은 6가지 유형이 있으며, 각각의 성능과 용도에 따라 선택할 수 있습니다.

# EBS 볼륨 유형

## 범용 SSD (GP2/GP3)

### GP3 (최신 세대)

- 기본: 3,000 IOPS, 125MB/s
- 최대: 16,000 IOPS, 1,000MB/s
- IOPS와 처리량 독립적 설정 가능

### GP2 (이전 세대)

- 볼륨 크기와 IOPS 연동
- 최대 16,000 IOPS
- 3,000 IOPS까지 버스트 가능
- 1GB-16TB 크기

## 프로비저닝된 IOPS (IO1/IO2)

### IO1

- 4-16TB 지원
- 최대 64,000 IOPS (Nitro)
- 일반 인스턴스: 32,000 IOPS
- 크기와 IOPS 독립적 설정

### IO2 Block Express

- 최대 64TB
- 서브 밀리초 지연
- 최대 256,000 IOPS
- IOPS:GB = 1000:1

## HDD 볼륨

### ST1 (처리량 최적화)

- 최대 16TB
- 최대 500MB/s
- 최대 500 IOPS
- 빅데이터, 로그 처리용

### SC1 (Cold HDD)

- 최대 16TB
- 최대 250MB/s
- 최대 250 IOPS
- 아카이브 데이터용

# 주요 사용 사례

- 데이터베이스: GP2/GP3, IO1/IO2
- 개발/테스트: GP2/GP3
- 빅데이터: ST1
- 아카이브: SC1

# 부팅 볼륨 지원

- GP2, GP3, IO1, IO2만 지원
- ST1, SC1은 부팅 볼륨 불가

# 성능 고려사항

- 32,000+ IOPS: EC2 Nitro + IO1/IO2 필요
- 비용 효율성: GP2/GP3
- 최고 성능: IO2 Block Express
- 최저 비용: SC1
