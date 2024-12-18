# Now, initialize this wrapper with your model
from langchain_community.vectorstores import Neo4jVector
import sentenceTransformerWrapper
from versions._helpers.neo4j_connection import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD
from sentenceTransformerWrapper import SentenceTransformerWrapper

embedding_model = SentenceTransformerWrapper('sentence-transformers/all-MiniLM-L6-v2')

# Create Neo4j Vector object
academic_staff_vector = Neo4jVector.from_existing_graph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    index_name="academic_staff_index",
    node_label="AcademicStaff",
    text_node_properties=['name', "nameArabic", "biography", "biographyArabic", "teaches", "title",
                          "titleArabic", "specialization", "specializationArabic", "position",
                          "positionArabic", "link"],
    embedding_node_property="academicEmbedding",
    embedding=embedding_model  # Use the function to generate embeddings
)
#
# # Perform similarity search
# response = academic_staff_vector.similarity_search("ابرار", k=5)
# print(response[0])
# print(response[1])
# print(response[2])
# print(response[3])
# print(response[4])
