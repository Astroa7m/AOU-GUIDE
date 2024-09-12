from functools import cache

from gpt4all import GPT4All
from langchain_community.chat_models import ChatOllama
from langchain_core.callbacks import StreamingStdOutCallbackHandler, CallbackManager
from langchain_groq import ChatGroq


# general llm
@cache
def get_singleton_general_llm():
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    return ChatOllama(model="llama3-aou", callbacks=callback_manager, max_predict=2, temperature=1, top_k=25,
                      top_p=1)


def get_chat_groq_llm():
    return ChatGroq(model_name="Llama3-8b-8192", temperature=0)

# cypher specialized llm
# llm = Ollam(....)

