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
    license = models.ImageField(upload_to='images/')
