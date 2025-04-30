import math

def calculate_emi(principal: float, annual_rate: float, tenure_years: int) -> float:
    """
    Calculates the Equated Monthly Installment (EMI) for a loan.

    Args:
        principal (float): The loan amount.
        annual_rate (float): The annual interest rate in percentage.
        tenure_years (int): Loan tenure in years.

    Returns:
        float: The monthly EMI amount.
    """
    if principal <= 0 or annual_rate < 0 or tenure_years <= 0: 
        raise ValueError("Inputs must be positive values.")

    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months)) / \
          (math.pow(1 + monthly_rate, tenure_months) - 1)
    return round(emi, 2)
