from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.html import format_html

from .models import Products, Category, Customer, Order, Subcategory
# Register your models here.

# Model Configuration in admin site


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'view_image']

    def view_image(self, obj):
        return format_html(f"<img src='{obj.image.url}' name='{obj.name}' width='50' height='50' class='rounded rounded-lg'/>")


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'password']


class AdminOrder(admin.ModelAdmin):
    list_display = ['customer_name', 'product_name',
                    'quantity', 'price', 'total_price', 'create_date', 'status']

    def customer_name(self, obj):
        return obj.customer

    def product_name(self, obj):
        return obj.product

    def total_price(self, obj):
        return obj.quantity * obj.price

    def order_status(self, obj):
        return "Completed" if obj.status is True else "Inprogress"


admin.site.register(Products, AdminProduct)
# admin.site.register(Products)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
admin.site.register(Subcategory)
