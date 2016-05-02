from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class BootstrapAuthenticationForm(AuthenticationForm):
    """
    Extend :model:`auth.AuthenticationForm` with Bootstrap classes.
    """

    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
