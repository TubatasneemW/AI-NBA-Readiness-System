# AI-Driven NBA Accreditation Readiness System

An advanced **Multi-Agent Decision-Support and Virtual Inspection System** designed for engineering institutions preparing for **National Board of Accreditation (NBA)** evaluations across Criteria 3, 4, 5, and 6.

---

## 🏛️ Core Architectural Principles

1. **Deterministic Calculations in Python**: Mathematical metrics (SFR, Cadre Ratio, Ph.D. percentages, graduation rates, placement percentages, and funding sums) are strictly computed in Python via `metrics_service.py`. Generative LLMs are **never permitted to do arithmetic or hallucinate numbers**.
2. **Factually Bounded LLM Reasoning**: The Language Model (via Groq / OpenAI compatible API) is used strictly to contextualize, explain, and assemble verified findings into auditable sections.
3. **Multi-Format RAG Ingestion**: Ingests unstructured academic evidence (PDF syllabi, Word documents, appointment orders, and research reprints) with provenance citation grounding.
4. **Data Integrity & Traceability**: Explicitly differentiates confirmed achievements from pending records to prevent audit penalties.

---

## 🤖 Multi-Agent Architecture

| Agent | Module | Criterion | Responsibility |
| :--- | :--- | :--- | :--- |
| **Assessment Agent** | `assessment_agent.py` | Criterion 3 | Course outcomes (COs), assessment scheme coverage, Bloom's cognitive levels, CO-PO-PSO mapping. |
| **Student Agent** | `student_agent.py` | Criterion 3 & 4 | Student academic progression, CIE distributions, graduation rates without backlog, placement rates, higher education. |
| **Faculty Agent** | `faculty_agent.py` | Criterion 5 & 6 | Faculty qualifications, Student-to-Faculty Ratio (SFR), cadre distribution, teaching experience, research papers, patents, grants, consultancy, and FDPs. |
| **Coordinator Agent** | `coordinator_agent.py` | Multi-Criteria | Synthesizes Criteria 3, 4, 5, and 6 findings into a unified departmental summary, resolving duplicate claims and enforcing consistency. |
| **Compliance Agent** | `compliance_agent.py` | NBA Rubrics | Evaluates institutional data against NBA SAR rubrics; categorizes Critical, Major, and Minor gaps; computes completeness percentages. |
| **Report Agent** | `report_agent.py` | SAR Reporting | Formats inspection-ready Self-Assessment Reports (SAR) in GitHub Flavored Markdown with clean tables and audit appendices. |
| **Inspection Agent** | `inspection_agent.py` | Digital Twin | Evaluator cockpit for visiting peer reviewers; computes evidence verification ratios, flags on-site audit risks, and answers queries. |
| **Document Agent (RAG)** | `document_agent.py` | Document Intelligence | Grounded Q&A and structured entity extraction from uploaded evidence files with exact source citations (`[Source: file.pdf, Page: X]`). |

---

## 📚 RAG Pipeline Architecture (`ai-service/app/rag/`)

```
Document (PDF / DOCX / TXT / JSON)
               │
               ▼
   [text_extractor.py]  ──▶ Normalization & layout preservation
               │
               ▼
      [chunker.py]       ──▶ Page-aware semantic chunks with overlap
               │
               ▼
     [embeddings.py]     ──▶ Deterministic TF-IDF vectors / API embeddings
               │
               ▼
    [vector_store.py]    ──▶ In-memory cosine similarity index & criterion filter
               │
               ▼
     [retriever.py]      ──▶ Top-k context retrieval with provenance tags
               │
               ▼
   [document_agent.py]   ──▶ Grounded Q&A & structured extraction
```

---

## 🚀 Running the AI Service

### 1. Install Dependencies
```bash
cd ai-service
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Copy `.env.example` to `ai-service/.env`:
```env
GROQ_API_KEY="your_groq_api_key_here"
```

### 3. Start the FastAPI Service
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Interactive Swagger documentation is available at: `http://localhost:8000/docs`

---

## 📡 REST API Reference for Backend & Frontend Teammates

### Criteria Analysis Endpoints
- `POST /criterion3/analyze`: Course Outcomes, assessment coverage, and CIE statistics.
- `POST /criterion4/analyze`: Student graduation rates, placement percentages, and achievements.
- `POST /criterion5/analyze`: Faculty roster, SFR calculation, cadre ratio, and experience.
- `POST /criterion6/analyze`: Publications (SCI/Scopus), patents, grants, consultancy, and FDPs.

### Synthesis & Evaluation Endpoints
- `POST /coordinator/department`: Synthesizes Criteria 3, 4, 5, and 6 into a unified departmental audit summary.
- `POST /compliance/evaluate`: Complete NBA gap analysis with Critical, Major, and Minor severity classification.
- `POST /report/generate`: Full inspection-ready Self-Assessment Report in GitHub Flavored Markdown.

### Virtual Inspection Cockpit Endpoints
- `POST /inspection/audit`: End-to-end evidence verification ratios and on-site audit checklist.
- `POST /inspection/query`: Evaluator Q&A against verified department evidence.

### RAG & Document Intelligence Endpoints
- `POST /rag/ingest`: Ingest a file (`.pdf`, `.docx`, `.txt`, `.json`) into the vector index.
- `POST /rag/query`: Semantic retrieval with source citations.
- `POST /rag/extract`: Automated extraction of structured academic entities from text.
- `GET /rag/status`: Number of indexed chunks and files.

---

## 🧪 Running the Automated Test Suite

The test suite validates all 8 agents, deterministic mathematics, the RAG pipeline, and FastAPI routes:
```bash
pytest -v
```
**Test Results: 51 / 51 passed (100% pass rate)**
