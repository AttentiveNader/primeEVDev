from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache
from .forms import UserRegistrationForm

# Create your views here.

@never_cache
def login(request):
    if request.method == 'POST':
        """
            TODO
            1. Extract all the data from request
            2. Query DB for authentication
            3. Login using this user
            4. Redirect to login with error message OR Redirect to home accordingly
        """
    return render(request, 'registration/LogIn.html')

@never_cache
def home(request):
    return render(request,'homePage/home.html')

@never_cache
def contactUs(request):
    return render(request, 'homePage/contactUs.html')

@never_cache
def signUp(request):
    return render(request, 'registration/SignUp.html')

@never_cache
def aboutUs(request):
    return render(request, 'homePage/aboutUs.html')

@never_cache
def info(request):
    return render(request, 'homePage/info.html')

@never_cache
def signUp(request):
    if request.method == 'POST':
        """
            TODO
            1. Extract all the data from request
            2. Query DB for authentication
            3. Create User
            4. Save User
            5. Login using this user
        """
        return redirect('home')
    return render(request, 'registration/SignUp.html', {'form': form})

