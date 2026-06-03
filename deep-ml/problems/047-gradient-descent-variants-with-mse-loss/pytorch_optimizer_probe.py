"""PyTorch probe for the same MSE gradient descent idea.

Use this after the NumPy warmup. It shows what PyTorch does for full-batch
gradient descent, but it is not the final Deep-ML NumPy answer.
"""

from __future__ import annotations

import torch


X = torch.tensor(
    [
        [1.0, 1.0],
        [2.0, 1.0],
        [3.0, 1.0],
    ]
)
y = torch.tensor([2.0, 3.0, 4.0])
weights = torch.zeros(X.shape[1], requires_grad=True)
optimizer = torch.optim.SGD([weights], lr=0.1)

for epoch in range(3):
    optimizer.zero_grad()
    y_pred = X @ weights
    loss = torch.mean((y_pred - y) ** 2)
    loss.backward()

    print("epoch:", epoch)
    print("weights before step:", weights.detach())
    print("loss:", loss.item())
    print("gradient:", weights.grad)

    optimizer.step()
    print("weights after step:", weights.detach())
    print()

# TODO: Change this file so it trains on X[:1], then X[1:2], then X[2:3].
# That is the PyTorch equivalent of looking at SGD one sample at a time.
