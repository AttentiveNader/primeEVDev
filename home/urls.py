from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLogInForm


from . import views

app_name = ''

urlpatterns = [
    path('', views.home, name='home' ),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('Sign-Up/', views.signUp , name='signUp'),
    path('Sign-In/', auth_views.LoginView.as_view(authentication_form=UserLogInForm), name='signIn'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homePage/home.html'), name="logout")
]

#path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),