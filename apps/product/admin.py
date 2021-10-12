# apps/product/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.product.models import Category  

# Register your models here.

admin.site.register(Category)