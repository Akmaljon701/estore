from django.contrib import admin
from parameter.models import GPU, CPU, RAM

admin.site.register(GPU)
admin.site.register(CPU)
admin.site.register(RAM)
