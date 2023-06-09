from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "username", "email",)
