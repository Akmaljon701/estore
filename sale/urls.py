from django.urls import path
from sale.views import *

urlpatterns = [
    path('get/categories/', get_categories),
    path('get/products/', get_products),
]
