from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request, 'dorm_detective_app/index.html')
    return response

def about(request):
    response = render(request, 'dorm_detective_app/about.html')
    return response