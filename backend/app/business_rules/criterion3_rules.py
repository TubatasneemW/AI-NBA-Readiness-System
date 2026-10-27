# criterion3_rules.py
"""
NBA Criterion 3 Business Rules: Course Outcomes and Program Outcomes.

NBA Guidelines:
1. Course Outcomes (COs) must be defined for all courses (typically 4-6 COs per course)
   aligned with Bloom's Taxonomy cognitive levels.
2. Assessment Scheme must cover both Continuous Internal Evaluation (CIE) and
   Semester End Examination (SEE) totaling 100 marks.
3. Assessment-to-CO Mapping: Every CO must be assessed by at least one internal
   or external assessment component.
4. CO-PO and CO-PSO Mapping: Correlation matrices must map COs to POs/PSOs
   with strength levels 1 (Slight/Low), 2 (Moderate/Medium), or 3 (Substantial/High).
5. Attainment Calculation: Clear methodology and target thresholds must be defined
   for direct (CIE + SEE) and indirect attainment.
"""

from typing import Any, Dict, List


def evaluate_criterion3_compliance(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deterministically evaluate Criterion 3 course and assessment data
    against NBA accreditation rubrics.
    """
    gaps: List[Dict[str, Any]] = []
    total_checks = 6
    passed_checks = 0

    # 1. Course Outcomes Definition Check
    cos = data.get("course_outcomes", [])
    if cos and len(cos) >= 4:
        passed_checks += 1
    elif cos:
        passed_checks += 0.5
        gaps.append({
            "id": "C3-GAP-001",
            "criterion": "Criterion 3",
            "rule": "Course Outcomes Count",
            "severity": "Minor",
            "description": f"Only {len(cos)} COs defined. NBA recommends 4 to 6 COs per course.",
            "evidence_required": "Updated Course Syllabus and Course Articulation Matrix"
        })
    else:
        gaps.append({
            "id": "C3-GAP-001",
            "criterion": "Criterion 3",
            "rule": "Course Outcomes Count",
            "severity": "Critical",
            "description": "No Course Outcomes (COs) defined for the course.",
            "evidence_required": "Approved Course Syllabus with CO statements"
        })

    # 2. Assessment Scheme Coverage
    scheme = data.get("assessment_scheme", {})
    if scheme and ("CIE" in scheme or "CIE-I" in scheme) and ("SEE" in scheme or "End Semester" in scheme):
        passed_checks += 1
    elif scheme:
        passed_checks += 0.5
        gaps.append({
            "id": "C3-GAP-002",
            "criterion": "Criterion 3",
            "rule": "Assessment Scheme",
            "severity": "Major",
            "description": "Incomplete assessment scheme: CIE or SEE component missing.",
            "evidence_required": "Academic Regulations and Assessment Weightage Scheme"
        })
    else:
        gaps.append({
            "id": "C3-GAP-002",
            "criterion": "Criterion 3",
            "rule": "Assessment Scheme",
            "severity": "Critical",
            "description": "No formal assessment scheme defined.",
            "evidence_required": "Institutional Examination and Evaluation Manual"
        })

    # 3. Assessment to CO Mapping
    assessment_mapping = data.get("assessment_co_mapping", {})
    if assessment_mapping and len(assessment_mapping) >= 2:
        passed_checks += 1
    else:
        gaps.append({
            "id": "C3-GAP-003",
            "criterion": "Criterion 3",
            "rule": "Assessment-to-CO Mapping",
            "severity": "Major",
            "description": "Assessment-to-CO mapping table is incomplete or missing.",
            "evidence_required": "Assessment Mapping Matrix linking questions/tools to COs"
        })

    # 4. CO-PO-PSO Mapping
    co_po_mapping = data.get("co_po_pso_mapping", {})
    if co_po_mapping and len(co_po_mapping) >= 4:
        passed_checks += 1
    elif co_po_mapping:
        passed_checks += 0.5
        gaps.append({
            "id": "C3-GAP-004",
            "criterion": "Criterion 3",
            "rule": "CO-PO Mapping Matrix",
            "severity": "Minor",
            "description": "CO-PO-PSO mapping is only partially specified.",
            "evidence_required": "Complete Program Articulation Matrix (CO-PO-PSO)"
        })
    else:
        gaps.append({
            "id": "C3-GAP-004",
            "criterion": "Criterion 3",
            "rule": "CO-PO Mapping Matrix",
            "severity": "Critical",
            "description": "No CO-PO-PSO correlation matrix available.",
            "evidence_required": "Department Curriculum Book with CO-PO Mapping"
        })

    # 5. Attainment Calculation Methodology
    data_quality = data.get("data_quality", {})
    co_formula_present = data_quality.get("official_co_attainment_formula_available", False)
    if co_formula_present:
        passed_checks += 1
    else:
        gaps.append({
            "id": "C3-GAP-005",
            "criterion": "Criterion 3",
            "rule": "CO Attainment Formula",
            "severity": "Critical",
            "description": "Official CO direct attainment calculation formula and threshold not documented.",
            "evidence_required": "Departmental Assessment and Attainment Policy Document"
        })

    # 6. Student-Level Evidence Availability (SEE marks & question marks)
    see_marks_present = data_quality.get("student_level_see_marks_available", False)
    if see_marks_present:
        passed_checks += 1
    else:
        gaps.append({
            "id": "C3-GAP-006",
            "criterion": "Criterion 3",
            "rule": "Summative Assessment Data",
            "severity": "Major",
            "description": "Student-level SEE component marks are missing; only course-level grade distribution available.",
            "evidence_required": "University / Controller of Examinations Mark Sheets"
        })

    completeness_pct = round((passed_checks / total_checks) * 100, 2)
    if completeness_pct >= 85:
        status = "Compliant"
    elif completeness_pct >= 60:
        status = "Partially Compliant"
    else:
        status = "Needs Improvement"

    return {
        "criterion": "Criterion 3",
        "completeness_percentage": completeness_pct,
        "status": status,
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "gaps_count": len(gaps),
        "gaps": gaps
    }
