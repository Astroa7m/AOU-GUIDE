from sentence_transformers import SentenceTransformer


class SentenceTransformerWrapper:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    # This method will be called by Neo4jVector for embedding text queries
    def embed_query(self, text):
        return self.model.encode(text)

    # Optionally, you can add another method for embedding documents
    def embed_documents(self, documents):
        return self.model.encode(documents)