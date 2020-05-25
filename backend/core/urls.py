from django.urls import path

from core.views import *

urlpatterns = [
    path('cars/', all_cars, name='cars'),
]