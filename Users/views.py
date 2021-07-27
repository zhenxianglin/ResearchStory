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
    # update方法只接受bytes类型
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
        # 获取数据
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1']
                                             )
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse("MainPage:index"))
    context = {"form": form}
    return render(request, 'Users/register.html', context)

@login_required(login_url='/userprofile/login/')
def profile_edit(request, id):
    user = User.objects.get(id=id)

    # 旧教程代码
    # profile = Profile.objects.get(user_id=id)
    # 新教程代码： 获取 Profile
    if Profile.objects.filter(user_id=id).exists():
        # user_id 是 OneToOneField 自动生成的字段
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create(user=user)


    if request.method == 'POST':
        # 验证修改数据者，是否为用户本人
        if request.user != user:
            return HttpResponse("You do not have permission to modify this user information.。")

        # 上传的文件保存在 request.FILES 中，通过参数传递给表单类
        profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            # 取得清洗后的合法数据
            profile_cd = profile_form.cleaned_data
            profile.age = profile_cd['age']
            profile.gender = profile_cd['gender']
            profile.last_name = profile_cd['last_name']
            profile.first_name = profile_cd['first_name']
            profile.bio = profile_cd['bio']

            # 如果 request.FILES 存在文件，则保存
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd["avatar"]

            profile.save()
            # 带参数的 redirect()
            return redirect("userprofile:edit", id=id)
        else:
            return HttpResponse("The registration form is entered incorrectly. Please re-enter~")

    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = { 'profile_form': profile_form, 'profile': profile, 'user': user }
        return render(request, 'Users/edit.html', context)
    else:
        return HttpResponse("Please use GET or POST to request data.")



#
# @login_required
# def profile_edit(request, id):
#     user = User.objects.get(id=id)
#     # profile = Profile.objects.get(user_id=id)
#     if Profile.objects.filter(user_id=id).exists():
#         profile = Profile.objects.get(user_id=id)
#     else:
#         profile = Profile.objects.create(user=user)
#
#     if request.method == 'POST':
#         if request.user != user:
#             return HttpResponse("You do not have permission to modify this user information.")
#         # 上传的文件保存在 request.FILES 中，通过参数传递给表单类
#         profile_form = ProfileForm(request.POST, request.FILES)
#
#         if profile_form.is_valid():
#             # 取得清洗后的合法数据
#
#             profile_cd = profile_form.cleaned_data
#
#             # profile.age = profile_cd['age']
#             # profile.gender = profile_cd['gender']
#             # profile.last_name = profile_cd['last_name']
#             # profile.first_name = profile_cd['first_name']
#             profile.bio = profile_cd['bio']
#
#             # # 如果 request.FILES 存在文件，则保存
#             if 'avatar' in request.FILES:
#                 profile.avatar = profile_cd['avatar']
#
#             profile.save()
#             return HttpResponseRedirect(reverse('Users:edit',args=[id]))
#         else:
#             return HttpResponse("The registration form is entered incorrectly. Please re-enter~")
#
#     elif request.method == 'GET':
#         profile_form = ProfileForm()
#         context = {
#             'profile_form': profile_form,
#             'profile': profile,
#             'user': user,
#         }
#         return render(request, 'Users/edit.html', context)
#     else:
#         return HttpResponse("Please use GET or POST to request data.")
