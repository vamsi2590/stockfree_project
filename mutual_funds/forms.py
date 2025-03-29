from django import forms

class FundForm(forms.Form):
    symbol = forms.CharField(label='Mutual Fund Symbol', max_length=10)
# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        # Check if passwords match
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        user = User.objects.create_user(username=username, email=email, password=password)
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
