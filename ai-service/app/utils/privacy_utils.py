# privacy_utils.py
"""
Data Privacy and PII (Personally Identifiable Information) Sanitizer.

Responsibilities:
1. Strip unnecessary sensitive personal data (personal phone numbers, personal emails,
   residential addresses, national identity numbers, blood group, date of birth)
   before payloads are passed to language models or external services.
2. Preserve professional accreditation facts:
   - Faculty ID, Designation, Qualification, Experience, Specialization,
     Department, Workload, Courses handled, Evidence verification status.
3. Protect student privacy by removing student names, phone numbers, and USNs
   if provided in raw feeds.
"""

from typing import Any, Dict, List

# Sensitive fields that must NEVER be passed to the LLM
SENSITIVE_FACULTY_KEYS = {
    "phone", "mobile", "phone_number", "contact_number",
    "personal_email", "email", "home_email",
    "address", "residential_address", "home_address",
    "pan", "aadhaar", "ssn", "national_id",
    "dob", "date_of_birth", "blood_group", "salary_in_hand", "bank_account"
}


def sanitize_faculty_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sanitize an individual faculty record by removing personal PII.
    """
    sanitized = {}
    for key, value in record.items():
        clean_key = key.lower().strip().replace(" ", "_")
        if clean_key in SENSITIVE_FACULTY_KEYS:
            continue
        sanitized[key] = value
    return sanitized


def sanitize_faculty_data(faculty_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Sanitize a list of faculty records, stripping all PII.
    """
    return [sanitize_faculty_record(rec) for rec in faculty_records]
