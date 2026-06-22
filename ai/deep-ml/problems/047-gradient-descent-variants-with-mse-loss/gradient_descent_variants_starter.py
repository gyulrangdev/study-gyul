"""Starter scaffold for Deep-ML problem 047.

Fill the TODOs yourself. This is not the final submitted answer.
"""

from __future__ import annotations

import numpy as np


def mse_loss(X: np.ndarray, y: np.ndarray, weights: np.ndarray) -> float:
    predictions = X @ weights
    errors = predictions - y
    return float(np.mean(errors**2))


def gradient_for_current_batch(
    X_batch: np.ndarray,
    y_batch: np.ndarray,
    weights: np.ndarray,
) -> np.ndarray:
    """Return the MSE gradient for only the current batch."""
    # TODO:
    # 1. Predict with X_batch @ weights.
    # 2. Compute errors as prediction - answer.
    # 3. Average the gradient by the current batch size, not total dataset size.
    raise NotImplementedError


def gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    weights: np.ndarray,
    learning_rate: float,
    n_iterations: int,
    batch_size: int = 1,
    method: str = "batch",
) -> np.ndarray:
    """Practice scaffold for batch, stochastic, and mini-batch updates."""
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    current_weights = np.asarray(weights, dtype=float).copy()

    if method not in {"batch", "stochastic", "mini_batch"}:
        raise ValueError("method must be 'batch', 'stochastic', or 'mini_batch'")

    for _ in range(n_iterations):
        if method == "batch":
            # TODO: Use the whole dataset once.
            raise NotImplementedError

        if method == "stochastic":
            # TODO: Loop over one sample at a time.
            # Hint: X[i : i + 1] keeps the batch dimension.
            raise NotImplementedError

        if method == "mini_batch":
            # TODO: Loop over slices of size batch_size.
            # Hint: range(0, len(X), batch_size)
            raise NotImplementedError

    return current_weights


if __name__ == "__main__":
    X_demo = np.array([[1.0, 1.0], [2.0, 1.0], [3.0, 1.0], [4.0, 1.0]])
    y_demo = np.array([2.0, 3.0, 4.0, 5.0])
    weights_demo = np.zeros(X_demo.shape[1])

    print("initial loss:", mse_loss(X_demo, y_demo, weights_demo))
    print("Fill the TODOs, then call gradient_descent(...) here.")
