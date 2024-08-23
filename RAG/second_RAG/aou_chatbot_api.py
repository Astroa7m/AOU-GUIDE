# getting neo4j python driver instance
from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from RAG.helpers.neo4j_connection import get_graph

graph = get_graph()

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0)

CYPHER_GENERATION_TEMPLATE = """You are an expert Neo4j Developer translating user questions into Cypher to answer 
questions about Arab Open University and provide information. Convert the user's question based on the schema.

Instructions: 
- Use only the provided relationship types and properties in the schema.

- Do not use any other relationship types or properties that are not provided.

- When asked about a name of a tutor or module, use contains for the name and ignore
  any titles entered by the user, if you want to use logical operators mostly use OR match the 
  case for input and values from the graph. E.g. MATCH (t:Tutor) 
  WHERE lower(t.name) contains lower("alaa") OR lower(t.title) contains lower("doctor") 
  RETURN t.name, t.title, t.email, t.Biography
  
- When asked about modules, the user might use module codes or names or description in English and Arabic make sure 
  to compare them with their corresponding fields and don't forget to use lower function. E.g.
  MATCH (m:Modules) 
  WHERE lower(m.name) contains lower("java") OR lower(m.nameArabic) contains lower("جافا") OR m.description CONTAINS 
  lower("java") OR m.descriptionArabic CONTAINS lower("جافا")
  RETURN m

- The user might misspell a word in Arabic or English or it might also be correct according to the data saved within the
  database, make sure to include variants of the word when comparing or looking for different things, 
  also when translating use similar words to so the result can be found. E.g ابرار can also be Ibrar as well as Abrar
  
- always provide a link if there was a link attached to the node for more details so the user can click on

- When asked in Arabic reply in Arabic, and if asked in English reply in English unless the user says otherwise

Schema: {schema}
Question: {question}
"""

cypher_generation_prompt = PromptTemplate(
    template=CYPHER_GENERATION_TEMPLATE,
    input_variables=["schema", "question"]
)

cypher_chain = GraphCypherQAChain.from_llm(
    llm=llm,
    graph=graph,
    cypher_prompt=cypher_generation_prompt,
    verbose=True
)

while True:
    question = input("> ")
    response = cypher_chain.invoke({"query": question})
    print(response)
