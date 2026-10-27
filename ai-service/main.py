# main.py
"""
AI Service for NBA Accreditation Readiness System.

A multi-agent decision-support service for National Board of Accreditation (NBA)
evaluations covering Criteria 3, 4, 5, and 6.

Core Architectural Principles:
1. Deterministic Calculations in Python: Arithmetic and metrics are computed in Python.
2. Factually Bounded LLM Reasoning: The LLM organizes, contextualizes, and formats verified findings.
3. Decoupled Specialized Agents: Dedicated agents for assessment, student, faculty,
   coordination, compliance, reporting, and virtual inspection.
4. Data Integrity: Strict separation of confirmed evidence from pending records.
"""

from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.agents.assessment_agent import analyze_assessment
from app.agents.student_agent import (
    analyze_student_performance,
    analyze_criterion4_student_performance
)
from app.agents.faculty_agent import (
    analyze_faculty_information,
    analyze_faculty_contributions
)
from app.agents.coordinator_agent import (
    coordinate_criterion3,
    coordinate_department_readiness
)
from app.agents.compliance_agent import analyze_compliance_gaps
from app.agents.report_agent import generate_inspection_report
from app.agents.inspection_agent import (
    run_virtual_inspection_audit,
    query_inspection_cockpit
)
from app.agents.document_agent import (
    answer_document_query,
    extract_structured_entities_from_document
)
from app.rag.document_loader import load_document, load_directory
from app.rag.vector_store import default_vector_store
from app.services.metrics_service import evaluate_department_readiness


# ============================================================
# 1. CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="AI-Driven NBA Accreditation Readiness System",
    description="Multi-Agent AI Decision-Support Service for NBA Criteria 3, 4, 5, and 6",
    version="2.0.0"
)


# ============================================================
# 2. REQUEST & RESPONSE MODELS
# ============================================================

class Criterion3Request(BaseModel):
    data: Optional[Dict[str, Any]] = Field(default=None, description="Criterion 3 dataset (optional, uses default if None)")
    mock_response: Optional[str] = Field(default=None, description="Mock response for testing")


class Criterion4Request(BaseModel):
    data: Dict[str, Any] = Field(default_factory=dict, description="Criterion 4 cohorts, placements, and achievements data")
    mock_response: Optional[str] = Field(default=None, description="Mock response for testing")


class Criterion5Request(BaseModel):
    data: Dict[str, Any] = Field(default_factory=dict, description="Criterion 5 faculty roster and student intake data")
    mock_response: Optional[str] = Field(default=None, description="Mock response for testing")


class Criterion6Request(BaseModel):
    data: Dict[str, Any] = Field(default_factory=dict, description="Criterion 6 research publications, patents, projects, and FDPs")
    mock_response: Optional[str] = Field(default=None, description="Mock response for testing")


class DepartmentReadinessRequest(BaseModel):
    data: Dict[str, Any] = Field(default_factory=dict, description="Full department data covering criteria 3, 4, 5, 6")
    mock_response: Optional[str] = Field(default=None, description="Mock response for testing")


class ReportGenerationRequest(BaseModel):
    data: Dict[str, Any] = Field(default_factory=dict, description="Full department data covering criteria 3, 4, 5, 6")
    coordinator_summary: Optional[str] = Field(default=None, description="Optional Coordinator Agent summary")
    compliance_analysis: Optional[str] = Field(default=None, description="Optional Compliance Agent analysis")
    mock_response: Optional[str] = Field(default=None, description="Mock response for testing")


class InspectionQueryRequest(BaseModel):
    query: str = Field(..., description="Evaluator natural language query about department accreditation readiness")
    data: Dict[str, Any] = Field(default_factory=dict, description="Department accreditation evidence dataset")
    mock_response: Optional[str] = Field(default=None, description="Mock response for testing")


class RAGIngestRequest(BaseModel):
    file_path: str = Field(..., description="Path to document file (PDF, DOCX, TXT, MD, JSON)")
    criterion_tag: Optional[str] = Field(default=None, description="Optional NBA criterion tag (e.g. Criterion 3)")


class RAGQueryRequest(BaseModel):
    query: str = Field(..., description="User query against ingested documents")
    criterion_filter: Optional[str] = Field(default=None, description="Optional NBA criterion filter")
    top_k: int = Field(default=4, description="Number of passages to retrieve")
    mock_response: Optional[str] = Field(default=None, description="Mock response for testing")


