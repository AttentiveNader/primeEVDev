from django.db import models
from django.core.exceptions import ValidationError



# Create your models here.

class Member(models.Model):
    def validate_battery_range(value):
        if value < 50 or value > 600:  # Your conditions here
            raise ValidationError('Battery Range is out of range')

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=255, unique=True, primary_key=True)
    phone_number = models.CharField(max_length=11, null=False)
    is_male = models.BooleanField(null=False)
    car_brand = models.CharField(max_length=50, null=False)
    car_type = models.CharField(max_length=50, null=False)
    battery_range = models.PositiveIntegerField(validators=[validate_battery_range])
    has_card = models.BooleanField(null=False, default=False)
    license = models.ImageField(upload_to='images/license')
    
    
class Product(models.Model):
    image = models.ImageField(upload_to='images/product')
    name = models.CharField(max_length=50, null=True, default="Not Working")
    description = models.TextField(max_length=1000, null=False)
    socket_type = models.CharField(max_length=50, null=False)
    number_of_sockets = models.IntegerField()
    charging_power = models.IntegerField()
    protection = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    code = models.CharField(unique=True, max_length=100)
    ware_number = models.CharField(unique=True, max_length=100)
    
    
class Station(models.Model):
    image = models.ImageField(upload_to='images/station')
    name = models.CharField(max_length=50, null=True, default="out of service")
    Available_Charger = models.CharField(max_length=50, null=False)
    number_of_sockets = models.IntegerField()