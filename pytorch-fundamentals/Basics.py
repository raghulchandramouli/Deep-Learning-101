import torch

# Scalar:
scalar = torch.tensor(7)
print(scalar.ndim)

# Vector:
vector = torch.tensor([7, 7])
print(vector.ndim)

# Matrix:
Matrix = torch.tensor([[7, 8], 
                       [9, 10]])
print(Matrix.ndim)

# Tensor:
Tensor = torch.tensor([[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [10, 11, 12]]])
print(Tensor.ndim)

