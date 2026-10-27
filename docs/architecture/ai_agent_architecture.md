# AI-Driven NBA Accreditation Readiness System
## Multi-Agent Architecture & Design Specification

---

### 1. Conceptual Overview (For Viva & Technical Presentation)

The system functions as a **Decision-Support Digital Twin** for engineering departments preparing for National Board of Accreditation (NBA) evaluations.

#### Core Architectural Philosophy:
1. **Deterministic Calculations in Python**: Mathematical and statistical computations (such as averages, grade distributions, Student-Faculty Ratios, and progression rates) are **strictly calculated in Python**. A Generative Large Language Model (LLM) is **never** permitted to calculate numbers or perform arithmetic.
2. **Factually Bounded LLM Reasoning**: The LLM (via Groq `openai/gpt-oss-20b`) is used strictly to organize, explain, contextualize, and format verified findings into auditable sections.
3. **Decoupled Specialized Agents**: Individual criteria (3, 4, 5, 6) are handled by dedicated agents. A centralized **Coordinator Agent** manages routing and synthesizes multi-agent outputs, preventing unneeded cross-agent communication.
4. **Data Integrity & Traceability**: The system never hallucinates attainment scores, compliance verdicts, or missing documents. It explicitly tags what is verified, what is incomplete, and what requires human review.

---

### 2. Multi-Agent Logical Flow

```
                      Verified Academic / Faculty Data
                                     │
                                     ▼
                      Data Validation Layer (Pydantic)
                                     │
                                     ▼
                     Central Coordinator Router
                                     │
         ┌──────────────────┬────────┴─────────┬──────────────────┐
         ▼                  ▼                  ▼                  ▼
   Criterion 3        Criterion 4        Criterion 5        Criterion 6
Assessment Agent    Student Agent      Faculty Agent      Faculty Agent
 (COs, Scheme,      (Progression,      (Roster, SFR,      (Research,
 Grade Dist.)       Placements)        Cadre, Workload)   Patents, FDP)
         │                  │                  │                  │
         └──────────────────┼──────────────────┴──────────────────┘
                            ▼
                     Coordinator Agent
              (Merges facts, prevents duplicate claims)
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
  Compliance Agent     Report Agent     Inspection Agent
 (Gap check against   (Structured GFM   (Virtual Inspection
 approved rules)       Documentation)    Digital Twin)
         │                  │                  │
         └──────────────────┼──────────────────┘
                            ▼
                    FastAPI REST API
                            │
                    Backend Database
```

---

### 3. Agent Responsibility Matrix

| Agent | Criteria | Responsibility | Allowed Data | Calculations Performed |
| :--- | :--- | :--- | :--- | :--- |
| **Assessment Agent** | 3 | Course outcomes (COs), assessment scheme, assessment-to-CO mappings, rubrics, grade distribution, limitation flags. | Course metadata, syllabi, rubrics, grade distributions. No student PII. | None. Summarizes verified assessment structures. |
| **Student Agent** | 3 & 4 | Student academic performance, CIE scores, progression, placements, higher education. | Anonymized records (`S001`, `S002`). No names/USNs/phones. | Averages, ranges, min/max, attendance distributions, placement rates. |
| **Faculty Agent** | 5 & 6 | Faculty qualifications, cadre ratio, designations, SFR, courses handled, publications, patents, consultancy. | Faculty profile metadata, verified research citations. | Student-to-Faculty Ratio (SFR), Cadre ratios, publication metrics. |
| **Coordinator Agent** | 3, 4, 5, 6 | Synthesizes multi-agent outputs into consolidated findings, resolves duplicates, enforces factual consistency. | Verified facts JSON + agent summary texts. | None. Enforces ground truth and formatting. |
| **Compliance Agent** | 3, 4, 5, 6 | Compares institutional evidence against approved NBA criteria rubrics to pinpoint missing evidence or unverified items. | Approved checklist rules + aggregated agent findings. | Completeness percentage, gap counts. |
| **Report Agent** | 3, 4, 5, 6 | Formats inspection-ready reports with tables, verified metrics, and explicit limitation sections. | Consolidated outputs from Coordinator & Compliance. | None. Document assembly. |
| **Inspection Agent** | Digital Twin | Provides virtual inspection cockpit for visiting evaluators to audit verification statuses and browse evidence links. | Full department audit record and evidence metadata. | Evidence verification ratios. |

