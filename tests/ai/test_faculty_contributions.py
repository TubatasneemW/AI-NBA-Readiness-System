# test_faculty_contributions.py
"""
Unit tests for Criterion 6 Faculty Contributions Analysis.
Verifies publications, patents, research projects, consultancy, FDPs,
verification status separation, and Faculty Agent Criterion 6 analysis.
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
    calculate_criterion6_publication_metrics,
    calculate_criterion6_patent_metrics,
    calculate_criterion6_project_metrics,
    calculate_criterion6_fdp_metrics
)
from app.agents.faculty_agent import analyze_faculty_contributions
from tests.fixtures.criterion6_test_fixture import synthetic_criterion6_fixture


def test_publication_metrics():
    """Verify deterministic publication metrics and indexing categorization."""
    pubs = synthetic_criterion6_fixture["publications"]
    res = calculate_criterion6_publication_metrics(pubs)

    assert res["total_publications_submitted"] == 5
    assert res["confirmed_publications_count"] == 4
    assert res["pending_verification_count"] == 1

    # 1 SCI, 1 SCIE, 1 Scopus, 1 Conferences
    assert res["sci_scopus_confirmed_count"] == 3
    assert res["confirmed_indexing_breakdown"]["SCI"] == 1
    assert res["confirmed_indexing_breakdown"]["Scopus"] == 1
    assert res["confirmed_indexing_breakdown"]["Conferences"] == 1


def test_patent_metrics():
    """Verify deterministic patent metrics and status breakdown."""
    patents = synthetic_criterion6_fixture["patents"]
    res = calculate_criterion6_patent_metrics(patents)

    assert res["total_patents_submitted"] == 3
    assert res["confirmed_patents_count"] == 2
    assert res["pending_verification_count"] == 1
    assert res["confirmed_granted_count"] == 1
    assert res["confirmed_published_count"] == 1
    assert res["confirmed_filed_count"] == 0  # Filed one was unverified


def test_project_and_consultancy_metrics():
    """Verify deterministic research funding and consultancy revenue."""
    projects = synthetic_criterion6_fixture["sponsored_projects"]
    consultancy = synthetic_criterion6_fixture["consultancy"]
    res = calculate_criterion6_project_metrics(projects, consultancy)

    # 1 verified project (25.0 Lakhs), 1 unverified project (12.0 Lakhs)
    sp = res["sponsored_projects"]
    assert sp["submitted_count"] == 2
    assert sp["confirmed_count"] == 1
    assert sp["pending_count"] == 1
    assert sp["total_funding_amount_lakhs"] == 25.0

    # 1 verified consultancy (4.5 Lakhs)
    con = res["consultancy"]
    assert con["submitted_count"] == 1
    assert con["confirmed_count"] == 1
    assert con["total_revenue_amount_lakhs"] == 4.5

    # Aggregate: 25.0 + 4.5 = 29.5 Lakhs
    assert res["aggregate_research_revenue_lakhs"] == 29.5


def test_fdp_metrics():
    """Verify deterministic FDP metrics and roles."""
    fdps = synthetic_criterion6_fixture["fdps"]
    res = calculate_criterion6_fdp_metrics(fdps)

    assert res["total_fdp_submitted"] == 4
    assert res["confirmed_fdp_count"] == 3
    assert res["pending_verification_count"] == 1
    assert res["confirmed_roles"]["Attended"] == 2
    assert res["confirmed_roles"]["Organized"] == 1


def test_faculty_contributions_agent_mock():
    """Verify Faculty Contributions Agent execution with mock response."""
    mock_response = (
        "SECTION 1: Research Publications and Journal Indexing\n"
        "SECTION 2: Intellectual Property and Patents\n"
        "SECTION 3: Sponsored Research Projects and Consultancy Revenue\n"
        "SECTION 4: Faculty Development Programs (FDPs)\n"
        "SECTION 5: Evidence Verification Audit"
    )
    result = analyze_faculty_contributions(
        synthetic_criterion6_fixture,
        mock_response=mock_response
    )

    assert "SECTION 1" in result
    assert "Research Publications" in result
    assert "SECTION 2" in result
    assert "Intellectual Property and Patents" in result
    assert "SECTION 3" in result
    assert "Consultancy Revenue" in result
