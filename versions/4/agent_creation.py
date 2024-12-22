from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tools import send_email
# memory
memory = MemorySaver()



# creating the tool
search = TavilySearchResults(max_results=2)
# search_results = search.invoke("what is the weather in Oman")
# print(search_results)
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search, send_email]


# model init
# doesn't support fucntion calling, must use llama3.1
# llm = ChatOllama(model="llama3")

llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0, groq_api_key = "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")



# binding tools
# llm_with_tools = llm.bind_tools(tools)


# creating agent
agent_exe = create_react_agent(llm, tools)

config = {"configurable": {"thread_id": "abc123"}}



response = agent_exe.stream({"messages": "with my credentials ('fake.dr.abrar@gmail.com', 'iloe gfvm jskg pgdb') send an email to ahmed123.as27@gmail.com saying that sorry I can't make it to class?"}, stream_mode="values")

for chunk in response:
    print(chunk['messages'][-1].pretty_print(), end='')

