# test_contributions_live.py
"""
Live test of Criterion 6 Faculty Contributions Analysis with Groq API.
Uses synthetic test fixture to demonstrate research, patents, grants, and FDP analysis.
"""

import sys
from pathlib import Path

# Add project root and ai-service to sys.path
root_path = Path(__file__).resolve().parent.parent
ai_service_path = root_path / "ai-service"
if str(ai_service_path) not in sys.path:
    sys.path.insert(0, str(ai_service_path))
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from app.agents.faculty_agent import analyze_faculty_contributions
from tests.fixtures.criterion6_test_fixture import synthetic_criterion6_fixture

print("=" * 70)
print("RUNNING CRITERION 6 FACULTY CONTRIBUTIONS ANALYSIS (LIVE GROQ)")
print("=" * 70)

result = analyze_faculty_contributions(synthetic_criterion6_fixture)

print("\nCriterion 6 Faculty Agent completed successfully.")
print("\n" + "=" * 70)
print("CRITERION 6 ANALYSIS OUTPUT")
print("=" * 70)
print(result)
