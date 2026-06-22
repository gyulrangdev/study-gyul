"""Manual scalar autograd playground for Deep-ML problem 026.

Fill the TODOs yourself. This is a scaffold, not the final answer.
"""

from __future__ import annotations


class Value:
    def __init__(self, data: float, _children=(), _op: str = "") -> None:
        self.data = data
        self.grad = 0.0
        self._prev = set(_children)
        self._op = _op
        self._backward = lambda: None

    def __repr__(self) -> str:
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other: "Value") -> "Value":
        # TODO: Create output Value and define how gradient flows to both inputs.
        raise NotImplementedError

    def __mul__(self, other: "Value") -> "Value":
        # TODO: Create output Value and define multiplication local derivatives.
        raise NotImplementedError

    def relu(self) -> "Value":
        # TODO: Create output Value and define ReLU local derivative.
        raise NotImplementedError

    def backward(self) -> None:
        topo: list[Value] = []
        visited: set[Value] = set()

        def build_topo(node: "Value") -> None:
            # TODO: DFS over node._prev, then append node.
            raise NotImplementedError

        build_topo(self)

        # TODO: Set the starting gradient for the final output.
        # TODO: Visit nodes in reverse topological order and call _backward().


if __name__ == "__main__":
    a = Value(2)
    b = Value(-3)
    c = Value(10)

    # TODO: Build a small expression, call backward, and inspect gradients.
    print(a, b, c)
