"""
AI-NBA Readiness System — Backend
app/business_rules/criterion6_rules.py

Deterministic evaluation rules for NBA Criterion 6:
Facilities and Technical Support.

ALL thresholds and scoring weights below are PLACEHOLDERS marked [PLACEHOLDER].
No official NBA Criterion 6 thresholds are implemented here.
"""

from __future__ import annotations

from typing import Any

from app.business_rules.readiness_rules import (
    EvaluationResult,
    RequirementStatus,
    _missing_data_warning,
)


RULE_LAB_FACILITY = "criterion6.lab_facility_availability"


def evaluate_lab_facility(context: dict[str, Any]) -> EvaluationResult:
    """
    Placeholder: evaluate lab facility availability.

    Expected context keys:
        labs_required   int  [PLACEHOLDER]
        labs_available  int  [PLACEHOLDER]
    """
    required = context.get("labs_required")
    available = context.get("labs_available")

    if required is None or available is None:
        return _missing_data_warning(
            rule=RULE_LAB_FACILITY,
            missing=["labs_required", "labs_available"],
            max_score=20.0,  # [PLACEHOLDER]
        )

    if required == 0:
        return EvaluationResult(
            status=RequirementStatus.NOT_APPLICABLE,
            score_attained=0.0,
            max_score=20.0,
            deterministic_metrics={"labs_required": 0, "labs_available": 0},
            limitations=["No lab requirement specified."],
        )

    ratio = available / required
    pct = min(ratio * 100, 100)

    if pct >= 100:
        status = RequirementStatus.PASS
    elif pct >= 75:
        status = RequirementStatus.WARNING
    else:
        status = RequirementStatus.FAIL

    return EvaluationResult(
        status=status,
        score_attained=round((pct / 100) * 20, 2),
        max_score=20.0,
        deterministic_metrics={
            "labs_required": required,
            "labs_available": available,
            "availability_pct": round(pct, 2),
        },
        limitations=[],
    )


CRITERION6_RULES: dict[str, Any] = {
    RULE_LAB_FACILITY: evaluate_lab_facility,
}
