import torch
print(torch.cuda.is_available())  # Should return True
print(torch.version.cuda)  # Should show your CUDA version
print(torch.cuda.is_available())  # Should return True if GPU is available
print(torch.cuda.device_count())  # Should return the number of GPUs
print(torch.cuda.current_device())  # Should return the current GPU index
print(torch.cuda.get_device_name(0))  # Should return 'GTX 1050' or your GPU's name