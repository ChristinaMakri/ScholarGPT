from sentence_transformers import SentenceTransformer

class CustomEmbeddingModel:
    def __init__(self, model_name="allenai-specter"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents):
        texts = [doc.page_content for doc in documents]
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return embeddings
