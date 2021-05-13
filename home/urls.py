from django.urls import path


from . import views

app_name = ''

urlpatterns = [
    path('',views.home,name='home' ),
    path('contactUs/',views.contactUs,name='contactUs')
]