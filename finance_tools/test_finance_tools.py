import unittest
from finance_tools import (
    calculate_emi,
    calculate_sip,
    calculate_fd,
    calculate_rd,
    estimate_retirement_corpus,
    estimate_home_loan_eligibility,
    calculate_credit_card_balance,
    calculate_taxable_income,
    plan_budget,
    calculate_net_worth,
)
from math import isclose
 
class TestFinanceTools(unittest.TestCase):
 
    def test_calculate_emi(self):

        self.assertTrue(isclose(calculate_emi(1000000, 7.5, 20), 8055.93, rel_tol=1e-2))

        self.assertEqual(calculate_emi(0, 7.5, 20), 0.0)

        self.assertEqual(calculate_emi(100000, 0, 10), 833.33)
 
    def test_calculate_sip(self):

        self.assertTrue(isclose(calculate_sip(5000, 12, 10), 1165460.98, rel_tol=1e-2))

        self.assertEqual(calculate_sip(0, 12, 10), 0.0)

        self.assertEqual(calculate_sip(5000, 0, 10), 600000.0)
 
    def test_calculate_fd(self):

        self.assertTrue(isclose(calculate_fd(100000, 6.5, 5), 137185.29, rel_tol=1e-2))

        self.assertEqual(calculate_fd(0, 6.5, 5), 0.0)

        self.assertEqual(calculate_fd(100000, 0, 5), 100000.0)
 
    def test_calculate_rd(self):

        self.assertTrue(isclose(calculate_rd(2000, 7, 5), 144438.82, rel_tol=1e-2))

        self.assertEqual(calculate_rd(0, 7, 5), 0.0)

        self.assertEqual(calculate_rd(2000, 0, 5), 120000.0)
 
    def test_estimate_retirement_corpus(self):

        self.assertTrue(isclose(estimate_retirement_corpus(10000, 10, 30), 22604946.14, rel_tol=1e-2))

        self.assertEqual(estimate_retirement_corpus(0, 10, 30), 0.0)

        self.assertEqual(estimate_retirement_corpus(10000, 0, 30), 3600000.0)
 
    def test_estimate_home_loan_eligibility(self):

        self.assertGreater(estimate_home_loan_eligibility(60000, 30000), 0)

        self.assertEqual(estimate_home_loan_eligibility(30000, 30000), 0)

        self.assertEqual(estimate_home_loan_eligibility(20000, 30000), 0)

        low = estimate_home_loan_eligibility(50000, 10000, interest_rate=0.05)

        high = estimate_home_loan_eligibility(50000, 10000, interest_rate=0.1)

        self.assertLess(high, low)
 
    def test_calculate_credit_card_balance(self):

        self.assertGreater(calculate_credit_card_balance(50000, 0.24), 50000)

        self.assertEqual(calculate_credit_card_balance(0, 0.2), 0.0)

        self.assertLess(calculate_credit_card_balance(50000, 0), 50000)

        self.assertLess(calculate_credit_card_balance(50000, 0.2, 0.2), 50000)
 
    def test_calculate_taxable_income(self):

        self.assertEqual(calculate_taxable_income(600000), 550000)

        self.assertEqual(calculate_taxable_income(500000, 0), 500000)

        self.assertEqual(calculate_taxable_income(40000, 50000), 0)
 
    def test_plan_budget(self):

        result = plan_budget(50000, 30000)

        self.assertEqual(result['monthly_savings'], 6000.0)

        self.assertEqual(result['monthly_investments'], 14000.0)
 
        msg = plan_budget(20000, 25000)

        self.assertIsInstance(msg, str)

        self.assertIn("No surplus", msg)
 
        msg = plan_budget(0, 10000)

        self.assertIsInstance(msg, str)

        self.assertIn("No surplus", msg)
 
    def test_calculate_net_worth(self):

        self.assertEqual(calculate_net_worth({'cash': 10000, 'stocks': 50000}, {'loan': 20000}), 40000.0)

        self.assertEqual(calculate_net_worth({}, {}), 0.0)

        self.assertEqual(calculate_net_worth({'bike': 5000}, {'loan': 10000}), -5000.0)
 
if __name__ == '__main__':

    unittest.main()
 