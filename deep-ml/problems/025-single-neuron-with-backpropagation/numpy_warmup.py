"""NumPy warmup for Deep-ML problem 025.

Use this file to build shape intuition before writing manual gradients.
It is intentionally not the final submitted answer.
"""

from __future__ import annotations

import numpy as np


features = np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]])
labels = np.array([1.0, 0.0, 0.0])
weights = np.array([0.1, -0.2])
bias = 0.0


def sigmoid(z: np.ndarray) -> np.ndarray:
    """Sigmoid activation for a NumPy array."""
    return 1 / (1 + np.exp(-z))


z = features @ weights + bias
predictions = sigmoid(z)
errors = predictions - labels
mse = np.mean(errors**2)

print("features shape:", features.shape)
print("weights shape:", weights.shape)
print("labels shape:", labels.shape)
print("z:", z)
print("predictions:", predictions)
print("errors:", errors)
print("mse:", mse)

# TODO: Print the derivative shape you expect for weights.
# Hint: it should match weights.shape.
