import math

"""
This module provides financial calculators for various use cases.
- Loan EMI calculation
- SIP, RD, FD maturity estimation
- Retirement savings projection
- Home loan eligibility
- Credit card interest estimation
- Taxable income calculation
- Budget planning
- Net worth evaluation
"""

"""
Function Name : emi_calculator
    emi_calculator(principal, annual_rate, tenure_years):
        Calculates the Equated Monthly Installment (EMI) for a loan.
Formula: EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
Input:
P = Principal loan amount
r = Monthly interest rate (annual_rate / 12 / 100)
n = Loan tenure in months
Returns:
    - float: The monthly EMI rounded to 2 decimal places.
"""
def calculate_emi(principal:float, annual_rate:float, tenure_years:int):
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12

    if monthly_rate == 0:
        emi = principal / tenure_months
    else:
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)

    return round(emi, 2)

"""
Function Name : sip_calculator
    sip_calculator(monthly_investment, annual_rate, tenure_years):
        Calculates the maturity amount for a Systematic Investment Plan (SIP).
Formula: M = P * [(1 + r)^n - 1] / r * (1 + r)
Input:
P = Monthly investment amount
r = Monthly interest rate (annual_rate / 12 / 100)
n = Investment tenure in months
Returns:
    - float: The maturity amount after the tenure, rounded to 2 decimal places.
"""
def calculate_sip(monthly_investment:float, annual_rate:float, tenure_years:int):
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
 
    if monthly_rate == 0:
        maturity_amount = monthly_investment * tenure_months
    else:
        maturity_amount = monthly_investment * (((1 + monthly_rate) ** tenure_months - 1) / monthly_rate) * (1 + monthly_rate)
 
    return round(maturity_amount, 2)

"""
Function Name : fd_calculator
    fd_calculator(principal, annual_rate, tenure_years):
        Calculates the maturity amount for a Fixed Deposit (FD).
Formula: M = P * (1 + r)^n
Input:
P = Principal amount
r = Annual interest rate (annual_rate / 100)
n = Tenure in years
Returns:
    - float: The maturity amount after the tenure, rounded to 2 decimal places.
"""
def calculate_fd(principal:float, annual_rate:float, tenure_years:int):
    maturity_amount = principal * (1 + annual_rate / 100) ** tenure_years
    return round(maturity_amount, 2)

"""
Function Name : rd_calculator
    rd_calculator(monthly_deposit, annual_rate, tenure_years):
        Calculates the maturity amount for a Recurring Deposit (RD).
Formula: M = P * [(1 + r)^n - 1] / (1 - (1 / (1 + r)))
Input:
P = Monthly deposit amount
r = Monthly interest rate (annual_rate / 12 / 100)
n = Tenure in months
Returns:
    - float: The maturity value of the RD, rounded to 2 decimal places.
"""
def calculate_rd(monthly_deposit:float, annual_rate:float, tenure_years:int):
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12

    if monthly_rate == 0:
        maturity_value = monthly_deposit * tenure_months
    else:
        maturity_value = monthly_deposit * ((1 + monthly_rate) ** tenure_months - 1) / (1 - (1 / (1 + monthly_rate)))

    return round(maturity_value, 2)

"""
Function Name : retirement_savings_estimator
    retirement_savings_estimator(monthly_savings, annual_rate, tenure_years):
        Estimates the future corpus for retirement savings.
Formula: F = P * [(1 + r)^n - 1] / r * (1 + r)
Input:
P = Monthly savings amount
r = Monthly interest rate (annual_rate / 12 / 100)
n = Savings tenure in months
This module provides financial calculators for various use cases.
Returns:
    - float: Estimated maturity amount rounded to 2 decimal places.
"""
def estimate_retirement_corpus(monthly_savings:float, annual_rate:float, tenure_years:int):
    if annual_rate == 0:
        return round(monthly_savings * 12 * tenure_years, 2)  # No interest case, simple calculation
 
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
    future_corpus = monthly_savings * (((1 + monthly_rate) ** tenure_months - 1) / monthly_rate) * (1 + monthly_rate)
    return round(future_corpus, 2)

"""
    Function Name : home_loan_eligibility
    Description   : Estimates maximum home loan eligibility based on income and expenses.
    Arguments     : income -> Total monthly income
                    expenses -> Total monthly expenses
                    loan_term_years -> Duration of the loan in years (default is 20 years).
                    interest_rate ->  Annual interest rate of the loan (default is 7%).
    Return value  : A float value representing the maximum loan amount the user is eligible for.
"""
def estimate_home_loan_eligibility(income: float, expenses: float, loan_term_years: int = 20, interest_rate: float = 0.07):
    surplus = income - expenses
    if surplus <= 0:
        return 0
    emi = surplus * 0.5  
    months = loan_term_years * 12
    r = interest_rate / 12
    loan = emi * ((1 + r)**months - 1) / (r * (1 + r)**months)
    return round(loan, 2)
 
"""
    Function name  : credit_card_interest_calculator
    Description    : Calculates final balance if only minimum payment is made each month.
    Arguments      : balance -> The current credit card balance (principal amount).
                     annual_rate -> Annual interest rate on the card (e.g., 0.24 for 24%).
                     min_payment_percent -> Minimum payment as a percentage of the balance each month (default is 5%).
    Return Value   : A float value representing the remaining credit card balance after 12 months if only minimum payments are made.
"""
 
def calculate_credit_card_balance(balance: float, annual_rate: float, min_payment_percent: float = 0.02):
    months = 12
    monthly_rate = annual_rate / 12
 
    for _ in range(months):
        interest = balance * monthly_rate
        min_payment = balance * min_payment_percent
        balance += interest - min_payment * 0.8  # Assume only 80% reduces debt
 
    return round(balance, 2)
 
"""
    Function Name : taxable_income_calculator
    Description   : Calculates taxable income after standard deductions.
    Arguments     : gross_income -> Total annual income before deductions.
                    deductions -> Total applicable deductions (default is 50,000; adjust based on rules).
    Return Value  : A float value representing the taxable income after applying deductions.
"""
def calculate_taxable_income(gross_income: float, deductions: float = 50000):
 
    taxable_income = gross_income - deductions
    return max(taxable_income, 0)
 
"""
    Function Name : simple_budget_planner
    Description   : Suggests saving and investing strategy based on income and expenses.
    Arguments     : income -> Monthly income.
                    expenses -> Monthly expenses.
    Return Value  : A dictionary containing recommended monthly saving and investment values.
"""
def plan_budget(income: float, expenses: float):
 
    surplus = income - expenses
    if surplus <= 0:
        return "No surplus to plan savings. Try reducing expenses."
    savings = surplus * 0.3
    investments = surplus * 0.7
    return {
        "monthly_savings": round(savings, 2),
        "monthly_investments": round(investments, 2)
    }
 
"""
    Function Name : net_worth_calculator
    Description   : Calculates net worth from assets and liabilities.
    Arguments     : assets -> Dictionary of assets with their values.
                    liabilities -> Dictionary of liabilities with their values.
    Return Value  : A float value representing the net worth, calculated as total assets minus total liabilities.
"""
def calculate_net_worth(assets: dict, liabilities: dict):
 
    total_assets = sum(assets.values())
    total_liabilities = sum(liabilities.values())
    return round(total_assets - total_liabilities, 2)

