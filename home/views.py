from django.db.models.fields import EmailField
from django.shortcuts import render, redirect

from django.contrib import messages
from django.views.decorators.cache import never_cache

from .models import Member, Product
from django.core.files.storage import FileSystemStorage
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
def register(request):
    return render(request, 'homePage/info.html')

@never_cache
def registerForm(request):
    template = 'homePage/info.html'

    form = request.POST
    if Member.objects.filter(email=request.POST.get('email')).exists():
        return render(request, template, {'form': form, 'errorMsg': 'Email already exists'})

    else:
        if request.method == "POST" and request.FILES['img']:
            gender = False
            upload = request.FILES.get('img')
            if request.POST.get('gender') == "true":
                    gender = True

            member = Member(
                first_name = request.POST.get("fname"),
                last_name = request.POST.get("lname"),
                email = request.POST.get('email'),
                phone_number = request.POST.get('nb'),
                is_male = gender,
                car_brand = request.POST.get('brand'),
                car_type = request.POST.get('carType'),
                battery_range = request.POST.get('bRange'),
                has_card = False,
                license = upload,
            )
            member.save()
        return redirect('/')


def view_product_list(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'homePage/productList.html', context=context)


def product_details(request, product_id):
    context = {
        'product': Product.objects.filter(id=product_id)[0]
    }
    return render(request, 'homePage/productDetails.html', context=context)

"""@never_cache
def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/SignUp.html', {'form': form})"""

