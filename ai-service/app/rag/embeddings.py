# embeddings.py
"""
Embeddings Engine for NBA Accreditation Evidence.

Provides vector representations for document chunks and search queries:
1. Local Vector Engine: Uses deterministic TF-IDF feature space (via scikit-learn & numpy).
   Ensures fast, 100% offline, zero-cost, and rate-limit-free semantic search.
2. Optional API Engine: Can interface with OpenAI text-embedding-3-small if configured.
3. Deterministic cosine similarity computations using numpy.
"""

import os
from typing import List, Optional
import numpy as np


class LocalTFIDFEmbedder:
    """
    Lightweight, fast, in-memory TF-IDF embedding model.
    Runs 100% offline without network requests or API costs.
    """

    def __init__(self):
        from sklearn.feature_extraction.text import TfidfVectorizer
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=2048,
            sublinear_tf=True,
            stop_words="english"
        )
        self.is_fitted = False
        self.corpus_cache: List[str] = []

    def fit(self, texts: List[str]):
        """Fit the vectorizer on the document corpus."""
        valid_texts = [t for t in texts if t and t.strip()]
        if not valid_texts:
            valid_texts = ["nba accreditation criterion academic evidence default token"]
        self.vectorizer.fit(valid_texts)
        self.is_fitted = True
        self.corpus_cache = valid_texts

    def transform(self, texts: List[str]) -> np.ndarray:
        """Transform texts into normalized TF-IDF dense vectors."""
        if not self.is_fitted:
            self.fit(texts)
        matrix = self.vectorizer.transform(texts)
        return matrix.toarray()

    def embed_query(self, query: str) -> np.ndarray:
        """Embed a single search query."""
        if not self.is_fitted:
            self.fit([query])
        vec = self.vectorizer.transform([query]).toarray()[0]
        return vec


def compute_cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """
    Compute cosine similarity between two 1D numpy vectors.
    """
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return float(np.dot(vec_a, vec_b) / (norm_a * norm_b))


def compute_batch_cosine_similarities(
    query_vec: np.ndarray,
    doc_matrix: np.ndarray
) -> np.ndarray:
    """
    Compute cosine similarity of a query vector against a matrix of document vectors.
    """
    if doc_matrix.size == 0 or query_vec.size == 0:
        return np.array([])

    query_norm = np.linalg.norm(query_vec)
    if query_norm == 0.0:
        return np.zeros(doc_matrix.shape[0])

    doc_norms = np.linalg.norm(doc_matrix, axis=1)
    # Avoid division by zero
    doc_norms[doc_norms == 0.0] = 1.0

    dot_products = np.dot(doc_matrix, query_vec)
    similarities = dot_products / (doc_norms * query_norm)
    return similarities


class EmbeddingManager:
    """
    Central embeddings manager supporting local TF-IDF and optional OpenAI API embeddings.
    """

    def __init__(self, use_openai: bool = False):
        self.use_openai = use_openai and bool(os.environ.get("OPENAI_API_KEY"))
        self.local_embedder = LocalTFIDFEmbedder()

    def embed_documents(self, texts: List[str]) -> np.ndarray:
        """Generate embeddings for a list of document chunk texts."""
        if self.use_openai:
            try:
                import openai
                client = openai.OpenAI()
                response = client.embeddings.create(
                    model="text-embedding-3-small",
                    input=texts
                )
                vectors = [item.embedding for item in response.data]
                return np.array(vectors)
            except Exception:
                # Fallback to local embedder if OpenAI call fails
                pass

        return self.local_embedder.transform(texts)

    def embed_query(self, query: str) -> np.ndarray:
        """Generate embedding vector for a search query."""
        if self.use_openai:
            try:
                import openai
                client = openai.OpenAI()
                response = client.embeddings.create(
                    model="text-embedding-3-small",
                    input=[query]
                )
                return np.array(response.data[0].embedding)
            except Exception:
                pass

        return self.local_embedder.embed_query(query)
