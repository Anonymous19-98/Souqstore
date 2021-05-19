from django.contrib import admin
from .models import Product, Category, Product_Alternative, Product_Accesories
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accesories)
