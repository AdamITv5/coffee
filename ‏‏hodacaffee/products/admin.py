from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']
    list_filter = ['category', 'price']
    search_fields = ['name', 'description']
    list_per_page = 20
    ordering = ['category', 'name']
