from django import forms
 
class DepositForm(forms.Form):
    amount = forms.DecimalField(label="Amount to deposit", min_value=1, decimal_places=2)
 
class WithdrawForm(forms.Form):
    amount = forms.DecimalField(label="Amount to withdraw", min_value=1, decimal_places=2)