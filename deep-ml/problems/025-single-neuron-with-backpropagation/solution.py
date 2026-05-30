from __future__ import annotations

import numpy as np


def train_neuron(
    features: np.ndarray,
    labels: np.ndarray,
    initial_weights: np.ndarray,
    initial_bias: float,
    learning_rate: float,
    epochs: int,
) -> tuple[np.ndarray, float, list[float]]:
    weights = initial_weights.astype(float).copy()
    bias = float(initial_bias)
    mse_values: list[float] = []

    for _ in range(epochs):
        z = features @ weights + bias
        predictions = 1 / (1 + np.exp(-z))

        errors = predictions - labels
        mse = np.mean(errors**2)
        mse_values.append(round(float(mse), 4))

        d_mse_d_predictions = 2 * errors / len(labels)
        d_predictions_d_z = predictions * (1 - predictions)
        d_mse_d_z = d_mse_d_predictions * d_predictions_d_z

        weight_gradients = features.T @ d_mse_d_z
        bias_gradient = np.sum(d_mse_d_z)

        weights -= learning_rate * weight_gradients
        bias -= learning_rate * bias_gradient

    updated_weights = np.round(weights, 4)
    updated_bias = round(float(bias), 4)

    return updated_weights, updated_bias, mse_values
