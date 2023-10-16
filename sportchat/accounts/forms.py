from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    contact_number = forms.CharField(max_length=15, required=True, label="Contact Number")

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'email', 'contact_number', 'password1', 'password2']
