from django.test import TestCase
from banking_webapp.forms import DepositForm, WithdrawForm, LoginForm
from decimal import Decimal
 
class FormTests(TestCase):
 
    # Test DepositForm
    def test_deposit_form_valid(self):
        form_data = {'amount': Decimal('100.00')}
        form = DepositForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_deposit_form_invalid_negative_amount(self):
        form_data = {'amount': Decimal('-50.00')}
        form = DepositForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['amount'], ['Ensure this value is greater than or equal to 1.'])
 
    def test_deposit_form_invalid_zero_amount(self):
        form_data = {'amount': Decimal('0.00')}
        form = DepositForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['amount'], ['Ensure this value is greater than or equal to 1.'])
 
    # Test WithdrawForm
    def test_withdraw_form_valid(self):
        form_data = {'amount': Decimal('50.00')}
        form = WithdrawForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_withdraw_form_invalid_negative_amount(self):
        form_data = {'amount': Decimal('-50.00')}
        form = WithdrawForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['amount'], ['Ensure this value is greater than or equal to 1.'])
 
    def test_withdraw_form_invalid_zero_amount(self):
        form_data = {'amount': Decimal('0.00')}
        form = WithdrawForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['amount'], ['Ensure this value is greater than or equal to 1.'])
 
    # Test LoginForm
    def test_login_form_valid(self):
        form_data = {'username': 'testuser', 'password': 'password123'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_login_form_invalid_missing_username(self):
        form_data = {'username': '', 'password': 'password123'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])
 
    def test_login_form_invalid_missing_password(self):
        form_data = {'username': 'testuser', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])
 
    def test_login_form_invalid_missing_both_fields(self):
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password'], ['This field is required.'])