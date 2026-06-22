"""PyTorch probe for Adam optimizer state.

Use this after the NumPy warmup to connect manual Adam variables to
torch.optim.Adam. This file is not the final Deep-ML NumPy answer.
"""

from __future__ import annotations

import torch


x = torch.tensor([1.0, 1.0], requires_grad=True)
optimizer = torch.optim.Adam([x], lr=0.001, betas=(0.9, 0.999), eps=1e-8)

for step in range(3):
    optimizer.zero_grad()
    loss = torch.sum(x**2)
    loss.backward()

    print("step:", step + 1)
    print("x before optimizer.step():", x.detach())
    print("gradient:", x.grad)

    optimizer.step()

    state = optimizer.state[x]
    print("x after optimizer.step():", x.detach())
    print("stored Adam state keys:", sorted(state.keys()))
    print("exp_avg is Adam m:", state["exp_avg"])
    print("exp_avg_sq is Adam v:", state["exp_avg_sq"])
    print()

# TODO: Compare exp_avg and exp_avg_sq with your NumPy m and v values.
