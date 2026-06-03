# 087 - Adam Optimizer

Deep-ML link: https://www.deep-ml.com/problems/87?from=PyTorch%20Basics

## Goal

Adam optimizer를 NumPy로 직접 구현하기 전에, Adam이 gradient를 어떻게 기억하고 보정하는지 이해한다.

Deep-ML 문제의 핵심 함수는 objective function `f`, gradient function `grad`, initial parameters `x0`를 받아 Adam update를 여러 번 수행하는 형태다.

최종 제출 코드는 아직 넣지 않는다. 이 폴더는 수업 준비와 직접 풀이용 자료다.

## Beginner Mental Model

기본 gradient descent는 매 순간의 gradient만 보고 움직인다.

```text
parameter = parameter - learning_rate * gradient
```

Adam은 여기에 두 가지 기억을 더한다.

- `m`: gradient의 이동 평균. 최근 방향을 부드럽게 기억한다.
- `v`: gradient 제곱의 이동 평균. gradient 크기가 컸는지 작았는지 기억한다.

직관:

- `m`은 "최근에 대체로 어느 방향으로 가고 있었지?"다.
- `v`는 "이 방향의 gradient 크기가 평소에 얼마나 컸지?"다.
- `m / sqrt(v)`는 방향은 유지하되, 너무 큰 gradient는 조심해서 움직이게 만든다.

## Adam Update Formula

At step `t`, with current gradient `g`:

```text
m = beta1 * m + (1 - beta1) * g
v = beta2 * v + (1 - beta2) * (g ** 2)

m_hat = m / (1 - beta1 ** t)
v_hat = v / (1 - beta2 ** t)

parameter = parameter - learning_rate * m_hat / (sqrt(v_hat) + epsilon)
```

Default values usually used:

```text
learning_rate = 0.001
beta1 = 0.9
beta2 = 0.999
epsilon = 1e-8
```

## Why Bias Correction Exists

처음에는 `m = 0`, `v = 0`에서 시작한다.

그래서 초반의 이동 평균은 실제 gradient보다 작게 잡힌다.

예를 들어 첫 gradient가 `g = 2`이고 `beta1 = 0.9`라면:

```text
m = 0.9 * 0 + 0.1 * 2 = 0.2
```

실제 gradient는 `2`인데 `m`은 `0.2`밖에 안 된다.

그래서 첫 step에서는:

```text
m_hat = m / (1 - beta1 ** 1)
      = 0.2 / 0.1
      = 2
```

이렇게 보정해서 초반 추정값이 너무 작아지는 문제를 줄인다.

## Tiny Hand Example

Objective:

```text
f(x) = x^2
grad(x) = 2x
x0 = 1
learning_rate = 0.001
```

Step 1:

```text
g = 2
m = 0.9 * 0 + 0.1 * 2 = 0.2
v = 0.999 * 0 + 0.001 * 4 = 0.004

m_hat = 0.2 / (1 - 0.9) = 2
v_hat = 0.004 / (1 - 0.999) = 4

step = 0.001 * 2 / (sqrt(4) + epsilon)
     ~= 0.001

x = 1 - 0.001 = 0.999
```

첫 step에서 `m_hat`과 `v_hat`이 원래 gradient 크기를 회복하는 것을 보는 것이 중요하다.

## Concept Talk Track

For a 2-3 minute concept explanation:

1. Gradient descent는 현재 gradient만 보고 parameter를 업데이트한다.
2. Momentum은 이전 gradient 방향을 기억해서 업데이트를 부드럽게 만든다.
3. Moving average는 새 값 일부와 과거 평균 일부를 섞는 방식이다.
4. Adam의 first moment `m`은 gradient의 이동 평균이다.
5. Adam의 second moment `v`는 gradient 제곱의 이동 평균이다.
6. `m`과 `v`가 0에서 시작해서 초반에 작게 추정되므로 bias correction을 한다.
7. `epsilon`은 `sqrt(v_hat)`가 0에 가까울 때 나누기가 불안정해지는 것을 막는다.

## Code Talk Track

For a 2-3 minute code explanation:

1. `x = x0.copy()`로 시작해서 원본 입력을 바꾸지 않는다.
2. `m`과 `v`는 `np.zeros_like(x)`로 만든다.
3. 반복문은 `t = 1`부터 시작한다. Bias correction의 지수에 들어가기 때문이다.
4. 매 step마다 `g = grad(x)`를 먼저 계산한다.
5. `m`, `v`를 이동 평균 공식으로 업데이트한다.
6. `m_hat`, `v_hat`으로 bias correction을 한다.
7. `x`를 Adam 공식으로 업데이트한다.

## Syntax To Know

NumPy:

```python
np.asarray(x0, dtype=float)
np.zeros_like(x)
np.sqrt(v_hat)
g**2
```

Function arguments:

```python
def adam_optimizer(
    f,
    grad,
    x0,
    learning_rate=0.001,
    beta1=0.9,
    beta2=0.999,
    epsilon=1e-8,
    num_iterations=10,
):
    ...
```

PyTorch connection:

```python
optimizer = torch.optim.Adam([parameter], lr=0.001, betas=(0.9, 0.999), eps=1e-8)
loss.backward()
optimizer.step()
optimizer.zero_grad()
```

## Shape Notes

If:

- `x` has shape `(n_parameters,)`
- `grad(x)` returns shape `(n_parameters,)`

Then:

- `m` has shape `(n_parameters,)`
- `v` has shape `(n_parameters,)`
- `m_hat / (sqrt(v_hat) + epsilon)` has shape `(n_parameters,)`

Adam works element by element, so every parameter gets its own adjusted step size.

## Common Bugs

- `t`를 0부터 시작해서 `1 - beta1 ** t`가 0이 되는 경우
- `v`에 `g`를 넣고 `g**2`를 넣지 않는 경우
- `sqrt(v_hat + epsilon)`처럼 epsilon 위치를 바꾸는 경우
- `x0`를 copy하지 않아 함수 밖의 값까지 바뀌는 경우
- `grad` 함수가 list를 반환해서 NumPy 연산 shape가 흔들리는 경우
- `f`를 꼭 호출해야 한다고 착각하는 경우. Adam update 자체에는 `grad(x)`만 필요하다.

## Your Steps

Required packages:

```bash
python3 -m pip install numpy
python3 -m pip install torch  # only for pytorch_adam_probe.py
```

1. Run `adam_moments_warmup.py` and explain `g`, `m`, `v`, `m_hat`, `v_hat`.
2. Fill TODOs in `adam_optimizer_starter.py`.
3. Run `pytorch_adam_probe.py` to see that PyTorch stores Adam state internally.
4. Explain why bias correction uses `t = 1, 2, 3, ...`.

## Sources

- Deep-ML problem: https://www.deep-ml.com/problems/87?from=PyTorch%20Basics
- Kingma and Ba introduced Adam as a first-order gradient-based optimizer using adaptive estimates of lower-order moments: https://arxiv.org/abs/1412.6980
