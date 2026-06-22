# 047 - Gradient Descent Variants with MSE Loss

Deep-ML link: https://www.deep-ml.com/problems/47?from=PyTorch%20Basics

## Goal

MSE loss를 줄이도록 linear model의 `weights`를 직접 업데이트한다.

핵심 forward path:

```text
y_pred = X @ weights
loss = mean((y_pred - y) ** 2)
weights = weights - learning_rate * gradient
```

이 문제의 핵심은 같은 gradient descent라도 데이터를 얼마나 모아서 한 번 업데이트하느냐에 따라 Batch, SGD, Mini-Batch로 나뉜다는 점이다.

최종 제출 코드는 아직 넣지 않는다. 이 폴더는 수업 준비와 직접 풀이용 자료다.

## Beginner Mental Model

`weights`는 모델이 현재 믿고 있는 규칙이다.

예를 들어 집값을 예측한다고 하면:

- `X`는 집의 정보다. 예: 넓이, 방 개수
- `weights`는 각 정보가 얼마나 중요한지 나타내는 숫자다.
- `X @ weights`는 현재 규칙으로 만든 예측값이다.
- `y`는 정답이다.
- `loss`는 예측이 얼마나 틀렸는지 나타내는 점수다.
- `gradient`는 "이 weight를 올리면 loss가 커지는지 작아지는지" 알려주는 방향표시다.

Gradient descent는 loss가 커지는 방향의 반대로 조금 움직인다.

```text
weights = weights - learning_rate * gradient
```

`gradient`가 양수면 weight를 줄이고, `gradient`가 음수면 weight를 늘린다.

## Shape Notes

Let:

- `X` have shape `(n_samples, n_features)`
- `weights` have shape `(n_features,)`
- `y` have shape `(n_samples,)`

Then:

- `X @ weights` has shape `(n_samples,)`
- `y_pred - y` has shape `(n_samples,)`
- `X.T @ (y_pred - y)` has shape `(n_features,)`
- `gradient` must have the same shape as `weights`

Shape를 맞추는 것이 이 문제의 절반이다.

## MSE Gradient

MSE:

```text
loss = mean((y_pred - y) ** 2)
```

여기서:

```text
y_pred = X @ weights
error = y_pred - y
```

Full batch gradient:

```text
gradient = (2 / n_samples) * X.T @ error
```

왜 `2`가 붙는가:

```text
d(error ** 2) / d(error) = 2 * error
```

왜 `X.T`가 붙는가:

각 weight가 각 feature와 곱해져서 예측값을 만들기 때문이다. 각 feature가 error에 얼마나 기여했는지 다시 모으려면 `X.T @ error`가 된다.

## Tiny Hand Example

작은 데이터:

```text
X = [[1, 1],
     [2, 1]]
y = [2, 3]
weights = [0, 0]
learning_rate = 0.1
```

1. 예측:

```text
y_pred = X @ weights = [0, 0]
```

2. 오차:

```text
error = y_pred - y = [-2, -3]
```

3. MSE:

```text
loss = mean([4, 9]) = 6.5
```

4. Gradient:

```text
X.T = [[1, 2],
       [1, 1]]

X.T @ error = [
  1 * -2 + 2 * -3,
  1 * -2 + 1 * -3
] = [-8, -5]

gradient = (2 / 2) * [-8, -5] = [-8, -5]
```

5. Update:

```text
new_weights = [0, 0] - 0.1 * [-8, -5]
            = [0.8, 0.5]
```

Gradient가 음수라서 weight가 커졌다. 현재 예측값이 정답보다 너무 작았기 때문에 자연스럽다.

## Batch vs SGD vs Mini-Batch

| Method | 한 번 업데이트할 때 보는 데이터 | 느낌 | 장점 | 주의점 |
| --- | --- | --- | --- | --- |
| Batch | 전체 데이터 | 가장 차분함 | gradient가 안정적 | 데이터가 크면 한 번 업데이트가 무거움 |
| SGD | 샘플 1개 | 많이 흔들림 | 자주 업데이트해서 빠르게 움직임 | loss가 출렁일 수 있음 |
| Mini-Batch | 작은 묶음 | 실전에서 가장 흔함 | 속도와 안정성의 균형 | 마지막 batch 크기가 작을 수 있음 |

