# test_metrics_service.py
"""
Unit tests for deterministic metrics calculations.

Validates that mathematical calculations (means, ranges, mins, maxs, and pass percentages)
are strictly computed by Python without reliance on generative language models.
"""

import sys
from pathlib import Path

# Add ai-service to sys.path so modules can be imported directly
ai_service_path = Path(__file__).resolve().parent.parent.parent / "ai-service"
if str(ai_service_path) not in sys.path:
    sys.path.insert(0, str(ai_service_path))

from app.services.metrics_service import (
    calculate_student_statistics,
    calculate_grade_distribution_metrics
)
from data.criterion3_data import criterion3_data


def test_official_criterion3_dataset_statistics():
    """
    Verify deterministic statistics against the verified Criterion 3 dataset
    containing 56 student records.
    """
    students = criterion3_data["students"]
    stats = calculate_student_statistics(students)

    assert stats["record_count"] == 56

    # CIE-I: 14.11 average, min 4.5, max 20.0
    assert stats["CIE-I"]["average"] == 14.11
    assert stats["CIE-I"]["minimum"] == 4.5
    assert stats["CIE-I"]["maximum"] == 20.0
    assert stats["CIE-I"]["range"] == 15.5

    # CIE-II: 13.34 average, min 3.0, max 20.0
    assert stats["CIE-II"]["average"] == 13.34
    assert stats["CIE-II"]["minimum"] == 3.0
    assert stats["CIE-II"]["maximum"] == 20.0
    assert stats["CIE-II"]["range"] == 17.0

    # Micro Project: 10.00 average, min 10.0, max 10.0
    assert stats["Micro Project"]["average"] == 10.00
    assert stats["Micro Project"]["minimum"] == 10.0
    assert stats["Micro Project"]["maximum"] == 10.0
    assert stats["Micro Project"]["range"] == 0.0

    # Internal Total: 37.73 average, min 20.0, max 50.0
    assert stats["Internal Total"]["average"] == 37.73
    assert stats["Internal Total"]["minimum"] == 20.0
    assert stats["Internal Total"]["maximum"] == 50.0
    assert stats["Internal Total"]["range"] == 30.0

    # Attendance: 90.98% average, min 86, max 96
    assert stats["Attendance"]["average"] == 90.98
    assert stats["Attendance"]["minimum"] == 86
    assert stats["Attendance"]["maximum"] == 96
    assert stats["Attendance"]["range"] == 10.0


def test_grade_distribution_calculations():
    """
    Verify course-level grade distribution calculations (60 registered, 49 passed -> 81.67%).
    """
    grade_data = criterion3_data["grade_distribution"]
    metrics = calculate_grade_distribution_metrics(grade_data)

    assert metrics["registered"] == 60
    assert metrics["appeared"] == 60
    assert metrics["passed"] == 49
    assert metrics["pass_percentage"] == 81.67
    assert metrics["grades"]["O"] == 1
    assert metrics["grades"]["F"] == 11


def test_student_statistics_with_optional_fields():
    """
    Verify that custom inputs without Attendance or Internal Total
    do not crash and compute totals dynamically.
    """
    records = [
        {"student_id": "S1", "CIE-I": 10.0, "CIE-II": 12.0, "Micro Project": 8.0},
        {"student_id": "S2", "CIE-I": 20.0, "CIE-II": 18.0, "Micro Project": 10.0}
    ]
    stats = calculate_student_statistics(records)

    assert stats["record_count"] == 2
    assert stats["CIE-I"]["average"] == 15.0
    # Dynamic sum: 10+12+8=30, 20+18+10=48 => avg = 39.0
    assert stats["Internal Total"]["average"] == 39.0
    assert "Attendance records not provided" in stats["Attendance"]["status"]
