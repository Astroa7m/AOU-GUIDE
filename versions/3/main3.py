from uuid import uuid4

from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.chat_message_histories import Neo4jChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.tools import Tool
from graphLLM import uni_info_cypher_chain
import ToolHelpers
from LLMsHelper import get_singleton_general_llm
from versions._helpers.neo4j_connection import get_graph

# Neo4j db graph
graph = get_graph()

# LLM prep

llm = get_singleton_general_llm()


# chat memory prep
def get_memory(session_id):
    return Neo4jChatMessageHistory(session_id=session_id, graph=graph)


SESSION_ID = str(uuid4())

# tools prep used by agent
current_tools = [
    # Tool.from_function(
    #     name="General",
    #     func=llm.invoke,
    #     description=ToolHelpers.Descriptions.general
    # ),
    Tool.from_function(
        name="Graph",
        func=uni_info_cypher_chain.invoke,
        description=ToolHelpers.Descriptions.graph_db
    ),
    Tool.from_function(
        name="User Info",
        description=ToolHelpers.Descriptions.user_info,
        func=ToolHelpers.Functions.get_current_user_info
    ),
    Tool.from_function(
        name="Validate url",
        description=ToolHelpers.Descriptions.validate_url,
        func=ToolHelpers.Functions.validate_url
    )
]

# agent prep

agent_prompt = hub.pull("hwchase17/react-chat")
agent = create_react_agent(llm, current_tools, agent_prompt)
agent_executor = AgentExecutor(agent=agent, tools=current_tools, verbose=True, return_intermediate_steps=True,
                               handle_parsing_errors=True)

chat_agent = RunnableWithMessageHistory(
    agent_executor,
    get_memory,
    input_messages_key="input",
    history_messages_key="chat_history",
)

while True:
    q = input("> ")

    response = chat_agent.invoke(
        {
            "input": q
        },
        {"configurable": {"session_id": SESSION_ID}},
    )

    print(response["output"])
