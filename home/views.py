from django.shortcuts import render
from django.views.decorators.cache import never_cache

# Create your views here.

@never_cache
def home(request):
    return render(request,'homePage/home.html')

@never_cache
def contactUs(request):
    return render(request, 'homePage/contactUs.html')

@never_cache
def signIn(request):
    return render(request, 'logInSignUp/LogIn.html')

@never_cache
def signUp(request):
    return render(request, 'logInSignUp/SignUp.html')

@never_cache
def aboutUs(request):
    return render(request, 'homePage/aboutUs.html')