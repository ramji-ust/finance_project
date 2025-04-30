from django import forms
 
class DepositForm(forms.Form):
    amount = forms.DecimalField(label="Amount to deposit", min_value=1, decimal_places=2)
 
class WithdrawForm(forms.Form):
    amount = forms.DecimalField(label="Amount to withdraw", min_value=1, decimal_places=2)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)