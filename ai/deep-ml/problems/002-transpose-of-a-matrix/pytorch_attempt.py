"""PyTorch attempt for Deep-ML problem 002.

Fill this in after the NumPy warmup feels clear.
"""

from __future__ import annotations

import torch


sample = torch.tensor([[1, 2, 3], [4, 5, 6]])

print("sample:")
print(sample)
print("shape:", tuple(sample.shape))

print("transpose view:")
print(sample.T)
print("transpose shape:", tuple(sample.T.shape))


def practice_transpose(a: list[list[int | float]]) -> list[list[int | float]]:
    """Practice version. Keep final Deep-ML answer separate."""
    rows = len(a)
    cols = len(a[0])

    result: list[list[int | float]] = []
    for col_index in range(cols):
        new_row: list[int | float] = []
        for row_index in range(rows):
            # TODO: Which original value belongs here?
            pass
        result.append(new_row)

    return result


print(practice_transpose([[1, 2], [3, 4], [5, 6]]))
