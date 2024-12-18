from langchain_community.embeddings import FakeEmbeddings
from langchain_community.graphs import Neo4jGraph
import os

from langchain_community.vectorstores import Neo4jVector
from langchain_huggingface import HuggingFaceEmbeddings
from neo4j import GraphDatabase

NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_URI = os.getenv("NEO4J_URI")

graph = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD
)

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD),
)




