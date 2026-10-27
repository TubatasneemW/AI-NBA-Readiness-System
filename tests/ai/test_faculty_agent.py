# test_faculty_agent.py
"""
Unit tests for Criterion 5 Faculty Information Analysis.
Verifies SFR calculations, Cadre Ratio, Ph.D. percentage, PII sanitization,
and Faculty Agent execution using the synthetic test fixture.
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
    calculate_criterion5_sfr,
    calculate_criterion5_cadre_metrics,
    calculate_criterion5_experience_metrics
)
from app.utils.privacy_utils import sanitize_faculty_data
from app.agents.faculty_agent import analyze_faculty_information
from tests.fixtures.criterion5_test_fixture import synthetic_criterion5_fixture


def test_sfr_calculation():
    """Verify deterministic Student-to-Faculty Ratio (SFR) calculation."""
    total_students = synthetic_criterion5_fixture["total_enrolled_students"]
    faculty_count = len(synthetic_criterion5_fixture["faculty_members"])

    # 180 students / 12 faculty = 15.0
    res = calculate_criterion5_sfr(total_students, faculty_count)
    assert res["sfr_ratio"] == 15.0
    assert res["sfr_display"] == "15.0:1"
    assert res["regular_faculty_count"] == 12

    # Zero faculty edge case
    zero_res = calculate_criterion5_sfr(180, 0)
    assert zero_res["sfr_ratio"] is None
    assert "error" in zero_res


def test_cadre_ratio_and_qualifications():
    """Verify deterministic Cadre Ratio and Ph.D. percentage calculations."""
    faculty = synthetic_criterion5_fixture["faculty_members"]
    res = calculate_criterion5_cadre_metrics(faculty)

    assert res["total_faculty"] == 12
    # 2 Professors, 2 Associate Professors, 8 Assistant Professors
    assert res["cadre_counts"]["professors"] == 2
    assert res["cadre_counts"]["associate_professors"] == 2
    assert res["cadre_counts"]["assistant_professors"] == 8
    assert res["cadre_ratio_display"] == "2 : 2 : 8"

    # Qualifications: 4 Ph.Ds, 8 M.Techs -> 4/12 = 33.33%
    assert res["qualifications"]["phd_count"] == 4
    assert res["qualifications"]["masters_count"] == 8
    assert res["qualifications"]["phd_percentage"] == 33.33


def test_experience_calculations():
    """Verify deterministic experience calculations."""
    faculty = synthetic_criterion5_fixture["faculty_members"]
    res = calculate_criterion5_experience_metrics(faculty)

    assert res["faculty_count_with_experience_data"] == 12
    assert res["max_total_experience_years"] == 20.0
    assert res["min_total_experience_years"] == 3.0
    assert res["average_total_experience_years"] > 0
    assert res["average_institution_experience_years"] > 0


def test_pii_sanitization():
    """Verify that sensitive personal PII is completely stripped before LLM processing."""
    faculty = synthetic_criterion5_fixture["faculty_members"]
    sanitized = sanitize_faculty_data(faculty)

    for fac in sanitized:
        assert "phone" not in fac
        assert "personal_email" not in fac
        assert "home_address" not in fac
        # Essential academic credentials must remain preserved
        assert "faculty_id" in fac
        assert "designation" in fac
        assert "qualification" in fac


def test_faculty_agent_mock():
    """Verify Faculty Agent mock execution and structure."""
    mock_response = (
        "SECTION 1: Faculty Roster and Cadre Ratio Summary\n"
        "SECTION 2: Student-to-Faculty Ratio (SFR) Analysis\n"
        "SECTION 3: Faculty Experience and Teaching Distribution\n"
        "SECTION 4: Data Completeness and Evidence Verification Audit\n"
        "SECTION 5: Recommendations"
    )
    result = analyze_faculty_information(
        synthetic_criterion5_fixture,
        mock_response=mock_response
    )

    assert "SECTION 1" in result
    assert "Faculty Roster and Cadre Ratio Summary" in result
    assert "SECTION 2" in result
    assert "Student-to-Faculty Ratio (SFR)" in result
