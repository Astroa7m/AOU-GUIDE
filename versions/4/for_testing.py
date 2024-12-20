from langchain.agents import create_react_agent, AgentExecutor
from langchain_ollama import ChatOllama
from tools import tools
llm = ChatOllama(model="llama3")

from utils.agent_prompt import agent_prompt

agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    handle_parsing_errors=True,
    verbose=True
)

res = agent_executor.stream(
    {"input": "with my credentials (fake.dr.abrar@gmail.com, iloe gfvm jskg pgdb) send an email to ahmed123.as27@gmail.com saying that sorry I can't make it to class"})
for chunk in res:
    print(chunk, end="")
