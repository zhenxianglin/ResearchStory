from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib import admin

from Users import views

app_name = 'Users'

urlpatterns = [

    # Login interface
    path('login/', LoginView.as_view(template_name='Users/login.html'), name='login')


]
