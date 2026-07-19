"""2주차 실습 (07) - 베이즈 정리 & 나이브 베이즈 from scratch.

베이즈 정리로 사후확률을 계산하고, 라플라스 스무딩 + log 공간으로
나이브 베이즈 스팸 분류기를 만든다. 순차 베이즈 갱신(Beta)도 확인한다.

실행: python week-02-bayes-scratch.py
"""

import math
from collections import defaultdict


def bayes(prior, likelihood, false_positive_rate):
    """P(H|E) = P(E|H)P(H) / [P(E|H)P(H) + P(E|¬H)P(¬H)]."""
    evidence = likelihood * prior + false_positive_rate * (1 - prior)
    return likelihood * prior / evidence


class NaiveBayes:
    def __init__(self, smoothing=1.0):
        self.smoothing = smoothing
        self.class_counts = defaultdict(int)
        self.word_counts = defaultdict(lambda: defaultdict(int))
        self.class_word_totals = defaultdict(int)
        self.vocab = set()

    def train(self, documents, labels):
        for doc, label in zip(documents, labels):
            self.class_counts[label] += 1
            for word in doc.lower().split():
                self.word_counts[label][word] += 1
                self.class_word_totals[label] += 1
                self.vocab.add(word)

    def predict(self, document):
        words = document.lower().split()
        total_docs = sum(self.class_counts.values())
        vocab_size = len(self.vocab)
        best_class, best_score = None, float("-inf")
        for cls in self.class_counts:
            score = math.log(self.class_counts[cls] / total_docs)   # log 사전
            for word in words:
                count = self.word_counts[cls].get(word, 0)
                total = self.class_word_totals[cls]
                # 라플라스 스무딩 + log 우도 (언더플로 방지)
                score += math.log((count + self.smoothing)
                                  / (total + self.smoothing * vocab_size))
            if score > best_score:
                best_class, best_score = cls, score
        return best_class


def main():
    print("=== 의료검사 (기저율 오류) ===")
    p1 = bayes(prior=1e-4, likelihood=0.99, false_positive_rate=0.01)
    print(f"1회 양성:  P(sick|+) = {p1:.4f}  ({p1 * 100:.2f}%)")
    p2 = bayes(prior=p1, likelihood=0.99, false_positive_rate=0.01)  # 사후→사전
    print(f"2회 양성:  P(sick|+,+) = {p2:.4f}  ({p2 * 100:.2f}%)")

    print("\n=== 나이브 베이즈 스팸 분류 ===")
    docs = [
        "win free money now", "free lottery ticket winner",
        "claim your prize today free", "urgent offer free cash",
        "congratulations you won free",
        "meeting tomorrow at noon", "project update attached",
        "can we schedule a call", "quarterly report review",
        "lunch on thursday sounds good", "team standup notes attached",
        "please review the pull request",
    ]
    labels = ["spam"] * 5 + ["ham"] * 7
    clf = NaiveBayes()
    clf.train(docs, labels)
    for msg in ["free money waiting for you", "meeting rescheduled to friday",
                "you won a free prize", "please review the attached report"]:
        print(f"  '{msg}' -> {clf.predict(msg)}")

    print("\n=== 순차 베이즈 갱신 (Beta 켤레 사전) ===")
    a, b = 1, 1                              # Beta(1,1) = 균등 사전
    print(f"사전    Beta({a},{b})  mean={a / (a + b):.3f}")
    for heads, tails in [(7, 3), (5, 5)]:
        a, b = a + heads, b + tails         # 사후 = Beta(a+성공, b+실패)
        print(f"+{heads}H/{tails}T -> Beta({a},{b})  mean={a / (a + b):.3f}")


if __name__ == "__main__":
    main()
