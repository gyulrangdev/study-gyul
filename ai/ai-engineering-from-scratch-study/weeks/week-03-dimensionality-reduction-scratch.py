"""3주차 실습 - PCA from scratch.

NumPy만으로 PCA를 구현한다: 중심화 -> 공분산 -> 고유분해 -> 투영.
합성 데이터로 설명분산비를 확인하고, (설치돼 있으면) sklearn과 대조한다.

실행: python week-03-dimensionality-reduction-scratch.py
"""

import numpy as np


class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.mean = None
        self.components = None          # (k, d)
        self.eigenvalues = None
        self.explained_variance_ratio_ = None

    def fit(self, X):
        # 1. 중심화
        self.mean = np.mean(X, axis=0)
        Xc = X - self.mean

        # 2. 공분산 행렬 (대칭, 양의 준정부호)
        cov = np.cov(Xc, rowvar=False)

        # 3. 고유분해 (대칭 행렬 -> eigh, 실수 고유값 보장)
        eigenvalues, eigenvectors = np.linalg.eigh(cov)

        # 4. 고유값 내림차순 정렬 (분산 큰 방향 우선)
        order = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[order]
        eigenvectors = eigenvectors[:, order]

        # 5. 상위 k개만 유지
        self.components = eigenvectors[:, : self.n_components].T
        self.eigenvalues = eigenvalues[: self.n_components]
        self.explained_variance_ratio_ = self.eigenvalues / np.sum(eigenvalues)
        return self

    def transform(self, X):
        return (X - self.mean) @ self.components.T

    def fit_transform(self, X):
        return self.fit(X).transform(X)

    def inverse_transform(self, X_reduced):
        """저차원 표현에서 원 공간으로 복원 (근사)."""
        return X_reduced @ self.components + self.mean


def reconstruction_mse(X, pca):
    """복원 오차 = 버린 성분에 담긴 분산의 합과 같아야 한다."""
    X_hat = pca.inverse_transform(pca.transform(X))
    return np.mean((X - X_hat) ** 2)


def main():
    rng = np.random.default_rng(42)
    n = 500

    # 3D 이지만 실질적으로 2D 매니폴드(원) 위에 놓인 데이터
    t = rng.uniform(0, 2 * np.pi, n)
    x1 = 3 * np.cos(t) + rng.normal(0, 0.2, n)
    x2 = 3 * np.sin(t) + rng.normal(0, 0.2, n)
    x3 = 0.5 * x1 + 0.3 * x2 + rng.normal(0, 0.1, n)   # x1, x2의 선형 결합 = 잉여 차원
    X = np.column_stack([x1, x2, x3])

    pca = PCA(n_components=2)
    X_reduced = pca.fit_transform(X)

    print("=== PCA from scratch ===")
    print(f"원본 shape:      {X.shape}")
    print(f"축소 shape:      {X_reduced.shape}")
    print(f"설명분산비:      {np.round(pca.explained_variance_ratio_, 4)}")
    print(f"누적 분산:       {pca.explained_variance_ratio_.sum():.4f}")
    print(f"복원 MSE(2성분): {reconstruction_mse(X, pca):.6f}")

    # sklearn 과 대조 (설치돼 있으면)
    try:
        from sklearn.decomposition import PCA as SKPCA

        sk = SKPCA(n_components=2).fit(X)
        print("\n=== sklearn 대조 ===")
        print(f"우리 설명분산비:   {np.round(pca.explained_variance_ratio_, 6)}")
        print(f"sklearn 설명분산비: {np.round(sk.explained_variance_ratio_, 6)}")
    except ImportError:
        print("\n(sklearn 미설치 - pip install scikit-learn 하면 대조 가능)")


if __name__ == "__main__":
    main()
