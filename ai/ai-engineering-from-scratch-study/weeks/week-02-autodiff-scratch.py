"""2주차 실습 (05) - 미니 autograd 엔진 (micrograd 스타일).

값을 감싸 연산 그래프를 기록하고, 위상정렬 후 역순으로 연쇄 법칙을 적용해
reverse-mode 자동미분을 구현한다. 이걸로 XOR MLP까지 학습한다.

실행: python week-02-autodiff-scratch.py
"""

import math
import random


class Value:
    """스칼라 값 + 그래디언트 + 이 값을 만든 연산 기록."""

    def __init__(self, data, children=(), op=""):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None      # 국소 그래디언트를 부모로 전파하는 클로저
        self._prev = set(children)
        self._op = op

    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += out.grad          # d(a+b)/da = 1
            other.grad += out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self.grad += other.data * out.grad   # d(a*b)/da = b
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def __pow__(self, n):
        out = Value(self.data ** n, (self,), f"**{n}")

        def _backward():
            self.grad += n * (self.data ** (n - 1)) * out.grad
        out._backward = _backward
        return out

    def relu(self):
        out = Value(max(0.0, self.data), (self,), "relu")

        def _backward():
            self.grad += (1.0 if out.data > 0 else 0.0) * out.grad
        out._backward = _backward
        return out

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,), "tanh")

        def _backward():
            self.grad += (1 - t ** 2) * out.grad
        out._backward = _backward
        return out

    # 파생 연산 (기존 연산으로 정의 -> 그래디언트 공짜)
    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def backward(self):
        # 위상정렬: 모든 의존 노드가 뒤에 오도록
        topo, visited = [], set()

        def build(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build(child)
                topo.append(v)

        build(self)
        self.grad = 1.0                    # 시드 dy/dy = 1
        for v in reversed(topo):
            v._backward()


# --- 미니 MLP -----------------------------------------------------------------

class Neuron:
    def __init__(self, n_in):
        self.w = [Value(random.uniform(-1, 1)) for _ in range(n_in)]
        self.b = Value(0.0)

    def __call__(self, x):
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        return act.tanh()

    def parameters(self):
        return self.w + [self.b]


class Layer:
    def __init__(self, n_in, n_out):
        self.neurons = [Neuron(n_in) for _ in range(n_out)]

    def __call__(self, x):
        return [n(x) for n in self.neurons]

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]


class MLP:
    def __init__(self, sizes):
        self.layers = [Layer(sizes[i], sizes[i + 1]) for i in range(len(sizes) - 1)]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x[0] if len(x) == 1 else x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]


def gradient_check(build_expr, x_val, h=1e-7):
    """autodiff 그래디언트 vs 수치 미분."""
    x = Value(x_val)
    y = build_expr(x)
    y.backward()
    y_plus = build_expr(Value(x_val + h)).data
    y_minus = build_expr(Value(x_val - h)).data
    numerical = (y_plus - y_minus) / (2 * h)
    return x.grad, numerical, abs(x.grad - numerical)


def main():
    print("=== 수동 검증: y = relu(x1*x2 + 1) ===")
    x1, x2 = Value(2.0), Value(3.0)
    y = (x1 * x2 + 1).relu()
    y.backward()
    print(f"y = {y.data}  dy/dx1 = {x1.grad} (=x2)  dy/dx2 = {x2.grad} (=x1)")

    print("\n=== 그래디언트 체킹: (x^3 + 2x + 1).tanh() @ x=0.5 ===")
    ad, num, diff = gradient_check(lambda x: (x ** 3 + x * 2 + 1).tanh(), 0.5)
    print(f"autodiff={ad:.8f}  numerical={num:.8f}  diff={diff:.2e}")

    print("\n=== XOR 학습 (MLP [2,4,1]) ===")
    random.seed(42)
    model = MLP([2, 4, 1])
    xs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    ys = [-1, 1, 1, -1]                 # tanh 출력이라 -1/1
    for step in range(100):
        preds = [model(x) for x in xs]
        loss = sum((p - y) ** 2 for p, y in zip(preds, ys))
        for p in model.parameters():
            p.grad = 0.0
        loss.backward()
        for p in model.parameters():
            p.data -= 0.05 * p.grad     # 경사하강
        if step % 20 == 0:
            print(f"step {step:3d}  loss = {loss.data:.4f}")
    print("학습 후 예측:")
    for x, y in zip(xs, ys):
        print(f"  input={x}  target={y:2d}  pred={model(x).data:6.3f}")


if __name__ == "__main__":
    main()
