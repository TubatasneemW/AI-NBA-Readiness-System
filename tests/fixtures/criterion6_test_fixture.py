# criterion6_test_fixture.py
"""
EXPLICIT DISCLAIMER:
This dataset is a SYNTHETIC TEST FIXTURE designed strictly for isolated unit
and integration testing of NBA Criterion 6 AI agents.
It contains synthetic faculty contribution records (publications, patents,
funded R&D projects, consultancy, and FDPs) including deliberate unverified records
to test verification audit separation.
It does NOT represent real institutional records or production data.
"""

synthetic_criterion6_fixture = {
    "department": "Artificial Intelligence and Machine Learning",
    "academic_years_covered": ["2022-23", "2023-24", "2024-25"],

    # Research Publications
    "publications": [
        {
            "publication_id": "PUB-2023-001",
            "title": "Optimized Deep Learning for Multimodal Healthcare Data",
            "indexing": "SCI",
            "year": "2023",
            "doi": "10.1016/j.aihealth.2023.01.005",
            "verified": True,
            "evidence_document": "DOC-PUB-001-REPRINT.pdf"
        },
        {
            "publication_id": "PUB-2023-002",
            "title": "Edge AI Inference Acceleration in Resource-Constrained IoT",
            "indexing": "Scopus",
            "year": "2023",
            "doi": "10.1109/TII.2023.109283",
            "verified": True,
            "evidence_document": "DOC-PUB-002-REPRINT.pdf"
        },
        {
            "publication_id": "PUB-2024-003",
            "title": "Self-Supervised Representation Learning for Satellite Imagery",
            "indexing": "SCIE",
            "year": "2024",
            "doi": "10.1007/s11042-024-18492-w",
            "verified": True,
            "evidence_document": "DOC-PUB-003-REPRINT.pdf"
        },
        {
            "publication_id": "PUB-2024-004",
            "title": "Federated Learning for Autonomous Driving Fleet Analytics",
            "indexing": "Conferences",
            "year": "2024",
            "doi": "10.1145/3639845.3640212",
            "verified": True,
            "evidence_document": "DOC-PUB-004-CONF.pdf"
        },
        {
            "publication_id": "PUB-2024-005",
            "title": "Quantum Machine Learning Algorithms: A Systematic Survey",
            "indexing": "UGC-CARE",
            "year": "2024",
            "doi": None,
            "verified": False,  # Pending verification test case
            "evidence_document": None
        }
    ],

    # Intellectual Property / Patents
    "patents": [
        {
            "patent_id": "PAT-2023-01",
            "title": "An Automated AI Drone System for Crop Disease Detection",
            "status": "Granted",
            "application_number": "202241049281",
            "verified": True,
            "evidence_document": "DOC-PAT-GRANTED-CERT.pdf"
        },
        {
            "patent_id": "PAT-2024-02",
            "title": "Hardware-Accelerated Neural Network Processor for Wearables",
            "status": "Published",
            "application_number": "202341088219",
            "verified": True,
            "evidence_document": "DOC-PAT-PUBLISHED-GAZETTE.pdf"
        },
        {
            "patent_id": "PAT-2024-03",
            "title": "Adaptive Traffic Signal Optimizer Using Edge Vision",
            "status": "Filed",
            "application_number": "202441019283",
            "verified": False,  # Pending verification test case
            "evidence_document": None
        }
    ],

    # Sponsored R&D Projects
    "sponsored_projects": [
        {
            "project_id": "PRJ-DST-2023",
            "title": "AI-Driven Predictive Maintenance for Smart Power Grids",
            "funding_agency": "Department of Science and Technology (DST)",
            "funding_amount_lakhs": 25.0,
            "duration_years": 3,
            "status": "Ongoing",
            "verified": True,
            "evidence_document": "DOC-DST-SANCTION-2023.pdf"
        },
        {
            "project_id": "PRJ-AICTE-2024",
            "title": "Deep Learning Laboratory for Assistive Technologies",
            "funding_agency": "AICTE-MODROBS",
            "funding_amount_lakhs": 12.0,
            "duration_years": 2,
            "status": "Ongoing",
            "verified": False,  # Pending sanction letter verification
            "evidence_document": None
        }
    ],

    # Consultancy Work
    "consultancy": [
        {
            "consultancy_id": "CON-2023-01",
            "title": "Computer Vision Defect Inspection System for Manufacturing Line",
            "client_organization": "Precision Auto Components Ltd.",
            "revenue_amount_lakhs": 4.5,
            "verified": True,
            "evidence_document": "DOC-CONS-AGREEMENT-2023.pdf"
        }
    ],

    # Faculty Development Programs (FDPs / STTPs)
    "fdps": [
        {
            "fdp_id": "FDP-2023-01",
            "title": "Advanced Deep Learning with PyTorch and CUDA",
            "role": "Attended",
            "duration_days": 5,
            "verified": True,
            "evidence_document": "DOC-FDP-CERT-01.pdf"
        },
        {
            "fdp_id": "FDP-2023-02",
            "title": "Generative AI and Large Language Models in Engineering",
            "role": "Attended",
            "duration_days": 10,
            "verified": True,
            "evidence_document": "DOC-FDP-CERT-02.pdf"
        },
        {
            "fdp_id": "FDP-2024-03",
            "title": "National Workshop on MLOps and Cloud Deployments",
            "role": "Organized",
            "duration_days": 5,
            "verified": True,
            "evidence_document": "DOC-FDP-REPORT-03.pdf"
        },
        {
            "fdp_id": "FDP-2024-04",
            "title": "AI in Cybersecurity and Threat Intelligence",
            "role": "Attended",
            "duration_days": 5,
            "verified": False,  # Pending certificate verification
            "evidence_document": None
        }
    ]
}
