from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
import random
import time
from Users.userform import RegisterForm, LoginFom
from Users.models import User
from django.contrib.auth.forms import UserCreationForm
import hashlib


def hash_code(s, salt='Mysite_project'):
    h = hashlib.sha256()
    s += salt
    # update方法只接受bytes类型
    h.update(s.encode())
    return h.hexdigest()


def logout_view(request):
    """log out the account"""
    logout(request)
    return HttpResponseRedirect(reverse("MainPage:index"))


def register(request):
    """register a new account"""
    # if request == "POST":
    #     form = RegisterForm()
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password1 =form.cleaned_data.get('password1')
    #         new_user =authenticate(username=username, password = raw_password1)
    #         login(request, new_user)
    #         return HttpResponseRedirect(reverse("MainPage:index"))
    #     else:
    #         print(form.errors)
    # else:
    #     form = RegisterForm()
    #
    # return render(request, 'Users/register.html', context = {"form": form})

    if request.method != "POST":

        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        message = 'Please check your information'
        # 获取数据
        if form.is_valid():
            new_user = form.save()

            authenticate_user = authenticate( username=new_user.username,
                                             password=request.POST['password1']
                                             )
            login(request, authenticate_user)

            return HttpResponseRedirect(reverse("MainPage:index"))

    context = {"form": form}

    return render(request, 'Users/register.html', context)
