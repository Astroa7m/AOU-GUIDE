import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# Load the base model (Mistral or any other model)
base_model_name = "astroa7m/mistral_v3_7b_aou"  # Replace with your actual model
model = AutoModelForCausalLM.from_pretrained(base_model_name, token="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")

# Load the tokenizer (associated with the base model)
tokenizer = AutoTokenizer.from_pretrained(base_model_name, token="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")

# Load the LoRA adapters from Hugging Face Hub
adapter_name = "your-hf-username/your-lora-"  # Replace with your adapter on HF Hub
model = PeftModel.from_pretrained(model, adapter_name)

# Put model in evaluation mode
model.eval()

# Now you can use the model for inference!
# Example text prompt
prompt = "What can you tell me about the M351 module?"

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# Generate the output from the model
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=50)

# Decode the output into text
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
