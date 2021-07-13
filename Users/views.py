from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect

import random
import time

from .models import User


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        username = request.POST.get('username')
        age = request.POST.get('age')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        gender = request.POST.get('gender')
        e_mail = request.POST.get('e_mail')
        password = make_password(request.POST.get('password'))

        User.objects.create(username=username,
                            age=age,
                            last_name=last_name,
                            first_name=first_name,
                            gender=gender,
                            e_mail=e_mail,
                            password=password)
        return HttpResponseRedirect("/Users/login/")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exist():
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                ticket = ''
                for i in range(15):
                    s = "zxcvbnmlkjhgfdsaqwertyuiop"
                    ticket += random.choice(s)
                current_time = str(int(time.time()))
                ticket = 'TICKET' + ticket + current_time

                response = HttpResponseRedirect("/MainPage/index")
                response.set_cookie("ticket", ticket, max_age=10000)
                user.ticket = ticket
                user.save()
                return response
            else:
                return render(request, "login.html", {'password': "Wrong password."})
        else:
            return render(request, 'login.html', {'username': 'Username does not exist.'})


def logout(request):
    if request.method == "GET":
        response = HttpResponseRedirect("/MainPage/login")
        response.delete_cookie("ticket")
        return response


