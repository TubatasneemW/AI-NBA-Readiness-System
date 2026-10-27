# test_api_endpoints.py
"""
Integration tests for FastAPI REST API endpoints in ai-service/main.py.
Tests all endpoints using FastAPI TestClient with mock responses.
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

from main import app
from tests.fixtures.department_test_fixture import synthetic_department_fixture

client = TestClient(app)


def test_home_endpoint():
    """Verify health check and agent listing endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "agents" in data
    assert len(data["agents"]) >= 7


def test_criterion3_analyze_endpoint():
    """Verify POST /criterion3/analyze endpoint."""
    response = client.post(
        "/criterion3/analyze",
        json={
            "data": {},
            "mock_response": "Mock Criterion 3 Coordinated Analysis"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["criterion"] == "Criterion 3"
    assert data["status"] == "success"
    assert "coordinated_analysis" in data


def test_criterion4_analyze_endpoint():
    """Verify POST /criterion4/analyze endpoint."""
    response = client.post(
        "/criterion4/analyze",
        json={
            "data": synthetic_department_fixture["criterion4"],
            "mock_response": "Mock Criterion 4 Student Performance Analysis"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["criterion"] == "Criterion 4"
    assert data["status"] == "success"
    assert "analysis" in data


def test_criterion5_analyze_endpoint():
    """Verify POST /criterion5/analyze endpoint."""
    response = client.post(
        "/criterion5/analyze",
        json={
            "data": synthetic_department_fixture["criterion5"],
            "mock_response": "Mock Criterion 5 Faculty Analysis"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["criterion"] == "Criterion 5"
    assert data["status"] == "success"
    assert "analysis" in data


def test_criterion6_analyze_endpoint():
    """Verify POST /criterion6/analyze endpoint."""
    response = client.post(
        "/criterion6/analyze",
        json={
            "data": synthetic_department_fixture["criterion6"],
            "mock_response": "Mock Criterion 6 Faculty Contributions Analysis"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["criterion"] == "Criterion 6"
    assert data["status"] == "success"
    assert "analysis" in data


def test_coordinator_department_endpoint():
    """Verify POST /coordinator/department endpoint."""
    response = client.post(
        "/coordinator/department",
        json={
            "data": synthetic_department_fixture,
            "mock_response": "Mock Coordinated Department Readiness Synthesis"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "coordinated_synthesis" in data


def test_compliance_evaluate_endpoint():
    """Verify POST /compliance/evaluate endpoint."""
    response = client.post(
        "/compliance/evaluate",
        json={
            "data": synthetic_department_fixture,
            "mock_response": "Mock Compliance Gap Analysis"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "deterministic_metrics" in data
    assert "compliance_gap_analysis" in data


def test_report_generate_endpoint():
    """Verify POST /report/generate endpoint."""
    response = client.post(
        "/report/generate",
        json={
            "data": synthetic_department_fixture,
            "mock_response": "# Mock NBA Inspection Report\n\n## 1. Executive Summary"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["format"] == "github_flavored_markdown"
    assert "report_markdown" in data


def test_inspection_audit_endpoint():
    """Verify POST /inspection/audit endpoint."""
    response = client.post(
        "/inspection/audit",
        json={
            "data": synthetic_department_fixture,
            "mock_response": "Mock Virtual Inspection Cockpit Audit"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "inspection_audit" in data


def test_inspection_query_endpoint():
    """Verify POST /inspection/query endpoint."""
    response = client.post(
        "/inspection/query",
        json={
            "query": "What is the department SFR?",
            "data": synthetic_department_fixture,
            "mock_response": "The department SFR is 15.0:1."
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "answer" in data
    assert data["answer"] == "The department SFR is 15.0:1."
