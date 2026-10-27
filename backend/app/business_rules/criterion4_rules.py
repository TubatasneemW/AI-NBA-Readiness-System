# criterion4_rules.py
"""
NBA Criterion 4 Business Rules: Students' Performance.

NBA Guidelines:
1. Enrolment and Academic Progression:
   - Success rate without backlogs (Benchmark >= 60% for optimal NBA score).
   - Overall graduation rate (Benchmark >= 80%).
2. Placement, Higher Studies, and Entrepreneurship:
   - Placement + Higher Education + Entrepreneurship rate:
     - >= 80%: Full marks (Compliant - Strong)
     - 60% - 79.9%: Partial marks (Compliant - Acceptable)
     - 40% - 59.9%: Marginal / Needs Improvement
     - < 40%: Deficient
3. Student Professional Achievements:
   - Technical competitions, paper presentations, hackathons.
   - All claims must have verifiable documentary evidence (Certificates).
"""

from typing import Any, Dict, List
from app.services.metrics_service import (
    calculate_criterion4_progression_metrics,
    calculate_criterion4_placement_metrics,
    summarize_student_achievements
)


def evaluate_criterion4_compliance(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deterministically evaluate Criterion 4 student performance and progression
    against NBA accreditation rubrics.
    """
    gaps: List[Dict[str, Any]] = []
    total_checks = 4
    passed_checks = 0

    cohort_records = data.get("cohorts", [])
    placement_records = data.get("placements", [])
    achievement_records = data.get("achievements", [])

    # 1. Academic Progression Rate
    prog_metrics = calculate_criterion4_progression_metrics(cohort_records)
    if prog_metrics.get("cohort_count", 0) > 0:
        agg = prog_metrics.get("aggregate", {})
        rate_without_backlog = agg.get("aggregate_completion_rate_without_backlog_pct", 0.0)
        overall_rate = agg.get("aggregate_overall_completion_rate_pct", 0.0)

        if rate_without_backlog >= 60.0 and overall_rate >= 80.0:
            passed_checks += 1
        elif overall_rate >= 70.0:
            passed_checks += 0.5
            gaps.append({
                "id": "C4-GAP-001",
                "criterion": "Criterion 4",
                "rule": "Academic Progression Rate",
                "severity": "Major",
                "description": f"Completion without backlog ({rate_without_backlog}%) is below optimal NBA target (60%).",
                "evidence_required": "Remedial Coaching Records and Mentorship Logs"
            })
        else:
            gaps.append({
                "id": "C4-GAP-001",
                "criterion": "Criterion 4",
                "rule": "Academic Progression Rate",
                "severity": "Critical",
                "description": f"Overall graduation rate ({overall_rate}%) is low (< 70%).",
                "evidence_required": "Student Support Policy and Academic Retention Analysis"
            })
    else:
        gaps.append({
            "id": "C4-GAP-001",
            "criterion": "Criterion 4",
            "rule": "Academic Progression Data",
            "severity": "Critical",
            "description": "No cohort progression data provided.",
            "evidence_required": "Official Cohort Enrolment and Graduation Registers"
        })

    # 2. Placement, Higher Studies, and Entrepreneurship
    place_metrics = calculate_criterion4_placement_metrics(placement_records)
    if place_metrics.get("year_count", 0) > 0:
        agg_place = place_metrics.get("aggregate", {})
        progression_rate = agg_place.get("aggregate_progression_pct", 0.0)

        if progression_rate >= 80.0:
            passed_checks += 1
        elif progression_rate >= 60.0:
            passed_checks += 0.75
            gaps.append({
                "id": "C4-GAP-002",
                "criterion": "Criterion 4",
                "rule": "Career Progression Rate",
                "severity": "Minor",
                "description": f"Placement and progression rate is {progression_rate}%. Target for full score is >= 80%.",
                "evidence_required": "Training & Placement Cell Annual Report and Offer Letters"
            })
        else:
            gaps.append({
                "id": "C4-GAP-002",
                "criterion": "Criterion 4",
                "rule": "Career Progression Rate",
                "severity": "Major",
                "description": f"Placement and progression rate ({progression_rate}%) is below 60%.",
                "evidence_required": "Career Guidance and Industry Interaction Action Plan"
            })
    else:
        gaps.append({
            "id": "C4-GAP-002",
            "criterion": "Criterion 4",
            "rule": "Placement Records",
            "severity": "Critical",
            "description": "No placement or higher education records provided.",
            "evidence_required": "Verified Placement Registers and Higher Education Admission Proofs"
        })

    # 3. Student Professional Achievements & Verification
    achieve_summary = summarize_student_achievements(achievement_records)
    total_ach = achieve_summary.get("total_achievements", 0)
    verified_ach = achieve_summary.get("verification_breakdown", {}).get("verified", 0)
    pending_ach = achieve_summary.get("verification_breakdown", {}).get("pending_verification", 0)

    if total_ach > 0:
        if pending_ach == 0:
            passed_checks += 1
        else:
            passed_checks += 0.5
            gaps.append({
                "id": "C4-GAP-003",
                "criterion": "Criterion 4",
                "rule": "Achievement Verification",
                "severity": "Minor",
                "description": f"{pending_ach} out of {total_ach} student achievements are missing verification proof documents.",
                "evidence_required": "Participation and Award Certificates for Pending Entries"
            })
    else:
        gaps.append({
            "id": "C4-GAP-003",
            "criterion": "Criterion 4",
            "rule": "Student Achievements",
            "severity": "Major",
            "description": "No student co-curricular, technical, or sports achievements logged.",
            "evidence_required": "Student Activity Register and Event Participation Certificates"
        })

    # 4. Competitive Examinations Data
    if data.get("competitive_exams") is not None:
        passed_checks += 1
    else:
        gaps.append({
            "id": "C4-GAP-004",
            "criterion": "Criterion 4",
            "rule": "Competitive Examinations",
            "severity": "Minor",
            "description": "Data on competitive exams (GATE, CAT, GRE, TOEFL, IELTS) is not documented.",
            "evidence_required": "Student Scorecards for Competitive Examinations"
        })

    completeness_pct = round((passed_checks / total_checks) * 100, 2)
    if completeness_pct >= 85:
        status = "Compliant"
    elif completeness_pct >= 60:
        status = "Partially Compliant"
    else:
        status = "Needs Improvement"

    return {
        "criterion": "Criterion 4",
        "completeness_percentage": completeness_pct,
        "status": status,
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "progression_metrics": prog_metrics,
        "placement_metrics": place_metrics,
        "gaps_count": len(gaps),
        "gaps": gaps
    }
