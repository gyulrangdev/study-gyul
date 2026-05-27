# 026 - Implementing Basic Autograd Operations

Deep-ML link: https://www.deep-ml.com/problems/26?from=PyTorch%20Basics

## Goal

Build a tiny scalar autograd engine.

The class should wrap one scalar value and remember:

- its numeric data
- its gradient
- which previous values created it
- which operation created it
- how to push gradient back to its parents

## Concept Talk Track

For a 1-2 minute concept explanation:

1. A `Value` object stores one scalar and its gradient.
2. Operator overloading lets `a + b` call `a.__add__(b)` and `a * b` call `a.__mul__(b)`.
3. Each operation creates a new `Value`, forming a computation graph.
4. During forward computation, only data values are produced.
5. During backward computation, local derivatives are multiplied by upstream gradients.
6. Gradients must accumulate because one node can affect the output through multiple paths.
7. A topological order makes sure children are processed before parents.
8. PyTorch tensors do the same idea at a much larger scale.

## Code Talk Track

For a 1-2 minute code explanation:

1. `__init__` stores `data`, starts `grad` at `0`, and records `_prev`.
2. `__add__` and `__mul__` return new `Value` objects with custom `_backward` closures.
3. `relu()` passes positive values forward and blocks non-positive gradients.
4. `backward()` builds a topological list with DFS.
5. The final output gradient starts at `1` because `d_output/d_output = 1`.
6. Walk the graph backward and call each node's `_backward`.

## Syntax To Know

Python class/object:

```python
class Value:
    def __init__(self, data):
        self.data = data
```

Operator overloading:

```python
def __add__(self, other):
    ...

def __mul__(self, other):
    ...
```

Closures:

```python
def outer():
    x = 1

    def inner():
        return x

    return inner
```

DFS/topological traversal:

```python
visited = set()
order = []

def build(node):
    if node not in visited:
        visited.add(node)
        for child in node._prev:
            build(child)
        order.append(node)
```

PyTorch connection:

```python
x = torch.tensor(2.0, requires_grad=True)
y = x * x
y.backward()
print(x.grad)
```

## Local Derivatives To Remember

- Addition: each input receives the upstream gradient.
- Multiplication: each input receives the other input's data times upstream gradient.
- ReLU: gradient passes through only when the forward data was positive.

## Your Steps

1. Run `python_object_warmup.py` to practice class and operator syntax.
2. Fill TODOs in `manual_autograd_playground.py`.
3. Run `pytorch_autograd_connection.py` to compare with PyTorch.
4. Explain why `backward()` starts with gradient `1`.

## Notes

- Do not add `solution.py` until you solve and submit the problem yourself.
- The goal is to understand the engine, not memorize final code.
