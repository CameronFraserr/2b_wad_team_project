from django.urls import path
from dorm_detective_app import views

app_name = 'dorm_detective'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
]