from django.urls import path
from dorm_detective_app import views
from registration.backends.default.views import RegistrationView

from dorm_detective_app.views import CustomRegistrationView

app_name = 'dorm_detective'

urlpatterns = [
	path('', views.index, name='index'),
	path('universities/', views.universities, name='universities'),
	path('universities/<str:university_slug>/', views.university_name, name='university_name'),
	path('universities/<str:university_name>/<str:accomodation_name>/', views.accommodation_name, name='accommodation_name'),
	path('about_us/', views.about_us, name='about_us'),
	path('FAQ/', views.faq, name='faq'),
	path('contact_us/', views.contact_us, name='contact_us'),
	path('sign_up/', views.sign_up, name='sign_up'),
	path('login/', views.user_login, name='login'),
	path('login/my_account/', views.my_account, name='my_account'),
	path('login/my_account/my_reviews/', views.my_reviews, name='my_reviews'),
	path('logout/', views.user_logout, name='logout'),
	path('restricted/', views.restricted, name='restricted'),
    path('about/', views.about, name="about"),
    path('accounts/register/', CustomRegistrationView.as_view(), name='django_registration_register'),
    path('universities/university_of_glasgow/', views.glasgow, name="glasgow"),
    path('glasgow/finnieston_avenue/', views.finnieston_avenue, name="finnieston_avenue"),
    # path('universities', views.universities, name="universities"),
    # path('sign_up/', views.sign_up, name='sign_up'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    
]