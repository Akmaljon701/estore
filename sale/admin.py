from django.contrib import admin
from sale.models import Category, Product, Sale, Cart

admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(Cart)
admin.site.register(Sale)
