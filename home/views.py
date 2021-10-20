from django.shortcuts import render, redirect
from django.http import HttpResponse
from .decorator import unauthenticated_user
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import json
from .models import *


@login_required(login_url="login")
def index(request):
    shops = Shop.objects.all()
    context = {"shops": shops}
    return render(request, "pages/shop/list_shop.html", context)


@unauthenticated_user
def loginUser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Email or password is incorrect")

    context = {}
    return render(request, "pages/accounts/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


def functionUser(request):
    from django.db import connection, transaction

    cursor = connection.cursor()

    query = f"""SELECT t1.id, t1.name,t3.name,t4.role from hc_shop as t1 LEFT JOIN (hc_users_of_shop as t2 CROSS JOIN users as t3 CROSS JOIN hc_role_login as t4) ON (t2.cid_shop = t1.id AND t3.id = t2.cid_user AND t4.user_id = t2.cid_user);"""

    cursor.execute(query)

    results = cursor.fetchall()
    jsonObj = json.dumps(results)
    jsonArr = json.loads(jsonObj)

    context = {"results": jsonArr}

    return render(request, "pages/shop/function_user.html", context)
