# criterion6_rules.py
"""
NBA Criterion 6 Business Rules: Faculty Contributions, R&D, Consultancy, FDPs.

NBA Guidelines:
1. Research Publications:
   - Publications in high-impact indexed journals (SCI, SCIE, Scopus, UGC-CARE).
   - Target: >= 1 indexed paper per faculty per academic year.
2. Sponsored Research & Grants:
   - External funding from government (DST, AICTE, DRDO, etc.) or industry.
3. Industrial Consultancy:
   - Active consultancy with revenue generation.
4. Intellectual Property:
   - Patents filed, published, or granted.
5. Faculty Development Programs (FDPs / STTPs):
   - Regular participation and hosting of continuous education programs (>= 5 days).
6. Evidence Traceability:
   - Only confirmed, document-backed contributions are counted for NBA marks.
"""

from typing import Any, Dict, List
from app.services.metrics_service import (
    calculate_criterion6_publication_metrics,
    calculate_criterion6_patent_metrics,
    calculate_criterion6_project_metrics,
    calculate_criterion6_fdp_metrics
)


def evaluate_criterion6_compliance(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deterministically evaluate Criterion 6 faculty contributions against NBA rubrics.
    """
    gaps: List[Dict[str, Any]] = []
    total_checks = 5
    passed_checks = 0

    publications = data.get("publications", [])
    patents = data.get("patents", [])
    projects = data.get("sponsored_projects", [])
    consultancy = data.get("consultancy", [])
    fdps = data.get("fdps", [])

    # 1. Publications Check
    pub_metrics = calculate_criterion6_publication_metrics(publications)
    confirmed_pubs = pub_metrics.get("confirmed_publications_count", 0)
    sci_scopus = pub_metrics.get("sci_scopus_confirmed_count", 0)
    pending_pubs = pub_metrics.get("pending_verification_count", 0)

    if confirmed_pubs >= 3:
        if sci_scopus >= 2:
            passed_checks += 1
        else:
            passed_checks += 0.75
            gaps.append({
                "id": "C6-GAP-001",
                "criterion": "Criterion 6",
                "rule": "Journal Indexing Quality",
                "severity": "Minor",
                "description": f"Only {sci_scopus} publications are indexed in SCI/Scopus. Prioritize higher indexed venues.",
                "evidence_required": "Scopus / Web of Science Indexing Verification Pages"
            })
    elif confirmed_pubs > 0:
        passed_checks += 0.5
        gaps.append({
            "id": "C6-GAP-001",
            "criterion": "Criterion 6",
            "rule": "Research Publications Count",
            "severity": "Major",
            "description": f"Low publication volume ({confirmed_pubs} confirmed papers). Target >= 1 paper per faculty annually.",
            "evidence_required": "Journal Reprints, Conference Proceedings, and DOIs"
        })
    else:
        gaps.append({
            "id": "C6-GAP-001",
            "criterion": "Criterion 6",
            "rule": "Research Publications Count",
            "severity": "Critical",
            "description": "No confirmed research publications with documentary evidence.",
            "evidence_required": "Department Research Repository and Publication Reprints"
        })

    if pending_pubs > 0:
        gaps.append({
            "id": "C6-GAP-001B",
            "criterion": "Criterion 6",
            "rule": "Publication Verification",
            "severity": "Minor",
            "description": f"{pending_pubs} publications are pending DOI / proof document verification.",
            "evidence_required": "Paper DOIs and Acceptance/Publication Letters"
        })

    # 2. Intellectual Property (Patents)
    pat_metrics = calculate_criterion6_patent_metrics(patents)
    confirmed_pats = pat_metrics.get("confirmed_patents_count", 0)
    granted = pat_metrics.get("confirmed_granted_count", 0)
    published = pat_metrics.get("confirmed_published_count", 0)

    if confirmed_pats > 0 and (granted > 0 or published > 0):
        passed_checks += 1
    elif confirmed_pats > 0:
        passed_checks += 0.5
        gaps.append({
            "id": "C6-GAP-002",
            "criterion": "Criterion 6",
            "rule": "Patent Commercialization / Grant",
            "severity": "Minor",
            "description": "Patents are currently in Filed status; none yet Published or Granted.",
            "evidence_required": "Patent Journal Publication Gazette / Grant Certificates"
        })
    else:
        gaps.append({
            "id": "C6-GAP-002",
            "criterion": "Criterion 6",
            "rule": "Intellectual Property",
            "severity": "Major",
            "description": "No confirmed patent filings or grants recorded for the department.",
            "evidence_required": "Indian Patent Office Application Filing Receipts / Form 1"
        })

    # 3. Sponsored R&D Projects
    proj_metrics = calculate_criterion6_project_metrics(projects, consultancy)
    spons = proj_metrics.get("sponsored_projects", {})
    funding_lakhs = spons.get("total_funding_amount_lakhs", 0.0)

    if funding_lakhs >= 10.0:
        passed_checks += 1
    elif funding_lakhs > 0:
        passed_checks += 0.75
        gaps.append({
            "id": "C6-GAP-003",
            "criterion": "Criterion 6",
            "rule": "Sponsored Research Quantum",
            "severity": "Minor",
            "description": f"Sponsored research grant total is INR {funding_lakhs} Lakhs. Target for maximum score is >= 10 Lakhs.",
            "evidence_required": "Grant Sanction Orders and Fund Utilization Certificates"
        })
    else:
        gaps.append({
            "id": "C6-GAP-003",
            "criterion": "Criterion 6",
            "rule": "Sponsored Research",
            "severity": "Major",
            "description": "Zero sponsored research grants or external funding recorded.",
            "evidence_required": "Research Grant Applications and Sanction Letters"
        })

    # 4. Industry Consultancy Revenue
    consult = proj_metrics.get("consultancy", {})
    rev_lakhs = consult.get("total_revenue_amount_lakhs", 0.0)

    if rev_lakhs >= 2.0:
        passed_checks += 1
    elif rev_lakhs > 0:
        passed_checks += 0.5
        gaps.append({
            "id": "C6-GAP-004",
            "criterion": "Criterion 6",
            "rule": "Consultancy Revenue",
            "severity": "Minor",
            "description": f"Consultancy revenue is INR {rev_lakhs} Lakhs (benchmark >= 2 Lakhs).",
            "evidence_required": "Client Invoices, Bank Remittance Proofs, and MoUs"
        })
    else:
        gaps.append({
            "id": "C6-GAP-004",
            "criterion": "Criterion 6",
            "rule": "Industrial Consultancy",
            "severity": "Major",
            "description": "No industrial consultancy revenue logged.",
            "evidence_required": "Industry Consultancy Contracts and Work Orders"
        })

    # 5. Faculty Development Programs (FDPs)
    fdp_metrics = calculate_criterion6_fdp_metrics(fdps)
    confirmed_fdp = fdp_metrics.get("confirmed_fdp_count", 0)

    if confirmed_fdp >= 3:
        passed_checks += 1
    elif confirmed_fdp > 0:
        passed_checks += 0.5
        gaps.append({
            "id": "C6-GAP-005",
            "criterion": "Criterion 6",
            "rule": "Faculty Development Participation",
            "severity": "Minor",
            "description": f"Only {confirmed_fdp} confirmed FDP participation records. Target is active participation for all faculty.",
            "evidence_required": "FDP Completion Certificates and Attendance Proofs"
        })
    else:
        gaps.append({
            "id": "C6-GAP-005",
            "criterion": "Criterion 6",
            "rule": "Faculty Development Programs",
            "severity": "Major",
            "description": "No confirmed FDP or STTP participation records provided.",
            "evidence_required": "AICTE/ATAL/NPTEL FDP Certificates"
        })

    completeness_pct = round((passed_checks / total_checks) * 100, 2)
    if completeness_pct >= 85:
        status = "Compliant"
    elif completeness_pct >= 60:
        status = "Partially Compliant"
    else:
        status = "Needs Improvement"

    return {
        "criterion": "Criterion 6",
        "completeness_percentage": completeness_pct,
        "status": status,
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "publication_metrics": pub_metrics,
        "patent_metrics": pat_metrics,
        "project_metrics": proj_metrics,
        "fdp_metrics": fdp_metrics,
        "gaps_count": len(gaps),
        "gaps": gaps
    }
