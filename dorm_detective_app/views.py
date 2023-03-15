from django.shortcuts import render
from .forms import UserForm, UserProfileForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

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
