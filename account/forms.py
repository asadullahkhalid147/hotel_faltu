
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class sinup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username' , 'email', 'password1', 'password2']
       
       
class userProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name','last_name','email']
        
    
   
class sigin_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())