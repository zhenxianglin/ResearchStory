from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    # 主页
    # path('index/', views.index, name='index'),

    url(r'^$', views.index, name='index'),

]
