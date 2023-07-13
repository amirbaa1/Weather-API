from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeWeather, name='home'),
    path('search=', search_city, name='search')
]
