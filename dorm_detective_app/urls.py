from django.urls import path
from dorm_detective_app import views

app_name = 'dorm_detective_app'

urlpatterns = [
	path('', views.home, name='home'),
	path('universities/', views.universities, name='universities'),
	path('universities/<str:university_name>/', views.university_name, name='university_name'),
	path('univresities/<str:university_name>/<str:accomodation_name>/', views.accommodation_name, name='accommodation_name'),
	path('about_us/', views.about_us, name='about_us'),
	path('FAQ/', views.faq, name='faq'),
	path('contact_us/', views.contact_us, name='contact_us'),
	path('sign_up/', views.sign_up, name='sign_up'),
	path('login/', views.user_login, name='login'),
	path('login/my_account/', views.my_account, name='my_account'),
	path('login/my_account/my_reviews/', views.my_reviews, name='my_reviews'),
	path('logout/', views.user_logout, name='logout'),
	path('restricted/', views.restricted, name='restricted'),
]