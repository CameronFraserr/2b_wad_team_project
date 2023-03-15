from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from registration.forms import RegistrationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('current_student',)

class CustomRegistrationForm(RegistrationForm):
    is_student = forms.BooleanField(
        required=False,
        initial=False,
        label="I am a student",
    )
