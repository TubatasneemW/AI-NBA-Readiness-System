# student_agent.py

import os
from collections import Counter
from statistics import mean

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
# 3. CALCULATE VERIFIED STUDENT STATISTICS
# ============================================================

def calculate_student_statistics(student_records):
    """
    Calculate exact numerical statistics from the verified
    student records.

    Python performs the calculations.
    The LLM does not calculate these values.
    """

    cie1_values = [
        student["CIE-I"]
        for student in student_records
    ]

    cie2_values = [
        student["CIE-II"]
        for student in student_records
    ]

    micro_project_values = [
        student["Micro Project"]
        for student in student_records
    ]

    internal_total_values = [
        student["Internal Total"]
        for student in student_records
    ]

    attendance_values = [
        student["Attendance"]
        for student in student_records
    ]

    statistics = {
        "record_count": len(student_records),

        "CIE-I": {
            "average": round(mean(cie1_values), 2),
            "minimum": min(cie1_values),
            "maximum": max(cie1_values),
            "range": round(
                max(cie1_values) - min(cie1_values),
                2
            )
        },

        "CIE-II": {
            "average": round(mean(cie2_values), 2),
            "minimum": min(cie2_values),
            "maximum": max(cie2_values),
            "range": round(
                max(cie2_values) - min(cie2_values),
                2
            )
        },

        "Micro Project": {
            "average": round(mean(micro_project_values), 2),
            "minimum": min(micro_project_values),
            "maximum": max(micro_project_values),
            "range": round(
                max(micro_project_values) - min(micro_project_values),
                2
            )
        },

        "Internal Total": {
            "average": round(mean(internal_total_values), 2),
            "minimum": min(internal_total_values),
            "maximum": max(internal_total_values),
            "range": round(
                max(internal_total_values) - min(internal_total_values),
                2
            )
        },

        "Attendance": {
            "average": round(mean(attendance_values), 2),
            "minimum": min(attendance_values),
            "maximum": max(attendance_values),
            "range": round(
                max(attendance_values) - min(attendance_values),
                2
            ),
            "distribution": dict(
                sorted(Counter(attendance_values).items())
            )
        }
    }

    return statistics


# ============================================================
# 4. STUDENT PERFORMANCE ANALYSIS
# ============================================================

