from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Users


@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "mobile", "is_staff")
