# test_criterion3_agents.py
"""
Unit tests for Criterion 3 agents running with mocked LLM output.
Validates end-to-end agent orchestration without requiring live Groq API quota.
"""

import sys
from pathlib import Path

# Add ai-service to sys.path
ai_service_path = Path(__file__).resolve().parent.parent.parent / "ai-service"
if str(ai_service_path) not in sys.path:
    sys.path.insert(0, str(ai_service_path))

from app.agents.assessment_agent import analyze_assessment
from app.agents.student_agent import analyze_student_performance
from app.agents.coordinator_agent import coordinate_criterion3


def test_assessment_agent_mock():
    """Verify assessment agent produces valid response using mock mode."""
    mock_out = "SECTION 1: Assessment Scheme Summary\nSECTION 2: CO Coverage"
    result = analyze_assessment(mock_response=mock_out)
    assert "SECTION 1" in result
    assert "Assessment Scheme Summary" in result


def test_student_agent_mock():
    """Verify student agent handles input and mock response."""
    mock_out = "SECTION 1: Student Performance Summary\nSECTION 3: Numerical Observations"
    result = analyze_student_performance(mock_response=mock_out)
    assert "SECTION 1" in result
    assert "Numerical Observations" in result


def test_coordinator_agent_mock():
    """Verify coordinator agent merges outputs in mock mode."""
    mock_coord = "1. Criterion 3 Summary\n2. Assessment Findings\n3. Student Performance Findings"
    result = coordinate_criterion3(
        assessment_analysis="Assessment Output Mock",
        student_analysis="Student Output Mock",
        mock_response=mock_coord
    )
    assert "Criterion 3 Summary" in result
