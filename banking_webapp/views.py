from django.shortcuts import render
from finance_tools.finance_tools import calculate_emi

# Create your views here.

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