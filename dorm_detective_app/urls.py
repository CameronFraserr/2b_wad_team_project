from django.urls import path, include
from dorm_detective_app import views
from registration.backends.default.views import RegistrationView

#from dorm_detective_app.views import CustomRegistrationView

app_name = 'dorm_detective'

urlpatterns = [
	path('', views.index, name='index'),
	path('universities/', views.universities, name='universities'),
	path('universities/<slug:university_slug>/', views.university, name='university'),
	path('universities/<slug:university_slug>/<slug:accommodation_slug>/', views.accommodation, name='accommodation'),
	path('about/', views.about, name="about"),
	path('FAQ/', views.faq, name='faq'),
	path('contact_us/', views.contact_us, name='contact_us'),
	path('account/<int:user_id>/', views.my_account, name='my_account'),
	path('add-like/', views.add_like, name="add_like"),
    path('logout/', views.custom_logout, name='auth_logout'),
    path('', include('registration.backends.simple.urls')) 
    
]