import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory


st.title("G'day "+st.session_state.username)

history = StreamlitChatMessageHistory(key="chat_messages")

st.session_state.memory = history

if len(history.messages) == 0:
    history.add_ai_message("Welcome There")

print(st.session_state.user)

llm = ChatOllama(model="llama3")

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

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

chain = prompt | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
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

