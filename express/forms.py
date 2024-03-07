
from django.contrib.auth.models import User
from django import forms
from . models import Hotel,Rating

       
class ReviewForm(forms.ModelForm):
    class Meta:
        model= Rating
        fields = ['rating','descrip']
         