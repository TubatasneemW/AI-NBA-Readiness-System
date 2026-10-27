# criterion5_rules.py
"""
NBA Criterion 5 Business Rules: Faculty Information and Contributions.

NBA Guidelines:
1. Student-to-Faculty Ratio (SFR):
   - Regular faculty counted against total sanctioned student intake across all years.
   - SFR <= 15.0: Compliant (Full Marks / 20)
   - 15.0 < SFR <= 20.0: Marginally Compliant (Pro-rata Marks)
   - 20.0 < SFR <= 25.0: Needs Improvement (Severe Penalty)
   - SFR > 25.0: Non-Compliant (0 Marks - Critical Deficiency)
2. Faculty Cadre Ratio:
   - Target ratio: 1 Professor : 2 Associate Professors : 6 Assistant Professors.
   - Cadre proportion compliance.
3. Faculty Qualification:
   - Ph.D. Faculty Percentage: Target >= 30% for Tier-II, >= 40% for Tier-I.
4. Faculty Retention:
   - Average stay in the institution >= 3.0 years (stability of faculty).
5. Document Verification:
   - 100% of faculty appointments and degrees must be verifiable with proof.
"""

from typing import Any, Dict, List
from app.services.metrics_service import (
    calculate_criterion5_sfr,
    calculate_criterion5_cadre_metrics,
    calculate_criterion5_experience_metrics
)


