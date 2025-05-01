from django.urls import reverse
from django.test import SimpleTestCase
 
class TestUrls(SimpleTestCase):
 
    def test_register_url_resolves(self):
        url = reverse('register_view')
        self.assertEqual(url, '/')
 
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')
 
    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(url, '/logout/')
 
    def test_dashboard_url_resolves(self):
        url = reverse('dashboard_view')
        self.assertEqual(url, '/dashboard/')
 
    def test_emi_calculator_url_resolves(self):
        url = reverse('emi_calculator_view')
        self.assertEqual(url, '/tools/emi/')
 
    def test_sip_tool_url_resolves(self):
        url = reverse('sip_tool')
        self.assertEqual(url, '/tools/sip/')
 
    def test_fd_calculator_url_resolves(self):
        url = reverse('fd_calculator_view')
        self.assertEqual(url, '/tools/fd/')
 
    def test_rd_calculator_url_resolves(self):
        url = reverse('rd_calculator_view')
        self.assertEqual(url, '/tools/rd/')
 
    def test_retirement_corpus_url_resolves(self):
        url = reverse('retirement_corpus_view')
        self.assertEqual(url, '/tools/retirement/')
 
    def test_home_loan_tool_url_resolves(self):
        url = reverse('home_loan_tool')
        self.assertEqual(url, '/tools/home-loan/')
 
    def test_credit_card_tool_url_resolves(self):
        url = reverse('credit_card_tool')
        self.assertEqual(url, '/tools/credit-card/')
 
    def test_taxable_income_tool_url_resolves(self):
        url = reverse('taxable_income_tool')
        self.assertEqual(url, '/tools/taxable-income/')
 
    def test_budget_planner_tool_url_resolves(self):
        url = reverse('budget_planner_tool')
        self.assertEqual(url, '/tools/budget-planner/')
 
    def test_net_worth_tool_url_resolves(self):
        url = reverse('net_worth_tool')
        self.assertEqual(url, '/tools/net-worth/')
 
    def test_loan_prediction_url_resolves(self):
        url = reverse('predict_loan')
        self.assertEqual(url, '/predict-loan/')