from django.urls import path
from sale.views import *

urlpatterns = [
    path('get/categories/', get_categories),
    path('get/products/', get_products),
    path('add_product_to_cart/', user_add_product_to_cart),
    path('remove_product_from_cart/', user_remove_product_from_cart),
    path('user_get_cart/', user_get_cart),
    path('user_sale/', user_sale),
]
