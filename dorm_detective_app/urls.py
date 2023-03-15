from django.urls import path
from . import views

app_name = 'dorm_detective_app'

urlpatterns = [
    path('register/', views.register, name='register'),
]
