from django.contrib.auth.models import User
from .models import UserProfile, Review
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
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['accommodation', 'title', 'description', 'picture', 'rating']
        widgets = {
            'accommodation': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control', 'rows': 5}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)], attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Title',
            'description': 'Description',
            'picture': 'Picture (optional)',
            'rating': 'Rating (1-5)',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['accommodation'].required = False
        self.fields['picture'].required = False

class CustomRegistrationForm(RegistrationForm):
    current_student = forms.BooleanField(
        required=False,
        initial=False,
        label="I am a student",
    )

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserProfile.objects.create(user=user, current_student=self.cleaned_data['current_student'])
        return user