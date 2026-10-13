import unittest
from datetime import date
from backend.service import evaluate_supplier, deletion_eligibility


class PolicyTests(unittest.TestCase):
    def test_completed_low_risk_approved(self):
        self.assertTrue(evaluate_supplier({"assessment_status": "completed",
                                            "risks": {"labour": 10}})["approved"])

    def test_pending_assessment_blocked(self):
        self.assertFalse(evaluate_supplier({"assessment_status": "pending",
                                             "risks": {"labour": 0}})["approved"])

    def test_missing_assessment_blocked(self):
        self.assertFalse(evaluate_supplier({"risks": {"labour": 0}})["approved"])

    def test_severe_dimension_not_diluted(self):
        result = evaluate_supplier({"assessment_status": "completed",
                                    "risks": {"labour": 95, "environment": 5,
                                              "safety": 5}})
        self.assertFalse(result["approved"])

    def test_boundary_eighty_blocked(self):
        self.assertFalse(evaluate_supplier({"assessment_status": "completed",
                                             "risks": {"labour": 80}})["approved"])

    def test_unknown_risks_blocked(self):
        self.assertFalse(evaluate_supplier({"assessment_status": "completed"})["approved"])

    def test_invalid_risk_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_supplier({"risks": {"labour": -1}})

    def test_one_year_record_retained(self):
        self.assertFalse(deletion_eligibility({"created_at": "2025-10-13"},
                                               date(2026, 10, 13))["eligible"])

    def test_before_seven_year_anniversary_retained(self):
        self.assertFalse(deletion_eligibility({"created_at": "2019-10-14"},
                                               date(2026, 10, 13))["eligible"])

    def test_seven_year_anniversary_eligible(self):
        self.assertTrue(deletion_eligibility({"created_at": "2019-10-13"},
                                              date(2026, 10, 13))["eligible"])

    def test_legal_hold_retained(self):
        self.assertFalse(deletion_eligibility({"created_at": "2010-01-01",
                                               "legal_hold": True},
                                               date(2026, 10, 13))["eligible"])

    def test_leap_day_anniversary(self):
        record = {"created_at": "2020-02-29"}
        self.assertFalse(deletion_eligibility(record, date(2027, 2, 28))["eligible"])
        self.assertTrue(deletion_eligibility(record, date(2027, 3, 1))["eligible"])
