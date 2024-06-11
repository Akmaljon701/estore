from django.db import models
from parameter.models import *
from user.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    CPU = models.ForeignKey(CPU, on_delete=models.PROTECT, blank=True, null=True)
    GPU = models.ForeignKey(GPU, on_delete=models.PROTECT, blank=True, null=True)
    RAM = models.ForeignKey(RAM, on_delete=models.PROTECT, blank=True, null=True)
    OS = models.CharField(max_length=50)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    photo_url = models.CharField(max_length=200)
    info = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.info} - {self.count}"


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_carts', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='product_carts', blank=True)

    def __str__(self):
        return f"{self.user}"


class Sale(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_sales', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='product_sales')
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=[
        ('in_progress', 'in_progress'),
        ('completed', 'completed'),
        ('canceled', 'canceled')
    ], default='in_progress')

    def __str__(self):
        return f"{self.user} - {self.status}"
