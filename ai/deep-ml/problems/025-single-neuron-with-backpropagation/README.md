# 025 - Single Neuron with Backpropagation

Deep-ML link: https://www.deep-ml.com/problems/25?from=PyTorch%20Basics

## Goal

Train one sigmoid neuron with full-batch gradient descent.

Core forward path:

```text
z = XW + b
y_pred = sigmoid(z)
loss = mean((y_pred - y_true)^2)
```

The problem asks for manual NumPy backpropagation, while the presentation should also connect the same computation to PyTorch autograd.

## Concept Talk Track

For a 1-2 minute concept explanation:

1. A single neuron is a weighted sum plus bias: `z = XW + b`.
2. Sigmoid squashes each score into a value between 0 and 1.
3. MSE measures average squared prediction error.
4. Backpropagation applies the chain rule from loss back to `W` and `b`.
5. Gradient descent updates parameters in the opposite direction of the gradient.
6. PyTorch autograd records the computation graph and computes the chain rule for us.

## Code Talk Track

For a 1-2 minute code explanation:

1. Convert inputs to arrays or tensors.
2. Compute `z`, `predictions`, and `mse`.
3. Save the MSE before updating.
4. Compute gradients for the full batch.
5. Update weights and bias once per epoch.
6. Round only the returned values, not intermediate training math.

## Syntax To Know

NumPy:

```python
features @ weights
np.exp(...)
np.mean(...)
array.shape
array.T
```

PyTorch:

```python
torch.tensor(..., dtype=torch.float32, requires_grad=True)
torch.sigmoid(...)
loss.backward()
weights.grad
with torch.no_grad():
    # parameter update
    pass
weights.grad.zero_()
```

## Shape Notes

Let:

- `features` have shape `(batch_size, num_features)`
- `weights` have shape `(num_features,)`
- `bias` be a scalar
- `labels` have shape `(batch_size,)`

Then:

- `features @ weights` has shape `(batch_size,)`
- `predictions - labels` has shape `(batch_size,)`
- gradients for `weights` should match `(num_features,)`

## Your Steps

1. Run `numpy_warmup.py` and inspect shapes.
2. Fill the TODOs in `numpy_manual_backprop.py`.
3. Run `pytorch_autograd_probe.py` to see how PyTorch computes the same gradients.
4. Explain the difference: NumPy requires manual chain rule; PyTorch stores the graph and calls `backward()`.

## Notes

- `solution.py` was added after the user explicitly requested the final answer because of time pressure.
- Keep exploratory warmups separate from final Deep-ML answer code.
