# test_coordinator_multicriteria.py
"""
Unit and integration tests for Multi-Criteria Department Coordinator.
Validates synthesis across Criteria 3, 4, 5, and 6 without duplicate claims.
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

from app.agents.coordinator_agent import coordinate_department_readiness
from tests.fixtures.department_test_fixture import synthetic_department_fixture


def test_coordinator_department_readiness_mock():
    """Verify multi-criteria coordinator execution with mock response."""
    mock_synthesis = (
        "1. Consolidated Departmental Readiness Overview\n"
        "2. Criterion-wise Evidence Synthesis\n"
        "3. Cross-Criteria Consistency and Duplicate Checks\n"
        "4. Consolidated Audit Risks and Missing Evidence\n"
        "5. Unified Action Plan for Accreditation Visit"
    )

    result = coordinate_department_readiness(
        department_data=synthetic_department_fixture,
        criterion3_summary="Criterion 3 CO-PO mappings and assessment.",
        criterion4_summary="Criterion 4 cohort completion and placements.",
        criterion5_summary="Criterion 5 faculty roster and SFR 15.0.",
        criterion6_summary="Criterion 6 research grants and publications.",
        mock_response=mock_synthesis
    )

    assert "1. Consolidated Departmental Readiness Overview" in result
    assert "2. Criterion-wise Evidence Synthesis" in result
    assert "3. Cross-Criteria Consistency" in result
    assert "4. Consolidated Audit Risks" in result
    assert "5. Unified Action Plan" in result
