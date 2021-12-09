from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf.urls import url



from . import views

app_name = ''

urlpatterns = [
    path('', views.home, name='home' ),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('Register/', views.register , name='register'), #TODO Change to new registration page
    path('aboutUs/',views.aboutUs, name='aboutUs'),
    url(r'^registerForm/$', views.registerForm, name='registerForm'),
    path('productList/', views.view_product_list, name="productList"),
    path('<int:product_id>/details', views.product_details, name="productDetails")
]

