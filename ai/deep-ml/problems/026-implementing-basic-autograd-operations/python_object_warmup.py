"""Python object and operator-overloading warmup for problem 026.

This intentionally avoids gradients. Use it to learn the syntax first.
"""

from __future__ import annotations


class Box:
    def __init__(self, data: float) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f"Box(data={self.data})"

    def __add__(self, other: "Box") -> "Box":
        return Box(self.data + other.data)

    def __mul__(self, other: "Box") -> "Box":
        return Box(self.data * other.data)


a = Box(2)
b = Box(3)
c = Box(10)

print("a:", a)
print("a + b:", a + b)
print("a + b * c:", a + b * c)

# TODO: Add a relu-like method to Box that returns 0 when data <= 0.
