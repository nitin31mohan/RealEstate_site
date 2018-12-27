from django.db import models
from useraccounts.models import UserModel
from datetime import datetime

class ListingModel(models.Model):
    account = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True, related_name='account')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=2)
    photo_main = models.ImageField(upload_to='properties', blank=True, default='')
    photo_1 = models.ImageField(upload_to='properties', blank=True)
    photo_2 = models.ImageField(upload_to='properties/', blank=True)
    photo_3 = models.ImageField(upload_to='properties/', blank=True)
    photo_4 = models.ImageField(upload_to='properties/', blank=True)
    photo_5 = models.ImageField(upload_to='properties/', blank=True)
    photo_6 = models.ImageField(upload_to='properties/', blank=True)
    rented = models.BooleanField(default=False)
    posting_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name