class RAGExtractRequest(BaseModel):
    document_text: str = Field(..., description="Raw text of document")
    target_criterion: str = Field(default="Criterion 3", description="Target criterion for entity extraction")
    mock_response: Optional[str] = Field(default=None, description="Mock response for testing")


# ============================================================
# 3. ROOT & HEALTH ENDPOINTS
# ============================================================

@app.get("/")
def home():
    """
    Service health check and capabilities summary.
    """
    return {
        "service": "AI-Driven NBA Accreditation Readiness System",
        "status": "healthy",
        "version": "2.0.0",
        "agents": [
            "Assessment Agent (Criterion 3)",
            "Student Agent (Criteria 3 & 4)",
            "Faculty Agent (Criteria 5 & 6)",
            "Coordinator Agent (Multi-Criteria Synthesis)",
            "Compliance Agent (Gap Analysis & Rubrics)",
            "Report Agent (Inspection-Ready SAR Generator)",
            "Inspection Agent (Virtual Evaluator Digital Twin)",
            "Document Agent (RAG Intelligence & Ingestion)"
        ]
    }


# ============================================================
# 4. CRITERION 3 ENDPOINT
# ============================================================

@app.post("/criterion3/analyze")
def analyze_criterion3_endpoint(request: Criterion3Request):
    """
    Run complete Criterion 3 Course Outcomes & Assessment Analysis.
    """
    try:
        input_data = request.data if request.data else None

        assessment_result = analyze_assessment(
            data=input_data,
            mock_response=request.mock_response
        )
        student_result = analyze_student_performance(
            data=input_data,
            mock_response=request.mock_response
        )
        final_result = coordinate_criterion3(
            assessment_analysis=assessment_result,
            student_analysis=student_result,
            data=input_data,
            mock_response=request.mock_response
        )

        return {
            "criterion": "Criterion 3",
            "status": "success",
            "assessment_analysis": assessment_result,
            "student_analysis": student_result,
            "coordinated_analysis": final_result
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Criterion 3 analysis failed: {str(error)}")


# ============================================================
# 5. CRITERION 4 ENDPOINT
# ============================================================

@app.post("/criterion4/analyze")
def analyze_criterion4_endpoint(request: Criterion4Request):
    """
    Run Criterion 4 Student Performance, Academic Progression & Placements Analysis.
    """
    try:
        analysis_result = analyze_criterion4_student_performance(
            data=request.data,
            mock_response=request.mock_response
        )
        return {
            "criterion": "Criterion 4",
            "status": "success",
            "analysis": analysis_result
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Criterion 4 analysis failed: {str(error)}")


# ============================================================
# 6. CRITERION 5 ENDPOINT
# ============================================================

@app.post("/criterion5/analyze")
def analyze_criterion5_endpoint(request: Criterion5Request):
    """
    Run Criterion 5 Faculty Information, SFR & Cadre Analysis.
    """
    try:
        analysis_result = analyze_faculty_information(
            data=request.data,
            mock_response=request.mock_response
        )
        return {
            "criterion": "Criterion 5",
            "status": "success",
            "analysis": analysis_result
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Criterion 5 analysis failed: {str(error)}")


# ============================================================
# 7. CRITERION 6 ENDPOINT
# ============================================================

@app.post("/criterion6/analyze")
def analyze_criterion6_endpoint(request: Criterion6Request):
    """
    Run Criterion 6 Faculty Contributions, Research, Patents, Grants & FDPs Analysis.
    """
    try:
        analysis_result = analyze_faculty_contributions(
            data=request.data,
            mock_response=request.mock_response
        )
        return {
            "criterion": "Criterion 6",
            "status": "success",
            "analysis": analysis_result
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Criterion 6 analysis failed: {str(error)}")


# ============================================================
# 8. COORDINATOR SYNTHESIS ENDPOINT
# ============================================================

@app.post("/coordinator/department")
def coordinate_department_endpoint(request: DepartmentReadinessRequest):
    """
    Synthesize department findings across Criteria 3, 4, 5, and 6.
    """
    try:
        synthesis = coordinate_department_readiness(
            department_data=request.data,
            mock_response=request.mock_response
        )
        return {
            "status": "success",
            "coordinated_synthesis": synthesis
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Department coordination failed: {str(error)}")


# ============================================================
# 9. COMPLIANCE EVALUATION ENDPOINT
# ============================================================

@app.post("/compliance/evaluate")
def evaluate_compliance_endpoint(request: DepartmentReadinessRequest):
    """
    Run complete NBA compliance gap analysis across Criteria 3, 4, 5, and 6.
    """
    try:
        deterministic_eval = evaluate_department_readiness(request.data)
        analysis_result = analyze_compliance_gaps(
            department_data=request.data,
            mock_response=request.mock_response
        )
        return {
            "status": "success",
            "deterministic_metrics": deterministic_eval,
            "compliance_gap_analysis": analysis_result
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Compliance evaluation failed: {str(error)}")


# ============================================================
# 10. REPORT GENERATION ENDPOINT
# ============================================================

@app.post("/report/generate")
def generate_report_endpoint(request: ReportGenerationRequest):
    """
    Generate an inspection-ready Self-Assessment Report (SAR) in Markdown.
    """
    try:
        report_markdown = generate_inspection_report(
            department_data=request.data,
            coordinator_summary=request.coordinator_summary,
            compliance_analysis=request.compliance_analysis,
            mock_response=request.mock_response
        )
        return {
            "status": "success",
            "format": "github_flavored_markdown",
            "report_markdown": report_markdown
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Report generation failed: {str(error)}")


# ============================================================
# 11. INSPECTION COCKPIT ENDPOINTS
# ============================================================

@app.post("/inspection/audit")
def virtual_inspection_audit_endpoint(request: DepartmentReadinessRequest):
    """
    Run an end-to-end Virtual Inspection Cockpit audit for visiting evaluators.
    """
    try:
        audit_result = run_virtual_inspection_audit(
            department_data=request.data,
            mock_response=request.mock_response
        )
        return {
            "status": "success",
            "inspection_audit": audit_result
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Virtual inspection audit failed: {str(error)}")


@app.post("/inspection/query")
def virtual_inspection_query_endpoint(request: InspectionQueryRequest):
    """
    Interactive Q&A for NBA Evaluators against verified evidence.
    """
    try:
        answer = query_inspection_cockpit(
            query=request.query,
            department_data=request.data,
            mock_response=request.mock_response
        )
        return {
            "status": "success",
            "query": request.query,
            "answer": answer
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Inspection query failed: {str(error)}")


# ============================================================
# 12. RAG & DOCUMENT INTELLIGENCE ENDPOINTS
# ============================================================

@app.post("/rag/ingest")
def rag_ingest_document_endpoint(request: RAGIngestRequest):
    """
    Ingest a document file (PDF, DOCX, TXT, MD, JSON) into the vector store.
    """
    try:
        result = load_document(
            file_path=request.file_path,
            vector_store=default_vector_store,
            criterion_tag=request.criterion_tag
        )
        if result.get("status") == "error":
            raise HTTPException(status_code=400, detail=result.get("error"))
        return result
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Document ingestion failed: {str(error)}")


@app.post("/rag/query")
def rag_query_endpoint(request: RAGQueryRequest):
    """
    Grounded Question-Answering against ingested evidence documents with citations.
    """
    try:
        result = answer_document_query(
            query=request.query,
            criterion_filter=request.criterion_filter,
            vector_store=default_vector_store,
            top_k=request.top_k,
            mock_response=request.mock_response
        )
        return result
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"RAG query failed: {str(error)}")


@app.post("/rag/extract")
def rag_extract_endpoint(request: RAGExtractRequest):
    """
    Extract structured accreditation entities from raw document text.
    """
    try:
        extracted = extract_structured_entities_from_document(
            document_text=request.document_text,
            target_criterion=request.target_criterion,
            mock_response=request.mock_response
        )
        return {
            "status": "success",
            "target_criterion": request.target_criterion,
            "extracted_entities": extracted
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Entity extraction failed: {str(error)}")


@app.get("/rag/status")
def rag_status_endpoint():
    """
    Get current vector store index status and list of ingested documents.
    """
    return {
        "status": "active",
        "total_chunks_indexed": default_vector_store.get_total_chunks(),
        "indexed_documents": default_vector_store.get_indexed_files()
    }