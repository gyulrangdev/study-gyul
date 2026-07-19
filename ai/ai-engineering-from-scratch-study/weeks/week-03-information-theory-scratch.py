"""3주차 실습 - Information Theory from scratch.

순수 Python으로 정보이론의 핵심 양들을 직접 구현하고 관계를 확인한다.
    엔트로피 H(P), 크로스 엔트로피 H(P,Q), KL 발산 D_KL(P||Q)
    핵심 항등식: H(P,Q) = H(P) + D_KL(P||Q)

실행: python week-03-information-theory-scratch.py
"""

import math
import random


# --- Step 1: 정보량과 엔트로피 -------------------------------------------------

def information_content(p, base=2):
    """사건 확률 p의 정보량(놀람) -log_base(p)."""
    if p <= 0 or p > 1:
        return float("inf") if p <= 0 else 0.0
    return -math.log(p) / math.log(base)


def entropy(probs, base=2):
    """분포의 평균 놀람 H(P) = -sum p*log p."""
    return sum(p * information_content(p, base) for p in probs if p > 0)


# --- Step 2: 크로스 엔트로피와 KL 발산 ----------------------------------------

def cross_entropy(p, q, base=2):
    """H(P, Q) = -sum p*log q."""
    total = 0.0
    for pi, qi in zip(p, q):
        if pi > 0:
            if qi <= 0:
                return float("inf")
            total += pi * (-math.log(qi) / math.log(base))
    return total


def kl_divergence(p, q, base=2):
    """D_KL(P||Q) = H(P,Q) - H(P) = sum p*log(p/q)."""
    return cross_entropy(p, q, base) - entropy(p, base)


# --- Step 3: 분류 손실로서의 크로스 엔트로피 -----------------------------------

def softmax(logits):
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def cross_entropy_loss(true_class, logits):
    """원-핫 타깃에 대한 CE = -log q(정답). base=e (nat)."""
    return -math.log(softmax(logits)[true_class])


# --- Step 5: 상호정보량 --------------------------------------------------------

def mutual_information(joint, base=2):
    """I(X;Y) = sum p(x,y) log( p(x,y) / (p(x)p(y)) )."""
    rows, cols = len(joint), len(joint[0])
    px = [sum(joint[i][j] for j in range(cols)) for i in range(rows)]
    py = [sum(joint[i][j] for i in range(rows)) for j in range(cols)]
    mi = 0.0
    for i in range(rows):
        for j in range(cols):
            pxy = joint[i][j]
            if pxy > 0:
                mi += pxy * math.log(pxy / (px[i] * py[j])) / math.log(base)
    return mi


def main():
    print("=== Step 1: 엔트로피 (bits) ===")
    print(f"공정한 동전:  {entropy([0.5, 0.5]):.4f}")   # 1.0
    print(f"편향 동전:    {entropy([0.99, 0.01]):.4f}")  # 0.08
    print(f"공정 주사위:  {entropy([1 / 6] * 6):.4f}")   # 2.585

    print("\n=== Step 2: CE = H + KL 확인 ===")
    p = [0.7, 0.2, 0.1]
    good, bad = [0.6, 0.25, 0.15], [0.1, 0.1, 0.8]
    for name, q in [("good", good), ("bad", bad)]:
        ce, kl, h = cross_entropy(p, q), kl_divergence(p, q), entropy(p)
        print(f"[{name}] CE={ce:.4f}  H={h:.4f}  KL={kl:.4f}  "
              f"H+KL={h + kl:.4f}  일치={math.isclose(ce, h + kl)}")

    print("\n=== Step 3: 분류 손실 & 퍼플렉서티 ===")
    logits, true_class = [2.0, 1.0, 0.1], 0
    loss = cross_entropy_loss(true_class, logits)
    print(f"softmax = {[round(x, 4) for x in softmax(logits)]}")
    print(f"loss = {loss:.4f} nats,  perplexity = {math.exp(loss):.2f}")

    print("\n=== Step 4: CE == 음의 로그우도(NLL) ===")
    random.seed(42)
    n, k = 1000, 3
    labels = [random.randint(0, k - 1) for _ in range(n)]
    model_logits = [[random.gauss(0, 1) for _ in range(k)] for _ in range(n)]
    ce = sum(cross_entropy_loss(y, z) for y, z in zip(labels, model_logits)) / n
    nll = -sum(math.log(softmax(z)[y]) for y, z in zip(labels, model_logits)) / n
    print(f"CE={ce:.6f}  NLL={nll:.6f}  차이={abs(ce - nll):.2e}")

    print("\n=== Step 5: 상호정보량 (bits) ===")
    indep = [[0.25, 0.25], [0.25, 0.25]]
    dep = [[0.45, 0.05], [0.05, 0.45]]
    print(f"독립:   {mutual_information(indep):.4f}")   # 0.0
    print(f"의존:   {mutual_information(dep):.4f}")     # > 0


if __name__ == "__main__":
    main()
