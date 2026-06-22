"""Manual NumPy backprop practice for Deep-ML problem 025.

Fill the TODOs yourself. This is a learning scaffold, not the final answer.
"""

from __future__ import annotations

import numpy as np


def sigmoid(z: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-z))


def sigmoid_derivative(sigmoid_output: np.ndarray) -> np.ndarray:
    """Derivative of sigmoid when you already have sigmoid(z)."""
    # TODO: Fill this in from the identity using s = sigmoid(z).
    raise NotImplementedError


def one_epoch_shapes(
    features: np.ndarray,
    labels: np.ndarray,
    weights: np.ndarray,
    bias: float,
) -> None:
    """Print intermediate shapes for one full-batch step."""
    z = features @ weights + bias
    predictions = sigmoid(z)
    errors = predictions - labels

    print("z shape:", z.shape)
    print("predictions shape:", predictions.shape)
    print("errors shape:", errors.shape)

    # TODO: Work out these gradients by chain rule.
    # d_loss/d_predictions:
    # d_predictions/d_z:
    # d_z/d_weights:
    # d_z/d_bias:


if __name__ == "__main__":
    sample_features = np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]])
    sample_labels = np.array([1.0, 0.0, 0.0])
    sample_weights = np.array([0.1, -0.2])
    sample_bias = 0.0

    one_epoch_shapes(sample_features, sample_labels, sample_weights, sample_bias)
