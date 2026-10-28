"""
AI-NBA Readiness System — Backend
app/business_rules/criterion3_rules.py

Deterministic evaluation rules for NBA Criterion 3:
Course Outcomes & Program Outcomes (CO-PO Attainment).
Total: 120 marks.

Sources:
  NBA Manual for UG Engineering Tier I — 2026 Edition
  Annexure VII, Criterion 3 (pp. 155-157)
  Working Rulebook: NBA_Criteria_3_4_5_6_Rulebook_2026_Manual_v2.docx

Rule contract:
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
    _needs_clarification,
)


# ---------------------------------------------------------------------------
# 3.1  Continuous Assessment / CO Definition Completeness (10 marks)
# ---------------------------------------------------------------------------

RULE_CO_COMPLETENESS = "criterion3.co_definition_completeness"
RULE_CONTINUOUS_ASSESSMENT = "criterion3.continuous_assessment"


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
            max_score=10.0,
        )

    if total == 0:
        return EvaluationResult(
            status=RequirementStatus.NOT_APPLICABLE.value,
            score_attained=0.0,
            max_score=10.0,
            deterministic_metrics={"total_subjects": total, "subjects_with_cos": with_cos},
            limitations=["No subjects found for this academic year."],
        )

    coverage_pct = (with_cos / total) * 100

    if coverage_pct >= 100:
        status = RequirementStatus.PASS.value
    elif coverage_pct >= 80:
        status = RequirementStatus.WARNING.value
    else:
        status = RequirementStatus.FAIL.value

    return EvaluationResult(
        status=status,
        score_attained=round((coverage_pct / 100) * 10, 2),
        max_score=10.0,
        deterministic_metrics={
            "total_subjects": total,
            "subjects_with_cos": with_cos,
            "co_coverage_pct": round(coverage_pct, 2),
        },
        limitations=[],
    )


# ---------------------------------------------------------------------------
# 3.2  CO-PO Mapping Completeness (10 marks)
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
            max_score=10.0,
        )

    if total_cos == 0:
        return EvaluationResult(
            status=RequirementStatus.NOT_APPLICABLE.value,
            score_attained=0.0,
            max_score=10.0,
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
# 3.3  SEE Question Paper Quality (10 marks)
# ---------------------------------------------------------------------------

RULE_SEE_QUESTION_PAPER = "criterion3.see_question_paper"


def evaluate_see_question_paper(context: dict[str, Any]) -> EvaluationResult:
    """
    3.3 Quality of Semester End Examination Question Papers (10 marks).
    Qualitative rubric / reviewer-evaluated.
    """
    score = context.get("reviewer_score")
    if score is None:
        return _missing_data_warning(
            rule=RULE_SEE_QUESTION_PAPER,
            missing=["reviewer_score"],
            max_score=10.0,
        )
    score = max(0.0, min(float(score), 10.0))
    status = (
        RequirementStatus.PASS.value if score >= 7.0
        else RequirementStatus.WARNING.value if score >= 4.0
        else RequirementStatus.FAIL.value
    )
    return EvaluationResult(
        status=status,
        score_attained=round(score, 2),
        max_score=10.0,
        deterministic_metrics={"reviewer_score": score},
        limitations=["Qualitative rubric; score entered by NBA reviewer."],
    )


# ---------------------------------------------------------------------------
# 3.4  Lab and Workshop Conduct (10 marks)
# ---------------------------------------------------------------------------

RULE_LAB_WORKSHOP = "criterion3.lab_workshop"


def evaluate_lab_workshop(context: dict[str, Any]) -> EvaluationResult:
    """
    3.4 Lab and Workshop Conduct (10 marks).
    Qualitative rubric / reviewer-evaluated.
    """
    score = context.get("reviewer_score")
    if score is None:
        return _missing_data_warning(
            rule=RULE_LAB_WORKSHOP,
            missing=["reviewer_score"],
            max_score=10.0,
        )
    score = max(0.0, min(float(score), 10.0))
    status = (
        RequirementStatus.PASS.value if score >= 7.0
        else RequirementStatus.WARNING.value if score >= 4.0
        else RequirementStatus.FAIL.value
    )
    return EvaluationResult(
        status=status,
        score_attained=round(score, 2),
        max_score=10.0,
        deterministic_metrics={"reviewer_score": score},
        limitations=["Qualitative rubric; score entered by NBA reviewer."],
    )


# ---------------------------------------------------------------------------
# 3.4  Industrial Training / Internship (10 marks)
# ---------------------------------------------------------------------------

RULE_INDUSTRIAL_TRAINING = "criterion3.industrial_training"


def evaluate_industrial_training(context: dict[str, Any]) -> EvaluationResult:
    """
    3.4 Evaluation of Industrial Training or Internship Programs (10 marks).
    Qualitative rubric / reviewer-evaluated.
    Manual Annexure VII, p. 156: 10 marks max.
    """
    score = context.get("reviewer_score")
    if score is None:
        return _missing_data_warning(
            rule=RULE_INDUSTRIAL_TRAINING,
            missing=["reviewer_score"],
            max_score=10.0,
        )
    score = max(0.0, min(float(score), 10.0))
    status = (
        RequirementStatus.PASS.value if score >= 7.0
        else RequirementStatus.WARNING.value if score >= 4.0
        else RequirementStatus.FAIL.value
    )
    return EvaluationResult(
        status=status,
        score_attained=round(score, 2),
        max_score=10.0,
        deterministic_metrics={"reviewer_score": score},
        limitations=["Qualitative rubric; score entered by NBA reviewer."],
    )


# ---------------------------------------------------------------------------
# 3.5  Project Evaluation (20 marks)
# ---------------------------------------------------------------------------

RULE_PROJECT_EVALUATION = "criterion3.project_evaluation"


def evaluate_project_evaluation(context: dict[str, Any]) -> EvaluationResult:
    """
    3.5 Evaluation of Projects (20 marks).
    Qualitative rubric / reviewer-evaluated.
    Manual Annexure VII, p. 156: 20 marks max.
    """
    score = context.get("reviewer_score")
    if score is None:
        return _missing_data_warning(
            rule=RULE_PROJECT_EVALUATION,
            missing=["reviewer_score"],
            max_score=20.0,
        )
    score = max(0.0, min(float(score), 20.0))
    status = (
        RequirementStatus.PASS.value if score >= 14.0
        else RequirementStatus.WARNING.value if score >= 8.0
        else RequirementStatus.FAIL.value
    )
    return EvaluationResult(
        status=status,
        score_attained=round(score, 2),
        max_score=20.0,
        deterministic_metrics={"reviewer_score": score},
        limitations=["Qualitative rubric; score entered by NBA reviewer."],
    )


# ---------------------------------------------------------------------------
# 3.6  Sustainable Development Goals (SDG) (10 marks)
# ---------------------------------------------------------------------------

RULE_SDG = "criterion3.sdg_evidence"


def evaluate_sdg_evidence(context: dict[str, Any]) -> EvaluationResult:
    """
    3.6 Evidence of Addressing Sustainable Development Goals (SDG) (10 marks).
    Qualitative rubric / reviewer-evaluated.
    Manual Annexure VII, p. 156: 10 marks max.
    """
    score = context.get("reviewer_score")
    if score is None:
        return _missing_data_warning(
            rule=RULE_SDG,
            missing=["reviewer_score"],
            max_score=10.0,
        )
    score = max(0.0, min(float(score), 10.0))
    status = (
        RequirementStatus.PASS.value if score >= 7.0
        else RequirementStatus.WARNING.value if score >= 4.0
        else RequirementStatus.FAIL.value
    )
    return EvaluationResult(
        status=status,
        score_attained=round(score, 2),
        max_score=10.0,
        deterministic_metrics={"reviewer_score": score},
        limitations=["Qualitative rubric; score entered by NBA reviewer."],
    )


# ---------------------------------------------------------------------------
# 3.7  CO Attainment (25 marks)
# ---------------------------------------------------------------------------

RULE_CO_ATTAINMENT = "criterion3.co_attainment_tools"


def evaluate_co_attainment(context: dict[str, Any]) -> EvaluationResult:
    """
    3.7 Course Outcome Attainment (25 marks).

    NBA Tier-I requires institution-specific direct and indirect assessment
    processes. If attainment_formula_configured is False, returns
    NEEDS_RULE_CLARIFICATION.
    """
    configured = context.get("attainment_formula_configured", False)
    if not configured:
        return _needs_clarification(
            rule=RULE_CO_ATTAINMENT,
            reason=(
                "NBA Tier-I requires each institution to configure and approve "
                "its specific direct and indirect CO attainment calculation methodology. "
                "Set attainment_formula_configured=True with verified institutional thresholds."
            ),
            max_score=25.0,
        )

    score = context.get("attainment_score")
    if score is None:
        return _missing_data_warning(
            rule=RULE_CO_ATTAINMENT,
            missing=["attainment_score"],
            max_score=25.0,
        )
    score = max(0.0, min(float(score), 25.0))
    status = (
        RequirementStatus.PASS.value if score >= 17.5
        else RequirementStatus.WARNING.value if score >= 10.0
        else RequirementStatus.FAIL.value
    )
    return EvaluationResult(
        status=status,
        score_attained=round(score, 2),
        max_score=25.0,
        deterministic_metrics={"attainment_score": score},
        limitations=[],
    )


# ---------------------------------------------------------------------------
# 3.8  PO and PSO Attainment (25 marks)
# ---------------------------------------------------------------------------

RULE_PO_PSO_ATTAINMENT = "criterion3.po_pso_attainment"


def evaluate_po_pso_attainment(context: dict[str, Any]) -> EvaluationResult:
    """
    3.8 Program Outcomes and PSO Attainment (25 marks).

    NBA Tier-I requires institution-specific PO/PSO attainment calculation methodology.
    If attainment_formula_configured is False, returns NEEDS_RULE_CLARIFICATION.
    """
    configured = context.get("attainment_formula_configured", False)
    if not configured:
        return _needs_clarification(
            rule=RULE_PO_PSO_ATTAINMENT,
            reason=(
                "NBA Tier-I requires institutionally configured and approved "
                "PO/PSO attainment targets and assessment formulas. "
                "Set attainment_formula_configured=True with institutional benchmarks."
            ),
            max_score=25.0,
        )

    score = context.get("attainment_score")
    if score is None:
        return _missing_data_warning(
            rule=RULE_PO_PSO_ATTAINMENT,
            missing=["attainment_score"],
            max_score=25.0,
        )
    score = max(0.0, min(float(score), 25.0))
    status = (
        RequirementStatus.PASS.value if score >= 17.5
        else RequirementStatus.WARNING.value if score >= 10.0
        else RequirementStatus.FAIL.value
    )
    return EvaluationResult(
        status=status,
        score_attained=round(score, 2),
        max_score=25.0,
        deterministic_metrics={"attainment_score": score},
        limitations=[],
    )


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

CRITERION3_RULES: dict[str, Any] = {
    RULE_CO_COMPLETENESS: evaluate_co_completeness,
    RULE_CONTINUOUS_ASSESSMENT: evaluate_co_completeness,
    RULE_COPO_MAPPING: evaluate_copo_mapping,
    RULE_SEE_QUESTION_PAPER: evaluate_see_question_paper,
    RULE_LAB_WORKSHOP: evaluate_lab_workshop,
    RULE_INDUSTRIAL_TRAINING: evaluate_industrial_training,
    RULE_PROJECT_EVALUATION: evaluate_project_evaluation,
    RULE_SDG: evaluate_sdg_evidence,
    RULE_CO_ATTAINMENT: evaluate_co_attainment,
    RULE_PO_PSO_ATTAINMENT: evaluate_po_pso_attainment,
}
