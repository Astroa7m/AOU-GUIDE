import random

from langchain_community.chat_models import ChatOllama
from langchain_community.llms.ollama import Ollama

models = ["mistral-7b-aou", "llama3-aou"]

llm = ChatOllama(model=models[0], max_tokens=100)
while True:
    user_input = input("Prompt: ")
    prompt = user_input# + "<|end_header_id|>"
    res = llm.stream(prompt)

    for chunk in res:
        print(chunk.content, end="")
    print()