def analyze_student_performance(data=None):
    """
    Analyze verified student performance data for NBA
    Criterion 3.

    Python calculates exact numerical statistics.
    Groq is used only to explain and organize the
    verified information.
    """

    # --------------------------------------------------------
    # Load verified student data
    # --------------------------------------------------------

    if data is None:

        student_records = criterion3_data["students"]

        data = {
            "student_records": student_records,
            "course_student_count": (
                criterion3_data["grade_distribution"]["registered"]
            ),
            "available_student_records": len(student_records)
        }

    else:

        student_records = data["student_records"]

    # --------------------------------------------------------
    # Calculate statistics using Python
    # --------------------------------------------------------

    statistics = calculate_student_statistics(
        student_records
    )

    # --------------------------------------------------------
    # Prepare verified summary for the AI
    # --------------------------------------------------------

    verified_summary = {
        "course_registered_students": data[
            "course_student_count"
        ],

        "available_student_records": data[
            "available_student_records"
        ],

        "missing_student_records": (
            data["course_student_count"]
            - data["available_student_records"]
        ),

        "statistics": statistics,

        "available_fields": [
            "Student ID",
            "CIE-I",
            "CIE-II",
            "Micro Project",
            "Internal Total",
            "Attendance"
        ],

        "missing_from_student_input": [
            "Student-level SEE marks",
            "Question-level assessment marks",
            "Official CO attainment formula",
            "CO-PO mapping within this student-performance input"
        ]
    }

    # --------------------------------------------------------
    # Prompt for Student Agent
    # --------------------------------------------------------

    prompt = f"""
You are the Student Performance Analysis Agent
in an NBA Accreditation Readiness System.

Your responsibility is to analyze VERIFIED student
performance information related to NBA Criterion 3.

The information below has already been calculated
and verified by Python from backend data.

The backend data is the source of truth.


==================================================
STRICT DATA INTEGRITY RULES
==================================================

1. Use ONLY the verified information supplied below.

2. DO NOT recalculate any statistics.

3. DO NOT change any numerical value.

4. DO NOT invent:
   - student marks
   - student records
   - student IDs
   - CO attainment
   - PO attainment
   - targets
   - thresholds
   - formulas
   - missing assessment results

5. Do not create values for the missing student records.

6. Do not identify students using names, USNs,
   phone numbers, or other personal information.

7. Use only anonymized student IDs if they are explicitly
   supplied.

8. Do not describe performance as:
   - good
   - bad
   - weak
   - strong
   - low
   - high
   - moderate
   - poor
   - effective
   - ineffective
   - fair
   - unfair

   unless an official benchmark or threshold is supplied.

9. Numerical values must be reported exactly as supplied.

10. Do not infer CO attainment from CIE marks.

11. Do not infer SEE performance because student-level
    SEE marks are not included.

12. Do not infer student ability, learning quality,
    fairness, or assessment effectiveness.

13. Do not claim that Criterion 3 is compliant or
    non-compliant.

14. Do not claim that CO-PO mapping does not exist
    in the overall system.

    Instead, if relevant, say:

    "The required CO-PO mapping is not included in the
    student-performance input supplied to this agent."

15. Similarly, if the CO attainment formula is needed,
    say:

    "The official CO attainment formula is not included
    in the student-performance input supplied to this agent."

16. Clearly distinguish:
    - confirmed facts
    - numerical observations
    - missing information
    - further analysis required


==================================================
VERIFIED STUDENT PERFORMANCE INFORMATION
==================================================

{verified_summary}


==================================================
OUTPUT FORMAT
==================================================

Return EXACTLY these six sections:

1. Student Performance Summary

2. Available Student Data

3. Confirmed Numerical Observations

4. Missing Student Information

5. Areas Requiring Further Analysis

6. Recommendations


==================================================
SECTION 1
==================================================

Student Performance Summary

State:

- registered student count
- available student-record count
- number of records not included in the supplied dataset
- assessment fields available


==================================================
SECTION 2
==================================================

Available Student Data

List the fields available in the student-performance input.


==================================================
SECTION 3
==================================================

Confirmed Numerical Observations

Report the verified statistics exactly.

Include:

- CIE-I average, minimum, maximum and range
- CIE-II average, minimum, maximum and range
- Micro Project average, minimum, maximum and range
- Internal Total average, minimum, maximum and range
- Attendance average, minimum, maximum and range
- Attendance distribution

Do not add interpretations such as good, weak, high,
low or moderate.


==================================================
SECTION 4
==================================================

Missing Student Information

State only information that is not included in the
current student-performance input.

Do not invent missing values.


==================================================
SECTION 5
==================================================

Areas Requiring Further Analysis

Explain what additional verified information would be
needed for deeper analysis.

Do not claim that such information does not exist
elsewhere in the system.


==================================================
SECTION 6
==================================================

Recommendations

Provide recommendations related to:

- data collection
- data validation
- student-performance analysis
- CO attainment analysis
- evidence preparation

Do not invent accreditation requirements.

Do not claim Criterion 3 compliance or non-compliance.


Remember:

Python has already performed the numerical calculations.

Your job is to organize and explain the verified results,
not to perform arithmetic or create accreditation evidence.
"""


    # --------------------------------------------------------
    # Call Groq
    # --------------------------------------------------------

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=prompt,
        max_output_tokens=3000,
        reasoning={
            "effort": "low"
        }
    )

    # --------------------------------------------------------
    # Return final AI analysis
    # --------------------------------------------------------

    return response.output_text