이 문제에서는 같은 MSE gradient 공식을 쓰되, `n_samples` 자리에 현재 update에 사용한 데이터 개수를 넣는다고 생각하면 된다.

## Concept Talk Track

For a 2-3 minute concept explanation:

1. Linear prediction은 `X @ weights`로 만든다.
2. MSE는 예측값과 정답의 차이를 제곱해서 평균낸 값이다.
3. Gradient는 loss를 줄이려면 weights를 어느 방향으로 바꿔야 하는지 알려준다.
4. Gradient descent는 gradient 반대 방향으로 weights를 조금 이동한다.
5. Learning rate는 한 번에 움직이는 크기다.
6. Epoch는 전체 데이터를 한 번 다 보는 것이다.
7. Batch, SGD, Mini-Batch는 업데이트 한 번에 사용하는 데이터 양만 다르다.

## Code Talk Track

For a 2-3 minute code explanation:

1. `X`, `y`, `weights`를 NumPy array로 맞춘다.
2. `y_pred = X @ weights`를 계산한다.
3. `error = y_pred - y`를 계산한다.
4. `gradient = (2 / batch_size) * X_batch.T @ error`를 계산한다.
5. `weights -= learning_rate * gradient`로 업데이트한다.
6. Batch는 전체 `X`, SGD는 한 행, Mini-Batch는 `X[start:end]`를 사용한다.
7. 중간 계산은 반올림하지 말고, 문제에서 요구할 때만 마지막에 반올림한다.

## Syntax To Know

NumPy:

```python
X @ weights
X.T
np.mean(errors**2)
np.asarray(...)
range(start, stop, step)
```

PyTorch connection:

```python
weights = torch.zeros(num_features, requires_grad=True)
loss.backward()
weights.grad
optimizer.step()
optimizer.zero_grad()
```

## Implementation Checklist

1. `method`가 `"batch"`, `"stochastic"`, `"mini_batch"` 중 하나인지 확인한다.
2. `weights`를 원본 그대로 바꾸지 않도록 copy한다.
3. Batch는 한 epoch마다 전체 데이터로 한 번 업데이트한다.
4. SGD는 한 epoch 안에서 샘플을 하나씩 꺼내 업데이트한다.
5. Mini-Batch는 한 epoch 안에서 `batch_size` 단위로 잘라 업데이트한다.
6. 마지막 mini-batch가 작아도 실제 batch 길이로 gradient 평균을 낸다.
7. `gradient.shape == weights.shape`를 계속 확인한다.

## Common Bugs

- `error = y - y_pred`로 바꿨는데 update 식은 그대로 써서 방향이 반대로 되는 경우
- `X @ weights` 대신 `weights @ X`를 써서 shape가 깨지는 경우
- Mini-Batch에서 항상 전체 데이터 개수로 나누는 경우
- SGD에서 샘플 한 개를 1D로 꺼내고 `X.T @ error` shape를 헷갈리는 경우
- Training 중간에 매번 반올림해서 학습이 부정확해지는 경우

## Your Steps

Required packages:

```bash
python3 -m pip install numpy
python3 -m pip install torch  # only for pytorch_optimizer_probe.py
```

1. Run `numpy_mse_gradient_warmup.py` and explain every printed shape.
2. Fill TODOs in `gradient_descent_variants_starter.py`.
3. Run `pytorch_optimizer_probe.py` to connect the same idea to PyTorch.
4. Explain the difference between one epoch and one parameter update.

## Sources

- Deep-ML problem: https://www.deep-ml.com/problems/47?from=PyTorch%20Basics
- Deep-ML describes the platform as a place to practice ML coding challenges in the browser and get instant feedback: https://www.deep-ml.com/problems/47
