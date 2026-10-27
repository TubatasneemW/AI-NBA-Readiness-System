# test_criterion4_agent.py
"""
Unit tests for Criterion 4 Student Performance & Progression Analysis.
Tests deterministic mathematics and agent handling using the synthetic test fixture.
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
    calculate_criterion4_progression_metrics,
    calculate_criterion4_placement_metrics,
    summarize_student_achievements
)
from app.agents.student_agent import analyze_criterion4_student_performance
from tests.fixtures.criterion4_test_fixture import synthetic_criterion4_fixture


def test_progression_metrics_calculations():
    """Verify deterministic calculations for cohort progression and graduation rates."""
    cohorts = synthetic_criterion4_fixture["cohorts"]
    results = calculate_criterion4_progression_metrics(cohorts)

    assert results["cohort_count"] == 2

    # Cohort 1 (2019-2023): 48/60 = 80.0%, (48+6)/60 = 90.0%
    c1 = results["cohorts"][0]
    assert c1["batch"] == "2019-2023"
    assert c1["completion_rate_without_backlog_pct"] == 80.0
    assert c1["overall_completion_rate_pct"] == 90.0

    # Cohort 2 (2020-2024): 52/62 = 83.87%, (52+5)/62 = 91.94%
    c2 = results["cohorts"][1]
    assert c2["batch"] == "2020-2024"
    assert c2["completion_rate_without_backlog_pct"] == 83.87
    assert c2["overall_completion_rate_pct"] == 91.94

    # Aggregate: admitted 122, completed w/o backlog 100 -> 81.97%
    agg = results["aggregate"]
    assert agg["total_admitted"] == 122
    assert agg["total_completed_without_backlog"] == 100
    assert agg["total_graduated"] == 111
    assert agg["aggregate_completion_rate_without_backlog_pct"] == 81.97
    assert agg["aggregate_overall_completion_rate_pct"] == 90.98


def test_placement_metrics_calculations():
    """Verify deterministic calculations for placement, higher studies, and entrepreneurship."""
    placements = synthetic_criterion4_fixture["placements"]
    results = calculate_criterion4_placement_metrics(placements)

    assert results["year_count"] == 2

    # Year 1 (2022-23): 42/54 = 77.78%, (42+6+1)/54 = 49/54 = 90.74%
    y1 = results["years"][0]
    assert y1["placement_pct"] == 77.78
    assert y1["total_progression_pct"] == 90.74

    # Year 2 (2023-24): 46/57 = 80.70%, (46+5+2)/57 = 53/57 = 92.98%
    y2 = results["years"][1]
    assert y2["placement_pct"] == 80.70
    assert y2["total_progression_pct"] == 92.98

    # Aggregate: final year 111, placed 88 -> 79.28%, total progressed 102 -> 91.89%
    agg = results["aggregate"]
    assert agg["total_final_year_students"] == 111
    assert agg["total_placed"] == 88
    assert agg["total_higher_studies"] == 11
    assert agg["total_entrepreneurs"] == 3
    assert agg["total_progressed"] == 102
    assert agg["aggregate_placement_pct"] == 79.28
    assert agg["aggregate_progression_pct"] == 91.89


def test_achievement_categorization_and_verification():
    """Verify categorization and verification count separation for student achievements."""
    achievements = synthetic_criterion4_fixture["achievements"]
    summary = summarize_student_achievements(achievements)

    assert summary["total_achievements"] == 3
    assert summary["categories"]["Technical Competition"] == 2
    assert summary["categories"]["Publication"] == 1
    assert summary["verification_breakdown"]["verified"] == 2
    assert summary["verification_breakdown"]["pending_verification"] == 1


def test_criterion4_agent_mock():
    """Verify Criterion 4 agent execution with mock response and structure."""
    mock_response = (
        "SECTION 1: Academic Progression and Completion\n"
        "SECTION 2: Placements, Higher Studies, and Entrepreneurship\n"
        "SECTION 3: Student Achievements\n"
        "SECTION 4: Data Quality and Evidence Limitations\n"
        "SECTION 5: Recommendations"
    )
    result = analyze_criterion4_student_performance(
        synthetic_criterion4_fixture,
        mock_response=mock_response
    )

    assert "SECTION 1" in result
    assert "Academic Progression and Completion" in result
    assert "SECTION 4" in result
    assert "Data Quality and Evidence Limitations" in result
