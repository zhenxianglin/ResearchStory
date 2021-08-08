from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
import random
import time
from Users.userform import RegisterForm, ProfileForm
from Users.models import User, Profile
from django.contrib.auth.forms import UserCreationForm
import hashlib
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def hash_code(s, salt='Mysite_project'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def logout_view(request):
    """log out the account"""
    logout(request)
    return HttpResponseRedirect(reverse("MainPage:index"))


def register(request):
    """register a new account"""
    if request.method != "POST":
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        message = 'Please check your information'
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1']
                                             )
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse("MainPage:index"))
    context = {"form": form}
    return render(request, 'Users/register.html', context)


@login_required
def profile_edit(request, user_id):
    """personal info editing"""
    user = User.objects.get(id=user_id)

    if Profile.objects.filter(user_id=user_id).exists():
        profile = Profile.objects.get(user_id=user_id)
    else:
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("You do not have permission to modify this user information.。")

        profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.age = profile_cd['age']
            profile.gender = profile_cd['gender']
            profile.last_name = profile_cd['last_name']
            profile.first_name = profile_cd['first_name']
            profile.bio = profile_cd['bio']

            if 'avatar' in request.FILES:
                profile.avatar = profile_cd["avatar"]

            profile.save()
            return HttpResponseRedirect(reverse("Users:edit", args=[user_id]))
            # return redirect("Users:edit", id=user_id)
        else:
            return render(request, "Fail/profile_fail.html")
            # return HttpResponse("The registration form is entered incorrectly. Please re-enter~")

    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = {'profile_form': profile_form,
                   'profile': profile,
                   'user': user}
        return render(request, 'Users/edit.html', context)
    else:
        return render(request, "Fail/post_get_fail.html")
        # return HttpResponse("Please use GET or POST to request data.")
