"""Adam moment warmup for Deep-ML problem 087.

This file prints the intermediate Adam values for a tiny objective.
It is intentionally not the final submitted answer.
"""

from __future__ import annotations

import numpy as np


def gradient(x: np.ndarray) -> np.ndarray:
    """Gradient of f(x) = sum(x ** 2)."""
    return 2 * x


x = np.array([1.0, 1.0])
m = np.zeros_like(x)
v = np.zeros_like(x)

learning_rate = 0.001
beta1 = 0.9
beta2 = 0.999
epsilon = 1e-8

for t in range(1, 4):
    g = gradient(x)
    m = beta1 * m + (1 - beta1) * g
    v = beta2 * v + (1 - beta2) * (g**2)

    m_hat = m / (1 - beta1**t)
    v_hat = v / (1 - beta2**t)
    step = learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
    x = x - step

    print("t:", t)
    print("gradient:", g)
    print("m:", m)
    print("v:", v)
    print("m_hat:", m_hat)
    print("v_hat:", v_hat)
    print("step:", step)
    print("x:", x)
    print()

# TODO: Change beta1 to 0.0.
# What disappears when the optimizer stops remembering past gradients?
