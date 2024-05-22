from django.db import models
from parameter.models import *


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
    info = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.info} - {self.count}"
