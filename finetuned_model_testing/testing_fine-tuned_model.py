# the model must be first quantized to 4-bit to be used with my limited resources
#Regular laptops don’t have enough RAM and GPU memory to load the entire model,
#so we have to quantify the GGUF model, reducing the 16 GB model to around 4-5 GB.
# this code has no use
import torch
from transformers import pipeline

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
device = 0 if torch.cuda.is_available() else -1  # Automatically select GPU if available

pipe = pipeline("text-generation", model="astroa7m/llama-3-8b-full-chat-aou", device=device)
messages = [{"role": "user", "content": "Who are you?"}]
pipe(messages)
