# Load and split documents
from langchain_community.document_loaders import JSONLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("../../data/training_data/aou_training_dataset.json", encoding="utf-8")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
chunks = splitter.split_documents(documents=docs)

# Initialize HuggingFace embeddings
embeddings = HuggingFaceEmbeddings()

# Create FAISS vector store
vector_store = FAISS.from_documents(chunks, embeddings)

vector_store.save_local("uni_vectorstore")


print("Retrieval created successfully ")