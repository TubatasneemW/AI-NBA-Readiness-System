# test_faculty_live.py
"""
Live test of Criterion 5 Faculty Information Analysis with Groq API.
Uses synthetic test fixture to demonstrate the complete Criterion 5 workflow.
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

from app.agents.faculty_agent import analyze_faculty_information
from tests.fixtures.criterion5_test_fixture import synthetic_criterion5_fixture

print("=" * 70)
print("RUNNING CRITERION 5 FACULTY INFORMATION ANALYSIS (LIVE GROQ)")
print("=" * 70)

result = analyze_faculty_information(synthetic_criterion5_fixture)

print("\nCriterion 5 Faculty Agent completed successfully.")
print("\n" + "=" * 70)
print("CRITERION 5 ANALYSIS OUTPUT")
print("=" * 70)
print(result)
