from django.contrib.auth.models import User
from django import forms
from authapp.models import CoffeeShop

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name')

class CoffeeShopForm(forms.ModelForm):
    class Meta:
        model = CoffeeShop
        fields = ('name', 'logo' )