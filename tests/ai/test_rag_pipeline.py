# test_rag_pipeline.py
"""
Unit and integration tests for the NBA RAG (Retrieval-Augmented Generation) pipeline
and Document Intelligence Agent.
Validates text extraction, chunking, embeddings, vector search, retriever provenance,
and Document Agent query execution.
"""

import sys
from pathlib import Path
from fastapi.testclient import TestClient

# Add project root and ai-service to sys.path
root_path = Path(__file__).resolve().parent.parent.parent
ai_service_path = root_path / "ai-service"
if str(ai_service_path) not in sys.path:
    sys.path.insert(0, str(ai_service_path))
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from app.rag.text_extractor import extract_document_text, clean_extracted_text
from app.rag.chunker import split_text_into_chunks, chunk_document
from app.rag.embeddings import (
    LocalTFIDFEmbedder,
    compute_cosine_similarity,
    compute_batch_cosine_similarities
)
from app.rag.vector_store import InMemoryVectorStore, default_vector_store
from app.rag.document_loader import (
    detect_criterion_from_content,
    load_document,
    load_directory
)
from app.rag.retriever import (
    retrieve_relevant_chunks,
    format_retrieved_context_for_prompt,
    get_retrieved_sources_summary
)
from app.agents.document_agent import (
    answer_document_query,
    extract_structured_entities_from_document
)
from main import app

client = TestClient(app)


def test_clean_extracted_text():
    """Verify whitespace normalization and control character stripping."""
    raw = "  Course   Outcomes  \r\n\r\n\r\n\r\nBloom Taxonomy:   L3 \t\t Level  "
    cleaned = clean_extracted_text(raw)
    assert cleaned == "Course Outcomes\n\nBloom Taxonomy: L3 Level"


def test_text_extractor_sample_files():
    """Verify multi-format extraction from local sample documents."""
    sample_file = root_path / "documents" / "sample" / "sample_syllabus_criterion3.txt"
    res = extract_document_text(str(sample_file))

    assert res["status"] == "success"
    assert res["filename"] == "sample_syllabus_criterion3.txt"
    assert "MACHINE LEARNING ALGORITHMS" in res["full_text"]
    assert "CO1" in res["full_text"]
    assert len(res["pages"]) >= 1


def test_chunker_splitting_and_overlap():
    """Verify intelligent text chunking with overlap."""
    sample_text = (
        "Paragraph 1 discusses Course Outcomes and Bloom taxonomy alignment.\n\n"
        "Paragraph 2 discusses continuous internal evaluation CIE-I and CIE-II.\n\n"
        "Paragraph 3 details semester end examination SEE component weightages."
    )
    chunks = split_text_into_chunks(sample_text, chunk_size=120, chunk_overlap=30)

    assert len(chunks) >= 2
    for c in chunks:
        assert "text" in c
        assert "chunk_index" in c
        assert len(c["text"]) > 0


def test_embeddings_and_cosine_similarity():
    """Verify deterministic TF-IDF embeddings and cosine similarity."""
    embedder = LocalTFIDFEmbedder()
    corpus = [
        "Faculty cadre ratio and student to faculty ratio SFR in engineering departments.",
        "Machine learning algorithms course outcomes and assessment scheme.",
        "Sponsored research funding grants from DST and industrial consultancy."
    ]
    embedder.fit(corpus)
    matrix = embedder.transform(corpus)

    assert matrix.shape[0] == 3
    assert matrix.shape[1] > 0

    query_vec = embedder.embed_query("What is the faculty SFR?")
    sims = compute_batch_cosine_similarities(query_vec, matrix)

    # First document is about faculty and SFR, so its similarity should be highest
    assert sims[0] > sims[1]
    assert sims[0] > sims[2]


def test_auto_criterion_detection():
    """Verify heuristic classification into NBA criteria."""
    assert detect_criterion_from_content("course outcome syllabus bloom co1", "syllabus.pdf") == "Criterion 3"
    assert detect_criterion_from_content("placement higher studies median salary offer letter", "placements.pdf") == "Criterion 4"
    assert detect_criterion_from_content("professor designation appointment student-to-faculty", "faculty.pdf") == "Criterion 5"
    assert detect_criterion_from_content("scopus sci research grant patent sanction order", "grant.pdf") == "Criterion 6"
    assert detect_criterion_from_content("miscellaneous campus facilities", "notes.txt") == "General"


