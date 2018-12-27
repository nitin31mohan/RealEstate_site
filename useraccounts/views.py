from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from enquiries.models import Enquiry
from django.contrib.auth import login, authenticate, logout
from useraccounts.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import *
from listings.models import ListingModel
from enquiries.models import Enquiry
from .forms import *
from operator import attrgetter
from itertools import chain
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        messages.error(request, 'Alert message testing')
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')    
    else:
        form = UserForm()
    return render(request, 'useraccounts/signup.html', {'form': form})

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('/')
 
    if request.method == 'POST':
        messages.error(request, 'Alert message testing')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
 
        if user is not None:
            # correct username and password login the user
            login(request, user)
            pk = user.pk
            if user.is_seller == True:
                return redirect('/useraccounts/dashboard/' +str(pk))
            else:
                return redirect('/')
        else:
            messages.error(request, 'Error Invalid username/password')
 
    return render(request, 'useraccounts/login.html')

def userlogout(request):
    logout(request)
    messages.error(request, 'Alert message testing')
    return redirect('/')

# def dashboard(request):
#     user_enquiries = Enquiry.objects.order_by('-enquiry_date').filter(user_id=request.user.id)
#     context = {
#         'user_enquiries': user_enquiries
#     }
#     return render(request, 'useraccounts/dashboard.html', context)


class Dashboard(DetailView):
    template_name = 'useraccounts/dashboard.html'
    # queryset = UserModel.objects.all()      ### puts in the USERMODEL's fields as context
    context_object_name = 'object'

    def get_queryset(self):
        return UserModel.objects.all()

    def get_context_data(self, **kwargs):
        pk = self.request.user.pk
        context = super(Dashboard, self).get_context_data(**kwargs)
        user_details = UserModel.objects.get(pk=pk)
        queries_made = Enquiry.objects.get(enquirer_id = pk)
        # listing_details = ListingModel.objects.all()
        listing_details = user_details.account.all()            #'account' is the related-name in the ListingModel which connects it to UserModel
        context.update({
            'user_details':user_details,
            'listing_details':listing_details,
            'queries_made':queries_made,
        })
        
    # def get_context_data(self, **kwargs):
    #     context = super(Dashboard, self).get_context_data(**kwargs)
    #     context['key'] = value              ###put in the LISTINGS-POSTED/ENQUIRED-ABOUT fields as additional context
        return context                    ### this context can then be accessed using the 'key'-name

class UserUpdate(UpdateView):
    template_name = 'useraccounts/update.html'
    form_class = UserUpdateForm

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(UserModel, id=id_)