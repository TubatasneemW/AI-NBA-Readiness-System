# test_report_agent.py
"""
Unit and integration tests for the NBA Accreditation Report Agent.
Validates report compilation and GFM markdown document generation.
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

from app.agents.report_agent import generate_inspection_report
from tests.fixtures.department_test_fixture import synthetic_department_fixture


def test_report_agent_mock():
    """Verify inspection report generation with mock response."""
    mock_report = (
        "# NBA Self-Assessment Readiness Dossier\n\n"
        "## 1. Executive Summary & Readiness Verdict\n\n"
        "## 2. Criterion 5: Faculty Profile & Academic Cadre\n\n"
        "## 3. Criterion 4: Student Academic Performance & Placement\n\n"
        "## 4. Criterion 6: Research, Innovations & Faculty Development\n\n"
        "## 5. Compliance Gap Analysis Matrix\n\n"
        "## 6. Limitations, Pending Proofs & Verification Appendix\n"
    )

    result = generate_inspection_report(
        department_data=synthetic_department_fixture,
        coordinator_summary="Coordinated summary of department data.",
        compliance_analysis="Compliance gap findings.",
        mock_response=mock_report
    )

    assert "# NBA Self-Assessment Readiness Dossier" in result
    assert "## 1. Executive Summary & Readiness Verdict" in result
    assert "## 2. Criterion 5: Faculty Profile & Academic Cadre" in result
    assert "## 3. Criterion 4: Student Academic Performance & Placement" in result
    assert "## 4. Criterion 6: Research, Innovations & Faculty Development" in result
    assert "## 5. Compliance Gap Analysis Matrix" in result
    assert "## 6. Limitations, Pending Proofs & Verification Appendix" in result
