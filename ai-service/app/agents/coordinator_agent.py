# coordinator_agent.py

import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from data.criterion3_data import criterion3_data


# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# 2. CREATE GROQ CLIENT
# ============================================================

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# ============================================================
# 3. GET COMPACT VERIFIED FACTS
# ============================================================

def get_verified_facts(data=None):
    """
    Return only the important verified Criterion 3 facts.

    If external data is supplied, use that data.

    If no data is supplied, use the local
    criterion3_data.py dataset.

    Python is the source of truth for:
    - course information
    - assessment scheme
    - COs
    - assessment-to-CO mapping
    - CO-PO-PSO mapping
    - grade distribution
    - student record count
    - data availability
    """

    # --------------------------------------------------------
    # Use local verified data if no external data is supplied
    # --------------------------------------------------------

    if data is None:
        data = criterion3_data

    # --------------------------------------------------------
    # Return compact verified facts
    # --------------------------------------------------------

    return {
        "course": data["course"],

        "course_outcomes": data["course_outcomes"],

        "assessment_scheme": data["assessment_scheme"],

        "micro_project": data["micro_project"],

        "assessment_co_mapping": data[
            "assessment_co_mapping"
        ],

        "co_po_pso_mapping": data[
            "co_po_pso_mapping"
        ],

        "grade_distribution": data[
            "grade_distribution"
        ],

        "student_record_count": len(
            data["students"]
        ),

        "data_quality": data[
            "data_quality"
        ]
    }


# ============================================================
# 4. COMPACT AGENT OUTPUT
# ============================================================

def compact_agent_output(text, max_chars=1800):
    """
    Keep agent output small enough to stay within the
    Groq TPM limit.

    The verified Python data remains the source of truth,
    so the full agent output does not need to be sent.
    """

    if not text:
        return ""

    text = str(text)

    if len(text) <= max_chars:
        return text

    return text[:max_chars] + "\n[Agent output truncated]"


# ============================================================
# 5. COORDINATOR FUNCTION
# ============================================================

def coordinate_criterion3(
    assessment_analysis,
    student_analysis,
    data=None
):
    """
    Combine the Assessment Agent and Student Agent outputs.

    The Coordinator is an organizing agent.

    Python-verified data is the factual source of truth.

    If external Criterion 3 data is supplied, it is used.

    If no external data is supplied, the local
    criterion3_data.py dataset is used.

    The LLM must not invent:
    - numbers
    - mappings
    - formulas
    - thresholds
    - attainment values
    - missing evidence
    - recommendations
    """

    # --------------------------------------------------------
    # Get verified facts
    # --------------------------------------------------------

    verified_facts = get_verified_facts(data)

    verified_facts_json = json.dumps(
        verified_facts,
        indent=2,
        default=str
    )

    # --------------------------------------------------------
    # Compact agent outputs
    # --------------------------------------------------------

    assessment_text = compact_agent_output(
        assessment_analysis,
        max_chars=1800
    )

    student_text = compact_agent_output(
        student_analysis,
        max_chars=1800
    )

    # ========================================================
    # 6. COORDINATOR PROMPT
    # ========================================================

    prompt = f"""
You are the Coordinator Agent for an
AI-Driven NBA Accreditation Readiness System.

Produce a factual Criterion 3 report.

Python-verified data is the SOURCE OF TRUTH.

The Assessment Agent and Student Agent outputs are
supporting summaries only.


================ VERIFIED DATA ================

{verified_facts_json}


================ ASSESSMENT AGENT ================

{assessment_text}


================ STUDENT AGENT ================

{student_text}


================ RULES ================

1. Use the Python-verified data for all factual values.

2. Never change a verified number.

3. Never calculate a new number.

4. Never invent CO attainment.

5. Never invent PO attainment.

6. Never invent formulas.

7. Never invent thresholds.

8. Never invent targets.

9. Never invent assessment mappings.

10. Never invent student information.

11. Never expose student names, USNs, or phone numbers.

12. Do not infer relationships between attendance,
    marks, grades, COs, or POs.

13. Do not make compliance judgments.

14. Do not use unsupported words such as:
    good, bad, strong, weak, poor, effective, ineffective,
    satisfactory, unsatisfactory.

15. CO-PO-PSO mapping IS AVAILABLE in the verified data.

16. Do not say that CO-PO-PSO mapping is missing.

17. The verified assessment-to-CO mapping is:

    CIE-I -> CO1, CO2
    CIE-II -> CO3, CO4
    Micro Project -> CO1, CO2, CO3, CO4
    SEE -> CO1, CO2, CO3, CO4

18. Do not say that every assessment component covers
    every CO.

19. The verified student-performance record count is 56.

20. The course-level registered student count is 60.

21. Do not infer the identities of the 4 records that are
    not present.

22. Student-level SEE marks are unavailable.

23. Question-level student marks are unavailable.

24. Official CO attainment formula is unavailable.

25. Official PO attainment formula is unavailable.

26. A data limitation is not automatically a recommendation.

27. Do not invent recommendations.

28. Do not invent additional analysis.

29. If no explicit further analysis is supported, write:

    No additional analysis was explicitly identified.

30. If no explicit next step is supported, write:

    No additional next steps were explicitly identified.


================ OUTPUT ================

Return exactly these seven sections:


1. Criterion 3 Summary

Briefly summarize:
- course
- assessment scheme
- assessment-to-CO coverage
- student record availability
- explicit data limitations


2. Assessment Findings

Include:
- course information
- assessment scheme
- COs
- assessment-to-CO mapping
- Micro Project rubric
- CO-PO-PSO mapping
- grade distribution
- relevant data availability


3. Student Performance Findings

Include the verified student statistics supplied by the
Student Agent.

Do not recalculate or interpret them.


4. Combined Observations

Only combine facts explicitly supported by the verified
data and agent outputs.

Do not create new conclusions.


5. Missing Evidence

List only explicitly unavailable information:

- student-level SEE marks
- question-level student marks
- official CO attainment formula
- official PO attainment formula

Do NOT list the 56-versus-60 difference as missing evidence.


6. Further Analysis Required

Only include explicitly supported analysis needs.

Otherwise write:

No additional analysis was explicitly identified.


7. Recommended Next Steps

Only include explicitly stated recommendations from the
agents.

Do not create recommendations from data limitations.

Otherwise write:

No additional next steps were explicitly identified.
"""


    # ========================================================
    # 7. CALL GROQ
    # ========================================================

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=prompt,
        max_output_tokens=1400,
        reasoning={
            "effort": "low"
        }
    )


    # ========================================================
    # 8. RETURN FINAL RESULT
    # ========================================================

    return response.output_text