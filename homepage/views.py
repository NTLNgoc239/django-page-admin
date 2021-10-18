
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from .forms import StoreForm, CreateUserForm, FilterForm, AddStoreForm, UpdateStoreForm
from django.db.models import Q
from django.views.generic import ListView
import datetime
from .decorations import unauthenticated_user, allowed_users
import json


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'login/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # if remember_me == True:
            #     request.session.set_expiry(0)
            return redirect('home')
        else:
            messages.info(request, 'email or password is incorrect')

    context = {}
    return render(request, 'login/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'login/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
    context = {}
    return render(request, 'login/register.html', context)


@login_required(login_url='login')
def home(request):
    stores = Store.objects.all()
    total_stores = stores.count()
    context = {'stores': stores,
               'total_stores': total_stores}
    return render(request, 'login/dashboard.html', context)


@login_required(login_url='login')
def stores(request):
    stores = Store.objects.all()

    print(stores)
    return render(request, 'login/stores.html', {'stores': stores})


@login_required(login_url='login')
def functionUser(request):
    stores = Store.objects.all()
    print(stores)

    return render(request, 'login/function_user.html', {'stores': stores})


def functionUser(request):
    from django.db import connection, transaction
    cursor = connection.cursor()

    query = f"""SELECT t1.auto_increment_id, t1.name,t3.name,t4.role from homepage_shop as t1 LEFT JOIN (homepage_user_of_shop as t2 CROSS JOIN homepage_user as t3 CROSS JOIN homepage_role_login as t4) ON (t2.cid_shop = t1.id_shop AND t3.id = t2.cid_user AND t4.cid_user = t2.cid_user);"""

    cursor.execute(query)

    results = cursor.fetchall()
    jsonObj = json.dumps(results)
    jsonArr = json.loads(jsonObj)

    context = {'results': jsonArr}

    return render(request, 'login/function_user.html', context)


@login_required(login_url='login')
def updateStore(request, pk):

    store = Store.objects.get(id=pk)
    form = UpdateStoreForm(instance=store)

    if request.method == 'POST':
        form = UpdateStoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'login/update_store.html', context)


@login_required(login_url='login')
def deleteStore(request, pk):
    store = Store.objects.get(id=pk)
    if request.method == "POST":
        store.delete()
        return redirect('/')

    context = {'item': store}
    return render(request, 'login/delete.html', context)


@login_required(login_url='login')
def addStore(request):
    form = AddStoreForm
    if request.method == 'POST':
        form = AddStoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

            # redirect('home') //redirect to any page you wish to send the user after registration
    context = {'form': form}
    # return render(request, 'login/store_form.html', context)
    return render(request, 'login/store_form.html', context)


@login_required(login_url='login')
def myview(request, **kwargs):
    form = AddStoreForm
    if request.method == 'POST':
        form = AddStoreForm(request.POST)
        if form.is_valid():
            # save and redirect to another url
            form.save()
            return redirect('home')
    context = {'form': form}
    if request.GET:
        return render(request, 'login/store_form.html', context)
