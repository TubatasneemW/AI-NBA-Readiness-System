# criterion5_test_fixture.py
"""
EXPLICIT DISCLAIMER:
This dataset is a SYNTHETIC TEST FIXTURE designed strictly for isolated unit
and integration testing of NBA Criterion 5 AI agents.
It contains synthetic faculty profiles and deliberately includes mock PII fields
to test data sanitization and privacy filtering.
It does NOT represent real institutional records or production data.
"""

synthetic_criterion5_fixture = {
    "department": "Artificial Intelligence and Machine Learning",
    "academic_year": "2024-25",
    "total_enrolled_students": 180,  # 60 students per batch across 2nd, 3rd, 4th year

    "faculty_members": [
        {
            "faculty_id": "FAC-AIML-001",
            "name": "Dr. A. Sharma",
            "designation": "Professor",
            "qualification": "Ph.D. in Computer Science",
            "specialization": "Artificial Intelligence & NLP",
            "total_experience_years": 20.0,
            "institution_experience_years": 8.0,
            "verified": True,
            "evidence_document": "DOC-FAC-001-APPT.pdf",
            # Mock PII to verify privacy sanitization
            "phone": "+91-9876543210",
            "personal_email": "sharma.personal@example.com",
            "home_address": "123 Academic Colony, City"
        },
        {
            "faculty_id": "FAC-AIML-002",
            "name": "Dr. B. Kulkarni",
            "designation": "Professor",
            "qualification": "Ph.D. in Information Technology",
            "specialization": "Machine Learning & Big Data",
            "total_experience_years": 18.0,
            "institution_experience_years": 6.0,
            "verified": True,
            "evidence_document": "DOC-FAC-002-APPT.pdf",
            "phone": "+91-9876543211",
            "personal_email": "kulkarni.personal@example.com"
        },
        {
            "faculty_id": "FAC-AIML-003",
            "name": "Dr. C. Rao",
            "designation": "Associate Professor",
            "qualification": "Ph.D. in Computer Engineering",
            "specialization": "Deep Learning & Computer Vision",
            "total_experience_years": 14.0,
            "institution_experience_years": 5.0,
            "verified": True,
            "evidence_document": "DOC-FAC-003-APPT.pdf"
        },
        {
            "faculty_id": "FAC-AIML-004",
            "name": "Dr. D. Patil",
            "designation": "Associate Professor",
            "qualification": "Ph.D. in AI",
            "specialization": "Reinforcement Learning",
            "total_experience_years": 12.0,
            "institution_experience_years": 4.0,
            "verified": True,
            "evidence_document": "DOC-FAC-004-APPT.pdf"
        },
        {
            "faculty_id": "FAC-AIML-005",
            "name": "Prof. E. Nair",
            "designation": "Assistant Professor",
            "qualification": "M.Tech in Machine Learning",
            "specialization": "Data Analytics",
            "total_experience_years": 8.0,
            "institution_experience_years": 4.0,
            "verified": True,
            "evidence_document": "DOC-FAC-005-APPT.pdf"
        },
        {
            "faculty_id": "FAC-AIML-006",
            "name": "Prof. F. Deshmukh",
            "designation": "Assistant Professor",
            "qualification": "M.Tech in Artificial Intelligence",
            "specialization": "Neural Networks",
            "total_experience_years": 6.0,
            "institution_experience_years": 3.0,
            "verified": True,
            "evidence_document": "DOC-FAC-006-APPT.pdf"
        },
        {
            "faculty_id": "FAC-AIML-007",
            "name": "Prof. G. Reddy",
            "designation": "Assistant Professor",
            "qualification": "M.Tech in Computer Science",
            "specialization": "Cloud Computing",
            "total_experience_years": 5.0,
            "institution_experience_years": 2.0,
            "verified": True,
            "evidence_document": "DOC-FAC-007-APPT.pdf"
        },
        {
            "faculty_id": "FAC-AIML-008",
            "name": "Prof. H. Verma",
            "designation": "Assistant Professor",
            "qualification": "M.Tech in Data Science",
            "specialization": "Statistical Modeling",
            "total_experience_years": 5.0,
            "institution_experience_years": 2.0,
            "verified": True,
            "evidence_document": "DOC-FAC-008-APPT.pdf"
        },
        {
            "faculty_id": "FAC-AIML-009",
            "name": "Prof. I. Joshi",
            "designation": "Assistant Professor",
            "qualification": "M.Tech in Software Engineering",
            "specialization": "MLOps",
            "total_experience_years": 4.0,
            "institution_experience_years": 2.0,
            "verified": True,
            "evidence_document": "DOC-FAC-009-APPT.pdf"
        },
        {
            "faculty_id": "FAC-AIML-0010",
            "name": "Prof. J. Mehta",
            "designation": "Assistant Professor",
            "qualification": "M.Tech in Computer Networks",
            "specialization": "IoT and Edge AI",
            "total_experience_years": 4.0,
            "institution_experience_years": 1.0,
            "verified": True,
            "evidence_document": "DOC-FAC-010-APPT.pdf"
        },
        {
            "faculty_id": "FAC-AIML-0011",
            "name": "Prof. K. Iyer",
            "designation": "Assistant Professor",
            "qualification": "M.Tech in Artificial Intelligence",
            "specialization": "Robotics & AI",
            "total_experience_years": 3.0,
            "institution_experience_years": 1.0,
            "verified": True,
            "evidence_document": "DOC-FAC-011-APPT.pdf"
        },
        {
            "faculty_id": "FAC-AIML-0012",
            "name": "Prof. L. Gupta",
            "designation": "Assistant Professor",
            "qualification": "M.Tech in Computer Science",
            "specialization": "Algorithms & AI",
            "total_experience_years": 3.0,
            "institution_experience_years": 1.0,
            "verified": False,  # Pending verification test case
            "evidence_document": None
        }
    ]
}
