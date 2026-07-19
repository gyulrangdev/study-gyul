"""Starter scaffold for Deep-ML problem 087.

Fill the TODOs yourself. This is not the final submitted answer.
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np


def adam_optimizer(
    f: Callable[[np.ndarray], float],
    grad: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    learning_rate: float = 0.001,
    beta1: float = 0.9,
    beta2: float = 0.999,
    epsilon: float = 1e-8,
    num_iterations: int = 10,
) -> np.ndarray:
    """Practice scaffold for Adam.

    The objective function f is accepted to match the problem signature.
    The update itself should use grad(x).
    """
    _ = f
    x = np.asarray(x0, dtype=float).copy()
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    beta1_power = 1.0
    beta2_power = 1.0

    for _ in range(num_iterations):
        g = grad(x)
        beta1_power *= beta1
        beta2_power *= beta2

        m *= beta1
        m += (1.0 - beta1) * g
        v *= beta2
        v += (1.0 - beta2) * np.square(g)

        x -= learning_rate * (m / (1.0 - beta1_power)) / (
            np.sqrt(v / (1.0 - beta2_power)) + epsilon
        )

    return x


if __name__ == "__main__":
    def objective(x: np.ndarray) -> float:
        return float(np.sum(x**2))

    def gradient(x: np.ndarray) -> np.ndarray:
        return 2 * x

    start = np.array([1.0, 1.0])
    print("Fill the TODOs, then call adam_optimizer(objective, gradient, start).")
