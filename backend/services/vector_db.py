import chromadb
from chromadb.config import Settings
from backend.core.config import get_settings
from backend.services.gemini_service import GeminiService

settings = get_settings()

class VectorDBService:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_PERSIST_DIRECTORY)
        self.collection = self.client.get_or_create_collection(name="documents")
        self.gemini_service = GeminiService()

    def add_document(self, doc_id: str, text: str, metadata: dict = None):
        embedding = self.gemini_service.get_embedding(text)
        if not embedding:
            raise ValueError("Failed to generate embedding")
        
        self.collection.add(
            documents=[text],
            metadatas=[metadata or {}],
            ids=[doc_id],
            embeddings=[embedding]
        )

    def query(self, query_text: str, n_results: int = 5):
        embedding = self.gemini_service.get_embedding(query_text)
        if not embedding:
            raise ValueError("Failed to generate embedding for query")

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )
        return results