def evaluate_criterion5_compliance(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deterministically evaluate Criterion 5 faculty data against NBA rubrics.
    """
    gaps: List[Dict[str, Any]] = []
    total_checks = 5
    passed_checks = 0

    faculty_records = data.get("faculty_members", [])
    total_students = int(data.get("total_enrolled_students", 0))

    # 1. Student-to-Faculty Ratio (SFR)
    sfr_metrics = calculate_criterion5_sfr(total_students, len(faculty_records))
    sfr = sfr_metrics.get("sfr_ratio") or sfr_metrics.get("student_to_faculty_ratio") or 0.0

    if sfr > 0:
        if sfr <= 15.0:
            passed_checks += 1
        elif sfr <= 20.0:
            passed_checks += 0.7
            gaps.append({
                "id": "C5-GAP-001",
                "criterion": "Criterion 5",
                "rule": "Student-to-Faculty Ratio",
                "severity": "Minor",
                "description": f"SFR is {sfr}:1. Optimal target for full marks is <= 15:1.",
                "evidence_required": "Faculty Recruitment Plan and Workload Distribution Matrix"
            })
        elif sfr <= 25.0:
            passed_checks += 0.3
            gaps.append({
                "id": "C5-GAP-001",
                "criterion": "Criterion 5",
                "rule": "Student-to-Faculty Ratio",
                "severity": "Major",
                "description": f"SFR is {sfr}:1, which incurs an NBA penalty. Recommended <= 20:1.",
                "evidence_required": "Urgent Faculty Recruitment Sanction Order"
            })
        else:
            gaps.append({
                "id": "C5-GAP-001",
                "criterion": "Criterion 5",
                "rule": "Student-to-Faculty Ratio",
                "severity": "Critical",
                "description": f"SFR is {sfr}:1, which exceeds the NBA ceiling of 25:1 (Zero marks).",
                "evidence_required": "Emergency Faculty Hiring and Board Approval"
            })
    else:
        gaps.append({
            "id": "C5-GAP-001",
            "criterion": "Criterion 5",
            "rule": "Student-to-Faculty Ratio",
            "severity": "Critical",
            "description": "Student intake or faculty count is zero or missing.",
            "evidence_required": "Sanctioned Student Intake and Faculty Appointment Orders"
        })

    # 2. Cadre Ratio
    cadre_metrics = calculate_criterion5_cadre_metrics(faculty_records)
    cadre_counts = cadre_metrics.get("cadre_counts", {})
    profs = cadre_counts.get("professors", 0)
    assoc_profs = cadre_counts.get("associate_professors", 0)
    asst_profs = cadre_counts.get("assistant_professors", 0)

    if profs >= 1 and assoc_profs >= 2:
        passed_checks += 1
    elif profs >= 1 or assoc_profs >= 1:
        passed_checks += 0.5
        gaps.append({
            "id": "C5-GAP-002",
            "criterion": "Criterion 5",
            "rule": "Cadre Ratio",
            "severity": "Major",
            "description": f"Cadre distribution ({profs}:{assoc_profs}:{asst_profs}) has deficit in Professors/Associate Professors against NBA norm (1:2:6).",
            "evidence_required": "Cadre Promotion Policy and CAS Documentation"
        })
    else:
        gaps.append({
            "id": "C5-GAP-002",
            "criterion": "Criterion 5",
            "rule": "Cadre Ratio",
            "severity": "Critical",
            "description": "Senior faculty shortage: No full Professors or Associate Professors in the cadre.",
            "evidence_required": "Senior Faculty Recruitment and Retention Strategy"
        })

    # 3. Faculty Qualification (Ph.D. Percentage)
    qual = cadre_metrics.get("qualifications", {})
    phd_pct = qual.get("phd_percentage", 0.0)

    if phd_pct >= 30.0:
        passed_checks += 1
    elif phd_pct >= 20.0:
        passed_checks += 0.5
        gaps.append({
            "id": "C5-GAP-003",
            "criterion": "Criterion 5",
            "rule": "Faculty Ph.D. Ratio",
            "severity": "Major",
            "description": f"Faculty with Ph.D. is {phd_pct}%. NBA minimum benchmark is >= 30%.",
            "evidence_required": "Faculty Quality Improvement (QIP) and Ph.D. Enrolment Orders"
        })
    else:
        gaps.append({
            "id": "C5-GAP-003",
            "criterion": "Criterion 5",
            "rule": "Faculty Ph.D. Ratio",
            "severity": "Critical",
            "description": f"Critically low Ph.D. faculty ratio ({phd_pct}%). Benchmark is >= 30%.",
            "evidence_required": "Ph.D. Hiring Mandate and Faculty Higher Education Support"
        })

    # 4. Faculty Retention / Institutional Stability
    exp_metrics = calculate_criterion5_experience_metrics(faculty_records)
    avg_inst_exp = exp_metrics.get("average_institution_experience_years", 0.0)

    if avg_inst_exp >= 3.0:
        passed_checks += 1
    elif avg_inst_exp >= 1.5:
        passed_checks += 0.5
        gaps.append({
            "id": "C5-GAP-004",
            "criterion": "Criterion 5",
            "rule": "Faculty Retention",
            "severity": "Minor",
            "description": f"Average institution experience is {avg_inst_exp} years (target >= 3.0 years).",
            "evidence_required": "Faculty Service Registers and Retention Policy"
        })
    else:
        gaps.append({
            "id": "C5-GAP-004",
            "criterion": "Criterion 5",
            "rule": "Faculty Retention",
            "severity": "Major",
            "description": f"High faculty turnover: average institutional stay is only {avg_inst_exp} years.",
            "evidence_required": "Institutional Human Resources and Service Rule Audits"
        })

    # 5. Document Verification Audit
    unverified_faculty = [f for f in faculty_records if not f.get("verified", False)]
    if len(faculty_records) > 0 and len(unverified_faculty) == 0:
        passed_checks += 1
    elif len(faculty_records) > 0:
        passed_checks += 0.5
        gaps.append({
            "id": "C5-GAP-005",
            "criterion": "Criterion 5",
            "rule": "Faculty Profile Verification",
            "severity": "Major",
            "description": f"{len(unverified_faculty)} faculty records are pending official HR document verification.",
            "evidence_required": "Appointment Orders, Joining Reports, and Degree Certificates"
        })
    else:
        gaps.append({
            "id": "C5-GAP-005",
            "criterion": "Criterion 5",
            "rule": "Faculty Roster",
            "severity": "Critical",
            "description": "No faculty members submitted for verification.",
            "evidence_required": "Approved Department Faculty Roster"
        })

    completeness_pct = round((passed_checks / total_checks) * 100, 2)
    if completeness_pct >= 85:
        status = "Compliant"
    elif completeness_pct >= 60:
        status = "Partially Compliant"
    else:
        status = "Needs Improvement"

    return {
        "criterion": "Criterion 5",
        "completeness_percentage": completeness_pct,
        "status": status,
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "sfr_metrics": sfr_metrics,
        "cadre_metrics": cadre_metrics,
        "experience_metrics": exp_metrics,
        "gaps_count": len(gaps),
        "gaps": gaps
    }
