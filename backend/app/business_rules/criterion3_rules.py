"""
AI-NBA Readiness System — Backend
app/business_rules/criterion3_rules.py

Deterministic evaluation rules for NBA Criterion 3:
Course Outcomes & Program Outcomes (CO-PO Attainment).

IMPORTANT PLACEHOLDERS
----------------------
All threshold values below are labelled [PLACEHOLDER] and must be confirmed
from the institution''s official NBA SAR or departmental evaluation policy
before use in an actual accreditation submission.  Do not treat these values
as official NBA requirements.

Rule contract
-------------
Every rule function receives a `context` dict containing structured data
fetched from the backend database, and returns an EvaluationResult named-tuple:

    EvaluationResult(
        status:             RequirementStatus value string
        score_attained:     float
        max_score:          float
        deterministic_metrics: dict
        limitations:        list[str]
    )

Numerical calculations are performed entirely in Python.
The LLM must not be consulted for numerical results or compliance decisions.
"""

from __future__ import annotations

from typing import Any

from app.business_rules.readiness_rules import (
    EvaluationResult,
    RequirementStatus,
    _missing_data_warning,
)


# ---------------------------------------------------------------------------
# Rule: C3.PLACEHOLDER_1 — CO Definition Completeness
# ---------------------------------------------------------------------------
# [PLACEHOLDER] Checks whether COs are defined for every subject in the
# academic year.  Threshold: 100% subjects must have >= 1 CO.
# ---------------------------------------------------------------------------

RULE_CO_COMPLETENESS = "criterion3.co_definition_completeness"


def evaluate_co_completeness(context: dict[str, Any]) -> EvaluationResult:
    """
    Check that all subjects in the academic year have at least one CO defined.

    Expected context keys:
        total_subjects      int — total subjects in the year/department
        subjects_with_cos   int — subjects that have >= 1 CO defined
    """
    total = context.get("total_subjects")
    with_cos = context.get("subjects_with_cos")

    if total is None or with_cos is None:
        return _missing_data_warning(
            rule=RULE_CO_COMPLETENESS,
            missing=["total_subjects", "subjects_with_cos"],
        )

    if total == 0:
        return EvaluationResult(
            status=RequirementStatus.NOT_APPLICABLE.value,
            score_attained=0.0,
            max_score=10.0,  # [PLACEHOLDER]
            deterministic_metrics={"total_subjects": total, "subjects_with_cos": with_cos},
            limitations=["No subjects found for this academic year."],
        )

    coverage_pct = (with_cos / total) * 100

    # [PLACEHOLDER] Threshold: 100% required
    if coverage_pct >= 100:
        status = RequirementStatus.PASS.value
    elif coverage_pct >= 80:
        status = RequirementStatus.WARNING.value
    else:
        status = RequirementStatus.FAIL.value

    return EvaluationResult(
        status=status,
        score_attained=round((coverage_pct / 100) * 10, 2),  # [PLACEHOLDER] max 10
        max_score=10.0,
        deterministic_metrics={
            "total_subjects": total,
            "subjects_with_cos": with_cos,
            "co_coverage_pct": round(coverage_pct, 2),
        },
        limitations=[],
    )


# ---------------------------------------------------------------------------
# Rule: C3.PLACEHOLDER_2 — CO-PO Mapping Completeness
# ---------------------------------------------------------------------------
# [PLACEHOLDER] Checks whether every CO is mapped to at least one PO.
# ---------------------------------------------------------------------------

RULE_COPO_MAPPING = "criterion3.copo_mapping_completeness"


def evaluate_copo_mapping(context: dict[str, Any]) -> EvaluationResult:
    """
    Check that every Course Outcome is mapped to at least one Program Outcome.

    Expected context keys:
        total_cos       int
        cos_with_po_map int
    """
    total_cos = context.get("total_cos")
    mapped = context.get("cos_with_po_map")

    if total_cos is None or mapped is None:
        return _missing_data_warning(
            rule=RULE_COPO_MAPPING,
            missing=["total_cos", "cos_with_po_map"],
        )

    if total_cos == 0:
        return EvaluationResult(
            status=RequirementStatus.NOT_APPLICABLE.value,
            score_attained=0.0,
            max_score=10.0,  # [PLACEHOLDER]
            deterministic_metrics={"total_cos": total_cos, "cos_with_po_map": mapped},
            limitations=["No COs found."],
        )

    pct = (mapped / total_cos) * 100
    status = (
        RequirementStatus.PASS.value if pct >= 100
        else RequirementStatus.WARNING.value if pct >= 80
        else RequirementStatus.FAIL.value
    )

    return EvaluationResult(
        status=status,
        score_attained=round((pct / 100) * 10, 2),
        max_score=10.0,
        deterministic_metrics={
            "total_cos": total_cos,
            "cos_with_po_map": mapped,
            "mapping_coverage_pct": round(pct, 2),
        },
        limitations=[],
    )


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

CRITERION3_RULES: dict[str, Any] = {
    RULE_CO_COMPLETENESS: evaluate_co_completeness,
    RULE_COPO_MAPPING: evaluate_copo_mapping,
}
