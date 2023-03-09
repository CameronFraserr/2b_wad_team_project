from django.urls import path
from dorm_detective_app import views

app_name = 'dorm_detective_app'

urlpatterns = [
	path('home', views.home, name='home'),
	path('universities/', views.universities, name='universities'),
	path('universities/<slug:university_name_slug>/', views.university, name='university'),
	path('univresities/<slug:university_name_slug>/<slug:accomodation_name_slug>/', views.accommodation, name='accommodation'),
	path('about_us/', views.about_us, name='about_us'),
	path('faq/', views.faq, name='faq'),
	path('contact_us/', views.contact_us, name='contact_us'),
	path('sign_up/', views.register, name='sign_up'),
	path('login/', views.user_login, name='login'),
	path('login/my_account', views.my_account, name='my_account'),
	path('login/my_account/my_reviews', views.my_reviews, name='my_reviews'),
	path('logout/', views.user_logout, name='logout'),
	path('restricted/', views.restricted, name='restricted'),
]