from django import forms
from .models import ListingModel

class ListingForm(forms.ModelForm):
    class Meta:
        model = ListingModel
        exclude = ['account', 'posting_date']