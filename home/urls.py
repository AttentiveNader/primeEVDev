from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = ''

urlpatterns = [
    path('', views.home, name='home' ),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('Register/', views.register , name='register'), #TODO Change to new registration page
    path('aboutUs/',views.aboutUs, name='aboutUs'),
    url(r'^registerForm/$', views.registerForm, name='registerForm'),
]

