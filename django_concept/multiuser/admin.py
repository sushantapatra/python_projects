from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Category, Subcategory, Employee, Profile


class AdminSubcategory(admin.ModelAdmin):
    model = Subcategory
    list_display = ["name", 'category']
    list_filter = ["category",]


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = "employee"


class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline, ProfileInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory, AdminSubcategory)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
