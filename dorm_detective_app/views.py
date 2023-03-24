from django.shortcuts import render
from dorm_detective_app.forms import *
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
def my_account(request, user_id):
    user = User.objects.get(id=user_id)
    user_profile = UserProfile.objects.filter(user=user)[0]
    universities = University.objects.all()
    reviews = Review.objects.filter(user=user.userprofile)
    context = {"universities": universities, "reviews": reviews, "user":user, "user_profile" : user_profile}
    template_name = 'dorm_detective_app/my_account.html'
    return render(request, template_name, context)


@login_required
def my_reviews(request):
    universities = University.objects.all()
    context = {"universities": universities}
    template_name = 'dorm_detective_app/my_reviews.html'
    return render(request, template_name, context)

def custom_logout(request):
    logout(request)
    return redirect('index')

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

        avg_rating = 0
        for review in reviews:
            rating = review.rating
            avg_rating += rating

        rating_no = reviews.count()
        avg_rating /= rating_no

    except Accommodation.DoesNotExist:
        accommodation = None
        university = None
        avg_rating = None
        rating_no = None
    except Review.DoesNotExist:
        reviews = None
        avg_rating = None
        rating_no = None

    context = {"universities": universities, "accommodation" : accommodation, "university" : university, "reviews" : reviews, "avg_rating" : avg_rating, "rating_no" : rating_no}
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