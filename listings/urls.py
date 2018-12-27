# from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    path('', all_listings, name='all_listings'),
    path('<int:listing_id>', listing, name='listing'),
    path('search', search, name='search'),
    path('postlisting', login_required(PostListing.as_view()), name='postlisting')
]