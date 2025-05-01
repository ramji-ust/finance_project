from django.test import TestCase
from django.contrib.auth.models import User
from banking_webapp.models import BankAccount, UserProfile, Transaction
from decimal import Decimal


class BankAccountModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='testpass')
        self.account = BankAccount.objects.create(
            user=self.user,
            account_number='1234567890',
            balance=Decimal('1000.00')
        )

    def test_account_creation(self):
        self.assertEqual(self.account.user.username, 'alice')
        self.assertEqual(self.account.account_number, '1234567890')
        self.assertEqual(self.account.balance, Decimal('1000.00'))

    def test_str_method(self):
        self.assertEqual(str(self.account), 'alice - 1234567890')


class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bob', password='testpass')
        self.profile = UserProfile.objects.create(
            user=self.user,
            account_number='9876543210'
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'bob')
        self.assertEqual(self.profile.account_number, '9876543210')

    def test_str_method(self):
        self.assertEqual(str(self.profile), 'bob - 9876543210')


class TransactionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='carol', password='testpass')
        self.account = BankAccount.objects.create(
            user=self.user,
            account_number='1111222233',
            balance=Decimal('5000.00')
        )
        self.transaction = Transaction.objects.create(
            account=self.account,
            transaction_type='deposit',
            amount=Decimal('1500.00'),
            description='Salary credit'
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.account, self.account)
        self.assertEqual(self.transaction.transaction_type, 'deposit')
        self.assertEqual(self.transaction.amount, Decimal('1500.00'))
        self.assertEqual(self.transaction.description, 'Salary credit')
        self.assertIsNotNone(self.transaction.timestamp)

    def test_str_method(self):
        self.assertIn('Deposit - ₹1500.00', str(self.transaction))
