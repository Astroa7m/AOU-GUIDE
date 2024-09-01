# Load and split documents
from langchain_community.document_loaders import JSONLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# loader = TextLoader("../../data/training_data/aou_training_dataset.json", encoding="utf-8")
# docs = loader.load()
# splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
# chunks = splitter.split_documents(documents=docs)
#
# # Initialize HuggingFace embeddings
# embeddings = HuggingFaceEmbeddings()
#
# # Create FAISS vector store
# vector_store = FAISS.from_documents(chunks, embeddings)
# retriever = vector_store.as_retriever()
#
# vector_store.save_local("../first_RAG/uni_vectorstore")


from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# setting up chromadb
loader = TextLoader("../../data/training_data/aou_training_dataset.json", encoding="utf-8")
reviews = loader.load()

reviews_db = Chroma.from_documents(
    documents=reviews, embedding=HuggingFaceEmbeddings(), persist_directory="uni_vectorstore_chroma"
)

print("Retrieval created successfully ")