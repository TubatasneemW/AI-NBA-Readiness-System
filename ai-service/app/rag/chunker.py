# chunker.py
"""
Intelligent Text Chunker for NBA Accreditation Evidence Documents.

Splits extracted document texts into semantically coherent chunks with overlap,
preserving document metadata, page numbers, and section headers.
"""

import re
from typing import Any, Dict, List, Optional


def split_text_into_chunks(
    text: str,
    chunk_size: int = 600,
    chunk_overlap: int = 100,
    base_metadata: Optional[Dict[str, Any]] = None
) -> List[Dict[str, Any]]:
    """
    Split text into chunks of roughly `chunk_size` characters with `chunk_overlap`.
    Tries to split on paragraph or sentence boundaries rather than cutting words in half.
    """
    if not text or not text.strip():
        return []

    if base_metadata is None:
        base_metadata = {}

    cleaned = text.strip()

    # If text is already shorter than chunk size, return single chunk
    if len(cleaned) <= chunk_size:
        chunk = {
            "chunk_index": 0,
            "text": cleaned,
            "char_length": len(cleaned),
            **base_metadata
        }
        return [chunk]

    # Split into paragraphs or sections
    paragraphs = re.split(r"\n\n+", cleaned)
    chunks: List[Dict[str, Any]] = []

    current_chunk_parts: List[str] = []
    current_length = 0

    for para in paragraphs:
        para_clean = para.strip()
        if not para_clean:
            continue

        # If a single paragraph is longer than chunk_size, split by sentences
        if len(para_clean) > chunk_size:
            sentences = re.split(r"(?<=[.!?])\s+", para_clean)
            for sentence in sentences:
                sent_len = len(sentence)
                if current_length + sent_len > chunk_size and current_chunk_parts:
                    chunk_text = " ".join(current_chunk_parts).strip()
                    chunks.append({
                        "chunk_index": len(chunks),
                        "text": chunk_text,
                        "char_length": len(chunk_text),
                        **base_metadata
                    })
                    # Overlap: keep last part if possible
                    overlap_parts = []
                    overlap_len = 0
                    for part in reversed(current_chunk_parts):
                        if overlap_len + len(part) <= chunk_overlap:
                            overlap_parts.insert(0, part)
                            overlap_len += len(part)
                        else:
                            break
                    current_chunk_parts = overlap_parts + [sentence]
                    current_length = sum(len(p) for p in current_chunk_parts) + len(current_chunk_parts)
                else:
                    current_chunk_parts.append(sentence)
                    current_length += sent_len + 1
        else:
            para_len = len(para_clean)
            if current_length + para_len > chunk_size and current_chunk_parts:
                chunk_text = "\n\n".join(current_chunk_parts).strip()
                chunks.append({
                    "chunk_index": len(chunks),
                    "text": chunk_text,
                    "char_length": len(chunk_text),
                    **base_metadata
                })
                # Overlap logic
                current_chunk_parts = [para_clean]
                current_length = para_len
            else:
                current_chunk_parts.append(para_clean)
                current_length += para_len + 2

    if current_chunk_parts:
        final_text = "\n\n".join(current_chunk_parts).strip()
        if final_text:
            chunks.append({
                "chunk_index": len(chunks),
                "text": final_text,
                "char_length": len(final_text),
                **base_metadata
            })

    return chunks


def chunk_document(
    extracted_doc: Dict[str, Any],
    chunk_size: int = 600,
    chunk_overlap: int = 100
) -> List[Dict[str, Any]]:
    """
    Chunk an entire extracted document structure with page-aware metadata.
    """
    filename = extracted_doc.get("filename", "unknown_document")
    file_path = extracted_doc.get("file_path", "")
    criterion_tag = extracted_doc.get("criterion_tag", "General")
    pages = extracted_doc.get("pages", [])

    all_chunks: List[Dict[str, Any]] = []

    if pages:
        for p in pages:
            page_num = p.get("page_number", 1)
            page_text = p.get("text", "")
            if not page_text.strip():
                continue

            page_meta = {
                "source_file": filename,
                "file_path": file_path,
                "page_number": page_num,
                "criterion_tag": criterion_tag
            }

            page_chunks = split_text_into_chunks(
                text=page_text,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                base_metadata=page_meta
            )

            for chunk in page_chunks:
                chunk["chunk_id"] = f"{filename}_p{page_num}_c{chunk['chunk_index']}"
                all_chunks.append(chunk)
    else:
        full_text = extracted_doc.get("full_text", "")
        base_meta = {
            "source_file": filename,
            "file_path": file_path,
            "page_number": 1,
            "criterion_tag": criterion_tag
        }
        all_chunks = split_text_into_chunks(
            text=full_text,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            base_metadata=base_meta
        )
        for chunk in all_chunks:
            chunk["chunk_id"] = f"{filename}_c{chunk['chunk_index']}"

    return all_chunks
