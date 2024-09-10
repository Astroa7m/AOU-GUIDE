from langchain_community.document_loaders import TextLoader, JSONLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# # setting up chromadb
# loader = TextLoader("../../data/training_data/aou_training_dataset.json", encoding="utf-8")
# reviews = loader.load()

# # Initialize HuggingFace embeddings
# embeddings = HuggingFaceEmbeddings()

loader = JSONLoader(file_path="../../data/training_data/aou_training_dataset.json", jq_schema=".[]", text_content=False)
collection = loader.load()

model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(collection, model, persist_directory="uni_data_chromadb")



