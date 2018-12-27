from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    # path('listings', listings, name='listings'),
    path('contactus', contactus, name='contactus'),
]