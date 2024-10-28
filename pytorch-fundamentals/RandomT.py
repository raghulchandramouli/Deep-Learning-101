import torch

# Random Tensors:
random_tensor = torch.rand(size=(3, 4))
print(random_tensor, random_tensor.dtype)

# Creating a tensor with a size of an Image:
random_image_size_tensor = torch.rand(size=(224, 224, 3))
print(random_image_size_tensor.shape, random_image_size_tensor.ndim)

# starting with ones & zeros:
zeros = torch.zeros(size=(3, 4))
print(zeros, zeros.dtype)

ones = torch.ones(size=(3, 4))
print(ones, ones.dtype)

# Default data type is float32:
float_32_tensor = torch.tensor([3.0, 6.0, 9.0],
                               dtype=torch.float16,
                               device=None,
                               requires_grad=False)

print(float_32_tensor, float_32_tensor.dtype, float_32_tensor.device)

# Create a Tensor:
some_tensor = torch.rand(3, 4)

print(some_tensor)
print(f"Shape of tensor: {some_tensor.shape}")
print(f"Datatype of tensor: {some_tensor.dtype}")
print(f"Device tensor is stored on: {some_tensor.device}")

