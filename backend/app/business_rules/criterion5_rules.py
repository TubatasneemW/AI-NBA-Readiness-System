"""
AI-NBA Readiness System — Backend
app/business_rules/criterion5_rules.py

Deterministic evaluation rules for NBA Criterion 5:
Faculty Information and Contributions.

ALL thresholds and scoring weights below are PLACEHOLDERS marked [PLACEHOLDER].
"""

from __future__ import annotations

from typing import Any

from app.business_rules.readiness_rules import (
    EvaluationResult,
    RequirementStatus,
    _missing_data_warning,
)


RULE_FACULTY_QUALIFICATION = "criterion5.faculty_qualification_ratio"


def evaluate_faculty_qualification(context: dict[str, Any]) -> EvaluationResult:
    """
    Evaluate ratio of faculty with required minimum qualification.

    Expected context keys:
        total_faculty           int
        faculty_with_pg_or_phd  int  (postgraduate or doctoral qualification)
    """
    total = context.get("total_faculty")
    qualified = context.get("faculty_with_pg_or_phd")

    if total is None or qualified is None:
        return _missing_data_warning(
            rule=RULE_FACULTY_QUALIFICATION,
            missing=["total_faculty", "faculty_with_pg_or_phd"],
            max_score=20.0,  # [PLACEHOLDER]
        )

    if total == 0:
        return EvaluationResult(
            status=RequirementStatus.NOT_APPLICABLE,
            score_attained=0.0,
            max_score=20.0,
            deterministic_metrics={"total_faculty": 0, "faculty_with_pg_or_phd": 0},
            limitations=["No faculty records found for this department."],
        )

    ratio_pct = (qualified / total) * 100

    # [PLACEHOLDER] >= 80% PASS, >= 60% WARNING, else FAIL
    if ratio_pct >= 80:
        status = RequirementStatus.PASS
    elif ratio_pct >= 60:
        status = RequirementStatus.WARNING
    else:
        status = RequirementStatus.FAIL

    return EvaluationResult(
        status=status,
        score_attained=round((ratio_pct / 100) * 20, 2),
        max_score=20.0,
        deterministic_metrics={
            "total_faculty": total,
            "faculty_with_pg_or_phd": qualified,
            "qualification_ratio_pct": round(ratio_pct, 2),
        },
        limitations=[],
    )


CRITERION5_RULES: dict[str, Any] = {
    RULE_FACULTY_QUALIFICATION: evaluate_faculty_qualification,
}
