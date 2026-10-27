# test_inspection_agent.py
"""
Unit and integration tests for the Virtual Inspection Digital Twin Agent.
Validates verification ratio calculation, inspection audit, and evaluator Q&A cockpit.
"""

import sys
from pathlib import Path

# Add project root and ai-service to sys.path
root_path = Path(__file__).resolve().parent.parent.parent
ai_service_path = root_path / "ai-service"
if str(ai_service_path) not in sys.path:
    sys.path.insert(0, str(ai_service_path))
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from app.agents.inspection_agent import (
    calculate_inspection_verification_ratios,
    run_virtual_inspection_audit,
    query_inspection_cockpit
)
from tests.fixtures.department_test_fixture import synthetic_department_fixture


def test_inspection_verification_ratios():
    """Verify deterministic calculation of evidence verification ratios."""
    metrics = calculate_inspection_verification_ratios(synthetic_department_fixture)

    assert metrics["grand_total_submissions"] > 0
    assert metrics["grand_total_verified"] > 0
    assert metrics["grand_total_pending"] >= 0
    assert 0.0 <= metrics["overall_verification_ratio_pct"] <= 100.0

    breakdown = metrics["category_breakdown"]
    assert "faculty_profiles" in breakdown
    assert "student_achievements" in breakdown
    assert "publications" in breakdown
    assert "patents" in breakdown
    assert "sponsored_projects" in breakdown
    assert "consultancy" in breakdown
    assert "fdps" in breakdown

    # Faculty: 12 faculty in synthetic_criterion5_fixture (11 verified, 1 pending)
    assert breakdown["faculty_profiles"]["total"] == 12
    assert breakdown["faculty_profiles"]["verified"] == 11
    assert breakdown["faculty_profiles"]["pending"] == 1

    # Publications: 5 total in synthetic_criterion6_fixture, 4 verified, 1 pending
    assert breakdown["publications"]["total"] == 5
    assert breakdown["publications"]["verified"] == 4
    assert breakdown["publications"]["pending"] == 1


def test_virtual_inspection_audit_mock():
    """Verify Virtual Inspection Audit generation with mock response."""
    mock_audit = (
        "SECTION 1: Virtual Inspection Cockpit Overview\n"
        "SECTION 2: Documentary Evidence Verification Audit\n"
        "SECTION 3: Evaluator Red Flags & High-Risk Areas\n"
        "SECTION 4: On-Site Physical Inspection Checklist\n"
        "SECTION 5: Evaluator Recommendations"
    )

    result = run_virtual_inspection_audit(
        department_data=synthetic_department_fixture,
        mock_response=mock_audit
    )

    assert "SECTION 1" in result
    assert "Virtual Inspection Cockpit Overview" in result
    assert "SECTION 3" in result
    assert "Evaluator Red Flags & High-Risk Areas" in result
    assert "SECTION 4" in result
    assert "On-Site Physical Inspection Checklist" in result


def test_query_inspection_cockpit_mock():
    """Verify Evaluator Cockpit Q&A query answering with mock response."""
    mock_answer = "The verified Student-to-Faculty Ratio (SFR) is 15.0:1 across 180 students and 12 faculty members."

    result = query_inspection_cockpit(
        query="What is the department's Student-to-Faculty Ratio (SFR)?",
        department_data=synthetic_department_fixture,
        mock_response=mock_answer
    )

    assert "Student-to-Faculty Ratio" in result
    assert "15.0:1" in result
