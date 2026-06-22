"""NumPy warmup for Deep-ML problem 047.

This file shows one full-batch MSE gradient update on a tiny example.
It is intentionally not the final submitted answer.
"""

from __future__ import annotations

import numpy as np


X = np.array(
    [
        [1.0, 1.0],
        [2.0, 1.0],
        [3.0, 1.0],
    ]
)
y = np.array([2.0, 3.0, 4.0])
weights = np.array([0.0, 0.0])
learning_rate = 0.1

y_pred = X @ weights
errors = y_pred - y
mse = np.mean(errors**2)
gradient = (2 / len(X)) * (X.T @ errors)
new_weights = weights - learning_rate * gradient

print("X shape:", X.shape)
print("weights shape:", weights.shape)
print("y_pred shape:", y_pred.shape)
print("errors:", errors)
print("mse:", mse)
print("gradient:", gradient)
print("gradient shape:", gradient.shape)
print("new weights:", new_weights)

first_mini_batch = X[:2]
first_mini_labels = y[:2]
print("first mini-batch shape:", first_mini_batch.shape)
print("first mini-batch labels shape:", first_mini_labels.shape)

# TODO: Change weights to [0.8, 0.5] and run this again.
# What happens to MSE after one update?
