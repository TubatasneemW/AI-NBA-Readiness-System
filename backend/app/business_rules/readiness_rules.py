# readiness_rules.py
"""
NBA Departmental Readiness Evaluation Engine.

Synthesizes compliance, evidence completeness, and gap severity across:
- Criterion 3: Course Outcomes & Program Outcomes
- Criterion 4: Students' Performance & Progression
- Criterion 5: Faculty Information & SFR
- Criterion 6: Faculty Contributions, R&D & Consultancy

Computes composite readiness index and categorizes overall accreditation status.
"""

from typing import Any, Dict, List
from app.business_rules.criterion3_rules import evaluate_criterion3_compliance
from app.business_rules.criterion4_rules import evaluate_criterion4_compliance
from app.business_rules.criterion5_rules import evaluate_criterion5_compliance
from app.business_rules.criterion6_rules import evaluate_criterion6_compliance


def evaluate_department_readiness(
    department_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Deterministically synthesize readiness metrics and compliance statuses
    across Criteria 3, 4, 5, and 6.
    """
    c3_input = department_data.get("criterion3", {})
    c4_input = department_data.get("criterion4", {})
    c5_input = department_data.get("criterion5", {})
    c6_input = department_data.get("criterion6", {})

    c3_eval = evaluate_criterion3_compliance(c3_input)
    c4_eval = evaluate_criterion4_compliance(c4_input)
    c5_eval = evaluate_criterion5_compliance(c5_input)
    c6_eval = evaluate_criterion6_compliance(c6_input)

    # Weights according to typical NBA SAR distribution (Tier-I / Tier-II)
    # Criterion 3: 100/120 pts (~25%)
    # Criterion 4: 100/150 pts (~25%)
    # Criterion 5: 150/200 pts (~25%)
    # Criterion 6: 75/100 pts (~25%)
    weights = {
        "criterion3": 0.25,
        "criterion4": 0.25,
        "criterion5": 0.25,
        "criterion6": 0.25
    }

    composite_score = round(
        c3_eval["completeness_percentage"] * weights["criterion3"]
        + c4_eval["completeness_percentage"] * weights["criterion4"]
        + c5_eval["completeness_percentage"] * weights["criterion5"]
        + c6_eval["completeness_percentage"] * weights["criterion6"],
        2
    )

    all_gaps: List[Dict[str, Any]] = (
        c3_eval["gaps"] + c4_eval["gaps"] + c5_eval["gaps"] + c6_eval["gaps"]
    )

    critical_gaps = [g for g in all_gaps if g.get("severity") == "Critical"]
    major_gaps = [g for g in all_gaps if g.get("severity") == "Major"]
    minor_gaps = [g for g in all_gaps if g.get("severity") == "Minor"]

    # Readiness Verdict
    if len(critical_gaps) > 0 or composite_score < 60.0:
        verdict = "Low Readiness - Critical Action Required"
        status = "Non-Compliant"
    elif len(major_gaps) > 3 or composite_score < 80.0:
        verdict = "Moderate Readiness - Gaps Identified"
        status = "Partially Compliant"
    else:
        verdict = "High Readiness - Inspection Ready"
        status = "Compliant"

    return {
        "department": department_data.get("department", "Department Not Specified"),
        "composite_readiness_score": composite_score,
        "overall_status": status,
        "readiness_verdict": verdict,
        "criterion_breakdown": {
            "criterion3": c3_eval,
            "criterion4": c4_eval,
            "criterion5": c5_eval,
            "criterion6": c6_eval
        },
        "gap_summary": {
            "total_gaps": len(all_gaps),
            "critical_count": len(critical_gaps),
            "major_count": len(major_gaps),
            "minor_count": len(minor_gaps),
            "critical_gaps": critical_gaps,
            "major_gaps": major_gaps,
            "minor_gaps": minor_gaps
        }
    }
