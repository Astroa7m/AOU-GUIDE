import random

from langchain_community.chat_models import ChatOllama
from langchain_community.llms.ollama import Ollama

llm = ChatOllama(model="llama3-aou",  temperature=1, top_k=25, top_p=1, seed=random.randint(0, 10000000))

res = llm.stream("can you provide the profile of doctor Abrar?")

for chunk in res:
    print(chunk.content, end="")
