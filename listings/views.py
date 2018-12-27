from django.shortcuts import render, get_object_or_404
from .models import ListingModel
from useraccounts.models import UserModel
from .forms import ListingForm
from django.views.generic import CreateView
from .decorator import seller_authenticate
from django.utils.decorators import method_decorator
from django.core.paginator import (
    EmptyPage, 
    PageNotAnInteger, 
    Paginator
)
from listings.choices import (
    state_choices, 
    bedroom_choices, 
    bathroom_choices, 
    garage_choices, 
    price_choices
)

# Create your views here.
def all_listings(request):
    listings = ListingModel.objects.order_by('-posting_date').filter(rented=False)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, 'listings/all_listings.html', {'listings': paged_listings,})

def listing(request, listing_id):
    single_listing = get_object_or_404(ListingModel, pk=listing_id)
    context = {
        'single_listing':single_listing,
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = ListingModel.objects.order_by('-posting_date')

    if 'keywords' in request.GET:       # searching for keyword in description
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)       ## contains, not exact; i => case-insensitive
    
    if 'city' in request.GET:           # searching for city
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)     ## exact reqd; i=> case-insensitive

    if 'state' in request.GET:           # searching for city
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)     ## exact reqd; i=> case-insensitive
    
    if 'bedrooms' in request.GET:           # searching UPTO bedrooms
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)     ## lte => less-than-or-equal
    
    if 'bathrooms' in request.GET:           # searching UPTO bathrooms
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            queryset_list = queryset_list.filter(bathrooms__lte=bathrooms)     ## lte => less-than-or-equal
    
    if 'price' in request.GET:           # searching for city
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)     ## lte => less-than-or-equal


    context = {
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'bathroom_choices':bathroom_choices,
        'garage_choices':garage_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values':request.GET,
    }
    return render(request, 'listings/search.html', context)

@method_decorator(seller_authenticate, name='dispatch')
class PostListing(CreateView):
    model = ListingModel
    form_class = ListingForm
    template_name = 'listings/post_listing.html'
    success_url = "/listings"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.account = self.request.user
        self.object.save()
        return super(PostListing, self).form_valid(form)