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
    # initial_weights를 바로 바꾸지 않도록 복사하고, 계산을 위해 float 타입으로 맞춘다.
    weights = initial_weights.astype(float).copy()

    # initial_bias도 계산 중 바뀔 값이라 별도 변수 bias에 저장한다.
    bias = float(initial_bias)

    # 각 epoch마다 업데이트 전 MSE loss를 저장할 리스트다.
    mse_values: list[float] = []

    # epochs 횟수만큼 forward pass -> loss 기록 -> backprop -> update를 반복한다.
    for epoch in range(epochs):
        # forward pass (예측하기)
        # 뉴런의 점수를 계산한다. (z = X @ W + b) 입력값에 가중치들을 더하고 + bias
        z = features @ weights + bias

        # sigmoid 점수를 0~1로 누른다
        # z 큰 양수 -> 1, z가 0 -> 0.5, z가 큰 음수 -> 0
        pred = 1 / (1 + np.exp(-z))

        # error는 예측값 - 정답이다. 어느 방향으로 얼마나 틀렸는지 나타낸다.
        error = pred - labels

        # MSE loss (얼마나 틀렸는지)
        mse = np.mean(error**2)

        # 문제에서 epoch마다의 MSE를 요구하므로, 업데이트하기 전 loss를 소수점 4자리로 저장한다.
        mse_values.append(round(float(mse), 4))

        # 목적: "pred가 조금 바뀌면 mse는 얼마나 바뀌지?"를 구한다.
        # 이 값을 알아야 mse의 책임을 pred 쪽으로 넘길 수 있다.
        # MSE를 pred에 대해 미분한다. mean을 썼으므로 데이터 개수로 나눈다.
        d_mse_d_pred = 2 * error / len(labels)

        # 목적: "z가 조금 바뀌면 pred는 얼마나 바뀌지?"를 구한다.
        # pred는 sigmoid(z)로 만들어졌으므로, z의 변화가 pred에 주는 영향을 알아야 한다.
        # sigmoid의 미분이다. sigmoid(z)를 이미 pred로 구했으므로 p * (1 - p)를 쓴다.
        d_pred_d_z = pred * (1 - pred)

        # 목적: "z가 mse를 얼마나 바꾸는지"를 구한다.
        # mse -> pred -> z 로 책임을 한 칸 더 뒤로 보내는 단계다.
        # chain rule: mse -> pred -> z 순서로 이어진 미분값을 곱한다.
        d_mse_d_z = d_mse_d_pred * d_pred_d_z

        # 목적: "weights가 mse를 얼마나 바꾸는지"를 구한다.
        # weights는 z를 만들고, z는 mse까지 이어지므로 d_mse_d_z를 features와 연결한다.
        # z = features @ weights + bias 이므로, weights별 gradient는 features.T @ d_mse_d_z로 모은다.
        weight_gradients = features.T @ d_mse_d_z

        # 목적: "bias가 mse를 얼마나 바꾸는지"를 구한다.
        # bias는 모든 샘플의 z에 똑같이 더해지므로, 각 샘플의 책임을 전부 더한다.
        # bias는 모든 샘플에 더해지는 값이라, 각 샘플의 z gradient를 전부 더한다.
        bias_gradient = np.sum(d_mse_d_z)

        # 목적: weights를 loss가 줄어드는 방향으로 실제로 수정한다.
        # gradient는 loss가 커지는 방향을 가리키므로, 반대로 빼준다.
        # gradient descent: loss를 줄이기 위해 gradient 방향의 반대로 weights를 이동시킨다.
        weights -= learning_rate * weight_gradients

        # 목적: bias도 loss가 줄어드는 방향으로 실제로 수정한다.
        # bias도 weights와 같은 방식으로 업데이트한다.
        bias -= learning_rate * bias_gradient

    # 최종 weights를 소수점 4자리로 반올림하고, 예시 출력처럼 Python list로 바꾼다.
    updated_weights = np.round(weights, 4).tolist()

    # 최종 bias도 소수점 4자리로 반올림한다.
    updated_bias = round(float(bias), 4)

    # 문제에서 요구한 순서대로 업데이트된 weights, bias, MSE 기록을 반환한다.
    return updated_weights, updated_bias, mse_values
