from django.shortcuts import render
from django.views.decorators.cache import never_cache

# Create your views here.

@never_cache
def home(request):
    return render(request,'homePage/home.html')

@never_cache
def contactUs(request):
    return render(request, 'homePage/contactUs.html')