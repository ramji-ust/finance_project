from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path("tools/emi/", views.emi_calculator_view, name="emi_calculator_view"),
    path("tools/sip/", views.sip_tool, name="sip_tool"),
    path('tools/fd/', views.fd_calculator_view, name='fd_calculator_view'),
    path('tools/rd/', views.rd_calculator_view, name='rd_calculator_view'),
    path('tools/retirement/', views.retirement_corpus_view, name='retirement_corpus_view'),
    path('tools/home-loan/', views.home_loan_tool, name='home_loan_tool'),
    path('tools/credit-card/', views.credit_card_tool, name='credit_card_tool'),
    path('tools/taxable-income/', views.taxable_income_tool, name='taxable_income_tool'),
    path('tools/budget-planner/', views.budget_planner_tool, name='budget_planner_tool'),
    path('tools/net-worth/', views.net_worth_tool, name='net_worth_tool'),
    path('predict-loan/', views.loan_prediction_view, name='predict_loan'),
]
