from django.shortcuts import render
from .forms import UserForm, UserProfileForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from registration.backends.default.views import RegistrationView
from .forms import CustomRegistrationForm

class CustomRegistrationView(RegistrationView):
    def get_form_class(self):
        return CustomRegistrationForm

# Create your views here.

def sign_up(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)  # don't save the user object yet

            # Validate the password using Django's built-in password validators
            try:
                validate_password(user.password)
            except ValidationError as e:
                user_form.add_error('password', e)  # Add the password validation error to user_form
            else:
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'dorm_detective_app/sign_up.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('dorm_detective_app:sign_up'))
            else:
                return HttpResponse("Your Dorm Detective account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'dorm_detective_app/login.html', {})
    
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('dorm_detective_app:login'))