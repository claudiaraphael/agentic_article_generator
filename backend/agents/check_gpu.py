import torch

# Check if GPU is available
gpu_available = torch.cuda.is_available()
device_name = torch.cuda.get_device_name(0) if gpu_available else "No GPU found"

print(f"GPU Available: {gpu_available}")
print(f"GPU Name: {device_name}")