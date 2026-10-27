# test_compliance_agent.py
"""
Unit and integration tests for the NBA Compliance Gap Analysis Agent.
Validates deterministic scoring, gap classification, and agent output structure.
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

from app.services.metrics_service import (
    evaluate_criterion3_compliance,
    evaluate_criterion4_compliance,
    evaluate_criterion5_compliance,
    evaluate_criterion6_compliance,
    evaluate_department_readiness
)
from app.agents.compliance_agent import analyze_compliance_gaps
from tests.fixtures.department_test_fixture import synthetic_department_fixture


def test_deterministic_criterion3_compliance():
    """Verify Criterion 3 compliance evaluation and gap detection."""
    c3_data = synthetic_department_fixture["criterion3"]
    eval_result = evaluate_criterion3_compliance(c3_data)

    assert eval_result["criterion"] == "Criterion 3"
    assert eval_result["total_checks"] == 6
    assert eval_result["completeness_percentage"] > 0
    assert eval_result["gaps_count"] > 0

    # Official dataset has missing attainment formulas and missing SEE marks
    gap_ids = [g["id"] for g in eval_result["gaps"]]
    assert "C3-GAP-005" in gap_ids  # CO attainment formula missing
    assert "C3-GAP-006" in gap_ids  # SEE student marks missing


def test_deterministic_criterion4_compliance():
    """Verify Criterion 4 compliance evaluation."""
    c4_data = synthetic_department_fixture["criterion4"]
    eval_result = evaluate_criterion4_compliance(c4_data)

    assert eval_result["criterion"] == "Criterion 4"
    assert eval_result["completeness_percentage"] >= 60.0
    assert eval_result["status"] in ["Compliant", "Partially Compliant"]


def test_deterministic_criterion5_compliance():
    """Verify Criterion 5 compliance evaluation for SFR and Cadre."""
    c5_data = synthetic_department_fixture["criterion5"]
    eval_result = evaluate_criterion5_compliance(c5_data)

    assert eval_result["criterion"] == "Criterion 5"
    assert "sfr_metrics" in eval_result
    assert "cadre_metrics" in eval_result
    assert eval_result["sfr_metrics"]["student_to_faculty_ratio"] == 15.0  # 180 / 12


def test_deterministic_criterion6_compliance():
    """Verify Criterion 6 compliance evaluation for Research and Patents."""
    c6_data = synthetic_department_fixture["criterion6"]
    eval_result = evaluate_criterion6_compliance(c6_data)

    assert eval_result["criterion"] == "Criterion 6"
    assert "publication_metrics" in eval_result
    assert "patent_metrics" in eval_result


def test_evaluate_department_readiness_synthesis():
    """Verify composite readiness score and gap categorization."""
    readiness = evaluate_department_readiness(synthetic_department_fixture)

    assert "composite_readiness_score" in readiness
    assert 0.0 <= readiness["composite_readiness_score"] <= 100.0
    assert readiness["overall_status"] in ["Compliant", "Partially Compliant", "Non-Compliant"]
    assert "readiness_verdict" in readiness

    gap_summary = readiness["gap_summary"]
    assert gap_summary["total_gaps"] > 0
    assert gap_summary["critical_count"] >= 0
    assert gap_summary["major_count"] >= 0
    assert gap_summary["minor_count"] >= 0


def test_compliance_agent_mock():
    """Verify Compliance Agent output formatting using mock response."""
    mock_response = (
        "SECTION 1: Executive Compliance Summary\n"
        "SECTION 2: Criterion-by-Criterion Compliance Evaluation\n"
        "SECTION 3: Critical and Major Gap Matrix\n"
        "SECTION 4: Evidence Verification Shortfalls\n"
        "SECTION 5: Prioritized Remediation Action Plan"
    )

    result = analyze_compliance_gaps(
        synthetic_department_fixture,
        mock_response=mock_response
    )

    assert "SECTION 1" in result
    assert "Executive Compliance Summary" in result
    assert "SECTION 3" in result
    assert "Critical and Major Gap Matrix" in result
    assert "SECTION 5" in result
