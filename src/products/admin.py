from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'is_digital']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)