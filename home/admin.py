from django.contrib import admin
from .models import Member, Product,Station

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'is_male', 'car_brand', 'car_type', 'battery_range', 'license', 'has_card')
    
    """def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""
        
    list_filter = ("has_card",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'socket_type', 'number_of_sockets', 'charging_power', 'protection', 'ware_number', 'category', 'price', 'code')


class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'Available_Charger', 'number_of_sockets')


admin.site.register(Member, MemberAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Station, StationAdmin)