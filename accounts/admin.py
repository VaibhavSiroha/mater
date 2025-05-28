from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

class CustomUserAdmin(UserAdmin):
    model = Users
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'age', 'gender', 'location', 'profile_pic')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'age', 'gender', 'location', 'profile_pic')}),
    )

admin.site.register(Users, CustomUserAdmin)