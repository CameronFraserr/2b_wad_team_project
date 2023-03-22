from django.shortcuts import render
from dorm_detective_app.forms import *
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from dorm_detective_app.models import *
from datetime import datetime

def index(request):
    universities = University.objects.all()
    universities_supported = universities.count()
    context = {"universities" : universities, "universities_supported" : universities_supported}
    template_name = 'dorm_detective_app/index.html'
    return render(request, template_name, context)


def about_us(request):
    universities = University.objects.all()
    context = {"universities": universities}
    template_name = 'dorm_detective_app/about.html'
    return render(request, template_name, context)


def contact_us(request):
    universities = University.objects.all()
    context = {"universities": universities}
    template_name = 'dorm_detective_app/contact_us.html'
    return render(request, template_name, context)


def faq(request):
    universities = University.objects.all()
    context = {"universities": universities}
    template_name = 'dorm_detective_app/faq.html'
    return render(request, template_name, context)


@login_required
def my_account(request):
    universities = University.objects.all()
    context = {"universities": universities}
    template_name = 'dorm_detective_app/my_account.html'
    return render(request, template_name, context)


@login_required
def my_reviews(request):
    universities = University.objects.all()
    context = {"universities": universities}
    template_name = 'dorm_detective_app/my_reviews.html'
    return render(request, template_name, context)


def universities(request):
    universities = University.objects.all()
    accommodations = Accommodation.objects.all()
    context = {"universities": universities, "accommodations" : accommodations}
    template_name = 'dorm_detective_app/universities.html'
    return render(request, template_name, context)


def university(request, university_slug):
    universities = University.objects.all()

    try:
        university = University.objects.get(slug=university_slug)
        accommodations = Accommodation.objects.filter(university=university)
    except University.DoesNotExist:
        university = None
        accommodations = None

    if university is None:
        return redirect('/dorm_detective/')

    context = {"universities": universities, "university" : university, "accommodations" : accommodations}
    template_name = 'dorm_detective_app/university.html'
    return render(request, template_name, context)


def accommodation(request, university_slug, accommodation_slug):
    universities = University.objects.all()

    try:
        accommodation = Accommodation.objects.get(slug=accommodation_slug)
        university = accommodation.university
        reviews = Review.objects.filter(accommodation=accommodation)
    except Accommodation.DoesNotExist:
        accommodation = None
        university = None
    except Review.DoesNotExist:
        reviews = None

    context = {"universities": universities, "accommodation" : accommodation, "university" : university, "reviews" : reviews}
    template_name = 'dorm_detective_app/accommodation.html'
    return render(request, template_name, context)

# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


# Updated the function definition
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits


def about(request):
    response = render(request, 'dorm_detective_app/about.html')
    return response


def glasgow(request):
    response = render(request, 'dorm_detective_app/glasgow.html')
    return response


def finnieston_avenue(request):
    response = render(request, 'dorm_detective_app/finnieston_avenue.html')
    return response

# def sign_up(request):
#     registered = False

#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save(commit=False)  # don't save the user object yet

#             # Validate the password using Django's built-in password validators
#             try:
#                 validate_password(user.password)
#             except ValidationError as e:
#                 user_form.add_error('password', e)  # Add the password validation error to user_form
#             else:
#                 user.set_password(user.password)
#                 user.save()

#                 profile = profile_form.save(commit=False)
#                 profile.user = user
#                 profile.save()

#                 registered = True

#         else:
#             print(user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()

#     return render(request, 'dorm_detective_app/sign_up.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return redirect(reverse('dorm_detective_app:sign_up'))
#             else:
#                 return HttpResponse("Your Dorm Detective account is disabled.")
#         else:
#             print("Invalid login details: {0}, {1}".format(username, password))
#             return HttpResponse("Invalid login details supplied.")
#     else:
#         return render(request, 'dorm_detective_app/login.html', {})


# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect(reverse('dorm_detective_app:login'))

def add_like(request):
    if request.method == "POST":
        pk=request.POST["pk"]

        try:
            review = Review.objects.get(pk=pk)
            review.likes += 1
            review.save()
        except Review.DoesNotExist:
            pass
    return HttpResponse()