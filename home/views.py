from django.shortcuts import render, redirect
from django.http import HttpResponse
from .decorator import unauthenticated_user
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import *

@login_required(login_url='login')
def index(request):
    shops = Shop.objects.all()
    context = {'shops': shops}
    return render(request, 'pages/shop/list_shop.html', context)

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Email or password is incorrect')

    context = {}
    return render(request, 'pages/accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')