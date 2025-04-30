from django.urls import path
from . import views

urlpatterns = [
    path("tools/emi/", views.emi_calculator_view, name="emi_calculator"),
]
