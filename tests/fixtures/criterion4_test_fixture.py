# criterion4_test_fixture.py
"""
EXPLICIT DISCLAIMER:
This dataset is a SYNTHETIC TEST FIXTURE designed strictly for isolated unit
and integration testing of NBA Criterion 4 AI agents.
It does NOT represent real institutional records or production data.
"""

synthetic_criterion4_fixture = {
    "program": "B.E. Artificial Intelligence & Machine Learning",
    "academic_years_covered": ["2021-22", "2022-23", "2023-24"],

    # Academic progression across recent cohorts
    "cohorts": [
        {
            "batch": "2019-2023",
            "admitted_count": 60,
            "completed_without_backlog": 48,
            "completed_with_backlog": 6
        },
        {
            "batch": "2020-2024",
            "admitted_count": 62,
            "completed_without_backlog": 52,
            "completed_with_backlog": 5
        }
    ],

    # Placements, higher studies, and entrepreneurship
    "placements": [
        {
            "academic_year": "2022-23",
            "final_year_students": 54,
            "placed_count": 42,
            "higher_studies_count": 6,
            "entrepreneurship_count": 1,
            "median_salary_lpa": 6.5
        },
        {
            "academic_year": "2023-24",
            "final_year_students": 57,
            "placed_count": 46,
            "higher_studies_count": 5,
            "entrepreneurship_count": 2,
            "median_salary_lpa": 7.0
        }
    ],

    # Student achievements, activities, and participation
    "achievements": [
        {
            "achievement_id": "ACH-001",
            "title": "Smart India Hackathon Finalist",
            "category": "Technical Competition",
            "academic_year": "2023-24",
            "verified": True,
            "evidence_document": "DOC-CERT-SIH-2023.pdf"
        },
        {
            "achievement_id": "ACH-002",
            "title": "IEEE Conference Best Paper Award",
            "category": "Publication",
            "academic_year": "2023-24",
            "verified": True,
            "evidence_document": "DOC-IEEE-AWARD-2024.pdf"
        },
        {
            "achievement_id": "ACH-003",
            "title": "State-level Coding Marathon Runner-Up",
            "category": "Technical Competition",
            "academic_year": "2022-23",
            "verified": False,  # Pending verification test case
            "evidence_document": None
        }
    ],

    "competitive_exams": None  # Intentionally None to test missing evidence handling
}
