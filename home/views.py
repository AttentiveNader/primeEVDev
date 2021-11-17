from django.shortcuts import render, redirect

from django.contrib import messages
from django.views.decorators.cache import never_cache
from .forms import UserRegistrationForm

# Create your views here.

@never_cache
def home(request):
    return render(request,'homePage/home.html')

@never_cache
def contactUs(request):
    return render(request, 'homePage/contactUs.html')

@never_cache
def aboutUs(request):
    return render(request, 'homePage/aboutUs.html')
@never_cache
def info(request):
    return render(request, 'homePage/info.html')

@never_cache
def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/SignUp.html', {'form': form})

