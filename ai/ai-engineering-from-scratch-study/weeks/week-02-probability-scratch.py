"""2주차 실습 (06) - 확률과 분포 from scratch.

PMF/PDF, 기댓값/분산, 수치 안정 softmax/log-softmax, 중심극한정리를
표준 라이브러리만으로 구현하고 확인한다.

실행: python week-02-probability-scratch.py
"""

import math
import random


def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


# --- PMF / PDF ----------------------------------------------------------------

def bernoulli_pmf(k, p):
    return p if k == 1 else (1 - p)


def poisson_pmf(k, lam):
    return (lam ** k) * math.exp(-lam) / factorial(k)


def normal_pdf(x, mu, sigma):
    coeff = 1.0 / (sigma * math.sqrt(2 * math.pi))
    return coeff * math.exp(-0.5 * ((x - mu) / sigma) ** 2)


# --- 기댓값 / 분산 ------------------------------------------------------------

def expected_value(values, probs):
    return sum(v * p for v, p in zip(values, probs))


def variance(values, probs):
    mu = expected_value(values, probs)
    return sum(p * (v - mu) ** 2 for v, p in zip(values, probs))


# --- softmax / log-softmax (수치 안정) ----------------------------------------

def softmax(logits):
    m = max(logits)                       # 오버플로 방지: 최댓값 빼기
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def log_softmax(logits):
    m = max(logits)
    log_sum_exp = m + math.log(sum(math.exp(z - m) for z in logits))
    return [z - log_sum_exp for z in logits]


def cross_entropy_loss(logits, target_index):
    return -log_softmax(logits)[target_index]


# --- 샘플링 (Box-Muller) ------------------------------------------------------

def sample_normal(mu, sigma, n=1):
    out = []
    for _ in range(n):
        u1, u2 = random.random(), random.random()
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        out.append(mu + sigma * z)
    return out


# --- 중심극한정리 -------------------------------------------------------------

def demonstrate_clt(dist_fn, n_samples, n_averages):
    return [sum(dist_fn() for _ in range(n_samples)) / n_samples
            for _ in range(n_averages)]


def main():
    print("=== 주사위 기댓값/분산 ===")
    vals, probs = [1, 2, 3, 4, 5, 6], [1 / 6] * 6
    mu, var = expected_value(vals, probs), variance(vals, probs)
    print(f"E[X]={mu:.4f}  Var={var:.4f}  SD={var ** 0.5:.4f}")  # 3.5 / 2.9167

    print("\n=== PMF/PDF 몇 개 ===")
    print(f"Poisson(k=2, λ=3) = {poisson_pmf(2, 3):.4f}")
    print(f"Normal(0, μ=0, σ=1) = {normal_pdf(0, 0, 1):.4f}")   # 0.3989 (1/√2π)

    print("\n=== softmax 안정화 (큰 logit) ===")
    print(f"softmax([100,101,102]) = {[round(x, 4) for x in softmax([100, 101, 102])]}")
    logits = [2.0, 0.5, -1.0, 3.0, 0.1]
    print(f"CE loss (정답=3) = {cross_entropy_loss(logits, 3):.4f}")

    print("\n=== 중심극한정리: 주사위 평균 ===")
    random.seed(42)
    die = lambda: random.randint(1, 6)
    for n in (1, 2, 30):
        avgs = demonstrate_clt(die, n_samples=n, n_averages=5000)
        m = sum(avgs) / len(avgs)
        sd = (sum((a - m) ** 2 for a in avgs) / len(avgs)) ** 0.5
        print(f"주사위 {n:2d}개 평균:  mean={m:.3f}  sd={sd:.3f}  (n↑ 이면 sd↓, 종형에 근접)")


if __name__ == "__main__":
    main()
