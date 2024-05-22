from django.db import models


class RAM(models.Model):
    RAM = models.CharField(max_length=50)

    def __str__(self):
        return self.RAM


class GPU(models.Model):
    GPU = models.CharField(max_length=50)

    def __str__(self):
        return self.GPU


class CPU(models.Model):
    CPU = models.CharField(max_length=50)

    def __str__(self):
        return self.CPU
