from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="uni_data_chromadb", embedding_function=model)

print(answer)