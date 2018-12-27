from django.urls import path
from django.views.generic import TemplateView
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('userlogin', userlogin, name='userlogin'),
    # path('userlogin', 'django.contrib.auth.views.login', {'template_name': 'useraccounts/login.html'}),
    path('register', register, name='register'),
    path('userlogout', userlogout, name='userlogout'),
    path('dashboard/<int:pk>', login_required(Dashboard.as_view()), name='dashboard'),
    path('userupdate/<int:pk>', login_required(UserUpdate.as_view()), name='update'),
]