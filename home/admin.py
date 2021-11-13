from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'is_male', 'car_brand', 'car_type', 'battery_range', 'license', 'has_card')
    """def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""



admin.site.register(Member, MemberAdmin)