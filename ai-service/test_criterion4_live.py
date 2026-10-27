# test_criterion4_live.py
"""
Live test of Criterion 4 Student Performance Analysis with Groq API.
Uses synthetic test fixture to demonstrate the complete Criterion 4 workflow.
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

from app.agents.student_agent import analyze_criterion4_student_performance
from tests.fixtures.criterion4_test_fixture import synthetic_criterion4_fixture

print("=" * 70)
print("RUNNING CRITERION 4 STUDENT PERFORMANCE ANALYSIS (LIVE GROQ)")
print("=" * 70)

result = analyze_criterion4_student_performance(synthetic_criterion4_fixture)

print("\nCriterion 4 Student Agent completed successfully.")
print("\n" + "=" * 70)
print("CRITERION 4 ANALYSIS OUTPUT")
print("=" * 70)
print(result)
