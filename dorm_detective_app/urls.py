from django.urls import path
from . import views

app_name = 'dorm_detective_app'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
