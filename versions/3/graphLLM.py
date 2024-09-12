from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain
from langchain_core.prompts import PromptTemplate

import ToolHelpers
from LLMsHelper import get_chat_groq_llm, get_singleton_general_llm
from versions._helpers.neo4j_connection import get_graph

cypher_llm = get_chat_groq_llm()
qa_llm = get_singleton_general_llm()

graph = get_graph()

####################
# For database generation
cypher_generation_prompt = PromptTemplate(
    template=ToolHelpers.Prompts.cypher_generation_template,
    input_variables=["schema", "question"],
)

qa_generation_prompt = PromptTemplate(
    input_variables=["context", "question"], template=ToolHelpers.Prompts.qa_generation_template
)

uni_info_cypher_chain = GraphCypherQAChain.from_llm(
    # will use a fine-tuned llm on schema and cypher later for cypher_llm
    cypher_llm=cypher_llm,
    qa_llm=qa_llm,
    graph=graph,
    verbose=True,
    qa_prompt=qa_generation_prompt,
    cypher_prompt=cypher_generation_prompt,
    validate_cypher=True,
    top_k=100
)


answer = uni_info_cypher_chain.invoke({"query": "Who is doctor alaa"})


for chunk in answer:
    print(chunk.content, end="")


