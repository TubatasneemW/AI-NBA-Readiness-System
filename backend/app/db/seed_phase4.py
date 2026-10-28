"""
AI-NBA Readiness System — Backend
app/db/seed_phase4.py

Idempotent seed data for NBA Criteria and Requirements (Phase 4).

IMPORTANT PLACEHOLDERS
-----------------------
All max_marks, weightage, and threshold values are PLACEHOLDERS.
They must be replaced with values from official NBA SAR documentation
before any accreditation submission.  This seed serves only as a
structural scaffold and testing fixture.

Usage:
    python -m app.db.seed_phase4
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Allow running as __main__ from backend/
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.phase4 import NBACriterion, NBARequirement

# ---------------------------------------------------------------------------
# Seed data — structure only; values are PLACEHOLDERS
# ---------------------------------------------------------------------------

CRITERIA_SEED: list[dict[str, Any]] = [
    {
        "code": "CRITERION_3",
        "name": "Course Outcomes and Program Outcomes",
        "description": "[PLACEHOLDER] Criterion 3 covers CO definition, CO-PO/PSO mapping, and attainment measurement.",
        "max_marks": 120.0,
        "display_order": 3,
        "requirements": [
            {
                "code": "REQ_3_1",
                "title": "Course Outcome Definition and Documentation",
                "description": "[PLACEHOLDER] All subjects must have documented COs aligned with Bloom''s taxonomy.",
                "weightage": 10.0,
                "is_mandatory": True,
                "evaluation_rule_key": "criterion3.co_definition_completeness",
                "display_order": 1,
            },
            {
                "code": "REQ_3_2",
                "title": "CO-PO Mapping Completeness",
                "description": "[PLACEHOLDER] Every CO must be mapped to at least one PO with a correlation level.",
                "weightage": 10.0,
                "is_mandatory": True,
                "evaluation_rule_key": "criterion3.copo_mapping_completeness",
                "display_order": 2,
            },
        ],
    },
    {
        "code": "CRITERION_4",
        "name": "Students'' Performance",
        "description": "[PLACEHOLDER] Criterion 4 covers student pass rates, higher studies, and placement.",
        "max_marks": 150.0,
        "display_order": 4,
        "requirements": [
            {
                "code": "REQ_4_1",
                "title": "Batch Pass Percentage",
                "description": "[PLACEHOLDER] Department-level pass percentage across all semesters.",
                "weightage": 20.0,
                "is_mandatory": True,
                "evaluation_rule_key": "criterion4.pass_percentage",
                "display_order": 1,
            },
        ],
    },
    {
        "code": "CRITERION_5",
        "name": "Faculty Information and Contributions",
        "description": "[PLACEHOLDER] Criterion 5 covers faculty qualifications, publications, and achievements.",
        "max_marks": 200.0,
        "display_order": 5,
        "requirements": [
            {
                "code": "REQ_5_1",
                "title": "Faculty Qualification Ratio",
                "description": "[PLACEHOLDER] Proportion of faculty with PG or PhD qualifications.",
                "weightage": 20.0,
                "is_mandatory": True,
                "evaluation_rule_key": "criterion5.faculty_qualification_ratio",
                "display_order": 1,
            },
        ],
    },
    {
        "code": "CRITERION_6",
        "name": "Facilities and Technical Support",
        "description": "[PLACEHOLDER] Criterion 6 covers laboratory infrastructure, software, and support staff.",
        "max_marks": 100.0,
        "display_order": 6,
        "requirements": [
            {
                "code": "REQ_6_1",
                "title": "Laboratory Facility Availability",
                "description": "[PLACEHOLDER] Availability of required laboratories relative to curriculum needs.",
                "weightage": 20.0,
                "is_mandatory": True,
                "evaluation_rule_key": "criterion6.lab_facility_availability",
                "display_order": 1,
            },
        ],
    },
]


def seed_phase4(db: Session) -> None:
    """
    Idempotently seed NBA Criteria and Requirements.

    - Existing records (matched by code) are not modified.
    - New criteria/requirements are inserted.
    - Safe to run multiple times.
    """
    for item in CRITERIA_SEED:
        criterion_data = dict(item)
        req_data = criterion_data.pop("requirements", [])

        existing_criterion = (
            db.query(NBACriterion)
            .filter(NBACriterion.code == criterion_data["code"])
            .first()
        )
        if existing_criterion is None:
            criterion = NBACriterion(**criterion_data)
            db.add(criterion)
            db.flush()
        else:
            criterion = existing_criterion

        for req in req_data:
            existing_req = (
                db.query(NBARequirement)
                .filter(NBARequirement.code == req["code"])
                .first()
            )
            if existing_req is None:
                requirement = NBARequirement(criterion_id=criterion.id, **req)
                db.add(requirement)

    db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_phase4(db)
        print("Phase 4 seed completed successfully.")
    finally:
        db.close()
