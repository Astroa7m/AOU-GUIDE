from gpt4all import GPT4All

model = GPT4All("C:\\llama-3-8b-full-chat-aou-Q4_K_M\\llama-3-8b-full-chat-aou-Q4_K_M.gguf", device='gpu')  # device='amd', device='intel'
with model.chat_session():
    print(model.generate("اخبرني عن دكتور يوسف", max_tokens=100))