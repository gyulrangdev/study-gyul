"""PyTorch autograd probe for Deep-ML problem 025.

Use this after the NumPy warmup to see what PyTorch tracks automatically.
This file is not the final Deep-ML NumPy answer.
"""

from __future__ import annotations

import torch


features = torch.tensor([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]])
labels = torch.tensor([1.0, 0.0, 0.0])
weights = torch.tensor([0.1, -0.2], requires_grad=True)
bias = torch.tensor(0.0, requires_grad=True)

z = features @ weights + bias
predictions = torch.sigmoid(z)
loss = torch.mean((predictions - labels) ** 2)

print("z:", z)
print("predictions:", predictions)
print("loss:", loss)
print("weights.grad before backward:", weights.grad)

# TODO: Call backward on the scalar loss and inspect gradients.
# TODO: Compare weights.grad and bias.grad to your NumPy chain-rule result.
