# document_loader.py
"""
Document Loader and Ingestion Coordinator for NBA Evidence Files.

Loads files from local paths or upload directories, automatically classifies
evidence by NBA criterion, extracts and chunks text, and indexes into the vector store.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

from app.rag.text_extractor import extract_document_text
from app.rag.chunker import chunk_document
from app.rag.vector_store import InMemoryVectorStore, default_vector_store


def detect_criterion_from_content(text: str, filename: str) -> str:
    """
    Heuristically tag the document by NBA Criterion based on filename and text keywords.
    """
    combined = (filename + " " + text[:3000]).lower()

    # Criterion 3: Course Outcomes & Assessment
    c3_keywords = [
        "course outcome", "syllabus", "bloom", "co1", "co2", "co3",
        "cie-i", "cie-ii", "semester end", "internal test", "course articulation",
        "co-po", "pso"
    ]
    if any(k in combined for k in c3_keywords):
        return "Criterion 3"

    # Criterion 4: Student Performance & Progression
    c4_keywords = [
        "placement", "higher studies", "cohort", "admitted", "graduated",
        "backlog", "median salary", "offer letter", "hackathon", "student achievement"
    ]
    if any(k in combined for k in c4_keywords):
        return "Criterion 4"

    # Criterion 5: Faculty Information & Cadre
    c5_keywords = [
        "faculty", "professor", "associate professor", "assistant professor",
        "appointment order", "joining report", "student-to-faculty", "sfr",
        "ph.d notification", "cadre", "workload distribution"
    ]
    if any(k in combined for k in c5_keywords):
        return "Criterion 5"

    # Criterion 6: Research, Patents, Grants & FDPs
    c6_keywords = [
        "scopus", "sci", "scie", "patent", "sanction order", "research grant",
        "consultancy", "fdp", "sttp", "nptel", "ugc-care", "doi.org"
    ]
    if any(k in combined for k in c6_keywords):
        return "Criterion 6"

    return "General"


def load_document(
    file_path: str,
    vector_store: Optional[InMemoryVectorStore] = None,
    criterion_tag: Optional[str] = None,
    chunk_size: int = 600,
    chunk_overlap: int = 100
) -> Dict[str, Any]:
    """
    Ingest a single document file into the vector store.
    """
    if vector_store is None:
        vector_store = default_vector_store

    extracted = extract_document_text(file_path)
    if extracted.get("status") == "error":
        return extracted

    # Auto-detect criterion tag if not explicitly specified
    if not criterion_tag:
        criterion_tag = detect_criterion_from_content(
            text=extracted.get("full_text", ""),
            filename=extracted.get("filename", "")
        )

    extracted["criterion_tag"] = criterion_tag

    # Chunk the document
    chunks = chunk_document(
        extracted_doc=extracted,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    # Index into vector store
    indexed_count = vector_store.add_chunks(chunks)

    return {
        "status": "success",
        "filename": extracted.get("filename"),
        "file_path": extracted.get("file_path"),
        "file_type": extracted.get("file_type"),
        "criterion_tag": criterion_tag,
        "total_pages": extracted.get("total_pages", 1),
        "total_chunks_created": len(chunks),
        "total_chunks_indexed": indexed_count,
        "full_text_character_count": len(extracted.get("full_text", ""))
    }


def load_directory(
    directory_path: str,
    vector_store: Optional[InMemoryVectorStore] = None,
    recursive: bool = True
) -> Dict[str, Any]:
    """
    Ingest all supported documents in a directory.
    """
    dir_path = Path(directory_path)
    if not dir_path.exists() or not dir_path.is_dir():
        return {
            "status": "error",
            "error": f"Directory does not exist: {directory_path}",
            "processed_files": []
        }

    supported_extensions = [".pdf", ".docx", ".txt", ".md", ".json", ".csv"]
    pattern = "**/*" if recursive else "*"
    files_to_load = [
        p for p in dir_path.glob(pattern)
        if p.is_file() and p.suffix.lower() in supported_extensions
    ]

    processed = []
    total_chunks = 0

    for file_path in files_to_load:
        res = load_document(str(file_path), vector_store=vector_store)
        if res.get("status") == "success":
            total_chunks += res.get("total_chunks_indexed", 0)
            processed.append(res)

    return {
        "status": "success",
        "directory": str(dir_path),
        "total_files_discovered": len(files_to_load),
        "total_files_ingested": len(processed),
        "total_chunks_indexed": total_chunks,
        "processed_files": processed
    }
