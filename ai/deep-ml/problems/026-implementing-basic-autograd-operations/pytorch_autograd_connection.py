"""PyTorch connection for Deep-ML problem 026.

PyTorch tensors are like a production-grade version of the tiny Value class.
"""

from __future__ import annotations

import torch


a = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(-3.0, requires_grad=True)
c = torch.tensor(10.0, requires_grad=True)

d = a + b * c
e = torch.relu(d)

print("d:", d)
print("e:", e)
print("a.grad before backward:", a.grad)

# TODO: Call e.backward() and inspect a.grad, b.grad, c.grad.
# TODO: Change b to a positive value and observe how ReLU changes gradient flow.
