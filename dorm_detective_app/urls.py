from django.urls import path
from . import views

app_name = 'dorm_detective_app'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
]
