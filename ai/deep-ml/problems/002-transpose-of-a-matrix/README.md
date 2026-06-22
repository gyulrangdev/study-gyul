# 002 - Transpose of a Matrix

Deep-ML link: https://www.deep-ml.com/problems/2?from=PyTorch%20Basics

## Goal

Given a 2D matrix with shape `(m, n)`, produce a matrix with shape `(n, m)`.

Think in coordinates:

- original position: row `i`, column `j`
- transposed position: row `j`, column `i`

## Syntax To Know

Python lists:

```python
rows = len(a)
cols = len(a[0])
value = a[row_index][col_index]
```

Loop shape:

```python
for col_index in range(cols):
    new_row = []
    for row_index in range(rows):
        # append one item from the original matrix
        pass
```

NumPy checks:

```python
arr.shape
arr.T
arr.tolist()
```

PyTorch checks:

```python
tensor.shape
tensor.T
tensor.tolist()
```

## Your Steps

1. Use `numpy_warmup.py` to inspect the shape and transpose behavior.
2. Fill in `pytorch_attempt.py` after the NumPy version makes sense.
3. Write the final Deep-ML browser answer only after you can explain which index moves where.

## Notes

- Keep the final answer out of this folder until you solve it yourself.
- Add final submitted code later as `solution.py`.
