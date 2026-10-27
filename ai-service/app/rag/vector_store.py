# vector_store.py
"""
Vector Store for NBA Accreditation Evidence Chunks.

Maintains in-memory document vectors and supports fast semantic retrieval
with cosine similarity scoring and criterion-based filtering.
"""

from typing import Any, Dict, List, Optional
import numpy as np

from app.rag.embeddings import EmbeddingManager, compute_batch_cosine_similarities


class InMemoryVectorStore:
    """
    Lightweight, deterministic in-memory vector index.
    """

    def __init__(self, use_openai: bool = False):
        self.embedding_manager = EmbeddingManager(use_openai=use_openai)
        self.chunks: List[Dict[str, Any]] = []
        self.vector_matrix: Optional[np.ndarray] = None

    def add_chunks(self, chunks: List[Dict[str, Any]]) -> int:
        """
        Add document chunks to the store and compute/update their vector embeddings.
        """
        if not chunks:
            return 0

        new_texts = [c.get("text", "") for c in chunks]

        # Combine all existing texts + new texts to re-fit local vectorizer
        all_texts = [c.get("text", "") for c in self.chunks] + new_texts
        self.embedding_manager.local_embedder.fit(all_texts)

        # Re-compute vectors for all chunks
        self.chunks.extend(chunks)
        full_texts = [c.get("text", "") for c in self.chunks]
        self.vector_matrix = self.embedding_manager.embed_documents(full_texts)

        return len(chunks)

    def similarity_search(
        self,
        query: str,
        top_k: int = 5,
        criterion_filter: Optional[str] = None,
        min_score: float = 0.0
    ) -> List[Dict[str, Any]]:
        """
        Search for the most relevant document chunks matching the query.
        """
        if not self.chunks or self.vector_matrix is None or self.vector_matrix.size == 0:
            return []

        query_vec = self.embedding_manager.embed_query(query)
        scores = compute_batch_cosine_similarities(query_vec, self.vector_matrix)

        results = []
        for idx, score in enumerate(scores):
            chunk = self.chunks[idx]

            # Apply optional criterion filter (e.g. "Criterion 3", "Criterion 5")
            if criterion_filter:
                chunk_crit = chunk.get("criterion_tag", "").lower()
                if criterion_filter.lower() not in chunk_crit and chunk_crit not in ["general", "all"]:
                    continue

            if score >= min_score:
                results.append({
                    "chunk_id": chunk.get("chunk_id", f"chunk_{idx}"),
                    "text": chunk.get("text", ""),
                    "score": round(float(score), 4),
                    "source_file": chunk.get("source_file", ""),
                    "page_number": chunk.get("page_number", 1),
                    "criterion_tag": chunk.get("criterion_tag", "General"),
                    "metadata": {
                        k: v for k, v in chunk.items()
                        if k not in ["text", "chunk_id", "source_file", "page_number", "criterion_tag"]
                    }
                })

        # Sort descending by similarity score
        results.sort(key=lambda x: x["score"], reverse=True)

        return results[:top_k]

    def get_total_chunks(self) -> int:
        """Return the number of indexed chunks."""
        return len(self.chunks)

    def get_indexed_files(self) -> List[str]:
        """Return list of distinct source filenames in the vector store."""
        return sorted(list(set(c.get("source_file", "") for c in self.chunks if c.get("source_file"))))

    def clear(self):
        """Reset the vector index."""
        self.chunks = []
        self.vector_matrix = None
        self.embedding_manager = EmbeddingManager()


# Singleton default vector store instance
default_vector_store = InMemoryVectorStore()
