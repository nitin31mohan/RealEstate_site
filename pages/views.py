from django.shortcuts import render
from django.http import HttpResponse
from listings.models import ListingModel
from listings.choices import (
    state_choices, 
    bedroom_choices, 
    bathroom_choices, 
    garage_choices, 
    price_choices
)

def index(request):
    listings = ListingModel.objects.order_by('-posting_date').filter(rented=False)[:3]
    context={
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'bathroom_choices':bathroom_choices,
        'garage_choices':garage_choices,
        'price_choices':price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

# def listings(request):
#     return render(request, 'pages/listings.html')

def contactus(request):
    return render(request, 'pages/contactus.html')