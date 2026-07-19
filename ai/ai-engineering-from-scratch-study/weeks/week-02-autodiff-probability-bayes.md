# 2주차 - Chain Rule & Autodiff · Probability · Bayes' Theorem

> 건너뛰었던 05·06·07강을 한 번에 정리하는 노트. (원래 진도 중 놓친 부분 보충)

## 기본 정보

- 일정: 일요일 오후 9시
- 장소: 온라인
- 메인 자료:
  - [05. Chain Rule & Automatic Differentiation](https://aiengineeringfromscratch.com/lesson.html?path=phases/01-math-foundations/05-chain-rule-and-autodiff)
  - [06. Probability and Distributions](https://aiengineeringfromscratch.com/lesson.html?path=phases/01-math-foundations/06-probability-and-distributions)
  - [07. Bayes' Theorem](https://aiengineeringfromscratch.com/lesson.html?path=phases/01-math-foundations/07-bayes-theorem)
- 진도: Phase 1 - Lesson 05, 06, 07
- 상태: 진행

## 이번 주 목표

- 연쇄 법칙 → 역전파를 잇고, 값을 감싸 그래프를 기록하는 **미니 autograd 엔진**을 직접 만든다.
- Bernoulli·categorical·normal·Poisson의 PMF/PDF를 구현하고 기댓값·분산·중심극한정리를 설명한다.
- 수치 안정 softmax(최댓값 빼기)와 log 확률이 왜 필요한지 안다.
- 베이즈 정리로 사후확률을 계산하고, 나이브 베이즈 분류기를 처음부터 만든다. MLE vs MAP와 L2 정칙화의 관계를 안다.

## 읽고 정리할 범위

- Lesson 05: 연쇄 법칙, 계산 그래프, forward/reverse mode, Value 클래스, 위상정렬 backward, XOR MLP, 그래디언트 체킹
- Lesson 06: 확률 공리, 조건부확률/독립, PMF vs PDF, 주요 분포, 기댓값/분산, 결합/주변 분포, CLT, log 확률, softmax, 샘플링
- Lesson 07: 베이즈 정리 4요소, 의료검사/스팸 예제, 나이브 베이즈, 라플라스 스무딩, MLE/MAP, 켤레 사전분포, 순차 베이즈 갱신, A/B 테스트

---

## 핵심 개념 1: Chain Rule & Autodiff (Lesson 05)

> 한 줄 요약: 연쇄 법칙은 학습하는 모든 신경망의 엔진이다. autodiff는 그 연쇄 법칙을 임의의 함수 합성에 자동으로 적용한다.

### 연쇄 법칙

- `y = f(g(x))` → `dy/dx = f'(g(x)) · g'(x)`. 사슬을 따라 국소 미분을 곱한다.
- 예: `y = sin(x²)` → `dy/dx = cos(x²)·2x`. 신경망의 각 층이 이 사슬의 한 고리.

### 계산 그래프 · forward/reverse mode

- 연산 = 노드. 값은 앞으로 흐르고(forward), 그래디언트는 뒤로 흐른다(backward).
- **Forward mode**: 입력에서 시작, `dx/dx=1` 전파. 입력 적고 출력 많을 때 유리.
- **Reverse mode**: 출력에서 시작, `dy/dy=1` 전파. **입력 많고 출력 적을 때** 유리.
- 신경망은 입력(가중치)이 수백만, 출력(손실)이 하나 → **reverse mode = 역전파**. 한 번의 backward로 모든 그래디언트.

| 모드 | 시드 | 방향 | 유리한 경우 |
| --- | --- | --- | --- |
| Forward | `dx_i/dx_i = 1` | 입력→출력 | 입력 소, 출력 다 |
| Reverse | `dy/dy = 1` | 출력→입력 | 입력 다, 출력 소 (신경망) |

### autograd 엔진의 3요소

1. **값 감싸기**: 모든 수를 `data`와 `grad`를 가진 객체로 래핑.
2. **그래프 기록**: 연산마다 입력과 국소 그래디언트 함수(클로저)를 기록.
3. **backward**: 그래프를 위상정렬 → 역순으로 순회하며 각 노드에서 연쇄 법칙 적용.
   - 핵심: `grad += ...` (한 값이 여러 연산에 쓰이면 그래디언트는 **더해진다** = gradient accumulation).

→ 이게 PyTorch `autograd`가 하는 일. `requires_grad=True`면 연산을 기록하고 `.backward()`로 계산. 그래프는 매 forward마다 새로 만드는 **동적 그래프(define-by-run)** 라서 if/for 제어문을 모델 안에 쓸 수 있다.

### 그래디언트 체킹

- autodiff 그래디언트를 수치 미분 `(f(x+h)-f(x-h))/(2h)` 과 비교해 검증. 차이 < 1e-5 면 OK.
- 새 연산 추가 / 학습이 수렴 안 할 때 필수. (프로덕션엔 느려서 X)

---

## 핵심 개념 2: Probability and Distributions (Lesson 06)

> 한 줄 요약: 확률은 AI가 불확실성을 표현하는 언어다. 모든 예측은 분포이고, 모든 손실은 두 분포의 차이를 잰다.

### 기초

- 표본공간 S, 사건 = 부분집합. 공리 3개: `P(A)≥0`, `P(S)=1`, 배반이면 `P(A∪B)=P(A)+P(B)`.
- 조건부확률 `P(A|B) = P(A∩B)/P(B)`. 독립 ⟺ `P(A∩B)=P(A)P(B)`.
- **PMF**(이산): `P(X=k)` 직접 읽음. **PDF**(연속): `f(x)`는 밀도(>1 가능), 구간 적분해야 확률.
  - ML: 분류 출력 = PMF, VAE 잠재공간 = PDF.

### 주요 분포

| 분포 | 형태 | 평균 / 분산 | ML 쓰임 |
| --- | --- | --- | --- |
| Bernoulli | `P(1)=p, P(0)=1-p` | `p` / `p(1-p)` | 이진 분류 |
| Categorical | `P(i)=p_i, Σp=1` | — | 다중 분류(softmax) |
| Uniform | 균등 | — | 랜덤 초기화 |
| Normal | `(1/√(2πσ²))e^{-(x-μ)²/2σ²}` | `μ` / `σ²` | 가중치 초기화, 노이즈 |
| Poisson | `λ^k e^{-λ}/k!` | `λ` / `λ` | 희귀 사건 카운트 |

- **기댓값** `E[X]=Σ x·P(x)` (손실 = 데이터 분포에 대한 평균 손실). **분산** `Var(X)=E[X²]-(E[X])²`.
- **결합/주변 분포**: `P(X)=Σ_y P(X,Y)` (다른 변수를 합해서 소거).

### 왜 정규분포가 어디에나 나오나 — 중심극한정리(CLT)

- 독립 확률변수 여러 개의 합/평균은 원래 분포와 무관하게 정규분포로 수렴.
- 그래서: 측정 오차, 가중치 초기화, SGD 그래디언트 노이즈가 대략 정규. (정규 = 주어진 평균·분산에서 최대 엔트로피 분포)

### log 확률 · softmax

- 작은 확률을 계속 곱하면 언더플로 → **log 확률**로 곱을 합으로. `log P` 는 항상 ≤ 0, 더 음수일수록 덜 가능.
- **softmax** `exp(z_i)/Σexp(z_j)` → logit을 확률분포로. **안정화 트릭**: 지수 전에 `max(z)`를 빼서 오버플로 방지 (결과 동일).
- log-softmax = softmax+log 결합. PyTorch가 크로스 엔트로피에 내부적으로 사용. → 3주차 Information Theory와 직결.

---

## 핵심 개념 3: Bayes' Theorem (Lesson 07)

> 한 줄 요약: 확률이 "무엇을 기대하는가"라면, 베이즈 정리는 "증거를 보고 무엇을 배우는가"다.

### 베이즈 정리

- `P(A∩B) = P(A|B)P(B) = P(B|A)P(A)` → **`P(A|B) = P(B|A)·P(A) / P(B)`**.

| 부분 | 이름 | 의미 |
| --- | --- | --- |
| `P(A\|B)` | 사후(posterior) | 증거 B를 본 뒤 A에 대한 갱신된 믿음 |
| `P(B\|A)` | 우도(likelihood) | A가 참일 때 증거 B가 나올 확률 |
| `P(A)` | 사전(prior) | 증거 전 A에 대한 믿음 |
| `P(B)` | 증거(evidence) | 정규화 상수 `= P(B\|A)P(A)+P(B\|¬A)P(¬A)` |

- **의료검사 함정**: 99% 정확한 검사라도 유병률 1/10000이면 양성일 때 실제 병일 확률 ≈ **0.98%**. 사전확률이 지배 → 희귀할수록 대부분 오탐. (기저율 오류)

### 나이브 베이즈 · MLE/MAP

- **나이브 베이즈**: 특징들이 클래스 조건부 독립이라 가정 → `score(c)=P(c)·∏P(feature_i|c)`. 가정은 틀려도(단어 상관) 순위만 맞으면 되니 잘 작동.
- **MLE**: `P(단어|클래스)=빈도`. 안 본 단어면 0 → 전체 곱이 0. **라플라스 스무딩** `(count+1)/(total+|V|)` 로 방지.
- **MAP**: `argmax P(θ|data) ∝ P(data|θ)·P(θ)`. 파라미터에 사전분포 추가 = **정칙화**. 가우시안 사전 = L2(ridge), 라플라스 사전 = L1.

| 추정 | 최적화 대상 | ML 대응 |
| --- | --- | --- |
| MLE | `P(data\|θ)` | 정칙화 없는 학습 |
| MAP | `P(data\|θ)·P(θ)` | L2 / L1 정칙화 |

### 켤레 사전분포 · 순차 갱신

- 사전과 사후가 같은 분포족이면 **켤레(conjugate)** → 적분 없이 숫자 몇 개만 갱신.
- Beta는 확률 파라미터의 대표 켤레 사전. `Beta(a,b) + s성공/f실패 → Beta(a+s, b+f)` (덧셈뿐).
- **순차 갱신**: 오늘의 사후 = 내일의 사전. 배치 갱신과 수학적으로 동일 → 원데이터 저장 없이 온라인 학습. (A/B 테스트: `P(B>A)`를 몬테카를로로 계산, 언제 멈춰도 안전)

---

## 직접 확인해볼 것

- [ ] `Value` 클래스로 `y = relu(x1*x2 + 1)` 그래프를 만들고 `backward()` → `dy/dx1=x2`, `dy/dx2=x1` 확인. PyTorch와 대조.
- [ ] micrograd 스타일 MLP `[2,4,1]`로 XOR 학습(손실이 내려가는지). (`week-02-autodiff-scratch.py` 참고)
- [ ] `gradient_check`로 `(x³+2x+1).tanh()`의 autodiff vs 수치 미분 차이 < 1e-5 확인.
- [ ] `normal_pdf`, `poisson_pmf`, `softmax`(안정화), `log_softmax`를 구현하고 주사위 `E[X]=3.5`, `Var=2.9167` 확인.
- [ ] 주사위 30개 평균을 여러 번 뽑아 히스토그램 → CLT로 종형이 되는지 확인.
- [ ] `bayes(prior=1e-4, likelihood=0.99, fpr=0.01)` → `P(sick|+)≈0.0098` 확인. 두 번 양성이면?
- [ ] 나이브 베이즈 스팸 분류기를 학습시켜 새 메시지 분류 + 스무딩 값(0.01~10) 바꿔가며 top 단어 확률 변화 관찰.

## 이야기할 질문

- 왜 신경망은 forward mode가 아니라 reverse mode(역전파)를 쓰는가?
- "그래디언트는 더한다(accumulation)"가 왜 맞는가? 한 값이 여러 곳에 쓰일 때 무슨 일이 일어나나?
- 99% 정확한 검사인데 양성 시 실제 병일 확률이 1%도 안 되는 게 직관에 반한다 — 어떻게 설명할까?
- "사전분포 = 정칙화"라는 말이 실제 학습에서 어떤 의미인가? (ridge = 가우시안 사전)
- softmax의 max 빼기 트릭이 없으면 실제로 무엇이 깨지나?

## 관심사 / 추가 탐구

- Karpathy의 micrograd / [Zero to Hero](https://karpathy.ai/zero-to-hero.html) 로 autograd 감각 보강.
- Deep-ML의 autograd(#026), single neuron backprop(#025) 문제와 연결 (이미 푼 것들과 이어짐).
- [3Blue1Brown: Bayes' theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM), [CLT](https://www.youtube.com/watch?v=zeJD6dqJ5lo) 영상.
- log-sum-exp 트릭이 크로스 엔트로피/퍼플렉서티(3주차)로 이어지는 흐름 정리.

## 다음 주로 넘길 것

- (완료 후) 08. Optimization 으로 이어서 → 09/10(정보이론·차원축소, 3주차)과 합류.
