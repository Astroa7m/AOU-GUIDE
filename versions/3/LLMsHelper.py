from functools import cache

from gpt4all import GPT4All
from langchain_community.chat_models import ChatOllama
from langchain_core.callbacks import StreamingStdOutCallbackHandler, CallbackManager
from langchain_groq import ChatGroq


# general llm
@cache
def get_singleton_general_llm():
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    return ChatOllama(model="mistral-7b-aou", temperature=0, top_k=100, top_p=100,num_predict=50, callbacks=callback_manager)



def get_chat_groq_llm():
    return ChatGroq(model_name="Llama3-8b-8192", temperature=0)

# cypher specialized llm
# llm = Ollam(....)