---

### 4. Shared Services

- **`model_client.py`**: Centralized Groq / OpenAI-compatible interface with secret protection, timeout handling, and offline deterministic mock support for fast testing.
- **`metrics_service.py`**: Deterministic statistical engine ensuring zero mathematical hallucinations.

---

### 5. Criterion 4 (Students' Performance) Specification

- **Input Contract**:
  - `cohorts`: list of batch dictionaries (`batch`, `admitted_count`, `completed_without_backlog`, `completed_with_backlog`).
  - `placements`: list of year dictionaries (`academic_year`, `final_year_students`, `placed_count`, `higher_studies_count`, `entrepreneurship_count`, `median_salary_lpa`).
  - `achievements`: list of achievement items (`achievement_id`, `category`, `verified`, `evidence_document`).
- **Deterministic Metrics Computed in Python**:
  - Cohort completion rate without backlog: `(completed_without_backlog / admitted) * 100`
  - Overall completion rate: `((completed_without_backlog + completed_with_backlog) / admitted) * 100`
  - Placement rate: `(placed / final_year_students) * 100`
  - Total progression rate: `((placed + higher_studies + entrepreneurship) / final_year_students) * 100`
- **Prompt Guardrails**: Strictly forbids fabricating graduation numbers, placement companies, student names/USNs, or assigning subjective ratings like "good" or "poor".

---

### 6. Criterion 5 (Faculty Information) Specification

- **Input Contract**:
  - `department`: name of the academic department.
  - `total_enrolled_students`: student strength across eligible undergraduate/postgraduate years.
  - `faculty_members`: list of faculty profiles (`faculty_id`, `name`, `designation`, `qualification`, `specialization`, `total_experience_years`, `institution_experience_years`, `verified`, `evidence_document`).
- **Privacy & PII Protection**:
  - Automatically filtered by `privacy_utils.py` to scrub personal phone numbers, personal email addresses, national IDs, and residential addresses prior to model prompt construction.
- **Deterministic Metrics Computed in Python**:
  - Student-to-Faculty Ratio (SFR): `round(total_enrolled_students / regular_faculty_count, 2)`
  - Cadre Ratio: Professors : Associate Professors : Assistant Professors
  - Qualification percentage: Ph.D. faculty percentage = `(phd_count / total_faculty) * 100`
  - Experience stats: Mean total experience, institution experience, min, max.
  - Verification audit: Verified records vs records pending HR documentation.
- **Prompt Guardrails**: Forbids inventing faculty degrees, inflating experience, or declaring compliance without official accreditation criteria.

---

### 7. Criterion 6 (Faculty Contributions) Specification

- **Input Contract**:
  - `publications`: list of papers (`publication_id`, `title`, `indexing` [SCI/SCIE/Scopus/UGC-CARE/Conferences], `doi`, `verified`, `evidence_document`).
  - `patents`: list of patents (`patent_id`, `title`, `status` [Granted/Published/Filed], `application_number`, `verified`, `evidence_document`).
  - `sponsored_projects`: list of research grants (`project_id`, `title`, `funding_agency`, `funding_amount_lakhs`, `verified`, `evidence_document`).
  - `consultancy`: list of industrial consultancies (`consultancy_id`, `title`, `client_organization`, `revenue_amount_lakhs`, `verified`, `evidence_document`).
  - `fdps`: list of programs (`fdp_id`, `title`, `role` [Attended/Organized], `duration_days`, `verified`, `evidence_document`).
- **Deterministic Metrics Computed in Python**:
  - Publication counts by indexing; SCI/Scopus totals; confirmed vs pending.
  - Patent counts by status (Granted, Published, Filed).
  - Sponsored project grant sum in INR Lakhs.
  - Consultancy revenue sum in INR Lakhs.
  - Aggregate research funding sum in INR Lakhs.
  - FDP counts (Attended vs Organized).
- **Core Verification Guardrail**:
  - Only confirmed records with supporting documentary proof are counted toward confirmed totals. Unverified submissions are quarantined in pending tallies to prevent audit penalties.



