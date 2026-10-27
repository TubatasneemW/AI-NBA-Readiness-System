# department_test_fixture.py
"""
EXPLICIT DISCLAIMER:
This dataset is a SYNTHETIC TEST FIXTURE designed strictly for isolated unit
and integration testing of NBA Multi-Agent System (Compliance, Reporting, Inspection).
It does NOT represent real institutional records or production data.
"""

from data.criterion3_data import criterion3_data
from tests.fixtures.criterion4_test_fixture import synthetic_criterion4_fixture
from tests.fixtures.criterion5_test_fixture import synthetic_criterion5_fixture
from tests.fixtures.criterion6_test_fixture import synthetic_criterion6_fixture


synthetic_department_fixture = {
    "department": "Department of Artificial Intelligence & Machine Learning",
    "institution": "Apex Institute of Engineering & Technology",
    "academic_year": "2024-25",
    "criterion3": criterion3_data,
    "criterion4": synthetic_criterion4_fixture,
    "criterion5": synthetic_criterion5_fixture,
    "criterion6": synthetic_criterion6_fixture
}
