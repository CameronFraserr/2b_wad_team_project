from django.urls import path
from dorm_detective_app import views
from registration.backends.default.views import RegistrationView

app_name = 'dorm_detective'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('universities/university_of_glasgow/', views.glasgow, name="glasgow"),
    path('glasgow/finnieston_avenue/', views.finnieston_avenue, name="finnieston_avenue"),
    path('universities', views.universities, name="universities")
    # path('sign_up/', views.sign_up, name='sign_up'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('accounts/register/', CustomRegistrationView.as_view(), name='django_registration_register'),
]