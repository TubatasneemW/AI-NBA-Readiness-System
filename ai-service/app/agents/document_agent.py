# document_agent.py
"""
Document Intelligence & RAG Agent for NBA Accreditation Evidence.

Responsibilities:
1. Grounded Question-Answering: Queries ingested institutional documents (syllabi,
   appointment letters, research papers, patent certificates, NBA SAR manual)
   and provides factually bounded answers with exact document citations.
2. Structured Entity Extraction: Parses unstructured documents to extract
   Course Outcomes (COs), assessment weightages, faculty designations, and DOIs.
3. Strict Verification & Provenance: Never hallucinates facts not present in the
   retrieved evidence passages. Declares missing information explicitly.
"""

from typing import Any, Dict, List, Optional

from app.services.model_client import call_model
from app.rag.retriever import (
    retrieve_relevant_chunks,
    format_retrieved_context_for_prompt,
    get_retrieved_sources_summary
)
from app.rag.vector_store import InMemoryVectorStore, default_vector_store


def answer_document_query(
    query: str,
    criterion_filter: Optional[str] = None,
    vector_store: Optional[InMemoryVectorStore] = None,
    top_k: int = 4,
    mock_response: Optional[str] = None
) -> Dict[str, Any]:
    """
    Perform a RAG-grounded query against ingested accreditation evidence.

    Returns:
        Dictionary containing:
        - query
        - answer (LLM generated with citations)
        - sources (list of cited source documents and page numbers)
        - raw_retrieved_chunks_count
    """
    if vector_store is None:
        vector_store = default_vector_store

    # 1. Retrieve top-k relevant evidence chunks
    matched_chunks = retrieve_relevant_chunks(
        query=query,
        top_k=top_k,
        criterion_filter=criterion_filter,
        vector_store=vector_store
    )

    sources = get_retrieved_sources_summary(matched_chunks)
    context_str = format_retrieved_context_for_prompt(matched_chunks)

    # 2. Build factually bounded RAG prompt
    prompt = f"""
You are the Document Intelligence & RAG Agent in an
AI-Driven NBA Accreditation Readiness System.

Your responsibility is to answer the following accreditation query
STRICTLY using the retrieved evidence passages provided below.

==================================================
GROUNDING & CITATION RULES
==================================================

1. Base your answer ONLY on the provided evidence passages.
2. DO NOT assume, extrapolate, or invent facts not present in the text.
3. ALWAYS cite the source document and page number for every claim made
   (e.g., "[Source: Course_Syllabus.pdf, Page: 2]").
4. If the retrieved evidence does not contain the answer, explicitly state:
   "The uploaded institutional documents do not contain information regarding this query."
5. Never hallucinate numbers, accreditation grades, or compliance approvals.

==================================================
RETRIEVED DOCUMENT EVIDENCE PASSAGES
==================================================

{context_str}

==================================================
USER QUERY
==================================================

"{query}"

==================================================
ANSWER WITH CITATIONS
==================================================
"""

    answer_text = call_model(
        prompt=prompt,
        max_output_tokens=1500,
        model="openai/gpt-oss-20b",
        reasoning_effort="low",
        mock_response=mock_response
    )

    return {
        "status": "success",
        "query": query,
        "criterion_filter": criterion_filter,
        "answer": answer_text,
        "sources": sources,
        "chunks_retrieved_count": len(matched_chunks)
    }


def extract_structured_entities_from_document(
    document_text: str,
    target_criterion: str = "Criterion 3",
    mock_response: Optional[str] = None
) -> str:
    """
    Extract structured academic entities (e.g. COs, Bloom levels, SFR fields, research DOIs)
    from unstructured document text.
    """
    prompt = f"""
You are the Document Intelligence Agent in an
AI-Driven NBA Accreditation Readiness System.

Your responsibility is to extract structured accreditation information
for {target_criterion} from the document text provided below.

==================================================
EXTRACTION RULES
==================================================

1. Extract ONLY facts explicitly stated in the document text.
2. DO NOT invent course codes, names, percentages, or faculty designations.
3. If an entity is not mentioned, omit it or mark it as "Not specified in document".
4. Format the output cleanly with clear labels or JSON structure.

==================================================
DOCUMENT TEXT
==================================================

{document_text[:4000]}

==================================================
STRUCTURED EXTRACTED ENTITIES
==================================================
"""

    return call_model(
        prompt=prompt,
        max_output_tokens=1800,
        model="openai/gpt-oss-20b",
        reasoning_effort="low",
        mock_response=mock_response
    )
