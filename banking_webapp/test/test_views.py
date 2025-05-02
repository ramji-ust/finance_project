from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from banking_webapp.models import BankAccount, Transaction
import numpy as np
import joblib
from unittest.mock import patch

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.account = BankAccount.objects.create(user=self.user, account_number='1234567890', balance=1000)

    def test_register_view_get(self):
        response = self.client.get(reverse('register_view'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_post(self):
        response = self.client.post(reverse('register_view'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_post(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to dashboard

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('dashboard_view'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_post_deposit(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('dashboard_view'), {
            'deposit': '1',
            'amount': 500
        })
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_post_withdraw(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('dashboard_view'), {
            'withdraw': '1',
            'amount': 500
        })
        self.assertEqual(response.status_code, 200)

    def test_emi_calculator_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('emi_calculator_view'), {
            'principal': 100000,
            'rate': 10,
            'tenure': 12
        })
        self.assertEqual(response.status_code, 200)

    def test_sip_tool_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('sip_tool'), {
            'monthly_investment': 2000,
            'annual_rate': 12,
            'tenure_years': 10
        })
        self.assertEqual(response.status_code, 200)

    def test_fd_calculator_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('fd_calculator_view'), {
            'principal': 100000,
            'rate': 6,
            'tenure': 5
        })
        self.assertEqual(response.status_code, 200)

    def test_rd_calculator_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('rd_calculator_view'), {
            'monthly_deposit': 2000,
            'rate': 7,
            'tenure': 5
        })
        self.assertEqual(response.status_code, 200)

    def test_retirement_corpus_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('retirement_corpus_view'), {
            'monthly_savings': 5000,
            'rate': 8,
            'tenure': 30
        })
        self.assertEqual(response.status_code, 200)

    def test_home_loan_tool(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('home_loan_tool'), {
            'income': 50000,
            'expenses': 20000,
            'loan_term_years': 20,
            'interest_rate': 7
        })
        self.assertEqual(response.status_code, 200)

    def test_credit_card_tool(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('credit_card_tool'), {
            'balance': 10000,
            'annual_rate': 18,
            'min_payment_percent': 2
        })
        self.assertEqual(response.status_code, 200)

    def test_taxable_income_tool(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('taxable_income_tool'), {
            'gross_income': 600000,
            'deductions': 100000
        })
        self.assertEqual(response.status_code, 200)

    def test_budget_planner_tool(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('budget_planner_tool'), {
            'income': 50000,
            'expenses': 30000
        })
        self.assertEqual(response.status_code, 200)

    def test_net_worth_tool(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('net_worth_tool'), {
            'asset_name': ['Car', 'House'],
            'asset_value': ['100000', '500000'],
            'liability_name': ['Loan'],
            'liability_value': ['200000']
        })
        self.assertEqual(response.status_code, 200)

    @patch("banking_webapp.views.model.predict")
    def test_loan_prediction_view(self, mock_predict):
        mock_predict.return_value = [500000]
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('predict_loan'), {
            'age': 30,
            'monthly_income': 50000,
            'credit_score': 750,
            'loan_tenure': 10,
            'existing_loan': 0,
            'dependents': 2
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("₹", response.content.decode())

