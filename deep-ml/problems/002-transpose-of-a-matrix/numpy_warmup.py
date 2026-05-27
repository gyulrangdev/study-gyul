"""NumPy warmup for Deep-ML problem 002.

This file is intentionally not the final submitted answer.
Use it to observe shapes and indexing before writing the browser solution.
"""

from __future__ import annotations

import numpy as np


sample = np.array([[1, 2, 3], [4, 5, 6]])

print("sample:")
print(sample)
print("shape:", sample.shape)

print("transpose view:")
print(sample.T)
print("transpose shape:", sample.T.shape)

# TODO: Try a different rectangular matrix below.
your_matrix = np.array([
    # fill this in
])

if your_matrix.size:
    print("your matrix shape:", your_matrix.shape)
    print(your_matrix.T)
