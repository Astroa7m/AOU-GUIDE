import random

from langchain_community.chat_models import ChatOllama
from langchain_community.llms.ollama import Ollama

models = ["mistral-7b-aou", "llama3-aou"]

llm = ChatOllama(model=models[0],  temperature=0, top_k=100, top_p=100,num_predict=50)

res = llm.stream("Can you help me knowing some modules?")

for chunk in res:
    print(chunk.content, end="")
