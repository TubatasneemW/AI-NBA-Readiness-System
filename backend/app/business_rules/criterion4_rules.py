"""
AI-NBA Readiness System — Backend
app/business_rules/criterion4_rules.py

Deterministic evaluation rules for NBA Criterion 4:
Students'' Performance.

ALL thresholds and scoring weights below are PLACEHOLDERS marked [PLACEHOLDER].
They must be confirmed from official NBA SAR documents before use in a real
accreditation submission.
"""

from __future__ import annotations

from typing import Any

from app.business_rules.readiness_rules import (
    EvaluationResult,
    RequirementStatus,
    _missing_data_warning,
)


RULE_PASS_PERCENTAGE = "criterion4.pass_percentage"


def evaluate_pass_percentage(context: dict[str, Any]) -> EvaluationResult:
    """
    Evaluate the batch pass percentage for a department / academic year.

    Expected context keys:
        registered_students int
        passed_students     int
    """
    registered = context.get("registered_students")
    passed = context.get("passed_students")

    if registered is None or passed is None:
        return _missing_data_warning(
            rule=RULE_PASS_PERCENTAGE,
            missing=["registered_students", "passed_students"],
            max_score=20.0,  # [PLACEHOLDER]
        )

    if registered == 0:
        return EvaluationResult(
            status=RequirementStatus.NOT_APPLICABLE,
            score_attained=0.0,
            max_score=20.0,  # [PLACEHOLDER]
            deterministic_metrics={"registered_students": 0, "passed_students": 0},
            limitations=["No registered students found."],
        )

    pass_pct = (passed / registered) * 100

    # [PLACEHOLDER] Thresholds: >= 80% PASS, >= 60% WARNING, else FAIL
    if pass_pct >= 80:
        status = RequirementStatus.PASS
    elif pass_pct >= 60:
        status = RequirementStatus.WARNING
    else:
        status = RequirementStatus.FAIL

    return EvaluationResult(
        status=status,
        score_attained=round((pass_pct / 100) * 20, 2),
        max_score=20.0,
        deterministic_metrics={
            "registered_students": registered,
            "passed_students": passed,
            "pass_percentage": round(pass_pct, 2),
        },
        limitations=[],
    )


CRITERION4_RULES: dict[str, Any] = {
    RULE_PASS_PERCENTAGE: evaluate_pass_percentage,
}
