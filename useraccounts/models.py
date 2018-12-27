from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# import os

class UserModel(AbstractUser):
    # DEFAULT_DP_DIR = os.path.dirname(os.path.abspath(__file__))
    is_seller = models.BooleanField('Seller', default=False)
    description = models.TextField(blank=True)
    signup_date = models.DateTimeField(default=datetime.now, blank=True)
    user_profile_image = models.ImageField(upload_to='user/', null=True, blank=True, default='defaultDP.png')

    def get_absolute_url(self):
        return reverse('index')