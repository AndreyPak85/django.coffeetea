from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authapp.forms import UserForm, CoffeeShopForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



# Create your views here.
def auth(request):
    return render(request, 'auth.html', {})

def authapp_sign_up(request):
    user_form = UserForm()
    coffeeshop_form = CoffeeShopForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        coffeeshop_form = CoffeeShopForm(request.POST, request.FILES)
        if user_form.is_valid() and coffeeshop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_coffeeshop = coffeeshop_form.save(commit=False)
            new_coffeeshop.user = new_user
            new_coffeeshop.save()
            user = authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            )
            login(request, user)
            return redirect(auth)

    return render(request, 'sign_up.html', {
        'user_form': user_form,
        'coffeeshop_form': coffeeshop_form,
    })

