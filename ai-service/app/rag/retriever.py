# retriever.py
"""
Context Retriever for NBA Accreditation Evidence.

Retrieves top-k relevant evidence chunks from the vector store and formats them
into an auditable context block with source provenance citations.
"""

from typing import Any, Dict, List, Optional
from app.rag.vector_store import InMemoryVectorStore, default_vector_store


def retrieve_relevant_chunks(
    query: str,
    top_k: int = 4,
    criterion_filter: Optional[str] = None,
    min_score: float = 0.01,
    vector_store: Optional[InMemoryVectorStore] = None
) -> List[Dict[str, Any]]:
    """
    Retrieve top-k relevant document chunks for a query.
    """
    if vector_store is None:
        vector_store = default_vector_store

    return vector_store.similarity_search(
        query=query,
        top_k=top_k,
        criterion_filter=criterion_filter,
        min_score=min_score
    )


def format_retrieved_context_for_prompt(
    chunks: List[Dict[str, Any]],
    max_total_chars: int = 3500
) -> str:
    """
    Format retrieved evidence chunks into an auditable context block with provenance tags.
    """
    if not chunks:
        return "No relevant documentary evidence found in the vector store for this query."

    formatted_blocks = []
    total_chars = 0

    for idx, c in enumerate(chunks, 1):
        source = c.get("source_file", "Unknown Document")
        page = c.get("page_number", 1)
        crit = c.get("criterion_tag", "General")
        score = c.get("score", 0.0)
        text = c.get("text", "").strip()

        block = (
            f"[EVIDENCE PASSAGE {idx}]\n"
            f"Source Document: {source} (Page: {page} | Tag: {crit} | Match Score: {score})\n"
            f"Content:\n{text}\n"
        )

        if total_chars + len(block) > max_total_chars and formatted_blocks:
            break

        formatted_blocks.append(block)
        total_chars += len(block)

    return "\n---\n".join(formatted_blocks)


def get_retrieved_sources_summary(chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Extract a clean summary of cited sources from the retrieved chunks.
    """
    sources = []
    seen = set()

    for c in chunks:
        doc = c.get("source_file", "")
        page = c.get("page_number", 1)
        key = (doc, page)
        if key not in seen:
            seen.add(key)
            sources.append({
                "source_file": doc,
                "page_number": page,
                "criterion_tag": c.get("criterion_tag", "General"),
                "score": c.get("score", 0.0)
            })

    return sources
