from django.urls import path
from dorm_detective_app import views

app_name = 'dorm_detective'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('universities/university_of_glasgow/', views.glasgow, name="glasgow"),
    path('glasgow/finnieston_avenue/', views.finnieston_avenue, name="finnieston_avenue"),
    path('universities', views.universities, name="universities")
]