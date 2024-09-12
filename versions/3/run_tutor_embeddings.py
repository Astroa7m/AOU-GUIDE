import os

from langchain_community.vectorstores import Neo4jVector
from langchain_huggingface import HuggingFaceEmbeddings

# creating index
neo4j_vector_index = Neo4jVector.from_existing_graph(
    embedding=HuggingFaceEmbeddings(),
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
    index_name="tutor_info",
    node_label="Tutor",
    text_node_properties=["biography", "biographyArabic", "name", "nameArabic"],
    embedding_node_property="tutor_info_emb"

)

result = neo4j_vector_index.similarity_search_with_score("Alaa'g")

print("Suitable result:")
print()
print(result[0])
print()
for tutor in result:
    print(tutor)
