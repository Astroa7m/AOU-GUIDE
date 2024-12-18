from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from versions._helpers.neo4j_connection import graph
from LLMsHelper import get_singleton_general_llm, get_chat_groq_llm
from vector import academic_staff_vector

# text to cypher tool
cypher_generation_template = """
    You are an expert Neo4j Developer translating user questions into Cypher to answer 
questions about Arab Open University and provide information. Convert the user's question based on the schema.


    Instructions: 
    - Use only the provided relationship types and properties in the schema.

    - Do not use any other relationship types or properties that are not provided.

    - Always return the full context as the result of the cypher chain query not just some fields

    - Always use 'OR' instead of 'AND', never use 'AND' in queries

    - The user might provide extra names or titles beside the intended element for instance, 
    'What is module BS323' Do not create a query like the following:
    MATCH (n: Module) WHERE lower(n.code) contains lower('module BS323') return n
    you should get only the module code and passed to the query, same with other queries.

    - The user might mention the name of the node within the input which might make it easier

    for you to look for but if nothing is mentioned that can match the schema and if for instance
    the input was generic like 'Who is Ahmed?' then you should run the following example:
    MATCH (n) where n.name contains 'Ahmed' or m.description or m.biography return n
    As if you were searching the whole nodes and comparing all properties to find a match

    - Always use 'contains' and not '=' as the user might not enter the full name nor the correct name. Also
    lower the user input and the column value when comparing for instance if the input 'what is m110 module'
    then the query should be:
    MATCH (n: Module) WHERE lower(n.code) contains lower(m110) return n


    Schema:
    {schema}
    Question:
    provide all information about the following question, {question}
    """
cypher_qa = GraphCypherQAChain.from_llm(
    get_singleton_general_llm(),
    graph=graph,
    cypher_prompt=PromptTemplate.from_template(cypher_generation_template),
    verbose=True
)

#retrieval tool
instructions = (
    "Use the given context to answer the question."
    "If you don't know the answer, say you don't know."
    "Context: {context}"
)

retrieval_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", instructions),
        ("human", "{input}"),
    ]
)

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
retriever = academic_staff_vector.as_retriever()

question_answer_chain = create_stuff_documents_chain(get_singleton_general_llm(), retrieval_prompt)

academic_staff_retrieval_chain = create_retrieval_chain(
    retriever,
    question_answer_chain
)

def get_academic_staff_retriever(input):
    return academic_staff_retrieval_chain.invoke({'input': input})

# creating the aou chain
from langchain.tools import Tool


chat_prompt = ChatPromptTemplate(
    [
        ("system",
         "You are an Arab Open University (AOU) expert, providing information about various aspect of the university"),
        ("human", "{input}")
    ]
)

aou_chat = chat_prompt | get_singleton_general_llm()

# creating set of tools
tools = [
    Tool.from_function(
        name="General Chat",
        description="For general discussion not covered by other tools",
        func=aou_chat.invoke,
    ),
    # Tool.from_function(
    #     name="Academic staff search",
    #     description="When you need to find information about academic staff or tutors",
    #     func=get_academic_staff_retriever,
    # ),
Tool.from_function(
        name="General QA question",
        description="Use it for every question",
        func=cypher_qa,
    )
]

# Create chat history callback
from langchain_community.chat_message_histories import Neo4jChatMessageHistory


def get_memory(session_id):
    return Neo4jChatMessageHistory(session_id=session_id, graph=graph)


# Create the agent
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.runnables.history import RunnableWithMessageHistory
from utils.agent_prompt import agent_prompt

agent = create_react_agent(get_singleton_general_llm(), tools, agent_prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

chat_agent = RunnableWithMessageHistory(
    agent_executor,
    get_memory,
    input_messages_key="input",
    history_messages_key="chat_history",
)
# Create a handler to call the agent
while True:
    user_input = input("prompt: ")
    response = chat_agent.invoke(
        {"input": user_input},
        {"configurable": {"session_id": 2}}, )

    print(response['output'])
