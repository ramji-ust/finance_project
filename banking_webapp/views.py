from finance_tools.finance_tools import *
from .forms import DepositForm, WithdrawForm
 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BankAccount  # ✅ Make sure you have this model
 
# ----- AUTHENTICATION -----
 
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
 
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')
 
        user = User.objects.create_user(username=username, email=email, password=password)
        BankAccount.objects.create(user=user, account_number=f"AC{user.id}", balance=0)  # Create a blank account
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
 
    return render(request, 'auth/register.html')
 
 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
 
        user = authenticate(request, username=username, password=password)
 
        if user is not None:
            login(request, user)
            return redirect('dashboard_view')
        else:
            messages.error(request, 'Invalid credentials')
 
    return render(request, 'auth/login.html')
 
 
def logout_view(request):
    logout(request)
    return redirect('login')
 
 
# ----- DASHBOARD -----
 
@login_required(login_url='login')
def dashboard_view(request):
    try:
        account = BankAccount.objects.get(user=request.user)
    except BankAccount.DoesNotExist:
        messages.error(request, "Bank account not found.")
        return redirect('logout')
 
    deposit_form = DepositForm()
    withdraw_form = WithdrawForm()
    message = ""
 
    if request.method == "POST":
        if "deposit" in request.POST:
            deposit_form = DepositForm(request.POST)
            if deposit_form.is_valid():
                amount = deposit_form.cleaned_data['amount']
                account.balance += amount
                account.save()
                message = f"₹{amount} deposited successfully."
        elif "withdraw" in request.POST:
            withdraw_form = WithdrawForm(request.POST)
            if withdraw_form.is_valid():
                amount = withdraw_form.cleaned_data['amount']
                if amount <= account.balance:
                    account.balance -= amount
                    account.save()
                    message = f"₹{amount} withdrawn successfully."
                else:
                    message = "Insufficient balance."
 
    context = {
        "account": account,
        "deposit_form": deposit_form,
        "withdraw_form": withdraw_form,
        "message": message,
    }
    return render(request, "banking_webapp/dashboard.html", context)
 
 
# ----- FINANCE TOOLS -----
 
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
 
 
def sip_tool(request):
    result = None
    if request.method == 'POST':
        monthly_investment = float(request.POST.get('monthly_investment', 0))
        annual_rate = float(request.POST.get('annual_rate', 0))
        tenure_years = int(request.POST.get('tenure_years', 0))
        result = calculate_sip(monthly_investment, annual_rate, tenure_years)
    return render(request, 'banking_webapp/sip_calculator.html', {'result': result})
 
 
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
 
 
def home_loan_tool(request):
    result = None
    if request.method == 'POST':
        income = float(request.POST.get('income', 0))
        expenses = float(request.POST.get('expenses', 0))
        loan_term_years = int(request.POST.get('loan_term_years', 20))
        interest_rate = float(request.POST.get('interest_rate', 7)) / 100  
        result = estimate_home_loan_eligibility(income, expenses, loan_term_years, interest_rate)
    return render(request, 'banking_webapp/home_loan.html', {'result': result})
 
 
def credit_card_tool(request):
    result = None
    if request.method == 'POST':
        balance = float(request.POST.get('balance', 0))
        annual_rate = float(request.POST.get('annual_rate', 0)) / 100  
        min_payment_percent = float(request.POST.get('min_payment_percent', 2)) / 100  
        result = calculate_credit_card_balance(balance, annual_rate, min_payment_percent)
    return render(request, 'banking_webapp/credit_card.html', {'result': result})
 
 
def taxable_income_tool(request):
    result = None
    if request.method == 'POST':
        gross_income = float(request.POST.get('gross_income', 0))
        deductions = float(request.POST.get('deductions', 50000))
        result = calculate_taxable_income(gross_income, deductions)
    return render(request, 'banking_webapp/taxable_income.html', {'result': result})
 
 
def budget_planner_tool(request):
    result = None
    if request.method == 'POST':
        income = float(request.POST.get('income', 0))
        expenses = float(request.POST.get('expenses', 0))
        result = plan_budget(income, expenses)
    return render(request, 'banking_webapp/budget_planner.html', {'result': result})
 
 
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