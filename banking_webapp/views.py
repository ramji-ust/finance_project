from finance_tools.finance_tools import *
from .forms import DepositForm, WithdrawForm
 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BankAccount, Transaction, UserProfile
 
# ----- AUTHENTICATION -----
 
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        account_number = request.POST['account_number']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return render(request, 'auth/register.html')

        if UserProfile.objects.filter(account_number=account_number).exists():
            messages.error(request, 'Account number already in use')
            return render(request, 'auth/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user, account_number=account_number)

        messages.success(request, 'Registration successful! Please log in.')
        return redirect('login')

    return render(request, 'auth/register.html')
 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        account_number = request.POST['account_number']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.account_number == account_number:
                    login(request, user)
                    return redirect('dashboard_view')
                else:
                    messages.error(request, 'Incorrect account number.')
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile not found.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'auth/login.html')
 
 
def logout_view(request):
    logout(request)
    return redirect('login')
 
 
# ----- DASHBOARD -----
 
@login_required(login_url='login')
def dashboard_view(request):
    # Get or create the user's bank account
    account, created = BankAccount.objects.get_or_create(user=request.user)

    # Initialize messages and forms
    message = ''
    deposit_form = DepositForm()
    withdraw_form = WithdrawForm()

    # Handle POST request for deposit or withdrawal
    if request.method == 'POST':
        if 'deposit' in request.POST:
            deposit_form = DepositForm(request.POST)
            if deposit_form.is_valid():
                amount = deposit_form.cleaned_data['amount']
                account.balance += amount
                account.save()
                Transaction.objects.create(account=account, transaction_type='deposit', amount=amount)
                message = f"₹{amount} deposited successfully!"

        elif 'withdraw' in request.POST:
            withdraw_form = WithdrawForm(request.POST)
            if withdraw_form.is_valid():
                amount = withdraw_form.cleaned_data['amount']
                if account.balance >= amount:
                    account.balance -= amount
                    account.save()
                    Transaction.objects.create(account=account, transaction_type='withdraw', amount=amount)
                    message = f"₹{amount} withdrawn successfully!"
                else:
                    message = "Insufficient balance for withdrawal."

    # Get recent transactions
    transactions = account.transactions.order_by('-timestamp')[:10]

    context = {
        'account': account,
        'deposit_form': deposit_form,
        'withdraw_form': withdraw_form,
        'transactions': transactions,
        'message': message,
    }

    return render(request, 'banking_webapp/dashboard.html', context)
 
 
# ----- FINANCE TOOLS -----

@login_required(login_url='login')
def emi_calculator_view(request):
    emi = None
    error = None
    if request.method == "POST":
        try:
            principal = float(request.POST.get("principal"))
            rate = float(request.POST.get("rate"))
            tenure = int(request.POST.get("tenure"))
            emi = calculate_emi(principal, rate, tenure)
        except Exception as e:
            error = str(e)
    return render(request, "banking_webapp/emi_calculator.html", {"emi": emi, "error": error})
 
@login_required(login_url='login')
def sip_tool(request):
    result = None
    if request.method == 'POST':
        monthly_investment = float(request.POST.get('monthly_investment', 0))
        annual_rate = float(request.POST.get('annual_rate', 0))
        tenure_years = int(request.POST.get('tenure_years', 0))
        result = calculate_sip(monthly_investment, annual_rate, tenure_years)
    return render(request, 'banking_webapp/sip_calculator.html', {'result': result})
 
@login_required(login_url='login')
def fd_calculator_view(request):
    result = None
    error = None
    if request.method == "POST":
        try:
            principal = float(request.POST.get("principal"))
            rate = float(request.POST.get("rate"))
            tenure = int(request.POST.get("tenure"))
            result = calculate_fd(principal, rate, tenure)
        except Exception as e:
            error = str(e)
    return render(request, "banking_webapp/fd_calculator.html", {"result": result, "error": error})
 
@login_required(login_url='login') 
def rd_calculator_view(request):
    result = None
    error = None
    if request.method == "POST":
        try:
            monthly_deposit = float(request.POST.get("monthly_deposit"))
            rate = float(request.POST.get("rate"))
            tenure = int(request.POST.get("tenure"))
            result = calculate_rd(monthly_deposit, rate, tenure)
        except Exception as e:
            error = str(e)
    return render(request, "banking_webapp/rd_calculator.html", {"result": result, "error": error})
 
@login_required(login_url='login') 
def retirement_corpus_view(request):
    result = None
    error = None
    if request.method == "POST":
        try:
            monthly_savings = float(request.POST.get("monthly_savings"))
            rate = float(request.POST.get("rate"))
            tenure = int(request.POST.get("tenure"))
            result = estimate_retirement_corpus(monthly_savings, rate, tenure)
        except Exception as e:
            error = str(e)
    return render(request, "banking_webapp/retirement_corpus_calculator.html", {"result": result, "error": error})
 
@login_required(login_url='login') 
def home_loan_tool(request):
    result = None
    if request.method == 'POST':
        income = float(request.POST.get('income', 0))
        expenses = float(request.POST.get('expenses', 0))
        loan_term_years = int(request.POST.get('loan_term_years', 20))
        interest_rate = float(request.POST.get('interest_rate', 7)) / 100  
        result = estimate_home_loan_eligibility(income, expenses, loan_term_years, interest_rate)
    return render(request, 'banking_webapp/home_loan.html', {'result': result})
 
@login_required(login_url='login')
def credit_card_tool(request):
    result = None
    if request.method == 'POST':
        balance = float(request.POST.get('balance', 0))
        annual_rate = float(request.POST.get('annual_rate', 0)) / 100  
        min_payment_percent = float(request.POST.get('min_payment_percent', 2)) / 100  
        result = calculate_credit_card_balance(balance, annual_rate, min_payment_percent)
    return render(request, 'banking_webapp/credit_card.html', {'result': result})
 
@login_required(login_url='login') 
def taxable_income_tool(request):
    result = None
    if request.method == 'POST':
        gross_income = float(request.POST.get('gross_income', 0))
        deductions = float(request.POST.get('deductions', 50000))
        result = calculate_taxable_income(gross_income, deductions)
    return render(request, 'banking_webapp/taxable_income.html', {'result': result})
 
@login_required(login_url='login') 
def budget_planner_tool(request):
    result = None
    if request.method == 'POST':
        income = float(request.POST.get('income', 0))
        expenses = float(request.POST.get('expenses', 0))
        result = plan_budget(income, expenses)
    return render(request, 'banking_webapp/budget_planner.html', {'result': result})
 
@login_required(login_url='login')
def net_worth_tool(request):
    result = None
    if request.method == 'POST':
        assets = {}
        liabilities = {}
 
        asset_keys = request.POST.getlist('asset_name')
        asset_values = request.POST.getlist('asset_value')
        for name, value in zip(asset_keys, asset_values):
            if name and value:
                assets[name] = float(value)
 
        liability_keys = request.POST.getlist('liability_name')
        liability_values = request.POST.getlist('liability_value')
        for name, value in zip(liability_keys, liability_values):
            if name and value:
                liabilities[name] = float(value)
 
        result = calculate_net_worth(assets, liabilities)
 
    return render(request, 'banking_webapp/net_worth.html', {'result': result})