def test_vector_store_and_loader_end_to_end():
    """Verify document ingestion and semantic search in an isolated vector store."""
    store = InMemoryVectorStore()
    sample_dir = root_path / "documents" / "sample"

    ingest_res = load_directory(str(sample_dir), vector_store=store)
    assert ingest_res["status"] == "success"
    assert ingest_res["total_files_ingested"] >= 3
    assert store.get_total_chunks() > 0

    # Query 1: Syllabus & COs
    results_c3 = store.similarity_search("What are the course outcomes?", top_k=2)
    assert len(results_c3) > 0
    assert any("CO" in r["text"] or "COURSE" in r["text"] for r in results_c3)

    # Query 2: Research Grant
    results_c6 = store.similarity_search("DST research funding grant amount", top_k=2)
    assert len(results_c6) > 0
    assert any("DST" in r["text"] or "Lakhs" in r["text"] for r in results_c6)


def test_retriever_formatting():
    """Verify retrieved context formatting and provenance citations."""
    mock_chunks = [
        {
            "text": "CO1: Understand mathematical foundations of linear regression.",
            "source_file": "sample_syllabus_criterion3.txt",
            "page_number": 1,
            "criterion_tag": "Criterion 3",
            "score": 0.88
        }
    ]
    formatted = format_retrieved_context_for_prompt(mock_chunks)
    assert "[EVIDENCE PASSAGE 1]" in formatted
    assert "sample_syllabus_criterion3.txt" in formatted
    assert "Criterion 3" in formatted

    sources = get_retrieved_sources_summary(mock_chunks)
    assert len(sources) == 1
    assert sources[0]["source_file"] == "sample_syllabus_criterion3.txt"


def test_document_agent_query_mock():
    """Verify Document Agent RAG query execution with mock response."""
    store = InMemoryVectorStore()
    syllabus_file = root_path / "documents" / "sample" / "sample_syllabus_criterion3.txt"
    load_document(str(syllabus_file), vector_store=store)

    mock_answer = (
        "Based on [Source: sample_syllabus_criterion3.txt, Page: 1], the assessment scheme "
        "comprises 50 marks Continuous Internal Evaluation (CIE) and 50 marks Semester End Examination (SEE)."
    )

    rag_result = answer_document_query(
        query="What is the assessment scheme weightage?",
        vector_store=store,
        mock_response=mock_answer
    )

    assert rag_result["status"] == "success"
    assert "Based on [Source: sample_syllabus_criterion3.txt" in rag_result["answer"]
    assert rag_result["chunks_retrieved_count"] > 0
    assert len(rag_result["sources"]) > 0


def test_document_agent_extract_mock():
    """Verify Document Agent structured entity extraction with mock response."""
    mock_entities = (
        "{\n"
        '  "course_code": "22UAI608C",\n'
        '  "course_name": "Machine Learning Algorithms",\n'
        '  "co_count": 4\n'
        "}"
    )

    extracted = extract_structured_entities_from_document(
        document_text="Course: Machine Learning Algorithms (22UAI608C). CO1, CO2, CO3, CO4 defined.",
        target_criterion="Criterion 3",
        mock_response=mock_entities
    )

    assert "22UAI608C" in extracted
    assert "Machine Learning Algorithms" in extracted


def test_fastapi_rag_endpoints():
    """Verify FastAPI /rag/* REST API endpoints."""
    # 1. Status endpoint
    status_resp = client.get("/rag/status")
    assert status_resp.status_code == 200
    assert status_resp.json()["status"] == "active"

    # 2. Ingest endpoint
    syllabus_file = root_path / "documents" / "sample" / "sample_syllabus_criterion3.txt"
    ingest_resp = client.post(
        "/rag/ingest",
        json={
            "file_path": str(syllabus_file),
            "criterion_tag": "Criterion 3"
        }
    )
    assert ingest_resp.status_code == 200
    assert ingest_resp.json()["status"] == "success"

    # 3. Query endpoint
    query_resp = client.post(
        "/rag/query",
        json={
            "query": "What are the course outcomes?",
            "criterion_filter": "Criterion 3",
            "mock_response": "CO1 through CO4 are detailed in [Source: sample_syllabus_criterion3.txt]."
        }
    )
    assert query_resp.status_code == 200
    assert query_resp.json()["status"] == "success"
    assert "sample_syllabus_criterion3.txt" in query_resp.json()["answer"]

    # 4. Extract endpoint
    extract_resp = client.post(
        "/rag/extract",
        json={
            "document_text": "Sample text for extraction",
            "target_criterion": "Criterion 3",
            "mock_response": "Extracted Entities Mock"
        }
    )
    assert extract_resp.status_code == 200
    assert extract_resp.json()["status"] == "success"
    assert "Extracted Entities Mock" in extract_resp.json()["extracted_entities"]
