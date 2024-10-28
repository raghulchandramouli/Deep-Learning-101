# Reproducibility (trying to take the random out of random)

import torch
import random

# Create a random tensor:
random_tensor_A = torch.rand(3, 3)
random_tensor_B = torch.rand(3, 3)

print(f"Tensor A: {random_tensor_A}\n")
print(f"Tensor B: {random_tensor_B}\n")
print(f"Does Tensor A equal Tensor B? {random_tensor_A == random_tensor_B}")

# Taking Random out of Random:
RANDOM_SEED = 42

torch.manual_seed(RANDOM_SEED)
random_tensor_C = torch.rand(3, 3)

# Have to reset every time a new_rand() is called:
torch.random.manual_seed(RANDOM_SEED)
random_tensor_D = torch.rand(3, 3)

print(f"Tensor C: {random_tensor_C}\n")
print(f"Tensor D: {random_tensor_D}\n")
print(f"Does Tensor C equal Tensor D? {random_tensor_C == random_tensor_D}")

