from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def auth(request):
    return redirect(auth_home)

@login_required(login_url='/authapp/login')
def auth_home(request):
    return render(request, 'auth.html', {})
