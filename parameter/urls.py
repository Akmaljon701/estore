from django.urls import path
from parameter.views import *

urlpatterns = [
    path('get/GPU/all/', get_gpus),
    path('get/CPU/all/', get_cpus),
    path('get/RAM/all/', get_rams),
]
