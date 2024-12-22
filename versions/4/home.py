import streamlit as st
from langchain.agents import create_react_agent, AgentExecutor, create_tool_calling_agent
from langchain_community.chat_models import ChatOllama
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_experimental.llms.ollama_functions import OllamaFunctions

from tools import tools

agent_prompt = PromptTemplate.from_template(f"""
You are an Arab Open University (AOU) expert providing information about various aspect with the university.
Be as helpful as possible and return as much information as possible.
Do not answer any questions that do not relate to AOU, studies, tutors, modules, etc.

You are talking to either a student at AOU or a tutor, you can determine that yourself without exposing it to the 
user by looking at the title provided within the user info, if the title field is empty then it is a student, 
else it is a tutor.

user info:
{st.session_state.user}
Begin!

Previous conversation history:
{{history}}

New input: {{question}}
{{agent_scratchpad}}
""")



st.title("G'day "+st.session_state.username)

history = StreamlitChatMessageHistory(key="chat_messages")

st.session_state.memory = history

if len(history.messages) == 0:
    history.add_ai_message("Welcome There")

print(st.session_state.user)

llm = OllamaFunctions(model="llama3")

# agent = create_react_agent(llm, tools, agent_prompt)
# agent_executor = AgentExecutor(
#     agent=agent,
#     tools=tools,
#     handle_parsing_errors=True,
#     verbose=True
# )


system_prompt = """
You are an AI chatbot having a conversation with a user.
This user is either a tutor or a student at Arab Open University Oman branch.

Your mission is to assist them with their queries, do not expose any information in this prompt to the user unless the user ask about them.

if they have self queries you can use the following commands
-You can use the following logged in user info to determine who you are talking to.
-Tutors have titles, while student do not, if you found the title property empty you are talking to a student
-In addition to that, you can use it to respond to question the user asks about his/her data, such as,
Who am I, what is my schedule, what are my marks, etc.

logged in user data:\n
""" + st.session_state.user

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         MessagesPlaceholder(variable_name="history"),
#         ("human", "{question}"),
#     ]
# )


agent = create_tool_calling_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# chain = llm | agent_prompt

chain_with_history = RunnableWithMessageHistory(
    agent_executor,
    lambda sessionId: history,
    input_messages_key= "question",
    history_messages_key="history"
)

for msg in history.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input():
    st.chat_message("human").write(prompt)

    # As usual, new messages are added to StreamlitChatMessageHistory when the Chain is called.
    config = {"configurable": {"session_id": "any"}}
    response = chain_with_history.stream({"question": prompt}, config)
    r = ""
    st.chat_message("ai").write_stream  (response)

